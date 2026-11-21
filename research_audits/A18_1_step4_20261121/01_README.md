# A18.1 Step 4 — Independent Numerical Reproduction

**21 November 2026 · Step 4 only · originals read-only**
Subject: accepted AAI2026 paper, presentation 23 December 2026.

## Result in one line

**Status: EXACT.** Every reportable manuscript figure reproduced, by two independent paths, at integer-count level — not merely after rounding.

## No-write guarantee

Working root `/Users/iskandar/Documents/my_stuff/research-test-2`, git commit `6c8d783`. Everything created lives in `research_audits/A18_1_step4_20261121/`.

Nine original artefacts were SHA-256 hashed before and after every execution and are **byte-identical**. `git diff HEAD --diff-filter=MD` is empty. `data/prediction-register.csv` is unchanged and the Path A log contains the line `Register NOT written (read-only default; pass --write-register to enable)`.

One side effect, outside the repository: `scripts/sensitivity/threshold_sensitivity.py:150` writes `/tmp/sens_out.txt`. That is system temp, not an original path (register B-03).

## Manuscript edition used

The repository holds eleven manuscript versions. The **configuration register** `aai-2026-evidence-resolution-and-configuration-register.md` is the authoritative numerical source and was used for the targets, cross-read against `aai-2026-independent-review-v8.md:131-188` for the rule statement. `aai-2026-manuscript-v11-renumbered-A4.pdf` is the latest render. **No distinct "Oct 31 revised" edition exists in the repository** — every manuscript file carries an 11 November date.

## Two independent calculation paths

**Path A — original code, read-only.**
```
python3 scripts/condition_comparison.py                    # no --write-register
python3 scripts/sensitivity/threshold_sensitivity.py
```
Logs: `pathA_condition_comparison.log`, `pathA_threshold_sensitivity.log`.

**Path B — independent, standard library only.**
```
python3 -I research_audits/A18_1_step4_20261121/independent_reproduce.py
```
`independent_reproduce.py` imports **no pandas, no numpy and no original module**. It reads the CSVs with `csv`, performs the join and the null-exclusion itself, and classifies through the Step 3 reference implementation — which was transcribed from source with line citations and is not a wrapper around the original. Path B therefore shares no dependency with the artefact under audit; the agreement in `09_original_vs_independent_parity.csv` is a genuine cross-check.

Both ran under `python3 -I` with `sys.dont_write_bytecode = True`.

## Environment

| | |
|---|---|
| Python | 3.10.12 |
| Path A | `pandas 2.3.3`, `numpy 2.2.6` — matching `requirements-aai-2026.txt` |
| Path B | standard library only |
| Determinism | no RNG in any canonical script; no seed needed |

Carried from Step 2: that requirements file was written 2026-10-08, after the September 2026 runs, so the pins are retrospective documentation rather than a captured environment.

## Method

1. **E1** hash all inputs and scripts, record commit and versions.
2. **E2** recompute populations from the raw CSVs with explicit reject reasons.
3. **E3** classify every eligible hour through the Step 3 pure functions, not the original summary; decompose by component with overlap caveats.
4. **E4** derive admissible sets per row for C0/C1/C2/C3 and count all six pairwise divergences, verifying the four claimed identities **at integer-numerator level before comparing any percentage**.
5. **E5** run only the source-specified variants from `threshold_sensitivity.py`.
6. **E6** compare Path A against Path B at count, set and aggregate level.
7. **E7** apply the inference guardrails — exact retrospective frequencies, no IID intervals.

No threshold, filter, unit or rounding was changed at any point to approach a target. The one discrepancy that arose was a defect in **my** Path B implementation; it is documented as B-01 and the original was correct.

## Files

`02_source_and_run_manifest.csv` · `03_population_reconciliation.csv` · `04_state_occupancy.csv` · `05_component_risk_decomposition.csv` · `06_policy_pairwise_divergence.csv` · `07_manuscript_numerical_reconciliation.csv` · `08_sensitivity_and_secondary_results.csv` · `09_original_vs_independent_parity.csv` · `10_discrepancy_blocker_register.csv` · `11_A18_1_STEP4_REPORT.md` · `12_A18_1_STEP5_HANDOFF.md` · `13_SHA256SUMS.txt` · `audit_status.json` · `independent_reproduce.py` · two Path A logs

## What was NOT done

Step 5 case selection. Manuscript revision. Expert labels. Any new model. Any change to risk states. Any real-world safety assertion. No network access, no package installation, no commit, no push.
