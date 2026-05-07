# Architectural layering design and graphic representation

---

## 1. Design philosophy

The architecture organises decision-making as a layered governance system. Lower layers handle environmental input and safety constraints; middle layers implement governance and control; upper layers handle AI reasoning and human decision-making. Decision authority flows bottom-up through the pipeline, while constraints flow top-down from governance into AI. No layer can exceed the permissions granted by the layer below it.

---

## 2. Layer structure

Four main layers make up the architecture, with sub-layers in Layers 2 and 3:

| Layer | Name | Sub-layers |
|---|---|---|
| Layer 1 | Environmental input | — |
| Layer 2 | Deterministic safety governance | 2a: Safety state classification; 2b: Governance decision |
| Layer 3 | Advisory AI system | 3a: Participation control; 3b: Admissible action space; 3c: Recommendation generation |
| Layer 4 | Human decision layer | — |

### Governance logic by safety state

| Safety state | G(S) | A_AI(S) | RS(S) passed to Layer 3 | AI(E) | Layer 3 status |
|---|---|---|---|---|---|
| SAFE | 1 | {Go, Delay, DepartureTime, Duration} | RS(SAFE) — full rule set | ⊆ {Go, Delay, DepartureTime, Duration} | Active — full advisory scope |
| CAUTION | 1 | {Go, Delay} | RS(CAUTION) — restricted rule set | ⊆ {Go, Delay} | Active — restricted advisory scope |
| UNSAFE | 0 | ∅ | Not passed | ∅ | Disabled — no output |

The Safety Dominance Property AI(E) ⊆ A_AI(S) holds in all three rows. Under UNSAFE it holds trivially (∅ ⊆ ∅). Under CAUTION and SAFE it holds by construction: RS(S) contains only rules capable of producing recommendation types within A_AI(S), so the rule engine cannot generate an inadmissible type.

---

## 3. Layer 2 — deterministic safety governance

Layer 2 is the governance core of the architecture. It enforces deterministic control over AI participation through risk-based decision gating, ensuring that safety state takes precedence over AI output before any AI reasoning begins.

### 3.1 Layer 2a — safety state classification

Layer 2a maps environmental input into discrete safety states. Given the environmental feature vector E = {w, r, m, o, v, t}, the classification function S = f(E) returns one of three states: SAFE, CAUTION, or UNSAFE. This mapping is fully deterministic — no AI involvement, no probabilistic inference. The same environmental inputs always produce the same safety state.

### 3.2 Layer 2b — governance decision

Layer 2b determines system behaviour based on the classified safety state. It produces a governance pair: a participation decision G(S) ∈ {0, 1}, where G(S) = 1 permits AI participation and G(S) = 0 blocks it; and an admissible action space A_AI(S) defining the recommendation types AI may produce. Together, (G(S), A_AI(S)) control everything that Layer 3 is permitted to do.

---

## 4. Layer 3 — advisory AI system

Layer 3 operates exclusively within the constraints supplied by Layer 2. Before any reasoning begins, Layer 2 determines whether Layer 3 may participate and defines the set of recommendation types it may produce. Layer 3 has no independent decision authority.

### 4.1 Layer 3a — participation control

Layer 3a enforces the participation gate. When G(S) = 0, Layer 3 receives no input and produces no output: AI(E) = ∅. When G(S) = 1, Layer 3 is enabled and receives the environmental input E along with the rule set RS(S) from Layer 2. AI execution is gated before inference begins, not filtered after the fact.

### 4.2 Layer 3b — admissible action space

Layer 3b defines the boundary of what Layer 3 may recommend. The admissible action space satisfies the containment property:

A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅

Under SAFE, Layer 3 may produce recommendations from the full set {Go, Delay, DepartureTime, Duration}. Under CAUTION, the space contracts to {Go, Delay}. Under UNSAFE, no recommendations are permitted. This containment relationship is the formal expression of the Safety Dominance Property.

### 4.3 Layer 3c — recommendation generation

Layer 3c implements recommendation generation as a **production rule system**: a classical AI architecture in which each rule takes the form `IF <condition> THEN <action>`. Layer 2 supplies the active rule set RS(S) before reasoning begins. RS(CAUTION) contains only rules producing recommendations in {Go, Delay}; RS(SAFE) extends this to include DepartureTime and Duration. RS(UNSAFE) is empty and is never passed to Layer 3 because G(UNSAFE) = 0.

The rule engine fires only rules present in the active set, so no inadmissible recommendation type can appear in AI(E). Safety Dominance (AI(E) ⊆ A_AI(S)) holds by construction rather than by runtime checking — the constraint is the rule set itself, not a post-hoc filter.

---

## 5. Why sub-layers exist

Sub-layers separate responsibilities that would otherwise collapse into a single undifferentiated block. Without the separation, safety state detection and governance decisions mix, AI control logic becomes unclear, and formalisation is harder to express.

| Sub-layer | Responsibility | Formal function |
|---|---|---|
| 2a | Safety state classification | S = f(E) |
| 2b | Governance decision | G(S), A_AI(S) |
| 3a | AI participation | Gate on G(S) |
| 3b | Action restriction | A_AI(S) constraint |
| 3c | Recommendation generation | AI(E) ⊆ A_AI(S) |

Each sub-layer maps to a distinct formal function. This one-to-one correspondence between architectural components and formal definitions is what makes the architecture verifiable rather than just describable.

---

## 6. Graphic design concept

The architecture is represented as a control-flow diagram with a vertical pipeline structure.

### 6.1 Visual flow

```
Layer 1      Environmental input
↓
Layer 2a     Safety state classification  S = f(E)
↓
Layer 2b     Governance decision  →  (G(S), A_AI(S), RS(S))
↓
Layer 3a     AI participation (enable/disable on G(S))
↓
Layer 3b     Action restriction  →  A_AI(S) applied
↓
Layer 3c     Recommendation generation (production rule system)
↓
Layer 4      Human decision
```

### 6.2 Design principles

**Vertical flow** represents the sequential decision pipeline. Each step depends on the output of the step above: constraints propagate downward; the recommendation surfaces upward to the human.

**Layer grouping.** Layer 2 (sub-layers 2a and 2b) is grouped under a single "Governance" block. Layer 3 (sub-layers 3a, 3b, 3c) is grouped under a single "AI System" block. This grouping makes the two-level governance structure visible without requiring the viewer to track individual sub-layers.

**Hard boundary between Layer 2 and Layer 3.** This boundary represents the Safety Dominance Property. Layer 3 does not run until Layer 2 resolves G(S) and supplies RS(S). The constraints cross this boundary with the data — they are not applied after the fact.

**Constraint flow arrows** from Layer 2 into Layer 3 carry both the participation gate (G(S)) and the active rule set (RS(S)). These should appear as a secondary arrow or annotation alongside the main vertical pipeline to show what Layer 2 passes down, distinct from the primary data flow.

### 6.3 Colour coding

- Layer 2 (governance): red or orange — safety control takes precedence
- Layer 3 (AI system): blue — AI processing, constrained
- Layer 4 (human): green — human decision authority

---

## 7. Core concept

> The architecture separates decision capability from decision permission.

Layer 3 defines what the AI can compute. Layer 2 defines what the AI is allowed to recommend. A production rule system in Layer 3 makes that permission enforceable by construction: RS(S) is the permission, and the rule engine cannot exceed it.

---

## 8. Contribution summary

The layered design produces five properties that a flat or binary architecture cannot provide together.

First, deterministic safety enforcement: Layer 2 classifies state and applies governance before AI runs. Second, controlled AI participation: G(S) gates whether AI operates at all. Third, constrained recommendation space: A_AI(S) limits what AI may recommend, not just whether it runs. Fourth, formal verifiability: each sub-layer corresponds to a formally defined function, and the Safety Dominance Property is provable by construction from the rule set definition. Fifth, an explainable decision pipeline: every recommendation is traceable through the layer structure to the environmental conditions that produced it.

---

## 9. One-line summary

> The architecture governs both whether AI participates and what it is allowed to recommend, using a deterministic safety layer that takes precedence over AI reasoning.

---
