## Literature Review Extraction: Vermaelen & Holvoet (2025)

---

## Early Relevance Check: PROCEED

1. **Does this paper address at least one of the 8 core research themes?** Yes — safety-critical AI decision-making, AI governance/control mechanisms, decision architecture formalisation.
2. **Does this paper contribute to safety-critical AI architecture, AI governance mechanisms, hybrid AI design, formal decision models?** Yes — constraint-based planning with formal safety guarantees, state rules governing permissible actions, soundness/completeness by construction.
3. **Could this paper plausibly be cited in a literature review about graduated AI governance for safety-critical decision support?** Yes — its state rules and action-filtering mechanism represent a form of Level 1 governance (blocking unsafe actions), and its discussion of future work on weighted safety constraints is relevant gap evidence.

**Decision: Proceed with extraction.** Relevance mapping (Section 3) yields 3 Yes → FULL EXTRACTION.

---

### 1. Paper Identity

- **Title:** Tumato 2.0 — A Constraint-Based Planning Approach for Safe and Robust Robot Behavior
- **Authors:** Jan Vermaelen, Tom Holvoet
- **Year:** 2025 (published online 26 July 2024; journal volume dated 2025)
- **Venue:** *Annals of Mathematics and Artificial Intelligence*, 93, 541–567
- **DOI:** https://doi.org/10.1007/s10472-024-09949-3
- **Type:** System design paper with formal methods, extending a prior constraint-based planning framework; includes case study evaluation and performance experiments

---

### 2. Core Contribution

- **Problem addressed:** Generating safe and robust behaviour policies for autonomous robots operating in non-deterministic environments — specifically, ensuring that planned actions never lead to unsafe states even when actions produce unintended (alternative) outcomes.
- **Proposed solution:** An extension of the Tumato constraint-based planning framework that introduces: (1) alternative (non-deterministic) effects for actions, so the planner accounts for foreseeable deviations; (2) declarative *state rules* that constrain reachable states rather than requiring manual enumeration of unsafe state-action pairs; and (3) cost/duration values enabling the planner to choose the most preferred way to restore safety.
- **Main contributions:**
  - Extending Tumato from deterministic-only to non-deterministic action outcomes while preserving soundness and completeness guarantees
  - Introducing state rules as a declarative, less error-prone alternative to reaction rules for safety specification
  - Demonstrating that state rules reduce the number of required safety rules and cover situations the designer may not anticipate
  - Establishing a link between Tumato and Systems-Theoretic Process Analysis (STPA) for identifying unsafe control actions
- **Novelty:** The combination of constraint programming with explicit non-deterministic action modelling (nominal vs. alternative outcomes) and purely declarative safety conditions (state rules) that guarantee — by construction — that no action selected by the policy can lead to an unsafe state under any foreseeable outcome.

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | Partial | Purely rule-based/constraint-based — no probabilistic AI component. However, the architecture is a deterministic constraint layer that governs permissible actions, structurally analogous to the deterministic gate layer in my architecture. |
| Safety-critical AI decision-making | Yes | Core focus: generating policies for autonomous robots where unsafe states must be avoided, including under non-deterministic outcomes. Safety is enforced by construction through constraint satisfaction. |
| AI governance / control mechanisms | Yes | State rules function as a governance mechanism that filters which actions are permissible in each state. This is a form of Level 1 governance — actions that could lead to unsafe states are blocked entirely. |
| Low-resource environments | No | The system is designed for a factory environment with full computational resources; offline policy generation assumes adequate compute. No resource-aware design considerations. |
| Decision architecture formalisation | Yes | Formally defines state vectors, actions with preconditions and effects (nominal + alternative), state rules as logical constraints on reachable states, and the `allowed(a,s)` predicate. Policies are generated via Constraint Satisfaction Problems with provable soundness and completeness. |
| Human role in decision-making | Partial | The human role is limited to specification-time (designing the model, defining state rules). At runtime, the policy executes autonomously. The paper discusses participant-based evaluation of specification usability but not human-in-the-loop decision support. |
| Socio-technical evaluation | Partial | Mentions an ongoing participant-based empirical evaluation assessing usability and specification effectiveness, but results are not yet reported in this paper. |
| Coastal fisheries / maritime domain | No | Case study is an Autonomous Mobile Robot in a factory setting. No maritime or fisheries application. |

**Mid-Extraction Relevance Gate:** 3 Yes (safety-critical, governance, formalisation) + 3 Partial → **FULL EXTRACTION.**

---

### 4. Decision Architecture Analysis

- **Decision-making structure:** The architecture is a **constraint-based offline policy generator**. The system specification (states, actions, preconditions, effects, safety rules, goals) is translated into a set of Constraint Satisfaction Problems (CSPs). Solving these CSPs produces a complete policy — a mapping from every valid state to the action(s) to execute in that state.
- **Layered architecture / governance structure:** There is a single governance layer: state rules constrain which actions are permissible by requiring that all foreseeable outcomes (nominal and alternative) of any selected action satisfy the declared safety conditions. This is structurally a **pre-computation gate** — unsafe actions are excluded from the policy at planning time, not filtered at runtime.
- **Rule-based constraints before AI/probabilistic decisions:** Yes, but the entire system is rule-based/constraint-based. There is no probabilistic AI component. Safety constraints are integrated into the constraint solver and are satisfied by construction.
- **Boundary between deterministic control and AI reasoning:** Not applicable in the traditional sense — there is no AI reasoning module separate from the deterministic planner. The entire decision pipeline is deterministic constraint programming.
- **Failure modes and fallback:** The planner generates a complete policy covering every valid state. If the system arrives in an unsafe state (due to external forces), the policy includes instructions to restore safety in the most preferred way (lowest cost/duration). If no safety-restoring action exists for a state, the planner reports this as feedback to the designer. Unrealizable specifications are detected at planning time.

---

### 5. Formal Model and Mathematical Representation

- **Formal model:** Yes. The system is formally modelled with:
  - **State vector:** Discrete state variables (e.g., S_Location, S_Battery, S_Load, S_Conveyor)
  - **Actions:** Defined with preconditions, nominal effects, alternative effects, and cost/duration values
  - **State rules:** Logical conditions of the form `IF condition THEN constraint` that must hold in all reachable next states
  - **Permissibility predicate:** `allowed(a,s) ⇔ ∀effect ∈ effect(a,s) : effect ⇒ {state_rules}` — an action is allowed only if every possible outcome satisfies all state rules

- **Comparison to DSR pipeline E → S = f(E) → (G(S), A_AI(S)) → AI(E):**
  - The state vector is analogous to **E** (system state), though it represents robot internal state rather than environmental conditions
  - There is no explicit **safety state classification function S = f(E)** mapping to discrete safety levels (SAFE/CAUTION/UNSAFE). Instead, safety is encoded as constraints on reachable states — each state is either valid (assumptions satisfied, state rules maintained) or not
  - The `allowed(a,s)` predicate functions as a combined gate: it blocks actions whose outcomes could violate safety (analogous to **G(S) = 0** for those specific actions). However, this operates at the per-action level, not at a global safety state level
  - There is no concept of a **restricted-but-non-empty admissible action space** that varies by safety classification — actions are either permitted or blocked based on their individual outcomes

- **State-dependent recommendation restriction (A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅)?** No. The system does not classify states into discrete safety levels with different admissible action sets. Each state has its own set of permissible actions determined by preconditions, goals, and state rule satisfaction — but this is not organised into graduated safety tiers.

- **Safety Dominance Property (AI(E) ⊆ A_AI(S))?** The system achieves an analogous guarantee but formulated differently: the policy is **sound by construction** — every action in the policy satisfies all state rules under all foreseeable outcomes. This is a per-action, per-state guarantee rather than a global safety-state-conditioned property. The guarantee is: `∀(a,s) ∈ policy : allowed(a,s)`, which ensures no selected action can violate safety. This is structurally comparable to the Safety Dominance Property but not state-conditioned.

- **Formalisation purpose:** The formalisation is used for automated policy generation (constructive) and provides soundness/completeness guarantees (proof-level). It is not merely descriptive.

---

### 6. Safety State Classification

- **Discrete safety levels?** No. The system does not classify states into discrete risk or safety levels. Instead, it uses a binary distinction: states either satisfy all state rules (safe) or violate at least one (unsafe). There is no intermediate classification.
- **Thresholds or rules:** Safety conditions are specified as logical state rules (propositional logic). Violation is binary — a state either satisfies a rule or it does not.
- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:** Tumato operates with a binary safe/unsafe distinction at the state level. There is no CAUTION equivalent. When the current state is unsafe, the system selects the fastest action to restore safety — but this is a reactive recovery mechanism, not a proactive graduated governance mode.
- **Does the paper differentiate AI recommendation scope across safety levels?** No. All permissible actions in a given state are equally available. There is no concept of restricting the *type* of action (e.g., advisory scope) based on safety classification — only whether a specific action's outcomes are safe.

---

### 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (equivalent to G(S)) | Yes | The `allowed(a,s)` predicate blocks any action whose foreseeable outcomes could violate state rules. At the per-action level, this is a participation gate. However, there is no global system-level "AI off" state — the system always operates; individual actions are filtered. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (equivalent to A_AI(S)) | No | The system does not differentiate *types* of recommendations or restrict recommendation categories by safety state. All permitted actions are treated uniformly. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | No | No classified environmental safety state exists. Governance is per-action, per-state constraint satisfaction, not a two-level state-conditioned architecture. |

- **Binary AI switch or graduated governance?** Neither in the traditional sense. The system implements per-action binary filtering (each action is individually allowed or blocked) rather than a global binary switch or graduated model. This is closer to Level 1 governance applied at action granularity.
- **Level 2 governance?** Not implemented. No distinction between types or categories of actions based on safety state.
- **Support or contradiction for two-level governance pair (G(S), A_AI(S))?** The paper supports the *need* for safety governance of autonomous system actions but implements only per-action Level 1 control. The absence of graduated governance — and the paper's own future work suggestion about weighted safety constraints — provides indirect gap evidence for the two-level model.

---

### 8. Human Role in Decision-Making

- **Human involvement:** The human's role is entirely at **design time** — specifying the system model, actions, goals, and safety rules. At runtime, the policy executes autonomously without human intervention.
- **Decision support vs. automation:** This is **decision automation** — the generated policy dictates exactly which actions to execute in every state. There is no decision support or advisory component.
- **Human interaction at runtime:** None during normal operation. The AMR has an emergency stop button as a physical override, but this is outside the planning framework.
- **Human override / escalation:** Not modelled within the planning framework. The planner reports unrealizable specifications to the designer at planning time, which could be considered a design-time escalation mechanism.

---

### 9. System Constraints and Environment

- **Real-world constraints:** The system accounts for non-determinism (action outcomes may deviate) and resource conflicts (mutually exclusive actions). However, it does not address limited data, limited compute, or unreliable connectivity — the policy is generated offline with full computational resources.
- **Deployment:** The system is validated on a physical AMR in a demo factory. Policies generated by Tumato are executed on real hardware, so this is real-world deployment (though in a controlled environment).
- **Resource-aware design:** Policies are computed offline, so runtime computational cost is negligible (policy lookup). However, the offline planning process itself can be computationally expensive for large state spaces (74 seconds for 2688 valid states).
- **Edge cases:** The system handles unforeseen states by providing recovery actions in the policy. If no recovery is possible, the planner flags those states during planning.

---

### 10. Hybrid AI Taxonomy

- **Type of hybrid AI:** This is **not a hybrid AI system** in the traditional sense — it is a purely constraint-based/rule-based planner with no machine learning or probabilistic AI component. The classification would be:
  - **Constitutional / governance-based:** Safety rules (state rules) constrain the entire action space — no action in the policy can lead to an unsafe state
  - **Closest analogy:** A deterministic safety layer that could, in principle, govern an AI component — but in this paper, there is no AI component to govern

- **Where safety enforcement sits:** Safety is enforced **at planning time** (before any runtime execution). The policy is safe by construction — no runtime safety checking is needed.
- **Two-level governance support?** No. The system implements a single level of governance: binary per-action filtering based on outcome safety. No graduated advisory scope governance.
- **Comparison to my architecture:** Tumato's state rules are structurally analogous to the deterministic gate in my architecture (ensuring safety constraints are never violated), but the entire system is deterministic — there is no probabilistic AI reasoning component to gate. The key structural parallel is: safety constraints override productive goals (analogous to Safety Dominance), but this is not formalised as a state-conditioned two-level governance pair.

---

### 11. Baseline Comparison and Evaluation

- **Baseline comparison:** Yes — the paper compares reaction rules (manual safety specification) against state rules (declarative safety specification) in terms of generated constraints, variables, and execution time.
- **Metrics:** Number of constraints generated, number of internal variables, policy generation time, and qualitative assessment of specification complexity and error-proneness.
- **Evaluation type:** Performance experiments on the AMR case study with varying specification approaches and maximum planning lengths. Real-world deployment on physical AMR (video provided).
- **CAUTION zone testing?** No. There is no CAUTION zone — safety is binary. The evaluation does not test graduated governance behaviour.
- **Safety Dominance verification?** Implicitly — the soundness guarantee of the constraint solver ensures that no policy action can lead to a state rule violation. This is verified by construction rather than by empirical testing.
- **Graduated vs. binary governance comparison?** No — the paper does not compare graduated governance against binary governance because it only implements binary (per-action) governance.
- **Evaluation gaps:**
  - No comparison with other safety-critical planning approaches (MDPs, shielded RL, etc.)
  - Scalability evaluation is limited (one "Large" specification with 2688 states)
  - Participant-based usability evaluation is ongoing but results not reported
  - No evaluation under resource-limited conditions
  - No evaluation of graduated governance modes

---

### 12. Key Concepts and Definitions

- **State rules:** Declarative safety conditions specified as logical constraints on reachable states (`IF condition THEN constraint`), enforced for all foreseeable outcomes of any selected action. A state rule violation means the system has been pushed into an unsafe state by external forces.
- **Nominal vs. alternative effects:** Actions have one intended outcome (nominal) and zero or more foreseeable unintended outcomes (alternative). Nominal effects drive goal-oriented planning; all effects (nominal + alternative) must satisfy safety constraints.
- **`allowed(a,s)` predicate:** Formal permissibility criterion — an action is allowed in a state if and only if every possible outcome satisfies all state rules.
- **Soundness by construction:** The policy generated by the constraint solver is guaranteed to never select an action that could lead to a state rule violation under any foreseeable outcome.
- **Completeness:** The policy provides an action for every valid state — if the system arrives in any valid state, including through alternative effects, it has instructions to proceed.
- **Safety restoration:** When the current state violates a state rule (due to external forces), the planner selects the action(s) that restore safety with minimum cost/duration.
- **STPA (Systems-Theoretic Process Analysis):** A systems-theoretic hazard analysis framework; the paper identifies overlap between STPA's unsafe control action identification and Tumato's state rules.

---

### 13. Limitations and Unsolved Problems

- **Stated limitations:**
  - Requires discrete state variables — continuous environments need a monitoring module to discretise (acknowledged as a notable limitation)
  - Safety restoration is limited to single-step recovery — future work could explore multi-step recovery sequences
  - Safety constraints are treated as equally weighted — no notion of severity differentiation
  - The `allowed(a,s)` predicate covers only foreseeable alternative outcomes — truly unforeseen external events are not guaranteed safe
  - Scalability for very large state spaces remains an open question
  - Participant-based usability evaluation is incomplete

- **Future work identified by authors:**
  - Multi-step safety restoration (allowing sequences of actions in unsafe states)
  - **Weighted safety rules** — varying severity of safety constraints to enable the solver to find globally optimal solutions accounting for different degrees of safety criticality
  - Integration with Linear Temporal Logic for safety rule specification
  - Deeper STPA–Tumato integration

- **Gaps aligned with my research:**
  - **No graduated governance:** The system treats safety as binary — actions are either safe or unsafe. There is no intermediate CAUTION mode where some actions are permitted with restrictions while others are blocked. The authors' own suggestion of weighted safety constraints hints at the need for graduated safety treatment but does not implement it.
  - **No two-level governance model:** There is no separation between participation governance (whether the system acts) and advisory scope governance (what types of actions are permitted). All governance is at a single level: per-action binary filtering.
  - **No Safety Dominance Property for graduated governance:** The soundness guarantee applies uniformly — there is no state-conditioned property that varies the admissible action space across classified safety levels.
  - **No environmental safety state classification:** The system does not classify environmental conditions into safety tiers — it evaluates each action's outcomes individually rather than first classifying the overall environmental state and then determining governance behaviour accordingly.

---

### 14. Methodology Notes

- **Research method:** Formal methods (constraint programming) + system design + case study validation + performance experiments. The approach is constructive — the tool generates provably correct policies from declarative specifications.
- **Alignment with DSR pipeline:** Partial alignment. The paper follows a design → formalise → implement → evaluate trajectory, but it is not framed as Design Science Research. The formalisation is constructive (constraint programming) rather than analytical, and the evaluation is primarily computational performance rather than socio-technical.
- **Methodological takeaways:**
  - The `allowed(a,s)` predicate and state rules provide a clean formal pattern for expressing safety constraints — this could inform how to formally express the relationship between state rules and admissible actions in my architecture
  - The distinction between maintaining safety (preventing entry to unsafe states) and restoring safety (recovering from unsafe states caused by external forces) is a useful conceptual separation that could map to my SAFE/CAUTION/UNSAFE state transitions
  - The idea of cost-weighted safety restoration could inform how to formalise preferred governance actions within the CAUTION state

---

### 15. Quotable / Citable Points

1. **On declarative safety specification (Section 4.2.2):** The paper introduces state rules as constraints on reachable states rather than manual enumeration of unsafe state-action combinations, arguing this significantly reduces specification errors — citable for motivation of declarative safety governance.

2. **On binary safety treatment (Section 7, Discussion — Future work):** The authors explicitly identify that safety constraints are currently treated with equal weight and suggest that weighting of safety rules by severity should be considered in future work — directly citable as gap evidence for graduated safety governance.

3. **On soundness by construction (Section 5.1):** The constraint-based approach guarantees that the generated policy never selects actions violating state rules under any foreseeable outcome — citable as an example of constructive safety guarantee (analogous to but different from the Safety Dominance Property).

4. **On the `allowed(a,s)` predicate (Section 4.2.2):** The formal permissibility criterion `allowed(a,s) ⇔ ∀effect ∈ effect(a,s) : effect ⇒ {state_rules}` — citable as a per-action safety gate formalism to contrast with the global state-conditioned governance pair (G(S), A_AI(S)).

5. **On safety restoration preference (Section 3.2 / 4.1):** When the system is in an unsafe state, the planner selects the recovery action with minimum cost/duration — citable as evidence that even within binary safety frameworks, there is emerging recognition that not all safety responses should be treated identically (precursor to graduated governance).

---

### 16. Relation to My Research and Positioning

- **Level 1 governance (participation control):** Yes — implemented at per-action granularity via the `allowed(a,s)` predicate and state rules. Actions whose outcomes could violate safety conditions are blocked.
- **Level 2 governance (output-scope control):** No — the system does not differentiate types or categories of actions based on safety classification. All permitted actions are treated uniformly regardless of the system's safety proximity.
- **State-conditioned Level 2?** Not applicable — no Level 2 governance exists.
- **Proximity to (G(S), A_AI(S))?** The system implements a strong form of Level 1 governance (per-action gating with formal soundness guarantees) but lacks: (a) a global environmental safety state classification, (b) a two-level governance structure separating participation from advisory scope, and (c) a graduated model where the admissible action space narrows progressively across safety tiers.
- **Formal safety property comparable to Safety Dominance?** The soundness guarantee (`∀(a,s) ∈ policy : allowed(a,s)`) is comparable in spirit — it ensures system outputs always satisfy safety constraints. However, it is not state-conditioned (no S ∈ {SAFE, CAUTION, UNSAFE}) and does not express graduated containment (A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅).
- **Gap my research addresses:** Tumato demonstrates that formal safety governance can be achieved through constraint-based action filtering, but it operates with binary safety (safe/unsafe) and single-level governance (action permitted or blocked). The gap is: (1) no intermediate governance mode where the system continues operating under restricted scope rather than full permission or full blocking; (2) no environmental safety state classification driving graduated governance; (3) no two-level governance pair. The authors' own identification of weighted safety constraints as future work signals awareness of this limitation.

**Positioning paragraph:** Vermaelen and Holvoet (2025) contribute a formally rigorous approach to safety governance in autonomous systems through constraint-based planning with declarative state rules. Their `allowed(a,s)` predicate and soundness-by-construction guarantee represent a strong implementation of Level 1 governance — ensuring no action in the generated policy can lead to an unsafe state under any foreseeable outcome. This positions the paper as **supporting evidence for the feasibility of formal safety governance** in autonomous decision-making. However, the system's binary safety treatment (actions are either fully permitted or fully blocked, with no intermediate mode) and single-level governance structure (no separation between participation governance and advisory scope governance) exemplify the gap that my research addresses. The authors' own acknowledgement that safety constraints should be weighted by severity, and that multi-step recovery strategies warrant investigation, indirectly supports the motivation for a graduated governance model with a CAUTION state offering restricted-but-non-empty AI participation. In my literature review, this paper serves as **gap evidence from the robotics/constraint-programming domain** — demonstrating that even sophisticated formal safety frameworks default to binary governance, reinforcing the claim that graduated two-level governance is an unaddressed contribution.

---

### 17. Overall Relevance Score

**⭐⭐ Low**

**Justification:** The paper is a well-formalised contribution to safety-critical robot behaviour planning with strong formal guarantees, but it operates in a different domain (factory robotics), uses a purely deterministic constraint-based approach (no hybrid AI with probabilistic reasoning), does not address low-resource environments, and implements only binary single-level governance. Its primary value to my research is as **gap evidence** — demonstrating that formal safety frameworks in robotics default to binary action gating without graduated governance — and as a minor **formalisation reference** for the `allowed(a,s)` predicate pattern. It does not address the core two-level governance gap, environmental safety state classification, or advisory scope restriction. The relevance is limited to background/gap-evidence positioning rather than direct architectural comparison.

**Recommended citation uses:**
- Gap evidence (robotics domain): binary safety governance even in formally rigorous constraint-based systems
- Future work on weighted safety constraints as indirect motivation for graduated governance
- The `allowed(a,s)` formalism as a per-action governance pattern to contrast with global state-conditioned governance
