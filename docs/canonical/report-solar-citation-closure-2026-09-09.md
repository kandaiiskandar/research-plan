# Solar Citation Closure Report

**Date:** 2026-09-09
**Scope:** Citation, provenance and validation audit for the canonical sunrise/sunset formulation used by SDR-001 Model B.
**Not:** solar-model selection · architecture redesign · new SDR · classifier change · threshold change · empirical replay · prediction re-resolution · reviewer audit.

---

# RESULT

# **SOLAR CITATION CLOSURE COMPLETE — PROVENANCE AND VALIDATION TRACEABLE**

All 37 closure criteria pass. **No stop condition triggered.**

> ### The governing principle held without strain.
>
> The implementation did not need to change to fit a citation, because **the citation supports the implementation as a faithful implementation of NOAA's published general solar-position equations with two documented simplifications.** At equation level the correspondence is exact for the equation of time, solar declination, sunrise/sunset hour angle and the 90.833° zenith — those four match coefficient-for-coefficient. The two simplifications sit in the fractional-year argument alone, and both are disclosed and **deterministically quantified against the unsimplified equations** rather than asserted to be small. **No claim is made that the implementation as a whole is an exact NOAA implementation.**

---

## 1–2. Frozen canonical state

Verified unchanged before and after: `solar.py` `3b7dc371…`, `canonical_gt.py` `b330bf9f…`, daily artefact `057c46a1…`, USNO artefact `da14a8dc…`, register `5574b88e…` (24 entries, **15 CONFIRMED / 9 REFUTED**), C-8 output `0bca160f…`, empirical findings `667161e2…`, Appendix C `03e80802…`, and all eight classifier scripts. Live recompute confirms **PRIMARY 5.81% / RESOLUTION 4.48%**.

---

## 3–4. Implementation inspected — equation level

`scripts/sensitivity/solar.py`, 39 lines, unchanged throughout.

| # | Element | Code | Implemented form |
|---|---|---|---|
| 1 | Day of year | L36 | `tm_yday` |
| 2 | Fractional year γ | L19 | `2π/365 × (doy − 1)` |
| 3 | Equation of time | L20–21 | `229.18(0.000075 + 0.001868cos γ − 0.032077sin γ − 0.014615cos 2γ − 0.040849sin 2γ)` |
| 4 | Declination | L22–24 | 7-term series to 3rd harmonic |
| 5 | Latitude conversion | L25 | `radians(lat)` |
| 6 | Hour angle | L26–28 | `arccos(cos z /(cos φ cos δ) − tan φ tan δ)` |
| 7 | Zenith | L14 | `90.833°` |
| 8 | Solar noon | — | **not implemented** (not required by `g_t`) |
| 9 | Sunrise | L29 | `720 + 4(−lon − ha) − eq` |
| 10 | Sunset | L30 | `720 + 4(−lon + ha) − eq` |
| 11 | Timezone | L31 | `utc_min/60 + tz`, east-positive |
| 12 | Invalid/polar | L27 | `clip(c, −1, 1)` — guard added in the builder/canonical layer, not here |
| 13 | Output precision | artefact | 6 decimal hours **stored** |

Full map: `data/solar-citation-closure/equation-source-map.csv`.

---

## 5. Meeus exclusion finding

> ### **The implementation is not a Meeus implementation.**

Searched for every Meeus-characteristic construct: Julian day/century, `2451545`, geometric mean longitude (`280.46`), geometric mean anomaly (`357.52`), equation of centre (`1.914602`), orbital eccentricity (`0.016708`), obliquity (`23.439`), nutation, apparent longitude, `omega`/`125.04`. **Zero occurrences.** The code uses a truncated day-angle Fourier formulation with no Julian time argument.

**Active publication sweep for surviving Meeus attribution: zero occurrences** in either working manuscript. No correction required — the C-0 cleanup already removed it and it has not returned.

---

## 6–7. NOAA provenance and equation-to-source comparison

**Source:** NOAA Global Monitoring Laboratory, *General Solar Position Calculations* — https://gml.noaa.gov/grad/solcalc/solareqns.PDF

| Element | Code | NOAA published | Match |
|---|---|---|---|
| Fractional year | `2π/365 (doy−1)` | `2π/365 (doy−1+(hour−12)/24)` | **structural** — intra-day term omitted |
| Leap year | fixed 365 | *"For leap years, use 366 instead of 365"* | **documented simplification** |
| **Equation of time** | 5-term, coefficients as above | **identical** | ✅ **EXACT** |
| **Declination** | 7-term | **identical** | ✅ **EXACT** |
| **Hour angle** | `arccos{cos(90.833)/(cos lat cos decl) − tan lat tan decl}` | **identical** | ✅ **EXACT** |
| **Zenith 90.833°** | constant | **identical**, with decomposition stated | ✅ **EXACT** |
| **Sunrise** | `720 + 4(−lon − ha) − eq` | `720 − 4(longitude + ha) − eqtime` | ✅ **EXACT** — algebraically identical |
| **Sunset** | `720 + 4(−lon + ha) − eq` | same with `ha` negated | ✅ **EXACT** |

### Simplifications quantified — reproducible provenance

| Simplification | Sunrise | Sunset | Days |
|---|---|---|---|
| Omitting NOAA's `(hour − 12)/24` term | max **0.116 min**, mean 0.057 | max **0.141 min**, mean 0.064 | doy 1–365 |
| Canonical 365 vs NOAA 366 denominator | max **0.457 min**, mean 0.118 | max **0.483 min**, mean 0.137 | doy 1–366 |

**Provenance:** `data/solar-citation-closure/verify_noaa_simplifications.py` → `noaa-simplification-check.json`. Deterministic (no randomness, no network); two consecutive runs produce a byte-identical JSON. Configuration 5.98° N, 116.01° E, UTC+8, zenith 90.833°. Each experiment isolates **one** difference in the fractional-year argument — the equation-of-time series, declination series, hour angle, zenith and sunrise/sunset expressions are identical on both sides.

**Event-time evaluation method, stated because it is a choice:** NOAA's γ depends on the event hour being solved for, so this is a fixed-point problem. A **single-pass substitution** is used — the canonical event time is substituted into NOAA's γ, without iterating to convergence. The iterated variant is computed as a robustness check and moves the intra-day sunrise bound from 0.116 to **0.115 min**, so the choice is not load-bearing.

> **Evidence class: deterministic implementation-sensitivity verification.** This compares two models against each other. It is **not** USNO validation and **not** empirical astronomical validation — no observation and no external reference are involved.

**Overall classification: faithful implementation with documented simplification.**

---

## 8. Final implementation wording

> **The solar-event calculation implements NOAA's published general solar-position equations, with two documented simplifications: the fractional-year term omits NOAA's intra-day refinement, and the day-angle denominator is held at 365 rather than 366 in leap years.**

This is stronger than the previous holding wording ("NOAA-style … formulation") and is now supported at equation level. **SOL-1 not triggered.**

---

## 9. 90.833° provenance

NOAA states it directly, including the decomposition — no invention required:

> *"the zenith is set to 90.833 (the approximate correction for atmospheric refraction at sunrise and sunset, and the size of the solar disk)"*

**Strength: DIRECT. SOL-2 not triggered.**

---

## 10. Sunrise/sunset event convention

Three layers, kept separate:

| Layer | Content | Source |
|---|---|---|
| **Astronomical event** | Zenith 90.833°; positive hour angle = sunrise, negative = sunset | NOAA — **DIRECT** |
| **Study classifier** | `sunrise ≤ t < sunset` (half-open; exact sunrise SAFE, exact sunset UNSAFE) | **Study design choice** — no astronomical source |
| **Architecture policy** | Outside that interval → UNSAFE → AI advisory withdrawn | **SDR-001** — no external source |

The astronomy source supports **only** the event calculation.

---

## 11. Malaysian authoritative-source search

| Institution | Examined | Provides | Reproducible method | Suitable |
|---|---|---|---|---|
| MET Malaysia | met.gov.my | fetch returned empty body | unknown | no |
| JUPEM / national survey | targeted search | no official ephemeris surfaced | no | no |
| Falak observatory network | prior finding | prayer-time determination | no | no |
| Commercial calculators | timeanddate, gaisma, suncalc, theskylive | sunrise/sunset tables | no published method | no — excluded as authority |

> **"No Malaysian government source providing a general-purpose, reproducible sunrise/sunset ephemeris suitable for this study was identified in the sources examined."**

The MET fetch failure is recorded as **not assessable by that route**, not as evidence of absence. Detail: `malaysia-source-search.csv`.

---

## 12–13. USNO authority and service provenance

| Field | Value |
|---|---|
| Institutional author | **U.S. Naval Observatory, Astronomical Applications Department** |
| Official title | **Astronomical Applications API v4.0.1** |
| URL | https://aa.usno.navy.mil/data/api |
| Service | `rstt/oneday` — *Complete Sun and Moon Data for One Day* |
| Template | `https://aa.usno.navy.mil/api/rstt/oneday?date=DATE&coords=COORDS&tz=TZ` |
| Coordinate convention | decimal degrees, **east-positive, north-positive** — matches `5.98, 116.01` |
| Timezone convention | **east-positive**, −12 ≤ tz ≤ +14 — matches `+8` |
| Date range | 1700–2100 — covers 2024 |
| Access | 2026-09-08 |

**§15 question answered:** version `4.0.1` is **both** the documented page heading **and** returned in the JSON as `apiversion`. Not invented, not locally assumed.

**Role separation, stated explicitly:** NOAA supplies the **implementation formulation**; USNO supplies **independent event-time comparison**. The code does not implement USNO equations, and no claim is made that it does.

---

## 14–16. Validation — historical vs reconstructed

### V_historical — retained, separately labelled
28 comparisons; max ≈ 0.90 min; mean ≈ 0.37; sunrise/sunset mean ≈ 0.35. **Underlying artefact unavailable.** Status: *historically reported, underlying comparison artefact unavailable.* **Not claimed to have been reconstructed.**

### V_reconstructed — the reproducible record
`data/solar/usno-validation-2026-09-08.csv`, `da14a8dc…` — **all §12 metadata verified**: 28 rows, 7 dates × 4 events, source `USNO AA API v4.0.1 /api/rstt/oneday`, captured 2026-09-08, coords `5.98/116.01`, `solar-v1` / `solar-spec-v1`, status `RECONSTRUCTED-2026-09-08`.

**Statistics recomputed from the frozen CSV:**

| Subset | n | Max | Mean | Expected | Result |
|---|---|---|---|---|---|
| All events | 28 | **0.9200** | **0.3786** | 0.92 / 0.38 | ✅ **REPRODUCES** |
| Sunrise/sunset only | 14 | **0.7500** | **0.3321** | 0.75 / 0.33 | ✅ **REPRODUCES** |

All 28 within one minute. Mean **signed** difference **+0.0064 min** — no systematic bias. **SOL-3 not triggered.** No new USNO data was fetched for statistics.

---

## 17–18. Leap-year approximation

Denominator is **fixed 365**, including leap years, where NOAA specifies 366. Disclosed as a low-precision approximation.

**The existing "worst sampled post-February-29 offset ≈ 0.47 min" is traced, and its scope is narrower than the new bound — the two are different quantities and must not be conflated.**

| | Historical ≈ 0.47 min | New leap bound |
|---|---|---|
| What is compared | Canonical implementation against **itself**, same *calendar date*, common year 2023 vs leap year 2024 (doy differs by one after 29 Feb) | Canonical **365** denominator against **NOAA's 366** denominator, same doy |
| Events | **Sunrise only** | Sunrise **and** sunset |
| Coverage | **5 sampled dates** | **All 366 days** |
| Value | **0.471 min** (03-20), reproduced exactly under its own definition | **0.457** sunrise / **0.483** sunset |

**0.47 is therefore not the exact combined maximum**, and is not presented as one. It is the worst of five sampled sunrise dates under a year-type comparison. The full canonical-versus-NOAA sweep gives **0.483 min** for sunset, which is the figure the manuscripts quote as the bound (rounded to 0.48). The historical figure is retained in the C-1 report as the record of what was measured there, with its scope now stated.

---

## 19. Minute-boundary sensitivity — bounded correctly

Recomputed from the frozen daily artefact; matches `solar-boundary-audit.csv` (`e8402b81…`) exactly.

| | |
|---|---|
| Definition of "within one minute" | \|h − round(h)\| × 60 < 1.0 — event decimal hour less than one minute from an **integer hour mark** |
| Sunrise events | **150** of 1,827 days |
| Sunset events | **65** of 1,827 days |
| **Overlap (both on same day)** | **0** — the counts are disjoint |
| **Union** | **215 of 1,827 days** |
| Closest approach | 0.0156 min sunrise = **0.94 s**; 0.0716 min sunset |

> **Correct interpretation:** these events demonstrate **sensitivity to minute-level rounding near classification boundaries**. They are **not** 215 incorrect classifications. Because canonical classification consumes decimal-hour values, minute-rounded display times are not the classifier input.

---

## 20. Decimal-hour semantics

`canonical_gt.py` L72–73 loads `sunrise_hours` / `sunset_hours` as floats; L34 states explicitly that classification *"consumes `sunrise_hours` / `sunset_hours` (float, 6 dp), NEVER the HH:MM:SS display columns."* Verified. Publication wording does not imply minute-rounded times are classifier inputs.

**Precision caveat added to Threats:** six-decimal-hour storage is a numerical representation, **not** a claim of corresponding astronomical accuracy.

---

## 21–22. Dependency chain and canonical consumer verification

> **solar formulation → frozen daily artefact → `g_t` → `f`**

| Script | imports `canonical_gt` | own astronomy |
|---|---|---|
| all 8 canonical scripts | **1 each** | **0 each** |

**No canonical script computes solar geometry. SOL-7 not triggered.** The daily artefact traces to the frozen implementation: every row carries `impl_sha256 = 3b7dc371…`, `solar-v1`, `solar-spec-v1`, uniform coordinate `5.98 / 116.01`, `UTC+8`, zenith `90.833`, 1,827 rows covering 2020-01-01 → 2024-12-31. **SOL-4 not triggered.**

*Noted, not a defect:* `solar.py`'s `solar_table()` default argument is the superseded `lon=116.07`. It is **never used canonically** — the builder passes `116.01` explicitly and the artefact is uniformly 116.01. The default is vestigial. Changing it would alter a frozen, hash-pinned file for cosmetic reasons and is deliberately **not** done here.

---

## 23–24. COLREG provenance and architecture-policy distinction

**Rule 20(b), verified verbatim:** *"The Rules concerning lights shall be complied with from sunset to sunrise…"* Rule 20(c) separately requires lights *"from sunrise to sunset in restricted visibility"* — confirming darkness and restricted visibility are **distinct triggers**.

**Citation quality (§26):** the reproduction consulted was eColregs, an EU-funded training resource. To avoid citation laundering the manuscript cites the **primary instrument** — IMO COLREG 1972 as amended, Rule 20(b) — not the reproduction.

**Bounded:** COLREG establishes a **lighting obligation**. It does not mandate AI abstention, fishing prohibition, a nighttime UNSAFE state, or physical danger. The chain is kept in three parts:

> astronomical source → sunrise/sunset calculation
> COLREG → maritime relevance of the sunset/sunrise boundary
> **SDR-001 → AI abstention policy**

---

## 25. Citation claim-source matrix

`data/solar-citation-closure/claim-source-matrix.csv` — SOL-C1…SOL-C12 with source, type, exact support, strength (DIRECT / STRUCTURAL / EMPIRICAL / DESIGN / LIMITATION) and publication use.

Summary: **C1, C3, C4, C5, C6(event), C7, C11 = DIRECT · C2 = STRUCTURAL · C8 = EMPIRICAL · C6(interval), C10, C12 = DESIGN · C9 = LIMITATION.**

---

## 26–28. Active-publication findings and edits

`publication-solar-audit.csv` classifies every active solar claim. **The material finding: the conference manuscript had no solar provenance sentence at all**, and its Threats section stated *"publication-reference closure remains outstanding"* — accurate at the time, and exactly what this task closes.

| # | Location | Was | Edit |
|---|---|---|---|
| 1 | Conference **Methods** | UNSOURCED — no provenance | **Added** provenance paragraph: NOAA equations, zenith with NOAA's own decomposition, both simplifications with measured bounds, decimal-hour semantics, and bounded USNO agreement |
| 2 | Conference **Threats** | AMBIGUOUS — "closure outstanding" | **Replaced** with closed provenance, the storage-vs-accuracy caveat, and the 150/65 boundary sensitivity |
| 3 | Conference **Threats** policy sentence | COLREG unreferenced | **Cited [38]**; "lighting obligation, not an operating prohibition" |
| 4 | Conference **references** | no solar sources | **Added [36] NOAA GML, [37] USNO API v4.0.1, [38] IMO COLREG Rule 20(b)** |
| 5 | **Journal 1** time/observation context | UNSOURCED | **Added** bounded provenance paragraph incl. COLREG role limit |
| 6 | `report-c1-c2-c3-solar-reproducibility-2026-09-08.md` | gap recorded OPEN | **Marked CLOSED**, original gap statement retained verbatim |

**Bounded language used throughout.** The validation sentence reads: *"For the 28 sampled comparisons at the study coordinate … differed from the USNO reference by less than one minute in every case … This is a bounded agreement check at one coordinate and date set, not a general accuracy claim."* No astronomical-grade accuracy claim, no safety validity claim, no superiority claim, and **no new empirical result** was introduced.

---

## 29–30. Files modified and integrity

**Modified — 4:**

| File | Before → After |
|---|---|
| `manuscript-v3.md` | `90f35d60…` → `bf8161f4…` |
| Journal 1 `manuscript.md` | `893626fb…` → `145eb377…` |
| `report-c1-c2-c3-solar-reproducibility-2026-09-08.md` | gap marked closed |
| — plus this report and the evidence directory |

**Created:** `data/solar-citation-closure/` — `integrity-before.json`, `integrity-after.json`, `equation-source-map.csv`, `claim-source-matrix.csv`, `publication-solar-audit.csv`, `malaysia-source-search.csv`, `validation-check.json`.

**All 16 protected artefacts byte-identical**, verified before/after: `solar.py`, `canonical_gt.py`, both solar artefacts, prediction register, C-8 output, empirical findings, Appendix C, and all eight classifier scripts.

**Frozen empirical state intact:** PRIMARY **5.81%**, RESOLUTION **4.48%** (live recompute), register **24 entries / 15 CONFIRMED / 9 REFUTED**.

---

## 31. Stop-condition assessment

| | Condition | Status |
|---|---|---|
| **SOL-1** | Attribution mismatch | ✅ **NOT TRIGGERED** — equations match at coefficient level |
| **SOL-2** | Zenith provenance failure | ✅ **NOT TRIGGERED** — NOAA states 90.833° and its decomposition |
| **SOL-3** | Validation reproduction failure | ✅ **NOT TRIGGERED** — 0.92/0.3786 and 0.75/0.3321 reproduce |
| **SOL-4** | Artefact provenance failure | ✅ **NOT TRIGGERED** — impl hash and spec in every row |
| **SOL-5** | Implementation-change requirement | ✅ **NOT TRIGGERED** — no code changed |
| **SOL-6** | Unresolved authoritative disagreement | ✅ **NOT TRIGGERED** — no conflict found |
| **SOL-7** | Canonical consumer drift | ✅ **NOT TRIGGERED** — 0 of 8 compute astronomy |
| **SOL-8** | Frozen artefact drift | ✅ **NOT TRIGGERED** — all 16 unchanged |

---

## 32. Remaining limitations

- **Deliberately low-precision.** Two simplifications relative to NOAA, bounded at ≤ 0.14 min and ≤ 0.48 min at this site. Adequate for hourly classification; not an ephemeris.
- **Validation is bounded** to 28 comparisons at one coordinate across seven dates. It establishes nothing about other sites or dates.
- **V_historical remains unreconstructable** — its row-level artefact was never stored. Retained as provenance only.
- **No Malaysian authoritative source identified** in the routes examined; MET was not assessable via the attempted fetch.
- **Boundary sensitivity persists** on ~215 of 1,827 days by construction; mitigated, not eliminated, by classifying from stored decimal hours.
- **`solar_table()` default `lon=116.07`** is vestigial and unused canonically; left unchanged deliberately.
- The **half-open interval** and the **abstention policy** have no external source and are not presented as having one.

---

## 33. Recommended next task

**Full Conference Reviewer Audit** — novelty, argument strength and reviewer-facing framing. Not begun here. Also outstanding from the publication audit: completion of planned Journal 1 sections and implementation/fidelity evidence where future claims require it.

---

---

## Addendum — CSV serialization repair, 2026-09-09

An independent parse of `equation-source-map.csv` failed with **"Expected 6 fields in line 14, saw 8"**. The evidence artefacts were originally written with a shell heredoc, and the `invalid_polar_handling` row contained the unquoted value `np.clip(c,-1,1)`, whose two internal commas were read as field delimiters.

**Repaired by rewriting, not patching.** All four CSVs were regenerated through Python `csv.writer` / `csv.DictWriter` with `QUOTE_MINIMAL`, so quoting is now decided by the serializer rather than by hand. `equation-source-map.csv` was reconstructed field-by-field from explicit Python lists with a row-width assertion; the other three were round-tripped `DictReader → DictWriter` to normalise their quoting.

**Serialization only — no scientific content changed.** The `implemented_equation` value for that row is still `np.clip(c,-1,1)` and its `match` is still *"differs - guard added in builder/canonical layer instead"*. Two incidental serialization-safety changes were made in the same rewrite: the `equation_of_time` constants list now uses semicolon separators instead of commas, and `±` / `→` were written as `+/-` / `-` in ASCII. No value, finding, source, strength label or classification was altered.

### Parser verification — all four files

| File | Columns | Rows | Malformed | `csv.DictReader` | `pandas.read_csv` |
|---|---|---|---|---|---|
| `claim-source-matrix.csv` | 7 | 12 | **0** | **PASS** | **PASS** |
| `equation-source-map.csv` | **6** | **14** | **0** | **PASS** | **PASS** |
| `malaysia-source-search.csv` | 6 | 4 | **0** | **PASS** | **PASS** |
| `publication-solar-audit.csv` | 4 | 9 | **0** | **PASS** | **PASS** |

The supplied assertion block executes clean: `len(df.columns) == 6`, `len(rows) == len(df) == 14`, and no row contains a `None` key or value.

### Hashes

| File | Before | After |
|---|---|---|
| `claim-source-matrix.csv` | `b8a6799d519e76e3…` | `aa35f8263d270926…` |
| `equation-source-map.csv` | `eb0e306c6d043582…` | `5d5a2a63b4c32767…` |
| `malaysia-source-search.csv` | `3ba696f760c9c223…` | `442dcff9c5e682d6…` |
| `publication-solar-audit.csv` | `ea4a69b1f381dbcd…` | `41e932b1f3cbf085…` |

**Only the malformed file was semantically defective; the other three changed hash solely from quoting normalisation.** All protected solar, classifier and prediction artefacts re-verified byte-identical — **SOL-8 not triggered**. The closure verdict is unaffected.


---

## Evidence Repair Addendum — final (2026-09-09)

| # | Item | Status |
|---|---|---|
| 1 | **CSV parser repair** | ✅ **PASS** — all four artefacts: 0 malformed rows, `csv.DictReader` PASS, `pandas.read_csv` PASS. `equation-source-map.csv` = 6 cols × 14 rows |
| 2 | **Global NOAA wording corrected** | ✅ **PASS** — "the citation turned out to describe it exactly" replaced with the faithful-implementation-with-two-documented-simplifications formulation, plus an explicit disclaimer that no whole-implementation exactness is claimed. Equation-level `EXACT` labels retained only where they genuinely apply (EoT, declination, hour angle, zenith). Sweep of both active manuscripts found **no** whole-implementation exactness wording — every `exactly` there is Theorem-totality phrasing ("returns exactly one element"), which is unrelated and correct |
| 3 | **Simplification-bound provenance** | ✅ **PASS** — `verify_noaa_simplifications.py` → `noaa-simplification-check.json` deterministically reproduces **0.116 / 0.141 / 0.457 / 0.483 min**; two consecutive runs give byte-identical output. Classified **deterministic implementation-sensitivity verification**, explicitly *not* USNO or empirical astronomical validation. Numbers retained in the manuscripts, now with exact values and evidence class rather than rounded assertions |
| 4 | **Historical ≈ 0.47 min reconciled** | ✅ **PASS** — scope stated in both reports: it is the canonical implementation **against itself**, same calendar date, common year vs leap year, **sunrise only, five sampled dates** (0.471 min at 03-20). It is **not** the canonical-vs-NOAA comparison and **not** a combined maximum. The full 366-day sweep gives 0.457 sunrise / **0.483 sunset**, which is what the manuscripts now quote |
| 5 | **Protected hashes unchanged** | ✅ **PASS** — `solar.py` `3b7dc371ebe5931b…`, `canonical_gt.py` `b330bf9f94e848aa…`, daily artefact `057c46a19d0e8ea7…`, USNO artefact `da14a8dca224ae18…`, register `5574b88ea65168b6…`, Appendix C `03e80802a46404df…`, empirical findings `667161e288d5e403…` — all identical to the pre-task baseline. **SOL-8 not triggered** |
| 6 | **PRIMARY / RESOLUTION** | ✅ **PASS** — **5.81% / 4.48%**, live recompute from the migrated canonical pipeline |
| 7 | **Prediction register** | ✅ **PASS** — **24 entries · 15 CONFIRMED · 9 REFUTED**, unchanged |

**Robustness note carried forward, not buried:** the intra-day bound depends on a stated methodological choice — single-pass substitution of the canonical event time into NOAA's γ rather than iterating the fixed point. The iterated variant gives 0.115 min instead of 0.116 min for sunrise, so the choice moves the third decimal only and is recorded in the JSON as `robustness_check`.

**Nothing scientific changed in this repair.** No classifier, threshold, artefact, figure or prediction outcome was touched; the edits were serialization, wording scope, and evidence provenance.

# **SOLAR CITATION CLOSURE COMPLETE — EVIDENCE REPAIR VERIFIED**
