# Literature Review Extraction: Ramos et al. (2024)

## 1. Paper Identity

- **Title:** Collaborative Intelligence for Safety-Critical Industries: A Literature Review
- **Authors:** Inês F. Ramos, Gabriele Gianini, Maria Chiara Leva, Ernesto Damiani
- **Year:** 2024
- **Venue:** Information (MDPI), Vol. 15, Issue 11, Article 728
- **DOI:** https://doi.org/10.3390/info15110728
- **Type:** Systematic literature review (91 articles, 2014–2023)

---

## 2. Core Contribution

- **Problem addressed:** While AI-driven automation improves performance and safety, humans should not be replaced in safety-critical systems but integrated to collaborate and mitigate each other's limitations. However, no unified overview exists of how AI methods are applied across the diverse landscape of collaborative intelligence (CI) for safety-critical industries.
- **Proposed solution:** A systematic review of 91 articles employing AI methods for collaborative intelligence in safety-critical industries, organised by a domain-focused taxonomy based on: (1) the type of collaborative interaction (machine assists human or human assists machine), (2) the AI paradigm used, and (3) the AI problem domain.
- **Main contributions:** (1) A taxonomy of CI interaction types and task categories (Figure 1); (2) identification of 11 CI task sub-categories across two interaction types; (3) analysis of trends, gaps, and techniques across 91 papers; (4) safety recommendations for CI practitioners (Figure 7); (5) mapping of CI research to safety-critical industry domains (manufacturing, automotive, aviation, maritime, nuclear, rail).
- **Novelty:** The paper unifies previously disparate research threads (human–robot collaboration, human-in-the-loop learning, shared control, safety monitoring) under a single CI framework with safety as the organising lens. The taxonomy bridges robotic, HCI, AI, and safety engineering perspectives.

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | Partial | Reviews neuro-symbolic approaches, hybrid models combining multiple AI paradigms (e.g., fuzzy controllers + neural networks, probabilistic models + logic-based supervisors). Discusses the general AI paradigm taxonomy but not hybrid AI in the specific sense of deterministic safety gates controlling probabilistic AI. |
| Safety-critical AI decision-making | Yes | Core focus. Covers AI applications across safety-critical industries (automotive, aviation, maritime, nuclear, rail, manufacturing). Discusses safety assessment, accident prediction, human state recognition for safety, and CI safety monitoring. |
| AI governance / control mechanisms | Partial | Reviews shared control strategies (blending human and autonomous control based on disagreement/risk), supervisor synthesis using POMDP/PCTL for formal safety compliance, and dynamic safety zones. These represent forms of AI participation governance, though none implement state-conditioned two-level governance. |
| Low-resource environments | No | Not addressed. All reviewed applications assume industrial or high-resource deployment contexts. |
| Decision architecture formalisation | Partial | Some reviewed papers use formal models — POMDP for modelling human/vehicle state, PCTL for specification of safety properties, deterministic finite automata for supervisor controllers, Bayesian frameworks for prediction uncertainty. However, no unified decision architecture is proposed or reviewed. |
| Human role in decision-making | Yes | Core focus. The entire review is structured around human–machine collaboration: machine assists human-in-the-loop (safety monitoring, intention prediction, state recognition) and human assists machine (demonstrations, safe RL training, deployment oversight). |
| Socio-technical evaluation | Partial | Discusses trust, explainability, regulatory compliance (EU AI Act, Machinery Regulation 2023/1230), worker autonomy, cognitive ergonomics, and privacy. Recommends human-centred CI system design. However, no socio-technical evaluation methodology is applied. |
| Coastal fisheries / maritime domain | Partial | One reviewed paper (Zhang & Furusho 2016) uses a Bayesian network for risk and accident prediction in ship navigation. Maritime is listed as an application domain but receives minimal coverage. |

**Mid-Extraction Relevance Gate:** 2 Yes + 4 Partial → **REDUCED EXTRACTION** (Sections 4–7 and 12–13 only; Sections 8–11 and 14–15 skipped).

---

## 4. Decision Architecture Analysis

- **Architecture:** The paper does not propose a decision architecture. It reviews diverse CI solutions, each addressing a specific component of human–machine collaboration (perception, planning, control). The taxonomy organises these by interaction type and task category rather than as an integrated architecture.
- **Layered architecture / governance structure:** The paper's taxonomy implicitly identifies *layers* of CI functionality — perception (human/object detection, state recognition), reasoning (intention prediction, mental model estimation), control (robot control, shared control), and planning (motion planning, task scheduling) — but does not integrate these into a governance architecture controlling AI participation.
- **Rule-based constraints before AI:** Several reviewed papers implement safety constraints:
  - Supervisor synthesis using PCTL specifications and L* learning to ensure safety compliance in human–robot collaboration (Zhang et al. 2016; Wu et al. 2021).
  - Dynamic safety zones with constrained optimisation for robot stop trajectories (Scalera et al. 2022).
  - Fuzzy inference systems mapping risk levels (high/medium/low) to robot speed scaling (Costanzo et al. 2021).
  - These represent forms of deterministic safety constraints applied *alongside* or *after* AI, but none implement a pre-AI safety gate conditioned on classified environmental state.
- **Boundary between deterministic control and AI reasoning:** The shared control literature reviewed (Oh et al. 2021; Li et al. 2022) explicitly addresses blending autonomous AI control with human control, with mechanisms to shift control authority based on disagreement or risk. This is the closest concept to a governance boundary, though it operates at the human–AI interface rather than at an environmental safety state level.
- **Failure modes / fallback behaviour:** Discussed extensively:
  - Human intervention for safe RL training (Saunders et al. 2018) — blocking unsafe agent actions and substituting safe ones.
  - Confidence/uncertainty estimation for AI outputs (Fisac et al. 2018; Fridovich-Keil et al. 2020) — Bayesian framework for prediction confidence as a hidden state.
  - Simplex architecture for path planning (Ionescu 2021) — switching from neural network to deterministic baseline when safety is at risk.
  - Digital twins for safe learning before real-world deployment.

**Summary:** No unified decision architecture exists across the reviewed literature. The paper documents a fragmented landscape where individual CI components implement their own safety mechanisms (supervisor controllers, dynamic safety zones, shared control arbitration, confidence estimation) without integration into a state-conditioned governance framework.

---

## 5. Formal Model and Mathematical Representation

- **Formal models reviewed:**
  - **POMDP** — used to model human as partially observable agent (hidden intents) in human–robot collaboration (Zhang et al. 2016; Wu et al. 2021).
  - **PCTL (Probabilistic Computation Tree Logic)** — used to specify safety requirements for supervisor synthesis; a deterministic supervisor satisfying PCTL specifications is learned via L* algorithm.
  - **Deterministic Finite Automata** — used to model the supervisor controller of the robot.
  - **Hidden Markov Models** — used extensively for human intention/behaviour modelling and mental model estimation.
  - **Bayesian frameworks** — used for prediction uncertainty reasoning (updating belief over model confidence).
- **Comparison to E → S = f(E) → (G(S), A_AI(S)) → AI(E):** No reviewed paper implements a comparable pipeline. The supervisor synthesis work (Zhang et al. 2016; Wu et al. 2021) comes closest — it models the human and robot as state variables, defines safety specifications in PCTL, and synthesises a supervisor that ensures compliance — but the supervisor operates on task completion constraints, not on classified environmental safety state. There is no safety state classification function S = f(E), no three-mode governance, and no state-conditioned restriction of AI output types.
- **State-dependent recommendation restriction:** Not present in any reviewed paper. The fuzzy risk classification (Costanzo et al. 2021) maps sensor data to three risk levels (high/medium/low) controlling robot speed — this is functionally analogous to a simple safety state classification affecting AI behaviour, but operates only on a single output dimension (speed) and lacks the two-level governance structure.
- **Safety Dominance Property:** Not defined. The PCTL-based supervisor synthesis guarantees formal safety compliance, which is conceptually related — ensuring the supervised system satisfies safety specifications — but is formulated as task-completion probability constraints, not as a dominance property over AI output space.

---

## 6. Safety State Classification

- **Discrete risk/safety levels:** One reviewed paper explicitly classifies risk into discrete levels: Costanzo et al. (2021) maps sensor inputs to three fuzzy risk levels (high, medium, low) for robot speed control. The Bayesian confidence framework (Fisac et al. 2018) implicitly creates a binary classification (confident/uncertain) of AI prediction reliability.
- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:** The fuzzy three-level risk classification (high/medium/low) is structurally similar to my tripartite classification, but: (1) it is applied to a single control variable (robot speed), not to the AI's overall recommendation scope; (2) it is not formalised as a function of an environmental state vector; (3) it does not produce a state-conditioned governance pair (G(S), A_AI(S)).
- **AI recommendation scope differentiation across safety levels:** Not present. Risk level affects a single behaviour parameter (speed, stop trajectory) rather than restricting the *types* of recommendations AI may generate. No paper implements the concept that at intermediate risk, AI should still participate but with a restricted output space.

---

## 7. Governance Level Analysis

| Level | Question | Implemented? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (G(S)) | Partial | Several mechanisms effectively block or constrain AI: human intervention blocking unsafe RL actions (Saunders et al. 2018), simplex architecture switching from NN to deterministic baseline (Ionescu 2021), shared control shifting authority to human in high-disagreement/high-risk scenarios (Oh et al. 2021). These are functionally Level 1, but triggered by task-specific conditions, not classified environmental safety state. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | No | No reviewed paper restricts the *types* of AI recommendations based on conditions. AI outputs are either fully generated or fully blocked/overridden — the binary paradigm. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | No | Not present in any reviewed work. |

- **Governance type:** The reviewed literature implements various forms of Level 1 governance (participation control) through supervisor controllers, shared control arbitration, human intervention, and simplex switching. All are **binary** — AI either operates or is overridden/blocked. None implement graduated governance where AI participates with restricted output scope.
- **Binary switch vs. graduated model:** Binary across all reviewed papers. The fuzzy three-level risk classification (Costanzo et al. 2021) modulates a *continuous* parameter (speed) rather than implementing graduated governance over discrete recommendation types.
- **Support for two-level governance pair:** The review strongly supports the *motivation* for my two-level governance model — the reviewed literature documents extensive work on Level 1 governance but a complete absence of Level 2 (output-scope governance conditioned on safety state). This confirms the gap.

---

## 12. Key Concepts and Definitions

| Term / Concept | Definition / Relevance |
|---|---|
| **Collaborative Intelligence (CI)** | Human and machine intelligence are interdependent and interact to achieve a goal — two main types: machine assists human-in-the-loop, or human assists machine. Relevant as the broader paradigm within which my architecture operates. |
| **Shared control** | Blending autonomous system control with human operator control, with mechanisms to shift authority based on disagreement, risk, or confidence. Relevant as a form of participation governance, though operating at the human–AI interface rather than environmental safety state level. |
| **Supervisor synthesis (POMDP + PCTL)** | Formal method for synthesising a deterministic supervisor controller that ensures safety specifications (expressed in PCTL) are satisfied, modelling the human as a POMDP (hidden intents). Relevant as a formal safety verification approach, though applied to task completion rather than environmental safety state governance. |
| **Simplex architecture** | Safety assurance pattern: use neural network for performance, switch to deterministic baseline algorithm when safety is at risk. Relevant as a binary Level 1 governance mechanism. |
| **Dynamic safety zones** | Online-optimised bounding volumes around robot and human, with minimised stop trajectories. Represents spatial safety governance in physical collaboration. |
| **Human Intervention RL (HIRL)** | Human blocks unsafe RL agent actions during training, substituting safe alternatives. A CNN learns to imitate the human's intervention decisions. Relevant as a form of human-mediated participation governance during learning. |
| **Bayesian prediction confidence** | Bayesian belief updated over model prediction confidence (modelled as HMM hidden state) — when predictions are assigned low probability, confidence drops. Relevant as an uncertainty quantification mechanism that could inform safety state classification. |
| **EU AI Act / Machinery Regulation 2023/1230** | Regulatory frameworks requiring human agency and oversight for high-risk AI systems, communication of planned actions to operators, and safety throughout the lifecycle. Relevant as the regulatory context motivating my governance architecture. |

---

## 13. Limitations and Unsolved Problems

- **Stated limitations:**
  - The review captures only a sample of the extensive CI literature; "collaborative intelligence" is still an emerging concept.
  - Most reviewed solutions address a single component of a complex system; integration across components is rarely addressed.
  - Evaluation/validation is mostly in simulated environments or lab settings; real-world deployment validation is rare.
  - Quality and representativeness of training/testing data are rarely assessed.
  - No general guidelines exist with comprehensive, paradigm-agnostic metrics for ensuring CI system reliability and dependability before open-world deployment.

- **Unsolved problems acknowledged:**
  - True proactive collaboration involving purposeful interactions, adaptation to context, and mutual understanding remains far from achieved.
  - Explainability of AI actions in shared control scenarios is rarely addressed.
  - Multi-human, multi-agent collaboration scenarios are unexplored.
  - Human state recognition models lack generalisation across tasks and subjects.
  - Safety certification of CI systems integrating probabilistic AI and uncertain human behaviour remains a fundamental challenge.

- **Gaps aligning with my research:**
  - **Binary governance gap:** Across 91 reviewed papers, all safety governance mechanisms are binary — AI operates or is blocked/overridden. No paper implements graduated governance where AI participates with restricted recommendation scope under intermediate risk. This directly confirms the CAUTION mode gap my architecture addresses.
  - **No state-conditioned output restriction:** No reviewed paper restricts AI output *types* based on classified safety state. Risk modulates continuous parameters (speed, safety zone size) but never the *set of permissible recommendation types*. My A_AI(S) concept has no precedent in this literature.
  - **No unified governance architecture:** Safety mechanisms are implemented component-by-component (supervisor for this task, fuzzy controller for that parameter, shared control for this interface). No paper integrates these into a unified, formal governance pair conditioned on environmental state. My (G(S), A_AI(S)) pair fills this integration gap.
  - **Absence of Safety Dominance Property:** While PCTL-based supervisor synthesis guarantees formal safety compliance for specific task specifications, no paper defines a general property ensuring that AI outputs always fall within state-determined bounds across a graduated governance model.

---

## 16. Relation to My Research and Positioning

- **Governance level implemented:** Level 1 (participation governance) is well-represented across multiple mechanisms (supervisor controllers, shared control, human intervention, simplex switching). Level 2 (output-scope governance) is absent. No unified, state-conditioned governance pair exists.
- **State-conditioned governance:** Not present. Safety mechanisms are triggered by task-specific conditions (collision risk, human disagreement, prediction confidence), not by classified environmental safety state.
- **Proximity to (G(S), A_AI(S)):** Moderate — the components are present in isolation (risk classification, participation control, formal safety specifications) but never integrated into a two-level, state-conditioned governance pair.
- **Safety Dominance Property:** Not defined, though PCTL-based supervisor synthesis is a related formal safety guarantee.
- **Gap my research addresses:** The review documents the full landscape of Level 1 governance for safety-critical human–AI collaboration, confirming that Level 2 governance (state-conditioned restriction of AI recommendation types) is entirely absent. My architecture fills this gap.

**Positioning paragraph:** Ramos et al. (2024) provides **background on safety-critical human–AI collaboration and gap evidence** for my research. As a comprehensive review of 91 papers on collaborative intelligence for safety-critical industries, it documents the state of the art in how AI participation is governed during human–machine collaboration — and reveals that this governance is universally binary. Supervisor controllers, shared control arbitration, human intervention during RL training, simplex architectures, and dynamic safety zones all implement forms of Level 1 governance (whether AI participates), but none restrict the *types* of AI outputs based on classified safety state. The review's fuzzy three-level risk classification (high/medium/low) for robot speed control is structurally closest to my tripartite safety state model, but operates on a single continuous parameter rather than governing a discrete recommendation space. The paper is citable as: (1) evidence that binary governance is the universal paradigm across safety-critical CI research, confirming the CAUTION mode gap; (2) background on the regulatory landscape (EU AI Act, Machinery Regulation) motivating governance architectures; and (3) a taxonomy of human–AI collaboration types relevant to positioning my architecture's human role.

---

## 17. Overall Relevance Score

### ⭐⭐⭐ Medium

**Justification:** This review provides useful background across two major themes of my research — safety-critical AI decision-making and human role in AI-assisted decision-making — and offers indirect gap evidence by documenting the universal binary governance paradigm across 91 CI papers. The fuzzy three-level risk classification, supervisor synthesis with PCTL, shared control arbitration, and simplex architecture are all relevant comparison points. However, the paper does not address decision architecture formalisation, low-resource environments, or fisheries/maritime contexts in depth, and it reviews rather than proposes solutions. Citable in the safety-critical AI background section, the governance gap analysis, the human role discussion, and the regulatory motivation — but not in the core architecture or formalisation chapters.
