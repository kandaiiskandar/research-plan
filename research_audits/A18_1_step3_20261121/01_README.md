# A18.1 Step 3 — Deterministic Governance Contract Reconstruction

**21 November 2026 · read-only · Step 3 only**
Subject: accepted AAI2026 paper, presentation 23 December 2026. **No original file was modified.**

## Directory boundaries and no-write statement

Working root `/Users/iskandar/Documents/my_stuff/research-test-2`. Everything this task created lives in `research_audits/A18_1_step3_20261121/`. **No original dataset, script, manuscript, configuration or Git object was written, renamed or re-run in place.** `git diff HEAD --diff-filter=MD` is empty.

Five original artefacts were SHA-256 hashed before and after the parity run and confirmed byte-identical: the three canonical raw inputs, `data/solar/solar-events-daily.csv` and `data/prediction-register.csv`. The register matters because Step 2 flagged that `condition_comparison.py` can write it; see A-13 — the write sits behind an explicit `--write-register` flag, and the hash confirms it did not fire.

## Method

The contract was **reconstructed, not imported**. `08_reconstruction_reference.py` is pure standard library — no pandas, no numpy, no import of any original module — and every constant and comparison operator in it carries a file-and-line citation to the source it was transcribed from. Reading the solar artefact uses `csv`, not pandas.

`09_test_reconstruction.py` then imports the originals for parity comparison only. That import is safe and was verified so before use: every write in `historical_replay.py`, `condition_comparison.py` and `canonical_gt.py` sits inside `main()`, and the one register write is additionally flag-guarded. Nothing executes at module import beyond constant definition.

Both run under `python3 -I` (isolated mode) so neither the current directory nor user site-packages can inject a module, with `sys.dont_write_bytecode = True` so no `__pycache__` appears beside the originals.

## Command log

```
mkdir -p research_audits/A18_1_step3_20261121
python3 -I research_audits/A18_1_step3_20261121/09_test_reconstruction.py
```

Exit status 0. No failures. No package installed. No network call. Step 4 commands are written in `11_A18_1_STEP4_HANDOFF.md` and were **not run**.

## Tool versions

| | |
|---|---|
| Python | 3.10.12 |
| Reconstruction dependencies | standard library only |
| Parity-test dependencies | `pandas 2.3.3`, `numpy 2.2.6` — matching `requirements-aai-2026.txt` |

Carried from Step 2: that requirements file states it was written 2026-10-08, after the September 2026 runs, so the pins are a retrospective reconstruction rather than a captured environment.

## Source artefacts reviewed

| Path | Lines read | Role |
|---|---|---|
| `scripts/historical_replay.py` | 1–258 (all) | thresholds, component functions, max-severity aggregation, config flag, exclusion subset, departure window |
| `scripts/condition_comparison.py` | 56–200, 305–340 | **authoritative for C0–C3**, small-vessel band, vectorised classifier, divergence counting, register guard |
| `scripts/canonical_gt.py` | 1–147 (all) | canonical `g_t`, half-open solar rule, fail-safe, superseded fixed-clock variant |
| `scripts/diagnostic_binding.py` | 38–101 | threshold cross-check (agrees) |
| `data/solar/solar-events-daily.csv` | header + 1,827 rows | frozen C-3 solar artefact |
| `publications/.../aai-2026-independent-review-v8.md` | 131–188 | manuscript-side statement of the same operators |
| `publications/.../aai-2026-evidence-resolution-and-configuration-register.md` | 18–95 | threshold provenance, configuration register |

## Files produced

| File | Contents |
|---|---|
| `01_README.md` | this file |
| `02_rule_source_traceability.csv` | 30 rules, each with path, function, line, exact text, evidence tier |
| `03_risk_threshold_contract.csv` | 15 rows: variable, unit, vessel applicability, state, operators, precedence, missing behaviour |
| `04_governance_admissible_sets.csv` | 12 rows: 4 configurations × 3 states, with role classification |
| `05_rule_assumptions_and_discrepancies.csv` | 13 findings A-01…A-13 |
| `06_boundary_test_cases.csv` | 62 synthetic fixtures, all labelled synthetic |
| `07_original_vs_reconstruction_parity.csv` | 164 real canonical records, stratified across all three states |
| `08_reconstruction_reference.py` | isolated pure functions |
| `09_test_reconstruction.py` | the deterministic test suite |
| `10_A18_1_STEP3_REPORT.md` | report with the six mandatory tables and the gate |
| `11_A18_1_STEP4_HANDOFF.md` | exact Step 4 commands, not executed |
| `12_SHA256SUMS.txt` | hashes of outputs plus before/after proof for originals |
| `audit_status.json` | machine-readable status |

## What was NOT done

Step 4 percentage reproduction. Expert adjudication. Historical warning reconstruction. Algorithm design. Any real-world safety inference. No manuscript percentage is hard-coded as a computed output anywhere in this folder.
