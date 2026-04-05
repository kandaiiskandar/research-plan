# Literature Review Extraction: Rahim et al. (2024)

---

## 1. Paper Identity

- **Title:** Survival Decisions and Adaptation Strategies of Small-scale Fishers in the Face of Extreme Weather Impacts in Coastal Areas
- **Authors:** Abd. Rahim, Diah Retno Dwi Hastuti, Ahmadin, Dewi Agustin Pratama Sari, Muhammad Roestam Afandi
- **Year:** 2024
- **Venue:** *Journal of Marine and Island Cultures*, v13n3
- **DOI:** 10.21463/jmic.2024.13.3.05
- **Type:** Empirical study (quantitative survey with logistic regression + SWOT analysis)

---

## 2. Core Contribution

- **Problem addressed:** Small-scale fishers in coastal regions face life-threatening decisions about whether to fish during extreme weather events driven by climate change. Limited alternative employment forces fishers to continue fishing despite safety risks, yet the determinants of these survival decisions and the adaptation strategies fishers employ are poorly understood.
- **Proposed solution / key finding:** Uses a logistic regression model (MLE) on 79 small-scale fishing households in coastal Makassar City, Indonesia, to identify factors influencing survival decisions under extreme weather. Key findings: fishing revenue (Exp(βi) = 1.004), fishing experience (1.081), and government-provided eco-friendly fishing gear assistance programs (6.583) significantly increase the probability of fishermen persisting. Formal education, family size, and direct cash transfers (BLT) do not significantly affect survival decisions. A SWOT analysis identifies adaptation strategies: minimising damages through economic/environmental adjustments, optimising government assistance programs, and enhancing patron-client relationships.
- **Main contributions:** (1) Quantitative identification of survival decision determinants under extreme weather; (2) SWOT-based adaptation strategy framework for small-scale fishers; (3) Empirical documentation of the socioeconomic conditions of small-scale fishers during extreme weather (income drops from IDR 656K to 213K per trip; trips reduce from 5–6 to 2–3 per week).
- **Novelty:** Combines logistic regression modelling of survival decisions with SWOT-based adaptation strategy analysis — prior studies examined survival and adaptation separately or partially across different regions.

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | **No** | No AI content |
| Safety-critical AI decision-making | **No** | No AI system; decisions are purely human |
| AI governance / control mechanisms | **No** | No AI governance |
| Low-resource environments | **Partial** | Directly documents the resource constraints of small-scale fishers: low education (73.41% did not complete primary school), small vessels (<10 GT), limited technology, dependence on experience-based weather reading rather than meteorological data, income vulnerability |
| Decision architecture formalisation | **No** | Uses logistic regression as an analytical model, not a decision architecture; no formal decision system design |
| Human role in decision-making | **Partial** | Directly studies human fisher decision-making under weather uncertainty — the exact decision context my architecture aims to support. Fishers rely on experiential knowledge (natural indicators: sea wind, water temperature, marine organisms, currents) to make go/no-go decisions. No AI mediation exists |
| Socio-technical evaluation | **No** | No technology system evaluated |
| Coastal fisheries / maritime domain | **Yes** | Directly addresses small-scale coastal fishers' survival decisions and adaptation strategies under extreme weather in an Indonesian coastal context |

**Mid-Extraction Relevance Gate:** 1 Yes + 2 Partial → **REDUCED EXTRACTION** (Sections 4–7, 12–13, 16–17 only)

---

## 4. Decision Architecture Analysis

**No computational decision architecture exists in this paper.** The paper analyses *human* decision-making processes, not system-mediated decisions. However, the paper documents the implicit decision structure used by small-scale fishers, which is relevant as the *baseline human decision process* that my architecture aims to augment:

- **Decision type:** Binary go/no-go — fishers decide whether to venture to sea under extreme weather
- **Decision inputs (implicit environmental state vector):** Wind speed (5–40 knots depending on season), sea wave height (up to 2+ metres), precipitation intensity, tidal conditions, season classification (West season = dangerous Nov–Feb; East season = moderate Mar–Jun; Fishing season = favourable Mar–Jun)
- **Decision drivers:** Economic necessity (household survival), fishing experience, knowledge of safe near-shore fishing locations, government gear assistance
- **No safety classification system:** Fishers rely on experiential pattern recognition (natural indicators) rather than any formalised risk classification. The paper notes that fishers lack access to current meteorological data and depend exclusively on personal experience to forecast conditions.
- **No override or fallback mechanism:** The only "override" is the Indonesian Ministry of Maritime Affairs (KKP) issuing weather warnings instructing fishers not to sail — a binary advisory with no graduated response.

**Key observation for my research:** The environmental factors documented here — wind velocity, wave height, precipitation, season — map directly to the environmental state vector **E = {w, r, m, o, v, t}** in my architecture. The paper empirically confirms that these are the decision-relevant variables that fishers already attend to, but without formalised classification or graduated decision support.

---

## 5. Formal Model and Mathematical Representation

The paper uses a **logistic regression model** (not a decision architecture) to analyse the probability of fisher survival decisions:

**P_i / (1 - P_i) = β₀ + β₁(πCB) + β₂(FAge) + β₃(FFEdu) + β₄(FExp) + β₅(QFM) + δ₅(DmBLTp) + δ₆(DmIFA) + μ₁**

Where the dependent variable is the probability of deciding to survive as a fisher during extreme weather (binary: 1 = survive, 0 = other), and independent variables include fishing income, age, education, experience, family size, and dummy variables for BLT and fishing gear assistance programs.

**Comparison to DSR pipeline:** This model is fundamentally different from my pipeline **E → S = f(E) → (G(S), A_AI(S)) → AI(E)**:
- The logistic model is **retrospective/analytical** — it identifies which socioeconomic factors statistically predict fisher persistence. It does not prescribe or govern decisions.
- My pipeline is **prospective/prescriptive** — it classifies environmental state, gates AI participation, and constrains advisory scope in real time.
- The logistic model does not classify environmental states, does not define admissible actions, and does not implement governance.
- No state-dependent recommendation restriction, no Safety Dominance Property, no gate function.

**However:** The logistic model's independent variables partially overlap with my architecture's environmental and contextual inputs. The finding that experience and gear assistance (not education or cash) drive survival decisions provides empirical support for why decision support tools — rather than purely educational interventions — may be the appropriate response.

---

## 6. Safety State Classification

**No formal safety state classification.** The paper describes three seasons qualitatively:

| Season | Period | Conditions | Implicit Safety Level |
|---|---|---|---|
| West season | Nov–Feb | Intense winds (30–40 knots), heavy precipitation, waves >2m | UNSAFE (fishers face highest risk) |
| East season | Mar–Jun | Vigorous winds, heavy precipitation, but calm seas (5 knots) | Mixed / CAUTION analogue |
| Fishing season | Mar–Jun | Low winds, moderate precipitation, mild swells | SAFE |

These seasonal categories are **not formalised** — they emerge from fisher interviews as experiential knowledge rather than computed classifications. No thresholds, no rule-based classification function, no dynamic state transitions.

**Key observation:** The three-season structure described by fishers maps suggestively onto the tripartite {SAFE, CAUTION, UNSAFE} classification in my architecture, and provides empirical grounding for why a three-state (not binary) model is ecologically valid in this domain. The East season in particular — with mixed conditions (high precipitation but calm seas) — represents a natural analogue to the CAUTION state where conditions are neither fully safe nor fully dangerous.

---

## 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? | **No** | No AI system present |
| **Level 2 — Advisory scope governance** | What may AI recommend? | **No** | No AI recommendations |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | **No** | N/A |

The only governance mechanism described is the **KKP weather warning** — a binary advisory from the Ministry of Maritime Affairs instructing fishers not to sail during adverse conditions. This is a single-level, binary, human-institutional governance mechanism (sail/don't sail), not a computational AI governance system.

**Gap observation:** The paper documents that fishers routinely *ignore* this binary advisory because of economic necessity — they continue fishing near shore despite warnings. This directly supports the argument for a **graduated governance model** (my CAUTION state) rather than a binary permit/block approach. A system that provides restricted but useful advisory under marginal conditions (e.g., "fish near shore only, with caution, for limited duration") could align with how fishers actually behave, rather than issuing an all-or-nothing warning they ignore.

---

## 12. Key Concepts and Definitions

The following domain-specific concepts provide empirical grounding for my architecture's design context:

- **Survival decision:** The binary choice by small-scale fishers to continue or cease fishing under extreme weather; driven by economic necessity rather than rational risk assessment — the "survival decision" is closer to a forced choice than a free one
- **Near-shore/coastal fishing under extreme weather:** Fishers adaptively shift from open-sea to near-shore operations during adverse conditions — effectively a *self-imposed restriction on operational scope* analogous to the CAUTION state's restricted advisory space
- **Experiential weather indicators:** Fishers use natural cues (sea wind direction, water temperature, marine organisms, ocean currents) as informal environmental state variables — parallels the E vector but without formalisation
- **Three-season structure (West/East/Fishing):** Empirical seasonal classification with distinct risk profiles — informal precursor to a formal S = f(E) classification
- **Fishing trip frequency reduction:** During extreme weather, trips reduce from 5–6/week to 2–3/week; duration drops from 7–10 hours to 3–5 hours — quantitative evidence of adaptive operational restriction
- **Patron-client relationships:** Financial dependencies between fishers and intermediaries that constrain and enable fisher behaviour — a socioeconomic factor affecting decision autonomy
- **Eco-friendly fishing gear (EFFG):** Government-provided equipment (rods, gill nets) based on FAO's Code of Conduct for Responsible Fisheries (CCRF)
- **Vessel capacity constraint:** Small-scale vessels <10 GT cannot withstand severe weather — a hard physical safety constraint analogous to the vessel class variable (v) in my E vector

---

## 13. Limitations and Unsolved Problems

**Stated limitations:**
- Small sample size (79 households) in a single coastal area (Makassar City, Indonesia)
- Cross-sectional data (Oct–Dec 2023) rather than longitudinal tracking across seasons
- Nagelkerke R² of 36.7% — the model explains only about a third of variance in survival decisions, indicating significant unmeasured factors
- SWOT analysis is qualitative/descriptive rather than formally validated

**Unsolved problems / future work:**
- No mechanism for providing fishers with real-time, actionable weather information — the paper notes fishers lack access to meteorological data
- No graduated decision support — the only external intervention described is a binary "don't sail" warning from KKP
- No assessment of what specific decision support fishers would actually use or trust
- No formal risk classification despite the implicit three-season structure

**Alignment with my research problem:**
- The paper documents the **exact decision gap** my architecture addresses: fishers make safety-critical go/no-go decisions under weather uncertainty with no formal decision support, no graduated advisory, and no state-sensitive recommendations
- The paper does **not** identify this as an AI governance gap (it operates outside the AI discourse entirely), but it provides strong empirical evidence for **why** a graduated, weather-state-conditioned decision support system is needed
- The finding that fishers ignore binary warnings but adaptively self-restrict operations (near-shore, shorter trips) directly supports the design rationale for a CAUTION state with restricted-but-non-empty advisory scope rather than binary permit/block

---

## 16. Relation to My Research and Positioning

- **Level 1 governance:** Not implemented (no AI system)
- **Level 2 governance:** Not implemented
- **State-conditioned governance pair:** Not applicable
- **Formal safety property:** None defined
- **Gap my research addresses:** This paper documents a real-world decision context in which small-scale coastal fishers make safety-critical decisions without any formal decision support, weather-state classification, or graduated advisory system. The entire gap that my architecture fills is present: no formalised environmental state classification, no AI participation governance, no advisory scope restriction, and no Safety Dominance Property.

**Positioning paragraph:** This paper provides **critical empirical grounding** for my architecture's design rationale and case study context. It documents the exact decision scenario my system targets — small-scale coastal fishers making go/no-go decisions under extreme weather — and reveals that the current decision environment has no formal risk classification, no graduated advisory mechanism, and relies entirely on experiential knowledge and binary governmental warnings that fishers routinely override due to economic necessity. Crucially, the paper shows that fishers already *adaptively self-restrict* their operations during marginal conditions (shifting to near-shore fishing, reducing trip duration and frequency), which provides direct behavioural evidence for the CAUTION state's restricted-but-non-empty advisory scope as ecologically and socially valid. The environmental variables documented (wind velocity, wave height, precipitation, season, vessel size) map directly onto the E vector in my architecture. This paper is best positioned in the **domain background / problem motivation subsection**, providing empirical evidence for (a) the safety-critical nature of fishing decisions, (b) the absence of formal decision support, (c) the inadequacy of binary warnings, and (d) fishers' existing adaptive behaviour that a graduated architecture should align with.

---

## 17. Overall Relevance Score

### ⭐⭐ Low — with elevated domain utility

**Justification:** The paper contains no AI content, no decision architecture, no formal models, and no governance mechanisms relevant to the core architectural contribution. It scores ⭐⭐ by the standard rating criteria. However, within the ⭐⭐ tier it has **unusually high strategic value** compared to other domain background papers because: (1) it directly documents the *exact decision scenario* the architecture targets (fisher go/no-go decisions under weather uncertainty), (2) it provides quantitative socioeconomic data on the decision context (income impacts, trip reduction, vessel constraints), (3) it reveals that fishers' adaptive self-restriction behaviour validates the CAUTION state concept, and (4) the environmental variables documented map directly onto the E vector. Among domain background papers, this one speaks most directly to the *human decision-making baseline* that the architecture augments.
