## Literature Review Extraction — GAP-FOCUSED
### Tandel et al. (2025) — Smart Aquaculture: IoT and AI Application for Sustainable Fisheries

---

### 1. Paper Identity

- **Title:** Smart Aquaculture: IOT AND AI Application for Sustainable Fisheries
- **Authors:** Binal Tandel¹*, H. V. Parmar², Smit Tandel³, Yash Solanki¹, Trushti Tandel¹
- **Affiliations:** ¹PG Scholar, Department of Aquaculture; ²Assistant Professor, Department of Aquaculture; ³PG Scholar, Department of Fisheries Resource Management — College of Fisheries Science, Kamdhenu University, Veraval 362265, India
- **Year:** 2025 (Published 25 February 2025)
- **Journal:** The Science World — A Monthly e Magazine, ISSN 2583-2212, Vol.5(2), pp. 6319–6327
- **DOI:** https://doi.org/10.5281/ScienceWorld.14946381
- **Type:** Popular article (e-magazine, not peer-reviewed research article)
- **URL:** www.thescienceworld.net
- **Citation quality note:** This is a popular/practitioner-oriented article in an e-magazine, not a peer-reviewed journal article. Its value to the corpus is as a domain-specific source that directly addresses IoT+AI in aquaculture/fisheries — the closest domain overlap with the proposed architecture. Treat claims with appropriate weight; corroborate key claims with Chandran et al. (2025) which covers similar ground with higher methodological rigour.

---

### 2. Core Contribution

- **Problem:** Global aquaculture production exceeds 120 MMT annually (p.2) with annual growth rate exceeding 10%, now accounting for over one-third of global fish consumption (p.1). The industry faces challenges: environmental impact, disease outbreaks, resource optimisation, high costs, connectivity issues, and maintenance constraints (Abstract, Section 5).
- **Proposed solution:** Review of IoT innovations in aquaculture covering water quality monitoring, automated feeding, disease detection, and cloud-based smart management platforms.
- **Structure:** 7 sections — Introduction (aquaculture food security, sustainability, IoT role), Understanding IoT in Aquaculture (definition, sensors/automation/analytics, examples), Key IoT Innovations (water quality, feeding, disease, management), Benefits, Challenges & Limitations, Conclusion, References.
- **Key IoT applications described:**
  - **Water quality monitoring (Section 3.1):** Wireless sensor networks measuring pH, temperature, dissolved oxygen, TDS. "López-Munoz et al. used wireless sensor networks to measure pH, temperature and TDS, providing real-time data through IoT platforms" (p.4). Koronides et al. analysed seawater parameters over 3 months in Ayia Napa, Cyprus (p.5).
  - **Automated feeding systems (Section 3.2):** PLC + IoT + ML for optimising feeding schedules. Ecoaquatics system integrates feeding with water quality monitoring (Nandyala & Bathula, 2024). "User-friendly interfaces help farmers adjust schedules for better fish health" (p.5). Mobile food feeders enhance precision (Abidin et al., 2024).
  - **Disease detection & health monitoring (Section 3.3):** ML + predictive analytics + real-time data collection. "Machine learning models analyze large datasets to detect disease patterns, enabling timely interventions" (Khan et al., 2024) (p.5).
  - **Smart aquaculture management (Section 3.3b):** Cloud-based platforms for remote monitoring and data-driven decision-making. "Automated alert systems notify operators of any deviations, allowing for immediate corrective actions" (Bahadur et al., 2024) (p.5). "Sensors continuously track vital parameters such as pH, temperature and turbidity, maintaining optimal conditions for aquatic life" (p.5). Suitable for "both small-scale and commercial aquaculture operations" (Rahul et al., 2024) (p.5).
- **Example systems (Section 2.3):**
  - **IoT-Based Fish Tank Management:** Arduino Uno monitoring pH, turbidity, water levels. "It sends automated SMS alerts in case of abnormal conditions, improving fish welfare" (Abidin et al., 2024) (p.4) — **binary: abnormal → SMS alert**
  - **Smart Aquaponics Systems:** Three-tier architecture for scalability, sensors for pH, humidity, temperature (p.4)
  - **AI-Enhanced Aquaponics:** Disease detection and biomass estimation via image processing. Mobile app for real-time monitoring (Abd El-Atty et al., 2024) (p.4)
  - **Integrated Farming Systems:** Automatic sensor cleaning, zero-waste approach (Abidin et al., 2024) (p.4)
- **Automation pattern (Section 2.2.2, p.3):** "smart control systems regulate environmental parameters by automatically adjusting temperature, oxygen levels and other critical factors to maintain ideal conditions" (Chelladurai et al., 2024) — **binary: out-of-range → auto-adjust to maintain ideal**
- **Benefits (Section 4):** Operational efficiency, resource management, fish health improvement, cost reduction, environmental sustainability. "The continuous real-time monitoring of critical water parameters, such as temperature and ammonia levels, facilitates timely interventions that improve fish growth and survival rates" (Darmaji & Wisaksono, 2024) (p.6). "Automated monitoring of water quality plays a crucial role in disease prevention by maintaining optimal environmental conditions" (Nayoun et al., 2024) (p.5–6).
- **Challenges and limitations (Section 5, pp.6–7):**
  - **High initial costs:** "Implementing IoT infrastructure requires substantial financial investment in sensors, monitoring devices and network solutions, making it less accessible to small-scale aquaculture farmers who may lack the necessary capital" (Rahul et al., 2024) (p.6)
  - **Connectivity:** "many aquaculture farms are located in remote areas where internet connectivity is limited or unreliable, which affects the real-time transmission of critical data" (p.6)
  - **Cybersecurity:** "IoT systems are susceptible to cyber threats, necessitating the implementation of robust security protocols to protect sensitive operational data from unauthorized access and potential breaches" (Adam et al., 2024) (p.6)
  - **Technical expertise gap:** "Many farmers lack the necessary knowledge and skills to configure, monitor and troubleshoot IoT-based technologies, leading to a dependency on specialized training programs and technical support" (Selvaganesh et al., 2024) (p.7)
  - **Hardware durability:** "the exposure of IoT hardware to water, humidity and other harsh environmental conditions can lead to system malfunctions, reduced device longevity and increased maintenance requirements" (p.7)
  - **Required solutions:** "a combination of financial support, improved connectivity infrastructure, cybersecurity measures, capacity-building programs and the development of durable, water-resistant IoT devices" (p.7)

---

### 3. Governance Mechanism Analysis

| Property | Assessment |
|---|---|
| **Governance type** | **Binary** — all IoT/AI systems described operate on a detect/alert or detect/auto-adjust basis. Environmental parameters are monitored continuously; when values deviate from acceptable ranges, the system either alerts the operator (SMS, notification) or automatically adjusts conditions back to ideal. No intermediate governance mode. |
| **Trigger** | Sensor threshold breaches — parameter values (pH, temperature, dissolved oxygen, turbidity, water levels) exceeding predefined acceptable ranges |
| **Intermediate mode?** | **No** — systems either maintain conditions within ideal ranges (normal operation) or trigger alerts/corrections when deviations occur. No graduated response modes based on environmental classification. |
| **Environmental conditioning?** | **Partially, but inverted** — environmental sensors ARE the core technology, but environmental data is used as INPUT to AI reasoning (predicting feeding times, detecting disease, optimising conditions), never as a TRIGGER for governing what AI may recommend or do. The environment conditions AI operation but does not govern AI scope. |
| **Advisory scope restriction?** | **No** — AI operates at full scope at all times. AI-driven predictive analytics, automated feeding, disease detection all operate without scope restriction based on environmental conditions. The only "restriction" is binary: the system either works or alerts on failure. |
| **Key distinction** | Environmental sensors → AI reasoning → binary output (alert/adjust). The architecture is: **environment as input, not environment as governance trigger**. This is the fundamental pattern across all aquaculture IoT systems described in the paper. |

---

### 4. Governance Level Analysis

| Level | Question | Implemented? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI act at all? (G(S)) | **Implicit binary only** | AI systems are either operational (monitoring, predicting, adjusting) or offline/malfunctioning. No dynamic governance of whether AI participates based on environmental state. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | **No** | AI systems generate all types of recommendations regardless of environmental conditions — feeding schedules, water quality adjustments, disease alerts, growth predictions. No restriction on advisory scope. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | **No** | No concept of classifying environmental state into governance modes. Environmental data feeds AI models directly; it does not determine what AI is permitted to output. |

---

### 5. Gap Evidence for Novelty Argument

**Key finding:** This paper reviews IoT+AI in the **direct application domain** of the proposed architecture (aquaculture/fisheries). It confirms that in the aquaculture IoT domain, the pattern is universally: **environmental sensors → AI input → binary output**. Environmental data (pH, temperature, dissolved oxygen, turbidity, water level) is collected by sensors and fed into AI models for analysis, prediction, and optimisation. The AI then produces outputs that are either informational (alerts, notifications) or actuational (auto-adjust parameters). At no point does the environmental state GOVERN what the AI is permitted to recommend.

**The environment-as-input-not-governance pattern — three concrete examples:**

1. **SMS alert system (Section 2.3, p.4):** Arduino Uno monitors pH, turbidity, water levels → "sends automated SMS alerts in case of abnormal conditions." Environmental data is INPUT; the governance decision is binary (abnormal → alert, normal → no alert). The system does not classify environmental conditions into graduated states that determine what the AI advisory system may recommend.

2. **Smart control systems (Section 2.2.2, p.3):** "smart control systems regulate environmental parameters by automatically adjusting temperature, oxygen levels and other critical factors to maintain ideal conditions." Environmental data triggers binary auto-adjustment (out-of-range → adjust, in-range → no action). No intermediate governance mode between "fully operational" and "corrective action."

3. **Cloud-based management (Section 3.3b, p.5):** "Automated alert systems notify operators of any deviations, allowing for immediate corrective actions." The pattern is deviation-detection → alert → corrective action. No graduated governance where the environmental state determines the SCOPE of what the system may recommend.

**The small-scale fisheries gap:** The paper explicitly identifies that IoT adoption is "less accessible to small-scale aquaculture farmers who may lack the necessary capital" (p.6) and that "many aquaculture farms are located in remote areas where internet connectivity is limited or unreliable" (p.6). This directly supports the proposed architecture's low-resource environment framing — existing IoT+AI systems are designed for well-resourced settings, and even when deployed in aquaculture/fisheries, they implement binary governance only.

**The missing link:** The paper describes a complete sensor-to-AI-to-action pipeline for aquaculture, but the governance architecture is fundamentally flat. There is no classification of environmental states (e.g., S ∈ {SAFE, CAUTION, UNSAFE}) that would govern AI advisory scope. The proposed architecture's innovation — using classified environmental state to govern WHAT AI may recommend, not just WHETHER to alert — is absent from the aquaculture IoT literature.

**Use in justification:** Cite alongside Chandran et al. (2025) to show that IoT+AI systems in both aquaculture engineering (Chandran) and fisheries practice (Tandel) lack any form of environment-state-conditioned governance over AI advisory scope. Together, these two papers establish that the fisheries/aquaculture IoT community has not implemented the proposed architecture's governance mechanism despite having the technical infrastructure (environmental sensors, AI models, cloud platforms) to do so.

---

### 6. Theme Relevance

| Theme | Match? | Notes |
|---|---|---|
| T1: Hybrid AI | ✅ Yes | IoT + ML/DL + automated control + cloud platforms integrated for aquaculture management |
| T2: Safety-critical AI | ⚠️ Partial | Disease outbreaks and environmental degradation have safety implications; automated feeding affects fish health/survival; but paper does not frame this as safety-critical AI per se |
| T3: AI governance | ✅ Yes | Demonstrates complete absence of AI governance in aquaculture IoT — AI operates at full scope at all times, governed only by binary threshold alerts. Confirms the gap. |
| T4: Low-resource environments | ✅ Yes | Explicitly discusses: "less accessible to small-scale aquaculture farmers who may lack the necessary capital" (p.6); "remote areas where internet connectivity is limited or unreliable" (p.6); technical expertise gap among farmers (p.7); hardware durability in harsh conditions (p.7) |
| T5: Decision architecture formalisation | ❌ No | No formal model; descriptive review only |
| T6: Human role | ⚠️ Partial | Farmers receive alerts and make corrective decisions; "user-friendly interfaces help farmers adjust schedules" (p.5); but no formal human-AI interaction model |
| T7: Socio-technical evaluation | ❌ No | No empirical evaluation; descriptive review |
| T8: Coastal fisheries / maritime | ✅ Yes | Directly addresses aquaculture and sustainable fisheries. Authors from College of Fisheries Science, Kamdhenu University, Veraval, India — a major fishing port on Gujarat's coast. Discusses reducing dependence on wild fish stocks (p.6). |

---

### 7. Overall Relevance Score

**⭐⭐⭐ Moderate–High** (Verified from full text — PDF uploaded and read, 9 pages including references)

Value is primarily as **domain-specific gap evidence**: confirms that the environment-as-input-not-governance pattern holds in the closest application domain (aquaculture/fisheries IoT+AI). The paper is a popular article rather than a peer-reviewed research paper, so individual claims should be corroborated with Chandran et al. (2025). However, it provides three concrete examples of binary governance in aquaculture IoT systems, explicitly discusses small-scale fisheries accessibility barriers (T4), and comes from a fisheries science department at a coastal Indian university — establishing direct domain relevance. The complete absence of any environmental-state-conditioned governance in this domain-specific review strengthens the novelty argument that the proposed architecture addresses a genuine gap.
