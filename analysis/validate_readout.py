#!/usr/bin/env python3
"""Validate the Section IX abstraction; no learned or hardware circuit is claimed.

Run beside resource_analysis_miso_wiretap.py:
  OPENBLAS_NUM_THREADS=1 python validate_readout.py --output readout_validation.json

The exact binomial check is equivalent to independent Pauli-Z measurements of
2*Nt product-state qubits with means equal to the real beamformer components.
It validates finite-shot readout only; preparation of an optimal beamformer is
an oracle assumption, not a proposed learning algorithm. The correlated Gaussian
case is an illustrative covariance sensitivity, not a hardware noise model.
"""
import argparse, importlib.util, json, math
from pathlib import Path
import numpy as np

def load_base(path):
 spec=importlib.util.spec_from_file_location('base_analysis',path)
 module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
 return module

def arrays(model):
 hb,he,w,cap,z=map(np.array,zip(*model.cases))
 return hb,he,w,cap,z

def losses(data, w):
 hb,he,_,cap,_=data
 w=w/np.linalg.norm(w,axis=-1,keepdims=True)
 rb=10*np.abs(np.sum(hb.conj()*w,axis=-1))**2
 re=10*np.abs(np.sum(he.conj()*w,axis=-1))**2
 rates=np.maximum(np.log2(1+rb)-np.log2(1+re),0)
 return (cap-rates)/cap

def threshold(data, exact_variance=False, correlation=0, seed=99001):
 _,_,w,_,z=data
 sig_r=np.sqrt(np.maximum(1-w.real**2,0)) if exact_variance else np.ones(w.shape)
 sig_i=np.sqrt(np.maximum(1-w.imag**2,0)) if exact_variance else np.ones(w.shape)
 zr,zi=z.real,z.imag
 if correlation:
  shared=np.random.default_rng(seed).normal(size=(len(w),1))
  zr=np.sqrt(1-correlation)*zr+np.sqrt(correlation)*shared
  zi=np.sqrt(1-correlation)*zi+np.sqrt(correlation)*shared
 err=sig_r*zr+1j*sig_i*zi
 lo,hi=10.,1e8
 for _ in range(60):
  mid=math.sqrt(lo*hi)
  if float(np.mean(losses(data,w+err/math.sqrt(mid))))<=.05:hi=mid
  else:lo=mid
  if hi/lo<1.0001:break
 return hi

def binomial(data,shots,repetitions=20,seed=7113):
 w=data[2];rng=np.random.default_rng(seed);results=[]
 for _ in range(repetitions):
  real=2*rng.binomial(shots,np.clip((1+w.real)/2,0,1))/shots-1
  imag=2*rng.binomial(shots,np.clip((1+w.imag)/2,0,1))/shots-1
  results.append(losses(data,real+1j*imag))
 vals=np.array(results);per_channel=np.mean(vals,axis=0)
 # Channel draws are the independent units; repeats reduce measurement noise.
 mean=float(vals.mean());se=float(per_channel.std(ddof=1)/np.sqrt(len(per_channel)))
 return {'shots':shots,'repetitions':repetitions,'mean_loss':mean,'channel_standard_error':se,
         'approx_95pct_interval':[mean-1.96*se,mean+1.96*se]}

def main():
 p=argparse.ArgumentParser();p.add_argument('--base',type=Path,default=Path(__file__).with_name('resource_analysis_miso_wiretap.py'));p.add_argument('--output',type=Path,default=Path('readout_validation.json'));p.add_argument('--trials',type=int,default=2000);a=p.parse_args()
 base=load_base(a.base);out={'snr_db':10,'trials':a.trials,'reference_seed':1234,'other_seeds':list(range(1,11)),'model':'idealized wide-output measurement, one real component per qubit','results':[]}
 for nt in [4,16,64]:
  d=arrays(base.ShotModel(nt,10,a.trials,1234));s=threshold(d);sv=threshold(d,True)
  other=[]
  for seed in range(1,11):other.append(threshold(arrays(base.ShotModel(nt,10,a.trials,seed))))
  rounded,_=base.two_sig(s)
  result={'nt':nt,'gaussian_threshold':s,'other_seed_thresholds':other,'seed_min':min(other),'seed_max':max(other),'exact_variance_threshold':sv,'variance_change_percent':100*(sv/s-1),'binomial_at_unrounded_threshold':binomial(d,math.ceil(s)),'binomial_at_table_budget':binomial(d,int(rounded)),'correlated_gaussian_thresholds':{str(rho):threshold(d,True,rho) for rho in [.25,.5]}}
  out['results'].append(result);print(json.dumps(result),flush=True)
 a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
