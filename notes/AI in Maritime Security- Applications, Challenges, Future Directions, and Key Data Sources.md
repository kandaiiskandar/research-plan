## Literature Review Extraction
### Paper: AI in Maritime Security: Applications, Challenges, Future Directions, and Key Data Sources

---

## Early Relevance Check: PASSED (marginal)

1. **Core research themes?** Partial — maritime domain (Theme 8), touches on safety-critical AI and human-AI interaction in surveillance contexts
2. **Contributes to relevant areas?** Partial — maritime AI applications, but focused on surveillance/detection rather than decision support architecture or governance
3. **Citable in literature review?** Yes — as domain background establishing the current state of AI in maritime environments, and as evidence that existing maritime AI lacks governance architecture

**→ Proceed with reduced extraction.**

---

### 1. Paper Identity

- **Title:** AI in Maritime Security: Applications, Challenges, Future Directions, and Key Data Sources
- **Authors:** Kashif Talpur, Raza Hasan, Ismet Gocer, Shakeel Ahmad, Zakirul Bhuiyan
- **Year:** 2025 (Published 31 July 2025; received 30 June 2025)
- **Venue:** *Information* 2025, 16, 658 (MDPI, open access)
- **DOI:** https://doi.org/10.3390/info16080658
- **Type:** Systematic literature review (88 papers from 258 initially identified, covering 2020–2025)

---

### 2. Core Contribution

- **Problem addressed:** Traditional maritime surveillance methods (coastal radar, patrol vessels, satellite imagery, human observation) are insufficient against the volume, stealth, and sophistication of modern maritime security threats including illegal fishing, smuggling, trafficking, and environmental violations. Manual monitoring cannot keep pace with the scale and speed of incoming maritime data.
- **Proposed solution / key finding:** The paper surveys state-of-the-art deep learning techniques applied to maritime security across three capability areas: object detection and tracking (CNNs, YOLO variants, Transformers), anomaly detection in vessel behaviour (RNNs, LSTMs, GRUs, autoencoders), and multi-sensor fusion (EO/IR, radar, AIS, SAR, acoustic). It also catalogues key datasets for training maritime deep learning models.
- **Main contributions:**
  1. Comprehensive review of deep learning architectures for maritime vessel detection, anomaly detection, and situational awareness (2020–2025)
  2. Analysis of multimodal data fusion strategies (early, mid, late fusion) for maritime surveillance
  3. Survey of specific maritime security applications: illegal fishing detection, piracy prevention, smuggling detection, environmental monitoring, search and rescue
  4. Catalogue of key datasets for maritime deep learning research (Tables 4–5)
  5. Identification of open challenges: data scarcity, small object detection, explainability, real-time edge deployment, algorithmic bias
- **Novelty:** The paper is a survey, not a novel architecture. Its value lies in comprehensiveness across the maritime security AI landscape and the compiled dataset catalogue. It identifies explainability and real-time deployment as significant open gaps.

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | No | Paper surveys deep learning architectures but does not address rule-based + probabilistic hybrid governance. Mentions that traditional anomaly detection used rule-based systems but frames deep learning as their replacement, not their complement. |
| Safety-critical AI decision-making | Partial | Maritime security is inherently safety-critical. The paper discusses decision support for maritime operators (Section 3.3) and the need for explainability to build operator trust. However, it does not address safety-critical *architecture* or formal safety constraints. |
| AI governance / control mechanisms | No | No governance mechanisms, gate functions, or AI participation control discussed. AI systems are treated as always-on detection/classification tools without any governance over when or how they operate. |
| Low-resource environments | Partial | Discusses edge computing challenges (lightweight models on USVs, drones), data scarcity in maritime domain, and bandwidth-constrained environments. These are resource constraints but framed as engineering challenges, not as a design philosophy for low-resource contexts. |
| Decision architecture formalisation | No | No formal model of any kind. No state variables, safety functions, or action spaces. |
| Human role in decision-making | Partial | Section 3.3 describes decision support and visualisation for human operators — automated alerts, geo-referenced displays, colour-coded vessel statuses, XAI overlays. Operators remain final decision-makers in MDA systems. |
| Socio-technical evaluation | No | No socio-technical evaluation. Paper is a technical survey of deep learning methods. |
| Coastal fisheries / maritime domain | Partial | Maritime domain throughout, including a dedicated section on illegal fishing detection (Section 4.1). However, the focus is on *surveillance and enforcement* (detecting illegal fishing from satellites/AIS), not on *fisheries decision support* for fishers themselves. |

**Mid-Extraction Relevance Gate:** 0 Yes, 4 Partial → **REDUCED EXTRACTION** (Sections 4–7, 12–13, 16–17)

---

### 4. Decision Architecture Analysis

- **Decision-making structure:** The paper describes Maritime Domain Awareness (MDA) systems as a processing pipeline: sensor data ingestion → deep learning detection/classification → fusion → alert generation → human operator decision support (Section 3.3). This is a sequential perception-to-display pipeline, not a decision architecture with governance layers.
- **Layered architecture / governance structure:** None. The deep learning models are always active; there is no mechanism governing *when* AI operates or *what* it may recommend based on conditions. The fusion architectures (early/mid/late) are data processing layers, not governance layers.
- **Rule-based constraints before AI:** Not present. The paper notes that traditional rule-based anomaly detection has been *replaced* by deep learning, not combined with it: "Traditionally, rule-based systems were used to define what constitutes 'normal' behaviour, but such methods often lack the flexibility to adapt to dynamic maritime environments." This framing positions rules and AI as alternatives rather than complementary layers.
- **Boundary between deterministic control and AI reasoning:** Not defined. All decision logic is within probabilistic deep learning models. No deterministic safety layer constrains AI outputs.
- **Failure modes / fallback behaviour:** Not addressed architecturally. The paper notes challenges with false positives, performance degradation in adverse weather, and detection failures for small objects — but these are treated as model accuracy problems, not as triggers for architectural fallback. No fallback to deterministic or human-only modes is described.

**Assessment:** The MDA pipeline described is purely perception-oriented: detect → classify → alert → display. There is no governance layer, no state-dependent modulation of AI behaviour, and no formal boundary between AI and human authority. This is representative of the current state of maritime AI: AI as a perception tool with implicit always-on status, lacking the governance architecture my research proposes.

---

### 5. Formal Model and Mathematical Representation

- **Formal model defined?** No. The paper contains no formal model. Deep learning architectures are described at the algorithmic level (CNN layers, attention mechanisms, loss functions) but no system-level formal model of decision-making, safety states, or governance exists.
- **Comparison to E → S = f(E) → (G(S), A_AI(S)) → AI(E):** Not applicable. The paper's implicit pipeline is: Sensor Data → DL Model → Detection/Classification Output → Human Operator. There is no safety state classification, no gate function, and no state-conditioned action space.
- **State-dependent recommendation restriction?** No. AI models always produce the same type of output (detections, classifications, alerts) regardless of environmental conditions. There is no variation in AI output scope across safety states.
- **Safety Dominance Property?** No. No formal safety property of any kind.
- **Formalisation purpose:** N/A.

---

### 6. Safety State Classification

- **Discrete risk/safety levels?** No. The paper does not classify environmental or operational conditions into risk levels. Environmental conditions (weather, sea state, lighting) are discussed as factors affecting *model performance*, not as inputs to a safety state function.
- **Comparison to S ∈ {SAFE, CAUTION, UNSAFE}:** The paper implicitly acknowledges varying conditions — adverse weather degrades detection, nighttime requires different sensors, cluttered scenes increase false positives — but these are framed as engineering challenges for model robustness, not as classified states that should govern AI behaviour.
- **AI recommendation scope differentiation across levels?** No. The paper's approach is to make AI work in *all* conditions (via multimodal fusion, SAR for night/weather, lightweight models for edge). The idea that AI should *restrict its output scope* or *disengage* under certain conditions is absent.

**Assessment:** This is a significant finding for my literature review. The maritime AI literature, as surveyed here, treats environmental variability as a model robustness problem to be solved through better architectures and fusion — not as a governance input that should modulate AI participation. My architecture takes the opposite approach: environmental conditions are inputs to a safety state function that governs AI behaviour, rather than challenges to be overcome through better models.

---

### 7. Governance Level Analysis

| Level | Question | Implemented? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? | No | AI is always on. No mechanism to disable or restrict AI based on conditions. |
| **Level 2 — Advisory scope governance** | What may AI recommend? | No | AI always produces the same output types (detections, classifications, alerts). No state-dependent restriction on output scope. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | No | No state classification; no governance pair. |

- **Binary switch vs. graduated governance?** Neither. AI is ungoverned — it operates continuously without any participation control.
- **Support for two-level governance pair?** The paper provides *indirect* support by documenting the problems that ungoverned AI creates: false positives under adverse conditions, performance degradation in cluttered scenes, unexplainable alerts. These are precisely the problems that a state-conditioned governance model would mitigate — by restricting or disabling AI under conditions where its reliability drops below acceptable thresholds.

---

### 12. Key Concepts and Definitions

- **Maritime Domain Awareness (MDA):** Integrated understanding of vessel activities for security and safety, combining deep learning analytics with operational decision support. Ingests satellite, sensor, AIS, and OSINT data into a processing pipeline.
- **Multimodal data fusion:** Integration of heterogeneous sensor data (EO, IR, radar, AIS, SAR, acoustic) to compensate for individual sensor limitations. Categorised as early fusion (pixel-level), mid fusion (feature-level), or late fusion (decision-level).
- **IUU fishing:** Illegal, Unreported, and Unregulated fishing — a global problem costing billions annually and threatening marine ecosystems and food security. The FAO estimates up to 26 million tons of IUU fishing worth USD 23 billion.
- **Dark vessels:** Vessels operating without AIS transponders, making them invisible to standard tracking systems. Detecting dark vessels requires satellite imagery, SAR, or nighttime light detection.
- **Edge computing for maritime AI:** Deployment of lightweight models (e.g., Tiny YOLO variants) on specialised hardware (NVIDIA Jetson, Google Coral) aboard USVs, buoys, or drones for in-situ inference, transmitting only metadata to command centres.
- **Explainable AI (XAI) in maritime context:** Techniques including Grad-CAM, SHAP, and saliency maps to justify AI-generated alerts for human operators, identified as a significant open research gap.

---

### 13. Limitations and Unsolved Problems

- **Stated limitations of the survey:**
  - Focused on 2020–2025 literature; may miss relevant earlier foundational work
  - Maritime data access is constrained by confidentiality and security concerns
  - Many reviewed datasets are limited in scale, diversity, or modality coverage

- **Unsolved problems / open challenges identified:**
  1. **Data scarcity and quality:** Maritime security datasets are limited, often imbalanced (rare anomalies vs. normal operations), regionally biased, and sometimes confidential
  2. **Small/occluded object detection:** Detecting small vessels, inflatable boats, and objects in cluttered or reflective maritime backgrounds remains difficult
  3. **Environmental robustness:** Model performance degrades under adverse weather, sea states, lighting changes, and reflections
  4. **Real-time edge deployment:** Advanced architectures are computationally heavy; lightweight models compromise accuracy
  5. **Explainability:** Fully interpretable deep learning systems for maritime security are identified as a clear literature gap
  6. **Algorithmic bias:** Models trained on regionally biased datasets may unfairly target specific vessel types or regions
  7. **Sensor fusion complexity:** Temporal synchronisation, spatial alignment, and handling of sensor-specific noise across heterogeneous data streams

- **Gaps aligned with my research:**
  - **No governance architecture.** The entire surveyed literature treats AI as an always-on perception tool. No paper implements a mechanism to govern *when* AI should participate or *what scope of output* AI should produce based on environmental conditions. This is the fundamental gap my architecture addresses.
  - **No safety state classification for AI governance.** Environmental conditions are treated as model robustness challenges, not as inputs to a safety state function. My architecture formalises this with S = f(E).
  - **No CAUTION mode.** AI either works (producing detections/alerts) or fails (performance degradation). There is no intermediate mode where AI operates with restricted output scope.
  - **No Safety Dominance Property.** No formal guarantee constrains AI outputs based on environmental state.
  - **No hybrid governance model.** The paper notes that rule-based systems have been *replaced* by deep learning. My architecture instead *combines* deterministic rules (for safety governance) with probabilistic AI (for advisory generation), preserving the safety guarantees of rules while leveraging AI capabilities.

---

### 16. Relation to My Research and Positioning

- **Governance level implemented:** Neither Level 1 nor Level 2. AI is always on and ungoverned.
- **Proximity to (G(S), A_AI(S))?** Distant. No governance pair of any kind exists in the surveyed literature.
- **Safety Dominance Property?** Not defined.
- **Gap my research addresses:** The paper comprehensively demonstrates that current maritime AI is focused on perception (detection, classification, tracking) without governance. The entire surveyed landscape treats AI as an always-on tool whose problems are solved through better models rather than through architectural governance. My research addresses a fundamentally different layer: not *how well* AI detects, but *when and what* AI is permitted to recommend, governed by classified environmental state.

**Positioning paragraph:** Talpur et al. (2025) serves as **domain background** for my research, establishing the current state of AI applications in the maritime environment. Its primary value is twofold. First, it documents the maritime AI landscape as entirely perception-focused — deep learning for vessel detection, anomaly detection, and surveillance — with no governance architecture governing AI participation or advisory scope. This confirms that the governance gap identified in safety-critical AI literature (Könighofer et al., Dalrymple et al.) extends into the maritime domain specifically. Second, the paper's treatment of environmental variability (weather, sea state, lighting) as a model robustness problem rather than a governance input directly contrasts with my architecture's approach, where environmental conditions feed a safety state function that formally governs AI behaviour. The paper's catalogue of maritime data sources and its discussion of challenges (data scarcity, edge deployment, explainability) also provide useful background for contextualising my coastal fisheries deployment environment. However, the paper operates entirely at the perception/detection layer and contributes nothing to decision architecture, formal governance, or safety-critical AI design.

---

### 17. Overall Relevance Score

**⭐⭐ Low** — Provides useful domain background on the state of AI in maritime environments and confirms that governance architecture is absent from the maritime AI landscape. The illegal fishing detection section and maritime data challenges are tangentially relevant. However, the paper is a surveillance/detection survey with no decision architecture, no governance mechanisms, no formal model, and no focus on decision support for end-users (fishers). Its contribution to my literature review is limited to establishing that maritime AI currently lacks the governance layer my architecture provides.

---

*Functional role in literature review:* **Domain background** — establishes the current state of maritime AI as perception-focused and ungoverned, confirming the governance gap extends into the maritime domain.
