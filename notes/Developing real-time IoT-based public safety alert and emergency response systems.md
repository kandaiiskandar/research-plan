## Literature Review Extraction — GAP-FOCUSED
### Zhang et al. (2025) — Developing real-time IoT-based public safety alert and emergency response systems

---

### 1. Paper Identity

- **Title:** Developing real-time IoT-based public safety alert and emergency response systems
- **Authors:** Han Zhang¹, Runze Zhang², Jiamanzhen Sun³
- **Affiliations:** ¹China People's Police University, Immigration Management College, Guangzhou 510663; ²Immigration Service Center, National Immigration Administration, Beijing 100000; ³School of Management, Lanzhou University, Lanzhou 730000
- **Year:** 2025
- **Journal:** Scientific Reports, 15, 29056
- **DOI:** https://doi.org/10.1038/s41598-025-13465-7
- **Type:** Journal article (peer-reviewed, open access, Nature portfolio)
- **URL:** https://www.nature.com/articles/s41598-025-13465-7
- **Citation Quality:** ✅ Nature portfolio journal (Scientific Reports). Peer-reviewed. Compared against 7 state-of-the-art systems.

---

### 2. Core Contribution

- **Problem:** "Many current public safety systems remain encumbered by outdated protocols, manual processes, and fragmented communication channels" (p.1). Systems are reactive, lack real-time data integration, and cannot handle multi-hazard scenarios.
- **Proposed solution:** A 5-layer IoT-based architecture (Fig. 2, p.7): Sensor Layer → Communication Layer (LoRa, 5G, Wi-Fi) → Cloud Layer → Edge Computing Layer → Emergency Services & User Interface. Sensor network formalised as S = {s₁, s₂, ..., sₙ} with each sensor generating multivariate time-series D_i(t) = {x_{i1}(t), x_{i2}(t), ..., x_{im}(t)} (Eq. 1, p.6).
- **Key formalisms:**
  - Communication latency modelled via Shannon-Hartley: τ_comm = P / (B · log₂(1 + SNR/N)) (Eq. 2)
  - Edge processing latency: τ_edge(e_k) = Σ[f(x_i(t)) + δ_i] (Eq. 3)
  - **Binary classifier (Eq. 4, p.8):** φ(X(t)) = {1, if P_alert(X(t)) ≥ θ; 0, Otherwise} — where P_alert is predicted probability of critical event, θ ∈ [0,1] is tunable threshold
  - Total latency: τ_total = τ_sense + τ_comm + τ_edge + τ_decision (Eq. 5), constrained to ≤ 500ms
- **Data flow (Fig. 3, p.9):** Sensor Data Collection → Event Detection → Edge Processing (Filtering, Aggregation, Inference) → Threshold Evaluation (φ(X(t)) ≥ θ?) → **Yes:** Alert Distribution → Stakeholder Notification → Cloud Storage / **No:** Cloud Synchronization (Normal Data Logging)
- **Performance (Table 1):** Fire detection 410ms, accident detection 450ms, gas leak 430ms. Outperforms 7 systems (Legacy IoT, DeepSenseNet, EdgeGuard, SafeCity, QuickResponse IoT, RealAlert, EM-Sense). Reliability 99.1% alert success, uptime 99.8%.
- **Scenarios tested:** Fire, traffic accident, gas leak, medical distress — in smart city simulation testbed.

---

### 3. Governance Mechanism Analysis

| Property | Assessment |
|---|---|
| **Governance type** | **Binary — formally proven.** Eq. 4 defines the decision function as φ(X(t)) = {1, if P_alert(X(t)) ≥ θ; 0, Otherwise}. Two states only: normal operation (φ=0) and emergency alert (φ=1). |
| **Trigger** | Aggregated sensor data X(t) from heterogeneous sensors (temperature, humidity, gas, CO₂, NO₂, AQI, motion, biometric). P_alert(X(t)) is the predicted probability of a critical event. |
| **Intermediate mode?** | **No** — despite monitoring multiple environmental parameters simultaneously, the decision is always binary. "Only if the risk level exceeds this threshold does the system escalate the event to emergency responders" (p.8). No intermediate escalation level. |
| **Environmental conditioning?** | **Yes, but binary** — environmental sensor data (T, H, gas concentrations, AQI) directly triggers the safety response via P_alert. However, the response has only two outcomes: normal logging (φ=0) or full emergency alert (φ=1). No graduated governance modes despite rich environmental input. |
| **Advisory scope restriction?** | **No** — citizen notifications are the same type regardless of severity: "Evacuate North Exit" or "Shelter-in-Place" (p.8). No concept of restricting advisory scope based on graduated environmental severity. |
| **Key distinction** | The paper has the most explicit formalisation of the binary pattern: environmental sensors → feature vector X(t) → probability P_alert → **binary threshold** φ. This is exactly the pattern the proposed architecture replaces with S = f(E) → {SAFE, CAUTION, UNSAFE}. |

---

### 4. Governance Level Analysis

| Level | Question | Implemented? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI act at all? (G(S)) | **Binary** | AI edge processing always runs (continuous monitoring). When φ(X(t))=1, system transitions to alert mode. This is binary participation: monitoring or alerting. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | **No** | Alert content types are not restricted by environmental severity. System issues same notification types (mobile push, SMS, sirens, electronic signboards) regardless of whether it's a minor gas elevation or a major fire. No graduated advisory scope. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | **No** | Environmental state triggers binary alert via φ(X(t)), not graduated governance. The rich environmental feature vector X(t) could classify into multiple states, but the architecture reduces it to a single binary threshold. |

---

### 5. Gap Evidence for Novelty Argument

**Key finding:** This paper provides the **most mathematically explicit proof** of the binary governance gap in IoT safety systems. Equation 4 formalises the decision as a binary classifier: φ(X(t)) = {1, 0}. The data flow (Fig. 3) visually confirms the binary branch: threshold evaluation → Yes (alert) / No (normal logging). Despite rich environmental input from heterogeneous sensors (temperature, humidity, gas, CO₂, NO₂, AQI, motion, biometric), the system reduces all information to a single binary decision.

**The structural parallel to the proposed architecture:** Both systems have:
- Environmental sensors generating a feature vector (Zhang: X(t); proposed: E = {w, r, m, o, v, t})
- A classification function (Zhang: φ(X(t)) → {0, 1}; proposed: f(E) → {SAFE, CAUTION, UNSAFE})
- Different system behaviours based on classification result

The critical difference: Zhang's φ maps to **two** states with **identical response type** (alert or no alert). The proposed f maps to **three** states with **qualitatively different governance regimes** (full AI advisory, restricted advisory, no AI participation). Zhang's approach is the binary ceiling that the proposed architecture breaks through.

**The missed opportunity this reveals:** With sensors measuring temperature, humidity, gas concentrations, CO₂, NO₂, and AQI simultaneously, this system could classify into graduated states (e.g., elevated risk / imminent danger / active emergency) and provide different advisory types at each level. Instead, it implements a single tunable threshold θ that produces a binary output. Adjusting θ changes *sensitivity*, not *governance type*.

**Use in justification:** Cite as the most formally explicit evidence of binary governance in IoT safety systems. Equation 4 can be directly contrasted with the proposed S = f(E): same structure (environmental features → classification), different cardinality ({0,1} vs. {SAFE, CAUTION, UNSAFE}), different governance consequence (binary alert vs. graduated governance pair).

---

### 6. Theme Relevance

| Theme | Match? | Notes |
|---|---|---|
| T1: Hybrid AI | ⚠️ Partial | Edge AI + cloud AI + sensor fusion; deterministic threshold + ML models |
| T2: Safety-critical AI | ✅ Yes | Public safety and emergency response; sub-500ms latency requirement |
| T3: AI governance | ❌ No | No AI governance discussed; AI is the governed output, not the governance mechanism |
| T4: Low-resource environments | ✅ Yes | Edge computing on Raspberry Pi/ESP32; LoRa fallback for "rural or low-connectivity environments" (abstract); designed for "both developed and resource-constrained urban areas" (p.6) |
| T5: Decision architecture formalisation | ✅ Yes | Formal equations for latency (Eq. 2-3, 5-6), binary classifier (Eq. 4), sensor network model (Eq. 1). Most formalised IoT safety system in the corpus. |
| T6: Human role | ⚠️ Partial | Emergency responders and citizens as alert recipients; "citizen feedback loops" mentioned in gaps section (p.6) |
| T7: Socio-technical evaluation | ⚠️ Partial | Smart city simulation testbed; comparison against 7 systems (Table 1) |
| T8: Coastal fisheries / maritime | ❌ No | Urban public safety domain |

---

### 7. Overall Relevance Score

**⭐⭐⭐⭐ High** (Verified from full text — PDF uploaded and read, 14+ pages)

The most formally explicit evidence of the binary governance gap in IoT safety systems. Equation 4 (φ(X(t)) = {1, 0}) is the exact mathematical structure that the proposed architecture generalises to three states. Nature portfolio journal adds citation authority. The system's 5-layer architecture, formal latency model, and rich environmental sensor input make the binary ceiling especially stark — all the infrastructure for graduated governance exists, but the decision function reduces to a single binary threshold.
