# AAI 2026 — Revision Log (v3 → v4)

**Date:** 7 October 2026
**Input:** `aai-2026-manuscript-v3-evidence-corrected.docx`
**Output:** `aai-2026-manuscript-v4-final-revised.docx` / `.pdf`
**Figure:** `aai-2026-figure1-v5.png` / `-nocaption.png` / `-source.html`
**Basis:** *Focused Evidence Audit of Two Unresolved Methodological Issues* (`aai-2026-issue-A-B-evidence-audit.md`) and the *Evidence Resolution and Configuration Register*.

Every edit below was applied directly to `word/document.xml` under an assertion that the target string matched **exactly once**. No edit was applied on a fuzzy or multiple match.

---

## A. Removal of the medium-vessel variant (Issue A)

**Why.** `docs/canonical/appendix-c-formalisation.md` line 611 records the 2.8 m medium-vessel UNSAFE boundary as *"interpolated… No corpus source provides a direct medium-vessel UNSAFE threshold. This is the weakest-grounded value in the table."* Six candidate interpolation rules were tested against the corpus; they give 2.39–3.05 m and **none reproduces 2.8**. The value is exactly 2.0 × the 1.4 m onset, which is a round-number researcher choice, not a sourced or derived threshold. It therefore cannot be presented alongside the externally sourced small- and large-vessel configurations.

| # | Section | Previous content | Change | Evidence / reason |
|---|---|---|---|---|
| 1 | Abstract | "falls to 1.96% and 1.26% under medium- and large-vessel configurations" | "falls to **1.26% under a large-vessel configuration**" | Appendix C line 611; interpolation-rule test |
| 2 | §V-C (sensitivity paragraph) | "Under the medium- and large-vessel threshold configurations the PRIMARY value falls to 1.96% and 1.26% respectively, and to 0.66% and 0.37% in RESOLUTION." | "Under the **large-vessel** threshold configuration the PRIMARY value falls to **1.26%**, and to **0.37%** in RESOLUTION." | as above |
| 3 | §V-C (RQ1 answer) | "falls to 1.96% and 1.26% for the medium and large vessel classes" | "falls to **1.26% for the large-vessel class**" | as above |
| 4 | §VI Conclusion | "falling to 1.96% and 1.26% for larger vessel classes" | "falling to **1.26% for the large-vessel class**" | as above |
| 5 | §VI Conclusion | "the vessel-class **variants are** configuration checks" | "the vessel-class **variant is a** configuration check" | grammatical agreement after removal |
| 6 | Figure 1, stage 6 | "Vessel class analysis: Small vessels (baseline) / **Medium vessels** / Large vessels" | "Small vessels (baseline) / Large vessels" | figure must not assert a variant the text no longer reports |

**Retained.** The large-vessel configuration is kept. Its boundaries trace to sourced values (Appendix C line 607: the 1.0 m SAFE/CAUTION boundary is Jeong & Im's own proposed restriction for vessels ≤ 10 m LOA, their Table 12; the 1.25 m CAUTION/UNSAFE boundary is Yaakob et al.'s operational ceiling). The small-vessel baseline is unchanged.

---

## B. Reporting the RESOLUTION decomposition (Issue B)

**Why.** The audit traced the withheld cells to `docs/analysis/canonical-revision-report.md` line 178: *"41.08% / 45.56% remain withheld pending a provenance row."* "Provenance incomplete" meant a **missing register row**, not a defective or unreproducible computation. Re-executing `scripts/condition_comparison.py` with raw-count instrumentation returned 2,438 and 2,704 hours of 5,935 — a difference of **266** — and two independent runs were byte-identical. A direct C1↔C2 comparison returns the same 266, so the decomposition is internally consistent. The register row now exists, so the reason for withholding no longer holds.

| # | Section | Previous content | Change | Evidence / reason |
|---|---|---|---|---|
| 7 | §V-A | "The RESOLUTION pairwise components are not reported because their provenance is incomplete; Δ_L2 is unaffected." | "The RESOLUTION decomposition gives **C0↔C1 = 41.08% and C0↔C2 = 45.56%**, a difference of **266 of the 5,935 evaluated hours**." | re-execution with raw counts; two byte-identical runs; direct C1↔C2 cross-check returns 266 |
| 8 | Results table, RESOLUTION column | `---` in the C0↔C1 and C0↔C2 rows | **41.08%** and **45.56%** | as above |
| 9 | Results table note | "— indicates pairwise resolution components withheld because provenance is incomplete; Δ_L2 is unaffected." | sentence removed | the condition it described no longer obtains |

**Unchanged.** The PRIMARY decomposition (42.88% / 48.69%) is untouched. It remains exact: the audit's raw-count re-execution gave 4,448 − 3,917 = **531 hours**, matching the CAUTION-hour count §V-B reports (the manuscript states the percentages and the 531, not the two intermediate counts). Δ_L2 itself, the identity Δ_L2 ≡ P(S = CAUTION), and the C1↔C3 = 0.00% conformance check are untouched.

---

## C. Configuration-count precision

| # | Section | Previous content | Change | Evidence / reason |
|---|---|---|---|---|
| 10 | §IV | "the canonical sensitivity script evaluates 56 distinct combinations" | "…evaluates 56 distinct combinations, **of which this paper reports a subset**," | Instrumented execution of `scripts/sensitivity/threshold_sensitivity.py` gives **78 executions / 56 unique configurations**. The manuscript reports fewer than 56; the clause prevents the reader inferring that all 56 appear in the paper. |

---

## D. Defect found during verification

| # | Section | Previous content | Change | Evidence / reason |
|---|---|---|---|---|
| 11 | Reference [10] | "in Proc. IECON 2024 `---` 50th Annu. Conf." | "in Proc. IECON 2024 **—** 50th Annu. Conf." | Caught by the post-edit consistency sweep (18/19 pass, this the single FAIL). A literal triple-hyphen, not an em dash. Pre-existing in v3. |

---

## E. Figure 1 re-embedding

The figure embedded in v3 still showed "Medium vessels". It was replaced with the corrected v5 render.

| Property | v3 embed | v4 embed |
|---|---|---|
| Pixel size | 1983 × 738 | **3000 × 774** |
| Effective resolution at 7.0 in width | 283 dpi | **≈ 429 dpi** |
| `wp:extent` / `a:ext` | `cx=6400800 cy=2381250` | `cx=6400800` **`cy=1650714`** |
| Aspect ratio | 0.3721 | **0.2579** (matches the render exactly) |

Both extent elements were updated so the image is not stretched. The caption-free render was used, because the Word document supplies its own IEEE caption.

---

## Nothing else changed

No threshold, no governance contract, no comparator definition, no Δ_L2 value, no record or hour count, no citation, no section ordering, no claim of generality. The PRIMARY results, the deterministic-census framing, the declared exclusion D = {m}, the lower-bound language and the ranges 5.67–9.56% (PRIMARY) stand as written.
