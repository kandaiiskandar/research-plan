# Appendix C: Mathematical Formalisation of the Graduated Safety-State-Gated Architecture

## C.1 Environmental State Representation

Let the environmental–operational state be defined as a state vector:

**E = {w, r, m, o, v, t}**

Where:

- **w** = wind speed (knots, sustained)
- **r** = rainfall intensity (none, light, moderate, heavy, storm)
- **m** = marine warning level (none, advisory, warning, alert)
- **o** = ocean state (wave height m, swell period s)
- **v** = vessel category (small, medium, big)
- **t** = time of day (hour, 24‑hour clock)

The environmental state represents the operational context used by the deterministic safety classification layer.

### Time of Day Classification Note

t ∈ [0, 24) is classified by the threshold function g_t(t) into three safety zones:

- **SAFE**: 06:00–17:00 (daytime — sufficient daylight for safe operation and return)
- **CAUTION**: 17:00–19:00 (approaching darkness — elevated visual risk)
- **UNSAFE**: 19:00–06:00 (night — insufficient daylight for safe small‑vessel operation)

The overall safety state **S = max‑severity(S_w, S_r, S_m, S_o, S_v, S_t)** applies the conservative worst‑case rule across all six parameters, including t. *(max‑severity is formally defined via the severity order in Definition C.1, Section C.2.)* Time of day is therefore a direct input to the governance classification, not a post‑hoc filter on recommendation types.

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

### Definition C.1 — Severity Order

Define a total strict order ≻ on the safety state set {SAFE, CAUTION, UNSAFE} as:

**UNSAFE ≻ CAUTION ≻ SAFE**

This order is transitive (UNSAFE ≻ SAFE follows from UNSAFE ≻ CAUTION and CAUTION ≻ SAFE) and total (every pair of distinct states is ordered). The ordering reflects increasing operational risk: UNSAFE represents conditions in which departure is not survivable for the vessel category and no AI advisory output is permissible; CAUTION represents marginal conditions in which AI advisory output is restricted to coarse operational guidance; SAFE represents conditions in which all environmental parameters are within acceptable bounds and full AI advisory scope is available.

The empirical basis for this ordering is established in C.1: Atacan & Düzbastılar (2023) document that combined adverse conditions produce consequence scores that far exceed any single adverse factor (mean 37.03 for combined night and heavy weather vs. 12.80 for night alone), establishing that UNSAFE is strictly more dangerous than CAUTION. Dominguez‑Péry et al. (2023) confirm that multi-variable adverse conditions constitute the highest risk cluster across 504 IMO accident reports, establishing that SAFE (all parameters within bounds) is strictly less dangerous than CAUTION (at least one parameter elevated).

This definition is the formal basis for the worst‑case aggregation rule in the classification function and for Theorem C.2 (Monotonicity of A_AI) in C.6.

---

The deterministic safety layer maps the environmental state to a safety state:

**S = f(E)**

Where:

**S ∈ {SAFE, CAUTION, UNSAFE}**

### Per-Component Classification Functions

For each component xᵢ ∈ E, define a per-component classification function gᵢ : domain(xᵢ) → {SAFE, CAUTION, UNSAFE}. The overall classification function is then:

**f(E) = max-severity(g_w(w), g_r(r), g_m(m), g_o(o), g_v(v), g_t(t))**

where max-severity applies the severity order ≻ from Definition C.1 and returns the most severe classification across all six components.

The per-component functions and their threshold values are defined below. Thresholds are anchored to MET Malaysia's published Kawasan Perairan warning criteria and empirical fisher departure decision patterns documented across three independent studies (Rahim et al. 2024; Gao 2024; Yamin et al. 2025) — see `docs/implementation/dataset-label-derivation.md` for full derivation.

---

**g_w(w) — Wind Speed (knots, sustained)**

| Classification | Threshold | Empirical basis |
|---|---|---|
| SAFE | w ≤ 22 knots | Full fishing operations observed; Rahim et al. fishing season (low winds) |
| CAUTION | 22 < w ≤ 27 knots | Restricted operations (2–3 trips/week, near-shore); Rahim et al. East season |
| UNSAFE | w > 27 knots | "Do not go at all" — Rahim et al. West season (30–40 knots); Gao: "if wind too strong, I don't go" |

*Domain:* w ∈ ℝ≥0. The three intervals [0, 22], (22, 27], (27, +∞) partition ℝ≥0 exhaustively with no overlap.

---

**g_r(r) — Rainfall Intensity (ordinal categorical)**

| Classification | Values of r | Empirical basis |
|---|---|---|
| SAFE | {none, light, moderate} | Normal operations documented under none/light rain; moderate rain alone does not trigger restriction |
| CAUTION | {heavy} | Yamin et al.: erratic/heavy rainfall rated primary hazard by 91% of fishers; triggers restricted operations |
| UNSAFE | {storm} | Ribut Petir (thunderstorm warning) or Ribut Taufan (cyclone) — unconditional halt in all three studies |

*Domain:* r ∈ {none, light, moderate, heavy, storm}. All five values are assigned; the domain is fully covered.

---

**g_m(m) — Marine Warning Level (ordinal categorical)**

| Classification | Values of m | Empirical basis |
|---|---|---|
| SAFE | {none} | No active warning — baseline operating condition |
| CAUTION | {advisory} | Category 1 advisory — approaching warning threshold; signals elevated risk without full restriction |
| UNSAFE | {warning, alert} | Category 2–3 warning, Ribut Petir, or Ribut Taufan — MET Malaysia institutional halt threshold |

*Domain:* m ∈ {none, advisory, warning, alert}. All four values are assigned; the domain is fully covered.

---

**g_o(o) — Ocean State (wave height, metres)**

| Classification | Threshold | Empirical basis |
|---|---|---|
| SAFE | o < 1.5m | Calm/mild swell — full operations; Rahim et al. fishing season |
| CAUTION | 1.5m ≤ o ≤ 3.5m | Moderate swell — restricted scope; Rahim et al. East season (elevated waves, near-shore shift) |
| UNSAFE | o > 3.5m | Rough seas — Rahim et al. West season (waves >2m combined with 30–40 knot winds = halt) |

*Note:* Ocean state o is a tuple (wave height m, swell period s) in the general definition (C.1). For classification purposes, wave height is the primary component; swell period is a secondary modifier applied during domain instantiation. The threshold values above use wave height as the governing variable, consistent with MET Malaysia's Kawasan Perairan range vocabulary.

*Domain:* o (wave height component) ∈ ℝ≥0. The three intervals [0, 1.5), [1.5, 3.5], (3.5, +∞) partition ℝ≥0 exhaustively.

---

**g_v(v) — Vessel Category (ordinal categorical)**

| Classification | Values of v | Empirical basis |
|---|---|---|
| SAFE | {big} | Large vessels have lowest mean fatality rank (1.02); withstand adverse conditions that would restrict small vessels |
| CAUTION | {small, medium} | Small vessels: highest mean fatality rank (3.67, p = 0.01) per Dominguez-Péry et al. (2023); cannot withstand severe weather (Rahim et al. 2024); vessels ≤22 ft within 5 nm shore (Shaffril et al. 2017; Yamin et al. 2025). Medium vessels: intermediate vulnerability. |

*Note on UNSAFE:* g_v has no UNSAFE classification. Vessel category alone does not trigger UNSAFE — that state requires an environmental condition (e.g., extreme wind or an active marine warning) that is beyond the vessel's physical limits. The codomain of g_v is therefore {SAFE, CAUTION} ⊂ {SAFE, CAUTION, UNSAFE}. This is consistent with the totality requirement (Theorem C.1): every v maps to exactly one classification within {SAFE, CAUTION, UNSAFE}, and the absence of an UNSAFE row simply means no value of v maps to UNSAFE in isolation. The UNSAFE state for small and medium vessels arises through max-severity when g_v(v) = CAUTION combines with UNSAFE classifications from other components (e.g., g_w(w) = UNSAFE when w > 27 knots).

*Note on interaction:* Vessel category contributes at minimum CAUTION to max-severity when v ∈ {small, medium}. This reflects the empirical finding that small and medium vessels carry elevated baseline risk regardless of other environmental conditions. In practice, the vessel category threshold shifts the effective safety boundary for w, o, and m: conditions classified as SAFE for a big vessel may classify as CAUTION or UNSAFE for a small vessel through the max-severity rule.

*Domain:* v ∈ {small, medium, big}. All three values are assigned to exactly one classification; the domain is fully covered.

---

**g_t(t) — Time of Day (hour, 24-hour clock)**

| Classification | Threshold | Empirical basis |
|---|---|---|
| SAFE | 06:00 ≤ t < 17:00 | Daytime — sufficient daylight for safe operation and return to port |
| CAUTION | 17:00 ≤ t < 19:00 | Approaching darkness — elevated visual risk; restricted visibility onset |
| UNSAFE | 19:00 ≤ t < 24:00 or 00:00 ≤ t < 06:00 | Night — restricted visibility; Atacan & Düzbastılar (2023): highest accident probability and consequence scores under night conditions |

*Domain:* t ∈ [0, 24). The three intervals [6, 17), [17, 19), [19, 24) ∪ [0, 6) partition [0, 24) exhaustively.

---

### Theorem C.1 — Totality of f

**Theorem C.1 (Totality of f).** For all E ∈ domain(E), f(E) is defined and returns exactly one element of {SAFE, CAUTION, UNSAFE}.

**Proof.** It suffices to show that (i) each per-component function gᵢ is total over domain(xᵢ), and (ii) max-severity is total over {SAFE, CAUTION, UNSAFE}⁶.

*(i) Totality of each gᵢ.*

- **g_w:** The thresholds [0, 22], (22, 27], (27, +∞) partition ℝ≥0 exhaustively. Every w ∈ ℝ≥0 falls in exactly one interval. ✓
- **g_r:** The five values {none, light, moderate, heavy, storm} are the complete domain of r. Each value is assigned to exactly one classification. ✓
- **g_m:** The four values {none, advisory, warning, alert} are the complete domain of m. Each value is assigned to exactly one classification. ✓
- **g_o:** The thresholds [0, 1.5), [1.5, 3.5], (3.5, +∞) partition ℝ≥0 exhaustively (wave height component). Every o ∈ ℝ≥0 falls in exactly one interval. ✓
- **g_v:** The three values {small, medium, big} are the complete domain of v. Each value is assigned to exactly one classification. ✓
- **g_t:** The intervals [6, 17), [17, 19), [19, 24) ∪ [0, 6) partition [0, 24) exhaustively. Every t ∈ [0, 24) falls in exactly one interval. ✓

*(ii) Totality of max-severity.*

max-severity takes a tuple (S_w, S_r, S_m, S_o, S_v, S_t) ∈ {SAFE, CAUTION, UNSAFE}⁶ and returns the element that is greatest under ≻ (Definition C.1). Since ≻ is a total strict order on a finite set, the maximum always exists and is unique. ✓

Therefore f(E) = max-severity(g_w(w), g_r(r), g_m(m), g_o(o), g_v(v), g_t(t)) is defined and returns exactly one element of {SAFE, CAUTION, UNSAFE} for all E. ∎

**Significance.** Theorem C.1 establishes that the safety classifier has no undefined states — every combination of environmental conditions maps to exactly one safety state. This is a necessary condition for runtime governance: a classifier that could fail to return a state would leave the governance layer without a basis for enforcing (G(S), A_AI(S)).

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

### Theorem C.2 — Monotonicity of A_AI

Formal safety architectures require that safety constraints tighten consistently as risk increases — a property Bloomfield & Rushby (2025) [[notes]](../../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md) establish as a core expectation of deterministic guards surrounding AI components, and that Dalrymple et al. (2024) [[notes]](../../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md) require of world model safety specifications under increasing uncertainty. The following theorem proves that the proposed architecture satisfies this property.

**Theorem C.2 (Monotonicity of A_AI).** For all S₁, S₂ ∈ {SAFE, CAUTION, UNSAFE}, if S₁ ≻ S₂ then A_AI(S₁) ⊆ A_AI(S₂).

*Informally:* as the safety state becomes more severe, the AI admissible recommendation space never expands — it either contracts or remains equal.

**Proof.** From Definition C.1, the severity order ≻ on {SAFE, CAUTION, UNSAFE} yields three ordered pairs: (UNSAFE, CAUTION), (CAUTION, SAFE), and (UNSAFE, SAFE). We verify each case using the set definitions from C.4.

**Case 1: S₁ = UNSAFE, S₂ = CAUTION (UNSAFE ≻ CAUTION).**

A_AI(UNSAFE) = ∅ and A_AI(CAUTION) = {Go, Delay}.

∅ ⊆ {Go, Delay} holds trivially, since the empty set is a subset of every set.

Therefore A_AI(UNSAFE) ⊆ A_AI(CAUTION). ∎

**Case 2: S₁ = CAUTION, S₂ = SAFE (CAUTION ≻ SAFE).**

A_AI(CAUTION) = {Go, Delay} and A_AI(SAFE) = {Go, Delay, DepartureTime, Duration}.

{Go, Delay} ⊆ {Go, Delay, DepartureTime, Duration} holds because every element of A_AI(CAUTION) is also an element of A_AI(SAFE).

Therefore A_AI(CAUTION) ⊆ A_AI(SAFE). ∎

**Case 3: S₁ = UNSAFE, S₂ = SAFE (UNSAFE ≻ SAFE, by transitivity of ≻).**

A_AI(UNSAFE) = ∅ and A_AI(SAFE) = {Go, Delay, DepartureTime, Duration}.

∅ ⊆ {Go, Delay, DepartureTime, Duration} holds trivially.

Therefore A_AI(UNSAFE) ⊆ A_AI(SAFE). ∎

All three ordered pairs satisfy the subset condition. The theorem holds. ∎

**Corollary C.2 (Strict Monotonicity).** The inclusions in Cases 1 and 2 are strict: A_AI(UNSAFE) ⊊ A_AI(CAUTION) ⊊ A_AI(SAFE). This is precisely the containment relationship stated in C.4: A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅. Theorem C.2 provides the formal proof that this containment is not coincidental but follows necessarily from the severity ordering on S and the set definitions of A_AI(S).

**Significance.** Theorem C.2 guarantees that the architecture is well-behaved across state transitions. As environmental conditions deteriorate (S moves up the severity order), the AI advisory scope never suddenly expands. The Safety Dominance Property (C.7) establishes that AI output is bounded at any single state; Theorem C.2 establishes that this bound tightens monotonically as risk increases. Together they characterise the full safety behaviour of the governance pair (G(S), A_AI(S)).

---

## C.7 Safety Dominance Property

The Graduated Safety‑State‑Gated Architecture satisfies the **Safety Dominance Property** if deterministic safety classification always constrains AI recommendations.

Let **AI(E)** denote the set of recommendation types generated by the AI for environmental state **E**.

Then the Safety Dominance Property is defined as:

**For all E, if S = f(E), then:**
- **AI(E) ⊆ A_AI(S)**
- **If S = UNSAFE, then AI(E) = ∅**

This means the AI can only generate recommendations that belong to the admissible recommendation space defined by the safety state.

### C.7.1 Enforcement mechanism

The Layer 3 advisory component is implemented as a rule-based engine. The governance layer (Layer 2) supplies a rule set RS(S) to Layer 3 before any reasoning begins:

- **RS(SAFE)** = rules producing recommendations in {Go, Delay, DepartureTime, Duration}
- **RS(CAUTION)** = rules producing recommendations in {Go, Delay}
- **RS(UNSAFE)** = ∅ (never passed — G(UNSAFE) = 0, so Layer 3 receives no input)

The rule engine fires only rules present in the active RS(S). No rule in RS(CAUTION) produces DepartureTime or Duration, so those types cannot appear in AI(E) when S = CAUTION. The constraint is structural — it holds before generation begins, not by filtering outputs after the fact.

### C.7.2 Proof of the Safety Dominance Property

**Theorem C.3 (Safety Dominance Property).** Let AI(E) denote the set of recommendation types generated by the AI reasoning engine for environmental state E, and let S = f(E) be the safety state returned by the classifier. Then:

**For all E ∈ domain(E): AI(E) ⊆ A_AI(f(E))**

and as a special case:

**If f(E) = UNSAFE, then AI(E) = ∅**

**Assumptions.**

1. **(A1) Rule-based engine.** Layer 3 is implemented as a rule-based symbolic reasoning engine. It generates only recommendation types for which an active rule exists in its current rule set.

2. **(A2) Rule set supply.** The governance layer (Layer 2) supplies rule set RS(S) to Layer 3 before any reasoning begins, where RS(S) is defined as:
   - RS(SAFE) contains only rules producing recommendations in {Go, Delay, DepartureTime, Duration}
   - RS(CAUTION) contains only rules producing recommendations in {Go, Delay}
   - RS(UNSAFE) = ∅ — never supplied, since G(UNSAFE) = 0 gates off Layer 3 entirely

3. **(A3) Gate enforcement.** If G(S) = 0, Layer 3 receives no input and produces no output: AI(E) = ∅.

4. **(A4) Engine fidelity.** The rule engine fires only rules present in the active RS(S). No rule produces a recommendation type not present in the rule's conclusion.

**Proof by exhaustive case analysis on S.**

Since f(E) is total (Theorem C.1) and S ∈ {SAFE, CAUTION, UNSAFE}, there are exactly three cases.

**Case 1: f(E) = UNSAFE.**

By (A3), G(UNSAFE) = 0, so Layer 3 receives no input.
By (A3), AI(E) = ∅.
By definition, A_AI(UNSAFE) = ∅.
Therefore AI(E) = ∅ = A_AI(UNSAFE), and in particular AI(E) ⊆ A_AI(UNSAFE). ∎

**Case 2: f(E) = CAUTION.**

By (A3), G(CAUTION) = 1, so Layer 3 is active.
By (A2), Layer 3 receives RS(CAUTION), which contains only rules producing recommendations in {Go, Delay}.
By (A4), the engine produces only recommendation types present in RS(CAUTION).
Therefore AI(E) ⊆ {Go, Delay} = A_AI(CAUTION). ∎

**Case 3: f(E) = SAFE.**

By (A3), G(SAFE) = 1, so Layer 3 is active.
By (A2), Layer 3 receives RS(SAFE), which contains only rules producing recommendations in {Go, Delay, DepartureTime, Duration}.
By (A4), the engine produces only recommendation types present in RS(SAFE).
Therefore AI(E) ⊆ {Go, Delay, DepartureTime, Duration} = A_AI(SAFE). ∎

In all three cases, AI(E) ⊆ A_AI(f(E)). The Safety Dominance Property holds. ∎

**Remarks.**

- The proof is constructive: it depends only on the definitions of RS(S) and the gate function G(S), both of which are fully under the designer's control. No runtime checking is required.
- The property holds *before* generation begins, not by filtering outputs after the fact. RS(S) is supplied to Layer 3 as a precondition; the engine has no mechanism to generate types outside its active rule set.
- Together with Theorem C.2 (Monotonicity), this theorem characterises the full safety behaviour of the governance pair: at any given state, AI output is bounded within A_AI(S); as S becomes more severe, that bound tightens.

See `docs/canonical/justification-layer3-enforcement.md` for the full enforcement justification and design rationale for the rule set supply mechanism.

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

These four functions together define the **Graduated Safety‑State‑Gated Architecture**.

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

This structure represents a state‑governed architecture where deterministic safety classification governs symbolic AI advisory behaviour.

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