# AAI 2026 — Figure 1 ↔ Manuscript Consistency and Methodological Audit

**Manuscript audited:** `aai-2026-manuscript-v2-revised.docx` / `.pdf` (6 pages, A4, IEEE two-column)
**Figure audited:** Figure 1, revised version supplied 2026-10-07
**Date:** 2026-10-07
**Authority:** the manuscript, for all definitions, equations, results and claim boundaries.

Nothing was modified. This is a report only.

---

# PART A — Executive verdict

## **Publication-ready after minor corrections**

The revision closed four of the five figure/text mismatches raised in the previous audit. A<sub>AI</sub>(S) notation is now correct, the vessel classes are now small/medium/large, the wave CAUTION onset bullet has been replaced by the wave UNSAFE boundary alternative reading, and "RESOLUTION (subset)" is now "alternative environmental-data configuration". The figure also now marks {Go, Delay} as a researcher-defined strict subset, which answers the supervisor's provenance point directly on the page where the contract is shown. The manuscript body is clean: every trace of the ±0.25 m perturbation is gone, Table II is removed with no stale reference and no lost definition, all numbers reconcile, and the claim boundaries hold.

**One new error was introduced by the figure update, and it is not cosmetic.** Box 6 now lists a denominator policy of *"Departure-window only · All hours"*. The manuscript evaluates departure-window versus **daylight-only** (9.59% PRIMARY, 7.40% RESOLUTION). The string "all hours" appears nowhere in the manuscript, and no result exists for it. This is worse than a mislabel: an all-hours denominator would *include* the night hours that the time component classifies UNSAFE, which would push the proportion **down**, whereas the daylight-only denominator removes them and pushes it **up** to 9.59%. The figure therefore advertises a condition that was never run and whose direction of effect is opposite to the one that was.

Two further issues concern provenance, which is the supervisor's stated concern. Box 6's heading *"Threshold configuration (sourced from official guidelines)"* covers the wave UNSAFE boundary, which the manuscript sources to a peer-reviewed journal paper [16], not to an official guideline. And box 2 presents the wind, rainfall, ocean and time thresholds with no provenance marking at all, while box 3 explicitly marks {Go, Delay} as researcher-defined — an asymmetry that reads as if everything unmarked is externally sourced. The manuscript's own Section IV makes all these distinctions correctly; the figure does not yet carry them. All required corrections are to the figure. None requires touching the manuscript text.

---

# PART B — Alignment table

## Stage 1 — Environmental Historical Data

| Item | Figure 1 | Manuscript | Status | Severity | Required action |
|---|---|---|---|---|---|
| Record type | "Meteorological and oceanographic records (2020–2024)" | §IV: hourly environmental records, PRIMARY Jan 2020 – Dec 2024 | Aligned for PRIMARY | None | — |
| Components listed | Wind speed, Rainfall, Ocean state (wave), Time (hour), Marine warning | §IV: "wind, rainfall, marine warning, ocean state and time" | Aligned | None | — |
| Marine warning | "(unavailable for replay period)" | §IV: "no usable historical archive for the replay period" | Aligned | None | — |
| Period coverage | Header reads "(2020–2024)"; the RESOLUTION period is now shown **nowhere** in the figure | §IV: RESOLUTION covers **October 2021 – December 2024** | Partial | **Minor** | Add the RESOLUTION period to box 5, or qualify the box 1 header as PRIMARY |

## Stage 2 — Environmental State Classification

| Item | Figure 1 | Manuscript | Status | Severity | Required action |
|---|---|---|---|---|---|
| Three states | SAFE / CAUTION / UNSAFE | §III: "Each evaluated hour is assigned one of three states, SAFE, CAUTION or UNSAFE" | Aligned | None | — |
| Aggregation rule | Not shown | §IV: "maximum severity among the available component classifications" | Figure omits | None | Acceptable omission for a visual overview |
| Vessel-class role | Not shown | §IV: "Vessel class parameterises the ocean-state component rather than contributing an independent severity term" | Figure omits | None | Acceptable |
| Time/daylight | "Time / daylight state (COLREGs Rule 20(b))" | §IV: day boundary follows COLREGs Rule 20(b) [17]; **the policy treating non-daylight hours as UNSAFE is researcher-defined** | Partial | **Major** | The citation is correct but the researcher-defined UNSAFE policy is unmarked — see C-2 |
| Threshold provenance | Wind / Rainfall / Ocean state shown as "(thresholds)" with no provenance marking | §IV distinguishes four different provenances across these three components | Not represented | **Major** | See C-2 |
| Marine warning | "excluded; held at least-severe value" | §IV: declared exclusion, held at least-severe value | Aligned | None | — |

## Stage 3 — Governance Contract

| Item | Figure 1 | Manuscript | Status | Severity | Required action |
|---|---|---|---|---|---|
| Governed object | *A*<sub>AI</sub>(*S*) | §III: *A*<sub>AI</sub>(*S*) | **Aligned — previously flagged, now fixed** | None | — |
| SAFE | FULL (all recommendations) | Table I: FULL | Aligned | None | — |
| CAUTION | {Go, Delay} (researcher-defined strict subset) | Table I + §III: researcher-defined, strict subset | **Aligned — the researcher-defined marking is new and correct** | None | — |
| UNSAFE | Ø (no participation) | Table I: ∅; §III: "Participation gating is the special case in which the admissible set is empty" | Aligned in meaning | **Minor** | Glyph: figure appears to use Ø (U+00D8), manuscript uses ∅ (U+2205) — confirm and unify |
| FULL definition | Not expanded | §III: FULL = {Go, Delay, DepartureTime, Duration} | Figure omits | None | Acceptable; Table I carries it |

## Stage 4 — Governance Configurations

| Item | Figure 1 | Manuscript | Status | Severity | Required action |
|---|---|---|---|---|---|
| C0 Ungated | FULL / FULL / FULL | §III: "C0 applies no restriction" | Aligned | None | — |
| C1 Participation-only | FULL / FULL / Ø | §III: "C1 gates participation alone" | Aligned | None | — |
| C2 Intermediate-scope (evaluated) | FULL / {Go, Delay} / Ø | §III: "C2 is the evaluated intermediate-scope configuration" | Aligned | None | — |
| C3 Three-state topology | FULL / FULL / Ø | §III: "C3 declares three states without contracting scope at the intermediate one" | Aligned | None | — |
| Isolation statement | "Same at SAFE and UNSAFE · Different only at CAUTION" | §III: "C1 and C2 are identical at SAFE and identical at UNSAFE, and differ only at CAUTION" | Aligned | None | — |
| C3 provenance | Not shown | §III: C3 ports the topology of [10], which conditions on AI degradation | Figure omits | None | Acceptable; body retains it |

**All twelve admissible-set entries verified identical to the removed Table II.** The figure fully substitutes for it.

## Stage 5 — Historical Replay and Measurement

| Item | Figure 1 | Manuscript | Status | Severity | Required action |
|---|---|---|---|---|---|
| Replay character | "Deterministic replay (on classified record)" | §IV: "a deterministic historical replay rather than a model-training experiment"; "no randomisation is involved" | Aligned | None | — |
| PRIMARY period | 2020–2024 | January 2020 – December 2024 | Aligned | None | — |
| PRIMARY records | 43,848 hourly | 43,848 | Aligned | None | — |
| PRIMARY evaluated hours | 9,135 | 9,135 | Aligned | None | — |
| RESOLUTION label | "alternative environmental-data configuration" | §V-A: "differ in both wave source and record period"; "not attributed to spatial resolution alone" | **Aligned — previously flagged, now fixed** | None | — |
| RESOLUTION records | 28,501 hourly | 28,501 | Aligned | None | — |
| RESOLUTION evaluated hours | 5,935 | 5,935 | Aligned | None | — |
| Window | 05:00–09:00, both configurations | §IV: "The evaluation window is 05:00–09:00, which defines *N*<sub>eval</sub>" | Aligned | None | — |
| Metric | Δ*L*<sub>2</sub>, "Frequency that the intermediate restriction binds (C2 vs C1)" | §III: Δ<sub>L2</sub> = (C0↔C2) − (C0↔C1); C1↔C2 computed as cross-check; §V-A: "The direct C1↔C2 comparison returned the same value" | Numerically consistent | **Minor** | The figure shows the cross-check form, not the defining form — see C-5 |

## Stage 6 — Sensitivity and Attribution Analysis

| Item | Figure 1 | Manuscript | Status | Severity | Required action |
|---|---|---|---|---|---|
| Heading | "Threshold configuration (sourced from official guidelines)" | §IV sources wind and rainfall-UNSAFE to MET Malaysia, rainfall-CAUTION to DID (explicitly non-MET), **wave to a peer-reviewed paper [16]** | Mislabelled | **Major** | See C-3 |
| Alternative threshold sets | listed | §V-B: envelope 5.67–9.56% PRIMARY, 4.26–6.64% RESOLUTION | Aligned | None | — |
| Rainfall threshold | listed | §V-B: 0.48 pp PRIMARY, 0.78 pp RESOLUTION | Aligned | None | — |
| Wind threshold | listed | §V-B: structural zero across *W*<sub>C</sub> = 18–25 kn | Aligned | None | — |
| Wave UNSAFE boundary (alternative reading) | listed | §V-B: two sourced readings giving 5.81% and 9.22% | **Aligned — previously flagged, now fixed** | None | — |
| Vessel classes | Small (baseline) / Medium / Large | §V-C: 5.81% / 1.96% / 1.26% PRIMARY; 0.66% / 0.37% RESOLUTION | **Aligned — previously flagged, now fixed** | None | — |
| Denominator policy | "Departure-window only · **All hours**" | §V-C: departure-window baseline vs **daylight-only** (9.59% / 7.40%). "All hours" appears nowhere | **Contradicted** | **CRITICAL** | See C-1 |
| Component attribution | Wind, Rainfall, Ocean state, Time/daylight, Marine warning (excluded) | §V-C: all five, with three distinct zeros | Aligned | None | — |

## Cross-cutting

| Item | Status | Severity |
|---|---|---|
| ±0.25 m perturbation removed from figure, methodology, results, discussion, abstract, conclusion, tables and captions | **Confirmed absent** — searched for 0.25, 2.54, 14.75, −1.2, and "wave CAUTION onset"; zero hits in the rendered PDF | None |
| Table II removal | **Clean** — zero prose references to "Table II" remain; former Table III correctly renumbered TABLE II; C0 and C3 purposes still defined in text; the Δ<sub>L2</sub> equation's dependence on C0 still satisfied | None |
| Abstract | No removed result present; 5.81%, 4.48%, 5.67–9.56%, 1.96%, 1.26%, 97.6% all consistent with §V | None |
| Conclusion | Consistent; the sensitivity sentence now rests on the two sourced wave readings rather than the deleted perturbation | None |
| Δ<sub>L2</sub> interpretation | Correct in every occurrence — binding frequency, never safety, accuracy, advice quality, oversight or optimality | None |

---

# PART C — Issues requiring correction

## CRITICAL

### C-1. Figure 1 states a denominator policy the manuscript never evaluated

**Issue.** Box 6 lists *"Denominator policy: Departure-window only · All hours"*. The manuscript's alternative denominator is **daylight-only**, not all hours.

**Why it matters.** This is not a wording slip. The time component classifies non-daylight hours as UNSAFE. A daylight-only denominator *removes* those hours, which is why Δ<sub>L2</sub> **rises** to 9.59% (PRIMARY) and 7.40% (RESOLUTION). An all-hours denominator would *add* the full night back in and push the proportion **down**. The figure therefore names a condition that (a) was never run, (b) has no reported result, and (c) would move the headline in the opposite direction from the condition that was run. A reviewer tracing the figure's box 6 into Section V-C finds a dead end.

**Manuscript location.** §V-C: *"Replacing the departure-window denominator with a daylight-only denominator raises it to 9.59% in PRIMARY and 7.40% in RESOLUTION."* Also §V-C RQ1 paragraph and the Fig. 1 overview paragraph in §III.

**Figure location.** Box 6, third sub-box.

**Recommended correction.** Change the second bullet from "All hours" to **"Daylight-only"**. No manuscript change is required.

---

## MAJOR

### C-2. Researcher-defined choices are unmarked in box 2, while {Go, Delay} is marked in box 3

**Issue.** Box 3 now correctly labels {Go, Delay} as a *"researcher-defined strict subset"*. Box 2 lists Wind speed, Rainfall and Ocean state as *"(thresholds)"* with no provenance marking, and attributes Time/daylight state to COLREGs Rule 20(b) without noting that the **policy treating non-daylight hours as UNSAFE is researcher-defined**. The evaluation window and the three-state cardinality are also researcher-defined and appear nowhere as such.

**Why it matters.** Marking one researcher-defined choice and leaving the others unmarked implies, by contrast, that everything unmarked is externally sourced. That is the exact inference the supervisor asked to be prevented. Section IV states the distinction correctly in prose — *"Researcher-defined choices are the three-state cardinality, A<sub>AI</sub>(CAUTION), the policy treating non-daylight hours as UNSAFE, the evaluation window, and the declared exclusion"* — so the figure currently contradicts the paper's own care.

**Manuscript location.** §IV, threshold-provenance paragraph; §IV, when/what paragraph.

**Figure location.** Box 2 (all four threshold items); box 5 (the 05:00–09:00 window).

**Recommended correction.** Mark provenance in box 2 the same way box 3 now does — for example "(sourced)" against wind and rainfall-UNSAFE, "(sourced, non-MET)" against rainfall-CAUTION, "(sourced, [16])" against ocean state, and "(COLREGs boundary; night→UNSAFE researcher-defined)" against time. If space does not permit, a single legend distinguishing sourced from researcher-defined items would serve.

### C-3. "Sourced from official guidelines" misdescribes the wave boundary's provenance

**Issue.** Box 6's heading reads *"Threshold configuration (sourced from official guidelines)"* and its bullets include the **wave UNSAFE boundary**. Section IV sources that boundary to *"the operational ceiling reported by [16]"* — Yaakob et al. 2015, a peer-reviewed journal article, not an official guideline. The rainfall CAUTION boundary is DID/Infobanjir, which is an official agency but which the manuscript is careful to flag as **not** a Meteorological Department threshold.

**Why it matters.** The supervisor's concern is precisely whether source-grounded and researcher-defined values are distinguishable. A heading that promotes a journal-sourced threshold to "official guideline" weakens the paper's own most careful passage, and the wave boundary is the one that moves the result most (5.81% → 9.22%).

**Manuscript location.** §IV provenance paragraph; §V-B, second paragraph.

**Figure location.** Box 6, first sub-box heading.

**Recommended correction.** Change the heading to **"(externally sourced)"** or **"(sourced thresholds)"**. Both are accurate across all four bullets; "official guidelines" is not.

---

## MINOR

### C-4. The RESOLUTION record period is no longer shown anywhere in the figure

Box 1 is headed "(2020–2024)" and box 5 no longer gives the RESOLUTION period, so the figure now reads as though both configurations cover 2020–2024. Section IV gives RESOLUTION as **October 2021 – December 2024**, and Section V-A makes the period difference load-bearing: *"The two configurations differ in both wave source and record period."* Recommended: restore the period line to box 5, or qualify box 1's header as PRIMARY.

### C-5. The figure shows Δ<sub>L2</sub> as "(C2 vs C1)", which is the cross-check rather than the definition

Section III defines Δ<sub>L2</sub> = (C0↔C2) − (C0↔C1) and computes the direct C1↔C2 comparison as an implementation cross-check; Section V-A confirms it *"returned the same value"*. The figure is therefore numerically correct but shows the secondary form, which makes C0's role in the decomposition invisible. Not an error. Consider adding the decomposition form alongside, or leave as-is if space is tight — the body text is unambiguous.

### C-6. Empty-set glyph

The figure appears to use **Ø** (U+00D8, capital O with stroke); the manuscript uses **∅** (U+2205, empty set). Visually near-identical at figure resolution, typographically different. Worth unifying to ∅ before camera-ready.

### C-7. "Five years" in the Abstract and Introduction applies to PRIMARY only

Pre-existing, not introduced by this revision. The Abstract says the configurations were *"replayed over five years of hourly environmental records"* and then reports both PRIMARY and RESOLUTION; RESOLUTION covers 3.25 years. Defensible as a description of the headline configuration, but a precise reader may notice. No change required unless you want it tightened.

---

# PART D — Confidence assessment

| | Score | Explanation |
|---|---|---|
| **A. Figure 1 ↔ manuscript alignment** | **72%** | Four of five previously flagged mismatches are fixed and all four stage-4 configurations plus every number reconcile exactly. Held down by C-1, where the figure names an experimental condition that does not exist in the paper and whose effect runs opposite to the one that does, and by C-4, where the RESOLUTION period has disappeared from the figure entirely. |
| **B. Methodological clarity** | **88%** | The framework figure, the explicit replay procedure and the when/what separation make the method substantially easier to follow than the previous version. Held below 90% only because the figure's box 2 does not carry the provenance distinctions that the prose makes carefully, so a reader working from the figure alone gets a flatter picture than the paper actually supports. |
| **C. Threshold / design-choice traceability** | **76%** | Section IV is explicit and correct: every boundary is attributed, the non-MET gap is declared, and the researcher-defined list is enumerated. The score is depressed by the figure, not the text — C-2 leaves most researcher-defined choices unmarked while marking one, and C-3 promotes a journal-sourced threshold to "official guideline". Since provenance is the supervisor's stated concern, these carry more weight than their size suggests. |
| **D. Experimental reproducibility** | **80%** | Determinism is now stated outright, the per-configuration procedure is spelled out step by step, and the claim that an identical record under an identical configuration reproduces an identical result is explicit. The gap is that the manuscript still never states **how many configurations were evaluated** — which is the literal form of the supervisor's question. See Author Verification Required. |
| **E. Numerical consistency** | **97%** | Every figure number matches the manuscript: 43,848 / 9,135 / 28,501 / 5,935, the window, and all stage-6 categories. All retained results verified present in the rendered PDF; all deleted values verified absent. No orphan or unsupported number anywhere. The residual 3% is C-4, a missing period rather than a wrong one. |
| **F. Claim discipline** | **95%** | Δ<sub>L2</sub> is interpreted as binding frequency in every occurrence. No safety, decision-quality, advice-accuracy, oversight or optimality claim appears. Both scoped *"Within the reviewed literature"* statements survive. {Go, Delay} is described as researcher-defined and unvalidated in the body, in Table I's note, in §VI and now in the figure. The deducted 5% is C-7's "five years" imprecision and nothing more. |
| **G. Overall publication readiness** | **82%** | The manuscript body is submission-quality: content-complete, internally consistent, within 6 A4 pages, claim-disciplined. Readiness is gated entirely on three figure edits — one critical, two major — none of which requires touching the text. Once C-1 to C-3 are applied, this would move to the low-to-mid 90s. |

---

# AUTHOR VERIFICATION REQUIRED

### 1. Number of evaluated configurations / replays

The revised Section IV now establishes **reproducibility** — the replay is deterministic, nothing is estimated, nothing is randomised, and an identical configuration reproduces an identical result. That answers the *kind* of question behind "how many times did you run the test?" by making repeated runs unnecessary.

It does **not** answer the *count*. The manuscript names the configurations (C0–C3), the two environmental-data configurations, three vessel classes, two denominator policies and several threshold settings, but never multiplies them out or states a total. Figure 1 does not either.

The two senses must be kept apart when you answer the supervisor:

- **Repeated runs of one identical configuration:** one run suffices, and the manuscript now says why.
- **Distinct configurations evaluated:** a real count exists but is not stated anywhere in the supplied materials.

**No number was inserted.** If you want one in the paper, it should be counted from the canonical sensitivity script rather than reconstructed from the text — and it would then be new information entering the manuscript, which needs your sign-off.

### 2. Empty-set glyph in the figure source

Whether the figure uses Ø (U+00D8) or ∅ (U+2205) cannot be determined with certainty from the rendered image at this resolution. Check the figure source. (C-6)

---

**Everything else in this audit was resolvable from the supplied manuscript and figure. No other author input is required.**
