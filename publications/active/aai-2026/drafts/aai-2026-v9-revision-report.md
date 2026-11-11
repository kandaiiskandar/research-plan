# AAI 2026 — Controlled Revision Report

**Revised manuscript:** `aai-2026-manuscript-v9-revised-A4.docx`, SHA-256 `16f31033b7efa8f43ffcc114b79dd0eb0d2afcd4465599379308890c742ba5a6`
**Rendered PDF:** `aai-2026-manuscript-v9-revised-A4.pdf`, SHA-256 `75db31a15974edd6316517dad8e73d17421c1802140b945cb85832bcab0e851b`
**Date:** 9 October 2026

> **Rendered page count: 6 pages, A4 (595.304 × 841.89 pt), two-column.** Within the verified 4–6 page limit, references included.

---

# Part 1 — Revision report

## 1.1 Baseline verification

| | |
|---|---|
| Supplied manuscript | `bc4e53e8-Rewrite_V2_conference-template-letter.docx`, 420,280 bytes |
| SHA-256 | `a29a0c27bf5b631c36ecbbaa92ecd7e7cc6cf2acabf95ef4d79c628804f41f97` |
| Against the reviewed v8 baseline | **byte-identical** (`cmp` clean) |
| Original file | copied to a read-only working path and **never written**. All edits were applied to a separate working copy of `word/document.xml`. |

## 1.2 Reconciliation of the 24-edit plan with P-1 … P-9

| | Layout correction | Disposition |
|---|---|---|
| **P-1** | Compression not mandatory for compliance | Accepted. Compression was applied only to pay for additions. |
| **P-2** | A4 at 39.70 pt side margins; do not use v4's 1-inch geometry | Applied exactly. |
| **P-3** | One uniform side-margin value across all nine `sectPr` blocks | Applied — all nine now carry identical `pgSz` and `pgMar`. |
| **P-4** | Merge compression cuts 1 and 6 | Applied as C-1 + D-12. |
| **P-5** | Narrow cuts to protect §I ¶15, §II ¶23, §VI ¶121, §III ¶61, the `<10 GRT` row | Applied. All five preserved verbatim or near-verbatim. |
| **P-6** | E-9 as prose, not a table | Applied. No third table introduced; no float reflow. |
| **P-7** | Raise the net target above −67 words | Superseded by measurement: A4 at IEEE width absorbed the additions, so the final document is **+116 words** on the baseline and still 6 pages. |
| **P-8** | M-7's conditional void; Figure 1 is 152.9 × 60.0 mm | Confirmed. Figure unchanged, same media file. |
| **P-9** | Blocker B-1 resolved | Confirmed — no blocking inconsistency was found. |

**No contradiction between the two plans was found.** One dependency was resolved during implementation: the conclusion's phrase "four-configuration comparator" became inaccurate once C3's empirical result was removed, so it was corrected (G-1), and Figure 1's caption still carried the retired "operational effect" framing, so it was aligned with the new title (G-3). Neither was in the 24-edit plan; both are consequences of E-1 and E-8.

## 1.3 Scientific edits implemented — E-1 … E-24

| ID | Section | What was done | Δ words |
|---|---|---|---|
| **E-1** | Title | "Measuring the Operational Effect of AI Governance Through…" → "**Measuring How Often an Intermediate Governance Level Binds in** Deterministic Historical Replay" | +1 |
| **E-2** | Abstract | "Under a stipulated three-state classifier," prefixed to the headline result | +5 |
| **E-3** | Abstract | added "and differing by 1.97 percentage points between two wave data products evaluated on identical hours" | +15 |
| **E-4** | §I RQ1 | reached-under-a-stipulated-classifier framing; comparator difference noted as fixed by the mappings; "denominator-policy" → "wave-data-product … evaluation-set" in both RQ1 and its restatement | +7 |
| **E-5** | §I contributions | **deleted** "the isolation of an intermediate advisory-scope level against a participation-only configuration differing from it at one state" — a construction, not a result | −17 |
| **E-6** | §I contributions | sensitivity broadened to threshold/data product/evaluation set; **two limits of the measure added** (invariance including the empty set; three-state declaration indistinguishable from a two-state gate) | +39 |
| **E-7** | §III | invariance proviso corrected: holds for **any proper subset, including the empty set**; non-emptiness is a contract property, not detected by the metric | +18 |
| **E-8** | §III, §V-A, Table II | **C3 demoted.** Its conformance paragraph replaced by the conceptual limitation; the [10]-adaptation paragraph deleted; the §V-A `C1↔C3 = 0.00%` paragraph deleted; the Table II row deleted; the caption clause removed. C3 remains *defined* in §III as the subject of the conceptual point. | −79 |
| **E-9/E-10** | §IV | **Classifier specification inserted as prose** (P-6): all ten rules — thresholds, the categorical WMO trigger, the inclusive ocean-state onset, max-severity aggregation, the fail-safe, the solar table and its coordinates | +147 |
| **E-11** | §IV | retrieval parameters: three grid cells (weather, ERA5-Ocean, MFWAM), sea cell selection, timezone | +29 |
| **E-12** | §IV | window stated as "the five hourly timestamps from 05:00 to 09:00 inclusive" | +8 |
| **E-13** | §IV | wave-band provenance: "restrictions **or cautions**" with the non-prohibitive reading adopted; [16] sets no upper boundary; neither source keyed to tonnage; band is a stipulated parameter. Transfer described as "of a length-parameterised guideline". | +49 |
| **E-14** | §V-A | **common-period comparison added**: 6.45% vs 4.48% on the 5,935 shared hours, the 1.33-point full-record gap understating it by the 0.64-point record-length offset | +44 |
| **E-15** | §V-B | sensitivity reframed to the asymmetry-proof comparison: 3.41 points on sourced wave readings against 0.48/0.78 on the widest unsourced rainfall sweep, about seven to one | +12 |
| **E-16** | §V-B | **wind inertness at sourced settings**: binds in no evaluated hour; maxima 21.80 kn and 19.30 kn against 27.0 kn | +33 |
| **E-17** | §V-C | attribution linked to the transfer assumption | +29 |
| **E-18** | §V-C | daylight-only result restated as a **denominator identity** with an invariant numerator at 531 and 266 | +27 |
| **E-20** | §VI | intermediate ocean-state band added to the researcher-defined list, with its two-source, length-not-tonnage, unvalidated status | +25 |
| **E-21** | §V-D | "RQ1 can **be answered conditionally**"; answer qualified by the stipulated classifier and the unvalidated band | +16 |
| **E-22** | §IV | repeatability clause: exactly repeatable from the archived records, which are not guaranteed re-retrievable | +25 |
| **E-24** | §VI | three-way statement — what the replay establishes, what follows by construction, what remains unvalidated | +57 |
| **E-19** | §V-A | **deferred** (would duplicate the 86.5% / 93.2% night finding) | 0 |
| **E-23** | — | **deferred** (venue requires no availability statement; repository accessibility unestablished) | 0 |

**Consequential edits not in the plan:** **G-1** conclusion "four-configuration comparator" → "a comparator that differs at one state"; **G-2** removed a duplicated "97.6%" in §V-C; **G-3** Figure 1 caption aligned with the new title; **G-4** document properties set (title, authors, keywords) replacing the IEEE template defaults.

## 1.4 Compression applied

| ID | What was compressed | Δ words |
|---|---|---|
| **C-1 / D-12** | §I mechanism survey reduced to one sentence carrying [2]–[5] plus the "contributes none of these mechanisms" disclaimer, with §II retained as the detailed treatment and itself tightened | −71 |
| **C-2** | non-claims consolidated: §I tail points to §VI, §III tail removed, §V-D trimmed. **§VI ¶121 preserved in full.** | −87 |
| **C-4 / D-10, D-11** | ladder-purpose paragraph, duplicate configuration-range disclaimer, narrow-interpretation paragraph | −34 |
| **C-5** | Table II "Period" row (duplicates §IV) | −5 |
| **C-6, D-6, D-13, D-14** | four local redundancies in §III and §V-C | −32 |
| **D-1 … D-9** | tightening of the new material: classifier prose, conclusion, band provenance, product comparison, two-readings paragraph, retrieval sentence | −97 |
| **F-1 … F-6** | §I opening [1] duplication, §I roadmap, §III figure-summary roadmap, duplicated validation disclaimer, repeatability clause, arithmetic restatement in §V-A | −121 |

**Preserved as instructed:** the literature-supported gap (§I ¶15), the functional-allocation grounding from [5] (§I ¶14, §II), the substantive comparison with [7], [8] and [9] (§II ¶23), "ΔL2 measures how often the intermediate restriction binds, not how much the recommendation set contracts" (§III), the `<10 GRT` baseline row, and §VI's validity-boundary paragraph.

## 1.5 Word and layout accounting

| | Baseline v8 | Revised v9 | Δ |
|---|---|---|---|
| Body words (excl. references) | 4,611 | **4,726** | +115 |
| Total words | 5,133 | **5,249** | +116 |
| References | 19 | **19** | 0 |
| Tables | 2 | **2** (Table II lost 2 rows) | 0 |
| Figures | 1 | **1**, unchanged | 0 |
| Page size | 612 × 792 pt (Letter) | **595.304 × 841.89 pt (A4)** | — |
| Side margins | 44.65 / 45.35 pt, two values | **39.70 pt, uniform across 9 `sectPr`** | — |
| **Pages** | **7** | **6** | **−1** |

Per-page fill of the final render: 5,330 / 6,725 / 4,720 / 6,837 / 6,482 / **7,173** characters. Page 3 is lightest because Table I and Figure 1 occupy it; page 6 carries §VI and all nineteen references and ends within the page.

---

# Part 2 — Numerical verification checklist

Every reported figure was cross-checked against the preserved canonical captures, whose hashes were re-verified as unchanged during this task:

- `data/c8/reproducibility-verification/threshold-sensitivity-20261008-stdout.txt` — `9323489a990399d0…`
- `data/c8/canonical-results-post-migration.txt` — `0bca160f69f68663…`

| Figure | Value in v9 | Source capture | Verified |
|---|---|---|---|
| PRIMARY records | 43,848 | sensitivity stdout | ✅ |
| RESOLUTION usable records | 28,501 | sensitivity stdout | ✅ |
| PRIMARY departure-window hours | 9,135 | both | ✅ |
| RESOLUTION departure-window hours | 5,935 | both | ✅ |
| Excluded wave observations | 11 | raw CSV (empty fields) | ✅ |
| PRIMARY Δ<sub>L2</sub> | 5.81% | both | ✅ |
| RESOLUTION Δ<sub>L2</sub> | 4.48% | both | ✅ |
| PRIMARY C0↔C1 | 42.88% | both | ✅ |
| RESOLUTION C0↔C1 | 41.08% | both | ✅ |
| PRIMARY C0↔C2 | 48.69% | canonical-results :223, :226 | ✅ |
| RESOLUTION C0↔C2 | 45.56% | canonical-results :257, :260 | ✅ |
| Comparator difference | 5.81 points | 48.69 − 42.88 | ✅ |
| RESOLUTION difference | 266 of 5,935 | canonical-results :251 | ✅ |
| PRIMARY CAUTION hours | 531 | canonical-results :217 | ✅ |
| RESOLUTION CAUTION hours | 266 | canonical-results :251 | ✅ |
| Ocean-state attribution | 518 (97.6%) | sensitivity stdout :19 | ✅ |
| Rainfall attribution | 13 (2.4%) | sensitivity stdout :18 | ✅ |
| Wave-boundary range PRIMARY | 5.81–9.22% | sensitivity stdout :39, :41 | ✅ |
| Wave-boundary range RESOLUTION | 4.48–6.08% | sensitivity stdout :95, :97 | ✅ |
| Wave-boundary movement | 3.41 points | 9.22 − 5.81 | ✅ |
| Alternative boundary values | 1.25 m; 1.875 m implemented as 1.90 m | script literal `(1.0, 1.9)` | ✅ |
| Rainfall sweep movement | 0.48 / 0.78 points | 6.15 − 5.67; 5.04 − 4.26 | ✅ |
| Wind sweep | no change, W<sub>C</sub> = 18–25 kn | sensitivity stdout :32–36, :88–92 | ✅ |
| Maximum window wind | 21.80 / 19.30 kn | sensitivity stdout :9, :65 | ✅ |
| Large-vessel values | 1.26% / 0.37% | sensitivity stdout :43, :99 | ✅ |
| Daylight-only denominators | 5,536 / 3,594 | sensitivity stdout :46, :102 | ✅ |
| Daylight-only rates | 9.59% / 7.40% | 531/5,536; 266/3,594 — exact quotients | ✅ |
| Non-daylight UNSAFE share | 86.5% / 93.2% | 3,389/3,917; RESOLUTION 93.19% | ✅ |
| **Common-period PRIMARY (new)** | **6.45%** | **sensitivity stdout :117** | ✅ |
| **Common-period RESOLUTION** | **4.48%** | **sensitivity stdout :118** | ✅ |
| **Product difference (new)** | **1.97 points** | 6.45 − 4.48 | ✅ |
| **Full-record gap (new)** | **1.33 points** | 5.81 − 4.48 | ✅ |
| **Record-length offset (new)** | **0.64 points** | 5.81 − 6.45 | ✅ |
| Evaluations / combinations | 78 / 56 | static enumeration of the script literals | ✅ |
| Classifier thresholds | 21.6, 27.0, 10.0, 20.0, 1.0, 1.25 | `condition_comparison.py:63, 72, 76` | ✅ |
| WMO storm codes | 95, 96, 99 | `condition_comparison.py:161` | ✅ |
| Grid cells | 5.940/116.025; 6.00/116.00; 5.958/116.042 | CSV headers; `data-provenance.md:70` | ✅ |
| Solar coordinates | 5.98 N, 116.01 E, UTC+8 | `build_solar_artefacts.py:72–73` | ✅ |

**No figure was recalculated, substituted or invented. The only number added is 6.45% (with its three derived differences), taken from the existing preserved capture.** Three figures appear in the headline-experiment capture rather than the sensitivity capture — 48.69%, 45.56% and 531 — and were traced to `canonical-results-post-migration.txt` lines 223, 257 and 217 respectively.

**Experimental integrity.** No canonical script, dataset, threshold, source capture, experiment output or verification artefact was modified. All eight canonical artefact hashes re-verified unchanged; `git status` reports **0 modified tracked files**. No experiment was run.

**Absent from v9, as required:** `C1↔C3`, `0.00%`, the "Period" row, "conformance check", and "Operational Effect of AI Governance" — all zero occurrences.

---

# Part 3 — Unresolved issues requiring author decision

## Blocking submission

**U-1 — IEEE PDF eXpress has not been run.** Conference ID **71745X**. No compliance claim is made and none can be made from here. This must be performed on the final PDF.

**U-2 — Word rendering must be confirmed.** The 6-page count comes from LibreOffice 24.2. Word's line-breaking and font metrics differ, and page 6 ends inside the page rather than with wide slack. **Open the DOCX in Word and confirm six pages before submitting.** If it spills, the cheapest reversible cuts are: drop the §V-C sentence beginning "Because the ocean-state component produces almost all" (−28 words), then the §V-A sentence beginning "The products differ" is already removed, then shorten the classifier prose by deleting its final sentence (−21 words).

**U-3 — Template compliance beyond page size.** Side margins were set to 39.70 pt to give the IEEE A4 two-column text width of 182.0 mm. I did not verify this against the official IEEE A4 template file, which the project does not hold. **Six pages is not by itself proof of template compliance.** Compare the render against the official template before submission.

## Not blocking, author's decision

**U-4 — Reference [14]'s URL appears broken.** `https://www.met.gov.my/ramalan/angin-kencang-and-laut-bergelora/` mixes English "and" into a Malay slug where the title reads "dan". **Not corrected — no invented replacement.** Please verify and fix.

**U-5 — Data/code availability statement (E-23) remains deferred.** The venue requires none, references count toward the limit, and repository accessibility is unestablished. Roughly 0.1 page of slack exists. If you want it, the short form is: *"The replay scripts, the three retrieved hourly datasets and the generated solar table are version-controlled and available from the authors on request. The reported figures are exactly repeatable from those archived inputs; re-retrieval from the provider is not guaranteed to reproduce them, as the underlying reanalysis products are subject to revision."*

**U-6 — [16] Table 12's cell label is unverified.** The publisher serves Tables 11 and 12 as images; neither the HTML nor the PDF yielded their contents. The revised §IV now says "departure restrictions or cautions … of which the non-prohibitive reading is adopted", which is accurate under either label, so **this no longer affects the text.** Obtaining the open-access PDF and holding it in `papers/sources/` would close it; the project does not currently hold the primary source for its dominant threshold.

**U-7 — MMD's operator phrasing (inclusive or strict) is unverified.** §IV now states the implementation's conventions as facts about the implementation, without attributing strictness to MMD, so no claim depends on this.

**U-8 — Two editorial items I did not change.** The author block renders correctly in the PDF — the run-together text reported earlier was an artefact of my text extraction, not a document defect, and no fix was needed. Keywords and affiliations are unchanged, as instructed.

---

## Submission-readiness statement

The manuscript is **not marked submission-ready**, because U-1, U-2 and U-3 remain open and each is outside what can be completed here. Every scientific and numerical item is complete and verified: claims are scoped to what the evidence supports, the classifier is specified to the point of exact reproducibility, all canonical results are preserved, one already-verified result was added, and the document renders at six A4 pages with nineteen references intact.

With PDF eXpress run, the Word page count confirmed and the template checked, it is ready.
