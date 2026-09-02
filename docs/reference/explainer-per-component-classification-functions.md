# Explainer: Per-Component Classification Functions (gᵢ)

**Type:** Author reading reference — plain-language + formal explanation  
**Relates to:** `docs/canonical/appendix-c-formalisation.md` Section C.2; manuscript Section 5.3  
**Date added:** 2026-08-09

---

## What are the gᵢ functions?

Each `gᵢ` is a **per-component classification function** — it takes one parameter from E and maps it to a safety state. There are six, one per component of E. Together they are the heart of how the safety state is determined.

---

## 1. Intuitive Explanation (Plain English)

Think of each environmental parameter as **voting** on how dangerous the conditions are.

| Parameter | What it measures | What it says |
|-----------|------------------|--------------|
| **g_w(w)** | Wind speed | "The wind is calm" (SAFE) / "The wind is strong" (CAUTION) / "The wind is extreme" (UNSAFE) |
| **g_r(r)** | Rain intensity | "It's drizzling" (SAFE) / "It's heavy rain" (CAUTION) / "It's a storm" (UNSAFE) |
| **g_m(m)** | Marine warning level | "No warnings" (SAFE) / "Be careful" (CAUTION) / "Serious warnings" (UNSAFE) |
| **g_o(o)** | Wave height | "The sea is flat" (SAFE) / "Moderate waves" (CAUTION) / "Huge waves" (UNSAFE) |
| **g_v(v)** | Vessel size | "Your boat is big" (SAFE) / "Your boat is small" (CAUTION) — *never UNSAFE alone* |
| **g_t(t)** | Time of day | "Daytime" (SAFE) / "Dusk" (CAUTION) / "Nighttime" (UNSAFE) |

Each function takes a **single input** (one component of E) and returns **one of three safety states**.

**The key insight:** No single parameter decides the final safety state alone. They all vote, and the **worst-case vote wins** (max_≻ aggregation). This is the "non-compensatory" principle — good weather cannot compensate for bad weather.

---

## 2. Formal Explanation (Mathematical Structure)

### What type of function is gᵢ?

Each gᵢ is a **total function** that maps its input domain to the set {SAFE, CAUTION, UNSAFE}:

```
g_w : ℝ≥0 → {SAFE, CAUTION, UNSAFE}
g_r : {none, light, moderate, heavy, storm} → {SAFE, CAUTION, UNSAFE}
g_m : {none, advisory, warning, alert} → {SAFE, CAUTION, UNSAFE}
g_o : ℝ≥0 → {SAFE, CAUTION, UNSAFE}
g_v : {small, medium, big} → {SAFE, CAUTION}        ← UNSAFE not in codomain
g_t : [0, 24) → {SAFE, CAUTION, UNSAFE}
```

**"Total" means:** Every possible input value maps to exactly one output. There are no undefined cases. This is what Theorem 5.1 (Totality of f) depends on — because if every gᵢ is total, then f(E) = max_≻ over all gᵢ is also total.

### How is each gᵢ defined internally?

Each gᵢ is a **piecewise function** defined by threshold intervals. For continuous parameters (w, o, t):

**g_w(w)**
```
g_w(w) = SAFE    if w ≤ 22
g_w(w) = CAUTION if 22 < w ≤ 27
g_w(w) = UNSAFE  if w > 27
```

**g_o(o)**
```
g_o(o) = SAFE    if o < 1.5
g_o(o) = CAUTION if 1.5 ≤ o ≤ 3.5
g_o(o) = UNSAFE  if o > 3.5
```

**g_t(t)** (note the wrap-around for UNSAFE)
```
g_t(t) = SAFE    if 6.0 ≤ t < 17.0
g_t(t) = CAUTION if 17.0 ≤ t < 19.0
g_t(t) = UNSAFE  if t ∈ [19.0, 24.0) ∪ [0.0, 6.0)
```

For categorical parameters (r, m, v), the function is a **lookup table**:

**g_r(r)**
```
g_r(none)     = SAFE
g_r(light)    = SAFE
g_r(moderate) = SAFE
g_r(heavy)    = CAUTION
g_r(storm)    = UNSAFE
```

### Why are the thresholds where they are?

| Parameter | Threshold basis |
|-----------|-----------------|
| w (wind) | MET Malaysia official warning criteria: Category 1 onset = 40 km/h (≈22 kn); Category 2 onset = 50 km/h (≈27 kn) |
| o (wave height) | Three-Tier Triangulation: hydrodynamic modelling (Yaakob et al. 2015), empirical risk analysis (Jeong & Im 2023), state policy (MET Malaysia Category 1 max = 3.5 m) |
| r (rain) | MET Malaysia operational definition: Ribut Petir (thunderstorm/cyclone) = unconditional halt |
| m (marine warning) | MET Malaysia three-tier warning system: none → advisory → warning → alert |
| v (vessel) | Vessel-size fatality gradient from 504 IMO accident reports (Dominguez-Péry et al. 2023) |
| t (time) | Night navigation risk: highest accident probability and consequence scores (Atacan & Düzbastılar 2023) |

### The special case: g_v

**g_v is unique** because its codomain is {SAFE, CAUTION} — it never returns UNSAFE.

```
g_v(big)    = SAFE
g_v(small)  = CAUTION
g_v(medium) = CAUTION
```

Why? Because **vessel category alone cannot make conditions UNSAFE**. A small boat in calm seas is still risky (CAUTION), but it is not inherently UNSAFE — that requires a combination with another parameter (e.g., high wind + small boat = UNSAFE via max_≻).

This is architecturally important: if g_v could return UNSAFE, then every small vessel would be UNSAFE in every condition, which is not operationally correct. The risk of small vessels is *contextual* — it depends on the weather.

---

## 3. Operational Explanation (Step-by-Step Runtime Evaluation)

### Example A — CAUTION scenario

Fisher requests a departure advisory. Layer 1 reads:

| Component | Value |
|-----------|-------|
| w | 25 kn |
| r | moderate |
| m | advisory |
| o | 2.0 m |
| v | small |
| t | 14.5 (14:30) |

Layer 2 evaluates each gᵢ:

| Function | Input | Output | Reason |
|----------|-------|--------|--------|
| g_w(25) | 25 kn | **CAUTION** | 22 < 25 ≤ 27 |
| g_r(moderate) | moderate | **SAFE** | moderate ∈ {none, light, moderate} |
| g_m(advisory) | advisory | **CAUTION** | advisory ∈ {advisory} |
| g_o(2.0) | 2.0 m | **CAUTION** | 1.5 ≤ 2.0 ≤ 3.5 |
| g_v(small) | small | **CAUTION** | small ∈ {small, medium} |
| g_t(14.5) | 14.5 | **SAFE** | 6.0 ≤ 14.5 < 17.0 |

Aggregation: f(E) = max_≻ {CAUTION, SAFE, CAUTION, CAUTION, CAUTION, SAFE} = **CAUTION**

Result: G(CAUTION) = 1, A_AI(CAUTION) = {Go, Delay}. Layer 3 receives RS(CAUTION). Advisory output: "Departure is possible — exercise caution."

---

### Example B — UNSAFE scenario (one parameter changes)

Same as above but w = 30 kn:

| Function | Input | Output |
|----------|-------|--------|
| g_w(30) | 30 kn | **UNSAFE** | 30 > 27 |
| (others) | — | SAFE / CAUTION |

Aggregation: f(E) = max_≻ {**UNSAFE**, SAFE, CAUTION, CAUTION, CAUTION, SAFE} = **UNSAFE**

Result: G(UNSAFE) = 0. Layer 3 not invoked. AI(E) = ∅. Advisory output: "Departure not recommended — conditions are unsafe."

**Key point:** One UNSAFE component dominates everything else. Extreme wind cannot be compensated by calm seas or a large vessel.

---

## 4. Why the Per-Component Functions Are Critical

| Reason | Explanation |
|--------|-------------|
| They establish the safety state | The entire governance mechanism depends on S = f(E). If any gᵢ is wrong, the entire architecture fails. |
| They encode domain expertise | Thresholds are derived from meteorological standards, hydrodynamic modelling, and empirical risk analysis — not arbitrary. |
| They are the formal basis for Theorem 5.1 | Because each gᵢ is total, f(E) is total. |
| They implement non-compensation | The worst-case aggregation rule (max_≻) is only meaningful because gᵢ produces a totally ordered output set. |
| They are the enforcement boundary | The Safety Dominance Property (Property 5.3) depends on Layer 2's correct evaluation of gᵢ. Misclassification → wrong RS(S) → governance failure. |

---

## 5. Summary Table: gᵢ at a Glance

| Function | Domain | SAFE | CAUTION | UNSAFE | Key citation |
|----------|--------|------|---------|--------|--------------|
| g_w | ℝ≥0 | ≤ 22 kn | 22–27 kn | > 27 kn | MET Malaysia (2026) |
| g_r | {none, light, moderate, heavy, storm} | none, light, moderate | heavy | storm | MET Malaysia (2026) |
| g_m | {none, advisory, warning, alert} | none | advisory | warning, alert | MET Malaysia (2026) |
| g_o | ℝ≥0 | < 1.5 m | 1.5–3.5 m | > 3.5 m | Jeong & Im (2023); Yaakob et al. (2015) |
| g_v | {small, medium, big} | big | small, medium | — (never) | Dominguez-Péry et al. (2023) |
| g_t | [0, 24) | 6.0 ≤ t < 17.0 | 17.0 ≤ t < 19.0 | [19.0, 24.0) ∪ [0.0, 6.0) | Atacan & Düzbastılar (2023) |

---

## 6. What This Means for the Paper

When Section 5.3.2 defines the per-component classification functions, it is simultaneously doing four things:

1. **Formally defining** the classification functions (mathematical precision → Section 6 proofs)
2. **Empirically justifying** the thresholds (scientific credibility → Section 5.3.2 citations)
3. **Enabling the proofs** in Section 6 (Theorem 5.1 Totality, Theorem 5.2 Monotonicity)
4. **Specifying the implementation** for Section 9 (prototype rule sets RS(SAFE), RS(CAUTION))

This is why Section 5.3.2 is dense — it is doing multiple jobs at once.
