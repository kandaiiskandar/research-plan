# Journal 1 Layer 3 Prototype

## Batch 3 — Governed Core Engine Implementation

### Task Type

Bounded implementation task.

Implement the executable Layer 3 governed reasoning engine from the already-closed scientific and design specifications.

This task is **not** a new scientific-specification task.

Do not invent:

* new advisory rules;
* new recommendation types;
* new Layer 2 thresholds;
* new predicate semantics;
* new governance states;
* new scientific evidence;
* new safety claims;
* new performance thresholds.

Do not run the Journal 1 scientific evaluation yet.

---

# 1. Branch

Work on:

```text
feat/journal1-layer3-core-engine
```

Before making changes, verify the actual current branch and repository status.

Record:

```text
branch
HEAD commit
working-tree status
```

If the repository contains unrelated uncommitted changes, do not silently overwrite them.

---

# 2. Primary Implementation Authority

Read these documents before implementing anything:

```text
publications/active/journal-1/layer3-prototype-specification.md
publications/active/journal-1/algorithm-specification.md
publications/active/journal-1/evaluation-specification.md
```

Also inspect the closed Layer 3 evidence:

```text
data/journal1-layer3-prototype/
data/journal1-layer3-prototype/open-l3-2-resolution/
data/journal1-layer3-prototype/open-l3-3-resolution/
```

Treat the closed specifications as implementation authority.

Do not reinterpret them for convenience.

---

# 3. Frozen Scientific State

Preserve:

```text
S ∈ {SAFE, CAUTION, UNSAFE}

G(SAFE)    = 1
G(CAUTION) = 1
G(UNSAFE)  = 0
```

Preserve:

```text
R = {Go, Delay, DepartureTime, Duration}

A_AI(SAFE)    = FULL
A_AI(CAUTION) = {Go, Delay}
A_AI(UNSAFE)  = ∅
```

Preserve Safety Dominance:

```text
AI(E) ⊆ A_AI(S)
```

Human authority remains unconditional.

An empty advisory set:

```text
AI(E) = ∅
```

must never be represented as:

```text
departure prohibited
unsafe physical condition
automated human decision
```

---

# 4. Frozen Rule-Content State

Do not invent new scientific rule content.

Use only concrete rules already admitted by the closed Batch 2 scientific specification.

Current scientific candidates include:

```text
SAFE:
R-SAFE-001 → Go
CONDITIONALLY SUPPORTED
```

and:

```text
CAUTION:
R-CAUTION-001 → Delay
R-CAUTION-002 → Delay
R-CAUTION-003 → Delay
R-CAUTION-004 → Delay

all CONDITIONALLY SUPPORTED
```

Read the Batch 2 authority artefacts for their exact predicates, mappings, provenance, and payload requirements.

Do not reconstruct these rules from memory or Layer 2 thresholds.

If any concrete rule cannot be implemented exactly from the existing Batch 2 specification, STOP that rule and report the missing implementation authority.

Do not guess.

---

# 5. Protected OPEN Items

Preserve:

```text
OPEN-L3-1C = OPEN
```

for `DepartureTime`.

Preserve:

```text
OPEN-L3-1D = OPEN
```

for `Duration`.

Preserve:

```text
GAP-03 = OPEN evidence gap
```

for the absence of independent evidence supporting a CAUTION→Go rule.

Therefore:

* do not invent a DepartureTime rule;
* do not invent a Duration rule;
* do not invent a CAUTION→Go rule;
* do not convert admissibility into rule existence.

In particular:

```text
Go ∈ A_AI(CAUTION)
```

does **not** imply:

```text
∃ rule producing Go under CAUTION
```

---

# 6. Preserve OPEN-L3-3 Resolution B

OPEN-L3-3 is CLOSED under Resolution B.

Preserve:

```text
S = CAUTION ∧ Go ∈ AI(E)
→ Present(Go, caution_qualifier)
```

Do not implement:

```text
S = CAUTION
→ Go ∈ AI(E)
```

Presentation qualification must not create a recommendation.

If presentation rendering is outside the Batch 3 core-engine boundary, leave the presentation mechanism outside the engine and document the interface expectation.

Do not create a synthetic Go advisory merely to exercise this path.

---

# 7. Target Module Structure

Implement the existing prototype module design unless the repository already contains an equivalent implementation:

```text
governance/
    __init__.py
    rule.py
    advisory.py
    rule_repository.py
    rule_set_provider.py
    reasoning_engine.py
    reasoning_episode.py
    fidelity_trace.py
```

The intended responsibilities are:

```text
rule.py
→ Rule
→ ConditionPredicate
→ structural rule representation

advisory.py
→ Advisory output representation

rule_repository.py
→ repository of scientifically admitted rules

rule_set_provider.py
→ Algorithm 3
→ select
→ validate
→ supply

reasoning_engine.py
→ Algorithm 4 reasoning
→ predicate evaluation
→ deterministic rule firing

reasoning_episode.py
→ governed episode orchestration

fidelity_trace.py
→ conceptual fidelity instrumentation
```

Do not change module boundaries merely for stylistic preference unless an actual implementation conflict requires it.

Document any justified deviation.

---

# 8. Rule and Predicate Representation

Implement the existing Rule and ConditionPredicate contracts from the prototype specification.

At minimum, preserve the conceptual schema:

```text
Rule:
    rule_id
    applicable_state
    conditions
    conclusion_type
    conclusion_payload
    provenance
    enabled
```

and:

```text
ConditionPredicate:
    variable
    operator
    value
```

Supported operators must come from the existing specification.

Do not silently add operators.

All predicates within a rule are conjunctive:

```text
p1 ∧ p2 ∧ ... ∧ pn
```

A rule fires if and only if all predicates evaluate `TRUE`.

---

# 9. Algorithm 3 — Rule-Set Selection

Implement:

```text
select_rule_set(repository, state)
```

with the existing state-indexed semantics.

Conceptually:

```text
RS_SAFE =
enabled rules where applicable_state == SAFE

RS_CAUTION =
enabled rules where applicable_state == CAUTION

RS_UNSAFE =
∅
```

Preserve:

```text
RS(UNSAFE) = ∅
```

The governed UNSAFE path should not invoke Layer 3 reasoning.

---

# 10. Algorithm 3 — Admissibility Validation

Preserve the existing formal validation:

```text
ConclusionTypes(RS_candidate) ⊆ A_AI(S)
```

If violated:

```text
ConfigurationError
configuration_failure = True
AI(E) = ∅
S unchanged
no reasoning
```

Do not post-hoc filter invalid advisories.

The invalid rule set must be refused before reasoning.

---

# 11. Algorithm 3 — Structural Validation V1–V4

Implement the frozen OPEN-L3-2 micro-repair contract.

The four checks are:

```text
V1 — referenced variable exists in DecisionContext schema
     → F-T-11

V2 — predicate operand/value type is compatible
     with declared variable type
     → F-T-04

V3 — operator is valid for the declared operand types
     → F-T-05

V4 — categorical predicate value belongs
     to the declared variable domain
     → F-T-06
```

Order matters.

At minimum:

```text
V1 before V2
```

because an unknown variable has no declared type to check.

Do not collapse:

```text
unknown variable
```

into:

```text
type mismatch
```

These are distinct configuration-fidelity failures.

All V1–V4 violations occur before runtime reasoning and must produce:

```text
ConfigurationError
configuration_failure = True
AI(E) = ∅
S unchanged
```

These checks remain a design interpretation of Algorithm 3's structural-validation role.

Do not promote them into new external scientific claims.

---

# 12. Algorithm 4 — Predicate Result Domain

Implement the closed OPEN-L3-2 contract:

```text
PredicateResult = {TRUE, FALSE, ERROR}
```

Semantics:

```text
TRUE
= predicate successfully evaluated and satisfied

FALSE
= predicate successfully evaluated and not satisfied

ERROR
= predicate could not be established because evaluation failed
```

Critical invariant:

```text
ERROR ≠ FALSE
ERROR ≠ TRUE
```

Do not implement:

```text
except:
    return False
```

Do not implement:

```text
except:
    return True
```

---

# 13. Rule Firing Semantics

A rule fires if and only if:

```text
∀p ∈ conditions(rule):
    evaluate(p, E) = TRUE
```

Therefore:

```text
all TRUE
→ fire rule

any FALSE
→ normal no-fire

any ERROR
→ evaluation failure
```

`FALSE` is an ordinary semantic result.

`ERROR` is an execution failure state.

They must remain distinguishable in code and trace output.

---

# 14. OPEN-L3-2 Model C+D Runtime Failure Policy

Implement the accepted policy:

```text
Model C + Model D
```

If any runtime predicate evaluation returns `ERROR`:

```text
AI(E) = ∅
evaluation_failure = True
S unchanged
G(S) unchanged
A_AI(S) unchanged
no partial advisory output
human authority preserved
```

The episode must refuse advisory generation.

Do not implement rule-local quarantine as the externally visible episode result.

For example, this is prohibited:

```text
rule A → ERROR
rule B → TRUE
therefore emit advisory from rule B
```

The final episode result must instead be:

```text
AI(E) = ∅
evaluation_failure = True
```

---

# 15. Runtime Failure Taxonomy

Implement structured handling for the runtime classes already specified:

```text
F-T-07 — runtime predicate exception

F-T-08 — numeric conversion failure on actual context value

F-T-09 — malformed runtime value

F-T-10 — unexpected internal evaluation error
```

Do not invent additional scientific meaning for these categories.

If implementation reveals an engineering exception class not cleanly represented by this taxonomy, report it rather than silently altering the scientific taxonomy.

---

# 16. Early Abort vs Complete Failure Collection

The closed OPEN-L3-2 contract permits either:

```text
A. abort on first ERROR
```

or:

```text
B. continue evaluating to collect all ERROR-producing rules,
   then refuse the episode
```

Both must produce:

```text
AI(E) = ∅
```

Choose the simpler deterministic implementation unless existing repository authority specifies otherwise.

Document the chosen strategy as an engineering decision.

Do not claim scientific superiority for the selected strategy.

---

# 17. UNSAFE Short-Circuit

Implement the governed wrapper so that:

```text
S = UNSAFE
→ G(S) = 0
→ AI(E) = ∅
→ no RS supplied
→ no predicate evaluation
→ engine.reason() not invoked
```

This should be structurally testable.

Do not create an empty rule-set reasoning pass merely for implementation convenience.

The engine should not execute for UNSAFE.

---

# 18. Reasoning Episode

Implement the episode orchestration approximately as:

```text
execute_episode(S, E, repository)

1. establish governance configuration
2. if G(S) == 0:
       return AI(E) = ∅ with trace
3. select RS_candidate(S)
4. validate RS_candidate
5. supply RS(S)
6. engine.reason(E, RS(S))
7. produce AI(E)
8. emit fidelity trace
9. return EpisodeResult
```

Preserve the actual authority contracts if they differ in naming or interface details.

Layer 3 consumes S.

It must never compute or mutate S.

---

# 19. Advisory Output

Every generated advisory must satisfy:

```text
advisory.type ∈ A_AI(S)
```

and be attributable to an actually fired rule.

At minimum retain:

```text
type
payload
rule_id
explanation
```

where already specified.

No advisory may exist without a fired rule.

Do not create state-only advisories.

---

# 20. Fidelity Trace Implementation

Implement the trace schema already specified by Batch 1 and OPEN-L3-2.

Preserve existing fields including, where defined:

```text
episode_id
S
G
A_AI
active_rule_ids
active_rule_conclusion_types
fired_rule_ids
generated_advisory_types
configuration_failure
S_old
S_new
rule_set_bound_for_state
```

Implement the OPEN-L3-2 additions:

```text
evaluation_failure: bool

failed_rule_ids: list[str]

failure_category:
    PREDICATE_EXCEPTION
    NUMERIC_CONVERSION_FAILURE
    MALFORMED_VALUE
    INTERNAL_ERROR
    or None
```

The trace must distinguish:

```text
fired_rule_ids = []
evaluation_failure = False
```

from:

```text
fired_rule_ids = []
evaluation_failure = True
```

The first means normal no-fire.

The second means reasoning failed.

---

# 21. Configuration Failure vs Evaluation Failure

These must remain separate.

## Configuration failure

Occurs before reasoning, for example:

```text
V1
V2
V3
V4
A_AI containment failure
required episode structural failure
```

Trace:

```text
configuration_failure = True
evaluation_failure = False
AI(E) = ∅
```

## Runtime evaluation failure

Occurs during `engine.reason()`:

```text
F-T-07..F-T-10
```

Trace:

```text
configuration_failure = False
evaluation_failure = True
AI(E) = ∅
```

Do not use one generic boolean for both.

---

# 22. Determinism

The engine should be deterministic.

Given identical:

```text
S
DecisionContext
repository
enabled rule set
```

the engine must produce identical:

```text
AI(E)
fired_rule_ids
generated_advisory_types
failure state
```

Do not introduce:

```text
LLM inference
randomness
network calls
external model calls
non-deterministic ranking
```

into the Layer 3 prototype.

---

# 23. Production Rule Engine Strategy / OPEN-B3-2

Use the simplest implementation consistent with the existing algorithm specification.

A deterministic linear scan is acceptable if supported by the existing prototype specification:

```text
for rule in RS(S):
    evaluate conditions
    if all TRUE:
        emit rule conclusion
```

Do not introduce a third-party rule-engine dependency unless repository evidence establishes a need.

If this implementation sufficiently resolves the implementation-strategy portion of OPEN-B3-2, document exactly what is closed and what remains OPEN.

Do not automatically declare the entire OPEN-B3-2 scientific/performance issue closed.

Do not make efficiency claims.

Preserve the established complexity form:

```text
T_select + O(k_S)
```

where applicable.

---

# 24. Concrete Rule Loading

Separate:

```text
engine mechanism
```

from:

```text
scientific rule content
```

The engine must be generic.

Load only Batch 2 rules whose scientific predicates and mappings are sufficiently specified for executable representation.

If any CONDITIONALLY SUPPORTED rule lacks enough information for exact executable conditions:

```text
DO NOT invent the missing condition.
```

Instead:

```text
mark rule implementation deferred
record exact missing authority
continue implementing generic engine
```

The core engine must not depend on all future recommendation types being populated.

---

# 25. OPEN-L3-1C and OPEN-L3-1D

Do not implement concrete rules producing:

```text
DepartureTime
Duration
```

unless those rules already have explicit scientific authority in the closed Batch 2 artefacts.

Their presence in:

```text
R
```

or:

```text
A_AI(SAFE)
```

is not sufficient evidence for rule creation.

Keep:

```text
OPEN-L3-1C = OPEN
OPEN-L3-1D = OPEN
```

---

# 26. GAP-03

Preserve:

```text
GAP-03 = OPEN evidence gap
```

Do not add:

```text
CAUTION → Go
```

merely because:

```text
Go ∈ A_AI(CAUTION)
```

Admissibility and scientific rule support are different concepts.

---

# 27. Tests Required in Batch 3

This task should include implementation-level automated tests.

These are engineering verification tests, **not yet Journal 1 F1–F3 scientific evaluation**.

At minimum test:

```text
T01 SAFE gate enabled

T02 CAUTION gate enabled

T03 UNSAFE gate disabled

T04 UNSAFE returns AI(E)=∅ without engine invocation

T05 SAFE selects only SAFE rules

T06 CAUTION selects only CAUTION rules

T07 disabled rules excluded

T08 A_AI containment violation rejected

T09 V1 unknown variable → F-T-11 configuration failure

T10 V2 type mismatch → F-T-04 configuration failure

T11 V3 invalid operator → F-T-05 configuration failure

T12 V4 invalid categorical value → F-T-06 configuration failure

T13 all predicates TRUE → rule fires

T14 any predicate FALSE → normal no-fire

T15 predicate ERROR ≠ FALSE

T16 predicate ERROR → episode refusal

T17 runtime failure → evaluation_failure=True

T18 runtime failure → AI(E)=∅

T19 runtime failure does not mutate S

T20 no partial advisory survives runtime failure

T21 configuration_failure and evaluation_failure distinguishable

T22 emitted advisory attributable to fired rule

T23 generated advisory type ∈ A_AI(S)

T24 identical input produces identical output

T25 human-authority boundary preserved structurally
```

Add more implementation tests where necessary, but do not turn them into new scientific claims.

---

# 28. Explicitly Do Not Run F1–F3

Do not report:

```text
F1 = PASS
F2 = PASS
F3 = PASS
```

as scientific evaluation results in this task.

You may state:

```text
implementation tests exercise mechanisms required for future F1–F3
```

but fidelity evaluation remains a separate downstream task.

Do not update Journal 1 results tables with F1–F3 results.

---

# 29. Do Not Run E5

Do not benchmark latency as Journal 1 evidence.

Do not invent:

```text
X ms
latency threshold
acceptable runtime threshold
```

`OPEN-B1-6` remains OPEN unless separately resolved.

Implementation-level timing used solely for debugging must not be reported as E5 evidence.

---

# 30. No Layer 2 Reimplementation

Do not implement:

```text
ρ_{D,τ}
f
F_{D,τ}
g_w
g_r
g_m
g_o
g_t
```

inside the Layer 3 engine.

The prototype receives the already determined:

```text
S
```

and resolved DecisionContext.

Layer 3 must not become a second safety classifier.

---

# 31. Protected Canonical Files

Do not modify:

```text
docs/canonical/appendix-c-formalisation.md
docs/canonical/architecture-illustration.md
```

Do not modify canonical thresholds or formal definitions.

If implementation exposes a genuine contradiction with canonical authority:

```text
STOP
```

and report the contradiction.

Do not silently repair canonical authority inside this implementation task.

---

# 32. Evidence Directory

Create:

```text
data/journal1-layer3-prototype/batch3-core-engine/
```

At minimum produce:

```text
implementation-manifest.json
test-results.json
contract-verification.json
report.md
```

Recommended additional artefacts where useful:

```text
module-map.md
failure-path-verification.json
rule-loading-manifest.json
```

`implementation-manifest.json` should record:

```text
branch
HEAD-before
implementation files
test files
scientific authority files used
implemented rule IDs
deferred rule IDs
OPEN items preserved
```

---

# 33. Contract Verification

Create explicit checks for at least:

```text
G_mapping_preserved

A_AI_mapping_preserved

UNSAFE_short_circuit_preserved

RS_UNSAFE_empty

Algorithm3_containment_enforced

V1_FT11_enforced
V2_FT04_enforced
V3_FT05_enforced
V4_FT06_enforced

ERROR_distinct_from_FALSE
ERROR_distinct_from_TRUE

runtime_ERROR_causes_episode_refusal

runtime_ERROR_produces_empty_AI

runtime_ERROR_does_not_mutate_S

configuration_failure_distinct_from_evaluation_failure

no_partial_advisory_on_evaluation_failure

every_advisory_has_fired_rule

every_advisory_within_A_AI

deterministic_output

OPEN_L3_3_resolution_B_preserved

no_CAUTION_Go_rule_invented

OPEN_L3_1C_preserved

OPEN_L3_1D_preserved

GAP_03_preserved

canonical_files_unchanged

Layer2_not_reimplemented

F1_F3_not_run

E5_not_run
```

Report:

```text
PASS
FAIL
OPEN
```

counts.

A FAIL must not be hidden by an overall PASS.

---

# 34. Stop Conditions

STOP and do not claim Batch 3 closure if:

* implementation requires inventing a scientific predicate;
* implementation requires inventing a new advisory mapping;
* concrete Batch 2 rule content is insufficient and the engine cannot remain generic without it;
* Model C+D cannot be implemented without changing its semantics;
* Algorithm 3 V1–V4 conflict with existing repository authority;
* Layer 3 would need to mutate S;
* UNSAFE would require reasoning-engine invocation;
* an advisory can be emitted without a fired rule;
* a runtime ERROR can produce partial advisory output;
* implementation requires modifying canonical architecture;
* tests expose a contradiction between closed specifications.

Report the exact blocker.

Do not force closure.

---

# 35. Closure Criteria

Batch 3 may close only if:

```text
core modules implemented
Algorithm 3 implemented
V1–V4 implemented
Algorithm 4 deterministic engine implemented
Model C+D implemented
UNSAFE short-circuit implemented
fidelity trace implemented
engineering tests pass
contract verification passes
no scientific rules invented
protected OPEN items preserved
canonical integrity preserved
F1–F3 not run
E5 not run
```

If some concrete Batch 2 rules remain non-executable due to insufficient scientific specification, distinguish:

```text
core engine implementation closure
```

from:

```text
complete scientific rule-set population
```

Do not fail the generic engine merely because OPEN-L3-1C/1D remain OPEN.

---

# 36. Expected Closure Line

If all Batch 3 core-engine criteria pass, use exactly:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 3 CLOSED —
GOVERNED CORE ENGINE AND FAILURE CONTRACT IMPLEMENTED
```

If implementation is complete but a bounded non-core item remains OPEN, do not use this line unless the closure criteria above are genuinely satisfied.

If blocked, provide:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 3 REMAINS OPEN —
<EXACT BLOCKER>
```

---

# 37. Required Final Report

Return:

1. Verdict
2. Branch and HEAD
3. Authorities inspected
4. Files created
5. Files modified
6. Module implementation summary
7. Algorithm 3 implementation
8. V1–V4 validation implementation
9. Algorithm 4 implementation
10. Predicate TRUE/FALSE/ERROR implementation
11. Model C+D failure handling
12. UNSAFE short-circuit
13. Rule loading status
14. Implemented scientific rule IDs
15. Deferred rule IDs and exact reason
16. Fidelity trace implementation
17. Configuration vs evaluation failure handling
18. OPEN-B3-2 status
19. Automated test results
20. Contract-verification PASS / FAIL / OPEN counts
21. Canonical integrity
22. Protected OPEN items
23. Confirmation F1–F3 were not run
24. Confirmation E5 was not run
25. Remaining blockers
26. Exact closure/status line

Do not start the next scientific evaluation task automatically.
