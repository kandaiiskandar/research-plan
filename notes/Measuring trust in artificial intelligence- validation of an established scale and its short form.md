# Methodological Foundation Paper Extraction

## Paper: McGrath et al. (2025) — Measuring Trust in AI: Validation of TIAS and S-TIAS

---

## 1. Paper Identity

- **Full title**: Measuring trust in artificial intelligence: validation of an established scale and its short form
- **Authors**: Melanie J. McGrath, Oliver Lack, James Tisch, Andreas Duenser
- **Year**: 2025
- **Publication venue**: *Frontiers in Artificial Intelligence*, 8:1582880
- **DOI**: 10.3389/frai.2025.1582880
- **Type of paper**: Empirical instrument validation (psychometric study across four studies)
- **Open access**: Yes (CC BY)
- **Received / Accepted / Published**: 25 Feb 2025 / 11 Apr 2025 / 09 May 2025

---

## 2. Core Contribution

- **Problem addressed**: The Trust in Automation Scale (TIAS; Jian et al., 2000) is the most widely used self-report measure of trust in automated systems, yet it had never been subjected to comprehensive psychometric validation. Additionally, at 12 items it is impractical for contexts requiring frequent, minimally disruptive measurement — precisely the contexts needed to study trust dynamics, calibration, and trajectories over time.
- **Proposed solution / key finding**:
  1. Conducted comprehensive psychometric validation of the 12-item TIAS across four studies, testing sensitivity to trustworthiness manipulations (performance and integrity), convergent validity (with human trust propensity and machine trust propensity), and predictive validity (predicting behavioural intention to rely on AI).
  2. Developed and validated a **3-item Short Trust in Automation Scale (S-TIAS)** comprising items: "I am confident in the AI assistant," "The AI assistant is reliable," and "I can trust the AI assistant." The S-TIAS demonstrated comparable reliability (α = 0.97), sensitivity, convergent validity, and predictive validity to the full TIAS.
- **What makes it foundational**: Provides the first rigorous psychometric validation of the field's most-used trust-in-automation scale, and delivers a validated short form that enables repeated trust measurement within experimental sessions — a prerequisite for studying trust dynamics across changing system states.

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | No | Paper does not address AI architecture types |
| Safety-critical AI decision-making | Partial | One vignette involves a self-driving car; another a medical diagnostic app. Trust calibration framed as safety concern (overtrust → misuse; undertrust → disuse) |
| AI governance / control mechanisms | No | Does not address governance architectures or gating mechanisms |
| Low-resource environments | No | All studies US-based Prolific samples |
| Decision architecture formalisation | No | No formal architectural notation |
| Human role in decision-making | Yes | Central focus: human trust as mediator of willingness to rely on AI recommendations |
| Socio-technical evaluation | Yes | Provides validated instrument and methodology for measuring trust as dependent variable in human–AI interaction evaluation |
| Coastal fisheries / maritime domain | No | No domain overlap |

---

## 4. Graduated Automation / Governance Framework

### Does the paper define levels, stages, or grades of automation, autonomy, or system control?

**No.** The paper does not propose or test a graduated automation taxonomy. It operates within a binary trustworthiness manipulation paradigm (high vs low performance; high vs low integrity). The system is either trustworthy or not — there is no intermediate condition.

### Does it distinguish between "system participates at all" (Level 1) and "what the system is allowed to do" (Level 2)?

**No.** The paper assumes the AI system is always active; the question is whether the user trusts and relies on its output. There is no governance gate controlling AI participation or scope.

### Does it include an intermediate mode analogous to CAUTION?

**No.** The experimental design is strictly two-condition (high/low trustworthiness). There is no "medium trustworthiness" or "restricted system" condition.

### Mapping to my three-mode governance model

| Paper's concept | My architecture's equivalent | Alignment |
|---|---|---|
| High-trustworthiness condition | SAFE state (AI fully enabled, user trusts fully) | Partial — analogous in terms of expected user trust level, but no governance mechanism |
| Low-trustworthiness condition | Could map to either CAUTION or UNSAFE depending on interpretation | Weak — paper treats low trust as a single state; my architecture distinguishes CAUTION (restricted AI) from UNSAFE (AI disabled) |
| Trust calibration concept | Core design goal of G(S) — ensuring user trust matches system's actual governance state | Strong conceptual alignment |
| Overtrust / complacency | Risk in SAFE state if user fails to verify AI recommendations | Strong |
| Undertrust / disuse | Risk in UNSAFE state if user rejects system's safety classification | Strong |

### Does the paper argue graduated control is superior to binary?

**No.** The paper does not address graduated control. However, its theoretical framing of **trust calibration** — that trust must be appropriately matched to system capability — provides indirect theoretical support for graduated governance. If the system operates in three distinct capability modes (SAFE/CAUTION/UNSAFE), trust must be calibrated to three distinct levels, not just two.

### Does it identify risks of binary automation control?

**Indirectly.** The paper's core framework (drawn from Parasuraman & Riley, 1997; Lee & See, 2004) identifies that binary trust states (overtrust vs undertrust) lead to misuse vs disuse. This is the trust-level analogue of the binary governance gap: if the system only has "fully on" and "fully off" modes, users have no intermediate trust target, making calibration harder.

---

## 5. Trust, Reliance, and User Response

### Does the paper address human trust in automated/AI systems?

**Yes — this is the paper's entire focus.**

### Does it define or operationalise trust in a measurable way?

**Yes.** Trust is operationalised as a latent self-report construct measured via the TIAS/S-TIAS, treated as a predictor of behavioural intention to rely on AI-generated recommendations.

### Validated measurement instruments

#### TIAS (Trust in Automation Scale) — Jian et al. (2000), validated by this paper

- **Items**: 12 items (see Table 1 in paper)
- **Dimensions**: Oblique two-factor model (Factor 1: distrust items 1–5; Factor 2: trust items 6–12)
- **Response format**: 7-point Likert (1 = Not at all, 7 = Extremely)
- **Scoring**: Mean of 12 items (items 1–5 reverse scored)
- **Reliability**: Cronbach's α = 0.94–0.95 across all four studies
- **Validation evidence**: Sensitivity to performance and integrity manipulations; convergent validity with MTP; predictive validity for behavioural intention (R² = 0.70–0.88 in final regression models)
- **Factor structure**: CFA supports oblique two-factor model (CFI = 0.96, TLI = 0.95, RMSEA = 0.09)

#### S-TIAS (Short Trust in Automation Scale) — Developed by this paper

- **Items**: 3 items:
  1. "I am confident in the [system]" (TIAS item 6)
  2. "The [system] is reliable" (TIAS item 10)
  3. "I can trust the [system]" (TIAS item 11)
- **Response format**: 7-point Likert (1 = Not at all, 7 = Extremely)
- **Scoring**: Mean of 3 items
- **Reliability**: Cronbach's α = 0.97 across Studies 3 and 4
- **Validation evidence**: Comparable sensitivity, convergent validity, and predictive validity to full TIAS
- **Key advantage**: Enables repeated measurement within experimental sessions without disrupting interaction — critical for measuring trust dynamics across state transitions

#### Behavioural Intention (BI) scale

- **Items**: 3 items based on Theory of Planned Behavior components (self-prediction, desire/forethought, intent)
- **Reliability**: α = 0.96–0.97
- **Role**: Criterion variable for predictive validity of TIAS/S-TIAS

#### Human Trust Propensity (HTP) — Frazier et al. (2013)

- **Items**: 4 items, 7-point Likert
- **Reliability**: α = 0.88–0.98
- **Finding**: Inconsistently correlated with TIAS — propensity to trust humans does NOT reliably transfer to trust in AI

#### Machine Trust Propensity (MTP) — Merritt et al. (2013)

- **Items**: 6 items, 7-point Likert
- **Reliability**: α = 0.90–0.91
- **Finding**: Consistently positively correlated with TIAS, especially in high-trustworthiness conditions

### Trust failure types

| Trust failure type | Addressed? | Detail |
|---|---|---|
| Overtrust / complacency | Yes | Framed via Parasuraman & Riley (1997); when trust exceeds system capability, outcomes range from "inconvenient to catastrophic" (citing Robinette et al., 2016) |
| Undertrust / disuse | Yes | Framed as: lack of trust in a trustworthy system leads to "reduced productivity and lost resources" |
| Misuse | Implicit | Not terminologically distinguished from overtrust, but the concept is embedded in the trust calibration framework |

### Application to three governance modes

| Mode | Trust concern | S-TIAS applicability |
|---|---|---|
| SAFE | Overtrust risk — user may over-rely on fully enabled AI without verification | S-TIAS can measure whether trust is appropriately high but not excessive |
| CAUTION | **Critical measurement need** — does restricted AI scope help calibrate trust to an intermediate level? Or does it create confusion (is restricted AI seen as less reliable, or as more carefully governed)? | S-TIAS enables repeated measurement across state transitions (SAFE → CAUTION → SAFE), capturing trust trajectory through mode changes |
| UNSAFE | Undertrust risk — user may reject the system's safety classification; also, trust may not recover when system re-enables | S-TIAS can capture trust level during and after UNSAFE episodes |

---

## 6. Mode Awareness and Automation Surprises

### Does the paper address mode confusion?

**No.** The paper does not use the term "mode confusion" or address scenarios where users misunderstand which state the system is in. All vignettes present a single, clearly described trustworthiness condition.

### Does it address automation surprises?

**No.** The experimental design uses static vignettes, not interactive systems. Users do not experience state transitions during the study.

### Implications for CAUTION mode design

The paper does not directly inform CAUTION mode communication design. However, two findings are relevant:

1. **The HTP/MTP divergence**: Users' propensity to trust humans does not predict their trust in AI systems, suggesting that trust in AI is a distinct psychological construct. This means CAUTION mode communication cannot assume users will apply general trust heuristics — the system must explicitly signal what "restricted AI" means in operational terms.

2. **Performance primacy**: The three items selected for the S-TIAS all relate to perceived performance/reliability, not integrity. This suggests users primarily evaluate AI trust through a performance lens. When the system enters CAUTION mode and restricts its advisory scope, users may interpret this as a performance reduction rather than a governance safeguard — a potential source of inappropriate undertrust that PS5 should measure.

---

## 7. Evaluation Methodology

### Experimental design

- **Design**: Between-subjects across all four studies
- **Studies 1–2**: 2 (trustworthiness: high/low) × 3 (AI application: car/assistant/medical or car/assistant/airline) between-subjects
- **Studies 3–4**: 2 (trustworthiness: high/low) × 2 (scale version: TIAS/S-TIAS) between-subjects
- **Sample sizes**: N = 270 (Studies 1, 2), N = 182 (Study 3), N = 180 (Study 4)
- **Platform**: Prolific (US-based), hosted on Qualtrics
- **Compensation**: Pro-rated £6.60/hour

### Dependent variables

| Variable | Measure | Reliability |
|---|---|---|
| Trust | TIAS (12 items) / S-TIAS (3 items) | α = 0.94–0.97 |
| Behavioural intention | BI (3 items) | α = 0.96–0.97 |

### Independent variables

| Variable | Levels |
|---|---|
| Trustworthiness (performance) | High / Low (Studies 1, 3) |
| Trustworthiness (integrity) | High / Low (Studies 2, 4) |
| Scale version | TIAS / S-TIAS (Studies 3, 4) |
| AI application | Self-driving car / Virtual assistant / Medical diagnosis app / Airline booking (varied by study) |

### Individual difference measures

- Human Trust Propensity (HTP)
- Machine Trust Propensity (MTP)

### Analytical methods

- Independent samples t-tests (sensitivity to trustworthiness manipulations)
- Pearson's correlations (convergent validity)
- Hierarchical multiple regression (predictive validity — 5-step model)
- Exploratory factor analysis (Study 1)
- Confirmatory factor analysis (Study 2, using lavaan in R)

### Does it evaluate transitions between automation levels?

**No.** All studies use static vignettes with a single trustworthiness condition per participant. No within-subjects state transition is tested.

### Safety-critical contexts included?

**Partial.** Self-driving car and medical diagnostic app vignettes involve safety-critical scenarios, but the evaluation is vignette-based, not situated in operational safety-critical environments.

---

## 8. Applicability to PS4 (Comparative Evaluation: Graduated vs Binary Governance)

### Theoretical justification for comparing graduated vs binary control?

**Indirect.** The paper's trust calibration framework (drawn from Parasuraman & Riley, 1997; Lee & See, 2004) establishes that trust must be matched to system capability. If the system has three capability modes, binary measurement (trust/distrust) is insufficient — trust must be measurable at intermediate levels. This provides theoretical grounding for why a three-condition evaluation (ungated / binary-gated / graduated) is necessary.

### Specific metrics for measuring the value of an intermediate mode?

**Yes.** The S-TIAS can serve as the primary trust measure across all three PS4 conditions, enabling:
- Comparison of trust levels across conditions
- Assessment of whether graduated governance produces more appropriately calibrated trust than binary governance
- Repeated measurement across scenarios within a single experimental session

### What does "better" mean?

The paper frames "better" as **appropriate calibration**: trust that matches actual system capability. In PS4 terms:
- Better = trust is highest in SAFE, intermediate in CAUTION, lowest in UNSAFE
- Binary governance should show only two trust levels; graduated governance should show three distinct, appropriately ordered trust levels
- "Better calibrated trust" can be operationalised as smaller discrepancy between measured trust (S-TIAS) and governance-appropriate trust level

### Experimental design considerations

- Between-subjects design used throughout — supports PS4's three-condition between-subjects design
- Sample sizes of ~90 per cell yielded large effect sizes (d = 1.5–2.5) for trustworthiness manipulations — suggests PS4 may detect governance-mode effects with similar cell sizes
- Vignette-based approach is transferable to PS4 scenario design (fishing trip scenarios with different governance states)

### What to cite from this paper for PS4

- Validation of S-TIAS as the trust measurement instrument
- Trust calibration as the theoretical framework for evaluating governance effectiveness
- Predictive validity of S-TIAS for behavioural intention to rely on AI recommendations (directly relevant to whether users follow AI advice in each governance state)

---

## 9. Applicability to PS5 (Socio-Technical Evaluation of CAUTION Mode)

### Validated instruments for measuring trust across governance modes?

**Yes — this is the paper's primary contribution to PS5.**

- **S-TIAS** (3 items, α = 0.97): Enables minimally disruptive, repeated trust measurement across governance state transitions within a single user study session
- **BI scale** (3 items, α = 0.96–0.97): Measures intention to rely on AI recommendations — directly captures whether users intend to follow AI advice in each governance state
- **MTP scale** (6 items): Controls for individual differences in dispositional trust toward machines

### Precedent for evaluating user understanding of intermediate automation states?

**No.** The paper does not test intermediate states. This is a gap that PS5 fills.

### How to measure trust calibration?

The paper operationalises trust calibration implicitly through the gap between trust level and system trustworthiness. For PS5, this can be adapted:
- **Appropriate calibration in CAUTION mode** = S-TIAS score is intermediate between SAFE and UNSAFE scores
- **Miscalibration** = S-TIAS score in CAUTION is equal to SAFE (suggesting user does not perceive restriction) or equal to UNSAFE (suggesting user treats restriction as total system failure)

### How do users interpret system restriction?

**Not directly addressed.** The paper notes that the S-TIAS items emphasise performance/reliability rather than integrity. This suggests that when the system restricts its scope (CAUTION mode), users may perceive this through a performance lens — potentially interpreting restriction as unreliability rather than as appropriate governance. PS5 should include items measuring whether users understand restriction as a safety feature vs a performance limitation.

### What to cite from this paper for PS5

- S-TIAS as the primary repeated trust measure for within-session governance state transitions
- BI scale as the behavioural intention measure for reliance on AI in each governance state
- The HTP/MTP divergence finding — trust in AI is distinct from general interpersonal trust, meaning CAUTION mode communication must be AI-specific, not drawn from interpersonal trust heuristics
- Performance primacy in trust evaluation — design implication for how CAUTION mode restriction should be communicated

---

## 10. Key Concepts and Definitions

| Term / Framework | Definition | Location | Mapping to my research |
|---|---|---|---|
| **Trust calibration** | User trust must be appropriately matched to the capabilities of the system; overtrust leads to misuse, undertrust leads to disuse | Section 1 (citing Parasuraman & Riley, 1997) | Core evaluative concept for PS4/PS5 — graduated governance should produce better trust calibration than binary governance |
| **Trust in Automation Scale (TIAS)** | 12-item self-report measure of trust in automated systems; oblique two-factor structure (trust/distrust) | Section 2, Table 1 | Full-length instrument option; validated for AI applications |
| **Short Trust in Automation Scale (S-TIAS)** | 3-item short form (items 6, 10, 11 from TIAS); α = 0.97 | Section 4, validated in Studies 3–4 | **Primary trust instrument for PS4/PS5** — enables repeated measurement across governance state transitions |
| **Behavioural Intention (BI)** | 3-item measure based on Theory of Planned Behavior; captures self-prediction, desire, and intent to follow system recommendations | Section 3.1.1.2.5 | Criterion measure for reliance on AI recommendations in each governance state |
| **Machine Trust Propensity (MTP)** | Dispositional tendency to trust machines; 6-item scale (Merritt et al., 2013) | Section 3.1.1.2.4 | Individual difference covariate for PS4/PS5 |
| **Overtrust / misuse** | Relying on system when it should not be trusted; can lead to outcomes "ranging from inconvenient to catastrophic" | Section 1 (citing Robinette et al., 2016) | Risk in SAFE mode; measured via S-TIAS + BI |
| **Undertrust / disuse** | Rejecting trustworthy system; leads to reduced productivity | Section 1 | Risk in UNSAFE mode; trust repair challenge when system re-enables |
| **Perfect Automation Schema (PAS)** | Cognitive schema reflecting expectations of automation; comprises all-or-none thinking and high expectations (Gibson et al., 2023) | Section 5 (Discussion) | Potential confound in PS5: users with high PAS may expect AI to be either perfect or useless, rejecting the CAUTION intermediate |

---

## 11. Quotable / Citable Points

1. **Trust calibration as safety requirement** (Section 1): The paper establishes that for safe and effective human–AI interaction, user trust must be calibrated to system capability — overtrust leads to misuse with potentially catastrophic outcomes, while undertrust leads to disuse and lost productivity. *→ Cite when arguing that graduated governance requires graduated trust measurement.*

2. **S-TIAS validated for repeated measurement** (Section 5 / Discussion): The 3-item S-TIAS is validated as psychometrically comparable to the full 12-item TIAS while being practical for frequent, minimally disruptive measurement — enabling the study of trust trajectories and calibration over time. *→ Cite when justifying instrument selection for PS4/PS5.*

3. **HTP does not predict trust in AI** (Section 5 / Discussion): Propensity to trust humans is not consistently associated with trust in AI systems, while machine trust propensity is. This suggests trust in AI is a qualitatively distinct construct from interpersonal trust. *→ Cite when arguing that CAUTION mode communication must be specifically designed for the AI governance context, not borrowed from human delegation analogies.*

4. **Performance primacy in trust evaluation** (Section 4 / Item analysis): The three highest-performing items all relate to performance/reliability rather than integrity, suggesting that users primarily evaluate AI trust through a performance lens. *→ Cite when discussing the risk that CAUTION mode restriction may be misperceived as performance degradation.*

5. **TIAS predicts behavioural intention** (Studies 1–4): Trust measured by TIAS/S-TIAS is the strongest predictor of intention to rely on AI recommendations, accounting for the greatest proportion of variance in BI (R² change = 0.19–0.37 for S-TIAS). *→ Cite when establishing trust as the key mediating variable between governance state and user reliance behaviour.*

---

## 12. Limitations and Gaps

### Stated limitations

- All studies use **vignette-based** methodology — participants read about AI interactions rather than experiencing them. The authors acknowledge that measuring actual behaviour in human–AI interactions would extend the findings.
- All samples are **US-based Prolific participants** — no cross-cultural validation.
- **Behavioural intention** is measured rather than actual behaviour — people may not act in accordance with their stated intentions.
- The two-factor structure of the TIAS may be a **methodological artifact** of reverse-scored item distribution.

### Gaps my research could address

| Gap | How my research addresses it |
|---|---|
| No evaluation of trust across **multiple system states** within a single interaction | PS5 measures S-TIAS across SAFE/CAUTION/UNSAFE transitions within a scenario sequence |
| No evaluation of trust response to **system restriction** (reduced capability mode) | PS5 specifically evaluates user trust in the CAUTION state where AI is active but scope-restricted |
| No application to **environmental-state-conditioned governance** | My architecture conditions governance on classified environmental state S = f(E), not on static design-time configuration |
| No application to **safety-critical decision support** in operational contexts | PS4 evaluates governance in a coastal fisheries safety-critical context |
| No evaluation in **low-resource or non-Western deployment contexts** | PS5 targets Malaysian coastal fishing communities |
| No evaluation of **governance state communication** | PS5 must assess whether users understand what CAUTION mode means — the S-TIAS measures trust but not comprehension of the governance mechanism |

### What this paper does NOT cover that my research needs

- A measure of **mode understanding / mode awareness** — S-TIAS measures trust level but not whether users correctly understand which governance state they are in or what that state means
- A measure of **trust appropriateness** — the paper measures trust but does not define what the "correct" trust level is for a given system state; my research must define governance-appropriate trust targets
- Evaluation of trust during **state transitions** — how trust changes when the system moves from SAFE to CAUTION, or CAUTION to UNSAFE

---

## 13. Positioning in My Literature Review

### Role in the argumentative chain

- **Link 9 (partial)**: Contributes to establishing the evaluation methodology for PS5 — provides the validated instrument but does not itself conduct socio-technical evaluation of intermediate governance modes
- **Methodological foundation**: Establishes the measurement infrastructure (S-TIAS, BI, MTP) that PS4 and PS5 build upon

### Role in the literature review

- ✅ Provides **validated instruments** for PS4/PS5 evaluation design
- ✅ Provides **theoretical grounding** for trust calibration as the evaluative criterion
- ✅ Establishes **methodological foundation** that has not yet been applied to AI governance architectures
- ❌ Does NOT provide empirical precedent for evaluating intermediate governance modes (this is the gap)
- ❌ Does NOT provide design recommendations for communicating governance state to users

### Gap statement

This paper establishes the S-TIAS as a psychometrically validated, practical instrument for measuring trust in AI systems, and confirms that trust calibration — the appropriate matching of user trust to system capability — is the critical mediating variable for safe human–AI interaction. However, the S-TIAS has been validated only in binary trustworthiness conditions (high/low), and has not been applied to contexts where the AI system operates in multiple governance states with distinct capability profiles. My research extends this by deploying the S-TIAS across a three-state graduated governance architecture (SAFE/CAUTION/UNSAFE), testing whether the instrument can detect the intermediate trust calibration that the CAUTION state is designed to produce, and evaluating whether graduated governance achieves better trust calibration than binary governance in a safety-critical, low-resource deployment context.

---

## 14. Overall Relevance Score

### ⭐⭐⭐⭐ High

**Justification**: This paper provides the primary validated trust measurement instrument (S-TIAS) and the behavioural intention scale (BI) that will be directly adopted in PS4 and PS5 evaluation design. It also provides the trust calibration theoretical framework that underpins the evaluative logic of both studies. It falls short of ⭐⭐⭐⭐⭐ because it does not address graduated governance, intermediate automation modes, or state transitions — the specific evaluation challenges that are novel in my research. It provides the measurement tool but not the evaluation precedent.

**Role cluster**: Methodological instrument source / trust theory foundation

**Recommended citation uses**:
1. Instrument selection justification for PS4/PS5 (S-TIAS, BI, MTP)
2. Trust calibration as the evaluative criterion for comparing governance modes
3. Evidence that trust in AI is distinct from interpersonal trust (HTP/MTP divergence)
4. Performance-primacy finding as design consideration for CAUTION mode communication
