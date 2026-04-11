## Literature Review Extraction — GAP-FOCUSED
### Chandran, Khalil, Hashir & Veerasingam (2025) — Smart technologies in aquaculture

---

### 1. Paper Identity

- **Title:** Smart technologies in aquaculture: An integrated IoT, AI, and blockchain framework for sustainable growth
- **Authors:** Prince Jebedass Isaac Chandran, Hana Ahmed Khalil, PK Hashir, Veerasingam S.
- **Affiliation:** Environmental Science Center & Mechanical and Industrial Engineering, Qatar University, Doha, Qatar
- **Year:** 2025 (Received 13 April 2025; Accepted 11 June 2025; Available online 12 June 2025)
- **Journal:** Aquacultural Engineering, 111, 102584
- **DOI:** https://doi.org/10.1016/j.aquaeng.2025.102584
- **Type:** Systematic review (peer-reviewed, open access CC BY 4.0)
- **Methodology:** PRISMA guidelines, 350 initial papers → 111 final selection via Rayyan tool, ROBINS-I risk-of-bias assessment
- **URL:** https://www.sciencedirect.com/science/article/pii/S0144860925000731
- **Funding:** Qatar University grant QUT2RP-ESC-24/25-343; Ministry of Environment and Climate Change (MoECC) grant QUEX-ENV-1-2023

---

### 2. Core Contribution

- **Problem:** Aquaculture faces challenges in efficiency, sustainability, and traceability. "Manual monitoring methods, which track key parameters such as water quality, feeding schedules, and fish health, are labor-intensive and susceptible to human error" (p.1). The concept of "Aquaculture 4.0" (p.2) envisions smart, automated systems integrating IoT, AI, and blockchain.
- **Proposed solution:** A systematic review (111 papers) synthesising an integrated framework combining IoT (real-time environmental monitoring), AI (predictive analytics for disease detection, feeding optimisation, water quality management), and blockchain (supply chain transparency and traceability).
- **Key architecture (Fig. 7, p.9):** Edge Subsystem (IoT sensor nodes: temp, humidity, CO₂, NH₃, light + cameras → Edge Gateway via BLE/LoRa/Ethernet → Edge Device for AI/Inference) → Digital Farming Platform (IoT platform, farm management, incident detection, alert hub, stress detection, food mix optimisation, detection of dead fishes, fish weight estimation) → Portals (user portal, command center, mobile app, admin portal, data storage).
- **Key quantitative findings (Tables 1, 3):** IoT+AI reduced fish mortality by 45% in monitored systems; water management efficiency improved by 30%; disease detection CNNs achieved 92% accuracy; hybrid AI water quality models reached 95% accuracy; feeding optimisation via RL achieved FCR of 1.1.
- **Small-scale barriers (Table 2, Table 5):** High implementation costs restrict small-scale farm accessibility; limited connectivity in remote/offshore locations; technical expertise gaps; regulatory barriers across jurisdictions.

---

### 3. Governance Mechanism Analysis

| Property | Assessment |
|---|---|
| **Governance type** | **Binary** — when environmental parameters cross thresholds, system triggers alert or automated intervention. No intermediate governance mode. Smart contracts execute "only when predefined conditions, such as product delivery or compliance with sustainability metrics, are met" (p.11) — binary trigger. |
| **Trigger** | Sensor data thresholds (e.g., dissolved oxygen below critical level, temperature outside range) |
| **Intermediate mode?** | **No** — the system operates normally or triggers alerts/interventions. No mode where AI continues operating but with restricted advisory scope. |
| **Environmental conditioning?** | **Partial** — environmental sensor data feeds *into* AI reasoning. Section 5.2: "External environmental factors such as temperature, precipitation, and wind significantly impact aquaculture operations. ML models are now widely employed to simulate and forecast these variables" (p.7). But environmental state does not govern *what AI is allowed to recommend*. The AI's advisory scope is unrestricted regardless of environmental conditions. |
| **Advisory scope restriction?** | **No** — AI always provides full-scope recommendations across all domains (feeding, disease, water quality, growth prediction, behavioral monitoring — Table 1). When conditions deteriorate, AI recommends *responses* to the deterioration — it does not restrict its own recommendation types. |
| **Key distinction** | Environmental data is used as **input to AI reasoning**, not as **a trigger for governance over AI output scope**. The architecture (Fig. 7) has no governance layer between the Edge Subsystem (sensors) and the AI processing modules. |

---

### 4. Governance Level Analysis

| Level | Question | Implemented? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI act at all? (G(S)) | **Implicit binary only** | AI operates continuously. If system fails or connectivity is lost, AI stops. No formal governance layer deciding whether AI should participate. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | **No** | AI recommends across all domains (feeding, disease, water quality) regardless of environmental conditions. No scope restriction. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | **No** | No safety state classification. No governance pair. |

---

### 5. Gap Evidence for Novelty Argument

**Key finding:** This paper presents a full IoT+AI architecture for aquaculture with environmental sensors providing real-time data to AI — the exact technical infrastructure that could support environment-state-conditioned governance. Yet no such governance exists. Environmental data flows *into* the AI's reasoning but never *governs* what the AI is permitted to recommend.

**The IoT gap this reveals:** IoT systems have all the components needed for S = f(E) → (G(S), A_AI(S)):
- ✅ Environmental sensors (equivalent to E vector)
- ✅ Real-time data processing (could compute S = f(E))
- ✅ AI making recommendations (equivalent to AI advisory layer)
- ❌ No classification of environmental state into governance modes
- ❌ No governance layer restricting AI advisory scope based on environmental state
- ❌ No concept of "conditions are marginal, so AI may only recommend conservative actions"

**Use in justification:** Cite as evidence that IoT+AI systems in aquaculture — the domain most closely related to fisheries and most naturally suited to environment-state-conditioned governance — do not implement any form of environmental governance over AI. The gap between "AI uses environmental data" and "environmental data governs AI" is the precise contribution of the proposed architecture.

---

### 6. Theme Relevance

| Theme | Match? | Notes |
|---|---|---|
| T1: Hybrid AI | ✅ Yes | IoT + AI + blockchain integrated framework; edge computing + cloud AI |
| T2: Safety-critical AI | ⚠️ Partial | "AI-driven safety measures" (p.2) means AI detects safety issues — not safety governing AI |
| T3: AI governance | ❌ No | No AI governance mechanism discussed; blockchain governs supply chain transactions, not AI behaviour |
| T4: Low-resource environments | ✅ Yes | Explicitly discusses small-scale farm barriers: "High implementation costs restrict small-scale farm accessibility" (Table 2); NB-IoT for off-grid monitoring; LoRaWAN for remote connectivity |
| T5: Decision architecture formalisation | ❌ No | Framework description and systematic review, no formal model |
| T6: Human role | ⚠️ Partial | Remote monitoring portal (Fig. 7), but no human-AI interaction analysis |
| T7: Socio-technical evaluation | ⚠️ Partial | Discusses adoption barriers, resistance to change, regulatory challenges (Tables 2, 5) |
| T8: Coastal fisheries / maritime | ✅ Yes | Aquaculture — directly adjacent to fisheries domain; discusses offshore aquaculture, coastal management |

---

### 7. Overall Relevance Score

**⭐⭐⭐⭐ High** (Verified from full text — PDF uploaded and read, 14 pages + references)

Essential for the IoT governance gap argument. Demonstrates that even in aquaculture — the domain most closely related to the target fisheries context — IoT+AI systems use environmental data as input to AI reasoning but never as a governance trigger over AI advisory scope. The architecture (Fig. 7) has all the ingredients for S = f(E) → (G(S), A_AI(S)) — sensors, edge AI, platform processing — but no assembly into a governance architecture. The small-scale deployment barriers (Table 2) also support the low-resource environment relevance (T4).
