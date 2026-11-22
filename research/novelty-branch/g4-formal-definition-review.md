# G4 — Formal Definition Review

**Prepared:** 17 November 2026 · **Author:** Claude (Cowork session) · **Status:** exploratory research branch, v2. Frozen RQ1–RQ3 and all canonical artefacts untouched. No experiment was run.

**Versioned record.** `novelty-literature-matrix.md`, `candidate-research-gaps.md`, `evaluation-feasibility.md` and `novelty-go-no-go-decision.md` (all 17 Nov 2026, v1) are **preserved unedited**. Their conclusions stand as the v1 record. This document and its three companions are **v2** and supersede v1 §G4 wherever they conflict. The conflicts are itemised in `g4-revised-decision.md` §5.

---

## 1. What v1 got wrong

v1 defined evidential support as **residual information beyond a trivial baseline**, operationalised as: if the output is a deterministic function of the concurrent observation, it is *unsupported*; if it varies beyond persistence, it is *supported*.

**That definition is incorrect, and the project's own data refutes it.**

The fitted damping coefficient for wave at lead 8 is **α = 0.970**. Under the surrogate form `α·y(h) + (1−α)·clim(month, hour)`, α → 1 means persistence is very nearly the error-minimising predictor for wave at this site — i.e. **persistence is the good wave forecast.** Wave also drives **97.6%** of CAUTION activation.

So v1's statistic would classify a `Duration` recommendation derived from the **best available wave predictor** as *unsupported*, purely because that predictor happens to be a deterministic function of the present observation. And it would classify a recommendation derived from the climatological surrogate as *supported* — even though that surrogate's measured false-acceptable rate at lead 1 was **9.8% against persistence's 9.4%**, i.e. **worse**.

**v1's support statistic therefore ranks a better predictor below a worse one.** That is not a defect in calibration; it is a category error. The statistic measures the *functional form of the generator*, and treats functional novelty as if it were evidential warrant.

---

## 2. Three concepts that v1 conflated

Let:

- `E` — an **evidence class**: the set of quantities observable at the decision instant, with their quality attributes (present/absent, age, source agreement, measurement reliability).
- `t ∈ T` — an **output type** (a recommendation category, e.g. `Go`, `DepartureTime`).
- `G` — a declared **class of permissible derivation procedures** (see `g4-prior-art-challenge.md` §2 and §2.4 below).
- `g ∈ G` — a procedure; `g_t(E)` its type-`t` output.
- `Y` — the **independent outcome** against which a type-`t` output can be scored.
- `L_t` — a **loss** appropriate to type `t`.
- `B` — a reference or baseline procedure.

### 2.1 Incremental information (II)

> **Definition 1.** Procedure `g` carries **incremental information** for type `t` relative to baseline `B` on evidence class `E` iff `g_t(E)` is **not almost surely equal to a measurable function of `B_t(E)`**. Quantitatively, `II(g, B; t, E) = I(g_t(E); Z) − I(B_t(E); Z)` for a declared target `Z`.

**What it is a property of:** the pair `(g, B)` and the input distribution. **Not** of `E`, **not** of `t`, **not** of `Y`.

**What it is not:** a normative statement. II is **neither necessary nor sufficient** for an output to be warranted. It requires no outcome data to compute, which is precisely why it is the wrong instrument — *warrant is a claim about outcomes, and II never looks at one.*

### 2.2 Predictive validity (PV)

> **Definition 2.** The **predictive validity** of `g` for type `t` on evidence class `E` is `PV(g; t, E) = −𝔼[L_t(g_t(E), Y)]`, or a skill score `1 − 𝔼[L_t(g_t(E),Y)] / 𝔼[L_t(B_t(E),Y)]` relative to a declared reference `B`.

**What it is a property of:** `(g, t, E, Y, L_t)`. **Requires outcome data.**

**Relation to II:** none in general. The two are **logically independent** (§3).

### 2.3 Evidential adequacy (EA)

> **Definition 3.** Evidence class `E` is **evidentially adequate** for type `t`, relative to a declared procedure class `G` and a type-specific requirement `τ_t`, iff
>
> `EA(E, t; G, τ_t) ⟺ ∃ g ∈ G : PV(g; t, E) ≥ τ_t`.

**What it is a property of:** `(E, t, G, τ_t)` — and, through `PV`, of `Y` and `L_t`.

**Three features that make EA the normative concept, and that v1 lacked entirely:**

1. **It is existential over a procedure class.** Adequacy asks whether *some* permissible procedure can meet the requirement, not whether *this one* does. v1 evaluated one fixed generator and attributed the result to the evidence.
2. **The threshold `τ_t` is type-specific and must be grounded in the consequence of error for type `t`.** This is where "adequate *for the specific recommendation*" lives. v1 had no `τ_t` at all.
3. **It requires outcome data**, because `PV` does. v1's statistic required none, which should have been the warning sign.

### 2.4 A fourth quantity, needed to keep EA from being vacuous

> **Definition 4.** Type `t` is **`G`-reachable** from `E` iff `∃ g ∈ G` such that `g_t(E)` is defined — i.e. some permissible procedure produces a type-`t` output at all.

`EA` presupposes `G`-reachability: if no permissible procedure emits type `t`, the existential in Definition 3 is empty and `EA` is false for a reason that has nothing to do with evidence quality. **Reachability and adequacy must therefore be reported separately**, and `G` must be declared for either to be meaningful. `g4-prior-art-challenge.md` §2 handles the reachability half.

---

## 3. Why the three differ — worked examples, all from measured data where possible

### Example A — unsupported by II, valid by PV, adequate by EA

**Setting.** `Duration` advice at this site under persistence. Wave α = 0.970 at lead 8.

| | Verdict |
|---|---|
| **II** | **Zero.** The predicted run length is a deterministic function of the concurrent exposure margin — step residual exactly 0.000000, baseline R² exactly 1.000000 **[measured]** |
| **PV** | **High.** Persistence is close to the error-minimising wave predictor here; its measured false-acceptable rate on the generator's own acceptability notion is **9.4% at lead 1**, the best of the three conditions **[measured]** |
| **EA** | **Plausibly satisfied**, if `τ_Duration` is set by the consequence of an over-long duration estimate — discomfort and a shortened trip rather than loss of the vessel |

**This is the decisive counterexample.** v1 called this *unsupported*. It is a deterministic function of the present **and** the best available predictor **and** arguably adequate. **II = 0 says nothing about warrant.**

### Example B — supported by II, worse by PV

**Setting.** The same `Duration` advice under the climatological surrogate.

| | Verdict |
|---|---|
| **II** | **Positive.** Ten distinct run lengths; 24.65% of episodes unexplained by the concurrent margin; calendar explaining 31.5% of residual **[measured]** |
| **PV** | **Worse than persistence at lead 1** — false-acceptable rate 9.8% against 9.4% **[measured]**. Better at leads ≥3 (19.1% vs 31.7% at lead 8) |

**II and PV point in opposite directions at short leads.** A criterion built on II would have preferred the worse predictor exactly where the advice is most often issued.

### Example C — valid by PV, inadequate by EA, and the reverse

**Setting.** Two output types sharing one predictor with 80% hit rate on "conditions will remain workable".

| Type | Consequence of a false "workable" | `τ_t` | EA at PV = 0.80 |
|---|---|---|---|
| `Duration` | Trip cut short; discomfort | low | **adequate** |
| `Go` issued in conditions the classifier calls UNSAFE | Possible loss of vessel and crew | high | **inadequate** |

**Same evidence, same procedure, same predictive validity — opposite adequacy verdicts, because `τ_t` differs.** No function of II or PV alone can produce this; it requires the type-specific threshold. **This is the only one of the three concepts that is recommendation-specific**, and it is the one v1 omitted.

### Example D — II high, PV undefined

A generator that adds a pseudo-random perturbation has strictly positive II relative to persistence and **no PV at all** beyond the baseline. v1's criterion would score it as *more supported* than persistence. **II is gameable by construction; PV and EA are not.**

### 3.1 Summary of the independence structure

| | Needs outcomes? | Property of | Recommendation-specific? | Normative? |
|---|---|---|---|---|
| **II** | No | `(g, B)`, input distribution | No | **No** |
| **PV** | **Yes** | `(g, t, E, Y, L_t)` | Only through `L_t` | Partly |
| **EA** | **Yes** | `(E, t, G, τ_t)` | **Yes, through `τ_t`** | **Yes** |
| **`G`-reachability** | No | `(E, t, G)` | Yes | Precondition |

**II is independent of PV in both directions** (Examples A, B, D). **PV does not determine EA** (Example C). So the three are genuinely distinct, and v1 collapsed them into the weakest one.

---

## 4. What this does to v1's empirical instance

v1 offered the `DepartureTime` / `Duration` contrast as evidence that the distinction is "measurable rather than merely stateable". Re-read under the corrected definitions:

| v1 claim | Corrected reading |
|---|---|
| "`Duration` is **reachable but unsupported**" | `Duration` has **II = 0 relative to persistence**. That is a measured fact about the generator's functional form. It is **not** a finding about evidential warrant, and on PV grounds the opposite holds |
| "`DepartureTime` is **structurally unreachable**" | `DepartureTime` is **unreachable under the one procedure tested**. See `g4-prior-art-challenge.md` §2 — this does not generalise |
| "The exactly-zero residual is what makes this a test" | The exactly-zero residual makes it a **clean test of II**. II was the wrong quantity, so the cleanliness is beside the point |

**The measurements stand; the interpretation does not.** Nothing in the executed run is withdrawn — `results-causal-replication.json` is unchanged — but v1's reading of it as evidence of an evidential-support phenomenon is withdrawn.

---

## 5. Consequences for the research claim

1. **A support criterion that needs no outcome data cannot be a criterion of warrant.** Any replacement must consume `Y`.
2. **`τ_t` must be derived, not chosen.** Its grounding is the consequence of a type-`t` error. In this project, no such grounding exists: the D-4 investigation established that **no harm-severity reference exists for this vessel class in these waters**, and the best independent hazard reference has no discriminating power at this site. **So `τ_t` is not currently derivable in the thesis domain**, which is a further reason to evaluate any EA claim on a public benchmark where consequences are at least proxied by labelled outcomes.
3. **`G` must be declared.** Without it, both reachability and adequacy are ill-posed.
4. **The three-state taxonomy (unreachable / reachable-but-unsupported / reachable-and-supported) does not survive** in v1's form. Under the corrected definitions the states are `G`-unreachable, `G`-reachable-but-inadequate, and `G`-reachable-and-adequate — and all three are relative to a declared `G` and a derived `τ_t`, neither of which v1 had.
