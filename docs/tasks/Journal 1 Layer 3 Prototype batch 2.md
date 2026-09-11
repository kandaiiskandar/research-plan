# Task — Journal 1 Layer 3 Prototype

## Batch 2: Concrete Layer 3 Advisory Rule Scientific Specification

### Goal

Resolve, or precisely bound, `OPEN-L3-1` by developing a scientifically defensible specification for the concrete Layer 3 advisory rules used by:

```text
RS(SAFE)
RS(CAUTION)
```

The purpose of this batch is to determine:

```text
1. what advisory rules are scientifically warranted;
2. what input variables each rule may use;
3. what antecedents activate each rule;
4. what recommendation type each rule may conclude;
5. what evidence supports each antecedent → conclusion mapping;
6. which rules belong to SAFE and which belong to CAUTION;
7. which recommendation types remain unsupported and therefore OPEN.
```

This is a **scientific rule-specification task**.

It is NOT yet the executable prototype implementation.

Do not implement the engine.
Do not run F1–F3.
Do not run E5.
Do not invent advisory rules merely to populate all recommendation types.
Do not convert Layer 2 classification thresholds directly into Layer 3 advisory rules without independent justification.

---

# 1. Branch

Continue on:

```text
feat/journal1-layer3-prototype
```

Do not create a new branch.

Batch 1 is CLOSED with:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 1 CLOSED —
FIDELITY TRACE AND FAILURE-SEMANTICS CONTRACT REPAIRED
```

Do not reopen Batch 1 unless a genuine scientific contradiction is discovered.

---

# 2. Immediate authority

Primary Layer 3 implementation authority:

```text
publications/active/journal-1/layer3-prototype-specification.md
```

Scientific upstream authorities:

```text
publications/active/journal-1/algorithm-specification.md
publications/active/journal-1/evaluation-specification.md
publications/active/journal-1/research-design.md
docs/canonical/appendix-c-formalisation.md
docs/canonical/architecture-illustration.md
docs/canonical/justification-layer3-enforcement.md
```

Inspect any existing literature-review, evidence, fisheries-domain, safety,
operational, maritime, or advisory-rule artefacts in the repository that
could provide scientific support for Layer 3 rule content.

Do not assume that absence from the six closed upstream documents means
the wider repository contains no usable evidence.

---

# 3. Protected scientific state

Before editing, verify the same protected canonical state used in the
previous workstreams.

Do not modify:

```text
canonical formalisation
canonical empirical findings
canonical replay scripts
canonical g_t implementation
solar artefact
raw replay data
prediction register
submitted conference manuscripts
```

If protected state differs unexpectedly:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 2 OPEN —
PROTECTED CANONICAL STATE DRIFT
```

STOP.

---

# 4. Existing governance contract is immutable

Preserve exactly:

```text
S = {SAFE, CAUTION, UNSAFE}
```

and:

```text
G(SAFE)    = 1
G(CAUTION) = 1
G(UNSAFE)  = 0
```

Recommendation universe:

```text
R = {
    Go,
    Delay,
    DepartureTime,
    Duration
}
```

Admissible scopes:

```text
A_AI(SAFE)
=
{Go, Delay, DepartureTime, Duration}

A_AI(CAUTION)
=
{Go, Delay}

A_AI(UNSAFE)
=
∅
```

Therefore:

```text
ConclusionTypes(RS(SAFE))
⊆
{Go, Delay, DepartureTime, Duration}
```

and:

```text
ConclusionTypes(RS(CAUTION))
⊆
{Go, Delay}
```

and:

```text
RS(UNSAFE) = ∅
```

Do not change these mappings to accommodate desired rules.

---

# 5. Critical scientific distinction

Preserve:

```text
Layer 2 classification
≠
Layer 3 advisory reasoning
```

Layer 2 determines:

```text
S
```

Layer 3 determines advisory content within:

```text
A_AI(S)
```

Therefore a Layer 2 threshold such as:

```text
rain > 20
wave > 1.25
wind > 27
```

does NOT automatically imply a Layer 3 rule such as:

```text
IF rain > 20 THEN Delay
IF wave > 1.25 THEN Delay
IF wind < 21.6 THEN Go
```

Those mappings require independent advisory justification.

Do not create circular logic where the same threshold both determines
the governance state and is then reused without justification to create
the advisory recommendation.

---

# 6. Scientific question for Batch 2

For every proposed rule, answer:

```text
Given that the architecture has already classified the episode as S,
what additional evidence warrants this specific advisory conclusion?
```

The rule must add advisory reasoning within the permitted scope.

It must not merely restate the state classifier.

---

# 7. Recommendation semantics

Before defining rules, specify the precise semantics of the four existing
recommendation types.

At minimum:

```text
Go
Delay
DepartureTime
Duration
```

For each, define:

```text
meaning
decision variable affected
expected payload
human interpretation
what it does NOT mean
applicable governance states
```

Do not redefine their formal membership in `R`.

---

# 8. Go semantics

Define `Go` carefully.

`Go` must NOT mean:

```text
safe to depart
approved to depart
permission to depart
risk-free departure
```

A bounded interpretation should be closer to:

```text
an AI advisory indicating that the evaluated advisory rules do not
identify a reason, within the rule system's configured scope, to
recommend delay or adjustment.
```

However, do not adopt this exact wording automatically.

Determine the strongest semantics supported by the architecture and evidence.

Human authority remains unconditional.

---

# 9. Delay semantics

Define what `Delay` means.

Possible dimensions may include:

```text
defer departure
wait for a condition to change
reassess later
```

but these are not automatically authoritative.

Determine whether available evidence supports:

```text
Delay
```

as:

```text
a recommendation type only
```

or whether a time payload is scientifically warranted.

Do not invent:

```text
delay 30 minutes
delay 1 hour
delay until rain stops
```

without evidence.

---

# 10. DepartureTime semantics

`DepartureTime` is available only in:

```text
SAFE
```

because:

```text
DepartureTime ∈ A_AI(SAFE)
DepartureTime ∉ A_AI(CAUTION)
```

Determine whether there is sufficient scientific authority for Layer 3
to recommend a specific departure time or departure window.

Do not infer a departure time merely from sunrise.

For example:

```text
sunrise = 06:03
```

does NOT automatically justify:

```text
recommended departure = 06:03
```

The solar rule in Layer 2 determines governance participation.

It does not establish an optimal fishing departure time.

If evidence is insufficient:

```text
DepartureTime rule content remains OPEN.
```

This is acceptable.

---

# 11. Duration semantics

`Duration` is also available only in SAFE.

Determine what the recommendation would represent:

```text
maximum suggested trip duration?
expected fishing duration?
recommended time at sea?
return-before condition?
```

Do not choose one without authority.

Do not derive duration solely from:

```text
sunset - departure time
```

unless evidence explicitly warrants that advisory interpretation.

If evidence is insufficient:

```text
Duration rule content remains OPEN.
```

---

# 12. No requirement to populate every recommendation type

This is mandatory.

Batch 2 does NOT require:

```text
one Go rule
one Delay rule
one DepartureTime rule
one Duration rule
```

A valid result could be:

```text
Go              SUPPORTED
Delay           SUPPORTED
DepartureTime   OPEN
Duration        OPEN
```

or even:

```text
Go              OPEN
Delay           SUPPORTED
DepartureTime   OPEN
Duration        OPEN
```

depending on evidence.

Scientific incompleteness is preferable to fabricated completeness.

---

# 13. Evidence search

Conduct a repository-wide evidence search for sources relevant to:

```text
small-scale fishing departure decisions
weather-related fishing advisories
marine operational decision support
rainfall and fishing operations
wave conditions and small fishing vessels
wind and departure decisions
daylight constraints
trip timing
trip duration
weather-window decision making
fisher decision behaviour
Sabah small-scale fisheries
Zone A fisheries
```

Search existing:

```text
literature review
evidence matrices
conference work
PhD proposal
research design
references
domain reports
government guidance
maritime guidance
fisheries studies
```

Record every candidate source.

Do not rely on filename alone.

Inspect the actual supporting passage.

---

# 14. External research boundary

If repository evidence is insufficient, do NOT silently invent rules.

Record the evidence gap first.

If this task environment has an approved research mechanism and external
research is explicitly part of the project workflow, identify candidate
authoritative sources separately.

Prioritise, where relevant:

```text
peer-reviewed fisheries literature
METMalaysia
Department of Fisheries Malaysia
Marine Department Malaysia
FAO
IMO
WMO
government maritime guidance
peer-reviewed small-scale fisheries safety research
```

Distinguish:

```text
repository-supported
external-source-supported
interpretive proposal
unsupported
```

Do not collapse these categories.

---

# 15. Evidence hierarchy

For each proposed rule classify its support:

```text
LEVEL A — Direct normative/operational authority
LEVEL B — Direct empirical fisheries evidence
LEVEL C — Strong domain evidence requiring bounded adaptation
LEVEL D — Architecture/design interpretation
UNSUPPORTED
```

Define these categories precisely in the authority document.

Do not present Level D as equivalent to Level A.

---

# 16. Rule provenance requirement

Every concrete rule must have:

```text
rule_id
applicable_state
antecedent
conclusion_type
conclusion_payload
evidence_source
evidence_location
evidence_level
adaptation_required
scientific_rationale
limitations
status
```

No rule may have:

```text
evidence_source = "architecture"
```

if the architecture only permits the recommendation type but does not
justify the antecedent → conclusion mapping.

---

# 17. Rule status vocabulary

Use:

```text
SUPPORTED
CONDITIONALLY SUPPORTED
PROPOSED — REQUIRES VALIDATION
OPEN — INSUFFICIENT EVIDENCE
REJECTED
```

Definitions:

```text
SUPPORTED
= evidence directly warrants the rule within the study context.

CONDITIONALLY SUPPORTED
= evidence supports the relationship but bounded adaptation is required.

PROPOSED — REQUIRES VALIDATION
= scientifically plausible design rule but not sufficiently established
  to be treated as validated domain knowledge.

OPEN — INSUFFICIENT EVIDENCE
= no defensible concrete rule can currently be specified.

REJECTED
= candidate rule conflicts with architecture, evidence, or governance.
```

Do not silently promote PROPOSED to SUPPORTED.

---

# 18. Rule antecedent design

For each rule determine whether antecedents use:

```text
resolved environmental observations
derived variables
vessel category
governance state
temporal information
combinations thereof
```

Do not silently introduce new sensors or inputs.

Any antecedent variable must map to an existing authoritative input or be
explicitly introduced as a new implementation requirement.

If a rule requires unavailable data:

```text
rule remains CONDITIONAL / OPEN
```

depending on severity.

---

# 19. Avoid classifier duplication

Audit each candidate rule for:

```text
CLASSIFIER_DUPLICATION
```

Example:

```text
Layer 2:
wave > threshold
→ UNSAFE
```

Candidate Layer 3:

```text
IF wave > same threshold
THEN Delay
```

This is structurally impossible in the normal governed path because
Layer 3 receives:

```text
G(UNSAFE)=0
```

and does not reason.

Likewise, do not construct rules whose antecedent can occur only in a
state where the conclusion type is unavailable.

---

# 20. State-conditioned reasoning

Candidate rules should be reasoned about conditional on the governing state.

Conceptually:

```text
RS(SAFE):
    advisory reasoning permitted within FULL scope

RS(CAUTION):
    advisory reasoning permitted only within {Go, Delay}

RS(UNSAFE):
    ∅
```

Do not create rules for UNSAFE.

---

# 21. CAUTION is not automatically Delay

This is mandatory.

Do not encode:

```text
IF S == CAUTION
THEN Delay
```

unless scientifically justified.

The architecture says:

```text
A_AI(CAUTION) = {Go, Delay}
```

It does NOT say:

```text
AI(CAUTION) = Delay
```

CAUTION limits advisory scope.

It does not determine the advisory conclusion.

---

# 22. SAFE is not automatically Go

Likewise, do not encode:

```text
IF S == SAFE
THEN Go
```

merely because `Go ∈ A_AI(SAFE)`.

SAFE defines what Layer 3 may say.

It does not automatically determine what Layer 3 should say.

---

# 23. Potential rule interaction

For each supported candidate rule identify whether multiple rules may fire.

Do not invent conflict resolution yet unless needed.

Record cases such as:

```text
Go + Delay
multiple Delay rules
multiple DepartureTime rules
DepartureTime + Duration
```

Determine whether these combinations are:

```text
compatible
conflicting
requires aggregation
requires priority
OPEN
```

This may expose a new scientific or implementation decision.

Do not silently choose salience or priority.

---

# 24. Contradictory advisory outputs

Explicitly analyse whether:

```text
Go
```

and:

```text
Delay
```

could be emitted in the same episode.

If candidate rules make this possible, do not simply select one.

Record:

```text
ADVISORY_CONFLICT_POLICY_REQUIRED
```

and determine whether it is:

```text
scientific policy
or
implementation policy
```

If scientific meaning is required to resolve it, STOP that portion of the
rule specification rather than inventing priority.

---

# 25. Payload specification

For each supported recommendation type define the minimum scientifically
warranted payload.

Examples of payload categories might include:

```text
reason
time
duration
condition
confidence
```

but do not add them automatically.

The existing Batch 1 schema has:

```text
conclusion_payload
```

OPEN-L3-1.

Batch 2 should resolve payload semantics only where evidence supports them.

---

# 26. Explanation field

The prototype includes:

```text
Advisory.explanation
```

Determine whether explanation should be:

```text
rule rationale
triggered condition summary
human-readable evidence statement
```

Do not encode scientific certainty that the evidence does not support.

Avoid wording such as:

```text
This trip is safe.
```

Prefer bounded state/advisory explanations.

---

# 27. Cause taxonomy boundary

Do not misuse canonical:

```text
reasons ∈ {fault, hazard, policy}
```

as Layer 3 advisory rules.

The cause taxonomy is explanatory annotation for classification.

It does not govern.

Therefore:

```text
reason = hazard
```

does not automatically imply:

```text
Delay
```

and:

```text
reason = policy
```

does not automatically imply any Layer 3 conclusion.

---

# 28. Safety Dominance boundary

Every candidate rule must satisfy:

```text
conclusion_type ∈ A_AI(S)
```

But passing Safety Dominance does NOT prove the rule is scientifically
correct.

Separate:

```text
governance admissibility
```

from:

```text
scientific advisory justification
```

A rule may be admissible but unsupported.

---

# 29. Human authority boundary

No concrete rule may conclude:

```text
Approved
Prohibited
MustGo
MustStay
PermissionGranted
PermissionDenied
```

No rule may automatically override a fisher.

Even:

```text
Go
```

remains advisory.

---

# 30. Create a candidate-rule register

Create:

```text
data/journal1-layer3-prototype/rule-candidate-register-batch2.csv
```

At minimum columns:

```text
rule_id
applicable_state
antecedent_summary
antecedent_variables
conclusion_type
payload_summary
governance_admissible
classifier_duplication
evidence_source
evidence_location
evidence_level
adaptation_required
conflict_risk
status
limitation
```

Include rejected candidates as well.

This is important for auditability.

---

# 31. Create an evidence matrix

Create:

```text
data/journal1-layer3-prototype/rule-evidence-matrix-batch2.csv
```

At minimum:

```text
source_id
source_type
citation
study_context
population
vessel_context
environmental_context
supported_relationship
recommendation_implication
direct_or_inferred
transferability_to_Sabah
limitations
candidate_rule_ids
```

Do not claim transferability merely because a study concerns fishermen.

---

# 32. Create recommendation semantics authority

Extend:

```text
publications/active/journal-1/layer3-prototype-specification.md
```

with a new Batch 2 section.

Suggested sections:

```text
16. Batch 2 Scientific Rule-Specification Scope
17. Recommendation Semantics
18. Evidence Hierarchy
19. Candidate Rule Derivation Method
20. SAFE Rule Candidates
21. CAUTION Rule Candidates
22. Rule Interaction and Conflict Analysis
23. Payload Semantics
24. Concrete Rule Register
25. Evidence Gaps
26. OPEN Scientific Decisions
27. Batch 2 Traceability
```

Do not overwrite Batch 1 history.

---

# 33. Concrete RS specification

Only after evidence review, define:

```text
RS_candidate(SAFE)
RS_candidate(CAUTION)
```

using supported or explicitly proposed rules.

Do not call them final executable `RS(S)` unless the evidence status warrants it.

For example:

```text
RS_candidate(SAFE) = {
    R1,
    R2,
    ...
}
```

with each rule carrying a scientific status.

If no rule reaches sufficient support:

```text
RS_candidate(SAFE) remains scientifically under-specified.
```

That is an acceptable scientific result.

---

# 34. Do not force closure of OPEN-L3-1

`OPEN-L3-1` may have one of three outcomes.

### Outcome A — Fully resolved

Evidence supports a defensible concrete rule set for all intended Layer 3
behaviour.

Then:

```text
OPEN-L3-1 CLOSED
```

### Outcome B — Partially resolved

Some rule types are defensible, others remain unsupported.

Example:

```text
Go            supported
Delay         supported
DepartureTime OPEN
Duration      OPEN
```

Then:

```text
OPEN-L3-1 PARTIALLY RESOLVED
```

and create specific successor OPEN items.

### Outcome C — Not resolved

Evidence does not justify concrete advisory mappings.

Then:

```text
OPEN-L3-1 remains OPEN
```

Do not downgrade scientific standards merely to obtain Outcome A.

---

# 35. Potential successor OPEN items

If needed, split `OPEN-L3-1` into bounded items such as:

```text
OPEN-L3-1A — Go advisory semantics
OPEN-L3-1B — Delay advisory semantics
OPEN-L3-1C — DepartureTime advisory derivation
OPEN-L3-1D — Duration advisory derivation
```

Only create these if the evidence genuinely separates the problems.

Do not create unnecessary administrative OPEN items.

---

# 36. OPEN-L3-2

Do not resolve:

```text
OPEN-L3-2 — Rule-condition evaluation failure handling
```

unless concrete rule specification makes a resolution necessary.

This is primarily an executable-engine policy.

It can remain OPEN through Batch 2.

---

# 37. F1–F3 boundary

Do not run F1–F3.

However, for every candidate rule verify structurally:

```text
rule.applicable_state
rule.conclusion_type
```

against:

```text
A_AI(S)
```

This is a specification consistency check.

It is NOT F1/F2/F3 empirical fidelity evidence.

Use wording:

```text
STRUCTURAL CHECK — PASS
```

not:

```text
F1 PASS
```

---

# 38. E5 boundary

Do not perform:

```text
latency benchmark
CPU measurement
memory measurement
energy measurement
throughput measurement
```

Do not set H3.

`OPEN-B1-6` remains OPEN.

---

# 39. Validation boundary

Do not call literature-supported rules:

```text
validated by fishermen
validated in Sabah
validated operationally
```

unless such validation has actually occurred.

Distinguish:

```text
literature-supported rule specification
```

from:

```text
human/domain validation
```

and from:

```text
prototype implementation fidelity
```

---

# 40. Domain transferability

For evidence from outside Sabah, record explicitly:

```text
source domain
target domain
shared characteristics
material differences
transfer assumption
validation requirement
```

Do not treat evidence from:

```text
industrial vessels
offshore fleets
large commercial fisheries
recreational boating
```

as automatically transferable to Sabah Zone A small-scale fishers.

---

# 41. No optimality claims

Do not claim a rule provides:

```text
optimal departure time
optimal duration
best fishing time
maximum safety
minimum risk
```

unless evidence genuinely establishes that optimisation objective.

This architecture is a governed decision-support architecture.

It is not currently an optimisation model.

---

# 42. Evidence artefacts

In:

```text
data/journal1-layer3-prototype/
```

create:

```text
rule-candidate-register-batch2.csv
rule-evidence-matrix-batch2.csv
recommendation-semantics-batch2.csv
rule-conflict-analysis-batch2.csv
scientific-gap-register-batch2.csv
semantic-verification-batch2.json
change-map-batch2.csv
closure-batch2.json
report-batch2.md
```

Update parser/build tooling only as necessary.

Preserve all Batch 1 artefacts.

---

# 43. Required semantic verification

At minimum verify:

```text
recommendation_universe_unchanged
governance_mapping_unchanged
unsafe_ruleset_empty
go_semantics_not_equated_with_permission
delay_semantics_bounded
departure_time_not_derived_from_sunrise_without_evidence
duration_not_derived_from_daylight_window_without_evidence

layer2_thresholds_not_automatically_reused_as_layer3_rules
safe_not_automatically_go
caution_not_automatically_delay
cause_taxonomy_not_used_as_governance_logic

every_candidate_rule_has_provenance
every_supported_rule_has_evidence_location
evidence_level_explicit
adaptation_explicit
unsupported_rules_not_promoted

all_rule_types_within_A_AI
no_UNSAFE_rules
human_authority_unconditional

rule_conflicts_identified
go_delay_conflict_not_silently_resolved
payload_semantics_bounded

F1_F3_not_run
E5_not_run
latency_threshold_not_invented
OPEN_L3_2_preserved
protected_canonical_state_unchanged
```

Each:

```text
PASS
FAIL
OPEN
```

with evidence.

---

# 44. Stop conditions

If a candidate rule requires inventing an antecedent:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 2 OPEN —
ADVISORY ANTECEDENT LACKS SCIENTIFIC AUTHORITY
```

If a recommendation type has no defensible semantics:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 2 OPEN —
RECOMMENDATION SEMANTICS UNDER-SPECIFIED
```

If resolving conflicting advisories requires a new scientific priority:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 2 OPEN —
ADVISORY CONFLICT POLICY REQUIRES SCIENTIFIC DECISION
```

If available evidence cannot justify transfer to the target context:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 2 OPEN —
DOMAIN TRANSFERABILITY REQUIRES VALIDATION
```

If protected state changes:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 2 OPEN —
PROTECTED CANONICAL STATE DRIFT
```

A stop condition may apply to an individual rule family without requiring
the entire batch to be abandoned.

Record partial progress.

---

# 45. Closure criteria

Close Batch 2 only when:

```text
[ ] semantics of Go examined and bounded
[ ] semantics of Delay examined and bounded
[ ] semantics of DepartureTime examined and bounded
[ ] semantics of Duration examined and bounded

[ ] repository-wide evidence search completed
[ ] evidence matrix created
[ ] candidate-rule register created

[ ] every proposed rule has provenance
[ ] every rule has explicit evidence level
[ ] every adaptation is explicit
[ ] classifier duplication checked
[ ] governance admissibility checked

[ ] SAFE rule candidates assessed
[ ] CAUTION rule candidates assessed
[ ] UNSAFE remains empty

[ ] Go/Delay conflict possibility assessed
[ ] multi-rule interaction assessed
[ ] payload semantics bounded

[ ] unsupported rules remain OPEN
[ ] no rule invented merely to fill R
[ ] no Layer 2 threshold automatically promoted to Layer 3 rule

[ ] OPEN-L3-1 outcome explicitly classified:
    CLOSED / PARTIALLY RESOLVED / OPEN

[ ] OPEN-L3-2 preserved unless independently justified
[ ] F1–F3 not run
[ ] E5 not run

[ ] protected canonical state unchanged
[ ] evidence artefacts parse cleanly
```

---

# 46. Required final report

Return:

## Evidence search

What repository areas and sources were inspected.

## Recommendation semantics

For:

```text
Go
Delay
DepartureTime
Duration
```

state the bounded scientific meaning and evidence status.

## Evidence hierarchy

Explain Level A–D classifications used.

## Candidate rules

Provide a concise table:

```text
Rule
State
Antecedent
Conclusion
Evidence level
Status
```

## Rejected rules

Especially document rejected:

```text
SAFE → Go
CAUTION → Delay
Layer-2-threshold → advisory
sunrise → DepartureTime
daylight window → Duration
```

unless evidence unexpectedly supports any of them.

## Rule interactions

Report possible simultaneous conclusions and unresolved conflicts.

## Concrete RS status

Report:

```text
RS_candidate(SAFE)
RS_candidate(CAUTION)
RS(UNSAFE)=∅
```

without pretending unsupported rules are final.

## OPEN-L3-1 outcome

Exactly one:

```text
CLOSED
PARTIALLY RESOLVED
OPEN
```

with justification.

## Remaining OPEN items

List scientific and implementation OPENs separately.

## Files changed

State the scientific effect of each change.

## Protected integrity

Report:

```text
unchanged
changed
verdict
```

---

# 47. Closure lines

If `OPEN-L3-1` is fully resolved:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 2 CLOSED —
CONCRETE ADVISORY RULE SCIENTIFIC SPECIFICATION VERIFIED
```

If partially resolved:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 2 CLOSED WITH BOUNDED OPEN ITEMS —
ADVISORY RULE EVIDENCE AND SEMANTICS PARTIALLY SPECIFIED
```

If evidence remains insufficient for a defensible concrete rule set:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 2 REMAINS OPEN —
CONCRETE ADVISORY RULES REQUIRE ADDITIONAL SCIENTIFIC EVIDENCE
```

Do not select the closure line based on desire to progress.

Select it from the evidence.

---

# Guiding principle

Preserve the distinction:

```text
A_AI(S)
=
what the AI is permitted to recommend
```

versus:

```text
RS(S)
=
what the evidence warrants the AI to recommend
under specific conditions
```

Therefore:

```text
permission
≠ justification
```

and:

```text
classification threshold
≠ advisory rule
```

and:

```text
literature-supported rule
≠ validated human decision support
```

The purpose of Batch 2 is not to fill the rule repository.

The purpose is to determine which rules can be defended scientifically.

If the defensible answer is that some recommendation types must remain
unimplemented, preserve that result.
