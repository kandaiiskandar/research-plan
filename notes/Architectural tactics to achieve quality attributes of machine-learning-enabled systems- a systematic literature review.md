# Literature Review Extraction
## Paper: Architectural tactics to achieve quality attributes of machine-learning-enabled systems: a systematic literature review

---

## 1. Paper Identity

- **Full title:** Architectural tactics to achieve quality attributes of machine-learning-enabled systems: a systematic literature review
- **Authors:** Vladislav Indykov, Daniel Strüber, Rebekkha Wohlrab
- **Affiliations:** University of Gothenburg and Chalmers University of Technology (Sweden); Radboud University, Nijmegen (Netherlands); Carnegie Mellon University (USA)
- **Year:** 2025
- **Venue:** The Journal of Systems & Software, Vol. 223 (2025), Article 112373
- **DOI:** https://doi.org/10.1016/j.jss.2025.112373
- **Received:** 17 July 2024 | **Revised:** 5 February 2025 | **Accepted:** 5 February 2025 | **Online:** 13 February 2025
- **Open access:** Yes — CC BY 4.0
- **Type:** Systematic literature review (SLR)
- **Primary sources reviewed:** 206 papers (2011–2024)

---

## 2. Core Contribution

- **Research problem:** Machine-learning-enabled (ML-enabled) systems have unique quality characteristics not fully addressed by traditional software quality standards (ISO 25010, ISO 25059). The relationship between architectural design decisions and these quality attributes is poorly understood — trade-offs between quality attributes when applying a given architectural tactic are largely uncharted.
- **Three research questions:**
  - **RQ1:** What are the most frequently reported quality attributes (QAs) for ML-enabled systems? → Produces a common quality model
  - **RQ2:** What architectural tactics (ATs) have been reported as effective for ML-enabled systems? → Identifies 16 ATs
  - **RQ3:** For each AT, what is the reported impact on all identified QAs? → Produces 85 quality trade-offs (Table 3)
- **Key outputs:**
  - **11 Common Quality Attributes (CQAs)** — a synthesised quality model for ML-enabled systems
  - **16 Architectural Tactics (ATs)** — design decisions to achieve those QAs
  - **Trade-off matrix (Table 3)** — impact of each AT on each QA (positive, negative, ambivalent, or insufficient evidence)
- **Validation:** Quality model validated by 6 experts at Swedish Requirements Engineering Meeting (SiREN 2023); AT list validated by 4 ML engineers from Swedish AI software companies

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | **Partial** | AT11 Rule-based Models is identified as a tactic for ML-enabled systems — maps conceptually to the deterministic governance layer S = f(E) |
| Safety-critical AI decision-making | **Partial** | Safety is one of the 11 CQAs (19 papers reference it), but the paper does not address how to formally guarantee safety properties |
| AI governance / control mechanisms | No | The ATs focus on system design, training, and deployment — not on runtime governance of AI recommendation scope |
| Pre-generation advisory scope restriction | No | None of the 16 ATs address restricting what an AI may recommend based on classified environmental state |
| Environmental state classification | No | No concept of S = f(E), safety states, or state-conditioned governance |
| Low-resource environments | No | Resource Efficiency is a CQA, but the paper does not address low-resource deployment constraints specifically |
| Decision architecture formalisation | No | No formal mathematical model. Qualitative trade-off analysis only |
| Human role in decision-making | **Partial** | AT4 Human-in-the-Loop is identified — maps to Layer 4 human decision-maker, but framed as a training/monitoring component, not a final decision authority |
| Maritime / fisheries domain | No | General ML-enabled systems scope |

**Mid-Extraction Relevance Gate:** 0 Yes + 3 Partial → **REDUCED EXTRACTION** (core sections only)

---

## 4. The 11 Common Quality Attributes (CQAs)

Derived from Table 1 (all retrieved QAs, sorted by frequency) and Figure 1 (proposed quality model). The 11 CQAs included in the proposed model and their definitions:

| CQA | #Occ. | Definition |
|---|---|---|
| **Fairness** | 19 | Degree to which a system can detect and prevent algorithmic bias created by a model |
| **Safety** | 19 | Degree to which a system performs specified functions under specified conditions in the fixed domain |
| **Security** | 18 | Degree to which a system protects information and data |
| **Explainability** | 18 | Degree to which the behaviour of a system (primarily, the behaviour of ML models) and its output can be explained by humans |
| **Privacy** | 17 | Sub-characteristic of Security |
| **Reliability** | 16 | Degree to which a system performs specified functions under specified conditions |
| **Performance** | 16 | Sub-divided into Resource Efficiency and System Accuracy |
| **Transparency** | 14 | Sub-characteristic of Explainability — openness and accessibility of internal processes |
| **Robustness** | 13 | Sub-characteristic of Reliability |
| **Data Quality** | 13 | Degree of integrity and sufficiency of data for model training, testing, and validation |
| **Maintainability** | 12 | Degree to which a system can be modified and supported by developers and maintainers |

Additional top-level CQAs in the model: **Resource Efficiency**, **System Accuracy**, **Usability**, **Portability**.

**Key finding:** Compatibility (ISO 25010) was mentioned only twice — not included in the common model. "System accuracy" and "data quality" are ML-specific attributes absent from ISO 25059.

---

## 5. The 16 Architectural Tactics (ATs) — Definitions and Scope

From Table 2 (architectural tactics to achieve CQAs) and Section 4.2.11 (definitions). Scope: TS = Training System; DS = Deployed System.

| AT | Name | Scope | Definition |
|---|---|---|---|
| AT1 | Distributed Learning | TS | Architectural approach to ML aimed at parallelising computing powers among several computers |
| AT2 | Automated Data Reduction | TS/DS | Automated process aimed at minimising the complexity and size of datasets while preserving their essential information |
| AT3 | Federated Learning | TS | Architectural approach to ML aimed at training on local heterogeneous datasets |
| **AT4** | **Human-in-the-Loop (HitL)** | **TS/DS** | **Architectural approach where a human (expert) is integrated into the ML-enabled system as a separate component aimed at monitoring and improving the system's behaviour** |
| AT5 | Automated Data Versioning | TS/DS | Automated process aimed at creation, tracking, and management of different versions or iterations of datasets used for model training, testing, and validation |
| AT6 | Intrusion Detection | TS/DS | Tactic aimed at detection and classification of network intrusions and anomalies |
| AT7 | Automated Data Encryption | TS/DS | Automated process aimed at securing sensitive data used for training, inference, or model deployment |
| AT8 | Containerisation | DS | Architectural approach aimed at packaging an entire system or model (incl. dependencies and runtime environment) into a standardised unit called a container |
| AT9 | Componentisation | TS/DS | Architectural approach aimed at breaking down a software system into modular components or building blocks that can be independently developed, tested, and deployed |
| AT10 | Local Interpretable Models (LIME) | TS/DS | Approach to ML aimed at explaining black boxes by approximating the behaviour of a complex model around a specific prediction using simpler (more interpretable) models |
| **AT11** | **Rule-based Models** | **TS/DS** | **Type of model that relies on explicit rules (if-then) that are designed and specified by humans or domain knowledge to approximate complex model behaviour** |
| AT12 | Automated Hyperparameter Tuning | TS | Method aimed at searching for the best hyperparameter values for the model based on certain criteria |
| AT13 | Automated Algorithm Selection | DS | Automated process aimed at searching the most appropriate method(s) for a certain task or in certain circumstances |
| AT14 | Automated Bias Mitigation | DS | Automated process aimed at identifying and reducing bias in algorithms, models, and datasets by evaluating through fairness metrics or "sensitive" feature monitoring |
| AT15 | Automated Data Preprocessing | TS/DS | Automated process aimed at preparing raw data for analysis and model training |
| AT16 | Automated Data Profiling | TS | Automated process aimed at analysing and summarising the characteristics of a dataset to gain insights into its structure, quality, and distribution |

---

## 6. Trade-off Analysis — Key Rows for This Research (Table 3)

The full trade-off matrix covers 16 ATs × 11 QAs. Key rows for this research:

**AT11 — Rule-based Models:**

| QA | Impact | Note |
|---|---|---|
| Resource Efficiency | 0 | Insufficient evidence |
| Usability | 0 | Insufficient evidence |
| Reliability | 0 | Insufficient evidence |
| Security | 0 | Insufficient evidence |
| Maintainability | 0 | Insufficient evidence |
| Portability | 0 | Insufficient evidence |
| **Explainability** | **+** | Positive — rule-based models are inherently interpretable |
| **System Accuracy** | **−** | Negative — limited adaptability to complex and dynamic data patterns outside predefined rules |
| Fairness | 0 | Insufficient evidence |
| Data Quality | 0 | Insufficient evidence |
| **Safety** | **0** | **Insufficient evidence — no formal safety property demonstrated** |

**AT4 — Human-in-the-Loop:**

| QA | Impact | Note |
|---|---|---|
| Resource Efficiency | + | Positive |
| **Security** | **a** | **Ambivalent — controversial: guides XAI, but introduces unpredictable human element (security concern)** |
| Maintainability | + | Positive |
| Portability | 0 | Insufficient evidence |
| Explainability | + | Positive — bidirectional symbiotic sensing feedback |
| System Accuracy | 0 | Insufficient evidence |
| **Fairness** | **+** | **Positive** |
| Data Quality | + | Positive — constant human feedback |
| **Safety** | **a** | **Ambivalent — can mitigate some safety issues of autonomous systems, but introduces unpredictable elements** |

**Critical observation:** Both AT11 and AT4 show 0 (insufficient evidence) or ambivalent for **Safety**. This confirms the gap: the architectural tactics literature has not formally characterised how rule-based models or human integration contributes to safety properties in ML-enabled systems — which is precisely what the Safety Dominance Property AI(E) ⊆ A_AI(S) formalises.

---

## 7. AT11 Limitation — Reframed as a Governance Feature

Section 4.3.11 states: *"The main focus of rule-based models found with our search strategy was on system accuracy, which can suffer from limited adaptability to complex and dynamic data patterns when scenarios lie outside the predefined rules."*

This limitation is identified in the context of using rule-based models to **approximate complex ML model behaviour** (i.e., to replicate what a deep neural network does). In that use case, limited adaptability is a weakness — the rule-based model fails when the ML model would succeed.

**Architectural distinction for this research:** The deterministic governance layer S = f(E) is not used to approximate ML behaviour. It is used to **govern** ML behaviour — to restrict what the ML component may recommend based on classified environmental state. In this context, the non-adaptability of the rule-based layer is a design feature, not a limitation. You want the governance boundary to be:
- **Deterministic** — the same conditions always produce the same governance outcome
- **Non-adaptive** — the governance layer does not drift or learn from AI outputs
- **Formally verifiable** — the same properties that make AT11 "limited" in model approximation make it formally analysable in governance

This is a critical distinction for viva positioning: the paper's critique of AT11 applies to one specific use case (model approximation). The research applies AT11's rule-based mechanism to a fundamentally different purpose (pre-generation scope restriction), where those same properties become advantages.

---

## 8. AT4 — Human Role Framing Distinction

The paper frames AT4 HitL as: *"integration of human intelligence as a system component aimed at monitoring and improving the system's behaviour."*

This framing positions the human as an input to ML system improvement — an expert who validates outputs, corrects errors, and feeds back into training. Both the training system (TS) and deployed system (DS) scopes are included.

**Architectural distinction for this research:** Layer 4 in the governance architecture is not a monitoring or improvement component — it is the **terminal decision authority**. The human does not monitor the AI or improve it; the human makes the final decision using AI-generated advice as input. The governance architecture is specifically designed to ensure that what the human receives has already been bounded by the Safety Dominance Property — so the human is never presented with advice the AI is not permitted to give under current environmental conditions.

This is a more precise architectural specification of the human role than what AT4 captures. AT4 treats human integration as a quality tactic for improving ML system performance. The architecture treats human authority as a formal architectural requirement that the governance layer serves.

---

## 9. Architectural Level Distinction

The 16 ATs in this paper all operate **inside** the ML component — they are design decisions about how to build, train, and configure the ML system itself. Examples:
- AT12/AT13: how to select the best model or algorithm
- AT15/AT16: how to prepare and profile training data
- AT11: how to make ML predictions interpretable via rules
- AT4: how to integrate human expertise into training/deployment

The governance architecture operates **above** the ML component — it constrains what the ML system is permitted to do **before it generates recommendations**, based on classified environmental state. This is a different architectural level entirely.

The paper's framework cannot capture the governance pair (G(S), A_AI(S)) because none of its three RQs address the question: *"What architectural mechanisms restrict what an AI may recommend, based on classified environmental conditions?"* That question is outside the scope of ML system quality architecture as defined in this paper.

---

## 10. Formal Model and Mathematical Representation

- **Formal model:** None. The paper uses frequency analysis (RQ1), content analysis (RQ2), and impact coding (+/−/a/0) for trade-off analysis (RQ3). No mathematical formalisation.
- **Comparison to (G(S), A_AI(S)):** No comparison possible. The paper does not define state variables, classification functions, gate functions, admissible action spaces, or containment hierarchies.
- **Safety Dominance Property:** Not defined. Safety is a CQA (19 papers), but no AT formally demonstrates how to achieve it.

---

## 11. ISO Standard Comparison (Table 4)

| Proposed CQA | ISO 25059 (AI) | ISO 25010 (general software) |
|---|---|---|
| Functional Suitability | Functional Correctness | Functional Suitability |
| Resource Efficiency | — | Performance Efficiency |
| Usability | User Controllability | Usability |
| Reliability | Robustness | Reliability |
| Security | — | Security |
| Maintainability | Interoperability | Maintainability |
| Portability | Functional Adaptability | Portability |
| Explainability | Transparency | — |
| System Accuracy | — | — |
| Fairness | Ethical | — |
| Data Quality | — | — |
| — | — | Compatibility |

**Key finding (Section 5.2):** Neither ISO 25059 nor ISO 25010 includes "System Accuracy" or "Data Quality" at the system level. These are ML-specific attributes absent from existing standards. ISO 25059 does not include "Resource Efficiency" — relevant for low-resource deployment contexts.

---

## 12. Key Concepts and Definitions

| Concept | Definition | Relevance |
|---|---|---|
| **Quality attribute (QA)** | Measurable or testable property of a system that indicates how well it satisfies the needs of its stakeholders | Background — establishes the design vocabulary for ML system quality |
| **Architectural tactic (AT)** | "A technique an architect can use to achieve the required quality attributes" (Bass et al., 2003) | Background — establishes that design decisions are specifically aimed at QAs |
| **Common Quality Attribute (CQA)** | Quality attribute that appears frequently across multiple independent papers for ML-enabled systems | Background — the 11 CQAs define the quality landscape for ML systems |
| **Quality trade-off** | Balance or compromise between QAs when an AT is implemented | Background — confirms that architectural decisions have side-effects across multiple QAs |
| **AT11 Rule-based Models** | If-then rules specified by humans or domain knowledge to approximate complex model behaviour | Directly related — conceptual match for the deterministic governance layer S = f(E), but different purpose |
| **AT4 Human-in-the-Loop** | Human expert integrated as a separate component for monitoring and improving ML system behaviour | Directly related — conceptual match for Layer 4, but different framing (monitoring vs. terminal authority) |

---

## 13. Limitations and Unsolved Problems

- Gray literature excluded — may have missed relevant industry architectural practices
- AT list cannot be claimed complete — verification limited by search strategy
- Trade-off matrix based on literature-reported impacts, not empirical measurement
- Generalisability: findings derived from papers across diverse domains — may not apply uniformly to all ML-enabled system types
- No formal verification of trade-offs — expert peer-review only
- Safety as a CQA has minimal AT coverage — AT11 shows 0 for Safety, AT4 shows ambivalent — the paper identifies this as requiring further study

---

## 14. Positioning for This Research

**Governance levels implemented:** None of the 16 ATs implement Level 1 (participation gate G(S)) or Level 2 (advisory scope restriction A_AI(S)) in the sense used in this architecture. AT11 provides a rule-based mechanism conceptually related to the deterministic layer, and AT4 provides a human integration mechanism conceptually related to Layer 4, but neither operates at the governance level.

**State-conditioned governance:** Not present. No AT is conditioned on classified environmental safety state. The ATs apply uniformly to ML system design without reference to runtime environmental conditions.

**Safety Dominance Property:** Not defined. Safety is identified as a CQA but no AT formally achieves it. Table 3 shows AT11 → Safety = 0 (insufficient evidence) — the precise gap this research fills by combining AT11-type rule-based mechanisms with formal state classification to produce a provable safety property.

**Gap confirmation:** The paper inadvertently confirms the novelty gap. It identifies Safety as one of the two most frequently mentioned QAs (19 papers) but finds no AT with demonstrated positive impact on Safety. The proposed architecture addresses this by using a rule-based deterministic governance layer (AT11 concept) specifically to enforce the Safety Dominance Property — a formal safety guarantee that this paper's entire AT library cannot produce.

**Positioning paragraph:** Indykov et al. (2025) present a systematic quality model and architectural tactic catalogue for ML-enabled systems, identifying 11 CQAs and 16 ATs across 206 papers. Two tactics are conceptually related to the proposed architecture: AT11 (Rule-based Models) maps to the deterministic governance layer S = f(E), and AT4 (Human-in-the-Loop) maps to Layer 4 (human decision authority). However, the paper's 16 ATs all operate inside the ML component — they are design decisions for building and training ML systems, not runtime governance mechanisms for constraining ML recommendation scope based on environmental state. Critically, Table 3 shows AT11 scoring 0 (insufficient evidence) for the Safety attribute — confirming that the architectural tactics literature has not established how rule-based mechanisms formally achieve safety properties. This is precisely the gap the proposed architecture addresses: combining AT11-type deterministic rule evaluation with formal environmental state classification (S = f(E)) to produce a provable Safety Dominance Property (AI(E) ⊆ A_AI(S)) that none of the 16 identified ATs can deliver.

---

## 15. Overall Relevance Score

### ⭐⭐ Low–Medium

**Justification:** The paper is directly useful as background on ML system quality architecture — it confirms that Safety is a widely recognised QA and that rule-based models (AT11) and human integration (AT4) are established architectural mechanisms. However, none of the 16 ATs address pre-generation advisory scope restriction, environmental state classification, state-conditioned governance, or formal safety guarantees. The paper's primary value for this research is as confirmatory evidence that: (1) the architectural building blocks used in the proposed architecture (rule-based layer, human layer) are established concepts in ML system architecture; and (2) the Safety attribute has no AT with demonstrated positive impact in the existing literature — confirming the formal gap the proposed architecture fills.
