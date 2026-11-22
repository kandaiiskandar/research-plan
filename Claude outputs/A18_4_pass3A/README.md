# A18.4 Pass 3A — Dataset Retrieval and Provenance Verification

**22 November 2026 · Result: Track A HOLD, Track B HOLD, combined HOLD.**
**`raw/` is empty: 0 files, 0 bytes. No dataset was acquired.**

Start with `09_A18_4_PASS3A_EXECUTION_REPORT.md`.

## Why HOLD

Every data-provider host was refused at this environment's egress proxy with
`HTTP 403 Forbidden (agent proxy: no rule or network setting allows this host)`, in both the cloud
container and on the linked computer, probed independently. Separately, Copernicus Marine requires a
free registered account. No bypass was attempted.

One blocker is **not** environmental and changes the plan: the NWS `/alerts` API **retains seven days
only**, so it cannot supply 2020–2024 issued records from any network. Track B should target the
**NCEI NDFD** archive instead (AWS Open Data mirror, 2020-04-16 to present).

## Contents

| Path | Contents |
|---|---|
| `raw/` | **empty by design** — see `raw/README.md` |
| `processed/` | empty; `netcdf_qa.csv` is written here on a successful Track A run |
| `logs/` | connectivity probe results and the report's computed metrics |
| `01_source_acquisition_register.csv` | 5 providers: product, link, status, access requirement, licence |
| `02_raw_file_manifest.csv` | **header only** — 0 files |
| `03_environmental_metadata.csv` | 18 Copernicus variables, all tiered `DOCUMENTED_ONLY` |
| `04_issued_source_provenance.csv` | **header only** — no eligible issued record |
| `05_dataset_quality_report.md` | what was checked, what could not be, and why page text is not data |
| `06_evidence_eligibility_matrix.csv` | 14 prerequisites across R0 / R1-SOURCE-ONLY / R1-PAIRED / R2 / R3 |
| `07_cross_region_compatibility.md` | domain fit, explicit non-merges, v2.5 scope note |
| `08_discrepancy_and_limitation_register.csv` | 10 entries: blockers, leads, overstatement risks |
| `09_A18_4_PASS3A_EXECUTION_REPORT.md` | the audit report, gate-by-gate |
| `reproduce_acquisition.py` | acquisition + verification; never completed a download |
| `requirements.txt` | pinned, and never exercised against a provider |
| `SHA256SUMS.txt` | checksums of the deliverables |

## Commands

```bash
python3 reproduce_acquisition.py --probe          # status-only, no payload
python3 reproduce_acquisition.py --verify         # re-hash every manifest row
python3 reproduce_acquisition.py --track-b-ndfd   # prints the NDFD route, returns HOLD

export COPERNICUSMARINE_SERVICE_USERNAME=...      # free account; NEVER in a file
export COPERNICUSMARINE_SERVICE_PASSWORD=...
python3 reproduce_acquisition.py --track-a \
  --lon-min 115.5 --lon-max 116.5 --lat-min 5.5 --lat-max 6.5 \
  --start 2024-01-01T00:00:00 --end 2024-01-07T23:59:59
```

The default box is a **proposal, never executed**: 1°×1° off Kota Kinabalu covering the three A18.1 grid
cells, over 7 days — about 6×6 cells × 56 time steps at 0.2° and 3-hourly.

Verify this folder with `sha256sum -c SHA256SUMS.txt` (run from this directory).

## Prerequisites

Python 3.10+. Only the standard library was used to produce these artifacts. Track A additionally needs
`copernicusmarine`, `xarray`, `netCDF4`, `numpy` (pinned in `requirements.txt`) and a Copernicus account.

## Rights

**Copernicus Marine** — "Licence to use the Copernicus Marine Service Products": worldwide,
non-exclusive, royalty-free, perpetual, free of charge; attribution required, *"Generated using E.U.
Copernicus Marine Service Information"* plus the DOI; no warranty as to quality, accuracy or
availability; French law; revisable at any time; users must keep usage records. **No Copernicus bytes are
redistributed here — none were obtained.**

**NOAA / NWS / NCEI** — US Government public domain. The NWS API needs no key but requires a User-Agent
and recommends no more than one request per 30 seconds.

**MET Malaysia** — commercial data shop; fees and licensing apply. Not approached; external requests
require authorisation.

## Scope

Successful R0 acquisition would advance **computational readiness only**. Nothing in this folder
supports a claim about marine safety, harm prevention, vessel-safety thresholds, operator behaviour or
any safe/unsafe label. No fisher decision, operator receipt or expert judgment was created or inferred.
