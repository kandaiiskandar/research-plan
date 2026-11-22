# A18.1 Step 2 — Dataset Provenance and Integrity Audit Report

**21 November 2026 · read-only source audit · Step 2 only**
Subject: accepted AAI2026 paper, presentation 23 December 2026. **No conference output, data or conclusion was modified.**

Every assertion below is tagged. `VERIFIED_FROM_FILE` = read directly from the artefact. `COMPUTED_FROM_FILE` = recomputed by this audit from the artefact. `DOCUMENTED_ONLY` = asserted in repository text or code but not independently checkable from stored data. `UNKNOWN` = not determinable from local artefacts.

---

## 1. Headline

**All four manuscript counts reproduce exactly**, recomputed by a standard-library reader that shares no dependency with the original pandas pipeline. Dataset integrity is strong: zero duplicate timestamps, strict hourly cadence, monotonic ordering, and every null accounted for.

Provenance is weaker than integrity. **No provider manifest, request log or published checksum is stored for any raw file** (D-07), so local hashes prove local byte-integrity only and not agency authenticity. And every value in the study is **retrospective reanalysis**, so decision-time availability is `UNKNOWN` for 100% of records (D-08) — a permanent limit, not a gap to be filled.

Two findings change how results should be *described* rather than whether they reproduce: the stated coordinates are provider-snapped outputs rather than the requested site (D-11), and the PRIMARY/RESOLUTION contrast changes wave product **and** wind–wave co-location distance together, so it is not a single-factor resolution comparison (D-12).

**Step 3 decision: GO WITH CONDITIONS.**

---

## 2. Table 1 — File-level inventory

| # | Path | Role | Provider (documented) | Rows | SHA-256 (first 16) |
|---|---|---|---|---:|---|
| 1 | `data/raw_weather_sea.csv` | **RAW canonical** — wind, precip, WMO | Open-Meteo archive | 43,848 | `96850d7547189ffa` |
| 2 | `data/raw_marine_era5_sea.csv` | **RAW canonical** — wave, PRIMARY | Open-Meteo marine, ERA5-Ocean | 43,848 | `6754e2c2ee5586ee` |
| 3 | `data/raw_marine_mfwam.csv` | **RAW canonical** — wave, RESOLUTION | Open-Meteo marine, MFWAM | 28,512 | `e9f323e086a3e9dd` |
| 4 | `data/raw_weather.csv` | RAW superseded — land cell, F-10 condemned | Open-Meteo archive | 43,848 | see manifest |
| 5 | `data/raw_marine.csv` | RAW superseded — land cell | Open-Meteo marine | 43,848 | see manifest |
| 6 | `data/raw_rainfall.csv` | RAW superseded — **precip NOT taken from here** | Open-Meteo archive | 43,848 | see manifest |
| 7 | `data/raw_tide_marea.csv` | RAW **unused by replay** | Marea/tide service | 43,855 | see manifest |

Status: rows 1–7 `VERIFIED_FROM_FILE` for content; provider identity `DOCUMENTED_ONLY` throughout (D-07).

**Lineage, verified from code comments and read statements:**

```
Open-Meteo archive  --collect_raw_v2.py-->  raw_weather_sea.csv  ──┐
                                                                   ├─ inner join on 'time' ─→ replay rows
Open-Meteo marine   --collect_raw_v2.py-->  raw_marine_era5_sea.csv┘   (PRIMARY)
                                        └─→ raw_marine_mfwam.csv  ──→  (RESOLUTION)
```

Canonical configuration is declared in `scripts/historical_replay.py:117-132` as "v2 SEA-CELL"; the three land-cell files are retained for comparison only and explicitly condemned there by F-10.

---

## 3. Table 2 — Manuscript targets vs independently computed counts

| Quantity | Manuscript (target, unverified until recomputed) | **Computed from file** | Verdict |
|---|---:|---:|---|
| PRIMARY records | 43,848 | **43,848** | **MATCH** |
| PRIMARY departure-window hours | 9,135 | **9,135** | **MATCH** |
| RESOLUTION usable records | 28,501 | **28,501** | **MATCH** |
| RESOLUTION departure-window hours | 5,935 | **5,935** | **MATCH** |
| RESOLUTION missing wave excluded | 11 | **11** | **MATCH** |

`COMPUTED_FROM_FILE`. Derivations, none hard-coded:

- PRIMARY: inner join of `raw_weather_sea.csv` × `raw_marine_era5_sea.csv` on `time` = 43,848 rows, 1:1, zero nulls in wind, wave or precip → usable 43,848. Window hours at `05 ≤ hour ≤ 09` = 9,135 = 1,827 days × 5 slots.
- RESOLUTION: inner join with `raw_marine_mfwam.csv` = 28,512 rows = 1,188 days × 24. Minus 11 null `wave_height` = **28,501**. Window hours 1,188 × 5 = 5,940, minus the 5 nulls falling at 05:00–09:00 = **5,935**.

**Target counts were never written into a computed field.** The script computes, then compares.

---

## 4. Table 3 — Temporal coverage, timezone and filter rule

| File | First | Last | Days | Dup. | Non-hourly steps | Window 05–09 incl. |
|---|---|---|---:|---:|---:|---:|
| `raw_weather_sea.csv` | 2020-01-01T00:00 | 2024-12-31T23:00 | 1,827 | 0 | 0 | 9,135 |
| `raw_marine_era5_sea.csv` | 2020-01-01T00:00 | 2024-12-31T23:00 | 1,827 | 0 | 0 | 9,135 |
| `raw_marine_mfwam.csv` | 2021-10-01T00:00 | 2024-12-31T23:00 | 1,188 | 0 | 0 | 5,940 |
| `raw_tide_marea.csv` | 2020-01-01T**08:00** | **2025-01-01T07:20** | 1,828 | 0 | **10** | — |

**Endpoint convention settled** (`COMPUTED_FROM_FILE`, D-04): inclusive of both 05:00 and 09:00 — five hourly slots per complete day. The half-open alternative `05 ≤ h < 09` yields **7,308**, which does not match the manuscript. 1,827 days confirms the 2020 leap year is included (366+365+365+365+366).

**Timezone** (`DOCUMENTED_ONLY`, D-03): timestamps are timezone-**naive** in-file. Every Open-Meteo file's metadata declares `timezone=Asia/Kuching`, `utc_offset_seconds=28800`, and the retrieval scripts request `TIMEZONE = "Asia/Kuching"` (`collect_raw_v2.py:53`). The series is therefore **already local** and **no UTC→local conversion exists anywhere in the pipeline**. This is correct on the provider's documented behaviour but is an assumption inherited from the request — a single mis-set parameter would shift the whole window by eight hours and would be undetectable from the stored artefacts. The audit built Asia/Kuching-aware copies in memory and confirmed the +08:00 offset is constant across the record (no DST in this zone).

`raw_tide_marea.csv` is the exception: **no metadata block, no declared timezone, no coordinates**, a 08:00 start suggesting an undocumented offset applied at download, ten 20-minute steps, a wholly empty `date` column, and coverage past the study window. It is read by **none** of the four canonical scripts (D-06).

---

## 5. Table 4 — Wave availability and the 11 exclusions

| | |
|---|---|
| Variable | `wave_height (m)` in `raw_marine_mfwam.csv` |
| Nulls | **exactly 11** |
| Timestamps | `2021-10-01T00:00` … `2021-10-01T10:00`, **contiguous** |
| Inside 05:00–09:00 | **5** (05, 06, 07, 08, 09) |
| Effect | 28,512 − 11 = **28,501**; 5,940 − 5 = **5,935** |

`COMPUTED_FROM_FILE`. The mechanism is a **single leading gap on the product's first day**, not scattered dropout — the MFWAM series effectively begins at 11:00 on 2021-10-01.

**A near-miss worth recording** (D-02): `wave_period (s)` in the same file has **35** nulls, not 11 — 11 on 2021-10-01, 13 on 2023-10-31, 11 on 2023-11-01. The manuscript's figure of 11 is correct **for the variable actually used**: `scripts/historical_replay.py:136` drops NA on exactly `["wind_speed_10m (kn)", "wave_height (m)", "precipitation (mm)"]`, and `wave_period` appears nowhere in any analysis script. Had `wave_period` ever entered a rule, the usable count would fall below 28,501.

**Marine warnings** (D-05, `VERIFIED_FROM_FILE`): a column-name scan of all seven raw files found **no marine-warning column of any kind**. Any conference treatment of historical marine warnings is therefore a **modelling assumption with no local data behind it**. A constant SAFE must not be read as observed absence of warnings.

---

## 6. Table 5 — Coordinates, observed cells and source

**One point was requested. Three different cells came back.**

| Stream | Requested | Returned cell | Displacement | Status |
|---|---|---|---:|---|
| wind / precip / WMO | 5.98 N, 116.01 E | 5.940246, 116.025 | 4.72 km | `VERIFIED_FROM_FILE` |
| wave — ERA5-Ocean (PRIMARY) | 5.98 N, 116.01 E | 6.0, 116.0 | 2.48 km | `VERIFIED_FROM_FILE` |
| wave — MFWAM (RESOLUTION) | 5.98 N, 116.01 E | 5.958336, 116.04167 | 4.25 km | `VERIFIED_FROM_FILE` |
| *(land, condemned)* | 5.98 N, 116.01 E | 5.940246, 116.100006 | 10.89 km | `VERIFIED_FROM_FILE` |

The three manuscript coordinates all match their files to ≤ 0.05 km, i.e. rounding only. But the **requested** point `LATITUDE = 5.98, LONGITUDE = 116.01` (`collect_raw_v2.py:51-52`) appears nowhere in the manuscript, so a reader cannot tell the stated coordinates are provider-snapped grid centres rather than the study site (D-11). Selection is provider nearest-cell snapping, `INFERRED` from Open-Meteo behaviour; no interpolation flag is stored and the requested point is not recorded in the files.

**Cross-stream separation — and a confound** (D-12): the classifier joins wind and precipitation from one cell to waves from another.

| Pair | Separation |
|---|---:|
| wind cell ↔ ERA5 wave cell (PRIMARY) | **7.20 km** |
| wind cell ↔ MFWAM wave cell (RESOLUTION) | **2.73 km** |
| ERA5 wave cell ↔ MFWAM wave cell | 6.53 km |

So switching PRIMARY → RESOLUTION changes **two things at once**: the wave product, and the wind–wave co-location distance. **The contrast is not a clean single-factor resolution comparison.** This audit cannot apportion any observed difference between the two factors — that would be a new experiment and is out of Step 2 scope. It does mean the contrast should not be described as resolution-only.

No claim is made here about validation against local vessel experience.

---

## 7. Table 6 — Original code vs actual preprocessing behaviour

| Documented behaviour | Observed in file / code | Status |
|---|---|---|
| `skiprows=3` on Open-Meteo CSVs | 2 metadata lines + 1 blank, header on line 4 | `VERIFIED_FROM_FILE` |
| Canonical = v2 sea cell | `historical_replay.py:117-132`; both canonical files carry the sea-cell coordinates | `VERIFIED_FROM_FILE` |
| Precip from the sea file, not `raw_rainfall.csv` | `condition_comparison.py:132` comment; `:135` reads `raw_weather_sea.csv` | `VERIFIED_FROM_FILE` |
| Exclusion = dropna on wind, wave, precip | `historical_replay.py:136` | `VERIFIED_FROM_FILE` |
| Units: wind kn, wave m, precip mm | declared in column headers; consistent with the 21.6/27.0 kn, 1.0/1.25 m, 10/20 mm thresholds | `VERIFIED_FROM_FILE` header-declared; **not** cross-checked against a provider data dictionary |
| Deterministic, no RNG | no `seed`/`random` in any of the four canonical scripts | `VERIFIED_FROM_FILE` |
| `pandas==2.3.3`, `numpy==2.2.6` | file states it was written 2026-10-08, **after** the September 2026 runs, and that no dependency file existed before | `DOCUMENTED_ONLY` — retrospective reconstruction, not a captured environment |
| Five all-empty columns in superseded files | `openmeteo_raw_download.py:55` records the product does not provide partitioned components; not a download error | `VERIFIED_FROM_FILE` (D-09) |

Nothing was re-executed. No command that would write over an original was run; none was needed, since the audit reads only.

---

## 8. Table 7 — Blockers and Step 3 decision

| ID | Severity | Finding | Blocks |
|---|---|---|---|
| D-08 | **HIGH (interpretive)** | 100% reanalysis; `decision_time_availability = UNKNOWN` for every record | any decision-time availability claim — **permanently** |
| D-12 | **HIGH (interpretive)** | PRIMARY/RESOLUTION confounds wave product with wind–wave co-location (7.20 → 2.73 km) | attribution of any PRIMARY/RESOLUTION difference |
| D-03 | MEDIUM | local-time claim is `DOCUMENTED_ONLY` | nothing; one UTC request would settle it |
| D-05 | MEDIUM | no marine-warning column exists anywhere | promoting the warning treatment to an observation |
| D-06 | MEDIUM | tide file has no timezone/coordinates and is unused | nothing; must be excluded explicitly |
| D-07 | MEDIUM | no provider manifest or published checksum | external authenticity claims only |
| D-11 | MEDIUM | stated coordinates are snapped cells, not the requested site | site-representativeness claims |
| D-01, D-02, D-04, D-09, D-10 | INFO / LOW | resolved on inspection; see register | nothing |

### Decision: **GO WITH CONDITIONS** for A18.1 Step 3

**Why GO.** The data needed to reconstruct the governance rules is present, integral and traceable. All four counts reproduce exactly by an independent reader. Lineage is explicit in code. Every null is explained. No input was altered.

**The conditions**, all of which are documentation or framing rather than new work:

1. Pin the configuration by **flag, not filename** — the land-cell files are one careless path away (D-01).
2. Carry `decision_time_availability = UNKNOWN` forward verbatim; do not let Step 3/4 wording imply a fisher had this information (D-08).
3. Describe PRIMARY vs RESOLUTION as a **two-factor** change (D-12).
4. State the marine-warning treatment as an assumption (D-05) and exclude tide explicitly (D-06).
5. Report the requested point 5.98/116.01 beside the three returned cells (D-11).
6. Keep `wave_period` out of every rule, or re-derive the counts (D-02).

**Step 4 blockers: none identified** for count reproduction. The governance percentages were not tested here, by design.

### Assurance claims, kept separate

| Claim | Status |
|---|---|
| Provenance completeness | **PARTIALLY_VERIFIED** — lineage traced in code; provider manifest absent |
| Dataset integrity | **VERIFIED** — hashed, zero duplicates, strict hourly cadence, nulls fully accounted |
| Processing reproducibility (counts) | **VERIFIED** — four of four reproduced independently |
| Operational information availability | **UNKNOWN** for 100% of records — not closable locally |

---

## 9. Integrity of the audit itself

All raw inputs remain **byte-identical**: SHA-256 recomputed after the audit matches the value taken before it, for every file inspected. Full list in `08_manifest_sha256.txt`, which also hashes the generated outputs.

```
96850d7547189ffa5ccc02a36cf69987bfae742e54b61597c2ca7d251e84c424  data/raw_weather_sea.csv
6754e2c2ee5586ee864e590f1ccf363bbd8840b364763e01e8c9eb05e5d63888  data/raw_marine_era5_sea.csv
e9f323e086a3e9dddd29129bda6dbbea7590bbdcc9a1500c0460ca18233bf60f  data/raw_marine_mfwam.csv
5574b88ea65168b6ef5e308629f3eb14fb70f8688a592fde279103ea4b37eae6  data/prediction-register.csv
```

These are **local** hashes. They prove local byte-integrity. They do **not** establish that the bytes came from ERA5, MFWAM or Open-Meteo (D-07).

No fabricated provenance, checksum, warning event, forecast availability or safety label appears anywhere in these artefacts. Where evidence was absent the finding is recorded as `UNKNOWN` or `DOCUMENTED_ONLY` rather than filled in.
