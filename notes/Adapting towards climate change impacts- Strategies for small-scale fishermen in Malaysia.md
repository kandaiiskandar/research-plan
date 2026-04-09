# Structured Extraction: Shaffril et al. (2017)

## 1. Citation & Metadata

- **Authors:** Hayrol Azril Mohamed Shaffril, Asnarulkhadi Abu Samah, Jeffrey Lawrence D'Silva
- **Title:** Adapting towards climate change impacts: Strategies for small-scale fishermen in Malaysia
- **Year:** 2017
- **Venue:** Marine Policy (Elsevier)
- **Volume/Pages:** 81, 196–201
- **DOI:** [10.1016/j.marpol.2017.03.032](http://dx.doi.org/10.1016/j.marpol.2017.03.032)
- **Peer-reviewed:** Yes
- **Type:** Conceptual/narrative review with policy recommendations

---

## 2. Research Problem (as relevant to this study)

The paper documents the environmental conditions, decision constraints, and socio-economic profile of Malaysian small-scale fishermen — the exact target population for the proposed safety-state-gated architecture. Its value lies not in AI or governance content (it has none) but in providing peer-reviewed empirical grounding for three architectural design choices: (a) the composition of the environmental state vector E, (b) the selection of environmental safety state as the governance trigger, and (c) the socio-technical constraints that any decision support system must satisfy in this domain.

---

## 3. Relevance Gate: Eight Core Research Themes

| # | Theme | Relevant? | Notes |
|---|---|---|---|
| 1 | Hybrid AI (rule-based + probabilistic) | ❌ | — |
| 2 | Safety-critical AI decision-making | ❌ | — |
| 3 | AI governance/control mechanisms | ❌ | — |
| 4 | Low-resource environments | ✅ Strong | Core population: low-income, low-education fishermen on small vessels |
| 5 | Decision architecture formalisation | ❌ | — |
| 6 | Human role in decision-making | ✅ Moderate | Participatory adaptation planning; fishermen as active decision agents |
| 7 | Socio-technical evaluation | ✅ Moderate | Strategies framed around community needs, abilities, interests |
| 8 | Coastal fisheries/maritime domain | ✅ Strong | Malaysian small-scale fisheries — exact application domain |

**Gate result:** Passes on reduced path — domain-context paper.

---

## 4. Empirical Grounding for Environmental State Vector E

This is the paper's primary contribution to the dissertation. The climate change evidence documented maps directly onto the components of E = {w, r, m, o, v, t}:

| E component | Evidence from paper |
|---|---|
| **w (wind condition)** | Razali et al. (2010) confirmed long-term risk of extreme wind speeds in Alor Star, Kuantan, Mersing, and Kota Bharu. North-east monsoon brings extreme winds that suspend boat rental services and fishing operations. Wind is a primary driver of the binary go/no-go decision. |
| **r (rainfall intensity)** | Extreme rainfall events have exceeded the 90th percentile of total rainfall at multiple meteorological stations since the 1980s (Wan Azli, 2010). 2015 Kelantan floods destroyed 11 ha of agricultural land — demonstrates cascading impacts of extreme rainfall on fishermen with occupational mobility into agriculture. |
| **m (marine warning level)** | Not cited as a formal classification in this paper, but the north-east monsoon functions as a de facto seasonal marine warning — fishermen treat monsoon onset as a system-level signal to cease or drastically reduce operations. The paper implicitly supports the role of an official marine warning level (e.g., MetMalaysia warnings) as the institutional analogue of the informal monsoon-based signal fishermen already respond to. |
| **o (ocean condition: wave, tide, current)** | Extreme waves identified as a major contributor to coastal erosion (29.1% of Malaysia's 4,809 km coastline experiencing critical erosion). Extreme waves in 2012 forced relocation of 41 families in Kuala Besut, Terengganu. Warmer temperatures affect fish migration, spawning, and algal blooms — ocean conditions drive both safety risk and resource availability. |
| **v (vessel class)** | Small-scale fishermen operate vessels ≤22 feet, within <5 nautical miles of shore, using nets, rods, or rawai. This vessel class is highly vulnerable to environmental conditions — small size means rapid environmental state transitions (wind, wave) have immediate safety consequences. The paper's entire framing of vulnerability is conditioned on this vessel class: it is the vessel constraint that makes identical environmental conditions dangerous for small-scale fishermen but manageable for larger commercial operators. |
| **t (trip state)** | Fishing trips are 5–9 hours in duration. The paper documents that during the north-east monsoon, operating days are reduced by up to 90% — decisions about whether to initiate a trip (pre-departure), continue a trip, or return early are all conditioned on environmental state. Boat rental services to islands are "temporarily suspended" during monsoon — a trip-state-level decision (do not depart). The paper does not differentiate governance behaviour across trip phases, but the evidence supports that trip state interacts with environmental conditions to determine risk. |

**Key implication:** The environmental parameters that drive real-world fishing decisions in this domain are observable, measurable, and correspond to the proposed state vector. This is not a design assumption — it is an empirical characteristic of the domain.

---

## 5. Evidence for Binary Status Quo (Motivation for CAUTION Mode)

The paper documents that the current human response to environmental risk is **binary go/no-go**:

- During the north-east monsoon, operating days are reduced by **up to 90%** in a month — fishermen either go out or they don't.
- No intermediate strategy is documented where fishermen modify *what they do* under elevated-but-non-extreme risk (e.g., restricting to nearshore zones, changing target species, reducing trip duration, adjusting gear).
- Fishermen with occupational mobility shift to alternative income sources (tourism, agriculture) during monsoon — a binary switch between occupations, not a graduated adjustment within fishing.
- Boat rental services to islands like Redang and Perhentian are "temporarily suspended" during monsoon — again, binary cessation, not graduated restriction.

**Architectural implication:** The binary status quo is functionally equivalent to a Level 1 participation gate G(S) enacted by the fishermen themselves: S = UNSAFE → don't fish; S = SAFE → fish normally. There is no equivalent of A_AI(CAUTION) — no graduated, scope-restricted response at intermediate risk states. This gap exists at the *operational practice* level, not just in the AI literature, strengthening the motivation for the proposed CAUTION mode.

---

## 6. Socio-Technical Constraints for Architecture Design

The paper establishes the user population profile that constrains any decision support system in this domain:

| Constraint | Evidence | Design implication |
|---|---|---|
| **Low income** | >30% earn below RM 500/month (≈ USD 166); monthly income RM 500–1000 | Low-resource environment assumption is empirically grounded; technology must be low-cost or zero-cost to end user |
| **Low education** | MCE (Malaysian Certificate Education) or lower | Interface must be simple; governance logic must be comprehensible without technical literacy; supports environmental state over model uncertainty as governance trigger — fishermen understand weather, not confidence intervals |
| **Age** | Generally >40 years old | Technology adoption barriers; existing mental models of risk are weather-based, not probabilistic |
| **Small vessels** | ≤22 feet, operating <5 nautical miles from shore | High vulnerability to environmental conditions; rapid environmental state transitions have immediate safety consequences; nearshore operations mean environmental state is directly observable |
| **Mobile phone usage** | Identified as heavy mobile phone users (Omar et al., 2011; Shaffril et al., 2015) | Fisher Friend-type mobile technology identified as feasible warning mechanism; establishes that mobile-based decision support is a realistic deployment platform |
| **Strong place attachment** | Fishermen display strong attachment to residence; forced relocation causes stress and conflict | Socio-technical evaluation (PS5) must account for cultural context; system must work *within* existing community structures, not displace them |
| **Existing cooperative culture** | Gotong royong (mutual cooperatives), merewang (wedding cooperatives) | Community-level trust and social capital exist; PS5 evaluation should leverage existing social structures for adoption |

---

## 7. Governance Trigger Rationale: Why Environmental State

This paper provides the **domain-side argument** for conditioning governance on environmental safety state S = f(E) rather than AI-internal metrics:

1. **Decision legibility.** Fishermen already make go/no-go decisions based on observable environmental conditions (wind, waves, rain, monsoon season). Conditioning AI governance on the same parameters ensures the system's decision logic is *legible* to its users. An AI system that restricts its advisory scope because "wind speed exceeds threshold X" is comprehensible to a fisherman in a way that "model confidence dropped below 0.7" is not.

2. **Low-education population.** With MCE-or-lower education levels and ages generally >40, this population cannot be expected to interpret AI confidence scores, uncertainty estimates, or reward functions. Environmental state is the *only* governance trigger that aligns with the users' existing mental models of risk.

3. **Direct observability and experiential verification.** The dynamic parameters (w, r, m, o) are directly observable or experientially verifiable by fishermen operating within <5 nautical miles of shore — they can see the wind, feel the waves, and check the rain. The contextual parameters (v, t) are known facts about their own vessel and current trip phase. This creates a natural trust mechanism: the fisherman can verify that the system's state classification matches their own perception. No such verification is possible for AI-internal metrics like model confidence or uncertainty estimates.

4. **Causal proximity.** In this domain, the *environmental conditions themselves* are the source of danger (extreme waves, winds, reduced visibility), not AI model degradation. Conditioning governance on the *cause* of risk (environmental state) rather than a *symptom* of risk (model uncertainty) is the architecturally correct choice for safety-critical maritime environments.

---

## 8. Mapping onto Architecture Components

| Component | Mapping | Strength |
|---|---|---|
| **E = {w, r, m, o, v, t}** | All parameters except visibility are directly evidenced as real-world fishing decision drivers in this domain | ✅ Strong |
| **S = f(E)** | Current practice implements an informal binary classification: monsoon → don't fish; normal season → fish | ✅ Supports motivation |
| **G(S)** | Human-enacted binary participation gate exists in practice (90% operating day reduction during monsoon) | ✅ Supports gap argument |
| **A_AI(S)** | ❌ Not present in paper — no AI system discussed | Confirms gap |
| **CAUTION mode** | ❌ No intermediate graduated response documented in current practice | Confirms gap |
| **Safety Dominance Property** | ❌ Not applicable | — |

---

## 9. Relevance to PS4 and PS5

| Study | Relevance |
|---|---|
| **PS4 (graduated vs. binary governance)** | The binary monsoon go/no-go regime documented here is the **ecological validity baseline** for PS4. The evaluation tests whether graduated governance (with CAUTION mode) improves upon this binary status quo. Shaffril et al. provide the empirical evidence that the binary regime is the actual current practice, not a theoretical strawman. |
| **PS5 (socio-technical evaluation)** | The paper's central framing — adaptation strategies must align with community "needs, abilities and interests" — is directly applicable to PS5. The socio-technical constraints (low income, low education, strong place attachment, cooperative culture) define the evaluation criteria: the CAUTION mode must be understandable, trustworthy, and culturally appropriate for this population. |

---

## 10. Relevance Score

### ⭐⭐⭐ (Three Stars) — Domain-Context Reference with Environmental State Grounding

**Justification:** No AI, no formal methods, no governance architecture. However, provides essential empirical grounding for (a) the environmental state vector composition, (b) the binary status quo that motivates the CAUTION mode, (c) the socio-technical constraints on architecture design, and (d) the domain-side argument for environmental state as the governance trigger. Three-star rating reflects high domain relevance despite nil architectural content.

---

## 11. Positioning Paragraph

Shaffril et al. (2017) ground the proposed architecture's environmental state vector E = {w, r, m, o, v, t} in peer-reviewed evidence from the target domain. The paper documents that the observable environmental parameters driving Malaysian small-scale fishermen's decisions — wind condition, rainfall intensity, ocean conditions (waves, tides, currents), and monsoon seasonality — correspond to the dynamic components of the proposed state vector (w, r, o), while the vulnerability profile (vessels ≤22 feet, <5 nautical miles from shore, 5–9 hour trips) grounds the contextual components (v, t) and implicitly supports the role of an official marine warning level (m) as the institutional analogue of the monsoon-based signal fishermen already respond to. Critically, the paper reveals that the current decision regime is binary: during the north-east monsoon, fishermen reduce operations by up to 90%, with no documented intermediate strategy for modifying fishing behaviour under elevated but non-extreme risk. This binary go/no-go practice, functionally equivalent to a human-enacted Level 1 participation gate G(S), provides both the empirical motivation for a graduated CAUTION mode and the ecological validity baseline for PS4. The paper's characterisation of the user population — low income (>30% below RM 500/month), low education (MCE or lower), aged >40, operating vessels ≤22 feet within <5 nautical miles of shore — establishes the socio-technical constraints that mandate environmental safety state, rather than AI-internal metrics, as the governance trigger: these fishermen understand weather, not confidence intervals.

---

## 12. Citation Placement Recommendations

| Section | Use |
|---|---|
| **Environmental state vector justification (primary placement)** | Empirical evidence that E components (wind, rainfall, wave height, ocean conditions, monsoon timing) are the actual decision drivers in this domain |
| **Governance trigger rationale** | Domain-side argument for environmental state over AI-internal metrics: decision legibility, low-education population, direct observability, causal proximity to source of danger |
| **Binary governance gap argument** | Evidence that current practice is binary go/no-go (90% operating day reduction during monsoon), supporting the claim that graduated governance is absent at the operational level |
| **PS4 design rationale** | Establishes the binary status quo as ecological validity baseline against which graduated governance is evaluated |
| **PS5 design rationale** | Socio-technical constraints (needs, abilities, interests framework) defining evaluation criteria for CAUTION mode acceptance |
| **Chapter 1 — Application domain characterisation (supporting)** | Population demographics, vessel size, income, geographic distribution |

---

## 13. Methodological Caution

This is a **narrative review**, not a systematic review. No PRISMA flow, no formal inclusion/exclusion criteria, no quality appraisal. Quantitative claims (e.g., 32% catch reduction, 90% operating day reduction) are drawn from secondary sources — for load-bearing empirical claims, cite the originals (Omar & Quah, 2005; Shaffril et al., 2016) rather than this paper's secondary citations. Use Shaffril et al. (2017) for the synthesis and framing, not as primary evidence.
