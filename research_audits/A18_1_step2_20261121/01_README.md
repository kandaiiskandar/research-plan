# A18.1 Step 2 — Dataset Provenance and Integrity Audit

**Date:** 21 November 2026 · **Scope:** Step 2 ONLY · **Mode:** read-only source audit
**Subject:** the accepted, not-yet-published AAI2026 paper *"From Declared Risk Levels to Admissible Recommendations: Measuring How Often an Intermediate Governance Level Binds in Deterministic Historical Replay"*

## Working root

`/Users/iskandar/Documents/my_stuff/research-test-2` — supplied as the project repository root. No traversal outside it. No other plausible repository was found, so no clarification was needed.

## What this audit is NOT

- **Not** A18.1 Step 3 governance-rule reconstruction
- **Not** A18.1 Step 4 numerical reproduction of 5.81% / 4.48% / 42.88% / 41.08% / 48.69% / 45.56%
- **Not** a new safety study, and no claim about correct or safe fishing actions
- No network retrieval, no API calls, no data purchase, no git history alteration
- The original pandas code path was **read, not re-executed**

## Method, and why it is independent

Counts were recomputed by `audit_step2.py` in this directory using the **Python standard library only** — `csv`, `hashlib`, `json`, `statistics`, `datetime`, `zoneinfo`. It deliberately does not use pandas, so the audit shares no dependency with the artefact under audit and every count comes from a reader independent of the original code path. The agreement reported in §Reconciliation is therefore a genuine cross-check, not a re-run.

The Open-Meteo metadata block is 2 lines plus 1 blank; the data header is line 4. This matches the original code's `skiprows=3`, verified by reading `scripts/historical_replay.py:122-132`.

## Commands executed

```
mkdir -p research_audits/A18_1_step2_20261121
python3 -I research_audits/A18_1_step2_20261121/audit_step2.py
sha256sum data/raw_weather_sea.csv data/raw_marine_era5_sea.csv data/raw_marine_mfwam.csv data/prediction-register.csv
grep -n 'wave_period' scripts/*.py
grep -n '^LATITUDE\|^LONGITUDE\|^TIMEZONE' scripts/collect_raw_v2.py scripts/openmeteo_raw_download.py
```

`python3 -I` (isolated mode) was used so neither the current directory nor user site-packages can inject a module — the inputs include downloaded CSV data and the audit directory is not on the import path. No failures occurred. No package was installed.

## Software

| | |
|---|---|
| Python (audit) | 3.10.12 |
| Audit dependencies | standard library only |
| Original pipeline | `pandas==2.3.3`, `numpy==2.2.6` (`requirements-aai-2026.txt`) — both present on this machine at those versions |
| Determinism | no RNG and no seed appears in any of the four canonical scripts; the pipeline is deterministic by construction |

**Caveat carried from the repository's own documentation:** `requirements-aai-2026.txt` states it was created 2026-10-08 as retrospective documentation and **did not exist when the experiments were run in September 2026**. The pinned versions are therefore a later reconstruction, not a captured environment.

## Files in this directory

| File | Contents |
|---|---|
| `01_README.md` | this file |
| `02_source_data_inventory.csv` | 7 artefacts: lineage, SHA-256, size, rows, columns, coverage, coordinates |
| `03_schema_units_quality.csv` | 33 fields: dtype, declared unit, nulls, min/median/max |
| `04_temporal_integrity.csv` | timezone assumptions, bounds, cadence, duplicates, gaps, window counts |
| `05_spatial_integrity.csv` | requested vs returned cell, displacement, selection method |
| `06_missingness_join_reconciliation.csv` | join cardinality, the 11-record wave gap, marine-warning scan |
| `07_transformation_lineage.csv` | 10 scripts/artefacts in the chain, hashed |
| `08_manifest_sha256.txt` | hashes of every input read and every output written |
| `09_discrepancy_and_blocker_register.csv` | 12 findings D-01…D-12 with severity and required action |
| `10_A18_1_STEP2_AUDIT_REPORT.md` | the report, with the seven mandatory tables |
| `11_A18_1_STEP3_HANDOFF.md` | confirmed fields and assumptions for Step 3 |
| `audit_status.json` | machine-readable summary and Step 3 readiness |
| `audit_step2.py` | the read-only audit script |

No synthesized dataset was produced. No input file was written to, renamed, resampled or interpolated.
