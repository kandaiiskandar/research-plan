# Methodological Foundation Paper Extraction

## Paper: Schrills et al. (2025) — Questioning Trust in AI Research: Exploring the Influence of Trust Assessment on Dependence in AI-Assisted Decision-Making

---

## 1. Paper Identity

- **Full title:** Questioning Trust in AI Research: Exploring the Influence of Trust Assessment on Dependence in AI-Assisted Decision-Making
- **Authors:** Tim Schrills, Thomas Franke, Steffen Hoesterey, Eileen Roesler
- **Year:** 2025 (published online 7 October 2025)
- **Venue:** *Behaviour & Information Technology* (Taylor & Francis — peer-reviewed)
- **DOI:** https://doi.org/10.1080/0144929X.2025.2553153
- **Type:** Preregistered empirical study (2×2 between-subjects experiment, N=149)
- **Citation count:** 2,071 article views (recent publication)
- **Institutional affiliations:** University of Luebeck (Germany), Technische Universität Berlin (Germany), George Mason University (USA)

---

## 2. Core Contribution

- **Problem addressed:** Self-reported trust questionnaires are the dominant method for assessing trust in human-AI interaction (HAII) research. The "question-behaviour effect" (QBE) from social psychology suggests that the act of measuring an attitude can alter subsequent behaviour. If assessing trust changes participants' dependence on AI, this creates a systematic experimental artifact threatening the internal validity of all HAII trust research.
- **Proposed solution:** A preregistered 2×2 between-subjects experiment (N=149) manipulating the *timing* (early vs. late) and *extent* (single-item vs. multi-item TiA scale) of trust assessment, with a no-assessment control group, to test whether trust assessment affects dependence behaviour in an AI-supported pattern recognition task.
- **Key findings:**
  1. **No question-behaviour effect found** — trust assessment did not alter subsequent dependence behaviour regardless of timing or scale length
  2. **Correlations between self-reported trust and behavioural dependence were notably low** — trust assessment was a poor predictor of actual reliance behaviour
  3. **Instructed reliability was the strongest predictor of dependence** — participants matched their agreement with AI recommendations (~78%) to the instructed reliability level (80%), even though the AI was actually 100% correct ("probability matching")
  4. **Dependence increased over time** — higher agreement in block 2 than block 1, independent of trust assessment condition
- **What makes this paper important:** It directly challenges the foundational assumption of HAII trust research — that self-reported trust predicts dependence behaviour. It demonstrates that *instructed reliability* may be more influential than *assessed trust* in shaping user behaviour, with major implications for how PS4/PS5 should conceptualise and measure trust.

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | No | Not addressed — focuses on trust measurement methodology |
| Safety-critical AI decision-making | Partial | References safety-critical contexts (medical, governmental) in motivation but uses abstract pattern recognition task |
| AI governance / control mechanisms | No | Not addressed directly — but findings about instructed reliability influencing behaviour are relevant to how governance state communication shapes user response |
| Low-resource environments | No | UK-based online participants via Prolific |
| Decision architecture formalisation | No | No architectural formalisation |
| Human role in decision-making | Yes | Core focus — examines how humans depend on AI recommendations and what shapes that dependence |
| Socio-technical evaluation | Yes | Directly addresses measurement methodology for human-AI trust evaluation — the methodological validity question underlying PS4/PS5 |
| Coastal fisheries / maritime domain | No | Abstract Kandinsky pattern recognition task |

**Early relevance gate:** This paper has **high methodological relevance** for PS4/PS5 evaluation design. It does not provide theoretical grounding for graduated governance but directly informs *how* to measure trust and dependence validly, warns against assuming self-reported trust predicts behaviour, and identifies instructed/communicated reliability as a key driver of user dependence — directly applicable to how governance state communication in the CAUTION mode shapes user behaviour.

---

## 4. Graduated Automation / Governance Framework

### Does the paper define levels, stages, or grades of automation?

**No.** The paper operates within a single automation level — AI provides a recommendation and the user decides whether to follow it. However, the paper references the broader literature on "varying levels of task allocation between AI and human users" (Paul et al. 2022) and notes that "further research is needed to investigate varied levels of automation and interaction types" (Section 6.3).

### Does the framework distinguish Level 1 from Level 2 governance?

**No.** The AI system is either present (providing recommendations) or absent (baseline condition). There is no concept of restricted AI advisory scope.

### Does the framework include an intermediate mode?

**No.** However, the paper's findings about instructed reliability creating a "probability matching" effect have indirect implications. If users match their dependence to *communicated* system reliability, then communicating that AI is operating under CAUTION (restricted reliability/scope) could directly shape their reliance behaviour — possibly more powerfully than their subjective trust attitudes.

### Mapping to my architecture

| Paper's concept | My architecture's equivalent | Alignment |
|---|---|---|
| Instructed reliability shaping dependence | Governance state communication (SAFE/CAUTION/UNSAFE) | **Partial** — if users match behaviour to communicated system capability, then communicating CAUTION mode should directly calibrate dependence |
| Probability matching (dependence ≈ instructed reliability) | Trust calibration across governance modes | **Partial** — suggests users may calibrate reliance to communicated governance state rather than subjective trust |
| Trust as attitude vs. dependence as behaviour | Trust measurement in PS5 vs. actual reliance in PS4 | **Strong** — PS4/PS5 must measure both attitudinal trust and behavioural dependence separately |

### Does the paper argue graduated control is superior to binary?

**No.** But the probability matching finding implies that *communicating different reliability levels* produces *different dependence levels*. This supports graduated governance: if you communicate three distinct capability states (SAFE/CAUTION/UNSAFE), users should produce three distinct dependence patterns, enabling finer-grained trust calibration than binary (on/off).

---

## 5. Trust, Reliance, and User Response

### Does the paper address human trust in AI systems?

**Yes — this is the paper's central focus**, but from a *methodological validity* perspective rather than a trust factor identification perspective.

### Does it define or operationalise trust?

**Yes.** The paper adopts Lee & See's (2004) definition: trust is an "attitude that an agent will help achieve an individual's goals in a situation characterised by uncertainty and vulnerability" (Section 2.1). The paper emphasises the consensus that trust should be conceptualised as an **attitude** (not a behaviour), meaning it is not directly observable and requires self-report assessment.

The paper makes a critical terminological distinction: it uses "trust *assessment*" rather than "trust *measure*" because most scales in the literature lack sufficient validation to warrant the term "measure" in its strict psychometric sense (citing Razin & Feigh 2024).

### Does it propose or validate a measurement instrument?

**The paper tests rather than proposes instruments.** It uses:

1. **Trust in Automation (TiA) scale** (Jian et al. 2000) — the multi-item condition used this established scale (the most cited trust-in-automation scale)
2. **Single-item trust assessment** — "How much do you trust the system?" on a 6-point Likert scale
3. **Behavioural dependence measures:**
   - **Recommendation agreement** — Cohen's Kappa coefficient measuring agreement between user responses and AI recommendations
   - **Task completion time** — average time per task as behavioural indicator

**Critical finding for PS4/PS5:** The TiA multi-item scale and the single-item trust assessment produced no significant difference in trust values (Section 5.5.5). The correlation between self-reported trust and behavioural dependence was only moderate (r = 0.42–0.45). Neither trust assessment nor perceived reliability significantly improved prediction of dependence beyond the instructed reliability baseline (R² = 0.008, p = .640).

### Does the paper distinguish trust failure types?

**Not formally, but the findings illuminate failure modes:**

- **Overtrust / complacency:** Participants followed AI recommendations ~78% of the time even though baseline performance without AI was only ~62%. They matched dependence to *instructed* reliability (80%) rather than their own capability — a form of anchoring to communicated system properties.
- **Undertrust / disuse:** Some participants rejected correct AI recommendations, possibly due to a "gambler's fallacy" effect — after a series of correct AI recommendations, they expected an incorrect one and proactively disagreed (Section 6.2).
- **Miscalibration:** The gap between instructed reliability (80%), actual reliability (100%), and perceived reliability (~73%) shows systematic miscalibration. Participants underestimated AI performance despite experiencing perfect reliability.

### Application to three governance modes

| Governance mode | Implication from this paper |
|---|---|
| **SAFE** (full AI) | If users anchor dependence to communicated system reliability, communicating "fully reliable" in SAFE mode may create appropriate high dependence — but the paper shows users may still underestimate actual reliability |
| **CAUTION** (restricted AI) | **Key finding:** If communicated reliability shapes dependence more than subjective trust, then clearly communicating CAUTION mode restrictions should directly calibrate user reliance to a reduced level — the mechanism may be more about *information communication* than *trust attitudes* |
| **UNSAFE** (AI disabled) | Users may still expect AI to be available if they've been "instructed" to expect it — transition communication is critical |

---

## 6. Mode Awareness and Automation Surprises

### Does the paper address mode confusion?

**Not directly.** However, the paper's key finding about the "description-experience gap" is closely related. Participants were *told* the AI was 80% reliable but *experienced* 100% reliability. Despite this, most participants (101 of 149) reported perceived reliability at or below 80% — the communicated description overrode actual experience. This is a form of mode unawareness: users failed to perceive the system's actual operating state because the *described* state dominated their perception.

### Does it address automation surprises?

**Indirectly.** The paper references the finding that "trust might decline when automated systems are not reliable enough" (Moray et al. 2000) and that users' expectations can be violated by system errors (Section 1). The probability matching behaviour itself could create automation surprises: if a user expects the AI to be wrong 20% of the time (based on instructed 80% reliability) and the AI is actually always correct, the user may incorrectly reject correct recommendations — a self-generated automation surprise.

### Application to CAUTION mode

The paper's findings generate a specific design principle for CAUTION mode: **what you tell users about the system's capability may matter more than what the system actually does.** If the DSR communicates "AI is operating under restriction in CAUTION mode," users may match their dependence to this communicated restriction even if the restricted AI is still performing well within its limited scope. This means:

1. CAUTION mode communication must accurately describe what the AI *can* do (not just what it *can't* do), to avoid excessive undertrust
2. The restriction description becomes a *reliability anchor* that shapes dependence — it must be carefully calibrated
3. Transitioning from CAUTION to SAFE (or vice versa) will create a new reliability anchor — the transition communication itself shapes subsequent behaviour

---

## 7. Evaluation Methodology

### Experimental design

- **Design:** 2 × 2 between-subjects + control group (5 conditions total)
- **IV 1:** Timing of trust assessment (early: before block 1 / late: before block 2)
- **IV 2:** Extent of trust assessment (single-item / multi-item TiA scale)
- **Control:** No trust assessment
- **N:** 149 participants (Prolific platform, UK residents)
- **Task:** AI-supported pattern recognition using Kandinsky Figures — abstract enough to eliminate domain expertise effects

### Dependent variables

| Variable | Measurement | Purpose |
|---|---|---|
| **Self-reported trust** | TiA scale (Jian et al. 2000) or single-item 6-point Likert | Attitudinal trust assessment |
| **Recommendation agreement** | Cohen's Kappa between user responses and AI recommendations | Behavioural dependence indicator |
| **Task completion time** | Average seconds per task per block | Behavioural effort/deliberation indicator |
| **Perceived reliability** | Post-experiment percentage estimate | Calibration check |
| **Affinity for Technology Interaction (ATI)** | Validated ATI scale (Franke et al. 2019) | Individual difference control variable |
| **Propensity to trust** | Assessed as individual difference | Dispositional trust control |

### Key methodological features adaptable for PS4/PS5

1. **Behavioural dependence measurement via Cohen's Kappa** — directly applicable to PS4. Agreement between user decisions and AI recommendations in each governance mode can be measured as a behavioural trust indicator independent of self-reported trust.

2. **Dual measurement approach (attitudinal + behavioural)** — the paper demonstrates that attitudinal trust (self-report) and behavioural dependence (recommendation agreement) can diverge substantially. PS4/PS5 should measure both independently.

3. **Instructed reliability as experimental manipulation** — for PS4, the governance state (SAFE/CAUTION/UNSAFE) functions similarly to instructed reliability. The paper shows this communication strongly shapes behaviour. PS4 should track whether user dependence matches the communicated governance state.

4. **Pre-registration** — the study was preregistered, establishing methodological credibility. PS4/PS5 should consider pre-registration.

5. **Power analysis** — based on pre-study effect size (η² = 0.038), the authors calculated N=150 needed for 80% power. This provides a concrete sample size benchmark for PS4.

6. **Control group with no assessment** — the inclusion of a no-assessment control group tests whether measurement itself affects behaviour. PS5 could consider a similar design to validate that trust assessment doesn't confound governance mode effects.

### Safety-critical context

**Not directly.** The Kandinsky task is abstract and non-safety-critical. However, the authors acknowledge this limitation and note that "collaborative human-AI tasks involve experienced humans, and expertise can change the result of the interaction" (Section 6.3). This supports the argument that PS4/PS5's safety-critical fisheries context would provide higher ecological validity.

---

## 8. Applicability to PS4 (Comparative Evaluation of Graduated vs Binary Governance)

### Theoretical justification for graduated vs binary comparison

**Indirect but important.** The probability matching finding suggests that users calibrate dependence to communicated system capability. If the DSR communicates three distinct governance states (each with different implied AI capability), users should produce three distinct dependence patterns. This is directly testable in PS4's three-condition design (ungated vs. binary-gated vs. graduated).

### Specific metrics for measuring intermediate mode value

The paper provides concrete metrics:

- **Recommendation agreement (Cohen's Kappa):** Measure in each governance mode across the three PS4 conditions. If graduated governance produces closer alignment between governance mode and dependence than binary governance, this demonstrates calibration value.
- **Task completion time:** Measure as indicator of deliberation effort. If CAUTION mode triggers more careful decision-making (longer completion time) compared to SAFE mode, this demonstrates appropriate mode-responsive behaviour.

### What "better" means

The paper reframes "better" in terms of **calibration accuracy**: does user dependence match the system's actual capability in each mode? The probability matching finding shows users can be reliably anchored to communicated reliability. In PS4, "better" means: does graduated governance produce more appropriate dependence across conditions than binary governance?

### Experimental design considerations

- **N ≈ 150** provides 80% power for between-subjects effects of moderate size (η² ≈ 0.04) — benchmark for PS4
- **Between-subjects design** avoids carryover effects between conditions — relevant for PS4's three-condition comparison
- **Include both self-report and behavioural measures** — the paper's finding that these diverge means PS4 must not rely on self-report alone
- **Include a perceived reliability check** — verify that participants perceive the governance modes as intended
- **Pre-register** the study to establish credibility

### Citable elements for PS4

- Instructed reliability is a stronger predictor of dependence than self-reported trust — supports the argument that governance state communication design is critical for PS4 outcomes
- Cohen's Kappa as a validated behavioural dependence metric — directly adoptable in PS4
- Self-reported trust has low predictive value for actual dependence — justifies measuring both attitudinal and behavioural trust in PS4

---

## 9. Applicability to PS5 (Socio-Technical Evaluation of CAUTION Mode)

### Validated instruments for measuring user trust across governance modes

The paper confirms the **TiA scale (Jian et al. 2000)** as the most cited trust assessment instrument and uses it directly. However, it also demonstrates that single-item and multi-item assessments produce comparable trust values. This is practically useful for PS5: if conducting evaluation with fishers in a field context where survey fatigue is a concern, a single-item trust assessment may be acceptable.

### Precedent for evaluating user understanding of intermediate states

**No direct precedent.** But the description-experience gap finding is directly relevant: users anchored to *described* reliability rather than *experienced* reliability. This suggests that how the CAUTION mode is *described/communicated* to users may be more influential on their behaviour than their actual experience of restricted AI. PS5 should evaluate both what users are told about CAUTION mode and what they actually experience.

### Trust calibration measurement

**Yes — provides a concrete calibration methodology.** The paper measures calibration as the alignment between communicated system capability and user dependence. Extending this to PS5:

- **SAFE mode calibration:** Do users depend on AI at a level appropriate for unrestricted AI?
- **CAUTION mode calibration:** Do users depend on AI at a level appropriate for restricted AI? (Neither overtrusting nor undertrusting the restricted system)
- **UNSAFE mode calibration:** Do users appropriately not depend on AI when it is disabled?

### User interpretation of system restriction

**Not directly addressed**, but the probability matching mechanism predicts that users will *match* their dependence to the *communicated* restriction level. This is testable: does telling users "AI is restricted in CAUTION mode" produce appropriately reduced dependence?

### Citable elements for PS5

- Trust assessment does not alter subsequent behaviour (no QBE) — validates that PS5 can assess trust without confounding behavioural measures
- Self-reported trust and behavioural dependence can diverge — PS5 must measure both
- Instructed reliability shapes dependence more than subjective trust — governance state communication design is critical for PS5
- Single-item and multi-item trust assessments produce comparable results — supports economical assessment in field contexts

---

## 10. Key Concepts and Definitions

| Term | Definition | Location | Mapping to my research |
|---|---|---|---|
| **Trust (Lee & See 2004)** | "Attitude that an agent will help achieve an individual's goals in a situation characterised by uncertainty and vulnerability" | Section 2.1 | Adopted trust definition — same as recommended by Bach et al. (2024) for uncertainty/vulnerability contexts |
| **Dependence** | Behaviour related to following system recommendations (distinct from trust as attitude) | Section 2.1, citing Meyer (2004) | Behavioural measure for PS4 — recommendation agreement across governance modes |
| **Trust assessment vs. trust measure** | "Assessment" preferred over "measure" because most scales lack sufficient validation for the strict psychometric sense of "measure" | Section 2.1, citing Razin & Feigh (2024) | Terminological precision for PS5 methodology description |
| **Question-behaviour effect (QBE)** | The observation that applying a questionnaire can change subsequent behaviour | Section 1 | Methodological concern for PS5 — this paper shows QBE does *not* occur for trust assessment in HAII, validating the use of trust questionnaires in PS5 |
| **Probability matching** | Users match their dependence to the anticipated/communicated system reliability | Section 6.2, citing Bartlett & McCarley (2017) | Predicts that communicating CAUTION mode will anchor user dependence to the communicated restriction level |
| **Description-experience gap** | Discrepancy between how a system is *described* and how it is *experienced*, where description dominates perception | Section 6.2, citing Chen et al. (2018) | Governance state communication design — users may rely more on how CAUTION mode is *described* than on their actual experience of it |
| **Recommendation agreement (Cohen's Kappa)** | Metric quantifying agreement between AI recommendation and user response, accounting for chance agreement | Section 4.5 | Directly adoptable as behavioural dependence metric in PS4 |

---

## 11. Quotable / Citable Points

1. **Trust poorly predicts dependence:** "Correlations between trust and dependence were notably low... our results question the conceptualisation of trust as a general predictor for dependence, especially in comparison to instructed reliability" (Abstract) — supports measuring both attitudinal trust and behavioural dependence independently in PS4/PS5.

2. **Instructed reliability dominates behaviour:** "Instructed reliability appears to be more influential in determining behaviour compared to assessed trust... participants complied with system recommendations depending on the instructed reliability of the system across various conditions" (Section 6.2) — supports the argument that governance state communication shapes user behaviour more than subjective trust, critical for CAUTION mode design.

3. **No question-behaviour effect:** "Assessing trust in participants did not affect their subsequent dependence behaviour" (Section 6.1) — validates that PS5 can use trust questionnaires without confounding behavioural measures.

4. **Scale length doesn't matter for trust values:** "There is no significant difference between the trust values of single- and multi-item assessment groups" (Section 5.5.5) — supports using economical single-item trust assessment in PS5 field contexts where survey fatigue is a concern.

5. **Need for varied automation levels research:** "Further research is needed to investigate varied levels of automation and interaction types to understand how these factors impact trust assessment and dependence" (Section 6.3) — directly supports PS4/PS5's research on trust across three governance modes.

---

## 12. Limitations and Gaps

### Stated limitations

- Abstract Kandinsky task lacks ecological validity — "collaborative human-AI tasks involve experienced humans" (Section 6.3)
- Task complexity may have been too high for participants (60% baseline accuracy)
- AI provided direct recommendations without explanatory information
- Single sequence: AI recommendation shown simultaneously with task stimuli (not before/after user decision)
- Study potentially too short to clearly identify effects over time
- Online (Prolific) sample — participants may have treated perceived reliability question as attention check

### Gaps my research could address

| Gap in this paper | How my research addresses it |
|---|---|
| **Abstract task with no domain expertise** | PS4/PS5 uses a safety-critical fisheries context where users have domain expertise (fishing trip decision-making) |
| **Single automation level** (AI present or absent) | PS4 compares three governance modes (SAFE/CAUTION/UNSAFE) — directly tests trust and dependence across graduated automation/governance levels |
| **No intermediate capability communication** | CAUTION mode communicates restricted-but-active AI — tests whether probability matching extends to intermediate governance states |
| **No safety-critical context** | Coastal fisheries decisions have real safety consequences — vulnerability and uncertainty are ecologically present, not experimentally constructed |
| **No non-Western participants** | PS5 evaluates trust among Malaysian coastal fishers |
| **Online study with no real consequences** | PS5 operates in a context where decisions have genuine safety implications |

---

## 13. Positioning in My Literature Review

### Role in the argumentative chain

- **Link 8 (methodological):** Informs the *design* of PS4's comparative evaluation by providing validated behavioural dependence metrics (Cohen's Kappa), demonstrating the need to measure both attitudinal trust and behavioural dependence, and establishing sample size benchmarks
- **Link 9 (methodological):** Informs PS5 evaluation design by validating that trust questionnaires don't confound behaviour (no QBE), supporting economical single-item assessment, and highlighting that governance state communication may shape behaviour more than subjective trust

### Role in the literature review

- Provides **empirical precedent** for measuring trust and dependence in AI-supported decision tasks
- Provides **validated methodological approach** (TiA scale, Cohen's Kappa, dual attitudinal+behavioural measurement) directly adoptable in PS4/PS5
- Provides **design recommendations** — governance state communication (analogous to instructed reliability) is critical for shaping user behaviour
- Establishes **methodological foundation** showing that trust assessment is valid (no QBE) but insufficient alone — behavioural measures needed

### Gap statement

This paper establishes that self-reported trust assessment does not confound subsequent behaviour (no question-behaviour effect), but that self-reported trust is a poor predictor of behavioural dependence — with instructed reliability being the stronger determinant. However, the study examines only a single automation level (AI fully present with constant reliability) in an abstract non-safety-critical task. My research extends these findings by evaluating trust and dependence across three governance modes (SAFE/CAUTION/UNSAFE), where the communicated governance state functions analogously to instructed reliability, in a safety-critical fisheries context with domain-expert users.

---

## 14. Overall Relevance Score

### ⭐⭐⭐ Medium-High — Provides strong methodological grounding for PS4/PS5 experimental design

**Justification:** This paper doesn't provide theoretical frameworks for graduated governance or trust calibration across automation levels (which would earn ⭐⭐⭐⭐ or ⭐⭐⭐⭐⭐). However, it provides something equally important for evaluation validity: *empirical evidence about what trust assessment can and cannot tell you*. Its contributions to PS4/PS5 design are concrete and actionable:

1. **Validates trust questionnaire use** — no QBE, so PS5 can assess trust without confounding behaviour
2. **Warns against relying on self-reported trust alone** — low correlation with behaviour means PS4 must include behavioural measures
3. **Provides Cohen's Kappa as dependence metric** — directly adoptable
4. **Identifies communicated system capability as the dominant behaviour driver** — directly informs CAUTION mode communication design
5. **Supports single-item trust assessment** — practical for field evaluation in PS5
6. **Provides sample size benchmarks** — N≈150 for 80% power

**Why not ⭐⭐⭐⭐:** The study uses a single automation level in an abstract context. It doesn't evaluate trust across multiple governance/automation modes, doesn't provide a trust calibration framework, and doesn't address safety-critical or field contexts.

**Recommended citation uses:**
- **Primary citation** when justifying dual measurement (attitudinal + behavioural) in PS4/PS5
- **Primary citation** for Cohen's Kappa as behavioural dependence metric
- **Supporting citation** when arguing that governance state communication (CAUTION mode description) directly shapes user dependence
- **Supporting citation** when validating that trust questionnaires don't confound experimental behaviour
- **Methodological reference** for sample size planning and between-subjects design in PS4

---

## Post-Extraction Commentary

### Strategic Assessment

This paper's value is primarily **methodological and cautionary** rather than theoretical. Its core message for your work: *don't assume that measuring trust tells you how people will actually behave with your system.* This has three concrete implications for your evaluation design:

**First, PS4 must include behavioural dependence measures, not just trust questionnaires.** The paper shows that self-reported trust explains very little variance in actual reliance behaviour (R² < 0.01 for predicting recommendation agreement). If PS4 only measures self-reported trust across the three governance conditions, it may find trust differences but miss the more important question: *do users actually behave differently across governance modes?* Cohen's Kappa on recommendation agreement is a clean, validated way to capture this.

**Second, the "probability matching" finding is directly applicable to CAUTION mode.** If users anchor dependence to communicated system capability, then the *way you communicate CAUTION mode* becomes a design variable with measurable behavioural consequences. PS5 should treat CAUTION mode communication design as an experimental factor, not just a transparency feature.

**Third, the finding that scale length doesn't significantly affect trust values is practically useful for field evaluation.** In a Malaysian coastal fishing community, administering a 12-item TiA scale after every scenario may cause survey fatigue. This paper's evidence that a single-item trust assessment produces comparable values supports an economical approach.

### Score Rationale Relative to Prior Papers

At ⭐⭐⭐, this sits between the broad-but-shallow trustworthiness survey of Nastoska et al. (2025) [⭐⭐] and the comprehensive trust factor taxonomy of Bach et al. (2024) [⭐⭐⭐⭐]. It provides deeper methodological insight than Nastoska et al. but is narrower in scope than Bach et al. Its unique contribution is the *empirical validation of measurement methodology* — something no other paper in your extraction set provides.

### Recommended Next Steps

This paper strengthens the case for extracting these methodological foundations:

1. **Lee & See (2004)** — the canonical trust definition and trust-dependence model that this paper both uses and challenges. Essential for understanding the theoretical relationship between trust attitude and reliance behaviour.
2. **Hoff & Bashir (2015)** — "Trust in Automation: Integrating Empirical Evidence on Factors That Influence Trust." Comprehensive trust factor model referenced extensively here.
3. **Kohn et al. (2021)** — "Measurement of Trust in Automation: A Narrative Review and Reference Guide." The most comprehensive review of trust assessment methods, cited repeatedly in this paper. Would provide the complete methodological landscape for PS5 instrument selection.
