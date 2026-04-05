# Literature Extraction: Bhuvaneswari et al. (2025)
## "A human-centered hybrid AI framework for optimizing emergency triage in resource-constrained settings"

---

## 1. Paper Identity

- **Title:** A human-centered hybrid AI framework for optimizing emergency triage in resource-constrained settings
- **Authors:** E. Bhuvaneswari, K.D.V. Prasad, Mohd Ashraf, Sachin Jadhav, TK Rama Krishna Rao, Tirukoti Sudha Rani
- **Year:** 2025
- **Venue:** Intelligence-Based Medicine, Volume 12, 100311 (Elsevier)
- **Type:** System design paper with empirical evaluation (simulated + pilot)

---

## 2. Core Contribution

- **Problem:** Emergency triage in resource-constrained healthcare settings suffers from cognitive biases (anchoring, availability), human error (up to 32% triage error rates), and inability of traditional triage systems (MTS, ESI) to adapt to changing workloads and resource availability. Existing AI triage systems lack integration of cognitive modelling, resource awareness, and human-in-the-loop feedback.

- **Proposed solution:** A hybrid AI triage framework combining three modules: (1) a **cognitive module** that encodes clinical heuristics and probabilistically models cognitive biases, (2) a **CNN-based predictive module** with SHAP explainability for patient risk scoring, and (3) a **resource-aware optimizer** using integer programming or heuristic reinforcement learning. A human-in-the-loop interface enables clinician overrides with rationale capture for adaptive learning.

- **Main contributions:** Integration of cognitive bias modelling into AI triage; resource-aware optimization that adapts triage labels to actual resource constraints; human-in-the-loop feedback loop for continuous model refinement; demonstration of 90% accuracy, 0.86+ AUC, 31% reduction in decision time, false negative reduction from 12% to 5%.

- **Novelty:** The combination of explicit cognitive bias modelling (probabilistic), resource-constrained optimization, and HITL feedback in a single triage architecture designed for low-resource settings. Most prior AI triage systems address prediction accuracy without integrating resource constraints or cognitive factors.

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | **Yes** | The cognitive module encodes rule-based clinical heuristics (binary decision functions h_j : X → {0,1}) combined with probabilistic bias modelling and a CNN-based predictive module. This is a rule + ML hybrid. |
| Safety-critical AI decision-making | **Yes** | Emergency triage is explicitly safety-critical. The system addresses patient safety through false negative reduction, bias alerts, and clinician override mechanisms. |
| AI governance / control mechanisms | **Partial** | The HITL interface allows clinician overrides, and the cognitive module generates bias alerts. However, there is no formal gate function controlling AI participation based on safety state, and no state-conditioned restriction on AI output scope. |
| Low-resource environments | **Yes** | Explicitly designed for resource-constrained healthcare: rural hospitals, small clinics, disaster scenarios. Resource-aware optimizer accounts for bed, oxygen, and staff constraints. Lightweight CNN architecture. |
| Decision architecture formalisation | **Partial** | Provides mathematical formulations for each module (input vector X_t, cognitive output C(X,c), CNN predictor f_θ, optimizer objective). However, no unified formal pipeline comparable to E → S → (G(S), A_AI(S)) → AI(E). |
| Human role in decision-making | **Yes** | Core design principle. Clinician overrides with rationale capture, confidence signals, bias alerts. System explicitly positioned as decision support, not automation. |
| Socio-technical evaluation | **Partial** | Includes clinician survey feedback (trust 4.2/5, usability 4.0/5, cognitive burden 2.3/5), override analysis (reasons, rationales), and workflow efficiency metrics. Limited by small sample size (15 real cases). |
| Coastal fisheries / maritime domain | **No** | Healthcare/emergency medicine domain. |

**Yes count: 4 | Partial count: 3 → FULL EXTRACTION**

---

## 4. Decision Architecture Analysis

The system structures decision-making as a **parallel-then-sequential pipeline** with four main stages:

**Stage 1 — Input aggregation:** Multi-dimensional input vector X_t = [P_t; C_t; H_t] combining patient features (vital signs, GCS, comorbidities, lactate), context features (beds, oxygen, staff, time-of-day), and human factors (clinician experience, workload, confidence).

**Stage 2 — Dual processing (parallel):**
- **Cognitive module:** Encodes clinical heuristics as binary functions H = {h_j : X → {0,1}} and models cognitive biases probabilistically as b_k = P(bias_k | X, c). Combined cognitive output C(X,c) = Σ w_j·h_j(X) − Σ λ_k·b_k adjusts recommendations and triggers bias alerts.
- **Predictive module:** CNN (2 conv layers, 2 FC layers) produces risk score ŷ_t = f_θ(X_t) with SHAP decomposition for interpretability.

**Stage 3 — Resource-aware optimization:** Integer programming or heuristic RL maps predicted risk and resource needs to feasible triage labels and transfer recommendations under explicit resource constraints (beds ≤ B, oxygen ≤ O).

**Stage 4 — Human-in-the-loop interface:** Presents triage recommendation, confidence score, and bias alert. Clinician accepts or overrides (y_t = ŷ_t or o_t). Override rationale r_t captured. Tuple (y_t, c_t, b_t, r_t) fed back for adaptive learning.

**Rule-based constraints before AI:** The cognitive module's heuristics (e.g., low SpO2, high lactate, high HR thresholds) act as rule-based pre-processing that adjusts or flags recommendations. However, these do not *block* AI participation — they modify the cognitive output score that feeds into the recommendation. There is no formal gate that prevents AI from operating based on safety state.

**Failure modes / fallback:** The clinician override is the primary fallback mechanism. No formal deterministic fallback mode where AI is disabled. The resource optimizer can downgrade triage labels or recommend transfers when resources are insufficient (31 of 100 cases changed due to resource constraints), which is a form of resource-constrained adaptation but not a safety-state gate.

**Comparison to my architecture:** The system has no equivalent to S = f(E) → {SAFE, CAUTION, UNSAFE}. The input vector X_t includes contextual/resource features (analogous to parts of E), but these feed into ML prediction and optimization rather than into a deterministic safety state classifier. There is no gate function G(S) controlling AI participation, and no state-conditioned restriction on what types of recommendations AI may generate.

---

## 5. Formal Model and Mathematical Representation

The paper provides module-level mathematical formulations but no unified formal pipeline:

**Input:** X_t = [P_t; C_t; H_t] — patient, context, human factor vectors (eq. 1)

**Cognitive module:**
- Heuristics: H = {h_j : X → {0,1} | j = 1,...,M} (eq. 2)
- Bias probability: b_k = P(bias_k | X, c) (eq. 3)
- Combined output: C(X,c) = Σ w_j·h_j(X) − Σ λ_k·b_k (eq. 4)

**Predictive module:**
- Risk prediction: ŷ_t = f_θ(X_t) (eq. 5)
- SHAP decomposition: ŷ_t = ϕ_0 + Σ ϕ_i (eq. 6)

**Resource optimizer:**
- Decision variable: x_i ∈ {0,1} (admit or not) (eq. 7)
- Objective: max Σ v_i·x_i subject to bed and oxygen constraints (eqs. 8–11)
- Alternative: RL policy π(s) mapping state to triage actions

**HITL interface:**
- Final decision: y_t = ŷ_t (accept) or o_t (override) (eq. 12)
- Override rationale: r_t = [r_{t,1}, ..., r_{t,m}] (eq. 13)

**Adaptive learning:**
- Dataset: D = {X_i, y_i, o_i, r_i, z_i} (eq. 14)
- Parameter update: θ*, τ* = argmin Σ L(f_θ(X_i; τ), z_i, o_i) (eq. 15)

**Comparison to my pipeline E → S = f(E) → (G(S), A_AI(S)) → AI(E):**

| Component | My Architecture | Bhuvaneswari et al. |
|---|---|---|
| Environmental state vector E | {w, r, m, o, v, t} — environmental | X_t = [P_t; C_t; H_t] — patient + context + human factors |
| Safety state classification S = f(E) | Tripartite: SAFE/CAUTION/UNSAFE | Not present — no safety state classification |
| Gate function G(S) | Binary, state-conditioned | Not present — AI always operates; clinician override is post-hoc |
| Admissible action space A_AI(S) | State-conditioned, graduated | Not present — AI produces full risk scores and triage labels regardless of state |
| Safety Dominance Property | AI(E) ⊆ A_AI(S) | Not present — no formal bound on AI output scope |

**State-dependent recommendation restriction:** Not present. The CNN produces a risk score and the optimizer produces triage labels regardless of any safety state classification. The resource optimizer *adapts* outputs to resource constraints (changing triage labels, recommending transfers), but this is resource-conditioned, not safety-state-conditioned. The adaptation changes *which patients get resources*, not *what types of recommendations AI may generate*.

**Formalisation purpose:** The formalisations are descriptive and implementational — they define each module's computation. They are not used for formal proof or safety property verification.

---

## 6. Safety State Classification

**Discrete risk/safety levels:** The system classifies patients into triage acuity levels (the paper uses triage labels, with at least a RED/high-acuity category visible in the results). However, this is *patient-level acuity classification*, not *environmental/operational safety state classification*.

The resource optimizer implicitly creates resource-feasibility states (60% feasible vs 40% infeasible in Fig. 16), and resource constraints cause triage label changes (31 of 100 cases modified). However, this is not formalised as a discrete safety state classification — it is an optimisation outcome.

**Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:** The paper classifies *patient risk* (high acuity vs non-high), not *environmental safety state*. There is no function that takes environmental conditions as input and produces a categorical safety state that then governs AI behaviour. The contextual features (beds, oxygen, staff) feed into the ML pipeline as input features, not into a deterministic state classifier.

**Critical gap:** The system does not differentiate AI recommendation scope across any safety or risk levels. The CNN always produces a full risk score. The optimizer always produces triage labels and transfer recommendations. There is no mode where AI output types are restricted based on classified state — no equivalent to CAUTION where A_AI(CAUTION) ⊂ A_AI(SAFE).

---

## 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (equivalent to G(S)) | **No** | AI always operates. There is no mechanism to disable AI based on safety state. The clinician can override post-hoc, but AI always generates its recommendation. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (equivalent to A_AI(S)) | **No** | AI always produces the full suite of outputs (risk score, triage label, transfer recommendation). No mechanism restricts output types based on state. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | **No** | No environmental safety state classification exists. No governance pair (G(S), A_AI(S)). |

**Binary vs graduated:** Neither. The system has no AI participation gate at all. AI always runs; governance is entirely post-hoc via clinician override. This is weaker than even binary Level 1 governance — it is *no pre-hoc governance*.

**Governance mechanisms present:** The paper implements governance through:
- **Clinician override** (post-hoc, human-initiated — not system-initiated)
- **Cognitive bias alerts** (informational — flags potential bias but does not restrict AI)
- **Resource constraints** (optimizer adapts outputs to feasibility — resource-conditioned, not safety-state-conditioned)

These are all valuable mechanisms, but none constitute formal governance of AI participation or output scope conditioned on classified environmental safety state.

**Support for two-level governance pair:** The paper's architecture indirectly supports the motivation for my research: even in a system explicitly designed for safety-critical, resource-constrained settings with HITL integration, there is no formal mechanism to govern *when* AI participates or *what* AI may recommend based on environmental safety state. The governance gap exists even in purpose-built safety-critical hybrid AI systems.

---

## 8. Human Role in Decision-Making

**Decision authority:** The system is explicitly positioned as **decision support** — the clinician makes the final decision. The HITL interface presents recommendations, confidence scores, and bias alerts, but the clinician can override with rationale capture.

**Override mechanism:** Formally defined as y_t = ŷ_t (accept) or o_t (override). Override rationale r_t is captured as a vector of qualitative/quantitative annotations. Override data feeds back into adaptive learning.

**Override analysis results:** 45% of overrides attributed to clinical judgment, 25% to contraindications, 15% to system errors, 15% to resource constraints. Override rationales: 55% safety concerns, 20% patient preferences, 15% additional clinical information, 10% other.

**Human factors integration:** The input vector includes clinician experience, workload index, and self-confidence score. The cognitive module models cognitive biases probabilistically. This is more sophisticated human factor integration than most AI decision support systems.

**Relevance to my research:** The human role model (decision support with override) aligns with my architecture's positioning. The override rationale capture and adaptive learning mechanism is relevant to socio-technical evaluation design. However, the override is entirely post-hoc and human-initiated — there is no system-initiated escalation based on classified safety state.

---

## 9. System Constraints and Environment

**Resource constraints:** Central design consideration. The resource-aware optimizer explicitly accounts for bed availability, oxygen supply, and staffing levels. Integer programming or heuristic RL ensures feasible triage labels under constraints. Resource optimization improved critical resource utilisation by 20%.

**Low-resource design choices:**
- Lightweight CNN (2 conv layers, 2 FC layers) — computationally modest
- Heuristic RL alternative to integer programming for real-time performance (< 3s for 500 patients vs 25s for IP)
- Cognitive module encodes clinical heuristics to reduce dependence on large training datasets
- Designed for "rural hospitals, small clinics, and disaster scenarios"

**Real-world deployment:** Evaluated through simulated scenarios and small pilot implementations (15 real patient cases supplemented with synthetic data). Not yet validated in large-scale real-world deployment.

**Edge cases:** The resource optimizer handles infeasible resource allocations (~40% of cases exceeded resource thresholds). When resources are insufficient, the system downgrades triage labels or recommends transfers. This is a form of graceful degradation under resource pressure.

**Relevance to my research:** This is one of the few papers that explicitly designs for resource-constrained settings with lightweight architecture, resource-aware optimization, and adaptation to local constraints. The resource-constraint motivation parallels my low-resource environment theme, though the domain (healthcare) and specific constraints (beds, oxygen, staff) differ from mine (connectivity, compute, maritime infrastructure). The resource-conditioned adaptation (triage label downgrade, transfer recommendation) is conceptually adjacent to my state-conditioned output restriction, but it is triggered by resource feasibility rather than classified environmental safety state.

---

## 10. Hybrid AI Taxonomy

**Hybrid AI type:** This is a **Rule-ML pipeline with resource optimization**:
- Rule-based component: cognitive module with binary heuristic functions h_j
- ML component: CNN-based risk predictor with SHAP
- Optimization component: integer programming / heuristic RL for resource-aware triage
- HITL component: clinician override with feedback loop

**Safety enforcement location:** Safety enforcement is distributed:
- **Before AI reasoning:** Cognitive heuristics (rule-based thresholds for low SpO2, high lactate, high HR) run alongside the CNN, potentially triggering alerts
- **After AI reasoning:** Resource optimizer constrains outputs to feasible allocations; clinician override provides final safety check
- There is no safety enforcement that *blocks* AI reasoning based on classified state

**Two-level governance support:** The hybrid architecture does not support two-level governance. There is no mechanism where both AI participation and AI output scope are governed by safety state. The cognitive module's heuristics adjust scores but do not gate AI participation. The resource optimizer constrains outputs by resource feasibility but not by safety state classification.

**Comparison to my architecture:** My deterministic-gate-first model differs in that: (1) safety state is classified deterministically from environmental inputs before any AI processing, (2) the gate function G(S) can block AI entirely (UNSAFE), (3) the admissible action space A_AI(S) restricts output types by state (CAUTION). This paper's system always runs AI and applies constraints post-hoc through optimization and human override.

---

## 11. Baseline Comparison and Evaluation

**Baselines:**
- CNN vs Logistic Regression vs Random Forest (Table 2)
- CNN accuracy 91% vs LR 83% vs RF 87%
- Baseline triage (no AI) vs AI-assisted triage: false negative rate 12% → 5%, delayed decisions 18% → 7%, inappropriate triage 15% → 4%

**Ablation study (Table 3):**
- Baseline CNN: accuracy 0.83, AUC 0.87, FNR 9.5%
- + Clinician features: 0.86, 0.89, 7.8% (p=0.042)
- + Cognitive module: 0.88, 0.91, 6.2% (p=0.008)
- + Resource optimizer: 0.85, 0.88, 8.1% (p=0.126)
- Full hybrid: 0.91, 0.94, 5.0% (p<0.001)

**CAUTION zone testing:** Not present. No evaluation tests behaviour in an intermediate safety state where AI participates under restriction. The evaluation tests overall accuracy, not graduated governance behaviour.

**Safety Dominance Property verification:** Not present. No formal property verified that AI outputs fall within state-determined bounds.

**Graduated vs binary governance comparison:** Not present. No comparison of governance models.

**Evaluation gaps:**
- Very small real dataset (15 patients), heavily supplemented with synthetic data
- No multi-centre validation
- No evaluation of system behaviour under different environmental safety states
- No formal safety property verification
- No comparison of governance approaches (graduated vs binary vs none)

---

## 12. Key Concepts and Definitions

- **Cognitive module:** Component that encodes clinical heuristics as binary decision functions and probabilistically models cognitive biases (anchoring, availability) to adjust recommendations or trigger alerts.
- **Resource-aware optimizer:** Integer programming or heuristic RL component that ensures triage labels and transfer recommendations are feasible under actual resource constraints (beds, oxygen, staff).
- **Human-in-the-loop (HITL) interface:** Two-way communication interface enabling clinician override with rationale capture, confidence display, and bias alerts, feeding back into adaptive learning.
- **Cognitive bias modelling:** Probabilistic representation b_k = P(bias_k | X, c) of biases (anchoring, availability) that may affect clinician decision-making under stress and uncertainty.
- **Adaptive learning:** Periodic or online parameter and threshold update using combined dataset of AI recommendations, clinician overrides, rationales, and patient outcomes.

---

## 13. Limitations and Unsolved Problems

**Stated limitations:**
1. Very limited real patient data (15 cases) — generalisability is constrained despite synthetic data augmentation.
2. Clinician acceptance and feedback quality may vary by setting.
3. No multi-centre validation.
4. Model performance may not generalise across diverse emergency scenarios and populations.
5. The CNN architecture, while lightweight, was not compared against other lightweight architectures for resource efficiency.

**Gaps aligning with my research problem:**
- **No safety state classification:** The system does not classify the operational environment into discrete safety states. Contextual features (resources, workload) feed into ML as input features rather than into a deterministic state classifier.
- **No AI participation governance:** AI always operates — there is no gate function that blocks or restricts AI based on environmental conditions. Governance is entirely post-hoc via clinician override.
- **No state-conditioned output restriction:** The AI produces the same types of output (risk score, triage label, transfer recommendation) regardless of environmental state. The resource optimizer adapts *which patients get resources*, but does not restrict *what types of recommendations AI may generate*.
- **No Safety Dominance Property:** No formal guarantee that AI outputs remain within state-determined bounds.
- **No CAUTION mode:** There is no intermediate mode where AI participates with restricted output scope. The system is either fully on (always) with post-hoc human override.

---

## 14. Methodology Notes

- **Research method:** System design with simulated + pilot evaluation. Cognitive task analysis and clinician interviews for heuristic elicitation. CNN training on mixed real/synthetic dataset. Evaluation via simulation (100 validation cases), tabletop exercises, and small pilot deployment.
- **Alignment with DSR:** Partially aligns — the paper follows a design → implement → evaluate cycle. However, it lacks formal model verification and does not use a formal DSR methodology framework.
- **Methodological utility for my research:** The cognitive task analysis approach for eliciting clinical heuristics is potentially informative for my approach to eliciting fisher decision heuristics. The HITL override rationale capture mechanism is relevant to my socio-technical evaluation design. The resource-aware optimization approach (adapting outputs to constraints) is conceptually related to my state-conditioned output restriction, though implemented differently (optimization feasibility vs deterministic safety state governance). The ablation study methodology (testing component contributions) could inform my evaluation of the two-level governance model's value.

---

## 15. Quotable / Citable Points

1. **Triage error rates (Section 1):** The paper notes that triage error rates can reach up to 32% in certain systems, and that over 80% of physicians in some regions lack formal training in pediatric emergency triage.

2. **Hybrid system design rationale (Section 1/3):** The framework combines cognitive modelling, lightweight ML, and resource-aware optimization to provide adaptive triage recommendations, allowing clinicians to override as needed — positioning AI as complement rather than replacement for clinical judgment.

3. **Resource-constrained adaptation (Section 4, Fig. 14):** Of 100+ patients, 31 cases had triage labels modified due to resource constraints (15 downgraded, 15 transferred), demonstrating resource-conditioned adaptation of AI outputs — though this is resource-feasibility-driven, not safety-state-driven.

4. **Override analysis (Section 4, Figs. 17–18):** 45% of clinician overrides were attributed to clinical judgment and 55% of override rationales cited safety concerns, indicating that safety considerations drive human override behaviour in AI-assisted triage.

5. **False negative reduction (Section 4, Fig. 23):** The hybrid AI system reduced false negative rates for high-acuity patients from 12% to 5% compared to baseline triage — a 58% relative improvement in detection of critical cases.

---

## 16. Relation to My Research and Positioning

**Level 1 governance:** Not implemented. AI always operates; no gate function blocks AI based on safety state. Clinician override is post-hoc, not pre-hoc.

**Level 2 governance:** Not implemented. AI produces full output suite regardless of state. Resource optimizer adapts triage labels to feasibility constraints, but this is not state-conditioned output-scope governance.

**State-conditioned governance pair:** Not present. No (G(S), A_AI(S)) equivalent.

**Safety Dominance Property:** Not present. No formal safety property verified.

**Gap my research addresses:** The paper demonstrates that even a purpose-built hybrid AI system for safety-critical, resource-constrained emergency care — with cognitive modelling, HITL integration, and resource-aware optimization — does not implement: (1) environmental safety state classification, (2) AI participation governance conditioned on safety state, (3) state-conditioned restriction on AI output scope, or (4) a formal Safety Dominance Property. My architecture fills these gaps with the two-level governance pair (G(S), A_AI(S)) and the Safety Dominance Property AI(E) ⊆ A_AI(S).

**Positioning paragraph:** This paper serves as **domain-adjacent gap evidence** and **partial design parallel** for my research. It is one of the few papers that explicitly designs a hybrid AI decision support system for safety-critical operations in resource-constrained settings — the same high-level design context as my architecture, though in healthcare rather than coastal fisheries. The paper's resource-aware optimizer, which adapts triage labels to actual resource constraints, is the closest conceptual parallel to my state-conditioned output restriction — but it operates on resource feasibility rather than classified environmental safety state, and it modifies *which patients get resources* rather than *what types of recommendations AI may generate*. The absence of formal safety state classification, AI participation governance, and state-conditioned output restriction in this purpose-built system reinforces the gap my architecture addresses: even domain-specific hybrid AI systems designed for safety-critical, low-resource contexts do not implement graduated, state-conditioned governance over AI output scope. The paper's cognitive heuristic elicitation methodology and HITL override rationale capture are additionally relevant to my socio-technical evaluation design.

---

## 17. Overall Relevance Score

### ⭐⭐⭐ Medium

**Justification:** This paper addresses four of my research themes (hybrid AI, safety-critical decision-making, low-resource environments, human role) and provides useful context as a domain-adjacent system design for safety-critical AI decision support in resource-constrained settings. Its strongest value is as **gap evidence in a parallel domain**: a purpose-built hybrid AI system for safety-critical, resource-constrained operations that nonetheless lacks environmental safety state classification, AI participation governance, state-conditioned output restriction, and formal safety properties. The resource-aware optimization approach offers a useful conceptual contrast to my state-conditioned governance. However, it is in a different domain (healthcare, not maritime/fisheries), does not implement any form of governance pair, and its formalisation is module-level rather than pipeline-level. It is **background/gap evidence**, not an architectural antecedent or baseline comparator.
