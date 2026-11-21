# A18.1 Step 3 Handoff — confirmed source fields and assumptions

**From Step 2, 21 November 2026.** Only what is file-verified or explicitly flagged. Step 3 reconstructs governance rules; it must not re-derive these inputs.

---

## 1. Confirmed input fields — safe to build rules on

All `VERIFIED_FROM_FILE`. Column names are exact, including the unit suffix and spacing.

### `data/raw_weather_sea.csv` — wind, precipitation, WMO code
`skiprows=3`. Grid centre 5.940246 N, 116.025 E. 43,848 rows, 2020-01-01T00:00 → 2024-12-31T23:00, Asia/Kuching local, hourly, no gaps, no duplicates, **zero nulls**.

| Column | Unit | Role |
|---|---|---|
| `time` | naive local (Asia/Kuching) | join key |
| `wind_speed_10m (kn)` | knots | `g_w` |
| `wind_direction_10m (°)` | degrees | not used by the classifier |
| `wind_gusts_10m (kn)` | knots | not used by the classifier |
| `precipitation (mm)` | mm | `g_r` |
| `weather_code (wmo code)` | WMO code | not used by the classifier |

### `data/raw_marine_era5_sea.csv` — wave, PRIMARY
`skiprows=3`. Grid centre 6.0 N, 116.0 E. 43,848 rows, same span and cadence, **zero nulls**.

| Column | Unit | Role |
|---|---|---|
| `time` | naive local | join key |
| `wave_height (m)` | m | `g_o` |
| `wave_period (s)` | s | **DO NOT USE** — see §3 |

### `data/raw_marine_mfwam.csv` — wave, RESOLUTION
`skiprows=3`. Grid centre 5.958336 N, 116.04167 E. 28,512 rows, 2021-10-01T00:00 → 2024-12-31T23:00, hourly, no gaps, no duplicates. `wave_height (m)` has **11 nulls**; `wave_period (s)` has 35.

### `data/solar/solar-events-daily.csv`
The C-3 frozen artefact read by `scripts/canonical_gt.py:58` for `g_t`. Present and hashed. **No solar astronomy is computed at run time** — `g_t` reads this file.

### `data/prediction-register.csv`
Pre-registered predictions P21–P24, hash `5574b88ea65168b6…`. **Warning:** `condition_comparison.py:313,334` both reads and, on one path, *writes* this file — C-5 and C-7 recorded that it did so. Step 3 must treat it as read-only and confirm which path is live before executing anything.

---

## 2. Confirmed derivation rules

| Rule | Exact form | Evidence |
|---|---|---|
| Join | inner join on `time`, 1:1, no duplicate keys either side | this audit |
| Exclusion | `dropna(subset=["wind_speed_10m (kn)", "wave_height (m)", "precipitation (mm)"])` | `historical_replay.py:136` |
| Departure window | `05 ≤ hour ≤ 09`, **inclusive both ends**, 5 slots/day | this audit; half-open gives 7,308 ≠ 9,135 |
| Timezone | none applied; series already local | metadata + `TIMEZONE = "Asia/Kuching"` |
| Config | canonical = v2 sea cell | `historical_replay.py:117-132` |
| Precipitation source | the **sea** weather file, not `raw_rainfall.csv` | `condition_comparison.py:132` |

Counts these rules yield, reproduced independently: PRIMARY 43,848 / 9,135. RESOLUTION 28,501 / 5,935.

---

## 3. Do-not-use list

| Artefact | Why |
|---|---|
| `raw_weather.csv`, `raw_marine.csv`, `raw_rainfall.csv` | v1 **land cell**, condemned by F-10, 10.89 km from the requested point. Retained for comparison only. |
| `raw_tide_marea.csv` | read by no canonical script, no declared timezone or coordinates, 10 irregular steps, extends past the window. Not a classifier input. |
| `wave_period (s)` | downloaded but referenced by no analysis script. It carries 35 nulls, not 11 — using it would drop the usable count below 28,501. |
| Five all-empty columns | `wind_wave_*`, `swell_wave_*`, `precipitation_probability` — product does not supply them. |

---

## 4. Assumptions Step 3 must carry forward verbatim

These are **not** findings. They are unresolved dependencies that must travel with any result.

1. **`decision_time_availability = UNKNOWN` for 100% of records.** Every value is retrospective reanalysis. Nothing in `data/` is an issued-before-decision forecast or observation. No wording may imply a fisher had this information at the historical decision time. **Not closable from local artefacts.**
2. **Marine warnings are a modelling assumption.** No warning column exists in any raw file. A constant SAFE is not observed absence of warnings.
3. **The local-time claim rests on the retrieval request**, not on the stored files. One provider request with `timezone=UTC`, compared on a single sample hour, would settle it cheaply and decisively.
4. **PRIMARY vs RESOLUTION is a two-factor change** — wave product *and* wind–wave separation (7.20 km → 2.73 km). Do not attribute a difference to resolution alone.
5. **Stated coordinates are provider-snapped grid centres.** The requested point was 5.98 N, 116.01 E; report it alongside.
6. **Provider identity is `DOCUMENTED_ONLY`.** Local hashes are not provider checksums.
7. **The dependency file is retrospective** — written 2026-10-08, after the September 2026 runs.

---

## 5. What Step 3 must NOT do

- Not equate risk-state occupancy, governance binding or threshold crossing with correct or safe fishing actions.
- Not treat the A2/A3 fisheries action catalogue as interchangeable with `{Go, Delay, DepartureTime, Duration}`.
- Not modify any conference output, data or conclusion.
- Not introduce new policy logic.
- Not write to `data/prediction-register.csv`.

---

## 6. Evidence the researcher must supply to lift remaining limitations

| To lift | Provide |
|---|---|
| D-03 timezone | one Open-Meteo request with `timezone=UTC` for a single day, for comparison |
| D-07 provenance | request URL, parameters, response headers, retrieval timestamp — or a provider-published checksum |
| D-08 decision-time availability | archived **issue-time** forecast products for Kota Kinabalu 2020–2024. If unobtainable, the limitation is permanent and should be stated as such. |
| D-12 confound | a wind field co-located with each wave cell, which would make the resolution contrast single-factor. This is a new experiment, not a documentation fix. |
