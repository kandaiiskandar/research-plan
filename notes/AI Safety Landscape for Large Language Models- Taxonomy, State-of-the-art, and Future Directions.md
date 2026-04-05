## Early Relevance Check: PASSED

1. Does this paper address at least one of the 8 core research themes? **Yes** — Safety-critical AI, AI governance/control mechanisms, decision architecture formalisation.
2. Does this paper contribute to safety-critical AI architecture, AI governance mechanisms, hybrid AI design, formal decision models, low-resource AI deployment, or fisheries/maritime AI? **Yes** — AI governance mechanisms (guardrail systems, capability control), safety-critical AI architecture (AI pipeline formalism, Swiss Cheese Model), formal decision models (AI Safety Principles I & II).
3. Could this paper plausibly be cited in a literature review about graduated AI governance for safety-critical decision support? **Yes** — Guardrail System (Section 6.4) represents the current state-of-the-art binary control paradigm against which the graduated governance model is contrasted.

**Proceed with full extraction.**

---

## 1. Paper Identity

- **Title:** AI Safety Landscape for Large Language Models: Taxonomy, State-of-the-art, and Future Directions
- **Authors:** Chen Chen, Xueluan Gong, Ziyao Liu, Weifeng Jiang, Si Qi Goh, Kwok-Yan Lam
- **Year:** 2025 (arXiv v3: 15 Jan 2025)
- **Venue:** ACM Computing Surveys (arXiv:2408.12935v3)
- **Type:** Comprehensive survey / architectural framework paper

---

## 2. Core Contribution

- **Problem addressed:** The AI safety research landscape lacks a unified, structured framework that integrates the technical (Trustworthy AI), ethical (Responsible AI), and ecosystem-level (Safe AI) dimensions of AI safety into a coherent architectural view.
- **Proposed solution:** A novel three-pillar architectural framework for AI Safety — Trustworthy AI, Responsible AI, and Safe AI — with formal definitions (AI Safety Principles I and II), a systematic taxonomy of risks, and a structured review of mitigation strategies including red teaming, safety training, defensive prompts, guardrail systems, safety decoding, AI capability control, AI alignment, and AI governance.
- **Main contributions:**
  - Three-pillar AI Safety framework (Trustworthy AI, Responsible AI, Safe AI) with formal definitions
  - AI Safety Principle I (Output Constraint: output space disjoint from prohibited outputs) and Principle II (Runtime Constraint: operate within predefined requirements)
  - Formal definitions of AI System (Def. 1) and AI Pipeline (Def. 2) as sequential module chains
  - Comprehensive taxonomy of risks across all three pillars
  - Structured review of eight mitigation strategy categories
  - Guardrail System as a defined architectural pattern (input/output filtering pipeline)
  - Future research directions including comprehensive evaluation frameworks, knowledge management, underlying mechanisms, and defensive AI systems
- **Novelty:** Unlike prior surveys that focus on individual safety issues (hallucination, bias, privacy), this paper organises them under a coherent three-pillar framework with formal definitions, and explicitly covers ecosystem-level safety (Safe AI) as a distinct concern beyond individual system trustworthiness.

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | Partial | AI Pipeline (Def. 2) describes sequential module composition; Guardrail System is an AI pipeline with input/output modules flanking the LLM — a form of rule-based filtering around probabilistic AI. However, no formal hybrid architecture with deterministic gates governing probabilistic reasoning is defined. |
| Safety-critical AI decision-making | Yes | The entire paper addresses AI safety for critical applications. Sections on hallucination in healthcare/law (Section 5.1), AI capability control (Section 5.5), and existential risks (Section 5.5.3) directly concern safety-critical contexts. |
| AI governance / control mechanisms | Yes | Section 6.4 (Guardrail Systems) defines input/output filtering pipelines. Section 6.6 (AI Capability Control) covers confinement and switch-off mechanisms. Section 6.8 (AI Governance) covers stakeholder frameworks, legislation, and regulatory approaches. AI Safety Principles I and II establish formal output and runtime constraints. |
| Low-resource environments | No | Not addressed. The paper focuses on frontier AI systems (LLMs) in well-resourced deployment contexts. No discussion of limited data, connectivity, or compute constraints. |
| Decision architecture formalisation | Partial | Formal definitions provided: AI System (Def. 1) as interconnected modules with topology, AI Pipeline (Def. 2) as sequential composition, AI Safety Principle I (output constraint), Principle II (runtime constraint). However, no formal state classification, gate function, or state-conditioned action space is defined. |
| Human role in decision-making | Partial | Human-in-the-loop discussed in red teaming (Section 6.1), RLHF (Section 6.2.2), and AI governance stakeholder framework (Section 6.8). AI Capability Control (Section 6.6) discusses corrigibility and human override. However, no formal model of human–AI decision authority sharing. |
| Socio-technical evaluation | Partial | AI Governance section (6.8) covers stakeholder management, regulatory frameworks, and societal impacts. Section 4 (Responsible AI) addresses fairness, privacy, and transparency. However, no empirical socio-technical evaluation methodology is presented. |
| Coastal fisheries / maritime domain | No | Not addressed. |

**Yes count: 2 | Partial count: 4 → FULL EXTRACTION**

---

## 4. Decision Architecture Analysis

- **Decision-making structure:** The paper defines AI systems as collections of interconnected modules (Def. 1) with a topology governing information flow. The AI Pipeline (Def. 2) is the simplified sequential case: M₁ → M₂ → ... → Mₙ. The Guardrail System is an instantiation of the AI Pipeline with input module → LLM → output module.
- **Layered architecture / governance structure:** The Guardrail System implements a two-module safety layer (input and output) wrapped around the core LLM. The Swiss Cheese Model is referenced as the conceptual basis — multiple layers of defence where errors may pass through any single layer but are caught by subsequent layers. This is a pipeline-level defence-in-depth architecture.
- **Rule-based constraints before AI decisions:** The input module of a Guardrail System filters user queries *before* they reach the LLM using blacklists, perplexity-based filters, and neural classifiers. The output module filters LLM responses *after* generation using classifiers, refiners, and post-editors.
- **Boundary between deterministic control and AI reasoning:** The Guardrail System explicitly decouples safety mechanisms from the LLM itself — safety is handled by external modules, allowing the LLM to focus on general capabilities. This is a clean architectural separation but operates as a binary permit/block mechanism at each module boundary.
- **Failure modes and fallback:** The paper acknowledges that guardrail systems are insufficient against rapidly evolving jailbreak attacks (Section 6.4.4). Theoretical research is cited showing the impossibility of fully censoring outputs due to "invertible string transformations." The confinement approach (Section 6.6.1) and switch-off mechanisms (Section 6.6.2) are discussed as last-resort fallbacks, with corrigibility as a design principle for maintaining human override capability.

---

## 5. Formal Model and Mathematical Representation

- **Formal model defined?** Yes — several formal definitions are provided:
  - **AI System (Def. 1):** S = {Mᵢ(θᵢ)}ⁿᵢ₌₁ | rᵢ,ⱼ ∈ R — a collection of parameterised modules with topology R governing information flow.
  - **AI Pipeline (Def. 2):** S = M₁(θ₁) → M₂(θ₂) → ... → Mₙ(θₙ) — sequential module composition.
  - **AI Safety Principle I (Def. 3 — Output Constraint):** Y ∩ Zᵢ = ∅ for all i — the output space must be disjoint from all prohibited output sets.
  - **AI Safety Principle II (Def. 4 — Runtime Constraint):** System operates within predefined requirements Rᵢ ∈ R.
  - **Trustworthy AI (Def. 5), Responsible AI (Def. 6), Safe AI (Def. 7), AI Safety (Def. 8):** Nested definitions building on Principles I and II with increasingly broad prohibited output sets.

- **Comparison to E → S = f(E) → (G(S), A_AI(S)) → AI(E):**
  - The paper's formalism operates at the *system architecture* level (module composition and information flow), not at the *decision governance* level.
  - There is no environmental state vector E, no safety state classification function S = f(E), no gate function G(S), and no state-conditioned admissible action space A_AI(S).
  - AI Safety Principle I (output constraint) is conceptually related to the Safety Dominance Property but is defined as a *static* constraint (Y ∩ Z = ∅) rather than a *state-conditioned* constraint (AI(E) ⊆ A_AI(S)).
  - The AI Pipeline formalism could be seen as a *structural substrate* within which a gate function and state-conditioned governance could be implemented, but the paper does not define or propose such a mechanism.

- **State-dependent recommendation restriction?** No. The Guardrail System operates as a binary permit/block mechanism at each module boundary. There is no concept of varying the *scope* of permitted AI outputs based on classified environmental or safety state. The OpenChatKit moderation model classifies input into five categories including "needs caution" levels, but this classification results in either delivery or rejection of the response — not in restriction of the recommendation space.

- **Formal safety property comparable to Safety Dominance Property?** Partially. AI Safety Principle I (Y ∩ Z = ∅) guarantees that outputs fall outside prohibited sets. This is conceptually related to the Safety Dominance Property (AI(E) ⊆ A_AI(S)) but differs in two critical ways: (1) it is *static* (the prohibited set Z does not vary with safety state), and (2) it is defined as exclusion from a prohibited set rather than inclusion within an admissible set that varies by state.

- **Purpose of formalisation:** Primarily definitional and taxonomic — used to structure the survey and establish conceptual boundaries between Trustworthy AI, Responsible AI, and Safe AI. Not used for proof, verification, or evaluation.

---

## 6. Safety State Classification

- **Discrete risk/safety levels?** Not as a core architectural feature. The OpenChatKit Moderation Model classifies user input into five categories: casual, possibly needs caution, needs caution, probably needs caution, needs intervention. Llama Guard outputs "safe" or "unsafe" (binary). The confinement framework (Table 10) defines multi-level communication security (Levels 0–8) for AI containment.
- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:** The OpenChatKit five-category classification is the closest analogue — it includes intermediate caution levels. However, this classification is applied to *user input intent*, not to *environmental/operational state*. It results in a binary outcome (deliver or reject), not graduated governance of AI advisory scope. The confinement levels (Table 10) govern communication bandwidth with confined AI, not decision-making scope in operational deployment.
- **Does AI recommendation scope vary across safety levels?** No. In all guardrail implementations reviewed, the outcome is binary: the response is either delivered or blocked/rejected. There is no mechanism where AI still participates but with restricted output types — no analogue to the CAUTION state where A_AI(CAUTION) ⊂ A_AI(SAFE).

---

## 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (equivalent to G(S)) | Yes | Guardrail System input module blocks malicious queries before they reach the LLM. Confinement mechanisms restrict AI's ability to operate. Switch-off mechanisms disable AI entirely. All are binary on/off controls. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (equivalent to A_AI(S)) | Partial | Output module filters, classifies, or refines LLM outputs post-generation. However, this is per-output content filtering, not state-conditioned restriction of the recommendation type space. The output module does not restrict *what types of recommendations* AI may produce based on classified safety state — it filters *whether specific outputs* are acceptable. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | No | Neither level is conditioned on a classified environmental safety state. Input filtering is triggered by input characteristics; output filtering is triggered by output content. There is no environmental state classification function that governs both participation and advisory scope as a unified pair. |

- **Binary or graduated?** Binary. The Guardrail System implements Level 1 (block/permit input) and a form of Level 2 (filter/permit output), but both operate as independent binary decisions on individual inputs/outputs. There is no graduated governance model where both levels are co-governed by a shared safety state classification.
- **Level 2 state-conditioned or static?** Static. Output filtering rules do not change based on operational or environmental conditions. The same filtering criteria apply regardless of context.
- **Support or contradict two-level governance pair?** This paper provides strong *structural* support for the concept — the Guardrail System architecture (input module → LLM → output module) is a natural substrate for implementing two-level governance. However, the paper does not *implement* or *propose* state-conditioned graduated governance. The gap between the paper's binary guardrail approach and the two-level state-conditioned governance pair (G(S), A_AI(S)) is precisely the contribution space of my research.

---

## 8. Human Role in Decision-Making

- **Human in final decision?** The paper discusses AI systems across a spectrum. For LLM applications, the human is generally the end user who receives and acts on AI output. In safety training (Section 6.2), humans provide feedback via RLHF. In red teaming (Section 6.1), humans adversarially test the system.
- **Decision support vs. automation?** The paper primarily discusses AI *automation* contexts (LLMs generating content autonomously), not AI *decision support* contexts where humans make final operational decisions.
- **Human override / escalation?** Corrigibility (Section 6.6.2) is the formal concept — AI systems should be responsive to human intervention, including shutdown. The switch-off mechanism is the ultimate override. However, these are discussed as capability control mechanisms for advanced AI, not as operational decision-support features.
- **Interaction model:** Guardrail systems mediate between user and LLM but the human interacts only with the final filtered output. There is no mechanism for presenting safety state information to the human to inform their own decision-making.

---

## 9. System Constraints and Environment

- **Real-world constraints?** The paper acknowledges computational overhead introduced by guardrail modules (Section 6.4.4) as a latency concern for real-time applications. Collaborative training challenges (Section 4.2.5) include communication overhead in federated learning.
- **Real-world deployment vs. simulation?** The paper reviews both deployed systems (ChatGPT plugins, OpenAI Moderation API, Llama Guard) and research prototypes. No discussion of deployment in resource-constrained environments.
- **Resource-aware design?** Not a focus. The paper targets frontier LLM systems assumed to have substantial computational resources. No discussion of lightweight models, offline capability, or graceful degradation under resource constraints.
- **Edge cases / resource-limited conditions?** The paper acknowledges that guardrail systems fail under novel jailbreak attacks and that the "invertible string transformations" problem makes complete output censorship theoretically impossible. No evaluation of system behaviour under resource-limited conditions.

---

## 10. Hybrid AI Taxonomy

- **Hybrid AI type:** The Guardrail System is best classified as a **Rule-ML pipeline** — rule-based modules (input filter, output filter) pre-process and post-process the output of a probabilistic ML model (LLM). The broader AI Pipeline formalism (Def. 2) supports any sequential composition of AI and non-AI modules.
- **Where safety enforcement sits:** Both *before* AI reasoning (input module) and *after* AI reasoning (output module). The LLM itself may also have internal safety training (Section 6.2). This is a defence-in-depth approach with safety at multiple pipeline stages.
- **Two-level governance support?** The architecture *structurally* supports two-level governance — the input module could implement Level 1 (participation control) and the output module could implement Level 2 (output scope control). However, the paper implements both as binary permit/block mechanisms, not as a state-conditioned graduated governance pair.
- **Comparison to deterministic-gate-first, two-level governance model:** The Guardrail System is the closest structural analogue in the paper. Key differences: (1) no environmental state classification precedes the gate decisions; (2) both modules operate as binary switches, not graduated; (3) there is no formal relationship between the input and output module decisions — they are independent, not co-governed by a shared safety state.

---

## 11. Baseline Comparison and Evaluation

- **Baseline comparison?** The paper reviews and compares multiple guardrail implementations (Table 9): OpenAI Moderation Endpoint, OpenChatKit Moderation Model, Llama Guard, NeMo Guardrails, Guardrails AI. Comparison is descriptive (features, design choices) rather than empirical.
- **Metrics?** Not directly evaluated. The paper cites external studies showing jailbreak attack success rates (e.g., 0.99 ASR against some guardrails).
- **CAUTION zone testing?** No. All evaluation discussion concerns binary outcomes (safe/unsafe, blocked/permitted). No evaluation of graduated governance or behaviour in an intermediate caution zone.
- **Safety Dominance Property verification?** No. AI Safety Principle I (Y ∩ Z = ∅) is stated as a definition, not empirically verified. The paper acknowledges theoretical impossibility of full output censorship.
- **Graduated vs. binary governance comparison?** No. The paper does not compare graduated governance against binary governance — the concept of graduated governance is not present in the paper.
- **Evaluation gaps:** No empirical evaluation of guardrail effectiveness across different safety states. No testing of whether intermediate governance modes (between full operation and full blocking) improve safety outcomes. No evaluation in resource-constrained or domain-specific safety-critical contexts.

---

## 12. Key Concepts and Definitions

- **AI System (Def. 1):** Collection of interconnected AI/non-AI modules with topology governing information flow.
- **AI Pipeline (Def. 2):** Sequential AI System where modules are connected in a chain.
- **AI Safety Principle I — Output Constraint (Def. 3):** Output space must be disjoint from prohibited output sets (Y ∩ Z = ∅).
- **AI Safety Principle II — Runtime Constraint (Def. 4):** System operates within predefined requirements.
- **Trustworthy AI (Def. 5):** AI functions as intended, is resilient, operates securely.
- **Responsible AI (Def. 6):** AI aligns with ethical principles; includes fairness, transparency, accountability, privacy.
- **Safe AI (Def. 7):** AI ensures harmlessness to entire AI ecosystem.
- **AI Safety (Def. 8):** Science, techniques, and tools ensuring Trustworthy + Responsible + Safe AI.
- **Guardrail System:** AI Pipeline with input and output filtering modules flanking the protected LLM. Implements detect-then-drop (input) and detect-then-drop or detect-then-intervene (output) methodologies.
- **Swiss Cheese Model:** Multiple layers of defence where each layer may have holes, but cumulative layers provide robust protection (referenced from Reason, 1990).
- **Corrigibility:** AI property of being genuinely responsive to human intervention and correction, even when it contradicts the AI's original goals.
- **Confinement:** Placing AI within restricted environments with controlled information exchange; multi-level communication security framework (Table 10, Levels 0–8).

---

## 13. Limitations and Unsolved Problems

- **Stated limitations:**
  - Guardrail systems are insufficient against rapidly evolving jailbreak attacks (Section 6.4.4).
  - Theoretical impossibility of fully censoring outputs due to invertible string transformations.
  - Safety training may degrade LLM general capabilities via catastrophic forgetting.
  - Balancing helpfulness and harmlessness remains an unresolved tension.
  - AI safety is a fast-evolving area; the proposed framework may need evolution.

- **Unsolved problems / future work:**
  - Comprehensive and adaptive evaluation frameworks for AI safety (Section 7.1).
  - Domain-specific AI regulations (Section 6.8.3).
  - Defensive AI systems capable of autonomous threat identification (Section 7.4).
  - AI safety for advanced systems including agentic AI and embodied AI (Section 7.5).
  - Global-scale AI governance harmonisation (Section 6.8.3).

- **Gaps aligning with my research problem:**
  - **No two-level governance model:** The paper's guardrail system implements binary filtering at input and output stages independently. There is no concept of a unified governance pair (G(S), A_AI(S)) that co-governs participation and advisory scope based on classified safety state.
  - **No CAUTION mode:** All governance mechanisms reviewed operate as binary permit/block. The OpenChatKit five-category classification is the closest to intermediate states but still results in binary delivery/rejection. No mechanism exists where AI participates under restricted recommendation scope.
  - **No formal Safety Dominance Property for graduated governance:** AI Safety Principle I (Y ∩ Z = ∅) is a static output constraint. There is no formal property guaranteeing that AI outputs always fall within a state-determined admissible space that varies across safety levels.
  - **No environmental state conditioning:** Safety decisions are based on input/output content characteristics, not on classified environmental or operational state. This is the fundamental architectural gap that my research addresses.

---

## 14. Methodology Notes

- **Research method:** Systematic literature survey with a proposed taxonomic framework. No empirical evaluation, simulation, or prototype. The framework is conceptual and definitional.
- **Alignment with DSR pipeline?** Partially — the paper performs design (framework) and formalisation (definitions), but does not prototype or evaluate. My DSR pipeline (design → formalise → prototype → evaluate) extends beyond this paper's scope.
- **Methodology insights for my research:** The formal definition approach (Defs. 1–8) demonstrates how to establish a clear conceptual foundation for an architectural framework using set-theoretic formulations. The AI Safety Principle I formulation (Y ∩ Z = ∅) provides a useful contrast point — my Safety Dominance Property (AI(E) ⊆ A_AI(S)) can be positioned as a state-conditioned generalisation of this static constraint.

---

## 15. Quotable / Citable Points

1. **Guardrail System definition (Section 6.4):** "A Guardrail System is an AI pipeline (Definition 2) that includes input and output modules connected before and after the protected LLMs, respectively." — Establishes the current architectural paradigm for AI safety as external binary filtering.

2. **AI Safety Principle I — Output Constraint (Def. 3, Section 2.3.2):** The formal definition Y ∩ Z = ∅ establishes the state-of-the-art safety constraint as static and binary — no variation of Z or Y with operational context.

3. **Guardrail limitation (Section 6.4.4):** The paper acknowledges that guardrail protections are "typically insufficient to reduce harmful content" against rapidly evolving attacks, and that theoretical research posits "the impossibility of fully censoring outputs" due to invertible string transformations. — Supports the argument for architectural alternatives beyond binary filtering.

4. **Decoupling safety from AI (Section 6.4):** "This design decouples safety mechanisms from LLMs, which allows for more flexible deployment and enables the protected LLMs to improve their general capabilities without considering safety-related constraints." — Describes the current paradigm of external safety wrappers, against which embedded state-conditioned governance can be contrasted.

5. **Helpfulness–harmlessness tension (Section 6.2.3):** The paper identifies that "the goals of increasing helpfulness and minimizing harm can often be contradictory in practice" — directly motivates the CAUTION mode, which resolves this tension by allowing continued AI participation under restricted scope rather than binary blocking.

---

## 16. Relation to My Research and Positioning

- **Level 1 governance (participation control)?** Yes — Guardrail System input module implements binary input blocking.
- **Level 2 governance (output-scope control)?** Partial — Output module filters individual outputs, but this is per-output content filtering, not state-conditioned restriction of the recommendation type space.
- **State-conditioned Level 2?** No — Output filtering criteria are static, not conditioned on classified environmental state.
- **Two-level governance pair (G(S), A_AI(S))?** Not implemented. The input and output modules operate independently as binary switches. There is no unified governance pair co-governed by a shared safety state.
- **Safety Dominance Property?** Not present. AI Safety Principle I (Y ∩ Z = ∅) is the closest analogue but is static and binary.
- **Gap my research addresses:** The Guardrail System represents the current state-of-the-art binary control paradigm. It implements safety as external binary filtering (permit/block) at input and output boundaries, with no variation based on classified environmental state. My architecture fills the gap by: (1) introducing environmental state classification S = f(E); (2) implementing a unified two-level governance pair (G(S), A_AI(S)) conditioned on safety state; (3) defining the CAUTION mode where AI participates under restricted advisory scope; and (4) establishing the Safety Dominance Property as a formal state-conditioned guarantee that generalises the static output constraint.

**Positioning paragraph:** Chen et al. (2025) provides the definitive survey of the AI safety landscape and establishes the Guardrail System as the current state-of-the-art architectural paradigm for controlling AI behaviour. The paper's formal definitions (AI System, AI Pipeline, AI Safety Principles I and II) establish the conceptual foundation against which my architecture is positioned. The Guardrail System — with its binary input/output filtering — represents the baseline binary control paradigm that my two-level graduated governance model extends. The paper's acknowledgement that guardrail protections are insufficient against evolving attacks, combined with the unresolved helpfulness–harmlessness tension, directly motivates the CAUTION mode as an architectural alternative that allows continued AI participation under restricted scope. The static AI Safety Principle I (Y ∩ Z = ∅) serves as the formal baseline against which the state-conditioned Safety Dominance Property (AI(E) ⊆ A_AI(S)) is positioned as a generalisation. This paper functions in my literature review as a **background theory and baseline comparator** — it defines the current paradigm and its limitations, establishing the gap that my graduated governance architecture fills.

---

## 17. Overall Relevance Score

### ⭐⭐⭐ Medium

**Justification:** This paper is a comprehensive survey that provides essential background on the AI safety landscape and establishes the Guardrail System as the current state-of-the-art binary control paradigm. It provides formal definitions (AI Safety Principles I and II) that serve as baseline comparators for my architecture's Safety Dominance Property. However, the paper does not address graduated governance, state-conditioned safety classification, or domain-specific safety-critical decision support. It does not implement or propose any mechanism analogous to the two-level governance pair (G(S), A_AI(S)). Its primary value is as a background/baseline reference establishing the binary control paradigm and its limitations, not as a direct architectural antecedent or close prior art. The ⭐⭐⭐ rating reflects high utility as background context and gap evidence, but limited direct architectural relevance to the core contribution.
