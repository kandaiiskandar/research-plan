# AAI 2026 — Reproducibility Manifest Verification Report

**Task:** reproducibility manifest and execution-environment documentation (M-6 follow-up)
**Date:** 8 October 2026, 13:57–14:05 UTC
**Mode:** documentation and provenance only. **No canonical experiment, sensitivity analysis or attribution analysis was executed.** No experimental script, dataset, configuration or archived result was modified. No package was installed. No external dataset was fetched. No Git state-changing operation was performed.

---

## A. Executive Summary

Four documentation files were created from verified repository evidence. Nothing experimental was run or changed.

**What was documented.** The complete canonical artefact chain — nine scripts, four input datasets, one frozen solar artefact, four archived output artefacts — each with an independently computed SHA-256, Git tracking status and last-touching commit. The full environmental, governance and sensitivity configuration, read from source code rather than from research reports. Six reproduction commands with their actual argument handling. A twenty-entry evidence matrix grading every reported numerical result.

**Three findings worth stating up front.**

1. **The headline experiment is traceable to a specific revision, and the code has not moved since.** `canonical_gt.py`, `condition_comparison.py`, `diagnostic_binding.py`, `threshold_comparison.py` and all four input datasets are **byte-identical between commit `babe92f` (2026-09-08, which contains the archived results) and HEAD**, and their working-tree copies match their HEAD copies. The M-6 audit recorded the historical execution revision as potentially unestablishable; it is established, with high confidence, for the headline chain.

2. **The solar artefact self-certifies its generator, and the certificate checks out.** Its `impl_sha256` column records `3b7dc371ebe5931b…c36c`; `scripts/sensitivity/solar.py` hashes to exactly that value. Independently verified during this task.

3. **The evidence gap is confirmed and precisely bounded.** Thirteen reported results carry archived machine output (grade A). Six carry only a dated research report (grade C). One carries nothing at all (grade E — the 56-combination count). The 9.22% provenance weakness **remains unresolved**, and the investigation shows it is not isolated: every sensitivity and attribution figure shares the same cause, namely that `threshold_sensitivity.py:150` writes to `/tmp/sens_out.txt`.

**What remains unverified.** Repository public accessibility; the Copernicus lineage of the RESOLUTION wave data; the historical Python minor version, OS and architecture; data retrieval timestamps; and whether any documented command executes cleanly — nothing was run.

**One correction to the task brief.** The repository is **not** on `main`. It is on branch `AMIT-v5`. Recorded as observed.

---

## B. Files Created

| Path | Purpose | Bytes |
|---|---|---|
| `data/c8/aai-2026-reproducibility-manifest.json` | Machine-readable manifest: repository snapshot, historical execution revisions, environments, scripts, datasets, solar artefact, configuration, commands, archived outputs, evidence matrix, unverified items, limitations | 44,996 |
| `docs/reproducibility/aai-2026-reproduction-guide.md` | Human-readable guide for a researcher new to the project | 17,299 |
| `docs/reproducibility/aai-2026-manifest-verification-report.md` | This report | — |
| `requirements-aai-2026.txt` | Dependency specification, pinned to the historically documented versions, with an explicit statement of what is not established | 2,759 |

All four are **new files**. No existing file was modified.

### On the dependency file

It was created because the evidence supports it, narrowly. The canonical analysis scripts import exactly two third-party packages — pandas and numpy — verified by reading every import statement; everything else is standard library. Both pins come from the one place in the repository that records them: `docs/analysis/experiment-report-delta-l2.md:395`, *"re-run on 2026-09-21 (Python 3, pandas 2.3.3, numpy 2.2.6)"*. The file's header states plainly that these are **historical documented versions, not an observation of the author's current machine**, and that the **Python minor version is unknown and was not invented**. No `python_requires` line was added, because no evidence supports one.

---

## C. Repository Snapshot

| | |
|---|---|
| **Branch** | **`AMIT-v5`** — *not* `main`. The brief stated the repository was on the latest `main`; it is not. |
| **HEAD commit** | `a7f77d8351ec94c586309d796aabd1230f4886dd` |
| **HEAD date** | 2026-10-07 16:05:14 +0800 |
| **HEAD subject** | "Add Phase 8 Reference & Assembly Audit and Phase 9 Layout & Submission Audit documents for AAI 2026" |
| **Remote** | `git@github.com:kandaiiskandar/research-plan.git` (SSH) |
| **Remote visibility** | **NOT VERIFIED** |

### Working tree — before and after

| | Before this task | After this task |
|---|---|---|
| Clean? | **No — already dirty** | No |
| Entries reported by `git status --short` | **41** | **44** |
| Modified **tracked** files | **0** | **0** |
| Deleted or renamed tracked files | 0 | 0 |

**The working tree was already dirty before this task began.** All 41 pre-existing entries were untracked (`??`) files under `publications/active/aai-2026/drafts/`, produced by earlier sessions. This task added **three** `git status` entries covering **four** files — the two files under the new `docs/reproducibility/` directory collapse into a single untracked-directory entry:

```
?? data/c8/aai-2026-reproducibility-manifest.json
?? docs/reproducibility/
?? requirements-aai-2026.txt
```

**Modified tracked files remained at 0 throughout**, which is the direct evidence that no script, dataset or archived result was altered.

### Git operations performed

Read-only only: `branch --show-current`, `rev-parse`, `status --short`, `ls-files`, `log`, `show`. **No** `pull`, `fetch`, `checkout`, branch switch, branch creation, commit, push, history rewrite or visibility change.

---

## D. Canonical Artefact Inventory

### Scripts

| Path | Status | SHA-256 (first 16) | Last commit | Unchanged since `babe92f`? |
|---|---|---|---|---|
| `scripts/condition_comparison.py` | canonical (main entry point) | `3c32913a2a9cc85f` | `babe92f` 2026-09-08 | **Yes** |
| `scripts/canonical_gt.py` | canonical (shared `g_t`) | `b330bf9f94e848aa` | `babe92f` 2026-09-08 | **Yes** |
| `scripts/diagnostic_binding.py` | canonical (attribution) | `113b5b92e81535a9` | `babe92f` 2026-09-08 | **Yes** |
| `scripts/threshold_comparison.py` | supporting | `daed570596df1dbf` | `babe92f` 2026-09-08 | **Yes** |
| `scripts/sensitivity/threshold_sensitivity.py` | canonical (sensitivity) | `6ddaea583941134b` | `3c70a1d` 2026-09-22 | No — but unchanged since `3c70a1d` |
| `scripts/canonical_figures.py` | canonical (figures) | `56c8d4c295b0df7d` | `f8215e4` 2026-09-09 | **No — changed after the capture** |
| `scripts/sensitivity/gt_counterfactual.py` | supporting | `eb58508e9159722d` | `edde171` 2026-09-08 | — |
| `scripts/sensitivity/solar.py` | canonical (solar generator) | `3b7dc371ebe5931b` | `edde171` 2026-09-08 | — |
| `scripts/collect_raw_v2.py` | canonical (collection) | `c646dc9a575f3f15` | `21695e0` 2026-09-06 | — |

`scripts/openmeteo_raw_download.py` is classified **superseded** (v1 collector, land-cell defect F-10) and is recorded in the manifest so it is not mistaken for canonical. **No script was classified canonical on the strength of its filename**; each was read.

### Datasets

| Path | SHA-256 (first 16) | Rows | Usable | Tracked |
|---|---|---|---|---|
| `data/raw_weather_sea.csv` | `96850d7547189ffa` | 43,848 | 43,848 | yes |
| `data/raw_marine_era5_sea.csv` | `6754e2c2ee5586ee` | 43,848 | 43,848 | yes |
| `data/raw_marine_mfwam.csv` | `e9f323e086a3e9dd` | 28,512 | **28,501** (11 leading NaN) | yes |
| `data/solar/solar-events-daily.csv` | `057c46a19d0e8ea7` | 1,827 | — | yes |

### Archived outputs

| Path | SHA-256 (first 16) | Commit |
|---|---|---|
| `data/c8/canonical-results-post-migration.txt` | `0bca160f69f68663` | `babe92f` 2026-09-08 |
| `data/c5/c5-run-manifest.json` | `1f04720cb373e688` | 2026-09-08 |
| `data/c8/pre-migration-scripts/` | (directory) | 2026-09-08 |
| `data/c8/pre-migration-anchors.txt` | — | 2026-09-08 |

### Disagreements with the M-6 audit report, resolved against the repository

| M-6 said | Repository shows |
|---|---|
| Historical execution revision may be unestablishable | **Established.** `babe92f` for the headline chain; `3c70a1d` for the sensitivity analysis. Code stability verified by `git log babe92f..HEAD -- <path>` returning no commits for each canonical file. |
| Scripts depend on pandas and numpy | Confirmed — **and `scripts/sensitivity/solar.py`**, a local module imported by `gt_counterfactual.py`, which M-6 did not list. Now inventoried. |
| No dependency specification exists | Confirmed for the pre-task state. One is added by this task, with its limits stated. |

---

## E. Execution Environment

Three categories, kept strictly apart.

### CURRENT — inspection environment only

> **This is not the project environment.** These values come from the isolated Linux VM through which this session reads the repository, **not** from the author's machine, on which the experiments ran.

| | |
|---|---|
| OS | Linux 6.8.0-138-generic |
| Architecture | aarch64 |
| Python | 3.10.12 (main, Aug 31 2026, GCC 11.4.0) |
| pandas | 2.3.3 |
| numpy | 2.2.6 |

The pandas and numpy versions happen to match the historical record. That is corroborative only, and says nothing about the author's machine.

### HISTORICAL — documented September 2026

| | | Source |
|---|---|---|
| pandas | **2.3.3** | `docs/analysis/experiment-report-delta-l2.md:395` |
| numpy | **2.2.6** | same |
| Python | **"Python 3"** — minor version **UNKNOWN** | same |
| Date of record | 2026-09-21 | same |

### UNKNOWN

Historical Python minor version · historical OS · historical architecture · data retrieval timestamps · whether the author's current environment matches either of the above.

**No version was invented, and no current value was presented as historical.**

---

## F. Manifest Validation

| Check | Result |
|---|---|
| JSON parses | **PASS** — valid JSON, 15 top-level keys, re-parsed after the one post-creation edit |
| Every recorded local file path exists | **PASS** — 16/16 hashed entries present; 0 missing. All non-hashed referenced paths present |
| Every recorded SHA-256 matches its file | **PASS** — **16/16 verified, 0 mismatches**, recomputed on the device against the files as written to the repository |
| Recorded byte sizes match | **PASS** — all entries carrying a `bytes` field matched |
| Git branch correctly recorded | **PASS** — recorded `AMIT-v5`, actual `AMIT-v5` |
| Git commit SHA correctly recorded | **PASS** — recorded and actual both `a7f77d8351ec94c586309d796aabd1230f4886dd` |
| Working-tree status accurately represented | **PASS** — manifest records the tree as *already dirty before* the task with 41 untracked entries and 0 modified tracked files, and as dirty after with 3 additional entries covering 4 files. Both verified. |
| Guide agrees with manifest | **PASS after one correction.** The first check found a transcription error: the guide printed `6ddaea5839411341` for `threshold_sensitivity.py` against the manifest's `6ddaea583941134b`. Corrected in the guide; re-checked, **0 disagreements across 13 cross-referenced paths**. Branch and HEAD SHA also agree, and all twenty manuscript figures appear in both. |
| Historical and current environment clearly distinguished | **PASS** — separate top-level objects, each carrying an explicit warning |
| No archived numerical result modified | **PASS** — `data/c8/canonical-results-post-migration.txt` hash matches its recorded value, and `git status` reports **0 modified tracked files** |

The manifest was edited once after creation, to correct the predicted count of additional untracked entries from 4 to 3 (the `docs/reproducibility/` directory collapses into one `git status` entry). Re-parsed and re-verified afterwards.

---

## G. Reproduction Commands

**None of the following was executed during this task.** Each is labelled **DOCUMENTED — NOT EXECUTED IN THIS TASK** in the manifest. Syntax was derived by reading each script's `argparse` / `sys.argv` handling.

| # | Command | Output destination |
|---|---|---|
| 1 | `python3 scripts/collect_raw_v2.py --start 2020-01-01 --end 2024-12-31` | files — **overwrites the committed datasets; do not run to reproduce results** |
| 2 | `python3 scripts/condition_comparison.py` | **stdout only** |
| 3 | `python3 scripts/sensitivity/threshold_sensitivity.py` | stdout **and `/tmp/sens_out.txt`** (ephemeral — the defect) |
| 4 | `python3 scripts/diagnostic_binding.py` | stdout; CSV only with `--write-register` |
| 5 | `python3 scripts/canonical_figures.py` | stdout only |
| 6 | `python3 scripts/threshold_comparison.py` | stdout only |

### CLI flag verification

Every flag documented was confirmed present in its script, and every script documented as taking no arguments was confirmed to contain no `add_argument` call:

| Script | Flag | Present? |
|---|---|---|
| `collect_raw_v2.py` | `--start`, `--end` | **PRESENT** |
| `condition_comparison.py` | `--write-register` | **PRESENT** |
| `diagnostic_binding.py` | `--write-register`, `--v1-historical` | **PRESENT** |
| `threshold_sensitivity.py`, `canonical_figures.py`, `threshold_comparison.py`, `gt_counterfactual.py` | — | confirmed: no `argparse` |

**No CLI flag was invented.**

### Ephemeral output — recommendation, not applied

`scripts/sensitivity/threshold_sensitivity.py:150` writes the entire run to `/tmp/sens_out.txt`. `/tmp` is ephemeral and the September run's output is gone. **The script was not modified during this task.** The recommended persistent destination for a later controlled verification run is `data/c8/sensitivity-run-<ISO8601>.txt`, reachable either by changing that line or, without touching the script, by:

```bash
python3 scripts/sensitivity/threshold_sensitivity.py | tee data/c8/sensitivity-run-$(date -u +%Y%m%dT%H%M%SZ).txt
```

---

## H. Numerical Evidence Status

Twenty results graded. **A** archived machine output · **B** stored result table · **C** dated research report · **D** manuscript only · **E** nothing.

### Grade A — archived machine output (13)

All in `data/c8/canonical-results-post-migration.txt`: PRIMARY 43,848 records (:198) · RESOLUTION 28,501 usable (:232) · 9,135 evaluated hours (:215) · 5,935 evaluated hours (:249) · 531 CAUTION (:217) · 266 CAUTION (:251) · C0↔C1 42.88% / 41.08% (:223, :257) · C0↔C2 48.69% / 45.56% (:223, :257) · Δ<sub>L2</sub> 5.81% / 4.48% (:226, :260) · C1↔C3 0.00% both (:224–225, :258–259).

### Grade C — dated research report only (6)

| Result | Value | Source |
|---|---|---|
| CAUTION attribution | 518 ocean-state / 13 rainfall (97.6% / 2.4%) | `experiment-report-delta-l2.md:282–283` |
| PRIMARY sourced-threshold envelope | 5.67–9.56% | `threshold-sensitivity-analysis.md:158, 217` |
| RESOLUTION envelope | 4.26–6.64% | same, §E |
| Large-vessel Δ<sub>L2</sub> | 1.26% / 0.37% | same, :112–115 |
| Daylight-only denominator Δ<sub>L2</sub> | 9.59% / 7.40% | same, :136 |
| **Alternative wave UNSAFE Δ<sub>L2</sub>** | **9.22%** | same, :114 |

### Grade E — no artefact (1)

| Result | Value | Note |
|---|---|---|
| Sensitivity combination count | **56** | No artefact in the repository states this. Established by instrumenting the script during an earlier audit; the instrumentation was not retained. |

**No evidence grade was upgraded.** A number repeated across several documents was counted once, at its original source; repetition is not independent verification. The 518/13 attribution deserves particular note: the archived capture contains only **overlapping** "at max" counts (lines 361–374, summing to 104.7% of the departure-window non-SAFE hours), not the exclusive split the manuscript reports, and **no script in the repository was found that produces that exclusive split**.

---

## I. Outstanding Reproducibility Gaps

1. **Missing sensitivity run output.** `threshold_sensitivity.py:150` writes to `/tmp/sens_out.txt`; absent. Cause of five of the six grade-C results. **Closeable by one `tee`'d run — no new experiment.**
2. **Missing exclusive-attribution output for 518 / 13.** Not in any artefact, and no producing script identified. Closing this requires locating or writing the step that emits an exclusive single-component attribution over departure-window CAUTION hours.
3. **No preserved verification for the 56-combination count.** Grade E; the only such result.
4. **The 9.22% provenance weakness remains unresolved**, and is systemic rather than isolated — it shares a single cause with items 1 and 3.
5. **Historical execution revision — largely resolved.** `babe92f` for the headline chain with code stability verified; `3c70a1d` for the sensitivity analysis. Residual: `canonical_figures.py` changed at `f8215e4`, after the archived capture, so its current output may not match the archived block.
6. **Copernicus product lineage — NOT VERIFIED.** No artefact names `GLOBAL_ANALYSISFORECAST_WAV_001_027` or DOI `10.48670/moi-00017`. The identification of Open-Meteo's `meteofrance_wave` with that product is an inference from provider documentation.
7. **Public repository accessibility — NOT VERIFIED.** SSH remote; no GitHub API access from this session; visibility check not completed. **No availability statement may rest on this.**
8. **Execution verification not performed.** No script was run. Command syntax is from static inspection.
9. **Historical Python minor version, OS and architecture — UNKNOWN.**
10. **Data retrieval timestamps — UNKNOWN.** Bounded only by commit `21695e0`, 2026-09-06 12:55:31 +0800.

---

## J. Manuscript Implications

**The manuscript was not edited, and no edit is proposed here.**

One genuine discrepancy surfaced, and it is between the manuscript and the code rather than within either:

- **Metric definition.** The manuscript defines the disagreement count as *"the number of those hours in which one configuration admits a strictly smaller set than another"* — a directional strict-subset rule. `condition_comparison.py:198` computes **set inequality** (`x != y`). The two coincide for all four configurations, because every admissible set is a subset of FULL, so **no reported number is affected**. The definitions are nonetheless not the same, and the manifest records the inconsistency rather than silently resolving it.

Everything else is consistent. In particular, the manuscript's determinism claims are supported by the evidence inventoried here: no randomisation, no estimated parameters, no seeds in the canonical path, and an independent re-execution on 2026-09-21 reproducing the headline figures.

Two matters already raised in the M-6 audit are unchanged by this task and are **not** manuscript implications of it: the absence of a time-zone statement in §IV, and the paper's page size and page count against the venue requirement.

---

## K. Final Verdict

> ## MANIFEST COMPLETE WITH LIMITATIONS

**Complete:** every canonical artefact is inventoried with an independently computed and verified SHA-256 (16/16 matched, 0 mismatches, 0 missing); the repository snapshot is recorded and verified against live `git`; the experimental configuration is traced to source code rather than to reports; six reproduction commands are documented with every CLI flag confirmed present and none invented; current, historical and unknown environment information are kept strictly apart; and all twenty reported results are graded without exaggeration.

**With limitations**, for reasons that are evidential rather than editorial:

- **Seven of twenty reported results have no archived machine output** (six grade C, one grade E). They are unverified, not shown to be wrong.
- **No command was executed**, so the manifest documents a reproduction path that was not walked.
- **Three provenance facts could not be established at all**: repository visibility, Copernicus lineage, and the historical Python minor version, OS and architecture.
- **One canonical script changed after the archived capture** (`canonical_figures.py` at `f8215e4`), so its current output is not guaranteed to match.

The verdict is not **MANIFEST INCOMPLETE** because nothing required for the manifest was unobtainable — the gaps are in the *underlying record*, not in the documentation of it, and each is explicitly recorded as a gap. It is not **MANIFEST COMPLETE** because a manifest documenting a chain in which a third of the reported figures lack machine evidence should say so in its own verdict.

**The single highest-value next step changes nothing in the manuscript and requires no new experiment:** run `scripts/sensitivity/threshold_sensitivity.py` once, with output `tee`'d into `data/c8/`, and write a run manifest beside it on the pattern of `data/c5/c5-run-manifest.json`. That would move five grade-C results to grade A and resolve gaps 1 and 4.
