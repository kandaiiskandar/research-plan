# Journal 1 Layer 3 Prototype

## Batch 4B-1 — Canonical Layer 2 → Layer 3 Interface Amendment

### Task Type

Bounded canonical/specification amendment.

This task occurs **after Batch 4A authority resolution** and **before Batch 4B-2 implementation**.

The purpose is to formally document the already-approved-in-principle **Model B component-state interface** so that the subsequent implementation has an explicit canonical/specification authority.

This task must NOT implement the interface in code.

This task must NOT add executable rules.

This task must NOT run F1–F3 or E5.

---

# 1. Branch

Create:

```text
design/journal1-layer3-component-state-interface
```

Record before work:

```text
current branch
HEAD commit
working-tree status
Batch 4A closure commit/hash
```

If Batch 4A changes have not yet been committed, STOP and report:

```text
BATCH4A_CLOSURE_NOT_COMMITTED
```

Do not mix Batch 4A evidence repairs with Batch 4B-1.

---

# 2. Primary Objective

Formally establish the interface:

```text
Layer 2
  ↓
S + ComponentStateTrace
  ↓
Layer 3
```

where `ComponentStateTrace` exposes **already-computed Layer 2 component classification results**.

Layer 3 consumes these values.

Layer 3 does NOT recompute:

```text
g_w
g_r
g_m
g_o
g_t
```

The amendment exists to support the already-resolved Batch 4A disposition:

```text
R-CAUTION-002
→ component_o_state == CAUTION

R-CAUTION-003
→ component_r_state == CAUTION

R-CAUTION-004
→ component_w_state == CAUTION
```

Do not implement these rules in this task.

---

# 3. Authorities

Read before modifying anything:

```text
docs/canonical/appendix-c-formalisation.md
docs/canonical/architecture-illustration.md

publications/active/journal-1/layer3-prototype-specification.md
publications/active/journal-1/algorithm-specification.md
publications/active/journal-1/evaluation-specification.md

data/journal1-layer3-prototype/batch4a-executable-rule-authority/
    report.md
    resolution.json
    verification.json
    rule-executability-matrix.csv
    interface-candidate-matrix.csv
    layer2-layer3-interface-analysis.md
```

Also inspect, read-only:

```text
governance/rule.py
governance/rule_set_provider.py
governance/reasoning_episode.py
governance/canonical_rules.py
```

The implementation files are read-only in Batch 4B-1.

---

# 4. Frozen Batch 4A Decisions

Do NOT reopen these decisions.

## 4.1 Selected interface

```text
Model B — Layer 2 component-state interface
```

Accepted in principle.

## 4.2 Model A

```text
raw-value predicate expansion
```

REJECTED because it duplicates Layer 2 classifiers.

## 4.3 Model C

```text
reasons taxonomy as governance/rule-selection input
```

REJECTED.

Reasons remain explanatory only.

## 4.4 Model D

Partial:

```text
R-SAFE-001 remains deferred.
```

## 4.5 R-SAFE-001

Frozen:

```text
R-SAFE-001
classification = STATE_RESTATEMENT
disposition = DEFERRED
implementation_authorised = false
```

Do not repair it.

Do not invent an additional discriminant.

Do not convert it into:

```text
SAFE → Go
```

## 4.6 R-CAUTION rules

Frozen dispositions:

```text
R-CAUTION-001
IMPLEMENTED
NO CHANGE

R-CAUTION-002
EXECUTABLE_WITH_INTERFACE_EXTENSION
AUTHORISED IN PRINCIPLE

R-CAUTION-003
EXECUTABLE_WITH_INTERFACE_EXTENSION
AUTHORISED IN PRINCIPLE

R-CAUTION-004
EXECUTABLE_WITH_INTERFACE_EXTENSION
AUTHORISED IN PRINCIPLE
```

Implementation remains blocked until this amendment closes.

---

# 5. Canonical Architecture Amendment

Modify only the necessary Layer 2 → Layer 3 interface description in:

```text
docs/canonical/architecture-illustration.md
```

The amendment must make explicit that Layer 2 provides:

```text
S
+
ComponentStateTrace
```

to the Layer 3 execution boundary.

Do NOT rewrite unrelated architecture sections.

Do NOT modify:

```text
G(S)
A_AI(S)
RS(S)
Safety Dominance
cause taxonomy
human authority
Layer 1 semantics
Layer 2 thresholds
```

The change must be minimal and traceable.

---

# 6. Formal Meaning of ComponentStateTrace

Document `ComponentStateTrace` as an **implementation-facing trace/interface object containing already-computed Layer 2 component classifications**.

It is NOT:

```text
a new governance layer
a new environmental state vector
a replacement for E
a replacement for S
a second classifier
a new source of authority
```

It must not modify:

```text
E
ρ_{D,τ}
f
F_{D,τ}
```

The canonical state remains:

```text
S = F_{D,τ}(obs,v)
```

and Layer 2 remains solely responsible for determining `S`.

---

# 7. Component Fields

The proposed interface fields are:

```text
component_w_state
component_r_state
component_m_state
component_o_state
component_t_state
```

They represent the already-computed outcomes associated with:

```text
g_w
g_r
g_m
g_o
g_t
```

respectively.

Do not expose raw thresholds as Layer 3 rules.

Do not duplicate classifier formulas inside Layer 3 specification.

---

# 8. Interface Domain

Batch 4A proposed the Layer 3-visible domain:

```text
SAFE
CAUTION
EXCLUDED
```

with component-specific restrictions where applicable.

Document the exact domain carefully.

At minimum:

```text
component_w_state:
SAFE | CAUTION | EXCLUDED

component_r_state:
SAFE | CAUTION | EXCLUDED

component_m_state:
SAFE | CAUTION | EXCLUDED

component_o_state:
SAFE | CAUTION | EXCLUDED

component_t_state:
SAFE | EXCLUDED
```

However, verify this representation against the canonical exclusion semantics before writing it into authority.

Do not silently assume that every component is legally excludable merely because the generic interface contains `EXCLUDED`.

Preserve:

```text
D ⊆ C
t ∉ D
```

If canonical authority constrains which components may actually be excluded, document the distinction between:

```text
interface type domain
```

and:

```text
valid runtime values under the current configuration
```

Do not change `D`.

---

# 9. Critical Semantic Distinction: EXCLUDED vs SAFE

This distinction must be explicit.

An excluded component may be pinned SAFE for aggregation purposes, but:

```text
EXCLUDED ≠ observed SAFE
```

Therefore the interface may expose:

```text
component_m_state = EXCLUDED
```

while Layer 2 aggregation semantics internally treat the excluded component according to the existing exclusion rule.

Do NOT redefine the canonical aggregation semantics merely to accommodate `EXCLUDED`.

The trace/interface representation and aggregation contribution are different concepts.

State this clearly.

---

# 10. UNSAFE and Fault Semantics

Preserve:

```text
required nonexcluded invalid/absent/stale
→ ⊥
→ UNSAFE
```

and:

```text
any component UNSAFE
→ S = UNSAFE
→ G(UNSAFE)=0
→ Layer 3 reasoning not executed
```

Batch 4A concluded that `UNSAFE` and `FAULTED` component values are therefore not normally visible to the Layer 3 reasoning interface.

Document this carefully as an **execution-boundary consequence**, not as a redefinition of the component classifiers.

Do NOT claim:

```text
g_i can never return UNSAFE
```

Instead:

```text
UNSAFE may be produced in Layer 2,
but an episode with S=UNSAFE is gated off before Layer 3 reasoning.
```

Likewise, `FAULTED` is not a new component governance state.

Fault resolves through existing Layer 2 fail-safe semantics.

---

# 11. Time Component Protection

Preserve:

```text
g_t : ([0,24) × Date) ∪ {⊥}
      → {SAFE, UNSAFE}
```

No CAUTION.

Preserve:

```text
t ∉ D
```

Therefore under the current architecture:

```text
component_t_state
```

may be represented as SAFE at the Layer 3 reasoning boundary, while an UNSAFE `g_t` result causes global UNSAFE and gate-off.

If `EXCLUDED` is retained in the interface type for generic consistency, explicitly state that it is unreachable for `t` under the current configuration because:

```text
t ∉ D
```

Do not change g_t semantics.

Do not add solar calculations to Layer 3.

---

# 12. Marine Warning / Exclusion Protection

Replay remains:

```text
D = {m}
```

because no historical marine warning archive is available.

Therefore retrospective replay may expose:

```text
component_m_state = EXCLUDED
```

Do not reinterpret this as:

```text
marine condition SAFE
```

Do not claim absence of marine hazard.

Do not claim absence of marine warning events.

It means only that the component is excluded under the declared replay configuration.

---

# 13. Layer 3 Specification Amendment

Modify the minimum necessary section(s) of:

```text
publications/active/journal-1/layer3-prototype-specification.md
```

especially §7 / DecisionContext.

Formally specify the additional interface fields.

Define:

```text
ComponentStateTrace
```

or equivalent explicit fields in `DecisionContext`.

The specification must state that these values:

1. originate from Layer 2;
2. are already classified;
3. are read-only inputs to Layer 3;
4. must not be recomputed by Layer 3;
5. do not modify S;
6. do not select governance state;
7. may be used only as predicates within an already-selected RS(S);
8. do not override A_AI(S);
9. do not alter human authority.

---

# 14. Ordering / Execution Contract

Make the execution order explicit:

```text
1. Layer 2 resolves observations.
2. Layer 2 evaluates component gates.
3. Layer 2 determines S.
4. Layer 2 produces ComponentStateTrace from the same resolved component classifications.
5. Governance configuration G(S), A_AI(S) is established.
6. If G(S)=0:
      no Layer 3 reasoning.
7. Otherwise:
      Layer 3 receives S + ComponentStateTrace + other DecisionContext inputs.
8. RS(S) is selected.
9. Structural validation occurs.
10. Rule predicates may inspect ComponentStateTrace.
11. Reasoning produces AI(E).
12. Safety Dominance remains enforced.
```

Do not allow component states to independently select a different RS than S.

---

# 15. Consistency Invariant

Specify an interface consistency invariant.

At minimum:

```text
ComponentStateTrace must correspond to the same
Layer 2 evaluation episode that produced S.
```

Layer 3 must never receive:

```text
S from episode A
+
component states from episode B
```

Consider expressing:

```text
episode_id(S) = episode_id(ComponentStateTrace)
```

or equivalent implementation contract.

Do not invent cryptographic requirements unless already supported.

---

# 16. State Consistency

Specify that component-state trace and S must be semantically consistent.

Examples:

```text
S = SAFE
→ no active/nonexcluded component may be CAUTION or UNSAFE

S = CAUTION
→ at least one active/nonexcluded component is CAUTION
   and none is UNSAFE

S = UNSAFE
→ Layer 3 reasoning is gated off
```

Account correctly for `EXCLUDED`.

Do not treat EXCLUDED as observed SAFE.

Do not create a new governance state for inconsistency.

If inconsistent inputs are possible at implementation boundaries, classify the required handling as:

```text
configuration/interface fidelity failure
```

unless existing authority establishes another category.

Do not implement the handling yet.

---

# 17. Algorithm Specification Impact

Inspect:

```text
publications/active/journal-1/algorithm-specification.md
```

Determine whether the new interface requires a textual/interface amendment.

Do NOT automatically modify it.

Classify:

```text
NO_CHANGE_REQUIRED
```

or:

```text
BOUNDED_INTERFACE_SYNC_REQUIRED
```

with rationale.

If modification is required solely to keep Algorithm 3 input signature accurate, make only the minimal bounded sync and record it explicitly.

Do not change algorithm behaviour.

Do not change Algorithm 3 complexity claims.

Do not change Algorithm 4.

---

# 18. Evaluation Specification Impact

Inspect:

```text
publications/active/journal-1/evaluation-specification.md
```

Determine whether the interface amendment requires any textual consistency sync.

Prefer:

```text
NO_CHANGE_REQUIRED
```

if the existing F1–F3 definitions remain valid.

Do not redefine F1–F3.

Do not run F1–F3.

Do not change E1–E6.

Do not run E5.

---

# 19. Safety Dominance Protection

The amendment must preserve:

```text
AI(E) ⊆ A_AI(S)
```

ComponentStateTrace does not modify:

```text
A_AI(SAFE)
A_AI(CAUTION)
A_AI(UNSAFE)
```

Frozen:

```text
A_AI(SAFE) =
{Go, Delay, DepartureTime, Duration}

A_AI(CAUTION) =
{Go, Delay}

A_AI(UNSAFE) =
∅
```

Do not reinterpret these sets as guaranteed recommendations.

---

# 20. OPEN-L3-3 Protection

Preserve exactly:

```text
S = CAUTION ∧ Go ∈ AI(E)
→ Present(Go, caution_qualifier)
```

NOT:

```text
S = CAUTION
→ Go ∈ AI(E)
```

ComponentStateTrace must not create a CAUTION→Go rule.

---

# 21. R-SAFE-001 Protection

Do not add:

```text
component_w_state == SAFE
AND
component_r_state == SAFE
AND
component_m_state == SAFE
AND
component_o_state == SAFE
AND
component_t_state == SAFE
→ Go
```

This would reproduce the state-restatement rejected/deferred in Batch 4A.

Keep:

```text
R-SAFE-001 = DEFERRED
```

---

# 22. R-CAUTION-002/003/004

This task may document their **future executable representation**:

```text
R-CAUTION-002:
component_o_state == CAUTION

R-CAUTION-003:
component_r_state == CAUTION

R-CAUTION-004:
component_w_state == CAUTION
```

but MUST NOT insert these rules into:

```text
governance/canonical_rules.py
```

That belongs to Batch 4B-2.

---

# 23. R-CAUTION-001

Do not migrate:

```text
resolved_m == "advisory"
```

to:

```text
component_m_state == CAUTION
```

in this task.

Record migration as:

```text
FUTURE_CONSISTENCY_CONSIDERATION
```

only.

Do not assume equivalence beyond existing g_m authority.

---

# 24. Cause Taxonomy Protection

Preserve:

```text
reasons : Q → P({fault,hazard,policy})
```

as explanatory only.

ComponentStateTrace is NOT `reasons`.

Do not connect:

```text
reason == hazard
→ Delay
```

or any equivalent rule.

---

# 25. Human Authority

Preserve unconditional human authority.

The new interface must not introduce:

```text
automatic prohibition
automatic approval
human override restriction
```

No advisory generated by Layer 3 becomes mandatory merely because its predicate is based on a component state.

---

# 26. Complexity

Do not make new efficiency claims.

The interface amendment alone does not justify a new asymptotic result.

Preserve current bounded complexity authority unless an unavoidable signature-only wording sync is required.

E5 latency/performance remains OPEN/not run.

No X ms threshold.

---

# 27. Required Canonical Change Record

Create:

```text
data/journal1-layer3-prototype/batch4b1-interface-amendment/
    canonical-change-record.json
```

At minimum record:

```text
task
branch
HEAD_before

files_modified

canonical_file_modified
canonical_change_scope
canonical_change_reason

appendix_c_modified
appendix_c_change_required

scientific_architecture_changed
governance_semantics_changed
safety_dominance_changed

component_state_interface_added

R_SAFE_001_status
R_CAUTION_002_status
R_CAUTION_003_status
R_CAUTION_004_status

implementation_performed
F1_F3_run
E5_run
```

Expected if successful:

```text
appendix_c_modified = false
scientific_architecture_changed = false
governance_semantics_changed = false
safety_dominance_changed = false

implementation_performed = false
F1_F3_run = false
E5_run = false
```

Do not force these values if evidence contradicts them.

---

# 28. Required Interface Contract Artefact

Create:

```text
component-state-interface-contract.md
```

It must include:

```text
Purpose
Authority
Producer
Consumer
Fields
Domains
Exclusion semantics
Fault semantics
UNSAFE gate-off relationship
Episode consistency invariant
S/component-state consistency invariant
Read-only requirement
No Layer 2 recomputation requirement
Safety Dominance relationship
Human-authority relationship
Future rule mappings
Explicit non-goals
```

---

# 29. Required Impact Matrix

Create:

```text
interface-impact-matrix.csv
```

Rows at minimum:

```text
appendix-c-formalisation.md
architecture-illustration.md
layer3-prototype-specification.md
algorithm-specification.md
evaluation-specification.md
governance/rule.py
governance/rule_set_provider.py
governance/reasoning_episode.py
governance/canonical_rules.py
```

Columns:

```text
artifact
authority_level
change_required
changed_in_batch4b1
change_type
reason
semantic_effect
deferred_to_batch4b2
```

All implementation files should normally show:

```text
changed_in_batch4b1 = false
deferred_to_batch4b2 = true
```

where applicable.

---

# 30. Required Verification

Create:

```text
verification.json
```

Verify at minimum:

```text
Batch4A_authority_preserved

ModelB_preserved

architecture_illustration_interface_updated

appendix_c_unchanged

formal_E_unchanged

rho_unchanged

f_unchanged

F_unchanged

g_w_unchanged

g_r_unchanged

g_m_unchanged

g_o_unchanged

g_t_unchanged

G_unchanged

A_AI_unchanged

Safety_Dominance_unchanged

human_authority_unchanged

ComponentStateTrace_defined

component_states_are_layer2_outputs

component_states_read_only_in_layer3

no_layer2_recomputation_in_layer3

EXCLUDED_distinct_from_SAFE

fault_semantics_preserved

UNSAFE_gateoff_preserved

episode_consistency_defined

state_trace_consistency_defined

R_SAFE_001_remains_deferred

R_CAUTION_002_not_implemented

R_CAUTION_003_not_implemented

R_CAUTION_004_not_implemented

R_CAUTION_001_not_migrated

OPEN_L3_3_preserved

OPEN_L3_1C_preserved

OPEN_L3_1D_preserved

GAP_03_preserved

implementation_code_unchanged

F1_F3_not_run

E5_not_run
```

Use:

```text
PASS
FAIL
OPEN
```

Report exact totals.

Protection checks such as:

```text
F1_F3_not_run
E5_not_run
implementation_code_unchanged
```

should be PASS when the prohibited action was correctly not performed.

Do not mark successful absence checks OPEN.

---

# 31. Required Integrity Record

Create:

```text
integrity.json
```

Record before/after hashes for at least:

```text
docs/canonical/appendix-c-formalisation.md
docs/canonical/architecture-illustration.md
publications/active/journal-1/layer3-prototype-specification.md
publications/active/journal-1/algorithm-specification.md
publications/active/journal-1/evaluation-specification.md
governance/canonical_rules.py
governance/rule_set_provider.py
governance/reasoning_episode.py
```

Expected pattern:

```text
architecture-illustration.md
→ CHANGED intentionally

layer3-prototype-specification.md
→ CHANGED intentionally

appendix-c-formalisation.md
→ UNCHANGED

governance/*
→ UNCHANGED
```

Algorithm/evaluation specification may be changed only if the impact analysis proves a minimal bounded sync is required.

---

# 32. Required Report

Create:

```text
report.md
```

Report:

1. Verdict
2. Branch / HEAD
3. Authorities inspected
4. Batch 4A decision inherited
5. Exact canonical amendment
6. Exact specification amendment
7. ComponentStateTrace definition
8. Exclusion semantics
9. Fault semantics
10. UNSAFE boundary semantics
11. S/component consistency invariant
12. Algorithm-specification impact
13. Evaluation-specification impact
14. Safety Dominance impact
15. Human-authority impact
16. R-SAFE-001 status
17. R-CAUTION-001 status
18. R-CAUTION-002/003/004 status
19. Protected OPEN items
20. Implementation status
21. F1–F3 status
22. E5 status
23. Integrity results
24. Verification PASS/FAIL/OPEN totals
25. Files modified
26. Files created
27. Remaining blockers
28. Exact closure line

---

# 33. Stop Conditions

STOP and report OPEN/FAIL if the amendment requires any of the following:

```text
changing Appendix C formal E

changing ρ_{D,τ}

changing f or F_{D,τ}

changing g_w/g_r/g_m/g_o/g_t semantics

changing G(S)

changing A_AI(S)

changing Safety Dominance

changing human authority

turning reasons into rule authority

implementing SAFE→Go

creating CAUTION→Go

reimplementing Layer 2 classifiers in Layer 3

inventing new thresholds

inventing new advisory evidence

implementing executable rules

running F1–F3

running E5
```

Do not repair such a conflict by silently expanding scope.

---

# 34. Success Criteria

Batch 4B-1 succeeds only if:

```text
ComponentStateTrace is explicitly documented
AND
architecture-illustration.md accurately reflects the interface
AND
layer3-prototype-specification.md defines the interface contract
AND
Appendix C remains unchanged
AND
scientific architecture remains unchanged
AND
governance semantics remain unchanged
AND
implementation code remains unchanged
AND
R-SAFE-001 remains deferred
AND
no new executable rule is added
AND
F1–F3 are not run
AND
E5 is not run
```

---

# 35. Batch 4B-2 Readiness

At the end classify:

```text
BATCH4B2_IMPLEMENTATION_READY = true | false
```

Set TRUE only if:

```text
canonical interface amendment accepted
specification interface amendment accepted
no unresolved semantic contradiction
no implementation occurred prematurely
```

This flag authorises only the **next bounded implementation task**.

It does NOT authorise:

```text
F1–F3
E5
R-SAFE-001
CAUTION→Go
DepartureTime
Duration
```

---

# 36. Closure Line

Only if all Batch 4B-1 criteria pass:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 4B-1 CLOSED —
COMPONENT-STATE INTERFACE CANONICALLY DOCUMENTED AND SPECIFIED
```

Otherwise:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 4B-1 REMAINS OPEN —
<EXACT BLOCKER>
```

---

# 37. Required Final Response

Return:

1. Verdict
2. Branch and HEAD
3. Batch 4A authority inherited
4. Canonical files inspected
5. Canonical file modified
6. Exact canonical amendment
7. Specification files modified
8. ComponentStateTrace contract
9. EXCLUDED semantics
10. fault/UNSAFE semantics
11. episode consistency invariant
12. S/component consistency invariant
13. Algorithm specification impact
14. Evaluation specification impact
15. Appendix C integrity
16. Safety Dominance result
17. Human authority result
18. R-SAFE-001 status
19. R-CAUTION-001 status
20. R-CAUTION-002/003/004 status
21. implementation-code integrity
22. F1–F3 status
23. E5 status
24. verification PASS/FAIL/OPEN counts
25. files modified
26. files created
27. remaining OPEN items
28. BATCH4B2_IMPLEMENTATION_READY
29. exact closure/status line

Do NOT start Batch 4B-2 automatically.
