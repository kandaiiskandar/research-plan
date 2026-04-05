## Literature Review Extraction: Liang et al. (2025)

---

### 1. Paper Identity

- **Title:** Safeguarded AI-Driven Semantic Communication: Design Principles, Architecture, and Challenges
- **Authors:** Chengsi Liang, Yao Sun, Dongzhu Liu, Dahui Yu, Muhammad Ali Imran
- **Year:** 2025 (published September 2025)
- **Venue:** IEEE Communications Standards Magazine, December 2025, pp. 41–49
- **DOI:** 10.1109/MCOMSTD.2025.3602816
- **Type:** Framework/architecture paper with simulation-based case study

---

### 2. Core Contribution

- **Problem:** AI models in semantic communication (SemCom) networks for 6G are safety-critical but operate on a "best effort" basis — producing outputs regardless of reliability, exhibiting overconfidence (high confidence scores for incorrect outputs), and lacking generalisation to changing network conditions and knowledge bases. No existing work applies safeguarded AI to SemCom networks.
- **Solution:** A safeguarded AI framework for SemCom networks with three core components: (1) **world model** — mathematical/logical representation of operational environment, (2) **safety specifications** — formal conditions defining safe operation (KB alignment thresholds, semantic effectiveness, semantic QoS, Age of Information), and (3) **gatekeepers** — external oversight modules that enforce safety constraints on AI outputs by filtering outputs falling outside defined safety boundaries before they reach the application operator.
- **Main contributions:**
  - Architecture design for safeguarded AI in SemCom: world model → safety specifications → gatekeeper pipeline
  - Four gatekeeper implementation techniques: simple threshold filtering, random smoothing, conformal prediction (with formal coverage guarantee P(true output ∈ predicted set) ≥ 1 − α), and Monte Carlo dropout for uncertainty estimation
  - Simulation case study showing 54% BLEU score improvement at 0 dB SNR versus baseline DeepSC when gatekeeper threshold τ = 0.7
  - Identification of trade-off: higher safety thresholds improve accuracy but increase failure rate (more outputs filtered out)
- **Novelty:** First application of the safeguarded AI framework (building on Dalrymple et al. [2024]) to semantic communication networks. The gatekeeper is positioned as an external, model-agnostic safety layer — it controls and validates AI outputs rather than modifying internal model architectures.

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | Partial | The architecture separates a deterministic safety layer (gatekeeper with predefined thresholds/specifications) from probabilistic AI models (neural semantic encoder/decoder). However, the "hybrid" is safety overlay + AI model, not integrated rule-based + probabilistic reasoning within a decision pipeline |
| Safety-critical AI decision-making | Yes | Explicitly frames SemCom as safety-critical (enabling power grids, transportation, autonomous vehicles, industrial automation). Safety is the core design concern — AI outputs must be constrained to prevent unsafe transmission |
| AI governance / control mechanisms | Yes | Gatekeepers implement explicit governance over AI output. The gatekeeper is positioned between AI model output and the application operator, filtering outputs that fall outside safety boundaries. This is a clear AI output governance mechanism |
| Low-resource environments | No | Framework targets 6G communication infrastructure — high-resource, high-bandwidth context |
| Decision architecture formalisation | Partial | Architecture is described with components (world model, safety specifications, gatekeeper) and formal elements (conformal prediction guarantee, Bayesian networks, Markov chains for world modelling). However, the governance is not formalised as a state-classified pipeline with explicit gate function and admissible action space notation |
| Human role in decision-making | Partial | Users (domain experts) monitor outcomes post-execution and provide feedback to gatekeepers. An "application operator" executes approved actions. However, the human role is feedback-based, not decision-authority-based |
| Socio-technical evaluation | No | Evaluation is simulation-only (BLEU scores, failure rates). No stakeholder involvement or socio-technical assessment |
| Coastal fisheries / maritime domain | No | Telecommunications / 6G communication domain |

**Mid-Extraction Relevance Gate:** 2 Yes, 3 Partial → **REDUCED EXTRACTION** (Sections 4–7, 12–13, 16–17)

---

### 4. Decision Architecture Analysis

- **Architecture:** Three-component pipeline: **World Model** (environmental representation) → **Safety Specifications** (derived from world model) → **Gatekeeper** (enforces specifications on AI output) → **Application Operator** → **Users** (feedback loop). AI models operate *within* the world model and produce outputs that are *intercepted* by the gatekeeper before reaching the operator.
- **Layered structure:** Yes — the architecture explicitly separates: (a) the AI model layer (semantic encoder/decoder producing outputs), (b) the safety specification layer (defining what constitutes safe output), and (c) the gatekeeper enforcement layer (filtering unsafe outputs). This is a three-layer safety architecture.
- **Rule-based constraints before AI:** The gatekeeper operates *after* AI output, not before. It is a post-hoc filter, not a pre-AI gate. The simple threshold filter is deterministic; conformal prediction and random smoothing provide probabilistic guarantees. The gatekeeper does not prevent AI from operating — it filters AI's output.
- **Boundary between deterministic control and AI reasoning:** Clearly defined. The AI model operates freely within the world model. The gatekeeper then applies deterministic or formally guaranteed constraints to the AI's output. The key architectural principle is that the gatekeeper is *external* to the AI model — it does not modify internal architecture or training.
- **Failure modes / fallback:** Explicitly addressed through the failure rate analysis (Fig. 5). When the gatekeeper filters out unsafe outputs, this results in data reconstruction failure — a known and measured trade-off. The paper notes that the gatekeeper can "dynamically adjust the threshold based on channel conditions and user requirements" to balance accuracy vs. failure rate.

**Critical architectural comparison to my research:**

| Aspect | Liang et al. (2025) | My DSR Architecture |
|---|---|---|
| **What triggers governance** | AI output quality (post-hoc evaluation against safety specifications) | Environmental safety state classification S = f(E) (pre-decision) |
| **When governance acts** | After AI produces output (output filtering) | Before and during AI operation (participation gating + scope restriction) |
| **Governance mechanism** | Gatekeeper filters individual outputs below threshold | Two-level pair: G(S) gates AI participation; A_AI(S) restricts advisory scope |
| **Governance granularity** | Binary per-output: pass or reject | Three-state: SAFE (full scope), CAUTION (restricted scope), UNSAFE (AI blocked) |
| **State conditioning** | Threshold can be adjusted by channel conditions (mentioned but not formalised) | Formally state-conditioned: governance pair (G(S), A_AI(S)) is a function of classified environmental state S |

---

### 5. Formal Model and Mathematical Representation

- **Formal elements present:**
  - Bayesian network joint probability: P(V) = ∏_{v∈V} P(v | Pa(v))
  - Markov chain state transitions with transition probabilities p_ij
  - Structural Causal Model: M(U,V,F,P(U)) with V_i = f_i(Pa(V_i), U_i)
  - RL state transition function: s_{t+1} = f(s_t, a_t) and reward function r_t = g(s_t, a_t)
  - Conformal prediction guarantee: P(true output ∈ predicted set) ≥ 1 − α
  - Game-theoretic strategy profiles and Nash equilibrium
- **Comparison to DSR pipeline:** The paper's architecture (World Model → Safety Specifications → Gatekeeper → Operator) is structurally adjacent to my E → S = f(E) → (G(S), A_AI(S)) → AI(E), but with critical differences:
  - The world model captures environmental dynamics but does not *classify* them into discrete safety states
  - Safety specifications define acceptable operating ranges but are not organised as a state-conditioned governance pair
  - The gatekeeper filters per-output, not per-safety-state — it does not define an admissible action space A_AI(S) that varies by classified state
- **State-dependent recommendation restriction:** Not formally implemented. The gatekeeper uses a fixed threshold τ (tested at 0.5, 0.6, 0.7). The paper mentions dynamic threshold adjustment based on channel conditions as a possibility but does not formalise or implement it as state-conditioned governance.
- **Safety Dominance Property equivalent:** The conformal prediction guarantee (P(true output ∈ predicted set) ≥ 1 − α) is a formal safety property — it provides a probabilistic bound on output correctness. However, it operates per-output (bounding individual prediction reliability) rather than per-state (bounding AI's admissible action space). It is a **coverage guarantee**, not a **containment guarantee** like AI(E) ⊆ A_AI(S).
- **Formalisation purpose:** The formal elements serve world model construction and gatekeeper implementation (operational use), not architectural governance proof. The conformal prediction guarantee is the closest to a formal safety property.

---

### 6. Safety State Classification

- **Discrete safety levels:** Not defined as discrete classified states. The world model captures continuous environmental dynamics (channel conditions, KB states, resource allocation) but does not classify them into discrete safety levels like {SAFE, CAUTION, UNSAFE}.
- **Comparison to S = f(E):** The world model plays the role of E (environmental representation), and safety specifications partially play the role of constraints. However, there is no classification function f(E) → S that maps continuous environmental state to discrete safety categories. Governance is per-output-threshold, not per-classified-state.
- **AI recommendation scope differentiation across safety levels:** Not implemented. The gatekeeper applies the same governance logic (threshold filtering) regardless of environmental state. The AI always generates full output; the gatekeeper either passes or rejects each output. There is no CAUTION-equivalent mode where AI operates with restricted scope.

**Key gap observation:** The paper's architecture has the *components* needed for state-conditioned governance (world model, safety specifications, gatekeeper) but does not *organise* them into a state-classified, scope-graduated governance pipeline. The gatekeeper is a binary per-output filter (pass/reject), not a state-conditioned scope restrictor.

---

### 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (G(S)) | Partial | The gatekeeper can reject AI outputs, effectively blocking AI from influencing the operator for individual outputs. However, this is per-output rejection, not state-level AI disengagement. AI always runs; only individual outputs are filtered |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | No | AI always generates full-scope output. The gatekeeper does not restrict what *types* of output AI may produce — it evaluates quality of whatever AI produces and passes/rejects the whole output |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | No | No state classification function. Gatekeeper threshold is fixed (though dynamic adjustment is mentioned as future possibility) |

- **Governance type:** **Single-level, per-output binary filtering.** The gatekeeper implements a binary pass/reject decision on each AI output based on a quality threshold. This is Level 1 governance at the output level — not at the system participation level (AI never stops operating) and not at the scope level (AI output types are never restricted).
- **Binary switch or graduated governance:** Binary per-output (pass or reject). No graduated governance across safety states. The different threshold values (τ = 0.5, 0.6, 0.7) represent different *strictness levels*, not different *governance modes conditioned on environmental state*.
- **Relation to two-level governance pair:** The paper's gatekeeper is structurally analogous to G(S) operating at the output level — it determines whether a specific AI output proceeds. However, it lacks:
  - State classification: no S = f(E) to determine governance mode
  - Scope governance: no A_AI(S) restricting output types by state
  - Graduated governance: no CAUTION mode with restricted but non-empty advisory scope
  - State conditioning: threshold is static per deployment, not dynamically mapped to classified environmental state

This paper represents the **strongest articulation of per-output binary gatekeeper governance** in a safety-critical AI context, building directly on Dalrymple et al. (2024). It confirms the binary gatekeeper paradigm while leaving the graduated, state-conditioned governance gap that my architecture fills.

---

### 12. Key Concepts and Definitions

- **Safeguarded AI:** Framework ensuring AI systems operate under strict safety protocols through external oversight mechanisms (gatekeepers) that provide mathematical guarantees for keeping AI outputs within proven safety boundaries. Distinguished from broader AI safety by emphasis on formal verification over empirical testing. (Building on Dalrymple et al. 2024.)
- **Gatekeeper:** External module positioned between AI model output and application operator. Performs independent safety assessments using separate safety criteria (not relying on AI's internal confidence scores). Four implementation techniques: simple threshold filter, random smoothing, conformal prediction, Monte Carlo dropout.
- **World model:** Mathematical and logical representation of real-world dynamics, establishing the formal foundation for safety verification. Transforms abstract safety concepts into verifiable constraints (mathematical inequalities and logical predicates over defined model states).
- **Safety specifications:** Formal criteria defining safe operating conditions, including: KB alignment thresholds, semantic effectiveness metrics, semantic quality of service (S-QoS), and Age of Information/Incorrect Information (AoI/AoII).
- **Conformal prediction:** Method transforming AI output into prediction sets with formal coverage guarantee P(true output ∈ predicted set) ≥ 1 − α. When uncertain, the prediction set enlarges or returns no prediction — preventing overconfident unsafe outputs.
- **Accuracy-failure trade-off:** Higher safety thresholds improve output quality but increase the proportion of outputs rejected by the gatekeeper (failure rate). At τ = 0.7: highest BLEU scores but also highest failure rates, especially at low SNR.

---

### 13. Limitations and Unsolved Problems

- **Stated limitations:**
  - Lack of standardised SemCom frameworks — no universal safety properties or verification methodologies across implementations
  - Resource costs — gatekeepers introduce computational overhead (recursive challenge: safety mechanisms require resources to monitor resource-constrained AI models)
  - Gatekeeper threshold is static per deployment — dynamic adjustment mentioned but not formalised or implemented
- **Observable limitations:**
  - Per-output binary governance only — no graduated governance across safety states
  - No state classification function — environmental dynamics are captured by the world model but not classified into discrete safety levels
  - No scope governance — AI always generates full output; gatekeeper only passes/rejects, never restricts output types
  - Simulation-only evaluation — no real-world deployment or field testing
  - Domain-specific to 6G semantic communication — transferability to other safety-critical domains unclear
- **Alignment with my research gaps:**
  - **Binary gatekeeper paradigm confirmed:** The paper implements exactly the per-output pass/reject governance that characterises the existing binary paradigm. The gatekeeper is structurally equivalent to G(S) ∈ {0, 1} at the output level — no intermediate mode.
  - **No CAUTION mode:** The paper has no equivalent to A_AI(CAUTION) ⊂ A_AI(SAFE). When the gatekeeper rejects output, the system fails (no output at all), rather than providing restricted-scope output. The choice is full output or no output.
  - **No state-conditioned governance:** The threshold τ is fixed, not dynamically conditioned on classified environmental state. The paper *mentions* dynamic threshold adjustment as a possibility but does not formalise it.
  - **No Safety Dominance Property for graduated governance:** The conformal prediction guarantee is per-output coverage, not per-state containment. No property ensuring AI(E) ⊆ A_AI(S) across a graduated governance model.

---

### 16. Relation to My Research and Positioning

- **Governance implementation:** Level 1 (partial) — per-output binary filtering via gatekeeper. No Level 2 (scope governance).
- **State conditioning:** Not implemented. Threshold is static.
- **Two-level governance pair:** The paper has the architectural *ingredients* (world model → safety specifications → gatekeeper) but does not organise them into a state-conditioned governance pair (G(S), A_AI(S)).
- **Safety property:** Conformal prediction coverage guarantee (per-output), not Safety Dominance Property (per-state containment).
- **Gap my research addresses:** Liang et al. demonstrate that even in an architecture explicitly designed for safeguarded AI — with world model, safety specifications, and gatekeepers — the governance defaults to binary per-output filtering. The gatekeeper either passes or rejects; there is no intermediate mode where AI continues to operate under restricted scope. My architecture fills this gap by introducing: (a) state classification S = f(E) that organises continuous environmental dynamics into discrete governance modes, (b) two-level governance (G(S), A_AI(S)) that separates participation from scope, and (c) a CAUTION state where G(S) = 1 but A_AI(CAUTION) ⊂ A_AI(SAFE) — enabling restricted-scope AI output rather than binary pass/reject.

**Positioning paragraph:** Liang et al. (2025) is a **significant cross-domain reference for the AI governance mechanism theme**, directly extending the Dalrymple et al. (2024) guaranteed safe AI framework into a concrete safety-critical application domain (6G semantic communication). The paper's gatekeeper architecture — world model → safety specifications → per-output filtering — represents the current state of the art in safeguarded AI implementation: an external, model-agnostic safety layer that provides formal guarantees (conformal prediction) on individual AI outputs. Critically, this implementation confirms the binary governance paradigm identified across other domains: the gatekeeper operates as a pass/reject filter on AI outputs, with no intermediate mode where AI continues under restricted scope. The accuracy-failure trade-off documented in their results (higher thresholds → better quality but more rejected outputs) empirically demonstrates the cost of binary governance — precisely the problem my CAUTION state addresses by enabling restricted-scope AI output rather than outright rejection. This paper should be cited as: (a) a concrete implementation of the Dalrymple et al. guaranteed safe AI framework in a safety-critical domain, confirming the binary gatekeeper paradigm, (b) empirical evidence of the accuracy-failure trade-off inherent in binary pass/reject governance, and (c) a close architectural antecedent that has the components (world model, safety specifications, gatekeeper) but not the state-conditioned graduated governance that my architecture provides.

---

### 17. Overall Relevance Score

**⭐⭐⭐⭐ High**

**Justification:** This paper directly addresses two core themes (safety-critical AI governance, AI governance mechanisms) and partially addresses three more (hybrid architecture, decision architecture formalisation, human role). It implements the Dalrymple et al. safeguarded AI framework in a concrete safety-critical domain, providing the clearest available example of how the binary gatekeeper paradigm operates in practice — and where it falls short (no graduated governance, no state conditioning, binary pass/reject trade-off). The gatekeeper architecture (world model → safety specifications → filtering) is structurally adjacent to my pipeline (E → S = f(E) → (G(S), A_AI(S)) → AI(E)), making the comparison precise and constructive. The paper's documented accuracy-failure trade-off provides empirical motivation for the CAUTION state. Elevated to ⭐⭐⭐⭐ because it serves as a cross-domain baseline confirming the binary governance gap while providing architectural vocabulary (gatekeeper, safety specifications, world model) that aligns with my framework's components.

---

### Recommended Citation Uses

| Use | Section in dissertation | Specific point |
|---|---|---|
| Binary governance gap evidence (cross-domain) | Research gap section | Concrete implementation of Dalrymple et al. framework defaults to per-output binary pass/reject — no graduated governance even with world model, safety specifications, and gatekeeper components |
| Accuracy-failure trade-off of binary governance | Motivation for CAUTION state | Higher gatekeeper threshold → better output quality but higher failure rate. Binary pass/reject forces choice between safety and availability; CAUTION state resolves this |
| Gatekeeper as Level 1 governance baseline | Architecture comparison / baseline | Gatekeeper = external post-hoc filter on AI output = Level 1 per-output governance. Structural comparison to G(S) |
| Safeguarded AI architectural vocabulary | Architecture design rationale | World model, safety specifications, gatekeeper terminology aligns with my E, S = f(E), (G(S), A_AI(S)) components — enables precise cross-framework comparison |
| Conformal prediction as per-output safety property | Formalisation comparison | Coverage guarantee P(true ∈ set) ≥ 1 − α contrasts with Safety Dominance Property AI(E) ⊆ A_AI(S) — per-output vs. per-state safety guarantee |
| Dynamic threshold adjustment as unrealised potential | Future work / gap identification | Paper mentions but does not formalise state-conditioned threshold adjustment — exactly the formalisation my architecture provides |
