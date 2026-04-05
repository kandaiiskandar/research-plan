# Literature Review Extraction: Kühn et al. (2025)

## 1. Paper Identity

- **Title:** Machine Learning Applications for Fisheries—At Scales from Genomics to Ecosystems
- **Authors:** Bernhard Kühn, Arjay Cayetano, Jennifer I. Fincham, Hassan Moustahfid, Maria Sokolova, Neda Trifonova, Jordan T. Watson, Jose A. Fernandes-Salvador, Laura Uusitalo
- **Year:** 2025 (published online November 2024)
- **Venue:** Reviews in Fisheries Science & Aquaculture, Vol. 33, No. 2, pp. 334–357
- **DOI:** https://doi.org/10.1080/23308249.2024.2423189
- **Type:** Comprehensive review paper

---

## 2. Core Contribution

- **Problem addressed:** The growing volume and complexity of fisheries data creates a bottleneck requiring automated workflows. The paper surveys how machine learning (ML) methods are being applied — and could be applied — across the full breadth of fisheries science, from genomic analysis to ecosystem-level management.
- **Proposed solution:** A structured review of ML applications organised by fisheries science sub-discipline (genomics → biometrics → fish assemblages → electronic monitoring → stock dynamics → metier/fleet → ecosystem → management), highlighting both opportunities and limitations at each scale.
- **Main contributions:** (1) A comprehensive, scale-organised taxonomy of ML applications in fisheries; (2) identification of discipline-specific challenges (training data quality, domain shift, operationalisation gaps, model validation); (3) a "trustworthy AI" discussion addressing privacy, bias, adversarial attacks, model inversion, and stakeholder trust; (4) identification of physics-informed ML as a promising hybrid approach for data-limited fisheries.
- **Novelty:** The paper is not technically novel — it introduces no new method or system. Its value lies in providing a single, structured reference across the full range of fisheries ML applications, organised by domain problem rather than by ML technique, making it accessible to fisheries scientists exploring ML adoption.

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | Partial | Discusses "physics-informed ML" / "scientific ML" — hybrid models substituting parts of mechanistic/dynamical systems with ML components (Rackauckas et al. 2020; Karniadakis et al. 2021). Also covers Bayesian networks as probabilistic models combining domain knowledge structure with data-driven inference. However, these are not hybrid in the sense of rule-based safety gates controlling ML participation. |
| Safety-critical AI decision-making | No | ML applications are framed as data processing, monitoring, and analysis tools — not as safety-critical decision support systems. No discussion of safety-state classification, operational risk gating, or safety-critical decision architecture. |
| AI governance / control mechanisms | No | No architectural governance mechanisms discussed. The "trustworthy AI" section addresses policy-level concerns (EU AI Act, privacy, auditability, transparency) but not runtime governance of AI participation or output scope. |
| Low-resource environments | Partial | Repeatedly highlights data scarcity as a major constraint: limited labelled training data for fisheries EM, domain shift between training and deployment environments, challenges of cross-vessel/cross-fishery operationalisation. Notes that physics-informed ML improves extrapolation under data-limited settings. Does not address computational or connectivity resource constraints. |
| Decision architecture formalisation | No | No formal model, no mathematical architecture specification, no state variables or gate functions. |
| Human role in decision-making | Partial | Notes human-in-the-loop EM review, EcoCast as a near-real-time decision analysis tool for fishers, and reinforcement learning as analogous to Management Strategy Evaluation. Discusses the importance of communicability (Bayesian networks as non-black-box alternatives). However, human role is not formalised or structured as decision support architecture. |
| Socio-technical evaluation | Partial | The "trustworthy AI" section discusses privacy concerns, stakeholder trust, biases in training data leading to predictive profiling, false positives in automated vessel classification, adversarial attacks, model inversion, and the need for transparency and auditability. Relevant framing for socio-technical evaluation, though not in the context of evaluating a specific decision support system. |
| Coastal fisheries / maritime domain | Yes | Core domain throughout. Covers genomics, biometrics, electronic monitoring, stock assessment, species distribution modelling, fleet/metier analysis, ecosystem dynamics, and fisheries management — all within the marine/fisheries domain. |

**Mid-Extraction Relevance Gate:** 1 Yes + 4 Partial → **REDUCED EXTRACTION** (Sections 4–7 and 12–13 only; Sections 8–11 and 14–15 skipped).

---

## 4. Decision Architecture Analysis

- **Architecture:** The paper does not describe or propose any decision architecture. It surveys ML *applications* across fisheries sub-disciplines — each application is presented as a standalone data processing or modelling task (species ID, age estimation, stock-recruitment modelling, etc.), not as components within a unified decision architecture.
- **Layered architecture / governance structure:** None. The paper's organisational structure (genomics → individuals → assemblages → stock → fleet → ecosystem → management) is a *taxonomic* hierarchy of fisheries science problems, not a layered decision or governance architecture.
- **Rule-based constraints before AI:** Not present as an architectural pattern. The paper notes that ecological theory provides mechanistic functional forms (von Bertalanffy, Beverton-Holt) that ML can be constrained by in physics-informed approaches — but this is about embedding domain knowledge in model structure, not about safety-gate constraints controlling AI participation.
- **Boundary between deterministic control and AI reasoning:** Not defined. The physics-informed ML discussion comes closest — combining mechanistic differential equations with neural network components — but this is a model design pattern, not a governance boundary.
- **Failure modes / fallback behaviour:** Not architecturally addressed. The paper discusses model failure in terms of domain shift (training vs. deployment data mismatch), adversarial attacks, and loss of predictive power under novel environmental conditions (e.g., marine heatwaves). No fallback or degradation mechanism is described.

**Summary:** No decision architecture is present. The paper catalogues ML methods by fisheries application area without proposing or analysing any integrated decision system.

---

## 5. Formal Model and Mathematical Representation

- **Formal model:** None. The paper references formal models *used within* fisheries (von Bertalanffy growth functions, Beverton-Holt stock-recruitment, Lotka-Volterra dynamics) but does not define any formal model of a decision system or governance structure.
- **Comparison to E → S = f(E) → (G(S), A_AI(S)) → AI(E):** Not applicable. No comparable formal pipeline exists in this paper.
- **State-dependent recommendation restriction:** Not modelled or discussed.
- **Safety Dominance Property:** Not defined or referenced.
- **Formalisation purpose:** N/A.

---

## 6. Safety State Classification

- **Discrete risk/safety levels:** None for operational/environmental conditions. The paper mentions risk assessment (bycatch risk hotspots, ecosystem risk under climate change) but these are spatial/ecological risk maps, not operational safety state classifications that govern system behaviour.
- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:** Not applicable. No runtime safety state classification exists.
- **AI recommendation scope differentiation across safety levels:** Not present. All ML applications in the review operate unconditionally — there is no mechanism described where ML outputs are restricted or blocked based on classified environmental conditions.

---

## 7. Governance Level Analysis

| Level | Question | Implemented? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (G(S)) | No | Not addressed. All ML applications are presented as always-on tools — no mechanism governs *whether* AI operates based on environmental or safety state. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | No | Not addressed. No mechanism restricts ML output types based on conditions. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | No | Not applicable. |

- **Governance type:** The paper discusses *policy-level* governance (EU AI Act high-risk classification, privacy regulations, human-in-the-loop requirements) in its "trustworthy AI" section, but not runtime architectural governance of AI participation or output scope.
- **Binary switch vs. graduated model:** Neither — no runtime governance mechanism of any kind.
- **Support or contradiction of two-level governance pair:** Neither supports nor contradicts. The paper operates at a fundamentally different level of abstraction (ML techniques and fisheries applications) than the architectural governance modelled by (G(S), A_AI(S)).

---

## 12. Key Concepts and Definitions

| Term / Concept | Definition / Relevance |
|---|---|
| **Physics-informed ML / Scientific ML** | Hybrid models that substitute part of a mechanistic/dynamical system (differential equations) with an ML component, constraining the ML by known physical relationships. Relevant as a form of hybrid AI, though distinct from the rule-based safety governance hybrid in my architecture. |
| **Domain shift** | Discrepancy between model training data and deployment data leading to unintended extrapolation and performance degradation. Relevant as a low-resource/deployment challenge my architecture must account for. |
| **Electronic monitoring (EM)** | On-vessel camera systems for catch monitoring; the review covers extensive ML work on automated species ID, counting, and catch event detection from EM video — relevant as domain context. |
| **Species distribution modelling (SDM)** | Using environmental covariates (SST, depth, habitat) to predict spatial distributions of fish — widely uses ML (BRT, RF, MaxEnt). Relevant as a fisheries ML application that uses environmental state as input, though not for safety governance. |
| **EcoCast** | A near-real-time decision support tool using BRT-based SDMs to produce daily maps showing predicted ratios of target species to bycatch species, helping fishers avoid bycatch. The closest thing in this paper to an operational decision support system, though it has no safety-state gating. |
| **Reinforcement learning for fisheries management** | Agent-based models using RL to simulate fisher behaviour and explore management strategies (quota allocation, spatial closures). Noted as analogous to Management Strategy Evaluation. Currently theoretical with no real-life implementations. |
| **Model inversion / adversarial attacks** | Security concerns where trained ML models can be reverse-engineered to reconstruct training data, or adversarial inputs can break classifiers. Relevant to the trustworthiness discussion for any AI deployment in fisheries. |
| **Bayesian networks in fisheries ecology** | Probabilistic graphical models representing dependencies among species and ecosystem factors; noted as non-black-box, communicable to end-users, and capable of handling heterogeneous data types — relevant contrast to opaque DL approaches. |

---

## 13. Limitations and Unsolved Problems

- **Stated limitations:**
  - Most DL-based fisheries applications (especially automated EM review) are still under development and not operationally deployed; generalisation under non-standardised conditions remains the main challenge.
  - Automated fish ID and counting in highly mixed commercial trawler settings with frequent occlusion, size variation, similar species, and debris lacks necessary accuracy for operational use.
  - Cross-vessel and cross-institution operationalisation of trained models remains difficult due to domain shift.
  - SDMs lose predictive power under novel environmental conditions (marine heatwaves, climate change), raising concerns about extrapolation.
  - RL for fisheries management remains a theoretical exercise in conceptual models lacking real-world implementation.
  - Trustworthiness concerns — black-box nature, privacy, bias, adversarial vulnerability, model inversion — hinder stakeholder acceptance.

- **Unsolved problems acknowledged:**
  - No scalable solution for generalising ML models across different fisheries, gears, vessels, and environmental conditions.
  - Lack of labelled training data across many fisheries contexts.
  - No framework for systematically building trust in ML-based management advice.
  - No integration of ML applications into unified decision architectures — each application is treated as a standalone tool.

- **Gaps aligning with my research:**
  - The paper surveys ML applications as *standalone tools* without any architectural framework governing when and how AI participates in decision-making. My architecture addresses exactly this gap — providing a formal governance structure (G(S), A_AI(S)) that controls AI participation and output scope based on classified environmental state.
  - The paper's emphasis on domain shift and performance degradation under novel conditions implicitly motivates a safety-gating mechanism — if ML models fail under unusual conditions, there should be a formal way to restrict or block AI outputs. The paper identifies the problem but proposes no architectural solution; my CAUTION and UNSAFE modes provide this.
  - No paper in the review implements graduated governance. All ML applications either operate fully or do not operate — the binary paradigm gap is present throughout.
  - The trustworthy AI discussion identifies the *need* for transparency, auditability, and human oversight but offers no formal model for achieving these through architectural design. My Safety Dominance Property and two-level governance formalise what this section discusses informally.

---

## 16. Relation to My Research and Positioning

- **Governance level implemented:** Neither Level 1 nor Level 2 in the architectural sense. ML applications are presented as unconditional tools.
- **State-conditioned governance:** Not applicable.
- **Proximity to (G(S), A_AI(S)):** Distant. The paper catalogues what ML *can do* in fisheries but does not address how ML participation should be *governed* at runtime.
- **Safety Dominance Property:** Not defined or comparable.
- **Gap my research addresses:** The paper documents the full landscape of fisheries ML applications but reveals — by omission — that no governance architecture exists to control when and how these AI tools operate based on environmental safety conditions. My research fills this gap with a formal, graduated safety-state-gated architecture.

**Positioning paragraph:** Kühn et al. (2025) provides **broad domain background** on the landscape of ML applications in fisheries science. Its comprehensive, scale-organised taxonomy — from genomics to ecosystem management — documents what AI can do in the fisheries domain, making it a useful reference for situating my research within the broader fisheries AI context. The paper's discussion of physics-informed ML as a hybrid approach, domain shift as a deployment challenge, and the "trustworthy AI" concerns around transparency, bias, and stakeholder trust are all tangentially relevant to my architecture's motivation. However, the paper's most significant contribution to my literature review is what it *does not* contain: across dozens of ML applications surveyed at every scale of fisheries science, not a single application implements any form of runtime governance that controls AI participation or restricts AI outputs based on classified environmental safety state. This absence — consistent across a comprehensive review of the field — reinforces the gap my two-level governance architecture addresses. The paper is citable as evidence that fisheries ML operates without safety-state governance, and as domain context for the types of AI outputs my architecture would govern.

---

## 17. Overall Relevance Score

### ⭐⭐ Low

**Justification:** This is a broad review of ML techniques across fisheries science sub-disciplines. It contains no content on safety-critical decision architecture, safety-state classification, AI governance mechanisms, or decision system formalisation — the core themes of my dissertation. Its value is limited to domain background: documenting the fisheries ML landscape and, by omission, evidencing the absence of any governance architecture controlling AI participation or output scope. The "trustworthy AI" section and the physics-informed ML discussion offer minor supporting points. Useful for a brief citation establishing the breadth of fisheries ML activity and the absence of safety governance within it; not citable in the architecture, formalisation, or governance chapters.
