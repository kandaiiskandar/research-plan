## Literature Review Extraction
### Corsi, Amir, Rodríguez, Sánchez, Katz & Fox (2024) — Verification-Guided Shielding

---

### 1. Paper Identity

- **Title:** Verification-Guided Shielding for Deep Reinforcement Learning
- **Authors:** Davide Corsi, Guy Amir, Andoni Rodríguez, César Sánchez, Guy Katz, Roy Fox
- **Year:** 2024
- **Venue:** arXiv preprint (arXiv:2406.06507v2)
- **Type:** System design + empirical evaluation
- **Provenance note:** Preprint as of June 2024. Multi-institutional (UC Irvine, Hebrew University of Jerusalem, IMDEA Software Institute). Strong author track record in formal verification (Katz — Marabou framework) and safe DRL (Corsi). Not yet peer-reviewed at a named venue — **treat as supporting reference, not load-bearing for gap claims.**

---

### 2. Core Contribution

- **Problem:** Shielding guarantees DRL agent safety by overriding unsafe actions at runtime, but incurs significant computational overhead because the shield must be invoked at every time step — even when the agent's action is already safe. Formal verification can identify unsafe inputs offline but provides no corrective action when the policy is deemed unsafe.
- **Proposed solution:** Verification-guided shielding — a five-step pipeline that combines offline verification and online shielding:
  1. **Domain splitting** (ε-ProVe) — probabilistically partition input space into safe/unsafe regions
  2. **Formal verification** (Marabou) — formally certify approximated safe regions
  3. **Clustering** (agglomerative) — compress the set of unsafe regions into a compact representation
  4. **Symbolic representation** (Z3 SMT solver) — encode unsafe regions as succinct first-order logic formulas
  5. **Selective shield execution** — activate shield only in (potentially) unsafe regions; bypass in provably safe regions
- **Main contributions:** Reduces shield activation overhead by 25–71% while preserving formal safety guarantees. Demonstrates that even well-trained DRL agents (95%+ success rate, 0% empirical collisions) have formally verifiable unsafe input configurations.
- **Novelty:** First approach to combine offline DNN verification with online shielding to achieve selective, region-dependent shield activation. The key insight is that the shield need not be invoked everywhere — only where the agent's behaviour cannot be formally guaranteed safe.

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | **Yes** | Core hybrid: deterministic formal verification (Marabou, sound and complete) + probabilistic verification (ε-ProVe, approximated) + LTL-synthesised shield (deterministic) + DRL policy (probabilistic). Multiple formal methods composed in a pipeline. |
| Safety-critical AI decision-making | **Yes** | Motivated by collision avoidance in autonomous navigation. Demonstrates that DRL policies passing empirical testing (0% observed collisions) still have formally verifiable unsafe configurations — motivating formal safety guarantees. |
| AI governance / control mechanisms | **Yes** | Shielding is runtime participation governance: the shield overrides unsafe actions. The novel contribution is making this governance *region-selective* — the shield is activated only in verified-unsafe input regions. |
| Low-resource environments | **Partial** | Efficiency is a core motivation: reducing runtime overhead for real-time robotic systems with limited compute. Data collected on "commercial laptop to align with the limited hardware typically used to operate autonomous robotic systems." However, the offline verification requires 160 CPUs and hours of computation. |
| Decision architecture formalisation | **Yes** | Formally defined: DNN verification problem (Definition 1), LTL synthesis, safety-game formulation for shield synthesis, symbolic representation via SMT formulas. Input space formally partitioned into safe/unsafe regions with provable guarantees. |
| Human role in decision-making | **No** | Fully autonomous agent-environment loop. No human decision-maker. |
| Socio-technical evaluation | **No** | Purely technical evaluation: overhead reduction, shield activation percentage, collision avoidance. |
| Coastal fisheries / maritime domain | **No** | Robotic navigation domain (Particle World grid, Mapless Navigation with lidar). |

**Mid-Extraction Relevance Gate:** 4 Yes + 1 Partial = **≥ 3 Yes → FULL EXTRACTION**

---

### 4. Decision Architecture Analysis

- **Architecture structure:** Two-phase layered pipeline:
  - **Offline phase:** Input domain → ε-ProVe splitting → Marabou formal verification → clustering → symbolic encoding → partitioned safe/unsafe region map
  - **Online phase:** At each time step: check if current input ∈ unsafe region → if yes, activate shield → shield verifies action and overrides if unsafe → if no, bypass shield and use original policy action

- **Safety constraint mechanism:** LTL specifications encode safety properties (e.g., φ := □(¬COLLIDE)). Shield synthesised from LTL specification guarantees that all behaviours satisfy φ. Formal verification (Marabou) certifies that in safe regions, the policy already satisfies φ without the shield.

- **Rule-based constraints before AI:** **Region-dependent.** In unsafe regions, the shield (deterministic, LTL-synthesised) intercepts the DRL agent's action *after* the agent proposes it but *before* it reaches the environment. In safe regions, no constraint is applied — the agent acts freely because formal verification has already proven safety.

- **Failure modes and fallback:** The shield provides a corrective action (O') when the original action (O) would violate φ. However, "although the shield guarantees adherence to the given requirements, it does not necessarily select the optimal action, among the safe ones." No explicit degraded mode or escalation mechanism.

- **Override mechanism:** The shield has full override authority in unsafe regions. No human in the loop.

---

### 5. Formal Model and Mathematical Representation

- **Formal model:** Yes — multiple formal layers:
  - **DNN Verification Problem (Definition 1):** R = ⟨N, P, Q⟩ where N is DNN, P is precondition on inputs, Q is postcondition on outputs. Output: SAT if ∃x | P(x) ∧ Q(N(x)), UNSAT otherwise.
  - **LTL specification:** φ := □(¬COLLIDE) and variants. Standard LTL syntax with temporal operators (□, ◇, U, ○).
  - **Shield synthesis:** Given LTL φ and system D, shield S guarantees D ∘ S never violates φ. When D(I) := O violates φ(I,O), S replaces O with O' such that φ(I,O') holds.
  - **Region partition:** Input domain divided into safe set U (UNSAT — formally verified) and unsafe set S (SAT — at least one counterexample found). Clustering produces overapproximation S' ⊇ S.
  - **Symbolic representation:** Unsafe regions encoded as SMT formulas (linear real arithmetic) and simplified using Z3.

- **Comparison to my pipeline E → S = f(E) → (G(S), A_AI(S)) → AI(E):**
  - The paper partitions the input space into two regions: safe (shield off) and unsafe (shield on). This is structurally analogous to a binary safety state classification S = f(E) → {SAFE, UNSAFE} with G(SAFE) = 1 (AI unrestricted), G(UNSAFE) = 1 (AI + shield).
  - However, this is **not** an environmental state classification — it's a verification-derived partition of the *input space* based on the DNN's formal properties, not based on environmental conditions.
  - There is **no Level 2 governance**. In unsafe regions, the shield either allows or replaces the action — it doesn't restrict the *types* of actions the agent can propose.
  - There is **no CAUTION mode**. The partition is binary: provably safe (no shield) or potentially unsafe (full shield). No intermediate mode with restricted advisory scope.

- **State-dependent recommendation restriction:** **No.** The shield either lets the action pass or replaces it entirely. No restriction on action types or advisory scope as a function of classified state.

- **Safety Dominance Property equivalent:** **Partial.** The combined system D ∘ S is formally guaranteed to never violate φ (in unsafe regions, the shield ensures compliance; in safe regions, verification ensures compliance). This is a system-level safety guarantee, but it applies uniformly — not conditioned on a classified safety state that determines admissible output scope. It guarantees behavioural compliance with φ, not AI(E) ⊆ A_AI(S).

- **Formalisation purpose:** Operational — verification queries are solved by Marabou, ε-ProVe performs actual domain splitting, shield synthesis produces a deployable runtime component.

---

### 6. Safety State Classification

- **Discrete risk/safety levels:** **Binary only.** The input domain is partitioned into:
  - **Safe regions (UNSAT):** Formally verified — agent provably satisfies safety properties; shield deactivated
  - **Unsafe regions (SAT):** At least one counterexample exists; shield activated
- **No intermediate level.** The clustering step may overapproximate (mark safe regions as unsafe for compactness), but this only increases the unsafe set — it doesn't create a graduated intermediate category.
- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:** The binary partition maps to {SAFE, UNSAFE} only. No CAUTION state exists. No mechanism for the agent to participate with restricted scope in a borderline region.
- **CAUTION mode equivalent:** **Absent.** The paper's key innovation is reducing *where* the shield is active (efficiency optimisation) — not *how* the shield behaves in intermediate states. In unsafe regions, the full shield is activated; there's no partial or graduated shielding mode.

---

### 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (G(S)) | **Yes** | Region-selective participation governance: in safe regions, AI operates freely; in unsafe regions, AI operates under shield supervision (action may be overridden). The shield is a Level 1 participation gate — it determines whether the agent's proposed action reaches the environment. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | **No** | The shield does not restrict what *types* of actions the agent may propose. It evaluates each proposed action individually and either allows or replaces it. No scope restriction based on region classification. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | **No** | The region partition is verification-derived (based on DNN formal properties), not environmental-state-conditioned. No unified governance pair. |

- **Binary vs. graduated:** Binary. The system has exactly two modes: shield-off (safe region) and shield-on (unsafe region). No graduated governance.
- **Level 2 governance:** Absent.
- **Support for two-level governance pair:** The paper's region-selective approach is **architecturally suggestive** for graduated governance. The idea that the shield's *activation intensity* should vary based on formally verified properties of the input region is conceptually adjacent to the idea that advisory scope should vary based on classified safety state. However, the paper only varies *whether* the shield is active (Level 1), not *what* the shield constrains (Level 2).

---

### 8. Human Role in Decision-Making

- **Human involvement:** None at runtime. The domain expert encodes safety properties (LTL specifications) and verification queries offline. All runtime decisions are fully automated.
- **Decision support vs. automation:** Pure **decision automation.** Agent acts autonomously; shield intervenes autonomously.
- **Human override:** Not addressed.

---

### 9. System Constraints and Environment

- **Real-world constraints:** Efficiency is a primary motivation. The paper explicitly notes that "in many real-time applications such an overhead may be infeasible in practice." Online data collected on a commercial laptop to simulate resource-constrained deployment.
- **Deployment context:** Robotic navigation — Particle World (2D grid) and Mapless Navigation (lidar-based robot). Simulated environments but modelled after real-world robotics.
- **Resource-aware design:** The entire method is an efficiency optimisation — reducing shield invocations from 100% to as low as 1.3% of time steps. Overhead reduction of 25–71%. However, offline verification is compute-intensive (160 CPUs, hours of computation).
- **Edge cases:** Formal verification is NP-complete per query. ε-ProVe provides only probabilistic guarantees (complemented by Marabou for formal certification). Clustering overapproximates unsafe regions (shield may activate unnecessarily but never fails to activate when needed). Shield does not guarantee optimal action among safe alternatives.

---

### 10. Hybrid AI Taxonomy

- **Hybrid AI type:** **Supervisory control with verification-guided selective activation.** The DRL agent (probabilistic) is supervised by the shield (deterministic, LTL-synthesised), but supervision is only active in regions where formal verification cannot prove safety.
- **Safety enforcement position:** **After AI reasoning, selectively.** The shield intercepts the agent's action post-hoc, but only in verified-unsafe regions. In safe regions, no enforcement is applied.
- **Two-level governance support:** **No.** Single-level binary control — shield on or off. No graduated scope restriction.
- **Comparison to my architecture:** Both architectures use formal methods to determine governance intensity. However: (1) My architecture classifies *environmental state* → governs *advisory scope*; this paper classifies *input regions by DNN properties* → governs *shield activation*. (2) My architecture has three modes (SAFE/CAUTION/UNSAFE) with two governance levels; this paper has two modes (safe/unsafe) with one governance level. (3) My architecture restricts recommendation *types*; this paper replaces individual *actions*.

---

### 11. Baseline Comparison and Evaluation

- **Baselines:** Full (always-active) shielding vs. verification-guided (selective) shielding vs. no shielding.
- **Metrics:** Shield active time (%), overhead (×), gain (%), collision rate (%), shield interventions (%).
- **Key results:**
  - Particle World: Shield active 28–45% of time (down from 100%); overhead reduced from 31–40× to 13–22×; gain 41–65%
  - Mapless Navigation: Shield active 1.3–62% of time; overhead reduced from 4.4–4.8× to 1.5–3.6×; gain 20–71%
  - Zero collisions maintained in all shielded configurations
- **CAUTION zone testing:** **No.** No intermediate mode tested.
- **Safety Dominance Property verification:** The combined system D ∘ S is formally verified to satisfy φ across the entire input domain (safe regions by verification, unsafe regions by shield). This is a system-level guarantee, but not conditioned on classified safety states.
- **Graduated vs. binary comparison:** **No.** Only binary comparison (shield always on vs. shield selectively on).
- **Evaluation gaps:** No graduated governance evaluation, no human-in-the-loop testing, no real-world deployment (only simulation), limited DNN architectures (small MLPs with ReLU only).

---

### 12. Key Concepts and Definitions

| Concept | Definition / Relevance |
|---|---|
| **Verification-guided shielding** | Combining offline formal verification with online selective shielding — shield activated only in regions where the policy cannot be formally verified as safe. Core innovation. |
| **DNN Verification Problem** | R = ⟨N, P, Q⟩; SAT if ∃x | P(x) ∧ Q(N(x)), UNSAT otherwise. Standard definition from Katz et al. (2017). |
| **ε-ProVe** | Probabilistic algorithm that splits input domain into approximated safe/unsafe regions via iterative subdivision and sampling. Provides probabilistic (not formal) safety guarantees. |
| **All-DNN-Verification** | The problem of identifying *all* regions where a DNN satisfies a given property. #P-hard. ε-ProVe provides an underapproximation. |
| **Shield synthesis (LTL)** | Automatic generation of a shield S from LTL specification φ, guaranteeing D ∘ S satisfies φ. |
| **Region overapproximation** | Clustering may mark safe regions as unsafe, increasing shield activation but never compromising safety. Conservative approximation preserves soundness. |
| **Symbolic representation** | Encoding unsafe regions as SMT formulas (linear real arithmetic) for compact representation and efficient online lookup. |

---

### 13. Limitations and Unsolved Problems

- **Stated limitations:**
  1. Requires valid encoding of safety properties and access to environment dynamics / transition model
  2. Shield guarantees adherence to requirements but not optimal action among safe alternatives
  3. Backend verification (Marabou) has limited support for some activation functions, restricting applicability to advanced DNN architectures
  4. Offline verification is computationally intensive (NP-complete per query, hours of total computation)
  5. Symbolic representation step did not improve efficiency in their evaluation (ran slightly slower)

- **Unstated but identifiable limitations:**
  1. Binary safe/unsafe partition — no graduated intermediate mode
  2. Region classification is based on DNN formal properties, not environmental conditions — the partition is static (computed offline), not dynamic (adapting to changing environmental state at runtime)
  3. No human in the decision loop
  4. Tested only on small MLPs (8–9 inputs, 16–32 hidden neurons) — scalability to larger networks undemonstrated

- **Gaps aligned with my research:**
  - **Graduated governance gap:** The binary safe/unsafe partition maps directly to Level 1 governance only. My CAUTION mode addresses precisely the "unsafe but not critically so" regions where the agent could still participate with restricted scope.
  - **Environmental state conditioning gap:** The partition is DNN-property-based, not environmental-state-based. My S = f(E) classifies environmental conditions, not DNN input-output relationships.
  - **Advisory scope restriction gap:** In unsafe regions, the shield either allows or replaces actions — it doesn't restrict what types of actions are admissible. My A_AI(S) restricts the recommendation space itself.

---

### 14. Methodology Notes

- **Research method:** System design + empirical evaluation. Five-step pipeline combining multiple formal methods. Evaluated on two DRL benchmarks with extensive offline and online measurements.
- **DSR alignment:** Partial. The pipeline follows a design-build-evaluate pattern. Formal guarantees are proven (soundness of the combined system). However, not framed as DSR.
- **Informing my research:**
  - The insight that governance intensity should vary across the input space (shield active only where needed) is conceptually parallel to my claim that advisory scope should vary across safety states
  - The use of formal verification to *justify* differential governance (provably safe regions don't need the shield) is methodologically relevant — my architecture uses deterministic rules to justify differential advisory scope
  - The overapproximation principle (clustering may mark safe regions as unsafe but never the reverse) parallels conservative design in my CAUTION mode — restrict more than necessary rather than risk under-restriction

---

### 15. Quotable / Citable Points

1. **Empirically safe ≠ formally safe:** "Although the models were extensively trained with a state-of-the-art algorithm to solve a (relatively) simple task, and although they seemed to behave safely in empirical evaluation, this was indeed not the case, as formal methods were able to uncover input configurations in which they fail miserably." (Section 3, p.5) — Motivates formal safety guarantees.

2. **Shield overhead problem:** "The external shield must be invoked in every time step, resulting in significant overhead. This issue is critical, because in many real-time applications such an overhead may be infeasible in practice." (Section 1, p.2) — Motivates efficiency-aware governance design.

3. **Shield non-optimality:** "Although the shield guarantees adherence to the given requirements, it does not necessarily select the optimal action, among the safe ones." (Section 1, p.2) — Motivates scope restriction over action replacement.

4. **Region-selective activation:** "In the remaining (unsafe) input region, we activate the shield... Our approach significantly reduces the overall overhead of 'traditional shielding', while still preserving the formal guarantees." (Section 1, p.2) — Demonstrates region-dependent governance intensity.

5. **Overhead reduction:** Shield active time reduced to as low as 1.3% (from 100%) with zero safety degradation. (Table 4, p.8) — Quantifies the benefit of selective governance activation.

---

### 16. Relation to My Research and Positioning

- **Level 1 governance:** **Yes** — region-selective participation governance. The innovation is making Level 1 activation *efficient* by restricting it to verified-unsafe regions.
- **Level 2 governance:** **No** — no restriction on advisory scope based on region classification. Shield either allows or replaces actions.
- **State-conditioned:** **Partial** — regions are conditioned on DNN formal properties (offline), not on classified environmental state (runtime).
- **Two-level governance pair proximity:** The binary region partition (safe vs. unsafe) is conceptually the simplest instance of state-dependent governance variation. My architecture extends this from two states to three, from one governance level to two, and from DNN-property-based classification to environmental-state-based classification.
- **Safety Dominance Property:** System-level guarantee (D ∘ S satisfies φ) is present but not conditioned on classified safety states.
- **Gap my research addresses:** This paper demonstrates that *where* governance is applied can be formally justified — but only in a binary sense (shield on/off). My architecture extends this to *what* governance constrains (advisory scope) and conditions it on *environmental state* rather than DNN formal properties.

**Positioning paragraph:** This paper demonstrates a valuable principle: governance intensity can and should vary across the input space, and formal methods can justify where governance is needed. The verification-guided approach partitions the input domain into safe regions (no shield needed) and unsafe regions (shield activated), reducing runtime overhead by up to 71% while preserving formal safety guarantees. However, the governance remains single-level and binary — the shield is either fully active or fully inactive, and when active, it either allows or replaces actions without restricting the agent's advisory scope. This paper should be cited in Section 2.2 as an example of efficiency-optimised Level 1 governance and as a conceptual precursor to the idea that governance intensity should be state-dependent. The principle that formal methods can justify differential governance levels is methodologically aligned with my architecture's use of deterministic environmental state classification to condition two-level governance. The binary limitation provides direct gap evidence for the CAUTION mode, where the agent would participate with restricted scope in borderline regions — a mode absent from this work's safe/unsafe partition.

---

### 17. Overall Relevance Score

**⭐⭐⭐ Medium**

Useful conceptual precursor to state-dependent governance variation, with the important principle that formal methods can justify *where* governance is applied. The binary safe/unsafe partition and the efficiency motivation are relevant to the argument for graduated governance. However, the approach is limited to Level 1 binary shielding, does not classify environmental states, and does not implement advisory scope restriction. Preprint status limits citability for load-bearing claims. Best used in Section 2.2 (efficiency-aware shielding) and as supporting motivation for the CAUTION mode.
