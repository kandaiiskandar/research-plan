## Literature Review Extraction

---

### 1. Paper Identity

- **Title:** Evaluating Trustworthiness in AI: Risks, Metrics, and Applications Across Industries
- **Authors:** Aleksandra Nastoska, Bojana Jancheska, Maryan Rizinski, Dimitar Trajanov
- **Year:** 2025
- **Venue:** *Electronics*, 14(13), 2717 (MDPI) — doi:10.3390/electronics14132717
- **Type:** Review / survey paper

---

### 2. Core Contribution

- **Problem addressed:** How can trust in AI systems be systematically measured across the AI lifecycle, and what trade-offs arise when optimising for different trustworthiness dimensions (fairness, transparency, privacy, security, accountability)?
- **Proposed solution / key finding:** A comprehensive review and comparative analysis of existing frameworks (NIST AI RMF, AI-TMM, ISO/IEC standards, KAIRI) and metrics (SHAP, LIME, differential privacy, federated learning) for evaluating AI trustworthiness. The paper bridges theoretical frameworks with practical applications via case studies in healthcare, finance, public administration, and autonomous systems.
- **Main contributions:**
  1. Structured taxonomy of AI trustworthiness components (fairness, transparency, privacy, accountability, security) with associated metrics
  2. Comparative analysis of four major governance/trust frameworks (NIST AI RMF, AI-TMM, ISO/IEC 24028/42001, KAIRI)
  3. Real-world case studies demonstrating trustworthiness metric application (COMPAS, Robodebt, OHCA detection, credit scoring, Swedish PES)
  4. Identification of trade-offs between competing trustworthiness dimensions
- **Novelty:** The paper is a synthesis and comparative review rather than proposing a novel architecture or framework. Its contribution is in systematically mapping existing frameworks against each other and grounding them in cross-sector case studies.

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | No | Not discussed. No hybrid AI architecture is proposed or reviewed. |
| Safety-critical AI decision-making | Partial | Discusses autonomous systems (UAVs, autonomous driving) and healthcare as safety-critical domains, but only from a trustworthiness/governance-framework perspective — not from a runtime decision-architecture perspective. |
| AI governance / control mechanisms | Partial | Covers governance extensively, but at the **organisational/regulatory/policy level** (NIST RMF, EU AI Act, ISO standards). Does NOT address **runtime architectural governance** — i.e., gate functions, admissible action spaces, or state-conditioned AI participation control. |
| Low-resource environments | No | Not addressed. All frameworks and case studies assume well-resourced institutional contexts. |
| Decision architecture formalisation | No | No formal decision architecture is defined. No state variables, gate functions, or action spaces. |
| Human role in decision-making | Partial | Discusses human oversight as a trustworthiness principle (EU AI Act, NIST RMF). The Swedish PES case study examines human–AI collaboration. However, the human role is discussed at a governance-policy level, not as a formalised element of a decision architecture. |
| Socio-technical evaluation | Partial | The NIST AI RMF is explicitly described as adopting a "sociotechnical approach." The OHCA case study uses sociotechnical scenarios for evaluation. However, no socio-technical evaluation methodology is developed or applied systematically. |
| Coastal fisheries / maritime domain | No | Not mentioned. |

**Mid-Extraction Relevance Gate:** 0 Yes, 4 Partial → **REDUCED EXTRACTION** (Sections 4–7 and 12–13 only).

---

### 4. Decision Architecture Analysis

- **Architecture structure:** The paper does not propose or analyse any runtime decision architecture. It reviews organisational governance frameworks (NIST AI RMF's Map–Measure–Manage–Govern cycle; AI-TMM's five-step maturity process; ISO/IEC 42001's ten-clause management system). These are **lifecycle governance structures**, not runtime decision-making architectures.
- **Layered architecture / safety constraints:** The EU AI Act's four-tier risk categorisation (unacceptable, high-risk, limited-risk, minimal-risk) is the closest analogue to a layered governance structure — but it operates at the **regulatory classification level** (classifying AI *systems* by risk category), not at the **runtime operational level** (classifying environmental *states* to control AI behaviour within a single system).
- **Rule-based constraints before AI reasoning:** Not addressed at the architectural level. The paper discusses bias mitigation techniques (pre-processing, in-processing, post-processing) as interventions in the ML pipeline, but these are not framed as deterministic safety gates preceding AI reasoning.
- **Boundary between deterministic control and AI reasoning:** Not defined. The paper treats governance as an organisational/regulatory overlay on AI systems, not as an internal architectural boundary within a decision system.
- **Failure modes / fallback:** The Robodebt case study illustrates failure due to absence of human oversight. The OHCA case study notes false positives as a failure mode. However, no systematic fallback architecture is described.

---

### 5. Formal Model and Mathematical Representation

- **Formal model:** None. The paper does not define any formal model of a decision system. No state variables, safety functions, gate functions, or action spaces are specified.
- **Comparison to E → S = f(E) → (G(S), A_AI(S)) → AI(E):** No comparable formal pipeline exists in this paper. The frameworks reviewed operate at the organisational governance level and are not expressed as mathematical structures governing runtime AI behaviour.
- **State-dependent recommendation restriction:** Not modelled. The EU AI Act's risk categories restrict what *types of AI systems* are permitted in different risk classes — but this is a static, design-time regulatory classification, not a runtime state-conditioned restriction on AI output scope within a single system.
- **Safety Dominance Property:** No formal safety property is defined or referenced. The paper discusses trustworthiness *principles* (fairness, transparency, etc.) but not formal *properties* guaranteeing that AI outputs remain within state-determined bounds.
- **Formalisation purpose:** Not applicable — no formalisation is present.

---

### 6. Safety State Classification

- **Classification of operational conditions:** The EU AI Act classifies AI **systems** into four risk tiers: unacceptable, high-risk, limited-risk, and minimal/no-risk. This is a **regulatory product-classification scheme**, not an environmental state classification within a running system.
- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:** Fundamentally different in scope and mechanism. The EU AI Act classifies the *system itself* at design/deployment time. The DSR architecture classifies *environmental conditions* at runtime to dynamically control AI behaviour. The Act's risk tiers do not vary with real-time operational state.
- **Differentiation of AI recommendation scope across safety levels:** No. The EU AI Act's risk tiers determine whether an AI system is *permitted to exist* (unacceptable = banned) or must meet certain *compliance requirements* (high-risk = conformity assessment). Within a permitted system, there is no mechanism analogous to restricting AI advisory scope based on classified runtime safety state.
- **CAUTION-equivalent mode:** Not present. The Act's framework is binary at each tier boundary (permitted vs. banned; compliant vs. non-compliant) — there is no intermediate mode where an AI system is permitted to operate but with restricted output scope conditioned on environmental state.

---

### 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (equivalent to G(S)) | Partial | The EU AI Act's "unacceptable risk" category bans certain AI applications entirely (facial recognition in public spaces, social scoring). This is a **static, regulatory-level** participation gate — not a runtime, state-conditioned gate function. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (equivalent to A_AI(S)) | No | No framework reviewed in this paper governs the *scope of AI recommendations* conditioned on classified environmental state. Compliance requirements (transparency obligations, bias audits) constrain how AI systems must be built and monitored — not what specific recommendation types they may generate at runtime. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | No | Not addressed. All governance operates at the organisational/regulatory level, not at the runtime environmental-state level. |

- **Binary vs. graduated governance:** The governance frameworks reviewed are either binary (permitted/banned, compliant/non-compliant) or operate on a static risk-tier scale (EU AI Act's four tiers). None implements a **graduated runtime governance model** where AI participation and advisory scope dynamically adjust based on classified environmental state.
- **State-conditioned Level 2 governance:** Not present in any reviewed framework. The closest analogue — the EU AI Act's tiered risk classification — is static and applies to the system as a product category, not to real-time operational states.
- **Support for (G(S), A_AI(S))?** The paper **indirectly supports the motivation** for the DSR architecture's two-level governance pair by demonstrating that existing governance frameworks operate exclusively at the organisational/regulatory level and do not address runtime, state-conditioned governance of AI behaviour within a single decision system. This represents a gap that the DSR architecture fills.

---

### 12. Key Concepts and Definitions

- **AI trustworthiness components:** Fairness, transparency, privacy, accountability, security — defined as the five pillars of trustworthy AI, consistent with EU AI HLEG and NIST AI RMF.
- **EU AI Act risk categories:** Unacceptable risk, high risk, limited risk, minimal/no risk — a four-tier regulatory classification of AI systems.
- **NIST AI RMF core functions:** Map, Measure, Manage, Govern — lifecycle governance activities.
- **AI-TMM Maturity Indicator Levels (MILs):** Structured evaluation of organisational AI trustworthiness maturity across seven trust pillars.
- **SAFE metrics (Giudici & Raffinetti, 2023):** Sustainability, Accuracy, Fairness, Explainability — unified under the Lorenz curve framework for AI trustworthiness measurement in finance.
- **Sociotechnical approach:** The NIST AI RMF's recognition that AI harms arise from combining technical and social factors — relevant to the DSR research's socio-technical evaluation theme.

---

### 13. Limitations and Unsolved Problems

- **Stated limitations:**
  - NIST AI RMF lacks specific technical implementation guidance; its voluntary nature may hinder consistent adoption.
  - AI-TMM relies on self-assessment, risking biased evaluations without external audits.
  - ISO/IEC standards are slow to evolve and emphasise compliance over innovation.
  - KAIRI's quantitative focus may underrepresent qualitative trust dimensions.
  - Trade-offs between competing trustworthiness dimensions (fairness vs. efficiency, privacy vs. transparency) remain unresolved.
  - Current metrics fail to capture intersectional biases and dynamic context sensitivity.
- **Gaps aligning with my research:**
  - **All governance frameworks reviewed operate at the organisational/regulatory level.** None addresses runtime, state-conditioned governance of AI behaviour within a single decision system. This confirms the gap that the DSR two-level governance pair (G(S), A_AI(S)) is designed to fill.
  - **No framework distinguishes between participation governance (whether AI operates) and advisory scope governance (what AI may recommend).** The paper's entire governance landscape is either binary (permit/block) or static-tiered — with no CAUTION-equivalent mode where AI operates under restricted recommendation scope.
  - **No formal Safety Dominance Property.** None of the reviewed frameworks defines a formal guarantee that AI outputs remain within state-determined bounds.
  - **The paper acknowledges that trustworthiness trade-offs are context-dependent** but provides no mechanism for dynamically adjusting AI behaviour in response to changing environmental conditions — which is exactly what the DSR architecture's state-conditioned governance provides.

---

### 16. Relation to My Research and Positioning

- **Governance level:** The paper reviews **organisational/regulatory governance** (Level 0, so to speak — above and outside the runtime system). It does not implement Level 1 (participation control) or Level 2 (output-scope control) in the architectural sense defined by the DSR framework.
- **State-conditioned governance:** Not present. All governance is static or lifecycle-based.
- **Distance from (G(S), A_AI(S)):** Very far. The paper operates in a fundamentally different governance layer — regulatory/policy vs. runtime/architectural.
- **Formal safety property:** None defined.
- **Gap my research addresses:** The paper thoroughly documents existing governance frameworks, all of which operate at the organisational/regulatory level. None provides a mechanism for **runtime, state-conditioned governance** of AI behaviour within a single decision system. The DSR architecture's two-level governance pair fills this gap by operating *inside* the system, dynamically adjusting AI participation and advisory scope based on classified environmental state.

**Positioning paragraph:** Nastoska et al. (2025) provides a comprehensive survey of AI trustworthiness frameworks and metrics operating at the organisational and regulatory governance level. The paper is useful as **broad background** for situating the DSR research within the wider AI governance landscape — demonstrating that substantial governance infrastructure exists for managing AI trustworthiness at the policy, compliance, and organisational levels. However, it simultaneously confirms a significant gap: none of the reviewed frameworks (NIST AI RMF, AI-TMM, ISO/IEC standards, KAIRI, EU AI Act) addresses **runtime architectural governance** — the internal mechanisms by which a safety-critical AI decision system dynamically adjusts its own behaviour based on classified environmental state. The paper can be cited as evidence that existing governance approaches, while extensive at the organisational level, leave the runtime governance gap unaddressed — precisely the gap that the DSR architecture's state-conditioned two-level governance pair (G(S), A_AI(S)) is designed to fill.

---

### 17. Overall Relevance Score

**⭐⭐ Low — tangentially related**

**Justification:** The paper is a broad survey of AI trustworthiness metrics and organisational governance frameworks. It does not address runtime decision architecture, formal safety-state classification, gate functions, admissible action spaces, hybrid AI design, low-resource environments, or the coastal fisheries domain. Its governance discussion operates at a fundamentally different level (organisational/regulatory) from the DSR architecture's runtime governance. The paper provides useful background context for the broader AI governance landscape but does not contribute directly to any of the core architectural themes of the DSR research. The ⭐⭐ rating reflects its potential utility as a background reference demonstrating that existing governance approaches operate exclusively at the organisational level — supporting the claim that runtime state-conditioned governance remains an unaddressed gap.
