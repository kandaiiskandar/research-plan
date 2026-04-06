## Literature Review Extraction
### Odriozola-Olalde, Zamalloa & Arana-Arexolaleiba (2023) — Shielded Reinforcement Learning

---

### 1. Paper Identity

- **Title:** Shielded Reinforcement Learning: A review of reactive methods for safe learning
- **Authors:** Haritz Odriozola-Olalde, Maider Zamalloa, Nestor Arana-Arexolaleiba
- **Year:** 2023
- **Venue:** 2023 IEEE/SICE International Symposium on System Integration (SII)
- **DOI:** 10.1109/SII55687.2023.10039301
- **Type:** Review / survey paper

---

### 2. Core Contribution

- **Problem:** RL algorithms show promise in simulation but lack functional safety guarantees for deployment in real-world safety-critical applications. Existing functional safety standards (e.g., IEC 61508) do not cover AI-based controllers.
- **Proposed solution:** A structured review and classification of ShieldedRL methods — reactive safety mechanisms that filter unsafe agent actions at runtime using a shield synthesised from safety specifications and environment dynamics.
- **Main contributions:**
  1. Categorisation of shielded RL methods into three Safety Levels (I/II/III) based on constraint compliance guarantees (soft, probabilistic, hard)
  2. Discussion of advantages and disadvantages of each reviewed method
  3. Identification of shortcomings — particularly vulnerability to environment dynamics changes, sim-to-real gap, and the "hidden unsafe states" problem
- **Novelty:** The paper does not propose a new method but provides the first structured taxonomy of shielding approaches mapped to Safety Levels and identifies a critical vulnerability: when environment dynamics change drastically, a Safety Level III shield can degrade to Safety Level I because its model becomes outdated.

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | **Yes** | Shielding is inherently hybrid: a deterministic rule/constraint layer (shield) governs a probabilistic learning agent (RL). The shield enforces safety specifications while the RL agent optimises reward. |
| Safety-critical AI decision-making | **Yes** | Central focus. The entire review is about ensuring functional safety of RL agents in safety-critical applications, with explicit reference to IEC 61508 and industrial deployment requirements. |
| AI governance / control mechanisms | **Yes** | Shielding is a runtime AI governance mechanism — the shield controls whether the agent's proposed action reaches the environment. This is Level 1 participation governance (G(S)) in my framework. |
| Low-resource environments | **Partial** | Not the focus, but the paper notes that shielding's reactive nature has minimal computational overhead (only acts when needed), making it a candidate for embedded systems. |
| Decision architecture formalisation | **Partial** | Formalises the problem as CMDP (Constrained MDP) with tuple ⟨S, A, P, R, γ, C⟩. Defines safe policy subspace Γ ⊆ Π. Individual methods use formal specifications (LTL, safety games, reach-avoid). However, no unified governance formalisation comparable to (G(S), A_AI(S)). |
| Human role in decision-making | **No** | Entirely autonomous agent-environment loop. No human decision-maker in the architecture. |
| Socio-technical evaluation | **No** | No socio-technical evaluation. All methods evaluated in simulation only. |
| Coastal fisheries / maritime domain | **No** | No maritime or fisheries application. Domains include GridWorld, cart-pole, PAC-MAN, collaborative robotics. |

**Mid-Extraction Relevance Gate:** 3 Yes + 2 Partial = **≥ 3 Yes → FULL EXTRACTION**

---

### 4. Decision Architecture Analysis

- **Architecture structure:** The shielded RL architecture is a **supervisory intercept pattern** — the shield sits between the agent's action output and the environment's action input (see Figure 1 in paper):
  ```
  Environment → (state, reward) → Learning Agent → action → Shield → safe action → Environment
  ```
- **Safety constraint mechanism:** The shield is synthesised from safety specifications (typically LTL properties) and an environment model. It evaluates each proposed action against these constraints before allowing it to pass.
- **Rule-based constraints before AI:** Yes — the shield acts as a deterministic filter *after* the RL agent proposes an action but *before* it reaches the environment. Safety is enforced deterministically; the RL agent is not trusted to self-regulate.
- **Boundary between deterministic and AI reasoning:** Clearly defined. The RL agent handles reward optimisation (probabilistic). The shield handles safety enforcement (deterministic/formal). The shield has override authority — it can replace any agent action with a known safe action.
- **Failure modes and fallback:**
  - **Model Predictive Shielding:** Uses a backup policy (recovery policy → equilibrium policy) as fallback when recoverability cannot be guaranteed
  - **Base Shielded RL:** Uses a safety-game formulation to compute winning regions; actions outside winning regions are replaced
  - **Critical shortcoming identified:** When environment dynamics change drastically, the shield's model becomes outdated, and previously safe actions may now lead to unsafe states. The shield degrades from Safety Level III to Safety Level I during the adaptation period.

---

### 5. Formal Model and Mathematical Representation

- **Formal model:** Yes — the problem is formalised as a Constrained Markov Decision Process (CMDP):
  - MDP tuple: ⟨S, A, P, R, γ⟩
  - CMDP tuple: ⟨S, A, P, R, γ, C⟩ where c_i ∈ C, c_i: S × A × S → ℝ are constrained cost functions
  - Safe policy subspace: Γ ⊆ Π (only policies satisfying constraints C)
- **Shield formalisms vary by method:**
  - **Base Shielded RL (Alshiekh et al.):** Finite Mealy machine + LTL safety specifications + safety-game for shield synthesis. Winning region computed; shield synthesised from winning strategy.
  - **ShieldPPO:** Tabular shield S_T(s,a) = {1 if (s,a) ∉ T; 0 otherwise} where T stores catastrophic state-action pairs. Labelling function L_ϕ: S × A → {0,1}.
  - **Probabilistic Shield:** δ-shield using LTL properties, value iteration/linear programming for probability computation. Action blocked if it increases constraint violation probability beyond threshold δ.
  - **POMDP Shielding:** Reach-avoid specifications φ = ⟨REACH, AVOID⟩ with belief function b over states.
- **Comparison to my pipeline E → S = f(E) → (G(S), A_AI(S)) → AI(E):**
  - Shielding formalises the agent-environment interaction (MDP/CMDP) but does **not** formalise a state classification function S = f(E) that maps environmental conditions to discrete safety states.
  - Shielding operates on individual state-action pairs, not on classified environmental safety states.
  - There is no equivalent to A_AI(S) — no formal restriction of the admissible recommendation space as a function of safety state.
  - The shield implements G(s,a) ∈ {0,1} per action, not G(S) ∈ {0,1} per safety state.
- **State-dependent recommendation restriction:** **No.** The shield does not reduce the agent's action space as a function of classified state. It evaluates each action independently. The agent is free to propose any action; the shield only blocks individually identified unsafe ones.
- **Safety Dominance Property equivalent:** **Partial.** Safety Level III methods guarantee that no unsafe action reaches the environment (analogous to a per-action safety guarantee). However, this is not formalised as AI(E) ⊆ A_AI(S) — it's formalised as "the shield's winning strategy ensures only safe states are visited." The guarantee is over state trajectories, not over a classified-state-conditioned admissible output space.
- **Formalisation purpose:** Mixed — CMDP is used for analysis and proof (particularly for Safety Level III methods where winning regions are formally computed). Safety Level I methods use formalisation more descriptively.

---

### 6. Safety State Classification

- **Discrete risk/safety levels:** Yes — the paper references a three-zone safety model (from [10], Ro et al. 2022):
  1. **Safe states** — environment is safe w.r.t. imposed constraints
  2. **Unsafe states** — environment violates safety constraints
  3. **Hidden unsafe states** — constraints are technically met, but *every* action a ∈ A leads to an unsafe state or another hidden unsafe state (points of no return)
- **Additionally**, the paper adopts a three-level Safety Level taxonomy (from [8], Brunke et al. 2021):
  - **Safety Level I (Soft Constraints):** Agent encouraged to comply; no guarantee. Penalty-based.
  - **Safety Level II (Probabilistic Constraints):** Maximum violation probability bounded by threshold.
  - **Safety Level III (Hard Constraints):** Agent must comply at all times. Zero-violation guarantee.
- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:**
  - The three-zone model (safe / hidden unsafe / unsafe) is a **state-space partition**, not an **environmental state classification**. It classifies regions of the MDP state space based on reachability analysis, not based on environmental input variables (wind, marine conditions, etc.).
  - The Safety Levels (I/II/III) classify **methods**, not **operational states**. They describe the degree of guarantee a shielding method provides, not the current environmental condition.
  - Neither classification maps to a runtime state classification function S = f(E) that conditions governance behaviour.
- **Critically:** The paper does **not** differentiate the AI's recommendation scope across safety levels. The shield either allows or blocks an action — the same binary operation regardless of whether the system is in a "safe" or "borderline" region. There is no CAUTION mode where the agent participates but with restricted output types.

---

### 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (G(S)) | **Yes** | The shield controls whether each proposed action reaches the environment. If blocked, a safe replacement action is applied. This is per-action participation governance. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | **No** | No method restricts the *types* or *categories* of actions the agent may propose based on classified state. The shield evaluates individual actions post-hoc. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | **No** | No environmental state classification function exists. No unified governance pair. |

- **Binary AI switch vs. graduated governance:** All shielded RL methods implement a **binary switch per action** — allow or block. This is Level 1 governance only. No graduated model exists.
- **Level 2 governance:** Absent. No state-conditioned restriction on the action space.
- **Support for two-level governance pair:** The paper **supports the need** for it indirectly:
  - The "hidden unsafe states" concept reveals that binary allow/block is insufficient — the agent can be in a technically "safe" state where all actions eventually lead to disaster. This is precisely the scenario where CAUTION-mode scope restriction would add value: rather than allowing the agent full action scope in a borderline state, restrict it to conservative actions.
  - The Safety Level degradation problem (Level III → Level I during environment change) also motivates graduated governance — rather than maintaining full trust or no trust, a graduated mechanism could reduce trust (restrict scope) during periods of model uncertainty.

---

### 8. Human Role in Decision-Making

- **Human involvement:** None. The architecture is fully autonomous — agent proposes actions, shield filters, environment receives safe action. No human is in the loop.
- **Decision support vs. automation:** Pure **decision automation**. The agent acts on the environment directly.
- **Human override:** Not addressed. The shield is the override mechanism, but it is automated, not human-initiated.
- **Relevance to my research:** My architecture is explicitly **decision support** (human decides). The shielded RL paradigm operates at a fundamentally different level — it governs an autonomous agent, not a human decision-maker. This is a categorical difference that should be noted when citing this paper.

---

### 9. System Constraints and Environment

- **Real-world constraints:** The paper explicitly acknowledges a major gap: all reviewed methods are tested only in simulation, in low-dimensional, deterministic environments (GridWorld, cart-pole, PAC-MAN). None has been validated in real industrial applications.
- **Deployment context:** Simulation only. The paper calls for higher-complexity benchmarks closer to industrial conditions and identifies sim-to-real gap as a critical unresolved problem.
- **Resource-aware design:** Shielding is noted as computationally lightweight (reactive — only intervenes when needed), making it suitable for embedded systems. However, some methods (Centralised Shield, POMDP Shielding) have high computational cost for shield synthesis.
- **Edge cases:** The paper identifies a critical edge case — drastic environment dynamics change renders the shield's model outdated, degrading safety guarantees. The "hidden unsafe states" represent another edge case where the shield is structurally unable to prevent eventual constraint violation.

---

### 10. Hybrid AI Taxonomy

- **Hybrid AI type:** **Supervisory control** — the RL agent (probabilistic) is supervised by the shield (deterministic/formal). The shield has override authority.
- **Safety enforcement position:** **After AI reasoning** — the shield intercepts the agent's proposed action post-hoc. The agent reasons freely; the shield filters the output.
- **Two-level governance support:** **No.** The hybrid approach supports single-level binary control only. The shield governs participation (allow/block) but not advisory scope. All methods implement the same binary filter regardless of state classification.
- **Comparison to my architecture:** My architecture places deterministic safety governance *before* AI reasoning (gate-first design: E → S = f(E) → G(S) determines whether AI even runs). Shielded RL places governance *after* AI reasoning (the agent always runs; the shield filters its output). Additionally, my architecture governs at two levels (participation + scope); shielding governs at one level (participation per action).

---

### 11. Baseline Comparison and Evaluation

- **Baseline comparison:** Individual methods compare shielded vs. unshielded RL agents. Base Shielded RL compares shield with and without negative reward feedback.
- **Metrics:** Safety violations (number of unsafe actions), convergence speed, reward obtained, computational cost. No formal safety property verification comparable to Safety Dominance Property.
- **Evaluation type:** Simulation only. GridWorld, cart-pole, PAC-MAN, collaborative robotics simulation.
- **CAUTION zone testing:** **No.** No method tests behaviour in a restricted-scope intermediate zone. Testing is binary: safe actions pass, unsafe actions are blocked.
- **Safety Dominance Property verification:** Not formally. Safety Level III methods claim zero constraint violations in tested environments, but this is empirical, not a formally verified property over a classified-state-conditioned output space.
- **Graduated vs. binary governance comparison:** **No.** The paper does not compare graduated and binary governance approaches because no graduated approach is reviewed.
- **Evaluation gaps:** Simulation-only testing, low-dimensional environments, no real-world deployment, no testing under dynamic environment changes, no evaluation of intermediate/graduated safety modes.

---

### 12. Key Concepts and Definitions

| Concept | Definition / Relevance |
|---|---|
| **Shielded RL** | A reactive safety method where a shield filters unsafe agent actions at runtime, only intervening when needed. Minimum interference principle. |
| **Constrained MDP (CMDP)** | MDP extended with constraint cost functions C. Reduces policy space Π to safe subspace Γ. Formal basis for safe RL. |
| **Safety Levels I/II/III** | Taxonomy from Brunke et al. (2021): Soft constraints (Level I, no guarantee), Probabilistic constraints (Level II, bounded violation probability), Hard constraints (Level III, zero violations). |
| **Hidden unsafe states** | States where imposed safety constraints are met but every possible action leads to an unsafe state or another hidden unsafe state. Points of no return. From Ro et al. (2022). |
| **Minimum interference principle** | The shield should ensure safety with minimum intervention — only acting when necessary, preserving agent autonomy otherwise. |
| **Safety-game** | A two-player game (environment vs. agent) used to synthesise the shield. The winning region defines the state set from which a winning (safe) strategy exists. |
| **δ-shield** | Probabilistic shield that blocks actions increasing constraint violation probability beyond threshold δ. |
| **Shield degradation** | When environment dynamics change, the shield's model becomes outdated, and Safety Level III can degrade to Safety Level I during the adaptation period. |

---

### 13. Limitations and Unsolved Problems

- **Stated limitations:**
  1. All methods tested only in low-dimensional simulated environments — large gap with real industrial applications
  2. Shield models depend on accurate environment dynamics; drastic environment changes degrade safety guarantees
  3. Sim-to-real gap means simulation-safe agents are not guaranteed to be real-world-safe
  4. Hidden unsafe states are structurally unresolvable by binary shielding — the shield cannot prevent the agent from entering states where all future actions lead to unsafe outcomes
  5. Functional safety standards (IEC 61508) lack procedures for AI-based control systems
  6. MARL shielding methods are all Safety Level I — insufficient for industrial standards

- **Unsolved problems:**
  1. Methodology to mitigate vulnerability during transient periods (environment dynamics change) — proposed as a new research line
  2. Verification and validation methodology for real-world deployment of shielded RL
  3. Updating functional safety standards to include AI-based controller requirements
  4. Scaling shielded RL to high-dimensional, stochastic, real-world environments

- **Gaps aligned with my research:**
  - **Two-level governance gap:** All reviewed methods implement Level 1 (per-action allow/block) only. No method restricts the admissible action space based on classified environmental state (Level 2). My architecture's A_AI(S) addresses this directly.
  - **CAUTION mode gap:** No intermediate mode exists where the agent participates with restricted scope. The "hidden unsafe states" problem motivates exactly this — in borderline states, restricting scope rather than allowing full action freedom or blocking entirely.
  - **Safety Dominance Property gap:** No formal property guarantees that all AI outputs fall within a state-conditioned admissible space. Safety Level III provides trajectory-level guarantees, not output-scope guarantees.
  - **Environmental state classification gap:** No method classifies environmental conditions into discrete safety states that condition governance. Shielding evaluates individual state-action pairs, not the overall environmental safety context.

---

### 14. Methodology Notes

- **Research method:** Systematic literature review with taxonomic classification. Methods categorised along multiple dimensions: Safety Level, environment characteristics (sim/real, dimensionality, deterministic), and feedback mechanism.
- **DSR alignment:** Partial. The paper reviews design artifacts (shields) but does not follow a DSR pipeline. It is a review, not a design contribution.
- **Informing my research:**
  - The three Safety Levels taxonomy provides a useful classification lens for comparing my graduated governance approach against existing shielding methods
  - The "hidden unsafe states" concept from reference [10] could strengthen my motivation for the CAUTION mode — these are precisely the states where binary governance fails and graduated scope restriction is needed
  - The shield degradation scenario (Level III → I under environment change) provides an argument for environmental-state-conditioned governance rather than model-dependent action-level filtering

---

### 15. Quotable / Citable Points

1. **Definition of Shielded RL:** "The use of a shield is proposed, which acts as a filter that allows only those actions that are identified as safe and if safety requirements/constraints cannot be guaranteed, a safe action is provided." (Section I, p.1) — Establishes the binary nature of shielding.

2. **Minimum interference principle:** "Shielding is a reactive method, i.e., it only takes part in those time-steps where it foresees that the action chosen by the agent will lead to a violation of the constraints associated with safety." (Section III, p.3) — Confirms shielding intervenes reactively, not proactively.

3. **Hidden unsafe states:** "[There is] a third zone, the hidden unsafe states, which corresponds to those states where even if the imposed safety constraints are met, any action a ∈ A leads to an unsafe state or another hidden unsafe state." (Section VI, p.7) — Motivates CAUTION mode; binary safe/unsafe is insufficient.

4. **Shield degradation under dynamics change:** "As the model associated with the shield corresponds to the instants before the unusual event, the shield will continue to identify the action as safe, which leads to the environment ending up in a catastrophic state... the algorithm used is now Safety Level I." (Section VI, p.7) — Motivates environmental-state-conditioned governance.

5. **Simulation-only limitation:** "The experimentation to obtain the results has been carried out in low-dimensional, deterministic environments that do not fit to real industrial applications conditions or requirements." (Section V, p.6) — Supports low-resource deployment gap argument.

---

### 16. Relation to My Research and Positioning

- **Level 1 governance:** **Yes** — shielding is the canonical example of Level 1 participation governance. Every method reviewed implements a binary allow/block gate for individual actions.
- **Level 2 governance:** **No** — no method restricts the agent's admissible action space as a function of classified environmental state.
- **State-conditioned:** **No** — shields evaluate individual state-action pairs, not classified environmental safety states.
- **Two-level governance pair proximity:** The paper demonstrates the state of the art in Level 1 governance but explicitly does not reach Level 2. No method comes close to a unified (G(S), A_AI(S)) pair.
- **Safety Dominance Property:** **No formal equivalent.** Safety Level III provides trajectory-based guarantees (no unsafe states visited), not output-scope-based guarantees (AI outputs ⊆ admissible space).
- **Gap my research addresses:** The entire shielded RL paradigm operates at Level 1 only — binary per-action filtering. My architecture adds Level 2 (state-conditioned scope restriction) and unifies both levels under a classified environmental safety state. The "hidden unsafe states" problem identified in this paper is precisely the class of scenarios where CAUTION-mode scope restriction adds value beyond binary shielding.

**Positioning paragraph:** This review paper provides a comprehensive survey of shielded RL methods that collectively represent the strongest form of Level 1 participation governance in the safe AI literature. It confirms that all surveyed shielding methods implement binary allow/block action filtering — none restricts the agent's admissible output scope based on classified environmental state. The paper's identification of "hidden unsafe states" (where binary shielding is structurally insufficient) and shield degradation under environment dynamics change directly motivates the need for graduated, state-conditioned governance. This paper should be cited in Section 2.2 (safety-critical AI governance mechanisms) as evidence that even the most formally rigorous shielding methods remain limited to Level 1 governance, and in the research gap section as supporting the absence of Level 2 advisory scope governance across the shielded RL literature. The "hidden unsafe states" concept may also be referenced in the architecture design rationale for the CAUTION mode.

---

### 17. Overall Relevance Score

**⭐⭐⭐ Medium**

Strong background reference for Level 1 governance (shielding paradigm), with the "hidden unsafe states" concept and shield degradation scenario providing useful motivation for graduated governance. Does not directly address the two-level governance gap or implement anything close to A_AI(S), but comprehensively confirms the binary nature of the shielding literature. Useful for Sections 2.2 (governance mechanisms) and 2.3 (research gap evidence). The three Safety Levels taxonomy (Brunke et al.) and the three-zone state model (Ro et al.) are independently useful references to trace back to the original sources.
