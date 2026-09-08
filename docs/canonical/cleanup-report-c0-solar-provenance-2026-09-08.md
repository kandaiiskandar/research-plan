# Cleanup Report: C-0 — Solar Algorithm Provenance Correction

**Date:** 2026-09-08
**Basis:** `finding-sdr-001-readiness-audit.md` — condition **C-0**, the sole pre-approval condition
**Scope:** Documentation/provenance only. **Model B not adopted. C-1…C-8 not executed. No script, figure, threshold or prediction touched.**

---

## 1. Algorithm identified from `scripts/sensitivity/solar.py`

**The code implements a low-precision solar-position formulation built on a truncated Fourier series in the day angle. It is not Meeus.**

Adopted name, used consistently in the corrected documents:

> ### **NOAA-style low-precision solar-position formulation implemented in `scripts/sensitivity/solar.py`**

This is the conservative wording that instruction 5 authorises. §2.4 explains why a more specific name — including `NOAA/Spencer` — is not yet supportable from project evidence.

---

## 2. Evidence for the identification

### 2.1 Component-by-component, read from the code

| Component | Code (`solar.py`) | Reading |
|---|---|---|
| **Day angle** | `g = 2*np.pi/365.0 * (doy - 1)` | Fractional-year angle from **day-of-year**. A fixed **365-day** year — no Julian Day, no century argument |
| **Equation of time** | `229.18*(0.000075 + 0.001868·cos g − 0.032077·sin g − 0.014615·cos 2g − 0.040849·sin 2g)` | Truncated **Fourier series in `g`**, to 2nd harmonic. `229.18 ≈ 1440/2π`, converting radians → minutes |
| **Declination** | `0.006918 − 0.399912·cos g + 0.070257·sin g − 0.006758·cos 2g + 0.000907·sin 2g − 0.002697·cos 3g + 0.00148·sin 3g` | Truncated **Fourier series in `g`**, to 3rd harmonic. Result in **radians** — used directly in `cos`/`tan` with no conversion, which is internally consistent |
| **Solar zenith** | `ZENITH_SUNRISE = 90.833` (refraction + semi-diameter); `ZENITH_CIVIL = 96.0` | **Fixed constants.** No pressure, temperature, or observer-elevation term |
| **Sunrise/sunset** | `c = cos(z)/(cos φ·cos δ) − tan φ·tan δ`; `ha = degrees(arccos(clip(c,−1,1)))`; `rise = 720 + 4(−lon − ha) − eq`; `set = 720 + 4(−lon + ha) − eq` | Standard **hour-angle** equation, solved once per day in UTC minutes. `clip` silently bounds polar cases rather than signalling no-event |
| **Timezone** | `return rise_utc_min/60.0 + tz`, `tz=8` | UTC minutes → hours, then a **constant integer offset**. No DST logic (correct for Malaysia; the reason is unrecorded) |

### 2.2 Decisive structural test — no Meeus construct is present

Meeus, *Astronomical Algorithms* (2nd ed., 1998) computes solar position from a **Julian-century time argument** `T`, then geometric mean longitude, geometric mean anomaly, equation of centre, true/apparent longitude, and mean/apparent obliquity of the ecliptic.

Searched `solar.py` for every one of these constructs and their characteristic constants (`julian`, `jd`, `century`, `2451545`, `280.46`, `357.52`, `equation of centre`, `obliquity`, `23.439`, `eccentricity`):

> **Zero matches. The file is 39 lines; none of the Meeus machinery exists in it.**

The distinction is structural, not a matter of tuning: Meeus's time argument is Julian centuries since J2000.0; this code's is an integer day-of-year over a 365-day year. **These are different methods, and only one of them was validated.**

### 2.3 What the docstring calls it

`solar.py` lines 1 and 6–7:

> *"NOAA solar position algorithm"* … *"Reference: NOAA Global Monitoring Laboratory solar calculator equations (Astronomical Almanac low-precision formulae)."*

**The docstring names two distinct sources at once** — the NOAA GML calculator *and* the *Astronomical Almanac* low-precision formulae. These are not the same artefact. **The file's own attribution is therefore already imprecise**, independently of the Meeus error, and this is part of how the confusion propagated.

### 2.4 Why not "NOAA/Spencer" — the limit of what the project can claim

The readiness audit called this "NOAA GML / Spencer (1971)". The **mathematical form is genuinely of the Spencer type** — the declination and equation-of-time series in the day angle are the well-known truncated-Fourier form associated with that work. But three things must be separated, per instruction 5:

| Question | Answer |
|---|---|
| **What does the code implement?** | A truncated Fourier series in `Γ = 2π(doy−1)/365`, plus the standard hour-angle equation and fixed zenith constants — **established from the code** |
| **What does the code call it?** | NOAA GML calculator equations **and** Astronomical Almanac low-precision formulae — **two attributions, neither verified** |
| **What is traceable to Spencer in this project?** | **Nothing.** The project holds **no Spencer citation** — no reference entry, no notes file, no URL. The name appears only in the readiness audit's own diagnosis |
| **What does NOAA publish?** | **Not determined here.** NOAA solar material describes more than one formulation, and the project has not established which corresponds to this code |

**Naming it "NOAA/Spencer" would manufacture a citation chain the project does not possess** — the same class of error as C-0 itself, in the opposite direction. The audit's hybrid has therefore been superseded and the audit annotated (§6).

**Recorded citation gap → C-1:** the exact published reference, coefficient rendering, and edition must be identified and cited before the implementation is pinned. **C-0 does not require this.** C-0 requires only that the SDR stop naming an algorithm that was not validated.

---

## 3. Previous SDR-001 wording

`finding-gt-evidence-closure.md`, Part 6, Decision clause:

> Sunrise and sunset computed per (date, latitude, longitude) by the **Meeus algorithm**, validated against USNO API v4.0.1 (max deviation 0.9 min, §2).

**Defect:** asserts an algorithm that was never implemented and never validated, and attaches to it a validation result obtained from different code. Approving this clause would have authorised, as canonical, a method this project has no evidence for.

---

## 4. Corrected SDR-001 wording

> Sunrise and sunset computed per (date, latitude, longitude) by the **NOAA-style low-precision solar-position formulation implemented in `scripts/sensitivity/solar.py`** — the local implementation that was actually validated. Validation authority: **USNO Astronomical Applications API v4.0.1**, 28 comparisons, **maximum absolute deviation 0.9 min, mean 0.37 min** (§2); sunrise/sunset alone, max 0.9 min, mean 0.35 min.
>
> **USNO is the independent astronomical reference against which the local implementation was checked. It is not the source of the algorithm, and no claim is made that USNO uses this or any particular formulation.**

Followed by a dated correction note recording the previous wording, the structural evidence, the decision to preserve the implementation, and the residual C-1 citation gap.

**All four required elements are present:** (1) computation by the implementation actually in `solar.py`; (2) validated against USNO API v4.0.1; (3) the existing recorded deviations, unchanged; (4) USNO named as independent reference, **explicitly not as algorithm source**.

**Unchanged:** the decision is still Model B (fixed-clock three-state → solar-event two-state); the classifier definition, rationale, rejected alternatives, known consequences and approval conditions are untouched; **status remains DRAFT — NOT APPROVED — NOT APPLIED**.

---

## 5. Every active/canonical provenance statement inspected

Swept `Meeus`, `NOAA`, `Spencer`, `solar.py`, `solar_table`, `0.9 min`, `0.37`, `0.35 min`, `28 comparisons`, `7 dates` across `docs/`, `publications/`, `scripts/`, `CLAUDE.md`.

| # | Location | Statement | Class | Action |
|---|---|---|---|---|
| 1 | `finding-gt-evidence-closure.md` **Part 6 Decision** | "by the Meeus algorithm, validated against USNO" | ❌ **INCORRECT** | **Corrected** |
| 2 | `finding-gt-evidence-closure.md` **Part 2 header** | "(`solar.py`, NOAA/Meeus formulae)" | ❌ **INCORRECT** — prohibited hybrid | **Corrected** |
| 3 | `finding-gt-evidence-closure.md` **§1.3** | "**Method:** Meeus, *Astronomical Algorithms*…" | ⚠️ **AMBIGUOUS** — a *recommendation* read downstream as a description; the origin of the defect | **Corrected + annotated** |
| 4 | `finding-gt-evidence-closure.md` **Part 10 sources, NOAA row** | "Corroborating government implementation of **the same formulae**" | ❌ **INCORRECT** — asserts an unestablished equivalence; a propagation route | **Corrected** |
| 5 | `finding-gt-evidence-closure.md` **Part 10 sources, Meeus row** | "**Recommended method** — offline-reproducible, citable" | ⚠️ **AMBIGUOUS** post-correction | **Corrected** to "Candidate method, not implemented" |
| 6 | `finding-gt-evidence-closure.md` **§1.1 table** (lines 15, 18, 23) | "NOAA states it implements the Meeus formulae"; "cites Meeus rather than being primary" | ✅ **EXTERNAL-SOURCE DESCRIPTION** — true of NOAA's *own web calculator* | **Text unchanged; guard added** so it cannot be chained into a claim about `solar.py` |
| 7 | `finding-gt-sensitivity-analysis.md` **§7** | "NOAA GML solar-position equations (Astronomical Almanac low-precision formulae), implemented in `solar.py`" | ✅ **FREE OF THE C-0 DEFECT** — verified, not assumed; **but imprecise** (two attributions) | **Text unchanged; note added.** See §6 |
| 8 | `finding-sdr-001-readiness-audit.md` §4.1–4.2, §11 | "NOAA GML / Spencer (1971)", "NOAA/Spencer" | ⚠️ **AMBIGUOUS** — overstates provenance (§2.4) | **Annotated, not rewritten;** C-0 marked CLOSED |
| 9 | `scripts/sensitivity/solar.py` lines 1, 6–7 | "NOAA solar position algorithm"; two-source reference | ⚠️ **AMBIGUOUS** | **UNCHANGED — scripts out of scope.** → C-1 |
| 10 | `scripts/sensitivity/gt_counterfactual.py` line 13 | "Solar times: NOAA algorithm" | ⚠️ **AMBIGUOUS** | **UNCHANGED — scripts out of scope.** → C-1 |
| 11 | `cleanup-report-unsafe-semantics-2026-09-08.md` | "0 occurrences of sunrise/sunset/USNO/Meeus in `appendix-c`" | ✅ **CORRECT** — a verification record, still true | None |
| 12 | `publications/.../*` `0.37`/`375–400` hits | Cash et al. page range | ✅ **UNRELATED** — false positives | None |
| 13 | `appendix-c-formalisation.md` | — | ✅ **NO SOLAR CONTENT.** `grep -ci "sunrise\|sunset\|USNO\|Meeus"` → **0** | None |

**No statement anywhere claims USNO uses Meeus or any particular algorithm.** Verified.

---

## 6. Verification of the sensitivity-analysis wording — checked, not assumed

The readiness audit reported §7 of `finding-gt-sensitivity-analysis.md` as already correct. **Verified directly against the file.**

**Confirmed free of the C-0 defect:** it does not name Meeus, does not use a Meeus/NOAA hybrid, and does not attribute the validation to an unimplemented algorithm. It is the only document that never carried the defect — which is why it alone needed no correction while the evidence-closure needed five.

**But it is imprecise**, and the audit's "correct" was slightly generous. It attributes the code to **two distinct sources simultaneously** — NOAA GML calculator equations *and* Astronomical Almanac low-precision formulae — and the code's actual Fourier-series form is not established in this project as matching either as published.

**Left as written, deliberately.** C-0 licenses correcting statements that repeat the *Meeus* defect; it is not a mandate for a general terminology rewrite. A dated note records the agreed conservative term and routes the precision question to C-1.

---

## 7. Statements deliberately left unchanged

| Location | Why |
|---|---|
| **`scripts/sensitivity/solar.py`** — code **and** docstring | **Scripts are explicitly out of scope**, and the integrity requirement is that the solar implementation itself be unchanged. Preserving the code is the *point* of the C-0 decision: evidence follows implementation. Docstring imprecision → **C-1** |
| `scripts/sensitivity/gt_counterfactual.py` line 13 | Same |
| `finding-gt-evidence-closure.md` §1.1 candidate-source table | **External-source descriptions**, true as written. Guarded rather than rewritten |
| `finding-gt-sensitivity-analysis.md` §7 method sentence | §6 |
| `finding-sdr-001-readiness-audit.md` diagnostic text | It is the **record of how the defect was found**. Rewriting it would erase the audit trail. Annotated; its finding is unchanged |
| All archived manuscripts and `docs/obsolete/` | Historical; contain no solar provenance claim |

**Nothing was silently rewritten.** Every correction carries a dated marker naming the prior wording.

---

## 8. Validation values — not recomputed

**No validation was re-run. No solar calculation was executed. No network call was made.**

| Value | Status |
|---|---|
| Validation dates | **7** — unchanged |
| Events per date | **4** — unchanged |
| Total comparisons | **28** — unchanged |
| Maximum absolute difference | **0.9 min** — unchanged |
| Mean absolute difference | **0.37 min** — unchanged |
| Sunrise/sunset max | **0.9 min** — unchanged |
| Sunrise/sunset mean | **0.35 min** — unchanged |
| Per-date table (7 rows, 2024-02-02 … 2024-12-21) | Unchanged |
| Near-boundary counts (160 sunrise / 60 sunset days; closest 0.02 min) | Unchanged |

**This task changed what those numbers are understood to validate, not the numbers.** They were always measurements of `solar.py`; only the label attached to `solar.py` was wrong.

---

## 9. Longitude inconsistency — OPEN under C-1

| | |
|---|---|
| `solar.py` default | **116.07° E** |
| Dataset site (`empirical-findings-2026-09-06.md` §5) | **116.01° E** |
| Difference | 0.06° ≈ **14 s of solar time** |

**Not resolved in this task. Neither coordinate chosen. No solar value recomputed.** Recorded as an OPEN C-1 item in the Part 2 validation block, where the 116.07 figure appears, so the discrepancy is visible at the point of use rather than only in the audit.

---

## 10. Status of C-0

> # **C-0 — CLOSED**

| Requirement | Met? |
|---|---|
| SDR-001 no longer names an algorithm that was not validated | ✅ |
| The named implementation is the one actually in `solar.py` | ✅ |
| Identification evidenced from the code, not assumed | ✅ §2 |
| Validation authority named as USNO API v4.0.1 | ✅ |
| Recorded deviations preserved exactly | ✅ §8 |
| USNO not implied to be the algorithm source | ✅ Stated explicitly |
| No prohibited hybrid naming survives in an active claim | ✅ §5 |
| Implementation preserved rather than replaced to fit prior wording | ✅ Meeus not implemented |
| Model B unchanged; SDR status unchanged | ✅ DRAFT — NOT APPROVED — NOT APPLIED |

---

## 11. C-1 through C-8 remain OPEN

**Closing C-0 does not solve solar reproducibility.** C-0 was one condition: *stop naming an unvalidated algorithm*. Everything else stands.

| | Condition | Status |
|---|---|---|
| **C-1** | Pin the implementation — **exact published reference (§2.4)**, version/commit, **longitude 116.07 vs 116.01 (§9)**, leap-year handling, timezone documentation, invalid-input/`⊥` behaviour, rounding rule, zenith constants, boundary rule. **Also: the imprecise attributions in `solar.py`, `gt_counterfactual.py` and sensitivity §7** | 🔴 **OPEN** |
| **C-2** | Record the 28 per-event USNO reference values in the specification | 🔴 **OPEN** |
| **C-3** | Store daily sunrise/sunset timestamps; make figures re-derivable from stored inputs + version | 🔴 **OPEN** |
| **C-4** | Accept the SAFE→UNSAFE step cost (2 → 1,536); non-surjectivity statement | 🔴 **OPEN** |
| **C-5** | Three-stage hysteretic re-run before re-resolving P12 | 🔴 **OPEN** |
| **C-6** | Re-resolve the 16 computable predictions | 🔴 **OPEN** |
| **C-7** | Reconcile baselines (P07 87.58 · P10 230 · P11 37 · P12 7.83) | 🔴 **OPEN — untouched, per instruction 8** |
| **C-8** | Execute the corrected propagation list (8 scripts, ~17 documents) | 🔴 **OPEN** |

**Explicitly not done in this task:** no prediction inspected or altered; no coordinate chosen; no version pinned; no timestamps stored; no per-event values recorded; no classifier change.

---

## 12. Integrity check

**Three files modified, all documentation. Verified by mtime — no other file was touched.**

| Item | Status | Evidence |
|---|---|---|
| **Canonical `g_t`** | ✅ **UNCHANGED** | `06:00 ≤ t < 17:00` / `17:00 ≤ t < 19:00` / `19:00 ≤ t < 24:00 or 00:00 ≤ t < 06:00` |
| **Appendix C classifier** | ✅ **UNCHANGED** | Not modified. `grep -ci "sunrise\|sunset\|USNO\|Meeus"` → **0** — no solar content introduced |
| **Wind / rainfall / wave thresholds** | ✅ **UNCHANGED** | `21.6, 27.0` · `10.0, 20.0` · `{small:(1.0,1.25), medium:(1.4,2.8), big:(1.5,3.5)}` |
| **`cause`** | ✅ **UNCHANGED** | `cause : Y → {fault, hazard}` intact |
| **Scripts** | ✅ **UNCHANGED** | `canonical_figures.py` `5af9eaf7f4420180` · `condition_comparison.py` `1f0f4e9cd2868820` · `hysteresis_analysis.py` `73015d881a29cd4d` |
| **Solar implementation itself** | ✅ **UNCHANGED** | `solar.py` `3b7dc371ebe5931b` · `gt_counterfactual.py` `eb58508e9159722d` |
| **Replay outputs** | ✅ **UNCHANGED** | Nothing executed |
| **Sensitivity outputs** | ✅ **UNCHANGED** | Nothing re-run |
| **Figures** | ✅ **UNCHANGED** | 7.72% ×8, 5.98% ×5 in §0a |
| **Prediction register** | ✅ **BYTE-FOR-BYTE UNCHANGED** | `sha256 538808b6d82249fa…` — **identical to the hash recorded in the readiness audit** |
| **All prediction outcomes** | ✅ **UNCHANGED** | 24 entries, 22 CONFIRMED / 2 REFUTED. P07 87.58 · P09 5416 · P10 230 · P11 37 · P12 7.83 · P16 2 · P18 8.32 · P19 6.1 |
| **C-1 … C-8** | ✅ **ALL OPEN** | §11 |
| **SDR-001** | ✅ **DRAFT — NOT APPROVED — NOT APPLIED** | Line 176 |
| **Model B** | ✅ **NOT ADOPTED** | Decision unchanged; classifier untouched |

**Files modified (3):** `finding-gt-evidence-closure.md` (5 edits) · `finding-gt-sensitivity-analysis.md` (1 note) · `finding-sdr-001-readiness-audit.md` (2 annotations). Plus this report.

---

## 13. Assessment

The correction was small and the principle behind it is not. The project's own recorded failure mode — the 7.5 mm/hr threshold — was a value in the code with a different justification in the document, and nothing comparing the two. **C-0 was the same shape**: `solar.py` computing one thing while the decision record claimed another, with a validation result sitting between them and belonging to neither as described.

The right resolution was the one the instruction specified: **preserve what was validated and correct what was written**. Implementing Meeus to rescue the prior wording would have inverted the method — manufacturing evidence to fit a document, having just caught a document that did not fit its evidence.

**What remains honest to say:** the project still cannot name the exact published source of the formulation it uses. That is a real gap, it is recorded, and it is C-1's to close. C-0 asked only that the SDR stop claiming a source it does not have — and it no longer does.

---

# **C-0 CLOSED — SDR-001 READY FOR APPROVAL DECISION**

*The approval decision itself is not taken here. SDR-001 remains **DRAFT — NOT APPROVED — NOT APPLIED**, and C-1 through C-8 remain open as conditions on canonical migration.*
