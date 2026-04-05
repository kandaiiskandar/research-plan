# Literature Review Extraction
## Paper: Artificial Intelligence in Process Safety: A Review of Opportunities, Challenges, and Future Directions for the Chemical Process Industries

---

## Early Relevance Check: PASSED — Proceed with Full Extraction

1. **Addresses core themes?** Yes — safety-critical AI decision-making, AI governance/control mechanisms, human role in decision-making
2. **Contributes to relevant areas?** Yes — proposes a four-dimensional taxonomy (safety function × intelligence type × autonomy level × assurance maturity) for classifying AI contributions to safety-critical operations
3. **Citable in literature review?** Yes — the autonomy-level taxonomy and functional safety alignment discussion provide background on how current practice structures AI governance in safety-critical domains, and confirm the binary/advisory paradigm

---

## 1. Paper Identity

- **Title:** Artificial intelligence in process safety: A review of opportunities, challenges, and future directions for the chemical process industries
- **Authors:** D. Christopher Selvam, T. Raja, Divyesh Rameshbhai Vaghela, Mansingh Meena, Sasmeeta Tripathy, Bhavan Kumar, Honganur Raju Manjunath, Kulmani Mehar, Yuvarajan Devarajan
- **Year:** 2026 (Published online 6 January 2026; accepted 6 January 2026)
- **Venue:** Journal of Loss Prevention in the Process Industries, Volume 100, Article 105917
- **DOI:** https://doi.org/10.1016/j.jlp.2026.105917
- **Type:** Review paper (18 pages); part of special issue "Process Safety in the Era of AI"

---

## 2. Core Contribution

- **Problem addressed:** The literature on AI for process safety in Chemical Process Industries (CPIs) is fragmented across three dimensions: (i) applications are categorised by safety function or algorithm type without linking to autonomy levels or assurance maturity; (ii) "AI for safety" and "safety of AI" are treated as independent subjects; (iii) reviews end with generic recommendations rather than structured research agendas.

- **Proposed solution / key finding:** A four-dimensional framework that classifies AI contributions to process safety according to:
  1. **Process-safety function** — hazard identification, monitoring/early warning, barrier/asset management, learning/governance
  2. **Type of intelligence** — descriptive, diagnostic, predictive, prescriptive
  3. **Level of autonomy** — advisory, human-in-the-loop, semi-autonomous, safety-critical closed-loop
  4. **Assurance maturity** — from ad-hoc tools to safety-certifiable solutions

- **Main contributions:**
  1. Four-dimensional taxonomy integrating safety function, intelligence type, autonomy level, and assurance maturity
  2. Lifecycle-oriented mapping of AI applications across HAZID, risk analysis, operational monitoring, and post-event learning
  3. Analysis of "safety of AI" as an emergent hazard category requiring functional safety alignment
  4. Five grand challenges for AI in process safety: safety data ecosystems, safety-certifiable AI / AI-SIL, human-centred autonomy, cyber-secure AI architectures, digital-twin-enabled dynamic risk assessment
  5. Phased roadmap (short/medium/long-term) for AI integration in process safety

- **What is novel:** The explicit integration of autonomy levels and assurance maturity into a process-safety-specific AI taxonomy. The concept of "AI Safety Integrity Level" (AI-SIL) as an analogue to traditional SIL for learning systems.

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | **Partial** | Describes hybrid architectures where deterministic safety PLCs and hardwired logic retain authority over emergency actions while AI modules generate advisory or predictive outputs. Also discusses hybrid physics-based + data-driven prognostic models. Not formalised as a hybrid architecture. |
| Safety-critical AI decision-making | **Yes** | Core topic. Covers AI applications across the entire process safety lifecycle in CPIs — hazard identification, dynamic risk assessment, barrier management, early warning, and post-event learning. |
| AI governance / control mechanisms | **Yes** | Proposes a four-level autonomy taxonomy (advisory → human-in-the-loop → semi-autonomous → safety-critical closed-loop). Discusses functional safety alignment with IEC 61508/61511. Proposes the concept of AI-SIL for certifying AI in safety functions. |
| Low-resource environments | **No** | Focus is on heavily instrumented refineries, petrochemical plants, LNG facilities, and chemical warehouses with extensive DCS/SIS/IIoT infrastructure. No discussion of limited data, connectivity, or compute constraints. |
| Decision architecture formalisation | **No** | The four-dimensional taxonomy is conceptual/descriptive, not formalised mathematically. No state variables, gate functions, or formal safety properties are defined. |
| Human role in decision-making | **Yes** | Substantial discussion of human-AI collaboration, cognitive overload from alarm floods, automation bias, adaptive decision-support interfaces, XAI for operator trust, and the imperative that human operators retain authority over safety-critical actions. |
| Socio-technical evaluation | **Partial** | Discusses human factors, safety culture, organisational barriers to AI adoption, ethical accountability, and regulatory governance. Does not conduct empirical socio-technical evaluation. |
| Coastal fisheries / maritime domain | **No** | Entirely focused on chemical process industries — refineries, petrochemical plants, LNG storage, chemical warehousing. |

**Mid-Extraction Relevance Gate:** 3 Yes + 2 Partial → **FULL EXTRACTION**

---

## 4. Decision Architecture Analysis

- **Decision-making structure:** The paper does not propose a specific decision architecture. It describes a **lifecycle-oriented, layered integration model** where AI capabilities are mapped across four lifecycle phases (hazard studies → risk analysis → operational monitoring → post-event learning), with each phase characterised by its intelligence type and autonomy level.

- **Safety constraint mechanisms:** The paper describes a **functional safety alignment** model where:
  - AI modules generate advisory or predictive outputs
  - Deterministic safety PLCs and hardwired logic retain ultimate authority over emergency procedures
  - AI influence on operational thresholds, maintenance priorities, or alarm configurations is "strictly regulated through well-defined envelopes and override protocols"
  - Interventions that directly activate safety functions "still necessitate high assurance maturity and explicit human authorisation"

- **Rule-based constraints before AI?** Yes — the hybrid architecture described places deterministic safety logic (PLCs, hardwired interlocks) as the authoritative layer, with AI as an advisory/predictive layer that cannot autonomously override safety-instrumented functions.

- **Boundary between deterministic control and AI:** Defined through the autonomy levels: advisory and human-in-the-loop autonomy keeps AI outputs subordinate to human decision; semi-autonomous AI may adjust operating limits within "established constraints"; safety-critical closed-loop control requires the highest assurance maturity. The paper explicitly states that most current applications operate within advisory or human-in-the-loop frameworks.

- **Failure modes and fallback:** The paper discusses AI-specific failure modes: model drift, sensor inaccuracies, data quality degradation, adversarial tampering, and out-of-distribution scenarios. Proposes that AI models should operate under "continuous performance monitoring and predefined fallback protocols." Does not formalise fallback behaviour.

---

## 5. Formal Model and Mathematical Representation

- **Formal model defined?** No. The paper is entirely descriptive/taxonomic. No mathematical representation of the decision system, safety states, gate functions, or action spaces is provided.

- **Comparison to E → S = f(E) → (G(S), A_AI(S)) → AI(E):** No comparable pipeline exists. The four-dimensional taxonomy (function × intelligence × autonomy × assurance) is a classification framework, not a formal decision pipeline. It does not define:
  - An environmental state vector
  - A safety state classification function
  - A gate function controlling AI participation
  - A state-conditioned admissible action space

- **State-dependent recommendation restriction?** Not formalised. The autonomy levels imply that AI's scope changes (advisory → semi-autonomous → closed-loop), but this is framed as a design-time configuration choice, not as a runtime state-conditioned restriction. There is no mechanism where the same AI system dynamically restricts its own output types based on classified environmental safety state.

- **Safety Dominance Property equivalent?** Not defined. The concept of "well-defined envelopes and override protocols" is conceptually related but is not formalised as a property guaranteeing AI(E) ⊆ A_AI(S).

- **Formalisation purpose:** N/A — purely descriptive taxonomy.

---

## 6. Safety State Classification

- **Discrete risk/safety levels?** The paper references SIL (Safety Integrity Levels) from IEC 61508/61511 and proposes the concept of "AI-SIL" for AI-specific safety certification. However, these are design-time integrity classifications, not runtime environmental safety state classifications.

- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:** The paper does not classify runtime environmental conditions into discrete safety states. The four autonomy levels (advisory, human-in-the-loop, semi-autonomous, safety-critical closed-loop) describe the design-time configuration of AI involvement, not a runtime safety state function. There is no dynamic transition between autonomy levels based on classified environmental conditions.

- **Does AI recommendation scope change across safety levels?** Not in a state-conditioned sense. The autonomy level determines the *design-time ceiling* on what AI may do (e.g., advisory AI recommends; semi-autonomous AI adjusts setpoints under constraints). But this is fixed by system design, not dynamically adjusted based on environmental safety state.

- **CAUTION mode equivalent?** **Not present.** The taxonomy's intermediate autonomy levels (human-in-the-loop, semi-autonomous) resemble the concept of graduated AI engagement, but they are structural design choices, not runtime operating modes that activate or deactivate based on environmental conditions. There is no state where a system dynamically transitions from full AI scope to restricted AI scope in response to deteriorating environmental conditions.

---

## 7. Governance Level Analysis

| Level | Question | Implemented? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (G(S)) | **Partial** | Deterministic PLCs retain authority over safety-critical actions. AI may be excluded from closed-loop safety functions if assurance maturity is insufficient. But this exclusion is a design-time decision, not a runtime gate conditioned on environmental state. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | **Partial** | The autonomy taxonomy implicitly restricts AI scope: advisory AI can only recommend; semi-autonomous AI can adjust within constraints. But this restriction is fixed by design configuration, not dynamically conditioned on classified environmental safety state. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | **No** | Neither participation nor advisory scope is conditioned on a runtime environmental safety state function. Governance is determined by design-time autonomy level assignment and assurance maturity. |

- **Binary or graduated?** The taxonomy is **graduated by design** (four autonomy levels), but this graduation is a **static design-time classification**, not a runtime state-conditioned governance model. At runtime, the AI operates at its assigned autonomy level regardless of environmental conditions.

- **Level 2 governance present?** Partially — the autonomy levels constrain what AI may do (recommend vs. adjust vs. control), but these constraints are static, not state-conditioned.

- **Support or contradict two-level governance?** The paper **partially supports** the concept by demonstrating that industry recognises the need for graduated AI governance beyond binary on/off. The four autonomy levels acknowledge that different situations require different degrees of AI involvement. However, the paper does not propose making this graduation *dynamic* or *state-conditioned*, which is the core innovation of my architecture. The gap between design-time autonomy levels and runtime state-conditioned governance is precisely the space my research occupies.

---

## 8. Human Role in Decision-Making

- **Human involvement:** Central to the paper's framework. The paper explicitly states that "human operators maintain an irreplaceable role in overseeing safety-critical scenarios, particularly in the presence of novel or ambiguous circumstances." AI integration must "emphasize collaboration rather than substitution."

- **Decision support vs. automation:** Predominantly **decision support**. Most current AI applications in CPIs operate at advisory or human-in-the-loop levels. Semi-autonomous applications (e.g., automatically modifying operating limits) exist but are constrained. Safety-critical closed-loop AI remains aspirational and requires the highest assurance maturity.

- **Human-AI interaction:** The paper discusses: XAI dashboards providing transparent rationale for recommendations; AI-enhanced alarm management that filters nuisance alarms and prioritises by risk significance; adaptive interfaces that adjust information density to operator workload; reinforcement learning agents presenting prioritised response arrays with predicted outcomes and confidence metrics.

- **Override/escalation:** AI interventions that activate safety functions require "explicit human authorisation." Deterministic safety PLCs and hardwired logic retain ultimate authority. The paper emphasises the need for "clearly delineated handover junctures between human and machine decision-making."

- **Relevance to my research:** The paper's emphasis on human-AI collaboration, cognitive overload mitigation, and mandatory human oversight for safety-critical actions aligns strongly with my decision support model. The discussion of alarm fatigue from binary safety systems supports the motivation for graduated governance — providing operators with useful restricted-scope advice (CAUTION mode) rather than overwhelming them with either full AI output or no AI output.

---

## 9. System Constraints and Environment

- **Real-world constraints:** Focused on data-rich industrial environments with DCS, SIS, IIoT sensor networks, and SCADA platforms. Discusses data quality challenges (sparse incident data, biased datasets, proprietary restrictions, inconsistent reporting formats). Mentions computational infrastructure requirements for continuous data streaming and DL model execution.

- **Deployment context:** Refineries, petrochemical plants, LNG facilities, chemical warehouses — all high-infrastructure industrial environments. Case studies demonstrate pilot-scale deployment (e.g., Middle Eastern refinery, hydrocracker units, gas processing plants).

- **Resource-aware design:** Not a focus. The paper addresses data scarcity for rare events but not computational or connectivity constraints. No discussion of offline capability, graceful degradation, or lightweight models for low-resource deployment.

- **Low-resource gap:** The paper's entire context assumes heavily instrumented industrial facilities with continuous data infrastructure. My research's low-resource, developing-nation context (limited data, intermittent connectivity, non-expert users, low computational budgets) is entirely outside this paper's scope.

---

## 10. Hybrid AI Taxonomy

- **Hybrid approach type:** The paper describes two hybrid patterns:
  1. **Supervisory control / constitutional architecture:** Deterministic safety PLCs and hardwired logic retain authority; AI modules generate advisory/predictive outputs governed by "well-defined envelopes and override protocols"
  2. **Physics-informed hybrid models:** Physics-based models capture known failure mechanisms (fatigue, fouling, creep) while data-driven models identify plant-specific patterns, combining to estimate degradation rates

- **Safety enforcement location:** Primarily **after** and **alongside** AI reasoning. Safety PLCs operate in parallel as the authoritative layer. AI outputs are subject to operator validation before implementation. For safety-critical functions, deterministic logic overrides AI outputs.

- **Two-level governance support?** The paper's hybrid architecture implicitly implements Level 1 governance (deterministic PLCs can override AI entirely) but does not implement state-conditioned Level 2 governance (AI advisory scope is not dynamically restricted based on environmental safety state). The autonomy taxonomy provides a graduated design-time framework but not a runtime governance mechanism.

- **Comparison to my architecture:** The paper's hybrid architecture (deterministic authority + AI advisory) is structurally similar to my architecture's deterministic gate + AI reasoning pipeline. However, the paper's governance is design-time static (fixed autonomy level), whereas mine is runtime dynamic (state-conditioned). The paper lacks the S = f(E) → (G(S), A_AI(S)) pipeline that makes governance responsive to environmental conditions.

---

## 11. Baseline Comparison and Evaluation

- **Baseline comparisons:** The paper synthesises reported improvements from individual studies: 30–60% improvement in anomaly detection, 45% false alarm reduction (LSTM in refineries), 30% improvement in compressor-surge precursor identification, 40% faster leak detection, 25% improvement in fault prediction accuracy. These compare AI-enhanced approaches against traditional threshold-based monitoring.

- **CAUTION zone testing?** Not present. No evaluation tests an intermediate mode where AI participates under restriction. Evaluations compare AI-on vs. traditional (no AI) approaches — a binary comparison.

- **Safety Dominance Property verification?** Not addressed. No evaluation verifies that AI outputs remain within state-determined bounds under graduated governance.

- **Graduated vs. binary governance comparison?** Not conducted. The paper proposes four autonomy levels but does not evaluate whether graduated autonomy outperforms binary control.

- **Evaluation gaps relevant to my research:**
  - No evaluation of state-conditioned dynamic governance
  - No comparison of graduated vs. binary governance approaches
  - No testing of AI behaviour under environmental state transitions
  - No evaluation in low-resource or non-industrial contexts
  - Case studies are limited to high-infrastructure CPI facilities

---

## 12. Key Concepts and Definitions

- **Four-dimensional AI-safety taxonomy:** Classification of AI contributions by (1) process-safety function, (2) intelligence type (descriptive/diagnostic/predictive/prescriptive), (3) autonomy level (advisory/human-in-the-loop/semi-autonomous/safety-critical closed-loop), (4) assurance maturity (ad-hoc to certifiable)

- **AI Safety Integrity Level (AI-SIL):** Proposed concept linking AI model performance metrics, uncertainty thresholds, retraining triggers, and monitoring requirements to PSM decision thresholds. Analogous to traditional SIL (IEC 61508) but specific to learning systems. Not yet formalised or standardised.

- **Assurance maturity continuum:** Progression from ad-hoc AI tools to safety-certifiable AI solutions. Current practice is mostly at the ad-hoc/advisory end; the paper argues for structured progression toward certifiable AI.

- **"Living" risk assessments / "living HAZOPs":** Dynamic hazard registers continuously updated as operating conditions, process configurations, or organisational practices change — contrasted with traditional static, periodic assessments.

- **Hybrid architecture (PLC authority + AI advisory):** Safety-critical design pattern where deterministic PLCs retain authority over emergency procedures while AI provides advisory/predictive intelligence within defined envelopes.

- **Grand challenges:** Safety data ecosystems; safety-certifiable AI/AI-SIL; human-centred autonomy; cyber-secure AI architectures; digital-twin-enabled dynamic risk assessment.

---

## 13. Limitations and Unsolved Problems

- **Stated limitations:**
  - Sparse and biased incident datasets; data imbalance for rare events (<0.01% of records)
  - Limited model interpretability (black-box DL systems)
  - Difficulty validating AI under actual plant conditions
  - Regulatory ambiguities — existing standards (IEC 61508/61511) do not address learning behaviour, model updates, or drift
  - Organisational resistance and siloed safety/IT functions
  - Cybersecurity vulnerabilities from IIoT and cloud-based AI systems
  - No universally endorsed framework for AI performance/reliability in safety-instrumented systems

- **Unsolved problems / future work:**
  - Formal AI-SIL concept and certification workflows
  - Standardised benchmark datasets and performance metrics for AI in process safety
  - Human-AI collaboration patterns balancing automation bias and cognitive overload
  - Integrated cyber-process anomaly detection
  - Digital-twin-enabled dynamic risk assessment integrated into existing bow-tie/LOPA frameworks

- **Gaps my architecture addresses:**
  - **Two-level governance model:** The paper's autonomy taxonomy is design-time static. My architecture provides runtime, state-conditioned governance where both AI participation (G(S)) and advisory scope (A_AI(S)) dynamically respond to classified environmental conditions.
  - **CAUTION mode:** The paper identifies that most AI applications operate at advisory level but does not formalise intermediate operating modes where AI participation is permitted but scope-restricted based on environmental risk. My CAUTION state fills this gap.
  - **Formal safety properties:** The paper calls for "quantitative performance objectives" and "formal or semi-formal verification of essential properties" but does not define any. My Safety Dominance Property (AI(E) ⊆ A_AI(S)) provides exactly this.
  - **Low-resource deployment:** The paper is entirely scoped to high-infrastructure industrial environments. My architecture is designed for low-resource, developing-nation contexts with limited data, connectivity, and computing.
  - **Dynamic state-conditioned governance:** The paper's autonomy levels are fixed at design time. My S = f(E) function enables runtime transitions between governance modes based on environmental conditions — a capability the paper does not propose but implicitly motivates through its discussion of dynamic risk assessment needs.

---

## 14. Methodology Notes

- **Research method:** Narrative/systematic literature review with proposed conceptual framework. The paper synthesises existing applications, proposes a four-dimensional taxonomy, and derives a phased roadmap for future research.

- **Alignment with DSR?** Not directly. The paper does not follow a Design Science Research methodology — it does not design, formalise, prototype, or evaluate an artefact. It is a literature synthesis with a conceptual framework.

- **Methodological insights for my research:**
  - The autonomy-level taxonomy (advisory → human-in-the-loop → semi-autonomous → closed-loop) provides useful vocabulary for positioning my architecture's CAUTION mode. My CAUTION state can be characterised as enabling "advisory with restricted scope" or "human-in-the-loop with state-conditioned advisory boundary."
  - The paper's call for AI-SIL concepts aligns with my Safety Dominance Property as a formal safety assurance mechanism.
  - The phased roadmap approach (foundational readiness → assurance/integration → trusted autonomy) could inform how I frame the maturity trajectory of my architecture.

---

## 15. Quotable / Citable Points

1. **AI as advisory, not autonomous, in current practice:** The paper states that "most contemporary applications still operate within an advisory or human-in-the-loop framework, generating early warnings, risk assessments, and suggested interventions that require operator validation before implementation." Citable as evidence that safety-critical AI governance remains predominantly at Level 1 advisory. *(Section 3.3)*

2. **Deterministic authority over safety functions:** "AI modules generate advisory or predictive outputs, while deterministic safety PLCs and hardwired logic maintain ultimate authority over emergency procedures." Citable as the dominant hybrid pattern in safety-critical CPIs. *(Section 6.2)*

3. **AI-SIL concept:** The paper proposes "developing an AI-specific Safety Integrity Level (AI-SIL) concept" that would "align model performance metrics, uncertainty thresholds, retraining triggers, and monitoring requirements with the risk thresholds used in PSM decision-making." Citable as an emerging concept that my Safety Dominance Property could contribute to. *(Section 8.4)*

4. **False alarm problem:** LSTM-based anomaly detection in refineries "can reduce false alarms by approximately 45%." Citable as evidence that binary alarm systems generate excessive false positives, motivating graduated governance. *(Section 5.2)*

5. **Autonomy governance gap:** "No universally endorsed framework defines performance or reliability benchmarks for AI in safety-instrumented systems. Existing standards such as IEC 61508, IEC 61511, and ISO 13849 ... do not explicitly address learning behaviour, model updates, or drift detection." Citable as evidence of the governance gap my architecture addresses. *(Section 8.4)*

---

## 16. Relation to My Research and Positioning

- **Governance level implemented:** Level 1 governance (participation control) via deterministic PLC authority over safety functions. Partial Level 2 governance through the autonomy taxonomy (advisory/HitL/semi-autonomous/closed-loop), but this is design-time static, not runtime state-conditioned.

- **Level 2 state-conditioned?** No. The autonomy levels determine what AI *may* do at design time, not what AI *does* do in response to runtime environmental conditions.

- **Proximity to (G(S), A_AI(S))?** The paper's hybrid architecture (deterministic authority + AI advisory within envelopes) captures the *spirit* of G(S) and A_AI(S) but does not formalise either. There is no environmental state classification function S = f(E), no gate function conditioned on safety state, and no state-dependent restriction of AI recommendation types.

- **Formal safety property?** The paper proposes AI-SIL as a concept but does not define a formal property. My Safety Dominance Property (AI(E) ⊆ A_AI(S)) would be a concrete instantiation of the kind of formal assurance the paper calls for.

- **Gap my research fills:** The paper demonstrates that the process safety community recognises the need for graduated AI governance (four autonomy levels) and formal safety assurance (AI-SIL), but provides neither a runtime state-conditioned governance mechanism nor a formal safety property. My architecture fills both gaps: the two-level governance pair (G(S), A_AI(S)) makes governance dynamic and state-conditioned, and the Safety Dominance Property provides the formal assurance the paper calls for.

- **Positioning paragraph:** This paper serves as **domain background and partial motivation** for my research. Its four-dimensional taxonomy demonstrates that the process safety community has progressed beyond binary thinking about AI governance — four autonomy levels are recognised as necessary — but the graduation remains a *design-time configuration choice*, not a *runtime state-conditioned mechanism*. The paper's call for AI-SIL concepts, dynamic risk assessment, and formal safety assurance directly motivates my contributions: the Safety Dominance Property operationalises the formal assurance that AI-SIL requires, and the (G(S), A_AI(S)) governance pair makes autonomy-level governance responsive to runtime environmental conditions. The paper's focus on high-infrastructure CPIs (refineries, LNG, petrochemicals) contrasts sharply with my low-resource coastal fisheries context, reinforcing the argument that my architecture addresses an underserved deployment environment. The paper's discussion of cognitive overload from binary alarm systems and the need for human-centred AI design further supports the motivation for my CAUTION mode as a cognitively appropriate intermediate between full AI and no AI.

---

## 17. Overall Relevance Score

### ⭐⭐ Low

**Justification:** This paper provides useful background on how AI governance is conceptualised in a parallel safety-critical domain (CPIs) and confirms that the current paradigm is predominantly advisory/binary with no formalised state-conditioned governance. The four-level autonomy taxonomy and AI-SIL concept are conceptually relevant. However, the paper is entirely descriptive (no formal model, no architecture, no evaluation), focuses on a different domain (CPIs, not maritime/fisheries), assumes high-infrastructure environments (opposite of my low-resource context), and does not propose or identify the specific two-level state-conditioned governance gap that is central to my contribution. It can be cited as background on how graduated autonomy is conceptualised in adjacent domains, and to show that even where graduation is recognised, it remains design-time static rather than runtime dynamic. Its contribution to my literature review is limited to supporting motivation and domain contrast.
