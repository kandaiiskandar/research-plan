## Literature Review Extraction: Könighofer et al. (2025) — Shields for Safe RL (CACM)

---

### 1. Paper Identity

- **Title:** Shields for Safe Reinforcement Learning
- **Authors:** Bettina Könighofer, Roderick Bloem, Nils Jansen, Sebastian Junges, Stefan Pranger
- **Year:** 2025 (November)
- **Venue:** Communications of the ACM, Vol. 68, No. 11, pp. 80–90
- **DOI:** 10.1145/3715958
- **Type:** Research overview / tutorial article (accessible synthesis of shielding research programme)
- **Note:** Already rated ⭐⭐⭐⭐⭐ in tracker. This extraction covers the CACM 2025 article specifically, which is a mature, accessible synthesis suitable for direct citation.

---

### 2. Core Contribution

- **Problem:** RL does not provide safety guarantees during learning or deployment. The agent must explore (risking unsafe actions), and even during exploitation there is no guarantee it will never choose unsafe actions. Three categories of safe RL exist: reward shaping, constraining (cost functions), and shielding (blocking unsafe actions).
- **Solution:** Shields — mechanisms that provide formal safety guarantees by preventing unsafe actions from being executed at runtime. Shields are computed from a formal specification of safety-critical properties + an abstract model of the environment, independent of the agent's learning objective. Two integration modes: pre-shielding (providing list of safe actions) and post-shielding (replacing unsafe actions with safe alternatives).
- **Main contributions (this CACM article):**
  - Clear taxonomy of shield types: absolute (deterministic) vs. probabilistic guarantees
  - Formal framework: safety games on environment models, winning regions, dangerous/safe/unsafe state classification
  - Demonstration of both absolute and probabilistic shields with UAV examples
  - Discussion of benefits (safety assurance, improved sample efficiency), drawbacks (model dependence, possible reduced learning performance, computational effort), and extensions (partial observability, continuous systems, multi-agent, beyond safety properties)
- **Key insight:** "Shielded RL combines symbolic AI, which provides formal safety guarantees but has lower scalability, with sub-symbolic RL, which offers high scalability but lacks guarantees."

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | Yes | Explicitly combines symbolic AI (formal model, shield computation via model checking/game solving) with sub-symbolic RL (neural network policies). Shield is the deterministic rule-based layer; RL is the probabilistic learning layer |
| Safety-critical AI decision-making | Yes | Core focus — shields enforce safety in safety-critical RL applications (UAV, robotics, autonomous driving). Formal safety guarantees during both training and deployment |
| AI governance / control mechanisms | Yes | Shields are the archetypal runtime AI governance mechanism — they control which actions the AI may execute based on formal safety specifications. Pre-shielding restricts available actions; post-shielding corrects unsafe actions |
| Low-resource environments | No | Computational requirements for shield synthesis are significant (model checking); not low-resource oriented |
| Decision architecture formalisation | Yes | Formally defined: MDP model, safety specification (LTL), safety game, winning region, shield computation via backward traversal. Probabilistic shields with threshold ε, dynamic programming for reachability probabilities |
| Human role in decision-making | No | Fully autonomous RL agent; no human decision-maker |
| Socio-technical evaluation | No | Formal verification and simulation demonstrations only |
| Coastal fisheries / maritime domain | No | UAV delivery, robotics, autonomous driving |

**Mid-Extraction Relevance Gate:** 4 Yes → **FULL EXTRACTION**

---

### 4. Decision Architecture Analysis

- **Architecture:** Two-component architecture: **RL agent** (generates candidate actions) + **Shield** (evaluates and constrains actions). Two modes:
  - **Post-shielding:** Shield sits between agent and environment. Agent proposes action → shield evaluates → shield either passes or replaces with safe alternative → environment executes safe action
  - **Pre-shielding:** Shield provides list of all safe actions → agent selects from safe set only
- **Layered structure:** Binary: (1) shield layer (formal, symbolic, deterministic), (2) RL layer (learned, sub-symbolic, probabilistic). Clear architectural separation.
- **Rule-based constraints before/on AI:** Shield is computed from formal model + safety specification using model checking / safety game solving. Constraints are mathematically proven, not learned. Applied either before (pre-shielding) or after (post-shielding) agent's action selection.
- **Boundary between deterministic and AI reasoning:** Explicitly defined and architecturally enforced. The shield is a separate module from the RL agent. Shield maintains "a clear separation between an agent's safety and performance."
- **Failure modes / fallback:** "In case a state outside of the winning region is entered during runtime, a fallback strategy needs to be defined, such as selecting a predefined action (for example, braking or landing), or allowing only the safest possible action." Also: "it is formally not possible to compute a shield if no safe action exists."

---

### 5. Formal Model and Mathematical Representation

- **Formal elements:**
  - **MDP:** Environment modelled as finite-state MDP with probabilistic transition function
  - **Two-player game:** Deterministic shield computed by transforming MDP into adversarial two-player game (agent vs. environment)
  - **Safety specification:** Expressed in LTL, converted to automata, combined with model via product construction
  - **Winning region:** Set of all safe states (inductive — from any safe state, agent can select action leading to another safe state regardless of environment's choice). Computed by backward traversal in time linear in graph size
  - **Dangerous states:** States from which environment can force visit to unsafe state regardless of agent's actions
  - **Probabilistic shield:** Action classified as safe if probability of reaching unsafe state within h steps is at most ε. Computed via dynamic programming (stochastic shortest path)
  - **Dynamic program:** x_{s,h} = min_a { Σ_{s'} P(s'|s,a) · x_{s',h-1} } computing minimal reachability probability to bad states

- **Comparison to DSR pipeline:**

| Shield concept | My DSR concept | Relationship |
|---|---|---|
| Environment model (MDP) | E (environmental state vector) | Both represent the operational environment formally |
| Safety specification (LTL) | Safety properties & constraints | Both define what constitutes safe/unsafe operation |
| Shield (safe/unsafe action classification) | G(S) (gate function) | Both determine whether AI actions are permitted |
| Pre-shield safe action set | A_AI(S) (admissible action space) | Both define the set of permitted AI actions |
| Winning region (safe states) | S = SAFE or CAUTION | Both classify environmental states by safety |
| Dangerous states | S = UNSAFE (or approaching UNSAFE) | Both identify states where AI should be restricted |

- **State-dependent recommendation restriction:** **Partially.** The shield's safe action set varies by state — in different states, different actions are permitted. This is state-dependent action restriction. However, the shield classifies actions as safe/unsafe per individual state-action pair, not by classifying the environmental state into discrete governance modes (SAFE/CAUTION/UNSAFE) with different advisory scope types.

- **Safety Dominance Property equivalent:** **Yes — the shield provides a formal safety guarantee** that from any state in the winning region, the agent can always avoid unsafe states regardless of environment behaviour. For absolute shields: unsafe states are never visited. For probabilistic shields: probability of reaching unsafe states ≤ ε. This is structurally analogous to AI(E) ⊆ A_AI(S) — the agent's executed actions always fall within the shield-determined safe set.

- **Formalisation purpose:** Used for provable safety guarantees (model checking, game solving). The formalisation is operational — shields are computed from the formal model and deployed at runtime.

---

### 6. Safety State Classification

- **State classification:** Yes — the paper explicitly classifies states into three categories:
  - **Safe states** (winning region): Agent can always avoid unsafe states regardless of environment
  - **Dangerous states:** Environment can force visit to unsafe state regardless of agent's actions
  - **Unsafe states:** States representing safety property violations (e.g., collision)
- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:** Structurally parallel but functionally different:
  - Shield's classification is per-state binary: safe (in winning region) or dangerous/unsafe (outside)
  - My classification is environmental tripartite: SAFE / CAUTION / UNSAFE
  - The shield's "safe" encompasses both my SAFE and CAUTION (agent can still act); the shield's "dangerous" maps to my UNSAFE (agent should be blocked)
  - **No CAUTION equivalent:** The shield has no intermediate mode where the agent is permitted but with restricted scope. States are either in the winning region (all safe actions available) or outside it (fallback/safe state)
- **AI recommendation scope across safety levels:** Within the winning region, the shield restricts which specific actions are safe (varying per state), but does not restrict action *types*. The agent can always attempt any *type* of action — the shield evaluates specific action instances. No equivalent to A_AI(CAUTION) ⊂ A_AI(SAFE) where entire categories of output are excluded.

---

### 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (G(S)) | Yes | Within the winning region, AI operates (G = 1). Outside it, fallback is triggered (effectively G = 0). Shield enforces this boundary |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | Partial | Pre-shielding provides state-specific safe action sets (varying per state). However, these sets are defined by individual action safety, not by action *type* restriction across governance modes |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | Partial | Safe action sets are state-conditioned (vary per state). But governance does not vary by discrete classified environmental mode — it's per-state, per-action evaluation |

- **Governance type:** **Level 1 (binary participation via winning region boundary) + per-state action filtering (partial Level 2).** The shield provides the most formally rigorous per-action safety governance available. But it does not implement graduated governance modes.
- **Binary vs. graduated:** Binary at the state level (in winning region → AI operates; outside → fallback). Within the winning region, action sets vary per state, but this is per-action safety filtering, not mode-graduated scope restriction.
- **Probabilistic threshold ε as graduated parameter:** Different ε values produce shields of different restrictiveness (ε = 0.00 most restrictive; ε = 0.05 most liberal). This is the closest element to graduated governance — by adjusting ε, shields can be "more liberal or more restrictive toward the agent." However, ε is a design-time parameter, not a runtime state-conditioned mode switch.

---

### 8. Human Role in Decision-Making

- **Human role:** None during operation. The agent is fully autonomous; the shield operates automatically.
- **Decision support vs. automation:** Full automation. The shield enforces safety without human intervention.
- **Override mechanism:** The shield itself is the override mechanism — it overrides unsafe agent actions with safe alternatives.

---

### 9. System Constraints and Environment

- **Computational requirements:** Shield computation requires model checking / safety game solving, which can handle billions of states but may be challenged by larger real-world environments. Ongoing research challenge.
- **Deployment:** Demonstrated in simulation (grid worlds, UAV scenarios). Applied to robotics and autonomous driving in referenced works.
- **Resource-aware:** Not explicitly. Shield computation is computationally intensive.

---

### 10. Hybrid AI Taxonomy

- **Type:** **Neuro-symbolic / supervisory control.** Shield (symbolic AI, formal verification) supervises RL agent (sub-symbolic AI, neural networks). The paper explicitly frames this as combining symbolic and sub-symbolic AI.
- **Safety enforcement:** **Before AI reasoning (pre-shielding)** or **after AI reasoning (post-shielding)**, depending on integration mode.
- **Two-level governance support:** The shield implements Level 1 governance with per-state action filtering (partial Level 2). Does not implement graduated governance modes with different advisory scope types.
- **Comparison to my architecture:** Both use a deterministic safety layer constraining probabilistic AI. The shield is structurally equivalent to G(S) with per-state action sets. My architecture extends this by: (a) classifying states into discrete governance modes, (b) defining action *type* restrictions per mode (A_AI(S)), (c) enabling a CAUTION mode with restricted but non-empty advisory scope.

---

### 11. Baseline Comparison and Evaluation

- **Baselines:** Shielded vs. unshielded RL in two demonstrations:
  - UAV with absolute safety (Fig. 10): Shielded achieves zero safety violations and faster convergence
  - UAV with probabilistic safety (Fig. 12): Different ε values compared — ε = 0.03 and 0.05 learn faster and achieve higher reward than both unshielded and ε = 0.00
- **Key result:** "When using either shield that allows the agent to take some risk, the agent learns faster and achieves a higher reward compared to using no shield or a shield that completely forbids taking risks." This demonstrates that intermediate levels of restriction outperform both no restriction and maximum restriction — empirical motivation for graduated governance.
- **CAUTION zone testing:** Not directly. But the ε = 0.03/0.05 results show that intermediate-restrictiveness shields outperform both extremes, which is the empirical analogue of CAUTION outperforming binary SAFE/UNSAFE.
- **Safety Dominance verification:** Yes — absolute shields guarantee zero violations; probabilistic shields guarantee P(violation) ≤ ε.

---

### 12. Key Concepts and Definitions

- **Shield:** Mechanism providing formal safety guarantees by preventing unsafe actions at runtime, computed from formal specification + abstract environment model, independent of agent's learning objective.
- **Pre-shielding:** Shield provides list of safe actions before agent selects; agent chooses from safe set.
- **Post-shielding:** Shield positioned between agent and environment; evaluates agent's action and replaces unsafe actions with safe alternatives.
- **Winning region:** Inductive set of safe states from which agent can always avoid unsafe states regardless of environment behaviour.
- **Dangerous states:** States from which environment can force visit to unsafe state regardless of agent's actions.
- **Absolute vs. probabilistic safety guarantees:** Absolute — unsafe states are never visited (deterministic model, worst-case). Probabilistic — P(reaching unsafe state within h steps) ≤ ε (probabilistic model, risk-bounded).
- **Permissiveness:** Shields do not hinder safe actions — they are maximally permissive within safety constraints.
- **Dynamic adaptation:** "Shields with probabilistic guarantees may adapt their probability threshold dynamically based on the agent's performance and the state of the environment."
- **Supervisory control theory:** Shielding interpretable as high-level controller disabling certain actions of lower-level controllers.

---

### 13. Limitations and Unsolved Problems

- **Stated limitations:**
  - Shield depends on model correctness — "if the model fails to capture a safety-relevant aspect, the shield cannot avoid safety-critical behavior"
  - Computational effort — realistic MDPs may have very large state spaces
  - Possible reduced learning performance — restrictive shields may hinder exploration
  - Shield cannot ensure perception correctness (e.g., object classification)
- **Open challenges identified:**
  - How to obtain reliable world models?
  - How to maintain guarantees in uncertain and changing world?
  - How to provide meaningful probabilistic guarantees?
  - Can shields be explained to increase trust in human-AI interactions?
- **Alignment with my research gaps:**
  - **Binary governance:** Shields classify actions as safe/unsafe — no intermediate "partially restricted" mode. The shield either permits an action or blocks it.
  - **No graduated advisory scope:** Within the winning region, shields filter specific actions but do not restrict action *types*. No equivalent to A_AI(CAUTION) ⊂ A_AI(SAFE).
  - **ε threshold is design-time:** Different ε values produce different shields, but switching between ε values based on runtime environmental state is not formalised (though "dynamic adaptation" is mentioned).
  - **My architecture fills the gap** between the shield's per-action binary classification and a mode-graduated governance pair that restricts advisory scope types across classified environmental states.

---

### 14. Methodology Notes

- **Method:** Formal methods (model checking, safety games, reactive synthesis, supervisory control). Demonstrations via simulation with Stable-Baselines3 and TEMPEST shield synthesis tool.
- **DSR alignment:** Not DSR. Pure formal methods + experimental demonstration. However, the formal rigour of shield computation aligns with my formalisation approach.

---

### 15. Quotable / Citable Points

1. "Shielded RL combines symbolic AI, which provides formal safety guarantees but has lower scalability, with sub-symbolic RL, which offers high scalability but lacks guarantees." (Key Insights box) — hybrid AI definition.
2. "A shield maintains a clear separation between an agent's safety and performance." (p. 82) — separation of concerns principle.
3. "By adjusting this threshold, shields can be generated that are either more liberal or more restrictive toward the agent." (p. 83) — ε-parameterised restrictiveness, closest concept to graduated governance.
4. "When using either shield that allows the agent to take some risk, the agent learns faster and achieves a higher reward compared to using no shield or a shield that completely forbids taking risks." (p. 88) — empirical evidence that intermediate restriction outperforms binary extremes.
5. "Shields with probabilistic guarantees may adapt their probability threshold dynamically based on the agent's performance and the state of the environment." (p. 86) — dynamic adaptation concept, unrealised precursor to state-conditioned governance.

---

### 16. Relation to My Research and Positioning

- **Governance implementation:** Level 1 fully implemented (winning region boundary). Level 2 partially implemented (per-state action filtering). No graduated governance modes.
- **State conditioning:** Safe action sets are state-conditioned (vary per state). But no discrete governance mode classification (SAFE/CAUTION/UNSAFE).
- **Two-level governance pair:** The shield is the strongest formal implementation of G(S) with per-state action sets. It is the closest existing mechanism to my governance pair but lacks: (a) discrete environmental mode classification, (b) advisory scope type restriction, (c) CAUTION mode.
- **Safety property:** Provides the strongest formal safety guarantee in the literature — absolute (never visit unsafe states) or probabilistic (P ≤ ε). Structurally analogous to Safety Dominance Property.
- **Gap my research addresses:** Shields provide per-action binary safety governance with formal guarantees. My architecture extends this in two directions: (a) classifying environmental states into discrete governance modes (S = f(E) → {SAFE, CAUTION, UNSAFE}) rather than per-state winning region analysis, and (b) restricting advisory scope *types* per mode (A_AI(S)) rather than filtering individual actions. The CAUTION mode — where AI participates but with restricted output types — has no shield equivalent.

**Positioning paragraph:** Könighofer et al. (2025) is one of the **⭐⭐⭐⭐⭐ core references** for my dissertation — the most formally rigorous AI safety governance mechanism in the literature. Published in Communications of the ACM, it provides an authoritative and accessible synthesis of the shielding research programme. Shields implement the archetypal Level 1 governance mechanism: a formally computed, model-based safety layer that classifies actions as safe/unsafe and prevents unsafe actions at runtime. The shield's state-dependent safe action sets are the closest existing mechanism to my governance pair (G(S), A_AI(S)), and the shield's safety guarantee (never visit unsafe states / P ≤ ε) is the closest to my Safety Dominance Property. The empirical finding that intermediate-restrictiveness shields (ε = 0.03, 0.05) outperform both no restriction and maximum restriction provides direct empirical motivation for the CAUTION state — intermediate governance levels improve both safety and performance. However, the shield operates at the per-action level (classifying individual actions as safe/unsafe) rather than the per-mode level (classifying environmental states into governance modes with different advisory scope types). My architecture extends the shield concept from per-action binary filtering to per-mode graduated governance, adding: (a) environmental state classification S = f(E), (b) two-level governance pair (G(S), A_AI(S)), and (c) the CAUTION mode where G(S) = 1 but A_AI(CAUTION) ⊂ A_AI(SAFE). The shield remains the primary formal baseline against which my governance architecture is positioned.

---

### 17. Overall Relevance Score

**⭐⭐⭐⭐⭐ Core — directly addresses the governance gap and implements the closest prior art for Level 1 governance**

**Justification:** This is one of the foundational references for my dissertation. It addresses four core themes (hybrid AI, safety-critical AI, AI governance, decision architecture formalisation) with the highest formal rigour in the literature. The shield is the primary baseline mechanism for my governance pair — the closest existing implementation of G(S) with per-state action filtering. The CACM venue gives it maximum citation credibility. The probabilistic shield results (intermediate ε outperforming extremes) provide direct empirical motivation for graduated governance. Confirmed at ⭐⭐⭐⭐⭐.

---

### Recommended Citation Uses

| Use | Section in dissertation | Specific point |
|---|---|---|
| Primary Level 1 governance baseline | Architecture comparison / baseline | Shield = archetypal binary per-action safety governance with formal guarantees |
| Hybrid AI archetype | Literature review — hybrid AI | "Combines symbolic AI (formal guarantees) with sub-symbolic RL (scalability)" |
| Safety guarantee baseline | Formalisation comparison | Absolute: never visit unsafe states. Probabilistic: P ≤ ε. Compare to Safety Dominance Property |
| Empirical motivation for CAUTION | Motivation for graduated governance | Intermediate-restrictiveness shields (ε = 0.03, 0.05) outperform both extremes |
| Dynamic adaptation as unrealised precursor | Gap identification | "Shields may adapt threshold dynamically based on state of environment" — mentioned but not formalised as state-conditioned governance modes |
| Winning region / state classification | Architecture comparison | Safe / dangerous / unsafe state classification — binary, not tripartite with intermediate mode |
| Pre-shielding safe action set as A_AI precursor | Formalisation comparison | Per-state safe action set is the closest existing concept to A_AI(S) — but per-action, not per-type |
