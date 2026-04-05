# Literature Review Extraction
## Paper: Artificial Intelligence for Safety-Critical Systems in Industrial and Transportation Domains: A Survey

---

## Early Relevance Check: PASSED — Proceed with Full Extraction

1. **Addresses core themes?** Yes — safety-critical AI, AI governance/control, hybrid AI, human role, socio-technical evaluation
2. **Contributes to relevant areas?** Yes — safety-critical AI architecture, AI governance mechanisms, hybrid AI design, formal safety standards
3. **Citable in literature review?** Yes — comprehensive survey of safety techniques, governance mechanisms (safety bags, monitors, envelopes), and classification frameworks (Class I/II/III) for AI in safety-critical systems

---

## 1. Paper Identity

- **Title:** Artificial Intelligence for Safety-Critical Systems in Industrial and Transportation Domains: A Survey
- **Authors:** Jon Perez-Cerrolaza, Jaume Abella, Markus Borg, Carlo Donzella, Jesús Cerquides, Francisco J. Cazorla, Cristofer Englund, Markus Tauber, George Nikolakopoulos, Jose Luis Flores
- **Year:** 2024 (Published April 2024; Online AM October 2023)
- **Venue:** ACM Computing Surveys, Volume 56, Issue 7, Article 176
- **DOI:** https://doi.org/10.1145/3626314
- **Type:** Survey / Systematic review (40 pages, 294 references)

---

## 2. Core Contribution

- **Problem addressed:** The literature on AI for safety-critical systems is vast and fragmented across domains (automotive, avionics, railway, industrial, robotics), safety standards, AI types, lifecycle phases, and levels of autonomy. There is no consolidated overview of challenges, techniques, and methods for reconciling cutting-edge AI with safety engineering processes and standards.

- **Proposed solution / key finding:** A structured survey that categorises AI safety techniques across three points of application — **product** (AI embedded in the safety-critical system), **runtime** (AI with online learning/adaptation), and **process** (AI assisting safety engineering development). The survey introduces a unifying taxonomy covering Types of AI (TAI), levels of automation (autonomous, heteronomous, automatic), ISO 5469 Usage Levels, and a Class I/II/III safety compliance classification.

- **Main contributions:**
  1. Structured categorisation of safety techniques for AI-based products (safety bags, safety monitors/envelopes, formal verification)
  2. Taxonomy reconciling cross-domain terminology (TAI, automation levels, safety standards, usage levels, classes)
  3. Analysis of runtime learning/adaptation safety techniques (safety bag, safe adaptation, limited adaptation, limited actuation, library-based offline)
  4. Survey of AI-based development assistance for safety engineering (traditional V-model and ML workflow)
  5. Discussion of trustworthiness dimensions (engineering, ethics, legal)

- **What is novel:** The cross-domain, cross-lifecycle structuring of a highly fragmented field. The Class I/II/III taxonomy provides a clear framework for how AI of varying certifiability can be used in safety-critical systems through compensatory measures.

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | **Yes** | Core theme — the survey extensively covers hybrid architectures where rule-based safety mechanisms (safety bags, safety envelopes, formal verification) constrain or monitor AI/ML outputs. The Class II approach is fundamentally a hybrid: AI performs the function, a rule-based safety bag ensures safety. |
| Safety-critical AI decision-making | **Yes** | Central topic of the entire survey. Covers safety-critical AI across automotive AD, avionics, railway, industrial robotics, UAVs/UAS, and space. |
| AI governance / control mechanisms | **Yes** | Extensively covers governance mechanisms: safety bags (runtime checkers), safety monitors/envelopes, run-time assurance (ASTM F3269), formal verification, Class I/II/III classification of AI safety compliance, and safety assurance cases. |
| Low-resource environments | **Partial** | Mentions SWaP (Size, Weight, Power) constraints for UAVs/drones and execution platform limitations. Discusses lightweight deployment on embedded platforms. Does not address low-resource environments in the development-nation, limited-data, limited-connectivity sense. |
| Decision architecture formalisation | **Partial** | Discusses safety assurance cases, Safety Integrity Levels (SIL), and formal verification of safety properties. Does not formalise a decision pipeline comparable to E → S = f(E) → (G(S), A_AI(S)) → AI(E). |
| Human role in decision-making | **Yes** | Distinguishes autonomous (no human-in-the-loop), heteronomous (varying degrees of human collaboration/supervision), and automatic systems. Discusses human cognitive limitations (overload, oversight, reaction time) in context of safety monitors. |
| Socio-technical evaluation | **Partial** | Section 7 covers trustworthiness across engineering, ethics, and legal dimensions. Discusses the "moral machine experiment," liability, GDPR, and the EU AI Act. Does not conduct empirical socio-technical evaluation. |
| Coastal fisheries / maritime domain | **No** | Not addressed. Focus is on automotive, avionics, railway, industrial robotics, and UAVs. |

**Mid-Extraction Relevance Gate:** 4 Yes + 3 Partial → **FULL EXTRACTION**

---

## 4. Decision Architecture Analysis

- **Decision-making structure:** The survey does not propose a single decision architecture. Instead, it catalogues architectural patterns used across domains. The predominant pattern is a **layered/supervisory architecture** where:
  - An AI item performs a function (perception, control, optimisation)
  - A safety mechanism (safety bag, safety monitor, safety envelope) monitors and constrains the AI item's outputs
  - The overall AI-based safety-critical system is composed of one or more AI-based systems, each containing one or more AI items, deployed on execution platforms

- **Safety constraint mechanisms:** Multiple mechanisms are catalogued:
  - **Safety bag / diverse monitor** (IEC 61508-7 C.3.4): A certified runtime checker that monitors AI outputs and activates a safe state if outputs are unsafe. This is the primary Class II compensatory measure.
  - **Safety envelope / safety monitor / runtime monitor:** Formally specified operational rules that bound AI behaviour at runtime. Used extensively in avionics (ASTM F3269) and AD.
  - **Formal verification (Class I):** Offline verification of all possible input-output combinations to guarantee safety.

- **Rule-based constraints before AI?** Yes — the safety bag and safety envelope approaches enforce rule-based safety checks on AI outputs at runtime. In Class II systems, the safety bag is the certified safety function; the AI item is non-safety (Usage Level C).

- **Boundary between deterministic control and AI reasoning:** Clearly defined through the Class I/II/III taxonomy:
  - **Class I:** AI can be fully verified (formal verification) → deterministic safety assurance
  - **Class II:** AI cannot be fully verified, but compensatory measures (safety bag, safety monitor) provide deterministic safety bounds around non-deterministic AI
  - **Class III:** AI cannot be verified and compensation is insufficient → not safety-critical; human is responsible

- **Failure modes and fallback:** Safety bags activate safe states when AI outputs violate safety constraints. The ASTM F3269 architecture switches to a recovery control function when the complex function operates outside safe constraints. Library-based offline technique pre-defines all possible safe configurations for runtime transitions.

---

## 5. Formal Model and Mathematical Representation

- **Formal model defined?** Not a unified formal model of the decision system. The survey references formal methods used within individual papers (Reluplex for NN verification, model checking for AD overtaking, Bayesian methods for uncertainty quantification) but does not itself define a formal pipeline.

- **Comparison to E → S = f(E) → (G(S), A_AI(S)) → AI(E):**
  - The survey does not define an equivalent pipeline. The closest structural analogy is the Class II architecture: environment → safety bag evaluates AI output → AI output is either permitted or blocked (safe state activated). However, this is a **binary gate** (permit/block), not a graduated model.
  - The Safety Integrity Level (SIL 1–4) provides a classification of *system integrity requirements* at design time, not a runtime safety state classification of environmental conditions.

- **State-dependent recommendation restriction?** No. The survey describes binary control: AI outputs are either permitted (within safety envelope) or blocked (safe state activated). There is no intermediate mode where AI participates with restricted output types. The closest is the heteronomous system concept where humans retain varying degrees of supervision, but this is about automation level, not state-conditioned AI output restriction.

- **Safety Dominance Property equivalent?** The safety bag / safety envelope concept enforces a property that AI outputs must fall within formally specified safety bounds. This is functionally similar to AI(E) ⊆ A_AI(S), but it is applied as a binary check (within bounds or not), not as a graduated, state-conditioned constraint. There is no formal equivalent to A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅.

- **Formalisation purpose:** Where formal methods are used (referenced papers), they serve verification (proving safety properties) and runtime monitoring (checking constraint satisfaction). The survey itself is descriptive/taxonomic rather than formal.

---

## 6. Safety State Classification

- **Discrete risk/safety levels?** Yes, but at the **design-time system integrity** level, not at the **runtime environmental state** level:
  - **SIL 1–4** (IEC 61508): Safety Integrity Levels classifying the required integrity of safety functions
  - **ASIL A–D** (ISO 26262): Automotive Safety Integrity Levels
  - **DAL A–E** (avionics): Design Assurance Levels
  - **TPL 0–4** (VDE-AR-E 2842-61): Trustworthiness Performance Levels

- **How do these compare to S = f(E) → {SAFE, CAUTION, UNSAFE}?** These are fundamentally different. SIL/ASIL/DAL classify the **required integrity of the safety function** based on risk analysis at design time. They do not classify **runtime environmental conditions** into operational safety states. My S = f(E) is a runtime function that evaluates current environmental inputs to determine the current safety state; SIL is a design-time attribute of the system.

- **Does AI recommendation scope change across levels?** No. The Class I/II/III classification determines *how* AI can be used (fully verified, with compensatory measures, or not safety-critical), but this is a design-time architectural decision, not a runtime state-conditioned restriction on AI output types.

- **CAUTION mode equivalent?** **Not present.** The survey consistently describes **binary** runtime safety control:
  - AI outputs are within safety envelope → permitted
  - AI outputs violate safety constraints → blocked, safe state activated
  - There is no intermediate state where AI participates with a restricted recommendation space

---

## 7. Governance Level Analysis

| Level | Question | Implemented? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (G(S)) | **Yes** | Safety bag/safety monitor/safety envelope: monitors AI output and can block it entirely, activating safe state. ASTM F3269 run-time assurance can switch from complex function to recovery control. Class II/III distinction determines whether AI can participate in safety functions at all. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | **No** | No mechanism restricts the *type* of AI recommendations based on classified safety state. The safety bag checks whether a specific AI output is safe/unsafe — it does not restrict the *categories* of output the AI is permitted to generate. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | **No** | Design-time safety classification (SIL/ASIL) determines architectural requirements. Runtime safety mechanisms (safety bags, monitors) perform binary permit/block on individual outputs. No unified, state-conditioned governance pair exists. |

- **Binary or graduated?** **Binary.** All safety mechanisms described operate as binary switches: AI output is either within the safety envelope (permitted) or outside it (blocked → safe state). The survey explicitly describes this as the state of the art.

- **Level 2 governance present?** Not in the state-conditioned sense. Per-action output filtering exists (safety bags check individual outputs), but this is output validation, not state-conditioned restriction of the AI's admissible recommendation space.

- **Support or contradict two-level governance?** The survey **implicitly supports the need** for graduated governance by cataloguing the limitations of binary approaches. The observation that "excessive false alarms could lead to new system-level hazards" in binary safety bags suggests the need for intermediate modes. However, the survey does not propose or identify graduated governance as a solution. This is a **gap** the survey leaves open.

---

## 8. Human Role in Decision-Making

- **Human involvement:** Varies by automation level:
  - **Automatic systems:** No human intervention; operate in closed environments with known safety rules
  - **Heteronomous systems:** Human collaboration, control, and supervision at varying degrees (e.g., AD SAE levels 1–4, avionics levels 1A-3A)
  - **Autonomous systems:** No human-in-the-loop; operate in open environments

- **Decision support vs. automation:** The survey covers both. Class III AI (e.g., ADAS) explicitly positions AI as decision support where the driver is responsible. Class II automatic systems (e.g., railway interlocking) are decision automation with safety bag oversight.

- **Human override/escalation:** Heteronomous systems require human capability to take control. The survey notes human cognitive limitations (overload, oversight, reaction time) as constraints on safety monitor design — excessive false alarms can create new hazards.

- **Relevance to my research:** The heteronomous category maps closely to my decision support model. The survey's observation about cognitive overload from binary safety monitors supports the motivation for a graduated approach (CAUTION mode) that provides restricted but useful AI advice rather than a jarring full-block.

---

## 9. System Constraints and Environment

- **Real-world constraints:** Discusses SWaP constraints for UAVs and embedded execution platforms. Mentions computational resource demands for AutoML and DL model training. Notes that training tools and platforms are typically non-safety-qualified.

- **Real-world deployment vs. simulation:** The survey notes that field testing alone is generally considered not feasible for autonomous systems, and validation relies heavily on simulation frameworks. Some systems have been deployed (e.g., SIL4 railway interlocking with safety bag, ADAS systems).

- **Resource-aware design:** Mentions DNN compression for avionics collision avoidance, deployment on edge devices (GPUs, FPGAs, TPUs, NPUs), and the need for temporal predictability. Discusses lightweight approaches but not in the context of developing-nation low-resource environments.

- **Low-resource gaps:** The survey focuses on industrial/transportation domains with substantial engineering infrastructure. It does not address environments with limited data availability, intermittent connectivity, low computational budgets, or non-expert users — which are central to my research context.

---

## 10. Hybrid AI Taxonomy

- **Hybrid approach type:** The survey catalogues multiple hybrid patterns:
  - **Supervisory control (Class II):** AI output monitored by rule-based safety bag/safety monitor. Most prevalent pattern.
  - **Neuro-symbolic:** Symbolist approaches (decision trees, formal logic) used to explain or verify connectionist (NN/DL) models
  - **Rule-ML pipeline:** Safety rules pre-process (constrain input space) or post-process (validate output) ML results
  - **Safe adaptation:** Hybrid TAI (connectionist + fuzzy) with safety-compliant runtime adaptation

- **Where does safety enforcement sit?** Primarily **after** AI reasoning (safety bag checks outputs). Also **before** (formal specification of safety envelopes constrains the operational domain) and **alongside** (runtime monitors run in parallel with AI). The dominant pattern is post-hoc output monitoring.

- **Two-level governance support?** No. All described hybrid patterns implement **single-level** governance: AI is either permitted to operate (within safety envelope) or blocked. None implement a second governance level that restricts the *type* of AI output based on classified environmental state.

- **Comparison to my architecture:** My deterministic-gate-first, two-level governance model differs from the survey's state of the art in two key ways:
  1. My gate function G(S) is conditioned on classified *environmental* safety state S = f(E), not on AI output validation
  2. My Level 2 governance A_AI(S) restricts the *categories* of permissible AI recommendation, not just the *values*. No mechanism in this survey does this.

---

## 11. Baseline Comparison and Evaluation

- **Baseline comparisons:** The survey does not itself conduct evaluations. It reports that individual papers compare AI approaches against baselines (e.g., human-designed vs. AutoML models for AD perception). The safety bag technique has been deployed in certified systems (SIL4 railway interlocking since the 1980s).

- **CAUTION zone testing?** Not present. No referenced paper tests behaviour in an intermediate mode where AI participates under restriction. Evaluations test binary conditions: AI within safety bounds (permitted) or outside (blocked).

- **Safety Dominance Property verification?** Not as a formal property. Safety bag evaluations verify that unsafe AI outputs are caught and blocked, which is a binary version of the concept. No evaluation verifies graduated constraint satisfaction.

- **Graduated vs. binary governance comparison?** Not conducted. The survey does not compare systems with intermediate governance modes against binary systems. This is a significant evaluation gap relevant to my research.

- **Evaluation gaps identified:**
  - Testing and validation of AI-based autonomous systems is "still an unsolved key area"
  - Field testing alone is "generally considered not feasible"
  - Data management has "recurrent challenges and limited research contributions"
  - AutoML for safety-critical model training has "limited research" addressing systematic error reduction
  - No evaluation of graduated governance models

---

## 12. Key Concepts and Definitions

- **Safety Bag (a.k.a. diverse monitor, IEC 61508-7 C.3.4):** A certified runtime checker that monitors AI outputs and ensures they are safe; activates safe state if not. The safety bag is the safety function; the AI item becomes non-safety (Class II).

- **Safety Envelope (a.k.a. safety monitor, runtime monitor, runtime verification, supervisor, guardian agent, safety layer, safety net):** Formally specified operational rules that bound the behaviour of complex AI functions at runtime.

- **Class I / II / III:** Taxonomy for AI safety compliance:
  - **Class I:** AI can be developed and reviewed in compliance with safety standards (e.g., formal verification of all input-output combinations)
  - **Class II:** AI cannot be fully verified, but compensatory measures (safety bag, diverse monitor) are sufficient
  - **Class III:** AI cannot be verified and compensation is insufficient; not safety-critical

- **Usage Level (UL) A–D (ISO 5469):** Classifies how AI technology is used: A = safety function (A1 = automated decisions, A2 = non-automated), B = development process, C = non-safety function with potential interference, D = non-safety function interference-free

- **Safety Integrity Level (SIL 1–4):** Discrete integrity levels from IEC 61508, classifying the required integrity of safety functions based on risk analysis

- **Trustworthiness Performance Level (TPL 0–4):** From VDE-AR-E 2842-61, requiring traceability of trustworthiness attributes through development

- **ML Properties for safety assurance:** Auditability, Data Quality, Explainability/Interpretability, Monitorability, Provability, Robustness

- **Point of Application:** Product (embedded AI), Runtime (online learning AI), Process (AI assisting development)

- **Heteronomous system (ISO 22989):** System operating in a semi-open environment with varying degrees of human collaboration, control, and supervision

---

## 13. Limitations and Unsolved Problems

- **Stated limitations:**
  - "There are still no structured development approaches, methods and tools with generic acceptance for developing AI-based safety-critical systems"
  - Generic application of formal verification for autonomous systems is "questionable" due to uncertainty and high-dimensional design spaces
  - Safety standards have "little or no consideration for AI technology"
  - Fragmented and scarce research contributions for traditional safety engineering with AI
  - Data management has "recurrent challenges and limited mitigation techniques"
  - Training tools and platforms lack safety standard compliance support
  - No consolidated industry best practices exist

- **Future work acknowledged:**
  - Need for comprehensive AI safety engineering approach with generic techniques, lifecycles, methods, and processes
  - Data management for safe model training and verification
  - Model verification scalability and automation
  - Explainability as a "pivotal attribute" requiring further development
  - System-level safety assurance cases using ML properties
  - Trustworthiness across engineering, ethics, and legal dimensions

- **Gaps my architecture addresses:**
  - **Two-level governance model:** The survey describes only binary (Level 1) governance — permit or block AI entirely. No paper implements Level 2 (state-conditioned restriction of AI recommendation scope). My (G(S), A_AI(S)) pair directly fills this gap.
  - **CAUTION mode:** The survey identifies no intermediate operating mode where AI participates with restricted output. My CAUTION state (G(S) = 1, A_AI(CAUTION) ⊂ A_AI(SAFE)) provides exactly this.
  - **Safety Dominance Property for graduated governance:** The survey describes binary safety bounds enforcement. My Safety Dominance Property (AI(E) ⊆ A_AI(S)) extends this to graduated, state-conditioned constraints.
  - **Excessive false alarms from binary blocking:** The survey notes that "excessive false alarms could lead to new system-level hazards" — my graduated approach mitigates this by providing restricted-but-useful AI advice in CAUTION rather than full blocking.

---

## 14. Methodology Notes

- **Research method:** Systematic survey / literature review with structured categorisation using a multi-dimensional taxonomy (TAI, automation levels, safety standards, point of application, Class I/II/III).

- **Alignment with DSR pipeline?** Partially. The survey is a literature synthesis, not a design science artefact. However, its taxonomies and categorisations provide a structured landscape that informs the *design* phase of DSR by identifying the gap space and existing baselines.

- **Methodological insights for my research:**
  - The Class I/II/III taxonomy provides a useful framework for positioning my architecture: the safety gate function G(S) operates as a Class I deterministic component, while the AI reasoning operates under its governance (analogous to Class II pattern where safety mechanism bounds AI).
  - The point of application taxonomy (product/runtime/process) helps position my work as a *product* contribution (architecture for deployed decision support system).
  - The survey's cross-domain approach validates the transferability argument — safety mechanisms developed for automotive/avionics can inform maritime/fisheries applications.

---

## 15. Quotable / Citable Points

1. **Binary governance as state of the art:** The survey consistently describes safety bags, safety monitors, and safety envelopes as binary mechanisms that permit or block AI outputs entirely. This is citable as evidence that the current paradigm is binary governance (Level 1 only). *(Sections 4.1, 4.2.4, 5.1.1)*

2. **False alarm hazard of binary blocking:** The survey notes that "excessive false alarms could lead to new system-level hazards (e.g., cascade errors in systems with multiple safety functions) and should also consider human cognitive limitations (e.g., cognitive overload, oversight and reaction time limitations)." This directly motivates the need for a graduated CAUTION mode. *(Section 4, p.176:11)*

3. **Class II pattern — safety bag as compensatory measure:** "The safety bag becomes the safety function that prevents unsafe states, and the AI item does not require safety standard compliance." Citable as the dominant architectural pattern for AI in safety-critical systems. *(Section 3.4, p.176:9)*

4. **No generic acceptance for AI safety engineering:** "Nowadays, there are still no structured development approaches, methods and tools with generic acceptance for developing AI-based safety-critical systems." Citable for gap motivation. *(Section 1, p.176:2)*

5. **Pareto principle observation:** The survey suggests that achieving full autonomous AI safety certification may follow a Pareto distribution — 20% effort has yielded 80% technical progress, but the remaining 20% may require 80% additional effort due to the extreme failure probability requirements. *(Section 8.1, p.176:25–26)*

---

## 16. Relation to My Research and Positioning

- **Governance level implemented:** Level 1 only (participation control) — the survey catalogues safety bags, safety monitors, safety envelopes, and formal verification, all of which implement binary permit/block governance.

- **Level 2 implemented?** No. No mechanism described in this survey restricts the *type* or *scope* of AI recommendations based on classified environmental safety state. Per-action output validation (safety bag checking individual outputs) exists, but this is output validation, not state-conditioned advisory scope governance.

- **Proximity to (G(S), A_AI(S))?** The safety bag/safety envelope pattern implements G(S) ∈ {0, 1} — a binary gate. There is no A_AI(S) equivalent that modulates the admissible recommendation space across safety states. The closest structural analogue is the ASTM F3269 run-time assurance architecture, which switches between a complex function and a recovery control function — but this is still binary (complex function or recovery), not graduated.

- **Formal safety property?** Safety bag/envelope enforcement is functionally equivalent to: "AI output ∈ safety bounds ⇒ permit; else ⇒ block." This is a binary version of the Safety Dominance Property. No graduated equivalent is defined.

- **Gap my research fills:** The entire survey confirms that binary governance (permit/block) is the universal paradigm for AI in safety-critical systems across all domains surveyed. No paper implements a graduated governance model with an intermediate mode where AI still participates under restricted advisory scope. My two-level governance pair (G(S), A_AI(S)) with the CAUTION state directly fills this gap.

- **Positioning paragraph:** This survey serves as **comprehensive background and gap evidence** for my research. It provides the most thorough cross-domain catalogue of safety mechanisms for AI in safety-critical systems, and it consistently confirms that the state of the art is binary governance: AI outputs are either permitted or blocked entirely. The Class I/II/III taxonomy, the safety bag/safety envelope concepts, and the ML properties framework provide essential vocabulary and baseline mechanisms that my architecture builds upon. Critically, the survey's observation that excessive false alarms from binary blocking can create new system-level hazards and human cognitive overload directly motivates my graduated approach — the CAUTION mode provides a principled alternative to the disruptive full-block by restricting AI advisory scope rather than eliminating AI participation entirely. The survey's coverage of multiple domains (automotive, avionics, railway, industrial) also supports my argument that the binary governance gap is cross-domain, not domain-specific.

---

## 17. Overall Relevance Score

### ⭐⭐⭐ Medium

**Justification:** This is a high-quality, comprehensive survey that provides essential background on safety mechanisms for AI in safety-critical systems. It does not address the two-level governance gap directly (it is a survey, not an architecture paper), but it provides the strongest available evidence that binary governance is the universal paradigm across all industrial and transportation domains. It supplies key terminology (safety bag, safety envelope, Class I/II/III), baseline mechanisms, and the critical observation about false alarm hazards that motivates graduated governance. It does not address low-resource environments, coastal fisheries, or decision architecture formalisation at the level of my pipeline. Its primary role in my literature review is as **background and gap evidence** — documenting the state of the art against which my contribution is positioned.
