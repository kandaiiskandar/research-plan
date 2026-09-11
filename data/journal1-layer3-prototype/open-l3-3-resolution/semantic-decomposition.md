# OPEN-L3-3 Semantic Decomposition — Propositions P1–P5

**Purpose.** Determine which of five distinct propositions the Appendix C §C.4 line 791 statement actually asserts. The propositions must not be collapsed.

**Target statement (verbatim, appendix-c-formalisation.md line 791, commit c42aae6c 2026-04-10):**

> When S = CAUTION, the **Go** recommendation is automatically presented by the system with a caution qualifier (e.g., "Proceed with caution"). The recommendation type remains **Go**, but its presentation and explanation are modified by the safety state. This preserves set containment while allowing state‑dependent advisory messaging.

---

## P1 — Admissibility

**Formal form.** `Go ∈ A_AI(CAUTION)`.

**Status in repository.** Established. `A_AI(CAUTION) = {Go, Delay}` is stated in appendix-c §C.4 (lines 781–784) and repeated in Theorem C.2 case 2 (line 860). It is not the subject of dispute.

**Does line 791 assert P1?** Yes — trivially, because the containment relationship on the previous line (789) already established it. The line 791 statement operates *within* the space already opened by P1.

---

## P2 — Rule availability

**Formal form.** `∃ r ∈ RS(CAUTION) : conclusion_type(r) = Go`.

**Status in repository.** Currently unsatisfied. `rule-candidate-register-batch2.csv` contains four CAUTION rules (R-CAUTION-001…R-CAUTION-004), all concluding Delay. No Go rule exists in RS_candidate(CAUTION).

**Does line 791 assert P2?** No. §C.4 is the *admissible-set* section (A_AI(S)). RS(S) is not introduced until §C.7.1 (line 897). The line 791 statement does not define, imply, or presuppose the existence of a rule; it operates on the set A_AI(CAUTION) directly. The Batch 2 gap-register entry GAP-03 explicitly records the absence of any CAUTION-Go rule evidence.

---

## P3 — Rule firing

**Formal form.** `∃ r ∈ RS(CAUTION) : antecedent(r) evaluates true on E`.

**Status in repository.** Vacuously false — no CAUTION-Go rule exists (P2 fails), so none can fire.

**Does line 791 assert P3?** No. Firing is a run-time property of a rule's antecedent, not a set-definition property. Line 791 makes no antecedent claim.

---

## P4 — Advisory generation

**Formal form.** `Go ∈ AI(E)` where AI(E) is the set produced by Layer 3 under the active rule set.

**Status in repository.** AI(E) is defined via the rule engine (justification-layer3-enforcement §3–§4). Interpretation A would extend AI(E) to include a Go generated *without* a firing rule — but Algorithm 4 (Batch 4) specifies `AI = engine.reason(E, RS(S))` with no other emission path, and the Layer 3 justification explicitly rules out post-hoc generation ("There is nothing to filter" — §3).

**Does line 791 assert P4?** Only under Interpretation A — and that reading requires a generation mechanism that no current authority specifies. Under Interpretation B, P4 is a *precondition* the statement conditions on (if Go was generated, present it with a qualifier); the statement itself does not create P4.

---

## P5 — Automatic presentation

**Formal form.** `S = CAUTION → system presents Go automatically` — read either as (a) automatic *emission* into AI(E) followed by mandatory presentation, or (b) automatic *presentation attribute* attached to Go if produced.

**Status in repository.** The parallel canonical text in `architecture-illustration.md` §"Why Go carries a caution qualifier in CAUTION mode" (lines 202–204) resolves this without using the word "automatically" at all — it uses "presented", "communicates", "understands". Reading (a) has no corresponding architectural mechanism; reading (b) is what §137 of architecture-illustration.md, §793 of appendix-c, and the Batch 2 Go semantics converge on.

**Does line 791 assert P5?** Yes — but the intended reading is (b), presentation attribute. Evidence:
- The full sentence continues: *"The recommendation type remains Go, but its presentation and explanation are modified by the safety state."* — "presentation and explanation" are presentation-layer concepts.
- The purpose clause states: *"This preserves set containment while allowing state‑dependent advisory messaging."* — "messaging" is presentation.
- The parallel statement in `architecture-illustration.md` §202 is unambiguous on reading (b): *"The qualifier communicates that conditions are elevated and the fisher should exercise additional vigilance."*

---

## Which proposition does line 791 actually assert?

**Line 791 asserts P5 in its reading-(b) form: a presentation-layer attribute (caution qualifier) that attaches to a Go advisory generated through the normal rule-engine path (P2 → P3 → P4).**

The statement does not:

- extend `A_AI(CAUTION)` (P1 is unchanged),
- create a rule (P2 is unchanged),
- fire a rule (P3 is unchanged),
- generate an advisory outside the rule engine (P4 mechanism unchanged),
- mandate that Go must always appear under CAUTION (reading-(a) is refuted by parallel canonical text and by the absence of any emission mechanism).

The Batch 2 working classification of line 791 as **B (UI/presentation guidance)** — recorded in `closure-batch2.json` and `semantic-verification-batch2.json` — is confirmed by this decomposition. OPEN-L3-3 was opened only because the surface word "automatically" leaves the wording *readable* as reading-(a); provenance and every downstream architectural authority make reading-(b) the intended and consistent meaning.

---

## Formalisation of Interpretation B

Given the decomposition, the presentation rule is:

```
S = CAUTION  ∧  Go ∈ AI(E)   →   Present(Go, caution_qualifier)
```

Not:

```
S = CAUTION   →   Go ∈ AI(E)
```

The antecedent `Go ∈ AI(E)` is preserved as a distinct precondition. The consequent modifies the presentation of an already-generated Go, not the set of advisories generated.

---

## What this decomposition does NOT do

- It does not add a rule to RS(CAUTION). `RS_candidate(CAUTION)` remains Delay-only under current scientific evidence, and P2 remains false at Batch 2 scope.
- It does not remove Go from `A_AI(CAUTION)`. P1 is preserved: an admissible recommendation type does not require a current concrete rule.
- It does not create a fifth recommendation type. `R = {Go, Delay, DepartureTime, Duration}` is unchanged. "Go with caution qualifier" is the same type Go with presentation metadata.
- It does not turn Go into approval or CAUTION into prohibition. Human authority remains unconditional.
- It does not modify Algorithm 3 or Algorithm 4. The generation path is unchanged.
