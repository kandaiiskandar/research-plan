# Journal 1 Layer 3 Prototype

## OPEN-L3-2 — Predicate Evaluation Failure Policy

### Task type

Scientific/design resolution only.

Resolve the currently OPEN item:

```text
OPEN-L3-2 — Predicate evaluation failure handling
```

Do **not** implement the Layer 3 engine in this task.

Do not run F1–F3.

Do not run E5.

Do not invent scientific advisory rules.

Do not reopen Batch 2 or OPEN-L3-3.

---

# 1. Starting scientific state

The following state is frozen:

```text
OPEN-L3-3 = CLOSED — Resolution B

JOURNAL 1 LAYER 3 PROTOTYPE BATCH 2 CLOSED —
CAUTION-GO PRESENTATION SEMANTICS RESOLVED
```

Resolution B remains:

```text
S = CAUTION ∧ Go ∈ AI(E)
→ Present(Go, caution_qualifier)
```

not:

```text
S = CAUTION
→ Go ∈ AI(E)
```

Preserve:

```text
A_AI(SAFE)    = FULL
A_AI(CAUTION) = {Go, Delay}
A_AI(UNSAFE)  = ∅

G(SAFE)    = 1
G(CAUTION) = 1
G(UNSAFE)  = 0
```

Current scientific rule candidates remain unchanged.

SAFE:

```text
R-SAFE-001 → Go
CONDITIONALLY SUPPORTED
```

CAUTION:

```text
R-CAUTION-001 → Delay
R-CAUTION-002 → Delay
R-CAUTION-003 → Delay
R-CAUTION-004 → Delay
```

all CONDITIONALLY SUPPORTED.

Preserve:

```text
GAP-03 = OPEN evidence gap
OPEN-L3-1C = OPEN
OPEN-L3-1D = OPEN
```

---

# 2. Problem to resolve

Batch 1 established that predicate evaluation failures must **not silently collapse to false**.

For a rule:

```text
r = (conditions, conclusion)
```

there is an important semantic distinction between:

```text
predicate evaluates TRUE
predicate evaluates FALSE
predicate cannot be evaluated
```

The third case is not equivalent to FALSE.

This task must determine the explicit Layer 3 policy for predicate evaluation failures.

Examples include, but are not limited to:

```text
missing field
null / absent field
malformed value
wrong type
unsupported categorical value
predicate exception
numeric conversion failure
invalid operator application
unexpected internal evaluation error
```

Do not assume these cases are semantically identical.

---

# 3. Critical architecture boundary

Layer 2 already owns environmental-state resolution and safety-state classification.

Its established fail-safe semantics must not be silently duplicated or replaced inside Layer 3.

Layer 3 receives a resolved episode/environment representation and safety state under the defined architecture boundary.

Therefore distinguish carefully between:

```text
Layer 2 input-resolution failure
```

and:

```text
Layer 3 rule-predicate evaluation failure
```

Do not convert a Layer 3 predicate exception into a new Layer 2 safety classification unless an existing authority explicitly requires it.

In particular, do not automatically claim:

```text
predicate failure → S = UNSAFE
```

unless this is supported by the architecture.

S must not be silently mutated by Layer 3.

---

# 4. Candidate semantic models

Evaluate at least the following possibilities.

## Model A — Fail-closed predicate

```text
ERROR → FALSE
```

The failed predicate is treated as unsatisfied.

Analyse whether this silently hides evaluation failures.

---

## Model B — Fail-open predicate

```text
ERROR → TRUE
```

The rule may fire despite failure.

Analyse whether this can generate an advisory without a successfully established antecedent.

---

## Model C — Three-valued predicate semantics

```text
TRUE
FALSE
ERROR/UNKNOWN
```

A rule fires only if all required predicates evaluate TRUE.

FALSE means:

```text
antecedent successfully evaluated and not satisfied
```

ERROR/UNKNOWN means:

```text
antecedent could not be established
```

Determine what the engine should return when ERROR/UNKNOWN occurs.

---

## Model D — Episode-level refusal

Any predicate evaluation failure causes Layer 3 to refuse advisory generation for the episode while preserving S.

For example:

```text
S unchanged
G unchanged
configuration_failure / evaluation_failure recorded
AI(E) = ∅
human authority unchanged
```

Determine whether this is supported by existing architecture and failure-semantics contracts.

---

## Model E — Rule-local quarantine

A failed rule is marked unavailable, but other successfully evaluated rules may continue.

Analyse whether this is scientifically defensible or whether it risks producing incomplete/misleading advisory output.

---

Evaluate combinations if the existing architecture supports them.

Do not choose a model for implementation convenience.

---

# 5. Required semantic distinctions

Explicitly distinguish:

```text
FALSE
≠
ERROR
≠
NOT_APPLICABLE
≠
DISABLED
```

where supported by the current rule schema.

Also distinguish:

```text
configuration failure
```

from:

```text
runtime predicate evaluation failure
```

if the repository supports this distinction.

Determine whether malformed rule definitions should be rejected during Algorithm 3 rule-set supply rather than handled as ordinary runtime predicate failures.

---

# 6. Algorithm 3 compatibility

Inspect the current Algorithm 3 contract.

Existing principle:

```text
ConclusionTypes(RS_candidate) ⊆ A_AI(S)
```

Invalid candidate rule-set configuration is already treated as configuration-fidelity failure:

```text
refuse supply
no reasoning
S unchanged
```

Determine which failures belong to Algorithm 3 validation versus runtime predicate evaluation.

Do not blur:

```text
invalid rule configuration
```

with:

```text
valid rule + runtime evaluation failure
```

---

# 7. Algorithm 4 compatibility

Inspect Algorithm 4:

```text
check G(S)

if G(S) = 0:
    return ∅

else:
    engine.reason(E, RS(S))
```

Determine what `engine.reason()` must do if predicate evaluation fails.

Specify the contract without implementing the engine.

The policy must preserve:

```text
Safety Dominance
ConclusionTypes(AI(E)) ⊆ A_AI(S)
human authority unconditional
S unchanged by Layer 3
```

---

# 8. UNSAFE behaviour

Preserve existing UNSAFE semantics:

```text
S = UNSAFE
G(S) = 0
A_AI(UNSAFE) = ∅
no RS supplied
no reasoning
AI(E) = ∅
```

Predicate evaluation should therefore never occur for an UNSAFE episode under the governed wrapper.

Verify this explicitly.

---

# 9. Failure observability

Determine the minimum scientific trace needed to distinguish:

```text
normal no-fire
```

from:

```text
predicate evaluation failure
```

At minimum consider:

```text
episode_id
S
rule_id
predicate identifier
evaluation status
failure category
configuration_failure
evaluation_failure
AI(E)
```

Do not invent implementation-specific logging infrastructure.

Specify conceptual trace requirements only.

The trace must make it impossible for later F1–F3 analysis to count:

```text
predicate ERROR
```

as:

```text
predicate FALSE
```

without detection.

---

# 10. Scientific consequences

Analyse whether the selected policy affects:

```text
F1
F2
F3
Safety Dominance
rule firing interpretation
advisory completeness
future E5 measurements
```

Do not run these evaluations.

Only specify consequences for later measurement.

---

# 11. Evidence and authority hierarchy

Use repository authority in this order where applicable:

1. canonical formal architecture
2. Algorithm Specification authority
3. Layer 3 Prototype Batch 1 contract
4. Layer 3 Prototype Batch 2 scientific specification
5. evaluation specification
6. implementation/design interpretation

Clearly label any policy choice that is architecture/design interpretation rather than externally established scientific evidence.

Do not search for external literature merely to justify a preferred software behaviour unless the repository explicitly requires external authority for this decision.

---

# 12. Required evidence artefacts

Create:

```text
data/journal1-layer3-prototype/open-l3-2-resolution/
```

with at minimum:

```text
failure-taxonomy.csv
policy-candidate-matrix.csv
algorithm-boundary-analysis.md
resolution.json
verification.json
report.md
```

`failure-taxonomy.csv` should distinguish failure classes and ownership.

Suggested conceptual columns:

```text
failure_id
failure_class
example
layer_owner
detectable_stage
semantic_status
selected_handling
authority
notes
```

`policy-candidate-matrix.csv` should compare Models A–E.

---

# 13. Resolution requirements

A valid closure must establish explicitly:

```text
predicate result domain
rule firing condition
ERROR/UNKNOWN semantics
episode-level behaviour
whether other rules may continue
whether AI(E) is empty on evaluation failure
S mutation policy
trace requirements
Algorithm 3 boundary
Algorithm 4 boundary
UNSAFE short-circuit behaviour
```

Do not leave these implicit.

---

# 14. Stop conditions

STOP and keep OPEN-L3-2 unresolved if:

* current authorities materially conflict;
* the selected policy requires changing Layer 2 semantics;
* the selected policy requires introducing a new safety state;
* the selected policy requires silently treating ERROR as FALSE;
* the selected policy can generate an advisory from an unestablished antecedent;
* resolving the issue requires inventing scientific rule content;
* the correct behaviour cannot be determined without an unresolved upstream architecture decision.

Report the exact blocker rather than forcing closure.

---

# 15. Protected state

Do not modify the scientific content of:

```text
docs/canonical/appendix-c-formalisation.md
docs/canonical/architecture-illustration.md
```

unless a direct contradiction is discovered.

Do not modify:

```text
A_AI
G
Layer 2 thresholds
g_t
g_r
RS_candidate rule scientific content
OPEN-L3-3 Resolution B
GAP-03
```

Do not resolve OPEN-L3-1C or OPEN-L3-1D in this task.

---

# 16. Verification

At minimum verify:

```text
predicate_ERROR_not_silently_FALSE
predicate_ERROR_not_silently_TRUE
FALSE_distinguished_from_ERROR
configuration_failure_distinguished_from_runtime_evaluation_failure
Layer2_failure_distinguished_from_Layer3_failure
S_not_mutated_by_Layer3_failure
UNSAFE_short_circuits_before_reasoning
no_advisory_generated_from_unestablished_antecedent
Algorithm3_contract_preserved
Algorithm4_contract_preserved
Safety_Dominance_preserved
human_authority_preserved
OPEN_L3_3_remains_CLOSED
OPEN_L3_1C_preserved
OPEN_L3_1D_preserved
GAP_03_preserved
no_new_scientific_rules
engine_not_implemented
F1_F3_not_run
E5_not_run
canonical_integrity_preserved
```

Report PASS / FAIL / OPEN counts.

---

# 17. Closure outcome

If a policy is established without unresolved contradiction, close:

```text
OPEN-L3-2
```

and provide one exact closure line.

Recommended wording if the resulting contract uses explicit non-Boolean failure semantics and advisory refusal:

```text
JOURNAL 1 LAYER 3 OPEN-L3-2 CLOSED —
PREDICATE EVALUATION FAILURE SEMANTICS EXPLICITLY GOVERNED
```

Do not use this closure line if the actual selected policy differs materially.

If unresolved, provide an exact OPEN status line instead.

---

# 18. Required final response

Return:

1. Verdict
2. Authority inspected
3. Failure taxonomy
4. Candidate policy comparison
5. Selected policy
6. Predicate result domain
7. Rule firing semantics
8. Episode-level failure behaviour
9. Algorithm 3 boundary
10. Algorithm 4 boundary
11. UNSAFE behaviour
12. Trace requirements
13. Scientific/evaluation consequences
14. Canonical changes, if any
15. Remaining OPEN items
16. Verification PASS / FAIL / OPEN counts
17. Files created / modified
18. Exact closure or OPEN status line

Do not begin Batch 3 implementation in this task.
