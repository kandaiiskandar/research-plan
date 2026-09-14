TASK: AMICT RQ REDESIGN AND CONFERENCE NARRATIVE FREEZE

Context
-------
The AMICT conference rebuild has completed:

    NOVELTY_AUDIT = STOP_MATERIAL_EQUIVALENCE_FOUND
    SOURCE_CORPUS_VALIDATION = CLOSED
    CONTRIBUTION_FREEZE_V2 = CLOSED

The frozen contribution structure is:

    C1 = formal operational specification / scoped generalisation
    C2 = empirical characterisation

The underlying governance mechanism is NOT claimed as novel.

Implementation fidelity is supporting evidence for C1 only.

The old review-based headline contribution has been withdrawn.

No manuscript has been drafted.

==================================================
1. OBJECTIVE
==================================================

Freeze the research questions and the paper-level scientific narrative
before conference manuscript drafting.

The task must produce:

1. the final conference RQs;
2. an explicit mapping from RQ -> contribution -> evidence;
3. the paper's central narrative;
4. the role of each evidence block;
5. the exact novelty-positioning sentence;
6. section-level content priorities for a six-page conference paper.

Do NOT draft the manuscript yet.

==================================================
2. BINDING AUTHORITIES
==================================================

Read first:

    data/amict-conference-rebuild/contribution-freeze-v2.md
    data/amict-conference-rebuild/contribution-claim-matrix.csv
    data/amict-conference-rebuild/source-validation-report.md
    data/amict-conference-rebuild/novelty-audit-report.md
    data/amict-conference-rebuild/novelty-audit-addendum-001.md

Also use:

    publications/active/journal-1/evaluation-specification.md
    publications/active/journal-1/algorithm-specification.md
    docs/canonical/appendix-c-formalisation.md

Conference baseline:

    publications/active/ipsci-2026/submissions/v3-revision/manuscript-v3.md

Do not modify the baseline.

==================================================
3. FROZEN CONTRIBUTIONS
==================================================

C1 is frozen as:

    A formal operational specification of graduated advisory-scope
    governance that separates AI participation G(S) from admissible
    advisory scope A_AI(S), generalises the conditioning state beyond
    a single hazard variable to a classified multi-component
    environmental state S = f(E), and defines explicit
    observation-resolution, declared-exclusion, failure and
    containment semantics, including operational classifier
    F_D,tau = f o rho_D,tau and pre-reasoning rule-set supply.

C2 is frozen as:

    An empirical characterisation, using five years of retrospective
    environmental traces, of when advisory-scope graduation produces
    governance outcomes distinct from participation-only governance,
    reporting the intermediate-level contribution under PRIMARY and
    RESOLUTION configurations and a zero-divergence control against an
    intermediate-state comparator lacking advisory-scope
    differentiation.

Do NOT change the scientific meaning of either contribution.

==================================================
4. RQ DESIGN PRINCIPLES
==================================================

The RQs must map directly to the frozen contributions.

Do not create an RQ merely because an evidence block exists.

Do not create:

- an E5/performance RQ
- an implementation-fidelity RQ
- a hysteresis RQ
- a human-study RQ
- a safety-effectiveness RQ
- a novelty RQ

Target:

    RQ_COUNT = 3

The expected structure is:

    RQ1 -> C1 formal operational specification
    RQ2 -> C2 empirical divergence
    RQ3 -> C2 alternative environmental-data configuration

==================================================
5. RQ1 REDESIGN
==================================================

The previous candidate was:

    How can graduated advisory-scope governance be specified as a
    general runtime governance abstraction that separates AI
    participation from admissible recommendation scope while
    preserving explicit containment properties?

This requires rewording.

Problems:

1. "general" risks implying domain-independent applicability;
2. emphasis on containment makes the question look like a property-
   novelty claim;
3. the strongest part of C1 is the operational observation-resolution
   semantics.

RQ1 should instead foreground:

- operational specification;
- distinction between ideal classifier f(E) and deployed F_D,tau;
- missing/stale/invalid/unmeasured observations;
- participation vs admissible advisory scope;
- pre-reasoning admissibility.

Design a concise conference-appropriate RQ.

Do not make it so detailed that it reads like an algorithm
specification.

==================================================
6. RQ2
==================================================

The current direction is already aligned:

    How often does graduated advisory-scope governance produce
    governance outcomes that differ from participation-only governance
    in retrospective environmental replay?

Audit for clarity and concision.

Preserve:

    governance outcomes

Do NOT substitute:

    safety outcomes
    decision outcomes
    risk outcomes
    effectiveness

Expected evidence:

    DeltaL2 PRIMARY = 5.81%
    DeltaL2 RESOLUTION = 4.48%

and comparator context.

==================================================
7. RQ3 REDESIGN
==================================================

The old candidate:

    Are those governance differences preserved under the alternative
    environmental-data configuration?

is prohibited because "preserved" implies robustness, replication or
statistical stability.

PRIMARY and RESOLUTION are alternative environmental-data
configurations.

They are NOT:

- repeated trials
- confidence intervals
- uncertainty bounds
- independent datasets

Use a formulation such as:

    How does the measured governance-outcome divergence change under
    the alternative environmental-data configuration?

Audit whether:

    change
    differ
    vary

is the most scientifically accurate verb.

Do not use:

    robust
    stable
    preserved
    replicated

unless explicitly qualified and supported.

==================================================
8. C1 <-> C3 CONTROL
==================================================

The result:

    C1 <-> C3 = 0.00% PRIMARY
    C1 <-> C3 = 0.00% RESOLUTION

belongs inside C2 evidence.

Determine whether it primarily answers:

    RQ2

or:

    RQ3

or supports both.

Its frozen interpretation is:

    under the evaluated comparator definitions, adding an intermediate
    labelled governance state without advisory-scope differentiation
    produces no admissible-set divergence.

Do not generalise beyond the comparator definitions.

==================================================
9. IMPLEMENTATION FIDELITY
==================================================

Implementation fidelity is:

    SUPPORTING_EVIDENCE_FOR_C1

not an RQ.

The only allowed core statement is:

    The executable implementation produced zero violations of the
    configured advisory admissibility contract within the bounded
    deterministic interface-contract fidelity state space.

Required limitations:

    R-SAFE-001 = DEFERRED
    SAFE rule set empty
    four CAUTION rules
    Delay only
    454 advisory records != 454 advisory types
    restrictive side only

Determine where this evidence belongs in the paper narrative.

Likely:

    Method / Formalisation -> short executable-conformance subsection

not:

    headline Results RQ.

==================================================
10. PAPER NARRATIVE
==================================================

Freeze one concise scientific narrative.

The paper must NOT read as:

    We invented a new three-state governance architecture and tested it.

It should read approximately as:

    Prior work establishes state-conditioned advisory inhibition and
    graduated automation, but the reviewed AI-governance literature
    lacks an operational formalisation combining multi-component
    environmental classification, explicit observation-resolution
    semantics, and advisory-type admissibility.

    We formalise that governance contract and evaluate how often its
    intermediate advisory-scope level produces a governance outcome
    distinct from participation-only alternatives in five years of
    retrospective environmental traces.

Audit and improve this narrative.

It must explicitly acknowledge:

    certified avionics precedent

without making the Introduction revolve around TCAS.

==================================================
11. EVIDENCE HIERARCHY
==================================================

Freeze the paper's evidence priority.

Expected order:

PRIMARY:
    C2 empirical replay

SECONDARY:
    C1 formal operational specification

SUPPORTING:
    implementation fidelity

BACKGROUND:
    72-paper structured review
    targeted post-review novelty validation
    prior-work comparison

OPTIONAL / CUT FIRST:
    hysteresis

EXCLUDED:
    E5
    H3
    human study
    target-hardware performance

Determine whether this ordering is optimal for a conference paper
rejected previously for insufficient empirical evidence.

==================================================
12. SIX-PAGE STORY
==================================================

Assume the historical six-page conference budget for narrative
planning only.

Do NOT perform final formatting.

Design a section-level allocation such as:

I. Introduction
II. Related Work
III. Operational Governance Formalisation
IV. Evaluation Method
V. Results
VI. Discussion and Limitations
VII. Conclusion

For each section specify:

- purpose
- must-keep content
- content to compress
- content to omit
- evidence referenced
- approximate relative space priority

Do not write manuscript prose.

==================================================
13. RELATED WORK POSITIONING
==================================================

The Related Work narrative must distinguish:

A. original structured review:

    72 papers

B. targeted post-review sources from novelty validation.

Required precedent families:

- TCAS II / ACAS II
- ACAS X formal verification
- levels of automation
- adaptive automation
- selective prediction / deferral
- shielding / action masking
- graduated runtime governance

Do not turn Related Work into a second systematic review.

Its purpose is to establish:

    mechanism precedent exists

while showing the scoped remaining gap.

==================================================
14. FROZEN GAP STATEMENT
==================================================

Create one manuscript-facing gap statement.

It must be scoped.

Preferred shape:

    Within the reviewed AI decision-support and governance literature,
    we did not identify a formal operational treatment that combines
    a classified multi-component environmental state, explicit
    observation-resolution and exclusion semantics, and a
    state-conditioned advisory-type admissibility contract.

Audit every clause.

The statement must acknowledge separately that analogous advisory-type
restriction exists in certified avionics.

Do not write:

    no prior work
    no existing architecture
    first
    unprecedented

==================================================
15. FROZEN NOVELTY-POSITIONING SENTENCE
==================================================

Create exactly one canonical novelty-positioning sentence to be reused
later in:

- Introduction
- contribution paragraph
- Discussion

The sentence must position the work as:

    formalisation + scoped generalisation + empirical characterisation

of an existing mechanism pattern.

Do not claim mechanism invention.

==================================================
16. TITLE
==================================================

Frozen decision from contribution freeze:

    TITLE = RETAIN

Title:

    Evaluating Graduated Advisory-Scope Governance for AI Decision Support

Reconfirm only.

Do not propose new titles unless a contradiction appears.

==================================================
17. PROVENANCE ITEM
==================================================

Record:

    RESOLUTION_PAIRWISE_C0_C1_C0_C2 = PROVENANCE_INCOMPLETE

Do NOT use:

    41.08%
    45.56%

as headline manuscript evidence yet.

Do not recompute them.

Do not repair provenance in this task unless specifically required by
the narrative.

RQ2/RQ3 must remain fully supportable using:

    DeltaL2 5.81% / 4.48%
    C1<->C3 0.00% / 0.00%

==================================================
18. REQUIRED OUTPUTS
==================================================

Create:

    data/amict-conference-rebuild/rq-narrative-freeze.md

and:

    data/amict-conference-rebuild/rq-evidence-map.csv

The Markdown artefact must contain:

1. Executive verdict
2. Final RQ1
3. Final RQ2
4. Final RQ3
5. RQ design rationale
6. RQ -> contribution mapping
7. RQ -> evidence mapping
8. C1<->C3 control disposition
9. Implementation-fidelity narrative role
10. Frozen conference narrative
11. Evidence hierarchy
12. Six-page section strategy
13. Related Work positioning
14. Frozen gap statement
15. Frozen novelty-positioning sentence
16. Title confirmation
17. Excluded claims/evidence
18. Provenance-open item
19. Downstream manuscript rules
20. Changed files

CSV columns at minimum:

    rq_id
    rq_text
    contribution
    claim_type
    primary_evidence
    supporting_evidence
    excluded_evidence
    allowed_interpretation
    prohibited_interpretation
    status

==================================================
19. STOP CONDITIONS
==================================================

STOP if:

1. an RQ requires new experiments;
2. an RQ depends on E5/H3;
3. an RQ requires human-study evidence;
4. RQ1 can only be phrased by restoring mechanism novelty;
5. RQ2 or RQ3 requires interpreting divergence as safety/effectiveness;
6. the narrative cannot distinguish contribution from TCAS/ACAS X;
7. the narrative requires changing frozen C1 or C2;
8. a numerical contradiction appears;
9. the six-page story cannot accommodate both frozen contributions
   without dropping required limitations.

Do not resolve by changing scientific evidence.

==================================================
20. PROHIBITED ACTIONS
==================================================

Do NOT:

- draft manuscript prose
- modify manuscript-v3.md
- create manuscript.md
- create .docx/.pdf/.tex
- run new experiments
- recompute empirical results
- modify C1/C2
- create new contribution
- restore review as headline contribution
- repair E5
- perform Android benchmark
- implement R-SAFE-001
- change thresholds
- change architecture
- change comparator definitions
- alter the 72-paper sample

==================================================
21. SUCCESS STATUS
==================================================

If successful:

    RQ_NARRATIVE_FREEZE = CLOSED
    RQ_COUNT = 3
    RQ1 = FROZEN
    RQ2 = FROZEN
    RQ3 = FROZEN
    CONFERENCE_NARRATIVE = FROZEN
    GAP_STATEMENT = FROZEN
    NOVELTY_POSITIONING = FROZEN
    TITLE = RETAIN
    CONFERENCE_MANUSCRIPT = NOT_DRAFTED

If not:

    RQ_NARRATIVE_FREEZE = BLOCKED

==================================================
22. FINAL REPORT
==================================================

End with:

    RQ_NARRATIVE_FREEZE = <status>
    RQ_COUNT = <number>
    RQ1 = <status>
    RQ2 = <status>
    RQ3 = <status>
    CONFERENCE_NARRATIVE = <status>
    GAP_STATEMENT = <status>
    NOVELTY_POSITIONING = <status>
    TITLE = RETAIN
    PROVENANCE_OPEN_ITEMS = <count>
    CONFERENCE_MANUSCRIPT = NOT_DRAFTED

Then report:

- exact final RQs
- frozen gap statement
- canonical novelty-positioning sentence
- evidence hierarchy
- six-page story
- exact changed files
- remaining blockers

Do not proceed to manuscript drafting.