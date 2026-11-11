# Audit Investigation — C-1: RESOLUTION Data Provenance

**Scope:** Finding C-1 only, from the independent pre-submission audit of the AAI 2026 manuscript.
**Manuscript under investigation:** `publications/active/aai-2026/drafts/aai-2026-manuscript-v6-rewrite-v2.docx` (saved to the repository this session as the latest version).
**Investigation date:** 8 October 2026
**Mode:** read-only. No manuscript, script, dataset, configuration or report was modified. No experiment was re-run.

---

## A. Executive Finding

**Classification: PARTIALLY CONFIRMED.**

The two concerns resolve in opposite directions, and both resolve conclusively against repository evidence.

**Concern B (record counts) — NOT SUPPORTED, and already documented.** Both discrepancies are fully explained by the primary data file. `data/raw_marine_mfwam.csv` contains **28,512** hourly rows spanning `2021-10-01T00:00` to `2024-12-31T23:00` local (Asia/Kuching, GMT+8), with **zero gaps and zero duplicates**. The first **11** rows carry `NaN` wave heights, contiguously, from `2021-10-01T00:00` to `2021-10-01T10:00` inclusive. The canonical pipeline drops them at `scripts/condition_comparison.py:148` (`dropna`), giving **28,501** usable records. All five of 1 October 2021's departure-window hours (05:00–09:00) fall inside that NaN block, so the window denominator is 5,940 − 5 = **5,935**. Both manuscript figures are exact. The repository had already recorded this in `docs/canonical/data-provenance.md:73` — *"28,512 (3.25 y), 11 NaN"* — before the audit was written.

The auditor's hypothesis that the record "may begin at 11:00 on 1 October 2021" is **correct as to the first valid observation** but **wrong as to mechanism**: the file is complete and begins at 00:00; the first eleven values are missing, not the first eleven rows.

**Concern A (temporal provenance) — PARTIALLY CONFIRMED, with the substantive sub-claim contradicted.**

- *Contradicted:* the returned data **does** cover October 2021. There are **733 valid wave observations in October 2021** (744 hours less the 11 NaN), ranging 0.22–1.56 m across 59 distinct values. They are real varying observations, not fill. Whatever the published CMEMS coverage dates say, the series the experiment consumed is populated from 1 October 2021.
- *Confirmed:* the manuscript's provenance description is **imprecise**. The wave data was **not** obtained from Copernicus Marine. It came from the **Open-Meteo Marine API** with `models=meteofrance_wave` (`scripts/collect_raw_v2.py:145`). The attribution to Copernicus product `GLOBAL_ANALYSISFORECAST_WAV_001_027` is an inference from provider documentation, recorded as such in `aai-2026-manuscript-v1-prefinal.md:265`: *"The ~8 km figure and the October 2021 record start trace to the Open-Meteo documentation."* No request, response, manifest or log in the repository names that CMEMS product.
- Also confirmed: the manuscript's sentence *"Records were retrieved through the Open-Meteo archive [12], [13]"* cites the **weather** archive API [12] and **ERA5** [13]. The marine data came through a **different Open-Meteo endpoint** (`marine-api.open-meteo.com/v1/marine`), which the sentence does not cover.

**Submission risk: LOW–MODERATE, and fully correctable by two clarifying sentences.** No result changes. No record count changes. No dataset period changes. The numbers are sound and traceable; the provenance *description* understates one layer of indirection, and a reviewer who checks the CMEMS product page — as the independent auditor did — will raise exactly this.

---

## B. Evidence Inventory

| File path | Location | What the evidence establishes | Strength |
|---|---|---|---|
| `data/raw_marine_mfwam.csv` | header line 2 | Returned grid cell `5.958336, 116.04167`; `utc_offset_seconds=28800`; timezone `Asia/Kuching` (GMT+8). Timestamps are **local**, not UTC. | **Direct — primary artefact** |
| `data/raw_marine_mfwam.csv` | first/last data rows | First `2021-10-01T00:00`, last `2024-12-31T23:00`. 28,512 data rows. | **Direct — primary artefact** |
| `data/raw_marine_mfwam.csv` | rows 1–11 of data | 11 contiguous `NaN` wave heights, `2021-10-01T00:00` → `2021-10-01T10:00`. First valid observation `2021-10-01T11:00`. | **Direct — primary artefact** |
| `data/raw_marine_mfwam.csv` | all October 2021 rows | 733 valid observations, 0.22–1.56 m, 59 distinct values — genuine varying data, not fill | **Direct — primary artefact** |
| `data/raw_weather_sea.csv` | header + all rows | 43,848 rows, `2020-01-01T00:00` → `2024-12-31T23:00`, cell `5.940246, 116.025`, **zero NaN in every column** | **Direct — primary artefact** |
| `scripts/collect_raw_v2.py` | line 145 | `"models": "meteofrance_wave"` — the model identifier actually requested | **Direct — code** |
| `scripts/collect_raw_v2.py` | line 150 | Endpoint `https://marine-api.open-meteo.com/v1/marine` — **Open-Meteo, not Copernicus** | **Direct — code** |
| `scripts/collect_raw_v2.py` | lines 58–59 | `MFWAM_MIN_START = "2021-10-01"` with the comment *"MFWAM coverage begins Oct 2021 — earlier dates will return empty or error"* | **Direct — code + author's stated assumption** |
| `scripts/collect_raw_v2.py` | line 140 | `mfwam_start = max(args.start, MFWAM_MIN_START)`; defaults `--start 2020-01-01`, `--end 2024-12-31` (lines 100–101) → **requested interval 2021-10-01 → 2024-12-31** | **Direct — code** |
| `scripts/collect_raw_v2.py` | lines 147–148 | `cell_selection: "sea"`, `timezone: Asia/Kuching`, `format: csv` | **Direct — code** |
| `scripts/condition_comparison.py` | lines 135–136 | Loads `raw_weather_sea.csv` + the configured marine file, `skiprows=3` | **Direct — code** |
| `scripts/condition_comparison.py` | line 148 | `d.dropna(subset=["wave","wind","precip"])` — **the mechanism that turns 28,512 into 28,501** | **Direct — code** |
| `scripts/condition_comparison.py` | line 213 | `dep = (d.hour >= 5) & (d.hour <= 9)` — the departure-window implementation, 5 hours/day inclusive | **Direct — code** |
| `scripts/condition_comparison.py` | line 125 | `"RESOLUTION (3.25 yr, sea wind + MFWAM ~8 km)": "raw_marine_mfwam.csv"` | **Direct — code** |
| `data/c8/canonical-results-post-migration.txt` | line 232 | `Loaded 28,501 hourly records  2021-10-01 to 2024-12-31` | **Direct — stored execution output** |
| `data/c8/canonical-results-post-migration.txt` | line 249 | `DEPARTURE WINDOW 05:00-09:00   (n = 5,935 hours)` | **Direct — stored execution output** |
| `data/c8/canonical-results-post-migration.txt` | line 251 | `state distribution: SAFE 3,231 (54.4%)  CAUTION 266 (4.5%)  UNSAFE 2,438 (41.1%)` | **Direct — stored execution output** |
| `data/c8/canonical-results-post-migration.txt` | lines 257–260 | C0↔C1 = 41.08%, C0↔C2 = 45.56%, C1↔C2 = 4.48%, C1↔C3 = 0.00% | **Direct — stored execution output** |
| `data/c8/canonical-results-post-migration.txt` | lines 215, 223, 251 | PRIMARY n = 9,135; 42.88% / 48.69%; CAUTION 531 | **Direct — stored execution output** |
| `docs/canonical/data-provenance.md` | line 73 | `Records | 43,848 (5 y) | 28,512 (3.25 y), 11 NaN` — **the 11 NaN rows were already documented** | **Direct — canonical record** |
| `docs/canonical/data-provenance.md` | line 96 | *"Source: Open-Meteo Marine API — `marine-api.open-meteo.com/v1/marine`"* | **Direct — canonical record** |
| `docs/canonical/data-provenance.md` | lines 67–69 | MFWAM *"Delivered via Copernicus Marine (CMEMS), GLOBAL_ANALYSISFORECAST_WAV_001_027"*; *"0.08° ≈ 8 km"*; *"Oct 2021 → present"* | **Canonical record, but a provider-documentation claim, not an observation** |
| `docs/canonical/data-provenance.md` | lines 106–111 | Open-Meteo marine model table: *"MeteoFrance MFWAM | ~8 km | Oct 2021"* — the origin of the Oct 2021 start date | **Direct — shows the source of the assumption** |
| `publications/.../aai-2026-manuscript-v1-prefinal.md` | line 265 | *"The ~8 km figure and the October 2021 record start trace to the Open-Meteo documentation"* | **Direct — the authors' own earlier statement** |
| `publications/.../aai-2026-phase7-evidence-resolution.md` | line 105 | *"MFWAM is Météo-France's third-generation wave model, distributed as Copernicus Marine product GLOBAL_ANALYSISFORECAST_WAV_001_027 … stated spatial resolution 0.083° × 0.083°"* | **Inference from the Copernicus catalogue, documented as such** |
| `git log -- data/raw_marine_mfwam.csv` | commit `21695e0` | First committed **2026-09-06 12:55:31 +0800**, in the same commit as `scripts/collect_raw_v2.py` | **Direct — version control** |
| `git log -- data/c8/canonical-results-post-migration.txt` | commit `babe92f` | Committed **2026-09-08 21:06:22 +0800** | **Direct — version control** |

**What does not exist in the repository:** no HTTP response headers, no stored request URL, no API manifest, no download log, no retrieval-timestamp file. `scripts/collect_raw_v2.py`'s `download()` (lines ~63–74) prints the URL to stdout but writes no log. The retrieval date is therefore known only to commit-date precision.

---

## C. Data Provenance

| Question | Answer | Basis |
|---|---|---|
| **Actual provider** | **Open-Meteo** — `https://marine-api.open-meteo.com/v1/marine` | `collect_raw_v2.py:150` (direct) |
| **Actual product / endpoint** | Open-Meteo Marine API, parameter **`models=meteofrance_wave`**, `hourly=wave_height,wave_period`, `cell_selection=sea`, `format=csv`, `timezone=Asia/Kuching` | `collect_raw_v2.py:142–149` (direct) |
| **Requested period** | **2021-10-01 → 2024-12-31** (`max("2020-01-01","2021-10-01")` → `args.end`) | `collect_raw_v2.py:59,100–101,140,146` (direct) |
| **Requested location** | 5.98 N, 116.01 E, sea cell | `collect_raw_v2.py:52–53,148` (direct) |
| **Returned period** | **2021-10-01T00:00 → 2024-12-31T23:00 local (GMT+8)**, 28,512 contiguous hourly slots, no gaps, no duplicates | `raw_marine_mfwam.csv` (direct) |
| **Returned cell** | 5.958336, 116.04167 — 2.7 km from the weather cell | CSV header (direct); distance from `data-provenance.md:161` |
| **First valid observation** | **2021-10-01T11:00 local = 03:00 UTC** | `raw_marine_mfwam.csv` (direct) |
| **Retrieval date** | On or before **2026-09-06** | git commit `21695e0` (direct, bounding) |
| **Underlying wave model** | Open-Meteo's `meteofrance_wave`, which Open-Meteo documents as MFWAM (Météo-France Wave Model) at ~8 km from Oct 2021 | **Provider claim**, recorded at `data-provenance.md:106–111` |
| **Link to CMEMS `GLOBAL_ANALYSISFORECAST_WAV_001_027`** | **Inference.** Phase-7 evidence work identified MFWAM as being distributed as that CMEMS product and adopted its DOI. **No repository artefact ties the Open-Meteo feed to that specific product identifier or version.** | `aai-2026-phase7-evidence-resolution.md:105,217` (inference, documented as such) |
| **Does the data cover October 2021?** | **Yes.** 733 valid observations in October 2021, 0.22–1.56 m, 59 distinct values. | `raw_marine_mfwam.csv` (direct) |
| **Does the manuscript describe provenance accurately?** | **Not fully.** It attributes the wave data to a Copernicus product, and its retrieval sentence cites the Open-Meteo *weather archive* API and ERA5, neither of which served the marine data. | Manuscript §IV vs `collect_raw_v2.py:150` |

### Separation of evidence types

- **Directly observed:** the endpoint, the model parameter, the requested interval, the returned interval, the 11 NaN rows, the returned grid cell, the October 2021 values, the commit dates, and every reported RESOLUTION figure.
- **Provider claim (not independently verified here):** that Open-Meteo's `meteofrance_wave` is MFWAM; that its resolution is ~8 km; that its archive begins October 2021.
- **Assumption embedded in the scripts:** `MFWAM_MIN_START = "2021-10-01"` — a hard-coded constant justified by a code comment referencing Open-Meteo's model table, not by a tested response.
- **My inference:** that the 11 NaN hours mark the true start of Open-Meteo's `meteofrance_wave` archive at 03:00 UTC on 1 October 2021. This is consistent with the data but not proven by it — the NaNs could equally be a source-side gap at the start of the month.

### Remaining uncertainty

The repository cannot establish whether Open-Meteo's `meteofrance_wave` archive is sourced from CMEMS `GLOBAL_ANALYSISFORECAST_WAV_001_027` specifically, from another Météo-France MFWAM distribution, or from a back-extended reconstruction. The external auditor's observation that CMEMS publishes later coverage start dates for that product (2021-11-30 / 2022-06-01 / 2022-11-01) is **not contradicted** by this investigation — it is simply not the series the experiment used. Both can be true: Open-Meteo may serve an archive that reaches further back than the CMEMS near-real-time product page advertises.

---

## D. Timestamp and Count Reconciliation

### D.1 Measured facts — `data/raw_marine_mfwam.csv`

| Property | Value |
|---|---|
| Data rows | **28,512** |
| First timestamp | `2021-10-01T00:00` |
| Last timestamp | `2024-12-31T23:00` |
| Time zone | `Asia/Kuching`, `utc_offset_seconds = 28800` (GMT+8) — **timestamps are local** |
| Unique timestamps | 28,512 |
| Duplicate timestamps | **0** |
| Expected slots over the span | 28,512 — **gaps = 0**, continuous hourly sequence |
| NaN `wave_height` rows | **11**, contiguous, `2021-10-01T00:00` → `2021-10-01T10:00` |
| First valid observation | **`2021-10-01T11:00`** |
| Non-NaN rows | **28,501** |
| Rows in 05:00–09:00, all | 5,940 |
| Rows in 05:00–09:00, non-NaN | **5,935** |
| First day partial? | **No** — the day is present in full; its first 11 values are missing |
| Last day partial? | **No** — complete through 23:00 |

### D.2 The arithmetic

```
Calendar span            1 Oct 2021 .. 31 Dec 2024 inclusive = 1,188 days
Expected hourly slots    1,188 × 24                          = 28,512   ← matches file exactly
Leading NaN wave values                                      =     11
Usable records           28,512 − 11                         = 28,501   ← MANUSCRIPT ✔

Expected window hours    1,188 days × 5 h (05,06,07,08,09)   =  5,940
Window hours inside the NaN block (2021-10-01 05:00–09:00)   =      5
Usable window hours      5,940 − 5                           =  5,935   ← MANUSCRIPT ✔
                         = 1,187 complete days × 5
```

### D.3 Against the auditor's expectations

| Quantity | Auditor expected | Manuscript | File | Verdict |
|---|---|---|---|---|
| Hourly records | 28,512 | 28,501 | 28,512 rows, 28,501 usable | **Both right, different things.** The auditor counted rows; the manuscript counts usable records. |
| Window hours | 5,940 | 5,935 | 5,940 rows, 5,935 usable | Same. |
| 11-hour difference | unexplained | — | **11 contiguous leading NaN** | **Fully explained.** |
| 5-hour window difference | unexplained | — | Day 1's whole window sits in the NaN block | **Fully explained.** |
| "data may begin at 11:00 on 1 Oct 2021" | hypothesis | — | First *valid* value is `2021-10-01T11:00` | **Correct as to effect; wrong as to mechanism.** |

### D.4 Why the filter is the whole explanation

`scripts/condition_comparison.py:148` drops rows with NaN in `wave`, `wind` or `precip`. `raw_weather_sea.csv` was measured to contain **zero NaN in any column across all 43,848 rows**, and the inner join is on an exact hourly timestamp with no gaps on either side. The wave column is therefore the *only* source of loss, and it loses exactly 11 rows. The reconciliation is complete with no residual.

### D.5 PRIMARY, as a control

| Property | Value |
|---|---|
| `raw_marine_era5_sea.csv` rows | 43,848, `2020-01-01T00:00` → `2024-12-31T23:00`, 0 gaps, 0 duplicates, **0 NaN** |
| Window rows (05–09) | 9,135 = 1,827 × 5 |

PRIMARY reconstructs exactly with no filtering, which is why it showed no discrepancy. The asymmetry the auditor noticed is real and has a mundane cause.

---

## E. Experimental Result Traceability

Every RESOLUTION figure in the manuscript appears verbatim in a stored execution artefact: **`data/c8/canonical-results-post-migration.txt`** (committed `babe92f`, 2026-09-08 21:06:22 +0800), produced by `scripts/condition_comparison.py`.

| Manuscript figure | Artefact line | Artefact text |
|---|---|---|
| 28,501 hourly records | 232 | `Loaded 28,501 hourly records  2021-10-01 to 2024-12-31` |
| 5,935 denominator | 249 | `DEPARTURE WINDOW 05:00-09:00   (n = 5,935 hours)` |
| CAUTION 266 hours | 251 | `state distribution: SAFE 3,231 (54.4%)   CAUTION 266 (4.5%)   UNSAFE 2,438 (41.1%)` |
| C0↔C1 = 41.08% | 257 | `C0 ungated  —  41.08%  41.08%  45.56%` |
| C0↔C2 = 45.56% | 257 | same row |
| Δ<sub>L2</sub> = 4.48% | 258 | `C1 binary-gated  41.08%  —  0.00%  4.48%` |
| C1↔C3 = 0.00% | 258–259 | same block |

**Internal consistency of the artefact** (arithmetic performed here on the artefact's own counts, not a re-run):

```
SAFE 3,231 + CAUTION 266 + UNSAFE 2,438 = 5,935            ✔ partition complete
UNSAFE / n          = 2,438 / 5,935 = 41.0783%  → 41.08%   ✔
(CAUTION+UNSAFE)/n  = 2,704 / 5,935 = 45.5602%  → 45.56%   ✔
CAUTION / n         =   266 / 5,935 =  4.4819%  →  4.48%   ✔
45.56 − 41.08 = 4.48                                        ✔
```

PRIMARY, for completeness: SAFE 4,687 + CAUTION 531 + UNSAFE 3,917 = 9,135; 3,917/9,135 = 42.88%; 4,448/9,135 = 48.69%; 531/9,135 = 5.81% (artefact lines 217, 223).

`docs/analysis/experiment-report-delta-l2.md:16,395` additionally records that the canonical scripts were re-executed on **2026-09-21** (Python 3, pandas 2.3.3, numpy 2.2.6) and *"reproduced 5.81% / 4.48% / 0.00% / 42.88% / 48.69% exactly."*

**Statement of limits.** The figures are **traceable** to a stored artefact and that artefact is **internally consistent**. This investigation did **not** re-execute `condition_comparison.py`, and nothing here should be read as an independent reproduction of the governance results.

---

## F. Assessment of Auditor C-1

| Auditor claim | Status | Basis |
|---|---|---|
| "The cited Copernicus product may not provide historical coverage back to October 2021" | **Correct about the CMEMS product, irrelevant to the experiment** | The CMEMS coverage dates are not disputed here; the data did not come from CMEMS. The series actually used is populated from 1 Oct 2021. |
| "Eight to thirteen months of the claimed study period does not exist in the cited product" | **Incorrect as applied** | 733 valid October 2021 observations and a continuous series thereafter. The premise that the manuscript's data is the CMEMS feed is what fails. |
| "The record counts do not reconcile with the stated period by 11 hours" | **Correct arithmetic, wrong inference** | 1,188 × 24 = 28,512 is right. The deficit is 11 NaN values, not 11 absent hours — and it was already documented at `data-provenance.md:73`. |
| "5,940 expected vs 5,935 reported" | **Correct arithmetic, wrong inference** | Same mechanism. |
| "The data may begin at 11:00 on 1 October 2021" | **Correct as to the first valid observation; wrong as to mechanism** | File begins 00:00; first non-NaN is 11:00. |
| "These two findings point at the same place" | **Correct** | They do — both at the start of the MFWAM series. |
| Implied: the manuscript's provenance description is imprecise | **Correct, and this is the finding that survives** | The provider is Open-Meteo; the CMEMS attribution is an inference; the retrieval sentence cites the wrong endpoint. |
| Recommendation: "State the exact first and last timestamps … If the data came through Open-Meteo's own blend rather than directly from CMEMS, say so and cite accordingly" | **Correct and actionable** | Adopted below. |

**Classification rationale.** Concern B is not supported — the counts are correct and the explanation was already in the canonical record, so this half of C-1 should be withdrawn. Concern A is partially confirmed — not as a coverage gap (there is none in the data used), but as a **provenance-description** defect: the manuscript names a Copernicus product as the wave-data source when the access route was Open-Meteo's `meteofrance_wave` model, and the CMEMS attribution is an inference the manuscript presents as fact. That is a real and fixable reporting problem, which is why the classification is PARTIALLY CONFIRMED rather than NOT SUPPORTED.

---

## G. Recommended Manuscript Action

### G.1 Provenance sentence

**Exact original text (§IV):**

> "The RESOLUTION configuration covers October 2021 to December 2024, comprising 28,501 hourly records with wave data from MFWAM [11] at approximately 8 km resolution, giving a denominator of 5,935 hours. Records were retrieved through the Open-Meteo archive [12], [13]."

**Minimal replacement:**

> "The RESOLUTION configuration covers 1 October 2021 to 31 December 2024, comprising 28,501 usable hourly records of 28,512 in the interval — the first eleven wave values are unavailable — giving a denominator of 5,935 hours. Wave data are Open-Meteo's `meteofrance_wave` series [12], which the provider documents as the Météo-France MFWAM model [11] at approximately 8 km resolution. Weather records were retrieved through the Open-Meteo archive API [12], [13]."

**Scientific justification.** Three changes, each evidence-driven and none touching a result:

1. *"28,501 usable hourly records of 28,512 in the interval — the first eleven wave values are unavailable"* pre-empts the exact arithmetic check the auditor performed. The reader can now reconcile 28,501 and 5,935 from the printed text. Evidence: `raw_marine_mfwam.csv`, `condition_comparison.py:148`, `data-provenance.md:73`.
2. *"Open-Meteo's `meteofrance_wave` series … which the provider documents as"* states the access route observed in `collect_raw_v2.py:145,150` and marks the MFWAM identification as a provider claim rather than a direct observation. This is the honest form, and it is what `aai-2026-manuscript-v1-prefinal.md:265` already says internally.
3. *"Weather records were retrieved through the Open-Meteo archive API"* corrects a scope error: the marine data came from a different endpoint.

### G.2 Does reference [11] need correction?

**No — but its role should change.** [11] remains the correct citation for the MFWAM model itself, and the DOI resolves to the right product. What is wrong is not the reference but the implication that the data was obtained from it. Under the replacement sentence, [11] is cited for the *model*, [12] for the *series actually used*. No change to the reference entry is required.

**One optional precision point, outside C-1's remit but adjacent:** the Copernicus product page gives 0.083° ≈ 9.3 km, while "approximately 8 km" is Open-Meteo's figure (`data-provenance.md:106–111`). If the sentence is rewritten to attribute the series to Open-Meteo, "approximately 8 km" becomes consistent with its stated source and needs no change. If the attribution stays with Copernicus, the resolution figure should become ~9 km.

### G.3 What must not change

Dataset period, source citation list, record counts and every numerical result stand as published. Nothing in the repository supports altering them, and this investigation found no error in any of them.

---

## H. Unresolved Questions

1. **Whether Open-Meteo's `meteofrance_wave` archive is sourced from CMEMS `GLOBAL_ANALYSISFORECAST_WAV_001_027`.** The repository records this as an inference from two documentation sources. It cannot be confirmed or refuted from repository evidence, and it is the one claim a determined reviewer could still press. Resolving it requires a statement from Open-Meteo about its marine data sourcing — not a repository artefact.

2. **Why the first eleven hours are NaN.** Consistent with an archive beginning at 03:00 UTC on 1 October 2021, but equally consistent with a source-side gap. The repository contains no response metadata that would distinguish them.

3. **Exact retrieval timestamp.** Known only as "on or before 2026-09-06 12:55:31 +0800" (commit `21695e0`). `collect_raw_v2.py`'s `download()` prints the request URL to stdout but writes no log, so no stored artefact records the retrieval moment. *Recommendation for future collections, not for this manuscript: have `download()` write the full request URL and the response date to a sidecar file.*

4. **Open-Meteo's MFWAM temporal resolution.** `data-provenance.md:81–89` records that Open-Meteo's model table lists MFWAM as 3-hourly, and that a second-difference test found no linear-interpolation signature. I measured mean identical-consecutive-value run lengths of **2.16** for MFWAM against **2.45** for the known-hourly ERA5-Ocean series — no evidence of 3-hourly step-holding. The documented discrepancy remains formally open but is not supported by the data. **Outside C-1's scope**; noted only because it concerns the same file.

---

## I. Final Verdict

> ## MINOR CLARIFICATION REQUIRED

Two sentences in §IV. No result, count, period or reference changes.

The record-count half of C-1 should be **withdrawn** — the counts are correct, the mechanism is documented in the canonical record, and the manuscript's figures are exact. The provenance half should be **upheld in narrowed form**: not as a coverage gap, but as a description that names a Copernicus product where the data came through Open-Meteo, and that presents a provider-documentation inference as an established fact.

---

### Appendix — reproducing these checks

Every measurement in this report can be re-derived read-only from the repository:

```bash
# counts, timestamps, NaN block
python3 - <<'EOF'
lines = open('data/raw_marine_mfwam.csv').read().split('\n')
hi = [i for i,l in enumerate(lines) if l.startswith('time,')][0]
rows = [l.split(',') for l in lines[hi+1:] if l.strip()]
ts  = [r[0] for r in rows]; wh = [r[1] for r in rows]
nan = [t for t,v in zip(ts,wh) if v.upper()=='NAN']
print(len(rows), ts[0], ts[-1], len(set(ts)), len(nan), nan[0], nan[-1])
EOF

# stored execution artefact
sed -n '232p;249p;251p;257,260p' data/c8/canonical-results-post-migration.txt

# collection parameters
sed -n '58,59p;140,151p' scripts/collect_raw_v2.py

# the filter that produces 28,501
sed -n '148p;213p' scripts/condition_comparison.py
```
