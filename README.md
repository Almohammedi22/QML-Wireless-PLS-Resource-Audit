# QML-Wireless-PLS-Resource-Audit

Supplementary material for the manuscript

**Quantum Machine Learning for Wireless Physical-Layer Optimization and Security: A Critical Review and Resource Audit**
A. Almohammedi, N. Hakim, W. Jaafar, and R. Langar

The files below let readers check the corpus selection, the resource audit, and the resource analysis reported in the manuscript.

| File | Supports |
|---|---|
| `S1_confirmatory_search_screening.xlsx` | Section II, Table 3, Appendix B |
| `S2_quantum_resource_audit.xlsx` | Section VIII, Tables 11 and 12 |
| `S3_resource_analysis_miso_wiretap.py` | Section IX, Tables 13 and 14 |

## S1. Confirmatory search screening

The confirmatory searches of Scopus and IEEE Xplore were run on 21 September 2026 and returned 32 and 26 records, or 42 after removing duplicates. Each record is listed with its decision and the reason for it. Two studies were added to the corpus, six were already in it, three were earlier versions of retained studies, two were cited as adjacent work without being counted, and 29 were excluded under the scope rule. The exact query strings are given in Appendix B of the manuscript.

## S2. Quantum resource audit

One row per retained study, identified by its reference number in the manuscript. Each extracted value is accompanied by the page, section, table or figure it was taken from. NR means the study does not report the quantity. Values were never inferred from companion papers. The `Summary` sheet reproduces every statistic reported in Section VIII.

## S3. Resource analysis script

Reproduces Tables 13 and 14 for the MISO wiretap channel. The assumptions are stated at the top of the script.

Requirements: Python 3 with `numpy` and `scipy`. Tested with numpy 2.4 and scipy 1.17.

```
python S3_resource_analysis_miso_wiretap.py --selftest
python S3_resource_analysis_miso_wiretap.py
```

The self-test checks that the closed-form secrecy-optimal beamformer is never beaten by a randomly drawn beamformer. The main run takes a few seconds. With the defaults (2000 channel draws, seed 1234, 10 dB), the shot thresholds for a mean secrecy-rate loss below 5% round to 4.5e2, 1.1e3 and 3.2e3 for Nt = 4, 16 and 64, matching Table 13 of the manuscript. The unrounded values may differ slightly in the fourth significant digit between numpy and scipy versions; the rounded values do not.

## Citation

Citation details will be added once the manuscript is published.
