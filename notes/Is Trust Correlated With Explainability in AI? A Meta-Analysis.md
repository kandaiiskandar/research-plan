# Methodological Foundation Paper Extraction

## Paper: Atf & Lewis (2026) — Is Trust Correlated With Explainability in AI? A Meta-Analysis

---

## 1. Paper Identity

- **Full title**: Is Trust Correlated With Explainability in AI? A Meta-Analysis
- **Authors**: Zahra Atf, Peter R. Lewis
- **Year**: 2026 (published online April 2025; journal issue March 2026)
- **Publication venue**: *IEEE Transactions on Technology and Society*, Vol. 7, No. 1
- **DOI**: 10.1109/TTS.2025.3558448
- **Type of paper**: Meta-analysis (90 studies synthesised; PRISMA protocol)
- **Open access**: Licensed (accessed via Universiti Malaysia Sabah institutional access)
- **Received / Accepted / Published**: 29 Mar 2024 / 30 Mar 2025 / 14 Apr 2025

---

## 2. Core Contribution

- **Problem addressed**: The widely held assumption in XAI research that enhancing explainability in AI systems inherently and substantially increases user trust. Empirical studies have yielded mixed results — some find trust increases with explanations, others find no effect or even negative effects — but no quantitative synthesis had established the overall effect size.
- **Proposed solution / key finding**: A meta-analysis of 90 studies reveals a **statistically significant but weak positive correlation** between AI explainability and trust (r = 0.194, 95% CI [0.174, 0.210], p < 0.001, random-effects model). This means explainability contributes to trust but is far from being the dominant or sole factor. The correlation falls in the "weak" range (0.1–0.3 on standard interpretation scales).
- **Additional key arguments**:
  - The study distinguishes between **Trust Enforcement** (presenting selective data to make users trust) and **Trust Empowerment** (providing all relevant information so users can determine their own trust level) — drawing on Lewis & Marsh (2022)
  - The study distinguishes between **trust** (subjective stakeholder belief) and **trustworthiness** (objective system property), arguing designers should focus on building trustworthiness rather than manipulating trust
  - Interpretable models can engender distrust as well as trust — they allow users to discern *whether* to trust, not simply to trust more (citing Rudin et al., 2022)
  - Complementary factors — ethical safeguards, bias management, socio-cultural context, user engagement — are necessary alongside explainability
- **What makes it foundational**: First large-scale meta-analysis quantifying the explainability–trust relationship across the XAI literature. Provides the definitive empirical basis for the claim that explainability alone is insufficient for trust, requiring a multifaceted approach.

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | No | Does not distinguish AI architecture types |
| Safety-critical AI decision-making | Partial | Discusses healthcare and autonomous vehicles as high-stakes XAI domains; notes trust is about confidence in correct/logical performance under complex conditions |
| AI governance / control mechanisms | Partial | Distinguishes Trust Enforcement vs Trust Empowerment — relevant to how governance states communicate restrictions to users |
| Low-resource environments | No | Not addressed; notes socio-cultural context as important but unstudied |
| Decision architecture formalisation | No | No architectural notation |
| Human role in decision-making | Yes | Central concern: how explanations shape human trust and reliance decisions |
| Socio-technical evaluation | Yes | Emphasises socio-technical framing of AI trust; argues trust requires ethical, cultural, and social dimensions beyond technical transparency |
| Coastal fisheries / maritime domain | No | No domain overlap |

---

## 4. Graduated Automation / Governance Framework

### Does the paper define levels, stages, or grades of automation or governance?

**No.** The paper does not address automation levels or graduated governance. Its independent variable is the presence/absence (or degree) of explainability, not system operational mode.

### Does it distinguish Level 1 (participation) from Level 2 (scope)?

**No.** However, the **Trust Enforcement vs Trust Empowerment** distinction has a structural parallel:
- Trust Enforcement ≈ binary governance that presents a fixed trust framing ("trust the system" or "don't trust it")
- Trust Empowerment ≈ graduated governance that provides users with enough information to calibrate their own trust to the system's actual governance state

### Does it include an intermediate mode analogous to CAUTION?

**No.** But the paper's core finding — that explainability has only a weak effect on trust — has implications for CAUTION mode design: simply *explaining* that the system is operating under restriction will not be sufficient to calibrate trust. Additional design elements (governance state transparency, scope communication, risk framing) are needed.

### Mapping to my three-mode governance model

| Paper's concept | My architecture's equivalent | Alignment |
|---|---|---|
| Explainability as trust factor | Governance state communication — explaining to users why AI is in SAFE/CAUTION/UNSAFE | Partial — explainability is one component of governance state communication |
| Trust Empowerment | Graduated governance designed to enable users to calibrate trust to system state | Strong conceptual alignment |
| Trust Enforcement | Binary governance that does not support user trust calibration | Strong — what the CAUTION mode is designed to avoid |
| Trustworthiness vs trust distinction | Governance architecture builds trustworthiness (objective); PS5 measures trust (subjective) | Strong — supports the design principle that G(S) should focus on trustworthiness; PS5 evaluates whether appropriate trust follows |
| Weak explainability–trust correlation | Implication: CAUTION mode explanation alone won't produce appropriate trust; must be combined with other design elements | Strong design implication |

---

## 5. Trust, Reliance, and User Response

### Does the paper address human trust in AI systems?

**Yes — trust is the dependent variable in the meta-analysis.**

### Does it define or operationalise trust?

**Yes.** The paper offers several trust framings:

1. **Technical trust** (adopted as the paper's primary focus): Confidence in the model's correct and logical performance under complex data conditions and sensitive outcomes. This represents the cognitive, performance-based dimension of trust — explicitly excluding emotional/psychological dimensions of interpersonal trust.

2. **Trust Enforcement vs Trust Empowerment** (from Dwyer et al. / Lewis & Marsh):
   - Trust Enforcement: Presenting selective data to instill trust — may involve manipulation
   - Trust Empowerment: Providing all relevant information, enabling users to determine their own trust level

3. **Trust vs Trustworthiness** (from Lewis & Marsh, 2022; Kästner et al., 2021):
   - Trust = subjective stakeholder belief/confidence
   - Trustworthiness = objective system property
   - Design focus should be on trustworthiness; trust should follow from genuine trustworthiness, not be engineered

### Does it propose or validate a measurement instrument?

**No.** The meta-analysis aggregates across diverse trust measures used in 90 studies (60 used quantitative surveys/questionnaires; 30 used qualitative methods). Trust was measured using quantitative surveys and questionnaires in the majority of included studies, but the paper does not develop or validate a specific instrument.

### Trust failure types

| Trust failure type | Addressed? | Detail |
|---|---|---|
| Overtrust / complacency | Yes | Explicitly discussed: explanations can lead to "over-reliance on incorrect information if not carefully managed" (citing Ayoub et al., 2021); chain-of-thought reasoning in LLMs may give "a misleading sense of how decisions are made" (citing Turpin, 2023) |
| Undertrust / disuse | Implicit | The paper notes that interpretable models can "engender distrust" as well as trust (citing Rudin et al., 2022), and that transparency about AI limitations can decrease trust |
| Misuse | Implicit | Discussed through "hallucination" risk — users relying on inaccurate AI outputs |

### Application to three governance modes

| Mode | Implication from meta-analysis |
|---|---|
| SAFE | Explaining how the AI works (XAI) will have only a weak positive effect on trust (r ≈ 0.19). Trust in SAFE mode will primarily come from system performance and perceived reliability, not from explanation alone |
| CAUTION | Simply explaining *why* AI is restricted will not be sufficient to calibrate trust appropriately. The weak explainability–trust correlation means CAUTION mode design must rely on multiple communication channels: governance state display, scope restriction clarity, risk framing, and possibly behavioural nudges |
| UNSAFE | Explaining why AI is disabled may help users accept the governance decision, but the meta-analysis suggests explanation alone accounts for very little trust variance. Users' trust in the UNSAFE classification will depend more on their trust in the underlying environmental assessment than on the explanation of why AI was disabled |

---

## 6. Mode Awareness and Automation Surprises

### Does the paper address mode confusion?

**No.** The term does not appear.

### Does it address automation surprises?

**Indirectly.** The paper discusses LLM "hallucination" as a form of automation surprise — where the system produces incorrect or misleading information that undermines trust. It also notes that chain-of-thought explanations may not accurately represent actual model reasoning, creating a mismatch between apparent and actual system behaviour.

### Implications for CAUTION mode design

The paper's finding that explainability has only a weak effect on trust has a critical design implication: **explaining the CAUTION mode will not be enough to make users understand and appropriately trust it.** The CAUTION mode is a novel governance state that users have never encountered. If explanations account for only ~4% of trust variance (r² ≈ 0.038), then the design of CAUTION mode communication must go beyond explanation to include:
- Visual/interface cues distinguishing CAUTION from SAFE and UNSAFE
- Concrete scope restriction information (what AI can and cannot recommend)
- Possibly experiential learning (users experiencing CAUTION mode before trusting/distrusting it)

---

## 7. Evaluation Methodology

### Meta-analytic approach

- **Protocol**: PRISMA systematic review
- **Databases**: Scopus, IEEE, Web of Science
- **Time window**: 2017–2024 (7 years, coinciding with DARPA XAI program and its research wave)
- **Initial pool**: 1,305 studies
- **Final sample**: 90 studies meeting statistical reporting criteria
- **Exclusion**: All studies lacking main statistical indicators (sample size, validity/reliability, correlation coefficients) and all purely qualitative/mixed studies without statistical indicators
- **Independent variable**: AI explainability (presence, type, or degree)
- **Dependent variable**: Trust (measured via quantitative surveys in 60 studies; qualitative methods in 30)

### Key statistical results

| Model | r | 95% CI | Z | p |
|---|---|---|---|---|
| Fixed effects | 0.204 | [0.194, 0.214] | 38.842 | 0.000 |
| Random effects | 0.194 | [0.174, 0.210] | 7.68 | 0.000 |

- **Heterogeneity**: High (Q-statistic significant), mandating random-effects model
- **Publication bias**: Minimal (symmetrical funnel plot)
- **Effect size interpretation**: r = 0.194 = weak positive correlation (0.1–0.3 range); r² ≈ 0.038, meaning explainability accounts for approximately 3.8% of variance in trust

### Study categorisation within the 90 papers

- 17 focused on data governance and ethical considerations
- 22 addressed algorithmic transparency and bias mitigation
- 18 explored user interface design for explainability
- 33 covered human-AI interaction, decision-making, and trust dynamics

### Does it evaluate transitions between automation levels?

**No.**

### Safety-critical contexts?

**Partial.** Healthcare and autonomous vehicles are discussed as critical XAI domains, but the meta-analysis aggregates across all domains without domain-specific subgroup analysis.

---

## 8. Applicability to PS4 (Comparative Evaluation: Graduated vs Binary Governance)

### Theoretical justification for comparing graduated vs binary control?

**Indirect but important.** The Trust Enforcement vs Trust Empowerment distinction maps directly to the binary vs graduated governance comparison:
- Binary governance (permit/block) is analogous to Trust Enforcement — it presents a fixed trust framing
- Graduated governance (SAFE/CAUTION/UNSAFE) is analogous to Trust Empowerment — it provides state-specific information enabling users to calibrate their own trust

The meta-analysis finding that explainability alone has only a weak effect on trust strengthens the argument for graduated governance: if simply explaining AI decisions doesn't substantially increase trust, then the governance architecture itself must be designed to support appropriate trust calibration through structural mechanisms (scope restriction, state communication), not just through explanation.

### Specific metrics for measuring the value of an intermediate mode?

**Not directly.** However, the meta-analysis provides a baseline: explainability alone produces r ≈ 0.19 correlation with trust. PS4 could test whether graduated governance combined with explanation produces a stronger effect than explanation alone — exceeding the 0.19 baseline would demonstrate that governance structure adds value beyond mere transparency.

### What to cite from this paper for PS4

- The r = 0.194 finding as evidence that explainability alone is insufficient for trust — justifying the need for structural governance mechanisms
- The Trust Enforcement vs Trust Empowerment distinction as theoretical framing for binary vs graduated governance
- The argument that focus should be on trustworthiness (system property) rather than manipulating trust (user state) — supporting the design principle that G(S) builds objective trustworthiness through governance

---

## 9. Applicability to PS5 (Socio-Technical Evaluation of CAUTION Mode)

### Validated instruments for measuring trust across governance modes?

**No.** The meta-analysis does not develop or validate instruments. It aggregates across diverse measures.

### Precedent for evaluating user understanding of intermediate automation states?

**No.** None of the 90 studies evaluated intermediate governance or automation modes.

### How to measure trust calibration?

**Indirectly relevant.** The paper's distinction between trust and trustworthiness suggests a measurement approach for PS5: measure both (a) the objective trustworthiness of the system in each governance state (defined by the architecture) and (b) the subjective trust users report (via S-TIAS). Trust calibration = alignment between (a) and (b). The meta-analysis suggests that explanation is insufficient to achieve this alignment, so PS5 should measure multiple factors contributing to trust calibration.

### How do users interpret system restriction?

**Not directly addressed.** However, the finding that interpretable models can engender distrust as well as trust (citing Rudin et al.) is directly relevant: when CAUTION mode makes the system's restriction transparent, this may engender appropriate caution (good) or inappropriate distrust (bad). PS5 must distinguish between these outcomes.

### What to cite from this paper for PS5

- The weak explainability–trust correlation as evidence that CAUTION mode communication cannot rely on explanation alone
- The Trust Empowerment concept as the design goal for CAUTION mode — providing users with state-specific information to calibrate their own trust, rather than enforcing a trust level
- The trust/trustworthiness distinction as a methodological principle — PS5 should measure trust (subjective) against a defined trustworthiness benchmark (objective governance state properties)

---

## 10. Key Concepts and Definitions

| Term / Framework | Definition | Location | Mapping to my research |
|---|---|---|---|
| **Explainability** | AI-focused term involving provision of mechanical or technical explanations of how a model works; often conflated with interpretability | Section II, ¶1 | One component of governance state communication; the meta-analysis shows it is necessary but insufficient for trust |
| **Explicability** | Broader philosophical concept emphasising accountability — ensuring stakeholders can understand and challenge AI outputs | Section II, ¶1 | Closer to what CAUTION mode communication needs: not just "how the AI works" but "why the governance decision was made and what it means for the user" |
| **Trust (technical)** | Confidence in the model's correct and logical performance under complex data conditions and sensitive outcomes | Section II, ¶2 | Maps to cognitive trust; the primary trust type expected in the DSR safety-critical context |
| **Trust Enforcement** | Presenting selective data to instill trust; a directive approach | Section IV, ¶1 (citing Lewis & Marsh, 2022; Dwyer et al.) | What binary governance risks becoming — presenting "AI on" or "AI off" without supporting user trust calibration |
| **Trust Empowerment** | Providing all relevant information enabling users to determine their own trust level | Section IV, ¶1 | The design goal of graduated governance — CAUTION mode should empower users to calibrate trust, not enforce a predetermined trust level |
| **Trust vs Trustworthiness** | Trust = subjective stakeholder belief; Trustworthiness = objective system property. Designers should focus on trustworthiness | Section V, ¶6 (citing Lewis & Marsh, 2022; Kästner et al., 2021) | Fundamental design principle: G(S) builds trustworthiness (objective governance); PS5 measures whether appropriate trust (subjective) follows |
| **Weak correlation (r = 0.1–0.3)** | Standard interpretation: values 0.1–0.3 indicate weak relationship; the explainability–trust correlation at r = 0.194 falls in this range | Section IV, ¶5 | Benchmark: if PS4 finds that graduated governance + explanation produces trust effects stronger than r ≈ 0.19, this demonstrates the added value of governance structure beyond mere explainability |

---

## 11. Quotable / Citable Points

1. **Weak explainability–trust correlation** (Section IV/VI): The meta-analysis of 90 studies finds a correlation of r = 0.194 between AI explainability and trust — statistically significant but weak, meaning explainability accounts for only ~4% of trust variance. *→ Cite when arguing that CAUTION mode communication cannot rely on explanation alone; governance structure must contribute independently to trust calibration.*

2. **Trust Enforcement vs Trust Empowerment** (Section IV): The distinction between forcing users to trust (by presenting selective information) and empowering users to calibrate their own trust (by providing complete information) is central to ethical AI governance. *→ Cite when framing graduated governance as Trust Empowerment — providing users with governance-state-specific information to make their own trust decisions.*

3. **Trustworthiness over trust** (Section V): Designers should focus on building system trustworthiness (objective property they can control) rather than attempting to manipulate subjective trust. *→ Cite when arguing that G(S) is designed to be objectively trustworthy (correct governance decisions), and PS5 evaluates whether trust follows naturally.*

4. **Interpretable models can engender distrust** (Section V, citing Rudin et al., 2022): Transparency allows users to discern *whether* to trust, not simply to trust more. *→ Cite when discussing the design challenge of CAUTION mode: making the restriction transparent may produce appropriate caution or inappropriate distrust, and PS5 must distinguish between these outcomes.*

5. **Multifaceted approach required** (Section VI): Trust in AI cannot be achieved solely through explainability but requires ethical safeguards, bias management, socio-cultural context understanding, and user engagement. *→ Cite when justifying the socio-technical evaluation approach (PS5) that goes beyond technical transparency to assess user understanding, trust calibration, and cultural context.*

---

## 12. Limitations and Gaps

### Stated limitations

- **Non-generative AI focus**: The meta-analysis primarily covers non-generative AI; generative AI explainability is acknowledged as a nascent domain
- **Heterogeneity**: High heterogeneity across the 90 studies (Q-statistic significant), reflecting diverse AI types, domains, explainability methods, and trust measures — mitigated by random-effects model but limits specificity of the aggregate finding
- **No domain-specific subgroup analysis**: The r = 0.194 is an aggregate across all domains; the explainability–trust relationship may differ in safety-critical vs low-stakes contexts
- **Trust measurement diversity**: The 90 studies used heterogeneous trust measures (60 quantitative, 30 qualitative), making aggregation approximate

### Gaps my research could address

| Gap | How my research addresses it |
|---|---|
| No analysis of how explainability interacts with **governance structure** | My architecture provides graduated governance (G(S)) as a structural mechanism that operates alongside but independently of explainability |
| No examination of explainability's trust effect in **intermediate/restricted AI modes** | PS5 evaluates whether explaining the CAUTION mode restriction improves trust calibration beyond the r ≈ 0.19 baseline |
| No domain-specific analysis for **safety-critical decision support** | PS4/PS5 evaluate trust in a specific safety-critical domain (coastal fisheries) |
| No examination of trust in **low-resource or non-Western contexts** | PS5 targets Malaysian coastal fishing communities |
| The trust/trustworthiness distinction is raised theoretically but not **operationalised for evaluation** | PS4 defines governance-appropriate trust levels (trustworthiness benchmarks) and PS5 measures whether actual trust (S-TIAS) aligns with them |
| No examination of **state transition effects** on the explainability–trust relationship | PS5 measures trust across SAFE → CAUTION → UNSAFE transitions |

### What this paper does NOT cover that my research needs

- A specific trust measurement instrument (provided by McGrath et al., 2025)
- Evaluation of trust in systems that operate in multiple distinct modes
- Mode awareness / comprehension measurement
- Operational trust calibration metrics (how to quantify the gap between measured trust and appropriate trust)

---

## 13. Positioning in My Literature Review

### Role in the argumentative chain

- **Link 8 (supporting)**: Provides quantitative evidence that explainability alone is insufficient for trust, strengthening the argument that graduated governance architecture provides necessary structural trust support beyond mere transparency
- **Link 9 (supporting)**: Confirms that no study in the 90-paper corpus evaluated trust across intermediate AI governance modes — gap confirmation
- **Theoretical grounding**: The Trust Enforcement vs Trust Empowerment distinction provides the normative framing for why graduated governance is preferable to binary governance

### Role in the literature review

- ✅ Provides **theoretical grounding** for graduated governance as a trust-enabling design choice (not just transparency-enabling)
- ✅ Provides **quantitative evidence** (r = 0.194) that explainability alone is insufficient — justifying the need for structural governance mechanisms
- ✅ Provides **normative framework** (Trust Empowerment vs Trust Enforcement) applicable to governance design
- ❌ Does NOT provide validated instruments for PS4/PS5
- ❌ Does NOT address intermediate governance modes empirically
- ❌ Does NOT address safety-critical or low-resource contexts specifically

### Gap statement

This paper establishes through meta-analysis of 90 studies that AI explainability has only a weak positive correlation with trust (r = 0.194), demonstrating that transparency alone is insufficient for building appropriate trust. It further argues that the design focus should be on building system trustworthiness (an objective property) rather than manipulating subjective trust, and that trust requires a multifaceted approach including ethical, cultural, and social dimensions beyond technical transparency. However, the meta-analysis does not examine how structural governance mechanisms — such as state-conditioned AI participation and advisory scope restriction — interact with explainability to produce trust calibration. My research extends this by implementing a graduated governance architecture (G(S), A_AI(S)) where the governance structure itself is designed to support trust calibration through distinct operational modes, and evaluating whether this structural approach produces better trust outcomes than explainability alone, in a safety-critical, low-resource deployment context.

---

## 14. Overall Relevance Score

### ⭐⭐⭐ Medium

**Justification**: This paper provides an important quantitative finding (r = 0.194) and useful theoretical distinctions (Trust Enforcement vs Empowerment; trust vs trustworthiness) that strengthen the argumentative case for graduated governance. However, it operates at a high level of abstraction — it is a meta-analysis of the XAI field, not a targeted study of governance, safety-critical systems, or trust measurement methodology. Its contribution to my research is primarily at the *justification* level: explaining why governance architecture must go beyond explainability to support trust calibration. It does not provide instruments, specific evaluation methods, or direct precedent for PS4/PS5 design.

It falls short of ⭐⭐⭐⭐ because: (a) no validated instrument provided, (b) no governance-specific analysis, (c) no domain-specific findings for safety-critical contexts, and (d) the r = 0.194 finding, while useful as a benchmark, does not directly inform PS4/PS5 methodology.

**Role cluster**: Trust theory / explainability limitation evidence / governance design rationale

**Recommended citation uses**:
1. **Literature review, explainability–trust subsection**: Cite the r = 0.194 finding as definitive evidence that explainability alone is insufficient for trust
2. **Architecture design rationale**: Cite Trust Enforcement vs Trust Empowerment when framing graduated governance as enabling user trust calibration
3. **PS4 justification**: Cite when arguing that PS4 tests whether governance structure adds trust value beyond what explainability alone provides (exceeding the r ≈ 0.19 baseline)
4. **PS5 discussion**: Cite the trustworthiness vs trust distinction when interpreting whether measured trust levels reflect objective governance appropriateness
5. **Discussion chapter**: Cite when situating findings within the broader XAI-trust literature — if PS4/PS5 show governance effects stronger than r ≈ 0.19, this demonstrates architectural contribution beyond the explainability baseline

**Pairing**: Cite alongside McGrath et al. (2025) and Aquilino et al. (2025) — this paper establishes *why* explanation is insufficient (r = 0.194), Aquilino et al. establishes *what types* of trust are relevant (cognitive > affective for decision support), and McGrath et al. provides *how* to measure trust (S-TIAS).
