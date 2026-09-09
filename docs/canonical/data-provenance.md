# Data Provenance — What Each Variable Actually Comes From

**Created:** 2026-09-06
**Why this exists:** three separate data-provenance problems (F-10, F-11, F-12) were found in one afternoon by ad-hoc checking. None was recorded anywhere. This document is the single place to check before trusting any figure derived from `data/`.

**Rule:** before citing any empirical result, confirm the variables it depends on are fit for the threshold they are compared against. The "Fit for threshold?" column is the one that matters.

---

## 1. The central provenance mismatch

> **The thresholds come from MET Malaysia. The measurements come from ERA5 reanalysis.**

`docs/implementation/data-source-met-malaysia.md` §5.1 names MET Malaysia's *Kawasan Perairan* as "the primary data source for prototype and evaluation." It is not what the five-year analysis used. It could not be — that page carries only a rolling 7-day forecast with **no historical archive**, so retrospective data had to come from elsewhere.

Consequence: every threshold comparison in the empirical work checks **ECMWF model output against criteria written for MET Malaysia's own observations**. Two different organisations, potentially different measurement conventions, definitely different instruments. This is the thread connecting F-1, F-9 and F-10, and it must be stated in both papers' Threats to Validity.

---

## 2. Variable-by-variable

### w — wind speed

| | |
|---|---|
| **Source** | Open-Meteo Historical Weather API — `archive-api.open-meteo.com/v1/archive` |
| **Underlying** | ERA5 / ECMWF IFS reanalysis (Best Match: IFS 9 km for 2017+) |
| **Variable** | `wind_speed_10m`, unit knots |
| **"10m"** | **Height above ground** — the WMO standard reference level. Not a time interval |
| **Valid time** | **Instant** — a snapshot at the indicated hour, not an hourly mean |
| **Grid cell — v1** | **LAND — 5.940246, 116.100006** (`cell_selection` unset, defaults to `land`) |
| **Grid cell — v2** | **SEA — 5.940246, 116.025** (`cell_selection=sea`), file `raw_weather_sea.csv` |
| **Fit for threshold?** | ✅ **RESOLVED — see F-13.** v2 collected with a sea cell: mean wind **+57.3%** (3.13 → 4.92 kn), max 17.8 → **21.8 kn**. Against the canonical **21.6 kn** CAUTION boundary (MET Cat 1 onset 40 km/h = 21.598 kn), `g_w` **activates twice** in 43,848 hours — readings of 21.7 and 21.8 kn — and **binds in neither**, a more severe component already governing on both occasions. **Use `raw_weather_sea.csv` going forward.** *(Corrected 2026-09-09: this cell previously read "activations remain 0 — the threshold is 22.0 kn, missed by 0.2 … `g_w` never fires either way". The 22.0 was an undocumented rounding; at the source value the activations exist. See F-17.)* |

Also available and unused: `wind_gusts_10m` (max 36.9 kn, would fire 205 CAUTION / 24 UNSAFE).

### r — rainfall intensity

| | |
|---|---|
| **Source** | Same as `w` — `raw_weather_sea.csv`, the v2 **sea** cell (5.940246, 116.025). *(Corrected 2026-09-09: read "Same as `w` (land cell)". Wind moved to the sea cell at v2 and precipitation moved with it, since both are columns of the same file.)* |
| **Variables** | `precipitation` (mm, preceding-hour **sum**) — the **required** rate coordinate; `weather_code` (WMO) — the **raw provider code `c`**, which is *not* the classifier input |
| **Derived κ** | The classifier consumes **κ = χ(c)**, a *derived* binary indicator: χ(c) = 1 iff c ∈ {95, 96, 99}, else 0. **κ is not measured** — no provider reports κ, and no instrument observes it; it is computed from `c`. An absent or unrecognised `c` yields κ = 0 (non-escalating, fail-open for the storm disjunct — **not** fail-safe, and **not** a fault of the rate). A missing or invalid *rate* is the separate, required-input case: ⊥ → UNSAFE as a fault. See `appendix-c-formalisation.md` C.2.0.4a |
| **Valid time** | Precipitation is a preceding-hour sum — **unlike every other variable here, which is instantaneous** |
| **Fit for threshold?** | ⚠️ **PARTIAL — see F-11.** MET anchors the UNSAFE tier to *Ribut Petir* (thunderstorm). `weather_code` returns **zero** activating codes (95/96/99) in five years — Open-Meteo states thunderstorm estimation "is not possible" outside Central Europe — so κ = 0 in all 43,848 hours and the storm route, though typed, implemented and evaluated, is **empirically unexercised**. This establishes only that the *activating provider codes did not occur in the replay*; it is **not** evidence that no thunderstorms occurred, that thunderstorms do not occur in Sabah, or that the route is unnecessary. UNSAFE is therefore reachable only via precipitation > 20 mm/hr, and every `g_r` figure is a lower bound |

### m — marine warning level

| | |
|---|---|
| **Source** | **NONE — no historical data exists** |
| **Intended** | `met.gov.my/data/IDM20016.html`, current bulletin only, no archive |
| **Held at** | `none` throughout all analyses |
| **Fit for threshold?** | ❌ **UNMEASURED.** `g_m` can only *raise* severity, so **every severity figure in the empirical work is a lower bound** |

Candidate source: **myMETdata** (`mymetdata.met.gov.my`) — paid, RM20/CSV, station WMKK. See Q2.

### o — ocean state (wave height)

**Two datasets exist. MFWAM is the better instrument; ERA5-Ocean has the longer record.**

| | ERA5-Ocean | **MFWAM** |
|---|---|---|
| Full name | ECMWF ERA5 ocean-wave component | **Météo-France WAve Model** |
| Type | **Reanalysis** — frozen historical reconstruction | **Operational analysis/forecast** |
| Assimilates observations | Historical, at reanalysis production | **Live satellite altimetry** |
| Delivered via | Copernicus C3S | Copernicus Marine (CMEMS), `GLOBAL_ANALYSISFORECAST_WAV_001_027` |
| **Resolution** | 0.5° ≈ **50 km** | 0.08° ≈ **8 km** |
| **Coverage** | **1940 → present** | Oct 2021 → present |
| Grid cell returned | 6.0, 116.0 | **5.958336, 116.04167** |
| Distance to weather cell | 7.2 km | **2.7 km** |
| File | `raw_marine.csv`, `raw_marine_era5_sea.csv` | `raw_marine_mfwam.csv` |
| Records | 43,848 (5 y) | 28,512 (3.25 y), 11 NaN |
| Observed max wave | 2.60 m | **1.84 m** |
| Mean wave | 0.645 m | 0.590 m |

The two correlate at **r = 0.953** over their 28,501-hour overlap. The difference is concentrated in the upper tail — ERA5-Ocean's 50 km cell averages open water that MFWAM resolves as sheltered by the Tunku Abdul Rahman island group. See F-12 and F-14.

**Which to use.** MFWAM for any headline figure: finer resolution, observation-assimilating, and its cell sits 2.7 km from the weather cell rather than 7.2 km. ERA5-Ocean for the full five-year record, and as the resolution-sensitivity comparison. Report both.

**Temporal resolution — checked.** Open-Meteo's model table lists MFWAM as *3-hourly* against ERA5-Ocean's *hourly*, which would mean two of every three MFWAM values are interpolated fill. Tested empirically for an interpolation signature in second differences:

| | at 0/3/6/9… | at intermediate hours | ratio |
|---|---|---|---|
| MFWAM | 0.01240 | 0.01334 | **0.93** |
| ERA5-Ocean (known hourly) | 0.01244 | 0.01162 | 1.07 |

Both near 1.0 — **no linear-interpolation signature.** Intermediate hours carry as much genuine variation as native steps, so the series behaves as hourly and the hysteresis analysis on it holds. *Caveat: this rules out linear interpolation, not a smoother spline. The docs/data discrepancy is unresolved but does not appear to affect results.*

---

**Details of the v1 collection (ERA5-Ocean):**

| | |
|---|---|
| **Source** | Open-Meteo Marine API — `marine-api.open-meteo.com/v1/marine` |
| **Model** | **`era5_ocean`** — explicitly requested |
| **Resolution** | **0.5° ≈ 50 km — the coarsest of the nine models Open-Meteo offers** |
| **Variable** | `wave_height` = **significant wave height (Hs)** — semantically correct for thresholds derived from Yaakob and Jeong & Im |
| **Valid time** | Instant |
| **Grid cell** | **SEA — 6.0, 116.0** (marine API defaults to `cell_selection=sea`; correct) |
| **Fit for threshold?** | ⚠️ **COARSE — see F-12.** Carries ~97–99% of daylight CAUTION decisions (**98.71% primary / 97.66% resolution** — `g_o`'s share as the deciding component; see empirical-findings §0a). A ~50 km open-water average, compared against the small-vessel **1.0 m / 1.25 m** thresholds, governing boats operating within ~9 km of an island-sheltered coast *(Corrected 2026-09-09: previously 98.66% / 97.41%, superseded by the SDR-001 migration, and "1.9 m", superseded by the 2026-09-06 operational-ceiling amendment)* |

**The model choice was effectively forced and is defensible.** Every finer model begins in 2021 or later:

| Model | Resolution | Earliest |
|---|---|---|
| DWD EWAM | ~5 km | Europe only |
| MeteoFrance MFWAM | ~8 km | Oct 2021 |
| ECMWF WAM | 9 km | Nov 2025 |
| NCEP GFS Wave 0.16° | ~16 km | Oct 2024 (covers Borneo) |
| **ERA5-Ocean** | **~50 km** | **1940** |

For a 2020–2024 retrospective, ERA5-Ocean is the only option. State it as a deliberate trade-off, not an oversight.

**Also available and unused:** `wave_period` is fully populated (non-NaN). `wind_wave_*` and `swell_wave_*` are entirely NaN because ERA5-Ocean does not provide partitioned components — not a download error. See Q5.

### v — vessel category

| | |
|---|---|
| **Source** | Not measured — a fixed registry attribute set per scenario |
| **Fit for threshold?** | ✅ Not applicable. Conditions `g_o`; carries no measurement error |

### t — time of day

| | |
|---|---|
| **Source** | Timestamp, `Asia/Kuching` (GMT+8) |
| **Fit for threshold?** | ✅ Exact |

### tide — collected, not modelled

| | |
|---|---|
| **Source** | **Marea API** — `api.marea.ooo/v2/tides` |
| **File** | `data/raw_tide_marea.csv` — 5 years hourly, fully populated |
| **Status** | **Not in E.** Gao (2024) rates tide highest of any factor at 4.55/5 — above weather. The data exists and is unused. See Q3 |

---

## 3. Grid cell summary — the mismatch at a glance

All requested at **5.98, 116.01**.

| File | Returned cell | Surface | km from request | Status |
|---|---|---|---|---|
| `raw_weather.csv` (v1) | 5.940246, 116.100006 | **land** | 10.9 | superseded |
| `raw_rainfall.csv` (v1) | 5.940246, 116.100006 | **land** | 10.9 | **not in use** — superseded by the `precipitation` column of `raw_weather_sea.csv` *(status corrected 2026-09-09; it read "still in use")* |
| `raw_marine.csv` (v1) | 6.0, 116.0 | sea | 2.5 | superseded |
| **`raw_weather_sea.csv` (v2)** | 5.940246, **116.025** | **sea** | 4.7 | **current** |
| `raw_marine_era5_sea.csv` (v2) | 6.0, 116.0 | sea | 2.5 | comparison |
| **`raw_marine_mfwam.csv` (v2)** | **5.958336, 116.04167** | sea | **4.3** | **current** |

**Pairwise separation — the v1 problem and the v2 fix:**

| Pair | km |
|---|---|
| v1 weather (LAND) ↔ marine ERA5 | **12.9** ← the original mismatch |
| v2 weather (SEA) ↔ marine ERA5 | 7.2 |
| **v2 weather (SEA) ↔ marine MFWAM** | **2.7** ← best-matched pair |

The v1 classifier combined wind measured over **land** with waves measured over **water 12.9 km away**, as though they described one place. The v2 pairing (`raw_weather_sea.csv` + `raw_marine_mfwam.csv`) reduces that to **2.7 km**.

✅ **`raw_rainfall.csv` was never re-collected — and no longer needs to be, because no canonical analysis reads it.** Canonical precipitation is the `precipitation` column of **`raw_weather_sea.csv`** (sea cell, 5.940246 / 116.025), which arrived with the v2 wind re-collection; the land-sited `raw_rainfall.csv` is reachable only behind `--v1-historical`. The two are genuinely different series — 14,019.4 mm against 14,970.2 mm over five years, 113 hours above 10 mm/hr against 131 — so this was a real provenance difference, not a nominal one, and it is resolved by substitution rather than by re-collection. `g_r` decides only **0.20% / 0.26%** of all-hours non-SAFE classifications (PRIMARY / RESOLUTION). *(Status corrected 2026-09-09: this paragraph read "⚠️ has not been re-collected … but it is an outstanding inconsistency", which was written before the canonical scripts moved to the sea-cell precipitation column.)* *(Corrected 2026-09-09: previously "3.7% of non-SAFE hours", computed before the rainfall-threshold anchoring and the SDR-001 migration.)* Precipitation is also available in `raw_weather_sea.csv`, which is sea-sited; prefer that column.

---

## 4. Checklist before citing any empirical figure

- [ ] **Which files?** Use `raw_weather_sea.csv` + `raw_marine_mfwam.csv` (2.7 km apart) unless you need the full five years, in which case say so
- [ ] Does it depend on `w`? → resolved (F-13). At the canonical **21.6 kn** boundary `g_w` **activates twice** in 43,848 hours and **binds in neither**. **Quote both counts — 2 activations, 0 bindings — and never write "never fires".** A binding share of 0.00% does *not* mean zero activations: *activation* is `g_w` reaching a non-SAFE component state; *binding* is `g_w` being the deciding component under max-severity. *(Corrected 2026-09-09: this item read "`g_w` never fires at either cell", which was true only under the superseded 22 kn rounding. See F-17.)*
- [ ] Does it depend on `r`? → thunderstorms undetectable (F-11), so the figure is a lower bound. **Provenance is settled: canonical precipitation comes from the `precipitation` column of `raw_weather_sea.csv` (sea cell), not from the land-cell `raw_rainfall.csv`, which no canonical analysis reads.** *(Corrected 2026-09-09: this item asked the reader to check which file the rainfall column came from; the answer is now fixed and verified against executable data flow.)*
- [ ] Does it depend on `m`? → no data; the figure is a lower bound
- [ ] Does it depend on `o`? → **state which model.** ERA5-Ocean 50 km or MFWAM 8 km — they differ by 33% on the headline figure (F-14)
- [ ] Is it compared against a MET Malaysia threshold? → §1 provenance mismatch applies, and see `finding-met-hydrodynamic-gap.md`

---

## 5. Related

| Document | Relationship |
|---|---|
| `empirical-findings-2026-09-06.md` | F-9 to F-12 are the findings this document generalises |
| `decision-record-empirical-first.md` | Open questions Q1a (land/sea), Q1b (storm detection), Q2 (marine warning archive), Q3 (tide), Q5 (wave period) |
| `docs/implementation/data-source-met-malaysia.md` | The *intended* sources, and why they could not be used retrospectively |
| `scripts/openmeteo_raw_download.py` | The collection script; carries inline warnings |
