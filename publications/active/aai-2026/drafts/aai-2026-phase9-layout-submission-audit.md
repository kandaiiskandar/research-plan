# AAI 2026 — Phase 9 Layout & Submission Audit

**Date:** 2026-09-24
**Artefacts:** `aai-2026-manuscript-v1-ieee-layout.docx` · `aai-2026-manuscript-v1-ieee-layout.pdf`
**Content source:** `aai-2026-manuscript-v1-full-assembled.md` (unchanged)

---

## 1. Venue Requirements

| Requirement | Verified requirement | Official source | Status |
|---|---|---|---|
| Paper size | **A4** — *"Paper must be 4 to 6 pages of A4 size in length including all texts, references, figures and photographs."* | aai.unimap.edu.my — Manuscript Preparation | ✅ VERIFIED |
| Columns | IEEE conference two-column | same | ✅ VERIFIED |
| Page limit | **4–6 pages.** *"Any submitted paper that exceeds six (6) pages will be rejected."* | same | ✅ VERIFIED |
| References included in limit? | **YES** — the limit covers *"all texts, references, figures and photographs"* | same | ✅ VERIFIED |
| Template | *"Follow the IEEE Manuscript Template for Conference Proceedings format."* | same, linking ieee.org/conferences/publishing/templates | ✅ VERIFIED |
| Author policy | **Not stated** on the manuscript-preparation page | — | ⚠️ CARRIED — the repo's track-fit analysis records AAI 2026 as non-blind; not re-verified from an official page this phase |
| PDF requirement | IEEE PDF eXpress | same | ✅ VERIFIED |
| PDF eXpress | Required; **Conference ID 71745X**, ieee-pdf-express.org | same | ✅ VERIFIED |
| Submission system | **EDAS** — https://edas.info/N34957 | same | ✅ VERIFIED |
| Deadline | **19 October 2026** (extended from 21 September 2026) | aai.unimap.edu.my — Call for Papers | ✅ VERIFIED |

No **VENUE REQUIREMENT CONFLICT**. Every locked assumption (IEEE conference format, A4, two-column, 6-page maximum) is confirmed by the official page, and the requirement that references count toward the limit is now confirmed rather than assumed.

---

## 2. Layout Result

**Rendered page count: 6.** Page size 595.3 × 841.9 pt = A4, confirmed by `pdfinfo` on the rendered PDF, not estimated.

| Item | Value |
|---|---|
| References begin | page 5, right column |
| References end | page 6, left column |
| Classification | **FIT** — 6 pages, at the limit, not over it |

Per Part F the prose was **not compressed** and the spare space on page 6 was **not filled**. No figure, literature, discussion or conclusion text was added.

---

## 3. Per-Page Layout Audit

| Page | Content | Issue | Status |
|---|---|---|---|
| 1 | Title block (full width), Abstract, Index Terms, §I Introduction | None | ✅ |
| 2 | §I end, §II Background, §III opening, TABLE I | None | ✅ |
| 3 | §III criterion, **TABLE II (spans both columns)**, both displayed Δ expressions, §IV opening | Table II initially wrapped its header and orphaned a `)`; fixed by two-column spanning | ✅ resolved |
| 4 | §IV end, §V-A, TABLE III, §V-B, §V-C opening | None | ✅ |
| 5 | §V-C, §VI, References [1]–[5] | Reference [4]'s long FAA URL wraps mid-token | ✅ acceptable |
| 6 | References [6]–[18], left column only; right column empty | Spare space by design — not refilled | ✅ |

No clipping, no overlapping text, no broken equation, no unreadably small text, no orphaned heading, no inconsistent columns, no text crossing margins.

**Layout-only optimisations applied** (all within Part G, none touching content):

1. **TABLE II set to span both columns** via a continuous single-column section. At one-column width the header `A_AI(CAUTION)` could not fit on one line at 8 pt, leaving a `)` alone on a second line, and three of four row labels wrapped to three lines. Spanning resolves both; this is the standard IEEE construct for a table of this width.
2. **References changed from justified to left-aligned.** The long official URLs in [4], [14], [15], [17] and [18] forced extreme inter-word stretching under justification. Left alignment is normal IEEE practice for reference lists containing URLs.

Neither change altered a word of the manuscript.

---

## 4. Table Audit

| Table | Result |
|---|---|
| **TABLE I** — Admissible recommendation sets | **PASS.** Three rows, subscripted A<sub>AI</sub>(*S*) renders correctly, ∅ renders, footnote present |
| **TABLE II** — Four governance configurations | **PASS** after column spanning. All four configurations present with FULL/FULL/FULL · FULL/FULL/∅ · FULL/{Go, Delay}/∅ · FULL/FULL/∅ |
| **TABLE III** — Binding frequency, comparator decomposition and sensitivity results | **PASS.** All eight rows, both notes, and the two **withheld RESOLUTION cells remain em dashes**. 41.08% and 45.56% do not appear anywhere in the PDF |

All locked values verified present in the rendered text: 5.81%, 4.48%, 42.88%, 48.69%, 0.00%, 5.67–9.56%, 4.26–6.64%, 9,135, 5,935, <10 GRT.

---

## 5. Equation Audit

| Expression | Result |
|---|---|
| Δ = (*N*<sub>restricted</sub> / *N*<sub>eval</sub>) × 100% | **PASS** — centred, italic, subscripts correct |
| Δ<sub>L2</sub> = (C0↔C2) − (C0↔C1) | **PASS** |
| Δ<sub>L2</sub> ≡ *P*(*S* = CAUTION) | **PASS** — identity sign renders; still introduced in prose as *"a metric-interpretation identity, not a result"* |

Equations are unnumbered, which the template permits and the prose does not require. None is called a theorem or proposition.

**Declared formatting limitation.** The expressions are typeset as Unicode text runs in Times New Roman rather than as OMML/MathType objects. They render correctly and are legible at 10 pt, but a publisher-side conversion may prefer native equation objects. This is noted rather than hidden.

---

## 6. Bibliographic Recheck

| Item | Result |
|---|---|
| **MET thunderstorm [15]** | **CARRIED LIMITATION.** `met.gov.my/ramalan/ribut-petir/` again returned a redirect loop on two further attempts. The page exists on the issuing authority's domain, and the companion wind page fetched cleanly, so the domain is live. No criterion wording was invented |
| **COLREG [17]** | **CLAIM SUPPORT NOW VERIFIED.** The IMO page remains robots-disallowed, but Rule 20(b) was verified verbatim from the US Coast Guard Navigation Center's official *Navigation Rules Amalgamated*: *"The Rules concerning lights shall be complied with from sunset to sunrise…"* — exactly the day boundary the manuscript uses. The reference still points to the IMO convention as the primary instrument. The non-daylight→UNSAFE policy remains declared researcher-defined |
| **Open-Meteo year [12]** | **UNRESOLVED.** Open-Meteo's own documentation publishes no recommended citation, and the concept DOI 10.5281/zenodo.7970649 resolves to the latest version record (14582479, dated 2024-12-31). The first-version date could not be confirmed. **2023 was retained as locked** rather than changed on the strength of a version page |
| **Alshiekh DOI [3]** | **NOT REQUIRED.** No authoritative DOI established; cited by proceedings with pages 2669–2678. None invented |
| **Flehmig pagination [10]** | **UNESTABLISHED.** A targeted search returned no pagination. Reference left as-is. No page numbers guessed |

**MET wind [14]** was fully verified in Phase 8 — Category One is *"40–50 kmsj"*, i.e. 21.6–27.0 kn, exactly the canonical W<sub>C</sub> and W<sub>U</sub>. **DID [18]** was likewise verified — *Light* tops out at 10 mm in one hour, exactly R<sub>C</sub>.

---

## 7. IPoSCI Status

**STATUS A — ACCEPTED, NOT PUBLICLY PUBLISHED.**

The symposium is 12–13 November 2026; today is 24 September 2026, so it has not taken place. The official organiser page carries no proceedings link, DOI or ISBN, and a further search for proceedings or an indexing record returned nothing.

**Consequence for AAI:** no bibliographic citation is required or permitted at this stage. IPoSCI is absent from the manuscript and from the reference list, and nothing describes the material as previously published or previously reported. The recheck must run once more immediately before the 19 October submission.

---

## 8. Scientific Integrity Audit

| # | Check | Result |
|---|---|---|
| 1 | Responsible AI governance-measurement framing | ✅ preserved |
| 2 | No claim the mechanism is novel | ✅ — *"This paper contributes none of these mechanisms"* on page 1 |
| 3 | Scoped gap language | ✅ *"Within the reviewed literature"* ×2, both intact |
| 4 | No novelty escalation | ✅ *novel*, *first*, *unique*, *unprecedented*, *never*, *no previous study* all absent; the single *unexplored* is a negation |
| 5 | Criterion remains an operational measurement rule | ✅ |
| 6 | C1↔C3 = 0 entailed / conformance | ✅ |
| 7 | Δ<sub>L2</sub> ≡ P(CAUTION) a metric-interpretation identity | ✅ |
| 8 | 5.81% / 4.48% remain binding frequencies | ✅ |
| 9 | Envelopes remain deterministic configuration ranges | ✅ *"not confidence intervals or uncertainty estimates"* |
| 10 | 2.54–14.75% remains a controlled perturbation | ✅ |
| 11 | −1.2 pp / 0.05 m descriptive, not causal | ✅ *"rather than a causal derivative"*; **−1.4 absent from the PDF** |
| 12 | 97.6% is attribution of CAUTION classifications | ✅ *"not of incidents or unsafe outcomes"* |
| 13 | Marine-warning qualification is a lower bound | ✅ |
| 14 | {Go, Delay} researcher-defined and unvalidated | ✅ |
| 15 | No safety-effectiveness claim | ✅ |
| 16 | No decision-quality claim | ✅ |
| 17 | No effective-human-oversight claim | ✅ |
| 18 | No generalisation claim | ✅ |

### Strict content diff

The rendered PDF text was extracted and compared against `aai-2026-manuscript-v1-full-assembled.md`. All **177 body sentences** are present. Nine did not match on a first whole-string comparison; each was probed individually and found present. The cause in every case was `pdftotext` dropping a hyphen that falls at a line break (*specification-level* → `specificationlevel`, *Risk-management* → `Riskmanagement`, *human-automation*, *three-state*, *non-daylight*), which is an extraction artefact, not a document defect — the same hyphens survive when they fall mid-line.

**No scientific prose difference. No UNAUTHORISED CONTENT CHANGE.**

---

## 9. Citation Integrity

| Check | Result |
|---|---|
| In-text unique references | **18** |
| Bibliography entries | **18** |
| Numbers present in rendered PDF | **[1]–[18], gapless** |
| Orphans | **0** |
| Missing | **0** |
| Duplicates | **0** |
| Unresolved symbolic keys | **0** |
| Batool et al. | **2025** ✅ |
| MFWAM | **[11]** ✅ |
| IPoSCI | **absent** ✅ |
| ASTM | **no invented clause** ✅ |

---

## 10. Submission Metadata Still Required

1. **Author name(s), affiliation(s), email(s).** The layout carries `[AUTHOR NAME]`, `[AFFILIATION]`, `[EMAIL]`. AAI 2026 is recorded as non-blind, so real details are required. **AUTHOR METADATA REQUIRED BEFORE SUBMISSION.**
2. **Acknowledgment / funding.** None written. If a scholarship or grant must be acknowledged, the author must supply the wording — no funding text was invented.
3. **IEEE PDF eXpress.** Conference ID **71745X**. The PDF here has **not** been processed through PDF eXpress; no compliance claim is made. That step must be run on the final PDF after author details are inserted.
4. **EDAS metadata.** Title, author order, abstract and keywords entered at https://edas.info/N34957 must match the PDF exactly.
5. **Copyright.** The manuscript-preparation page did not state a copyright-notice or eCF requirement at this stage. Not verified; check on EDAS at final submission. No copyright text was invented.
6. **Blind/non-blind confirmation.** Not stated on the official page; carried from the repo's earlier analysis. Confirm before inserting author details.

---

## 11. Layout Compression

**NOT REQUIRED.** The compliant layout renders at exactly 6 pages, inside the 4–6 page rule. No controlled compression plan was drafted and no content cut was proposed or made.

The paper sits **at** the limit rather than under it, so the margin is thin. Anything later added — an acknowledgment, a funding line, longer author affiliations, or PDF eXpress reflow — could push it to 7 and trigger rejection. The empty right column on page 6 absorbs some of that, but the author block is on page 1 and expands downward there. Worth watching when author details go in.

---

## 12. Final Decision

**PHASE 9 STATUS: READY FOR AUTHOR METADATA & FINAL PDF COMPLIANCE**

The manuscript is content-complete, verified, and fits the official format at 6 A4 pages. What remains before submission is author metadata, any acknowledgment the author chooses, and the PDF eXpress pass — none of which this phase can supply or fake.

---

PHASE 9 STATUS: READY FOR AUTHOR METADATA & FINAL PDF COMPLIANCE
