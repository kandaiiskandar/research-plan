---
layout: document
---

# Appendix C: Mathematical Formalisation of the Graduated Safety-State-Gated Architecture

## C.1 Environmental State Representation

Let the environmental–operational state be defined as a state vector:

**E = {w, r, m, o, v, t}**

Where:

- **w** = wind condition (speed / strength, e.g., Beaufort scale or m/s)
- **r** = rainfall intensity (e.g., none, light, moderate, heavy)
- **m** = sea state (wave height / swell, e.g., calm, moderate, rough)
- **o** = official marine warning level (e.g., no warning, caution, danger / warning)
- **v** = vessel category (small, medium, big)
- **t** = time of day (hour, 24‑hour clock)

The environmental state represents the operational context used by the deterministic safety classification layer.

### Time of Day Classification Note

t ∈ [0, 24) is classified by the threshold function g_t(t) into three safety zones:

- **SAFE**: 06:00–17:00 (daytime — sufficient daylight for safe operation and return)
- **CAUTION**: 17:00–19:00 (approaching darkness — elevated visual risk)
- **UNSAFE**: 19:00–06:00 (night — insufficient daylight for safe small‑vessel operation)

The overall safety state **S = max‑severity(S_w, S_r, S_m, S_o, S_v, S_t)** applies the conservative worst‑case rule across all six parameters, including t. Time of day is therefore a direct input to the governance classification, not a post‑hoc filter on recommendation types.

**Empirical justification for t.** The inclusion of t is grounded in two complementary empirical sources. Atacan & Düzbastılar (2023) conducted a bridge navigation simulator study with 30 small‑scale fishing vessel captains and found that night navigation significantly elevates both accident probability (mean 4.08 vs. 3.43 at calm conditions) and consequence (mean 12.80 vs. 8.53). Combined night and heavy weather produced the highest consequence scores across all tested conditions (mean 37.03). Restricted visibility — the principal mechanism by which nighttime elevates risk for small vessels without radar — was rated the single most dangerous factor for sea navigation accident probability (mean 7.90, the highest across all six environmental scenarios). Dominguez‑Péry et al. (2023) analysed 504 IMO maritime accident investigation reports (2011–2021) and found that external environmental factors including visibility constitute the largest single risk cluster (26.7% of text segments), with time of day captured as a standard field in IMO accident records. These findings establish that time of day is an empirically validated maritime risk factor, not an arbitrary addition to E.

### Vessel Category Classification Note

v ∈ {small, medium, big} classifies the fishing vessel by size category. Vessel category is a contextual parameter — it is fixed for a given vessel and does not change during a trip, unlike the dynamic environmental parameters (w, r, m, o). It enters the governance classification because vessel size directly determines vulnerability to the same environmental conditions captured by the other five parameters.

**Empirical justification for v.** The inclusion of vessel category is grounded in three independent lines of evidence. First, Dominguez‑Péry et al. (2023) analysed 504 IMO maritime accident investigation reports (2011–2021) and found a statistically significant difference in deaths by vessel size (ANOVA, p = 0.01): small vessels (≤2,000 GT) had the highest mean rank for deaths (3.67), compared to large vessels (1.02) and medium vessels (0.85) — despite small vessels comprising only 58 of 504 accidents in the dataset. This establishes that vessel size is an empirically validated risk factor with disproportionate fatality consequences at the small end. Second, Rahim et al. (2024), studying small‑scale fishers in coastal Indonesia, identify vessel capacity as a hard physical safety constraint: vessels under 10 GT cannot withstand severe weather, making vessel size a direct determinant of the environmental conditions under which safe operation is possible. Third, Shaffril et al. (2017), characterising Malaysian small‑scale fishers, document that this population operates vessels ≤22 feet within 5 nautical miles of shore, establishing high vulnerability to environmental conditions and rapid environmental state transitions. Yamin et al. (2025), surveying 136 fishers in central Terengganu, confirm that Malaysian SSF are limited to the 0–5 nm zone with traditional vessels below 40 GRT. The convergence across these sources — an IMO global accident analysis, an Indonesian fisher survival study, and two Malaysian fisher characterisation studies — establishes vessel category as a cross‑nationally validated safety parameter, not an arbitrary addition to E.

**Interaction with other parameters.** Vessel category modulates the effective risk of other E vector components. A given wave height (o) or wind speed (w) poses categorically different physical danger to a small vessel than to a big one. In the worst‑case aggregation rule S = max‑severity(S_w, S_r, S_m, S_o, S_v, S_t), a small vessel classification shifts the overall state toward CAUTION or UNSAFE even when other parameters are favourable — reflecting the empirical finding that small‑vessel operations carry elevated baseline risk (Dominguez‑Péry et al., 2023).

### Worst‑Case Aggregation Justification Note

The overall safety state is determined by worst‑case (max‑severity) aggregation: S = max‑severity(S_w, S_r, S_m, S_o, S_v, S_t). Instead of averaging conditions or using a majority vote, the system's final safety state is dictated by whichever single parameter is currently in the most dangerous condition. This produces three strict rules:

- **UNSAFE dominance:** If even one parameter is classified as UNSAFE, the entire system state becomes UNSAFE, even if all other conditions are favourable.
- **CAUTION priority:** If no parameter is UNSAFE but at least one is classified as CAUTION, the overall state is CAUTION.
- **SAFE requirement:** The system is classified as SAFE only if every single parameter meets the SAFE criteria.

**Empirical justification for worst‑case aggregation.** The choice of max‑severity over averaging or weighted combination is grounded in five independent lines of evidence.

First, **risk factors are non‑compensatory**. Baxi (2026), developing the Comprehension‑Gated Agent Economy architecture, independently derives the same weakest‑link aggregation principle for a structurally analogous governance problem: k = min(g₁(CC), g₂(ER), g₃(AS)), where the overall tier is determined by the worst‑performing dimension. The explicit design principle is that "high scores on one dimension must not compensate for failures on another." The same logic applies to environmental parameters: calm seas cannot compensate for dangerous wind, and clear skies cannot compensate for nighttime visibility loss.

Second, **combined adverse factors are super‑additive**. Atacan & Düzbastılar (2023), studying risk perception among 30 small‑scale fishing vessel captains using a bridge navigation simulator, found that combined night and heavy weather produced consequence scores (mean 37.03) far exceeding night alone (mean 12.80) or heavy weather alone. The interaction between adverse parameters amplifies rather than averages risk. This means max‑severity is actually a *conservative lower bound* on actual combined risk — the true danger under multiple adverse conditions exceeds the worst individual parameter.

Third, **conservative over‑approximation is the standard in formal safety methods**. Corsi et al. (2024), implementing verification‑guided shielding for deep reinforcement learning, apply the principle that region overapproximation "may mark safe regions as unsafe, increasing shield activation but never compromising safety." Newcomb & Ochoa (2026), reviewing 46 formal methods studies for safety‑critical ML, confirm that sound over‑approximation — a computed set that provably contains every true output — is the standard safety guarantee. Max‑severity implements this principle at the classification level: it may over‑classify (producing false CAUTION or false UNSAFE) but never under‑classifies when any single parameter indicates danger.

Fourth, **conservative bias is standard safety engineering practice**. Perez‑Cerrolaza et al. (2024), surveying AI safety governance across automotive, avionics, railway, and industrial domains, document that safety mechanisms are calibrated to err on the side of restriction. They also observe that "excessive false alarms could lead to new system‑level hazards" — which is precisely why the three‑state architecture mitigates the over‑triggering cost of conservatism. With only two states (SAFE/UNSAFE), max‑severity would over‑trigger full AI blocking. With three states, max‑severity triggers CAUTION first, maintaining restricted‑but‑useful AI advisory capability rather than forcing a binary choice.

Fifth, **adverse environmental conditions degrade all information sources simultaneously**. Ryu & Han (2025), reviewing environment‑aware multi‑sensor fusion for maritime domain awareness, demonstrate that environmental conditions corrupt all maritime sensing modalities — SAR, optical, AIS, and RF — simultaneously under adverse conditions. A single degraded environmental parameter undermines the reliability of the entire information basis that any AI decision support system depends upon. This simultaneous degradation means that when one parameter signals danger, the AI's ability to generate reliable recommendations across *all* types is compromised — supporting worst‑case aggregation over averaging.

Additionally, Dominguez‑Péry et al. (2023) document contradictory findings across studies regarding individual environmental characteristics as risk predictors, confirming that no single variable is reliable in isolation. Multi‑variable agreement — all parameters at SAFE — is needed before full advisory scope is warranted. The SAFE requirement (all parameters must classify as SAFE) reflects this empirical finding.

---

## C.2 Safety State Classification Function

The deterministic safety layer maps the environmental state to a safety state:

**S = f(E)**

Where:

**S ∈ {SAFE, CAUTION, UNSAFE}**

An example rule‑based classification (illustrative, not exhaustive):


An example rule-based classification:

S =
- UNSAFE if m = Warning or w > w_max
- CAUTION if w_caution < w ≤ w_max
- SAFE otherwise


This example illustrates the classification logic using wind (w) and official warning level (o), which are the two most critical factors from the literature.  
In the full system, the function **f(E)** incorporates all variables in the environmental state vector **E** (including rainfall r, sea state m, vessel category v, and time of day t), with thresholds derived from Malaysian maritime safety data and expert elicitation during the design science research cycle.

---

## C.3 AI Participation Gate Function

The AI participation gate determines whether the Advisory AI Layer is allowed to operate:

**G(S) =**
- **0** if S = UNSAFE
- **1** if S ∈ {SAFE, CAUTION}

Where:
- G(S) = 0 → AI disabled  
- G(S) = 1 → AI enabled  

This gate controls AI participation, but it does not define the scope of AI recommendations.

---

## C.4 AI‑Admissible Recommendation Space

To formally represent advisory governance, define the AI‑admissible recommendation space:

**A_AI(S)**

Let the set of recommendation types be:

**R = {Go, Delay, DepartureTime, Duration}**

Where:
- **Go** = go / no‑go recommendation  
- **Delay** = recommendation to delay departure  
- **DepartureTime** = recommended departure window  
- **Duration** = recommended safe trip duration  

The AI‑admissible recommendation space is defined as:

A_AI(S) =
- {Go, Delay, DepartureTime, Duration} if S = SAFE
- {Go, Delay} if S = CAUTION
- ∅ if S = UNSAFE


This produces the containment relationship:

**A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅**

When S = CAUTION, the **Go** recommendation is automatically presented by the system with a caution qualifier (e.g., “Proceed with caution”). The recommendation type remains **Go**, but its presentation and explanation are modified by the safety state. This preserves set containment while allowing state‑dependent advisory messaging.

This restriction means that under CAUTION conditions, the AI cannot provide timing optimisation or trip duration recommendations.

---

## C.5 Two‑Level Governance Structure

The architecture implements a two‑level AI governance model controlled by environmental safety state.

### Level 1 – Participation Governance
Determines whether AI is allowed to operate: **G(S)**

### Level 2 – Advisory Scope Governance
Determines what the AI is allowed to recommend: **A_AI(S)**

Therefore, the AI decision system is governed by the pair:

**(G(S), A_AI(S))**

Environmental safety state therefore governs:

1. Whether AI participates  
2. What the AI is allowed to recommend  

This two‑level governance structure is the core architectural mechanism of the proposed system.

---

## C.6 Governance Constraints

The architecture must satisfy the following governance constraints.

### Participation Constraint
If the AI participation gate is closed, the AI recommendation space must be empty:

**G(S) = 0 ⇒ A_AI(S) = ∅**

This ensures deterministic safety constraints override AI advisory reasoning.

### Advisory Restriction Constraint
The CAUTION state must restrict AI advisory scope relative to SAFE:

**S = CAUTION ⇒ A_AI(CAUTION) ⊂ A_AI(SAFE)**

This ensures that CAUTION represents a restricted advisory mode rather than full AI operation.

---

## C.7 Safety Dominance Property

The Graduated Safety‑State‑Gated Architecture satisfies the **Safety Dominance Property** if deterministic safety classification always constrains AI recommendations.

Let **AI(E)** denote the set of recommendation types generated by the AI for environmental state **E**.

Then the Safety Dominance Property is defined as:

**For all E, if S = f(E), then:**
- **AI(E) ⊆ A_AI(S)**
- **If S = UNSAFE, then AI(E) = ∅**

This means the AI can only generate recommendations that belong to the admissible recommendation space defined by the safety state.

This property ensures that probabilistic AI reasoning cannot generate recommendations outside deterministic safety constraints.

---

## C.8 Formal Architecture Flow

The decision architecture can be summarised as the following formal pipeline:

**E → S = f(E) → (G(S), A_AI(S)) → AI(E)**

This represents the layered governance process:

1. Environmental state is observed  
2. Safety state is classified  
3. Governance rules determine AI participation and advisory scope  
4. AI generates recommendations within permitted scope  

---

## Summary of Formal Model Components

The formal architecture is defined by four core functions:

| Symbol | Meaning |
|--------|---------|
| **E** | Environmental state |
| **S = f(E)** | Safety classification |
| **G(S)** | AI participation gate |
| **A_AI(S)** | AI admissible recommendation space |

These four functions together define the **Graduated Safety‑State‑Gated Hybrid AI Decision Architecture**.

---

## Conceptual Structure of the Architecture Governance Model

The formal architecture defines the governance mechanism that controls AI participation and advisory scope using environmental safety state.

The architecture is governed by the following sequence:

**E → S = f(E) → (G(S), A_AI(S)) → AI(E)**

Where:
- **E** = Environmental–operational state
- **S** = Safety state
- **G(S)** = AI participation gate
- **A_AI(S)** = AI‑admissible recommendation space
- **AI(E)** = AI‑generated recommendations

In this architecture:

1. The environmental state is observed.
2. The deterministic safety layer classifies the safety state.
3. The safety state controls whether AI is allowed to operate.
4. The safety state controls what the AI is allowed to recommend.
5. The AI generates recommendations within the permitted advisory scope.
6. The human operator makes the final decision.

This structure represents a state‑governed hybrid AI decision architecture where deterministic safety classification governs probabilistic AI advisory behaviour.

---

## Formal Contribution of the Architecture

The formal contribution of this research is the definition of a safety‑state‑governed AI decision architecture using a two‑level governance mechanism.

The architecture is formally defined by the governance pair:

**(G(S), A_AI(S))**

Where:
- **G(S)** determines whether the AI is allowed to participate.
- **A_AI(S)** determines the set of recommendation types the AI is allowed to generate.

The architecture must satisfy the following governance properties:

1. **Participation Constraint**  
   If G(S) = 0, then A_AI(S) = ∅.

2. **Advisory Restriction Constraint**  
   A_AI(CAUTION) ⊂ A_AI(SAFE).

3. **Safety Dominance Property**  
   AI(E) ⊆ A_AI(S).

These properties ensure that deterministic safety classification always constrains AI participation and advisory behaviour.

Therefore, the proposed contribution is **not** a new AI prediction model, but a **governance architecture** that formally constrains how AI participates in decision‑making under different safety states. The architecture ensures that AI operates within a safety‑governed advisory space and cannot generate recommendations outside deterministic safety constraints.