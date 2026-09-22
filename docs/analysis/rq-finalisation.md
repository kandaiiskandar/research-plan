# Research-Question Finalisation

**Date:** 2026-09-21
**Trigger:** Decision to remove RQ-J2 (target-hardware latency) from the research-question level.
**Inputs:** `research-chain-lock.md`, `threshold-sensitivity-analysis.md`, `final-novelty-stress-test.md`, `primary-source-verification-audit.md`, `g3-literature-falsification.md`, evaluation specification §§5, 11, 14, 17.
**Canonical report:** **UNCHANGED.**

---

## A. RQ-J2 removal decision

**Removed from the active research-question set.**

**Why it does not belong there.** The surviving contribution is an empirical characterisation, a domain operationalisation, and an operational specification. None of these depends on how fast the governance layer executes. The thesis claims no real-time algorithm, no computational optimisation, no low-latency inference and no hardware-efficiency result, so a latency measurement could not confirm or refute anything it asserts. Retaining it would have left an RQ whose only possible answer was a descriptive number with, as the evaluation specification itself records, **no externally justified acceptance criterion** (`H3 = X ms` is OPEN, and the specification explicitly forbids inventing one).

**Where it now sits.** *Deferred deployment / prototype evaluation — outside the evidence required for the current contribution.* It belongs in the future-work and implementation-validation discussion, alongside the note that the harness is validated (`E5_HARNESS = CLOSED`) and a development-machine reference run exists that must not be extrapolated to a target device.

**How it must not be described.** Not as an unanswered research question, and not as a limitation of the evaluation. The evaluation is not weaker for omitting it; the question was mis-scoped as an RQ.

**Consequence for OPEN-5.** `E5_ANDROID_TARGET_BENCHMARK = DEFERRED_MANDATORY` should be re-designated. It is no longer mandatory for thesis closure, because nothing at contribution level rests on it. This is a change to the evaluation specification, not to any result.

---

## B. Old RQ audit

| RQ | Source | Verdict | Reason |
|---|---|---|---|
| Thesis RQ1 — architecture design | CLAUDE.md | **MERGE → new RQ1** | Mechanism novelty conceded; design and specification are one activity |
| Thesis RQ2 — formal specification | CLAUDE.md | **MERGE → new RQ1** | As above |
| Thesis RQ3 — prototype implementation | CLAUDE.md | **REMOVE** | Necessary engineering, not a research question. Retain as an implementation chapter |
| Thesis RQ4 — technical validation | CLAUDE.md | **REWRITE → new RQ2** | The surviving empirical question. "Validation" must go — there is no incident record |
| Thesis RQ5 — contextual validation with fishers | CLAUDE.md | **FUTURE WORK** | Not conducted. An RQ the thesis does not answer cannot remain an RQ |
| RQ-J1 — Safety Dominance proof | eval-spec §5 | **DEMOTE → supporting formal property** | Answered by construction; valuable as contract conformance, not as an open question |
| RQ-J2 — latency / overhead | eval-spec §5 | **REMOVE** | §A |
| RQ-J3 — C2 vs C1/C0 divergence | eval-spec §5 | **MERGE → new RQ2** | Directly the empirical characterisation |
| RQ-J4 — component attribution | eval-spec §5 | **MERGE → new RQ3** | Now has its own evidence from the sensitivity analysis and earns a place, but not as an independent *governance* question |

---

## C. Final thesis-level RQs

Three, each with evidence, each answerable in a way that could have come out otherwise.

> **RQ1 — Operational specification.**
> Can AI participation and admissible advisory scope be specified as two separate state-conditioned functions over a classified multi-component environmental state such that classification remains total and the containment property is preserved when some conceptually required components are structurally unavailable — and which elements of that specification must be decided by the designer rather than derived from published sources?

> **RQ2 — Empirical characterisation and robustness.**
> Over a multi-year historical environmental record for the deployment site, how frequently does the intermediate safety state produce a stricter admissible recommendation set than a participation-only gate, and how sensitive is that frequency to defensible environmental-threshold and data configurations?

> **RQ3 — Structural warrant of the multi-component classifier.**
> Which components of the environmental state actually determine the intermediate classification at the deployment site, and is the multi-component structure warranted by the evaluated record?

### Why RQ1 was strengthened rather than demoted

The previous wording — *"How can X be specified?"* — was answered by specifying X, and `research-chain-lock.md` flagged it as circular. Two changes fix that without inflating it.

The **constraint clause** makes it falsifiable: totality and containment could have failed to hold together under structural unavailability. The alternative would have been to fabricate values for unmeasured components or to leave the classifier partial, both of which the specification rejects. That the two properties survive is a result, albeit one established by construction and proof.

The **second clause** — which elements must be decided rather than derived — is the genuinely informative half, and it has a concrete enumerable answer from the provenance work: four boundaries trace to named authorities (MET Cat 1/Cat 2, MET *Ribut Petir*, JPS/DID *Light* limit, Yaakob's operational ceiling, COLREGs Rule 20(b)), while three load-bearing choices are researcher-defined with no external source (`A_AI(CAUTION) = {Go, Delay}`, the policy `night ⇒ UNSAFE`, and the three-state cardinality). Reporting that boundary honestly is a contribution of the domain-operationalisation kind.

### Why RQ3 was added

The sensitivity analysis produced an attribution result that no existing RQ covered and that has a clear negative finding: **of five component classifiers, `g_o` binds 97.6% of CAUTION hours, `g_r` binds 2.4%, and `g_w`, `g_t` and `g_m` bind none.** `g_w` activates twice in 43,848 hours and is decisive in neither. This bears directly on whether a five-component state is justified at this site, and the honest answer is that it is not empirically warranted here while remaining defensible as a transferable specification. That tension is worth an RQ; burying it inside RQ2 would hide the negative result.

### Preserved limitation

None of the three RQs asks whether `A_AI(CAUTION) = {Go, Delay}` is correct, and none can. Because C1 and C2 differ only in that cell, Δ_L2 equals the CAUTION activation rate for *any* strict subset of FULL. The RQ set therefore asks **how often the intermediate restriction is activated**, never **whether the selected advisory content is appropriate**. This must be stated wherever the RQs appear.

---

## D. Supporting questions and formal properties — below thesis-RQ level

| Item | Status |
|---|---|
| **P1 Totality** (Thm 6.1; C.1, C.1b) | Supporting formal property. Evidence *for* RQ1's constraint clause, not an RQ |
| **P2 Monotonicity / containment** (Thm 6.2) | Supporting design property. True by definition of `A_AI` |
| **P3 Safety Dominance** (Thm 6.3; C.3, C.7.2) | Supporting formal property — contract conformance under A1–A4. **Former RQ-J1** |
| **P4 / J1-P1** (C1 ≡ C3) | Supporting proof. Entailed by the mapping tables; the 0.00% replay value is harness consistency, not discovery |
| **F1–F3** prototype fidelity | Supporting implementation evidence. CLOSED PASS, bounded to the interface contract |
| **E5 harness validation** | Implementation evidence. Retained; the *target-hardware* measurement is future work |

---

## E. RQ → evidence map

| RQ | Why it exists | How answered | Evidence | Contribution |
|---|---|---|---|---|
| **RQ1** | Gap A: the mechanisms exist in other domains but were not composed for a multi-source environmental classifier with structurally unavailable components | Construction, proof, and provenance separation | `appendix-c-formalisation.md`; P1–P3; `D = {m}` with lower-bound consequence; threshold provenance table (4 sourced boundaries, 3 researcher-defined choices) | Operational specification (secondary) |
| **RQ2** | Gap B: activation frequency of an intermediate advisory-scope level has not been reported | Deterministic replay + threshold sensitivity | Δ_L2 = 5.81% / 4.48%; sourced-threshold range 5.67%–9.56%; full grid 1.11%–9.56%; `O_C` elasticity ≈ −1.4 pp per 0.05 m; common-period comparison 6.45% vs 4.48% | **Empirical characterisation (primary)** |
| **RQ3** | Whether a five-component state earns its complexity on real data | Component attribution over the same replay | `g_o` 518/531 binding, `g_r` 13/531, `g_w` 0 (2 activations), `g_t` 0, `g_m` 0 (excluded); zero ties | Empirical characterisation (primary, negative result) |

No RQ lacks evidence. No completed experiment lacks an RQ.

---

## F. Remaining experiment requirements

| Work | Classification | Reasoning |
|---|---|---|
| **Threshold sensitivity** | **COMPLETE** | Done. Answers reviewer attack #10, which was OPEN |
| **Common-period resolution comparison** | **COMPLETE** | Done within the sensitivity task. Resolves ISSUE-1 and shows canonical §0a's attribution wrong in magnitude — 1.97 pts resolution effect, −0.64 pts record-length effect |
| **E5 target-hardware benchmark** | **FUTURE WORK** | RQ-J2 removed. Not required evidence for any surviving claim |
| **Exclusion sensitivity `D ∈ {{m}, {m,r}, {m,o}}`** | **STRENGTHENING** | Would quantify how far a single excluded channel can move the result. Introduces no new constant. Not novelty evidence — the mechanism is Manski's. Do **not** run `D = {m,w}`: `g_w` binds never, so the result is a structural zero |
| **Advisory-content ablation** | **FUTURE WORK** | Ill-posed under the current metric: admissible-set divergence is invariant to the content of `A_AI(CAUTION)`. Requires Layer 3 in the loop and a defined outcome measure. Must be specified before attempting |
| **Additional site** | **OPTIONAL** | The claim is explicitly single-site |
| **Additional historical period** | **OPTIONAL** | Marginal; the common-period comparison already separates period from model |
| **Fault injection (staleness / invalidity)** | **NOT JUSTIFIED** | Requires inventing `ageᵢ`, which is OPEN, repeating the 7.5 mm/hr error class. The property it would test is conceded to prior work |

**Nothing is classified REQUIRED BEFORE LOCK.**

---

## G. Gate 4 reassessment

> ### **Gate 4 — Experiment: SUFFICIENT**

Previously NEEDS STRENGTHENING on two grounds. Both are discharged: threshold sensitivity is complete, and E5 is removed rather than deferred, because RQ-J2 no longer exists.

Every surviving claim now has evidence. RQ2 is answered with a robustness envelope rather than a point value. RQ3 is answered by attribution over the same replay. RQ1 is answered by construction, proof and the provenance separation. The one substantial hole — whether `{Go, Delay}` is the right restriction — is not an evidence gap, because it is **not claimed**; it is recorded as a limitation and as future work.

Two outstanding items are **documentation corrections, not experiments**: `empirical-findings-2026-09-06.md` §0a still attributes the PRIMARY/RESOLUTION spread to grid resolution at 1.33 points when the like-for-like figure is 1.97, and the evaluation specification still carries RQ-J2 and `DEFERRED_MANDATORY`. Neither requires new computation.

---

## H. Updated research chain

| Stage | Content |
|---|---|
| **Gap A** (operationalisation) | Advisory-type restriction by external state, totality over incomplete observations, and directional bounds from unmeasured variables are each established — in certified avionics, runtime verification, and partial-identification methodology respectively. Within the reviewed literature they were not composed into one operational contract with participation and advisory scope as two separate functions over a classified multi-component *environmental* state |
| **Gap B** (empirical) | Within the reviewed literature, no characterisation was identified of how often such an intermediate level changes the admissible recommendation set on a multi-year environmental record |
| ↓ | |
| **RQ1** ← Gap A · **RQ2, RQ3** ← Gap B | |
| ↓ | |
| **Method** | Specification and proof (RQ1); deterministic four-condition replay over 43,848 / 28,501 hourly records with threshold-sensitivity and common-period analysis (RQ2); component attribution over the same replay (RQ3) |
| ↓ | |
| **Results** | Δ_L2 = 5.81% / 4.48%, identity Δ_L2 = P(CAUTION) verified from implementation; sourced-threshold envelope 5.67%–9.56%; wave CAUTION onset dominant at ≈ −1.4 pp per 0.05 m; rainfall boundary moves it < 0.5 pp; wind structurally zero; `g_o` binds 97.6% of CAUTION hours; three of five components never bind; grid-resolution effect 1.97 pts on a like-for-like comparison |
| ↓ | |
| **Contribution** | **Primary:** empirical characterisation with a reported operating envelope and a negative structural finding. **Secondary:** domain operationalisation with separated provenance; operational specification separating `G(S)` from `A_AI(S)`. **Supporting:** contract-conformance proofs; reproducibility and pre-registration methodology |

**Verification of the required path:** empirical gap → RQ2/RQ3 → historical replay + threshold sensitivity → CAUTION activation frequency, robustness envelope and component attribution → empirical characterisation contribution. **Intact.**

---

## I. Final decision

> ## **RQ STRUCTURE AND EXPERIMENT SET READY TO LOCK**

Removing RQ-J2 closes the last item that was blocking Gate 4, and it closes it correctly — by recognising that the question was mis-scoped rather than by running an experiment to satisfy a structure that no longer needed it. With threshold sensitivity and the common-period comparison complete, every remaining RQ has evidence already in hand, and no outstanding work is classified REQUIRED. The three RQs are answerable, non-circular, and each could have returned a different answer: the specification could have failed to preserve totality and containment under structural unavailability; the activation rate could have been vacuous for the small-vessel population and was not; and the five-component classifier could have been empirically warranted, which it is not.

Two changes to the RQ set are more than administrative. RQ1 was strengthened rather than demoted, by adding the constraint clause that makes it falsifiable and the provenance clause that makes its answer informative — four sourced boundaries against three researcher-defined choices is a concrete, defensible result of the domain-operationalisation kind. RQ3 is new, and it exists to carry a negative finding that would otherwise have been buried inside RQ2: three of five component classifiers never bind at this site, and `g_o` alone accounts for 97.6% of the intermediate state. Surfacing that strengthens the thesis, because a reviewer who computes it independently and finds it unreported will read the five-component design as decoration.

What remains before the canonical report can be updated is documentation, not research. The evaluation specification still lists RQ-J2 and marks the target-hardware benchmark `DEFERRED_MANDATORY`; `empirical-findings-2026-09-06.md` §0a still attributes the PRIMARY/RESOLUTION spread to grid resolution at 1.33 points when the like-for-like figure is 1.97 with record length pulling 0.64 the other way; and the limitation on `A_AI(CAUTION)` invariance is not yet written anywhere in the canonical tree. Those three edits, plus the RQ and contribution wordings from this document and from `research-chain-lock.md` §Q and §R, are the full remaining scope of the report revision.
