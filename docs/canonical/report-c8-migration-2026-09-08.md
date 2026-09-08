# Report: SDR-001 Execution Condition C-8 — Canonical Migration

**Date:** 2026-09-08
**Final status:** **SDR-001 APPLIED — MODEL B CANONICAL**
**Scope:** Complete canonical migration. Not partial.

---

# RESULT

# **C-8 CLOSED — SDR-001 APPLIED — MODEL B CANONICAL**

All twenty closure criteria satisfied. No stop condition fired.

> **One material issue arose mid-migration and was diagnosed rather than forced.** The migrated `hysteresis_analysis.py` first produced P09 = 3,698 against C-6's 3,661. **The canonical `g_t` was not at fault** — three scripts still read the **v1 land-cell** data F-10 condemned. Migrating their data source to v2 sea-cell produced exact reproduction. Had that been waved through, the canonical prediction outcomes would have come from the wrong grid cell.

---

## 1. Pre-migration integrity anchors

Recorded before any edit — `data/c8/pre-migration-anchors.txt`.

| Item | Pre-migration state |
|---|---|
| Prediction register | `d95cf81f19341c3c…` · 24 entries · **22 CONFIRMED / 2 REFUTED** |
| Appendix C | `7681261ea5f48ea0…` |
| 8 canonical scripts | `5af9eaf7…` `1f0f4e9c…` `69bc2bd6…` `73015d88…` `dd6a6c3f…` `8e977c90…` `d051cac4…` `7e799b5f…` |
| C-3 solar artefact | `057c46a19d0e8ea7…` |
| C-5 metrics | `3566cd6b1aab6cd3…` |
| C-6 re-resolution | `46474a320e11502c…` |
| Empirical findings | `dd29cddb3fe82d45…` |
| Conference manuscript | `ffc366c1d9d889bf…` |
| Journal 1 manuscript | `b917df033b8d53a8…` |
| Canonical `g_t` | Incumbent fixed clock — 3 rows present in Appendix C ✅ |
| Headline figures | **7.72% / 5.98%** ✅ |

**All anchors reproduced. Migration proceeded.**

---

## 2. Shared canonical `g_t` implementation

**`scripts/canonical_gt.py`** — sha256 `b330bf9f94e848aa…`

```
g_t : ([0,24) × Date) ∪ {⊥} → {SAFE, UNSAFE}
      SAFE    sunrise(date) ≤ t < sunset(date)
      UNSAFE  t < sunrise(date) or t ≥ sunset(date)
      UNSAFE  t = ⊥   (missing/invalid clock, date or solar lookup)
```

**Half-open by construction — exact sunrise SAFE, exact sunset UNSAFE.** `Im(g_t) = {SAFE, UNSAFE}`; **no CAUTION**, deliberately. Classification reads `sunrise_hours` / `sunset_hours` (float, 6 dp), never the HH:MM:SS display columns.

Also exports **`is_daylight()`** — the canonical astronomical daylight predicate — and **`g_t_incumbent_superseded()`**, retained for historical reproduction only.

---

## 3. Solar dependency

> **stored solar artefact → `g_t` → `f`**

| | |
|---|---|
| Artefact | `data/solar/solar-events-daily.csv` · **`057c46a19d0e8ea7…` (unchanged)** |
| Specification | `solar-spec-v1` |
| Implementation | `solar-v1` (`solar.py` `3b7dc371…`, **unchanged**) |
| Location | **5.98° N, 116.01° E**, UTC+8, no DST |

**No canonical script computes solar astronomy.** Eight scripts, one implementation, one frozen table.

---

## 4. Appendix C change

The `g_t` table now defines the solar-event classifier with its type, the half-open rule, the `⊥` fail-safe row, the COLREGs Rule 20(b) boundary attribution, and a pointer to `canonical_gt.py`.

**The superseded classifier is recorded, not deleted:** a marked block states the fixed clock 06:00 / 17:00 / 19:00 was superseded 2026-09-08, that its boundaries had no located source, that SAFE began before sunrise every day of the year, and that the 17:00–19:00 CAUTION band is **withdrawn, not relocated**. **Both classifiers are never presented as simultaneously canonical.**

The C-4 heading *"approved replacement design, pending canonical migration"* now reads *"canonical time classifier following SDR-001 application"*. **The C-4 non-surjectivity statement is preserved verbatim.** An evidence/policy block was added at the classifier itself.

---

## 5. Script migrations — 8 of 8

| # | Script | Change | sha256 |
|---|---|---|---|
| 1 | `canonical_figures.py` | `g_t` + daylight window → canonical | `cb4f1ee26ab36f85…` |
| 2 | `condition_comparison.py` | `g_t` → canonical; write guarded | `3c32913a2a9cc85f…` |
| 3 | `diagnostic_binding.py` | `g_t` + daylight + **data source → v2**; write guarded | `113b5b92e81535a9…` |
| 4 | `hysteresis_analysis.py` | `g_t` + **data source → v2**; write guarded | `a58af0133acdf4f8…` |
| 5 | `historical_replay.py` | `g_t` + daylight + **data source → v2**; old `g_t` now raises | `3b1105b7cc03839b…` |
| 6 | `compare_v1_v2.py` | `g_t` → canonical; write guarded | `5d69dfa951fe455a…` |
| 7 | `threshold_decision.py` | `g_t` + daylight window → canonical | `ef30ad3f8df7eba9…` |
| 8 | `threshold_comparison.py` | daylight window → canonical | `daed570596df1dbf…` |

**Verified:** all 8 import `canonical_gt`; **zero** incumbent fixed-clock expressions remain in any script except the explicitly-labelled `g_t_incumbent_superseded`; all 8 execute with exit code 0. Pre-migration copies preserved in `data/c8/pre-migration-scripts/`.

### 5.1 The data-source finding

`hysteresis_analysis.py`, `diagnostic_binding.py` and `historical_replay.py` still read `raw_weather.csv` / `raw_marine.csv` / `raw_rainfall.csv` — the **land cell F-10 condemned**. With Model B applied but the land cell retained, `hysteresis_analysis.py` produced **P09 = 3,698 / P10 = 258 / P11 = 45 / P12 = 8.9** — a fourth configuration matching nothing.

**Diagnosed, not forced.** All three now default to **v2 sea-cell** (`raw_weather_sea.csv` + `raw_marine_era5_sea.csv`, precipitation from the sea-cell weather file). The v1 files remain reachable behind **`--v1-historical`** for reproducing pre-migration findings.

---

## 6. Register-write safety

C-5 and C-7 found four scripts calling `reg.to_csv()` unconditionally. **All four are now opt-in:**

```python
def _register_write_enabled():
    return ("--write-register" in sys.argv
            or os.environ.get("ALLOW_REGISTER_WRITE") == "1")
```

Default output: *"Register NOT written (read-only default; pass --write-register to enable)."* The `_register_guard` immutability check is retained. A misleading leftover print in `diagnostic_binding.py` that announced a write which never happened was removed.

**Verified:** every run during this migration left the register untouched until the deliberate promotion step.

---

## 7–8. Regenerated canonical results

**Emerged from the migrated canonical scripts. Not hard-coded.**

| | PRIMARY (5.00 yr, ERA5-Ocean 50 km) | RESOLUTION (3.25 yr, MFWAM 8 km) |
|---|---|---|
| **Level 2 binding rate** | **5.81%** | **4.48%** |

These match the C-5/C-6 candidate values exactly, computed independently by the canonical pipeline.

---

## 9. Full canonical comparison table

| Metric | Previous canonical | **New canonical** | Delta | Attribution |
|---|---|---|---|---|
| **Level 2 binding, PRIMARY** | 7.72% | **5.81%** | −1.91 pp | `g_t` |
| **Level 2 binding, RESOLUTION** | 5.98% | **4.48%** | −1.50 pp | `g_t` |
| Daylight UNSAFE hours, PRIMARY | 1,170 | **1,262** | +92 | `g_t` **+ daylight redefinition** |
| Daylight UNSAFE hours, RESOLUTION | 409 | **455** | +46 | `g_t` **+ daylight redefinition** |
| Weather-driven share of UNSAFE | 11.8% / 7.0% | **10.9% / 6.4%** | −0.9 / −0.6 pp | `g_t` |
| Small vs big differ (departure) | 12.16% / 7.94% | **9.11% / 5.86%** | −3.05 / −2.08 pp | `g_t` |
| `g_o` share of daylight CAUTION | 98.66% / 97.41% | **98.71% / 97.66%** | +0.05 / +0.25 pp | `g_t` + redefinition |
| `g_t` share of all-hours non-SAFE | 87.63% / 91.10% | **86.82% / 90.19%** | −0.81 / −0.91 pp | `g_t` |
| `g_r` share of daylight CAUTION | 1.55% / 2.99% | **1.48% / 2.70%** | −0.07 / −0.29 pp | `g_t` + redefinition |
| **`g_t` share of daylight CAUTION** | 0% | **0% — emits no CAUTION** | — | structural |
| `g_w`, `g_m` ever bind | 0% | **0%** | 0 | unchanged |
| Max sustained wind | 21.8 / 21.7 kn | **21.8 / 21.7 kn** | 0 | unaffected |
| Max wave height | 2.60 / 1.84 m | **2.60 / 1.84 m** | 0 | unaffected |
| **C3 vs C1 divergence** | 0.00% | **0.00%** | **0** | **structurally invariant** |
| C0 vs C1 (Level 1) | 24.64% | **42.88%** | +18.24 pp | `g_t` — UNSAFE enlarged |
| C0 vs C2 (Levels 1+2) | 32.36% | **48.69%** | +16.33 pp | `g_t` |
| Total transitions | 5,201 | **3,661** | −1,540 | `g_t` |
| Non-scheduled transitions | 207 | **222** | +15 | `g_t` |
| Oscillations | 27 | **26** | −1 | `g_t` |
| Hysteresis reduction | 8.70% | **10.36%** | +1.66 pp | `g_t` |
| **Direct SAFE→UNSAFE transitions** | **2** | **1,536** | **+1,534** | **`g_t` — the accepted cost** |
| **`g_t`-driven SAFE→CAUTION** | **1,545** | **0** | **−1,545** | **`g_t` — by construction** |

Full output: `data/c8/canonical-results-post-migration.txt`.

---

## 10. C-6 reproduction check

**Every script-resolved prediction reproduces the C-6 candidate exactly.**

| | C-6 candidate | Migrated canonical | Match |
|---|---|---|---|
| **P09** | 3,661 | **3,661** | ✅ |
| **P10** | 222 | **222** | ✅ |
| **P11** | 26 | **26** | ✅ |
| **P12** | 10.36% | **10.36%** | ✅ |
| P13 | non-sched 222, osc 26 | **222 / 26** | ✅ |
| P05 / P06 / P07 / P08 | 98.53 / 0.83 / 86.82 / 3 | **98.7 / 1.2 / 86.8 / 3.0** | ✅ |
| P21 / P22 / P23 / P24 | 0.00 / 4.48 / 45.56 / 41.08 | **0.00 / 4.48 / 45.56 / 41.08** | ✅ |

**No material disagreement. No implementation drift.** The one apparent disagreement was the data-source issue of §5.1, diagnosed and corrected before promotion.

---

## 11–13. Prediction outcome migration

**Promoted by `scripts/c8/promote_register.py` after reproduction succeeded**, with a guard that aborts unless all of `id`, `registered`, `analysis`, `scope`, `metric`, `pred_type`, `pred_lo`, `pred_hi`, `pred_stated`, `rationale` are byte-identical **and** each promoted row's previous actual survives in `notes`. **The guard passed.** Backup: `data/c8/prediction-register.pre-c8.csv` (`d95cf81f…`).

**20 rows promoted · 4 unaffected · 7 status flips.**

### Final count — computed from the rows, not asserted

> ## **15 CONFIRMED / 9 REFUTED** *(was 22 / 2)*

### The seven flips, attribution preserved

| | Prediction | Previous | New | Attributable to SDR-001? |
|---|---|---|---|---|
| 1 | **P20** | 409 CONFIRMED | 1,529 REFUTED | ✅ **Yes** |
| 2 | **P23** | 28.19 CONFIRMED | 45.56 REFUTED | ✅ **Yes** |
| 3 | **P24** | 22.21 CONFIRMED | 41.08 REFUTED | ✅ **Yes** |
| 4 | **P04** | 12.4 CONFIRMED | 5.81 REFUTED | ❌ **No** — already REFUTED under the incumbent (7.72 vs band 12.0–12.8) |
| 5 | **P09** | 5,416 CONFIRMED | 3,661 REFUTED | ❌ **No** — already REFUTED (5,201 vs floor 5,400) |
| 6 | **P18** | 8.32 CONFIRMED | 4.48 REFUTED | ❌ **No** — already REFUTED (5.98 vs band 8–12) |
| 7 | **P19** | 6.1 CONFIRMED | 4.48 REFUTED | ❌ **No** — already REFUTED (5.98 vs band 6.0–6.2) |

> **Only three of the seven are consequences of Model B.** Four had already left their bands under the incumbent classifier at the current configuration, by the threshold and data corrections that predate this decision. **Describing all seven as Model B's doing would undo C-6's central finding**, and the attribution is carried in every promoted row's notes.

**P09's four-stage decomposition is preserved in its notes:** 5,416 —(threshold −196)→ 5,220 —(data −19)→ 5,201 —(`g_t` −1,540)→ 3,661.

---

## 14. P20 terminology migration

**Handled as a definition migration, not a recomputation.**

| | |
|---|---|
| **Canonical actual** | **1,529** — computed in the prediction's **registered** 06:00–17:00 scope, so the original prediction is answered as asked |
| **Under astronomical daylight** | **455** (RESOLUTION) — the same phenomenon under the new definition |

The register note states this explicitly: *"the canonical architecture now defines daylight astronomically (sunrise ≤ t < sunset); under that definition the RESOLUTION daylight-UNSAFE count is 455, not 1529. Same phenomenon, two definitions — not one quantity measured twice."*

**The rule applied throughout:** historical prediction re-resolution retains the original scope; **all future prose and new analysis use astronomical daylight**. `canonical_gt.is_daylight()` is the single implementation, and §0a's row is relabelled "Daylight UNSAFE hours (sunrise–sunset)".

---

## 15. P21 invariant verification

**Recomputed under the canonical pipeline: 0.00% under both configurations.**

`condition_comparison.py` defines C1 and C3 as the identical admissible-set map, so their divergence is 0 for **any** classifier. **P21 CONFIRMED, unchanged.** The F-15 result answering Review 3's novelty objection is untouched by the migration — the single most reviewer-facing empirical claim in the project survives a change to its most load-bearing component.

---

## 16. SC-10 resolution

**Redesigned to trigger CAUTION through an environmental component**, with the rationale recorded in `evaluation-design-rq4.md`.

| | Before | **After** |
|---|---|---|
| SC-10 | 0.5 m, 18:00 → CAUTION via `g_t` | **1.6 m, 10:00 → CAUTION via `g_o`** (1.5–3.5 m band, big vessel) |
| SC-15 | 0.5 m, 22:00 → UNSAFE | **0.5 m, 2024-03-20 22:00** → UNSAFE (t ≥ sunset 18:27 that date) |

**Options rejected, and why:** keeping 18:00 with an explicit date would still yield SAFE or UNSAFE — never CAUTION — so Category B would lose a member; **inventing a twilight CAUTION band was rejected outright**, since that is the very thing SDR-001 rests on not existing.

**Time policy is still tested** — SC-15 now carries an explicit date so its boundary comes from the stored artefact rather than an assumed clock hour.

---

## 17. Conference manuscript propagation

`manuscript-v3.md` — 16 targeted substitutions plus a rewritten Threats to Validity paragraph and conclusion:

Algorithm 1 `g_t` line → `g_t(t, date)`; abstract and Results 1–6 figures → 5.81% / 4.48%; daylight UNSAFE → 1,262 / 455 with the astronomical definition stated; vessel conditioning → 9.11% / 5.86%; TABLE VI binding shares → 98.71% / 86.82% with `g_t` marked as emitting no CAUTION; TABLE VII divergence matrix → 42.88 / 48.69 / 5.81; resolution spread → 1.3 points.

**Threats to Validity updated from counterfactual to canonical tense** — the step is now *"1,536, against 2 under the fixed-clock classifier this replaced"*, stated as an observed property. **The tension is not removed.** The paragraph still opens by naming it, and now adds that the governance rule is a **policy** choice which no source establishes.

**Conclusion updated**, including the prediction sentence: *"fifteen of twenty-four are confirmed and nine refuted. Of the seven outcomes that changed, three follow from the time-classifier decision and four had already been refuted by earlier threshold and data corrections."*

---

## 18. Journal 1 propagation

Active working manuscript updated: the `g_t` specification row → solar-event two-state with the COLREGs attribution; the stale F-6 figures **5,416 / 70 / 6.2%** → **3,661 / 26 / 10.36%**; a migration banner added at the head.

**Submitted and archived versions are historical and were not edited** — the banner says so.

---

## 19. Empirical findings propagation

§0a regenerated from the migrated `canonical_figures.py`. A dated header records the previous canonical figures **as provenance**: *"Level 2 binding 7.72% / 5.98%; daylight UNSAFE 1,170 / 409; …"* — **discoverable, not deleted, and no longer presented as current.** The grid-resolution spread updated 1.7 → **1.3 points**. A new row records `g_t`'s daylight-CAUTION share as **0% — emits no CAUTION**.

---

## 20. Threats to Validity update

Covered in §17. Tense moved from *approved design / counterfactual sensitivity* to *canonical classifier / observed result*; the disclosure obligation from C-4 is retained in full; the evidence/policy separation is now stated inside the threat itself.

---

## 21. Active-document terminology sweep

| Document | Change |
|---|---|
| `explainer-per-component-classification-functions.md` | `g_t` signature, "Dusk (CAUTION)" removed, worked example |
| `dataset-label-derivation.md` | Label rows; 17:00–19:00 CAUTION row struck as withdrawn |
| `safety-state-design.md` | Threshold row |
| `data-source-met-malaysia.md` | Threshold row + COLREGs attribution |
| `architecture-illustration.md` | Threshold row; **scenario times now carry explicit dates** (05:30 / 16:30 / 18:30 on 2024-03-20 with their solar boundaries) |
| `evaluation-design-rq4.md` | Threshold row; SC-10 / SC-15 |
| `formal-model.md` | Three-zone text → two zones, with the policy caveat |
| `journal-1/section-5-plan.md` | Threshold row |
| `CLAUDE.md` | `g_t` block rewritten; threshold table; F-6 figures; documents map; recomputation-rule note |
| `decision-record-empirical-first.md`, `finding-bottom-semantics.md`, `finding-met-lower-boundary-gap.md` | Provenance labels on quoted 7.72% |

Each edited document carries a dated SDR-001 banner. **"Daylight" now means sunrise ≤ t < sunset in all active canonical prose**, and every fixed-window occurrence is either migrated or explicitly marked as a historical prediction scope.

**Active twilight-CAUTION language removed.** The 17:00–19:00 band survives only inside superseded-specification blocks and historical records.

---

## 22. Historical documents preserved

**Nothing historical was rewritten to look as though Model B was always canonical.**

Untouched or annotation-only: `session-log-2026-09-06.md` · `finding-gt-provenance-audit.md` · `finding-gt-operational-semantics.md` · `finding-gt-sensitivity-analysis.md` · `finding-unsafe-semantics-audit.md` · `finding-sdr-001-readiness-audit.md` · all `cleanup-report-*`, `approval-report-*` and `report-c*` documents · archived and submitted manuscript versions · `docs/obsolete/`.

Preserved artefacts: `data/c8/pre-migration-anchors.txt` · `data/c8/pre-migration-scripts/` (all 8 originals) · `data/c8/prediction-register.pre-c8.csv` · `data/c6/prediction-register.pre-c6.csv` · C-3/C-5/C-6/C-7 artefacts **all unchanged by hash**.

---

## 23. Prediction register before / after

| | |
|---|---|
| **BEFORE** | `d95cf81f19341c3c14f136070473bbf56ffa1928458d164fbd4bbf85bed218ce` |
| **AFTER** | `5574b88ea65168b6ef5e308629f3eb14fb70f8688a592fde279103ea4b37eae6` |
| Backup of BEFORE | `data/c8/prediction-register.pre-c8.csv` — `d95cf81f…` ✅ |

**24 entries · 15 CONFIRMED / 9 REFUTED · original texts and bands byte-identical · previous actuals and statuses preserved in notes.**

---

## 24. Canonical artefact hashes

| Artefact | sha256 |
|---|---|
| `scripts/canonical_gt.py` | `b330bf9f94e848aa…` |
| `data/solar/solar-events-daily.csv` | `057c46a19d0e8ea7…` **(unchanged)** |
| `data/solar/usno-validation-2026-09-08.csv` | `da14a8dca224ae18…` **(unchanged)** |
| `scripts/sensitivity/solar.py` | `3b7dc371ebe5931b…` **(unchanged)** |
| `data/prediction-register.csv` | `5574b88ea65168b6…` |
| `docs/canonical/appendix-c-formalisation.md` | `0d8a1d8ae56a4ec1…` |
| `docs/canonical/empirical-findings-2026-09-06.md` | `667161e288d5e403…` |
| `data/c8/canonical-results-post-migration.txt` | 392-line full output |

---

## 25. Theorem and invariant verification

**Every invariant verified present and unchanged in Appendix C:**

| Invariant | Status |
|---|---|
| `𝒮 = {SAFE, CAUTION, UNSAFE}` | ✅ Unchanged |
| Severity ordering `UNSAFE ≻ CAUTION ≻ SAFE` | ✅ Unchanged |
| Max-severity aggregation | ✅ Unchanged |
| `G(S)` · `A_AI(S)` · containment | ✅ Unchanged |
| **Theorem C.1** (ideal totality) | ✅ Unchanged — two intervals partition `[0,24)` exhaustively per date |
| **Theorem C.1b** (operational totality) | ✅ Unchanged |
| **Corollary C.1b.1** (fail-safe) | ✅ Unchanged — `g_t(⊥) = UNSAFE` implemented |
| **Lemma C.1c** | ✅ Unchanged |
| **Theorem C.2** (monotonicity) | ✅ Unchanged |
| **Theorem C.3** (Safety Dominance) | ✅ Unchanged |
| **(D1) `t ∉ D`** | ✅ Unchanged |
| Human override unconditional | ✅ Unchanged |
| **`cause`** | ✅ **Unchanged** — the night→`hazard` mismatch remains a separate future issue, deliberately not touched |
| C.9.6 notification separation | ✅ Unchanged — no twilight CAUTION, no warning interval invented |

**No theorem required rewriting.** Only the canonical classifier reference changed.

---

## 26. Files created / modified

**Created (5):** `scripts/canonical_gt.py` · `scripts/c8/promote_register.py` · `data/c8/pre-migration-anchors.txt` · `data/c8/canonical-results-post-migration.txt` · `data/c8/prediction-register.pre-c8.csv` · plus `data/c8/pre-migration-scripts/` (8 originals) and this report.

**Modified — scripts (8):** all canonical script sites.
**Modified — documents (13):** `appendix-c-formalisation.md` · `empirical-findings-2026-09-06.md` · `architecture-illustration.md` · `evaluation-design-rq4.md` · `finding-gt-evidence-closure.md` · `decision-record-empirical-first.md` · `finding-bottom-semantics.md` · `finding-met-lower-boundary-gap.md` · `explainer-per-component-classification-functions.md` · `dataset-label-derivation.md` · `data-source-met-malaysia.md` · `safety-state-design.md` · `formal-model.md` · `CLAUDE.md`.
**Modified — publications (3):** `manuscript-v3.md` · Journal 1 active manuscript · `journal-1/section-5-plan.md`.
**Modified — data (1):** `data/prediction-register.csv`.

---

## 27. Repository stale-value sweep

| Pattern | Result |
|---|---|
| `06:00` / `17:00` / `19:00` / `17:00–19:00` in **active code** | ✅ **Zero** outside `g_t_incumbent_superseded` |
| `7.72` / `5.98` in active docs | ✅ All occurrences are **labelled provenance** or inside historical records |
| `5.81` / `4.48` | ✅ **Current canonical** |
| `5416` / `5220` / `70` / `6.17` / `6.2%` | ✅ **Historical / provenance-labelled** |
| `daylight` / `dusk` / `twilight` | ✅ Active prose = astronomical; twilight only in superseded blocks |
| `approved replacement` / `NOT YET CANONICAL` / `NOT YET APPLIED` | ✅ **Zero active occurrences** |

**No unexplained stale active hit remains.** Every occurrence is classified as current canonical, historical, archived, or explicitly provenance-labelled.

---

## 28–29. Final condition and SDR status

| | Condition | Status |
|---|---|---|
| **C-0** | Solar algorithm provenance | ✅ CLOSED |
| **C-1** | Pin solar implementation | ✅ CLOSED |
| **C-2** | 28-row USNO validation artefact | ✅ CLOSED |
| **C-3** | Daily solar-event artefact | ✅ CLOSED |
| **C-4** | Design consequences documented | ✅ CLOSED |
| **C-5** | Three-stage hysteretic isolation | ✅ CLOSED |
| **C-6** | Prediction re-resolution | ✅ CLOSED |
| **C-7** | Baseline reconciliation | ✅ CLOSED |
| **C-8** | Canonical migration | ✅ **CLOSED** |

> # **SDR-001 — APPLIED, MODEL B CANONICAL** *(2026-09-08)*

**No stop condition fired.** All 8 script sites migrated; C-6 evidence reproduced; register history preserved; manuscripts and formal model agree; "daylight" unambiguous; P20 definition migration explicit; no unqualified 17:00–19:00 CAUTION survives; canonical figures match frozen candidate evidence; no invariant changed.

---

## 30. Remaining out-of-scope issues

| Issue | Status |
|---|---|
| **`cause` night→`hazard` mismatch** | **OPEN, deliberately.** A `g_t`-driven UNSAFE at night is labelled `hazard` when nothing hazardous was detected. Provenance-only, no theorem affected, pre-existing. Separate workstream |
| **Solar publication reference** | **OPEN.** The formulation is hash-pinned and reproducible but not yet citable to a specific publication (C-1 §8) |
| **Anticipatory sunset notification** | **OPEN, future work.** C.9.6 forbids a twilight CAUTION band or an invented warning interval |
| `ageᵢ` freshness parameters | Unspecified — pre-existing |
| Layer 3 rule engine (Q8) | Unimplemented — pre-existing |
| Docstring attributions in `solar.py` / `gt_counterfactual.py` | Imprecise, recorded at C-0 |

---

## 31. Assessment

**The migration's most useful moment was the one where it nearly went wrong.**

`hysteresis_analysis.py` produced P09 = 3,698 against C-6's 3,661 — a 1% discrepancy, easily rationalised as rounding or a harmless implementation difference. It was neither. Three scripts were still reading the land-cell data F-10 condemned, and had that passed, **the canonical prediction outcomes would have been computed from the wrong grid cell** while every surrounding document asserted they came from the right one. The C-6 frozen evidence is what caught it, which is the entire reason C-5 and C-6 produced frozen evidence in the first place.

**The result is one canonical specification, and it can be shown rather than asserted:** one implementation of `g_t`, one frozen solar table, eight scripts importing the same module, zero fixed-clock expressions outside an explicitly superseded function.

**Three things were deliberately not smoothed.** The 2 → 1,536 step is now an observed canonical property, disclosed in Threats to Validity with its tension intact. The register lost seven confirmations, and the record keeps saying that only three of them are SDR-001's doing. And the governance rule — *night ⇒ AI advisory unavailable* — remains labelled a policy choice that no source establishes, in the formal model, in the manuscript, and in the module docstring.

**What the project gains is smaller than the headline drop suggests.** 7.72% → 5.81% looks like a loss; what it buys is a time classifier whose boundary comes from a binding international regulation and a version-pinned ephemeris, rather than three numbers nobody could source.

---

# **C-8 CLOSED — SDR-001 APPLIED — MODEL B CANONICAL**
