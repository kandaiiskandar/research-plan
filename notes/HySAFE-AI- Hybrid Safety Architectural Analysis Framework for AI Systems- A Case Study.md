# Literature Review Extraction
## Paper: HySAFE-AI: Hybrid Safety Architectural Analysis Framework for AI Systems: A Case Study

---

## 1. Paper Identity

- **Full title:** HySAFE-AI: Hybrid Safety Architectural Analysis Framework for AI Systems: A Case Study
- **Authors:** Mandar Pitale, Jelena Frtunikj, Abhinaw Priyadershi, Vasu Singh, Maria Spence (all Nvidia Corporation / Nvidia GmbH)
- **Year:** 2025 (arXiv:2507.17118v1, 23 July 2025)
- **Venue:** arXiv preprint (not yet peer-reviewed)
- **Type of paper:** Industry-oriented framework/methodology paper with case study (safety analysis of end-to-end autonomous driving architecture)

---

## 2. Core Contribution

- **Main problem:** Traditional safety analysis methods (FMEA, FTA) were designed for systems with clear component boundaries and well-understood failure mechanisms. They are fundamentally limited when applied to foundation-model-based AI systems (LLMs, VLMs) due to three issues: (1) abstraction incompatibility (distributed representations in continuous latent spaces vs. discrete failure states), (2) causal opacity (untraceable cause-effect in DNNs), and (3) temporal dynamism (context-dependent behaviours vs. assumed stable behaviour).
- **Proposed solution:** HySAFE-AI — a hybrid framework that augments traditional FMEA/FTA with: (a) architectural transparency requirements (multi-level abstraction of FM systems), (b) an AI-specific failure taxonomy mapping AI failure modes (hallucination, distributional shift, quantization effects, temporal reasoning failure) to standard FMEA guidewords, and (c) augmented FTA incorporating latent space error propagation paths. The framework is demonstrated on a reference end-to-end autonomous driving architecture.
- **Main contributions:**
  - Identifies fundamental limitations of FMEA/FTA for foundation-model-based AI
  - Creates an AI-specific failure mode taxonomy with FMEA guideword mappings (Table III)
  - Applies augmented FMEA/FTA to a reference E2E ADS architecture, computing Risk Priority Numbers (RPN)
  - Proposes a "fused stack" architecture with safety mitigations: Policy Monitor (OOD detection, uncertainty quantification), Safety Evaluator (rule-based/physics checks), and Plan Arbitration (trajectory selection)
  - Demonstrates RPN reduction through architectural safety mitigations (Table V)
- **What is novel:** The systematic mapping between AI-specific failure modes and traditional FMEA guidewords. The augmented FTA that decomposes E2E "closed-box" AI into analysable sub-components. The fused architecture combining FM capabilities with runtime safety mechanisms.

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | **Partial** | The "fused stack" architecture combines E2E foundation models (probabilistic) with a Safety Evaluator that applies rule-based and physics-derived checks. This is a hybrid architecture, but focused on perception/planning validation, not decision-support governance. |
| Safety-critical AI decision-making | **Yes** | Autonomous driving is a safety-critical domain. The paper analyses safety failure modes and proposes architectural safety mitigations for FM-based systems. |
| AI governance / control mechanisms | **Partial** | The Policy Monitor and Safety Evaluator function as runtime governance mechanisms that evaluate and can reject AI outputs. The Arbitrator selects trajectories that pass both checks. However, these are per-output validation mechanisms, not state-conditioned governance of AI recommendation scope. |
| Low-resource environments | No | Targets high-compute autonomous driving with large foundation models (8.4B parameters). Notes quantization for resource-constrained hardware but not in the low-resource sense of my research. |
| Decision architecture formalisation | No | No formal mathematical model. FMEA/FTA are structured engineering methods but not formal decision models with state variables, gate functions, or action spaces. |
| Human role in decision-making | No | The paper focuses entirely on automated systems architecture. No discussion of human decision-making, human-AI interaction, or decision support. |
| Socio-technical evaluation | No | Pure engineering safety analysis. |
| Coastal fisheries / maritime domain | No | Autonomous driving domain. |

**Mid-Extraction Relevance Gate:** 1 Yes + 2 Partial → **REDUCED EXTRACTION** (Sections 4–7 and 12–13 only; Sections 8–11 and 14–15 skipped)

---

## 4. Decision Architecture Analysis

- **Decision-making structure:** The paper describes an end-to-end autonomous driving pipeline: sensor inputs → encoder → latent space processing (diffusion, U-Net, denoiser) → decoder → trajectory planner → control. The fused architecture adds safety mechanisms: Policy Monitor evaluates E2E planner reliability, Safety Evaluator applies rule-based/physics checks, and Plan Arbitration selects validated trajectories.
- **Layered architecture / governance structure:** The fused architecture (Figure 3) has a two-path structure: (1) E2E monolithic model generates candidate trajectories, and (2) a modular safety pathway (perception → prediction → planning) provides fallback trajectories. Both paths feed into the Arbitrator, which selects based on verification from Policy Monitor and Safety Evaluator. This is a redundancy-based safety architecture, not a state-conditioned governance architecture.
- **Rule-based constraints or safety checks:** Yes — the Safety Evaluator applies "rule-based and physics-derived checks to reject unsafe trajectories." These include vehicle dynamics constraints (e.g., rejecting physically impossible manoeuvres like 90-degree turns at highway speeds). The Policy Monitor performs OOD detection and uncertainty quantification.
- **Boundary between deterministic control and AI reasoning:** Partially defined. The E2E model is the probabilistic AI component; the Safety Evaluator and Policy Monitor are the deterministic/rule-based safety layer. The Arbitrator mediates between them.
- **Failure modes / fallback behaviour:** Extensively analysed via FMEA (Table III) and FTA (Figure 2). The fused architecture provides a fallback: if the E2E model's trajectory fails Safety Evaluator or Policy Monitor checks, the modular pathway's trajectory can be selected instead.

**Key distinction from my architecture:** The fused architecture validates AI *outputs* (trajectories) against safety criteria and selects among alternatives. My architecture restricts AI's *recommendation scope* before generation based on classified environmental safety state. Their approach is post-generation filtering/selection; mine is pre-generation scope restriction.

---

## 5. Formal Model and Mathematical Representation

- **Formal model:** None in the mathematical sense. The paper uses FMEA (structured tables with Severity × Occurrence × Detection = RPN) and FTA (fault tree diagrams). These are engineering analysis methods, not formal mathematical models.
- **Comparison to E → S = f(E) → (G(S), A_AI(S)) → AI(E):** No comparison possible. The paper does not define environmental state vectors, safety state classification functions, gate functions, or admissible action spaces. The safety analysis operates at the component-failure level, not the system-governance level.
- **State-dependent recommendation restriction:** Not present. The Safety Evaluator applies the same physics-based checks regardless of environmental conditions. There is no concept of varying AI recommendation scope based on classified safety state.
- **Safety Dominance Property:** Not formally defined. The fused architecture aims to ensure that unsafe trajectories are rejected, but this is not formalised as a property guaranteeing AI outputs fall within state-determined bounds.

---

## 6. Safety State Classification

- **Discrete risk/safety levels:** Not present as operational states. RPN values in the FMEA provide risk rankings for failure modes, but these are engineering analysis metrics, not runtime operational safety states that condition system behaviour.
- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:** No comparison possible. The paper does not classify operational conditions into safety levels. The OOD detection in the Policy Monitor could be interpreted as a binary safe/unsafe signal, but this is per-prediction validation, not environmental safety state classification.
- **AI recommendation scope differentiation:** Not present. The system either accepts or rejects a trajectory — there is no intermediate mode where AI generates trajectories with restricted scope.

---

## 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (equivalent to G(S)) | **Partial** | The Arbitrator can reject E2E model trajectories and select fallback modular trajectories instead. This is a per-output participation decision, not a state-conditioned system-level gate. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (equivalent to A_AI(S)) | No | No restriction on what the AI may *generate*. The Safety Evaluator and Policy Monitor validate outputs after generation, but do not restrict the AI's recommendation scope. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | No | No environmental safety state classification. Governance is per-output validation, not state-conditioned. |

- **Governance type:** **Per-output validation** — each AI output (trajectory) is individually evaluated against safety criteria. This is fundamentally different from my state-conditioned governance, which restricts the *type* of recommendations AI may generate based on classified environmental safety state.
- **Binary governance:** Yes — the system either accepts or rejects each trajectory. There is no intermediate mode.
- **Supports or contradicts two-level governance pair:** Neither directly. The paper's safety mechanisms (Policy Monitor, Safety Evaluator, Arbitrator) operate at a different architectural layer — they validate specific outputs rather than governing the AI's operational scope. However, the fused architecture's principle of combining AI capabilities with safety mechanisms is conceptually aligned with my hybrid approach.

---

## 12. Key Concepts and Definitions

| Concept | Definition / Description | Relevance |
|---|---|---|
| **HySAFE-AI** | Hybrid safety analysis framework augmenting FMEA/FTA for AI systems | Methodology reference — adapting safety analysis for AI |
| **AI-specific failure taxonomy** | Mapping of AI failure modes (hallucination, distributional shift, quantization effects, temporal reasoning failure, dataset staleness) to FMEA guidewords | Background on AI failure modes applicable to any AI safety analysis |
| **Policy Monitor** | Runtime component performing OOD detection and uncertainty quantification on AI outputs | Conceptually related to my gate function as a safety check mechanism |
| **Safety Evaluator** | Rule-based and physics-derived checks applied to AI-generated trajectories | Analogous to deterministic safety constraints in my architecture |
| **Plan Arbitration** | Selection logic choosing trajectories verified by both Policy Monitor and Safety Evaluator | Mediator between AI and safety — similar conceptual role to my governance pair |
| **Fused stack architecture** | Combines E2E foundation model with modular safety pathway, Policy Monitor, Safety Evaluator, and Arbitrator | Reference architecture for combining AI capabilities with safety mechanisms |
| **RPN (Risk Priority Number)** | Severity × Occurrence × Detection — quantitative risk metric in FMEA | Engineering risk metric; could inform my system's risk assessment approach |

---

## 13. Limitations and Unsolved Problems

- **Stated limitations:**
  - The FMEA analysis is not exhaustive — selected examples only
  - RPN values based on expert judgement, not empirical measurement
  - The fused architecture introduces computational overhead and latency
  - The paper is a case study on a reference architecture, not a deployed system
  - Limited to autonomous driving domain

- **Unsolved problems / future work:**
  - Comprehensive analysis of E2E ADS failure modes
  - Runtime mitigation measures based on hazard analysis
  - Collaboration with standards bodies for hybrid-AI safety architecture guidance

- **Alignment with my research gaps:**
  - The paper does **not** identify the lack of state-conditioned governance as a gap — its safety mechanisms operate per-output, not per-state
  - The paper does **not** address the CAUTION mode gap or graduated AI recommendation scope
  - The paper does **not** address decision support, human-AI interaction, or low-resource environments
  - **However**, the AI-specific failure taxonomy and the principle of combining AI capabilities with rule-based safety mechanisms are conceptually relevant. The Safety Evaluator (rule-based/physics checks applied to AI outputs) is a domain-specific instantiation of the deterministic-constraint-over-probabilistic-AI principle that my architecture also implements.

---

## 16. Relation to My Research and Positioning

- **Governance levels implemented:** Partial Level 1 (per-output accept/reject via Arbitrator). No Level 2. No state-conditioning.
- **State-conditioned governance:** No. Safety checks are applied uniformly to all outputs regardless of environmental conditions.
- **Proximity to (G(S), A_AI(S)):** Distant. The paper operates at the safety engineering/analysis layer (FMEA, FTA, architectural mitigations), not at the decision-governance layer. The Safety Evaluator applies rule-based checks to AI outputs, which is conceptually related to my deterministic safety constraints, but it does not vary by environmental safety state.
- **Safety Dominance Property:** Not defined.
- **Gap my research fills:** The paper demonstrates that safety-critical AI systems need hybrid architectures combining AI capabilities with deterministic safety mechanisms — but implements this as per-output validation rather than state-conditioned governance of AI recommendation scope.

**Positioning paragraph:** Pitale et al. (2025) provides **tangential background** on adapting safety analysis methods for AI systems. The paper's core contribution — augmenting FMEA/FTA with an AI-specific failure taxonomy for foundation-model-based systems — addresses safety *engineering methodology*, not safety *governance architecture*. The fused stack architecture (combining E2E models with Policy Monitor, Safety Evaluator, and Arbitrator) embodies the principle of constraining probabilistic AI with deterministic safety checks, which is conceptually aligned with my hybrid approach. However, the paper's safety mechanisms operate as per-output validation (accept/reject each trajectory individually) rather than as state-conditioned governance (restricting AI's recommendation scope based on classified environmental safety state). It does not define environmental state classification, does not implement graduated governance, and does not address decision support or human-AI interaction. Its primary value for my literature review is as a reference for how the autonomous driving industry approaches hybrid safety architectures — confirming that the principle of deterministic safety constraints over probabilistic AI is broadly adopted, but showing that state-conditioned governance of AI recommendation scope remains unaddressed even in industry safety frameworks.

---

## 17. Overall Relevance Score

### ⭐⭐ Low

**Justification:** The paper is directly relevant to one theme (safety-critical AI) and partially relevant to two others (hybrid AI, AI governance). It provides useful background on AI-specific safety analysis methodology and the principle of hybrid safety architectures in autonomous driving. However, it operates at the safety engineering/analysis layer rather than the decision-governance layer central to my research. It contains no formal model, no environmental safety state classification, no state-conditioned governance, no human role treatment, no decision support framing, and no relevance to low-resource or maritime domains. Its value is limited to a supporting reference for the industry-wide adoption of hybrid deterministic-constraint + probabilistic-AI architectures, without contributing to the specific governance gap my research addresses.
