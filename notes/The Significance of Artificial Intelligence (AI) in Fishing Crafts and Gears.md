## Literature Review Extraction
### Mandal, Banerjee & Ghosh (2025) — The Significance of Artificial Intelligence (AI) in Fishing Crafts and Gears

---

### 1. Paper Identity
- **Title:** The Significance of Artificial Intelligence (AI) in Fishing Crafts and Gears
- **Authors:** Arghya Mandal, Mainak Banerjee, Apurba Ratan Ghosh
- **Year:** 2025 (Published 20 January 2025)
- **Venue:** Environmental Science Archives, Vol. IV, Issue 1, pp. 44–58
- **DOI:** 10.5281/zenodo.14698633
- **Type:** Narrative review

---

### 2. Core Contribution
- **Problem:** Traditional fishing crafts and gears face challenges in efficiency, sustainability, and technological capability. AI technologies offer potential to address these limitations.
- **Solution:** A broad narrative overview of AI applications in fishing and aquaculture, covering autonomous navigation, fish detection, smart gears, weather prediction, feeding optimisation, disease detection, and stock management.
- **Main contributions:** Descriptive tables summarising AI applications in fishing crafts (Table 1), AI-enabled fishing gears (Table 2), and AI benefits (Table 3). Suggests statistical methods (t-test, ANOVA, ROI) for evaluating AI integration — though none are actually performed.
- **Novelty:** Limited. The paper is a broad descriptive survey without original analysis, empirical data, formal models, or architectural contributions. It catalogues known AI applications at a surface level.

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | No | Not discussed — AI is treated monolithically |
| Safety-critical AI decision-making | No | "Safety" mentioned briefly as a benefit (weather monitoring, risk assessment) but not treated as an architectural concern or design principle |
| AI governance / control mechanisms | No | No discussion of when, whether, or how AI participation should be controlled or restricted |
| Low-resource environments | No | Technology accessibility/affordability noted as a challenge (Sec. on Cons) but not addressed architecturally |
| Decision architecture formalisation | No | No formal models, pipelines, or architectural specifications |
| Human role in decision-making | Partial | Mentions fishermen using AI-generated recommendations to make decisions, but does not analyse the human role structurally |
| Socio-technical evaluation | No | Not addressed |
| Coastal fisheries / maritime domain | Yes | Core domain — covers AI applications in fishing vessels, gear design, fish detection, and aquaculture |

**Mid-Extraction Relevance Gate:** 1 Yes + 1 Partial → **REDUCED EXTRACTION** (Sections 4–7 and 12–13 only, skip 8–11 and 14–15)

---

### 4. Decision Architecture Analysis
- The paper does not describe any decision architecture. AI is discussed as a collection of standalone capabilities (fish detection, route optimisation, catch prediction, gear optimisation) without any integrated decision pipeline or architectural framework.
- No layered architecture, safety constraint mechanism, or governance structure is presented.
- No rule-based constraints or safety checks applied before AI decisions.
- No boundary defined between deterministic control and AI reasoning.
- Failure modes, fallback behaviour, and override mechanisms are not discussed.

---

### 5. Formal Model and Mathematical Representation
- No formal model is defined. The paper suggests statistical methods (t-test, ANOVA, chi-square, logistic regression, ROI analysis) for evaluating AI integration, but these are proposed as future work — none are actually executed.
- No comparison possible to the DSR pipeline E → S = f(E) → (G(S), A_AI(S)) → AI(E).
- No state-dependent recommendation restriction is modelled.
- No Safety Dominance Property or equivalent is defined.

---

### 6. Safety State Classification
- No classification of operational or environmental conditions into risk or safety levels.
- Weather prediction is mentioned as an AI application (Table 1) but is treated as a standalone capability, not as input to a safety classification function.
- No comparison possible to S = f(E) → {SAFE, CAUTION, UNSAFE}.

---

### 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (G(S)) | No | Not discussed — AI is assumed to always be available and operating |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | No | Not discussed — no distinction between what AI should/shouldn't recommend under different conditions |
| **Levels 1 + 2 unified, state-conditioned** | Both governed by classified environmental state? | No | Not discussed |

- The paper assumes AI operates unconditionally. No governance mechanism of any kind is discussed.

---

### 12. Key Concepts and Definitions
- **AI applications catalogue:** Autonomous navigation, fish detection, oceanographic mapping, weather prediction, energy optimisation, vessel maintenance, catch prediction, fishing effort control (Table 1)
- **AI-enabled gears:** Smart fishing nets, autonomous fishing bots, intelligent lures, drone fishing, automated trawlers (Table 2)
- **AI techniques listed:** Machine learning, deep learning, NLP, computer vision, genetic algorithms, expert systems, robotics/automation
- **Cons of AI in fishing:** Ethical concerns (animal welfare), environmental impact (overfishing risk), bycatch, technology accessibility/affordability, dependence on technology (loss of traditional skills), data privacy

---

### 13. Limitations and Unsolved Problems
- **Stated limitations:** None explicitly stated — the paper does not include a limitations section.
- **Implicit limitations:** The paper is purely descriptive with no empirical data, no formal analysis, and no original contribution beyond cataloguing. Suggested statistical evaluations are not performed.
- **Gaps aligning with my research:**
  - The paper highlights that AI is being applied in fishing but with **zero consideration of safety governance** — when AI should/shouldn't operate, what it should/shouldn't recommend under different safety conditions. This absence is itself evidence of the gap my research addresses.
  - Technology accessibility/affordability is noted as a barrier — relevant to my low-resource theme, but not treated as an architectural design constraint.
  - No mention of environmental safety state classification, graduated AI participation, or any form of AI governance mechanism.

---

### 16. Relation to My Research and Positioning
- The paper implements **neither** Level 1 nor Level 2 governance. AI is treated as an always-on capability.
- No formal safety property is defined.
- The gap is total: the paper demonstrates that domain literature on AI in fishing operates without any concept of safety-gated AI governance.

**Positioning paragraph:** This paper serves as a minor domain background reference illustrating the breadth of AI applications being explored in fishing (vessel navigation, gear optimisation, catch prediction, weather forecasting). Its value to my research is limited to showing that the fisheries domain is adopting AI technologies but without any safety governance framework, safety state classification, or architectural consideration of when and how AI participation should be controlled. The paper's identification of technology accessibility/affordability as a barrier provides peripheral support for my low-resource deployment theme. However, the paper's lack of depth, absence of formal analysis, and narrative-only character limit its citability. For domain background on AI in fisheries, stronger alternatives exist (e.g., Wing & Woodward 2024 in ICES Journal of Marine Science; Kühn et al. 2025 in Reviews in Fisheries Science and Aquaculture).

---

### 17. Overall Relevance Score

**⭐⭐ Low — tangentially related domain background**

**Justification:** The paper touches my fisheries domain and catalogues AI applications, but contributes nothing to my core themes of safety-critical architecture, AI governance, formalisation, or hybrid AI design. It contains no formal model, no architectural framework, no safety state classification, and no governance mechanism. The venue (Environmental Science Archives) is relatively obscure, and stronger peer-reviewed domain references are available. Usable only as a peripheral citation showing the breadth of AI adoption in fisheries — and even for that purpose, better alternatives exist.
