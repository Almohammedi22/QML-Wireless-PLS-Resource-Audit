# Citation search, 7 November 2026

Targeted backward and forward citation search for direct-security studies, added after the database searches of 28 September 2026. Supplementary Section S-II-F of the article reports it, and the change log of `protocol.md` records it as an amendment.

## Method

- Seeds: the 14 Tier-1 studies included at that point, references [88] to [101] of the article (`seeds.csv`).
- One round, backward (reference lists) and forward (citing papers).
- Two passes on the same day (column `pass` of both CSV files).
- First pass: reference lists and citing papers from OpenAlex. The reference lists of [88] and [94] came from the publisher versions and that of [95] from its arXiv full text.
- Second pass: the references that OpenAlex omits, from Crossref (ten seeds) and from the arXiv full text of [96], and further citing papers from Semantic Scholar.
- Merging: by OpenAlex identifier, DOI and normalized title, then matching against Workbooks 1 to 3 and the article's reference list.
- Eligibility: the rules and exclusion codes of Section 7 of `protocol.md`, unchanged. Records published after 28 September 2026, the date of the database searches, were not eligible.

## Files

| File | Contents |
| --- | --- |
| `seeds.csv` | The 14 seeds with their identifiers and the number of entries taken from each source |
| `retrieved.csv` | Every retrieved entry (614), with its seed, list, source, identifier and the record it was merged into |
| `records.csv` | The 568 merged records, with their status, the screening proposal and its reason, and the first author's decision |

## Counts

- First pass: 529 retrieved, 494 unique. 22 seeds or already screened, 472 screened by title and abstract, 471 excluded and 1 assessed in full text.
- Second pass: 85 retrieved, 74 new after merging. 2 seeds or already screened, 2 published after the cutoff, 70 screened by title and abstract and 70 excluded.
- Total retrieved: 614 (555 from reference lists, 59 citing papers). Duplicates removed: 46. Unique after merging: 568.
- Seeds: 3. Already screened in the review: 21. Published after the cutoff: 2.
- Screened by title and abstract: 542. Excluded: 541 (X4 453, X6 70, X5 10, X10 4, X1 2, X9 2). Assessed in full text and included: 1, reference [102] of the article, record CIT-1 in Workbooks 2 and 3.

`../../analysis/verify_workbook_totals.py` recomputes these counts.

## Tool use

The lists were retrieved and merged with tool assistance, which also proposed a code and reason for each record (columns `proposal` and `proposal_reason` of `records.csv`). An OpenAlex search of titles and abstracts for quantum terms supported the proposals of the first pass. The first author made every eligibility decision (column `author_decision`). Record 562 merges reference [1] of [100] and of [101], which both cite 3GPP TS 22.261 v16.1.0, and keeps both links in `source_ids` and `found_via`.
