TASK: AMICT NOVELTY CORPUS VALIDATION AND SOURCE INTEGRATION

Context
-------
The targeted novelty audit for the AMICT conference rebuild has completed with:

    NOVELTY_AUDIT = STOP_MATERIAL_EQUIVALENCE_FOUND

The audit identified TCAS II / ACAS II low-altitude advisory inhibition as a materially equivalent precedent for the mechanism pattern:

    externally measured state
    -> banded classification
    -> nested admissible advisory-type set
    -> human operator

The conference contribution is therefore being repositioned from:

    invention of a new advisory-scope restriction mechanism

to:

    formalisation, generalisation, and empirical characterisation
    of graduated advisory-scope governance.

The manuscript MUST NOT be drafted yet.

This task exists only to validate the six external sources identified by the novelty audit, replace weak or outdated sources where appropriate, integrate accepted sources into the repository's EXISTING notes system, and establish a defensible contemporary literature basis for the subsequent contribution freeze.

--------------------------------------------------
1. OBJECTIVE
--------------------------------------------------

Validate and curate the six source areas identified by the novelty audit:

1. TCAS II / ACAS II advisory inhibition
2. ACAS X formal verification
3. Levels of automation / presented-option restriction
4. Adaptive automation / adjustable autonomy
5. Selective prediction / abstention / deferral
6. FDA Clinical Decision Support guidance

The goal is NOT to preserve the exact six references originally found.

The goal is to obtain the strongest valid source set supporting the novelty comparison.

Where a candidate is old, superseded, preprint-only, or otherwise weak, locate a stronger source where possible.

--------------------------------------------------
2. DATE REQUIREMENT
--------------------------------------------------

For manuscript-facing research literature:

    PREFERRED_PUBLICATION_YEAR >= 2023

Prioritise research published from 2023 onward.

A pre-2023 source may be retained only when it is necessary as:

A. the original/foundational source of a concept, or

B. primary historical evidence of an operational/certified mechanism that cannot be represented accurately using only newer literature.

Every accepted pre-2023 source must be explicitly classified:

    FOUNDATIONAL_HISTORICAL

and its necessity must be justified.

Do NOT use old literature merely because it is famous or convenient.

The final conference Related Work should be dominated by contemporary 2023+ literature, with older sources used only where historically necessary.

--------------------------------------------------
3. SOURCE-QUALITY REQUIREMENT
--------------------------------------------------

A manuscript-facing source must preferably be one of:

A. peer-reviewed journal article,
B. peer-reviewed conference proceeding from an established venue,
C. official government or regulatory publication,
D. official standards / certification / aviation authority material,
E. authorised technical research report from a recognised research institution.

Preferred hierarchy:

    peer-reviewed publisher record
    >
    official government/regulatory record
    >
    recognised institutional technical report
    >
    preprint

Do NOT use as bibliographic authority:

- blogs,
- commercial summaries,
- Wikipedia,
- ResearchGate metadata,
- Academia.edu metadata,
- generic web summaries,
- secondary news articles,
- AI-generated summaries.

ResearchGate or similar repositories may be used only to obtain a readable copy if necessary.

Bibliographic metadata must be verified against:
- publisher record,
- DOI record,
- official government website,
- official institutional repository,
or equivalent authoritative source.

--------------------------------------------------
4. PREPRINT POLICY
--------------------------------------------------

Do NOT use an unreviewed preprint as load-bearing novelty evidence when a peer-reviewed or official alternative exists.

If a candidate exists only as a preprint:

1. search for a subsequently published peer-reviewed version;
2. verify whether title/authors/venue changed;
3. use the published version if found.

If no peer-reviewed replacement exists and the source is still scientifically useful:

    SOURCE_STATUS = PREPRINT_SUPPLEMENTARY

It must NOT become the sole evidence supporting a central novelty distinction.

If no acceptable source exists for an important claim:

    CORPUS_GAP = OPEN

Do not silently lower the source-quality threshold.

--------------------------------------------------
5. SIX REQUIRED SOURCE VALIDATIONS
--------------------------------------------------

### SOURCE AREA 1 — TCAS II / ACAS II ADVISORY INHIBITION

The novelty audit used FAA AC 20-151A as evidence that advisory types are progressively inhibited according to radio-altitude bands.

Validate:

- publication status,
- publication year,
- whether it has been cancelled/superseded,
- current FAA or equivalent official authority chain,
- whether a newer official source preserves the relevant advisory-inhibition mechanism,
- exact altitude/inhibition rules relevant to the novelty comparison.

Prefer a current official source if it supports the required mechanism.

If an older FAA document remains necessary as direct historical evidence:

    SOURCE_CLASS = FOUNDATIONAL_HISTORICAL

Record clearly that it is historical/superseded if applicable.

Do NOT present an obsolete advisory circular as current regulatory guidance.

The required claim is only:

    advisory-type inhibition conditioned on externally measured runtime state
    has operational precedent in certified collision-avoidance avionics.

Do not infer anything beyond what the official source establishes.


### SOURCE AREA 2 — ACAS X FORMAL VERIFICATION

Validate contemporary peer-reviewed research supporting formal verification of ACAS X / next-generation airborne collision avoidance.

Specifically investigate the 2023 work by:

    Cleveland, Mitsch, and Platzer

concerning formally verified next-generation airborne collision avoidance / ACAS X.

Verify:

- exact title,
- authors,
- year,
- journal/conference,
- volume/issue/pages if applicable,
- DOI,
- publisher,
- peer-review status,
- exact formal property/properties established.

If the 2023 peer-reviewed source supports the required comparison, prefer it over older ACAS X verification work.

Older ACAS X papers may be retained only as:

    FOUNDATIONAL_HISTORICAL

if necessary for provenance.

Do NOT claim that ACAS X proves the same general governance theorem as this project unless the paper actually does.

The intended comparison is narrower:

    formal verification of state-conditioned advisory logic has precedent.


### SOURCE AREA 3 — LEVELS OF AUTOMATION

The novelty audit identified:

    Parasuraman, Sheridan & Wickens (2000)

as a foundational precedent for graduated restriction of options presented to a human.

Because it predates 2023:

1. verify the original publication and DOI;
2. classify it as FOUNDATIONAL_HISTORICAL if retained;
3. search for a 2023+ peer-reviewed review/synthesis that discusses contemporary levels-of-automation or human-autonomy interaction and can provide modern context.

Do NOT replace the foundational source merely with a later paper that cites it if the historical claim specifically belongs to the original.

Use contemporary literature for the current research landscape and the original source only for the historical concept.

Required distinction:

    design-time narrowing of options presented to humans
    !=
    runtime environmental-state-conditioned advisory-scope governance.


### SOURCE AREA 4 — ADAPTIVE AUTOMATION / ADJUSTABLE AUTONOMY

Locate a strong peer-reviewed 2023+ source.

Investigate, but do not automatically accept:

    Bernabei & Costantino (2024)
    Robotics and Computer-Integrated Manufacturing

Verify exact metadata and whether the article genuinely supports the comparison required here.

The source must help establish what adaptive automation actually governs, such as:

- level of automation,
- task allocation,
- operator workload/state,
- mission context,
- human-machine authority/allocation.

Do not cite it for advisory-scope restriction unless it actually implements that mechanism.

Authorised aviation/human-factors technical reports from 2023+ may be retained as supplementary evidence where useful.

Preferred:

    PEER_REVIEWED_2023_PLUS

rather than technical-report-only evidence.


### SOURCE AREA 5 — SELECTIVE PREDICTION / DEFERRAL

The novelty audit identified:

    "On the Limits of Selective AI Prediction:
     A Case Study in Clinical Decision Making"

as a close comparison.

If it remains only an arXiv preprint, do NOT make it load-bearing.

Search for a peer-reviewed 2023+ journal or established conference source covering:

- selective prediction,
- learning to defer,
- abstention,
- selective withholding,
- human-AI decision support,

preferably one that clarifies whether the governed quantity is:

    prediction participation / instance-level output

rather than:

    recommendation-type scope conditioned on external environment.

Verify the exact mechanism.

Do not select a paper simply because it contains the terms:
"selective prediction",
"abstention",
or
"deferral".

Mechanistic relevance is required.

If no suitable peer-reviewed 2023+ replacement exists:

    SELECTIVE_PREDICTION_CORPUS_GAP = OPEN

The preprint may remain supplementary but must not become load-bearing.


### SOURCE AREA 6 — FDA CLINICAL DECISION SUPPORT

Use the latest official FDA Clinical Decision Support Software guidance available from the FDA.

Verify:

- current revision/year,
- document status,
- exact relevant criterion,
- distinction between lists/options and specific directives/recommendations,
- human professional review/independent-basis requirement.

Use the FDA's official publication as authority.

Classification:

    AUTHORISED_REGULATORY_SOURCE

This source is NOT evidence of a runtime advisory-scope mechanism unless the guidance explicitly establishes one.

Its intended role is narrower:

    recommendation/output type is already treated as a meaningful governance/regulatory variable.

Do not overinterpret it.

--------------------------------------------------
6. MECHANISM-FIRST VALIDATION
--------------------------------------------------

For every accepted source, evaluate the actual mechanism.

Do NOT infer relevance from terminology.

Record:

- What is governed?
- What causes the restriction/change?
- Runtime or design-time?
- External state or AI-internal state?
- Does AI participation change?
- Does advisory content change?
- Does recommendation TYPE scope change?
- Does executable action space change?
- Does human/AI authority change?
- Does human final authority remain invariant?
- Is there formal verification?
- Is there empirical evaluation?

The novelty comparison must remain mechanistic.

--------------------------------------------------
7. REQUIRED SOURCE CLASSIFICATION
--------------------------------------------------

Every source must receive exactly one primary status:

    ACCEPT_CONTEMPORARY
    ACCEPT_AUTHORISED
    FOUNDATIONAL_HISTORICAL
    SUPPLEMENTARY
    REPLACE
    REJECT

Also record:

    SOURCE_VALIDITY = PASS / FAIL

A manuscript-facing source may be accepted only if:

    SOURCE_VALIDITY = PASS

and either:

    YEAR >= 2023

or:

    FOUNDATIONAL_HISTORICAL = JUSTIFIED

or:

    AUTHORISED_SOURCE = TRUE

For historical sources, explicitly record why a modern replacement is insufficient for the specific historical claim.

--------------------------------------------------
8. EXISTING NOTES SYSTEM — MANDATORY
--------------------------------------------------

All accepted literature MUST be integrated into the repository's EXISTING notes system.

Use:

    notes/

Do NOT create:

- a second notes directory,
- a new literature database,
- a separate reference-management system,
- a conference-specific notes folder unless the existing repository convention explicitly requires it.

Follow the existing note:
- filename convention,
- structure,
- metadata convention,
- citation convention,
- extraction style.

Before creating a note, check whether that source already exists in:

    notes/

Do not create duplicate notes.

If an existing note is present:
- verify it,
- update it only if required,
- preserve valid existing content,
- clearly distinguish newly verified metadata from previous extraction.

Register all accepted notes in:

    docs/canonical/citation-notes-map.md

using the repository's existing mapping convention.

All manuscript-facing citations must ultimately resolve through the existing `[[notes]]` system.

--------------------------------------------------
9. REQUIRED CONTENT FOR EACH NEW/UPDATED NOTE
--------------------------------------------------

Each accepted source note must contain, following the existing repository format:

- Full title
- Authors
- Publication year
- Venue
- Publisher
- Volume / issue / pages where applicable
- DOI where applicable
- Official URL / publisher record where applicable
- Source type
- Peer-review status or authority status
- Contemporary / historical classification
- Exact mechanism relevant to this project
- Exact claim(s) the source supports
- Exact claim(s) the source does NOT support
- Relevance to novelty defence
- Relationship to graduated advisory-scope governance
- Any important limitation/caveat

Use the repository's established note format rather than inventing a new schema if the two differ.

--------------------------------------------------
10. NOVELTY-AUDIT UPDATE RULE
--------------------------------------------------

Do NOT rewrite the completed novelty audit simply because a newer source is found.

The existing:

    data/amict-conference-rebuild/novelty-defence-matrix.md
    data/amict-conference-rebuild/novelty-audit-report.md

are audit records.

If source validation materially changes a finding, create a clearly documented addendum rather than silently rewriting history.

If no material finding changes, leave the audit artefacts untouched.

--------------------------------------------------
11. CURRENT SCIENTIFIC POSITION — DO NOT REOPEN
--------------------------------------------------

The following decision has been accepted:

    REPOSITIONING_DECISION = ACCEPTED
    MECHANISM_NOVELTY = WITHDRAWN

The paper will NOT claim invention of runtime advisory-type restriction.

Current contribution basis:

    FORMALISATION
    +
    GENERALISATION
    +
    EMPIRICAL_CHARACTERISATION

Implementation fidelity:

    SUPPORTING_EVIDENCE

not a standalone contribution.

Do not attempt to rescue mechanism novelty through terminology.

Do not claim:

- first,
- first-ever,
- unprecedented,
- globally novel,
- uniquely novel,
- no existing architecture,
- no prior system restricts advisory scope.

--------------------------------------------------
12. CURRENT CONTRIBUTION DIRECTION
--------------------------------------------------

Do NOT formally freeze contributions in this task.

However, validate whether the source corpus remains consistent with the intended direction:

C1 candidate:

    A domain-independent formalisation and generalisation of
    graduated advisory-scope governance, separating AI
    participation from state-conditioned admissible recommendation
    scope and establishing formal governance properties.

C2 candidate:

    Empirical characterisation of graduated advisory-scope
    governance against participation-only governance using
    retrospective environmental traces.

Implementation fidelity remains supporting evidence for C1.

If source validation contradicts either contribution direction:

    CONTRIBUTION_DIRECTION_CONTRADICTION = TRUE

STOP and report the contradiction.

Do not silently rewrite the contribution.

--------------------------------------------------
13. RQ DIRECTION — DO NOT FREEZE YET
--------------------------------------------------

Current candidate RQs are:

RQ1:
How can graduated advisory-scope governance be specified so that AI participation and admissible recommendation scope remain distinct while advisory containment is enforced across governance states?

RQ2:
How often does graduated advisory-scope governance produce governance outcomes that differ from participation-only governance in retrospective environmental replay?

RQ3:
Are the observed governance differences preserved under the alternative environmental-data configuration?

Do not finalise or insert these into a manuscript during this task.

Only report whether the validated literature creates a contradiction with this RQ direction.

--------------------------------------------------
14. REQUIRED OUTPUT
--------------------------------------------------

Create:

    data/amict-conference-rebuild/source-validation-report.md

The report must contain:

1. Executive verdict

2. Validation table for all six source areas

3. For each candidate:
   - original source
   - validation result
   - accepted/replacement source
   - year
   - source type
   - peer-review/authority status
   - DOI/official identifier
   - status
   - rationale

4. Contemporary literature coverage:
   - number of accepted 2023+ research sources
   - number of authorised official sources
   - number of foundational historical sources
   - number of supplementary/preprint sources
   - unresolved corpus gaps

5. Exact notes created

6. Existing notes updated

7. citation-notes-map entries added/updated

8. Rejected/replaced sources and reason

9. Whether the TCAS material-equivalence finding survives validation

10. Whether the ACAS X formal-verification precedent survives validation

11. Whether the repositioned contribution direction remains defensible

12. Any OPEN corpus gap

13. Changed files

14. Verification summary

--------------------------------------------------
15. OUTPUT FORMAT
--------------------------------------------------

Use Markdown for narrative artefacts.

Permitted:
    .md
    .csv
    .json

Do NOT create:
    .docx
    .pdf
    .tex

Do NOT draft:

    manuscript.md

yet.

Do NOT begin conference-template formatting.

--------------------------------------------------
16. VERIFICATION
--------------------------------------------------

Before closure, verify:

A. Every accepted citation resolves to an existing note.

B. No duplicate source note was created.

C. Every new manuscript-facing research source is:
       2023+
   OR explicitly justified as FOUNDATIONAL_HISTORICAL.

D. Every official source is verified against its issuing authority.

E. Every DOI is verified.

F. Every claimed peer-reviewed publication is actually peer reviewed.

G. No ResearchGate / blog / generic website is used as bibliographic authority.

H. No preprint is load-bearing where a peer-reviewed alternative exists.

I. The TCAS precedent has not been weakened or hidden merely to restore novelty.

J. The distinction between:
       mechanism precedent
   and
       formalisation/generalisation contribution
   remains explicit.

K. No scientific experiment was run.

L. No frozen empirical figure was recomputed.

M. No manuscript was drafted.

--------------------------------------------------
17. STOP CONDITIONS
--------------------------------------------------

STOP and report if:

1. TCAS material equivalence cannot be supported by authoritative evidence.

2. A newer source materially changes the novelty-audit conclusion.

3. ACAS X formal-verification precedent cannot be verified.

4. A source required for a load-bearing claim exists only as an unverifiable or unsuitable source.

5. The validated literature reveals a materially equivalent prior work not already accounted for that also performs the claimed generalisation/formalisation/empirical characterisation.

6. Source validation contradicts the intended two-contribution direction.

Do not resolve any of these by assumption.

--------------------------------------------------
18. COMPLETION STATUS
--------------------------------------------------

If all required source areas are satisfactorily validated:

    SOURCE_CORPUS_VALIDATION = CLOSED

If some non-load-bearing source remains unresolved:

    SOURCE_CORPUS_VALIDATION = CLOSED_WITH_OPEN_SUPPLEMENTARY_GAP

If a load-bearing issue remains:

    SOURCE_CORPUS_VALIDATION = BLOCKED

Do NOT set:

    CONTRIBUTION_FREEZE = CLOSED

during this task.

That is the next task.

--------------------------------------------------
19. FINAL REPORT
--------------------------------------------------

End with:

SOURCE_CORPUS_VALIDATION = <status>
MECHANISM_NOVELTY = WITHDRAWN
REPOSITIONING_DECISION = ACCEPTED
CONTRIBUTION_FREEZE = NOT_STARTED
CONFERENCE_MANUSCRIPT = NOT_DRAFTED

Then provide:

- PASS / FAIL / OPEN counts
- accepted contemporary sources
- authorised sources
- foundational historical sources
- rejected/replaced sources
- notes created/updated
- exact changed files
- unresolved issues

Do not proceed to contribution freeze or manuscript drafting.