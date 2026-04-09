# Literature Extraction: Tatasciore & Loft (2025)

## Section 1: Bibliographic Information
- **Title:** Calibrating Reliance on Automated Advice: Transparency and Trust Calibration Feedback
- **Authors:** Monica Tatasciore, Shayne Loft
- **Year:** 2025
- **Venue:** International Journal of Human–Computer Interaction, 41(23), 14723–14733
- **DOI:** 10.1080/10447318.2025.2487861
- **Publisher:** Taylor & Francis (Open Access, CC BY-NC-ND 4.0)
- **Venue Quality:** Peer-reviewed journal; IJHCI is a well-established HCI venue. Part of a programmatic research line by Loft's lab at UWA with multiple prior publications in Human Factors, Applied Ergonomics, and Cognitive Research.

## Section 2: Paper Type & Methodology
- **Type:** Empirical experimental study (between-/within-subjects mixed design)
- **Methodology:** Controlled laboratory experiment with 160 undergraduate participants. 2 (Transparency: low, high; within-subjects) × 2 (Trust Calibration Feedback: absent, present; between-subjects) mixed ANOVA design. 200 trials per participant in an uninhabited vehicle (UV) management task. Signal Detection Theory (SDT) metrics (d′, criterion c) for automation use accuracy.
- **Domain:** Military uninhabited vehicle management (decision support for UAV/UGV/USV selection)

## Section 3: Research Problem & Motivation
The paper addresses the challenge of calibrating human trust in automated decision aids. Inappropriate reliance manifests as either *misuse* (accepting incorrect advice due to over-trust) or *disuse* (rejecting correct advice due to under-trust). Two design principles are examined: (1) increased automation transparency (providing rationale behind advice), and (2) trust calibration feedback (explicitly notifying users when their trust is inappropriate and instructing corrective behaviour). The authors hypothesise these may interact synergistically — feedback would prompt users to scrutinise transparency information more carefully when trust has been historically inappropriate.

## Section 4: Key Concepts & Definitions
- **Automation bias:** Using automated output as a heuristic replacement for vigilant information processing (Mosier & Skitka, 1996)
- **Trust calibration:** Aligning trust with the automation's true capabilities/reliability
- **Misuse:** Accepting incorrect automated advice (over-reliance)
- **Disuse:** Rejecting correct automated advice (under-reliance)
- **Automation transparency:** Providing real-time understanding of AI system actions; operationalised via SAT model (Chen et al., 2014): Level 1 (purpose/intent), Level 2 (rationale), Level 3 (projected outcomes)
- **Trust calibration feedback:** Explicit notification of whether user trust was appropriate/inappropriate, with corrective instructions when inappropriate
- **Cognitive-miser hypothesis:** Humans prefer minimal cognitive effort in decision making, defaulting to heuristic acceptance of automation

## Section 5: Technical Approach / Architecture
No AI governance architecture per se. The study tests two design interventions:

**Transparency manipulation (within-subjects):**
- *Low transparency:* SAT Level 1 — table showing capability importance weightings only
- *High transparency:* SAT Levels 1+2+3 — table showing better/poorer UV per capability + graph showing Recommender's calculations including environmental factor impacts and projected scores

**Trust calibration feedback (between-subjects):**
- *Absent:* Post-trial feedback on human decision accuracy and automation accuracy only
- *Present:* Above + explicit "trust appropriate/inappropriate" message + when inappropriate: instruction to "take your time and check the [transparency] information more carefully"

**Automation characteristics:**
- Recommender was 75% reliable (25% incorrect advice)
- Error types: missed environmental factor, miscalculated factor impact, or combination
- 10% of correct-advice trials included non-consequential errors (to prevent simple error-detection heuristic)

## Section 6: Governance Mechanism Analysis

### Level 1 — G(S): Participation Governance
**Not implemented.** The automation is always ON; there is no state-conditioned mechanism to enable/disable AI participation. The Recommender provides advice on every trial regardless of conditions.

### Level 2 — A_AI(S): Advisory Scope Governance
**Not implemented.** The recommendation space is unconstrained — the Recommender always advises a full Plan A/Plan B selection regardless of environmental complexity or its own reliability state. There is no restriction of the advisory scope based on environmental conditions.

### Relationship to E → S = f(E) → (G(S), A_AI(S))
Environmental factors (terrain, weather symbols) are *inputs to the Recommender's calculation* but do not condition a governance state. There is no classified safety state S, no state-dependent governance pair, and no graduated restriction of advisory scope. Environmental factors affect *what* the AI recommends, not *whether* or *how much* it is permitted to recommend.

### Gap Assessment
**Binary per-trial governance only.** The user's decision is binary: accept Plan A or reject (select Plan B). Trust calibration feedback is binary: "appropriate" or "inappropriate." There is no intermediate CAUTION mode where the advisory scope is restricted but non-empty. The closest analogue is the transparency manipulation, which varies the *amount of information* provided, but this is a static within-block manipulation — not a runtime, state-conditioned governance response.

## Section 7: Formal Methods
Signal Detection Theory (SDT) applied rigorously:
- d′ (sensitivity): discriminability between correct and incorrect advice
- c (criterion): response bias toward agreeing with automation (negative = agree bias)
- Hit rate and correct rejection rate separated
- Mixed ANOVA with partial η² effect sizes (Cohen's benchmarks: 0.01, 0.06, 0.14)
- Extreme value correction for SDT (Macmillan & Kaplan, 1985)

No formal governance specification. No runtime safety constraints. No formal verification.

## Section 8: Key Findings

### Transparency effects (all significant):
- **Hit rate:** High > Low (0.93 vs. 0.88), F(1,156)=56.35, p<.001, η²=0.27 (large)
- **Sensitivity (d′):** High > Low (2.65 vs. 2.18), F(1,156)=41.85, p<.001, η²=0.21 (large)
- **Decision time:** High faster than Low (11.74s vs. 12.90s), F(1,156)=14.36, p<.001, η²=0.08 (medium)
- **Workload:** High lower than Low (3.88 vs. 4.35), F(1,156)=41.53, p<.001, η²=0.21 (large)
- **Trust:** High > Low (2.67 vs. 2.44), F(1,156)=15.13, p<.001, η²=0.09 (medium)
- **Usability:** High > Low (63.34 vs. 60.18), F(1,155)=5.82, p=.02, η²=0.04 (small)
- **Correct rejection rate:** No effect (p=.19) — automation bias persists
- **Criterion (bias):** Greater agree-bias with high transparency (c=−0.33 vs. −0.15), η²=0.22 (large)

### Trust calibration feedback effects:
- **No significant main effects** on any outcome variable (all p>.19)
- **No interaction with transparency** on any outcome variable
- Post-error slowing confirmed: slower decisions after incorrect vs. correct use (14.63s vs. 12.37s), F(1,152)=152.16, p<.001, η²=0.50 (very large) — but not modulated by trust feedback condition
- 68% of participants self-reported slowing down after inappropriate feedback (possible demand characteristics)

### Critical finding for dissertation:
Despite trust calibration feedback explicitly telling users their trust was inappropriate and instructing corrective behaviour, this had **zero measurable effect** on automation use accuracy, decision time, workload, trust, or usability. The authors attribute this partly to the baseline condition already providing decision/automation accuracy feedback, and partly to the static, repetitive phrasing of trust messages being easy to discount.

## Section 9: Strengths
- Large N (160) with adequate power for the mixed design
- Rigorous SDT decomposition separating sensitivity from bias — critical for understanding *why* accuracy changes
- Programmatic replication within established UV management paradigm strengthens cumulative evidence
- Clean separation of transparency and trust feedback effects
- Ecological validity via consultation with Australian Defence Science and Technology Group
- Open Access publication

## Section 10: Limitations (Author-Stated)
- Undergraduate student sample, not expert operators
- UV task does not capture full field complexity or multitasking demands
- Trust calibration feedback used fixed phrasing every trial (potentially easy to habituate/ignore)
- Baseline condition already included performance feedback, potentially obscuring incremental trust feedback effects
- No fatigue measures despite 2-hour experiment
- No cumulative reliability information provided (contrast with Okamura & Yamada, 2020)

## Section 11: Limitations (Analyst-Identified)
- **No environmental state classification:** Environmental factors affect the Recommender's calculation but are not classified into discrete safety states — prevents any mapping to graduated governance
- **Static transparency levels:** Low/high transparency is block-level, not runtime-adaptive; cannot serve as evidence for dynamic governance adjustment
- **Binary accept/reject decision:** The decision architecture offers no intermediate response option (e.g., "defer," "request more information," "proceed with caution") — the user must fully agree or fully disagree
- **No domain transfer evidence:** Military UV management is structurally different from safety-critical advisory systems where environmental risk directly threatens operator safety
- **Trust calibration feedback is post-hoc, not pre-emptive:** Feedback occurs *after* a decision, not as a runtime constraint *before* the AI produces advice — fundamentally different from pre-decision governance

## Section 12: Relevance to Dissertation

### Relevance Score: ⭐⭐⭐ (Moderate — Trust/Evaluation Support)

### Primary relevance:
1. **Empirical evidence that corrective feedback alone is insufficient** — even explicit "your trust is inappropriate" messaging failed to improve automation use. This *strengthens* the argument that architectural governance (structural restriction of advisory scope) is needed rather than merely informational interventions.
2. **Automation bias persists with transparency** — increased transparency increases agree-bias (c shifts negative), meaning users are *more* likely to uncritically accept advice when the system provides richer rationale. This directly motivates architectural constraints (A_AI(S)) rather than relying on user self-correction.
3. **SDT framework as evaluation methodology** — the hit rate / correct rejection / d′ / criterion decomposition is a rigorous model for PS4/PS5 evaluation design. Separating sensitivity from bias is exactly what is needed to test whether CAUTION mode reduces misuse without increasing disuse.

### Secondary relevance:
4. **Post-error slowing as behavioural marker** — the robust post-error slowing finding (η²=0.50) suggests a measurable behavioural signature of recalibration. In PS5, decision time following CAUTION-mode encounters could serve as a behavioural indicator of active recalibration.
5. **Expertise moderation noted but untested** — the authors acknowledge that novices exhibit greater automation bias than experts (citing Goddard et al., 2012; Mosier et al., 1992; Riley, 1996). This supports including expertise as a variable in PS5.

## Section 13: Specific Contribution to Gap Analysis
**Role: Counter-evidence to "feedback is sufficient" objection**

An examiner might argue: "Why do you need architectural governance (CAUTION mode)? Why not simply tell users when conditions are marginal and let them self-correct?" Tatasciore & Loft (2025) provides direct experimental evidence that this approach fails: explicit corrective feedback had zero effect on automation use accuracy, even when it specifically named the trust problem and prescribed corrective action. The architectural alternative — restricting the advisory scope itself (A_AI(S)) — addresses the problem at the system level rather than relying on human behavioural change that demonstrably does not occur.

Additionally, the finding that higher transparency *increases* automation bias (agree-bias) is a cautionary result: making the AI system more transparent does not solve over-reliance and may exacerbate it. This further motivates structural governance constraints.

## Section 14: Cross-References to Other Extracted Papers
- **Atf & Lewis (2026):** Their finding of weak correlation (r=0.194) between explainability and appropriate trust is consistent with Tatasciore & Loft's finding that transparency increases agree-bias — both suggest information provision alone is insufficient for trust calibration
- **Aquilino et al. (2025):** Cognitive trust dominance for low-anthropomorphism systems aligns with this paper's focus on system-level trust calibration mechanisms
- **McGrath et al. (2025) S-TIAS:** The trust measurement approach here (adapted Merritt, 2011, 6-item scale) is a precursor to the more refined S-TIAS instrument — S-TIAS remains preferable for PS5
- **Könighofer et al. (2025):** Their finding that intermediate ε outperforms binary extremes complements Tatasciore & Loft's null finding on binary trust feedback — both point toward graduated mechanisms being structurally superior to binary ones
- **Okamura & Yamada (2020):** Directly contrasted in the paper; their *adaptive* trust cues (only when over-trust detected) were effective, while this paper's *every-trial* feedback was not — relevant design consideration for any trust feedback component in the CAUTION state

## Section 15: Key Quotes for Potential Citation
- On automation bias: humans use automated output "as a heuristic replacement for vigilant information seeking and processing" (attributing Mosier & Skitka, 1996, p. 205)
- On trust calibration goal: "ensuring humans align their trust with the automation's true capabilities/reliability" — standard framing useful for Chapter 2
- On corrective feedback null result: the explicit instruction to "take your time and check the information more carefully" had no measurable effect — paraphrase for the architectural motivation argument

## Section 16: Citation Placement Recommendations
| Section | Role | Usage |
|---------|------|-------|
| **2.2 (Trust & Reliance)** | Background | Cite for trust calibration definitions, misuse/disuse framework, automation bias |
| **2.3 (Gap Argument)** | Gap evidence | Cite as evidence that informational interventions (feedback, transparency) are insufficient — motivating architectural governance |
| **Formalisation chapter** | Not applicable | No formal governance mechanisms to reference |
| **O5 / PS5 design** | Methodological | SDT framework (d′, criterion) as evaluation model; post-error slowing as behavioural marker; expertise moderation rationale |
| **Discussion** | Counter-argument | "Why not just provide feedback?" — direct experimental refutation |

## Section 17: Tracker Entry

```
| ID | Citation | Relevance | Role | Status |
| T&L-25 | Tatasciore & Loft (2025) IJHCI | ⭐⭐⭐ | Gap evidence (feedback insufficiency); PS5 methodology (SDT framework) | Extracted |
```

---

## Post-Extraction Commentary

### Strategic Value Assessment
This paper's greatest value is **defensive**: it pre-empts the examiner objection that informational interventions (transparency, corrective feedback) could substitute for architectural governance. The null result on trust calibration feedback is remarkably clean — no effect on *any* measured variable — making it a powerful citation for arguing that the CAUTION mode must operate at the *system architecture* level (restricting A_AI(S)) rather than the *user interface* level (telling users to be more careful).

### Argument Chain
The argument chain from this paper runs:
1. Transparency helps accuracy but *increases* automation bias (agree-bias)
2. Even explicit corrective feedback ("your trust is inappropriate — be more careful") produces zero behavioural change
3. Therefore, relying on users to self-correct when conditions are marginal is empirically falsified
4. Therefore, the system itself must restrict its advisory scope in marginal conditions (→ CAUTION mode with A_AI(S))

### Cluster Assignment
- **Primary cluster:** Trust & evaluation methodology
- **Secondary cluster:** Gap evidence (informational insufficiency)

### Limitation for Your Framework
Note that this paper's trust calibration feedback is *post-decision* (reactive), whereas your CAUTION mode operates *pre-decision* (proactive restriction). This is actually a strength for your argument: even reactive correction fails, so proactive architectural restriction is the stronger design. However, be precise about this distinction when citing — you are not arguing against feedback per se, but arguing that governance must be structural, not merely informational.
