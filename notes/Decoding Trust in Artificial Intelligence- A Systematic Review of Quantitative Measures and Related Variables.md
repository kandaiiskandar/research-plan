# Methodological Foundation Paper Extraction

## Paper: Aquilino et al. (2025) — Decoding Trust in AI: Systematic Review of Quantitative Measures

---

## 1. Paper Identity

- **Full title**: Decoding Trust in Artificial Intelligence: A Systematic Review of Quantitative Measures and Related Variables
- **Authors**: Letizia Aquilino, Cinzia Di Dio, Federico Manzi, Davide Massaro, Piercosma Bisconti, Antonella Marchetti
- **Year**: 2025
- **Publication venue**: *Informatics*, 12(3), 70
- **DOI**: 10.3390/informatics12030070
- **Type of paper**: Systematic literature review (PRISMA-guided; 45 papers from 1,283 screened)
- **Open access**: Yes (CC BY)
- **Received / Revised / Accepted / Published**: 29 May 2025 / 3 Jul 2025 / 7 Jul 2025 / 14 Jul 2025

---

## 2. Core Contribution

- **Problem addressed**: Trust in AI is measured using highly heterogeneous definitions, instruments, and conceptual frameworks across the literature. This variability undermines replicability and cross-study comparability. The field lacks a systematic mapping of how trust is defined, operationalised, and measured in relation to different types of AI systems.
- **Proposed solution / key finding**: The review applies a **cognitive–affective trust** lens to systematise 45 empirical studies. Key findings:
  1. **Diverse conceptualisations**: Trust definitions range from interpersonal trust frameworks (Mayer et al., 1995 — ability, benevolence, integrity) to technology-specific frameworks (McKnight et al., 2011 — functionality, reliability, helpfulness) to automation-specific frameworks (Lee & See, 2004 — performance, process, purpose).
  2. **Cognitive dominance**: Almost every study measures at least one cognitive trust attribute (competence, reliability, functionality). Affective trust attributes (benevolence, care, emotional bonding) appear in only 24 of 45 studies.
  3. **Anthropomorphism–trust type alignment**: The level of anthropomorphism of the AI system predicts which trust component dominates. Highly anthropomorphic systems (virtual assistants, social robots) tend to elicit affective trust; low-anthropomorphism systems (classification tools, decision aids) tend to elicit primarily cognitive trust.
  4. **Measurement–definition discrepancies**: Four studies define trust with affective components but measure it with only cognitive attributes — revealing a gap between conceptualisation and operationalisation.
- **What makes it foundational**: Provides the most comprehensive recent mapping of trust measurement instruments and trust-related constructs across AI system types, organised through the cognitive–affective lens. Establishes that trust measurement should be tailored to both the type of AI system and the deployment context.

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | No | Review does not distinguish AI architecture types |
| Safety-critical AI decision-making | Partial | Some included studies address medical AI (studies 18, 21, 22, 24) and self-driving cars; review notes that high-risk applications likely invoke cognitive trust more than affective trust |
| AI governance / control mechanisms | No | No studies address governance architectures or gating mechanisms |
| Low-resource environments | No | No studies conducted in low-resource contexts; review notes geographic distribution (11 Europe, 18 East Asia, 6 South Asia, 10 America) but does not address resource constraints |
| Decision architecture formalisation | No | No formal architectural notation |
| Human role in decision-making | Yes | Central focus: how humans form, calibrate, and express trust in AI systems |
| Socio-technical evaluation | Yes | Provides comprehensive mapping of trust measurement approaches, experimental stimuli types, and trust-related constructs |
| Coastal fisheries / maritime domain | No | No domain overlap |

---

## 4. Graduated Automation / Governance Framework

### Does the paper define levels, stages, or grades of automation, autonomy, or system control?

**No.** The review does not address automation levels or graduated autonomy. It categorises AI systems by **anthropomorphism level** (high / medium / low / undefined), not by governance or autonomy level.

### Does it distinguish between "system participates at all" (Level 1) and "what the system is allowed to do" (Level 2)?

**No.** There is no governance framework. The review assumes the AI system is always active; the question is how users perceive and trust it.

### Does it include an intermediate mode analogous to CAUTION?

**No.** No concept of restricted, intermediate, or graduated AI operation appears in the review or in any of the 45 included studies.

### Mapping to my three-mode governance model

| Paper's concept | My architecture's equivalent | Alignment |
|---|---|---|
| Cognitive trust (rational, competence-based) | Primary trust type expected in CAUTION and UNSAFE states — users evaluating whether the system's governance decisions are correct | Partial — cognitive trust maps to rational evaluation of governance appropriateness |
| Affective trust (emotional, relational) | More relevant in SAFE state where sustained AI interaction builds familiarity; less relevant in CAUTION/UNSAFE where governance restriction disrupts relational continuity | Partial — the cognitive/affective distinction helps predict which trust component dominates in each governance state |
| Anthropomorphism level predicting trust type | DSR system is a low-anthropomorphism decision support tool → predicts cognitive trust will dominate | Strong — supports choosing cognitive-trust-focused instruments for PS4/PS5 |
| High-risk contexts invoke cognitive trust | Safety-critical fishing decisions → cognitive trust should dominate over affective trust | Strong alignment with instrument selection rationale |

### Does the paper argue graduated control is superior to binary?

**No.** The review does not address system control modes at all.

### Does it identify risks of binary automation control?

**No.** However, the review's finding that trust measurement should match system characteristics provides indirect support for the argument that governance modes should produce distinct, measurable trust profiles — which binary governance cannot achieve.

---

## 5. Trust, Reliance, and User Response

### Does the paper address human trust in automated/AI systems?

**Yes — this is the paper's entire scope.** It systematically reviews 45 studies measuring trust in AI.

### Does it define or operationalise trust in a measurable way?

**Yes.** The review catalogues multiple trust definitions and maps them to the cognitive–affective framework:

#### Trust definitions identified (with frequency)

| Definition / Framework | Studies using it | Trust type |
|---|---|---|
| **Mayer et al. (1995)** — Willingness to be vulnerable; antecedents: ability, benevolence, integrity | 13 studies | Primarily cognitive (ability); partially affective (benevolence, integrity) |
| **McKnight et al. (2011)** — Functionality, reliability, helpfulness (technology-specific) | 3 studies | Cognitive |
| **Lee & See (2004)** — Performance, process, purpose (automation-specific) | 2 studies | Cognitive |
| **Madsen & Gregor (2000)** — Degree of confidence in AI + willingness to act | 2 studies | Cognitive |
| Various vulnerability-centred definitions | 3 studies | Mixed |
| No clear definition stated | 13 studies | — |

#### Cognitive vs affective trust attributes measured across 45 studies

**Cognitive attributes** (measured in 43 of 45 studies): competence, reliability, functionality, dependability, safety, accuracy, predictability, intelligence, effectiveness, credibility, helpfulness, transparency

**Affective attributes** (measured in 24 of 45 studies): benevolence, honesty, integrity, care, truthfulness, well-intendedness, fairness, familiarity

### Validated measurement instruments catalogued

The review does not validate instruments itself but catalogues what the 45 studies used. Key instruments referenced across studies:

- **Jian et al. (2000) TIAS** — Referenced in the review's discussion of trust-in-automation measurement (reference [127] in the paper)
- **Mayer et al. (1995) ABI framework** — Ability, Benevolence, Integrity subscales adapted by 13 studies
- **McKnight et al. (2002/2011)** — Technology trust subscales (functionality, reliability, helpfulness)
- **Madsen & Gregor (2000)** — Human-computer trust scale
- **Lee & See (2004)** — Trust in automation framework (performance, process, purpose)
- Various custom and ad hoc multi-item scales developed per study

### Trust failure types

| Trust failure type | Addressed? | Detail |
|---|---|---|
| Overtrust / complacency | Partial | Referenced indirectly through discussion of users trusting AI systems beyond their capabilities; study 28 (De Brito Duarte et al.) found explanations can lead to overreliance when performance is not guaranteed |
| Undertrust / disuse | Partial | Referenced through studies finding lower initial trust in automated systems vs humans (study 33, Langer et al.) and lower trust in AI vs human doctors (study 18, Yokoi et al.) |
| Misuse | Not directly addressed | |

### Application to three governance modes

| Mode | Trust implication from review | Instrument recommendation |
|---|---|---|
| SAFE | Sustained interaction with fully enabled AI → both cognitive and affective trust may develop; risk of overtrust if system performs well consistently | Include both cognitive and affective trust items; the review suggests affective trust builds over repeated interactions |
| CAUTION | Restricted AI is a low-anthropomorphism, functional-tool interaction → review predicts cognitive trust will dominate; the restriction disrupts any affective bond | Prioritise cognitive trust measurement (competence, reliability); affective items may not be sensitive to this mode |
| UNSAFE | No AI interaction → trust question shifts to user trust in the *governance decision* itself, not in the AI | May need a distinct "trust in governance" measure rather than standard trust-in-AI instruments |

---

## 6. Mode Awareness and Automation Surprises

### Does the paper address mode confusion?

**No.** The term "mode confusion" does not appear. The review does not address scenarios where users misunderstand which operational state the system is in.

### Does it address automation surprises?

**No.** No discussion of unexpected system behaviour or state transitions.

### Implications for CAUTION mode design

Two findings from the review are indirectly relevant:

1. **Anthropomorphism–trust alignment**: The review establishes that a system's perceived characteristics determine which trust components are activated. When the DSR system transitions from SAFE (full advisory) to CAUTION (restricted advisory), its functional profile changes — users may perceive this as a shift from a more capable "partner" to a more limited "tool." The review's framework predicts this should shift trust from mixed cognitive–affective to primarily cognitive. PS5 should measure whether this shift occurs.

2. **Definition–measurement discrepancy risk**: The review identifies four studies where trust was defined with affective components but measured with only cognitive attributes — missing important trust dynamics. For PS5, this warns against using a purely cognitive trust instrument (like S-TIAS alone) if affective trust might also be relevant in SAFE mode. A complementary affective measure may be needed for the SAFE condition.

---

## 7. Evaluation Methodology

### Does the paper describe an evaluation method?

The review catalogues **four types of experimental stimuli** used across the 45 included studies:

| Stimulus type | Description | Studies using | Trust type favoured |
|---|---|---|---|
| **Representation of past experience** | Participants recall prior use of a specific AI system | 14 studies | Both cognitive and affective (sustained interaction allows affective trust to develop) |
| **Direct experience: task** | Participants complete a task using an AI system in the experiment | 13 studies | Primarily cognitive (limited interaction time) |
| **Direct experience: scenario (vignette)** | Participants read a scenario and imagine being the protagonist | 9 studies | Primarily cognitive (no sustained interaction) |
| **General representation** | Participants respond based on general impressions of AI (no specific system) | 9 studies | Cognitive (no specific target to form affective bond with) |

### Experimental design considerations for PS4/PS5

The review's analysis suggests:
- **Vignette-based designs** (which PS4/PS5 will likely use for fishing trip scenarios) naturally emphasise cognitive trust over affective trust
- **Task-based designs** where participants interact with a prototype would provide richer trust data but require a functional system
- **Recall-based designs** would only work for users who have already experienced the DSR system (post-deployment evaluation)

### Does it evaluate transitions between automation levels?

**No.** None of the 45 studies evaluated trust during system state transitions.

### Safety-critical contexts included?

**Partial.** Medical AI appears in 4 studies (studies 18, 21, 22, 24); self-driving cars appear in several studies. The review notes that high-risk applications likely invoke cognitive trust more strongly than affective trust.

---

## 8. Applicability to PS4 (Comparative Evaluation: Graduated vs Binary Governance)

### Theoretical justification for comparing graduated vs binary control?

**Indirect.** The review's central argument — that trust measurement must be tailored to system characteristics and context — provides meta-methodological support for PS4. If graduated governance produces three distinct system profiles (fully enabled, restricted, disabled), PS4 must use trust instruments sensitive to each profile. The review's cognitive–affective framework helps predict which trust components to measure in each condition.

### Specific metrics for measuring the value of an intermediate mode?

**Not directly.** However, the review's categorisation of trust attributes provides a checklist for PS4 instrument design:
- **Cognitive attributes to measure**: competence, reliability, dependability, safety (dominant in all governance states)
- **Affective attributes to consider**: benevolence, care, honesty (may only be relevant in SAFE state with sustained interaction)

### What does "better" mean?

The review does not define "better" in governance terms. However, it frames trust measurement quality as: (a) alignment between trust definition and measurement, (b) alignment between system characteristics and trust type measured, and (c) sensitivity to the specific trust-related constructs activated by the system. Applying this to PS4: "better governance" could be operationalised as governance that produces trust scores more appropriately calibrated to each system state.

### What to cite from this paper for PS4

- Justification for prioritising cognitive trust measurement for a low-anthropomorphism decision support tool
- Evidence that safety-critical contexts invoke cognitive trust → supports choosing cognitive-trust instruments (S-TIAS) over affective-trust instruments
- The taxonomy of experimental stimuli types — cite when justifying vignette-based design choice and acknowledging its limitation (favours cognitive over affective trust measurement)

---

## 9. Applicability to PS5 (Socio-Technical Evaluation of CAUTION Mode)

### Validated instruments for measuring trust across governance modes?

**Indirectly.** The review does not validate instruments itself but provides a comprehensive catalogue of instruments used across 45 studies, enabling informed selection. The cognitive–affective framework helps PS5 select instruments that match the expected trust dynamics of each governance state.

### Precedent for evaluating user understanding of intermediate automation states?

**No.** None of the 45 reviewed studies evaluated intermediate automation or governance states. This confirms that PS5 is entering unmapped territory.

### How to measure trust calibration?

**Not directly addressed.** However, the review's identification of cognitive vs affective trust provides a framework: appropriate trust calibration in the DSR system means cognitive trust is high in SAFE, intermediate in CAUTION, and potentially low/redirected in UNSAFE. Affective trust should not vary much across governance states for a low-anthropomorphism system — if it does, this signals users are anthropomorphising the governance mechanism itself (an interesting finding).

### How do users interpret system restriction?

**Not addressed.** However, the review's finding that transparency and explanations sometimes reduce trust (citing studies where information about AI limitations decreased trust) is relevant. When CAUTION mode communicates that the AI is "operating under restriction," this is effectively a transparency disclosure about reduced capability — which the review suggests may reduce trust beyond what is appropriate.

### What to cite from this paper for PS5

- Framework for selecting cognitive vs affective trust measurement based on system anthropomorphism level → justifies cognitive-focused instrument selection for DSR
- Catalogue of trust definitions → cite when establishing which trust definition the research adopts
- Evidence that transparency about system limitations can paradoxically reduce trust → cite when discussing risk that CAUTION mode disclosure may cause excessive undertrust
- Cultural variation acknowledgement → cite when discussing PS5's Malaysian coastal community context as a deployment context not represented in the existing literature

---

## 10. Key Concepts and Definitions

| Term / Framework | Definition | Location | Mapping to my research |
|---|---|---|---|
| **Cognitive trust** | Rational, evidence-based trust grounded in evaluation of the trustee's reliability, competence, and predictability | Section 1, ¶3–4 | Primary trust component expected across all three governance states for a decision support system |
| **Affective trust** | Trust shaped by emotional connections, personal experiences, and perceived genuine care; extends beyond what is justified by concrete knowledge | Section 1, ¶5–6 | Secondary trust component; may be relevant in SAFE mode with sustained use; PS5 should measure but not expect large effects |
| **Mayer et al. (1995) ABI model** | Three antecedents of trustworthiness: Ability (skills/competence), Benevolence (positive intentions), Integrity (consistency/honesty) | Section 3.1.1 | Most-cited trust framework in AI literature; Ability maps to cognitive trust, Benevolence/Integrity bridge cognitive and affective |
| **McKnight et al. (2011) technology trust** | Three dimensions: Functionality (capability), Reliability (consistency), Helpfulness (utility) | Section 3.1.1 | Technology-specific trust framework; all three dimensions are cognitive; good fit for low-anthropomorphism decision support |
| **Lee & See (2004) trust in automation** | Three bases: Performance (operational characteristics), Process (suitability for user goals), Purpose (designer intent) | Section 3.1.1 | Automation-specific framework; Performance maps to system reliability, Purpose maps to governance design intent |
| **Anthropomorphism–trust type alignment** | Higher anthropomorphism → more affective trust; lower anthropomorphism → more cognitive trust | Section 3.2 / Discussion | DSR is low-anthropomorphism → expect cognitive trust dominance; guides instrument selection |
| **Trust measurement–system alignment principle** | Trust definitions and measurement should match the level of anthropomorphism and the context of application | Section 5 (Conclusions) | Meta-methodological principle for PS4/PS5 instrument selection |

---

## 11. Quotable / Citable Points

1. **Cognitive trust dominance in functional systems** (Section 3.2 / Discussion): The review establishes that low-anthropomorphism AI systems (classification tools, decision aids) predominantly invoke cognitive trust, while highly anthropomorphic systems (virtual assistants, social robots) additionally invoke affective trust. *→ Cite when justifying cognitive-trust-focused instrument selection for the DSR system.*

2. **Trust definition variability undermines comparability** (Section 3.1.1): The 45 reviewed studies employ at least six distinct trust definitions, with 13 studies providing no clear definition at all. *→ Cite when justifying explicit adoption of a specific trust definition (e.g., Lee & See, 2004) for PS4/PS5.*

3. **Definition–measurement discrepancy** (Section 3.1.1, "From Definition to Measurement"): Four studies define trust with affective components but measure it using only cognitive attributes, potentially missing important trust dynamics. *→ Cite when justifying inclusion of both cognitive and affective trust items in PS5 even though cognitive trust is expected to dominate.*

4. **Safety-critical contexts invoke cognitive trust** (Discussion, Section 4.3): The review argues that in high-risk applications where user self-preservation is involved, the cognitive component of trust is expected to dominate, as the choice to rely on the system must be marked by rational certainty. *→ Cite when positioning the coastal fisheries safety-critical context as one that requires cognitive-trust-focused evaluation.*

5. **Cultural variation in trust** (Discussion, Section 4.5): The review notes that studies were conducted across diverse geographic regions and acknowledges that cultural dimensions (individualism/collectivism, uncertainty avoidance) may significantly influence trust formation and measurement, but this has not been systematically investigated. *→ Cite when positioning PS5's Malaysian context as addressing a gap in cross-cultural trust evaluation.*

---

## 12. Limitations and Gaps

### Stated limitations

- **Quantitative-only scope**: Excluded qualitative and mixed-methods studies, potentially missing nuanced trust formation insights
- **Journal-only inclusion**: Excluded conference proceedings, which in technical fields may contain innovative findings
- **Pre-December 2023 coverage**: Search period cuts off before the recent wave of generative AI trust research (2024–2025)
- **No meta-analysis**: Descriptive synthesis only; no statistical aggregation of effect sizes

### Gaps my research could address

| Gap | How my research addresses it |
|---|---|
| No study evaluates trust across **multiple AI operational states** within a single system | PS5 measures trust across SAFE/CAUTION/UNSAFE governance states for a single DSR system |
| No study evaluates trust in an **intermediate/restricted AI mode** | PS5 specifically evaluates CAUTION mode where AI is active but scope-restricted |
| No study evaluates trust in **environmental-state-conditioned governance** | My architecture conditions AI participation on classified environmental safety state S = f(E) |
| No study evaluates trust in **low-resource, non-Western contexts** | PS5 targets Malaysian coastal fishing communities |
| No study aligns trust measurement with **governance architecture** (as opposed to system type or anthropomorphism) | My research selects trust instruments based on governance state characteristics, not just system characteristics |
| **Definition–measurement alignment** is identified as a problem but not resolved | My research explicitly adopts a defined trust framework and selects instruments that match it, using the cognitive–affective lens from this review as the selection criterion |
| No study measures trust during **system state transitions** | PS5 measures S-TIAS across SAFE → CAUTION → UNSAFE transitions |

### What this paper does NOT cover that my research needs

- Specific instrument recommendations — the review catalogues but does not recommend. My research uses McGrath et al. (2025) for the specific instrument (S-TIAS) and this review for the meta-level justification of instrument selection criteria
- Trust calibration operationalisation — the review identifies cognitive and affective trust but does not define what "appropriately calibrated" trust looks like for a given system state
- Mode awareness / comprehension measurement — no instrument or approach for measuring whether users *understand* what a governance state means, only whether they *trust* the system in that state
- Governance-specific trust — the review treats trust as directed at the AI system; my research needs to distinguish trust in the AI system from trust in the governance mechanism that controls the AI system

---

## 13. Positioning in My Literature Review

### Role in the argumentative chain

- **Link 9 (supporting)**: Confirms that no existing empirical study evaluates trust in an intermediate AI governance mode — all 45 reviewed studies assume the AI system is in a single, fixed operational state
- **Methodological grounding**: Provides the meta-level framework (cognitive–affective trust) for selecting and justifying trust instruments in PS4/PS5

### Role in the literature review

- ✅ Provides **theoretical grounding** for trust measurement selection based on system characteristics and deployment context
- ✅ Establishes **methodological foundation** (cognitive–affective trust taxonomy) that has not yet been applied to AI governance architectures
- ✅ Provides **catalogue of instruments** and trust-related constructs from which PS4/PS5 instrument battery can be assembled
- ❌ Does NOT provide a specific validated instrument (that role is filled by McGrath et al., 2025)
- ❌ Does NOT provide empirical precedent for evaluating intermediate governance modes
- ❌ Does NOT provide design recommendations for communicating governance state to users

### Gap statement

This paper establishes that trust measurement in AI must be tailored to the characteristics of the specific system and context, distinguishing between cognitive trust (dominant for functional, low-anthropomorphism decision support tools) and affective trust (more relevant for highly anthropomorphic, social AI systems). However, the review's 45 included studies all assume a single, fixed AI operational state — no study evaluates trust across multiple governance modes within a single system, and no study addresses the novel case where an AI system operates in a restricted intermediate mode. My research extends this by deploying cognitive-trust-focused instruments across a three-state graduated governance architecture (SAFE/CAUTION/UNSAFE), testing whether the cognitive–affective framework correctly predicts trust dynamics in each state, and evaluating trust in a safety-critical, low-resource deployment context (Malaysian coastal fisheries) not represented in the existing literature.

---

## 14. Overall Relevance Score

### ⭐⭐⭐ Medium

**Justification**: This paper provides valuable meta-level guidance for trust instrument selection and a useful organising framework (cognitive vs affective trust) for predicting trust dynamics across governance states. However, it is a secondary source that reviews and catalogues existing work rather than providing a validated instrument or novel empirical findings directly applicable to PS4/PS5. Its contribution to my research is primarily at the instrument selection justification level — explaining *why* a cognitive-trust-focused instrument (S-TIAS) is appropriate for a low-anthropomorphism, safety-critical decision support system. It falls short of ⭐⭐⭐⭐ because the actual instrument comes from McGrath et al. (2025), not from this review.

**Role cluster**: Trust measurement landscape / instrument selection rationale

**Recommended citation uses**:
1. Meta-level justification for choosing cognitive-trust instruments for a low-anthropomorphism DSR system
2. Evidence that no existing study evaluates trust across multiple AI operational states (gap confirmation for PS5)
3. Acknowledgement that safety-critical contexts invoke cognitive trust → supports instrument selection
4. Cultural variation gap → positions PS5's Malaysian context as addressing an under-researched area
5. Taxonomy of experimental stimuli types → justifies vignette/scenario design and acknowledges its cognitive trust bias

**Pairing**: Cite alongside McGrath et al. (2025) — this review provides the *why* (cognitive trust instruments suit low-anthropomorphism, safety-critical decision support), McGrath et al. provides the *what* (S-TIAS as the specific validated instrument).
