## Literature Review Extraction: Leppinen et al. (2026)

---

### 1. Paper Identity

- **Full title:** A stage-gate decision process for guiding the development of AI solutions for preventive maintenance
- **Authors:** Jussi Leppinen, Ahti Salo, Michele Compare
- **Year:** 2026 (available online 8 December 2025)
- **Venue:** EURO Journal on Decision Processes, 14, 100063
- **Type:** Conceptual framework with illustrative case study (train toilet door system PHM task)

---

### 2. Core Contribution

- **Problem:** Developing AI solutions for Prognostics and Health Management (PHM) is risky and resource-demanding. Multiple candidate AI algorithms exist whose performance is initially uncertain. No prior structured decision-making framework accommodated both technical and organisational criteria in the early development phases of AI-based PHM solutions.
- **Solution:** A four-stage, three-gate development process that screens increasingly detailed AI candidate solutions using Robust Portfolio Modelling (RPM). The stages progress from use case specification → exploratory testing → implementation plan formulation → execution. At each decision gate, candidates are evaluated against six development objectives operationalised via 17 criteria spanning cost, time, performance, capabilities, economic benefits, and reputation.
- **Main contributions:**
  1. A structured stage-gate process specifically designed for AI solution development in PHM contexts.
  2. Integration of RPM to handle incomplete preference and score information, identifying non-dominated portfolios of candidates under budget and schedule constraints.
  3. A multi-criteria evaluation framework (6 objectives, 17 criteria) that spans technical performance, economic benefits, organisational capabilities, and reputation.
  4. An illustrative case study demonstrating the process on a train toilet door system.
- **Novelty:** The combination of stage-gate methodology (from new product development) with RPM for AI algorithm selection under uncertainty. The framework explicitly manages multiple candidates in parallel to mitigate premature fixation risk, and handles incomplete information via score intervals and weight ranges rather than requiring precise numerical inputs.

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | No | The paper considers different AI algorithm types (Table 1) but does not combine rule-based and probabilistic reasoning within a single architecture. It is about *selecting between* AI approaches, not *integrating* them. |
| Safety-critical AI decision-making | Partial | The case study domain (train toilet door) is explicitly stated as *not* safety-critical. However, the framework addresses structured decision-making under uncertainty for AI deployment, and the stage-gate methodology includes go/no-go gates that function as risk-management checkpoints. |
| AI governance / control mechanisms | Partial | The decision gates function as governance checkpoints controlling whether a candidate AI solution proceeds to the next stage (go/no-go). This is a *development-process-level* governance mechanism, not a *runtime* governance mechanism. The gates control the *development lifecycle* of AI, not the *operational behaviour* of deployed AI. |
| Low-resource environments | Partial | The framework acknowledges resource constraints (budget, time, personnel, computational feasibility) and explicitly models them as feasibility constraints in the RPM. Computational feasibility is a "must-meet" criterion in the case study. However, the paper does not address deployment in low-resource operational environments (limited connectivity, low literacy, etc.). |
| Decision architecture formalisation | Partial | The paper formalises the portfolio selection process mathematically (RPM with score intervals, weight sets, dominance conditions). However, this formalisation is about *development portfolio optimisation*, not about *runtime decision architecture* (no equivalent of E → S → G(S) → A_AI(S)). |
| Human role in decision-making | Partial | Humans (steering groups, domain experts) are central to the decision gates — they elicit preferences, provide expert judgements, and make final go/no-go decisions. The framework is explicitly positioned as decision support, not automation. However, this pertains to the *development process*, not to the *end-user interaction* with a deployed AI system. |
| Socio-technical evaluation | Partial | The criteria framework includes socio-technical dimensions: organisational readiness, management support, learning, reputation, explainability, trust. The literature review surveys technology acceptance models (TAM, TOE). However, no socio-technical evaluation of a *deployed* system is conducted. |
| Coastal fisheries / maritime domain | No | Domain is preventive maintenance for rail systems. No connection to fisheries or maritime operations. |

**Mid-Extraction Relevance Gate:** 0 Yes, 6 Partial → **REDUCED EXTRACTION.** Complete Sections 4–7 and 12–13 only. Skip Sections 8–11 and 14–15.

---

### 4. Decision Architecture Analysis

- **Structure:** Sequential stage-gate pipeline with four development stages and three decision gates. Candidates proceed linearly from Stage 1 (use case specification) through to Stage 4 (execution), with go/no-go decisions at each gate. Failed candidates may be terminated or redirected to an earlier stage.
- **Layered architecture:** The process is layered in the sense that each stage produces increasingly refined deliverables (use case → proof of concept → implementation plan → AI solution), and each gate applies progressively more criteria as evidence accumulates. However, this layering governs the *development lifecycle*, not *runtime AI behaviour*.
- **Rule-based constraints before AI decisions:** "Must-meet" criteria function as hard constraints that eliminate candidates regardless of their scores on other criteria (e.g., computational feasibility < threshold → terminate). This is analogous to a pre-filter, but it operates on candidate *selection*, not on candidate *output*.
- **Boundary between deterministic control and AI reasoning:** Not applicable in the runtime sense. The framework is about deciding *which* AI algorithm to develop, not about controlling *what* a deployed AI system does.
- **Failure modes and fallback:** The framework includes fallback mechanisms: candidates can be reverted to earlier stages, previously terminated use cases can be re-examined if no attractive proof of concept emerges, and new AI algorithms can be introduced at any point if promising ones become available.

**Key distinction from my architecture:** This paper's "gates" operate at the *meta-level* of AI development (deciding which AI to build), not at the *operational level* of AI deployment (deciding what AI may do in a given environmental state). The gate function here is G(development_evidence) → {go, no-go}, not G(S) → {0, 1} conditioned on environmental safety state.

---

### 5. Formal Model and Mathematical Representation

- **Formal model:** Yes. The paper defines a formal RPM framework:
  - Candidates: X = {x¹, …, xᵐ}
  - Criteria evaluations: xⁱⱼ mapped to normalised scores vⁱⱼ ∈ [0, 1] via criterion-specific value functions
  - Score intervals: [v̲ⁱⱼ, v̄ⁱⱼ] to capture uncertainty
  - Criteria weights: wᵒᵢ ∈ Sₒ (feasible weight sets modelling incomplete preferences)
  - Objective weights: wₒ ∈ Oᵤ
  - Portfolio value: V(p, v, wc, w) = z(p)ᵀ v·wc·w
  - Dominance condition: portfolio p dominates p′ iff the minimum value difference ≥ 0 and maximum > 0 across all feasible parameter combinations
  - Feasibility constraints: Az(p) ≤ B (budget and schedule)

- **Comparison to my pipeline E → S = f(E) → (G(S), A_AI(S)) → AI(E):**
  - **No equivalent of E (environmental state vector).** The inputs here are development evidence (expert evaluations, test results), not real-time environmental conditions.
  - **No equivalent of S = f(E) (safety state classification).** There is no classification of operational conditions into discrete safety levels.
  - **Partial analogue to G(S) (gate function).** The decision gates produce go/no-go decisions for each candidate, but these are conditioned on multi-criteria evaluation of development evidence, not on classified environmental state.
  - **No equivalent of A_AI(S) (state-conditioned admissible action space).** There is no concept of restricting what a deployed AI may *recommend* based on operational conditions. The "restriction" here is about which candidates *survive* the development pipeline.

- **State-dependent recommendation restriction:** No. The framework does not model any form of output-scope restriction on deployed AI. A candidate either proceeds or is terminated — there is no intermediate mode where a candidate "proceeds with restricted scope."
- **Safety Dominance Property:** No equivalent. There is no formal guarantee that AI outputs fall within state-determined bounds. The dominance concept here is *portfolio dominance* (one portfolio of candidates dominates another across all feasible parameter values), which is a completely different mathematical structure.
- **Formalisation purpose:** The formalisation is operational — it directly drives the RPM computation to identify non-dominated portfolios. It is used for analysis and decision recommendation, not purely descriptive.

---

### 6. Safety State Classification

- **Discrete risk/safety levels:** No. The paper does not classify operational or environmental conditions into safety levels. The "must-meet" / "should-meet" distinction for criteria is the closest analogue, but this is a *criterion classification*, not an *environmental state classification*.
- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:** No parallel. The framework has no concept of mapping environmental inputs to discrete safety states that then govern AI behaviour.
- **Differentiated AI recommendation scope across safety levels:** No. There is no concept analogous to CAUTION mode where AI still participates but with restricted output types. The gates produce binary outcomes for each candidate: go or no-go. A candidate that passes the gate proceeds with full scope — there is no "proceed with restricted advisory scope" option.

---

### 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (equivalent to G(S)) | Partial | Decision gates produce go/no-go decisions for each candidate AI algorithm, controlling whether it proceeds to the next development stage. However, this governs *development continuation*, not *runtime participation*. Once deployed, the AI solution operates without the gate framework. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (equivalent to A_AI(S)) | No | No mechanism restricts *what* a deployed AI solution may recommend based on operational state. The framework addresses *which* AI to develop, not *what scope of output* a deployed AI may produce. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | No | Neither level is conditioned on environmental state. The gates are conditioned on accumulated development evidence and multi-criteria evaluation. |

- **Binary AI switch or graduated governance?** Binary at each gate (go/no-go per candidate), though the portfolio-level analysis allows multiple candidates to proceed simultaneously. There is no graduated governance in the runtime sense.
- **Level 2 governance:** Not implemented. No state-conditioned output-scope restriction exists.
- **Support or contradiction for (G(S), A_AI(S))?** Neither supports nor contradicts. The paper operates at a fundamentally different level of abstraction — governing *AI development* rather than *AI runtime behaviour*. The stage-gate concept is structurally interesting as an analogy (sequential checkpoints with go/no-go decisions), but the architectural function is distinct from environmental-state-conditioned runtime governance.

---

### 12. Key Concepts and Definitions

- **Stage-gate process:** A structured development pipeline with sequential stages producing deliverables of increasing detail, separated by decision gates where go/no-go decisions are made.
- **Robust Portfolio Modelling (RPM):** A decision-analytic method that identifies non-dominated portfolios of alternatives under incomplete preference and score information, subject to resource constraints.
- **Core candidate / Exterior candidate:** A candidate included in all non-dominated portfolios (should proceed) vs. included in none (should be terminated).
- **"Must-meet" vs. "should-meet" criteria:** Hard feasibility constraints vs. desirable features that inform preference rankings. Must-meet failure → immediate termination.
- **Use case (in PHM context):** A combination of a PHM task, a data resource, and an AI algorithm — the unit of evaluation in the framework.
- **Score intervals:** Evaluations expressed as ranges [v̲, v̄] to capture uncertainty and incomplete information, which narrow as evidence accumulates.
- **Non-dominated portfolio:** A feasible portfolio such that no other feasible portfolio has higher aggregate value for all feasible parameter combinations.

---

### 13. Limitations and Unsolved Problems

**Stated limitations:**
1. The evaluation framework assumes objectives and criteria can be agreed on and operationalised in advance, which may be challenging under high uncertainty or for intangible societal/ethical impacts.
2. High uncertainty may make it hard to elicit well-founded judgements, and evaluators may provide inconsistent evaluations across candidates.
3. The additive value function structure may oversimplify situations with synergies between criteria.
4. The framework presumes sufficient organisational resources to apply it — smaller companies or tight timescales may lack these.
5. The framework does not guarantee eventual implementation success, which depends on external factors like data compatibility.

**Unsolved problems / future work:**
- The paper does not address how the deployed AI solution should be *governed at runtime* — only how to select which AI to deploy.
- No consideration of how the AI solution should behave under varying operational conditions once deployed.
- The illustrative case study is explicitly non-safety-critical (toilet door); adaptation to genuinely safety-critical domains is not demonstrated.

**Alignment with my research gaps:**
- The paper has **no concept of runtime two-level governance** separating participation (G(S)) from advisory scope (A_AI(S)).
- There is **no CAUTION mode** where a deployed AI operates under restricted recommendation scope.
- There is **no Safety Dominance Property** or any formal guarantee about what a deployed AI may output under varying conditions.
- The gap is structural: this framework governs *which AI to build*, whereas my architecture governs *how a built AI behaves* under classified environmental states. The two are complementary but non-overlapping in their governance scope.

---

### 16. Relation to My Research and Positioning

- **Level 1 governance (participation control):** Partial — at the development-process level only (go/no-go at gates), not at runtime.
- **Level 2 governance (output-scope control):** Not implemented. No restriction on what a deployed AI may recommend.
- **State-conditioned?** No. Gates are conditioned on development evidence, not environmental state.
- **Two-level governance pair (G(S), A_AI(S))?** Falls far short. The paper operates at a fundamentally different abstraction level — AI development lifecycle governance rather than AI runtime operational governance.
- **Safety Dominance Property?** No equivalent. Portfolio dominance is a different mathematical concept.
- **Gap my research addresses:** This paper provides a rigorous framework for deciding *which* AI solution to develop but offers no mechanism for governing *what that AI does once deployed*. My architecture fills the post-deployment governance gap: once an AI solution is selected and implemented, the two-level governance pair (G(S), A_AI(S)) governs its runtime participation and advisory scope based on classified environmental safety state. The stage-gate framework terminates at deployment — my architecture begins there.

**Positioning paragraph:** Leppinen et al. (2026) provides a structured decision framework for the AI development lifecycle, contributing to the broader background on how organisations manage the selection of AI solutions under uncertainty. Its stage-gate concept offers a useful structural analogy to the gate function G(S) in my architecture — both implement sequential checkpoints with go/no-go decisions — but the two operate at fundamentally different levels: Leppinen's gates govern development-stage transitions conditioned on accumulated evidence, while my gate governs runtime AI participation conditioned on classified environmental state. The paper reinforces the observation that existing gate-like mechanisms are universally binary (go/no-go) and do not implement a graduated mode where AI proceeds with restricted scope. The "must-meet"/"should-meet" criteria distinction is a hard/soft binary, not a three-level graduated model. This paper is best positioned as **background motivation** — demonstrating that structured governance of AI is an active concern in decision science, while highlighting that current frameworks stop at the development lifecycle boundary and leave runtime operational governance unaddressed.

---

### 17. Overall Relevance Score

**⭐⭐ Low**

**Justification:** The paper addresses AI decision-making in a structured, formal manner and introduces a stage-gate governance concept with go/no-go decisions. However, it operates at the AI development lifecycle level, not at the runtime operational level that is the focus of my research. It does not address safety-critical operational environments, does not classify environmental states, does not implement runtime AI governance, and does not define any formal property analogous to the Safety Dominance Property. The domain (preventive maintenance for rail toilet doors) is neither safety-critical nor related to fisheries/maritime operations. The paper is tangentially useful as background on structured AI governance and as evidence that existing governance frameworks are binary (go/no-go) and stop at the development boundary — reinforcing the gap my architecture addresses. It would merit at most a brief citation in a background section on AI governance frameworks, noting that even sophisticated development-lifecycle governance models lack runtime operational governance mechanisms.
