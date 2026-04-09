# CLGuard: A Context-Aware Suppression Framework for Resilient Driving Control
**Seong, Y., Lim, H., & Yoon, S. (2025)**

---

## 1. Bibliographic Information

- **Title:** CLGuard: A Context-Aware Suppression Framework for Resilient Driving Control
- **Authors:** Yeongju Seong, Hyuk Lim, Seunghyun Yoon
- **Affiliation:** Dept. of Energy Engineering, Korea Institute of Energy Technology (KENTECH), Naju, Republic of Korea
- **Year:** 2025
- **Venue:** 2025 IEEE 30th Pacific Rim International Symposium on Dependable Computing (PRDC)
- **DOI:** 10.1109/PRDC67299.2025.00024
- **Publisher:** IEEE
- **Citation Quality:** ✅ Peer-reviewed IEEE symposium (PRDC — 30th edition, established venue in dependable computing). Acceptable as primary citation.

---

## 2. Early Relevance Gate

| Theme | Match? | Notes |
|-------|--------|-------|
| T1: AI governance architecture | ✅ Yes | Suppression framework as runtime governance wrapper |
| T2: Safety-state classification | ✅ Yes | CLG score classifies scene–action consistency as safe/unsafe |
| T3: Graduated/adaptive autonomy | ❌ No | Binary suppress/permit — no intermediate mode |
| T4: Low-resource / maritime / fisheries | ❌ No | Autonomous driving domain (CARLA simulator) |
| T5: Environmental context in AI safety | ✅ Yes | "Context-aware" — uses driving scene semantics to validate actions |
| T6: Formal safety properties | ⚠️ Partial | Suppression policy is formalised (Eq. 2) but no formal safety proofs |
| T7: Trust / human-AI interaction | ❌ No | No trust measurement or human factors |
| T8: Decision-support systems | ⚠️ Partial | Operates on control commands, not advisory recommendations |

**Gate Decision:** 3+ theme matches → **FULL EXTRACTION**

---

## 3. Research Problem & Motivation

CLGuard addresses the problem that autonomous driving systems are vulnerable to diverse faults — CAN injection attacks, actuator glitches, controller errors, and AI misjudgments — that manifest not as obvious signal anomalies but as control actions inconsistent with the semantic expectations of the surrounding driving scene. Prior anomaly detection approaches are limited to narrow failure categories (signal-level CAN detectors, perception-only VLM applications) and do not provide a mechanism for suppressing unsafe control actions in real time regardless of fault source.

---

## 4. Research Questions / Objectives

No explicit research questions stated. Three contributions claimed:
1. Semantic and fault-agnostic runtime suppression for driving control through CLG-based scene–action alignment
2. A deployable wrapper design requiring no retraining of the existing controller
3. Validation of effectiveness through diverse injected fault scenarios in simulation

---

## 5. Methodology

- **Approach:** Design and experimental evaluation of a runtime suppression framework
- **Core Method:** Pre-trained vision-language model (OpenCLIP ViT-B/32, LAION-2B) computes semantic alignment between driving scene (front-view RGB) and issued control commands via Contrasting Language Goals (CLG)
- **Evaluation Environment:** CARLA 0.9.10.1 simulator, Town03 map, integrated with PYLOT autonomous vehicle framework
- **Fault Injection:** Two representative anomalies injected at random intervals:
  - (i) CAN injection — steering commands overwritten with random values for 3 seconds
  - (ii) Actuator glitch — brake commands ignored, throttle fixed at maximum
- **Episode Design:** 30 episodes per anomaly type, 40–50 seconds each, covering straight roads and intersections
- **Hardware:** Single GPU; average per-frame latency 27 ms

---

## 6. Key Concepts & Definitions

- **Contrasting Language Goals (CLG):** A formulation using paired positive and negative natural language goal descriptions (e.g., "the car is driving safely at an appropriate speed" vs. "the car is accelerating dangerously into traffic") to compute a semantic validity score via cosine similarity in CLIP embedding space
- **CLG Score:** $r_t^{CLG} = \alpha \cdot \text{sim}(I_t, l_{pos}) - \beta \cdot \text{sim}(I_t, l_{neg})$, where $\alpha + \beta = 1$
- **Multi-Modal Context Buffer ($C_t$):** Rolling buffer aggregating: front-view RGB images ($I_{t-k:t}$), vehicle state ($s_{t-k:t}$: velocity, acceleration, yaw), recent control actions ($a_{t-k:t}$: throttle, brake, steer), and semantic validity scores ($r_{t-k:t}^{CLG}$)
- **Suppression Policy:** $\text{suppress}(a_t) \text{ if } r_t^{CLG} < \tau_r \land (|\dot{v}_t| > \tau_{acc} \lor |\dot{\psi}_t| > \tau_{yaw})$ — i.e., semantic score below threshold AND either acceleration magnitude or yaw rate exceeds limits
- **Safe Fallback:** Replacement command (reduced throttle or steering neutralisation) issued when suppression triggered
- **Fault-Agnostic:** Framework does not model specific failure types; evaluates semantic consistency regardless of fault source

---

## 7. Core Architecture / Framework

**Pipeline:** Sensor input → Multi-Modal Context Buffer ($C_t$) → Semantic Evaluation via CLG → Suppression Decision → Safe Fallback (if triggered)

**Architectural properties:**
- **Non-intrusive wrapper:** Wraps around existing autonomy stack without retraining or modification
- **Runtime operation:** Per-frame evaluation at ~27 ms latency
- **Dual-condition gating:** Suppression requires BOTH semantic anomaly (low CLG score) AND dynamic anomaly (excessive acceleration or yaw rate)
- **Temporal smoothing:** Context buffer smooths score variations to prevent false suppressions from transient noise

---

## 8. Findings / Results

| Method | Collision Rate | False Suppression Rate | Latency (ms) |
|--------|---------------|----------------------|---------------|
| Baseline (No Filter) | 45.8% | – | – |
| CLGuard | 6.7% | 7.9% | 27.5 |

- CLGuard reduces collision rate from 45.8% to 6.7% (85.4% reduction)
- Low false suppression rate (7.9%) indicates suppression decisions are well-calibrated
- Real-time capable at 27.5 ms average latency
- Suppression decisions track CLG score trends, confirming the framework captures meaningful scene–action inconsistencies
- Generalises across different fault types without explicit signal-level models

---

## 9. Limitations (Author-Stated)

- Evaluation limited to two representative anomaly types (CAN injection, actuator glitch)
- Simulation-only validation (CARLA) — no real-world deployment
- Future work acknowledged: multi-agent settings, formal semantic safety guarantees, real-world validation

---

## 10. Limitations (Analyst-Identified)

- **Binary governance:** Suppress/permit binary — no intermediate mode (e.g., restricted advisory scope). The system either passes the command through or replaces it entirely with a safe fallback.
- **Hybrid trigger but still partially self-referential:** While CLG uses external scene semantics (a strength), the context buffer includes the AI's own recent CLG scores ($r_{t-k:t}^{CLG}$) as input. The semantic evaluation is applied to the AI's own control commands against the scene, making this a sophisticated form of self-referential validation — the AI is checking its own outputs against visual context, rather than an independent external authority classifying the environmental state.
- **No environmental state classification:** The framework does not classify the operational environment into discrete safety states. It evaluates individual actions against the current scene but does not reason about the broader environmental context (e.g., deteriorating conditions requiring proactive governance changes).
- **Sensor dependency unaddressed:** The CLIP-based semantic evaluation depends on front-view RGB camera quality. In degraded visibility conditions (fog, rain, night, biofouling in maritime analogue), the semantic evaluation itself becomes unreliable — the exact "reliability collapse" problem identified in the argumentative frame.
- **No advisory scope restriction:** Suppression operates at the individual action level. There is no mechanism to proactively restrict the *types* of recommendations/actions the system is permitted to generate before they are issued.
- **Simulation fidelity gap:** CARLA provides clean, repeatable conditions. Real-world sensor degradation, environmental volatility, and edge cases are not tested.

---

## 11. Relevance to Dissertation

### Rating: ⭐⭐⭐⭐ (High)

**Role:** Gap evidence + architectural contrast case for the "Action Suppression → Advisory Space Contraction" argument

### 11.1 Mapping to Governance Architecture

| Governance Element | CLGuard Implementation | Gap Relative to Dissertation |
|---|---|---|
| **E (Environmental input)** | Front-view RGB + vehicle state (velocity, acceleration, yaw) | Limited E vector — no broader environmental state classification |
| **S = f(E)** | ❌ Not implemented | No discrete environmental state classification. CLG score is a continuous per-action validity metric, not an environmental state classifier |
| **G(S) — Level 1 Participation** | ⚠️ Implicit | Binary: AI controller is always active; suppression intervenes at output level. No governance over whether the AI *participates* — only over whether its output is *executed* |
| **A_AI(S) — Level 2 Advisory Scope** | ❌ Not implemented | No restriction on the admissible recommendation/action space. The AI generates any action it wants; CLGuard evaluates post-hoc |
| **Safety Dominance Property** | ⚠️ Partial | Suppression enforces $\text{suppress}(a_t)$ when conditions met, but this is per-action filtering, not containment of the output space: $AI(E) \not\subseteq A_{AI}(S)$ because $A_{AI}(S)$ does not exist |
| **CAUTION mode** | ❌ Absent | Binary suppress/permit. No intermediate mode with restricted-but-non-empty scope |

### 11.2 The Three Argumentative Threads

**Thread 1 — Reliability Collapse:**
CLGuard's semantic evaluation depends on CLIP embeddings of the current visual scene. In maritime environments where sensor degradation (biofouling, spray, fog, corrosion) is caused by the very conditions that should trigger governance transitions, the CLG score itself becomes unreliable. CLGuard has no mechanism to detect or compensate for this — it trusts its own perceptual input. This is the structural vulnerability that justifies externalising the governance trigger to $S = f(E)$ using independently validated environmental state sources (meteorological services, port authority data, vessel monitoring systems) rather than the AI's own sensor-derived assessments.

**Thread 2 — Flehmig Contrast Strengthened:**
CLGuard and Flehmig et al. (2024) share a critical structural property: both rely on the AI system's own internally-derived metrics to trigger governance transitions (Flehmig: confidence scores + drift detection → traffic-light index; CLGuard: CLG semantic score + dynamic thresholds → suppress/permit). Both are therefore vulnerable to the same reliability collapse in volatile environments. Your $S = f(E)$ architecture breaks this self-referential loop by grounding the governance trigger in externally classified environmental state.

**Thread 3 — Action Suppression vs. Advisory Space Contraction:**
This is the strongest framing. CLGuard operates as **per-action post-hoc suppression**: the AI generates an action → CLGuard evaluates it → suppress or pass. Your $A_{AI}(S)$ operates as **proactive advisory space contraction**: the environmental state $S$ determines the admissible recommendation space *before* any specific advisory output is generated. The distinction is:

| Dimension | CLGuard (Action Suppression) | Dissertation $A_{AI}(S)$ (Advisory Space Contraction) |
|---|---|---|
| **When** | Post-generation, pre-execution | Pre-generation |
| **What** | Individual action $a_t$ | Entire admissible set $A_{AI}(S)$ |
| **Mechanism** | Binary filter: pass/suppress | Set restriction: $A_{AI}(SAFE) \supset A_{AI}(CAUTION) \supset A_{AI}(UNSAFE)$ |
| **Guarantee** | If suppression triggers correctly, individual unsafe action blocked | $AI(E) \subseteq A_{AI}(S)$ — Safety Dominance Property ensures *no* inadmissible recommendation can be generated |
| **Failure mode** | Missed suppression → unsafe action executes | Governance state misclassification → wrong scope applied, but scope still bounded |

---

## 12. Key Citations to Follow

| Ref | Citation | Potential Relevance |
|-----|----------|-------------------|
| [1] | Jeong et al. (2023) — X-CANIDS, IEEE Trans. Vehicular Technology | Signal-level anomaly detection — contrast case for semantic approach |
| [2] | Zhou et al. (2024) — AnomalyCLIP, ICLR 2024 | VLM-based anomaly detection — perception-only, no suppression |
| [3] | Huang et al. (2024) — VLM-RL, arXiv | VLM + RL for safe autonomous driving — planning-level, no runtime suppression |

*Assessment:* Low priority for dissertation follow-up. All are autonomous driving-specific and do not address governance architecture.

---

## 13. Quotable Passages

- "many of these faults manifest not as obvious signal anomalies but as control actions that are inconsistent with the semantic expectations of the surrounding driving scene" — useful framing for why semantic validation matters
- "fault-agnostic" — key property claim; your architecture similarly does not model specific failure types
- "non-intrusive wrapper" — architectural pattern analogous to your governance layer sitting outside the AI system

---

## 14. Methodological Concerns

- Only 2 fault types tested; claims of generalisation ("fault-agnostic") are aspirational beyond what is empirically demonstrated
- No ablation separating the contribution of semantic evaluation vs. dynamic thresholds — unclear which component drives the collision rate reduction
- Threshold parameters ($\tau_r$, $\tau_{acc}$, $\tau_{yaw}$) selection not discussed — potential sensitivity analysis gap
- 30 episodes per condition is modest for statistical confidence

---

## 15. Inter-Paper Relationships

| Paper | Relationship |
|-------|-------------|
| **Flehmig et al. (2024)** | Both rely on internally-derived metrics for governance triggering. CLGuard uses semantic scores; Flehmig uses confidence + drift. Both binary. Both vulnerable to reliability collapse in volatile environments. Your $S = f(E)$ addresses the shared structural weakness. |
| **SHIELDAGENT / Chen, Kang & Li (2025)** | Both are runtime safety wrappers. SHIELDAGENT operates at the agent planning level with per-action binary shield; CLGuard operates at the control command level with per-action binary suppression. Neither implements Level 2 scope governance. |
| **Liang et al. (2025, SAFEXPLAIN)** | Both implement output-level gating. SAFEXPLAIN's gatekeeper is closest to $G(S)$; CLGuard's suppression is closest to per-action safety filtering. Neither restricts the admissible space proactively. |
| **Abella et al. (SAFEXPLAIN automotive)** | Both automotive domain. Abella's supervision function / safe envelope concept is closer to $A_{AI}(S)$ than CLGuard's per-action suppression, though still unformalised. |
| **Könighofer et al. (2025)** | Complementary evidence: Könighofer shows intermediate shielding ($\varepsilon$) outperforms binary extremes. CLGuard is a binary extreme — suppress or pass. Provides empirical motivation for why CLGuard's binary approach is suboptimal and graduated governance (CAUTION mode) would improve performance. |
| **Bloomfield & Rushby (2025)** | Both binary permit/override governance. CLGuard implements this at the control command level with semantic validation; Bloomfield & Rushby formalise it at the architectural level. Same gap: no CAUTION mode. |

---

## 16. Citation Placement in Dissertation

| Section | Role |
|---------|------|
| **Section 2/3: AI Safety Governance Mechanisms** | Example of runtime semantic validation — cited alongside SHIELDAGENT and SAFEXPLAIN as state-of-art in action-level safety gating. Maps to Level 1 only (binary suppress/permit) in the escalation from established → emerging → absent |
| **Section 4: The Level 1 / Level 2 Gap** | Enters the classification table as Level 1 only. CLGuard implements per-action binary suppression with no advisory scope governance — no $A_{AI}(S)$, no CAUTION mode. Strengthens the "unified row = None" finding. Strongest exemplar for the "Action Suppression → Advisory Space Contraction" argumentative move |
| **Section 6: Gap Summary** | Supports gap points on binary governance universality and absence of Safety Dominance Property for graduated governance |
| **Formalisation Chapter** | Contrast case for the table distinguishing per-action suppression from proactive advisory space restriction. CLGuard as the exemplar of what the existing paradigm achieves and where it stops |

---

## 17. Tracker Entry

```
| Seong, Lim & Yoon (2025) | CLGuard: Context-Aware Suppression Framework | IEEE PRDC 2025 | ⭐⭐⭐⭐ | Gap evidence + architectural contrast | Semantic suppression via VLM + CLG; binary suppress/permit; per-action post-hoc; no S=f(E), no A_AI(S), no CAUTION mode. Strongest exemplar of Action Suppression paradigm for "→ Advisory Space Contraction" argument. | 2.2, 2.3, Formalisation |
```
