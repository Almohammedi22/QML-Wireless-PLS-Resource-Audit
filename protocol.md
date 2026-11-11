# Search and screening protocol

QML for wireless physical-layer optimization and security: critical review and resource audit.

Initial protocol, drafted 28 September 2026. Commit this file before the final searches. Any later change goes in the change log at the end, with its date and reason. The tier definitions and exclusion rules are those of Section II-A of the manuscript.

Registration: the review was not registered. Amendments to the initial protocol are listed with their dates in the change log (Section 10).

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
OR adversarial OR GAN OR transformer ) ) )
AND ( wireless OR radio OR "physical layer" OR "physical-layer"
OR satellite OR UAV OR MIMO OR beamform* OR NOMA OR RIS OR mmWave )
AND ( beamform* OR precod* OR "beam prediction" OR "power allocation" OR "power control"
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
OR adversarial OR GAN OR transformer ) ) )
AND ( wireless OR radio OR "physical layer" OR "physical-layer"
OR satellite OR UAV OR MIMO OR beamform* OR NOMA OR RIS OR mmWave )
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
OR "All Metadata":policy OR "All Metadata":adversarial OR "All Metadata":GAN
OR "All Metadata":transformer)))
AND ("All Metadata":wireless OR "All Metadata":radio OR "All Metadata":"physical layer"
OR "All Metadata":satellite OR "All Metadata":UAV OR "All Metadata":MIMO
OR "All Metadata":beamforming OR "All Metadata":NOMA OR "All Metadata":RIS
OR "All Metadata":mmWave)
AND ("All Metadata":beamforming OR "All Metadata":precoding
OR "All Metadata":"beam prediction" OR "All Metadata":"power allocation"
OR "All Metadata":"power control" OR "All Metadata":"transmit power"
OR "All Metadata":"resource allocation" OR "All Metadata":"reconfigurable intelligent surface"
OR "All Metadata":"intelligent reflecting surface" OR "All Metadata":"stacked intelligent metasurface"
OR "All Metadata":"channel estimation" OR "All Metadata":UAV)
```

### IEEE Xplore, Tier 1

```
(("All Metadata":"variational quantum" OR "All Metadata":"parameterized quantum circuit"
OR "All Metadata":"quantum kernel" OR "All Metadata":"quantum support vector"
OR "All Metadata":"hybrid quantum-classical" OR "All Metadata":"quantum deep unfolding")
OR ("All Metadata":quantum ONEAR/5 ("All Metadata":learning OR "All Metadata":neural OR "All Metadata":reinforcement
OR "All Metadata":policy OR "All Metadata":adversarial OR "All Metadata":GAN
OR "All Metadata":transformer)))
AND ("All Metadata":wireless OR "All Metadata":radio OR "All Metadata":"physical layer"
OR "All Metadata":satellite OR "All Metadata":UAV OR "All Metadata":MIMO
OR "All Metadata":beamforming OR "All Metadata":NOMA OR "All Metadata":RIS
OR "All Metadata":mmWave)
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
(((ti:"variational quantum" OR abs:"variational quantum") OR (ti:"parameterized quantum circuit" OR abs:"parameterized quantum circuit") OR (ti:"quantum kernel" OR abs:"quantum kernel") OR (ti:"quantum support vector" OR abs:"quantum support vector") OR (ti:"hybrid quantum-classical" OR abs:"hybrid quantum-classical") OR (ti:"quantum deep unfolding" OR abs:"quantum deep unfolding")) OR ((ti:quantum OR abs:quantum) AND ((ti:learning OR abs:learning) OR (ti:neural OR abs:neural) OR (ti:reinforcement OR abs:reinforcement) OR (ti:policy OR abs:policy) OR (ti:adversarial OR abs:adversarial) OR (ti:GAN OR abs:GAN) OR (ti:transformer OR abs:transformer)))) AND ((ti:wireless OR abs:wireless) OR (ti:radio OR abs:radio) OR (ti:"physical layer" OR abs:"physical layer") OR (ti:"physical-layer" OR abs:"physical-layer") OR (ti:satellite OR abs:satellite) OR (ti:UAV OR abs:UAV) OR (ti:MIMO OR abs:MIMO) OR (ti:beamforming OR abs:beamforming) OR (ti:NOMA OR abs:NOMA) OR (ti:RIS OR abs:RIS) OR (ti:mmWave OR abs:mmWave)) AND ((ti:"physical layer security" OR abs:"physical layer security") OR (ti:"physical-layer security" OR abs:"physical-layer security") OR (ti:secrecy OR abs:secrecy) OR (ti:eavesdropping OR abs:eavesdropping) OR (ti:eavesdropper OR abs:eavesdropper) OR (ti:wiretap OR abs:wiretap) OR (ti:"physical layer authentication" OR abs:"physical layer authentication") OR (ti:"physical-layer authentication" OR abs:"physical-layer authentication") OR (ti:"RF fingerprinting" OR abs:"RF fingerprinting") OR (ti:"RF fingerprint" OR abs:"RF fingerprint") OR (ti:"radio frequency fingerprint" OR abs:"radio frequency fingerprint") OR (ti:"emitter identification" OR abs:"emitter identification") OR (ti:spoofing OR abs:spoofing) OR (ti:jamming OR abs:jamming) OR (ti:jammer OR abs:jammer) OR (ti:"covert communication" OR abs:"covert communication") OR (ti:"key generation" OR abs:"key generation"))
```

Tier 2:

```
(((ti:"variational quantum" OR abs:"variational quantum") OR (ti:"parameterized quantum circuit" OR abs:"parameterized quantum circuit") OR (ti:"quantum kernel" OR abs:"quantum kernel") OR (ti:"quantum support vector" OR abs:"quantum support vector") OR (ti:"hybrid quantum-classical" OR abs:"hybrid quantum-classical") OR (ti:"quantum deep unfolding" OR abs:"quantum deep unfolding")) OR ((ti:quantum OR abs:quantum) AND ((ti:learning OR abs:learning) OR (ti:neural OR abs:neural) OR (ti:reinforcement OR abs:reinforcement) OR (ti:policy OR abs:policy) OR (ti:adversarial OR abs:adversarial) OR (ti:GAN OR abs:GAN) OR (ti:transformer OR abs:transformer)))) AND ((ti:wireless OR abs:wireless) OR (ti:radio OR abs:radio) OR (ti:"physical layer" OR abs:"physical layer") OR (ti:"physical-layer" OR abs:"physical-layer") OR (ti:satellite OR abs:satellite) OR (ti:UAV OR abs:UAV) OR (ti:MIMO OR abs:MIMO) OR (ti:beamforming OR abs:beamforming) OR (ti:NOMA OR abs:NOMA) OR (ti:RIS OR abs:RIS) OR (ti:mmWave OR abs:mmWave)) AND ((ti:beamforming OR abs:beamforming) OR (ti:precoding OR abs:precoding) OR (ti:"beam prediction" OR abs:"beam prediction") OR (ti:"power allocation" OR abs:"power allocation") OR (ti:"power control" OR abs:"power control") OR (ti:"transmit power" OR abs:"transmit power") OR (ti:"resource allocation" OR abs:"resource allocation") OR (ti:"reconfigurable intelligent surface" OR abs:"reconfigurable intelligent surface") OR (ti:"intelligent reflecting surface" OR abs:"intelligent reflecting surface") OR (ti:"stacked intelligent metasurface" OR abs:"stacked intelligent metasurface") OR (ti:"channel estimation" OR abs:"channel estimation") OR (ti:UAV OR abs:UAV) OR (ti:"unmanned aerial vehicle" OR abs:"unmanned aerial vehicle"))
```

Xplore allows 25 terms per clause and counts each word of a phrase. Not counting the field names, the groups above use 24 (quantum learning), 11 (wireless), 24 (design) and 22 (security) terms. The Xplore design group omits "unmanned aerial vehicle" to stay within the limit, since "UAV" covers it.

## 3. Export

- Scopus: select all results, Export, CSV. Tick "Citation information", "Bibliographical information" and "Abstract & keywords". Without the last one there is nothing to screen.
- Xplore: select all results, Export, CSV.
- arXiv: run `python arxiv_search.py` on the same day. If arXiv refuses scripted requests, open the two API URLs in a browser and save each page as XML. Each feed repeats the query it ran, which is checked against Section 2. It writes `arxiv_T1_<date>.csv`, `arxiv_T2_<date>.csv` and the two query files, and prints the checks for Section 4.
- File names: `scopus_T2_<date>.csv`, `scopus_T1_<date>.csv`, `xplore_T2_<date>.csv`, `xplore_T1_<date>.csv`. Keep the raw files unchanged.

## 4. Checks before screening

Screening starts only when every run passes its check. The earlier exports named here are kept in the repository.

For Scopus, the query text shown in Search History must match Section 2 exactly, apart from line breaks, and is copied into the search log. For arXiv, the query repeated in each saved feed must match Section 2. IEEE Xplore kept no accessible search history of the executed Command Search strings for the final runs. The search log therefore records the exact protocol string for Xplore, and the Xplore exports are verified by the result-set and recall checks below.

| Run | Must contain | Tier-2 recall |
|---|---|---|
| Scopus Tier 2 | all 238 records of the 28 September run with the previous strings, and DOI 10.1049/qtc2.12120 | 19 of 25 |
| Xplore Tier 2 | all 471 records of the 28 September run with the previous strings, apart from any whose only design term was "unmanned aerial vehicle" | 16 of 25 |
| Scopus Tier 1 | all 32 records of the 21 September search and all 57 of the 28 September run with the previous strings; 8 of the 10 direct-security studies, all but the two arXiv preprints | not applicable |
| Xplore Tier 1 | all 26 records of the 21 September search and all 134 of the 28 September run with the previous strings | not applicable |
| arXiv Tier 1 | the two Tier-1 preprints, arXiv:2602.13238 and arXiv:2608.20240; unique records equal to the API total | not applicable |
| arXiv Tier 2 | arXiv:2408.04747, the preprint of the TWC 2024 hybrid quantum-classical beamforming study; unique records equal to the API total | reported, not a target |

Both databases are expected to miss the quantum gradient descent MIMO-NOMA study (IEEE WCL 2025). Its metadata has no quantum-method term, because it presents an optimization algorithm rather than a learning model, and it entered the corpus through reference lists. Xplore also misses the three papers in the Journal of the Korean Institute of Communications and Information Sciences, which it does not carry. Together the database searches retrieve 19 of 25. Terms were added only for vocabulary shared by several records. "Quantum gradient descent" appears in a single known title and was not added.

The five transferable studies that no Scopus run can retrieve were confirmed absent from Scopus by title search on 27 September 2026: the four KICS conference papers (OMP hybrid precoding, zero-forcing hybrid precoding, quantum deep unfolding for power allocation and precoding, statistical QFL for NOMA) and the Authorea preprint on federated quantum GAN.

If a check fails, stop and find the reason before screening. A failed superset check means the string that ran is not the string printed here.

## 5. Search log

One row per run: database, tier, string version (commit hash of this file), query text and its provenance, search date, search time where the source keeps it, number of results, export file name and check result.

## 6. Deduplication

Merge all six exports. Remove duplicates by DOI, then by normalized title (lowercase, punctuation removed). Flag conference and journal versions of the same work and keep the most complete version. Near-identical titles (similarity of 0.93 or more) are checked by the authors before the calibration sample is drawn. Versions of the same work are merged, keeping the published or most complete version, and each decision is recorded in `manual_merges.csv`. Mark records already in the corpus as "known".

arXiv records: versions of one preprint (v1, v2) count once. An arXiv record that matches a Scopus or Xplore record by DOI or normalized title is merged into the published record, and the published version is kept. Merged arXiv records are counted as duplicates.

Keep these counts for the flow diagram: records per database and tier, duplicates removed, records screened, excluded at title and abstract, full texts assessed, excluded at full text with reasons, included.

## 7. Screening

Decisions: T1, T2, T3 (quantum-inspired classical method, or coherent Ising machine optimization as set out below, recorded and counted separately), Exclude with a reason code, or Unsure.

Tier 2 requires a learning model: a quantum model whose parameters are trained, such as a QNN, a variational quantum classifier or regressor, a quantum RL policy, a quantum kernel method or a quantum generative model. Quantum optimization without a trained model, such as quantum annealing, QAOA, Grover adaptive search or quantum gradient descent used as a solver, falls outside Tier 2 (code X10). It enters Tier 1 when it evaluates a security metric, because Tier 1 admits quantum algorithms.

Reviewers. Reviewer A is the first author. Reviewer B is a second reviewer who is not an author; reviewer B screened the calibration sample independently, cross-checked the 47 full-text exclusions and 15 Tier-1 decisions, and checked five audit fields for all 15 Tier-1 studies (9 November 2026 entries). The first author resolves disagreements and makes the final eligibility decisions. Deviations from the reviewer roles set out below are recorded in the change log.

Tool assistance. ChatGPT (OpenAI, including Codex) and Claude (Anthropic) assisted with parts of the screening, extraction and source checks under the first author's direction. They were not used for κ. The first author checked their output and made all final decisions.

| Code | Reason |
|---|---|
| X1 | Decision variables above the physical layer (offloading, caching, edge or fog placement, routing, scheduling) |
| X2 | Physical-layer variable mixed with an above-physical-layer objective |
| X3 | UAV trajectory or path planning only |
| X4 | No eligible quantum-computational or quantum-inspired method, including quantum sensing used only with classical processing |
| X5 | Overview, framework or survey without a dedicated evaluation |
| X6 | Not a radio physical-layer problem (quantum-state authentication, QKD, general QML) |
| X7 | Preprint without enough methodological detail |
| X8 | Duplicate or earlier version |
| X9 | Not a primary study (proceedings front matter, a book without a study of its own, retracted item); a chapter that reports its own study is a primary report |
| X10 | Identified quantum or quantum-inspired computation outside the admitted scope: a non-learning quantum solver without a direct-security evaluation, QML used only as the workload, or a method applied to a task outside the admitted Tier 1 and Tier 2 tasks, such as detection or localization |
| X11 | Retrieved full text does not establish an eligible implemented method and its connection to an admitted task or output |

Scheduling boundary C, adopted 10 October 2026. Tier 2 requires an implemented, trained quantum learning model that produces at least one design output admitted in Section II-A and is evaluated on an in-scope physical-layer objective. Eligible outputs include beamforming or precoding, beam prediction, transmit power, RIS or SIM phases and channel estimates. The other tasks admitted in Section II-A remain eligible. UAV trajectory is eligible only alongside another admitted PHY variable; trajectory alone remains X3.

Radio user grouping, user or access-point association, and subchannel or pilot assignment may be learned alongside an admitted PHY output. Record these accompanying assignments in the extraction. Assignment-only learning, including assignment combined with UAV trajectory but no other admitted PHY output, is excluded under X1. Time-domain user scheduling, user activation and frame or time allocation remain X1 even when learned alongside a PHY output. This includes a secondary user's within-slot transmit/harvest duration. The radio-assignment allowance does not extend to network deployment, placement, offloading, caching or routing. These remain excluded under X1.

X2 continues to apply when a PHY variable is coupled to an above-PHY objective. A learned power or precoding output does not override this or another exclusion. T3 follows this assignment boundary; the T3 task scope and the classification of coherent Ising machines are set out below. UAV flight energy, adopted 10 October 2026: propulsion, hovering and avionics energy may be included in a communication-energy-efficiency objective or a reward combining an admitted PHY metric with energy consumption. Their presence alone does not trigger X2 when the implemented model also produces an admitted PHY design output. Record the energy components and their role in the objective, reward or constraints. X2 still applies to traffic queueing, task-computing, offloading or other above-PHY objectives. Transmission time computed from link rates and relay decoding or processing time do not by themselves establish an above-PHY objective; assess the defined delay model rather than the word "latency." All other tier requirements and exclusion rules remain in force.

Computational scope, adopted 11 October 2026. The review covers quantum computation, including QML, and quantum-inspired computation. Quantum sensing alone, used with a classical controller or learner, is outside this scope and is excluded under X4. Method classification follows the computation the source reports, not the words "quantum" or "optical" or the machine named. A genuine quantum model simulated on a classical computer remains a quantum model; it is not classified as T3 because it uses a simulator.

T3 task scope, adopted 11 October 2026. T3 uses the same admitted physical-layer design and direct-security tasks as Tier 1 and Tier 2. The source must identify the quantum-inspired mechanism and connect it to an admitted task or output. A quantum or quantum-inspired method applied to another task, such as detection or localization, is excluded under X10.

Coherent Ising machines, adopted 11 October 2026. A coherent Ising machine (CIM) is an Ising-machine optimizer based on degenerate optical parametric oscillator dynamics. It is not a trained quantum model and is not treated as a quantum annealer. CIM optimization is admitted to T3 whether its dynamics are computed numerically on a classical computer or run on analog optical CIM hardware, subject to the T3 task scope and boundary C. Record the execution category (numerical, analog optical or both) and report the two separately. A quantum annealer used as a solver remains a non-learning quantum solver under X10 unless a direct-security metric is evaluated.

Eligibility evidence, adopted 11 October 2026. An eligibility decision needs enough information to identify a qualifying implemented method, its admitted task or output and its evaluated objective. It does not need full reproducibility, source code or every resource-audit field. Where scope is established but qubits, depth, shots, backend or similar fields are missing, the study is retained with NR entries and marked not auditable. X7 remains specific to insufficiently described preprints. X11 applies to a retrieved full text that does not establish an eligible implemented method and its connection to an admitted task or output, after source assessment and any clarification actually obtained, whatever the publication type. Missing resource fields alone are not an X11 reason. X11 concerns insufficient evidence to establish eligibility; it does not replace an established scope exclusion, and a retrieved but unclear report is not counted as not retrieved.

Rule freeze. Boundary C, the flight-energy rule and the four rules above complete the eligibility rules, which are frozen from 11 October 2026. Any later change is recorded in the change log as a dated deviation, with the records it affects.

Calibration. After deduplication, draw a random 20% of unique records with seed 20260928 and commit the list. Reviewers A and B screen these titles and abstracts independently. Compute Cohen's κ on include (T1, T2, T3 or Unsure) against exclude. T3 counts as include because those records go to full-text reading. At κ ≥ 0.80, reviewer A screens the rest alone. Below 0.80, discuss every disagreement, clarify the rule wording in this file, draw another 10% and repeat.

Full text. Reviewer A reads the full text of every T1, T2, T3 and Unsure record.

Borderline rescreen. Reviewer B rescreens the following without seeing A's decisions (deviations: 7 October, 8 to 10 October and 9 November 2026 entries):

- every Unsure;
- every full-text exclusion;
- every X2, X5, X7 and T3;
- every record whose title or abstract mentions UAV, jamming, key generation, quantum-inspired or arXiv;
- every T1 include, and every T2 include that mentions secrecy, eavesdropping, jamming, authentication, spoofing or covert;
- the 11 scope exclusions from the original candidate log.

Each disagreement is discussed, and the final decision and its reason are logged.

## 8. Extraction and verification

Reviewer A extracts every new study into the existing schema. Each value carries its page, table or figure, and NR is recorded when the paper does not report it. The schema also records the fields that Section 7 requires: accompanying radio assignments (boundary C), UAV energy components (flight-energy rule), the execution category of CIM studies, and a not-auditable flag where resource fields are missing.

Reviewer B checks every entry, old and new (deviation: 13 October 2026 entry), and fills two columns: "confirmed or corrected" and "reason". A reported value is checked at its recorded location. An NR entry is confirmed only after searching the full text for its terms:

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
- 28 September 2026. Recall test with the documented strings: the Scopus reruns (238 and 57 records) and the Xplore runs (471 and 134) retrieved 16 and 14 of the 25 transferable studies, 17 together. The records they missed named their system only by its radio technology, or used quantum transformer models for beam prediction. The wireless group gained NOMA, RIS and mmWave, the quantum proximity list gained "transformer", and the Tier-2 design group gained "beam prediction", in all three sources. The Xplore design group dropped "unmanned aerial vehicle" to stay within the 25-term limit, since "UAV" covers it. "Quantum gradient descent" was not added, because it names an optimization algorithm and appears in a single known title. The revised strings replace those of all earlier runs.
- 28 September 2026. The arXiv API refused every scripted request from this network, including a one-word test query, while the same requests succeeded in a browser. Both arXiv searches were therefore run by opening the API URLs in a browser (Tier 1 at 18:48:42 UTC, 25 records; Tier 2 at 18:49:04 UTC, 63 records) and saving the feeds as XML. The query repeated in each feed is identical to Section 2.
- 28 September 2026. Screening pool built using the documented deduplication procedure: 1,019 records identified, 271 duplicates removed (267 matched by DOI or title, and 4 preprint, conference or journal versions merged by the authors as listed in `manual_merges.csv`), 748 unique records. The calibration sample of 150 records was drawn after the version decisions.
- 28 September 2026. Documentation clarified after the final searches. IEEE Xplore kept no accessible copy of the executed Command Search strings, so `search_log.csv` records their provenance accordingly, and the Xplore result sets were verified by the prespecified superset and recall checks. Search times are recorded where the source keeps them. No search string, result set, screening record or calibration sample changed.
- 28 September 2026, before reviewer A screened the calibration sample. Tier 2 was clarified to require a trained quantum learning model, and code X10 was added for quantum methods outside Tier 2. T3 counts as include for κ and goes to full-text reading. The corpus study that uses quantum gradient descent as a solver is to be rechecked at full text against the clarified rule.
- 28 September 2026. Calibration. Reviewer B is a second reviewer who is not an author. Reviewers A and B agreed on include or exclude for 148 of 150 records, κ = 0.94, which passes the 0.80 threshold (`calibration_result.xlsx`). Reviewer A screens the remaining 598 records alone.
- 5 October 2026. Calibration differences resolved by the first author: R0550 and R0726 (include or exclude) and R0218 and R0442 (tier only) were set to Unsure for full-text reading, with reasons in `calibration_result.xlsx`. κ is computed on the independent decisions and does not change.
- By 6 October 2026. Reviewer A screened the 598 remaining records by title and abstract: 11 T1, 32 T2, 6 T3, 51 Unsure and 498 excluded (`screening_reviewer_A_verified.xlsx`). A separate AI screening of the same 598 records is kept as a secondary check (Workbook 1, sheet "AI check (598)"). It agreed with reviewer A on 585 of 598 include or exclude decisions (κ = 0.92) and made no final decision. Reviewer A retained all 21 corpus studies found among the 598 records.
- 7 October 2026. Deviation from Section 7: the borderline rescreen of 359 records was run as a secondary check with tool assistance instead of by reviewer B. It agreed with reviewer A on 345 of 359 include or exclude decisions (κ = 0.87), leaving 14 include or exclude differences and 10 tier differences.
- 7 to 10 October 2026. Screening differences. The first author resolved the 24 differences and the other flagged records (R0218, R0442, R0550, R0726 and LOG-1 to LOG-3) against Section 7; reviewer A's original decisions are kept unchanged. On 10 October, a working exclusion of R0298 drafted from its abstract was withdrawn, because the abstract did not settle eligibility, and the record was restored to reviewer A's original Unsure and added to the full-text queue. Final screening decisions, adopted on 13 October 2026: 625 excluded and 126 forwarded to full text, of 751 records (748 from the pool and three candidate-log records).
- 8 to 10 October 2026. Full text. Proposed full-text decisions, with reasons and page evidence, were prepared with tool assistance (Workbook 2, columns E to J). The first author read each retrieved full text and confirmed or corrected each proposal (19 October entry). The queue holds the 123 records forwarded by screening (122 from the pool and LOG-1, after R0298's restoration) and six corpus studies outside the search pool (CORP-b73, CORP-b74, CORP-b76, CORP-b85, CORP-b87 and CORP-b94), assessed against the same criteria; this includes the recheck of the quantum gradient descent study announced on 28 September.
- 10 October 2026. Version merges at full text. Nine reports overlap with a fuller or published report of the same study and are recorded as X8 merges in `manual_merges.csv` and Workbook 2; the first author adopted them on 13 October. For R0659 and R0667, the published ATC 2025 paper (R0659) is the representative, following Section 6, and the fuller arXiv preprint (R0667) is used only for extraction details that R0659 lacks, with the source report named for each value.
- 10 October 2026. Reports not retrieved. Ten reports could not be obtained through institutional access or publisher, conference and author-copy searches: six chapters of one River Publishers book (R0003, R0006, R0007, R0027, R0032 and R0035), one IGI Global chapter (R0626) and three KICS conference papers (CORP-b73, CORP-b76 and CORP-b87). Reports still missing at the retrieval cutoff of 13 October 2026 are counted as not retrieved in the flow diagram. Missing access is not used as an exclusion reason.
- 10 October 2026, during full-text assessment. The first author chose scheduling boundary C to resolve an ambiguity affecting 15 records. An admitted PHY design output is required for Tier 2; radio grouping, association, subchannel or pilot assignment may accompany it for an in-scope objective, while assignment-only learning is X1. UAV trajectory alone remains X3, and assignment with trajectory but no other admitted PHY output is X1. Time scheduling, activation and time allocation, including within-slot transmit/harvest duration, remain X1. Network deployment remains excluded and X2 continues to apply to above-PHY objectives. T3 uses this assignment boundary when its method category is established. Optical-CIM classification, the wider T3 task scope and total-UAV-energy objectives were settled by the 10 and 11 October rules below. The 15 affected records are R0070, R0136, R0248, R0294, R0314, R0348, R0363, R0415, R0442, R0471, R0511, R0534, R0575, R0624 and R0724. Original screening decisions and calibration statistics are unchanged.
- 10 October 2026, during full-text assessment. UAV flight energy: the first author chose to allow propulsion, hovering and avionics energy in communication-energy-efficiency objectives and PHY-metric/energy rewards when the implemented model also outputs an admitted PHY design variable. The energy components are recorded in extraction. Queueing, task-computing, offloading and other above-PHY objectives remain subject to X2; all other exclusions continue to apply. R0363 now supports a T2 proposal. R0531 remained Unsure until its implemented scheduling variables were established (11 October entry): learned time allocation or user activation is X1, while the accompanying radio assignments allowed by boundary C do not automatically exclude it.
- 10 October 2026, source checks. R0534 retains its T2 proposal: PDF p. 7, Eq. (19), defines link delay as rate-based transmission time plus relay decoding and processing; p. 8, Eqs. (22)–(24), gives the state, power/subchannel actions and reward; p. 13, Table 2, specifies processing delay. R0533 retains X2 because PDF pp. 7–8, Eqs. (27)–(32), explicitly models and penalizes traffic queues. Workbook 2 applies the adopted energy rule to R0363 and records the revised reasons for R0531 and R0534 in its correction log.
- 11 October 2026, end of full-text assessment. At the first author's request, the computational-scope, T3 task-scope, coherent Ising machine and eligibility-evidence rules were added to Section 7, code X11 was added, X4, X9 and X10 were clarified, X7 was kept for preprints, and the eligibility rules were frozen. Section 8 now lists the extraction fields these rules require. Basis: a source review of the 16 assessed records that remained Unsure (`full_text_source_review.md`). Proposals changed in Workbook 2: R0248 T3, R0531 T2, R0661 X1 and R0298 X10, which the source review supports under the existing rules; R0136 T3 (numerical and analog optical CIM) and R0437 T3 (analog optical CIM) under the CIM rule; R0269 and R0622 X10 under the T3 task scope, with R0268 still linked to R0269 as its earlier version; R0609 X4 (quantum sensing with classical processing); and R0101, R0165, R0315, R0472, R0515, R0524 and R0686 X11. Proposals now stand at 14 T1, 40 T2, 10 T3 and 55 Exclude, with 10 reports not retrieved (129 records). Working screening codes in the master were corrected from chapter-specific abstracts: R0002 X6 and R0026 X4. R0009, R0012 and R0030 kept the title-and-abstract X9 exclusion by reviewers A and B, because no chapter-specific abstract or full text was found and the code was not replaced from the title (see the 12 October entry). The LOG-2 abstract was verified against the publisher page; LOG-3 keeps the X1 code of the candidate log. Original screening decisions are unchanged.
- 11 to 12 October 2026. Extraction. Reviewer A verified every value against the full texts. It uses the Audit schema of the corrected first-round workbook (`S2_quantum_resource_audit_corrected.xlsx`: [99] cleared and marked Full text not available, [102] citation corrected) and adds record IDs and the fields Section 7 requires. Every new value carries its PDF page with section, equation, table or figure. Coverage: 40 new studies; R0164, R0206 and R0659 as the counted reports for [115], [94] and [86], each checked value by value against the first-round row, with R0667 used only for details missing from R0659 and labelled as R0667; new fields and a first-round check for R0363 [120] and R0415 [107]. First-round values are kept for the other first-round studies. Coding conventions were harmonized and logged (Workbook 3, Correction_log). The reporting statistics apply one rule to every row: a quantity counts as reported when it is given for a circuit the study specifies or evaluates. Under this rule, [101] and [118], counted as reporting a qubit number in the first round, are not counted, because their first-round values state that the evaluated count is not given.
- 12 October 2026. Three chapters reopened: R0009, R0012 and R0030 were changed from working Exclude X9 to Unsure in the master, with their codes cleared; A's and B's original X9 decisions are preserved. X9 does not exclude a chapter merely because it is a chapter, and no chapter-specific evidence was found. Their full texts are not available (the same River Publishers book as R0003, R0006, R0007, R0027, R0032 and R0035), so they are added to the full-text queue as reports not retrieved. The master now forwards 126 records, the queue holds 132 reports, and 13 reports are not retrieved; the proposals remain 14 T1, 40 T2, 10 T3 and 55 Exclude.
- 12 October 2026. Source check of the extraction. The accompanying-assignment and UAV-energy fields of the 19 retained first-round studies were completed from their PDFs, with 38 per-value entries and page locations; their first-round resource values were kept. R0509 [108] gained its publisher DOI, 10.7840/kics.2023.48.8.897. The check supported the [120] encoding correction and the execution coding of R0312 and R0531.
- 13 October 2026. Full-text decisions finalized. The first author adopted the eligibility decisions, the nine X8 merges and the extraction corrections, with the scope frozen at the 11 October rules: 14 T1, 40 T2, 10 T3 and 55 Exclude, including the nine merges, with 13 reports not retrieved. Deviation from Section 8: reviewer B's check of the extraction was reduced to a sample, namely all 14 T1 studies and 10 of the other 50 included studies drawn with Python `random.Random(20261013).sample` from the sorted record IDs (R0546, R0509, R0267, R0541, R0649, R0390, R0511, R0176, R0465, R0737), covering 673 evidence entries, 26 replacement checks and 81 flags. This sample check was not carried out (19 October entry).
- 19 October 2026. First author's checks recorded. The first author read each of the 119 retrieved full texts, confirming or correcting each proposed eligibility decision, and checked every extracted resource value, including the first-round values, against the full texts. His decisions and confirmations were entered in the supplementary workbooks: 36 screening confirmations (Workbook 1, Master F–G), the decisions and reasons for the 119 assessed reports (Workbook 2, Q–S, with the recording date in T) and the confirmation of the 64 included studies (Workbook 3, Audit, Author_Confirmation). The 13 reports not retrieved have no full-text decision and are labelled Not retrieved. No eligibility decision or extracted value changed.
- 19 October 2026. Reporting. The header states that the review was not registered. Bracketed reference numbers in the 11 and 12 October entries follow the draft numbering of 12 October 2026; sheet "Reference numbers" of Workbook 3 gives the article's numbers. The distributed workbooks are in `workbooks/`, and the numerical scripts and outputs are in `analysis/`. Other working files named in this log are available from the authors on request.
- 19 October 2026. Additional source audit. It checked five core field classifications (qubits, layers, shots, execution environment and baseline fairness) in the 24-study sample of the 13 October entry, 120 classifications in all, and rechecked the PDFs of 54 of the 55 full-text exclusions, including the nine linked reports; the PDF of R0741 could not be retrieved again, and its decision stands. No eligibility decision or aggregate reporting indicator changed. R0560 is a reporting-boundary case: counting the 257-qubit logical register implied by its symbolic N_E+1 register and the classical N_E = 256 reliability setting would raise qubit reporting from 38/54 to 39/54 and Tier-1 qubit reporting from 10/14 to 11/14, without changing the execution or Tier-1 shot results (Supplementary S-V; Workbook 4). Reviewer B's sample check of the extraction (13 October entry) was not carried out. Workbook 3 records the check as "Not performed".
- 19 October 2026. Numerical checks. The resource script reproduces the 64-antenna Gaussian 5% target at 3234.47 shots, reported as about 3,200. Seeds 1–10 give 3264.85–3422.29 shots, and output-dependent Pauli-Z variances give 3209.91 shots for the reference draw. Exact product-state binomial readout at 3200 shots gives a mean loss of about 5.1% over 2000 channels and 20 measurement repetitions per channel (`validate_readout.py`, `readout_validation.json`). Assignment-only channel selection is outside scope in all tiers. No search date, study tier, included-study count or audit total changed.
- 20 October 2026. Sections 7 and 8 now point to the change-log entries that record deviations from the planned reviewer and extraction roles.
- 20 October 2026. Coding and readout sensitivity. Parameter-matching categories now distinguish explicit unequal counts, matching not established and non-learning comparisons; the five positive matching indicators are unchanged. The readout experiment now compares direct components with infinity-norm-rescaled target expectations, reports loss percentiles, and repeats the seed, variance, exact-sampling and covariance checks for both mappings (`readout_sensitivity.py`, `readout_sensitivity.json`). A related quantum-enabled 6G survey was added to the background comparison, and the article-reference columns of the workbooks were renumbered. No search was rerun, and no eligibility rule or study decision changed.
- 21 October 2026. Report accounting and scripts. The 119 assessed reports are reconciled as 72 included reports and 47 excluded reports; the verifier separates the eight linked companions of included studies from the 55 rows marked Exclude, and Workbook 2 guide cell B5 explains this. A check of the 13 recorded full-text X1 reasons found no security-driven channel or frequency-selection task; the security-oriented X1 exclusion is mini-slot scheduling. A floating-point-to-integer conversion in `readout_sensitivity.py` was corrected so that a rounded budget of 230 uses exactly 230 shots, and the numerical JSON, Workbook 4 cells G16:J18 and Supplementary Table S-III were updated to match. The Table 2 marks for references [24], [34] and [35] were checked against their publisher PDFs (`search/survey_comparison.md`). No study decision, tier, extracted value or numerical result changed.
- 21 to 24 October 2026. Manuscript and repository layout. The exclusion-code table moved to the supplement (Table S-I) and the scope decision tree to the article (Fig. 3); the tool-use table was replaced by the process summary in Supplementary Section S-II, whose tables were renumbered. Pointers in this log and in the workbooks follow the current numbering and folders. No search, eligibility decision, reviewer role, extracted value or numerical result changed.
- 1 November 2026. Execution coding and a year label. Evidence level E1 now requires an explicit statement that the simulation is noiseless and no stated finite-shot sampling; naming a simulator, or calling the simulation idealised, is not enough. This is the criterion applied to R0531 on 12 October, following R0470. E2 requires finite-shot sampling stated by a shot count or by repeated measurement, which covers R0300. Applied to R0167, the E1 criterion moves that study from E1 to unclassified, as R0587 already was. The execution environment is therefore classifiable for 19 of the 54 audited studies, 7 of them at E1, and the verifier expectations were updated. The year label of R0573 in Workbook 3 now follows the issue-year convention (2024). Workbook 3 Correction_log entries 34 to 36 give the details. No eligibility decision or other extracted value changed.
- 7 November 2026. Citation search, added after the database searches as a targeted check of direct-security coverage. The seeds were the 14 Tier-1 studies included at that point, [88] to [101], and one round covered their reference lists and the papers citing them. The search ran in two passes on the same day. The first took reference lists and citing papers from OpenAlex, with the reference lists of [88] and [94] from the publisher versions and that of [95] from its arXiv full text. The second added the references that OpenAlex omits, from Crossref for ten seeds and from the arXiv full text of [96], and further citing papers from Semantic Scholar. Records were merged by OpenAlex identifier, DOI and normalized title and matched against Workbooks 1 to 3. The eligibility rules and codes of Section 7 were applied unchanged, and records published after 28 September 2026, the search date, were not eligible. The first pass returned 529 records, 494 of them unique. Of these, 22 were seeds or already screened, and 472 were screened by title and abstract. The second pass returned 85 records, 74 of them new after merging. Of these, 2 were seeds or already screened, 2 were published after the cutoff and 70 were screened by title and abstract. In total, 614 records gave 568 unique records, and 542 were screened. The first author excluded 541 of them (X4 453, X6 70, X5 10, X10 4, X1 2, X9 2) and included the remaining one after full-text assessment as a third analytical Tier-1 study, [102] (record CIT-1 in Workbooks 2 and 3). The records and decisions are in `search/citation_search_2026-11-07/`. Adding [102] renumbered the article references [102] to [166] of the earlier numbering as [103] to [167]. The Manuscript_Ref columns of Workbooks 3 and 4 follow the new numbering, and earlier dated entries keep the numbering of their date. Workbook 3 Correction_log entries 37 to 40 give the details.
- 8 November 2026. The first author checked the source for CIT-1 ([102]) and confirmed the corrected extraction in Workbook 3 (Audit, Author_Confirmation).
- 8 November 2026. Final Tier-1 source check. The check described in Section 7 compared the qubit, layer, shot, execution and baseline entries of the 15 Tier-1 studies with their PDFs. [88] reports a rule for the PVM encoding and gives the evaluated antenna count, yielding three qubits for that component. [94] and [96] report unequal parameter counts for the indicated classical comparisons. [95] describes comparable classical layers without establishing a parameter match. [93] explicitly tunes one comparator to an approximate match and gives both counts. Workbook 3 records the original values, corrections and page locations. The updated audit counts 39 of 55 studies reporting qubits, 11 of 15 in Tier 1, four of 55 reporting a parameter match, and six not auditable. No eligibility decision, shot count or execution classification changed. Reviewer B's planned extraction check was not performed.
- 9 November 2026. Reviewer B's Tier-1 verification. After the five corrections recorded on 8 November, Reviewer B checked the 75 worksheet entries for studies [88] to [102] against the source PDFs, covering qubit counts, circuit layers, shots, execution settings and classical baselines. The reviewer reported no discrepancies in the checked entries or their cited page locations. Workbook 3 (Evidence, columns J and K) records the checked values and source locations. The check covered five fields per study and did not replace the broader planned sample check described on 13 October. No audit values or totals changed.
- 9 November 2026. Reviewer B's blinded cross-check of full-text decisions. Reviewer B assessed the 47 full-text exclusions and the 15 Tier-1 includes against Section 7, without access to the first author's decisions, and agreed on 60 of 62 include-or-exclude decisions (κ = 0.92), including all 15 Tier-1 decisions. The first author checked the two disputed reports against their PDFs and kept both exclusions, R0661 under X1 and R0165 under X11. `workbooks/Full_text_reviewer_B_crosscheck_2026-11-09.csv` records the assessment and the adjudication. No eligibility decision or count changed.
- 10 November 2026. The tool-assistance paragraph of Section 7 and the dated entries were condensed. No decision or count changed.
