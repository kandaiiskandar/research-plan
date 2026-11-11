# AAI 2026 — Focused Evidence Audit: Medium-Vessel 2.8 m and RESOLUTION Pairwise Values

**Date:** 2026-10-07
**Manuscript:** `aai-2026-manuscript-v3-evidence-corrected.docx`
**Status:** audit only — **no manuscript or figure change applied**

---

# 1. EXECUTIVE VERDICT

**Issue B is resolved, decisively, in favour of reporting.** I re-ran the canonical comparator twice and instrumented it to emit unrounded percentages and raw hour counts. For RESOLUTION over the departure window (n = 5,935): C0↔C1 = 2,438 hours = 41.0783487784%, C0↔C2 = 2,704 hours = 45.5602358888%, and the difference is **exactly 266 hours** = 4.4818871104%, which is also exactly what the direct C1↔C2 comparison returns — the same integer, not a rounding coincidence. C1↔C3 = 0/5,935 = 0.000000%. The two consecutive executions were byte-for-byte identical. PRIMARY comes from the same script, the same function and the same single run: 3,917 and 4,448 hours, differing by **531** — the very CAUTION-hour count the manuscript already reports in §V-C. There is no computational, procedural or data-lineage difference between the two configurations; only the input marine file differs. The phrase "provenance is incomplete" traces to a project bookkeeping lock (`RESOLUTION_PAIRWISE_C0_C1_C0_C2 = PROVENANCE_INCOMPLETE`), and `docs/analysis/canonical-revision-report.md` line 178 states the reason in full: *"41.08% / 45.56% remain withheld **pending a provenance row**."* That is a missing documentation entry, not a scientific defect — and this audit supplies the row.

**Issue A is partially resolved, and the answer is worse than "interpolated".** The 2.8 m medium-vessel UNSAFE boundary is researcher-defined, and it is **not reproducible from its own stated derivation rule**. Appendix C says it was *"interpolated between the small and big rows, preserving an approximately proportional CAUTION band width."* I tested six defensible readings of that rule: linear in the UNSAFE value → 3.05 m; linear in CAUTION band width → 3.05 m; linear in the UNSAFE/onset ratio → 2.96 m; linear in band/onset ratio → 2.96 m; midpoint of ratios → 2.51 m; geometric mean of ratios → 2.39 m. **None yields 2.8.** What 2.8 actually is, is exactly 2.0 × the 1.4 m onset — a round multiplier, not an interpolation output. The project's own records already call it *"the weakest-grounded value in the g_o table"* and log it as a threat to internal validity in C.9.

**Neither issue touches the paper's spine.** The 2.8 m value does not enter the headline 5.81%, the 5.67–9.56% sourced envelope (which is computed over the two small-vessel wave columns only), the C1-vs-C2 isolation, the component attribution, or the contribution. It appears solely in the vessel-class robustness disclosure. The RESOLUTION pairwise values are decomposition detail; Δ<sub>L2</sub> = 4.48% is unaffected either way. Both are reporting-quality issues, not validity issues — but the 2.8 m one is the sort of value a viva question lands on, because the paper currently gives a reader no way to tell it apart from a sourced threshold.

---

# 2. ISSUE A — 2.8 m EVIDENCE CHAIN

## A1 / A2 — Where the value lives, and what the sources actually support

| Claim / value | Evidence | Source location | Classification | Confidence |
|---|---|---|---|---|
| medium UNSAFE = 2.8 m | *"the 2.8 m CAUTION/UNSAFE boundary is **interpolated between the small and big rows**… **No corpus source provides a direct medium-vessel UNSAFE threshold.** This is the **weakest-grounded value** in the table"* | `docs/canonical/appendix-c-formalisation.md` line 611; restated line 1043 | **Researcher-defined** | **High** |
| medium UNSAFE in code | `(1.4, 2.8)` | `canonical_figures.py:93`, `compare_v1_v2.py:21`, `diagnostic_binding.py:54`, `historical_replay.py:59`, `threshold_sensitivity.py` wave block | — | High |
| medium CAUTION onset = 1.4 m | *"derives from Hs_KIMO evaluated across the 10–15 m LOA range (1.13 m at 10 m, 1.48 m at 15 m)"* | appendix-c line 611 | **Derived** from Jeong & Im | High |
| small CAUTION onset = 1.0 m | *"Jeong & Im's own proposed restriction for vessels ≤ 10 m LOA (**their Table 12**)"* | appendix-c line 607 | **Directly stated by source** | High |
| small UNSAFE = 1.25 m | Yaakob operational ceiling, top of Sea State 3 | appendix-c lines 562, 607 | **Directly stated by source** | High |
| small UNSAFE alt reading ≈ 1.875 m | Yaakob failure point, Sea State 4 | appendix-c line 568 | **Directly stated by source** | High |
| big CAUTION onset = 1.5 m | *"corroborated by Jeong & Im… 1.58 m at 16 m LOA and 1.43 m at 14 m LOA — bracketing 1.5 m"* | appendix-c line 605 | **Corroborated**, not stated | Medium |
| big UNSAFE = 3.5 m | *"aligns with MET Malaysia Category 1 maximum wave height criteria"* | appendix-c line 605; MET page verified in Phase 8 (*"laut bergelora… sehingga 3.5 meter"*) | **Directly stated by source** | High |

### Per-class summary table

| Vessel class | Boundary | Value | Source | Directly stated? | Derived? | Researcher-defined? |
|---|---|---|---|---|---|---|
| small | CAUTION onset | 1.0 m | Jeong & Im, Table 12 | ✅ | — | — |
| small | UNSAFE | 1.25 m | Yaakob, SS3 ceiling | ✅ | — | — |
| medium | CAUTION onset | 1.4 m | Jeong & Im, Hs_KIMO over 10–15 m LOA | — | ✅ | — |
| **medium** | **UNSAFE** | **2.8 m** | **none** | — | — | **✅** |
| big | CAUTION onset | 1.5 m | Jeong & Im Hs_KIMO brackets it | — | ✅ (corroboration) | — |
| big | UNSAFE | 3.5 m | MET Malaysia Cat 1 wave ceiling | ✅ | — | — |

## A3 — Reconstruction: the stated rule does not produce the value

The medium onset (1.4 m) sits at position **0.80** between the small (1.0 m) and big (1.5 m) onsets. Applying that position under six defensible readings of *"preserving an approximately proportional CAUTION band width"*:

| Interpolation rule | Resulting medium UNSAFE |
|---|---|
| **Adopted value** | **2.80 m** (= exactly 2.0 × onset) |
| Linear in the UNSAFE value | 3.05 m |
| Linear in CAUTION band width | 3.05 m |
| Linear in the UNSAFE/onset ratio | 2.96 m |
| Linear in the band/onset ratio | 2.96 m |
| Midpoint of the UNSAFE/onset ratios | 2.51 m |
| Geometric mean of the ratios | 2.39 m |

**Findings:**

1. **Source values used:** small (1.0, 1.25) and big (1.5, 3.5).
2. **Exact calculation:** none is recorded anywhere in the repository, and none of the six reconstructions returns 2.8. The value equals 2.0 × 1.4 exactly.
3. **Why interpolation was used:** no corpus source provides a medium-vessel UNSAFE threshold — stated explicitly in appendix-c lines 611 and 1043.
4. **Defined before or after the experiment?** **Before.** Every `amended 2026-09-06` annotation in the scripts and in appendix-c names the **small** row only (1.9 → 1.25 m). The medium row predates that amendment and was not touched by it. It was not introduced to fit a result.
5. **Independent methodological justification?** Partial. "No source exists, so interpolate conservatively between neighbours" is a reasonable stance. But the stated rule does not determine the number, so the justification explains the *approach*, not the *value*.
6. **Would another equally defensible interpolation give a different value?** **Yes — 2.39 m to 3.05 m**, a spread of 0.66 m around an adopted 2.8 m.

### Classification

**D — researcher-defined with weak justification.**

Not A: no source states it. Not B: no stated calculation reproduces it. Not C: the documented method yields 2.96–3.05 m, not 2.8 m, so the value is not the output of its own justification. Not E: the provenance is fully resolved — we know exactly what it is and how it got there; it is simply weak.

**Not computed, by instruction:** whether the 1.96% medium result is sensitive to this choice would require replaying (1.4, 2.96) or (1.4, 2.39), which is a new experiment the brief forbids. **The robustness of the medium figure to the interpolation choice is therefore unestablished.**

## A4 — Role in the paper

| Study element | Does 2.8 m enter it? |
|---|---|
| PRIMARY Δ<sub>L2</sub> = 5.81% | **No** — small-vessel baseline (1.0, 1.25) |
| RESOLUTION Δ<sub>L2</sub> = 4.48% | **No** |
| C0↔C1 / C0↔C2 decomposition | **No** |
| C1-vs-C2 isolation logic | **No** |
| Sourced-threshold envelope 5.67–9.56% | **No** — verified from the grid output: 5.67% is (1.0, 1.25) at R_C = 19.9 and 9.56% is (1.0, 1.9) at R_C = 5.0. The envelope is the min/max over the **two small-vessel wave columns only**; the medium and big columns are excluded, consistent with §V-B's wording *"for the small-vessel baseline"* |
| Component attribution 518/531 = 97.6% | **No** |
| Research gap / RQ1 / contribution | **No** |
| Vessel-class robustness disclosure (1.96%, 0.66%) | **Yes — this is its only use** |

> **"If the medium-vessel analysis were removed, would the main experiment, the 5.81% result, the C1-vs-C2 isolation and the core contribution remain intact?"**
>
> **Yes — entirely intact.** Nothing else in the paper reads the medium row. The large-vessel variant (1.26% / 0.37%) would remain and would still demonstrate scope dependence, and its boundaries are better grounded: the 1.5 m onset is bracketed by Jeong & Im's formula and the 3.5 m UNSAFE boundary is MET Malaysia's Category 1 wave ceiling.

## A5 — Recommendation

### **3 — KEEP BUT LABEL AS RESEARCHER-DEFINED**

**Justification from evidence.** The manuscript currently makes **no false claim** about this value — §IV scopes its ocean-state provenance sentence to the small-vessel class, and §V-B scopes the envelope to the small-vessel baseline. The defect is an *omission*: a reader is given no way to distinguish the medium-vessel UNSAFE boundary from the sourced thresholds beside it, and the paper's own project record calls it the weakest-grounded value in the table. One clause closes that, costs roughly twelve words, and leaves the reported figures untouched.

**Removal (option 4) is equally defensible and would simplify the paper**, as the brief invited me to say explicitly: nothing depends on the medium row, the large-vessel variant alone already establishes scope dependence, and removing it would delete the single weakest-grounded value from the manuscript entirely while freeing space at a hard six-page limit. I did not recommend it because the figure is already in the project's canonical record, dropping a reported result mid-revision invites the question of why it disappeared, and disclosure achieves the same honesty at lower cost. If you prefer the simpler paper, option 4 is sound — but then say in §V-C that only two vessel classes are reported, rather than letting the medium class vanish silently.

---

# 3. ISSUE B — RESOLUTION EVIDENCE CHAIN

## B1 / B5 — Traced and reproduced

Source: `scripts/condition_comparison.py`, instrumented to emit raw hour counts and unrounded percentages, executed twice.

**RESOLUTION, departure window 05:00–09:00, n = 5,935 evaluated hours**

| Metric | Canonical value (unrounded) | Raw count | Evidence source | Reproduced? | Confidence |
|---|---|---|---|---|---|
| C0↔C1 | **41.0783487784%** | 2,438 / 5,935 | `condition_comparison.py`, divergence matrix | ✅ twice, identical | **High** |
| C0↔C2 | **45.5602358888%** | 2,704 / 5,935 | same run, same matrix | ✅ twice, identical | **High** |
| Δ<sub>L2</sub> = (C0↔C2) − (C0↔C1) | **4.4818871104%** | 2,704 − 2,438 = **266** | derived from the same two counts | ✅ | **High** |
| direct C1↔C2 | **4.4818871104%** | **266** / 5,935 | same matrix, independent cell | ✅ | **High** |
| C1↔C3 | **0.0000000000%** | 0 / 5,935 | same matrix | ✅ | **High** |

**PRIMARY, departure window, n = 9,135** — same script, same function, same single execution:

| Metric | Unrounded | Raw count |
|---|---|---|
| C0↔C1 | 42.8790366721% | 3,917 |
| C0↔C2 | 48.6918445539% | 4,448 |
| difference | 5.8128078818% | **531** |
| direct C1↔C2 | 5.8128078818% | **531** |

**The PRIMARY difference is 4,448 − 3,917 = 531 hours — the exact CAUTION-hour count the manuscript already reports in §V-C.** The decomposition is exact at the integer level in both configurations.

## B2 — Mathematical consistency

- 45.5602358888 − 41.0783487784 = **4.4818871104** ✅ exact to ten decimal places.
- Equivalently 2,704 − 2,438 = 266 hours ✅ exact in integers, so the identity does not depend on rounding.
- Direct C1↔C2 returns **the same 266 hours**, i.e. the cross-check is not merely close — it is the identical count, as the Section III mappings entail.
- The manuscript's rounded presentation (45.56 − 41.08 = 4.48) is therefore faithful.

## B3 — Procedure comparison

| Component | PRIMARY | RESOLUTION | Same? |
|---|---|---|---|
| State classification | `g_w`, `g_r`, `g_o`, `g_t`, `g_m`, max-severity | identical code path | ✅ |
| Governance mappings | C0/C1/C2/C3 from one `A_AI` dict | same dict | ✅ |
| Pairwise comparison | `divergence_matrix`, same function | same function, same call | ✅ |
| Δ<sub>L2</sub> calculation | difference of two matrix cells | identical | ✅ |
| Denominator | departure window 05:00–09:00 | identical | ✅ |
| **Environmental data** | ERA5-Ocean, Jan 2020–Dec 2024 | MFWAM, Oct 2021–Dec 2024 | **Differs — by design** |

> **"Are the RESOLUTION pairwise values produced by the same valid governance comparison procedure used for PRIMARY?"**
>
> **Yes.** They are produced by the same function, in the same execution, printed in adjacent blocks of the same output. The only difference is the input marine file and record period — which is the configured difference between the two environmental-data configurations, not a procedural one. Nothing here attributes the numerical gap to spatial resolution.

## B4 — What "provenance incomplete" actually meant

The phrase originates in a project-level bookkeeping lock, not in a finding:

- `docs/analysis/aai-2026-locked-research-chain-patched.md` line 225: *"RESOLUTION pairwise components remain withheld under `RESOLUTION_PAIRWISE_C0_C1_C0_C2 = PROVENANCE_INCOMPLETE`. **Do not invent them.**"*
- `docs/tasks/AMICT CONFERENCE MANUSCRIPT V4` lines 460–465: *"Do NOT use as headline evidence: C0↔C1 RESOLUTION = 41.08%, C0↔C2 RESOLUTION = 45.56% **until provenance is repaired**. The manuscript does not require these numbers."*
- **The decisive line** — `docs/analysis/canonical-revision-report.md` line 178: *"Unchanged. 41.08% / 45.56% remain withheld **pending a provenance row**."*

Two things follow. First, **the values themselves were never in doubt** — they are written out, correctly, inside the very documents that withhold them. Second, the stated blocker is a **missing row in a provenance register**, i.e. a documentation gap. The surrounding context explains why the gap mattered at the time: the same revision episode was correcting *"three grid-resolution attributions"*, so RESOLUTION figures were quarantined while the attribution defect around them was repaired.

Against the brief's checklist of possible meanings: **"merely undocumented rather than scientifically unsupported"** — and *not* data-lineage uncertainty, calculation uncertainty, unverified configuration, or an unavailable script. The canonical script is present, runs, and reproduces the values deterministically.

**The original provenance concern is now resolved by this audit**, which supplies the missing row: script, function, raw counts, unrounded values, denominator, and two identical executions.

## B6 — Recommendation

### **1 — REPORT 41.08% AND 45.56%**

Evidence and reproducibility are sufficient and, on the record, overwhelming: same script, same function, same run as the PRIMARY values the paper already reports; exact integer decomposition; an independent cross-check returning the identical count; and bit-identical re-execution.

Continued withholding is not defensible. The manuscript's current sentence states a reason — *"their provenance is incomplete"* — that the artefact contradicts. A reviewer who runs `condition_comparison.py`, which the paper's reproducibility framing invites, will see 41.08% and 45.56% printed in the same table as 42.88% and 48.69%. **Withholding them while asserting that reason is now the larger reviewer risk**, because it suggests either that the authors do not know their own pipeline or that something was suppressed.

If you would rather not expand Table III at a six-page limit, option 3 (report Δ<sub>L2</sub> only) remains available — **but the stated reason must change**, because "provenance is incomplete" is no longer true.

---

# 4. IMPACT ON THE STUDY

| Study element | Impact | Explanation |
|---|---|---|
| Research gap | **Unaffected** | Neither issue touches the scoped absence claim or the near-neighbour concessions. |
| RQ1 | **Unaffected** | RQ1 asks how often the intermediate level binds and how sensitive that is to defensible configurations; neither issue changes the question or the answer. |
| PRIMARY 5.81% | **Unaffected** | Small-vessel baseline; 2.8 m plays no part, and the decomposition that produces it is confirmed exact (4,448 − 3,917 = 531). |
| RESOLUTION 4.48% | **Unaffected** | Confirmed as 266/5,935 by two independent cells of the same matrix. |
| C1-vs-C2 isolation | **Unaffected** | Mapping-level property, independent of both issues. |
| Sourced-threshold envelope 5.67–9.56% | **Unaffected** | Verified to span only the two small-vessel wave columns. |
| Configuration-dependence conclusion | **Minor impact** | It rests on four dimensions — thresholds, vessel class, denominator, environmental data. One of the three vessel-class rows uses a researcher-defined boundary, which slightly weakens that one dimension without affecting the conclusion, which the other three carry independently. |
| Component attribution | **Unaffected** | Computed at the small-vessel baseline. |
| Core contribution | **Unaffected** | The measurement assembly and criterion are untouched by either issue. |
| Reporting integrity / reviewer risk | **Material impact** | A reviewer running the artefact finds two values the paper says cannot be reported, and a threshold the paper does not distinguish from sourced ones. Both are fixable in two sentences. |

---

# 5. EXACT CORRECTIONS — NOT APPLIED

## Correction 1 — §V-A, RESOLUTION decomposition *(Issue B)*

**Existing sentence:**
> "The RESOLUTION pairwise components are not reported because their provenance is incomplete; Δ<sub>L2</sub> is unaffected."

**Proposed replacement:**
> "The RESOLUTION decomposition gives C0↔C1 = 41.08% and C0↔C2 = 45.56%, a difference of 266 of the 5,935 evaluated hours."

## Correction 2 — Table III, two withheld cells *(Issue B)*

| Row | Current RESOLUTION cell | Proposed |
|---|---|---|
| C0↔C1 | — | **41.08%** |
| C0↔C2 | — | **45.56%** |

## Correction 3 — Table III note *(Issue B)*

**Existing:**
> "— indicates pairwise resolution components withheld because provenance is incomplete; Δ<sub>L2</sub> is unaffected. C1↔C3 = 0.00% is entailed by the mappings and is reported as an implementation conformance check. The sourced-threshold envelope is a deterministic configuration range, not a confidence interval."

**Proposed:** delete the first clause through "Δ<sub>L2</sub> is unaffected." and begin at *"C1↔C3 = 0.00% is entailed…"*. The em-dash legend becomes unnecessary once both cells are populated.

## Correction 4 — §V-C, medium-vessel disclosure *(Issue A)*

**Existing sentence:**
> "Under the medium- and large-vessel threshold configurations the PRIMARY value falls to 1.96% and 1.26% respectively, and to 0.66% and 0.37% in RESOLUTION."

**Proposed addition immediately after it:**
> "The medium-vessel UNSAFE boundary is researcher-defined by interpolation between the small and large classes rather than taken from a source."

*(If you choose removal instead, delete the medium figures from this sentence and from §V-B's framing, and state that two vessel classes are reported.)*

## Page-budget warning

The manuscript is at **exactly 6 pages**, the stated AAI maximum, with rejection on overflow. Corrections 1 and 4 together add roughly 40 words; correction 3 removes about 15. Net is a small increase, but populating two Table III cells also lets the table note shrink. **Apply and re-measure before accepting** — I have not tested the combined effect.

---

# AUTHOR VERIFICATION REQUIRED

1. **The exact arithmetic that produced 2.8 m.** Appendix C records the *approach* ("interpolated between the small and big rows, preserving an approximately proportional CAUTION band width") but not the calculation, and none of six defensible readings of that rule returns 2.8 m — they return 2.39, 2.51, 2.96, 2.96, 3.05 and 3.05. If you recall the actual derivation, it would move the value from classification **D** to **B** or **C**. If you do not, **D** stands and the disclosure in Correction 4 is the right response.

2. **Whether to report or remove the medium-vessel variant.** Correction 4 assumes you keep it. Removal is equally defensible and simplifies the paper; the choice is editorial and yours.

3. **Whether the six-page limit survives the corrections.** Stated above, not tested.

**Nothing else is unresolved.** The provenance of every other wave boundary, the meaning of "provenance incomplete", and all RESOLUTION pairwise values are established from the repository's own records and from re-execution of the canonical scripts.
