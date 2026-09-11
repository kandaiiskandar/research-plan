# Journal 1 Layer 3 Prototype

## OPEN-L3-2 Algorithm-Boundary Taxonomy Micro-Repair

### Purpose

Perform one strictly bounded consistency repair to the already-accepted OPEN-L3-2 predicate evaluation failure resolution.

The scientific decision remains accepted:

```text
Model C + Model D

Predicate result domain:
{TRUE, FALSE, ERROR}

Any predicate ERROR
→ episode-level refusal
→ AI(E) = ∅
→ S unchanged
→ evaluation_failure = True
```

This task does **NOT** reopen the OPEN-L3-2 policy decision.

Current closure remains provisionally valid:

```text
JOURNAL 1 LAYER 3 OPEN-L3-2 CLOSED —
PREDICATE EVALUATION FAILURE SEMANTICS EXPLICITLY GOVERNED
```

The sole scientific/technical issue to repair is an inconsistency between the failure taxonomy and the stated Algorithm 3 structural-validation checks.

---

# 1. Scope

Inspect and repair only the OPEN-L3-2 artefacts necessary to resolve the following inconsistency:

```text
failure taxonomy:
F-T-04 = predicate/rule type mismatch

but

resolution/report Algorithm 3 validation list:
- operator validity
- categorical domain membership
- referenced variable existence
```

`referenced variable existence` does not replace `type compatibility`.

The repaired Algorithm 3 validation contract must distinguish these concerns explicitly.

Primary artefacts:

```text
data/journal1-layer3-prototype/open-l3-2-resolution/
    failure-taxonomy.csv
    policy-candidate-matrix.csv
    algorithm-boundary-analysis.md
    resolution.json
    verification.json
    report.md

publications/active/journal-1/layer3-prototype-specification.md
```

Do not perform a repository-wide audit.

---

# 2. Frozen Scientific Decision

Do not change:

```text
selected_policy =
Model C + Model D
```

Do not change:

```text
predicate domain = {TRUE, FALSE, ERROR}
```

Do not change:

```text
ERROR ≠ FALSE
ERROR ≠ TRUE
```

Do not change:

```text
any runtime predicate ERROR
→ AI(E) = ∅
→ evaluation_failure = True
→ no partial advisory output
→ S unchanged
```

Do not change:

```text
UNSAFE
→ G(S) = 0
→ no engine invocation
```

Do not change:

```text
configuration_failure
≠
evaluation_failure
```

---

# 3. Required Algorithm 3 Structural Validation Contract

The repaired Algorithm 3 structural validation should explicitly distinguish at least the following checks:

```text
V1 — referenced variable exists in DecisionContext schema

V2 — predicate operand/value type is compatible
     with the declared variable type

V3 — predicate operator is valid for the
     declared variable/value operand types

V4 — categorical predicate value belongs
     to the declared variable domain
```

These are separate validation concerns.

Do not collapse:

```text
unknown variable
```

into:

```text
type mismatch
```

unless current repository authority already defines them as the same failure class.

Do not claim that variable-name existence validation closes a type-compatibility failure.

---

# 4. Failure Taxonomy Repair

Inspect:

```text
failure-taxonomy.csv
```

Current taxonomy contains approximately:

```text
F-T-04 — type mismatch
F-T-05 — invalid operator
F-T-06 — unsupported categorical value
```

but the resolution also requires:

```text
referenced variable does not exist in DecisionContext schema
```

Determine the cleanest explicit taxonomy representation.

Preferred approach, if no existing authority blocks it:

```text
F-T-04 — predicate operand/type mismatch
F-T-05 — invalid operator for declared operand types
F-T-06 — unsupported categorical/domain value
F-T-11 — unknown/unresolvable predicate variable reference
```

The exact new ID may differ if repository numbering constraints require another choice.

If adding a new failure class would create unnecessary renumbering or conflict, preserve F-T-04..F-T-10 and add a distinct new ID after the existing sequence.

Do not repurpose an existing failure ID to mean two different things.

---

# 5. Ownership Boundary

The repaired taxonomy must preserve this boundary:

## Layer 2

Environmental resolution failures remain upstream.

```text
resolution failure
→ ⊥
→ S = UNSAFE
→ G(S) = 0
→ Layer 3 not invoked
```

## execute_episode startup

Required episode/context structure failures may still be treated as pre-reasoning configuration/startup failures where already defined.

## Algorithm 3

Failures detectable without evaluating actual runtime environmental values belong here, including:

```text
unknown predicate variable
type incompatibility
invalid operator/type pairing
categorical value outside declared domain
recommendation-type containment violation
```

Handling:

```text
ConfigurationError
configuration_failure = True
AI(E) = ∅
S unchanged
no reasoning
```

## Algorithm 4 / engine.reason()

Only failures dependent on actual runtime evaluation remain OPEN-L3-2 runtime failures, e.g.:

```text
runtime predicate exception
numeric conversion failure on actual input
malformed runtime value
unexpected internal evaluation error
```

Handling remains:

```text
evaluation_failure = True
AI(E) = ∅
S unchanged
```

---

# 6. Do Not Overclaim Algorithm 3 Authority

The extended validation remains:

```text
DESIGN_INTERPRETATION
```

unless direct repository authority establishes otherwise.

Do not say the canonical architecture formally mandates these exact four software validation checks.

The defensible claim is:

```text
These checks are assigned to Algorithm 3 because they are
structural/configuration-detectable before runtime reasoning,
consistent with Algorithm 3's existing validation role.
```

---

# 7. Report Repair

Inspect `report.md`, especially the Algorithm 3 section.

The repaired text must enumerate all distinct checks consistently.

For example:

```text
By design interpretation, validate_rule_set() extends its
pre-reasoning structural validation to:

1. referenced variable existence;
2. predicate operand/value type compatibility;
3. operator validity for declared operand types;
4. categorical value-domain membership.
```

Then map each check explicitly to the relevant failure taxonomy ID.

Do not say:

```text
three additional checks
```

if four are actually specified.

Do not claim F-T-04 is covered by variable-name existence.

---

# 8. Algorithm Boundary Analysis Repair

Inspect:

```text
algorithm-boundary-analysis.md
```

Ensure the Algorithm 3 table and boundary diagram include the repaired variable-reference failure class separately from type mismatch.

The narrative should preserve:

```text
configuration failure
and
runtime evaluation failure
```

as distinct classes.

---

# 9. resolution.json Repair

Inspect:

```text
resolution.json
```

Under the Algorithm 3 boundary, the final `extended_validation_scope` should explicitly include:

```text
referenced variable existence
predicate operand/value type compatibility
operator validity
categorical value-domain membership
```

Ensure failure IDs and handling align with `failure-taxonomy.csv`.

Do not modify the selected policy.

---

# 10. verification.json Repair

Extend verification only as necessary to prove consistency.

Add or update checks equivalent to:

```text
unknown_variable_distinguished_from_type_mismatch

algorithm3_validation_scope_matches_failure_taxonomy

F_T_04_meaning_consistent_across_artefacts

all_structural_validation_classes_have_unique_taxonomy_mapping
```

Existing scientific checks must remain PASS.

Report updated PASS / FAIL / OPEN counts.

---

# 11. layer3-prototype-specification.md

Inspect the sections updated by OPEN-L3-2.

If the specification repeats the incomplete three-check list, repair it to the four-check structural validation contract.

Do not alter unrelated Batch 1 or Batch 2 scientific content.

---

# 12. Branch Metadata Residue

The current prototype specification may still contain:

```text
Branch: design/journal1-algorithm-specification
```

while the OPEN-L3-2 task was executed on:

```text
design/journal1-layer3-predicate-failure-policy
```

Inspect whether this branch field is intended to represent:

```text
historical document-origin branch
```

or:

```text
current workstream branch
```

If it is stale current-workstream metadata, repair it.

If it is intentionally historical metadata, do not overwrite it; clarify its meaning instead.

This is metadata hygiene only and must not affect the scientific closure.

---

# 13. Protected State

Do not modify:

```text
docs/canonical/appendix-c-formalisation.md
docs/canonical/architecture-illustration.md
```

Do not modify:

```text
A_AI
G
Layer 2 thresholds
g_t
g_r
RS_candidate scientific rule content
OPEN-L3-3 Resolution B
GAP-03
OPEN-L3-1C
OPEN-L3-1D
```

Do not implement:

```text
reasoning_engine.py
rule_set_provider.py
predicate evaluation code
trace code
```

No engine implementation in this task.

---

# 14. Required Verification

At minimum verify:

```text
predicate_ERROR_not_silently_FALSE = PASS
predicate_ERROR_not_silently_TRUE = PASS
FALSE_distinguished_from_ERROR = PASS

unknown_variable_distinguished_from_type_mismatch = PASS

type_mismatch_has_unique_taxonomy_meaning = PASS

invalid_operator_has_unique_taxonomy_meaning = PASS

unsupported_categorical_value_has_unique_taxonomy_meaning = PASS

algorithm3_validation_scope_matches_taxonomy = PASS

configuration_failure_distinguished_from_evaluation_failure = PASS

Layer2_failure_distinguished_from_Layer3_failure = PASS

S_not_mutated = PASS

UNSAFE_short_circuit_preserved = PASS

no_advisory_from_unestablished_antecedent = PASS

selected_policy_C_plus_D_unchanged = PASS

OPEN_L3_3_remains_CLOSED = PASS

OPEN_L3_1C_preserved = PASS
OPEN_L3_1D_preserved = PASS
GAP_03_preserved = PASS

canonical_files_unchanged = PASS

engine_not_implemented = PASS
F1_F3_not_run = PASS
E5_not_run = PASS
```

Also parse:

```text
failure-taxonomy.csv
policy-candidate-matrix.csv
resolution.json
verification.json
```

and report structural validity.

---

# 15. Stop Conditions

STOP and report OPEN if the repair discovers that:

* current repository authority explicitly conflicts with separating unknown-variable and type-mismatch failures;
* changing the taxonomy would alter the accepted Model C+D semantics;
* Algorithm 3 cannot defensibly own one of the structural failures without changing the formal architecture;
* a canonical change would be required.

Do not force closure around a contradiction.

---

# 16. Expected Outcome

If the repair succeeds, retain:

```text
OPEN-L3-2 = CLOSED
```

and retain exactly:

```text
JOURNAL 1 LAYER 3 OPEN-L3-2 CLOSED —
PREDICATE EVALUATION FAILURE SEMANTICS EXPLICITLY GOVERNED
```

Add a micro-repair status line:

```text
OPEN-L3-2 ALGORITHM-BOUNDARY TAXONOMY MICRO-REPAIR CLOSED —
STRUCTURAL VALIDATION CLASSES ALIGNED
```

---

# 17. Required Final Response

Return:

1. Verdict
2. Files inspected
3. Exact inconsistency found
4. Final Algorithm 3 validation checks
5. Final failure taxonomy mapping
6. Whether a new failure ID was added
7. Algorithm 3 / Algorithm 4 boundary result
8. `resolution.json` changes
9. `report.md` changes
10. `algorithm-boundary-analysis.md` changes
11. `verification.json` changes
12. Branch metadata result
13. Canonical integrity result
14. Verification PASS / FAIL / OPEN counts
15. CSV/JSON parse results
16. Files modified
17. Remaining OPEN items
18. Exact micro-repair closure line

Do not begin Layer 3 Batch 3 implementation in this task.
