# Literature Review Extraction: Bloomfield & Rushby (2025)

## Early Relevance Check: PASSED ✅

| Screening Question | Answer |
|---|---|
| Addresses ≥1 core research theme? | **Yes** — Safety-critical AI, AI governance, architecture, human role, socio-technical |
| Contributes to safety-critical AI architecture, governance, hybrid AI, formal models, or maritime AI? | **Yes** — Central focus on guarded architectures, runtime verification, defense in depth |
| Citable in a literature review on graduated AI governance for safety-critical decision support? | **Yes** — Directly relevant as a major baseline for dependability-perspective governance architectures |

**Proceed with FULL extraction** (≥3 "Yes" in Section 3).

---

## 1. Paper Identity

- **Title:** Assurance of AI Systems From a Dependability Perspective
- **Authors:** Robin Bloomfield (City, University of London) and John Rushby (SRI International)
- **Year:** 2025 (arXiv v3: 2 June 2025; CSL Technical Report SRI-CSL-2024-02R3, 4 June 2025)
- **Venue:** SRI International Technical Report (CSL series), arXiv:2407.13948v3, DARPA ANSR Program
- **Type:** Comprehensive technical report / position paper with architectural analysis
- **Length:** 87 pages + 254 references
- **DOI/Identifier:** arXiv:2407.13948v3

---

## 2. Core Contribution

### Problem Addressed
How to provide dependability assurance for systems incorporating AI and ML, given that AI/ML components are opaque, experimentally derived, and cannot satisfy classical fault-avoidance assurance requirements (which demand near-complete understanding of internal design and operation).

### Proposed Solution
A **dependability perspective** on AI assurance that:
1. **Minimises trust in AI/ML** by treating them as unreliable components within guarded architectures
2. Uses **runtime verification** via conventionally engineered guards to check AI behaviour against safety properties
3. Employs **diversity and defense in depth** through layered architectures with multiple protection levels
4. Distinguishes a **dependability/trustworthiness spectrum** — from placing no trust in AI/ML (dependability end) to full trust (trustworthiness end)

### Main Contributions
1. A systematic **taxonomy of 8 architectural patterns** (numbered 1–8) for guarded AI systems, progressing from unguarded through assured backup guards to micro-ODD-specialised guard portfolios
2. Formal distinction between **assuredly guarded** systems (guards use no AI/ML) and **unassuredly guarded** systems (guards depend on AI/ML for perception)
3. Analysis of the **perception assurance problem** as the fundamental bottleneck — action guards can generally be assured, but perception guards cannot
4. Application of **defense in depth** from nuclear power (control → limitation → shutdown) to AI systems (primary → safety-focused → emergency backup)
5. Discussion of **micro-ODDs** as a strategy to specialise assured backup guards for different operational circumstances
6. Extension from CPS to specific-function AI, general-purpose AI (LLMs), and speculative AGI/AFGI scenarios

### Novelty
- Reframes AI safety as a classical dependability engineering problem rather than an alignment/trustworthiness problem
- Provides the most comprehensive architectural taxonomy of guarded AI systems from the dependability perspective
- Identifies perception assurance (not action assurance) as the critical unsolved problem
- Introduces the concept of **recursively structured** guard architectures where guards themselves may be guarded

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| **Hybrid AI (rule-based + probabilistic)** | **Yes** | Core framing: conventionally engineered (deterministic) guards constraining AI/ML (probabilistic) components. Discusses neurosymbolic AI, dual-process architectures (System 1/System 2), and predictive processing. |
| **Safety-critical AI decision-making** | **Yes** | Central topic. Covers assurance requirements from 10⁻³ to 10⁻⁹ failure rates. Discusses CPS, autonomous vehicles, nuclear power, avionics as domains. |
| **AI governance / control mechanisms** | **Yes** | Extensively covers runtime verification, guards, backup systems, guardrails, defense in depth. Distinguishes internal guardrails (unassurable) from external guards (potentially assurable). |
| **Low-resource environments** | **Partial** | Discusses ODDs and micro-ODDs as operational constraints; mentions graceful degradation and the idea that simpler guards may be more trustworthy. Does not specifically address data-limited, connectivity-limited, or compute-limited environments. |
| **Decision architecture formalisation** | **Partial** | Provides structured architectural diagrams (8 patterns) and qualitative assurance reasoning. Uses dependability terminology (fault/error/failure, 4-state model) but does not provide a formal mathematical model comparable to the DSR pipeline. |
| **Human role in decision-making** | **Yes** | Section 3.5 on human review. Discusses automation bias, ironies of automation, theory of mind requirements, human-AI model misalignment, and the need for AI to build models of human mental states. |
| **Socio-technical evaluation** | **Yes** | Discusses system boundaries extending into social context, STPA for socio-technical hazard analysis, system failures ("normal accidents"), resilience as societal adaptation. |
| **Coastal fisheries / maritime domain** | **No** | Not addressed. Domains covered: automotive, avionics, nuclear, medical, general-purpose LLMs. |

**Theme count: 5 Yes, 2 Partial, 1 No → FULL EXTRACTION**

---

## 4. Decision Architecture Analysis

### Architecture Structure
The paper presents a **layered, defense-in-depth architecture** with up to three functional tiers:

1. **Primary system** — AI/ML-based perception and action (full functionality, unassured)
2. **Safety-focused guard/limitation system** — may use AI/ML with diverse perception, checks actions against safety properties (weakly assured)
3. **Assured backup guard** — conventionally engineered, no AI/ML dependency, emergency intervention only (strongly assured)

This mirrors the nuclear power ladder: **operational control → limitation system → shutdown system**.

### Rule-Based Constraints Before AI Decisions
Yes — the core architectural principle. Guards intercept AI-proposed actions and check them against safety properties derived from a domain model before allowing execution. In Architecture 4, the action guard checks AI actions against properties; the backup guard provides last-resort intervention.

### Boundary Between Deterministic Control and AI Reasoning
Explicitly defined through the **perception/action decomposition**:
- **Action subsystems** can generally be guarded by conventionally engineered components using human-developed domain models
- **Perception subsystems** are the critical boundary — they build the local world model using AI/ML and cannot easily be guarded without also using AI/ML

### Failure Modes and Fallback
- **Assuredly guarded systems**: guard intervention (e.g., emergency braking) when safety properties violated
- **Micro-ODD approach**: specialised backup guards for different operational circumstances, reducing false alarms and providing less disruptive interventions
- **Safe failure states**: the 4-state dependability model (OK → Error → Safe Failure / Unsafe Failure) with recovery transitions
- **Resilience**: recognised as a strategy when some failures are acceptable, particularly for AFGI/AGI

### Architectural Patterns Summary (8 variants)

| # | Architecture | Assurability | Key Feature |
|---|---|---|---|
| 1 | AI perception → AI actions (no guard) | Unassured | Trustworthiness-only baseline |
| 2 | + Assured backup guard | **Assurable** | Viable for geofenced vehicles |
| 3 | + Assurable action guard (same model) | Unassurable | Guard vulnerable to perception errors |
| 4 | Combination of 2 + 3 | **Assurable** | Backup + action guard reduces demands |
| 5 | + Diverse perception, separate models | Unassurable | Diversity benefit but no cross-comparison |
| 6 | + Diverse perception, single fused model | Weakly assurable | Diversity argument for model |
| 7 | Combination of 2 + 6 | **Assured** | Best general architecture |
| 8 | Architecture 7 + micro-ODD detector + portfolio of specialised backup guards | **Assured** | Most sophisticated; recommended |

---

## 5. Formal Model and Mathematical Representation

### Formal Structure
The paper does **not** define a formal mathematical model comparable to the DSR pipeline. Its formalisation is primarily:
- **Qualitative architectural patterns** (box-and-arrow diagrams)
- **Dependability terminology** (fault → error → failure → safe failure / unsafe failure)
- **Assurance confidence levels**: weak (~10⁻³), modest (~10⁻⁶), strong (~10⁻⁹), exceptional (~10⁻¹²)
- **Probability of failure on demand (pfd)** used for quantitative reasoning about diversity (e.g., two systems with pfd ≤ 10⁻⁴ giving 10⁻⁸ combined)

### Comparison to DSR Pipeline: E → S = f(E) → (G(S), A_AI(S)) → AI(E)

| DSR Pipeline Element | Bloomfield & Rushby Equivalent | Match? |
|---|---|---|
| **E** (environmental state vector) | Local world model (built by perception) + domain model | Partial — no formal state vector definition |
| **S = f(E)** (safety state classification) | ODD/micro-ODD detection; safety property checking | Partial — ODDs are operational domains, not classified safety states |
| **G(S)** (participation gate) | Backup guard intervention (binary: allow/override) | **Yes** — structurally equivalent to Level 1 governance |
| **A_AI(S)** (admissible action space) | **Not formalised** | **No** — guards check individual actions, not state-conditioned action spaces |
| **Safety Dominance Property** | Assurance case claims; pfd calculations | Partial — assurance arguments serve a similar function but are not expressed as a formal containment property |

### State-Dependent Recommendation Restriction
**No.** The paper does not model varying AI output scope across classified safety states. Guards operate as binary interceptors: they either permit or override AI-proposed actions. There is no intermediate mode where AI participates with restricted recommendation types.

### Formal Safety Property
The paper uses **assurance case arguments** rather than formal safety properties. The closest analogue is the claim that AI actions always fall within bounds checked by the guard — but this is argued qualitatively through architectural assurance, not stated as a formal property like AI(E) ⊆ A_AI(S).

### Formalisation Purpose
Primarily **descriptive and argumentative** — used to structure reasoning about assurance claims, not for proof or formal verification of the architecture itself.

---

## 6. Safety State Classification

### Discrete Risk Levels
The paper uses a **binary classification** for AI guard intervention:
- AI action passes guard check → **permitted** (OK state)
- AI action fails guard check → **overridden** (intervention/safe failure state)

The 4-state dependability model (OK, Error, Safe Failure, Unsafe Failure) provides a richer state space for the overall system, but this is a **system health model**, not an environmental safety state classification.

### Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}
**No equivalent.** The paper does not classify the operating environment into discrete safety states that condition AI governance. Instead:
- **ODDs and micro-ODDs** define operational domains where specific guard configurations apply
- Micro-ODD detection selects which backup guard to activate — but this is a **guard selection** mechanism, not a safety state classification that restricts AI advisory scope

### CAUTION State Equivalent
**Absent.** The paper implements binary governance at each guard: AI is either permitted or overridden. There is no intermediate mode analogous to CAUTION where AI still participates but with restricted output types. The closest structural analogue is the **limitation system** in nuclear power (between operational control and shutdown), which reduces plant capability without full shutdown — but this is not formalised as restricting the AI's recommendation scope.

---

## 7. Governance Level Analysis

| Level | Question | Implemented? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (≡ G(S)) | **Yes** | Backup guard can override/disable AI actions entirely. Guard intervention = G(S) = 0. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (≡ A_AI(S)) | **No** | Guards check individual actions against safety properties; they do not restrict the *types* of recommendation AI may generate based on classified environmental state. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | **No** | Guard intervention is triggered by detected property violations, not by a classified safety state that conditions both participation and scope. |

### Binary vs. Graduated Governance
**Binary.** Each guard implements a binary switch: permit or override. The **defense in depth** architecture provides multiple binary switches (action guard, backup guard), but none implements graduated governance where AI advisory scope is restricted without full override.

### State-Conditioned vs. Static
The **micro-ODD approach** (Architecture 8) introduces conditional guard selection (different backup guards for different operational circumstances), which is a form of state-conditioned governance at Level 1. However, within each micro-ODD, governance remains binary (permit/override).

### Support for Two-Level Governance Pair
The paper **strongly supports the motivation** for two-level governance but **does not implement it**:
- The nuclear power analogy (control → limitation → shutdown) implicitly recognises that binary shutdown is too crude and that an intermediate "limitation" mode is valuable
- The discussion of micro-ODDs recognises that different operational states require different guard configurations
- But neither mechanism restricts what the AI may *recommend* — only whether its actions are permitted or overridden

**This paper is excellent gap evidence:** it represents the state of the art in dependability-perspective governance and demonstrates that even the most sophisticated architectures implement only Level 1 (binary participation control), confirming the gap that Level 2 (advisory scope governance conditioned on safety state) fills.

---

## 8. Human Role in Decision-Making

### Decision Support vs. Automation
The paper covers both:
- **Decision automation**: autonomous CPS (self-driving cars, UAVs) where the system acts
- **Decision support**: AI systems for specific functions (medical imaging, loan applications) where humans make final decisions

### Human-AI Interaction Concerns
- **Automation bias**: humans either ignore automation or trust it completely (Bainbridge's "ironies of automation")
- **Model misalignment**: humans and AI build different world models; AI lacks theory of mind for effective collaboration
- **Metacognition gap**: AI lacks higher-order thinking needed for situation awareness in uncertain environments
- **Kegworth crash example**: pilots persisted with flawed mental model despite contrary instrument data; an AI co-pilot would need to diagnose not just the physical fault but the pilot's faulty mental model

### Override Mechanism
- Assured backup guards provide override when AI actions violate safety properties
- Human review is discussed as a form of runtime verification but acknowledged as unreliable due to automation bias
- The paper notes that for assurable human oversight, AI must present explanations relative to an accurate theory of the human's state of knowledge

---

## 9. System Constraints and Environment

### Real-World Constraints
- Discusses **ODD limitations** as a strategy to reduce assurance burden by constraining operational environments
- Addresses **perception limitations**: sensor fusion challenges, adversarial examples, robustness vs. accuracy
- Notes that **testing is infeasible** for high-assurance systems (10⁹ hours needed to validate 10⁻⁹ failure rate)

### Resource-Aware Design
- **Micro-ODDs**: specialise guards for particular circumstances to reduce complexity
- **Simpler models for safety systems**: safety-focused perception could use simpler, more conservative local models (e.g., undifferentiated objects with safety boxes rather than full classification)
- **Conservative Bayesian Inference (CBI) and Bootstrapping**: methods to reduce testing requirements using prior confidence from design assurance

### Low-Resource Deployment
The paper does **not specifically address** low-resource deployment constraints (limited data, connectivity, compute). Its focus is on high-criticality systems with substantial engineering resources (automotive, avionics, nuclear). This is a gap relative to my research context.

---

## 10. Hybrid AI Taxonomy

### Classification
The paper describes a **supervisory control / constitutional governance** hybrid:
- **Conventionally engineered guards** (deterministic, rule-based) constrain **AI/ML components** (probabilistic, learned)
- The guard layer is architecturally separated from the AI layer
- Safety enforcement sits **after AI reasoning** (runtime verification of proposed actions) and **alongside it** (defense in depth with diverse safety-focused system)

### Dual-Process Architecture
The paper explicitly advocates a **dual-process architecture** inspired by human cognition:
- **System 1**: rapid AI/ML perception using predictive processing
- **System 2**: deliberative symbolic AI with domain model, intervenes on "surprises" (large prediction errors)
- System 2 provides diverse interpretation and optionally guards actions

### Two-Level Governance Support
The paper's architectures implement **single-level binary control** (permit/override). The defense-in-depth approach provides multiple such binary controls in sequence, but none restricts AI advisory scope based on classified safety state. The nuclear power analogy implicitly recognises the value of graduated control (limitation before shutdown) but does not formalise this as two-level governance.

### Comparison to DSR Architecture
| Feature | Bloomfield & Rushby | DSR Architecture |
|---|---|---|
| Guard placement | After AI reasoning (runtime) | Before AI reasoning (gate) + after (scope restriction) |
| Governance levels | Level 1 only (binary permit/override) | Level 1 (participation) + Level 2 (scope) |
| State conditioning | ODD/micro-ODD selection of guard configuration | Environmental safety state S = f(E) conditions both G(S) and A_AI(S) |
| Intermediate mode | Not formalised (limitation system concept only) | CAUTION: G(S)=1, A_AI restricted |
| Formal property | Assurance case arguments | Safety Dominance Property: AI(E) ⊆ A_AI(S) |

---

## 11. Baseline Comparison and Evaluation

### Baseline Comparisons
The paper is primarily a **position/survey report**, not an empirical study. It does not present experimental evaluations. Instead, it:
- Compares architectural patterns qualitatively (assurability assessment for each of the 8 architectures)
- References quantitative methods: CBI, bootstrapping, pfd calculations, N/T theory
- Cites real-world incidents (Uber Arizona crash, Cruise SF incident, Kegworth crash) as illustrative evidence

### CAUTION Zone Testing
**Not addressed.** Evaluation framework is binary: does the guard intervene correctly or not?

### Graduated vs. Binary Governance Comparison
**Not performed.** The paper does not compare graduated governance against binary governance.

### Formal Property Verification
The paper advocates for assurance cases but does not verify any formal property comparable to the Safety Dominance Property.

### Evaluation Gaps
- No empirical evaluation of the proposed architectures
- No testing in low-resource or degraded environments
- No comparison between Level 1-only and Level 1+2 governance
- No formal verification of guard properties

---

## 12. Key Concepts and Definitions

1. **Dependability perspective**: Assurance based on minimising trust in AI/ML components through guarded architectures, as opposed to the "trustworthiness perspective" that seeks to assure AI/ML directly
2. **Dependability/trustworthiness spectrum**: A continuum from placing no trust in AI/ML (dependability end) to full trust (trustworthiness end)
3. **Assuredly guarded systems**: Systems whose guards do not themselves use AI/ML and can therefore be assured conventionally
4. **Unassuredly guarded systems**: Systems whose guards depend on AI/ML (typically for perception) and therefore cannot be fully assured
5. **Defense in depth / ladder of protection**: Multiple diverse guard layers providing redundant protection (from nuclear power: control → limitation → shutdown)
6. **Micro-ODDs**: Specialised Operational Design Domains tailored to specific assured detection and intervention strategies
7. **4-state dependability model**: OK → Error → Safe Failure / Unsafe Failure, with transitions corresponding to fault avoidance, fault tolerance, failure management, and resilience strategies
8. **Conservative Bayesian Inference (CBI)**: Method allowing design assurance (prior confidence) to reduce testing requirements — n hours failure-free → confidence for 10n hours
9. **Bootstrapping**: Incremental confidence building over deployment lifetime
10. **Safety Performance Indicators (SPIs)**: Runtime checks of lesser claims that serve as leading indicators for potential violations of critical claims
11. **Perception assurance problem**: The fundamental bottleneck — action guards can be assured, but perception systems that build local world models using AI/ML cannot
12. **AFGI (Artificial Fairly General Intelligence)**: AI systems good enough and cheap enough to displace human services but without true AGI capabilities

---

## 13. Limitations and Unsolved Problems

### Stated Limitations
1. **No formal mathematical model** — the paper provides architectural patterns and qualitative assurance reasoning, not formal proofs
2. **Perception assurance remains unsolved** — the fundamental obstacle to fully assured AI systems
3. **No empirical evaluation** — the report is analytical/argumentative, not experimental
4. **Defense-in-depth assurance is weak** — diversity provides "useful but modest" assurance; independence of failures cannot be validated
5. **Internal guardrails are unassurable** — guardrails within LLMs are driven by the same perception and model, lack diversity, and can be faked

### Gaps Aligning with My Research

| Gap | How My Architecture Addresses It |
|---|---|
| **Guards implement only binary permit/override** — no intermediate mode where AI participates with restricted scope | DSR architecture defines CAUTION state: G(S)=1 but A_AI(CAUTION) ⊂ A_AI(SAFE) |
| **No classified environmental safety state conditioning governance** — guards react to individual property violations, not to holistic environmental assessment | S = f(E) classifies environment into {SAFE, CAUTION, UNSAFE} and conditions both G(S) and A_AI(S) |
| **No formal Safety Dominance Property** — assurance argued through cases, not formal containment | DSR defines AI(E) ⊆ A_AI(S) as a formal property |
| **No two-level governance pair** — participation and scope not distinguished as separate governance functions | DSR formalises (G(S), A_AI(S)) as a unified governance pair |
| **Architectures assume high-resource engineering** — no consideration of low-resource deployment | DSR architecture designed for low-resource environments with limited data, connectivity, and compute |

---

## 14. Methodology Notes

### Research Method
- **Position paper / technical survey** with architectural analysis
- Not DSR, not empirical — primarily analytical and argumentative
- Draws on classical dependability engineering, nuclear safety practice, and extensive literature review (254 references)

### Alignment with DSR Pipeline
The paper does not follow DSR methodology. However:
- Its **architectural analysis** (Section 2.5) corresponds to the design phase
- Its **assurance case framework** corresponds to formalisation/justification
- Its identification of **perception as the unsolved problem** informs evaluation requirements

### Methodological Insights for My Research
- The **assurance case framework** (Assurance 2.0) could inform how the DSR architecture's safety properties are justified
- The **CBI and bootstrapping** concepts provide a framework for arguing confidence in the DSR architecture's safety claims without exhaustive testing
- The **4-state dependability model** could be used to frame the DSR architecture's failure modes and recovery mechanisms

---

## 15. Quotable / Citable Points

1. **On the fundamental limitation of AI assurance** (Abstract/Section 1.1): The dependability perspective aims to minimise trust in AI/ML elements by using defense in depth with a hierarchy of less complex systems to guard them — because AI/ML internal operation is opaque and does not support the understanding required for justified confidence.

2. **On binary guard intervention** (Section 2.5, Architecture patterns): The architectural patterns demonstrate that guards implement binary permit/override control — the guard either allows the AI action or intervenes to override it, with no intermediate mode of restricted-but-non-empty AI participation.

3. **On the nuclear power analogy for defense in depth** (Section 2.4): Nuclear power generation employs a ladder of protection systems — operational control, limitation system, and shutdown system — where the limitation system reduces demands on the shutdown system, providing an intermediate level between full operation and emergency shutdown.

4. **On internal guardrails being unassurable** (Section 4.6): Internal guardrails are driven from the same perception and local model as the main action system, providing no protection for faults in those elements, and it is difficult to argue that they are either independent or diverse.

5. **On graduated risk levels for AFGI** (Section 5.2): The upper levels of risk should be more finely graduated than simply "existential" — catastrophic system failures often accumulate from combinations of smaller faults within complex systems, and safety is best achieved by making systems more resilient through being able to break and work around failure pathways.

---

## 16. Relation to My Research and Positioning

### Governance Level Implementation
- **Level 1 (participation control)**: Yes — backup guards implement binary AI override
- **Level 2 (output-scope control)**: No — guards do not restrict what types of recommendations AI may generate
- **State-conditioned**: Partial — micro-ODDs condition guard selection but not AI advisory scope

### Proximity to (G(S), A_AI(S))
The paper comes close in **spirit** but falls short in **mechanism**:
- The nuclear power limitation system concept recognises the value of an intermediate mode between full AI participation and complete override
- Micro-ODDs recognise that different operational states require different guard configurations
- But neither is formalised as a state-conditioned restriction on AI advisory scope

### Formal Safety Property
No formal Safety Dominance Property. Assurance is argued through qualitative assurance cases, not formal containment properties.

### Gap My Research Fills
This paper demonstrates that **the most sophisticated dependability-perspective architectures still implement only binary governance** (permit/override). The defense-in-depth approach provides multiple such binary checkpoints but never restricts the *type* of AI recommendation based on classified environmental safety state. My DSR architecture fills this gap by:
1. Introducing environmental safety state classification S = f(E)
2. Defining a two-level governance pair (G(S), A_AI(S)) conditioned on S
3. Formalising the CAUTION state where AI participates with restricted advisory scope
4. Proving the Safety Dominance Property as a formal guarantee

### Positioning Paragraph
Bloomfield & Rushby (2025) represents the most comprehensive treatment of AI assurance from the dependability perspective, providing a systematic taxonomy of guarded architectures for safety-critical AI systems. Their work is directly relevant to my research as **strong supporting evidence for the binary governance gap**: even their most sophisticated architecture (Architecture 8, with micro-ODD-specialised backup guards, diverse perception, and defense in depth) implements only binary permit/override control at each guard layer. The nuclear power analogy — where a limitation system sits between operational control and emergency shutdown — implicitly recognises the value of an intermediate governance mode, but this is not formalised as state-conditioned restriction on AI advisory scope. This paper serves three roles in my literature review: (a) as a **major reference confirming that binary governance is the state of the art** even in the most rigorous dependability-focused work, (b) as **architectural background** establishing the defense-in-depth principle that the DSR architecture extends with graduated governance, and (c) as **gap evidence** showing that no existing dependability architecture implements the two-level governance pair (G(S), A_AI(S)) with a CAUTION mode where AI participates under restricted recommendation scope. The paper's observation that internal guardrails are unassurable because they lack independence and diversity further motivates the DSR architecture's approach of implementing governance through an external, deterministic gate function.

---

## 17. Overall Relevance Score

### ⭐⭐⭐⭐ High

**Justification:** This paper directly addresses 5 of 8 core research themes (safety-critical AI, governance, hybrid AI, human role, socio-technical) and partially addresses 2 more (low-resource, formalisation). It provides the most comprehensive dependability-perspective treatment of guarded AI architectures, making it a **major baseline** for the DSR architecture's contribution claim. However, it does not implement Level 2 governance, does not define a formal safety property comparable to the Safety Dominance Property, and does not address the fisheries/maritime domain or low-resource deployment — so it falls short of ⭐⭐⭐⭐⭐ which is reserved for papers that directly address the two-level governance gap or implement the closest prior art (such as AgentSpec or Shields for Safe RL).

**Role in literature review:** Gap evidence + architectural background + baseline comparator for binary governance paradigm.
