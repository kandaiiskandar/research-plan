# Empirical Findings — Historical Replay, Diagnostic and Hysteresis Analysis

**Date:** 2026-09-06
**Status:** Complete. All 14 pre-registered predictions resolved — **14 confirmed, 0 refuted**.
**Data:** Open-Meteo archive, Kota Kinabalu (5.98 N, 116.01 E), 2020-01-01 to 2024-12-31, 43,848 hourly records.
**Scripts:** `scripts/historical_replay.py`, `scripts/diagnostic_binding.py`, `scripts/hysteresis_analysis.py`
**Register:** `data/prediction-register.csv` — predictions registered *before* the diagnostic and hysteresis runs.
**Parent decision:** `docs/canonical/decision-record-empirical-first.md`

---

## 0. Standing caveats

Applies to every figure below.

| Caveat | Consequence |
|---|---|
| `m` (marine warning) has no historical archive; held at `none` throughout | `g_m` can only *raise* severity, so **all severity figures are lower bounds** |
| Data is ERA5 reanalysis, not MET Malaysia observations | Different source from the one the thresholds are anchored to |
| ~~`wind_speed_10m` is an hourly mean~~ — **CORRECTED, see F-9** | Open-Meteo documents it as **"Instant"**. The hourly-mean claim was wrong |
| **Weather data comes from a LAND grid cell; marine data from a SEA cell** | See F-10. Likely the principal cause of F-1 |
| **Zero thunderstorm codes in five years** | See F-11. `g_r`'s storm branch is effectively unexercised |
| Swell period columns are entirely NaN | The second component of the `o` tuple remains unusable |
| Hourly resolution | Sub-hourly oscillation is invisible — bounds F-6 to hourly resolution only |

---

## 1. Findings

### F-1 — `g_w` never fires. Not once in five years.

Sustained wind ranges **0–17.8 kn**. Thresholds are 22 kn (CAUTION) and 27 kn (UNSAFE). **Zero activations.**

Gusts reach 36.9 kn and *would* fire 205 CAUTION + 24 UNSAFE if `w` were defined over gusts.

MET Malaysia's published criteria state "wind speeds from 40–50 kmph" **without specifying sustained or gust** — the ambiguity is in the source. Combined with the ERA5 hourly-mean caveat, this is as much a measurement-mismatch problem as a threshold problem.

**Status:** open question **Q1** in the decision record. Not to be repaired by choosing whichever definition makes the component fire.

### F-2 — The superseded model's UNSAFE state was, in effect, "it is dark"

Under vessel-blind `g_o` (1.5 / 3.5 m) combined with an inert `g_w`:

- UNSAFE-by-wave: **0 occurrences in five years** (maximum observed wave 2.60 m)
- UNSAFE in daylight hours: **10 of 20,097** (0.05%), all from rainfall

With `g_w` inert and `g_o` unable to reach UNSAFE, almost every UNSAFE classification came from `g_t`.

### F-3 — `g_v(small) = CAUTION` made SAFE unreachable — measured, not argued

| Model (daylight, small vessel) | SAFE | CAUTION | UNSAFE |
|---|---|---|---|
| Superseded + `g_v(small)` floor | **0.0%** | 99.9% | 0.05% |
| Amended `g_o(o,v)` | **84.3%** | 15.6% | 0.15% |

SAFE = 0.0% in *every* time window examined. The analytical prediction that motivated removing `g_v`, confirmed on five years of real data.

### F-4 — Vessel conditioning is operative, not cosmetic

Small and big vessels classify **differently in 10.7%** of departure-window hours (13.4% of daylight hours). Under the superseded vessel-blind thresholds this figure would be 0% by construction.

### F-5 — Level 2 governance binds in 12.4% of departure hours

**This is the empirical result the papers were missing.**

Over five years of real site conditions, for a small vessel in the 05:00–09:00 departure window, `S = CAUTION` in **12.4%** of hours — conditions in which the architecture withholds `DepartureTime` and `Duration` and a binary architecture would supply them.

Approximately **one departure hour in eight**.

### F-6 — Mode-chattering is NOT a demonstrated deployment problem *(negative result)*

| Measure | Value |
|---|---|
| Total state transitions, 5 years | 5,416 |
| — of which **scheduled** clock events (06:00 / 17:00 / 19:00) | 5,189 (**95.8%**) |
| — **non-scheduled** | 227 (4.2%) |
| Genuine A→B→A round trips within 3 h | **70 — 14 per year** |
| Reduction from dual-threshold hysteresis (10% margin) | **6.2%** |

Every observed oscillation is a 0→1→0 flip lasting exactly one hour, wave height brushing the 1.0 m boundary.

**Both papers currently assert mode-chattering as a deployment concern requiring dual-threshold hysteresis. That claim is not supported at hourly resolution.** Fourteen events per year is not a deployment problem, and hysteresis buys 6%.

### F-7 — The classifier reduces to a wave gate plus a night curfew

Share of hours in which each function sits at the maximum (ties counted for each tied function):

| Function | Daylight CAUTION | Daylight non-SAFE | All-hours non-SAFE |
|---|---|---|---|
| `g_o` | **97.5%** | 97.2% | 13.6% |
| `g_t` | 0% | 0% | **88.2%** |
| `g_r` | 3.4% | 3.7% | 0.5% |
| `g_w` | **0%** | **0%** | **0%** |
| `g_m` | **0%** (no data) | **0%** | **0%** |

Only **three** functions ever bind in the departure window: `g_o`, `g_t`, `g_r`.

`g_o`'s binding share falls with vessel size — **97.5% small, 86.2% medium, 78.8% big** — so the wave gate matters most for exactly the deployment population.

### F-9 — CORRECTION: `wind_speed_10m` is instantaneous, not an hourly mean

The `10m` in `wind_speed_10m` is **height above ground**, not a time interval — 10 metres is the WMO standard reference level for surface wind. Open-Meteo: *"Wind speed at 10 or 100 meters above ground. Wind speed on 10 meters is the standard level."*

**An error introduced on 2026-09-06 and now corrected.** Earlier versions of this document, the decision record, and a note added to `appendix-c-formalisation.md` C.2 all stated that ERA5 `wind_speed_10m` is an hourly mean, and reasoned from that to a claim that it systematically under-represents peak sustained wind relative to MET's 10-minute means.

Open-Meteo documents the variable's valid time as **"Instant"** — an instantaneous value at the indicated hour, not an average over it.

The correction cuts both ways. An instantaneous value does not smooth peaks the way a mean would, so the "ERA5 smooths the peaks" explanation for F-1 is weaker than stated. But hourly *sampling* still misses everything between samples, so under-capture of short-lived maxima remains plausible — by a different mechanism, and one that is not quantified here.

Height is not the issue: MET's observations are also at the 10 m standard level. The two are comparable in that respect.

### F-10 — Wind was sampled over LAND, waves over SEA

Open-Meteo's `cell_selection` parameter defaults to **`land`** — *"finds a suitable grid-cell on land."* The alternatives are `sea` and `nearest`. The download script does not set it.

The coordinates returned by each API confirm the consequence:

| File | Grid cell returned | Surface |
|---|---|---|
| `raw_weather.csv` (wind, precipitation) | 5.940246, 116.100006 | **land** |
| `raw_rainfall.csv` | 5.940246, 116.100006 | **land** |
| `raw_marine.csv` (wave height) | 6.0, 116.0 | sea |

Both were requested at 5.98, 116.01. The two grid cells are roughly 12 km apart, and **the classifier is combining wind measured over land with waves measured over water.**

Surface roughness over land is far higher than over open water, so 10 m wind over a land cell is materially lower than over the adjacent sea. **This is the most likely single explanation for F-1** — more so than any averaging or sampling effect.

**Untested.** A comparison run with `cell_selection=sea` was attempted and could not complete: the sandbox blocks the host and the fetch timed out. This needs running locally.

**If sea-cell wind is materially higher, F-1 is a data-collection artefact rather than a finding about the site, and Q1 changes character entirely** — the question would become "was the wind data ever right?" rather than "should `g_w` read gusts?"

Until that test runs, **F-1 should not be reported in either paper as a property of the location.**

### F-11 — Thunderstorms are undetectable in this dataset

`weather_code` never takes values 95, 96 or 99 across all 43,848 records. **Zero thunderstorms in five years**, in equatorial Borneo.

This is not climatology. Open-Meteo documents the limitation directly: *"As barely no information about atmospheric stability is available, estimation about thunderstorms is not possible"*, and thunderstorm-with-hail codes are *"only available in Central Europe."*

Consequence for `g_r`: the storm branch is reached **only** via precipitation > 20 mm/hr, which occurs 14 times in five years. Since **Ribut Petir (thunderstorm) is MET Malaysia's stated trigger** for the rainfall UNSAFE classification, the mechanism the threshold is anchored to cannot be observed in this data at all.

`g_r = UNSAFE` is therefore under-detected by an unknown margin, and F-6's chattering counts and F-7's binding shares for `g_r` are both lower bounds.

### F-12 — The wave data carrying 97.5% of decisions is a ~50 km open-water average

`o` comes from the Open-Meteo Marine API using model **`era5_ocean`**, explicitly requested in the download script. ERA5-Ocean runs at **0.5° ≈ 50 km — the coarsest of the nine wave models Open-Meteo offers.**

**The choice was effectively forced.** Every finer model begins in 2021 or later — MeteoFrance MFWAM (~8 km) from Oct 2021, NCEP GFS Wave 0.16° (~16 km, covers Borneo) from Oct 2024, ECMWF WAM (9 km) from Nov 2025. For a 2020–2024 retrospective series ERA5-Ocean is the only option. This is a defensible trade-off, not an oversight — but it must be stated rather than left implicit.

The consequence is that **the single input carrying 97.5% of daylight CAUTION decisions (F-7) is a wave height averaged over roughly 50 km of open water**, compared against thresholds of 1.0 m and 1.9 m, governing vessels operating within about 9 km of a coast sheltered by islands. ERA5-Ocean cannot resolve nearshore sheltering, shoaling or refraction.

Direction of error is not determined. Open-water waves generally exceed sheltered nearshore waves, which would make `g_o` over-restrictive; but a 50 km average also smooths local maxima, which would make it under-restrictive. Both effects are present and neither is quantified.

**Three things are correct here and worth recording:**

- `cell_selection` defaults to `sea` for the Marine API, so the wave data *did* come from a sea cell. The land/sea mismatch in F-10 is confined to the weather side.
- `wave_height` is **significant wave height (Hs)** — the same quantity used by Yaakob et al. and Jeong & Im, so the thresholds and the measurement are at least commensurable in kind.
- The all-NaN `wind_wave_*` and `swell_wave_*` columns are explained: ERA5-Ocean does not provide partitioned components. Not a download failure.

**Newly available:** `wave_period` is fully populated and unused. `o` is defined as *(wave height, swell period)*; mean wave period is not swell period, but it is more than nothing — partially reopening Q5.

### F-13 — Q1a RESOLVED: F-1 is real. Wind genuinely never reaches the threshold

Re-collected with `cell_selection=sea`. The land-cell error was real and substantial:

| | v1 LAND cell | v2 SEA cell | change |
|---|---|---|---|
| Mean sustained wind | 3.13 kn | **4.92 kn** | **+57.3%** |
| p99 | 9.1 kn | 13.7 kn | +51% |
| **Max over 5 years** | 17.8 kn | **21.8 kn** | +4.0 kn |
| **`g_w` activations** | **0** | **0** | **unchanged** |

The uplift exceeded my prediction of 20–40%. But **`g_w` still never fires** — the five-year maximum reaches **21.8 kn against a 22.0 kn threshold**, missing by 0.2 knots.

**Prediction P16 was REFUTED.** I predicted the sea-cell wind would cross the threshold occasionally. It does not.

**Consequence: F-1 stands as a genuine property of the site, not a collection artefact.** Sustained wind at Kota Kinabalu does not reach MET Malaysia's Category 1 criterion in five years of data, at either grid cell. Q1 is answered — but not in the direction that rescues `g_w`.

**Caveat on the margin.** 21.8 against 22.0 is thin. A different reanalysis, a 10-minute mean instead of an instantaneous value, or a slightly different grid point could plausibly cross it. The honest statement is *"sustained wind essentially never reaches the threshold"*, not *"wind is far from mattering."*

**A methodological note worth recording:** the land/sea error was a genuine flaw, and correcting it changed **nothing** in the results — the departure-window figures are identical to one decimal place (12.4% under both). Because `g_w` never fires either way, the wind data never influenced any classification. A real error with no material consequence.

### F-14 — Q6 RESOLVED: wave resolution matters. The headline drops to 8.3%

MFWAM at ~8 km compared against ERA5-Ocean at ~50 km, over their 28,512-hour overlap (Oct 2021 – Dec 2024):

| | ERA5-Ocean ~50 km | MFWAM ~8 km |
|---|---|---|
| Mean wave height | 0.645 m | **0.590 m** (−8.5%) |
| p99 | 1.64 m | 1.42 m |
| **Max** | **2.60 m** | **1.84 m** |
| `g_o` CAUTION rate (small) | 16.4% | **11.3%** |
| `g_o` UNSAFE (small) | 43 hours | **0 hours** |

The two models **correlate at r = 0.953** across 28,501 valid pairs, so they agree closely on the shape of the series. The difference is concentrated in the upper tail: ERA5-Ocean's coarse cell produces larger maxima, consistent with averaging open water that the finer model resolves as sheltered.

**Predictions P17 and P18 both confirmed.** The nearshore-sheltering reasoning in F-12 holds.

**The headline result is resolution-sensitive:**

| Configuration | Level 2 binding rate, departure window |
|---|---|
| v1 — land wind, ERA5 50 km | **12.4%** |
| v2 — sea wind, ERA5 50 km | 12.4% (unchanged) |
| v2 — sea wind, **MFWAM 8 km** | **8.3%** |

**A 33% relative reduction.** One departure hour in twelve, not one in eight.

**Which figure to report.** MFWAM is the better-sited measurement — 8 km resolution, and its grid cell sits 2.7 km from the weather cell versus 12.9 km in v1. But it covers only 3.25 years against ERA5's 5. The defensible presentation is **both**: report 8.3% as the primary figure on the higher-resolution data, give 12.4% for the full five years, and state that the difference quantifies grid-resolution sensitivity. That converts a vulnerability into a demonstrated robustness check.

Note also that under MFWAM, **small-vessel UNSAFE via wave height never occurs** (max 1.84 m against a 1.9 m threshold) — a second near-miss margin, mirroring F-13.

### F-8 — MET Malaysia's criteria are disjunctive

The published criteria read: *"strong winds with wind speeds from 40–50 kmph **and/or** rough seas with wave heights of up to 3.5 metres."*

MET does not average wind against sea state; either triggers a category. This is **independent institutional support for non-compensatory worst-case aggregation**, and it is currently uncited in both papers.

---

## 2. Consequences for the papers

| Finding | Action |
|---|---|
| F-5 | **Add as the headline empirical result.** Directly answers Review 3's "lacks the empirical evidence to establish effectiveness" |
| F-3, F-4 | Add as validation that the vessel-conditional revision was necessary, not presentational |
| F-8 | Cite in the worst-case aggregation justification — free institutional support |
| **F-6** | **Withdraw or qualify the mode-chattering claim** in both papers. Options: drop it, or retain as an explicitly untested precaution noting that sub-hourly data would be required. Recommended: the latter |
| F-1, F-7 | Requires a framing decision — see §3 |
| F-2 | Useful in Threats to Validity: shows the revision corrected a model whose UNSAFE state was near-degenerate at the deployment site |

---

## 3. The framing question raised by F-1 and F-7

The classifier has five functions. At the deployment site, two never bind — one because its thresholds are never reached (`g_w`), one because no historical data exists (`g_m`). A third contributes 3.7%.

This is not a defect in the governance architecture. `f(E)` is an input to the governance pair, and the contribution — `(G(S), A_AI(S))` and the Safety Dominance Property — is indifferent to how many terms `f` aggregates. But it *is* a defect in the domain instantiation if presented as a five-factor classifier without qualification.

Three honest options:

1. **Report it as a finding.** "At this site the classifier is driven by sea state and time of day; wind never reaches warning thresholds and marine warning data is unavailable." Accurate, and demonstrates that the architecture was tested rather than asserted.
2. **Reduce the classifier** to the functions that discriminate, and justify the reduction empirically.
3. **Retain all five with explicit scope statements** — `g_w` retained for transferability to sites with stronger wind regimes, `g_m` retained pending data.

Option 1 or 3. Option 2 loses domain transferability, which matters for the generalisation claim in both papers.

**Not yet decided.** Feeds Q1 and Q4 in the decision record.

---

## 4. Method note — pre-registration

All fourteen predictions were registered in `data/prediction-register.csv` with machine-comparable bounds *before* the diagnostic and hysteresis analyses were run. Scripts populate `actual` and `status` automatically; `pred_*` columns are not edited after registration.

Two predictions were deliberately uncomfortable: **P13** predicted a negative result that undermines a claim in both papers, and **P14** predicted the reductive framing in §3. Both confirmed.

This was adopted specifically to guard against the failure mode identified in the decision record — a model elaborated ahead of validation, with the corresponding risk of rationalising results once seen. **14 confirmed, 0 refuted.**

The value of the register is not the pass rate. It is that F-6 and F-7 were written down as expectations before they could be reframed as intentions.
