## Literature Review Extraction
### Paper: AI in Healthcare for Resource Limited Settings: An Exploration and Ethical Evaluation

---

## Early Relevance Check: PASSED

1. **Core research themes?** Yes — low-resource environments, human role in decision-making, socio-technical evaluation
2. **Contributes to relevant areas?** Yes — low-resource AI deployment, ethical governance of AI in healthcare
3. **Citable in literature review?** Yes — background on ethical and deployment challenges for AI in low-resource, safety-relevant contexts

**→ Proceed with full extraction.**

---

### 1. Paper Identity

- **Title:** AI in Healthcare for Resource Limited Settings: An Exploration and Ethical Evaluation
- **Authors:** Rune Chi Zhao, Xiuyuan Yuan
- **Year:** 2025
- **Venue:** WWW Companion '25: Companion Proceedings of the ACM Web Conference 2025, Sydney, NSW, Australia (ACM)
- **DOI:** https://doi.org/10.1145/3701716.3717747
- **Type:** Narrative review (survey-natured), ethical evaluation

---

### 2. Core Contribution

- **Problem addressed:** AI healthcare applications have been developed and evaluated primarily in high-income settings. Significant gaps remain in understanding how to ethically and responsibly deploy AI in resource-limited settings (RLS), where infrastructure, data, regulatory frameworks, and human resources are constrained.
- **Proposed solution / key finding:** The paper provides a structured survey of AI healthcare applications in RLS across four categories (decision support, predictive analytics, telemedicine/digital health, resource management) and conducts an ethical evaluation across five dimensions (bias/fairness, non-maleficence, privacy/security, autonomy, transparency). It identifies under-discussed ethical dilemmas — including whether ethical boundaries should shift under extreme resource scarcity — and provides implementation recommendations including phased deployment, local stakeholder participation, and context-specific regulation.
- **Main contributions:**
  1. Taxonomy of AI healthcare applications relevant to RLS (decision support, predictive analytics, telemedicine, resource management)
  2. RLS-specific ethical evaluation across five ethical dimensions
  3. Identification of under-discussed ethical dilemmas (e.g., whether AI should assume decision authority in emergencies; whether AI investment is the best use of scarce resources)
  4. Recommendations for ethical implementation including gradual introduction, local stakeholder involvement, and safety-net mechanisms
- **Novelty:** The paper's distinctiveness lies in applying ethical evaluation specifically to the RLS context (rather than high-income settings) and in surfacing dilemmas rarely addressed in prior literature — particularly around whether ethical boundaries for human oversight should be relaxed in extreme resource scarcity.

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | No | Paper does not discuss hybrid AI architectures or the interaction between deterministic and probabilistic components. |
| Safety-critical AI decision-making | Partial | Healthcare is safety-critical; the paper discusses non-maleficence and harm risks from AI errors. However, it does not address safety-critical AI architecture or formal safety mechanisms. |
| AI governance / control mechanisms | Partial | Discusses ethical governance (human oversight requirements, regulatory frameworks, autonomy preservation) but does not address technical governance mechanisms such as gate functions or action-space restriction. |
| Low-resource environments | **Yes** | Core focus. Defines RLS characteristics (data scarcity, limited connectivity, workforce shortages, weak regulatory frameworks) and evaluates AI deployment challenges specific to these contexts. |
| Decision architecture formalisation | No | No formal model, mathematical representation, or decision architecture is presented. |
| Human role in decision-making | **Yes** | Extensively discusses human autonomy, shared decision-making, clinician role in interpreting AI outputs, and risks of AI overriding patient preferences. Notes that current regulations do not allow AI to be the final decision-maker. |
| Socio-technical evaluation | **Yes** | The entire ethical evaluation (Sections 4–5) constitutes a socio-technical evaluation of AI deployment in RLS, covering bias, fairness, autonomy, transparency, and community participation. |
| Coastal fisheries / maritime domain | No | Healthcare domain only; no maritime or fisheries context. |

**Mid-Extraction Relevance Gate:** 3 Yes → **FULL EXTRACTION**

---

### 4. Decision Architecture Analysis

- **Decision-making structure:** The paper does not describe a specific decision architecture. It surveys Clinical Decision Support Systems (CDSS) generically — these provide probability assessments and recommendations to clinicians who retain final decision authority.
- **Layered architecture / governance structure:** None formalised. The paper notes that CDSS are "primarily employed as screening tools and diagnostic or treatment aids" with human clinicians as final decision-makers, but this is described as a regulatory norm rather than an architectural feature.
- **Rule-based constraints before AI:** Not discussed at the architectural level. The paper references regulatory requirements (AI cannot be the final decision-maker) as external constraints, not as embedded safety mechanisms.
- **Boundary between deterministic control and AI reasoning:** Not defined. The paper operates at the policy/ethics level rather than the technical architecture level.
- **Failure modes / fallback behaviour:** The paper recommends that "in the case of systems malfunction or connectivity failure, there must be safety net mechanisms in place and healthcare professionals must be able to deliver care regardless of AI assistance" (Section 5). This is a recommendation, not a formalised fallback mechanism.

**Assessment:** This paper provides no technical decision architecture. Its contribution is at the ethical/policy level. The recommendation for safety-net mechanisms and the discussion of when AI should or should not operate autonomously are relevant as *motivational context* for why a formal gated architecture is needed, but the paper itself does not provide one.

---

### 5. Formal Model and Mathematical Representation

- **Formal model defined?** No. The paper contains no formal model, no mathematical representation, and no state variables.
- **Comparison to E → S = f(E) → (G(S), A_AI(S)) → AI(E):** Not applicable. The paper operates entirely at the qualitative/ethical level.
- **State-dependent recommendation restriction?** No. The paper does not model any variation in AI output scope across conditions.
- **Safety Dominance Property?** No formal safety property is defined.
- **Formalisation purpose:** N/A — no formalisation present.

**Assessment:** The absence of any formal model in this paper, despite its extensive discussion of when AI should and should not operate and what it should be allowed to do, is itself evidence of the gap my architecture addresses. The paper identifies the *need* for graduated control but does not formalise it.

---

### 6. Safety State Classification

- **Discrete risk/safety levels?** No explicit classification. However, the paper implicitly describes a spectrum of conditions: normal operations (AI as decision support), degraded conditions (limited connectivity, workforce shortages), and extreme scenarios (emergencies, severe resource scarcity where human oversight may be unavailable).
- **Thresholds or rules?** None defined.
- **Comparison to S ∈ {SAFE, CAUTION, UNSAFE}:** The paper's discussion of whether ethical boundaries should change in "drastic, resource-limited scenarios" (Section 4.6) implicitly maps onto a graduated safety model — normal → constrained → extreme — but this is framed as an ethical dilemma rather than a formal classification.
- **AI recommendation scope differentiation across levels?** No. The paper treats AI governance as binary: either human oversight is maintained (AI as decision support) or, in extreme scenarios, the question is raised whether AI should assume full decision authority. There is no intermediate mode where AI participates with restricted output scope.

**Assessment:** The paper's ethical dilemma about relaxing human oversight in extreme scarcity is a direct motivational case for the CAUTION mode — a formalised intermediate state would address this dilemma architecturally rather than leaving it to ad hoc ethical judgment.

---

### 7. Governance Level Analysis

| Level | Question | Implemented? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? | Partial | The paper notes regulations require human oversight; recommends safety-net mechanisms for when AI is unavailable. But this is policy-level, not an architectural gate function. |
| **Level 2 — Advisory scope governance** | What may AI recommend? | No | No discussion of restricting the *types* of AI recommendations based on conditions. AI output scope is treated as static. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | No | No state classification; no unified governance model. |

- **Binary switch vs. graduated governance?** The paper's implicit model is binary: AI operates under human supervision, or (in the ethical dilemma) AI potentially operates autonomously. No graduated model.
- **Level 2 state-conditioned or static?** N/A — Level 2 not implemented.
- **Support for two-level governance pair?** The paper *motivates* the need for such a model through its ethical dilemmas but does not propose or implement one. The unresolved question of "should ethical boundaries change in extreme scenarios" is precisely what a formal (G(S), A_AI(S)) pair would resolve architecturally.

---

### 8. Human Role in Decision-Making

- **Human involvement:** The paper strongly positions AI as decision *support*, not decision *automation*. Clinicians retain final authority: "Currently, most experts agree that such algorithms themselves are not reliable enough to act as the final decision-maker, which is reflected in global regulatory frameworks."
- **Decision support vs. automation:** Explicitly decision support. However, the paper raises the dilemma of whether this should change in extreme resource scarcity where clinicians are unavailable.
- **Human-AI interaction:** CDSS provide probability assessments, diagnostic suggestions, and treatment recommendations. Clinicians interpret outputs and communicate with patients.
- **Human override / escalation:** Not formalised. The paper recommends maintaining human capability to deliver care without AI assistance, but does not describe override mechanisms.

**Assessment:** The paper's strong emphasis on human decision authority and its dilemma about when that authority might be unavailable directly supports the design rationale for my architecture's human-in-the-loop model with formal fallback to deterministic safety defaults in UNSAFE states.

---

### 9. System Constraints and Environment

- **Real-world constraints addressed?** Yes — this is a core strength of the paper. It extensively catalogues RLS constraints:
  - **Data scarcity:** Fragmented health information systems, datasets sourced from high-income contexts with domain mismatch
  - **Limited compute/connectivity:** Implied through discussion of telemedicine barriers and system malfunction scenarios
  - **Workforce shortages:** Severe clinician-to-patient ratio imbalances (e.g., Nigeria's 380 critical care nurses vs. USA's 500,000+)
  - **Weak regulatory frameworks:** Inadequate data protection legislation, limited enforcement capacity
  - **Low digital/health literacy:** Patients and some clinicians lack familiarity with AI technologies
- **Real-world deployment vs. simulation:** The paper surveys real-world deployments (Peru TB diagnosis system, South Africa cholera prediction, China DoctorBot, Africa Gukiza cancer monitoring) and notes that most AI healthcare applications have been deployed and evaluated only in high-income countries.
- **Resource-aware design choices:** The paper recommends gradual/phased introduction, integration into existing workflows, and capacity-building — but these are implementation strategies, not architectural design choices.
- **Edge cases / resource-limited performance:** The paper highlights that AI systems may recommend treatments unavailable in RLS, and that connectivity failures require safety-net mechanisms.

**Assessment:** This section provides strong citable background for characterising the low-resource deployment environment. The constraints catalogued here (data scarcity, connectivity, workforce shortages, low literacy) map directly onto the environmental constraints motivating my architecture's design for coastal fisheries.

---

### 10. Hybrid AI Taxonomy

- **Hybrid AI approach?** Not applicable. The paper does not describe or propose a hybrid AI architecture.
- **Safety enforcement position:** Not addressed at the architectural level.
- **Two-level governance support?** No.

**Assessment:** N/A — paper operates at the ethical/survey level, not the architectural level.

---

### 11. Baseline Comparison and Evaluation

- **Baseline comparison?** No. The paper is a narrative review; it does not evaluate a specific system against a baseline.
- **Metrics?** N/A.
- **CAUTION zone testing?** No.
- **Safety Dominance Property verification?** No.
- **Graduated vs. binary governance comparison?** No — though the ethical dilemma in Section 4.6 implicitly asks this question.
- **Evaluation gaps:** The paper itself identifies that "there have been few studies regarding the large-scale adoption and deployment of AI in RLS, and so the cost-effectiveness remains yet to be assessed." It calls for "well-designed, large-scale studies that enable robust meta-analyses."

---

### 12. Key Concepts and Definitions

- **Resource-Limited Settings (RLS):** "Regions or communities where access to essential healthcare services, infrastructure, and economic resources is significantly constrained" — encompasses LMICs and underserved rural areas in high-income countries.
- **Clinical Decision Support Systems (CDSS):** AI systems that assist clinicians with evidence-based guidance for diagnosis, treatment planning, and patient monitoring, positioned as aids rather than autonomous decision-makers.
- **Five ethical dimensions for AI in RLS:** Bias and fairness, non-maleficence, privacy and security, autonomy, transparency.
- **"New technological colonisation":** The concern that AI applications may impose high-income-country paradigms on RLS without consideration for local practices and values.
- **Phased implementation:** Recommended strategy of gradual AI introduction to allow local adaptation without overwhelming existing structures.

---

### 13. Limitations and Unsolved Problems

- **Stated limitations:**
  - Narrative review methodology — not a systematic review; potential selection bias in included studies
  - Primarily focused on narrow AI (ANI) applications; does not address AGI implications
  - Limited to healthcare domain; does not generalise to other safety-critical domains
  - Written by undergraduate students at ANU (noted in author affiliations)
- **Unsolved problems / future work:**
  - Whether ethical boundaries should shift in extreme resource-scarcity scenarios (unresolved dilemma)
  - Whether AI investment is optimal use of scarce resources vs. traditional interventions
  - How to detect and measure bias in AI healthcare applications
  - Need for comprehensive ethical frameworks tailored to RLS
  - Need for large-scale deployment studies and cost-effectiveness evidence
- **Gaps aligned with my research:**
  - **No formal model for graduated AI governance.** The paper identifies the ethical *need* for varying levels of AI autonomy across conditions but provides no formal mechanism — no state classification, no gate function, no action-space restriction.
  - **No CAUTION mode.** The paper's governance model is implicitly binary (human oversight present → AI as support; human oversight absent → ethical dilemma about full AI autonomy). An intermediate mode with restricted AI output scope is absent.
  - **No Safety Dominance Property.** No formal guarantee that AI outputs are bounded by safety-state-determined constraints.
  - **No architectural fallback mechanism.** The recommendation for "safety-net mechanisms" is qualitative; my architecture formalises this as G(UNSAFE) = 0 with deterministic fallback.

---

### 14. Methodology Notes

- **Method:** Narrative review / survey, drawing from 42 sources across PubMed and Google Scholar. Inclusion criteria: studies evaluating AI in healthcare, addressing ethical issues, discussing equitable implementation frameworks, or discussing barriers/facilitators relevant to RLS.
- **Alignment with DSR pipeline?** No. This is a review paper, not a design science research study. It does not design, formalise, prototype, or evaluate an artefact.
- **Methodological insights for my research:** The paper's ethical evaluation framework (five dimensions) could inform the socio-technical evaluation component of my DSR pipeline — particularly around autonomy, transparency, and culturally sensitive deployment. The recommendation for phased implementation aligns with my prototype-first evaluation approach.

---

### 15. Quotable / Citable Points

1. **RLS definition and scope:** The paper provides a clear characterisation of resource-limited settings encompassing data scarcity, workforce shortages, and regulatory gaps — useful for establishing the deployment context of my architecture. (Section 1, p. 1953)

2. **AI as decision support, not automation:** "Currently, most experts agree that such algorithms themselves are not reliable enough to act as the final decision-maker, which is reflected in global regulatory frameworks." — supports my architecture's human-in-the-loop design. (Section 3.1, p. 1954)

3. **Ethical dilemma on graduated autonomy:** The paper raises whether "ethical principles, such as the requirement for human oversight, be relaxed in [extreme] scenarios to prioritize maximizing the number of lives saved" — directly motivates the need for a formalised graduated governance model rather than ad hoc ethical judgment. (Section 4.6, p. 1958)

4. **Safety-net recommendation:** "In the case of systems malfunction or connectivity failure, there must be safety net mechanisms in place and healthcare professionals must be able to deliver care regardless of AI assistance." — supports my UNSAFE-state fallback design. (Section 5, p. 1959)

5. **Over-reliance warning:** The paper warns against over-reliance on AI in RLS and calls for maintaining human capability independent of AI — aligns with my architecture's deterministic fallback layer. (Section 5, p. 1959)

---

### 16. Relation to My Research and Positioning

- **Governance level implemented:** Partial Level 1 only (policy-level human oversight requirement). No Level 2.
- **Level 2 state-conditioned?** N/A — not implemented.
- **Proximity to (G(S), A_AI(S))?** Distant. The paper identifies the ethical *questions* that a formal governance pair would answer (when should AI autonomy change? what should AI be allowed to do under different conditions?) but provides no formal mechanism.
- **Safety Dominance Property?** Not defined.
- **Gap my research addresses:** The paper's unresolved ethical dilemma — whether governance should be graduated across conditions — is precisely what my architecture resolves formally through the three-mode model with (G(S), A_AI(S)). Rather than leaving graduated governance to ad hoc ethical judgment, my architecture embeds it as a deterministic, formally verifiable property.

**Positioning paragraph:** Zhao & Yuan (2025) serves as **domain background and motivational context** for my research. Its primary value is threefold: (1) it provides a well-structured characterisation of resource-limited settings that applies beyond healthcare to my coastal fisheries domain — including data scarcity, workforce constraints, weak regulatory oversight, connectivity challenges, and low digital literacy; (2) it identifies the ethical dilemma of whether AI governance should vary by operational severity, which directly motivates the formal graduated governance model at the core of my architecture; and (3) it reinforces the consensus that AI should function as decision support with human authority preserved, supporting my architecture's human-in-the-loop design. However, the paper operates entirely at the qualitative/ethical level and provides no formal model, no technical architecture, and no governance mechanism — making it a motivation source rather than a technical antecedent or baseline comparator.

---

### 17. Overall Relevance Score

**⭐⭐⭐ Medium** — Provides useful background on low-resource deployment constraints and ethical evaluation dimensions. The RLS characterisation and the ethical dilemma around graduated governance are directly citable. However, the paper has no formal model, no technical architecture, and no governance mechanism, limiting its contribution to motivational context rather than architectural antecedent or baseline comparison. Its healthcare focus (rather than maritime/fisheries) and undergraduate-level scope further reduce direct applicability.

---

*Functional role in literature review:* **Domain background / motivational context** — establishes the deployment challenges of AI in resource-limited settings and the ethical imperative for graduated governance, supporting the motivation section of the dissertation.
