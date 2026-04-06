# Low-Resource Environments: Definition, Architectural Fit, and Contribution Status

**Document type**: Theoretical justification / argumentation note  
**For**: Chapter 1 (Introduction), Chapter 3 (Architecture Design), and viva preparation  
**Questions addressed**: What is a low-resource environment? Why is the architecture suitable? Computational cost? Offline operation? Data sources? Data quality dependence? Applicability to developed countries? Constraint or contribution? Design implications?

**Cross-references**: For domain generality, see `justification-unified-governance.md` §9 and `justification-caution-mode-operation.md` §7. For why environmental state (not AI confidence) as trigger, see `justification-environmental-state-governance.md` §3.2 (independent observability) and §3.5 (domain empirical validation).

---

## 1. What Is a Low-Resource Environment?

### 1.1 Definition

A low-resource environment is a deployment context characterised by structural constraints in one or more of five dimensions:

| Constraint dimension | Manifestation in coastal fisheries | Evidence |
|---|---|---|
| **Limited data** | No standardised catch data, no trip logs, no historical fisheries databases; data collection depends on individual fisher recall or intermittent enumerator surveys | Longobardi et al. (2025 — Peskas): first automated analytics platform for "data-deficient" SSFs; Timor-Leste deployment demonstrates operation where no prior fisheries data system existed |
| **Limited connectivity** | Intermittent or no internet at sea; mobile network coverage unreliable in coastal areas; satellite connectivity expensive | Katende (2026): "unreliable connectivity" as a primary constraint axis; fishers at sea have no guaranteed data connection |
| **Limited compute** | No access to cloud computing from vessels; devices limited to smartphones or basic tablets; no GPU resources for local inference | Katende (2026): "low compute" constraint mapped to TinyML, knowledge distillation, and model compression methods |
| **Limited institutional capacity** | No dedicated IT staff, no data science expertise, no formal data governance processes; fisheries agencies in developing countries have minimal technical infrastructure | Longobardi et al. (2025): Peskas deployed with Timor-Leste's national fisheries agency, one of the world's least-resourced |
| **Limited financial resources** | Small-scale fishers operate on subsistence or near-subsistence incomes; no budget for specialised equipment, software licenses, or connectivity subscriptions | Yamin et al. (2025): 67.6% of surveyed fishers rely solely on fishing for household income; Rahim et al. (2024): fishers' adaptive capacity constrained by economic vulnerability |

### 1.2 Low-Resource Is Not a Synonym for Low-Tech

Small-scale fishers in Malaysia and Indonesia are not technology-absent. Yamin et al. (2025) document that fishers use weather apps (Windy, Windfinder) for raw environmental data. Gao (2024) documents active use of social media (WhatsApp groups) for information sharing among Penang fishers. Rahim et al. (2024) document mobile phone ownership among Indonesian coastal fishers. The constraint is not access to devices — it is access to the data infrastructure, connectivity, and computational resources that mainstream AI systems assume.

Katende (2026) articulates this distinction precisely: low-resource AI design is not about making sophisticated AI "work despite limitations" but about designing from structural constraints as first-order design requirements. The architecture's design choices are not accommodations of poverty but responses to measured deployment constraints.

---

## 2. Why Is the Architecture Suitable for Low-Resource Environments?

### 2.1 The Governance Layer Is Computationally Lightweight

The governance layer — S = f(E) → (G(S), A_AI(S)) — consists entirely of:
- Threshold comparisons on six environmental parameters
- A worst-case aggregation (max-severity across six component classifications)
- Two lookup operations (G(S), A_AI(S))

This is computationally trivial. It requires no matrix operations, no model inference, no gradient computation, no GPU. It can execute on any microcontroller, smartphone, or embedded device in constant time O(1) with negligible memory. The entire governance function could be implemented in fewer than 100 lines of code in any programming language.

### 2.2 The Architecture Separates Governance from AI Inference

The three-layer design — Environment → Governance → AI Reasoning — means the governance layer functions independently of the AI reasoning layer's computational requirements. Even if the AI model requires cloud inference (because local compute is insufficient), the governance layer operates locally:

| Component | Compute requirement | Connectivity requirement | Can run locally? |
|---|---|---|---|
| f(E) classification | Negligible | None — uses local sensor data | Yes |
| G(S) gate | Negligible | None — lookup function | Yes |
| A_AI(S) scope | Negligible | None — lookup function | Yes |
| AI recommendation generation | Moderate to high (depends on model) | Possibly — may need cloud inference | Depends on implementation |

This means governance is always available, even when the AI component is not. The safety guarantee (Safety Dominance Property) holds as long as the governance layer functions — which it always can, because its computational requirements are negligible.

### 2.3 Environmental State Is Observable Without Data Infrastructure

The conditioning variable S = f(E) requires six environmental parameters. Every one is observable without sophisticated data infrastructure:

| Parameter | Low-resource observation method | High-resource observation method |
|---|---|---|
| Wind speed (w) | Beaufort scale estimation by eye; handheld anemometer (~$20) | Automated weather station |
| Rainfall (r) | Visual observation (none/light/moderate/heavy) | Rain gauge, weather radar |
| Marine warnings (m) | Radio broadcast; SMS alert from maritime authority | API integration with weather service |
| Ocean state (o) | Visual wave height estimation (Douglas scale); swell observation | Wave buoy, satellite altimetry |
| Vessel condition (v) | Pre-departure visual inspection checklist | IoT sensor instrumentation |
| Time of day (t) | Clock, sunrise/sunset knowledge | GPS with astronomical computation |

The governance layer does not require calibrated instruments, continuous data streams, or real-time API access. It can operate on qualitative assessments — the same assessments fishers already make before every trip. Gao (2024) documents that fishers assess tide (4.55/5 importance), weather (3.75/5), and safety (3.40/5) as part of their daily decision-making. The governance layer formalises these existing assessments, not replaces them with technology-dependent measurements.

This is a direct consequence of choosing environmental state as the governance trigger. Alternative triggers — AI confidence, model uncertainty, performance degradation — all require the AI system to be operational and generating outputs before governance can function. Environmental state governance requires only sensor observation, making it the only governance trigger suitable for low-resource deployment. See `justification-environmental-state-governance.md` §3.2 for the full independence argument.

---

## 3. Can the System Run Offline?

### 3.1 The Governance Layer: Fully Offline

The governance layer requires no connectivity. f(E) operates on locally observed environmental parameters. G(S) and A_AI(S) are deterministic lookups. The governance function is fully offline-capable by design.

### 3.2 The AI Layer: Depends on Implementation

The AI reasoning layer's connectivity requirement depends on the implementation strategy:

**Offline-capable implementations:**
- Pre-trained model deployed locally on device (smartphone, tablet)
- Rule-based expert system with locally stored decision rules
- Lookup tables with pre-computed recommendations for common parameter combinations
- TinyML models compressed for edge inference (Katende, 2026 — knowledge distillation, model compression)

**Connectivity-dependent implementations:**
- Cloud-hosted model with API-based inference
- LLM-based recommendation generation

The architecture does not prescribe which implementation is used. For low-resource deployment, offline-capable implementations are preferable. The architectural contribution is that the governance layer works regardless — even if the AI layer is unavailable due to connectivity loss, the governance layer still classifies the environment and can communicate the safety state to the user (the warning-only fallback discussed in `justification-ai-necessity.md` §5).

### 3.3 Graceful Degradation Under Connectivity Loss

The three-layer separation enables graceful degradation:

| Scenario | Layer 1 (Sensors) | Layer 2 (Governance) | Layer 3 (AI) | User experience |
|---|---|---|---|---|
| Full connectivity | Available | Available | Available | Full governance + AI recommendations |
| Connectivity lost | Available | Available | **Unavailable** (if cloud-dependent) | Governance mode still visible; no AI recommendations |
| Sensor failure (partial) | **Partial** | Available (worst-case: escalate to CAUTION/UNSAFE for missing parameters) | Available | Conservative governance; AI recommendations within restricted scope |
| Full system failure | Unavailable | Unavailable | Unavailable | Fisher relies on own judgement (status quo) |

The worst case (full system failure) is equivalent to the current status quo — fishers deciding without any AI support. Every functioning intermediate state provides value above the status quo. This fail-safe degradation is a direct architectural consequence of the layered design and the independence of the governance layer from the AI layer.

---

## 4. What About Data Quality?

### 4.1 The Governance Layer Is Not Data-Quality-Dependent

The governance layer classifies environmental conditions from physical observations. These observations can be imprecise (Beaufort scale wind estimation rather than anemometer measurement) without catastrophic consequence. The classification function f(E) uses ordinal thresholds — the question is "is wind above or below the CAUTION threshold?" not "what is the exact wind speed to 0.1 knots?" Ordinal assessments are robust to measurement imprecision.

Misclassification due to imprecise input is analysed in `justification-safety-state-design.md` §3: over-classification (false CAUTION) is safe; under-classification (false SAFE) is mitigated by conservative threshold setting and worst-case aggregation. The architecture is designed to tolerate the measurement imprecision inherent in low-resource observation methods.

### 4.2 The AI Layer Is Data-Quality-Dependent

The AI reasoning layer's recommendation quality depends on the data it is trained on and the data available at inference time. In low-resource environments, training data is scarce and potentially noisy. This is a real constraint — but it is a constraint on the AI *within each recommendation type*, not on the governance architecture.

The governance architecture actually *mitigates* this constraint through scope restriction. Under CAUTION, the AI generates only go/no-go and delay guidance — recommendation types that depend on threshold-crossing and trend assessment, which are inherently more robust to data quality limitations than precise temporal or spatial recommendations. The architecture matches AI output scope to what the available data can reliably support — which is the CAUTION mode's core design principle.

Katende (2026) documents methods specifically designed for data-scarce AI: few-shot learning, physics-informed neural networks, transfer learning, active learning. These methods can be used in the AI reasoning layer to maximise recommendation quality under data constraints. The governance layer does not depend on them.

---

## 5. Could This Architecture Be Used in Developed Countries?

### 5.1 Yes — Low-Resource Is a Deployment Context, Not a Development Category

The architecture addresses *deployment constraints*, not *national development status*. Low-resource deployment contexts exist in developed countries:

| Developed-country low-resource context | Constraints present |
|---|---|
| Remote agricultural operations (Australia, Canada) | Limited connectivity, limited data, extreme distances |
| Small-scale coastal fishing (Mediterranean, Nordic) | Limited data infrastructure, intermittent connectivity at sea |
| Mountain rescue / search and rescue | No connectivity, extreme conditions, limited compute |
| Remote mining operations | Intermittent connectivity, harsh environment, limited institutional IT |
| Disaster response in affected areas | Infrastructure destroyed, no connectivity, limited compute |

The architecture's suitability for these contexts follows from the same properties that make it suitable for Malaysian coastal fisheries: lightweight governance computation, offline-capable governance layer, environmental state observation without data infrastructure, and graceful degradation under connectivity loss.

### 5.2 The Architecture Also Works in High-Resource Contexts

In high-resource environments, the architecture operates identically but with enhanced implementation:
- Sensor data comes from calibrated instruments rather than visual estimation
- AI models are more sophisticated (larger, cloud-hosted, ensemble methods)
- Connectivity enables real-time weather API integration
- Historical data improves threshold calibration

The governance architecture — S = f(E) → (G(S), A_AI(S)) — is unchanged. Higher-quality inputs produce higher-quality governance classifications and higher-quality AI recommendations, but the formal properties (containment, Safety Dominance) hold regardless of input quality. The architecture scales up gracefully; it is designed for the floor, not the ceiling.

---

## 6. Is Low-Resource a Constraint or a Contribution?

### 6.1 Both — At Different Levels

**Low-resource is a constraint at the implementation level.** It limits which AI methods are feasible (no large models, no continuous cloud inference), which sensor technologies are available (visual estimation, not automated stations), and which deployment models work (offline-first, not cloud-dependent). These constraints narrow the implementation design space.

**Low-resource is a contribution at the architectural level.** The constraints force design choices that produce desirable architectural properties:

| Constraint | Forced design choice | Resulting architectural property |
|---|---|---|
| No reliable connectivity | Governance must work locally | Governance independence from cloud/AI |
| Limited compute | Governance must be lightweight | Deterministic threshold classification (not learned model) |
| Imprecise sensors | Governance must tolerate measurement noise | Ordinal thresholds, worst-case aggregation |
| No AI infrastructure at sea | Governance trigger must not depend on AI | Environmental state conditioning (not AI confidence) |
| Low user technical literacy | Governance modes must be interpretable | Three-state proceed/caution/stop grammar |

Each forced design choice aligns with a formal requirement of the architecture: governance independence from AI (Bloomfield & Rushby, 2025), deterministic governance (for formal verifiability), environmental state conditioning (for causal primacy), and interpretable discrete states (for trust calibration). The low-resource context forces the architecture toward formally desirable properties that a high-resource context might not demand.

### 6.2 The Research Title Reflects This Dual Role

The dissertation title — "A Graduated Safety-State-Gated Architecture for AI Decision Support in **Low-Resource Environments**" — frames low-resource as the deployment context that motivates and validates the architecture. The architecture is not "for low-resource environments" in the sense that it only works there; it is designed *from* low-resource constraints, producing properties (independence, determinism, interpretability) that are valuable in any deployment context but are *essential* in low-resource ones.

---

## 7. How Does Low-Resource Affect AI Decision Support Design?

### 7.1 Design Principles Forced by Low-Resource Constraints

Katende (2026) establishes six design principles for data-efficient AI in low-resource settings. Three are directly relevant to the proposed architecture:

**Offline-first design.** Systems must function without continuous connectivity. The proposed architecture satisfies this at the governance layer (fully offline) and accommodates it at the AI layer (implementation choice between local and cloud inference).

**Constraint-first method selection.** AI methods should be selected based on measured deployment constraints, not transferred from high-resource contexts. The proposed architecture applies this principle at the architectural level: the governance layer's design is determined by what the deployment context can reliably provide (environmental observations from non-AI sources), not by what a well-resourced deployment could theoretically offer.

**Interpretability as a non-negotiable.** In contexts where users cannot evaluate AI outputs technically, system behaviour must be interpretable through domain-relevant concepts. The three-state SAFE/CAUTION/UNSAFE classification — mapping to the proceed/caution/stop grammar that fishers already use (Gao, 2024) — satisfies this requirement without technical explanation.

### 7.2 What Low-Resource Excludes

Low-resource constraints exclude certain design approaches that might otherwise be considered:

| Excluded approach | Why excluded | What the architecture uses instead |
|---|---|---|
| Continuous uncertainty quantification (Bayesian inference, deep ensembles) | Computationally expensive; requires reliable model infrastructure | Deterministic threshold classification |
| AI-confidence-based governance | Requires AI to be running to assess its own confidence | Environmental state classification from sensors |
| Cloud-dependent real-time processing | No reliable connectivity at sea | Local governance + optional cloud AI |
| Complex multi-level graduated governance (5+ levels) | Requires fine-grained sensor data and user training | Three levels with maximum distinguishability |
| Continuous risk scoring with dynamic threshold adjustment | Requires calibration data, compute, and connectivity | Fixed thresholds calibrated at design time, updatable between deployments |

Perez-Cerrolaza et al. (2024) note the SWaP (Size, Weight, Power) constraints on edge-deployed safety-critical AI systems. The proposed architecture's governance layer has negligible SWaP requirements — it is deployable on any device capable of running a simple conditional statement.

---

## 8. Comparative Summary Table

| Question | Answer | Key justification |
|---|---|---|
| **What is low-resource?** | Deployment context with structural constraints in data, connectivity, compute, institutional capacity, and/or finances | Five constraint dimensions; not a synonym for low-tech (Katende, 2026) |
| **Why suitable for low-resource?** | Governance layer is computationally negligible, operates on locally observable parameters, requires no AI infrastructure | f(E) is threshold comparisons + lookups; all parameters observable without instruments |
| **Computational cost?** | Governance: O(1), negligible. AI: depends on implementation | Governance independent of AI compute requirements |
| **Offline operation?** | Governance: fully offline. AI: depends on implementation | Three-layer separation enables graceful degradation |
| **Connectivity loss?** | Governance continues; AI may be unavailable; system degrades to governance-only (safety state visible, no recommendations) | Worst case = status quo (no AI support) |
| **Data sources?** | Visual estimation, handheld instruments, weather apps, maritime radio, pre-departure checklist | Same sources fishers already use (Gao, 2024; Yamin et al., 2025) |
| **Data quality dependence?** | Governance: tolerant of imprecision (ordinal thresholds). AI: quality-dependent but mitigated by scope restriction | CAUTION restricts to recommendation types robust to data limitations |
| **Developed countries?** | Yes — low-resource is a deployment context, not a national category | Remote agriculture, small-scale coastal fishing, disaster response, mountain rescue |
| **Constraint or contribution?** | Both: constraint at implementation level; contribution at architectural level (forces independence, determinism, interpretability) | Constraints produce formally desirable properties (Bloomfield & Rushby, 2025) |
| **Design implications?** | Offline-first, constraint-first, interpretability as non-negotiable; excludes uncertainty quantification, confidence-based governance, cloud-dependent processing | Katende (2026): design from constraints, not despite them |

---

## 9. One-Paragraph Summary (for use in Chapter 1 or Chapter 3)

> Low-resource environments — characterised by structural constraints in data availability, connectivity, compute, institutional capacity, and finances (Katende, 2026) — are not a peripheral deployment concern but a first-order architectural design driver. The proposed architecture is suitable for low-resource deployment because the governance layer — the safety-critical component — is computationally negligible (threshold comparisons and lookups on six parameters), fully offline-capable (no AI infrastructure or connectivity required), and observable without sophisticated instrumentation (environmental parameters are the same inputs fishers already assess daily: wind, waves, rainfall, marine warnings, vessel condition, time — Gao, 2024; Yamin et al., 2025; Rahim et al., 2024). The three-layer separation (Environment → Governance → AI Reasoning) enables graceful degradation: if the AI layer is unavailable due to connectivity loss or compute limitations, the governance layer continues functioning, providing safety state classification even without recommendations — a degradation mode superior to the current status quo of no decision support. Low-resource constraints are simultaneously a deployment constraint (limiting which AI methods and sensor technologies are feasible) and an architectural contribution driver: they force design choices — governance independence from AI, deterministic classification, environmental state conditioning, three-state interpretability — that align with formal requirements for assuredly guarded systems (Bloomfield & Rushby, 2025), verifiable safety guarantees (Dalrymple et al., 2024), and trust calibration through stable, interpretable system modes (McGrath et al., 2025). The architecture is not restricted to low-resource contexts: it functions identically in high-resource environments with enhanced implementation (calibrated sensors, sophisticated AI models, continuous connectivity), because the formal properties hold regardless of input quality. Low-resource is the design floor that ensures the architecture works everywhere, not a ceiling that limits where it applies.
