# AAI 2026 v4 — Author Verification Required

Items I could not close from evidence in the project. None blocks submission of v4, but each is yours to decide before the paper is final.

---

## 1. The 2.8 m medium-vessel boundary remains unexplained in the project record

The variant is now out of the paper, so this does not affect the manuscript. It is still an open hole in the canonical record.

- `docs/canonical/appendix-c-formalisation.md` line 611 calls the value "interpolated" but records no arithmetic.
- I tested six candidate interpolation rules against the corpus; they give 2.39–3.05 m and none returns 2.8.
- 2.8 is exactly 2.0 × the 1.4 m onset, which is the most plausible origin, but nothing in the repository says so.

**You need to decide:** either record the actual derivation in Appendix C, or reclassify the row as researcher-defined. Leaving it marked "interpolated" without a rule will fail the same audit again in the journal version.

---

## 2. Your own Figure 1 raster still uses **Ø**, not **∅**

The figure you supplied uses U+00D8 (capital O with stroke) where the empty set is meant. The reconstruction I deliver (`aai-2026-figure1-v5*.png`) uses U+2205 throughout, and that is what is embedded in v4.

I could not correct your original because **no editable source for it exists in the project** — I searched for `.svg`, `.drawio`, `.pptx`, `.ai`, `.fig` and `.vsdx` and found none. v5 is a reconstruction, not an edit of your file.

**You need to decide:** accept the reconstruction as the figure of record, or send me your source file and I will apply the same corrections to it so your exact styling is preserved.

---

## 3. "−1.4 pp per 0.05 m" in `docs/analysis/experiment-report-delta-l2.md` §272 is wrong

Already corrected in the manuscript to −1.2. The **source report still carries −1.4**. Canonical endpoints give −1.221 (PRIMARY) and −1.252 (RESOLUTION).

**You need to decide:** whether I should amend that report. I have not touched it — it is an analysis artefact, and your standing instruction is not to edit historical or provenance artefacts without being asked.

---

## 4. The configuration-count clause is a judgement call

§IV now reads "evaluates 56 distinct combinations, of which this paper reports a subset". Instrumented execution gives **78 executions / 56 unique configurations**. The paper reports fewer than 56 and does not enumerate which.

**You need to decide:** whether a reviewer will want the specific subset named. Naming it costs roughly two lines, and page 6 is full — something would have to come out.

---

## 5. Defect I introduced and have now fixed — for the record

The 38 stray `\"` backslashes across all 19 reference entries in **v2** came from a pandoc round-trip I ran, not from your source. They rendered in the v2 PDF you received. They were removed in v3 and v4 (`stray backslash-quote: 0`). If v2 went anywhere outside this project, that copy is defective.

---

## Not verification items, but worth knowing before you submit

- **Page 6 is full.** No whitespace remains. Any addition requires a matched removal.
- **Reference [10]** carried a literal `---` instead of an em dash in v3; fixed in v4.
- **PDF eXpress** conference ID **71745X**; EDAS https://edas.info/N34957; deadline **19 October 2026**. Run the PDF through eXpress before uploading — LibreOffice output is not automatically IEEE-compliant on font embedding.
