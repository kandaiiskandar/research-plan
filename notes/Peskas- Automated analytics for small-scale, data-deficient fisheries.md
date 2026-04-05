# Literature Review Extraction: Longobardi et al. (2025)

## 1. Paper Identity

- **Title:** Peskas: Automated analytics for small-scale, data-deficient fisheries
- **Authors:** Lorenzo Longobardi, Villiam Sozinho, Hamza Altarturi, E. Fernando Cagua, Alexander Tilley
- **Year:** 2025 (published online December 2024)
- **Venue:** SoftwareX, Vol. 29, Article 102028
- **DOI:** https://doi.org/10.1016/j.softx.2024.102028
- **Type:** Original Software Publication (system design + deployment case study)

---

## 2. Core Contribution

- **Problem addressed:** Small-scale fisheries (SSFs) account for over 40% of global fish catch and nearly 90% of fisheries employment, yet suffer from severe data deficiency — particularly in least developed countries — due to logistical, financial, and capacity constraints. No systems existed to collect, validate, analyse, and visualise SSF catch and effort data in near-real-time for these contexts.
- **Proposed solution:** Peskas — an open-source, modular, low-cost digital platform providing a template workflow for SSF data ingestion, preprocessing, validation, analytics, export, and dashboard visualisation. Piloted and operationally deployed in Timor-Leste; now scaling to East and Southern Africa.
- **Main contributions:** (1) A six-module automated data pipeline (collection → preprocessing → validation → analytics → export → visualisation) running in Docker containers with GitHub Actions automation; (2) integration of digital catch surveys (KoBoToolbox), GPS vessel tracking, and external databases (FishBase) into a unified workflow; (3) a multilingual interactive Shiny dashboard co-designed with fisheries managers; (4) real-world deployment as Timor-Leste's national fisheries monitoring system since 2019; (5) open data publication to Harvard Dataverse.
- **Novelty:** First open-source, end-to-end automated analytics platform purpose-built for data-deficient SSFs in low-resource, least-developed-country contexts. The novelty is in the deployment model and contextualisation — the individual technical components (R, Shiny, Docker, KoBoToolbox) are established tools assembled into a fit-for-purpose pipeline.

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | No | Peskas uses statistical methods (GLMMs for landing estimates, MAD for outlier detection, Cook's Distance for multivariate validation) but no AI/ML models and no hybrid architecture. |
| Safety-critical AI decision-making | No | Not addressed. Peskas is a data monitoring and visualisation platform, not a safety-critical decision support system. No safety-state classification, no risk-gated decisions, no operational safety governance. |
| AI governance / control mechanisms | No | No AI governance mechanisms. No runtime control of AI participation or output. The system does not employ AI in decision generation. |
| Low-resource environments | Yes | Core focus. Explicitly designed for data-deficient, low-resource SSFs in least developed countries. Addresses limited data, limited connectivity (KoBoToolbox for offline-capable data collection), limited institutional capacity, and limited financial resources (open-source, low-cost cloud infrastructure). Timor-Leste deployment demonstrates operation in one of the world's poorest countries with extremely limited governance capacity. |
| Decision architecture formalisation | No | No formal model. The six-module pipeline (collection → preprocessing → validation → analytics → export → visualisation) is a *data workflow architecture*, not a *decision architecture*. No state variables, gate functions, or action spaces are defined. |
| Human role in decision-making | Partial | Positioned as a decision *dashboard* — humans (fisheries managers, policymakers) are the decision-makers; Peskas provides data and insights to inform their decisions. Co-designed with government fisheries officers. However, no formal model of human-AI interaction or decision support structure. |
| Socio-technical evaluation | Partial | Discusses co-design with stakeholders, multilingual interface for local community engagement, impacts on collaboration between fishers/enumerators/NGOs/government, sex-disaggregated data for gender inclusion, and a formal impact evaluation study (Tilley et al. 2024) finding improved collaboration and communication despite limited regulatory change. However, this is evaluation of a data platform, not of an AI decision support system. |
| Coastal fisheries / maritime domain | Yes | Core domain. Deployed in Timor-Leste coastal small-scale fisheries; scaling to Kenya, Zanzibar, Mozambique, and Malawi. Covers catch composition, fishing effort, vessel tracking, species-specific trends, nutritional characterisation, and market dynamics. |

**Mid-Extraction Relevance Gate:** 2 Yes + 2 Partial → **REDUCED EXTRACTION** (Sections 4–7 and 12–13 only; Sections 8–11 and 14–15 skipped).

---

## 4. Decision Architecture Analysis

- **Architecture:** Peskas has a *data pipeline architecture* — a six-module sequential workflow (collection → preprocessing → validation → analytics → export → visualisation) — not a *decision architecture*. It processes fisheries data into dashboard outputs but does not structure, govern, or constrain any decision-making process.
- **Layered architecture / governance structure:** The pipeline modules are layered in a data-flow sense (raw data → cleaned data → validated data → analytics → outputs), but there is no governance layer controlling system behaviour based on environmental or safety state.
- **Rule-based constraints before AI:** The validation module applies rule-based outlier detection (21 distinct alert flags, MAD-based univariate detection, Cook's Distance multivariate checks) *before* analytics — but this governs data quality, not AI participation or recommendation scope.
- **Boundary between deterministic control and AI reasoning:** Not applicable — there is no AI reasoning component. Analytics consist of statistical estimation (GLMMs, extrapolation from GPS samples to fleet-level), not AI-generated recommendations.
- **Failure modes / fallback behaviour:** The validation module flags anomalous data (21 alert codes) and excludes outliers from analysis. GPS data validation handles undetected trips, merged trips, signal loss, and anomalous speeds. However, these are data quality controls, not system-level fallback or degradation mechanisms.

**Summary:** Peskas is a data pipeline and dashboard, not a decision architecture. It provides information to human decision-makers but does not structure, gate, or govern any AI-mediated decision process.

---

## 5. Formal Model and Mathematical Representation

- **Formal model:** None for the system architecture. The analytics module uses established statistical methods (GLMMs for estimating landings per fisher, length-weight relationships from FishBase, MAD-based outlier detection) but these are standard fisheries estimation techniques, not formal models of a decision system.
- **Comparison to E → S = f(E) → (G(S), A_AI(S)) → AI(E):** Not applicable. Peskas has no environmental state classification, no safety function, no gate function, and no AI recommendation space.
- **State-dependent recommendation restriction:** Not present. Peskas outputs (dashboard visualisations, catch estimates, fishing effort indicators) are not conditioned on any classified state.
- **Safety Dominance Property:** Not defined or referenced.

---

## 6. Safety State Classification

- **Discrete risk/safety levels:** None. Peskas does not classify operational or environmental conditions into safety states.
- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:** Not applicable.
- **AI recommendation scope differentiation:** Not present — there are no AI recommendations and no state-dependent output restriction.
- **Note:** The paper briefly mentions "safety at sea concerns" as a topic that Peskas monitoring data has helped address, but this refers to using catch/effort data patterns to identify fishing activity in dangerous conditions — not to any safety-state classification mechanism within the system.

---

## 7. Governance Level Analysis

| Level | Question | Implemented? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (G(S)) | No | No AI component exists to govern. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | No | No AI recommendations generated. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | No | Not applicable. |

- **Governance type:** Peskas implements *data governance* (validation, quality assurance, outlier exclusion, open data publication) and *access governance* (multilingual interface, role-appropriate dashboards, privacy anonymisation). Neither corresponds to runtime AI governance.
- **Support or contradiction of two-level governance pair:** Neither supports nor contradicts. Peskas operates at a different level — it is the data infrastructure *upstream* of where an AI decision system would sit. An AI decision support system (like my architecture) could potentially consume Peskas data as input.

---

## 12. Key Concepts and Definitions

| Term / Concept | Definition / Relevance |
|---|---|
| **Peskas** | Open-source automated analytics platform for SSF data; six-module pipeline from collection to dashboard. Represents the state of the art in low-resource fisheries data infrastructure. |
| **Data-deficient fisheries** | Fisheries where insufficient data exist for conventional stock assessment and management — the norm for SSFs in least developed countries. Directly relevant as the deployment environment my architecture targets. |
| **Near-real-time monitoring** | Peskas provides daily-updated dashboards and automated pipeline execution, enabling near-real-time fisheries monitoring even in low-resource contexts. Relevant as evidence that near-real-time data flows are achievable in these environments. |
| **Co-design** | Peskas was iteratively co-designed with fisheries officers and updated based on stakeholder feedback since 2017 — relevant methodological precedent for my socio-technical evaluation approach. |
| **KoBoToolbox** | Open-source digital survey tool designed for challenging environments with limited connectivity. Relevant as a data collection mechanism that could feed environmental state data into my architecture's E vector. |
| **GPS vessel tracking** | Solar-powered GPS trackers (6-second intervals) on ~15% of fishing fleet, enabling modelling of fishing effort and extrapolation to fleet-wide estimates. Relevant as a low-resource deployment pattern for vessel monitoring. |
| **Validation alert flags** | 21 distinct coded alerts for data quality issues (outlier values, impossible trip durations, impossible catch sizes, GPS anomalies). Represents a rule-based quality control layer — analogous to deterministic constraints, though applied to data quality rather than AI governance. |

---

## 13. Limitations and Unsolved Problems

- **Stated limitations:**
  - Peskas is not an off-the-shelf turnkey solution — contextualisation to each new country/fishery requires collaboration with local stakeholders and experts.
  - Vessel tracking (the costliest module) involves hardware purchase, replacement plans, and ongoing data fees.
  - Software development and management cannot easily be assumed by host countries; long-term sustainability depends on external technical support.
  - Data privacy approaches need standardisation as the platform scales to more locations.
  - Digital divide — ensuring inclusive access to technology for small-scale fisheries communities remains a crucial challenge.
  - Government adoption is slowed by weak legal infrastructure and limited institutional capacity (despite Timor-Leste's formal adoption in 2019).

- **Unsolved problems acknowledged:**
  - No AI or ML is used for decision support — all analytics are descriptive/estimative. The paper does not discuss any automated decision recommendation capability.
  - The system produces dashboards and reports for human interpretation but provides no structured decision support, no risk classification, and no graduated response framework.
  - Safety at sea is mentioned as a concern that monitoring data can help address, but no safety-oriented system functionality exists.

- **Gaps aligning with my research:**
  - Peskas provides the *data infrastructure* layer but lacks any *decision support* layer. My architecture sits above this kind of data pipeline — consuming environmental and fisheries data to produce safety-classified, governance-gated AI recommendations.
  - Peskas demonstrates that near-real-time data collection and automated analytics are achievable in the exact low-resource environments my architecture targets (Timor-Leste, East Africa), validating the deployment feasibility assumption.
  - The system has no safety-state classification despite operating in environments where fisher safety is a documented concern — exactly the gap my S = f(E) function addresses.
  - No AI participation governance exists because no AI participates — but as AI capabilities are inevitably added to such platforms (the review by Kühn et al. 2025 shows the trajectory), the governance gap my architecture fills becomes directly relevant.

---

## 16. Relation to My Research and Positioning

- **Governance level implemented:** Neither Level 1 nor Level 2. No AI component; no runtime governance.
- **State-conditioned governance:** Not applicable.
- **Proximity to (G(S), A_AI(S)):** Distant — but complementary. Peskas is a data infrastructure that could serve as the upstream data source for my architecture's environmental state vector E.
- **Safety Dominance Property:** Not defined.
- **Gap my research addresses:** Peskas demonstrates that automated, near-real-time fisheries data pipelines are feasible in low-resource environments, but stops at data visualisation for human interpretation. My architecture adds the missing decision support layer — taking environmental data (of the kind Peskas collects), classifying it into safety states, and governing AI-generated recommendations through the two-level (G(S), A_AI(S)) pair.

**Positioning paragraph:** Longobardi et al. (2025) provides **deployment environment validation** for my research. Peskas is the most advanced operational example of automated fisheries analytics in a low-resource, data-deficient context — precisely the deployment environment my architecture targets. Its successful deployment in Timor-Leste (one of the world's poorest countries, with extremely limited institutional capacity) demonstrates that automated, near-real-time data pipelines are technically and organisationally feasible in these environments. The data variables Peskas collects — landing date, site, gear, trip duration, habitat, vessel GPS tracks — overlap substantially with the environmental state vector components my architecture requires. However, Peskas is purely a data monitoring and visualisation platform; it provides no decision support, no safety-state classification, no AI-generated recommendations, and no governance mechanism. It occupies the *data infrastructure layer* below where my architecture operates. The paper is citable as evidence of deployment feasibility in the target environment, and as a concrete example of the upstream data systems my architecture could integrate with.

---

## 17. Overall Relevance Score

### ⭐⭐ Low

**Justification:** Peskas is a fisheries data pipeline and dashboard with no AI, no decision architecture, no safety-state classification, and no governance mechanism. It operates at a fundamentally different system layer (data infrastructure) than my architecture (AI decision support governance). Its relevance is limited to two points: (1) deployment environment validation — proving that automated, near-real-time analytics are feasible in the exact low-resource contexts my architecture targets; and (2) upstream data compatibility — the data Peskas collects overlaps with my architecture's environmental state vector inputs. Useful for a brief citation in the domain motivation or deployment feasibility sections; not citable in the architecture, formalisation, or governance chapters.
