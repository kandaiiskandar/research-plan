# Literature Extraction: Castagnone & Nitti (2026)
## "A Neuro-Symbolic Framework for Ensuring Deterministic Reliability in AI-Assisted Structural Engineering: The SYNAPSE Architecture"

---

## 1. Paper Identity

- **Title:** A Neuro-Symbolic Framework for Ensuring Deterministic Reliability in AI-Assisted Structural Engineering: The SYNAPSE Architecture
- **Authors:** Adriano Castagnone, Giuseppe Nitti
- **Year:** 2026
- **Venue:** Buildings, 16(3), 534 (MDPI)
- **Type:** System design paper with case study evaluation

---

## 2. Core Contribution

- **Problem:** LLMs are fundamentally unsuitable for direct application in structural engineering due to their probabilistic nature, hallucination risk, and non-deterministic outputs. Structural engineering requires deterministic reproducibility, regulatory compliance, legal traceability, and zero tolerance for computational errors. The equation "LLMs + Engineering = Risk" captures this paradox: the field needs AI's adaptive capabilities but cannot accept its probabilistic unreliability.

- **Proposed solution:** The **SYNAPSE architecture** (Symbolic Neural Architecture for Predictive Structural Engineering) — a neuro-symbolic AI (NSAI) hybrid that strictly separates neural and symbolic components. The neural component (LLM) handles natural language understanding, intent recognition, and result presentation. The symbolic component (deterministic calculation engine + intelligent query system) handles all safety-critical calculations, regulatory compliance verification, and formal reasoning. The **fundamental design principle: the neural component is never allowed to perform safety-critical calculations directly**.

- **Main contributions:** (1) Analysis of why pure LLMs are unsuitable for safety-critical structural engineering; (2) Theoretical framework for neuro-symbolic integration in this domain; (3) The SYNAPSE architecture with four-component pipeline; (4) Empirical validation via the 3Muri chatbot (94% accuracy, <2s response time, 200+ queries).

- **Novelty:** The architectural separation that delegates *all* safety-critical computation to deterministic symbolic engines while using the LLM only as an intelligent interface. The four-stage verification protocol for LLM-generated scripts before they reach the deterministic engine. The specific application of neuro-symbolic AI to structural engineering with regulatory compliance enforcement.

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | **Yes** | Core contribution. Neuro-symbolic architecture combining LLM (probabilistic) with deterministic calculation engines and rule-based compliance checking (symbolic). Explicit separation of neural and symbolic roles. |
| Safety-critical AI decision-making | **Yes** | Central focus. The entire architecture is motivated by safety-criticality of structural engineering. Extensive discussion of hallucination risks, legal liability, and the need for deterministic reliability. |
| AI governance / control mechanisms | **Yes** | The Intelligent Query System (IQS) governs what the LLM may do — it enriches prompts, constrains LLM behaviour, and the four-stage verification protocol gates whether LLM-generated scripts may execute. The LLM is architecturally prevented from performing safety-critical calculations. |
| Low-resource environments | **No** | Not addressed. System runs on cloud infrastructure (AWS), uses GPT-4, and targets professional structural engineering firms. |
| Decision architecture formalisation | **Partial** | The architecture is described as a four-component sequential pipeline with clear data flow, but no formal mathematical model (no state variables, gate functions, or action spaces). Architecture is described diagrammatically and procedurally, not formally. |
| Human role in decision-making | **Partial** | The engineer is the end user who submits queries and receives results. The system is positioned as decision support (intelligent assistant). However, the human role is not formally modelled — no override mechanism, no escalation protocol, no formal human-in-the-loop governance. |
| Socio-technical evaluation | **No** | Evaluation is purely technical (accuracy, response time) plus user satisfaction survey (4.7/5). No socio-technical analysis of human-AI interaction patterns, trust dynamics, or organisational factors. |
| Coastal fisheries / maritime domain | **No** | Structural engineering domain. |

**Yes count: 3 | Partial count: 2 → FULL EXTRACTION**

---

## 4. Decision Architecture Analysis

The SYNAPSE architecture structures decision-making as a **four-component sequential pipeline**:

**Component 1 — User Interface Layer:** Receives natural language queries, hand-drawn sketches, or mixed media from the structural engineer. Accepts informal, ambiguous inputs.

**Component 2 — Intelligent Query System (IQS) [Symbolic Core]:** Three-layer architecture:
- Layer 1 (Information Repository): Verified technical documentation, case examples, historical data, validated code snippets
- Layer 2 (Logic Framework): Domain ontology, verification protocols, compliance rules (Eurocodes, NTC)
- Layer 3 (Context Retrieval System): Interprets requests, retrieves relevant information, consults logic framework, assembles enriched context

The IQS enriches the user's query with regulatory requirements, calculation methods, and predefined templates before passing to the LLM.

**Component 3 — LLM Interface [Neural Interface]:** Receives enriched prompt from IQS. Role is strictly circumscribed to: interpreting user intent, preparing structured data for deterministic algorithms, generating scripts (e.g., Code Aster), and presenting results in natural language. **The LLM is never permitted to perform safety-critical calculations.**

**Component 4 — Deterministic Calculation Engine [Computational Core]:** Performs all actual structural analysis using Code Aster (open-source FEM solver). Two functions: solver (FEM analysis, frame analysis, section capacity) and post-processor (extracting critical values, compliance checking, report generation).

**Rule-based constraints before AI reasoning:** Yes — the IQS constrains the LLM by enriching prompts with regulatory requirements and prescribed calculation methods *before* the LLM processes the query. Additionally, a **four-stage verification protocol** gates LLM-generated scripts before execution:
1. Syntactic validation (correct syntax, command sequencing)
2. Semantic validation (engineering logic consistency, material property ranges, boundary condition checks, load combination validation)
3. Dimensional consistency (unit compatibility, mesh density)
4. Regulatory compliance (cross-reference against building code requirements)

Only scripts passing all four stages may execute on the deterministic engine.

**Failure modes / fallback:**
- Pre-execution errors: structured error report → LLM regenerates script (max 3 attempts) → escalates to user
- Convergence failures: adaptive strategy (reduce load stepping → switch solver algorithm → report failure with diagnostics)
- Runtime errors: immediate termination with full state logging
- **Fundamental principle: no unverified or partially completed results are ever presented as valid engineering outputs**

**Boundary between deterministic and AI:** Architecturally enforced. The LLM operates in a constrained role (intent interpretation, result presentation). All calculations are performed by the deterministic engine. The four-stage verification protocol is the formal boundary between neural processing and deterministic execution.

---

## 5. Formal Model and Mathematical Representation

**Formal model:** Not present in a mathematical sense. The paper describes the architecture procedurally and diagrammatically (Figure 5) rather than formally. There are no state variables, gate functions, action spaces, or formal safety properties defined mathematically.

**Comparison to my pipeline E → S = f(E) → (G(S), A_AI(S)) → AI(E):**

| Component | My Architecture | SYNAPSE |
|---|---|---|
| Environmental state vector E | {w, r, m, o, v, t} — environmental inputs | User query + project context (not formalised as a vector) |
| Safety state classification S = f(E) | Tripartite: SAFE/CAUTION/UNSAFE | Not present — no environmental state classification |
| Gate function G(S) | State-conditioned binary: G(S)=0 or 1 | Not present as state-conditioned gate. However, the four-stage verification protocol acts as a gate on LLM-generated scripts (pass/fail). This is *task-conditioned* gating, not *environmental-state-conditioned* gating. |
| Admissible action space A_AI(S) | State-conditioned, graduated | Not present as state-conditioned. The LLM's action space is *architecturally fixed*: it may interpret and present, never calculate. This is a static constraint, not a dynamic state-conditioned restriction. |
| Safety Dominance Property | AI(E) ⊆ A_AI(S) | No formal equivalent. However, the architectural principle that "the neural component is never allowed to perform safety-critical calculations directly" is a *design-time* safety property, not a *runtime state-conditioned* property. |

**State-dependent recommendation restriction:** Not present. The LLM's role is *always* restricted to interpretation and presentation — this restriction does not vary by state. There is no mode where the LLM gains or loses capabilities based on classified environmental conditions. The restriction is static/architectural, not dynamic/state-conditioned.

**Formalisation purpose:** The architecture is described for implementation guidance, not for formal proof or property verification. The paper acknowledges the absence of ablation studies and component-level analysis as a limitation.

---

## 6. Safety State Classification

**Discrete risk/safety levels:** Not present. The system does not classify operational or environmental conditions into discrete safety levels. The four-stage verification protocol classifies *LLM-generated scripts* as pass/fail (binary), but this is a code quality check, not an environmental safety state classification.

**Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:** No equivalent. The system's safety mechanism is architectural separation (neural vs symbolic) rather than state classification. The system does not assess "how safe is the current situation" and adjust AI behaviour accordingly — it permanently restricts the LLM to non-computational roles regardless of context.

**Critical gap:** Because the safety mechanism is architectural (static role assignment) rather than state-conditioned (dynamic role adjustment), there is no CAUTION mode. The LLM is either operating in its permanently restricted role or failing the verification protocol. There is no intermediate state where the LLM operates with *graduated* restrictions based on assessed safety conditions.

---

## 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (equivalent to G(S)) | **Partial** | The LLM always operates (for interpretation/presentation). The four-stage verification protocol gates whether LLM-generated scripts reach the deterministic engine — this is a form of participation governance for the *computational* path, but it is task-quality-conditioned, not environmental-state-conditioned. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (equivalent to A_AI(S)) | **Partial (static)** | The LLM's scope is architecturally restricted: it may interpret intent and present results but never perform calculations. This is a *static* scope restriction — it does not vary by state. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | **No** | No environmental state classification. Governance is architectural/static, not state-conditioned/dynamic. |

**Binary vs graduated:** The system implements a **static architectural separation** rather than either binary or graduated dynamic governance. The LLM's role is permanently constrained by design. This is stronger than binary Level 1 governance (the LLM is never fully blocked — it always operates in its restricted role) but weaker than graduated governance (the restriction never varies by state).

**Support for two-level governance pair:** The paper's architecture is conceptually *adjacent* to my governance model but operates on a different axis. SYNAPSE separates *computational roles* (neural = interpret, symbolic = calculate) permanently. My architecture separates *AI participation modes* (SAFE = full, CAUTION = restricted, UNSAFE = blocked) dynamically by state. The SYNAPSE approach answers "what *type of processing* may AI perform?" with a static architectural answer. My approach answers "what *types of recommendations* may AI generate?" with a dynamic state-conditioned answer.

---

## 8. Human Role in Decision-Making

**Decision authority:** The engineer is the end user who submits queries and receives results. The system is positioned as an intelligent assistant — decision support, not decision automation. The engineer retains full professional responsibility for structural design decisions.

**Override/escalation:** Pre-execution errors escalate to the user after three failed LLM script regeneration attempts. Convergence failures report diagnostics to the user. However, there is no formal human override mechanism for AI recommendations, no escalation protocol based on safety conditions, and no structured rationale capture.

**Human factors:** The paper discusses legal responsibility, professional liability, and the need for traceable/defensible calculations. The system supports these through deterministic reproducibility and compliance documentation. However, human cognitive factors (biases, workload, expertise variation) are not modelled.

---

## 9. System Constraints and Environment

**Resource constraints:** Not addressed. The system targets professional structural engineering firms with cloud infrastructure (AWS), GPT-4 API access, and Code Aster computational resources. No consideration of limited compute, connectivity, or offline operation.

**Real-world deployment:** The 3Muri chatbot has been deployed in production use. Evaluation based on 200+ queries rated by expert structural engineers. Real users interact with the system for masonry structural analysis support.

**Edge cases:** The error handling logic addresses three failure categories (pre-execution, convergence, runtime) with graduated responses. The system's design principle of never presenting unverified results is a strong edge-case safety mechanism.

---

## 10. Hybrid AI Taxonomy

**Hybrid AI type:** **Neuro-symbolic** — the paper's primary architectural contribution.
- Neural component: LLM (GPT-4/Gemini) for NLU, intent recognition, script generation, result presentation
- Symbolic component: IQS (domain ontology, compliance rules, verification protocols) + deterministic calculation engine (Code Aster FEM solver)

**Safety enforcement location:** **Before AI output reaches the user** — the four-stage verification protocol sits between LLM output and deterministic engine execution. Additionally, the architectural separation prevents the LLM from performing calculations at any point.

**Two-level governance support:** The architecture implements a *static* form of output-scope restriction (LLM may never calculate) but not a *dynamic, state-conditioned* two-level governance model. The restriction does not vary by classified environmental state.

**Comparison to my architecture:** Both architectures share the fundamental principle of deterministic-first safety enforcement — safety-critical operations are handled by deterministic/rule-based components, not probabilistic AI. The key difference is that SYNAPSE's separation is *permanent and architectural* (LLM never calculates, regardless of context), while my architecture's separation is *dynamic and state-conditioned* (AI scope varies by classified environmental safety state). SYNAPSE does not need graduated governance because the LLM's role is always the same. My architecture needs graduated governance because the AI's advisory role must adapt to varying environmental conditions.

---

## 11. Baseline Comparison and Evaluation

**Baselines:** Table 1 compares SYNAPSE against pure LLMs, hallucination mitigation, traditional ML/DL, XAI methods, verified AI/formal methods, and general neuro-symbolic AI across determinism, explainability, and safety-critical reliability. SYNAPSE rates "Yes/High/High" — the only approach with full determinism.

**Performance metrics:**
- Response accuracy: 94% (expert-evaluated)
- Average response time: 1.8s
- User satisfaction: 4.7/5

**Failure analysis (Section 6.1):** Of the 6% failures: ~70% were non-safety-critical (licensing, installation, unimplemented features). ~30% of failures (~2% of total) involved technically correct but incomplete responses to complex questions. Crucially, "the NSAI architecture's symbolic verification layer prevented any incorrect structural calculations from being presented to users."

**CAUTION zone testing:** Not applicable — no graduated governance model to test.

**Safety Dominance Property verification:** Not formally verified. The architectural separation is a design-time property, not a runtime-verified formal property.

**Ablation studies:** Explicitly acknowledged as absent (Section 6.2) — identified as a priority for future work.

---

## 12. Key Concepts and Definitions

- **SYNAPSE (Symbolic Neural Architecture for Predictive Structural Engineering):** A four-component sequential pipeline architecture that separates neural (LLM) and symbolic (IQS + deterministic engine) roles to achieve both natural interaction and deterministic reliability.
- **Neuro-Symbolic AI (NSAI):** Hybrid approach integrating neural network pattern recognition and adaptive learning with symbolic logical reasoning, rule enforcement, and knowledge representation. Described as the "third wave" of AI.
- **Intelligent Query System (IQS):** The symbolic core of SYNAPSE, comprising three layers (information repository, logic framework, context retrieval) that enrich user queries with regulatory context before passing to the LLM.
- **Four-stage verification protocol:** Syntactic → Semantic → Dimensional → Regulatory compliance validation of LLM-generated scripts before execution on the deterministic engine.
- **Hallucination problem:** LLMs generating plausible but incorrect outputs — identified as the fundamental obstacle to LLM adoption in structural engineering.
- **Deterministic reliability:** The requirement that identical inputs always produce identical, verifiable, legally defensible outputs — the core safety requirement that probabilistic AI cannot satisfy.

---

## 13. Limitations and Unsolved Problems

**Stated limitations:**
1. Knowledge engineering is extremely labour-intensive (~6 person-months for initial NTC masonry provisions alone).
2. Neural-symbolic coherence challenges: LLM sometimes maps intent to incorrect symbolic categories (e.g., "wall resistance" → wrong capacity type).
3. Version synchronization: base LLM updates (GPT-3.5 → GPT-4) required recalibration of prompt templates and confidence thresholds.
4. Limited to Italian/European regulatory frameworks — extending to other jurisdictions requires substantial effort per code family.
5. No ablation studies isolating individual component contributions.
6. The 94% accuracy leaves a 6% failure rate that, while mostly non-safety-critical, requires continued improvement.

**Gaps aligning with my research problem:**
- **No environmental safety state classification:** The system does not classify operational conditions into safety states. Its safety mechanism is permanent architectural separation, not dynamic state-conditioned governance.
- **No dynamic AI participation governance:** The LLM's role is permanently fixed. There is no mechanism to dynamically expand or contract AI capabilities based on assessed environmental conditions — no equivalent to G(S) varying by S.
- **No state-conditioned output scope restriction:** The LLM's output scope (interpret + present) is static. There is no CAUTION mode where AI participation continues but with restricted recommendation types.
- **No formal Safety Dominance Property:** The architectural separation is a design principle, not a formally defined and runtime-verified property.
- **Static vs dynamic governance:** SYNAPSE's governance is appropriate for its use case (LLM always assists with structural analysis software) but would not support contexts where AI advisory scope should vary by environmental conditions (e.g., fisheries where weather conditions change the appropriate level of AI engagement).

---

## 14. Methodology Notes

- **Research method:** Architecture design with case study evaluation. The SYNAPSE architecture is proposed theoretically (Sections 3–4), then implemented as the 3Muri chatbot (Section 5), and evaluated on 200+ queries rated by expert structural engineers.
- **Alignment with DSR:** Partially aligns — follows a design → implement → evaluate cycle. However, no formal DSR methodology is cited, and there is no formal model verification step.
- **Methodological utility for my research:** The paper's clear articulation of *why* probabilistic AI is unsuitable for safety-critical calculations, and its principled architectural response (deterministic components handle all safety-critical work, neural components handle interaction), directly supports the motivation for my architecture. The four-stage verification protocol is an interesting governance mechanism — a task-quality gate between neural and symbolic processing — that could inform my thinking about verification at the boundary between probabilistic AI and deterministic safety rules, though it operates on a different axis (script quality vs environmental safety state).

---

## 15. Quotable / Citable Points

1. **LLM inadequacy for safety-critical engineering (Section 1):** The paper articulates the paradox that structural engineering needs AI's adaptive capabilities but cannot accept its probabilistic unreliability, summarised as "LLMs + Engineering = Risk."

2. **Architectural separation principle (Section 4):** The architecture is designed around a fundamental principle that the neural component is never allowed to perform safety-critical calculations directly — instead, the neural role is limited to interpreting intent and presenting results, while all calculations are performed by verified deterministic algorithms.

3. **Verification prevents hallucination propagation (Section 6.1):** The symbolic verification layer prevented any incorrect structural calculations from being presented to users; when the system could not provide complete answers with high confidence, it acknowledged uncertainty rather than generating potentially dangerous misinformation.

4. **Neuro-symbolic as "third wave" (Section 3, citing Garcez & Lamb):** NSAI integrates pattern recognition and adaptive learning strengths of neural networks with logical reasoning, rule enforcement, and knowledge representation of symbolic AI, enabling systems that learn from data while adhering to explicit logical constraints and domain rules.

5. **Determinism requirement (Section 1):** Structural engineering requires that every calculation be verifiable, traceable, and defensible in potential litigation; the probabilistic nature of LLM outputs, where the same query might produce different results, fundamentally conflicts with this requirement for reproducibility and accountability.

---

## 16. Relation to My Research and Positioning

**Level 1 governance:** Partially implemented. The four-stage verification protocol gates LLM-generated scripts (pass/fail), and the architectural separation permanently restricts the LLM from performing calculations. However, this is not conditioned on environmental safety state — it is static.

**Level 2 governance:** Partially implemented in static form. The LLM's output scope is permanently restricted to interpretation and presentation. This is a static scope restriction, not a dynamic state-conditioned restriction.

**State-conditioned governance pair:** Not present. No (G(S), A_AI(S)) equivalent. Governance is architectural, not state-conditioned.

**Safety Dominance Property:** Not formally defined. The architectural separation serves as a design-time safety property but is not formalised as a runtime-verified containment guarantee.

**Gap my research addresses:** SYNAPSE demonstrates that architectural separation between neural and symbolic components can achieve deterministic reliability in safety-critical AI systems. However, its governance is *static* — the LLM's role never varies by context. My architecture addresses contexts where AI advisory scope must *dynamically adapt* to varying environmental safety conditions. In coastal fisheries, unlike structural engineering software assistance, the environmental state changes (weather deteriorates, conditions shift) and the AI's advisory scope must contract accordingly. SYNAPSE's static governance cannot handle this — it has no mechanism to say "conditions have degraded, so restrict AI to go/no-go advice only." My two-level governance pair (G(S), A_AI(S)) provides this dynamic capability.

**Positioning paragraph:** This paper serves as a **strong thematic parallel and partial architectural antecedent** for my research. SYNAPSE shares my architecture's fundamental principle: safety-critical operations must be handled by deterministic/rule-based components, not probabilistic AI. The four-stage verification protocol is a concrete implementation of the principle that AI outputs must be constrained within verified bounds before reaching the user — conceptually adjacent to my Safety Dominance Property. However, SYNAPSE implements *static architectural governance* (the LLM's role is permanently fixed) while my architecture implements *dynamic state-conditioned governance* (AI scope varies by classified environmental safety state). This difference reflects the different operational contexts: in structural engineering software assistance, the LLM always does the same job (interpret queries, present results). In coastal fisheries decision support, the environment changes, and the AI's advisory scope must change with it. SYNAPSE validates the neuro-symbolic approach for safety-critical domains but does not address the graduated, state-conditioned governance that my architecture contributes. The paper is citable for its principled articulation of why probabilistic AI requires deterministic governance in safety-critical contexts, and its NSAI architecture provides a useful comparator showing how hybrid AI can achieve safety without state-conditioned graduation.

---

## 17. Overall Relevance Score

### ⭐⭐⭐⭐ High

**Justification:** This paper directly addresses three major research themes (hybrid AI, safety-critical AI, AI governance) with a concrete architecture that shares my fundamental design principle: deterministic components must govern probabilistic AI in safety-critical contexts. The SYNAPSE architecture serves as a strong comparator showing how neuro-symbolic hybrid AI can achieve safety through *static* architectural separation — making the gap my architecture fills (dynamic, state-conditioned governance) clearly visible. The paper's articulation of why LLMs are unsuitable for direct safety-critical application, and its principled response through neuro-symbolic integration, directly supports my dissertation's motivation. It does not address low-resource environments, environmental safety state classification, or graduated governance — the specific gaps my architecture fills. The rating of ⭐⭐⭐⭐ rather than ⭐⭐⭐⭐⭐ reflects that it implements static rather than state-conditioned governance and lacks formal model definition, but its thematic alignment and architectural parallels make it highly relevant.
