## Literature Review Extraction

---

### 1. Paper Identity

- **Title:** Are We Regulating the Right Digital Systems? Testing Emerging Artificial Intelligence Frameworks against Real-World Public Sector Systems
- **Authors:** José-Miguel Bello y Villarino, Kimberlee Weatherall, Terry Carney, Alexandra Sinclair, Scarlet Wilcock
- **Year:** 2025
- **Venue:** *University of New South Wales Law Journal*, 48(4), pp. 1165–1195
- **DOI:** 10.53637/vrjl5367
- **Type:** Empirical-doctrinal analysis (comparative legal analysis + empirical classification of 163 real-world ADM systems)

---

### 2. Core Contribution

- **Problem:** Emerging AI regulatory frameworks (EU AI Act, NSW AIAF) restrict their scope to systems classified as "AI," but this may leave many high-risk automated decision-making (ADM) systems outside regulatory oversight — particularly rule-based systems operating in sensitive public sector domains.
- **Solution/Finding:** Empirical testing of 163 NSW government ADM systems against both frameworks reveals that roughly 60% of systems posing potentially elevated risk under the NSW AIAF do not qualify as "AI" under the EU AI Act definition, and are therefore exempt from mandatory assessment. The paper advocates extending risk-based regulatory frameworks to all ADM systems, not only AI.
- **Main contributions:**
  1. First large-scale empirical test of whether AI-focused regulation captures the right public sector systems
  2. Comparative doctrinal analysis of the EU AI Act and NSW AIAF definitions of "AI" and "high/elevated risk"
  3. Evidence that AI is a poor proxy for technological risk in the public sector — rule-based systems in sensitive domains (health, corrections, justice) fall outside AI-focused frameworks
  4. Policy recommendation: risk-based frameworks should encompass all ADM, not just AI
- **Novelty:** Unique empirical dataset (163 systems from NSW government) used to test regulatory scope assumptions; demonstrates the gap between regulatory intent and actual coverage quantitatively.

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | Partial | Distinguishes rule-based ADM from AI systems; shows that many public sector systems are purely rule-based and that the boundary between rule-based and AI is a live regulatory question — but does not design or propose a hybrid architecture |
| Safety-critical AI decision-making | Partial | Examines AI/ADM systems in safety-relevant public sector contexts (health pathology, corrections, justice) but does not address safety-critical systems in the engineering or operational sense (real-time, life-safety) |
| AI governance / control mechanisms | Yes | Core focus: analyses how two major regulatory frameworks govern AI systems through risk-based classification and assessment obligations; examines definitional scope as a governance mechanism |
| Low-resource environments | No | Not addressed; all systems are in a well-resourced government context (NSW, Australia) |
| Decision architecture formalisation | No | No formal model of decision architecture; analysis is legal/regulatory, not computational |
| Human role in decision-making | Partial | Notes that the majority of mapped systems involve humans making final decisions; discusses the limitations of human oversight as a sole governance mechanism (citing Green 2022, Crootof et al. 2023) |
| Socio-technical evaluation | Partial | Empirical evaluation of how regulatory frameworks apply to real-world socio-technical systems; highlights the socio-technical gap between regulatory definitions and deployed system characteristics |
| Coastal fisheries / maritime domain | No | Not addressed |

**Mid-Extraction Relevance Gate:** 1 Yes + 3 Partial = **REDUCED EXTRACTION** (Sections 4–7 and 12–13 only; skip 8–11, 14–15)

---

### 4. Decision Architecture Analysis

- **Not applicable in the technical sense.** This paper does not describe or propose a decision architecture. It analyses *regulatory* architecture — the two-step scope test (1: "does the system involve AI?" → 2: "does it pose high/elevated risk?") that determines whether a system falls within governance frameworks.
- The regulatory architecture is sequential and conjunctive: a system must satisfy *both* criteria to trigger mandatory assessment. This is a **binary gate at each stage** — AI yes/no, then risk yes/no.
- There is no layered safety constraint mechanism, no runtime governance, and no formal fallback or override mechanism described at the system level.
- **Relevant observation for DSR research:** The paper demonstrates that regulatory governance over AI systems operates as a static, design-time classification exercise (does the system qualify as AI? does the use case qualify as high-risk?) rather than a runtime, state-conditioned mechanism. This contrasts directly with the DSR architecture's runtime safety-state-conditioned governance.

---

### 5. Formal Model and Mathematical Representation

- **No formal model is defined.** The paper is a doctrinal-empirical legal analysis.
- The closest to formalisation is the structured concordance analysis (Tables 1 and 2), which cross-tabulates systems along two binary dimensions (high-risk yes/no × AI yes/no) to identify regulatory coverage gaps.
- **Comparison to DSR pipeline:** No analogue exists. The paper does not define environmental state vectors, safety classification functions, gate functions, or admissible action spaces. The "governance" it examines is regulatory (which systems are *subject to* rules) rather than operational (how a system *behaves* under different conditions).
- **No state-dependent recommendation restriction.** The regulatory frameworks examined impose a single set of obligations on all in-scope systems; they do not graduate the *type* of AI output permitted based on classified risk state.
- **No Safety Dominance Property or equivalent.**

---

### 6. Safety State Classification

- **Risk classification exists but is regulatory, not operational.**
  - **EU AI Act:** Binary high-risk / not-high-risk, determined by use case (Annex III categories) or product safety legislation (Annex I). A derogation in Art. 6(3) exempts systems performing narrow procedural tasks, preparatory tasks, etc.
  - **NSW AIAF:** Graduated risk scale (low → mid-range → high → very high residual risk), determined by six indicator questions (operational impact, autonomy, data sensitivity, unintended harms, explainability). Different consequences attach to different residual risk levels (mid-range: pilot required; high: AI Review Committee referral).
- **The NSW AIAF is the more interesting comparator:** It implements a graduated risk classification with differentiated governance obligations at each level. This is structurally analogous to graduated safety states — but it operates at the *regulatory assessment* level (design-time), not at the *system runtime* level.
- **Critical difference from DSR:** Neither framework differentiates the *AI's recommendation scope* across risk levels. All in-scope systems face the same category of obligations (assessment, monitoring, documentation). There is no mechanism equivalent to A_AI(S) where the *type* of AI output permitted varies by classified state.
- **No CAUTION-mode analogue.** The NSW AIAF's mid-range risk category triggers additional process (piloting) but does not restrict what the AI system may do — it adds procedural requirements on the deploying agency, not operational constraints on the system itself.

---

### 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (equivalent to G(S)) | Partial | The regulatory frameworks implement a binary inclusion/exclusion gate: systems either fall within scope (and must be assessed) or outside scope (and face no AI-specific obligations). This is a *regulatory* participation gate — "does this system get governed?" — not an *operational* participation gate — "does the AI activate?" |
| **Level 2 — Advisory scope governance** | What may AI recommend? (equivalent to A_AI(S)) | No | Neither framework constrains the *type* of AI output based on risk level. Obligations are procedural (assessment, documentation, monitoring, committee review) and apply uniformly to all in-scope systems. No mechanism restricts the AI's recommendation space based on classified risk state. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | No | Risk classification is static and design-time, not conditioned on real-time environmental state. |

- **Governance type:** Binary regulatory gate (Level 1 only, at the regulatory scope level). The NSW AIAF's graduated risk scale introduces *procedural* graduation (different assessment obligations at different risk levels) but not *operational* graduation (different AI behaviour at different risk levels).
- **Key insight for DSR positioning:** This paper provides strong evidence that even the most sophisticated existing governance frameworks (EU AI Act, NSW AIAF) operate at a single governance level — they determine *whether* a system is subject to governance, not *what the system may do* under different conditions. The absence of Level 2 operational governance — and particularly the absence of state-conditioned restriction of AI advisory scope — is visible even in the regulatory domain. This supports the broader gap claim that Level 2 governance (A_AI(S)) conditioned on classified state is absent across both regulatory and technical domains.

---

### 12. Key Concepts and Definitions

- **ADM (Automated Decision-Making):** Fully or partially automated technical systems used by government in administrative decision-making affecting the public — explicitly broader than AI, encompassing rule-based and traditional computing systems
- **Risk-based regulatory approach:** Graduated governance obligations scaled to assessed risk level; the dominant paradigm in AI regulation globally
- **AI as regulatory proxy for risk:** The assumption (challenged by this paper) that restricting governance to AI systems adequately captures technological risk
- **Regulatory blind spot:** Systems posing elevated risk but falling outside AI definitions — particularly rule-based systems in sensitive domains (health, corrections, justice)
- **Binary scope gate:** The conjunctive two-step test (AI? + high-risk?) that determines regulatory coverage — structurally a binary gate at each stage
- **"When in doubt, include" principle:** The NSW AIAF's guidance to public servants to apply the framework when uncertain about whether a system qualifies — an expansive interpretive principle that nonetheless depends on voluntary compliance

---

### 13. Limitations and Unsolved Problems

- **Stated limitations:**
  1. Dataset limited to NSW state government; excludes local government and NSW Police
  2. Classification based on brief text descriptions — fuller system documentation would improve accuracy
  3. AI classification used only the EU AI Act definition; the NSW AIAF's broader, open-ended definition could not be operationalised for systematic classification
  4. Single-evaluator methodology for primary classification (mitigated by partial second-evaluator quality check)
  5. Analysis reveals scope gaps but does not assess whether excluded systems have *actually* caused harm

- **Unsolved problems / future work:**
  1. How to design regulatory frameworks that capture all high-risk ADM systems without imposing excessive burden on low-risk systems
  2. Whether AI-specific risks (opacity, adaptiveness, autonomy) warrant a distinct regulatory track or can be addressed within a unified ADM framework
  3. How to manage "creeping AI" — simple systems that incorporate AI capabilities through future updates without triggering reassessment

- **Alignment with DSR research gaps:**
  - The paper does **not** identify the absence of runtime state-conditioned governance as a gap — its analysis remains at the regulatory/policy level
  - However, the paper **strongly supports** the claim that existing governance operates as binary inclusion/exclusion (Level 1 only), with no mechanism to graduate *what AI may do* based on classified risk state (Level 2 absence)
  - The finding that rule-based systems in sensitive domains fall outside AI-focused governance indirectly supports the case for hybrid architectures that *combine* rule-based safety governance with AI reasoning — the DSR architecture's core design principle

---

### 16. Relation to My Research and Positioning

- **Governance level:** Implements Level 1 (regulatory participation gate: AI yes/no → in-scope/out-of-scope) at the policy level. Does not implement Level 2 (advisory scope governance). Does not implement state-conditioned governance.
- **Gap relative to DSR:** The paper demonstrates that even sophisticated regulatory frameworks operate at a single governance level — determining *whether* a system falls within scope — without graduating *what the system may do* based on classified risk state. The NSW AIAF's graduated risk scale (low/mid-range/high/very high) produces differentiated *procedural* obligations (piloting, committee review) but not differentiated *operational constraints* on AI behaviour. This is precisely the gap the DSR two-level governance pair (G(S), A_AI(S)) addresses at the operational/architectural level.
- **No Safety Dominance Property equivalent.** The regulatory frameworks impose general obligations (transparency, monitoring, human oversight) but do not define a formal property guaranteeing that AI outputs always fall within state-determined bounds.
- **Positioning paragraph:** This paper serves as **supporting background for the governance gap claim**, particularly from the regulatory/policy perspective. It provides empirical evidence that existing AI governance frameworks implement binary scope gates (AI yes/no, high-risk yes/no) rather than graduated operational governance. While the paper operates at the regulatory level rather than the system architecture level, its core finding — that governance frameworks fail to differentiate system behaviour across risk states — reinforces the DSR architecture's motivation. The paper is best cited in the **literature review's AI governance section** to demonstrate that the binary governance paradigm extends beyond technical safety mechanisms (shields, guardrails) into the regulatory domain, and that even graduated risk classification (NSW AIAF's four-level scale) produces only procedural differentiation, not operational constraint graduation. It also provides useful evidence for the **hybrid AI motivation** — the finding that rule-based systems in sensitive domains fall outside AI-focused governance frameworks supports the case for architectures that formally integrate rule-based safety governance with AI reasoning rather than treating them as separate regulatory categories.

---

### 17. Overall Relevance Score

**⭐⭐ Low**

**Justification:** The paper addresses AI governance from a regulatory/legal perspective rather than from the system architecture or safety engineering perspective central to the DSR research. It does not define formal models, decision architectures, safety state classification functions, or operational governance mechanisms. Its contribution to the DSR literature review is limited to background evidence: (1) that binary governance (in-scope/out-of-scope) is the dominant paradigm even in regulatory frameworks, (2) that graduated risk classification produces procedural but not operational differentiation, and (3) that rule-based systems warrant governance attention alongside AI systems — supporting the hybrid architecture rationale. It does not address safety-critical operations, low-resource environments, maritime/fisheries domains, or decision architecture formalisation. Useful as a secondary citation in the governance gap discussion but not a core reference.

**Recommended citation uses:**
- AI governance section: evidence that regulatory frameworks implement binary scope gates rather than graduated operational governance
- Background support for the claim that no existing framework graduates *what AI may do* based on classified risk state
- Hybrid AI motivation: evidence that rule-based systems in sensitive domains require governance attention, supporting architectures that integrate both paradigms
