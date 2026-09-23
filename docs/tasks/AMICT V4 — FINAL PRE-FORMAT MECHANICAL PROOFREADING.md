TASK: AMICT V4 — FINAL PRE-FORMAT MECHANICAL PROOFREADING

Context
-------
AMICT V4 scientific work is CLOSED.

Current authoritative state:

    POST_DRAFT_AUDIT                  = CLOSED
    RELATED_WORK_MICRO_REPAIR         = CLOSED
    RELATED_WORK_FUNCTIONAL_FRAMING   = PASS
    REVIEW_HISTORY_DEPENDENCY         = NONE
    CORPUS_SIZE_DEPENDENCY            = NONE
    FORMAL_SLR_DEPENDENCY             = NONE
    AUDIT_PROTOCOL_DEPENDENCY         = NONE
    POPULATION_LEVEL_LITERATURE_CLAIM = NONE
    SCOPED_SEARCH_OUTCOME_LANGUAGE    = PASS

    REFERENCE_COUNT                   = 19
    ORPHAN_REFERENCES                 = 0
    DANGLING_CITATIONS                = 0
    BODY_WORD_COUNT                   = 3674
    PROTECTED_DISCLOSURES             = PASS

    MANUSCRIPT_V4_SCIENTIFIC_TEXT     = REVIEWER_READY
    FORMAT_READY                      = NO

The scientific argument is now FROZEN.

This task is NOT another scientific review.

It is a narrow mechanical proofreading pass before the manuscript is
placed into the official AMICT template.

==================================================
1. OBJECTIVE
==================================================

Inspect the complete current V4 manuscript for mechanical defects that
may have been introduced during the sequence of surgical scientific
edits.

Look specifically for:

- duplicated sentences
- duplicated clauses
- accidental repetition
- broken sentences
- missing words
- obvious grammar defects
- subject-verb disagreement
- malformed punctuation
- doubled punctuation
- inconsistent spacing
- broken Markdown
- malformed equations or notation
- inconsistent section/table references
- citation punctuation defects
- stale citation numbers after renumbering
- broken citation ranges
- table/prose numerical mismatch
- table/prose terminology mismatch
- obvious copy-edit artefacts
- incomplete edit remnants

Do NOT perform stylistic rewriting merely because another wording might
sound better.

==================================================
2. KNOWN DEFECT — FIX
==================================================

Section V.C currently contains:

    "The two configurations differ in both wave model and record
    length. The configurations differ in both wave model and record
    length; this evaluation does not isolate which difference accounts
    for the observed spread of approximately 1.3 percentage points."

This is an accidental duplication produced by prior surgical editing.

Replace the duplicated construction with:

    "The configurations differ in both wave model and record length;
    this evaluation does not isolate which difference accounts for the
    observed spread of approximately 1.3 percentage points."

Do not otherwise reinterpret RQ3.

The paragraph must continue to state:

    PRIMARY Δ_L2 = 5.81%
    RESOLUTION Δ_L2 = 4.48%
    spread ≈ 1.3 percentage points
    C1 against C3 = 0.00%
    configurations differ in wave model AND record length
    evaluation does not isolate causation

==================================================
3. SCIENTIFIC FREEZE
==================================================

Do NOT change:

- title
- Abstract scientific meaning
- RQ1
- RQ2
- RQ3
- C1
- C2
- canonical gap statement
- canonical novelty-positioning sentence
- architecture
- governance pair
- operational semantics
- formal properties
- comparator definitions
- thresholds
- evaluation design
- empirical values
- interpretation of empirical values
- avionics precedent
- Related Work scientific positioning
- site wording
- lower-bound interpretation
- protected disclosures
- R-SAFE-001 status
- E5/H3 status
- provenance-open item

Do not add scientific claims.

Do not remove scientific limitations.

Do not improve scientific arguments.

Do not reopen novelty.

Do not run experiments.

==================================================
4. RELATED WORK IS FROZEN
==================================================

The recently repaired Related Work framing is CLOSED.

Preserve:

    "Prior work informing this study is considered in two groups..."

Preserve the functional distinction:

    governance framing
        versus
    closest-mechanism comparison

Preserve:

    "what we did not identify in the reviewed AI-governance
    literature..."

Do NOT restore:

- 72
- 72 papers
- structured review
- earlier review
- review protocol
- bounded audit
- corpus size
- original search
- screening protocol

Do not restore removed reference Ghaleb.

Current reference count is 19.

==================================================
5. CANONICAL TEXT LOCK
==================================================

Verify by exact/normalised comparison that the following remain
unchanged after proofreading:

    RQ1 = exact
    RQ2 = exact
    RQ3 = exact

    canonical gap statement = exact

    canonical novelty-positioning sentence =
        exact in all existing occurrences

If a mechanical correction appears necessary inside one of these
frozen strings:

    STOP

Report it rather than editing it.

==================================================
6. NUMERICAL INTEGRITY
==================================================

Verify all headline quantities without recomputing experiments:

    43,848 primary hourly records
    9,135 departure-window observations

    C0 against C1 = 42.88%
    C0 against C2 = 48.69%

    Δ_L2 PRIMARY = 5.81%
    Δ_L2 RESOLUTION = 4.48%

    C1 against C3 =
        0.00% PRIMARY
        0.00% RESOLUTION

    bounded conformance:
        292 primary episodes
        32 permissive
        260 intermediate
        244 advisory episodes
        16 intermediate episodes with no advisory
        454 advisory records
        162 gate-off structural cases

    wind:
        2 activations
        0 bindings

Do not introduce:

    41.08
    45.56

Those values remain excluded because provenance is incomplete.

==================================================
7. TABLE INTEGRITY
==================================================

Check TABLE I, TABLE II and TABLE III against surrounding prose.

Confirm:

    TABLE_COUNT = 3

Check:

TABLE I
    citation numbers valid after 19-reference renumbering
    mechanism labels consistent with prose
    no stale old citation number

TABLE II
    invalid / absent / stale / unmeasured semantics unchanged
    exclusion remains distinct from fault

TABLE III
    5.81 / 4.48 correct
    0.00 / 0.00 correct
    42.88 primary only
    48.69 primary only
    resolution pairwise provenance-open values remain "not reported"

Do not redesign tables in this task.

==================================================
8. REFERENCE INTEGRITY
==================================================

Perform a mechanical citation/reference check.

Required:

    REFERENCE_COUNT = 19
    numbering = contiguous 1..19
    ORPHAN_REFERENCES = 0
    DANGLING_CITATIONS = 0

Verify all citation numbers in prose and tables refer to the intended
renumbered source.

Specifically verify:

    FAA AC 20-151C
    Cleaveland spelling
    no AC 20-151A
    no Cleveland misspelling

Do not add references.

Do not remove references unless a genuine mechanical corruption is
found.

If reference integrity cannot be maintained without a scientific
decision:

    STOP

==================================================
9. PROTECTED DISCLOSURES
==================================================

Re-run the protected-disclosure check.

Required:

    PROTECTED_DISCLOSURES = PASS (19/19)

Do not cut or weaken any disclosure.

The literature-related disclosure remains in its CURRENT functional
form, not the historical 72-paper form.

==================================================
10. PROHIBITED CLAIM SCAN
==================================================

Confirm no surgical edit introduced language equivalent to:

    first-ever
    unprecedented
    globally novel
    uniquely novel
    no prior work
    no existing architecture
    domain-independent
    safer
    safety improvement
    risk reduction
    real-world validation
    validated human outcomes
    454 advisory types
    robustness across configurations
    replicated result

Context-inspect hits rather than mechanically rejecting legitimate
negations or bibliographic titles.

==================================================
11. DOUBLE-BLIND SCIENTIFIC TEXT
==================================================

Check the manuscript body for:

- author names
- affiliations
- emails
- acknowledgements
- "our previous work"
- "our earlier work"
- "companion journal"
- "forthcoming"
- "under review"
- internal repository references

The build comment at the head of the Markdown is already known and is
NOT to be removed in this task.

Keep:

    BUILD_COMMENT = REMOVE_BEFORE_SUBMISSION

Formatting will remove it.

Scientific body must remain:

    DOUBLE_BLIND_SCIENTIFIC_TEXT = PASS

==================================================
12. WHAT COUNTS AS AN EDIT
==================================================

Allowed edits are only Level-0 mechanical corrections:

Examples:

    duplicated sentence → remove duplicate
    duplicated word → remove duplicate
    missing comma that changes readability → repair
    obvious typo → repair
    stale citation number → correct to intended renumbered reference
    broken Markdown → repair
    malformed punctuation → repair

Not allowed:

    rewrite paragraph for elegance
    strengthen argument
    shorten discussion for page fit
    change terminology for style
    alter scientific interpretation
    add literature
    remove limitations
    compress protected disclosures
    change comparator wording
    change novelty wording

If uncertain whether something is mechanical or scientific:

    DO NOT EDIT IT.

Report it as:

    REVIEW_REQUIRED

==================================================
13. FULL MANUSCRIPT READ
==================================================

Do not stop after fixing the known RQ3 duplication.

Read the complete manuscript from:

    title
        through
    final reference

The purpose of this task is to detect surgical-edit artefacts before
formatting.

Pay particular attention to boundaries between paragraphs that were
edited during:

- post-draft scientific audit
- Related Work corpus reframe
- Related Work micro-repair
- reference renumbering
- RQ3 causal-language correction

==================================================
14. AUDIT RECORD
==================================================

Append:

    Addendum C — Final Pre-Format Mechanical Proofreading

to:

    post-draft-audit.md

Do NOT rewrite:

    original audit
    Addendum A
    Addendum B

Record:

1. defects found;
2. exact before/after for every edit;
3. classification of each edit;
4. numerical-integrity result;
5. table-integrity result;
6. reference-integrity result;
7. canonical-text integrity;
8. protected-disclosure result;
9. double-blind scientific-text result;
10. final word count;
11. files changed.

==================================================
15. STOP CONDITIONS
==================================================

STOP rather than edit if you find:

- contradiction in scientific interpretation
- unsupported scientific claim requiring substantive repair
- canonical frozen text requiring modification
- empirical number mismatch that cannot be explained mechanically
- comparator inconsistency
- reference problem requiring a new scientific source
- protected disclosure that cannot be preserved
- evidence/provenance contradiction

Report such an item separately as:

    SCIENTIFIC_REOPEN_REQUIRED

Do not solve it inside this task.

==================================================
16. SUCCESS CONDITIONS
==================================================

If successful, return:

    PRE_FORMAT_MECHANICAL_PROOFREAD = CLOSED
    KNOWN_RQ3_DUPLICATION           = FIXED
    MECHANICAL_DEFECTS_REMAINING    = 0
    SCIENTIFIC_REOPEN_REQUIRED      = NO

    RQ_INTEGRITY                    = PASS
    GAP_STATEMENT_INTEGRITY         = PASS
    NOVELTY_SENTENCE_INTEGRITY      = PASS
    NUMERICAL_INTEGRITY             = PASS
    TABLE_INTEGRITY                 = PASS

    REFERENCE_COUNT                 = 19
    ORPHAN_REFERENCES               = 0
    DANGLING_CITATIONS              = 0

    PROTECTED_DISCLOSURES           = PASS
    DOUBLE_BLIND_SCIENTIFIC_TEXT    = PASS

    MANUSCRIPT_V4_SCIENTIFIC_TEXT   = REVIEWER_READY
    FORMAT_READY                    = NO

Report the resulting BODY_WORD_COUNT.

Do not proceed to AMICT formatting.