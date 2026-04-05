## Literature Review Extraction: Abella et al. (2025) — SAFEXPLAIN

---

### 1. Paper Identity

- **Title:** SAFEXPLAIN: a Complete Approach Towards Trustworthy AI-Based Safety-Critical Systems
- **Authors:** Jaume Abella, Irune Agirre, Thanh Bui, Frank Geujen, Gabriele Giordana, Carlo Donzella, Francisco J. Cazorla, Enrico Mezzetti, Axel Brando, et al. (21 authors)
- **Year:** 2025
- **Venue:** 28th Euromicro Conference on Digital System Design (DSD), IEEE, pp. 324–331
- **DOI:** 10.1109/DSD67783.2025.00053
- **Type:** Project overview / framework paper (EU Horizon Europe project, 3-year, multi-partner)
- **Note:** This is the project summary paper for a large EU-funded initiative. Cites Perez-Cerrolaza et al. (2024) as foundational work (already ⭐⭐⭐ in tracker).

---

### 2. Core Contribution

- **Problem:** DL software clashes with traditional safety-critical development processes in four fundamental ways: (1) DL is designed monolithically via training, not by implementing safety requirements; (2) DL cannot be considered correct-by-design due to data-driven stochasticity; (3) DL design depends on data, unlike traditional software; (4) DL imposes high computational demands with insufficient guidance for safety-critical integration.
- **Solution:** SAFEXPLAIN provides an end-to-end approach for integrating AI/DL into safety-critical systems across automotive, space, and railway domains, consisting of three pillars: (1) **AI Functional Safety Management (AI-FSM)** — extended V-model development process incorporating DL lifecycle phases; (2) **Safety architecture patterns** — reference pattern with supervision, redundancy, decision functions, and hierarchical diagnostics; (3) **Platform support** — middleware and tools on NVIDIA AGX Orin for implementing safety patterns.
- **Main contributions:**
  - AI-FSM lifecycle extending traditional V-model with DL-specific phases (Data Management, Learning Management, Inference Management)
  - Reference safety architecture pattern (Fig. 3) integrating: diverse AI redundancy, supervision function (safe envelope), hierarchical diagnostics (L1/L2/L3), decision function, non-AI fallback subsystem, and safety control
  - Three cross-domain case studies: automotive (object detection, distance estimation, trajectory prediction), railway (automatic train operation with obstacle/person detection), space (autonomous mission operations)
- **Novelty:** End-to-end integration from development process to safety architecture to platform realisation across three safety-critical domains. Inspired by E-Gas safety concept from automotive domain. First comprehensive framework addressing AI-FSM, architecture, and platform together.

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | Yes | Explicit architectural separation of AI-based subsystem and traditional (non-AI) subsystem. Supervision function provides rule-based safe envelope constraining DL output. Safety control integrates AI and non-AI outputs with diagnostic information |
| Safety-critical AI decision-making | Yes | Core focus — automotive, space, railway safety-critical systems. Entire framework designed to reconcile DL with functional safety standards (IEC 61508, ISO 26262, ISO/IEC TR 5469) |
| AI governance / control mechanisms | Yes | Supervision function bounds AI operations within predefined safety envelope. Safety control can discard AI suggestion and switch to non-AI fallback. Decision function aggregates diverse AI outputs with supervision signals. Hierarchical diagnostics (L1/L2/L3) monitor AI behaviour at multiple levels |
| Low-resource environments | No | Targets high-performance MPSoCs (NVIDIA AGX Orin, 275 TOPS, 32GB DRAM) |
| Decision architecture formalisation | Partial | Reference safety architecture pattern with defined components and information flows (Fig. 3). However, not formalised as mathematical pipeline with state variables, gate functions, or safety properties. Architecture is described as a configurable pattern, not a formal model |
| Human role in decision-making | Partial | User receives suggestions or decisions from decision function depending on DL usage level. Safety control can override AI. However, human role is not central — focus is on autonomous operation |
| Socio-technical evaluation | No | No socio-technical evaluation described. Evaluation is through case study integration |
| Coastal fisheries / maritime domain | No | Automotive, space, railway domains |

**Mid-Extraction Relevance Gate:** 3 Yes, 2 Partial → **FULL EXTRACTION**

---

### 4. Decision Architecture Analysis

- **Architecture:** Two-subsystem reference safety architecture pattern (Fig. 3):
  - **AI-based subsystem:** AI/ML constituent (with diverse redundancy) → Decision Function → outputs suggestion/decision
  - **Supervision components:** L1 Diagnostics & Monitoring + Supervision Function providing safe envelope constraints/limits
  - **Traditional subsystem:** Non-AI subsystem (fallback) + L2 Diagnostics & Monitoring
  - **Safety control:** Integrates AI output, non-AI output, diagnostic info, and supervision limits to command actuators or take system to safe state
  - **L3 Diagnostics:** External watchdog/microcontroller for final error handling
- **Layered structure:** Yes — multi-layered:
  - Layer 1: AI/ML constituent generates predictions
  - Layer 2: L1 diagnostics and supervision function monitor AI and establish safe boundaries
  - Layer 3: Decision function aggregates AI outputs with supervision signals
  - Layer 4: Safety control integrates all sources and can override AI
  - Layer 5: L2/L3 diagnostics provide platform-level and external monitoring
- **Rule-based constraints on AI:** The **supervision function** is the key governance element. It "bounds the AI/ML constituent operations to work within a predefined safety envelope" by collecting information from AI inputs/outputs and providing "a set of constraints or limits to the decision function." This is a rule-based constraint applied to AI output scope.
- **Boundary between deterministic and AI reasoning:** Explicitly architectural. The AI-based subsystem operates probabilistically; the supervision function, safety control, and non-AI fallback operate deterministically. The safety control can "discard the suggestion/decision from the decision function and operate according to the fallback function."
- **Failure modes / fallback:** Comprehensive:
  - L1DM detects runtime errors and model insufficiencies in AI constituent
  - Supervision function identifies when AI operates outside safe envelope
  - Safety control can switch to non-AI fallback or take system to safe state
  - L2DM provides platform-level error handling
  - L3DM provides external watchdog-level error handling

---

### 5. Formal Model and Mathematical Representation

- **Formal model:** No formal mathematical model. The architecture is described as a configurable reference pattern with defined components and information flows, but no state variables, gate functions, admissible action spaces, or safety properties are formally specified.
- **Comparison to DSR pipeline:** The architecture has structural parallels but is not formalised:
  - AI/ML constituent ≈ AI(E) (generates outputs from environmental inputs)
  - Supervision function providing safe envelope ≈ partial A_AI(S) (constraining AI output)
  - Safety control discarding AI and switching to fallback ≈ G(S) = 0 (blocking AI)
  - However, these are architectural descriptions, not formal functions
- **State-dependent recommendation restriction:** Not formally defined. The supervision function provides "constraints or limits" to the decision function, but whether these vary by classified environmental state is not specified. The architecture is described as configurable for "different DL usage levels" — suggesting the safe envelope can vary, but the mechanism for this variation is not formalised.
- **Safety Dominance Property:** Not defined. No formal guarantee that AI outputs always fall within state-determined bounds. The supervision function provides constraints, but these are not expressed as a formal containment property.
- **Formalisation purpose:** N/A — the paper describes an architectural pattern and development process, not a formal model.

---

### 6. Safety State Classification

- **Discrete safety levels:** Not explicitly defined as environmental state classification. The paper references "different DL usage levels" (with diverse safety requirements) that the architecture pattern can be tailored to — suggesting different governance configurations for different criticality levels. However, these are design-time configuration levels, not runtime environmental state classifications.
- **Comparison to S = f(E):** No environmental state classification function. The supervision function monitors AI behaviour and can trigger fallback, but the trigger conditions are not classified into discrete safety states.
- **AI recommendation scope across safety levels:** The decision function "according to the DL usage level, might provide a suggestion (e.g., warning message, status information) and/or decision (e.g., command on the actuators) to the user and/or safety control." This is the closest element to graduated advisory scope — different DL usage levels produce different output types (suggestion vs. decision). However, DL usage levels are design-time configurations, not runtime state-conditioned governance.

**Key observation:** The paper's "DL usage levels" concept — where the same architecture pattern is configured differently for different safety criticality — is conceptually adjacent to my graduated governance. But DL usage levels are **design-time static configurations**, not **runtime state-conditioned governance**. The architecture does not dynamically change DL usage level based on classified environmental state.

---

### 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (G(S)) | Yes | Safety control can "discard the suggestion/decision from the decision function and operate according to the fallback function" — effectively G(S) = 0. Triggered by L1/L2 diagnostics or supervision function detecting unsafe AI operation |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | Partial | Supervision function provides "constraints or limits" to the decision function (safe envelope). DL usage levels determine whether AI provides suggestion vs. decision. However, this is static (design-time) not dynamic (runtime state-conditioned) |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | No | No runtime environmental state classification. Level 1 triggered by detected errors/anomalies. Level 2 (safe envelope) is configured at design-time per DL usage level, not dynamically per runtime state |

- **Governance type:** **Level 1 (binary participation) implemented; Level 2 (scope restriction) partially implemented as design-time configuration.** Safety control can disable AI and switch to fallback (binary Level 1). Supervision function constrains AI within safe envelope (partial Level 2). But Level 2 does not vary by runtime environmental state.
- **Binary or graduated:** The architecture supports binary participation governance (AI on → fallback/safe state) and design-time graduated scope (DL usage levels configuring suggestion vs. decision output). But no runtime graduated governance — no CAUTION-equivalent mode where AI participation and scope dynamically adjust based on classified environmental state.
- **Relation to two-level governance pair:** SAFEXPLAIN has the *architectural components* for two-level governance (supervision function ≈ Level 2; safety control ≈ Level 1), but does not *organise* them into a state-conditioned governance pair (G(S), A_AI(S)). The governance is either binary (AI → fallback) or design-time configured (DL usage levels), not dynamically state-conditioned.

---

### 8. Human Role in Decision-Making

- **Human role:** User receives "suggestion or decision" from the decision function depending on DL usage level. Domain experts certify surrogate model rules within AI-FSM lifecycle. Users provide feedback that can inform gatekeeper updates.
- **Decision support vs. automation:** Configurable — higher DL usage levels provide autonomous decisions to actuators; lower levels provide suggestions to users. The DL usage level determines the human-AI authority balance.
- **Override mechanism:** Safety control can override AI output with non-AI fallback. L2/L3 diagnostics can trigger safe state. Supervision function limits AI output to safe envelope.

---

### 9. System Constraints and Environment

- **Real-world constraints:** The framework targets deployment on NVIDIA AGX Orin (high-performance edge platform), addressing computational demands of concurrent AI models.
- **Real-world deployment:** Three case studies in automotive, railway, and space domains — integration on real hardware with middleware support.
- **Resource-aware design:** SAFEXPLAIN middleware manages DL and XAI library integration, supports model optimisation and conversion for target hardware. Not low-resource but resource-conscious.

---

### 10. Hybrid AI Taxonomy

- **Type:** **Supervisory control with diverse redundancy.** AI/ML constituent generates outputs; supervision function provides rule-based safe envelope; safety control integrates AI with non-AI fallback. Additionally, diverse redundancy within AI (multiple DL models with input data transformations).
- **Safety enforcement:** Applied **alongside and after** AI reasoning — supervision function monitors AI inputs/outputs in parallel; safety control makes final decision after AI output.
- **Two-level governance support:** The architecture has the structural components for two-level governance but implements it as binary (Level 1) + design-time scope configuration (partial Level 2), not as runtime state-conditioned graduated governance.
- **Comparison to my architecture:** Both use a deterministic safety layer constraining probabilistic AI. Both have a supervision/gate function between AI output and system action. The key difference: SAFEXPLAIN's governance is binary at runtime (AI on or fallback); my governance is graduated at runtime (SAFE/CAUTION/UNSAFE with different AI scopes).

---

### 11. Baseline Comparison and Evaluation

- **Baselines:** Not evaluated against baselines in this paper (project overview, not experimental paper). Case study results referenced as forthcoming.
- **Evaluation:** Case studies demonstrate successful integration of the framework in automotive (object detection for collision avoidance), railway (ATO with obstacle detection), and space (autonomous mission operations). Evaluation is integration-focused, not comparative.
- **CAUTION zone testing:** Not addressed — no graduated governance modes to test.
- **Safety Dominance verification:** Not addressed — no formal safety property defined.
- **Graduated vs. binary governance comparison:** Not evaluated.

---

### 12. Key Concepts and Definitions

- **AI Functional Safety Management (AI-FSM):** Extended V-model development process incorporating DL-specific lifecycle phases (Data Management, Learning Management, Inference Management) alongside traditional safety development phases. Grounded in IEC 61508, ISO 26262, EASA Concept Paper, AMLAS, A-SPICE for ML, ISO/IEC TR 5469.
- **Supervision function:** Component that bounds AI/ML constituent operations within a predefined safety envelope. Collects information from AI inputs/outputs and provides constraints/limits to the decision function. Key safety architecture element.
- **Safety envelope:** The set of constraints or limits within which the AI/ML constituent is permitted to operate. Defined by the supervision function based on environment appropriateness and AI output monitoring.
- **DL usage levels:** Different levels of AI/DL involvement in safety functions, each with different safety requirements and architectural configurations. The same reference architecture pattern is tailored per DL usage level (details omitted for space in this paper).
- **Decision function:** Aggregates outputs from diverse DL models and supervision components (anomaly detectors, surrogate models, uncertainty-aware models), producing consolidated prediction with trustworthiness score and explanations.
- **Diverse redundancy:** Multiple AI/ML models with diverse input data transformations, combined via decision function (averaging, voting, non-maximum suppression). Used to increase error detection coverage.
- **Surrogate models:** Simplified, interpretable models certified by safety experts that mimic main DL model behaviour. When discrepancy between main model and surrogate exceeds threshold, main model's prediction is rejected.
- **Safe state:** System state the safety control transitions to when diagnostics identify irrecoverable unsafe conditions.

---

### 13. Limitations and Unsolved Problems

- **Stated limitations:**
  - Details of DL usage level configurations omitted for space
  - Case study results forthcoming (paper written before project completion September 2025)
  - No standardised way to adopt V-model arrangement for new DL-specific processes
- **Observable limitations:**
  - No formal mathematical model — architecture described as configurable pattern, not formalised pipeline
  - No environmental state classification — governance is binary (AI → fallback) or design-time (DL usage levels)
  - No runtime graduated governance — DL usage levels are design-time configurations, not runtime state-conditioned modes
  - No formal Safety Dominance Property or equivalent safety guarantee
  - Supervision function "safe envelope" is not formally defined — constraints/limits not specified mathematically
- **Alignment with my research gaps:**
  - **Binary runtime governance confirmed:** Safety control implements AI → fallback as binary switch. No intermediate mode where AI participates under restricted scope.
  - **Design-time vs. runtime scope restriction:** DL usage levels configure output types (suggestion vs. decision) at design time. My A_AI(S) configures output types at runtime based on classified environmental state. Same concept, different activation mechanism.
  - **Supervision function as unformalised Level 2:** The safe envelope concept is structurally equivalent to A_AI(S) — it constrains what AI may output. But it is not formalised, not state-conditioned, and not expressed as a formal containment property.
  - **No Safety Dominance Property:** Despite comprehensive safety architecture, no formal guarantee that AI outputs always fall within state-determined bounds.

---

### 14. Methodology Notes

- **Method:** EU Horizon Europe project (SAFEXPLAIN, grant 101069595, 3-year). Design science approach — framework development + case study integration in automotive, space, railway.
- **Standards alignment:** IEC 61508, ISO 26262, ISO/IEC TR 5469, ISO 8800, EASA Concept Paper, AMLAS, A-SPICE for ML, ISO/IEC 5338.
- **DSR alignment:** Iterative framework development with environment requirements (safety standards) → design (AI-FSM + architecture + platform) → case study validation. Methodologically compatible with my DSR pipeline.

---

### 15. Quotable / Citable Points

1. "DL software is designed monolithically following empirical training processes with example training data, rather than implementing specific safety requirements" (Section I) — foundational tension between DL and safety culture.
2. "Its main goal is to check the appropriateness of the environment and to supervise the output of the ML constituent to identify unsafe situations and stablish the limits for safe operation, providing a safe envelope" (Section III.A.3) — supervision function definition.
3. "According to the DL usage level, the Decision Function might provide a suggestion (e.g., warning message, status information) and/or decision (e.g., command on the actuators)" (Section III.A.2) — DL usage levels governing output type.
4. "If the non-AI subsystem implements a fallback function for the ML constituent, in the event that a functional safety problem is detected in the AI-subsystem, the safety control might decide to discard the suggestion/decision from the decision function and operate according to the fallback function" (Section III.B.3) — binary fallback governance.
5. "The safety control might also limit the output(s) to meet with the safe limits defined in the supervision function or even take the system to a safe state" (Section III.B.3) — output limiting as partial Level 2.

---

### 16. Relation to My Research and Positioning

- **Governance implementation:** Level 1 (binary participation — AI → fallback/safe state) fully implemented. Level 2 (scope restriction — safe envelope, DL usage levels) partially implemented as design-time configuration.
- **State conditioning:** Not implemented at runtime. DL usage levels are design-time. Supervision function triggers are event-based (error/anomaly detection), not state-classified.
- **Two-level governance pair:** The architecture has the structural components (supervision function ≈ A_AI, safety control ≈ G) but does not organise them as a state-conditioned pair (G(S), A_AI(S)).
- **Safety property:** No formal safety property defined. The safe envelope concept is the closest to A_AI(S) but is not formalised.
- **Gap my research addresses:** SAFEXPLAIN demonstrates the most comprehensive available safety architecture for AI in safety-critical systems — spanning development process (AI-FSM), architecture (safety patterns), and platform (middleware). Yet even this comprehensive framework defaults to binary runtime governance (AI or fallback) with design-time scope configuration (DL usage levels). My architecture fills the missing runtime graduated governance layer: S = f(E) classifies environmental state at runtime, and the governance pair (G(S), A_AI(S)) dynamically conditions both AI participation and scope on that classification — enabling a CAUTION mode that SAFEXPLAIN's binary fallback architecture cannot express.

**Positioning paragraph:** SAFEXPLAIN (Abella et al., 2025) is a **major cross-domain safety architecture reference** — the most comprehensive available framework for integrating AI/DL into safety-critical systems, backed by a 3-year EU Horizon Europe project with case studies in automotive, space, and railway. The reference safety architecture pattern (Fig. 3) implements diverse AI redundancy, a supervision function providing a safe envelope, hierarchical diagnostics (L1/L2/L3), a non-AI fallback subsystem, and a safety control function — representing the current state of practice in industry-aligned AI safety architecture. Critically, despite this comprehensiveness, the runtime governance remains binary: the safety control either accepts AI output or switches to fallback/safe state. The supervision function's safe envelope constrains AI output scope, but this constraint is statically configured per DL usage level at design time, not dynamically conditioned on classified environmental state at runtime. The DL usage levels concept — where different criticality levels receive different governance configurations (suggestion vs. decision output types) — is conceptually adjacent to my graduated governance but operates at design time rather than runtime. This paper should be cited as: (a) the most comprehensive cross-domain AI safety architecture reference, confirming binary runtime governance as the industry state of practice; (b) evidence that even the most complete frameworks lack runtime state-conditioned graduated governance; (c) the supervision function / safe envelope concept as an architectural antecedent to my A_AI(S); and (d) the DL usage levels concept as a design-time precursor to my runtime state-conditioned scope restriction. The paper also references Perez-Cerrolaza et al. (2024), already in the tracker, creating a direct citation chain.

---

### 17. Overall Relevance Score

**⭐⭐⭐⭐ High**

**Justification:** This paper addresses three core themes (hybrid AI, safety-critical AI, AI governance) and partially addresses two more (decision architecture, human role). It provides the most comprehensive available safety architecture for AI in safety-critical systems, directly relevant as a cross-domain baseline for comparing against my graduated governance architecture. The supervision function (safe envelope), DL usage levels (design-time scope configuration), and binary fallback governance provide precise comparison points. The paper's grounding in functional safety standards (IEC 61508, ISO 26262) and cross-domain case studies (automotive, space, railway) give it strong credibility. Elevated to ⭐⭐⭐⭐ because: (a) it represents the industry state of practice in AI safety architecture, (b) its supervision function / safe envelope is the closest existing concept to my A_AI(S), (c) it directly extends Perez-Cerrolaza et al. (2024) already in the tracker, and (d) the gap between its design-time DL usage levels and my runtime state-conditioned governance is precisely the gap my research fills.

---

### Recommended Citation Uses

| Use | Section in dissertation | Specific point |
|---|---|---|
| Industry state of practice in AI safety architecture | Literature review — safety-critical AI architecture | Most comprehensive cross-domain framework (automotive, space, railway); supervision function, diverse redundancy, hierarchical diagnostics, fallback |
| Binary runtime governance evidence | Research gap — binary governance gap | Even the most comprehensive AI safety framework defaults to binary AI → fallback at runtime |
| Supervision function / safe envelope as Level 2 antecedent | Architecture comparison | Safe envelope = static output constraint ≈ unformalised A_AI; my A_AI(S) = dynamic state-conditioned scope restriction |
| DL usage levels as design-time scope precursor | Gap identification — design-time vs. runtime | DL usage levels configure suggestion vs. decision at design time; my (G(S), A_AI(S)) does this at runtime conditioned on S = f(E) |
| AI-FSM development process | Methodology alignment | Extended V-model with DL lifecycle phases; relevant to my DSR approach for AI system development |
| Standards landscape | Background — functional safety standards | IEC 61508, ISO 26262, ISO/IEC TR 5469, ISO 8800, EASA, AMLAS coverage |
| Citation chain with Perez-Cerrolaza et al. (2024) | Literature coherence | SAFEXPLAIN cites and extends Perez-Cerrolaza survey; creates traceable chain from survey → framework → gap → my architecture |
