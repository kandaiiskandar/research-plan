TASK: AMICT MANUSCRIPT V4 — POST-DRAFT SCIENTIFIC AND REVIEWER AUDIT

Context
-------
The evidence-led V4 conference manuscript now exists:

    publications/active/ipsci-2026/submissions/v4-amict-rebuild/manuscript.md

Draft status:

    MANUSCRIPT_V4_DRAFT = COMPLETE
    RQ_COUNT = 3
    HEADLINE_CONTRIBUTIONS = 2
    RESULTS_SECTION_LARGEST = YES
    PROTECTED_DISCLOSURES = PASS (19/19)
    DOUBLE_BLIND_CHECK = PASS
    PROVENANCE_OPEN_ITEMS = 1

Do NOT format the manuscript yet.

This task is a scientific/reviewer audit of the actual drafted text.

==================================================
1. OBJECTIVE
==================================================

Audit V4 as if reviewing it for conference submission.

The task must answer:

1. Are all manuscript claims supported at the strength written?
2. Did any novelty overclaim return during prose drafting?
3. Are C1 and C2 still faithful to the contribution freeze?
4. Do RQ1–RQ3 receive direct, sufficient answers?
5. Are citations attached to the correct claims?
6. Are any references mischaracterised?
7. Are formal and empirical evidence types kept separate?
8. Are all protected disclosures preserved in context?
9. Is the draft scientifically self-contained enough for conference review?
10. Are there wording defects likely to trigger reviewer criticism?

This task may make surgical manuscript edits where a defect is
clearly established.

Do NOT redesign the science.

==================================================
2. AUTHORITIES
==================================================

Read:

    publications/active/ipsci-2026/submissions/v4-amict-rebuild/manuscript.md
    publications/active/ipsci-2026/submissions/v4-amict-rebuild/drafting-report.md

Binding freezes:

    data/amict-conference-rebuild/contribution-freeze-v2.md
    data/amict-conference-rebuild/contribution-claim-matrix.csv
    data/amict-conference-rebuild/rq-narrative-freeze.md
    data/amict-conference-rebuild/rq-evidence-map.csv
    data/amict-conference-rebuild/source-validation-report.md
    data/amict-conference-rebuild/novelty-audit-report.md
    data/amict-conference-rebuild/novelty-audit-addendum-001.md

Formal/evaluation authorities:

    publications/active/journal-1/evaluation-specification.md
    publications/active/journal-1/algorithm-specification.md
    docs/canonical/appendix-c-formalisation.md

Do not use v3 as authority where V4 or a frozen artefact supersedes it.

==================================================
3. AUDIT MODE
==================================================

Audit every substantive sentence into one of:

    PASS
    PASS_WITH_SCOPE
    REVISE
    REMOVE
    OPEN

For each REVISE/REMOVE/OPEN item record:

- exact manuscript location
- current wording
- defect type
- authority/evidence
- required action
- whether the defect is submission-blocking

Defect types include:

    NOVELTY_OVERCLAIM
    SCOPE_OVERCLAIM
    CITATION_MISMATCH
    EVIDENCE_TYPE_CROSSING
    NUMERIC_PROVENANCE
    FORMAL_MODEL_MISMATCH
    COMPARATOR_MISSTATEMENT
    LIMITATION_DROPPED
    DOUBLE_BLIND_RISK
    SELF_CONTAINMENT
    TERMINOLOGY
    LANGUAGE_CLARITY

==================================================
4. PRIORITY CHECK — ABSTRACT GAP CLAIM
==================================================

Audit this Abstract claim:

    "but has not been given a corresponding operational treatment
    in the AI governance literature"

The frozen novelty boundary requires scoped absence language.

Compare it against the canonical gap statement:

    "Within the reviewed AI decision-support and governance
    literature, we did not identify..."

If the abstract wording makes a claim about the state of the entire
literature rather than the reviewed corpus:

    REVISE

Prefer a concise scoped formulation such as:

    "but we did not identify a corresponding operational treatment
    in the reviewed AI-governance literature"

Do not strengthen the claim.

==================================================
5. PRIORITY CHECK — TCAS HUMAN-AUTHORITY WORDING
==================================================

Audit Introduction wording:

    "and the admissible set contracts to empty while the crew retains
    the aircraft"

Check:

- grammatical clarity;
- consistency with FAA AC 20-151C;
- consistency with the novelty audit's conclusion that human-authority
  distinction relative to TCAS is real but thin;
- risk of implying unconditional human authority in TCAS.

If unsupported or ambiguous, revise by removing the crew-authority
clause rather than creating a stronger comparison.

The purpose of the sentence is only to establish the mechanism
precedent.

==================================================
6. PRIORITY CHECK — "THREE LARGE-SCALE SYSTEMATIC REVIEWS"
==================================================

Audit Related Work sentence describing:

    "three large-scale systematic reviews"

and citation range:

    [1]–[6]

Inspect the actual reference types.

Do not assume this inherited label is correct.

If the references do not support exactly three systematic reviews,
revise the sentence to state only what the sources support.

Possible safe direction:

    "The first is the structured review of 72 papers that established
    the original governance framing and comparator set..."

and then cite only sources actually supporting the associated claim.

Do not invent a review count.

==================================================
7. PRIORITY CHECK — COMPANION JOURNAL TREATMENT
==================================================

Audit Section III statement:

    "Proofs are given in the companion journal treatment."

Questions:

1. Is that journal treatment publicly accessible to conference
   reviewers?
2. Does referring to it create a double-blind identification risk?
3. Does V4 depend on unpublished material for a claim that should be
   self-contained?
4. Is the statement necessary?

If the answer creates reviewer risk, prefer:

    "The full proofs are omitted here for space; only the properties
    used by the evaluation are stated."

or another wording supported by the frozen artefacts.

Do not add a self-citation unless double-blind handling is explicitly
resolved.

==================================================
8. ABSTRACT AUDIT
==================================================

Audit each abstract sentence for:

- scoped novelty
- no mechanism invention
- no safety/effectiveness inference
- correct empirical denominator
- correct interpretation of 5.81%, 4.48%, 0.00%
- plain-text/no-symbol compliance
- no unsupported literature-wide statements

The abstract must be independently defensible.

==================================================
9. INTRODUCTION AUDIT
==================================================

Check especially:

    "AI decision-support systems ... are typically governed by a
    binary question"

Determine whether "typically" is supported.

If not, scope to:

    reviewed systems
    common governance framing
    the comparator framing used in this study

Do not make global prevalence claims without evidence.

Verify:

- canonical gap statement verbatim
- canonical novelty-positioning sentence verbatim
- all three RQs verbatim
- exactly two contributions
- no old review contribution

==================================================
10. RELATED WORK CLAIM-CITATION AUDIT
==================================================

For every row of TABLE I and each synthesis sentence:

- verify governed object
- verify runtime state source
- verify whether advisory type is actually conditioned
- verify formal guarantee description
- verify relation-to-this-work wording

Special care:

    TCAS / ACAS
    ACAS X
    Parasuraman
    Bernabei
    Kwon & Kim
    shielding
    Flehmig / Baxi / Kang

Kang remains supplementary and non-load-bearing.

Do not allow a preprint to carry a central novelty claim.

==================================================
11. FORMALISATION AUDIT
==================================================

Check notation and semantics against canonical authority:

    S = f(E)
    Obs_i
    rho_D,tau
    F_D,tau
    G(S)
    A_AI(S)
    RS(S)

Verify:

- ideal/deployed distinction
- invalid/absent/stale handling
- declared exclusion
- exclusion-before-fault
- D fixed
- t not in D
- pinned SAFE
- lower-bound consequence
- operational totality
- pre-reasoning supply/no post-filter

Flag any sentence that simplifies these enough to become false.

==================================================
12. FORMAL PROPERTY AUDIT
==================================================

Verify that:

    totality
    monotonicity
    Safety Dominance
    containment

are presented as properties established by this formalisation,
not as novel properties.

Audit whether all formal-property wording is internally consistent.

Do not turn "formal verification" into empirical validation.

==================================================
13. FIDELITY AUDIT
==================================================

Verify every implementation-fidelity number:

    292
    32
    260
    244
    16
    454
    162
    F1/F2/F3 = 0

Verify wording preserves:

    records != types
    Delay only
    SAFE set empty
    R-SAFE-001 deferred
    restrictive-side only

Do not allow "validated", "proven", "complete" or equivalent to
overstate this evidence.

==================================================
14. EVALUATION METHOD AUDIT
==================================================

Check:

- 43,848 hourly records
- departure-window definition
- small-vessel scope
- thresholds/source claims
- NOAA / USNO wording
- COLREG use
- four comparator definitions
- PRIMARY vs RESOLUTION distinction
- D = {m}
- kappa = 0 consequence

Do not silently restore superseded model descriptions.

==================================================
15. RESULTS AUDIT
==================================================

Verify:

PRIMARY:
    C0<->C1 = 42.88%
    C0<->C2 = 48.69%
    DeltaL2 = 5.81%
    C1<->C3 = 0.00%

RESOLUTION:
    DeltaL2 = 4.48%
    C1<->C3 = 0.00%

Prohibited:

    41.08%
    45.56%

unless provenance has separately been repaired.

Check whether any sentence turns descriptive census results into
statistical inference.

==================================================
16. RQ3 INTERPRETATION AUDIT
==================================================

Pay special attention to this current interpretation:

    "The direction of movement is consistent with a finer model
    resolving nearshore sheltering that the coarser grid cell averages
    away..."

Determine whether this causal/explanatory interpretation is directly
supported by the frozen evidence.

If it is only plausible interpretation rather than established
evidence:

    PASS_WITH_SCOPE or REVISE

Possible safer form:

    "The configurations differ in both wave model and record length;
    this evaluation does not isolate which difference accounts for
    the observed 1.3 percentage-point spread."

Do not imply the finer model caused the lower divergence unless the
evidence isolates that mechanism.

==================================================
17. ZERO-DIVERGENCE CONTROL AUDIT
==================================================

Verify that C1<->C3 = 0.00% is always bounded to the evaluated
comparator definitions.

Check for any text that implies:

    all traffic-light systems
    all three-state governance
    advisory-scope governance universally superior

Revise if found.

==================================================
18. DISCUSSION AUDIT
==================================================

Check:

- mechanism precedent acknowledged
- C1 stated at frozen strength
- C2 stated at frozen strength
- zero-divergence interpretation bounded
- no safety/effectiveness inference
- generalisation conditional remains formal
- cross-domain demonstration explicitly absent
- target-hardware evidence absent
- no human study

==================================================
19. SITE-DISCLOSURE DECISION
==================================================

Current manuscript gives:

    5.98 N, 116.01 E

without naming the city.

Assess double-blind and reproducibility separately.

Do not assume omitting the city anonymises the site when exact
coordinates remain.

Preferred scientific wording, unless a venue-specific blind-review
rule requires stronger masking:

    "a coastal site in Sabah, Malaysia (5.98 N, 116.01 E)"

If keeping coordinates, record that this is a reproducibility choice,
not an anonymisation device.

Do not change site disclosure automatically unless justified.

==================================================
20. BUILD COMMENT
==================================================

The Markdown build-comment block contains internal repository paths.

Set:

    BUILD_COMMENT = REMOVE_BEFORE_SUBMISSION

It may remain during scientific audit if useful.

Do not allow it into the formatted submission.

==================================================
21. REFERENCE AUDIT
==================================================

For all 20 references verify:

- cited in manuscript where needed
- no orphan references
- no missing reference for surviving factual claim
- metadata adequate
- reference type represented accurately in prose
- AC 20-151C current
- Cleaveland spelling correct

Do not add references merely to raise the count.

==================================================
22. DOUBLE-BLIND AUDIT
==================================================

Re-check the actual manuscript, not only the report.

Audit:

- build comments
- self-citation phrasing
- "companion journal treatment"
- project/site wording
- acknowledgements
- repository references
- named institutional relationships

Return:

    DOUBLE_BLIND_SCIENTIFIC_TEXT = PASS / FAIL
    DOUBLE_BLIND_FORMATTING_PREP = PASS / FAIL

The build comment can make formatting-prep FAIL even if scientific
body text PASSes.

==================================================
23. LANGUAGE / REVIEWER-FRICTION AUDIT
==================================================

Flag wording that is technically true but likely to confuse a reviewer.

Examples:

- "crew retains the aircraft"
- undefined shorthand
- excessive bold emphasis
- claims whose denominator is not obvious
- sentences that make a formal property sound empirical
- sentences that imply causation from descriptive comparison

Make only surgical edits.

Do not stylistically rewrite the whole manuscript.

==================================================
24. WORD-BUDGET RULE
==================================================

After edits:

    Results must remain the largest prose section.

Do not increase total body materially.

Target:

    BODY_WORD_COUNT <= approximately 3,800

Protected disclosures remain mandatory.

==================================================
25. REQUIRED OUTPUT
==================================================

Create:

    publications/active/ipsci-2026/submissions/v4-amict-rebuild/
    post-draft-audit.md

If surgical corrections are unambiguously required, edit:

    manuscript.md

Do not create a new manuscript version yet.

The audit must include:

1. Executive verdict
2. PASS / PASS_WITH_SCOPE / REVISE / REMOVE / OPEN counts
3. Submission-blocking defects
4. Abstract audit
5. Introduction audit
6. Related Work citation audit
7. Formalisation audit
8. Fidelity audit
9. Evaluation/Results audit
10. Discussion audit
11. Reference audit
12. Double-blind audit
13. Site-disclosure decision
14. Build-comment decision
15. Word counts after edits
16. Changed files
17. Remaining open items

==================================================
26. STOP CONDITIONS
==================================================

STOP and mark:

    POST_DRAFT_AUDIT = BLOCKED

if:

1. a frozen contribution is unsupported in the actual manuscript;
2. an RQ cannot be answered from the included evidence;
3. a load-bearing Related Work distinction collapses;
4. a required empirical number conflicts with authority;
5. conference self-containment requires new scientific evidence;
6. correcting the draft would require changing architecture,
   comparator definitions or thresholds;
7. the manuscript cannot remain within the budget after necessary
   corrections.

Do not repair scientific evidence during this task.

==================================================
27. SUCCESS STATUS
==================================================

If successful:

    POST_DRAFT_AUDIT = CLOSED
    MANUSCRIPT_V4_SCIENTIFIC_TEXT = REVIEWER_READY
    RQ_COUNT = 3
    HEADLINE_CONTRIBUTIONS = 2
    RESULTS_SECTION_LARGEST = YES
    PROTECTED_DISCLOSURES = PASS
    BUILD_COMMENT = REMOVE_BEFORE_SUBMISSION
    DOUBLE_BLIND_SCIENTIFIC_TEXT = PASS
    FORMAT_READY = NO

FORMAT_READY remains NO until:

- current AMICT template obtained
- current-cycle page limit confirmed
- build comment removed
- final pagination completed

==================================================
28. FINAL REPORT
==================================================

End with:

    POST_DRAFT_AUDIT = <status>
    MANUSCRIPT_V4_SCIENTIFIC_TEXT = <status>
    CLAIMS_REVISED = <count>
    CLAIMS_REMOVED = <count>
    OPEN_ITEMS = <count>
    BODY_WORD_COUNT = <count>
    RESULTS_SECTION_LARGEST = <yes/no>
    PROTECTED_DISCLOSURES = <pass/fail>
    DOUBLE_BLIND_SCIENTIFIC_TEXT = <pass/fail>
    BUILD_COMMENT = REMOVE_BEFORE_SUBMISSION
    FORMAT_READY = NO

Then report:

- every manuscript edit made
- every remaining scientific concern
- whether site wording changed
- whether any reference was added/removed
- whether current template/page-limit confirmation remains outstanding

Do not proceed to template formatting.