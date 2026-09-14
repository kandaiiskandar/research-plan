TASK: AMICT CONFERENCE MANUSCRIPT V4 — EVIDENCE-LED SIX-PAGE DRAFT

Context
-------
The AMICT conference rebuild has passed all pre-drafting gates:

    NOVELTY_AUDIT = STOP_MATERIAL_EQUIVALENCE_FOUND
    SOURCE_CORPUS_VALIDATION = CLOSED
    CONTRIBUTION_FREEZE_V2 = CLOSED
    RQ_NARRATIVE_FREEZE = CLOSED

The manuscript may now be drafted.

The scientific position is frozen.

Do NOT redesign the science during drafting.

==================================================
1. OBJECTIVE
==================================================

Create a new Markdown conference manuscript that implements the frozen:

- title
- novelty position
- two headline contributions
- three research questions
- evidence hierarchy
- six-page narrative strategy
- required limitations and disclosures

The manuscript must be materially different from the rejected
architecture-only paper.

It must read as:

    known governance pattern
        ->
    operational formalisation
        ->
    bounded executable verification
        ->
    retrospective empirical evaluation

NOT:

    literature review
        ->
    new architecture proposal
        ->
    small evaluation appendix

==================================================
2. OUTPUT LOCATION
==================================================

Create a NEW submission version.

Do not modify:

    publications/active/ipsci-2026/submissions/v3-revision/manuscript-v3.md

First inspect the existing submission-version naming convention.

If no later version already exists, create:

    publications/active/ipsci-2026/submissions/v4-amict-rebuild/manuscript.md

Also create:

    publications/active/ipsci-2026/submissions/v4-amict-rebuild/drafting-report.md

Do not create .docx, .pdf or .tex.

==================================================
3. BINDING AUTHORITIES
==================================================

Read in full before drafting:

    data/amict-conference-rebuild/contribution-freeze-v2.md
    data/amict-conference-rebuild/contribution-claim-matrix.csv
    data/amict-conference-rebuild/rq-narrative-freeze.md
    data/amict-conference-rebuild/rq-evidence-map.csv
    data/amict-conference-rebuild/source-validation-report.md
    data/amict-conference-rebuild/novelty-audit-report.md
    data/amict-conference-rebuild/novelty-audit-addendum-001.md

Formal / evaluation authorities:

    publications/active/journal-1/evaluation-specification.md
    publications/active/journal-1/algorithm-specification.md
    docs/canonical/appendix-c-formalisation.md

Conference baseline:

    publications/active/ipsci-2026/submissions/v3-revision/manuscript-v3.md

Use v3 only as a source of reusable material.

Do NOT preserve its section structure by default.

==================================================
4. TITLE — FROZEN
==================================================

Use exactly:

    Evaluating Graduated Advisory-Scope Governance for AI Decision Support

No subtitle.

Do not propose alternatives.

==================================================
5. FINAL RESEARCH QUESTIONS — VERBATIM
==================================================

Use exactly:

RQ1:
    How can graduated advisory-scope governance be specified and
    verified operationally, separating AI participation from
    admissible advisory scope under incomplete, stale or excluded
    environmental observations?

RQ2:
    How often does graduated advisory-scope governance produce
    governance outcomes that differ from participation-only governance
    in retrospective environmental replay?

RQ3:
    How does the measured governance-outcome divergence differ under
    the alternative environmental-data configuration?

Do not paraphrase the RQs.

==================================================
6. HEADLINE CONTRIBUTIONS — EXACTLY TWO
==================================================

C1:
    formal operational specification / scoped generalisation

C2:
    empirical characterisation

Do not recreate the old literature-review contribution.

Set:

    OLD_REVIEW_HEADLINE_CONTRIBUTION = WITHDRAWN

Implementation fidelity:

    SUPPORTING_VERIFICATION_FOR_RQ1

not a third contribution.

==================================================
7. NOVELTY BOUNDARY
==================================================

Binding:

    MECHANISM_NOVELTY = WITHDRAWN

The paper must explicitly acknowledge that runtime restriction of
advisory types conditioned on externally measured state has precedent
in certified collision-avoidance avionics.

Do NOT claim:

- first
- first-ever
- unprecedented
- unique
- globally novel
- no existing architecture
- no prior system restricts advisory scope
- first formal advisory-admissibility mechanism
- first graduated governance architecture
- first environmental-state governance
- first nested admissible set

Do not rescue novelty by renaming the mechanism.

==================================================
8. CANONICAL GAP STATEMENT — VERBATIM
==================================================

Use exactly:

    Within the reviewed AI decision-support and governance literature,
    we did not identify a formal operational treatment that combines
    a classified multi-component environmental state, explicit
    observation-resolution and exclusion semantics, and a
    state-conditioned advisory-type admissibility contract. Analogous
    restriction of advisory types conditioned on an externally
    measured state is established practice in certified
    collision-avoidance avionics.

It must appear in the Introduction.

Do not weaken the avionics acknowledgement.

Do not strengthen the absence claim.

==================================================
9. CANONICAL NOVELTY-POSITIONING SENTENCE — VERBATIM
==================================================

Use exactly:

    This work formalises an existing governance pattern — runtime
    restriction of advisory types by an externally measured state,
    established in certified collision-avoidance avionics — as an
    operational specification over a classified multi-component
    environmental state, and characterises empirically how often its
    intermediate advisory-scope level produces a governance outcome
    distinct from participation-only governance.

Use this sentence verbatim in:

1. Introduction
2. contribution paragraph
3. Discussion

Do not create alternate versions.

==================================================
10. GENERALISATION BOUNDARY
==================================================

Allowed:

    generalised beyond a single hazard variable

Allowed with scope:

    domain-reinstantiable at the governance-structure level

Required qualifier:

    re-instantiation is specified and illustrated, not empirically
    demonstrated across domains

Do NOT write:

    domain-independent

as an engineering/applicability claim.

The formal statement that properties hold for any correct
instantiation satisfying the assumptions is allowed as FORMAL.

Do not convert it into a deployment claim.

==================================================
11. C1 — REQUIRED OPERATIONAL CONTENT
==================================================

C1 must foreground the operational formalisation.

Must include, concisely:

    S = f(E)

    (G(S), A_AI(S))

    Obs_i = (X_i x T) union {bottom}

    rho_D,tau

    F_D,tau = f o rho_D,tau

Required operational semantics:

- required missing observation -> bottom -> UNSAFE
- required stale observation -> bottom -> UNSAFE
- required invalid observation -> bottom -> UNSAFE
- declared unmeasured input -> exclusion
- exclusion-before-fault
- D fixed and declared
- t not in D
- excluded component pinned SAFE
- severity results become lower bounds when D != empty
- operational totality
- distinction between ideal f(E) and deployed F_D,tau
- admissibility supplied pre-reasoning through RS(S)
- no post-generation output filter

Do not reproduce full proofs.

State the formal properties compactly and point to their role.

==================================================
12. FORMAL PROPERTY DISCIPLINE
==================================================

The manuscript may state that the formalisation establishes:

- totality
- monotonicity
- Safety Dominance
- containment

But it must NOT call these properties novel.

Prior work establishes related formal properties.

Use them as verification of the formalisation.

Do not write:

    a novel monotonicity theorem
    a novel containment property
    the first formally verified graduated governance architecture

==================================================
13. RQ1 IMPLEMENTATION CONFORMANCE
==================================================

Implementation fidelity belongs inside Section III.

Allowed core statement:

    The executable implementation produced zero violations of the
    configured advisory admissibility contract within the bounded
    deterministic interface-contract fidelity state space.

Required nearby disclosure:

    R-SAFE-001 = DEFERRED
    SAFE rule set is empty
    four implemented rules are CAUTION rules
    generated conclusion type is Delay only
    454 advisory records, NOT types
    containment exercised only on the restrictive side

Relevant figures:

    primary episodes = 292
    SAFE = 32
    CAUTION = 260
    episodes with advisory = 244
    CAUTION empty advisory = 16
    advisory records = 454
    UNSAFE gate-off structural cases = 162
    F1 = 0
    F2 = 0
    F3 = 0

Do not over-expand this block.

==================================================
14. RQ2 / RQ3 — CORE EMPIRICAL EVIDENCE
==================================================

The Results section is the centre of the paper.

Core headline values:

PRIMARY:

    DeltaL2 = 5.81%
    C1 <-> C3 = 0.00%

RESOLUTION:

    DeltaL2 = 4.48%
    C1 <-> C3 = 0.00%

PRIMARY supporting context:

    C0 <-> C1 = 42.88%
    C0 <-> C2 = 48.69%

Replay scale:

    43,848 hourly records

Use:

    governance-outcome divergence

Do NOT use:

    safety improvement
    risk reduction
    improved decision quality
    effectiveness
    safer

==================================================
15. C1 <-> C3 INTERPRETATION
==================================================

Primary home:

    RQ2

Secondary support:

    RQ3

Allowed interpretation:

    Under the evaluated comparator definitions, adding an
    intermediate labelled governance state without advisory-scope
    differentiation produces no admissible-set divergence.

Do not generalise to all traffic-light or three-state systems.

This control is important.

Do not bury it in Discussion.

==================================================
16. PRIMARY / RESOLUTION DISCIPLINE
==================================================

PRIMARY and RESOLUTION are:

    alternative environmental-data configurations

They are NOT:

- confidence intervals
- repeated trials
- uncertainty estimates
- independent replications
- error bars

Do not write:

    robust
    preserved
    stable
    replicated

as a result of the configuration comparison.

Do not write:

    5.81 +/- 4.48

or equivalent.

==================================================
17. PROVENANCE OPEN ITEM
==================================================

Binding:

    RESOLUTION_PAIRWISE_C0_C1_C0_C2 = PROVENANCE_INCOMPLETE

Do NOT use as headline evidence:

    C0 <-> C1 RESOLUTION = 41.08%
    C0 <-> C2 RESOLUTION = 45.56%

until provenance is repaired.

The manuscript does not require these numbers.

Do not repair them during drafting.

==================================================
18. LOWER-BOUND DISCLOSURES
==================================================

The manuscript must state:

    D = {m}

because the marine-warning archive is unavailable.

Therefore severity results are lower bounds.

Also:

    kappa = 0 throughout the replay record

so rainfall-related severity figures are lower bounds by an unknown
margin for the unobserved storm-code component.

Do not imply complete hazard observation.

==================================================
19. WIND REPORTING
==================================================

If wind appears:

    g_w activation = 2 / 43,848 hours
    g_w binding = 0

Never write:

    wind never fires
    wind has no effect

Use the two-number rule.

==================================================
20. STALE / OPEN IMPLEMENTATION ITEMS
==================================================

Required limitations:

    age_i = specified but unparameterised
    reasons runtime capture = unimplemented
    R-SAFE-001 = DEFERRED
    E5 = OPEN
    H3 = OPEN_UNSUPPORTED
    no human study
    cross-domain re-instantiation not demonstrated

Do not invent values or close these gaps.

==================================================
21. REVIEW CORPUS REPORTING
==================================================

The original structured review sample remains:

    72 papers

The six novelty-validation works are:

    TARGETED_POST_REVIEW_ADDITIONS

Do not write:

    78 papers

Do not pretend the six were part of the original screening protocol.

Related Work should distinguish the two populations.

==================================================
22. RELATED WORK — TABLE LED
==================================================

Related Work must be compact.

Use one comparison table across these families:

1. TCAS II / ACAS II advisory inhibition
2. ACAS X formal verification
3. levels of automation
4. adaptive automation
5. selective prediction / deferral
6. shielding / action masking
7. graduated runtime governance

Suggested columns:

    governed object
    runtime state source
    runtime/design-time
    recommendation-type scope conditioned?
    human final authority
    formal guarantee

Use short synthesis prose only.

Do not recreate six v3 literature-review subsections.

Do not create a mini-SLR.

==================================================
23. SOURCE DISCIPLINE
==================================================

Use the validated sources already integrated in notes and the
citation map.

Load-bearing comparisons include:

- FAA AC 20-151C
- Cleaveland, Mitsch & Platzer (2023)
- Parasuraman, Sheridan & Wickens (2000)
- Bernabei & Costantino (2024)
- Kwon & Kim (2026)
- FDA CDS guidance (2026)

Also use relevant existing corpus sources where needed:

- Punzi et al.
- shielding/action masking
- Flehmig et al.
- Baxi
- Kang

Kang is supplementary / preprint and must not become load-bearing.

Do not introduce unvalidated new sources during drafting unless
strictly necessary.

==================================================
24. SECTION STRUCTURE
==================================================

Use:

    I. Introduction
    II. Related Work
    III. Operational Governance Formalisation
    IV. Evaluation Method
    V. Results
    VI. Discussion and Limitations
    VII. Conclusion

Do not inherit v3's architecture-heavy structure.

==================================================
25. DRAFTING TARGET — LOWER BOUND
==================================================

The narrative freeze established:

    SIX_PAGE_STORY = FEASIBLE_WITH_MANDATORY_COMPRESSION

Draft to approximately:

I. Introduction
    450 words

II. Related Work
    450 words

III. Operational Governance Formalisation
    750 words

IV. Evaluation Method
    550 words

V. Results
    900 words

VI. Discussion and Limitations
    600 words

VII. Conclusion
    180 words

Target prose:

    approximately 3,880 words

Do NOT draft to the midpoint.

Do NOT exceed section ceilings simply because source text is available.

==================================================
26. VISUAL BUDGET
==================================================

Maximum planning budget:

    3 visuals

Priority:

1. Related Work comparison table
2. empirical Results table
3. architecture/governance-flow figure

If space is tight:

    drop architecture figure first

Do not create images in this task unless an existing figure can be
reused directly without scientific reinterpretation.

A table is preferable to verbose prose.

==================================================
27. PROTECTED DISCLOSURE BUDGET
==================================================

Reserve approximately:

    350–550 words

for binding limitations/disclosures.

Must preserve the scientific content of:

- R-SAFE-001 deferred
- SAFE set empty
- Delay-only
- 454 records not types
- restrictive-side-only fidelity
- D = {m}
- lower-bound severity
- kappa = 0 lower bound
- g_w 2 activations / 0 bindings
- age_i unparameterised
- reasons unimplemented
- re-instantiation not demonstrated
- PRIMARY/RESOLUTION not uncertainty bounds
- C1<->C3 comparator-bounded
- TCAS precedent
- 72 vs targeted-post-review distinction
- E5/H3 open
- no target-hardware evidence
- no human study / human-outcome validation

Do not delete disclosures to meet word count.

==================================================
28. DISCUSSION DISCIPLINE
==================================================

Discussion should answer:

1. what C1 establishes;
2. what C2 establishes;
3. why C1<->C3 matters;
4. what the results do NOT establish;
5. relationship to TCAS and related governance paradigms;
6. generalisation boundary;
7. deployment/evaluation limitations.

Do not repeat Results numerically unless needed for interpretation.

Use the canonical novelty-positioning sentence verbatim.

==================================================
29. HYSTERESIS
==================================================

Default:

    OMIT

If space is unexpectedly available, it may appear as a secondary
result only with:

    hysteresis was evaluated as a precautionary stabilisation
    mechanism, not because mode chattering had been established

Do not include it in contributions, RQs or core Results.

==================================================
30. E5 / PERFORMANCE
==================================================

E5 does not support this conference paper.

Do not include MacBook timing as evidence of deployment feasibility.

Do not create a performance subsection.

Target hardware remains future work.

==================================================
31. INTRODUCTION MUST DO FIVE THINGS
==================================================

Within approximately 450 words:

1. establish the AI decision-support governance problem;
2. acknowledge avionics mechanism precedent;
3. state the scoped gap;
4. state the three RQs;
5. state exactly two contributions.

Do not spend large space describing fisheries.

The deployment domain is the evaluation context, not the paper's
primary novelty claim.

==================================================
32. RESULTS MUST BE THE LARGEST SECTION
==================================================

Results must receive the largest single prose allocation.

It must clearly answer:

    RQ2
    RQ3

and include the RQ2 control:

    C1<->C3 = 0.00%

Do not let Formalisation exceed Results in prose.

If this happens:

    DRAFT_STRUCTURE = FAIL

and revise before closure.

==================================================
33. ABSTRACT
==================================================

Draft a compact conference abstract.

It must contain:

- problem
- scoped contribution
- method
- headline empirical result
- bounded conclusion

Do not include mathematical symbols if the AMICT template prohibition
remains applicable.

Prefer plain text:

    multi-component environmental state
    participation gating
    advisory-scope restriction

instead of formula notation.

Do not claim novelty of the mechanism.

==================================================
34. KEYWORDS
==================================================

Use 4–6 compact keywords.

Possible concepts:

- AI governance
- decision support
- runtime governance
- advisory scope
- safety-critical systems
- formal methods

Do not over-specialise toward fisheries.

==================================================
35. REFERENCES
==================================================

Use numbered bracket references consistent with the existing
conference style.

Prefer validated bibliographic metadata.

Do not cite ResearchGate, blogs, or search-engine metadata.

Do not cite superseded FAA AC 20-151A as current authority.

Use:

    FAA AC 20-151C

Use:

    Cleaveland

not:

    Cleveland

==================================================
36. STALE V3 TEXT — MUST NOT SURVIVE
==================================================

Remove or rewrite any inherited statement that says or implies:

- "being developed as a prototype"
- prototype fidelity has not yet been verified
- reasoning engine is specified but not implemented
- no architecture restricts advisory scope as a function of state
- mechanism itself is new
- utility is an evaluated secondary metric
- domain-independent applicability
- human outcomes were validated

The old unscoped review contribution must not survive.

==================================================
37. CLAIM CATEGORY DISCIPLINE
==================================================

Maintain the freeze categories:

FORMAL
IMPLEMENTATION_FIDELITY
EMPIRICAL_TRACE
LITERATURE
INTERPRETATION
LIMITATION

Do not cross categories silently.

Example:

    formal Safety Dominance

must not become:

    empirical safety improvement.

==================================================
38. DRAFTING REPORT
==================================================

Create:

    drafting-report.md

It must report:

- output manuscript path
- section word counts
- total body word count
- abstract word count
- number of tables
- number of figures
- number of references
- RQ1 answer location
- RQ2 answer location
- RQ3 answer location
- C1 location
- C2 location
- all mandatory disclosures and where each appears
- exact reuse of canonical gap statement
- exact reuse count of canonical novelty-positioning sentence
- confirmation that AC 20-151A is absent
- confirmation that "Cleveland" misspelling is absent
- confirmation that prohibited novelty phrases are absent
- confirmation that 41.08% and 45.56% are absent unless provenance was
  separately repaired before this task
- confirmation manuscript-v3.md is untouched

==================================================
39. SELF-AUDIT BEFORE CLOSURE
==================================================

Search the draft for prohibited phrases/concepts.

At minimum check:

    first
    first-ever
    unprecedented
    unique
    no existing architecture
    no prior
    domain-independent
    safer
    safety improvement
    risk reduction
    effectiveness
    real-world validation
    454 advisory types
    5.81 ± 4.48
    robust
    preserved
    replicated
    AC 20-151A
    Cleveland

Contextually inspect every hit.

Do not mechanically delete legitimate phrases such as:

    first manuscript-facing use

if unrelated to scientific novelty, but the final manuscript should
avoid ambiguity.

==================================================
40. STOP CONDITIONS
==================================================

STOP and mark drafting BLOCKED if:

1. frozen C1 or C2 must be changed to make the paper coherent;
2. any RQ requires new evidence;
3. six-page lower-bound structure still cannot fit without deleting a
   protected disclosure;
4. empirical Results cannot remain the largest prose section;
5. a required citation lacks validated support;
6. the draft requires E5/H3;
7. the manuscript can only sound novel by omitting the avionics
   precedent;
8. a numerical conflict appears;
9. the draft requires the provenance-incomplete RESOLUTION pairwise
   values;
10. the targeted post-review literature cannot be distinguished from
    the original 72-paper review.

Do not repair scientific problems by inventing evidence.

==================================================
41. SUCCESS CRITERIA
==================================================

A successful draft has:

    MANUSCRIPT_V4_DRAFT = COMPLETE

    RQ_COUNT = 3

    HEADLINE_CONTRIBUTIONS = 2

    MECHANISM_NOVELTY = WITHDRAWN

    RESULTS_SECTION = LARGEST_PROSE_SECTION

    SIX_PAGE_STORY = LOWER_BOUND_TARGET

    PROTECTED_DISCLOSURES = PRESERVED

    PROVENANCE_OPEN_ITEMS = 1

unless separately repaired before this task.

==================================================
42. FINAL REPORT
==================================================

End with:

    MANUSCRIPT_V4_DRAFT = <status>
    TITLE = <title>
    BODY_WORD_COUNT = <count>
    ABSTRACT_WORD_COUNT = <count>
    RQ_COUNT = 3
    HEADLINE_CONTRIBUTIONS = 2
    RESULTS_SECTION_LARGEST = <yes/no>
    TABLE_COUNT = <count>
    FIGURE_COUNT = <count>
    REFERENCE_COUNT = <count>
    PROTECTED_DISCLOSURES = <pass/fail>
    PROVENANCE_OPEN_ITEMS = <count>
    MANUSCRIPT_V3_UNTOUCHED = <yes/no>

Then report:

- manuscript path
- drafting-report path
- section word counts
- exact RQ locations
- exact contribution locations
- any deviations from the frozen narrative
- any remaining blocker

Do not proceed to DOCX/PDF/template formatting.