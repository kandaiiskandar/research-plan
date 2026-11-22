# Supervisor Decision Memorandum

**To:** Supervisory team · **From:** Iskandar Samsuddin · **Date:** 17 November 2026 · **Version:** 2 (final for review)
**Subject:** Advisory-type reachability and evidential support — two paths, and a recommendation

**Sources.** `research/non-degeneracy/causal/causal-replication-results.md` (executed 17 Nov 2026), the R1–R3 specifications in `research/`, `docs/analysis/final-research-chain-lock.md`, `docs/canonical/appendix-c-formalisation.md`, `docs/canonical/architecture-illustration.md`, `data/prediction-register.csv`. No frozen artefact was modified. No experiment was run for this memorandum and no external request was made.

**How to read this.** **Part I** is the decision. **Part II** is the evidence behind it. **Part III** is the correction and revision history, including six defects in my own criteria. Claims are labelled **[VERIFIED]** (structural fact, executed measurement, or reproduction of a canonical figure) or **[INTERPRETATION]** (a judgement that the evidence informs but does not establish). The distinction is load-bearing: Version 1 of this memorandum presented four interpretations as findings, and Part III records the corrections.

---

# PART I — SUPERVISOR-FACING SUMMARY

## The decision required

> **Approve Path B: retain the locked thesis scope — frozen RQ1–RQ3 unchanged — and document advisory-type reachability and evidential support as a specification-level limitation. Defer the human advisory-comparison study to future work behind a named entry criterion (A3 below), rather than beginning it now.**
>
> The alternative, **Path A**, is to obtain real issue-time forecast data and repeat the advisory feasibility study.
>
> **Nothing is needed from you before the next supervision meeting except this choice.** No licence request, ethics application or recruitment has been initiated.

## Verified findings

**V1 — `Go` and `Delay` are never withheld.** `A_AI(CAUTION) = {Go, Delay}` contains both, so the CAUTION filter removes only `DepartureTime` and `Duration`. Measured across 7,305 episodes: the `Go`/`Delay` content is identical under C1 and C2 in **1.000000** of episodes, and **1.000000** of divergences consist solely of withheld forecast-dependent types. **Δ_L2 therefore measures withheld advisory detail, never a change in the departure recommendation.** This was the design intent, documented at `architecture-illustration.md` §203/§209 with a cited rationale and registered as prediction P22; what is new is only the measurement consequence. **[VERIFIED]**

**V2 — The two withheld types fail for different reasons.** This replaces Version 1's claim that "two of four types cannot be produced", which was wrong about `Duration`. **[VERIFIED]**

| Type | Under persistence (concurrent information only) | Status |
|---|---|---|
| `DepartureTime` | **Structurally unreachable.** The rule requires a strictly better later hour; persistence predicts every later hour equal to the present, so the predicate can never be satisfied. Observed rate **exactly 0.00%** | A reachability failure |
| `Duration` | **Reachable (69.68% of episodes) but evidentially unsupported.** The predicted run is a deterministic threshold on the present observation, carrying no information about the future. Confirmed exactly: 2 distinct run values, step residual **0.000000**, base R² **1.000000**, calendar contribution **0** | A support failure, not a reachability failure |

**V3 — A climatological surrogate fixes the second problem and not the first.** Under damped persistence toward a causally estimated climatology, `Duration` becomes evidentially supported (ten distinct run lengths, 24.65% unexplained by the present margin, calendar explaining 31.5% of residual), while `DepartureTime` reaches only **2.48%**, against a pre-registered adequacy bar of 10%. **[VERIFIED]**

**V4 — The structural ceiling on governance divergence is the CAUTION rate.** C1 and C2 can differ only at CAUTION, so divergence cannot exceed **423 of 7,305 episodes (5.79%)**. That ceiling follows from the governance mapping and holds for any generator. Observed realisation: **146 episodes** with the oracle generator, **131** with persistence, **121** with the surrogate. **[VERIFIED]**

**V5 — Validation held.** `P(S = CAUTION)` = 5.7906% against the canonical 5.81%; UNSAFE share 42.82% against 42.88%; `α ≡ 1` reproduced persistence in 7,305/7,305 episodes; and in daylight the driver of elevated states is wave at **97.8%**, against the canonical `g_o` attribution of **97.6%** reached by a different route. **[VERIFIED]**

**V6 — Leakage detection works.** The leaky baseline failed exactly the three checks designed to catch it (truncation invariance 99/3,650; future-shuffle 240/5,475; placebo-future 43/60); both causal generators passed every gate. **[VERIFIED]**

## Interpretations

**I1 — The advisory comparison is probably underpowered, and that is the strongest practical objection.** V4 caps divergence at 423 episodes over four years, and the generators tested realised 121–146. Those cases are **not independent**: they fall within clustered CAUTION episodes, and the site's own clustering gives 85–123 independent weather events in five years. The effective sample is plausibly tens of events. **[INTERPRETATION]**

**I2 — Whether a real wave forecast would help is untested, and it is the question that decides Path A.** CAUTION at this site is 97.6% wave-driven, and the fitted damping for wave was α = 0.970 at lead 8 against 0.278 for wind and 0.138 for rainfall. **That coefficient describes the tested surrogate, not the atmosphere.** It means a monthly-hourly climatology adds little beyond persistence for wave — not that wave changes are unforecastable at 1–8 h leads. An operational wave model resolves swell arrival and wind-sea growth that a climatology cannot represent. So the orthogonality concern is a **hypothesis**, and criterion A3 is its test. Version 1 presented this as near-decisive physics; that was an overstatement. **[INTERPRETATION]**

**I3 — Path A answers no frozen research question.** Frozen RQ1–RQ3 are operational specification, empirical characterisation and robustness, and structural warrant of the classifier. A human-scored advisory comparison answers none of them, and `final-research-chain-lock.md` records the experiment set as **SUFFICIENT**. Path A would require either a new RQ under supervisory authority or siting as a construct-validity study. **[INTERPRETATION of a documentary position]**

**I4 — Path B adds a contribution rather than conceding one.** The statement *"an admissible advisory set can be specified over recommendation types that the specified inputs cannot reach, and over types reachable but evidentially unsupported — and the gap is measurable"* is a specification-level finding, verified, and not available to any of the nine competitor papers, none of which has advisory output types at all. **[INTERPRETATION]**

## Limitations

1. **Operational availability is not satisfied anywhere in this work.** The record is ERA5-Ocean reanalysis, produced days to months after the fact; nothing in it was available at 05:00 on the morning it describes. This applies to the canonical replay and to Δ_L2 = 5.81%, and belongs in the abstract of Journal 1 v2 rather than its limitations.
2. **One generator, one surrogate, one site, one configuration.** All rates are for a fixed rule set with fixed thresholds; the S1–S9 sensitivity grid was not run; PRIMARY (ERA5) only.
3. **No external safety reference exists** for this vessel class in these waters; the best independent hazard reference has no discriminating power here (FAO Category C exceeded in 2 of 9,135 episodes).
4. **The replication is exploratory throughout**, specified after the original gate had run. Original and revised criteria must be published side by side.
5. **Six of my own criteria across R1–R3 and this run were non-discriminating or defective** (Part III). V1–V6 do not depend on any single one, but that is the right context for weighing anything else.

## Recommendation

**Path B, and preserve frozen RQ1–RQ3 unchanged.** Three reasons, now in the correct order of weight after the corrections in Part III:

1. **RQ fit (I3).** Path A answers no frozen RQ and would reopen a set frozen deliberately. This is documentary, not a judgement about data.
2. **Power (I1, on V4).** A structural ceiling of 423 CAUTION episodes, 121–146 realised, clustering into tens of independent events.
3. **Resolution and licensing bind against each other (Part II).** The only hourly issue-time wave source forbids publishing the extracted records; the publishable route is 3-hourly on waves and cannot resolve a five-hour window.

**I2 is deliberately not among the reasons.** It would be the strongest argument if established, and it is not established. If the supervisory team prefers Path A, **test A3 first** — it is cheap and it is the one criterion that could settle I2 either way.

---

# PART II — EVIDENCE AND PATH ASSESSMENT

## The observed rates, stated without bounds

Version 1 claimed an "achievable bracket" of 2.48%–32.99%. **That claim is withdrawn** (Part III, C1). What exists is three observed rates from three configurations of **one fixed generator**:

| Configuration | Calibration | Forecast | `DepartureTime` | `Duration` |
|---|---|---|---|---|
| **G-A** | causal, prior data only | persistence | **0.00%** | 69.68% |
| **G-B** | causal, prior data only | damped persistence toward causal climatology | **2.48%** | 68.02% |
| **G-L** | whole-record (leaky) | realised future values | **32.99%** | 63.23% |

**No bound on operational forecast performance may be read from these.** G-L is not an upper limit: the generation rules are parameters, and a configuration with a smaller required improvement margin would fire more often with the same information. G-A's 0.00% is below G-B's 2.48%, so the three points do not even order as a bracket. The rates vary with **both** the information available **and** the fixed rule set, and three points cannot separate those. Monotonicity in forecast skill is a plausible expectation, not a demonstrated relation.

Note also that `Duration` moved in the **opposite** direction from `DepartureTime` across configurations — highest under persistence, lowest under the oracle — because realised conditions break runs that persistence predicts continuing.

## Path A — obtain real issue-time forecasts and repeat the study

| Dimension | Assessment |
|---|---|
| **Data availability** | `DepartureTime` needs forecasts resolving hour-to-hour differences inside a five-hour window. The free route — NOAA GFS via Earth Engine (wind, rainfall, 2015→) paired with Copernicus MFWAM (waves, 2022→) — is **3-hourly on waves**, placing at most two points inside the window. **Only ECMWF MARS supplies hourly wave forecasts** (HRES-WAM, hourly to T+90, four cycles daily, covering 2020–2025) |
| **Licensing** | **The hourly route is the worst-licensed.** MARS requires a Service Agreement; the research fee waiver treats dissemination as commercial use, bars redistribution, and fixes attribution wording. **The extracted forecast records could not be published as thesis supplementary data.** The publishable route is 3-hourly on the variable that matters |
| **Evaluation sample size** | Structural ceiling **423** CAUTION episodes in four years (V4); realised divergence 121–146 under the generators tested; clustering into plausibly tens of independent weather events (I1). Sufficient for a feasibility pilot, thin for an effect estimate |
| **Operational availability** | **Path A's one unambiguous gain.** A forecast issued at 18Z and disseminated before 05:00 local satisfies operational availability. Nothing else available to this project does, including everything in the thesis to date |
| **Expected scientific contribution** | Would convert the advisory comparison from chronologically causal to operationally available, and would test I2 directly. But it answers no frozen RQ (I3), and if I2 holds the measurable effect is small. **Unknown rather than low** — which is itself a reason to test A3 before committing |
| **Cost** | Licence negotiation, a collection pipeline, ethics approval, rater recruitment. Months, with the thesis timeline exposed |

### Path A go/no-go criteria — all five must hold

| | Criterion | Why it is decisive |
|---|---|---|
| **A1** | **Hourly** issue-time wave forecasts, ≥3 years, at this site, with issue, valid and lead times resolved | 3-hourly cannot resolve a five-hour window. Fails ⇒ `DepartureTime` stays unreachable whatever else is obtained |
| **A2** | Licence permits publishing the extracted records as supplementary data, **or** the supervisory team accepts a documented non-redistribution exception | A thesis whose central dataset cannot be shared is a reproducibility problem |
| **A3** | **Measured skill of a real wave forecast at 1–4 h intra-window leads, against persistence, by a margin stated in advance** | **The test of I2, and the cheapest criterion.** Persistence is already a strong wave baseline here. If a real forecast cannot beat it inside the window, Path A gains little |
| **A4** | With the real forecast: ≥100 cases where C1 ≠ C2 **and** ≥30 independent weather events among them | Below this the study supports a feasibility report, not an effect estimate |
| **A5** | The result is sited under a declared RQ or a named validity chapter **before** collection begins | It currently populates no chapter. Settling this after collection is the expensive order |

**Test A3 first.** It can close or open Path A on its own, and it requires no licence, no ethics approval and no recruitment to scope.

## Path B — retain the locked scope and document the limitation

| Dimension | Assessment |
|---|---|
| **Fit to the lock** | **Exact.** `final-research-chain-lock.md` records the experiment set as SUFFICIENT and reintroduces neither a fisher study nor prototype implementation as an RQ. **Frozen RQ1–RQ3 are preserved unchanged.** Path B adds no RQ and reopens nothing |
| **What gets written** | The V2 distinction: `A_AI(SAFE)` ranges over one type **unreachable** from the specified inputs and one **reachable but evidentially unsupported**; `A_AI(CAUTION)` withholds exactly those two. Δ_L2 therefore quantifies the withholding of advisory detail that the prototype cannot generate and that the architecture provides no input to support. This sharpens the existing concession at `manuscript.md:1462`, which attributes the gap to the rule set — the mapping-level statement holds for a complete rule set too |
| **Evidence in hand** | V1–V6, the leak-check suite, three case tables, and the measured divergence realisations. Enough for a methods appendix demonstrating the constraint empirically rather than asserting it |
| **Cost** | Forgoes the human study. The structural novelty claim stays conceptual and sample-limited — nine primary sources, non-systematic, single reviewer |
| **Risk** | An examiner asks why the admissible set includes types the system cannot produce or support. **Path B answers that in the thesis; Path A leaves it open longer** |

### Actions if Path B is approved

| | Action | Cost |
|---|---|---|
| 1 | Add the V1 sentence to the thesis and Journal 1 v2 limitations, citing `architecture-illustration.md` §209 | One sentence |
| 2 | Add the V2 reachability-versus-support distinction to Appendix C alongside the open 2.8 m item, with the α coefficients as evidence and the I2 qualification attached | One paragraph |
| 3 | **Run condition G-O** (perfect foresight + causal calibration) as a **diagnostic comparison**. Read-only, existing data, no new artefact. See Part III, C6 for what it can and cannot establish | Hours |
| 4 | Fix the base-rate guard on false-acceptable rate and re-specify E-ES-5 against the internal threshold family, publishing both versions | Hours |
| 5 | State operational availability (Limitation 1) in the abstract of Journal 1 v2 | One sentence |
| 6 | Record A1–A5 as the named entry criteria for the deferred advisory study | One table |

---

# PART III — CORRECTIONS, DEFECTS AND REVISION HISTORY

## Corrections to Version 1 of this memorandum

**C1 — The "achievable bracket" is withdrawn.** Version 1 stated *"the achievable rate lies in (2.48%, 32.99%) and rises with intra-window forecast skill."* Three defects: G-L is not an upper bound on operational performance, because the generation rules are tunable parameters and a different configuration could exceed it with the same information; 2.48% is not a lower bound, since G-A produced 0.00%; and the three configurations differ in **both** calibration and forecast content, so no monotone relation in skill is identified. Replaced by the table of observed rates in Part II, with no bound claimed.

**C2 — The leakage attribution is withdrawn.** The results report said *"~30.5 percentage points of `DepartureTime` availability was leakage."* G-L differs from G-B in two respects — leaky calibration **and** perfect foresight versus a deliberately minimal surrogate — so the gap conflates illegitimate information with one surrogate's skill deficit. The leakage share is **not identified** by these three conditions.

**C3 — The wave α = 0.970 interpretation is qualified.** Version 1 treated it as a property of the site's physics making timing advice unavailable. It is a property of **the fitted surrogate**: within the form `α·y(h) + (1−α)·clim(month, hour)`, a monthly-hourly climatology adds little beyond persistence for wave. It does not establish that wave changes are unforecastable at 1–8 h leads, and an operational wave model represents physics a climatology cannot. Downgraded from a finding to hypothesis I2, with A3 as its test. **This materially re-weighted the recommendation**, which now rests on RQ fit, power, and the resolution/licensing conflict rather than on physics.

**C4 — The 146 cases are not an oracle ceiling.** They are the observed C1 ≠ C2 divergence count for **one fixed generator** (G-L) with perfect foresight and leaky calibration. A differently parameterised generator could realise more. **The genuine structural ceiling is 423 episodes (5.79%)** — the CAUTION count — which follows from the governance mapping and holds for any generator. Restated as V4.

**C5 — The ±3.4 percentage-point interval is indicative only.** It is an **approximate independent-binomial calculation** on 673 episodes treating them as independent draws. They are not: departure-window hours cluster into weather events, and the site's clustering gives 85–123 independent events from 531 CAUTION hours over five years. The effective sample is materially smaller and **the true interval is wider by an unquantified design-effect factor**. It is not an event-cluster-adjusted confidence interval and should not be reported as one.

**C6 — G-O is a diagnostic comparison, not a guaranteed decomposition.** Version 1 said G-L − G-O isolates the calibration leak and G-O − G-B the skill deficit. That presumes additivity and no interaction. Calibration and forecast content **do** interact: the percentile cutoffs are derived from the calibration, and forecast values are mapped through the same empirical distributions, so changing one alters how the other acts. G-O gives an informative contrast that would **bound the calibration contribution under a stated additivity assumption**; it does not uniquely decompose the gap.

**C7 — Correct denominators for the index–state concordance metric.** The rates are conditional, and the block sizes reported alongside them are not their denominators.

| Metric | Denominator | Count | Rate |
|---|---|---|---|
| Permissive mismatch, all cases | episodes with `S` ∈ {CAUTION, UNSAFE} = **3,551** (not 7,305) | ≈2,166 | 60.997% |
| Permissive mismatch, daylight only | `S` elevated **and** `g_t` = SAFE = **673** (not 4,427) | ≈179 | 26.597% |
| Restrictive mismatch, both blocks | episodes with `S` = SAFE = **3,754** | ≈830 | 22.110% |

The restrictive figure is identical in both blocks because `S` = SAFE entails `g_t` = SAFE, making the SAFE set a subset of daylight. That identity is a correctness check on the implementation, and it held exactly.

## Implementation defects

| | Defect | Status |
|---|---|---|
| **D1** | **A leak check reported a pass on zero compared cases** — a vacuous pass, from `Timestamp` and `datetime64` stringifying differently | Fixed; an empty comparison now fails. Defective run preserved |
| **D2** | **A second leak check failed all three conditions on a swallowed `KeyError`**, masking the real signal | Fixed; exception text recorded |
| **D3** | **E-ES-5 passed vacuously for all three conditions.** Its 0.10 false-acceptable bound sits roughly five times above the achievable range on wave, so it can never bind | Reported as failed-by-vacuity; **not** re-specified to obtain a pass |
| **D4** | **False-acceptable rate has no base-rate guard.** `wind > 21.6 kn` has zero exceedances at lead 8, so the rate reports 0.0 from an empty numerator | Open |
| **D5** | **A prediction of mine was refuted.** I predicted the oracle would show non-zero error against physical thresholds; it is 0.0 everywhere, because comparing a variable's forecast to that variable's threshold makes an oracle trivially correct. The mismatch is a property of the acceptability *decision* and was measured by a different metric | Recorded as refuted |

## Cumulative criterion history

| Criterion | Original (pre-registered) | R1 | R2 | R3 | Executed |
|---|---|---|---|---|---|
| N1 type coverage ≥10% | PASS on 9,135 | → E-GC-1 | — | absorbed E-GC-2a | **G-L PASS; G-A, G-B FAIL** |
| N2 divergence ≥20% | FAIL 2.69% | → descriptive | — | — | descriptive, 1.66–2.00% |
| N3 withheld ≥50% | FAIL 46.33% | → ≥30% marker | — | — | G-L, G-A meet; **G-B misses at 28.61%** |
| N4 boundary ≥30% | FAIL 6.17% | → absolute counts | — | — | PASS all (441 / 137 / 121–146) |
| type non-redundancy | — | all pairs | **unpassable, replaced** | **bin-width defect, replaced** | G-A FAIL at exact structural values; G-B PASS |
| divergence direction | — | ≥95% | **true by construction** | verified analytically | **1.000000 in all conditions** |
| skill-ceiling check | — | gate | **diagnostic** | — | no measured benchmark exists |
| availability | — | not distinguished | **A-CHK added** | — | C1 satisfied, C2 not |

**Non-discriminating or defective criteria of mine, cumulative: six** — unpassable (`Delay ≡ ¬Go`), structurally confounded (pooled target hours), true by construction (nested admissible sets), defeated by bin width (within-decile variance), vacuous (E-ES-5), plus two broken leak checks. Every one was found by inspection rather than by a run.

## What this memorandum does not claim

1. No experiment was run for it; no external request was made; no frozen artefact was modified.
2. **No bound on operational forecast performance** is claimed (C1).
3. **The leakage share is not identified** (C2), and G-O would not uniquely decompose it (C6).
4. **I2 is untested.** Path A's unsuitability is a judgement about power, licensing and RQ fit — not a demonstration that useful intra-window wave forecasting is impossible. A3 could overturn it.
5. The daylight mismatch figure rests on 673 episodes with an interval wider than the ±3.4 points quoted (C5).
6. Everything is PRIMARY (ERA5), single site, single configuration, exploratory.
