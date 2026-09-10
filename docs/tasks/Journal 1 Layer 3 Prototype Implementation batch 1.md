# Task — Journal 1 Layer 3 Prototype Implementation

## Batch 1: Prototype Contract, Rule Representation, and Fidelity Testability

### Goal

Prepare the implementation authority for the Journal 1 Layer 3 prototype before building the full rule engine.

This batch must define:

```text
1. the executable Layer 3 prototype boundary;
2. the concrete representation of RS(SAFE) and RS(CAUTION);
3. the rule object / schema;
4. the decision-episode execution interface;
5. the state-to-rule-set supply interface;
6. the recommendation output representation;
7. the instrumentation required for future F1–F3 fidelity testing;
8. the implementation decisions that can be closed without changing the scientific architecture.
```

This batch is primarily an **implementation-design and contract task**.

Do not yet conduct the full F1–F3 evaluation.
Do not run E5 performance benchmarking.
Do not set a latency acceptance threshold.
Do not claim implementation fidelity PASS.
Do not invent new scientific thresholds, states, recommendation types, or governance policies.

---

# 1. New workstream branch

Create:

```text
feat/journal1-layer3-prototype
```

This is a new workstream.

Do not continue implementation work on:

```text
design/journal1-algorithm-specification
```

That workstream is CLOSED.

---

# 2. Closed upstream authority

Treat the following as CLOSED upstream authority:

```text
publications/active/journal-1/algorithm-specification.md
publications/active/journal-1/evaluation-specification.md
publications/active/journal-1/research-design.md
docs/canonical/appendix-c-formalisation.md
docs/canonical/architecture-illustration.md
docs/canonical/justification-layer3-enforcement.md
```

The Algorithm Specification & Complexity Analysis workstream closed with:

```text
JOURNAL 1 ALGORITHM SPECIFICATION AND COMPLEXITY ANALYSIS CLOSED —
ALGORITHM 3 COMPLEXITY AND AUTHORITY RESIDUE REPAIRED
```

Do not modify the scientific meaning of Algorithms 1–4.

---

# 3. Protected canonical state

Before editing, verify the existing protected canonical state.

At minimum preserve the same 16 protected canonical files used in the preceding workstream.

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

If protected scientific state differs unexpectedly:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 1 OPEN —
PROTECTED CANONICAL STATE DRIFT
```

STOP.

---

# 4. Scientific architecture that implementation must preserve

The executable pipeline remains:

```text
observations
→ ρ_{D,τ}
→ f
→ S
→ G(S), A_AI(S)
→ RS(S)
→ Layer 3 reasoning
→ AI(E)
→ Human Decision
```

Preserve:

```text
F_{D,τ} = f ∘ ρ_{D,τ}
```

Do not replace the operational classifier with:

```text
S = f(E)
```

except where explicitly labelled ideal-form shorthand.

---

# 5. Fixed governance state

Preserve exactly:

```text
S = {SAFE, CAUTION, UNSAFE}
```

Participation:

```text
G(SAFE)    = 1
G(CAUTION) = 1
G(UNSAFE)  = 0
```

Recommendation universe:

```text
R = {Go, Delay, DepartureTime, Duration}
```

Admissible recommendation scopes:

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

Do not add recommendation types or subtypes.

---

# 6. Layer 3 governance invariant

The implementation must preserve:

```text
ConclusionTypes(RS(S)) ⊆ A_AI(S)
```

and:

```text
RS(UNSAFE) = ∅
```

and:

```text
AI(E) ⊆ A_AI(S)
```

subject to the already stated engine-fidelity assumption.

Rule-set restriction remains the primary governance mechanism.

Do not implement:

```text
all rules
→ generate any output
→ filter disallowed recommendations afterwards
```

as the primary safety mechanism.

---

# 7. Batch 1 responsibility

Create an implementation authority document, suggested location:

```text
publications/active/journal-1/layer3-prototype-specification.md
```

The document should define what the prototype will implement, not merely restate the formal architecture.

Suggested structure:

```text
1. Purpose and scope
2. Upstream authority
3. Prototype module boundaries
4. Rule representation
5. Rule-set representation
6. Recommendation representation
7. Decision context representation
8. Rule-set selection and validation
9. Reasoning episode interface
10. State/rule-set consistency contract
11. Fidelity instrumentation
12. Error and configuration handling
13. Human-authority boundary
14. OPEN implementation decisions
15. Batch 1 implementation traceability
```

---

# 8. Rule representation

Define a concrete prototype-level rule representation.

At minimum, each rule should have fields equivalent to:

```text
rule_id
applicable_state
conditions
conclusion_type
conclusion_payload
provenance / source reference
enabled
```

Do not blindly use these exact field names if the repository already has a stronger convention.

The important scientific constraints are:

```text
conclusion_type ∈ R
```

and for any active state S:

```text
conclusion_type ∈ A_AI(S)
```

for every rule in `RS(S)`.

---

# 9. Do not invent concrete scientific rule contents yet unless authoritative

This is load-bearing.

OPEN-B1-4 previously recorded:

```text
Layer 3 prototype / concrete rule contents
```

Before populating concrete rules, inspect the existing research design, manuscript, architecture, and any existing rule artefacts.

If authoritative rule antecedents and conclusions already exist, reuse them.

If they do not exist, do NOT invent rules such as:

```text
IF wave < 1.0 AND rain < 10 THEN Go
```

merely because the thresholds exist in Layer 2.

Layer 2 safety thresholds do not automatically define Layer 3 advisory rules.

If no authoritative concrete rule set exists, record:

```text
OPEN-L3-1 — Concrete Layer 3 advisory rule content requires scientific specification
```

and continue designing the engine and interfaces without fabricating rule semantics.

This OPEN may block later full prototype completion but does not block Batch 1 contract design.

---

# 10. Rule-set representation

Define concrete prototype representations for:

```text
RS(SAFE)
RS(CAUTION)
RS(UNSAFE)
```

Required invariant:

```text
RS(UNSAFE) = ∅
```

SAFE and CAUTION may be represented as:

```text
state-indexed rule collections
```

but do not silently choose an implementation that changes Algorithm 3 semantics.

The currently specified Algorithm 3 performs candidate validation before supply.

Preserve that behaviour unless a separate implementation decision explicitly documents a different realisation and proves it preserves the contract.

---

# 11. Algorithm 3 implementation fidelity

The prototype implementation of Algorithm 3 must preserve:

```text
RS_candidate ← candidate(repository, S)

verify:
ConclusionTypes(RS_candidate) ⊆ A_AI(S)

if invalid:
    refuse supply
    no reasoning
    S unchanged
```

Do not map invalid repository configuration to environmental `UNSAFE`.

Do not invent a fourth state.

---

# 12. OPEN-B3-1 — invalid repository runtime handling

Batch 3 left this OPEN:

```text
OPEN-B3-1 — Invalid rule-repository runtime handling
```

Batch 1 of the prototype may now choose an implementation behaviour if a bounded engineering choice is sufficient.

Candidate behaviours might include:

```text
return configuration error
log structured failure
disable Layer 3 for the episode
surface configuration failure to caller
```

But do not choose behaviour that:

```text
changes S
creates an advisory
silently removes invalid rules and continues
```

If a choice is made, document clearly:

```text
this closes implementation handling only;
it does not alter the scientific state model.
```

If no choice is needed yet, keep OPEN-B3-1 OPEN.

---

# 13. State/rule-set consistency

The prototype must enforce the invariant:

```text
one reasoning episode
→ one governing S
→ corresponding G(S), A_AI(S)
→ corresponding RS(S)
```

No reasoning episode may use stale:

```text
RS(S_old)
```

under:

```text
S_new
```

However, OPEN-B1-8 remains:

```text
state/rule-set consistency enforcement mechanism
```

Do not choose atomic swap / lock / transaction merely to close it unless the actual runtime architecture requires a choice.

Batch 1 may define the software interface such that consistency can later be enforced without choosing a concurrency primitive.

---

# 14. Decision episode

OPEN-B3-3 remains:

```text
Decision-episode implementation boundary
```

Define the minimum executable contract:

```text
ReasoningEpisode {
    state
    governance
    rule_set
    context
}
```

or equivalent.

The key invariant is:

```text
all four belong to the same episode
```

Do not invent:

```text
episode duration
polling interval
refresh frequency
```

unless implementation genuinely requires it.

---

# 15. Decision context

Define the Layer 3 context representation without silently redefining canonical `E`.

Distinguish if necessary:

```text
canonical resolved environmental state
```

from:

```text
prototype reasoning context
```

If Layer 3 requires additional advisory features not contained in canonical `E`, identify them explicitly as implementation inputs rather than silently extending `E`.

Do not introduce new scientific variables without authority.

---

# 16. Recommendation output representation

Define a concrete output type for generated advisory instances.

At minimum distinguish:

```text
recommendation instance
```

from:

```text
recommendation type ∈ R
```

Possible shape:

```text
Advisory {
    type
    payload
    rule_id
    explanation
}
```

but use repository conventions if stronger.

Required invariant:

```text
type(advisory) ∈ A_AI(S)
```

for every emitted advisory.

---

# 17. UNSAFE implementation path

Preserve exactly:

```text
S = UNSAFE
→ G = 0
→ A_AI = ∅
→ no rule set supplied
→ no Layer 3 reasoning
→ AI(E) = ∅
```

Do not generate:

```text
Do Not Go
Cancel
Return Home
Stay Ashore
```

as advisory outputs.

State reporting is outside `AI(E)`.

---

# 18. Human authority

The prototype must not introduce:

```text
automatic approval
automatic prohibition
automatic override
automatic departure decision
```

Human Decision remains unconditional.

A `Go` advisory is not an approval.

An empty advisory set is not a prohibition.

---

# 19. Rule engine strategy — OPEN-B3-2

Do not prematurely select:

```text
RETE
forward chaining
backward chaining
agenda priority
salience
first-match
all-match
```

unless the prototype implementation genuinely requires a choice now.

Prefer the simplest deterministic engine sufficient to test the governance contract.

But if a specific engine strategy is chosen, document:

```text
why it was chosen
what scientific claims it does NOT affect
what complexity assumption it closes
```

Do not claim the strategy itself provides Safety Dominance.

---

# 20. Solar lookup — OPEN-B4-1

This workstream is Layer 3.

Do not opportunistically close:

```text
OPEN-B4-1 — solar lookup representation
```

unless Layer 3 implementation actually needs to modify Algorithm 1 infrastructure.

Prefer to leave it untouched.

---

# 21. Fidelity instrumentation

Design instrumentation now so F1–F3 can later be measured.

At minimum record per reasoning episode:

```text
episode_id
S
G(S)
A_AI(S)
active_rule_ids
active_rule_conclusion_types
fired_rule_ids
generated_advisory_types
configuration_failure
```

For state transitions, record enough to test:

```text
S_old
S_new
RS used in new episode
```

Do not fabricate empirical results.

Instrumentation design is not F1/F2/F3 PASS.

---

# 22. F1–F3 future obligations

Read the active evaluation specification and map the prototype instrumentation exactly to F1–F3.

Do not redefine the metrics.

Batch 1 should produce a table such as:

```text
Fidelity criterion
Required runtime field
Required assertion
Prototype module responsible
Status
```

Use:

```text
DESIGNED
NOT YET TESTED
```

not PASS.

---

# 23. Required prototype modules

Propose the minimum module structure.

Conceptually:

```text
governance/
  rule.py
  rule_repository.py
  rule_set_provider.py
  reasoning_engine.py
  advisory.py
  reasoning_episode.py
  fidelity_trace.py
```

or repository-language equivalent.

Do not force Python if the project uses another implementation language.

Inspect existing repository conventions first.

---

# 24. Interface contracts

Define function/module signatures for at least:

```text
select_rule_set(...)
validate_rule_set(...)
reason(...)
execute_episode(...)
emit_fidelity_trace(...)
```

Use repository-native naming where appropriate.

Each contract must state:

```text
inputs
outputs
preconditions
postconditions
failure behaviour
scientific invariant preserved
```

---

# 25. Testing plan — specification only

Design unit/contract tests for later implementation.

At minimum include:

```text
SAFE rule set contains only FULL recommendation types
CAUTION rule set excludes DepartureTime and Duration
UNSAFE has no rule set
invalid rule repository refuses supply
engine cannot fire rule outside active RS
empty rule firing result is valid
multiple allowed recommendations remain valid
SAFE→CAUTION uses new restricted RS
CAUTION→UNSAFE disables reasoning
UNSAFE→SAFE enables SAFE rule set
human authority semantics not encoded as automated decision
```

Do not report tests PASS unless they are actually implemented and run in this batch.

---

# 26. Evidence artefacts

Create:

```text
data/journal1-layer3-prototype/
```

Suggested artefacts:

```text
prototype-contract-batch1.csv
rule-schema-batch1.json
module-map-batch1.csv
fidelity-instrumentation-batch1.csv
test-plan-batch1.csv
open-decisions-batch1.csv
semantic-verification-batch1.json
change-map-batch1.csv
closure-batch1.json
report-batch1.md
```

Do not reuse the algorithm-specification evidence directory for new prototype evidence.

---

# 27. Required semantic checks

At minimum:

```text
upstream_algorithm_contract_unchanged
recommendation_universe_exact
governance_mapping_exact
unsafe_has_no_advisory
RS_before_reasoning_preserved
no_posthoc_filter_substitution
rule_schema_conclusion_type_bounded
concrete_rules_not_invented_without_authority
invalid_repository_does_not_modify_S
state_ruleset_consistency_invariant_preserved
concurrency_primitive_not_invented
decision_episode_boundary_bounded
engine_strategy_not_overclaimed
human_authority_unconditional
fidelity_instrumentation_defined
F1_F3_not_reported_as_results
E5_not_run
latency_threshold_not_invented
canonical_state_unchanged
```

Each:

```text
PASS
FAIL
OPEN
```

with evidence.

---

# 28. OPEN decision handling

Carry forward:

```text
OPEN-B1-1
OPEN-B1-2
OPEN-B1-3
OPEN-B1-4
OPEN-B1-5
OPEN-B1-6
OPEN-B1-7
OPEN-B1-8

OPEN-B3-1
OPEN-B3-2
OPEN-B3-3

OPEN-B4-1
```

Some may now become implementation-relevant.

Do not close any unless this batch contains enough evidence and the closure does not change scientific meaning.

If concrete Layer 3 rule content is absent, explicitly split:

```text
engine/interface implementation can proceed
```

from:

```text
scientific rule-content specification remains OPEN
```

---

# 29. Stop conditions

If concrete rule contents are required but no authoritative source exists:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 1 OPEN —
CONCRETE RULE CONTENT REQUIRES SCIENTIFIC SPECIFICATION
```

Do not invent them.

If implementation requires a new recommendation type:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 1 OPEN —
NEW RECOMMENDATION TYPE REQUIRED
```

If implementation requires changing `A_AI(S)`:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 1 OPEN —
GOVERNANCE CONTRACT CONFLICT
```

If implementation requires changing Algorithm 3 semantics:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 1 OPEN —
RULE-SET SUPPLY CONTRACT CONFLICT
```

If protected canonical state changes:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 1 OPEN —
PROTECTED CANONICAL STATE DRIFT
```

---

# 30. Closure criteria

Close Batch 1 only when:

```text
[ ] prototype authority document created
[ ] upstream algorithm contract preserved
[ ] module boundaries defined
[ ] rule representation defined
[ ] rule-set representation defined
[ ] recommendation representation defined
[ ] decision-episode interface defined
[ ] Algorithm 3 implementation contract defined
[ ] invalid rule-set behaviour bounded
[ ] state/rule-set consistency invariant preserved
[ ] human authority preserved

[ ] concrete rules reused only if authoritative
[ ] otherwise concrete-rule requirement remains explicit OPEN
[ ] engine strategy bounded
[ ] no scientific thresholds invented

[ ] F1–F3 instrumentation defined
[ ] F1–F3 still NOT YET TESTED
[ ] E5 not run
[ ] H3 threshold remains OPEN

[ ] evidence artefacts complete
[ ] protected canonical state unchanged
```

---

# 31. Required report

Return:

## Prototype boundary

What Layer 3 prototype will and will not implement.

## Module design

Concrete module/file structure.

## Rule representation

Schema and invariants.

## Rule-set representation

SAFE / CAUTION / UNSAFE handling.

## Reasoning episode

Inputs, outputs, state consistency.

## Recommendation representation

How advisory instances map to `R`.

## Engine strategy

Chosen or OPEN, with bounded justification.

## Concrete rule-content status

Authoritative / absent / OPEN.

## Fidelity instrumentation

How future F1–F3 will be measured.

## OPEN decisions

Existing and newly introduced.

## Files changed

Scientific effect of each file.

## Protected integrity

Report:

```text
unchanged
changed
verdict
```

---

# 32. Closure line

If all Batch 1 contract criteria PASS:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 1 CLOSED —
PROTOTYPE CONTRACT AND FIDELITY-INSTRUMENTATION DESIGN VERIFIED
```

If concrete rule content blocks closure but the engine contract is otherwise complete:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 1 OPEN —
CONCRETE RULE CONTENT REQUIRES SCIENTIFIC SPECIFICATION
```

Otherwise:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 1 REMAINS OPEN —
IMPLEMENTATION CONTRACT GAP REMAINS
```

---

# Guiding principle

The previous workstream established:

```text
what the architecture means
→ how the four algorithms behave
→ their bounded computational complexity
```

This workstream now establishes:

```text
how those contracts become executable software
```

without turning engineering choices into new scientific claims.

The order remains:

```text
Prototype Contract
→ Prototype Implementation
→ F1–F3 Fidelity Testing
→ E5 Performance Measurement
```

Do not skip directly to benchmarking or empirical PASS/FAIL claims.
