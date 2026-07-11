# Article Summary: XHAILe — Explainable Hybrid AI for Computational Law and Accurate Legal Chatbots

---

## 1. Paper Identity

- **Title:** XHAILe: Explainable Hybrid AI for Computational Law and Accurate Legal Chatbots
- **Authors:** Thomas Hildebrandt, Hugo-Andrés López-Acosta, Konstantinos Varvoutas, Henrik Palmer Olsen, Marieke Anne Heyl, Manex Aguirrezabal Zabaleta, Bolette Pedersen, Daniel Hershcovich, Ilias Chalkidis, Ali Mohammed Ali Al-Laith, Aryan Raina, Thomas Zuckmantel, Morten Marquard, Søren Debois, Håkon Normann, Louise Storgaard, Gustav Thiesen, Joachim Foli, Jacob Eiby (19 authors total)
- **Year:** 2026 (In press/accepted)
- **Venue:** Proceedings of the 38th International Conference on Advanced Information Systems Engineering (CAiSE'26), CEUR-WS
- **DOI:** Not yet assigned (preprint version)
- **Type:** Project roadmap/architecture paper describing a 3.5-year research project (April 2025–October 2028) funded by Innovation Fund Denmark
- **Project Website:** XHAILer Grand Solutions project (Denmark)
- **Keywords:** Hybrid AI, Computational Law, Legal Chatbots, DCR Graphs, NLP, LLM, eGovernment
- **Core Technology:** Dynamic Condition Response (DCR) Graphs + Large Language Models (LLMs)
- **Key Reference:** Belle, V. (2025). On the relevance of logic for artificial intelligence, and the promise of neurosymbolic learning. *Neurosymbolic Artificial Intelligence*, 1, 29498732251339951. DOI: 10.1177/29498732251339951

---

## 2. Problem Statement

### 2.1. Domain Problem

| Aspect | Description |
|--------|-------------|
| **Context** | Danish public sector and legal compliance systems |
| **Scale** | Social services legislation: 2,213 clauses, 908 administrative regulations, 32 main laws, amended 5×/year (2007–2018) |
| **Economic Impact** | Danish companies spent 40 million hours/year (2023) on documentation/reporting → DKK 23.5 billion/year; 3 new EU legal requirements/week (2017–2022) |
| **Legacy Process** | Laws manually translated to PDF forms → manually coded as self-service solutions (two translations, both introducing interpretation) |
| **Failed Attempt** | "Workflow bank" initiative (2007–2010) abandoned in 2013; process descriptions could not be maintained up-to-date with law |
| **Broader Context** | Analysis of 11 EU member states (2019) showed average spending > EUR 1 billion/year per state on compliance |

### 2.2. Technical Problem

| Issue | Explanation |
|-------|-------------|
| **LLM Hallucination** | End-to-end LLM solutions cannot be trusted for high-stakes legal decisions |
| **Interpretation Complexity** | LLMs cannot reliably interpret legal texts with ambiguity and context |
| **Accountability Gap** | Opaque AI outputs cannot provide auditable legal justification |
| **Maintenance Burden** | Legal rules change frequently; ML models require retraining |
| **No Formal Guarantees** | Pure statistical systems provide probabilistic outputs, not deterministic guarantees |
| **Trustworthiness** | Critical concerns about entire conversational framework: prompt interpretation, information retrieval, task execution, response dissemination |

### 2.3. Key Quote

> "While in many use cases, e.g., Q&A of common knowledge, code development assistance, end-to-end LLM-based solutions can be quite effective, if the user is aware of and ready to cope with the potential challenges involved, the situation is quite different in high-stakes scenarios, such as those commonly encountered in processes that involve the interpretation and execution of law." (Page 3)

---

## 3. Proposed Solution: Hybrid AI Architecture

### 3.1. Core Architectural Principle

The project follows the **Neuro-Symbolic AI** paradigm, specifically **Approach 2**:

> "The sub-symbolic models are used to feed, e.g., as translators of inputs from users or knowledge bases, the symbolic models, which carry out the inference of the answer." (Page 5)

**Architectural Rationale:** 

> "The grounding in formal symbolic reasoning ensures that the final output is not a hallucination, but a natural language description of a valid logical proof derived by the symbolic engine." (Page 5)

### 3.2. Technology Stack

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Symbolic Foundation** | DCR Graphs (Dynamic Condition Response) | Executable, declarative, temporal logic process modelling; defines what is forbidden/required |
| **Symbolic Execution** | DCR Execution Engine | Validates and executes DCR graphs; provides formal guarantees |
| **Interpretation Layer** | LLMs (bounded interface) | Converts natural language user input to structured queries; renders explanations |
| **Translation Tool** | NLP + Highlighter Tool | Assists legal experts in mapping legal text to DCR graphs |
| **Integration** | Open API | Accessible rule engine for external systems |

### 3.3. DCR Graphs as Computational Law

**What Are DCR Graphs?**

> "Unlike imperative process modelling notations (like BPMN) that rigidly describe the sequencing of possible steps as flow charts, DCR graphs model the 'rules of the game'—defining only what is forbidden or required, leaving everything else allowed. This aligns naturally with the nature of law, which typically prescribes obligations and benefits, and proscribes conduct, rather than scripting it." (Page 5)

**DCR Graph Capabilities:**

| Feature | Description |
|---------|-------------|
| **Temporal Logic** | Models processes with time constraints |
| **Data & Decision Modelling** | Data-dependent rules and embedded computations |
| **DMN Integration** | Integrates Decision Model and Notation standard |
| **Simulation** | Tools for validating process models |
| **Execution** | Cloud-based process-engine-as-a-service |
| **Deployment** | Already used in Danish public-sector case management |

**Figure 2 Description:**

> "Rules and activities in law texts can be highlighted by domain-experts and thereby translated to a DCR graph in the DCR no-code design tool (dcsolutions.net), that can be simulated for validation and executed in a case management processes and digital self-service forms using the DCR execution engine service." (Page 6)

### 3.4. The Conversational Hybrid AI (CHAI) Architecture

**Figure 3 Architecture:**

| Layer | Component | Responsibility |
|-------|-----------|----------------|
| **Layer 1** | User (Citizen/Caseworker) | Initiates interaction; provides natural language input |
| **↓** | | |
| **Layer 2** | LLM as Bounded Interface | Intent understanding; natural language adaptation; input normalization; DOES NOT determine outcomes |
| **↓** | | |
| **Layer 3** | DCR Rule Engine Controller | Executes legal decision logic; guarantees sound execution; provides provenance and auditability; ALL final decisions remain here |
| **↓** | | |
| **Layer 4** | Fact-Rule Disaggregated Explanation | States what user supplied; what controller verified; which conditions are satisfied/unmet; which next steps follow |

**Key Design Principle (Page 7-8):**

> "This separation maintains public-authority accountability: the controller guarantees sound execution, provenance, and auditability; the LLM improves accessibility (intent understanding and language adaptation) but does not determine outcomes."

**Dialogue Loop Mechanism:**

> "A dialogue loop can be realized in which the LLM converts free-form utterances into schema-constrained structures aligned with the controller's inputs, queries the controller to test preconditions and obligations, and renders the controller's trace and explanation into citizen-facing feedback." (Page 7-8)

### 3.5. Three-Phase Development Roadmap

| Phase | Focus | Key Activities |
|-------|-------|----------------|
| **Near Term** | Formalization | Dialogue tool grammar; controller interface extensions; confidence-aware verification; fact-rule faithful explanations |
| **Medium Term** | Process Routing | Intent router with hard guardrails; language/persona policies; escalation pathways for caseworkers |
| **Long Term** | Full Integration | All features operational; TRL/SRL 7 demonstrated on use cases |

---

## 4. Technical Research Challenges Addressed

### 4.1. Scalable DCR Graphs for Law

**Problem:** DCR graphs become difficult to manage beyond 20–30 activities.

**Proposed Solutions:**

| Approach | Description | Reference |
|----------|-------------|-----------|
| **Networks of DCR Graphs** | Separating graphs into sub-parts; linking activities between sub-parts | López et al., 2020 |
| **Object-Oriented Modelling** | Inheritance between classes of DCR graphs; encapsulation principles | Snyder, 1986; Christfort et al., 2024 |
| **Akoma Ntoso (AKN4EU)** | EU standard for legal document exchange; explore structure of legal documents | AKN4EU specification |
| **Grouping Techniques** | Group activities with common rules to reduce complexity | Cosma et al., 2024 |

**Key Quote:**

> "Initial work on object-centric DCR graphs was initiated in... We propose to extend this line of work by investigating suitable definitions of inheritance between classes of DCR graphs that still respect the principles of encapsulation and investigate their usefulness in the modelling of law." (Page 6)

### 4.2. Translating Law to DCR Graphs

**Problem:** Current NLP techniques:
- Ignore data and timing constraints
- Only capture the most basic elements of DCR models
- Trained on business process descriptions, not legal texts
- Cannot identify data-dependent rules
- Cannot handle ambiguity in input texts

**Proposed Solutions:**

| Approach | Description | Reference |
|----------|-------------|-----------|
| **Data Extraction from Requirements** | Classical NLP techniques for object class/data models | Harmain & Gaizauskas, 2003; Yue et al., 2011 |
| **LLM-Based Extraction** | Modern LLM approaches for automated domain modelling | Chen et al., 2023; De Bari et al., 2024 |
| **Semantic Parsing** | Extract events, entities, and relations from legal text | Oepen et al., 2019, 2020 |
| **Meaning Representation** | Treat legal process extraction as a semantic parsing task | Schrack et al., 2022; Vijay & Hershcovich, 2024 |
| **Knowledge Graphs** | Build from natural language (for legal context) | Ji et al., 2010; Li et al., 2024 |

**Key Challenge:**

> "The translations need to deal systematically with the presence of ambiguities in the input texts." (Page 5, citing López et al., 2025)

**Application to Example:**

> "Assistance shall only be provided where the cost exceeds DKK 500 which is based on a data value representing the cost of the consumer durables." (Page 6, from §113(2))

### 4.3. Accurate Conversational Legal Chatbot

**Problem:** Existing web forms are outdated; need natural language interaction with formal guarantees.

**Proposed Solution:**

> "We propose a flexible, controllable, and legally compliant Conversational Hybrid AI (CHAI) assistant that treats large (or if sufficient, small) language models strictly as a bounded interface to a rule-based controller executing legal decision and dynamic process logic encoded in DCR graphs." (Page 7)

**Key Features:**

| Feature | Description |
|---------|-------------|
| **Schema-Constrained Calls** | LLM outputs validated against controller's input schema |
| **Uncertainty Fields** | Explicit flagging of uncertain interpretations |
| **Confidence-Aware Verification** | Only flagged cases get confirmations/paraphrase-backs |
| **Hard Guardrails** | Prevent calls outside activated processes |
| **Trace-Linked Escalation** | Summaries for caseworkers with full provenance |
| **Fact-Rule Disaggregation** | Separates user input, controller verification, satisfied/unmet conditions, next steps |
| **Presentation Constraints** | Language and persona policies never alter execution semantics |

**Explanation Format:**

> "Explanations are fact-rule disaggregated: the interface states what the user supplied, what the controller verified, which conditions are satisfied or unmet, and which next steps follow from the model." (Page 8)

### 4.4. Legal Implications

**Two Distinct Use Cases:**

| Use Case | Purpose | Key Constraint |
|----------|---------|----------------|
| **Citizen-Facing** | General information about how legal rules apply | Cannot provide suggestions for decisions; would create unfounded expectations |
| **Caseworker-Facing** | Assist in making binding decisions | Suggests decisions at each step; enables forward/backward movement between sub-decisions |

**Critical Insight:**

> "By decomposing the legal rule into individual decision steps with the DCR tool, it becomes possible to use different solutions to provide suggestions. Depending on the kind of sub-decision, rule-based, expert-based or Rag-based solutions could be used to provide suggestions to the case worker." (Page 8)

**Holistic Decision-Making:**

> "The DCR format will be specifically helpful here, as it allows the case-worker to move both forward and backwards between sub-decisions—a necessary mechanism for legal decision making that involve interpretation or discretion, since these are made on the basis of a holistic analysis of all elements in the case as a whole." (Page 9)

**Legal Framework Requirements:**

> "Building a graph to support and partially automate steps for a specific provision in law... need to take into account the entire legal framework relevant to ensure rightful administration. This entails... the provisions in the Danish Public Administration Act... relevant case law... and instructions internal to the administration." (Page 8)

---

## 5. Project Objectives

| # | Objective | Description |
|---|-----------|-------------|
| 1 | **Open-Source Rule Engine** | Prototype of rule engine for computational law format, consistent with international standards (LegalRuleML) and DCR Solutions platform, accessible via open API |
| 2 | **Automated Translation** | Algorithm to automatically translate majority of computational rules; GUI for legal experts to complete translation in less than 1 hour |
| 3 | **Hybrid-AI Chatbot** | Conversational natural language interaction with e-government solutions; applies rule engine for accurate answers attributed to relevant law |
| 4 | **Legal Practice Guidelines** | Trustworthy benchmarks for computational law and conversational interfaces for e-government processes |
| 5 | **Demonstration** | Prototypes at SRL and TRL 7 on use cases with central/local government; covers Danish, Norwegian, and EU regulations |

---

## 6. Methodology: Reflective System Development

**Approach:** Reflective System Development (action research method)

**Three Main Research Activities:**

| Activity | Description |
|----------|-------------|
| **1. Understanding through Interpretation** | Researchers engage with practitioners to understand challenges |
| **2. Supporting through Design** | Develop solutions iteratively |
| **3. Improving through Intervention** | Test and refine with real users |

**Project Structure:**
- 4 cycles of 6 months
- TRL and SRL from 2 → 7 (tested in operational environment with relevant stakeholders)
- Interdisciplinary team: legal scholars, computer scientists (LLMs, NLP, symbolic logic, case/BPM management)
- Partners: Local and central governmental organizations

**Methodology Rationale:**

> "Reflective System Development is an action research method where researchers are actively engaged with practitioners when investigating opportunities and addressing challenges equally relevant for both research and practice." (Page 9)

**Research Cycle:**

> "Reflective System Development has a distinct cyclic iterative nature formed by three main research activities: 1) understanding through interpretation, 2) supporting through design, and 3) improving through intervention." (Page 9)

---

## 7. Key Contributions to Your Research

### 7.1. Direct Relevance Matrix

| Your Research Element | XHAILe Parallel | Relevance Level |
|-----------------------|-----------------|-----------------|
| Symbolic rule engine for final decisions | DCR Graph rule engine executes all decisions | ★★★★★ |
| Formal guarantees via symbolic reasoning | "Grounding in formal symbolic reasoning ensures final output is not a hallucination" | ★★★★★ |
| Separation of interface and reasoning | LLM as bounded interface; controller guarantees execution | ★★★★★ |
| Neuro-symbolic AI framing | Explicitly positioned in neuro-symbolic paradigm | ★★★★★ |
| State-conditioned rule sets | DCR graphs define what is allowed/forbidden per context | ★★★★☆ |
| Safety/Governance layer | Hard guardrails prevent actions outside activated processes | ★★★★☆ |
| Human-in-the-loop | Final authority remains with decision-maker | ★★★★☆ |
| Explainability | Fact-rule disaggregated explanations | ★★★★☆ |
| Low-resource deployment | Not primary focus (legal, not fisheries) | ★★★☆☆ |
| Offline capability | Not primary focus | ★★☆☆☆ |

### 7.2. Citations You Should Add

**To strengthen your Neuro-Symbolic AI framing:**

> Hildebrandt, T., et al. (2026). XHAILe: Explainable Hybrid AI for Computational Law and Accurate Legal Chatbots. *Proceedings of CAiSE'26*. CEUR-WS.

**To support the "bounded LLM interface" concept:**

> "The grounding in formal symbolic reasoning ensures that the final output is not a hallucination, but a natural language description of a valid logical proof derived by the symbolic engine." (Hildebrandt et al., 2026, p. 5)

**To support the "governance separation" principle:**

> "This separation maintains public-authority accountability: the controller guarantees sound execution, provenance, and auditability; the LLM improves accessibility (intent understanding and language adaptation) but does not determine outcomes." (Hildebrandt et al., 2026, p. 7-8)

### 7.3. What to Cite from This Paper in Each Section

| Your Proposal Section | What to Cite from XHAILe |
|-----------------------|---------------------------|
| **Introduction** | Problem of complexity in high-stakes domains; failed attempts at manual translation; economic impact of regulatory burden |
| **Literature Review** | Neuro-symbolic AI as a recognized paradigm; Belle (2025) citation validation; DCR Graphs as an alternative formalism |
| **Conceptual Framework** | "LLM as bounded interface" → parallels your governance layer; separation of interface from reasoning |
| **Formal Specification** | DCR graphs as formal declarative language; "rules of the game" vs. imperative scripting |
| **Expected Results** | XHAILe as precedent showing formal symbolic engines are deployable in practice; TRL/SRL 7 validation |
| **Methodology** | Reflective System Development validates your DSR + contextual user validation approach |
| **Future Work** | DCR Graphs as an alternative implementation of your reasoning layer; integration with LLM interfaces |

---

## 8. Key Quotes for Your Proposal

### 8.1. On Why Symbolic Reasoning Matters

> "The grounding in formal symbolic reasoning ensures that the final output is not a hallucination, but a natural language description of a valid logical proof derived by the symbolic engine." (Page 5)

### 8.2. On the LLM/Interface vs. Rule Engine Separation

> "This separation maintains public-authority accountability: the controller guarantees sound execution, provenance, and auditability; the LLM improves accessibility (intent understanding and language adaptation) but does not determine outcomes." (Page 7-8)

### 8.3. On the "Rules of the Game" Approach

> "Unlike imperative process modelling notations (like BPMN) that rigidly describe the sequencing of possible steps as flow charts, DCR graphs model the 'rules of the game'—defining only what is forbidden or required, leaving everything else allowed. This aligns naturally with the nature of law, which typically prescribes obligations and benefits, and proscribes conduct, rather than scripting it." (Page 5)

### 8.4. On Holistic Decision-Making (Relevant to Your CAUTION Mode)

> "The DCR format will be specifically helpful here, as it allows the case-worker to move both forward and backwards between sub-decisions—a necessary mechanism for legal decision making that involve interpretation or discretion, since these are made on the basis of a holistic analysis of all elements in the case as a whole." (Page 9)

### 8.5. On the Need for Formal Guarantees in High-Stakes Domains

> "While in many use cases... end-to-end LLM-based solutions can be quite effective... the situation is quite different in high-stakes scenarios, such as those commonly encountered in processes that involve the interpretation and execution of law." (Page 3)

### 8.6. On Decomposing Complex Decisions

> "By decomposing the legal rule into individual decision steps with the DCR tool, it becomes possible to use different solutions to provide suggestions. Depending on the kind of sub-decision, rule-based, expert-based or Rag-based solutions could be used to provide suggestions to the case worker." (Page 8)

---

## 9. Relationship to the Neuro-Symbolic AI Literature

### 9.1. Citations Used in XHAILe

| Citation | Relevance |
|----------|-----------|
| Belle, V. (2025) — "On the relevance of logic for artificial intelligence, and the promise of neurosymbolic learning" | Directly supports your framing of symbolic reasoning as contemporary AI |
| d. Garcez & Lamb (2023) — "Neurosymbolic AI: The 3rd wave" | Establishes neuro-symbolic AI as an active research paradigm |
| Hildebrandt et al. (2011) — DCR Graphs foundational paper | DCR formalism papers |
| Arent Eiriksson & Nordland (2020) — Danish legal complexity analysis | Contextual problem evidence |
| European Commission (2020) — Compliance costs study | Broader EU context |

### 9.2. How to Position Your Research Relative to XHAILe

**Similarities:**

| Dimension | XHAILe | Your Research |
|-----------|--------|---------------|
| Paradigm | Neuro-symbolic AI | Neuro-symbolic AI (classical AI + ML extension) |
| Symbolic Engine | DCR Graphs | Rule-based inference engine |
| Formal Guarantees | "Not a hallucination" | Safety Dominance Property |
| Domain | Legal compliance | Fisheries safety |
| Interface | LLM chatbot | Human decision-maker (future LLM option) |
| Governance Separation | LLM bounded; engine controls execution | Governance Layer (G(S), A_AI(S)) constrains inference |
| Final Authority | Human decision-maker/caseworker | Human fisher |

**Differences:**

| Dimension | XHAILe | Your Research |
|-----------|--------|---------------|
| Scale | Large project (19 authors, 3.5 years) | PhD research (single researcher) |
| Use Case | eGovernment, legal tech | Safety-critical departure decisions |
| Deployment Constraints | Cloud-based; Danish public sector | Offline-capable; smartphone-class hardware; low-resource |
| Provenance | Legal auditability (DCR graphs) | Safety guarantee (Safety Dominance Property) |
| Reasoning Formalism | Declarative (constraint-based) | Imperative (production rules) |

---

## 10. Example Use Case: Technical Aids Application

### 10.1. Legal Context

> "The right to technical aids and consumer durables is described in four sections: §112, §112a, §113, §113a and §113b." (Page 3)

### 10.2. Current Process

> "The law stipulates in §112a (1-3), applications not submitted by means of digital self-service shall be rejected by the municipal council, unless special circumstances apply... Local Government Denmark maintains carefully developed official application forms as pdf documents, that can be obtained from the municipality (or printed) and filled out manually." (Page 3-4)

### 10.3. Translation Process

> "The form serves as requirement specification for the digital self-service solutions. Consequently, the digital self-service solutions are developed by two manual translations as depicted in Fig. 1. Each of these translations involve interpretations of the law, notably on what data is required to be provided by the citizen, under which conditions, and what information the citizen must be given (and consent to) as part of the application process." (Page 4)

### 10.4. DCR Graph Application

**Example from §113(2):**

> "Assistance shall only be provided where the cost exceeds DKK 500 which is based on a data value representing the cost of the consumer durables." (Page 6)

**Data-Dependent Rules:**

> "The DCR graphs should contain nodes corresponding to the input fields and rules representing which information is relevant or required based on the data provided in the input fields." (Page 6)

---

## 11. Direct Text to Insert into Your Proposal

### 11.1. For the Literature Review (Neuro-Symbolic AI)

The neuro-symbolic AI paradigm, which combines the pattern recognition capabilities of neural networks with the formal reasoning of symbolic systems, is gaining traction in high-stakes domains (Hildebrandt et al., 2026). The XHAILe project operationalizes this paradigm for legal chatbots, using DCR Graphs as the symbolic foundation and LLMs as a "bounded interface" for natural language interaction. The project explicitly notes that "the grounding in formal symbolic reasoning ensures that the final output is not a hallucination, but a natural language description of a valid logical proof derived by the symbolic engine" (Hildebrandt et al., 2026, p. 5). This mirrors our rationale for using a symbolic rule-based prototype to enable formal verification of the Safety Dominance Property, rather than relying solely on probabilistic ML models.

### 11.2. For the Conceptual Framework (Governance Separation)

The XHAILe project (Hildebrandt et al., 2026) demonstrates a parallel architectural principle: a formal separation between a symbolic rule engine (which provides auditable, legally compliant decisions) and a natural language interface (which improves accessibility but does not determine outcomes). The project's CHAI architecture enforces that "the controller guarantees sound execution, provenance, and auditability; the LLM improves accessibility... but does not determine outcomes" (Hildebrandt et al., 2026, p. 7-8). This aligns with our governance architecture, where the Deterministic Safety-State Gating Layer constrains the AI Advisory Reasoning Engine before inference begins, and final decision authority remains with the human fisher.

### 11.3. For the Expected Results (Precedent for Deployment)

The XHAILe project (Hildebrandt et al., 2026) demonstrates that symbolic rule engines can be deployed in operational high-stakes environments, achieving Technology Readiness Level (TRL) and Society Readiness Level (SRL) 7 (tested in operational environment with relevant stakeholders). This provides a precedent for the deployability of our rule-based prototype in coastal fisheries, despite the low-resource constraints of the deployment environment.

### 11.4. For the Introduction (Problem Context)

The challenge of translating complex regulations into operational decision support systems is not unique to fisheries. The XHAILe project (Hildebrandt et al., 2026) documents that Danish social services legislation comprises 2,213 clauses with 908 administrative regulations, amended an average of five times per year. A previous initiative to create a "workflow bank" of standardized process descriptions was abandoned in 2013 because maintaining up-to-date descriptions proved overwhelming. This parallels our observation that traditional weather knowledge among Malaysian fishers is eroding, while raw weather apps provide data without decision logic (Yamin et al., 2025). Both domains face the same challenge: connecting complex, changing conditions to actionable, safe decisions.

### 11.5. For Formal Specification (Alternative Formalisms)

The DCR Graphs formalism used in the XHAILe project (Hildebrandt et al., 2026) offers a potentially complementary approach to our forward-chaining rule engine. DCR graphs are declarative: they define what is forbidden or required, leaving everything else allowed. This aligns with the nature of law—and, we would argue, with safety-critical decision-making—where prohibitions and requirements are more stable than operational sequences. While our prototype uses imperative production rules to enable direct proof by construction via Rule-Set Starvation, DCR Graphs represent an alternative formalism for future work, particularly if the system were to be extended with temporal or data-dependent rules.

---

## 12. Additional References to Add from XHAILe's Bibliography

| Citation | Relevance to Your Research |
|----------|----------------------------|
| Belle, V. (2025) — Neurosymbolic AI Journal | Grounds neuro-symbolic AI framing; use in your "Clarification of Scope" section |
| Hildebrandt et al. (2011) — DCR Graphs foundational | DCR formalism (alternative to your rule engine) |
| DCR Solutions — Commercial DCR tools | Shows symbolic rule engines can be commercialized and deployed |
| Process Highlighter (López et al., 2018) | NLP → DCR translation (parallel to your rule extraction) |
| Cosma et al. (2024) — Nested DCR groups | Scalability solutions for rule systems |
| Christfort et al. (2024) — Object-centric DCR | Object-oriented modelling of rules |
| López et al. (2025) — Ambiguity detection | Addresses the challenge of ambiguous text/input interpretation |

---

## 13. Suggested Bibliography Entry

```bibtex
@inproceedings{hildebrandt2026xhaile,
  author = {Hildebrandt, Thomas and L{\'o}pez-Acosta, Hugo-Andr{\'e}s and Varvoutas, Konstantinos and Olsen, Henrik Palmer and Heyl, Marieke Anne and Zabaleta, Manex Aguirrezabal and Pedersen, Bolette and Hershcovich, Daniel and Chalkidis, Ilias and Al-Laith, Ali Mohammed Ali and Raina, Aryan and Zuckmantel, Thomas and Marquard, Morten and Debois, S{\o}ren and Normann, H{\aa}kon and Storgaard, Louise and Thiesen, Gustav and Foli, Joachim and Eiby, Jacob},
  title = {{XHAILe}: Explainable Hybrid {AI} for Computational Law and Accurate Legal Chatbots},
  booktitle = {Proceedings of the 38th International Conference on Advanced Information Systems Engineering (CAiSE'26)},
  publisher = {CEUR-WS},
  year = {2026},
  note = {In press}
}

## 14. Final Assessment: Relevance to Your PhD

| Criterion | Rating | Justification |
|-----------|--------|---------------|
| Architectural Relevance | ★★★★★ | Same core pattern: symbolic engine final decision, interface separated, formal guarantees |
| Paradigm Alignment | ★★★★★ | Both positioned in neuro-symbolic AI; both cite Belle (2025) |
| Methodology Relevance | ★★★★☆ | Both use iterative, user-centered development (DSR/Reflective System Development) |
| Domain Transferability | ★★★★☆ | Legal domain differs but architectural pattern transfers directly |
| Funding Validation | ★★★★★ | XHAILe is a funded Innovation Fund Denmark project; validates your research direction |
| Technology Option | ★★★★☆ | DCR Graphs are an alternative to your forward-chaining rule engine; worth considering for future work |
| Deployment Precedent | ★★★★☆ | DCR graphs already deployed in Danish public sector; shows symbolic rule engines work in practice |
| Interdisciplinary Validation | ★★★★★ | 19 authors from computer science, law, linguistics, and industry → validates the interdisciplinary nature of your work |

---

## 15. Summary Table: How to Use This Paper

| Purpose | How to Use XHAILe | Section to Place |
|---------|-------------------|------------------|
| Literature Review | Cite as a contemporary neuro-symbolic AI project demonstrating the value of symbolic rule engines in high-stakes domains | Literature Review (Neuro-Symbolic AI subsection) |
| Conceptual Framework | Use the "LLM as bounded interface to rule engine" pattern to explain your governance layer | Conceptual Framework (Governance Layer explanation) |
| Neuro-Symbolic Framing | Cite Belle (2025) which XHAILe uses; shows your approach is aligned with funded research | Introduction / Clarification of Scope |
| Formal Verification Rationale | Quote "the grounding in formal symbolic reasoning ensures that the final output is not a hallucination" | Conceptual Framework / Expected Results |
| Governance Separation Principle | Quote "the controller guarantees sound execution, provenance, and auditability; the LLM improves accessibility but does not determine outcomes" | Conceptual Framework (Layer 2 explanation) |
| Methodology Validation | XHAILe's Reflective System Development parallels your DSR + contextual user validation | Research Design and Methodology |
| Future Directions | Consider DCR Graphs as an alternative formalism for your reasoning layer | Future Work / Discussion |
| Problem Context | Document legal complexity and failed automation attempts to contextualize similar challenges | Introduction / Problem Statement |
| Deployment Precedent | Show that symbolic rule engines can achieve TRL/SRL 7 in operational environments | Expected Results / Potential for Application |

---

## 16. Comparison with Your PhD Research: Extended Table

| Aspect | XHAILe | Your PhD Research | Insight |
|--------|--------|-------------------|---------|
| Domain | Legal/eGovernment | Fisheries safety | Different domains, same structural challenges |
| Problem Type | Regulatory complexity, manual translation, maintenance burden | Safety-critical decisions under uncertainty, eroding traditional knowledge | Both involve high-stakes decisions with changing conditions |
| AI Paradigm | Neuro-symbolic (LLM + DCR) | Classical AI (symbolic rule-based) + ML architectural extension | Both use neuro-symbolic framing; you emphasize formal verification |
| Symbolic Formalism | DCR Graphs (declarative, constraint-based) | Production rules (imperative, if-then) | Different but complementary approaches to rule representation |
| Interface | LLM chatbot (citizens/caseworkers) | Human decision-maker (fishers) | Both maintain human final authority |
| Governance | LLM bounded; hard guardrails; engine controls execution | G(S), A_AI(S); Rule-Set Starvation; governance layer constrains inference | Both enforce formal separation between interface and reasoning |
| Formal Guarantee | "Not a hallucination"; auditable proof trace | Safety Dominance Property; proof by construction | Both prioritize formal verification over empirical performance |
| Deployment | Cloud-based; Danish public sector | Offline-capable; smartphone-class; low-resource | You address more severe resource constraints |
| Scale | 3.5-year, 19-author project | 3-year PhD, single researcher | XHAILe validates your research direction is fundable and relevant |
| Methodology | Reflective System Development (action research) | Design Science Research (DSR) | Both use iterative, user-centered design |
| User Validation | Real users in operational environment | Small-scale fishers and fisheries officers | Both validate with actual end-users |
| Commercial Partners | DCR Solutions, TietoEvry, Kommuneforlaget | LKIM (potential) | Both have institutional partners |

---

## 17. Conclusion

**Summary:** This paper provides strong validation for your research direction and should be cited prominently in your proposal. It demonstrates that your architectural pattern (symbolic engine + governance/interface separation) is part of an active, funded research program with established industrial partners and real-world deployments. The paper also provides a rich set of references—particularly Belle (2025) and the neuro-symbolic AI literature—that you can use to strengthen your theoretical framing.

**Key Takeaway:** If a funded 19-author project involving top Danish universities and industry partners is building the same kind of system (symbolic rule engine + bounded interface + formal guarantees) for legal compliance, your approach for fisheries safety is not just valid—it is at the forefront of a recognized research paradigm. Your research applies the same neuro-symbolic principles to a different high-stakes domain (safety-critical fisheries decisions) with more severe resource constraints (offline, smartphone-class, low-resource), making it a novel and timely contribution.

---

## 18. Quick Reference: One-Page Summary

| Item | Details |
|------|---------|
| **Full Citation** | Hildebrandt, T., et al. (2026). XHAILe: Explainable Hybrid AI for Computational Law and Accurate Legal Chatbots. *CAiSE'26*. CEUR-WS. |
| **Core Problem** | LLMs hallucinate; high-stakes legal decisions need formal guarantees |
| **Core Solution** | Neuro-symbolic AI: LLM as bounded interface + DCR Graph rule engine |
| **Key Principle** | "Controller guarantees sound execution, provenance, and auditability; LLM does not determine outcomes" |
| **Your Parallel** | Governance Layer constrains inference; rule engine provides formal Safety Dominance Property |
| **Why Cite** | Validates neuro-symbolic approach; shows symbolic engines are deployable in practice; provides funding validation |
| **Key References to Add** | Belle (2025) — DOI: 10.1177/29498732251339951 |
| **Project Status** | 3.5-year project (April 2025–October 2028); in progress |
| **TRL/SRL Target** | Level 7 (operational environment with relevant stakeholders) |

---

## 19. References from XHAILe Most Relevant to Your Research

| Reference | Full Citation | Relevance |
|-----------|---------------|-----------|
| Belle (2025) | Belle, V. (2025). On the relevance of logic for artificial intelligence, and the promise of neurosymbolic learning. *Neurosymbolic Artificial Intelligence*, 1, 29498732251339951. DOI: 10.1177/29498732251339951 | Grounds neuro-symbolic AI framing; use in your "Clarification of Scope" section |
| d. Garcez & Lamb (2023) | d. Garcez, A., & Lamb, L. C. (2023). Neurosymbolic AI: The 3rd wave. *Artificial Intelligence Review*. | Establishes neuro-symbolic AI as an active research paradigm |
| Hildebrandt et al. (2011) | Hildebrandt, T. T., & Mukkamala, R. R. (2011). Declarative event-based workflow as distributed dynamic condition response graphs. *arXiv:1110.4161*. | DCR formalism foundational paper |
| López et al. (2018) | López, H. A., Hildebrandt, T., Debois, S., & Marquard, M. (2018). The process highlighter: From texts to declarative processes and back. *CEUR Workshop Proceedings*. | NLP → DCR translation |
| Cosma et al. (2024) | Cosma, V. P., et al. (2024). Improving simplicity by discovering nested groups in declarative models. *CAiSE'24*. | Scalability solutions for rule systems |
| Christfort et al. (2024) | Christfort, A. K., et al. (2024). Discovery of object-centric declarative models. *ICPM'24*. | Object-oriented modelling of rules |
| López et al. (2025) | López, H. A., et al. (2025). Ambiguity detection in business process descriptions. *BPM'25*. | Addresses ambiguous text/input interpretation |

---

## 20. Suggested Citation for Your Proposal

```bibtex
@inproceedings{hildebrandt2026xhaile,
  author = {Hildebrandt, Thomas and L{\'o}pez-Acosta, Hugo-Andr{\'e}s and Varvoutas, Konstantinos and Olsen, Henrik Palmer and Heyl, Marieke Anne and Zabaleta, Manex Aguirrezabal and Pedersen, Bolette and Hershcovich, Daniel and Chalkidis, Ilias and Al-Laith, Ali Mohammed Ali and Raina, Aryan and Zuckmantel, Thomas and Marquard, Morten and Debois, S{\o}ren and Normann, H{\aa}kon and Storgaard, Louise and Thiesen, Gustav and Foli, Joachim and Eiby, Jacob},
  title = {{XHAILe}: Explainable Hybrid {AI} for Computational Law and Accurate Legal Chatbots},
  booktitle = {Proceedings of the 38th International Conference on Advanced Information Systems Engineering (CAiSE'26)},
  publisher = {CEUR-WS},
  year = {2026},
  note = {In press}
}