# Causally Valid N1–N4 Replication — Specification, Revision 3

**Prepared:** 17 November 2026 · **Author of this document:** Claude (Cowork session) · **Status:** **specification only. The causal replication has still not been executed.**

**What was run for this document.** Nothing of the replication. Four **read-only** reads of canonical files were made to verify D-4h as directed: `scripts/condition_comparison.py`, `data/prediction-register.csv`, `docs/canonical/architecture-illustration.md` and `docs/analysis/final-research-chain-lock.md`. No file was modified; `git status` reports no tracked file changed.

**What this revises.** Revisions 1 and 2 stand unaltered and carry pointers. Three items change: **E-GC-2b** (the bin-width defect you identified), **E-ES-7** (the oracle/threshold conflation), and **D-4h**, whose status drops sharply after verification. One further criterion is retired as redundant. §6 is the cumulative ledger across all three revisions.

---

## 1. E-GC-2b was defeated by bin width — corrected

### 1.1 The defect, confirmed

R2 §1.4 proposed: stratify into deciles of concurrent exposure `e(h)`; require within-stratum variance of the predicted run length `> 0`.

Under persistence the run length is

> `run = horizon if e(h) ≤ e_ok else 0`

a step function with a single breakpoint at `e_ok` (the `P_OK` cutoff). **Any decile that straddles that breakpoint contains episodes on both sides of it**, so the run length takes both values inside that bin and the within-bin variance is positive. Persistence would therefore **pass** E-GC-2b in the straddling decile — not because it carries forecast information, but because the bin has width. Since `e_ok` is a percentile of a calibration set and the deciles are of the evaluation set, the two will not align, so at least one straddling decile is essentially guaranteed.

The criterion measured bin width and reported it as forecast dependence.

### 1.2 The design rule this yields

The defect generalises, so the rule is stated explicitly to be applied to every future criterion here:

> **A discriminator must be a quantity that is exactly zero under persistence by construction — not merely small, and not "small in a well-chosen bin".** Any binned, smoothed or thresholded statistic can leak a non-zero value from the structure of the bins rather than from the generator.

Within-bin variance fails this rule. Cardinality, step-function conformity and residual-information tests satisfy it, because each is **identically zero under a deterministic step function of a single scalar**.

### 1.3 E-GC-2b revised — four bin-free tests

All computed on the **numeric predicted run length**, which requires a specification change: the generator currently emits `Duration` as set membership only. **The run length must be logged as an integer diagnostic alongside the advice set.** Without it none of these tests can be computed.

| | Test | Mechanism | Exactly-zero property under persistence | Threshold |
|---|---|---|---|---|
| **E-GC-2b-i** | **Cardinality of predicted run lengths** | Count distinct values of `run` across the evaluation set | Persistence admits **exactly two** values, `{0, horizon}` | **≥ 4 distinct values** (>2 is the bare structural test; 4 is the exploratory bar) |
| **E-GC-2b-ii** | **Single-breakpoint step conformity** | Fit the best non-increasing single-breakpoint step function of `e(h)` to `run`; report the share of episodes it fails to reproduce exactly | Residual is **exactly 0** — persistence *is* that step function | **≥ 10% of episodes unexplained** |
| **E-GC-2b-iii** | **Near-tie discordance, by distance from the breakpoint** | For pairs with `│Δe│ < τ` (τ pre-registered at 0.05 percentile points) and different `run`, report the distribution of each pair's distance from the fitted breakpoint | Under persistence **every** discordant near-tie pair lies within τ of the breakpoint — the distribution is a spike at zero | **≥ 50% of discordant pairs beyond 5 percentile points from the breakpoint** |
| **E-GC-2b-iv** | **Residual information from calendar** | Baseline: flexible monotone fit of `run` on the full concurrent vector `(wind, wave, precip)`. Then test whether `(month, hour-of-window)` adds explanatory power | Baseline fit is **exact**, `R² = 1.0`, leaving nothing for the calendar to explain | Baseline `R² < 0.95` **and** a non-null calendar contribution |

**b-i and b-ii are primary** — cheapest, exact, assumption-free. **b-iii and b-iv are confirmatory and quantitative.** b-iii is the one that directly repairs the original intent: it keeps the matched-pairs idea but conditions on distance from the breakpoint, which is precisely the artefact the decile version absorbed.

**Why b-iii needs the breakpoint correction.** Two episodes whose exposure differs by 0.01 percentile points can still straddle `e_ok` and receive run lengths 0 and 9 under persistence. So near-tie discordance *alone* does not discriminate; **where** the discordance sits does. Under persistence it can only occur at the breakpoint; under G-B it occurs anywhere, because at equal concurrent exposure a favourable climatological trajectory lengthens the predicted run.

### 1.4 E-GC-2a retired as redundant

R2 §1.4 kept E-GC-2a (decile-stratified `DepartureTime` emission rate). It is **bin-robust** — persistence gives a rate of exactly 0 in every stratum, so no bin width can rescue it — but it is **redundant**: for `DepartureTime`, existing at all *is* the forecast-dependence test, and that is already E-GC-1's ≥10% bar, with target-hour spread already covered by E-GC-3.

**E-GC-2a is withdrawn and folded into E-GC-1**, with a note in the ledger. Fewer criteria is better here: each one is another chance for the class of error this revision keeps finding.

**So E-GC-2 now applies to `Duration` only**, which is correct — `Duration` is the type whose forecast dependence is genuinely in question, because `DepartureTime`'s is settled by its mere existence.

---

## 2. E-ES-7 conflated two different oracles — corrected, and the correction is useful

### 2.1 The defect, confirmed

R2 §2.3 predicted G-L's false-acceptable rate would be *"≈0 at every lead, by construction"*. **That holds only for the internal threshold family.**

G-L reads realised forward values, so it is an oracle for **its own exposure index** `e`. It is **not** an oracle for the physical thresholds. The exposure index is the **arithmetic mean of three percentile ranks**; the architecture aggregates by **max-severity** over separate per-variable thresholds. These are different functionals of the same variables, so an hour can satisfy `e ≤ P_OK` while wave exceeds 1.0 m — low wind and low rainfall pull the mean down below the cutoff while the wave component alone would classify CAUTION.

So:

| | Family | G-L's false-acceptable rate |
|---|---|---|
| **T-INT** | the generator's own `P_OK` cutoff | **Exactly 0, by construction.** A wiring check, nothing more |
| **T-PHYS** | wave 1.0 / 1.25 m, wind 21.6 / 27.0 kn, rain 10 / 20 mm/hr | **Empirically unknown, and possibly substantial.** Not predicted, and R2's prediction 6 is withdrawn |

### 2.2 The correction turns G-L into a decomposition instrument

`FAR_acc` on T-PHYS confounds two error sources. G-L separates them, because its forecast error is identically zero:

| Condition | T-PHYS false-acceptable rate contains |
|---|---|
| **G-L** | **index–threshold mismatch only** — forecast error is zero by construction |
| **G-B** | mismatch + forecast error + interaction |
| **G-B − G-L** | ≈ the **forecast-error contribution**, which is the quantity E-ES actually wants |

This is a better reason to run G-L than the one R2 gave. It was included as the leakage estimate; it is **also the only available zero-forecast-error baseline**, and without it the T-PHYS metrics cannot be attributed to forecasting at all.

### 2.3 E-ES-8 — index–state concordance (new, and needed before any human study)

A pure design property of the generator against the classifier, computed on **observed** values with no forecasting involved:

| | Metric | Definition |
|---|---|---|
| **E-ES-8a** | Permissive mismatch | `P(e(h) ≤ P_OK │ S(h) ∈ {CAUTION, UNSAFE})` — how often the generator calls an hour workable that the architecture does not |
| **E-ES-8b** | Restrictive mismatch | `P(e(h) > P_OK │ S(h) = SAFE)` — the converse |
| **E-ES-8c** | Component attribution of 8a | Which variable drove the architecture's classification in mismatch cases. Expected: overwhelmingly wave, since `g_o` is 97.6% of activation |

**Why this matters before the rubric is ever used.** If E-ES-8a is high, the generator will routinely produce advice that reads as reckless to an expert rater **for index-design reasons that have nothing to do with governance**. In the C0 and C1 arms that noise is unfiltered, so a rating study could attribute to "absence of governance" what is actually an artefact of the exposure index's aggregation. That confound must be measured and declared before raters are recruited, not diagnosed afterwards from their scores.

**The yardstick caveat, repeated wherever these numbers appear:** T-PHYS and E-ES-8 use the architecture's thresholds as an **evaluation yardstick only**. They are not an independent safety reference — `research/d4-critical-review.md` §1 established that none exists.

### 2.4 A tension that must be reported rather than resolved silently

Mismatch could be reduced by switching the exposure index to max-severity aggregation — which is exactly S4's `max` variant. But **that makes the generator more like the classifier, which is precisely the independence the generator exists to have.**

So: *reducing index–threshold mismatch costs generator independence.* This is the same shape as the tension already recorded in `research/d4-critical-review.md` §2.6 — information parity versus non-degeneracy — and it is the third such conflict in this design. The pattern is worth naming: **this design keeps producing pairs of desiderata that cannot both be maximised, and the honest move each time is to report the trade-off with both endpoints measured, not to pick one and present it as the design.** S4 should therefore be reported as a declared trade-off curve, not as a robustness check.

---

## 3. D-4h verified against the canonical replay — and substantially downgraded

### 3.1 The structural claim is TRUE and exactly confirmed **[VERIFIED, read-only]**

From `scripts/condition_comparison.py` lines 81–104, quoted verbatim:

```python
FULL       = frozenset({"Go", "Delay", "DepartureTime", "Duration"})
RESTRICTED = frozenset({"Go", "Delay"})
"C1": {SAFE: FULL, CAUTION: FULL,       UNSAFE: EMPTY},
"C2": {SAFE: FULL, CAUTION: RESTRICTED, UNSAFE: EMPTY},
```

- C1 and C2 are **identical at SAFE and at UNSAFE**, and differ **only at CAUTION**.
- At CAUTION the difference is exactly `FULL \ RESTRICTED = {DepartureTime, Duration}`.
- `Go` and `Delay` are in **both** sets at SAFE and at CAUTION, and in **neither** at UNSAFE.

So the `Go`/`Delay` bit is identical under C1 and C2 at **every** hour, and D-4h holds: **graduated restriction at CAUTION removes advisory detail and never alters the primary departure recommendation.**

The divergence metric is confirmed set-level — `sum(1 for x, y in zip(sets[a], sets[b]) if x != y)`, frozenset inequality, no comparison of advice content. Two incidental confirmations: C3's table is byte-identical to C1's, corroborating the known C1 ≡ C3 identity; and the canonical C2↔C1 figure of **4.4819%** matches Δ_L2 RESOLUTION = 4.48% exactly, as the structural identity requires.

### 3.2 But it is already documented — in three places

**`docs/canonical/architecture-illustration.md` §209 states it directly:**

> *"When S = CAUTION, the Go recommendation type remains available but is presented with a caution qualifier… The recommendation* type *is unchanged — it is still a Go/no-go assessment. This design preserves set containment (Go ∈ A_AI(CAUTION) and Go ∈ A_AI(SAFE) — same type in both)."*

**§203 supplies the domain rationale**, citing Gao (2024) and Rahim et al. (2024): under marginal conditions fishers continue to make go/no-go and near-shore decisions but do not attempt to optimise departure timing or trip duration. **§386** summarises the CAUTION mode as *"Gets go/no-go and delay only"*.

**`data/prediction-register.csv` P22 states the set-level identity and registered it as a test:**

> *"C1 and C2 agree at SAFE (both full) and at UNSAFE (both empty). They can differ ONLY at CAUTION. Divergence must therefore equal the CAUTION rate exactly. Regression check that the comparison harness is wired correctly."*

with the resolution note recording that *"the STRUCTURAL claim held exactly — C1/C2 divergence still equals the CAUTION rate to 2 d.p."*

**`docs/analysis/final-research-chain-lock.md` §81 and §315** already correct an earlier, harsher characterisation of `A_AI(CAUTION) = {Go, Delay}`, settling on *"rationale rather than fiat while still denying validation and optimality"*.

**So this was a deliberate design decision with a cited rationale, registered as a prediction, used as a wiring regression check, and already corrected once for over-harsh description.** R2 §5.2 called it *"the most consequential item in the revision"* and R2 §9 advised acting on it *"regardless of what else happens"*. **Both overstated it.**

### 3.3 The residual, stated narrowly

What is **not** stated anywhere I found is the step from the set-level fact to its measurement consequence:

> Because `Go` and `Delay` survive the CAUTION filter, **Δ_L2 = 5.81% measures exclusively the withholding of timing and duration detail.** No part of it is a change in go/no-go advice — and this follows from the governance mapping alone, independently of what any rule set can produce.

The manuscript's `:1462` concession is adjacent but differently grounded: it says divergence *"counts admissible-set differences, not differences in what was actually recommended"* and attributes the gap to the prototype generating only one conclusion type. **The mapping-level statement is stronger**, because it holds for a complete rule set too. That is a one-sentence sharpening of an existing limitation, not a finding.

**D-4h is therefore downgraded** from an independent action item to a **wording check** on how Δ_L2 is described in the thesis and Journal 1 v2.

### 3.4 My own error pattern, since it bears on how to read this series

**Three times now I have presented as new a finding already in this repository**: the Jeong & Im ← Wolfson derivation (in `notes/`), the 1.25 m NORDFORSK provenance (in Appendix C C.9), and now D-4h (in `architecture-illustration.md` §203/§209 and the prediction register).

The cause is identifiable: I have been deriving consequences from the formal mapping and the data **without first searching the canonical tree for them**. The fix is procedural and I am adopting it for the rest of this work — **search `docs/canonical/`, `notes/` and `data/prediction-register.csv` before characterising anything as new.** The register in particular has turned out to document structural claims I assumed nobody had stated.

This matters beyond etiquette: a review that keeps rediscovering the project's own documented positions **overstates how much is unresolved**, which is a bias in the opposite direction from the usual one and is just as unhelpful to a supervisor meeting.

---

## 4. Revised predictions

Replacing R2 §6 where they differ.

1. **G-A fails E-GC-1** with `DepartureTime` at exactly 0% — unchanged, structural.
2. **G-A fails E-GC-2b-i** (exactly 2 distinct run lengths) and **E-GC-2b-ii** (step residual exactly 0). *R2's decile-variance prediction is withdrawn; persistence would have passed it in the straddling bin.*
3. **G-A's discordant near-tie pairs all lie within τ of the breakpoint** (E-GC-2b-iii), giving a spike at zero.
4. **G-B's forecast-dependent rates fall below G-L's** 36.12% and 72.56%. Gap unquantified.
5. **E-ES-5 is the criterion most likely to bind**, degrading with lead, worst under S9's 12 h variant.
6. **G-L's FAR_acc is exactly 0 on T-INT and non-zero on T-PHYS.** *(R2's "≈0 at every lead" is withdrawn.)* Its T-PHYS value is the index–threshold mismatch baseline and is **not predicted**.
7. **E-ES-8c attributes mismatch overwhelmingly to wave**, consistent with `g_o` = 97.6% of activation.
8. **E-GE-3a and E-GE-3b hold at 100%** — now **verified** analytically from the canonical comparator tables (§3.1), not merely predicted.
9. **A-CHK-6 records C1 satisfied, C2 not satisfied** for every condition.
10. **Whether G-B passes E-GC-1, E-GC-2b and E-ES-5 remains genuinely open.** That is still the point of the replication.

---

## 5. What this revision does not fix

1. **The causal replication has not been executed.** Every prediction is an argument.
2. **E-GC-2b-ii needs a monotone step fit that is not yet specified in detail** — the breakpoint search is trivial for one scalar, but the "flexible monotone fit" in b-iv is a modelling choice that could be gamed, so it must be fixed in code before the run, not chosen after.
3. **The E-GC-2b thresholds (4 distinct values, 10% unexplained, 50% beyond 5 pp) are judgements.** Only the structural facts beneath them — exactly 2 values, exactly 0 residual, a spike at the breakpoint — are derived.
4. **τ = 0.05 percentile points in b-iii is arbitrary** and must be pre-registered as such, with sensitivity at 0.02 and 0.10.
5. **E-ES-8 cannot say whether mismatch is a defect.** It is partly intentional, since independence requires a different aggregation. The metric quantifies a trade-off; it does not adjudicate it.
6. **The 0.10 FAR_acc bound in E-ES-5 remains a judgement**, unchanged from R2 §8.
7. **C2 operational availability still cannot be achieved on this data**, and L-CHK-6 stays diagnostic for want of a measured benchmark.
8. **Four non-discriminating criteria have now been found in my own specifications** — E-GC-2 (unpassable), E-GC-3 (structurally confounded), E-GE-3 (true by construction), E-GC-2b (defeated by bin width) — plus one redundant (E-GC-2a). The rate is not obviously declining, and the design rule in §1.2 is a guard against one mechanism, not all of them.
9. **RESOLUTION (MFWAM) remains out of scope.**

---

## 6. Cumulative revision ledger

Every original is preserved in place; nothing is deleted or rewritten.

| Item | Original (pre-registered 17 Nov) | R1 | R2 | **R3** | Reason for the latest change |
|---|---|---|---|---|---|
| **N1** ≥10% type coverage | **PASS** — 69.38 / 30.62 / 36.12 / 72.56% | → E-GC-1 | unchanged | **absorbs E-GC-2a** | Redundancy |
| **N2** ≥20% divergence | **FAIL** — 2.69% / 46.33% | → E-GE-1 descriptive | unchanged | unchanged | — |
| **N3** ≥50% withheld realisation | **FAIL** — 46.33% | → E-GE-2, ≥30% marker | unchanged | unchanged | — |
| **N4** ≥30% boundary share | **FAIL** — 6.17%, 564 cases | → E-CA-1/2/3 absolute | unchanged | unchanged | — |
| `GATE_PASS` composite | **false** | **retired** for future use | unchanged | unchanged | — |
| type non-redundancy | — | **E-GC-2** all pairs | **replaced** by 2a/2b/2c, decile-stratified | **2a withdrawn** (redundant); **2b replaced** by bin-free i–iv; **2c superseded** by 2b-iv | 2b's within-bin variance is positive under persistence whenever a bin straddles `e_ok` |
| `Duration ≡ f(Go)` claim | — | asserted in R1 §2 | **withdrawn** | — | `P_GO ≠ P_OK`, so it adds a bit beyond the `Go` bit |
| run length logging | — | not specified | not specified | **NEW requirement** — log the integer run length, not just set membership | None of E-GC-2b is computable without it |
| target-hour spread | — | **E-GC-3** pooled, ≤70% | **revised** — within hour-of-window strata | unchanged | — |
| forecast skill | — | **E-ES-1…4** MAE / skill score | **strengthened to E-ES-1…7**, threshold-specific, FAR_acc headline | **E-ES-7 corrected**; **E-ES-8a/b/c added** | An oracle for future exposure is not an oracle for separate physical thresholds |
| G-L's role | — | leakage estimate | leakage estimate + skill diagnostic | **also the zero-forecast-error baseline** for decomposing T-PHYS error | Follows from the E-ES-7 correction |
| divergence direction | — | **E-GE-3** ≥95% | **revised** to 3a/3b/3c structural | **VERIFIED analytically** from the canonical comparator tables | Read-only verification, §3.1 |
| **L-CHK-6** | — | gate | **diagnostic** | unchanged | — |
| availability | — | not distinguished | **A-CHK-1…6**, C1 vs C2 | unchanged | — |
| **V-2** validation | — | residual = deferred SAFE rule | **revised** — two gaps | unchanged | — |
| **D-4h** | — | — | *"most consequential item"*, act regardless | **DOWNGRADED to a wording check.** Verified true; **already documented** in `architecture-illustration.md` §203/§209/§386, `prediction-register.csv` P22, and `final-research-chain-lock.md` §81/§315 | Read-only verification found three prior statements of it |
| R2 prediction 6 (G-L FAR_acc ≈0) | — | — | asserted | **withdrawn** | True on T-INT only |
| R2 prediction 2 (decile variance) | — | — | asserted | **withdrawn** | Bin-width artefact |

**Reporting rule, cumulative.** The write-up publishes the original criteria and all three revisions side by side with reasons. **Five of the revisions are corrections of my own errors**, and recording that is cheaper than having an examiner find a criterion that could not discriminate.

---

## 7. Decisions, revised

| | Decision | Who | Recommendation |
|---|---|---|---|
| **D-4h′** | **Downgraded.** Add one sentence to the thesis and Journal 1 v2 stating that Δ_L2 measures the withholding of timing and duration detail only, and never a change in go/no-go advice — **as a sharpening of the existing `:1462` limitation**, citing `architecture-illustration.md` §209. **Do not present it as a new finding** | Author | **One sentence, in the limitations.** Verified true and already designed-for; the only gap was the measurement consequence |
| **D-3⁵** | Authorize execution of the R3 specification. New files only; G-L untouched; no participants. Add run-length logging first | Author | **Proceed** — L-CHK-1…5, 7, 8 passing and A-CHK-1…6 recorded **before** any criterion is computed |
| **D-5⁗** | Unchanged: the forecast archives carry four justifications — staleness, forecast-dependent type generation, C2 availability, and skill calibration | Supervisor | **One decision, four payoffs** |
| **D-4j** | **New.** Accept that **E-ES-8 must be measured and declared before raters are recruited.** If permissive mismatch is high, the C0/C1 arms carry generator-design noise that a rating study would misattribute to absence of governance | Supervisor + author | **Accept.** It is cheap, it runs on existing data, and discovering it from rater scores afterwards would be unrecoverable |
| **D-4k** | **New, procedural.** Before anything in this series is characterised as new, search `docs/canonical/`, `notes/` and `data/prediction-register.csv` first | Author | **Adopt.** Three of three structural "findings" were already documented; the series has been overstating how much is unresolved |

**What I would do first.** D-4j, because it is the only item here that can invalidate a human study after the fact and it costs one query on data already in hand. D-4h′ is now a sentence, not a project.
