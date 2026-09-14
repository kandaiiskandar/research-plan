TASK: AMICT CONFERENCE PAPER REBUILD — ARCHITECTURE TO EMPIRICAL EVALUATION

Objective
---------
Rebuild the previously rejected AMICT conference paper

"A Graduated Safety-State-Gated Architecture for AI Decision Support"

into a materially stronger conference paper centred on:

1. graduated advisory-scope governance,
2. executable implementation fidelity, and
3. empirical retrospective evaluation.

This is NOT a request to create a new architecture, invent new experiments, extend the scientific design, or rewrite Journal 1 wholesale.

The purpose is to convert the prior architecture-only conference paper into a focused conference follow-up that directly addresses prior reviewer criticism regarding lack of technical and empirical validation.

Target working title:

"Evaluating Graduated Advisory-Scope Governance for AI Decision Support"

Treat the title as PROVISIONAL until the novelty audit is completed.

--------------------------------------------------
1. PRIMARY SCIENTIFIC STORY
--------------------------------------------------

The conference paper must tell one coherent story:

Existing work commonly governs:
- whether AI participates,
- whether AI abstains,
- whether autonomous actions are allowed,
- or how decision authority shifts between human and AI.

This work instead evaluates a runtime governance mechanism that treats:

    AI participation

and

    AI advisory scope

as distinct governance dimensions.

The mechanism conditions the admissible recommendation space on an externally classified environmental governance state while preserving unconditional human decision authority.

Canonical conceptual relation:

    (G(S), A_AI(S))

with:

    A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅

The novelty is NOT:
- three states,
- traffic-light classification,
- external gating by itself,
- abstention,
- action masking,
- adjustable autonomy,
- or "AI safety" generally.

The candidate novelty is:

"runtime advisory-scope governance"

where the intermediate state restricts which recommendation types may be presented to a human decision-maker, without transferring final decision authority to the AI.

Do NOT claim:
- first-ever,
- globally novel,
- uniquely novel,
- safer,
- improved real-world safety,
- fewer accidents,
- better human decision quality,
- improved trust,
- improved calibrated reliance,
unless directly supported by evidence.

--------------------------------------------------
2. REQUIRED FIRST STEP — TARGETED NOVELTY AUDIT
--------------------------------------------------

Before drafting the paper, perform a bounded novelty audit.

Compare the proposed mechanism against ONLY the closest relevant prior-work families:

A. selective prediction / abstention / deferral
B. runtime assurance / Simplex-style assurance
C. shielding / action masking / admissible-action constraints
D. adjustable autonomy / mixed-initiative / graduated human-AI authority
E. graduated runtime governance / allow-escalate-block mechanisms

Primary question:

"Has prior work already implemented a mechanism in which the set of recommendation types that an AI decision-support system may present to a human is dynamically restricted according to an externally classified runtime risk/environmental state, while human final decision authority remains invariant?"

Create:

data/amict-conference-rebuild/novelty-defence-matrix.md

Columns:

- Prior-work family
- What is governed
- AI participation changed?
- Human authority changed?
- Executable action space changed?
- Advisory/recommendation scope changed?
- Runtime state-conditioned?
- Closest similarity to this work
- Key distinction
- Novelty threat level: LOW / MEDIUM / HIGH
- Evidence/source
- Wording allowed
- Wording prohibited

Do not perform a broad new systematic literature review.

Use:
1. existing repository literature first,
2. authoritative external sources only if needed for this bounded comparison.

Do not invent citations or bibliographic metadata.

If the novelty audit finds a materially equivalent prior mechanism, STOP before drafting and report the contradiction.

--------------------------------------------------
3. CONFERENCE CONTRIBUTION FREEZE
--------------------------------------------------

If the novelty audit supports the distinction, freeze the conference contributions to THREE:

C1 — Formal governance contribution
A runtime governance mechanism separating AI participation from state-conditioned admissible advisory scope.

C2 — Executable implementation-fidelity contribution
A bounded executable prototype evaluation demonstrating conformance to the configured advisory admissibility contract.

C3 — Empirical characterisation contribution
A retrospective environmental replay showing when graduated advisory-scope governance produces governance outcomes different from binary participation-only governance.

Do not add additional contributions without explicit evidence.

--------------------------------------------------
4. EVIDENCE BOUNDARY
--------------------------------------------------

Only use evidence already CLOSED.

FORMAL
------
P1–P4 = CLOSED

Use formal results only as needed for a conference paper.
Do not reproduce the entire Journal 1 formal development.

Canonical theorem home is Section 6 in Journal 1:
- Theorem 6.1 Totality
- Theorem 6.2 Monotonicity
- Theorem 6.3 Safety Dominance

Do not reintroduce obsolete Theorem 5.x numbering.

IMPLEMENTATION FIDELITY
-----------------------
F1–F3 = CLOSED / PASS

Canonical bounded figures:

Primary fidelity episodes:
    292

SAFE:
    32

CAUTION:
    260

Advisory records:
    454

Episodes with advisory:
    244

CAUTION episodes with no advisory:
    16

F1 violations:
    0

F2 violations:
    0

F3 mismatches:
    0

UNSAFE gate-off structural cases:
    162

IMPORTANT:
The 162 UNSAFE gate-off cases are not part of the 292 primary episode denominator.

IMPORTANT SAFE limitation:
    R-SAFE-001 = DEFERRED

All 32 SAFE fidelity episodes generated zero advisory records.

Current implemented rules are four CAUTION rules and generated advisory type is Delay.

Therefore:

DO NOT claim that:
- a populated SAFE rule set was evaluated,
- the full SAFE recommendation space was exercised,
- all A_AI(SAFE) recommendation types were generated,
- the prototype demonstrates real-world safety.

Implementation-fidelity claim allowed:

"The executable implementation produced zero violations of the configured advisory admissibility contract within the bounded deterministic interface-contract fidelity state space."

--------------------------------------------------
5. EMPIRICAL EVIDENCE
--------------------------------------------------

The conference paper should centre the empirical contribution on the existing retrospective environmental trace.

PRIMARY configuration:
    43,848 hourly records
    approximately 5 years

Do not describe the fidelity episode set as historical replay.

E1 — Pairwise governance divergence
PRIMARY:
    C0↔C1 = 42.88%
    C0↔C2 = 48.69%
    C1↔C2 = 5.81%
    C1↔C3 = 0.00%

RESOLUTION:
    C0↔C1 = 41.08%
    C0↔C2 = 45.56%
    C1↔C2 = 4.48%
    C1↔C3 = 0.00%

E2 — Intermediate Level-2 contribution
PRIMARY:
    ΔL2 = 5.81%

RESOLUTION:
    ΔL2 = 4.48%

Interpretation allowed:

"The intermediate advisory-scope governance level is empirically non-vacuous within the evaluated trace."

Interpretation prohibited:

"5.81% safer"
"5.81% risk reduction"
"5.81% improvement"
"5.81% accident prevention"

E3 — Resolution sensitivity
Scope is ONLY:
    {E1, E2, E6}

PRIMARY and RESOLUTION are alternative configurations.

They are NOT:
- confidence intervals,
- uncertainty bounds,
- repeated trials,
- error bars.

Do not write:
    5.81 ± 4.48
or equivalent.

E4 — Temporal dynamics / hysteresis
PRIMARY only:

Total state transitions:
    3,661

Scheduled transitions:
    3,439

Non-scheduled transitions:
    222

Genuine oscillations:
    26

Oscillation rate:
    approximately 5.2/year

Hysteresis reduction of non-scheduled transitions:
    10.36%

E4_RESOLUTION:
    NOT_REQUIRED_BY_CURRENT_E3_DESIGN

Do not create a RESOLUTION hysteresis result.

E6:
    C1↔C3 = 0.00%

Use this carefully.

Allowed interpretation:

"An intermediate state or traffic-light topology alone does not necessarily create advisory-scope differentiation."

Do NOT overstate this as a universal theorem about all traffic-light systems.

--------------------------------------------------
6. OPEN / EXCLUDED EVIDENCE
--------------------------------------------------

E5 = OPEN

E5_HARNESS = CLOSED
MacBook reference = COMPLETE / REFERENCE_ONLY
Android target-hardware benchmark = DEFERRED_MANDATORY
H3 = OPEN / UNSUPPORTED

DO NOT:
- create an E5 result,
- use MacBook timing as target-hardware evidence,
- claim mobile performance,
- invent latency thresholds,
- claim H3 PASS.

For this conference paper, E5 must NOT be a research question.

If relevant, mention target-hardware performance as future work or limitation only.

Human study:
    NOT REQUIRED for this conference paper.

Do not claim:
- user trust,
- decision quality,
- adoption,
- actionability,
- livelihood improvement,
- real-world safety outcome,
- accident reduction.

--------------------------------------------------
7. PRIOR CONFERENCE PAPER — USE AS FOUNDATION, NOT AUTHORITY
--------------------------------------------------

Use the rejected conference paper as a structural and historical baseline.

Retain only material that remains scientifically valid.

Expected treatment:

KEEP / COMPRESS:
- problem motivation
- advisory-scope gap
- useful related work
- core governance concept
- human authority framing

REWRITE:
- Abstract
- Introduction
- Contributions
- Methodology
- Domain instantiation
- Conclusion

REMOVE OR STRONGLY COMPRESS:
- illustrative-only scenario
- broad unsupported mechanistic claims
- "being developed as a prototype"
- architecture-only presentation
- excessive literature-review methodology

The old paper must not control newer scientific authority.

Where the old paper conflicts with:
- Journal 1 formalisation,
- evaluation specification,
- Layer 3 implementation authority,
- Batch 5 fidelity evidence,
- E1–E4/E6 evidence,
the newer canonical authority wins.

--------------------------------------------------
8. TARGET CONFERENCE PAPER STRUCTURE
--------------------------------------------------

Use a concise IEEE-style conference structure:

I. Introduction

II. Related Work and Research Gap

III. Graduated Advisory-Scope Governance
    A. Runtime governance model
    B. State-conditioned admissible advisory space
    C. Safety Dominance / formal property

IV. Prototype and Evaluation Method
    A. Executable prototype
    B. Fidelity evaluation
    C. Retrospective environmental replay
    D. Governance comparators
    E. Resolution sensitivity

V. Results
    A. Implementation fidelity
    B. Pairwise governance divergence
    C. Intermediate-level contribution
    D. Temporal dynamics / hysteresis

VI. Discussion and Limitations
    A. What the evidence establishes
    B. What it does not establish
    C. SAFE-rule limitation
    D. Target-hardware limitation
    E. External validity

VII. Conclusion

Do not force subsections if page constraints make them unnecessary.

--------------------------------------------------
9. RESEARCH QUESTIONS
--------------------------------------------------

Use ONLY research questions that can be answered by CLOSED evidence.

Proposed RQs:

RQ1:
Can the proposed advisory-scope governance mechanism enforce state-conditioned containment of AI-generated recommendations?

RQ2:
Does the executable prototype conform to the configured governance contract across the bounded fidelity state space?

RQ3:
How often does graduated advisory-scope governance produce governance outcomes different from binary participation-only governance in retrospective environmental replay?

Optional RQ4 only if space permits:
How does hysteresis affect governance-state transition stability over the primary retrospective trace?

Do NOT include:
- target-hardware latency RQ,
- human-trust RQ,
- safety outcome RQ,
- user utility RQ.

--------------------------------------------------
10. CONFERENCE RESULTS PRIORITY
--------------------------------------------------

Highest-priority results:

1. ΔL2:
       5.81% PRIMARY
       4.48% RESOLUTION

2. C1↔C3:
       0.00% PRIMARY
       0.00% RESOLUTION

3. Fidelity:
       292 episodes
       454 advisory records
       0 F1 violations
       0 F2 violations
       0 F3 mismatches

Secondary result if space allows:

4. Hysteresis:
       3,661 transitions
       26 genuine oscillations
       10.36% reduction in non-scheduled transitions

Do not overload the conference paper with every Journal 1 number.

--------------------------------------------------
11. REQUIRED TABLES / FIGURES
--------------------------------------------------

Propose, but do not fabricate, a minimum set.

Preferred:

TABLE I
Closest related governance mechanisms / novelty comparison.

TABLE II
Governance states and admissible advisory sets.

TABLE III
Evaluation summary and main results.

FIGURE 1
Compact architecture:
environmental observations
→ deterministic state classifier
→ governance state
→ admissible advisory scope
→ Layer 3 reasoning
→ human decision-maker

Optional FIGURE 2:
Comparator / divergence result visualisation.

All figures must preserve:
- human decision authority,
- gate-off at UNSAFE,
- CAUTION scope restriction,
- no automatic final action by AI.

--------------------------------------------------
12. AMICT TEMPLATE CONSTRAINTS
--------------------------------------------------

Use the provided AMICT template as formatting authority.

Important:
- IEEE-style A4 two-column layout.
- No subtitle.
- Do not put symbols, special characters, footnotes or math in the title or abstract.
- Double-blind review: author identities must not appear in the text body.
- Figure captions below figures.
- Table titles above tables.
- Citations numbered consecutively in brackets.

Do not alter template margins, column widths, fonts or spacing.

Do not insert author-identifying information into the review manuscript.

--------------------------------------------------
13. CLAIM DISCIPLINE
--------------------------------------------------

Every material statement must be classified as one of:

FORMAL
IMPLEMENTATION-FIDELITY
EMPIRICAL-TRACE
LITERATURE
INTERPRETATION
LIMITATION

Create:

data/amict-conference-rebuild/claim-evidence-matrix.csv

Columns:
- claim_id
- manuscript_section
- claim_text
- claim_type
- evidence_source
- evidence_status
- allowed
- limitation
- notes

No quantitative claim may appear without provenance.

Do not transform:
- deterministic census into statistical inference,
- sensitivity configuration into uncertainty interval,
- formal containment into empirical safety,
- prototype fidelity into real-world effectiveness.

--------------------------------------------------
14. REQUIRED AUDITS
--------------------------------------------------

Before declaring the task complete, perform:

A. Quantitative provenance audit
Every number in the paper must resolve to canonical evidence.

B. Novelty/overclaim audit
Search for:
- first
- novel
- unprecedented
- safer
- safety improvement
- risk reduction
- validated
- proven safe
- real-world
- effective
- optimal

Classify every occurrence.

C. Status audit
Confirm:

P1–P4 = CLOSED
F1–F3 = CLOSED
E1–E4 = CLOSED
E6 = CLOSED
E5 = OPEN
R-SAFE-001 = DEFERRED
H3 = OPEN / UNSUPPORTED

D. SAFE-rule negative control
Verify that the paper never implies that a populated SAFE rule set was tested.

E. Historical replay boundary
Verify that 292 fidelity episodes are never described as the five-year replay.

F. Human outcome boundary
Verify no unsupported claim about:
- safety improvement,
- accidents,
- trust,
- behaviour,
- livelihood,
- decision quality.

G. Formal-reference audit
No obsolete Theorem 5.x references.

H. Double-blind audit
No author identity or affiliation in text body.

--------------------------------------------------
15. OUTPUT ARTEFACTS
--------------------------------------------------

Create under:

data/amict-conference-rebuild/

At minimum:

1. novelty-defence-matrix.md
2. conference-contribution-freeze.md
3. evidence-boundary.md
4. claim-evidence-matrix.csv
5. quantitative-provenance.csv
6. prior-paper-change-map.md
7. conference-paper-outline.md
8. overclaim-audit.md
9. double-blind-audit.md
10. verification.json
11. report.md

And create a draft manuscript in the appropriate conference submission directory.

Do NOT overwrite the rejected historical submission.

Create a new version/submission path.

--------------------------------------------------
16. STOP CONDITIONS
--------------------------------------------------

STOP and report rather than guessing if:

1. Prior work is found that is materially equivalent to the claimed advisory-scope governance novelty.
2. A required numerical result conflicts across canonical artefacts.
3. The old conference paper and newer authority cannot be reconciled without changing scientific design.
4. A required reference cannot be verified.
5. Conference page limit cannot be established and it materially affects manuscript completion.
6. A requested claim would require a new experiment.
7. A requested claim depends on E5, H3, human study, or R-SAFE-001 completion.

Do not resolve contradictions by inventing assumptions.

--------------------------------------------------
17. PROHIBITED ACTIONS
--------------------------------------------------

Do NOT:

- run new scientific experiments,
- reopen CLOSED workstreams,
- change architecture,
- change thresholds,
- alter evaluation design,
- create a new comparator,
- extend historical replay,
- perform new Android benchmark,
- invent SAFE rules,
- invent recommendation types,
- add human participants,
- invent references,
- invent statistical significance,
- invent confidence intervals,
- claim real-world safety,
- claim clinical/operational effectiveness,
- describe this as a validated deployed system,
- copy the Journal 1 manuscript wholesale.

--------------------------------------------------
18. COMPLETION CRITERIA
--------------------------------------------------

The task is complete only if:

NOVELTY_AUDIT = PASS
CONTRIBUTION_FREEZE = COMPLETE
CONFERENCE_DRAFT = COMPLETE
QUANTITATIVE_PROVENANCE = PASS
CLAIM_EVIDENCE_AUDIT = PASS
OVERCLAIM_AUDIT = PASS
SAFE_RULE_NEGATIVE_CONTROL = PASS
HISTORICAL_REPLAY_BOUNDARY = PASS
DOUBLE_BLIND_AUDIT = PASS
FORMAL_REFERENCE_AUDIT = PASS
E5_REMAINS_OPEN = true
H3_REMAINS_OPEN_UNSUPPORTED = true
R_SAFE_001_REMAINS_DEFERRED = true

Final status must NOT be "scientifically complete" or "journal reviewer ready".

Use:

AMICT_CONFERENCE_REBUILD = DRAFT_COMPLETE_PENDING_FINAL_FORMAT_AND_SUBMISSION_REVIEW

unless a STOP condition occurs.

--------------------------------------------------
19. FINAL REPORT FORMAT
--------------------------------------------------

Report:

1. Executive decision:
   PASS / STOP

2. Novelty finding

3. Final contribution statement

4. Sections created/revised

5. Evidence used

6. Key numerical results

7. Limitations preserved

8. Claims deliberately excluded

9. References added/removed

10. Verification totals:
    PASS / FAIL / OPEN

11. Changed files

12. Scientific status after task

13. Exact closure sentence:

"AMICT CONFERENCE PAPER REBUILD CLOSED — PRIOR ARCHITECTURE-ONLY SUBMISSION REFRAMED AS A FORMAL, EXECUTABLE AND EMPIRICALLY CHARACTERISED ADVISORY-SCOPE GOVERNANCE STUDY WITHOUT EXTENDING THE FROZEN SCIENTIFIC EVIDENCE BASE."

Only use the closure sentence if all completion criteria pass.