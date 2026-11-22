# 05 — Dataset Quality Report

**A18.4 Pass 3A · 22 November 2026 · probes executed 03:52–03:5x UTC**

## 1. What was available to inspect

**Nothing.** `raw/` holds 0 files and 0 bytes, so **no QA check on actual data could be executed.**

This section exists to record that fact precisely, not to substitute page text for data. Every quality
gate in the task that requires a parsed file — A3A-01, A3A-02, A3A-03, A3A-04 — therefore **fails**, and
fails for an environmental reason plus, independently, a provider-credential reason.

## 2. Executable checks that WERE run

| Check | Result |
|---|---|
| Connectivity probe, 7 hosts, status-only | **6 of 7 at HTTP 403**; control host `pypi.org` at 200 |
| Same probe from the linked computer | **identical outcome** — 3 provider hosts at 000/403, `pypi.org` at 200 |
| `reproduce_acquisition.py` syntax | parses |
| `reproduce_acquisition.py --verify` on the empty manifest | correctly reports HEADER ONLY and 0 entries, exits clean |
| `reproduce_acquisition.py --track-b-ndfd` | correctly returns HOLD without fetching |
| Manifest/filesystem agreement | 0 manifest rows, 0 files — consistent |

The proxy response text is the literal provider-side refusal, captured verbatim:

```
HTTP/1.1 403 Forbidden (agent proxy: no rule or network setting allows this host)
```

That `pypi.org` returns 200 from both environments establishes the proxy is functioning and selectively
allowlisted to package registries, so the 403s are a policy decision and not a transient network fault.

## 3. QA checks specified but NOT executed

These are the Track A step 5 checks. Each is implemented in `reproduce_acquisition.py :: qa_netcdf()`
and each will run on the first genuine file:

- date and timezone decoding, against the `time` variable's own `units` attribute
- latitude/longitude ordering and monotonicity, with an explicit duplicate count per coordinate
- grid coordinate values versus the provider-stated 0.2° regular grid
- `_FillValue` / `missing_value` attributes, read from the file, never assumed
- NaN counts per variable
- observed min/max per variable, for a physical-range sanity check
- `standard_name`, `long_name` and `units` per variable, read from attributes

**None of these numbers exists yet, and none is reported anywhere in this folder.**

## 4. Provider-stated metadata, and why it is not a substitute

`03_environmental_metadata.csv` carries 18 variables for
`cmems_mod_glo_wav_my_0.2deg_PT3H-i_202411`, every row tiered `DOCUMENTED_ONLY`. It came from the
product description and services pages through a document fetcher that returns **processed page text,
not raw bytes**. That output cannot be byte-hashed and is not a provider file.

Two specific gaps make the page text insufficient even as a stopgap:

**Units and standard names are absent.** The pages list variable names only. So the one thing Track A
step 4 most needs — unit metadata, and a flag on any incompatible definition — cannot be recorded from
them at all. (Register `P3A-05`.)

**The product offers many distinct wave definitions.** Total significant height, primary swell,
secondary swell and wind-wave heights; three different mean periods from spectral moments; period at
spectral density maximum. A18.1 used a single `wave_height (m)` / `wave_period (s)` pair from
Open-Meteo. **Those are not automatically any of these.** Mapping them requires the NetCDF attributes.
(Register `P3A-06`.)

## 5. Missingness versus negative evidence

No observation was recorded, so **nothing here is a safe condition, and nothing is verified negative
evidence.** The distinction the task requires is trivially preserved in this run because the record set
is empty: `02_raw_file_manifest.csv` and `04_issued_source_provenance.csv` are header-only rather than
populated with nulls.

## 6. What a hash would and would not prove

Recorded for the first real acquisition: a SHA-256 confirms **the bytes retained are the bytes
retrieved.** It does not establish provider semantic correctness, that the provider's model is right,
or anything whatever about real-world safety. This holds for every hash in this project, including the
A18.1 input hashes (carried from Step 2, finding D-07).

## 7. Classification

**Track A: R0 ONLY — and not achieved.** Even on success this product is a **reanalysis hindsight model
product**. It is not an issuance-time forecast and not fisher safety information, and it yields **no
independent safe/unsafe vessel label** of any kind.
