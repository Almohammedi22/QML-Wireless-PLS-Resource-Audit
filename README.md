# QML Wireless PLS Resource Audit

Data and code for the article *Quantum Machine Learning for Wireless Physical-Layer Optimization and Security: A Critical Review and Resource Audit* by A. Almohammedi, N. Hakim, W. Jaafar and R. Langar.

## Contents

| Path | Contents | Article |
| --- | --- | --- |
| `Supplementary_material.pdf` | Supplementary material of the article (Sections S-I to S-V) | Cited throughout |
| `protocol.md` | Review protocol, the six search strings and the dated change log | Section II |
| `search/` | arXiv exports and recorded query strings of the 28 September 2026 searches, an API query helper, Table 2 comparison evidence and the records of the 7 November 2026 citation search | Section II-B, Supplementary Section S-II-F |
| `workbooks/Workbook_1_Screening.xlsx` | Title and abstract screening of 751 records, including the calibration sample | Section II-C, Fig. 2 |
| `workbooks/Workbook_2_Full_text_assessment.xlsx` | Decisions and exclusion codes for the 120 reports assessed at full text | Section II-C, Supplementary Table S-I |
| `workbooks/Full_text_reviewer_B_crosscheck_2026-11-09.csv` | Reviewer B's blinded cross-check of the 47 full-text exclusions and 15 Tier-1 decisions, with the adjudication | Supplementary Section S-II-C |
| `workbooks/Workbook_3_Extraction_and_resource_audit.xlsx` | Extraction of the 65 included studies, including the 55-study resource audit, with source pages | Section VIII, Tables 11 and 12 |
| `workbooks/Workbook_4_Source_audit.xlsx` | Additional source checks and readout validation | Supplementary Section S-V |
| `analysis/resource_analysis_miso_wiretap.py` | Shot budgets and latency for the direct and rescaled output mappings | Section IX, Tables 13 and 14 |
| `analysis/readout_sensitivity.py` | Seed, exact-sampling, loss-tail and covariance checks | Supplementary Table S-III |
| `analysis/validate_readout.py` | Direct-readout validation | Supplementary Section S-V |
| `analysis/verify_workbook_totals.py` | Recomputes the study accounting, the citation-search counts and the reporting totals | Sections II and VIII, Supplementary Section S-II-F |
| `analysis/results/` | Outputs of the reference run, including the printed shot and latency tables | |

## Corpus

The review includes 65 studies described in 73 reports:

- Tier 1 (direct physical-layer security): 12 learning-based studies and three analytical proposals.
- Tier 2 (transferable physical-layer design): 40 studies.
- Tier 3 (quantum-inspired classical methods): a contextual sample of 10 studies, counted separately.

The resource audit covers the 55 Tier-1 and Tier-2 studies. Of these, 39 report a qubit count, 38 a layer count and 14 a measurement-shot budget. Four report parameter matching for at least one classical comparison. A missing value means that the study does not report the quantity; it is not evidence that the design is infeasible.

Of the 120 reports assessed at full text, 47 were excluded. Workbook 2 marks 55 rows as Exclude because eight of them are companion reports of included studies (code X8).

## Reproducing the results

Requirements: Python 3 with NumPy and SciPy; the versions used are in `analysis/requirements.txt`. Run from `analysis/`:

```bash
pip install -r requirements.txt
python verify_workbook_totals.py --output results/workbook_totals.json
OPENBLAS_NUM_THREADS=1 python resource_analysis_miso_wiretap.py --selftest
OPENBLAS_NUM_THREADS=1 python resource_analysis_miso_wiretap.py
OPENBLAS_NUM_THREADS=1 python readout_sensitivity.py --output results/readout_sensitivity.json
OPENBLAS_NUM_THREADS=1 python validate_readout.py --output results/readout_validation.json
```

`verify_workbook_totals.py` uses only the Python standard library. It stops with an error if any total differs from the article.

The reference run uses 2,000 Rayleigh channel draws at 10 dB, seed 1234 and ten additional seeds, with Python 3.12.14, NumPy 2.3.5 and SciPy 1.17.0.

- At 64 antennas, the 5% mean-loss thresholds are about 3,234 shots for direct targets and 233 for rescaled targets.
- The rounded budgets of 3,200 and 230 shots take 320 ms and 23 ms at an assumed 100 µs per shot.
- With exact Pauli-Z variances, the thresholds are about 3,210 and 208 shots.
- Exact binomial sampling at the rounded budgets gives mean losses of 5.1% and 4.8%.

The analysis uses the known optimal beamformer as the target and an idealized product-state readout to isolate the effect of output representation on measurement cost. Training and hardware feasibility are outside its scope.

## Searches

All six searches were run on 28 September 2026. The arXiv exports and their query strings are in `search/`, together with `arxiv_search.py`, a helper for the arXiv API. The Scopus and IEEE Xplore exports are available from the authors on request.

`search/survey_comparison.md` gives the source pages behind three of the Table 2 comparisons.

A targeted citation search from the 14 Tier-1 studies of the database and seed-corpus routes followed on 7 November 2026 (change log of `protocol.md`). `search/citation_search_2026-11-07/` holds its seeds, every retrieved reference and citing paper, the merged records and the screening decisions. It added one study, reference [102] of the article.

## Review process

Two reviewers independently screened the calibration sample. The first author made all final eligibility decisions and checked the extraction for all 65 studies, and Reviewer B checked the Tier-1 resource entries against the source PDFs. In a blinded cross-check, Reviewer B independently matched 60 of 62 full-text decisions (`workbooks/Full_text_reviewer_B_crosscheck_2026-11-09.csv`). The protocol records tool assistance and amendments.

