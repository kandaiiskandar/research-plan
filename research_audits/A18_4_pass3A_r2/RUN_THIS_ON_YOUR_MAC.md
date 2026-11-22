# Track A — run this in your own macOS Terminal

## Why you, and not me

Both environments I can execute in are blocked from the provider at an egress
proxy. Measured today, 2026-11-22, and logged:

| Environment | `data.marine.copernicus.eu` | `pypi.org` | log |
|---|---|---|---|
| Cloud container (where my shell runs) | **000 / refused** | 200 | `logs/connectivity_probe_container.json` |
| Cowork VM on your Mac (where the folder is mounted) | **000 / refused** | 200 | `logs/connectivity_probe_device.json` |
| **Your own Terminal** | not yet tested | — | — |

Your Copernicus registration removed the *credentials* blocker. It did not and
could not change the *network* blocker, because that sits in front of my
sandboxes, not in front of your account. The one environment with both a valid
account and unrestricted egress is your own Terminal.app, outside the Cowork VM.

**Track A stays HOLD until a real file is hashed and parsed.** Running this is
what ends the HOLD.

## Credential rule — read before you start

Never paste your Copernicus username or password into the Claude conversation,
into any file in this repository, or into any report. `copernicusmarine login`
stores them in your own home directory, where nothing in this package reads
them. The audit gate G-12 fails the package if an assigned credential value
appears anywhere in it.

## Commands

Open **Terminal.app** (not the Cowork session) and run these in order.

```sh
cd ~/Documents/my_stuff/research-test-2/research_audits/A18_4_pass3A_r2

# 1. dependencies (a venv keeps them out of your system python)
python3 -m venv .venv
. .venv/bin/activate
pip install copernicusmarine xarray netCDF4 numpy

# 2. log in once — interactive prompt, credentials stored in your home dir
copernicusmarine login

# 3. status-only reachability check. No payload, nothing written.
#    Expect 200s here where my environments got 000.
python3 reproduce_acquisition.py --probe

# 4. prove the QA actually works before trusting it on real data.
#    8 behavioural tests against synthetic NetCDF fixtures.
python3 test_qa.py

# 5. the actual subset: 1 week, 1 degree square off Sabah, 3 wave variables.
#    ~a few MB. On success it hashes the file, rebuilds the manifest and runs QA.
python3 reproduce_acquisition.py --track-a

# 6. independent re-verification of what step 5 wrote
python3 reproduce_acquisition.py --verify
python3 audit_report_against_artifacts.py
```

### If step 5 complains the dataset id is unknown

You gave me `cmems_mod_glo_wav_my_0.2deg_PT3H-i`. The services page lists it
with a release suffix, `..._202411`, which is the built-in default. The suffix is
provider-controlled and gets bumped. Override it without editing any hashed
file:

```sh
python3 reproduce_acquisition.py --track-a --dataset-id cmems_mod_glo_wav_my_0.2deg_PT3H-i
```

The id you actually used is recorded in the manifest row and in the provenance
note, so the two are never ambiguous afterwards.

### The request, and how to change it

Defaults, deliberately small so the first run is cheap and fast:

| Parameter | Default | Flag |
|---|---|---|
| Longitude | 115.5 – 116.5 °E | `--lon-min` `--lon-max` |
| Latitude | 5.5 – 6.5 °N | `--lat-min` `--lat-max` |
| Period | 2024-01-01 → 2024-01-07 | `--start` `--end` |
| Variables | `VHM0 VTM10 VMDR` | `--variables` |

The three variable short names are **provider-documented, not file-verified**.
If they are wrong the Toolbox will say so, and the QA's expected-variable check
is what verifies them against the real file rather than against documentation.

## Exit codes — what each one means

Nothing here returns success for work it did not do. That was the defect the
r3 review caught, so the codes are now explicit:

| Code | `reproduce_acquisition.py --verify` | `audit_report_against_artifacts.py` |
|---|---|---|
| 0 | manifest non-empty **and** every row matches disk | all 26 gates pass |
| 1 | a hash mismatch | a gate **failed** |
| 3 | manifest empty — consistent, but nothing was acquired | a gate **could not run** |

A `3` from the audit on a machine without `xarray` is expected and correct: the
behavioural tests are reported BLOCKED, not passed. Installing the dependencies
in step 1 turns that into a real PASS or a real FAIL.

## When it finishes

Tell me, and I take it from there through the folder bridge: confirm the hash,
read the NetCDF header, check the bounds and the variable set against what was
requested, and write the first real numbers into
`05_dataset_quality_report.md`. That is also the point where Track A's evidence
tier can move off R0 — and where it still cannot go past R1-SOURCE-ONLY, because
this is a reanalysis hindcast, not information that was available to a fisher at
a historical decision time.
