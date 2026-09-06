# Appendix C: Mathematical Formalisation of the Graduated Safety-State-Gated Architecture

## C.1 Environmental State Representation

Let the environmental–operational state be defined as a state vector:

**E = {w, r, m, o, v, t}**

Where:

- **w** = wind speed (knots, sustained)
- **r** = rainfall intensity (none, light, moderate, heavy, storm)
- **m** = marine warning level (none, advisory, warning, alert)
- **o** = ocean state (wave height m, swell period s)
- **v** = vessel category (small, medium, big), defined by gross registered tonnage
- **t** = time of day (hour, 24‑hour clock)

The environmental state represents the operational context used by the deterministic safety classification layer.

**Vessel category definition.** v is defined by gross registered tonnage following the Malaysian small boat classification of Yunus (2007), as reproduced by Yaakob et al. (2015) [[notes]](../../notes/Stability%2C%20Seakeeping%20and%20Safety%20Assessment%20of%20Small%20Fishing%20Boats%20Operating%20in%20Southern%20Coast%20of%20Peninsular%20Malaysia.md) Table 1:

| Category | GRT | Nominal LOA range | Operating zone |
|---|---|---|---|
| small | < 10 | 5.5–10.0 m | < 10 nm |
| medium | 10–25 | 7.5–15.0 m | < 30 nm |
| big | > 25 | 11.0–25.0 m | > 30 nm |

Tonnage is the discriminating variable because the LOA ranges in the source classification overlap (a 12 m vessel falls in both the medium and large LOA bands), whereas the tonnage bands are disjoint and exhaustive over ℝ≥0. This also aligns with how the surrounding corpus characterises the population: Yamin et al. (2025) describe Malaysian small-scale fishers as operating vessels below 40 GRT, and Jeong & Im (2023) report that 89% of Korean fishing vessel accidents involve vessels under 10 tons.

**Role of v in classification.** Unlike the five condition variables (w, r, m, o, t), v is a fixed attribute of the operator rather than a time-varying observation. It does not classify to a safety state independently. Instead it parameterises the ocean state classification function g_o(o, v) — see C.2. The rationale is given in the Vessel Category Classification Note below.

### Time of Day Classification Note

t ∈ [0, 24) is classified by the threshold function g_t(t) into three safety zones:

- **SAFE**: 06:00–17:00 (daytime — sufficient daylight for safe operation and return)
- **CAUTION**: 17:00–19:00 (approaching darkness — elevated visual risk)
- **UNSAFE**: 19:00–06:00 (night — insufficient daylight for safe small‑vessel operation)

The overall safety state **S = max‑severity(S_w, S_r, S_m, S_o, S_t)** applies the conservative worst‑case rule across all five condition classifications, including t. *(max‑severity is formally defined via the severity order in Definition C.1, Section C.2.)* Time of day is therefore a direct input to the governance classification, not a post‑hoc filter on recommendation types.

**Empirical justification for t.** The inclusion of t is grounded in two complementary empirical sources. Atacan & Düzbastılar (2023) conducted a bridge navigation simulator study with 30 small‑scale fishing vessel captains and found that night navigation significantly elevates both accident probability (mean 4.08 vs. 3.43 at calm conditions) and consequence (mean 12.80 vs. 8.53). Combined night and heavy weather produced the highest consequence scores across all tested conditions (mean 37.03). Restricted visibility — the principal mechanism by which nighttime elevates risk for small vessels without radar — was rated the single most dangerous factor for sea navigation accident probability (mean 7.90, the highest across all six environmental scenarios). Dominguez‑Péry et al. (2023) analysed 504 IMO maritime accident investigation reports (2011–2021) and found that external environmental factors including visibility constitute the largest single risk cluster (26.7% of text segments), with time of day captured as a standard field in IMO accident records. These findings establish that time of day is an empirically validated maritime risk factor, not an arbitrary addition to E.

### Vessel Category Classification Note

v ∈ {small, medium, big} classifies the fishing vessel by gross registered tonnage. Vessel category is a **conditioning parameter**, not an independent classifier: it is fixed for a given vessel and does not vary during a trip, unlike the dynamic condition variables (w, r, m, o, t). It enters the governance classification by parameterising the ocean state classification function — g_o(o, v) — rather than by contributing an independent per-component classification to the worst-case aggregation.

**Why v parameterises rather than votes.** The physical mechanism by which vessel size affects safety is that a given sea state produces categorically different hull response depending on vessel dimensions. This is a *conditional* effect: it determines the wave height at which conditions become dangerous for a particular vessel, not a fixed quantity of danger carried by the vessel in all conditions. Representing v as an independent classifier contributing a constant severity to a maximum cannot express this. A constant term in a max operation establishes a floor on the output; it cannot shift a threshold. Under such a formulation, vessel category would have no effect whatsoever on the CAUTION/UNSAFE boundary — a 5 m traditional boat and a 20 m vessel would be classified UNSAFE at identical wave heights, which contradicts the hydrodynamic evidence below. Parameterising g_o by v implements the conditional effect directly.

**Empirical justification for v.** The inclusion of vessel category is grounded in four independent lines of evidence.

*Hull response is vessel-specific.* Yaakob et al. (2015) [[notes]](../../notes/Stability%2C%20Seakeeping%20and%20Safety%20Assessment%20of%20Small%20Fishing%20Boats%20Operating%20in%20Southern%20Coast%20of%20Peninsular%20Malaysia.md), assessing two traditional Malaysian small fishing boats from the Johor coast using Maxsurf (JONSWAP spectrum, NORDFORSK 1987 criteria), established distinct operability limits by vessel size: the 6.54 m vessel remained within NORDFORSK limits to Sea State 3 (operational limit Hs ≈ 1.25 m) and failed at Sea State 4 (Hs ≈ 1.875 m), while the 5.03 m vessel remained within limits only to Sea State 2 (operational limit Hs ≈ 0.5 m) and failed at Sea State 3 (Hs ≈ 0.875 m). Both passed IMO static stability criteria at all loading conditions, establishing that dynamic seakeeping — not static stability — is the binding constraint, and that the binding wave height differs by vessel.

*Departure thresholds are length-dependent.* Jeong & Im (2023) [[notes]](../../notes/Proposal%20of%20Restrictions%20on%20the%20Departure%20of%20Korea%20Small%20Fishing%20Vessel%20according%20to%20Wave%20Height.md), analysing 66 capsizing incidents in Korean coastal waters over 23 years, derive a length-dependent departure restriction formula from the UK Wolfson Unit critical wave height framework (Hs_KIMO = √(1 + 0.4 × (0.88 × LOA)) − 1) producing thresholds from 1.13 m at 10 m LOA to 2.07 m at 24 m LOA, and propose a graduated management framework in which vessels ≤ 10 m are restricted at Hs ≥ 1.0 m and vessels ≤ 24 m at Hs ≥ 2.0 m. Their central finding — that 82% of 2017–2022 capsizing accidents occurred on days without any weather warning, and 38% at Hs ≤ 3 m — establishes that vessel-blind institutional thresholds systematically fail to capture small-vessel risk.

*Consequences are disproportionate at the small end.* Dominguez‑Péry et al. (2023) analysed 504 IMO maritime accident investigation reports (2011–2021) and found a statistically significant difference in deaths by vessel size (ANOVA, p = 0.01): small vessels had the highest mean rank for deaths (3.67), compared to large (1.02) and medium (0.85), despite comprising only 58 of 504 accidents. This is a consequence-severity finding rather than a probability finding, and it justifies setting small-vessel thresholds conservatively — a smaller vessel requires more margin because the outcome of misclassification is worse.

*The target population is at the small end.* Rahim et al. (2024) identify vessel capacity as a hard physical safety constraint for Indonesian small-scale fishers, with vessels under 10 GT unable to withstand severe weather. Shaffril et al. (2017) document Malaysian small-scale fishers operating vessels ≤ 22 feet within 5 nautical miles of shore, and Yamin et al. (2025), surveying 136 fishers in central Terengganu, confirm operation in the 0–5 nm zone with traditional vessels below 40 GRT. These establish that the deployment population sits predominantly in the small and medium tonnage bands, making vessel-conditional thresholds operationally consequential rather than a marginal refinement.

**Interaction with other parameters.** Vessel category shifts the effective safety boundary for ocean state: the same wave height classifies differently depending on v. Wind speed (w) is not vessel-parameterised in the current model, as no corpus source provides vessel-specific wind thresholds; this is recorded as a limitation in C.9. Marine warning level (m) is not vessel-parameterised because MET Malaysia warnings are institutional signals issued independently of who is at sea. Rainfall (r) and time of day (t) are likewise treated as vessel-independent.

### Worst‑Case Aggregation Justification Note

The overall safety state is determined by worst‑case (max‑severity) aggregation: S = max‑severity(S_w, S_r, S_m, S_o, S_t), where S_o = g_o(o, v) is itself conditioned on vessel category. Instead of averaging conditions or using a majority vote, the system's final safety state is dictated by whichever single condition is currently most dangerous. This produces three strict rules:

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

For each condition component xᵢ ∈ {w, r, m, o, t}, define a per-component classification function gᵢ → {SAFE, CAUTION, UNSAFE}. Four of these are single-argument functions of their condition variable; g_o is additionally parameterised by vessel category v. The overall classification function is then:

**f(E) = max-severity(g_w(w), g_r(r), g_m(m), g_o(o, v), g_t(t))**

where max-severity applies the severity order ≻ from Definition C.1 and returns the most severe classification across the five condition classifications.

Vessel category v does not appear as a separate argument to max-severity. It enters through g_o, shifting the wave height thresholds rather than contributing an independent severity term — see the Vessel Category Classification Note in C.1 for the rationale.

The per-component functions and their threshold values are defined below. Thresholds are anchored to MET Malaysia's published warning criteria, to peer-reviewed seakeeping and capsizing analyses for the vessel-conditional wave rows, and corroborated by empirical fisher departure decision patterns documented across three independent studies (Rahim et al. 2024; Gao 2024; Yamin et al. 2025).

*Cross-reference note (corrected 2026-09-06):* this section previously pointed to `docs/implementation/dataset-label-derivation.md` "for full derivation" of the thresholds. That document derives **training labels for the advisory AI (Layer 3)**, not the classifier thresholds — it consumes the thresholds defined here rather than deriving them. The threshold derivation is in this section and in the per-row empirical basis under g_o. The label-derivation document remains the correct reference for how the three fisher studies map to Go/Delay training labels.

**MET Malaysia source links (verified August 2026):**
- Strong Wind & Rough Seas Warning Criteria: https://www.met.gov.my/en/ramalan/angin-kencang-and-laut-bergelora/
- Thunderstorm Warning Criteria: https://www.met.gov.my/en/ramalan/ribut-petir/
- Live Marine Warning Bulletin: https://www.met.gov.my/data/IDM20016.html

---

**g_w(w) — Wind Speed (knots, sustained)**

| Classification | Threshold | Empirical basis |
|---|---|---|
| SAFE | w ≤ 22 knots | Full fishing operations observed; Rahim et al. fishing season (low winds) |
| CAUTION | 22 < w ≤ 27 knots | Restricted operations (2–3 trips/week, near-shore); Rahim et al. East season |
| UNSAFE | w > 27 knots | MET Malaysia Category 2 onset (50 km/h ≈ 27 kn). Corroborated by Gao: "if wind too strong, I don't go" |

*Note on `w` as sustained wind (added 2026-09-06).* `w` is defined as **sustained** wind speed, and the thresholds are MET Malaysia sustained-wind criteria. Care is needed when drawing on fisher-interview sources, which often report gusts: Rahim et al. (2024) [[notes]](../../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) describe West season as "wind **gusts** of 30 to 40 knots per hour," which at typical gust ratios implies roughly 19–31 kn sustained — straddling rather than clearly exceeding the 27 kn boundary. That paper's West season figure was previously cited here as direct support for the UNSAFE threshold; the citation has been removed, since the threshold rests on MET Malaysia criteria and the West season classification is more securely driven by wave height (> 2 m) than by wind. Any future empirical corroboration of `g_w` must confirm whether the source reports sustained or gust values.

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

**g_o(o, v) — Ocean State (wave height, metres), conditioned on vessel category**

g_o is a two-argument function: the wave height component of o, and the vessel category v. Thresholds shift by vessel category, reflecting that a given sea state produces different hull response depending on vessel size.

| v (GRT) | SAFE | CAUTION | UNSAFE |
|---|---|---|---|
| small (< 10) | o < 1.0 m | 1.0 ≤ o ≤ 1.9 m | o > 1.9 m |
| medium (10–25) | o < 1.4 m | 1.4 ≤ o ≤ 2.8 m | o > 2.8 m |
| big (> 25) | o < 1.5 m | 1.5 ≤ o ≤ 3.5 m | o > 3.5 m |

*Note on the tuple:* Ocean state o is a tuple (wave height m, swell period s) in the general definition (C.1). Classification depends only on the wave height component; swell period is retained in the state representation as a secondary modifier for domain instantiation but does not enter g_o. The thresholds use wave height as the governing variable, consistent with MET Malaysia's Kawasan Perairan range vocabulary.

**Empirical basis by row.**

*big (> 25 GRT) — unchanged from the prior vessel-independent definition.* The 1.5 m SAFE/CAUTION boundary is corroborated by Jeong & Im (2023) [[notes]](../../notes/Proposal%20of%20Restrictions%20on%20the%20Departure%20of%20Korea%20Small%20Fishing%20Vessel%20according%20to%20Wave%20Height.md), whose Hs_KIMO formula yields 1.58 m at 16 m LOA and 1.43 m at 14 m LOA — bracketing 1.5 m. The 3.5 m CAUTION/UNSAFE boundary aligns with MET Malaysia Category 1 maximum wave height criteria (https://www.met.gov.my/en/ramalan/angin-kencang-and-laut-bergelora/, verified August 2026).

*small (< 10 GRT).* The 1.0 m SAFE/CAUTION boundary is Jeong & Im's own proposed restriction for vessels ≤ 10 m LOA (their Table 12), independently corroborated by Yaakob et al. (2015) [[notes]](../../notes/Stability%2C%20Seakeeping%20and%20Safety%20Assessment%20of%20Small%20Fishing%20Boats%20Operating%20in%20Southern%20Coast%20of%20Peninsular%20Malaysia.md), whose 6.54 m Malaysian vessel had a NORDFORSK operational limit of Hs ≈ 1.25 m. The 1.9 m CAUTION/UNSAFE boundary corresponds to Sea State 4 (Hs ≈ 1.875 m), at which Yaakob's 6.54 m vessel failed NORDFORSK criteria on multiple parameters (RMS vertical acceleration at FP = 0.332 g against a 0.275 g limit; bridge = 0.195 g against 0.150 g). **Design decision:** treating NORDFORSK operability failure as the UNSAFE trigger is an interpretation of Yaakob et al.'s seakeeping results, not a claim the paper makes. The reasoning is that a sea state in which the crew cannot safely perform heavy manual work is one in which departure should not be advised at all. This is recorded as a threat to internal validity in C.9.

*medium (10–25 GRT).* The 1.4 m SAFE/CAUTION boundary derives from Hs_KIMO evaluated across the 10–15 m LOA range (1.13 m at 10 m, 1.48 m at 15 m). **Design decision:** the 2.8 m CAUTION/UNSAFE boundary is interpolated between the small and big rows, preserving an approximately proportional CAUTION band width. No corpus source provides a direct medium-vessel UNSAFE threshold. This is the weakest-grounded value in the table and is recorded as a threat to internal validity in C.9.

*Why vessel-blind thresholds fail.* Jeong & Im report that 82% of 2017–2022 Korean capsizing accidents occurred on days without any weather warning, and that 38% of all capsizing incidents occurred at Hs ≤ 3 m, including incidents at Hs as low as 1.0 m. A single vessel-independent threshold set therefore cannot be defended on the grounds that correlated parameters (high wind, issued marine warnings) will catch small-vessel risk in practice — the accident record shows they do not.

*Geographic limitation:* The Hs_KIMO formula was calibrated for Korean fishing vessel geometry; Malaysian traditional vessels may have different beam-to-length ratios. Yaakob et al. partially addresses this by studying actual Malaysian hulls, but with a sample of two. The formula provides empirical corroboration for the threshold ranges, not a direct numerical transfer.

*Domain:* g_o : (ℝ≥0 × ℝ≥0) × {small, medium, big} → {SAFE, CAUTION, UNSAFE}. For each fixed v, the three wave-height intervals partition ℝ≥0 exhaustively with no overlap; classification is independent of the swell period component. Since {small, medium, big} is finite and each row induces an exhaustive partition, g_o is total over its domain.

---

**Note: there is no g_v.**

Earlier versions of this formalisation defined a per-component classification function g_v(v) with codomain {SAFE, CAUTION} contributing an independent severity term to max-severity, such that v ∈ {small, medium} produced at minimum CAUTION regardless of conditions. That formulation is superseded.

The reason is structural. A constant term in a maximum establishes a floor on the output but cannot shift a threshold. Under the superseded definition, vessel category had no effect on the CAUTION/UNSAFE boundary: a vessel of any size classified UNSAFE at precisely the same wave height (3.5 m) and wind speed (27 knots). Yaakob et al. (2015) document that a 6.54 m Malaysian vessel exceeds NORDFORSK operability limits at Hs ≈ 1.875 m — 1.9 times below the threshold at which the superseded model would have classified it UNSAFE. The formulation therefore under-classified risk for exactly the vessels the architecture targets, across the 1.5–3.5 m band in which the CAUTION mode is intended to operate.

A secondary consequence: because g_v(small) = CAUTION held unconditionally, SAFE was unreachable for any vessel under 25 GRT. The deployment population is predominantly below 40 GRT (Yamin et al. 2025), so for real users the three-state architecture collapsed to two reachable states, rendering the strict containment A_AI(SAFE) ⊃ A_AI(CAUTION) — the architecture's principal claim — unobservable in the target domain.

Vessel category now enters through g_o(o, v) as documented above. The empirical sources previously cited in support of g_v (Dominguez-Péry et al. 2023; Rahim et al. 2024; Shaffril et al. 2017; Yamin et al. 2025) are retained in C.1, where they justify vessel-conditional threshold selection rather than an independent severity contribution.

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

**Proof.** It suffices to show that (i) each condition classification function is total over its domain, and (ii) max-severity is total over {SAFE, CAUTION, UNSAFE}⁵.

*(i) Totality of each classification function.*

- **g_w:** The thresholds [0, 22], (22, 27], (27, +∞) partition ℝ≥0 exhaustively. Every w ∈ ℝ≥0 falls in exactly one interval. ✓
- **g_r:** The five values {none, light, moderate, heavy, storm} are the complete domain of r. Each value is assigned to exactly one classification. ✓
- **g_m:** The four values {none, advisory, warning, alert} are the complete domain of m. Each value is assigned to exactly one classification. ✓
- **g_o:** g_o is two-argument, with domain (ℝ≥0 × ℝ≥0) × {small, medium, big}. Totality is established in two steps. First, for each fixed v ∈ {small, medium, big}, the corresponding row of the threshold table induces three intervals that partition ℝ≥0 exhaustively with no overlap — [0, 1.0), [1.0, 1.9], (1.9, +∞) for small; [0, 1.4), [1.4, 2.8], (2.8, +∞) for medium; [0, 1.5), [1.5, 3.5], (3.5, +∞) for big. Second, {small, medium, big} is finite and exhausts the domain of v, and classification does not depend on the swell period component of o, so every (o, v) pair falls under exactly one row and within exactly one interval of that row. ✓
- **g_t:** The intervals [6, 17), [17, 19), [19, 24) ∪ [0, 6) partition [0, 24) exhaustively. Every t ∈ [0, 24) falls in exactly one interval. ✓

*(ii) Totality of max-severity.*

max-severity takes a tuple (S_w, S_r, S_m, S_o, S_t) ∈ {SAFE, CAUTION, UNSAFE}⁵ and returns the element that is greatest under ≻ (Definition C.1). Since ≻ is a total strict order on a finite set, the maximum always exists and is unique. ✓

Therefore f(E) = max-severity(g_w(w), g_r(r), g_m(m), g_o(o, v), g_t(t)) is defined and returns exactly one element of {SAFE, CAUTION, UNSAFE} for all E. ∎

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

## C.9 Known Limitations of the Formal Model

The following are recorded as limitations of the current formalisation. Each is a design decision made in the absence of a directly applicable source, or a scope boundary accepted deliberately.

### C.9.1 Threshold grounding

**Small-vessel UNSAFE boundary (1.9 m).** Derived by treating NORDFORSK 1987 operability failure as the UNSAFE trigger. Yaakob et al. (2015) report that their 6.54 m vessel exceeded RMS vertical acceleration limits at Sea State 4 (Hs ≈ 1.875 m); the reasoning applied here is that a sea state in which the crew cannot safely perform heavy manual work is one in which departure should not be advised. Yaakob et al. do not themselves characterise this as a departure prohibition. The interpretation is defensible but is not a finding of the source.

**Medium-vessel UNSAFE boundary (2.8 m).** Interpolated between the small and big rows to preserve an approximately proportional CAUTION band width. No corpus source provides a medium-vessel UNSAFE threshold. This is the weakest-grounded value in the g_o table.

**Vessel category granularity.** Three tonnage bands are a coarse discretisation of a continuous relationship. Jeong & Im's Hs_KIMO formula is continuous in LOA; the architecture discretises to three categories for tractability and because vessel category is already a categorical field in the deployment context. A continuous formulation would be more precise but would require LOA rather than tonnage as the state variable.

**Sample size for Malaysian hull data.** Yaakob et al. study two vessels. The paper itself notes that "different design factor and different operating area may produce different results." The small-vessel thresholds rest on a sample of two Malaysian hulls plus a Korean formula calibrated on different vessel geometry.

### C.9.2 Parameters not vessel-conditioned

**Wind (g_w).** Wind thresholds are vessel-independent. A small vessel and a large vessel are classified identically at the same wind speed, despite the physical expectation that a 5–7 m hull with a 15 HP outboard cannot hold station in conditions a larger vessel tolerates. No corpus source provides vessel-specific wind thresholds. Wind-driven risk is partly captured indirectly through correlated wave height, but this is not a formal guarantee — and Jeong & Im's finding that 82% of capsizings occurred without an active weather warning indicates that correlation-based reasoning is unreliable in this domain. This is the most significant known gap in the classifier.

**Time of day (g_t).** Not vessel-conditioned. Yaakob et al. document that the studied vessels lacked navigation lights, which would plausibly justify tighter night thresholds for small vessels, but no source quantifies this.

**Marine warning (g_m) and rainfall (g_r).** Not vessel-conditioned by design. MET Malaysia warnings are institutional signals issued independently of vessel characteristics; conditioning them on v would misrepresent their nature.

### C.9.3 Scope boundaries

**Vessel compliance is out of scope.** Yaakob et al. found both studied vessels failing IMO/Torremolinos safety equipment requirements — missing survival craft, signals, fire extinguishers, and navigation lights. The classifier governs environmental safety state, not vessel certification. A vessel lacking required equipment carries elevated risk in all conditions, but encoding this in f(E) would conflate environmental classification with regulatory compliance. If advisory restriction on compliance grounds is desired, it belongs in a separate gate with its own justification.

**Tide is absent from E.** Gao (2024) [[notes]](../../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md), the only corpus study that ranks decision factors by importance, found Penang fishers rating **tide highest at 4.55/5** — above weather (3.75) and safety concern (3.40). Tide is not represented in E. It is a distinct phenomenon from ocean state `o`: tidal height is driven by lunar and solar forcing, whereas `o` captures wind- and swell-driven wave height. Tidal state affects harbour access, bar crossing, and grounding risk for shallow-draft vessels — safety-relevant mechanisms that the current model cannot express. Two other highly rated factors (fishing resource 4.45, previous catch 4.38) are also absent, but those are catch-productivity rather than safety factors, so their exclusion from a safety classifier is defensible; tide is less clearly so. Adding tide would require a `g_tide` classification function with thresholds grounded in local bathymetry and harbour depth, which no corpus source currently provides.

**Swell period is unused.** o is defined as a tuple (wave height, swell period), but g_o classifies on wave height alone. Encounter period relative to vessel natural roll period is a genuine determinant of seakeeping response, and its omission means the classifier cannot distinguish a short-period wind sea from a long-period swell at the same significant wave height. Retained in the state representation for future use.

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