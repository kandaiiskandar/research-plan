# E5 Authority Assessment

**Batch 6, Task 2**
**Date:** 2026-09-11
**Branch:** design/journal1-post-fidelity-evaluation-plan
**Status decision:** E5 = READY_DESCRIPTIVE
**Task 1 READY classification:** CONFIRMED

---

## 1. E5 Definition Recovery

### Primary source: `publications/active/journal-1/evaluation-specification.md` §11

**What to measure.** Wall-clock latency of one full Layer 2 pass (classification + gate + admissible-set selection + rule-set supply), reported as mean, maximum and tail percentiles (p95, p99). Peak memory and CPU cost during the pass.

**On what hardware.** The low-resource target deployment hardware for Kota Kinabalu coastal fisheries (documented in Section 9 of the manuscript).

**How to report.** Descriptive measurement — mean, maximum, tail percentiles — with the hardware, workload and instrumentation stated. Confidence intervals over the timing distribution are legitimate because timing carries genuine variance.

**Acceptance threshold.** `H3 = X ms` is **OPEN**. No externally justified acceptance criterion exists. **Do not invent one.** If a future paper or standard supplies a threshold, this document should be updated to accept it; until then, the criterion is descriptive only.

**Stated status in evaluation-specification.md §11:** OPEN — requires prototype benchmarking. Blocked by Layer 3 build for realistic end-to-end timing.

### Corroboration: `data/journal1-evaluation-specification/evaluation-specification.csv` row E5/RQ-J2

| Field | Value |
|---|---|
| `evidence_type` | PERFORMANCE |
| `conditions` | C2 (proposed) — the arm carrying the governance overhead |
| `metric` | latency (mean, max, tail percentiles); memory/CPU cost |
| `current_status` | OPEN — requires prototype benchmarking |
| `requires_layer3` | YES (prototype required for realistic timing) |
| `requires_humans` | NO |
| `reporting_boundary` | Acceptance threshold X ms = OPEN; report as descriptive measurement; latency alone admits inferential treatment because timing carries genuine variance |

### Corroboration: `data/journal1-evaluation-specification/metric-audit.csv` row `governance overhead / latency`

| Field | Value |
|---|---|
| `new_classification` | PERFORMANCE |
| `requires_layer3` | YES (prototype required) |
| `disposition` | RETAIN as descriptive performance metric; acceptance threshold OPEN |
| `rationale` | "Genuinely empirical. Report mean/max/tail latency on target hardware. Do not invent an acceptance threshold — none is externally justified." |

---

## 2. Threshold Authority Search

The following searches were conducted across the repository.

### Files containing "latency" in `publications/active/journal-1/*.md`

Five files found:
- `algorithm-specification.md`
- `evaluation-baseline-decision.md`
- `evaluation-specification.md`
- `research-design.md`
- `submissions/v1-initial-submission/manuscript.md`

### Threshold candidates found across all five files

Every mention of a threshold in the journal-1 tree uses the placeholder form `H3 = X ms` or `[X ms]`. No numerical value fills the placeholder anywhere in the repository. The complete set of threshold-relevant occurrences, with classification:

| Location | Text | Classification |
|---|---|---|
| `evaluation-specification.md` §8 | "Its acceptance threshold `H3 = X ms` is **OPEN** — no externally justified value exists, and none is invented." | PLACEHOLDER — not a threshold value |
| `evaluation-specification.md` §11 | "`H3 = X ms` is **OPEN**. No externally justified acceptance criterion exists. **Do not invent one.**" | EXPLICIT PROHIBITION against inventing |
| `evaluation-specification.md` §17 (OPEN-1) | "Governance latency acceptance threshold `H3 = X ms` … No externally justified value exists … Only H3 in acceptance-hypothesis form; RQ-J2 is closed as a descriptive question" | OPEN item, descriptive path unblocked |
| `evaluation-baseline-decision.md` §10 | "Note `[X ms]` is an unfilled placeholder and needs a justified value before it is testable" | PLACEHOLDER |
| `evaluation-baseline-decision.md` §14 | "Supply a justified value for H3's `[X ms]`" | Historical recommendation (not fulfilled) |
| `algorithm-specification.md` (OPEN-B1-6) | "Latency acceptance threshold `H3 = X ms` … No externally justified acceptance criterion exists" | OPEN — unchanged from evaluation-spec |
| `layer3-prototype-specification.md` (OPEN-B1-6) | "Latency acceptance threshold H3 … OPEN — unchanged" | OPEN — unchanged |
| `research-design.md` | "`H3 threshold = OPEN`" | OPEN |
| `manuscript.md` §8 | "`H3 = X ms` remains OPEN" | OPEN |

### Search in `docs/canonical/` for latency/performance thresholds

Files returned: `appendix-c-formalisation.md`, `rq5-study-design.md`, `research-alignment-table.md`, `report-hardware-cost-provenance-2026-09-08.md`, `finding-unsafe-semantics-audit.md`. Inspection of the hardware-cost provenance report confirms that the design plans include "measurable latency/overhead aims (one bound remains `[X ms]`)" — confirming no canonical authority has filled the placeholder.

### Classification of all threshold candidates

**Result: there are no threshold candidates to classify.** The repository contains one threshold placeholder (`H3 = X ms`) that explicitly marks itself as OPEN and unresolved. No numerical value — not even an "industry expectation" or "typical target" — appears anywhere in the corpus in connection with E5. There is no AUTHORITATIVE, CONTEXTUAL, or UNSUPPORTED threshold number to assess; the threshold space is empty.

---

## 3. Answers to the 11 Questions

### Q1. What exactly is E5?

E5 is the performance evaluation workstream for Journal 1, answering RQ-J2: "What runtime latency and computational overhead does Layer 2 introduce on the target deployment hardware?" It measures the wall-clock cost of one full execution of the Layer 2 governance pass (state classification, participation gate check, admissible-set selection, and rule-set supply to Layer 3) on hardware representative of the low-resource coastal fisheries deployment target. It is the only genuinely stochastic measurement in Journal 1 (all other metrics are deterministic census values on the replay trace); timing carries genuine runtime variance, making inferential reporting (mean, tail percentiles) appropriate here and only here.

**Source:** `evaluation-specification.md` §5 (RQ-J2), §11 (performance evaluation), §12 (statistical treatment exception for latency).

### Q2. What does E5 measure?

E5 measures:

1. **Wall-clock latency** of one full Layer 2 pass, reported as: mean, maximum, p95 (95th percentile), p99 (99th percentile).
2. **Peak memory** consumption during the Layer 2 pass.
3. **CPU usage** during the Layer 2 pass.

The measured object is the full Layer 2 governance sequence: classification (`f(E)` = `F_{D,τ}`) + participation gate `G(S)` + admissible-set lookup `A_AI(S)` + rule-set supply `RS(S)`. Partial timing (Layer 2 alone, without a Layer 3 end-to-end call) may be reported as a **lower bound**, per `evaluation-specification.md` §14.

**Source:** `evaluation-specification.md` §11; `evaluation-specification.csv` column `metric`.

### Q3. What environment does E5 require?

**Hardware:** The low-resource target deployment hardware for Kota Kinabalu coastal fisheries. This is characterised as commodity smartphones or low-cost single-board computers (hardware-cost-provenance-2026-09-08.md §4; `evaluation-specification.md` §11 points to "manuscript §9" for the hardware specification). Note: manuscript §9 is currently a placeholder draft — the hardware is characterised as a class, not yet specified as a concrete model. A representative device from the class must be chosen before E5 runs.

**Software:** The Layer 3 prototype (governance module). The evaluation-specification states "requires prototype benchmarking" and "blocked by Layer 3 build for realistic end-to-end timing" — but the Layer 3 prototype has since been built and its fidelity confirmed in Batch 5 (F1, F2, F3 all PASS; see claim-status-matrix.csv rows F1–F3).

**Instrumentation:** Hardware, workload and instrumentation method must be stated in the report. Confidence intervals over the timing distribution are legitimate.

**Source:** `evaluation-specification.md` §11; `evaluation-specification.csv` row E5; `claim-status-matrix.csv` rows F1–F3.

### Q4. Does a pass/fail threshold exist in any authority document?

**No.** The threshold `H3 = X ms` appears in eight locations across the Journal 1 tree and in docs/canonical, uniformly as an unfilled placeholder. Every occurrence explicitly states that no externally justified value exists, that none is invented, and that the criterion is currently descriptive only. No authority document contains a numerical bound for E5 acceptance.

**Source:** All eight locations enumerated in §2 above.

### Q5. Where does any threshold come from?

**Nowhere.** The threshold does not exist. The evaluation-specification explicitly prohibits inventing one: "No externally justified acceptance criterion exists. **Do not invent one.** If a future paper or standard supplies a threshold, this document should be updated to accept it; until then, the criterion is descriptive only." OPEN-1 in `evaluation-specification.md` §17 identifies the gap and scopes its impact: it blocks only H3 in acceptance-hypothesis form; RQ-J2 is closed as a descriptive question. OPEN-B1-6 in `algorithm-specification.md` and `layer3-prototype-specification.md` confirms the same status.

### Q6. Can descriptive latency be reported without an acceptability claim?

**Yes, explicitly.** The evaluation-specification's wording of RQ-J2 was deliberately rewritten from "acceptable for low-resource deployment" (which contained an unsourced threshold) to a pure descriptive performance question. `evaluation-specification.md` §11 states: "Descriptive measurement — mean, maximum, tail percentiles — with the hardware, workload and instrumentation stated." The OPEN-1 item in §17 confirms that the absence of a threshold "blocks only H3 in acceptance-hypothesis form; RQ-J2 is closed as a descriptive question." `research-design.md` states "report as descriptive performance measurement until one does."

A descriptive E5 result — mean, max, p95, p99 latency, memory, CPU, with hardware and instrumentation stated — is fully authorised without any acceptability claim.

### Q7. Does E5 require mobile hardware specifically?

**No — the class is defined, not a specific form factor.** The hardware is characterised as "commodity smartphones or low-cost single-board computers." No Android-only or mobile-first requirement was located in any canonical document (hardware-cost-provenance-2026-09-08.md §4 explicitly states: "No canonical Android-only or mobile-first requirement was located; those possibilities are not asserted as established choices here"). The device-class qualifier "low-resource coastal fisheries deployment target" is functional, not form-factor specific. Any device representative of the defined class may be used, provided it is stated in the report.

### Q8. Does E5 require production deployment?

**No.** E5 requires a built prototype (the governance module). Production deployment — a live fishing-fleet device with real sensors, connectivity, and ongoing use — is not required. The evaluation-specification §14 distinguishes prototype fidelity evidence (F1–F3) from performance evidence (E5) and both from human-validation evidence (outside Journal 1 scope). E5 is a benchmark on the built prototype on representative hardware, not a field measurement.

Note that `evaluation-specification.md` §14 also allows partial Layer 2 timing without the full end-to-end pipeline, reported as a lower bound. However, since Layer 3 is now built (F1–F3 PASS, claim-status-matrix.csv), full Layer 2 + Layer 3 end-to-end timing is now available.

### Q9. What claims would E5 permit if run descriptively?

If E5 is run as a descriptive measurement on the defined hardware class, the following claims are permitted:

- "The mean wall-clock latency of one Layer 2 governance pass on [stated hardware] is X ms (max: Y ms; p95: Z ms; p99: W ms)."
- "Peak memory consumption during a Layer 2 pass is M MB on [stated hardware]."
- "CPU utilisation during a Layer 2 pass is C% on [stated hardware]."
- Confidence intervals over the timing distribution, because timing carries genuine variance.
- A lower-bound statement if partial (Layer 2 alone) timing is used: "The Layer 2-only timing (excluding Layer 3 reasoning) was X ms — a lower bound on full-pipeline latency."
- Contextual characterisation (without an acceptability claim): e.g., comparison against other known governance operations of similar scope, or against the dataset's 1-hour decision cadence.

**Source:** `evaluation-specification.md` §11, §8, §12.

### Q10. What claims would E5 NOT permit without a threshold?

Without an authoritative threshold, the following claims are prohibited:

- "The governance overhead is acceptable for low-resource deployment." (`H3 = X ms` is OPEN; no criterion defines "acceptable".)
- "The latency is negligible." (Requires an established reference for negligibility.)
- "The architecture is suitable for low-resource environments" on the basis of E5 evidence alone. (Requires an acceptability threshold; also broader than latency alone.)
- Algorithmic complexity bounds as E5 evidence. (`algorithm-specification.md` §§26–32 establish O(n) + T_solar_lookup; these are not runtime measurements and do not substitute for E5 — `algorithm-specification.md` explicitly lists six forbidden claims that complexity does not support.)
- Treating unittest runtime from Batch 5 as E5 evidence. (`claim-status-matrix.csv` row E5 explicitly states "E5 not run" in Batch 5.)

**Source:** `evaluation-specification.md` §11, §16 (threats), §17 (OPEN-1); `claim-status-matrix.csv` row E5 `manuscript_claim_prohibited` column; `algorithm-specification.md` §§26–32.

### Q11. What is E5's final status?

**E5 = READY_DESCRIPTIVE.**

All previous blockers have been resolved or clarified:

| Blocker | Resolution |
|---|---|
| Layer 3 not built | **RESOLVED** — F1, F2, F3 all PASS in Batch 5 (claim-status-matrix.csv rows F1–F3). Layer 3 prototype exists and is conforming. |
| Threshold required | **NOT A BLOCKER FOR DESCRIPTIVE** — evaluation-specification.md §11 and §17 (OPEN-1) explicitly allow descriptive reporting without a threshold. H3 = X ms blocks only pass/fail hypothesis closure, not the measurement itself. |
| Hardware not specified | **PARTIAL** — device class defined (commodity smartphones or low-cost SBCs); specific model not yet chosen. Pre-execution step: select a representative device from the defined class and state it in the report. This is a light constraint, not an environment-specification gap that blocks the measurement design. |

The measurement design is fully specified: full Layer 2 pass (classification + gate + A_AI(S) selection + RS(S) supply), on the target hardware class, reported as mean/max/p95/p99 with hardware and instrumentation stated. No further design authority is needed. The execution requires selecting a device and running the benchmark.

---

## 4. Confirmation of Task 1 READY Classification

**Task 1 classified E5 as READY with `blocker = null`.**

**Assessment: CONFIRMED, with two precision notes.**

The READY classification is correct. Both notes refine precision without changing the binary status:

**Note 1 — Mode precision.** The correct vocabulary is **READY_DESCRIPTIVE**, not READY without qualification. The evaluation-specification explicitly distinguishes the descriptive path (open) from the acceptability-claim path (blocked by OPEN-1). The READY status should carry the constraint that E5 may only be run and reported in descriptive mode; no pass/fail assertion is authorised. The `blocker = null` in claim-status-matrix.csv is accurate for the descriptive path.

**Note 2 — Pre-execution step.** One light pre-execution step is needed before running E5: select a specific representative device from the defined hardware class (commodity smartphones or low-cost SBCs, Kota Kinabalu deployment context). This is not a specification gap and does not require new authority — the class is defined, the selection is an implementation choice that must be stated in the report.

---

## 5. Status Decision

```
E5 = READY_DESCRIPTIVE

status          = READY
blocker         = null
evaluation_mode = DESCRIPTIVE
```

### What this status permits in the manuscript

- Descriptive latency table: mean, max, p95, p99 wall-clock latency for one Layer 2 governance pass on [stated hardware].
- Memory and CPU characterisation.
- Confidence intervals over the timing distribution.
- Lower-bound reporting if only Layer 2 (not full end-to-end) timing is measured.
- Comparison with the decision cadence (hourly records) as a contextual reference.

### What this status prohibits in the manuscript

- Any acceptability claim ("acceptable", "suitable", "negligible") without an externally sourced threshold.
- H3 in pass/fail form (`H3 = X ms` remains OPEN — do not fill it with an invented number).
- Citing algorithmic complexity bounds as E5 evidence.
- Citing Batch 5 unittest runtime as E5 evidence.
- Treating E5 evidence as establishing low-resource suitability without a threshold.

### Next action

1. Select a representative device from the defined hardware class. State the device model, OS, and instrumentation method in the experimental record.
2. Deploy the governance module (`governance/`) on the selected device.
3. Run the E5 benchmark: measure mean, max, p95, p99 wall-clock latency for a full Layer 2 pass; record peak memory and CPU.
4. Report the results as a descriptive measurement per `evaluation-specification.md` §11, with hardware, workload and instrumentation stated.
5. Do not assert H3 acceptability — report only the descriptive values.

---

## Appendix: Key Document References

| Document | Relevant section | Role in this assessment |
|---|---|---|
| `publications/active/journal-1/evaluation-specification.md` | §5 (RQ-J2), §8, §11, §12, §14, §16, §17 (OPEN-1) | Primary authority for E5 definition and reporting contract |
| `data/journal1-evaluation-specification/evaluation-specification.csv` | Row E5/RQ-J2 | Machine-readable E5 specification |
| `data/journal1-evaluation-specification/metric-audit.csv` | Row `governance overhead / latency` | Metric classification and disposition |
| `publications/active/journal-1/algorithm-specification.md` | §§26–32, OPEN-B1-6 | Complexity ≠ E5; threshold still OPEN |
| `publications/active/journal-1/layer3-prototype-specification.md` | OPEN-B1-6 | Threshold still OPEN |
| `publications/active/journal-1/research-design.md` | E5/RQ-J2 entry | "H3 threshold = OPEN; report as descriptive" |
| `publications/active/journal-1/submissions/v1-initial-submission/manuscript.md` | §8, §9, §10 | "H3 = X ms remains OPEN"; §9 hardware = draft placeholder |
| `docs/canonical/report-hardware-cost-provenance-2026-09-08.md` | §4, §5 | Hardware class defined; USD 50 removed; no canonical device model required |
| `data/journal1-post-fidelity-plan/claim-status-matrix.csv` | Rows F1, F2, F3, E5 | F1–F3 CLOSED (Layer 3 built); E5 READY, blocker null |
