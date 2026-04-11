## Literature Review Extraction — GAP-FOCUSED
### Hamel-De le Court, Belardinelli & Goodall (2025) — Probabilistic Shielding for Safe Reinforcement Learning

---

### 1. Paper Identity

- **Title:** Probabilistic Shielding for Safe Reinforcement Learning
- **Authors:** Edwin Hamel-De le Court, Francesco Belardinelli, Alexander W. Goodall
- **Affiliation:** Imperial College London ({e.hamel-de-le-court, francesco.belardinelli, a.goodall22}@ic.ac.uk)
- **Year:** 2025
- **Venue:** The Thirty-Ninth AAAI Conference on Artificial Intelligence (AAAI-25), pp. 16091–16099
- **DOI:** 10.1609/aaai.v39i15.33767
- **Type:** Conference paper (peer-reviewed, top-tier AI venue)
- **URL:** https://ojs.aaai.org/index.php/AAAI/article/view/33767
- **Funding:** EPSRC grant EP/X015823/1 ("An abstraction-based technique for Safe Reinforcement Learning")
- **Citation Quality:** ✅ Top-tier AI venue (AAAI). Peer-reviewed. Full text verified from PDF.

---

### 2. Core Contribution

- **Problem:** In Safe RL, an agent must maximise cumulative reward while satisfying a safety constraint (probabilistic state-avoidance). Existing approaches providing strict safety guarantees rely on Linear Programming (Karmarkar 1984), which has limited scalability. Policy-based approaches (PPO-Lagrangian, CPO) lack strict formal guarantees.
- **Proposed solution:** A new shielding approach based on state-augmentation of the MDP. For a finite MDP with known safety dynamics, the method computes an inductive ε-upper bound β of β_M (the minimal probability of reaching an unsafe state), then constructs a shield Sh^{≤p}_β(M) that augments each state (s, q) with a "safety level" q ∈ [β(s); 1] representing the maximal probability of reaching an unsafe state.
- **Key mechanism:** The shield is defined as a new MDP where states are (s, q) pairs and actions are probability distributions (α, v) that must satisfy two conditions: (1) predictions must be coherent — the expected next safety level must be ≤ current safety level q; (2) predictions cannot be less than the ε-upper bound β. The shield restricts the agent to actions satisfying these conditions. Any memoryless policy in the shielded MDP is guaranteed safe (Theorem 1: Sh^{≤p}_β(M)_π ⊨ P_{≤p}(Reach(u))). The approach also preserves optimality (Theorem 2).
- **Four contributions:** (1) Shield design via safety-aware state-augmentation; (2) formal proof the shield makes exploration safe; (3) proof that finding optimal safe policy reduces to finding optimal policy in the shield; (4) practical implementation via encoded MDP for gym environments.
- **Evaluation:** Five gridworld/game environments (Media streaming, Colour bomb v1/v2, Bridge crossing v1/v2, Pacman). PPO-Shield guarantees safety throughout training and test, significantly outperforms CPO and PPO-Lagrangian on both safety and reward.

---

### 3. Governance Mechanism Analysis

| Property | Assessment |
|---|---|
| **Governance type** | **Binary** — actions are either permitted or blocked by the shield. The shield constructs a polytope C^{s,q}_α of safe probability distributions over actions; any distribution outside this polytope is forbidden. Within the polytope, all actions are equally "permitted" — there is no graduated restriction. |
| **Trigger** | Agent's current state (s, q) in the augmented MDP, where s is the original state and q is the current "safety level" (maximal probability of reaching unsafe state). The safety level q is continuous in [β(s); 1], not discrete. |
| **Intermediate mode?** | **No** — the paper explicitly labels states as **s** (safe) and **u** (unsafe) only (p. 16091: "some states are labelled unsafe, and the safety we consider consists in avoiding those unsafe states"). The safety level q is a continuous tracking variable, not a discrete governance mode. There is no CAUTION equivalent — no state where the agent operates under qualitatively different governance rules. |
| **Environmental conditioning?** | **No** — the shield is conditioned on the agent's state within the MDP (s, q), not on a classified external environmental state variable. The MDP's safety dynamics are assumed known and fixed. |
| **Advisory scope restriction?** | **No** — the shield restricts which probability distributions over actions are permitted at each (s, q). It does not restrict categories or types of recommendations. All action types remain available if they fall within the safe polytope. No Level 2 governance. |
| **Runtime adaptation?** | The shield operates at runtime and the safety level q changes with each transition, but the governance mechanism is always the same: enforce the polytope constraint. The *type* of governance does not change — only the *boundary* shifts. |

---

### 4. Governance Level Analysis

| Level | Question | Implemented? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI act at all? (G(S)) | **Yes (binary)** | Shield permits or blocks each action. If all actions are blocked, the agent cannot act. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | **No** | No concept of restricting recommendation types or categories based on environmental state. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | **No** | Governance is per-action within the MDP, not per-environmental-state-mode. |

---

### 5. Gap Evidence for Novelty Argument

**Key finding:** This paper represents the most recent (2025) formal shielding work published at a top-tier AI venue (AAAI). The probabilistic shield provides the strictest formal safety guarantees in the shielding literature — Theorem 1 proves any memoryless policy in the shielded MDP is safe, and Theorem 2 proves optimality is preserved. Yet the governance decision remains strictly binary: states are labelled **s** (safe) or **u** (unsafe) only. The continuous safety level q tracks *how close* the agent is to unsafe states, but this does not create intermediate governance modes — it only adjusts the safe action polytope boundary.

**The safety level q is NOT a CAUTION mode.** An examiner might argue that the continuous safety level q ∈ [β(s); 1] provides graduated governance, since different q values produce different safe action sets. The rebuttal: q adjusts the *quantitative boundary* of the same binary governance mechanism (the polytope constraint). It does not create qualitatively different governance regimes. At every q value, the governance question is the same: "is this action distribution within the safe polytope?" There is no q value at which the system switches to restricting *types* of recommendations rather than individual actions. The proposed architecture's CAUTION mode is qualitatively different from SAFE — it restricts recommendation *categories* (e.g., no far-offshore trips), not just individual action probabilities.

**Critical distinction from proposed architecture:** The shield evaluates individual state-action probability distributions for safety. The proposed architecture classifies the *entire environmental state* into discrete governance modes (SAFE/CAUTION/UNSAFE) and applies categorically different governance at each mode — not just tighter polytope boundaries but different *types* of advisory restrictions. The probabilistic shield has no mechanism equivalent to A_AI(CAUTION) ⊂ A_AI(SAFE) where the containment is over recommendation *types*, not action probabilities.

**Use in justification:** Cite as evidence that even the most formally rigorous shielding method (AAAI 2025, Imperial College London, with Theorems 1 and 2 providing strict safety and optimality guarantees) implements binary state classification (safe/unsafe) with a continuous safety tracking variable — not discrete governance modes with qualitatively different advisory scope. Strengthens PS1 (no intermediate AI participation mode) and PS2 (no state-conditioned (G(S), A_AI(S))). Particularly powerful because the continuous safety level q is the closest mechanism in the shielding literature to graduated governance, yet it remains fundamentally binary in governance type.

---

### 6. Theme Relevance

| Theme | Match? | Notes |
|---|---|---|
| T1: Hybrid AI | ⚠️ Partial | Shield is rule-based wrapper over RL agent |
| T2: Safety-critical AI | ✅ Yes | Core focus — formal safety guarantees |
| T3: AI governance | ✅ Yes | Binary action-level governance |
| T4: Low-resource environments | ❌ No | No resource constraint discussion |
| T5: Decision architecture formalisation | ✅ Yes | State-augmented MDP with probabilistic safety proofs |
| T6: Human role | ❌ No | No human-in-the-loop |
| T7: Socio-technical evaluation | ❌ No | Formal/simulation evaluation only |
| T8: Coastal fisheries / maritime | ❌ No | General RL domains |

---

### 7. Overall Relevance Score

**⭐⭐⭐⭐ High** (Verified from full text — PDF uploaded and read)

Top-tier venue (AAAI 2025, Imperial College London), strictest formal safety guarantees in shielding literature (Theorems 1 & 2), directly confirms binary state classification (safe/unsafe) persists even in the most sophisticated probabilistic shielding mechanisms. The continuous safety level q is the strongest possible counterargument to the novelty claim within the shielding literature — and the precise rebuttal (q adjusts boundary, not governance type) strengthens the argument. Essential for closing the "has probabilistic shielding solved this?" examiner challenge.
