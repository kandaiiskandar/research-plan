# Finding: `g_t` Counterfactual Sensitivity Analysis — Models A, B, C

**Date:** 2026-09-08
**Status:** **Counterfactual only. Nothing canonical changed.** `g_t`, Appendix C, the canonical scripts, the published figures (7.72% / 5.98%) and the prediction register (22 confirmed / 2 refuted) are all unmodified. No prediction re-resolved.
**Predecessors:** `finding-gt-provenance-audit.md` (the values have no source) · `finding-gt-operational-semantics.md` (COLREGs Rule 20(b) defines the boundary as sunset-to-sunrise; evidence supports two states, not three).
**Analysis code:** `scripts/sensitivity/solar.py`, `scripts/sensitivity/gt_counterfactual.py` — **new, isolated, non-canonical.** Neither writes to the register nor emits canonical figures.

---

## 1. Headline

**Model B costs less than expected. Model C costs far more — and for a reason that discredits it.**

| | Level 2 binding, PRIMARY | Δ | RESOLUTION | Δ |
|---|---|---|---|---|
| **A** incumbent fixed clock | **7.72%** | — | **5.98%** | — |
| **B** sunrise/sunset, two-state | **5.81%** | **−1.90 pp** | **4.48%** | **−1.50 pp** |
| **C** civil twilight, three-state | **19.59%** | **+11.88 pp** | **18.94%** | **+12.96 pp** |

**Model C's +12 pp is an artefact of window overlap, not a safety finding.** Civil dawn at this site falls between **05:37 and 06:11**, and the departure window is **05:00–09:00**. The dawn twilight band therefore lands squarely inside the measurement window, and Model C reclassifies most early-window hours from UNSAFE to CAUTION. The Level 2 rate triples because the CAUTION band was moved into the window being measured — not because the site became more marginal.

**Model B is the only model where the headline moves for a defensible reason:** it removes `g_t`'s CAUTION state entirely, so every remaining CAUTION hour comes from `g_o` or `g_r`.

---

## 2. Models as implemented

| | Definition | Status |
|---|---|---|
| **A** | SAFE 06:00 ≤ t < 17:00 · CAUTION 17:00 ≤ t < 19:00 · UNSAFE else | Incumbent. Unchanged |
| **B** | SAFE sunrise ≤ t < sunset · UNSAFE else. **No CAUTION from `g_t`** | Regulation-derived (COLREGs Rule 20(b)) |
| **C** | SAFE sunrise ≤ t < sunset · CAUTION [civil dawn, sunrise) ∪ [sunset, civil dusk) · UNSAFE else | **Exploratory only.** The CAUTION interpretation is *not* evidence-supported — see the operational-semantics finding §6 |

**Controls held fixed, as required:** `g_w` (21.6/27.0), `g_r` (10.0/20.0), `g_m` (pinned SAFE, D = {m}), `g_o` (1.0/1.25 small vessel), max-severity aggregation, both dataset configurations, small-vessel assumption, departure window 05:00–09:00. **The only thing varied is `g_t`.**

---

## 3. Full results

### PRIMARY — 43,848 hours, 5.00 yr, ERA5-Ocean

| Measure | A incumbent | B sun | C civil |
|---|---|---|---|
| **1–2. State distribution** | | | |
| SAFE hours | 16,990 (38.75%) | 18,424 (42.02%) | 18,424 (42.02%) |
| CAUTION hours | 5,375 (12.26%) | **2,091 (4.77%)** | 3,564 (8.13%) |
| UNSAFE hours | 21,483 (48.99%) | 23,333 (53.21%) | 21,860 (49.85%) |
| **3. `g_t` activations** | 23,751 (54.17%) | 22,074 (50.34%) | 22,074 (50.34%) |
| **4. `g_t` EXCLUSIVE binding** | **81.99%** | 81.80% | 81.25% |
| **5. `g_t` tied-at-maximum** | 87.63% | 86.82% | 86.48% |
| **6. Overlap — another component ≥ `g_t`** | | | |
| `g_w` ≥ `g_t` | 0 | 0 | 0 |
| `g_r` ≥ `g_t` | 14 | 13 | 13 |
| `g_m` ≥ `g_t` | 0 | 0 | 0 |
| `g_o` ≥ `g_t` | 1,717 | 1,264 | 1,405 |
| **7. SAFE→CAUTION by `g_t`** | 1,545 | **0** | 176 |
| **8. CAUTION→UNSAFE by `g_t`** | 1,724 | 186 | 365 |
| **9. SAFE→UNSAFE (any cause)** | **2** | **1,536** | 1,360 |
| — of which by `g_t` | 0 | 1,534 | 1,358 |
| **10. `g_t` transitions/day** | 2.73 | 1.88 | 2.61 |
| Total transitions | 5,201 | 3,661 | 4,995 |
| **11. LEVEL 2 BINDING (05–09)** | **7.72%** | **5.81%** | **19.59%** |

### RESOLUTION — 28,501 hours, 3.25 yr, MFWAM *(item 12)*

| Measure | A incumbent | B sun | C civil |
|---|---|---|---|
| SAFE / CAUTION / UNSAFE % | 40.87 / 11.56 / 47.57 | 44.04 / **3.89** / 52.07 | 44.04 / 7.54 / 48.42 |
| `g_t` activations | 15,438 (54.17%) | 14,386 (50.48%) | 14,386 (50.48%) |
| `g_t` exclusive binding | 87.19% | 87.11% | 86.71% |
| `g_t` tied-at-max | 91.10% | 90.20% | 90.02% |
| SAFE→CAUTION by `g_t` | 1,041 | **0** | 170 |
| CAUTION→UNSAFE by `g_t` | 1,148 | 102 | 275 |
| SAFE→UNSAFE (any) | 2 | 1,045 | 875 |
| `g_t` transitions/day | 2.82 | 1.94 | 2.76 |
| **LEVEL 2 BINDING** | **5.98%** | **4.48%** | **18.94%** |

---

## 4. What the numbers show

**The 87.63% survives every model.** `g_t` is tied-at-maximum in 86.5–87.6% of non-SAFE hours regardless of semantics, and **exclusively binding in 81–82%**. The provenance audit flagged that the published figure was an at-maximum share; it is now measured both ways, and **the exclusive figure is only ~6 pp lower**. `g_t`'s dominance is a property of the site — 11–12 hours of darkness daily against weather that is rarely severe — not an artefact of where the boundaries sit.

**Model B eliminates time-driven CAUTION entirely.** SAFE→CAUTION transitions caused by `g_t` fall from 1,545 to **exactly 0**, by construction. CAUTION hours drop 61% (5,375 → 2,091), and what remains is genuinely weather-driven. This is the cleanest structural result in the analysis: under B, **every CAUTION hour in the model is a weather CAUTION.**

**Model B converts graduation into a step.** Direct SAFE→UNSAFE transitions rise from **2 to 1,536**. Under A, the architecture almost never jumps two levels; under B it does so twice daily at sunrise and sunset. Whether that is a defect depends on what the CAUTION state is *for* — if it exists to give the operator warning of a coming withdrawal, B removes that warning for the most predictable transition of the day. **This is the strongest argument against B and it is a design argument, not an evidential one.**

**Model C's headline movement is a measurement artefact.** Civil dawn 05:37–06:11 sits inside the 05:00–09:00 departure window. C's Level 2 rate of 19.59% is largely the dawn band being counted, and it would move again under any other window. **The figure is not comparable to A's 7.72% and should not be presented as though it were.**

**`g_t` and `g_o` rarely conflict.** `g_o` is at or above `g_t` in only 1,717 hours under A (3.9%). `g_w` and `g_m` never are — `g_w` because it activates twice in five years, `g_m` because it is pinned SAFE by the exclusion set. The classifier is `g_t` and `g_o` operating in almost disjoint regimes.

---

## 5. Prediction sensitivity — **not re-resolved**

⚠️ **Configuration caveat.** P09–P13 were registered against **v1 land-cell data**; this analysis runs on sea-cell data. The incumbent column below is therefore *not* the registered actual. Both are shown.

> ### ⚠️ Annotation added 2026-09-08 (C-7). **Table text unchanged; its "Registered actual" column is mislabelled.**
>
> The values in the "Registered actual" column below — **P07 88.23 · P10 227 · P11 70 · P12 6.17** — are **not** the prediction register's values. They are a **coherent snapshot of the pre-amendment threshold vintage** (v1 data, `r_CAUTION = 7.5 mm/hr`, small-vessel `o_UNSAFE = 1.9 m`), and all four reproduce exactly under it. **The register holds the current-threshold values: 87.58 · 230 · 37 · 7.83**, which also reproduce exactly.
>
> | | Register | Quoted here | Both reproduce? |
> |---|---|---|---|
> | P07 | **87.58** | 88.23 | ✅ different vintages |
> | **P09** | **5,416** | 5,416 | ⚠️ the register value *is* the pre-amendment one; current-threshold baseline **5,220** |
> | P10 | **230** | 227 | ✅ |
> | P11 | **37** | 70 | ✅ |
> | P12 | **7.83** | 6.17 | ✅ |
>
> **These are not errors of arithmetic.** They are one superseded specification quoted as though it were the register. **This finding is retained unchanged as the record of what was computed on 2026-09-08**; the authoritative baselines for C-6 are in `data/c7/baseline-provenance.csv` and `report-c7-closure-2026-09-08.md`. **P12 is no longer "not computed" — C-5 computed it: 7.83 → 8.70 → 10.36.**

| Prediction | Registered statement | Registered actual | A (this analysis) | B | C | Would the outcome change? |
|---|---|---|---|---|---|---|
| **P07** | `g_t` share of all-hours non-SAFE **> 70%** | 88.23% ✅ | 87.63% | 86.82% | 86.48% | **No.** Confirmed under all three |
| **P09** | total transitions **5,400–8,000** | 5,416 ✅ | 5,201 | **3,661** | 4,995 | **Yes under B and C — and already under A.** All three fall below 5,400 on sea-cell data. *P09's band was v1-specific; this is a data-configuration effect, not a `g_t` effect* |
| **P10** | non-scheduled transitions **< 500** | 227 ✅ | 207 | 222 | 222 | **No.** Confirmed under all three |
| **P11** | A→B→A oscillations within 3 h **< 100** | 70 ✅ | 27 | 26 | 26 | **No.** Confirmed under all three |
| **P12** | hysteresis reduction **5–40%** | 6.17% ✅ | ❌ **not computed** | ❌ | ❌ | **Unknown.** Requires a full hysteretic re-run per model — not performed, not invented |
| **P13** | mode-chattering **NOT** a demonstrated problem | NO ✅ | Supported (27 osc) | Supported (26) | Supported (26) | **No.** Conclusion holds under all three |
| **P14** | classifier reduces to a **wave gate + night curfew** | YES ✅ | Holds | **Holds more strongly** — `g_t` is purely a curfew under B | Holds | **No**, but B makes the "curfew" reading literal by removing time-CAUTION |
| **P19 / P20** | Level 2 binding 6.1%; daylight UNSAFE 409 h | ✅ | window/daylight defined by `g_t` | changes | changes | **Yes** — both are `g_t`-window-dependent |
| **P22 / P23 / P24** | C1↔C2, C0↔C2, C0↔C1 divergence | P22 ❌, P23 ✅, P24 ✅ | — | changes | changes | **Yes** — all are departure-window figures |

**P16 and P01 are unaffected** — `g_w` activations do not depend on `g_t`.

---

## 6. Affected figures if a model were adopted

Every figure in `empirical-findings-2026-09-06.md` §0a that is time-windowed or state-distribution-dependent: Level 2 binding rate (both configs); daylight UNSAFE hours and share; weather-driven share of UNSAFE; `g_t` and `g_o` binding shares; small-vs-big departure divergence; the complete C0/C1/C2/C3 divergence matrix (all four conditions share `g_t`); F-6's transition and oscillation counts; F-7's binding table.

**"Daylight" would itself need redefining.** The daylight window is currently *defined* as `g_t` = SAFE (06:00–17:00). Under B it becomes sunrise–sunset, so "daylight UNSAFE hours" changes meaning as well as value.

---

## 7. Provenance of the solar times — **and its limitation**

**Method:** NOAA Global Monitoring Laboratory solar-position equations (Astronomical Almanac low-precision formulae), implemented in `scripts/sensitivity/solar.py`. Deterministic, dependency-free, no network access. Sunrise/sunset at solar zenith **90.833°** (refraction + semi-diameter); civil dawn/dusk at **96°**. Site 5.98° N, 116.07° E, UTC+8.

> **Note added 2026-09-08 (C-0 sweep) — text unchanged, terminology clarified.** This sentence was checked, not assumed, during the C-0 correction. **It is free of the C-0 defect: it does not name Meeus and does not conflate Meeus with NOAA**, which is why it alone was left standing while `finding-gt-evidence-closure.md` had to be corrected in three places.
>
> Its parenthetical is nonetheless **imprecise**, and is recorded as such. It attributes the code to two distinct sources at once — NOAA GML calculator equations *and* the *Astronomical Almanac* low-precision formulae — and the code's actual form (a truncated Fourier series in the day angle `Γ = 2π(doy−1)/365`) is not established in this project as matching either as published. The agreed conservative term is **"NOAA-style low-precision solar-position formulation implemented in `scripts/sensitivity/solar.py`"**. **The wording here is deliberately left as written**: C-0 licenses correcting statements that repeat the Meeus defect, not a general terminology rewrite. Pinning the exact published reference is **C-1**.

**Validation against published values for Kota Kinabalu:**

| | Computed | Published (timeanddate) |
|---|---|---|
| Sunrise range | 06:00 – 06:33 | 06:01 – 06:34 |
| Sunset range | 17:56 – 18:35 | 17:57 – 18:35 |
| Civil dawn / dusk | 05:37 – 06:11 / 18:18 – 18:57 | — |
| Mean twilight duration | 21.7 min | — |

**Agreement within one minute at both extremes.**

> ### ⚠️ Reproducibility limitation — flagged as instructed
>
> **This solar source is adequate for sensitivity analysis and is *not* adequate for the canonical model.** Three reasons:
>
> 1. **No authoritative backing.** The NOAA formulae are standard and the implementation validates to ±1 min, but a canonical threshold should cite an official ephemeris — **MET Malaysia**, the **USNO Astronomical Applications** service, or a published nautical almanac — not a re-implementation.
> 2. **The validation reference was a commercial website.** timeanddate.com is reliable in practice and carries no authority. It was used to check the computation, not to supply values, and no scraped value entered the analysis.
> 3. **Unmodelled terms.** Atmospheric refraction is treated as a constant 34′; observer elevation, local horizon obstruction and pressure/temperature variation are ignored. All are sub-minute at this latitude, but none is documented in a citable source.
>
> **If B or C is adopted, the solar source must be replaced with an authoritative one before any figure is published.** Doing otherwise would repeat the 7.5 mm/hr error in a new variable.

---

## 8. Recommendation

**Model B is the most defensible basis for the next specification decision — with one unresolved design question that this analysis cannot settle.**

**For B:**

- **The only regulation-derived option.** COLREGs Rule 20(b) — "from sunset to sunrise" — is binding on these vessels and names exactly this boundary. Neither A nor C has any regulatory basis.
- **Matches the evidence structure.** The operational-semantics review found support for two states and none for a time-based intermediate. B is two-state; A and C both assert a CAUTION band nothing supports.
- **Moves the headline modestly and in the honest direction** — 7.72% → 5.81%, a *reduction*, consistent with every prior provenance correction in this project.
- **Site-transferable by construction**, computed from (date, lat, lon), which the transferability claim in both papers requires.
- **Fixes the concrete defect:** under A, SAFE begins at 06:00, before sunrise every day of the year.

**Against B, and unresolved:**

- **Direct SAFE→UNSAFE transitions rise from 2 to 1,536.** The architecture's own thesis is that graduated governance beats a binary step. Under B, the most predictable transition of the day becomes a step. This does not make B wrong — `g_t` may simply not be a graduated variable — but it should be decided explicitly, not absorbed.

**Against C:**

- **Its CAUTION band is unsupported** (operational-semantics §6) and was adopted here only to test it.
- **Its headline figure is not comparable** — the +12 pp is dawn-band/departure-window overlap.
- If a graduated time band is wanted, C is the *mechanism*, but it needs its own evidence, which does not currently exist.

**Against A:** no source for any of its three values; 06:00 precedes sunrise year-round; 17:00 precedes sunset by 1–1.5 h.

**Recommended next step, if any:** decide the design question — **should `g_t` be graduated at all?** — before choosing a model. If yes, C becomes the mechanism and needs evidence for the CAUTION band. If no, B is straightforwardly the answer and the two-state `g_t` should be stated as a deliberate asymmetry with the other components.

---

## 9. Stop condition — verified

`g_t` unchanged · Appendix C unchanged · canonical scripts unchanged · register unchanged (24 predictions, 22 confirmed / 2 refuted) · headline figures unchanged (7.72% / 5.98%) · no prediction re-resolved · no historical outcome overwritten.

New files are confined to `scripts/sensitivity/` and this finding.
