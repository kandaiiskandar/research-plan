## Literature Review Extraction: Tahsin et al. (2025)

---

### 1. Paper Identity

- **Title:** Towards the adoption of AI, IoT, and Blockchain technologies in Bangladesh's maritime industry: Challenges and insights
- **Authors:** Ruthbah Tahsin, Sakib Bin Alomgir Rantu, Mahjabin Rahman, Sheak Salman, Md. Rezaul Karim
- **Year:** 2025 (available online 23 December 2024)
- **Venue:** *Results in Engineering*, Vol. 25, 103825
- **DOI:** 10.1016/j.rineng.2024.103825
- **Type:** Empirical study (expert-based barrier analysis using Delphi + Fuzzy DEMATEL)

---

### 2. Core Contribution

- **Problem addressed:** Developing nations face numerous barriers to adopting AI, IoT, and Blockchain in the maritime sector, but existing research focuses on technologically advanced regions and treats barriers in isolation rather than examining their causal interdependencies.
- **Proposed solution:** A two-phase methodology combining a three-stage Delphi method (to identify and validate 12 key barriers) with Fuzzy DEMATEL (to model causal interdependencies and rank barriers by prominence and influence).
- **Main contributions:**
  - Identification and prioritisation of 12 barriers to AI/IoT/Blockchain adoption in Bangladesh's maritime industry
  - Causal-effect classification of barriers: data security & privacy, interoperability, and education & awareness emerged as the three most significant barriers
  - Distinction between causal barriers (drivers that influence others) and effect barriers (those that are influenced)
  - Contextualised evidence that barriers differ between developing and developed nations — energy efficiency and technology obsolescence rank lowest in Bangladesh, contrasting with findings from advanced economies
- **Novelty:** Applies Fuzzy DEMATEL specifically to Bangladesh's maritime sector, revealing causal structures among barriers rather than simple rankings; emphasises resource-constrained, developing-country context overlooked in prior work.

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | **No** | Paper does not discuss AI architecture or hybrid AI design |
| Safety-critical AI decision-making | **No** | No treatment of safety-critical decision systems or safety constraints on AI |
| AI governance / control mechanisms | **No** | Governance here refers to policy/regulatory governance, not runtime AI control mechanisms |
| Low-resource environments | **Yes** | Core focus: Bangladesh as a resource-constrained developing nation with limited data, infrastructure, connectivity, expertise, and financial capacity |
| Decision architecture formalisation | **No** | No formal decision architecture; methodology is barrier prioritisation via MCDM |
| Human role in decision-making | **No** | Human experts participate in the Delphi/DEMATEL process but the paper does not address human roles in AI-assisted operational decisions |
| Socio-technical evaluation | **Partial** | Evaluates socio-economic and infrastructural barriers to technology adoption; discusses practical implications for workforce, policy, and stakeholder engagement |
| Coastal fisheries / maritime domain | **Partial** | Maritime industry in Bangladesh (shipbuilding, shipping, logistics); not coastal fisheries specifically, but overlapping domain context |

**Mid-Extraction Relevance Gate:** 1 Yes + 2 Partial → **REDUCED EXTRACTION** (Sections 4–7, 12–13, 16–17 only; Sections 8–11, 14–15 skipped).

---

### 4. Decision Architecture Analysis

- **No decision architecture is presented.** The paper does not design or propose a system for AI-assisted decision-making. Its focus is entirely on identifying and ranking pre-adoption barriers using MCDM methodology.
- There is no layered architecture, safety constraint mechanism, or governance structure controlling how decisions are made at runtime.
- No rule-based constraints or safety checks are applied before AI reasoning — the paper operates at the technology adoption strategy level, not the system design level.
- No failure modes, fallback behaviour, or override mechanisms are discussed.
- **Assessment:** This paper contributes zero architectural content. Its value lies exclusively in documenting deployment barriers in a low-resource maritime context.

---

### 5. Formal Model and Mathematical Representation

- The paper employs a formal mathematical methodology (Fuzzy DEMATEL), but this formalises **barrier interdependencies**, not a decision system.
- Key formal elements:
  - Fuzzy linguistic scale converting expert judgments to Triangular Fuzzy Numbers (TFNs)
  - Direct-relation matrix F, normalised matrix S, total-relation matrix M = S(I − S)⁻¹
  - Prominence (D + R) and relation (D − R) metrics for each barrier
  - Threshold value α = 0.265805 for filtering significant causal relationships
- **Comparison to DSR pipeline E → S = f(E) → (G(S), A_AI(S)) → AI(E):** No correspondence. The formal model analyses inter-barrier causal structure, not environmental state classification, gate functions, or admissible action spaces.
- No state-dependent recommendation restriction is modelled.
- No Safety Dominance Property or analogous formal safety property is defined.
- The formalisation is used for **analysis and ranking** — it produces actionable barrier prioritisation, not system design or proof.

---

### 6. Safety State Classification

- **No safety state classification is performed.** The paper does not classify operational or environmental conditions into risk levels.
- No tripartite (SAFE/CAUTION/UNSAFE) or binary (safe/unsafe) scheme is used.
- No thresholds for safety levels are defined.
- No differentiation of AI recommendation scope across safety levels.
- **Assessment:** Entirely absent. The paper operates at the technology adoption barrier level, not the operational safety level.

---

### 7. Governance Level Analysis

| Level | Question | Implemented? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (G(S)) | **No** | Not addressed; paper concerns pre-deployment barriers, not runtime AI control |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | **No** | Not addressed |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | **No** | Not addressed |

- The paper implements **neither** Level 1 nor Level 2 governance in the architectural sense.
- "Governance" in this paper refers to **policy governance** — government regulation, industry standards, stakeholder coordination — not runtime AI participation or advisory scope control.
- The paper **indirectly supports** the motivation for a two-level governance pair by documenting the barriers that make careful AI governance necessary in low-resource maritime environments: data quality concerns, infrastructure limitations, and education gaps all imply that unrestricted AI deployment would be inappropriate and that graduated governance mechanisms are needed.

---

### 12. Key Concepts and Definitions

- **Fuzzy DEMATEL:** A multi-criteria decision-making technique that models causal interdependencies among factors using fuzzy set theory; distinguishes between cause-group and effect-group barriers.
- **Prominence (D + R):** Total importance of a barrier, combining its role as both influencer and receiver.
- **Relation (D − R):** Net causal direction — positive = cause (net influencer), negative = effect (net receiver).
- **12 identified barriers:** Data Availability & Quality (C₁), Infrastructure Limitations (C₂), Cost Constraints (C₃), Industry Collaboration & Standards (C₄), Data Security & Privacy (C₅), Interoperability (C₆), Scalability & Integration (C₇), Power Supply & Energy Efficiency (C₈), Education & Awareness (C₉), Energy Efficiency (C₁₀), Technology Obsolescence (C₁₁), Supply Chain Complexity (C₁₂).
- **Top-3 barriers by prominence:** (C₅) Data Security & Privacy, (C₆) Interoperability, (C₉) Education & Awareness.
- **Causal group barriers** (net influencers): C₁, C₃, C₅, C₆, C₁₂.
- **Effect group barriers** (net receivers): C₂, C₄, C₇, C₈, C₉, C₁₀, C₁₁.

---

### 13. Limitations and Unsolved Problems

- **Stated limitations:**
  - Results are derived from the Bangladeshi maritime sector specifically; generalisability to other regions may be limited.
  - The study predominantly relies on a single methodological approach (Fuzzy DEMATEL); alternative MCDM methods (fuzzy-AHP, fuzzy-TODIM, fuzzy-ANP) could validate findings.
  - Expert panel of 15 professionals — sample size may limit robustness.
- **Unsolved problems / future work:**
  - Investigation of alternative evaluation criteria and additional barriers specific to individual companies.
  - Integration of these technologies into the Industry 5.0 paradigm.
  - Cross-country comparisons to test whether barrier rankings hold in other developing maritime nations.
- **Gaps aligned with my research:**
  - The paper documents **why** AI deployment in low-resource maritime settings is difficult but offers **no solution architecture** for how AI should operate under these constraints. My architecture directly addresses this gap by providing a formal governance mechanism that accounts for environmental uncertainty and resource limitations.
  - The paper does not address **how** AI systems should be governed once deployed — no participation governance (G(S)), no advisory scope governance (A_AI(S)), no Safety Dominance Property. My two-level governance pair fills exactly this gap.
  - The barrier of "education and awareness" as the third-highest-ranked barrier supports my research's emphasis on decision support (human decides) rather than decision automation, and the need for transparent, interpretable AI output in low-resource contexts.

---

### 16. Relation to My Research and Positioning

- **Governance levels implemented:** Neither Level 1 nor Level 2 in the architectural sense.
- **Two-level governance pair:** Not addressed; the paper operates entirely at the pre-deployment barrier analysis level.
- **Formal safety property:** None.
- **Gap my research addresses:** This paper establishes that Bangladesh's maritime industry faces fundamental deployment barriers — data scarcity, infrastructure limitations, security concerns, education gaps — but provides no architectural solution for how AI should operate within these constraints. My research directly addresses this by designing a graduated governance architecture that is inherently resource-aware: deterministic safety classification requires no ML training data, the gate function operates offline, and the CAUTION mode restricts AI scope precisely in the uncertain conditions that low-resource environments frequently produce.

**Positioning paragraph:** Tahsin et al. (2025) serves as **deployment barrier evidence** in my literature review. It provides peer-reviewed, DOI-bearing empirical data on the specific obstacles to AI adoption in a South Asian maritime context (Bangladesh), which is geographically and structurally proximate to my coastal fisheries case study. The paper's finding that data security, interoperability, and education/awareness are the most prominent barriers — with infrastructure limitations ranking fourth — provides citable justification for my architecture's design choices: lightweight deterministic safety classification that does not depend on large datasets, offline-capable gate functions, and human-centred decision support rather than automation. However, the paper contributes no architectural, formal, or governance-level content. It documents the problem space that motivates my solution but does not offer competing or complementary system design.

---

### 17. Overall Relevance Score

**⭐⭐ Low — tangentially related**

**Justification:** The paper is relevant only as deployment barrier evidence for the low-resource maritime domain. It contributes no architectural design, no formal model comparable to the DSR pipeline, no governance mechanisms, and no safety state classification. Its primary citation value lies in: (a) empirical evidence that data scarcity, infrastructure limitations, and education gaps are the dominant barriers to AI adoption in South Asian maritime industries; (b) supporting the argument that AI systems deployed in such contexts require resource-aware, safety-governed architectures rather than unconstrained deployment. The paper belongs in the **domain background / deployment barriers** subsection of the literature review, not in the core architecture or governance sections.

---

### Recommended Citation Uses

| Use | Section | Specific claim |
|---|---|---|
| Deployment barrier evidence | Domain background | Data security, interoperability, and education are the top-3 barriers to AI/IoT/Blockchain adoption in Bangladesh's maritime sector |
| Low-resource justification | Research gap / motivation | Infrastructure limitations (connectivity, computing, power) rank among the top-4 barriers, justifying resource-aware AI architecture design |
| Education/awareness gap | Design rationale | Education and awareness as 3rd-ranked barrier supports decision-support (not automation) paradigm and need for interpretable AI output |
| Developing-country context | Domain background | Barrier profiles differ between developing and developed nations — findings from advanced economies may not generalise to low-resource contexts |
