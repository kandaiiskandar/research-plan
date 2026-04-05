# Examiner & Supervisor Feedback

**Candidate**: Iskandar
**Document reviewed**: Literature Review Plan (review-plan.md) and Paper Tracker (paper_tracker.md)
**Date**: 5 April 2026
**Papers analysed**: 49 (25 full extraction, 24 reduced extraction)

---

## Overall Assessment

The analytical framework underpinning this literature review is exceptionally systematic — among the strongest I have seen at this stage of a PhD. The governance level distribution table, formal component coverage matrix, and argumentative chain with explicit transitions demonstrate a level of structural rigour that will serve the candidate well under examination. The gap claim — that zero papers implement unified two-level environment-state-conditioned governance — is precisely stated and supported by converging evidence from multiple independent surveys (Newcomb: 46 papers, Ramos: 91 papers, Bengio: 11 frameworks).

The main risks are methodological (PS4/PS5 evaluation design), defensive (the Baxi differentiator and domain choice justification), and coverage-related (T4 depth). None are fatal; all require targeted strengthening before submission.

---

## Strengths

### S1: Argumentative Chain

The nine-link argumentative chain (Section 5) is the backbone of a strong literature review. Links 1–7 build a compelling, logical progression from context → established paradigm → gap → domain motivation. The transition sentences read as a constructed narrative rather than a catalogue of papers. This is exactly what examiners want to see — a literature review that *argues*, not one that merely *reports*.

### S2: Governance Level Analysis

The table in Section 3 showing governance level distribution across all 49 papers is particularly effective. The progression from "~15 papers implement Level 1 only" to "~10 papers implement any form of Level 2" to "2 papers implement state-conditioned Level 2" to "0 papers implement unified two-level environment-state-conditioned governance" is the kind of evidence examiners find persuasive because it is falsifiable and precise.

### S3: Formal Component Coverage

Section 4 clearly separates what has precedent, what has structural analogs, and what is genuinely novel. This is exactly the scaffolding that makes a contribution claim defensible. The identification of Baxi's nested tier permissions as a structural analog to the containment property — while distinguishing the conditioning variable — shows mature analytical judgement.

### S4: Citation Chain Mapping

Section 6 maps citation relationships between papers in the set and identifies where the candidate's contribution enters each cluster. The observation that the fisheries cluster is entirely isolated from the safety governance cluster — and that the candidate's work bridges them — is a strong positioning insight.

---

## Substantive Concerns

### C1: The "0 Papers" Claim Needs Defensive Anticipation

**Severity: High**

The central gap claim is powerful but also the most vulnerable point under examination. An examiner will probe this in two directions:

1. **Completeness of search**: Is it possible that the literature search missed relevant work? The review plan does not document the search methodology — databases searched, search strings used, inclusion/exclusion criteria, or a PRISMA flow diagram. With 49 papers, the corpus is respectable, but without a reproducible protocol an examiner cannot audit the claim. A systematic or semi-systematic search protocol must be documented and presented alongside the gap claim.

2. **Necessity of the contribution**: Is it possible the gap exists because tripartite governance is not a useful thing to build? The plan partially addresses this through fisheries domain motivation (Gao's go/cautious-go/don't-go mapping), but the *theoretical* argument for why tripartite governance is architecturally superior to binary governance with post-hoc filtering is underdeveloped. The argument currently rests on "it doesn't exist" — it also needs "and here is why it *should* exist, from first principles."

**Recommendation**: (a) Include a search methodology section with PRISMA flow. (b) Add a brief first-principles argument for why binary governance is structurally inadequate — e.g., that binary governance forces a choice between over-restriction (disabling AI when partial assistance would be safe and valuable) and under-restriction (permitting full AI participation when conditions warrant caution). The fisheries domain provides empirical evidence that practitioners already make this tripartite distinction informally.

### C2: PS4 and PS5 "Unsupported" — Methodological Risk

**Severity: High**

PS4 (no comparative evaluation of graduated vs binary governance) and PS5 (no socio-technical evaluation of CAUTION mode) are correctly identified as unsupported by the literature. However, from an examiner's perspective, these are not just literature gaps — they are *methodological risks* for the dissertation. If nobody has done this evaluation, there is no validated evaluation framework to adapt. The candidate will be designing evaluation instruments from scratch.

**Recommendation**: Actively search for and incorporate proxy methodologies:

- **Levels of automation literature**: Sheridan and Verplank (1978), Parasuraman et al. (2000), the SAE J3016 automation levels for driving — decades of work on human response to graduated automation, directly applicable to evaluation design.
- **Trust calibration literature**: Lee and See (2004) provide the foundational trust-in-automation framework; Jian et al. (2000) provide a validated trust scale widely used in human-AI studies.
- **Automation surprise and mode confusion**: Studies of automation mode confusion in aviation (e.g., Sarter and Woods, 1995) are directly relevant to PS5 — how users understand and respond to a system operating in an intermediate governance mode.

Positioning these as methodological foundations turns PS4 and PS5 from "unsupported" to "methodologically grounded but not yet applied to governance architectures."

### C3: The Baxi Differentiator Requires Sharper Articulation

**Severity: Medium**

Baxi is correctly identified as the structurally closest analog — graduated tiers with containment, formally expressed. The stated differentiator is "robustness-conditioned vs environment-conditioned." An examiner will ask: **is this distinction sufficient to constitute a novel contribution, or is it merely a change of input variable?**

The answer likely lies in the *runtime observability* argument:

- Environmental state is observable through sensors in real-time and changes dynamically during operation, requiring continuous reclassification and governance adjustment.
- Agent robustness is an assessed property determined through evaluation, producing relatively static tier assignment.

These two conditioning variables demand different observation mechanisms, update frequencies, and governance response dynamics. This distinction must be made explicit in the review — currently it is implied but not argued.

**Recommendation**: Add a brief comparative analysis (possibly as a table) contrasting the architectural implications of conditioning on environmental state vs agent robustness: observation mechanism, update frequency, governance response latency, failure mode under misclassification, and applicability to dynamic operational environments.

### C4: Domain Justification May Appear Opportunistic

**Severity: Medium**

The review includes 10 fisheries/maritime papers, but as correctly noted, none implements any AI governance mechanism. This is simultaneously the strongest motivation ("the domain needs this") and a potential weakness ("why not apply the architecture to automotive or healthcare where richer comparators exist?").

**Recommendation**: Develop a crisp argument for why the fisheries domain is not just *a* valid application but *the right* application. Three elements should be foregrounded:

1. **Environmental variability as a first-class concern**: Unlike automotive or industrial domains where the operating environment is relatively controlled, fisheries operations face continuously varying environmental conditions (weather, sea state, visibility, tidal patterns) that directly determine operational safety — making environmental-state-conditioned governance particularly natural.
2. **Existing informal graduated decision-making**: Gao's (2024) empirical finding that Penang fishers already use an informal go/cautious-go/don't-go decision framework maps directly to the proposed SAFE/CAUTION/UNSAFE classification. This is not an imposed abstraction; it formalises existing practice.
3. **Resource constraints that make binary governance costly**: In a low-resource environment where AI assistance is valuable but intermittent, a binary gate that disables AI entirely under moderate risk wastes a scarce resource. The CAUTION mode is specifically designed for contexts where partial AI assistance is more valuable than no AI assistance.

Make Gao's findings the centrepiece of the domain justification rather than treating them as one paper among several.

### C5: Theme T4 (Low-Resource) Remains the Thinnest Coverage Area

**Severity: Medium**

Four "Yes" papers for a theme that appears in the dissertation title is a concern. The "Partially Covered" label somewhat understates the risk: an examiner will ask whether the low-resource deployment constraints that the architecture must satisfy have been adequately characterised.

Katende (2026) appears to carry most of this weight. Peskas (Longobardi et al., 2025) helps but describes a data platform, not a decision architecture.

**Recommendation**: Add 2–3 papers that specifically address AI system design under resource constraints. Candidate areas:

- **Edge AI and offline-first architectures**: Systems designed for intermittent connectivity, relevant to the fisheries deployment context.
- **Disaster response AI**: Emergency response systems operating under communication breakdown and resource scarcity — similar constraint profile to coastal fisheries.
- **Remote healthcare / telemedicine AI**: Decision support under limited bandwidth and specialist scarcity — a more mature literature with directly transferable design patterns.

These need not be core architectural comparators; they can serve as background establishing that the constraints are well-characterised and the proposed architecture's design choices (e.g., local state classification, pre-cached recommendation logic) are motivated by documented deployment challenges.

### C6: Venue Quality Distribution

**Severity: Low**

Several core architectural comparators — Bajcsy/Fisac, Dalrymple, and Baxi — are arXiv preprints. For a PhD literature review this is not disqualifying, especially in a rapidly evolving field, but an examiner may question whether core comparators have survived peer review.

**Recommendation**: Where peer-reviewed versions of arXiv preprints have been published (or accepted), cite those instead. Where they have not, acknowledge the pre-print status briefly when introducing the paper (e.g., "Dalrymple et al. (2024, preprint) propose..."). This signals awareness without undermining the citation. The strongest peer-reviewed anchors in the set — Perez-Cerrolaza in *ACM Computing Surveys*, Könighofer in *Communications of the ACM*, Wang in *ICSE* — should be prominently positioned as core references.

---

## Structural Recommendations

### R1: Merge Sections 2 and 3 of the Proposed Outline

The proposed seven-section outline separates Level 1 governance (Section 2) from Level 2 governance (Section 3). This risks reading as a taxonomy rather than a narrative. Consider integrating them into a single section — "AI Safety Governance Mechanisms" — with an internal structure that moves from the well-established (binary participation control) to the emerging (output scope restriction) to the absent (state-conditioned two-level governance). This creates a single continuous escalation toward the gap rather than two separate stops with a transition between them.

### R2: Add a Comparative Summary Table

Include a summary table comparing the top 6–8 comparator architectures across a consistent set of dimensions: governance trigger (environmental state vs performance vs robustness), governance level (L1 only, L2 only, L1+L2), governance mode (binary vs graduated), runtime vs design-time, and formal safety property (if any). This table would serve as a visual anchor for the gap argument and give examiners a quick reference for understanding the positioning.

### R3: Position the Contribution Earlier

The current plan defers the explicit contribution statement to the end of the argumentative chain (after Link 9). Consider inserting a brief forward reference to the proposed architecture at the end of Section 2.3 or 2.4, so that readers can evaluate subsequent sections with the contribution in mind. This is a standard rhetorical technique in PhD literature reviews — the reader should know what they are being led toward, not be surprised by it.

---

## Summary of Actions Required

| # | Action | Severity | Section affected |
|---|--------|----------|-----------------|
| 1 | Document search methodology with PRISMA flow | High | New section or appendix |
| 2 | Add first-principles argument for why binary governance is inadequate | High | Section 4 (Two-Level Gap) |
| 3 | Incorporate levels-of-automation and trust calibration literature for PS4/PS5 | High | Section 7 (Evaluation Gaps) |
| 4 | Sharpen Baxi differentiator with comparative analysis | Medium | Section 4 (Two-Level Gap) |
| 5 | Strengthen domain justification — foreground Gao, articulate why fisheries specifically | Medium | Section 6 (Domain Context) |
| 6 | Add 2–3 papers on AI design under resource constraints | Medium | Section 6 (Domain Context) |
| 7 | Check and prefer peer-reviewed versions of arXiv preprints | Low | Throughout |
| 8 | Merge governance Sections 2 and 3 into single section | Structural | Outline |
| 9 | Add comparative summary table of top comparators | Structural | Section 4 |
| 10 | Insert forward reference to contribution earlier in the review | Structural | Section 2.3 or 2.4 |
