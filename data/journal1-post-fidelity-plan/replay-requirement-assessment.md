# Replay Requirement Assessment — Layer 3 Retrospective Replay

**Date:** 2026-09-11
**Branch:** `design/journal1-post-fidelity-evaluation-plan`
**Batch context:** Batch 6, Task 3 (post-Batch-5, F1=F2=F3=PASS)
**Question:** Does the now-implemented Layer 3 rule engine need to be connected to the 43,848-hour retrospective environmental replay to satisfy any currently authorised Journal 1 claim?

---

## §1 Dependency Trace — Replay-Related Claims

The 43,848-hour retrospective replay is used in two distinct ways in the Journal 1 authority chain: (a) as the data source for empirical-trace claims (E1–E4, E6), computed by the pre-Layer-3 environmental classifier, and (b) as a potential input to Layer 3 fidelity claims (F1–F3). Each claim is traced below.

### Claim E1 — Pairwise Admissible-Set Divergence

**RQ → claim → metric → required evidence:**

RQ-J3 → pairwise divergence (C0↔C1, C0↔C2) → percentage of departure-window hours where conditions permit different admissible sets → canonical values from `scripts/condition_comparison.py`.

**Status:** CLOSED (`claim-status-matrix.csv` row E1).

**Evidence already captured:** PRIMARY C0↔C1 = 42.88%; C0↔C2 = 48.69%. These are produced by `condition_comparison.py`, which runs the environmental classifier (pre-Layer-3) against the full 43,848-hour window. The condition comparison script applies the mapping tables for C0/C1/C2/C3 directly to the classifier output state S — it does not invoke Layer 3.

**Would Layer 3 connection produce new evidence?** No. E1 measures admissible-set divergence at the Layer 2 output level. The admissible sets A_AI(S) are determined by the safety state S, not by what rules Layer 3 subsequently fires. Connecting Layer 3 to the replay would produce rule activation counts, not divergence percentages. These are orthogonal metrics.

**Is new evidence required?** No. E1 is CLOSED.

---

### Claim E2 — Isolated Level 2 Contribution (Δ_L2)

**RQ → claim → metric → required evidence:**

RQ-J4 → ablation isolating A_AI(S) contribution → Δ_L2 = div(C0,C2) − div(C0,C1) → canonical values from `scripts/condition_comparison.py`.

**Status:** CLOSED (`claim-status-matrix.csv` row E2).

**Evidence already captured:** PRIMARY Δ_L2 = 5.81%; RESOLUTION Δ_L2 = 4.48%. Same source as E1.

**Would Layer 3 connection produce new evidence?** No. Δ_L2 is computed from the difference of two divergence values, both derived from the classifier mapping tables. Layer 3 rule activation patterns do not affect this calculation.

**Is new evidence required?** No. E2 is CLOSED.

---

### Claim E3 — Resolution Sensitivity

**RQ → claim → metric → required evidence:**

RQ-J3/RQ-J4 supporting → dual-configuration reporting → PRIMARY and RESOLUTION values for all empirical claims → `scripts/canonical_figures.py`.

**Status:** CLOSED (`claim-status-matrix.csv` row E3).

**Evidence already captured:** Dual-configuration values exist for E1, E2, E4, E6 from canonical scripts.

**Would Layer 3 connection produce new evidence?** No. Resolution sensitivity is a property of the environmental input data (ERA5-Ocean vs. MFWAM grid resolution) and the classifier, not of Layer 3 rule execution.

**Is new evidence required?** No. E3 is CLOSED.

---

### Claim E4 — Transition and Hysteresis Characterisation

**RQ → claim → metric → required evidence:**

RQ-J4 supporting → state transition characterisation → transition count; genuine oscillation count (per year); hysteresis reduction share → `scripts/hysteresis_analysis.py`.

**Status:** CLOSED (`claim-status-matrix.csv` row E4).

**Evidence already captured:** 3,661 state transitions in 5 years; 26 genuine oscillations (5.2/yr); hysteresis reduces non-scheduled transitions by 10.36%.

**Would Layer 3 connection produce new evidence?** No. Hysteresis is a property of the state sequence produced by the Layer 2 classifier. It is computed from state transitions, not from Layer 3 rule activations. Layer 3 fires within states, not across them.

**Is new evidence required?** No. E4 is CLOSED.

---

### Claim E6 — C1 ↔ C3 Trace Confirmation (J1-P1)

**RQ → claim → metric → required evidence:**

RQ-J1 novelty argument → trace confirmation of Proposition J1-P1 → C1 ↔ C3 divergence = 0.00% → `scripts/condition_comparison.py`.

**Status:** CLOSED (`claim-status-matrix.csv` row E6).

**Evidence already captured:** 0.00% divergence over 43,848 hours, PRIMARY and RESOLUTION.

**Would Layer 3 connection produce new evidence?** No. J1-P1 is an admissible-set equivalence proposition (A_C1(S) = A_C3(S) for all S). The mapping tables for C1 and C3 are identical dict literals in `condition_comparison.py`; the 0.00% result is a confirmation of implementation consistency, not a Layer 3 measurement.

**Is new evidence required?** No. E6 is CLOSED.

---

### Claims F1, F2, F3 — Implementation-Fidelity Criteria

**RQ → claim → metric → required evidence:**

RQ-J1 → Safety Dominance implementation conformance → F1: no recommendation outside A_AI(S); F2: violation count = 0; F3: RS(S) switching correctness → Batch 5 evaluation against the interface-contract-exhaustive fidelity state space (292 episodes).

**Status:** All CLOSED — PASS (`claim-status-matrix.csv` rows F1, F2, F3).

**Evidence already captured:** F1 PASS: 0 violations / 292 primary episodes / 454 advisory records. F2 PASS: violation count = 0 / 244 advisory-producing episodes. F3 PASS: mismatches = 0 / 292 episodes. Source: `data/journal1-layer3-prototype/batch5-fidelity-evaluation/report.md` §13–15 and `fidelity-results.json`.

**Critical scoping note from `claim-status-matrix.csv`:** The F1 claim definition explicitly states "denominator = interface-contract-exhaustive primary episode count" and lists as a PROHIBITED claim "Claiming F1 PASS constitutes a proof of Safety Dominance; claiming F1 covers the 43,848-hour retrospective replay." The specification deliberately bounded F1–F3 to the 292-episode interface-contract fidelity state space, not the 43,848-hour retrospective replay.

**Would connecting Layer 3 to the 43,848-hour replay produce new evidence for F1–F3?** No. The fidelity criteria are closed under the 292-episode test. The replay would produce a larger denominator, but the claim as authorised does not require the larger denominator. The Safety Dominance Property holds by proof (Theorem 6.3, `appendix-c-formalisation.md` C.3 and C.7.2); F1–F3 test implementation conformance to the assumptions A1–A4 on which the proof rests. The 292-episode fidelity state space provides exhaustive coverage of the interface-contract conditions. Extending to 43,848 hours would not add fidelity test coverage beyond what is already proved analytically.

**Is new evidence required?** No. F1–F3 are CLOSED.

---

### Claim E5 — Governance Latency (Performance)

**RQ → claim → metric → required evidence:**

RQ-J2 → descriptive latency measurement → mean, max, p95, p99 wall-clock; peak memory and CPU → benchmarking on target hardware.

**Status:** READY_DESCRIPTIVE (`e5-authority-assessment.md`, Batch 6 Task 2).

**Does E5 require the 43,848-hour replay?** No. E5 measures the wall-clock cost of one Layer 2 pass on the target deployment hardware. The 43,848-hour trace is not the input — a representative set of timing measurements is. No authority document requires that timing measurements be collected by running Layer 3 through the full historical replay.

**Is the retrospective replay required for E5?** No.

---

## §2 Batch 4B-2 Activation Projection Classification

**Document:** `data/journal1-layer3-prototype/batch4b2-component-state-rules/canonical-rule-activation-analysis.md`

**What the document contains:** A projection of expected rule activation counts for each CAUTION rule (R-CAUTION-001 through R-CAUTION-004) against the 43,848-hour replay (D = {m}, PRIMARY configuration). The counts are derived by reasoning from known empirical binding profiles:

| Rule | Expected activations | Reasoning |
|---|---|---|
| R-CAUTION-001 | 0 | m ∈ D throughout; predicate always FALSE |
| R-CAUTION-002 | ~g_o binding rate | Fires when component_o_state == "CAUTION" and S = CAUTION |
| R-CAUTION-003 | ~g_r binding rate | Fires when component_r_state == "CAUTION" and S = CAUTION |
| R-CAUTION-004 | 0 or near 0 | g_w activates 2 times / 43,848 hours and never binds (F-17) |

**Classification: DESIGN PROJECTION**

**Reasoning:** The activation counts are not produced by executing Layer 3 against the 43,848-hour replay. They are derived by reasoning from confirmed empirical values already established in the canonical record (g_o dominance at 98.71%/97.66% of daylight CAUTION classifications, g_w activating twice with 0 bindings per F-17, g_r binding share). The document itself uses the phrase "Expected activations" and "Reasoning" — not "Observed activations" or "Measured."

The projection correctly reasons from the binding architecture of the classifier, but it constitutes a design argument about what Layer 3 WOULD produce, not an empirical confirmation that it DID produce those results. This is a meaningful design artefact — it confirms internal consistency between the rule set design and the empirical binding profiles — but it is not executable confirmation.

**Could it be promoted to REQUIRES EXECUTABLE CONFIRMATION?** Only if an authorised claim required empirical rule activation counts. No current Journal 1 claim does. The fidelity claims (F1–F3) are satisfied by the 292-episode Batch 5 test, and the empirical-trace claims (E1–E4, E6) do not reference rule activation counts at all.

**Classification summary:**

```
Batch 4B-2 canonical-rule-activation-analysis.md = DESIGN PROJECTION
```

The projection is internally consistent with the empirical record and serves as supporting design documentation. It must not be cited as empirical evidence of rule activation counts or Layer 3 behaviour in the retrospective window. Do not promote to SUPPORTING ANALYSIS without a corresponding claim that requires it as evidence.

---

## §3 New Evidence Analysis — What Replay Would Produce vs. What Already Exists

If the Layer 3 rule engine were connected to the 43,848-hour retrospective replay and run to completion, it would produce:

1. **Rule activation counts** — how many hours each CAUTION rule fired. The Batch 4B-2 projection already characterises the expected values analytically. The primary finding (g_o dominance → R-CAUTION-002 dominates; R-CAUTION-001 = 0 due to D={m}; R-CAUTION-004 = 0 due to g_w never binding) is predictable from the existing empirical record. A run would confirm or refute the projection.

2. **Advisory record counts** — how many Delay advisories were generated under CAUTION, and their rule provenance. This adds a Layer 3 operational characterisation that does not exist in the current evidence base.

3. **Concurrent activation patterns** — when multiple CAUTION components are active simultaneously (multiple rules fire). This is a secondary characterisation of the rule engine's multi-rule behaviour.

**What already exists:**
- All admissible-set divergence values (E1–E4, E6) — CLOSED, do not require Layer 3
- All fidelity results (F1–F3) — CLOSED via 292-episode Batch 5 test
- All formal proofs (P1–P4) — independent of empirical execution
- The Batch 4B-2 design projection characterises expected Layer 3 behaviour analytically

**Assessment:** Connecting Layer 3 to the 43,848-hour replay would produce additional descriptive characterisation of rule activation patterns — specifically, actual vs. projected activation counts and advisory attribution by rule. This is potentially useful supporting material but is not required by any currently authorised claim. No claim in the evaluation-specification.csv or claim-status-matrix.csv specifies rule activation counts, advisory attribution by rule, or Layer 3 operational statistics on the historical replay as required evidence.

The distinction between the replay and the fidelity test space is explicit in the claim definitions: F1's claim definition at `claim-status-matrix.csv` prohibits "claiming F1 covers the 43,848-hour retrospective replay" and bounds the denominator to the 292-episode interface-contract state space.

---

## §4 Conclusion

```
L3_RETROSPECTIVE_REPLAY = NOT_REQUIRED
```

**Justification:** No currently authorised Journal 1 claim requires connecting the Layer 3 rule engine to the 43,848-hour retrospective environmental replay. The retrospective replay claims (E1–E4, E6) are computed from the environmental classifier (pre-Layer-3 condition_comparison.py) and are CLOSED. The fidelity claims (F1–F3) are CLOSED via the 292-episode interface-contract fidelity test space in Batch 5; the evaluation-specification explicitly bounds these to the fidelity state space and prohibits characterising F1 as covering the retrospective replay. The formal claims (P1–P4) require no empirical execution. The performance claim (E5) requires hardware benchmarking, not replay execution. The Batch 4B-2 activation projection is classified as a DESIGN PROJECTION — a consistent and useful design artefact derived from confirmed empirical binding profiles, but not empirically confirmed Layer 3 execution, and not required by any authorised claim. Connecting Layer 3 to the replay would produce descriptive rule activation statistics that are currently neither claimed nor authorised; adding them without a corresponding authorised claim would introduce unclaimed evidence into the evidence base.

---

*Author: iskandar · Date: 2026-09-11 · Batch 6 Task 3*
