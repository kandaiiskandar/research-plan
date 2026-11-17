# Causal N1–N4 Replication — Results

> **TWO CORRECTIONS — 17 Nov 2026, same day.** See `research/supervisor-decision-memorandum.md` §3.
> **(1)** This report's statement that *“~30.5 percentage points of `DepartureTime` availability was leakage”* **overstates it and is withdrawn.** G-L differs from G-B in **two** respects — leaky calibration *and* perfect foresight versus a deliberately minimal surrogate. The design identifies a **bracket** (the achievable rate lies in 2.48%–32.99% and rises with intra-window forecast skill), **not a leakage share**. Separating them requires a fourth condition, G-O = perfect foresight + causal calibration, which has not been run.
> **(2)** E-ES-8's rates are conditional, and the block sizes shown below are **not** their denominators. E-ES-8a all-cases: **3,551** elevated episodes (not 7,305). E-ES-8a daylight: **673** elevated episodes (not 4,427), so 26.597% rests on ~179 mismatches, ±~3.4 pp at 95%. E-ES-8b both blocks: **3,754** SAFE episodes — identical in both because `S` = SAFE entails `g_t` = SAFE, which is a correctness check that held exactly.
> **Nothing below is edited.**


**Executed:** 17 November 2026 · **Author:** Claude (Cowork session) · **Status:** **EXPLORATORY.** Supersedes no canonical result and creates none.

**Frozen artefacts untouched.** The original gate script, its results JSON and its 9,135-episode case table are byte-identical (MD5-verified). `git status` reports no tracked file modified. All new code and output is under `research/non-degeneracy/causal/`.

**No threshold was adjusted to obtain a pass.** Every criterion ran at the value pre-registered in R1–R3. Five criteria failed and two of my own leak checks were found defective; all are reported as such below.

**Preserved.** Original N1–N4 (9,135 episodes) and R1/R2/R3 criteria remain in their own documents. This report adds; it rewrites nothing.

---

## 1. Headline

**The causally honest generators cannot produce `DepartureTime` at a usable rate. `G-A` produces it at exactly 0.00%; `G-B` at 2.48%, against a pre-registered bar of 10%. The leaky original produced it at 32.99% on the same window.**

So **~30.5 percentage points of `DepartureTime` availability was leakage**, and the pre-registered consequence now applies: per R2 §10, *"if G-B fails E-GC-1, the conclusion is not that the study is impossible but that it requires real forecast data."* That condition has been met.

Three things also went right, and they matter:

- **G-B carries genuine forecast information in `Duration`.** All four bin-free E-GC-2b tests pass, and `G-A` sits at its exact structural values — cardinality 2, step residual 0.000000, base R² 1.000000. The episode-specific margin correction worked precisely as intended.
- **G-B has real, measured skill.** On the generator's own acceptability notion, its false-acceptable rate at lead 8 is **19.1% against persistence's 31.7%**, and its reliability is **0.831 against 0.767**.
- **Case availability passes for all three conditions** — 441 boundary cases, 137 CAUTION∩boundary, and 121–146 cases where C1 ≠ C2.

---

## 2. Validation

| | Expected | Observed (2021–2024, 7,305 episodes) | |
|---|---|---|---|
| **V-1** `P(S = CAUTION)` | canonical 5.81% on 9,135 | **5.7906%** | ✓ within 0.02 pp on a shorter window |
| **V-1** UNSAFE share | canonical 42.88% | **42.82%** | ✓ within 0.06 pp |
| **V-3** G-L type shares | published 36.12% / 72.56% | 32.99% / 63.23% | ✓ window effect, as R2 predicted |
| **V-4 / L-CHK-7** `α ≡ 1` reproduces G-A | exact | **7,305 / 7,305 identical** | ✓ |

**V-2 revised prediction confirmed.** G-A yields `Go` 59.29%, `Delay` 40.71%, `DepartureTime` **0.00%**, `Duration` 69.68%. The prototype yields `Delay` only. The residual is the two gaps R3 identified — no executable SAFE rule, and no `Duration` rule — and **not** an information gap, since `Duration` is reachable from concurrent information alone.

---

## 3. Leakage checks — and two defects in my own checks

### 3.1 Two checks were broken on the first run

| Check | What happened | Root cause |
|---|---|---|
| **L-CHK-1** | Reported `compared: 0, PASS: true` for all three conditions — **a vacuous pass** | `str()` on a pandas `Timestamp` gives `'2021-01-01 05:00:00'`; on a numpy `datetime64` it gives `'2021-01-01T05:00:00.000000000'`. The key sets never intersected |
| **L-CHK-4** | Reported `60/60 changed_or_failed` for **all three**, including the causal conditions | The same mismatch raised `KeyError`, caught by a bare `except` and counted as a failure |

**A leak check that reports a pass on zero compared cases is the exact failure mode this whole exercise exists to prevent**, and I wrote it. Both are fixed: one canonical `tkey()` formatter, a `VACUOUS` flag that makes an empty comparison fail rather than pass, and the exception text now recorded instead of swallowed. The defective runs are preserved as `leakage-checks-RUN1-defective.json` and `leakage-checks-RUN2-stale.json`.

### 3.2 Corrected results — gates pass for the causal conditions

| Check | G-L | G-A | G-B | |
|---|---|---|---|---|
| **L-CHK-1** truncation invariance (cut 2022-12-31) | **FAIL** 99/3,650 differ | PASS 0/3,650 | PASS 0/3,650 | G-L's L1/L2 calibration leak |
| **L-CHK-3** future-shuffle (post-2023 shuffled) | **FAIL** 240/5,475 differ | PASS 0/5,475 | PASS 0/5,475 | same |
| **L-CHK-4** placebo-future (post-episode → NaN) | **FAIL** 43/60 changed | PASS 0/60 | PASS 0/60 | G-L's L3 within-day lookahead |
| **L-CHK-5** calibration provenance | — | PASS 0/48 epochs | PASS | every epoch's source ends before the epoch starts |
| **L-CHK-7** `α ≡ 1` identity | — | — | PASS 0 differ | |
| **L-CHK-2/8** causal view | FullView by design | PASS, no violation | PASS | enforced by type: `CausalView` raises on any read past the episode |

**`GATES_PASS_for_causal_conditions: true`.** G-L fails exactly the three checks it should, which is what demonstrates the checks detect leakage rather than merely passing.

### 3.3 A-CHK — availability, declared not gated

**C1 chronological causality: SATISFIED** for G-A and G-B. **C2 operational availability: NOT SATISFIED for any condition.** The record is ERA5-Ocean reanalysis with days-to-months production latency; nothing in it was available at 05:00 on the morning it describes. This applies to the architecture's own replay too, and belongs in the abstract rather than the limitations.

---

## 4. Generator capability

| | G-L (leaky) | G-A (persistence) | G-B (surrogate) | Bar |
|---|---|---|---|---|
| `Go` | 59.53% | 59.29% | 59.29% | — |
| `Delay` | 40.47% | 40.71% | 40.71% | — |
| **`DepartureTime`** | **32.99%** | **0.00%** | **2.48%** | **≥10%** |
| `Duration` | 63.23% | 69.68% | 68.02% | — |
| **E-GC-1** | **PASS** | **FAIL** | **FAIL** | |
| **E-GC-2b-i** distinct run values | 10 | **2** `{0, 9}` | 10 | ≥4 |
| **E-GC-2b-ii** step unexplained | 37.47% | **0.000000** | 24.65% | ≥10% |
| **E-GC-2b-iii** discordant near-tie pairs / share far from breakpoint | 3,246 / 76.8% | **1 / 0.0%** | 2,283 / 67.5% | ≥50% |
| **E-GC-2b-iv** base R² / calendar share of residual | 0.2123 / 34.6% | **1.000000 / 0.0%** | 0.6252 / 31.5% | R² < 0.95 |
| **E-GC-3** at 05:00 | 47.2% modal, 4 targets | n = 0 | **86.8% modal, 2 targets** | ≤70% |

### What this says

**The margin correction was necessary and it worked.** G-A's step residual is **exactly** 0.000000 and its base R² is **exactly** 1.000000. Under a global breakpoint these would have been non-zero from threshold drift alone — the episode-specific margin `m_ok = ê(h) − e_ok(epoch)` is what makes persistence's determinism visible. R3 §1.2's design rule held: the discriminator is exactly zero under persistence by construction, not merely small.

**`Duration` under G-B is genuinely forecast-informative.** Ten distinct run lengths, a quarter of episodes unexplained by the concurrent margin, two thirds of discordant near-ties far from the breakpoint, and the calendar explaining 31.5% of the residual. That is the signature R3 predicted and G-A does not have it.

**`DepartureTime` is the wall.** Even where G-B produces it, 86.8% of its targets at 05:00 point at 09:00 — the last window hour — across only 2 distinct targets. So the few recommendations it makes are close to "go as late as you can", which is weak advice dressed as timing guidance. **E-GC-3 fails for G-B**, and it is the one criterion where the leaky generator looks qualitatively better (47.2% modal, 4 targets).

**The leak's direction differs by type.** `DepartureTime` was inflated by 30.5 pp. `Duration` was **deflated** — 63.23% leaky against 69.68% under persistence — because reality is less persistent than persistence assumes, so an oracle sees runs break that the surrogate predicts continuing. The leak did not simply make the generator better; it made it differently wrong.

---

## 5. Forecast skill, and a refuted prediction of mine

### 5.1 G-B is measurably more skilful than persistence

False-acceptable rate on the generator's own acceptability notion (T-INT), by lead:

| Lead | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| **G-A** | 9.4% | 14.6% | 18.7% | 23.3% | 27.1% | 30.2% | 31.6% | **31.7%** |
| **G-B** | 9.8% | 13.4% | 16.4% | 19.2% | 20.1% | 20.5% | 19.8% | **19.1%** |
| **G-L** | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% |

G-B is marginally worse at lead 1 and clearly better from lead 3 onward, **turning over after lead 6 while persistence keeps degrading**. Reliability of "predicted acceptable": **G-B 0.831, G-A 0.767, G-L 1.000**. The fitted damping shows why — α at lead 8 is **0.278 for wind and 0.138 for precipitation**, but **0.970 for wave**.

**The structural consequence is important.** The surrogate has skill where the architecture does not bind, and almost none where it does: wave is 97.6% of CAUTION activation and is the one variable for which persistence is already near-optimal. **Adding a climatological forecast improves the variables that never bind.**

### 5.2 E-ES-7 — my R3 prediction is refuted, and the reason is instructive

R3 §2.1 predicted G-L's false-acceptable rate would be **zero on T-INT but non-zero on T-PHYS**, because an oracle for the exposure index is not an oracle for separate physical thresholds.

**Observed: G-L's FAR_acc is 0.0 at every lead on T-PHYS too.** The reasoning identified a real distinction but **mis-located it in the metric.** T-PHYS as implemented compares *the forecast of a variable* against *a threshold on that same variable* — so an oracle on the variable is trivially an oracle on any threshold of it. The index–threshold mismatch I described is a property of the generator's *acceptability decision*, not of its per-variable forecasts.

**The mismatch is real and it was measured — by E-ES-8, not E-ES-7** (§6). So the correction was right about the phenomenon and wrong about which metric would show it. Recorded as refuted.

### 5.3 E-ES-5 passed vacuously — the fifth non-discriminating criterion

E-ES-5 passed at share = 1.000 for **all three conditions**, including persistence. The reason: FAR_acc on wave > 1.0 m ranges from 0.4% to 2.1% across all leads, so every lead clears the 0.10 bound trivially. The bound sits roughly five times above the achievable range and **can never bind on wave**.

Two causes, both mine. The bound was a declared judgement with no evidence behind it, and I set it without checking the base rate — wave exceeds 1.0 m in ~14% of hours and persistence is near-perfect on wave, so low false-acceptable rates are arithmetic, not skill. **A related guard is also missing:** `wind > 21.6 kn` has **zero** exceedances at lead 8, so its FAR_acc is reported as 0.0 from an empty numerator. The `MIN_CELL_N` rule guards the denominator and POD but not FAR_acc against a zero base rate.

**E-ES-5 should be re-specified against T-INT, where the spread is 9%–32% and discriminates, and FAR_acc should carry a base-rate guard.** Not changed here; reported as failed-by-vacuity.

---

## 6. E-ES-8 index–state concordance — the daylight split changed the answer

| | All cases | **Daylight only (`g_t` = SAFE)** |
|---|---|---|
| n | 7,305 | 4,427 |
| episodes with `S` elevated | 3,551 | 673 |
| **E-ES-8a permissive mismatch** | **60.997%** | **26.597%** |
| E-ES-8b restrictive mismatch | 22.110% | 22.110% |
| **E-ES-8c driver of the elevated state** | **time 76.3%**, wave 18.5%, time+wave 4.7%, rain 0.4% | **wave 97.8%**, rain 2.2% |

**Reporting only the all-cases figure would have overstated the confound by a factor of 2.3.** The 61% is almost entirely the generator having no time-of-day term at all: `g_t` drives 76.3% of elevated states, and the exposure index is built from wind, wave and precipitation only. That mismatch is structural and uninteresting.

**The environmental mismatch is 26.6%** — in roughly a quarter of daylight episodes where the architecture says CAUTION or UNSAFE, the generator calls the hour workable. That is the real confound for a rating study, and it is large enough to matter: in the C0 and C1 arms it is unfiltered, so a panel could attribute to "absence of governance" what is the exposure index's mean-of-percentiles aggregation disagreeing with max-severity.

**An independent reproduction worth noting.** In daylight, the driver of elevated states is wave at **97.8%** — against the canonical `g_o` attribution of **97.6%**, reached by a completely different route. RQ3's negative result is corroborated from outside its own analysis.

---

## 7. Governance effectiveness and case availability

| | G-L | G-A | G-B | |
|---|---|---|---|---|
| `P(S = CAUTION)` — the structural ceiling | 5.7906% | 5.7906% | 5.7906% | identical by construction |
| **E-GE-1** divergence, all cases | 2.00% | 1.79% | 1.66% | descriptive, no gate |
| **E-GE-1** divergence, CAUTION pool | 34.52% | 30.97% | 28.61% | |
| **E-GE-2** withheld realised in CAUTION | 34.52% ✓ | 30.97% ✓ | **28.61% ✗** | marker 30% |
| **E-GE-3a** `Go`/`Delay` bit identical | **1.000000** | **1.000000** | **1.000000** | |
| **E-GE-3b** divergences solely withheld forecast types | **1.000000** | **1.000000** | **1.000000** | |
| **E-CA-1** boundary cases | 441 ✓ | 441 ✓ | 441 ✓ | ≥120 |
| **E-CA-2** CAUTION ∩ boundary | 137 ✓ | 137 ✓ | 137 ✓ | ≥60 |
| **E-CA-3** C1 ≠ C2 cases | 146 ✓ | 131 ✓ | **121 ✓** | ≥100 |

**R2 prediction 5 confirmed.** Unstratified divergence moves only from 2.00% to 1.66% across conditions — governance effectiveness is a property of the classifier and the record, not of the generator, and it sits far below its 5.79% ceiling.

**E-GE-2 fails for G-B by 1.4 points.** The marker stays at 30%.

**D-4h now confirmed empirically as well as analytically.** `E-GE-3a = 1.000000` and `E-GE-3b = 1.000000` in all three conditions: the `Go`/`Delay` bit is identical under C1 and C2 in **every** episode, and every divergence consists solely of withheld `DepartureTime`/`Duration`. Boundary cases remain a wave phenomenon — 435 wave, 2 wind, 5 rain.

---

## 8. Criterion verdict matrix

No composite pass is computed.

| | G-L | G-A | G-B |
|---|---|---|---|
| E-GC-1 type coverage | PASS | **FAIL** | **FAIL** |
| E-GC-2b-i cardinality | PASS | **FAIL** | PASS |
| E-GC-2b-ii step conformity | PASS | **FAIL** | PASS |
| E-GC-2b-iii near-tie distance | PASS | **FAIL** | PASS |
| E-GC-2b-iv calendar residual | PASS | **FAIL** | PASS |
| E-GC-3 target spread at 05:00 | PASS | n/a (no advice) | **FAIL** |
| E-ES-5 skilful-lead share | PASS (vacuous) | PASS (vacuous) | PASS (vacuous) |
| E-GE-2 adequacy marker | meets | meets | **misses** |
| E-CA-1 / 2 / 3 | PASS | PASS | PASS |

G-A's five FAILs are the **intended** structural result: persistence cannot support forecast-dependent advice, and the tests say so at their exact structural values.

---

## 9. What this does not establish

1. **Exploratory throughout.** Criteria were specified after the original gate had run; original and revised sets must be published side by side.
2. **C2 operational availability is not satisfied**, so no claim can be made about advice a fisher could have received.
3. **E-ES-5 passed vacuously** and E-ES-7's T-PHYS prediction is refuted. Neither is evidence of skill adequacy.
4. **FAR_acc lacks a base-rate guard**, so zero-exceedance cells report 0.0 misleadingly.
5. **G-B is one surrogate.** A fitted lead-time regression or real NWP would have more skill, particularly on wave, where α ≈ 0.97 leaves little for climatology to add.
6. **The exposure index weights the three variables equally** — a declared arbitrary choice. The sensitivity grid S1–S9 has **not** been run; everything here is the primary configuration only.
7. **PRIMARY only.** RESOLUTION (MFWAM) is untouched.
8. **Six non-discriminating or defective criteria of mine have now surfaced** — E-GC-2 (unpassable), E-GC-3 (confounded, fixed in R2), E-GE-3 (true by construction), E-GC-2b (bin width), E-ES-5 (vacuous), plus two broken leak checks. The rate is not declining, and every one was found by someone checking rather than by the run itself.

---

## 10. What follows

| | Item | Recommendation |
|---|---|---|
| **A** | **`DepartureTime` needs real forecast skill.** 0.00% under persistence, 2.48% under a climatological surrogate, 32.99% only with leakage | **Treat real issue-time forecast data as a precondition** for any advisory comparison that depends on timing advice — the R2 §10 pre-registered consequence has triggered. The forecast archives now carry five justifications |
| **B** | **A `Go`/`Delay`-only study is feasible now.** Both types sit near 59%/41% in every condition, and 121 C1 ≠ C2 cases exist under G-B | But note `A_AI(CAUTION) = {Go, Delay}` withholds neither, so such a study would have **nothing to compare** — which is D-4h restated as an empirical result |
| **C** | **E-ES-8a = 26.6% in daylight must be declared before any rater is recruited** | A quarter of elevated-state daylight episodes are called workable by the generator. Unfiltered in C0/C1, this is attributable noise |
| **D** | Re-specify **E-ES-5** against T-INT and add a base-rate guard to FAR_acc | Do not re-run until both are fixed |
| **E** | Run the **S1–S9 sensitivity grid**, especially S4 (`max` aggregation, which would cut E-ES-8a at the cost of independence) and S6 | Report as a trade-off curve |
| **F** | **Supervisor decision unchanged in substance, sharper in evidence:** the advisory comparison as designed is not feasible on reanalysis alone | The blocker is now measured, not argued |
