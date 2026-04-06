## Literature Review Extraction
### Chen, Kang & Li (2025) — SHIELDAGENT

---

### 1. Paper Identity

- **Title:** SHIELDAGENT: Shielding Agents via Verifiable Safety Policy Reasoning
- **Authors:** Zhaorun Chen, Mintong Kang, Bo Li
- **Year:** 2025
- **Venue:** Proceedings of the 42nd International Conference on Machine Learning (ICML), Vancouver, Canada. PMLR 267.
- **arXiv:** 2503.22738v2
- **Type:** System design + benchmark paper

---

### 2. Core Contribution

- **Problem:** LLM-based autonomous agents (web browsing, GUI navigation, embodied control) are vulnerable to adversarial attacks and malicious instructions. Existing guardrails are designed for LLMs as models, not as agentic systems operating through sequential interactions with dynamic environments. Safety policies encoded in lengthy regulation documents (EU AI Act, corporate handbooks) are difficult to systematically extract, verify, and enforce.
- **Proposed solution:** SHIELDAGENT — the first LLM-based guardrail agent that shields other agents' action trajectories by enforcing explicit safety policy compliance through probabilistic logical reasoning and formal verification.
- **Main contributions:**
  1. An Automated action-based Safety Policy Model (ASPM) that extracts verifiable LTL rules from policy documents, iteratively refines them, and organises them into action-based probabilistic rule circuits
  2. A guardrail inference framework that retrieves relevant rule circuits per invoked action, generates shielding plans, executes formal verification code, and produces binary safety labels with explanations
  3. SHIELDAGENT-BENCH — a benchmark of 3,110 safety-related pairs of agent instructions and action trajectories across 6 web environments and 7 risk categories
  4. SOTA performance: 11.3% improvement over prior methods, 90.1% rule recall, 64.7% reduction in API queries, 58.2% reduction in inference time
- **Novelty:** Unlike prior guardrails that rely on text-based content filtering (LlamaGuard, GuardAgent), SHIELDAGENT operates on *action trajectories* (not text content), uses *formal LTL verification* (not heuristic filtering), and enforces *explicit external policy documents* (not internal model knowledge). The action-based probabilistic circuit architecture and relative safety condition (barrier certificate-inspired) are novel.

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | **Yes** | Core architecture: deterministic LTL rules for formal verification combined with probabilistic Markov Logic Network inference for safety certification. Rules are hard logical constraints; weights are learned probabilistic parameters. |
| Safety-critical AI decision-making | **Yes** | Designed for high-stakes agentic applications where unsafe actions can cause privacy breaches, financial losses, and life-threatening failures. Explicitly motivated by safety-critical deployment concerns. |
| AI governance / control mechanisms | **Yes** | Central focus. SHIELDAGENT is a runtime governance mechanism that enforces safety policy compliance on autonomous agents' action trajectories. Extracts rules from formal policy documents (EU AI Act, corporate handbooks) and verifies each action against relevant rule circuits. |
| Low-resource environments | **No** | Requires GPT-4o API calls, embedding models, formal verification tools (Stormpy, Prover9), and fine-tuned InternVL2-2B models. Cloud-dependent, compute-intensive architecture. |
| Decision architecture formalisation | **Yes** | Formally defined: ASPM as G_ASPM = (P, R, π_θ) with predicate space P = {P_a, P_s}, rule space R = {R_a, R_p}, and probabilistic logic model π_θ. Safety condition formalised via barrier certificate: l_s(a_i) = 1 iff P_θ(μ_{pa}=1) − P_θ(μ_{pa}=0) ≥ ε. LTL syntax for rule specification. |
| Human role in decision-making | **Partial** | Users can adjust the safety threshold ε and customise tools/policies. Human experts may review optimised rules. However, the guardrail decision itself is automated — the human is not in the decision loop at runtime. |
| Socio-technical evaluation | **No** | Evaluation is purely technical: accuracy, false positive rate, rule recall, inference cost. No socio-technical evaluation with end users. |
| Coastal fisheries / maritime domain | **No** | Domain is web agents (shopping, CMS, Reddit, GitLab, Maps, SuiteCRM). |

**Mid-Extraction Relevance Gate:** 4 Yes + 1 Partial = **≥ 3 Yes → FULL EXTRACTION**

---

### 4. Decision Architecture Analysis

- **Architecture structure:** Two-stage pipeline:
  1. **Offline: ASPM Construction** — Policy documents → structured policy extraction → LTL rule extraction → iterative optimisation (Verifiability Refinement + Redundancy Pruning) → action-based probabilistic circuit clustering → weight learning from training data
  2. **Online: Guardrail Inference** — For each agent action a_i: extract action predicates → retrieve relevant rule circuits → generate shielding plan → execute verification operations (Search, Binary-Check, Detect, Formal Verify) → assign predicate truth values → generate formal verification code → probabilistic inference → binary safety label + violated rules + explanation

- **Safety constraint mechanism:** LTL rules extracted from external policy documents (EU AI Act, GitLab handbook, etc.). Rules are organised into action-based circuits — each action type has an associated set of relevant rules. Verification is formal (model checking via Prover9/Mace4) rather than heuristic.

- **Rule-based constraints before AI:** **Yes, structurally.** The ASPM is a rule-based knowledge graph that governs the protected agent's actions. The guardrail agent (SHIELDAGENT) sits between the protected agent and the environment, verifying each action before it executes. However, note that SHIELDAGENT itself uses an LLM for plan generation and tool orchestration — so the guardrail *implementation* involves AI, but the *governance logic* is rule-based (LTL + formal verification).

- **Fallback behaviour:** When an action is flagged as unsafe, SHIELDAGENT provides violated rules, explanations, and remediation suggestions. In the online guardrail setting (Table 4), feedback is sent to the protected agent to adjust behaviour. The system does not define a fallback action or degraded mode — it blocks and explains.

- **Override mechanism:** The threshold ε is user-adjustable, allowing trade-off between safety stringency and permissiveness. However, there is no runtime override by a human decision-maker.

---

### 5. Formal Model and Mathematical Representation

- **Formal model:** Yes — formally defined at multiple levels:
  - **ASPM structure:** G_ASPM = (P, R, π_θ) where P = {P_a, P_s} (action and state predicates), R = {R_a, R_p} (action and physical rules), π_θ = {C^{pa}_{θa} | pa ∈ P_a} (action-based probabilistic circuits)
  - **Guardrail formulation:** (l_s, V_s, T_s) = A_s(a_i | (o_i, H_{<i}, G_ASPM)) producing safety label, violated rules list, and textual explanation
  - **LTL rule format:** r = [P_r, T_r, φ_r, t_r] with predicates, natural language description, LTL formula, and rule type
  - **Probabilistic inference via Markov Logic Network:** P_θ(μ_{pa}=1 | {μ_{ps}=v_s}) = (1/Z) exp(Σ_{r∈R_{pa}} θ_r I[μ ~ r])
  - **Relative safety condition (barrier certificate):** l_s(a_i) = 1 iff P_θ(μ_{pa}=1) − P_θ(μ_{pa}=0) ≥ ε
  - **Weight learning via guardrail hinge loss:** L_g(θ) = E_{(ζ,Y)~D} max(0, −y^{(i)}(P_θ(μ^{(i)}_{pa}=1) − P_θ(μ^{(i)}_{pa}=0)))

- **Comparison to my pipeline E → S = f(E) → (G(S), A_AI(S)) → AI(E):**
  - SHIELDAGENT does **not** classify environmental conditions into discrete safety states. There is no S = f(E) producing {SAFE, CAUTION, UNSAFE}.
  - The governance is **policy-conditioned** (static rules from documents), not **environmental-state-conditioned** (rules varying by classified environmental state).
  - The output is a binary safe/unsafe label per individual action — not a state-conditioned restriction on the admissible recommendation space.
  - The ASPM is closest to a sophisticated implementation of per-action Level 1 governance with rich formal backing.

- **State-dependent recommendation restriction:** **No.** The rule set R is fixed (extracted from policy documents, learned weights from training data). The same rules apply regardless of environmental state. There is no mechanism where the admissible action space narrows under different classified states — the same rule circuits are evaluated with the same weights regardless of context. The ε threshold is user-set, not state-conditioned.

- **Safety Dominance Property equivalent:** **Partial.** The relative safety condition l_s(a_i) = 1 iff P_θ(μ_{pa}=1) − P_θ(μ_{pa}=0) ≥ ε provides a formal guarantee that actions are only permitted when their safety probability exceeds a threshold. This is a per-action safety guarantee, not an output-scope guarantee. It does not guarantee AI(E) ⊆ A_AI(S) because there is no classified state S conditioning the admissible space.

- **Formalisation purpose:** Operational — the LTL rules and probabilistic circuits are used for actual runtime verification, not just descriptive modelling.

---

### 6. Safety State Classification

- **Discrete risk/safety levels:** **No.** There is no classification of environmental or operational conditions into discrete safety states. The system evaluates individual actions against a fixed policy model. The seven risk *categories* (access restriction, content restriction, hallucination, instruction adherence, operational restriction, error patterns, long-term risks) classify *types of violation*, not *environmental states*.
- **Comparison to S = f(E):** Not applicable. SHIELDAGENT does not have an environmental state classification function. The "state" in the ASPM is the state predicates P_s describing system/environment conditions at a given moment, but these are per-step boolean observations, not a classified safety state that conditions governance behaviour.
- **CAUTION mode equivalent:** **No.** The system produces binary safe/unsafe per action. There is no intermediate mode where the protected agent participates with restricted output scope. The ε threshold could theoretically be adjusted to create softer/harder gating, but this is a static user setting, not a runtime state-conditioned scope restriction.

---

### 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (G(S)) | **Yes** | Binary safe/unsafe decision per action. If unsafe, the action is blocked and feedback is provided. This is per-action participation governance with formal verification backing. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | **No** | The system does not restrict the *types* of actions the protected agent may propose based on classified state. It evaluates each proposed action individually against a fixed policy model. The protected agent's action space is not narrowed as a function of environmental state. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | **No** | No environmental state classification. Governance is policy-conditioned (static rules), not state-conditioned. |

- **Binary vs. graduated:** Binary. Each action receives a safe/unsafe label. The probabilistic margin (P_θ(μ_{pa}=1) − P_θ(μ_{pa}=0)) is continuous, but the final decision is thresholded to binary.
- **Level 2 governance:** Absent. No state-conditioned restriction on action scope.
- **Support for two-level governance pair:** The paper **supports the need** for structured policy governance but does not implement state-conditioned scope restriction. The distinction between action rules (R_a) and physical rules (R_p) — where physical rules capture environmental constraints that inform action rule evaluation — is architecturally interesting but does not produce a graduated governance model. The ε threshold is a *user-configurable parameter*, not a *state-conditioned governance function*.

---

### 8. Human Role in Decision-Making

- **Human involvement:** Minimal at runtime. Users set ε and configure policies. Human experts may review extracted rules during ASPM construction. At runtime, the guardrail decision is fully automated.
- **Decision support vs. automation:** Pure **decision automation** for the guardrail function. The protected agent is also autonomous. In the online guardrail setting, SHIELDAGENT provides feedback to the protected agent (not to a human) to adjust behaviour.
- **Human override:** Not addressed. No mechanism for a human to override the guardrail decision at runtime.
- **Relevance to my research:** My architecture is decision *support* for a human decision-maker. SHIELDAGENT governs an autonomous agent. The architectural patterns (policy extraction → formal rules → runtime verification) are transferable, but the governance target is fundamentally different.

---

### 9. System Constraints and Environment

- **Real-world constraints:** Not designed for resource-constrained environments. Requires GPT-4o API access, embedding models, formal verification tools, fine-tuned vision-language models. Average inference time is 31–34 seconds per sample with ~10 API queries.
- **Deployment context:** Web agent environments (Shopping, CMS, Reddit, GitLab, Maps, SuiteCRM). Realistic but not resource-limited.
- **Resource-aware design:** Some efficiency optimisations: action-based circuit clustering reduces inference complexity (only relevant circuits evaluated per action); hybrid memory module caches workflows; 64.7% reduction in API queries vs. baselines. But still cloud-dependent.
- **Edge cases:** Weaker performance on hallucination-related risks (requires external knowledge beyond policy). Environment-based attacks easier to detect than agent-based attacks.

---

### 10. Hybrid AI Taxonomy

- **Hybrid AI type:** **Constitutional / governance-based** — a rule layer (LTL rules in ASPM) constrains AI agent behaviour. Additionally, **neuro-symbolic** elements: LLM generates shielding plans and orchestrates tools, while formal verification (Prover9/Mace4) checks logical consistency, and probabilistic inference (Markov Logic Network) produces safety scores.
- **Safety enforcement position:** **After AI reasoning** — SHIELDAGENT evaluates the protected agent's action *after* the agent proposes it but *before* it reaches the environment. Post-hoc verification with pre-execution blocking.
- **Two-level governance support:** **No.** Single-level binary control per action. The sophisticated formal machinery (LTL, MLN, barrier certificates) all serve the same binary safe/unsafe decision. No graduated scope restriction.
- **Comparison to my architecture:** Both architectures use deterministic rules to constrain AI behaviour. However: (1) SHIELDAGENT's rules are policy-derived and static; mine are environmental-state-conditioned and dynamic. (2) SHIELDAGENT produces binary per-action decisions; mine produces state-conditioned scope restrictions on recommendation types. (3) SHIELDAGENT governs autonomous agents; mine governs a decision-support system for human decision-makers.

---

### 11. Baseline Comparison and Evaluation

- **Baselines:** Direct prompt (GPT-4o with full policy), Rule Traverse (per-rule GPT-4o evaluation), GuardAgent (prior SOTA guardrail agent).
- **Metrics:** Guardrail accuracy (ACC), false positive rate (FPR), average rule recall rate (ARR), number of API queries (NoQ), inference time.
- **Evaluation type:** Benchmark-based (SHIELDAGENT-BENCH + 3 existing benchmarks). Online guardrail evaluation with AWM web agent. No formal property verification.
- **CAUTION zone testing:** **No.** No intermediate mode tested. All evaluation is binary safe/unsafe.
- **Safety Dominance Property verification:** **No.** The relative safety condition is evaluated empirically (accuracy metrics), not formally verified as a system-level property.
- **Graduated vs. binary comparison:** **No.** No comparison between graduated and binary governance.
- **Evaluation gaps:** No testing of graduated modes, no resource-constrained deployment evaluation, no socio-technical evaluation, no human-in-the-loop testing, no environmental-state-conditioned governance evaluation.

---

### 12. Key Concepts and Definitions

| Concept | Definition / Relevance |
|---|---|
| **Action-based Safety Policy Model (ASPM)** | Logical knowledge graph G_ASPM = (P, R, π_θ) encoding safety constraints from policy documents as LTL rules organised into action-based probabilistic circuits. Core innovation of the paper. |
| **Action predicates (P_a) vs. State predicates (P_s)** | Action predicates represent target actions (e.g., delete_data); state predicates represent environmental conditions (e.g., is_private). Analogous to but distinct from the action space / state space in my architecture. |
| **Action rules (R_a) vs. Physical rules (R_p)** | Action rules constrain target actions; physical rules capture internal system constraints on state variables. Physical rules enhance robustness but don't directly constrain actions. |
| **Relative safety condition** | l_s(a_i) = 1 iff P_θ(μ_{pa}=1) − P_θ(μ_{pa}=0) ≥ ε. Inspired by control barrier certificates. Compares safety probability of executing vs. not executing an action. |
| **Probabilistic rule circuits** | Action-based circuits where rules are assigned soft weights θ_r indicating relative importance. Enables efficient retrieval and inference per action type. |
| **Verifiability Refinement (VR)** | Iterative process to make extracted rules accurate, verifiable, and atomic. Includes vagueness estimation via embedding similarity. |
| **Redundancy Pruning (RP)** | Global optimisation step that clusters semantically similar rules and merges redundant predicates. |

---

### 13. Limitations and Unsolved Problems

- **Stated limitations:**
  1. Weaker performance on hallucination risks requiring external knowledge beyond extracted policies
  2. Dependent on quality of policy extraction (GPT-4o-based, may miss nuances)
  3. High computational requirements (GPT-4o API, embedding models, formal verification tools)
  4. Evaluated only in web agent environments — generalisability to other domains undemonstrated

- **Unstated but identifiable limitations:**
  1. Binary safe/unsafe output — no graduated governance or restricted-scope intermediate mode
  2. Static policy model — rules are fixed after extraction/training, not conditioned on runtime environmental state
  3. No human in the decision loop at runtime
  4. No formal Safety Dominance Property — safety guarantee is probabilistic and per-action, not a system-level property over classified states

- **Gaps aligned with my research:**
  - **Two-level governance gap:** SHIELDAGENT implements sophisticated Level 1 governance (per-action binary allow/block with formal verification) but no Level 2 (state-conditioned scope restriction). The protected agent either gets full permission or gets blocked — there is no CAUTION mode with restricted action types.
  - **Environmental state conditioning gap:** Rules are policy-derived and static. No mechanism conditions governance on classified environmental state. The same rules and weights apply regardless of whether conditions are safe, cautious, or dangerous.
  - **Safety Dominance Property gap:** The relative safety condition is a per-action probabilistic guarantee, not a formal property ensuring all AI outputs fall within a state-conditioned admissible space.

---

### 14. Methodology Notes

- **Research method:** System design + empirical evaluation. ASPM construction is a pipeline (extraction → optimisation → training). Evaluation is benchmark-based with ablation studies.
- **DSR alignment:** Partial. The ASPM construction follows a design-build-evaluate cycle, but not explicitly framed as Design Science Research. No formal proof of system properties.
- **Informing my research:**
  - The LTL rule extraction pipeline (policy documents → structured rules → iterative refinement) is methodologically interesting for formalising safety constraints, though my architecture derives constraints from environmental state rather than policy documents
  - The action-based circuit clustering — organising rules by action type for efficient retrieval — is a practical pattern that could inform implementation of A_AI(S) where different recommendation types have different rule sets
  - The relative safety condition (barrier certificate-inspired) is a novel formal mechanism that could complement the Safety Dominance Property as an alternative per-action guarantee

---

### 15. Quotable / Citable Points

1. **Guardrail gap for agents:** "Existing guardrails primarily focus on LLMs as models, while failing to safeguard them as agentic systems due to two key challenges: (1) LLM-based agents operate through sequential interactions with dynamic environments..." (Section 1, p.1) — Motivates the need for governance beyond content filtering.

2. **Policy enforcement challenge:** "Safety policies governing these agents are often complex and encoded in lengthy regulation documents... making it difficult to systematically extract, verify, and enforce rules across different platforms." (Section 1, p.1) — Supports the argument for structured, formal governance mechanisms.

3. **Binary guardrail output:** The system produces "a binary flag l_s indicating whether action a_i is safe" (Section 3.1, p.3) — Confirms binary governance design.

4. **Adjustable threshold:** "Users are allowed to adjust ε to adapt to different levels of safety requirements (e.g. higher ε for more critical safety needs)." (Section 3.2.4, p.5) — Shows awareness that safety stringency should vary, but implements this as a static user parameter rather than a runtime state-conditioned mechanism.

5. **Online guardrail effectiveness:** SHIELDAGENT achieves "the highest policy compliance rate" as a "System 2" post-verification module copiloting with task agents. (Section 5.2, p.8) — Validates the runtime guardrail paradigm.

---

### 16. Relation to My Research and Positioning

- **Level 1 governance:** **Yes** — sophisticated per-action participation governance with LTL formal verification, probabilistic inference, and barrier certificate-inspired safety condition. Among the most formally rigorous Level 1 implementations in the surveyed literature.
- **Level 2 governance:** **No** — no restriction of the protected agent's admissible action scope based on classified state.
- **State-conditioned:** **No** — governance is policy-conditioned (static rules from documents), not environmental-state-conditioned.
- **Two-level governance pair proximity:** Closer than basic shielding methods (has formal rule structure, action-type-based circuit organisation, and probabilistic weighting) but still fundamentally binary per action. The distinction between action predicates and state predicates is structurally adjacent to the G(S)/A_AI(S) distinction but is not used to produce graduated governance.
- **Safety Dominance Property:** Not present. The relative safety condition is per-action and probabilistic, not a system-level property over classified states.
- **Gap my research addresses:** SHIELDAGENT demonstrates state-of-the-art in formal policy-based Level 1 governance. My architecture extends this paradigm by: (1) introducing environmental state classification S = f(E) as the governance condition, (2) adding Level 2 advisory scope governance A_AI(S) that restricts recommendation types by classified state, and (3) defining a formal Safety Dominance Property that guarantees AI outputs fall within the state-conditioned admissible space.

**Positioning paragraph:** SHIELDAGENT represents the most formally sophisticated per-action guardrail system in the surveyed literature, combining LTL rule extraction from policy documents, Markov Logic Network probabilistic inference, and barrier certificate-inspired safety conditions. It demonstrates that rich formal machinery can be deployed for runtime governance of AI agents. However, its governance remains single-level (binary allow/block per action) and policy-conditioned (static rules regardless of environmental state). It does not classify environmental conditions into safety states, does not restrict the agent's admissible action scope as a function of classified state, and does not define a system-level Safety Dominance Property. This paper should be cited in Section 2.2 as a strong example of formal Level 1 governance and runtime policy enforcement, and in the research gap section as evidence that even the most advanced guardrail systems remain limited to binary per-action governance without state-conditioned scope restriction. The ASPM's distinction between action rules and physical rules, and the action-based circuit clustering, are architecturally adjacent to the G(S)/A_AI(S) pair but are not used to produce graduated governance — making SHIELDAGENT a useful contrast point for motivating Level 2.

---

### 17. Overall Relevance Score

**⭐⭐⭐⭐ High**

Among the most formally sophisticated guardrail systems reviewed. Directly relevant as a strong Level 1 governance example and as contrast/baseline for the two-level governance gap argument. The ASPM architecture (policy extraction → LTL rules → action-based circuits → probabilistic inference) provides a rich formal comparator. The binary output limitation and absence of environmental state conditioning directly support the gap claim. Useful for Section 2.2 (formal governance mechanisms), Section 2.3 (gap evidence — even ICML-level guardrail systems remain binary), and potentially the formalisation chapter (barrier certificate comparison with Safety Dominance Property).
