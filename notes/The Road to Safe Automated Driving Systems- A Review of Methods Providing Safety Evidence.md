## Literature Review Extraction
### Gyllenhammar, Rodrigues de Campos & Törngren (2025) — The Road to Safe Automated Driving Systems: A Review of Methods Providing Safety Evidence

---

### 1. Paper Identity
- **Title:** The Road to Safe Automated Driving Systems: A Review of Methods Providing Safety Evidence
- **Authors:** Magnus Gyllenhammar, Gabriel Rodrigues de Campos, Martin Törngren
- **Year:** 2025 (published 30 January 2025; current version 31 March 2025)
- **Venue:** IEEE Transactions on Intelligent Transportation Systems, Vol. 26, No. 4, pp. 4315–4345
- **DOI:** 10.1109/TITS.2025.3532684
- **Type:** Comprehensive literature review with challenge classification and gap analysis

---

### 2. Core Contribution
- **Problem:** Existing safety assurance methods (design, V&V, runtime) are insufficient to cope with the complexity, operational uncertainty, and high-dependability requirements of Automated Driving Systems (ADSs, SAE Level 3–5). No holistic analysis exists of how different methods contribute to safety evidence across the full lifecycle.
- **Solution:** A structured review of methods for providing safety evidence, organised into four categories — design techniques, verification & validation methods, runtime risk assessment, and runtime (self-)adaptation — evaluated against eight identified challenges.
- **Main contributions:**
  1. Identification of **eight challenges** for safety evidence provision for ADSs (grouped into: operational uncertainties, behavioural/structural complexity, high-dependability requirements, AI/ML components, agile development)
  2. A **state-of-the-art review** of existing methods classified against these eight challenges (TABLE VI)
  3. **Five categories of research gaps** derived from the challenge classification
- **What is novel:** The holistic, lifecycle-spanning perspective — no prior work analyses the full landscape of safety evidence methods for ADSs across design-time and runtime, mapped against a common set of challenges. The challenge classification framework (TABLE VI) and systematic gap derivation methodology are original contributions.

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | **Yes** | Supervisor architectures (Sec. IV-E) implement a nominal channel (may use ML) monitored by a safety/supervisory channel (high-integrity, rule-based), with a decision module switching between them — a structural hybrid |
| Safety-critical AI decision-making | **Yes** | Core topic — the entire paper concerns safety evidence for autonomous systems making safety-critical decisions in open, uncertain environments |
| AI governance / control mechanisms | **Yes** | Covers ODD-based confinement, supervisor architectures with binary switching, contract-based design (assume/guarantee), runtime certification (ConSerts), degradation strategies (MRC/ROD), Dynamic Safety Management, and precautionary safety policies |
| Low-resource environments | **Partial** | Mentions limited computational resources and bandwidth as constraints for operational data collection (Sec. VI-A); discusses cost-effectiveness of architectural redundancy; but low-resource deployment is not a primary concern |
| Decision architecture formalisation | **Partial** | Reviews formal methods (theorem proving, reachability analysis, model checking), contract-based design formalisation, and formal rules for driving behaviour (RSS, Safety Force Field); discusses action space restriction (Fig. 10); but does not itself propose a new formal architecture model |
| Human role in decision-making | **Partial** | Explicitly delimits human-machine interaction as out of scope (Sec. II-B), but notes the shift of tactical responsibility from human to ADS as a core challenge (C-B-resp); discusses automation complacency and safety operator limitations |
| Socio-technical evaluation | No | Not addressed — the review focuses on technical methods, not socio-technical evaluation |
| Coastal fisheries / maritime domain | No | Exclusively automotive/ADS domain |

**Mid-Extraction Relevance Gate:** 3 Yes + 3 Partial → **FULL EXTRACTION**

---

### 4. Decision Architecture Analysis
- **Structure:** The paper reviews multiple architectural paradigms rather than proposing one. The dominant pattern is a **supervisory/simplex architecture** (Fig. 8): a nominal/complex channel runs in parallel with a supervisory/safety channel, with a monitor and decision module governing channel switching.
- **Layered architecture:** The review identifies a clear design-time / runtime partition:
  - **Design-time:** ODD specification → HARA → FSC/TSC → architecture → V&V (V-model, Fig. 6)
  - **Runtime:** Risk assessment (operational data, threat assessment, OoD detection, DRA) → Self-adaptation (degradation strategies, runtime certification, DSM, precautionary safety)
- **Safety constraint mechanisms:**
  - **ODD confinement** — limits the operational scope before deployment
  - **Supervisor architectures** — binary switching between nominal and safety channels based on monitor output
  - **Contract-based design** — assume/guarantee contracts checked at compilation, configuration, or execution time
  - **Runtime certification (ConSerts)** — runtime evaluation of conditional safety certificates determining valid system configurations
  - **Degradation strategies** — MRC (Minimal Risk Condition) as fail-safe, ROD (Restricted Operational Domain) as intermediate degradation
- **Boundary between deterministic control and AI reasoning:** Defined architecturally through the simplex pattern — the nominal channel may include ML-based components; the safety channel is high-integrity, deterministic. The decision module/monitor sits at the boundary.
- **Failure modes and fallback:** Explicitly treated through three fault tolerance regimes (fail-operational, fail-degraded, fail-safe; Stolte et al.) and the MRC/ROD hierarchy (Fig. 11): ODD → ROD → MRC, with the MRC representing the ultimate fallback.

---

### 5. Formal Model and Mathematical Representation
- **Formal models reviewed (not proposed):**
  - **Risk definition:** R(x) = P(x) · S(x) — probability × severity
  - **Contract-based design:** Assume/Guarantee (A/G) contracts formalised per Benveniste et al. [92]; preconditions and postconditions for system elements
  - **Action space restriction (Fig. 10):** The permissible action space is IL ∩ P̄U — the reachable set limited by internal capabilities (IL) intersected with the complement of the uncertainty-extended obstacle occupancy (PU). This is the closest construct to a formal action space restriction.
  - **Formal rules for driving behaviour:** RSS, Safety Force Field, rulebooks — formal specifications of safe driving behaviour
  - **Scenario space (Fig. 9):** A (applicable scenarios) ∩ G (generated scenarios) ∩ C (safety-critical scenarios) — completeness requires C ∩ A ∩ Ḡ = ∅
  - **ConSerts:** Conditional safety certificates with demands/supplies evaluated at runtime

- **Comparison to DSR pipeline E → S = f(E) → (G(S), A_AI(S)) → AI(E):**
  - **No equivalent pipeline exists** in any reviewed method. The closest structural analogy is the MRC/ROD decision hierarchy (Fig. 11): ODD → ROD → MRC, which sequences from broader to narrower operational scope. However, this is triggered by **system degradation** (internal faults, capability loss), not by **environmental safety state classification** as in my f(E).
  - The **action space restriction** (Fig. 10) is structurally analogous to A_AI(S) — it defines what the ADS may do given its current situation — but it is a **continuous, physics-based** restriction (reachable set minus obstacle occupancy), not a **discrete, state-conditioned** restriction on recommendation types.
  - The **supervisor architecture** switching implements a binary gate (nominal or safety channel), analogous to G(S) at Level 1, but without Level 2 graduated advisory scope restriction.

- **State-dependent recommendation restriction:** The ROD concept restricts the operational domain (and implicitly what the system may attempt), and the DRA/DSM framework adapts behaviour to current risk. However, **none of these implement a discrete, classified safety state that restricts the set of permitted AI output types** (analogous to A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅).

- **Safety Dominance Property equivalent:** No formal property comparable to AI(E) ⊆ A_AI(S) is defined. The closest is the contract-based design guarantee that outputs satisfy postconditions given preconditions hold, but this is per-component, not a global safety dominance property across classified states.

- **Formalisation purpose:** The formal constructs reviewed are used for **verification, specification, and runtime monitoring** — not for expressing graduated governance.

---

### 6. Safety State Classification
- **Operational space partitioning:** The paper references Machin et al. [111] who partition the operational space into **safe, warning, and catastrophic states** (Sec. VI, p. 4330). This is the closest to a tripartite classification.
- **ODD-based classification:** The ODD defines a binary boundary — inside ODD (nominal) vs. outside ODD (requires transition to MRC). The ROD adds an intermediate zone for degraded operation.
- **Integrity levels:** Feth et al. [183] perform DRA using three parallel components corresponding to low, mid, and high integrity levels (Sec. VI-D).
- **Monitoring purposes (Sec. VI):** Three types of runtime monitoring are distinguished:
  - (i) Safe tactical decisions despite errors or unexpected environmental changes (within ODD)
  - (ii) Coping with more permanent system degradations
  - (iii) Avoiding ODD exit

- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:**
  - The safe/warning/catastrophic partition [111] is structurally similar but is used for **monitoring and state identification**, not for governing AI recommendation scope.
  - The **ODD/ROD/MRC hierarchy** (Fig. 11) provides three operational levels but is triggered by **system degradation**, not environmental state classification.
  - **No reviewed paper classifies environmental conditions into discrete safety states that then determine what types of recommendations AI may produce.** The environmental state drives risk assessment (DRA) and behaviour adaptation (DSM), but through continuous risk metrics, not through a classified state that gates a discrete set of permitted output types.

- **Critical assessment:** The paper does NOT identify any method that differentiates AI recommendation scope across safety levels. Governance is always binary (AI on/off, nominal/safety channel) or continuous (risk-adapted behaviour). The CAUTION mode — where AI participates but with restricted output types — has no precedent in the reviewed automotive literature.

---

### 7. Governance Level Analysis

| Level | Question | Does this paper identify it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (G(S)) | **Yes** | Supervisor architectures implement binary switching: nominal channel (with ML) vs. safety channel. The monitor/decision module acts as a gate. ODD confinement determines whether the system operates at all. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | **Partial** | The action space restriction concept (Fig. 10) constrains what the ADS may do based on capabilities and uncertainties. DRA/DSM adapts behaviour to risk. RODs restrict operational scope. But these are **continuous, per-situation** restrictions — not state-conditioned output-type filtering. |
| **Levels 1 + 2 unified, state-conditioned** | Both governed by classified environmental state? | **No** | No reviewed method implements both levels unified under a classified environmental safety state. |

- **Governance model:** The automotive domain as reviewed here implements **Level 1 (binary) governance** through supervisor architectures and ODD confinement. Level 2 exists in continuous form (DRA restricts action space) but is not formalised as a discrete, state-conditioned governance mechanism.
- **Binary AI switch vs. graduated governance:** The dominant paradigm is a **binary switch** — either the nominal channel operates or control is handed to the safety channel. The ROD/MRC hierarchy introduces gradation, but this is a **degradation response** (triggered by system faults), not a **governance mechanism** over AI advisory scope conditioned on environmental state.
- **Support for two-level governance pair:** The paper **implicitly supports the motivation** for my two-level governance pair by demonstrating that:
  1. Existing methods implement Level 1 (participation) governance extensively but treat Level 2 only through continuous risk-adapted behaviour
  2. The gap between binary switching and continuous risk adaptation is not bridged by any formal mechanism governing discrete advisory scope
  3. The safe/warning/catastrophic state partition exists in monitoring but is not connected to governing what AI may recommend

---

### 8. Human Role in Decision-Making
- **Scope limitation:** Human-machine interaction is explicitly delimited as out of scope (Sec. II-B), including hand-over procedures, mode confusion, and automation complacency.
- **Decision responsibility:** The core challenge C-B-resp addresses the shift of complete Dynamic Driving Task (DDT) responsibility to the ADS — the system decides autonomously (SAE Level 3–5). This is **decision automation**, not decision support.
- **Human override:** Safety operators are mentioned in the context of FOTs, and the MRC can be triggered by the user or the system. But the architecture is not designed as a decision support system with human-in-the-loop.
- **Contrast with my research:** My architecture is a **decision support system** (human fisher decides); this paper reviews **decision automation** (ADS decides). The governance mechanisms are analogous but the final decision authority differs fundamentally.

---

### 9. System Constraints and Environment
- **Real-world constraints acknowledged:**
  - Limited computational resources for runtime evaluation (Sec. VI-A)
  - Limited transmission bandwidth requiring careful data curation (Sec. VI-A)
  - Cost-effectiveness constraints on architectural redundancy (triple modular redundancy deemed too expensive; Sec. IV-E)
  - Sim2Real transfer gap for validation (Sec. V-C)
  - "Billion miles problem" — infeasibility of collecting sufficient field data (Introduction)
- **Deployment context:** The methods reviewed span simulation, proving grounds, field operational tests, and commercial operations. The paper explicitly addresses the transition from testing to real-world deployment.
- **Resource-aware design:** Lightweight models or offline capability are not discussed — the automotive context assumes relatively high computational resources compared to my low-resource domain.

---

### 10. Hybrid AI Taxonomy
- **Hybrid approach:** The dominant pattern is **supervisory control** — a high-performance nominal channel (which may include ML-based components) monitored by a high-integrity safety channel (rule-based/deterministic), with a decision module switching between them (simplex architecture, Fig. 8).
- **Safety enforcement position:** Safety enforcement sits **alongside** AI reasoning (parallel channels) with a switching mechanism. The safety channel can override the nominal channel when the monitor detects issues.
- **Two-level governance support:** The hybrid approach supports **Level 1 governance** (binary switching between channels). It does **not** support Level 2 (state-conditioned advisory scope restriction). The switching is all-or-nothing: either the nominal channel operates fully or control passes entirely to the safety channel.
- **Comparison to my architecture:** My architecture places safety enforcement **before** AI reasoning (deterministic gate-first), with graduated governance over both participation and advisory scope. The automotive simplex pattern places safety enforcement **in parallel** with a binary switch. The structural difference is significant: my architecture gates and constrains AI output scope; the automotive architecture switches between entirely separate processing channels.

---

### 11. Baseline Comparison and Evaluation
- **Classification framework:** TABLE VI classifies 17 methods × 8 challenges using a six-level scale: S (solution), A (ameliorates), U (uncertain), N (neutral), O (obstacle), FC (fundamental challenge). This is a qualitative assessment by the authors.
- **No formal property verification:** The review does not identify any method that verifies a property comparable to the Safety Dominance Property. Contract-based design verifies assume/guarantee contracts, and formal methods verify specification compliance, but neither establishes a global guarantee that AI outputs always fall within state-determined bounds.
- **CAUTION zone testing:** No evaluated method tests behaviour specifically in a CAUTION zone with restricted advisory scope. The ROD concept restricts operational capability during degradation, but evaluation of ROD behaviour is noted as requiring explicit analysis of each subsystem's capabilities — a gap.
- **Graduated vs. binary governance comparison:** The paper does not compare graduated governance against binary governance. All methods reviewed implement binary governance (nominal/safety, inside/outside ODD). The gradation exists in degradation strategies (ROD as intermediate between full operation and MRC) but is not evaluated as a governance model.
- **Evaluation gaps:** The five categories of research gaps (Sec. IX-B) identify substantial gaps in: completeness of safety evidence, method improvement, closed-loop data collection, AI/ML component integration, and scalability.

---

### 12. Key Concepts and Definitions
- **Operational Design Domain (ODD):** Operating conditions under which the ADS is specifically designed to function — defines the design-time scope and runtime boundary
- **Minimal Risk Condition (MRC):** Stable stopped condition at acceptable risk — the fail-safe fallback when a trip cannot or should not be completed
- **Restricted Operational Domain (ROD):** Operational domain of the system after degradation — intermediate between full ODD and MRC; encodes what the degraded system can still safely do
- **Dynamic Risk Assessment (DRA):** Runtime assessment of operational risk based on situation awareness, connecting current situation to safety requirements via quantitative risk measurement
- **Dynamic Safety Management (DSM):** Runtime adaptation of system objectives and constraints based on safety awareness (contextual + self-awareness); circumvents the need for static worst-case design-time analysis
- **Precautionary Safety (PcS):** Driving policy derived to satisfy quantitative risk norms (QRN) by accounting for emergency response capabilities, perception performance, and exposure levels
- **ConSerts (Conditional Safety Certificates):** Runtime-evaluated contracts with demands/supplies; enable configuration-dependent safety assurance for adaptive systems
- **Simplex architecture:** Parallel nominal + safety channels with monitor and decision module switching between them
- **Fault tolerance regimes:** Fail-operational, fail-degraded, fail-safe (Stolte et al.)
- **Action space restriction:** Permissible action space = reachable set (limited by capabilities) ∩ complement of uncertainty-extended obstacle occupancy (Fig. 10)

---

### 13. Limitations and Unsolved Problems
- **Stated limitations:**
  - Non-systematic reference collection — references gathered through exploratory search and snowballing, not systematic literature search (acknowledged as threat to reproducibility)
  - Challenge classification (TABLE VI) is a qualitative assessment by the authors
  - Interconnections and dependencies between methods are not analysed
  - Human-machine interaction, cybersecurity, organisational complexity are out of scope
- **Unsolved problems / future work:**
  - How to combine methods to holistically address all eight challenges
  - Dependencies and relationships between methods
  - Extension to collaborative/connected systems and systems-of-systems
  - Analysis of assumptions, models, and uncertainties each method imposes/consumes/mitigates
  - Integration of assurance methodologies for argument/evidence traceability
- **Gaps aligning with my research problem:**
  - **Binary governance dominance:** All reviewed governance mechanisms are binary (nominal/safety channel switching, inside/outside ODD). No method implements graduated advisory scope governance.
  - **No two-level governance model:** Level 1 (participation) is well-established; Level 2 (advisory scope) exists only as continuous risk-adapted behaviour, not as a formal, discrete, state-conditioned mechanism.
  - **No CAUTION mode:** The ROD concept provides an intermediate operational state between full capability and MRC, but it is triggered by system degradation, not environmental state classification, and restricts operational scope rather than AI recommendation types.
  - **No Safety Dominance Property for graduated governance:** The reviewed formal methods verify specification compliance and contract fulfilment, but no method establishes a formal property guaranteeing that AI outputs always fall within bounds defined by a classified environmental safety state.
  - **Environmental state classification not connected to AI scope restriction:** The safe/warning/catastrophic partition exists for monitoring, and DRA provides continuous risk assessment, but neither is connected to a discrete mechanism governing what types of recommendations AI may produce.

---

### 14. Methodology Notes
- **Method:** Literature review with structured challenge classification and gap analysis. Not a traditional systematic literature review — uses exploratory search, snowballing, domain expertise, supplemented by a focused high-level systematic search for validation.
- **Process (Fig. 3):** (1) Literature survey → (2) Challenge identification → (3) Method identification → (4) Organisation into mind-map structure → (5) Method-challenge investigation → (6) Classification (TABLE VI) → (7) Gap analysis → (8) Research question formulation → (9) Focused systematic validation
- **DSR alignment:** The methodology does not follow DSR. However, the structured approach of identifying challenges, classifying methods against challenges, and deriving gaps provides a model for how to position a contribution (like my architecture) against existing methods.
- **Informing my work:** The challenge classification framework (TABLE VI) could inform how I position my architecture's contributions — specifically, my architecture addresses the gap between binary supervisor switching (Level 1) and continuous risk-adapted behaviour by introducing formal, discrete, state-conditioned Level 2 governance.

---

### 15. Quotable / Citable Points

1. **Binary switching as dominant paradigm (Sec. IV-E / Fig. 8):** The simplex architecture pattern — nominal channel monitored by safety channel with binary switching — is presented as the standard supervisory approach for ADSs, confirming Level 1 governance as the established norm.

2. **Operational space partitioning (Sec. VI, referencing Machin et al. [111]):** The partitioning of operational space into "safe, warning and catastrophic states" for monitoring purposes — while structurally similar to tripartite classification, this is used only for monitoring, not for governing AI output scope.

3. **Action space restriction concept (Sec. VI-D / Fig. 10):** The permissible action space of the ADS is restricted by capabilities and perception uncertainties, showing that action space restriction is recognised but implemented as continuous physics-based constraint, not discrete state-conditioned governance.

4. **MRC/ROD hierarchy as graduated degradation (Sec. VII-A / Fig. 11):** The decision hierarchy ODD → ROD → MRC demonstrates that graduated operational restriction exists in automotive domain, but is triggered by system degradation rather than environmental safety state.

5. **Research gap on formalisation of operational uncertainties (Sec. IX-B.1):** The paper asks how tactical responsibility and operational uncertainties could be formalised for contract-based design, formal methods, and runtime certification — directly motivating formal architectures that connect environmental state to governance mechanisms.

---

### 16. Relation to My Research and Positioning

- **Level 1 governance:** Extensively documented across supervisor architectures, ODD confinement, and runtime certification — all implementing binary AI participation control.
- **Level 2 governance:** Present only in continuous form — DRA restricts the action space based on dynamic risk assessment, and DSM adapts objectives/constraints. No discrete, state-conditioned output-type filtering is identified.
- **State-conditioned two-level pair:** Not implemented by any reviewed method. The closest — the ROD/MRC hierarchy — is triggered by system degradation and restricts operational scope, not AI advisory scope.
- **Safety Dominance Property:** No equivalent defined. Contract-based design provides per-component guarantees under assumptions; no global property bounds AI outputs within state-determined admissible spaces.
- **Gap my research addresses:** The automotive domain, as comprehensively surveyed here, implements Level 1 governance extensively and Level 2 only as continuous risk adaptation. The formal, discrete, state-conditioned two-level governance pair (G(S), A_AI(S)) — where a classified environmental safety state determines both whether AI participates and what it may recommend — fills this gap. Specifically, the CAUTION mode (G(S) = 1 but A_AI restricted) has no precedent in the automotive methods reviewed.

**Positioning paragraph:** This paper provides authoritative, comprehensive evidence that the automotive ADS domain — arguably the most mature safety-critical AI domain — relies on binary governance mechanisms (supervisor switching, ODD confinement) for Level 1 participation control, and continuous risk-adapted behaviour (DRA, DSM) for dynamic safety management, but has no formal mechanism connecting classified environmental state to discrete AI advisory scope restriction. The MRC/ROD hierarchy demonstrates that graduated operational restriction is recognised as necessary (rather than purely binary fail-safe), but this is triggered by system degradation and restricts what the system may operationally attempt, not what types of recommendations AI may produce. The paper's explicit identification of research gaps around formalising operational uncertainties and their connection to governance mechanisms directly motivates my two-level governance architecture. This paper serves as strong **background evidence for the binary governance gap** in the automotive domain, complementing Perez-Cerrolaza et al. (2024) for the broader cross-domain picture, and provides rich vocabulary and conceptual framing (action space restriction, operational state partitioning, graduated degradation) that I can cite when positioning my contribution.

---

### 17. Overall Relevance Score

**⭐⭐⭐ Medium — provides substantial background evidence and rich conceptual framing for the binary governance gap in the automotive domain**

**Justification:** The paper does not directly address the two-level governance gap or implement prior art comparable to my architecture (which would warrant ⭐⭐⭐⭐ or ⭐⭐⭐⭐⭐). However, it provides the most comprehensive single source documenting that the automotive domain — the most mature safety-critical AI domain — relies exclusively on binary governance (Level 1) and continuous risk adaptation, with no formal mechanism for state-conditioned advisory scope restriction (Level 2). This makes it valuable for: (a) documenting the binary governance paradigm in the automotive domain alongside Perez-Cerrolaza et al.'s cross-domain evidence; (b) citing specific architectural patterns (simplex, MRC/ROD) as prior art that my architecture extends; (c) leveraging its identified research gaps to position my contribution; and (d) borrowing conceptual vocabulary (action space restriction, graduated degradation, safety awareness) to frame my formalisation. The rating is ⭐⭐⭐ rather than ⭐⭐⭐⭐ because the paper is a review (not proposing a competing architecture), is automotive-specific (not my domain), and does not itself formalise any governance mechanism.
