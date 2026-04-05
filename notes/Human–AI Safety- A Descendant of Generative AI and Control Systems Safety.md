# Literature Review Extraction
## Paper: Human–AI Safety: A Descendant of Generative AI and Control Systems Safety

---

## 1. Paper Identity

- **Full title:** Human–AI Safety: A Descendant of Generative AI and Control Systems Safety
- **Authors:** Andrea Bajcsy (Carnegie Mellon University), Jaime F. Fisac (Princeton University)
- **Year:** 2024 (arXiv:2405.09794v2, 22 June 2024)
- **Venue:** arXiv preprint (not yet peer-reviewed in a journal)
- **Type of paper:** Position/roadmap paper with formal theoretical framework

---

## 2. Core Contribution

- **Main problem:** Current AI safety paradigms focus on fine-tuning generative model outputs (value alignment via RLHF, red-teaming, monitoring), but these approaches treat AI outputs in isolation. In reality, AI outputs and human behaviour form a dynamic feedback loop whose consequences evolve over time. Meaningful safety assurances require reasoning about how this feedback loop drives the interaction towards different outcomes.
- **Proposed solution:** A unifying formal framework that models human-AI interaction as a closed-loop dynamical system (the Human-AI game), drawing on control-theoretic safety (safety filters, reachability analysis, dynamic games) combined with generative AI's latent representations and human behaviour modelling capabilities. The paper proposes the **Human-AI Safety Filter** — a runtime mechanism that monitors and minimally overrides AI task policy outputs to prevent safety violations.
- **Main contributions:**
  - Synthesis of complementary lessons from AI safety (value alignment, red-teaming, monitoring) and control systems safety (safety filters, reachability, dynamic games, operational design domains)
  - Formal Human-AI (HAI) dynamical system model with state spaces, action spaces, and dynamics for both human and AI agents
  - Safety formalisation: failure set F^AI, maximal safe set Ω*, safety value function V(z^AI), and the zero-sum safety game (Equation 4-5)
  - **Human-AI Safety Filter** (Theorem 1): a tuple (π^AI_fallback, Δ, ϕ) comprising a fallback policy, safety monitor, and intervention scheme that guarantees safety for all allowable human behaviours
  - Four-category taxonomy of failure specification mechanisms: factory rules, common sense, direct feedback, need reading
  - Technical roadmap towards algorithmic instantiation using adversarial RL, deep safety value function approximation, and PAC-Bayes generalization theory
- **What is novel:** First generalisation of the safety filter formalism from embodied/physics-based systems (robotics, autonomous driving) to general human-AI systems operating in latent state spaces (including dialogue). The formal game-theoretic safety framework for human-AI interaction that provides mathematical safety guarantees (Theorem 1).

---

## 2. Core Contribution (cont.)

**Key distinction from existing AI safety work:** The paper argues that safety is not a property of AI outputs in isolation but a property of the *dynamic interaction trajectory*. Present actions that appear safe can lead to future states from which safety violations become unavoidable. This temporal, trajectory-level reasoning is the core insight from control systems that the paper brings to AI safety.

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | **Partial** | The safety filter architecture is conceptually hybrid: a learned task policy (probabilistic/generative) is constrained by a safety mechanism (control-theoretic/deterministic in intent). The fallback policy and safety monitor act as constraint layers over the task policy. |
| Safety-critical AI decision-making | **Yes** | Central focus. Formal definition of safety-critical human-AI systems. Safety defined as continued satisfaction of critical human needs at all times. |
| AI governance / control mechanisms | **Yes** | The safety filter is a governance mechanism: it monitors AI task policy outputs and intervenes (overrides) when candidate actions could lead to future safety violations. The intervention scheme ϕ governs what the AI is permitted to output. |
| Low-resource environments | No | The paper targets internet-scale generative AI systems. No discussion of resource constraints. |
| Decision architecture formalisation | **Yes** | Extensively formalised: HAI dynamical system with states z = [s, z^AI, z^H], action spaces, dynamics functions, failure sets, safety value function, maximal safe set, zero-sum dynamic game, and Theorem 1 (safety filter guarantee). |
| Human role in decision-making | **Yes** | Human modelled as an agent with internal state z^H, action space A^H, and policy π^H. The Operational Design Domain (ODD) specifies bounds on allowable human behaviour Â^H(z^AI). Human actions influence system state evolution. |
| Socio-technical evaluation | No | Purely theoretical framework. No empirical or socio-technical evaluation. |
| Coastal fisheries / maritime domain | No | Examples from autonomous driving, aviation, AI chatbots. |

**Mid-Extraction Relevance Gate:** 4 Yes + 1 Partial → **FULL EXTRACTION**

---

## 4. Decision Architecture Analysis

- **Decision-making structure:** The paper models human-AI interaction as a two-player dynamic game. At each time step: (1) the AI observes its internal state z^AI, (2) the AI's task policy proposes an action a^AI, (3) the safety filter evaluates whether the action could lead to future constraint violations, (4) the intervention scheme either permits or replaces the action, (5) both agents' states evolve based on the joint actions. This is sequential, temporal, and feedback-loop-driven.
- **Layered architecture / governance structure:** Yes — a two-layer architecture: (i) the **task policy** π^AI_§ pursues task objectives (helping the user, generating content), and (ii) the **safety filter** (π^AI_fallback, Δ, ϕ) monitors and overrides the task policy when safety is at risk. The filter only intervenes at the "last possible moment," preserving task performance while guaranteeing safety.
- **Rule-based constraints or safety checks before AI decisions:** Yes — the safety monitor Δ evaluates candidate actions *before* they are executed. If the monitor determines that the fallback policy cannot maintain safety after the candidate action, the intervention scheme replaces it. This is a pre-execution safety gate.
- **Boundary between deterministic control and AI reasoning:** Explicitly defined. The task policy is a learned generative model (probabilistic). The safety filter is derived from control-theoretic principles (deterministic in its safety guarantee, though computed via learned approximations). The boundary is the intervention scheme ϕ, which decides whether the task policy's output passes through or is replaced.
- **Failure modes / fallback behaviour:** Explicitly formalised. The fallback policy π^AI_fallback is a dedicated safety-only policy that avoids catastrophic failures without regard to task performance. The safety filter guarantees that the system can always revert to the fallback policy and maintain safety.

**Key parallel to my architecture:** The safety filter's structure — a task-performing AI constrained by a safety mechanism that monitors and can override AI outputs — is conceptually parallel to my architecture's structure: a probabilistic AI generating recommendations within an admissible action space A_AI(S) defined by the deterministic gate function G(S). Both enforce the principle that safety constraints dominate task performance.

---

## 5. Formal Model and Mathematical Representation

- **Formal model:** Extensively formalised. The Human-AI (HAI) dynamical system includes:
  - **States:** Privileged game state z = [s, z^AI, z^H] where s = world state, z^AI = AI internal state, z^H = human internal state
  - **Actions:** a^AI ∈ A^AI (AI actions), a^H ∈ A^H (human actions)
  - **Dynamics:** s_{t+1} = f^s(s_t, a^AI_t, a^H_t); z^H_{t+1} = f^H(z^H_t, a^AI_t, a^H_t, o^H_t); z^AI_{t+1} = f^AI(z^AI_t, a^AI_t, a^H_t, o^AI_t)
  - **Failure set:** F^AI ⊆ Z^AI — states where AI assesses the system may be in failure
  - **Safety condition:** ∀t, z^AI_t ∉ F^AI (Equation 2)
  - **Maximal safe set:** Ω* := {z^AI_0 : ∃π^AI, ∀π̂^H | ∀τ ≥ 0, z^AI_τ ∉ F^AI} (Equation 3)
  - **Safety value function:** V(z^AI_0) := max_{π^AI} min_{π̂^H} [min_{t≥0} ℓ(z^AI_t)] (Equation 4)
  - **Isaacs equation:** V(z^AI) = max_{a^AI} min_{a^H} min{ℓ(z^AI), E[V(f^AI(...))]} (Equation 5)
  - **Safety filter:** Tuple (π^AI_fallback, Δ, ϕ) with Theorem 1 guaranteeing safety
  - **Operational Design Domain (ODD):** Predictive action bounds Â^H(z^AI) delimiting allowable human actions

- **Comparison to E → S = f(E) → (G(S), A_AI(S)) → AI(E):**

| My Architecture | Bajcsy & Fisac |
|---|---|
| E (environmental state vector) | s (world state) + o^AI (AI observations) |
| S = f(E) (safety state classification) | Failure set F^AI and safe set Ω* (derived from safety value function) |
| G(S) (gate function: AI on/off) | Safety monitor Δ (determines if fallback needed) + intervention scheme ϕ (permits or overrides AI action) |
| A_AI(S) (admissible recommendation space) | The set of actions a^AI that pass the safety monitor: {a^AI : Δ(z^AI, a^AI) ≥ 0} |
| Safety Dominance Property: AI(E) ⊆ A_AI(S) | Theorem 1: ∀t ≥ 0, z^AI ∉ F^AI under filtered dynamics |

- **State-dependent recommendation restriction:** **Yes** — the safety filter implicitly defines state-dependent action restriction. The set of permissible AI actions depends on the current state z^AI: some actions pass the safety monitor in safe states but would be blocked in states closer to the failure set boundary. This is formally encoded in the safety value function V(z^AI) and the Q-function Q(z^AI, a^AI, a^H).
- **Safety Dominance Property comparison:** **Close parallel.** Theorem 1 guarantees that under the safety filter, the system never enters the failure set for all allowable human behaviours. This is the formal analogue of my Safety Dominance Property (AI(E) ⊆ A_AI(S)): the AI's actual outputs are guaranteed to fall within the set of safe actions determined by the current state. The key difference: my Safety Dominance Property is defined over a discrete tripartite safety state (SAFE/CAUTION/UNSAFE) with a fixed containment relationship A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅, while their formulation uses a continuous safety value function over latent state space.
- **Formalisation purpose:** Analytical — used for proving safety guarantees (Theorem 1) and defining a computational procedure (algorithmic safety filtering).

---

## 6. Safety State Classification

- **Discrete risk/safety levels:** Not used. The paper employs a **continuous** safety measure: the safety value function V(z^AI) ∈ ℝ, where V ≥ 0 means safe (z^AI ∈ Ω*) and V < 0 means unsafe (z^AI ∉ Ω*). This is a binary safe/unsafe boundary, not a tripartite classification.
- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:** The paper's safety value function V(z^AI) is a continuous analogue of my discrete safety state. The boundary V = 0 separates safe from unsafe. There is no formal intermediate CAUTION state. However, the continuous nature of V implicitly encodes degrees of safety: states with V barely above 0 are "near the boundary" (analogous to CAUTION), while states with large positive V are deeply safe (analogous to SAFE). But this gradient is not formalised into distinct modes with different AI behavioural regimes.
- **AI recommendation scope differentiation across safety levels:** **Binary, not graduated.** The safety filter has two modes: (1) task policy passes through (safe), or (2) fallback policy takes over (unsafe). The intervention scheme ϕ is typically a binary switch. There is no intermediate mode where the AI participates with restricted recommendation scope — the paper's architecture is fundamentally binary (pass/override), not tripartite (full/restricted/blocked).

**Critical gap relative to my research:** The paper formalises sophisticated safety filtering but with a **binary** intervention logic (permit or override). My architecture introduces the CAUTION mode as a formally distinct intermediate state where AI participates under restricted advisory scope A_AI(CAUTION) ⊂ A_AI(SAFE) — neither fully permitted nor fully blocked. This graduated governance is absent from Bajcsy & Fisac's framework.

---

## 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (equivalent to G(S)) | **Yes** | The safety filter's intervention scheme ϕ determines whether the AI task policy's proposed action is executed or replaced by the fallback policy. When ϕ replaces the action, the task policy is effectively blocked. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (equivalent to A_AI(S)) | **Partial** | The safety monitor implicitly restricts which actions are permissible: only actions a^AI for which Δ(z^AI, a^AI) ≥ 0 pass through. However, this restriction is binary (pass/block), not graduated across distinct advisory scope regimes. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | **Partial** | Both levels are state-conditioned via z^AI (the safety filter's decisions depend on the current AI state). However, there is no classified discrete safety state S ∈ {SAFE, CAUTION, UNSAFE}. The conditioning is via a continuous value function, and the governance is binary (permit/override), not graduated. |

- **Governance type:** **Binary safety filter** — the most sophisticated binary governance in my review so far. It is state-conditioned (via V(z^AI)), runtime (operates during deployment), and formally guaranteed (Theorem 1). But it is binary: the AI either operates fully or is overridden by the fallback.
- **Supports or contradicts two-level governance pair:** **Strongly supports Level 1** with formal guarantees. **Partially supports Level 2** by implicitly restricting permissible actions via the safety monitor. But the paper's binary governance confirms the literature-wide gap my CAUTION mode addresses: even the most formally sophisticated safety frameworks in the literature implement permit/block, not permit-with-restriction.

---

## 8. Human Role in Decision-Making

- **Human involvement:** The human is modelled as a full agent in the dynamic game with their own internal state z^H, actions a^H, and policy π^H. The AI must maintain safety *for all allowable human behaviours* — the human is not assumed to be cooperative.
- **Decision support vs. automation:** The paper's framework applies to both. The safety filter permits the AI's task policy to operate freely as long as safety is maintained — this can be decision support (chatbot advising) or automation (autonomous driving). The framework is agnostic to the automation level.
- **Human-AI interaction dynamics:** Modelled as a feedback loop: AI outputs influence human behaviour, which in turn influences AI state, which influences future AI outputs. The ODD specifies bounds on allowable human actions.
- **Override / escalation:** The safety filter IS the override mechanism — it automatically intervenes when safety is at risk. The human does not need to manually override; the system self-corrects.

---

## 9. System Constraints and Environment

- **Real-world constraints:** Not discussed in the low-resource sense. The paper assumes access to powerful generative AI models, learned representations, and sufficient compute for adversarial RL.
- **Deployment context:** Theoretical framework. Examples from autonomous driving, aviation collision avoidance, and AI chatbots, but no real-world deployment.
- **Resource-aware design:** Not addressed.

---

## 10. Hybrid AI Taxonomy

- **Type:** **Supervisory control / safety filter architecture.** A learned task policy (generative AI) is supervised and overridden by a safety mechanism (control-theoretic filter). This maps to my "supervisory control" category.
- **Safety enforcement location:** **Alongside and after AI reasoning** — the safety filter evaluates the task policy's proposed action and intervenes if needed. The safety mechanism operates at the output boundary of the AI, not within its reasoning process.
- **Two-level governance support:** Supports Level 1 (binary participation control via safety filter). Does not implement graduated Level 2 (advisory scope restriction).
- **Comparison to my architecture:** My architecture places safety enforcement *before* AI reasoning (deterministic gate evaluated first, admissible action space defined before AI generates recommendations). Bajcsy & Fisac's filter operates *after* AI reasoning (task policy proposes, filter evaluates). Both enforce the same principle (safety constraints dominate), but the enforcement point differs: mine is pre-generation restriction, theirs is post-generation filtering.

---

## 11. Baseline Comparison and Evaluation

- **Baseline comparison:** None — theoretical framework paper with no empirical evaluation.
- **Metrics:** None measured. The paper proves Theorem 1 (safety guarantee) but does not empirically validate the framework.
- **CAUTION zone testing:** N/A — no CAUTION mode exists.
- **Safety Dominance Property verification:** Theorem 1 provides a formal guarantee analogous to (but different from) my Safety Dominance Property.
- **Evaluation gaps:** No empirical instantiation. The paper acknowledges the "approximate nature of learning-based generative AI" limits guarantees to statistical assurances.

---

## 12. Key Concepts and Definitions

| Concept | Definition / Description | Relevance |
|---|---|---|
| **Safety filter** | Tuple (π^AI_fallback, Δ, ϕ): fallback policy, safety monitor, intervention scheme that guarantees safety by minimally overriding AI task policy | Direct parallel to my gate function G(S) — both constrain AI output for safety |
| **Maximal safe set Ω*** | Set of AI states from which safety can be maintained for all allowable human behaviours | Analogous to the union of states where G(S) = 1 in my architecture |
| **Safety value function V(z^AI)** | Continuous measure of proximity to failure; V ≥ 0 means safe | Continuous analogue of my discrete safety state S ∈ {SAFE, CAUTION, UNSAFE} |
| **Failure set F^AI** | States where human critical needs are violated | Analogous to my UNSAFE state where G(S) = 0 and A_AI = ∅ |
| **Operational Design Domain (ODD)** | Conditions and behavioural assumptions under which the system can operate safely | Relevant to defining the scope within which my architecture's safety guarantees hold |
| **Predictive action bounds Â^H(z^AI)** | Set-valued mapping delimiting allowable human actions given AI's current state | Formalises the human behaviour assumptions in my system |
| **Values vs. needs** | Values = optimisation objective (reward); needs = hard constraints that must always be satisfied | Aligns with my architecture: AI recommendations optimise utility (values) subject to safety constraints (needs) |

---

## 13. Limitations and Unsolved Problems

- **Stated limitations:**
  - Approximate learning-based components limit guarantees to statistical assurances, not hard certificates
  - Latent state spaces of generative AI are poorly understood — unclear how to specify failure sets in latent space
  - Scalability to high-dimensional systems remains challenging
  - Risk of misuse: the framework's interaction-awareness could be repurposed for manipulation
  - Binary intervention (permit/override) may be overly restrictive in practice

- **Alignment with my research gaps:**
  - The paper implements **binary** governance (permit/override) — confirming the gap for graduated governance with an intermediate CAUTION mode
  - The paper uses a **continuous** safety measure without discrete safety state classification — my tripartite classification S ∈ {SAFE, CAUTION, UNSAFE} provides a simpler, more interpretable model suitable for low-resource contexts
  - The paper does not address **low-resource environments** or domain-specific instantiation
  - The paper does not address **advisory scope restriction** — the AI either outputs its full task policy or is completely overridden; there is no intermediate mode where AI participates with a restricted recommendation set

---

## 14. Methodology Notes

- **Research method:** Theoretical/formal — synthesises control theory and AI safety into a unified mathematical framework. Proves Theorem 1. No empirical evaluation.
- **Alignment with DSR:** Partially — the paper formalises a design artefact (the safety filter) and provides theoretical analysis, but does not prototype or evaluate.
- **Methodological insights:** The game-theoretic formulation and safety value function provide a rigorous mathematical basis that could inform future formalisation of my Safety Dominance Property. The distinction between "values" (optimisation objectives) and "needs" (hard constraints) maps cleanly to my architecture's separation of AI recommendation optimisation from deterministic safety constraints.

---

## 15. Quotable / Citable Points

1. **Safety as dynamic trajectory property:** "The consequences of an AI model's outputs cannot be determined in isolation: they are tightly entangled with the responses and behavior of human users over time" (Abstract). — *Supports my architecture's state-conditioned governance rationale*

2. **Values vs. needs:** "Human values correspond to the optimization objective, whereas human needs correspond to the hard constraints that must always be satisfied" (Section 2). — *Directly parallels my separation of AI recommendation optimisation from deterministic safety constraints*

3. **Safety definition:** "We define safety as the continued satisfaction of the human's critical needs at all times" (Section 2). — *Supports my Safety Dominance Property framing*

4. **Binary filter limitation (implicit):** The intervention scheme is a "simple binary switch (at each time, apply π^AI_§ if deemed safe, else apply π^AI_fallback)" or "a more sophisticated override" (Section 5). — *Citable as evidence that even frontier safety frameworks implement binary governance, not graduated*

5. **Present actions causing future failures:** "Present actions which do not appear to violate constraints can still steer the system into states from which it is impossible to avoid catastrophic failures in the future" (Section 3.1). — *Supports my gate function's pre-emptive approach*

---

## 16. Relation to My Research and Positioning

- **Governance levels implemented:** Full Level 1 (binary participation control via safety filter, with formal guarantee). Partial Level 2 (implicit action restriction via safety monitor, but binary not graduated).
- **State-conditioned governance:** Yes — via continuous safety value function V(z^AI). But no discrete safety state classification.
- **Proximity to (G(S), A_AI(S)):** **Closest formal parallel in the review.** The safety filter's structure (task policy constrained by safety monitor and intervention scheme) is the most formally rigorous instantiation of the governance principle that my architecture also implements. The key differences: (1) their safety measure is continuous, mine is tripartite discrete; (2) their governance is binary (permit/override), mine is tripartite (full/restricted/blocked); (3) their framework targets general human-AI systems in latent space, mine targets a specific domain (coastal fisheries) with explicit environmental variables.
- **Safety Dominance Property comparison:** Theorem 1 is the closest formal analogue to my Safety Dominance Property in the entire review. Both guarantee that AI outputs remain within safety-determined bounds. Theorem 1 is more general (applies to arbitrary latent state spaces) but binary; my Safety Dominance Property is domain-specific but graduated (CAUTION mode).
- **Gap my research fills:** Bajcsy & Fisac demonstrate that even the most sophisticated formal safety frameworks implement binary governance. My architecture introduces the CAUTION mode — a formally distinct intermediate state where AI participates under restricted advisory scope — which is absent from their framework and from all other surveyed literature.

**Positioning paragraph:** Bajcsy & Fisac (2024) provides the **strongest formal foundation** for safety-critical AI governance in my literature review, and serves as a key **gap-evidence paper** for the CAUTION mode contribution. Their Human-AI Safety Filter (Theorem 1) formalises the principle that AI outputs must be constrained to maintain safety for all allowable human behaviours — the closest formal analogue to my Safety Dominance Property. Their two-layer architecture (task policy + safety filter) parallels my architecture's separation of probabilistic AI recommendations from deterministic safety governance. However, their framework implements **binary** governance: the AI either operates fully under its task policy or is completely overridden by the fallback. There is no intermediate mode where AI participates with a restricted recommendation scope. This binary limitation — present even in this state-of-the-art, formally guaranteed framework — is the most compelling evidence that the CAUTION mode gap I identify is genuine and architecturally significant. My research extends the governance principle formalised by Bajcsy & Fisac from a binary filter to a **graduated** governance model with the containment relationship A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅, instantiated in the coastal fisheries domain with explicit environmental state variables and interpretable safety state classification.

---

## 17. Overall Relevance Score

### ⭐⭐⭐⭐⭐ Core

**Justification:** This paper is directly relevant to four core themes (safety-critical AI, AI governance, decision architecture formalisation, human role) and partially relevant to one more (hybrid AI). It provides the most rigorous formal framework for AI safety governance in my entire review, with Theorem 1 serving as the closest formal analogue to my Safety Dominance Property. It simultaneously provides the strongest gap evidence for my CAUTION mode contribution: even this state-of-the-art framework implements binary (permit/override) governance, not graduated governance with an intermediate restricted-participation mode. The paper is a **primary architectural antecedent** (the safety filter architecture parallels my gate-first governance), a **key gap-evidence paper** (binary limitation confirms the CAUTION gap), and a **formal methods reference** (game-theoretic safety formulation, safety value function, Theorem 1) for my dissertation. It belongs alongside AgentSpec, Shields for Safe RL, and Towards Guaranteed Safe AI as a core paper in the review.
