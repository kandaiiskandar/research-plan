# Report: SDR-001 Execution Condition C-5 — Three-Stage Hysteretic Isolation

**Date:** 2026-09-08
**SDR-001:** **APPROVED — NOT YET APPLIED** · **Model B: SELECTED — NOT YET CANONICAL** · canonical `g_t` unchanged
**Scope:** C-5 only. No prediction re-resolved. Prediction register byte-for-byte unchanged. No canonical migration.

---

# RESULT

# **C-5 CLOSED — THREE-STAGE HYSTERETIC ISOLATION COMPLETE**

**The provenance gate passed exactly: Stage 1 reproduces P12 = 7.83.** All thirteen closure criteria satisfied.

**One material finding for C-7:** the registered **P09 = 5,416 is not reproducible** under the current specification, and the configuration that does produce it has been identified precisely. **P10, P11 and P12 all reproduce exactly.**

---

## 1. Stage 1 baseline reproduction

**Executed read-only.** `hysteresis_analysis.py` writes the register on every run (line 236, `reg.to_csv`), so **it was never executed**. Its functions were imported and reused unmodified by an isolated harness.

| | |
|---|---|
| **Input** | `raw_weather.csv`, `raw_marine.csv`, `raw_rainfall.csv` — v1 land cell, via `H.load()` verbatim, including its historical positional alignment |
| **Rows** | 43,848 |
| **Script reused** | `scripts/hysteresis_analysis.py` sha256 `73015d88…cefe` |
| **Hysteresis params** | `MARGIN = 0.10`, `LO = 1.0`, `HI = 1.25` |
| **Classifier thresholds** | `W 21.6/27.0`, `R 10.0/20.0`, `o_small 1.0/1.25` |
| **`g_t`** | Incumbent — `H.g_t_series()`, 06:00 / 17:00 / 19:00 |
| **Exclusions** | `D = {m}` — `g_m` pinned SAFE, absent from the max |

**Result: P12 = 7.83**

---

## 2. Authoritative P12 comparison — **GATE PASSED**

| | |
|---|---|
| **Authoritative (register)** | **7.83** |
| **Stage 1 computed** | **7.83** |
| **\|difference\|** | **0.0000** |

> ### **GATE: PASS.** The stale 6.17 was not used at any point.

### 2.1 Full Stage-1 register cross-check

| Prediction | Computed | Registered | Result |
|---|---|---|---|
| **P09** total transitions | **5,220** | **5,416** | ❌ **DIFFERS by 196** |
| **P10** non-scheduled | **230** | **230** | ✅ **MATCH** |
| **P11** oscillations | **37** | **37** | ✅ **MATCH** |
| **P12** reduction % | **7.83** | **7.83** | ✅ **MATCH** |

### 2.2 P09 diagnosed — a threshold-vintage mismatch, not a data effect

A read-only sweep over the two threshold amendments applied since P09 was resolved:

| `r` CAUTION | `o` small UNSAFE | Total transitions | |
|---|---|---|---|
| 10.0 (current) | 1.25 (current) | **5,220** | ← Stage 1 |
| 10.0 (current) | 1.9 (pre-amend) | 5,356 | |
| 7.5 (pre-amend) | 1.25 (current) | 5,280 | |
| **7.5 (pre-amend)** | **1.9 (pre-amend)** | **5,416** | ✅ **← the registered value** |

> **P09's registered baseline was produced under v1 data *and both pre-amendment thresholds*** — the 1.9 m small-vessel wave boundary (superseded 2026-09-06) and the 7.5 mm/hr rainfall boundary (superseded 2026-09-08). It is therefore a **third configuration**, not "v1/incumbent" as currently specified.
>
> **The register is internally inconsistent on this point.** P10, P11 and P12 carry post-amendment values; P09 carries a pre-amendment one, restored by hand per its own `notes` field. **This is a C-7 baseline-reconciliation item and is recorded, not fixed here.**

**Consequence for the earlier isolation.** The readiness audit reported P09 Δ_data = **−215** (5,416 → 5,201). **That figure conflated the threshold amendments with the data change.** Isolated cleanly at current thresholds, the data effect is **−19** (5,220 → 5,201). The remaining −196 is threshold vintage, not data.

**The gate is defined on P12, and P12 passed exactly**, so Stage 2 proceeded.

---

## 3. Hysteresis semantics — documented, not redesigned

Read from `classify_hysteretic()` and reused verbatim in all three stages.

| Property | Value |
|---|---|
| **Applies to** | **`g_o` and `g_r` only** |
| **Does NOT apply to** | **`g_w`, `g_t`, or the aggregated state** |
| **Level** | **Component level, BEFORE max-severity aggregation** |
| **Entry (rising) threshold** | Nominal — `o`: 1.0 / 1.25 m; `r`: 10.0 mm/hr |
| **Exit (falling) threshold** | `threshold × (1 − MARGIN)`, `MARGIN = 0.10` → `o`: 0.90 / 1.125 m; `r`: 9.0 mm/hr |
| **State memory** | `prev_o`, `prev_r`, carried across consecutive rows |
| **Initialisation** | **`prev_o = prev_r = 0` (SAFE)** |
| **`⊥` treatment** | Not represented in the replay — every row carries values; NaN rows dropped at load |
| **Excluded components `D = {m}`** | `g_m` pinned SAFE, simply absent from the max — identical in all stages |
| **Storm override** | `precip > 20.0` or WMO 95/96/99 forces `g_r = UNSAFE`, bypassing hysteresis |
| **Reset between datasets** | None — each stage is a single continuous series, re-initialised at its own first row |

**Identical semantics used in all three stages.** No parameter, rule or initialisation was altered.

---

## 4. Temporal-order verification

| Stage | Rows | Duplicates | Monotonic | Non-hourly steps | Span check | Complete |
|---|---|---|---|---|---|---|
| **1** v1/incumbent | 43,848 | **0** | ✅ | **0** | 43,848 | ✅ |
| **2** v2/incumbent | 43,848 | **0** | ✅ | **0** | 43,848 | ✅ |
| **3** v2/ModelB | 43,848 | **0** | ✅ | **0** | 43,848 | ✅ |

**No gaps, no duplicates, strictly increasing, uniform hourly cadence in every stage.** Timezone consistent — all inputs carry `utc_offset_seconds = 28800` (UTC+8). Since hysteresis is stateful, row ordering is part of the specification, and it is verified rather than assumed.

---

## 5. Initialization semantics

**`prev_o = prev_r = 0` (SAFE) at the first row of every stage** — the existing script's rule, preserved exactly. No more convenient initialisation was chosen for v2 or Model B.

**Comparability across stages is exact**: all three cover the identical window **2020-01-01 00:00 → 2024-12-31 23:00**, 43,848 rows. Stages 2 and 3 use the *same* dataframe, so their initial states are identical by construction. The v1 and v2 series share the same time boundaries, so no boundary adjustment was needed.

---

## 6. Stage 2 result — v2/incumbent

Only the data/configuration changes. `g_t` remains the incumbent fixed clock; all other thresholds identical.

| | |
|---|---|
| **Input** | `raw_weather_sea.csv` (wind, precipitation, WMO) + `raw_marine_era5_sea.csv` (waves), inner join on time |
| **Rows** | 43,848 |
| **P09** total transitions | **5,201** |
| **P10** non-scheduled | **207** |
| **P11** oscillations | **27** |
| **P12** reduction | **8.70%** |

*Precipitation is taken from `raw_weather_sea.csv`, not `raw_rainfall.csv` — the latter is still on the land cell F-10 condemned. This matches the canonical PRIMARY configuration.*

---

## 7. Stage 3 result — v2/ModelB

**Identical v2 inputs to Stage 2. The only classifier difference is `g_t`.**

| | |
|---|---|
| **Solar source** | **Frozen C-3 artefact** `data/solar/solar-events-daily.csv`, sha256 `057c46a1…1894` |
| **`g_t` image** | SAFE **21,754** · UNSAFE **22,094** · **CAUTION 0** ✅ |
| **Fail-safe** | Missing/invalid solar entry → UNSAFE. **0 rows required it** |
| **P09** total transitions | **3,661** |
| **P10** non-scheduled | **222** |
| **P11** oscillations | **26** |
| **P12** reduction | **10.36%** |

**No second solar implementation was created.** The harness contains no solar equations and calls no solar routine; it reads the stored `sunrise_hours` / `sunset_hours` columns and applies the half-open rule `sunrise ≤ t < sunset` from `solar-spec-v1`. Dependency: **C-3 frozen artefact → `g_t` → hysteretic analysis.**

---

## 8–10. P12 three-stage table and isolated effects

| | v1/incumbent | v2/incumbent | v2/Model B |
|---|---|---|---|
| **P12 reduction in non-scheduled transitions** | **7.83%** | **8.70%** | **10.36%** |

> ### **Δ_data = +0.87 pp**  (7.83 → 8.70) — data/configuration effect only
> ### **Δ_g_t = +1.66 pp**  (8.70 → 10.36) — SDR-001 classifier effect only
> ### Δ_total = +2.53 pp, and **Δ_total = Δ_data + Δ_g_t** ✅

**The `g_t` effect is roughly twice the data effect, and both raise the measured hysteresis benefit.** Under Model B, hysteresis removes a *larger share* of non-scheduled transitions than under the incumbent — because Model B eliminates the time-driven CAUTION band, so a greater proportion of the remaining non-scheduled transitions are wave- and rainfall-driven, which is exactly what hysteresis acts on.

**No CONFIRMED/REFUTED status was determined.** That is C-6, and it must follow C-7 baseline reconciliation.

---

## 11. P09 / P10 / P11 / P13 three-stage table

All four emerge from the same controlled pipeline. **Hysteresis-dependence is labelled, per instruction.**

| Prediction | Hysteresis-dependent? | v1/incumbent | v2/incumbent | v2/Model B | **Δ_data** | **Δ_g_t** | Δ_total |
|---|---|---|---|---|---|---|---|
| **P09** total transitions | ❌ **No** — non-hysteretic count | 5,220 | 5,201 | 3,661 | **−19** | **−1,540** | −1,559 |
| **P10** non-scheduled | ❌ **No** — non-hysteretic count | 230 | 207 | 222 | **−23** | **+15** | −8 |
| **P11** oscillations | ❌ **No** — non-hysteretic count | 37 | 27 | 26 | **−10** | **−1** | −11 |
| **P12** hysteresis reduction | ✅ **Yes** — requires both runs | 7.83 | 8.70 | 10.36 | **+0.87** | **+1.66** | +2.53 |
| **P13** interpretation | ❌ No — derived from P10/P11 | non-sched 230, osc 37 | 207, 27 | 222, 26 | — | — | — |

> **Only P12 requires `classify_hysteretic()`.** P09, P10, P11 and P13 are defined on the *plain* classification and were **not forced through the hysteretic loop** — they are reported from the same controlled pipeline for isolation, as instructed. The hysteretic run is nonetheless executed at every stage, because P12 needs both series.

**P13's conclusion is unaffected at every stage:** non-scheduled ≤ 500 and oscillations ≤ 100 hold in all three (230/37, 207/27, 222/26). Mode-chattering remains undemonstrated under Model B.

**No register entry was changed.** These are candidate results for C-6/C-7.

---

## 12. P09 expected cross-check

| | Expected (readiness audit) | Computed | Result |
|---|---|---|---|
| v1/incumbent | 5,416 | **5,220** | ❌ **Differs — diagnosed, §2.2** |
| v2/incumbent | 5,201 | **5,201** | ✅ **Exact** |
| v2/Model B | 3,661 | **3,661** | ✅ **Exact** |

**Two of three reproduce exactly.** The v1 baseline differs for the reason established in §2.2: 5,416 requires **both** pre-amendment thresholds. **Nothing was forced, and the register was not modified.**

**Corrected decomposition:** Δ_data = **−19** (not −215) and Δ_g_t = **−1,540** (unchanged). The `g_t` effect was reported correctly; the data effect was overstated by a factor of eleven because it absorbed the threshold amendments.

---

## 13. Interaction between Model B and hysteresis

**Determined from the code, not assumed.**

> ### **Hysteresis does not act on `g_t`. The Model B sunrise/sunset transition is NOT hysteretically delayed.**

`classify_hysteretic()` applies dual-threshold logic to `g_o` and `g_r` only, then passes `g_w` and `g_t` unmodified into the max. `g_t` — incumbent or Model B — reaches the aggregation with no state memory, no return margin, and no delay.

**Consequences:**

1. **The direct SAFE→UNSAFE solar transition survives hysteresis intact.** C-4 accepted that transition as a design cost; C-5 confirms the existing mechanism neither mitigates nor worsens it.
2. **Every `g_t`-driven transition is "scheduled"** by the script's own definition (`g_t` changed across the boundary), so it is excluded from the non-scheduled counts that P10, P11 and P12 measure. This is why P12 can *rise* under Model B while total transitions *fall* by 1,540.
3. **No sunset hysteresis was invented.** Per §14 of the instruction: no twilight CAUTION, no grace period, no sunset delay, no pre-sunset hysteresis, no notification interval. **C-5 measures the transition; it does not redesign it.**

---

## 14. Frozen output artefacts

| Artefact | sha256 |
|---|---|
| `data/c5/c5-three-stage-metrics.csv` | `3566cd6b1aab6cd362180bb7034e97b6497c259ffd7414061d33c53b4a76feb7` |
| `data/c5/c5-three-stage-deltas.json` | `23de3c07558b0c979b0ffceb86d56364c730d7185c5c4bf4a1541a0b94ed92ec` |
| `data/c5/c5-run-manifest.json` | `1f04720cb373e688925d1aa14299a9b056bf445b7641bc2e4b7c77795ee5c9ba` |
| `scripts/c5/three_stage_hysteresis.py` | `846b93abea5fc952632f649a3b72cb94bb77b9cd81f64f13037c4694ada9377a` |

The metrics CSV carries one row per stage with rows, date span, and all five metrics. The deltas JSON carries the stage records, temporal checks, isolated deltas with an additivity check, the Stage-1 register cross-check, and the P09 provenance sweep. **C-6 can consume these without re-running anything.**

---

## 15. Run manifest

**`data/c5/c5-run-manifest.json`** — sha256 `1f04720cb373e688925d1aa14299a9b056bf445b7641bc2e4b7c77795ee5c9ba`

Records, per stage: input artefact paths **with sha256 for every input file**, the `g_t` specification, the solar artefact and its hash/spec/impl version (Stage 3 only), row counts, exclusions, thresholds, full hysteresis parameters and initialisation, both code hashes, output artefact hashes, UTC timestamp, and the register hash before the run. **This is the provenance authority for C-5.**

---

## 16. Files and scripts modified

| File | Status |
|---|---|
| `scripts/c5/three_stage_hysteresis.py` | **Created** — isolated harness |
| `data/c5/c5-three-stage-metrics.csv` · `c5-three-stage-deltas.json` · `c5-run-manifest.json` | **Created** — frozen outputs |
| `docs/canonical/finding-gt-evidence-closure.md` | **Modified** — C-5 row marked CLOSED in the execution-conditions table |
| `docs/canonical/report-c5-closure-2026-09-08.md` | **Created** — this report |

> **`scripts/hysteresis_analysis.py` was NOT modified and NOT executed.** Hash unchanged: `73015d881a29cd4d…`. It was imported so that `classify_hysteretic`, `g_t_series`, `count_oscillations` and `load` are the *same code paths* the historical result came from. Executing it would have rewritten the register even under the guard, because `main()` calls `reg.to_csv()` unconditionally.

A stray `__pycache__` created by the import was removed.

---

## 17. Prediction-register integrity

| | |
|---|---|
| **BEFORE** | `538808b6d82249faa66caf20fece38e994144fbbe2280b62d3193817a3cdc484` |
| **AFTER** | `538808b6d82249faa66caf20fece38e994144fbbe2280b62d3193817a3cdc484` |
| **Result** | ✅ **BYTE-FOR-BYTE IDENTICAL** — matches the integrity anchor |

24 entries · **22 CONFIRMED / 2 REFUTED**. Values untouched: P09 `5416.0`, P10 `230.0`, P11 `37.0`, P12 `7.83`, P13 `non-sched=230, osc=37`.

**C-5 generated evidence. C-6 decides re-resolution. The operations remain separate.**

---

## 18. Canonical `g_t` integrity

> **`g_t^canonical` = `g_t^incumbent`** — SAFE 06:00 ≤ t < 17:00 · CAUTION 17:00 ≤ t < 19:00 · UNSAFE otherwise

All three rows verbatim in Appendix C. The four solar terms present in Appendix C are confined to the C-4 subsection explicitly headed *"Approved replacement design, pending canonical migration"* — the canonical table is unchanged.

**Unchanged by hash:** `hysteresis_analysis.py` `73015d88…` · `canonical_figures.py` `5af9eaf7…` · `condition_comparison.py` `1f0f4e9c…` · `solar.py` `3b7dc371…` · solar artefacts `057c46a1…` / `da14a8dc…`.

**Also unchanged:** wind 21.6/27.0 · rainfall 10.0/20.0 · wave 1.0/1.25 · `cause` · `G(S)` · `A_AI(S)` · **canonical figures 7.72% (×8) and 5.98% (×5)** · empirical findings §0a.

**Stage 3 remains a controlled migration candidate.** Nothing from it entered the canonical specification.

---

## 19–20. Condition status

| | Condition | Status |
|---|---|---|
| **C-1** | Pin solar implementation | ✅ **CLOSED** — unaffected; Stage 3 consumed `solar-spec-v1` / `solar-v1` |
| **C-2** | 28-row USNO validation artefact | ✅ **CLOSED** — unaffected, unchanged |
| **C-3** | Daily solar-event artefact | ✅ **CLOSED** — **consumed** by Stage 3, unmodified |
| **C-4** | Document Model B design consequences | ✅ **CLOSED** — unaffected; §13 confirms its accepted step cost is untouched by hysteresis |
| **C-5** | Three-stage hysteretic isolation | ✅ **CLOSED** |

### C-5 closure test — all thirteen criteria

| # | Criterion | Met |
|---|---|---|
| 1 | Stage 1 reproduces authoritative P12 = 7.83 | ✅ Exactly, \|diff\| 0.0000 |
| 2 | Hysteresis semantics documented | ✅ §3 — 11 properties |
| 3 | v2 port uses identical hysteresis semantics | ✅ Same reused loop, same params, same init |
| 4 | Stage 2 runs under incumbent `g_t` | ✅ §6 |
| 5 | Stage 3 runs under Model B | ✅ §7 |
| 6 | Stage 3 consumes frozen C-3 timestamps | ✅ No solar equations in the harness |
| 7 | P12 has all three stage values | ✅ 7.83 / 8.70 / 10.36 |
| 8 | Data effect and `g_t` effect separately quantified | ✅ +0.87 / +1.66, additive |
| 9 | P09/P10/P11/P13 isolated where applicable | ✅ §11, hysteresis-dependence labelled |
| 10 | Temporal ordering / gaps / initialization verified | ✅ §4–§5 |
| 11 | Raw outputs and manifest stored | ✅ §14–§15, all hashed |
| 12 | Register byte-for-byte unchanged | ✅ §17 |
| 13 | Canonical `g_t` unchanged | ✅ §18 |

---

## 21. C-6, C-7, C-8 — confirmed OPEN

| | Condition | Status |
|---|---|---|
| **C-6** | Re-resolve affected predictions | 🔴 **OPEN — not executed.** No CONFIRMED/REFUTED status determined; no register entry changed |
| **C-7** | Reconcile baseline discrepancies | 🔴 **OPEN — not executed.** **Now carries an additional, precisely diagnosed item: P09's registered 5,416 requires both pre-amendment thresholds** (§2.2), and the previously reported Δ_data = −215 should be corrected to −19 |
| **C-8** | Execute the propagation list | 🔴 **OPEN — not executed.** No canonical `g_t` conversion; no script or document propagated |

---

## 22. Assessment

**The gate was the point of this task, and it did its job twice over.**

P12 reproduced to the digit, which is what licensed Stages 2 and 3. But the same cross-check found that **P09's registered baseline does not reproduce** — and rather than accept "close enough" or quietly substitute the computed value, the sweep identified the exact configuration that yields 5,416: v1 data with *both* pre-amendment thresholds. That is a threshold-vintage mismatch, not a data effect, and it means the earlier isolation had **Δ_data wrong by a factor of eleven** — −215 where the clean figure is −19.

**This is precisely what three-stage isolation exists to catch.** A two-point comparison would have reported −1,559 and attributed it to whatever the analyst had in mind.

**The substantive P12 result is that hysteresis becomes *more* effective under Model B** (+1.66 pp), not less — because removing the time-driven CAUTION band leaves a higher proportion of non-scheduled transitions in the wave and rainfall components that hysteresis actually governs. And §13 settles a question C-4 could only flag: **hysteresis never touches `g_t`**, so the accepted sunset step is neither smoothed nor amplified by the existing mechanism.

**What was deliberately not done:** no status determined, no register touched, no sunset hysteresis invented, no canonical value changed. C-5 produced evidence; C-6 and C-7 decide what it means.

---

# **C-5 CLOSED — THREE-STAGE HYSTERETIC ISOLATION COMPLETE**

**C-1 · C-2 · C-3 · C-4 · C-5 CLOSED — C-6, C-7, C-8 REMAIN OPEN.**
**SDR-001 remains APPROVED — NOT YET APPLIED. Canonical migration has not begun.**
