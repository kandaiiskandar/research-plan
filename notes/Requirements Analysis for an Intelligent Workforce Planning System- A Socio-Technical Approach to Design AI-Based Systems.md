## Literature Review Extraction: Gabriel et al. (2022)

---

### 1. Paper Identity

- **Title:** Requirements analysis for an intelligent workforce planning system: a socio-technical approach to design AI-based systems
- **Authors:** Stefan Gabriel, Dominik Bentler, Eva-Maria Grote, Caroline Junker, David Meyer zu Wendischhoff, Michael Bansmann, Benedikt Latos, Daniela Hobscheidt, Arno Kühn, Roman Dumitrescu
- **Year:** 2022
- **Venue:** Procedia CIRP 109, pp. 431–436 (32nd CIRP Design Conference)
- **DOI:** 10.1016/j.procir.2022.05.274
- **Type:** Applied methodology paper (procedure model for socio-technical requirements elicitation, with industrial case study)

---

### 2. Core Contribution

- **Problem:** Developing AI-based systems using purely technology-centred approaches fails to capture employee needs, implicit knowledge, and organisational constraints. Existing socio-technical design approaches are insufficiently focused on the specific challenges of requirements elicitation for AI-based systems.
- **Solution:** A four-step procedure model that adapts the HTO analysis (Human–Technology–Organisation, per Ulich 2013) for requirements elicitation of AI-based systems. The four steps are: (1) mission statement development (company level), (2) process mapping (organisational unit level), (3) stakeholder interviews (group level), and (4) quantitative survey of affected workers (individual level).
- **Main contributions:**
  - Combines proven requirements elicitation methods with HTO analysis levels in a simplified four-step (vs. original seven-step) procedure
  - Demonstrates the procedure on an industrial case: intelligent workforce planning in manufacturing assembly
  - Produces a prioritised requirements catalogue covering technical, employee-related, and organisational categories
- **Novelty:** The specific combination of HTO analysis with AI-focused requirements elicitation is new; individual methods used are established. The simplification from seven to four steps is positioned as practical for industrial adoption.

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | No | No hybrid AI architecture is discussed; the paper is about requirements elicitation methodology, not system architecture |
| Safety-critical AI decision-making | No | The application domain is manufacturing workforce planning — not safety-critical in the sense of life-safety or environmental hazard |
| AI governance / control mechanisms | No | No mechanisms for controlling when/what AI may decide; the paper captures what stakeholders *want* from AI but does not design governance |
| Low-resource environments | No | Industrial manufacturing context with enterprise IT infrastructure |
| Decision architecture formalisation | No | No formal model, state variables, or decision pipeline is defined |
| Human role in decision-making | Yes | Explicitly positions AI as decision *support* not decision *automation*; reports stakeholder finding that "participants wanted decision suggestions but not decision automation through AI"; uses intelligence augmentation framing (Jarrahi 2018) |
| Socio-technical evaluation | Yes | Core contribution — the entire paper is a socio-technical requirements elicitation approach; uses HTO analysis, stakeholder interviews, and quantitative work design survey before system development |
| Coastal fisheries / maritime domain | No | Manufacturing assembly domain |

**Mid-Extraction Relevance Gate:** 2 Yes, 0 Partial → **REDUCED EXTRACTION** (Sections 4–7, 12–13, 16–17)

---

### 4. Decision Architecture Analysis

- **Architecture:** No decision architecture is defined. The paper produces a *requirements catalogue* for a future AI-based system, not the system itself.
- **Layered structure:** The HTO analysis levels (company → organisational unit → group → individual) provide a layered *elicitation* structure, not a layered *decision* architecture.
- **Rule-based constraints before AI:** Not addressed. The paper does not discuss how AI outputs would be constrained or gated.
- **Boundary between deterministic control and AI reasoning:** Not defined. The paper identifies that users want "recommendation generation" and "forecasting" from AI, but does not specify how these would be governed.
- **Failure modes / fallback:** Not addressed at the architectural level.

**Assessment:** This paper operates entirely upstream of architecture design — it captures *what* the system should do, not *how* it should be governed. No overlap with the DSR pipeline's governance pair (G(S), A_AI(S)).

---

### 5. Formal Model and Mathematical Representation

- **Formal model:** None. The paper is qualitative/procedural — no state variables, safety functions, gate functions, or action spaces are defined.
- **Comparison to DSR pipeline:** No comparison possible. The paper does not model any decision pipeline, environmental state vector, or safety classification.
- **State-dependent recommendation restriction:** Not addressed.
- **Safety Dominance Property:** Not addressed.
- **Formalisation purpose:** N/A — no formalisation is present.

---

### 6. Safety State Classification

- **Discrete risk/safety levels:** Not defined. The application domain (workforce planning) does not involve environmental hazard classification.
- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:** No parallel structure exists in this paper.
- **AI recommendation scope differentiation across safety levels:** Not addressed — the paper identifies recommendation types stakeholders want (e.g., shift plan suggestions, capacity forecasts) but does not condition these on any safety or risk state.

---

### 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (G(S)) | No | No mechanism for enabling/disabling AI based on system state |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | No | No mechanism for restricting recommendation types by state |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | No | Not addressed |

- **Governance type:** Neither binary switch nor graduated governance is implemented or proposed. The paper identifies *desired* AI functions (recommendations, forecasts) but does not define any governance mechanism over those functions.
- **Relation to two-level governance pair:** The paper operates at the requirements level — it captures the human expectations and organisational context that a governance mechanism would need to respect, but does not design or formalise such a mechanism.

---

### 12. Key Concepts and Definitions

- **HTO Analysis (Human–Technology–Organisation):** Integrated analysis framework per Ulich (2013) examining work systems across four levels: company, organisational unit, group, individual. Ensures socio-technical perspective in system design.
- **Intelligence augmentation:** AI designed to support, not replace, human decision-makers (framing drawn from Jarrahi 2018).
- **Complementarity of humans and AI:** Humans handle uncertainty, complexity, and equivocality through intuition, consensus-building, and data-seeking; AI handles real-time data access, data processing, and sentiment analysis (Table 1, per Jarrahi 2018).
- **Mission statement for AI system design:** A preliminary framing document specifying goals, stakeholders, and principles of action (e.g., employee participation, non-discrimination, transparency, ethics, health) before technical development begins.
- **Design Science Research (Hevner 2007):** Three-cycle methodology (relevance, design, rigour) used as the overarching research framework.

---

### 13. Limitations and Unsolved Problems

- **Stated limitations:**
  - Procedure demonstrated on a single use case only; generalisability to other AI applications unconfirmed
  - Requirements remain at a high level of abstraction — technical specifications still need derivation
  - No consideration of parallel introduction of multiple AI use cases or their interactions
- **Unsolved problems:**
  - How to translate high-level socio-technical requirements into concrete AI system architecture and governance mechanisms
  - How to handle iterative refinement of requirements as the AI system is incrementally implemented
- **Alignment with my research gaps:**
  - The paper identifies that stakeholders want AI as decision support (not automation) and want transparency and non-discrimination — but provides **no mechanism** for enforcing these at runtime
  - The gap between "stakeholders want restricted AI" and "the system formally restricts AI" is exactly the space my two-level governance architecture fills
  - The paper lacks any formal governance model — no G(S), no A_AI(S), no state-conditioned recommendation restriction

---

### 16. Relation to My Research and Positioning

- **Governance implementation:** Neither Level 1 nor Level 2 governance is implemented. The paper is pre-architectural.
- **Two-level governance pair:** Not approached. The paper identifies the *need* for human-centred AI that supports rather than automates decisions, but does not formalise how this is enforced.
- **Safety Dominance Property:** Not defined or approximated.
- **Gap my research addresses:** The paper demonstrates that socio-technical requirements elicitation for AI systems consistently surfaces the demand for AI as decision *support* with human oversight — but stops before defining any architectural mechanism to enforce this. My research fills this gap by formalising the governance pair (G(S), A_AI(S)) that operationalises such requirements into state-conditioned runtime constraints.

**Positioning paragraph:** Gabriel et al. (2022) is a **methodological background reference for socio-technical evaluation** in my literature review. It demonstrates an established approach (adapted HTO analysis) for capturing human, organisational, and technical requirements before AI system development — a process analogous to my own stakeholder engagement and socio-technical evaluation phases. The paper's key finding that end-users want AI-generated recommendations but explicitly reject AI-driven automation reinforces the motivation for decision-support architectures like mine. However, the paper operates entirely upstream of system architecture: it produces requirements but not governance mechanisms. It therefore supports my argument that socio-technical requirements elicitation is necessary but insufficient — the requirements must be translated into formal governance structures (like the two-level pair (G(S), A_AI(S))) to be operationally enforced. Citable primarily in the socio-technical evaluation methodology section and as motivational evidence for the human-in-the-loop design principle.

---

### 17. Overall Relevance Score

**⭐⭐ Low**

**Justification:** The paper is tangentially related. It addresses socio-technical requirements elicitation for AI-based systems — relevant to my evaluation methodology — but operates in a non-safety-critical domain (manufacturing workforce planning), defines no formal architecture or governance mechanism, and has no overlap with the core themes of hybrid AI, safety-state classification, or graduated governance. Its primary citation value is limited to: (a) methodological precedent for socio-technical requirements gathering via adapted HTO analysis, and (b) empirical evidence that end-users prefer AI as decision support over decision automation. It does not advance the architecture, formalisation, or governance gap claims central to my dissertation.

---

### Recommended Citation Uses

| Use | Section in dissertation | Specific point |
|---|---|---|
| Socio-technical methodology precedent | Evaluation methodology / Socio-technical evaluation design | HTO analysis adaptation as structured approach for capturing human–AI collaboration requirements |
| Stakeholder preference for decision support over automation | Motivation / Human role in decision-making | Empirical finding that assembly workers and planners explicitly prefer AI recommendations over AI automation |
| DSR methodology alignment | Research methodology | Uses Hevner (2007) three-cycle DSR — same methodological family as my research |
