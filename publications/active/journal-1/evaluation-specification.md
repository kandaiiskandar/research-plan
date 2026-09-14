# Journal 1 — Evaluation Specification

**Status:** CLOSED — this document is the single maintained design authority for Journal 1 evaluation
**Closed on:** 2026-09-10
**Branch:** `design/journal1-evaluation-specification`
**Task:** [`docs/tasks/Journal-1-Evaluation-Specification-Alignment.md`](../../../docs/tasks/Journal-1-Evaluation-Specification-Alignment.md)
**Evidence directory:** [`data/journal1-evaluation-specification/`](../../../data/journal1-evaluation-specification/)

---

## 1. Purpose

Convert the accepted evaluation baseline decision — **Option C** in [`evaluation-baseline-decision.md`](evaluation-baseline-decision.md) — into a final, internally coherent evaluation specification, so that Journal 1 can proceed to write results, tables, figures and implementation benchmarking against exactly one meaning per condition label, hypothesis and metric.

This document distinguishes:

- **what is proved** (formal propositions with proofs deferred to Section 6 of the manuscript);
- **what is deterministic** (structural equivalences that follow from mapping literals);
- **what is descriptively measured** (empirical-trace results from the retrospective replay);
- **what is implementation-fidelity evidence** (fidelity criteria measured against the built Layer 3 prototype);
- **what requires human validation** (constructs for a future user study, explicitly outside Journal 1).

No new experiments are run here, no canonical empirical results are modified, and no canonical architecture decision is reopened.

---

## 2. Accepted baseline decision

Option C in [`evaluation-baseline-decision.md`](evaluation-baseline-decision.md) is accepted and is not reopened.

Its content in one sentence: run a three-arm primary experiment (C0 Ungated / C1 Binary-gated / C2 Proposed) and treat the Flehmig-style traffic-light governance topology (C3) as a **structural proposition** — proved by finite-mapping comparison and confirmed against the retrospective replay — rather than as a fourth experimental arm.

Two bounded wording issues in the baseline decision record were corrected before that record was used as authority here:

- **§12 Statistical treatment** — "complete enumeration over the full population" replaced with "deterministic census of all hourly records in the predefined retrospective study window", to make explicit that the census is scoped to the analysed window and its values are not estimates of future Sabah operating conditions.
- **§14 Deferred question 4** — "If Layer 3 is built before submission, do H1/H2 become genuinely empirical? (Likely yes …)" replaced with the correct claim: Layer 3 implementation makes compliance and violation rates **implementation-fidelity measurements**, and does not convert a formal governance invariant (Safety Dominance) into a behavioural hypothesis.

Both repairs are recorded in [`data/journal1-evaluation-specification/change-map.csv`](../../../data/journal1-evaluation-specification/change-map.csv).

---

## 3. Condition definitions

The Journal 1 primary experiment uses canonical condition labels. The earlier Journal-local labels (`C1/C2/C3 = Ungated/Binary/Proposed`), which inverted `C2` relative to the canonical harness, have been retired before any Journal 1 result was produced. The temporary translation table in the working manuscript has been retired with a provenance note.

| Canonical label | Name | A_AI(SAFE) | A_AI(CAUTION) | A_AI(UNSAFE) | Governance active |
|---|---|---|---|---|---|
| **C0** | Ungated | FULL | FULL | FULL | None |
| **C1** | Binary-gated | FULL | FULL | ∅ | Level 1 only (participation gate G) |
| **C2** | Proposed graduated architecture | FULL | {Go, Delay} | ∅ | Level 1 + Level 2 (G and A_AI) |

where `FULL = {Go, Delay, DepartureTime, Duration}` and `∅` denotes the empty admissible set.

`C1` and `C2` differ only in `A_AI(CAUTION)`. That single cell — restricted to {Go, Delay} in C2, unchanged as FULL in C1 — is the axis on which the architectural contribution is directly observable.

The condition-label audit (18 occurrences audited across the maintained Journal 1 tree) is at [`condition-label-audit.csv`](../../../data/journal1-evaluation-specification/condition-label-audit.csv). Historical section plans (`section-5-plan.md`, `section-6-plan.md`) retain their earlier labels behind a superseded-audit banner; they are not maintained design artefacts.

---

## 4. Structural comparator (C3)

**C3 is not a fourth experimental arm.** It is retained as a **structural comparator** addressing the novelty objection.

| Canonical label | Name | A_AI(SAFE) | A_AI(CAUTION) | A_AI(UNSAFE) |
|---|---|---|---|---|
| **C3** | Flehmig-style traffic-light topology | FULL | FULL | ∅ |

At the admissible-recommendation-set level, `C1 ≡ C3` by inspection of the mapping literals in [`scripts/condition_comparison.py`](../../../scripts/condition_comparison.py) lines 90–105:

```python
"C1": {SAFE: FULL, CAUTION: FULL, UNSAFE: EMPTY},
"C3": {SAFE: FULL, CAUTION: FULL, UNSAFE: EMPTY},
```

**Fairness qualification.** Flehmig et al. (2024) condition their traffic-light index on AI degradation (drift, outliers, performance decay), not on environmental state. C3 ports their **governance topology** onto the shared state axis in order to compare admissible-output structure. It is not a reproduction of their system, and it is not a claim that their framework is deficient — their framework answers a different question and is correct for it. This fairness qualification travels with every mention of C3 in this document, in the manuscript, and in the audit CSVs. Do not write "Flehmig's actual system was reproduced", "Flehmig's architecture was empirically tested", "Flehmig is deficient" or "its orange state is useless".

The proposition itself is stated in Section 6 (Proposition J1-P1).

---

## 5. Research questions

Four research questions carry the Journal 1 evaluation. Each is tagged with a single evidence type and identifies the conditions and metrics that produce evidence for it. Full per-RQ audit — current wording, construct, evidence type, conditions, metrics, validity and required change — is at [`rq-audit.csv`](../../../data/journal1-evaluation-specification/rq-audit.csv).

| RQ | Wording | Evidence type | Conditions | Metrics |
|---|---|---|---|---|
| **RQ-J1** | Can the Safety Dominance Property be proved formally, and under what assumptions does it hold? | **FORMAL** | n/a | Proof (Theorem 6.3) |
| **RQ-J2** | What runtime latency and computational overhead does Layer 2 introduce on the target deployment hardware? | **PERFORMANCE** | C2 (the arm carrying the overhead) | E5 (latency mean/max/tail; memory/CPU) |
| **RQ-J3** | On the retrospective replay, how do the admissible-recommendation-set outputs of C2 differ from C1 and C0, and what share of the divergence is attributable to Level 2 alone? | **EMPIRICAL-TRACE** | C0, C1, C2 | E1 (pairwise divergence); E2 (isolated Level 2 contribution); E3 (resolution sensitivity) |
| **RQ-J4** | Which architectural component of the governance pair (G(S) vs. A_AI(S)) accounts for the observed C2 vs. C1 divergence? | **EMPIRICAL-TRACE** | C0, C1, C2 (Δ_L2 ablation) | E2 (Δ_L2); E4 (transition and hysteresis characterisation, supporting) |

Rationale for each rewording is in [`rq-audit.csv`](../../../data/journal1-evaluation-specification/rq-audit.csv). RQ-J3's earlier wording ("outperform … on advisory scope compliance") collapsed three evidence types (FORMAL invariant, IMPLEMENTATION-FIDELITY test, EMPIRICAL-TRACE comparison) and has been corrected to a pure empirical-trace comparison. RQ-J2's earlier "acceptable for low-resource deployment" hid an unsourced acceptance threshold and has been rewritten as a descriptive measurement.

---

## 6. Formal propositions

Four formal claims are proved, not tested.

- **P1 Totality** — for all valid E, `f(E)` returns exactly one element of `{SAFE, CAUTION, UNSAFE}`. The operational classifier `F_{D,τ} = f ∘ ρ_{D,τ}` is total under valid startup configuration. Proof: Theorem 6.1 (manuscript §6.2; appendix-c C.1 and the C.1b operational extension).

- **P2 Monotonicity** — `S₁ ≻ S₂ ⇒ A_AI(S₁) ⊆ A_AI(S₂)`, with strict containment `A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅`. Proof: Theorem 6.2 (manuscript §6.3; appendix-c C.2).

- **P3 Safety Dominance** — for all E, `AI(E) ⊆ A_AI(f(E))`; and if `f(E) = UNSAFE` then `AI(E) = ∅`. Proof by construction from the RS(S) supply mechanism, under assumptions A1–A4 (Layer 3 rule-engine; RS(S) supply; gate enforcement; engine fidelity). Theorem 6.3 (manuscript §6.4; appendix-c C.3 and C.7.2).

- **P4 (J1-P1) C1 ≡ C3 admissible-set equivalence.**

  **Proposition J1-P1.** *At the admissible-recommendation-set level, the binary participation gate C1 and the Flehmig-style governance topology C3 are output-equivalent under the comparison mapping.*

  **Proof.** By finite-mapping comparison from the canonical mapping tables:

  ```
  A_C1(SAFE)    = FULL              A_C3(SAFE)    = FULL
  A_C1(CAUTION) = FULL              A_C3(CAUTION) = FULL
  A_C1(UNSAFE) = ∅                  A_C3(UNSAFE) = ∅
  ```

  Both mappings agree at every `S ∈ {SAFE, CAUTION, UNSAFE}`. Therefore `A_C1(S) = A_C3(S)` for all S. ∎

  **Fairness qualification.** As in Section 4: Flehmig et al. condition their traffic-light index on AI degradation. J1-P1 ports their governance topology onto the shared state axis to compare admissible-output structure; it does not reproduce, test or dispute their framework.

  **Three levels of evidence for J1-P1, kept separate:**

  | Level | Claim | Status |
  |---|---|---|
  | **Analytical** | `A_C1(S) = A_C3(S)` for all S | Proved in one line from the mapping definitions above |
  | **Executable** | The implemented harness preserves the mapping | Trivially true — the two entries in the harness are literally identical dict literals (`condition_comparison.py` lines 95, 101) |
  | **Trace confirmation** | `C1 ↔ C3 = 0.00%` divergence over 43,848 hours | Confirms the harness computed what the tables say — a harness-consistency check |

  **The 0.00% replay value is confirmation of implementation consistency, not discovery of an uncertain physical phenomenon.** State this explicitly wherever the number appears.

---

## 7. Implementation-fidelity criteria

Three fidelity criteria test whether the Layer 3 build conforms to the specification. **None of these criteria is a re-proof of Safety Dominance or a behavioural hypothesis.** They test that the code matches the specification.

- **F1** — The Layer 3 rule engine produces no recommendation type outside `A_AI(S)` across an exhaustive test suite / replay: `∀ (E, r ∈ AI(E)) : r ∈ A_AI(f(E))`.
- **F2** — The observed count of recommendations outside `A_AI(S)` is exactly zero. *Expected value analytically zero under a conforming implementation (follows from P3).*
- **F3** — RS(S) rule-set switching follows state transitions correctly; no stale rule-set persists across a transition.

**Status:** all three are **CLOSED — PASS** (Batch 5 implementation-fidelity evaluation, 2026-09-11). See Section 14.

Measured over **292 primary episodes** (32 SAFE, 260 CAUTION) producing **454 advisory records** across **244 episodes with a non-empty advisory**: **F1 violations = 0**, **F2 violation count = 0**, **F3 mismatches = 0**. The remaining 16 CAUTION episodes produced `AI(E) = ∅` because no implemented rule predicate evaluated TRUE, which is not a fidelity failure — `A_AI(S)` defines admissibility, not a requirement that an advisory exist. A further **162 UNSAFE gate-off cases** exercise the `G(S) = 0` path in which Layer 3 is not invoked; **these are counted separately and are not part of the 292 primary episodes**. Evidence: [`data/journal1-layer3-prototype/batch5-fidelity-evaluation/`](../../../data/journal1-layer3-prototype/batch5-fidelity-evaluation/).

**Bounded interpretation — read this with the result.** The evaluation scope is **interface-contract exhaustive**: it enumerates the Layer 3 interface state space and is not the retrospective replay, not historically or environmentally exhaustive, and not exhaustive over deployment conditions. It was run against the **implemented rule configuration**, which is the four CAUTION rules; **`R-SAFE-001` remains DEFERRED, so `RS(SAFE)` is empty**, all 32 SAFE episodes generated zero advisories, and the only conclusion type the prototype generates is `Delay`. F1–F3 therefore demonstrate implementation fidelity over the evaluated interface-contract state space and implemented rule configuration. They do **not** demonstrate fidelity of a populated SAFE rule set, do not establish that every type in `A_AI(SAFE)` was exercised, and are not behavioural or real-world validation.

*Status synchronised 2026-09-13 by the F1–F3 / E5 status-synchronisation micro-repair. This section, §1, §11, §14, §17 and §18 previously represented F1–F3 as OPEN and Layer 3 as unbuilt — wording that predated the Batch 5 evaluation of 2026-09-11 and was superseded by it, as §18 already noted. No fidelity criterion, metric, condition, threshold or evaluation-design decision was changed, and no result was recomputed; only status representation was corrected. E5 remains OPEN.*

The fidelity criteria replace the previous behavioural hypotheses H1 and H2. The reclassification and its rationale are in [`hypothesis-audit.csv`](../../../data/journal1-evaluation-specification/hypothesis-audit.csv). H1 asked whether the graduated architecture achieves *higher advisory scope compliance* than baselines: under Theorem 6.3, compliance for C2 is 100% by proof, and C0/C1 have no scope restriction to violate — H1 was either trivially true or measured an undefined quantity. H2 asked about the *false positive rate* of recommendations outside `A_AI(S)`: analytically zero under a conforming implementation, so again a fidelity check rather than a behavioural hypothesis.

---

## 8. Empirical hypotheses

Journal 1 carries no free-standing empirical hypotheses in the H1–H4 sense. The empirical claims are stated as **trace results** (Section 9), because the retrospective replay is a deterministic census — a claim about the trace, not a claim to be tested against an alternative.

- The **isolated Level 2 contribution** E2 (`Δ_L2`) is the load-bearing empirical result and replaces the former H4. It is uncertain in its magnitude across datasets and configurations (E3), but not in its sign under a conforming implementation of the specification. The canonical value on the analysed window is 5.81% PRIMARY / 4.48% RESOLUTION.
- The **performance criterion** E5 / RQ-J2 (governance latency) is the only genuinely stochastic measurement because timing carries variance from the runtime environment. Its acceptance threshold `H3 = X ms` is **OPEN** — no externally justified value exists, and none is invented. See Section 11.

---

## 9. Metrics

The final metric set — nine items, each with a single classification and a stated purpose — is in [`metric-audit.csv`](../../../data/journal1-evaluation-specification/metric-audit.csv).

| ID | Metric | Classification | Answers |
|---|---|---|---|
| M-Fidelity-F1 | Recommendation type outside A_AI(S) — occurrence check | FIDELITY | F1 |
| M-Fidelity-F2 | Violation count on exhaustive suite / replay | FIDELITY | F2 |
| M-Fidelity-F3 | RS(S) switching correctness at transitions | FIDELITY | F3 |
| M-Empirical-E1 | Pairwise admissible-set divergence (C0↔C1, C0↔C2, C1↔C2) | DESCRIPTIVE (empirical-trace) | RQ-J3 |
| M-Empirical-E2 | Isolated Level 2 contribution Δ_L2 = div(C0,C2) − div(C0,C1) | DESCRIPTIVE (empirical-trace) | RQ-J4 |
| M-Empirical-E3 | Resolution sensitivity: report PRIMARY and RESOLUTION for empirical quantities whose design supports a like-for-like comparison. **Mandatory scope {E1, E2, E6}**; E4 excluded (`E4_RESOLUTION = NOT_REQUIRED_BY_CURRENT_E3_DESIGN`, §13) | DESCRIPTIVE (sensitivity) | RQ-J3 / RQ-J4 supporting |
| M-Empirical-E4 | Transition and hysteresis characterisation, **PRIMARY chronology only** (transitions; genuine oscillations/yr; hysteresis reduction share). Outside the E3 mandatory dual-configuration scope — §13 | DESCRIPTIVE | RQ-J4 supporting |
| M-Empirical-E6 | C1 ↔ C3 divergence (canonical confirmation of J1-P1) | DESCRIPTIVE (implementation-consistency confirmation) | Novelty argument (P4 / J1-P1) |
| M-Performance-E5 | Governance latency and computational overhead of Layer 2 | PERFORMANCE | RQ-J2 |

Two metrics from the original Journal 1 list are dropped or reclassified:

- *Advisory scope compliance rate* — reclassified as fidelity check (F1) rather than a comparative behavioural metric. Rationale: analytically 100% for C2 under P3 and trivially 100% for C0/C1 against their own admissible-set definitions.
- *False positive rate* — reclassified as fidelity check (F2). Rationale: analytically zero under a conforming implementation.

One metric is marked OPEN:

- **Decision-support utility** — `OPEN — CONSTRUCT DEFINITION REQUIRED`. No operational definition on the replay alone has been established. Possible operational meanings (ground-truth recommendation correctness, fisher preference, decision quality, actionability, task completion, real-world outcome) each require a different data source and study design. Do not invent a utility formula. Deferred to a future user study (thesis RQ5 scope). Marking this OPEN does not block the rest of the specification.

Canonical metrics adopted:

- **Pairwise admissible-set divergence** and **isolated Level 2 contribution** are the two canonical metrics from `scripts/condition_comparison.py` adopted for E1, E2 and E6.

---

## 10. Ablation design

**Primary ablation — Isolated Level 2 contribution (Δ_L2).**

Removing the advisory-scope restriction reduces C2 to C1 behaviour by construction. The load-bearing ablation metric is measured on the retrospective replay:

**Δ_L2 = divergence(C0, C2) − divergence(C0, C1)**

Canonical departure-window values from [`scripts/condition_comparison.py`](../../../scripts/condition_comparison.py):

| Configuration | div(C0,C1) | div(C0,C2) | Δ_L2 |
|---|---|---|---|
| PRIMARY (5.00 yr, ERA5-Ocean ~50 km) | 42.88% | 48.69% | **5.81%** |
| RESOLUTION (3.25 yr, MFWAM ~8 km) | *canonical value* | *canonical value* | **4.48%** |

Because C0 and C1 differ only in Level 1 (participation gate) while C0 and C2 differ in Levels 1 + 2 combined, the subtraction removes the Level 1 term and isolates the Level 2 contribution.

**Secondary ablations:**

- **Remove participation gate** (`G(S) = 1` always) — realised by C0's configuration for AI participation; report as an interpretive comparison against C1 rather than as a separately implemented ablation.
- **Remove hysteresis smoothing** — measured under the canonical specification (F-6): 3,661 state transitions in five years; 26 genuine oscillations (5.2/yr); hysteresis reduces non-scheduled transitions by 10.36% at hourly resolution. Frame hysteresis as a retained low-cost precaution, not as a mitigation for an observed instability. Do not re-run.
- **Remove worst-case aggregation** — evaluated via boundary scenarios SC-16–SC-20 in [`docs/canonical/evaluation-design-rq4.md`](../../../docs/canonical/evaluation-design-rq4.md), retained as boundary/fail-safe cases inside the empirical frame.

---

## 11. Performance evaluation

Governance latency and computational overhead of Layer 2 on the target deployment hardware (metric M-Performance-E5, answering RQ-J2).

- **What to measure.** Wall-clock latency of one full Layer 2 pass (classification + gate + admissible-set selection + rule-set supply), reported as mean, maximum and tail percentiles (p95, p99). Peak memory and CPU cost during the pass.
- **On what hardware.** The low-resource target deployment hardware for Kota Kinabalu coastal fisheries (documented in Section 9 of the manuscript).
- **How to report.** Descriptive measurement — mean, maximum, tail percentiles — with the hardware, workload and instrumentation stated. Confidence intervals over the timing distribution are legitimate because timing carries genuine variance.
- **Acceptance threshold.** `H3 = X ms` is **OPEN**. No externally justified acceptance criterion exists. **Do not invent one.** If a future paper or standard supplies a threshold, this document should be updated to accept it; until then, the criterion is descriptive only.

**Status:** **OPEN — requires target-hardware benchmarking.** The Layer 3 build is no longer the blocker: the prototype is implemented and the benchmark harness is validated (`E5_HARNESS = CLOSED`). A **development-machine reference** run is complete (`MACBOOK_REFERENCE = COMPLETE`, `MACBOOK_CLASSIFICATION = DEVELOPMENT_MACHINE_REFERENCE`, `target_hardware_evidence = false`); it validates the measurement methodology and is **not** deployment, target-hardware, mobile or real-time performance evidence, and must not be scaled or extrapolated to a target device. The outstanding dependency is measurement on representative physical hardware (`E5_ANDROID_TARGET_BENCHMARK = DEFERRED_MANDATORY`), deferred for want of a device. `H3 = X ms` remains **OPEN/UNSUPPORTED**; a low reference latency is not a threshold pass.

---

## 12. Statistical treatment

The retrospective replay is a **deterministic census of all hourly records in the predefined retrospective study window (Kota Kinabalu, 2020–2024 — 43,848 hourly records; the RESOLUTION configuration covers a 3.25-year subset)**. It is not a random sample from a broader climatological population.

For deterministic replay metrics — pairwise divergence, binding rates, component shares, transition counts, Δ_L2 — report **exact descriptive values** for the analysed trace and configuration. Do not apply p-values, confidence intervals or significance tests. There is no sampling and no stochastic component in the classifier.

Values reported for the deterministic replay (5.81%, 4.48%, 0.00%, 42.88%, 48.69%, 3,661 transitions, etc.) are **exact descriptive values for the analysed trace/configuration**, not estimates of all future Sabah operating conditions.

The one exception is **governance latency** (Section 11): timing measurements carry genuine variance from the runtime environment, and inferential treatment (mean, tail percentiles, distribution reporting) is appropriate there.

---

## 13. PRIMARY / RESOLUTION reporting

Journal 1 preserves the canonical dual-configuration reporting contract:

- **PRIMARY** — 5.00 yr, ERA5-Ocean sea-cell (~50 km resolution). Headline configuration.
- **RESOLUTION** — 3.25 yr, MFWAM sea-cell (~8 km resolution). Resolution-sensitivity check.

**Cross-configuration resolution sensitivity is reported under PRIMARY and RESOLUTION for empirical quantities whose evaluation design supports a like-for-like comparison.** The difference between the two is a **resolution-sensitivity result**, not a confidence interval. Do not write "`5.81 ± something`".

**Mandatory dual-configuration scope: E3 covers {E1, E2, E6}.** For those quantities both configurations exist and must both be reported. A quantity inside this scope that is available under only one configuration must state that explicitly and identify the missing configuration.

**E4 is outside the mandatory scope: `E4_RESOLUTION = NOT_REQUIRED_BY_CURRENT_E3_DESIGN`.** E4 characterises temporal dynamics — transition, oscillation and hysteresis counts — over its predefined PRIMARY chronology. A valid sensitivity comparison would require an explicitly comparable temporal design; raw event counts drawn from differing source windows and temporal coverage are not directly comparable merely because both configurations are named PRIMARY and RESOLUTION. E4 is therefore reported as a PRIMARY temporal-dynamics characterisation, and cross-configuration sensitivity for E4 lies outside the current E3 comparison contract.

**`NOT_REQUIRED` means exactly that.** It does not mean ZERO, NOT_FOUND, FAILED or REFUTED. In particular, this specification does **not** claim that E4 is insensitive to resolution, that E4 would reproduce under MFWAM, or that a RESOLUTION E4 result equals the PRIMARY one — none of these has been tested. Nor does it imply that a required experiment was omitted. Any future E4 sensitivity evaluation must be separately authorised and would need to control for common temporal coverage, comparable input availability, and normalised transition and oscillation rates under equivalent hysteresis parameters.

*Scope corrected 2026-09-13 by the E3/E4 resolution-sensitivity authority micro-repair. This clause previously read "Every empirical figure in Journal 1 must be reported under both configurations", which conflicted with E4's authoritative PRIMARY-only evidence and would have prohibited E4's own permitted reporting. Both E3 and E4 remain CLOSED; no empirical result changed.*

Reference: `scripts/canonical_figures.py` (authoritative source for §0a of [`docs/canonical/empirical-findings-2026-09-06.md`](../../../docs/canonical/empirical-findings-2026-09-06.md)).

---

## 14. Layer 3 dependency

Current state: Layer 3 is **specified and implemented**. The rule-based engine, the RS(S) supply mechanism (Algorithm 3), the `ComponentStateTrace` Layer 2 → Layer 3 interface and the four CAUTION rules `R-CAUTION-001`–`R-CAUTION-004` are implemented; `R-SAFE-001` remains **DEFERRED**. It is a **research prototype**, not a production deployment, an operational maritime system, a validated field system or a complete recommendation engine.

**Journal 1 therefore distinguishes:**

- **Formal architecture evidence** — Theorems 6.1–6.3 (P1, P2, P3) and Proposition J1-P1 (P4). These hold by proof, under the stated engine assumptions. Present-tense evidence for Journal 1.
- **Empirical / trace evidence** — E1, E2, E3, E4, E6. All measurable on the classifier alone (Layer 1 + Layer 2). Already present-tense evidence.
- **Prototype fidelity evidence** — F1, F2, F3. **CLOSED — PASS** (Section 7), bounded to the interface-contract state space and the implemented rule configuration. **Do not write future-tense planned implementation as completed experimental evidence, and do not read the closure as covering a populated SAFE rule set.**
- **Performance evidence** — E5 / RQ-J2. **OPEN.** The harness is validated and a development-machine reference run is complete; target-hardware measurement remains outstanding and mandatory (Section 11).

The fidelity criteria do not empirically rediscover Safety Dominance. They test whether the implementation conforms to the specification.

---

## 15. Human-validation boundary

Journal 1 makes no claim about human decision quality, trust, calibrated reliance, actionability, task completion or real-world safety outcomes. These constructs require field data (a user study, incident records) that Journal 1 does not have.

Explicitly deferred to a future study (thesis RQ5 scope):

- Decision-support utility (construct definition OPEN — see Section 9).
- Trust and calibrated reliance under graduated advisory scope.
- Advisory utility in the field.
- Real-world safety outcomes.

Journal 1's evidence base is limited to: formal proofs, mapping-literal comparisons, retrospective replay statistics, and Layer 2 performance measurements.

---

## 16. Threats and limitations

Threats specific to this evaluation specification (in addition to the threats to validity in manuscript §14):

- **Assumption dependence of P3.** Safety Dominance holds by construction under assumptions A1–A4. If a Layer 3 build violates any of these (e.g. a rule engine that generates types outside its active rule set, or a Layer 2/Layer 3 boundary that leaks stale rule-sets across transitions), P3 ceases to hold as an operational guarantee. F1–F3 test for exactly these failure modes.
- **J1-P1 modelling premise.** The mapping `A_C3(CAUTION) = FULL` is a *reading* of Flehmig et al.'s traffic-light topology — the intermediate level alters supervisory intensity, not AI advisory scope. That reading is what a reviewer can legitimately dispute; the proof and the 0.00% trace confirmation follow trivially from it. State the modelling premise explicitly alongside the proposition.
- **Retrospective-window scope.** All empirical values in E1–E4 and E6 are exact descriptive values for the analysed Kota Kinabalu 2020–2024 record under the stated configurations. They are not estimates of future conditions, and structural re-instantiability of the architecture in another domain does not imply empirical portability of these values.
- **`g_m` unmeasured.** The retrospective replay declares `D = {m}` because no marine warning archive exists for the study site. All severity figures are therefore **lower bounds**; a live required marine-warning feed would raise binding rates.
- **Latency threshold unsourced.** Do not close H3 by fabricating a threshold. See Section 11.
- **Decision-support utility construct undefined.** Do not close the utility metric by inventing a formula on replay data. See Section 9.

---

## 17. Open items

The specification closes carrying the following **bounded** open items, per task §34. Each is scoped so it does not create a contradiction elsewhere.

| ID | Item | Reason it is open | Blocks |
|---|---|---|---|
| OPEN-1 | Governance latency acceptance threshold `H3 = X ms` | No externally justified value exists | Only H3 in acceptance-hypothesis form; RQ-J2 is closed as a descriptive question |
| OPEN-2 | Decision-support utility construct | No operational definition on replay alone | Only the utility metric; other metrics are unaffected |
| ~~OPEN-3~~ | ~~Layer 3 prototype fidelity evidence (F1, F2, F3)~~ | **CLOSED 2026-09-11 by the Batch 5 fidelity evaluation** — Layer 3 is implemented and F1–F3 are CLOSED PASS (Section 7). Retained struck through rather than deleted, as the record of an item that was open when this specification closed | Nothing. Superseded |
| OPEN-5 | E5 target-hardware benchmark | Representative physical hardware unavailable; the harness is validated and only a development-machine reference exists | E5 / RQ-J2 only. `E5_ANDROID_TARGET_BENCHMARK = DEFERRED_MANDATORY` |
| OPEN-4 | Future user study / socio-technical evaluation (thesis RQ5) | Requires field data outside Journal 1's evidence base | Explicitly outside Journal 1; does not block Journal 1 closure |

No numerical threshold, utility formula or human-outcome value is fabricated to close any of these items.

---

## 18. Final evaluation matrix

The machine-readable master table produced by the Evaluation Specification Alignment batch is [`evaluation-specification.csv`](../../../data/journal1-evaluation-specification/evaluation-specification.csv). **It is frozen batch evidence, not a maintained authority: its `current_status` column records the state at that batch and is now stale (for example F1–F3 read "OPEN — requires Layer 3 build", whereas Batch 5 closed all three PASS), and its E3 row carries the pre-repair dual-configuration wording superseded by §13. This Markdown specification is authoritative wherever the two differ.** It carries every row (P1–P4, F1–F3, E1–E6, H-DEFERRED-utility, H-DEFERRED-trust) with all eleven columns required by task §24 (`id`, `question_or_claim`, `evidence_type`, `conditions`, `metric`, `current_status`, `expected_source`, `analytical_or_empirical`, `requires_layer3`, `requires_humans`, `reporting_boundary`).

### Final specification

```
PRIMARY EXPERIMENT
  C0 Ungated
  C1 Binary-gated
  C2 Proposed graduated architecture

STRUCTURAL COMPARATOR (not a fourth arm)
  C3 Flehmig-style traffic-light topology (Proposition J1-P1)

FORMAL
  P1 Totality
  P2 Monotonicity
  P3 Safety Dominance
  P4 (J1-P1) C1 ≡ C3 admissible-set equivalence

FIDELITY (CLOSED — PASS; interface-contract exhaustive scope,
          implemented rule configuration; R-SAFE-001 DEFERRED)
  F1 no output outside A_AI(S)                      0 violations
  F2 zero recommendations outside A_AI(S)           0 violations
  F3 RS(S) switching correctness at transitions     0 mismatches

EMPIRICAL / TRACE
  E1 pairwise admissible-set divergence (C0/C1/C2)
  E2 isolated Level 2 contribution Δ_L2 (5.81% PRIMARY / 4.48% RESOLUTION)
  E3 resolution sensitivity (PRIMARY / RESOLUTION spread)
  E4 transition / hysteresis characterisation
  E6 C1 ↔ C3 = 0.00% (J1-P1 confirmation)

PERFORMANCE
  E5 / RQ-J2 governance latency and computational overhead (threshold OPEN)

HUMAN VALIDATION (out of Journal 1 scope)
  decision-support utility (OPEN — construct definition required)
  trust / calibrated reliance / real-world safety outcomes (deferred to RQ5)
```

---

## Guiding principles (reaffirmed from task §Guiding principles)

- A theorem is not a hypothesis.
- An invariant is not a behavioural outcome.
- A deterministic census value is not a population estimate.
- A structural comparator is not necessarily an experimental arm.
- Implementation fidelity is evidence that code matches the specification; it is not evidence that the specification is epistemically correct.
- The smallest defensible evaluation is better than the largest possible evaluation.
- No experiment begins until every condition label, hypothesis and metric has exactly one meaning.

---

*Author: iskandar · Date: 2026-09-10 · Branch: `design/journal1-evaluation-specification`*
