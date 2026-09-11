# Journal 1 Layer 3 Prototype

## Batch 4B-2 — Governed Component-State Interface & Rule Implementation

### Task Type

Bounded implementation and engineering verification.

This task implements the canonical/specification authority established by Batch 4B-1.

This is NOT a scientific redesign task.

This task must not invent new scientific rules, thresholds, governance semantics, or advisory mappings.

---

# 1. Branch

Create:

```text
feat/journal1-layer3-component-state-rules
```

Before modifying anything record:

```text
current branch
HEAD commit
working-tree status
Batch 4B-1 closure commit/hash
```

The working tree must contain the accepted Batch 4B-1 canonical/specification amendments.

If Batch 4B-1 is not committed, STOP:

```text
BATCH4B1_CLOSURE_NOT_COMMITTED
```

Do not mix uncommitted Batch 4B-1 documentation changes with Batch 4B-2 implementation.

---

# 2. Gate Authority

Independent review has accepted Batch 4B-1.

Treat:

```text
BATCH4B2_IMPLEMENTATION_READY = true
```

as the implementation gate for this task.

The authorised implementation scope is ONLY:

```text
ComponentStateTrace implementation

DecisionContext extension

DECISION_CONTEXT_SCHEMA extension

interface structural validation

episode/state-trace consistency enforcement

R-CAUTION-002 implementation

R-CAUTION-003 implementation

R-CAUTION-004 implementation

engineering tests
```

Not authorised:

```text
R-SAFE-001
CAUTION → Go
R-CAUTION-001 migration
DepartureTime
Duration
F1–F3
E5
new thresholds
new scientific evidence
new advisory mappings
Layer 2 classifier duplication
```

---

# 3. Authorities to Read First

Read:

```text
docs/canonical/appendix-c-formalisation.md
docs/canonical/architecture-illustration.md

publications/active/journal-1/layer3-prototype-specification.md
publications/active/journal-1/algorithm-specification.md
publications/active/journal-1/evaluation-specification.md

data/journal1-layer3-prototype/
  batch4a-executable-rule-authority/
  batch4b1-interface-amendment/
```

In particular read:

```text
batch4b1-interface-amendment/
  canonical-change-record.json
  component-state-interface-contract.md
  interface-impact-matrix.csv
  verification.json
  integrity.json
  report.md
```

Then inspect the existing implementation:

```text
governance/rule.py
governance/advisory.py
governance/fidelity_trace.py
governance/rule_repository.py
governance/rule_set_provider.py
governance/reasoning_engine.py
governance/reasoning_episode.py
governance/canonical_rules.py

tests/test_governance_engine.py
```

Do not start coding before reconciling the current code with the Batch 4B-1 interface contract.

---

# 4. Frozen Architecture

Preserve:

```text
Layer 1
observations

↓

Layer 2
ρ_{D,τ}
component classifiers g_i
S = F_{D,τ}(obs,v)

↓

S + ComponentStateTrace

↓

Layer 3
G(S)
A_AI(S)
RS(S)
reasoning
AI(E)
```

Layer 3 MUST NOT recompute:

```text
g_w
g_r
g_m
g_o
g_t
```

No Layer 2 threshold logic may be copied into Layer 3.

---

# 5. Frozen Governance

Preserve exactly:

```text
G(SAFE) = 1
G(CAUTION) = 1
G(UNSAFE) = 0
```

and:

```text
A_AI(SAFE)
= {Go, Delay, DepartureTime, Duration}

A_AI(CAUTION)
= {Go, Delay}

A_AI(UNSAFE)
= ∅
```

`A_AI(S)` defines admissible conclusion types.

It does NOT mean that a rule for every admissible type must exist.

Safety Dominance remains:

```text
AI(E) ⊆ A_AI(S)
```

Human authority remains unconditional.

---

# 6. ComponentStateTrace Implementation

Implement the Batch 4B-1 interface.

Required fields:

```text
component_w_state
component_r_state
component_m_state
component_o_state
component_t_state
```

These are already-computed Layer 2 component classifications.

They are NOT raw environmental measurements.

They are NOT recomputed by Layer 3.

They are read-only episode inputs.

---

# 7. Component-State Domains

Implement the accepted interface domains.

For:

```text
component_w_state
component_r_state
component_m_state
component_o_state
```

structural domain:

```text
SAFE
CAUTION
EXCLUDED
```

For:

```text
component_t_state
```

structural domain:

```text
SAFE
EXCLUDED
```

But preserve the runtime restriction:

```text
t ∉ D
```

therefore:

```text
component_t_state = EXCLUDED
```

is structurally representable only if required by the accepted interface type, but unreachable under the current canonical runtime configuration.

Do not invent a CAUTION value for g_t.

---

# 8. EXCLUDED Semantics

Preserve:

```text
EXCLUDED ≠ SAFE
```

An excluded component is not an observed SAFE component.

It may be pinned SAFE for Layer 2 aggregation, but Layer 3 receives:

```text
EXCLUDED
```

as its provenance-aware interface status.

For current retrospective replay:

```text
D = {m}
```

therefore:

```text
component_m_state = EXCLUDED
```

is valid.

Do not translate it to:

```text
SAFE
none
no hazard
no warning
```

Do not make `EXCLUDED` satisfy a predicate requiring `SAFE`.

---

# 9. UNSAFE / Fault Boundary

Do NOT add UNSAFE or FAULTED as normal Layer 3 component-state values.

Preserve:

```text
required nonexcluded fault
→ ⊥
→ g_i(⊥)=UNSAFE
→ S=UNSAFE
→ G(UNSAFE)=0
→ Layer 3 not invoked
```

The component classifiers can still return UNSAFE in Layer 2.

It is merely unreachable at the Layer 3 reasoning boundary.

Do not redefine g_i.

---

# 10. DecisionContext Extension

Extend `DecisionContext` with the ComponentStateTrace fields.

Prefer the smallest implementation consistent with the accepted specification.

Do not introduce a second environmental model.

The component states must be associated with the same episode as:

```text
state
episode_id
```

Do not allow cross-episode reuse.

---

# 11. DECISION_CONTEXT_SCHEMA Extension

Update:

```text
governance/rule_set_provider.py
```

so Algorithm 3 structural validation recognises the new component-state variables.

The schema must encode appropriate categorical domains.

At minimum:

```text
component_w_state
component_r_state
component_m_state
component_o_state
component_t_state
```

The schema must support future predicates:

```text
component_o_state == "CAUTION"
component_r_state == "CAUTION"
component_w_state == "CAUTION"
```

Do not add raw threshold predicates.

---

# 12. Preserve Algorithm 3 Validation Boundary

Existing Algorithm 3 validation semantics remain authoritative.

Preserve ordering:

```text
containment
→ V1
→ V2
→ V3
→ V4
```

Frozen classes:

```text
V1 unknown variable
→ F-T-11

V2 type mismatch
→ F-T-04

V3 invalid operator
→ F-T-05

V4 categorical value outside domain
→ F-T-06
```

Component-state predicates must pass through the same structural validation.

Do not create a special bypass for canonical rules.

---

# 13. Mandatory V3 Verification

Explicitly verify that an invalid operator on a numeric OR categorical predicate is rejected during Algorithm 3 structural validation as:

```text
F-T-05
```

Do not allow an invalid operator to survive validation and become a runtime:

```text
INTERNAL_ERROR
```

If current implementation fails this requirement, repair the validator within the narrow Algorithm 3 contract.

Record the repair explicitly.

Do not expand scope beyond operator validation.

---

# 14. Component-State Invalid Values

Values outside the declared categorical domain must fail structural validation.

Examples:

```text
component_w_state == "DANGER"
component_r_state == "UNKNOWN"
component_o_state == "UNSAFE"
```

must not silently become normal FALSE predicates if those values are outside the Layer 3 schema.

They must be caught under the existing categorical-domain validation contract:

```text
V4
→ F-T-06
```

Do not invent a new failure code.

---

# 15. Episode Consistency Invariant

Implement or enforce:

```text
episode_id(S) = episode_id(ComponentStateTrace)
```

The implementation must prevent Layer 3 reasoning from using:

```text
S from episode A
+
ComponentStateTrace from episode B
```

Use the smallest implementation mechanism consistent with the existing architecture.

Do not invent cryptographic identity or persistence infrastructure.

If the current `DecisionContext` object already guarantees same-object episode construction, demonstrate that guarantee with tests rather than adding unnecessary machinery.

---

# 16. S / Component-State Consistency Invariant

Before reasoning, enforce or verify:

```text
S = SAFE
→ all active/non-EXCLUDED component states = SAFE

S = CAUTION
→ at least one active component state = CAUTION
→ no component state UNSAFE

S = UNSAFE
→ Layer 3 gate-off before engine
```

`EXCLUDED` must be handled correctly.

Example valid:

```text
S = SAFE

w = SAFE
r = SAFE
m = EXCLUDED
o = SAFE
t = SAFE
```

Example valid:

```text
S = CAUTION

w = SAFE
r = CAUTION
m = EXCLUDED
o = SAFE
t = SAFE
```

Example invalid:

```text
S = SAFE
r = CAUTION
```

Example invalid:

```text
S = CAUTION
w = SAFE
r = SAFE
m = EXCLUDED
o = SAFE
t = SAFE
```

because no active component explains CAUTION.

---

# 17. Consistency Failure Classification

Batch 4B-1 established that an inconsistent S/ComponentStateTrace pair is:

```text
configuration/interface fidelity failure
```

Do NOT silently correct the trace.

Do NOT recompute S.

Do NOT change component states.

Do NOT continue normal reasoning.

Use the existing configuration-failure mechanism where possible.

Expected semantic outcome:

```text
configuration_failure = true
AI(E) = ∅
no advisory supplied
S unchanged
```

Do not classify this as predicate `ERROR` unless the failure genuinely occurs during predicate evaluation rather than interface consistency validation.

Keep:

```text
configuration_failure
```

distinct from:

```text
evaluation_failure
```

---

# 18. Algorithm 4 / Predicate Failure Semantics

Preserve the frozen three-valued model:

```text
TRUE
FALSE
ERROR
```

Rule fires iff all predicates are TRUE.

FALSE:

```text
successfully evaluated but unsatisfied
```

ERROR:

```text
antecedent could not be established
```

Any ERROR in an episode:

```text
episode-level refusal
AI(E) = ∅
evaluation_failure = true
```

No partial advisory.

Do not weaken this because new component predicates are simple categorical comparisons.

---

# 19. R-CAUTION-001

Preserve exactly.

Current predicate remains:

```text
resolved_m == "advisory"
```

Do NOT migrate it to:

```text
component_m_state == "CAUTION"
```

Batch 4B-1 classifies that only as:

```text
FUTURE_CONSISTENCY_CONSIDERATION
```

No change in this batch.

---

# 20. Implement R-CAUTION-002

Implement the already-authorised candidate:

```text
rule_id:
R-CAUTION-002

applicable_state:
CAUTION

predicate:
component_o_state == "CAUTION"

conclusion_type:
Delay
```

Preserve the Batch 2 scientific provenance and evidence grading exactly.

Do not strengthen its evidence level.

Do not change wording from conditional support to direct normative authority if that was not previously established.

Do not add wave thresholds.

---

# 21. Implement R-CAUTION-003

Implement:

```text
rule_id:
R-CAUTION-003

applicable_state:
CAUTION

predicate:
component_r_state == "CAUTION"

conclusion_type:
Delay
```

Preserve exact Batch 2 provenance.

Do not add:

```text
10 mm/h
20 mm/h
κ
WMO codes
```

to the Layer 3 rule.

Those remain Layer 2 semantics.

---

# 22. Implement R-CAUTION-004

Implement:

```text
rule_id:
R-CAUTION-004

applicable_state:
CAUTION

predicate:
component_w_state == "CAUTION"

conclusion_type:
Delay
```

Preserve exact Batch 2 provenance.

Do not add:

```text
21.6 kn
27.0 kn
40 km/h
50 km/h
```

to Layer 3 rule logic.

---

# 23. Duplicate Advisory Semantics

Multiple CAUTION rules may fire simultaneously and all conclude:

```text
Delay
```

Do not silently assume the desired output representation.

Inspect existing advisory aggregation semantics.

Determine whether:

```text
R-CAUTION-002
R-CAUTION-003
R-CAUTION-004
```

firing simultaneously should produce:

```text
one Delay advisory with multiple provenance entries
```

or:

```text
multiple Delay advisory records
```

Use existing architecture/Batch 2/Batch 3 authority.

If no authority exists, preserve current engine behaviour and explicitly document it as an implementation representation rather than inventing a new scientific semantic.

Do not deduplicate in a way that destroys rule-level provenance.

---

# 24. R-SAFE-001 Hard Protection

Do not implement:

```text
R-SAFE-001
```

Do not add any equivalent:

```text
all components SAFE → Go
S == SAFE → Go
```

Do not create an indirect version using ComponentStateTrace.

Frozen:

```text
R-SAFE-001
= STATE_RESTATEMENT
= DEFERRED
```

---

# 25. OPEN-L3-3 Protection

Do not create:

```text
CAUTION → Go
```

Preserve:

```text
S=CAUTION ∧ Go∈AI(E)
→ Present(Go, caution_qualifier)
```

as presentation semantics only.

GAP-03 remains OPEN.

---

# 26. DepartureTime / Duration

Do not implement either.

Preserve:

```text
OPEN-L3-1C
OPEN-L3-1D
```

Their presence in:

```text
A_AI(SAFE)
```

does not imply rule existence.

---

# 27. Cause Taxonomy

Preserve:

```text
reasons : Q → P({fault,hazard,policy})
```

as explanatory only.

Do not use:

```text
reason == hazard
reason == policy
reason == fault
```

as predicates for R-CAUTION-002/003/004.

ComponentStateTrace is distinct from `reasons`.

---

# 28. Human Authority

No implementation may encode:

```text
Delay = prohibition
Go = approval
AI(E)=∅ = prohibition
```

Delay remains an advisory conclusion.

Human decision authority remains unconditional.

---

# 29. Mandatory Engineering Tests

Extend the existing test suite.

At minimum test the following categories.

## A. Interface construction

```text
ComponentStateTrace fields accepted
valid categorical values accepted
read-only/episode-local behaviour preserved
```

## B. EXCLUDED

```text
EXCLUDED accepted where schema permits
EXCLUDED != SAFE
m=EXCLUDED works with SAFE episode
m=EXCLUDED works with CAUTION episode driven by another component
t=EXCLUDED rejected at runtime if current implementation enforces t∉D
```

If t runtime reachability is not enforceable at this layer without duplicating Layer 2 configuration, document and test the strongest justified boundary instead of inventing new authority.

## C. S/trace consistency

Test:

```text
SAFE + all active SAFE
→ valid

SAFE + one CAUTION
→ configuration failure

CAUTION + one CAUTION
→ valid

CAUTION + multiple CAUTION
→ valid

CAUTION + all active SAFE
→ configuration failure

UNSAFE
→ gate-off before engine
```

## D. Rule activation

Test independently:

```text
R-CAUTION-002 fires on o_state=CAUTION

R-CAUTION-003 fires on r_state=CAUTION

R-CAUTION-004 fires on w_state=CAUTION
```

and does not fire when corresponding component is SAFE/EXCLUDED.

## E. Concurrent activation

Test:

```text
o_state=CAUTION
r_state=CAUTION
w_state=CAUTION
```

within one CAUTION episode.

Verify deterministic output and provenance preservation.

## F. Structural validation

Test:

```text
unknown component variable
→ F-T-11

type mismatch
→ F-T-04

invalid operator
→ F-T-05

categorical outside domain
→ F-T-06
```

Explicitly include:

```text
component_w_state == "DANGER"
component_r_state == "UNSAFE"
```

as invalid-domain cases.

## G. Predicate failure

Preserve tests for:

```text
TRUE
FALSE
ERROR
```

and:

```text
any ERROR
→ AI(E)=∅
→ evaluation_failure=true
→ no partial advisory
```

## H. Governance

Verify:

```text
UNSAFE → no reasoning
UNSAFE → AI(E)=∅

SAFE cannot receive CAUTION rule set

CAUTION receives only CAUTION rule set

generated conclusion types ⊆ A_AI(S)
```

## I. Protected rules

Assert:

```text
R-SAFE-001 absent
CAUTION→Go absent
DepartureTime rule absent
Duration rule absent
R-CAUTION-001 unchanged
```

---

# 30. Existing Tests

All existing Batch 3 tests must continue to pass unless a test fixture requires the newly mandatory interface fields.

If fixture adaptation is required:

```text
update fixture construction only
```

Do not weaken assertions merely to accommodate the new implementation.

Record:

```text
existing tests before
existing tests after
new tests added
total tests
PASS
FAIL
```

---

# 31. Scientific Evaluations Prohibited

Do NOT run:

```text
F1
F2
F3
```

Do NOT run:

```text
E5
```

Engineering unit/integration tests are authorised.

Do not compute scientific replay results in this task.

Do not produce empirical claims from engineering tests.

---

# 32. Performance Claims Prohibited

Do not claim:

```text
efficient
fast
real-time
low latency
mobile suitable
deployment ready
```

from engineering tests.

E5 remains the authority for latency/performance.

No X ms threshold may be invented.

---

# 33. Files Expected to Change

Expected implementation changes:

```text
governance/reasoning_episode.py
governance/rule_set_provider.py
governance/canonical_rules.py
tests/test_governance_engine.py
```

Additional governance implementation files may be modified only if strictly required to enforce the accepted interface/failure contract.

If modifying another implementation file, explain why.

Do not modify:

```text
docs/canonical/appendix-c-formalisation.md
docs/canonical/architecture-illustration.md

publications/active/journal-1/
  layer3-prototype-specification.md
  algorithm-specification.md
  evaluation-specification.md
```

Batch 4B-2 implements existing authority; it does not rewrite it.

---

# 34. Evidence Directory

Create:

```text
data/journal1-layer3-prototype/
  batch4b2-component-state-rules/
```

Required artefacts:

```text
implementation-manifest.json
rule-manifest.json
test-results.json
contract-verification.json
integrity.json
report.md
```

---

# 35. implementation-manifest.json

Record:

```text
task
branch
HEAD_before

files_modified
files_created

ComponentStateTrace_implemented
DecisionContext_extended
schema_extended
consistency_validation_implemented

R_CAUTION_001_changed
R_CAUTION_002_implemented
R_CAUTION_003_implemented
R_CAUTION_004_implemented
R_SAFE_001_implemented

Layer2_classifier_logic_added
new_threshold_added

F1_F3_run
E5_run
```

Expected:

```text
R_CAUTION_001_changed = false
R_CAUTION_002_implemented = true
R_CAUTION_003_implemented = true
R_CAUTION_004_implemented = true
R_SAFE_001_implemented = false

Layer2_classifier_logic_added = false
new_threshold_added = false

F1_F3_run = false
E5_run = false
```

Do not force expected values if implementation evidence contradicts them.

---

# 36. rule-manifest.json

For every executable rule after Batch 4B-2 record:

```text
rule_id
applicable_state
conditions
conclusion_type
conclusion_payload
provenance
scientific_support_class
implementation_status
```

Include:

```text
R-CAUTION-001
R-CAUTION-002
R-CAUTION-003
R-CAUTION-004
```

Also record deferred:

```text
R-SAFE-001
```

separately.

Do not silently change Batch 2 provenance.

---

# 37. test-results.json

Record:

```text
test_command
test_framework

existing_test_count
new_test_count
total_test_count

PASS
FAIL
SKIPPED

test_categories

failure_details
```

No failing engineering test may be hidden.

---

# 38. contract-verification.json

Verify at minimum:

```text
Batch4B1_authority_preserved

ComponentStateTrace_implemented

DecisionContext_extended

schema_extended

component_domains_correct

EXCLUDED_distinct_from_SAFE

fault_semantics_preserved

UNSAFE_gateoff_preserved

episode_consistency_enforced

state_trace_consistency_enforced

configuration_failure_distinct_from_evaluation_failure

no_layer2_classifier_reimplementation

no_new_thresholds

Algorithm3_containment_preserved

V1_FT11_preserved

V2_FT04_preserved

V3_FT05_preserved

V4_FT06_preserved

invalid_numeric_operator_rejected_structurally

invalid_categorical_operator_rejected_structurally

invalid_component_state_rejected_structurally

Algorithm4_three_valued_preserved

ERROR_episode_refusal_preserved

no_partial_advisory_on_ERROR

R_CAUTION_001_unchanged

R_CAUTION_002_correct

R_CAUTION_003_correct

R_CAUTION_004_correct

concurrent_CAUTION_rules_supported

rule_provenance_preserved

R_SAFE_001_absent

CAUTION_Go_absent

DepartureTime_absent

Duration_absent

OPEN_L3_3_preserved

OPEN_L3_1C_preserved

OPEN_L3_1D_preserved

GAP_03_preserved

Safety_Dominance_preserved

human_authority_preserved

canonical_docs_unchanged

scientific_specs_unchanged

all_engineering_tests_pass

F1_F3_not_run

E5_not_run
```

Use:

```text
PASS
FAIL
OPEN
```

Protection checks should be PASS when correctly preserved.

---

# 39. Integrity Record

Create:

```text
integrity.json
```

Record before/after SHA-256 for at least:

```text
docs/canonical/appendix-c-formalisation.md
docs/canonical/architecture-illustration.md

publications/active/journal-1/layer3-prototype-specification.md
publications/active/journal-1/algorithm-specification.md
publications/active/journal-1/evaluation-specification.md

governance/rule.py
governance/advisory.py
governance/fidelity_trace.py
governance/rule_repository.py
governance/rule_set_provider.py
governance/reasoning_engine.py
governance/reasoning_episode.py
governance/canonical_rules.py
```

Expected authority documents:

```text
UNCHANGED
```

Implementation files may change only where justified.

---

# 40. Stop Conditions

STOP rather than expanding scope if implementation requires:

```text
changing E

changing ρ_{D,τ}

changing f

changing F_{D,τ}

changing any g_i threshold or semantics

changing G(S)

changing A_AI(S)

changing Safety Dominance

changing human authority

modifying Appendix C

modifying canonical architecture

inventing new scientific rule authority

implementing R-SAFE-001

creating CAUTION→Go

implementing DepartureTime

implementing Duration

using reasons as decision authority

running F1–F3

running E5
```

Report the exact blocker.

---

# 41. Success Criteria

Batch 4B-2 closes only if:

```text
ComponentStateTrace implemented
AND
DecisionContext/schema extended
AND
interface consistency contract enforced
AND
R-CAUTION-002 implemented exactly
AND
R-CAUTION-003 implemented exactly
AND
R-CAUTION-004 implemented exactly
AND
R-CAUTION-001 unchanged
AND
R-SAFE-001 absent
AND
no CAUTION→Go rule
AND
no Layer 2 classifier duplication
AND
all engineering tests PASS
AND
canonical/specification authority unchanged
AND
F1–F3 not run
AND
E5 not run
```

---

# 42. F1–F3 Readiness Gate

At completion classify:

```text
F1_F3_IMPLEMENTATION_READY = true | false
```

Set TRUE only if:

```text
Batch 4B-2 implementation contract passes
all engineering tests pass
no unresolved configuration/interface contradiction
rule provenance is intact
no scientific scope expansion occurred
```

This does NOT authorise running F1–F3 automatically.

It only means the implementation is ready for independent review.

Independent review must occur before scientific fidelity evaluation begins.

---

# 43. Closure Line

Only if all Batch 4B-2 success criteria pass:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 4B-2 CLOSED —
COMPONENT-STATE INTERFACE AND AUTHORISED CAUTION RULES IMPLEMENTED
```

Otherwise:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 4B-2 REMAINS OPEN —
<EXACT BLOCKER>
```

---

# 44. Required Final Response

Return exactly these substantive items:

1. Verdict
2. Branch
3. HEAD before / HEAD after
4. Batch 4B-1 authority inherited
5. Files modified
6. ComponentStateTrace implementation
7. DecisionContext changes
8. schema changes
9. episode-consistency mechanism
10. S/component consistency mechanism
11. configuration-failure behaviour
12. V1/V2/V3/V4 result
13. R-CAUTION-001 status
14. R-CAUTION-002 implementation
15. R-CAUTION-003 implementation
16. R-CAUTION-004 implementation
17. R-SAFE-001 status
18. concurrent-rule behaviour
19. advisory/provenance behaviour
20. Safety Dominance result
21. human-authority result
22. existing/new/total test counts
23. PASS/FAIL/SKIPPED test counts
24. contract verification PASS/FAIL/OPEN
25. integrity result
26. F1–F3 status
27. E5 status
28. remaining OPEN items
29. F1_F3_IMPLEMENTATION_READY
30. exact closure/status line

Do NOT start F1–F3 automatically.
