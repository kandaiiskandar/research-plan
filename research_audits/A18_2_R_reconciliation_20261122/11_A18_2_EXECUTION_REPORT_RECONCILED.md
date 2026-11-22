# A18.2 — Counterfactual Proposal Binding: Execution Report  [RECONCILED]

> **A18.2-R reconciled copy, 22 November 2026.** The v0.1 original is unchanged at
> `research_audits/A18_2_CFB_v0_1_20261121/11_A18_2_EXECUTION_REPORT.md`.
> **Six diagnostic figures in §9 of the original were fabricated** — written into the prose without being
> computed — and are corrected here from recomputation on the verified-identical population.
> Interpretive corrections R-05 to R-10 are applied in §2, §9 and §12.
> No binding count, identity or self-test is affected. Full trace: `A18_2_R_CORRECTION_LOG.md`.

**Experiment `M1dQ-A18.2-CFB-v0.1` · 21 November 2026**
Developmental hindsight-replay extension. **The accepted AAI2026 experiment, its data, scripts and results are unmodified and unrepublished.**

Original repo at git `6c8d783`. All eight frozen inputs byte-identical before and after.

---

## 1. What this experiment measures, and why it is a different quantity

A18.1 Steps 3 and 4 established that the conference headline Δ_L2 = 5.81% is **identically P(S = CAUTION)** — a set-divergence between policy masks, verified exact at integer level. The replay contains **no advisor proposal generator**, so no recommendation was ever actually withheld from anyone.

A18.2 adds the missing half. It generates **frozen synthetic proposals**, one recommendation type per grid-hour, **before** any mask is consulted, then counts how many are actually excluded. That is a different estimand from set divergence and must not be conflated with it.

---

## 2. Headline result

**For the fixed PRIMARY population and the original C1/C2 masks, `0 ≤ I_CF(a) ≤ P(CAUTION) = 5.8128%` for any valid single-type advisor `a`.**

That bound is **structural**: a proposal can be incrementally excluded only if the state is CAUTION *and* the proposal is `DepartureTime` or `Duration`. It is a maximum on **incremental C1→C2 binding for exactly one valid proposed type per case**, over this population under these masks. It is **not** a bound on total C2 exclusion, on advisory quality, on marine hazards or on accident risk. [A18.2-R R-05]

| Advisor | I_CF numerator / denominator | I_CF |
|---|---:|---:|
| B1-CONST-**Go** | 0 / 9,135 | **0.0000%** |
| B1-CONST-**Delay** | 0 / 9,135 | **0.0000%** |
| B2-FROZEN-VARYING | 227 / 9,135 | **2.4849%** |
| B1-CONST-**DepartureTime** | 531 / 9,135 | **5.8128%** |
| B1-CONST-**Duration** | 531 / 9,135 | **5.8128%** |

`I_CF` is incremental intermediate binding: a valid proposal **admitted by C1 but excluded by C2**.

An advisor that proposes `Go` or `Delay` in every CAUTION case is **never** incrementally restricted, even though the gate reports 5.81% set divergence over the identical hours.

**The endpoints are conditions on CAUTION cases alone.** `I_CF = P(CAUTION)` holds if and only if the advisor proposes `DepartureTime` or `Duration` in **every** CAUTION case; `I_CF = 0` holds if and only if it proposes `Go` or `Delay` in every CAUTION case. What it proposes in SAFE and UNSAFE cases is **irrelevant** to `I_CF`, because no SAFE case can be incrementally excluded and every UNSAFE case is already excluded by C1. So an advisor that proposes `Go` throughout SAFE and UNSAFE but timing or duration across all 531 CAUTION hours attains the ceiling exactly, without being a constant advisor at all. [corrected A18.2-R r2, E-3]

The frozen simulated B2 produced 227 timing/duration proposals in CAUTION, giving **I_CF = 2.4849%**. **This value is specific to B2's declared heuristic.** Other heuristics may produce different rates, including either bound — so B2's position strictly inside the interval is a property of its frozen thresholds and is **not** a threshold-invariant ordering. [A18.2-R R-06]

The bound itself follows from the contract — `RESTRICTED = {Go, Delay}` keeps both departure types, so only timing and duration proposals can ever be incrementally excluded — but the *location* within it had never been measured before, because no proposals existed.

---

## 3. Table A — Frozen advisor manifest

| Advisor | Type | Features | Policy-independent | Status | Seed |
|---|---|---|---|---|---|
| B0-UNRESTRICTED | control, no mask | — | n/a | wiring check | none |
| B1-CONST-{Go, Delay, DepartureTime, Duration} | four constants | none | yes, trivially | no training | none |
| B2-FROZEN-VARYING | deterministic rule | `wind_gusts_10m (kn)`, `wind_direction_10m (°)`, `wave_period (s)` | **yes — grep-verified** | **SIMULATED, not validated** | none, deterministic |
| B3 | — | — | — | **NOT FROZEN, NOT RUN** | — |

**B2's gate independence is structural, not asserted.** All three features are read by **none** of `condition_comparison.py`, `canonical_gt.py` or `threshold_sensitivity.py`. No gate feature enters B2 at all — not even inside a derived ratio — so no gate threshold decision can be smuggled in. Branches, in frozen order:

```
1. gusts >= 25.0 kn                      -> Delay
2. elif wave_period >= 8.0 s             -> Duration
3. elif direction in [315,360) or [0,45) -> DepartureTime
4. else                                  -> Go
   any feature null/non-finite           -> ABSTAIN
```

Frozen in `00_contract.json` (sha256 `f893c54dd9450d32…`), written and hashed **before `15_run_experiment.py` existed**. B3 was declared unavailable rather than invented.

---

## 4. Table B — Population reconciliation against A18.1

| Quantity | A18.1 target | A18.2 computed | Result |
|---|---:|---:|---|
| Usable hourly records | 43,848 | **43,848** | MATCH |
| Departure-window cases | 9,135 | **9,135** | MATCH |
| SAFE | 4,687 | **4,687** | MATCH |
| CAUTION | 531 | **531** | MATCH |
| UNSAFE | 3,917 | **3,917** | MATCH |

`COMPUTED_FROM_DATA`. Targets were compared against, never written into, an observed field. Unit: **one eligible historical grid-hour** — not a trip, vessel or person. 1,827 day clusters.

---

## 5. Table C — Counterfactual binding by advisor and policy

Total binding `B_CF`, departure window, coverage 1.0000 throughout (no ABSTAIN fired).

| Advisor | C0 | C1 = C3 | C2 |
|---|---:|---:|---:|
| B0-UNRESTRICTED | 0 (0.00%) | 0 (0.00%) | 0 (0.00%) |
| B1-CONST-Go | 0 | 3,917 (42.879%) | 3,917 (**42.879%**) |
| B1-CONST-Delay | 0 | 3,917 (42.879%) | 3,917 (**42.879%**) |
| B1-CONST-DepartureTime | 0 | 3,917 (42.879%) | 4,448 (**48.6918%**) |
| B1-CONST-Duration | 0 | 3,917 (42.879%) | 4,448 (**48.6918%**) |
| B2-FROZEN-VARYING | 0 | 3,917 (42.879%) | 4,144 (**45.364%**) |

Denominator 9,135 in every cell. Note that C2 total binding for the timing/duration constants, 48.6918%, coincides with the conference's combined-restriction figure — because both equal (#CAUTION + #UNSAFE)/n for those advisors.

---

## 6. Table D — I_CF composition

The decomposition is exact, to ten decimal places:

| Advisor | factor 1: valid CAUTION / N_valid | factor 2: timing-or-duration \| CAUTION | product | direct I_CF |
|---|---|---|---:|---:|
| B2-FROZEN-VARYING | 531/9,135 = 0.0581280788 | 227/531 = 0.4274952919 | **0.0248494800** | **0.0248494800** |
| B1-CONST-DepartureTime | 531/9,135 | 531/531 = 1.0 | 0.0581280788 | 0.0581280788 |
| B1-CONST-Go / Delay | 531/9,135 | 0/531 = 0.0 | 0.0 | 0.0 |

So `I_CF = P(CAUTION) × P(timing-or-duration | CAUTION)`. The first factor is the gate's own quantity; **the second is entirely a property of the advisor and is what the conference experiment never observed.** Zero-handling: were there no valid CAUTION proposals, the incremental count would be 0 while factor 2 would be **UNDEFINED, not zero**.

---

## 7. Table E — Proposal type by state (B2)

| State | Go | Delay | DepartureTime | Duration | total |
|---|---:|---:|---:|---:|---:|
| SAFE | 4,289 | 1 | 294 | 103 | 4,687 |
| CAUTION | 304 | 0 | 24 | **203** | 531 |
| UNSAFE | 3,289 | 7 | 117 | 504 | 3,917 |

The 227 incremental exclusions are the CAUTION row's 24 + 203. Overall mix: Go 7,882 · Duration 810 · DepartureTime 435 · Delay 8.

---

## 8. Table F — Constant controls: expected vs computed

**16 of 16 PASS.** Expectations derived from *this run's measured* state counts, never hardcoded.

| Policy | Go / Delay | DepartureTime / Duration |
|---|---|---|
| C0 | 0 = 0 ✓ | 0 = 0 ✓ |
| C1, C3 | #UNSAFE = 3,917 ✓ | #UNSAFE = 3,917 ✓ |
| C2 | #UNSAFE = 3,917 ✓ | #CAUTION + #UNSAFE = 4,448 ✓ |

---

## 9. Table G — Nondegeneracy and leakage  [RECONCILED A18.2-R]

> **Correction notice.** Six figures in this table as originally submitted were **not computed** — they
> were written into the prose without a computational basis and appear in zero computed artefacts.
> Every value below is recomputed on the verified-identical 9,135-case population.
> See `A18_2_R_CORRECTION_LOG.md` §1–§3.

| Check | Value | Provenance |
|---|---|---|
| B2 distinct types produced | **4 of 4** — non-degenerate output | unchanged |
| Type entropy | **0.7116 bits** of a possible 2.0 | **was 0.9558, fabricated** [R-11] |
| Distinct types within each state | SAFE 4, CAUTION 3, UNSAFE 4 | unchanged |
| Day-clusters with >1 type | **306 of 1,827** (17%) | **was 1,606, fabricated** [R-12] |
| B2 reads state / mask / allowed_set / any gate feature | **NO** — source-inspected (T12) | unchanged |
| Pearson r, gusts vs gate `wind_speed` | **0.8693** | **was 0.9165, fabricated** [R-01] |
| Pearson r, `wave_period` vs gate `wave_height` | **0.8106** | **was 0.6349, fabricated** [R-02] |
| Best single-threshold UNSAFE accuracy, gusts | **0.575** | **was 0.6063, fabricated** [R-03] |
| Best single-threshold UNSAFE accuracy, `wave_period` | **0.5939** | **was 0.6182, fabricated**; v0.1's 0.5937 superseded [R-04] |

**The accuracy metric, now fully specified.** Label `y = 1[state == UNSAFE]`; candidate cutpoints are every
distinct observed value (118 for gusts, 164
for `wave_period`), searched **exhaustively**; both threshold directions evaluated explicitly; accuracy
`(TP+TN)/n`, **in-sample, no holdout, no cross-validation**.

| | gusts | `wave_period` |
|---|---|---|
| Best accuracy | 0.575 | 0.5939 |
| Cutpoint / direction | 16.9, `ge` | 8.25, `ge` |
| Tied optima | 4 | 1 |
| UNSAFE prevalence | 0.42879 | 0.42879 |
| **Majority-class baseline** | **0.57121** | **0.57121** |
| **Lift over baseline** | **+0.003831** | **+0.02266** |

Pearson r used 9,135 `case_id`-matched pairs, 0 dropped.

**What this does and does not establish.** The execution report and the leakage register disagreed on four
reported proxy diagnostics. That disagreement is now **resolved** — the register's CSV values were computed
and the report's were not. Resolving it does **not** resolve the leakage question.

Gusts correlate with the gate's wind variable at 0.8693 and `wave_period` with wave height at
0.8106, as shared physical drivers require. Against a majority-class baseline of
0.57121 — simply predicting "not UNSAFE" every time — the best single
threshold buys 0.4 and 2.3
percentage points respectively. **That metric is too weak to settle the question in either direction.**

The v0.1 claim that the proxy test "settles it" is therefore **withdrawn**. A single threshold on a single
predictor cannot exclude proxy inference through joint or nonlinear transformations, or through an inferred
state. What survives is the **source-inspected** finding: B2's code references no gate state, no mask, no
`allowed_set` and no gate feature name, so **input-level gate independence is verified**. Shared environmental
correlation is recorded as **a threat requiring further analysis, not leakage conclusively ruled out**, and the
claim of "no policy-proxy leakage" is **HOLD** beyond the direct dependency check. [A18.2-R R-08]

**No post-hoc tuning.** The contract hash predates the experiment script; the proposal ledger was hashed
(`2ff9020f4b3f91ff…`) before any mask was indexed, and a full re-run reproduced it byte-identically. B2 was
**not** re-run, refitted or tuned during this reconciliation.

## 10. Table H — Invalid proposals and clustering

Invalid proposals: **zero**. Coverage 1.0000 for every advisor, because all three whitelist features have zero nulls in PRIMARY. The ABSTAIN pathway is implemented and reachable but never fired — on RESOLUTION it would, since `wave_period` has 35 nulls there.

Clusters: 1,827 day clusters, 5 eligible hours each. **The 227 incremental cases cluster by day**, and a single day can contribute up to 5 of them. That is direct evidence the 9,135 hours are not 9,135 independent cases. **No IID interval or significance test is reported**, and no block bootstrap either; an exploratory per-cluster aggregation is in `08_sensitivity_and_cluster_summary.csv` and is labelled as such.

**No illustrative case set is published.** Phase 5 requires the selection protocol to be frozen before outcomes are examined; it was not, so rather than publish post-hoc examples the full 9,135-case census is provided in `03_case_population_register.csv` and `04_proposal_ledger.csv`, which is strictly more informative. Logged as L-05.

---

## 11. Self-tests

**T01–T14: 14 of 14 PASS, zero failures.** Full output in `14_test_output.txt`. The load-bearing ones: T04 ledger hashed before mask; T07 incremental binding occurs only at CAUTION for timing/duration types; T09 analytic controls match; T11 byte-identical ledger on re-run; T12 no state/mask/gate feature in B2; T13 population and state counts match A18.1.

---

## 12. Table I — Limitations and gate

### Readiness: **GO** — developmental proposal-binding feasibility only

F01–F05 and F08–F12 equivalents all pass: originals untouched, population reconciled, proposals frozen and hashed before masking, policy semantics preserved, invariants automated, controls analytic, determinism verified, no leakage of state or mask.

**F06/F07 reported separately, as required.** A nontrivial varying proposal process **was** demonstrated: B2 produced all four types, varied within every state, and varied within **306 of 1,827 day clusters (16.7%)**, yielding an `I_CF` that fell strictly between the endpoints in this executed run. [corrected A18.2-R r2, E-1]

But B2 is **SIMULATED** and its thresholds have no established source. **What is structural is the bound `0 ≤ I_CF ≤ P(CAUTION)`, which holds for any valid single-type advisor on this fixed population under the original masks. B2's location inside that bound is NOT robust to its threshold choices** — a different configuration could attain either endpoint. The earlier wording, that "the ordering is robust", is withdrawn. [corrected A18.2-R r2, E-2; A18.2-R R-06]

### What this does and does not license

| | |
|---|---|
| **Supported** | Δ_L2 = P(CAUTION) is an **upper bound** on incremental proposal exclusion. Actual exclusion depends on the advisor's type distribution, which the conference never measured. The bound is attained only by an always-timing/duration advisor and is 0 for an always-Go/Delay advisor. |
| **Not supported** | Any claim about maritime safety, harm reduction, actual departure decisions, decision quality, human trust, certified thresholds, algorithmic novelty, or the appropriateness of excluding any proposal. |
| **Permanent limits** | Hindsight inputs — `decision_time_availability` UNKNOWN for 100% of cases (D-08). No protective-action truth for any of the four types. Wave band is a researcher length-to-tonnage transfer (A-03). Serial dependence (L-04). |
| **Warning placeholder** | `g_m` is pinned SAFE because authenticated issued-warning data were unavailable. **The v0.1 lower-bound claim is withdrawn.** Reintroducing authenticated warnings could alter occupancy and binding **non-monotonically**: a case moved from CAUTION to UNSAFE would *cease* to contribute to C1→C2 incremental binding, so `I_CF` could fall as well as rise, while total C2 exclusion could move differently again. The effect on the state mix and on each binding measure is **UNKNOWN** without authenticated warnings and a frozen integration rule. No general lower-bound interpretation is supported. [A18.2-R R-07] |

A18.2 demonstrates **proposal-dependent exclusion in a developmental hindsight simulation**, not correctness of admission or protective value. Proposals are **retrospective synthetic advisor outputs under a frozen deterministic SIMULATED rule** — not a validated maritime advisor, and not observed operational advice. B2's branch thresholds have no independent domain justification, so its exclusion rate is **process-specific**. Hourly cases cluster by day and no naive IID inferential claim is made. No observed vessel decisions, independent protective-action labels, operational forecasts or impacts are involved. Nothing in this folder asserts that any excluded proposal should have been excluded. [A18.2-R R-09, R-10]
