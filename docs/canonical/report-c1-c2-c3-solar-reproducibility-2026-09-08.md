# Report: SDR-001 Execution Conditions C-1, C-2, C-3 — Solar Reproducibility Package

**Date:** 2026-09-08
**SDR-001 status:** **APPROVED — MODEL B SELECTED — NOT YET CANONICAL** (unchanged by this task)
**Scope:** C-1, C-2, C-3 only. **C-4 through C-8 not executed.** Canonical `g_t` unchanged; prediction register byte-for-byte unchanged; no published figure regenerated.

---

# RESULT

# **SOLAR REPRODUCIBILITY PACKAGE INCOMPLETE**

| Condition | Status |
|---|---|
| **C-1** — pin the implementation and all reproducibility parameters | ✅ **CLOSED** |
| **C-2** — complete 28-row USNO validation artefact | 🟡 **OPEN — partially discharged** |
| **C-3** — daily solar-event artefact for the replay period | ✅ **CLOSED** |

**C-2 remains open for one reason, stated plainly: the original per-event USNO reference values do not exist anywhere in the project, and a reconstruction does not reproduce the recorded summary statistics.** A complete 28-row artefact now exists and is fully usable, but it is a **reconstruction captured 2026-09-08**, not the original evidence, and it yields **max 0.92 / mean 0.3786 min** against the recorded **0.90 / 0.37**. Per instruction, nothing was fabricated and nothing was tuned to force agreement. §10–§11.

---

## 1. Authoritative coordinate determination

**The coordinate question was larger than "116.07 vs 116.01".** Tracing the data revealed *four* longitudes in play.

### 1.1 What the project actually contains

| Source | Latitude | Longitude | Role |
|---|---|---|---|
| `openmeteo_raw_download.py` L17–18 | **5.98** | **116.01** | **Requested** |
| `collect_raw_v2.py` L51–52 | **5.98** | **116.01** | **Requested** |
| `openmeteo_raw_rainfall.py` L17–18 | **5.98** | **116.01** | **Requested** |
| `data-provenance.md` L143 | **5.98** | **116.01** | *"All requested at 5.98, 116.01"* |
| `raw_weather_sea.csv` header | 5.940246 | 116.025 | **Delivered** grid cell (wind, precipitation) |
| `raw_marine_era5_sea.csv` header | 6.0 | 116.0 | **Delivered** grid cell (PRIMARY waves) |
| `raw_marine_mfwam.csv` header | 5.958336 | 116.04167 | **Delivered** grid cell (RESOLUTION waves) |
| `raw_weather.csv` header (v1 land) | 5.940246 | 116.100006 | Superseded land cell (F-10) |
| **`solar.py` default** | 5.98 | **116.07** | **Matches nothing** |

**Open-Meteo snaps requests to grid cells, so delivered coordinates differ per variable.** Three different cells serve one site.

### 1.2 The rule used, since the project defines a location rather than an instrument point

> **Solar events are a property of the geographic location, not of any data grid cell.** Sunrise depends on where the observer is; it has nothing to do with which ERA5 or MFWAM cell supplied a wave height. Since the three delivered cells disagree with one another, **no delivered cell can serve as "the site"** — selecting one would be arbitrary and would silently privilege one variable's grid over the others.
>
> **The representative coordinate is therefore the requested site coordinate** — the location the project declares it is studying, consistently, in all three collection scripts and in `data-provenance.md`.

### 1.3 Authoritative pair

> ## **φ = 5.98° N,  λ = 116.01° E**

**Provenance:** declared identically in `openmeteo_raw_download.py`, `collect_raw_v2.py` and `openmeteo_raw_rainfall.py`; recorded in `data-provenance.md` §L143.

---

## 2. Longitude 116.07 vs 116.01 — resolved

> ### **116.01 is authoritative. 116.07 is superseded and has no provenance.**

**116.07 matches no artefact in the project** — not the requested coordinate (116.01), not any delivered grid cell (116.025 / 116.0 / 116.04167), not the superseded land cell (116.100006). It is a fourth, undocumented value that entered `solar.py` as a default argument and propagated into three findings (`finding-gt-provenance-audit.md` §10, `finding-gt-operational-semantics.md`, `finding-gt-evidence-closure.md` Part 2).

**This is the same failure mode as 7.5 mm/hr and the 22 kn rounding:** a number in the code with no source, inherited by documents that then cited it as the site coordinate.

### 2.1 Quantified effect — computed, not estimated

Longitude enters the implementation as a pure additive term (`720 + 4·(−lon ± ha) − eq`), so the shift is **exact, constant, and identical for every event on every date**:

| | |
|---|---|
| Δλ | 116.07 → 116.01 = **−0.06°** westward |
| Solar-time rate | 4 min / degree |
| **Effect** | **all events occur 0.24 min (14.4 s) LATER** |

**No canonical replay figure was regenerated.** The effect is quantified here and reported separately, as required.

### 2.2 Consequences that follow

The change is small in magnitude and **not** negligible in effect, because it interacts with hour boundaries (§14) and with 1-minute-resolution reference values (§11).

---

## 3. Pinned solar specification — `solar-spec-v1`

| Parameter | Value |
|---|---|
| **Specification version** | `solar-spec-v1` |
| **Implementation** | NOAA-style low-precision solar-position formulation, `scripts/sensitivity/solar.py` |
| **Implementation version** | `solar-v1` |
| **Implementation sha256** | `3b7dc371ebe5931b3336f9982c5806a06a515dc2032569f5da7720470c1ec36c` |
| **Latitude** | **5.98° N** |
| **Longitude** | **116.01° E** |
| **Timezone** | **UTC+8**, fixed |
| **DST** | **None.** Malaysia observes no daylight saving; all dataset headers carry `utc_offset_seconds = 28800` and USNO returns `isdst: false` for every queried date |
| **UTC→local rule** | events computed in UTC minutes, then `hours = utc_min/60 + 8`; no zone database, no historical offset lookup |
| **Sunrise/sunset zenith** | **90.833°** = 90° + 34′ mean atmospheric refraction + 16′ solar semi-diameter — the geometric moment the upper limb appears on a sea horizon at nominal pressure and temperature |
| **Civil twilight zenith** | **96.0°** (sun 6° below horizon) — computed and stored, **not used by Model B**, retained for provenance |
| **Day-of-year** | calendar `tm_yday`, 1…365 (366 in leap years) |
| **Series denominator** | fixed **365** — see §5 |
| **Boundary rule** | half-open, **sunrise ≤ t < sunset** |
| **Elevation / pressure / temperature** | not modelled; refraction fixed at 34′ |

**Algorithm unchanged.** `solar.py` was re-used, not rewritten; its hash is identical before and after this task. No defect was found in the mathematics.

---

## 4. Implementation version and hash

> **`solar-v1` · sha256 `3b7dc371ebe5931b3336f9982c5806a06a515dc2032569f5da7720470c1ec36c`**

Recorded **in every row** of both artefacts (`impl_version`, `impl_sha256`, `spec_version`), so identification never depends on a filename or a directory location.

**Additional pin available:** the project *is* a git repository (`git rev-parse HEAD` → `01a6d9a` at the time of writing). The readiness audit recorded "no version pin of any kind" and "not a git repository" — **that was wrong**, and the correction is noted here. Git provides a repository-level pin; the per-row sha256 provides an artefact-level pin that survives export, copying, and reorganisation. Both are recorded.

---

## 5. Leap-year semantics — measured, not assumed

**The behaviour is fully specified and its consequence is bounded and documented.**

| Fact | Detail |
|---|---|
| **Is 29 February computed?** | **Yes.** `tm_yday = 60`. It is not skipped, not duplicated, and never yields INVALID |
| **Denominator** | fixed **365**, so the day angle is `Γ = 2π(doy−1)/365` |
| **Consequence** | In a leap year, every date from **1 March onward** carries a `doy` one higher than the same calendar date in a common year, so the series is evaluated one day further along |

**Measured offset, common year (2023) vs leap year (2024), same calendar date:**

| Date | Common year | Leap year | Δ |
|---|---|---|---|
| 03-01 | 06:28:48 | 06:28:28 | **0.34 min** |
| 03-20 | 06:20:58 | 06:20:30 | **0.47 min** |
| 06-21 | 06:03:13 | 06:03:26 | 0.22 min |
| 09-22 | 06:05:04 | 06:04:52 | 0.21 min |
| 12-21 | 06:20:32 | 06:21:00 | **0.47 min** |

> **Worst sampled post-Feb-29 offset: 0.47 min (28 s).**

**This is documented, not silently absorbed.** It is the same order as the implementation's own 0.9-min agreement with USNO, so it is within the method's established accuracy rather than a defect — but it is a real systematic effect, it is largest near the equinox and solstice, and **it interacts with the hour-boundary sensitivity in §14**.

**The validated formulation was not altered.** Changing the denominator to 366 in leap years would invalidate the existing USNO agreement and is out of scope; it is recorded as a candidate refinement for a future specification version, to be adopted only with fresh validation.

---

## 6. Boundary and precision semantics

### 6.1 Boundary rule — recorded explicitly

> **sunrise ≤ t < sunset**
> **Exact sunrise = SAFE.  Exact sunset = UNSAFE.**

Half-open, matching the incumbent's convention and preserving the exhaustive-partition argument Theorem C.1 requires. *(Recorded for migration; this task performs no classification.)*

### 6.2 Precision — four distinct levels, separately specified

| Level | Specification |
|---|---|
| **Calculation** | IEEE-754 float64 throughout; no intermediate rounding |
| **Stored** | `*_hours` to **6 decimal places** of an hour (≈ 3.6 ms) — the canonical value |
| **Display** | `*_local` as **HH:MM:SS** — human-readable only |
| **Comparison** | **the stored float**, never the display string |

> **Classification must consume `sunrise_hours` / `sunset_hours`, never `sunrise_local` / `sunset_local`.** Comparing against an HH:MM:SS rendering would reintroduce rounding at exactly the boundary where §14 shows it matters.

---

## 7. Invalid-input handling — specified and exercised

**Requirement:** invalid input must never return a plausible timestamp.

**Defect found in the current implementation:** `solar.py` has **no input validation**. `np.clip(c, −1, 1)` silently returns a value for out-of-range latitudes and for polar no-event days. Given an invalid latitude it produces a plausible-looking time.

**`solar.py` was deliberately left unmodified** — it is the hash-pinned validated artefact, and modifying it would void the validation. The guard is specified and exercised in the builder layer, and **must be carried into the canonical solar module at migration (C-8)**.

**All seven cases verified:**

| Case | Result |
|---|---|
| valid control (2024-03-20) | 06:20:30 ✅ |
| latitude 95 (out of range) | **INVALID** ✅ |
| latitude 89.9 (polar, no event that day) | **INVALID** ✅ |
| longitude 400 (out of range) | **INVALID** ✅ |
| timezone 99 (out of range) | **INVALID** ✅ |
| date is not a date | **INVALID** ✅ |
| **date is None (device clock unavailable)** | **INVALID** ✅ |
| non-finite or out-of-[0,24) result | **INVALID** ✅ |

**Architecture requirement preserved:** an INVALID or absent clock is `t = ⊥`, and **`g_t(⊥) = UNSAFE`** by Corollary C.1b.1 — never SAFE, and never a fabricated timestamp. `t ∉ D` (D1) still holds: a clock failure is a fault, never a declared exclusion.

---

## 8. Published-reference status — gap recorded, not invented

**Terminology retained exactly as approved under C-0:**

> **NOAA-style low-precision solar-position formulation implemented in `scripts/sensitivity/solar.py`**

**None of `Meeus`, `NOAA/Meeus`, `Meeus/NOAA`, `NOAA/Spencer` was reintroduced.**

| Question | Answer |
|---|---|
| What does the code implement? | Truncated Fourier series in `Γ = 2π(doy−1)/365` for declination (3rd harmonic) and equation of time (2nd harmonic), plus the standard hour-angle equation — **established from the code** |
| Is there a stable published reference in the project? | ❌ **No.** The docstring names two distinct sources (NOAA GML calculator equations *and* Astronomical Almanac low-precision formulae); neither is verified, and the project holds no citation for either |
| Was one established during this task? | ❌ **No.** Establishing it requires locating the specific published rendering and matching its coefficients — external bibliographic work not performed here |

> ### ⚠️ **PUBLICATION-REFERENCE GAP — recorded, open**
>
> The formulation is **pinned by hash and fully reproducible**, but **not yet citable to a specific publication**. This does not block C-1: the condition requires an honest pinned specification, and a hash pin plus an explicit gap statement is honest. It **does** need resolving before the method is described in a thesis or paper, and it is recorded as a **documentation item for C-8**, not manufactured here.

---

## 9. Complete C-1 checklist

| # | Requirement | Status | Value |
|---|---|---|---|
| 1 | Algorithm terminology | ✅ | NOAA-style low-precision solar-position formulation |
| 2 | Implementation version / hash | ✅ | `solar-v1` · `3b7dc371…c36c` · git `01a6d9a` |
| 3 | Published-reference status | ✅ **explicit** | **Gap recorded** (§8) — stated, not invented |
| 4 | Canonical latitude | ✅ | **5.98° N** |
| 5 | Canonical longitude | ✅ | **116.01° E** (§2) |
| 6 | Timezone | ✅ | UTC+8, no DST, evidenced |
| 7 | UTC/local rule | ✅ | `utc_min/60 + 8`, fixed offset |
| 8 | Leap-year handling | ✅ | Feb 29 computed, doy 60; fixed-365 denominator; **worst offset 0.47 min, measured** (§5) |
| 9 | Solar zenith | ✅ | 90.833° sunrise/sunset (34′ + 16′); 96.0° civil |
| 10 | Precision / rounding | ✅ | 4 levels separately specified (§6.2) |
| 11 | Invalid-input semantics | ✅ | 7 cases verified; `g_t(⊥) = UNSAFE` (§7) |
| 12 | Boundary comparison semantics | ✅ | `sunrise ≤ t < sunset` (§6.1) |

**All twelve explicit. No ambiguity remains.**

> ## **C-1 — CLOSED**

---

## 10. C-2 — USNO 28-row artefact status

### 10.1 The original evidence does not exist

**Searched:** every file in the project for `USNO`, for a validation script, for a captured API response, for the seven validation dates in any `.csv`/`.json`/`.py`.

> **Result: `USNO` appears in prose documents only.** No validation script, no captured response, no data artefact. The project retained **summary statistics alone**.

**Per instruction, reconstruction from summary statistics was not attempted and no reference value was reverse-engineered or invented.**

### 10.2 External re-query — performed and labelled

External re-query was identified as necessary and performed against **USNO Astronomical Applications API v4.0.1**, endpoint `/api/rstt/oneday`, `coords=5.98,116.01`, `tz=8`, on **2026-09-08**. All 7 dates returned all 4 events.

> ### ⚠️ **`data/solar/usno-validation-2026-09-08.csv` IS A RECONSTRUCTED VALIDATION DATASET.**
> **It is not the original captured response.** Every row carries `artefact_status = RECONSTRUCTED-2026-09-08` and `validation_captured = 2026-09-08`. It is not presented as historical.

### 10.3 The artefact — 28 rows, all required fields

`data/solar/usno-validation-2026-09-08.csv` — **7 dates × 4 events = 28 rows**, one per event:

`date` · `selection_reason` · `latitude` · `longitude` · `timezone` · `event` · `local_hours` · `local_time` · `usno_time` · `usno_hours` · `diff_signed_min` · `diff_abs_min` · `local_time_at_116_07` · `diff_abs_min_at_116_07` · `impl_version` · `impl_sha256` · `spec_version` · `validation_source` · `validation_captured` · `artefact_status`

Both coordinates are carried per row, so the superseded 116.07 comparison remains auditable rather than being erased.

---

## 11. Validation-statistic reproduction — **does not reproduce**

Recomputed from the frozen artefact. **The solar algorithm was not modified to force agreement.**

| Statistic | Recorded in the finding | At **116.01** (authoritative) | At **116.07** (as originally validated) |
|---|---|---|---|
| Max abs difference | **0.90 min** | **0.92 min** | 0.99 min |
| Mean abs difference | **0.37 min** | **0.3786 min** | 0.4107 min |
| Sunrise/sunset mean | **0.35 min** | **0.3321 min** | 0.3693 min |

> ### ⚠️ **DISCREPANCY — reported, not resolved**
>
> **Neither coordinate reproduces the recorded triple.** The differences are small (≤ 0.05 min on the mean) and do not change any conclusion — the implementation still agrees with USNO to **under one minute at every one of the 28 events**, which is what the decision rested on. But the recorded numbers cannot be regenerated exactly.

**Diagnosed cause — verified, not speculated.** USNO reports to **whole minutes**. Sub-minute coordinate differences therefore flip a reference value by a full minute at rounding boundaries. Re-querying USNO at 116.07 confirmed this directly: of 8 events checked across two dates, **2 differed by one minute** from the 116.01 response (2024-03-20 sunset 18:26 vs 18:27; 2024-11-11 civil dusk 18:17 vs 18:18).

**So the original reference set is not recoverable** without knowing which coordinate was queried — and even then, whole-minute rounding makes the comparison coordinate-sensitive in a way the summary statistics cannot encode.

**This is precisely the failure C-2 exists to prevent, demonstrated on the project's own evidence.** A validation recorded only as `max 0.9, mean 0.37` cannot be checked, cannot be reproduced, and cannot be attributed to a coordinate. **The new artefact makes the same loss impossible in future.**

> ## **C-2 — OPEN (partially discharged)**
>
> **Discharged:** a complete, frozen, self-describing 28-row artefact now exists and is usable for migration.
> **Not discharged:** it is a reconstruction, not the original evidence, and it does not reproduce the recorded summary statistics.
>
> **To close, one of:** (a) accept the reconstructed artefact as the validation of record and **correct the recorded statistics** in `finding-gt-evidence-closure.md` §2 to the reconstructed values — a documentation change requiring explicit approval, since it edits a recorded result; or (b) locate the original capture, if it exists outside the repository.
>
> **Neither was done here.** Option (a) rewrites a recorded empirical value and is exactly the kind of change this project requires to be deliberate and approved.

---

## 12. C-3 — daily solar artefact

**`data/solar/solar-events-daily.csv` — 1,827 rows, one per replay date.**

| Field | Purpose |
|---|---|
| `date` | Replay date |
| `latitude`, `longitude`, `timezone`, `utc_offset_seconds` | Location and time base, per row |
| `sunrise_hours`, `sunset_hours` | **Canonical values**, 6 dp — what classification must consume |
| `sunrise_local`, `sunset_local` | HH:MM:SS — display only |
| `zenith_deg` | 90.833 |
| `in_primary`, `in_resolution` | Configuration membership |
| `impl_version`, `impl_sha256`, `spec_version` | Provenance pin, per row |

**Governance separation enforced.** The table contains **astronomical values only**. Verified: `grep -c "SAFE\|CAUTION\|UNSAFE\|Level 2"` → **0** in all three artefacts. No safety state, no advisory permission, no Level 2 value.

**Downstream determinism.** The intended dependency is `stored solar artefact → g_t → f`, replacing eight scripts independently recomputing solar astronomy. A later classifier joins on `date` and compares `t` against `sunrise_hours` / `sunset_hours` — **no astronomy at classification time**. The builder is isolated in `scripts/solar/`; **no canonical script was touched**, and the canonical `g_t` is untouched.

> ## **C-3 — CLOSED**

---

## 13. Replay date coverage

**Traced from the actual dataset timestamps, not from the "five year" label.**

| | PRIMARY | RESOLUTION |
|---|---|---|
| Weather source | `raw_weather_sea.csv` | `raw_weather_sea.csv` |
| Wave source | `raw_marine_era5_sea.csv` | `raw_marine_mfwam.csv` |
| Merged hourly rows | **43,848** | **28,501** |
| **First date** | **2020-01-01** | **2021-10-01** |
| **Last date** | **2024-12-31** | **2024-12-31** |
| **Unique dates** | **1,827** | **1,188** |
| Calendar span | 1,827 days | 1,188 days |
| **Gaps** | **0** | **0** |

**Both ranges fully covered.** The artefact spans 2020-01-01 → 2024-12-31 (1,827 rows); RESOLUTION is the labelled subset (`in_resolution = Y`, 1,188 rows). **No date required by either configuration is missing.**

---

## 14. Boundary-sensitivity reproduction

Recomputed from the stored daily timestamps at the authoritative coordinate.

| | Previously recorded (at 116.07) | **Recomputed (at 116.01)** | Δ |
|---|---|---|---|
| **Sunrise within 1 min of an hour mark** | 160 days | **150 days** | **−10** |
| **Sunset within 1 min** | 60 days | **65 days** | **+5** |
| Sunrise within 2 min | 335 days | **305 days** | −30 |
| Sunset within 2 min | 125 days | **135 days** | +10 |
| **Closest approach** | 0.02 min | **0.0156 min** (sunrise) · 0.0716 min (sunset) | — |

> ### The differences are real and are reported, not hidden.
>
> **They are exactly what the 0.24-min coordinate shift predicts.** Moving all events 0.24 min later moves some across the 1-minute band and others out of it. Sunrise loses 10 days, sunset gains 5 — a net reduction in exposure, which is incidental rather than a benefit.

**The finding itself is unchanged and, if anything, reinforced:** roughly **215 of 1,827 days** have a solar boundary within one minute of an hour mark, with a closest approach of **0.94 seconds**. Sub-minute implementation differences *can* flip individual hourly classifications. **This is why C-3 requires stored timestamps rather than recomputation** — and why the leap-year offset of §5 (up to 0.47 min) is not negligible in this specific context, even though it is well within the method's accuracy.

*This was a reproducibility verification, not a canonical empirical re-run. No canonical figure was regenerated.*

---

## 15. Files created / modified

**Created — 4 (all new; no existing file modified):**

| Path | Rows | Purpose |
|---|---|---|
| `scripts/solar/build_solar_artefacts.py` | — | Isolated builder; carries `solar-spec-v1` in its docstring |
| `data/solar/usno-validation-2026-09-08.csv` | **28** | **C-2** — reconstructed validation artefact |
| `data/solar/solar-events-daily.csv` | **1,827** | **C-3** — daily solar events, provenance-pinned |
| `data/solar/solar-boundary-audit.csv` | 2 | C-3 verification |

Plus this report.

**Modified: none.** `solar.py` was imported and re-used, not edited — its hash is identical before and after. No canonical script, no canonical document, no dataset, no register entry was altered.

---

## 16. Integrity checks

| Item | Status | Evidence |
|---|---|---|
| **Canonical `g_t`** | ✅ **UNCHANGED** | All three rows present verbatim in Appendix C |
| **Appendix C classifier** | ✅ **UNCHANGED** | `grep -ci "sunrise\|sunset\|USNO\|Meeus"` → **0** |
| **`G(S)`** | ✅ **UNCHANGED** | C.3: `**0**` if S = UNSAFE; `**1**` if S ∈ {SAFE, CAUTION} |
| **`A_AI(S)`** | ✅ **UNCHANGED** | C.4: `∅ if S = UNSAFE` |
| **`cause`** | ✅ **UNCHANGED** | `cause : Y → {fault, hazard}` |
| **Wind thresholds** | ✅ **UNCHANGED** | `21.6, 27.0` |
| **Rainfall thresholds** | ✅ **UNCHANGED** | `10.0, 20.0` |
| **Wave thresholds** | ✅ **UNCHANGED** | `{small:(1.0,1.25), medium:(1.4,2.8), big:(1.5,3.5)}` |
| **Replay classifications** | ✅ **UNCHANGED** | No classifier executed |
| **7.72%** | ✅ **UNCHANGED** | 8 occurrences in §0a |
| **5.98%** | ✅ **UNCHANGED** | 5 occurrences |
| **Canonical figures** | ✅ **UNCHANGED** | Not regenerated |
| **`solar.py`** | ✅ **UNCHANGED** | `3b7dc371ebe5931b…` |
| **Canonical scripts** | ✅ **UNCHANGED** | `canonical_figures` `5af9eaf7…` · `condition_comparison` `1f0f4e9c…` · `hysteresis_analysis` `73015d88…` |
| **Prediction register** | ✅ **BYTE-FOR-BYTE UNCHANGED** | `sha256 538808b6d82249fa…` |
| **24 entries · 22 CONFIRMED / 2 REFUTED** | ✅ **UNCHANGED** | Verified |
| **SDR-001** | ✅ **APPROVED — NOT YET APPLIED** | Unchanged |

---

## 17–19. Condition status

| | Condition | Status |
|---|---|---|
| **C-1** | Pin the solar implementation and all reproducibility parameters | ✅ **CLOSED** — 12/12 checklist items explicit (§9) |
| **C-2** | Complete 28-row USNO validation artefact | 🟡 **OPEN** — artefact exists and is complete, but it is a **reconstruction** and **does not reproduce the recorded statistics** (§10–§11) |
| **C-3** | Daily solar-event artefact | ✅ **CLOSED** — 1,827 rows, both ranges covered, provenance-pinned, governance-separated (§12–§13) |

---

## 20. C-4 through C-8 — confirmed OPEN

| | Condition | Status |
|---|---|---|
| **C-4** | Document binary `g_t`, system-level graduation, accepted SAFE→UNSAFE cost | 🔴 **OPEN — not executed.** Appendix C still carries the fixed-clock classifier; Model B not inserted |
| **C-5** | Three-stage hysteretic re-run for P12 | 🔴 **OPEN — not executed.** No hysteretic run performed |
| **C-6** | Re-resolve affected predictions | 🔴 **OPEN — not executed.** No prediction re-resolved |
| **C-7** | Reconcile baseline discrepancies | 🔴 **OPEN — not executed.** P07/P10/P11/P12 untouched |
| **C-8** | Execute the propagation list | 🔴 **OPEN — not executed.** No canonical script or document propagated |

**Canonical classifier remains `06:00 / 17:00 / 19:00`.** No prediction was run or re-resolved. `data/prediction-register.csv` is byte-for-byte unchanged.

---

## 21. Assessment

**Two of three conditions closed, and the one that did not close failed for a reason worth having found.**

C-1 turned out to be larger than a version pin. The coordinate question was not "116.07 or 116.01" but "which of four longitudes, and by what rule" — and the answer needed a stated principle (solar events belong to the location, not to a data grid cell) rather than a preference. **116.07 had no provenance at all**, which is the same defect as 7.5 mm/hr and the 22 kn rounding: a number in the code that documents later cited as though it were sourced.

C-2 is the instructive one. **The original validation cannot be reproduced, because only its summary was kept.** A reconstruction gets close — max 0.92 against 0.90 — but not exact, and the diagnosis is specific: USNO reports whole minutes, so a 14-second coordinate difference flips reference values at rounding boundaries. Confirmed directly by re-querying at both coordinates. The conclusion the decision rested on is untouched — sub-minute agreement at all 28 events — but the recorded numbers are not regenerable.

**Marking C-2 closed would have been easy and wrong.** The artefact is complete and usable; the honest position is that it is a reconstruction that disagrees slightly with the record, and closing the gap means deciding whether to amend a recorded empirical value — a decision that belongs to the user, not to this task.

---

# **SOLAR REPRODUCIBILITY PACKAGE INCOMPLETE**

**Closed:** C-1, C-3.

**Remaining open:**

- **C-2** — the 28-row artefact exists but is a **reconstruction**, and its statistics (max **0.92** / mean **0.3786** / sunrise-sunset mean **0.3321**) do not reproduce the recorded **0.90 / 0.37 / 0.35**. Closing requires an explicit decision to amend the recorded statistics to the reconstructed values, or recovery of the original capture.
- **C-4, C-5, C-6, C-7, C-8** — not executed, as instructed.

**SDR-001 remains APPROVED — NOT YET CANONICAL. Canonical migration has not begun.**
