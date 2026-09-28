# Search and screening protocol

QML for wireless physical-layer optimization and security: critical review and resource audit.

Version 1, drafted 28 September 2026. Commit this file before the final searches. Any later change goes in the change log at the end, with its date and reason. The tier definitions and exclusion rules are those of Section II-A of the manuscript.

## 1. Databases and limits

- Scopus, Advanced document search, field TITLE-ABS-KEY.
- IEEE Xplore, Command Search, with the field name "All Metadata": before every search term, as Command Search requires.
- All six final searches (Scopus and Xplore for both tiers, and the two arXiv runs) are done in one session on the same day. That date is the search date reported in the paper.
- No language restriction. Scopus is limited to PUBYEAR < 2027. Xplore has no year filter, and no filter of any kind is ticked on either results page.
- arXiv, supplementary source for preprints in both tiers (decision D1). Searched through its API with `arxiv_search.py`, in titles and abstracts, since arXiv has no keyword field. Scopus and IEEE Xplore remain the primary databases.

## 2. Search strings

Paste each string exactly as printed. Do not retype it.

### Scopus, Tier 2

```
TITLE-ABS-KEY ( ( "quantum machine learning" OR "quantum neural network*"
OR "variational quantum" OR "parameterized quantum circuit*"
OR "quantum reinforcement learning" OR "quantum kernel*"
OR "quantum support vector" OR "hybrid quantum-classical"
OR "quantum federated learning" OR "quantum deep unfolding"
OR "quantum graph neural network*"
OR ( quantum PRE/5 ( learning OR neural OR reinforcement OR policy
OR adversarial OR GAN ) ) )
AND ( wireless OR radio OR "physical layer" OR "physical-layer"
OR satellite OR UAV OR MIMO OR beamform* )
AND ( beamform* OR precod* OR "power allocation" OR "power control"
OR "transmit power" OR "resource allocation"
OR "reconfigurable intelligent surface*"
OR "intelligent reflecting surface*"
OR "stacked intelligent metasurface*" OR "channel estimation"
OR UAV OR "unmanned aerial vehicle*" ) )
AND PUBYEAR < 2027
```

### Scopus, Tier 1

```
TITLE-ABS-KEY ( ( "quantum machine learning" OR "quantum neural network*"
OR "variational quantum" OR "parameterized quantum circuit*"
OR "quantum reinforcement learning" OR "quantum kernel*"
OR "quantum support vector" OR "hybrid quantum-classical"
OR "quantum federated learning" OR "quantum deep unfolding"
OR "quantum graph neural network*"
OR ( quantum PRE/5 ( learning OR neural OR reinforcement OR policy
OR adversarial OR GAN ) ) )
AND ( wireless OR radio OR "physical layer" OR "physical-layer"
OR satellite OR UAV OR MIMO OR beamform* )
AND ( "physical layer security" OR "physical-layer security" OR secrecy
OR eavesdrop* OR wiretap OR "physical layer authentication"
OR "physical-layer authentication" OR "RF fingerprint*"
OR "radio frequency fingerprint*" OR "emitter identification"
OR spoof* OR jamm* OR "covert communication*" OR "key generation" ) )
AND PUBYEAR < 2027
```

### IEEE Xplore, Tier 2

```
(("All Metadata":"variational quantum" OR "All Metadata":"parameterized quantum circuit"
OR "All Metadata":"quantum kernel" OR "All Metadata":"quantum support vector"
OR "All Metadata":"hybrid quantum-classical" OR "All Metadata":"quantum deep unfolding")
OR ("All Metadata":quantum ONEAR/5 ("All Metadata":learning OR "All Metadata":neural OR "All Metadata":reinforcement
OR "All Metadata":policy OR "All Metadata":adversarial OR "All Metadata":GAN)))
AND ("All Metadata":wireless OR "All Metadata":radio OR "All Metadata":"physical layer"
OR "All Metadata":satellite OR "All Metadata":UAV OR "All Metadata":MIMO
OR "All Metadata":beamforming)
AND ("All Metadata":beamforming OR "All Metadata":precoding
OR "All Metadata":"power allocation" OR "All Metadata":"power control"
OR "All Metadata":"transmit power" OR "All Metadata":"resource allocation"
OR "All Metadata":"reconfigurable intelligent surface" OR "All Metadata":"intelligent reflecting surface"
OR "All Metadata":"stacked intelligent metasurface" OR "All Metadata":"channel estimation"
OR "All Metadata":UAV OR "All Metadata":"unmanned aerial vehicle")
```

### IEEE Xplore, Tier 1

```
(("All Metadata":"variational quantum" OR "All Metadata":"parameterized quantum circuit"
OR "All Metadata":"quantum kernel" OR "All Metadata":"quantum support vector"
OR "All Metadata":"hybrid quantum-classical" OR "All Metadata":"quantum deep unfolding")
OR ("All Metadata":quantum ONEAR/5 ("All Metadata":learning OR "All Metadata":neural OR "All Metadata":reinforcement
OR "All Metadata":policy OR "All Metadata":adversarial OR "All Metadata":GAN)))
AND ("All Metadata":wireless OR "All Metadata":radio OR "All Metadata":"physical layer"
OR "All Metadata":satellite OR "All Metadata":UAV OR "All Metadata":MIMO
OR "All Metadata":beamforming)
AND ("All Metadata":"physical layer security" OR "All Metadata":secrecy
OR "All Metadata":eavesdropping OR "All Metadata":wiretap
OR "All Metadata":"physical layer authentication" OR "All Metadata":"RF fingerprinting"
OR "All Metadata":"radio frequency fingerprint" OR "All Metadata":"emitter identification"
OR "All Metadata":spoofing OR "All Metadata":jamming
OR "All Metadata":"covert communication" OR "All Metadata":"key generation")
```

### arXiv, Tier 1 and Tier 2

Generated by `arxiv_search.py`, which also saves the exact string next to each result file. The groups match the Xplore groups with three differences forced by the arXiv API: every term is searched in the title or the abstract, the proximity clause becomes a co-occurrence of "quantum" with the same six words, and a few word forms are listed explicitly because the API has no wildcards (eavesdropper, jammer, RF fingerprint).

Tier 1:

```
(((ti:"variational quantum" OR abs:"variational quantum") OR (ti:"parameterized quantum circuit" OR abs:"parameterized quantum circuit") OR (ti:"quantum kernel" OR abs:"quantum kernel") OR (ti:"quantum support vector" OR abs:"quantum support vector") OR (ti:"hybrid quantum-classical" OR abs:"hybrid quantum-classical") OR (ti:"quantum deep unfolding" OR abs:"quantum deep unfolding")) OR ((ti:quantum OR abs:quantum) AND ((ti:learning OR abs:learning) OR (ti:neural OR abs:neural) OR (ti:reinforcement OR abs:reinforcement) OR (ti:policy OR abs:policy) OR (ti:adversarial OR abs:adversarial) OR (ti:GAN OR abs:GAN)))) AND ((ti:wireless OR abs:wireless) OR (ti:radio OR abs:radio) OR (ti:"physical layer" OR abs:"physical layer") OR (ti:"physical-layer" OR abs:"physical-layer") OR (ti:satellite OR abs:satellite) OR (ti:UAV OR abs:UAV) OR (ti:MIMO OR abs:MIMO) OR (ti:beamforming OR abs:beamforming)) AND ((ti:"physical layer security" OR abs:"physical layer security") OR (ti:"physical-layer security" OR abs:"physical-layer security") OR (ti:secrecy OR abs:secrecy) OR (ti:eavesdropping OR abs:eavesdropping) OR (ti:eavesdropper OR abs:eavesdropper) OR (ti:wiretap OR abs:wiretap) OR (ti:"physical layer authentication" OR abs:"physical layer authentication") OR (ti:"physical-layer authentication" OR abs:"physical-layer authentication") OR (ti:"RF fingerprinting" OR abs:"RF fingerprinting") OR (ti:"RF fingerprint" OR abs:"RF fingerprint") OR (ti:"radio frequency fingerprint" OR abs:"radio frequency fingerprint") OR (ti:"emitter identification" OR abs:"emitter identification") OR (ti:spoofing OR abs:spoofing) OR (ti:jamming OR abs:jamming) OR (ti:jammer OR abs:jammer) OR (ti:"covert communication" OR abs:"covert communication") OR (ti:"key generation" OR abs:"key generation"))
```

Tier 2:

```
(((ti:"variational quantum" OR abs:"variational quantum") OR (ti:"parameterized quantum circuit" OR abs:"parameterized quantum circuit") OR (ti:"quantum kernel" OR abs:"quantum kernel") OR (ti:"quantum support vector" OR abs:"quantum support vector") OR (ti:"hybrid quantum-classical" OR abs:"hybrid quantum-classical") OR (ti:"quantum deep unfolding" OR abs:"quantum deep unfolding")) OR ((ti:quantum OR abs:quantum) AND ((ti:learning OR abs:learning) OR (ti:neural OR abs:neural) OR (ti:reinforcement OR abs:reinforcement) OR (ti:policy OR abs:policy) OR (ti:adversarial OR abs:adversarial) OR (ti:GAN OR abs:GAN)))) AND ((ti:wireless OR abs:wireless) OR (ti:radio OR abs:radio) OR (ti:"physical layer" OR abs:"physical layer") OR (ti:"physical-layer" OR abs:"physical-layer") OR (ti:satellite OR abs:satellite) OR (ti:UAV OR abs:UAV) OR (ti:MIMO OR abs:MIMO) OR (ti:beamforming OR abs:beamforming)) AND ((ti:beamforming OR abs:beamforming) OR (ti:precoding OR abs:precoding) OR (ti:"power allocation" OR abs:"power allocation") OR (ti:"power control" OR abs:"power control") OR (ti:"transmit power" OR abs:"transmit power") OR (ti:"resource allocation" OR abs:"resource allocation") OR (ti:"reconfigurable intelligent surface" OR abs:"reconfigurable intelligent surface") OR (ti:"intelligent reflecting surface" OR abs:"intelligent reflecting surface") OR (ti:"stacked intelligent metasurface" OR abs:"stacked intelligent metasurface") OR (ti:"channel estimation" OR abs:"channel estimation") OR (ti:UAV OR abs:UAV) OR (ti:"unmanned aerial vehicle" OR abs:"unmanned aerial vehicle"))
```

Xplore allows 25 terms per clause and counts each word of a phrase. Not counting the field names, the groups above use 23 (quantum learning), 8 (wireless), 25 (design) and 22 (security) terms. If Xplore rejects the design group, drop "unmanned aerial vehicle" and record that here.

## 3. Export

- Scopus: select all results, Export, CSV. Tick "Citation information", "Bibliographical information" and "Abstract & keywords". Without the last one there is nothing to screen.
- Xplore: select all results, Export, CSV.
- arXiv: run `python arxiv_search.py` on the same day. It writes `arxiv_T1_<date>.csv`, `arxiv_T2_<date>.csv` and the two query files, and prints the checks for Section 4.
- File names: `scopus_T2_<date>.csv`, `scopus_T1_<date>.csv`, `xplore_T2_<date>.csv`, `xplore_T1_<date>.csv`. Keep the raw files unchanged.

## 4. Checks before screening

Screening starts only when every run passes its check. The earlier exports named here are kept in the repository.

For every run, the query text shown in the database's search history must match Section 2 exactly, apart from line breaks. It is copied into the search log.

| Run | Must contain | Tier-2 recall |
|---|---|---|
| Scopus Tier 2 | DOI 10.1049/qtc2.12120 | 20 of 25 |
| Xplore Tier 2 | all 445 records of the 27 September Xplore run (export 20:36 local), and the ICAIIC 2025 terahertz beamforming study | 14 of 25 expected |
| Scopus Tier 1 | all 32 records of the 21 September Scopus search | not applicable |
| Xplore Tier 1 | all 26 records of the 21 September Xplore search | not applicable |
| arXiv Tier 1 | the two Tier-1 preprints, arXiv:2602.13238 and arXiv:2608.20240; unique records equal to the API total | not applicable |
| arXiv Tier 2 | arXiv:2408.04747, the preprint of the TWC 2024 hybrid quantum-classical beamforming study; unique records equal to the API total | reported, not a target |

Xplore Tier 2 is expected to miss three transferable studies that Xplore does index, because their Xplore metadata lacks one of the three concepts: the quantum transformer beam-prediction paper (ICTC 2024) has no quantum-method or design term, the quantum gradient descent MIMO-NOMA paper (IEEE WCL 2025) has no quantum-method term, and the QFRL STAR-RIS paper (IEEE IoT-J 2024) has no wireless term. Scopus retrieves all three, so the combined Tier-2 recall of the two databases is 20 of 25. The search terms are not tailored to individual known titles.

The five transferable studies that no Scopus run can retrieve were confirmed absent from Scopus by title search on 27 September 2026: the four KICS conference papers (OMP hybrid precoding, zero-forcing hybrid precoding, quantum deep unfolding for power allocation and precoding, statistical QFL for NOMA) and the Authorea preprint on federated quantum GAN.

If a check fails, stop and find the reason before screening. A failed superset check means the string that ran is not the string printed here.

## 5. Search log

One row per run: database, tier, string version (commit hash of this file), query text copied from the database's search history, date and time, number of results, export file name, check result.

## 6. Deduplication

Merge all six exports. Remove duplicates by DOI, then by normalized title (lowercase, punctuation removed). Flag conference and journal versions of the same work and keep the most complete version. Mark records already in the corpus as "known".

arXiv records: versions of one preprint (v1, v2) count once. An arXiv record that matches a Scopus or Xplore record by DOI or normalized title is merged into the published record, and the published version is kept. Merged arXiv records are counted as duplicates.

Keep these counts for the flow diagram: records per database and tier, duplicates removed, records screened, excluded at title and abstract, full texts assessed, excluded at full text with reasons, included.

## 7. Screening

Decisions: T1, T2, T3 (quantum-inspired classical method, recorded and counted separately), Exclude with a reason code, or Unsure.

| Code | Reason |
|---|---|
| X1 | Decision variables above the physical layer (offloading, caching, edge or fog placement, routing, scheduling) |
| X2 | Physical-layer variable mixed with an above-physical-layer objective |
| X3 | UAV trajectory or path planning only |
| X4 | No quantum or quantum-inspired method |
| X5 | Overview, framework or survey without a dedicated evaluation |
| X6 | Not a radio physical-layer problem (quantum-state authentication, QKD, general QML) |
| X7 | Preprint without enough methodological detail |
| X8 | Duplicate or earlier version |
| X9 | Not a primary study (proceedings front matter, book, retracted item) |

Calibration. After deduplication, draw a random 20% of unique records with seed 20260928 and commit the list. Reviewers A and B screen these titles and abstracts independently. Compute Cohen's κ on include (T1, T2 or Unsure) against exclude. At κ ≥ 0.80, reviewer A screens the rest alone. Below 0.80, discuss every disagreement, clarify the rule wording in this file, draw another 10% and repeat.

Full text. Reviewer A reads the full text of every T1, T2 and Unsure record.

Borderline rescreen. Reviewer B rescreens the following without seeing A's decisions:

- every Unsure;
- every full-text exclusion;
- every X2, X5, X7 and T3;
- every record whose title or abstract mentions UAV, jamming, key generation, quantum-inspired or arXiv;
- every T1 include, and every T2 include that mentions secrecy, eavesdropping, jamming, authentication, spoofing or covert;
- the 11 scope exclusions from the original candidate log.

Each disagreement is discussed, and the final decision and its reason are logged.

## 8. Extraction and verification

Reviewer A extracts every new study into the existing schema. Each value carries its page, table or figure, and NR is recorded when the paper does not report it.

Reviewer B checks every entry, old and new, and fills two columns: "confirmed or corrected" and "reason". A reported value is checked at its recorded location. An NR entry is confirmed only after searching the full text for its terms:

| Field | Search terms |
|---|---|
| Qubits | qubit, register |
| Depth or layers | depth, layer, block, ansatz |
| Shots | shot, measurement, sample, repetition, expectation |
| Execution environment | simulator, statevector, Qiskit, PennyLane, Cirq, hardware, IBM, backend, device |
| Noise model | noise, noisy, depolarizing, decoherence, NISQ |
| Baseline | baseline, benchmark, compare, trainable parameters |
| Tier-1 extras | gradient, parameter-shift, optimizer, epochs, iterations, transpile, CNOT, CZ |

Every correction is discussed before the value changes. All counts in the paper are recomputed from the corrected sheet by script.

## 9. Decisions

D1, arXiv. Decided 28 September 2026: searched as a supplementary source for both tiers, because preprints are eligible in both. Scopus and IEEE Xplore remain the primary databases. Section II reports arXiv separately from the two databases, and the flow diagram counts its records on their own line.

## 10. Change log

- 21 September 2026. Tier-1 confirmatory searches: Scopus 32 records, Xplore 26, 42 unique.
- 27 September 2026. Tier-2 recall test 1 (Scopus): 17 of 25. Three indexed studies were missed because their wording matched no quantum-learning phrase ("quantum deep reinforcement learning", "quantum AI-enhanced deep reinforcement learning", "quantum-based recurrent deep deterministic policy gradient"). Added the PRE/5 proximity clause, "quantum deep unfolding" and "quantum graph neural network*" to the quantum-learning group of all four strings.
- 27 September 2026. Scopus title check: the four KICS conference papers and the Authorea preprint are not in Scopus.
- 27 September 2026. An intermediate Scopus rerun lost 35 records of test 1, including four known transferable studies. The string that ran differed from the documented one, and the run was discarded.
- 27 September 2026. Xplore: phrase words count toward the 25-term clause limit, so the quantum-learning group was rewritten with ONEAR/5 (23 terms). It covers every earlier phrase.
- 27 September 2026. Xplore wireless group: added "beamforming", matching the Scopus group. Without it, Xplore missed the ICAIIC 2025 terahertz beamforming study, whose only wireless-group term is "beamforming".
- 27 September 2026. Scopus run at 00:54 UTC: 278 records, all 203 of test 1 included, 20 of 25 transferable studies retrieved, all five misses confirmed absent from Scopus. The export had no abstracts, and it did not contain DOI 10.1049/qtc2.12120, whose title alone matches all three groups of the documented string. The final session therefore repeats the search with the string exactly as printed here.
- 28 September 2026. Decision D1: arXiv is not searched. The database searches are described as covering indexed literature only.
- 28 September 2026. Decision D1 changed: arXiv is searched as a supplementary source for Tier 1 and Tier 2, since preprints are eligible in both tiers. Scopus and IEEE Xplore remain the primary databases.
- 28 September 2026. The Scopus Tier-2 check no longer compares against the 27 September run exported at 00:54 UTC. That run did not use the documented string: it lacked DOI 10.1049/qtc2.12120, whose title matches all three groups. Every run is now checked by comparing the query text in the database's search history with Section 2.
- 28 September 2026. The first final Scopus runs of Tier 1 and Tier 2 added six terms that are not in this protocol ("quantum transformer*", "quantum gradient descent", mmWave, NOMA, RIS and "beam prediction"). Both runs were discarded.
