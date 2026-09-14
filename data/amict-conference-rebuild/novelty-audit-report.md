# Novelty Audit Report — AMICT Conference Rebuild

**Date:** 2026-09-14
**Task:** targeted novelty audit, gate for all subsequent conference-rebuild work
**Companion artefact:** [`novelty-defence-matrix.md`](novelty-defence-matrix.md)
**Manuscript status:** not drafted. No conference manuscript was created in this task.

---

## 1. Novelty audit verdict

    NOVELTY_AUDIT = STOP_MATERIAL_EQUIVALENCE_FOUND

A materially equivalent prior mechanism exists. It is not in the research literature the review has covered; it is in certified operational avionics.

This verdict is issued against the *primary novelty question as posed*. It is not a finding that the work has no contribution. Sections 5, 6 and 10 set out what survives, and the recommendation is **reposition**, not abandon. But the contribution cannot be frozen in its current form, and the manuscript must not be drafted against the current C1 wording.

---

## 2. Answer to the primary novelty question

> *Has prior work already implemented a runtime mechanism in which the set of AI recommendation types that may be presented to a human decision-maker is dynamically restricted according to an externally classified risk or environmental state, while final human decision authority remains invariant?*

**Yes — with one qualification and one partial shortfall.**

TCAS II / ACAS II implements, in certified airborne equipment, a runtime mechanism in which the set of resolution-advisory types that may be issued to a human pilot is progressively inhibited as an externally measured state — radio-altimeter height above ground level, banded, together with aircraft-configuration discretes — becomes more hazardous. Per FAA AC 20-151A:

| Band (AGL, descending) | Admissible advisory types |
|---|---|
| above 1450 ft | full RA set |
| below 1450 ft | Increase Descent inhibited |
| below 1000 ft | Descend additionally inhibited |
| below 900 ft | all RAs inhibited — TA only |
| below 400 ft | TAs additionally inhibited |

The admissible sets are **nested and monotone in hazard severity**, contracting to empty. This is the same structural relation as `A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅`, realised on a five-band rather than three-state lattice, and it has been deployed for roughly three decades.

**The qualification:** the advisory generator is a deterministic collision-avoidance algorithm rather than an AI component. This does not rescue the claim. The mechanism under audit is the *governance* of an advisory space, not the internals of the advisor, and the task directs that mechanisms be compared rather than terminology. The distinction is further weakened by this project's own architecture: Layer 3 is a deterministic rule engine, so the governed component here is of the same computational kind as TCAS's advisory logic.

**The partial shortfall:** human final authority is *procedurally* rather than *structurally* invariant in TCAS. ICAO procedures expect RA compliance; the pilot may deviate, but compliance is the norm. This work asserts unconditional human authority as a structural property of the architecture. This is a real difference, but it is a difference in the *strength of an accompanying property*, not in the mechanism, and it is not sufficient on its own to sustain a novelty claim for the mechanism.

A second, independent finding compounds the first. **ACAS X advisory logic has been formally verified** — hybrid-systems proofs and probabilistic model checking of state-conditioned advisory selection are published. Formal enforcement of advisory admissibility therefore also has precedent.

---

## 3. Closest three prior mechanisms

1. **TCAS II / ACAS II low-altitude RA inhibition** (matrix N-01). Externally measured state → banded classification → nested admissible advisory-type set → human pilot decides. Overlap on the primary question is near-total.
2. **ACAS X formally verified advisory logic** (N-02). Adds proved safety properties over state-conditioned advisory selection, removing formal enforcement from the claimable set.
3. **Baxi (2026), Comprehension-Gated Agent Economy** (N-07). The closest *research-literature* formal parallel: a gate function mapping a vector to discrete tiers with nested permission sets and a proved monotonicity analogue — but over an agent's executable economic permissions, conditioned on agent-internal robustness audits, with no human adviser loop.

Two further findings bound the space. **Parasuraman, Sheridan & Wickens (2000)** already contains graduated restriction of the presented option space — Level 2 "offers a complete set of decision/action alternatives", Level 3 "narrows the selection down to a few", Level 4 "suggests one alternative" — assigned at design time. And **state-conditioned restriction of an admissible set** is the defining pattern of shielding and action masking, thoroughly established over executable action spaces.

---

## 4. Exact overlap with our mechanism

Coded element by element against TCAS II:

| Element of our mechanism | Present in TCAS II? |
|---|---|
| Runtime, per-encounter operation | Yes |
| Externally sourced state, independent of the advisor | Yes — radio altimeter, configuration discretes |
| State banded into discrete classes | Yes |
| Admissible advisory-type set conditioned on that class | Yes |
| Nested containment across classes | Yes |
| Monotone contraction as severity increases | Yes |
| Empty admissible set at maximum severity | Yes — all RAs inhibited |
| Advisory presented to a human who then decides | Yes |
| Participation gating distinguished from scope restriction | Implicitly — the lowest bands gate the function off entirely |
| Human final authority invariant | Partial — procedurally constrained |
| Advisor is an AI component | No — deterministic algorithm |
| Multi-component environmental classifier with max-severity aggregation | No — single scalar plus configuration discretes |
| Stated and proved containment property over the advisory set | No — certified design table (but see ACAS X, N-02) |
| Abstracted and presented as a governance construct | No |
| Empirical characterisation against a binary-governance comparator | No |

Ten of fifteen elements are fully present. The mechanism is not new. What is absent from the prior work is its *abstraction, formalisation, generalisation beyond one hazard variable, and empirical characterisation as governance*.

---

## 5. Exact remaining distinction

Stated as narrowly as the evidence supports, and no more narrowly than it requires:

1. **Generality of the conditioning state.** TCAS conditions advisory admissibility on one scalar plus configuration discretes. This work conditions on a classified multi-component environmental state `S = f(E)` aggregated by max severity over five component classifiers, with declared exclusions and `⊥` semantics. No prior work identified conditions an advisory-type set on a multi-component environmental classification.
2. **Abstraction as a governance construct.** TCAS's inhibition schedule is a device-specific certified design table. No prior work identified states the pattern as a general governance pair separating AI participation `G(S)` from admissible advisory scope `A_AI(S)`, applicable across domains and advisory generators.
3. **Proved containment over the advisory set as a general property.** ACAS X verification targets collision-avoidance safety of specific manoeuvre advisories. Totality, monotonicity of `A_AI` over a severity order, and containment `AI(E) ⊆ A_AI(f(E))` as *general properties of a governance abstraction* were not found in prior work.
4. **Structurally unconditional human authority.** Asserted here as an invariant of the architecture rather than a procedural expectation.
5. **Empirical characterisation of the intermediate level against binary governance.** No prior work identified measures how often a graduated advisory-scope level produces governance outcomes that a participation-only gate does not. This is what `ΔL2` and `C1↔C3` do.

Distinctions 1–3 and 5 are defensible. Distinction 4 is real but thin, and should not be load-bearing.

**What is explicitly NOT distinctive:** the mechanism pattern itself; runtime state-conditioned restriction of an admissible set; graduated non-binary governance; nested monotone containment; formal verification of advisory constraints; a three-level or traffic-light topology; the idea that recommendation *type* is a governable variable.

---

## 6. Strongest defensible novelty / contribution statement

> Restriction of the advisory types an automated system may present to a human, conditioned on an externally measured state, is established practice in certified collision-avoidance avionics, where resolution-advisory types are progressively inhibited as radio altitude decreases, and where the resulting admissible sets are nested and contract to empty. Within the reviewed AI decision-support and AI-governance literature we did not identify a corresponding general construct: an advisory space conditioned on a classified multi-component environmental state, specified independently of any one hazard variable or advisory generator, carrying proved totality, monotonicity and containment properties, and characterised empirically against participation-only governance. This work supplies that construct, together with a bounded executable conformance evaluation and a retrospective environmental replay quantifying how often the intermediate level changes the governance outcome.

Every clause is scoped. The claim is **formalisation, generalisation and empirical characterisation of an existing mechanism pattern**, not invention of the mechanism.

**Consequential rewrite required to C1.** The frozen wording proposed in the task — *"A runtime governance mechanism separating AI participation from state-conditioned admissible advisory scope"* — reads as a claim to have devised the mechanism. It must become a claim to have *specified and generalised* it. This is the principal input to the contribution-freeze task.

---

## 7. Claims that must NOT be made

Absolutely prohibited, now evidence-backed rather than precautionary:

- "no existing architecture restricts AI advisory scope based on classified state" — **false** as stated; TCAS does, for a non-AI advisor
- "the first architecture to restrict what an AI may recommend at runtime"
- "first", "first-ever", "unprecedented", "globally novel", "uniquely novel"
- "the first formal treatment of advisory admissibility" — ACAS X precedes it
- "the first formally proved graduated governance architecture" — Baxi (2026) precedes it
- "conditioning an admissible set on runtime state is novel" — shielding precedes it
- "the intermediate state is novel" — three-level topologies are established (Flehmig, Ghaleb)
- any unqualified generalisation from `C1↔C3 = 0.00%` to all traffic-light systems
- any claim of improved safety, risk reduction, accident prevention, trust, calibrated reliance, decision quality or real-world effectiveness

Two prior claims in the existing manuscript line require specific correction:

- v3 line 479 — *"The review's central claim is that no existing architecture restricts advisory scope as a function of classified safety state"* — must be rescoped to the reviewed AI literature, with the avionics precedent stated explicitly rather than omitted.
- The `CLAUDE.md` house framing *"which no existing architecture implements"* is no longer supportable in unscoped form and should be read as superseded by this audit for manuscript purposes.

Required scoped formulations: *"Within the reviewed literature…"*, *"We did not identify prior work in the reviewed literature that…"*, *"Outside the AI literature, an analogous mechanism exists in certified avionics…"*.

---

## 8. Is "graduated advisory-scope governance" still defensible?

**Yes, as a descriptive term. No, as a claimed-novel mechanism.**

The phrase accurately names what the architecture does and distinguishes the governed object (advisory scope) from the alternatives the families govern (participation, prediction availability, executable actions, supervisory intensity, autonomy level). Retain it as terminology.

It must not be introduced as though naming the thing establishes that the thing is new. On first use the term should be defined and immediately positioned against the avionics precedent. Renaming the mechanism to evade the precedent would be exactly the rescue-by-terminology the audit prohibits.

---

## 9. Is the proposed title still defensible?

**Yes.** *"Evaluating Graduated Advisory-Scope Governance for AI Decision Support"* survives the audit unchanged, and survives better than most alternatives would.

The operative verb is *Evaluating*. The title claims to evaluate a governance approach, not to have invented it — which is precisely the repositioned contribution. It contains no symbols, no mathematics and no subtitle, satisfying the template constraints. It should be treated as **provisional-confirmed**: retained pending the contribution freeze, and re-checked once C1 is reworded.

---

## 10. Recommendation for C2

    C2 = SUPPORTING IMPLEMENTATION EVIDENCE

Not a standalone contribution.

Assessed against the evidence as it stands:

- `R-SAFE-001 = DEFERRED`. The SAFE rule set is empty.
- All 32 SAFE fidelity episodes generated zero advisory records.
- All implemented rules are `R-CAUTION-001` … `R-CAUTION-004`.
- Every one of the 454 advisory records carries the single conclusion type `Delay`. 454 is a count of records, not of types.
- F1/F2/F3 establish bounded conformance to a configured admissibility contract within a deterministic interface-contract state space — not real-world effectiveness.

The consequence is structural: containment was demonstrated **only on the restrictive side**. No rule in the evaluated configuration is capable of emitting `Go`, `DepartureTime` or `Duration`, so no advisory was ever generated that a narrower state would have had to suppress. The evaluation confirms that a rule engine configured with four `Delay` rules emits only `Delay`, and that the interface contract held across 292 episodes with zero violations. That is a genuine and correctly reported conformance result. It is not an independent scientific contribution.

The novelty finding sharpens this further. With the mechanism pattern shown to be established practice, "we built one and it conformed" carries less weight as a contribution than it would have if the mechanism itself were new. Its proper role is as evidence that the formal specification in C1 is executable and that the containment property survives implementation — which is exactly what a formalisation contribution needs.

**Recommended disposition:** fold C2 into C1 as an implementation-conformance subsection, and promote C3 — the retrospective environmental replay — to the second headline contribution. This yields two contributions rather than three, which also eases the six-page constraint.

Reporting boundary unchanged: the only permitted fidelity claim remains *"The executable implementation produced zero violations of the configured advisory admissibility contract within the bounded deterministic interface-contract fidelity state space."*

---

## 11. What the audit does not change

Recorded so the subsequent task inherits them intact.

- **Baseline decision:** `publications/active/ipsci-2026/submissions/v3-revision/manuscript-v3.md` is the conference-paper baseline for the rebuild, **not** v2.5. Not drafted from in this task.
- **Evidence base:** frozen. No figure was recomputed, no workstream reopened. `P1–P4` CLOSED, `F1–F3` CLOSED/PASS, `E1–E4` and `E6` CLOSED, `E5` OPEN, `H3` OPEN/UNSUPPORTED, `R-SAFE-001` DEFERRED.
- **`Property 5.1 / 5.2 / 5.3`** are legitimate formal objects and were not touched. The obsolete pattern is `Theorem 5.x` only.
- **Superseded-figure blacklist** observed. No blacklisted figure appears in either artefact.
- **`g_w` two-number rule**, **`g_m` / κ lower-bound disclosure**, **withdrawn mode-chattering claim**, **qualified hysteresis framing**, **solar provenance naming**, **formal-model consistency** — all preserved; none was restated or reinterpreted here. In particular the 10.36% hysteresis figure is not used in this audit and must continue to be reported only as a precaution, never as evidence that hysteresis was required or that a mode-chattering problem was observed.
- **No manuscript, `.docx`, `.pdf`, `.tex` or template formatting** was produced. No six-page compression begun.

---

## 12. Required next actions before the contribution freeze

1. **Decide the repositioning.** Accept the §6 statement, or direct an alternative. The paper cannot be frozen against the current C1 wording.
2. **Add six works to the corpus** — `notes/` plus `docs/canonical/citation-notes-map.md` — before any drafting cites them: FAA AC 20-151A / TCAS II inhibition; ACAS X formal verification; Parasuraman, Sheridan & Wickens (2000); the adaptive-autonomy human-factors review; selective AI prediction in clinical decision making (arXiv:2508.07617); FDA CDS guidance Criterion 3. The first three are load-bearing for Related Work and their omission would be a defensible reviewer objection.
3. **Confirm the C2 disposition** in §10, which changes the contribution count from three to two.
4. **Re-examine the RQ set.** RQ1 as phrased is answered by construction. With the mechanism repositioned, an RQ asking whether the *generalised* construct can be specified and enforced reads better than one asking whether containment can be enforced at all.

---

## 13. Assessment of this verdict

The STOP is issued on a genuine mechanism match, not a terminological one, and it was found by looking outside the corpus rather than inside it — families A and D were flagged as the weak coverage, but the material equivalence surfaced in family E, in operational practice rather than in the literature.

The finding is recoverable. A reviewer who knows TCAS would have raised it, and a paper that states the precedent, then shows what the precedent lacks — generality, abstraction, proved containment, empirical characterisation against a binary comparator — is stronger than one that does not mention it. The prior rejection cited insufficient evidence for novelty claims; meeting that objection by narrowing the claim to what the evidence supports is the correct response.

The work is not abandoned. It is reclassified from *inventing a mechanism* to *formalising, generalising and empirically characterising one*. That is a smaller claim and a defensible one.

    NOVELTY_AUDIT = STOP_MATERIAL_EQUIVALENCE_FOUND
    CONFERENCE_MANUSCRIPT = NOT_DRAFTED
    CONTRIBUTION_FREEZE = BLOCKED_PENDING_REPOSITIONING_DECISION
