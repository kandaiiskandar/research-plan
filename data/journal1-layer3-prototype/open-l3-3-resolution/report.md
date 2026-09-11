# OPEN-L3-3 Resolution Report

**Item:** OPEN-L3-3 — CAUTION Go presentation-versus-rule semantics
**Verdict:** **CLOSED under Resolution B (presentation qualifier only)**
**Date:** 2026-09-11
**Branch:** feat/journal1-layer3-prototype
**Task authority:** `docs/tasks/ournal 1 Layer 3 Prototype L3 resolution.md`

---

## 1. The exact Appendix C statement (verbatim, before this task)

`docs/canonical/appendix-c-formalisation.md` line 791, §C.4 "AI-Admissible Recommendation Space":

> When S = CAUTION, the **Go** recommendation is automatically presented by the system with a caution qualifier (e.g., "Proceed with caution"). The recommendation type remains **Go**, but its presentation and explanation are modified by the safety state. This preserves set containment while allowing state-dependent advisory messaging.

**Introduced:** commit c42aae6c 2026-04-10 (git blame line 791). §C.4 body established by commit 978df609 2026-04-05.

**Immediately follows** the containment relationship on line 789 (`A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅`) and is followed on line 793 by the restriction clarification ("under CAUTION conditions, the AI cannot provide timing optimisation or trip duration recommendations").

---

## 2. Provenance findings

**Chronology (git log):**

| Date | Commit | Change | Bearing on OPEN-L3-3 |
|---|---|---|---|
| 2026-04-05 | 978df609 | §C.4 body first added (A_AI table, containment relationship) | Sets the section as an admissible-set definition, not an emission mechanism |
| 2026-04-10 | c42aae6c | Line 791 added ("automatically presented…caution qualifier") | The target sentence |
| 2026-04-25 | f517fc1 | `justification-layer3-enforcement.md` added — Layer 3 = production rule system, RS(S) supply, no post-hoc generation, proof by construction | Line 791 predates this enforcement mechanism by **15 days** |
| 2026-07-20 → 2026-09-09 | a182cc4, 115429a, cdc6608, 8ef8a26, af97c67 and others | Multiple §C.4 restructurings including §C.7.1 enforcement mechanism and §C.7.2 Theorem C.3 (Safety Dominance operational form) | Line 791 was **retained** through each restructuring with the same content. Retention through later revisions is consistent with continued treatment as presentation guidance, particularly when read alongside the clearer parallel canonical wording in `architecture-illustration.md` §202–204; retention alone is not treated here as proof of conscious reinterpretation. |

**Parallel canonical text (retained, not superseded):** `docs/canonical/architecture-illustration.md` §"Why Go carries a caution qualifier in CAUTION mode" (lines 202–204):

> "When S = CAUTION, the Go recommendation type remains available but is presented with a caution qualifier (e.g., "Proceed with caution"). The recommendation type is unchanged — it is still a Go/no-go assessment. **The qualifier communicates that conditions are elevated and the fisher should exercise additional vigilance.** This design preserves set containment (Go ∈ A_AI(CAUTION) and Go ∈ A_AI(SAFE) — same type in both) while ensuring the fisher understands that CAUTION-mode advice carries a different risk profile than SAFE-mode advice."

The word "automatically" does not appear here. The verbs are *presented*, *communicates*, *understands* — all presentation-layer.

**Downstream authority that contradicts Interpretation A:**

- `appendix-c-formalisation.md` §C.7.1 lines 896–904: "The rule engine fires only rules present in the active RS(S). ... The constraint is structural — it holds before generation begins, **not by filtering outputs after the fact**."
- `justification-layer3-enforcement.md` §3: "Their absence is not the result of checking and rejecting outputs after the fact — no rule that generates those types exists in the active configuration. **There is nothing to filter.**"
- `docs/tasks/Journal 1 Algorithm Specification batch 4.md` §11 (Algorithm 4 wrapper): `check G(S); if 0 → return ∅; else → invoke engine.reason(E, RS(S))` — **no third emission branch**.
- Batch 2 semantics of Go (`recommendation-semantics-batch2.csv`): "The rule system found no active Delay antecedent in the resolved environmental inputs." — a **rule-based negative-existential** conclusion, not an S-conditional emission.
- Batch 2 `rule-candidate-register-batch2.csv` R-REJ-002: `IF S == CAUTION THEN Delay` REJECTED as "state-restatement without independent evidence." A hypothetical `IF S == CAUTION THEN Go` would exhibit the same state-restatement structure; under the Batch 2 methodology it would therefore require independent advisory-mapping evidence rather than being justified solely from the CAUTION state or from Go ∈ A_AI(CAUTION). No such evidence currently exists (GAP-03); whether a future rule with that antecedent could be defended by independent evidence is a separate question not decided here.

Full provenance rows: `authority-trace.csv` (16 rows).

---

## 3. Authority hierarchy findings

For every category defined in task §6, the target statement's classification is:

| Category | Applies? | Basis |
|---|---|---|
| A — Formal normative architecture authority | NO | Would require an emission mechanism; none exists in §C.7, §C.8, Algorithm 3, Algorithm 4, or `justification-layer3-enforcement.md`. |
| B — Scientific advisory-rule authority | NO | Would require a rule in RS(CAUTION); the Batch 2 rule-candidate register contains none, and GAP-03 records zero empirical support. |
| C — Governance admissibility authority | PARTIAL | The statement operates *within* an admissible-set section (§C.4). It reaffirms Go ∈ A_AI(CAUTION) but does not extend the set. |
| **D — UI/presentation guidance** | **YES** | The statement is written inside a set-definition section, its own continuation frames the point as "presentation and explanation…state-dependent advisory messaging", the parallel `architecture-illustration.md` §202 uses only presentation verbs, and the Batch 2 closure record already classified it as D-equivalent (there labelled "B (UI/presentation guidance)"). |
| E — Illustrative/example text | NO | The example ("Proceed with caution") is illustrative but the surrounding claim is not. |
| F — Historical/superseded design residue | NO | Retained through multiple subsequent restructurings; not superseded. |

---

## 4. P1–P5 semantic decomposition

Full derivation: `semantic-decomposition.md`. Result:

| Proposition | Formal | Asserted by line 791? |
|---|---|---|
| P1 admissibility | Go ∈ A_AI(CAUTION) | Yes (trivially — line 783 already established it) |
| P2 rule availability | ∃ r ∈ RS(CAUTION) : conclusion_type(r) = Go | **No** — §C.4 is the admissible-set section; RS(S) is not introduced until §C.7.1 |
| P3 rule firing | ∃ r ∈ RS(CAUTION) : antecedent(r) evaluates true | **No** — vacuous, P2 false |
| P4 advisory generation | Go ∈ AI(E) | **No** — treated as a *precondition* under Interpretation B, not an entailment |
| P5 automatic presentation | System attaches caution qualifier to Go when presented | **Yes** (in its presentation-attribute reading — reading b) |

The intended reading of "automatically" is that the qualifier is applied automatically *when* Go is presented, **not** that Go is automatically emitted.

---

## 5. Algorithm 3 / Algorithm 4 compatibility

- **Algorithm 3 — Rule-Set Supply.** Contract `ConclusionTypes(RS(S)) ⊆ A_AI(S)` unchanged. RS(CAUTION) conclusion types = {Delay} ⊆ {Go, Delay} = A_AI(CAUTION). ✅
- **Algorithm 4 — Governed Advisory Generation.** Wrapper `check G(S); if 0 → return ∅; else → invoke engine.reason(E, RS(S))` unchanged. Presentation qualifier is applied on the presentation layer, downstream of `engine.reason()`. ✅
- **No post-hoc advisory generation introduced.** ✅
- **Theorem C.3 (Safety Dominance).** `AI ⊆ A_AI(F_{D,τ})` unchanged; Go remains admissible under CAUTION whether produced by a rule or not. ✅

---

## 6. Cautious-go evidence interpretation

Gao (2024) "go/cautious-go/don't-go" is a **behavioural category** observed in Penang fishers, distinct from an AI advisory conclusion. `notes/Mapping the decision-making factors of small-scale fishers.md` line 189 states: *"Fishers implicitly classify conditions into go/cautious-go/no-go states, but does not formalise this classification."*

- Mapping cautious-go → CAUTION *state* is an architectural interpretation, defensible and preserved.
- Mapping cautious-go → *a Go advisory* would be a further, distinct interpretation which the Batch 2 register did NOT adopt.
- **R-CAUTION-004** register entry explicitly flags: *"Gao cautious-go could plausibly map to either Go-with-caution-qualifier or Delay — this ambiguity intersects with OPEN-L3-3."* Batch 2 chose the more conservative Delay mapping. Under Resolution B, "Go-with-caution-qualifier" is preserved as the presentation form that applies *if* a Go rule fires (currently none do in CAUTION).
- **EV-08 is not counted as independent evidence.** Recorded as internal synthesis of EV-02+EV-03+EV-04 in `closure-batch2.json` and `rule-candidate-register-batch2.csv`. Not disturbed by this resolution.

---

## 7. Decision matrix

Full matrix: `decision-matrix.csv`. Summary:

| Interpretation | Repo support | Alg 3/4 compat | Needs CAUTION-Go rule | Needs canonical change | Verdict |
|---|---|---|---|---|---|
| A — Normative automatic Go advisory | NONE | NO | YES (task §20 stop condition) | YES (mechanism + rule) | REJECTED |
| **B — Presentation qualifier only** | **STRONG (7 corroborating authorities)** | **YES** | **NO** | Minimal clarification only | **ACCEPTED** |
| C — Historical/stale residue | PARTIAL (predates enforcement mechanism); retention through 8 revisions is consistent with continued treatment as presentation guidance, not evidence of obsolescence — retention itself is not treated as proof of conscious reinterpretation | NEUTRAL | NO | Would require deletion | REJECTED (subsumed by B) |

---

## 8. Selected interpretation

**B — Presentation qualifier only.**

Formal semantics of the sentence: `S = CAUTION ∧ Go ∈ AI(E) → Present(Go, caution_qualifier)`.

Not: `S = CAUTION → Go ∈ AI(E)`.

---

## 9. Canonical change

**Status: PROPOSED and APPLIED under task §15 permission.**

**Old wording (line 791, verbatim):**

> When S = CAUTION, the **Go** recommendation is automatically presented by the system with a caution qualifier (e.g., "Proceed with caution"). The recommendation type remains **Go**, but its presentation and explanation are modified by the safety state. This preserves set containment while allowing state-dependent advisory messaging.

**New wording (line 791, applied 2026-09-11):**

> When S = CAUTION, any **Go** advisory generated by the active Layer 3 rule set is presented with a caution qualifier (e.g., "Proceed with caution"). The recommendation type remains **Go**, but its presentation and explanation are modified by the safety state. This preserves set containment while allowing state-dependent advisory messaging. (OPEN-L3-3 resolution, 2026-09-11 — the earlier phrasing "the Go recommendation is automatically presented by the system" was reinterpreted as presentation-layer guidance conditioned on Go ∈ AI(E); no automatic emission mechanism outside the Layer 3 rule engine is introduced.)

**Authority basis.** OPEN-L3-3 resolution task §15 permits a minimal canonical clarification when Resolution B is established and the existing sentence is genuinely misleading. The word "automatically" is what created OPEN-L3-3; removing it while preserving the presentation intent stated in the same paragraph and in `architecture-illustration.md` §202 is the minimal fix.

**Scientific effect.** None. RS_candidate(CAUTION) unchanged; no new rule; no rule removed. Go remains admissible in A_AI(CAUTION).

**Formal effect.** None. A_AI(CAUTION) = {Go, Delay} unchanged; containment unchanged; Theorem C.2 and Theorem C.3 unchanged; Algorithm 3 and Algorithm 4 unchanged; Safety Dominance holds unchanged.

**Implementation effect.** Layer 3 engine implementation is unaffected. The presentation layer must, when rendering a Go advisory produced under S = CAUTION, attach a caution qualifier ("Proceed with caution" or equivalent). No Go emission mechanism outside the rule engine is required.

---

## 10. OPEN-L3-3 status

**CLOSED — 2026-09-11 — Resolution B.**

---

## 11. Successor OPEN items

**None from OPEN-L3-3.** The evidence gap GAP-03 (no scientific rule support for CAUTION-Go) remains open as an *evidence gap*, not a blocker — Interpretation B does not require closing it (an admissible recommendation type does not need a current concrete rule).

Independent preserved OPEN items (not created or affected by this resolution):

- OPEN-L3-1C — DepartureTime derivation
- OPEN-L3-1D — Duration derivation
- OPEN-L3-2 — Predicate evaluation failure policy

---

## 12. Batch 2 status after resolution

**CLOSED.** Exact closure line:

```
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 2 CLOSED —
CAUTION-GO PRESENTATION SEMANTICS RESOLVED
```

Applied to `publications/active/journal-1/layer3-prototype-specification.md` header (line 3), `closure-batch2.json` (closure_line), and `report-batch2.md` (§10).

---

## 13. Batch 3 gating status

**Unblocked on the OPEN-L3-3 axis.** Other Batch 3 gating conditions remain in force independently:

- OPEN-L3-1C (DepartureTime) — OPEN
- OPEN-L3-1D (Duration) — OPEN
- OPEN-L3-2 (Predicate evaluation failure policy) — OPEN
- Any implementation OPEN items (OPEN-B1-1, OPEN-B1-6, etc.)

This resolution does not authorise Batch 3 engine implementation, F1–F3 fidelity runs, or E5 performance runs. Task §21 item 13 explicitly requires that Batch 3 not begin in this task.

---

## 14. Verification summary

Full check set: `verification.json` (23 checks).

**Result: 23 PASS / 0 FAIL / 0 OPEN.**

Highlights:

- appendix statement exactly traced ✅
- appendix provenance examined (git blame c42aae6c 2026-04-10) ✅
- P1–P5 propositions distinguished ✅
- A_AI(CAUTION) Go preserved ✅
- No CAUTION-Go rule invented ✅
- Algorithm 3 and Algorithm 4 compatibility checked, no post-hoc generation introduced ✅
- Cautious-go behavioural category not equated with a CAUTION-Go rule; EV-08 not counted as independent evidence ✅
- Go ≠ approval; Delay ≠ prohibition; human authority unconditional (all preserved) ✅
- OPEN-L3-1C, OPEN-L3-1D, OPEN-L3-2 preserved ✅
- F1–F3 not run; E5 not run; engine not implemented ✅

Batch 2's own tracking check `appendix_c_caution_go_tension_resolved_or_OPEN_L3_3_created` (previously OPEN) transitioned to PASS on 2026-09-11 under this resolution, giving Batch 2 its **90 PASS / 0 FAIL / 0 OPEN / 90 total**.

---

## 15. Protected canonical integrity

**Canonical files touched by this resolution:**

| File | Before hash (SHA-256) | After hash (SHA-256) | Change |
|---|---|---|---|
| `docs/canonical/appendix-c-formalisation.md` | `abee8715e842e0d9ad49edc6a2093672dd1d5dabb3d393ead1aee4e4a76e0f8c` | `c4867f48003fec806189905499bbc8d55993f3e0d312a998f552e20028499f4e` | §C.4 line 791 minimal clarification (one clause replaced, one parenthetical provenance note appended). Line count 1191 → 1192. |
| `docs/canonical/architecture-illustration.md` | `bf1e5ff8ec3621da03cfd228a9471ea8d1145861fbd34fd09a6ef70e16df81df` | `bf1e5ff8ec3621da03cfd228a9471ea8d1145861fbd34fd09a6ef70e16df81df` | **UNCHANGED** — parallel text already clear. |

All other files under `docs/canonical/` are unchanged by this task (verified against pre-task working directory).

**Batch 2 artefacts updated to reflect closure** (not canonical files, but recorded for auditability):

| File | Before hash | After hash | Change |
|---|---|---|---|
| `data/journal1-layer3-prototype/closure-batch2.json` | `54dfe5415d7ac6f56b1e11c24457aaaa697ea03c4a78914374a5905ba0c89640` | `daa64b50082ea433d7966aa9add647fc00b4ee5f94be522b47ae9ed864b64a5d` | closure_line, closure_rationale, semantic_verification_pass, OPEN_L3_3 status, workstream_status, canonical_files_touched updated |
| `data/journal1-layer3-prototype/semantic-verification-batch2.json` | `cdc96983e0cb3aaa006f02c5c969f128aa5594b2efe91196d3dda74df250947b` | `6a1992feef5e1b8d7baa72d41452b945715bfb97bf81bc21925046ef640288e3` | OPEN-L3-3 tracking check verdict OPEN → PASS; summary PASS_count 89 → 90, OPEN_count 1 → 0 |
| `data/journal1-layer3-prototype/report-batch2.md` | `b477d16abb9d5be8e98ff1f52ed9384f9543e9074088adf4528081e089e3a8a4` | `3601d0ace3e114ff37d7cdcc2fe9fe569a1ba70a224d2d8b47f18dea16a80117` | Outcome, §9 OPEN table, §10 closure line, §13 resolution paragraph updated |
| `publications/active/journal-1/layer3-prototype-specification.md` | (not hashed before — snapshotted after) | `b292e04aa884a0c5474a8db51a3165d17e8400df145de213434a6f35fce85282` | Header status line, §26 OPEN-L3-3 row, §27 semantic verification cell updated |

**Exact changed lines in `appendix-c-formalisation.md`:** line 791 replaced; parenthetical provenance note appended within the same paragraph (net +1 line at end of file after wrap).

---

## 16. Files created / modified

**Created (this resolution — `data/journal1-layer3-prototype/open-l3-3-resolution/`):**

- `authority-trace.csv` (16 rows)
- `semantic-decomposition.md`
- `decision-matrix.csv`
- `resolution.json`
- `verification.json` (23 checks, all PASS)
- `report.md` (this file)

**Modified:**

- `docs/canonical/appendix-c-formalisation.md` — §C.4 line 791 clarification (under task §15 permission)
- `publications/active/journal-1/layer3-prototype-specification.md` — status header, §26 OPEN-L3-3 row (CLOSED), §27 semantic verification cell
- `data/journal1-layer3-prototype/closure-batch2.json` — closure_line, closure_rationale, semantic_verification_pass block, OPEN_L3_3 status, workstream_status, canonical_files_touched
- `data/journal1-layer3-prototype/semantic-verification-batch2.json` — OPEN-L3-3 tracking check verdict (OPEN → PASS), summary counts
- `data/journal1-layer3-prototype/report-batch2.md` — outcome, §9 OPEN table, §10 closure line, §13 resolution paragraph

**Not modified (verified):**

- All other canonical files under `docs/canonical/`
- All other Batch 2 artefacts (rule-candidate-register-batch2.csv, rule-evidence-matrix-batch2.csv, rule-conflict-analysis-batch2.csv, scientific-gap-register-batch2.csv, recommendation-semantics-batch2.csv, change-map-batch2.csv)
- All Batch 1 artefacts
- All engine implementation (none exists yet; this task did not create any)

---

## 17. Exact closure/status line

```
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 2 CLOSED —
CAUTION-GO PRESENTATION SEMANTICS RESOLVED
```
