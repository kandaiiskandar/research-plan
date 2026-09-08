# Publication Consistency Audit Report

**Date:** 2026-09-08  
**Status:** OPEN — stopped under SC-3 before publication edits.  
**Scope achieved:** preliminary inspection, identified findings, evidence capture and integrity verification. **This is not a completed publication audit.**

## 1. Scope

The requested scope covers active research manuscripts and publication-supporting documents after SDR-001/C-8 and the cause-taxonomy cleanup. The active working manuscripts identified are conference v3 and Journal 1 v1. Journal 2 has a planning README and no manuscript. The journal v1 path contains “submission”, but its explicit banner and README identify it as a working draft. Conference v2.5 and older submissions are historical.

No source file was edited before the stop. No classifier was run, no prediction re-resolved and no new empirical analysis performed. Numeric extraction below is a queue for later review, not a substitute for that review.

## 2. Authoritative sources consulted

- Appendix C: formal classifier, observation and provenance contracts.
- C-8 migration report and `data/c8/canonical-results-post-migration.txt`: current results, attribution and metric scopes.
- `empirical-findings-2026-09-06.md` §0a: current reportable figures; older sections require vintage interpretation.
- `data/prediction-register.csv`: frozen actuals, statuses and original prediction scopes.
- `scripts/canonical_gt.py` and read-only excerpts of canonical classifier scripts: implementation definitions; no execution.
- Cause-taxonomy closure from the preceding task: `reasons : Q → 𝒫({fault,hazard,policy})`.
- Publication READMEs and the working-manuscript banners: working versus historical status.

The task's “Go share during daylight CAUTION” label must be read carefully: §0a labels 98.71% / 97.66% as **g_o component binding share**, not the share of generated Go recommendations. No recommendation-content measurement is inferred.

## 3. Files inventoried and inspected

[File inventory](../../data/publication-consistency-audit/file-inventory.csv) lists 142 publication/document files with role, review coverage and preservation status. Inventory is not full inspection. The two working manuscripts were partially inspected; publication READMEs and selected canonical/supporting sections were read. Historical and rendered files were not exhaustively reviewed.

The supplied supporting-document set includes an explicitly superseded scenario design. Its 22-kn table is therefore not treated as an active canonical counterclaim. Scope and vintage must be assessed from banners, not directory names alone.

## 4. Quantitative-result inventory

[Audit table](../../data/publication-consistency-audit/audit-table.csv) contains **25 reviewed finding rows** with file, section, line, item type, metric, exact source text, expected canonical reference, PASS/STALE/AMBIGUOUS/UNSUPPORTED status, action and rationale.

[Numeric coverage queue](../../data/publication-consistency-audit/quantitative-coverage-queue.csv) extracts **1,227 numeric tokens** from both working manuscripts, preserving section, line and context. This includes citations, identifiers, dates, hypothetical examples and comments as well as results. Tokens are deliberately marked pending/ambiguous because semantic mapping stopped. It is **not** a claim that 1,227 empirical results were audited or are unsupported. Spelled-out known prediction counts are covered by reviewed finding rows. A full inventory of all quantitative results across supporting documents remains incomplete.

## 5. Stale values discovered

| Location | Existing text/value | Canonical comparator | Status |
|---|---|---|---|
| Conference abstract | 7.7% / 6.0%; 22 confirmed / 2 refuted | 5.81% / 4.48%; 15 / 9 | STALE |
| Conference Methods | 23 confirmed / 1 refuted | 15 / 9 | STALE |
| Prototype paragraph | approximately fourteen oscillations/year; 6.2% | 5.2/year; 10.36% | STALE |
| Deployment Challenges | 5,416 / 227 / 70 / fourteen per year / 6.2% | 3,661 / 222 / 26 / 5.2 per year / 10.36% | STALE |
| TABLE VII C0 row | 24.64% / 24.64% / 32.36% | 42.88% / 42.88% / 48.69% | STALE |
| TABLE VII caption | 9,133 departure hours | C-8 output: 9,135 PRIMARY departure hours | STALE |
| TABLE VI rainfall daylight CAUTION | 1.55% / 2.99% | 1.48% / 2.70% | STALE |
| Interpretation paragraph | 7.7% of departure mornings | PRIMARY 5.81%; RESOLUTION 4.48%, departure-window hours | STALE |
| Totality proof | wind 22; categorical rain; fixed-clock twilight intervals | 21.6; numeric rain; binary solar-event time | STALE |
| Fig.4 | 0600 → SAFE without a date; wind CAUTION above 22 | date-dependent time; wind CAUTION above 21.6 | STALE |

The old 95.8% scheduled-transition share appears alongside the Deployment Challenges numbers. It was flagged without choosing a replacement: its metric definition needs a separate provenance mapping. No global find-and-replace was performed.

## 6. Corrections made

**None to publications or canonical evidence.** The stop condition arose during read-only inspection. Known stale statements remain in their source documents. The audit table records them as flagged, not changed.

## 7. Ambiguous claims and the stop condition

**SC-3: “A manuscript value cannot be traced to an existing canonical artefact.”**

Conference v3, Deployment Challenges, line 504, states:

> The target deployment hardware is commodity smartphones or low-cost single-board computers (under USD 50).

The same limit appears in `supervisor-feedback-response.md:204` as “< $50” and the historical submitted v2.5 manuscript at line 378. Searches for `USD 50`, `US$50`, `$50`, `50 USD`, `50 dollars` and `fifty dollars` across docs, publications, scripts, data and notes located these repetitions but no canonical budget decision, bill of materials, measured hardware result or cited cost artefact establishing the limit.

This is **untraceable in the inspected repository**, not a claim that such hardware cannot exist. The manuscript calls it a deployment target; whether it is an intended budget assumption or a sourced capability/cost claim is unresolved. It was not silently recast as a canonical assumption, removed, or replaced. The user's SC-3 instruction requires stopping even though other stale numeric corrections are already clear.

**Correction to the preliminary SC-1 concern.** An intermediate update described 22 versus 21.6 kn as a conflict involving two active canonical supporting tables. Subsequent banner/context inspection showed that `evaluation-design-rq4.md` explicitly says SUPERSEDED, while `architecture-illustration.md` explicitly defers all formal definitions to Appendix C. The latter's 22-kn row is stale supporting text; Appendix C explicitly documents the amendment to 21.6. Therefore **no unresolved SC-1 conflict is asserted on that evidence**. The final stop rests on SC-3, not on treating the superseded evaluation design as a current authority.

## 8. Policy versus evidence

Valid nighttime abstention is already described as architecture policy in the conference time-boundary threat. The manuscript's NIST risk-tier mapping, broad MET threshold attribution and CAUTION epistemic-support wording were flagged for careful review; their full provenance classification was not completed. No standards research or stronger novelty claim was introduced. The medium-vessel 2.8 m interpolation must retain its existing limitation when the audit resumes.

## 9. Safety-language findings

The theorem and human-override limitation correctly distinguish admissible recommendation types from recommendation correctness and human behaviour. Other passages assert calibrated guidance or epistemic support without the same qualifications. These were left for bounded review, not silently rewritten into a different scientific claim. The audit does not certify every use of “safety”, “unsafe”, “danger” or related language.

## 10. Prediction-register consistency

Direct CSV inspection gives **24 entries, 15 CONFIRMED and 9 REFUTED**. Current abstract/Methods prose contradicts that register. C-8 identifies seven status flips, only **P20, P23, P24** attributable to SDR-001; **P04, P09, P18, P19** were already refuted after earlier corrections. These sources were not modified. Cross-document propagation remains incomplete.

## 11. P09 provenance

The inspected C-8 report preserves `5,416 → 5,220 → 5,201 → 3,661`, with threshold, data and g_t stages respectively. The full decrease must not be attributed to Model B alone. The register was preserved byte-for-byte. A complete search of all publication-supporting P09 discussions remains pending.

## 12. P20 definitions

The authoritative distinction remains **1,529** for the original registered 06:00–17:00 scope versus **455** for RESOLUTION astronomical daylight. They are different scopes, not interchangeable measurements. Full publication-wide verification of every P20 mention was not completed before the stop.

## 13. Hysteresis consistency

C-8 supplies 3,661 total transitions, 222 non-scheduled transitions, 26 oscillations and 10.36% reduction. Journal 1 prototype and ablation plans contain matching figures. Conference prototype and Deployment Challenges retain older numbers. These are identified findings, not applied fixes.

## 14. Time-classifier consistency

Binary solar-event g_t remains frozen. Conference Algorithm 1 and the time-boundary threat use solar events, but the totality proof retains twilight CAUTION intervals and Fig.4 retains an undated 0600 SAFE example. Exact sunrise/sunset conventions were not changed. These discrepancies are still open in publication text.

## 15. Cause-taxonomy consistency

Appendix C and CLAUDE retain the closed reason-set contract. No runtime reason consumer was found in the preceding cleanup, and none is claimed here. A complete active-publication reason-language sweep was not completed in this stopped task.

## 16. Observation and exclusion consistency

The conference describes absent historical m and lower-bound interpretation. Its algorithm resolves inputs in one step but then computes components from raw-variable notation, warranting a scope/overwrite check when resumed. Startup, t ∉ D, solar dependency failure and unconsumed wave-period semantics must be checked against Appendix C without modifying it. No canonical observation model was changed.

## 17. Human authority

The conference limitation explicitly states unconditional human override and advisory rather than final decision control. This passage passes. It does not establish that every active supporting document has been checked.

## 18. Threats to Validity

The conference already discloses **2 → 1,536** direct SAFE→UNSAFE transitions, no time CAUTION, and nighttime abstention as a policy choice rather than a physical discontinuity. Other threats still contain stale hysteresis and wind language. Solar-formulation limitations, interpolation, exclusions and case-study bounds were not certified across all active texts. Solar Citation Closure was not begun.

## 19. Historical preservation

All pre-existing source files match their pre-inspection hashes, including submitted manuscripts, C-8/SDR reports, prior audits, logs, snapshots and canonical definitions. No historical version was rewritten or retroactively relabelled. The explicitly superseded evaluation design is preserved as such.

## 20. Files modified

**Zero pre-existing files modified.** The source snapshot covers 217 existing files. Only the new evidence directory and this report were added. No changelog or publication pointer was changed.

## 21. Audit artefacts added

- `data/publication-consistency-audit/integrity-before.json`
- `data/publication-consistency-audit/integrity-after.json`
- `data/publication-consistency-audit/integrity-result.json`
- `data/publication-consistency-audit/audit-table.csv`
- `data/publication-consistency-audit/quantitative-coverage-queue.csv`
- `data/publication-consistency-audit/file-inventory.csv`
- `data/publication-consistency-audit/build_stop_evidence.py`
- `docs/canonical/report-publication-consistency-audit-2026-09-08.md` (this report)

The evidence builder reproduces the tables and verifies that all captured source bytes remain unchanged. It does not perform a full semantic audit or edit publications.

## 22. Before/after hashes

| File | SHA-256 before | SHA-256 after |
|---|---|---|
| `data/prediction-register.csv` | `5574b88ea65168b6ef5e308629f3eb14fb70f8688a592fde279103ea4b37eae6` | `5574b88ea65168b6ef5e308629f3eb14fb70f8688a592fde279103ea4b37eae6` |
| `scripts/canonical_gt.py` | `b330bf9f94e848aad282a71d226c85c7e73f4ec8c0f2f8c88bfd7112b6e9a577` | `b330bf9f94e848aad282a71d226c85c7e73f4ec8c0f2f8c88bfd7112b6e9a577` |
| `data/solar/solar-events-daily.csv` | `057c46a19d0e8ea7956cdc38ae3d7615cf43cf800e7bc33ab286dfdc20ce1894` | `057c46a19d0e8ea7956cdc38ae3d7615cf43cf800e7bc33ab286dfdc20ce1894` |
| `docs/canonical/empirical-findings-2026-09-06.md` | `667161e288d5e403ac068edab31b21c86c8694ca6fa6b35288ae2096f685b556` | `667161e288d5e403ac068edab31b21c86c8694ca6fa6b35288ae2096f685b556` |
| `docs/canonical/appendix-c-formalisation.md` | `03e80802a46404df90c3e36960feab298e9036396f3f3a5d64e956a5b3c6cfb4` | `03e80802a46404df90c3e36960feab298e9036396f3f3a5d64e956a5b3c6cfb4` |
| `CLAUDE.md` | `8b8cb984756f066b794f66a617ba125f05dcee32725b051dadaf414dfecf3b4d` | `8b8cb984756f066b794f66a617ba125f05dcee32725b051dadaf414dfecf3b4d` |
| `publications/active/ipsci-2026/submissions/v3-revision/manuscript-v3.md` | `f683b08e21118a4e8b749cf66df3d66af53d11aaab75822825e21fc7e902162b` | `f683b08e21118a4e8b749cf66df3d66af53d11aaab75822825e21fc7e902162b` |
| `publications/active/journal-1/submissions/v1-initial-submission/manuscript.md` | `0c9dcbc15cffef5baf60904177cbffe4e0efcc27c3cbcfafc87ade9386ac44dc` | `0c9dcbc15cffef5baf60904177cbffe4e0efcc27c3cbcfafc87ade9386ac44dc` |

All match. Full [before](../../data/publication-consistency-audit/integrity-before.json), [after](../../data/publication-consistency-audit/integrity-after.json), and [integrity result](../../data/publication-consistency-audit/integrity-result.json) preserve hashes for the full 217-file snapshot.

## 23. Prediction-register integrity

**PASS:** exact SHA-256 match, 24 entries, 15/9. All prediction text, bounds, scopes, actuals, statuses and notes remain untouched. No register reconciliation or re-resolution was attempted.

## 24. Classifier integrity

**PASS:** every captured script matches; Appendix C and CLAUDE also match. No classifier or threshold was modified. No pipeline execution was used to repair manuscript text. The audit therefore makes no new claim about current runtime reproducibility beyond existing canonical evidence.

## 25. Solar and empirical integrity

**PASS:** all captured solar artefacts and empirical calculation artefacts match. The canonical findings still contain **PRIMARY 5.81% / RESOLUTION 4.48%**. No solar calculation or citation closure was undertaken.

## 26. Unresolved issues and closure assessment

SC-3 remains unresolved: the USD 50 hardware target has no located canonical provenance. Known stale manuscript passages have not been corrected. Full quantitative tracing, scientific-language classification, policy/evidence mapping and all supporting-document checks remain incomplete. Accordingly closure criteria 1–19 and 25 are not collectively satisfied, and criterion 26 (no unresolved stop condition) fails. Integrity requirements are satisfied, but integrity alone cannot close a consistency audit.

Do not interpret the provisional SC-1 concern as an unresolved competing threshold authority. The authoritative 21.6-kn amendment is documented; the final report corrects the earlier classification of the supporting documents.

## 27. Recommended next task

Resolve the hardware-cost provenance first: identify the existing authoritative record if one exists, or explicitly decide whether the USD 50 limit is a documented design-budget assumption or an unsupported number to remove. Resume this same Publication Consistency Audit after that stop condition is resolved, using the finding table and pending coverage queue. Do not start Solar Citation Closure or the Full Reviewer Audit yet.

# `PUBLICATION CONSISTENCY AUDIT REMAINS OPEN`
