# AAI 2026 — Reproduction Guide

**Experiment:** *From Declared Risk Levels to Admissible Recommendations: Measuring the Operational Effect of AI Governance Through Deterministic Historical Replay*

**Companion manifest:** `data/c8/aai-2026-reproducibility-manifest.json`
**Written:** 8 October 2026. **Retrospective** — this guide did not exist when the experiments were run.
**Repository snapshot documented:** branch `AMIT-v5`, commit `a7f77d8351ec94c586309d796aabd1230f4886dd`

> **None of the commands in this guide were executed while writing it.** They were derived by reading each script's argument handling. Every command below is labelled **DOCUMENTED — NOT EXECUTED**.
>
> **Writing this guide verified nothing about the experimental results.** It records what is traceable today.

This guide is written for a computer-science researcher who has the repository but has never worked on the project.

---

## 1. What the experiment does

Five years of hourly weather and wave records for one coastal site (Kota Kinabalu, Sabah) are classified into three safety states — SAFE, CAUTION, UNSAFE — by max-severity aggregation over five component classifiers. Four governance configurations (C0–C3) map each state to an admissible set of AI recommendation types. The configurations are replayed over the same classified record and the hours on which two configurations admit different sets are counted.

The headline quantity is

```
Δ_L2 = D(C0,C2) − D(C0,C1)
```

which, for the evaluated mappings, equals P(S = CAUTION).

**It is a deterministic census, not a model-training experiment.** No parameter is estimated, nothing is sampled, and no random seed exists anywhere in the canonical path. Replaying an identical record under an identical configuration returns an identical result.

---

## 2. Canonical datasets

All four are **tracked in git**. Reproduction uses these committed files, not the live API.

| Path | Role | Rows | Coverage (local time, UTC+8) | SHA-256 (first 16) |
|---|---|---|---|---|
| `data/raw_weather_sea.csv` | Wind, precipitation, WMO code — sea cell | 43,848 | 2020-01-01T00:00 → 2024-12-31T23:00 | `96850d7547189ffa` |
| `data/raw_marine_era5_sea.csv` | PRIMARY waves (`era5_ocean`) | 43,848 | same | `6754e2c2ee5586ee` |
| `data/raw_marine_mfwam.csv` | RESOLUTION waves (`meteofrance_wave`) | 28,512 (28,501 usable) | 2021-10-01T00:00 → 2024-12-31T23:00 | `e9f323e086a3e9dd` |
| `data/solar/solar-events-daily.csv` | Frozen sunrise/sunset artefact | 1,827 days | 2020-01-01 → 2024-12-31 | `057c46a19d0e8ea7` |

**Three things to know before you touch the data.**

1. **Timestamps are local time (UTC+8, `Asia/Kuching`).** Every file header carries `utc_offset_seconds = 28800`. This matters: the 05:00–09:00 evaluation window straddles sunrise (05:59–06:32 at this latitude), so interpreting the timestamps as UTC would change the result entirely.
2. **`raw_marine_mfwam.csv` has 11 missing wave values** — contiguous, `2021-10-01T00:00` through `T10:00`. The first valid observation is `2021-10-01T11:00`. The analysis scripts drop them, which is how 28,512 rows become 28,501 usable records and 5,940 window hours become 5,935.
3. **The solar artefact self-certifies its generator.** Its `impl_sha256` column equals the SHA-256 of `scripts/sensitivity/solar.py` (`3b7dc371ebe5931b…c36c`), which is present and unchanged. The daylight classification is traceable to a specific generator.

**Do not re-collect the data to reproduce published results.** Open-Meteo serves a live, unversioned archive and no retrieval timestamp or checksum was recorded at collection time. Re-collection would also overwrite the committed files.

---

## 3. Canonical scripts

| Path | Role | SHA-256 (first 16) | Unchanged since the archived run? |
|---|---|---|---|
| `scripts/condition_comparison.py` | **Main entry point.** Classifier, four governance maps, pairwise divergence, departure window | `3c32913a2a9cc85f` | **Yes** |
| `scripts/canonical_gt.py` | Canonical time classifier `g_t`; imported by every analysis script | `b330bf9f94e848aa` | **Yes** |
| `scripts/sensitivity/threshold_sensitivity.py` | Threshold / vessel-class / denominator sweeps | `6ddaea583941134b` | Changed at `3c70a1d`; unchanged since |
| `scripts/diagnostic_binding.py` | Component attribution and prediction checks | `113b5b92e81535a9` | **Yes** |
| `scripts/canonical_figures.py` | Summary generator | `56c8d4c295b0df7d` | **No** — changed at `f8215e4`, after the capture |
| `scripts/threshold_comparison.py` | Threshold provenance comparison (supporting) | `daed570596df1dbf` | **Yes** |
| `scripts/sensitivity/gt_counterfactual.py` | Time-policy counterfactual (supporting; nothing reported from it) | `eb58508e9159722d` | — |
| `scripts/sensitivity/solar.py` | Solar-table generator certified by the artefact | `3b7dc371ebe5931b` | — |
| `scripts/collect_raw_v2.py` | Data collection (**optional**, see §2) | `c646dc9a575f3f15` | — |

**Not canonical:** `scripts/openmeteo_raw_download.py` is the superseded v1 collector. Its `cell_selection` default returns a *land* cell (defect F-10). Do not use it.

---

## 4. Environment

### What is documented

`docs/analysis/experiment-report-delta-l2.md:395` records a re-execution on **2026-09-21** under **pandas 2.3.3, numpy 2.2.6**, and "Python 3".

### What is not

The **Python minor version, operating system and architecture are UNKNOWN.** No `requirements.txt`, `pyproject.toml`, `setup.py`, `Pipfile` or `environment.yml` existed in the repository before this task. `requirements-aai-2026.txt` is added by this task and records the documented versions; read its header before relying on it.

### What the scripts actually need

Third-party: **pandas** and **numpy**, and nothing else. Everything else is standard library (`argparse`, `csv`, `json`, `math`, `pathlib`, `sys`, `itertools`, `urllib`). `collect_raw_v2.py` additionally needs network access; no analysis script does.

No credentials, no database, no external service, no GPU. All paths resolve relative to the file's own location, so the repository can sit anywhere.

---

## 5. Configuration

Read from code, not from reports.

### Environmental classifier — `scripts/condition_comparison.py`

| Component | CAUTION | UNSAFE | Line |
|---|---|---|---|
| Wind `g_w` | > 21.6 kn | > 27.0 kn | 63 |
| Rainfall `g_r` | > 10.0 mm/h | > 20.0 mm/h, or WMO code ∈ {95, 96, 99} | 72 |
| Ocean `g_o` (small vessel) | 1.0 ≤ wave ≤ 1.25 m | wave > 1.25 m | 76 |
| Time `g_t` | *never* | t < sunrise or t ≥ sunset | `canonical_gt.py` |
| Marine warning `g_m` | — | held at SAFE throughout (declared exclusion) | classifier |

Note the operators: **UNSAFE is strict (`>`), CAUTION is inclusive at both ends.** An hour at exactly 1.25 m is CAUTION.

Aggregation is `max` over the five severities. Departure window: `hour >= 5 and hour <= 9` (line 213), five hours per day.

Vessel-dependent wave boundaries: small `(1.0, 1.25)`, medium `(1.4, 2.8)`, big `(1.5, 3.5)`.

### Governance mappings — lines 85–106, explicit `frozenset` literals

```
FULL       = {Go, Delay, DepartureTime, Duration}
RESTRICTED = {Go, Delay}
EMPTY      = {}

C0:  SAFE FULL | CAUTION FULL       | UNSAFE FULL    (ungated baseline)
C1:  SAFE FULL | CAUTION FULL       | UNSAFE EMPTY   (participation gated)
C2:  SAFE FULL | CAUTION RESTRICTED | UNSAFE EMPTY   (evaluated configuration)
C3:  SAFE FULL | CAUTION FULL       | UNSAFE EMPTY   (identical to C1 by construction)
```

Disagreement is computed as **set inequality** (`x != y`, line 198) over the per-hour admissible sets.

> **One inconsistency, not silently resolved.** The manuscript defines the metric as *"the number of those hours in which one configuration admits a strictly smaller set than another"* — a directional strict-subset rule. The code tests set inequality. The two coincide for all four configurations because every admissible set is a subset of FULL, but they are not the same definition.

The participation gate `G(S)` is defined in `docs/canonical/appendix-c-formalisation.md` C.3 as a function of the *state* (0 at UNSAFE, 1 at SAFE and CAUTION). **It is never computed in the metric path**; no canonical script references it.

### Sensitivity sweeps — `scripts/sensitivity/threshold_sensitivity.py` lines 100–124

- Rainfall `R_C` ∈ {5.0, 7.5, 10.0, 15.0, 19.9}, `R_U` fixed at 20.0
- Wind `W_C` ∈ {18.0, 20.0, 21.6, 22.0, 25.0}, `W_U` fixed at 27.0
- Wave `(O_C, O_U)` ∈ {(0.75, 1.25), **(1.0, 1.25) canonical**, (1.25, 1.5), (1.0, 1.9), (1.4, 2.8), (1.5, 3.5)}
- Time policy **T1 is a denominator restriction**, not a rule change: the evaluation set is narrowed to departure-window ∩ daylight hours while `CANON` is unchanged and `g_t` still runs. Documented denominators: 5,536 (PRIMARY) and 3,594 (RESOLUTION).

The alternative wave UNSAFE boundary is implemented as **1.90 m**, which is the source value **1.875 m** rounded; the rounding is declared at `threshold_comparison.py:36`.

---

## 6. Execution order

```
(optional) collect_raw_v2.py   →  the three raw CSVs  [DO NOT RUN to reproduce published results]
                                          │
                                          ▼
 condition_comparison.py  ──────►  headline comparison + conformance check
 threshold_sensitivity.py ──────►  sensitivity sweeps
 diagnostic_binding.py    ──────►  component attribution
 canonical_figures.py     ──────►  summary table
```

The four analysis scripts are independent of one another. All read the committed CSVs and the solar artefact; none consumes another's output. Run from the **repository root**.

---

## 7. Commands

All **DOCUMENTED — NOT EXECUTED IN THIS TASK.** No CLI flag below was invented; each was read from the script's `argparse` or `sys.argv` handling.

### 7.1 Headline comparison — PRIMARY, RESOLUTION and the C1↔C3 conformance check

```bash
cd <repository root>
python3 scripts/condition_comparison.py
```

One invocation produces both configurations. Output goes to **stdout only**. To preserve it:

```bash
python3 scripts/condition_comparison.py | tee data/c8/condition-comparison-$(date -u +%Y%m%dT%H%M%SZ).txt
```

Optional flag: `--write-register` writes the prediction register. **Omit it** — the read-only default is correct for reproduction.

Expected: state distributions and 4×4 pairwise divergence matrices for ALL HOURS and for DEPARTURE WINDOW 05:00–09:00, both configurations.

### 7.2 Sensitivity analysis

```bash
python3 scripts/sensitivity/threshold_sensitivity.py | tee data/c8/sensitivity-run-$(date -u +%Y%m%dT%H%M%SZ).txt
```

No arguments.

> **Known defect.** Line 150 writes the run to `/tmp/sens_out.txt`. `/tmp` is ephemeral and the September run's output is gone — which is why every sensitivity figure in the manuscript lacks machine evidence. **Always `tee` into `data/c8/`.** A persistent destination should be set in the script itself during a later controlled run; this task did not modify it.

The script recomputes Δ_L2 twice by independent routes — once as P(CAUTION), once from the admissible-set tables (lines 60–66) — and prints `IDENTITY HOLDS` or `IDENTITY FAILS`. Watch that line.

### 7.3 Component attribution

```bash
python3 scripts/diagnostic_binding.py | tee data/c8/binding-run-$(date -u +%Y%m%dT%H%M%SZ).txt
```

Optional flags: `--write-register` (omit), `--v1-historical` (**do not use** — selects the superseded land-cell data).

> **Limitation.** This produces **overlapping** "at max" counts: for the PRIMARY departure window the archived capture shows `g_r` 18, `g_o` 1,042, `g_t` 3,599 against 4,448 non-SAFE hours — summing to 4,659, i.e. 104.7%. It does **not** produce the exclusive 518 / 13 CAUTION attribution the manuscript reports, and **no script in the repository was found that does.**

### 7.4 Canonical figures

```bash
python3 scripts/canonical_figures.py | tee data/c8/canonical-figures-$(date -u +%Y%m%dT%H%M%SZ).txt
```

> **Caveat.** This script changed at `f8215e4` (2026-09-09), one day after the archived capture. Its output at HEAD may differ from the archived block. Any difference is a script revision difference, not necessarily an error.

### 7.5 Threshold provenance (supporting)

```bash
python3 scripts/threshold_comparison.py
```

Produces no reported figure; documents the sea-state-to-metre conversions behind the wave thresholds.

### 7.6 Data collection — optional, and destructive

```bash
python3 scripts/collect_raw_v2.py --start 2020-01-01 --end 2024-12-31
```

**This overwrites the committed canonical datasets and will not reproduce the original bytes.** Included for completeness only.

---

## 8. Expected outputs and what evidence exists

### 8.1 Backed by archived machine output

`data/c8/canonical-results-post-migration.txt` (commit `babe92f`, 2026-09-08) contains:

| Result | PRIMARY | RESOLUTION |
|---|---|---|
| Hourly records | 43,848 | 28,501 |
| Departure-window hours | 9,135 | 5,935 |
| SAFE / CAUTION / UNSAFE | 4,687 / **531** / 3,917 | 3,231 / **266** / 2,438 |
| C0↔C1 | 42.88% | 41.08% |
| C0↔C2 | 48.69% | 45.56% |
| **Δ_L2** | **5.81%** | **4.48%** |
| C1↔C3 | 0.00% | 0.00% |

Arithmetic check you can do without running anything: 3,917/9,135 = 42.88%; (531+3,917)/9,135 = 48.69%; 531/9,135 = 5.81%; and the three state counts sum to the denominator in both configurations.

### 8.2 No archived machine output

| Result | Value | Only source |
|---|---|---|
| CAUTION attribution | 518 ocean-state / 13 rainfall (97.6% / 2.4%) | `docs/analysis/experiment-report-delta-l2.md:282–283` |
| PRIMARY sourced-threshold envelope | 5.67–9.56% | `docs/analysis/threshold-sensitivity-analysis.md:158, 217` |
| RESOLUTION envelope | 4.26–6.64% | same document, §E |
| Large-vessel Δ_L2 | 1.26% / 0.37% | same, lines 112–115 |
| Daylight-only denominator Δ_L2 | 9.59% / 7.40% | same, line 136 |
| Alternative wave UNSAFE Δ_L2 | 9.22% | same, line 114 |
| Sensitivity combination count | 56 | **no artefact anywhere** |

These figures are **unverified, not shown to be wrong.** The scripts that produce them are present, deterministic and at the correct revision; only the output was never kept. A single `tee`'d run of §7.2 would move six of the seven from prose to machine evidence.

---

## 9. Provenance

### Datasets

Both wave series and the weather series came from **Open-Meteo**, not from the upstream model providers directly:

- PRIMARY waves: `models=era5_ocean` on `marine-api.open-meteo.com/v1/marine`
- RESOLUTION waves: `models=meteofrance_wave` on the same endpoint
- Weather: `archive-api.open-meteo.com/v1/archive`

All three requested 5.98 N, 116.01 E with `cell_selection=sea`; the returned cells differ slightly per model and are recorded in each file header.

> **Do not assume the RESOLUTION series is the Copernicus product cited as [11].** No request, response, manifest or log in the repository names `GLOBAL_ANALYSISFORECAST_WAV_001_027` or DOI `10.48670/moi-00017`. The identification rests on Open-Meteo's documentation. Shared model family is not evidence of identical data.

### Code

The headline chain — `canonical_gt.py`, `condition_comparison.py`, `diagnostic_binding.py`, `threshold_comparison.py` — and all four data files are **byte-identical between commit `babe92f` and HEAD**, and the working-tree copies match their HEAD copies. The code that produced the archived results is the code you have.

---

## 10. Limits of external reproducibility

Stated plainly, because they bear on what this guide can promise.

1. **Repository visibility is unverified.** The remote is `git@github.com:kandaiiskandar/research-plan.git` over SSH. Whether it is publicly readable was not established. **No availability claim should be made on this basis.**
2. **Re-collection will not reproduce the original data.** The provider archive is live and unversioned; no retrieval timestamp or checksum was recorded. Use the committed CSVs.
3. **No dependency specification existed** before this task, and the historical Python minor version, OS and architecture are unknown. Determinism is a property of the algorithm, not a guarantee across arbitrary numpy builds — thresholds are compared against exact values such as 1.0 and 1.25, so a different floating-point build could in principle shift a boundary hour. Not observed; not tested.
4. **Nothing in this guide was executed.** Commands are documented from static inspection.
5. **This guide and its manifest verify no result.** They record provenance.

---

## 11. If you are picking this up to close the gaps

In order of value, and none of them requires a new experiment:

1. Run §7.2 with `tee` into `data/c8/`. Six grade-C results become grade-A.
2. Write a run manifest beside it, on the pattern of `data/c5/c5-run-manifest.json` — UTC timestamp, script SHA-256s, package versions.
3. Change `threshold_sensitivity.py:150` from `/tmp/sens_out.txt` to a path under `data/c8/`.
4. Establish how the exclusive 518 / 13 attribution was produced, or produce it from a script that is kept.
5. Decide, deliberately, whether a trimmed public archive should exist — and only then consider an availability statement.
