# Threshold Sensitivity Analysis of the Headline Empirical Result

**Date:** 2026-09-21
**Script:** `scripts/sensitivity/threshold_sensitivity.py` (new; imports `canonical_gt`, reads canonical sea-cell data only)
**Governance mappings frozen.** `G(S)` and `A_AI(S)` unchanged; `A_AI(CAUTION) = {Go, Delay}` unchanged.
**Canonical report:** **UNCHANGED.**

---

## A. Baseline reproduction

| | PRIMARY | RESOLUTION |
|---|---|---|
| Records | 43,848 | 28,501 |
| Departure-window denominator (05:00–09:00) | 9,135 | 5,935 |
| **Δ_L2 (admissible-set divergence C1↔C2)** | **5.81%** | **4.48%** |
| P(SAFE) | 51.31% | 54.44% |
| P(CAUTION) | 5.81% | 4.48% |
| P(UNSAFE) | 42.88% | 41.08% |

Baseline reproduces the canonical values exactly. Sensitivity analysis proceeds.

---

## B. Identity check

Verified **from the implementation**, not the documentation. In `condition_comparison.py`:

```
A_AI["C1"] = {SAFE: FULL, CAUTION: FULL,       UNSAFE: EMPTY}
A_AI["C2"] = {SAFE: FULL, CAUTION: RESTRICTED, UNSAFE: EMPTY}
```

The tables agree at SAFE (FULL = FULL) and at UNSAFE (∅ = ∅), and differ at CAUTION (FULL ≠ {Go, Delay}). Divergence is counted elementwise, so a departure-window hour contributes to C1↔C2 divergence **iff** its state is CAUTION.

Computed independently in the sensitivity script by evaluating the admissible-set tables per hour and comparing against the CAUTION count:

> **PRIMARY: Δ_L2 = 5.81%, P(CAUTION) = 5.81% — IDENTITY HOLDS (difference < 1e-9)**
> **RESOLUTION: Δ_L2 = 4.48%, P(CAUTION) = 4.48% — IDENTITY HOLDS (difference < 1e-9)**

**Δ_L2 is the CAUTION activation rate in the departure window.** This holds for every configuration below and was re-verified on each run.

---

## C. Threshold provenance

| Component | Value | Unit | Source / derivation | Status |
|---|---|---|---|---|
| `W_C` | **21.6** | kn | MET Malaysia Cat 1 onset, 40 km/h ÷ 1.852 | **Externally supported (canonical)** |
| `W_C` | 22.0 | kn | Superseded project rounding of 21.598 | Historical project value |
| `W_C` | 18.0, 20.0, 25.0 | kn | Perturbation around canonical | **Researcher-defined sensitivity value** |
| `W_U` | **27.0** | kn | MET Cat 2 onset, 50 km/h ÷ 1.852 | **Externally supported (canonical)** — held fixed |
| `R_C` | **10.0** | mm/hr | JPS/DID Infobanjir *Light* upper limit | **Externally sourced, non-MET (canonical)** |
| `R_C` | 7.5 | mm/hr | Superseded project value, matched no source | Historical project value |
| `R_C` | 5.0, 15.0, 19.9 | mm/hr | Perturbation; 19.9 is the degenerate case `R_C → R_U` | **Researcher-defined sensitivity value** |
| `R_U` | **20.0** | mm/hr | MET *Ribut Petir* warning trigger | **Externally supported (canonical)** — held fixed |
| `O_C`, `O_U` | **1.0 / 1.25** | m | Yaakob et al. (2015) small-vessel **operational ceiling** | **Externally supported (canonical)** |
| `O_C`, `O_U` | 1.0 / 1.9 | m | Yaakob NORDFORSK **failure point** as UNSAFE — the project's own superseded configuration | **Externally supported (alternative reading of the same source)** |
| `O_C`, `O_U` | 1.4 / 2.8 | m | Yaakob **medium vessel** (10–25 GRT) | **Externally supported — different population** |
| `O_C`, `O_U` | 1.5 / 3.5 | m | Yaakob **big vessel** (>25 GRT); 3.5 m is also the MET Cat 1 ceiling | **Externally supported — different population** |
| `O_C` | 0.80–1.25 in 0.05 steps | m | Gradient characterisation | **Researcher-defined sensitivity value** |
| `g_t` | sunrise ≤ t < sunset | — | COLREGs Rule 20(b) | **Externally supported** — not perturbed (§F) |

No new value is introduced here that is later presented as externally validated.

---

## D. Boundary density (departure window)

| Boundary | Window | PRIMARY n | % of window | RESOLUTION n | % of window |
|---|---|---|---|---|---|
| wind 21.6 kn | ±2.0 kn | **2** | 0.02% | **0** | 0.00% |
| wind 27.0 kn | ±2.0 kn | **0** | 0.00% | **0** | 0.00% |
| rain 10.0 mm/hr | ±3.0 | 33 | 0.36% | 25 | 0.42% |
| rain 20.0 mm/hr | ±5.0 | 5 | 0.05% | 4 | 0.07% |
| **wave 1.00 m** | ±0.15 m | **1,300** | **14.23%** | **833** | **14.04%** |
| **wave 1.25 m** | ±0.15 m | **742** | **8.12%** | **368** | **6.20%** |

Observed maxima in the departure window: wind 21.80 kn (PRIMARY) / 19.30 kn (RESOLUTION); wave 2.06 m / 1.80 m.

**Only the wave boundaries sit in a dense region of the data.** Wind has effectively no mass near either boundary. Rainfall has 0.36–0.42% of the window near its CAUTION boundary.

---

## E. One-at-a-time sensitivity

### Wind — structural zero

| `W_C` | 18.0 | 20.0 | 21.6 | 22.0 | 25.0 |
|---|---|---|---|---|---|
| Δ_L2 PRIMARY | 5.81% | 5.81% | 5.81% | 5.81% | 5.81% |
| Δ_L2 RESOLUTION | 4.48% | 4.48% | 4.48% | 4.48% | 4.48% |

Zero change to two decimal places across a 7-knot range. Per §10 of the task, **no wind grid was generated** — this is reported as a structural zero. It follows from the density table: maximum departure-window wind is 21.80 kn, and `g_w` is the binding component of **no** CAUTION hour.

### Rainfall — minimal

| `R_C` (mm/hr) | 5.0 | 7.5 | **10.0** | 15.0 | 19.9 |
|---|---|---|---|---|---|
| Δ_L2 PRIMARY | 6.15% | 5.93% | **5.81%** | 5.70% | 5.67% |
| Δ_L2 RESOLUTION | 5.04% | 4.65% | **4.48%** | 4.31% | 4.26% |

P(UNSAFE) is unchanged throughout (42.88% / 41.08%) because `R_U` is fixed.

Total range across a near-fourfold variation in `R_C`: **0.48 points (PRIMARY), 0.78 points (RESOLUTION)**. **The non-MET CAUTION boundary — the most criticised single choice in the threshold set — has minimal influence on the headline result.** This is a defensive finding and should be reported.

### Wave — dominant

| (`O_C`, `O_U`) | Provenance | Δ_L2 PRIMARY | Δ_L2 RESOLUTION |
|---|---|---|---|
| (0.75, 1.25) | researcher-defined, −0.25 m | 14.75% | 14.19% |
| **(1.00, 1.25)** | **Yaakob operational ceiling (canonical)** | **5.81%** | **4.48%** |
| (1.25, 1.50) | researcher-defined, +0.25 m | 2.54% | 1.67% |
| (1.00, 1.90) | Yaakob failure point as `O_U` (sourced) | 9.22% | 6.08% |
| (1.40, 2.80) | Yaakob medium vessel (different population) | 1.96% | 0.66% |
| (1.50, 3.50) | Yaakob big vessel (different population) | 1.26% | 0.37% |

**Gradient on `O_C`** (`O_U` fixed 1.25, small vessel):

| `O_C` (m) | 0.80 | 0.85 | 0.90 | 0.95 | **1.00** | 1.05 | 1.10 | 1.15 | 1.20 | 1.25 |
|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY | 12.94% | 10.31% | 8.83% | 6.87% | **5.81%** | 4.36% | 3.25% | 1.87% | 0.92% | 0.14% |
| RESOLUTION | 12.62% | 9.91% | 8.41% | 6.08% | **4.48%** | 3.10% | 2.54% | 1.68% | 0.98% | 0.22% |

**Gradient on `O_U`** (`O_C` fixed 1.00): PRIMARY 3.14% → 9.25% across 1.10–2.20 m, saturating above ~1.9 m (maximum observed wave 2.06 m).

---

## F. Time-policy sensitivity

Sunrise/sunset were **not** perturbed — the boundary is COLREGs-derived and semantically unlike a numeric environmental threshold. Instead the researcher-defined *policy* `night ⇒ UNSAFE` was tested by changing the denominator, which introduces no new parameter.

| | denominator | Δ_L2 PRIMARY | Δ_L2 RESOLUTION |
|---|---|---|---|
| **T0** canonical — night classified UNSAFE, counted in denominator | 9,135 / 5,935 | **5.81%** | **4.48%** |
| **T1** daylight-only — non-daylight hours excluded from denominator | 5,536 / 3,594 | **9.59%** | **7.40%** |

P(UNSAFE) falls to 5.74% / 2.70% under T1, confirming that most departure-window UNSAFE hours are darkness rather than sea state.

**T1 raises the headline by roughly two-thirds.** This is a framing choice, not an environmental one: the canonical figure dilutes CAUTION across a denominator that includes hours the architecture classifies UNSAFE by policy. Both are defensible; the difference should be disclosed.

---

## G. Combined grid — `R_C` × (`O_C`, `O_U`)

Only the two dimensions with non-zero influence. Wind excluded on the evidence of §E.

**PRIMARY** — Δ_L2 %

| `R_C` \ wave | (1.0, 1.25) | (1.0, 1.9) | (1.4, 2.8) | (1.5, 3.5) |
|---|---|---|---|---|
| 5.0 | 6.15 | 9.56 | 2.42 | 1.74 |
| 7.5 | 5.93 | 9.34 | 2.12 | 1.43 |
| **10.0** | **5.81** | 9.22 | 1.96 | 1.26 |
| 15.0 | 5.70 | 9.11 | 1.84 | 1.14 |
| 19.9 | 5.67 | 9.07 | 1.81 | 1.11 |

Grid min **1.11%**, grid max **9.56%**.

**RESOLUTION** — Δ_L2 %

| `R_C` \ wave | (1.0, 1.25) | (1.0, 1.9) | (1.4, 2.8) | (1.5, 3.5) |
|---|---|---|---|---|
| 5.0 | 5.04 | 6.64 | 1.31 | 1.03 |
| 7.5 | 4.65 | 6.25 | 0.86 | 0.57 |
| **10.0** | **4.48** | 6.08 | 0.66 | 0.37 |
| 15.0 | 4.31 | 5.91 | 0.49 | 0.20 |
| 19.9 | 4.26 | 5.86 | 0.44 | 0.15 |

Grid min **0.15%**, grid max **6.64%**.

Within each column the rainfall spread is under 0.5 points; between columns the wave spread exceeds 8 points. **The grid is essentially one-dimensional.**

---

## H. Component attribution (canonical, departure window)

| Component | PRIMARY: enters CAUTION | PRIMARY: binding | RESOLUTION: enters | RESOLUTION: binding |
|---|---|---|---|---|
| `g_w` | 1 | **0** | 0 | **0** |
| `g_r` | 15 | 13 | 14 | 13 |
| **`g_o`** | **877** | **518** | **436** | **253** |
| `g_t` | 0 | 0 | 0 | 0 |
| `g_m` | 0 (excluded, `D = {m}`) | 0 | 0 | 0 |
| **ties (>1 component at max)** | **0** | — | **0** | — |

Of 531 CAUTION hours under PRIMARY, `g_o` is the binding component in 518 (97.6%) and `g_r` in 13 (2.4%). `g_w` binds in none, consistent with F-1/F-17: it activates but is never decisive. The gap between "enters CAUTION" and "binding" for `g_o` (877 vs 518) is the set of hours where a more severe component — almost always `g_t` at UNSAFE — already governs.

---

## I. PRIMARY vs RESOLUTION, and the common-period comparison

The common-period comparison was feasible with existing data and was run.

| Configuration | n (records) | n (departure) | Δ_L2 | P(UNSAFE) |
|---|---|---|---|---|
| PRIMARY wave model (ERA5-Ocean ~50 km), **full 5.00 yr** | 43,848 | 9,135 | **5.81%** | 42.88% |
| PRIMARY wave model, **common 28,501-hour period** | 28,501 | 5,935 | **6.45%** | 42.90% |
| RESOLUTION wave model (MFWAM ~8 km), **common period** | 28,501 | 5,935 | **4.48%** | 41.08% |

**This resolves ISSUE-1 in `open-issues-log.md`, and shows the canonical attribution to be wrong in magnitude.**

Decomposing the reported 1.33-point spread, holding one factor fixed at a time:

- **Wave-model (grid-resolution) effect, record length held constant:** 6.45% − 4.48% = **1.97 points**
- **Record-length effect, wave model held constant:** 5.81% − 6.45% = **−0.64 points**
- **Sum:** 1.97 − 0.64 = 1.33 points = the reported spread ✓

The two effects act in **opposite directions**. `empirical-findings-2026-09-06.md` §0a states that "the 1.3-point gap between the columns IS the grid-resolution sensitivity." On a like-for-like comparison the grid-resolution sensitivity is **1.97 points**, not 1.33; the reported spread understates it because the shorter record independently raises the rate by 0.64 points. The direction of the canonical claim is right — the coarse model classifies more conservatively — but the magnitude is not.

---

## J. Robustness range

| Scope | Δ_L2^min | Δ_L2^canonical | Δ_L2^max |
|---|---|---|---|
| **Externally sourced thresholds, small vessel only** (canonical; Yaakob failure-point variant; sourced `R_C` values) | **5.67%** | **5.81%** | **9.56%** |
| Adding researcher-defined ±0.25 m perturbations on `O_C` | 2.54% | 5.81% | 14.75% |
| Adding other vessel classes (different deployment populations) | 1.11% | 5.81% | 9.56% |
| Full evaluated grid, PRIMARY | 1.11% | 5.81% | 9.56% |
| Full evaluated grid, RESOLUTION | 0.15% | 4.48% | 6.64% |

Reported as a **deterministic sensitivity range**, not a confidence interval. **Do not write "5.81% ± x".**

### Threshold elasticity, ranked descriptively

| Threshold | Approximate influence | Rank |
|---|---|---|
| `O_C` (wave CAUTION onset) | ≈ **−1.4 points per 0.05 m** (≈ −28 points per metre) over 0.80–1.25 m | **1 — dominant** |
| `O_U` (wave UNSAFE onset) | ≈ +0.2 points per 0.05 m below 1.6 m; saturates above ~1.9 m | 2 |
| `R_C` (rainfall CAUTION onset) | ≈ **−0.032 points per mm/hr** | 3 — negligible |
| `W_C`, `W_U` (wind) | **0.00** across 18–25 kn | 4 — structural zero |

Descriptive influence ranking only. Not causal importance.

---

## K. Falsification test

**Can a defensible configuration drive Δ_L2 ≈ 0?**

**Yes, by three routes, of which only the first two are legitimate:**

1. **Different vessel class.** Big vessel (1.5 / 3.5 m, Yaakob + MET Cat 1 ceiling): **1.26% PRIMARY, 0.37% RESOLUTION**. Medium vessel (1.4 / 2.8 m): 1.96% / 0.66%. For vessels above 25 GRT the intermediate state is close to vacuous at this site. **This is a real and reportable limit: the result is specific to the small-vessel deployment population.**
2. **Band collapse.** Setting `O_C → O_U` (1.25 / 1.25) gives **0.14% PRIMARY, 0.22% RESOLUTION**. Degenerate by construction — a zero-width CAUTION band — but it demonstrates that the result is produced by the *width* of the wave CAUTION band, not by the classifier's structure.
3. Not available: no *sourced small-vessel* threshold configuration drives the result near zero. The minimum over sourced small-vessel configurations is **5.67%**.

**Can a defensible configuration make CAUTION very frequent?**

Yes. `O_C` = 0.80 m gives **12.94% / 12.62%**; the sourced Yaakob failure-point variant (1.0 / 1.9) gives **9.22% / 6.08%**. The upper end of the sourced range is roughly 1.6× the canonical value.

---

## L. Interpretation

**What these results mean.** Δ_L2 is the CAUTION activation rate, and that rate is governed almost entirely by one boundary: the wave CAUTION onset `O_C`. Wind is irrelevant at this site by a wide margin. Rainfall — including the non-MET `R_C` = 10.0 mm/hr that is the most attackable single choice in the threshold set — moves the headline by less than half a point across a fourfold variation. The result is therefore **not** an artefact of the weakest-sourced threshold; it is a direct function of the best-sourced one.

That is the favourable reading. The unfavourable reading is equally true: a ±0.25 m change in a single externally sourced boundary moves the headline by a factor of about six, and Yaakob's own source supports two different readings of the small-vessel UNSAFE boundary (operational ceiling 1.25 m, failure point 1.9 m) that give 5.81% and 9.22%. The headline is a point value on a steep gradient.

**What these results do not mean.** Nothing here establishes that any threshold is correct — there is no incident record against which to score them. Nothing here addresses safety improvement. Nothing here evaluates the governance design: **Δ_L2 is invariant to the content of `A_AI(CAUTION)`** provided it remains a strict subset of FULL, so this analysis says nothing about whether `{Go, Delay}` is the right restriction. The ranges are deterministic sensitivity, not statistical uncertainty.

---

## M. Implications for the research chain

**RQ2 remains defensible, with its wording tightened.** The question "how often does the intermediate state admit a strictly smaller recommendation set" is answerable and was answered; it could have returned ≈0 for the small-vessel population and did not. But the answer is now known to be conditional on `O_C`, and RQ2's wording should carry that — it is a characterisation of *this classifier configuration* at this site, not of the site alone.

**Empirical characterisation remains the primary contribution**, and is strengthened in one respect and qualified in another. Strengthened: the sensitivity analysis is itself part of the empirical contribution, and it answers reviewer attack #10 from `research-chain-lock.md`, which was previously marked OPEN. Qualified: the contribution must now be stated as a characterisation with a reported operating envelope rather than a single figure.

**Two downstream corrections are now required.** First, `empirical-findings-2026-09-06.md` §0a attributes the 1.33-point PRIMARY/RESOLUTION spread to grid resolution; the like-for-like figure is 1.97 points, with record length contributing −0.64 in the opposite direction. ISSUE-1 is resolvable and the canonical text is wrong in magnitude. Second, the vessel-class finding — that the intermediate state is near-vacuous for vessels above 25 GRT — belongs in the limitations, since the architecture is presented as vessel-conditional and this is the strongest evidence of what that conditioning does.

---

## N. Recommended headline wording

> For the operative small-vessel class at the deployment site, the intermediate advisory-scope state was reached in 5.81% of departure-window hours under the primary configuration and 4.48% under the alternative environmental-data configuration. Sensitivity analysis over externally sourced threshold values for this vessel class gives a range of 5.67%–9.56%; the rate is governed almost entirely by the wave CAUTION onset, which moves it by approximately 1.4 percentage points per 0.05 m, while the rainfall CAUTION boundary moves it by less than 0.5 points across a fourfold variation and the wind boundaries by nothing measurable. These are exact descriptive values for the analysed traces and configurations and are reported as a deterministic sensitivity range, not as a confidence interval.

---

## O. Recommended limitation wording

> Three limitations bound this result. First, Δ_L2 is **invariant to the content of `A_AI(CAUTION)`**: because the compared conditions differ only in that cell, any strict subset of the full recommendation set yields the same figure. The result therefore characterises how often the intermediate state is reached and provides **no evidence** that restricting advisory scope to `{Go, Delay}` is appropriate; that choice is researcher-defined and unevaluated. Second, the figure is strongly dependent on the wave CAUTION onset. A ±0.25 m perturbation of that boundary moves it between 2.54% and 14.75%, and the source itself supports two readings of the small-vessel UNSAFE boundary giving 5.81% and 9.22%. Third, the result is specific to vessels under 10 GRT: under the same source's medium- and big-vessel thresholds the intermediate state is reached in 1.96% and 1.26% of departure hours respectively, approaching vacuity for the larger classes. No incident record exists for the site, so no threshold configuration can be scored for correctness.

---

## P. Decision

> ## **HEADLINE RESULT SENSITIVE BUT STILL INFORMATIVE**

The result is not an artefact of a weakly sourced choice, which was the specific risk the audit identified. The rainfall CAUTION boundary at 10.0 mm/hr — openly non-MET and the most attackable value in the threshold set — moves the headline by 0.48 points across a fourfold variation, and the wind boundaries move it by exactly nothing across a seven-knot range, with zero binding hours. The figure is produced almost entirely by the wave CAUTION onset, which is the best-sourced threshold in the set, taken from Yaakob's measured operational ceiling for the deployment population. Reviewer attack #10 in `research-chain-lock.md` can now be answered rather than conceded.

It is nonetheless sensitive, and the thesis must say so in the same breath as the number. A ±0.25 m perturbation of `O_C` spans 2.54%–14.75%, an elasticity of roughly 1.4 points per 5 cm, and the same source supports a second small-vessel reading giving 9.22%. Over all sourced small-vessel configurations the range is 5.67%–9.56% — always non-vacuous, never precise. The honest claim is an operating envelope with a dominant parameter identified, not a point estimate; §N and §O give wording that survives that reading.

Two findings beyond the sensitivity question should be carried forward. The common-period comparison resolves ISSUE-1 and shows the canonical attribution wrong in magnitude: the like-for-like grid-resolution effect is 1.97 points, not 1.33, because record length pulls 0.64 points the other way. And the vessel-class sweep shows the intermediate state approaching vacuity for vessels above 25 GRT — 1.26% and 0.37% — which is the clearest available evidence of what vessel-conditional thresholds actually do, and belongs in the limitations rather than being left for a reviewer to compute.
