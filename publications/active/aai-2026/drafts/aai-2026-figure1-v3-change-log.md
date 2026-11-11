# Figure 1 — Change Log (v2 → v3)

**Date:** 2026-10-07
**Basis:** the Figure 1 ↔ Manuscript Consistency and Methodological Audit.
**Manuscript:** unchanged. No text, result, threshold, configuration, citation or interpretation was altered.

---

## How this was produced — read this first

No editable source for Figure 1 exists in the project. I searched the whole repository for `.svg`, `.drawio`, `.pptx`, `.ai`, `.fig` and `.vsdx` files and found none; the figure is present only as the raster PNG you uploaded. Raster images cannot be text-edited, so **v3 is a faithful reconstruction, not an edit of the v2 file.**

Layout, six-stage structure, stage numbering, colour scheme, panel order, arrow flow, the bottom grouping band and the caption are reproduced as closely as I could match them. Typography and icon rendering will differ in small ways from your original, because they come from a different drawing engine.

**If you have the original source file, that route is better than this one.** The corrections below are seven text changes; applying them in your own tool would preserve your exact styling. Send me the source and I will apply them there instead.

An editable source for v3 is included — `aai-2026-figure1-v3-source.html`. Open it in a browser, edit the text, and re-screenshot the `.wrap` element at 3× to regenerate. That gives you an editable source going forward, which the project did not have before.

---

## Corrections applied

| # | Stage | Was | Now | Audit ref |
|---|---|---|---|---|
| 1 | 6 — Denominator policy | "Departure-window only · **All hours**" | "Departure-window · **Daylight-only**" | **C-1 (Critical)** |
| 2 | 6 — Threshold configuration heading | "(sourced from **official guidelines**)" | "(**externally sourced thresholds**)" | **C-3 (Major)** |
| 3 | 2 — Component provenance | Wind / Rainfall / Ocean state shown as "(thresholds)"; Time attributed to COLREGs only | "Wind speed (sourced threshold)" · "Rainfall (sourced thresholds)" · "Ocean state (sourced threshold)" · "Time / daylight state (COLREGs boundary; night→UNSAFE researcher-defined)" | **C-2 (Major)** |
| 4 | 5 — RESOLUTION | Period not shown | "RESOLUTION (Oct 2021–Dec 2024)" with "alternative environmental-data configuration" retained beneath | **C-4 (Minor)** |
| 5 | 3, 4 — Empty set | Ø (U+00D8, capital O with stroke) | **∅ (U+2205, empty set)** in all four places: contract UNSAFE, C1, C2, C3 | **C-6 (Minor)** |
| 6 | 5 — Δ*L*₂ box | "(C₂ vs C₁)" only | "(C₂ vs C₁)" retained, plus a separated line: "Defined by (C0↔C2) − (C0↔C1); direct cross-check C1↔C2" | **C-5 (Minor)** |
| 7 | 4 — Configuration labels | C₀–C₃ subscripts rendered raised in the first build | Corrected to true subscripts | build fix, not an audit item |

Correction 6 was optional in the brief, conditional on space. It fits without crowding, so it was included — it closes the last gap between the figure's shorthand and the manuscript's formal definition of Δ<sub>L2</sub>.

---

## Deliberately unchanged

Everything the audit found aligned was left alone: the six stage titles and numbering; the stage-1 record list and the marine-warning "unavailable for replay period" note; the three-state classification output; *A*<sub>AI</sub>(*S*) notation; the SAFE / CAUTION / UNSAFE contract rows including the researcher-defined marking on {Go, Delay}; all four configurations C0–C3 with all twelve admissible-set entries; the Comparator / Isolation box; "Deterministic replay (on classified record)"; the PRIMARY block; all four record and hour counts; the 05:00–09:00 window on both configurations; the vessel classes; component attribution; the bottom grouping band; and the caption.

**Not restored, by instruction:** wave CAUTION onset, ±0.25 m, 2.54–14.75%. Verified absent.

---

## Verification — 19/19 pass

| Check | Result |
|---|---|
| "All hours" completely removed | PASS |
| "Daylight-only" present | PASS |
| "official guidelines" removed from stage 6 heading | PASS |
| Threshold provenance not overstated | PASS |
| {Go, Delay} still marked researcher-defined | PASS |
| ±0.25 m absent | PASS |
| 2.54–14.75% absent | PASS |
| "Wave CAUTION onset" absent | PASS |
| Wave UNSAFE boundary (alternative reading) retained | PASS |
| RESOLUTION period shown as Oct 2021–Dec 2024 | PASS |
| Vessel classes Small / Medium / Large | PASS |
| *A*<sub>AI</sub>(*S*) used consistently | PASS |
| All empty-set symbols are ∅ (U+2205); zero Ø (U+00D8) | PASS |
| C0–C3 match the manuscript exactly | PASS |
| C1 vs C2 isolation explicit | PASS |
| PRIMARY counts correct (43,848 / 9,135) | PASS |
| RESOLUTION counts correct (28,501 / 5,935) | PASS |
| Marine-warning exclusion explicit | PASS |
| No new scientific claim introduced | PASS |

Checked by string search against the figure source and by visual inspection of the rendered output at full resolution.

---

## Files

| File | Use |
|---|---|
| `aai-2026-figure1-v3.png` | Standalone figure, caption included. 6060 × 1704 px (≈860 dpi at 179 mm column width) |
| `aai-2026-figure1-v3-nocaption.png` | **For insertion into the manuscript.** The Word document supplies its own IEEE caption; using the captioned version would print the caption twice, which is what happened with the previous figure |
| `aai-2026-figure1-v3-source.html` | Editable source for future changes |

---

## Not done, by instruction

The manuscript was not touched. The revised `.docx` still contains the **v2** figure. Updating it is a separate step — say the word and I will swap in the no-caption v3 and re-verify the page count, which has no margin left at exactly 6 pages.
