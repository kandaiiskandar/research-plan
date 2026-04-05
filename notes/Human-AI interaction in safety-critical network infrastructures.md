# Literature Review Extraction
## Paper: Human-AI Interaction in Safety-Critical Network Infrastructures

---

## 1. Paper Identity

- **Full title:** Human-AI Interaction in Safety-Critical Network Infrastructures
- **Authors:** Marco Mussi, Alberto Maria Metelli, Marcello Restelli, Gianvito Losapio, Ricardo J. Bessa, Daniel Boos, Clark Borst, Giulia Leto, Alberto Castagna, Ricardo Chavarriaga, + 21 additional co-authors
- **Year:** 2025 (published September 19, 2025)
- **Venue:** *iScience*, 28, 113400. DOI: 10.1016/j.isci.2025.113400 (Cell Press, open access)
- **Type of paper:** Perspective article (multi-domain, multi-stakeholder; interdisciplinary; industry-informed through workshops with operators from RTE, TenneT, Deutsche Bahn, SBB, NAV Portugal)

---

## 2. Core Contribution

- **Main problem:** AI is increasingly integrated into safety-critical network infrastructures (power grids, railway networks, air traffic management), but current AI systems are not designed to optimise the overall efficiency of socio-technical systems or to maximise human performance and engagement. The human-AI interaction challenge — defining roles, maintaining trust, ensuring transparency, and preserving human skills under increasing automation — remains inadequately addressed.
- **Proposed solution:** An interdisciplinary perspective that merges computer science, decision-making sciences, psychological constructs, and industrial practices. The paper identifies seven common decision-making characteristics across three safety-critical domains, proposes three AI architecture patterns (distributed, hierarchical, knowledge-assisted), and articulates six research theses for effective human-AI collaboration. It advocates for the Joint Control Framework (JCF) and Ecological Interface Design (EID) as complementary frameworks for designing human-AI interaction.
- **Main contributions:**
  - Cross-domain analysis identifying seven shared decision-making characteristics: human-AI interaction, multiple operators/stakeholders, action types (preventive/corrective), action space complexity, network capacity and external events, time resolution, and trade-off analysis on conflicting objectives
  - Three AI architecture patterns promoting transparency: distributed decision-making, hierarchical decision-making, and knowledge-assisted AI
  - Six research theses: function allocation, cognitive transparency and explainability, cognitive systems engineering for human-AI design, safety in AI agent design, human-AI co-learning, and human-AI collaboration under increasing autonomy
  - The CAB (Cockpit and Bidirectional Assistant) prototype for experimenting with bidirectional human-AI virtual assistants
  - Application of ALTAI (Assessment List for Trustworthy AI) to safety-critical use cases
- **What is novel:** The cross-domain synthesis across power, rail, and air traffic, identifying shared decision-making structures. The integration of JCF and EID as complementary design frameworks. The concept of the human as "director" rather than passive supervisor under increasing automation. The emphasis on AI supporting human *cognitive processes* (situation awareness, learning, motivation) rather than just providing recommendations.

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | **Yes** | Knowledge-assisted AI explicitly combines domain knowledge/rules with data-driven ML. Neuro-symbolic methods discussed. Safety constraints integrated into AI models as a foundation for ML-based improvements. |
| Safety-critical AI decision-making | **Yes** | Central focus. Three safety-critical domains analysed: power grids, railway networks, air traffic management. Real-time decision-making under uncertainty, time pressure, and cascading failure risk. |
| AI governance / control mechanisms | **Yes** | Discusses levels of automation from fully manual to fully autonomous, function allocation between humans and AI, "Meaningful Human Control" framework, HITL as essential for preventing critical failures, EU AI Act compliance. |
| Low-resource environments | No | All three domains involve well-resourced, high-tech infrastructure (control rooms, satellite data, simulation environments). |
| Decision architecture formalisation | **Partial** | Conceptual framework with distributed and hierarchical structures (Figure 2), common decision-making schematic (Figure 1), and human cognition model (Figure 3). But no mathematical formalisation — no state variables, gate functions, or action space definitions. |
| Human role in decision-making | **Yes** | Extensive treatment: situation awareness, mental models, trust calibration (undertrust/overtrust), intrinsic motivation, co-learning, cognitive load management, human as "director" role. |
| Socio-technical evaluation | **Partial** | References socio-technical systems theory; applies ALTAI trustworthiness assessment; discusses cognitive systems engineering (CSE). No formal evaluation framework or empirical evaluation. |
| Coastal fisheries / maritime domain | No | Domains are power grids, railways, air traffic. |

**Mid-Extraction Relevance Gate:** 4 Yes + 2 Partial → **FULL EXTRACTION**

---

## 4. Decision Architecture Analysis

- **Decision-making structure:** The paper identifies a common decision-making structure across all three domains (Figure 1A): network capacity constraints (identified via observations and forecasts, influenced by uncertainty and external factors) → multiple operators across different time horizons → trade-offs between multiple objectives under time constraints → preventive or corrective actions from a large action space. This is iterative, with exploration and validation loops between human operators and AI (Figure 1B).
- **Layered architecture / governance structure:** Yes — the paper proposes three architectural patterns:
  - **Distributed:** Multiple AI agents each handling a portion of the system, communicating via message passing, producing a joint action (Figure 2A)
  - **Hierarchical:** High-level agent overseeing subtasks handled by lower-level agents (Figure 2B) — maps high-level goals to sequences of low-level actions
  - **Knowledge-assisted:** Combines domain knowledge/rules with data-driven ML, integrating human-devised safety constraints as a foundation
- **Rule-based constraints or safety checks:** Yes — knowledge-assisted AI explicitly integrates human-devised safety constraints into AI models, providing "a foundation of reliability upon which learning-based improvements can build." In railway systems, signalisation is independent of the human-AI decision-making system, ensuring no safety-critical situations can occur from rescheduling decisions.
- **Boundary between deterministic control and AI reasoning:** Partially defined conceptually but not formally. The paper advocates for knowledge-assisted approaches where domain rules constrain ML, and for hierarchical structures where high-level goals decompose into constrained low-level actions. However, there is no formal specification of where deterministic rules end and probabilistic reasoning begins.
- **Failure modes / fallback behaviour:** Yes — ALTAI assessment requires fault tolerance, fallback mechanisms, clear operator notifications, and ability to revert to manual control. The paper states HITL design is "essential to prevent critical failures, ensuring that final decisions remain under human supervision."

**Key parallel to my research:** The common decision-making schematic (Figure 1A) shares structural similarities with my pipeline — observations/forecasts of network state (analogous to E), constraints and uncertainty, multiple objectives, and action selection from a large space. However, the paper does not formalise this into a pipeline with explicit state classification, gate functions, or admissible action spaces.

---

## 5. Formal Model and Mathematical Representation

- **Formal model:** None in the mathematical sense. The paper presents conceptual schematics (Figures 1-3) and verbal descriptions of decision-making structures. No equations, state variables, or formal specifications.
- **Comparison to E → S = f(E) → (G(S), A_AI(S)) → AI(E):** The conceptual structure has parallels: observations and forecasts of network state (≈ E), network capacity constraints that determine operational conditions (≈ S), decisions about preventive/corrective actions (≈ action space), and the iterative human-AI exploration/validation loop. However, there is no formal safety state classification function, no gate function controlling AI participation, and no formally defined admissible action space that varies by safety state.
- **State-dependent recommendation restriction:** Not formally defined. The paper discusses varying levels of automation (from fully manual to fully autonomous) and the concept of "management by consent" in air traffic, where AI acts with human approval. But these are levels of *automation*, not state-conditioned *recommendation scope*. The degree of AI autonomy does not formally vary based on a classified environmental safety state.
- **Safety Dominance Property:** Not defined. No formal guarantee that AI outputs fall within state-determined bounds.
- **Formalisation purpose:** N/A — purely conceptual/qualitative.

**Critical gap relative to my research:** The paper identifies all the *ingredients* for state-conditioned governance (environmental observations, safety constraints, varying action types, time pressure, trade-offs) but does not assemble them into a formal governance model. The seven common decision-making characteristics are descriptive, not prescriptive. My architecture fills this gap by formalising these ingredients into the pipeline E → S = f(E) → (G(S), A_AI(S)) → AI(E).

---

## 6. Safety State Classification

- **Discrete risk/safety levels:** Implicitly present. The power grid use case distinguishes between N conditions (all elements available) and N−k contingency conditions (up to k outages). The air traffic use case distinguishes pre-tactical (planned, 1-2h ahead) and tactical (real-time, minutes) decision modes. Railway operations distinguish normal operations from disrupted conditions.
- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:** These are not formalised as a tripartite safety classification. The power grid's N vs. N−k distinction is a binary contingency model. The air traffic pre-tactical/tactical distinction is temporal, not safety-state-based. None of these map to a formal three-mode classification that conditions AI behaviour.
- **AI recommendation scope differentiation across safety levels:** Not present. The paper discusses varying automation levels but does not tie them to classified environmental safety states. The closest concept is the power grid's "Last Time To Decide" (LTTD), which determines when action must begin — but this is temporal urgency, not safety-state-conditioned recommendation scope.

---

## 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (equivalent to G(S)) | **Partial** | The paper discusses levels of automation ranging from fully manual (AI doesn't participate) to fully autonomous (AI acts independently). Function allocation determines what AI handles. HITL is "essential to prevent critical failures." But participation is not governed by a real-time safety state classification. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (equivalent to A_AI(S)) | **Partial** | Hierarchical decision-making restricts low-level actions to align with high-level goals. Knowledge-assisted AI integrates safety constraints. Railway signalisation is independent, preventing safety-critical rescheduling errors. But these are architectural design patterns, not state-conditioned recommendation scope restrictions. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | **No** | The governance mechanisms described are design-time architectural choices (distributed, hierarchical, knowledge-assisted) and organisational function allocation, not runtime state-conditioned governance. |

- **Governance type:** The paper describes **design-time governance** (function allocation, architectural patterns, safety constraint integration) and **organisational governance** (levels of automation, human oversight requirements, ALTAI trustworthiness assessment). It does not describe **runtime state-conditioned governance** where AI participation and recommendation scope change dynamically based on classified environmental safety state.
- **Supports or contradicts two-level governance pair:** Strongly supports the *principle*. The paper's seven common decision-making characteristics, three architectural patterns, and six research theses collectively argue for structured human-AI governance in safety-critical systems. The knowledge-assisted AI pattern (domain rules constraining ML) is conceptually aligned with my deterministic-gate-first approach. The hierarchical pattern (high-level goals decomposed to constrained low-level actions) parallels the two-level governance structure. But the paper does not unify these into a formal, state-conditioned governance pair.

---

## 8. Human Role in Decision-Making

- **Human involvement:** Central and extensively theorised. The paper develops a comprehensive model of human decision-making in AI-assisted safety-critical operations (Figure 3), encompassing situation awareness, monitoring, deciding, continuous learning, and motivation.
- **Decision support vs. automation:** The paper explicitly argues for optimising "the degree of decision support of AI to humans" rather than simply deploying automation. It positions AI as a "collaborative partner" rather than a replacement. The conclusion states the goal should be "aligning system design with human cognitive processes and limitations."
- **Human-AI interaction dynamics:** Four mental models that operators must maintain: environment model (network knowledge), human-human collaboration model (understanding impacts on other operators), AI model (trust, capabilities, limitations), and self-model (awareness of own biases and patterns). AI supports these through five transparency forms: explanation, exploration, animation, mirroring, and intuitive interface design.
- **Human override / escalation:** Yes — HITL design is "essential to prevent critical failures." Fallback to manual control is a requirement. The power grid use case has escalation to management via operational rules. The concept of "management by consent" in air traffic means AI acts only with human approval.
- **The "director" concept:** The paper proposes assigning humans the role of a "director" who gives directions to one or more AI agents, rather than being a passive supervisor. This maintains human engagement, autonomy, and situation awareness.

**Relevance to my research:** Highly relevant to Theme 6 (human role). The mental model framework, trust calibration concepts (undertrust/overtrust), and the "director" role concept provide theoretical grounding for how fishers in my system should interact with AI recommendations. The five transparency forms suggest how my system should present SAFE/CAUTION/UNSAFE classifications and recommendation scope restrictions.

---

## 9. System Constraints and Environment

- **Real-world constraints:** Yes — all three domains involve real-time operations under uncertainty, time pressure, cascading failure risk, and coordination across multiple operators. External events (weather, equipment failures, public events) create dynamic constraints.
- **Deployment context:** Industry-informed through workshops with real operators (RTE, TenneT, Deutsche Bahn, SBB, NAV Portugal). The CAB prototype is being developed for industrial application. However, the paper itself is a perspective article, not a deployment report.
- **Resource-aware design:** Not in the low-resource sense. The simulation environments (Grid2Op, Flatland, BlueSky) assume standard computing infrastructure.
- **Edge cases:** The ALTAI assessment requires stress testing and handling of rare/corner-case scenarios. The power grid use case addresses N−k contingency conditions.

---

## 10. Hybrid AI Taxonomy

- **Type:** **Knowledge-assisted AI** — combining conventional planning approaches and human domain expertise with data-driven learning. Also distributed (multi-agent) and hierarchical approaches.
- **Classification in my taxonomy:** Closest to **constitutional/governance-based** (domain rules constrain AI behaviour) and **supervisory control** (HITL oversight). The knowledge-assisted pattern maps to my "rule-ML pipeline" category. The hierarchical pattern maps to "stage-gate" with high-level goals decomposed to constrained low-level actions.
- **Safety enforcement location:** Before and alongside AI reasoning. Safety constraints are integrated *into* AI models (knowledge-assisted), architectural decomposition constrains AI scope (hierarchical), and human oversight catches failures (HITL). This is a multi-layered approach.
- **Two-level governance support:** The architectural patterns support the *concept* of multi-level governance: the hierarchical pattern distinguishes high-level decisions (≈ Level 1, whether/what to do) from low-level actions (≈ Level 2, how to do it). Knowledge-assisted AI constrains AI within domain rules (≈ safety constraint integration). But neither pattern is state-conditioned.
- **Comparison to my architecture:** My architecture implements governance computationally through the formal pipeline E → S → (G(S), A_AI(S)) → AI(E), with the deterministic gate evaluated before probabilistic reasoning. This paper's knowledge-assisted pattern is conceptually similar but not formalised as a state-conditioned governance pair.

---

## 11. Baseline Comparison and Evaluation

- **Baseline comparison:** None. The paper is a perspective article, not an empirical evaluation.
- **Metrics:** None measured. The paper references ALTAI trustworthiness dimensions (safety, robustness, transparency, fairness, interpretability, explainability) as evaluation criteria, and suggests future metrics like cognitive load, response time, workload, and situation awareness.
- **Evaluation type:** Conceptual analysis. The ALTAI assessment was applied ex ante to the three use cases. No empirical testing, simulation, or prototype evaluation reported.
- **CAUTION zone testing:** N/A — no safety states defined.
- **Safety Dominance Property verification:** N/A.
- **Graduated vs. binary governance comparison:** Not tested.
- **Evaluation gaps:** The paper acknowledges "empirical evidence on the impact of increased AI transparency on human performance is limited."

---

## 12. Key Concepts and Definitions

| Concept | Definition / Description | Relevance |
|---|---|---|
| **Last Time To Decide (LTTD)** | The latest point when action must begin for its effect to occur before a deadline; computed by subtracting action lead time from deadline | Relevant temporal constraint concept for my architecture's real-time decision-making |
| **Knowledge-assisted AI** | Combining domain expertise/rules with data-driven learning to reduce learning complexity and ensure safety alignment | Directly aligned with my hybrid deterministic-rule + probabilistic-AI approach |
| **Meaningful Human Control** | Framework stressing that AI design must actively engage human decision-making, learning, and motivation | Background for Theme 6 (human role) |
| **Human Readiness Levels** | Framework for assessing human preparedness for effective human-AI collaboration | Could inform socio-technical evaluation design |
| **Co-learning** | Dynamic process where humans and AI continuously learn from each other to improve overall performance | Relevant to long-term system improvement |
| **Cognitive transparency** | Aligning AI outputs with human reasoning processes — beyond mere explainability to supporting situation awareness, learning, and trust | Important for how my system communicates safety states to fishers |
| **Progressive disclosure** | Delivering explanatory information in phases to avoid cognitive overload | Interface design principle for my system |
| **Joint Control Framework (JCF)** | Framework for describing execution and planning of activities when distributed over different agents | Design framework for human-AI interaction |
| **Ecological Interface Design (EID)** | Achieving system transparency by visualising physical and intentional constraints on activities | Interface design framework |
| **ALTAI** | Assessment List for Trustworthy AI — EU framework for evaluating AI trustworthiness properties | Could inform my system's trustworthiness evaluation |
| **Function allocation** | Systematic allocation of tasks between humans and AI based on strengths, limitations, and psychological meaningfulness | Core human-AI design principle |

---

## 13. Limitations and Unsolved Problems

- **Stated limitations:**
  - Perspective article — no empirical evaluation or prototype testing results
  - No formal mathematical model of the decision-making processes described
  - Limited empirical evidence on AI transparency's impact on human performance
  - The feasibility and extent of human oversight remains an open question
  - No consensus on what humans should understand about AI systems
  - The paper's proposals are research directions (theses), not validated solutions

- **Unsolved problems / future work:**
  - Developing hierarchical RL algorithms that scale to complex continuous state and action spaces
  - Integrating safety constraints directly into neural network architectures
  - Creating multi-domain simulation environments for human-AI experimentation
  - Empirical validation of transparency mechanisms on decision quality
  - Adapting AI to operator cognitive state in real-time (psychophysiological data)

- **Alignment with my research gaps:**
  - The paper does **not** identify the lack of state-conditioned governance as a specific gap — its governance concepts are design-time/organisational, not runtime/state-conditioned
  - The paper does **not** formalise the identified decision-making structures into a mathematical model
  - The paper does **not** address the specific CAUTION mode gap (AI participating under restricted scope)
  - **However**, the paper's seven common decision-making characteristics, knowledge-assisted AI concept, and hierarchical architecture pattern provide strong conceptual support for my architecture. The gap between their conceptual description and my formal specification is precisely where my contribution sits.

---

## 14. Methodology Notes

- **Research method:** Multi-stakeholder perspective article. Industry-informed through joint workshops with operators from power (RTE, TenneT), rail (Deutsche Bahn, SBB), and air traffic (NAV Portugal). ALTAI applied for ex ante trustworthiness assessment.
- **Alignment with DSR pipeline:** Partially aligned. The paper identifies requirements (from domain analysis), proposes design patterns (architectural), and discusses evaluation frameworks (ALTAI, CSE). But it does not follow a formal DSR cycle of design → formalise → prototype → evaluate.
- **Methodological insights for my research:**
  - The cross-domain analysis method (identifying shared decision-making characteristics through industry workshops) could inform how I position my architecture as generalizable beyond fisheries
  - The ALTAI trustworthiness assessment provides a structured evaluation framework applicable to my system
  - The JCF and EID integration provides a design methodology for the human-AI interface of my system

---

## 15. Quotable / Citable Points

1. **AI must go beyond accuracy:** "AI must go beyond accuracy and performance — it must be trustworthy" including safety, robustness, transparency, fairness, interpretability, and explainability (Introduction). — *Supports my architecture's emphasis on governance over raw performance*

2. **Knowledge-assisted AI rationale:** "Integrating human-devised safety constraints into AI models can provide a foundation of reliability upon which learning-based improvements can build, ensuring that AI contributions align with predefined safety and operational goals" (Proposed Design section). — *Directly supports my deterministic-gate-first approach*

3. **Optimising decision support degree:** "More focus should be placed on optimizing the degree of decision support of AI to humans, aiming at achieving the best possible interaction between humans and AI (rather than simply deploying AI-based systems)" (Conclusions). — *Supports the principle that AI's recommendation scope should be calibrated, not unconstrained*

4. **HITL essential for safety:** "A human-in-the-loop design is essential to prevent critical failures, ensuring that final decisions remain under human supervision" (ALTAI assessment). — *Supports my decision-support (not decision-automation) positioning*

5. **Human as director, not supervisor:** The paper proposes "to assign the human the role of a 'director,' interacting with and giving directions to one or more AI agents" rather than being a passive supervisory agent (Perspectives section). — *Relevant for how fishers should interact with my system*

---

## 16. Relation to My Research and Positioning

- **Governance levels implemented:** Partial Level 1 (function allocation determines whether AI handles tasks; HITL can block AI) and Partial Level 2 (hierarchical structure constrains low-level actions; knowledge-assisted AI integrates safety rules). Neither level is runtime state-conditioned.
- **State-conditioned governance:** No. Governance is design-time (architectural patterns) and organisational (function allocation, automation levels), not runtime state-conditioned.
- **Proximity to (G(S), A_AI(S)):** Conceptually close but formally distant. The paper identifies all the ingredients: environmental observations, safety constraints, time-varying operational conditions, action space complexity, trade-offs, and the need for human oversight. But it does not assemble these into a formal governance model conditioned on classified environmental safety state.
- **Safety Dominance Property:** Not defined.
- **Gap my research fills:** This paper demonstrates that safety-critical infrastructure domains share common decision-making challenges and that knowledge-assisted, hierarchical, human-in-the-loop AI architectures are needed. But it stops short of formalising these into a state-conditioned governance model. My research takes the next step: formalising the governance pair (G(S), A_AI(S)) that these domains implicitly need, instantiated in the coastal fisheries context.

**Positioning paragraph:** Mussi et al. (2025) provides **strong conceptual support and background for Themes 2, 3, and 6** (safety-critical AI, AI governance, human role) in my literature review. Their cross-domain analysis of power grids, railways, and air traffic management identifies seven shared decision-making characteristics that closely parallel the operational conditions in my coastal fisheries context: environmental uncertainty, time-constrained decisions, large action spaces, conflicting objectives, and the need for human-AI collaboration. Their knowledge-assisted AI pattern — integrating domain safety constraints as a foundation for ML-based improvements — is conceptually aligned with my deterministic-gate-first architecture, and their hierarchical decision-making pattern parallels my two-level governance structure (high-level participation control, low-level advisory scope control). However, the paper remains at the conceptual/qualitative level without formalising these patterns into a mathematical governance model. It proposes architectural design patterns and research theses, not a formal pipeline. The gap between their rich conceptual framework and a formal, runtime, state-conditioned governance specification is precisely where my architecture contributes. My research can cite Mussi et al. as evidence that the need for structured, multi-level, knowledge-assisted AI governance in safety-critical domains is recognised across multiple infrastructure sectors — and then demonstrate how the formal governance pair (G(S), A_AI(S)) provides the missing formalisation.

---

## 17. Overall Relevance Score

### ⭐⭐⭐⭐ High

**Justification:** The paper is directly relevant to four core themes (hybrid AI, safety-critical AI, AI governance, human role) and partially relevant to two more (decision architecture, socio-technical evaluation). It provides rich conceptual support across multiple dimensions of my research: the knowledge-assisted AI pattern supports my hybrid deterministic-rule + probabilistic-AI approach; the hierarchical architecture parallels my two-level governance; the seven common decision-making characteristics validate my problem framing; and the extensive human-role treatment (trust, mental models, situation awareness, motivation) provides theoretical grounding for my socio-technical evaluation. The paper does not reach ⭐⭐⭐⭐⭐ because it lacks mathematical formalisation, does not address the specific CAUTION mode gap, and operates in different domains (power/rail/air, not fisheries). But it is a strong background and gap-evidence paper that demonstrates the cross-domain need for the kind of formal governance architecture my research provides.
