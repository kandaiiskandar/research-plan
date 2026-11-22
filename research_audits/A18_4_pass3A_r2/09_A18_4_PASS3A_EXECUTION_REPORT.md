# A18.4 Pass 3A — Execution Report

**22 November 2026 · probes executed 2026-11-22T03:55:16Z**
PhD: *A Graduated Safety-State-Gated Architecture for AI Decision Support in Low-Resource Coastal Fisheries.*
Scope: M1d-Q v2.5 — Malaysia or comparable international regions; Sabah optional; under-10-GRT is a
legacy experimental subgroup, not a certified threshold. `PRE_DEPARTURE` is the initial decision phase.

**No A18.1–A18.3 artifact was read for modification or modified. No new algorithm was built. No R2 review
was performed. No marine-safety claim is made.**

---

## 1. Result

| Track | Outcome |
|---|---|
| **A — R0 historical environmental** | **HOLD** — 0 bytes acquired |
| **B — authentic issued forecast/warning** | **HOLD** — 0 records acquired |
| **Combined** | **HOLD** |

`raw/` contains **0 files and 0 bytes.** `02_raw_file_manifest.csv` and
`04_issued_source_provenance.csv` are **header-only**. No placeholder, sample, synthetic or substitute
file was created, and no provider URL is presented as a dataset.

Pass 3A therefore **does not advance computational readiness**. It does produce one finding that is
independent of this environment and that changes the Track B plan — see §4.

## 2. Why Track A is HOLD — two independent blockers

**Network.** Every data-provider host was refused at this environment's egress proxy, verbatim:

```
HTTP/1.1 403 Forbidden (agent proxy: no rule or network setting allows this host)
```

6 of 7 probed hosts were refused; the control host `pypi.org` returned 200. That asymmetry
establishes the proxy is working and selectively allowlisted to package registries, so these are
policy refusals, not transient faults.

**The linked computer was probed independently**, over its own egress path, and behaved identically:
6 of 7 refused, `pypi.org` at 200. **A separate log is preserved for each environment** —
`logs/connectivity_probe_container.json` and `logs/connectivity_probe_device.json` — so neither claim
rests on prose alone. **No bypass was attempted.**

**Provider credentials.** Independently of the network, Copernicus Marine `Subset`/`Files` access needs
a free registered account and the Copernicus Marine Toolbox. Track A would remain HOLD on credentials
even with open network access. The official route is in `08_discrepancy_and_limitation_register.csv`
`P3A-02`; credentials go in environment variables, never in a file or a report.

**What was obtained.** Provider-stated metadata, through a document fetcher, for product
`GLOBAL_MULTIYEAR_WAV_001_032` (DOI `10.48670/moi-00022`): dataset
`cmems_mod_glo_wav_my_0.2deg_PT3H-i_202411`, 3-hourly, 1980-01-01 to 2026-08-31, 0.2°×0.2° regular grid,
global, Level 4, NetCDF-4, and **18 listed variables** now in
`03_environmental_metadata.csv`. **Every row is tiered `DOCUMENTED_ONLY`.** That fetcher returns
processed page text, not raw bytes; it cannot be byte-hashed and is not a provider file.

Two gaps make the page text insufficient even as a stopgap. **Units and standard names are not stated on
the pages at all** (`P3A-05`), which is precisely what Track A step 4 requires. And the product offers
**several distinct wave-height and three distinct mean-period definitions**, none of which is
automatically the A18.1 `wave_height (m)` / `wave_period (s)` pair (`P3A-06`).

## 3. Why Track B is HOLD

Same network refusal; `api.weather.gov` is additionally robots-disallowed to the document fetcher
(observed on `/openapi.json`). No record was retrieved by any route, so
`04_issued_source_provenance.csv` is header-only and **no issuance timestamp, valid period, area or
revision sequence is claimed anywhere.**

## 4. The finding that is not about this sandbox

**The NWS alerts API retains seven days.** The provider's own documentation states the `/alerts`
endpoint covers "alerts issued over the past seven days" and directs users to NCEI for an official CAP
archive. So the primary Track B candidate **cannot supply 2020–2024 issued records at any time, from any
network.** That is structural (`P3A-03`, matrix row `EL-07`).

It also means a tempting shortcut is closed off, which the task anticipated: a current November 2026
alert *would* be an authentic issued record with genuine issuance metadata, and it is **not** a
historical record. It is not used, and nothing in this folder presents it as one.

**The viable route instead is NCEI NDFD** (`P3A-04`). Provider-stated periods of record: NDFD by WMO
header **2004-06-06 to present**; an **AWS Open Data mirror 2020-04-16 to present**. That mirror
overlaps the 2020–2024 replay window for all but its first 3.5 months. Caveats on the same page: AIRS
requests for pre-2008 data are limited to one day each, and NCEI warns of delayed archival during a
cloud migration. `reproduce_acquisition.py --track-b-ndfd` documents this route and deliberately returns
HOLD rather than attempting an unbounded recursive fetch.

## 5. Evidence tiers

`06_evidence_eligibility_matrix.csv`, 14 prerequisites. **13 of 14 are NOT met.**

| Tier | Status |
|---|---|
| **R0** | **NOT ACHIEVED in this pass.** No subset acquired, no bytes hashed, no file-verified metadata |
| **R1-SOURCE-ONLY** | **NOT ACHIEVED.** No issued record; and the probed primary source cannot cover the study window regardless |
| **R1-PAIRED** | **NOT ACHIEVED.** No source, no vessel identity, no trip, no decision moment, no time-and-knowledge rights |
| **R2** | **NOT ACHIEVED.** Explicitly unobtainable from Track A/B downloads. No expert judgment was collected or simulated |
| **R3** | **NOT ACHIEVED.** Requires separately collected behaviour or outcome records |

The one prerequisite marked met is `EL-04`, and it is a **negative** safeguard: the project already holds
hash-verified environmental CSVs from A18.1, and **they are not re-badged as a Pass 3A acquisition.** They
are Open-Meteo-derived, from an earlier pass, neither a Copernicus subset nor an issued source. Doing
otherwise would have satisfied several quality gates on paper while acquiring nothing (`P3A-08`).

## 6. Quality gates

| Gate | Result |
|---|---|
| A3A-01 genuine provider file, nonempty, independently parsed | **FAIL** — 0 files |
| A3A-02 SHA-256 and byte size for every retained original | **N/A** — nothing retained; manifest header-only |
| A3A-03 variables, units, dates, coverage **from raw data** | **FAIL** — all metadata is `DOCUMENTED_ONLY`; units not even stated on the pages |
| A3A-04 issued-source provenance verified, else HOLD | **HOLD** — correctly declared |
| A3A-05 access terms, dependencies, exact query documented | **PASS** — registers 01 and 08; `requirements.txt`; exact Toolbox call in the script |
| A3A-06 tiers accurate, no false R1-PAIRED/R2 | **PASS** — all tiers NOT ACHIEVED; no R1-PAIRED or R2 asserted |
| A3A-07 report numerics checked against artifacts | **PASS** — every count in this report is read from `logs/report_metrics.json`, computed from the files |
| A3A-08 no unsupported vessel-safety or harm-prevention claim | **PASS** — none made; the length-to-tonnage transfer is restated as uncertified |
| A3A-09 bounded reproducible commands, no secret leakage | **PASS** — probes are status-only, downloads bounded, credentials env-var only |
| A3A-10 independent Track A and Track B results, combined gate | **PASS** — A HOLD, B HOLD, combined HOLD |

Four gates pass on process, one is correctly HOLD, one is N/A, and **three fail for want of data.** The
failures are reported as failures.

## 7. Documents I could not read

**None of the six mandatory Google Doc references could be opened**: `docs.google.com` is unreachable
through the egress proxy and no document connector is attached to this session. The geographic-scope
amendment, Pass 3 shortlist, Pass 1 acquisition plan, A18.3 endpoint readiness, A18.3 Pass 4 provenance
rules and the A18.2-R findings doc were **not reviewed from source** (`P3A-07`).

I worked from the task text's own explicit requirements plus the **local** A18.1, A18.2 and A18.2-R
artifacts in this repository, which I have read directly in prior passes. **I do not assert that the six
documents were reviewed.** If any requirement in them differs from the task text, this pass has not
accounted for it.

## 8. Limitations

1. **Zero acquisition.** No numeric QA finding about any dataset exists in this folder, because no
   dataset exists. The checks are implemented and unexecuted.
2. **All provider metadata is page text**, tier `DOCUMENTED_ONLY`, and provisional until read from a
   NetCDF or CAP file.
3. **No region, bounding box or time range was fixed.** The script ships a default — a 1°×1° box off
   Kota Kinabalu over 7 days of January 2024, chosen to cover the three A18.1 grid cells — explicitly
   marked as a proposal never executed against the provider (`P3A-10`).
4. **A hash proves retained bytes, not provider semantic correctness and nothing about real-world
   safety.** Carried from A18.1 Step 2 D-07.
5. **Reanalysis is hindsight.** Even a successful Track A yields R0 only and no safe/unsafe vessel label.
6. **Carried forward unchanged:** `decision_time_availability` UNKNOWN for 100% of existing records
   (D-08); no protective-action truth for the four recommendation types (A18.2 L-08); the 1.0/1.25 m band
   is an uncertified length-to-tonnage transfer (A18.1 Step 3 A-03).

## 9. What to do next, in order

1. **Re-run from an environment with provider egress.** `python3 reproduce_acquisition.py --probe` first;
   it is status-only and payload-free.
2. **Register a free Copernicus Marine account**, export the two environment variables, then
   `--track-a`. On success the script hashes the file, appends to the manifest and runs the NetCDF QA
   that produces the first real numbers.
3. **Point Track B at NCEI NDFD, not the NWS alerts API.** Read the AWS registry object layout first.
4. **Supply the six reference documents** as text or local files if anything in them constrains the
   above.

**A18.3 reference design and A18.2-R conclusions are unaffected by this HOLD.** Pass 3A changes the
Track B target and otherwise adds no evidence.
