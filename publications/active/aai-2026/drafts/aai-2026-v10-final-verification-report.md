# AAI 2026 — v10 Final Verification Report

**Manuscript:** *From Declared Risk Levels to Admissible Recommendations: Measuring How Often an Intermediate Governance Level Binds in Deterministic Historical Replay*

| Item | Value |
|---|---|
| Revision stage | Minor revision / final verification |
| Source | `aai-2026-manuscript-v9-revised-A4.docx`, SHA-256 `16f31033b7efa8f43ffcc114b79dd0eb0d2afcd4465599379308890c742ba5a6` |
| Output (DOCX) | `aai-2026-manuscript-v10-final-A4.docx`, SHA-256 `b450226a0a73deec385e1aa22a1b10a00953a4cab1e2cd906f8bff2085d84ffd`, 416,759 B |
| Output (PDF) | `aai-2026-manuscript-v10-final-A4.pdf`, SHA-256 `7179f5f3647c3fed14abe34a771d5e165db8c45a2e691a08d50937ff02ad6ec0`, 381,412 B |
| Repository | `AMIT-v5` @ `a7f77d8351ec94c586309d796aabd1230f4886dd` |
| Date | 9 October 2026 |
| Edits applied | 4 asserted single-match OOXML substitutions implementing 3 corrections |
| Verdict | **Three corrections implemented and verified. Six A4 pages. No verified numerical result changed. Not marked submission-ready — three requirements remain outside this session (U-1, U-2, U-3).** |

v9 was opened read-only, copied, and left untouched; its DOCX and PDF still carry their original hashes (`16f31033…`, `75db31a1…`). No experiment was run and no canonical script, dataset, threshold or output artefact was modified; `git status` reports zero modified tracked files.

---

## A. Correction 1 — Common-period comparison (§V-A)

**Scientific reason.** "Independently lowers" asserts a causal effect of record length on the binding rate. The experiment compares a full record with its own subset; it does not isolate record length from the conditions that happen to fall inside the subset, so the causal reading is not supported by the design.

**Before (v9):**

> Evaluated on the 5,935 hours common to both records, with identical thresholds and denominator, the two products give 6.45% and 4.48%, 1.97 percentage points apart; the full-record gap of 1.33 points understates this because the longer record independently lowers the rate by 0.64 points.

**After (v10):**

> Evaluated on the 5,935 hours common to both records, with identical thresholds and denominator, the two products give 6.45% and 4.48%. The full-record gap is 1.33 percentage points, compared with 1.97 points on the common period, reflecting a 0.64-point difference between the full PRIMARY record and its common-period subset.

**Notes.** The replacement sentence is the author-specified wording verbatim. The trailing clause "1.97 percentage points apart" was removed from the preceding sentence because the new sentence states that value; 1.97 therefore still appears exactly once in the paragraph, and no value is lost. The 6.45% vs 4.48% matched-period comparison is preserved. The two preceding sentences — "The two configurations differ in both wave source and record period…" and "…the difference is not attributed to spatial resolution alone" — are unchanged, so the distinction between wave-product dependence and record-period difference is retained. Word delta +5.

---

## B. Correction 2 — Sensitivity interpretation (§V-B)

**Scientific reason.** The ratio divides a movement in a wave-height parameter, varied over two sourced interpretations, by a movement in a rainfall-intensity parameter, varied over an unsourced exploratory range. The operands differ in unit and in the width and provenance of their perturbation ranges, so the quotient is arithmetically correct but does not express a comparable sensitivity.

**Before (v9):**

> Varying the wave UNSAFE boundary across its two source-grounded readings moves ΔL2 by 3.41 percentage points, while varying the rainfall CAUTION boundary across the widest researcher-defined range evaluated here changes ΔL2 by 0.48 percentage points in PRIMARY and 0.78 percentage points in RESOLUTION, a ratio of about seven to one, with the wave boundary varied only over sourced values and rainfall over unsourced ones.

**After (v10):**

> Varying the wave UNSAFE boundary across its two source-grounded readings moves ΔL2 by 3.41 percentage points in PRIMARY, while varying the rainfall CAUTION boundary across the exploratory range evaluated here changes ΔL2 by 0.48 percentage points in PRIMARY and 0.78 percentage points in RESOLUTION. The wave boundary was varied only over sourced values and the rainfall boundary over an unsourced exploratory range, so the two movements are not comparable as a ratio and establish no intrinsic sensitivity ranking beyond the ranges evaluated.

**Notes.** The ratio is removed. All three absolute movements are reported as specified — wave UNSAFE 3.41 pts in PRIMARY, rainfall CAUTION 0.48 pts in PRIMARY and 0.78 pts in RESOLUTION — with PRIMARY attribution now explicit on the wave figure. The closing clause states both restrictions the author required: the comparison is confined to the evaluated ranges, and no intrinsic ranking is claimed. "Widest researcher-defined" became "exploratory" to match the corrected characterisation; the six other uses of "researcher-defined" elsewhere in the manuscript, all of which disclose unvalidated design choices, are untouched. The adjacent wind-threshold sentence (21.80 kn / 19.30 kn / 27.0 kn / W_C = 18–25 kn) is unchanged. Word delta +18 across two substitutions.

---

## C. Correction 3 — Conclusion (§VI)

**Scientific reason.** The observed frequency is produced jointly by the classifier, the environmental record replayed and the evaluation-set policy. Attributing it to the classifier alone understates two of its three determinants, and the contrast with "the contract" is the wrong axis: the contract is what makes the frequency mean something, not what sets its value.

**Before (v9):**

> The replay establishes an activation frequency for one contract at one site under one classifier; by construction the isolated increment equals the intermediate state's occupancy, so the figure is a property of the classifier rather than of the contract; and the wave band, the admissible set at CAUTION, and any link between activation and outcome remain unvalidated.

**After (v10):**

> The replay establishes an activation frequency for one contract at one site under one classifier; by construction the isolated increment equals the intermediate state's occupancy, so the observed binding frequency depends on the classifier, environmental record and evaluation policy, while the admissible-set contract determines what that frequency represents; and the wave band, the admissible set at CAUTION, and any link between activation and outcome remain unvalidated.

**Notes.** The clause "by construction the isolated increment equals the intermediate state's occupancy" is deliberately retained unchanged: it is the sentence that keeps the mathematical identity ΔL2 ≡ P(S = CAUTION) distinct from the CAUTION occupancy measured from the historical record, and removing or softening it would reopen a resolved issue. The limitation clause that follows is unchanged. Word delta +9.

---

## D. Reference [14] — verification outcome

**Outcome: VERIFIED AS CORRECT. No change made.**

The recorded URL, flagged as suspect in the v9 report (item U-4) because of the English conjunction "and" in an otherwise Malay slug, was retrieved on 9 October 2026 and resolves to a live METMalaysia page:

- URL: `https://www.met.gov.my/ramalan/angin-kencang-and-laut-bergelora/`
- Page title: *Kriteria Amaran Angin Kencang dan Laut Bergelora*
- Content: three warning categories with wind-speed and wave-height thresholds — 40–50 km/h and/or waves to 3.5 m; 50–60 km/h and/or waves to 4.5 m; above 60 km/h and/or waves above 4.5 m.

The slug's "and" is the department's own spelling, not a transcription error on our part. The Malay-spelled variant `.../angin-kencang-dan-laut-bergelora/` was also tested and does **not** resolve, which confirms the recorded form is the correct one rather than a corruption of it.

The retrieved thresholds corroborate the manuscript's wind provenance claim in §IV: 40 km/h = 21.6 kn and 50 km/h = 27.0 kn, exactly the W_CAUTION and W_UNSAFE boundaries the manuscript attributes to [14].

Reference [14] is unchanged, including its 24 September 2026 access date, which remains accurate. No other reference was touched; all 19 remain, in order, with identical text.

**U-4 from the v9 report is closed.** No replacement URL was invented and none was needed.

---

## E. Layout verification

| # | Requirement | Result | Evidence |
|---|---|---|---|
| 1 | Six pages maximum including references | **PASS — 6 pages** | `pdfinfo`: `Pages: 6`; references [1]–[19] all on page 6, ending with white space remaining in the right column |
| 2 | A4 dimensions | **PASS** | `pdfinfo`: `595.304 x 841.89 pts (A4)`; `<w:pgSz w:w="595.30pt" w:h="841.90pt"/>` on all 9 `sectPr` |
| 3 | Consistent two-column geometry | **PASS** | All 9 `sectPr` byte-identical to v9: body `<w:cols w:num="2" w:space="10.80pt"/>`, title band single column, author band 4-column, margins `top 54pt / right 39.70pt / bottom 72pt / left 39.70pt` |
| 4 | No text, table, figure or reference clipping | **PASS** | Table I and Table II both `tblW = 248.10pt` against a 252.55pt column; Figure 1 at 152.9 × 63.1 mm against a 182.0 mm full-width band; pages 1, 5 and 6 inspected as rendered images — no overset, no truncation, no run-together text; all 19 references complete |
| 5 | Figure 1 unchanged | **PASS** | `word/media/image1.png` SHA-256 `c324faa933f12e8d89eced2a1e5514f23bdf4160d3160d3dd9da8ffef5aa7204` in both v9 and v10; `<wp:extent cx="5504180" cy="2161540"/>` unchanged; still on page 3; single image in the document |
| 6 | Author block and keywords intact | **PASS** | Page 1 inspected visually: both authors, both affiliations, both e-mail addresses and the Keywords line render correctly and are byte-identical to v9 in the XML |
| 7 | No new layout regressions | **PASS** | Extracted text of pages 1–4 identical to v9 character-for-character; only pages 5 and 6 changed; `document.xml` validates as well-formed XML |

**Page fill (characters of extracted text, `pdftotext -layout`):**

| Page | v9 | v10 |
|---|---|---|
| 1 | 6,363 | 6,363 |
| 2 | 8,452 | 8,452 |
| 3 | 6,340 | 6,340 |
| 4 | 9,714 | 9,714 |
| 5 | 8,740 | 9,323 |
| 6 | 9,815 | 10,442 |

The +32 words were absorbed within the existing six pages; no compression was required and none was applied.

**Rendering toolchain:** LibreOffice 24.2.7.2. The DOCX was repackaged by the same procedure used for v9.

---

## F. Numerical integrity

Every numeric token in the document was extracted from v9 and v10 and compared as a multiset.

**Result: identical. No value, count, percentage, threshold, hour count or date differs between v9 and v10.**

Spot-confirmed as present and unchanged in v10: 5.81%, 4.48%, 6.45%, 1.97, 1.33, 0.64, 3.41, 0.48, 0.78, 9.22%, 1.26%, 0.37%, 9.59%, 7.40%, 97.6%, 531, 518, 13, 2.4%, 9,135, 5,935, 5,536, 3,594, 266, 86.5%, 93.2%, 21.80 kn, 19.30 kn, 27.0 kn, 18–25 kn, 1.0 m, 1.25 m, 1.875 m, 1.90 m, 10 GRT, 19 references.

Structural integrity: 2 tables (4 and 7 rows, as in v9), 1 figure, 19 references, 9 section properties. Body word count 6,892 → 6,924 (+32). Phrases removed and confirmed absent: "independently lowers", "understates", "seven to one", "property of the classifier", "1.97 percentage points apart". A character-level diff of `word/document.xml` returns 42 differing regions, every one of which is a fragment of the four intended substitutions; nothing else in the file changed.

Canonical artefacts: `git status` reports 0 modified tracked files. `scripts/condition_comparison.py`, `scripts/sensitivity/threshold_sensitivity.py` and `scripts/canonical_gt.py` are at their recorded hashes. No experiment was executed.

---

## G. Remaining submission requirements and unresolved issues

### Blocking the "submission-ready" label

**U-1 — IEEE PDF eXpress validation not performed.** Conference ID 71745X. The final PDF has not been submitted to PDF eXpress from this session and no claim of PDF eXpress compliance is made. This must be done by the author before upload to EDAS (https://edas.info/N34957).

**U-2 — Microsoft Word page count unverified.** The six-page count is from LibreOffice 24.2.7.2. Microsoft Word is not available in this environment, and a Word render could differ by a line or two at the page boundary. The author should open `aai-2026-manuscript-v10-final-A4.docx` in Word and confirm six pages. Page 6's right column ends with visible white space, so the margin is larger than in v9, but this remains unverified in Word.

*If Word reports seven pages,* three reversible cuts in priority order, each self-contained and none touching a numerical result:
1. In §V-B, delete "and the rainfall boundary over an unsourced exploratory range" (−9 words) — the provenance asymmetry is already stated in §IV.
2. In §V-A, shorten "reflecting a 0.64-point difference between the full PRIMARY record and its common-period subset" to "a 0.64-point difference from the full-record subset" (−8 words).
3. In §VI, delete ", environmental record and evaluation policy" and rely on the preceding sentence (−5 words) — least preferred, as it partly undoes Correction 3.

**U-3 — IEEE template compliance verified only for page geometry.** The repository holds no copy of the official AAI 2026 IEEE A4 conference template; a search of the working tree returns only our own earlier renders. Page size, margins, column count and column spacing were therefore verified against the IEEE A4 specification as recorded in the project's layout audit, not against the official template file. Font metrics, heading styles and caption styles have **not** been compared with the official template. No claim of official template compliance is made. To close this, place the official template in the repository and re-run the comparison.

### Author decisions, not blocking

**U-5 — Code and data availability statement.** Still deferred. The recorded AAI 2026 requirements contain no availability requirement, so this is optional; the reproducibility manifest and guide exist in `docs/reproducibility/` if the author chooses to add one.

**U-6 — Reference [16], Table 12 cell label.** The claim that the source proposes "departure restrictions or cautions" for vessels under 10 m at 1 m and above was verified from the publication text during the v9 review. The specific Table 12 cell label was not independently confirmed and the primary PDF is still not held in `papers/sources/`.

**U-7 — MMD operator phrasing.** Unverified, as in v9.

**U-8 — Author block rendering.** Closed. Page 1 renders correctly; the "run-together text" noted earlier was an artefact of text extraction, not a document defect.

**References [4] and [18]** end with a bare URL and no terminal period, unlike the other seventeen entries. This is a style inconsistency inherited from v9, not an error, and was left unchanged under the instruction not to modify unrelated references. The author may wish to normalise it.

---

## H. Completion criteria

| Criterion | Status |
|---|---|
| All three scientific corrections implemented | **Met** — verified in `word/document.xml` and in the rendered PDF |
| Verified numerical results unchanged | **Met** — numeric multiset identical to v9 |
| Renders within six A4 pages | **Met in LibreOffice** — 6 pages, 595.304 × 841.89 pt; unverified in Word (U-2) |
| Submission-ready | **Not claimed** — U-1, U-2 and U-3 are outside what this session can complete |
