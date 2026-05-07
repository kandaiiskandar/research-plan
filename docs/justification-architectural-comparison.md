# Justification: Architectural Comparison and Positioning of the Two-Level Governance Contribution

**Document type**: Theoretical justification / argumentation note  
**For**: Chapter 2 (Literature Review), Chapter 3 (Architecture Design), and viva preparation  
**Questions addressed**: How does this architecture differ from existing layered AI architectures? What is the precise nature of the gap? What does "graduated" mean formally? Why is pre-generation restriction architecturally superior to post-generation filtering in low-resource settings? How is this CS research, not social science or software development?

**Cross-references**: For formal model definitions, see `docs/appendix-c-formalisation.md`. For novelty gap argument, see `docs/justification-novelty-gap.md`. For low-resource environment justification, see `docs/justification-low-resource-environments.md`. For binary governance external evidence, see `docs/justification-binary-governance-external-evidence.md`.

---

## 1. The Conventional Four-Layer AI DSS Architecture

The literature consistently describes a four-layer pattern for hybrid AI decision support systems:

| Layer | Role | Nature |
|---|---|---|
| L1 | Input — environmental data, sensor readings, user query | Observable |
| L2 | Deterministic — rule-based safety classification or symbolic reasoning | Deterministic |
| L3 | Probabilistic — AI/ML advisory or reasoning component | Probabilistic |
| L4 | Human — final decision-maker retaining full authority | Human |

This pattern is independently confirmed across multiple architectural proposals:

- **Castagnone & Nitti (2026)** [[notes]](../notes/A%20Neuro-Symbolic%20Framework%20for%20Ensuring%20Deterministic%20Reliability%20in%20AI-Assisted%20Structural%20Engineering-%20The%20SYNAPSE%20Architecture.md) — SYNAPSE: User Interface Layer (L1) → Intelligent Query System/symbolic core (L2) → LLM Interface (L3) → Engineer decision-maker (L4)
- **Pitale et al. (2025)** [[notes]](../notes/HySAFE-AI-%20Hybrid%20Safety%20Architectural%20Analysis%20Framework%20for%20AI%20Systems-%20A%20Case%20Study.md) — HySAFE-AI: Sensor inputs (L1) → Safety Evaluator + Policy Monitor (L2) → End-to-end Foundation Model (L3) → Human driver (L4)
- **Shamsujjoha et al. (2025)** [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md) — Swiss Cheese: External environment (L1) → Multi-layered guardrails (L2/L3 boundary) → FM-based agent (L3) → Human intervention (L4)
- **Vedrtnam et al. (2025)** — Environmental AI: Sensor data (L1) → AI analysis (L3) → Alert/prediction (binary output) → Human response (L4)

The proposed architecture follows this same four-layer pattern. The contribution is not a new layering paradigm — it is a formally novel mechanism at the boundary between L2 and L3: **pre-generation advisory scope restriction governed by classified environmental safety state**.

---

## 2. The Problem with Existing Implementations

In all existing implementations of the four-layer pattern, the deterministic layer (L2) implements only **binary participation control**: the AI either operates at full scope or is blocked entirely.

The formal representation of existing Level 1-only governance:

**G(S) → {participate, block}**

When G(S) = 1 (participate), the AI generates recommendations from its full recommendation space R_full, regardless of how dangerous the environmental conditions are. No existing architecture formally specifies which *categories* of recommendation the AI is permitted to generate under each safety state.

**The specific problem this creates:**

Under CAUTION conditions, the AI's probabilistic model operates at the boundary of its reliable range. Environmental data is degraded. The AI may still confidently generate a departure time recommendation — but that recommendation is unreliable because the conditions that triggered CAUTION have degraded the data supporting it. The human decision-maker receives a confident-looking recommendation without knowing the AI is advising beyond its reliable range.

In formal terms: existing architectures cannot enforce the Safety Dominance Property AI(E) ⊆ A_AI(S) because they define no A_AI(S) — the admissible recommendation space is always R_full when the AI participates.

---

## 3. Fundamental Architectural Comparison

The following table identifies the precise formal difference between the proposed architecture and the three closest existing architectures:

| Dimension | SYNAPSE — Castagnone & Nitti (2026) | HySAFE-AI — Pitale et al. (2025) | Swiss Cheese — Shamsujjoha et al. (2025) | Vedrtnam et al. (2025) | **This Architecture** |
|---|---|---|---|---|---|
| **What is governed** | LLM-generated scripts | AI-generated trajectories | User input content and AI output content | Environmental prediction outputs | AI advisory recommendation categories |
| **Trigger** | Task type — LLM role permanently fixed | Per-output — each trajectory individually validated | Content of user request or AI output | Threshold — alert fires or not | Environmental safety state S = f(E) |
| **What it produces** | Pass or fail on script before execution | Accept or reject each trajectory | Block, filter, flag, modify, or validate | Binary alert or no alert | Admissible recommendation space A_AI(S) |
| **Governance type** | Static architectural separation | Per-output validation | Multi-layered content safety checking | Binary alerting | Pre-generation advisory scope restriction |
| **Pre or post generation** | Post-generation — LLM generates script, then checked | Post-generation — AI generates trajectory, then checked | Both — wraps AI at input, during, and output | Post-generation — AI predicts, then alert fires | Pre-generation — scope defined before AI reasons |
| **Static or dynamic** | Static — LLM role never changes regardless of conditions | Static — same checks applied regardless of environment | Context-dependent but not environmental-state-conditioned | Static — threshold does not vary by advisory category | Dynamic — scope varies by classified environmental state |
| **Binary or graduated** | Static restriction — always the same | Binary — accept or reject | Binary per action | Binary — alert or no alert | Graduated — A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ |
| **Formal safety property** | No — design-time principle, not runtime-verified | No — engineering analysis, not formal proof | No — taxonomy and reference architecture only | No — no formal model | Yes — Safety Dominance Property AI(E) ⊆ A_AI(S) |
| **Low-resource suitable** | No — cloud infrastructure, GPT-4, AWS | No — large foundation models, high compute | No — targets FM-based agents | Not addressed | Yes — deterministic governance, O(1) compute |
| **Domain** | Structural engineering | Autonomous driving | LLM agents | Environmental monitoring | Maritime DSS for human decision-makers |

**The single most important row is the trigger row.** None of the existing architectures are triggered by environmental safety state. This is the architectural gap the proposed research fills.

---

## 4. The Precise Distinction: Environmental State Trigger vs Content Trigger

A critical distinction must be maintained between two types of governance trigger that appear superficially similar but are formally different:

**Swiss Cheese prompt checking** is triggered by the **content of the user's request** — it asks: "Is this request safe to process?" It evaluates input text against content safety rules (banned topics, harmful intent, schema violations).

**This architecture's Layer 2** is triggered by the **classified environmental state S = f(E)** — it asks: "What is the AI permitted to recommend given current physical conditions?" It evaluates E = {w, r, m, o, v, t} against safety classification thresholds.

The formal difference:

| | Swiss Cheese Prompt Check | This Architecture — Layer 2 |
|---|---|---|
| Input | User text/request | Environmental state E = {w, r, m, o, v, t} |
| Question | Is this request safe? | What may the AI recommend? |
| Trigger | Content of user input | Physical environmental conditions |
| Output | Allow or block prompt | Admissible recommendation space A_AI(S) |
| Governance type | Content safety | Operational safety governance |
| Binary or graduated | Binary — allow or block | Graduated — SAFE, CAUTION, UNSAFE |

**Illustrative example:** A fisher asks "What time should I depart tomorrow?" — a perfectly well-formed, non-harmful request. The Swiss Cheese prompt check allows it through because the content is safe. This architecture still restricts the AI from answering that question if S = CAUTION — not because the question is inappropriate, but because the environment makes that recommendation type unreliable. Same question. Different trigger. Different outcome. Different concept.

---

## 5. Pre-Generation Restriction vs Post-Generation Filtering

The reason existing architectures use post-generation filtering is structural: they treat the AI as a black box. The safety architect does not control what the AI generates internally — they can only observe the output and decide to allow, modify, or block it. Post-generation filtering is the only option available when governance is external to the AI's reasoning process.

**Post-generation filtering (Swiss Cheese, HySAFE-AI):**
```
Input
  ↓
[AI generates recommendations] ← full scope, unconstrained
  ↓
[Safety check / guardrail] ← checks output after generation
  ↓
[Block or allow]
  ↓
Human
```

**Pre-generation scope restriction (this architecture):**
```
Input E = {w, r, m, o, v, t}
  ↓
[Deterministic layer] → S = f(E) → {SAFE, CAUTION, UNSAFE}
  ↓
[Governance layer] → A_AI(S) defined before AI reasons
  ↓
[AI generates recommendations] ← only within A_AI(S)
  ↓
Human
```

**Why pre-generation restriction is formally stronger:**

Post-generation filtering cannot guarantee the Safety Dominance Property. The AI generates the unsafe recommendation — it is simply not shown to the user. The unsafe reasoning still occurred. Pre-generation restriction ensures AI(E) ⊆ A_AI(S) by construction — the unsafe recommendation is never generated at all, because the AI was never asked to reason about that recommendation category.

In formal terms: the AI does not produce output and get filtered — it operates inside a pre-defined admissible space. The Safety Dominance Property holds as a structural guarantee, not as an enforcement mechanism applied after violation.

---

## 6. What "Graduated" Means Precisely

"Graduated" in this architecture refers specifically to **advisory scope** — the number and type of recommendation categories the AI is permitted to generate.

```
S = SAFE    → A_AI(S) = {Go, Delay, DepartureTime, Duration}  ← full scope (4 types)
S = CAUTION → A_AI(S) = {Go, Delay}                           ← restricted scope (2 types)
S = UNSAFE  → A_AI(S) = ∅                                     ← no scope (0 types)
```

The scope **steps down** as the environment becomes more dangerous, producing the containment hierarchy:

**A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅**

What is NOT graduated:
- The safety state S — classified deterministically, not on a continuous scale
- The participation gate G(S) — binary, on or off
- The environmental inputs — measured continuously but classified into discrete states

What IS graduated:
- The **admissible recommendation space A_AI(S)** — formally contracts in defined steps as S worsens

This is the architectural meaning of "graduated safety-state-gated." The architecture does not simply switch the AI on or off — it gates which categories of advice the AI may give, stepping down through formally defined states. The traffic light analogy: existing systems have only green and red. This architecture adds yellow — the AI still participates under CAUTION, but with a formally restricted advisory scope.

---

## 7. Pre-Generation Restriction Is Computationally Superior in Low-Resource Settings

In low-resource environments, post-generation filtering carries a specific computational cost problem. Filtering requires the AI to first generate the full recommendation set, then a second process evaluates and discards impermissible outputs. This doubles the computational burden — two inference passes where one would suffice.

A TinyML-based post-generation filter faces additional problems in safety-critical contexts:

- **Accuracy degradation**: TinyML models are quantised and compressed, reducing accuracy. A reduced-accuracy filter making safety-critical decisions is architecturally unsafe.
- **Probabilistic filter**: The filter model is still probabilistic — it can itself make errors. Two probabilistic components in the pipeline compound uncertainty with no formal safety guarantee.
- **No formal Safety Dominance Property**: A TinyML post-generation filter cannot formally prove AI(E) ⊆ A_AI(S). It can only make violations statistically less likely.

Pre-generation scope restriction via a deterministic governance layer avoids all these problems. The governance layer S = f(E) performs simple threshold comparisons — O(1) compute, formally verifiable, battery-efficient, no second inference pass. 

Katende (2026) [[notes]](../notes/Rethinking%20data-efficient%20artificial%20intelligence%20for%20low-resource%20settings.md) articulates the design principle directly: **constraint-first method selection** — AI methods should be selected based on measured deployment constraints, not transferred from high-resource contexts. Post-generation filtering violates this principle by assuming the compute budget for two inference passes. Pre-generation deterministic governance satisfies it by concentrating reasoning within the permitted advisory scope from the outset.

Perez-Cerrolaza et al. (2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) note the SWaP (Size, Weight, Power) constraints on edge-deployed safety-critical AI systems. The proposed governance layer has negligible SWaP requirements — it is deployable on any device capable of running a simple conditional statement.

---

## 8. Research Positioning: Formal Methods and Safety-Critical Systems Architecture

This research does not sit in social science, software development research, or domain application research. It sits in **formal methods and safety-critical systems architecture** — the same CS sub-field as safety shields, runtime assurance architectures, Simplex architecture, and ODD frameworks.

The contribution is a **formal architecture specification** with provable properties:
1. Participation Constraint: G(S) = 0 ⇒ A_AI(S) = ∅
2. Advisory Restriction Constraint: S = CAUTION ⇒ A_AI(CAUTION) ⊂ A_AI(SAFE)
3. Safety Dominance Property: AI(E) ⊆ A_AI(S) for all E

These are formal CS properties. The fishing domain is where the architecture is evaluated — it is not what the architecture is. A CS researcher who designs a medical diagnosis algorithm is not doing medicine. This research does not do social science — it designs a formal governance architecture that is evaluated in a maritime context.

The gap these properties fill is confirmed independently by the ML systems architecture literature. Indykov et al. (2025) [[notes]](../notes/Architectural%20tactics%20to%20achieve%20quality%20attributes%20of%20machine-learning-enabled%20systems-%20a%20systematic%20literature%20review.md) conducted a systematic review of 206 papers and identified 16 architectural tactics for ML-enabled systems against 11 common quality attributes. Safety is one of the two most frequently cited quality attributes (19 papers). Their trade-off matrix (Table 3) shows AT11 Rule-based Models — the tactic conceptually closest to the deterministic governance layer — scoring **0 (insufficient evidence) for Safety**. No identified tactic demonstrates a formally positive impact on the Safety attribute. This independently confirms that the architectural tactics literature has not established how rule-based mechanisms formally guarantee safety properties in ML-enabled systems — which is precisely what the Safety Dominance Property AI(E) ⊆ A_AI(S) provides.

The supervisor question "is this software development research?" can be addressed precisely: software development research asks "does this system work?" This research asks "what formal architectural properties must a governance layer satisfy to guarantee safe AI advisory behaviour across graduated safety states?" The contribution is the formal specification and its provable properties — not a software product.

---

## 9. The Core Argument in One Paragraph (for supervisor meetings and viva)

The conventional four-layer hybrid AI DSS architecture — input, deterministic governance, probabilistic AI advisory, human decision-maker — is well-established across CS literature (Castagnone & Nitti, 2026; Pitale et al., 2025; Shamsujjoha et al., 2025) and environmental AI literature (Vedrtnam et al., 2025). In all existing implementations, the deterministic layer implements only binary participation control: the AI either operates at full scope or is blocked. No existing architecture formally specifies pre-generation advisory scope restriction — a mechanism that restricts which *categories* of recommendation the AI is permitted to generate based on classified environmental safety state. This gap means that when the AI participates under CAUTION conditions, it generates the same full recommendation set as under SAFE conditions, despite operating beyond its reliable range. The proposed architecture addresses this gap by formally defining a two-level governance pair (G(S), A_AI(S)) where Level 1 controls participation and Level 2 controls advisory scope, governed by a deterministic safety state classification S = f(E). The resulting containment hierarchy A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ formally guarantees the Safety Dominance Property AI(E) ⊆ A_AI(S) — a property no existing architecture defines or enforces.

---

## 10. Viva-Ready Responses to Examiner Challenges

**"Isn't your Level 2 just a guardrail or prompt check?"**

No. Guardrails and prompt checks are triggered by the content of user input — they ask whether a request is safe to process. This architecture's Level 2 is triggered by the classified environmental state S = f(E). It asks what the AI is permitted to recommend given current physical conditions. A perfectly safe, well-formed user request will still be scope-restricted if S = CAUTION — not because the question is inappropriate, but because the environment makes certain recommendation types unreliable. These are formally different governance mechanisms with different triggers, different inputs, and different purposes.

**"Doesn't the literature already have graduated governance?"**

The literature uses the term "graduated safety architecture" to mean layered independent safeguarding mechanisms — multiple defence layers compensating for each other's failures. This is graduated in the sense of "multiple safety layers," not graduated in the sense of "advisory scope formally contracts across defined safety states." No paper in the reviewed literature defines A_AI(S) as a function of classified environmental state S with a formal containment hierarchy. The novelty is in the definition, not just the existence of the concept.

**"The second level doesn't exist anywhere in the literature"**

The precise claim is: the systematic literature review conducted for this dissertation — covering 79 primary papers, four independent systematic reviews used as gap confirmations, five targeted Scopus searches, and three book reviews — identified no architecture that implements A_AI(S) as a function of environmental safety state S in a DSS context, with the formal containment property A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅. The review methodology and corpus are documented in Chapter 2. If the examiner is aware of a specific paper that implements this, the reference is welcomed.

**"This is social science research"**

The domain is maritime fishing. The contribution is a formal governance architecture in computer science. The domain is where the problem comes from — the contribution is what was built to solve it. The architecture is defined by formal mathematical properties (participation constraint, advisory restriction constraint, Safety Dominance Property) using the same vocabulary and methods as the runtime assurance and formal methods literature confirmed by Scopus searches. None of these are social science concepts.

**"This is software development research"**

Software development research asks: "does this system work?" This research asks: "what formal architectural properties must a governance layer satisfy to guarantee safe AI advisory behaviour across graduated safety states?" The contribution is the formal architecture specification and its provable properties. Any software implementation would be a secondary instantiation of the formal specification, not the contribution itself.
