# A18.2 — Counterfactual Proposal Binding: Execution Report

**Experiment `M1dQ-A18.2-CFB-v0.1` · 21 November 2026**
Developmental hindsight-replay extension. **The accepted AAI2026 experiment, its data, scripts and results are unmodified and unrepublished.**

Original repo at git `6c8d783`. All eight frozen inputs byte-identical before and after.

---

## 1. What this experiment measures, and why it is a different quantity

A18.1 Steps 3 and 4 established that the conference headline Δ_L2 = 5.81% is **identically P(S = CAUTION)** — a set-divergence between policy masks, verified exact at integer level. The replay contains **no advisor proposal generator**, so no recommendation was ever actually withheld from anyone.

A18.2 adds the missing half. It generates **frozen synthetic proposals**, one recommendation type per grid-hour, **before** any mask is consulted, then counts how many are actually excluded. That is a different estimand from set divergence and must not be conflated with it.

---

## 2. Headline result

**The conference 5.81% is a ceiling, not a measurement.**

| Advisor | I_CF numerator / denominator | I_CF |
|---|---:|---:|
| B1-CONST-**Go** | 0 / 9,135 | **0.0000%** |
| B1-CONST-**Delay** | 0 / 9,135 | **0.0000%** |
| B2-FROZEN-VARYING | 227 / 9,135 | **2.4849%** |
| B1-CONST-**DepartureTime** | 531 / 9,135 | **5.8128%** |
| B1-CONST-**Duration** | 531 / 9,135 | **5.8128%** |

`I_CF` is incremental intermediate binding: a valid proposal **admitted by C1 but excluded by C2**.

An advisor that only ever proposes `Go` or `Delay` is **never** incrementally restricted, even though the gate reports 5.81% set divergence over the identical hours. The 5.81% figure is reached **only** by an advisor that always proposes `DepartureTime` or `Duration`. A plausible varying advisor lands at **2.48%, less than half the ceiling**.

This follows directly from the contract — `RESTRICTED = {Go, Delay}` keeps both departure types, so only timing and duration proposals can ever be incrementally excluded — but it had never been **measured** before, because no proposals existed.

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

## 9. Table G — Nondegeneracy and leakage

| Check | Result |
|---|---|
| B2 distinct types produced | **4 of 4** — non-degenerate output |
| Type entropy | 0.9558 bits of a possible 2.0 |
| Distinct types within each state | SAFE 4, CAUTION 3, UNSAFE 4 — variation survives conditioning on state |
| Day-clusters with >1 type | 1,606 of 1,827 |
| B2 reads state / mask / allowed_set / any gate feature | **NO** — source-inspected (T12) |
| Pearson r, gusts vs gate `wind_speed` | 0.9165 |
| Pearson r, `wave_period` vs gate `wave_height` | 0.6349 |
| Best single-threshold accuracy predicting UNSAFE, gusts | 0.6063 |
| Best single-threshold accuracy predicting UNSAFE, `wave_period` | 0.6182 |

Gusts correlate strongly with the gate's wind variable, as physics requires. That is **shared physical drivers, not leakage** — and the proxy test settles it: neither feature predicts UNSAFE better than 0.62 accuracy, far from the 1.0 that a state proxy would show. Logged as a caveat in `09_invalid_inputs_and_leakage_register.csv` (LK-01 … LK-05).

**No post-hoc tuning.** The contract hash predates the experiment script; the proposal ledger was hashed (`2ff9020f4b3f91ff…`) before any mask was indexed, and a full re-run reproduced it byte-identically.

---

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

**F06/F07 reported separately, as required.** A nontrivial varying proposal process **was** demonstrated: B2 produced all four types, varied within every state and within 1,606 of 1,827 day clusters, and yielded an I_CF strictly between the Go/Delay floor and the timing/duration ceiling. But B2 is **SIMULATED**. Its thresholds have no established source, so **what is robust is the ordering, not the level**.

### What this does and does not license

| | |
|---|---|
| **Supported** | Δ_L2 = P(CAUTION) is an **upper bound** on incremental proposal exclusion. Actual exclusion depends on the advisor's type distribution, which the conference never measured. The bound is attained only by an always-timing/duration advisor and is 0 for an always-Go/Delay advisor. |
| **Not supported** | Any claim about maritime safety, harm reduction, actual departure decisions, decision quality, human trust, certified thresholds, algorithmic novelty, or the appropriateness of excluding any proposal. |
| **Permanent limits** | Hindsight inputs — `decision_time_availability` UNKNOWN for 100% of cases (D-08). No protective-action truth for any of the four types. `g_m` pinned SAFE, so every count is a lower bound (D-05). Wave band is a researcher length-to-tonnage transfer (A-03). Serial dependence (L-04). |

Proposals here are **retrospective synthetic advisor outputs under a simulated rule**, not observed operational advice. Nothing in this folder asserts that any excluded proposal should have been excluded.
