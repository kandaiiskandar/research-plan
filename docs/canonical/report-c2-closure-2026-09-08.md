# Report: SDR-001 Execution Condition C-2 — USNO Validation Artefact Closure

**Date:** 2026-09-08
**SDR-001 status:** **APPROVED — NOT YET APPLIED** (unchanged)
**Scope:** C-2 only. C-4 through C-8 not executed. Canonical `g_t` unchanged. Prediction register byte-for-byte unchanged.

---

# RESULT

# **C-2 CLOSED — RECONSTRUCTED USNO VALIDATION ADOPTED FOR REPRODUCIBILITY**

Closed **non-destructively**. The historical result is preserved exactly as reported; the reconstructed artefact becomes the reproducibility authority going forward. **Nothing was overwritten, nothing was rounded to force agreement, and the reconstruction is nowhere presented as the original run.**

---

## 1. Status of the original 28 comparison values

> ### **Not preserved. Not recoverable.**

The project searched exhaustively for the original row-level evidence: every file for `USNO`, for a validation script, for a captured API response, for the seven validation dates in any `.csv` / `.json` / `.py`.

**`USNO` appears in prose documents only.** No validation script, no captured response, no data artefact. **Summary statistics were retained; the 28 underlying comparisons were not.**

Per the governing instruction, **no reference value was reverse-engineered from the summary statistics, and none was invented.**

---

## 2. Status assigned to the historical 0.90 / 0.37 result

> ## **historically reported, underlying comparison artefact unavailable**

Recorded in `finding-gt-evidence-closure.md` Part 2 in exactly those terms.

**What this status does say:** the project reported a 28-comparison USNO validation with maximum absolute deviation 0.90 min and mean absolute deviation 0.37 min; the 28 per-event values behind those summaries were never stored; therefore the summaries **cannot be independently reproduced from current project artefacts**.

**What this status does not say — and what was deliberately not written:**

- ❌ Not called **false**. No evidence contradicts it.
- ❌ Not called **fabricated**. There is no basis for that, and the figures are consistent with what the reconstruction independently obtains.
- ❌ Not **withdrawn**. It remains in the document, verbatim.
- ❌ **No inference drawn** about which coordinate, rounding behaviour, or reference capture produced it. That would require evidence the project does not hold. §10.

---

## 3. Reconstructed artefact identifier

| | |
|---|---|
| **Path** | `data/solar/usno-validation-2026-09-08.csv` |
| **Artefact sha256** | `da14a8dca224ae1869466c0ee03d58e5fc908fcee9ac3ac89172a8bf4a159c81` |
| **Per-row label** | **`RECONSTRUCTED-2026-09-08`** — present in all 28 rows |
| **Validation source** | `USNO AA API v4.0.1 /api/rstt/oneday` |
| **Capture date** | **2026-09-08** |
| **Implementation** | `solar-v1`, sha256 `3b7dc371ebe5931b3336f9982c5806a06a515dc2032569f5da7720470c1ec36c` |
| **Specification** | `solar-spec-v1` |
| **Rows / fields** | **28 / 20** |

---

## 4. Authoritative coordinate

> ## **φ = 5.98° N,  λ = 116.01° E**

Used for every row; verified as the single coordinate pair in the artefact.

**Why — the decision is preserved, not reopened:**

1. **It is the requested study/site coordinate**, declared identically in `openmeteo_raw_download.py` (L17–18), `collect_raw_v2.py` (L51–52) and `openmeteo_raw_rainfall.py` (L17–18), and recorded in `data-provenance.md` L143.
2. **Environmental providers snap independently to different data-grid cells** — 116.025 (wind/precipitation), 116.0 (ERA5 waves), 116.04167 (MFWAM waves). Three cells serve one site.
3. **Solar events describe the study location, not any one provider's grid centroid.** Sunrise depends on where the observer is, not on which cell supplied a wave height. Since the cells disagree, none can represent the site without arbitrarily privileging one variable.
4. **`116.07` has no demonstrated provenance** — it matches neither the request nor any delivered cell nor the superseded land cell (116.100006).

**No contrary evidence was found in this task, so the decision stands unchanged.**

---

## 5. All-event reconstructed statistics

Computed **from the 28 stored rows only** — no prose summary was consulted.

| Statistic | Full precision | Reported (2 d.p.) |
|---|---|---|
| **n** | 28 | 28 |
| **Maximum absolute difference** | 0.9200 min | **0.92 min** |
| **Mean absolute difference** | 0.3786 min | **0.38 min** |
| **Median absolute difference** | 0.3900 min | 0.39 min |
| **Minimum absolute difference** | 0.0100 min | 0.01 min |
| **Mean signed difference** | +0.0064 min | +0.01 min |

**Mean signed difference is +0.0064 min — essentially zero.** The implementation shows **no systematic bias** relative to USNO; the disagreements are scatter, not offset. This is a stronger statement than the absolute-difference summaries alone support, and it is available only because the row-level artefact now exists.

---

## 6. Sunrise/sunset-only statistics — **the events Model B actually uses**

| Statistic | Full precision | Reported |
|---|---|---|
| **n** | 14 | 14 |
| **Maximum absolute difference** | 0.7500 min | **0.75 min** |
| **Mean absolute difference** | 0.3321 min | **0.33 min** |
| Median | 0.3300 min | 0.33 min |
| Minimum | 0.0100 min | 0.01 min |
| Mean signed | −0.0293 min | −0.03 min |

Split further: **sunrise** max 0.57, mean 0.28 · **sunset** max 0.75, mean 0.38.

> ### This is the most decision-relevant finding in the reconstruction.
>
> **Model B reads sunrise and sunset only.** Across those 14 comparisons the worst disagreement is **0.75 min**, not 0.92. **The 0.92 maximum is a civil-dusk event — an event the approved classifier never evaluates.** The agreement on the events that matter is better than the headline figure implies.

---

## 7. Civil-twilight-only statistics

| Statistic | Full precision | Reported |
|---|---|---|
| **n** | 14 | 14 |
| **Maximum absolute difference** | 0.9200 min | **0.92 min** |
| **Mean absolute difference** | 0.4250 min | **0.43 min** |
| Median | 0.4150 min | 0.42 min |
| Minimum | 0.0300 min | 0.03 min |

Split: **civil dawn** max 0.71, mean 0.47 · **civil dusk** max 0.92, mean 0.38.

**Computed and stored for provenance; unused by Model B.** Civil twilight belonged to Model C, which was rejected. Retaining these rows keeps the reconstruction a faithful 4-event mirror of the historical design rather than a convenient subset.

---

## 8. Verification of all 28 rows

| Check | Result |
|---|---|
| Row count | **28** = 7 dates × 4 events ✅ |
| Rows per date | 4 for every date, no gaps ✅ |
| Distinct events | `sunrise`, `sunset`, `civil_dawn`, `civil_dusk` ✅ |
| Coordinate pairs present | exactly one: `(5.98, 116.01)` ✅ |
| Implementation version | single value `solar-v1` ✅ |
| Implementation hash | single value `3b7dc371…` ✅ |
| Validation source | single value, USNO AA API v4.0.1 ✅ |
| Capture date | single value `2026-09-08` ✅ |
| Reconstruction label | `RECONSTRUCTED-2026-09-08` on all 28 rows ✅ |

**Required-field check — all present and populated in every row:**

`date` · `event` · `latitude` · `longitude` · `local_time` · `usno_time` · `diff_signed_min` · `diff_abs_min` · `impl_version` · `impl_sha256` · `validation_source` · `validation_captured` · `artefact_status` · `spec_version`

Plus: `selection_reason`, `timezone`, `local_hours`, `usno_hours`, and — retained deliberately — `local_time_at_116_07` and `diff_abs_min_at_116_07`, so the superseded coordinate remains auditable rather than erased.

> **No row was inferred from summary statistics.** Every `usno_time` is a value returned by USNO API v4.0.1 on 2026-09-08; every `local_time` is computed by the hash-pinned implementation. The statistics in §5–§7 are recomputable from the table with no external input.

---

## 9. Validation-date coverage — verified, with one honest discrepancy

Coverage was checked against the annual extremes **computed at the canonical coordinate** from `solar-events-daily.csv`, rather than assumed from the historical descriptions.

| Intended case | Validation date | True 2024 extreme at 116.01 | Assessment |
|---|---|---|---|
| **Earliest sunrise** | 2024-05-24 (05:59:49) | 2024-05-24 (05:59:49) | ✅ **Exact** |
| **Latest sunrise** | 2024-02-02 (06:33:09) | 2024-02-04 (06:33:11) | ⚠️ 2 days off — **2 seconds** from the true extreme |
| **Earliest sunset** | 2024-11-11 (17:56:16) | 2024-11-10 (17:56:16) | ⚠️ 1 day off — **identical to the second** |
| **Latest sunset** | 2024-07-17 (18:34:58) | 2024-07-18 (18:34:58) | ⚠️ 1 day off — **identical to the second** |
| **March equinox** | 2024-03-20 | — | ✅ Correct |
| **June solstice** | 2024-06-21 | — | ✅ Correct |
| **December solstice** | 2024-12-21 | — | ✅ Correct |

> ### Documented difference
>
> **Three of the four extreme labels are off by one or two calendar days at 116.01.** The solar curve is stationary at a turning point, so the *values* are identical to the second in two cases and differ by 2 seconds in the third. **Coverage intent is fully satisfied** — the validation still probes all four annual extremes to within 2 seconds of the true extremum.
>
> **No date was changed.** Per instruction, dates were not adjusted to improve the statistics or to make the labels exact. The discrepancy is recorded instead.
>
> The historical labels were presumably assigned at 116.07, where the extreme dates may differ slightly — but **that is not asserted**, because the historical artefact is unavailable (§10).

---

## 10. Explanation of the historical / reconstructed discrepancy

**Two things must be kept apart, and the distinction is the substance of this section.**

### 10.1 Demonstrated effect

> **Changing the input longitude changes some USNO rounded event times.**

**Directly demonstrated, not inferred.** USNO reports to **whole minutes**. A re-query at 116.07 and at 116.01 for the same dates returned different values on **2 of 8 events checked across two dates**:

| Date | Event | USNO at 116.01 | USNO at 116.07 |
|---|---|---|---|
| 2024-03-20 | sunset | 18:27 | **18:26** |
| 2024-11-11 | civil dusk | 18:18 | **18:17** |

A 0.24-min (14 s) coordinate shift is therefore sufficient to move a minute-resolution reference value by a full minute at a rounding boundary.

### 10.2 Unknown historical provenance

> **We do not know precisely what inputs produced the historical summaries, because the original row-level artefact was not preserved.**

**It is therefore NOT claimed that coordinate rounding caused the 0.90 / 0.37 figures.** That would require knowing which coordinate was queried, when, and against which reference capture — none of which the project holds. §10.1 establishes only that such an effect *exists and is of the right magnitude*; it does not establish that it *is* the explanation.

### 10.3 What can be stated

- USNO outputs are minute-resolution. ✅
- Small input-coordinate changes can alter rounded minute outputs. ✅ (demonstrated, §10.1)
- The prior underlying reference table is unavailable. ✅
- **Therefore the exact origin of the 0.90 / 0.37 historical summaries cannot now be reconstructed.** ✅

**Nothing beyond this is asserted.**

---

## 11. Supersession policy — non-destructive

> ### **V_historical — RETAINED for provenance**
> Everything in Part 2 as originally written, including the 0.90 / 0.37 / 0.35 summaries and the per-date max-difference table. Status: *historically reported, underlying comparison artefact unavailable.* **Not rewritten, not withdrawn, not recalculated.** Verified still present verbatim.
>
> ### **V_reconstructed — AUTHORITATIVE for reproducibility going forward**
> `data/solar/usno-validation-2026-09-08.csv`. Every future reproducibility claim, migration check, and thesis methods statement cites this artefact.

**The rule, stated in the SDR:** *V_reconstructed supersedes V_historical **for reproducibility only**. It does not replace it as a record of what was reported at the time.*

**The sequence is visible in the project, not concealed:**

```
historical validation summary
  → missing artefact discovered        (readiness audit §4.3)
  → controlled re-query                (C-1/C-2/C-3 task)
  → reproducible validation reconstructed
  → reconstructed artefact adopted for future reproducibility   (this task)
```

**No historical audit report was rewritten** to imply the reconstruction existed earlier. Dated annotations were used throughout.

---

## 12. Exact SDR wording changed

**Three edits, all in `docs/canonical/finding-gt-evidence-closure.md`. All additive or clearly dated; no historical figure removed.**

### 12.1 Part 6, Decision clause — validation statement

**Before:**

> Validation authority: **USNO Astronomical Applications API v4.0.1**, 28 comparisons, **maximum absolute deviation 0.9 min, mean 0.37 min** (§2); sunrise/sunset alone, max 0.9 min, mean 0.35 min.

**After:**

> The local solar implementation was **historically reported** as agreeing with **USNO API v4.0.1** within **0.90 min** maximum absolute deviation and **0.37 min** mean absolute deviation over 28 comparisons. **The original row-level validation artefact was not preserved**, so those summaries are not independently reproducible from current project artefacts.
>
> A **reproducible reconstruction on 2026-09-08** at the canonical study coordinate (5.98° N, 116.01° E) produced, over the same 7 dates × 4 events: **maximum absolute deviation 0.92 min, mean 0.38 min** (0.3786), median 0.39 min; and for the **sunrise/sunset events Model B actually uses**, **maximum 0.75 min, mean 0.33 min** (0.3321). All 28 comparisons agree within one minute, with mean signed difference +0.0064 min.
>
> **The frozen 28-row artefact `data/solar/usno-validation-2026-09-08.csv` is the authoritative validation record used for reproducibility going forward.** It is labelled `RECONSTRUCTED-2026-09-08` and is **not** the original run.

The clause also now names `solar-v1`, the implementation hash, the canonical coordinate and `solar-spec-v1`.

### 12.2 Part 2 — two-evidence-object header and paired summary blocks

A dated header distinguishes **V_historical** from **V_reconstructed**. The original summary block is retained verbatim and labelled with its status; a second block reports the reconstructed statistics. The longitude note was updated from "OPEN under C-1" to the resolved decision with its four-point rationale.

### 12.3 Execution-conditions table

C-1, C-2 and C-3 marked **CLOSED 2026-09-08** with artefact paths and hashes. C-4 through C-8 untouched.

**No number was rounded to manufacture agreement.** 0.92 is reported as 0.92, not 0.9; 0.3786 as 0.38, not 0.37. Full precision preserved in the artefact.

---

## 13. Files modified

| File | Change |
|---|---|
| `docs/canonical/finding-gt-evidence-closure.md` | Three edits per §12 |

Plus this report (new).

**No other file touched.** No script, no dataset, no artefact, no register entry. `solar.py` unchanged (`3b7dc371…`); the two solar artefacts unchanged (`da14a8dc…`, `057c46a1…`) — they were read, not rewritten. A stray `__pycache__` directory created by the earlier build run was removed, leaving `scripts/sensitivity/` and `scripts/solar/` clean.

---

## 14–16. Condition status

| | Condition | Status |
|---|---|---|
| **C-1** | Pin the solar implementation and reproducibility parameters | ✅ **CLOSED** — **remains closed**; no contradiction found. This task used the same coordinate (116.01), implementation (`solar-v1` / `3b7dc371…`) and specification (`solar-spec-v1`) that C-1 pinned, and confirmed them present in every artefact row |
| **C-2** | Complete 28-row USNO validation artefact | ✅ **CLOSED** — see §17 |
| **C-3** | Daily solar-event artefact | ✅ **CLOSED** — **remains closed**; unmodified and unaffected. Used read-only in §9 to verify date coverage |

### 16.1 C-2 closure test — all eight criteria

| # | Criterion | Met |
|---|---|---|
| 1 | Historical result preserved as historical | ✅ Part 2 retains 0.90 / 0.37 / 0.35 verbatim, labelled `V_historical` |
| 2 | Missing row-level evidence explicitly acknowledged | ✅ *"historically reported, underlying comparison artefact unavailable"*, in Part 2 and in the Decision clause |
| 3 | Reconstructed 28-row artefact complete | ✅ 28 rows, 20 fields, all populated (§8) |
| 4 | Statistics reproducible directly from the artefact | ✅ §5–§7 computed from stored rows only |
| 5 | Canonical coordinate and implementation version identified | ✅ 5.98/116.01, `solar-v1`, sha256, `solar-spec-v1` — in every row |
| 6 | Reconstruction clearly labelled | ✅ `RECONSTRUCTED-2026-09-08` in all 28 rows; stated in the SDR |
| 7 | SDR points to the artefact as future reproducibility authority | ✅ §12.1 |
| 8 | No old summary silently overwritten | ✅ Every change dated; historical figures retained verbatim |

**All eight satisfied.**

---

## 17. C-4 through C-8 — confirmed OPEN

| | Condition | Status |
|---|---|---|
| **C-4** | Document binary `g_t`, graduation, accepted step cost | 🔴 **OPEN — not executed** |
| **C-5** | Three-stage hysteretic re-run for P12 | 🔴 **OPEN — not executed** |
| **C-6** | Re-resolve affected predictions | 🔴 **OPEN — not executed** |
| **C-7** | Reconcile baseline discrepancies | 🔴 **OPEN — not executed** |
| **C-8** | Execute the propagation list | 🔴 **OPEN — not executed** |

Verified: 5 conditions remain marked OPEN in the SDR. No canonical `g_t` replacement, no Appendix C classifier change, no hysteresis analysis, no prediction re-resolved, no P07/P10/P11/P12 reconciliation, no propagation into the 8 scripts, no figure regenerated, **7.72% / 5.98% unchanged**.

---

## 18. Prediction-register integrity

> ### **BYTE-FOR-BYTE UNCHANGED**
>
> `sha256 538808b6d82249faa66caf20fece38e994144fbbe2280b62d3193817a3cdc484`
> **Matches the integrity anchor `538808b6d82249fa…` exactly.**

24 entries · **22 CONFIRMED / 2 REFUTED**. No prediction record altered.

---

## 19. Canonical `g_t` integrity

> **`g_t^canonical` = `g_t^incumbent`**
> SAFE 06:00 ≤ t < 17:00 · CAUTION 17:00 ≤ t < 19:00 · UNSAFE 19:00 ≤ t < 24:00 or 00:00 ≤ t < 06:00

All three rows verbatim in Appendix C. **Solar terms in `appendix-c-formalisation.md`: 0.** Wind `21.6/27.0`, rainfall `10.0/20.0`, wave thresholds, `G(S)`, `A_AI(S)`, `cause` — all unchanged. Canonical scripts unchanged by hash (`5af9eaf7…`, `1f0f4e9c…`, `73015d88…`).

**Model B remains NOT CANONICAL. SDR-001 remains APPROVED — NOT YET APPLIED.**

---

## 20. Final scientific interpretation

**The question is not whether 0.90 = 0.92. It plainly does not.** The question is whether both support the same resolution-level conclusion.

> ### They do.
>
> **Both the historical summary and the reconstructed artefact support: the local solar implementation agrees with the authoritative reference to approximately one minute or better across the selected validation cases.**

| | Historical | Reconstructed |
|---|---|---|
| Max abs deviation | 0.90 min | **0.92 min** |
| Mean abs deviation | 0.37 min | **0.38 min** |
| All comparisons under 1 min | reported | **verified — all 28** |

The reconstruction adds two things the historical summary could not:

- **No systematic bias** — mean signed difference **+0.0064 min**. Scatter, not offset.
- **Better agreement on the events that matter** — for the sunrise/sunset events Model B evaluates, **max 0.75 min, mean 0.33 min**. The 0.92 maximum belongs to civil dusk, which the approved classifier never reads.

**Precision is not overstated.** "Approximately one minute or better" is the claim the evidence supports; "0.92 minutes" is a property of *this reconstruction at this coordinate against a minute-resolution reference*, not a stable physical constant of the implementation. The 0.02-min gap between the two runs is smaller than the reference's own quantisation, so it is not a meaningful difference in accuracy — it is two samples of the same agreement.

**The conclusion SDR-001 rested on is unchanged.** Model B's boundary can be computed locally, offline, to sub-minute agreement with a government astronomical authority — and now, for the first time, that claim is backed by a frozen artefact rather than a remembered number.

**The episode is worth keeping visible.** A validation recorded as "max 0.9, mean 0.37" was unreproducible within days of being written, not because anyone erred, but because the evidence behind it was never stored. That is exactly the class of silent loss the recomputation rule and the register guard exist to prevent, and it has now been closed for the solar component.

---

# **C-2 CLOSED — RECONSTRUCTED USNO VALIDATION ADOPTED FOR REPRODUCIBILITY**

**C-1 CLOSED · C-2 CLOSED · C-3 CLOSED · C-4 through C-8 REMAIN OPEN.**
**SDR-001 remains APPROVED — NOT YET APPLIED. Canonical migration has not begun.**
