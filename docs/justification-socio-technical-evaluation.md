# How Will You Evaluate This Socio-Technically? Trust, Usability, Decision Quality, and Field Study Design

**Document type**: Theoretical justification / argumentation note  
**For**: Chapter 5 (Evaluation Design), Chapter 6 (Findings), and viva preparation  
**Questions addressed**: What is socio-technical evaluation? Why is it needed? How will trust, usability, decision quality, and human-AI interaction be measured? How many participants, how long, what ethics? What if fishermen ignore or over-rely on AI? How will adoption be measured? What are success criteria?

**Cross-references**: For why the CAUTION state exists, see `justification-three-states.md`. For CAUTION mode operation and scope definition, see `justification-caution-mode-operation.md`. For the formal model being evaluated, see `justification-formal-model.md`. For why governance is conditioned on environmental state (not AI confidence), see `justification-environmental-state-governance.md`.

---

## 1. What Is Socio-Technical Evaluation?

### 1.1 Definition

Socio-technical evaluation assesses a system not only on its technical performance (does it compute correctly?) but on how it functions within its social context — how users understand it, trust it, interact with it, and make decisions with it. The term "socio-technical" comes from the recognition that a system's value is determined by the joint optimisation of its technical and social subsystems (Baxter & Sommerville, 2011), not by either in isolation.

In this research, socio-technical evaluation means assessing the three-mode governance architecture not merely on whether S = f(E) correctly classifies environmental states or whether AI(E) ⊆ A_AI(S) holds (these are technical verification tasks under O4), but on whether the graduated governance produces meaningful differences in how users understand, trust, and decide across SAFE, CAUTION, and UNSAFE modes (O5).

### 1.2 Why This Matters for This Research Specifically

The core architectural contribution — the CAUTION mode where AI operates under restricted advisory scope — is designed to serve human decision-makers. If users cannot distinguish CAUTION from SAFE (perceiving AI as fully capable when it is restricted), the governance architecture is technically sound but socio-technically ineffective. If users treat CAUTION identically to UNSAFE (ignoring AI altogether when it is restricted), the CAUTION mode provides no practical advantage over binary governance.

PS5 states: "No study has examined how users understand, trust, and respond to a graduated AI participation model — where the system communicates that AI is not merely on or off, but operating under restriction." This is a gap that can only be filled by socio-technical evaluation. Technical testing (O4) confirms the architecture works; socio-technical evaluation (O5) confirms it works *for people*.

Bach et al. (2024a), in a systematic review of HAII in safety-critical industries (24 empirical articles from IEEE Access), found that only 3 of 24 studies involved target end-users in any phase of AI system development. Most evaluations were conducted with proxy participants (researchers, students, crowd-workers). This finding establishes that socio-technical evaluation with actual target users is both rare and methodologically important — the architecture must be evaluated with fishers and fisheries domain experts, not proxies, to address PS5 credibly.

---

## 2. Why Is Socio-Technical Evaluation Necessary? (Can't Technical Testing Suffice?)

### 2.1 The Insufficiency of Technical Testing Alone

Technical testing (O4) can verify:
- Whether S = f(E) correctly classifies environmental conditions across test scenarios
- Whether the Safety Dominance Property AI(E) ⊆ A_AI(S) holds in all tested cases
- Whether graduated governance produces fewer safety violations than binary governance
- Whether decision consistency improves under two-level governance

What technical testing *cannot* verify:
- Whether users understand what CAUTION means operationally
- Whether users calibrate trust appropriately to each governance mode
- Whether the restricted advisory scope in CAUTION mode changes user decision behaviour
- Whether the system is usable by the target population (fishers with limited digital literacy)
- Whether governance state communication is interpretable
- Whether the architecture produces adoption or rejection in practice

### 2.2 The Trust Calibration Argument

McGrath et al. (2025b — CHAI-T framework) position trust not as an outcome to be maximised but as a *mediator* between system inputs and user performance. The goal is "calibrated trust aligned with actual system capabilities, not maximum trust." In a three-mode governance architecture, calibrated trust means:
- In SAFE: trust that the full recommendation space is reliable
- In CAUTION: trust that the restricted recommendation space is reliable, combined with awareness that some recommendation types are suppressed
- In UNSAFE: trust that the system's decision to disable AI is itself appropriate

If users achieve the same trust level across all three modes, trust is miscalibrated — the architecture has failed socio-technically even if it succeeds technically.

### 2.3 The Behavioural Dependence Argument

Schrills et al. (2025) demonstrate empirically (N=149, preregistered) that self-reported trust is a poor predictor of actual behavioural dependence on AI (correlation r = 0.42–0.45). Instead, *instructed reliability* — what users are told about system capability — was the strongest predictor of dependence. Participants matched their agreement with AI recommendations (~78%) to the instructed reliability level (80%), even though the AI was actually 100% correct.

This finding has a direct implication for the CAUTION mode: if users calibrate their dependence to *communicated* system capability rather than subjective trust attitudes, then clearly communicating that AI is operating under CAUTION (restricted scope) should directly shape reliance behaviour. But this effect can only be tested socio-technically — no amount of formal verification can predict whether governance state communication actually changes user behaviour.

---

## 3. How Will You Measure Trust?

### 3.1 The Measurement Problem

Trust in AI systems is measured heterogeneously across the literature. Aquilino et al. (2025), reviewing 45 empirical studies, found diverse conceptualisations ranging from interpersonal trust frameworks (Mayer et al., 1995 — ability, benevolence, integrity) to technology-specific frameworks (McKnight et al., 2011 — functionality, reliability, helpfulness) to automation-specific frameworks (Lee & See, 2004 — performance, process, purpose). Four of their 45 studies defined trust with affective components but measured it with only cognitive attributes, revealing a gap between conceptualisation and operationalisation.

Bach et al. (2024b — SLR of user trust in AI from an HCI perspective, 23 studies, 195 citations) identify three categories of trust antecedents: socio-ethical considerations, technical/design features, and user characteristics — with user characteristics as the dominant category. They note that no cross-context validated trust instrument exists and that research in non-Western settings is absent from their corpus.

### 3.2 The Chosen Approach: Validated Instrument + Behavioural Dependence

The evaluation will use a **dual measurement strategy**:

**Attitudinal trust (self-report):** The Trust in Automation Scale (TIAS; Jian et al., 2000) as validated by McGrath et al. (2025a). McGrath et al. (2025a) conducted the first comprehensive psychometric validation of TIAS across four studies and additionally developed the 3-item Short Trust in Automation Scale (S-TIAS), comprising "I am confident in the AI assistant," "The AI assistant is reliable," and "I can trust the AI assistant" (α = 0.97). The S-TIAS demonstrated comparable reliability, sensitivity, convergent validity, and predictive validity to the full 12-item TIAS.

The S-TIAS is particularly suited to this evaluation because:
- It enables **repeated measurement** across governance modes within a single session (3 items per mode, minimising respondent fatigue)
- It is validated for sensitivity to trustworthiness manipulations — the governance mode transition from SAFE to CAUTION to UNSAFE is analogous to a trustworthiness manipulation
- Its brevity makes it feasible for participants with limited formal education

**Behavioural dependence (observed):** Following Schrills et al.'s (2025) recommendation to measure behaviour separately from attitudes, the evaluation will also measure:
- **Recommendation agreement rate**: proportion of scenarios where the user follows AI recommendations, measured per governance mode
- **Decision modification**: whether users change their initial decision after seeing AI recommendations, per governance mode
- **Override frequency**: how often users override AI recommendations in each mode

### 3.3 Why Not Trust Alone?

Schrills et al. (2025) demonstrate that trust assessment and behavioural dependence are weakly correlated. A user may report high trust in CAUTION mode but still override AI recommendations frequently (or vice versa). Measuring only self-reported trust would miss the behavioural signal. Measuring only behavioural dependence would miss the attitudinal signal (which matters for adoption and sustained use). Both are needed.

Atf & Lewis (2026), in a meta-analysis of 90 XAI studies, find a statistically significant but weak positive correlation (r = 0.194) between AI explainability and trust. They distinguish between **Trust Enforcement** (presenting selective data to make users trust) and **Trust Empowerment** (providing all relevant information so users can determine their own trust level). The governance state communication in the CAUTION mode follows the Trust Empowerment model — users are informed of the restriction and empowered to calibrate their own reliance, not manipulated into trusting.

---

## 4. How Will You Measure System Usability?

### 4.1 Standard Instruments

System usability will be measured using a validated instrument appropriate for the target population. Standard options include the System Usability Scale (SUS; Brooke, 1996) — a 10-item Likert scale that produces a single usability score (0–100) and has been validated across thousands of studies and multiple languages.

### 4.2 Mode-Specific Usability Concerns

Usability measurement must address mode-specific questions:
- Can users identify which governance mode the system is currently in?
- Can users interpret the restricted recommendation set in CAUTION (i.e., understand why DepartureTime and Duration recommendations are absent)?
- Can users act on the recommendations provided in each mode?
- Is the transition between modes perceptible and understandable?

These questions go beyond standard SUS items and will be addressed through **task-based usability assessment** — observing whether users can successfully complete decision tasks in each governance mode — supplemented by **post-task interviews** probing comprehension of governance state transitions.

### 4.3 Cross-Cultural and Low-Literacy Considerations

The target population (Malaysian small-scale fishers) may have limited formal education and limited experience with digital interfaces. Bach et al. (2024a) found that only 3 of 24 HAII studies involved actual target end-users. The evaluation must:
- Use the local language (Bahasa Malaysia) for all instruments
- Use visual/icon-based governance state indicators in the prototype rather than text-only labels
- Pilot-test comprehension of survey instruments before the main study
- Supplement written instruments with structured interviews to capture responses that surveys may miss

---

## 5. How Will You Measure Decision Quality?

### 5.1 Definition

Decision quality in this context means: given the environmental conditions (E) and the governance mode (S), does the user make a decision that is consistent with safe operational practice? Decision quality is not about whether the user follows AI recommendations (that is dependence, not quality). It is about whether the user's final decision — whether AI-informed or independently made — avoids unsafe outcomes.

### 5.2 Metrics

| Metric | Definition | How measured |
|---|---|---|
| **Safety compliance** | Does the user's decision avoid actions that are inappropriate for the classified safety state? | Scenario-based: expert panel pre-classifies each scenario's "safe decision envelope"; user decisions are compared against it |
| **Decision consistency** | Does the same user make similar decisions under similar conditions across repeated scenarios? | Within-subject comparison across matched scenario pairs |
| **Appropriate scope adherence** | In CAUTION, do users limit their decisions to the types supported by the restricted advisory space? | Whether users make DepartureTime/Duration decisions in CAUTION when no AI recommendation supports these |
| **Override appropriateness** | When users override AI, is the override justified by local knowledge or context? | Post-decision interview probing rationale for overrides |

### 5.3 The Three-Condition Comparison (O4)

Decision quality is assessed across three conditions (O4):

1. **Ungated baseline**: AI generates recommendations from the full space R regardless of environmental conditions. No governance layer.
2. **Binary-gated baseline**: Level 1 governance only — G(S) controls whether AI participates (on/off). When AI is on, full R is available; when off, no AI.
3. **Two-level graduated**: The proposed architecture — G(S) controls participation, A_AI(S) controls advisory scope. CAUTION mode restricts R to {Go, Delay}.

The comparison isolates Level 2's contribution: the difference between conditions 2 and 3 measures the added value of advisory scope restriction beyond participation governance alone.

---

## 6. How Will You Evaluate Human-AI Interaction?

### 6.1 Framework

The CHAI-T framework (McGrath et al., 2025b) provides the conceptual structure for evaluating human-AI interaction. CHAI-T adopts an IMOI (Inputs-Mediators-Outputs-Inputs) process model where:
- **Inputs**: Human factors (experience, risk attitude, TK), technology factors (governance mode, recommendation type), context factors (environmental conditions, season, time of day)
- **Mediators**: Trust (attitudinal), comprehension of governance state, perceived system capability
- **Outputs**: Decision behaviour, recommendation acceptance, override rate, decision quality
- **Recursive feedback**: Outputs from one decision episode become inputs to the next

Each fishing trip decision is a *performance episode* in CHAI-T terms. The evaluation examines how interaction patterns differ across governance modes — not just whether users trust the system, but how the full input-mediator-output chain operates under SAFE, CAUTION, and UNSAFE.

### 6.2 Interaction Dimensions

Bach et al. (2024a) identify seven factors influencing HAII in safety-critical industries: user characteristics, user perceptions and attitudes, user expectations and experience, AI interface and features, AI output, explainability and interpretability, and usage of AI. Of these, the evaluation foregrounds:

- **AI output** — directly manipulated by the governance architecture (full R in SAFE, restricted in CAUTION, empty in UNSAFE)
- **User perceptions and attitudes** — measured via S-TIAS trust instrument
- **User expectations and experience** — probed in interviews (did the user expect the restriction? did they understand why?)
- **Explainability and interpretability** — assessed by whether users can articulate *why* the system is in CAUTION and *what* that means for the recommendations they receive

### 6.3 The Distinctive CAUTION Interaction Pattern

The evaluation specifically tests whether CAUTION produces a *distinct* interaction pattern — not merely an interpolation between SAFE and UNSAFE. If CAUTION interaction is indistinguishable from SAFE (users treat restricted AI as full AI), the architecture fails to achieve its purpose. If CAUTION interaction is indistinguishable from UNSAFE (users ignore restricted AI entirely), the CAUTION mode adds no value over binary governance.

The hypothesis is that CAUTION produces a distinctive pattern characterised by:
- Trust level intermediate between SAFE and UNSAFE
- Recommendation agreement rate lower than SAFE but higher than zero (UNSAFE has no recommendations)
- Greater reliance on personal knowledge and traditional knowledge to complement AI
- Awareness that certain recommendation types are absent

---

## 7. How Many Fishermen? How Long?

### 7.1 Sample Size Rationale

The evaluation is a **mixed-methods study** combining quantitative instruments (S-TIAS, SUS, decision metrics) with qualitative data (interviews, observation). Sample size is determined by the qualitative component's saturation requirements and the quantitative component's statistical constraints, whichever is larger.

For the qualitative component, thematic saturation in HCI studies typically occurs at 12–20 participants (Guest, Bunce & Johnson, 2006). For the quantitative component, the within-subjects design (each participant experiences all three governance modes) increases statistical power relative to between-subjects designs.

The target is **30–40 participants**, comprising:
- 20–25 active small-scale fishers from the target population (Terengganu coast, Malaysia)
- 5–8 fisheries officers or fisheries department staff
- 5–7 maritime/fisheries domain experts

This is consistent with the evaluation methodology stated in O5: "User study with fishermen / fisheries officers / domain experts."

### 7.2 Why This Number Is Sufficient

Yamin et al. (2025) surveyed 136 fishers for a quantitative attitude study. Rahim et al. (2024) studied 79 households. Gao (2024) used ethnographic methods with a smaller sample. The proposed study is not a large-scale survey — it is an interaction study requiring scenario-based sessions that take 60–90 minutes per participant. The depth of data per participant (trust measurement across 3 modes × multiple scenarios, plus interview data) compensates for the smaller sample compared to pure survey research.

Bach et al. (2024a) note that the median sample size in their 24-paper HAII SLR is small, and that the field is dominated by early-stage evaluations. A study with 30–40 participants involving actual target users is methodologically stronger than larger studies using proxies.

### 7.3 Duration

The field study has two phases:

1. **Controlled scenario sessions** (2–3 months): Each participant completes a structured interaction session with the prototype, experiencing pre-designed scenarios across all three governance modes. Sessions are individually administered, taking 60–90 minutes each.

2. **Extended observation** (optional, if prototype maturity permits): A subset of participants uses the system during actual fishing decision-making over 2–4 weeks, providing ecological validity data. This phase is contingent on prototype readiness and is explicitly noted as a secondary evaluation component.

---

## 8. What Ethical Issues Are Involved?

### 8.1 Core Ethical Concerns

| Concern | Mitigation |
|---|---|
| **Informed consent** | All participants receive oral and written explanation in Bahasa Malaysia; consent is documented; participants may withdraw at any time without consequence |
| **No operational risk** | The evaluation uses scenarios, not live fishing decisions — no participant will be placed in physical danger because of the study |
| **Data privacy** | Participant identities are anonymised; demographic and decision data are stored securely; no personally identifiable information is published |
| **Power dynamics** | Fisheries officers are evaluated separately from fishers to avoid authority influence on responses; researchers do not hold authority over participants |
| **Cultural sensitivity** | Instrument design respects local norms; traditional knowledge is acknowledged as complementary to (not inferior to) AI-based decision support |
| **Gatekeeping** | University ethics approval (UMS/MARA/equivalent) is obtained before any participant contact |

### 8.2 The "What If They Use It for Real Decisions?" Concern

The evaluation prototype is explicitly presented as a research tool, not an operational system. Participants are informed that the prototype is being evaluated and should not be used for actual fishing decisions. However, if the extended observation phase (§7.3) proceeds, the architecture's safety properties provide a structural safeguard: the Safety Dominance Property ensures that AI recommendations are always within the governance-permitted space, and the UNSAFE mode disables AI entirely. The architecture's worst-case behaviour (over-classification to UNSAFE, disabling AI unnecessarily) is safe — the user defaults to their existing decision-making practice.

---

## 9. What Happens If Fishermen Ignore the AI?

### 9.1 This Is Expected Behaviour, Not Failure

The architecture is a decision *support* system, not a decision *making* system. The human decision-maker retains full authority in all governance modes. Ignoring AI recommendations is a legitimate user response — it means the user's own judgment (including traditional knowledge) is preferred over the AI's recommendation.

### 9.2 The Analytical Value of Rejection

User rejection of AI recommendations is analytically informative, not problematic:

- **In SAFE mode**: If users frequently ignore full-scope AI recommendations, this suggests undertrust — the system's trust calibration mechanisms need improvement (McGrath et al., 2025b)
- **In CAUTION mode**: If users ignore restricted-scope AI recommendations at the same rate as full-scope (SAFE) recommendations, the restriction is transparent to users and CAUTION produces no distinct interaction pattern. If they ignore at a higher rate, users may perceive restricted AI as less useful (expected and informative). If they ignore at a lower rate, users may treat restriction as a quality signal (the system is being more careful, so its recommendations may be more trustworthy under uncertainty)
- **In UNSAFE mode**: AI is disabled; there is nothing to ignore. The user's autonomous decision-making under UNSAFE conditions is itself a data point

### 9.3 Domain Context

Rahim et al. (2024) document that fishers in coastal Makassar routinely ignore binary governmental warnings from Indonesia's Ministry of Maritime Affairs. The response to being ignored was not to make warnings mandatory — it was that the binary warning system failed to accommodate the adaptive fishing practices fishers already employ under marginal conditions. The CAUTION mode is specifically designed to address this: rather than a binary "don't go" warning that users ignore, it provides restricted-scope decision support that aligns with the cautious-go behaviour fishers already practise (Gao, 2024).

---

## 10. What Happens If Fishermen Over-Rely on AI?

### 10.1 Over-Reliance: The Complementary Risk

Over-reliance (automation complacency) occurs when users follow AI recommendations uncritically, suppressing their own judgment. This is the complementary failure mode to under-reliance (ignoring AI). McGrath et al. (2025a) frame these as the two calibration failures: "overreliance and lack of monitoring" (trust exceeds optimal) versus "disuse of technological systems" (trust falls below optimal).

### 10.2 Architectural Safeguards Against Over-Reliance

The three-mode governance architecture provides structural protection against over-reliance that binary systems cannot:

1. **CAUTION mode as a calibration intervention**: When environmental conditions degrade from SAFE to CAUTION, the system *visibly restricts* its own output. This is a system-initiated signal that conditions are uncertain and AI capability is reduced. Schrills et al. (2025) show that communicated system capability directly shapes user dependence — communicating restriction should reduce uncritical reliance.

2. **Graduated restriction prevents cliff-edge transitions**: In a binary system, the transition from "AI fully on" to "AI off" is abrupt. Users who have developed reliance habits during the "on" phase face a sudden loss of decision support. The CAUTION mode provides a graduated transition that may help users progressively re-engage their own judgment before AI is fully disabled.

3. **Scope restriction reduces the domain of possible over-reliance**: In CAUTION, even if the user follows AI recommendations uncritically, the recommendations are limited to {Go, Delay} — threshold-crossing assessments that are robust to environmental uncertainty. The architecture structurally prevents the AI from providing precise timing or duration recommendations that would be unreliable under CAUTION conditions, regardless of whether the user would have followed them.

### 10.3 Measurement

Over-reliance will be detected by comparing:
- User decision quality when AI recommendations are *correct* vs when AI recommendations are deliberately sub-optimal (in controlled scenarios) — over-reliant users will follow sub-optimal recommendations
- Whether users can articulate the rationale for their decisions or merely report following the AI — indicative of monitoring depth

---

## 11. How Will You Measure Adoption?

### 11.1 What Adoption Means in This Context

This is a PhD evaluation, not a product deployment. "Adoption" in this context does not mean uptake in a market sense. It means: would users willingly use this system for their fishing decisions if it were available?

### 11.2 Adoption Indicators

| Indicator | How measured |
|---|---|
| **Stated willingness to use** | Post-session survey: "Would you use this system for your fishing decisions?" (Likert scale) |
| **Comparative preference** | Post-session survey: preference ranking among (a) no AI, (b) binary AI (on/off), (c) three-mode AI |
| **Mode-specific value perception** | Interview: "Was CAUTION mode useful? Would you want the system without CAUTION mode?" |
| **Perceived trustworthiness** | S-TIAS scores across modes — high trust as a prerequisite for adoption |
| **Behavioural signal** (if extended observation proceeds) | Frequency of voluntary system consultation during actual decision-making |

### 11.3 Domain Context

Yamin et al. (2025) document that flexibility is the weakest adaptive capacity domain among Terengganu fishers (only 58% consider alternative livelihoods; 67.6% rely solely on fishing income). This suggests that any tool perceived as reducing risk or improving fishing decisions has strong adoption incentive. The evaluation measures whether the graduated governance architecture is perceived as providing this benefit above and beyond binary alternatives.

---

## 12. What Are Your Success Criteria for Socio-Technical Evaluation?

### 12.1 Primary Success Criteria (O5)

The socio-technical evaluation succeeds if it demonstrates that CAUTION produces a **distinct interaction pattern** that is not merely an interpolation between SAFE and UNSAFE. Specifically:

| Criterion | Operationalisation | Threshold |
|---|---|---|
| **Governance mode awareness** | Users can correctly identify which mode the system is in and what it means | ≥75% correct identification across all three modes |
| **Trust differentiation** | S-TIAS trust scores differ significantly across SAFE, CAUTION, and UNSAFE | Statistically significant difference (p < 0.05) on repeated-measures comparison |
| **Behavioural differentiation** | Recommendation agreement rate and decision patterns differ across modes | CAUTION agreement rate falls between SAFE and UNSAFE (not equal to either) |
| **Comprehension of restriction** | Users can articulate what CAUTION means operationally — what is available and what is not | ≥60% of participants can name at least one recommendation type that is suppressed in CAUTION |
| **Perceived value of CAUTION** | Users perceive CAUTION mode as distinct from and preferable to binary on/off | Majority (>50%) of participants express preference for three-mode over binary when asked directly |

### 12.2 Secondary Success Criteria (O4 — Technical)

| Criterion | Operationalisation |
|---|---|
| **Safety Dominance Property** | AI(E) ⊆ A_AI(S) holds in 100% of test scenarios |
| **Safety compliance improvement** | Graduated governance produces fewer safety violations than both binary-gated and ungated baselines |
| **Decision consistency** | Within-subject decision consistency is higher under graduated governance than binary |

### 12.3 What Constitutes Failure?

The evaluation produces a negative result (which is still a valid PhD contribution) if:
- Users cannot distinguish CAUTION from SAFE or UNSAFE (governance mode awareness fails)
- Trust and behaviour do not differ across modes (CAUTION produces no distinct pattern)
- Users overwhelmingly prefer binary governance over graduated governance

A negative result does not invalidate the architectural contribution (O1–O3) — it invalidates the claim that graduated governance is socio-technically superior to binary governance for the target population. This would itself be a contribution: demonstrating that while the formal architecture is sound, users do not respond to the additional governance granularity. Such a finding would have implications for all future graduated governance proposals.

---

## 13. Comparative Summary

| Question | Answer | Key Citation |
|---|---|---|
| What is socio-technical evaluation? | Assessment of both technical performance and user experience within social context | Baxter & Sommerville (2011); Bach et al. (2024a) |
| Why needed beyond technical testing? | Technical testing cannot verify trust calibration, user comprehension, or decision behaviour change | McGrath et al. (2025b — CHAI-T); Schrills et al. (2025) |
| How measure trust? | Dual: S-TIAS (3-item validated self-report) + behavioural dependence (agreement rate, override frequency) | McGrath et al. (2025a — S-TIAS validation); Schrills et al. (2025) |
| How measure usability? | SUS + task-based mode-specific assessment + post-task interview | Brooke (1996); adapted for low-literacy context |
| How measure decision quality? | Safety compliance, decision consistency, scope adherence, override appropriateness across three conditions | O4 three-condition comparison design |
| How evaluate human-AI interaction? | CHAI-T IMOI framework: Inputs → Mediators (trust) → Outputs (decision) across performance episodes | McGrath et al. (2025b); Bach et al. (2024a — 7 HAII factors) |
| How many participants? | 30–40 (20–25 fishers, 5–8 officers, 5–7 experts) | Guest et al. (2006) saturation; Bach et al. (2024a) sample norms |
| How long? | 2–3 months controlled sessions; optional 2–4 weeks extended observation | Within-subjects design; 60–90 min per participant |
| Ethics? | Informed consent, no operational risk (scenarios), anonymisation, cultural sensitivity, ethics board approval | Standard research ethics protocol |
| Fishermen ignore AI? | Expected and informative — different rejection patterns across modes reveal trust calibration | Rahim et al. (2024) — fishers already ignore binary warnings |
| Fishermen over-rely? | CAUTION mode is a structural safeguard: visible restriction → reduced uncritical reliance; scope restriction limits damage | Schrills et al. (2025); McGrath et al. (2025a) |
| Measure adoption? | Stated willingness, comparative preference (binary vs graduated), mode-specific value perception | Yamin et al. (2025) — adoption incentive from vulnerability context |
| Success criteria? | CAUTION produces a distinct pattern: awareness ≥75%, trust differentiation p<0.05, behavioural differentiation, comprehension ≥60%, majority preference for graduated | O5 operationalisation |

---

## One-Paragraph Summary

The socio-technical evaluation addresses PS5 by assessing whether the three-mode governance architecture produces meaningful differences in user understanding, trust, and decision behaviour across SAFE, CAUTION, and UNSAFE — differences that technical testing alone cannot detect. Trust is measured dually: the validated 3-item S-TIAS instrument (McGrath et al., 2025a) captures attitudinal trust per mode, while behavioural dependence measures (recommendation agreement, override frequency) capture actual reliance — a distinction Schrills et al. (2025) demonstrate is essential because self-reported trust poorly predicts behaviour (r = 0.42–0.45). Human-AI interaction is structured through McGrath et al.'s (2025b) CHAI-T IMOI framework, with each fishing decision as a performance episode where governance mode, trust, and decision quality form recursive feedback loops. The evaluation uses a within-subjects design with 30–40 participants (fishers, officers, experts) experiencing all three governance modes across controlled scenarios, with success defined as CAUTION producing a statistically distinct interaction pattern — not merely interpolating between SAFE and UNSAFE. User rejection of AI is treated as analytically informative, not as failure, following the precedent that fishers already ignore binary warnings that fail to accommodate their adaptive practices (Rahim et al., 2024). Over-reliance is structurally mitigated by the CAUTION mode itself: visible restriction of AI output communicates reduced capability and should directly calibrate dependence (Schrills et al., 2025), while scope restriction to {Go, Delay} prevents unreliable recommendation types from reaching users regardless of their reliance level.
