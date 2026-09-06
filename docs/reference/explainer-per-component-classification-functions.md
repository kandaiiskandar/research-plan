# Explainer: Per-Component Classification Functions

**Type:** Author reading reference — plain-language + formal explanation
**Relates to:** `docs/canonical/appendix-c-formalisation.md` Section C.2; manuscript Section 5.3
**Date added:** 2026-08-09
**Last revised:** 2026-09-06 — `g_v` removed; `g_o` parameterised by vessel category. See Section 7.

---

## What are the classification functions?

Each classification function takes one condition from E and maps it to a safety state. There are **five** of them — one for each *condition* variable. Together they determine the safety state.

The sixth component of E, vessel category `v`, is different in kind: it is not a condition that changes, and it does not classify on its own. It **parameterises** the ocean state function. Section 2 explains why.

---

## 1. Intuitive Explanation (Plain English)

Think of each environmental condition as **voting** on how dangerous things are right now.

| Function | What it measures | What it says |
|-----------|------------------|--------------|
| **g_w(w)** | Wind speed | "The wind is calm" (SAFE) / "The wind is strong" (CAUTION) / "The wind is extreme" (UNSAFE) |
| **g_r(r)** | Rain intensity | "It's drizzling" (SAFE) / "It's heavy rain" (CAUTION) / "It's a storm" (UNSAFE) |
| **g_m(m)** | Marine warning level | "No warnings" (SAFE) / "Be careful" (CAUTION) / "Serious warnings" (UNSAFE) |
| **g_o(o, v)** | Wave height, **for this boat** | "The sea is fine for this vessel" (SAFE) / "Getting marginal for this vessel" (CAUTION) / "Beyond this vessel" (UNSAFE) |
| **g_t(t)** | Time of day | "Daytime" (SAFE) / "Dusk" (CAUTION) / "Nighttime" (UNSAFE) |

**The key insight:** no single condition decides alone. They all vote, and the **worst vote wins** (max_≻ aggregation). This is the "non-compensatory" principle — good weather cannot compensate for bad weather.

**The second key insight:** `g_o` asks a different question from the others. Not "are the waves big?" but "are the waves big *for this boat*?" A 1.2 m sea is unremarkable for a 20 m vessel and marginal for a 6 m one. The same water, a different answer.

---

## 2. Formal Explanation (Mathematical Structure)

### Function signatures

```
g_w : ℝ≥0                                        → {SAFE, CAUTION, UNSAFE}
g_r : {none, light, moderate, heavy, storm}      → {SAFE, CAUTION, UNSAFE}
g_m : {none, advisory, warning, alert}           → {SAFE, CAUTION, UNSAFE}
g_o : (ℝ≥0 × ℝ≥0) × {small, medium, big}         → {SAFE, CAUTION, UNSAFE}
g_t : [0, 24)                                    → {SAFE, CAUTION, UNSAFE}
```

Aggregation:

```
f(E) = max_≻ {g_w(w), g_r(r), g_m(m), g_o(o, v), g_t(t)}
```

Five terms. `v` appears inside `g_o`, not as a separate argument to the maximum.

**"Total" means:** every possible input maps to exactly one output — no undefined cases. This is what Theorem C.1 (Totality of f) depends on: if every classification function is total, then `f(E)` is total.

### How each is defined internally

Threshold intervals for the continuous variables:

**g_w(w)**
```
g_w(w) = SAFE    if w ≤ 22
g_w(w) = CAUTION if 22 < w ≤ 27
g_w(w) = UNSAFE  if w > 27
```

**g_t(t)** — note the wrap-around for UNSAFE
```
g_t(t) = SAFE    if 6.0 ≤ t < 17.0
g_t(t) = CAUTION if 17.0 ≤ t < 19.0
g_t(t) = UNSAFE  if t ∈ [19.0, 24.0) ∪ [0.0, 6.0)
```

Lookup tables for the categorical variables:

**g_r(r)**
```
g_r(none) = g_r(light) = g_r(moderate) = SAFE
g_r(heavy)                             = CAUTION
g_r(storm)                             = UNSAFE
```

**g_m(m)**
```
g_m(none)                = SAFE
g_m(advisory)            = CAUTION
g_m(warning) = g_m(alert) = UNSAFE
```

### The parameterised one: g_o(o, v)

`g_o` is a **family of three threshold functions**, selected by vessel category:

| v (GRT) | SAFE | CAUTION | UNSAFE |
|---|---|---|---|
| small (< 10) | o < 1.0 m | 1.0 ≤ o ≤ 1.25 m | o > 1.25 m |
| medium (10–25) | o < 1.4 m | 1.4 ≤ o ≤ 2.8 m | o > 2.8 m |
| big (> 25) | o < 1.5 m | 1.5 ≤ o ≤ 3.5 m | o > 3.5 m |

Read it as: pick the row for the vessel, then apply that row's thresholds to the wave height.

**Why the wave height only?** `o` is formally a tuple `(wave height, swell period)`. Classification uses the height component; swell period is carried in the state representation but not used. This is a known limitation — encounter period relative to hull natural period genuinely matters for seakeeping, and the model cannot currently distinguish a short-period wind sea from a long-period swell at the same significant height. See appendix-c C.9.3.

**Why is `v` a parameter and not its own function?** This is the important structural point.

A prior version of the model defined `g_v(v)` returning CAUTION for small and medium vessels, contributing to the maximum like any other term. That does not work, and the reason is worth internalising:

> **A constant term inside a maximum is a floor. It cannot shift a threshold.**

If `g_v(small) = CAUTION` always, then `f(E) ≥ CAUTION` always — the output is floored. But the *boundary* between CAUTION and UNSAFE is set entirely by the other functions, and none of them know the vessel size. So a 5 m boat and a 20 m boat would be declared UNSAFE at precisely the same wave height (3.5 m) and the same wind speed (27 kn).

That contradicts the evidence. Yaakob et al. (2015) [[notes]](../../notes/Stability%2C%20Seakeeping%20and%20Safety%20Assessment%20of%20Small%20Fishing%20Boats%20Operating%20in%20Southern%20Coast%20of%20Peninsular%20Malaysia.md) report a 6.54 m Malaysian vessel with an operational ceiling of Hs ≈ 1.25 m — under a third of the wave height at which the old model would have called it UNSAFE.

Parameterising `g_o` by `v` shifts the boundary, which is what the physics requires. A floor cannot do this; a parameter can.

### Why the thresholds are where they are

| Function | Threshold basis |
|-----------|-----------------|
| g_w | MET Malaysia warning criteria: Category 1 onset = 40 km/h (≈22 kn); Category 2 onset = 50 km/h (≈27 kn) |
| g_r | MET Malaysia operational definition: Ribut Petir (thunderstorm) = unconditional halt |
| g_m | MET Malaysia three-tier warning system: none → advisory → warning → alert |
| g_o (big) | MET Malaysia Category 1 max (3.5 m); Jeong & Im (2023) [[notes]](../../notes/Proposal%20of%20Restrictions%20on%20the%20Departure%20of%20Korea%20Small%20Fishing%20Vessel%20according%20to%20Wave%20Height.md) Hs_KIMO = 1.58 m at 16 m LOA |
| g_o (small) | Jeong & Im Table 12: vessels ≤10 m restricted at Hs ≥ 1.0 m → CAUTION onset; Yaakob et al. 6.54 m vessel **operational ceiling 1.25 m** (top of SS3, last passing band) → UNSAFE |
| g_o (medium) | Hs_KIMO across 10–15 m LOA = 1.13–1.48 m; UNSAFE boundary interpolated |
| g_t | Night navigation risk: highest accident probability and consequence scores — Atacan & Düzbastılar (2023) [[notes]](../../notes/Determination%20of%20risk%20perception%20in%20small-scale%20fishing%20and%20navigation.md) |

Vessel category itself is grounded in Dominguez-Péry et al. (2023) [[notes]](../../notes/A%20holistic%20view%20of%20maritime%20navigation%20accidents%20and%20risk%20indicators-%20examining%20IMO%20reports%20from%202011%20to%202021.md) — small vessels carry the highest mean fatality rank (3.67, p = 0.01), which justifies setting their thresholds conservatively.

Two values are **design decisions rather than sourced numbers**: the small-vessel UNSAFE boundary (1.25 m) treats Yaakob's operational ceiling as a departure gate, which the paper does not itself claim; and the medium-vessel UNSAFE boundary (2.8 m) is interpolated with no direct source. Both are recorded in appendix-c C.9.1. *The small-vessel value was amended from 1.9 m on 2026-09-06 — the prior value used Yaakob's failure point rather than his operational ceiling.*

---

## 3. Operational Explanation (Step-by-Step Runtime Evaluation)

### Example A — SAFE, small vessel

A calm morning. Fisher with a 6 m boat (< 10 GRT) requests a departure advisory.

| Component | Value |
|-----------|-------|
| w | 8 kn |
| r | none |
| m | none |
| o | 0.5 m |
| v | small |
| t | 08:00 |

| Function | Input | Output | Reason |
|----------|-------|--------|--------|
| g_w(8) | 8 kn | **SAFE** | 8 ≤ 22 |
| g_r(none) | none | **SAFE** | none ∈ {none, light, moderate} |
| g_m(none) | none | **SAFE** | no active warning |
| g_o(0.5, small) | 0.5 m, small | **SAFE** | 0.5 < 1.0 (small row) |
| g_t(8.0) | 8.0 | **SAFE** | 6.0 ≤ 8.0 < 17.0 |

f(E) = max_≻ {SAFE, SAFE, SAFE, SAFE, SAFE} = **SAFE**

G(SAFE) = 1, A_AI(SAFE) = {Go, Delay, DepartureTime, Duration}. Full advisory scope.

> **Note:** this outcome was *impossible* under the superseded model — `g_v(small) = CAUTION` floored every small vessel at CAUTION regardless of conditions. Restoring reachable SAFE for the deployment population is what makes the three-state architecture observable in the target domain.

---

### Example B — CAUTION, same vessel, worse sea

Same boat, same day, larger swell.

| Component | Value |
|-----------|-------|
| w | 10 kn |
| r | none |
| m | none |
| o | **1.5 m** |
| v | small |
| t | 08:00 |

| Function | Output | Reason |
|----------|--------|--------|
| g_w(10) | SAFE | 10 ≤ 22 |
| g_r(none) | SAFE | — |
| g_m(none) | SAFE | — |
| g_o(1.5, small) | **CAUTION** | 1.0 ≤ 1.5 ≤ 1.9 (small row) |
| g_t(8.0) | SAFE | — |

f(E) = **CAUTION**. A_AI(CAUTION) = {Go, Delay}. DepartureTime and Duration withheld.

---

### Example C — UNSAFE by wave height alone

Same boat, distant-storm swell, no wind, no warning issued.

| Component | Value |
|-----------|-------|
| w | 10 kn |
| r | none |
| m | none |
| o | **2.5 m** |
| v | small |
| t | 08:00 |

| Function | Output | Reason |
|----------|--------|--------|
| g_o(2.5, small) | **UNSAFE** | 2.5 > 1.9 (small row) |
| (all others) | SAFE | — |

f(E) = **UNSAFE**. G = 0, AI(E) = ∅.

> **This is the case the superseded model got wrong.** With `g_o` vessel-blind, 2.5 m fell in [1.5, 3.5] = CAUTION, and `g_v(small) = CAUTION` added nothing further — so a 6 m boat in a 2.5 m sea received "Go, with caution." Jeong & Im's finding that **82% of capsizings occurred on days with no weather warning** is precisely this scenario: swell without wind, no institutional alert, and a vessel-blind threshold that misses it.

---

### Example D — the same sea, three different vessels

Conditions held constant at o = 2.5 m; everything else SAFE.

| v | g_o(2.5, v) | f(E) | A_AI(S) |
|---|---|---|---|
| small | **UNSAFE** | UNSAFE | ∅ |
| medium | CAUTION | CAUTION | {Go, Delay} |
| big | CAUTION | CAUTION | {Go, Delay} |

Same water, three governance outcomes. Under the superseded model all three rows read CAUTION.

---

### Example E — one UNSAFE condition dominates

Small vessel, calm sea, but extreme wind.

| Function | Output |
|----------|--------|
| g_w(30) | **UNSAFE** (30 > 27) |
| g_o(0.5, small) | SAFE |
| (others) | SAFE |

f(E) = **UNSAFE**. One UNSAFE condition dominates everything else — extreme wind cannot be compensated by a calm sea. This is the non-compensatory principle.

---

## 4. Why These Functions Are Critical

| Reason | Explanation |
|--------|-------------|
| They establish the safety state | The entire governance mechanism depends on S = f(E). If any classification function is wrong, the architecture fails. |
| They encode domain expertise | Thresholds derive from meteorological standards, hydrodynamic modelling, and empirical accident analysis — not arbitrary choices. |
| They are the formal basis for Theorem C.1 | Because each is total, f(E) is total. |
| They implement non-compensation | max_≻ is only meaningful because each function produces values in a totally ordered set. |
| They are the enforcement boundary | The Safety Dominance Property depends on Layer 2 classifying correctly. Misclassification → wrong RS(S) → governance failure. |
| **g_o carries the vessel model** | Vessel size affects safety *only* through `g_o`. If that parameterisation is wrong, vessel size is effectively ignored. |

---

## 5. Summary Table

| Function | Domain | SAFE | CAUTION | UNSAFE | Key citation |
|----------|--------|------|---------|--------|--------------|
| g_w | ℝ≥0 | ≤ 22 kn | 22–27 kn | > 27 kn | MET Malaysia |
| g_r | {none…storm} | none, light, moderate | heavy | storm | MET Malaysia |
| g_m | {none…alert} | none | advisory | warning, alert | MET Malaysia |
| g_o (small) | ℝ≥0 × {v} | < 1.0 m | 1.0–1.25 m | > 1.25 m | Jeong & Im; Yaakob et al. |
| g_o (medium) | ℝ≥0 × {v} | < 1.4 m | 1.4–2.8 m | > 2.8 m | Jeong & Im (Hs_KIMO) |
| g_o (big) | ℝ≥0 × {v} | < 1.5 m | 1.5–3.5 m | > 3.5 m | MET Malaysia; Jeong & Im |
| g_t | [0, 24) | 6.0–17.0 | 17.0–19.0 | 19.0–24.0 ∪ 0.0–6.0 | Atacan & Düzbastılar |

**Fail-safe:** if any component of E is undefined or corrupted (xᵢ = ⊥), f(E) = UNSAFE before any classification function is evaluated.

---

## 6. What This Means for the Paper

When Section 5.3 defines the classification functions, it is doing four things at once:

1. **Formally defining** them — mathematical precision, feeding the Section 6 proofs
2. **Empirically justifying** the thresholds — scientific credibility, via the Section 5.3.2 citations
3. **Enabling the proofs** — Theorem 6.1 (Totality) depends on each function being total
4. **Specifying the implementation** — the prototype rule sets in Section 9

This is why Section 5.3 is dense: it carries four jobs simultaneously.

---

## 7. What Changed on 2026-09-06

The model previously had **six** classification functions including `g_v(v) → {SAFE, CAUTION}`, with `f(E)` a maximum over six terms.

**Removed** because a constant term in a maximum floors the output but cannot shift a threshold. Under that formulation vessel category had no effect whatsoever on the CAUTION/UNSAFE boundary — all vessel sizes were declared UNSAFE at identical wave heights and wind speeds, under-classifying small-vessel risk across the entire 1.5–3.5 m band where the CAUTION mode is meant to operate. A secondary consequence was that SAFE became unreachable for any vessel under 25 GRT, i.e. for the entire deployment population, which made the architecture's central containment claim unobservable in-domain.

**Replaced by** parameterising `g_o(o, v)`, which implements the vessel effect as a threshold shift.

Full rationale: `docs/canonical/appendix-c-formalisation.md` C.2, "Note: there is no g_v", and `docs/superpowers/plans/2026-09-06-formal-model-and-evaluation-realignment.md`.

⚠️ `notes/Stability, Seakeeping and Safety Assessment...md` §4.2 still argues for the superseded design. Treat that section as historical; the seakeeping data it reports remains valid.
