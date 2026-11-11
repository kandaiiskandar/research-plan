# AAI 2026 — A4 Layout Assessment of Manuscript v8

**Manuscript:** `[Rewrite V2] conference-template-letter.docx`, SHA-256 `a29a0c27bf5b631c36ecbbaa92ecd7e7cc6cf2acabf95ef4d79c628804f41f97`
**Date:** 9 October 2026
**Mode:** read-only on the manuscript. The original file was **not modified**. Three page-geometry variants were built as separate copies in a scratch directory, with only `w:pgSz` and `w:pgMar` rewritten — no text, table, figure, reference or numerical value altered. Rendering via LibreOffice 24.2; page counts from `pdfinfo`, not estimated.

---

## 1. The headline result

> **v8 on A4 renders at 6 pages with no content change. The paper is already compliant once the page size is corrected.**

| Variant | Geometry | Side margins | Content width | **Pages** |
|---|---|---|---|---|
| **As submitted** | 612 × 792 pt (US Letter) | 45.35 pt | 183.9 mm | **7** ❌ |
| **A4, v8's own margins** | 595.3 × 841.9 pt (A4) | 45.35 pt | 178.0 mm | **6** ✅ |
| **A4, IEEE two-column width** | 595.3 × 841.9 pt (A4) | 39.70 pt | **182.0 mm** | **6** ✅ |
| **A4, v4's margins** | 595.3 × 841.9 pt (A4) | 72.00 pt (1 in) | 159.2 mm | **8** ❌ |

**This corrects the central assumption of the 24-edit plan.** §3 of that plan described the 560-word compression as "mandatory" and treated the page overflow as something prose had to fix. It does not: the overflow is entirely a template regression. **Compression is required only to pay for the additions, not for compliance.**

**Recommended target geometry: A4 at 39.70 pt side margins**, which yields the IEEE two-column text width of 182.0 mm. It renders at 6 pages and gives 3.3% more usable width than v8's own margins carried over.

---

## 2. Exact page count, including references

| | As submitted (Letter) | **A4, IEEE width (recommended)** |
|---|---|---|
| Total pages | **7** | **6** |
| Pages carrying body text | 1–6 | 1–6 |
| Pages carrying references | **6–7** | **6 only** |
| References included in the count | yes — the venue requires it | yes |

References occupy roughly the lower half of page 6 in the A4 render and run to the final line of the right column. **The document ends at the bottom of page 6 with no measurable headroom.**

---

## 3. Comparison with the previously verified v4 layout

`aai-2026-v4-final-verification-report.md:14–18` records v4 at 595.304 × 841.89 pt (A4), two columns, with a PASS on the 6-page limit. Two things follow that the 24-edit plan did not account for.

**(a) v4's geometry is not the geometry to copy.** v4 uses **1-inch margins on all four sides**, giving a 159.2 mm content width — roughly 12.5% narrower than the IEEE two-column standard. Applying it to v8's content gives **8 pages**. The phase-9 audit verified v4's page *size*, page *count* and column count; it did not establish that v4's margins match the IEEE conference template, and they do not.

**(b) The v4 comparison conflates content with geometry.** v4 and v8 are different manuscript versions — v8 is the v6/v7 rewrite line. v4's 6-page PASS is therefore evidence that A4 compliance is *achievable*, not a measurement of v8. The measurement above supplies that directly.

| | v4 (verified) | v8 (measured here) |
|---|---|---|
| Page size | A4 | Letter as submitted; A4 achievable |
| Side margins | 72 pt (1 in) | 44.65–45.35 pt, two values across 9 `sectPr` blocks |
| Content width | 159.2 mm | 183.9 mm as submitted |
| `sectPr` blocks | 4 | **9** |
| Pages | 6 (PASS) | 7 as submitted; **6 on A4** |

Minor housekeeping: v8's nine section blocks carry **two different side-margin values** (44.65 pt and 45.35 pt). Harmless at Letter, but the A4 conversion should set one value uniformly.

---

## 4. Where the page pressure sits

Characters of extracted text per page, A4 at IEEE width:

| Page | Chars | Floats | Content | Fill |
|---|---|---|---|---|
| 1 | 5,326 | — | title block, authors, abstract, keywords, §I start | moderate — the title/author block is fixed cost |
| **2** | **7,083** | Fig. 1 begins | §I end, §II | **fullest text page** |
| 3 | **4,337** | **Table I + Fig. 1 caption** | §III | **lightest — floats occupy ~⅓ of the page** |
| 4 | 6,751 | — | §III end, §IV | full |
| 5 | 6,500 | **Table II** | §IV end, §V-A | full |
| **6** | **7,050** | — | §VI **+ all 19 references** | **full to the last line** |

**Greatest page pressure, ranked.**

1. **Page 6 — the binding constraint.** §VI plus the entire reference list, ending on the final line. Any net addition anywhere upstream pushes content onto page 7. The references alone are **522 words / 4,131 chars**, about 60% of a page, and the venue counts them.
2. **Page 2 — the densest prose.** This is where §I's mechanism paragraph (¶14) and §II's re-statement of the same material (¶21–22) sit adjacent. The duplication the plan proposes cutting is concentrated exactly on the fullest text page, which is favourable.
3. **Page 3 — float-dominated, not text-dominated.** Table I and the full-width Figure 1 consume roughly a third of it. **Figure 1 is 152.9 × 60.0 mm**, not the 182 mm I had assumed; it fits every variant tested, including v4's narrow geometry. The figure is **not** a page-pressure risk and does not need rescaling. This also removes the conditional attached to M-7 in the review: the figure is not going to be shrunk, so the C₀–C₃ mappings can be added to the text on their merits rather than as insurance.
4. **Not a pressure point:** Table II (5 rows) and the author block, both modest.

---

## 5. Is ≈ 67 words of net reduction sufficient?

**It is arithmetically sufficient and operationally too thin.**

Measured at **7.17 characters per word** including spaces, from the manuscript's own text:

| | Words | Chars |
|---|---|---|
| Additions from the 24-edit plan | +493 | **+3,535** |
| Compression budget as planned | −560 | −4,015 |
| Net as planned | −67 | **−480** |

A page holds roughly 7,000 characters, so a 480-character surplus is **about 0.07 of a page**. Against a document that currently ends on the last line of page 6, that is the entire safety margin.

Three factors argue for more than break-even:

- **Renderer difference.** These counts come from LibreOffice. The author will render in Word, whose line-breaking and font metrics differ; a one- or two-line divergence is routine and 0.07 page is about four lines.
- **Known downstream additions.** `phase9:178` warns that an acknowledgment, funding line, expanded author affiliations or PDF eXpress reflow could each push the paper over.
- **Float reflow.** Adding a third table (E-9) changes float placement and can cascade across pages 3–5 unpredictably.

**Recommendation: target ≈ −200 words net, not −67.** Section 6 shows how to get there without losing anything essential.

---

## 6. Reassessment of the 560-word compression budget

The budget contains a **double-count** and three cuts that, taken as written, would remove material the review itself relies on.

### The double-count

**Cuts 1 and 6 are the same material.** Cut 1 deduplicates §I ¶14 against §II ¶21–22 (−200); cut 6 compresses "§II's three-paragraph treatment of [2]–[5]" to one paragraph (−100). Those are the same mechanism passages. They cannot both be banked.

### Cuts that would remove essential content

| Cut | Risk as written | Must be preserved |
|---|---|---|
| **1 — §I/§II dedup** | §I ¶14 ends "This paper contributes none of these mechanisms", and ¶15 carries the functional-individuation argument from [5] that **grounds the criterion itself**. Deleting ¶14 wholesale takes the disclaimer with it. | The four citations, the "contributes none of these mechanisms" disclaimer, and **¶15 untouched** |
| **2 — non-claims consolidation** | §VI ¶122 ("The study characterises governance activation; it does not validate it…") is the paper's defensive core. §V-D ¶119 sits immediately after the RQ1 answer, which is exactly where a reviewer needs the scope limit. | **§VI ¶122 in full**; a one-sentence §V-D ¶119 |
| **4 — §III ¶62–63 tightening** | ¶62 contains "ΔL2 measures how often the intermediate restriction binds, not how much the recommendation set contracts" — the paper's only defence against the magnitude objection, and the sentence E-7 amends. | **¶62's two consequences**; compress **¶63 only** |
| **5 — Table II trim** | "Small-vessel baseline / <10 GRT" is the only scannable statement of the baseline vessel class, which E-13, E-17 and E-20 make load-bearing. | **Keep the `<10 GRT` row**; cut "Period" only |
| **6 — §II compression** | §II ¶23 distinguishes [7], [8] and [9] on specific properties and is **the entire support for the gap claim**. | **¶23 in full** |

### Revised budget

| | Cut | Words |
|---|---|---|
| 1+6 | Consolidate the mechanism material into §II as one paragraph; §I retains one sentence with the four citations plus the disclaimer; ¶15 and ¶23 untouched | **−230** |
| 2 | Non-claims: delete the §I ¶18 tail, compress §III ¶62's tail, reduce §V-D ¶119 to one sentence; §VI ¶122 intact | **−110** |
| 3 | C₃ demotion (E-8, already inside the +493 net) | −120 |
| 4 | Compress §III ¶63 only | **−60** |
| 5 | Table II: "Period" row + the `C1↔C3` row | **−12** + 2 rows |
| | **Total** | **−532 words + 2 table rows** |

Two removed table rows are worth roughly 28 pt of vertical space, about 280 characters — call the effective budget **≈ −570 words**.

### One further change recovers the margin

**Render E-9's component specification as prose, not a table.** As drafted it is a 5-row × 3-column table; in one column of a two-column IEEE layout it would be cramped at 8 pt, it costs ~7 lines of frame beyond its ~60 words of content, and it introduces a third float that can reflow pages 3–5. The same information fits in about 70 words of prose, already most of the way written in E-10.

| | Table form | Prose form |
|---|---|---|
| Word-equivalent cost | ~140 | ~70 |
| New float | yes | no |
| Reflow risk | pages 3–5 | none |

**Revised arithmetic with that change:** additions +493 − 70 = **+423 words**; budget **−570**; **net ≈ −147 words ≈ −1,050 chars ≈ 0.15 page of slack.** That is a workable margin.

---

## 7. Changes required to the 24-edit plan

| | Change | Reason |
|---|---|---|
| **P-1** | §3's framing: compression is **not** mandatory for compliance | v8 on A4 is 6 pages unchanged |
| **P-2** | Fix the geometry target: **A4 at 39.70 pt side margins** (182.0 mm). **Do not copy v4's 1-inch margins** — they give 8 pages | Measured |
| **P-3** | Set one uniform side-margin value across all nine `sectPr` blocks | v8 carries two values |
| **P-4** | Merge compression cuts 1 and 6; revise the budget to **−532 words + 2 table rows** | Double-count |
| **P-5** | Narrow cuts 1, 2, 4, 5, 6 per the preservation column in §6 | Protects ¶15, ¶23, §VI ¶122, §III ¶62, the `<10 GRT` row |
| **P-6** | **E-9: prose, not a table** | Halves the cost, removes a float, eliminates reflow risk |
| **P-7** | Raise the net target from −67 to **≈ −150 words** | Renderer difference, known downstream additions |
| **P-8** | **M-7's conditional is void.** Figure 1 is 152.9 × 60.0 mm and fits every geometry; it will not be rescaled. Add the C₀–C₃ mappings on their merits | Measured from the docx |
| **P-9** | Blocker **B-1 is resolved.** The A4 page budget is now established | This assessment |

No change to any edit's **content**, classification or scientific justification. E-23 remains deferred.

---

## 8. Final revision sequence

**Stage 1 — Scientific edits** *(no page-count target; apply in full)*
Critical first: E-1 title · E-5 delete the isolation contribution · E-9 + E-10 classifier specification, **as prose** · E-17 attribution–transfer link · E-20 band status in limitations.
Then Major: E-2, E-3 abstract · E-4 RQ1 · E-6 contributions · E-7 invariance proviso · E-8 C₃ demotion · E-11 retrieval parameters · E-13 wave-band provenance · E-14 product comparison · E-15, E-16 sensitivity · E-18 daylight identity · E-21 conditional RQ1 answer · E-22 repeatability clause · E-24 conclusion.
Then Minor: E-12 window. **Defer E-19 and E-23.**

**Stage 2 — Low-risk compression** *(target −532 words, in this order)*
1+6 merged mechanism consolidation (−230) · non-claims (−110) · §III ¶63 (−60) · Table II two rows (−12). The C₃ demotion (−120) is already applied in Stage 1.

**Stage 3 — A4 rendering**
Set all nine `sectPr` blocks to 595.30 × 841.90 pt, side margins 39.70 pt, top 54 pt, bottom 72 pt, uniformly. Re-render. Confirm `pdfinfo` reports A4 and **≤ 6 pages**. Check that Figure 1 and both tables placed sensibly and that no column ends mid-table.

**Stage 4 — Final verification**
Re-confirm every canonical figure unchanged against `data/c8/reproducibility-verification/threshold-sensitivity-20261008-stdout.txt`: 5.81, 4.48, 42.88, 41.08, 48.69, 45.56, 0.00, 9.22, 6.08, 1.26, 0.37, 9.59, 7.40, 531, 518, 13, 97.6, 2.4, 9,135, 5,935, 43,848, 28,501, 5,536, 3,594, 78, 56, 0.48, 0.78, and the newly added 6.45. Confirm the reference list is unchanged at 19 entries and that `C1↔C3` no longer appears in Table II. Then: PDF metadata (title and author), reference [14]'s URL, the author block, and **IEEE PDF eXpress, Conference ID 71745X**, which must run on the final PDF.

**Do not** interleave Stages 1 and 2 with rendering. Apply the science, then compress, then set the geometry once, then measure once.

---

## 9. What was not done

The manuscript was not edited. No canonical result was altered. No resolved scientific issue was reopened: the [16] non-contradiction, the solar specification, the source-faithful equality operators, the 56-combination count, the 518/13 exclusivity and all 28 verified numerical claims stand as previously established and were not revisited. Three geometry variants were rendered from scratch copies; the submitted file is byte-identical to the one reviewed.
