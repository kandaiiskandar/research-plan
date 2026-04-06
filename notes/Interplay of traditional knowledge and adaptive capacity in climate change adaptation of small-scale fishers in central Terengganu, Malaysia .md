# Structured Extraction: Yamin et al. (2025)

## 1. Citation & Metadata

- **Authors:** Liyana Yamin, Ting-Chun Kuo, Nazli Aziz
- **Title:** Interplay of traditional knowledge and adaptive capacity in climate change adaptation of small-scale fishers in central Terengganu, Malaysia
- **Year:** 2025
- **Venue:** Frontiers in Marine Science, 12:1492131
- **DOI:** [10.3389/fmars.2025.1492131](https://doi.org/10.3389/fmars.2025.1492131)
- **Published:** 18 June 2025
- **Peer-reviewed:** Yes — Frontiers in Marine Science (Q1 marine science journal; open access, CC BY)
- **Type:** Original empirical research — questionnaire survey (n = 136) with SEM analysis
- **Ethics:** Approved by National Taiwan University Research Ethics Council (File: 202212ES028)

**Provenance assessment:** Strong. Q1 journal, DOI confirmed, primary empirical data, ethical approval documented. Suitable as a primary citation.

---

## 2. Research Problem (as relevant to this study)

The paper investigates perceived climate risks, traditional knowledge dependency, and adaptive capacity among 136 small-scale fishers in five coastal villages in central Terengganu, Malaysia. Its value to the dissertation is threefold: (a) it provides the most recent (2025) primary empirical data on the exact target population's environmental risk perceptions, directly validating the E vector parameters; (b) it documents fishers' declining ability to predict weather using traditional knowledge, providing domain-level motivation for AI decision support; and (c) it characterises adaptive capacity weaknesses (especially flexibility) and governance frustrations that frame PS5's socio-technical evaluation context.

---

## 3. Relevance Gate: Eight Core Research Themes

| # | Theme | Relevant? | Notes |
|---|---|---|---|
| 1 | Hybrid AI (rule-based + probabilistic) | ❌ | No AI content |
| 2 | Safety-critical AI decision-making | ❌ | No AI content |
| 3 | AI governance/control mechanisms | ❌ | No AI content |
| 4 | Low-resource environments | ✅ Strong | Half of fishers earn <RM 1,000/month; limited technology access; 0–5 nm zone restriction |
| 5 | Decision architecture formalisation | ❌ | — |
| 6 | Human role in decision-making | ✅ Strong | Traditional knowledge as decision-making framework; fishers integrate local knowledge with climate data; agency and learning as adaptive capacity domains |
| 7 | Socio-technical evaluation | ✅ Strong | Five-domain adaptive capacity assessment (assets, flexibility, social organisation, learning, agency); governance frustration documented; SEM model of TK → adaptive capacity |
| 8 | Coastal fisheries/maritime domain | ✅ Strong | Terengganu, Malaysia — exact geographic and demographic context |

**Gate result:** 4/8 themes (all strong). Passes on **full path** for domain-context relevance. No architectural content, but the strongest empirical domain paper yet extracted.

---

## 4. Empirical Grounding for Environmental State Vector E

This paper provides **primary, quantitative, fisher-reported** evidence for the E vector parameters — stronger than Shaffril et al.'s (2017) secondary synthesis and Muhamad et al.'s (2024) aggregate-level factors.

### 4.1 Perceived Climate Hazards (Section B results, Figure 2)

Fishers were asked to rate agreement on climate hazards experienced over the past 10 years:

| Climate hazard | % agree/strongly agree | E component mapping |
|---|---|---|
| Stronger monsoonal winds and larger waves | **95%** | **w (wind condition)** + **o (ocean condition: wave)** |
| Increased intensity of weather | **91%** | Cross-cutting — affects w, r, o simultaneously |
| Erratic rainfall patterns | **91%** | **r (rainfall intensity)** |
| Frequency of extreme weather | ~85% (from figure) | Cross-cutting — validates environmental state variability |
| Coastal erosion | ~80% (from figure) | **o (ocean condition)** — downstream consequence |
| Sea-level rise | ~75% (from figure) | **o (ocean condition: tide)** — long-term trend |
| Shoreline receding | ~70% (from figure) | **o (ocean condition)** — downstream consequence |
| Unpredictable monsoon | ~85% (from figure) | **m (marine warning level)** — monsoon unpredictability undermines fixed seasonal warning patterns, supporting the need for runtime state classification |

### 4.2 Mapping to E = {w, r, m, o, v, t}

| E component | Evidence from Yamin et al. (2025) | Strength |
|---|---|---|
| **w (wind condition)** | 95% of fishers identify stronger monsoonal winds as a primary hazard. Empirical knowledge item: "I know if it's suddenly windy/change of weather, I can't go fishing" — direct evidence that wind condition is a binary go/no-go trigger in current practice | ✅ **Very strong** — primary data, near-unanimous |
| **r (rainfall intensity)** | 91% report erratic rainfall patterns as a primary hazard. Terengganu's rainfall is heavily influenced by wind direction and temperature (citing Noor et al., 2023). Rainfall intensity classification has been studied specifically for East Coast Malaysia | ✅ **Strong** |
| **m (marine warning level)** | 85% report unpredictable monsoon. Fishers traditionally use monsoon seasonality as the primary temporal frame for fishing decisions (peak season March–October, especially July–September). Unpredictability of monsoon timing undermines fixed seasonal warnings, supporting runtime state classification over calendar-based rules | ✅ **Strong** — indirect but well-evidenced |
| **o (ocean condition: wave, tide, current)** | 95% identify larger waves as a primary hazard (paired with wind). Sea-level rise and coastal erosion reported. Fish migration patterns, spawning locations, and breeding ground degradation documented | ✅ **Very strong** |
| **v (vessel class)** | SSF in Malaysia limited to 0–5 nm zone with traditional vessels below 40 GRT. Fishers use hook-and-line (n = 113), gillnet (n = 30), bubu/trap (n = 24), purse seine (n = 23). 40.4% fish alone; 52.9% require 2–6 crew. Trip duration approximately 1 day (n = 82) | ✅ **Strong** — detailed vessel and gear characterisation |
| **t (trip state)** | Fishers go to sea 3–6 times per week unless weather is bad (n = 80). Trip duration approximately 1 day. Peak season March–October. Binary trip decision: "if it's suddenly windy/change of weather, I can't go fishing" — confirms trip initiation is a discrete state-dependent decision | ✅ **Strong** |

**Key finding:** The empirical knowledge item "I know if it's suddenly windy/change of weather, I can't go fishing" (agreed by majority of respondents, Figure 5) is direct primary evidence of the binary go/no-go decision pattern conditioned on environmental state — precisely the status quo that the CAUTION mode is designed to graduate.

---

## 5. Evidence for Binary Status Quo (Motivation for CAUTION Mode)

The paper provides the strongest primary evidence yet for the binary decision regime:

1. **"I can't go fishing"** — The empirical knowledge survey item explicitly frames the wind/weather decision as binary: can fish or can't fish. No intermediate option is documented (e.g., "I modify my fishing behaviour when weather is moderate").

2. **Flexibility is the weakest adaptive capacity domain** — Only 58% of fishers are willing to consider alternative livelihoods; 67.6% rely solely on fishing for household income. The adaptive capacity radar plot (Figure 9) shows flexibility as the clear deficit. This means fishers lack the *operational flexibility* to modify fishing behaviour under intermediate risk — they either go out as normal or don't go at all.

3. **No graduated fishing behaviour documented** — The questionnaire covers empirical knowledge (predicting weather, knowing spawning locations, using different gear for different months) but no item captures intermediate-risk behaviour modification. The closest is "I use different kind of methods of fishing for different month" — but this is seasonal gear switching, not risk-state-conditioned scope restriction.

4. **Traditional knowledge declining** — 60.3% still use traditional weather observation methods, but fishers report that their forecasting abilities are diminishing with intensifying climate change. They increasingly rely on apps (Windy, Windfinder). This creates a *decision support vacuum* at intermediate risk states: traditional knowledge can no longer reliably classify "safe enough to go but modify behaviour" conditions, and no AI system currently fills this gap.

**Architectural implication:** The binary go/no-go pattern is confirmed by primary data from 2023 fieldwork (published 2025). The flexibility deficit means the CAUTION mode doesn't just need to exist technically — it needs to *create* operational flexibility that fishers currently lack. This reframes CAUTION mode from "restricting what the AI recommends" to "enabling a graduated response that the population cannot currently execute without decision support."

---

## 6. Motivation for AI Decision Support in This Domain

The paper provides a domain-level justification for AI-assisted decision support that goes beyond the architecture itself:

| Finding | Implication for AI decision support |
|---|---|
| Traditional weather prediction declining in effectiveness due to climate unpredictability | Human-only decision-making is becoming less reliable → AI augmentation justified |
| Fishers increasingly relying on weather apps (Windy, Windfinder) | Technology adoption pathway already exists; fishers are not technology-averse, just resource-constrained |
| Flexibility is weakest adaptive capacity domain | Decision support that enables graduated responses could directly address the population's primary adaptive capacity deficit |
| Learning is strongest adaptive capacity domain (72% agree they need to be progressive) | Fishers are willing to learn and adopt new tools — PS5 adoption barrier may be lower than assumed |
| Fishers feel neglected by government agencies due to Zone A status | Any AI system must be perceived as *for* the fishers, not another top-down government tool — critical PS5 design requirement |
| 67.6% rely solely on fishing for household income | Consequences of poor decisions are existential, not marginal — safety-critical framing is empirically justified |

---

## 7. Socio-Technical Constraints for Architecture Design (Updated)

| Constraint | Evidence (Yamin et al., 2025) | Comparison to Shaffril et al. (2017) |
|---|---|---|
| **Income** | Half earn <RM 1,000/month (≈ USD 224.60); 5.1% earn ≤RM 500/month | Shaffril: >30% earn <RM 500/month. Income may have improved slightly but remains low |
| **Education** | 2.9% never schooled; 28.7% primary school only; 27.9% lower secondary (PT3); 34.6% upper secondary (SPM); 5.9% tertiary | Shaffril: MCE or lower. Yamin provides finer granularity — ~60% have lower secondary or below |
| **Age** | 44.9% aged 46–60; 32.4% aged 61+; 5.9% aged 15–30 | Shaffril: generally >40. Yamin confirms ageing population with minimal youth entry |
| **Vessel/zone** | 0–5 nm zone; traditional vessels below 40 GRT; hook-and-line dominant gear | Shaffril: ≤22 feet, <5 nm. Consistent characterisation |
| **Technology use** | Mobile apps (Windy, Windfinder) for weather; information sharing via social media | Shaffril: heavy mobile phone users. Yamin adds specific app usage — establishes that mobile-based AI decision support is realistic |
| **Religion** | 100% Muslim; 93.4% believe climate change related to Qadr (divine decree); spiritual practice is strongest TK component | Not addressed in Shaffril. Critical for PS5: any AI system must be culturally compatible with religious worldview; framing AI as a tool within divine order rather than replacing human/divine agency |
| **Governance frustration** | Fishers feel neglected by PNK and government; complaints not taken seriously; Zone A fishers deprioritised vs. Zone B/C | Not documented in Shaffril at this level. Critical PS5 insight: system must be positioned as fisher-empowering, not government-imposed |
| **Gender** | 100% male respondents | Consistent with SSF literature; PS5 sample will likely be all-male |

---

## 8. Governance Trigger Rationale: Why Environmental State

This paper strengthens the domain-side argument for environmental state as the governance trigger, with two new dimensions beyond Shaffril et al. (2017):

1. **Fisher-reported hazard hierarchy matches E vector.** The three primary hazards identified by fishers themselves — stronger winds/larger waves (95%), more intense weather (91%), erratic rainfall (91%) — map directly onto w, r, and o. This is not researcher-imposed categorisation; it is the population's own risk perception structure. Conditioning governance on these parameters means the AI's decision logic reflects how the users *actually think about risk*.

2. **Traditional knowledge erosion creates a decision support vacuum.** Fishers report that their traditional forecasting abilities are declining. They are turning to weather apps but these provide raw data without governance logic (Windy shows wind speed but doesn't advise "restrict to nearshore fishing"). An AI system conditioned on environmental state fills this specific gap: it translates the environmental parameters fishers already monitor into actionable, scope-restricted recommendations.

3. **Spiritual worldview compatibility.** 93.4% attribute climate change to Qadr (divine decree). An AI system conditioned on observable environmental conditions — wind, waves, rain — is more compatible with this worldview than one conditioned on model confidence or algorithmic uncertainty. Environmental conditions are part of the created order; AI confidence scores are abstract computational artefacts. This is a subtle but important cultural alignment for PS5 acceptance.

4. **Direct observability and experiential verification** (reinforcing Shaffril). 60.3% still use traditional observation methods (cloud locations, wind strength, waves). The dynamic E parameters (w, r, o) are what fishers *already observe*. The AI system classifies the same observable reality, enabling experiential verification of the safety state.

---

## 9. Mapping onto Architecture Components

| Component | Mapping | Strength |
|---|---|---|
| **E = {w, r, m, o, v, t}** | All six parameters evidenced by primary data: wind (95%), rainfall (91%), monsoon unpredictability, wave/ocean conditions (95%), vessel class (<40 GRT, 0–5 nm), trip patterns (3–6x/week, ~1 day) | ✅ **Very strong** — primary quantitative data from target population |
| **S = f(E)** | Current practice implements informal binary classification: "if it's suddenly windy/change of weather, I can't go fishing." Traditional weather prediction declining, creating demand for systematic state classification | ✅ Strongly supports motivation |
| **G(S)** | Binary participation gate confirmed: fishers either go out or don't. No intermediate operational mode documented | ✅ Confirms binary status quo |
| **A_AI(S)** | ❌ Not present — no AI advisory system discussed | Confirms gap |
| **CAUTION mode** | ❌ No intermediate graduated response in current practice. Flexibility is weakest adaptive capacity domain (Figure 9), meaning fishers lack the *capacity* for graduated responses without decision support | ✅ **Strongest motivation yet** — CAUTION mode addresses a measured adaptive capacity deficit |
| **Safety Dominance Property** | ❌ Not applicable | — |

---

## 10. Relevance to PS4 and PS5

| Study | Relevance |
|---|---|
| **PS4 (graduated vs. binary governance)** | The binary go/no-go decision pattern is confirmed by primary data ("I can't go fishing"). Flexibility as the weakest adaptive capacity domain provides the *outcome variable motivation*: PS4 should test whether graduated governance improves fishers' operational flexibility under intermediate risk, not just architectural compliance. |
| **PS5 (socio-technical evaluation)** | **Directly relevant across multiple dimensions:** (a) The five-domain adaptive capacity framework (assets, flexibility, social organisation, learning, agency) as operationalised here provides a validated evaluation structure that PS5 could adopt or parallel; (b) Governance frustration (fishers feel neglected by PNK/government) defines the positioning requirement: the system must be perceived as fisher-empowering; (c) Religious worldview (93.4% Qadr attribution) requires cultural sensitivity in how AI recommendations are framed; (d) Learning as strongest domain (72%) suggests adoption willingness is present if the system aligns with their mental models; (e) The questionnaire instrument (Cronbach's α = 0.914) provides a methodological precedent for PS5 instrument design in this population. |

---

## 11. Relevance Score

### ⭐⭐⭐⭐ (Four Stars) — Primary Domain-Context Reference with Strong E Vector and PS5 Grounding

**Justification:** This is the strongest domain-context paper extracted to date. It provides primary empirical data (n = 136) from the exact target population (Terengganu small-scale fishers, 0–5 nm zone), published in a Q1 journal in 2025. It delivers: (a) near-unanimous fisher-reported evidence that the E vector parameters are the primary perceived climate hazards; (b) the strongest primary evidence for the binary go/no-go decision pattern; (c) the finding that flexibility is the weakest adaptive capacity domain, directly motivating CAUTION mode as a capacity-building mechanism; (d) evidence of traditional knowledge erosion creating a decision support vacuum; and (e) rich socio-technical context (religious worldview, governance frustration, technology adoption patterns) essential for PS5 design. The four-star rating (not five) reflects the absence of any AI, governance, or architectural content — it remains a domain paper, not an architecture paper.

---

## 12. Positioning Paragraph

Yamin et al. (2025) provide the most recent and empirically robust characterisation of the target population for the proposed architecture. Surveying 136 small-scale fishers in central Terengganu, the study confirms that the primary perceived climate hazards — stronger monsoonal winds and larger waves (95%), more intense weather (91%), and erratic rainfall (91%) — map directly onto the dynamic components of the environmental state vector E = {w, r, m, o, v, t}. Critically, the finding that fishers' traditional weather prediction abilities are declining due to climate unpredictability, coupled with their increasing reliance on weather apps, establishes a domain-level decision support vacuum that the proposed architecture is designed to fill. The study's five-domain adaptive capacity assessment reveals flexibility as the weakest domain, providing an empirical motivation for the CAUTION mode that extends beyond architectural formalism: graduated governance addresses a measured adaptive capacity deficit in the target population. The binary decision pattern is confirmed by the empirical knowledge item "if it's suddenly windy/change of weather, I can't go fishing" — a fisher-reported binary go/no-go trigger with no documented intermediate response. For PS5, the study's documentation of governance frustration (fishers feeling neglected by PNK and government agencies), religious worldview (93.4% attributing climate change to divine decree), and learning willingness (72% agreeing they need to be progressive) defines the socio-technical evaluation context within which the CAUTION mode must demonstrate acceptance, trust, and cultural compatibility.

---

## 13. Citation Placement Recommendations

| Section | Use | Priority |
|---|---|---|
| **Environmental state vector justification (primary)** | Fisher-reported hazard data mapping directly onto E parameters — this is the strongest empirical evidence that the E vector reflects the population's own risk perception structure | **High** |
| **Binary governance gap argument** | "I can't go fishing" as primary evidence of binary go/no-go; flexibility as weakest adaptive capacity domain | **High** |
| **Motivation for CAUTION mode** | Flexibility deficit + TK erosion = decision support vacuum at intermediate risk states; CAUTION mode as capacity-building mechanism | **High** |
| **Governance trigger rationale** | Fisher-reported hazard hierarchy aligns with E vector; spiritual worldview compatibility; direct observability | **High** |
| **Motivation for AI decision support (Chapter 1)** | TK declining; fishers already adopting weather apps; 67.6% sole-income dependence = safety-critical framing justified | **High** |
| **PS5 design rationale** | Five-domain adaptive capacity framework; governance frustration; religious worldview; learning willingness; questionnaire instrument precedent (α = 0.914) | **High** |
| **PS4 design rationale** | Binary status quo baseline; flexibility as outcome variable for graduated governance evaluation | **Medium** |
| **Domain characterisation (Chapter 1 / Section 2.1)** | Updated demographics, fishing practices, gear types, income levels, geographic context | **Medium** — supplements Shaffril et al. with 2023 fieldwork data |

---

## 14. Inter-Paper Relationships

| Paper | Relationship |
|---|---|
| **Shaffril et al. (2017)** | Yamin et al. (2025) **supersedes** Shaffril as the primary domain characterisation source: same domain, same region, but 8 years more recent with primary empirical data. Shaffril remains useful for parameter-level climate evidence (wind speed stations, rainfall percentiles, sea-level rise data) not covered in Yamin's perception-based approach. Recommended pairing: Shaffril for objective climate data, Yamin for fisher-perceived hazards and adaptive capacity |
| **Muhamad et al. (2024)** | Yamin et al. (2025) largely **displaces** Muhamad's recency function. Both are post-2020 Malaysian SSF papers, but Yamin is in a Q1 journal with primary empirical data vs. Muhamad's aggregate factor validation in a weaker venue. Muhamad retains marginal value only if the fuzzy logic domain precedent is needed |
| **McGrath et al. (2025) S-TIAS** | The trust instrument for PS4/PS5. Yamin's finding that learning is strongest and flexibility weakest suggests PS5 should measure trust in the CAUTION mode's ability to *create* flexibility, not just provide information |

---

## 15. Methodological Notes for PS4/PS5

- **Sample size:** n = 136 from ~800 fishers (17% coverage). Snowball sampling. Authors cite Lakens (2022) justifying 50–200 for exploratory social science. PS4/PS5 should aim for comparable or larger n.
- **Instrument reliability:** Cronbach's α = 0.914 (predefined threshold 0.7). This establishes a benchmark for PS5 instrument reliability in this population.
- **Language:** Conducted in Malay Terengganu dialect. PS5 must also be conducted in dialect, not standard Malay — a practical consideration for questionnaire design.
- **Enumerator-administered:** Six enumerators administered questionnaires to fishers. This is likely necessary for PS5 given the education profile (60% lower secondary or below).
- **SEM analysis:** lavaan package in R. PS5 could use comparable analytical approach if testing structural relationships.
