# Publication Consistency Audit — continuation after SC-3 resolution

Date: 2026-09-09. Branch: `chore/publication-consistency-audit`.

This report supersedes the **open status**, not the historical contents, of [the stopped audit](report-publication-consistency-audit-2026-09-08.md). It closes the bounded consistency task for the two active working manuscripts. It is not a full reviewer audit, a completed Journal 1 manuscript, or solar citation closure.

## Continuation and authorised delta

The previous audit stopped under SC-3 because the USD 50 hardware parenthetical had no traceable provenance. [Hardware-cost resolution](report-hardware-cost-provenance-2026-09-08.md) reached Outcome C (unsupported number), removed that parenthetical from conference v3 and the supervisor response, and cleared SC-3. Commit `8c2e836` was fast-forward merged into the original audit branch after audit evidence commit `8adf9b0`; the hardware branch is retained. No contradictory new cost evidence was found and the question was not reopened.

The two authorised deletions are retained. Historical v2.5 is unchanged. The old integrity builder uses a pre-resolution baseline, so its detection of this delta is expected. The continuation records it in `authorised-resume-delta.json` and uses a fresh before-manifest. Preexisting `data/.DS_Store` and `docs/.DS_Store` changes are separately identified user metadata and are not staged as audit work.

## Scope and coverage

Both working manuscripts were inspected in full for consistency: conference v3 and Journal 1 v1 working draft. Existing journal placeholders remain planned work; no results or implementation were invented. Supporting publication pointers, the two old section plans, supervisor-response reuse guidance and the architecture illustration were checked where they could propagate obsolete definitions. The old plans and response retain their historical body text under explicit reuse/supersession guidance. This does not claim that every file in the original 142-file inventory received an independent full scientific review.

The existing 25-row finding table is carried forward in `audit-table-continuation.csv`; exact before/after corrections and source references are in `edit-log.json`. All 1,227 original queue IDs are retained and classified in `quantitative-coverage-mapped.csv`: 119 result tokens, 9 sample-size tokens, 15 prediction tokens, 45 figure/table tokens, 153 thresholds, 244 equation constants, 18 hypothetical examples, 97 historical/provenance tokens, 320 citation/year tokens and 207 identifiers. These are token counts, not counts of independent empirical claims. `result-source-index.csv` extracts result-related rows. Original line locations/text are retained for traceability; the edit log records replacement wording and newly added quantitative assertions. Bibliographic metadata is classified, not independently revalidated as a full citation audit. No unresolved publication-result metric remains in this bounded scope.

## Quantitative and formal corrections

| Finding | Current text and evidence |
|---|---|
| Abstract, Methods, interpretation, conclusion | PRIMARY 5.81%, RESOLUTION 4.48%; 15 CONFIRMED / 9 REFUTED from 24 register rows. Unit is departure-window hours, not mornings. C-8 output and frozen prediction register. |
| Prototype and deployment | 3,661 total transitions; 222 non-scheduled; 26 oscillations across five years, approximately 5.2/year; non-scheduled transitions 222→199 with hysteresis, reduction 10.36%. C-8 output and C-5 stage 3. |
| Old 95.8% | Historical F6 value 5,189 / 5,416, pre-amendment fixed-clock v1. Replaced with the existing C-8 value 3,439 / 3,661 = 93.9% (rounded). Scheduled denotes an aggregate transition step coinciding with a change in g_t; it is not exclusive causal attribution. |
| TABLE VII | Symmetric C0–C1 and C0–C3 values 42.88%; C0–C2 48.69%; C1–C3 0.00%; C1/C3–C2 5.81%. Caption: 9,135 PRIMARY hourly records in the inclusive 05:00–09:00 departure window. |
| TABLE VI | Rainfall daylight CAUTION 1.48% / 2.70%; all-hours non-SAFE 0.20% / 0.26%, PRIMARY then RESOLUTION. |
| Other replay quantities | Existing C-8 output anchors daylight counts, component shares, vessel comparisons, maxima and all-hours totals. Resolution configuration covers a shorter period, so its difference is not presented as an isolated causal estimate of spatial resolution. |
| Fig. 4 | Dated 2024-03-20; examples 07:00, 10:00, 14:00 lie within stored sunrise 6.341591 h and sunset 18.452345 h. Numeric rainfall examples and wind boundary 21.6 kn. No new solar calculation. |
| Totality and component definitions | Wind lower boundary 21.6 kn; numeric rain boundaries 10/20 mm/hr; half-open sunrise≤t<sunset SAFE, otherwise UNSAFE. No operational twilight CAUTION. Journal wave proof small-vessel upper boundary 1.25 m. Appendix C is unchanged. |

The original suspicion of a canonical 22 kn contradiction does not activate SC-1: the evaluation design is explicitly superseded and the illustration defers formal definitions to Appendix C. The supporting illustration is now corrected; historical evaluation text is preserved.

## Predictions and provenance

Registered wording, numeric bands and original scopes remain unchanged. Only P20, P23 and P24 of seven status flips are attributable to SDR-001; P04, P09, P18 and P19 were already refuted by earlier corrections. P09 provenance is preserved as **5,416 → 5,220 (threshold) → 5,201 (data) → 3,661 (g_t)**, with only the final value used for current transition totals. P20 retains **1,529 in its registered 06:00–17:00 scope**, distinct from **455 astronomical-daylight RESOLUTION hours**. No prediction was re-resolved.

## Scientific language, policy and operational semantics

| Area inspected | Finding and disposition |
|---|---|
| Safety, UNSAFE, danger, prohibition | Governance states bound AI participation and recommendation types. UNSAFE does not itself establish physical danger, legal prohibition or inevitable harm. Literature discussions of danger remain contextual evidence, not the definition of UNSAFE. |
| Guarantees and calibrated reliance | Formal guarantees concern totality, scope containment and the specified engine assumptions. Operator behaviour, advice quality, calibrated reliance and harm prevention are not demonstrated by replay or theorem; user study and engine fidelity remain outstanding. |
| Nighttime and COLREG | Sunset/sunrise supplies temporal relevance; withdrawal of AI advisory is an architecture policy, not an external mandate. |
| Vessel, wind and rain evidence | Medium 2.8 m is conservative interpolation, not a measured universal limit. Rain and wind provenance are component-specific; governance bands do not authorise/prohibit departure. The studied hull lengths are distinguished from claims about an entire deployment population. |
| NIST | Paragraph now describes voluntary, use-case-agnostic guidance and interpretive alignment. NIST does not prescribe this architecture’s three states or abstention policy. Checked against the official AI RMF 1.0 executive summary: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf. No compliance claim is made. |
| Observations and exclusions | Exclusion precedes fault handling. Historical D={m} is a retrospective design choice, not an absent-live-warning policy. t∉D; v is validated at startup; required clock/date/solar dependency failure uses fail-safe. Wave period is not consumed by g_o. Algorithm uses resolved values after resolution rather than overwriting them with raw values. |
| Human authority | Unconditional final human authority; the system permits, restricts or withdraws advisory generation. Go is not legal authorisation; Duration does not guarantee safe navigation. |
| Reasons | reasons:Q→𝒫({fault,hazard,policy}); valid night policy, valid environmental non-SAFE hazard, failed required non-excluded input fault, overlaps permitted, SAFE empty. Annotation does not modify S, G(S), A_AI(S), rule sets or human authority. Runtime reason-set instrumentation is not claimed. |

The conference Threats to Validity now explicitly covers 2→1,536 direct SAFE→UNSAFE transitions, removal of time CAUTION, policy status of night abstention, retrospective warning exclusion, medium-vessel interpolation, solar-method/reference limitations, single-site scope, unvalidated operator behaviour and disclosed refutations. Journal planned discussion carries the corresponding consistency constraints. The formal architecture remains three-state globally.

## Integrity and verification

`verify_publications.py` passes read-only checks against frozen records, including table symmetry, scope denominators, Fig. 4 stored solar values, P09/P20, register counts and manuscript statements. It does not run classifiers, generate new empirical results or test an unimplemented engine. `git diff --check` is also required before commit.

Before/after SHA-256 manifests are retained for all 489 baseline tracked files: 481 unchanged, eight authorised supporting/manuscript files changed. Full hashes are in `integrity-before.json` and `integrity-after.json`; the following selected frozen hashes match in both:

| Frozen file | SHA-256 before = after |
|---|---|
| `data/c8/canonical-results-post-migration.txt` | `0bca160f69f68663d1f11672c0295cf9234624379a67e164fe50c5f2dde301a9` |
| `data/prediction-register.csv` | `5574b88ea65168b6ef5e308629f3eb14fb70f8688a592fde279103ea4b37eae6` |
| `data/solar/solar-events-daily.csv` | `057c46a19d0e8ea7956cdc38ae3d7615cf43cf800e7bc33ab286dfdc20ce1894` |
| `docs/canonical/appendix-c-formalisation.md` | `03e80802a46404df90c3e36960feab298e9036396f3f3a5d64e956a5b3c6cfb4` |
| `scripts/canonical_gt.py` | `b330bf9f94e848aad282a71d226c85c7e73f4ec8c0f2f8c88bfd7112b6e9a577` |

All other baseline classifier scripts, solar artefacts, canonical empirical findings and cause-taxonomy contract are protected by the same full-manifest comparison. v2.5, old audit reports, C-8, SDR-001 records, superseded evaluation design and session logs remain unchanged.

Existing files modified:

- `docs/canonical/architecture-illustration.md`
- `publications/active/ipsci-2026/README.md`
- `publications/active/ipsci-2026/submissions/v3-revision/manuscript-v3.md`
- `publications/active/ipsci-2026/supervisor-feedback-response.md`
- `publications/active/journal-1/README.md`
- `publications/active/journal-1/section-5-plan.md`
- `publications/active/journal-1/section-6-plan.md`
- `publications/active/journal-1/submissions/v1-initial-submission/manuscript.md`

New files comprise this continuation report and evidence under `data/publication-consistency-audit/resumed/`. The manifests contain both hashes for each modified file; `edit-log.json` explains their semantic changes.

## Closure assessment and remaining work

| Closure criteria | Status and evidence |
|---|---|
| 1–2: two manuscripts and quantitative coverage | PASS: full text inspection, 1,227 mapped original IDs, result index and source-linked edit log. |
| 3–8: stale values, headlines, counts, attribution, hysteresis, 95.8 | PASS: corrected active prose; historical metric traced; frozen register and outputs match. |
| 9–12: tables, figure, proof, twilight | PASS: targeted verification and formal-definition inspection. Historical twilight descriptions are explicitly retrospective. |
| 13–14: scientific language and policy/evidence | PASS for consistency scope: distinctions documented above, empirical and implementation limits retained. |
| 15–19: P09, P20, observations, human authority, reasons | PASS: explicit scope and operational semantics in working texts. |
| 20–23: history, hashes, register, classifiers | PASS: full baseline comparison; no prediction re-resolution or classifier changes. |
| 24: stop conditions | PASS: no unresolved SC-1 through SC-7. Unsupported hardware amount remains removed. |

No unresolved quantitative blocker remains. Publication readiness still requires solar formulation reference closure, completion of planned Journal 1 sections, implementation/fidelity evidence where claimed in future, and a separate conference reviewer audit of novelty and argument strength. These are disclosed remaining work, not completed deliverables of this consistency audit.

Recommended next task: **Solar Citation Closure**, followed by the separately scoped full conference reviewer audit. Neither task was begun here.

# `PUBLICATION CONSISTENCY AUDIT CLOSED — ACTIVE PUBLICATIONS ALIGNED TO CANONICAL STATE`

---

## Addendum — independent re-verification, 2026-09-09

A later session re-verified this closure without repeating the audit. Read-only; no file was edited by the verification itself.

**Frozen state reproduces exactly.** Prediction register `5574b88e…`, 24 entries, **15 CONFIRMED / 9 REFUTED**, P09 = 3661, P20 = 1529. `canonical_gt.py` `b330bf9f…`, `canonical_figures.py` `cb4f1ee2…`, `hysteresis_analysis.py` `a58af013…`, solar artefacts `057c46a1…` / `da14a8dc…` — all unchanged. This report's own `integrity-after.json` matches the current state for every frozen artefact checked, so nothing has drifted since closure.

**Canonical figures recomputed live from the migrated pipeline:** Level 2 binds **5.81% / 4.48%**; daylight UNSAFE **1,262 / 455**; `g_t` all-hours non-SAFE **86.82% / 90.19%**; `g_r` daylight CAUTION **1.48% / 2.70%**. Hysteresis: **3,661** total transitions, **3,439 scheduled (93.9%)**, **222** non-scheduled, **222 → 199 = 10.4%** reduction, **26** oscillations (**5.2/yr**). The 93.9% replacement for the retired 95.8% is confirmed as live canonical output, not a derived figure.

**Stale-value sweep of both active manuscripts.** Absent as required: 7.7% / 6.0%, 22-confirmed / 2-refuted, 23-confirmed / 1-refuted, "fourteen" per year, 227, 1.55% / 2.99%, 9,133, 24.64%, 32.36%, 95.8%, USD 50. Four residual matches were inspected in context and are all legitimate:

| Match | Location | Disposition |
|---|---|---|
| `5,416` | conference L488 | **Required** — P09 provenance chain, preserved as mandated |
| `22 kn` ×2 | conference L465, L517 | **Correct** — both describe 22 kn as the superseded defect being corrected |
| `6.2%`, `5,416`, `17:00–19:00` | Journal 1 L3 | **Correct** — inside the SDR-001 supersession banner, explicitly labelled provenance |

**Targeted checks.** Totality proof carries 21.6 kn, numeric rainfall 10/20, and solar `g_t` — no 22 kn, no categorical rainfall, no fixed-clock twilight. TABLE VII: 9,135 records, symmetric 42.88%, C0↔C2 48.69%, C1↔C3 **0.00%**. TABLE VI rainfall row 1.48% / 2.70%. Fig. 4 dated 2024-03-20 with frozen sunrise 6.341591 h / sunset 18.452345 h. Attribution intact — P20/P23/P24 to SDR-001, P04/P09/P18/P19 to earlier corrections. Human authority unconditional (3 statements). No unbounded physical-danger language; both `prohibit` occurrences are explicitly governance-bounded, one stating "advisory governance policy, not a departure prohibition". Scalar `cause : Y → {fault, hazard}` is not resurrected in either manuscript. Historical v2.5 unchanged (`dbc3c4e3…`) and retains its original USD 50 text.

**Verdict unchanged.** No stop condition is live; no correction was required. Remaining work is as this report already records: Solar Citation Closure, then the separately scoped conference reviewer audit.
