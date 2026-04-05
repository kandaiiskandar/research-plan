# Literature Review Extraction
## Paper: Harnessing AI to Map Global Fishing Vessel Activity

---

## 1. Paper Identity

- **Full title:** Harnessing AI to Map Global Fishing Vessel Activity
- **Authors:** Heather Welch, Robert T. Ames, Namrata Kolla, David A. Kroodsma, Luca Marsaglia, Tommaso Russo, Jordan T. Watson, Elliott L. Hazen
- **Year:** 2024
- **Venue:** *One Earth*, 7, 1685–1691. DOI: 10.1016/j.oneear.2024.09.009 (Cell Press, open access)
- **Type of paper:** Primer / overview article (non-empirical; narrative review of AI applications in fisheries monitoring and surveillance)

---

## 2. Core Contribution

- **Main problem:** Roughly 98% of the global fishing fleet (~4.9 million vessels) do not publicly broadcast their locations, creating massive transparency gaps that enable illegal, unreported, and unregulated (IUU) fishing, overfishing, bycatch of protected species, and human rights violations including forced labour.
- **Proposed solution:** AI (specifically machine learning — supervised, unsupervised, and reinforcement learning) applied to satellite and sensor data (AIS, VMS, SAR, nighttime lights, daytime imagery, electronic monitoring, hydrophones, cameras) to track and detect fishing vessels, identify fishing activity, decode fishing behaviours, map marine resources, and combat IUU fishing.
- **Main contributions:**
  - Comprehensive overview of the AI + fisheries monitoring landscape as of 2024
  - Taxonomy of AI systems used: supervised (classification, regression), unsupervised (clustering, dimension reduction), reinforcement (strategy optimisation), with shallow and deep learning variants
  - Survey of vessel tracking technologies (VMS, AIS) and detection technologies (SAR, optical imagery, nighttime lights, local sensors)
  - Applications: fishing activity identification, gear type classification, vessel trajectory forecasting, métier clustering, IUU risk mapping, forced labour risk modelling, bycatch risk assessment, marine spatial planning
  - Outlook on future AI applications: climate-driven fisheries redistribution forecasting, blockchain for seafood traceability, LLMs for fisheries management queries, mobile marine protected areas
- **What is novel:** Not a primary research contribution — it is a primer synthesising existing work for a broad audience. The novelty is in the comprehensive mapping of the AI-fisheries-monitoring ecosystem across tracking, detection, and application layers.

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | No | AI applications described are purely probabilistic (ML models). No rule-based + probabilistic hybrid architecture. |
| Safety-critical AI decision-making | No | Focuses on monitoring and surveillance, not on safety-critical operational decision-making (e.g., go/no-go decisions for fishing trips). |
| AI governance / control mechanisms | No | Brief mention of human-in-the-loop in outlook section, but no governance architecture, gating mechanism, or AI control framework. |
| Low-resource environments | No | The AI systems described rely on big data, satellite constellations, cloud computing, and substantial computational infrastructure — the opposite of low-resource. |
| Decision architecture formalisation | No | No decision architecture or formal model. |
| Human role in decision-making | **Partial** | Outlook section advocates for human-in-the-loop approach and human oversight to mitigate AI biases, but this is a brief normative statement, not a substantive treatment. |
| Socio-technical evaluation | No | No socio-technical evaluation framework. |
| Coastal fisheries / maritime domain | **Yes** | Central focus. Covers the entire AI-for-fisheries-monitoring ecosystem: vessel tracking, detection, fishing activity classification, IUU detection, bycatch risk, marine spatial planning. |

**Mid-Extraction Relevance Gate:** 1 Yes + 1 Partial → **REDUCED EXTRACTION** (Sections 4–7 and 12–13 only; Sections 8–11 and 14–15 skipped)

---

## 4. Decision Architecture Analysis

- **Decision-making structure:** None. The paper describes AI systems for *monitoring and surveillance* — producing information about where vessels are fishing and what they are catching. It does not describe any decision architecture for how fishers, managers, or enforcement agencies should act on this information.
- **Layered architecture / governance structure:** None. The paper surveys a constellation of sensing and AI technologies but does not propose any layered decision architecture or governance structure that controls how decisions are made based on AI outputs.
- **Rule-based constraints or safety checks:** None. The AI systems described are pure ML models (classification, regression, clustering, reinforcement learning) without pre-AI safety gates, rule-based constraints, or deterministic safety checks.
- **Boundary between deterministic control and AI reasoning:** Not defined. All described systems are probabilistic ML.
- **Failure modes / fallback behaviour:** Not addressed architecturally. The outlook section notes that AI is "highly capable of making mistakes" and mentions racial biases in cancer detection and facial recognition software as cautionary examples. For fisheries, the paper notes that tracking data are biased toward large vessels from wealthy countries, and that AI systems may "perpetuate or even amplify these biases." The recommended mitigation is human-in-the-loop oversight, not an architectural fallback mechanism.

**Summary:** This paper has no decision architecture. It is an information-production paper — AI generates data and insights (vessel locations, fishing activity classifications, IUU risk maps) that inform human decisions, but the paper does not describe or formalise how those human decisions should be structured, governed, or constrained.

---

## 5. Formal Model and Mathematical Representation

- **Formal model:** None. The paper describes ML algorithms at a tutorial level (supervised/unsupervised/reinforcement, shallow/deep) but does not define any formal model of a decision system.
- **Comparison to E → S = f(E) → (G(S), A_AI(S)) → AI(E):** No comparison possible. The paper describes AI that processes environmental/vessel data to produce information products, but there is no safety state function, no gate function, no admissible action space.
- **State-dependent recommendation restriction:** Not present.
- **Safety Dominance Property:** Not present.
- **Formalisation purpose:** N/A.

---

## 6. Safety State Classification

- **Discrete risk/safety levels:** The paper describes AI systems that produce *risk maps* (IUU risk, forced labour risk, bycatch risk), which could be interpreted as continuous risk scores. However, these are information products, not operational safety state classifications that condition system behaviour. There is no tripartite or binary safety state classification.
- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:** No comparison possible. The risk maps described are outputs *of* AI systems for human consumption, not inputs *to* a governance function that controls AI behaviour.
- **AI recommendation scope differentiation:** Not present. The AI systems described always produce full outputs regardless of risk level. There is no concept of restricting what AI may recommend under elevated risk conditions.

---

## 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (equivalent to G(S)) | No | AI systems described are always-on monitoring tools. No gate controls whether AI participates based on operational state. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (equivalent to A_AI(S)) | No | No restriction on AI output scope. ML models produce whatever outputs they are trained to produce, without state-conditioned constraints. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | No | No governance model of any kind. |

- **Governance type:** None. The paper's brief advocacy for human-in-the-loop (in the outlook) is a normative recommendation, not an implemented governance mechanism. The specific recommendation — "use AI to determine if a vessel is at high risk for IUU, but perform a cargo inspection before prosecuting it" — is an enforcement principle, not an AI governance architecture.
- **Supports or contradicts two-level governance pair:** Neither supports nor contradicts. The paper is orthogonal — it describes the information-production layer (AI generating fisheries intelligence), while my research addresses the decision-governance layer (how AI recommendations are constrained by environmental safety state). The information products described here (vessel tracking, fishing activity detection, risk maps) could serve as *inputs* to the environmental state vector E in my architecture, but the paper does not address what happens after the information is produced.

---

## 12. Key Concepts and Definitions

| Concept | Definition / Description | Relevance |
|---|---|---|
| **VMS (Vessel Monitoring System)** | GPS-based vessel position tracking designed for surveilling commercial fishing vessels; usually confidential | Directly relevant as a data source in my target domain; part of the information environment that feeds my state vector E |
| **AIS (Automatic Identification System)** | GPS-based vessel position tracking designed for collision avoidance; publicly accessible | Same as above |
| **Dark vessels** | Fishing vessels not tracked by AIS or VMS — either not equipped or deliberately disabling transponders | Contextual understanding of the monitoring gaps in my target domain |
| **IUU fishing** | Illegal, unreported, and unregulated fishing — results in up to $25 billion in annual economic losses and is associated with forced labour | Domain background; motivates the need for better fisheries governance |
| **Electronic monitoring** | Vessel-mounted cameras recording gear deployment and catch handling; analysed via computer vision | Potential data source for validating fishing trip outcomes in my domain |
| **Métiers** | Functional fishing groups — units with similar vessel size and common exploitation patterns | Domain concept relevant to understanding vessel classification in my target context |
| **SAR (Synthetic Aperture Radar)** | Satellite radar imaging that penetrates clouds and operates day/night to detect vessels | Background technology awareness |
| **Computer vision** | AI application leveraging deep learning to interpret visual data from images/videos | Background AI concept |

---

## 13. Limitations and Unsolved Problems

- **Stated limitations (of the field, not the paper):**
  - 98% of the global fleet (~4.9M vessels) do not broadcast locations publicly
  - VMS/AIS biased toward larger vessels — less than 1% of vessels under 12m have AIS
  - Public satellite imagery struggles to resolve objects smaller than 10m and distinguish vessels from nearshore objects
  - Low satellite revisit rates make it difficult to track dark vessels over time, especially offshore
  - Electronic monitoring implemented on fewer than 1,000 vessels globally
  - AI training data historically scarce — systems require large volumes of labelled data
  - AI systems may perpetuate or amplify biases in tracking data (biased toward large vessels from wealthy countries)

- **Unsolved problems / future work:**
  - Climate-driven redistribution of fisheries and species — forecasting needed
  - Blockchain for seafood supply chain traceability (exploratory)
  - LLMs for fisheries management query assistance (under consideration)
  - Mobile marine protected areas informed by ML species distribution models
  - Real-time IUU detection (currently 4-6 hour delay, mostly satellite data transfer)
  - Forecasting IUU before it occurs (active competition)

- **Alignment with my research gaps:**
  - The paper does **not** identify the lack of a governance architecture for AI decision-making in fisheries as a gap
  - The paper does **not** address safety-critical decision support for fishers (go/no-go, trip timing, duration)
  - The paper does **not** discuss low-resource deployment constraints (connectivity, compute, offline capability)
  - **However**, the paper comprehensively documents the monitoring/surveillance layer that produces the kind of environmental data (weather, marine conditions, vessel tracking) that feeds into my architecture's environmental state vector E. It also highlights the significant data gaps and biases in small-scale fisheries monitoring — the exact context my architecture targets.

---

## 16. Relation to My Research and Positioning

- **Governance levels implemented:** None.
- **State-conditioned governance:** N/A.
- **Proximity to (G(S), A_AI(S)):** Very distant. The paper operates at the monitoring/surveillance layer, not the decision-governance layer.
- **Safety Dominance Property:** Not defined.
- **Gap my research fills:** This paper demonstrates the state of the art in AI for fisheries *monitoring* — producing information about where vessels fish, what they catch, and where IUU risk is high. But it does not address how AI should be used for fisheries *decision support* — advising individual fishers on whether to go fishing, when to depart, or how long to stay at sea, under varying safety conditions. My research fills exactly this gap: providing a governance architecture that takes the kind of environmental and vessel data surveyed by Welch et al. and uses it to generate safety-state-conditioned recommendations for individual fisher decision-making.

**Positioning paragraph:** Welch et al. (2024) serves as **domain background** for my literature review, documenting the current landscape of AI applications in fisheries monitoring and surveillance. It establishes that AI is well-developed for producing fisheries intelligence at scale — vessel tracking, fishing activity detection, IUU risk mapping — but this intelligence serves fleet-level management and enforcement, not individual fisher-level decision support. The paper's extensive coverage of VMS, AIS, satellite imagery, and electronic monitoring provides context for understanding the data environment within which my architecture operates, and its documentation of small-scale fisheries' underrepresentation in existing monitoring systems directly supports my motivation for targeting low-resource, small-scale coastal fisheries. The brief advocacy for human-in-the-loop oversight in the outlook section aligns with my architecture's decision-support (not decision-automation) positioning, but remains a normative statement without architectural implementation. The paper confirms that while AI's *information-production* capabilities in fisheries are rapidly advancing, AI's *decision-governance* capabilities — controlling when AI participates and what it may recommend based on classified safety state — remain unaddressed, even in the most comprehensive reviews of the field.

---

## 17. Overall Relevance Score

### ⭐⭐ Low

**Justification:** The paper is directly relevant to one theme (coastal fisheries/maritime domain) and partially relevant to one other (human role, via brief HITL mention). It provides useful domain background on the AI-for-fisheries monitoring ecosystem and documents the data sources (VMS, AIS, satellite imagery) and data gaps (small-scale fisheries underrepresentation) relevant to my target context. However, it contains no decision architecture, no governance model, no safety state classification, no formal model, and no treatment of safety-critical operational decision-making. Its value is limited to domain-context citation — establishing what AI *currently does* in fisheries (monitoring/surveillance) as a contrast to what my research proposes AI *should also do* (safety-state-governed decision support).
