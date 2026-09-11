# Batch 4A — Executable Rule-Set Authority Resolution: Closure Report

**Date:** 2026-09-11
**Branch:** design/journal1-layer3-executable-rule-authority
**HEAD before:** 3983f9875726e0b14ab8f2fcc197004c1ae9be27
**Batch 3 closure commit:** 3983f9875726e0b14ab8f2fcc197004c1ae9be27

---

## 1. Verdict

**JOURNAL 1 LAYER 3 PROTOTYPE BATCH 4A CLOSED —
EXECUTABLE RULE-SET AUTHORITY AND LAYER-BOUNDARY INTERFACE RESOLVED**

**Outcome B (partial acceptance):** R-CAUTION-002/003/004 are executable via Model B. R-SAFE-001 remains deferred as STATE_RESTATEMENT.

---

## 2. Authorities Inspected

| Document | Sections |
|---|---|
| `publications/active/journal-1/layer3-prototype-specification.md` | §7 (DecisionContext), §9 (execute_episode), §21-§26 (scientific rule candidates) |
| `publications/active/journal-1/algorithm-specification.md` | §17 (Algorithm 3), §19 (Algorithm 4) |
| `data/journal1-layer3-prototype/closure-batch2.json` | RS_candidate_at_closure, rule dispositions |
| `docs/canonical/appendix-c-formalisation.md` | §C.2 (max-severity, g_i), §C.2.0.8 (reasons), §C.7 (Safety Dominance), §C.7.2 (Theorem C.3) |
| `governance/canonical_rules.py` | R-CAUTION-001 implementation, DEFERRED_RULES |
| `governance/rule_set_provider.py` | DECISION_CONTEXT_SCHEMA, GOVERNANCE_MAP |
| `governance/reasoning_engine.py` | evaluate_predicate, ReasoningEngine |
| `governance/reasoning_episode.py` | DecisionContext, execute_episode |

---

## 3. Current Executable-Rule State (Post-Batch 3)

| Rule | Status |
|---|---|
| R-CAUTION-001 | IMPLEMENTED — `resolved_m == "advisory"` |
| R-SAFE-001 | DEFERRED — antecedent not expressible as ConditionPredicate without Layer 2 duplication |
| R-CAUTION-002 | DEFERRED — g_o(o,v)==CAUTION not expressible without duplicating vessel-category thresholds |
| R-CAUTION-003 | DEFERRED — g_r(r,κ)==CAUTION not expressible without duplicating rainfall thresholds + κ logic |
| R-CAUTION-004 | DEFERRED — g_w(w)==CAUTION not expressible without duplicating wind thresholds |

---

## 4. Model A Assessment — REJECTED

**Model A: raw-value predicate expansion** (e.g., g_r(r,κ)==CAUTION → `resolved_r_rate > 10 AND resolved_r_rate <= 20 AND resolved_r_kappa == 0`)

**Rejected.** Layer 3 would be performing the exact computation that Layer 2 already performed. This violates the frozen architecture boundary (task §4). Specific harms:

- Thresholds 21.6/27.0 kn (g_w), 10.0/20.0 mm/hr (g_r), and vessel-specific wave bands (g_o) would be duplicated in Layer 3
- Any future threshold change requires coordinated updates in both layers (divergence risk)
- Two-input rainfall semantics (rate + κ) would need to be reproduced in Layer 3, breaching Layer 2 encapsulation
- Canonical availability of thresholds does not automatically justify classifier duplication

---

## 5. Model B Assessment — ACCEPTED for R-CAUTION-002/003/004

**Model B: Layer 2 component-state interface** — Layer 2 exposes already-computed g_i(·) outputs alongside S; Layer 3 predicates consume these classified results.

**Accepted.** Assessment:

| Criterion | Result |
|---|---|
| Preserves layer boundary | YES — Layer 2 computes, Layer 3 consumes |
| Duplicates Layer 2 logic | NO |
| Changes scientific semantics | NO — g_o==CAUTION remains g_o==CAUTION |
| Supports existing rules | YES — R-CAUTION-002/003/004 executable |
| Preserves exclusion semantics | YES — EXCLUDED value distinct from SAFE |
| Preserves fault semantics | YES — faulted components → UNSAFE gate-off → Layer 3 never invoked |
| Requires canonical change | NO — Appendix C unaffected |
| Requires spec update | YES — layer3-prototype-specification.md §7 (Batch 4B) |

**Key authority:** layer3-prototype-specification.md §7 explicitly states that implementation-level interface additions may be documented there without extending canonical E. This provision was designed for exactly this situation.

**Safety Dominance proof (Theorem C.3) unaffected.** The proof depends only on the value of S — not on additional interface data. Component states are advisory inputs that do not affect which RS(S) is selected or how A_AI(S) constrains AI output.

**Proposed ComponentStateTrace interface:**

```
component_w_state: SAFE | CAUTION | EXCLUDED
component_r_state: SAFE | CAUTION | EXCLUDED
component_m_state: SAFE | CAUTION | EXCLUDED  (EXCLUDED when m∈D)
component_o_state: SAFE | CAUTION | EXCLUDED
component_t_state: SAFE | EXCLUDED             (g_t emits no CAUTION; t∉D)
```

UNSAFE is unreachable at the Layer 3 interface — any UNSAFE component state causes S=UNSAFE → gate-off → Layer 3 never invoked.

---

## 6. Model C Assessment — REJECTED

**Model C: reasons taxonomy as rule-selection interface.**

**Rejected.** Architecturally prohibited. The canonical architecture (Appendix C §C.2.0.8 and §C.7.2) explicitly states: "Reasons are annotations and never enter the case analysis or select RS(S)." Using `reasons` (fault/hazard/policy) to determine which rules fire would convert explanatory provenance into decision authority — a fundamental architectural violation.

---

## 7. Model D Assessment — PARTIAL

**Model D: keep all rules deferred.**

Partially accepted. R-SAFE-001 should remain deferred regardless (STATE_RESTATEMENT — see §10). Full deferral of R-CAUTION-002/003/004 is scientifically acceptable (task §6) but unnecessary when Model B provides a clean, architecturally sound path. With only R-CAUTION-001 executable and m∈D producing zero activations, F1-F3 would evaluate a near-empty rule set — an unnecessarily restricted lower bound.

---

## 8. Selected Interface Model

**Model B** for R-CAUTION-002/003/004.

**Model D** (continued deferral) for R-SAFE-001.

---

## 9. R-SAFE-001 State-Restatement Analysis

**Finding: STATE_RESTATEMENT confirmed.**

**Proof:**

```
f(E) = max-severity(g_w(w), g_r(r,κ), g_m(m), g_o(o,v), g_t(t,date))

S = SAFE ⟺ all non-excluded g_i(·) = SAFE
```

R-SAFE-001 antecedent: `all(g_w==SAFE, g_r==SAFE, g_m==SAFE, g_o==SAFE, g_t==SAFE)` is logically equivalent to `S=SAFE` under max-severity.

Furthermore: when Layer 3 executes with state="SAFE", the UNSAFE gate-off has already excluded any episode with a CAUTION or UNSAFE component. All component states visible to Layer 3 are already SAFE — the predicate is unconditionally TRUE. R-SAFE-001 would fire in every S=SAFE episode.

This creates an automatic SAFE→Go mapping. Batch 2 closure noted R-SAFE-001 as "CONDITIONALLY SUPPORTED" requiring an inference bridge from all-SAFE conditions to Go advisory. No inference bridge is present — the rule adds no environmental discriminant beyond S=SAFE itself.

**Disposition:** DEFERRED. Requires bounded scientific decision:
- Option A: add additional environmental discriminant to antecedent (e.g., time-of-day or weather stability criterion) to distinguish which SAFE episodes warrant Go
- Option B: explicitly document SAFE→Go as an accepted design choice with justification — but this must be treated as a state-to-advisory mapping and reviewed against the OPEN-L3-3 Resolution B precedent

---

## 10. R-CAUTION-001 Disposition

**IMPLEMENTED — no change in Batch 4A.**

Currently: `ConditionPredicate(variable='resolved_m', operator='==', value='advisory')`

Under Model B consistency: `component_m_state == CAUTION` would be equivalent (g_m('advisory')=CAUTION). This is a future migration consideration — not actioned in Batch 4A. Both representations are scientifically equivalent under the current g_m definition.

---

## 11. R-CAUTION-002 Disposition

**AUTHORISED_PENDING_BATCH4B**

- Classification: EXECUTABLE_WITH_INTERFACE_EXTENSION
- Candidate predicate: `ConditionPredicate(variable='component_o_state', operator='==', value='CAUTION')`
- Layer 2 duplication: None — vessel-category wave bands remain inside Layer 2 g_o
- Interface extension needed: ComponentStateTrace with component_o_state field

---

## 12. R-CAUTION-003 Disposition

**AUTHORISED_PENDING_BATCH4B**

- Classification: EXECUTABLE_WITH_INTERFACE_EXTENSION
- Candidate predicate: `ConditionPredicate(variable='component_r_state', operator='==', value='CAUTION')`
- Layer 2 duplication: None — two-input rainfall semantics (rate + κ) and thresholds remain inside Layer 2 g_r
- Interface extension needed: ComponentStateTrace with component_r_state field

---

## 13. R-CAUTION-004 Disposition

**AUTHORISED_PENDING_BATCH4B**

- Classification: EXECUTABLE_WITH_INTERFACE_EXTENSION
- Candidate predicate: `ConditionPredicate(variable='component_w_state', operator='==', value='CAUTION')`
- Layer 2 duplication: None — thresholds 21.6/27.0 kn remain inside Layer 2 g_w
- Interface extension needed: ComponentStateTrace with component_w_state field

---

## 14. Exclusion/Fault Semantics Result

**Exclusion:** EXCLUDED is a distinct value (not SAFE) in ComponentStateTrace. When m∈D, m_state=EXCLUDED — correctly distinguishes "excluded from classification" from "measured as SAFE."

**Fault:** Faulted components → g_i(⊥)=UNSAFE → S=UNSAFE → G(UNSAFE)=0 → Layer 3 gate-off. Faulted states never reach Layer 3. The UNSAFE gate-off is the fault-safety mechanism.

**Component state domain at Layer 3 interface:** {SAFE, CAUTION, EXCLUDED}

---

## 15. Layer 2 / Layer 3 Boundary Result

The boundary is preserved under Model B. Key finding from interface analysis:

> Layer 2 computes g_i(·) as internal intermediates of computing S. Exposing them is making an already-existing internal result explicit — not reimplementing Layer 2.

The Safety Dominance proof (Theorem C.3) is independent of interface content beyond S. A_AI(S) and RS(S) selection are unaffected.

---

## 16. Whether Canonical Change Is Required

**YES — canonical change required. Classification: Option A.**

`docs/canonical/architecture-illustration.md` is explicitly listed as a protected canonical file in task §29. It documents the full architecture walkthrough including the Layer 2 → Layer 3 interface. If ComponentStateTrace is added to that interface, the file must be updated to remain factually accurate — and that update is a modification to a protected canonical file.

**Why Option A and not Option B:** The task's §29 protection list names `architecture-illustration.md` alongside `appendix-c-formalisation.md`. The protection is the criterion: a file that triggers a stop condition when modified is not "documentation-only" for the purposes of this task. Treating it as documentation-only to avoid the canonical change classification would be rationalising the conclusion rather than applying the criterion.

**Scope of canonical change:** Scoped to `architecture-illustration.md`'s Layer 2 → Layer 3 interface description only. Appendix C is unaffected — the Safety Dominance proof (Theorem C.3) and formal variable definitions require no change.

**Action in Batch 4A:** The modification is NOT performed. Per task §29, Batch 4A stops at the canonical boundary. The authority question is fully answered; the canonical change is a Batch 4B prerequisite.

`layer3-prototype-specification.md §7` update (adding ComponentStateTrace to DecisionContext) is a specification change, not a canonical change — it does not touch either protected file and belongs to Batch 4B.

---

## 17. Whether Batch 4B Implementation Is Authorised

**Not yet — blocked by required canonical update.**

R-CAUTION-002/003/004 are authorised in principle via Model B. Implementation is blocked by the canonical change requirement identified in §16. Batch 4B must:

1. **Obtain review and approval for updating `docs/canonical/architecture-illustration.md`** — canonical change; must precede implementation
2. Formally specify ComponentStateTrace in `layer3-prototype-specification.md §7` — specification change
3. Add component_w_state/r_state/m_state/o_state/t_state fields to DECISION_CONTEXT_SCHEMA (`rule_set_provider.py`)
4. Extend DecisionContext (`reasoning_episode.py`) with component state fields
5. Add R-CAUTION-002, R-CAUTION-003, R-CAUTION-004 to `canonical_rules.py`
6. Run engineering tests (extend T01–T25 suite)

R-SAFE-001 remains deferred — Batch 4B must not implement it without resolving the STATE_RESTATEMENT finding.

---

## 18. Whether F1–F3 Are Ready

**No — pending Batch 4B.**

F1-F3 with current engine (R-CAUTION-001 only, m∈D) would produce zero-activation results — scientifically honest but a near-empty evaluation. The preferred configuration is Batch 4B first, then F1-F3.

If F1-F3 must be run before Batch 4B, they should be clearly framed as lower-bound results with the current executable rule set (R-CAUTION-001 only) and explicitly note the deferred rules.

---

## 19. Verification Summary

| Count | Status |
|---|---|
| 24 | PASS |
| 0 | FAIL |
| 1 | OPEN (BV-24: implementation correctly not prematurely authorised — pending Batch 4B canonical update) |

---

## 20. Files Created

| File | Contents |
|---|---|
| `data/journal1-layer3-prototype/batch4a-executable-rule-authority/rule-executability-matrix.csv` | Per-rule classification and disposition |
| `data/journal1-layer3-prototype/batch4a-executable-rule-authority/interface-candidate-matrix.csv` | Model A/B/C/D comparative assessment |
| `data/journal1-layer3-prototype/batch4a-executable-rule-authority/layer2-layer3-interface-analysis.md` | Formal boundary analysis Q1-Q8 |
| `data/journal1-layer3-prototype/batch4a-executable-rule-authority/resolution.json` | Authority resolution record |
| `data/journal1-layer3-prototype/batch4a-executable-rule-authority/verification.json` | 24 verification checks |
| `data/journal1-layer3-prototype/batch4a-executable-rule-authority/report.md` | This report |

**Files modified:** None. Batch 4A is an analysis-only task.

---

## 21. Protected OPEN Items

| Item | Status |
|---|---|
| OPEN-L3-1C (DepartureTime) | PRESERVED — no change |
| OPEN-L3-1D (Duration) | PRESERVED — no change |
| OPEN-L3-3 Resolution B | PRESERVED — no CAUTION→Go rule |
| GAP-03 | PRESERVED — interface engineering cannot substitute for missing evidence |
| OPEN-B3-2 (production strategy) | PRESERVED — no change |
| R-SAFE-001 STATE_RESTATEMENT | NEW — requires bounded scientific decision |

---

## 22. Remaining Blockers

None blocking Batch 4A closure. Blockers for subsequent batches:

1. **Batch 4B canonical update**: `docs/canonical/architecture-illustration.md` must be reviewed and updated to document the extended Layer 2 → Layer 3 interface before Batch 4B implementation may proceed
2. **Batch 4B**: requires ComponentStateTrace interface specification in `layer3-prototype-specification.md §7` and implementation of extended DecisionContext, DECISION_CONTEXT_SCHEMA, and three new rules
3. **R-SAFE-001**: requires bounded scientific decision (additional antecedent discriminant or explicit SAFE→Go policy justification) before any implementation is considered
4. **F1-F3**: deferred until Batch 4B complete (or explicitly framed as lower-bound if run earlier with R-CAUTION-001 only)

---

## 23. Closure Line

**JOURNAL 1 LAYER 3 PROTOTYPE BATCH 4A CLOSED —
EXECUTABLE RULE-SET AUTHORITY AND LAYER-BOUNDARY INTERFACE RESOLVED**
