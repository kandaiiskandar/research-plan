## Literature Review Extraction: Li et al. (2026)

---

### 1. Paper Identity

- **Title:** Safety-Enhanced Deep Reinforcement Learning for Autonomous Driving: Dare to Make Mistakes to Learn Better and Faster
- **Authors:** Zhuoren Li, Bo Leng, Lu Xiong, Arno Eichberger, Chao Huang, Jia Hu
- **Year:** 2026 (accepted March 2026)
- **Venue:** IEEE Transactions on Intelligent Transportation Systems (early access)
- **DOI:** 10.1109/TITS.2026.3670584
- **Type:** System design paper with simulation-based evaluation (lane-change motion planning)

---

### 2. Core Contribution

- **Problem:** DRL for autonomous driving motion planning has three safety limitations: (i) sparse collision feedback makes learning safe policies difficult, (ii) safety-critical experiences are diluted in replay buffers, slowing convergence, and (iii) trained policies may still produce reckless actions in unfamiliar scenarios due to extrapolation errors.
- **Solution:** PSE-DRL (Predictive Safety Enhancement DRL) — a safety-enhanced DRL method with dynamic safety guidance for lane-change motion planning. Three key mechanisms: (1) *anticipated risk evaluation* identifying potentially unsafe behaviours before collisions, (2) *dangerous experience enhancement* via separate memory batches and prioritised sampling, (3) *reckless action prevention* via dynamic risk constraints that block unsafe actions and generate safe alternatives from the admissible action space.
- **Main contributions:**
  - Anticipated risk function J(s_t, a_t) evaluating future trajectory safety using uncertainty-weighted potential fields
  - Dynamic risk threshold J_thres(k) that tightens over training episodes (Eq. 9)
  - Safe action correction: when J(s_t, a_t) > J_thres, the unsafe action is blocked and a safe alternative a* is generated from A − a_t (Eq. 10)
  - Three separate memory batches (safe, collision, anticipated risk) with priority-weighted sampling
  - Simulation results: 92.31% CR reduction vs. baseline; PSE-DRL(on) achieves near-zero collision (0.06% CR)
- **Novelty:** Combines predictive risk evaluation with dynamic (episode-dependent) safety constraints and risk-prioritised experience replay. The "dare to make mistakes" philosophy allows the agent to explore dangerous states while recording and learning from them.

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | Partial | Combines deterministic safety constraints (risk threshold, safe action correction) with probabilistic DRL policy learning. The dynamic safety guidance module acts as a rule-based overlay on the DRL agent. However, the "hybrid" is safety-constrained RL training, not a governed decision support architecture |
| Safety-critical AI decision-making | Yes | Autonomous driving is explicitly safety-critical. Safety is the core design concern — the entire method is built around learning and enforcing safe driving policies |
| AI governance / control mechanisms | Partial | The dynamic risk constraint blocks unsafe actions and substitutes safe alternatives — a form of per-action governance. The SCMDP formulation defines a feasible policy set Π_c with hard safety constraints. However, governance is per-action binary (pass/correct), not state-conditioned scope restriction |
| Low-resource environments | No | High-compute DRL training on GPU servers; highway simulation environment |
| Decision architecture formalisation | Partial | SCMDP formulation with state-action cost J, feasible policy set Π_c, and constraint threshold J_thres. Anticipated risk function J(s_t, a_t) is formally defined (Eq. 3, 8). Dynamic threshold schedule (Eq. 9). However, formalisation serves RL training, not system-level governance architecture |
| Human role in decision-making | No | Fully autonomous system — no human decision-maker in the loop |
| Socio-technical evaluation | No | Simulation-only evaluation (Highway-env). No stakeholder or user involvement |
| Coastal fisheries / maritime domain | No | Autonomous highway driving domain |

**Mid-Extraction Relevance Gate:** 1 Yes, 3 Partial → **REDUCED EXTRACTION** (Sections 4–7, 12–13, 16–17)

---

### 4. Decision Architecture Analysis

- **Architecture:** DRL agent with embedded Predictive Safety Enhancement module. The agent generates trajectory actions; the safety module evaluates anticipated risk; if risk exceeds threshold, the action is blocked and a safe alternative is generated. This is a supervisory safety overlay on the RL policy.
- **Layered structure:** Two-layer: (a) DRL policy network generating candidate actions, (b) dynamic safety guidance module evaluating and correcting actions. The safety layer sits *after* the policy output (post-hoc correction) rather than *before* (pre-decision gating).
- **Rule-based constraints on AI:** Yes — the dynamic risk constraint (J(s_t, a_t) > J_thres) is a deterministic threshold applied to each action. When violated, the action is replaced by a safe alternative generated by minimising deviation from the original action while satisfying the risk constraint (Eq. 10). This is a deterministic safety override on probabilistic RL output.
- **Boundary between deterministic control and AI reasoning:** Clear separation. The DRL agent reasons probabilistically; the safety module applies deterministic risk thresholds. The safety module does not modify the RL training objective — it externally corrects unsafe actions.
- **Failure modes / fallback:** When an action is blocked, a safe alternative is generated from the admissible action space (A − a_t). The agent continues operating — never disabled entirely. No mode where the agent is blocked from acting at all.

**Critical architectural comparison:**

| Aspect | Li et al. (2026) | My DSR Architecture |
|---|---|---|
| **Governance trigger** | Per-action anticipated risk J(s_t, a_t) > J_thres | Environmental state classification S = f(E) |
| **Governance mechanism** | Binary per-action: pass or replace with safe alternative | Two-level: G(S) gates participation; A_AI(S) restricts advisory scope |
| **Governance granularity** | Binary per-action (safe/corrected) | Three-state graduated (SAFE/CAUTION/UNSAFE) |
| **Scope restriction** | No — AI always generates full-scope actions; only individual unsafe actions are corrected | Yes — A_AI(S) restricts what *types* of output AI may produce |
| **Dynamic threshold** | J_thres decreases over training episodes (design-time schedule) | (G(S), A_AI(S)) conditioned on runtime environmental state S |

---

### 5. Formal Model and Mathematical Representation

- **Formal elements:**
  - MDP tuple ⟨S, A, R, Z, γ⟩ (Eq. 1)
  - State-wise Constrained MDP (SCMDP): feasible policy set Π_c = {π ∈ Π | ∀(s_t, a_t), J(s_t, a_t) < J_thres} (Eq. 2)
  - Anticipated risk function J(s_t, a_t) = f_J(Tr^(e), Tr^(s)_j, U(Tr^(s)_j)) (Eq. 3, expanded in Eq. 8)
  - Dynamic risk threshold J_thres(k) with episode-dependent schedule (Eq. 9)
  - Safe action correction: a* = argmin_{a ∈ A−a_t} [½‖a − a_t‖² + λ_J(J(s_t, a) − J_thres)] (Eq. 10)
  - Uncertainty risk potential field U(t) with time-decaying amplitude A(t) (Eq. 7)
- **Comparison to DSR pipeline:** Structurally different purposes. Li et al. formalise RL training constraints (how to learn a safe policy); my pipeline formalises runtime governance (how deployed AI is governed). Their J(s_t, a_t) evaluates individual action safety; my S = f(E) classifies overall environmental state. Their J_thres is a training schedule parameter; my G(S) and A_AI(S) are runtime governance functions.
- **State-dependent recommendation restriction:** Not present. The AI always generates full-scope actions (lane change, acceleration, etc.). Unsafe individual actions are corrected, but the *types* of action the AI may generate are never restricted by state.
- **Safety Dominance Property equivalent:** The SCMDP constraint (∀(s_t, a_t), J(s_t, a_t) < J_thres) is a per-action safety bound — ensuring each action falls within risk limits. This is analogous in spirit to AI(E) ⊆ A_AI(S) but operates per-action (bounding individual action risk) rather than per-state (bounding the admissible action space by classified environmental state).

---

### 6. Safety State Classification

- **Discrete safety levels:** Not defined as environmental state classification. The anticipated risk J(s_t, a_t) is continuous; the threshold J_thres creates a binary split (safe/unsafe) per action. There are no discrete environmental safety states like {SAFE, CAUTION, UNSAFE}.
- **Comparison to S = f(E):** The anticipated risk function evaluates the safety of a *specific action in a specific state*, not the safety of the *environment as a whole*. There is no environmental state classification function.
- **AI recommendation scope across safety levels:** Not differentiated. The AI always proposes from the full action space. Unsafe actions are corrected individually; the action space is never restricted.

---

### 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (G(S)) | No | AI always operates. Individual actions may be corrected, but the AI is never disabled |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | No | AI always proposes from full action space. No restriction on action *types* by state |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | No | No environmental state classification. Governance is per-action risk evaluation |

- **Governance type:** **Per-action binary correction.** Each action is individually evaluated against a risk threshold; unsafe actions are replaced with the closest safe alternative. This is neither Level 1 (AI participation) nor Level 2 (advisory scope) governance — it is per-action output correction, structurally similar to the gatekeeper in Liang et al. (2025) but applied at the action level rather than the output level.
- **Relation to two-level governance pair:** The SCMDP's admissible action concept (a* from A − a_t satisfying J constraints) is the closest formal element to my admissible action space A_AI(S). However, their "admissible" means "safe enough per action" while mine means "permitted action types given classified environmental state." The fundamental difference: their governance is action-level and risk-continuous; mine is state-level and mode-graduated.

---

### 12. Key Concepts and Definitions

- **State-wise Constrained MDP (SCMDP):** RL formulation requiring safety constraints to be satisfied at every exploration step (hard constraint), with feasible policy set Π_c defined by per-action cost bound J(s_t, a_t) < J_thres.
- **Anticipated risk evaluation:** Forward-looking risk assessment based on predicted future trajectories of ego vehicle and surrounding vehicles, using Gaussian uncertainty potential fields with time-decaying amplitude. Captures risk from actions that may *lead to* collisions, not just collision events themselves.
- **Dynamic risk constraint:** Safety threshold J_thres(k) that decreases over training episodes — permissive early (allowing exploration) and strict late (enforcing convergence to safe policy). Training-time schedule, not runtime state-conditioned governance.
- **Safe action correction:** When action exceeds risk threshold, replace with closest feasible alternative: a* = argmin [½‖a − a_t‖² + λ_J(J(s_t, a) − J_thres)]. Minimises deviation from original intent while satisfying safety constraint.
- **Risk experience enhancement:** Separate memory batches for safe, collision, and high-risk experiences, with priority-weighted sampling based on anticipated risk and scene similarity. Makes dangerous experiences more influential during training.

---

### 13. Limitations and Unsolved Problems

- **Stated limitations:**
  - Trajectory parameterisation could be more expressive for flexible manoeuvres
  - Online safety constraint data could be used for online policy updating (future work)
- **Observable limitations:**
  - Simulation-only (Highway-env with MOBIL/IDM surrogate vehicles) — no real-world deployment
  - Per-action binary governance only — no graduated governance across environmental states
  - No environmental state classification — risk is evaluated per-action, not per-environmental-condition
  - No scope restriction — AI always proposes from full action space; only individual actions corrected
  - Dynamic threshold is a training schedule (episode-dependent), not a runtime governance mechanism conditioned on environmental state
  - Fully autonomous — no human decision-maker, no decision support framing
- **Alignment with my research gaps:**
  - Confirms per-action binary safety correction as the dominant paradigm in safe RL for autonomous driving
  - No CAUTION-equivalent mode — actions are either passed or corrected; no intermediate restriction of action types
  - No environmental state classification — risk is continuous and per-action, not classified into discrete governance modes
  - The "admissible action space" concept (A − a_t satisfying J constraints) is structurally related to my A_AI(S) but operates differently (per-action feasibility vs. state-conditioned scope)

---

### 16. Relation to My Research and Positioning

- **Governance implementation:** Per-action binary correction (neither Level 1 nor Level 2 in my taxonomy).
- **State conditioning:** Not implemented at the environmental level. The dynamic threshold is training-schedule-dependent, not runtime-state-dependent.
- **Two-level governance pair:** Not approached. The SCMDP admissible action concept is formally related but functionally different.
- **Safety property:** SCMDP constraint (∀(s_t, a_t), J < J_thres) — per-action risk bound, not per-state containment.
- **Gap my research addresses:** Li et al. demonstrate sophisticated safety mechanisms for RL training and deployment — anticipated risk evaluation, dynamic constraints, safe action correction — all operating at the per-action level. The environmental safety state is never classified; governance never varies by classified state; the AI's action space is never restricted by type. My architecture fills this gap by introducing state-level governance: S = f(E) classifies environmental conditions, and the governance pair (G(S), A_AI(S)) restricts AI participation and scope by classified state — a fundamentally different governance granularity.

**Positioning paragraph:** Li et al. (2026) is a **cross-domain reference for per-action safety governance in autonomous systems**, published in a top-tier IEEE transactions venue. The paper demonstrates the state of the art in safe RL for autonomous driving: anticipated risk evaluation with predictive trajectories, dynamic safety constraints, and safe action correction from an admissible action space. These mechanisms represent sophisticated per-action binary governance — each action is individually evaluated and corrected if unsafe. However, the approach operates entirely at the action level: no environmental state classification, no graduated governance modes, no restriction of action *types* by state. The SCMDP formulation (feasible policy set Π_c with per-action cost bounds) provides a formal baseline for comparison with my state-conditioned governance pair (G(S), A_AI(S)). The paper is citable as: (a) evidence that even advanced safe RL systems default to per-action binary correction rather than state-conditioned graduated governance, (b) a formal baseline (SCMDP feasible policy set) for comparison with my state-conditioned admissible action space, and (c) a cross-domain example from automotive AI confirming the binary governance gap. The paper is well-published (IEEE T-ITS) and methodologically rigorous, making it a credible cross-domain citation.

---

### 17. Overall Relevance Score

**⭐⭐⭐ Medium**

**Justification:** The paper addresses safety-critical AI (Yes) and partially addresses hybrid AI, AI governance, and decision architecture formalisation. It is methodologically strong (IEEE T-ITS, comprehensive simulation, ablation studies) and provides a formal SCMDP framework for per-action safety. Its per-action binary correction paradigm confirms the governance gap my architecture addresses, and its admissible action space concept provides a formal comparison point. However, it operates in a different domain (autonomous driving), at a different governance level (per-action rather than per-state), and with a different system framing (autonomous control rather than decision support). Elevated from ⭐⭐ to ⭐⭐⭐ for: (a) formal SCMDP framework providing a comparison baseline, (b) top-tier venue credibility, and (c) the fact that even sophisticated safe RL defaults to per-action binary governance — direct evidence for the graduated governance gap.

---

### Recommended Citation Uses

| Use | Section in dissertation | Specific point |
|---|---|---|
| Per-action binary governance evidence (automotive) | Research gap — binary governance gap | Even advanced safe RL (SCMDP, anticipated risk, dynamic constraints) defaults to per-action pass/correct — no state-conditioned graduated governance |
| SCMDP as formal comparison baseline | Formalisation chapter | SCMDP feasible policy set Π_c with ∀(s_t, a_t), J < J_thres contrasts with state-conditioned A_AI(S) — per-action vs. per-state governance |
| Admissible action space concept | Architecture comparison | Safe action correction from A − a_t (per-action feasibility) vs. A_AI(S) (state-conditioned type restriction) — different meanings of "admissible" |
| Dynamic threshold as training schedule | Gap identification | J_thres(k) is episode-dependent training parameter, not runtime state-conditioned governance — illustrates the design-time vs. runtime gap |
