## Literature Review Extraction

---

### 1. Paper Identity

- **Title:** Toward a hybrid approach for the risk analysis of maritime autonomous surface ships: a systematic review
- **Authors:** Tomohiro Yuzui, Fujio Kaneko
- **Year:** 2025 (published online January 2025)
- **Venue:** *Journal of Marine Science and Technology*, 30, pp. 153–176 (Springer)
- **DOI:** 10.1007/s00773-024-01040-0
- **Type:** Systematic literature review (PRISMA-based, 47 papers on MASS risk analysis, 2018–2023)

---

### 2. Core Contribution

- **Problem:** No comprehensive, systematic literature review of MASS risk analysis methods has been previously conducted. Existing reviews are outdated, mix MASS with conventional vessels, or treat risk analysis only as one component of a broader review. A suitable comprehensive risk analysis method for MASS has not been established.
- **Solution/Finding:** PRISMA-based systematic review of 47 papers on MASS risk analysis, classified using a novel six-theme framework (analysis types, tools, indexes, risk types, MASS types, target accidents). Key conclusion: a **hybrid approach combining qualitative STAMP/STPA analysis with quantitative Bayesian Network (BN) modelling** is the most promising method for MASS risk assessment. STAMP/STPA is the most frequently used tool overall (especially for qualitative hazard identification), and BN is the most frequently used for quantitative analysis. Three papers already combine STAMP/STPA with BN.
- **Main contributions:**
  1. First PRISMA-based systematic review focused exclusively on MASS risk analysis
  2. Novel six-theme classification framework for MASS risk analysis literature
  3. Evidence-based recommendation for STAMP/STPA + BN hybrid approach
  4. Identification of research gaps: few studies on non-collision accidents, cybersecurity risks, automation-level-differentiated risk analysis, and ship insurance applications
- **Novelty:** The classification framework covering six themes (analysis types, tools, indexes, risk types, MASS types, accidents) is broader than prior reviews that classified only by risk analysis tools.

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | Yes | Core recommendation: hybrid approach combining qualitative/rule-based STAMP/STPA with quantitative/probabilistic BN for MASS risk analysis. This parallels the DSR architecture's combination of deterministic rule-based safety governance with probabilistic AI reasoning — though at the risk analysis methodology level rather than the system architecture level. |
| Safety-critical AI decision-making | Yes | Entire paper focuses on safety-critical risk analysis for maritime autonomous surface ships, a safety-critical domain. Reviews 47 studies on MASS safety risk assessment. |
| AI governance / control mechanisms | Partial | STAMP/STPA inherently models control structures and unsafe control actions — a systems-theoretic approach to governance. Several reviewed papers (e.g., Utne et al. 2020, Johansen & Utne 2022, Johansen et al. 2023) explicitly address supervisory risk control of autonomous ships. However, the review does not analyse governance architectures with state-conditioned AI behaviour control. |
| Low-resource environments | No | Not addressed; MASS context assumes well-instrumented vessels with sensor suites, communication links, and remote control centres. |
| Decision architecture formalisation | No | No formal decision architecture model is defined. The review classifies risk analysis tools and methods but does not formalise decision pipelines, gate functions, or action spaces. |
| Human role in decision-making | Partial | Human factors explicitly noted as important for MASS safety but deliberately excluded from the review scope (deferred to Veitch & Andreas Alsos 2022). The classification of MASS types (automated vs. remotely controlled) implicitly addresses human role variation. |
| Socio-technical evaluation | No | Not addressed; focus is on technical risk analysis methods, not socio-technical evaluation. |
| Coastal fisheries / maritime domain | Yes | Directly in the maritime domain — maritime autonomous surface ships. While not coastal fisheries specifically, the maritime safety context, IMO regulatory framework, and classification society guidelines are directly relevant to the DSR research's maritime application domain. |

**Mid-Extraction Relevance Gate:** 3 Yes + 2 Partial = **FULL EXTRACTION**

---

### 4. Decision Architecture Analysis

- **No decision architecture is proposed by this review paper.** The paper reviews risk analysis *methods* (STAMP/STPA, BN, FT, ET, FMEA) applied to MASS, not decision architectures governing how MASS systems make operational decisions.
- **STAMP/STPA as a control structure model:** STAMP/STPA, the most frequently used tool in the reviewed literature, inherently models hierarchical control structures with control actions, feedback, and unsafe control actions (UCAs). This is a systems-theoretic framework for identifying hazardous interactions between system components — structurally analogous to modelling governance hierarchies. However, it is used here for *hazard identification* (design-time analysis), not for *runtime decision governance*.
- **BN for quantitative modelling:** Bayesian Networks are used to quantify risk by modelling causal relationships between risk factors, failure probabilities, and accident outcomes. BNs can represent conditional dependencies and update probabilities based on evidence — potentially useful for runtime state estimation, though the reviewed literature uses them primarily for design-time risk quantification.
- **Hybrid STAMP/STPA + BN:** The recommended hybrid approach uses STAMP/STPA to identify hazards and model control structures qualitatively, then converts these results into BN for quantitative risk assessment. This is a sequential pipeline (qualitative identification → quantitative modelling) rather than a runtime hybrid architecture.
- **Relevant reviewed papers with architectural implications:**
  - Utne et al. (2020) — "Towards supervisory risk control of autonomous ships" — proposes STAMP/STPA + BN combination for supervisory risk control
  - Johansen & Utne (2022) — "Supervisory risk control of autonomous surface ships" — develops and tests a risk-based control system
  - Johansen et al. (2023) — "Development and testing of a risk-based control system for autonomous ships" — implements and tests a risk-based control system using STAMP/STPA + BN
  - These papers, cited in the review, may be closer to runtime governance architectures and could warrant individual extraction.

---

### 5. Formal Model and Mathematical Representation

- **No formal model is defined in this review paper.** The paper classifies and compares risk analysis methods used in the literature but does not propose its own formal model.
- **BN as probabilistic formal model:** Several reviewed papers use BNs as formal probabilistic models for MASS risk, computing accident probabilities, failure rates, and risk values. BNs provide a formal framework for conditional probability reasoning — but as used in the reviewed literature, they model risk at the design/assessment level, not runtime decision governance.
- **Comparison to DSR pipeline:** No analogue to E → S = f(E) → (G(S), A_AI(S)) → AI(E). The STAMP/STPA + BN hybrid pipeline operates at the risk analysis level: hazard identification → causal modelling → risk quantification. It does not define safety state classification, gate functions, or admissible action spaces.
- **No state-dependent recommendation restriction.** None of the 47 reviewed papers (as described in this review) implements a mechanism where the set of permitted AI outputs varies by classified safety state.
- **No Safety Dominance Property or equivalent.**
- **Potential bridge:** The STAMP/STPA control structure modelling + BN probabilistic quantification could potentially *inform* the design of a state-conditioned governance architecture (e.g., using BN for safety state classification, STAMP/STPA for identifying unsafe control actions under different states), but this bridge is not made in the reviewed literature.

---

### 6. Safety State Classification

- **No operational safety state classification is described in this review.** The review classifies risk analysis methods and their outputs (risk values, accident probabilities, failure rates) but does not discuss systems that classify operational conditions into discrete safety states.
- The classification of MASS types into "automated" vs. "remotely controlled" represents a static autonomy classification, not a runtime safety state classification.
- **Risk levels in reviewed literature:** Some reviewed papers use semi-quantitative risk matrices (logarithmic scale), which implicitly classify risk into levels — but these are used for design-time risk assessment, not for runtime system behaviour governance.
- **No CAUTION mode analogue.** None of the reviewed work (as described in this review) implements a graduated governance mechanism where AI participates under restricted scope in intermediate risk states.

---

### 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (equivalent to G(S)) | Partial | STAMP/STPA models control structures that include conditions under which autonomous control may be unsafe — implicitly identifying when AI should not participate. Several reviewed papers (Utne et al. 2020, Johansen & Utne 2022) propose supervisory risk control that could gate AI participation. But this is not formalised as G(S) in the review. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (equivalent to A_AI(S)) | No | Not addressed. No reviewed paper (as described here) restricts the *type* of AI output based on classified safety state. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | No | Not implemented. |

- **Governance type:** The reviewed literature primarily addresses risk analysis for design-time safety assessment, not runtime AI governance. The most architecturally relevant papers (Utne et al. 2020, Johansen & Utne 2022, Johansen et al. 2023) move toward supervisory risk control but are not analysed in depth for governance level structure.
- **Key insight for DSR positioning:** The STAMP/STPA + BN hybrid approach is recommended for MASS *risk analysis* (design-time), but the gap between risk analysis methodology and runtime governance architecture is not bridged. The DSR architecture operates at the runtime level — using environmental state classification to govern AI participation and advisory scope in real-time — which is a different application of the hybrid principle than what this review covers.

---

### 8. Human Role in Decision-Making

- **Explicitly excluded from review scope.** The paper notes that human factors are important for MASS safety but deliberately defers to Veitch & Andreas Alsos (2022) for systematic review of human–AI interaction in MASS.
- **Implicit human role through MASS type classification:** The distinction between automated (no onboard crew) and remotely controlled (shore-based operators) ships implies different human roles. 43% of reviewed studies target automated ships, 36% target remotely controlled ships.
- The review notes that "risk analysis studies that consider the different levels of automation may be required because the MASS risk value as well as hazard appears to depend on the level of automation, malfunctions when communicating with the remote control centre (RCC), and human intervention" — acknowledging that human role variation affects risk but not analysing it in depth.

---

### 9. System Constraints and Environment

- **Maritime operational constraints acknowledged but not analysed in depth.** MASS operate in open, dynamic environments with communication dependencies (ship-to-shore for remote control), sensor uncertainties, weather effects, and interaction with other vessels.
- The review identifies that 62% of studies target collision as the primary accident type, with limited research on other accidents (grounding, fire/explosion, capsizing).
- **No resource-constraint analysis.** The review does not examine whether risk analysis methods are suitable for resource-limited deployment contexts. MASS are assumed to be well-instrumented systems with sensor suites, navigation systems, and communication links.

---

### 10. Hybrid AI Taxonomy

- **Type of hybrid approach:** The recommended STAMP/STPA + BN combination is a **sequential qualitative-to-quantitative pipeline** — qualitative hazard identification (STAMP/STPA) feeds into quantitative risk modelling (BN). This is not a runtime hybrid AI architecture but a risk analysis methodology.
- **Taxonomy mapping:**
  - Not neuro-symbolic (no learning + logic verification)
  - Not supervisory control (no rule-based supervisor monitoring AI output)
  - Closest to a **Rule-ML pipeline** — rule-based/structured analysis (STAMP/STPA) feeds probabilistic modelling (BN)
  - Could also be classified as a **stage-gate** approach — qualitative analysis gates what enters quantitative modelling
- **Safety enforcement position:** Safety reasoning is applied *during risk analysis* (design-time) rather than at runtime. STAMP/STPA identifies unsafe control actions before system deployment; BN quantifies their probabilities.
- **Does not support two-level governance.** The hybrid approach supports risk identification and quantification, not runtime AI participation or advisory scope governance.
- **Comparison to DSR:** The DSR architecture uses a deterministic-gate-first design where rule-based safety state classification (analogous to STAMP/STPA's structured analysis) controls when and what probabilistic AI may recommend. The Yuzui & Kaneko hybrid operates at a different level — risk analysis methodology vs. runtime decision architecture — but shares the principle that deterministic/structured methods should complement probabilistic methods.

---

### 11. Baseline Comparison and Evaluation

- **No baseline comparison is conducted** — this is a literature review, not a system evaluation.
- The review compares risk analysis tools by frequency of use (STAMP/STPA most frequent, then BN) and argues for superiority based on usage counts and methodological advantages.
- **BN advantages cited:** Ability to model complex systems, make predictions and diagnoses, calculate event probabilities, update calculations based on evidence, represent multimodal variables, and support user-friendly graphical modelling.
- **STAMP/STPA advantages cited:** Can analyse both inappropriate interactions among components and single component failures (unlike FMEA which targets only single component failures), making it suitable for complex MASS systems.
- **No evaluation of CAUTION-zone behaviour, Safety Dominance Property, or graduated vs. binary governance.** These concepts are outside the review's scope.

---

### 12. Key Concepts and Definitions

- **MASS (Maritime Autonomous Surface Ships):** Categorised by autonomy level into automated (no onboard crew) and remotely controlled (shore-based operators) ships. No globally agreed-upon definition of autonomy levels; more than six international authorities (IMO, LR, DNV-GL, BV, ClassNK, ABS) have published different classifications.
- **Risk analysis types (UK-HSE classification):** Qualitative (hazard identification), semi-quantitative (risk on logarithmic scale), quantitative (numerical risk measurement). The reviewed literature is roughly evenly split: 38% qualitative, 23% semi-quantitative, 38% quantitative.
- **STAMP/STPA (Systems-Theoretic Accident Model and Processes / System-Theoretic Process Analysis):** Systems-theoretic approach modelling hierarchical control structures and identifying unsafe control actions (UCAs). Most frequently used tool across all risk analysis types.
- **BN (Bayesian Network):** Probabilistic graphical model for quantifying causal relationships and computing conditional probabilities. Most frequently used tool for quantitative MASS risk analysis. Advantages over FT/ET: can model complex systems, make predictions and diagnoses, update based on evidence.
- **FSA (Formal Safety Assessment):** IMO's established rule-making tool for maritime safety. Comprises five steps: HAZID, risk analysis, risk control options, cost-benefit analysis, and recommendations. The weak link between qualitative and quantitative steps in FSA motivates the STAMP/STPA + BN combination.
- **Hybrid STAMP/STPA + BN approach:** Qualitative hazard identification using STAMP/STPA → conversion of results into BN for quantitative risk assessment. Proposed by Utne et al. (2020) and Johansen & Utne (2022).

---

### 13. Limitations and Unsolved Problems

- **Stated limitations:**
  1. Search limited to Scopus and ScienceDirect; may not cover all relevant studies
  2. Manual classification of papers into six themes may introduce bias
  3. "Superiority" of tools defined by usage frequency, which may not capture all quality dimensions (usability, rigour, flexibility, cost)
  4. Search period limited to 2018–2023
  5. Human factors explicitly excluded from scope

- **Identified research gaps (RQ4):**
  1. **Accident type coverage:** Few studies on non-collision accidents (grounding, fire/explosion, capsizing) — only 38% of studies address these
  2. **Cybersecurity:** Only 9% of studies target cybersecurity risk alone; further integration of safety and cybersecurity risk analysis needed
  3. **Automation-level differentiation:** Risk analyses need to explicitly consider different levels of autonomy, as hazards and risk values vary by automation level
  4. **Ship insurance:** Risk analysis for MASS insurance premium setting using BN (following AV precedent by Sheehan et al. 2017) — a practical application gap
  5. **Weak link between qualitative and quantitative analysis** in maritime risk assessment (noted by Kontovas & Psaraftis 2009, Psaraftis 2012) — the STAMP/STPA + BN combination addresses this

- **Alignment with DSR research gaps:**
  - The review **does not identify** the absence of runtime state-conditioned governance as a gap — its focus is on risk analysis methodology, not system architecture governance
  - The identified gap of **automation-level-differentiated risk analysis** resonates with the DSR architecture's state-conditioned governance — different autonomy/safety levels requiring different system behaviours — but the review frames this as a risk analysis gap, not a runtime governance gap
  - The **hybrid STAMP/STPA + BN recommendation** shares the DSR architecture's principle that deterministic/structured safety reasoning should complement probabilistic reasoning — supporting the broader motivation for hybrid architectures in the maritime domain
  - The paper provides **strong domain evidence** that the maritime autonomous shipping field recognises the need for hybrid qualitative-quantitative approaches, with STAMP/STPA (systems-theoretic, hierarchical control structures) and BN (probabilistic reasoning) as the most suitable tools — aligning with the DSR architecture's combination of deterministic governance and probabilistic AI

---

### 14. Methodology Notes

- **Research method:** PRISMA-based systematic literature review with a novel six-theme classification framework
- **Search:** Scopus and ScienceDirect, January 2018 to March 2023, English language, comprehensive keyword protocol covering risk analysis tools and MASS terminology
- **Flow:** 795 identified → 107 screened → 47 included after full-text eligibility assessment
- **Classification framework:** Six themes — analysis types (qualitative/semi-quantitative/quantitative), tools (FMEA, STAMP/STPA, ET, FT, BN, others), indexes (risk, accident probability, failure rate), risk types (safety, cybersecurity, both), MASS types (automated, remote, both, unknown), target accidents (collision, other navigational, system malfunction, other)
- **DSR methodology alignment:** The systematic review methodology is well-established and could inform the DSR research's own literature review methodology. The six-theme classification framework demonstrates how to structure a comprehensive review covering multiple dimensions of a topic.

---

### 15. Quotable / Citable Points

1. **Hybrid approach recommendation (Section 3.3/4):** The paper concludes that combining qualitative STAMP/STPA with quantitative BN is the most promising approach for MASS risk assessment — directly relevant to the DSR hybrid architecture motivation in the maritime domain.

2. **STAMP/STPA dominance (Section 3.1):** STAMP/STPA is the most frequently used tool across all risk analysis types for MASS, used in the majority of qualitative studies and combined with BN in quantitative studies.

3. **Weak qualitative-quantitative link (Section 3.3):** The paper cites Kontovas & Psaraftis (2009) and Psaraftis (2012) on the historically weak link between qualitative and quantitative analysis in maritime risk assessment — the STAMP/STPA + BN combination addresses this gap.

4. **Automation-level differentiation gap (Section 3.4):** The review identifies that risk analysis studies need to explicitly consider different levels of automation because MASS risk values and hazards depend on the level of automation — directly relevant to the DSR architecture's state-conditioned governance.

5. **Research trajectory (Section 3.1, Fig. 4):** The main objective of MASS risk analysis is shifting from qualitative hazard identification (2018–2020) to quantitative risk value estimation (2021–2022) — indicating maturation of the field.

---

### 16. Relation to My Research and Positioning

- **Governance level:** The review does not implement or analyse runtime governance levels. It reviews risk analysis methodology (design-time) rather than runtime decision governance. The most architecturally relevant reviewed papers (Utne et al. 2020, Johansen & Utne 2022, Johansen et al. 2023) are cited but not analysed for governance structure.
- **No state-conditioned governance.** No reviewed paper (as described in this review) varies AI behaviour or recommendation scope based on classified environmental safety state.
- **Gap relative to DSR:** The review demonstrates that the maritime autonomous shipping domain has converged on hybrid approaches (STAMP/STPA + BN) for risk analysis — validating the hybrid principle — but has not extended this to runtime governance architectures that classify environmental safety state and condition AI participation and advisory scope accordingly. The DSR architecture occupies this gap: it applies the hybrid principle (deterministic safety governance + probabilistic AI) at the runtime decision-making level rather than the design-time risk analysis level.
- **No Safety Dominance Property equivalent.**

- **Positioning paragraph:** This paper serves as a **core domain reference** for the DSR literature review. It is the most comprehensive systematic review of risk analysis methods for maritime autonomous surface ships, published in a reputable maritime engineering journal (JMST/Springer). Its principal finding — that hybrid STAMP/STPA + BN approaches are the most suitable for MASS risk analysis — validates the broader hybrid principle (deterministic/structured safety reasoning + probabilistic/quantitative reasoning) that the DSR architecture implements at the runtime governance level. The paper can be cited in multiple places: (1) in the **maritime domain background** to establish the state of risk analysis for MASS, (2) in the **hybrid AI motivation** to show domain-level convergence on hybrid approaches, and (3) in the **research gap section** to demonstrate that existing MASS risk analysis remains at the design-time assessment level without extending to runtime state-conditioned governance of AI behaviour. The identified gap that automation-level-differentiated risk analysis is needed — because hazards and risk values vary by autonomy level — directly supports the DSR architecture's core principle that AI governance should vary by classified safety state. The three papers on STAMP/STPA + BN combination for supervisory risk control (Utne et al. 2020, Johansen & Utne 2022, Johansen et al. 2023) may warrant individual extraction as the closest prior art to runtime governance in the maritime domain.

---

### 17. Overall Relevance Score

**⭐⭐⭐ Medium**

**Justification:** This is a comprehensive, well-structured systematic review in the maritime domain — directly relevant as a domain reference for the DSR research. It validates the hybrid approach principle (STAMP/STPA + BN) for maritime autonomous systems and identifies research gaps that align with the DSR architecture's contribution. However, it operates entirely at the risk analysis methodology level (design-time) rather than the runtime governance architecture level that is the DSR research's core contribution. It does not address state classification, gate functions, admissible action spaces, or any mechanism comparable to the two-level governance pair. It also does not address low-resource environments or coastal fisheries specifically. Its primary value is as a domain background reference and evidence that the maritime MASS community has converged on hybrid approaches without extending them to runtime governance — strengthening the gap claim.

**Recommended citation uses:**
- **Maritime domain background:** The state of risk analysis for MASS — STAMP/STPA + BN as the dominant hybrid approach (Section 3.3)
- **Hybrid AI motivation (maritime domain):** Domain-level evidence that hybrid deterministic + probabilistic approaches are the recommended paradigm for maritime autonomous systems
- **Research gap section:** Evidence that MASS risk analysis remains at the design-time assessment level; the gap between risk analysis methodology and runtime governance architecture is not bridged
- **Automation-level differentiation gap:** The review's identified need for automation-level-differentiated risk analysis supports the DSR architecture's state-conditioned governance principle
- **Pointer to key individual papers:** Utne et al. (2020), Johansen & Utne (2022), and Johansen et al. (2023) are identified as the closest prior art to runtime supervisory risk control for MASS — may warrant individual extraction
