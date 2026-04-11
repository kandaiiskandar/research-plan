## Literature Review Extraction — GAP-FOCUSED
### Kwon, Ingebrand, Topcu & Feng (2025) — Adaptive Shielding for Safe RL under Hidden-Parameter Dynamics Shifts

---

### 1. Paper Identity

- **Title:** Adaptive Shielding for Safe Reinforcement Learning under Hidden-Parameter Dynamics Shifts
- **Authors:** Minjae Kwon¹, Tyler Ingebrand², Ufuk Topcu², Lu Feng¹
- **Affiliation:** ¹University of Virginia, ²University of Texas at Austin
- **Correspondence:** Lu Feng <lu.feng@virginia.edu>
- **Year:** 2026 (arXiv v2: 30 Jan 2026; original v1: June 2025)
- **Venue:** arXiv:2506.11033v2 (Preprint)
- **Type:** Preprint with open-source code (github: adaptive shield)
- **URL:** https://arxiv.org/abs/2506.11033
- **Citation Quality:** ⚠️ Preprint (not yet peer-reviewed). However, strong institutional affiliations (UVA, UT Austin), formal theorem with proof, comprehensive experiments on Safe-Gym benchmarks. Code released for reproducibility.

---

### 2. Core Contribution

- **Problem:** Robots and autonomous systems operate in environments where underlying dynamics vary due to hidden parameters (mass distribution, friction, terrain compliance, gravity). These parameters change across episodes and remain unobserved, introducing safety risks. Existing work splits into two non-overlapping camps: (1) adaptive methods (hypernetworks, contextual policies, mixture-of-experts) that handle varying dynamics but provide no safety mechanisms; (2) safe RL frameworks (CMDPs, shielding) that enforce safety but assume stationary dynamics.
- **Proposed solution:** Adaptive Shielding — a framework combining three complementary mechanisms:
  1. **Safety-Regularized Optimization (SRO):** A training-time objective augmenting rewards with a cost-sensitive safety measure Q^π_safe(s, a, b_φ) that proactively steers policy toward low-violation behaviour. Proposition 1 proves SRO does not degrade performance for already-safe policies.
  2. **Online Hidden-Parameter Adaptation:** Function encoders (Ingebrand et al., 2024b; 2025) infer a low-dimensional representation b_φ of hidden dynamics T_φ from transition samples online, enabling both policy and shield to adapt without retraining.
  3. **Adaptive Shield with Uncertainty-Awareness:** At execution time, the shield samples N candidate actions, uses the function encoder to predict next states, computes uncertainty-aware safety margins via Adaptive Conformal Prediction (ACP), and filters actions whose SafetyScore falls below zero (Eq. 11–12).
- **Formal guarantee — Theorem 1:** For any policy π augmented with the adaptive shield, there exists 0 ≤ ε̄ ≤ 1 such that the average cost rate ξ^π(s, φ) ≤ δ + ε̄(1 − δ), where δ is the ACP failure probability. The bound connects prediction errors in the dynamics model to the average cost rate.
- **Hidden parameters:** gravity, damping, mass, inertia, friction — sampled from [0.3, 1.7] for training, [0.15, 0.3] ∪ [1.7, 2.5] for OOD evaluation.
- **Evaluation:** Safe-Gym benchmark (Ji et al., 2023), 8 robot-task combinations (Point/Car × Goal/Button/Push/Circle). Compared against 6 baselines (Saute, PPO-Lag, RCPO, CPO, CUP, USL). SRO+Shield achieves best return-cost trade-off across all tasks, including OOD environments with unseen dynamics.
- **Three contributions:** (1) Safety-regularized optimization; (2) online hidden-parameter adaptation via function encoders; (3) adaptive uncertainty-aware shield with Theorem 1 guarantee.

---

### 3. Governance Mechanism Analysis

| Property | Assessment |
|---|---|
| **Governance type** | **Binary** — for each candidate action, SafetyScore(a) is computed (Eq. 11); actions with SafetyScore > 0 form Â_safe; actions with SafetyScore ≤ 0 are filtered out. The decision is binary: safe (positive score) or unsafe (non-positive score). |
| **Trigger** | Inferred hidden parameters b_φ of the environment dynamics (gravity, damping, mass, inertia, friction) + predicted next states via function encoder + ACP uncertainty margin Γ_t |
| **Intermediate mode?** | **No** — no CAUTION equivalent. The shield has a pre-safety check (Eq. 10: ν(e(s_t), E_t) > L_ν Δ) that can skip full verification when the agent is clearly safe, but this is a computational optimisation, not a governance mode. When full verification runs, the decision is still binary: Â_safe or filtered. |
| **Environmental conditioning?** | **Yes, but binary** — the shield explicitly adapts to changing environment dynamics via online inference of hidden parameters. The cost function separates agent-centric features e(s) ∈ ℝ^n₁ and **environment-centric features E ∈ ℝ^n₂** (p. 5). The safety margin ν(e(s_t), E_t) directly incorporates environmental features. This is the closest any shielding paper gets to environment-conditioned governance. However, the environmental features modulate the *safety boundary* (continuous), not a *governance mode* (discrete). There are no classified environmental states. |
| **Advisory scope restriction?** | **No** — the shield filters individual candidate actions based on SafetyScore. It does not restrict categories or types of actions. All action types remain eligible if their SafetyScore > 0. No Level 2 governance. |
| **Runtime adaptation?** | **Yes** — the shield adapts online via function encoder coefficients b_φ updated from transition data (Eq. 5), and ACP threshold Γ_t adapts to prediction errors over time. The governance *boundary* is continuously updated, but the governance *type* (binary filter) never changes. |

---

### 4. Governance Level Analysis

| Level | Question | Implemented? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI act at all? (G(S)) | **Yes (binary)** | Shield samples N candidate actions, computes SafetyScore(a) via Eq. 11–12, and filters actions with SafetyScore ≤ 0. Actions in Â_safe are permitted; all others are blocked. This is binary participation governance over individual actions. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | **No** | The shield evaluates each candidate action independently against the SafetyScore threshold. It does not restrict categories or types of actions — all action types remain eligible if their individual SafetyScore > 0. No mechanism equivalent to A_AI(S) restricting recommendation types. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | **No** | The cost function separates agent-centric features e(s) ∈ ℝ^n₁ and environment-centric features E ∈ ℝ^n₂ (Section 4.2), and the safety margin ν(e(s_t), E_t) incorporates both. But the environment-centric features modulate the *safety boundary* (continuous), not a *governance mode* (discrete). Hidden parameters φ are inferred continuously, not classified into discrete environmental states. |

---

### 5. Gap Evidence for Novelty Argument

**Key finding:** This paper is the strongest possible counterargument to the novelty claim because it *adapts the shield to changing environment conditions at runtime*. An examiner could argue: "This paper already does environment-conditioned governance." The rebuttal is precise:

1. **Adaptation ≠ mode classification.** The adaptive shield continuously adjusts its safety boundary as hidden parameters φ change via function encoder coefficients b_φ (Eq. 5). The proposed architecture classifies the environment into *discrete governance modes* (SAFE/CAUTION/UNSAFE) with categorically different governance properties at each mode. The function encoder provides continuous adaptation of the safety boundary — not discrete state classification.

2. **No intermediate governance mode.** When environment dynamics shift to make conditions more dangerous (e.g., hidden parameters moving toward OOD range [0.15, 0.3] ∪ [1.7, 2.5]), the adaptive shield tightens its action restrictions via the ACP threshold Γ_t — but the tightening is continuous, not modal. There is no point at which the system enters a distinct CAUTION mode with a qualitatively different governance regime (e.g., restricting recommendation types rather than individual actions). The pre-safety check (Eq. 10: ν(e(s_t), E_t) > L_ν Δ) is explicitly a computational optimisation to skip full verification when the agent is clearly safe — not a governance mode transition.

3. **No Level 2 governance.** The shield never restricts *what types of recommendations* are permitted. It evaluates each of N sampled candidate actions against the SafetyScore threshold (Eq. 11–12). The proposed architecture's A_AI(S) restricts entire categories of advisory output — a fundamentally different governance mechanism.

4. **Environment-centric features ≠ environmental state classification.** The cost function explicitly separates agent-centric features e(s) ∈ ℝ^n₁ and environment-centric features E ∈ ℝ^n₂ (Section 4.2). This is the closest any shielding paper gets to environment-conditioned governance. However, the environment-centric features feed into a continuous safety margin ν(e(s_t), E_t), not a discrete state classifier S = f(E). The environment modulates how restrictive binary governance is — it does not determine which *type* of governance applies.

**Critical distinction from proposed architecture:** Adaptive shielding adapts the *boundary* of binary governance to environmental changes. The proposed architecture changes the *type* of governance based on classified environmental state. The shield's binary decision becomes more or less restrictive; the proposed architecture's governance becomes qualitatively different (full advisory scope → restricted advisory types → no AI participation).

**Paper's own limitations (Section 7):** The authors acknowledge evaluation is limited to simulated Safe-Gym environments (8 robot-task combinations). No real-world deployment, no human-in-the-loop evaluation, no domain-specific safety considerations. This reinforces that even the most environment-aware shielding work remains in the formal RL domain and does not address the socio-technical governance needs of real-world advisory systems.

**Use in justification:** Cite as the strongest "near-miss" in the shielding literature. Its environment-adaptive property (function encoders + ACP + environment-centric cost features) makes it the closest comparator, which makes its binary limitation the most powerful evidence that even environment-aware shielding does not implement graduated governance.

---

### 6. Theme Relevance

| Theme | Match? | Notes |
|---|---|---|
| T1: Hybrid AI | ⚠️ Partial | Shield wrapper over RL agent — not a hybrid rule-based/ML architecture in the proposed sense |
| T2: Safety-critical AI | ✅ Yes | Formal safety guarantees (Theorem 1) with online adaptation via function encoders and ACP |
| T3: AI governance | ✅ Yes | Binary governance (SafetyScore filter) that adapts to environment changes via hidden-parameter inference — strongest near-miss |
| T4: Low-resource environments | ❌ No | No resource constraint discussion; assumes computational capacity for N-action sampling and function encoder inference |
| T5: Decision architecture formalisation | ✅ Yes | CHiP-MDP M = (S, A, Φ, T, R, C, γ, P_Φ), conformal prediction, formal safety bound |
| T6: Human role | ❌ No | No human-in-the-loop; fully autonomous shield |
| T7: Socio-technical evaluation | ❌ No | Simulation-only evaluation on Safe-Gym benchmarks (Point/Car × Goal/Button/Push/Circle) |
| T8: Coastal fisheries / maritime | ❌ No | General RL robot locomotion domains |

---

### 7. Overall Relevance Score

**⭐⭐⭐⭐⭐ Very High** (Verified from full text — PDF uploaded and read)

The most important comparator paper for the novelty argument. Its environment-adaptive shielding — combining function encoders for hidden-parameter inference, ACP for uncertainty-aware safety margins, and explicit separation of agent-centric and environment-centric features in the cost function — is the closest existing mechanism to the proposed architecture's environment-state-conditioned governance. The precise ways it falls short (binary SafetyScore filter only, continuous adaptation not discrete mode classification, no Level 2 advisory scope restriction, no CAUTION equivalent) define the exact contribution of the proposed architecture. Essential for rebutting the examiner challenge: "Doesn't adaptive shielding already do environment-conditioned governance?"
