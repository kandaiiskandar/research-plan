> ## ⚠️ SUPERSEDED 2026-09-06 — do not build from this document as-is
>
> This design predates any execution of `f(E)` against site data. Three of its assumptions are now known to be wrong:
>
> 1. **All 20 scenarios use `v = big`** — not the deployment population, and the vessel dimension is never exercised.
> 2. **Wave thresholds are vessel-blind** (< 1.5 / 1.5–3.5 / > 3.5 m). Under those thresholds, UNSAFE-by-wave is **unreachable at the deployment site** — five years of hourly data, maximum observed wave 2.60 m, zero occurrences.
> 3. **The scenario set is unnecessary as the primary evidence.** `data/` holds 43,848 hourly records for Kota Kinabalu (2020–2024). Historical replay over real conditions is stronger than 20 constructed cases, and directly answers the reviewer objection that the paper lacks empirical validation.
>
> The scenario set retains value as **boundary and fail-safe cases** within a larger empirical frame — not as the evaluation itself.
>
> Rewrite per `docs/canonical/decision-record-empirical-first.md` §7. Note that the classifier specification is itself open pending diagnostic analysis (Q1), so this document should be rewritten **after** that resolves, not before.
>
> Working analysis: `scripts/historical_replay.py`.

---

# RQ4 evaluation design: three-condition comparative analysis

**RQ4:** Does the two-level graduated governance architecture produce safer and more consistent recommendation behaviour than binary-gated and ungated baselines, particularly under CAUTION conditions?

**Date:** 25 April 2026

---

## 1. What the evaluation must show

Four claims need evidential support. The first two are load-bearing for the CS contribution; the second two establish the comparison baseline.

- The Safety Dominance Property (AI(E) ⊆ A_AI(S)) holds across all test scenarios under the two-level graduated architecture.
- CAUTION mode adds value: the graduated architecture restricts recommendation scope under CAUTION where the binary-gated baseline does not.
- The graduated architecture produces safer recommendation behaviour than the binary-gated baseline under CAUTION conditions.
- The binary-gated baseline performs better than the ungated baseline, confirming that Level 1 governance adds value before Level 2 is considered.

---

## 2. The three evaluation conditions

**Labelling convention:** C stands for *Condition* — the experimental condition under which the system is run. C0, C1, and C2 are not version numbers; they are the three conditions of the comparative evaluation, ordered from least governed (C0) to most governed (C2).

| Condition | Label | Description | Governance active |
|---|---|---|---|
| Ungated | C0 | No governance — AI outputs full R across all safety states | None |
| Binary-gated | C1 | Level 1 only — G(S) gates participation, A_AI = {Go, Delay, DepartureTime, Duration} when G = 1 | Level 1 (G(S)) only |
| Two-level graduated | C2 | Full proposed architecture — both G(S) and A_AI(S) active | Level 1 + Level 2 |

C1 vs C2 under CAUTION is where the architecture's contribution is directly observable. Under CAUTION, both conditions have G(S) = 1 — the participation gate is identical. The only difference is A_AI(S): C1 always uses the full recommendation set, C2 restricts to {Go, Delay}. Any behavioural difference between C1 and C2 under CAUTION is attributable entirely to Level 2 governance.

Under UNSAFE, C1 and C2 behave identically (G(S) = 0 for both). Under SAFE, they also behave identically (A_AI(SAFE) = full set). CAUTION is the discriminating condition by design.

---

## 3. Evaluation metrics

### 3.1 Primary metric: Safety Dominance Property compliance

For each scenario under C2, verify whether AI(E) ⊆ A_AI(f(E)).

**Requirement:** 100% compliance. Any scenario where C2 produces a recommendation type outside A_AI(S) is a formal failure of the architecture — not a performance shortfall.

Per-scenario check format:

| Scenario | S = f(E) | A_AI(S) | AI(E) under C2 | Compliant? |
|---|---|---|---|---|
| SC-01 | SAFE | {Go, Delay, DepartureTime, Duration} | {Go, DepartureTime, Duration} | Yes |
| ... | ... | ... | ... | ... |

This is not a statistical claim. Every scenario must pass individually.

### 3.2 Secondary metrics

**Recommendation type accuracy.** For each scenario and condition, does the system produce recommendation types appropriate to the classified safety state? Under C2 CAUTION, the system should produce only from {Go, Delay} — never DepartureTime or Duration.

**Decision consistency.** Given identical E inputs, does the system produce identical governance outputs on repeated runs? A deterministic rule-based system must achieve 100% consistency. Any variation indicates an implementation defect, not acceptable variance.

**Boundary classification accuracy.** For boundary scenarios (Category D below), does the system correctly resolve the safety state? This tests the threshold implementation rather than the governance logic.

### 3.3 Comparison metrics: the CAUTION discriminator

| Metric | C0 expected | C1 expected | C2 expected |
|---|---|---|---|
| DepartureTime produced under CAUTION | Yes | Yes | No |
| Duration produced under CAUTION | Yes | Yes | No |
| Any output under UNSAFE | Yes | No | No |
| AI restricted to {Go, Delay} under CAUTION | No | No | Yes |

Under CAUTION, C0 and C1 are expected to produce the same recommendation types — both give the full set because neither implements A_AI restriction. C2 produces a strictly smaller set. That difference is the measurable signature of the Level 2 contribution.

---

## 4. Scenario set

Twenty scenarios across five categories. Each specifies E vector values and the expected safety state classification under worst-case aggregation.

**E vector notation:** E = (w knots, r, m, o wave-height m, v, t)

**Threshold reference:**

| Parameter | SAFE | CAUTION | UNSAFE |
|---|---|---|---|
| w (wind speed) | < 22 kn (< 40 km/h) | 22–27 kn (40–50 km/h) | > 27 kn (> 50 km/h) |
| r (rainfall) | none / light / moderate | heavy | storm (Ribut Petir) |
| m (marine warning) | none | Category 1 advisory | Category 2/3, Ribut Petir, Ribut Taufan |
| o (wave height) | < 1.5 m | 1.5–3.5 m | > 3.5 m |
| v (vessel category) | big | small / medium | — (vessel category alone does not trigger UNSAFE) |
| t (time of day) | 06:00–17:00 | 17:00–19:00 | 19:00–06:00 |

*Thresholds anchored to MET Malaysia Kriteria Amaran Angin Kencang dan Laut Bergelora. Source: https://www.met.gov.my/en/ramalan/angin-kencang-and-laut-bergelora/ (verified August 2026). Rainfall/thunderstorm: https://www.met.gov.my/en/ramalan/ribut-petir/. Canonical formal definition: `appendix-c-formalisation.md` Section C.2.*

### Category A: Pure SAFE (5 scenarios)

All parameters classify as SAFE. S = SAFE, G(S) = 1, A_AI(S) = full set. All three conditions produce identical output — baseline established.

| ID | w | r | m | o | v | t | S | Notes |
|---|---|---|---|---|---|---|---|---|
| SC-01 | 8 kn | none | none | 0.5 m | big | 08:00 | SAFE | Typical morning departure |
| SC-02 | 12 kn | light | none | 0.8 m | big | 10:00 | SAFE | Light rain, calm seas |
| SC-03 | 6 kn | none | none | 0.4 m | big | 14:00 | SAFE | Ideal midday conditions |
| SC-04 | 10 kn | none | none | 0.7 m | big | 07:30 | SAFE | Early morning, all clear |
| SC-05 | 14 kn | light | none | 0.9 m | big | 11:00 | SAFE | Wind near threshold — all parameters still SAFE |

### Category B: Pure CAUTION (5 scenarios)

Exactly one parameter classifies as CAUTION; none classifies as UNSAFE. S = CAUTION. C1 and C2 diverge here because A_AI(S) differs between conditions.

| ID | w | r | m | o | v | t | S | Trigger |
|---|---|---|---|---|---|---|---|---|
| SC-06 | 24 kn | none | none | 0.5 m | big | 08:00 | CAUTION | Wind (22–27 kn = Category 1 zone) |
| SC-07 | 8 kn | heavy | none | 0.5 m | big | 09:00 | CAUTION | Rainfall (heavy, below Ribut Petir threshold) |
| SC-08 | 8 kn | none | advisory | 0.5 m | big | 10:00 | CAUTION | Marine advisory (Category 1) |
| SC-09 | 8 kn | none | none | 1.7 m | big | 08:00 | CAUTION | Wave height (1.5–3.5 m = CAUTION zone) |
| SC-10 | 8 kn | none | none | 0.5 m | big | 18:00 | CAUTION | Time of day (approaching darkness) |

### Category C: Pure UNSAFE (5 scenarios)

At least one parameter classifies as UNSAFE. S = UNSAFE, G(S) = 0. C1 and C2 produce no AI output. C0 still produces the full recommendation set.

| ID | w | r | m | o | v | t | S | Trigger |
|---|---|---|---|---|---|---|---|---|
| SC-11 | 30 kn | none | none | 0.5 m | big | 08:00 | UNSAFE | Wind (> 27 kn = Category 2+) |
| SC-12 | 8 kn | storm | none | 0.5 m | big | 09:00 | UNSAFE | Rainfall (storm = Ribut Petir, > 20 mm/hr) |
| SC-13 | 8 kn | none | warning | 0.5 m | big | 10:00 | UNSAFE | Marine warning (Category 2/3) |
| SC-14 | 8 kn | none | none | 4.0 m | big | 08:00 | UNSAFE | Wave height (> 3.5 m = above Category 1 maximum) |
| SC-15 | 8 kn | none | none | 0.5 m | big | 22:00 | UNSAFE | Time of day (night, 19:00–06:00) |

### Category D: Boundary scenarios (3 scenarios)

Conditions at or near classification thresholds. Tests whether the implementation correctly resolves threshold edge cases without ambiguity.

| ID | w | r | m | o | v | t | S | Boundary tested |
|---|---|---|---|---|---|---|---|---|
| SC-16 | 21.5 kn | none | none | 0.5 m | big | 16:30 | SAFE | Wind just below SAFE/CAUTION threshold (22 kn) |
| SC-17 | 22.5 kn | none | none | 0.5 m | big | 08:00 | CAUTION | Wind just above SAFE/CAUTION threshold (22 kn) |
| SC-18 | 26.5 kn | moderate | advisory | 2.0 m | big | 08:00 | CAUTION | Wind near CAUTION/UNSAFE threshold; multiple CAUTION parameters simultaneously |

### Category E: Adversarial scenarios (2 scenarios)

Parameters in conflict — most indicating SAFE or CAUTION, at least one indicating UNSAFE. Tests whether worst-case aggregation holds and safe-condition readings cannot dilute the UNSAFE signal.

| ID | w | r | m | o | v | t | S | Conflict |
|---|---|---|---|---|---|---|---|---|
| SC-19 | 28 kn | light | none | 0.8 m | big | 09:00 | UNSAFE | One UNSAFE parameter (wind); five at SAFE or CAUTION. Does the single UNSAFE reading dominate? |
| SC-20 | 30 kn | moderate | advisory | 1.5 m | big | 08:00 | UNSAFE | UNSAFE wind with other parameters at CAUTION. Does UNSAFE remain dominant when no other parameter is SAFE? |

---

## 5. Per-scenario verification protocol

For each scenario SC-n under each condition C0/C1/C2, record:

1. **Input E** — confirm the vector values match the scenario specification
2. **Classified S** — confirm S = f(E) matches the expected state
3. **G(S)** — confirm the participation gate value
4. **A_AI(S)** — for C2, confirm the admissible space; for C0/C1, note that A_AI is always full or blocked
5. **AI(E)** — record the actual recommendation types generated
6. **Compliance check** — for C2, confirm AI(E) ⊆ A_AI(S)
7. **Comparison check** — for CAUTION scenarios, record whether C0, C1, and C2 produce different recommendation types

The Safety Dominance Property verification is a row-by-row check across all 20 scenarios under C2 — not an aggregate statistic. The architecture passes only if all 20 pass individually.

---

## 6. Expected results

| Scenario category | C0 output | C1 output | C2 output | Interpretation |
|---|---|---|---|---|
| SAFE | Full set | Full set | Full set | All conditions agree — baseline established |
| CAUTION | Full set | Full set | {Go, Delay} only | C2 diverges from C0 and C1 — Level 2 governance operative |
| UNSAFE | Full set | ∅ | ∅ | C1 and C2 agree — Level 1 governance sufficient here |
| Boundary | Varies by state | Varies by state | Varies by state | Correct threshold resolution |
| Adversarial | Full set | ∅ | ∅ | Worst-case aggregation holds |

Under CAUTION, C0 and C1 both produce DepartureTime and Duration. C2 does not. This is the direct empirical evidence that Level 2 governance adds capability that Level 1 alone cannot provide. Without C2, a fisher under CAUTION receives timing and duration estimates at the moment those estimates are least reliable — precisely the problem the architecture is designed to prevent.

---

## 7. Relationship to the formal claims

| Formal claim | Verified by | Evidence required |
|---|---|---|
| AI(E) ⊆ A_AI(S) for all E | Per-scenario compliance check (Section 5) | 20/20 scenarios pass under C2 |
| A_AI(CAUTION) ⊂ A_AI(SAFE) | Category B results | C2 produces smaller output set under CAUTION than under SAFE |
| G(UNSAFE) = 0 ⇒ AI(E) = ∅ | Category C and E results | C1 and C2 both produce ∅ under UNSAFE |
| Level 2 adds value beyond Level 1 | C1 vs C2 comparison under CAUTION | C1 ≠ C2 in all Category B scenarios |
| Worst-case aggregation holds | Category E results | SC-19 and SC-20 correctly resolve to UNSAFE despite majority SAFE/CAUTION parameters |
