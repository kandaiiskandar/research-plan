# Methodological Foundation Paper Extraction

## Paper: McGrath et al. (2025) — Collaborative Human-AI Trust (CHAI-T): A Process Framework for Active Management of Trust in Human-AI Collaboration

---

## 1. Paper Identity

- **Full title:** Collaborative Human-AI Trust (CHAI-T): A Process Framework for Active Management of Trust in Human-AI Collaboration
- **Authors:** Melanie J. McGrath, Andreas Duenser, Justine Lacey, Cécile Paris
- **Year:** 2025 (published online 26 August 2025)
- **Venue:** *Computers in Human Behavior: Artificial Humans*, 6, 100200 (Elsevier — peer-reviewed, open access)
- **DOI:** https://doi.org/10.1016/j.chbah.2025.100200
- **Type:** Theoretical framework paper — proposes a process framework (CHAI-T) for trust in collaborative human-AI teams, drawing on psychological and computer science literature
- **Institutional affiliation:** CSIRO (Australia's national science agency)
- **Funding:** No specific external grant

---

## 2. Core Contribution

- **Problem addressed:** Existing models of trust in automation/AI account for antecedents and moderators of trust but fail to: (1) account for the specificity of task contexts and goals, (2) integrate processes of team interaction, and (3) capture how trust evolves over time — all requirements identified by the US National Academies of Sciences for HAI teaming.
- **Proposed solution:** The CHAI-T (Collaborative Human-AI Trust) framework, which adopts the established tripartite structure of trust antecedents (human factors, technology factors, context factors) but embeds them within an IMOI (Inputs-Mediators-Outputs-Inputs) process model of teaming. Trust is positioned as a **mediator** (not an outcome) between team inputs and outputs, with team processes operating reciprocally with trust across recurring performance episodes.
- **Key features:**
  1. **Context specificity** — not a one-size-fits-all model but a *framework* for specifying context-specific trust models
  2. **Team processes** — incorporates a taxonomy of 10 team processes (from Marks et al. 2001) as mechanisms through which inputs are converted to trust and outputs
  3. **Temporal dynamics** — recurring performance episodes where outputs from one cycle become inputs to the next, capturing trust evolution over time
  4. **Active trust management** — the framework enables identification of factors that increase/decrease trust and supports trust calibration
  5. **Optimal trust ≠ maximal trust** — explicitly states that the goal is calibrated trust aligned with actual system capabilities, not maximum trust

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | No | Framework is agnostic to AI architecture type |
| Safety-critical AI decision-making | Partial | References healthcare, autonomous driving, monitoring/anomaly detection — but safety-criticality is not the primary organising principle |
| AI governance / control mechanisms | Partial | Trust calibration framework implicitly addresses governance — calibrated trust means user expectations align with system capabilities, which is the goal of governance state communication |
| Low-resource environments | No | Not addressed — examples are from well-resourced scientific and institutional contexts |
| Decision architecture formalisation | No | No formal computational architecture — CHAI-T is a conceptual process framework |
| Human role in decision-making | Yes | Central — positions the human as a collaborative team member whose trust mediates team performance |
| Socio-technical evaluation | Yes | The IMOI framework is inherently socio-technical; trust is positioned as emergent from the interaction of human, technology, and contextual factors through team processes |
| Coastal fisheries / maritime domain | No | Not addressed |

**Early relevance gate:** This paper has **high relevance** for PS5's evaluation design and for the broader conceptual framing of trust in the DSR architecture. Its positioning of trust as a *mediator* (not an outcome), its emphasis on *trust calibration* (not trust maximisation), its incorporation of *temporal dynamics*, and its insistence on *context specificity* all align strongly with the evaluation needs of the CAUTION mode.

---

## 4. Graduated Automation / Governance Framework

### Does the paper define levels, stages, or grades of automation?

**No explicit levels.** However, the paper implicitly recognises graduated capability through its contextual framing. It distinguishes collaborative HAI teaming from "traditional forms of AI" and from full automation, positioning collaboration as an intermediate paradigm where AI and human have complementary but bounded roles. The framework's insistence that trust must be calibrated to *actual system capabilities* implies that different capability levels require different trust calibrations.

### Does the framework distinguish Level 1 from Level 2 governance?

**Not directly.** But the CHAI-T framework's structure is compatible with this distinction:
- **Level 1 (participation)** maps to whether the AI agent is a member of the team at all (the definitional criteria for HAI teaming require at least one AI agent)
- **Level 2 (advisory scope)** maps to what the AI agent's role is within the team — the framework explicitly notes that team roles, capabilities, and interdependencies are context-specific inputs

### Does the framework include an intermediate mode?

**Not as a discrete mode**, but the framework's temporal dynamics and performance episodes accommodate mode transitions naturally. The IMOI cycle means that trust calibration can shift across episodes as system capabilities or context change. The paper notes that "the factors that contribute to trust in an embodied robot, for example, are likely to be different to the factors relevant to the formation of trust in an algorithm" — extending this logic, the factors contributing to trust in SAFE-mode AI are likely different from those in CAUTION-mode AI.

### Mapping to my architecture

| Paper's concept | My architecture's equivalent | Alignment |
|---|---|---|
| Trust as mediator (not outcome) | Trust as mediating variable between governance state communication and user decision behaviour | **Strong** — both frameworks position trust as a means to an end, not an end in itself |
| Optimal trust ≠ maximal trust | Trust calibration across SAFE/CAUTION/UNSAFE | **Strong** — CAUTION mode requires users to trust AI *appropriately for its restricted capabilities*, not maximally |
| Context-specific trust "recipe" | Environmental state E conditioning governance | **Partial** — CHAI-T's context specificity is about choosing relevant antecedent factors; DSR's context specificity is about runtime state classification |
| Performance episodes with feedback loops | Fishing trip decision cycles across varying environmental conditions | **Strong** — each fishing trip decision is a performance episode where governance state, trust, and decision outcome feed back into the next cycle |
| Team processes (monitoring, coordination, communication) | Human-AI interaction during governance-state-conditioned decision support | **Partial** — CHAI-T's team processes could structure how fisher-AI interaction quality is evaluated across governance modes |
| Tripartite antecedents (human, technology, context) | PS5 evaluation dimensions | **Strong** — directly usable as PS5's evaluation structure |

### Does the paper argue graduated control is superior to binary?

**Not explicitly.** But the paper's core argument that trust must be calibrated to system capabilities, combined with its insistence that different contexts require different trust "recipes," strongly implies that a system with multiple operational modes (graduated governance) requires multiple trust calibrations — something binary governance cannot achieve.

The paper states: "Trust in a machine system is considered to have reached its optimal level and, consequently, best facilitate performance outcomes, when the human trustor's expectations are aligned with the capabilities of system" (Section 3.2, citing Jacovi et al. 2021; Schaefer et al. 2020). If capabilities change across governance states, optimal trust must also change — requiring graduated trust management.

### Does the paper identify risks of binary trust/automation control?

**Yes, explicitly:**

- **Overtrust (exceeding optimal level):** "When optimal levels of trust are exceeded, that is, when humans expect more of a system than its capabilities warrant, the resulting overreliance and lack of monitoring can have catastrophic outcomes" (Section 3.2)
- **Undertrust (failing to reach optimal level):** "A failure to reach optimal levels of trust, on the other hand, can result in disuse of technological systems, representing a waste of time and resources" (Section 3.2, citing Parasuraman & Riley 1997)

This directly supports the DSR's CAUTION mode rationale: if the system shifts from SAFE to CAUTION but trust is not recalibrated, either overtrust (expecting full AI capability from restricted AI) or undertrust (rejecting all AI because it's restricted) will result.

---

## 5. Trust, Reliance, and User Response

### Does the paper address human trust in AI systems?

**Yes — trust is the central construct.** The paper provides a comprehensive review of trust definitions, synthesising convergence across multiple foundational sources (Table 1) into five key features: (a) expectation/belief, (b) specific subject, (c) future actions, (d) positive outcomes, (e) risk/vulnerability.

### Does it define or operationalise trust?

**Yes.** The paper synthesises seven canonical trust definitions (Table 1) including Mayer et al. (1995), Lee & See (2004), Rotter (1967), Rousseau (1998), and others, identifying convergence on the five features above.

It also clearly distinguishes:
- **Trust** = an attitude or expectation of the trustor
- **Trustworthiness** = a characteristic of the trustee signalling it may be trusted
- **Reliance** = a behavioural outcome of trust (not trust itself)

This tripartite distinction (trust ≠ trustworthiness ≠ reliance) is critical for PS5: trust is the attitude being evaluated, trustworthiness is what the governance architecture design aims to project, and reliance is the behavioural outcome that PS4 measures.

### Does it propose or validate a measurement instrument?

**No specific instrument is proposed.** However, the paper identifies the measurement challenge explicitly and recommends:
- **Psychometrically validated self-report scales** for trust attitude
- **Multi-method approaches** combining self-report, behavioural, and potentially physiological measures
- **Methods that are "cheap, frequent, and stealthy"** for capturing temporal dynamics (citing Kozlowski 2015)
- **Context-adapted measurement** — selection of measures must be adapted to the specific task and domain

The paper references its own concurrent work on validating an established trust scale and its short form (McGrath, Lack et al. 2025 — in *Frontiers in Artificial Intelligence*), and on using conjoint analysis for trust-sensitive design (McGrath, Cooper et al. 2025).

### Does the paper distinguish trust failure types?

**Yes, through the trustworthiness dimensions:**

The paper maps Mayer et al.'s (1995) interpersonal trustworthiness dimensions to Lee & See's (2004) automation-specific dimensions:

| Interpersonal (Mayer et al.) | Automation (Lee & See) | Trust failure mode |
|---|---|---|
| **Ability** (competence, expertise) | **Performance** (reliability, accuracy, predictability) | Undertrust when system performs well but user doesn't recognise it; overtrust when system performs poorly |
| **Integrity** (adherence to principles) | **Process** (system's fit to situation and goals) | Mode confusion — user trusts system's process when it's operating outside its appropriate scope |
| **Benevolence** (trustee's good intentions) | **Purpose** (designer's intent) | Misuse — user trusts system purpose is aligned with their goals when it isn't |

The paper also adds two additional trustworthiness dimensions from Breuer et al. (2020):
- **Predictability** — consistency/regularity of behaviour (distinct from ability)
- **Transparency** — clear and open sharing of information

Both are directly relevant to CAUTION mode: the mode must be *predictable* (consistent restriction logic) and *transparent* (clear communication of what restrictions apply and why).

### Application to three governance modes

| Governance mode | CHAI-T trust calibration requirement |
|---|---|
| **SAFE** | Optimal trust = high but not maximal; user expectations aligned with full AI capabilities. Risk: overtrust leading to reduced monitoring |
| **CAUTION** | Optimal trust = moderate; user expectations aligned with *restricted* AI capabilities. Trust must be recalibrated from SAFE level. The restriction itself is a trust-relevant characteristic (performance dimension). Risk: either overtrust (expecting full capability) or undertrust (rejecting restricted AI entirely) |
| **UNSAFE** | Optimal trust = trust in the safety classification function rather than in AI recommendations (which are absent). Risk: undertrust in the classification leading to unsafe behaviour |

---

## 6. Mode Awareness and Automation Surprises

### Does the paper address mode confusion?

**Indirectly through trust calibration.** The paper frames the trust calibration problem as aligning expectations with capabilities. When a system changes modes (e.g., SAFE → CAUTION), the user's expectations must be updated. If they are not, the user is operating with miscalibrated trust — functionally equivalent to mode confusion.

The paper identifies **performance episodes** as the unit of trust dynamics. Each episode has inputs, processes, and outputs that feed into the next cycle. A governance mode transition is a disruption between performance episodes — the CHAI-T framework predicts that trust antecedents and processes must be reconfigured at the transition point.

### Does it address automation surprises?

**Yes, through the predictability dimension of trustworthiness.** Breuer et al.'s (2020) identification of predictability as a trust dimension distinct from ability means that even a highly capable system can erode trust if it behaves unpredictably. A governance mode transition (SAFE → CAUTION → UNSAFE) is inherently a predictability challenge: the system's capabilities change, and if the change is not predicted by the user, trust is threatened.

### Application to CAUTION mode

The CHAI-T framework generates specific design principles for CAUTION mode:

1. **Trust must be actively recalibrated at SAFE→CAUTION transitions.** The IMOI feedback loop means that trust built during SAFE mode performance episodes will carry into CAUTION mode as an input. If not explicitly recalibrated, this inherited trust will be miscalibrated for the restricted capabilities.

2. **Team processes must support recalibration.** The framework identifies "monitoring progress towards goals" and "team monitoring and back-up behavior" as team processes that enable trust calibration. For CAUTION mode, this means the system must communicate what goals remain achievable under restriction and what monitoring the human should perform.

3. **Transparency has a specific role in CAUTION mode.** The paper notes that transparency's effect on trust is not straightforward — it can increase trust but also reduce it when it reveals limitations. In CAUTION mode, transparency about restrictions serves *calibration* (aligning expectations with reduced capabilities), which may reduce absolute trust level but improve trust *appropriateness*.

---

## 7. Evaluation Methodology

### Does the paper describe an evaluation method?

**The paper is primarily theoretical**, but it provides a detailed methodology for *applying* the CHAI-T framework to specific contexts:

1. **Develop a comprehensive profile** of the HAI team and task (goals, risk profile, performance episodes, user types, desired outputs, relevant team processes)
2. **Cross-reference** key application characteristics with empirically verified trust antecedents from the literature (citing Saßmannshausen et al. 2022's index of 470+ antecedent factors)
3. **Enter identified antecedents into an IMOI model** and subject to hypothesis testing
4. **Empirically verify** the contribution of input factors to trust, and test the role of team processes in trust development
5. **Test optimal trust levels** for desired outcomes and identify design features necessary to achieve and maintain them

### Measurement approaches recommended

The paper recommends:
- **Psychometrically validated self-report scales** (citing McGrath, Lack et al. 2025 for a validated scale and short form)
- **Behavioural indicators** (reliance patterns, monitoring behaviours)
- **Physiological measures** (with the caveat that what they capture is unclear — citing Kohn et al. 2021)
- **Experience sampling methods** for temporal dynamics
- **Behavioural sensors or video observations**
- **Computational modelling** for process dynamics

### Experimental design considerations for PS4/PS5

The paper suggests:
- **Define performance episodes** for the target application — for the DSR, each fishing trip decision is a performance episode
- **Identify context-specific trust antecedents** — for PS5, which human factors (fisher experience, technical literacy), technology factors (governance state communication, recommendation type), and context factors (sea conditions, economic pressure) influence trust
- **Measure trust at multiple time points** within and across episodes to capture temporal dynamics
- **Use conjoint analysis** (citing McGrath, Cooper et al. 2025) to determine relative importance of trust antecedent factors

---

## 8. Applicability to PS4 (Comparative Evaluation of Graduated vs Binary Governance)

### Theoretical justification for graduated vs binary comparison

**Strong.** The paper's central argument that optimal trust requires alignment between expectations and capabilities, combined with the IMOI model's capacity for different trust configurations across performance episodes, directly supports the argument that:
- Binary governance (AI on/off) produces only two trust calibration points
- Graduated governance (SAFE/CAUTION/UNSAFE) produces three calibration points, enabling finer-grained trust management
- The intermediate CAUTION state specifically addresses the trust calibration challenge at the boundary between acceptable and unacceptable AI participation

### Specific metrics

The paper identifies trust calibration as the key metric: the degree to which user expectations align with system capabilities. For PS4, this translates to: does graduated governance produce better trust calibration (closer expectation-capability alignment) across conditions than binary governance?

### Citable elements for PS4

- "Trust in a machine system is considered to have reached its optimal level... when the human trustor's expectations are aligned with the capabilities of system" — defines the evaluation criterion for PS4
- Overtrust and undertrust as calibration failures — provides the theoretical vocabulary for PS4's dependent variables
- IMOI framework for structured comparison of trust dynamics across governance conditions

---

## 9. Applicability to PS5 (Socio-Technical Evaluation of CAUTION Mode)

### Validated instruments

**Not directly provided**, but the paper references concurrent work (McGrath, Lack et al. 2025) on validating a trust scale and short form, and recommends multi-method measurement.

### Precedent for evaluating intermediate states

**Not as a discrete study**, but the CHAI-T framework's temporal dynamics and performance episodes provide the theoretical structure for evaluating trust across governance mode transitions. The framework predicts that trust inherited from SAFE mode episodes will be miscalibrated for CAUTION mode — PS5 can test this prediction.

### Trust calibration measurement

**Yes — this is the framework's key contribution to PS5.** The concept of optimal trust as expectation-capability alignment provides a direct operationalisation: measure user expectations of AI capability in each governance mode, compare to actual capability, and quantify the gap as a calibration metric.

### User interpretation of system restriction

**Addressed through trustworthiness dimensions.** System restriction in CAUTION mode affects:
- **Performance** dimension — AI's reliability/accuracy changes (restricted recommendation types)
- **Process** dimension — AI's fit to situation changes (operating under environmental-state-conditioned restriction)
- **Predictability** dimension — AI's behaviour changes from previous mode
- **Transparency** dimension — restriction must be clearly communicated

### Citable elements for PS5

- Trust as mediator, not outcome — frames PS5's measurement approach
- Optimal trust ≠ maximal trust — defines the evaluation criterion
- Tripartite antecedent structure (human, technology, context) as PS5's evaluation framework
- Team processes taxonomy as a structure for evaluating human-AI interaction quality across governance modes
- Temporal dynamics via performance episodes — supports repeated-measures design across fishing trip decision cycles

---

## 10. Key Concepts and Definitions

| Term | Definition / Description | Location | Mapping to my research |
|---|---|---|---|
| **Trust (convergent definition)** | An expectation/belief that a specific subject will perform future actions with positive outcomes in situations of risk/vulnerability | Table 1 | Canonical trust definition synthesis — usable as conceptual grounding for PS5 |
| **Trustworthiness (Mayer et al. 1995)** | Perceived ability, benevolence, integrity of the trustee | Section 2.1 | What the DSR architecture must project through governance state communication |
| **Trustworthiness (Lee & See 2004, automation)** | Performance, process, purpose — automation-specific recast | Section 2.2 | Directly applicable: performance = AI accuracy, process = governance mechanism fit, purpose = designer intent |
| **Trust calibration** | Alignment of human expectations with actual system capabilities; optimal trust ≠ maximal trust | Section 3.2 | The core evaluation criterion for PS4/PS5 — does graduated governance produce better-calibrated trust? |
| **Performance episode** | A distinguishable period over which performance accrues and feedback is available | Section 3.4, citing Marks et al. 2001 | Each fishing trip decision = a performance episode in the CHAI-T sense |
| **IMOI model** | Inputs-Mediators-Outputs-Inputs — cyclical process model where outputs feed back as inputs | Section 3.1 | Framework for modelling trust dynamics across governance mode transitions |
| **Team processes (taxonomy)** | 10 processes: mission analysis, goal specification, strategy/planning, monitoring progress, systems monitoring, team monitoring/back-up, coordination, conflict management, motivation/confidence building, affect management | Table 2, from Marks et al. 2001 | Subset applicable to PS5: monitoring progress, team monitoring, coordination |
| **Predictability (trustworthiness dimension)** | Consistency or regularity of behaviour, distinct from ability | Section 2.1, citing Breuer et al. 2020 | CAUTION mode must behave predictably — consistent restriction logic across encounters |
| **Transparency (trustworthiness dimension)** | Clear and open sharing of information | Section 2.1, citing Breuer et al. 2020 | Governance state communication — CAUTION mode must transparently communicate restrictions |

---

## 11. Quotable / Citable Points

1. **Optimal trust ≠ maximal trust:** "Trust in a machine system is considered to have reached its optimal level and, consequently, best facilitate performance outcomes, when the human trustor's expectations are aligned with the capabilities of system. When optimal levels of trust are exceeded... the resulting overreliance and lack of monitoring can have catastrophic outcomes" (Section 3.2) — defines the trust calibration criterion for PS4/PS5.

2. **Context-specific trust recipes:** "Each of these applications requires its own 'recipe' for trust, and each of these recipes may work best with particular ingredients" (Section 3.2) — supports the argument that different governance states require different trust configurations.

3. **470+ antecedent factors identified:** "With more than 470 distinct antecedents to trust in AI identified in the literature, the pantry of ingredients is so large that models may become bloated or lack ecological validity if they attempt to include all possible antecedent factors" (Section 3.2, citing Saßmannshausen et al. 2022) — justifies PS5's focused selection of context-relevant trust antecedents.

4. **Trust as mediator, not endpoint:** "The positioning of trust as a mediator in an IMOI model clarifies the role of trust as a means to an end — whether that be increased reliance, adoption, or performance — not an end in itself" (Section 3.2) — frames PS5's measurement approach.

5. **Transparency's complex relationship with trust:** "While transparency may foster trust under some circumstances, at other times greater transparency may interact with human cognitive capacity to ultimately reduce trust" (Section 4, citing Dikmen & Burns 2022) — relevant to CAUTION mode design: transparency about restrictions may reduce absolute trust but improve calibration.

---

## 12. Limitations and Gaps

### Stated limitations

- The framework is deliberately theoretical — it has not been empirically validated
- Human teaming processes may not be meaningfully transposable to HAI contexts
- The framework requires detailed contextual profiling for each application, which demands significant effort
- No specific measurement instruments are prescribed

### Gaps my research could address

| Gap in this paper | How my research addresses it |
|---|---|
| **No empirical validation** | PS4/PS5 empirically evaluates trust dynamics in a specific collaborative HAI context (fisheries decision support) |
| **No graduated governance modes** — framework is agnostic to automation level | The DSR's three governance states (SAFE/CAUTION/UNSAFE) provide a concrete instantiation of the need for context-specific trust calibration across different system capability configurations |
| **No safety-critical environmental context** | Coastal fisheries decisions involve genuine safety risk — the vulnerability and uncertainty conditions for trust are ecologically present |
| **No low-resource or non-Western context** | PS5 in Malaysian coastal communities tests whether the framework's assumptions hold in non-Western, low-resource settings |
| **No intermediate mode trust calibration** | The CAUTION mode is precisely the trust calibration challenge the framework identifies — expectations must be realigned with restricted capabilities |
| **Trust calibration not operationally measured** | PS4/PS5 can operationalise trust calibration as the gap between user expectations of AI capability in each governance mode and actual AI capability |

---

## 13. Positioning in My Literature Review

### Role in the argumentative chain

- **Link 9 (directly):** Provides the theoretical framework for evaluating trust calibration across governance modes in PS5. The CHAI-T framework's concepts of optimal trust, trust calibration, and performance episodes structure how PS5 evaluates user response to the CAUTION mode.
- **Link 8 (supporting):** The framework's argument that different contexts require different trust configurations supports the claim that graduated governance (three trust calibration points) is superior to binary governance (two calibration points).

### Role in the literature review

- Provides **theoretical grounding** for trust calibration as the evaluation criterion (not trust maximisation)
- Provides **conceptual framework** (IMOI, performance episodes, tripartite antecedents) for structuring PS5's evaluation design
- Provides **design recommendations** for how team processes (monitoring, coordination, communication) should support trust calibration — applicable to CAUTION mode interaction design
- Establishes **methodological foundation** for context-specific trust model specification — PS5 instantiates this for the fisheries decision support context

### Gap statement

This paper establishes that trust in collaborative human-AI systems requires context-specific models that account for task specificity, interaction processes, and temporal dynamics, with trust calibration (expectation-capability alignment) as the key evaluation criterion rather than trust maximisation. However, the framework is entirely theoretical — it has not been empirically validated, it does not address systems with multiple runtime governance modes, and it has not been applied to safety-critical, low-resource, or non-Western contexts. My research provides an empirical instantiation of this framework by evaluating trust calibration across three runtime governance modes (SAFE/CAUTION/UNSAFE) in a safety-critical coastal fisheries context, where each fishing trip decision functions as a performance episode within the CHAI-T IMOI structure.

---

## 14. Overall Relevance Score

### ⭐⭐⭐⭐ High — Provides strong theoretical grounding for PS5 evaluation design

**Justification:** The CHAI-T framework provides the most comprehensive and theoretically sophisticated process model of trust in human-AI collaboration that you've extracted so far. Its contributions to your evaluation design are substantial:

1. **Trust calibration as the evaluation criterion** — the single most important conceptual contribution. PS4/PS5 should evaluate whether governance modes produce *appropriately calibrated* trust, not whether they produce *more* trust.
2. **IMOI structure for evaluation design** — performance episodes, feedback loops, and temporal dynamics provide the structural framework for repeated-measures evaluation across fishing trip decisions.
3. **Tripartite antecedent structure** — human factors, technology factors, and context factors provide a disciplined structure for selecting PS5's evaluation variables.
4. **Trust as mediator** — positions trust measurement as a means to understanding decision behaviour (the actual outcome of interest), not as an endpoint.
5. **Synthesis of canonical trust definitions** — Table 1 provides a definitive reference for the convergent features of trust across multiple foundational sources.

**Why not ⭐⭐⭐⭐⭐:** The framework is purely theoretical with no empirical validation. It does not provide validated measurement instruments (needed from Lee & See 2004, Jian et al. 2000, or Gulati et al. 2019). It does not address graduated automation/governance modes or safety-critical environmental contexts. The canonical sources it synthesises (Mayer et al. 1995; Lee & See 2004; Hoff & Bashir 2015) remain the primary foundations — CHAI-T integrates and extends them rather than replacing them.

**Recommended citation uses:**
- **Primary citation** when defining trust calibration as PS5's evaluation criterion (optimal trust = expectation-capability alignment)
- **Primary citation** when framing PS5 within an IMOI structure of performance episodes
- **Primary citation** for the argument that different system capability configurations require different trust "recipes"
- **Supporting citation** for trust as mediator (not outcome) in the evaluation framework
- **Supporting citation** for the tripartite antecedent structure of PS5's evaluation dimensions

---

## Post-Extraction Commentary

### Strategic Assessment

This paper is the strongest *theoretical* framework paper you've extracted for the methodological foundation layer. Where Bach et al. (2024) gives you the empirical landscape and instrument catalogue, and Schrills et al. (2025) gives you measurement validity insights, McGrath et al. (2025) gives you the *conceptual architecture* for your evaluation design. Together, these three papers form a coherent methodological triad:

| Paper | Contribution to PS4/PS5 | Rating |
|---|---|---|
| **Bach et al. (2024)** | What to measure (trust definitions, instruments, influencing factors) | ⭐⭐⭐⭐ |
| **Schrills et al. (2025)** | How measurement works (trust-dependence relationship, behavioural metrics, QBE validation) | ⭐⭐⭐ |
| **McGrath et al. (2025)** | Why and when to measure (trust calibration criterion, IMOI structure, temporal dynamics, context specificity) | ⭐⭐⭐⭐ |

### Score Rationale Relative to Prior Papers

At ⭐⭐⭐⭐, this ties with Bach et al. (2024) as the most relevant methodological paper. It provides theoretical depth where Bach provides empirical breadth. The two are complementary: Bach tells you *what* the field has done; McGrath tells you *how to think about* what the field should do next.

### The Trust Calibration Concept Is Your PS5 Evaluation Criterion

This is the single most important conceptual takeaway. Your PS5 evaluation question is not "do users trust the CAUTION mode?" (which could be answered by a simple trust score comparison). The question is: "do users trust the CAUTION mode *appropriately* — that is, are their expectations aligned with the AI's actual restricted capabilities?" This reframes the evaluation from a trust magnitude comparison to a trust calibration assessment, which is both more informative and more defensible.

Operationally, this means PS5 should measure:
1. **User expectation of AI capability** in each governance mode (what do they think the AI can/will do?)
2. **Actual AI capability** in each governance mode (what can the AI actually do?)
3. **Trust calibration gap** = discrepancy between 1 and 2
4. **Behavioural calibration** = does actual reliance behaviour match the governance mode's intended reliance pattern?

### Recommended Remaining Extractions

Your methodological foundation layer is now strong. The remaining priority extractions are the canonical *primary sources* that all these papers reference:

1. **Lee & See (2004)** — "Trust in Automation: Designing for Appropriate Reliance." *Human Factors*. The single most-cited paper across all four of your methodological extractions. Would likely score ⭐⭐⭐⭐⭐.
2. **Hoff & Bashir (2015)** — "Trust in Automation: Integrating Empirical Evidence." *Human Factors*. The three-layer trust model (dispositional, situational, learned) that CHAI-T explicitly builds upon.
3. **Parasuraman, Sheridan & Wickens (2000)** — "A Model for Types and Levels of Human Interaction with Automation." The graduated automation levels framework that would provide direct theoretical grounding for why graduated governance is a valid design choice.
