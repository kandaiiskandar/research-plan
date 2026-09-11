# Batch 5 — Executable Scientific Fidelity Evaluation (F1–F3): Closure Report

**Date:** 2026-09-11  
**Branch:** `eval/journal1-layer3-fidelity-f1-f3`  
**Batch 4B-2 commit:** `485f9d2` (merged as PR #36, `a73a4ff`)  
**Evaluation script:** `scripts/journal1_layer3_fidelity_evaluation.py`  
**Execution timestamp:** 2026-09-11T13:00:39.535705+00:00  
**Python version:** 3.13.12

---

## 1. Verdict

**F1 PASS — F2 PASS — F3 PASS**

```
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 5 CLOSED —
EXECUTABLE F1–F3 SCIENTIFIC FIDELITY EVALUATION PASSED
```

---

## 2. Frozen Implementation Authority

| Source | Role |
|---|---|
| `governance/reasoning_episode.py` | DecisionContext; execute_episode(); Step 2.5 consistency check |
| `governance/rule_set_provider.py` | select_rule_set(); validate_rule_set(); DECISION_CONTEXT_SCHEMA |
| `governance/canonical_rules.py` | build_canonical_repository(); R-CAUTION-001–004 |
| `governance/reasoning_engine.py` | ReasoningEngine.reason(); evaluate_predicate() |
| `governance/fidelity_trace.py` | FidelityTrace — F1/F2/F3 fields |
| `governance/rule.py` | Rule; ConditionPredicate; ConfigurationError |
| `governance/advisory.py` | Advisory |
| `governance/rule_repository.py` | RuleRepository |

All 8 governance files confirmed UNCHANGED from Batch 4B-2 hashes (see `integrity.json`).

---

## 3. Evaluation Authority

| Document | Role |
|---|---|
| `publications/active/journal-1/evaluation-specification.md §7` | F1, F2, F3 definitions |
| `publications/active/journal-1/layer3-prototype-specification.md §9, §11` | Episode orchestration; FidelityTrace fields |
| `docs/canonical/appendix-c-formalisation.md` | Formal variable definitions |
| `data/journal1-layer3-prototype/batch4b2-component-state-rules/report.md` | Batch 4B-2 closure |
| `docs/tasks/Journal 1 Layer 3 Prototype Batch 5.md` | Evaluation task specification |

---

## 4. Evaluation Question

> Does the frozen executable Layer 3 implementation faithfully enforce its formally specified governance and rule-set contracts across the reachable governed reasoning space?

This is an implementation-fidelity question, not a re-proof of Safety Dominance and not a claim about real-world safety outcomes.

---

## 5. Evaluation Method

**Deterministic census** of the interface-contract-exhaustive reachable governance/interface state space.

- No random sampling
- No p-values
- No confidence intervals
- No inferential statistics
- No retrospective replay (43,848-hour dataset not evaluated)
- No E5 latency threshold

All counts are exact descriptive values for the evaluated state space.

---

## 6. Primary Denominator

**Interface-contract exhaustive** — all component-state tuples that are reachable under the frozen Batch 4B-1/4B-2 interface contract, across the full component-domain Cartesian product.

Not current-configuration exhaustive (D={m} replay). The two are kept separate per task §13.

---

## 7. State-Space Construction

**Component domains:**

| Field | Domain | Size |
|---|---|---|
| `component_w_state` | {SAFE, CAUTION, EXCLUDED} | 3 |
| `component_r_state` | {SAFE, CAUTION, EXCLUDED} | 3 |
| `component_m_state` | {SAFE, CAUTION, EXCLUDED} | 3 |
| `component_o_state` | {SAFE, CAUTION, EXCLUDED} | 3 |
| `component_t_state` | {SAFE, EXCLUDED} | 2 |

**Raw component-tuples:** 3⁴ × 2 = **162**  
**With S ∈ {SAFE, CAUTION, UNSAFE}:** 162 × 3 = **486 raw combinations**

---

## 8. Reachability Treatment

| Class | Count | Rule |
|---|---|---|
| GATED_UNSAFE | 162 | S=UNSAFE → gate-off; no Layer 3 reasoning invoked |
| REACHABLE_CONSISTENT (SAFE) | 32 | All active (non-EXCLUDED) components SAFE; 2⁴ × 2 = 32 |
| REACHABLE_CONSISTENT (CAUTION) | 130 | At least one active component CAUTION; 162 − 32 = 130 |
| INTERFACE_INCONSISTENT (SAFE) | 130 | S=SAFE + any CAUTION component → STATE_TRACE_INCONSISTENCY |
| INTERFACE_INCONSISTENT (CAUTION) | 32 | S=CAUTION + no active CAUTION → STATE_TRACE_INCONSISTENCY |

**Total REACHABLE_CONSISTENT:** 32 + 130 = **162 component-state combinations**

---

## 9. EXCLUDED Treatment

EXCLUDED components are not counted as active. They do not violate SAFE consistency. They do not contribute a CAUTION for CAUTION consistency. EXCLUDED ≠ observed SAFE semantics are preserved.

Special cases:
- All-EXCLUDED + S=SAFE: consistent (active = ∅; `all()` on empty = True). Tested in BC-4. ✓
- All-EXCLUDED + S=CAUTION: inconsistent (no active CAUTION). Tested in BC-5. ✓
- `component_t_state=EXCLUDED`: valid in domain; structurally representable but unreachable under canonical configuration (t ∉ D; device clock always available).

---

## 10. UNSAFE Treatment

S=UNSAFE → G(UNSAFE)=0 → Layer 3 gate-off (Step 2 of execute_episode). Consistency check (Step 2.5) and rule reasoning never reached. 162 GATED_UNSAFE cases reported separately. Gate-off correct in all 10 sampled cases (BC-6).

---

## 11. R-CAUTION-001 Context Treatment

R-CAUTION-001 predicates on `resolved_m`, not a component-state field. To exercise its TRUE and FALSE paths, CAUTION episodes were evaluated with `resolved_m ∈ {None, "advisory"}`. SAFE episodes use `resolved_m=None` only (R-CAUTION-001 is in RS(CAUTION), not RS(SAFE)).

**Primary episodes:**  
- SAFE: 32 component-state combinations × 1 resolved_m = **32 cases**  
- CAUTION: 130 component-state combinations × 2 resolved_m values = **260 cases**  
- **Total primary: 292 episodes**

---

## 12. Concurrent-Rule Treatment

All 130 CAUTION-consistent component-state tuples are evaluated including those where multiple CAUTION predicates are simultaneously TRUE. Multiple fired rules produce multiple Delay advisory records. No deduplication is applied.

F1/F2 evaluate each generated advisory conclusion type individually. All are Delay ∈ A_AI(CAUTION).

---

## 13. F1 — Advisory Admissibility Fidelity

**Definition:** No generated advisory conclusion type lies outside A_AI(S).

**A_AI mapping:**

| S | A_AI(S) |
|---|---|
| SAFE | {Go, Delay, DepartureTime, Duration} |
| CAUTION | {Go, Delay} |
| UNSAFE | ∅ |

**Results:**

| Metric | Value |
|---|---|
| F1_episodes_evaluated | 292 |
| F1_advisory_records_evaluated | 454 |
| F1_conclusion_types_evaluated | 244 (unique conclusion types aggregated per episode; all are "Delay") |
| F1_violations | **0** |
| F1_violation_rate | **0.0000** |
| F1_verdict | **PASS** |

No generated advisory conclusion type was outside the configured admissible set for any episode.

Of the 292 primary episodes: 260 were CAUTION, 32 were SAFE. Of the 260 CAUTION episodes, 244 generated at least one advisory (AI(E)≠∅) and 16 generated AI(E)=∅ because none of the currently executable rule predicates evaluated TRUE in those episodes. This is not a fidelity failure — A_AI(S) defines admissibility, not a requirement that an advisory must exist.

---

## 14. F2 — Safety-Dominance Violation Count

**Definition:** Explicit count of AI(E) ⊄ A_AI(S) episodes (Safety Dominance).

**Results:**

| Metric | Value |
|---|---|
| F2_episodes_evaluated | 292 |
| F2_episodes_with_advisory | 244 |
| F2_advisory_records | 454 |
| F2_violation_count | **0** |
| F2_violation_rate | **0.0000** |
| F2_verdict | **PASS** |

**Bounded claim:** The frozen Layer 3 implementation produced zero violations of the configured advisory admissibility contract across the 292-episode deterministic fidelity state space. This does not constitute proof that the system is safe in the real world, nor that A_AI(CAUTION) is scientifically optimal.

---

## 15. F3 — Rule-Set / State Correspondence

**Definition:** RS_selected(e) = RS(S_e) for every episode.

| S | Expected RS |
|---|---|
| SAFE | [] (no SAFE rules implemented — R-SAFE-001 deferred) |
| CAUTION | [R-CAUTION-001, R-CAUTION-002, R-CAUTION-003, R-CAUTION-004] |
| UNSAFE | gate-off; no RS selected |

**Results:**

| Metric | Value |
|---|---|
| F3_episodes_evaluated | 292 |
| F3_SAFE_episodes | 32 |
| F3_CAUTION_episodes | 260 |
| F3_UNSAFE_gateoff_cases | 162 |
| F3_rule_sets_examined | 292 |
| F3_mismatches | **0** |
| F3_mismatch_rate | **0.0000** |
| F3_verdict | **PASS** |

Rule-set correspondence by state:

| S | Expected RS | Observed mismatch count |
|---|---|---|
| SAFE | [] | 0 |
| CAUTION | [R-CAUTION-001..R-CAUTION-004] | 0 |
| UNSAFE | gate-off | 0 (sampled 10/162) |

**Bounded claim:** The executable rule-set selection corresponded exactly to the governance state across all 292 evaluated cases. This does not mean the selected rules are scientifically correct, nor that the advisory content is optimal.

---

## 16. Rule-Level Activation Summary

| Rule | Selected | Pred TRUE | Pred FALSE | Pred ERROR | Fired | Advisories |
|---|---|---|---|---|---|---|
| R-CAUTION-001 | 260 | 130 | 130 | 0 | 130 | 130 |
| R-CAUTION-002 | 260 | 108 | 152 | 0 | 108 | 108 |
| R-CAUTION-003 | 260 | 108 | 152 | 0 | 108 | 108 |
| R-CAUTION-004 | 260 | 108 | 152 | 0 | 108 | 108 |
| R-SAFE-001 | 0 | 0 | 0 | 0 | 0 | 0 |

**R-CAUTION-001:** TRUE in 130 cases (resolved_m="advisory", one per CAUTION component-tuple); FALSE in 130 cases (resolved_m=None). No ERROR.

**R-CAUTION-002/003/004:** TRUE in 108 cases each (54 CAUTION-consistent tuples with the relevant component CAUTION × 2 resolved_m values). FALSE in 152 cases. No ERROR.

**Activation counts are counts within the synthetic fidelity state space, not real-world prevalence estimates.**

PRIOR PROJECTION in `batch4b2-component-state-rules/canonical-rule-activation-analysis.md` (e.g., "R-CAUTION-004: 0 activations in retrospective replay") is a retrospective replay projection, NOT an executed F1–F3 result. These are separate evidence bases.

---

## 17. Boundary-Check Results

All boundary checks PASS. These are supplementary — not counted in the primary F1/F2/F3 denominator.

| Check | Result |
|---|---|
| SAFE + CAUTION component → STATE_TRACE_INCONSISTENCY | PASS |
| CAUTION + no active CAUTION → STATE_TRACE_INCONSISTENCY | PASS |
| UNSAFE → gate-off (G=0, advisories=[], no config_failure) | PASS |
| All-EXCLUDED + SAFE → consistent (no config_failure) | PASS |
| All-EXCLUDED + CAUTION → inconsistent (STATE_TRACE_INCONSISTENCY) | PASS |
| UNSAFE gate-off: 10-case sample correct | PASS |
| Interface-inconsistent cases correctly rejected: 10-case sample | PASS |

Interface-inconsistent cases in state space: 162 total (130 SAFE-inconsistent + 32 CAUTION-inconsistent). All 10 sampled were correctly rejected as STATE_TRACE_INCONSISTENCY configuration failures. These are not F1/F2/F3 violations.

---

## 18. Safety-Dominance Interpretation

F1 and F2 confirm:

> The frozen Layer 3 implementation produced zero violations of the configured advisory admissibility contract (AI(E) ⊆ A_AI(S)) across the 292-episode deterministic fidelity state space.

This is an implementation-fidelity measurement. It does not:
- Constitute proof that the system is safe in the real world
- Confirm that A_AI(CAUTION) = {Go, Delay} is scientifically optimal for Malaysian coastal fisheries
- Imply that fishers will make safer decisions
- Prove that accidents will be prevented

Safety Dominance is proved formally by Theorem C.3 (appendix-c-formalisation.md), under assumptions A1–A4. F1/F2 test that the executable implementation conforms to those assumptions.

---

## 19. Claim Limitations

- This evaluation is over the interface-contract fidelity state space, not over the 43,848-hour retrospective replay.
- SAFE episodes generate AI(E)=∅ because R-SAFE-001 is deferred and no other SAFE rules exist. This is legitimate — A_AI defines admissibility, not guaranteed rule existence.
- `resolved_m` is exercised with {None, "advisory"} only — the minimum sufficient to exercise R-CAUTION-001 TRUE/FALSE paths. No new marine warning categories are invented.
- `component_t_state=EXCLUDED` is structurally present in the state space but unreachable under the canonical D configuration (t ∉ D). It is evaluated for interface completeness.

---

## 20. Human-Authority Result

No generated advisory encodes automatic approval, automatic prohibition, or human override restriction. All generated advisories are of type "Delay" with human-decision-preserving payloads. Human authority remains unconditional.

**Result: SUPPLEMENTARY INVARIANT — CONFIRMED**

---

## 21. Engineering Regression Result

**139/139 tests PASS** (confirmed before evaluation; `python3 -m unittest discover`).

All pre-existing tests from Batches 1–4B-2 pass without modification.

---

## 22. Integrity Result

All 8 governance implementation files confirmed UNCHANGED from Batch 4B-2 SHA-256 reference hashes.

All 5 canonical/specification files (appendix-c-formalisation.md, architecture-illustration.md, layer3-prototype-specification.md, algorithm-specification.md, evaluation-specification.md) confirmed UNCHANGED.

Full hashes: `integrity.json`.

---

## 23. Verification PASS/FAIL/OPEN Totals

| | |
|---|---|
| **PASS** | **37** |
| **FAIL** | **0** |
| **OPEN** | **0** |

Full check list: `verification.json`.

---

## 24. F1–F3 Overall Verdict

**PASS**

---

## 25. E5 Status

**Not run.** E5 is latency/performance evaluation; it remains OPEN. Ordinary test runtime printed by unittest is not E5 evidence. No latency threshold was invented.

---

## 26. Remaining OPEN Items

All OPEN items from prior batches are preserved:

| Item | Status |
|---|---|
| OPEN-L3-3 Resolution B | PRESERVED — no CAUTION→Go rule |
| OPEN-L3-1C (DepartureTime) | PRESERVED |
| OPEN-L3-1D (Duration) | PRESERVED |
| GAP-03 | PRESERVED |
| OPEN-B3-2 | PRESERVED |
| R-SAFE-001 STATE_RESTATEMENT | PRESERVED — deferred |
| E5 (latency threshold) | OPEN — unsourced |
| Decision-support utility construct | OPEN — construct definition required |

---

## 27. POST_FIDELITY_READY

```
POST_FIDELITY_READY = true
```

TRUE because:
- F1 = PASS ✓
- F2 = PASS ✓
- F3 = PASS ✓
- Frozen implementation integrity = PASS ✓
- Engineering regression = PASS ✓
- Evaluation evidence integrity = PASS ✓

This does NOT automatically authorise E5 or any further evaluation task. Batch 5 is ready for independent review and subsequent evaluation planning.

---

## 28. Files Created

| File | Contents |
|---|---|
| `scripts/journal1_layer3_fidelity_evaluation.py` | Deterministic evaluation script |
| `report.md` | This closure report |
| `evaluation-design.json` | Evaluation design parameters |
| `state-space-manifest.json` | State-space construction; reachability classification |
| `fidelity-results.json` | F1/F2/F3 computed results |
| `fidelity-traces.csv` | 292 primary episode traces (1 row each) |
| `rule-activation-summary.csv` | Per-rule activation counts |
| `boundary-checks.json` | Supplementary boundary/consistency checks |
| `integrity.json` | SHA-256 hashes before/after for governance and canonical files |
| `verification.json` | 37 verification checks (37 PASS / 0 FAIL / 0 OPEN) |

---

## 29. Closure Line

**JOURNAL 1 LAYER 3 PROTOTYPE BATCH 5 CLOSED —
EXECUTABLE F1–F3 SCIENTIFIC FIDELITY EVALUATION PASSED**
