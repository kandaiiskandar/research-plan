# What Kind of Contribution Is This? Characterising the Two-Level Governance Architecture

**Document type**: Theoretical justification / argumentation note  
**For**: Chapter 1 (Introduction), Chapter 3 (Architecture Design), and viva preparation  
**Questions addressed**: Q5 — Is this an algorithm, a system, or a governance model? Q6 — Is this conceptual, architectural, or mathematical? Q7 — Where does this sit in the AI system stack? Q8 — Is this a DSS or a safety architecture?

---

## 1. The Core Claim

The proposed contribution is a **formal governance architecture** — a precisely specified architectural layer that governs AI participation and advisory scope at runtime, expressed through mathematical definitions and formal properties.

It is:
- **Architectural** in structure — it defines components (E, S, G(S), A_AI(S)), their relationships (S = f(E), AI(E) ⊆ A_AI(S)), and their layered composition (Environment → Governance → AI Reasoning)
- **Mathematical** in expression — the governance pair, containment property, and Safety Dominance Property are formally defined and provable
- **At the governance layer** of the AI system stack — between environmental sensing and AI reasoning, constraining the AI output space without performing AI reasoning itself

It is not an algorithm (it does not specify a computation procedure for generating recommendations), not a system implementation (it does not prescribe technology choices, programming languages, or deployment platforms), and not a purely conceptual framework (it has formal definitions, provable properties, and implementable specifications).

---

## 2. Why This Is Not an Algorithm

### 2.1 What an Algorithm Is

An algorithm is a finite, deterministic sequence of computational steps that transforms a specified input into a specified output. Algorithms solve specific computational problems: sorting, searching, optimising, classifying. In AI, algorithms include gradient descent, Monte Carlo tree search, Q-learning, attention mechanisms, and the training procedures for neural networks.

### 2.2 The Structural Difference

The proposed architecture does not specify how to compute recommendations. It specifies the *constraints* within which any recommendation algorithm must operate. The architecture is agnostic to the AI reasoning method: the AI component (Layer 3) could use rule-based expert systems, Bayesian networks, deep neural networks, reinforcement learning, or large language models — the governance layer operates identically regardless.

The formal pipeline E → S = f(E) → (G(S), A_AI(S)) → AI(E) defines:
- f(E): a classification function mapping environmental parameters to safety states — this is a specification, not a learning algorithm
- G(S): a participation gate — a binary function, not a computational procedure
- A_AI(S): an admissible recommendation space — a set definition, not an optimisation objective
- The Safety Dominance Property AI(E) ⊆ A_AI(S): a formal constraint on outputs, not a loss function

Punzi et al. (2024) [[notes]](../notes/AI%2C%20Meet%20Human-%20Learning%20Paradigms%20for%20Hybrid%20Decision-Making%20Systems.md), surveying hybrid decision-making systems, define their formal model in terms of machine predictor f, human predictor h, and rejection/deferral policy ρ_M. The focus is on optimising the prediction function — minimising system loss L across human and machine agents. The proposed architecture operates at a different level: it does not define or optimise a predictor; it defines the governance constraints within which any predictor must operate. The relationship between the proposed architecture and an AI algorithm is analogous to the relationship between a traffic regulation and a navigation algorithm — the regulation defines where you may drive; the algorithm determines the optimal route within those constraints.

Könighofer et al. (2025) [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md), in the shielding literature, make this distinction explicit: a shield is not an RL algorithm — it is a constraint mechanism computed from a formal specification that operates alongside the RL algorithm. The shield "maintains a clear separation between an agent's safety and performance." The proposed governance layer has the same structural relationship to the AI recommendation algorithm: it constrains, not computes.

### 2.3 Implication for the Contribution Claim

The contribution is not "a new algorithm for generating fishing recommendations." It is "a new architectural mechanism for governing what types of recommendations any AI algorithm is permitted to generate, conditioned on classified environmental safety state." This is a governance contribution, not an algorithmic one. The algorithms that operate within the governance constraints remain a separate, substitutable concern.

---

## 3. Why This Is Not a System Implementation

### 3.1 What a System Implementation Is

A system implementation is a concrete, deployable artefact: source code, configured infrastructure, trained models, and operational procedures sufficient for deployment in a specific context. System implementations make technology-specific choices: database systems, cloud platforms, sensor hardware, communication protocols, user interface frameworks, programming languages.

### 3.2 The Structural Difference

The proposed architecture specifies formal components and their relationships at a level of abstraction above implementation. Consider:

| Architectural specification | What implementation would add |
|---|---|
| E = {w, r, m, o, v, t} — environmental parameter vector | Specific sensors (Davis Vantage Pro2 weather station, Datawell DWR-G4 wave buoy), sampling rates, data protocols, failure handling |
| S = f(E) — classification function | Specific threshold values (wind > 25 knots → CAUTION), hysteresis parameters, sensor fusion algorithms |
| G(S) — participation gate | Software implementation of the gate logic, API design, system integration architecture |
| A_AI(S) — admissible recommendation space | Data structures representing recommendation types, runtime enforcement mechanism, logging and audit trail |
| AI(E) — recommendation generation | Trained model, inference engine, hardware requirements, latency constraints |

The architecture defines *what* the system must enforce (the governance pair, the containment property, the Safety Dominance Property). Implementation defines *how* the system enforces it (specific technologies, configurations, operational procedures).

Abella et al. (2025) [[notes]](../notes/SAFEXPLAIN-%20a%20Complete%20Approach%20Towards%20Trustworthy%20AI-Based%20Safety-Critical%20Systems.md) — SAFEXPLAIN illustrate the distinction from the other direction: their reference safety architecture includes diverse AI redundancy, a supervision function, hierarchical diagnostics, and a non-AI fallback subsystem — all specified at the architectural level. The SAFEXPLAIN project then implements this architecture across three specific domains (automotive, space, railway) with domain-specific technology choices. The architecture and implementation are separate contributions. The proposed work similarly contributes at the architectural level.

Castagnone & Nitti (2026 — SYNAPSE) further illustrate this: SYNAPSE is both an architecture (symbolic verification gates neural interpretation) and a system implementation (GPT-4 + OpenSees + specific prompt templates). The architectural contribution (deterministic-gates-neural) is separable from and more general than the system implementation. The proposed work contributes at the architecture level, as SYNAPSE's architectural principle does, without being tied to a specific implementation.

### 3.3 The Evaluation Implication

Because the contribution is architectural, not implementational, it is evaluated primarily through:
- Formal analysis (are the properties provable? is the containment hierarchy well-defined?)
- Comparative analysis (how does this architecture differ from prior architectures?)
- Demonstrative implementation (does a reference implementation exhibit the claimed properties?)
- Socio-technical evaluation (do users respond to CAUTION mode as the architecture predicts?)

This is distinct from evaluating a system implementation, which would be assessed primarily on operational metrics (latency, throughput, uptime, cost, scalability).

---

## 4. Why This Is Not Purely Conceptual

### 4.1 What a Purely Conceptual Contribution Is

A conceptual contribution proposes ideas, frameworks, or taxonomies at a level of abstraction that does not admit formal verification or direct implementation. Conceptual contributions organise thinking, establish vocabulary, and motivate research directions. They do not define formal objects with provable properties.

### 4.2 The Structural Difference

The proposed architecture is not a proposal that "AI governance should be graduated" or "DSS should restrict scope under elevated risk." These would be conceptual contributions — valuable but not formally testable. The proposed architecture defines:

- **Formal objects**: S ∈ {SAFE, CAUTION, UNSAFE}; A_AI(S) for each S; R = {Go, Delay, DepartureTime, Duration}
- **Formal functions**: S = f(E); G: S → {0, 1}
- **Formal properties**: A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅; AI(E) ⊆ A_AI(S)
- **A proof obligation**: the Safety Dominance Property is stated as a formal invariant that any correct implementation must satisfy

These are not aspirational statements. They are mathematical definitions with falsifiable content: a proposed implementation either satisfies the containment property or it does not; the Safety Dominance Property either holds or it does not.

The distinction is illustrated by comparing the proposed architecture with two conceptual frameworks in the corpus:

**Porter et al. (2025 — INSYTE)**: An eight-dimension classification framework for AI systems, rated 0–5 per dimension, visualised as a radar chart. INSYTE provides vocabulary for describing AI systems but does not define formal governance mechanisms. It classifies the degree of human control; it does not implement governance. The notes observe: "INSYTE is a classification framework, not a governance architecture. It provides a vocabulary for describing AI systems from the outside; it does not define how AI should be governed from the inside."

**Bello y Villarino et al. (2025)**: An analysis of AI regulatory frameworks against 163 real-world systems. The EU AI Act's binary scope test and the NSW AIAF's graduated risk scale provide conceptual governance categories — but neither constrains the type of AI output based on risk level. "Obligations are procedural (assessment, documentation, monitoring, committee review) and apply uniformly to all in-scope systems."

The proposed architecture crosses from conceptual to formal at the point where it defines objects with provable properties and specifies the proof obligations that any implementation must satisfy. It is more than conceptual, less than a system implementation — it occupies the architectural-formal middle ground.

### 4.3 Comparison with Baxi (2026) [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md)

Baxi (2026) [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) — CGAE provides the strongest prior example of the same type of contribution: a formal governance architecture with proved theorems (Theorem 3: bounded economic exposure; Theorem 5: incentive-compatible robustness investment; Theorem 6: monotonic safety scaling). CGAE is not conceptual — it defines formal objects and proves properties about them. It is not a system implementation — no deployed platform is presented. It is an architectural-formal contribution, the same type as the proposed work. The structural parallel confirms the contribution type; the orthogonal conditioning variable (agent robustness vs. environmental state) and domain (economic vs. physical safety) confirm the novelty.

---

## 5. Why This Is Not Either/Or: DSS vs. Safety Architecture

### 5.1 The False Dichotomy

An examiner might ask: "Is this a decision support system or a safety architecture?" The question assumes mutual exclusivity. The proposed architecture is both, operating at different layers.

### 5.2 The Dual Nature

At Layer 3 (AI Reasoning), the architecture is a **decision support system**: it generates recommendations (go/no-go, departure time, trip duration, fishing area) to inform a human decision-maker who retains full decision authority. The fisher is always the decision-maker. The AI is always advisory. This is standard DSS.

At Layer 2 (Governance), the architecture is a **safety architecture**: it classifies environmental conditions, determines AI participation, and restricts AI advisory scope based on classified safety state. The governance layer enforces formal safety properties (the containment hierarchy, the Safety Dominance Property). This is safety engineering.

The relationship between the two layers is the contribution. No prior DSS has a governance layer that restricts recommendation types by classified environmental state. No prior safety architecture governs AI advisory scope (as opposed to participation or output correctness).

### 5.3 Where in the AI System Stack

The contribution sits specifically at the **governance layer** — between environmental sensing and AI reasoning:

```
┌─────────────────────────────────┐
│  Layer 3: AI Reasoning Layer    │  ← Generates recommendations
│  (Probabilistic, learned)       │  ← AI(E) ⊆ A_AI(S)
├─────────────────────────────────┤
│  Layer 2: Governance Layer      │  ← THE CONTRIBUTION
│  (Deterministic, rule-based)    │  ← S = f(E) → (G(S), A_AI(S))
├─────────────────────────────────┤
│  Layer 1: Environment/Sensor    │  ← Observable parameters
│  (Physical, measurable)         │  ← E = {w, r, m, o, v, t}
└─────────────────────────────────┘
```

This stack position is significant. The governance layer is:

1. **Below** the AI reasoning layer — it constrains AI from below, not from within. The AI does not govern itself. Bloomfield & Rushby (2025) [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md) identify this as the defining property of assuredly guarded systems: "assuredly guarded systems" are those whose guards "do not themselves use AI/ML and can therefore be assured conventionally."

2. **Above** the sensor layer — it interprets physical measurements into governance decisions. It is not a raw sensor interface but a classification and governance function.

3. **Deterministic while the layer above is probabilistic** — this asymmetry is the formal basis for the Safety Dominance Property proof. Because f(E) is deterministic, the containment hierarchy A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ ∅ holds as a formal invariant, not a statistical expectation.

4. **Independent of the AI layer** — governance functions even if the AI model is unavailable, degraded, or adversarial. The governance layer receives inputs from sensors (Layer 1) and provides constraints to the AI (Layer 3) but receives no inputs from the AI. This unidirectional dependency is the architectural guarantee of governance integrity.

Flehmig et al. (2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md) implement a conceptually similar stack position: their non-AI monitoring and supervisory components sit between the AI component and the system output, monitoring AI quality independently. But their monitoring layer observes AI performance — it depends on AI outputs as inputs. The proposed governance layer does not — it depends only on environmental sensors. This makes the governance layer fully independent of the governed system, satisfying the independence requirement that Dalrymple et al. (2024) [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md), Bajcsy & Fisac (2024) [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md), and Könighofer et al. (2025) [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md) all specify as necessary for formal safety guarantees.

---

## 6. Comparative Summary Table

| Characterisation | Describes the proposed contribution? | Why or why not |
|---|---|---|
| **Algorithm** | No | Does not specify a computation procedure for generating recommendations; specifies constraints within which any algorithm operates |
| **System implementation** | No | Does not prescribe technology choices, sensor hardware, or deployment configuration; specifies architectural components and their relationships |
| **Conceptual framework** | Partially — but insufficient | Proposes ideas and organises thinking, but also defines formal objects with provable properties, which goes beyond conceptual |
| **Governance model** | Partially — but insufficient | Defines governance rules, but also specifies architectural structure and formal properties, which goes beyond a policy model |
| **Formal governance architecture** | **Yes** | Defines architectural components (E, S, G(S), A_AI(S)), formal relationships (S = f(E), AI(E) ⊆ A_AI(S)), provable properties (containment, Safety Dominance), and layered composition — architectural in structure, mathematical in expression |
| **DSS** | At Layer 3 only | The AI reasoning layer generates advisory recommendations; but the contribution is at Layer 2, not Layer 3 |
| **Safety architecture** | At Layer 2 only | The governance layer enforces safety properties; but it governs a DSS, not a control system |
| **Both DSS and safety architecture** | **Yes — at different layers** | Layer 3 is DSS; Layer 2 is safety architecture; their integration is the contribution |

---

## 7. One-Paragraph Summary (for use in Chapter 1 or Chapter 3)

> The proposed contribution is a formal governance architecture — architectural in structure, mathematical in expression, positioned at the governance layer of the AI system stack between environmental sensing and AI reasoning. It is not an algorithm: it does not specify how recommendations are computed but constrains the space within which any recommendation algorithm must operate, analogous to the relationship between a shield and an RL agent (Könighofer et al., 2025) [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md). It is not a system implementation: it defines components and their formal relationships at a level of abstraction above technology choices, as SAFEXPLAIN (Abella et al., 2025) [[notes]](../notes/SAFEXPLAIN-%20a%20Complete%20Approach%20Towards%20Trustworthy%20AI-Based%20Safety-Critical%20Systems.md) defines a reference safety architecture separable from its domain-specific implementations. It is not purely conceptual: unlike classification frameworks (Porter et al., 2025 — INSYTE) or regulatory analysis (Bello y Villarino et al., 2025), it defines formal objects (S ∈ {SAFE, CAUTION, UNSAFE}; A_AI(S); G(S)), formal functions (S = f(E)), and provable properties (containment hierarchy, Safety Dominance Property) — the same type of contribution as Baxi's (2026) [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) CGAE, which proves analogous theorems for an orthogonally conditioned governance architecture. The architecture is simultaneously a decision support system (at Layer 3, where AI generates advisory recommendations) and a safety architecture (at Layer 2, where governance enforces formal safety properties), with the contribution located specifically at the governance layer — deterministic, independent of the AI it governs (Bloomfield & Rushby, 2025) [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md), receiving inputs only from environmental sensors, and providing constraints to the AI layer through the state-conditioned governance pair (G(S), A_AI(S)). This stack position — below AI reasoning, above sensing, deterministic while the layer above is probabilistic — is the formal basis for the Safety Dominance Property proof and the architectural guarantee that governance integrity does not depend on the correctness of the AI component it constrains.
