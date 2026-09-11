# Algorithm Boundary Analysis — OPEN-L3-2

**Item:** OPEN-L3-2 — Predicate Evaluation Failure Policy
**Date:** 2026-09-11
**Purpose:** Determine which predicate evaluation failure classes belong to Algorithm 3 (rule-set supply) versus Algorithm 4 / engine.reason() (runtime evaluation), and verify that the selected policy (C+D) does not blur this boundary.

---

## 1. The Existing Algorithm 3 Contract

Algorithm 3 (`algorithm-specification.md` §17–§18) is a **pre-reasoning validation layer**. It runs before any rule firing begins.

**Current postcondition Q1 (from algorithm-specification.md §18):**

```
ConclusionTypes(RS_candidate) ⊆ A_AI(S)
```

If the candidate rule set violates this constraint, Algorithm 3 refuses supply:
- `ConfigurationError` raised (OPEN-B3-1 handling)
- `configuration_failure = True` in trace
- `AI(E) = ∅`
- S not modified

**Key property:** Algorithm 3 validates the **structure and admissibility** of the rule set. It does not evaluate predicates against runtime data.

---

## 2. The Algorithm 4 / engine.reason() Contract

Algorithm 4 (`algorithm-specification.md` §19–§20) invokes `engine.reason(E, RS)` on the participating path (G(S) = 1). The engine receives a rule set that has already passed Algorithm 3 validation.

**What Algorithm 3 cannot catch:** failures that depend on **runtime context values** — the actual observations in E at the time of reasoning. A rule may be structurally valid at supply time yet encounter an exception when its predicate is evaluated against specific context values.

---

## 3. Failure Classification by Algorithm Boundary

### 3.1 Failures belonging to Algorithm 3 (validate_rule_set)

These failures are detectable from the rule definition and context schema alone, without runtime context values.

| Failure class | Validation check | Reason for Algorithm 3 ownership | Current handling |
|---|---|---|---|
| Unknown predicate variable reference (F-T-11) | V1 — referenced variable exists in DecisionContext schema | Variable existence is checkable from the rule definition and context schema at supply time; a missing variable has no type to check | `validate_rule_set()` rejects; `ConfigurationError`; `configuration_failure = True` |
| Rule type mismatch in predicate (F-T-04) | V2 — predicate operand/value type is compatible with declared variable type | Variable type is fixed in the context schema; type compatibility is checkable at supply time | `validate_rule_set()` rejects; `ConfigurationError`; `configuration_failure = True` |
| Invalid operator for operand types (F-T-05) | V3 — operator is valid for the declared operand types | Operator validity depends on declared types, not runtime values | `validate_rule_set()` rejects; `ConfigurationError`; `configuration_failure = True` |
| Unsupported categorical value in predicate (F-T-06) | V4 — categorical value belongs to the declared variable domain | Value domains are defined in appendix-c; membership is checkable at supply time | `validate_rule_set()` rejects; `ConfigurationError`; `configuration_failure = True` |

**Extended Algorithm 3 validation scope (this resolution):** `validate_rule_set()` should validate the four structural properties above (V1–V4) in addition to the existing `ConclusionTypes` check. This does not change the Algorithm 3 contract — it extends the set of configuration-fidelity checks that produce `ConfigurationError` before reasoning begins.

Note: V1 (variable existence) is the prerequisite check. A rule with an unknown variable cannot be assessed for type compatibility (V2), so V1 must precede V2. Unknown variable (F-T-11) and type mismatch (F-T-04) are distinct failure classes; one does not subsume the other.

**Why extend Algorithm 3 (not handle at runtime):** Catching these failures at supply time:
1. Preserves the clean semantic boundary between configuration failure and runtime evaluation failure.
2. Reduces the set of failures governed by OPEN-L3-2 to genuine runtime exceptions.
3. Prevents a rule-definition error from producing a runtime exception that could be misread as a data quality problem.

### 3.2 Failures belonging to Algorithm 4 / engine.reason() (OPEN-L3-2 scope)

These failures are only detectable at runtime, when predicates are evaluated against actual context values.

| Failure class | Reason for Algorithm 4 / engine ownership | Handling under selected policy (C+D) |
|---|---|---|
| Runtime predicate exception (F-T-07) | Depends on runtime context values; cannot be caught at supply time | Episode-level refusal: `AI(E) = ∅`; `evaluation_failure = True` |
| Numeric conversion failure on actual value (F-T-08) | Rule definition valid; failure arises from specific runtime value | Episode-level refusal: `AI(E) = ∅`; `evaluation_failure = True` |
| Malformed runtime value (F-T-09) | Rule valid; context value malformed at evaluation time | Episode-level refusal: `AI(E) = ∅`; `evaluation_failure = True` |
| Unexpected internal evaluation error (F-T-10) | Cannot be attributed to any rule/predicate at definition time | Episode-level refusal: `AI(E) = ∅`; `evaluation_failure = True` |

---

## 4. Upstream Failures Not in OPEN-L3-2 Scope

| Failure class | Handled by | Result |
|---|---|---|
| Environmental resolution failure (F-T-01) | Layer 2 / Algorithm 1; ρ_{D,τ} | S = UNSAFE; G(S) = 0; Algorithm 4 lines 1–3 return ∅; Layer 3 not invoked |
| Declared component exclusion (F-T-02) | Layer 2 configuration | Not a failure; m pinned at SAFE |
| Context required field absent (F-T-03) | execute_episode() startup | `ConfigurationError`; `configuration_failure = True`; AI(E) = ∅ |

---

## 5. The UNSAFE Short-Circuit — OPEN-L3-2 Does Not Apply

Algorithm 4 lines 1–3:

```text
1: if G(S) = 0 then
2:     AI ← ∅
3:     return AI
```

`G(UNSAFE) = 0`. For UNSAFE episodes:
- No rule set is selected (Algorithm 3 returns RS(UNSAFE) = ∅).
- `engine.reason()` is never called.
- Predicate evaluation never occurs.
- OPEN-L3-2 policy is unreachable for UNSAFE episodes.

This is structural — it follows from `G(UNSAFE) = 0` and the gate-off at Algorithm 4 lines 1–3. The OPEN-L3-2 policy applies only when `G(S) = 1` (SAFE or CAUTION).

---

## 6. S Mutation Boundary

Layer 3 has no mechanism to modify S. S flows from Algorithm 1 (Layer 2 classifier) and is consumed — not modified — by Algorithms 2, 3, and 4.

Under the selected policy (C+D):
- Evaluation failure → `evaluation_failure = True` in trace; `AI(E) = ∅`
- S is unchanged
- G(S) is unchanged
- A_AI(S) is unchanged

The task §3 instruction is preserved: **"S must not be silently mutated by Layer 3."**

A Layer 3 evaluation failure does not produce `S = UNSAFE`. That would constitute Layer 3 reclassifying an environmental observation, which is the exclusive responsibility of Layer 2 / Algorithm 1.

---

## 7. Boundary Summary

```
┌─────────────────────────────────────────────────────────┐
│ Layer 2 / Algorithm 1                                   │
│   Environmental resolution failure (F-T-01)             │
│   → S = UNSAFE via gᵢ(⊥) = UNSAFE (Corollary C.1b.1)  │
│   → Layer 3 not invoked (G(UNSAFE) = 0)                │
├─────────────────────────────────────────────────────────┤
│ execute_episode() startup                               │
│   Context required field absent (F-T-03)               │
│   → ConfigurationError; AI(E) = ∅; configuration_failure│
├─────────────────────────────────────────────────────────┤
│ Algorithm 3 — validate_rule_set()                       │
│   Unknown predicate variable reference (F-T-11) [V1]   │
│   Rule type mismatch (F-T-04) [V2]                     │
│   Invalid operator (F-T-05) [V3]                       │
│   Unsupported categorical value (F-T-06) [V4]          │
│   → ConfigurationError; AI(E) = ∅; configuration_failure│
├─────────────────────────────────────────────────────────┤
│ Algorithm 4 / engine.reason() — OPEN-L3-2 scope        │
│   Runtime predicate exception (F-T-07)                 │
│   Numeric conversion failure (F-T-08)                  │
│   Malformed runtime value (F-T-09)                     │
│   Unexpected internal error (F-T-10)                   │
│   → Episode-level refusal; AI(E) = ∅; evaluation_failure│
└─────────────────────────────────────────────────────────┘
```

**configuration_failure** and **evaluation_failure** are distinct trace fields. Both produce `AI(E) = ∅`, but for different reasons at different stages. The trace must record which kind of failure occurred.

---

## 8. Design Interpretation vs. External Authority

The extended Algorithm 3 validation scope (§3.1 above) is a **design interpretation** of the existing Algorithm 3 contract, not a statement from an external scientific authority. The rationale is architectural: Algorithm 3 already validates structural admissibility (`ConclusionTypes` check); extending that to predicate-operator and value-domain validation is a natural extension of the same validation role.

The episode-level refusal policy (C+D) for runtime failures (§3.2) is likewise a **design interpretation** — it is consistent with the existing ConfigurationError → `AI(E) = ∅` pattern and with the fail-safe orientation of the broader architecture. No external authority prescribes it; it is chosen as the most conservative option consistent with the existing architecture contracts.

Both design interpretations are flagged as such in `resolution.json` under `authority_class`.
