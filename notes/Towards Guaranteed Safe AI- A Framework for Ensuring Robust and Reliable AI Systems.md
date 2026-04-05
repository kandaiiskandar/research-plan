## Literature Review Extraction
### Dalrymple, Skalse, Bengio, Russell, Tegmark, Seshia, Omohundro, Szegedy et al. (2024) — Towards Guaranteed Safe AI: A Framework for Ensuring Robust and Reliable AI Systems

---

### 1. Paper Identity
- **Title:** Towards Guaranteed Safe AI: A Framework for Ensuring Robust and Reliable AI Systems
- **Authors:** David "davidad" Dalrymple, Joar Skalse, Yoshua Bengio, Stuart Russell, Max Tegmark, Sanjit Seshia, Steve Omohundro, Christian Szegedy, Ben Goldhaber, Nora Ammann, Alessandro Abate, Joseph Y. Halpern, Clark Barrett, Ding Zhao, Tan Zhi-Xuan, Jeannette Wing, Joshua B. Tenenbaum
- **Year:** 2024 (arXiv:2405.06624v3, 8 Jul 2024)
- **Venue:** arXiv preprint (position paper); authors affiliated with UK ARIA, Oxford, Mila/Montreal, UC Berkeley, MIT, Stanford, CMU, Columbia, Cornell, x.AI, FAR AI
- **DOI:** arXiv:2405.06624
- **Type:** Position paper / conceptual framework with formal definitions

---

### 2. Core Contribution
- **Problem:** AI systems in safety-critical contexts require high-assurance quantitative safety guarantees. Empirical evaluations (red-teaming, testing) are fundamentally insufficient — they cannot rule out deceptive alignment, cryptographic backdoors, or long-horizon distributional shift. Current XAI and alignment approaches do not provide verifiable guarantees.
- **Solution:** A family of approaches called **Guaranteed Safe (GS) AI**, defined by three core components: (1) a **world model** providing a mathematical description of how the AI affects the world, handling both Bayesian and Knightian uncertainty; (2) a **safety specification** describing mathematically what effects are acceptable; (3) a **verifier** producing an auditable proof certificate that the AI satisfies the specification relative to the world model.
- **Main contributions:**
  - Formal definition of GS AI (Definition 3.1 and Appendix B)
  - Multi-level spectra for each component: world models (W0–W5), safety specifications (S0–S7), and verifiers (V0–V10)
  - Concrete examples of GS AI applications (code translation, autonomous vehicles, household robots, medical diagnosis, compute centre management, cyber defence, nucleic acid screening, climate stabilisation)
  - Argument for necessity of this approach vs. empirical-only methods
  - Integration of multiple existing research agendas under one umbrella
- **Novelty:** Not claiming novelty of the three-component architecture per se (traces back to Newell & Simon's GPS, 1961), but identifying convergence between several existing approaches (Szegedy 2020, Wing 2021, Seshia et al. 2022, Russell 2022, Tegmark & Omohundro 2023, Dalrymple 2024, Bengio 2024) and providing a unified taxonomy and research agenda.

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | **Yes** | The GS framework is inherently hybrid: a formal verifier (rule-based, deterministic) constrains a potentially black-box AI system (probabilistic). The verifier gates AI output based on formal proof certificates. |
| Safety-critical AI decision-making | **Yes** | Core topic — the paper argues that safety-critical AI requires verifiable quantitative safety guarantees, not just empirical testing |
| AI governance / control mechanisms | **Yes** | The three-component architecture (world model + safety specification + verifier) is a governance architecture: the verifier acts as a gate that prevents unsafe AI outputs from reaching the world. The "deployment infrastructure" section discusses runtime monitoring and backup systems. |
| Low-resource environments | No | Not addressed — the paper focuses on frontier AI and high-capability systems (ASL-3+) |
| Decision architecture formalisation | **Yes** | Formal definition provided (Definition B.1): policy π, world model m, safety specification ψ, verifier Vψ. The GS AI system is formally a tuple ⟨π, m, ψ, Vψ⟩ |
| Human role in decision-making | **Partial** | Discusses democratic oversight through auditable specifications; CIRL (Cooperative Inverse Reinforcement Learning) for human-AI cooperation; human-in-the-loop for specification creation. But the framework primarily concerns autonomous AI systems. |
| Socio-technical evaluation | **Partial** | Discusses societal risk criteria, democratic oversight, multi-stakeholder coordination through proof certificates. But does not perform socio-technical evaluation. |
| Coastal fisheries / maritime domain | No | Not addressed |

**Mid-Extraction Relevance Gate:** 4 Yes + 2 Partial → **FULL EXTRACTION**

---

### 4. Decision Architecture Analysis
- **Structure:** The GS AI architecture is a **gate-verify-deploy** pipeline: AI produces output → verifier checks output against safety specification using world model → only verified-safe output reaches the world (Figure 1).
- **Layered architecture:** The three components form a layered governance structure:
  - **World model** provides the environmental state representation
  - **Safety specification** defines what is acceptable
  - **Verifier** provides the enforcement mechanism (gate)
  - **Deployment infrastructure** provides runtime monitoring and backup
- **Safety constraint mechanism:** The verifier is the central safety gate. It produces a quantitative guarantee (proof certificate, probabilistic bound, or asymptotic guarantee) that the AI's output satisfies the specification relative to the world model. The AI system's output is only deployed if this guarantee meets the required threshold.
- **Boundary between deterministic control and AI reasoning:** Clearly defined — the AI system (policy π) can be any black box (including neural networks); the verifier and safety specification are the deterministic/formal layer that constrains it. The paper is explicitly agnostic about how the AI system is produced.
- **Failure modes and fallback:** Discussed in Section 5 (deployment infrastructure). If runtime monitoring detects that the world model is inaccurate, the AI system should be disabled and a trustworthy backup system should safely transition to a safe state. The paper notes that for safety-critical systems (e.g., self-driving cars), simply shutting down may not be safe — hence the need for backup systems.
- **Time horizon modulation:** The deployment infrastructure can modulate the time horizon at which verified AI output is deployed, reducing verification complexity.

---

### 5. Formal Model and Mathematical Representation
- **Formal definition (Appendix B, Definition B.1):**
  - **A** = set of actions, **S** = set of world states, **O** = set of observations
  - **Policy:** π : (O × A)* × O → Δ(A) — returns distribution over actions given observation-action history
  - **World model:** m : S × A → P(Δ(O × S)) — returns a set of probability distributions (credal set) over next states and observations, given current state and action
  - **Safety specification:** ψ : Π × M → [0, 1] — maps policy-model pairs to a safety value
  - **Verifier:** Vψ : Π × M → P([0, 1]) — computes or estimates ψ(π, m)
  - **GS AI system:** Tuple ⟨π, m, ψ, Vψ⟩ where Vψ(π, m) lies in some permissible set

- **Comparison to DSR pipeline E → S = f(E) → (G(S), A_AI(S)) → AI(E):**

  | GS AI Component | DSR Pipeline Element | Comparison |
  |---|---|---|
  | World model m | Environmental state vector E | Both represent the environmental/world state. But m is a full dynamics model (S × A → distributions over next states); E is a classification input vector. GS AI models how actions affect the world; my E captures the current environmental state for safety classification. |
  | Safety specification ψ | Safety state S = f(E) + governance pair (G(S), A_AI(S)) | Both define what is acceptable. But ψ maps (policy, model) → [0,1] as a continuous safety value; my f(E) classifies into discrete states {SAFE, CAUTION, UNSAFE} that then determine discrete governance pairs. GS AI uses continuous verification; my architecture uses discrete state-conditioned governance. |
  | Verifier Vψ | Gate function G(S) | Both serve as enforcement mechanisms. But Vψ verifies the entire policy against the specification relative to the world model (static or runtime); G(S) gates AI participation at runtime based on classified safety state. GS AI verifies the policy as a whole; my G(S) gates individual interactions. |
  | Policy π | AI(E) | Both represent the AI's output. But π is the entire policy function; AI(E) is the AI's recommendation for a specific environmental state, constrained to A_AI(S). |

- **State-dependent recommendation restriction:** The GS AI framework does not implement discrete state-dependent recommendation restriction. The safety specification ψ operates on the entire policy-model pair, not on individual states. There is no analogue of A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ — the graduated restriction of advisory scope across classified safety states.

- **Safety Dominance Property comparison:** The GS AI framework provides a stronger but different guarantee: Vψ(π, m) ∈ permissible set, meaning the entire policy is verified against the specification relative to the world model. My Safety Dominance Property (AI(E) ⊆ A_AI(S)) is a per-state guarantee that each AI recommendation falls within the admissible set determined by the current safety state. The GS approach verifies the policy globally; my property constrains outputs locally per classified state.

- **Formalisation purpose:** The formalisation is used for **defining a research agenda** and **positioning existing approaches** on spectra. The concrete examples (Section 4) show how the framework would be applied, but no empirical evaluation is performed.

---

### 6. Safety State Classification
- **No discrete safety state classification.** The GS AI framework does not classify environmental conditions into discrete safety levels (SAFE/CAUTION/UNSAFE). Safety is assessed as a continuous value ψ(π, m) ∈ [0, 1] over the entire policy-model pair.
- **ASL classification (Section 2.2):** The paper adopts Anthropic's AI Safety Levels (ASL-1 through ASL-5+) to classify AI systems by capability level and risk. This is a system-capability classification, not an environmental-state classification.
- **Runtime monitoring:** The deployment infrastructure can detect when the world model is inaccurate and disable the AI, but this is a binary response (continue/disable), not a graduated response across classified environmental states.
- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:** The GS framework operates at a different granularity. My f(E) classifies the current environmental state at runtime into one of three discrete levels, determining what the AI may recommend. The GS framework verifies the entire policy against the entire specification before or during deployment. There is no intermediate CAUTION mode where AI participates with restricted scope — the verification either passes (AI operates) or fails (AI is disabled/backed up).

---

### 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (G(S)) | **Yes** | The verifier gates whether the AI's output reaches the world. If verification fails, the AI is disabled and a backup system takes over. Runtime monitoring can also disable the AI if the world model is found inaccurate. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | **Partial** | The safety specification constrains what the AI may do (ψ defines acceptable behaviour). But this constraint is applied globally to the entire policy, not as a state-conditioned restriction on recommendation types. The specification does not vary across classified environmental states. |
| **Levels 1 + 2 unified, state-conditioned** | Both governed by classified environmental state? | **No** | There is no environmental state classification. The governance is policy-level (verify the whole policy) not state-level (restrict recommendations per classified state). |

- **Binary vs. graduated governance:** The GS framework implements **binary governance at the policy level** — the policy either passes verification (AI operates) or it doesn't. The deployment infrastructure adds binary runtime monitoring (continue/disable). There is no graduated governance where AI participates under restricted advisory scope in intermediate safety states.
- **Key structural difference from my architecture:** My architecture classifies environmental state → determines governance pair (G(S), A_AI(S)) → constrains AI output per state. The GS framework verifies policy against specification relative to world model → gates the entire policy. My approach is **state-conditioned and graduated**; GS AI is **policy-level and binary** (at the verification level, though the safety specification itself can encode nuance).
- **Support for two-level governance pair:** The paper implicitly supports the need for something like my architecture by identifying the autonomous vehicle example (Example 4.2) where the specification includes "a more restricted specification that would be maintained by the backup system (of which there could be multiple levels)" — acknowledging that different safety levels require different specification scopes. However, this is described as a design pattern, not formalised as a state-conditioned governance mechanism.

---

### 8. Human Role in Decision-Making
- **Primarily autonomous systems:** The GS framework is designed for AI systems that operate autonomously. The human role is in creating the safety specification, auditing the world model, and performing democratic oversight — not in making individual decisions.
- **CIRL (Cooperative IRL):** Discussed as a method for creating specifications where the AI must cooperate with and learn from humans (Section 3.3). The AI listens to human feedback and aims to be corrigible.
- **Democratic oversight:** A key benefit of GS AI is that safety specifications can be audited and discussed by outside observers, regulators, and the public (Section 5). This enables societal input into what safety properties AI systems should satisfy.
- **Contrast with my research:** My architecture is a decision **support** system where the human makes the final decision. The GS framework is designed for decision **automation** where the AI acts autonomously within verified bounds.

---

### 9. System Constraints and Environment
- **Computational complexity:** Acknowledged as a major challenge. Formal verification is resource-intensive, but the paper argues that AI systems can be trained to automate much of this labour. The deployment infrastructure can modulate verification time horizons to manage complexity.
- **Real-world deployment:** Discussed through concrete examples (AVs, household robots, medical diagnosis). The paper acknowledges that for complex environments (human users, economies, ecosystems), fully manual world models may not be feasible — machine learning must be used.
- **Resource-aware design:** Not a focus. The paper targets frontier AI systems and well-resourced deployment contexts.
- **Edge cases:** The deployment infrastructure is designed to handle cases where the world model is found inaccurate at runtime, through monitoring and backup systems.

---

### 10. Hybrid AI Taxonomy
- **Hybrid approach:** The GS framework is inherently a **constitutional/governance-based hybrid** — a formal verification layer (deterministic, rule-based) constrains a potentially black-box AI system (probabilistic, neural network). The verifier acts as a governance mechanism over the AI's output.
- **Safety enforcement position:** Safety enforcement sits **after** AI reasoning — the AI produces output, then the verifier checks it before deployment. This is a post-hoc verification approach, contrasting with my architecture where the deterministic safety gate operates **before** AI reasoning (gate-first).
- **Two-level governance support:** The framework supports Level 1 (participation governance via verification gate) and partial Level 2 (safety specification constrains what AI may do). However, Level 2 is not state-conditioned — the specification is applied globally, not varied across classified environmental states.
- **Comparison to my architecture:** My architecture is **gate-first, state-conditioned, graduated**: classify state → gate AI participation → restrict advisory scope. The GS framework is **verify-after, policy-level, binary**: AI produces output → verifier checks → deploy or disable. Both use deterministic mechanisms to govern probabilistic AI, but at different structural positions, granularities, and with different graduation models.

---

### 11. Baseline Comparison and Evaluation
- **Compared against:** Current AI safety practices (empirical evaluations, red-teaming, quality assurance) — argued to be insufficient for safety-critical applications (Figure 1).
- **No empirical evaluation:** This is a position paper; no empirical results are presented. The examples (Section 4) are illustrative, not evaluated.
- **CAUTION zone testing:** Not applicable — no CAUTION zone exists in the framework.
- **Graduated vs. binary governance comparison:** Not performed. The paper does not compare graduated governance against binary governance.
- **Formal property verification:** The entire framework is designed around formal verification, but no concrete verification is demonstrated.
- **Evaluation gaps:** The paper acknowledges that creating accurate world models, adequate safety specifications, and scalable verifiers are all major open challenges. No concrete system has been built and evaluated.

---

### 12. Key Concepts and Definitions
- **Guaranteed Safe (GS) AI:** AI system equipped with a quantitative safety guarantee produced by a world model, safety specification, and verifier (Definition 3.1)
- **World model:** Mathematical description of how the AI system affects the outside world, handling Bayesian and Knightian uncertainty; m : S × A → P(Δ(O × S))
- **Safety specification:** Mathematical description of what effects are acceptable; ψ : Π × M → [0, 1]
- **Verifier:** Algorithm producing an auditable proof certificate that the AI satisfies the specification relative to the world model; Vψ : Π × M → P([0, 1])
- **World model levels (W0–W5):** From no world model (W0) to universally quantified specifications over all possible worlds (W5)
- **Safety specification levels (S0–S7):** From no specification (S0) to complete encoding of all human values (S7)
- **Verifier levels (V0–V10):** From no testing (V0) to human-readable formal proofs (V10)
- **AI Safety Levels (ASL):** Anthropic's classification of AI system risk from ASL-1 (no meaningful risk) to ASL-5+ (superhuman intelligence)
- **Knightian uncertainty:** Uncertainty that cannot be reduced to a probability distribution — handled through credal sets in the world model
- **Defence in depth:** Deploying multiple layers of protection against complex threats
- **Harm (Appendix A):** Formalised using causal models: event X=x causes harm if the actual outcome's utility is below default utility and an alternative event would have led to better utility

---

### 13. Limitations and Unsolved Problems
- **Stated limitations / open challenges:**
  - Creating sufficiently accurate and interpretable world models for complex environments (human behaviour, ecosystems, economies)
  - Fundamental trade-off between interpretability and predictive accuracy of world models
  - Difficulty of formalising complex safety predicates (e.g., "harm") — Goodhart's law means proxies may fail under optimisation pressure
  - Scalability of formal verification to AI systems
  - Most approaches in the GS portfolio remain at the research stage; no concrete system has been fully built
  - The paper is explicitly a research agenda, not a demonstrated solution
- **Gaps aligning with my research:**
  - **No state-conditioned governance:** The framework verifies policies globally but does not define how governance should vary across classified environmental states. My architecture fills this gap by introducing state-conditioned governance pairs.
  - **No graduated advisory scope restriction:** The GS framework is binary at the verification level (pass/fail). My CAUTION mode — where AI participates but with restricted recommendation scope — has no analogue.
  - **No environmental state classification function:** The GS framework has a world model but no f(E) that classifies the current state into discrete safety levels determining governance behaviour.
  - **No Safety Dominance Property for graduated governance:** The GS framework provides global policy-level guarantees. My Safety Dominance Property (AI(E) ⊆ A_AI(S)) provides per-state guarantees for graduated governance — a more granular formal property.
  - **No low-resource consideration:** The framework targets frontier AI; my architecture addresses low-resource deployment constraints.

---

### 14. Methodology Notes
- **Method:** Position paper with formal definitions, taxonomies (spectra for each component), concrete illustrative examples, and argument from necessity.
- **DSR alignment:** Not DSR. The paper defines a research agenda and provides a formal framework, but does not follow a design-build-evaluate cycle.
- **Informing my work:** The GS AI formal definition (tuple ⟨π, m, ψ, Vψ⟩) provides a high-level framework against which my architecture can be positioned. My architecture can be understood as a specific instantiation of the GS principle — with a particular world model (E), a particular safety specification (the state classification f(E) and governance pair (G(S), A_AI(S))), and a particular verification approach (deterministic safety gate with Safety Dominance Property). The key difference is that my instantiation is state-conditioned and graduated, operating at the per-recommendation level rather than the per-policy level.

---

### 15. Quotable / Citable Points

1. **Insufficiency of empirical evaluation (Sec. 2.3):** The paper argues that empirical evaluations are fundamentally inadequate for safety-critical AI — ChatGPT's safety precautions were circumvented within a day of going public despite months of detailed evaluation.

2. **Formal definition of GS AI (Definition 3.1 / B.1):** The three-component architecture (world model + safety specification + verifier) with formal mathematical definition provides the authoritative framing for formal safety guarantees in AI.

3. **World model levels spectrum (Sec. 3.2, Figure 2):** The W0–W5 classification provides vocabulary for positioning different approaches to environmental modelling, with manually created models at W4 and physics-verified models at the highest levels.

4. **Backup systems and deployment infrastructure (Sec. 5):** The paper notes that for safety-critical systems, simply shutting down may not be safe — a trustworthy backup system appropriate for the domain of use is required, echoing the need for graduated responses rather than binary disable.

5. **AV safety example (Example 4.2):** Explicitly mentions "a more restricted specification that would be maintained by the backup system (of which there could be multiple levels)" — implicitly acknowledging graduated safety governance.

---

### 16. Relation to My Research and Positioning

- **Level 1 governance:** Implemented through the verifier gate — AI output only reaches the world if verification passes. This is binary, policy-level participation governance.
- **Level 2 governance:** Partially present — the safety specification constrains what AI may do, but this constraint is global, not state-conditioned. The specification does not vary across classified environmental states.
- **State-conditioned two-level pair:** Not implemented. No environmental state classification drives governance behaviour.
- **Safety Dominance Property comparison:** The GS framework provides a global guarantee (Vψ(π, m) ∈ permissible set). My Safety Dominance Property (AI(E) ⊆ A_AI(S)) is a per-state, per-recommendation guarantee — more granular and specifically designed for graduated governance.
- **Gap my research addresses:** The GS AI framework provides the highest-level formal framing for AI safety guarantees, but does not specify how governance should graduate across classified environmental states. My architecture fills this gap by instantiating GS principles at a more granular, state-conditioned level — classifying the current environmental state, determining a governance pair (G(S), A_AI(S)), and constraining AI advisory scope accordingly, with a formal Safety Dominance Property guaranteeing per-state compliance.

**Positioning paragraph:** This paper provides the foundational theoretical framework for formal safety guarantees in AI, authored by leading AI safety researchers across top institutions. Its three-component architecture (world model, safety specification, verifier) establishes the vocabulary and formal machinery for reasoning about guaranteed AI safety. My architecture can be positioned as a **domain-specific, state-conditioned instantiation** of GS AI principles: where the GS framework verifies entire policies against global specifications, my architecture classifies the current environmental state and applies a state-conditioned governance pair that determines both whether AI participates and what it may recommend. The CAUTION mode — where AI participates under restricted advisory scope — addresses a gap in the GS framework, which is binary at the verification level (pass/fail) with no intermediate graduated mode. The Safety Dominance Property formalises a per-state guarantee that complements the GS framework's global policy-level guarantee. This paper is a core reference for: (a) positioning my contribution within the broader AI safety landscape, (b) anchoring my formal architecture in established theoretical foundations, (c) citing the argument for necessity of formal guarantees over empirical testing, and (d) contrasting my graduated, state-conditioned approach with the GS framework's global, binary verification model.

---

### 17. Overall Relevance Score

**⭐⭐⭐⭐⭐ Core — directly addresses the formal safety guarantee landscape within which my two-level governance contribution is positioned**

**Justification:** This is the most authoritative single reference on formal safety guarantees for AI, authored by a constellation of leading AI safety researchers. It establishes the theoretical framework (world model + safety specification + verifier) against which my architecture's contribution — state-conditioned graduated governance with a per-state Safety Dominance Property — can be precisely defined and differentiated. The paper's gap (no environmental state classification, no graduated advisory scope governance, no per-state formal property) is exactly what my architecture fills. It provides both the conceptual vocabulary and the formal machinery for positioning my contribution. Already rated ⭐⭐⭐⭐⭐ in the tracker; this extraction confirms and strengthens that rating.
