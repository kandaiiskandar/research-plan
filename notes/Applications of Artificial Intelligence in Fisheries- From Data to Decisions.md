# Literature Review Extraction: Haque & Al Jufaili (2026)
## Applications of Artificial Intelligence in Fisheries: From Data to Decisions

---

## 1. Paper Identity

- **Full title:** Applications of Artificial Intelligence in Fisheries: From Data to Decisions
- **Authors:** Syed Ariful Haque, Saud M. Al Jufaili
- **Year:** 2026 (Published 5 January 2026)
- **Venue:** Big Data and Cognitive Computing, 10(1), 19. MDPI.
- **DOI:** 10.3390/bdcc10010019
- **Type:** Structured review / survey paper

---

## 2. Core Contribution

- **Main problem:** AI applications in fisheries and aquaculture are advancing rapidly across species detection, precision aquaculture, IUU fishing detection, and sensing infrastructure, but these advancements are inconsistently deployed, subject to domain shifts, limited by labeled data scarcity, poorly benchmarked, and lack formal uncertainty quantification for decision-relevant outputs.

- **Proposed solution:** A structured synthesis across four application domains — (1) fisheries genetics & monitoring, (2) precision aquaculture, (3) fisheries management & surveillance, and (4) sensing infrastructure & technology — identifying implementation challenges, failure modes, and a research agenda for transitioning from experimental prototypes to operational, uncertainty-aware, equitable AI infrastructure.

- **Main contributions:**
  - Comprehensive mapping of AI techniques across fisheries domains with tabulated summaries of methods, benefits, limitations, validation context, and data maturity (Tables 1–4)
  - Systematic identification of cross-cutting challenges: dataset bias, model architecture vs. training protocol trade-offs, digital twin / AIoT maturity gaps, metrics/uncertainty deficiencies, and the "operational gap" between prototypes and decision-grade systems
  - Research agenda emphasising standardised multi-region benchmarks, calibrated uncertainty quantification, domain-robust edge algorithms, privacy-preserving data partnerships, and manager-in-the-loop validation

- **Novelty:** Distinguishes itself from prior fisheries AI reviews by explicitly tracing how model errors propagate to management endpoints (stock assessment, harvest control rules, compliance), and by foregrounding the operational gap — the disconnect between ML performance metrics and decision-grade reliability.

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | **Partial** | Mentions hybrid approaches: physics-informed surrogates combined with RL controllers, mechanistic bioenergetic models coupled with generative AI, digital-twin frameworks integrating growth models with ML forecasts. However, "hybrid" here means combining physics/domain knowledge with ML, not rule-based safety governance constraining probabilistic AI. |
| Safety-critical AI decision-making | **Partial** | Discusses safety-adjacent themes: RL controllers needing safety constraints for catastrophic events (aeration failure), action-clipping and safety regulations in RAS controllers, and the need for decision-grade validation. However, does not frame fisheries decision support as a safety-critical AI architecture problem. No safety state classification, no gate function. |
| AI governance / control mechanisms | **Partial** | Discusses fisheries governance (IUU detection, MPA enforcement, transshipment monitoring) and mentions "human-in-the-loop validation" and "manager-in-the-loop trials," but these refer to human oversight of AI outputs for quality assurance, not to formal AI participation governance mechanisms (G(S)) or advisory scope control (A_AI(S)). |
| Low-resource environments | **Partial** | Extensively discusses challenges for smallholder producers: inequitable data access, high AIoT costs, intermittent connectivity in remote coastal regions, edge computing on power-constrained platforms (solar buoys, battery systems), and ROI uncertainty. Does not frame these as architectural design constraints for AI decision systems. |
| Decision architecture formalisation | No | No formal decision architecture. No state variables, safety functions, gate functions, or action spaces defined. The "data to decisions" framework (Figure 3) is conceptual, not formalised. |
| Human role in decision-making | **Partial** | References "human-in-the-loop" validation for IUU detection, electronic monitoring, and protected species oversight. Emphasises "manager-in-the-loop" trials for aquaculture. Discusses XAI (SHAP, Grad-CAM) for farmer trust. However, the human role is discussed as a quality assurance mechanism, not formalised within a decision architecture. |
| Socio-technical evaluation | **Partial** | Discusses adoption barriers (farmer trust, XAI for transparency), equity concerns (smallholder exclusion, Global North monitoring bias), governance challenges (data ownership, privacy, cybersecurity), and the need for participatory design. Does not conduct socio-technical evaluation; identifies it as a gap. |
| Coastal fisheries / maritime domain | **Yes** | Core domain. Covers wild-capture fisheries, aquaculture, coastal monitoring, small-scale fleets, IUU detection, electronic monitoring, and sensing infrastructure across marine and freshwater systems. Directly contextualises the operational environment for my research. |

**Mid-Extraction Relevance Gate:** 1 Yes + 6 Partial → **REDUCED EXTRACTION** (Sections 4–7, 12–13, 16–17)

---

## 4. Decision Architecture Analysis

- **Decision-making structure:** No formal decision architecture is proposed. The paper's "Data to Decisions" conceptual framework (Figure 3) describes a progression from raw data acquisition through AI processing to management actions, but this is a review organising principle, not an architectural specification. Individual systems described within the review follow diverse ad-hoc architectures:
  - Aquaculture: Sensor → ML forecast → control action (feeding, aeration), sometimes with RL optimisation
  - IUU detection: AIS/SAR/VIIRS → anomaly detection → human-validated risk scoring → enforcement
  - Electronic monitoring: Video → CV classifier → human review → regulatory reporting
  - Stock assessment: Echogram → deep learning classification → abundance estimation → harvest control rules

- **Safety constraint mechanism:** Mentioned in passing for RL controllers in RAS: "action-clipping, stringent safety regulations, and physics-informed surrogates" are recommended to prevent catastrophic events (e.g., aeration failure). However, these are implementation-level safeguards, not a formal safety constraint architecture. No safety state classification, no gate function.

- **Rule-based constraints before AI:** Not present as an architectural pattern. The paper notes that RL controllers need safety constraints and that physics-informed components can bound AI behaviour, but does not describe a deterministic-gate-first architecture where rules pre-filter or constrain AI participation.

- **Boundary between deterministic control and AI reasoning:** Not formally defined. The paper describes hybrid approaches (physics + ML) but the boundary is ad-hoc and system-specific, not governed by a classified safety state.

- **Failure modes and fallback:** Extensively catalogued at the application level: domain shift, sensor fouling, concept drift, class imbalance, hallucination risk in super-resolution, and "false-safe" signals in water quality forecasting. However, no systematic fallback architecture or deterministic override mechanism is described. The paper notes the need for "confidence-aware throttling" (reducing feed ratios when model confidence drops) — a concept directionally aligned with graduated governance but not formalised.

---

## 5. Formal Model and Mathematical Representation

- **Formal model:** No. The paper is a domain review and does not define any formal model of its decision systems. No state variables, safety functions, gate functions, or action spaces are mathematically specified.

- **Comparison to my pipeline E → S = f(E) → (G(S), A_AI(S)) → AI(E):** No comparable formal structure exists. The paper describes individual AI systems (detectors, forecasters, controllers) but does not formalise the governance of AI participation or advisory scope.

- **State-dependent recommendation restriction (analogous to A_AI(S)):** **No.** No system described in the review varies its recommendation types based on classified environmental safety state. The closest concept is "confidence-aware throttling" for aquaculture feeding (reduce ratios when confidence drops), which is functionally analogous to restricting AI advisory scope under uncertainty — but this is mentioned as a recommendation, not implemented or formalised.

- **Safety Dominance Property (AI(E) ⊆ A_AI(S)):** **No.** No formal property constrains AI outputs to a state-determined admissible space. The paper identifies the absence of such guarantees as a systemic gap: "AI systems that inform regulatory or operational decisions... must prioritize statistical uncertainty and model drift as key outputs."

- **Formalisation purpose:** Not applicable — no formalisation present.

---

## 6. Safety State Classification

- **Discrete risk/safety levels:** **No.** The paper does not classify environmental or operational conditions into discrete safety states. Risk is discussed in application-specific terms (e.g., IUU risk scoring, bycatch risk, welfare alerts) but not as a unified environmental state classification driving AI governance.

- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:** No equivalent. Environmental conditions (turbidity, weather, sea state) are discussed as factors affecting AI performance, not as inputs to a safety classification function that governs AI participation.

- **Differentiated AI recommendation scope across safety levels:** **No.** AI systems described in the review operate at full scope whenever active. No system restricts its output types based on environmental risk conditions. The paper does not identify this as a gap, but the absence is structurally apparent.

---

## 7. Governance Level Analysis

| Level | Question | Implemented? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (≡ G(S)) | **No** | No system described implements a formal gate controlling whether AI participates based on classified environmental state. AI systems are always-on; human review occurs downstream. The closest concept is "action-clipping" in RL controllers, but this constrains action magnitude, not AI participation. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (≡ A_AI(S)) | **No** | No system restricts the types of AI recommendations based on safety state. When AI systems are active, they produce their full output scope. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | **No** | Not approached. |

- **Binary switch or graduated governance?** Neither. The paper describes always-on AI systems with downstream human validation, not governance-gated systems. There is no binary AI switch, let alone graduated governance.

- **Support for two-level governance pair (G(S), A_AI(S))?** The paper **indirectly motivates** this construct without identifying it. Several findings point to the need:
  - RL controllers "need safety constraints for infrequent catastrophic events" — implying environmental conditions should constrain AI behaviour
  - "Confidence-aware throttling" in feeding systems — directionally analogous to restricting AI scope under degraded conditions
  - The "operational gap" between prototypes and decision-grade systems — suggesting formal governance is needed to bridge this gap
  - "Human-in-the-loop validation" for enforcement — acknowledging that AI outputs require state-dependent human oversight
  
  These observations collectively describe the problem space that my two-level governance model addresses, but the paper does not synthesise them into an architectural solution.

---

## 12. Key Concepts and Definitions

- **Domain shift:** Performance degradation when AI models trained on one habitat/season/gear encounter different conditions — a fundamental challenge affecting all fisheries AI applications.
- **Operational gap:** The disconnect between offline ML validation metrics (accuracy, F1, mAP) and decision-grade reliability required for management actions (stock assessment, harvest control rules, compliance). Central finding of the review.
- **Manager-in-the-loop:** Prospective validation paradigm where AI-guided decisions are tested against heuristic baselines in operational settings, with managers retaining decision authority. Advocated as essential for transitioning from prototypes to deployment.
- **Confidence-aware throttling:** Recommended practice of reducing AI-driven actions (e.g., feed ratios) when model confidence decreases — functionally analogous to graduated AI scope restriction.
- **Digital twin:** Simulation framework integrating growth models, water quality forecasts, and market scenarios for aquaculture decision support. Currently more aspirational than operational in most contexts.
- **AIoT (Artificial Intelligence of Things):** Integration of edge/cloud computing with IoT sensor networks for real-time farm automation. Faces adoption barriers including cost, connectivity, interoperability, and cybersecurity.
- **Foundation models:** Marine-domain large language models (OceanGPT, AQUA), vision-language models (MarineInst, AquaticCLIP), and vision-language-action models for autonomous underwater vehicles. Currently prototype-stage.
- **Management strategy evaluation (MSE):** Closed-loop simulation framework for testing harvest control rules under observation error, implementation uncertainty, and stakeholder constraints. The paper identifies MSE as the appropriate framework for validating AI-driven management decisions, but notes that most fisheries AI studies do not engage with it.
- **Estimation-aware validation:** Evaluating AI model predictions based on their impact on final survey estimates (e.g., abundance indices) rather than solely on image-level metrics — advocated for acoustic target classification.

---

## 13. Limitations and Unsolved Problems

**Stated limitations (cross-cutting):**
- **Dataset bias:** Current benchmarks over-represent commercially valuable species, temperate regions, high-visibility conditions. Rare/protected taxa, deep-water, and data-sparse fisheries are under-represented. Curated datasets with high point accuracy (95–99%) provide minimal insight into operational performance.
- **Domain shift:** Detectors trained for one habitat/gear/season degrade significantly under different conditions. Domain adaptation remains unsolved at scale.
- **Uncertainty gap:** Most studies report point accuracy without confidence intervals or propagation to management endpoints. Few studies meet ecological ML best practices (spatial/temporal blocking, per-class diagnostics, calibration plots, Bayesian/conformal uncertainty).
- **Operational gap:** AI systems remain proof-of-concept; regulatory validation and integration with formal harvest strategies (MSE) is absent. Detection/classification performance does not translate to decision-grade reliability without uncertainty-aware pipelines.
- **Low-resource deployment:** AIoT costs, intermittent connectivity, sensor maintenance, and unclear ROI block smallholder adoption. Tiered edge-cloud architectures exist but lack standardised reference designs.
- **Governance/equity:** Data ownership unclear, privacy-preserving collaboratives (federated learning) face technical and institutional barriers, power asymmetries between industrial and small-scale producers persist.
- **RL safety:** Reinforcement learning controllers for aquaculture lack adequate safety constraints for rare catastrophic events; reward design is sensitive and poorly understood.
- **Foundation model maturity:** Marine LLMs, VLMs, and VLAs are prototype-stage with no longitudinal operational validation. Risk of hallucinated recommendations in safety-relevant contexts.

**Alignment with my research problem:**
- **Two-level governance gap:** The paper does not identify the two-level governance model as a solution, but its findings repeatedly describe the problem it addresses. AI systems in fisheries operate without formal participation governance (G(S)) or advisory scope control (A_AI(S)). The "operational gap" is, in part, a governance gap — the absence of formal mechanisms to control when AI participates and what it may recommend based on environmental conditions.
- **CAUTION mode absence:** No fisheries AI system described implements an intermediate mode where AI participates with restricted output scope. The concept of "confidence-aware throttling" is the closest analogue but is not formalised or generalised.
- **Safety state conditioning absence:** Environmental conditions (weather, sea state, turbidity) are discussed extensively as factors degrading AI performance, but no system uses classified environmental state to govern AI participation or scope. This is precisely the architectural gap my research addresses.
- **Low-resource context validation:** The paper extensively documents challenges of deploying AI in low-resource, small-scale fisheries contexts — directly validating the deployment environment my architecture targets. Challenges include limited data, connectivity, computing, and user expertise — aligning with my low-resource design constraints.

---

## 16. Relation to My Research and Positioning

- **Level 1 governance (participation control):** Not implemented by any system reviewed. AI systems are always-on with downstream human review.
- **Level 2 governance (output-scope control):** Not implemented. AI systems produce full-scope outputs when active.
- **Two-level governance pair (G(S), A_AI(S)):** Not approached. No system conditions AI participation or scope on classified environmental safety state.
- **Formal safety property (Safety Dominance):** Not defined. The paper identifies the absence of formal uncertainty guarantees as a critical gap but does not propose a formal safety property.
- **Gap my research addresses:** The paper demonstrates that the entire fisheries AI domain — from species detection to aquaculture control to IUU enforcement — operates without formal governance of AI participation or advisory scope conditioned on environmental safety state. AI systems are deployed as always-on tools with post-hoc human review, lacking the pre-emptive, state-conditioned governance that safety-critical environments require.

**Positioning paragraph:** Haque & Al Jufaili (2026) provides a comprehensive, recent domain review of AI applications across fisheries genetics, aquaculture, management, and sensing infrastructure. For my research, this paper serves primarily as **domain background and deployment-environment validation**. Its systematic cataloguing of AI techniques, failure modes, and implementation challenges across fisheries directly contextualises the operational environment my architecture targets — coastal fisheries as a safety-critical, low-resource domain. Three findings are particularly valuable: (1) the "operational gap" between ML performance metrics and decision-grade reliability, which motivates the need for formal governance structures like my (G(S), A_AI(S)) pair; (2) the concept of "confidence-aware throttling" as informal, ad-hoc evidence that practitioners recognise the need for graduated AI scope restriction under degraded conditions; and (3) the extensive documentation of low-resource deployment challenges (connectivity, computing, data scarcity, smallholder exclusion) that validates my architecture's design constraints. Critically, no system reviewed implements formal AI participation governance, advisory scope control, or safety state classification — confirming that the two-level governance gap persists across the fisheries AI domain, not just in the safety-critical AI architecture literature.

---

## 17. Overall Relevance Score

**⭐⭐⭐ Medium**

**Justification:** This paper provides authoritative, recent (January 2026) domain background on AI applications in fisheries — the core application domain of my research. Its value lies in three areas: (1) validating coastal fisheries as a domain where AI systems lack formal safety governance, (2) documenting low-resource deployment challenges that justify my architecture's design constraints, and (3) providing citable evidence of the operational gap between AI prototypes and decision-grade systems. However, it does not address safety-critical AI architecture, formal governance mechanisms, decision architecture formalisation, or safety state classification — the core architectural concerns of my dissertation. It contains no formal model, no safety properties, and no governance structures to compare against. Functional role: **domain background / deployment-environment validation / gap evidence from the fisheries AI perspective**.
