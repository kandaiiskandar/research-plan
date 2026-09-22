# Canonical Revision Report

**Date:** 2026-09-21
**Authority:** `docs/analysis/final-research-chain-lock.md`
**Type:** Controlled consistency revision. No new research, literature search, experiment or computation.

---

## Document classification (established before editing)

| Category | Documents |
|---|---|
| **ACTIVE CANONICAL — edited** | `docs/analysis/experiment-report-delta-l2.md`; `docs/canonical/empirical-findings-2026-09-06.md`; `publications/active/journal-1/evaluation-specification.md`; `CLAUDE.md` |
| **ACTIVE SUPPORTING — edited for consistency** | `docs/canonical/discussion-notes-governance-gap-precedents-and-formal-foundations.md`; `docs/chapters/chapter-2-literature-review/v1-initial-draft.md`; `docs/analysis/open-issues-log.md` |
| **HISTORICAL / SESSION RECORD — annotated only** | `docs/canonical/session-log-2026-09-06.md`; `docs/canonical/session-log-2026-09-08.md` |
| **SUBMITTED / ARCHIVED — not edited** | `publications/active/journal-1/submissions/v1-initial-submission/manuscript.md`; `publications/active/ipsci-2026/submissions/**` |

---

## A. Files modified

| File | What changed | Why | Locked section |
|---|---|---|---|
| `docs/analysis/experiment-report-delta-l2.md` | **Full restructure** to Problem → Prior Work → Gap A/B → RQ1–RQ3 → Architecture → Formal Properties → Evaluation → Sensitivity → Results → Contribution → Limitations. Corrections integrated into the argument, not appended | Report was built on the superseded framing | §C, §D, §E, §F, §G, §H, §I, §J, §K, §L, §M, §N, §O, §P, §T |
| `CLAUDE.md` :13 | Core contribution reframed from *"novel intermediate CAUTION mode … which no existing architecture implements"* to an operational composition, with an explicit "mechanisms are conceded" block | Direct contradiction with the frozen literature position | §A, §F, §U-1 |
| `CLAUDE.md` :59 | Gap layer 1 rewritten concession-first; Gap A + Gap B installed | Absolute novelty claim no longer defensible | §C, §D, §U-2 |
| `CLAUDE.md` :51, :53 | RQ5 struck through and re-designated future socio-technical validation | No fisher study conducted | §E, §U-9 |
| `docs/canonical/discussion-notes-governance-gap…` :218 | *"no existing architecture formally restricts AI advisory scope…"* marked superseded with the replacement framing inline | Same claim class | §C, §U-3 |
| `docs/chapters/chapter-2-literature-review/v1-initial-draft.md` §67 | Two absolute claims bounded to the AI decision-support literature, with TSO-C151c §5.6 named as the counterexample | Contradicted by primary-source verification | §A, §U-4 |
| `docs/canonical/empirical-findings-2026-09-06.md` §0a | Correction block installed with the 1.97 / −0.64 / 1.33 decomposition; body sentence reworded to "net spread" | The 1.33-point attribution was wrong in magnitude | §L, §U-5 |
| `publications/active/journal-1/evaluation-specification.md` | 12 edits: RQ-J2 row removed; revision banner with thesis-RQ mapping; RQ-J4 merged into RQ-J3; `E5_ANDROID_TARGET_BENCHMARK` re-designated `DEFERRED_NOT_REQUIRED_FOR_CONTRIBUTION`; §11 status → DEFERRED; OPEN-1 closed by removal; OPEN-5 blocks nothing; metric table and final matrix reconciled | RQ-J2 removed from the active set | §E, §S, §U-8 |
| `docs/canonical/session-log-2026-09-06.md` :209 | **Annotation only** — "1.7-point spread is the grid-resolution sensitivity" marked superseded, original text retained | Historical integrity | §S, task §20 |
| `docs/analysis/open-issues-log.md` | ISSUE-1 → **RESOLVED**, with original concern, method and decomposition preserved | Common-period comparison performed | §L, task §13 |

**New status vocabulary introduced:** `DEFERRED_NOT_REQUIRED_FOR_CONTRIBUTION`, formed on the existing `NOT_REQUIRED_BY_CURRENT_E3_DESIGN` pattern.

---

## B. Files intentionally not modified

| File | Reason |
|---|---|
| `publications/active/journal-1/submissions/v1-initial-submission/manuscript.md` :1136 | Submitted artefact. Carries *"the gap between them is the grid-resolution sensitivity"*. **To be superseded in the next revision, not edited** |
| `publications/active/ipsci-2026/submissions/**` | Submitted/archived versions |
| `docs/canonical/session-log-2026-09-08.md` | Historical record; contains no contradiction requiring annotation |
| `docs/canonical/appendix-c-formalisation.md` | Formal definitions unchanged by this revision; §N reclassifies their *status*, not their content |
| `data/prediction-register.csv` | Prediction state authority. No prediction was re-resolved |
| `scripts/**` | No implementation change. `scripts/sensitivity/threshold_sensitivity.py` was added in the prior task |
| `docs/canonical/traceability-table.md` :38 | Reviewed: references contextual validation as an *objective* (O5), not as completed work. Consistent with RQ5-as-future-work |
| `docs/canonical/report-journal1-canonical-consistency-sync…` :197, `evaluation-baseline-decision.md` :159 | **Already correct.** Both already state `{Go, Delay}` is not epistemically warranted or optimal, and that no safety-outcome claim is supported. Retained as source wording |

---

## C. Architecture-novelty corrections

Four claims removed or bounded. None replaced with a different absolute claim; each replacement concedes the prior mechanism first and then states the bounded composition gap.

1. `CLAUDE.md` :13 — *"novel intermediate CAUTION mode … which no existing architecture implements"*
2. `CLAUDE.md` :59 — *"no existing architecture restricts AI advisory scope…"*
3. `discussion-notes…` :218 — *"no existing architecture formally restricts AI advisory scope…"*
4. Chapter 2 §67 — *"no existing architecture defines intermediate operating modes"* and *"absent from every safety architecture reviewed"*

The replacement framing in every case: **an operational architecture and specification that composes established safety-governance mechanisms for a low-resource environmental decision-support setting**, with FAA TSO-C151c §5.6 named as the human-facing advisory-inhibition precedent.

---

## D. RQ changes

| Change | Detail |
|---|---|
| **Installed** | RQ1 operational specification · RQ2 empirical characterisation and robustness · RQ3 structural warrant of the multi-component classifier |
| **Removed** | RQ-J2 (target-hardware latency) — re-designated deferred deployment evaluation, explicitly **not** an evaluation limitation |
| **Merged** | RQ-J4 → RQ-J3; RQ-J3 → thesis RQ2 and RQ3 |
| **Demoted** | RQ-J1 (Safety Dominance) → supporting formal property |
| **Re-designated** | Thesis RQ5 (fisher validation) → future socio-technical validation, struck through in situ with a note that no study has been conducted |
| **Cross-references** | Evaluation specification banner carries the Journal-RQ → thesis-RQ mapping so old numbering remains traceable |

---

## E. Empirical corrections

| Correction | Before | After |
|---|---|---|
| PRIMARY/RESOLUTION spread | "the 1.3-point gap IS the grid-resolution sensitivity" | 1.97 pts resolution effect (period held constant) − 0.64 pts record-length effect (model held constant) = 1.33 pts net; effects in opposite directions |
| Headline presentation | 5.81% standing alone | 5.81% / 4.48% **with** the sourced-threshold envelope 5.67–9.56%, described as *sensitive but still informative* |
| Δ_L2 semantics | Implicitly a governance-difference rate | Explicit identity **Δ_L2 = P(S = CAUTION)**, verified from the implementation, placed at §7.3 immediately before the results — not in limitations |

---

## F. New sensitivity and attribution material

Installed in report §8, integrated ahead of the results rather than appended:

- **Wind** — structural zero for the evaluated site and trace (Δ_L2 unchanged across `W_C` 18–25 kn; two observations within ±2 kn of the boundary)
- **Rainfall** — minimal, 0.48 points across a fourfold variation; the **non-MET lower boundary is explicitly stated not to be driving the headline**
- **Wave** — dominant; `O_C` ≈ **−1.4 percentage points per 0.05 m**, labelled descriptive influence, **not causal**
- **Component attribution** — `g_o` 518/531 = 97.6%; `g_r` 13/531 = 2.4%; `g_w`, `g_t`, `g_m` zero binding; zero ties
- **Negative finding stated** — the five-component state remains defensible as a transferable specification, but the evaluated record does not empirically warrant equal importance of all five components at this site
- **Scope note preserved** — F-7 (binding across all states, `g_t` dominating non-SAFE) and the attribution table (CAUTION-specific, departure window) are correct at their own scopes; neither is presented as correcting the other

---

## G. Limitation changes

Nine limitations installed in report §11, led by the two that most threaten the headline:

1. **Δ_L2 invariant to `A_AI(CAUTION)` content** — no evidence that `{Go, Delay}` is appropriate
2. Wave-threshold dependence — 2.54%–14.75% under ±0.25 m
3. **Vessel-class specificity** — 1.96% medium, 1.26% large; approaching vacuity for larger classes
4. **Time policy** — `night ⇒ UNSAFE` is a conservative architectural policy, not a physical or legal determination; daylight-only denominator gives 9.59% / 7.40%
5. Characterisation, not validation · 6. Lower bounds · 7. Admissible-set level only · 8. Descriptive, not inferential · 9. Evidential provenance

`{Go, Delay}` wording uses the corrected position: **researcher-defined with a domain rationale** from Gao (2024) and Rahim et al. (2024), immediately followed by the statement that this is not empirical validation, optimality evidence, or evidence of improved safety.

A **"What this work does not establish"** block installed with all fourteen non-claims from lock §P.

---

## H. Contribution changes

Hierarchy installed unchanged from lock §O: **primary** empirical characterisation (including robustness envelope, attribution, common-period comparison and negative results); **secondary** domain operationalisation; **secondary** operational specification separating `G(S)` from `A_AI(S)`; **supporting** formal contract-conformance; **supporting** reproducibility and provenance methodology.

Formal properties repositioned per lock §N — totality as formalisation of an established mechanism, containment as a design property, Safety Dominance as contract conformance, C1 ≡ C3 as a structural proof. None presented as new theory.

---

## I. Historical records preserved

- `session-log-2026-09-06.md` — original 1.7-point claim retained verbatim, annotated as superseded with a pointer to the corrected section
- `empirical-findings-2026-09-06.md` §0a — the superseded sentence is **quoted inside** the correction block, so the change in interpretation is legible
- Evaluation specification — the RQ-J2 rationale sentence retained as the record of the intermediate rewording step before removal
- OPEN-1 and RQ5 struck through rather than deleted
- ISSUE-1 retains original concern, resolution method and decomposition
- Submitted manuscripts untouched

---

## J. Post-revision contradiction audit

Searched the active tree (`docs/canonical`, `docs/chapters/chapter-2-literature-review`, active journal-1 documents, `CLAUDE.md`), inspecting context rather than raw matches.

| Phrase | Result |
|---|---|
| `novel intermediate` | **Clean** — no active occurrence |
| `no existing architecture` | **Clean** — no active occurrence |
| `absent from every` | **Clean** — no active occurrence |
| `IS the grid-resolution` | One occurrence, **inside the correction block quoting the superseded wording** — correct |
| `RQ-J2` | Six occurrences, **all in supersession or mapping notes** — correct |
| `DEFERRED_MANDATORY` | One occurrence, in the re-designation note recording the former value — correct |
| `RQ5` | Struck through at :51, re-designated at :53; remaining occurrences are references to the future-work study design — correct |
| `Go, Delay` | All active occurrences state it is **not** validated or optimal, or describe the mapping neutrally — correct |
| `5.81` / `1.33` / `1.97` / `97.6` | Every occurrence carries denominator and interpretation |
| `Safety Dominance` | Labelled contract-conformance property wherever its status is stated |
| `novel` | Remaining uses are unrelated (e.g. describing other authors' contributions) — legitimate |

### Final consistency tests

| # | Test | Result |
|---|---|---|
| 1 | Every active RQ has evidence | **PASS** — report §4 → §6, §8, §9 |
| 2 | Every contribution maps to an RQ or design objective | **PASS** — §10 |
| 3 | Every headline number has denominator and interpretation | **PASS** — §7.1, §8, §9 |
| 4 | 5.81% never described as safety effectiveness | **PASS** |
| 5 | `{Go, Delay}` never described as validated or optimal | **PASS** |
| 6 | Architecture mechanism novelty not claimed | **PASS** |
| 7 | 1.33 points not described as pure resolution sensitivity | **PASS** |
| 8 | RQ-J2 not active | **PASS** |
| 9 | Fisher validation not presented as completed | **PASS** |
| 10 | Historical/submitted documents intact | **PASS** |

---

## K. Remaining open items

| Item | Status |
|---|---|
| Journal-1 v1 submitted manuscript :1136 carries the old resolution attribution | **By design** — supersede in the next revision; do not edit the submitted artefact |
| `RESOLUTION_PAIRWISE_C0_C1_C0_C2 = PROVENANCE_INCOMPLETE` | Unchanged. 41.08% / 45.56% remain withheld pending a provenance row |
| Exclusion sensitivity `D ∈ {{m}, {m,r}, {m,o}}` | **STRENGTHENING**, not required. Do not run `D = {m,w}` — `g_w` binds never |
| Advisory-content ablation | **FUTURE WORK** — ill-posed under the current metric; requires Layer 3 in the loop and a defined outcome measure |
| `ageᵢ` freshness parameter (OPEN-B1-1) | Remains OPEN and should not be invented |
| Thesis chapters 1, 3–7 | Not yet drafted; must be written to the locked framing |

---

## L. Final status

> # **CANONICAL REVISION COMPLETE — CONSISTENT WITH FINAL RESEARCH CHAIN**

Ten files were modified, eight left intentionally untouched, and all ten consistency tests pass. Every one of the nine contradictions identified in lock §U has been addressed at the file and line named there: four architecture-novelty claims removed or bounded with the prior mechanism conceded first, three grid-resolution attributions corrected or annotated, RQ-J2 removed across the evaluation specification with a new status marker formed on the repository's existing vocabulary, and RQ5 re-designated without implying work that was not done.

The canonical report was restructured rather than patched. The Δ_L2 identity now sits in §7.3, immediately before the results, so a reader meets the constraint on interpretation before meeting the number rather than discovering it in the limitations. Sensitivity and component attribution are integrated at §8 ahead of §9, which means the headline appears with its envelope and its dominant parameter already established. The two limitations most likely to be raised — invariance to the content of `A_AI(CAUTION)`, and dependence on the wave CAUTION onset — lead §11 rather than closing it.

Historical integrity is preserved throughout. Superseded wording is quoted inside its correction block, struck through, or annotated in place; nothing was silently rewritten, and no submitted artefact was touched. The record of how the interpretation changed — from an architecture-novelty claim, through primary-source falsification, to a composition and characterisation contribution — remains legible in the documents themselves.
