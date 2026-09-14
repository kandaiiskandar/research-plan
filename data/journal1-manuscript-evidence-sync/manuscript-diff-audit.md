# Batch 8A — Manuscript Diff Audit

**File:** `publications/active/journal-1/submissions/v1-initial-submission/manuscript.md`
**Before:** `51bcd6f627090f26` (905 lines) → **After:** `c1ef469e98101233` (928 lines)
**Diff:** 36 insertions, 13 deletions

Every changed paragraph is classified below. **No paragraph introduces a scientific proposition absent from `claim-evidence-matrix.csv`.**

| # | Section | Change | Classification |
|---|---|---|---|
| 1 | 5.2, Definition 5.1 table | `r` retyped from `ℝ≥0` to `ℝ≥0 × K` | terminology correction |
| 2 | 5.6.2 | "runtime fidelity is not yet demonstrated" → evaluated (F1–F3) | evidence synchronisation |
| 3 | 5.6.2 | rule-set content "remains to be implemented" → implemented and specified | evidence synchronisation |
| 4 | 5.6.3 | "supplementary design rationale (available from the authors)" → Layer 3 prototype specification | terminology correction |
| 5 | 5.7 | forward pointer separating closed evidence from undrafted sections; E5 named as open | evidence synchronisation |
| 6 | 6.5 | "Section 10 plans to evaluate implementation fidelity" → fidelity evaluated; theorem-vs-fidelity distinction stated | evidence synchronisation |
| 7 | 7.3 note | "a future implementation-fidelity test" → evaluated, zero observed violations | evidence synchronisation |
| 8 | 8 | "as when Layer 3 is not yet built" → configuration description | evidence synchronisation |
| 9 | 9 stub purpose | "planned … once implemented" → implemented, completed evaluation | evidence synchronisation |
| 10 | 9 stub content | "Planned implementation stack targets" → "Implementation stack" | terminology correction |
| 11 | 9 stub figure | E4 oscillation figures labelled PRIMARY, no RESOLUTION analogue | claim bounding |
| 12 | 11 stub instruction | "F1–F3 deferred to the Layer 3 build" → CLOSED but implementation-fidelity, belongs in §9 | claim bounding |
| 13 | 12 stub figure | E4 transition figures labelled PRIMARY with `E4_RESOLUTION = NOT_REQUIRED_BY_CURRENT_E3_DESIGN` | claim bounding |
| 14 | Abstract | UNDRAFTED marker with authoring constraints | limitation update |
| 15 | §§1–4, 9–15 (11 sections) | UNDRAFTED markers naming the evidence matrix and E5 OPEN | limitation update |

## Result insertion

**None.** Batch 8A inserted no empirical result into the manuscript. Items 11 and 13 *bound* figures that were already present in stub content; they add no new value. All closed E1/E2/E4/E6 values still awaiting a manuscript home are recorded in `claim-evidence-matrix.csv` with `required_action = DEFER to Batch 8B`.

## Flagged paragraphs

None. Two paragraphs carried a scientific proposition not previously in the matrix and were checked before retention:

- **§10 stub, C3 row** — "Structural proposition J1-P1: `A_C3(S) = A_C1(S)` for all S, proved by finite-mapping comparison and confirmed against the retrospective record." Present before Batch 8A, consistent with matrix row P4 and with `evaluation-specification.md` §4/§6. Retained unchanged; correctly separates proposition from trace confirmation.
- **§6.5** — "what the composite guarantee does not establish." Added by the earlier semantic closure repair, consistent with matrix rows P1–P3. Retained unchanged.
