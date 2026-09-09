# Appendix C Rainfall Signature Synchronisation Report

**Date:** 2026-09-09
**Role:** formal-specification maintainer and provenance auditor
**Type:** formal specification repair — **not** a scientific model change
**Appendix C:** `03e80802a46404df` → **`1ce268154807bd70`**
**Manuscript:** `27b33b846ae327cb` — **unchanged**

---

## 1. Scope

Synchronise canonical Appendix C with the rainfall classifier the canonical implementation already executes. Bounded to `appendix-c-formalisation.md` plus evidence artefacts. No classifier behaviour, threshold or empirical output changed.

## 2. Trigger for repair

The Full Conference Reviewer Audit (closed, same day) retyped the manuscript's rainfall classifier as consuming a rate together with a thunderstorm indicator, and recorded that Appendix C still carried the older scalar form. `repository-drift.csv` logged it as a canonical item requiring its own bounded repair. This is that repair.

## 3. Before-state hashes

23 protected artefacts hashed into `integrity-before.json`, including Appendix C, the manuscript, the prediction register, all canonical scripts, the frozen solar artefacts, the three environmental datasets and the C5–C8 evidence.

## 4. Appendix C incumbent formulation

`appendix-c-formalisation.md` declared, at the C.2 rainfall block:

```
g_r : ℝ≥0 → {SAFE, CAUTION, UNSAFE}
*Domain:* r ∈ ℝ≥0. The three intervals … partition ℝ≥0 exhaustively with no overlap.
```

while a prose block eleven lines later asserted that WMO codes 95/96/99 "also yield UNSAFE where present" and that "this route is **formally part of the specification**". The type table gave `X_r = ℝ≥0`, and Theorem C.1(i) proved totality over the rate axis alone. **The document simultaneously claimed the route was formal and provided no formal object to carry it.**

## 5. Canonical implementation inspected

Nine scripts evaluate rainfall. **All nine implement a two-input classifier with identical semantics:**

| File | Form |
|---|---|
| `canonical_figures.py:127` | `(precip > R_UNSAFE) \| wmo.isin([95,96,99])` |
| `condition_comparison.py:161` | same |
| `diagnostic_binding.py:101` | same |
| `hysteresis_analysis.py:111,122` | same; storm tested **before** hysteresis |
| `historical_replay.py:79-94` | `def g_r(precip_mm_hr, wmo_code)` |
| `compare_v1_v2.py:44` | `np.isin(c,[95,96,99])` |
| `threshold_decision.py:63` | same |
| `c5/three_stage_hysteresis.py:146,156,262` | same; storm overrides hysteresis |
| `c6/reresolve_predictions.py:124` | same |

`R_CAUTION = 10.0` and `R_UNSAFE = 20.0` in every file. Full table: `gr-implementation-audit.csv`.

**The specification was wrong, not the code.** The repair therefore follows the standing C-0 rule: evidence follows implementation.

## 6. Raw WMO-code semantics

The provider supplies a raw present-weather code `c` alongside the rate. `c` is **not** the classifier input. Codes actually present in the canonical record: 0, 1, 2, 3, 51, 53, 55, 61, 63, 65. The storm set is exactly **{95, 96, 99}**, taken from the implementation and from no other source. No code was invented, and no meteorological content beyond "thunderstorm present" is relied upon.

## 7. Definition of κ

```
χ : C_WMO ∪ {absent} → K = {0, 1}
χ(c) = 1  if c ∈ {95, 96, 99}
     = 0  otherwise, including c absent or unrecognised
```

Added as **C.2.0.4a**. κ = χ(c) is a *derived* indicator; the distinction between raw code and derived indicator is now explicit, as required.

## 8. Missing/invalid κ resolution semantics

This was the stop-condition-bearing question, and it was decided from the implementation, not from the manuscript's wording.

**Verified behaviour.** All three code paths in use return False for a missing code — `pandas .isin(NaN)`, `numpy np.isin(NaN)`, and Python `NaN in (95,96,99)` — so κ = 0. Independently, **`wmo` is excluded from every `dropna(subset=…)` while `precip` is included in every one**: a missing rate drops the record, a missing code does not. That 9-for-9 asymmetry is consistent and structural, not incidental.

**Classification: category C** — *a derived feature whose absence deterministically defaults to 0*. Not category A (required observation), because its absence never faults; not B, because it is derived rather than supplementary input; not D.

**The stop condition did not trigger**, because the executable semantics are unambiguous and uniform. But the honest qualification is recorded in C.2.0.4a rather than smoothed away: **defaulting an unavailable code to 0 is fail-*open* for that disjunct, not fail-safe.** It is the opposite of the rule applied to a required coordinate. No source justifies it; it is what the implementation does. The consequence travels with every figure — where the code feed is absent or incomplete, `g_r` results are lower bounds — and a deployment with an unreliable feed is directed to treat this as an open specification item rather than an inherited guarantee.

**It has never been exercised.** The raw code is present and recognised in all 43,848 hours, so the default branch of χ was itself never taken.

## 9. Revised `g_r` signature

```
g_r : ℝ≥0 × K → {SAFE, CAUTION, UNSAFE},  K = {0, 1}

               ⎧ UNSAFE   if κ = 1                      (storm route)
               ⎪ SAFE     if κ = 0 ∧ 0 ≤ r ≤ 10.0
   g_r(r, κ) = ⎨ CAUTION  if κ = 0 ∧ 10.0 < r ≤ 20.0
               ⎩ UNSAFE   if κ = 0 ∧ r > 20.0
```

Thresholds unchanged. A note records that the implementation's local variable `storm` denotes the *disjunction* `(r > 20.0) ∨ (κ = 1)`, not κ alone — κ is strictly the code-derived coordinate.

## 10. Revised valid-input domain

`X_r = ℝ≥0 × K` in the C.2.0.1 type table. This is the minimal change: `X_o = ℝ≥0 × ℝ≥0` was already a product, so the table needed no structural extension, and **`Y = ∏(Xᵢ ∪ {⊥})` absorbs it without amendment.**

## 11. Revised observation/resolution typing

C.2.0.2 previously carried one structured-component rule, for `o`. The rainfall pair is a *second and different* case and is stated as such rather than folded into the first: for `o` the second coordinate is not read, whereas for `r` it is. The rule added:

- **rate is the required coordinate** — ⊥ attaches to it under conditions A/B/C, and `g_r(⊥) = UNSAFE` via Corollary C.1b.1, unchanged;
- **κ is derived and never faults** — an unavailable code yields κ = 0, not ⊥.

## 12. Totality proof impact

Theorem C.1(i) now proves the `g_r` case in two exhaustive cases over κ: at κ = 1 the result is UNSAFE for every r; at κ = 0 the three rate intervals partition ℝ≥0. The former single-line claim that the rate partition exhausts the domain is explicitly retired.

## 13. Operational-totality impact

Theorem C.1b required **no structural change**. A note was added recording that `y_r = ⊥` denotes failure of the *rate* only, and that χ's totality into K means κ can never trigger the fail-safe. This preserves Corollary C.1b.1's scope exactly — it neither widens nor narrows it.

## 14. Monotone-degradation impact

Lemma C.1c concerns exclusion sets and is unaffected. A short **Observation C.1c.1** was added rather than a new theorem: `g_r(r,0) ⪯ g_r(r,1)` for all r, so κ is escalation-only and, since max-severity is monotone in each argument, an active indication can never reduce severity. Explicitly labelled a governance-classifier property, **not** a claim that thunderstorms are physically guaranteed unsafe.

## 15. Cause-taxonomy impact

**The `reasons` contract is unchanged.** An active κ already satisfies the existing **hazard** condition, since r is then a valid non-excluded environmental component at UNSAFE. No new reason category was created. One clause was added to the trace-retention bullet so the trace can record *which route applied* — a rate band or the κ = 1 storm route — with `hazard`'s bounded meaning restated.

## 16. Exclusion-set impact

**`D = {m}` unchanged.** C.2.0.4a states explicitly that κ is not and must not become a member of D: the unexercised storm route and the `g_m` archive gap are different phenomena, and conflating them would misstate both.

## 17. Empirical κ audit

`kappa-data-audit.json`, over `raw_weather_sea.csv` (canonical v2 sea cell):

| | |
|---|---|
| Total evaluated hours | **43,848** |
| κ = 0 | **43,848** |
| κ = 1 | **0** |
| Missing raw code | **0** |
| Invalid raw code | **0** |
| Distinct codes present | 0, 1, 2, 3, 51, 53, 55, 61, 63, 65 |
| Storm codes present | none |
| Missing precipitation | 0 · max rate 45.8 mm/hr · 21 hours > 20.0 · 113 hours > 10.0 |

The claim that the route is empirically inert is **confirmed**. Outcome C did not trigger.

## 18. Empirical invariance

Canonical generators re-run after the edits:

| | PRIMARY / RESOLUTION |
|---|---|
| Level 2 binds | **5.81% / 4.48%** ✓ |
| `g_o` daylight CAUTION | **98.71% / 97.66%** ✓ |
| `g_t` all-hours non-SAFE | **86.82% / 90.19%** ✓ |
| `g_r` daylight CAUTION | **1.48% / 2.70%** ✓ |
| `g_r` all-hours non-SAFE | **0.20% / 0.26%** ✓ |
| Daylight UNSAFE | 1,262 / 455 ✓ · weather-driven 10.9% / 6.4% ✓ · small vs big 9.11% / 5.86% ✓ |
| C0–C1 / C0–C2 / C3–C1 | 42.88% / 48.69% / 0.00% ✓ |
| Register | 24 · 15 CONFIRMED / 9 REFUTED · P09 3,661 · P20 1,529 ✓ |

Ten deterministic boundary cases plus the absent-code path were checked against the repaired Appendix C using the canonical implementation as oracle: **all PASS** (`verification.json`). Boundaries tested at 0, 10.0, 10.0+ε, 20.0, 20.0+ε and the record maximum 45.8, at both κ values.

## 19. Repository occurrence audit

16 loci classified in `gr-occurrence-audit.csv`: 1 CANONICAL (synchronised), 1 ACTIVE PUBLICATION (correct, untouched), 9 IMPLEMENTATION, 5 HISTORICAL preserved, 4 STALE deferred, 1 IRRELEVANT.

**Unrelated canonical drift found in passing and deliberately not fixed:** Theorem C.1's `g_t` case still lists the superseded fixed-clock intervals `[6,17), [17,19), [19,24) ∪ [0,6)`. This is a g_t item, not a rainfall item, and repairing it under a bounded rainfall task would be scope creep. Recorded for a separate bounded follow-up.

## 20. Files changed

`docs/canonical/appendix-c-formalisation.md` — eleven loci, all listed in `formal-change-map.csv`, every row carrying `semantic_change = NONE`.

## 21. Files intentionally not changed

The manuscript (verified correct — §19 of the task brief: **NO MANUSCRIPT EDIT**); all canonical scripts; the prediction register; frozen solar artefacts; C5–C8 evidence; the reviewer-audit report, which must continue to record that the defect existed; historical submissions and session logs; Journal 1; and the two known hygiene items (`CLAUDE.md` 98.66/97.41, `canonical_figures.py` trailer "22 kn"), which are out of scope and remain deferred.

## 22. Protected-state verification

23 artefacts re-hashed. **Changed: 1 — Appendix C. Unexpected changes: none.** `__pycache__` swept. Three CSVs parser-tested with both `csv.DictReader` and `pandas.read_csv`, with a strict field-count check: all PASS.

## 23. Stop-condition assessment

| Condition | Triggered? |
|---|---|
| **B** — κ resolution semantics require decision | **NO** — uniform across nine implementations and three language mechanisms; category C |
| **C** — κ empirical assumption refuted | **NO** — κ = 1 in 0 of 43,848 hours |
| **D** — implementation/specification conflict | **NO** — alignment achieved without touching executable behaviour |

## 24. Remaining repository drift

1. `CLAUDE.md` — 98.66 / 97.41 should be 98.71 / 97.66 *(deferred, out of scope)*
2. `canonical_figures.py` trailer — "22 kn" should be 21.6 kn *(deferred, prose only)*
3. `docs/justification/formal-model.md`, `docs/reference/explainer-per-component-classification-functions.md`, `docs/canonical/data-provenance.md` — scalar `g_r` *(newly recorded)*
4. Journal 1 manuscript and section-5 plan — scalar and superseded categorical `g_r` *(deferred; Journal 1 out of scope)*
5. **Appendix C Theorem C.1 `g_t` case — superseded fixed-clock intervals** *(newly identified, canonical, bounded follow-up)*

## 25. Final closure decision

All closure criteria pass. Appendix C no longer declares a scalar-only `g_r`; the product domain is correctly typed; rate thresholds are unchanged at 10.0 / 20.0; the storm route is explicitly typed rather than asserted in prose; totality covers both κ values; operational totality remains coherent with `⊥` semantics intact; `D = {m}` is unchanged; no new architecture state was introduced; the empirical state is bit-identical; and the manuscript is untouched and in agreement.

The specification now truthfully describes the classifier that generated the canonical evidence — which it did not before this repair.

---

*Artefacts:* `data/appendix-c-rainfall-sync/` — `integrity-before.json`, `integrity-after.json`, `gr-implementation-audit.csv`, `gr-occurrence-audit.csv`, `kappa-data-audit.json`, `formal-change-map.csv`, `verification.json`, `parser-test.json`, `closure.json`, `build.py`.
