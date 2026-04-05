# Methodological Foundation Paper Extraction

## Paper: Bach et al. (2024) — A Systematic Literature Review of User Trust in AI-Enabled Systems: An HCI Perspective

---

## 1. Paper Identity

- **Full title:** A Systematic Literature Review of User Trust in AI-Enabled Systems: An HCI Perspective
- **Authors:** Tita Alissa Bach, Amna Khan, Harry Hallock, Gabriela Beltrão, Sonia Sousa
- **Year:** 2024 (published online November 2022)
- **Venue:** *International Journal of Human–Computer Interaction*, 40(5), 1251–1266 (Taylor & Francis — peer-reviewed)
- **DOI:** https://doi.org/10.1080/10447318.2022.2138826
- **Type:** Systematic literature review (PRISMA-compliant) of 23 empirical studies on user trust in AI-enabled systems
- **Citation count:** 195 citing articles; 45,637 article views — **highly cited and established as a reference work**
- **Funding:** EU Horizon 2020 (AI-Mind project, grant 964220); US Air Force Office of Scientific Research (Trust and Influence Programme FA8655-22-1-7051)

---

## 2. Core Contribution

- **Problem addressed:** User trust in AI-enabled systems is recognised as key to adoption, but there is no consolidated overview of how trust is defined, what factors influence it, and how it is measured — particularly from an HCI (human-centric) perspective focused on the user-AI relationship.
- **Proposed solution:** A PRISMA-compliant systematic review of 23 empirical studies synthesising: (1) trust definitions used, (2) factors influencing user trust (organised into three themes: socio-ethical considerations, technical/design features, user characteristics), and (3) measurement methods.
- **What makes this paper foundational:** It consolidates the empirical evidence base for user trust in AI systems into a structured taxonomy of influencing factors, identifies the dominant trust definitions in use (Mayer et al. 2006; Lee & See 2004), catalogues measurement methods, and identifies critical gaps — particularly the lack of cross-context validated trust instruments and the absence of research in non-Western settings. With 195 citations and 45K+ views, it is a well-established reference in the HCI-trust literature.

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | No | Not addressed — focuses on user trust, not AI architecture |
| Safety-critical AI decision-making | Partial | Includes healthcare AI (Barda et al. 2020), robotic surgery (O'Sullivan et al. 2019), and workplace information systems (Thielsch et al. 2018) — but safety-criticality is not a central organising concept |
| AI governance / control mechanisms | Partial | Discusses accountability structures (O'Sullivan et al. 2019), ethical-legal boundaries, and the need for mechanisms to foster, maintain, and recover trust — but not formalised governance architectures |
| Low-resource environments | No | Studies predominantly from USA (30.43%) and Germany (26.09%); paper explicitly identifies geographical diversity as a gap |
| Decision architecture formalisation | No | No formal architectural models |
| Human role in decision-making | Yes | Central focus — the entire review is structured around the user-AI relationship; identifies user characteristics as the dominant factor category influencing trust |
| Socio-technical evaluation | Yes | Explicitly adopts HCI (human-centric) perspective; identifies socio-ethical considerations, user attitudes, and user-system interaction quality as trust determinants |
| Coastal fisheries / maritime domain | No | Not addressed |

**Early relevance gate:** This paper has **high relevance** as a methodological foundation. It provides the empirical evidence base and conceptual taxonomy for understanding user trust in AI systems — directly informing PS5's socio-technical evaluation design. Its identification of trust definitions, influencing factor categories, and measurement methods provides the conceptual infrastructure for evaluating user response to the CAUTION governance mode.

---

## 4. Graduated Automation / Governance Framework

### Does the paper define levels, stages, or grades of automation, autonomy, or system control?

**No.** The paper does not define graduated automation levels. It reviews trust in AI-enabled systems as a general category without distinguishing between different automation levels or governance modes.

### Does the framework distinguish Level 1 (participation) from Level 2 (advisory scope)?

**No.** The paper treats AI-enabled systems as either present or absent in the interaction — there is no concept of AI participating under different scope restrictions.

### Does the framework include an intermediate mode analogous to CAUTION?

**No explicit intermediate mode.** However, the paper identifies a relevant finding: user trust is **multidimensional and continuous**, not binary (Elkins & Derrick 2013). Trust increases over time through interaction, and users adjust expectations through experience. This supports the conceptual validity of an intermediate governance state — if trust is continuous rather than binary, then governance should also be graduated rather than binary.

Additionally, the paper documents that when users are **heavily dependent** on a system but cannot fully understand or control it, they may trust it simply because they perceive no alternative (Foehr & Germelmann 2020; Thielsch et al. 2018). This "perceived inescapability" trust pattern is directly relevant to understanding how CAUTION mode might be received — users may trust restricted AI not because they understand the restriction, but because some AI participation is perceived as better than none.

### Mapping to my architecture

| Paper's concept | My architecture's equivalent | Alignment |
|---|---|---|
| Trust as multidimensional and continuous (not binary) | Graduated governance S ∈ {SAFE, CAUTION, UNSAFE} | **Partial** — conceptual alignment (trust is not binary → governance should not be binary), but paper does not operationalise graduated modes |
| User-AI relationship as central construct | Human role in (G(S), A_AI(S)) decision architecture | **Partial** — paper focuses on user-system trust relationship; my architecture formalises the human role within governance structure |
| Mechanisms to foster, maintain, recover trust | Governance state communication design | **Partial** — paper identifies need for trust recovery mechanisms; CAUTION mode must communicate restriction clearly to maintain trust |
| Perceived inescapability driving trust | User response to CAUTION mode | **Weak** — users may accept restricted AI because some AI is perceived as better than none |

### Does the paper argue graduated control is superior to binary control?

**Not directly.** However, the finding that trust is continuous and context-dependent (not binary on/off) provides indirect support. The paper argues that "calibrating the user-AI relationship requires finding the optimal balance that works for not only the user but also the system" (Section 5). This calibration argument implies that binary (full trust / no trust; full AI / no AI) is insufficient — graduated approaches are needed to find the optimal balance.

### Does the paper identify risks of binary automation control?

**Indirectly.** The paper identifies that a **mismatch between user expectations and system behaviour** is a risk to trust (Lee et al. 2021; Thielsch et al. 2018). If an AI system is either fully on or fully off, any transition between states is abrupt and creates expectation mismatch. Graduated governance could mitigate this by providing an intermediate state that manages the transition.

---

## 5. Trust, Reliance, and User Response

### Does the paper address human trust in AI systems?

**Yes — this is the paper's core focus.** It systematically reviews how trust is defined, what influences it, and how it is measured across 23 empirical studies.

### Does it define or operationalise trust in a measurable way?

**Yes.** The paper catalogues seven explicit trust definitions from the included studies. The two dominant definitions are:

1. **Mayer et al. (2006)** — used by 4 studies: "The willingness of a party to be vulnerable to the actions of another party based on the expectation that the other will perform a particular action important to the trustor, irrespective of the ability to monitor or control that other party."

2. **Lee & See (2004)** — used by 2 studies: "The attitude that an agent will help achieve an individual's goals in a situation characterized by uncertainty and vulnerability."

The paper recommends selecting trust definitions based on context: Mayer's definition suits contexts where AI output has **significant personal impact** (health, finance), while Lee & See's suits contexts with **less personal impact** (workplace information systems). This context-sensitivity finding is directly relevant to the DSR architecture — the SAFE, CAUTION, and UNSAFE states represent different risk contexts that may require different trust operationalisations.

### Does it propose or validate a measurement instrument?

**The paper catalogues instruments used across the 23 studies:**

| Instrument | Source | Used by |
|---|---|---|
| Trust in Automation (TiA) questionnaire | Jian et al. (2000) | Weitz et al. (2021) |
| Multidimensional Measure of Trust (MDMT) — 20 items | Ullman & Malle (2018) | Law et al. (2021) |
| Trust scale for websites | Schlosser et al. (2006) | Sharma (2015) |
| 34-item trust questionnaire | Corritore et al. (2007) | Corritore et al. (2012) |
| Human-Computer Trust Scale (HCTS) — 12 items | Gulati et al. (2019) | Referenced as a recommended validated instrument |
| Custom questionnaires (7-point / 9-point Likert) | Various | 12 of 16 survey-based studies (75%) |

**Critical finding for PS5:** 75% of studies developed their own questionnaires rather than using validated instruments. The paper explicitly identifies this as a concern: "if user trust can be understood and measured in different ways, then being able to build upon the concept becomes challenging." It recommends using **validated cross-context instruments** such as the 12-item HCTS (Gulati et al. 2019).

**Implication for PS5 design:** PS5 should use established validated instruments (Jian et al. 2000 TiA scale; or Gulati et al. 2019 HCTS) rather than developing custom questionnaires, to enable comparability with existing literature.

### Does the paper distinguish trust failure types?

**Partially, through the influencing factors taxonomy rather than formal trust failure categories:**

- **Overtrust / complacency:** The paper finds that when users have **no choice but to use** an AI-enabled system, they trust it regardless of its reliability (Thielsch et al. 2018) — this forced dependency creates complacency risk. Also, "perceived inescapability" of AI drives trust not through understanding but through resignation (Foehr & Germelmann 2020).

- **Undertrust / disuse:** The paper identifies that users **without college education** were less likely to trust AI systems, potentially due to unfamiliarity or perceived non-benevolence (Elkins & Derrick 2013). Initial low trust can improve over time through interaction — but if the system is not designed to support this trust-building process, undertrust persists.

- **Misuse:** Not explicitly discussed as a trust failure category, but the paper notes that AI "could mislead users into unfair and even incorrect decision-making" when poorly designed (Lakkaraju & Bastani 2020, cited in Introduction).

### Application to three governance modes

| Governance mode | Trust challenge from this paper | Design implication |
|---|---|---|
| **SAFE** (full AI) | Risk of overtrust through perceived inescapability — users may trust system because they perceive no alternative, not because they understand it | SAFE mode must still communicate system limitations; transparency mechanisms needed |
| **CAUTION** (restricted AI) | **Novel territory** — no study in this review evaluates user response to a restricted-but-active AI mode. The closest finding: trust increases through interaction and is multidimensional, suggesting users can develop calibrated trust in a restricted mode if the restriction is clearly communicated | CAUTION mode communication design is critical; user interaction patterns must support trust calibration |
| **UNSAFE** (AI disabled) | Risk of undertrust carrying over — if users have been interacting with AI in SAFE or CAUTION modes, sudden AI disablement may create expectation mismatch and erode trust in the overall system | Transition from CAUTION→UNSAFE must be clearly explained; safety classification rationale must be transparent |

---

## 6. Mode Awareness and Automation Surprises

### Does the paper address mode confusion?

**Not directly by name.** However, the paper identifies two closely related phenomena:

1. **Expectation mismatch:** "User expectations of an AI-enabled system might not be aligned with the intention of the system's investors and developers" (Lee et al. 2021). When the system operates differently from expectations, trust is at risk. This is functionally equivalent to mode confusion — users expect AI to behave one way but it behaves differently.

2. **Trust recalibration difficulty:** When users interact with a system over time, they build expectations. The paper notes that "a mismatch of readiness levels might lead to low user trust" (Lee et al. 2021). Sudden changes in system behaviour (e.g., transitioning from SAFE to CAUTION) would create exactly this readiness mismatch.

### Does it address automation surprises?

**Indirectly.** The paper identifies that AI's inherent opacity makes it "harder to predict how AI may behave" (Bathaee 2017, cited in Introduction). This unpredictability is the root cause of automation surprises. The paper recommends explanations of AI actions and model performance as trust-building technical features — these would help mitigate automation surprises.

### Application to CAUTION mode

The paper provides no direct findings about user response to a restricted-but-active AI mode. However, its findings generate clear design implications:

1. **CAUTION mode must be clearly distinguished from SAFE mode.** The paper shows that users build expectations through interaction (Elkins & Derrick 2013). If CAUTION mode *looks* like SAFE mode but *behaves* differently (restricted recommendations), users will experience expectation mismatch — a form of mode confusion.

2. **The restriction must be explained, not just indicated.** The paper identifies that explanations of "how the algorithm worked" and "reflections of AI reliability" increase trust (Barda et al. 2020; Glikson & Woolley 2020). For CAUTION mode, this means explaining *why* the AI is operating under restriction (environmental conditions) and *what* types of recommendations are still available.

3. **Trust recovery mechanisms are needed for mode transitions.** The paper identifies the need for mechanisms to "foster, maintain, and recover user trust" (Binmad et al. 2017). Transitions between governance states (especially CAUTION→UNSAFE) are trust-vulnerable moments requiring explicit trust recovery support.

---

## 7. Evaluation Methodology

### Does the paper describe evaluation methods for measuring human response to AI?

**Yes — this is one of its three core contributions.** The paper catalogues measurement methods across 23 empirical studies:

| Method | N studies | % |
|---|---|---|
| Survey (standalone) | 13 | 56.52% |
| Survey + interviews/focus groups | 3 | 13.04% |
| Literature review | 3 | 13.04% |
| Multiple qualitative methods | 3 | 13.04% |
| Simulation experiment | 1 | 4.35% |

### Experimental designs used

The 23 studies used varied designs:

- **Experimental user studies** (Weitz et al. 2021; Law et al. 2021; Elkins & Derrick 2013): Controlled designs manipulating system features and measuring trust response
- **Surveys with large samples** (Zhang, Genc et al. 2021: N=3423; Yan et al. 2013: N=1120): Cross-sectional designs measuring trust correlates
- **Qualitative studies** (Foehr & Germelmann 2020; Lee et al. 2021; Klumpp & Zijm 2019): Interviews, focus groups, expert workshops exploring trust factors
- **Simulation experiments** (Binmad et al. 2017; Zhou et al. 2020): Controlled simulations measuring trust under different conditions

### Dependent variables measured

- User trust (all 23 studies)
- Trust over time / trust development (Elkins & Derrick 2013; Lee et al. 2021)
- User acceptance and readiness (Foehr & Germelmann 2020; Khosrowjerdi 2016)
- Cognitive load (Zhou et al. 2020)
- Personality traits influence on trust (Zhou et al. 2020)
- User perceived credibility, risk, ease of use (Corritore et al. 2012; Foehr & Germelmann 2020)

### Independent variables manipulated

- System features: anthropomorphism, social presence, explainability, voice characteristics
- User characteristics: personality traits, education level, prior experience, gender
- Context factors: time spent interacting, cognitive load, dependency on system

### Validated scales or instruments adaptable for PS4/PS5

**Directly usable instruments identified:**

1. **Trust in Automation (TiA) scale** (Jian et al. 2000) — validated, widely cited, used by Weitz et al. (2021). Measures trust in automated systems. **Recommended for PS4/PS5** — applicable to comparing trust across governance modes.

2. **Multidimensional Measure of Trust (MDMT)** — 20 items (Ullman & Malle 2018) — used by Law et al. (2021). Measures multiple trust dimensions. **Potentially adaptable for PS5** — could capture different trust dimensions across SAFE/CAUTION/UNSAFE modes.

3. **Human-Computer Trust Scale (HCTS)** — 12 items (Gulati et al. 2019) — recommended by the paper as a cross-context validated instrument. **Recommended for PS5** — designed specifically for cross-context comparability.

### Does the evaluation include safety-critical context?

**Partially.** Healthcare contexts: Barda et al. (2020) on ML predictions in pediatric critical care; O'Sullivan et al. (2019) on robotic surgery. Workplace information systems where trust failure has operational consequences: Thielsch et al. (2018). But no maritime, aviation, or environmental safety context.

---

## 8. Applicability to PS4 (Comparative Evaluation of Graduated vs Binary Governance)

### Theoretical justification for graduated vs binary comparison

**Moderate.** The paper's finding that trust is "multidimensional and continuous" (Elkins & Derrick 2013) and that "calibrating the user-AI relationship requires finding the optimal balance" (Section 5) provides conceptual justification for why binary governance (full AI vs. no AI) is insufficient — graduated governance better supports the continuous, multidimensional nature of trust.

### Specific metrics for measuring intermediate mode value

**Not directly.** However, the paper's three-category taxonomy of trust influencing factors (socio-ethical considerations, technical/design features, user characteristics) provides a measurement framework. PS4 could measure whether graduated governance (compared to binary):
- Better aligns with user expectations (user attitudes dimension)
- Produces more appropriate trust calibration (neither overtrust nor undertrust)
- Supports trust development over time through interaction quality

### What "better" means

The paper implicitly defines "better" as:
- **Better calibrated trust** — users trust the system appropriately for its actual capabilities in each mode
- **Reduced expectation mismatch** — user expectations align with system behaviour
- **Sustained trust over time** — trust develops and is maintained through quality interactions

### Experimental design considerations

- The paper's finding that 75% of studies used custom questionnaires argues for using **established validated instruments** in PS4/PS5
- Sample sizes ranged from 21 to 3423 (M=326.80) — PS4 should aim for at least medium sample sizes
- The paper identifies surveys as dominant but recommends supplementing with qualitative methods and potentially **psychophysiological signals** (Section 5) for more objective trust measurement
- Geographic concentration in USA/Germany is identified as a limitation — PS5's Malaysian context would address this gap

### Citable elements for PS4

- Trust is multidimensional and continuous, not binary — supports graduated governance design
- Trust calibration requires finding an optimal balance — supports the CAUTION mode as a calibration mechanism
- Expectation mismatch between user expectations and system behaviour is a trust risk — supports the argument that transitions between governance states must be carefully designed
- 75% of studies used custom questionnaires — supports the argument for standardised instruments in PS4

---

## 9. Applicability to PS5 (Socio-Technical Evaluation of CAUTION Mode)

### Validated instruments for measuring user trust across governance modes

**Yes — three instruments identified:**

1. **TiA scale (Jian et al. 2000):** Validated for trust in automated systems. Could be administered across SAFE/CAUTION/UNSAFE conditions to measure trust differences.
2. **HCTS (Gulati et al. 2019):** 12-item validated cross-context instrument. Recommended by the paper for cross-context comparability — suitable for measuring trust across governance modes.
3. **MDMT (Ullman & Malle 2018):** 20-item multidimensional measure. Could capture which trust dimensions (reliability, competence, etc.) are differentially affected by governance mode.

### Precedent for evaluating user understanding of intermediate automation states

**None.** This is explicitly a gap. The paper's 23 studies evaluate trust in AI systems that are either present or absent — no study evaluates user response to a system operating under restriction. This gap directly supports the novelty claim for PS5.

### Trust calibration measurement

**Partially addressed.** The paper identifies that trust should be "calibrated" — users should trust the system appropriately for its capabilities. However, no operationalised trust calibration measure is provided. The paper's taxonomy suggests measuring:
- Whether users understand what the system can and cannot do in each mode (understandability)
- Whether users adjust their reliance behaviour appropriately across modes (reliance calibration)
- Whether users perceive the governance mode as appropriate for the conditions (perceived appropriateness)

### User interpretation of system restriction

**Not directly addressed.** However, the paper's findings on user attitudes suggest several hypotheses for CAUTION mode:

- Users who perceive AI as **useful** are more likely to trust it (Foehr & Germelmann 2020) → If CAUTION mode restricts usefulness, trust may decrease unless the restriction rationale is clear
- Users who can **relate to** and **understand** the system's rationale show higher trust (Thielsch et al. 2018; Zhang, Genc et al. 2021) → CAUTION mode must explain *why* restrictions exist
- Users who perceive **no alternative** may trust by default (Foehr & Germelmann 2020) → In safety-critical contexts, restricted AI may still be trusted because some AI is better than none
- **Personality traits** moderate trust (Zhou et al. 2020) → PS5 should control for or measure personality traits

### Citable elements for PS5

- User trust is influenced by three themes (socio-ethical, technical/design, user characteristics) — provides structured framework for PS5 evaluation dimensions
- Trust increases through interaction and is continuous over time — supports longitudinal or repeated-measures PS5 design
- Mayer et al. (2006) and Lee & See (2004) are the dominant trust definitions — PS5 should adopt one explicitly with justification
- 75% of studies used custom instruments, creating comparability problems — justifies PS5's use of validated instruments
- Geographic concentration in Western countries is a gap — PS5's Malaysian coastal context directly addresses this
- No study evaluates user trust across intermediate AI operation modes — supports PS5's novelty claim

---

## 10. Key Concepts and Definitions

| Term | Definition | Location | Mapping to my research |
|---|---|---|---|
| **Trust (Mayer et al. 2006)** | "The willingness of a party to be vulnerable to the actions of another party based on the expectation that the other will perform a particular action important to the trustor, irrespective of the ability to monitor or control that other party" | Table 4 | Candidate trust definition for PS5 — suits high-personal-impact contexts (safety-critical fisheries decisions) |
| **Trust (Lee & See 2004)** | "The attitude that an agent will help achieve an individual's goals in a situation characterized by uncertainty and vulnerability" | Table 4 | Alternative trust definition for PS5 — emphasises uncertainty and vulnerability, directly relevant to safety-critical environmental conditions |
| **AI-enabled system** | "AI systems with capabilities to improve existing systems' performance (AI-enhanced) and/or develop new applications (AI-based)" | Section 1 | The DSR architecture is an AI-enabled decision support system — this definition positions it within the reviewed literature |
| **Socio-ethical considerations (trust factor)** | Environmental/contextual factors including accountability structures, data protection, communication mechanisms, ethical-legal boundaries | Section 3.2.1 | Evaluation dimension for PS5 — how do governance state communication and accountability structures affect trust? |
| **Technical and design features (trust factor)** | System features including explainability, anthropomorphism, integrity, social presence, information quality | Section 3.2.2 | Evaluation dimension for PS5 — how does governance state indication design affect trust? |
| **User characteristics (trust factor)** | Inherent (personality, gender), acquired (experience, education), attitudinal (acceptance, expectations, perceptions), external (cognitive load, time, usage) | Section 3.2.3 | Moderating variables for PS5 — must control for user characteristics when measuring trust across governance modes |
| **Trust as multidimensional and continuous** | Trust is not binary; it changes over time and across contexts; it has multiple dimensions | Section 3.2.3.4 | Supports graduated governance design — if trust is graduated, governance should be too |
| **Expectation mismatch** | User expectations of AI may not align with system capabilities or developer intentions, creating trust risk | Section 3.2.3.3 | Mode transition design — transitions between SAFE/CAUTION/UNSAFE must manage expectation mismatch |
| **Artificial divide** | "The ability or lack thereof to cooperate successfully with AI-enabled systems" (Klumpp & Zijm 2019) | Section 3.2.3.3 | Relevant to low-resource deployment — fishers with varying technical literacy may experience artificial divide |

---

## 11. Quotable / Citable Points

1. **Trust is multidimensional and continuous:** "User trust was thus suggested as multidimensional and continuous, and that human-system interactions were crucial to user trust development" (Elkins & Derrick 2013, as synthesised in Section 3.2.3.4) — supports the argument that binary governance (AI on/off) fails to match the continuous, multidimensional nature of trust.

2. **Calibration requires optimal balance:** "Calibrating the user-AI relationship requires finding the optimal balance that works for not only the user but also the system" (Section 5) — directly supports the CAUTION mode as a calibration mechanism between full AI participation and AI exclusion.

3. **Custom instruments undermine comparability:** "If user trust can be understood and measured in different ways, then being able to build upon the concept becomes challenging" (Section 4.3) — justifies using validated instruments (TiA, HCTS) in PS4/PS5 rather than developing custom questionnaires.

4. **Context-specific trust definitions needed:** "Instead of pursuing better trust definitions or comparing which definitions are better, it is probably more beneficial to select the most appropriate trust definition according to the context" (Section 4.1) — supports choosing Lee & See (2004) for the DSR context given its emphasis on uncertainty and vulnerability in goal achievement.

5. **Geographic gap in trust research:** "Approximately half of the studies included in this review were conducted in the USA and Germany, highlighting that future research should be conducted in more diverse geographical locations to help understand how cultural factors influence user trust" (Section 5) — directly supports PS5's value in conducting trust evaluation in a Malaysian coastal community context.

---

## 12. Limitations and Gaps

### Stated limitations

- The 23 studies cover different contexts — generalisation should be done with caution
- Search terms may be perceived as too narrow
- Grey literature excluded
- Trust definitions beyond those in the 23 studies may exist

### Gaps my research could address

| Gap in this paper | How my research addresses it |
|---|---|
| **No study evaluates user trust across AI operation modes** — all 23 studies evaluate trust in AI that is either present (on) or absent (off) | PS5 evaluates trust across three governance modes (SAFE/CAUTION/UNSAFE), including the novel intermediate CAUTION state |
| **No intermediate AI mode evaluated** — no study examines user response to AI operating under restriction | The CAUTION mode is precisely this — AI active but with restricted advisory scope; PS5 evaluates user understanding and trust in this mode |
| **Geographic concentration in Western countries** — USA (30.43%) and Germany (26.09%) dominate | PS5 is conducted in Malaysian coastal communities — non-Western, low-resource context |
| **User characteristics influence unclear across contexts** — "it is still unclear how these factors fit to distinct types of users and contexts and/or change over time" (Section 5) | PS5 evaluates trust among coastal fishers — a specific user group with distinct characteristics (domain expertise, varying technical literacy, safety-critical decision context) |
| **Measurement instrument fragmentation** — 75% developed custom instruments | PS4/PS5 will use established validated instruments (TiA or HCTS) to enable cross-study comparability |
| **No safety-critical environmental context** — closest is healthcare (4 studies) and robotic surgery (1 study) | The DSR operates in an environmental safety-critical context (sea state assessment for fishing trip decisions) |
| **No trust evaluation across governance transitions** — no study examines how trust changes when a system shifts between modes | PS5 can evaluate trust during SAFE→CAUTION and CAUTION→UNSAFE transitions |

---

## 13. Positioning in My Literature Review

### Role in the argumentative chain

- **Link 9 (directly):** Supports the claim that no socio-technical evaluation of user response to an intermediate AI governance mode (CAUTION) exists. This paper's comprehensive review of 23 empirical studies confirms that all existing trust research examines AI that is either fully present or fully absent — no study evaluates trust in AI operating under restriction.
- **Link 8 (indirectly):** The paper's finding that trust is multidimensional and continuous supports the theoretical argument that binary governance is insufficient and graduated governance should produce better-calibrated trust.

### Role in the literature review

- Provides **validated instruments** for PS4/PS5 evaluation design — specifically TiA (Jian et al. 2000), HCTS (Gulati et al. 2019), and MDMT (Ullman & Malle 2018)
- Provides **theoretical grounding** for user trust as multidimensional and context-dependent, supporting graduated governance design
- Provides **empirical precedent** for evaluating user trust in AI systems via surveys, interviews, and experimental designs — establishes methodological norms PS5 should follow
- Provides **design recommendations** for communicating AI system state to users (explainability, transparency, accountability) — applicable to CAUTION mode communication design
- Establishes **methodological foundation** that has not yet been applied to AI governance architectures with intermediate states

### Gap statement

This paper establishes a comprehensive empirical evidence base for user trust in AI-enabled systems, confirming that trust is multidimensional and continuous, influenced by socio-ethical considerations, technical features, and user characteristics, and best measured using validated instruments. However, all 23 reviewed studies evaluate trust in AI systems that are either fully present or fully absent — no study evaluates user trust in an AI system operating under environmental-state-conditioned restriction, no study examines trust across governance mode transitions, and no study is conducted in a non-Western, low-resource, safety-critical environmental context. My research extends this evidence base by evaluating user trust across three governance modes (SAFE, CAUTION, UNSAFE) — including the novel CAUTION state where AI participates under restriction — in Malaysian coastal fishing communities, using validated instruments to enable cross-study comparability.

---

## 14. Overall Relevance Score

### ⭐⭐⭐⭐ High — Provides strong theoretical and methodological grounding for PS5

**Justification:** This paper provides exactly the kind of methodological foundation the extraction prompt is designed to identify:

1. **Trust definitions:** Catalogues and contextualises the two dominant trust definitions (Mayer et al. 2006; Lee & See 2004) with guidance on context-appropriate selection — directly usable for PS5 operationalisation
2. **Validated instruments:** Identifies TiA (Jian et al. 2000), HCTS (Gulati et al. 2019), and MDMT (Ullman & Malle 2018) as usable trust measurement instruments — directly informing PS5 instrument selection
3. **Trust factor taxonomy:** Provides a three-theme taxonomy (socio-ethical, technical/design, user characteristics) that structures PS5's evaluation dimensions
4. **Gap identification:** Explicitly confirms the absence of trust evaluation in intermediate AI modes, non-Western contexts, and safety-critical environmental settings — all gaps PS5 addresses
5. **Methodological norms:** Establishes that surveys are the dominant method, supplemented by qualitative methods — validating PS5's likely mixed-methods approach

**Why not ⭐⭐⭐⭐⭐:** The paper does not directly address graduated automation/governance levels, does not provide a framework for evaluating mode transitions, and does not include any study in a safety-critical environmental context. The canonical automation trust literature (Lee & See 2004 primary source; Parasuraman et al. 2000; Jian et al. 2000 primary source) would earn ⭐⭐⭐⭐⭐ because they directly define the constructs this paper reviews.

**Recommended citation uses:**
- **Primary citation** when justifying the choice of trust definition for PS5 (context-specific selection argument)
- **Primary citation** when justifying use of validated instruments over custom questionnaires
- **Primary citation** for the gap claim that no study evaluates user trust in intermediate AI governance modes
- **Supporting citation** for the gap claim that trust evaluation is geographically concentrated in Western contexts
- **Supporting citation** when framing PS5's three evaluation dimensions (socio-ethical, technical/design, user characteristics)

---

## Post-Extraction Commentary

### Strategic Assessment

This is a genuinely valuable methodological foundation paper — one of the strongest you'll find for grounding PS5's evaluation design. Its value is threefold:

1. **Instrument identification.** It gives you a curated, empirically grounded shortlist of validated trust instruments. For PS5, I'd recommend the **TiA scale (Jian et al. 2000)** as primary — it's the most established automation trust scale and directly applicable to comparing trust across governance modes. The **HCTS (Gulati et al. 2019)** is a strong alternative if you want a more general human-computer trust measure.

2. **Gap documentation.** With 195 citations and comprehensive coverage, this paper's confirmation that *no study evaluates trust in intermediate AI modes* is a powerful gap citation. Your PS5 novelty claim is strengthened by citing this SLR rather than claiming the gap based on your own search alone.

3. **Context-sensitivity argument.** The paper's finding that trust definitions and influencing factors are context-dependent supports your position that governance should also be context-dependent (i.e., state-conditioned) rather than universal.

### Score Rationale Relative to Prior Papers

At ⭐⭐⭐⭐, this is the **highest-rated paper in your extraction set to date** for the methodological extraction prompt. It is more directly useful than Nastoska et al. (2025) [⭐⭐] because it provides validated instruments and a structured trust factor taxonomy rather than a broad framework survey. It would sit alongside (but slightly below) the primary sources it reviews — Lee & See (2004), Jian et al. (2000), Mayer et al. (2006) — which would earn ⭐⭐⭐⭐⭐ as foundational definitions and instruments.

### Recommended Next Steps

1. **Obtain and extract Lee & See (2004)** — "Trust in Automation: Designing for Appropriate Reliance," *Human Factors* 46(1), 50–80. This is the canonical trust-in-automation paper and the most likely ⭐⭐⭐⭐⭐ methodological foundation for your work. Bach et al. identifies it as one of the two dominant trust definitions.

2. **Obtain and extract Jian et al. (2000)** — the TiA scale paper. If you plan to use this instrument in PS5, you need to cite the primary source and understand its psychometric properties.

3. **Consider Gulati et al. (2019)** — the HCTS paper. If the TiA scale is too automation-specific for your governance context, the HCTS may be more appropriate as a general human-computer trust measure.

4. **Consider Parasuraman et al. (2000)** — "A Model for Types and Levels of Human Interaction with Automation," *IEEE Transactions on Systems, Man, and Cybernetics*. This defines graduated automation levels and would provide the strongest theoretical grounding for why graduated governance is a valid design choice.
