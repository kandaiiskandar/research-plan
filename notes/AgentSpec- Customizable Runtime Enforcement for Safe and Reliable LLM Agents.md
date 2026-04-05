## Literature Review Extraction: Wang, Poskitt & Sun (2026)

---

### 1. Paper Identity

- **Full title:** AgentSpec: Customizable Runtime Enforcement for Safe and Reliable LLM Agents
- **Authors:** Haoyu Wang, Christopher M. Poskitt, Jun Sun
- **Year:** 2026 (ICSE '26, April 12–18, Rio de Janeiro)
- **Venue:** IEEE/ACM 48th International Conference on Software Engineering (ICSE '26)
- **Type:** System design with empirical evaluation (DSL design + multi-domain implementation + experimental evaluation)

---

### 2. Core Contribution

- **Problem:** LLM agents autonomously perceive, plan, and act in diverse environments, but their autonomy introduces safety risks including security vulnerabilities, legal violations, and unintended harmful actions. Existing mitigation methods (model-based safeguards, pre-execution risk assessments) lack robustness, interpretability, and adaptability. Most critically, existing solutions lack *explicit runtime enforcement mechanisms* — they assess risk before execution but impose no active constraints to prevent unsafe actions *during* execution.
- **Solution:** AgentSpec, a lightweight domain-specific language (DSL) for specifying and enforcing runtime constraints on LLM agents. Users define structured rules composed of triggers (events), predicates (conditions), and enforcement mechanisms (interventions). AgentSpec intercepts the agent's decision pipeline, evaluating proposed actions against constraints *prior to execution*.
- **Main contributions:**
  1. The first runtime enforcement framework for LLM agent safety, allowing customizable safety policies via a DSL.
  2. Implementation across three domains: code execution (CodeAct), embodied agents (robotic), and autonomous driving (Apollo).
  3. Empirical evaluation showing: >90% unsafe code executions prevented, 100% compliance in AV law-violation scenarios, all hazardous actions eliminated in embodied agent tasks, with millisecond-level overhead.
  4. Investigation of LLM-generated rules: OpenAI o1 achieves 95.56% precision / 70.96% recall for embodied agents, 87.26% risky code detection, 5/8 AV law-breaking scenarios prevented.
- **Novelty:** First framework that systematically enforces *customizable* safety constraints on LLM agents *at runtime*. Distinguishes itself from pre-execution risk assessment (ToolEmu), dialogue-level constraints (Nemo), syntactic enforcement (llama.cpp), and LLM-interpreted guardrails (GuardAgent) by providing external, developer-defined, per-action rule enforcement with formal semantics.

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | Yes | Core architecture: deterministic rule-based enforcement (AgentSpec DSL) constraining probabilistic LLM agent behaviour. The rule layer is fully deterministic; the agent's planning/reasoning is LLM-driven (probabilistic). The two are explicitly decoupled — enforcement is external to the LLM's reasoning. |
| Safety-critical AI decision-making | Yes | Applied to safety-critical domains: autonomous driving (traffic law compliance), embodied agents (fire, electrical shock, property damage avoidance), code execution (25 vulnerability types). Demonstrates runtime safety enforcement with quantified effectiveness. |
| AI governance / control mechanisms | Yes | Directly implements governance of AI agent actions via per-action rule enforcement. Rules specify triggers, predicates, and enforcement mechanisms (stop, user_inspection, llm_self_examine, invoke_action). This is *per-action governance* — each planned action is evaluated against constraints before execution. |
| Low-resource environments | No | Not addressed. All evaluations assume full computing infrastructure (LangChain, Apollo, LLM API access). No consideration of limited connectivity, low computing power, or resource-constrained deployment. |
| Decision architecture formalisation | Yes | Formal model of LLM agents as tuple (S, A, Ω, Π, Δ). Formal definition of AgentSpec rules as three-tuple r = (η_r, P_r, E_r). Formal semantics for rule violation detection and trajectory modification. Formal definition of enforcement actions (stop, user_inspection, predefined action, LLM self-examination) as trajectory transformations. |
| Human role in decision-making | Yes | Explicitly supports human-in-the-loop via `user_inspection` enforcement — agent pauses and prompts user to approve/reject action. User either permits (trajectory continues) or denies (trajectory terminates). Rules can be manually defined or LLM-generated for user review. |
| Socio-technical evaluation | No | No socio-technical evaluation. Evaluation is purely technical (safety compliance rates, runtime overhead, LLM rule generation accuracy). |
| Coastal fisheries / maritime domain | No | Not addressed. Domains are code execution, embodied agents, and autonomous vehicles. |

**Mid-Extraction Relevance Gate:** 5 Yes → **FULL EXTRACTION.**

---

### 4. Decision Architecture Analysis

- **Decision-making structure:** The LLM agent operates in an iterative loop: receive user input → generate plan → execute action → observe results → repeat. AgentSpec intercepts this loop at three key decision points: before action execution (AgentAction), after observation (AgentStep), and at task completion (AgentFinish). This is a **supervisory control** architecture where the rule enforcement layer sits *between* the agent's planning and its execution.
- **Layered architecture:** Two distinct layers:
  1. **LLM reasoning layer** (probabilistic): the agent's policy function Δ : (U, S) → A generates planned actions.
  2. **AgentSpec enforcement layer** (deterministic): evaluates planned actions against rules before execution, modifying the trajectory if violations are detected.
  These layers are explicitly decoupled — enforcement is external to the LLM, improving verifiability and robustness.
- **Rule-based constraints before AI decisions:** Yes — this is the core mechanism. AgentSpec evaluates rules *before* each action is executed. The enforcement function Eval(τ_i, a_i) checks the trajectory and planned action against all active rules. If a violation is detected, enforcement modifies the trajectory before the action proceeds.
- **Boundary between deterministic control and AI reasoning:** Explicitly defined. The agent's reasoning (LLM-driven, probabilistic) produces planned actions. AgentSpec's enforcement (rule-driven, deterministic) evaluates and potentially modifies those actions. The LLM never controls the enforcement logic; enforcement is external and developer-defined.
- **Failure modes and fallback:** Four enforcement mechanisms provide graduated responses: (1) **stop** — immediately terminate; (2) **user_inspection** — pause for human approval; (3) **invoke_action** — execute a predefined corrective action; (4) **llm_self_examine** — invoke LLM self-reflection to generate corrective response. These provide a spectrum from full blocking to reflective correction.

**Key comparison to my architecture:** AgentSpec enforces rules *per-action* based on the action type and predicates about the current state/trajectory. My architecture enforces governance *per-safety-state* based on classified environmental conditions. AgentSpec asks "Is this specific action safe given current conditions?" My architecture asks "What *types* of actions is AI permitted to generate given the current safety state?" The distinction is between **per-action rule enforcement** and **state-conditioned action-space restriction**.

---

### 5. Formal Model and Mathematical Representation

- **Formal model:** Yes — well-formalised.
  - **Agent model:** Tuple (S, A, Ω, Π, Δ) where S = states, A = actions, Ω = observations, Π : Ω → S = perception function, Δ : (U, S) → A = policy function.
  - **Trajectory:** τ = ⟨s₀ →^a₀ s₁ →^a₁ ... →^aₙ₋₁ sₙ⟩
  - **Rule:** Three-tuple r = (η_r, P_r, E_r) where η_r = triggering event, P_r = set of predicate functions, E_r = sequence of enforcement functions.
  - **Rule violation:** Rule r is violated when triggering event η_r occurs AND all predicates p_r ∈ P_r evaluate to true.
  - **Enforcement as trajectory transformation:** Each enforcement e_r transforms the trajectory τ_i. Stop terminates with finish action. User inspection branches on user approval. Predefined action appends corrective action. LLM self-examination generates corrective response via Δ.

- **Comparison to E → S = f(E) → (G(S), A_AI(S)) → AI(E):**

  | My Architecture | AgentSpec | Comparison |
  |---|---|---|
  | **E** (environmental state vector) | S (agent states), Ω (observations) | Both model environmental/system state, but my E is specifically an environmental parameter vector; AgentSpec's S is the agent's internal state representation. |
  | **S = f(E)** (safety state classification) | No equivalent | **Critical gap.** AgentSpec has no global safety state classifier. There is no function that maps environmental conditions to discrete safety levels. Each rule evaluates conditions independently. |
  | **G(S)** (participation gate) | Rule enforcement can `stop` agent | AgentSpec's `stop` enforcement is functionally equivalent to G(S) = 0 for a *specific action*, but it is triggered per-action by specific predicates, not by a global classified safety state. There is no concept of "AI is blocked in UNSAFE state." |
  | **A_AI(S)** (admissible action space) | No equivalent | **Critical gap.** AgentSpec does not define a state-conditioned admissible action *space*. It evaluates individual actions against individual rules. There is no formal structure that says "under safety state S, only recommendation types {R₁, R₂} are permitted." |
  | **Safety Dominance Property** | Eval(τ_i, a_i) must be safe | Conceptually related but structurally different. AgentSpec ensures each individual action passes rule checks. My Safety Dominance Property guarantees that *all* AI outputs fall within the state-determined admissible space: AI(E) ⊆ A_AI(S). AgentSpec's guarantee is per-action; mine is per-state across the full output space. |

- **State-dependent recommendation restriction:** **No.** AgentSpec does not restrict the *types* of recommendations AI may generate based on classified safety state. It evaluates each specific planned action against applicable rules. The agent's action space A is the same regardless of environmental conditions — unsafe actions are caught and blocked individually, not excluded from the admissible space *a priori*.

- **Safety Dominance Property:** No formal equivalent. The closest analogue is the enforcement semantics ensuring that Eval(τ_i, a_i) is safe throughout operation. But this is a per-action verification property, not a global containment property like AI(E) ⊆ A_AI(S). AgentSpec could in principle *miss* an unsafe action if no rule covers it; the Safety Dominance Property would formally guarantee that *no* AI output exceeds the state-determined bounds.

- **Formalisation purpose:** Operational — the formal semantics directly drive the runtime enforcement implementation. The DSL syntax is parsed by ANTLR4 and executed as part of the agent's decision loop.

---

### 6. Safety State Classification

- **Discrete risk/safety levels:** **No.** AgentSpec does not classify the environment or operational conditions into discrete safety levels. There is no tripartite (SAFE/CAUTION/UNSAFE) or any other global state classification.
- **How risk is handled instead:** Risk is evaluated *per-action* through rule predicates. Each rule checks whether a specific condition holds for a specific action — e.g., `front_vehicle_closer_than(10)`, `is_destructive_cmd`, `is_fragile_object`. These are local, action-specific risk evaluations, not global safety state classifications.
- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:** AgentSpec's approach is fundamentally different. Where my architecture classifies the *environment* into a global safety state that then governs the *entire AI output space*, AgentSpec evaluates *each action* against *each rule* independently. There is no intermediate safety state layer between environmental conditions and enforcement decisions.
- **Differentiated AI recommendation scope across safety levels:** **No.** This is the core architectural gap. AgentSpec does not define modes where AI participates with different recommendation scopes. The agent either proceeds (action passes all rules) or is intervened upon (action violates a rule). There is no CAUTION mode where AI still participates but with a restricted output type set — e.g., where AI may recommend "go/no-go" but not "departure timing" or "trip duration."

---

### 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (equivalent to G(S)) | Partial | The `stop` enforcement terminates the agent for a specific action/trajectory. `user_inspection` conditionally blocks. But these are triggered per-action by specific predicates, not by a global classified safety state. There is no concept of "AI is systematically blocked when environmental state = UNSAFE." |
| **Level 2 — Advisory scope governance** | What may AI recommend? (equivalent to A_AI(S)) | No | AgentSpec does not restrict the *types* of recommendations AI may generate. It evaluates specific actions post-planning but pre-execution. The agent's planning function Δ always generates from the full action space A, with enforcement filtering individual actions. There is no mechanism to formally restrict the *recommendation space* to a subset conditioned on safety state. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | No | No global safety state classification exists. Rules are triggered by specific events and predicates, not by a unified environmental state classifier. |

- **Binary AI switch or graduated governance?** AgentSpec implements **per-action binary enforcement** — each specific action either passes (proceed) or fails (enforce). This is neither a global binary switch nor graduated governance. It is more fine-grained than binary (different rules for different actions) but less structured than graduated (no formal state-conditioned output space hierarchy).
- **Level 2 governance:** Not implemented. AgentSpec's rules constrain *individual actions*, not *action types* or *recommendation scopes*. The distinction is critical: AgentSpec says "this specific `pour` action is blocked because the target is not wettable." My architecture says "under CAUTION state, the AI is only permitted to generate {Go, Delay} recommendations — DepartureTime and Duration are excluded from the admissible space entirely."
- **Support or contradiction for (G(S), A_AI(S))?** AgentSpec **strongly supports the need** for structured AI governance but implements it at a different level of abstraction. It demonstrates that per-action rule enforcement is effective for catching specific unsafe actions (>90% code, 100% AV, 100% embodied). However, it does not address the question of *systematically restricting AI's advisory scope* based on classified environmental conditions. The two approaches are **complementary**: AgentSpec could enforce rules *within* each safety state, while my architecture defines *which types of recommendations are admissible* per state.

---

### 8. Human Role in Decision-Making

- **Human involvement:** The `user_inspection` enforcement pauses the agent and prompts the user to approve or reject the planned action. If the user permits, the trajectory continues; if the user denies, the agent stops. This is a binary human-in-the-loop mechanism.
- **System positioning:** Decision support with human override capability. The agent plans autonomously, but AgentSpec can force human review at critical junctures. The user can also define all rules, maintaining ultimate control over the safety policy.
- **Human–system interaction:** Through rule-triggered inspection prompts. The user sees the planned action and decides whether to proceed. Rules can also be manually authored, giving users interpretable control over safety policy.
- **Override mechanisms:** `user_inspection` is the primary override. The user can also define rules that invoke `stop` (automatic override) or `llm_self_examine` (system self-corrects without human intervention). The graduated enforcement options (stop / user_inspection / invoke_action / llm_self_examine) provide different levels of human involvement.

---

### 9. System Constraints and Environment

- **Real-world constraints:** Not addressed. AgentSpec assumes standard computing infrastructure (LangChain, LLM API access, Apollo autonomous driving stack). No consideration of limited data, connectivity, computing power, or user expertise constraints.
- **Deployment context:** Evaluated in controlled settings: RedCode-Exec benchmark (code safety), SafeAgentBench (embodied agent hazards), FixDrive (AV law violations). Not deployed in real-world operational environments.
- **Resource-aware design:** AgentSpec is computationally lightweight (millisecond overhead: ~1.42ms parsing, ~2.83ms predicate evaluation for code, ~1.11ms for embodied agents). This is resource-efficient but the paper does not address deployment in truly resource-constrained environments.
- **Edge cases:** The evaluation identifies some edge cases: LLM-generated rules can overfit to provided examples, miss complex object properties, or oversimplify (e.g., banning all `pour` actions instead of contextually evaluating them). The paper acknowledges that AgentSpec lacks trajectory-based safety analysis — it cannot reason about long-term consequences of action sequences.

---

### 10. Hybrid AI Taxonomy

- **Hybrid approach type:** **Supervisory control** — a deterministic rule-based enforcement layer supervises and constrains the probabilistic LLM agent's planned actions at runtime. The enforcement is external to the LLM's reasoning.
- **Safety enforcement location:** **Before AI action execution** — AgentSpec intercepts planned actions *after* the LLM generates them but *before* they are executed. This is a pre-execution enforcement point within the iterative plan-act loop.
- **Two-level governance support:** AgentSpec supports **single-level governance** (Level 1: per-action participation control). It does not support Level 2 (state-conditioned advisory scope restriction). The enforcement is per-action binary (pass/enforce), not state-conditioned graduated.
- **Comparison to my architecture:** Both implement deterministic-gate-first enforcement over probabilistic AI. However:
  - My architecture classifies the *environment* into a global safety state → restricts the *entire AI output space* per state.
  - AgentSpec evaluates *each planned action* against *each rule* → intervenes on specific actions that violate specific conditions.
  - My architecture is **state-to-space** governance; AgentSpec is **action-to-rule** governance.
  - My architecture defines *what AI may recommend*; AgentSpec checks *whether a specific recommendation is safe*.

---

### 11. Baseline Comparison and Evaluation

- **Baseline comparison:** Compared against: (a) unguarded agents (no AgentSpec), showing the baseline unsafe behaviour rates; (b) prior work qualitatively — ToolEmu (risk assessment without enforcement), GuardAgent (LLM-interpreted guardrails), Nemo (dialogue-level constraints), llama.cpp (syntactic enforcement).
- **Metrics:** Safety compliance rate (% of unsafe actions prevented), precision/recall for LLM-generated rules, runtime overhead (milliseconds).
- **Evaluation scope:**
  - Code agent: 750 risky scenarios across 25 vulnerability categories, 30 test cases each.
  - Embodied agent: 250 risky + safe scenarios across 10 unsafe + 1 safe category.
  - AV: 8 law-violation scenarios from FixDrive.
- **CAUTION zone testing:** **Not applicable.** No CAUTION mode exists — enforcement is binary per-action.
- **Safety Dominance Property verification:** Not explicitly. The evaluation measures the *proportion* of unsafe actions caught, not a formal guarantee that all outputs fall within state-determined bounds. The >90%/100% compliance rates are empirical, not formal proofs.
- **Graduated vs. binary governance comparison:** Not performed. No comparison between per-action binary enforcement and state-conditioned graduated governance.
- **Evaluation gaps:** (1) No evaluation of graduated governance where AI participates under restricted scope. (2) No real-world deployment testing. (3) No evaluation in low-resource or data-poor environments. (4) No formal verification of safety properties — compliance rates are empirical. (5) The paper acknowledges lacking trajectory-based safety analysis (long-term consequence reasoning).

---

### 12. Key Concepts and Definitions

- **AgentSpec rule:** Three-tuple r = (η_r, P_r, E_r) — triggering event, set of predicate functions, sequence of enforcement functions.
- **Triggering events:** state_change (current state differs from previous), before_action (before executing planned action), agent_finish (task completion). Plus domain-specific events (red_light_detected, rain_started, etc.).
- **Enforcement mechanisms:** stop (terminate trajectory), user_inspection (pause for human approval), invoke_action (execute predefined corrective action), llm_self_examine (LLM self-reflection to generate corrective response).
- **Trajectory:** τ = ⟨s₀ →^a₀ s₁ →^a₁ ... →^aₙ₋₁ sₙ⟩ — the sequence of states and actions capturing the agent's decision-making history.
- **Rule violation:** Occurs when triggering event fires AND all predicates evaluate to true.
- **Enforcement as trajectory transformation:** Each enforcement function e_r maps the current trajectory τ_i to a modified trajectory τ'_i.
- **Framework-agnostic design:** AgentSpec is implemented on LangChain but designed to be adaptable to other frameworks (AutoGen, Apollo).

---

### 13. Limitations and Unsolved Problems

**Stated limitations:**
1. AgentSpec performs **deterministic enforcement at discrete execution checkpoints** — it does not reason about long-term consequences of action sequences (no trajectory-based safety analysis).
2. LLM-generated rules can **overfit to provided examples**, failing to generalise to broader unsafe patterns.
3. LLM-generated rules can be **overly rigid** with vague requirements (e.g., banning all `pour` actions instead of contextual evaluation).
4. The framework requires **predicate implementations** — either manually coded or LLM-generated — which can miss edge cases.

**Unsolved problems / future work:**
1. Extending AgentSpec with **probabilistic enforcement mechanisms** incorporating model-based foresight (e.g., DTMC-based probabilistic reachability queries to estimate likelihood of reaching unsafe states).
2. No mechanism for **graduated governance** where AI's advisory scope varies by classified safety state.
3. No consideration of **low-resource deployment** environments.
4. No **formal verification** of safety properties — compliance is empirically measured, not formally proven.

**Alignment with my research gaps:**
- **No global safety state classification.** AgentSpec evaluates per-action conditions but does not classify the environment into discrete safety states. My architecture provides the missing S = f(E) layer.
- **No state-conditioned admissible action space.** AgentSpec checks individual actions against rules but does not define a formal space of permitted recommendation *types* per safety state. My architecture provides A_AI(S) — the two-level governance model that separates *whether AI operates* from *what AI may recommend*.
- **No CAUTION mode.** AgentSpec's enforcement is binary per-action: the action passes or is enforced. There is no intermediate mode where AI continues operating but with a restricted recommendation scope. My CAUTION state fills this gap: G(S) = 1 (AI participates) but A_AI(CAUTION) ⊂ A_AI(SAFE) (restricted advisory scope).
- **No Safety Dominance Property for graduated governance.** AgentSpec's per-action enforcement is effective but does not provide a formal guarantee comparable to AI(E) ⊆ A_AI(S).
- **The two approaches are complementary:** AgentSpec operates at the *per-action* enforcement level; my architecture operates at the *per-state governance* level. AgentSpec could be used to enforce rules *within* each safety state, while my architecture defines *which recommendation types are admissible* per state.

---

### 14. Methodology Notes

- **Method:** System design (DSL design + implementation) with empirical evaluation across three domains. Includes benchmarking against established datasets (RedCode-Exec, SafeAgentBench, FixDrive), runtime overhead measurement, and investigation of LLM-generated rules.
- **Alignment with my DSR pipeline:** Partial. AgentSpec follows a design → implement → evaluate cycle similar to DSR. The formal semantics provide a formalisation component. However, there is no socio-technical evaluation, no real-world deployment, and no user study.
- **Methodological insights:** The multi-domain evaluation approach (code, embodied, AV) demonstrates the framework's generalisability — a useful model for my own evaluation, which could similarly demonstrate my architecture's applicability across domains. The investigation of LLM-generated rules is relevant to automation of safety policy specification. The split between manual and LLM-generated rules maps to the distinction between expert-defined safety thresholds and automatically inferred parameters in my architecture.

---

### 15. Quotable / Citable Points

1. **Per-action enforcement as the state of the art:** AgentSpec is described as "the first framework that systematically enforces customizable safety constraints on LLM agents at runtime" — positioning per-action rule enforcement as the current frontier. (Section 1, Introduction)

2. **Limitation of pre-execution risk assessment:** "Most existing solutions lack explicit safety enforcement mechanisms, focusing instead on pre-execution risk assessments. This approach leaves agents vulnerable to runtime deviations from expected behavior, as there are no active constraints to prevent unsafe actions during execution." (Section 1, Introduction)

3. **Varying risk tolerance requiring customizable governance:** "Organizations that use [LLM agents] may exhibit varying levels of risk tolerance... effective mechanisms to customize and enforce safety restrictions on LLM agents are essential." (Section 1, Introduction)

4. **Lack of trajectory-based safety analysis:** "AgentSpec lacks support for trajectory-based safety analysis, i.e., estimating whether an action sequence might lead to unsafe states several steps into the future." (Section 6.3, Limitations)

5. **Decoupling enforcement from LLM reasoning:** "This explicit separation between the agent's reasoning and its safety enforcement mechanism improves verifiability and robustness in safety-critical scenarios." (Section 6.1, Comparison to Prior Work)

---

### 16. Relation to My Research and Positioning

- **Level 1 governance:** Partially implemented via per-action `stop` and `user_inspection` enforcement. But this is action-specific, not globally conditioned on classified environmental state.
- **Level 2 governance:** Not implemented. No state-conditioned restriction of AI recommendation *types*.
- **State-conditioned?** No. Rules are triggered by specific events and predicates, not by a unified safety state classifier.
- **Two-level governance pair (G(S), A_AI(S))?** Falls short on the unified, state-conditioned aspect. AgentSpec implements rich per-action enforcement (more fine-grained than my architecture at the action level) but lacks the global safety state classification and state-conditioned action space restriction (less structured than my architecture at the governance level).
- **Safety Dominance Property?** No formal equivalent. Empirical compliance rates (>90%, 100%) approximate but do not formally guarantee the containment property AI(E) ⊆ A_AI(S).
- **Gap my research addresses:** AgentSpec demonstrates that per-action rule enforcement is effective and practical. My architecture addresses the missing *structural layer*: global safety state classification → state-conditioned admissible action space → Safety Dominance Property. The two approaches complement each other: my architecture defines *what types of recommendations are permissible per safety state*; AgentSpec could enforce *specific action constraints within each state*.

**Positioning paragraph:** Wang et al. (2026) represents the **closest architectural antecedent** to my research and the primary baseline comparator. AgentSpec demonstrates that deterministic, rule-based runtime enforcement over probabilistic LLM agents is practical, effective, and computationally lightweight — validating the core design principle that deterministic safety constraints should govern AI behaviour externally. Its formal model of agents, rules, and enforcement as trajectory transformations provides a rigorous foundation upon which my architecture builds. However, AgentSpec implements **per-action rule enforcement** — evaluating each specific planned action against individual rules — without a global safety state classifier or state-conditioned admissible action space. Every rule in AgentSpec operates independently; there is no intermediate governance layer that classifies the *environment* into discrete safety states and then systematically restricts the *types* of recommendations AI may generate. This is precisely the gap my two-level governance model fills. Where AgentSpec asks "Is *this action* safe?" my architecture asks "What *types of actions* is AI permitted to generate given the current safety state?" The CAUTION mode — where G(S) = 1 but A_AI(CAUTION) ⊂ A_AI(SAFE) — is architecturally absent from AgentSpec, which has no mechanism for AI to continue operating with a formally restricted advisory scope. My architecture adds the missing layers: S = f(E) for global safety state classification, A_AI(S) for state-conditioned action space restriction, and the Safety Dominance Property AI(E) ⊆ A_AI(S) for formal guarantees over the graduated governance model.

---

### 17. Overall Relevance Score

**⭐⭐⭐⭐⭐ Core — closest prior art and primary architectural antecedent**

**Justification:** AgentSpec is the single most relevant paper to my research. It implements the closest existing approach to runtime AI safety enforcement via deterministic rules over probabilistic AI agents, with a formal model, multi-domain evaluation, and practical millisecond-level overhead. It directly demonstrates the effectiveness of the design principle my architecture extends (deterministic-gate-first enforcement). Its precisely identifiable gap — the absence of global safety state classification, state-conditioned admissible action space, and CAUTION mode with restricted advisory scope — is exactly what my two-level governance model provides. AgentSpec serves simultaneously as: (a) the **strongest baseline comparator** (per-action enforcement vs. my state-conditioned governance), (b) **architectural validation** (proves deterministic enforcement over LLM agents is practical), and (c) **gap evidence** (demonstrates that even the most advanced per-action enforcement lacks the state-level governance structure my architecture introduces). The formal structures (agent tuple, rule three-tuple, trajectory transformation) provide a compatible formal vocabulary that positions my formalisation as a natural extension.
