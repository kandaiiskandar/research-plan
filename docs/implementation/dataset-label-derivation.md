# Dataset Label Derivation: Advisory AI Training Labels from Empirical Fisher Studies

**Document type**: Dataset methodology note  
**For**: RQ3 (prototype implementation) — advisory AI training dataset  
**Prepared**: May 2026  
**Study site**: Kota Kinabalu, Sabah — Western Sabah and Labuan coastal waters

---

## 1. Context: Two Separate ML Questions

The architecture contains two distinct components that could involve ML. These must not be conflated:

| Component | Layer | Approach | Rationale |
|---|---|---|---|
| Safety classifier **f(E)** | Layer 2 | **Rule-based — not ML** | Safety Dominance Property holds by construction; deterministic rules from MET Malaysia published criteria; this is the formal contribution |
| Advisory AI **AI(E)** | Layer 3 | **ML-trainable** | Generates departure recommendations within the admissible action space A_AI(S); can learn from empirical fisher decision patterns |

This document concerns the **advisory AI layer only**. The safety classifier is intentionally rule-based and requires no training dataset.

---

## 2. What the Advisory AI Needs to Learn

The advisory AI takes the environmental state E and governance state S as input and generates a recommendation within A_AI(S):

| Governance state | A_AI(S) — admissible actions | ML task |
|---|---|---|
| **SAFE** | {Go, Delay, DepartureTime, Duration} | Predict departure recommendation + timing/duration |
| **CAUTION** | {Go, Delay} | Predict Go or Delay only |
| **UNSAFE** | ∅ — AI gated off | No prediction — G(S) = 0 |

For an initial feasibility dataset, the label is simplified to the primary departure decision: **`Go` or `Delay`** — the binary choice that applies across both SAFE and CAUTION states and is the most fundamental question every fisher faces each morning.

---

## 3. Label Source: Three Empirical Fisher Studies

Labels are derived from documented real-world departure decision patterns across three independent empirical studies of small-scale fishers in Malaysia and coastal Indonesia. Environmental conditions described in each study are mapped to E vector values using MET Malaysia's published warning criteria.

### 3.1 Rahim et al. (2024) [[notes]](../../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md)

**Study:** 79 small-scale fishing households, coastal Makassar City, Indonesia. Quantitative survey with logistic regression. Published in *Journal of Marine and Island Cultures*.

This study provides the most quantitatively detailed behavioral regimes, documenting three distinct seasons with explicit wind speed and wave height values and corresponding fisher behavior:

| Season | Documented conditions | Fisher behavior | Mapped label |
|---|---|---|---|
| **Fishing season** (Mar–Jun) | Low winds, moderate precipitation, mild swells | Full operations: 5–6 trips/week, 7–10 hours per trip | **Go** |
| **East season** (Mar–Jun, wind-dominant) | Vigorous winds, heavy precipitation, but calm seas ⚠️ *(see note)* | Restricted operations: 2–3 trips/week, 3–5 hours, near-shore only | **Delay** |
| **West season** (Nov–Feb) | Intense winds 30–40 knots, heavy precipitation, waves >2m | "Do not go at all" — dramatic curtailment of fishing activity | **AI off** (UNSAFE state; G(S) = 0) |

**Key quantitative evidence:**
- Trip frequency reduction from 5–6/week → 2–3/week under marginal conditions → **Delay** label
- Trip duration reduction from 7–10 hours → 3–5 hours under marginal conditions → **Delay** label  
- Near-shore operational shift under elevated wind → confirms CAUTION-state behavior
- Income drop from IDR 656K → 213K per trip under adverse conditions → risk is real and economic

> **Resolved 2026-09-06 — East season is CAUTION via rainfall, not wind.**
>
> The East season row previously read "Vigorous winds, heavy precipitation, but calm seas **(~5 knots wind)**", which is self-contradictory — 5 knots is Beaufort force 2 and classifies SAFE under `g_w`, not the CAUTION implied by the restricted-operations behaviour.
>
> Checking the source notes: Rahim reports wind across all three seasons spanning **5–40 knots**, with West season at 30–40 kn. The 5 kn figure sits at the bottom of that range and is not obviously a transcription error. Reading the three seasons together resolves the mapping:
>
> | Season | Wind | Precipitation | Seas | Classifies as |
> |---|---|---|---|---|
> | Fishing | low | **moderate** | mild swells | SAFE — `g_r(moderate)` = SAFE |
> | East | ~5 kn (SAFE) | **heavy** | calm | **CAUTION — via `g_r(heavy)`** |
> | West | 30–40 kn | heavy | > 2 m | UNSAFE — via `g_w` |
>
> The distinction between Fishing season and East season is precisely **moderate vs. heavy precipitation** — exactly where `g_r`'s SAFE/CAUTION boundary sits. The East season → Delay evidence therefore holds, but it supports the **rainfall-driven** CAUTION row in §4, not a wind-driven one. §4 has been amended accordingly; East season no longer underwrites the 22–27 kn row.
>
> **Source verified 2026-09-06.** The original paper was checked directly. It states: *"The East Season transpires from March to June, marked by vigorous winds and substantial precipitation but calm seas. In the East Season, the wind velocity is 5 knots per hour."* **The contradiction is in the source, not in these notes.** Three further points emerged from that check:
>
> **(a) West season figures are gusts, not sustained wind.** The paper reads: *"sea waves may exceed 2 meters, accompanied by wind **gusts** of 30 to 40 knots per hour."* Since `w` is defined as sustained wind speed, 30–40 kn gusts imply roughly 19–31 kn sustained at typical gust ratios — straddling rather than clearly exceeding the 27 kn UNSAFE boundary. **West season's UNSAFE classification therefore rests on wave height (> 2 m → UNSAFE for a small vessel under `g_o`), not on wind.** The corresponding citation has been removed from `appendix-c` C.2's `g_w` row.
>
> **(b) East and Fishing seasons overlap.** Both are given as March–June. The paper separately describes the Fishing season as *"low wind velocities, moderate precipitation, and mild oceanic swells."* Since East season is 5 kn — also low — the two are not distinguished by wind at all. They are distinguished by **precipitation: substantial vs. moderate**, which is exactly the `g_r` SAFE/CAUTION boundary. This reinforces the mapping above rather than undermining it.
>
> **(c) The contradiction is itself a finding.** The paper appears to combine meteorological data (5 kn sustained, plausibly from BMKG) with fisher interview descriptions ("vigorous"). Fishers characterising a 5 kn sustained wind as vigorous is a divergence between measured conditions and perceived risk — relevant to RQ5, which asks whether operators interpret governance states as intended. If perception diverges from measurement at the input side, that is a consideration for how classified states are communicated. Worth carrying into the RQ5 discussion rather than treating purely as a data-quality defect.

The East season behavioral pattern — where fishers continue to sea but with restricted scope and near-shore operations — is the closest empirical analogue to the CAUTION state, driven by heavy precipitation rather than wind. The West season pattern (30–40 kn, waves > 2 m) — full halt — confirms the UNSAFE threshold and is internally consistent, since 30–40 kn exceeds the 27 kn boundary.

### 3.2 Gao (2024) [[notes]](../../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md)

**Study:** 25 semi-structured interviews, small-scale gill net fishers, Penang, Malaysia. Qualitative causal mapping methodology. M.Sc. thesis, CGIAR/WorldFish repository.

This study documents the tripartite decision structure used by Penang fishers and provides direct quotes that map to the three governance states:

| Decision type | Documented behavior | Mapped label |
|---|---|---|
| **Go** (favourable conditions) | Full operational scope: fishers decide timing, location, species, trip duration | **Go** |
| **Cautious-go** (marginal conditions) | Shortened trips, near-shore operations, heightened monitoring, location changes | **Delay** |
| **Don't go** (adverse conditions) | *"If the wind is too strong, I don't go"* — trips cancelled entirely | **AI off** (UNSAFE) |

**Environmental factor importance ratings from Penang fishers (1–5 scale):**
- Tide: **4.55** — highest rated
- Fishing resource: **4.45**
- Previous catch: **4.38**
- Weather (wind, w): **3.75**
- Safety concern: **3.40**

> **Correction 2026-09-06.** The first item was previously annotated "Tide (**ocean state, o**)". **Tide is not `o`.** `o` is ocean state — wave height and swell period, driven by wind and swell propagation. Tide is tidal height, driven by lunar and solar forcing. They are distinct physical phenomena with different determinants and different time signatures. The conflation matters twice over: it misrepresents what Gao's respondents rated, and it implies E captures the fishers' highest-rated factor when it does not.
>
> **Tide is not in E at all.** This is a genuine scope limitation rather than a transcription slip, and it should be stated as such: the highest-rated decision factor in the only Malaysian study that ranked factors is absent from the environmental state vector. Two of the top three (fishing resource, previous catch) are likewise absent — though those are catch-productivity factors rather than safety factors, so their exclusion from a *safety* classifier is defensible. Tide is less clearly defensible: tidal state affects harbour access, bar crossing, and grounding risk for shallow-draft vessels. Recorded as a limitation in `appendix-c-formalisation.md` C.9 — see the follow-up note below.

The documented informal tripartite classification (go / cautious-go / don't go) directly parallels the formal SAFE / CAUTION / UNSAFE states, and this remains the study's principal contribution to the label logic. The factor ratings confirm that weather and safety concern are *among* the determinants fishers weigh, but they do not establish w and o as the *primary* ones — tide outranked both.

**Architectural alignment (from notes):** *"Fishers already operate an informal version of graduated, state-conditioned decision-making — they assess environmental state, classify conditions, and adjust both their participation and the scope of their decisions accordingly. My architecture formalises what fishers do intuitively."*

### 3.3 Yamin et al. (2025) [[notes]](../../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md)

**Study:** 136 small-scale fishers, five coastal villages, central Terengganu, Malaysia. Quantitative questionnaire with SEM analysis. Published in *Frontiers in Marine Science* (Q1), 2025.

This is the most recent and methodologically strongest study in the corpus for empirical grounding of E vector parameters. Key contributions to label derivation:

| Finding | Implication for labels |
|---|---|
| 95% of fishers identify stronger winds and larger waves as primary hazard | Go/No-Go trigger conditions confirmed as w and o → threshold values anchored to MET criteria |
| 91% identify erratic rainfall as primary hazard | Rainfall intensity (r) is a valid co-trigger for Delay/No-Go labels |
| *"If it's suddenly windy/change of weather, I can't go fishing"* — empirical knowledge item | Direct Go/No-Go binary confirmed; strong winds → **Delay or AI off** |
| **Flexibility is the weakest adaptive capacity domain** (only 58% willing to consider alternatives; 67.6% solely fishing-dependent) | Fishers currently operate binary (Go or No-Go); the **Delay** label represents the graduated response that the CAUTION mode enables — a capability they currently *lack* |
| Traditional knowledge declining; fishers using Windy/Windfinder apps | Decision support vacuum at intermediate risk states validates the Delay label as a genuinely useful output |

**Critical architectural implication:** Yamin et al. (2025) establish that the binary go/no-go pattern is the *current* baseline, not the desired outcome. The **Delay** label in the CAUTION state represents a graduated response that the population cannot currently execute without decision support — making the advisory AI's Delay recommendation genuinely novel and useful, not a replication of existing behavior.

---

## 4. Label Derivation Logic

Combining the three studies, the label logic is as follows. Environmental conditions are expressed using MET Malaysia's Kawasan Perairan range bands and warning thresholds.

> **Revision 2026-09-06 — wave thresholds are now vessel-conditional.** The previous version of this table specified wave-height bands without reference to vessel category, using the single vessel-blind set (< 1.5 / 1.5–3.5 / > 3.5 m). Under the amended model, `g_o(o, v)` selects thresholds by vessel category, so the same wave height maps to different states for different vessels. Several rows below were **wrong for the deployment population** — e.g. "waves 1.5–3.5 m → CAUTION" holds for a big vessel but a small vessel is UNSAFE above 1.9 m. Since these rows generate training labels, the error would have mislabelled the training data for exactly the vessel class the system is built for. Table restructured below.

**Vessel-independent conditions** — these determine S regardless of vessel category:

| Condition | Classification |
|---|---|
| Wind ≤ 22 kn | SAFE |
| Wind 22–27 kn | CAUTION |
| Wind > 27 kn | UNSAFE |
| Rain none / light / moderate | SAFE |
| Rain heavy | CAUTION |
| Rain storm (Ribut Petir) | UNSAFE |
| Warning none | SAFE |
| Warning advisory (Category 1) | CAUTION |
| Warning warning / alert (Category 2/3, Ribut Taufan) | UNSAFE |
| Time 06:00–17:00 | SAFE |
| Time 17:00–19:00 | CAUTION |
| Time 19:00–06:00 | UNSAFE |

**Wave height — conditional on vessel category:**

| v (GRT) | SAFE | CAUTION | UNSAFE |
|---|---|---|---|
| small (< 10) | o < 1.0 m | 1.0–1.9 m | > 1.9 m |
| medium (10–25) | o < 1.4 m | 1.4–2.8 m | > 2.8 m |
| big (> 25) | o < 1.5 m | 1.5–3.5 m | > 3.5 m |

**Label logic for the primary deployment case (small vessel, < 10 GRT):**

| Environmental conditions (E) | S | Study evidence | Label |
|---|---|---|---|
| Wind ≤ 22 kn, waves < 1.0 m, none/light/moderate rain, no warning, daytime | **SAFE** | Rahim fishing season; Gao "go" pattern | **Go** |
| Wind 22–27 kn, waves < 1.0 m, no warning, daytime | **CAUTION** | Gao "cautious-go" pattern under elevated wind; MET Category 1 onset | **Delay** |
| Wind ≤ 22 kn, waves 1.0–1.9 m, no warning, daytime | **CAUTION** | Yaakob operability limits for Zone A hulls; Jeong & Im ≤10 m departure restriction | **Delay** |
| Wind ≤ 22 kn, waves < 1.0 m, heavy rain (below Ribut Petir), no warning | **CAUTION** | **Rahim East season** — heavy precipitation with light wind and calm seas, restricted operations; Yamin erratic rainfall as primary hazard | **Delay** |
| Wind ≤ 22 kn, waves < 1.0 m, advisory (Category 1) active, daytime | **CAUTION** | MET Category 1 = *berbahaya kepada bot-bot kecil* | **Delay** |
| Wind > 27 kn, any waves, any rain | **UNSAFE** | Rahim West season "do not go at all"; Gao "if wind too strong, I don't go" | **AI off** |
| Any wind, **waves > 1.9 m** | **UNSAFE** | Yaakob: 6.54 m hull exceeds NORDFORSK limits at SS4 (Hs ≈ 1.875 m) | **AI off** |
| Any conditions, Ribut Petir active | **UNSAFE** | Yamin: sudden weather change = can't go | **AI off** |
| Any conditions, Ribut Taufan / Category 2–3 warning active | **UNSAFE** | Tropical cyclone or higher-tier warning = unconditional halt | **AI off** |
| Any conditions, t ∈ [19:00, 06:00) | **UNSAFE** | Night navigation; Atacan & Düzbastılar highest consequence scores | **AI off** |

For medium and big vessels the same logic applies with the corresponding wave-height row substituted. **Every training row must therefore carry `v_vessel`** — the label cannot be derived from weather alone.

**Value interpretation rule**: Upper bound of each MET range band is used (e.g., 10–20 km/h → treated as 20 km/h). This is consistent with the worst-case (max-severity) aggregation principle in the architecture.

**Note on the previous "Category 1+ warning" phrasing.** An earlier row read "Wind >27 knots, waves >3.5m, any rain, Category 1+ warning → UNSAFE". Category 1 corresponds to `advisory`, which classifies **CAUTION**, not UNSAFE; only Category 2/3 (`warning`, `alert`) classify UNSAFE. That row's conclusion was correct only because wind > 27 kn drives UNSAFE independently. The warning tiers are stated explicitly above to avoid the ambiguity.

---

## 5. Dataset Structure

Each row represents one departure decision scenario. The dataset has the following schema:

| Column | Type | Description | Source |
|---|---|---|---|
| `w_kmh` | Numeric | Wind speed (km/h) — upper bound of MET range | Kawasan Perairan |
| `w_knots` | Numeric | Wind speed (knots) — converted for classification | Derived |
| `o_m` | Numeric | Wave height (m) — upper bound of MET range | Kawasan Perairan |
| `r_cat` | Categorical | Rainfall: none / light / moderate / heavy / storm | Kawasan Perairan weather text |
| `m_warning` | Categorical | Marine warning: none / cat1 / cat2_3 / ribut_petir / ribut_taufan | MET warning bulletin |
| `v_vessel` | Categorical | Vessel category: small / medium / big | Fisher registration |
| `t_hour` | Numeric | Hour of day (0–23) | System clock |
| `S` | Categorical | Governance state: SAFE / CAUTION / UNSAFE | f(E) output — deterministic |
| `G_S` | Binary | AI gate: 1 = active, 0 = off | Derived from S |
| `A_AI_S` | Categorical | Admissible scope: full / restricted / none | Derived from S |
| `label` | Categorical | **Departure recommendation: Go / Delay / AI_off** | **Derived from three empirical studies** |

---

## 6. Methodological Justification

### 6.1 Why This Approach Is Valid

Labels derived from empirical fisher decision patterns are **stronger than rule-based synthetic labels** for three reasons:

1. **Behavioral grounding.** The labels reflect documented real-world decisions made by experienced fishers under real conditions — not what a researcher assumes a fisher should do. The advisory AI learns to replicate the collective wisdom of the studied fisher population.

2. **Cross-validation across three independent studies.** The same tripartite behavioral pattern — full operations / restricted operations / no operations — appears consistently across Penang (Gao, 2024), Terengganu (Yamin et al., 2025), and coastal Indonesia (Rahim et al., 2024). This convergence across three independent study sites strengthens confidence in the label logic.

3. **MET Malaysia threshold alignment.** The environmental conditions that trigger each behavioral shift in the empirical literature align with MET Malaysia's published warning criteria — the same thresholds used to anchor the UNSAFE classification boundary. This ensures internal consistency between the classification function f(E) and the advisory AI's training labels.

### 6.2 Limitation

The empirical studies describe seasonal and qualitative conditions (e.g., "vigorous winds, calm seas"), not precise hourly measurements. Mapping these to specific MET range band values involves interpretation. The mapping is documented explicitly in Section 4 and is grounded in the MET criteria, but the resulting labels should be treated as **expert-derived approximations** rather than directly observed ground truth. Validation against actual Kota Kinabalu fisher decisions — through the RQ5 user study — will provide ground truth confirmation.

### 6.3 Scope

The current label set covers the primary departure decision (**Go / Delay**). The full A_AI(SAFE) scope — including DepartureTime and Duration recommendations — requires additional domain expert elicitation or fisher interview data to label. These are second-phase labels deferred to the RQ5 fieldwork.

---

## 7. Source Summary

| Study | n | Location | Method | Label contribution |
|---|---|---|---|---|
| Rahim et al. (2024) [[notes]](../../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) | 79 households | Makassar, Indonesia | Logistic regression + SWOT | Three-season behavioral regime with explicit wind/wave values; trip frequency and duration data |
| Gao (2024) [[notes]](../../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md) | 25 interviews | Penang, Malaysia | Qualitative causal mapping | Tripartite go/cautious-go/don't-go decision structure; direct fisher quotes; environmental factor importance ratings |
| Yamin et al. (2025) [[notes]](../../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md) | 136 fishers | Terengganu, Malaysia | Questionnaire + SEM | Empirical knowledge items ("if windy, I can't go"); hazard prevalence data (95%, 91%); flexibility deficit confirming Delay label novelty |

---

## 8. Implication for the Architecture

The label derivation finding reinforces a key architectural distinction that must be communicated clearly to the supervisor:

> **The safety classifier f(E) is rule-based and requires no training data.** Its thresholds are anchored to MET Malaysia's published institutional criteria — this is the formal contribution.
>
> **The advisory AI AI(E) can be ML-trained.** Its labels are derivable from three independent empirical studies of small-scale fisher departure decisions. A feasibility dataset can be constructed now from these labels and MET Malaysia's Kawasan Perairan range vocabulary.
>
> **The governance layer enforces safety regardless of the advisory AI's training quality.** Even if the advisory AI makes suboptimal recommendations, the Safety Dominance Property (AI(E) ⊆ A_AI(S)) holds — the governance layer contains the AI's output within the admissible action space for the current safety state. This is the architectural guarantee that ML training uncertainty cannot compromise safety.
