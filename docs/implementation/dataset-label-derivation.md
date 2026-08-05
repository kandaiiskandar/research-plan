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
| **East season** (Mar–Jun, wind-dominant) | Vigorous winds, heavy precipitation, but calm seas (~5 knots wind) | Restricted operations: 2–3 trips/week, 3–5 hours, near-shore only | **Delay** |
| **West season** (Nov–Feb) | Intense winds 30–40 knots, heavy precipitation, waves >2m | "Do not go at all" — dramatic curtailment of fishing activity | **AI off** (UNSAFE state; G(S) = 0) |

**Key quantitative evidence:**
- Trip frequency reduction from 5–6/week → 2–3/week under marginal conditions → **Delay** label
- Trip duration reduction from 7–10 hours → 3–5 hours under marginal conditions → **Delay** label  
- Near-shore operational shift under elevated wind → confirms CAUTION-state behavior
- Income drop from IDR 656K → 213K per trip under adverse conditions → risk is real and economic

The East season behavioral pattern — where fishers continue to sea but with restricted scope and near-shore operations — is the closest empirical analogue to the CAUTION state. The West season pattern — full halt — confirms the UNSAFE state threshold.

### 3.2 Gao (2024) [[notes]](../../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md)

**Study:** 25 semi-structured interviews, small-scale gill net fishers, Penang, Malaysia. Qualitative causal mapping methodology. M.Sc. thesis, CGIAR/WorldFish repository.

This study documents the tripartite decision structure used by Penang fishers and provides direct quotes that map to the three governance states:

| Decision type | Documented behavior | Mapped label |
|---|---|---|
| **Go** (favourable conditions) | Full operational scope: fishers decide timing, location, species, trip duration | **Go** |
| **Cautious-go** (marginal conditions) | Shortened trips, near-shore operations, heightened monitoring, location changes | **Delay** |
| **Don't go** (adverse conditions) | *"If the wind is too strong, I don't go"* — trips cancelled entirely | **AI off** (UNSAFE) |

**Environmental factor importance ratings from Penang fishers (1–5 scale):**
- Tide (ocean state, o): **4.55** — highest rated
- Fishing resource: **4.45**
- Previous catch: **4.38**
- Weather (wind, w): **3.75**
- Safety concern: **3.40**

The importance of weather and safety concern confirms that w and o are the primary go/no-go determinants. The documented informal tripartite classification (go / cautious-go / don't go) directly parallels the formal SAFE / CAUTION / UNSAFE states.

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

Combining the three studies, the label logic is as follows. Environmental conditions are expressed using MET Malaysia's Kawasan Perairan range bands and warning thresholds:

| Environmental conditions (E) | S | Study evidence | Label |
|---|---|---|---|
| Wind <22 knots, waves <1.5m, none/light rain, no warning | **SAFE** | Rahim fishing season; Gao "go" pattern | **Go** |
| Wind <22 knots, waves <1.5m, moderate rain, no warning | **SAFE** | Gao weather importance (3.75) — moderate rain, otherwise calm = still safe | **Go** |
| Wind 22–27 knots, waves 1.5–2.5m, none/light rain, no warning | **CAUTION** | Rahim East season — elevated wind, restricted operations | **Delay** |
| Wind 22–27 knots, waves 1.5–3.5m, moderate rain, no warning | **CAUTION** | Rahim East season + Yamin erratic rainfall | **Delay** |
| Wind 22–27 knots, waves <1.5m, heavy rain / thunderstorm | **CAUTION** | Yamin erratic rainfall as primary hazard; Ribut Petir approaching threshold | **Delay** |
| Wind >27 knots, waves >3.5m, any rain, Category 1+ warning | **UNSAFE** | Rahim West season "do not go at all"; Gao "if wind too strong, I don't go" | **AI off** |
| Any wind, any wave, Ribut Petir warning active | **UNSAFE** | Yamin: sudden weather change = can't go; Rahim: intense precipitation season = halt | **AI off** |
| Any wind, any wave, Ribut Taufan advisory active | **UNSAFE** | Tropical cyclone = unconditional halt | **AI off** |

**Value interpretation rule**: Upper bound of each MET range band is used (e.g., 10–20 km/h → treated as 20 km/h). This is consistent with the worst-case (max-severity) aggregation principle in the architecture.

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
