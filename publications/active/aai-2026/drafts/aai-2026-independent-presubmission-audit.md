# Independent Pre-Submission Audit

**Manuscript:** *From Declared Risk Levels to Admissible Recommendations: Measuring the Operational Effect of AI Governance Through Deterministic Historical Replay*
**File audited:** `Rewrite_V2_conference-template-letter.pdf` — 6 pages, US Letter (612 × 792 pt), created 8 Oct 2026, all fonts embedded and subset.
**Audit date:** 8 October 2026
**Role:** independent reviewer. No manuscript text was modified. No experiment was executed.

---

## Scope and method — what was and was not done

| Method | What it covered |
|---|---|
| Arithmetic recomputation from the PDF | Every percentage, count, difference and ratio printed in the paper |
| Calendar reconstruction | Record counts and denominators against the stated study periods |
| Logical derivation from the stated mappings | The Δ<sub>L2</sub> identity, the C1↔C3 entailment, the invariance claim |
| Geometric measurement of the rendered PDF | Text block, margins, figure placement, figure label sizes, column balance |
| External source verification | All 19 references, via Crossref, DataCite, OpenAlex and publisher/agency pages |
| Astronomical computation | Sunrise at the deployment site, to test the composition of C0↔C1 |

**Not done, and not claimed:** the experiment was not re-executed. No source data, code, configuration file or log was available. Every statement below that depends on the pipeline is marked **VERIFICATION REQUIRED** and is not presented as a reproduction.

---

## A. Overall Assessment

This is a careful, unusually self-disciplined manuscript. Its epistemic hygiene is better than most conference submissions I would see: it concedes mechanism novelty outright ("This paper contributes none of these mechanisms"), it labels its own headline identity as "a metric-interpretation identity, not a result", it marks the C1↔C3 = 0.00% figure as entailed rather than empirical, it separates sourced thresholds from researcher-defined choices, and — notably — it **correctly refuses** the lower-bound interpretation of its own numbers under the marine-warning exclusion, which is the trap most papers of this kind fall into. Every arithmetic relationship I could check from the printed numbers holds exactly. No reference is fabricated; all 19 exist and every DOI resolves.

It is **not ready to submit as it stands**, for four reasons, in descending order of importance.

1. **A data-provenance problem that must be resolved either way.** The RESOLUTION configuration is stated to begin October 2021 using Copernicus product GLOBAL_ANALYSISFORECAST_WAV_001_027. No published description of that product puts its archive that early — the three sources I found give 30 Nov 2021, 1 Jun 2022 and 1 Nov 2022. Under the two later figures, eight to thirteen months of the claimed study period does not exist in the cited product. Separately, the RESOLUTION record counts do not reconcile with the stated period by 11 hours. These two findings point at the same place and must be settled before submission.

2. **The paper's most influential threshold rests on an undisclosed unit conversion.** §V-B reports that the two readings of the small-vessel wave UNSAFE boundary move the result from 5.81% to 9.22% — the largest single movement in the paper. Both are said to be "traceable to the same source [17]". Reference [17] expresses its limits as **WMO sea-state codes, not metres**, and does not quantify a failure point at all. The metre thresholds are the authors' own conversion, and the manuscript does not say so.

3. **Figure 1 is unreadable as placed.** Its labels render at approximately **3.3–3.7 pt** against IEEE's guidance that figure type "should appear approximately 9-10 point when viewed at full size". The figure also occupies only **78% of the available text width**, which is a free loss — widening it to the full 184 mm costs nothing but height, and the slack to do it already exists on page 6.

4. **No reproducibility artefact.** The paper's central methodological claim is determinism — "replaying an identical record under an identical configuration reproduces an identical result" — yet there is no data-availability statement, no code link and no configuration listing. A reviewer will ask for one, and the claim is unfalsifiable without it.

None of these is fatal. (1) and (2) are statements the authors can correct from their own records; (3) and (4) are production tasks. The scientific core — the identity, the comparator construction, the attribution — survived every check I could apply.

---

## B. Critical Findings — summary counts

| Severity | Count |
|---|---|
| **CRITICAL** | 1 |
| **MAJOR** | 7 |
| **MINOR** | 12 |
| **VERIFICATION REQUIRED** | 7 |

---

## C. Detailed Findings Table

All quotations below were extracted from the PDF text layer and verified character-for-character against it.

### CRITICAL

| ID | Severity | Page/Section | Exact Original Text | Problem | Evidence / Reasoning | Recommended Minimal Fix |
|---|---|---|---|---|---|---|
| **C-1** | CRITICAL | p.4, §IV | "The RESOLUTION configuration covers October 2021 to December 2024, comprising 28,501 hourly records with wave data from MFWAM [11] at approximately 8 km resolution, giving a denominator of 5,935 hours." | The cited wave product's documented archive does not reach back to October 2021, and the record counts do not reconcile with the stated period. | Copernicus product `GLOBAL_ANALYSISFORECAST_WAV_001_027` (the product behind DOI 10.48670/moi-00017) is a near-real-time analysis/forecast product. Three independent descriptions give its coverage start as **2021-11-30** (CMEMS/FEDEO metadata), **2022-06-01** (Google Earth Engine catalogue) and **1 Nov 2022** (Copernicus product page). All three are after October 2021; two are more than seven months after. Separately: 1 Oct 2021 – 31 Dec 2024 inclusive is 1,188 days = **28,512** hours, not 28,501 (deficit 11), and 1,188 × 5 = **5,940** window hours, not 5,935 (deficit 5). The two deficits are mutually consistent with a record beginning at **11:00 on 1 Oct 2021** — which would explain the arithmetic but not the product coverage. | State the exact first and last timestamps of the RESOLUTION record, and state which archive endpoint and product version supplied the wave data for the period before the cited product's documented start. If the data came through Open-Meteo's own blend rather than directly from CMEMS, say so and cite accordingly. |

### MAJOR

| ID | Severity | Page/Section | Exact Original Text | Problem | Evidence / Reasoning | Recommended Minimal Fix |
|---|---|---|---|---|---|---|
| **M-1** | MAJOR | p.4, §IV | "the ocean-state CAUTION onset follows the departure restriction proposed for vessels under 10 m by [16] and the UNSAFE boundary follows the operational ceiling reported by [17]" — and p.5, §V-B: "The small-vessel wave source supports two defensible readings of the UNSAFE boundary, an operational ceiling and a failure point, which give 5.81% and 9.22% respectively. Both are traceable to the same source [17]" | [17] does not report a metre-valued ceiling, and does not quantify a failure point. The conversion is the authors' and is undisclosed. | Yaakob *et al.* (2015), verified in full text at jssm.umt.edu.my, expresses its limits as **WMO sea-state codes**: Boat A "should only operate in sea states up to sea state condition 3", Boat B "only … sea state condition 2". Capsize is discussed qualitatively; **no failure wave height is given in metres**. Any metre threshold is a conversion from a sea-state band, and which end of the band is taken (midpoint vs upper limit) changes the number materially. This is the threshold the paper itself identifies as producing "the largest movement among the sourced threshold settings". | One sentence in §IV: state that [17] reports WMO sea-state limits and give the conversion used (band and endpoint) for both readings. Change "reported by [17]" to "derived from the sea-state limits reported by [17]". |
| **M-2** | MAJOR | p.3, §III | "the value of Δ<sub>L2</sub> is invariant to the content of A<sub>AI</sub>(CAUTION), provided that set remains a strict subset of FULL" | ∅ is a strict subset of FULL, so the stated condition admits the empty set — and the metric is then invariant to the difference between an *active contracted* set and *withdrawal of participation*. That difference is exactly what the paper uses to distinguish itself from [9]. | §II positions the contribution against Kim *et al.*: "that zone withdraws automated action rather than retaining an active contracted recommendation set." But setting A<sub>AI</sub>(CAUTION) = ∅ leaves C0↔C2 = P(CAUTION) + P(UNSAFE) unchanged and therefore Δ<sub>L2</sub> unchanged. The metric cannot see the property the positioning turns on. This is a genuine logical gap, not a reviewer preference. | Change "strict subset" to "non-empty strict subset" in the invariance sentence, and add one clause to §VI noting that Δ<sub>L2</sub> does not distinguish an active contraction from a withdrawal at the intermediate state. |
| **M-3** | MAJOR | p.4, §V-A; Table II | "C0↔C1 gave 42.88%, the frequency associated with participation gating alone" | The quantity presented as "participation gating" is dominated by a researcher-defined time rule, not by environmental severity, and the paper never says so. | Δ<sub>L2</sub> ≡ P(CAUTION) implies C0↔C1 = P(UNSAFE). The evaluation window is 05:00–09:00 (5 hours/day) and non-daylight hours are classified UNSAFE by a policy the paper itself calls researcher-defined. Computed sunrise at Kota Kinabalu (5.98 °N, 116.07 °E, UTC+8) ranges **05:59 to 06:32** across the year, so under an hour-start convention the 05:00 and 06:00 hours are pre-sunrise on 348 of 365 days: **2/5 = 40.0%** of window hours are definitionally UNSAFE. Reported C0↔C1 is 42.88% (PRIMARY) and 41.08% (RESOLUTION). **This does not affect Δ<sub>L2</sub>**, which is independent of the UNSAFE count — it affects how the decomposition reads. | One sentence in §V-A noting that the C0↔C1 magnitude is governed principally by the non-daylight policy applied to a window that opens before sunrise, and is therefore not an environmental-severity measure. |
| **M-4** | MAJOR | p.3, Figure 1 | (figure labels) | Figure 1's text renders at roughly 3.3–3.7 pt and cannot be read at normal viewing size. | Measured from the PDF: the image is placed at **406.95 × 167.76 pt (143.6 × 59.2 mm)**, clipped to 159.8 pt height. Measuring ink-row extents of individual label lines in panel 6 at 600 dpi gives 2.16–3.72 pt; converting from the figure's own design grid gives body labels ≈ **3.74 pt**, sub-notes ≈ **3.26 pt**, panel titles ≈ **5.00 pt**. IEEE's conference guidance states type "should appear approximately 9-10 point when viewed at full size". | See M-5; and if full width is still not enough, reduce the figure's content rather than its type size. |
| **M-5** | MAJOR | p.3, Figure 1 | (figure placement) | The figure uses only 78% of the available width — a free loss of legibility. | Measured text block: **184.0 mm** wide (left margin 16.0 mm, right 15.9 mm), matching the IEEE US Letter template (0.62 in margins, 2 × 3.5 in columns + 0.25 in gutter = 184.15 mm). The figure is placed at 143.6 mm = **78%**. Widening to 184.0 mm scales every label by **1.28×** (body ≈ 4.8 pt, titles ≈ 6.4 pt) at a height cost of 56.4 → 72.3 mm, i.e. +15.9 mm of full-width space = 90 pt of column length. Measured free column length at the foot of page 6: **93.4 pt** (left column 43.7 pt, right 49.7 pt). It fits, with 3.4 pt to spare. | Place the figure at the full 184 mm text width. If the 3.4 pt margin is uncomfortable, pair it with F-1 below, which frees ~173 pt. |
| **M-6** | MAJOR | p.4, §IV | "No parameter is estimated from the data and no randomisation is involved, so replaying an identical record under an identical configuration reproduces an identical result." | The paper's central methodological claim is determinism, but no artefact is provided by which anyone could test it. | There is no data-availability statement, no repository link, no configuration listing and no threshold table in the paper. A string search for "github", "zenodo", "repository", "availability", "supplementary" returns nothing in the body. Determinism is the one claim here that is cheap to substantiate and impossible to check without the artefact. | Add a one-line availability statement with a DOI-bearing archive (the paper already cites Zenodo for [12], so the mechanism is familiar to the authors). |
| **M-7** | MAJOR | p.4, §IV | "The day boundary follows COLREGs Rule 20(b) [18]." | Rule 20(b) is a lighting obligation, not a definition of day. | Rule 20(b) verbatim: "The Rules concerning lights shall be complied with from sunset to sunrise, and during such times no other lights shall be exhibited…". It imposes a duty keyed to sunset/sunrise; it does not define a day/night state. Rule 20(c) cuts further against a clean split, since lights are also required from sunrise to sunset in restricted visibility. Figure 1 is more careful than the text here, labelling it "COLREGs boundary; night→UNSAFE researcher-defined". | Change to "The day boundary is taken from the sunset-to-sunrise trigger in COLREGs Rule 20(b) [18]", bringing the text in line with the figure. |

### MINOR

| ID | Severity | Page/Section | Exact Original Text | Problem | Evidence / Reasoning | Recommended Minimal Fix |
|---|---|---|---|---|---|---|
| **N-1** | MINOR | p.3, Table I | "G is determined by emptiness of A<sub>AI</sub> and is shown for readability only." | **G is never defined anywhere in the paper.** The footnote says how it is computed but never says what it denotes. | A full-text search for a definition of G returns only the table header and this footnote. A reader cannot tell whether G is a gate indicator, a participation flag or something else. | Either define G in one clause, or delete the column — the footnote already concedes it carries no information. |
| **N-2** | MINOR | p.5, Table II | "2021-10–2024" | Malformed and internally inconsistent date format. | The PRIMARY cell reads "2020–2024" (years), the RESOLUTION cell mixes an ISO year-month with a bare year across an en dash. The body text says "October 2021 to December 2024". | Set both cells to the same granularity, e.g. "Jan 2020 – Dec 2024" and "Oct 2021 – Dec 2024". |
| **N-3** | MINOR | p.1, Abstract | "deterministic historical replay over five years of hourly environmental records" | Only PRIMARY covers five years; RESOLUTION covers 3.25 years, and the abstract reports both. | PRIMARY = 1,827 days = 5.00 years. RESOLUTION as stated = 1,188 days = 3.25 years. | "over up to five years of hourly environmental records", or name the two periods. |
| **N-4** | MINOR | p.5 §V-C vs p.6 §VI | "cannot be interpreted as lower bounds" (p.5) vs "are not necessarily lower bounds" (p.6) vs "should not be interpreted as lower bounds" (p.1, p.4) | Three different modal strengths for the same claim; one of them is too strong. | The supporting argument shows that "CAUTION occupancy alone may increase or decrease" — which licenses "not necessarily a lower bound", not "cannot be". The p.5 wording asserts more than the argument delivers. | Use "are not necessarily lower bounds" in all four places. |
| **N-5** | MINOR | p.2, §III | "Measuring that combination requires the governed object to be stated explicitly." | Dangling antecedent. "That combination" refers to the last sentence of §II, but a section heading and the Fig. 1 summary paragraph intervene. | §II ends "…do not combine active intermediate scope contraction, a participation-only comparator, marginal isolation, and binding-frequency measurement." The referent is two paragraphs and one heading away. | "Measuring that combination of properties…" or restate the referent in three words. |
| **N-6** | MINOR | §I and §II | (see Evidence) | References [1]–[5] are each described twice, once in the Introduction and once in Background, in different words but with identical content. | Verified by position: [1], [2], [3], [4] each appear exactly twice in the body; [5] appears four times. There is **no verbatim overlap** (zero shared 6-grams), so this is deliberate re-wording, not copy-paste — but it is the same five facts delivered twice. The shorter of the two blocks is **125 words ≈ 16 column lines ≈ 173 pt of column length**. | Keep the §II treatment (which does the positioning work) and compress the §I version to a single sentence naming the four precedents. This also pays for M-5. |
| **N-7** | MINOR | p.3, §III | "Δ = (N<sub>restricted</sub> / N<sub>eval</sub>) × 100%" where N<sub>restricted</sub> is "the number of those hours in which one configuration admits a strictly smaller set than another" | A directional definition ("strictly smaller than") carried by a symmetric notation ("C0↔C1"). | The definition is well-posed only when the two admissible sets are nested. All four configurations here are nested, so no error arises — but the metric would silently return 0 for two configurations whose sets are incomparable. | Add "(the mappings compared here are nested, so the relation is well defined)" or state the ordered pair explicitly. |
| **N-8** | MINOR | Equations, §III | three displayed equations | None is numbered. | IEEE style numbers displayed equations consecutively. None is cross-referenced in the text here, so nothing breaks, but it is a deviation from the template. | Number them (1)–(3). |
| **N-9** | MINOR | Reference [10] | "in Proc. IECON 2024 — 50th Annu. Conf. IEEE Ind. Electron. Soc., 2024." | Page numbers missing, unlike every other conference reference. | OpenAlex records pp. **1–8**. | Add "pp. 1–8". |
| **N-10** | MINOR | p.4, §IV | "with wave data from MFWAM [11] at approximately 8 km resolution" | Resolution understated. | The product grid is 1/12° = 0.083°, which Google Earth Engine records as **9,276.62 m ≈ 9.3 km**. | "approximately 9 km". |
| **N-11** | MINOR | p.4, §IV | "with wave data from ERA5-Ocean at approximately 50 km resolution" | "ERA5-Ocean" is not an official product name. The ~50 km figure is, however, correct. | CDS serves ERA5 ocean-wave variables on a 0.5° grid ≈ 55 km (native wave grid 0.36° ≈ 40 km), as distinct from the 0.25° atmospheric grid. So "approximately 50 km" is defensible and is correctly distinguished from the atmosphere. Only the product name is non-standard. | "ERA5 ocean-wave fields". |
| **N-12** | MINOR | Reference [12] | "P. Zippenfenig, 'Open-Meteo.com weather API,' Zenodo, 2023." | Year may be wrong. | DOI 10.5281/zenodo.7970649 is the concept DOI; DataCite reports `publicationYear` **2024** for the resolved version (v1.4.0, 31 Dec 2024). 2023 is widely cited but I could not confirm it from the record. | Confirm against the author's own recommended citation string. |

### VERIFICATION REQUIRED

| ID | Page/Section | Exact Original Text | What cannot be checked from the PDF | Why it matters |
|---|---|---|---|---|
| **V-1** | p.5, §V-C | "The ocean-state component accounted for 518 of those 531 hours, or 97.6%, and the rainfall component for the remaining 13, or 2.4%." | The tie-breaking rule. Classification is "using the maximum severity among the available component classifications"; when two components reach CAUTION in the same hour, the manuscript does not say which receives the attribution. 518 + 13 = 531 exactly, so a single-attribution rule was applied, but it is unstated. | 97.6% is a headline number. Its meaning depends entirely on the unstated rule. **Arithmetic verified**: 518/531 = 97.5518% → 97.6% ✓; 13/531 = 2.4482% → 2.4% ✓. |
| **V-2** | p.4, §IV | "the canonical sensitivity script evaluates 56 distinct combinations of environmental-data configuration, threshold setting and denominator policy, of which this paper reports a subset" | The factorisation. 56 = 2 data configurations × 2 denominator policies × 14 threshold settings is the natural reading, but the 14 settings are never enumerated. | A reviewer cannot judge whether the reported subset is representative or selected. |
| **V-3** | p.5, §V-B | "Δ<sub>L2</sub> spans 5.67–9.56% in PRIMARY and 4.26–6.64% in RESOLUTION" alongside "which give 5.81% and 9.22% respectively" | How the envelope endpoints arise. 9.56 > 9.22 and 5.67 < 5.81, so neither endpoint is one of the two wave readings, and neither is reachable by adding the stated rainfall movement (9.22 + 0.48 = 9.70; 5.81 − 0.48 = 5.33). | The envelope is quoted in the abstract and conclusion. Its derivation is not reconstructible. **Consistency verified**: both baselines lie inside their envelopes. |
| **V-4** | p.5, §V-C | "Replacing the departure-window denominator with a daylight-only denominator raises it to 9.59% in PRIMARY and 7.40% in RESOLUTION." | The daylight-only denominators themselves. | **Internally consistent**: 531/0.0959 = 5,537 h = 60.6% of the 9,135-hour window; 266/0.0740 = 3,595 h = 60.6% of the 5,935-hour window. The two independently implied daylight fractions agree to one decimal place, which is a strong sign the figures are genuine. |
| **V-5** | p.5, §V-B | "Varying the rainfall CAUTION boundary moves Δ<sub>L2</sub> by 0.48 percentage points in PRIMARY and 0.78 in RESOLUTION" and "The wind boundary is a structural zero across the evaluated range W<sub>C</sub> = 18–25 kn" | Both require the sensitivity run. | Not checkable without the artefact (M-6). |
| **V-6** | Reference [8] | "Miller evaluates alternative enforcement operators, including an ungoverned baseline, approval-only gating and projection-based repair, through systematic ablation [8]." | Whether the source uses an *ungoverned baseline* and a *systematic ablation*. | The MDPI abstract confirms "Projection-based repair consistently outperforms approval-only strategies", but the terms "ungoverned baseline" and "ablation" appear nowhere in the retrievable text. The reference itself is correct in every bibliographic field, and is correctly cited as single-author. |
| **V-7** | Whole document | — | Whether AAI 2026 requires A4 rather than US Letter, and whether the IEEE copyright notice should be present at submission. | The file is US Letter. Its geometry matches the IEEE US Letter template exactly (measured: top 19.0 mm, bottom 25.6 mm, left 16.0 mm, right 15.9 mm, text block 184.0 × 234.7 mm). The copyright notice is absent, which is normal for review submission but must be added for camera-ready. Both are conference-policy questions, not defects. |

---

## D. Numerical and Mathematical Verification

### D.1 The Δ<sub>L2</sub> identity — derived independently and confirmed

From the mappings printed in Fig. 1, with Δ counting hours on which one configuration admits a strictly smaller set:

| Pair | States at which they differ | N<sub>restricted</sub> |
|---|---|---|
| C0 ↔ C1 | UNSAFE only (FULL vs ∅) | #UNSAFE |
| C0 ↔ C2 | CAUTION and UNSAFE | #CAUTION + #UNSAFE |

Therefore Δ<sub>L2</sub> = (C0↔C2) − (C0↔C1) = #CAUTION / N<sub>eval</sub> = **P(S = CAUTION)**. ✔ The identity holds exactly as claimed, and follows from the mappings alone, not from the data.

**Corollary the paper does not state, and should:** C0↔C1 ≡ P(S = UNSAFE). This is what makes M-3 checkable.

### D.2 C1↔C3 = 0 by construction

C1 and C3 are printed with identical admissible sets at all three states (SAFE: FULL, CAUTION: FULL, UNSAFE: ∅). Under the stated criterion they denote the same governance function, so the count is zero for every record. ✔ Correctly described as "the entailed result rather than an empirical finding". No overclaim.

### D.3 Arithmetic — every printed relationship

| Claim | Recomputation | Result |
|---|---|---|
| 48.69 − 42.88 = 5.81 | exact | ✔ |
| 45.56 − 41.08 = 4.48 | exact | ✔ |
| PRIMARY hours: 42.88% × 9,135 = 3,917.1; 48.69% × 9,135 = 4,447.8 | difference 530.7 ≈ **531** | ✔ matches the 531 CAUTION hours reported in §V-C |
| 531 / 9,135 | 5.8128% → **5.81%** | ✔ identity confirmed against the data |
| RESOLUTION hours: 41.08% × 5,935 = 2,438.1; 45.56% × 5,935 = 2,704.0 | difference 265.9 ≈ **266** | ✔ matches "a difference of 266 of the 5,935 evaluated hours" |
| 266 / 5,935 | 4.4819% → **4.48%** | ✔ |
| 518 / 531 | 97.5518% → **97.6%** | ✔ |
| 13 / 531 | 2.4482% → **2.4%** | ✔ |
| 518 + 13 | **531** | ✔ complete partition |
| Envelope contains baseline | 5.67 ≤ 5.81 ≤ 9.56; 4.26 ≤ 4.48 ≤ 6.64 | ✔ both |
| Both wave readings inside envelope | 5.67 ≤ 5.81, 9.22 ≤ 9.56 | ✔ |
| Large-vessel implied hours | 1.26% × 9,135 = 115.1 h; 0.37% × 5,935 = 22.0 h | plausible |
| Daylight-only implied denominators | 5,537 h (60.6% of window) and 3,595 h (60.6% of window) | ✔ agree to 0.1 pp — strong internal evidence |

**Every arithmetic claim in the manuscript checks out.** That is worth saying plainly.

### D.4 Calendar reconstruction — where it fails

| Configuration | Stated period | Days | Expected hours | Printed | Δ |
|---|---|---|---|---|---|
| PRIMARY | 1 Jan 2020 – 31 Dec 2024 | 1,827 | 43,848 | **43,848** | **0** ✔ |
| PRIMARY window | 5 h/day | 1,827 | 9,135 | **9,135** | **0** ✔ |
| RESOLUTION | 1 Oct 2021 – 31 Dec 2024 | 1,188 | 28,512 | **28,501** | **−11** ✘ |
| RESOLUTION window | 5 h/day | 1,188 | 5,940 | **5,935** | **−5** ✘ |

PRIMARY reconstructs exactly, which shows the method is sound and makes the RESOLUTION mismatch conspicuous. 5,935 = 5 × 1,187 exactly, i.e. **exactly one day's window is missing**; 28,501 = 28,512 − 11. Both are reconciled by a record starting at **11:00 on 1 Oct 2021** (13 hours on day one, that day's 05:00–09:00 window absent). This is consistent arithmetic, but it is not stated, and it does not resolve the product-coverage question in C-1.

### D.5 Sunrise computation supporting M-3

NOAA solar-position algorithm, 5.9804 °N, 116.0735 °E, UTC+8, all 365 days:

- earliest sunrise **05:59**, latest **06:32**
- sunrise falls inside the 06:00 hour on **348 of 365 days**
- the 05:00 hour is pre-sunrise on every day of the year

Under an hour-start convention, **2 of the 5 window hours (40.0%) are UNSAFE by the non-daylight policy alone**, against a reported C0↔C1 of 42.88% / 41.08%.

### D.6 Geometry of the rendered PDF

| Measurement | Value | IEEE US Letter template |
|---|---|---|
| Page size | 612 × 792 pt | ✔ Letter |
| Top margin | 19.0 mm | 0.75 in = 19.05 mm ✔ |
| Bottom margin | 25.6 mm | 1.0 in = 25.4 mm ✔ |
| Left / right margin | 16.0 / 15.9 mm | 0.62 in = 15.75 mm ✔ |
| Text block | 184.0 × 234.7 mm | 184.15 × 234.95 mm ✔ |
| Column leading | 10.80 pt | ✔ |
| Lines per column | 56 | — |
| Figure 1 placed size | 143.6 × 59.2 mm (clipped to 56.4 mm) | **78% of available width** |
| Figure 1 raster | 1,243 × 513 px → **220 dpi** effective | IEEE accepts PS/EPS/PDF/PNG/TIFF; a line drawing of this kind is better supplied as vector |
| Free column length, p.6 | 43.7 + 49.7 = **93.4 pt** | — |

The template implementation is correct. No placeholders, no broken glyphs, no clipping or overlap; typographic characters are properly used throughout (U+2013 en dash ×16, U+2212 minus ×2, U+2261 ≡, U+2205 ∅, diacritics preserved in "Könighofer" and "González"). Table I and Table II both use correct IEEE rule structure and small-caps captions.

---

## E. Reference Verification

**All 19 references exist. Every DOI resolves. Nothing is fabricated.** This is the cleanest reference list I have audited on a paper of this kind, and the three highest-risk items (two 2026 conference/journal papers and an odd-looking DOI) all survived scrutiny.

| Ref | Exists | Bibliographic fields | Supports the attributed claim | Note |
|---|---|---|---|---|
| [1] NIST AI RMF 1.0 | ✔ | all correct | ✔ confirmed near-verbatim against the MEASURE function | — |
| [2] ASTM F3269-21 | ✔ | all correct — official title really is "Aircraft Systems"/"Behavior" (no "Unmanned", no "Flight"); F3269-21 is the active revision | plausible; "independently assured" wording not visible outside the paywall | UNVERIFIED on that one phrase |
| [3] Alshiekh *et al.*, AAAI-18 | ✔ | author order and **pp. 2669–2678 confirmed** from the proceedings PDF | ✔ paper's own terms are "preemptive"/"post-posed"; substance matches | — |
| [4] FAA AC 20-151C | ✔ | 2017-07-21, Active, current revision; no 20-151D exists | ✔ confirmed from the AC's graduated inhibit tables and §2.1.1 pilot-authority wording | — |
| [5] Parasuraman *et al.* 2000 | ✔ | every field matches Crossref | cannot tell — IEEE Xplore and doi.org both refused access | claim is highly plausible but UNVERIFIED |
| [6] Batool, Zowghi & Bano | ✔ | all correct | ✔ conclusions state the who/what/when gap; 3 of 28 studies answered all four questions | — |
| [7] Aarab, ICHCAI 2026 | ✔ | all correct; **genuinely single-author** (Hamza Aarab), conference independently verified (IFE Halden, 27–28 May 2026) | cannot tell — no abstract in Crossref or OpenAlex, Xplore unreadable | the body's "Aarab specifies…" without "et al." is **correct** |
| [8] Miller, MAKE 8(5) art. 125 | ✔ | all correct; **genuinely single-author** (Tymoteusz Miller) | partial — abstract confirms projection-based repair vs approval-only; "ungoverned baseline" and "ablation" not found | see V-6 |
| [9] Kim *et al.*, npj Digit. Med. | ✔ | 7 authors in exactly the cited order; **the "026" DOI is the real one** — the plausible-looking "025" variant 404s | ✔ confirmed: SA-ROC, mandated-review Gray Zone, Γ<sub>Area</sub> workload metric, α = 90/95/100%, 1,000 real screening mammograms | do **not** "correct" the DOI |
| [10] Flehmig *et al.*, IECON 2024 | ✔ | correct except **missing pp. 1–8** | ✔ abstract confirms a traffic-light degradation-indexing framework conditioned on AI degradation | "three-state" inferred from "traffic-light", not read in the body |
| [11] CMEMS MFWAM | ✔ | DOI ↔ product confirmed | ✘ **temporal coverage and resolution both contradicted** | see C-1 and N-10 |
| [12] Zippenfenig, Zenodo | ✔ | author and title correct; **year unconfirmed** (DataCite says 2024) | n/a | see N-12 |
| [13] ERA5 single levels | ✔ | DOI correct; dataset does carry ocean-wave variables | ✔ the ~50 km attribution is defensible (0.5° delivered wave grid ≈ 55 km) | author string and year unverified; "ERA5-Ocean" non-standard |
| [14] MMD strong wind | ✔ URL resolves | **the odd-looking "-and-" path is the real one**; the "dan" variant 404s | n/a | do **not** "fix" this URL |
| [15] MMD thunderstorm | ✔ URL resolves | correct; criteria are >20 mm/h | n/a | — |
| [16] Jeong & Im, JMSE 11(7) 1302 | ✔ | all fields correct | ✔ the paper does propose departure restriction/caution for vessels under 10 m at significant wave height ≥ 1 m | — |
| [17] Yaakob *et al.*, JSSM 10(1) | ✔ | all fields correct, full text located | ✘ **limits are WMO sea-state codes, not metres; no failure point is quantified** | see M-1 — the most consequential citation issue in the paper |
| [18] IMO COLREGs Rule 20(b) | rule text verified via IALA; IMO URL blocked by robots.txt, not shown dead | — | ✘ over-read: a lights obligation, not a day/night definition | see M-7 |
| [19] DID Public Infobanjir | ✔ live, last updated 08/10/2026 | correct | ✔ publishes Light 1–10 mm/h, Moderate 11–30, Heavy 31–60, Very heavy >60 | — |

**Checks that could not be performed:** full text of [2] (ASTM paywall), [5] (IEEE Xplore access refused), [7] (IEEE Xplore unreadable), [8] results sections (MDPI HTML truncated), [10] body text. Direct HTTP fetching outside the permitted tooling was not attempted.

**Missing references that could challenge the gap:** I did not find one. The gap statement is scoped to "the reviewed literature" and the three closest works ([7], [8], [9]) are each engaged specifically and fairly. That said, see Objection 1 below — the problem with the gap is its construction, not an omitted citation.

---

## F. Top Five Reviewer Objections

**1. "Your headline number is the base rate of a classifier you designed."**
Δ<sub>L2</sub> ≡ P(S = CAUTION) is an identity, and the CAUTION state is defined by thresholds the authors chose. The entire four-configuration apparatus produces a quantity obtainable by counting CAUTION hours — which the paper concedes ("the comparator ladder is not required to compute it"). The defence offered is that the ladder "establishes the identity rather than assuming it" and supplies a cross-check. A reviewer may accept that as methodological hygiene, or may conclude the contribution reduces to reporting a threshold-induced base rate at one site. **This is the objection the paper must survive**, and its current defence is one paragraph.

**2. "Your metric cannot see the thing you say is novel."**
§II distinguishes the work from [9] on the grounds that this intermediate zone retains "an active contracted recommendation set" rather than withdrawing automated action. But §III states that Δ<sub>L2</sub> is invariant to the content of A<sub>AI</sub>(CAUTION) for any strict subset of FULL — and ∅ is a strict subset. Setting A<sub>AI</sub>(CAUTION) = ∅ turns C2 into a two-state participation gate and leaves Δ<sub>L2</sub> unchanged. See M-2. This is the sharpest *technical* objection available, and it is currently unaddressed.

**3. "The gap is defined into existence."**
"Within the reviewed literature, no empirical characterisation was identified of how often an intermediate advisory-scope level changes the admissible recommendation set relative to a participation-only gate when replayed over a multi-year environmental record." Every conjunct is defensible, but a conjunction of five specific properties is unexplored almost by construction. The hedging ("within the reviewed literature", "was identified") is good practice and will help; the underlying structure will still be challenged.

**4. "The title promises more than the paper delivers."**
"Measuring the Operational Effect of AI Governance" is measured by one binding frequency, of one researcher-defined contraction, at one site, for one vessel class, over a window the authors chose, with one of five state components structurally excluded. The body is scrupulous about all of this; the title is not. Combined with M-3 — that the companion quantity C0↔C1 is largely a definitional artefact of the time rule — a reviewer may feel the framing outruns the evidence even though no individual sentence does.

**5. "I cannot check any of this."**
No data, no code, no configuration listing, no threshold table, no record of the 56 combinations, no attribution tie-breaking rule. For a paper whose methodological claim is exact reproducibility, the absence of an artefact is conspicuous. See M-6, V-1, V-2, V-3, V-5.

---

## G. Final Submission Checklist

**Must resolve before submission**

- [ ] **C-1** — State the exact first/last timestamps of the RESOLUTION record and reconcile them with the cited wave product's documented coverage start. If the data arrived via Open-Meteo's blend rather than CMEMS directly, cite that.
- [ ] **M-1** — Disclose the WMO sea-state → metre conversion behind both readings of the small-vessel UNSAFE boundary; change "reported by [17]" to "derived from".
- [ ] **M-2** — "non-empty strict subset"; add one clause acknowledging Δ<sub>L2</sub> does not distinguish contraction from withdrawal.
- [ ] **M-6** — Add a data/code availability statement.

**Should resolve**

- [ ] **M-3** — One sentence noting that C0↔C1's magnitude is governed by the non-daylight policy applied to a pre-sunrise window.
- [ ] **M-4 / M-5** — Place Figure 1 at the full 184 mm text width; supply it as vector (PDF/EPS) rather than a 220 dpi raster. Fits within the 93.4 pt of free column length on page 6, with 3.4 pt to spare.
- [ ] **M-7** — Soften the COLREGs Rule 20(b) attribution to match Figure 1's own wording.
- [ ] **N-6** — Compress the duplicated §I treatment of [1]–[5] to one sentence; frees ~173 pt, which makes M-5 comfortable rather than marginal.
- [ ] **N-1** — Define or delete the G column in Table I.

**Tidy-ups**

- [ ] **N-2** Table II period formats · **N-3** "five years" in the abstract · **N-4** one modal form for the lower-bound disclaimer · **N-5** "that combination" antecedent · **N-7** nestedness note on Δ · **N-8** number the equations · **N-9** add pp. 1–8 to [10] · **N-10** ~9 km not ~8 km · **N-11** "ERA5 ocean-wave fields" · **N-12** confirm [12]'s year

**Confirm against the AAI 2026 call for papers**

- [ ] Page size: the file is US Letter. If A4 is required, re-render — the two templates have different text blocks (184.0 × 234.7 mm vs 184.15 × 234.95 mm), so page count must be re-verified after any change.
- [ ] IEEE copyright notice: absent, which is normal for review submission; must be added for camera-ready.
- [ ] Six-page limit including references: **met** (6 pages, columns on page 6 balanced to within 6 pt).
- [ ] Corresponding-author email on page 1 — author to self-check.

**Do not "fix" these — they are already correct**

- Reference [9]'s DOI middle segment "026" (the "025" variant does not exist).
- Reference [14]'s URL containing "-and-" (the "dan" variant 404s).
- Reference [2]'s title wording "Aircraft Systems … Behavior" (no "Unmanned", no "Flight").
- "Aarab specifies" and "Miller evaluates" without "et al." — both sources are genuinely single-author.
- The "approximately 50 km" attribution for ERA5 wave data.

---

## Where no change is required

Stated explicitly, per the audit rules:

- **The marine-warning treatment is correct and needs no change.** The manuscript establishes that max-severity aggregation means "CAUTION-or-higher activation cannot decrease when the excluded component is restored", then correctly observes that "CAUTION occupancy alone may increase or decrease", and therefore declines the lower-bound reading. This is the right analysis, and it is rarer than it should be.
- **The C1↔C3 = 0.00% treatment is correct.** It is labelled entailed, not empirical, and the paper explicitly declines the inference that three-state designs are ineffective.
- **The separation of governance activation from safety outcomes is thorough** and I found no sentence that breaches it. §VI's enumeration of what is not established is accurate and complete.
- **The statistical abstinence is correct.** "No sampling inference is performed, and no p-values, confidence intervals or significance claims apply" is consistent with a deterministic census, and the ranges are correctly labelled "deterministic configuration ranges" in all four places they appear.
- **All arithmetic is correct.** No numerical correction is recommended anywhere in this audit.
- **The reference list is sound.** No reference should be removed or replaced.
