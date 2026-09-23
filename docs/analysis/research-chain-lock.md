# Research Chain Reconstruction and Contribution Lock

**Date:** 2026-09-21
**Basis:** `primary-source-verification-audit.md`, `g3-literature-falsification.md`, `final-novelty-stress-test.md`, `experiment-report-delta-l2.md`, evaluation specification §§3–6, `appendix-c-formalisation.md`, CLAUDE.md formal model.
**Canonical report:** **UNCHANGED.** This document is for human review before any edit.
**No new literature search performed.**

---

## A. Frozen literature position — conceded to prior work

The following are **established** and are not claimed:

| Mechanism | Conceded to |
|---|---|
| Advisory-category inhibition conditioned on external state | FAA AC 20-151C (TCAS II), TSO-C151c (TAWS) |
| Observation validity gating which advisory types reach a human | TSO-C151c §5.6 — invalid position ⇒ FLTA and PDA inhibited, GPWS retained, inhibit annunciated |
| Nested admissible sets contracting to empty | TCAS II inhibit schedule; Baxi (2026) tiers |
| Multi-component classified runtime state | TCAS II (radio alt + config discretes + W/A/T + airspeed + bank + OEI); Baxi f(R) over 3 components |
| Weakest-link / max-severity aggregation | Baxi (weakest-link gate); AMAGF ("control quality equals its weakest dimension") |
| Graduated multi-level governance | Baxi; AMAGF; Flehmig et al. |
| Human final authority preserved | AC 20-151C §2.1.1; Kwon & Kim (2026) |
| Fail-safe / fail-degraded / fail-operational regimes | Gyllenhammar et al. (2025); ODD-exit → Minimal Risk Condition |
| Totality of classification over incomplete observations | Bauer, Leucker & Schallhart (2011); Taleb, Hallé & Khoury (2023); assumption-based RV four-valued total monitoring |
| Conservative resolution of unusable observations | RV conservative-approximation family; AMAGF reduced-autonomy on missed checkpoint |
| Declared unmeasured variable ⇒ directional bound | Manski (1990, 1997); Manski & Pepper (2000) |
| Monotone contraction of admissible sets | Baxi Prop. 1; TCAS nested bands |
| Governance placed outside the generator | Könighofer et al. (2025); Baxi |

**Consequence:** no mechanism-level novelty claim is available. Any surviving contribution is compositional, domain-operational, empirical or methodological.

---

## B. Research problem — three separate problems

**B1 — Domain problem.** Small-scale fishers at Kota Kinabalu make a departure decision (go / delay / when / how long) under environmental conditions they must judge without instrumentation, in a setting with no marine-warning archive, no incident register, and official weather criteria that define where warnings *begin* but never where caution should begin.

**B2 — CS / design problem.** The governance mechanisms above exist in certified avionics, autonomous-agent frameworks and runtime verification, each with its own conditioning variable and governed object. Composing them for an unattended, heterogeneous, low-resource environmental classifier requires decisions none of the source domains supply: which components form the state, how independently-faulting observations resolve, whether participation and advisory scope are one function or two, and what the intermediate level admits.

**B3 — Evidence problem.** Whether an intermediate advisory-scope level is *reached often enough to matter* on real conditions has not been measured. Graduated-governance proposals in the reviewed literature are specified and sometimes proved, but their activation frequency on a multi-year environmental record is not reported.

These are not the same problem and must not be merged. B1 motivates; B2 is design work; **B3 is where the defensible contribution sits.**

---

## C. Final gap candidate — two parts

### Gap A — Operationalisation / composition gap

> Within the reviewed literature, advisory-type restriction by external state, totality over incomplete observations, and directional bounds from declared unmeasured variables are each established, in certified avionics, runtime verification and partial-identification methodology respectively. Within the reviewed literature, these have not been composed into a single operational specification in which participation `G(S)` and advisory scope `A_AI(S)` are **two separately specified functions** over a classified multi-component *environmental* state for a human-facing decision-support system.

**Strength: weak-to-moderate.** The three ingredients come from unrelated fields; their non-combination is largely disciplinary, not a recognised open problem.

### Gap B — Empirical characterisation gap

> Within the reviewed literature, no empirical characterisation was identified of how often an intermediate advisory-scope level changes the admissible recommendation set relative to a participation-only gate, when replayed over a multi-year environmental record.

**Strength: moderate-to-good.** This is a measurement nobody has reported, it could have returned a null result, and it is the part the existing experiment actually supports.

---

## D. RQ audit

| Current RQ | Source | Verdict | Reason |
|---|---|---|---|
| Thesis RQ1 — architecture design (three-mode graduated structure) | CLAUDE.md | **REWRITE** | Framed as designing a novel architecture; mechanism novelty is conceded |
| Thesis RQ2 — formal specification (E, f, G, A_AI, Safety Dominance) | CLAUDE.md | **MERGE into RQ1** | Specification and design are one activity here; separating them implies two contributions where there is one |
| Thesis RQ3 — prototype implementation | CLAUDE.md | **REMOVE from contribution claim** | Implementation is necessary work, not a research question. Retain as a chapter, not an RQ |
| Thesis RQ4 — technical validation (three-condition comparison) | CLAUDE.md | **KEEP, REWRITE** | This is the surviving empirical question; wording must drop "validation" |
| Thesis RQ5 — contextual validation with fishers | CLAUDE.md | **REMOVE or defer explicitly** | Not conducted. Cannot be an RQ of a thesis that does not answer it |
| RQ-J1 — can Safety Dominance be proved | eval-spec §5 | **KEEP as supporting** | Answerable, but by construction — see §H |
| RQ-J2 — latency/overhead on target hardware | eval-spec §5 | **KEEP, flagged OPEN** | `E5_ANDROID_TARGET_BENCHMARK = DEFERRED_MANDATORY` |
| RQ-J3 — how do C2 outputs differ from C1/C0 | eval-spec §5 | **KEEP** | The core empirical question |
| RQ-J4 — which component accounts for the divergence | eval-spec §5 | **MERGE into RQ-J3** | The subtraction answers both in one operation |

---

## E. Recommended RQs

> **RQ1 (operational specification).** How can AI participation and admissible advisory scope be specified as two separate state-conditioned functions over a classified multi-component environmental state, for a human-facing decision-support system in a low-resource setting where some conceptually required observations are structurally unavailable?

> **RQ2 (empirical characterisation).** Over a multi-year historical environmental record for one deployment site, how often does the intermediate advisory-scope state admit a strictly smaller recommendation set than a participation-only gate, and how sensitive is that frequency to the environmental-data configuration?

**Tests applied.**

| Test | RQ1 | RQ2 |
|---|---|---|
| Answerable | Yes | Yes |
| Non-circular | ⚠️ **Partially.** "How can X be specified" is answered by specifying it. Mitigated by the constraint clause (structurally unavailable observations), which can fail | Yes — the answer could have been ≈0 |
| Supported by current experiment | No — answered by construction and proof | **Yes** |
| Appropriately scoped for CS | Marginal — design-and-specification questions are weak RQs | Yes |

**RQ1 is the weaker of the two and should not be presented as the primary question.** Its honest form is closer to *"what must be specified, and what must be decided by the designer, to compose these mechanisms for this setting?"* — a question whose answer is an enumeration, not a discovery.

---

## F. Architecture role

Not a novel safety architecture. **An operational architecture composing established safety-governance mechanisms for one low-resource environmental DSS setting.**

| Category | Content |
|---|---|
| **Inherited** | Advisory-type restriction by external state; nested contracting admissible sets; deterministic gating outside the generator; max-severity aggregation; fail-safe resolution of unusable observations; human final authority |
| **Adapted** | The avionics inhibition pattern moved from a single certified platform with one validity-checked navigation input to an unattended multi-source environmental classifier; RV totality moved from trace monitoring to a component-wise environmental classifier |
| **Composed** | `G(S)` and `A_AI(S)` as two separately specified functions rather than one graduated tier index; component classifiers `gᵢ` aggregated by worst case into a single `S` that drives both |
| **Researcher-defined** | `A_AI(CAUTION) = {Go, Delay}`; the three-state cardinality; the policy `night ⇒ UNSAFE`; the departure window 05:00–09:00; the exclusion `D = {m}`; the decision to report two data configurations |
| **Empirically evaluated** | Only the activation frequency of the intermediate state, and its sensitivity to wave-model/record configuration |

---

## G. Governance contract — status of each choice

| Element | Mapping | Status |
|---|---|---|
| `g_w` 21.6 / 27.0 kn | SAFE / CAUTION / UNSAFE | **Externally supported** — MET Malaysia Cat 1 / Cat 2 onsets (40 / 50 km/h), preserved unrounded |
| `g_r` UNSAFE > 20.0 mm/hr | — | **Externally supported** — MET *Ribut Petir* warning trigger |
| `g_r` CAUTION at 10.0 mm/hr | — | **Externally sourced but non-MET** — JPS/DID Infobanjir *Light* upper limit. MET publishes no criterion below 20. Documented as a source gap, correctly |
| `g_o` small-vessel 1.0 / 1.25 m | — | **Externally supported** — Yaakob et al. (2015) operational ceiling, not the NORDFORSK failure point |
| `g_t` sunrise/sunset boundary | — | **Externally supported** — COLREGs Rule 20(b) gives the boundary *for navigation lights* |
| `g_t` policy: night ⇒ UNSAFE ⇒ no advisory | — | **RESEARCHER-DEFINED.** No source establishes it. CLAUDE.md states this explicitly. Night operation is neither prohibited nor physically unsafe |
| Three states rather than two or five | — | **RESEARCHER-DEFINED**, with independent motivation from Flehmig's tripartite index |
| `G(SAFE) = G(CAUTION) = 1`, `G(UNSAFE) = 0` | — | **Structurally necessary** given the state ordering |
| **`A_AI(CAUTION) = {Go, Delay}`** | — | **RESEARCHER-DEFINED.** No external source. The rationale — timing and duration advice is least supportable when conditions are marginal — is reasonable and is *not* established. **Must not be presented as an optimum** |
| `A_AI(UNSAFE) = ∅` | — | **Structurally necessary** given containment |
| `D = {m}` | — | **Forced by data availability**, correctly declared, with a correct directional consequence |

⚠️ **Critical observation for §J.** C1 and C2 differ **only** at `A_AI(CAUTION)`. Divergence therefore occurs in exactly those hours where `S = CAUTION`, regardless of *what* `A_AI(CAUTION)` contains, provided it is a strict subset of FULL. **Δ_L2 is numerically identical to the CAUTION occurrence rate in the departure window.** The `{Go, Delay}` choice does not affect the measured value at all.

---

## H. Formal claim audit

| Claim | Statement | Classification |
|---|---|---|
| **P1 Totality** (Thm 6.1; appendix-c C.1, C.1b) | `f(E)` returns exactly one state; `F_{D,τ}` total under valid startup | **FORMALISATION OF ESTABLISHED MECHANISM.** Totality over incomplete observations is established in RV. Retain as proof that this implementation satisfies its contract; do not claim as novel |
| **P2 Monotonicity / containment** (Thm 6.2) | `S₁ ≻ S₂ ⇒ A_AI(S₁) ⊆ A_AI(S₂)`, strict | **DESIGN PROPERTY.** True by how `A_AI` is defined. It is a consistency check on the definition, not a result |
| **P3 Safety Dominance** (Thm 6.3; C.3, C.7.2) | `AI(E) ⊆ A_AI(f(E))`; `f(E) = UNSAFE ⇒ AI(E) = ∅` | **IMPLEMENTATION PROPERTY.** Holds by construction from the RS(S) supply mechanism under A1–A4. Valuable as proof that Layer 3 cannot violate the contract. Not a discovery |
| **P4 / J1-P1** (C1 ≡ C3) | `A_C1(S) = A_C3(S)` for all S | **SUPPORTING PROOF.** One line from the mapping tables. The evaluation specification already labels the 0.00% replay value as harness-consistency confirmation — this is correct and should be preserved verbatim |
| **Corollary C.1b.1** (fail-safe) | `gᵢ(⊥) = UNSAFE` ⇒ max-severity yields UNSAFE | **FORMALISATION OF ESTABLISHED MECHANISM.** Conservative resolution is established |

**None is a NOVEL CONTRIBUTION.** All are worth keeping, correctly labelled as *proof that the implementation satisfies the intended governance contract*. A thesis may legitimately contain proved properties that are not themselves novel; it may not present them as the contribution.

---

## I. Experiment purpose

**What the replay tests:** whether, and how often, an intermediate state that contracts the admissible recommendation set produces an observable governance difference from a participation-only gate, over historical environmental conditions at one site.

| Condition | Why it exists |
|---|---|
| **C0 Ungated** | Zero point. Expresses each governance level's effect as divergence from ungoverned output. Not a proposal |
| **C1 Participation-only** | The comparator the contribution must differ from. Isolates Level 1 |
| **C2 Proposed** | Identical to C1 except `A_AI(CAUTION)`. Isolates Level 2 by subtraction |
| **C3 Three-state, scope unchanged** | Structural control. Shows a third *label* is not what produces divergence. **`A_C1(S) = A_C3(S)` by construction; the 0.00% replay value confirms harness consistency and is not an empirical discovery** (eval-spec §6, P4) |

---

## J. Result interpretation

### What Δ_L2 = 5.81% / 4.48% means

Under PRIMARY, 5.81% of evaluated departure-window hours (05:00–09:00, small vessel < 10 GRT, 2020–2024, 43,848 hourly records) produce a strictly smaller admissible recommendation set under C2 than under the participation-only comparator. 4.48% under RESOLUTION. Exact descriptive values for the analysed trace and configuration.

Equivalently, and more precisely: **these are the rates at which the classifier outputs CAUTION in the departure window**, given the stated thresholds.

### What it does NOT mean

Not accident reduction. Not improved fisher safety. Not AI or prediction accuracy. Not causal effectiveness. Not a frequency estimate for future Sabah conditions. Not optimality of the governance design. Not evidence that those were the *correct* hours to restrict — no incident record exists. Not a confidence interval, and never "5.81 ± 4.48".

### An additional limit the report does not currently state

Because C1 and C2 differ only at `A_AI(CAUTION)`, the measured value is **independent of the content of `A_AI(CAUTION)`**. Any strict subset of FULL yields the same number. The experiment therefore evidences *how often the intermediate state is reached*; it provides **no** evidence about whether `{Go, Delay}` is the right restriction. That choice — the researcher-defined core of the governance design — is unevaluated.

---

## K. Evidence map

| Claim | Type | Supporting evidence | Limitation | Status |
|---|---|---|---|---|
| Intermediate state reached on 5.81% / 4.48% of departure hours | Empirical | `condition_comparison.py`, `canonical_figures.py`, reproduced 2026-09-21 | One site, one period; = CAUTION rate; no incident data | **LOCK** |
| A third state label alone does not graduate governance | Structural | P4 / J1-P1, proved from mapping tables | Entailed, not measured | **LOCK WITH CAVEAT** — label as analytic |
| Resolution sensitivity: 5.81% → 4.48% | Empirical | Dual-configuration replay | Confounded — wave model *and* record length differ (ISSUE-1) | **LOCK WITH CAVEAT** |
| `G(S)` and `A_AI(S)` as two separate functions | Design / composition | Specification; unmatched in searched literature | Ingredients from unrelated fields; no evidence it outperforms a unified index | **LOCK WITH CAVEAT** |
| Implementation satisfies the governance contract | Formal | P1–P3, F1–F3 CLOSED PASS | Proved by construction under A1–A4 | **LOCK** as supporting |
| Threshold provenance and documented MET gap | Domain | `finding-met-lower-boundary-gap.md`, Yaakob, COLREGs | `g_r` CAUTION non-MET; night policy researcher-defined | **LOCK WITH CAVEAT** |
| Register/provenance methodology | Methodological | 15 CONFIRMED / 9 REFUTED; single-generator script rule | Self-assessed; no external benchmark | **LOCK** as supporting |
| `A_AI(CAUTION) = {Go, Delay}` is appropriate | Design | None | Not evaluated; Δ_L2 is invariant to it | **NEEDS ADDITIONAL EVIDENCE** |
| Governance latency on target hardware (RQ-J2) | Performance | Development-machine reference only | `DEFERRED_MANDATORY` | **NEEDS ADDITIONAL EVIDENCE** |
| Classification correctness | — | None; no incident record | No path with existing data | **DROP** from claims |
| Contextual validation with fishers (RQ5) | — | Not conducted | — | **DROP** from this thesis or declare deferred |

---

## L. Additional experiment assessment

| Experiment | Classification | Reasoning |
|---|---|---|
| **Target-hardware benchmark (E5)** | **REQUIRED** | RQ-J2 is an open RQ with no evidence. Either run it or remove the RQ |
| **Threshold sensitivity** (vary `g_o` 1.0/1.25 and `g_r` 10.0 within sourced ranges; report Δ_L2 across the grid) | **REQUIRED** | The most likely reviewer attack (§O.10). Δ_L2 is a direct function of thresholds, one of which is admittedly non-MET. Without this, the headline is one point estimate from one threshold set |
| **Exclusion sensitivity `D ∈ {{m}, {m,r}, {m,o}}`** | **STRENGTHENING** | Quantifies how much a single excluded channel can move the result. Introduces no new constant, so cannot repeat the 7.5 mm/hr error. **Not novelty evidence** — the mechanism is Manski's. Do **not** run `D = {m,w}`: `g_w` binds never, so the result is a structural zero |
| **Advisory-content ablation** (vary `A_AI(CAUTION)` and measure something other than set divergence) | **STRENGTHENING**, but currently ill-posed | Would address the gap in §J, but requires a metric that is not admissible-set divergence — which is invariant to it. Needs Layer 3 in the loop and a defined outcome measure. Specify before attempting |
| **Additional site** | **OPTIONAL** | Would strengthen generalisation but the claim is explicitly single-site |
| **Additional historical period** | **OPTIONAL** | Marginal |
| **Resolution sensitivity, de-confounded** (both wave models over the common 28,501-hour overlap) | **STRENGTHENING** | Resolves ISSUE-1; converts a confounded comparison into an attributable one; uses existing data |
| **Fault injection (staleness / invalidity)** | **NOT JUSTIFIED — yet** | Requires inventing `ageᵢ`, which is OPEN. Inventing it repeats the 7.5 mm/hr error class. And the property it would test (R1) is now conceded to prior work |

---

## M. Contribution hierarchy

### Primary
**Empirical characterisation of graduated advisory-scope governance under multi-year environmental replay.** The rate at which an intermediate advisory-scope state is reached, at one site over five years, under two data configurations, against a structural comparator, with predictions registered before analysis. This is the only element that could have come out otherwise.

### Secondary
**Domain operationalisation for small-scale Malaysian coastal fisheries** — environmental state construction from heterogeneous sources, threshold provenance traced to named authorities with the MET lower-boundary gap documented rather than papered over, and explicit separation of externally supported from researcher-defined choices.

### Secondary
**Operational composition separating `G(S)` from `A_AI(S)`** as two state-conditioned functions — presented as a specification decision with stated consequences, not as an architectural novelty.

### Supporting
**Formal verification that the implementation satisfies the intended governance contract** (P1–P4, F1–F3) — correctly labelled as contract conformance, not as new theory.

### Supporting
**Reproducibility and provenance methodology** — pre-registration with retained refutations, single-generator figure authority, full supersession history.

*Changed from the candidate hierarchy: the composition is demoted below domain operationalisation, because the stress test found its three ingredients in unrelated fields, making non-combination weak evidence.*

---

## N. Canonical research chain

| Step | Content | Why the next step follows |
|---|---|---|
| **Problem** | Fishers decide departure under conditions they cannot instrument; no marine-warning archive; official criteria define warning onset, not caution onset | A decision-support system is a plausible response, and it must be governed |
| **Prior work** | Advisory-type inhibition by external state (TCAS, TAWS); totality over incomplete observations (RV); bounds from unmeasured variables (Manski); graduated governance (Baxi, AMAGF, Flehmig) | The mechanisms exist; nothing needs inventing |
| **Limitation** | Each mechanism is defined for its own conditioning variable and governed object; none is specified for a multi-source *environmental* classifier driving *human-facing advisory categories*; and none reports activation frequency | Composition is required, and its behaviour is unmeasured |
| **Gap** | Gap A (composition) + Gap B (empirical characterisation) | Two distinct questions follow |
| **RQ1 / RQ2** | Specification question; frequency question | RQ1 answered by design and proof; RQ2 by replay |
| **Design** | `E → S = f(E) → (G(S), A_AI(S)) → AI(E) → Human`; five components, worst-case aggregation, `D = {m}` | The design must be shown internally consistent |
| **Formal properties** | P1 totality, P2 containment, P3 Safety Dominance, P4 C1 ≡ C3 | Consistency shown; but proofs cannot establish frequency |
| **Evaluation** | Four-condition replay, 43,848 hours, two configurations | Frequency is measurable only against a record |
| **Results** | Δ_L2 = 5.81% / 4.48%; C1 ↔ C3 = 0.00% (entailed) | Results bound what may be claimed |
| **Contribution** | Empirical characterisation (primary); domain operationalisation and composition (secondary); contract conformance and method (supporting) | — |

### ⚠️ Flagged breaks

1. **RQ1 → Formal properties is weak.** The proofs establish that the specification is self-consistent, which is not in doubt once it is written down. The arrow is defensible only if RQ1 is read as *"what must be decided, and what follows from those decisions"*.
2. **Design → Evaluation carries an unevaluated core.** `A_AI(CAUTION) = {Go, Delay}` is the researcher-defined heart of the design, and Δ_L2 is invariant to it (§J). The chain passes through a decision the evaluation cannot see.
3. **Results → Contribution is sound only for the primary contribution.** The secondary composition contribution has no evidence beyond the specification existing.

---

## O. Reviewer attack test

**1. "Isn't this just TCAS/TAWS applied to fisheries?"**
Substantially, at the mechanism level — yes, and the thesis should say so first. TSO-C151c §5.6 already inhibits advisory categories on input validity, human-facing, with annunciation. The defensible reply is that the transfer is non-trivial (single certified validity-checked input → unattended multi-source environmental classifier; fixed per-function rules → state-indexed admissible set) and that the activation frequency of such a scheme has not been reported. **Answerable, but only in a conceding form.**

**2. "Where is the actual Computer Science contribution?"**
The empirical characterisation and the operational specification. The formal properties are contract conformance, not new theory. **OPEN — this is the weakest point of the thesis and a supervisor decision, not an evidential one.**

**3. "Why are three states necessary?"**
They are not *necessary*. Three is researcher-defined, with independent motivation from Flehmig's tripartite index. What is defensible: a third state changes nothing unless it changes the admissible set (P4). **Answerable.**

**4. "Why is CAUTION `{Go, Delay}`?"**
A researcher-defined judgement that timing and duration advice is least supportable when conditions are marginal. Not externally sourced and not evaluated. **OPEN — additional evidence required.**

**5. "Why should 5.81% matter?"**
Because it could have been ≈0, which would have made the intermediate level vacuous at this site. It establishes non-vacuity, nothing more. **Answerable.**

**6. "Does 5.81% prove improved safety?"**
No. No incident record exists; this is characterisation, not validation. **Answerable — the report already states this.**

**7. "Why is this a PhD rather than an engineering implementation?"**
The strongest available answer: the empirical characterisation and the methodological discipline. The mechanism composition alone would not suffice. **OPEN — genuinely contestable.**

**8. "Are the thresholds validated?"**
Traced to named authorities, not validated against outcomes. `g_r` CAUTION at 10.0 mm/hr is admittedly non-MET. The night ⇒ UNSAFE policy has no source. **Answerable with concession.**

**9. "What happens without marine-warning data?"**
`D = {m}`, pinned SAFE; `g_m` can only raise severity, so all severity figures are lower bounds. Mechanism conceded to Manski. **Answerable.**

**10. "Would changing thresholds destroy the result?"**
**OPEN — additional evidence required.** No threshold-sensitivity analysis exists. Δ_L2 is a direct function of thresholds, one of which is non-MET. This is the most dangerous unanswered attack. See §L.

**11. "Why separate `G(S)` and `A_AI(S)`?"**
So participation and scope can be reasoned about and changed independently; Baxi's unified tier index cannot express one without the other. No evidence that the separation produces a better outcome. **Answerable as a design rationale, not as a result.**

**12. "What does the experiment establish that the formal definition does not already imply?"**
The definition implies that *if* CAUTION occurs, the admissible sets differ. Only the replay establishes *how often* CAUTION occurs on real conditions — a fact about the site and thresholds that no proof supplies. **Answerable, and this is the cleanest single justification for the experiment.**

---

## P. Decision gates

| Gate | Verdict |
|---|---|
| **Gate 1 — Research gap** | **REVISE** — split into Gap A and Gap B; adopt §R wording; delete every absence-style claim from §2/§3.1 of the report |
| **Gate 2 — RQs** | **REVISE** — adopt §E; remove RQ3 and RQ5 from the contribution frame; merge RQ-J4 into RQ-J3 |
| **Gate 3 — CS contribution** | **REVISE** — adopt §M hierarchy and §Q statement; empirical characterisation primary, not architecture |
| **Gate 4 — Experiment** | **NEEDS STRENGTHENING** — threshold sensitivity and E5 are REQUIRED; the replay alone is sufficient for the primary contribution but not for the thesis as currently scoped |
| **Gate 5 — Architecture framing** | **REVISE** — reframe as operational composition; adopt §F |

---

## Q. Locked contribution statement

> This work specifies and empirically characterises a graduated advisory-scope governance contract for AI decision support in a low-resource environmental setting. The governance mechanisms it uses are established: advisory-category inhibition conditioned on externally measured state is a certification requirement in collision-avoidance and terrain-awareness avionics; totality of classification over incomplete observations is established in runtime verification; and bounding a reported quantity from a declared unmeasured variable is standard partial-identification practice. The contributions are threefold. First, an empirical characterisation, over five years of hourly environmental records for one deployment site and under two environmental-data configurations, of how often an intermediate advisory-scope state admits a strictly smaller recommendation set than a participation-only gate — a measurement not previously reported in the reviewed literature, and one that could have returned a null result. Second, a domain operationalisation for small-scale Malaysian coastal fisheries in which every threshold is traced to a named authority, the absence of an official lower criterion is documented rather than filled, and researcher-defined choices are separated from externally supported ones. Third, an operational specification in which AI participation and admissible advisory scope are expressed as two separately state-conditioned functions rather than a single graduated index. The formal properties proved — classifier totality, admissible-set containment, and safety dominance — establish that the implementation satisfies its intended governance contract; they are not offered as new theory. No claim is made about accident reduction, decision quality, or classification correctness: no incident record exists for the site, and the evaluation is a characterisation of governance behaviour only.

---

## R. Locked research gap statement

> Governance of AI decision support is often framed around a single question — whether the AI may participate. A second question, which categories of recommendation it may present, is answered at runtime in certified aviation systems: TCAS II inhibits advisory types as radio altitude and aircraft configuration change, and TAWS inhibits terrain-avoidance and premature-descent alerts when the position source is faulted or invalid, annunciating the restriction to a crew that retains authority. Formal treatment of classification over incomplete observations is established in runtime verification, and directional bounds arising from declared unmeasured variables are standard in partial-identification methodology. Within the reviewed literature, however, these were not found composed into a single operational contract in which participation and advisory scope are specified as two separate functions over a classified multi-component *environmental* state assembled from heterogeneous, independently-faulting sources; and no empirical characterisation was identified of how often such an intermediate advisory-scope level changes the admissible recommendation set when replayed over a multi-year environmental record. The first is an operationalisation gap and is modest. The second is an evidence gap, and it is the one this work principally addresses.

---

# **RESEARCH CHAIN REQUIRES TARGETED REVISION**

The chain is coherent and defensible end to end once the framing is corrected, but it is not yet lockable, for three specific reasons rather than any general weakness. The literature position, the formal claims and the primary empirical contribution are all sound and evidenced; what breaks is the alignment between what the thesis currently claims and what the evidence supports. Gates 1, 2, 3 and 5 all return REVISE, and none requires new research — only rewriting to the wordings in §E, §Q and §R.

Gate 4 is the substantive one. Two experiments are REQUIRED rather than desirable. **Threshold sensitivity** is the most dangerous unanswered reviewer attack: Δ_L2 is a direct function of thresholds, one of which (`g_r` CAUTION at 10.0 mm/hr) is openly non-MET, and a single point estimate from a single threshold set will not survive informed questioning. **Target-hardware benchmarking** must either be completed or RQ-J2 removed, since an RQ with no evidence is worse than no RQ. Both are bounded; neither requires new data collection.

The one structural problem that no rewriting fixes is this: `A_AI(CAUTION) = {Go, Delay}` is the researcher-defined heart of the design, and the headline result is mathematically invariant to it — because C1 and C2 differ only in that cell, Δ_L2 equals the CAUTION occurrence rate whatever the cell contains. The thesis therefore measures how often the intermediate state is reached, not whether the restriction it applies is the right one. This should be stated plainly in the limitations rather than left for a reviewer to notice, and it is the strongest argument for the advisory-content ablation in §L — which must be properly specified before it is attempted, since admissible-set divergence cannot measure it.
