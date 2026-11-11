# AAI 2026 — Sensitivity Verification Report

**Task:** M-6 controlled sensitivity reproduction and evidence preservation
**Verification run:** 8 October 2026, 14:54:41–14:54:44 UTC
**Script executed:** `scripts/sensitivity/threshold_sensitivity.py`, unchanged, once
**Scientific configuration changed:** none. **Script source changed:** none. **Datasets changed:** none. **Manuscript changed:** none.
**Manuscript baseline used:** `publications/active/aai-2026/drafts/aai-2026-manuscript-v7-rewrite-v2.docx` — see the note in section J on the baseline named in the brief.

---

## A. Executive Summary

**The canonical sensitivity analysis reproduced.** The unchanged script ran to completion in 3.082 s with exit code 0 and an empty stderr, and its complete output is now preserved in the repository under `data/c8/reproducibility-verification/`. The ephemeral-output defect that caused this evidence gap is closed for this run: the output exists as a versionable file instead of in `/tmp`.

**Seven of the eight reported sensitivity results matched exactly**, at the full precision at which the manuscript reports them. Not one differed by even 0.01 percentage point. The eighth — the 56-combination count — is not printed by the script, and is addressed separately below.

**Four of the six grade-C results identified in the preceding manifest audit now carry archived machine output**, including the one the audit singled out as the paper's weakest-supported number: the alternative wave UNSAFE threshold value of **9.22%**. That figure is now machine-evidenced.

Three findings beyond the brief's checklist are worth stating.

1. **The daylight-only denominator is exactly derivable, and the implementation reading is confirmed arithmetically.** The CAUTION numerator is unchanged by the daylight restriction — 531 hours in PRIMARY, 266 in RESOLUTION — because a CAUTION classification requires `g_t ≠ UNSAFE`, which under the canonical solar-event classifier *means* daylight. So every CAUTION hour already lies inside the daylight subset, and the restriction removes only non-CAUTION hours from the denominator: 531 / 5,536 = 9.5918% → **9.59%**, and 266 / 3,594 = 7.4012% → **7.40%**. This is not a rounding coincidence; the reported figures are the exact quotients. It also settles the question the brief asks: the variant changes the denominator and does not remove the night→UNSAFE policy.

2. **The envelope endpoints are internally corroborated by the component counts.** The PRIMARY minimum 5.67% is exactly 518 / 9,135 — the ocean-state-only CAUTION count, which is what remains when `R_C` is raised to 19.9 and the 13 rainfall-attributed hours drop out. The RESOLUTION minimum 4.26% is exactly 253 / 5,935, the corresponding RESOLUTION ocean-state count. The two envelope floors and the component attribution printed in the same run agree to the hour.

3. **One claim in the preceding M-6 audit was wrong, and this run disproves it.** That audit stated that no script in the repository produces the exclusive 518 / 13 attribution. It does: `threshold_sensitivity.py` lines 93–99 print it, and this run's output carries it, with `ties = 0` establishing that the attribution is exclusive rather than overlapping. I wrote that claim and it was incorrect. Verifying the attribution is outside this task's scope and stays open as its own item, but the machine evidence for it now exists.

**Nothing canonical was disturbed.** All five canonical script hashes, all four input dataset hashes, the frozen solar artefact and both archived result files are byte-identical before and after the run, and `git` reports 0 modified tracked files throughout.

---

## B. Pre-Execution Integrity

| | |
|---|---|
| Branch | `AMIT-v5` |
| HEAD | `a7f77d8351ec94c586309d796aabd1230f4886dd` (2026-10-07 16:05:14 +0800) |
| Match with the previous manifest snapshot | **Identical** — same branch, same HEAD |
| Working tree before the run | **Already dirty**: 44 `git status` entries, **0 modified tracked files**, 0 deleted or renamed |
| Git operations | read-only only (`branch --show-current`, `rev-parse`, `log -1`, `status --short`) |

The 44 pre-existing entries were 41 untracked draft files plus the three entries created by the preceding manifest documentation task. No tracked file was modified before the run.

### Hashes, compared against `data/c8/aai-2026-reproducibility-manifest.json`

| Path | SHA-256 (first 16) | Manifest |
|---|---|---|
| `scripts/sensitivity/threshold_sensitivity.py` | `6ddaea583941134b` | **MATCH** |
| `scripts/canonical_gt.py` | `b330bf9f94e848aa` | **MATCH** |
| `scripts/sensitivity/solar.py` | `3b7dc371ebe5931b` | **MATCH** |
| `scripts/condition_comparison.py` | `3c32913a2a9cc85f` | **MATCH** |
| `scripts/sensitivity/gt_counterfactual.py` | `eb58508e9159722d` | **MATCH** |
| `data/raw_weather_sea.csv` | `96850d7547189ffa` | **MATCH** |
| `data/raw_marine_era5_sea.csv` | `6754e2c2ee5586ee` | **MATCH** |
| `data/raw_marine_mfwam.csv` | `e9f323e086a3e9dd` | **MATCH** |
| `data/solar/solar-events-daily.csv` | `057c46a19d0e8ea7` | **MATCH** |
| `data/c8/canonical-results-post-migration.txt` | `0bca160f69f68663` | **MATCH** |
| `data/c5/c5-run-manifest.json` | `1f04720cb373e688` | **MATCH** |

**Every required canonical script and dataset hash matched the manifest.** No discrepancy, so execution proceeded.

### Script inspection, before execution

Read in full (150 lines). Confirmed from source:

- **Canonical status.** Its docstring names it the threshold sensitivity analysis for the headline Δ<sub>L2</sub> result, and the manifest classifies it canonical.
- **Thresholds.** Line 19, `CANON = dict(W_C=21.6, W_U=27.0, R_C=10.0, R_U=20.0, O_C=1.0, O_U=1.25)` — identical to the recorded canonical configuration.
- **Governance mappings not varied.** Lines 61–63 freeze `FULL`/`REST`/`EMPTY` and the C1 and C2 admissible-set tables. The docstring states it: *"Governance mappings are NOT varied. A_AI(CAUTION) = {Go, Delay} is frozen. Only environmental classification thresholds vary."*
- **Shared classifier used.** Line 13 imports `g_t` and `is_daylight` from `scripts/canonical_gt.py`. No solar astronomy is embedded.
- **Departure window.** Line 47, `(hour >= 5) & (hour <= 9)`.
- **Declared exclusion.** Line 39 holds `g_m` at SAFE for every row.
- **Dependencies.** `pandas`, `numpy`, and the local `canonical_gt` — all available.
- **Output format.** Every reported line passes through the `P()` helper at line 70, which both appends to an in-memory list and prints. Percentages are formatted `.2f`.
- **Data paths are `__file__`-derived** (lines 11–16), so behaviour does not depend on the working directory.
- **Side effects.** Reads four CSVs; writes exactly one file. No canonical artefact is written.

### The `/tmp/sens_out.txt` question

The brief asks whether this is an output file, a shell redirection target, or a script-controlled write. **It is a script-controlled write.** Line 150:

```python
Path("/tmp/sens_out.txt").write_text("\n".join(out))
```

So `tee` alone would not have been the right instrument — it would capture stdout while the script independently wrote its own copy to an ephemeral path. The capture used instead was non-invasive and covered both channels: stdout and stderr redirected to separate files in the verification directory, and the script-written file copied out of `/tmp` verbatim after the run. `/tmp/sens_out.txt` was verified **absent** before the run, so no pre-existing file was overwritten.

---

## C. Execution Environment

| | Verification run (2026-10-08) | Historically documented (Sept 2026) | Comparable? |
|---|---|---|---|
| Python | **3.10.12** (main, Aug 31 2026, GCC 11.4.0) | "Python 3" — minor version **UNKNOWN** | **No** |
| pandas | **2.3.3** | **2.3.3** | **MATCH** |
| numpy | **2.2.6** | **2.2.6** | **MATCH** |
| OS | Linux-6.8.0-138-generic-aarch64-with-glibc2.35 | UNKNOWN | No |
| Architecture | aarch64 | UNKNOWN | No |
| Executable | `/usr/bin/python3` | — | — |

> **This is not the author's machine.** The run executed in the isolated Linux VM through which this audit session reaches the repository. The matching pandas and numpy versions are meaningful; the rest of the environment is not known to correspond to September 2026.

No package was installed, upgraded or downgraded. The script's only third-party imports are pandas and numpy, both present at the historically documented versions. **This run does not recreate the historical execution environment**, and no such claim is made.

---

## D. Execution Record

| | |
|---|---|
| Command | `python3 scripts/sensitivity/threshold_sensitivity.py` |
| Argument handling | The script contains no `argparse` and accepts no arguments; this is its documented canonical invocation |
| Working directory | repository root |
| Invocations | **1** |
| Exit code | **0** |
| Start / end (UTC) | 2026-10-08T14:54:41Z / 2026-10-08T14:54:44Z |
| Duration | **3.082 s** |
| stderr | **empty (0 bytes)** — no warnings, no errors |

### Preserved outputs

| Path | Bytes | SHA-256 (first 16) |
|---|---|---|
| `data/c8/reproducibility-verification/threshold-sensitivity-20261008-stdout.txt` | 6,924 | `9323489a990399d0` |
| `data/c8/reproducibility-verification/threshold-sensitivity-20261008-stderr.txt` | 0 | `e3b0c44298fc1c14` |
| `data/c8/reproducibility-verification/threshold-sensitivity-20261008-sens_out.txt` | 6,923 | `db246059ffbf1ea5` |
| `data/c8/reproducibility-verification/threshold-sensitivity-run-manifest.json` | — | machine-readable run record |

The raw output was preserved before any interpretation. The stdout capture and the script-written file are identical except that the latter has no trailing newline (`diff` reports exactly one difference, `\ No newline at end of file`), so either is a complete record.

---

## E. Numerical Verification Matrix

| Result | Manuscript | Generated | Status | Evidence |
|---|---|---|---|---|
| PRIMARY envelope | 5.67–9.56% | **5.67% – 9.56%** | **EXACT MATCH** | stdout:30 (`R_C=19.9 → 5.67%`), :50 (`R_C=5.0, wave=(1.0,1.9) → 9.56%`), :54, :56 (`grid max 9.56%`) |
| RESOLUTION envelope | 4.26–6.64% | **4.26% – 6.64%** | **EXACT MATCH** | stdout:86 (`R_C=19.9 → 4.26%`), :106, :110, :112 (`grid max 6.64%`) |
| Large vessel PRIMARY | 1.26% | **1.26%** | **EXACT MATCH** | stdout:43 `(1.5, 3.5) → 1.26%  [Yaakob big vessel / MET Cat1 ceiling]`; also stdout:52 |
| Large vessel RESOLUTION | 0.37% | **0.37%** | **EXACT MATCH** | stdout:99, also :108 |
| Daylight-only PRIMARY | 9.59% | **9.59%, n = 5,536** | **EXACT MATCH** | stdout:46. Exact quotient 531 / 5,536 = 9.5918% |
| Daylight-only RESOLUTION | 7.40% | **7.40%, n = 3,594** | **EXACT MATCH** | stdout:102. Exact quotient 266 / 3,594 = 7.4012% |
| Alternative wave PRIMARY | 9.22% | **9.22%** | **EXACT MATCH** | stdout:41 `(1.0, 1.9) → 9.22%  [Yaakob failure point as O_U]`; also stdout:52 |
| Unique combinations | 56 | **not printed; 56 by static enumeration** | **EXACT MATCH (derived, not printed)** | Script literals, lines 104/108/112/128/131. One interpretive step — see below |

Baseline figures in the same output, for context: PRIMARY Δ<sub>L2</sub> **5.81%** with the `Δ_L2 ≡ P(CAUTION)` identity printed as **HOLDS**, RESOLUTION **4.48%**, identity **HOLDS** (stdout:5, :61).

### Precision

The script formats every percentage with `.2f`, and the manuscript reports to 2 decimal places. The generated and reported digits are identical at that precision, so each match above is a match at the full reported precision. The underlying floats are not recoverable from the preserved output, and the September output no longer exists for byte comparison, so agreement below 0.01 percentage point is unobservable in principle here — not a shortfall of this run.

Where the printed output supplies integer counts, the quotient is exact and independently confirms the percentage:

| Quantity | Exact quotient | Rounds to | Reported |
|---|---|---|---|
| PRIMARY baseline | 531 / 9,135 = 5.81281% | 5.81% | 5.81% |
| RESOLUTION baseline | 266 / 5,935 = 4.48188% | 4.48% | 4.48% |
| PRIMARY daylight-only | 531 / 5,536 = 9.59176% | 9.59% | 9.59% |
| RESOLUTION daylight-only | 266 / 3,594 = 7.40122% | 7.40% | 7.40% |
| PRIMARY envelope floor | 518 / 9,135 = 5.67049% | 5.67% | 5.67% |
| RESOLUTION envelope floor | 253 / 5,935 = 4.26285% | 4.26% | 4.26% |

The last two deserve a note: 518 and 253 are precisely the ocean-state binding counts printed in the component-attribution block of the same run. The envelope floor is what remains once the rainfall boundary is raised past every rainfall-attributed CAUTION hour. The sensitivity sweep and the attribution block agree to the hour, which is a non-trivial internal consistency check that neither was designed to provide.

### The 56-combination count

The manuscript's wording is specific: *"the canonical sensitivity script evaluates 56 distinct combinations of environmental-data configuration, threshold setting and denominator policy, of which this paper reports a subset."* So the convention is stated — a triple — and the count can be checked against the script's configuration enumeration. The script itself prints no such number.

Counting `run()` invocations from the source literals, per data configuration: 1 baseline + 5 rainfall + 5 wind + 6 wave + 1 daylight-only + 20 grid = **38**. Two configurations give 76, plus 2 common-period runs = **78 gross invocations**.

Deduplicating on the threshold parameter tuple `(W_C, W_U, R_C, R_U, O_C, O_U)`:

| Block | Invocations | Duplicates of an earlier tuple | New |
|---|---|---|---|
| Baseline `CANON` | 1 | 0 | 1 |
| Rainfall `R_C` sweep | 5 | 1 (`R_C = 10.0` is canonical) | 4 |
| Wind `W_C` sweep | 5 | 1 (`W_C = 21.6` is canonical) | 4 |
| Wave `(O_C, O_U)` sweep | 6 | 1 (`(1.0, 1.25)` is canonical) | 5 |
| Combined grid, 5 × 4 | 20 | 8 | 12 |
| **Unique threshold settings** | | | **26** |
| Daylight-only denominator, canonical thresholds | 1 | — | 1 distinct case |
| **Distinct cases per data configuration** | **38** | **11** | **27** |

Two data configurations give 54. Adding the two common-period runs gives **56**.

The arithmetic lands exactly on the manuscript's figure, and the convention it uses is the one the manuscript names. **One interpretive step is required**, and it should be visible: the common-period comparison is counted as a denominator policy. That reading is defensible — the restriction changes the evaluated record, and both configurations are evaluated over the same 5,935 departure hours — but the script labels that block *"COMMON-PERIOD COMPARISON (de-confounds wave model from record length)"* rather than calling it a denominator policy. Without that step the count is 54, not 56.

So the figure is **correct and traceable**, but it is derived from a static read of the source rather than emitted by the script, and it depends on one classification choice the manuscript does not spell out. It is marked EXACT MATCH on that basis, with the derivation above as its evidence, rather than on the authority of an earlier Markdown report.

**A read-only enumeration diagnostic is proposed but was not executed.** A short script that imports the sweep literals and prints the deduplicated case count, under each candidate convention, would turn this from a derivation into machine output. It would be a new diagnostic, not the canonical experiment, and it awaits explicit approval.

---

## F. Endpoint Configuration Verification

The envelope is defined in `docs/analysis/threshold-sensitivity-analysis.md:217` as *"Externally sourced thresholds, small vessel only (canonical; Yaakob failure-point variant; sourced `R_C` values)"*. That selects the two small-vessel wave columns of the combined grid — `(1.0, 1.25)` and `(1.0, 1.9)` — across the five `R_C` values. The generated grid gives:

**PRIMARY** (stdout:49–56)

| `R_C` | `(1.0, 1.25)` | `(1.0, 1.9)` |
|---|---|---|
| 5.0 | 6.15% | **9.56% ← maximum** |
| 7.5 | 5.93% | 9.34% |
| 10.0 | 5.81% *(canonical)* | 9.22% |
| 15.0 | 5.70% | 9.11% |
| 19.9 | **5.67% ← minimum** | 9.07% |

**RESOLUTION** (stdout:105–112)

| `R_C` | `(1.0, 1.25)` | `(1.0, 1.9)` |
|---|---|---|
| 5.0 | 5.04% | **6.64% ← maximum** |
| 7.5 | 4.65% | 6.25% |
| 10.0 | 4.48% *(canonical)* | 6.08% |
| 15.0 | 4.31% | 5.91% |
| 19.9 | **4.26% ← minimum** | 5.86% |

| Endpoint | Configuration | Generated | Evidence |
|---|---|---|---|
| PRIMARY minimum 5.67% | `R_C = 19.9`, `O_C = 1.0`, `O_U = 1.25`, all else canonical | 5.67% | stdout:30, :54 |
| PRIMARY maximum 9.56% | `R_C = 5.0`, `O_C = 1.0`, `O_U = 1.9` | 9.56% | stdout:50, :56 |
| RESOLUTION minimum 4.26% | `R_C = 19.9`, `O_C = 1.0`, `O_U = 1.25` | 4.26% | stdout:86, :110 |
| RESOLUTION maximum 6.64% | `R_C = 5.0`, `O_C = 1.0`, `O_U = 1.9` | 6.64% | stdout:106, :112 |

Both endpoints of both envelopes are traceable to a named parameter configuration in the preserved output.

One point the manuscript handles correctly and which the output makes concrete: the script's **full** grid range is wider — PRIMARY grid min **1.11%** and RESOLUTION grid min **0.15%** (stdout:55, :111) — because the grid also spans the medium and large vessel wave pairs. The manuscript does not present those as the envelope; it reports them separately as vessel-class sensitivity. The narrower 5.67–9.56% envelope is therefore the *small-vessel sourced* range, exactly as the manuscript and the dated report both state.

### Other manuscript sensitivity claims, checked against the same output

| Claim (manuscript v7) | Generated | Status |
|---|---|---|
| "Varying the rainfall CAUTION boundary moves Δ<sub>L2</sub> by 0.48 percentage points in PRIMARY and 0.78 in RESOLUTION" | 6.15 − 5.67 = **0.48**; 5.04 − 4.26 = **0.78** | **EXACT MATCH** |
| "The wind boundary is a structural zero across the evaluated range W_C = 18–25 kn: no setting within that range altered the classification of any evaluated hour" | Δ<sub>L2</sub> and UNSAFE identical at all five `W_C` values, both configurations (stdout:32–36, :88–92) | **Supported.** One hour changing state would move Δ<sub>L2</sub> by 0.011 points and be visible at 2 dp, so the CAUTION count is unchanged. The claim is marginally stronger than the printed evidence, which shows no *net* change rather than no change in any individual hour |
| "±0.25 m perturbation of `O_C`" range | PRIMARY 2.54%–14.75% (stdout:38, :40); RESOLUTION 1.67%–14.19% (stdout:94, :96) | **EXACT MATCH** with the dated report |

---

## G. Denominator and Configuration Consistency

**Evaluated hours.** The departure-window denominators in this run are PRIMARY **9,135** and RESOLUTION **5,935** (stdout:3, :59), matching the archived canonical capture exactly. Record counts 43,848 and 28,501 likewise match.

**Alternative wave UNSAFE threshold — same denominator, one parameter changed.** The brief asks specifically. Confirmed from both source and output:

- `O_U` moves from **1.25** to **1.90**. `O_C` stays at 1.0; `W_C`, `W_U`, `R_C`, `R_U` stay canonical (line 115, `dict(CANON, O_C=oc, O_U=ou)`).
- The call uses `mask=None` (line 115 → `run(d, p)`), so `dep_mask` applies and the denominator is the same 9,135 hours.
- **1.90 was not silently changed to 1.875.** The script's literal is `1.9` (line 113), labelled *"Yaakob failure point as O_U"*, and the manuscript says *"1.875 m, implemented as 1.90 m"*. The implementation and the manuscript agree, and the 0.025 m gap between the source's tested value and the implemented boundary is disclosed rather than hidden.
- UNSAFE falls from 42.88% to 39.47% as expected when the UNSAFE boundary rises — hours formerly UNSAFE become CAUTION, which is why Δ<sub>L2</sub> rises to 9.22%.

**Daylight-only denominator — restriction, not policy removal.** Confirmed three ways:

1. *Source.* Lines 119–121: `dl_mask = is_daylight(...)`, `m2 = m.values & dl_mask`, then `run(d, CANON, mask=m2)`. Only the mask changes. `classify()` still calls the canonical `g_t`, so the night→UNSAFE rule remains in force.
2. *Output.* The T1 line still reports a non-zero UNSAFE share — 5.74% PRIMARY, 2.70% RESOLUTION (stdout:46, :102) — which comes from wind, rainfall and ocean state inside daylight hours. Had the time rule been removed, this would be the whole-record UNSAFE figure, not a residual.
3. *Arithmetic.* The CAUTION numerator is unchanged at 531 / 266. That follows necessarily: max-severity aggregation means a CAUTION classification requires `g_t ≠ UNSAFE`, and under the solar-event classifier that is exactly daylight. Every CAUTION hour was already inside the daylight subset, so the restriction can only shrink the denominator — 9,135 → 5,536 and 5,935 → 3,594.

Worth stating precisely, because it bears on how the variant should be described: the night→UNSAFE rule is *retained in the classifier* but is *vacuous on the retained subset*, since no included hour is night. The manuscript's framing — "replacing the departure-window denominator with a daylight-only denominator" — is accurate. A reader should not take the 9.59% figure as showing what happens if the night rule is dropped; it shows the binding rate among hours the rule already permits.

**Vessel-class configurations.** The manuscript's "large-vessel threshold configuration" corresponds to the script's `(1.5, 3.5)` pair, labelled *"Yaakob big vessel / MET Cat1 ceiling"*. The run also evaluates a medium class at `(1.4, 2.8)`, giving 1.96% PRIMARY and 0.66% RESOLUTION, which the manuscript does not report. Vessel class varies `O_C` and `O_U` only; everything else stays canonical.

**Governance mappings held fixed.** The C1 and C2 admissible-set tables (lines 62–63) are untouched across all 78 invocations, so every figure above varies environmental classification alone. The `Δ_L2 ≡ P(CAUTION)` identity is printed as HOLDS for both baselines, which is the script's own internal check that the set-divergence count and the CAUTION probability coincide.

---

## H. Discrepancies

**No numerical mismatch was found.** Every one of the seven directly reported values reproduced to the digit. There is nothing to attribute to inputs, environment or invocation.

Two items are not mismatches but should be recorded:

1. **The 56-combination count is derived, not printed.** Section E gives the full arithmetic and names the one interpretive step it rests on. If the common-period block is not counted as a denominator policy, the figure is 54. This is a documentation gap in the manuscript's wording, not a numerical error.

2. **The wind "structural zero" claim is slightly stronger than the printed evidence.** The output shows the CAUTION count unchanged across `W_C = 18–25`; the manuscript says no setting "altered the classification of any evaluated hour". Offsetting changes that leave the count identical are implausible but not excluded by a 2-dp figure. Section F records it as supported with that qualification.

**Unresolved: none from this run.**

---

## I. Remaining Provenance Gaps

### Now supported by machine-generated evidence (this run)

| Result | Previous grade | Now |
|---|---|---|
| PRIMARY sourced-threshold envelope 5.67–9.56% | C | **A** — stdout:30, :50, :54, :56 |
| RESOLUTION sourced-threshold envelope 4.26–6.64% | C | **A** — stdout:86, :106, :110, :112 |
| Large-vessel Δ<sub>L2</sub> 1.26% / 0.37% | C | **A** — stdout:43, :99 |
| Daylight-only denominator Δ<sub>L2</sub> 9.59% / 7.40% | C | **A** — stdout:46, :102, with denominators 5,536 / 3,594 newly evidenced |
| Alternative wave UNSAFE Δ<sub>L2</sub> 9.22% | C — *flagged as the weakest-supported figure* | **A** — stdout:41 |

That is **five of the six** grade-C sensitivity results from the preceding manifest audit. The sixth — the exclusive 518 / 13 attribution — is outside this task's scope.

### Still open

1. **The exclusive 518 / 13 attribution remains open**, as the brief requires. It is recorded here only as a factual correction: this run's output contains it (stdout:18–22, with `ties = 0`), and the preceding M-6 audit's statement that no script produces it was wrong. Verifying it needs its own task, including whether `threshold_sensitivity.py`'s "binding component" definition is the one the manuscript means.
2. **The 56-combination count** is derived rather than emitted. A read-only enumeration diagnostic is proposed and awaits approval.
3. **The historical September run cannot be byte-compared.** Its output was written to `/tmp` and is gone. This run reproduces the *values*; it does not recover the original artefact. Agreement is therefore established at the 2-dp printed precision, not bitwise.
4. **The historical execution environment is still partly unknown** — Python minor version, OS and architecture. pandas and numpy match.
5. **The ephemeral-output defect is not fixed in the script.** Line 150 still writes to `/tmp/sens_out.txt`. This run worked around it without editing the script; the next run will need the same workaround, or a one-line change to the output path.
6. **Outside this task and unchanged:** the Copernicus product lineage for the RESOLUTION data, repository public accessibility, and data retrieval timestamps all remain NOT VERIFIED.

---

## J. Manuscript Implications

**The manuscript was not edited.** Nothing in this run requires a change to any reported number — all seven checked values are correct as printed.

Three items for the author's judgement:

1. **State the counting convention for the 56 combinations, or have the script print it.** The sentence in §IV already names the triple, which is why the count is checkable at all; what it omits is that the common-period comparison is being counted as a denominator policy. A clause such as "including the common-period restriction as a denominator policy" would make the figure fully self-verifying. Alternatively, having the script emit the count would move it from derived to machine-generated.

2. **Consider softening the wind "structural zero" wording** from "altered the classification of any evaluated hour" to something the printed output establishes directly, such as "altered the CAUTION count". The stronger claim is almost certainly true and the weaker one is fully evidenced.

3. **The citation for the preserved evidence can now be specific.** Where the manuscript or thesis refers to the sensitivity analysis, it can now point at `data/c8/reproducibility-verification/threshold-sensitivity-20261008-stdout.txt` and its run manifest rather than at a Markdown report. If a data-availability statement is added, note that this is a 2026-10-08 verification run of the unchanged script, not the September execution.

**A note on the baseline named in the brief.** The brief names `[Rewrite V2] conference-template-letter(20261008-111217).docx` as the latest baseline. No file of that name exists in the repository, and none was attached to this task. The checks above were therefore run against `publications/active/aai-2026/drafts/aai-2026-manuscript-v7-rewrite-v2.docx` (419,027 bytes, SHA-256 `f8769389a5e5c681…`, mtime 2026-10-08 11:18), which the preceding manifest task recorded as byte-identical to the baseline supplied then, and whose timestamp matches the name's `20261008-111217`. If the named file differs from v7, the quotations in sections E–G need re-checking against it; every figure verified here came from the script's output rather than from the manuscript, so the verification itself is unaffected.

---

## K. Final Verdict

> ## SENSITIVITY RESULTS PARTIALLY VERIFIED

Not because anything failed. **Seven of the eight reported results are now verified against preserved machine output, with no mismatch of any size**, both envelope endpoint configurations are traceable to named parameter settings, two of the figures are confirmed as exact quotients of printed integer counts, and every canonical artefact is byte-identical before and after the run. Five of the six grade-C sensitivity results from the preceding audit are now grade A, including the 9.22% figure that audit identified as the paper's weakest-supported number.

The verdict is not **ALL SENSITIVITY RESULTS VERIFIED** for one reason: the eighth result, the 56-combination count, is **not produced by the canonical script**. It is arithmetically correct and traceable to the script's own configuration literals, but establishing it required a static enumeration of the source and one classification choice the manuscript does not state. Calling that "verified" on the same footing as a figure the script printed would blur exactly the distinction this audit exists to maintain.

It is not **SENSITIVITY VERIFICATION FAILED** — nothing diverged — and not **EXECUTION BLOCKED** — every pre-execution check passed and the script ran cleanly in 3.082 s.

**Two steps would upgrade the verdict to ALL SENSITIVITY RESULTS VERIFIED**, neither requiring a new experiment: approve a short read-only enumeration diagnostic that prints the deduplicated combination count under each candidate convention, and add the counting convention to the manuscript sentence that reports it.

---

### Files created by this task

```
data/c8/reproducibility-verification/threshold-sensitivity-20261008-stdout.txt
data/c8/reproducibility-verification/threshold-sensitivity-20261008-stderr.txt
data/c8/reproducibility-verification/threshold-sensitivity-20261008-sens_out.txt
data/c8/reproducibility-verification/threshold-sensitivity-run-manifest.json
docs/reproducibility/aai-2026-sensitivity-verification-report.md
```

No existing file was modified. `git` reports 0 modified tracked files before and after the run.
