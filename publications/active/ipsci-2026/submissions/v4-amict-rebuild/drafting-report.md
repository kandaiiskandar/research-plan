# Drafting Report — AMICT Conference Manuscript V4

> **Superseded in part.** Two statements in this report were corrected by the post-draft scientific and reviewer audit of 2026-09-14 (`post-draft-audit.md`): the double-blind check in §9 and the site-disclosure note in §9. Word counts in §2 and §3 predate the audit's twelve surgical corrections; current counts are in `post-draft-audit.md` §16.

**Date:** 2026-09-14
**Task:** `docs/tasks/AMICT CONFERENCE MANUSCRIPT V4 — EVIDENCE-LED SIX-PAGE DRAFT.md`
**Manuscript:** `publications/active/ipsci-2026/submissions/v4-amict-rebuild/manuscript.md`
**Title:** Evaluating Graduated Advisory-Scope Governance for AI Decision Support

---

## 1. Status

    MANUSCRIPT_V4_DRAFT   = COMPLETE
    RQ_COUNT              = 3
    HEADLINE_CONTRIBUTIONS = 2
    RESULTS_SECTION_LARGEST = YES
    REFERENCE_COUNT       = 20
    VISUAL_COUNT          = 3
    ARCHITECTURE_FIGURE   = OMITTED_FOR_SPACE
    DOUBLE_BLIND_CHECK    = PASS
    PROTECTED_DISCLOSURES = PASS (19/19)
    SIX_PAGE_FIT          = WORD_BUDGET_PROXY_ONLY
    PROVENANCE_OPEN_ITEMS = 1
    MANUSCRIPT_V3_UNTOUCHED = YES

No stop condition fired.

---

## 2. Word counts

| Section | Words | Target | Δ |
|---|---|---|---|
| I. Introduction | 408 | 420 | −12 |
| II. Related Work | 287 | 450 | −163 (table-led) |
| III. Operational Governance Formalisation | 738 | 750 ceiling | −12 |
| IV. Evaluation Method | 525 | 550 | −25 |
| V. Results | **858** | 900 | −42 |
| VI. Discussion and Limitations | 696 | 600 | +96 |
| VII. Conclusion | 192 | 160 | +32 |
| **Body total** | **3,704** | ~3,830 | **−126** |
| Abstract | 198 | 170–200 | within |
| References | 540 | — | 20 entries |

Counts exclude headings and table cell text.

**`RESULTS_SECTION_LARGEST = YES`.** Results (858) exceeds Formalisation (738) by 120 words. Section V was drafted and locked before Section III, per the binding drafting order.

Section VI is 96 words over its target. The overrun is entirely in the protected disclosure block, which §27 forbids cutting to meet word count. It is offset by Related Work coming in 163 under, since the comparison table carries content that would otherwise be prose.

---

## 3. Six-page position

| Component | Words |
|---|---|
| Front matter (title, abstract, keywords) | ~225 |
| Body prose | 3,704 |
| Table cell text (3 tables) | ~342 |
| References (20 entries) | 540 |
| **Total column-space equivalent** | **~4,811** |

| Density assumption | 6-page envelope | Position |
|---|---|---|
| 1,000 words/page | 6,000 | fits, ~1,189 slack |
| 900 words/page | 5,400 | fits, ~589 slack |
| 850 words/page | 5,100 | fits, ~289 slack |

**Caveat.** Rendered table area exceeds cell-text word count — a two-column table occupies roughly 1.5–2× its cell text in column space. At a 2× allowance the total rises to ~5,153, which still fits at 900 words/page and above but becomes marginal at 850.

    SIX_PAGE_FIT = WORD_BUDGET_PROXY_ONLY

The draft is designed to the historical six-page envelope using word-equivalent estimates. **Final pagination requires the current official AMICT template**, which is not present in the repository. No page-count claim is made.

The position is more comfortable than the readiness projection because the reference list came in at 20 entries / 540 words rather than the ~25 / 750 planned, and the tables are more compact than estimated.

---

## 4. Visuals

| # | Visual | Location | Role |
|---|---|---|---|
| TABLE I | Closest prior mechanism families (7 rows × 6 columns) | II. Related Work | Carries the precedent comparison in place of prose |
| TABLE II | Observation conditions and their governance treatment (4 rows × 4 columns) | III. Formalisation | Carries the observation-resolution and exclusion semantics |
| TABLE III | Admissible-set divergence summary (4 rows × 4 columns) | V. Results | Carries the empirical results |

**Figures: 0.** `ARCHITECTURE_FIGURE = OMITTED_FOR_SPACE`, per the execution decision. Restore for the journal manuscript.

---

## 5. Question and contribution locations

| Item | Location |
|---|---|
| RQ1 stated | I. Introduction |
| RQ1 answered | III. Operational Governance Formalisation (A–C specification; D bounded executable conformance) |
| RQ2 stated | I. Introduction |
| RQ2 answered | V. Results §A (Δ_L2) and §B (intermediate-state control) |
| RQ3 stated | I. Introduction |
| RQ3 answered | V. Results §C |
| C1 stated | I. Introduction (contributions paragraph); delivered in III |
| C2 stated | I. Introduction (contributions paragraph); delivered in IV and V |
| Implementation fidelity | III §D — supporting verification for RQ1, not a contribution |

All three RQs appear **verbatim** as frozen. Verified by exact string match.

---

## 6. Canonical text reuse

| Item | Occurrences | Locations |
|---|---|---|
| Gap statement (verbatim) | **1** | I. Introduction |
| Novelty-positioning sentence (verbatim) | **3** | I. Introduction · II. Related Work (closing/contribution-positioning paragraph) · VI. Discussion (opening) |

Both verified by normalised exact string match. No variant phrasings exist in the manuscript.

---

## 7. Protected disclosures — 19/19 present

| # | Disclosure | Location |
|---|---|---|
| 1 | Permissive-state requirement deferred | III §D; VI Limitations |
| 2 | SAFE rule set empty | III §D |
| 3 | Delay-only generated conclusion type | III §D; VI Limitations |
| 4 | 454 advisory **records**, not types | III §D |
| 5 | Containment exercised on restrictive side only | III §D; VI Limitations |
| 6 | Marine-warning component declared as exclusion | IV §D |
| 7 | Severity results are lower bounds | IV §D; V opening; VI Limitations |
| 8 | Storm-code input zero throughout the record | IV §D; V §D |
| 9 | Rainfall figures lower-bound constrained | IV §D; V §D |
| 10 | Wind: 2 activations in 43,848 hours, 0 bindings | V §D |
| 11 | Freshness parameter specified but unparameterised | VI Limitations |
| 12 | Provenance-capture runtime unimplemented | VI Limitations |
| 13 | Cross-domain re-instantiation not demonstrated | VI Generalisation boundary |
| 14 | Primary/resolution are alternative configurations, not uncertainty bounds | IV §C; V §C; VI Limitations |
| 15 | C1↔C3 interpretation bounded to evaluated comparators | V §B; VI |
| 16 | Avionics precedent acknowledged | Abstract; I; II; V; VI; VII |
| 17 | 72-paper review distinguished from targeted post-review additions | II opening |
| 18 | Performance and acceptance threshold open | VI Limitations |
| 19 | No human study; no human-outcome validation | VI What the results do not establish; VI Limitations |

No disclosure was removed or weakened for space.

---

## 8. Self-audit — prohibited phrases

Full-text scan with context inspection of every hit.

**Absent entirely:** first-ever · unprecedented · globally novel · uniquely novel · unique · no existing architecture · no prior · domain-independent · safer · safety improvement · risk reduction · real-world validation · 454 advisory types · 5.81 ± 4.48 · preserved · replicated · validated · proven · **AC 20-151A** · **Cleveland**.

**Present, inspected, retained as legitimate:**

| Term | Occurrences | Context |
|---|---|---|
| effectiveness | 1 | Conclusion — inside the negation "do not establish safety, effectiveness or decision-quality outcomes". A disclosure, not a claim |
| first | 3 | "The first is a structured review…" (enumerating two literature populations); "Three conclusions follow. First," (enumerative); "robustness-first architecture" (reference title) |
| robust | 3 | Related Work table cell describing Baxi's *robustness audit* as the conditioning variable of prior work; two reference titles |
| novel | 1 | Build comment only, naming the file `novelty-audit-report.md`. Not manuscript prose |

**Provenance check:** `41.08` and `45.56` are **absent**. `RESOLUTION_PAIRWISE_C0_C1_C0_C2 = PROVENANCE_INCOMPLETE` is respected; TABLE III marks those cells "not reported".

---

## 9. Double-blind check

    DOUBLE_BLIND_CHECK = PASS

No author names, initials, affiliations, institutional identifiers or email addresses appear. No acknowledgements section. The only match for "acknowledg" is inside the build comment, which states that no identifying acknowledgements appear.

First-person use is minimal — one instance, "we did not identify", inside the frozen gap statement.

**Correction (post-draft audit, 2026-09-14).** This scan was insufficient. It searched for names, affiliations, emails and acknowledgements, and did **not** search for self-referential pointers to the authors' own unpublished work — a standard blind-review leak. The sentence "Proofs are given in the companion journal treatment" passed this scan and should not have. It was identified as PC4 by the post-draft audit and has been corrected; see `post-draft-audit.md` §4 and §13.

**Two notes for the author before submission.** The build comment block at the head of the file references internal repository paths; it should be stripped at format time.

**Correction (post-draft audit, 2026-09-14).** This report originally described giving the site as coordinates without the city name as "more conservative than v3". That was wrong. The coordinates identify the site, so omitting the city masks nothing and created a false impression of anonymisation. The manuscript now reads "a coastal site in Sabah, Malaysia (5.98° N, 116.01° E)", and the record is `SITE_DISCLOSURE = REPRODUCIBILITY_CHOICE_NOT_ANONYMISATION`.

---

## 10. Reference list

**20 entries**, rebuilt around the new structure rather than inherited. v3 carried 40.

**Retained and load-bearing (new to this manuscript):** [10] FAA AC 20-151C · [11] Cleaveland, Mitsch & Platzer (2023) · [12] Parasuraman, Sheridan & Wickens (2000) · [13] Bernabei & Costantino (2024) · [14] Kwon & Kim (2026) · [15] FDA CDS guidance (2026). All six are registered in `docs/canonical/citation-notes-map.md` and resolve to validated notes.

**Retained from v3:** [1] Indykov · [2] Shamsujjoha · [3] Dalrymple · [4] Flehmig · [5] Könighofer · [6] Ghaleb · [7] Baxi · [8] Kang · [9] NIST AI RMF · [16] NOAA · [17] USNO · [18] IMO COLREGs · [19] Yaakob · [20] Jeong & Im.

**Dropped (20)** — all tied solely to deleted v3 literature-review subsections or to claims no surviving sentence makes: Yamin; Dominguez-Péry; Atacan & Düzbastılar; Wen; Bajcsy & Fisac; Ramos; Feng; Vermaelen (Tumato); Haque; Rahim; Katende; Longobardi; Bhuvaneswari; Bloomfield & Rushby; Perez-Cerrolaza; Sahoo; Kamath; Wu; Cash; Reuel; Engin & Hand; Mussi; Wang (Pro2Guard); Kolt; Gao; Belle.

No reference supporting a surviving scientific claim was dropped to meet the target. **Kang [8] is cited once, in the Related Work table row for graduated runtime governance, and is not load-bearing.** AC 20-151A is not cited; AC 20-151C is. The spelling is Cleaveland.

---

## 11. Stale v3 text — confirmed absent

None of the following survived into V4: "being developed as a prototype" · "prototype fidelity has not yet been verified" · "the reasoning engine is specified but not implemented" · any unscoped claim that no architecture restricts advisory scope as a function of state · any claim that the mechanism is new · decision-support utility offered as an evaluated secondary metric · domain-independent applicability · any claim that human outcomes were validated.

**The old review-based headline contribution is withdrawn.** V4 states exactly two contributions. The 72-paper review appears in Related Work as positioning and background.

---

## 12. Deviations from the frozen narrative

Three, all minor and none scientific.

1. **Related Work came in at 287 words against a 450 target.** The comparison table absorbed the content the prose would have carried. No required element is missing; the three synthesis conclusions and the two-population distinction are all present.
2. **Discussion is 96 words over target**, entirely within the protected disclosure block. Offset by Related Work.
3. **The reference list is 20 entries against a ~25 target.** Pruning followed §12's order strictly; no reference supporting a surviving claim was cut. The lower count improves the page position.

Body total is 126 words **under** the drafting target, so all three are absorbed.

---

## 13. Changed files

**Created:**

- `publications/active/ipsci-2026/submissions/v4-amict-rebuild/manuscript.md`
- `publications/active/ipsci-2026/submissions/v4-amict-rebuild/drafting-report.md` (this file)

**Untouched:** `v3-revision/manuscript-v3.md` (MD5 `1e80cb17dc197ed98bc737eccc203d21`, 634 lines — verified identical) · all other submission versions · all eight AMICT evidence artefacts · all empirical artefacts and scripts · `notes/` and `citation-notes-map.md` · all CLOSED Journal 1 workstreams.

No `.docx`, `.pdf` or `.tex` created. No experiment run. No empirical result recomputed. No architecture, threshold or comparator definition changed. The provenance gap was not repaired.

---

## 14. Remaining items

| Item | Status |
|---|---|
| `RESOLUTION_PAIRWISE_C0_C1_C0_C2` | `PROVENANCE_INCOMPLETE` — unused by the manuscript; downstream repair item |
| AMICT template | Absent. Required before any pagination claim or format conversion |
| Current-cycle page limit | Unconfirmed; six pages assumed from the 2026-07 record |
| Build comment block | Strip at format time |
| Study-site disclosure level | Coordinates only; confirm intended |

No blocker to closure.
