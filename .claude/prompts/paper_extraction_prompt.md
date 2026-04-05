## Literature Review Extraction Prompt
*For: "A Graduated Safety-State-Gated Architecture for AI Decision Support in Low-Resource Environments: Design and Socio-Technical Evaluation in Coastal Fisheries"*

---

You are assisting with a PhD literature review. The research focuses on designing a **Graduated Safety-State-Gated Hybrid AI Decision Architecture** for safety-critical, low-resource environments, with coastal fisheries as the case study.

### Formal Architecture (Appendix C)

The architecture is formally defined as a pipeline:

**E → S = f(E) → (G(S), A_AI(S)) → AI(E)**

Where:

- **E = {w, r, m, o, v, t}** — environmental state vector (wind, rainfall, marine warning, ocean condition, vessel class, trip state)
- **S = f(E)** — safety state classification function, where S ∈ {SAFE, CAUTION, UNSAFE}
- **G(S)** — AI participation gate function (Level 1 governance): G(S) = 0 (AI blocked) or 1 (AI permitted)
- **A_AI(S)** — AI-admissible recommendation space (Level 2 governance): the set of recommendation types AI is permitted to generate under safety state S
- **R = {Go, Delay, DepartureTime, Duration}** — the set of recommendation types, where Go = go/no-go, Delay = delay departure, DepartureTime = departure window, Duration = safe trip duration

### Two-Level Governance Structure (Core Contribution)

The architecture implements a **two-level governance model** controlled by environmental safety state. This is the core architectural contribution.

| Level | Function | What it controls |
|---|---|---|
| **Level 1 — Participation governance** | G(S) | Whether AI is allowed to operate |
| **Level 2 — Advisory scope governance** | A_AI(S) | What types of recommendation AI is allowed to generate |

The AI decision system is governed by the pair **(G(S), A_AI(S))**.

### Three-Mode AI Participation Model

| Safety State | G(S) | A_AI(S) | AI Behaviour |
|---|---|---|---|
| SAFE | 1 | {Go, Delay, DepartureTime, Duration} | Full advisory scope — go/no-go, timing, duration |
| CAUTION | 1 | {Go, Delay} | Restricted advisory — Go (with caution qualifier) and Delay only; no DepartureTime or Duration recommendations |
| UNSAFE | 0 | ∅ | AI disabled — no AI recommendations; warning only |

This produces the containment relationship:

**A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅**

The CAUTION state is where Level 2 governance does its work: G(S) = 1 (same as SAFE at Level 1), but A_AI(CAUTION) ⊂ A_AI(SAFE) (restricted at Level 2). Without Level 2 governance, CAUTION and SAFE are formally identical.

### Governance Constraints and Safety Properties

- **Participation constraint:** G(S) = 0 ⇒ A_AI(S) = ∅ — if the gate blocks AI, the recommendation space must be empty
- **Advisory restriction constraint:** S = CAUTION ⇒ A_AI(CAUTION) ⊂ A_AI(SAFE) — CAUTION must restrict advisory scope relative to SAFE
- **Safety Dominance Property:** For all E, AI(E) ⊆ A_AI(S) — the AI can only generate recommendations within the admissible space defined by the safety state. Probabilistic AI reasoning cannot override deterministic safety constraints

### Existing Literature Context

- **Level 1 governance (participation control)** is well-established: shields (Könighofer et al.), gatekeepers (Liang et al.), supervision functions (SAFEXPLAIN), and formal safety frameworks (Dalrymple et al.) all implement binary AI on/off control
- **Level 2 governance (output-scope control)** exists separately: guardrail taxonomies (Shamsujjoha et al.), runtime policy enforcement (AgentSpec), and output filtering (Chen et al.) constrain what AI produces — but these are applied per-action or per-artifact, not conditioned on classified environmental safety state
- **Flehmig et al.** is the closest prior art: a three-level traffic-light governance model for AI in safety-critical systems. However, it operates at a single governance level, is triggered by AI performance degradation (not environmental state), and governs monitoring intensity (not AI recommendation scope)
- **No existing paper** implements both levels in a unified, state-conditioned governance pair (G(S), A_AI(S))
- **No existing paper** defines a Safety Dominance Property for graduated (non-binary) governance

### Core Research Themes

1. Hybrid AI (deterministic rule-based + probabilistic AI reasoning)
2. Safety-critical AI decision systems
3. AI governance — controlling *when* AI participates (Level 1) and *what* AI may recommend (Level 2)
4. Low-resource environments (limited data, connectivity, computing)
5. Decision architecture formalisation (E, S = f(E), G(S), A_AI(S), Safety Dominance Property)
6. Human role in AI-assisted decision-making
7. Socio-technical evaluation of AI systems
8. Coastal fisheries as a safety-critical, low-resource domain

---

## Early Relevance Check (Hard Stop)

Before proceeding with full extraction, read the paper and answer these three screening questions:

1. Does this paper address **at least one** of the 8 core research themes listed above?
2. Does this paper contribute to **any** of the following: safety-critical AI architecture, AI governance mechanisms, hybrid AI design, formal decision models, low-resource AI deployment, or fisheries/maritime AI?
3. Could this paper plausibly be cited in a literature review about graduated AI governance for safety-critical decision support?

**If the answer to all three is No → STOP HERE.** Do not proceed with full extraction. Instead, output only:

```
## Early Relevance Check: STOPPED

### Paper Identity
- [Title, authors, year, venue]

### Reason for Exclusion
- [1–2 sentences explaining why the paper does not meet the relevance threshold]

### Overall Relevance Score: ⭐ Minimal
```

**If the answer to any question is Yes or Partial → proceed with full extraction below.**

---

Please extract the following:

### 1. Paper Identity
- Full title, authors, year, publication venue (journal/conference)
- Type of paper (empirical study, conceptual framework, review, system design, etc.)

### 2. Core Contribution
- What is the main problem this paper addresses?
- What is its proposed solution or key finding?
- What are the main contributions of this study?
- What is novel or unique about their approach compared to prior work?

### 3. Relevance to My Research
Map the paper's content to my research themes. For each relevant theme below, state whether the paper addresses it and briefly explain how:

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | Yes / Partial / No | ... |
| Safety-critical AI decision-making | Yes / Partial / No | ... |
| AI governance / control mechanisms | Yes / Partial / No | ... |
| Low-resource environments | Yes / Partial / No | ... |
| Decision architecture formalisation | Yes / Partial / No | ... |
| Human role in decision-making | Yes / Partial / No | ... |
| Socio-technical evaluation | Yes / Partial / No | ... |
| Coastal fisheries / maritime domain | Yes / Partial / No | ... |

**Mid-Extraction Relevance Gate:** Count the number of "Yes" and "Partial" ratings above.

- **If 0 Yes and ≤ 1 Partial → STOP HERE.** Output Sections 1–3 only, add a relevance score of ⭐ Minimal or ⭐⭐ Low, and state the reason for early termination.
- **If 1–2 Yes or ≥ 2 Partial → REDUCED EXTRACTION.** Complete Sections 4–7 and 12–13 only (architecture, formalisation, governance level, key concepts, limitations). Skip Sections 8–11 and 14–15. Complete Section 16–17 as normal.
- **If ≥ 3 Yes → FULL EXTRACTION.** Complete all 17 sections.

### 4. Decision Architecture Analysis
- How does the system structure its decision-making process? (e.g., sequential, hierarchical, parallel, layered)
- Is there a layered architecture, safety constraint mechanism, or governance structure controlling how decisions are made?
- Are there any rule-based constraints or safety checks applied *before* AI/probabilistic decisions are allowed to proceed?
- How is the boundary between deterministic control and AI reasoning defined or enforced?
- Does the architecture account for failure modes, fallback behaviour, or override mechanisms?

### 5. Formal Model and Mathematical Representation
- Does the paper define any formal model of its decision system? (e.g., state variables, safety functions, gate functions, action spaces)
- If yes, describe the formal structure — what inputs, states, and outputs are defined mathematically?
- How does the paper's formal model compare to the pipeline E → S = f(E) → (G(S), A_AI(S)) → AI(E) used in my research?
- Does the paper model any form of **state-dependent recommendation restriction** — where the set of permitted AI outputs changes across safety states (analogous to A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅)?
- Does the paper define any formal safety property comparable to the **Safety Dominance Property** (AI(E) ⊆ A_AI(S)) — i.e., a guarantee that AI outputs always fall within state-determined bounds?
- Is the formalisation used for analysis, proof, or evaluation — or is it purely descriptive?

### 6. Safety State Classification
- Does the paper classify operational or environmental conditions into discrete risk or safety levels?
- If yes, what are the levels used? (e.g., binary safe/unsafe, tripartite safe/caution/unsafe, or a continuous scale)
- How are thresholds or rules defined for each safety level?
- How does the paper's classification scheme compare to the S = f(E) → {SAFE, CAUTION, UNSAFE} structure in my research?
- **Critically**: Does the paper differentiate the *AI's recommendation scope* across safety levels — particularly a mode where AI still participates but with restricted output types (analogous to the CAUTION state where A_AI(CAUTION) ⊂ A_AI(SAFE))?

### 7. Governance Level Analysis
- Does the paper address *when* and *how* AI is allowed to operate — not just filtering its outputs but governing the degree of AI engagement?
- Classify the paper's governance approach:

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (equivalent to G(S)) | Yes / Partial / No | ... |
| **Level 2 — Advisory scope governance** | What may AI recommend? (equivalent to A_AI(S)) | Yes / Partial / No | ... |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | Yes / Partial / No | ... |

- Does the paper implement a **binary AI switch** (Level 1 only) or a **graduated governance model** (Level 1 + Level 2)?
- If the paper implements any form of Level 2 governance, is it state-conditioned (varies by classified safety state) or static (same constraints regardless of state)?
- Does this paper support or contradict the idea of a two-level governance pair (G(S), A_AI(S)) conditioned on environmental safety state?

### 8. Human Role in Decision-Making
- Is the human involved in the final decision, or does the system decide autonomously?
- Is the system positioned as **decision support** (human decides) or **decision automation** (system decides)?
- How does the system interact with human users — what information is presented, and how?
- Is there a human override or escalation mechanism when the system is uncertain or unsafe?

### 9. System Constraints and Environment
- Does the system account for real-world constraints such as limited data, limited compute, unreliable connectivity, or varying user expertise?
- Is the system designed for real-world deployment or evaluated only in simulation?
- Are there any resource-aware design choices — lightweight models, offline capability, graceful degradation?
- How does the system perform under edge cases or resource-limited conditions?

### 10. Hybrid AI Taxonomy
- What type of hybrid AI approach does the paper use? Classify it as one of the following (or describe if different):
  - Neuro-symbolic (learning + logic/rule verification)
  - Supervisory control (AI output monitored by rule-based supervisor)
  - Constitutional / governance-based (rule layer constrains AI behaviour)
  - Stage-gate (sequential checkpoints regulate AI participation)
  - Rule-ML pipeline (rules pre/post-process ML output)
  - Other — describe
- Where does safety enforcement sit: before AI reasoning, alongside it, or after?
- Does the hybrid approach support **two-level governance** — where both AI participation (Level 1) and AI advisory scope (Level 2) are governed by safety state — or is it limited to single-level binary control?
- How does this paper's hybrid AI approach compare to the deterministic-gate-first, two-level governance model in my research?

### 11. Baseline Comparison and Evaluation
- Does the paper compare its approach against a baseline system without safety constraints or gating?
- If yes, what metrics are used to compare performance? (e.g., safety compliance, decision accuracy, consistency)
- Does the evaluation include scenario-based testing, simulation, or real-world deployment?
- Does the evaluation test behaviour specifically in the CAUTION zone — where AI participates under restriction (G(S) = 1 but A_AI restricted) — or only at SAFE/UNSAFE extremes?
- Does the evaluation verify any formal property comparable to the Safety Dominance Property (AI(E) ⊆ A_AI(S))?
- Does the evaluation compare graduated governance against binary governance — i.e., testing whether Level 2 adds value beyond Level 1 alone?
- What evaluation gaps remain — particularly around low-resource or safety-critical conditions?

### 12. Key Concepts and Definitions
- List any important terms, models, frameworks, or definitions introduced in this paper that are relevant to my research.

### 13. Limitations and Unsolved Problems
- What are the stated limitations of the study?
- What problems remain unsolved or are acknowledged as future work?
- Does it identify any gaps that align with my research problem?
- Does it acknowledge limitations that my architecture could address — particularly:
  - The lack of a two-level governance model that separates participation governance (G(S)) from advisory scope governance (A_AI(S))?
  - The absence of a CAUTION mode where AI participates under restricted recommendation scope?
  - The absence of a formal Safety Dominance Property for graduated governance?

### 14. Methodology Notes
- What research method was used? (e.g., Design Science Research, simulation, case study, formal modelling, prototype testing)
- Does the methodology align with the DSR pipeline of design → formalise → prototype → evaluate used in my research?
- Can any aspect of the methodology inform my evaluation or formalisation approach?

### 15. Quotable / Citable Points
- List 3–5 specific claims or findings from the paper that I could directly cite in my literature review, with their approximate location (section or page).

### 16. Relation to My Research and Positioning
- Does this paper implement Level 1 governance (participation control), Level 2 governance (output-scope control), or both?
- If it implements Level 2, is it state-conditioned (varies by classified environmental state) or static?
- Does it come close to — or fall short of — the two-level governance pair (G(S), A_AI(S)) conditioned on environmental safety state?
- Does it define any formal safety property comparable to the Safety Dominance Property?
- What gap still exists that my research can address based on this paper?
- In one paragraph, explain how this paper positions within my research: Does it support my motivation? Fill background? Represent a baseline I compare against? Highlight a gap I fill?

### 17. Overall Relevance Score
Rate the paper's relevance to my PhD research:
- ⭐⭐⭐⭐⭐ Core — directly addresses the two-level governance gap or implements the closest prior art
- ⭐⭐⭐⭐ High — addresses 2–3 major themes including governance, formalisation, or safety-critical architecture
- ⭐⭐⭐ Medium — provides useful background or partial context on one or more themes
- ⭐⭐ Low — tangentially related
- ⭐ Minimal — limited relevance

---
*Note: If the paper is only partially readable or has limited content visible, extract what is available and flag any gaps.*
