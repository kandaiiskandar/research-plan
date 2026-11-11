# AAI 2026 — Final Verification Report (v4)

**File verified:** `aai-2026-manuscript-v4-final-revised.docx` (718,549 bytes) → `.pdf` (368,460 bytes)
**Rendered by:** LibreOffice headless → PDF; text extracted with `pdftotext -layout`; XML checked directly.
**Date:** 7 October 2026

---

## 1. Page limit

| Check | Result |
|---|---|
| Rendered page count | **6** |
| Page size | 595.304 × 841.89 pt (**A4**) |
| Columns | two, IEEE conference template |
| Margin remaining | none — the paper fills page 6; any future addition must be matched by a removal |

**PASS.** Hard 6-page limit met.

---

## 2. Medium-vessel variant absent

| Check | Count in rendered PDF |
|---|---|
| "medium" (lowercase) | **0** |
| "Medium" (capitalised) | **0** |
| "1.96" | **0** |
| "0.66" (the RESOLUTION medium value) | **0** |
| "2.8 m" | **0** |
| "Medium vessels" in the embedded figure | **0** (verified visually at 400 dpi) |

**PASS.** The variant is absent from the abstract, §V-C, §VI, the figure and the table.

---

## 3. RESOLUTION decomposition reported

| Check | Result |
|---|---|
| "41.08" occurrences | **2** (§V-A text, results table) |
| "45.56" occurrences | **2** (§V-A text, results table) |
| "266 of the 5,935 evaluated hours" | **1** (§V-A) |
| `---` placeholder cells in the table | **0** |

Arithmetic check: 45.56% − 41.08% = 4.48%; 4.48% × 5,935 = 265.9 ≈ **266 hours**. Consistent.

**PASS.**

---

## 4. No stale provenance language

| String searched | Occurrences |
|---|---|
| "withheld" | **0** |
| "provenance is incomplete" | **0** |
| "not reported because" | **0** |
| stray `---` anywhere in the document | **0** |
| stray `\"` (the v2 pandoc defect) | **0** |

**PASS.** The table note no longer carries the withholding sentence, and reference [10]'s triple-hyphen is now an em dash.

---

## 5. Core results unchanged

| Quantity | v3 | v4 |
|---|---|---|
| Δ_L2 PRIMARY | 5.81% | **5.81%** |
| Δ_L2 RESOLUTION | 4.48% | **4.48%** |
| PRIMARY decomposition | 42.88% / 48.69% | **unchanged** |
| PRIMARY CAUTION hours | 531 (§V-B) | **unchanged** |
| C1↔C3 conformance | 0.00% | **unchanged** |
| Δ_L2 range under sensitivity (PRIMARY) | 5.67–9.56% | **5.67–9.56%** (4 occurrences) |
| Large-vessel configuration | 1.26% / 0.37% | **unchanged** |
| Record counts | 43,848 / 9,135 · 28,501 / 5,935 | **unchanged** |
| Departure window | 05:00–09:00 | **unchanged** |
| Declared exclusion D = {m} | present | **unchanged** |

**PASS.** No result was changed. The only numerical additions are the two RESOLUTION pairwise values and the 266-hour difference; the only numerical removals are the medium-vessel 1.96% / 0.66%.

---

## 6. Structural integrity

| Check | Result |
|---|---|
| OOXML validation (`validate.py`) | **All validations PASSED** |
| Paragraphs | 144 |
| Total words (body + references) | 4,918 |
| References in list | [1]–[19], gapless |
| References cited in text | [1]–[19] |
| Cited but not listed | **none** |
| Listed but not cited | **none** |
| Figure 1 present, spanning both columns | **yes** (page 3, verified visually) |
| Figure 1 aspect ratio | 0.2579 render / 0.2579 in XML — **not stretched** |
| Figure 1 effective resolution | ≈ 429 dpi at 7.0 in width (up from 283 dpi) |
| Duplicate caption | **none** — the caption-free render was embedded |

**PASS.**

---

## 7. Figure ↔ manuscript consistency

| Figure element | Manuscript | Agrees |
|---|---|---|
| Vessel classes: Small (baseline), Large | §V-C reports large-vessel only, baseline small | ✔ |
| Threshold configuration: "externally sourced thresholds" | §V-C | ✔ |
| Denominator policy: Departure-window · Daylight-only | §IV | ✔ |
| PRIMARY 43,848 / 9,135 | §IV | ✔ |
| RESOLUTION 28,501 / 5,935, Oct 2021–Dec 2024 | §IV, §V-A | ✔ |
| C0–C3 admissible sets | §III | ✔ |
| Marine warning excluded | §IV | ✔ |
| ∅ rendered as U+2205 (4 occurrences, 0 × U+00D8) | — | ✔ |

**PASS.**

---

## Overall

**7 / 7 verification groups PASS.** The manuscript is internally consistent, within the page limit, free of the two unresolved methodological issues, and carries no claim that the evidence does not support.
