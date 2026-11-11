# Evidence for three Table 2 comparisons

The Table 2 marks for three related surveys were checked on 21 October 2026 against their publisher PDFs. Page numbers are PDF file pages counted from one. A mark describes what a survey covers, not its quality.

| Reference | PHY | PLS | QML | Search/selection | Per-study audit | Quantitative resource illustration |
| --- | --- | --- | --- | --- | --- | --- |
| [24] Sharma and Kumar (2023) | Covered | Covered | Absent | Partial | Absent | Absent |
| [34] Astiti and Lee (2026) | Partial | Partial | Covered | Absent | Absent | Partial |
| [35] Puspitasari and Lee (2026) | Partial | Partial | Covered | Absent | Absent | Covered |

## [24] Sharma and Kumar

Source: Deep learning based physical layer security for terrestrial communications in 5G and beyond networks: A survey. DOI: https://doi.org/10.1016/j.phycom.2023.102002

- PDF page 4, Section 2, states the review method and research questions. PDF page 7, Figure 5, shows a staged selection from 400 initial items through 280 and 210 to 140. This counts as partial search and selection reporting: the figure names a keyword-definition stage but gives no executed search strings, databases or search dates.
- Sections 4 and 6 cover classical DL/DRL for radio PLS. Trained quantum models are not reviewed; the brief mention of quantum communications in the conclusion is not QML coverage.
- The application tables compare classical techniques, results and limitations. They do not list per-study qubits, layers or depth, shots or execution backends, and there is no quantitative resource illustration.

## [34] Astiti and Lee

Source: A Survey of Quantum Deep Reinforcement Learning for Resource Allocation in Future Wireless Networks. DOI: https://doi.org/10.1109/COMST.2025.3638435

- Sections III-V cover QDRL architectures, algorithms and wireless tasks, several of them above the physical layer, so PHY coverage is partial.
- PDF page 18 (printed page 126), in the power-control discussion, mentions secure precoding and power control with an eavesdropper and a secrecy-rate objective. PLS is marked partial; that example is a mathematical optimization without DRL.
- PDF pages 28-29 (printed pages 136-137) discuss extracting classical outputs, measurement noise and repeated-sampling overhead, and PDF pages 34-35 discuss hardware limits. This is marked as partial feasibility coverage, since no numerical shot or latency budget or encoding-width example is given for a stated input.
- Tables VI-XIII compare tasks, objectives, algorithms and task performance, but not per-study qubits, layers or depth, shots and backends. The tutorial gate and state representations are not such an audit.
- No literature search or selection procedure is documented; "systematic" refers to the organization of the survey, not to a search protocol.

## [35] Puspitasari and Lee

Source: Quantum Reinforcement Learning for UAV-Enhanced Next-Generation Wireless Communications. DOI: https://doi.org/10.1109/COMST.2025.3632908

- The scope includes UAV trajectory, navigation, networking, resource allocation and radio design, so PHY is partial. Trained quantum policies and QNN-based multi-agent methods are explained, so QML is covered.
- PDF pages 28-29 (printed pages 3116-3117), Section VII-E and Table XIII, discuss eavesdropping, spoofing and jamming and potential QRL-based frequency and power adaptation. PLS is marked partial, because these are prospective defenses rather than demonstrated security studies.
- PDF pages 16-17 (printed pages 3104-3105), Section IV-C, work through the classical set {3,4,5,6}: basis and amplitude encoding use two qubits, angle encoding four. This meets the Table 2 criterion for a quantitative resource illustration, although it is not a shot budget or latency estimate for a trained model.
- Table VIII lists simulators and toolkits, and Tables IX-XII organize applications and algorithms; none gives a per-study resource audit.
- No literature search or selection procedure is documented.

## Summary

Table 2 credits [35] for its encoding-width example and its discussion of potential security defenses, and [34] for its discussion of measurement and sampling overhead. The publisher PDFs are not redistributed here; the page locations and DOIs above identify the evidence.
