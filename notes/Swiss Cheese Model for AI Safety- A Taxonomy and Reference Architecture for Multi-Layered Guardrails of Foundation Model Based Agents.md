## Literature Review Extraction: Shamsujjoha et al. (2025)

---

### 1. Paper Identity

- **Title:** Swiss Cheese Model for AI Safety: A Taxonomy and Reference Architecture for Multi-Layered Guardrails of Foundation Model Based Agents
- **Authors:** Md Shamsujjoha, Qinghua Lu, Dehai Zhao, Liming Zhu
- **Year:** 2025
- **Venue:** IEEE 22nd International Conference on Software Architecture (ICSA), pp. 37–48
- **DOI:** 10.1109/ICSA65012.2025.00014
- **Type:** SLR-derived taxonomy + reference architecture (32 selected studies)
- **Note:** Already referenced in extraction prompt template as existing literature context for guardrail taxonomies.

---

### 2. Core Contribution

- **Problem:** Existing guardrail approaches for FM-based agents are single-layered, narrowly applied to specific artifacts (prompts or outputs), and insufficient for managing autonomous, non-deterministic agent behaviour. If any single guardrail fails, risks bypass it.
- **Solution:** (1) Comprehensive taxonomy of runtime guardrails with two dimensions: 14 quality attributes (accuracy, efficiency, privacy, security, safety, fairness, compliance, generalizability, customizability, adaptability, traceability, portability, interoperability, interpretability) and design options (actions, targets, rules, applicability scope, modality, underlying models). (2) Swiss Cheese Model–inspired reference architecture for multi-layered guardrails across three dimensions: quality attributes × pipelines (prompts, intermediate results, final results) × artifacts (goals, context, memory, reasoning, plans, workflows, tools, knowledge bases, other agents, FMs).
- **Key insight:** Each guardrail layer may have weaknesses ("holes in the Swiss cheese"), but combined layers create robust defence. Multi-layered guardrails across different dimensions compensate for individual layer failures.

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | Partial | Identifies rule-based, narrow ML, FM-based, and hybrid models as underlying guardrail techniques. Hybrid guardrails integrate rule-based approaches with ML adaptability |
| Safety-critical AI decision-making | Yes | AI safety is the core concern — preventing harmful outputs, misinformation, privacy breaches, and unsafe actions from FM-based agents |
| AI governance / control mechanisms | Yes | Guardrails are explicitly defined as "mechanisms integrated into an agent's architecture to safeguard its behavior during runtime, preventing undesirable or unsafe behaviors." The taxonomy provides the most comprehensive classification of runtime AI governance actions available |
| Low-resource environments | No | Targets FM-based agents requiring substantial compute (foundation models, LLMs) |
| Decision architecture formalisation | Partial | Reference architecture with defined components and information flows (Fig. 3). Taxonomy provides structured classification. However, not formalised as mathematical pipeline with state variables or safety properties |
| Human role in decision-making | Partial | Human intervention is one of 13 guardrail actions — "requires humans to review and approve specific outputs or decisions." Fall back, defer, and flag also involve human escalation |
| Socio-technical evaluation | No | No socio-technical evaluation; architecture is conceptual, derived from SLR |
| Coastal fisheries / maritime domain | No | FM-based agent domain (chatbots, autonomous agents) |

**Mid-Extraction Relevance Gate:** 2 Yes, 3 Partial → **REDUCED EXTRACTION**

---

### 4. Decision Architecture Analysis

- **Architecture:** Swiss Cheese Model reference architecture (Fig. 3) with four components:
  1. **External environment** — users, tools, knowledge bases, other agents
  2. **Agent components** — context engine, reasoning & planning, workflow execution, memory
  3. **Multi-layered runtime guardrails** — structured across quality attributes × pipelines × artifacts
  4. **AgentOps infrastructure** — continuous monitoring and logging
- **Layered structure:** Multi-layered by design. Each guardrail "slice" addresses a specific combination of quality attribute, pipeline stage, and/or artifact. Layers compensate for each other's weaknesses.
- **Rule-based constraints on AI:** Guardrails can be rule-based, ML-based, FM-based, or hybrid. Rule-based guardrails "utilize predefined rules to monitor and control FM-based agents behavior" and "implement strict and deterministic guidelines." Applied at input (prompts), intermediate results, and output (final results).
- **Boundary between deterministic and AI:** In hybrid guardrails, rule-based approaches handle well-defined parameters while ML adapts to new scenarios. The boundary is at the guardrail layer level, not at the system architecture level.
- **Failure modes / fallback:** Fall back action "redirects to the previous step and state." Human intervention for sensitive decisions. Isolate action segregates compromised components. Redundancy provides backup processes.

**Critical observation for governance analysis:** The guardrail actions taxonomy (Fig. 2) provides 13 distinct runtime governance actions: block, filter, flag, modify, validate, parallel calls, retry, fall back, human intervention, defer, isolate, redundancy, evaluate. This is the most granular classification of AI output governance actions in the literature. However, these actions are applied per-artifact and per-pipeline-stage — they are not conditioned on classified environmental safety state.

---

### 5. Formal Model and Mathematical Representation

- **Formal model:** None. The taxonomy and architecture are classificatory and descriptive, not mathematical. No state variables, gate functions, admissible action spaces, or safety properties are formally defined.
- **Comparison to DSR pipeline:** The guardrail targets (prompts → intermediate results → final results) map loosely to pipeline stages, and the artifact-level guardrails (goals, plans, tools, etc.) map to different system components. However, there is no E → S = f(E) → (G(S), A_AI(S)) → AI(E) equivalent. Guardrails are applied based on artifact type and quality attribute, not based on classified environmental state.
- **State-dependent recommendation restriction:** Not implemented. The taxonomy includes "context-dependent rules" that "adjust the implementation of guardrails based on the system's specific operational context" — this is the closest element to state-conditioned governance. However, "context" here refers to data context (user location, regulatory environment), not classified environmental safety state.
- **Safety Dominance Property:** Not defined. No formal guarantee that AI outputs fall within state-determined bounds.

---

### 6. Safety State Classification

- **Discrete safety levels:** Not defined. The taxonomy classifies guardrails by quality attribute, action type, target, rule type, scope, and modality — but does not classify environmental or operational states into discrete safety levels.
- **Comparison to S = f(E):** No parallel. Guardrail activation is per-artifact and per-quality-attribute, not per-classified-environmental-state.
- **AI recommendation scope across safety levels:** Not differentiated by safety state. The same guardrail configuration applies regardless of environmental conditions (unless context-dependent rules are manually configured per deployment context).

---

### 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (G(S)) | Partial | "Block" action prevents AI from processing/outputting specific content. "Fall back" redirects to previous state. "Isolate" segregates compromised components. These can effectively disable AI for specific artifacts. However, not triggered by classified environmental state |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | Yes | The most comprehensive Level 2 taxonomy available. Guardrails constrain what AI may output across 13 action types, applied to 14 artifact/pipeline targets. Filter, modify, validate, flag actions restrict AI output scope. However, scope restrictions are per-artifact/per-quality-attribute, not per-environmental-safety-state |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | No | No environmental state classification. Guardrail configurations are static (per deployment context) or context-dependent (per data context), not dynamically conditioned on classified environmental safety state |

- **Governance type:** **Level 2 (output-scope governance) comprehensively taxonomised; Level 1 (participation) partially addressed.** This paper provides the definitive taxonomy of *what kinds of governance actions can be applied to AI output*. The gap: it does not specify *when* different governance configurations should be activated based on environmental conditions.
- **Rule types as graduated governance precursor:** The taxonomy identifies four rule types: uniform, priority-enabled, context-dependent, and negotiable. **Context-dependent rules** — which "adjust the implementation of guardrails based on the system's specific operational context" — are the closest concept to my state-conditioned governance. However, "context" is data/deployment context, not classified environmental safety state.

---

### 12. Key Concepts and Definitions

- **Guardrails:** "Mechanisms integrated into an agent's architecture to safeguard its behavior during runtime, preventing undesirable or unsafe behaviors."
- **Swiss Cheese Model for AI Safety:** Multi-layered defence where each layer (guardrail) has potential weaknesses ("holes"), but combined layers create robust protection. Adapted from risk management to AI agent safety.
- **Guardrail actions (13 types):** Block, filter, flag, modify, validate, parallel calls, retry, fall back, human intervention, defer, isolate, redundancy, evaluate — the most comprehensive taxonomy of runtime AI governance actions.
- **Guardrail targets:** Applied across pipelines (prompts, intermediate results, final results) and artifacts (goals, context, memory, reasoning, plans, workflows, tools, knowledge bases, other agents, FMs).
- **Rule types:** Uniform (same across scenarios), priority-enabled (based on criticality), context-dependent (adjusted per operational context), negotiable (hard vs. soft — hard = non-negotiable for safety/legal; soft = adjustable based on context).
- **Quality attributes (14):** Accuracy, efficiency, privacy, security, safety, fairness, compliance, generalizability, customizability, adaptability, traceability, portability, interoperability, interpretability.

---

### 13. Limitations and Unsolved Problems

- **Stated limitations:**
  - Definitions and categorisations may not capture all relevant aspects
  - Rapid evolution of FM-based agents may make findings outdated
  - Specific adaptations necessary for certain systems (healthcare, finance)
  - Operational validation of reference architecture beyond paper's scope
- **Alignment with my research gaps:**
  - **Comprehensive Level 2 taxonomy but no state conditioning:** The paper provides the definitive classification of guardrail actions and targets but does not address *when* different guardrail configurations should activate based on environmental state
  - **Context-dependent rules recognised but not formalised:** The concept of adjusting guardrails based on operational context is identified but not formalised as state-conditioned governance
  - **No environmental state classification:** Guardrails are configured per artifact and quality attribute, not per classified environmental safety state
  - **No Safety Dominance Property:** No formal guarantee linking guardrail configurations to classified safety states
  - **My architecture fills the gap:** by providing the state classification function S = f(E) and the governance pair (G(S), A_AI(S)) that determines *which* guardrail configuration applies *when* — the missing activation mechanism for the comprehensive guardrail taxonomy this paper provides

---

### 16. Relation to My Research and Positioning

- **Governance implementation:** Level 2 comprehensively taxonomised (13 action types × 14 targets). Level 1 partially addressed (block, fall back, isolate). No state conditioning.
- **Two-level governance pair:** The taxonomy provides the most comprehensive catalogue of Level 2 governance *options* (what can be done to AI output). My architecture provides the Level 1 + Level 2 *activation mechanism* (when to apply which options, conditioned on environmental state).
- **Safety property:** Not defined. No formal guarantee.
- **Gap my research addresses:** Shamsujjoha et al. answer "what governance actions exist?" comprehensively. My architecture answers "when should which governance configuration apply?" — by conditioning the governance pair (G(S), A_AI(S)) on classified environmental state S = f(E). The two contributions are complementary: their taxonomy catalogues the governance action space; my architecture provides the state-conditioned selection mechanism.

**Positioning paragraph:** Shamsujjoha et al. (2025) provides the **definitive taxonomy of runtime guardrails for AI agents** — the most comprehensive available classification of governance actions (13 types), targets (14 pipeline stages and artifacts), quality attributes (14), and rule types (4 including context-dependent). Published at IEEE ICSA, it represents the state of the art in cataloguing *what* runtime AI governance mechanisms exist. The Swiss Cheese Model reference architecture demonstrates that multi-layered guardrails across different dimensions (quality × pipeline × artifact) provide robust defence through redundancy. However, the taxonomy catalogues governance *options* without specifying a *selection mechanism* conditioned on environmental state. Guardrails are configured per artifact type and quality attribute, not dynamically activated based on classified environmental safety conditions. The context-dependent rule type — which adjusts guardrails based on operational context — is the closest concept to my state-conditioned governance but operates on data/deployment context rather than classified environmental safety state. My architecture fills this gap by providing: (a) the environmental state classification S = f(E) that determines which governance mode is active, and (b) the governance pair (G(S), A_AI(S)) that selects which guardrail configuration applies per classified state. The two contributions are complementary: Shamsujjoha et al. taxonomise the governance action space; my architecture provides the state-conditioned activation mechanism that selects from that space.

---

### 17. Overall Relevance Score

**⭐⭐⭐ Medium**

**Justification:** The paper addresses two core themes (safety-critical AI, AI governance) and partially addresses three more. It provides the most comprehensive available taxonomy of runtime AI governance mechanisms — directly relevant as the definitive catalogue of Level 2 governance options against which my state-conditioned governance is positioned. The Swiss Cheese Model multi-layered architecture demonstrates defence-in-depth principles applicable across domains. However, it operates in the FM/LLM agent domain (not safety-critical physical systems), provides no formal model or safety properties, and does not implement state-conditioned governance. Its value is as a complementary governance *options* catalogue rather than a governance *architecture* baseline. Elevated from ⭐⭐ to ⭐⭐⭐ because: (a) it provides the definitive Level 2 taxonomy against which my A_AI(S) is positioned, (b) its context-dependent rule type is the closest concept to state-conditioned governance in the guardrail literature, and (c) the complementary relationship (they catalogue options; I provide the selection mechanism) is a clean citation angle.

---

### Recommended Citation Uses

| Use | Section in dissertation | Specific point |
|---|---|---|
| Definitive Level 2 governance taxonomy | Literature review — AI governance mechanisms | 13 guardrail actions × 14 targets = most comprehensive available catalogue of what runtime AI governance can do |
| Context-dependent rules as precursor | Gap identification | Context-dependent guardrail rules adjust per operational context — closest existing concept to state-conditioned governance, but operates on data context not environmental safety state |
| Swiss Cheese multi-layered defence | Architecture design rationale | Defence-in-depth principle — multiple guardrail layers compensate for individual weaknesses. Applicable to my multi-layer governance (G(S) + A_AI(S)) |
| Guardrail actions vocabulary | Architecture comparison | Block, filter, flag, modify, validate, fall back, human intervention — vocabulary for describing what my A_AI(S) restricts |
| Complementary contribution framing | Research positioning | "They catalogue the governance action space; my architecture provides the state-conditioned selection mechanism" |
