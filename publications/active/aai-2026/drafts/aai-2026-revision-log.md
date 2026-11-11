# AAI 2026 — Revision Log

**Base:** `rewrite_aai-2026-manuscript-v1-ieee-layout.docx` (supplied, treated as authoritative)
**Output:** `aai-2026-manuscript-v2-revised.docx` / `.pdf` — IEEE conference format, A4, two-column, **6 pages** (unchanged from the base)
**Date:** 2026-10-07

Existing wording, terminology, equations, definitions, citations, numbering and section structure were retained wherever they remained correct. No paraphrasing for style. No new evidence, citations, thresholds, experiments or claims were introduced.

---

## 1. Figure 1 integrated

| Section | Change | Why |
|---|---|---|
| **III**, new opening paragraph | Added one paragraph introducing Fig. 1 and the workflow it represents: records → state classification → governance contract → configurations → deterministic replay → binding frequency → sensitivity and attribution. Closes by stating the division of labour: this section gives the formal object, criterion and metric; Section IV gives data, provenance and procedure. | Task §1. The figure is introduced before it appears, and the prose explains the methodological logic connecting the stages rather than restating the boxes. |
| **III**, after the C1/C3 paragraph | Supplied Figure 1 image inserted at the position previously occupied by Table II, spanning both columns, with the caption *"Fig. 1. Evaluation framework for measuring the operational effect of the intermediate governance restriction."* | The configurations are discussed at exactly this point, so the figure's box 4 is available where it is needed. |

**Figure handling.** The supplied image was not redrawn, regenerated or reinterpreted. One change was made and is declared: the caption strip baked into the bottom of the supplied PNG was cropped off, because the document carries its own IEEE caption and the page would otherwise print the caption twice. The diagram content, including the stage labels along the bottom, is untouched. The uncropped original is unchanged on disk.

## 2. Table II removed

| Section | Change | Why |
|---|---|---|
| **III** | Table II (label, caption, four-row table) deleted. | Task §2. Its content is reproduced exactly in Fig. 1 box 4 — all four configurations and all twelve admissible-set entries verified identical, see the audit below. |
| **III** | *"Table II defines four configurations over the same classifier."* → *"Four configurations are defined over the same classifier, and their admissible-set mappings are given in Fig. 1."* | Only cross-reference to Table II in the body. |
| **III** | **Retained unchanged:** the paragraph establishing that C1 and C2 are identical at SAFE and at UNSAFE and differ only at CAUTION, and the paragraph establishing that C1 and C3 are identical at every state and that C1↔C3 is a conformance check. | Task §2 explicitly protects the isolation logic and the C0/C3 purposes. Removing the table removed no explanation. |
| **V** | Table III renumbered to **TABLE II**. Caption and all values unchanged. | Only remaining table. |

## 3. Threshold provenance and researcher-defined choices

| Section | Change | Why |
|---|---|---|
| **III**, A<sub>AI</sub>(CAUTION) paragraph | Added one sentence: *"A strict subset of FULL is required at the intermediate state because a level that leaves the admissible set unchanged instantiates no contraction, and so provides nothing to isolate or measure."* | Task §3. Gives the methodological reason for the choice at first mention. The existing non-validation sentence is unchanged. |
| **IV**, after the provenance paragraph | Added one paragraph separating the two kinds of choice: environmental thresholds determine **when** a state such as CAUTION occurs; the governance contract determines **what** the system may recommend once it holds. A<sub>AI</sub>(CAUTION) is of the second kind, and the evaluation measures how often the contraction binds rather than whether its content is appropriate. | Supervisor feedback. The existing provenance sentences (which boundary comes from which source, and that provenance does not establish optimality) were already correct and were left as they stand. |

No claim was added that {Go, Delay} is optimal, validated, safer or externally prescribed. The Section VI limitation on field and stakeholder validation of the restricted set is unchanged.

## 4. Experimental procedure

| Section | Change | Why |
|---|---|---|
| **IV**, before the determinism paragraph | Added one paragraph stating the procedure explicitly: for each configuration, every evaluated hour is classified by the component rules, the configuration's admissible-set mapping is applied, and the hours on which two configurations admit different sets are counted; Δ<sub>L2</sub> follows from those counts; the same operations repeat for each alternative threshold, vessel-class and denominator setting; no parameter is estimated and no randomisation is involved, so an identical record under an identical configuration reproduces an identical result. | Task §4. Makes the reproducibility property explicit without restating what the existing determinism paragraph already covers (no sampling inference, no p-values, no confidence intervals), which was left unchanged. |

**Number of replays not stated.** See Author Verification Required, item 5.

## 5. Sensitivity analysis simplified

| Section | Change | Why |
|---|---|---|
| **V-B** | Deleted the entire paragraph describing the ±0.25 m wave-CAUTION-onset perturbation, the 2.54–14.75% range, and the ≈ −1.2 percentage-points-per-0.05-m statement. | Task §5. Researcher-defined perturbation removed from this conference manuscript. Nothing was substituted. |
| **V-C**, RQ1 paragraph | Deleted the clause *"moves across 2.54–14.75% under a ±0.25 m wave-onset perturbation,"*. The sentence now runs: spans 5.67–9.56% across sourced threshold configurations, falls to 1.96% and 1.26% for the medium and large vessel classes, and rises to 9.59% under a daylight-only denominator. | Dependent cross-reference. |
| **VI** | *"…with the wave CAUTION onset producing the largest sensitivity."* → *"…with the choice between the two sourced readings of the small-vessel wave boundary producing the largest movement among the sourced threshold settings."* | **This sentence rested entirely on the deleted perturbation** and would have been unsupported after removal. The replacement is supported by retained text: the two sourced readings give 5.81% and 9.22% (3.41 pp), against 0.48 pp for the rainfall boundary and a structural zero for wind. Scope narrowed to *sourced threshold settings* so it cannot be read as ranking against the vessel-class variants. |

**Retained in full:** the sourced-threshold envelopes (5.67–9.56% PRIMARY, 4.26–6.64% RESOLUTION) with their "deterministic configuration ranges, not confidence intervals" framing; the two sourced readings of the UNSAFE boundary; the rainfall and wind sensitivity; and the conclusion that the binding frequency is not a threshold-invariant property of the site.

**Abstract required no change** — it never referenced the perturbation.

## 6. Results, discussion and claim boundaries

Audited after the removal. No other sentence depended on the deleted analysis. Unchanged: Δ<sub>L2</sub> = 5.81% PRIMARY / 4.48% RESOLUTION; the C0↔C1 / C0↔C2 decomposition and the 48.69 − 42.88 = 5.81 arithmetic; C1↔C3 = 0.00% as entailed conformance; component attribution 518/531 = 97.6% and 13 = 2.4% with the three distinct zeros; vessel-class and denominator-policy variants; the lower-bound qualification; and every non-claim in §V-C and §VI.

No claim was strengthened. The manuscript still states that it does not establish correctness, optimality, safety, decision quality, oversight effectiveness or generalisation, and does not evaluate generated advice.

## 7. Verification performed on the output PDF

- **Removed:** `0.25`, `2.54`, `14.75`, `−1.2`, `TABLE III` — all absent.
- **Retained:** all 28 locked values checked individually, all present.
- **References [1]–[18]** gapless, unchanged.
- **Both** scoped *"Within the reviewed literature"* statements present.
- **Page count 6**, A4, measured on the rendered PDF.
