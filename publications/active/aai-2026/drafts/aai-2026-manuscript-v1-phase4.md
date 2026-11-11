# VI. Limitations and Conclusion

The replay concerns one deployment site and should not be read as a population estimate for other locations. The activation frequency is conditional on threshold interpretation, with the wave CAUTION onset producing the largest sensitivity. Several governance choices remain researcher-defined rather than empirically validated: the three-state cardinality, the evaluation policies fixed in Section IV, and the admissible set A<sub>AI</sub>(CAUTION) = {Go, Delay}. The evaluation measures how often that restriction binds. It does not establish that {Go, Delay} is the correct, optimal or safer set at CAUTION, and the reported measure is invariant to its content. The marine-warning component has no usable archive for the replay period and was held at its least-severe value, so activation frequencies are interpreted as lower bounds.

The study characterises governance activation; it does not validate it. No incident or outcome record exists for the site, so activation is not linked to unsafe departures or avoided harm. No generated advice is evaluated: the metric ranges over admissible recommendation types, not over the correctness, quality or usefulness of any recommendation. No user study has been conducted, so interpretation, acceptance, trust, behavioural response and human oversight in use remain untested. The replay is a deterministic census rather than a sample, so no statistical inference applies, and the vessel-class variants are configuration checks, not evidence of generalisation across classes, sites or periods. Field work should test the threshold mappings and the restricted set with domain stakeholders, examine how users interpret the advice, and relate activation to operational outcomes before any safety or generalisation claim is made.

The question addressed was whether a declared intermediate risk level changes what an advisory system is permitted to recommend, and how often. Stating a criterion on admissible sets and isolating the intermediate level with a four-configuration comparator, the contracting level was reached in 5.81% of PRIMARY departure-window hours and 4.48% under RESOLUTION: a lower bound, within a 5.67–9.56% sourced envelope, 97.6% attributable to one component, and falling to 1.96% and 1.26% for larger vessel classes. These are conditional measurements rather than stable site properties; the contribution is the assembly that makes such a figure interpretable, together with the criterion. For Responsible AI governance, the implication is that a declared risk level can be examined not only by its label, but by the admissible recommendations it changes and the conditions under which that change binds.

---

## Drafting Audit

| # | Check | Result |
|---|---|---|
| 1 | Section VI prose word count | **390** — inside target 350–390, at the top of the preferred 370–390 band; ceiling 410 not reached. Three paragraphs: 120 / 136 / 134 |
| 2 | One-site limitation explicit | **YES** — first sentence |
| 3 | No representativeness claim | **YES** — *"should not be read as a population estimate for other locations"*; no sampling-design language |
| 4 | Threshold dependence explicit | **YES** — conditional on threshold interpretation, wave CAUTION onset named as the largest sensitivity; no claim that thresholds are arbitrary, unreliable or optimal |
| 5 | A<sub>AI</sub>(CAUTION) researcher-defined status preserved | **YES** — named among choices *"researcher-defined rather than empirically validated"* |
| 6 | {Go, Delay} not claimed correct/optimal/safer | **YES** — denied explicitly, with the invariance consequence attached |
| 7 | Marine-warning exclusion acknowledged | **YES** — one sentence: no usable archive, held at least-severe value |
| 8 | Lower-bound interpretation preserved | **YES** |
| 9 | Lower bound not presented as a new method | **YES** — stated as a qualification; no partial identification, no bounds literature, no Manski |
| 10 | No safety-outcome validation claim | **YES** — *"no incident or outcome record exists for the site"* |
| 11 | No generated-advice validation claim | **YES** — metric ranges over admissible types, not correctness, quality or usefulness |
| 12 | No human-validation claim | **YES** — interpretation, acceptance, trust and behavioural response stated as untested |
| 13 | No meaningful-human-control claim | **YES** — the phrase does not appear; human oversight appears only as *"in use remain untested"* |
| 14 | No generalisation claim | **YES** — classes, sites and periods named as not established |
| 15 | Vessel-class variants not treated as generalisation | **YES** — *"configuration checks, not evidence of generalisation"* |
| 16 | Deterministic-census status preserved | **YES** |
| 17 | No statistical inference introduced | **YES** — no p-value, confidence interval or significance; *"no statistical inference applies"* |
| 18 | Future validation follows from limitations | **YES** — one sentence mapping to thresholds, restricted set, user interpretation and operational outcomes |
| 19 | Future work does not imply completed validation | **YES** — *"before any safety or generalisation claim is made"*; nothing promised as done |
| 20 | Conclusion answers the governance-measurement problem | **YES** — opens by restating the question as *whether* and *how often* |
| 21 | PRIMARY 5.81% used only as binding/activation frequency | **YES** — *"reached in 5.81% of PRIMARY departure-window hours"*; no improvement, gain or effectiveness reading |
| 22 | RESOLUTION 4.48% correctly scoped | **YES** — attached to the RESOLUTION configuration |
| 23 | Results described as conditional measurements | **YES** |
| 24 | No stable-site-property claim | **YES** — denied in the same sentence |
| 25 | Responsible AI implication stated | **YES** — final sentence |
| 26 | Responsible AI implication limited to operational auditability | **YES** — label versus admissible recommendations changed and the conditions under which the change binds; no ethics, trustworthiness or safety framing, and no universal quantifier |
| 27 | No architecture novelty claim | **YES** |
| 28 | No mechanism novelty claim | **YES** — no mechanism is named as contributed |
| 29 | Criterion not called theorem/proposition/proof | **YES** — *"a criterion on admissible sets"* |
| 30 | No claim three-state is better than binary | **YES** |
| 31 | No optimality claim | **YES** |
| 32 | No new result introduced | **YES** — every figure is locked and already in Section V |
| 33 | No new experiment introduced | **YES** |
| 34 | No new literature discovery | **YES** |
| 35 | No new citation introduced | **YES** — Section VI carries no citation key |
| 36 | IPoSCI absent | **YES** |
| 37 | FIGURE DATA EXTRACTION REQUIRED carried forward | **YES** |
| 38 | MFWAM citation-resolution task carried forward | **YES** |

**39. Unsupported claim.** None. Six numerals appear — 5.81%, 4.48%, 5.67–9.56%, 97.6%, 1.96%, 1.26% — all from the locked chain §§11–12 and all already reported in Section V. No new number was introduced, satisfying the architecture's constraint for this section.

**40. Deviation from the patched locked research chain.** None from the chain. One declared deviation from the lower-authority **architecture §17 conclusion content map**: its sentence 3 pairs the 5.81% statement with *"the non-contracting three-state configuration was identical to a binary gate."* That C1/C3 clause is omitted here, on the Phase 4 brief's explicit instruction to prefer omitting C1/C3 from Section VI because Section V already establishes it as an entailed conformance check. The omission removes a restatement, not a qualification, and nothing in Section VI can now be read as an empirical finding about three-state designs.

**41. Statement changing the epistemic status of an existing result.** None. The lower bound remains a qualification, the envelope remains a deterministic configuration range, the vessel-class figures remain robustness disclosures, and 97.6% remains an attribution of CAUTION classification.

**42. Material repetition that should be compressed.** One, retained deliberately. The lower-bound status appears at the end of paragraph 1 and again as the two words *"a lower bound"* in paragraph 3. It is kept because the binding drafting contract (item 15) requires the headline figures never to appear without the envelope, wave dominance, `g_o` 97.6% and the vessel-class figures, and the architecture's conclusion map likewise carries the lower bound into the closing sentence. Compressing it further would leave 5.81% unqualified at the point a reader is most likely to extract it.

### Compliance with MUST REPORT item 15

The headline does not appear alone. In paragraph 3, 5.81% and 4.48% are stated together with the 5.67–9.56% sourced envelope, the 97.6% single-component attribution and the 1.96% / 1.26% vessel-class figures; wave dominance is carried in paragraph 1 as the largest sensitivity rather than repeated numerically.

### Carried forward

**FIGURE DATA EXTRACTION REQUIRED.** Figure 1 in Section V remains a placeholder. No script was run, no coordinates were generated, and the task is unchanged.

**CITATION-RESOLUTION TASK — MFWAM.** Unresolved. Not searched, invented, replaced or removed.

### Cross-phase consistency check

No conflict detected.

**Section I** — the contribution sentence in paragraph 3 restates the scoped assembly and criterion; it claims nothing the introduction did not already scope, and adds no second contribution or second RQ.
**Section II** — no mechanism is claimed. Runtime restriction, graduated levels, the three-state topology, activation-frequency measurement, sensitivity analysis and comparator methodology are absent from Section VI as claims of any kind, so the page-1 concession stands unqualified.
**Section III** — the criterion is referred to as a criterion. The invariance consequence of Δ<sub>L2</sub> ≡ P(S = CAUTION) is carried in the sentence denying that {Go, Delay} is validated, and the comparator ladder is never implied to have been necessary to obtain the figure.
**Section IV** — the researcher-defined choices and the declared-exclusion lower bound are restated in the same status Section IV assigned them, and the cross-reference to Section IV avoids re-listing them.
**Section V** — the conditional framing, the non-claims and the locked closing wording are consistent. Section VI does not restate the V-C sentence, and uses no term from the prohibited effectiveness family.

### Final logical check

**A.** No. 5.81% appears only as *"reached in 5.81% of PRIMARY departure-window hours"*, with no improvement, gain or effectiveness predicate anywhere in the section.
**B.** No. The sentence denying that {Go, Delay} is correct, optimal or safer is explicit, and the invariance of the measure to the set's content is stated immediately after it.
**C.** No. Thresholds are described as an interpretation the result is conditional on, with the wave onset as the largest sensitivity; they are not called optimal, and not called arbitrary or unreliable either.
**D.** No. Interpretation, acceptance, trust, behavioural response and human oversight in use are all stated as untested, and no user study is described.
**E.** No. Generalisation across classes, sites and periods is denied, the vessel-class variants are labelled configuration checks, and the one-site restriction opens the section.
**F.** Yes. The closing paragraph opens by naming the question as whether a declared intermediate risk level changes what the system is permitted to recommend, and how often.
**G.** Yes. The closing point is that a declared level can be examined by the admissible recommendations it changes and the conditions under which that change binds — operational auditability, not ethics, trustworthiness or safety effectiveness, and stated for this examination rather than as a universal rule.

---

PHASE 4 STATUS: READY FOR INTEGRATION
