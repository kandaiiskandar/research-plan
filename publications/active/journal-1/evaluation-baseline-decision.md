# Journal 1 — Evaluation Baseline Design Decision

> **Status update 2026-09-10 — HISTORICAL DECISION RECORD.** Option C was accepted and executed by the Journal 1 Evaluation Specification Alignment. **The maintained design authority is now [`evaluation-specification.md`](evaluation-specification.md).** This document is retained as the historical record of how Option C was reached, including its §10 hypothesis assessment and §11 metric recommendations. All references below to H1–H4, "advisory scope compliance rate", "false positive rate", the retain/reconsider metric verdicts and the open items in §14 describe the state at decision time — they are historical assessments, not active instructions. The redesign they recommended (H1→F1, H2→F2, H3→E5/RQ-J2 with threshold OPEN, H4→E2 Δ_L2, utility OPEN, deterministic-census framing) has been applied to `research-design.md`, `manuscript.md` and `evaluation-specification.md`.

**Date:** 2026-09-10
**Branch:** `design/journal1-evaluation-baselines`
**Type:** experimental-design decision — **decision only, no implementation**
**Status:** ACCEPTED and EXECUTED (Option C). See `evaluation-specification.md` for the closed specification.

*Located here rather than `docs/journal1/` because Journal 1 design documents already live alongside the manuscript (`research-design.md`, `section-*-plan.md`).*

---

## 1. Problem

Journal 1 defines three evaluation conditions; the canonical harness defines four. The extra canonical condition is a Flehmig-style traffic-light baseline, and canonical evidence already reports `C1 ↔ C3 = 0.00%` divergence at the admissible-set output level.

Journal 1's contribution claim, as now worded in the manuscript, is that **graduated governance exists — graduated *advisory-scope* governance is the gap.** The question is whether three conditions can carry that claim.

## 2. The finding that determines the answer

Inspecting `scripts/condition_comparison.py` lines 90–105:

```python
"C1": {SAFE: FULL, CAUTION: FULL, UNSAFE: EMPTY},
"C3": {SAFE: FULL, CAUTION: FULL, UNSAFE: EMPTY},
```

**The two admissible-set tables are identical dictionaries.** `C1 ≡ C3` is not a measurement. It is true by inspection of the source, before any data is loaded, and the replay cannot return any other value unless the harness is broken.

This is stronger than the circularity §12 of the brief anticipated. The concern was that equivalence *may follow analytically from the mapping*; in fact it follows from **literal identity of the mapping**. Any design that presents 0.00% as an experimental outcome presents a tautology as a discovery.

**But the substance is not the 0.00%.** The contestable, falsifiable claim is the **modelling step**: that Flehmig's traffic light maps to `{FULL, FULL, EMPTY}` — that its intermediate level alters supervisory intensity and leaves AI advisory scope untouched. That is a reading of the literature. It is what a reviewer can dispute, and it is what actually answers the novelty objection. The 0.00% is a one-line consequence of it.

**A proposition dressed as an experimental condition is weaker than the same proposition stated as a proposition.**

## 3. Three levels of evidence, kept separate

| Level | Claim | Status | What it can support |
|---|---|---|---|
| **Analytical** | The C1 and C3 admissible-set mappings are output-equivalent | **Provable in one line** from the mapping tables | The novelty argument itself |
| **Executable** | The implementation preserves that equivalence | Trivially true — it is the same dict literal | Almost nothing; there is no gap between spec and code to check |
| **Empirical trace** | 0.00% divergence over 43,848 hours | Confirms the harness computed what the tables say | **A harness self-test**, not a result about the world |

Collapsing these into "we measured 0.00% divergence" would overstate all three.

## 4. Decision criteria

Construct validity · novelty strength · baseline fairness · reviewer risk · statistical meaningfulness · implementation burden · interpretability · compatibility with H1–H4 · compatibility with canonical results · paper complexity.

## 5. Decision matrix

| Criterion | **A** — 3 conditions | **B** — canonical 4 | **C** — 3 primary + structural proposition |
|---|---|---|---|
| Scientific question answered | Does Level 2 add governance beyond a binary gate? | As A, plus: does the proposed differ from existing graduated governance? | As B |
| Novelty strength | **Weak** — leaves the paper's own conceded premise untested | Strong, but earned by a condition that cannot vary | **Strong** — the claim is argued where it is contestable |
| Baseline fairness | n/a | **At risk** — a fourth arm whose output is fixed invites "manufactured strawman" | **Good** — presented as a modelling claim with the fairness qualification attached |
| Reviewer risk | *"You concede graduated governance exists and never compare against it"* | *"Your fourth condition is your own construction and could not have differed"* | Residual: *"is your reading of Flehmig right?"* — the correct place for the argument to land |
| Statistical implications | Deterministic census | Deterministic census plus one degenerate arm | Deterministic census; proposition proved, not tested |
| Implementation burden | Lowest | Highest — 4-arm design, new hypothesis, full label migration | **Low** — reuses existing canonical evidence, adds no experimental arm |
| Interpretability | Clean | Muddled — readers expect four arms to be four measurements | Clean, if the proposition is clearly not an experiment |
| Compatibility with H1–H4 | Unchanged | Requires a new hypothesis of dubious type | Unchanged; the proposition sits outside the hypothesis set |
| Compatibility with canonical results | Partial | Full | Full — reuses canonical characterisation as cited evidence |
| Paper complexity | Lowest | Highest | Low |

## 6. Option A assessed

Ungated / Binary / Proposed **can** support: the proposed architecture differs from a binary gate; Level 2 contributes measurable additional governance; the ablation collapses the proposed onto the binary baseline.

It **cannot** support the novelty framing the manuscript now uses. Section 5 explicitly concedes that graduated governance exists and locates the gap on the advisory-scope axis. Option A tests nothing on that axis against a graduated comparator, so the paper would concede the premise and then decline to examine it.

**Claim that would have to be weakened under A:** the paper could claim only that *graduated advisory-scope governance is absent from the reviewed literature* — a review finding — and not that *the closest graduated precedent is output-equivalent to a binary gate* — a structural finding. The second is materially stronger and is what answered the conference reviewer's novelty objection.

## 7. Option B assessed

Gives the strongest apparent construct validity and matches the canonical harness exactly. Genuine benefits: direct novelty test, shared harness, clean Level 1 / Level 2 decomposition.

But three problems, and the first is decisive:

1. **The fourth arm cannot vary.** Presenting a condition whose output is fixed by its own definition as an experimental condition misrepresents what was done. A reader reasonably assumes four arms means four measurements.
2. **Fairness exposure increases with prominence.** As a full experimental condition, C3 reads as *"we tested Flehmig and it failed"* — precisely the reading the canonical fairness note forbids. Their framework conditions on AI degradation and is correct for the question it addresses.
3. **Migration cost is real** — labels, H1–H4, both section plans, and a new hypothesis. The brief asks that this not be minimised, and it should not be; but see §9, because the label component of that cost is currently zero and is separable.

## 8. Option C assessed — and reframed

The brief asks whether Option C is coherent or *"merely hides a fourth condition outside the main experiment."*

**It is coherent, and the reason is §2: C3 is not a condition.** It is a proposition about a mapping. Placing a proposition among experimental arms is the category error; placing it where propositions belong — stated, proved, and confirmed against the record — is correct classification, not concealment.

The test for hiding is whether the claim becomes less visible or less falsifiable. Under Option C it becomes **more** falsifiable: the modelling step is stated explicitly as the thing a reviewer should attack, rather than buried in a condition definition.

Recommended shape:

- **Primary experiment (three arms):** Ungated / Binary-gated / Proposed. Carries the empirical / performance evidence for the closed claim structure (see the executed `evaluation-specification.md` — historically H1–H4, reclassified as F1–F3 fidelity / E1–E4, E6 trace / E5 performance / H3 threshold OPEN / utility OPEN).
- **Structural proposition, in Related Work or the novelty section:** the Flehmig topology maps to `{FULL, FULL, EMPTY}`; therefore its admissible-set output is identical to a binary gate; confirmed across the full canonical record at 0.00% in both reportable configurations. Cited as **reuse of existing canonical characterisation evidence**, explicitly not a new Journal 1 experiment.
- **Fairness qualification travels with it**, in the canonical wording.

## 9. Condition labels — decided separately

**Recommendation: migrate to `C0 / C1 / C2 / C3` now.** This is decoupled from the baseline decision, as the brief requires.

Evidence: **no Journal 1 results, data, figures or scripts exist** — `find` over the Journal 1 tree returns only Markdown — and **no artefact anywhere references `J1-C1/C2/C3`**. Migration cost is at its global minimum today and rises monotonically once any result is generated under the current labels.

The existing mapping table prevents semantic inversion and was the right repair while consistency work was in progress. It is a permanent translation burden, and permanently divergent notation between a paper and its own harness is a long-term correctness risk — every future figure must be translated by hand, and the inversion of C2 in particular is exactly the kind of error that survives review.

Under Option C the canonical numbering accommodates the design naturally: the primary experiment is C0/C1/C2, and C3 is a named topology that is discussed rather than run.

## 10. Hypothesis audit

| | Current wording | Conditions | Affected by C3? | Assessment |
|---|---|---|---|---|
| **H1** | Graduated achieves *higher advisory scope compliance* than binary and ungated | All three | No | ⚠️ **Analytically predetermined.** Theorem 6.3 gives `AI(E) ⊆ A_AI(f(E))` by construction, so compliance for the proposed architecture is 100% by proof. And a binary gate has no scope restriction to violate, so its compliance against its own admissible set is also trivially 100%. As written, H1 is either trivially true or measures an undefined quantity |
| **H2** | Graduated produces *lower false positive rate* (recommendations outside `A_AI(S)`) | All three | No | ⚠️ **Same problem.** Under Theorem 6.3 the count is analytically zero. This is a fidelity check on the implementation, not a hypothesis about behaviour |
| **H3** | Governance overhead below [X ms] | Proposed | No | ✅ **Genuinely empirical.** The one hypothesis requiring measurement of something not fixed by proof. Note `[X ms]` is an unfilled placeholder and needs a justified value before it is testable |
| **H4** | Removing scope restriction reduces compliance to binary-gated level | Proposed + ablation | No | ✅ **The load-bearing hypothesis.** This is what actually isolates Level 2's contribution |

**No hypothesis is affected by adding or omitting C3** — which is itself evidence that C3 does not belong in the hypothesis set.

**On a proposed structural hypothesis** (*"at the admissible-set output level, the Flehmig topology and a binary gate are equivalent"*): it should be a **formal proposition with a one-line proof**, accompanied by a whole-record executable confirmation. Not an empirical hypothesis — there is no uncertainty to resolve. Not a mere sanity check either — the modelling premise it rests on is substantive and contestable. **Proposition, proved; confirmation, reported as such.**

**Flagged for the design review, out of scope here:** H1 and H2 carry the same circularity the brief warns about for C3. Recommending that they be reconsidered is within this task's remit; rewriting them is not.

## 11. Metrics

| Metric | Recommendation |
|---|---|
| Advisory scope compliance | **Reconsider** — analytically 100% by Theorem 6.3; belongs as an implementation-fidelity check |
| False positive rate | **Reconsider** — analytically 0 for the same reason |
| Decision-support utility | **Retain** — genuinely empirical, and the one metric addressing whether restriction costs anything useful |
| Governance overhead / latency | **Retain** — supports H3 and RQ-J2 |
| **Pairwise admissible-set divergence** | **Adopt from canonical** — this is the metric H4 actually needs |
| **Level 2 isolated contribution** (C0↔C2 − C0↔C1) | **Adopt from canonical** — directly quantifies the paper's central claim |

The two canonical metrics are added because they answer H4 and RQ-J3, not because the harness computes them.

## 12. Statistical treatment

The replay is a **deterministic census of all hourly records in the predefined retrospective study window**, not a random sample from a broader climatological population. The classifier is deterministic and no stochastic component is involved.

- `0.00%`, `5.81%`, `4.48%` are **exact descriptive values for the analysed trace/configuration** — not estimates of all future Sabah operating conditions.
- `C1 ↔ C3 = 0.00%` is **analytical**, not even descriptive.
- Only latency (H3) admits inferential treatment, and only because timing measurement carries genuine variance.

**Significance testing over a deterministic enumeration of the entire retrospective window is not meaningful** and should not be applied. Confidence intervals on a census are similarly ill-defined. The appropriate treatment is exact reporting with the configuration stated, which is what the canonical dual-configuration contract already does — and the PRIMARY/RESOLUTION spread is a **resolution-sensitivity** result, not an error bar.

*(Wording repaired 2026-09-10, Journal 1 Evaluation Specification Alignment §5.1. The previous formulation "complete enumeration over the full population" invited generalisation to future weather; the census framing is scoped to the study window.)*

## 13. Recommendation

```
RECOMMENDATION:
OPTION C
```

**WHY.** The Flehmig comparison is not an experiment and cannot be made into one: `C1` and `C3` are the same mapping, so the arm can never vary. Its scientific content is a *modelling claim* about how Flehmig's topology projects onto admissible-set output. Argued as a proposition, that claim is stated where it is contestable, keeps the fairness qualification attached, and answers the novelty objection. Run as a fourth arm, the same claim becomes a tautology presented as a result and invites the strawman charge. Option A leaves the paper conceding that graduated governance exists and never engaging it. Option C is the smallest design that supports the intended novelty claim without overstating what the comparison proves.

**WHAT IT SUPPORTS.** That the proposed architecture differs from a binary gate at a measurable rate; that Level 2 contributes governance beyond Level 1, isolated by ablation; that the closest graduated precedent in the reviewed literature is output-equivalent to a binary gate at the admissible-set level, by construction and confirmed across the full record; that the architecture's formal guarantees hold by proof rather than by test.

**WHAT IT DOES NOT SUPPORT.** That Flehmig's system was reproduced, tested, or found deficient. That the graduated architecture produces better *advice*, calibrated reliance, or improved safety outcomes — Layer 3 is unbuilt and no incident data exists. That the results transfer beyond the Sabah instantiation. That `A_AI(CAUTION) = {Go, Delay}` is the epistemically correct partition.

**WHAT MUST CHANGE IN JOURNAL 1** *(on acceptance — not done in this task)*: migrate condition labels to `C0/C1/C2/C3` and retire the mapping table; add the Flehmig structural proposition with proof, fairness qualification and cited canonical confirmation, outside the experimental design; adopt pairwise divergence and isolated Level 2 contribution as metrics; reconsider H1 and H2 given their analytic determination; supply a justified value for H3's `[X ms]`; state the deterministic-census treatment in the statistics section.

**WHAT REMAINS UNCHANGED.** The canonical harness and all canonical results. H3 and H4. The three-arm primary experiment. Every formal result in Sections 5–6. All protected canonical state.

## 14. Deferred questions

1. Should H1/H2 be reformulated as implementation-fidelity checks, or replaced by behavioural hypotheses that are not analytically determined? *(Recommended; out of scope here.)*
2. What value should `[X ms]` take, and on what hardware basis?
3. Does decision-support utility require the RQ5-style user study to be meaningful, or can it be operationalised on the replay alone?
4. If Layer 3 is built before submission, how are H1/H2 reclassified? *(Layer 3 implementation makes compliance and violation rates **implementation-fidelity measurements** — they test whether the engine conforms to the RS(S) specification. It does not convert a formal governance invariant into a behavioural hypothesis: Safety Dominance remains `AI(E) ⊆ A_AI(f(E))` under the stated engine assumptions, and an implementation test checks conformance to that specification, not empirical rediscovery of the theorem. Wording repaired 2026-09-10, Journal 1 Evaluation Specification Alignment §5.2.)*

## 15. Stop-condition assessment

| Condition | Triggered |
|---|---|
| Literature interpretation required | **NO** — the canonical script already documents the topology and fairness note; no new reading of Flehmig was needed |
| Hypothesis context incomplete | **NO** — H1–H4 and RQ-J1–J4 read from `research-design.md` |
| Baseline implementation conflict | **NO** — the implemented C3 mapping `{FULL, FULL, EMPTY}` matches its documented topology exactly |
| Empirical input required | **NO** — the decision rests on design logic and existing canonical evidence |

## 16. Scientific state

**None changed.** No condition renamed, no hypothesis rewritten, no script or manuscript edited, no experiment run, no canonical result touched. This document is a proposal.

---

*Evidence inspected:* `scripts/condition_comparison.py` (lines 10–19 topology and fairness note; 90–107 admissible-set tables), `publications/active/journal-1/research-design.md` (H1–H4, RQ-J1–J4), `publications/active/journal-1/submissions/v1-initial-submission/manuscript.md` (Sections 10–15 plans, condition table), and the Journal 1 tree (no results artefacts present).
