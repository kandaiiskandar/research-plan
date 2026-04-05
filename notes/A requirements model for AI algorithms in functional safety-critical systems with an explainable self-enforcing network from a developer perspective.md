# Literature Extraction: Klüver et al. (2024)
## "A requirements model for AI algorithms in functional safety-critical systems with an explainable self-enforcing network from a developer perspective"

---

## 1. Paper Identity

- **Title:** A requirements model for AI algorithms in functional safety-critical systems with an explainable self-enforcing network from a developer perspective
- **Authors:** Christina Klüver, Anneliesa Greisbach, Michael Kindermann, Bernd Püttmann
- **Year:** 2024
- **Venue:** Security and Safety, Vol. 3, 2024020 (EDP Sciences)
- **Type:** Conceptual framework with tool demonstration (Self-Enforcing Network model)

---

## 2. Core Contribution

- **Problem:** AI methods (especially neural networks and deep learning) are entering safety-critical systems, but existing functional safety standards (EN 61508, EN ISO 13849-1, EN IEC 62061) were not designed for AI. There is a gap between current AI standardisation and what is required for compliance with regulations like the EU AI Act. The complexity of requirements across multiple standards, safety integrity levels, and application domains makes it difficult for developers and assessors to track and verify compliance.

- **Proposed solution:** A **requirements model** operationalised through a **Self-Enforcing Network (SEN)** — a self-organised learning neural network that maps 44 identified requirements for AI in safety-critical systems to achievable Safety Integrity Levels (SIL 1–3 or "not suitable"). Developers input the degree of fulfillment for each requirement, and the SEN classifies the achievable SIL. An **explainability component** based on Shapley values provides Feature Importance (FI) visualisation, showing which requirements are met or unmet relative to a target SIL.

- **Main contributions:** (1) Systematic compilation of 44 requirements for AI in functional safety-critical systems from standards, regulations, and practical experience; (2) Expert-defined "reference types" mapping requirement fulfillment degrees to SIL levels; (3) Implementation via SEN with intrinsic explainability through Shapley values; (4) Demonstration across four AI method types (deterministic NN with xAI, DL without xAI, DL with beginnings of xAI, rule-based algorithm).

- **Novelty:** The use of a self-organised learning network (SEN) as a compliance assessment tool for AI in safety-critical systems, with intrinsic explainability showing which requirements drive the SIL classification. The model bridges functional safety standards and AI-specific requirements in a single assessable framework.

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | **Partial** | Discusses functional safety architectures (1-channel, 2-channel with test equipment, 2-channel redundant) and the role of diversity principle. Notes that AI could reduce systematic errors through diverse circuit design. The SEN itself is a hybrid (self-organised NN with deterministic learning rule). |
| Safety-critical AI decision-making | **Yes** | Central focus. Comprehensive treatment of Safety Integrity Levels (SIL 1–3), Performance Levels (PL a–e), functional safety standards, and requirements for AI methods in safety-critical systems. |
| AI governance / control mechanisms | **Yes** | The entire requirements model is a governance framework — it defines what AI methods must satisfy to operate at each safety level. The functional safety architectures (Section 2.3) describe how safety systems govern behaviour through redundancy, test equipment, and diversity. |
| Low-resource environments | **No** | Not addressed. Focus is on industrial machinery, aerospace, mining, automotive — all with standard infrastructure. |
| Decision architecture formalisation | **Partial** | Formalises the SEN architecture (semantic matrix, weight matrix, learning rule, activation functions) and the functional safety architectures (I-L-O pipeline, 1/2-channel systems). However, no formal model comparable to E → S → (G(S), A_AI(S)). |
| Human role in decision-making | **Partial** | The model is developer/assessor-facing — humans input requirement fulfillment degrees and interpret SEN results. The safe state concept requires human understanding of what constitutes safety. However, no formal human-in-the-loop model for end-user decision-making. |
| Socio-technical evaluation | **No** | Pure technical/standards-compliance focus. No socio-technical evaluation of human-AI interaction. |
| Coastal fisheries / maritime domain | **No** | Industrial machinery, aerospace, mining, automotive domains. |

**Yes count: 2 | Partial count: 3 → REDUCED EXTRACTION (Sections 4–7 and 12–13 only)**

---

## 4. Decision Architecture Analysis

The paper describes **functional safety architectures** (Section 2.3) that are directly relevant to understanding how safety-critical systems structure governance:

**1-channel system (Figure 4):** Input → Logic → Output. A single functional channel. A dangerous fault in any subsystem leads to dangerous system behaviour. Lowest safety integrity.

**1-channel with test equipment (Figure 5, left):** The "functional channel" plus a "second channel" consisting of Test Equipment (TE) and Output Test Equipment (OTE). If TE detects unexpected behaviour in the functional channel, it switches to a "safe state" via OTE. The second channel must be as independent as possible from the functional channel. This increases safety integrity but leaves a vulnerability in the input section.

**2-channel redundant system (Figure 5, right):** Two fully independent sub-circuits, each capable of executing the safety function independently. Random hardware faults in one path cannot cause system failure. Cross-monitoring (c) between channels. Highest safety integrity for random faults.

**Key architectural principle — diversity:** If both channels are identical, systematic faults may cause the same failure in both. The diversity principle designs channels "differently" — different circuit technologies, hardware concepts, software architectures, different developers. AI-based algorithms could contribute to diversity in circuit design even if not directly permitted for primary safety functions.

**Relationship to my architecture:** The functional safety architecture patterns (particularly the test equipment / second channel concept) are structurally analogous to my architecture's deterministic safety layer. The test equipment channel that monitors the functional channel and can switch to a "safe state" mirrors my gate function G(S) that can block AI participation. However, these architectures are *hardware reliability* architectures — they address random and systematic hardware faults, not the question of *what types of AI recommendations are permitted* based on environmental safety state. The SIL classification determines the *required reliability level* for the safety function, not the *scope of AI advisory output* — a fundamental difference from my A_AI(S).

---

## 5. Formal Model and Mathematical Representation

**SEN formalisation:**
- Semantic matrix (sm) with values v_sm encoding expert-assessed requirement fulfillment for each SIL
- Weight matrix derived via Self-Enforcing Rule: w_ao = c × v_sm × cvf_a (Eq. 1), where c = learning rate, cvf_a = cue validity factor for attribute a
- Enforcing Activation Function: a_j = Σ(w_ao × a_i) / (1 + |w_ao × a_i|) (Eq. 2)
- Feature Importance via Shapley values: Φ_i(v) = v(i) (Eq. 4, simplified for SEN)

**Safety classification formalisation:**
- SIL determined by risk graph: factors S (severity), F (frequency), P (possibility of avoidance)
- Performance Level (PL a–e) mapped to SIL 1–3
- AI-SIL assessment (from Diemert et al.): combines conventional SIL, input complexity (entropy), and output complexity (non-determinism) through functional decomposition into AI and non-AI components

**Comparison to my pipeline:**

| Component | My Architecture | Klüver et al. |
|---|---|---|
| Environmental state vector E | {w, r, m, o, v, t} — runtime environmental inputs | Not present — requirements are design-time properties, not runtime states |
| Safety state classification S = f(E) | Runtime: SAFE/CAUTION/UNSAFE based on current conditions | Design-time: SIL 1–3 based on required risk reduction for the application |
| Gate function G(S) | Runtime gate: AI blocked when UNSAFE | Design-time gate: AI methods may be excluded from safety functions based on SIL requirements |
| Admissible action space A_AI(S) | Runtime: AI output types restricted by current state | Not present — requirements specify what AI *must demonstrate* to be permitted, not what AI *may output* at runtime |
| Safety Dominance Property | Runtime containment: AI(E) ⊆ A_AI(S) | Not present as runtime property. The functional safety architectures ensure that safety functions bring the system to a "safe state" with specified reliability. |

**Critical distinction:** This paper operates at the **design-time assessment level** — determining whether an AI system *qualifies* for a given SIL. My architecture operates at the **runtime governance level** — dynamically controlling what AI may do based on current environmental conditions. These are complementary but distinct: a system could pass SIL assessment (Klüver et al.) and then operate under runtime governance (my architecture).

---

## 6. Safety State Classification

The paper's safety classification operates at two levels:

**Application-level risk assessment:** Factors S, F, P (or Se, Fr, Pr, Av) determine the *required* PL or SIL for a safety function. This is a design-time classification of the application's risk profile, not a runtime classification of current conditions.

**AI method suitability assessment:** The SEN classifies whether a given AI method, at its current development stage, achieves SIL 1, SIL 2, SIL 3, or is "not suitable for SCS." This is an assessment of the AI method's properties against requirements, not a runtime state classification.

**AI-SIL (Section 2.2):** The proposed AI-SIL framework combines conventional SIL with AI complexity assessment (input entropy, output non-determinism) through functional decomposition. This is the most relevant concept — it acknowledges that AI components may need different safety integrity assessment than conventional components.

**Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:** Fundamentally different axis. My S = f(E) classifies the *current environmental state* at runtime to govern AI behaviour dynamically. This paper's SIL classifies the *required safety integrity* of the system at design-time to determine whether AI is permitted at all. The paper's SIL is analogous to determining which of my safety states should *exist in the design*, while my S = f(E) determines which state the system is *currently in*.

**CAUTION mode equivalent:** Not present in any form. The paper's framework is binary at the method level: an AI method either achieves a given SIL or it doesn't. There is no intermediate mode where AI operates with restricted scope. The closest concept is "usage levels" (Section 2.4) — AI used for diagnostics vs control vs development tool — but these are fixed application roles, not dynamic state-conditioned scope restrictions.

---

## 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (equivalent to G(S)) | **Partial (design-time)** | The SIL assessment determines whether an AI method is permitted in a safety-critical system. IEC 61508:2010 currently does not recommend AI methods even for diagnostics. The "not suitable for SCS" classification is a design-time participation gate. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (equivalent to A_AI(S)) | **No** | No mechanism restricts what AI may output at runtime based on classified state. The "usage levels" (diagnostics, control, development tool) are fixed application roles. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | **No** | All governance is design-time, not runtime state-conditioned. |

**Design-time vs runtime governance:** The paper provides a comprehensive **design-time governance framework** — determining whether AI methods qualify for safety-critical systems. My architecture provides **runtime governance** — dynamically controlling AI behaviour based on current conditions. These operate at different lifecycle stages and are complementary rather than competing.

---

## 12. Key Concepts and Definitions

- **Safety Integrity Level (SIL):** Four-level classification (SIL 1–4, with SIL 4 highest) based on dangerous failure rates for safety-related systems. EN IEC 62061 limits machinery to SIL 1–3. Determines how reliable a safety function must be.
- **Performance Level (PL):** Five-level classification (PL a–e, with PL e most stringent) from EN ISO 13849-1. Can be mapped to SIL levels.
- **AI-SIL:** Proposed extension combining conventional SIL with AI complexity assessment (input entropy, output non-determinism) through functional decomposition of AI and non-AI components.
- **Self-Enforcing Network (SEN):** Self-organised learning neural network where weight values are derived deterministically from the semantic matrix via the Self-Enforcing Rule, ensuring traceability and reproducibility. Used here to map requirement fulfillment to SIL classification.
- **Functional decomposition:** Dividing the overall safety function into conventional (non-AI) and AI-based components, each assessed separately for safety integrity.
- **Diversity principle:** Designing redundant safety channels "differently" to combat systematic faults — different technologies, architectures, developers.
- **Safe state:** A condition where a hazard is no longer present. Critically, what constitutes a "safe state" varies by application — stopping a machine may be safe for industrial machinery but not for aircraft or pacemakers.
- **Usage levels for AI:** AI used (a) inside a safety-related function, (b) as a non-AI safety function ensuring safety for AI-controlled equipment, or (c) as a tool in designing safety-related functions. Different evidence requirements for each.

---

## 13. Limitations and Unsolved Problems

**Stated limitations:**
1. The model was developed primarily for NN-based methods; requirements for other AI methods and diverse applications need extension.
2. Expert selection and evaluation of requirements involved a limited group — subjective influences cannot be ruled out. Broader expert involvement needed for generalisation.
3. The 44 requirements are "not to be considered complete" — the standards landscape is still evolving.
4. Current standards (IEC 61508:2010) do not recommend AI methods even for diagnostics in safety-related systems; the next edition is expected to change this.
5. The gap between current AI standardisation and EU AI Act requirements remains unresolved.

**Gaps aligning with my research problem:**
- **No runtime governance:** The entire model operates at design-time. Once an AI method is certified for a given SIL, there is no mechanism to dynamically adjust its participation or output scope based on current environmental conditions. My architecture fills this gap with runtime state-conditioned governance.
- **No environmental state classification:** The SIL classifies application risk and method capability, not current environmental state. There is no equivalent to S = f(E) that dynamically assesses current conditions.
- **No state-conditioned output restriction:** The "usage levels" (diagnostics, control, tool) are fixed application roles. There is no mechanism where AI transitions from full advisory scope to restricted scope based on classified state — no CAUTION mode.
- **Binary method suitability:** An AI method either achieves a SIL or doesn't. There is no graduated mode where a method operates at reduced capability under degraded conditions. The paper's architecture patterns (1-channel, 2-channel) address hardware redundancy, not AI advisory scope graduation.
- **No Safety Dominance Property:** The functional safety architectures ensure that safety functions achieve target failure rates. There is no equivalent to AI(E) ⊆ A_AI(S) — a runtime guarantee that AI outputs remain within state-determined bounds.

---

## 16. Relation to My Research and Positioning

**Level 1 governance:** Implemented at design-time. The SIL assessment determines whether an AI method qualifies for a safety-critical system. This is a pre-deployment participation gate, not a runtime state-conditioned gate.

**Level 2 governance:** Not implemented. No mechanism restricts AI output scope at runtime based on classified state.

**State-conditioned governance pair:** Not present. All governance is design-time assessment, not runtime state-conditioned control.

**Safety Dominance Property:** Not present as runtime containment. Functional safety architectures ensure target failure rates but do not formally bound AI output scope.

**Gap my research addresses:** This paper comprehensively addresses the *design-time certification* problem — whether an AI method qualifies for a safety-critical system. My architecture addresses the complementary *runtime governance* problem — how to dynamically control AI behaviour once deployed, based on changing environmental conditions. The two are complementary: an AI system could be certified for a given SIL (using this paper's framework) and then operate under runtime governance (using my architecture's (G(S), A_AI(S)) pair). The paper's requirements model could inform the design-time validation of my architecture's components.

**Positioning paragraph:** This paper serves as **background on functional safety standards and requirements** for my research. It provides a comprehensive mapping of the standards landscape (EN 61508, EN ISO 13849-1, EN IEC 62061, IEC ISO TR 5469, EU AI Act) and operationalises 44 requirements for AI in safety-critical systems. The paper's treatment of functional safety architectures (1-channel, 2-channel, diversity principle) and the AI-SIL concept (extending SIL assessment with AI complexity factors) provides useful context for positioning my architecture within established safety engineering practice. Critically, the paper operates exclusively at the design-time assessment level — determining whether AI methods *qualify* for safety-critical systems — while my architecture operates at the runtime governance level — dynamically controlling *what AI may do* based on current environmental conditions. This distinction is fundamental: the paper's SIL assessment is a prerequisite for deployment, while my (G(S), A_AI(S)) governance pair operates during deployment. The paper confirms that the safety-critical AI community is focused on *whether AI should be permitted* (Level 1, design-time) but has not addressed *how AI output scope should vary by environmental state at runtime* (Level 2, dynamic) — the specific gap my architecture fills.

---

## 17. Overall Relevance Score

### ⭐⭐⭐ Medium

**Justification:** This paper provides valuable background on functional safety standards, SIL/PL classification, functional safety architectures, and the requirements landscape for AI in safety-critical systems. It is relevant to two major themes (safety-critical AI, AI governance) and partially relevant to three others. Its strongest value is as **standards-level background** — grounding my architecture's safety claims in established functional safety practice. The AI-SIL concept, functional safety architectures, and diversity principle are all citable in my dissertation. However, the paper operates exclusively at design-time assessment, has no runtime governance mechanism, no environmental state classification, and no graduated AI output restriction — making it background rather than an architectural antecedent or comparator. It confirms the field's focus on design-time certification while leaving the runtime governance gap my architecture addresses.
