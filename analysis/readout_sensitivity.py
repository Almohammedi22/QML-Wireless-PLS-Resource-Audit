#!/usr/bin/env python3
"""Reproduce output-mapping sensitivity and loss tails in Section IX and S-V.

The target beamformer is an oracle supplied by a generalized eigensolver.
This tests measurement-only costs, not a trained model or physical device.
Rescaling changes the target quantum expectation values before measurement;
rescaling already noisy classical samples cannot obtain the same improvement.

Run beside resource_analysis_miso_wiretap.py:
  OPENBLAS_NUM_THREADS=1 python readout_sensitivity.py --output readout_sensitivity.json
"""
import argparse
import importlib.util
import json
import math
import platform
from pathlib import Path

import numpy as np
import scipy


def load_base():
    path = Path(__file__).with_name('resource_analysis_miso_wiretap.py')
    spec = importlib.util.spec_from_file_location('resource_analysis', path)
    base = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(base)
    return base


def losses(data, vector, snr=10):
    hb, he, _, cap, _, _ = data
    vector = vector / np.linalg.norm(vector, axis=1, keepdims=True)
    rb = snr * np.abs(np.sum(hb.conj() * vector, axis=1)) ** 2
    re = snr * np.abs(np.sum(he.conj() * vector, axis=1)) ** 2
    rate = np.maximum(np.log2(1 + rb) - np.log2(1 + re), 0)
    return (cap - rate) / cap


def gaussian_threshold(data, target=.05, exact_variance=False, rho=0):
    _, _, w, _, z, scale = data
    means = w / scale
    sr = np.sqrt(np.maximum(1 - means.real**2, 0)) if exact_variance else 1
    si = np.sqrt(np.maximum(1 - means.imag**2, 0)) if exact_variance else 1
    zr, zi = z.real, z.imag
    if rho:
        shared = np.random.default_rng(99001).normal(size=(len(w), 1))
        zr = math.sqrt(1-rho)*zr + math.sqrt(rho)*shared
        zi = math.sqrt(1-rho)*zi + math.sqrt(rho)*shared
    error = scale * (sr * zr + 1j * si * zi)
    lo, hi = 10., 1e8
    for _ in range(60):
        mid = math.sqrt(lo * hi)
        if losses(data, w + error/math.sqrt(mid)).mean() <= target:
            hi = mid
        else:
            lo = mid
        if hi / lo < 1.0001:
            break
    return hi


def binomial_check(data, shots, repetitions=20, seed=7113):
    _, _, w, _, _, scale = data
    means = w / scale
    rng = np.random.default_rng(seed)
    samples = []
    for _ in range(repetitions):
        real = 2*rng.binomial(shots, np.clip((1+means.real)/2, 0, 1))/shots - 1
        imag = 2*rng.binomial(shots, np.clip((1+means.imag)/2, 0, 1))/shots - 1
        samples.append(losses(data, real + 1j*imag))
    samples = np.array(samples)
    channel_means = samples.mean(axis=0)
    se = float(channel_means.std(ddof=1) / math.sqrt(len(w)))
    mean = float(samples.mean())
    return {
        'shots': shots, 'repetitions': repetitions, 'mean_loss': mean,
        'approx_95pct_mean_interval': [mean-1.96*se, mean+1.96*se],
        'loss_95th_percentile': float(np.quantile(samples, .95)),
        'fraction_loss_above_10pct': float(np.mean(samples > .10)),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--trials', type=int, default=2000)
    parser.add_argument('--output', type=Path, default=Path('readout_sensitivity.json'))
    args = parser.parse_args()
    base = load_base()
    out = {
        'model': 'oracle beamformer, idealized product-state readout; G=1',
        'snr_db': 10, 'trials': args.trials, 'reference_seed': 1234,
        'additional_seeds': list(range(1, 11)),
        'software': {'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__},
        'coherence_times_ms': {f'{f}GHz_{v}kmh': 1000*base.coherence_time(f, v) for f,v in base.SCENARIOS},
        'results': [],
    }
    for nt in (4, 16, 64):
        model = base.ShotModel(nt, 10, args.trials, 1234)
        rows = {}
        for mapping in ('direct', 'rescaled'):
            data = model.readout_arrays(mapping)
            w, scale = data[2], data[5]
            means = w / scale
            recovered = means / np.linalg.norm(means, axis=1, keepdims=True)
            assert np.max(np.abs(recovered-w)) < 1e-12
            assert np.max(np.abs(means.real)) <= 1+1e-12
            assert np.max(np.abs(means.imag)) <= 1+1e-12
            assert np.max(np.abs(losses(data, recovered))) < 1e-10
            s5 = gaussian_threshold(data)
            assert abs(s5-model.threshold(.05, mapping=mapping))/s5 < 1e-10
            s1 = gaussian_threshold(data, target=.01)
            sample = losses(data, w+scale*data[4]/math.sqrt(s5))
            rounded, _ = base.two_sig(s5)
            rounded = int(round(rounded))
            row = {
                'nt': nt, 'mapping': mapping, 'shots_5pct': s5,
                'shots_1pct': s1, 'rounded_shots_5pct': rounded,
                'gaussian_loss_mean': float(sample.mean()),
                'gaussian_loss_95th_percentile': float(np.quantile(sample, .95)),
                'gaussian_fraction_loss_above_10pct': float(np.mean(sample > .10)),
                'exact_variance_threshold': gaussian_threshold(data, exact_variance=True),
                'correlated_exact_variance_thresholds': {str(rho): gaussian_threshold(data, exact_variance=True, rho=rho) for rho in (.25, .5)},
                'binomial_at_unrounded_budget': binomial_check(data, math.ceil(s5)),
                'binomial_at_rounded_budget': binomial_check(data, int(rounded)),
                'other_seed_thresholds': [],
                'measurement_times_ms': {str(us): rounded*us/1000 for us in (10,100,1000)},
            }
            rows[mapping] = row
        for seed in range(1, 11):
            other = base.ShotModel(nt, 10, args.trials, seed)
            for mapping in rows:
                rows[mapping]['other_seed_thresholds'].append(gaussian_threshold(other.readout_arrays(mapping)))
        for row in rows.values():
            row['other_seed_min'] = min(row['other_seed_thresholds'])
            row['other_seed_max'] = max(row['other_seed_thresholds'])
            out['results'].append(row)
            print(json.dumps({k:row[k] for k in ('nt','mapping','shots_5pct','shots_1pct','gaussian_loss_95th_percentile','other_seed_min','other_seed_max')}), flush=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2)+'\n')


if __name__ == '__main__':
    main()
