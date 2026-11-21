# A18.1 Step 4 — Independent Numerical Reproduction Report

**21 November 2026 · supervisor-ready · Step 4 only**
Accepted AAI2026 paper, presentation 23 December 2026 · git commit `6c8d783` · **originals byte-identical before and after**

Evidence tiers: `VERIFIED_FROM_CODE` · `COMPUTED_FROM_DATA` · `MANUSCRIPT_REPORTED` · `INFERRED` · `UNKNOWN`.

---

## 1. Status: EXACT

Every reportable manuscript figure reproduced — **34 of 34 reconciliation rows**, by two independent calculation paths, agreeing at **integer-count level** and not merely after rounding. Thirty-two rows are manuscript targets; two are all-hours figures the paper withholds.

This is the strict EXACT criterion: canonical source data and the original code match every reportable target, **and** an audit-independent implementation that shares no dependency with the original also agrees, with provenance for each value.

One qualification that matters more than the status label. Every headline reproduced here is **an identity, not a measured comparative effect**. All four claimed identities held exactly:

| Identity | PRIMARY | RESOLUTION |
|---|---|---|
| D(C1,C2) = #CAUTION / n | 531/9,135 ✓ | 266/5,935 ✓ |
| D(C0,C1) = #UNSAFE / n | 3,917/9,135 ✓ | 2,438/5,935 ✓ |
| D(C0,C2) = (#CAUTION+#UNSAFE) / n | 4,448/9,135 ✓ | 2,704/5,935 ✓ |
| D(C1,C3) = 0 / n | 0/9,135 ✓ | 0/5,935 ✓ |

So the three reported percentages are **state-occupancy frequencies re-expressed as policy divergences**. They are numerically correct and structurally definitional. That is not a defect; it is what the contract makes them.

---

## 2. Table A — Record-count reconciliation

| Quantity | PRIMARY | RESOLUTION |
|---|---:|---:|
| Weather source rows | 43,848 | 43,848 |
| Wave source rows | 43,848 | 28,512 |
| Inner join on `time` | 43,848 | 28,512 |
| Rejected: no wave row for timestamp | 0 | 15,336 |
| Rejected: null `wave_height (m)` | 0 | **11** |
| Rejected: null `wind_speed_10m (kn)` | 0 | 0 |
| Rejected: null `precipitation (mm)` | 0 | 0 |
| **Usable rows** | **43,848** | **28,501** |
| **Departure-window rows (05–09 inclusive)** | **9,135** | **5,935** |
| Coverage | 2020-01-01T00:00 → 2024-12-31T23:00 | 2021-10-01T00:00 → 2024-12-31T23:00 |
| Distinct days | 1,827 | 1,188 |

`COMPUTED_FROM_DATA`. The 11 nulls are contiguous, `2021-10-01T00:00` to `10:00`, and **5** of them fall at 05:00–09:00 — which is exactly why 5,940 window hours become 5,935. Filter logic: inner join on `time`, then drop rows with a null in wave height, wind speed or precipitation. `wave_period` and tide play no part (Step 2 D-02, D-06).

**Raw weather coverage vs usable replay coverage**: weather supplies 43,848 hours in both configurations; RESOLUTION's usable set is smaller purely because the MFWAM wave product starts 2021-10-01 and has the 11-hour leading gap. No mismatch is unexplained.

---

## 3. Table B — State distribution

| Config | Scope | n | SAFE | CAUTION | UNSAFE |
|---|---|---:|---:|---:|---:|
| PRIMARY | departure window | 9,135 | 4,687 (51.31%) | **531 (5.8128%)** | 3,917 (42.879%) |
| PRIMARY | all hours | 43,848 | 18,401 (41.97%) | 2,091 (4.7687%) | 23,356 (53.27%) |
| RESOLUTION | departure window | 5,935 | 3,231 (54.44%) | **266 (4.4819%)** | 2,438 (41.078%) |
| RESOLUTION | all hours | 28,501 | 12,540 (44.00%) | 1,110 (3.8946%) | 14,851 (52.11%) |

Counts sum to the denominator in every row. **All states are LOWER BOUNDS on severity**: `g_m` is pinned SAFE, and because aggregation is by maximum, a real warning archive could only raise them. This is a model assumption, not observed absence of warnings.

---

## 4. Table C — Pairwise policy divergence

Departure window. Numerator / denominator given before any percentage.

| Pair | PRIMARY | RESOLUTION | Identity | Holds |
|---|---|---|---|---|
| C0 vs C1 | 3,917/9,135 = **42.879%** | 2,438/5,935 = **41.0783%** | #UNSAFE/n | **YES** |
| C0 vs C2 | 4,448/9,135 = **48.6918%** | 2,704/5,935 = **45.5602%** | (#CAUTION+#UNSAFE)/n | **YES** |
| C0 vs C3 | 3,917/9,135 = 42.879% | 2,438/5,935 = 41.0783% | — | — |
| C1 vs C2 | 531/9,135 = **5.8128%** | 266/5,935 = **4.4819%** | #CAUTION/n | **YES** |
| C1 vs C3 | 0/9,135 = **0.0000%** | 0/5,935 = **0.0000%** | 0/n | **YES** |
| C2 vs C3 | 531/9,135 = 5.8128% | 266/5,935 = 4.4819% | — | — |

Per-state contributions confirm the mechanism: C1-vs-C2 diverges at CAUTION hours only, C0-vs-C1 at UNSAFE hours only, C0-vs-C2 at both.

**Two readings this table does not support.** C0 vs C1 is a **participation-restriction frequency, not action accuracy**. And no divergence figure is AI proposal exclusion: the replay has **no AI proposal generator**, so no recommendation was ever actually withheld from anyone (B-05). All four configurations are output masks over a fixed candidate space.

---

## 5. Table D — Manuscript target vs independent calculation

Full table in `07_manuscript_numerical_reconciliation.csv` (34 rows). Headlines:

| Target | Manuscript | Reproduced | Numerator/denominator | Conclusion |
|---|---:|---:|---|---|
| PRIMARY Δ_L2 | 5.81% | **5.8128%** | 531/9,135 | **PASS** |
| RESOLUTION Δ_L2 | 4.48% | **4.4819%** | 266/5,935 | **PASS** |
| PRIMARY participation-only | 42.88% | **42.8790%** | 3,917/9,135 | **PASS** |
| RESOLUTION participation-only | 41.08% | **41.0783%** | 2,438/5,935 | **PASS** |
| PRIMARY combined | 48.69% | **48.6918%** | 4,448/9,135 | **PASS** |
| RESOLUTION combined | 45.56% | **45.5602%** | 2,704/5,935 | **PASS** |
| C1 vs C3, both configs | 0.00% | **0.0000%** | 0/n | **PASS** — definitional |
| PRIMARY CAUTION hours | 531 | **531** | — | **PASS** |
| PRIMARY attribution wave/rain | 518 / 13 | **518 / 13** | of 531 | **PASS** |
| PRIMARY wave-band sensitivity | 5.81–9.22% | **5.8128–9.2173%** | 531 → 842 | **PASS** |
| RESOLUTION wave-band sensitivity | 4.48–6.08% | **4.4819–6.0826%** | 266 → 361 | **PASS** |
| PRIMARY sourced envelope | 5.67–9.56% | **5.67–9.56%** | 10 cells | **PASS** |
| RESOLUTION sourced envelope | 4.26–6.64% | **4.26–6.64%** | 10 cells | **PASS** |
| PRIMARY daylight-only | 9.59% | **9.5918%** | 531/5,536 | **PASS** |
| RESOLUTION daylight-only | 7.40% | **7.4012%** | 266/3,594 | **PASS** |
| PRIMARY big-vessel band | 1.26% | **1.2589%** | 115/9,135 | **PASS** |
| PRIMARY medium-vessel band | 1.96% | **1.9595%** | 179/9,135 | **PASS** |
| RESOLUTION medium / big | 0.66% / 0.37% | **0.6571% / 0.3707%** | 39 / 22 of 5,935 | **PASS** |
| PRIMARY rainfall spread | 0.48 pp | **0.4817 pp** | 5.6705–6.1522% | **PASS** |
| RESOLUTION rainfall spread | 0.78 pp | **0.7751 pp** | 4.2628–5.0379% | **PASS** |
| PRIMARY wind sensitivity | structural zero | **0.0000 pp spread** | 531 at every W_C | **PASS** |

Both optional secondary figures named in the brief reproduced: **large-vessel 1.26%** and **daylight-only 9.59%**, each with an established denominator. Nothing is marked NOT_REPRODUCED.

### The wind structural zero is worth stating plainly

Across W_C ∈ {18.0, 20.0, 21.6, 22.0, 25.0} — a seven-knot sweep — Δ_L2 is **531 hours at every single value**. The wind term enters CAUTION **once** in 9,135 window hours and is the binding component **never**. The threshold sits above the observed range, so wind contributes nothing at this site regardless of where in that range it is placed.

---

## 6. Table E — Sensitivity configurations

80 rows in `08_sensitivity_and_secondary_results.csv`, covering every variant the source defines and no others. Operators held fixed throughout: wind and rain strict `>`; wave `≥ O_C` and `> O_U`.

| Group | Register | Variants | PRIMARY Δ_L2 | RESOLUTION Δ_L2 |
|---|---|---|---|---|
| Canonical | A1/A39 | (1.0, 1.25) small | 5.8128% | 4.4819% |
| Rainfall | A2–A6 | R_C ∈ {5.0, 7.5, 10.0, 15.0, 19.9} | 6.1522 → 5.6705% | 5.0379 → 4.2628% |
| Wind | A7–A11 | W_C ∈ {18.0, 20.0, 21.6, 22.0, 25.0} | 5.8128% throughout | 4.4819% throughout |
| Wave | A12–A17 | six (O_C, O_U) pairs | 1.2589 → 14.7455% | 0.3707 → 14.1870% |
| Denominator | A18/A56 | daylight-only | 9.5918% (n = 5,536) | 7.4012% (n = 3,594) |
| Grid | A19–A38 | R_C × 4 wave configs | full 1.11–9.56%; **sourced 5.67–9.56%** | full 0.15–6.64%; **sourced 4.26–6.64%** |
| Common period | A77/A78 | same 5,935 hours | 6.4532% | 4.4819% |

**A scope caveat on the envelope (B-02).** The register's "sourced envelope 5.67–9.56%" is the min–max over the **small-vessel** wave configurations only. The full 20-cell grid spans 1.11–9.56%, because two of its four wave rows are the medium and big vessel bands — a different vessel class. The published figure is correct for its stated scope; it should say "small vessel" wherever it appears.

The ±0.25 m pair results (14.75% and 2.54% PRIMARY) reproduced but are **removed from the paper** by the register's own decision, so they are not reconciliation targets.

### The PRIMARY/RESOLUTION gap decomposes into two opposing effects

On the **same 5,935 common window hours**:

| Effect | Calculation | Value |
|---|---|---:|
| Wave product + co-location | 6.4532% − 4.4819% | **+1.9713 pp** |
| Record length | 5.8128% − 6.4532% | **−0.6404 pp** |
| Net observed | 5.8128% − 4.4819% | +1.3309 pp |

Both reproduce to two decimal places against the +1.97 and −0.64 recorded in the repository. **The headline 5.81-vs-4.48 gap is not one resolution effect**; it is two effects of opposite sign that partially cancel. And per Step 2 D-12 the +1.97 pp cannot be attributed to grid resolution alone, because wind–wave co-location changes with it (7.20 km vs 2.73 km).

---

## 7. Table F — Path parity

| | |
|---|---|
| Quantities compared | **34** |
| Matches | **34** |
| Mismatches | **0** |

Compared at record population, state count, admissible-set, attribution and aggregate level — `09_original_vs_independent_parity.csv`.

**One discrepancy arose, and it was mine (B-01).** My first Path B applied the daylight mask to all hours, giving n = 21,754 and 9.612% against Path A's n = 5,536 and 9.59%. Reading `threshold_sensitivity.py:120` settled it: `m2 = m.values & dl_mask` ANDs the daylight mask with the departure-window mask. **The original was correct and my independent implementation was wrong.** Fixed; both paths now agree. It is recorded because it is the one defect the two-path design actually caught, which is the evidence that the design works rather than merely duplicating a single code path.

---

## 8. Table G — Scope and limitations

| Limitation | Status |
|---|---|
| **Constructed identity** | Every headline is an identity, not a measured effect. Δ_L2 is invariant to the content of `RESTRICTED` (B-04) |
| **Departure advice preserved** | `RESTRICTED` keeps both `Go` and `Delay`; only `DepartureTime` and `Duration` are removed, so the departure recommendation never changes |
| **No proposal generator** | No recommendation was ever actually withheld; divergence ≠ AI proposal exclusion (B-05) |
| **Warning assumption** | No marine-warning column exists; `g_m` pinned SAFE; all states are lower bounds (D-05) |
| **Hindsight input** | `decision_time_availability` UNKNOWN for 100% of records (D-08) — permanent |
| **Vessel threshold transfer** | 1.0/1.25 m sourced from vessel length, applied to tonnage; researcher assumption, not certified (A-03) |
| **Resolution / co-location confounding** | Two factors change together (D-12, B-07) |
| **Temporal correlation** | 9,135 window hours are not 9,135 independent cases; no IID interval or significance test applied (B-08) |
| **Time granularity** | `g_t` judges an hourly bucket at its start instant; the daylight-only denominator depends on this directly (A-10) |
| **Component concentration** | 518 of 531 PRIMARY CAUTION hours are wave-bound; only three of five components can contribute CAUTION at all (B-06) |

All figures in this report are **exact retrospective frequencies over an archived period**. They are not causal effects, not population safety guarantees, and carry no sampling error to interval-estimate.

**Nothing here supports a claim about** maritime safety improvement, actual departure decisions, injury prevention, user benefit, algorithmic novelty, or a causal wave-resolution effect.

---

## 9. Table H — Step 5 decision

### Gate: **GO**

Reproduction is complete and exact by two independent paths. No indispensable data, code or rule configuration is missing or unsafe to access. Originals are untouched.

**Remaining blockers: none for Step 5 execution.**

**Permanent claim-blockers, carried unchanged:**

1. **D-08** — no operational-availability statement is possible, ever, from these inputs.
2. **D-12 / B-07** — no PRIMARY/RESOLUTION difference may be attributed to resolution alone.
3. **B-04 / B-05** — the headlines are identities, and there is no proposal generator, so no policy-performance or withholding claim is available.

**Reporting conditions for Step 5:** state each headline with the identity that produces it; label the envelope small-vessel; state the `g_t` granularity; report the two-effect decomposition rather than a single gap; keep `g_m` and the length-to-tonnage transfer explicit as assumptions.

---

## 10. Acceptance checks

| Check | Result |
|---|---|
| Originals byte-identical before/after | **PASS** — 9 artefacts hashed; `git diff HEAD --diff-filter=MD` empty |
| `prediction-register.csv` unchanged | **PASS** — hash unchanged; log confirms "Register NOT written" |
| No remote access, no install, no commit | **PASS** |
| All numerators, denominators and percentages recomputed from records | **PASS** — integers compared before percentages throughout |
| No threshold, filter, unit or rounding changed to match a target | **PASS** — the only correction was to my own Path B defect (B-01) |
| No manuscript percentage hard-coded as a computed output | **PASS** — targets held in a separate comparison dict only |
| Two paths compared, differences not hidden behind rounding | **PASS** — 34/34, and the one discrepancy is documented in full |
| All failed or unmatched values reported honestly | **PASS** — none failed; B-01 reported although it was audit-side |
| EXACT not claimed on rounded percentages alone | **PASS** — every identity verified at integer-numerator level |
| Stopped after Step 4 | **PASS** |
