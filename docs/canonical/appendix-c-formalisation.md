# Appendix C: Mathematical Formalisation of the Graduated Safety-State-Gated Architecture

## C.1 Environmental State Representation

Let the environmental–operational state be defined as a state vector. *Notation: E is written as an ordered tuple rather than a set — its components are named, typed and positional, and `{...}` would wrongly imply an unordered collection. Corrected 2026-09-08.*


**E = (w, r, m, o, v, t)**

Where:

- **w** = wind speed (knots, sustained)
- **r** = rainfall intensity (mm/hr), r ∈ ℝ≥0
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

t is classified by `g_t(t, date)` into **two** governance zones *(SDR-001 applied 2026-09-08)*:

- **SAFE**: sunrise(date) ≤ t < sunset(date) — daytime operating condition; full AI advisory scope admissible
- **UNSAFE**: otherwise, and for t = ⊥ — night-time operating condition; AI advisory participation withdrawn

**`g_t` is deliberately binary and emits no CAUTION** (C.2). The architecture remains three-state: `𝒮 = {SAFE, CAUTION, UNSAFE}`, with CAUTION reached through `g_o` and `g_r`. **Superseded 2026-09-08:** the fixed clock 06:00 / 17:00 / 19:00, whose boundaries had no located source and whose 17:00–19:00 CAUTION band no source supported.

*Wording revised 2026-09-08 (pre-adoption semantic cleanup).* These rows previously read "sufficient daylight for safe operation and return" and "night — **insufficient daylight for safe small-vessel operation**". The second was an unsupported physical-safety claim: Atacan & Düzbastılar establish that night navigation carries *elevated* accident probability and consequence, not that it is unsafe or infeasible, and small-scale fishers demonstrably operate at night. Per Definition C.1, the rows now name the **operating condition** and the **governance response**, which is what the classifier actually determines. **That cleanup was wording-only and left the incumbent 06:00 / 17:00 / 19:00 thresholds in place; later the same day SDR-001 superseded them with the astronomical sunrise/sunset boundaries stated above. The fixed-clock thresholds are not canonical.** *(Chronology corrected 2026-09-09: this sentence previously ended "The thresholds 06:00 / 17:00 / 19:00 are unchanged", which was true of the cleanup at the moment it was written and became misleading once SDR-001 was applied.)*

**The governance response here is policy, not a finding.** The evidence establishes elevated night-time risk; it does not establish that AI advisory participation must be withdrawn at any particular hour. That withdrawal is an architectural governance choice and remains one under SDR-001: COLREGs Rule 20(b) supplies the sunset-to-sunrise boundary **for navigation lights**, and **no source establishes that AI advisory participation must be withdrawn there**. *(Corrected 2026-09-09: this sentence previously read "the boundaries themselves have no located source", which described the superseded 06:00 / 17:00 / 19:00 values. That defect is what SDR-001 resolved; read against the canonical astronomical boundaries the claim was false. What has no source is the **policy**, not the boundary.)* See `finding-gt-provenance-audit.md` and C.9.1.

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

Second, **combined adverse factors are super‑additive**. Atacan & Düzbastılar (2023), studying risk perception among 30 small‑scale fishing vessel captains using a bridge navigation simulator, found that combined night and heavy weather produced consequence scores (mean 37.03) far exceeding night alone (mean 12.80) or heavy weather alone. The interaction between adverse parameters amplifies rather than averages risk. This is empirical evidence that the true danger under multiple adverse conditions exceeds that of the worst individual parameter, and therefore that max‑severity does not *overstate* risk in the multi-parameter case. **It is not a formal lower-bound property.** Establishing that f(E) bounds actual risk from below would require a quantified risk model with a measurement scale on which 'combined risk' and 'the classification' are comparable; no such model exists here, and none of the cited sources supplies one. The claim is directional, not metric.

Third, **conservative over‑approximation is the standard in formal safety methods**. Corsi et al. (2024), implementing verification‑guided shielding for deep reinforcement learning, apply the principle that region overapproximation "may mark safe regions as unsafe, increasing shield activation but never compromising safety." Newcomb & Ochoa (2026), reviewing 46 formal methods studies for safety‑critical ML, confirm that sound over‑approximation — a computed set that provably contains every true output — is the standard safety guarantee. Max‑severity implements this principle at the classification level: it may over‑classify (producing false CAUTION or false UNSAFE), and **it cannot under-classify relative to its own component functions** — if any gᵢ returns UNSAFE then S = UNSAFE, in both forms. *This is a property of the aggregation operator, not of the system's correspondence to reality.* Under-classification remains possible through any of three routes the operator cannot address: a threshold set too high, a parameter absent from E, or a measurement that is missing, stale or wrong. `g_m` held at `none` throughout the replay (F-11, C.9) is a live instance of the second and third.

Fourth, **conservative bias is standard safety engineering practice**. Perez‑Cerrolaza et al. (2024), surveying AI safety governance across automotive, avionics, railway, and industrial domains, document that safety mechanisms are calibrated to err on the side of restriction. They also observe that "excessive false alarms could lead to new system‑level hazards" — which is precisely why the three‑state architecture mitigates the over‑triggering cost of conservatism. With only two states (SAFE/UNSAFE), max‑severity would over‑trigger full AI blocking. With three states, max‑severity triggers CAUTION first, maintaining restricted‑but‑useful AI advisory capability rather than forcing a binary choice.

Fifth, **adverse environmental conditions degrade all information sources simultaneously**. Ryu & Han (2025), reviewing environment‑aware multi‑sensor fusion for maritime domain awareness, demonstrate that environmental conditions corrupt all maritime sensing modalities — SAR, optical, AIS, and RF — simultaneously under adverse conditions. A single degraded environmental parameter undermines the reliability of the entire information basis that any AI decision support system depends upon. This simultaneous degradation means that when one parameter signals danger, the AI's ability to generate reliable recommendations across *all* types is compromised — supporting worst‑case aggregation over averaging.

Additionally, Dominguez‑Péry et al. (2023) document contradictory findings across studies regarding individual environmental characteristics as risk predictors, confirming that no single variable is reliable in isolation. Multi‑variable agreement — all parameters at SAFE — is needed before full advisory scope is warranted. The SAFE requirement (all parameters must classify as SAFE) reflects this empirical finding.

---

## C.2 Safety State Classification Function

### Definition C.1 — Severity Order

Define a total strict order ≻ on the safety state set {SAFE, CAUTION, UNSAFE} as:

**UNSAFE ≻ CAUTION ≻ SAFE**

This order is transitive (UNSAFE ≻ SAFE follows from UNSAFE ≻ CAUTION and CAUTION ≻ SAFE) and total (every pair of distinct states is ordered).

**The three states are defined by the governance configuration each selects, not by a claim about the physical world.** The ordering ranks them by how far AI advisory participation is withdrawn:

| State | Definition |
|---|---|
| **SAFE** | The governance state in which **full AI advisory participation is admissible**: G(S) = 1 and A_AI(S) = R |
| **CAUTION** | The governance state in which **AI advisory participation is admissible but restricted** to coarse operational guidance: G(S) = 1 and A_AI(S) ⊊ R |
| **UNSAFE** | The governance state in which **AI advisory participation is not admissible**: G(S) = 0 and A_AI(S) = ∅ |

*Revised 2026-09-08 (pre-adoption semantic cleanup).* The previous wording defined UNSAFE as "conditions in which departure lies outside the demonstrated operating envelope for the vessel category **and** no AI advisory output is permissible" — a conjunction that made an envelope claim about the world *constitutive* of the state. It is not. Envelope exceedance is one **reason** a component classifier may return UNSAFE, not part of what UNSAFE means. The prior wording also contradicted C.9.4, which states that the ordering "reflects operating envelopes, not survivability". Both now say the same thing. **The mathematical consequences are unchanged: G(UNSAFE) = 0 (C.3) and A_AI(UNSAFE) = ∅ (C.4) are exactly as before.**

#### How UNSAFE is reached

S = UNSAFE is produced by max-severity whenever any component classifier returns UNSAFE. Three routes exist and can coexist. The state itself does not record them; the provenance reason set in C.2.0.8 distinguishes fault, hazard, policy and their combinations:

1. **Environmental observation outside a supported operating envelope.** A valid reading falls in a component's UNSAFE band — e.g. g_o beyond the vessel-conditional wave boundary (C.9.1), g_w above the MET Category 2 onset, g_r above the Ribut Petir trigger. This is the case the threshold evidence in C.1 and C.2 speaks to.
2. **Fail-safe classification on a required observation.** A required component is unavailable, invalid or stale, so yᵢ = ⊥ and gᵢ(⊥) = UNSAFE (Corollary C.1b.1). **No valid observation is available for the failed required input** — the system has lost an input it needs. Other valid components may simultaneously contribute environmental or policy reasons.
3. **An explicitly defined conservative governance condition.** A component's UNSAFE band is set on policy grounds rather than by a source that establishes danger at that boundary. Where this applies it must be labelled as such at the component (C.9.1 already does so for the interpolated medium-vessel boundary).

**Reason terminology.** A valid environmental non-SAFE band contributes `hazard`; required resolution failure contributes `fault`; valid nighttime contributes `policy`. Conservative choices within environmental thresholds remain band-provenance details, not an additional nighttime-policy trigger. Reasons overlap and annotate the state; they do not define it (C.2.0.8).

**What UNSAFE does not assert.** It does not assert that operation is physically impossible, prohibited, or unsafe for every operator and vessel. Route 2 makes this plain: a failed sensor feed produces UNSAFE while the sea may be flat. Human decision authority is unconditional in all three states (C.8.2 step 6).

#### Evidence and policy are separate claims

Two questions must not be collapsed, and the answers come from different places:

- **Does a condition carry elevated operational risk, and where does the boundary fall?** These are **empirical or regulatory** questions. Sources can settle them, and C.1 and C.2 cite sources that do.
- **Should AI advisory participation be withdrawn at that boundary?** This is an **architectural governance policy** decision. It does not follow from the first, and **no source in the corpus establishes `elevated risk ⇒ AI advisory must be suppressed`** for any component.

The architecture's design principle is conservative over-approximation (C.1, Worst-Case Aggregation Justification Note): it may over-classify, and does so deliberately. Withdrawing advisory participation under elevated risk is therefore a defensible policy — but it is a policy, and where a component's boundary rests on policy rather than on a source, the component must say so.

The empirical basis for the *ordering itself* is established in C.1: Atacan & Düzbastılar (2023) document that combined adverse conditions produce consequence scores that far exceed any single adverse factor (mean 37.03 for combined night and heavy weather vs. 12.80 for night alone), establishing that the conditions grouped under UNSAFE carry higher operational risk than those grouped under CAUTION. Dominguez‑Péry et al. (2023) confirm that multi-variable adverse conditions constitute the highest risk cluster across 504 IMO accident reports, establishing that conditions with all parameters within bounds carry lower risk than those with at least one parameter elevated. **These sources support the ranking of risk; they do not by themselves establish the governance response attached to each rank.**

This definition is the formal basis for the worst‑case aggregation rule in the classification function and for Theorem C.2 (Monotonicity of A_AI) in C.6.

---

The deterministic safety layer maps the environmental state to a safety state. Two forms are used throughout this document and must not be conflated (C.2.0.1):

**Ideal form** — every component holds a valid value; this is what Theorem C.1 quantifies over:

**S = f(E)**, where f : ∏_{i∈C} Xᵢ × V → {SAFE, CAUTION, UNSAFE}

**Operational form** — the deployed system, consuming observations that may be absent, invalid or stale, under a declared exclusion set D; this is what Theorem C.1b quantifies over:

**S = F_{D,τ}(obs, v) = f(ρ_{D,τ}(obs), v)**

The ideal form is the special case in which D = ∅ and every observation resolves to a value. **Where this document writes `f(E)` it means the ideal form**; where deployed behaviour is at issue it writes `F_{D,τ}`.

Where:

**S ∈ {SAFE, CAUTION, UNSAFE}**

### C.2.0 Observation model — four conditions, four responses

*Added 2026-09-08. Prior to this section the specification defined gᵢ over ideal domains only, while the manuscript, the viva document and an explainer each asserted a fail-safe rule — "if any xᵢ = ⊥, return UNSAFE" — that appeared nowhere in this document. That rule, applied literally, would classify **100% of the five-year empirical record as UNSAFE**, because the marine warning variable m has no data source and would be permanently ⊥. Full analysis: `finding-bottom-semantics.md`.*

A deployed classifier does not receive values from Xᵢ. It receives **observations**, which may be absent, invalid, out of date, or structurally unavailable. Four distinct conditions were previously collapsed into the single symbol ⊥; they warrant four different responses and are separated here.

| # | Condition | Decidable from the value alone? | Response | Where resolved |
|---|---|---|---|---|
| **A** | **Invalid** — outside the physically possible range | Yes | ⊥ → UNSAFE | Validation, C.2.0.3 |
| **B** | **Absent** — no reading available now | Yes | ⊥ → UNSAFE | Validation, C.2.0.3 |
| **C** | **Stale** — reading older than the permitted age | **No** — requires an observation timestamp | ⊥ → UNSAFE | Freshness, C.2.0.4 |
| **D** | **Unmeasured** — no data source exists in this deployment | **No** — a property of the deployment | **Declared exclusion**, pinned at SAFE | Configuration, C.2.0.5 |

**A, B and C are runtime faults and resolve to ⊥. D is not a fault** — it is a permanent reduction of the specification's scope, and treating it as a fault is what produces the degenerate all-UNSAFE result.

---

#### C.2.0.1 Spaces and the type of f

*Added 2026-09-08 (typing audit). Before this subsection, `f(E)` was written with two incompatible meanings in the same document — applied to raw values of `E` in C.2 and Theorem C.1, and to resolved inputs `yᵢ` in the evaluation order of C.2.0.7. `E` also bundled `v`, which is a configuration parameter rather than an observation, while `g_o(o, v)` took it as a separate argument. The type of `f` is fixed here and used consistently thereafter.*

Let **C = {w, r, m, o, t}** be the set of **condition components** — the time-varying quantities the classifier reads — and let **V = {small, medium, big}** be the **configuration domain**. Vessel category v ∈ V is fixed for a deployment and is *not* a condition component (C.1).

Four spaces are distinguished:

| Space | Definition | Meaning |
|---|---|---|
| **Xᵢ** | X_w = ℝ≥0, X_r = ℝ≥0 × K with K = {0, 1}, X_m = {none, advisory, warning, alert}, X_o = ℝ≥0 × ℝ≥0, X_t = [0, 24) | Value domain of component i ∈ C |
| **Obsᵢ** | (Xᵢ × 𝕋) ∪ {⊥} | **Observation** — a value with the instant it was taken, or a fault |
| **Y** | ∏_{i∈C} (Xᵢ ∪ {⊥}) | **Resolved input** — what the classifier actually consumes |
| **V** | {small, medium, big} | Configuration |

The classifier and the pipeline that feeds it are then typed separately:

```
f   : Y × V → {SAFE, CAUTION, UNSAFE}                    the classifier
ρ_{D,τ} : ∏_{i∈C} Obsᵢ → Y                               resolution (C.2.0.3–5, 7)
F_{D,τ} = f ∘ ρ_{D,τ} : ∏_{i∈C} Obsᵢ × V → {SAFE, …}     the deployed classifier
```

**ρ is where the four conditions are discharged** — exclusion (C.2.0.5), validation (C.2.0.3) and freshness (C.2.0.4) all resolve to a member of Xᵢ ∪ {⊥} before f is reached. **f itself sees only values and ⊥.**

**Notation `f(E)` is retained** for the ideal case, where `E = (w, r, m, o, v, t)` holds a valid value in every component. Formally `f(E)` abbreviates `f((w, r, m, o, t), v)` with every component in its Xᵢ — the case Theorem C.1 quantifies over. Where resolved inputs are meant, the `yᵢ` notation is used explicitly. **The two are not interchangeable, and conflating them is what the audit found.**

---

#### C.2.0.2 Observation space

For each condition component xᵢ ∈ {w, r, m, o, t} with domain Xᵢ, define the **observation space**

**Obsᵢ = (Xᵢ × 𝕋) ∪ {⊥}**

where 𝕋 is the time domain, an observation (x, τ) pairs a value with the instant it was taken, and **⊥ denotes a runtime fault** — the value is absent or known invalid.

*What ⊥ attaches to.* ⊥ attaches to **the quantity the classification function reads**, not to the declared variable. This matters for o = (wave height, swell period): g_o reads the wave height component only (C.9.3), so an absent swell period does not make o faulted. Without this stipulation the swell period — which no available data source provides — would render o permanently ⊥ and produce the same degenerate result as m.

*The rainfall pair is a second, and different, structured case.* r = (rate, κ) has **both** coordinates read by g_r, so the o rule does not transfer to it and a separate stipulation is required (C.2.0.4a, added 2026-09-09):

- **rate is the required coordinate.** ⊥ attaches to it under conditions A, B and C exactly as for a scalar component, and g_r(⊥) = UNSAFE follows from Corollary C.1b.1 unchanged.
- **κ is a derived supplementary indicator, not an independent observation.** It is computed from the provider's weather code by the total map χ of C.2.0.4a. Where no code accompanies the rate, κ resolves to 0 and classification proceeds on the rate alone; an unavailable code is therefore **not** a fault of r.

This asymmetry is the executable behaviour of every canonical script and is stated here rather than inferred. Its safety direction is recorded in C.2.0.4a: because κ can only escalate, defaulting it to 0 is non-escalating, and the consequence — that all g_r figures are lower bounds — is carried explicitly rather than treated as a fail-safe guarantee.

*v is not in this space.* Vessel category is supplied by the operator at configuration time, not sampled at runtime. Its failure mode is *unconfigured*, handled in C.2.0.6.

---

#### C.2.0.3 Validation — conditions A and B

A validation function **valᵢ : Obsᵢ → Obsᵢ** maps any observation whose value lies outside the physically possible range for xᵢ to ⊥, and passes all others unchanged. Absence is already ⊥ by construction of Obsᵢ.

Physical ranges are properties of the measured quantity, not safety thresholds, and are distinct from the classification boundaries in C.2. A wind reading of −5 kn or 500 kn is rejected as impossible; a reading of 25 kn is accepted as valid and *then* classified CAUTION.

---

#### C.2.0.4 Freshness — condition C

Staleness cannot be expressed by a function of the value alone, so it is resolved **upstream of classification**. For each component define a maximum permitted age **ageᵢ ∈ 𝕋** and the freshness map

```
freshᵢ(obs, τ_now) = ⊥                 if obs = ⊥
                   = ⊥                 if τ_now − τ > ageᵢ
                   = x                 otherwise,  where obs = (x, τ)
```

so that **freshᵢ : Obsᵢ × 𝕋 → Xᵢ ∪ {⊥}**. This keeps gᵢ a function of a value, with the temporal judgement made where the timestamp is available.

**ageᵢ is a specified parameter per component, and no value is proposed here.** Wave height at hourly model resolution and a marine warning broadcast have different natural staleness budgets. Each requires its own justification; asserting an unsourced number would repeat the error corrected for the rainfall threshold on this date (`finding-met-lower-boundary-gap.md` §4).

---

#### C.2.0.4a The thunderstorm indicator κ — derivation and resolution

*Added 2026-09-09 (Appendix C rainfall signature synchronisation). This subsection records semantics that the canonical implementation has always executed; no classifier behaviour changes and no empirical figure moves. Prior to this subsection C.2 declared `g_r : ℝ≥0 → S` while every canonical script evaluated a two-input rainfall classifier, and the adjacent prose asserted the storm route was "formally part of the specification" without typing it.*

**Raw code versus derived indicator.** The provider supplies, alongside the precipitation rate, a **raw weather code c** drawn from the WMO present-weather code set. c is *not* the classifier input. The classifier consumes a derived binary indicator κ obtained by the total map

```
χ : C_WMO ∪ {absent} → K = {0, 1}

χ(c) = 1   if c ∈ {95, 96, 99}
     = 0   otherwise, including c absent or unrecognised
```

**{95, 96, 99} is the complete set of codes that activate the route**, taken from the canonical implementation and from no other source. No further code is included, and the meteorological content of these codes beyond "thunderstorm present" is not relied upon.

**χ is total and never returns ⊥.** This is the point on which the rainfall pair differs from every other component. An absent or unrecognised code does not produce a fault; it produces κ = 0, and the rainfall classification is then determined by the rate alone. Consequently:

- **κ is category C in the observation taxonomy of C.2.0** — a *derived feature whose absence deterministically defaults to 0* — and is not one of conditions A–D applied to an independent observation.
- **κ is not, and must not become, a member of the declared exclusion set D.** D records components for which no data source exists in a deployment (C.2.0.5). The unexercised storm route is a different phenomenon from the g_m archive gap, and conflating them would misstate both. **D = {m} for the retrospective replay, unchanged.**

**Safety direction, stated without overclaim.** Because κ can only escalate (C.2, and Observation C.1c.1), defaulting an unavailable code to 0 is the *non-escalating* default. This is fail-**open** for that disjunct, not fail-safe, and it is the opposite of the rule applied to a required coordinate. It is recorded here because it is what the implementation does, and it carries one consequence that must travel with every rainfall figure: **where the code feed is absent or incomplete, g_r results are lower bounds.** No source is claimed to justify the default, and a deployment whose code feed is unreliable should treat this as an open specification item rather than an inherited guarantee.

**Empirical status at the study site.** Over the canonical five-year record (43,848 hours) the raw code is present and recognised in every hour, and κ = 0 in every hour: no code in {95, 96, 99} occurs, because the provider documents thunderstorm estimation as unavailable for this region (F-11). **The route is typed and evaluated but empirically unexercised, and the default branch of χ was itself never taken.**

---

#### C.2.0.5 Declared exclusions — condition D

A deployment declares a set **D ⊆ {w, r, m, o}** of components for which **no data source exists**. For i ∈ D the component is **pinned at SAFE** — the least element of ≻, the value that cannot raise the classification:

**Well-formedness of D.** Three conditions; an exclusion set violating any of them is not well-formed.

- **(D1) t ∉ D.** The constraint is **structural, and does not rest on any empirical frequency.** Declared exclusion is condition D of C.2.0 — *no data source exists in this deployment* — and t cannot satisfy it: time of day is read from the device clock rather than from an external feed, so there is no deployment in which "no time source exists". A clock, date or solar-lookup failure is therefore a *fault* (t = ⊥ → UNSAFE via Corollary C.1b.1), never an exclusion, and the two must not be conflated: an exclusion pins a component at SAFE, whereas a fault drives it to UNSAFE. Admitting t ∈ D would let a well-formed deployment pin a required governance component at SAFE on the strength of a failure mode that is definitionally a fault.

  > *Corrected 2026-09-09 (closure residue repair).* This clause previously justified the constraint empirically — *"`g_t` determines 87.63% of all non-SAFE classifications at the study site"* — which was wrong twice over. **The figure is superseded**, computed under the fixed-clock classifier that SDR-001 replaced; the canonical `g_t` share of all-hours non-SAFE is **86.82% (PRIMARY) / 90.19% (RESOLUTION)**, and neither value belongs in this argument. **And the reasoning was inverted:** resting a structural constraint on a site-specific binding share would imply the constraint weakens wherever `g_t` happens to bind less often, when in fact it holds at every site regardless of the binding profile. The figures above are context only and carry no part of the argument.
- **(D2) D ⊊ C.** At least one component must be observed. This follows from (D1), since t ∈ C \ D.
- **(D3) D is declared, and every severity figure produced under D ≠ ∅ is reported as a lower bound.**

**Lemma C.1c (Monotone degradation of informativeness).** For exclusion sets D ⊆ D′ satisfying (D1)–(D2), and for every resolved input, **f_{D′} ⪯ f_D** — enlarging the exclusion set can only lower or preserve the classification, never raise it.

*Proof.* Excluded components are pinned at SAFE, the least element of ≻. Enlarging D replaces one or more arguments of max-severity with SAFE, and replacing an argument of a maximum by the least element cannot increase the maximum. ∎

**Observation C.1c.1 (κ is escalation-only).** *Added 2026-09-09.* For every r ∈ ℝ≥0, **g_r(r, 0) ⪯ g_r(r, 1)**. *Proof.* g_r(r, 1) = UNSAFE, which is the greatest element of ≻, so no value of g_r(r, 0) can exceed it. ∎ Since g_r enters f only as an argument of max-severity, and a maximum is monotone in each argument, raising κ from 0 to 1 can only raise or preserve f. **An active thunderstorm indication can therefore never reduce severity**, and the default κ = 0 of C.2.0.4a is the non-escalating choice.

This is a governance-classifier property, not a physical claim: it states that the specification treats an indicated thunderstorm as maximally severe, **not** that a thunderstorm is proven physically unsafe for any particular vessel. It also supplies the direction of the bound recorded in C.2.0.4a — because κ can only escalate, any hour in which a genuine thunderstorm went unindicated is classified no higher than it should be, so g_r figures are lower bounds.

**Why this lemma matters more than it looks.** Theorem C.1b holds for *any* well-formed D, and that generality could be mistaken for strength. It is not: totality is preserved as D grows, but **informativeness degrades monotonically**. At the maximal well-formed exclusion set D = {w, r, m, o}, f reduces to g_t alone — a pure night curfew, total and near-useless. **Totality is a floor, not a virtue.** A deployment must report D alongside its figures precisely so that a reader can judge where on that spectrum it sits.

Formally:

**gᵢ(·) ≜ SAFE for all i ∈ D**

Three obligations attach, and an exclusion is not well-formed without all three:

1. **D is declared in the specification of the deployment**, not left as an implicit convention.
2. The pin is at the **least severe** value, so an excluded component never raises the classification.
3. **Every severity figure produced under a non-empty D is a lower bound**, and must be reported as one.

*Why pin low rather than high.* Pinning at UNSAFE makes the system unusable whenever any source is permanently unavailable — the degenerate case above. Pinning low is sound only because obligation 3 is discharged: the figures are honest about being lower bounds. The residual risk is a reader mistaking a lower bound for an estimate, and the mitigation is disclosure rather than a different pin.

*This is the retrospective case.* Every historical replay in this project runs with **D = {m}** — no marine warning archive exists for the site (Q2). That is why m is held at `none` throughout and why all severity figures are lower bounds. **The practice was already correct; it had simply never been specified, which is what allowed it to contradict the fail-safe rule.**

*D is a property of a deployment, not of the architecture.* A deployment with a live MET broadcast has D = ∅, and m unavailable *at a moment* is then a fault (condition B), not an exclusion.

---

#### C.2.0.6 Configuration precondition — v

The system does not start without a vessel category. **v unconfigured is a startup precondition failure, not a classification outcome.** Returning UNSAFE would be incorrect: the architecture has nothing to govern until it knows which vessel it is governing, and g_o's thresholds are undefined without v.

---

#### C.2.0.7 Evaluation order

The four conditions are resolved in a fixed order, and the order is load-bearing — an excluded component is never treated as faulted:

```
0.  v configured?  and  D well-formed (t ∉ D)?   no → refuse to start   (C.2.0.5–6)
1.  for i ∈ D:        gᵢ ≜ SAFE                                          (C.2.0.4)
2.  for i ∉ D:        yᵢ ← freshᵢ(valᵢ(obsᵢ), τ_now)                     (C.2.0.3–4)
2a. for r:            κ ← χ(c), total into K; never ⊥                    (C.2.0.4a)
2b. for t:            resolve clock, date and canonical solar lookup.
                      any required one failing → y_t ← ⊥      (C.2 g_t row)
3.  F ← f(y, v) = max-severity( g_w(y_w), g_r(y_r, κ), g_m(y_m), g_o(y_o, v), g_t(y_t, d) )
```

**Step 2b is load-bearing and must not be short-circuited.** A failed clock, date or solar lookup resolves to ⊥ and reaches UNSAFE through Corollary C.1b.1 — as a **fault**. It does **not** establish that it is night, and the implementation must never infer nighttime from a missing dependency. The two routes to `g_t = UNSAFE` are distinct in provenance even though they agree in value: *valid* night is **policy**, failed resolution is **fault** (C.2.0.8). Steps 2a and 2b were made explicit on 2026-09-09; both record existing behaviour in `canonical_gt.py`, which defaults every row to UNSAFE and overwrites it only when the clock is finite *and* the date is present in the frozen artefact.

---

#### C.2.0.8 Provenance reason sets over an evaluated trace

*Canonical semantic cleanup, 2026-09-08, after SDR-001. Supersedes the scalar fault/hazard fallback; historical audit reports retain the earlier contract. This changes provenance semantics only.*

**Trace and type.** Let **q ∈ Q** be an explanatory abstraction over the information used and produced by the existing resolution/classification evaluation. Q is the set of completed, internally consistent evaluated traces under the current canonical specification. It is not a new environmental variable, a replacement for Y, an extra input to f, or a newly implemented runtime structure.

Each trace retains:

- The configured vessel category v, declared exclusion set D, and applicable resolution/freshness context τ.
- For each i ∈ {w,r,m,o,t}: component identity, exclusion status, resolution status (excluded, valid, or fault with the failed required input identified), and resulting component severity sᵢ. Excluded components have sᵢ = SAFE; required faults have sᵢ = UNSAFE. A valid environmental component retains its resolved reading and the applicable classifier band, including v for g_o. For r the resolved reading is the pair (rate, κ) and the retained detail identifies which route applied — a rate band, or the κ = 1 storm route of C.2.0.4a. *(Clarified 2026-09-09; the reason-set contract below is unchanged. An active κ satisfies the existing **hazard** condition, since r is then a valid non-excluded environmental component at UNSAFE. No new reason label is introduced, and hazard retains its bounded meaning — a configured non-SAFE band or trigger, not proven physical danger.)*
- For time: clock value and validity, date and validity, required solar-lookup validity, the sunrise/sunset values actually used and artefact identity, and resulting g_t. A failed required time dependency resolves to the existing fail-safe UNSAFE; it does not establish nighttime. If a dependency was not evaluated after an earlier failure, that status is retained rather than asserted valid.
- The existing aggregate S = max-severity(sᵢ). Trace consistency means these entries agree with the existing evaluation; an arbitrary or contradictory record is not in Q.

Only completed classifications have a trace in Q. Missing v or an ill-formed D (including t ∈ D) refuses startup as before (C.2.0.5–7); no classified state or reason set is presented. Exclusions are resolved before faults. Missing parts not read by a classifier, such as swell period for g_o, do not become required-input faults.

Define the canonical provenance annotation:

**reasons : Q → 𝒫({fault, hazard, policy})**

For q ∈ Q, include each label independently:

| Label | Necessary and sufficient condition |
|---|---|
| **fault** | At least one required, non-excluded component or required time dependency fails resolution (missing, invalid or stale where freshness applies). |
| **hazard** | At least one valid, non-excluded environmental component i ∈ {w,r,m,o} has sᵢ ∈ {CAUTION, UNSAFE}. |
| **policy** | Valid clock, date and solar lookup establish t < sunrise(date) or t ≥ sunset(date), hence g_t = UNSAFE under the canonical nighttime advisory policy. |

**SAFE and concurrency.** No active restriction gives reasons(q) = ∅; for consistent traces this holds iff S = SAFE. The labels are overlapping: valid night plus wave CAUTION gives {hazard, policy}; wind fault plus valid wave UNSAFE plus valid night gives {fault, hazard, policy}. No priority discards a concurrent reason. An excluded component contributes no label, even if its raw data are missing. Valid night and failed time resolution must be distinguished from trace validity, never from g_t = UNSAFE alone. Exact valid sunrise contributes no policy label; exact valid sunset does.

**Bounded meaning.** hazard means an environmental reading is in a configured non-SAFE band, including CAUTION. It does not prove physical danger, certain harm, prohibited navigation or causation beyond the classifier. Threshold evidence and conservative boundary choices (including the medium-vessel interpolation) remain separate provenance details. The policy label here specifically identifies the nighttime advisory trigger; it does not imply that other governance responses are policy-free. Detailed provenance should identify the component, band and evidence/policy basis; the time detail may be `nighttime_advisory_policy`.

**Active triggers, not a binding-cause partition.** All non-SAFE environmental triggers remain recorded even when a more severe component determines S. Retained component severities permit separate binding analysis, including ties. Reason shares may overlap and must not be summed to 100% without a separately defined mutually exclusive metric. Existing “weather-driven UNSAFE” metrics are not reinterpreted as a partition of these reason sets.

**Annotation only.** The conceptual annotated output is (S, reasons(q)); projection onto S returns exactly the existing F_{D,τ}(obs,v). Provenance reasons never participate in governance: they do not alter resolution, max-severity, G(S), A_AI(S), RS(S), rule selection, or human authority. Theorem C.3 continues to depend only on S. No classifier, threshold or fail-safe changes.

**Specification boundary and operator wording.** This is a canonical contract, not a claim that a runtime logger, UI or engine currently implements it. No implemented cause function or consumer was found in scripts/ during cleanup. An implementation using this contract should say “AI advisory unavailable: nighttime policy applies.” For simultaneous wave restriction: “AI advisory unavailable: nighttime policy applies. Wave reading exceeds the configured band.” Human decision authority remains unconditional.

**Closure:** the former OPEN taxonomy mismatch is closed at specification level by this contract. Verification and integrity evidence: [cleanup report](cleanup-report-cause-taxonomy-2026-09-08.md). Runtime trace capture remains unimplemented.

---

### Per-Component Classification Functions

For each condition component xᵢ ∈ {w, r, m, o, t} with domain Xᵢ, define a per-component classification function

**gᵢ : Xᵢ ∪ {⊥} → {SAFE, CAUTION, UNSAFE}**, with **gᵢ(⊥) = UNSAFE**

where X_w = ℝ≥0, **X_r = ℝ≥0 × K with K = {0, 1}** (rate paired with the thunderstorm indicator κ — C.2.0.4a), X_m = {none, advisory, warning, alert}, X_o = ℝ≥0 × ℝ≥0 and X_t = [0, 24). **Two of these read a single value** — g_w and g_m. **g_r reads the pair (r, κ)**; **g_o is additionally parameterised by vessel category v** and reads the wave-height coordinate only; and **g_t is evaluated against a valid date and its canonical solar lookup** alongside the clock value, which the resolution layer supplies as required context rather than as a widened X_t. The per-row threshold tables below define gᵢ on Xᵢ; the ⊥ case is uniform across all five and is not repeated in each table.

> *Corrected 2026-09-09.* This sentence previously declared `X_r = ℝ≥0` and described "four single-argument functions", contradicting the type table in C.2.0.1 and the g_r and g_t definitions below. It is a second type declaration that the rainfall synchronisation of the same day did not reach.

#### Component classifiers are not required to be surjective

*Added 2026-09-08 (SDR-001 execution condition C-4). This states a property the specification has always had; it is written down because it was previously only implicit, and a reader meeting a two-valued component beside three-valued ones would otherwise read it as an omission.*

**The declaration `gᵢ : Xᵢ ∪ {⊥} → 𝒮` states a *codomain*, not an image.** It fixes the set from which gᵢ draws its values. It does **not** assert

> Im(gᵢ) = 𝒮

and no result in this appendix requires that. A component classifier may therefore satisfy

> **|Im(gᵢ)| < |𝒮|**

while remaining **well typed and total**. Totality is a requirement on the *domain* — every input receives exactly one output — and is independent of how many distinct outputs are actually produced. **Totality ≠ surjectivity**, and it is totality that Theorem C.1 and Theorem C.1b establish.

**Verified against every formal result in this appendix.** None requires component surjectivity:

| Result | What it requires of gᵢ |
|---|---|
| **Definition C.1** (severity order) | Nothing — an order on the three-element set 𝒮, fixed by the cardinality of 𝒮, not by any component's image |
| **Theorem C.1** (ideal totality) | Each gᵢ **total**; each threshold partition **exhaustive**. A two-interval partition of [0, 24) satisfies this identically to a three-interval one |
| **Theorem C.1b** (operational totality) | Totality plus gᵢ(⊥) = UNSAFE |
| **Corollary C.1b.1** (fail-safe) | Only that gᵢ(⊥) = UNSAFE and that UNSAFE is ≻-maximal |
| **Lemma C.1c** (monotone degradation) | Only the ⪯ ordering of classifications under D ⊆ D′ |
| **Theorem C.2** (monotonicity of A_AI) | Nothing — quantifies over S₁, S₂ ∈ 𝒮; never mentions gᵢ |
| **Theorem C.3** (Safety Dominance) | Nothing — "the proof depends only on the value of S, never on how S was reached" (C.7.2) |
| **max-severity** | Only the total order ≻ on 𝒮 |
| **G(S), A_AI(S)** | Defined on S alone, after aggregation; blind to component structure |
| **(D1) t ∉ D** | Independent of Im(g_t) |

**No proof obligation changes if a component's image shrinks**, so no proof in this appendix required re-verification for this statement.

**Where graduation lives.** "Graduated" is a **system-level governance property**, not a requirement that each component independently realise every state. It holds because

> **A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅**   (C.4, Corollary C.2)

and because CAUTION is reachable in 𝒮 — at this site principally through `g_o` and `g_r` (F-7). Whether any single gᵢ realises CAUTION is a property of that component and its evidence, not of the architecture.

> #### Canonical time classifier following SDR-001 application — `g_t` under Model B
>
> **APPLIED 2026-09-08. This is the canonical `g_t`.** The superseded fixed-clock classifier is recorded in the `g_t` table below.
>
> **SDR-001** (`finding-gt-evidence-closure.md` Part 6) defines `g_t` as a solar-event classifier for which
>
> **Im(g_t) = {SAFE, UNSAFE}**  and  **CAUTION ∉ Im(g_t)**
>
> **by deliberate design, not by oversight.** Three independent reviews located no source supporting a time-based intermediate state: the cited simulator study tested no twilight condition, COLREGs Rule 20(b) has no intermediate level, and no corpus paper reports a graded dusk risk profile. Retaining a three-valued time classifier for architectural symmetry would exceed the evidence.
>
> The architecture remains globally three-state and graduated: **2,091 of 43,848 PRIMARY hours — 4.77% — are globally CAUTION, all weather-driven**. **Canonical figures after migration: Level 2 binds 5.81% (PRIMARY) / 4.48% (RESOLUTION).** The pre-migration figures 7.72% / 5.98% were computed under the superseded fixed-clock `g_t`.
>
> The accepted transition cost of that design is recorded in C.9.5.

#### Aggregation

The overall classification function is:

**f(E) = max-severity(g_w(w), g_r(r, κ), g_m(m), g_o(o, v), g_t(t, d))**   *(ideal form; operationally f(y, v) over resolved inputs — C.2.0.1. `d` is the valid date whose canonical solar lookup accompanies the clock value; it is required context resolved upstream, not a sixth condition component.)*

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

| Classification | Threshold | Source | Status |
|---|---|---|---|
| SAFE | w ≤ **21.6** knots | **MET Malaysia Category 1 onset — 40 km/h.** 40 ÷ 1.852 = 21.598 kn, expressed at the one-decimal resolution of the data. Corroborated by Rahim et al.: full fishing operations in the low-wind season | **Official — MET** |
| CAUTION | **21.6** < w ≤ **27.0** knots | Between MET Cat 1 and Cat 2 onsets. Corroborated by Rahim et al.: restricted operations (2–3 trips/week, near-shore) in the East season | **Official — MET** at both endpoints |
| UNSAFE | w > **27.0** knots | **MET Malaysia Category 2 onset — 50 km/h.** 50 ÷ 1.852 = 26.998 kn, which is 27.0 at one-decimal resolution. Corroborated by Gao: "if wind too strong, I don't go" | **Official — MET** |

> **Amended 2026-09-08: SAFE/CAUTION boundary 22 → 21.6 kn.**
>
> The boundary was specified as 22 kn with no stated derivation — the row cited only "Rahim et al. fishing season", which is corroboration, not a numeric source. MET Malaysia's Category 1 onset is **40 km/h = 21.598 kn**. The 22 was an undocumented rounding of that value.
>
> **Principle applied:** *a canonical threshold preserves its source value unless there is an independently justified reason to discretise.* No architectural reason exists for 22 over 21.6, and the data carries one-decimal resolution, so 21.6 is directly representable. The upper boundary is unchanged in value — 26.998 kn is 27.0 at the same resolution — but its provenance is now stated rather than implied.
>
> **This rounding changed an empirical result.** Over five years of sea-cell data the observed maximum sustained wind is **21.8 kn**. At a 22 kn boundary `g_w` never activates; at 21.6 kn it activates **twice** (readings of 21.7 and 21.8 kn). The prior finding that `g_w` *never* fires was an artefact of the rounding, not a property of the site.
>
> **Consequences, applied in full:** finding F-1 is restated — `g_w` is *almost never* binding rather than never binding; prediction **P16 is re-resolved from REFUTED to CONFIRMED**, since it registered "> 0 but < 500" and the corrected specification yields 2. See F-17 and `empirical-findings-2026-09-06.md` §0a.
>
> The amendment was adopted on provenance grounds. That it reverses a registered prediction *in the project's favour* is not a reason to prefer it, and the reasoning would be identical had it gone the other way — as it did for rainfall the same day, where the equivalent correction refuted P22.

*Note on `w` as sustained wind (added 2026-09-06, revised same day).* `w` is defined as **sustained** wind speed. Care is needed when drawing on fisher-interview sources, which often report gusts: Rahim et al. (2024) [[notes]](../../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) describe West season as "wind **gusts** of 30 to 40 knots per hour," which at typical gust ratios implies roughly 19–31 kn sustained — straddling rather than clearly exceeding the 27 kn boundary. That paper's West season figure was previously cited here as direct support for the UNSAFE threshold; the citation has been removed, since the threshold rests on MET Malaysia criteria and the West season classification is more securely driven by wave height (> 2 m) than by wind. Any future empirical corroboration of `g_w` must confirm whether the source reports sustained or gust values.

Note also that MET Malaysia's published criteria state "wind speeds from 40–50 kmph" **without specifying sustained or gust** — the ambiguity is in the source, not in this formalisation.

> **Correction.** An earlier version of this note additionally claimed that ERA5 `wind_speed_10m` is an hourly mean and therefore under-represents peak sustained wind. **That was wrong** — Open-Meteo documents the variable's valid time as *"Instant"*. The `10m` denotes height above ground (the WMO standard reference level), not an averaging window. See `empirical-findings-2026-09-06.md` F-9. A separate and more likely explanation for the observed low wind values is that the archive request used the default `cell_selection=land`, returning wind over a land grid cell while wave data came from a sea cell — see F-10, currently untested.

*Domain:* w ∈ ℝ≥0. The three intervals [0, 21.6], (21.6, 27.0], (27.0, +∞) partition ℝ≥0 exhaustively with no overlap.

---

**g_r(r, κ) — Rainfall: intensity (mm/hr) with thunderstorm indicator**

g_r : ℝ≥0 × K → {SAFE, CAUTION, UNSAFE},  K = {0, 1}

```
                ⎧ UNSAFE   if  κ = 1                          (storm route)
                ⎪ SAFE     if  κ = 0  ∧  0 ≤ r ≤ 10.0
    g_r(r, κ) = ⎨ CAUTION  if  κ = 0  ∧  10.0 < r ≤ 20.0
                ⎩ UNSAFE   if  κ = 0  ∧  r > 20.0
```

where **r** is the precipitation rate in mm/hr and **κ = χ(c)** is the derived thunderstorm indicator of C.2.0.4a, obtained from the provider's raw weather code c. **κ is an escalation-only trigger:** g_r(r, 1) = UNSAFE for every valid r, so κ can raise the rainfall classification and can never lower the classification obtained from the rate.

> **Retyped 2026-09-09.** This block previously declared `g_r : ℝ≥0 → S` and described the storm route only in the prose below, while all eight canonical scripts evaluated `(rate > 20.0) ∨ (c ∈ {95, 96, 99})`. The signature is corrected to the classifier that generated every canonical figure; **thresholds, classifications and empirical outputs are unchanged.** The two boundaries remain **R_CAUTION = 10.0** and **R_UNSAFE = 20.0**. This is a type-level repair under the standing rule that evidence follows implementation, and it is *not* a change of scientific behaviour.
>
> Note that the implementation's local variable named `storm` denotes the **disjunction** `(r > 20.0) ∨ (κ = 1)`, not κ alone. κ as defined here is strictly the code-derived coordinate; the rate-driven UNSAFE band is a separate route to the same classification.

| Classification | Threshold | Source | Status |
|---|---|---|---|
| SAFE | r ≤ 10.0 mm/hr | JPS/DID Malaysia (Infobanjir) — upper limit of the *Light* intensity band (1–10 mm/hr). **MET publishes no criterion below 20 mm/hr** | Official; **necessarily non-MET** |
| CAUTION | 10.0 < r ≤ 20.0 mm/hr | Interval between the two published boundaries. Yamin et al.: erratic/heavy rainfall rated a primary hazard by 91% of fishers | Official at both endpoints |
| UNSAFE | r > 20.0 mm/hr | **MET Malaysia — *Kriteria Amaran Ribut Petir*.** Thunderstorm warning issued at rain intensity exceeding 20 mm/hr expected to persist beyond one hour | **Official — MET** |

*Domain:* (r, κ) ∈ ℝ≥0 × {0, 1}. At κ = 0 the three intervals [0, 10.0], (10.0, 20.0], (20.0, +∞) partition ℝ≥0 exhaustively with no overlap; at κ = 1 the classification is UNSAFE for every r. The product domain is therefore covered exhaustively with no overlap. **The rate partition alone is no longer the whole domain of g_r** — see Theorem C.1(i).

> **Amended 2026-09-08 (second pass): `r` redefined as numeric, ℝ≥0 in mm/hr.**
>
> `r` was previously specified as an ordinal categorical variable over {none, light, moderate, heavy, storm}. That representation was **incoherent with the numeric thresholds** once those were anchored: a first-pass amendment earlier the same day paired the categorical labels with mm/hr bands, producing a table in which `CAUTION = {moderate, heavy} = 10.1–20.0 mm/hr` while `rainfall-intensity-mapping.md` defines *moderate* as 10.1–30.0 and *heavy* as 30.1–60.0. A reading of 25 mm/hr was therefore *moderate* — and so CAUTION by the label — while simultaneously UNSAFE by the numeric rule. The category *heavy* had also become unreachable, since anything above 20 classifies UNSAFE.
>
> **The defect was in the representation, not the thresholds.** The observation is, and always was, a continuous hourly precipitation rate. Making `r` numeric and letting `g_r` perform the classification removes the contradiction rather than patching it, and matches every implementation in `scripts/`.
>
> **The JPS/DID intensity categories are retained as provenance for the 10.0 mm/hr boundary — not as the mathematical domain of `r`.** See §C.9.4 and `finding-met-lower-boundary-gap.md`.
>
> **No threshold values changed and no empirical figure moves.** This amendment is a change of representation only.

**Secondary route to UNSAFE — now formally typed (2026-09-09).** WMO weather codes 95/96/99 (thunderstorm) yield UNSAFE where present. This route is carried by the κ coordinate of the classifier signature above and by the map χ of C.2.0.4a; it is no longer described in prose alone. It remains **inert in the present dataset** — zero thunderstorm codes appear in five years, because Open-Meteo documents thunderstorm estimation as not possible outside Central Europe. See C.9 and finding F-11. In consequence, `r = UNSAFE` is reached only through the rainfall-rate coordinate of a criterion that is fundamentally about a *phenomenon*, and is **under-detected by an unknown margin**. Typing κ changes what the specification *says*, not what the classifier *does*: the route was always evaluated, and it never fired.

> **Amended 2026-09-08: rainfall thresholds anchored to MET, SAFE/CAUTION 7.5 → 10.0 mm/hr.**
>
> Prior to this amendment the analysis scripts used `> 7.5` mm/hr for CAUTION and `> 20` mm/hr for UNSAFE, and neither value appeared in this document. The 20 was correct by coincidence — it matches MET's Ribut Petir trigger — but was undocumented. **The 7.5 matched no published source**; its nearest ancestor is a mapping recorded as an error in `docs/implementation/data-source-met-malaysia.md` line 125, corrected there but never in the code.
>
> **Why MET's *Hujan Berterusan* tiers were not used.** MET publishes continuous-rain warnings at *Buruk* (cumulative > 60 mm over the period) and *Bahaya* (> 150 mm / 24 hr). These are cumulative totals, not intensity rates, and applying them to hourly data would require an hourly disaggregation assumption that no source supplies — the assumption would itself become an unsourced parameter. The Ribut Petir criterion is MET's only published *hourly rate*, and is therefore the only MET rainfall criterion commensurable with the data.
>
> **Why the SAFE/CAUTION boundary is not MET-derived.** MET publishes no rainfall criterion below 20 mm/hr. This is the same structure documented for wave height in `finding-met-hydrodynamic-gap.md`: MET criteria state where a warning is *issued*, not where caution should *begin*. Observed independently in two variables from two separate MET criteria documents — a pattern with a mechanism, not a verified universal. See `finding-met-lower-boundary-gap.md` §1.
>
> **Empirical consequence** (small vessel, waves 1.0/1.25 m, sea-cell weather): Level 2 binding falls from **7.84% to 7.72%** on the five-year record (6.15% → 5.98% on the higher-resolution 3.25-year series). `g_r`'s share of daylight CAUTION falls from 3.21% to 1.55%. **The UNSAFE state is unaffected** — the 20 mm/hr trigger is unchanged, so daylight UNSAFE hours (1,170) and the weather-driven share of UNSAFE (11.8%) do not move. The entire effect is in CAUTION.
>
> **Cost, stated plainly:** this is the third amendment adopted on provenance grounds that lowered the reported headline, after the wave-resolution correction (12.4% → 8.3%) and the wave operational-ceiling correction (8.3% → 6.1%). It was adopted because the prior value had no source, not because of its effect on the figures.
>
> Full analysis: `finding-met-lower-boundary-gap.md`.
>
> **Open:** `r = storm` is defined by a rainfall-intensity proxy for a *phenomenon* — a thunderstorm — that cannot be observed in this dataset at all (F-11). The UNSAFE state is under-detected by an unknown margin and every `g_r` figure is a lower bound.

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
| small (< 10) | o < 1.0 m | 1.0 ≤ o ≤ **1.25** m | o > **1.25** m |
| medium (10–25) | o < 1.4 m | 1.4 ≤ o ≤ 2.8 m | o > 2.8 m |
| big (> 25) | o < 1.5 m | 1.5 ≤ o ≤ 3.5 m | o > 3.5 m |

> **Amended 2026-09-06: small-vessel UNSAFE 1.9 m → 1.25 m.**
>
> Yaakob et al. (2015) tested each vessel at the mean of successive sea-state bands. Boat A (6.54 m LOA) **passes** Sea State 3 (tested at Hs ≈ 0.875 m) and **fails** Sea State 4 (tested at Hs ≈ 1.875 m). Two distinct quantities follow:
>
> - **1.25 m** — the top of the SS3 band: the highest wave height at which the vessel is *demonstrated operable*
> - **1.875 m** — the point at which it is *demonstrated to fail*
>
> The prior threshold of 1.9 m used the failure point. For a departure gate the conservative reading is the operational ceiling: the boundary should sit at the edge of the demonstrated-safe envelope, not at the demonstrated-failure point. The true limit lies between 0.875 m and 1.875 m; 1.25 m is the highest value the evidence supports as safe.
>
> **Empirical consequence** (MFWAM 8 km, 2021-10 to 2024-12, small vessel): daylight UNSAFE rises from **3 hours to 409** (0.02% → 3.13%), and the weather-driven share of all UNSAFE hours from **0.1% to 7.0%**. Under the prior threshold the participation gate `G(S) = 0` was reachable only by darkness; it is now reachable by sea state.
>
> **Cost, stated plainly:** Level 2 binding in the departure window falls from **8.3% to 6.1%**, since hours previously classified CAUTION now classify UNSAFE. The amendment was adopted on the provenance argument, not the resulting figures — it produces a *smaller* headline number.
>
> Full analysis: `finding-met-hydrodynamic-gap.md` §6, `scripts/threshold_decision.py`.
>
> **Open:** the medium and big rows still use failure-point-style reasoning scaled from MET. Neither has vessel-specific NORDFORSK data, so neither can be given the same treatment without new evidence.

*Note on the tuple:* Ocean state o is a tuple (wave height m, swell period s) in the general definition (C.1). Classification depends only on the wave height component; swell period is retained in the state representation as a secondary modifier for domain instantiation but does not enter g_o. The thresholds use wave height as the governing variable, consistent with MET Malaysia's Kawasan Perairan range vocabulary.

**Threshold provenance — why some boundaries are not MET-derived.**

MET Malaysia's published criteria state that Category 1 covers *"rough seas with wave heights of **up to** 3.5 metres."* The 3.5 m figure is the Category 1 / Category 2 boundary. **MET does not state where Category 1 begins.**

The published criteria therefore supply an upper boundary and no lower one, and cannot provide the SAFE/CAUTION threshold for any vessel class. Nor do they differentiate by vessel size beyond the qualitative phrase "dangerous to small crafts."

The architecture accordingly adopts MET criteria wherever MET speaks, and fills with peer-reviewed hydrodynamic evidence only where MET is silent:

| Boundary | Source |
|---|---|
| CAUTION/UNSAFE, big vessel (3.5 m) | **MET Category 1 maximum — official** |
| SAFE/CAUTION, all vessels | Hydrodynamic — MET provides no value |
| Small and medium vessel rows | Hydrodynamic — MET has no vessel-specific criteria |

This is not a departure from official criteria; it fills a gap those criteria leave open. Full analysis, including a quantified comparison against Yaakob et al. and Jeong & Im on five years of site data, is in `finding-met-hydrodynamic-gap.md` — **the source of truth for threshold provenance.**

> **~~Open amendment (2026-09-06, not yet applied)~~ — ✅ ADOPTED 2026-09-06. This block is superseded; retained only as a record of the decision point.** The small-vessel UNSAFE boundary was 1.9 m, derived from Yaakob Boat A's NORDFORSK *failure point* (SS4, Hs ≈ 1.875 m). Yaakob reports a distinct quantity — Boat A's **operational ceiling of 1.25 m**, the top of Sea State 3 — which is the more appropriate basis for a departure gate. **The amendment was adopted the same day; the canonical value is 1.25 m, as stated in the `g_o` table above.** The empirical figures quoted in the original version of this block (zero UNSAFE-by-wave at 1.9 m; 2.8% at 1.25 m) were computed under a since-superseded data configuration and must not be cited — see `empirical-findings-2026-09-06.md` §0a for current values. Full rationale: `finding-met-hydrodynamic-gap.md` §6.

**Empirical basis by row.**

*big (> 25 GRT) — unchanged from the prior vessel-independent definition.* The 1.5 m SAFE/CAUTION boundary is corroborated by Jeong & Im (2023) [[notes]](../../notes/Proposal%20of%20Restrictions%20on%20the%20Departure%20of%20Korea%20Small%20Fishing%20Vessel%20according%20to%20Wave%20Height.md), whose Hs_KIMO formula yields 1.58 m at 16 m LOA and 1.43 m at 14 m LOA — bracketing 1.5 m. The 3.5 m CAUTION/UNSAFE boundary aligns with MET Malaysia Category 1 maximum wave height criteria (https://www.met.gov.my/en/ramalan/angin-kencang-and-laut-bergelora/, verified August 2026).

*small (< 10 GRT).* The 1.0 m SAFE/CAUTION boundary is Jeong & Im's own proposed restriction for vessels ≤ 10 m LOA (their Table 12). The **1.25 m CAUTION/UNSAFE boundary is Yaakob et al.'s (2015)** [[notes]](../../notes/Stability%2C%20Seakeeping%20and%20Safety%20Assessment%20of%20Small%20Fishing%20Boats%20Operating%20in%20Southern%20Coast%20of%20Peninsular%20Malaysia.md) **operational ceiling for their 6.54 m Malaysian vessel** — the top of Sea State 3, the highest band the hull passes under NORDFORSK 1987 criteria. At Sea State 4 (Hs ≈ 1.875 m) the same vessel fails on multiple parameters (RMS vertical acceleration at FP = 0.332 g against a 0.275 g limit; bridge = 0.195 g against 0.150 g).

**Design decision:** the boundary is placed at the operational ceiling rather than the failure point. Yaakob et al. do not themselves characterise either value as a departure prohibition; the reasoning applied here is that a departure gate should sit at the edge of the demonstrated-safe envelope, not at the point of demonstrated failure. The true limit lies between the last passing test (0.875 m) and the first failing test (1.875 m); 1.25 m is the highest value the evidence supports as safe. Recorded as a threat to internal validity in C.9.

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
| **SAFE** | **sunrise(date) ≤ t < sunset(date)** | Daytime operating condition — the baseline against which Atacan & Düzbastılar (2023) measure elevated night-time risk |
| **UNSAFE** | **t < sunrise(date) or t ≥ sunset(date)** | Night-time operating condition — Atacan & Düzbastılar (2023) report elevated accident probability (4.08 vs 3.43) and consequence (12.80 vs 8.53) relative to the daytime baseline. **Boundary from COLREGs Rule 20(b)**, "from sunset to sunrise" |
| **UNSAFE** | **t = ⊥** | Missing or invalid clock, date or solar lookup — fail-safe, Corollary C.1b.1 |

**Type:** `g_t : (X_t × Date) ∪ {⊥} → {SAFE, UNSAFE}`

**Half-open by construction: exact sunrise is SAFE, exact sunset is UNSAFE.** The two intervals partition `[0, 24)` exhaustively for every date, which is what Theorem C.1 requires.

**`g_t` emits no CAUTION.** `Im(g_t) = {SAFE, UNSAFE}` and `CAUTION ∉ Im(g_t)`, **by deliberate design** — see "Component classifiers are not required to be surjective" above. The architecture remains three-state; CAUTION is reached through `g_o` and `g_r`.

**Canonical implementation:** `scripts/canonical_gt.py`, reading the frozen solar artefact `data/solar/solar-events-daily.csv` (`solar-spec-v1`, `solar-v1`, 5.98° N / 116.01° E, UTC+8). **No canonical script computes solar astronomy independently** — the dependency is *stored solar artefact → `g_t` → `f`*.

> **⚠️ SUPERSEDED 2026-09-08 by SDR-001.** The previous canonical classifier was the fixed clock **SAFE 06:00 ≤ t < 17:00 · CAUTION 17:00 ≤ t < 19:00 · UNSAFE otherwise**. Its three boundaries had **no located source** across five priority tiers, and `SAFE` began at 06:00 while sunrise at this site falls between 06:01 and 06:34 — so SAFE began before sunrise on every day of the year. **It is retained in `canonical_gt.g_t_incumbent_superseded` for historical reproduction only and must not be used for current results.** Full record: `finding-gt-provenance-audit.md`, `finding-gt-evidence-closure.md` Part 6, `report-c8-migration-2026-09-08.md`.
>
> **The 17:00–19:00 CAUTION band is withdrawn, not relocated.** Three independent reviews located no source for a twilight intermediate state: the cited simulator study tested no twilight condition, COLREGs has no intermediate level, and no corpus paper reports a graded dusk risk profile.

> ### Evidence and policy — do not collapse these
>
> **Evidence establishes:** night navigation carries **elevated** operational risk; COLREGs Rule 20(b) defines sunset-to-sunrise as the boundary **for navigation lights**; the superseded 06:00/17:00/19:00 values have no source; no source supports a twilight CAUTION band.
>
> **Architecture policy decides:** **night ⇒ `g_t` = UNSAFE ⇒ AI advisory unavailable.** **No source establishes this implication.** COLREGs regulates lights, not decision support, and **does not require AI abstention**. Nothing here asserts that night operation is prohibited or physically unsafe — fishers demonstrably operate at night. `S = UNSAFE` sets `G(S) = 0` and `A_AI(S) = ∅`; **human decision authority remains unconditional** (C.8.2 step 6).

*Column revised 2026-09-08 (pre-adoption semantic cleanup); **thresholds unchanged by that cleanup — and subsequently replaced the same day by SDR-001**, which substituted the astronomical boundaries above for the fixed clock. The "unchanged" clause describes the wording cleanup only and must not be read as a statement about the current thresholds (chronology clarified 2026-09-09). The SAFE row previously claimed "sufficient daylight for safe operation and return to port" — an unsupported physical-safety claim, matching the one corrected in C.1. The UNSAFE row's figures are now given explicitly so that what the source establishes — **elevated risk relative to a baseline** — is visible rather than compressed into "highest scores".*

> 📌 **HISTORICAL — the state of this row before SDR-001 was applied on 2026-09-08.** Retained as provenance; **neither item describes the canonical classifier.** *(Status corrected 2026-09-09: this block previously stood unmarked and described SDR-001 as "**DRAFT — not approved, not applied**", which has been false since the C-8 migration.)*
> 1. **Item 1 is CLOSED by SDR-001.** The unsourced boundaries 06:00, 17:00 and 19:00 were the defect; the canonical classifier no longer uses them. The 87.63% figure quoted here was computed under the superseded fixed clock and is **provenance only** — the canonical `g_t` share of all-hours non-SAFE is **86.82% PRIMARY / 90.19% RESOLUTION**. See `finding-gt-provenance-audit.md` and **SDR-001 (APPROVED and APPLIED)** in `finding-gt-evidence-closure.md`, `report-c8-migration-2026-09-08.md`.
> 2. **Item 2 remains open and is unaffected by SDR-001.** The 7.90 score cited elsewhere for `t` is the score for Atacan & Düzbastılar's *restricted visibility* scenario, not their *night* scenario; both that study and COLREGs treat darkness and restricted visibility as separate hazards. The phrase remains dropped from this column pending that correction — see `finding-gt-operational-semantics.md` §3.2.

*Domain:* t ∈ [0, 24), evaluated against a valid date d and its canonical solar lookup. For each such d the stored events satisfy 0 ≤ sunrise(d) < sunset(d) < 24, and the **two** intervals

**[sunrise(d), sunset(d))**  and  **[0, sunrise(d)) ∪ [sunset(d), 24)**

are disjoint and together exhaust [0, 24). Every valid (t, d) therefore receives exactly one classification.

> *Corrected 2026-09-09 (g_t totality synchronisation).* This line previously read *"The three intervals [6, 17), [17, 19), [19, 24) ∪ [0, 6) partition [0, 24) exhaustively"* — the **superseded fixed-clock** partition, including its withdrawn 17:00–19:00 CAUTION band. It survived the SDR-001 migration unmarked and sat outside the superseded blockquote above, where a reader could take it for current semantics. **There are two intervals, not three, and `g_t` emits no CAUTION.**

---

### Theorem C.1 — Totality of f

**Theorem C.1 (Totality of f over ideal domains).** For all E ∈ domain(E) — that is, every component holding a valid value of its own domain — f(E) is defined and returns exactly one element of {SAFE, CAUTION, UNSAFE}.

*See Theorem C.1b for totality over the observation space a deployed system actually receives.*

**Proof.** It suffices to show that (i) each condition classification function is total over its domain, and (ii) max-severity is total over {SAFE, CAUTION, UNSAFE}⁵.

*(i) Totality of each classification function.*

- **g_w:** The thresholds [0, 21.6], (21.6, 27.0], (27.0, +∞) partition ℝ≥0 exhaustively. Every w ∈ ℝ≥0 falls in exactly one interval. ✓
- **g_r:** g_r is two-argument, with domain ℝ≥0 × K, K = {0, 1}. Totality is established in two cases over κ, which is exhaustive because K is finite with exactly two members. **Case κ = 1:** g_r(r, 1) = UNSAFE for every r ∈ ℝ≥0, by the first line of the definition; the case is total and does not depend on r. **Case κ = 0:** the thresholds [0, 10.0], (10.0, 20.0], (20.0, +∞) partition ℝ≥0 exhaustively, so every r falls in exactly one interval. The two cases are disjoint and cover K, so every pair (r, κ) ∈ ℝ≥0 × K receives exactly one classification. ✓ *(Amended 2026-09-08: `r` became numeric, the prior case arguing over five categorical values. Amended 2026-09-09: the domain is a product and the rate partition alone no longer exhausts it — see C.2.0.4a.)*
- **g_m:** The four values {none, advisory, warning, alert} are the complete domain of m. Each value is assigned to exactly one classification. ✓
- **g_o:** g_o is two-argument, with domain (ℝ≥0 × ℝ≥0) × {small, medium, big}. Totality is established in two steps. First, for each fixed v ∈ {small, medium, big}, the corresponding row of the threshold table induces three intervals that partition ℝ≥0 exhaustively with no overlap — [0, 1.0), [1.0, 1.25], (1.25, +∞) for small; [0, 1.4), [1.4, 2.8], (2.8, +∞) for medium; [0, 1.5), [1.5, 3.5], (3.5, +∞) for big. Second, {small, medium, big} is finite and exhausts the domain of v, and classification does not depend on the swell period component of o, so every (o, v) pair falls under exactly one row and within exactly one interval of that row. ✓
- **g_t:** g_t is evaluated on a clock value together with a valid date and its canonical solar lookup, so the valid-input branch is quantified over pairs (t, d) with t ∈ [0, 24). Fix any such d and write s_r = sunrise(d), s_s = sunset(d); the frozen artefact `data/solar/solar-events-daily.csv` supplies values satisfying **0 ≤ s_r < s_s < 24** (verified over all 1,827 replay dates; this is a property of the low-latitude study site, not a general astronomical claim — no polar-day or polar-night case is asserted or required). The half-open interval **[s_r, s_s)** and its complement in [0, 24), **[0, s_r) ∪ [s_s, 24)**, are disjoint — a point cannot be both inside and outside a set — and exhaustive, since every t ∈ [0, 24) satisfies exactly one of t < s_r, s_r ≤ t < s_s, or t ≥ s_s. g_t returns SAFE on the first interval and UNSAFE on the second, so every valid (t, d) receives exactly one classification. ✓ **Two intervals, not three: g_t emits no CAUTION** (Im(g_t) = {SAFE, UNSAFE}), and totality does not require surjectivity. *(Amended 2026-09-09: this case previously used the superseded fixed clock [6, 17), [17, 19), [19, 24) ∪ [0, 6), which had survived the SDR-001 migration of 2026-09-08.)*

*(ii) Totality of max-severity.*

max-severity takes a tuple (S_w, S_r, S_m, S_o, S_t) ∈ {SAFE, CAUTION, UNSAFE}⁵ and returns the element that is greatest under ≻ (Definition C.1). Since ≻ is a total strict order on a finite set, the maximum always exists and is unique. ✓

Therefore f(E) = max-severity(g_w(w), g_r(r, κ), g_m(m), g_o(o, v), g_t(t, d)) is defined and returns exactly one element of {SAFE, CAUTION, UNSAFE} for all E. ∎

**Significance.** Theorem C.1 establishes that the safety classifier has no undefined states — every combination of environmental conditions maps to exactly one safety state. This is a necessary condition for runtime governance: a classifier that could fail to return a state would leave the governance layer without a basis for enforcing (G(S), A_AI(S)).

**Scope, stated precisely.** Theorem C.1 quantifies over **E ∈ domain(E)** — tuples in which every component holds a valid value of its own domain. It says nothing about inputs a deployed system actually faces, where observations may be absent, invalid or stale. That gap is closed by Theorem C.1b.

---

### Theorem C.1b — Operational Totality of f

*Added 2026-09-08. Theorem C.1 is total over the ideal domains ∏Xᵢ. A deployed classifier receives observations, not values, and its input space is strictly larger. This theorem establishes totality over that larger space.*

**Definitions.** Let D be a **well-formed** exclusion set (C.2.0.5: D ⊆ {w, r, m, o}, so t ∉ D), let v ∈ V be configured (C.2.0.5), and let ρ_{D,τ} be the resolution map of C.2.0.1, producing a resolved input **y ∈ Y = ∏_{i∈C}(Xᵢ ∪ {⊥})**.

**Theorem C.1b (Operational Totality).** For every configured v ∈ V and every **well-formed** D, the deployed classifier

**F_{D,τ} = f ∘ ρ_{D,τ} : ∏_{i∈C} Obsᵢ × V → {SAFE, CAUTION, UNSAFE}**

is total: for **every** observation tuple — including those in which any subset of non-excluded components is absent, invalid or stale — F_{D,τ} is defined and returns exactly one element.

*Equivalently, f is total on Y × V, and ρ_{D,τ} is total into Y.*

**Proof.** By the evaluation order of C.2.0.7, each of the five arguments to max-severity is produced by exactly one of two routes.

*(i) Excluded components.* For i ∈ D, gᵢ ≜ SAFE by definition (C.2.0.5). This is a constant function, hence total, and returns exactly one element. ✓

*(ii) Non-excluded components.* For i ∉ D, the resolved input is yᵢ ∈ Xᵢ ∪ {⊥}. Two cases exhaust this set:
- **yᵢ ∈ Xᵢ** — gᵢ is total on Xᵢ and returns exactly one element, by Theorem C.1(i). ✓
- **yᵢ = ⊥** — gᵢ(⊥) = UNSAFE by definition, exactly one element. ✓

The union Xᵢ ∪ {⊥} is therefore exhausted, and gᵢ is total on it. Note that ⊥ arises from validation (invalid value), from absence, or from freshness (stale value); all three converge on the same symbol before gᵢ is reached, so no further case analysis is required. ✓

*Note on the structured components (2026-09-09).* Y = ∏_{i∈C}(Xᵢ ∪ {⊥}) is defined generically over the Xᵢ, so it absorbs the product-valued X_r = ℝ≥0 × K of C.2.0.1 without amendment: y_r ∈ (ℝ≥0 × K) ∪ {⊥}. **y_r = ⊥ denotes failure of the rate coordinate only.** κ cannot produce ⊥ — χ is total into K by C.2.0.4a — so the fail-safe of Corollary C.1b.1 is triggered by an absent, invalid or stale *rate*, never by an absent weather code. This preserves the corollary's scope exactly; it does not widen or narrow it.

*(iii) Aggregation.* max-severity is total over {SAFE, CAUTION, UNSAFE}⁵ by Theorem C.1(ii) — ≻ is a total strict order on a finite set, so the maximum exists and is unique. ✓

Every argument of max-severity is defined, and max-severity is total, so f is total on Y × V. ρ_{D,τ} is total into Y by (i) and (ii) — every component resolves either to a pin, a value, or ⊥, with no fourth case. The composite F_{D,τ} is therefore total. ∎

**Corollary C.1b.1 (Fail-safe).** If yᵢ = ⊥ for any i ∉ D, then F_{D,τ} = UNSAFE.

*Proof.* gᵢ(⊥) = UNSAFE, and UNSAFE is the greatest element of ≻, so it is the maximum regardless of the other four arguments. ∎

**This is the rule the manuscript, the viva document and the explainer have each asserted. It is now a theorem rather than a stated convention, and it is derived rather than stipulated — it follows from gᵢ(⊥) = UNSAFE together with the maximality of UNSAFE under ≻, not from a separate pre-condition check.**

**Significance — and why this is more than housekeeping.** *Mathematical totality* (Theorem C.1: f is defined over its specified domains) does not imply *operational totality* (Theorem C.1b: f is defined over the input space a deployment actually produces). The gap between them is precisely where a low-resource deployment operates: missing, delayed and permanently unavailable observations are the normal case in the target context, not the exception.

The distinction was not academic here. Before this section existed, the fail-safe rule was asserted in prose in three documents and defined in none, and the project's own historical replay — which holds m at a fixed value for all 43,848 hours because no archive exists — would have classified **every hour UNSAFE** had the asserted rule been applied literally. That is a concrete demonstration, found in this system rather than hypothesised, that a classifier total over its ideal domain can be degenerate over the domain it is deployed into.

**Consequences for the other theorems.** Theorem C.2 (Monotonicity) operates on the A_AI set definitions and does not reference f, so it is unaffected. Theorem C.3 (Safety Dominance) requires only that f be *total*; extending totality to a larger input space strengthens its antecedent and leaves the proof intact. Neither required re-verification, consistent with the scope boundary recorded in `decision-record-empirical-first.md` §4.

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

When S = CAUTION, any **Go** advisory generated by the active Layer 3 rule set is presented with a caution qualifier (e.g., “Proceed with caution”). The recommendation type remains **Go**, but its presentation and explanation are modified by the safety state. This preserves set containment while allowing state‑dependent advisory messaging. (OPEN-L3-3 resolution, 2026-09-11 — the earlier phrasing “the Go recommendation is automatically presented by the system” was reinterpreted as presentation-layer guidance conditioned on Go ∈ AI(E); no automatic emission mechanism outside the Layer 3 rule engine is introduced.)

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

Let **AI** denote the set of recommendation types generated by the AI reasoning engine under the active rule set. *(Written `AI(E)` elsewhere; the argument is the state that produced S, and the property does not depend on it — see C.7.2.)*

Then the Safety Dominance Property is defined as:

**For all E, if S = f(E) — or in deployment S = F_{D,τ} — then:**
- **AI ⊆ A_AI(S)**
- **If S = UNSAFE, then AI = ∅**

This means the AI can only generate recommendations that belong to the admissible recommendation space defined by the safety state.

### C.7.1 Enforcement mechanism

The Layer 3 advisory component is implemented as a rule-based engine. The governance layer (Layer 2) supplies a rule set RS(S) to Layer 3 before any reasoning begins:

- **RS(SAFE)** = rules producing recommendations in {Go, Delay, DepartureTime, Duration}
- **RS(CAUTION)** = rules producing recommendations in {Go, Delay}
- **RS(UNSAFE)** = ∅ (never passed — G(UNSAFE) = 0, so Layer 3 receives no input)

The rule engine fires only rules present in the active RS(S). No rule in RS(CAUTION) produces DepartureTime or Duration, so those types cannot appear in AI when S = CAUTION. The constraint is structural — it holds before generation begins, not by filtering outputs after the fact.

### C.7.2 Proof of the Safety Dominance Property

**Theorem C.3 (Safety Dominance Property).** Let AI denote the set of recommendation types generated by the AI reasoning engine, and let S be the safety state supplied to the governance layer — S = F_{D,τ} in deployment, S = f(E) in the ideal case be the safety state returned by the classifier. Then:

**Operational form (2026-09-08).** Safety Dominance is a claim about the *deployed* architecture — its assumptions A1–A4 concern the runtime rule engine and the gate — so it is stated over the operational classifier:

**For every observation tuple, every configured v ∈ V and every well-formed D:  AI ⊆ A_AI(F_{D,τ})**

and as a special case:

**If F_{D,τ} = UNSAFE, then AI = ∅**

*The ideal form `AI(E) ⊆ A_AI(f(E))` for E ∈ domain(E) is the special case D = ∅ with every observation resolving to a value, and follows immediately.*

**Assumptions.**

1. **(A1) Rule-based engine.** Layer 3 is implemented as a rule-based symbolic reasoning engine. It generates only recommendation types for which an active rule exists in its current rule set.

2. **(A2) Rule set supply.** The governance layer (Layer 2) supplies rule set RS(S) to Layer 3 before any reasoning begins, where RS(S) is defined as:
   - RS(SAFE) contains only rules producing recommendations in {Go, Delay, DepartureTime, Duration}
   - RS(CAUTION) contains only rules producing recommendations in {Go, Delay}
   - RS(UNSAFE) = ∅ — never supplied, since G(UNSAFE) = 0 gates off Layer 3 entirely

3. **(A3) Gate enforcement.** If G(S) = 0, Layer 3 receives no input and produces no output: AI = ∅. *This holds regardless of the reason set: fault, hazard, policy or any combination.*

4. **(A4) Engine fidelity.** The rule engine fires only rules present in the active RS(S). No rule produces a recommendation type not present in the rule's conclusion.

**Proof by exhaustive case analysis on S.**

Since S is total — by Theorem C.1 in the ideal case, by **Theorem C.1b** in the operational case — and S ∈ {SAFE, CAUTION, UNSAFE}, there are exactly three cases.

**The proof depends only on the value of S, never on how S was reached.** This makes it independent of reasons(q) in C.2.0.8: environmental UNSAFE (`hazard`), required resolution failure (`fault`, Corollary C.1b.1), valid nighttime (`policy`), and mixed reason sets all use Case 1 whenever S = UNSAFE. A hazard trigger in CAUTION uses Case 2. Reasons are annotations and never enter the case analysis or select RS(S).

**Case 1: S = UNSAFE.**

By (A3), G(UNSAFE) = 0, so Layer 3 receives no input.
By (A3), AI = ∅.
By definition, A_AI(UNSAFE) = ∅.
Therefore AI = ∅ = A_AI(UNSAFE), and in particular AI ⊆ A_AI(UNSAFE). ∎

**This case covers fault-driven UNSAFE.** If any non-excluded component resolves to ⊥ then S = UNSAFE by Corollary C.1b.1, G(UNSAFE) = 0, and (A3) gates Layer 3 off entirely — so the AI produces nothing, and Safety Dominance holds *a fortiori*. **A data-feed failure cannot cause the architecture to emit an out-of-scope recommendation; it causes it to emit none.**

**Case 2: S = CAUTION.**

By (A3), G(CAUTION) = 1, so Layer 3 is active.
By (A2), Layer 3 receives RS(CAUTION), which contains only rules producing recommendations in {Go, Delay}.
By (A4), the engine produces only recommendation types present in RS(CAUTION).
Therefore AI ⊆ {Go, Delay} = A_AI(CAUTION). ∎

**Case 3: S = SAFE.**

By (A3), G(SAFE) = 1, so Layer 3 is active.
By (A2), Layer 3 receives RS(SAFE), which contains only rules producing recommendations in {Go, Delay, DepartureTime, Duration}.
By (A4), the engine produces only recommendation types present in RS(SAFE).
Therefore AI ⊆ {Go, Delay, DepartureTime, Duration} = A_AI(SAFE). ∎

In all three cases, AI ⊆ A_AI(S). Since S is total in both the ideal and operational forms, the property holds for f(E) and for F_{D,τ} alike. ∎

**Remarks.**

- The proof is constructive: it depends only on the definitions of RS(S) and the gate function G(S), both of which are fully under the designer's control. **No runtime checking is required for the property to hold of the specified system.** This is a statement about the specification, not a guarantee about any implementation of it. The theorem's assumptions A1–A4 — that the gate is evaluated before generation, that RS(S) is the rule set actually supplied, that the engine draws only on its active rule set — are obligations the implementation must discharge. A defect that violates any of them violates the property, and the proof offers no protection against that. What the proof removes is the need for an *output filter*: correctness does not depend on inspecting recommendations after generation. It does not remove the need for implementation verification. See C.9.
- The property holds *before* generation begins, not by filtering outputs after the fact. RS(S) is supplied to Layer 3 as a precondition; the engine has no mechanism to generate types outside its active rule set.
- Together with Theorem C.2 (Monotonicity), this theorem characterises the full safety behaviour of the governance pair: at any given state, AI output is bounded within A_AI(S); as S becomes more severe, that bound tightens.

See `docs/canonical/justification-layer3-enforcement.md` for the full enforcement justification and design rationale for the rule set supply mechanism.

---

## C.8 Formal Architecture Flow — **canonical**

> ### ⚠️ Canonical Pipeline Rule
>
> **The formal end-to-end architecture pipeline is defined only in this section.** Any later section discussing the architecture as a whole must reference C.8 rather than restating the pipeline. Local equations may be repeated elsewhere only where a theorem or proof requires them, and must be explicitly scoped as **ideal** or **operational**.
>
> *Adopted 2026-09-08. Before consolidation the pipeline was stated independently in three places — this section, "Conceptual Structure", and "Formal Contribution" — with no marked authority among them. A notation correction applied to one silently left the other two stale, which is the mechanism by which drift had recurred. The duplicates are now cross-references.*

### C.8.1 Spaces and functions

Defined in C.2.0.1; restated here in full because this section is the canonical statement of the pipeline.

| Symbol | Type | Role |
|---|---|---|
| **C** | {w, r, m, o, t} | Condition components — the time-varying quantities read by the classifier |
| **V** | {small, medium, big} | Configuration domain. **v ∈ V is not a condition component** — it is supplied at configuration time, not sampled |
| **Xᵢ** | — | Value domain of component i ∈ C (C.2) |
| **Obsᵢ** | **(Xᵢ × 𝕋) ∪ {⊥}** | Observation — a value paired with the instant it was taken, or ⊥ denoting a runtime fault |
| **Y** | **∏_{i∈C} (Xᵢ ∪ {⊥})** | Resolved input — what the classifier consumes |
| **D** | D ⊆ {w, r, m, o}, **t ∉ D** | Declared exclusion set (C.2.0.5) |
| **ρ_{D,τ}** | **∏_{i∈C} Obsᵢ → Y** | Resolution map — discharges exclusion, validation and freshness (C.2.0.3–5) |
| **f** | **Y × V → 𝒮** | Resolved classifier, 𝒮 = {SAFE, CAUTION, UNSAFE} |
| **F_{D,τ}** | **f ∘ ρ_{D,τ} : ∏_{i∈C} Obsᵢ × V → 𝒮** | **Operational classifier — what a deployment executes** |

### C.8.2 The operational pipeline — authoritative form

The deployed architecture is:

```
obs ──ρ_{D,τ}──▶ y ──f(·, v)──▶ S ──▶ ( G(S), A_AI(S) ) ──▶ AI ──▶ Human Decision
```

with the operational state written explicitly as

**S = F_{D,τ}(obs, v) = f(ρ_{D,τ}(obs), v)**

and the governance stage as

**S → G(S) → A_AI(S)**

Stage by stage:

1. **Observation.** Each condition component yields an element of Obsᵢ — a timestamped value, or ⊥ if absent or invalid.
2. **Resolution (ρ_{D,τ}).** Excluded components (i ∈ D) are pinned at SAFE; the remainder pass through validation and freshness, resolving to Xᵢ ∪ {⊥}. Evaluation order is fixed and load-bearing — C.2.0.7.
3. **Classification (f).** Max-severity aggregation over the five component classifiers, with gᵢ(⊥) = UNSAFE. Total by **Theorem C.1b**.
4. **Governance.** G(S) sets participation; A_AI(S) sets admissible advisory scope.
5. **Advisory generation.** The rule engine draws only on RS(S). **AI ⊆ A_AI(S)** by **Theorem C.3**, and this holds for fault, hazard, policy and mixed reason sets; only S selects the governance configuration.
6. **Human decision.** Unconditional; the operator may act contrary to any recommendation.

Alongside S, the specification defines **reasons(q) ∈ 𝒫({fault, hazard, policy})**, where q ∈ Q is the evaluated trace of C.2.0.8. This annotation never participates in governance or changes RS(S). SAFE has an empty reason set. Runtime recording is not yet implemented; this is the provenance contract.

### C.8.3 The ideal form — theorem scope, not the deployed pipeline

**S = f(E)**, where **E = (w, r, m, o, v, t)** with every component holding a valid value of its domain:

**E → S = f(E) → (G(S), A_AI(S)) → AI**

**This is the ideal-domain special case that Theorem C.1 quantifies over — it is not the deployed pipeline.** It coincides with C.8.2 exactly when D = ∅ and every observation resolves to a value. Wherever this appendix writes `f(E)`, the ideal form is meant; deployed behaviour is written `F_{D,τ}`.

---

## C.9 Known Limitations of the Formal Model

The following are recorded as limitations of the current formalisation. Each is a design decision made in the absence of a directly applicable source, or a scope boundary accepted deliberately.

### C.9.1 Threshold grounding

**Small-vessel UNSAFE boundary (1.25 m).** *Amended 2026-09-06 from 1.9 m.* Set at Yaakob Boat A's **operational ceiling** — the top of Sea State 3, the highest band the 6.54 m hull passes under NORDFORSK 1987 — rather than at its failure point (SS4, Hs ≈ 1.875 m). Yaakob et al. do not characterise either value as a departure prohibition; treating the operational ceiling as the gate is an interpretation, though a conservative one: the boundary sits at the edge of the demonstrated-safe envelope rather than at demonstrated failure. The true limit lies between the last passing test (0.875 m) and the first failing test (1.875 m), and is not resolved by the source.

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

**Swell period is unused, and does not fault `o`.** o is defined as a tuple (wave height, swell period), but g_o classifies on wave height alone. Per C.2.0.2, ⊥ attaches to the quantity a classification function reads, so an unavailable swell period does not render o faulted. Without that stipulation o would be permanently ⊥ — no available data source provides swell period — and every hour would classify UNSAFE. Encounter period relative to vessel natural roll period is a genuine determinant of seakeeping response, and its omission means the classifier cannot distinguish a short-period wind sea from a long-period swell at the same significant wave height. Retained in the state representation for future use.


### C.9.4 What the formal results do and do not establish

*Added 2026-09-08 following a claim audit. Each entry names a place where an earlier version of this document asserted a formal property that the evidence supports only in a weaker form.*

**Max-severity cannot under-classify relative to its own components — not relative to reality.** If any gᵢ returns UNSAFE then S = UNSAFE, in both the ideal and operational forms. That is a property of the operator. Real-world under-classification remains possible through three routes the operator cannot address: a threshold set too high, a hazard absent from E, or a measurement that is missing, stale or wrong. `g_m` held at `none` throughout (F-11) and tide's absence from E (C.9.3) are live instances.

**Max-severity is not a proven lower bound on combined risk.** The super-additivity evidence is directional — it shows the true danger under multiple adverse conditions exceeds that of the worst single parameter, and therefore that max-severity does not overstate risk in the multi-parameter case. A formal lower-bound property would require a quantified risk model on which "combined risk" and "the classification" are commensurable. None exists here, and no cited source supplies one.

**Safety Dominance is a property of the specification, not of any implementation.** Theorem C.3 holds by construction, and no output filtering is required for it. But its assumptions A1–A4 are *obligations on the implementation*: that the gate is evaluated before generation, that RS(S) is the rule set actually supplied, that the engine draws only on its active rule set. A defect violating any of these violates the property, and the proof gives no protection against that. **The reasoning engine is not yet implemented, so none of these obligations has been verified in code.**

**The severity ordering reflects operating envelopes, not survivability.** Where a component's UNSAFE band is drawn from the seakeeping evidence, it marks conditions outside the *demonstrated operating envelope* for the vessel category. The seakeeping sources characterise their limits as the sea state at which criteria are breached or heavy manual work becomes unsafe; none characterises any threshold as a survivability boundary, and this document does not claim one.

*Scope corrected 2026-09-08 (pre-adoption semantic cleanup).* This entry previously read "UNSAFE denotes conditions outside the demonstrated operating envelope", which overstated it in the other direction — envelope exceedance is **one route to UNSAFE, not its definition**, and it is not the route taken when the state arises from a fail-safe on a missing observation. Definition C.1 now defines UNSAFE by its governance consequence and enumerates the three routes; this entry constrains what the *envelope route* is entitled to claim. The two are consistent.

**The MET lower-boundary gap is a two-case pattern with a mechanism, not a verified universal.** See `finding-met-lower-boundary-gap.md` §1 for the precise scope.

**Theorem C.1 is total over ideal domains; Theorem C.1b is total over the observation space.** The distinction matters and was not made before 2026-09-08. An earlier version of this document proved only C.1 while three other documents asserted a fail-safe rule that C.1 does not cover. See `finding-bottom-semantics.md`.

**`f` has two domains and they must not be conflated.** `f : Y × V → S` consumes *resolved inputs*; `f(E)` is an abbreviation for the ideal case in which every component holds a value. Before the typing audit of 2026-09-08 the same notation was used for both, in the same document. See C.2.0.1.

**Totality is a floor, not a virtue.** Theorem C.1b holds for every well-formed D, but Lemma C.1c shows informativeness degrades monotonically as D grows, and at D = {w, r, m, o} the classifier reduces to a night curfew — total and near-useless. Generality over D is not strength; D must be reported with the figures.

**`ageᵢ`, the maximum permitted observation age, is unspecified.** C.2.0.3 defines the freshness map but proposes no value for any component, because none is sourced. Until each `ageᵢ` is justified, condition C (stale observations) is formalised but not instantiated — the machinery exists and the parameters do not.

### C.9.5 Accepted transition cost of the approved `g_t` replacement design

*Added 2026-09-08 (C-4); updated on migration (C-8). **This cost was accepted at approval and is now an observed property of the canonical classifier.** SDR-001 applied 2026-09-08.*

**The boundary step.** Under the canonical solar-event classifier, `g_t` transitions **directly between SAFE and UNSAFE** at sunrise and at sunset. It has no intermediate value, so the governance response to the time component is **discontinuous at those two instants**.

**Magnitude** — canonical, PRIMARY replay, 43,848 hours:

| | Superseded fixed clock | **Canonical (Model B)** |
|---|---|---|
| **Direct SAFE→UNSAFE transitions** | **2** | **1,536** |
| **`g_t`-driven SAFE→CAUTION transitions** | **1,545** | **0** |

**Interpretation.** This is a consequence of **removing an unsupported intermediate time band**, not evidence that the world changes discontinuously at sunset. Nothing physical, meteorological or physiological is claimed to be discontinuous there. What changes discontinuously is the *governance response*, because the classifier no longer interposes a state for which no evidence was found.

**Architectural consequence.** The governance response is discontinuous **for the time component**, while the **global architecture retains its CAUTION mode through the weather classifiers** — `g_o` and `g_r` (2,091 PRIMARY hours, 4.77%, all weather-driven). System-level graduation, per C.4 and Corollary C.2, is unaffected. The tension is real and is between this component's behaviour and the architecture's graduated-governance narrative; it is not a failure of any formal property.

**Usability concern.** Predictable withdrawal of advisory support at sunset may require **anticipatory interface support**. That is a UI/notification matter and is deliberately kept outside the classifier — see C.9.6.

**Evidence limitation.** **No evidence was identified supporting a twilight CAUTION band**, so an intermediate band was **not** retained merely to smooth the transition. Introducing one to soften a step would be adopting a state because it yields a middle value, which is the reason the civil-twilight alternative was rejected.

**This cost is a disclosure obligation, not a defect to be argued away.** It must appear in Threats to Validity wherever the architecture's graduated-governance claim is made.

### C.9.6 Anticipatory notification is not a safety state

*Added 2026-09-08 (C-4).*

> **current governance state ≠ future-state notification**

A deterministic pre-event notice — for example *"AI advisory will become unavailable at [sunset time]"* — **may be investigated later**. If adopted it would be:

- **deterministic**, computed from the stored solar timestamps (C-3 artefact);
- **not AI-generated reasoning**, so it does not enter `AI` and cannot violate Theorem C.3;
- **not a safety-state classification** — it changes no `gᵢ`, no `S`, no `G(S)` and no `A_AI(S)`;
- **not CAUTION**, and not a route to reintroducing a time-based intermediate state;
- **not part of SDR-001's classifier semantics.**

**No warning interval is specified here.** No value — 15 minutes, 30 minutes, an hour — has any independent justification in this project, and inventing one would repeat the error the `g_t` provenance audit was opened to correct. **No new threshold is introduced.**

Any such notice must follow the operator-message standard already adopted: report state and reason, assert no danger, issue no instruction, and preserve the operator's unconditional authority (C.8.2 step 6).
---

## Summary of Formal Model Components

> **Symbol index only. Full types and the end-to-end pipeline are in C.8.1–C.8.2** — this table is a lookup aid and is not an independent definition (Canonical Pipeline Rule, C.8).

| Symbol | Reading | Defined in |
|--------|---------|-----------|
| **E** | Environmental state, ideal form — every component valid | C.1, C.8.3 |
| **obs, ρ_{D,τ}, y** | Observation, resolution map, resolved input | C.2.0.1–5, C.8.1 |
| **D** | Declared exclusion set (t ∉ D) | C.2.0.5 |
| **f** | Resolved classifier; `f(E)` is its ideal-form abbreviation | C.2, C.8.1 |
| **F_{D,τ}** | Operational classifier — what a deployment executes | C.8.1–C.8.2 |
| **gᵢ** | Component classifier, gᵢ(⊥) = UNSAFE | C.2 |
| **q ∈ Q** | Evaluated trace abstraction over existing resolution/classification context; not an environmental variable | C.2.0.8 |
| **reasons** | Q → 𝒫({fault, hazard, policy}); overlapping provenance annotations, empty for SAFE; never used by governance | C.2.0.8 |
| **G(S)** | AI participation gate | C.3 |
| **A_AI(S)** | AI admissible recommendation space | C.4 |

Together these define the **Graduated Safety‑State‑Gated Architecture**.

---

## Conceptual Structure of the Architecture Governance Model

The formal architecture defines the governance mechanism that controls AI participation and advisory scope using environmental safety state.

> **The canonical end-to-end formal pipeline — observation spaces, resolution, operational classification `F_{D,τ}`, and governance gating — is defined in Section C.8.** This section gives the conceptual reading only and deliberately states no equations. Per the Canonical Pipeline Rule, it does not restate the pipeline.

Read plainly, the architecture works as follows:

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

> **This section states what is contributed and why it matters. It does not restate the architecture.** The governance pair, its constraints and the pipeline are defined in C.3–C.7 and C.8; per the Canonical Pipeline Rule they are referenced here, not reproduced.

The contribution is the **governance pair (G(S), A_AI(S))** — a mechanism that separates two questions existing architectures conflate into one binary: *whether* the AI participates, and *what it may recommend*.

Three formal properties give the mechanism its force, each proved in the sections indicated:

| Property | Where proved | What it secures |
|---|---|---|
| Participation and advisory constraints | C.6 | Governance is well-formed: withdrawal implies empty scope, and the intermediate state is a strict restriction |
| **Monotonicity** (Theorem C.2) | C.6 | Advisory scope never expands as conditions worsen |
| **Safety Dominance** (Theorem C.3) | C.7.2 | AI output is bounded by the admissible set **by construction**, for the ideal and operational forms alike — including when the state is fault-driven |

Two further results establish that the mechanism is defined wherever it is deployed: **Theorem C.1** (totality over the ideal domains) and **Theorem C.1b** (totality over the observation space a deployment actually produces). The distinction between them is itself part of the contribution — see C.9.4.

Together these ensure that deterministic safety classification always constrains AI participation and advisory behaviour, and that the constraint holds under absent, invalid and stale observations rather than only under well-formed input.

Therefore, the proposed contribution is **not** a new AI prediction model, but a **governance architecture** that formally constrains how AI participates in decision‑making under different safety states. The architecture ensures that AI operates within a safety‑governed advisory space and cannot generate recommendations outside deterministic safety constraints.