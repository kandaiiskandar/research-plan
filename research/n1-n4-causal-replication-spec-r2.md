# Causally Valid N1–N4 Replication — Specification, Revision 2

> **REVISED BY REVISION 3 — 17 Nov 2026.** `research/n1-n4-causal-replication-spec-r3.md` corrects three items: **E-GC-2b** was defeated by bin width (within-decile run-length variance is positive under persistence whenever a bin straddles the `P_OK` breakpoint) and is replaced by four bin-free tests; **E-ES-7** conflated two oracles — G-L is an oracle for its own exposure index, **not** for the separate physical thresholds, so its false-acceptable rate is 0 on T-INT only and becomes the index–threshold mismatch baseline on T-PHYS; and **D-4h is downgraded to a wording check** after read-only verification found it already documented in `architecture-illustration.md` §203/§209/§386, `prediction-register.csv` P22 and `final-research-chain-lock.md` §81/§315. **E-GC-2a** is withdrawn as redundant. R2 predictions 2 and 6 are **withdrawn**. **Nothing below is edited**; §6 of R3 is the cumulative ledger.


**Prepared:** 17 November 2026 · **Author of this document:** Claude (Cowork session) · **Status:** **specification only. Still nothing executed.**

**Nothing was run.** No code was executed for this document and no data was read. Every number restated below is carried over from the 17 Nov 2026 run already recorded in `research/non-degeneracy/n1-n4-results.json`.

**What this revises.** `research/n1-n4-causal-replication-spec.md` (Revision 1) stands unaltered and carries a pointer to this document. Six criteria or checks change. Four were named in review; **two further defects of the same class were found by auditing the rest of R1 for them**, and both are corrected here rather than left to be found during execution. §7 is the cumulative ledger.

**Honest summary of what the review exposed.** R1 contained three criteria that could not do their job: one that **cannot pass for any generator**, one that **cannot pass for structural reasons unrelated to the generator**, and one that is **true by construction and therefore tests nothing**. All three would have produced confident-looking output carrying no information. That is the same failure mode as the leak they were written to catch, and finding them before execution rather than after is the only reason this revision is cheap.

---

## 1. E-GC-2 was unpassable — corrected

### 1.1 The defect

R1 required `H(type_i │ type_j) > 0` for **every ordered pair** of advice types. The generator's own rule is

```python
s.add("Go" if e[i] <= e_go else "Delay")
```

so `Delay ≡ ¬Go` exactly. Therefore `H(Delay │ Go) = H(Go │ Delay) = 0` **always, for every generator condition including G-B and G-L.** E-GC-2 could not pass under any circumstance. It was not a test; it was a guaranteed failure that would have fired identically on all three conditions and discriminated nothing.

**The right reframing, which is clarifying in itself:** `Go` and `Delay` are two labels for **one bit** — the concurrent accept/reject decision. The generator produces **one concurrent decision** and **up to two forecast-dependent augmentations**. Only the augmentations are candidates for an incremental-information test.

### 1.2 A second error this exposed, in R1 §2

R1 §2 claimed that under persistence `Duration` "becomes a **deterministic function of `Go`/`Delay`** and carries no independent information". **That is wrong.** Working it through:

- `Go` fires iff `e(h) ≤ P_GO` (60th percentile)
- `Duration` fires iff the predicted run ≥ 2 hours, and under persistence every forward hour inherits `e(h)`, so the run is the full horizon iff `e(h) ≤ P_OK` (70th percentile), else zero

`P_GO < P_OK`, so there are **three** outcomes, not two: `e ≤ P60` → `Go` + `Duration`; `P60 < e ≤ P70` → `Delay` + `Duration`; `e > P70` → `Delay` alone. Given `Delay`, `Duration` may be present or absent, so `H(Duration │ Go/Delay) > 0` under persistence. R1's prediction 2 was therefore wrong on its own terms.

**The correct characterisation.** Under persistence, `Duration` is a **threshold on the concurrent observation at a different cut point** — it adds a bit relative to the `Go`/`Delay` bit, but that bit is still a pure function of present information. It is not *forecast*-informative. So the question is not whether a type adds information beyond `Go`/`Delay`, but whether it adds information **beyond the concurrent observation**.

### 1.3 Why the obvious fix also fails, and what works

The tempting repair — require `H(type │ X_now) > 0` where `X_now` is the full concurrent observation — **fails for G-B too.** Under

> `ŷ(d, h+k) = α_k · y(d, h) + (1 − α_k) · clim(m(d), h+k)`

every term is a function of `y(d,h)`, `m(d)`, `h` and `k`. G-B's forecast is therefore *also* a deterministic function of concurrent observables plus the calendar. **Determinism is not the discriminating property**, and a criterion built on it would reject both methods.

What actually distinguishes them is whether the forecast-dependent types vary **at fixed concurrent exposure**. Under persistence they cannot: at a given `e(h)`, `DepartureTime` is always absent and `Duration` is always determined. Under G-B they can: two episodes with identical `e(h)` in different months or at different hours of the window receive different predicted trajectories, hence different run lengths and different better-hour verdicts.

### 1.4 E-GC-2 revised — forecast-dependent types only

| | Criterion | Test | Exploratory threshold |
|---|---|---|---|
| **E-GC-2a** | `DepartureTime` varies at fixed concurrent exposure | Stratify episodes into deciles of `e(h)`; within each stratum with `n ≥ 50`, compute the `DepartureTime` emission rate | **Non-zero and non-unit rate in ≥3 strata** |
| **E-GC-2b** | `Duration` run length varies at fixed concurrent exposure | Same strata; within-stratum variance of the predicted run length | **Variance > 0 in ≥3 strata** |
| **E-GC-2c** | The variation is attributable to the forecast, not to noise | Within strata, regress the forecast-dependent outcome on `(month, hour-of-window)`; report the share of strata with a non-null association | Descriptive, reported |

**Scope restriction, as directed:** E-GC-2 now applies **only to `DepartureTime` and `Duration`**. `Go`/`Delay` is one bit and is exempt by definition, not by exception.

**Method note.** Deciles with a minimum cell size replace conditional entropy on a continuous conditioning variable, which is poorly behaved at these sample sizes (7,305 episodes, and the forecast-dependent types are concentrated in part of the exposure range). Stratified rates and variances are non-parametric, report their own `n`, and degrade gracefully.

**Revised predictions.** G-A fails **E-GC-2a** (rate identically 0 in every stratum) and fails **E-GC-2b** (run length determined within each stratum). G-B's status is **open** — this is now a real test rather than a foregone one.

---

## 2. E-ES strengthened — threshold-specific errors and false-acceptable predictions

### 2.1 Why generic skill was the wrong instrument

R1's E-ES-1 and E-ES-2 used MAE and a skill score against persistence. Mean error is the wrong metric for a decision that is a **threshold crossing**: a forecast can have excellent MAE and still be useless at the one boundary the advice turns on, and it can have poor MAE while getting every crossing right. Worse, symmetric error treats the two mistakes as equivalent when they are not remotely equivalent in a safety setting.

### 2.2 Two threshold families, answering different questions

| Family | Thresholds | Question it answers |
|---|---|---|
| **T-INT — internal** | The generator's own `P_OK` exposure cutoff (and `P_GO`) | Is the generator's internal acceptability logic reliable at the leads it uses? |
| **T-PHYS — physical** | The architecture's own boundaries: wave **1.0 / 1.25 m**, wind **21.6 / 27.0 kn**, rain **10 / 20 mm/hr** | **Would acting on this advice have put a boat into conditions the architecture itself calls CAUTION or UNSAFE?** |

T-PHYS is new and is the safety-relevant family. It is also the only one that connects forecast error to a consequence anyone outside this study would recognise. Note it uses the architecture's thresholds **as an evaluation yardstick only** — not as an independent safety reference, which §1 of `research/d4-critical-review.md` established does not exist. The distinction must be stated wherever these numbers appear.

### 2.3 The revised E-ES metrics

For each threshold in both families, each lead time `k = 1…9`, and each generator condition:

| | Metric | Definition | Why |
|---|---|---|---|
| **E-ES-1** | **False-acceptable rate (FAR_acc)** | `P(observed exceeds threshold │ forecast predicted it would not)` | **The headline ES metric.** This is the safety-critical error: the generator said the hour would be workable and it was not. It replaces symmetric skill as the primary number |
| **E-ES-2** | **False-restrictive rate (FRR)** | `P(observed does not exceed │ forecast predicted it would)` | Reported **separately and never netted against FAR_acc.** The two have different costs, and a single accuracy figure hides which error the generator makes |
| **E-ES-3** | **Hit rate / POD** at each threshold | `P(forecast predicted exceedance │ observed exceedance)` | Standard companion to FAR_acc |
| **E-ES-4** | **Threshold-crossing base rate and cell counts** | Observed exceedance frequency and the full 2×2 count per threshold per lead | **Mandatory.** Wave exceeds 1.25 m in only 5.74% of window hours, so FAR_acc and POD will be unstable at that boundary. No metric is reported for a cell with `n < 30`; it is printed as `insufficient n` |
| **E-ES-5** | Share of forecast-dependent advice emitted at leads where **FAR_acc ≤ 0.10** on T-PHYS wave 1.0 m | Advice-weighted | Replaces R1's "share emitted at leads where skill > 0" with a threshold-specific, safety-directed version |
| **E-ES-6** | Reliability of "predicted acceptable", per lead | Reliability diagram | Carried over from R1 E-ES-3, unchanged |
| **E-ES-7** | **G-L's own FAR_acc, reported alongside** | Same metrics on the leaky condition | It will be ≈0 by construction. **This is the clearest possible demonstration of what L3 did**, in units a supervisor can act on |

**On the 0.10 bound in E-ES-5.** It is a **judgement, not an evidence-derived figure**, and is labelled as such wherever it appears. No source establishes an acceptable false-acceptable rate for small-vessel departure advice — that is the same evidential void §4 of the D-4 report documented. The bound is therefore a reporting convention chosen in advance so that the number is not interpreted after the fact, and the full FAR_acc curve by lead is reported regardless so a reader can apply their own bound.

**Asymmetry is a reporting rule, not an option.** FAR_acc and FRR appear in adjacent columns in every table. No combined accuracy, F-score or single skill score is reported for the threshold families.

---

## 3. Chronological causality is not operational availability

### 3.1 The distinction R1 conflated

R1's leakage checks establish **chronological causality**: no input is timestamped after the decision instant. That is necessary and it is what separates this replication from the leaky original. It is **not** sufficient for any claim about what a decision-maker could have had.

| | Property | What it requires | What R1 tested |
|---|---|---|---|
| **C1 Chronological causality** | No input value carries a timestamp later than `t_dec` | Timestamp discipline | **Yes — L-CHK-1…5** |
| **C2 Operational availability** | Every input was **actually obtainable** at `t_dec`: the product existed at that date, its production latency had elapsed, and it was reachable at the site | Product provenance, latency, dissemination | **No — not tested, and not testable on this data** |

### 3.2 The primary run is C1-valid and C2-invalid, and this must be declared

The record is **ERA5-Ocean reanalysis**. A reanalysis is by definition produced after the fact, with preliminary products lagging by days and final products by months. **No value in it was available to anyone at 05:00 on the morning it describes** — not to a fisher, not to a forecaster, not to the architecture.

So the honest claim this replication can support is:

> *Advice generable from information that **existed before** the decision instant.*

and the claim it cannot support is:

> *Advice a fisher **could have received** at the decision instant.*

**This limitation is not specific to the generator.** It applies with equal force to the architecture's own historical replay and therefore to the published Δ_L2 = 5.81%. The project already treats the replay as retrospective characterisation rather than operational simulation, which is correct — but **the distinction has not been named precisely anywhere, and conflating it with leakage would be an error in either direction**: calling the replication "operationally valid" overclaims, and calling it "leaky" because it uses reanalysis confuses two different properties.

### 3.3 A-CHK — availability attestations, separate from L-CHK

A new check family, reported as **declarations** rather than gates, because they cannot pass on this data and pretending otherwise would be the overclaim just described.

| | Attestation | Primary run's answer |
|---|---|---|
| **A-CHK-1** | Product identity and version for every input | ERA5-Ocean (waves); Open-Meteo archive (wind, precipitation, WMO code), v2 sea cell |
| **A-CHK-2** | Production latency of each product | Reanalysis: days to months. **Exceeds the decision horizon by orders of magnitude** |
| **A-CHK-3** | Did the product exist at the episode date, in the form used? | Partly. ERA5 existed; the specific sea-cell extraction did not |
| **A-CHK-4** | Was it reachable at the site — connectivity, cost, language? | **Not assessed.** Out of scope and would require fieldwork |
| **A-CHK-5** | Spatial representativeness at the decision point | 9–55 km grid; the site may sit offshore of its own sheltered water (decision package §3.5) |
| **A-CHK-6** | **Overall verdict** | **C1 satisfied, C2 not satisfied. Declared in the abstract, not the limitations section** |

### 3.4 What would satisfy C2, and why this matters beyond bookkeeping

**Real issue-time forecasts satisfy both C1 and C2.** A forecast issued at 00Z and disseminated before 05:00 local was genuinely available at the decision instant. Nothing else in the audited candidate set has that property.

So the forecast archives audited in `research/next-research-decision-package.md` §3 now carry **three** distinct justifications, which is a materially stronger case than when they were a single-strand concern:

1. the staleness/dependability strand (the original reason);
2. generating `DepartureTime` and `Duration` with genuine skill (`research/d4-critical-review.md` §2.5);
3. **operational availability — the only route to a C2-valid claim** (this section).

That raises the priority of decision D-5 again, and it should be put to the supervisor as one decision with three payoffs rather than three separate asks.

---

## 4. L-CHK-6 reclassified as diagnostic

### 4.1 The defect

R1 made L-CHK-6 a check: *"G-B's measured skill must not exceed a plausible operational-forecast skill at the same lead,"* justified by the assertion that *"damped persistence beating a real NWP forecast at 6 h would be impossible."*

**There is no measured benchmark behind that.** No NWP skill figure for this site, at these leads, for these variables has been obtained or verified anywhere in this project. The check rested on an intuition presented as a bound — which is the same species of error as the FAO recommendation in the D-4 report: a plausible-sounding standard with nothing measured underneath it.

### 4.2 Reclassification

| | R1 | R2 |
|---|---|---|
| **L-CHK-6** | **Gate.** Failure triggers investigation before reporting | **Diagnostic.** G-B's skill by lead is reported with the explicit statement that **no comparable measured benchmark exists for this site**, so no bound is applied |

**It becomes a gate only when** a real issue-time forecast archive for this location has been obtained and its skill measured at the same leads, same variables and same grid point. At that moment the comparison is meaningful and the bound can be set from data. **Until then the honest position is that G-B's skill is uninterpretable in absolute terms** — it can be compared to persistence and to climatology, which are both in hand, and to nothing else.

This is a fourth reason the forecast archives matter: they are the only way to calibrate what "reasonable skill" means here.

---

## 5. Two further defects found by auditing R1 for the same failure mode

Having found one unpassable criterion, I checked the rest of R1 for criteria that cannot discriminate. Two more.

### 5.1 E-GC-3 could fail for structural reasons unrelated to the generator

R1 required that no single target hour take more than 70% of `DepartureTime` recommendations. But the generator recommends the minimum-exposure **later** hour **within the same window**, and the number of candidates shrinks across the window: an episode at 05:00 has four later hours, at 08:00 exactly one — 09:00. Pooling across the window guarantees that 09:00 is over-represented, for reasons that are a property of the window's shape, not of the generator's behaviour.

**E-GC-3 revised:** computed **within hour-of-window strata**, and primarily on 05:00 episodes, which have the full four-way choice. The ≤70% bound applies to the modal target **within a stratum**. Pooled figures are reported as descriptive only.

### 5.2 E-GE-3 was true by construction and tested nothing — and its triviality is itself a finding

R1 asked whether, where C1 ≠ C2, C2's content is "more conservative", with a ≥95% bound. But `A_AI` is **nested by construction** — `A_AI(CAUTION) ⊂ A_AI(SAFE)` — so C2 ⊆ C1 always, and every divergence is a strict subset. The criterion is a theorem, not a test. R1's prediction that it "passes at or near 100%" was a restatement of the containment property.

**What matters is what the nesting implies, and it is substantive.** `Go` and `Delay` are both in `A_AI(CAUTION) = {Go, Delay}`, so the CAUTION filter **never removes them**. It removes only `DepartureTime` and `Duration`. Therefore:

> **Graduated restriction at CAUTION cannot change the depart / do-not-depart recommendation. It can only remove timing and duration detail.**

Δ_L2 = 5.81% counts restrictions that leave the primary go/no-go advice untouched in **every** case. This is adjacent to the Journal 1 §14.1 concession — *"the withheld types are withheld from a rule set that could not have produced them"* — but it is a sharper and more general statement, because it holds regardless of what the rule set can produce: **it follows from the governance mapping alone.**

**E-GE-3 revised** to a verified structural statement rather than a pass/fail check:

| | Revised treatment |
|---|---|
| **E-GE-3a** | **Assert** that the `Go`/`Delay` bit is identical in C1 and C2 for 100% of episodes. A violation would be an implementation error, so it is an assertion, not a criterion |
| **E-GE-3b** | **Report** the share of C1≠C2 divergences that consist solely of withheld `DepartureTime` and/or `Duration`. Expected: 100% |
| **E-GE-3c** | **State in the write-up**, as a structural property of the governance mapping: *at CAUTION, restriction removes advisory detail and never alters the primary departure recommendation* |

**This is the most consequential item in the revision**, and it did not come from the review — it came from checking a criterion that looked fine. It belongs in front of the supervisor independently of whether the replication ever runs, because it bears directly on how Δ_L2 should be described in the thesis and in Journal 1 v2.

---

## 6. Consolidated revised predictions

Replacing R1 §10. Written before execution.

1. **G-A fails E-GC-1** with `DepartureTime` at exactly 0% — structural (R1 §2, unchanged and still correct).
2. **G-A fails E-GC-2a and E-GC-2b.** *(R1's prediction 2 — that `Duration` is a deterministic function of `Go`/`Delay` — was wrong and is withdrawn; see §1.2. The revised prediction rests on `Duration` being a pure concurrent threshold, which is the correct statement.)*
3. **G-A emits `Duration` at a non-trivial rate**, as a concurrent threshold at `P_OK`. So `Duration` is **reachable without forecast skill but vacuous as a forecast claim**, while `DepartureTime` is **strictly unreachable**. The two are not equivalent, and R1 treated them as more alike than they are.
4. **G-B's forecast-dependent rates fall substantially below G-L's** 36.12% and 72.56%. The gap is the leak in capability terms and remains unquantified.
5. **E-ES-5 is the criterion most likely to bind**, and FAR_acc should degrade with lead, most visibly under S9's 12 h variant.
6. **G-L's FAR_acc will be ≈0 at every lead** — the leak expressed as a safety metric.
7. **E-GE-3a and E-GE-3b hold at 100%**, by construction rather than by result.
8. **Whether G-B passes E-GC-1, E-GC-2 and E-ES-5 is genuinely open.** That is what the replication is for.
9. **A-CHK-6 will record C1 satisfied, C2 not satisfied**, for every condition including G-A and G-B.

---

## 7. Cumulative revision ledger

Every original is preserved in place. Nothing is deleted or rewritten; superseded items remain readable in the documents that carry them.

| Item | Original (pre-registered, 17 Nov) | Revision 1 | **Revision 2** | Reason for the change |
|---|---|---|---|---|
| **N1** type coverage ≥10% | **PASS** — Go 69.38%, Delay 30.62%, DepartureTime 36.12%, Duration 72.56% | → E-GC-1, threshold retained | unchanged | — |
| **N2** arm divergence ≥20% | **FAIL** — 2.69% unstratified; 46.33% stratified | → E-GE-1, **descriptive, no gate** | unchanged | Structurally capped at `P(S=CAUTION)` = 5.81%; the bar was unreachable |
| **N3** withheld realisation ≥50% | **FAIL** — 46.33% | → E-GE-2, **≥30% adequacy marker** | unchanged | Re-justified from pool need, not from the observed value |
| **N4** boundary share ≥30% | **FAIL** — 6.17%, 564 cases | → E-CA-1/2/3, **absolute counts** | unchanged | Wrong units: 30% would need ε ≈ 0.25 m |
| `GATE_PASS_as_preregistered` | **false** | **Retired** for future use; value stands | unchanged | A composite over heterogeneous quantities is not actionable |
| **type non-redundancy** | not in the original gate | **E-GC-2**: `H(type_i│type_j) > 0` all pairs | **REPLACED by E-GC-2a/b/c** — forecast-dependent types only, stratified by concurrent exposure | **Unpassable:** `Delay ≡ ¬Go`, so it failed for every generator and discriminated nothing |
| **R1 §2 claim** `Duration ≡ f(Go)` under persistence | — | asserted | **WITHDRAWN.** `Duration` is a concurrent threshold at `P_OK ≠ P_GO`, so it adds a bit beyond the `Go` bit | Arithmetic error in R1, found while fixing E-GC-2 |
| **R1 prediction 2** | — | "G-A fails E-GC-2 because `Duration ≡ f(Go)`" | **WITHDRAWN**, replaced by revised prediction 2 | Follows from the above |
| **target-hour spread** | — | **E-GC-3**: modal target ≤70%, pooled | **REVISED** — computed within hour-of-window strata | Pooling guarantees 09:00 over-representation from the window's shape, not the generator's behaviour |
| **forecast skill** | — | **E-ES-1/2/3/4**: MAE, skill score vs persistence, reliability, G-L diagnostic | **STRENGTHENED to E-ES-1…7** — threshold-specific contingency metrics on two threshold families; **FAR_acc as the headline**; FRR reported separately and never netted; mandatory cell counts with `n ≥ 30` | Mean error is the wrong instrument for a threshold-crossing decision, and symmetric error treats unequal costs as equal |
| **divergence direction** | — | **E-GE-3**: ≥95% conservative | **REVISED to E-GE-3a/b/c** — assertion plus a reported structural statement | True by construction (`A_AI` is nested). Its triviality yields the finding in §5.2 |
| **L-CHK-6** skill ceiling | — | **Gate** | **RECLASSIFIED as diagnostic.** Becomes a gate only once a measured forecast benchmark for this site exists | No measured benchmark was ever obtained; the bound rested on intuition |
| **L-CHK-1…5, 7, 8** | — | gates / checks | unchanged | Sound as written |
| **availability** | — | not distinguished from causality | **NEW: A-CHK-1…6.** Declarations, not gates. Primary run is **C1-valid, C2-invalid** | Chronological causality and operational availability are different properties; R1 conflated them |
| **V-2** validation | — | G-A profile ≈ prototype, residual = `R-SAFE-001` deferred | **REVISED** — G-A also emits `Duration`, which the prototype never does. Residual is **two** gaps: no SAFE rule, and no `Duration` rule at all | Follows from §1.2: `Duration` is reachable without forecast skill, so its absence from the prototype is a rule-set gap, not an information gap |
| **R1 §2 structural claim** | — | "two of four advice types are forecast-dependent, hence unreachable" | **SHARPENED**: `DepartureTime` is **strictly unreachable** without forecast skill; `Duration` is **reachable but unsupported**. Still two types affected, by two different mechanisms | The original statement was right in direction and imprecise in mechanism |
| Original case table, results JSON, gate script | 9,135 episodes, MD5-verified | re-used unchanged as **G-L** | unchanged | Any de-leaked generator is a new file |

**Reporting rule, unchanged and now cumulative.** The write-up publishes the original criteria, Revision 1 and Revision 2 side by side with the reason for each change. Three of the five R1-era revisions are corrections of my own errors, and saying so is cheaper than having an examiner find a criterion that could not have passed.

---

## 8. What this revision does not fix

1. **Nothing has been executed.** Every prediction in §6 is an argument.
2. **The 0.10 FAR_acc bound in E-ES-5 is a judgement**, not an evidence-derived figure, and no source can supply one.
3. **C2 operational availability cannot be achieved on this data at all.** A-CHK makes the gap visible; only real issue-time forecasts close it.
4. **L-CHK-6 stays uninterpretable** until a measured benchmark exists, so G-B's skill can be compared to persistence and climatology and to nothing else.
5. **The E-GC-2 strata depend on cell sizes that are unknown before the run.** If the forecast-dependent types concentrate in few exposure deciles, the `n ≥ 50` rule may leave fewer than three usable strata, and the criterion would then be **indeterminate rather than failed** — which must be reported as such.
6. **§5.2's structural finding has not been checked against the canonical replay.** It follows from the governance mapping as documented, and confirming it against the published Δ_L2 artefacts is a separate read-only task that has not been done.
7. **I have now found three non-discriminating criteria in my own specification.** The base rate suggests more may remain, and the leak checks are a guard against one failure mode, not against this one.
8. **RESOLUTION (MFWAM) remains out of scope.** All of this is PRIMARY only.

---

## 9. Decisions, revised

| | Decision | Who | Recommendation |
|---|---|---|---|
| **D-4h** | **New, and independent of the replication.** Record in the thesis and in Journal 1 v2 that **graduated restriction at CAUTION cannot alter the primary departure recommendation** — it removes advisory detail only (§5.2). Verify first against the canonical replay, read-only | Supervisor + author | **Act on this regardless of what else happens.** It follows from the governance mapping alone, bears directly on how Δ_L2 is described, and is far better stated by the author than discovered by an examiner |
| **D-3⁗** | Authorize execution of the R2 specification. New files only; G-L untouched; no participants | Author | **Proceed** — but implement and pass L-CHK-1…5, 7, 8 and record A-CHK-1…6 **before** computing a single criterion |
| **D-5‴** | Accept that the forecast archives now carry **four** justifications: the staleness strand; generating the forecast-dependent types with skill; **C2 operational availability**; and **calibrating what "reasonable skill" means at this site** (§4.2) | Supervisor | **Put it as one decision with four payoffs.** It is the same request as before, with a much stronger case than when it was a single-strand concern |
| **D-4i** | Whether the C1 / C2 distinction should be stated in the **abstract** of Journal 1 v2, not only in its limitations | Supervisor | **Yes.** It applies to the published Δ_L2, not just to this replication, and an examiner who notices it unaided will wonder what else was not named |

**What I would do first.** D-4h, because it is read-only, costs almost nothing, is independent of everything else here, and is the one item in this revision that changes what the thesis says rather than how a future experiment is run.
