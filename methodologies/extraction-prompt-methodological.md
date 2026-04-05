# Methodological Foundation Paper Extraction Prompt

*For: "A Graduated Safety-State-Gated Architecture for AI Decision Support in Low-Resource Environments: Design and Socio-Technical Evaluation in Coastal Fisheries"*

---

You are assisting with a PhD literature review. The research focuses on designing a **Graduated Safety-State-Gated Hybrid AI Decision Architecture** for safety-critical, low-resource environments, with coastal fisheries as the case study.

This extraction prompt is for **methodological foundation papers** — papers that provide theoretical frameworks, validated instruments, or evaluation precedents that ground the research's evaluation methodology. These papers are NOT architectural comparators; they are the intellectual foundations for how the research evaluates its contribution.

---

## Research Context

### The Architecture (brief)

The architecture implements a **two-level governance pair (G(S), A_AI(S))** conditioned on classified environmental safety state S ∈ {SAFE, CAUTION, UNSAFE}:

- **Level 1 — Participation governance G(S)**: Whether AI operates at all (binary gate)
- **Level 2 — Advisory scope governance A_AI(S)**: What types of recommendations AI is permitted to generate

This produces three distinct AI participation modes:
- **SAFE**: AI fully enabled, full recommendation scope
- **CAUTION**: AI enabled but restricted — only a subset of recommendation types permitted
- **UNSAFE**: AI disabled entirely

### The Evaluation Gap

The research must evaluate two things that have no direct precedent in AI governance literature:

1. **PS4 — Comparative evaluation**: Does graduated two-level governance (Level 1 + Level 2) produce safer outcomes than binary governance (Level 1 only)? The research uses a three-condition experimental design: ungated AI vs binary-gated AI vs two-level graduated AI.

2. **PS5 — Socio-technical evaluation**: How do users understand, trust, and respond to three distinct AI governance states — particularly the CAUTION mode, where AI participates under restriction? Users have never encountered "AI active but operating under restriction" as a distinct mode from "AI fully enabled."

### Why Methodological Foundation Papers Matter

These papers provide:
- **Theoretical grounding** for why graduated governance is a valid design choice (not just "it doesn't exist")
- **Validated instruments** for measuring trust, understanding, and reliance across automation levels
- **Precedent** for evaluating human response to intermediate automation/governance modes
- **Conceptual frameworks** that the evaluation design adapts to the governance context

---

## Extraction Instructions

Please extract the following from the paper:

### 1. Paper Identity
- Full title, authors, year, publication venue (journal/conference)
- Type of paper (theoretical framework, empirical study, review, instrument development, standard, etc.)
- Citation count or impact indicator if available (this helps establish the paper as foundational)

### 2. Core Contribution
- What is the main problem this paper addresses?
- What is its proposed solution, framework, or key finding?
- What makes this paper foundational or widely cited in its field?

### 3. Relevance to My Research

Map the paper to these research themes:

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

### 4. Graduated Automation / Governance Framework

This is the key section for methodological papers. Extract in detail:

- Does the paper define **levels, stages, or grades** of automation, autonomy, or system control?
- If yes, list all levels/stages with their definitions.
- Does the framework distinguish between **"system participates at all"** (analogous to Level 1 governance) and **"what the system is allowed to do"** (analogous to Level 2 governance)?
- Does the framework include an **intermediate mode** where the system operates with reduced capability, restricted scope, or increased human oversight (analogous to the CAUTION state)?
- How does the paper's framework map to the proposed three-mode governance model?

| Paper's concept | My architecture's equivalent | Alignment |
|----------------|------------------------------|-----------|
| [Paper's level/concept] | [G(S), A_AI(S), SAFE/CAUTION/UNSAFE, etc.] | Strong / Partial / Weak |

- Does the paper argue that **graduated control is superior to binary control**? If so, what is the argument?
- Does the paper identify risks or failure modes of **binary (all-or-nothing) automation control**?

### 5. Trust, Reliance, and User Response

- Does the paper address **human trust** in automated or AI systems?
- Does it define or operationalise trust in a measurable way?
- Does it propose or validate a **measurement instrument** (scale, questionnaire, behavioural measure) for trust or reliance?
- If yes, describe the instrument: items, dimensions, validation method, reliability metrics.
- Does the paper distinguish between different types of trust failure:
  - **Overtrust / complacency** — relying on the system when it should not be trusted
  - **Undertrust / disuse** — rejecting the system when it should be trusted
  - **Misuse** — using the system outside its intended scope
- How do these trust concepts apply to the three governance modes?
  - SAFE mode: Risk of overtrust? (AI fully enabled, user may over-rely)
  - CAUTION mode: Does restricted AI scope help calibrate trust? Or create confusion?
  - UNSAFE mode: Risk of undertrust in the system's safety classification?

### 6. Mode Awareness and Automation Surprises

- Does the paper address **mode confusion** — where users do not understand which mode the system is operating in?
- Does it address **automation surprises** — where the system behaves differently from user expectations?
- If yes, what causes mode confusion or automation surprises?
- What design recommendations does the paper offer for **preventing mode confusion**?
- How do these findings apply to the CAUTION mode specifically?
  - The CAUTION mode is a novel intermediate state — users have encountered "AI on" and "AI off" but not "AI on but restricted"
  - What does this paper suggest about how users might (mis)understand the CAUTION state?
  - What design principles should inform how the CAUTION mode is communicated to users?

### 7. Evaluation Methodology

- Does the paper describe an **evaluation method** for measuring human response to automation/AI?
- What experimental design does it use (within-subjects, between-subjects, mixed)?
- What dependent variables does it measure (trust, reliance, performance, situational awareness, workload)?
- What independent variables does it manipulate (automation level, reliability, transparency)?
- Are there **validated scales or instruments** used that could be adapted for PS4/PS5 evaluation?
- Does the paper evaluate **transitions between automation levels** — how users respond when the system changes mode?
- Does the evaluation include any **safety-critical context** (aviation, healthcare, driving, maritime)?

### 8. Applicability to PS4 (Comparative Evaluation of Graduated vs Binary Governance)

Assess how this paper's framework or findings can inform the design of PS4's three-condition comparative evaluation:

- Does it provide theoretical justification for comparing graduated vs binary control?
- Does it suggest specific metrics for measuring the value of an intermediate mode?
- Does it identify what "better" means when comparing automation levels — safer? more consistent? better calibrated trust? higher situational awareness?
- Does it suggest experimental design considerations (sample size, scenario design, control conditions)?
- What specific elements from this paper should be cited when justifying the PS4 evaluation methodology?

### 9. Applicability to PS5 (Socio-Technical Evaluation of CAUTION Mode)

Assess how this paper's framework or findings can inform the design of PS5's user study:

- Does it provide validated instruments for measuring user trust across automation/governance modes?
- Does it provide precedent for evaluating user understanding of intermediate automation states?
- Does it suggest how to measure **trust calibration** — whether users trust the system appropriately for each governance state?
- Does it address how users interpret **system restriction** — do they see restricted AI as less trustworthy, more trustworthy, or differently trustworthy?
- What specific elements from this paper should be cited when justifying the PS5 evaluation methodology?

### 10. Key Concepts and Definitions

List important terms, frameworks, taxonomies, scales, or definitions from this paper that are directly usable in my research. For each:
- The term and its definition
- Where in the paper it is defined (section/page)
- How it maps to my research concepts

### 11. Quotable / Citable Points

List 3–5 specific claims, definitions, or findings from the paper that I could directly cite in my literature review, with their approximate location (section or page). Prioritise:
- Definitions of graduated automation that parallel graduated governance
- Arguments for why binary automation control is insufficient
- Validated measurement approaches for trust or mode understanding
- Findings about user response to intermediate automation states

### 12. Limitations and Gaps

- What are the stated limitations of the paper?
- Does it acknowledge gaps that my research could address — particularly:
  - Application of its framework to AI **governance** (not just automation level)
  - Application to **safety-critical decision support** (not just automation control)
  - Application to **environmental-state-conditioned** governance (not just static levels)
  - Evaluation in **low-resource** or **non-Western** deployment contexts
- What does this paper NOT cover that my research needs?

### 13. Positioning in My Literature Review

- **Role in the argumentative chain**: Which link(s) does this paper support?
  - Link 8: No evaluation compares graduated vs binary governance
  - Link 9: No socio-technical evaluation of user response to CAUTION mode
  - Other link (specify)
- **Role in the literature review**: Choose one or more:
  - Provides **theoretical grounding** for graduated governance as a design choice
  - Provides **validated instruments** for PS4/PS5 evaluation design
  - Provides **empirical precedent** for evaluating intermediate automation/governance modes
  - Provides **design recommendations** for communicating governance state to users
  - Establishes **methodological foundation** that has not yet been applied to AI governance architectures
- **Gap statement**: In one paragraph, explain what this paper provides and what gap remains that my research addresses. Use the format: "This paper establishes [X], but [Y] has not been applied to [Z]. My research extends this by [W]."

### 14. Overall Relevance Score

Rate the paper's relevance to my PhD research:
- ⭐⭐⭐⭐⭐ Core — provides foundational framework or validated instrument directly used in evaluation design
- ⭐⭐⭐⭐ High — provides strong theoretical or methodological grounding for PS4 or PS5
- ⭐⭐⭐ Medium — provides useful background or partial methodological contribution
- ⭐⭐ Low — tangentially related to evaluation methodology
- ⭐ Minimal — limited relevance

---

*Note: If the paper is only partially readable or has limited content visible, extract what is available and flag any gaps.*
