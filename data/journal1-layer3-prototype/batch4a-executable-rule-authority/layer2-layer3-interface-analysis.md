# Layer 2 / Layer 3 Interface Analysis

**Date:** 2026-09-11
**Branch:** design/journal1-layer3-executable-rule-authority
**Task:** Batch 4A — Executable Rule-Set Authority Resolution

---

## Q1: What information is Layer 2 formally allowed to expose to Layer 3?

The canonical architecture (Appendix C §C.7.2, Theorem C.3) defines the formal interface as:

```
Layer 2 → (S, RS(S)) → Layer 3
```

where S ∈ {SAFE, CAUTION, UNSAFE} and RS(S) is the rule set appropriate for state S.

The Safety Dominance proof (Theorem C.3) depends only on the **value of S** and the properties of RS(S). It does not constrain what additional information may accompany S in the interface. Specifically:

> *"The proof depends only on the value of S, never on how S was reached."*
> — Appendix C §C.7.2

The Layer 3 specification (§7) further states:

> *"If Layer 3 implementation in later batches identifies a need for additional advisory inputs not derivable from canonical E, those inputs must be documented explicitly here as implementation-level additions — they must not silently extend the formal definition of E in appendix-c-formalisation.md."*

This provision has two implications:
1. **Permitted:** implementation-level additions to the Layer 3 interface, documented in §7
2. **Protected:** Appendix C (formal variable definitions) must not be silently extended

Layer 2 is therefore formally permitted to expose to Layer 3:
- S (required, already in interface)
- RS(S) (required, already in interface)
- Any implementation-level additions documented in layer3-prototype-specification.md §7, provided they do not redefine canonical E variables

Component-state outputs (g_i(·) results) are intermediate Layer 2 computations. Exposing them as §7 implementation-level additions is within the permitted scope.

---

## Q2: Does exposing component-state outputs change the scientific architecture or merely make an already-existing internal result explicit?

**Finding: Implementation-level interface enrichment, not a scientific architecture change.**

Layer 2 computes g_i(·) internally as part of computing S:

```
f(E) = max-severity(g_w(w), g_r(r,κ), g_m(m), g_o(o,v), g_t(t,date))
```

Each g_i(·) result is an intermediate value that already exists in Layer 2 at the time S is produced. Exposing these via ComponentStateTrace is analogous to a function returning not just its final output but also named intermediate results — the computation is unchanged.

The scientific architecture:
- Does not change which rules are admitted (Batch 2 authority unchanged)
- Does not change S or how it is computed
- Does not change A_AI(S) or G(S)
- Does not change RS(S) selection or validation
- Does not change Safety Dominance (see Q3)

**Contrast with Layer 2 duplication (Model A):** If Layer 3 were to evaluate `resolved_w >= 21.6 AND resolved_w < 27.0`, it would be performing the g_w classification independently. That is duplication. Consuming the g_w output (w_state=CAUTION) is not.

---

## Q3: Would Layer 3 consumption of component states violate `S = max-severity(...)` or Safety Dominance?

**Finding: No.**

**`S = max-severity(...)` unchanged.** Layer 2 continues to compute S by the canonical formula. Layer 3 does not participate in this computation. Layer 3 receives S from the caller and consumes it as a precondition for RS(S) selection.

**Safety Dominance (Theorem C.3) unaffected.** The proof structure is:

```
G(S) = 0 → AI = ∅           (Case 1: UNSAFE — gate-off)
G(S) = 1, S=CAUTION →
  RS(CAUTION) ⊆ {Go,Delay} →
  AI ⊆ {Go,Delay} = A_AI(CAUTION)   (Case 2)
G(S) = 1, S=SAFE →
  RS(SAFE) ⊆ {Go,Delay,DepartureTime,Duration} →
  AI ⊆ A_AI(SAFE)                    (Case 3)
```

This proof depends only on the value of S and the structure of RS(S). Whether DecisionContext carries additional fields (component states, episode ID, vessel category) is irrelevant to the proof. Additional interface data cannot cause the engine to produce recommendation types outside A_AI(S) — A4 (engine fidelity) constrains output to rule conclusion types in the active RS(S), which A2 constrains to A_AI(S).

---

## Q4: Does R-SAFE-001 collapse logically into `S == SAFE → Go` under the current formalisation?

**Finding: YES — STATE_RESTATEMENT confirmed.**

**Proof:**

The canonical classifier: `f(E) = max-severity(g_w(w), g_r(r,κ), g_m(m), g_o(o,v), g_t(t,date))`

max-severity returns SAFE if and only if ALL arguments are SAFE.

```
S = SAFE
⟺ g_w(w)=SAFE ∧ g_r(r,κ)=SAFE ∧ g_m(m)=SAFE ∧ g_o(o,v)=SAFE ∧ g_t(t,date)=SAFE
```

Under the retrospective replay where m ∈ D: g_m(m) is pinned at SAFE (exclusion semantics). The R-SAFE-001 antecedent includes g_m(m)==SAFE, which is vacuously satisfied by exclusion. Therefore:

```
R-SAFE-001 antecedent:
all(g_w==SAFE, g_r==SAFE, g_m==SAFE, g_o==SAFE, g_t==SAFE)
≡ S = SAFE    (under the canonical formulation with D={m})
```

**More critically:** Layer 3 executes only when G(S) = 1, i.e. S ∈ {SAFE, CAUTION}. When Layer 3 is called with state="SAFE", the UNSAFE gate-off has already prevented execution for any unsafe component. When state="SAFE":

- No component can be CAUTION (else S would be CAUTION)
- No component can be UNSAFE (else S would be UNSAFE)
- Excluded components contribute SAFE by exclusion semantics

Therefore, in the execution context where R-SAFE-001 would apply (Layer 3 called with state="SAFE"), ALL component states are already guaranteed to be SAFE. The antecedent is always TRUE. The rule fires unconditionally in every S=SAFE episode.

**This is an automatic SAFE→Go mapping.** Batch 2 explicitly concluded (closure-batch2.json OPEN_L3_1A_Go): "CONDITIONALLY SUPPORTED" with inference bridge required. The inference bridge is environmental discriminant — R-SAFE-001 as structured contains no discriminant beyond state=SAFE.

**Disposition:** DEFERRED (STATE_RESTATEMENT). Requires a bounded scientific decision: either (a) identify an additional environmental discriminant to be added to the antecedent, distinguishing which SAFE episodes warrant Go, or (b) acknowledge that SAFE→Go is the intended behaviour and document it explicitly as a design decision with scientific justification.

---

## Q5: Can R-CAUTION-002/003/004 be implemented without copying `g_o`, `g_r`, `g_w` logic into Layer 3?

**Finding: YES — via Model B (component-state interface).**

Under Model B, Layer 2 exposes g_i(·) outputs as ComponentStateTrace:

```
ComponentStateTrace:
    w_state: "SAFE" | "CAUTION" | "EXCLUDED"
    r_state: "SAFE" | "CAUTION" | "EXCLUDED"
    m_state: "SAFE" | "CAUTION" | "EXCLUDED"
    o_state: "SAFE" | "CAUTION" | "EXCLUDED"
    t_state: "SAFE" | "EXCLUDED"  (g_t emits no CAUTION; t ∉ D)
```

Layer 3 rules consume these as facts:

```
R-CAUTION-002: ConditionPredicate(variable='component_o_state', operator='==', value='CAUTION')
R-CAUTION-003: ConditionPredicate(variable='component_r_state', operator='==', value='CAUTION')
R-CAUTION-004: ConditionPredicate(variable='component_w_state', operator='==', value='CAUTION')
```

All threshold logic stays inside Layer 2:
- g_w thresholds (21.6, 27.0 kn) remain in Layer 2
- g_r thresholds (10.0, 20.0 mm/hr) and κ logic remain in Layer 2
- g_o vessel-category bands remain in Layer 2

Layer 3 receives the classified output only. No Layer 2 logic is duplicated.

---

## Q6: How are excluded/faulted components represented at the interface?

**Exclusion (D):**

Excluded components (m ∈ D in the retrospective replay) are pinned at SAFE for max-severity purposes. However, exposing m_state=SAFE would falsely imply a valid observation. The interface must use a distinct value:

```
m_state = "EXCLUDED"   (m ∈ D)
```

This preserves the distinction between:
- SAFE: valid observation, within safe thresholds
- EXCLUDED: no data source; classification pinned at SAFE for architectural purposes

**Fault (⊥):**

Required non-excluded components that resolve to ⊥ cause g_i(⊥) = UNSAFE, which causes S = UNSAFE by max-severity. S = UNSAFE triggers the UNSAFE gate-off (G(UNSAFE) = 0), and Layer 3 is never called. Therefore:

**UNSAFE and FAULTED component states are never visible to Layer 3.**

When Layer 3 executes (G(S) = 1), the component state domain at the interface is:

```
{SAFE, CAUTION, EXCLUDED}
```

UNSAFE is unreachable at the Layer 3 interface — it would have triggered gate-off before Layer 3 was invoked. This is not a gap; it is a consequence of the UNSAFE gate-off design.

**Summary:**

| Component state at runtime | Layer 3 visible? |
|---|---|
| SAFE (valid, safe threshold) | YES |
| CAUTION (valid, caution threshold) | YES |
| EXCLUDED (m ∈ D) | YES — as EXCLUDED |
| UNSAFE (valid, unsafe threshold) | NO — S=UNSAFE → gate-off |
| FAULTED (⊥) | NO — g_i(⊥)=UNSAFE → S=UNSAFE → gate-off |

---

## Q7: Would the proposed interface change Algorithm 3 complexity?

**Finding: No.**

Algorithm 3 (select_rule_set + validate_rule_set) operates on rules, not on DecisionContext. Adding component state fields to DecisionContext does not affect:

- Rule selection (still filters by applicable_state + enabled)
- A_AI containment check (still checks conclusion_type ∈ A_AI(S))
- V1–V4 validation (DECISION_CONTEXT_SCHEMA would gain new fields, but validation logic is unchanged in structure)

DECISION_CONTEXT_SCHEMA in rule_set_provider.py would need new entries for the component state fields, defining their type (str), nullability, and domain ({SAFE, CAUTION, EXCLUDED}). This is an incremental change to the schema, not an algorithmic change.

Algorithm 4 complexity remains O(k_S × c): linear in rules and conditions per rule. The number of conditions per rule may increase slightly (rules with multiple component-state predicates), but the engine structure is unchanged.

---

## Q8: Would any proposal require canonical architecture modification?

**Finding: YES — Model B requires a canonical modification to `architecture-illustration.md`.**

**Classification: Option A**

**Protected files (Batch 4A §29):**
- `docs/canonical/appendix-c-formalisation.md`
- `docs/canonical/architecture-illustration.md`

**Appendix C:** No change required. The Safety Dominance proof is independent of interface content (see Q3). The formal variable definitions (C.1–C.9) are unchanged. No new canonical variable is introduced.

**architecture-illustration.md:** This file is explicitly listed as a protected canonical file in Batch 4A §29. It is the canonical full architecture walkthrough covering layers, the governance table, the scenario, and — critically — the Layer 2 → Layer 3 interface. The interface currently documented (Layer 2 supplies S and RS(S) to Layer 3) would be factually incomplete if ComponentStateTrace is added. Completing the documentation to reflect that Layer 2 also exposes component-state outputs IS a modification to a protected canonical file. This is therefore a canonical modification by the definition in task §29.

**Why this is Option A and not Option B:** Both canonical files reside under `docs/canonical/` and are explicitly named in §29's protection list. Protection implies that changes to these files in Batch 4A are prohibited — not that the files are "merely illustrative" in some weaker sense. If architecture-illustration.md were documentation-only with no canonical standing, the task would not have listed it alongside Appendix C as a file that triggers a stop condition. Its presence in the §29 protection list settles its standing.

**Consequence for Batch 4A:** The canonical modification CANNOT be performed in this task. Per §29, Batch 4A stops at the canonical boundary. The authority question (can the rules be expressed without Layer 2 duplication?) is fully answered YES via Model B. The stop applies to the canonical modification itself — not to the analysis conclusion. `implementation_authorised` is therefore false: Batch 4B must first obtain review and approval for the architecture-illustration.md update before implementation may proceed.

**Appendix C is unaffected.** The Safety Dominance proof, formal variable definitions, and governance pair (G(S), A_AI(S)) do not change. The canonical change is scoped to architecture-illustration.md's interface description only.

**What Batch 4B must do before implementation:**
1. Obtain review and approval for updating `docs/canonical/architecture-illustration.md` (canonical change)
2. Update `publications/active/journal-1/layer3-prototype-specification.md §7` — add ComponentStateTrace fields to DecisionContext
3. Update `governance/rule_set_provider.py` — add component state fields to DECISION_CONTEXT_SCHEMA
4. Update `governance/canonical_rules.py` — add R-CAUTION-002, 003, 004
5. Update `governance/reasoning_episode.py` — add component state fields to DecisionContext
6. Run engineering tests

---

## R-CAUTION-001 Consistency Note

R-CAUTION-001 is currently implemented as `resolved_m == "advisory"`. Under the proposed Model B interface, a consistency alternative exists:

```
m_state == CAUTION
```

This would be equivalent if g_m("advisory") = CAUTION and g_m("warning"/"alert") = UNSAFE. The Model B form is more general (automatically handles any future m value that maps to CAUTION) and more consistent with the interface pattern.

**Record as future migration consideration for Batch 4B.** No change to the current implementation in Batch 4A.
