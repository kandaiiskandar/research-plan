# OPEN-L3-2 Resolution Report

**Item:** OPEN-L3-2 — Predicate evaluation failure handling
**Verdict:** **CLOSED — policy established under Model C + Model D (three-valued semantics with episode-level refusal)**
**Date:** 2026-09-11
**Branch:** design/journal1-layer3-predicate-failure-policy
**Task authority:** `docs/tasks/Journal 1 Layer 3 Prototype OPEN-L3-2.md`

---

## 1. Verdict

OPEN-L3-2 is CLOSED. The predicate evaluation failure policy is now explicitly governed.

The selected policy is **Model C combined with Model D**: three-valued predicate semantics `{TRUE, FALSE, ERROR}` with episode-level refusal when any predicate evaluation fails. This is a design-interpretation decision consistent with the existing architecture contracts and the fail-safe orientation of the broader system.

No external scientific authority prescribes this policy. It is the most conservative option consistent with the existing contracts, selected because it:
- preserves Safety Dominance
- does not generate advisories from unestablished antecedents
- matches the existing ConfigurationError → `AI(E) = ∅` pattern
- produces a trace in which ERROR is distinguishable from FALSE

---

## 2. Authority Inspected

| Document | §§ inspected | Bearing |
|---|---|---|
| `docs/canonical/appendix-c-formalisation.md` | C.1, C.2.0, C.7.1, C.7.2, C.8.2, Corollary C.1b.1, Theorem C.3 | Canonical formal architecture; fail-safe semantics; Safety Dominance proof structure |
| `publications/active/journal-1/algorithm-specification.md` | §17–§20, §24 | Algorithm 3 and Algorithm 4 contracts; OPEN-B3-1, OPEN-B3-2 |
| `publications/active/journal-1/layer3-prototype-specification.md` | §8, §9, §11, §12, §14 | Batch 1 contract; Repair 3 (predicate failure); OPEN-L3-2 placeholder |
| `data/journal1-layer3-prototype/closure-batch1.json` | `repair_record.repairs[2]` | Repair 3 text confirming ERROR ≠ FALSE requirement |
| `data/journal1-layer3-prototype/closure-batch2.json` | `OPEN_L3_2_predicate_evaluation_failure_policy` | Batch 2 confirmation of OPEN status |
| `publications/active/journal-1/evaluation-specification.md` | §7 | F1, F2, F3 fidelity criteria scope |

---

## 3. Failure Taxonomy

Ten failure classes are identified and classified. Full detail in `failure-taxonomy.csv`.

| Range | Layer owner | Stage | Count |
|---|---|---|---|
| F-T-01, F-T-02 | Layer 2 / Layer 2 configuration | Before Layer 3 invocation | 2 |
| F-T-03 | execute_episode() startup | Pre-reasoning | 1 |
| F-T-04, F-T-05, F-T-06 | Algorithm 3 validate_rule_set() | Rule-set supply | 3 |
| F-T-07, F-T-08, F-T-09, F-T-10 | Algorithm 4 / engine.reason() | Runtime predicate evaluation | 4 |

OPEN-L3-2 governs only the last group (F-T-07 through F-T-10). The others are handled by existing contracts upstream.

---

## 4. Candidate Policy Comparison

Full matrix in `policy-candidate-matrix.csv`. Summary:

| Model | Disposition | Stop condition triggered | Reason |
|---|---|---|---|
| A — Fail-closed (ERROR → FALSE) | REJECTED | YES | §14: silently treats ERROR as FALSE; trace integrity violated |
| B — Fail-open (ERROR → TRUE) | REJECTED | YES | §14: generates advisory from unestablished antecedent |
| C — Three-valued domain (standalone) | PARTIAL | NO | Semantic framework; incomplete without episode-level policy |
| C+D — Three-valued + episode refusal | **ACCEPTED** | NO | Conservative; consistent with existing patterns |
| C+E — Three-valued + rule quarantine | REJECTED | NO (on stop conditions) | Scientifically indefensible; partial advisory completeness risk |

---

## 5. Selected Policy

**Model C + Model D — three-valued predicate semantics with episode-level refusal.**

C+E did not trigger any explicit stop condition but fails on scientific defensibility. With the current RS_candidate structure, Model E would allow a Delay recommendation to be produced even when one or more hazard assessments (e.g. the marine-warning-based R-CAUTION-001 or the wave-based R-CAUTION-002) could not be evaluated. That advisory would appear indistinguishable from one based on complete evaluation. No existing authority supports partial advisory production on evaluation failure. The architecture's existing failure patterns (Layer 2 → UNSAFE; ConfigurationError → `AI(E) = ∅`) are uniformly conservative; the selected policy preserves that character.

C+D is a design interpretation: no document in the authority hierarchy explicitly prescribes it. The authority class is `DESIGN_INTERPRETATION` in `resolution.json`.

---

## 6. Predicate Result Domain

```text
domain = {TRUE, FALSE, ERROR}

TRUE    — antecedent predicate successfully evaluated and satisfied
FALSE   — antecedent predicate successfully evaluated and not satisfied
ERROR   — antecedent could not be established (evaluation failed)
```

FALSE and ERROR are distinct states. Both prevent rule firing. Only ERROR produces `evaluation_failure = True` in the trace.

---

## 7. Rule Firing Semantics

A rule fires if and only if **all** predicates in its condition set evaluate to `TRUE`.

`FALSE` prevents firing without any failure flag. `ERROR` prevents firing and records `evaluation_failure = True` with `failed_rule_ids` and `failure_category`.

```text
all predicates TRUE → rule fires → Advisory produced
any predicate FALSE → rule does not fire → normal no-fire (no flag)
any predicate ERROR → rule does not fire → evaluation_failure flag set
```

The third case is the subject of OPEN-L3-2. Under the selected policy, it propagates to episode-level refusal.

---

## 8. Episode-Level Failure Behaviour

```text
any predicate evaluation ERROR in any rule
→ AI(E) = ∅
→ S unchanged
→ G unchanged
→ A_AI unchanged
→ evaluation_failure = True in trace
→ failed_rule_ids recorded
→ failure_category recorded
→ human authority preserved (∅ does not constrain human decision)
```

Other rules do not continue after an evaluation failure. The episode produces no advisory output. The trace always emits; it cannot be suppressed by an evaluation failure.

The implementation may either abort on the first predicate failure (early termination) or complete evaluation of all rules before refusing advisory generation. Both produce the same episode-level outcome: `AI(E) = ∅`. If the implementation evaluates remaining rules after the first failure, the trace should record all failed rule IDs, not only the first.

---

## 9. Algorithm 3 Boundary

The existing Algorithm 3 validation postcondition (`ConclusionTypes(RS_candidate) ⊆ A_AI(S)`) is unchanged.

By design interpretation, `validate_rule_set()` extends its structural validation to three additional checks before reasoning begins:

1. Predicate operator validity for declared variable types
2. Value domain membership for categorical predicates (per appendix-c variable definitions)
3. All referenced variable names exist in the DecisionContext schema

Violations in any of these three checks produce `ConfigurationError` — the same outcome as the existing admissibility check — with `configuration_failure = True` in the trace and `AI(E) = ∅`. S is not modified.

This extension keeps the boundary clean: failures detectable from the rule schema and context schema at supply time are caught by Algorithm 3; failures requiring actual runtime values are handled by the OPEN-L3-2 policy.

The extended validation catches F-T-04 (type mismatch), F-T-05 (invalid operator), and F-T-06 (unsupported categorical value).

---

## 10. Algorithm 4 Boundary

Algorithm 4 pseudocode is unchanged. The gate-off at lines 1–3 (G(S) = 0 → return ∅) runs prior to any predicate evaluation and is unaffected.

`engine.reason(E, RS)` at line 5 now has a specified failure contract:

```text
engine.reason(E, RS) raises or detects a predicate evaluation failure
→ return evaluation_failure = True
→ AI = ∅
→ trace records: evaluation_failure = True; failed_rule_ids; failure_category
→ S unchanged; G unchanged
```

The engine does not rethrow the raw exception to the caller without producing a trace. The `EpisodeResult` structure already supports this: `advisories = []`; `trace` always emitted; `error` field can carry structured failure information.

---

## 11. UNSAFE Behaviour

UNSAFE behaviour is unchanged and OPEN-L3-2 is not applicable to UNSAFE episodes.

```text
S = UNSAFE → G(S) = 0 → Algorithm 4 lines 1–3 → AI(E) = ∅
```

RS(UNSAFE) = ∅. No rule set is selected. `engine.reason()` is never called. Predicate evaluation never occurs. The OPEN-L3-2 policy is unreachable for UNSAFE episodes.

---

## 12. Trace Requirements

To distinguish predicate ERROR from normal no-fire, the FidelityTrace requires three additional conceptual fields:

| Field | Type | Semantics |
|---|---|---|
| `evaluation_failure` | bool | True iff any predicate evaluation failure occurred this episode |
| `failed_rule_ids` | list[str] | Rule IDs with predicate failures (at minimum first; ideally all) |
| `failure_category` | str \| None | PREDICATE_EXCEPTION \| NUMERIC_CONVERSION_FAILURE \| MALFORMED_VALUE \| INTERNAL_ERROR |

The two states must be distinguishable without inspecting any other field:

```text
fired_rule_ids = []  AND  evaluation_failure = False
→ normal no-fire — all predicates evaluated; none satisfied

fired_rule_ids = []  AND  evaluation_failure = True
→ evaluation failure — episode aborted; AI(E) = ∅
```

The `configuration_failure` field (existing) and `evaluation_failure` (new) are distinct. Both produce `AI(E) = ∅` but at different stages:

- `configuration_failure = True` → Algorithm 3 / startup failure
- `evaluation_failure = True` → engine.reason() predicate evaluation failure

Implementation of these fields is Batch 3 work; this task specifies the conceptual requirements only.

---

## 13. Scientific and Evaluation Consequences

**F1 (advisory type compliance):** Evaluation failure episodes return `AI(E) = ∅`, which satisfies F1 by construction. F1 analysis must count and report evaluation_failure episodes separately; they must not be treated as evidence of F1 compliance in the same category as successful reasoning episodes.

**F2 (violation count):** Evaluation failure episodes produce zero violations and must be labelled separately.

**F3 (RS consistency):** Unaffected. RS(S) is selected by Algorithm 3 before engine.reason() runs; the failure occurs after correct supply.

**Safety Dominance:** `AI(E) = ∅ ⊆ A_AI(S)` for all S. Theorem C.3 holds for failure episodes.

**Rule firing interpretation:** `fired_rule_ids = []` on evaluation failure must not be read as "all rules assessed and none fired." The `evaluation_failure` flag is the distinguishing marker.

**Advisory completeness:** The presentation layer must distinguish evaluation failure (where `AI(E) = ∅` means inability to evaluate) from normal no-fire (where `AI(E) = ∅` means all conditions assessed and no advisory warranted). These are materially different states for the human decision-maker.

**E5 latency:** Failure-abort episodes have a different latency profile than successful reasoning. E5 analysis should separate evaluation_failure episodes from the main performance distribution.

---

## 14. Canonical Changes

| Document | Change |
|---|---|
| `docs/canonical/appendix-c-formalisation.md` | **UNCHANGED** |
| `docs/canonical/architecture-illustration.md` | **UNCHANGED** |
| `publications/active/journal-1/layer3-prototype-specification.md` | §12: OPEN-L3-2 placeholder replaced with resolved policy; §14: OPEN-L3-2 status updated to CLOSED |

---

## 15. Remaining OPEN Items

| ID | Status | Note |
|---|---|---|
| OPEN-L3-1C | OPEN (preserved) | DepartureTime — no scientific authority in repository |
| OPEN-L3-1D | OPEN (preserved) | Duration — no scientific authority in repository |
| GAP-03 | OPEN evidence gap (preserved) | No evidence for CAUTION-Go rule; unaffected |
| OPEN-B1-8 | OPEN (preserved) | Concurrency mechanism for state/RS consistency |
| OPEN-B3-2 | PARTIALLY CLOSED (unchanged) | Production engine strategy remains OPEN |

---

## 16. Verification Results

21 checks. **PASS: 21 / FAIL: 0 / OPEN: 0**

Full check list in `verification.json`. Key checks:

| Check | Verdict |
|---|---|
| predicate_ERROR_not_silently_FALSE | PASS |
| predicate_ERROR_not_silently_TRUE | PASS |
| FALSE_distinguished_from_ERROR | PASS |
| configuration_failure_distinguished_from_runtime_evaluation_failure | PASS |
| Layer2_failure_distinguished_from_Layer3_failure | PASS |
| S_not_mutated_by_Layer3_failure | PASS |
| UNSAFE_short_circuits_before_reasoning | PASS |
| no_advisory_generated_from_unestablished_antecedent | PASS |
| Algorithm3_contract_preserved | PASS |
| Algorithm4_contract_preserved | PASS |
| Safety_Dominance_preserved | PASS |
| human_authority_preserved | PASS |
| OPEN_L3_3_remains_CLOSED | PASS |
| OPEN_L3_1C_preserved | PASS |
| OPEN_L3_1D_preserved | PASS |
| GAP_03_preserved | PASS |
| no_new_scientific_rules | PASS |
| engine_not_implemented | PASS |
| F1_F3_not_run | PASS |
| E5_not_run | PASS |
| canonical_integrity_preserved | PASS |

---

## 17. Files Created / Modified

**Created:**
- `data/journal1-layer3-prototype/open-l3-2-resolution/failure-taxonomy.csv`
- `data/journal1-layer3-prototype/open-l3-2-resolution/policy-candidate-matrix.csv`
- `data/journal1-layer3-prototype/open-l3-2-resolution/algorithm-boundary-analysis.md`
- `data/journal1-layer3-prototype/open-l3-2-resolution/resolution.json`
- `data/journal1-layer3-prototype/open-l3-2-resolution/verification.json`
- `data/journal1-layer3-prototype/open-l3-2-resolution/report.md` (this file)

**Modified:**
- `publications/active/journal-1/layer3-prototype-specification.md` — §12 OPEN-L3-2 placeholder replaced with resolved policy; §14 OPEN-L3-2 status updated to CLOSED

**Canonical files touched:** none

---

## 18. Closure

```text
JOURNAL 1 LAYER 3 OPEN-L3-2 CLOSED —
PREDICATE EVALUATION FAILURE SEMANTICS EXPLICITLY GOVERNED
```
