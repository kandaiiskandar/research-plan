---
title: "INSYTE: A Classification Framework for Traditional to Agentic AI Systems"
authors: "Zoe Porter, Radu Calinescu, Ernest Lim, Victoria Hodge, Philippa Ryan, Simon Burton, Ibrahim Habli, Tom Lawton, John McDermid, John Molloy, Helen Monkhouse, Phillip Morgan, Paul Noordhof, Colin Paterson, Isobel Standen, Jie Zou"
year: 2025
venue: "ACM Transactions on Autonomous and Adaptive Systems, Volume 20, Issue 3"
type: "conceptual framework"
relevance: "⭐⭐⭐"
source: "papers/sources/INSYTE- A Classification Framework for Traditional to Agentic AI Systems.pdf"
images: "notes/images/insyte-a-classification-framework-for-traditional-to-agentic-ai-systems/"
extracted: "2026-04-05"
---

## Figures

| File | Description |
|------|-------------|
| ![fig](images/insyte-a-classification-framework-for-traditional-to-agentic-ai-systems/radar_chart_example.png) | Illustrative INSYTE radar chart showing 8-axis pattern for a hypothetical AI system |
| ![fig](images/insyte-a-classification-framework-for-traditional-to-agentic-ai-systems/online_tool_worksheet.png) | INSYTE online tool: worksheet for dimension assessment and radar chart generation |
| ![fig](images/insyte-a-classification-framework-for-traditional-to-agentic-ai-systems/clara_healthcare_radar.png) | INSYTE pattern for CLARA clinical conversational AI (single variant) |
| ![fig](images/insyte-a-classification-framework-for-traditional-to-agentic-ai-systems/clara_variants_comparison.png) | Side-by-side comparison of two CLARA variants |
| ![fig](images/insyte-a-classification-framework-for-traditional-to-agentic-ai-systems/clara_four_variants_overlay.png) | Overlay of four CLARA variant patterns showing progressive capability expansion |
| ![fig](images/insyte-a-classification-framework-for-traditional-to-agentic-ai-systems/scanner_variants_overlay.png) | Overlay of four solar farm inspection robot (SCANNER) variant patterns |

---

## Early Relevance Check: PASSED

1. Does this paper address at least one core research theme? **Yes** — AI governance/control mechanisms (Dimensions 7–8), human role in decision-making, socio-technical evaluation.
2. Does it contribute to safety-critical AI architecture, governance, hybrid AI, etc.? **Yes** — classifies AI governance dimensions; informs safety engineering and regulatory classification.
3. Could it be cited in a literature review about graduated AI governance? **Yes** — its separation of intervention from oversight independence validates multi-dimensional governance thinking.

**Result: 3 Yes, 3 Partial → FULL EXTRACTION**

---

### 1. Paper Identity

- **Title:** INSYTE: A Classification Framework for Traditional to Agentic AI Systems
- **Authors:** Zoe Porter, Radu Calinescu, Ernest Lim, Victoria Hodge, Philippa Ryan, Simon Burton, Ibrahim Habli, Tom Lawton, John McDermid, John Molloy, Helen Monkhouse, Phillip Morgan, Paul Noordhof, Colin Paterson, Isobel Standen, Jie Zou
- **Year:** 2025
- **Venue:** ACM Transactions on Autonomous and Adaptive Systems, Vol. 20, No. 3
- **Type:** Conceptual framework with evaluation study
- **DOI:** https://doi.org/10.1145/3760424

### 2. Core Contribution

- **Problem:** Existing classification frameworks for AI and autonomous systems — particularly unidimensional Levels of Autonomy (LoA) — are rigid, coarse-grained, sector-specific, prone to misuse, and unable to capture the diverse characteristics of modern AI systems, especially agentic AI systems powered by frontier models.

- **Solution:** INSYTE — a multi-dimensional classification framework comprising 8 dimensions across 4 categories, each rated on a 0–5 scale and visualised as a radar chart pattern. The four categories are:
  1. **System Design:** Underspecification (Dim 1), Adaptiveness (Dim 2)
  2. **System Functionality:** Breadth (Dim 3), Depth (Dim 4)
  3. **Operating Environment:** Environmental Diversity (Dim 5), Environmental Dynamism (Dim 6)
  4. **Operational Independence:** Independence from Intervention (Dim 7), Independence from Oversight (Dim 8)

- **Main contributions:**
  1. Eight-dimension classification framework with 6^8 possible system patterns
  2. A systematic process for determining a system's level on each dimension
  3. Radar chart visualisation ("INSYTE pattern") for immediate visual comparison
  4. Freely available online tool (worksheet + chart generator)
  5. Two-round evaluation with 16 participants from diverse domains

- **What is novel:** Multi-dimensional (vs. unidimensional LoA); covers full spectrum from traditional rule-based to agentic AI; explicitly separates intervention independence from oversight independence; includes underspecification and adaptiveness as first-class dimensions; aligns with OECD AI system definition adopted by EU AI Act and other jurisdictions; domain-agnostic applicability.

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | Partial | Dimension 1 (Underspecification) classifies systems from fully rule-based (Level 0) to fully learned/underspecified (Level 5), providing a taxonomy that implicitly captures hybrid systems at intermediate levels (Levels 1–2) |
| Safety-critical AI decision-making | Partial | Framework is designed to classify safety-critical AI systems; Section 6.2.5 discusses INSYTE's use for safety engineering and hazard/risk identification through INSYTE pattern analysis |
| AI governance / control mechanisms | Yes | Dimensions 7 (intervention independence) and 8 (oversight independence) directly classify the degree of human governance over AI systems; Section 6.2.6 discusses regulatory classification applications |
| Low-resource environments | No | Not addressed; framework is domain-agnostic but has no specific low-resource orientation |
| Decision architecture formalisation | Partial | The 8-dimension × 6-level framework is a formal classification model with radar chart visualisation, but classifies systems externally rather than modelling their internal decision pipeline |
| Human role in decision-making | Yes | Dimensions 7 and 8 explicitly classify the human role from continuous control (Level 0) to full autonomy (Level 5); Dim 7 Levels 2–3 distinguish decision support from decision direction |
| Socio-technical evaluation | Yes | Two-round evaluation with 16 participants assessed usability and usefulness; Section 6.2.2 discusses cross-stakeholder communication value |
| Coastal fisheries / maritime domain | No | Maritime referenced in related work (Bureau Veritas, IMO autonomous vessel frameworks) but not a focus domain |

**Mid-Extraction Gate:** 3 Yes + 3 Partial → **FULL EXTRACTION**

### 4. Decision Architecture Analysis

INSYTE is a **classification framework**, not a decision architecture. It does not structure how AI decisions are made; it classifies AI systems along 8 dimensions describing their characteristics.

- **No layered decision-making architecture** — the framework classifies systems but does not prescribe how they should make decisions internally.
- **No safety constraint mechanism or governance structure** controlling how decisions are made at runtime.
- **No rule-based constraints applied before AI reasoning** — INSYTE's Dimension 1 (Underspecification) describes whether a system uses rules vs. learning, but does not mandate a rule-based pre-check layer.
- **No boundary between deterministic control and AI reasoning** is enforced — the framework describes where systems fall on the rule-based ↔ learned spectrum but does not enforce architectural boundaries.
- **Failure modes and fallback:** Dimension 2 (Adaptiveness) classifies how systems handle uncertainty and change, from no adaptation (Level 0) to proactive resilience (Level 5). This describes adaptive capability but does not define fallback architecture.

**Key distinction:** INSYTE could be used to classify a system that implements gate-first governance (e.g., my architecture), but it does not itself define or prescribe such governance.

### 5. Formal Model and Mathematical Representation

- **Formal model:** INSYTE defines a classification model: 8 dimensions × 6 levels (0–5) = 6^8 ≈ 1.68 million possible classification patterns. Each system is represented as an 8-tuple of levels visualised on a radar chart. No mathematical model of a decision system is defined.

- **No state variables, gate functions, or action spaces** — the framework classifies system properties, not runtime decision logic.

- **Comparison to E → S = f(E) → (G(S), A_AI(S)) → AI(E):** INSYTE operates at a completely different level of abstraction. It classifies a system's characteristics externally and statically, whereas my pipeline models the internal runtime decision logic. INSYTE could describe a system that implements my pipeline (e.g., characterising its underspecification, adaptiveness, and operational independence levels), but it does not model the pipeline itself.

- **No state-dependent recommendation restriction** — INSYTE does not model how permitted AI outputs change across safety states. Its classification is static for a given system configuration.

- **No Safety Dominance Property** — no formal guarantee that AI outputs fall within state-determined bounds.

- **Formalisation purpose:** Descriptive and evaluative — the framework provides a structured vocabulary for classifying and comparing AI systems, not for proving safety properties.

### 6. Safety State Classification

- INSYTE **does not classify environmental or operational conditions** into discrete safety levels at runtime. It classifies system characteristics (properties of the system's design and deployment context), not operational states.

- Dimensions 5 (Environmental Diversity) and 6 (Environmental Dynamism) characterise the **complexity of the operating environment** as a system property, not as a runtime state classification trigger. A system operating in a Level 5 dynamic environment faces frequent, rapid, high-magnitude changes — but INSYTE does not define how this should trigger governance responses.

- **No analogue to S = f(E) → {SAFE, CAUTION, UNSAFE}** — the framework does not classify runtime environmental conditions into safety states that control AI behaviour.

- **No differentiation of AI recommendation scope across safety levels.** INSYTE's Dimension 7 classifies whether the system is positioned as decision support (Level 2), decision direction (Level 3), or autonomous (Level 5), but this classification is static — it does not change based on environmental conditions.

- **Critical gap:** INSYTE classifies a system's overall independence level but does not model how that independence should vary with environmental state. My architecture fills this gap by making AI participation (G(S)) and advisory scope (A_AI(S)) functions of classified environmental state S.

### 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (equivalent to G(S)) | Partial | Dimension 7 classifies the degree of AI independence from intervention on a 0–5 scale, with Level 0 = continuous human intervention required. This describes participation levels but does not implement a runtime gate function. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (equivalent to A_AI(S)) | No | INSYTE does not classify or constrain what types of outputs AI may generate under different conditions. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | No | INSYTE classifies system properties statically; it does not model runtime governance conditioned on environmental state. |

- **Binary AI switch vs. graduated governance:** INSYTE's Dimension 7 describes a **gradient from full human control (Level 0) to full autonomy (Level 5)**, with intermediate levels including decision support (Level 2: "informs human decision making") and decision direction (Level 3: "directs human decision making"). This is a **classification of governance levels**, not an implementation of graduated governance. The separation of Dim 7 (intervention) from Dim 8 (oversight) is conceptually related to separating governance into multiple dimensions, but it classifies rather than implements.

- **No Level 2 governance** (advisory scope) is defined — INSYTE does not model what types of recommendations AI may generate.

- **Supports the idea of multi-dimensional governance:** The explicit separation of intervention independence (Dim 7) from oversight independence (Dim 8) validates the principle that governance should not be collapsed into a single dimension. This supports my approach of separating participation governance (G(S)) from advisory scope governance (A_AI(S)) as distinct governance mechanisms.

- **Does not support or contradict (G(S), A_AI(S)) directly** — INSYTE operates at the classification level rather than the architectural level. A system implementing my two-level governance pair could be classified on INSYTE, but INSYTE does not prescribe it.

### 8. Human Role in Decision-Making

- INSYTE explicitly classifies the human role through two dimensions:
  - **Dim 7 (Intervention Independence):** Level 0 = continuous human intervention required; Level 1 = frequent intervention or AI only informs; Level 2 = occasional intervention or AI directs; Level 3 = minimal intervention for extended operation; Level 4 = occasional intervention even for extended operation; Level 5 = no human intervention across all contexts.
  - **Dim 8 (Oversight Independence):** Level 0 = continuous monitoring; Level 1 = regular sanity checking; Level 2 = exception-triggered sense checking; Level 3 = end-of-mission assessment; Level 4 = regular retrospective auditing; Level 5 = incident-only retrospective auditing.

- The framework classifies systems as **decision support** (Dim 7, Level 2: "informs human decision making") or **decision direction** (Dim 7, Level 3: "directs human decision making") or **decision automation** (Dim 7, Levels 4–5).

- Human override is not explicitly modelled as a mechanism, but the framework's classification of intervention levels implies that systems at Levels 0–3 have human override capability.

- **Section 6.2.5** notes that "INSYTE patterns can indicate when the expectations on the human-in-the-loop are too demanding" — systems scoring highly on depth of functionality (Dim 4) are unlikely to be effectively verified by human operators in real time, highlighting the "liability sink" problem.

### 9. System Constraints and Environment

- INSYTE accounts for environmental complexity through Dimensions 5 (diversity) and 6 (dynamism), which characterise the richness and rate of change of the operating environment. These are system-level properties, not resource constraints.

- **No explicit consideration** of limited data, limited compute, unreliable connectivity, or varying user expertise as deployment constraints.

- The framework is designed for **classification across all deployment contexts** (real-world and simulated, embodied and non-embodied) but does not have a specific low-resource orientation.

- **Resource-aware design:** Not applicable — INSYTE is a classification framework, not a system design. The online tool is implemented as a Next.js web application with local storage for confidentiality.

### 10. Hybrid AI Taxonomy

- INSYTE's **Dimension 1 (Underspecification)** creates an implicit taxonomy of AI system types:
  - Level 0: Fully rule-based (IF-THEN encoded)
  - Level 1: Mostly rule-based (~2/3), remainder learned
  - Level 2: Mostly learned (~2/3), some rules (~1/3)
  - Level 3: Mostly learned from labelled data or RL with frequent human feedback
  - Level 4: Learned from mostly unlabelled data or RL with infrequent feedback
  - Level 5: High-level objectives only, minimal specification

- This implicitly captures **hybrid AI systems** at Levels 1–2 where rule-based and learned components coexist.

- **No classification of where safety enforcement sits** — INSYTE does not distinguish whether safety constraints are applied before, alongside, or after AI reasoning.

- **No support for two-level governance** — INSYTE classifies the degree of specification and the degree of independence but does not model how governance mechanisms should be structured.

- **Comparison to my research:** INSYTE could classify my architecture as having approximately Level 1–2 on underspecification (mostly rule-based safety gate + ML reasoning), Level 2–3 on adaptiveness (predefined adaptation via safety states), and Level 2–3 on intervention independence (decision support with state-dependent scope). But INSYTE does not prescribe the architectural pattern itself.

### 11. Baseline Comparison and Evaluation

- **Evaluation type:** Usability and usefulness study, not performance comparison. Two rounds of evaluation with 16 participants from diverse domains (healthcare, automotive, maritime, aviation, manufacturing).

- **No baseline system** — the evaluation compares INSYTE against existing classification frameworks (LoA) through qualitative analysis, not against a system without safety constraints.

- **Metrics:** Usability (ease of use, ease of dimension instantiation, ease of chart generation) and usefulness (value for communication, design, safety, regulation, liability) assessed on Likert-type scales.

- **No CAUTION zone testing** — irrelevant since INSYTE is a classification framework, not a governance system.

- **No Safety Dominance Property verification** — not applicable.

- **No graduated vs. binary governance comparison** — INSYTE classifies governance dimensions but does not test governance mechanisms.

- **Evaluation gaps:** The evaluation focused on expert opinion rather than quantitative validation of classification accuracy or inter-rater reliability. The paper acknowledges that instantiating the framework requires deep system knowledge and that cross-functional teams are needed for accurate classification.

### 12. Key Concepts and Definitions

- **INSYTE pattern:** The radar chart representation of an AI system's classification across 8 dimensions, each rated 0–5. Provides an "immediate visual summary of an AI system's overall capability and a detailed representation of its individual characteristics."

- **Underspecification (Dim 1):** The degree to which a system accomplishes objectives without explicit specification of how to do so — ranging from fully encoded rules (Level 0) to high-level objectives only (Level 5).

- **Adaptiveness (Dim 2):** The degree to which a system handles uncertainty and change in operation — from controlled environments only (Level 0) to proactive adaptation with learning (Level 5).

- **Intervention Independence (Dim 7):** The degree to which a system operates without human operational intervention — distinguishes decision support ("informs," Level 2) from decision direction ("directs," Level 3).

- **Oversight Independence (Dim 8):** The degree to which a system operates without human monitoring — from continuous monitoring (Level 0) to incident-only retrospective auditing (Level 5).

- **Agentic AI systems:** "AI systems that can pursue complex goals with limited direct supervision" — distinguished from traditional autonomous systems by being enabled by frontier AI models.

- **OECD AI system definition:** "A machine-based system that, for explicit or implicit objectives, infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments." INSYTE aligns with and enriches this definition.

### 13. Limitations and Unsolved Problems

- **Stated limitations:**
  1. Requires deep system knowledge — cross-functional teams needed for accurate classification
  2. Discrete levels (0–5) approximate a continuous spectrum; choosing between adjacent levels involves judgment
  3. "Higher" does not mean "better" — risk of misinterpretation as aspirational targets
  4. Static classification per system configuration — does not capture runtime variation in system characteristics
  5. System boundary definition requires judgment (e.g., is the user part of the system?)
  6. Framework needs ongoing refinement as AI capabilities evolve

- **Unsolved problems / future work:**
  1. Inter-rater reliability not formally tested — would multiple teams classify the same system identically?
  2. No formal mechanism linking INSYTE classification to governance requirements — i.e., what governance architecture is appropriate for a given INSYTE pattern?
  3. Potential to evolve INSYTE for real-time operational monitoring (Section 6.2.4) — "INSYTE could even evolve to allow users to directly adjust system levels on its eight dimensions, with appropriate safety guardrails"
  4. Sector-specific adaptations not yet developed

- **Gaps aligned with my research problem:**
  - **No two-level governance model** — INSYTE separates intervention (Dim 7) from oversight (Dim 8) but does not define participation governance (G(S)) or advisory scope governance (A_AI(S)) as architectural mechanisms
  - **No CAUTION mode** — Dim 7 distinguishes "informs" (Level 2) from "directs" (Level 3) as static system characteristics, but does not model a mode where AI participates under restricted recommendation scope that varies with environmental conditions
  - **No Safety Dominance Property** — INSYTE provides no formal guarantee about AI output constraints
  - **No runtime state conditioning** — the classification is static; it does not model how governance should change based on classified environmental safety state. The paper acknowledges this gap by noting that "a system's instantiation of some dimensions may change between intended use and unintended use, as well as between pre-deployment and operation" (Section 5.2.1)

### 14. Methodology Notes

- **Research method:** Systematic multi-stage framework development with stakeholder evaluation:
  1. Preliminary framework from 25 demonstrator projects (Assuring Autonomy International Programme, 2019–2024)
  2. Refinement through literature review of existing classification frameworks and agentic AI
  3. Internal testing by non-developer co-authors on known systems (ChatGPT, Roomba)
  4. Two-round external evaluation with 16 participants (7 in round 1, 9 in round 2)
  5. Framework refinement between evaluation rounds based on feedback

- **DSR alignment:** Shares commonalities with Design Science Research's build–evaluate cycle. The development process (identify problem → develop artefact → evaluate → refine) parallels DSR, though the authors do not explicitly use DSR methodology.

- **Applicable to my research:** The evaluation methodology — multiple rounds of stakeholder evaluation with iterative refinement — is a useful template for evaluating my architecture's governance framework with domain stakeholders. The questionnaire structure (context-setting + usability + usefulness + open-ended) is well-designed.

### 15. Quotable / Citable Points

1. **"The arbitrary groupings of characteristics into single, predefined levels does not allow for a distinct classification of many possible systems"** (Section 2.1) — critique of unidimensional frameworks that motivates multi-dimensional approaches including multi-dimensional governance.

2. **"Operational independence is the system's capacity and delegated authority to achieve its objectives without human operational control. We break this down into two key dimensions: [intervention and oversight]"** (Section 3.2.4) — independently validates separating governance into multiple distinct dimensions, supporting the principle of separating G(S) from A_AI(S).

3. **"INSYTE patterns can indicate when the expectations on the human-in-the-loop are too demanding... systems that score highly on depth of functionality (axis 4) are unlikely to be ones that users, even expert users, are able to verify as functioning correctly in real time"** (Section 6.2.5) — supports the argument that formal governance mechanisms must replace informal human oversight in complex systems.

4. **"INSYTE can show when a high-risk system (based on the criticality of application domain) is in fact low on dimensions like underspecification or environmental dynamism. Such a system is therefore less likely to cause (unforeseen) harm, incurs less uncertainty, and is more controllable"** (Section 6.2.6) — supports graduated, context-sensitive governance rather than blanket risk classification.

5. **"A system's instantiation of some dimensions may change between intended use and unintended use, as well as between pre-deployment and operation"** (Section 5.2.1) — acknowledges that static classification is insufficient and that runtime variation exists, motivating architectures that dynamically adjust governance.

### 16. Relation to My Research and Positioning

- **Level 1 governance (participation control):** Partially addressed — Dimension 7 classifies how much AI independence from intervention a system has, but as a static property, not as a runtime gate function triggered by environmental state.

- **Level 2 governance (output-scope control):** Not addressed — INSYTE does not classify or constrain what types of outputs AI may generate. The breadth (Dim 3) and depth (Dim 4) dimensions describe system capabilities, not governance constraints on those capabilities.

- **State-conditioned governance:** Not addressed — INSYTE classification is static for a given system configuration. The environmental dimensions (5, 6) describe the operating environment's complexity but do not condition AI governance on environmental state.

- **Proximity to (G(S), A_AI(S)):** INSYTE's separation of Dim 7 (intervention) from Dim 8 (oversight) validates the principle that governance should be decomposed into multiple dimensions. However, the Dim 7/8 distinction (intervention vs. monitoring) is orthogonal to the G(S)/A_AI(S) distinction (participation vs. advisory scope). INSYTE classifies the *degree* of human control; my research defines the *mechanism* by which AI participation is governed at runtime.

- **Formal safety property:** No Safety Dominance Property or equivalent. INSYTE provides no formal guarantee about AI output constraints.

- **Gap my research addresses:** INSYTE provides a rich descriptive vocabulary for classifying AI systems but does not prescribe how governance should be dynamically implemented. The gap is the transition from *classifying* governance dimensions to *implementing* runtime governance conditioned on classified environmental state. My architecture fills this by defining S = f(E) → (G(S), A_AI(S)) as a formal runtime mechanism that determines both whether AI participates and what it may recommend.

- **Positioning paragraph:** INSYTE serves as **useful background literature** for my research in two ways. First, it provides an independent, peer-reviewed validation that AI governance should not be collapsed into a single dimension — the separation of intervention independence from oversight independence (Dims 7 and 8) supports my architectural decision to separate participation governance (G(S)) from advisory scope governance (A_AI(S)). Second, INSYTE's observation that "higher" on its dimensions does not mean "better" — and that static classification is insufficient as systems change between pre-deployment and operation — implicitly motivates runtime architectures that dynamically adjust governance based on operational context. INSYTE could be used to classify my safety-state-gated architecture (positioning it on all 8 dimensions), providing a standardised description of the system for cross-stakeholder communication. However, INSYTE does not address the core research gap: no classification framework defines how AI participation and advisory scope should be formally governed at runtime as functions of classified environmental safety state.

### 17. Overall Relevance Score

**⭐⭐⭐ Medium** — Provides useful classification background and independently validates multi-dimensional governance thinking (separating intervention from oversight). Relevant to the broader landscape of AI governance frameworks. However, it does not address runtime governance, safety state classification, formal decision architecture, or the two-level governance gap. Primarily useful as background literature for positioning my architecture within AI classification and governance discourse.
