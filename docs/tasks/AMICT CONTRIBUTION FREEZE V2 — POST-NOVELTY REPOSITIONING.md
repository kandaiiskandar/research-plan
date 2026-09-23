TASK: AMICT CONTRIBUTION FREEZE V2 — POST-NOVELTY REPOSITIONING

Context
-------
The AMICT conference rebuild has completed two prerequisite gates:

    NOVELTY_AUDIT = STOP_MATERIAL_EQUIVALENCE_FOUND
    SOURCE_CORPUS_VALIDATION = CLOSED

The novelty audit established that the underlying mechanism pattern is
NOT new.

Certified TCAS II / ACAS II already implements:

    externally measured runtime state
    -> banded classification
    -> progressively restricted advisory-type set
    -> human operator

The current FAA authority, AC 20-151C, confirms the advisory-inhibition
schedule.

Formal verification of state-conditioned advisory logic also has
precedent in contemporary ACAS X research.

Therefore:

    MECHANISM_NOVELTY = WITHDRAWN

The conference paper must NOT claim invention of:

- runtime advisory-type restriction,
- graduated advisory scope itself,
- nested admissible sets,
- runtime state-conditioned admissibility,
- graduated governance,
- formal verification of advisory constraints,
- environmental triggering of governance change,
- or three-state governance.

The accepted repositioning direction is:

    FORMALISATION
    +
    GENERALISATION
    +
    EMPIRICAL CHARACTERISATION

This task must determine exactly which contribution claims survive and
freeze them before any manuscript drafting begins.

Do NOT draft the conference manuscript during this task.

==================================================
1. OBJECTIVE
==================================================

Produce a defensible Contribution Freeze V2 for the rebuilt AMICT
conference paper.

The freeze must answer:

1. What exactly is the paper contributing now that mechanism novelty
   has been withdrawn?

2. Which part is:
       formal contribution,
       implementation-support evidence,
       empirical contribution,
       literature positioning,
       limitation?

3. Is "generalisation" actually supported strongly enough to be a
   headline contribution?

4. Is "domain-independent" supportable, or should a weaker formulation
   such as "domain-agnostic specification", "general governance
   abstraction", or "domain-reinstantiable formulation" be used?

5. Which formal properties may legitimately be included in C1 without
   implying that those properties themselves are unprecedented?

6. What exactly does the five-year replay establish?

7. How should the existing implementation-fidelity evaluation support
   C1 without being represented as an independent scientific
   contribution?

8. How should the 72-paper review count be handled after the targeted
   post-review novelty sources were added?

The output of this task becomes binding authority for subsequent:

    RQ redesign
    conference outline
    manuscript drafting
    claim-evidence audit

==================================================
2. AUTHORITIES TO READ FIRST
==================================================

Before making any contribution decision, read and reconcile at minimum:

    data/amict-conference-rebuild/novelty-defence-matrix.md
    data/amict-conference-rebuild/novelty-audit-report.md
    data/amict-conference-rebuild/novelty-audit-addendum-001.md
    data/amict-conference-rebuild/source-validation-report.md

Also read the relevant existing authorities:

    publications/active/journal-1/evaluation-specification.md
    publications/active/journal-1/algorithm-specification.md

and the current conference baseline:

    publications/active/ipsci-2026/submissions/v3-revision/manuscript-v3.md

Use v3 as the conference baseline.

Do NOT rebuild from v2.5.

Read the validated [[notes]] entries for the load-bearing novelty
comparators, especially:

- FAA AC 20-151C
- Cleaveland, Mitsch & Platzer (2023)
- Parasuraman, Sheridan & Wickens (2000)
- Bernabei & Costantino (2024)
- Kwon & Kim (2026)
- FDA CDS guidance (2026)

Also inspect relevant existing corpus notes for:

- Baxi (2026)
- Flehmig et al. (2024)
- Kang (2026)
- shielding / action masking
- selective prediction / learning to defer

Do not rely only on the novelty report's summaries when freezing
contribution wording.

==================================================
3. FROZEN NOVELTY POSITION
==================================================

The following is binding:

    MECHANISM_NOVELTY = WITHDRAWN

Do not attempt to rescue novelty by terminology.

"Graduated advisory-scope governance" remains permitted as a
DESCRIPTIVE TERM.

It must not be treated as evidence that the mechanism is new.

The first manuscript-facing use will eventually need to acknowledge
the avionics precedent.

Do NOT claim:

- first
- first-ever
- unprecedented
- globally novel
- uniquely novel
- no existing architecture
- no prior system restricts advisory scope
- first formal advisory-admissibility mechanism
- first graduated governance architecture
- first use of environmental state for governance
- first nested advisory set

==================================================
4. CONTRIBUTION MODEL TO TEST
==================================================

Do NOT automatically accept this wording.

Treat it as the candidate to audit.

Candidate C1:

    Formalisation and generalisation of graduated advisory-scope
    governance as a runtime governance abstraction separating AI
    participation from state-conditioned admissible recommendation
    scope, with explicit totality, monotonicity, safety-dominance and
    containment properties.

Candidate C2:

    Empirical characterisation of the contribution of graduated
    advisory-scope governance relative to participation-only
    governance using five-year retrospective environmental replay
    under two environmental-data configurations.

Supporting implementation evidence:

    Executable conformance evaluation showing that the implementation
    respects the configured advisory-admissibility contract within the
    bounded deterministic interface-contract fidelity state space.

The task must determine whether each phrase survives evidence review.

==================================================
5. C1 — FORMALISATION AUDIT
==================================================

Evaluate C1 phrase by phrase.

Specifically test:

    "formalisation"
    "generalisation"
    "domain-independent"
    "domain-agnostic"
    "domain-reinstantiable"
    "general governance abstraction"
    "separates participation from advisory scope"
    "multi-component environmental state"
    "totality"
    "monotonicity"
    "Safety Dominance"
    "containment"

For every phrase classify:

    PASS
    PASS_WITH_SCOPE
    WEAK
    FAIL

For every PASS_WITH_SCOPE, provide the exact required qualifier.

Important:

The fact that this project proves a property does NOT mean the property
or proof pattern is novel.

ACAS X, Baxi, Kang, shielding and other prior work constrain what can
be claimed.

Separate:

    PROPERTY_EXISTS_IN_OUR_FORMALISM

from:

    PROPERTY_IS_NOVEL

These are not equivalent.

==================================================
6. GENERALISATION AUDIT — HIGH PRIORITY
==================================================

"Generalisation" is now potentially load-bearing.

Do not allow it without explicit support.

Determine what exactly has been generalised.

Possible dimensions include:

A. from a single scalar operational variable to:

       E = (w, r, m, o, v, t)

B. from a device-specific inhibition table to:

       S = f(E)

       (G(S), A_AI(S))

C. from a particular advisory generator to an admissibility contract
   defined independently of the Layer 3 generator.

D. explicit missing/stale/invalid semantics through:

       rho_D,tau

E. explicit severity ordering and monotone admissible sets.

F. re-instantiation through domain-specific component classifiers.

For each dimension determine:

    GENERALISATION_SUPPORTED = YES / PARTIAL / NO

Then answer the key question:

Does the evidence support:

    "domain-independent"

or only something narrower such as:

    "domain-reinstantiable"
    "domain-agnostic at the governance-contract level"
    "generalised beyond a single hazard variable"
    "a reusable governance abstraction"

Do not choose stronger language for rhetorical value.

If cross-domain implementation or evaluation is absent, explicitly
consider whether "domain-independent" overstates the evidence.

==================================================
7. HUMAN AUTHORITY — NON-LOAD-BEARING
==================================================

The architecture structurally preserves unconditional human final
authority.

This remains a valid architectural property.

However, the novelty audit concluded that this distinction is real but
thin relative to TCAS.

Therefore:

    HUMAN_AUTHORITY_INVARIANCE = PROPERTY
    HUMAN_AUTHORITY_INVARIANCE = NOT_LOAD_BEARING_NOVELTY

Do not make unconditional human authority a headline novelty claim.

Determine whether it belongs in:

- C1 wording,
- architecture description only,
- discussion,
- or comparison table.

==================================================
8. IMPLEMENTATION FIDELITY DISPOSITION
==================================================

The following is binding:

    R-SAFE-001 = DEFERRED

    SAFE episodes = 32
    CAUTION episodes = 260

    advisory records = 454
    episodes with advisory = 244
    CAUTION empty-advisory episodes = 16

    generated advisory conclusion type = Delay only

    F1 violations = 0
    F2 violations = 0
    F3 mismatches = 0

    UNSAFE gate-off cases = 162
    separate from the 292 primary fidelity episodes

Do NOT call the 454 records:

    454 advisory types

They are:

    454 advisory records

of one generated conclusion type:

    Delay

The following decision is presumed but must be formally recorded:

    IMPLEMENTATION_FIDELITY =
        SUPPORTING_IMPLEMENTATION_EVIDENCE

not:

    HEADLINE_CONTRIBUTION

Allowed interpretation:

    the executable implementation produced zero violations of the
    configured advisory-admissibility contract within the bounded
    deterministic interface-contract fidelity state space.

Prohibited interpretations:

- complete SAFE advisory-space validation
- all recommendation types exercised
- strong empirical validation of containment
- real-world validation
- effectiveness evidence
- safety improvement evidence

Determine exactly where this evidence belongs under C1.

==================================================
9. C2 — EMPIRICAL CONTRIBUTION AUDIT
==================================================

Audit whether the five-year retrospective replay is strong enough to
be the second headline contribution.

Relevant closed evidence includes:

PRIMARY:

    43,848 hourly records

    C0 <-> C1 = 42.88%
    C0 <-> C2 = 48.69%
    C1 <-> C2 = 5.81%
    C1 <-> C3 = 0.00%

RESOLUTION:

    C0 <-> C1 = 41.08%
    C0 <-> C2 = 45.56%
    C1 <-> C2 = 4.48%
    C1 <-> C3 = 0.00%

E2 / Level-2 contribution:

    PRIMARY = 5.81%
    RESOLUTION = 4.48%

Temporal characterisation:

    transitions = 3,661
    scheduled = 3,439
    non-scheduled = 222
    genuine oscillations = 26

    hysteresis reduction of non-scheduled transitions = 10.36%

E4 is PRIMARY-only under the current E3 design.

Do NOT create a RESOLUTION E4 comparison.

Do NOT interpret:

    5.81%

as:

- 5.81% safer
- 5.81% safety improvement
- 5.81% risk reduction
- 5.81% better decisions
- 5.81% improvement in effectiveness

Determine the strongest exact empirical contribution statement.

The contribution should describe:

    governance-outcome divergence

or equivalent,

not human or physical safety outcomes.

==================================================
10. C1 <-> C3 = 0.00% INTERPRETATION
==================================================

Explicitly decide how this result should be used.

The allowed interpretation is bounded:

    merely introducing an intermediate / traffic-light state does not
    necessarily produce a distinct admissible advisory-scope outcome.

The result demonstrates that, under the evaluated comparator
definitions, C1 and C3 are identical at the admissible-set level.

Do NOT generalise:

    all traffic-light systems are equivalent
    all three-state systems add no value
    advisory-scope governance is universally superior

Decide whether this result belongs:

- inside C2,
- as a supporting comparator result,
- or in Discussion.

==================================================
11. HYSTERESIS DISPOSITION
==================================================

Hysteresis remains secondary.

The 10.36% figure may be reported only with the established
qualification:

    hysteresis was evaluated as a precautionary stabilisation
    mechanism

not because a mode-chattering requirement had been established.

The previous mode-chattering claim was withdrawn.

Determine whether hysteresis should be:

    SECONDARY_EMPIRICAL_RESULT

or omitted from the six-page conference contribution story.

Do not make it a headline contribution.

==================================================
12. E5 / H3 / HUMAN OUTCOME BOUNDARY
==================================================

Binding status:

    E5 = OPEN
    E5_HARNESS = CLOSED
    MACBOOK_REFERENCE = COMPLETE_REFERENCE_ONLY
    E5_ANDROID_TARGET_BENCHMARK = DEFERRED_MANDATORY
    H3 = OPEN_UNSUPPORTED

Therefore E5 cannot support a conference contribution.

Do NOT create an RQ around performance.

Do NOT claim:

- smartphone feasibility demonstrated
- low-resource deployment validated
- real-time performance validated
- target-hardware performance established

Also:

    HUMAN_STUDY = NOT_REQUIRED / DEFERRED

There is no empirical evidence for:

- trust
- calibrated reliance
- human decision quality
- behavioural benefit
- accident reduction
- livelihood benefit
- real-world operational safety improvement

Keep these outside the contribution freeze.

==================================================
13. CORPUS COUNT RECONCILIATION
==================================================

This issue was intentionally deferred from source validation.

The existing conference review reports:

    72 manuscript-facing papers

The repository also contains broader corpus/note counts.

Six validated novelty-defence sources have now been added to notes,
including targeted post-review sources.

Do NOT mechanically change:

    72 -> 78

Determine the correct methodological treatment.

Explicitly distinguish:

A. papers included in the original structured/systematic review sample,

from:

B. targeted post-review literature added during reviewer-driven
   novelty validation / conference rebuild.

Answer:

1. Should the paper continue to say the structured review included
   72 papers?

2. Should the six targeted sources be described separately as
   post-review targeted literature?

3. Does adding these sources require reopening/re-running the original
   review methodology?

4. Would combining them into the 72-paper count without rerunning the
   search/screening protocol compromise methodological consistency?

Preferred principle:

    preserve the frozen review sample unless methodology requires
    reopening it.

Do not modify review counts during this task.

Produce a binding reporting rule for subsequent drafting.

==================================================
14. RQ DIRECTION CHECK — DO NOT FULLY REDESIGN
==================================================

Do not perform the complete RQ-redesign task yet.

Only determine whether the contribution freeze supports the following
direction:

Candidate RQ1:

    How can graduated advisory-scope governance be specified as a
    general runtime governance abstraction that separates AI
    participation from admissible recommendation scope while
    preserving explicit containment properties?

Candidate RQ2:

    How often does graduated advisory-scope governance produce
    governance outcomes that differ from participation-only governance
    in retrospective environmental replay?

Candidate RQ3:

    Are those governance differences preserved under the alternative
    environmental-data configuration?

Evaluate each:

    ALIGNED
    NEEDS_REWORDING
    REJECT

Provide reasoning.

Do NOT insert RQs into the manuscript.

==================================================
15. TITLE CHECK
==================================================

Current title:

    Evaluating Graduated Advisory-Scope Governance
    for AI Decision Support

The novelty audit marked it provisional-confirmed.

Re-evaluate it against the frozen contributions.

Determine:

    TITLE = RETAIN
    TITLE = MODIFY

Do not change the title merely to create apparent novelty.

No subtitle.

==================================================
16. CLAIM-TYPE DISCIPLINE
==================================================

Every candidate contribution clause must be tagged as one of:

    FORMAL
    IMPLEMENTATION_FIDELITY
    EMPIRICAL_TRACE
    LITERATURE
    INTERPRETATION
    LIMITATION

No clause may silently cross categories.

Example:

    "The architecture guarantees Safety Dominance"

may be FORMAL.

It must not silently become:

    "The architecture improves operational safety"

which would be an unsupported EMPIRICAL/HUMAN outcome claim.

==================================================
17. REQUIRED ARTEFACTS
==================================================

Create:

    data/amict-conference-rebuild/contribution-freeze-v2.md

and:

    data/amict-conference-rebuild/contribution-claim-matrix.csv

The Markdown artefact must contain:

1. Executive verdict

2. Frozen novelty boundary

3. C1 phrase-by-phrase audit

4. Generalisation audit

5. Final frozen C1 wording

6. Implementation-fidelity disposition

7. C2 empirical audit

8. Final frozen C2 wording

9. C1 <-> C3 interpretation rule

10. Hysteresis disposition

11. Human-authority disposition

12. E5/H3/human-outcome exclusion boundary

13. Corpus-count reconciliation

14. RQ-direction assessment

15. Title decision

16. Prohibited contribution wording

17. Claim-type classification

18. Downstream drafting rules

19. OPEN items

20. Changed files

The CSV must include at minimum:

    contribution_id
    clause_id
    candidate_clause
    final_clause
    claim_type
    evidence_source
    novelty_status
    support_status
    required_qualifier
    prohibited_interpretation
    disposition

==================================================
18. CONTRIBUTION COUNT
==================================================

Target:

    HEADLINE_CONTRIBUTIONS = 2

Do not create a third contribution merely to preserve the previous
paper structure.

Expected architecture:

    C1 = FORMALISATION / GENERALISATION

with implementation fidelity as supporting evidence.

    C2 = EMPIRICAL CHARACTERISATION

If the evidence does not support this two-contribution structure:

    CONTRIBUTION_STRUCTURE = BLOCKED

and report why.

==================================================
19. STOP CONDITIONS
==================================================

STOP if:

1. "generalisation" cannot be supported without a new experiment.

2. C1 materially duplicates the validated prior work after removing
   mechanism novelty.

3. C2 cannot be stated as a meaningful contribution without implying
   improved safety/effectiveness.

4. contribution wording requires E5.

5. contribution wording requires H3.

6. contribution wording requires human-study evidence.

7. the corpus-count issue requires reopening the structured review
   before a defensible contribution can be frozen.

8. a numerical conflict appears between frozen authorities.

9. contribution wording requires modifying the architecture,
   thresholds, comparator definitions, or empirical evidence.

Do not resolve these by adding new research.

==================================================
20. PROHIBITED ACTIONS
==================================================

Do NOT:

- draft the conference manuscript
- modify manuscript-v3.md
- create a new submission manuscript
- create .docx
- create .pdf
- create .tex
- run new experiments
- recompute frozen empirical results
- change thresholds
- change architecture
- add comparators
- extend replay
- perform Android benchmarking
- create SAFE rules
- implement R-SAFE-001
- invent recommendation types
- conduct a new systematic review
- modify the 72-paper count
- reopen CLOSED Journal 1 workstreams
- restore mechanism novelty through wording

==================================================
21. SUCCESS CRITERIA
==================================================

The task passes only if:

    MECHANISM_NOVELTY = WITHDRAWN

remains explicit,

and exactly two defensible headline contributions are frozen.

Expected structure:

    C1 = formalisation/generalisation
    C2 = empirical characterisation

with:

    IMPLEMENTATION_FIDELITY = SUPPORTING_EVIDENCE

The contribution wording must survive the validated precedents:

    TCAS II / ACAS II
    ACAS X
    Parasuraman et al.
    Bernabei & Costantino
    selective prediction / deferral
    graduated runtime governance
    shielding / action masking
    Kang (2026)

without relying on terminology differences.

==================================================
22. COMPLETION STATUS
==================================================

If successful:

    CONTRIBUTION_FREEZE_V2 = CLOSED
    HEADLINE_CONTRIBUTIONS = 2
    MECHANISM_NOVELTY = WITHDRAWN
    IMPLEMENTATION_FIDELITY = SUPPORTING_EVIDENCE
    CORPUS_COUNT_RECONCILIATION = CLOSED

If a contribution cannot be defended:

    CONTRIBUTION_FREEZE_V2 = BLOCKED

Do not proceed to manuscript drafting.

==================================================
23. FINAL CLOSURE REPORT
==================================================

End with:

    CONTRIBUTION_FREEZE_V2 = <status>
    MECHANISM_NOVELTY = WITHDRAWN
    HEADLINE_CONTRIBUTIONS = <number or BLOCKED>
    C1 = <status>
    C2 = <status>
    IMPLEMENTATION_FIDELITY = SUPPORTING_EVIDENCE
    CORPUS_COUNT_RECONCILIATION = <status>
    RQ_REDESIGN = NOT_STARTED
    CONFERENCE_MANUSCRIPT = NOT_DRAFTED

Then report:

- final C1 wording
- final C2 wording
- strongest allowed novelty-positioning sentence
- implementation-fidelity role
- corpus-count reporting rule
- RQ-direction verdict
- title verdict
- PASS / FAIL / OPEN counts
- exact changed files
- any remaining blocker

Do not proceed beyond Contribution Freeze V2.