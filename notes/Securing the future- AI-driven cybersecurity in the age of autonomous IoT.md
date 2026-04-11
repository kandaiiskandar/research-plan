## Literature Review Extraction — GAP-FOCUSED
### Ogenyi, Ugwu & Ugwu (2025) — Securing the future: AI-driven cybersecurity in the age of autonomous IoT

---

### 1. Paper Identity

- **Title:** Securing the future: AI-driven cybersecurity in the age of autonomous IoT
- **Authors:** Ogenyi FC¹, Ugwu CN², Ugwu OP-C¹
- **Affiliations:** ¹Department of Electrical, Telecommunication and Computer Engineering, Kampala International University, Kampala, Uganda; ²Department of Publication and Extension, Kampala International University, Kampala, Uganda
- **Author contributions:** FO: Writing – original draft, Conceptualization. CU: Writing – review and editing, Methodology. O-CU: Supervision, Writing – review and editing, Writing – original draft.
- **Year:** 2025 (Published 4 September 2025)
- **Journal:** Frontiers in the Internet of Things, Volume 4, Article 1658273
- **DOI:** https://doi.org/10.3389/friot.2025.1658273
- **Type:** Narrative review (peer-reviewed, open access CC BY)
- **URL:** https://www.frontiersin.org/journals/the-internet-of-things/articles/10.3389/friot.2025.1658273/full
- **Funding:** No financial support received
- **Generative AI statement:** "The author(s) declare that no Generative AI was used in the creation of this manuscript" (p.14)
- **Citation Quality:** Frontiers peer-reviewed journal. Comprehensive narrative review covering the full A-IoT cybersecurity landscape with 100+ references.

---

### 2. Core Contribution

- **Problem:** The evolution from traditional IoT to Autonomous IoT (A-IoT) — "self-governing, adaptive, and capable of autonomous decision-making" — creates novel cybersecurity challenges. "The scale, speed, and sophistication of current cyber threats are proving to be more than what can be handled by traditional rule-based defense mechanisms" (p.6). AI is needed to "shift into proactive and autonomous defense instead of reactive positions" (p.6).
- **Key concept — IoT evolution (Figure 1, p.3):** Three generations: (1) Basic IoT (connected devices, sensors), (2) Smart IoT (AI-enhanced, edge computing), (3) Autonomous IoT (self-governing, adaptive, autonomous decision-making, 5G/6G, distributed edge computing).
- **Cybersecurity challenges (Table 1, p.4):** 8 categories: Data Privacy & Integrity, Network Security, Device Authentication, Firmware Vulnerabilities, Adversarial Attacks on AI, Scalability, Regulatory Compliance, Supply Chain Security.
- **AI techniques for A-IoT cybersecurity (Figure 2, p.5; Table 3, p.8):** 9 AI techniques mapped to domains and functions:
  - Machine Learning → anomaly detection, malware classification
  - Deep Learning → intrusion detection, pattern recognition
  - Federated Learning → privacy-preserving training across devices
  - Swarm Intelligence → distributed threat detection, routing defense
  - Explainable AI (XAI) → transparent decision-making in detection
  - GANs → attack scenario modeling, synthetic data generation
  - Digital Twins → simulated threat response, system-level testing
  - Transfer Learning / Meta-Learning → rapid adaptation to new threats
  - Reinforcement Learning → autonomous response, adaptive defense
- **AI-driven cybersecurity techniques (Section 5):**
  - **5.1 IDS/IPS:** "Adaptive IPS systems surpass traditional methods by implementing real-time prevention measures, such as blocking malicious traffic or isolating compromised nodes" (p.6) — **binary: block/isolate**
  - **5.2 Anomaly detection:** Unsupervised learning (k-means, autoencoders, SVMs) for identifying anomalous behavior — **binary: normal/anomalous**
  - **5.3 Malware classification:** CNNs, RNNs for classifying malware variants — **binary: malware/benign**
  - **5.4 Authentication & access control:** "Methods such as decision trees and reinforcement learning adjust access privileges on a real-time basis depending on the level of risk" (p.7) — **adaptive privileges, but still binary authorized/unauthorized**
  - **5.5 Lightweight cryptography:** AI used to "dynamically switch key sizes, cypher strength, and mode of operation based on the degree of threat and available resources" (p.7) — **adaptive encryption parameters, not governance**
  - **5.6 Autonomous response:** "take immediate actions without human intervention. In a particular case, it could become isolated when identifying a compromise, reorganize the network association, or deploying decoy services" (p.7) — **autonomous but binary: threat → response**
- **Comparison of traditional vs. AI-driven security (Table 2, p.6):** 6 criteria (Adaptability, Detection Accuracy, Latency, Scalability, Real-Time Response) — AI improves all, but governance structure unchanged.
- **Case studies (Section 7, Figure 3, p.9):** Smart cities, healthcare, autonomous vehicles, IIoT, energy/smart grids. All domains show AI used FOR security, never environmental state governing AI scope.
- **Evaluation metrics (Table 4, p.11):** 8 metrics: Accuracy, Precision/Recall/F1, FPR, Latency, Energy Efficiency, Model Interpretability, Robustness, Scalability, Deployment Readiness.
- **Key adaptive security quote (Section 9, p.12):** "security models that can dynamically adapt the level of protection to the level of threat, the state of devices, and the priorities of the work" (citing Mallick and Nath, 2024). This is the most explicit statement of adaptive security in the paper — and it refers to adapting PROTECTION INTENSITY, not GOVERNANCE MODE.

---

### 3. Governance Mechanism Analysis

| Property | Assessment |
|---|---|
| **Governance type** | **Binary** — across all 6 cybersecurity technique categories (Section 5), every decision is binary: block/allow, malware/benign, normal/anomalous, authorized/unauthorized, threat/no-threat. No intermediate governance mode despite extensive discussion of "adaptive" security. |
| **Trigger** | AI-based anomaly detection, behavioural analytics, threat signatures, risk level assessment |
| **Intermediate mode?** | **No** — Section 9 discusses adaptive security that "dynamically adapt[s] the level of protection to the level of threat" (p.12), but this adaptation scales *protection intensity* (encryption strength, monitoring sensitivity, access privilege scope), not *advisory scope* or *governance mode*. The governance decision for any specific action remains binary: allow or block. |
| **Environmental conditioning?** | **No** — governance is conditioned on threat detection (internal system state), not on external environmental conditions. Sensors detect threats, not environmental states that would govern AI output scope. |
| **Advisory scope restriction?** | **No** — no concept of restricting what AI may recommend based on conditions. AI either operates fully (recommending responses across all domains) or blocks specific actions. Section 5.6: autonomous response systems "take immediate actions without human intervention" — no scope restriction on what actions may be taken. |
| **Key distinction** | "Adaptive security" in A-IoT means scaling **protection intensity** (key sizes, monitoring depth, authentication stringency) and **detection sensitivity**, not changing the **governance mode** or **AI advisory scope**. Section 5.5's "dynamically switch key sizes, cypher strength, and mode of operation based on the degree of threat" (p.7) is the clearest example: the system adapts *how strongly* it protects, not *what AI is permitted to recommend*. |

---

### 4. Governance Level Analysis

| Level | Question | Implemented? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI act at all? (G(S)) | **Yes (binary)** | AI-driven security can block IoT device actions deemed threatening. Section 5.1: IPS "blocking malicious traffic or isolating compromised nodes" (p.6). This is binary participation: AI blocks or permits. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | **No** | No restriction on what AI recommends — only whether specific actions are blocked. Section 5.6: autonomous response systems can isolate, reorganize networks, deploy decoy services — no scope restriction on response types. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | **No** | Governance conditioned on threat state (internal), not environmental state (external). No classification of environmental conditions into governance modes. |

---

### 5. Gap Evidence for Novelty Argument

**Key finding:** This paper reviews the **entire landscape** of AI-driven governance for Autonomous IoT systems — systems explicitly described as "self-governing" and "adaptive" (p.3, Figure 1). Despite these descriptors, and despite covering 9 AI technique categories (Table 3) and 5 application domains (Figure 3), the governance mechanisms are **uniformly binary** (detect/block) across every category.

**The "adaptive security ≠ adaptive governance" distinction:** The paper's most important contribution to the gap argument is in Section 9 (p.12), where it identifies the need for "security models that can dynamically adapt the level of protection to the level of threat, the state of devices, and the priorities of the work." This is the A-IoT community's vision of adaptive security — and it means adapting **how intensely the system protects** (encryption strength, monitoring depth, detection thresholds), NOT **what the AI is allowed to recommend**. Three specific examples from the paper:

1. **Section 5.5 (p.7):** "dynamically switch key sizes, cypher strength, and mode of operation based on the degree of threat" — adapts encryption parameters, not governance
2. **Section 5.4 (p.7):** "adjust access privileges on a real-time basis depending on the level of risk" — adapts access privileges, but the decision remains binary (authorized/unauthorized)
3. **Section 5.6 (p.7):** Autonomous response systems "take immediate actions without human intervention" including isolating compromised nodes, reorganizing networks, deploying decoy services — the AI can do anything it deems necessary, with no scope restriction based on environmental conditions

**The A-IoT governance gap:** Autonomous IoT represents the frontier of self-governing AI in sensor-rich environments. If any domain should have implemented environment-state-conditioned governance, it is A-IoT. The fact that A-IoT governance remains binary — even when the paper explicitly discusses adaptive, environment-aware, self-governing systems — demonstrates that the conceptual leap from "environmental data as input to AI reasoning" to "environmental state as governance trigger over AI advisory scope" has not been made.

**The future directions gap (Section 10):** The paper envisions "fully autonomous cybersecurity agents" (p.13), "self-healing security systems" (p.12), and systems that "strike a balance between autonomy and control" (p.13). Even in this forward-looking vision, governance remains binary — the balance between autonomy and control is framed as preventing "self-healing operations [from] unintentionally interfer[ing] with lawful activities" (p.13), not as graduated governance modes with different advisory scopes.

**Use in justification:** Cite as evidence that the Autonomous IoT literature — which explicitly discusses self-governing, adaptive AI systems operating in sensor-rich environments — implements binary governance only. The term "adaptive security" in A-IoT means adaptive protection intensity (encryption, monitoring, detection thresholds), not adaptive governance modes with graduated advisory scope. This demonstrates the conceptual gap: the IoT community scales *how strongly* systems protect but does not implement *graduated governance modes that restrict what AI may recommend* based on classified environmental state.

---

### 6. Theme Relevance

| Theme | Match? | Notes |
|---|---|---|
| T1: Hybrid AI | ✅ Yes | Reviews ML, DL, FL, swarm intelligence, XAI, GANs, RL, digital twins integrated with IoT infrastructure (Table 3) |
| T2: Safety-critical AI | ✅ Yes | Cybersecurity for autonomous systems; "automated decisions may have operational and safety-relevant consequences" (p.12); mission-critical A-IoT domains (autonomous vehicles, smart grids, healthcare) |
| T3: AI governance | ✅ Yes | Governance frameworks for A-IoT reviewed — all binary. Section 9 explicitly discusses adaptive security as adapting protection intensity, not governance mode. Future directions envision "balance between autonomy and control" (p.13) — still binary framing. |
| T4: Low-resource environments | ✅ Yes | Explicitly discusses resource constraints: "computational overhead and energy needs of AI models are realistic constraints to implementing AI models on lightweight A-IoT devices" (p.6); lightweight cryptography (Section 5.5); edge computing; "resource-limited" A-IoT environments (p.10); energy efficiency metric (Table 4) |
| T5: Decision architecture formalisation | ❌ No | Narrative review, no formal model |
| T6: Human role | ⚠️ Partial | Discusses human oversight: "human-in-the-loop strategies" (p.13); XAI for "human stakeholders to have an idea of the reasoning behind automated decisions" (p.7); "human supervision systems to assure control and responsibility" (p.13) |
| T7: Socio-technical evaluation | ⚠️ Partial | Discusses ethical issues, regulatory challenges (GDPR, NIST), legal frameworks across jurisdictions (pp.11-12), but no empirical socio-technical evaluation |
| T8: Coastal fisheries / maritime | ❌ No | General A-IoT domain (smart cities, healthcare, autonomous vehicles, IIoT, energy) |

---

### 7. Overall Relevance Score

**⭐⭐⭐⭐ High** (Verified from full text — PDF uploaded and read, 15 pages + references)

Comprehensive review of A-IoT governance confirming the binary paradigm across the **entire** autonomous IoT landscape. The paper's most valuable contribution to the gap argument is the explicit articulation of "adaptive security" as adapting protection intensity — not governance mode. Three concrete examples (Sections 5.4, 5.5, 5.6) demonstrate that even when A-IoT systems adapt dynamically to threat levels, the adaptation is to encryption strength, monitoring depth, and access privilege stringency — never to the scope of what AI may recommend. The future directions (Section 10) envision fully autonomous cybersecurity agents but still frame governance as a binary "autonomy vs. control" balance, not graduated modes. Resource constraint discussion (p.6, Table 4) also supports T4 relevance.
