# Justification: Layer 3 AI advisory component and Safety Dominance enforcement

**Decision:** The Layer 3 AI advisory component is implemented as a rule-based engine. The Safety Dominance Property (AI(E) ⊆ A_AI(S)) is enforced by construction: the rule engine holds a distinct rule set RS(S) per safety state, containing only rules capable of producing recommendation types within A_AI(S).

---

## 1. The three options considered

| Option | Description | Enforcement mechanism | Proof approach | Low-resource suitability |
|---|---|---|---|---|
| **A — Rule-based** | Explicit if-then rules per safety state | Rule set RS(S) excludes non-admissible types by configuration | Proof by construction — RS(S) defines the constraint | Excellent — deterministic, O(1), no GPU |
| **B — ML classifier with constrained output** | Learned model with output head restricted to permitted types | Output layer configured per safety state | Architecture-level enforcement — output space physically restricted | Good — lightweight but requires model inference |
| **C — LLM with output grammar** | Language model constrained by output grammar G_A(S) per state | Grammar intersection with model output distribution at decoding | Formal via grammar containment: A_AI(CAUTION) grammar ⊂ A_AI(SAFE) grammar | Poor — too heavy for low-resource deployment |

---

## 2. Justification for Option A

Option A makes the Safety Dominance Property provable by construction rather than by testing or runtime enforcement. RS(CAUTION) contains no rules that produce DepartureTime or Duration recommendations. The property AI(E) ⊆ A_AI(S) holds not because the engine checks its own output, but because no rule that violates it exists in the active configuration. The constraint is built into the reasoning space before generation begins.

The deployment context reinforces this choice. Coastal fisheries in Terengganu and Penang operate on constrained devices with intermittent connectivity. A rule engine runs in O(1) time with no GPU requirement. Options B and C both require model inference pipelines that are heavier to deploy and less reliable when connectivity drops or power is limited.

Layer 2 already computes S = f(E) through deterministic threshold comparisons. Option A extends that same computational character into Layer 3, so both layers can be verified using the same methods: static analysis and exhaustive testing of a finite classification function. Options B and C introduce probabilistic inference at Layer 3, opening an assurance gap between what Layer 2 can formally guarantee and what Layer 3 can only empirically demonstrate.

---

## 3. The enforcement mechanism

The governance layer (Layer 2) configures Layer 3 before reasoning begins. Given S = f(E):

- If G(S) = 0, Layer 3 receives no input and produces no output. AI(E) = ∅.
- If G(S) = 1, Layer 3 receives E and the rule set RS(S):

```
RS(SAFE)    = rules producing recommendations in {Go, Delay, DepartureTime, Duration}
RS(CAUTION) = rules producing recommendations in {Go, Delay}
RS(UNSAFE)  = ∅  (never passed — G(UNSAFE) = 0)
```

The rule engine fires only rules present in RS(S). Since RS(CAUTION) contains no rules for DepartureTime or Duration, those types cannot appear in AI(E) when S = CAUTION. Their absence is not the result of checking and rejecting outputs after the fact — no rule that generates those types exists in the active configuration. There is nothing to filter.

This is what the architecture description means when it states that recommendations are restricted "structurally — before the AI reasons, not filtered after the fact."

---

## 4. Proof of the Safety Dominance Property

**Claim:** For all E, AI(E) ⊆ A_AI(f(E)).

**Proof by construction.** Let S = f(E) for arbitrary E.

**Case 1: S = UNSAFE.**
G(UNSAFE) = 0. Layer 3 receives no input. AI(E) = ∅. Since A_AI(UNSAFE) = ∅, the containment holds trivially. ∎

**Case 2: S = CAUTION.**
G(CAUTION) = 1. Layer 3 receives E and RS(CAUTION). RS(CAUTION) contains only rules producing recommendations in {Go, Delay}. The rule engine can produce only types present in its active rule set. Therefore AI(E) ⊆ {Go, Delay} = A_AI(CAUTION). ∎

**Case 3: S = SAFE.**
G(SAFE) = 1. Layer 3 receives E and RS(SAFE). RS(SAFE) contains only rules producing recommendations in {Go, Delay, DepartureTime, Duration}. Therefore AI(E) ⊆ {Go, Delay, DepartureTime, Duration} = A_AI(SAFE). ∎

The property holds in all three cases. The proof requires no runtime checking, no output filtering, and no reasoning about probabilistic AI behaviour. It depends only on the definition of RS(S), which is fully under the designer's control.

At the viva, the likely question is: "How do you guarantee AI(E) ⊆ A_AI(S) in your implementation?" The answer: the rule engine in CAUTION mode holds only rules that produce {Go, Delay}. No other recommendation type can appear because no rule that generates it exists in the active configuration. The guarantee is architectural, not behavioural.

---

## 5. What this means for the architecture description

Layer 3 in `architecture-illustration.md` was previously described as a "probabilistic / learned component." Layer 3 is a rule-based engine whose active rule set RS(S) is supplied by the governance layer before any reasoning occurs. The formal pipeline is unchanged:

```
E → S = f(E) → (G(S), A_AI(S)) → AI(E) → Human Decision
```

The difference is in how AI(E) is generated: by a rule engine configured with RS(S), not by a probabilistic model. The Safety Dominance Property follows from the rule set definition.

---

## 6. Limitations of the rule-based choice

Option A gives a clean proof but narrows the advisory component's expressiveness.

A rule engine handles threshold-based, categorical, and logical combinations of environmental parameters well. What it cannot do, without explicit encoding, is capture non-linear interactions or patterns learned from historical catch data. For the departure decision problem in its current scope — directional guidance and threshold-based timing — this is sufficient. If future work extends R to include recommendation types that require learned generalisation (fishing area selection, species-specific guidance), a hybrid design with a constrained ML output layer would need to be considered. That extension would require a separate enforcement argument, since a constrained ML layer cannot rely on the construction proof above.

The rule sets also require ongoing maintenance. As R expands or threshold values are recalibrated, RS(S) must be updated across all three safety states in a way that preserves A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅. This is a design responsibility, not an architectural defect, but it should be documented explicitly.
