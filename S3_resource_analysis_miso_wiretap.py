#!/usr/bin/env python3
"""
Resource analysis for a representative secrecy problem (Section IX).

This script reproduces Tables 13 and 14 of the manuscript. It estimates how many
measurement shots a quantum model would need to output a near-optimal secrecy
beamformer for the MISO wiretap channel, and compares the resulting inference time
with the channel coherence time.

Model
    A transmitter with Nt antennas serves one single-antenna receiver in the presence
    of one single-antenna eavesdropper. The secrecy-optimal beamformer is known in
    closed form: it is the principal generalized eigenvector of the pencil
    (I + P h_B h_B^H, I + P h_E h_E^H), and the secrecy capacity is the base-2
    logarithm of the corresponding generalized eigenvalue (Khisti and Wornell, 2010).

Assumptions
    A1  Training is perfect. Only finite-shot readout error is modelled.
    A2  The readout is an abstract wide-output model: each of the 2*Nt real
        beamformer components is one Pauli-Z expectation on its own qubit, so all
        outputs are estimated from the same S-shot record.
    A3  Each output estimate carries independent zero-mean Gaussian error with
        standard deviation 1/sqrt(S), the worst case for an observable in [-1, 1].
    A4  The global phase of the optimal beamformer is fixed before the readout
        error is added, and the perturbed vector is renormalized before use.
    A5  The per-shot execution time is an input, not a device specification.
        Compilation, queueing, data transfer and synchronization are excluded.
    A6  A register with n_o < 2*Nt measured qubits would need
        G >= ceil(2*Nt / n_o) measurement groups, multiplying both the shot budget
        and the latency by G. The results below are for G = 1.

Method
    The loss is the relative shortfall of the achieved secrecy rate below the
    closed-form secrecy capacity, averaged over independent Rayleigh channel draws.
    The same channel draws and unit-variance noise draws are reused for every
    candidate shot budget, and the smallest budget meeting each loss target is found
    by bisection on a logarithmic scale.

Usage
    python S3_resource_analysis_miso_wiretap.py --selftest
    python S3_resource_analysis_miso_wiretap.py

Defaults: Nt = 4, 16, 64; 2000 channel draws; seed 1234; SNR 10 dB.
Requirements: Python 3, numpy, scipy.
"""
import argparse
import math
from decimal import Decimal, ROUND_HALF_UP

import numpy as np
from scipy.linalg import eigh

SPEED_OF_LIGHT = 299_792_458.0
SCENARIOS = ((3.5, 3), (3.5, 60), (28, 3), (28, 60))     # carrier GHz, speed km/h


def secrecy_rate(w, h_b, h_e, snr):
    gain_b = snr * abs(np.vdot(h_b, w)) ** 2
    gain_e = snr * abs(np.vdot(h_e, w)) ** 2
    return max(math.log2(1.0 + gain_b) - math.log2(1.0 + gain_e), 0.0)


def optimal_beamformer(h_b, h_e, snr):
    eye = np.eye(h_b.size, dtype=complex)
    vals, vecs = eigh(eye + snr * np.outer(h_b, h_b.conj()),
                      eye + snr * np.outer(h_e, h_e.conj()))
    w = vecs[:, -1]
    w = w / np.linalg.norm(w)
    # The eigensolver leaves the global phase arbitrary, and it can differ between
    # library builds. Fixing it (largest entry real and positive) makes the added
    # readout noise, and therefore every result, independent of the library.
    k = int(np.argmax(np.abs(w)))
    w = w * np.exp(-1j * np.angle(w[k]))
    return w, max(math.log2(vals[-1].real), 0.0)


def rayleigh(rng, nt):
    return (rng.normal(size=nt) + 1j * rng.normal(size=nt)) / math.sqrt(2)


def selftest(seed=0):
    """The closed-form beamformer must beat every randomly drawn beamformer."""
    rng = np.random.default_rng(seed)
    worst = 0.0
    for nt in (2, 4, 8):
        for _ in range(200):
            h_b, h_e = rayleigh(rng, nt), rayleigh(rng, nt)
            w_opt, cap = optimal_beamformer(h_b, h_e, 10.0)
            assert abs(secrecy_rate(w_opt, h_b, h_e, 10.0) - cap) < 1e-9
            for _ in range(60):
                w = rng.normal(size=nt) + 1j * rng.normal(size=nt)
                worst = max(worst, secrecy_rate(w / np.linalg.norm(w), h_b, h_e, 10.0) - cap)
    assert worst < 1e-9, f'a random beamformer beat the optimum by {worst:.2e}'
    print(f'Self-test passed (largest excess of a random beamformer over the optimum: {worst:.2e})')


class ShotModel:
    def __init__(self, nt, snr, trials, seed):
        rng = np.random.default_rng(seed)
        self.snr, self.cases = snr, []
        for _ in range(trials):
            h_b, h_e = rayleigh(rng, nt), rayleigh(rng, nt)
            w_opt, cap = optimal_beamformer(h_b, h_e, snr)
            if cap > 1e-6:
                self.cases.append((h_b, h_e, w_opt, cap, rng.normal(size=nt) + 1j * rng.normal(size=nt)))

    def mean_loss(self, shots):
        sigma = 1.0 / math.sqrt(shots)
        total = 0.0
        for h_b, h_e, w_opt, cap, z in self.cases:
            w = w_opt + sigma * z
            w /= np.linalg.norm(w)
            total += (cap - secrecy_rate(w, h_b, h_e, self.snr)) / cap
        return total / len(self.cases)

    def threshold(self, target, lo=1e1, hi=1e8):
        for _ in range(60):
            mid = math.sqrt(lo * hi)
            lo, hi = (lo, mid) if self.mean_loss(mid) <= target else (mid, hi)
            if hi / lo < 1.0001:
                break
        return hi


def coherence_time(carrier_ghz, speed_kmh):
    doppler = (speed_kmh / 3.6) * carrier_ghz * 1e9 / SPEED_OF_LIGHT
    return 0.423 / doppler


def two_sig(x):
    e = math.floor(math.log10(x))
    v = (Decimal(repr(x)) / Decimal(10) ** e).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
    if v >= 10:
        v, e = (v / 10).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP), e + 1
    return float(v) * 10 ** e, f'{v}e{e}'


def main():
    p = argparse.ArgumentParser(description='Reproduces Tables 13 and 14 of the manuscript.')
    p.add_argument('--selftest', action='store_true')
    p.add_argument('--nt', type=int, nargs='+', default=[4, 16, 64])
    p.add_argument('--trials', type=int, default=2000)
    p.add_argument('--seed', type=int, default=1234)
    p.add_argument('--snr-db', type=float, default=10.0)
    a = p.parse_args()
    if a.selftest:
        selftest()
        return

    snr = 10 ** (a.snr_db / 10)
    budgets = {}
    print(f'Table 13: shots per inference (SNR {a.snr_db} dB, {a.trials} draws, seed {a.seed})')
    print(f'{"Nt":>4} {"<=5% loss":>20} {"<=1% loss":>20} {"time":>8} {"inference/coherence":>22}')
    for nt in a.nt:
        model = ShotModel(nt, snr, a.trials, a.seed)
        s5, s1 = model.threshold(0.05), model.threshold(0.01)
        (b5, t5), (_, t1) = two_sig(s5), two_sig(s1)
        budgets[nt] = b5
        time_s = b5 * 100e-6
        ratios = [time_s / coherence_time(f, v) for f, v in SCENARIOS]
        print(f'{nt:>4} {s5:>10.1f} ({t5:>6}) {s1:>10.1f} ({t1:>6}) {time_s * 1e3:>6.0f} ms '
              f'{min(ratios):>10.1f} to {max(ratios):.0f}')

    print('\nTable 14: sensitivity to the assumed per-shot time')
    for nt, b5 in budgets.items():
        for t_us in (10, 100, 1000):
            time_s = b5 * t_us * 1e-6
            ratios = [time_s / coherence_time(f, v) for f, v in SCENARIOS]
            lo = f'{min(ratios):.2f}' if min(ratios) < 1 else f'{min(ratios):.1f}'
            ms = f'{time_s * 1e3:.1f}' if time_s * 1e3 < 10 else f'{time_s * 1e3:.0f}'
            print(f'  Nt={nt:<3} {t_us:>5} us per shot: {ms:>7} ms, {lo} to {max(ratios):.0f} x coherence time')

    print('\nCoherence times, 0.423/f_d:', ', '.join(
        f'{f} GHz at {v} km/h = {coherence_time(f, v) * 1e3:.3f} ms' for f, v in SCENARIOS))


if __name__ == '__main__':
    main()
