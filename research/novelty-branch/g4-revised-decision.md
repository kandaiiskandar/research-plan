# G4 — Revised Research Decision

**Prepared:** 17 November 2026 · **Author:** Claude (Cowork session) · **Status:** exploratory research branch, v2.

**Versioned record.** The four v1 documents of 17 Nov 2026 — `novelty-literature-matrix.md`, `candidate-research-gaps.md`, `evaluation-feasibility.md`, `novelty-go-no-go-decision.md` — are **preserved unedited**, including their CONDITIONAL verdict. This document supersedes v1's G4 reasoning and its decision; §5 itemises every conflict. **Frozen thesis RQ1–RQ3 and all canonical artefacts are untouched. No algorithm was implemented, no experiment run, no external request made.**

**Companions:** `g4-formal-definition-review.md`, `g4-prior-art-challenge.md`, `g4-minimum-evaluation-design.md`.

---

## The decision

# NO-GO

**G4 is not a viable novel methodological contribution.** Its reachability half is an established concept under new terminology. Its support half rested on a definition that the project's own data refutes, and the corrected definition is probably a restatement of the value-of-information stopping condition. What remains is a **useful empirical distinction without a novel method** — option (b) of the three the brief offered.

**This reverses v1's CONDITIONAL**, and it does so without running either of the experiments v1 proposed, because those experiments tested the wrong quantity.

---

## 1. Why, in four findings

**F1 — The support definition was refuted by the project's own measurements.** v1 classified an output as *unsupported* when it was a deterministic function of the concurrent observation. But the fitted damping for wave is **α = 0.970**, meaning persistence is very nearly the error-minimising wave predictor at this site, and wave drives **97.6%** of CAUTION activation. So v1's criterion classifies the **best available wave predictor** as unsupported, while classifying as *supported* a surrogate whose measured false-acceptable rate at lead 1 was **9.8% against persistence's 9.4%** — worse. **A criterion that ranks a better predictor below a worse one is not measuring warrant.** It measures the functional form of the generator, which is neither necessary nor sufficient for anything normative.

**F2 — Three concepts were conflated, and the one v1 used requires no outcome data.** `g4-formal-definition-review.md` separates **incremental information** (property of a procedure pair; needs no outcomes), **predictive validity** (property of a procedure against outcomes), and **evidential adequacy** (`∃g ∈ G : PV(g; t, E) ≥ τ_t` — existential over a declared procedure class, with a type-specific threshold grounded in consequence). They are logically independent in both directions, demonstrated on measured data. **v1 used the first and called it the third.** A criterion of warrant that never consumes an outcome cannot be one.

**F3 — The reachability claim does not survive a one-line counterexample.** `DepartureTime` was called *structurally unreachable* from concurrent observations on the strength of a 0.00% production rate. But the architecture's own `g_t` is computable from the clock, so a procedure emitting *"depart after sunrise at 06:20"* produces a `DepartureTime` output from concurrent information alone. The 0.00% reflects **the tested generator's predicate**, not the evidence class. An observed rate of zero is consistent with logical impossibility, algorithm-specific unreachability and low empirical frequency alike, and **distinguishes none of them.**

**F4 — Both halves have established homes.** Reachability relative to a declared procedure class is **realizability** — equivalently identifiability, monitorability, observability, or Gorostiaga & Sánchez's finite admissibility, which already does the per-output-value version with lemmas. And the project's own frozen position **already concedes Bauer et al. 2011 and Manski's partial identification**. Adequacy, in its corrected existential form, is the **acquire-or-decide stopping condition** of value-of-information analysis: *is expected loss on the current evidence acceptable, or is further evidence worth its cost?* That tradition is decades old, with an active cost-sensitive active-feature-acquisition literature — **and it is the literature v1 never read.**

---

## 2. What this means for the three options the brief offered

| | Option | Verdict |
|---|---|---|
| **(a)** | Established concept, new terminology | **Reachability: yes, confirmed.** Adequacy: **probably yes**, pending the one reading task in §4 |
| **(b)** | **A useful empirical distinction without a novel method** | **This is what survives, and it has real value** — just not as a CS contribution. Separating "no permissible procedure emits this type from this evidence" from "one does, but the result would not be warranted" keeps a specification honest, and this project's own data illustrates it cleanly |
| **(c)** | A genuinely unresolved computational problem | **Not established.** The only candidate is the joint problem, which is a combination of per-type thresholds (AC-RAC, Sadinle, Role-Stratified CRC), evidence-indexed validity (Zaffran et al.) and an acquire-or-decide condition (VOI). **The brief forbids counting a combination as novelty**, and no problem was identified that is not solved by solving the parts |

**The absence of an identical three-state taxonomy is not evidence of anything.** Its absence is explained by the parts being studied separately under their own established names.

---

## 3. What is kept

**The distinction retains value in exactly one role: a limitation-framing device for the thesis, which requires no novelty claim and which the lock permits.**

Stated correctly, and only this far:

> The admissible advisory set `A_AI(SAFE)` ranges over output types whose derivation depends on information the specified inputs do not provide. Under the procedures implemented, one type is not produced at all and another is produced as a deterministic function of the present observation. Whether either would be *warranted* is a separate question that this work does not answer, since warrant requires outcome data and a consequence-grounded threshold, and the domain supplies neither.

**Three things this wording deliberately does not say**, each because v1 said it and was wrong: that the unproduced type is *unreachable in principle*; that the deterministic type is *unsupported*; and that any of it is novel.

**The measurements are unaffected.** `results-causal-replication.json` is unchanged and nothing executed is withdrawn — only v1's reading of it.

---

## 4. What would reopen this

| | Condition | Cost | Why it is not pursued now |
|---|---|---|---|
| **R1** | **Read the VOI / EVSI / active-feature-acquisition primary literature** and establish whether evidential adequacy over a procedure class differs from the acquire-or-decide stopping condition | Days of reading. Nothing external | **The single decisive item.** If it does not differ, G4 is closed permanently. The prior that it differs is low |
| **R3** | Read AC-RAC's Appendix D and determine whether **consequence-derived** `τ_a`, as opposed to coverage-equalising α, is constructible inside its framework | Days | **If it is, the remaining daylight closes.** AC-RAC is peer-reviewed, ICML 2026, four months old |
| **R2** | Establish the venue of Gorostiaga & Sánchez and position finite admissibility fully against `G`-reachability | Days | Would likely strengthen the (a) verdict |
| **R4** | Read Dempster–Shafer conflict and reliability discounting primaries | Weeks | Plausibly contains closer prior art on conflict-conditioned admissibility |

**R1 and R3 are reading, not research, and either can close G4 for good.** Neither is a reason to hold the decision open: a NO-GO that two reading tasks could confirm is more useful than a CONDITIONAL that defers the judgement.

---

## 5. Conflict ledger — v1 against v2

| Item | v1 | v2 | Reason |
|---|---|---|---|
| **Decision** | **CONDITIONAL**, with six conditions K1–K6 | **NO-GO**, with four reopening conditions | The surviving gap rested on a refuted definition |
| Definition of support | residual information beyond a trivial baseline | **Withdrawn.** Replaced by three separated concepts: incremental information, predictive validity, evidential adequacy | Conflated a procedure property with a warrant claim; refuted by α = 0.970 |
| "`Duration` is reachable but unsupported" | asserted as a measured finding | **Withdrawn.** It has II = 0 relative to persistence; on predictive-validity grounds the opposite holds | Definition error |
| "`DepartureTime` is structurally unreachable" | asserted | **Withdrawn.** Algorithm-specific unreachability under one predicate; refuted by the sunrise counterexample | Invalid generalisation from one procedure to an evidence class |
| "The exactly-zero residual makes this a test" | offered as the design strength | **Still true, and now beside the point** — it is a clean test of the wrong quantity | — |
| Reachability's primitive | implicitly a property of the evidence class | **A property of `(E, t, G)`** with `G` an explicitly declared procedure class | Only coherent option; also where novelty evaporates into realizability |
| **K1** monotonicity test | monotone ⇒ NO-GO | **Withdrawn, both directions invalid.** Replaced by a three-arm incremental-value test whose decisive comparison is **B vs C** — evidence as features versus evidence as a mechanism | Monotonicity neither implies redundancy nor does its absence imply usefulness |
| **K2** zero-residual verification | a gate | **Withdrawn** — verified the wrong statistic | Follows from the definition correction |
| Benchmark | four candidates, none confirmed to have both properties | **One named: MIMIC-IV**, with native missingness and staleness, four distinct output types, independent outcomes, and reconstructible availability | v1 left the largest feasibility risk unresolved |
| Gorostiaga & Sánchez | "within one property's verdict domain", dismissed | **Closer than allowed** — finite admissibility already performs the reachability half, with lemmas | Re-examination under corrected definitions |
| AC-RAC | "utility elimination, not an evidence statement" | **Closer than allowed** — already has the type-specific-threshold component, peer-reviewed, with a guarantee | Re-examination |
| VOI / active acquisition | listed as an acknowledged coverage gap | **Reclassified as the centre of the target** and the decisive open item | It is where the adequacy concept already lives |
| Empirical instance as novelty evidence | "measurable rather than merely stateable" | **The measurements stand; their reading as evidence of an evidential-support phenomenon is withdrawn** | F1 |

**Nothing in v1 is deleted.** Everything above is a superseding judgement recorded alongside the original, which remains readable in its own file.

---

## 6. What this exercise does not claim

1. **No experiment was run for v2, and no algorithm was implemented.** Every judgement is analytic or rests on measurements already recorded.
2. **R1 and R4 remain unread**, so the (a) verdict on adequacy is a **reasoned expectation, not an established fact**. It is labelled as such.
3. **Gorostiaga & Sánchez's venue and peer-review status are still unknown**, which weakens the strongest reachability antecedent as a citation even as it strengthens it as a concept.
4. **The MIMIC availability-reconstruction property must be confirmed against the published schema**; it was not opened in this session.
5. **A NO-GO on G4 is not a claim that evidence-conditioned admissibility is a solved problem.** It is a claim that *this* formulation is not a distinct contribution, and that the nearest unoccupied ground — consequence-derived type-specific thresholds inside an existing action-conditional framework — is one modelling choice wide and belongs to AC-RAC's framework rather than to a new one.
6. **The thesis is unaffected.** Frozen RQ1–RQ3 stand, the lock's concessions bind, and the supervisor memorandum's Path B recommendation needs none of this. The corrected limitation wording in §3 is the only thing from this branch that should reach the thesis.

---

## 7. Recommendation

**Record NO-GO and close the branch, subject to R1 and R3 as confirmations rather than conditions.**

Do not run the three-arm evaluation, do not seek MIMIC access, and do not formulate a guarantee. The evaluation design in `g4-minimum-evaluation-design.md` is written so that it is **ready if R1 or R3 overturns this** — but on present evidence it would be spending a data use agreement and months of work to test a distinction whose two halves have established homes.

**What to do instead, and it is cheap:** carry the corrected limitation wording in §3 into the thesis and Journal 1 v2, and keep the v1 and v2 documents together as the record of how the claim was tested and withdrawn. A documented, honestly-closed novelty investigation is a defensible thing to have done; an undocumented one that quietly became a chapter is not.
