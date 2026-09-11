# Journal 1 Layer 3 Prototype

## Batch 4A — Executable Rule-Set Authority Resolution

### Task Type

Bounded scientific-to-executable specification task.

This task occurs **after Batch 3 core-engine implementation** and **before F1–F3 fidelity evaluation**.

The objective is to determine whether the scientifically admitted but currently deferred Batch 2 rules can be represented as executable Layer 3 `ConditionPredicate` structures without:

* inventing new scientific rules;
* inventing thresholds;
* duplicating Layer 2 classification logic inside Layer 3;
* weakening provenance;
* changing the architecture;
* converting admissibility into rule existence.

This is **not an implementation task** unless explicitly authorised by the outcome of this specification.

---

# 1. Branch

Create:

```text
design/journal1-layer3-executable-rule-authority
```

Record before work:

```text
current branch
HEAD commit
working-tree status
Batch 3 closure commit/hash
```

Do not modify Batch 3 implementation during the scientific analysis.

---

# 2. Why This Task Is Required

The Batch 3 executable repository currently contains only:

```text
R-CAUTION-001
```

The following scientifically admitted Batch 2 candidates remain deferred:

```text
R-SAFE-001
R-CAUTION-002
R-CAUTION-003
R-CAUTION-004
```

Their current antecedents are expressed using Layer 2 classifier notation such as:

```text
g_w(w) == CAUTION
g_r(r, κ) == CAUTION
g_o(o,v) == CAUTION
g_t(t,date) == SAFE
```

The Batch 3 engine, however, consumes executable predicates of the form:

```text
ConditionPredicate(
    variable,
    operator,
    value
)
```

The scientific question is therefore:

> Can the already-admitted rule antecedents be represented executably without Layer 3 re-performing Layer 2 classification or introducing unsupported scientific semantics?

Do not assume the answer is YES.

---

# 3. Primary Authorities

Inspect at minimum:

```text
publications/active/journal-1/layer3-prototype-specification.md
publications/active/journal-1/algorithm-specification.md
publications/active/journal-1/evaluation-specification.md

data/journal1-layer3-prototype/
data/journal1-layer3-prototype/open-l3-2-resolution/
data/journal1-layer3-prototype/open-l3-3-resolution/
data/journal1-layer3-prototype/batch3-core-engine/
```

Inspect the actual Batch 3 implementation:

```text
governance/canonical_rules.py
governance/rule.py
governance/rule_set_provider.py
governance/reasoning_engine.py
governance/reasoning_episode.py
```

Also inspect the authoritative Layer 2 formalisation necessary to understand the boundary.

Do not modify canonical Layer 2 authority.

---

# 4. Frozen Architecture Boundary

Preserve:

```text
Layer 2:
obs
→ ρ_{D,τ}
→ resolved environmental state
→ component gates
→ S ∈ {SAFE, CAUTION, UNSAFE}
```

and:

```text
Layer 3:
S + DecisionContext
→ RS(S)
→ governed reasoning
→ AI(E)
```

Layer 3 receives `S`.

Layer 3 must not become a second implementation of:

```text
f
F_{D,τ}
g_w
g_r
g_m
g_o
g_t
```

Do not solve the deferred-rule problem merely by copying Layer 2 thresholds into Layer 3.

---

# 5. Rules Under Review

Review individually:

```text
R-SAFE-001
R-CAUTION-002
R-CAUTION-003
R-CAUTION-004
```

Do not reopen the scientific evidence supporting their advisory mappings unless a genuine contradiction is discovered.

The question is narrower:

```text
Is the existing antecedent executable under the current
Layer 2 → Layer 3 interface?
```

For every rule assign one of:

```text
DIRECTLY_EXECUTABLE
EXECUTABLE_WITH_INTERFACE_EXTENSION
EXECUTABLE_WITH_DERIVED_CONTEXT
NOT_EXECUTABLE_WITHOUT_LAYER2_DUPLICATION
SCIENTIFIC_AUTHORITY_INSUFFICIENT
```

Define these categories explicitly before using them.

---

# 6. Critical Design Alternatives

Evaluate at least these alternatives.

## Model A — Raw-value predicate expansion

Example:

```text
g_r(r,κ) == CAUTION
```

becomes something similar to:

```text
resolved_r_rate > 10
AND
resolved_r_rate <= 20
AND
resolved_r_kappa == 0
```

Assess whether this is legitimate executable elaboration or impermissible duplication of Layer 2 classifier semantics.

Do not accept it merely because the numerical transformation is logically possible.

---

## Model B — Pass Layer 2 component states into DecisionContext

Example:

```text
DecisionContext:
    ...
    component_w_state
    component_r_state
    component_m_state
    component_o_state
    component_t_state
```

Then Layer 3 rule antecedents become:

```text
component_r_state == CAUTION
component_o_state == CAUTION
component_t_state == SAFE
```

Evaluate whether this provides a cleaner architecture:

```text
Layer 2 computes component classifications once
↓
Layer 3 consumes their resolved classifications
```

rather than Layer 3 recomputing them.

Determine whether this constitutes:

```text
implementation-level interface enrichment
```

or:

```text
scientific architecture change
```

Do not assume either conclusion.

---

## Model C — Pass explanatory cause/reason outputs

Evaluate whether the existing explanatory taxonomy:

```text
reasons : Q → P({fault,hazard,policy})
```

or any more granular component provenance can legitimately support Layer 3 rule selection.

Remember:

```text
reasons are explanatory only
```

and must never govern.

Therefore reject this model if it would turn explanatory provenance into decision authority.

---

## Model D — Keep rules deferred

It is scientifically acceptable to conclude that one or more rules should remain non-executable for Journal 1.

Do not force population merely to improve replay activation counts.

---

# 7. Preferred Architectural Question

Pay particular attention to whether Model B creates the cleanest separation:

```text
Layer 2 output:
S
+
component-state trace
```

where:

```text
component-state trace =
{
    w_state,
    r_state,
    m_state,
    o_state,
    t_state
}
```

and Layer 3 uses these values only as already-computed facts.

The key distinction to establish is:

```text
consuming Layer 2 component-state outputs
```

versus:

```text
recomputing Layer 2 component-state outputs
```

If the former is defensible, determine the exact interface contract required.

Do not implement it yet.

---

# 8. R-SAFE-001

Current conceptual antecedent:

```text
all(
    g_w(w) == SAFE,
    g_r(r,κ) == SAFE,
    g_m(m) == SAFE,
    g_o(o,v) == SAFE,
    g_t(t,date) == SAFE
)
```

Determine whether this rule is actually scientifically distinct from merely observing:

```text
S == SAFE
```

Given worst-case aggregation, inspect whether:

```text
S == SAFE
```

already logically implies all non-excluded component gates are SAFE.

If so, determine whether R-SAFE-001 is:

```text
a meaningful Layer 3 environmental rule
```

or effectively:

```text
SAFE → Go
```

which Batch 2 explicitly sought to avoid treating as an automatic state-to-advisory mapping.

This is a potentially important issue.

Do not silently make R-SAFE-001 executable.

If the rule collapses to state restatement, report that explicitly.

---

# 9. R-CAUTION-002

Current antecedent:

```text
g_o(o,v) == CAUTION
```

Assess:

* whether Layer 3 may consume an already-computed `o_state`;
* whether expanding vessel-specific wave thresholds duplicates `g_o`;
* whether the rule remains scientifically identical after executable representation;
* whether vessel category remains necessary if `o_state` is already supplied.

Do not create per-vessel rules merely for implementation convenience unless scientifically and architecturally justified.

---

# 10. R-CAUTION-003

Current antecedent:

```text
g_r(r,κ) == CAUTION
```

Assess whether executable expansion into rainfall thresholds would improperly duplicate `g_r`.

Prefer evaluating whether Layer 2 should expose:

```text
r_state
```

as an already-computed component state.

Preserve the existing two-input rainfall semantics.

Do not reinterpret κ.

---

# 11. R-CAUTION-004

Current antecedent:

```text
g_w(w) == CAUTION
```

Assess the same boundary issue.

Do not copy:

```text
21.6
27.0
```

into Layer 3 merely because those thresholds are canonical.

Canonical availability does not automatically justify classifier duplication.

---

# 12. Marine Warning Rule

Do not reopen:

```text
R-CAUTION-001
```

unless this analysis reveals an actual interface inconsistency.

It is already executable as:

```text
resolved_m == "advisory"
```

However, explicitly compare its structure against the proposed component-state interface.

Ask whether consistency would eventually favour:

```text
m_state == CAUTION
```

instead.

Do not change the existing implementation in this task.

Record the result as a future migration consideration if applicable.

---

# 13. Exclusion Semantics

Any proposed component-state interface must preserve:

```text
D ⊆ C
t ∉ D
```

and the existing exclusion-before-fault semantics.

Do not invent a component-state representation that loses the distinction between:

```text
excluded
faulted
valid SAFE
valid CAUTION
valid UNSAFE
```

unless the canonical architecture establishes that such distinction is unnecessary at the Layer 3 boundary.

Explicitly analyse this.

---

# 14. Missing/Fault Semantics

Remember:

```text
required nonexcluded invalid/absent/stale
→ ⊥
→ UNSAFE
```

Layer 3 must not reinterpret a Layer 2 fault as an ordinary environmental predicate failure.

Determine whether component-state outputs require a representation such as:

```text
SAFE
CAUTION
UNSAFE
EXCLUDED
```

or whether `S=UNSAFE` short-circuit makes some distinctions unreachable to Layer 3.

Do not invent new governance states.

---

# 15. Time Component

R-SAFE-001 references:

```text
g_t(t,date)
```

Layer 3 must not implement NOAA solar calculations.

If component-state passing is adopted, Layer 3 may potentially consume:

```text
t_state
```

already computed by Layer 2.

Assess this explicitly.

No solar calculation belongs in Layer 3.

---

# 16. Cause Taxonomy Protection

Preserve:

```text
reasons
```

as explanatory only.

Do not implement:

```text
reason == hazard
→ Delay
```

or equivalent.

Do not use cause taxonomy as a replacement for component-state outputs unless existing authority explicitly permits it.

---

# 17. Recommendation Admissibility Protection

Preserve:

```text
A_AI(SAFE)    = FULL
A_AI(CAUTION) = {Go, Delay}
A_AI(UNSAFE)  = ∅
```

But remember:

```text
admissible recommendation
≠
existing recommendation
≠
scientifically supported rule
```

This task must not create rules simply to fill every element of `A_AI`.

---

# 18. OPEN-L3-3 Protection

Preserve Resolution B exactly:

```text
S = CAUTION ∧ Go ∈ AI(E)
→ Present(Go, caution_qualifier)
```

not:

```text
S = CAUTION
→ Go ∈ AI(E)
```

No CAUTION→Go rule may be introduced.

---

# 19. OPEN-L3-1C / OPEN-L3-1D

Keep:

```text
OPEN-L3-1C = OPEN
OPEN-L3-1D = OPEN
```

This task does not search for new evidence for:

```text
DepartureTime
Duration
```

Do not populate those recommendation types.

---

# 20. GAP-03

Keep:

```text
GAP-03 = OPEN
```

Do not solve it through interface engineering.

An implementation interface cannot substitute for missing scientific advisory evidence.

---

# 21. F1–F3

Do not run F1–F3.

This task exists precisely to establish the executable rule-set authority before fidelity evaluation.

Do not report:

```text
F1 PASS
F2 PASS
F3 PASS
```

---

# 22. E5

Do not run E5 latency/performance evaluation.

Do not create or infer a latency threshold.

---

# 23. Required Rule Authority Matrix

Create:

```text
data/journal1-layer3-prototype/batch4a-executable-rule-authority/
    rule-executability-matrix.csv
```

At minimum columns:

```text
rule_id
applicable_state
conclusion_type
batch2_antecedent
current_executable_status
candidate_representation
requires_layer2_reimplementation
requires_interface_extension
requires_new_scientific_authority
state_restatement_risk
recommended_disposition
rationale
authority_reference
```

One row per:

```text
R-SAFE-001
R-CAUTION-001
R-CAUTION-002
R-CAUTION-003
R-CAUTION-004
```

---

# 24. Required Interface Candidate Matrix

Create:

```text
interface-candidate-matrix.csv
```

Compare at least:

```text
Model A — raw-value predicate expansion
Model B — Layer 2 component-state interface
Model C — explanatory/cause-based interface
Model D — keep deferred
```

Columns should include:

```text
model
description
preserves_layer_boundary
duplicates_layer2_logic
changes_scientific_semantics
supports_existing_rules
preserves_exclusion_semantics
preserves_fault_semantics
implementation_complexity
scientific_risk
decision
rationale
```

---

# 25. Required Formal Boundary Analysis

Create:

```text
layer2-layer3-interface-analysis.md
```

Explicitly answer:

### Q1

What information is Layer 2 formally allowed to expose to Layer 3?

### Q2

Does exposing component-state outputs change the scientific architecture or merely make an already-existing internal result explicit?

### Q3

Would Layer 3 consumption of component states violate:

```text
S = max-severity(...)
```

or Safety Dominance?

### Q4

Does R-SAFE-001 collapse logically into:

```text
S == SAFE → Go
```

under the current formalisation?

### Q5

Can R-CAUTION-002/003/004 be implemented without copying `g_o`, `g_r`, and `g_w` logic into Layer 3?

### Q6

How are excluded/faulted components represented at the interface?

### Q7

Would the proposed interface change Algorithm 3 complexity?

### Q8

Would any proposal require canonical architecture modification?

---

# 26. R-SAFE-001 Special Gate

Treat R-SAFE-001 separately.

Before recommending implementation, prove or refute:

```text
S = SAFE
⇔
all active/nonexcluded component states are SAFE
```

under the actual canonical semantics.

Then determine whether:

```text
R-SAFE-001 antecedent
```

contains information beyond:

```text
S = SAFE
```

If not, classify the rule as potentially:

```text
STATE_RESTATEMENT
```

and do not automatically implement it.

This finding may require a bounded scientific decision later.

---

# 27. Preferred Outcome If Supported

If the evidence supports Model B, specify—but do not yet implement—an interface such as:

```text
ComponentStateTrace:
    w_state
    r_state
    m_state
    o_state
    t_state
```

with values grounded in existing Layer 2 outputs.

Then executable Layer 3 predicates could conceptually become:

```text
R-CAUTION-002:
    o_state == CAUTION

R-CAUTION-003:
    r_state == CAUTION

R-CAUTION-004:
    w_state == CAUTION
```

This is only an example.

Do not adopt it unless the analysis establishes that component states are legitimate Layer 2 outputs and that exposing them does not change scientific semantics.

---

# 28. Do Not Modify Implementation Yet

Do not change:

```text
governance/canonical_rules.py
governance/reasoning_engine.py
governance/reasoning_episode.py
governance/rule_set_provider.py
governance/rule.py
```

in Batch 4A.

This is an authority-resolution task.

Implementation must be a separate Batch 4B only after the interface decision passes independent review.

---

# 29. Protected Canonical Files

Do not modify:

```text
docs/canonical/appendix-c-formalisation.md
docs/canonical/architecture-illustration.md
```

If the preferred interface would require canonical modification:

```text
STOP
```

and classify:

```text
CANONICAL_CHANGE_REQUIRED
```

Do not perform that change in this task.

---

# 30. Evidence Directory

Create:

```text
data/journal1-layer3-prototype/batch4a-executable-rule-authority/
```

At minimum:

```text
rule-executability-matrix.csv
interface-candidate-matrix.csv
layer2-layer3-interface-analysis.md
resolution.json
verification.json
report.md
```

---

# 31. resolution.json

Record at minimum:

```text
status
selected_interface_model
decision_basis
rule_dispositions
R_SAFE_001_state_restatement_result
canonical_change_required
implementation_authorised
F1_F3_ready
remaining_open_items
```

Do not set:

```text
implementation_authorised = true
```

unless the executable mapping is fully justified.

Do not set:

```text
F1_F3_ready = true
```

merely because Batch 3 engine works.

---

# 32. Verification

Verify at minimum:

```text
all_five_batch2_rules_classified

no_new_rule_invented

no_new_threshold_invented

no_layer2_classifier_duplicated

R_SAFE_001_state_restatement_tested

component_state_interface_assessed

exclusion_semantics_preserved

fault_semantics_preserved

g_t_not_reimplemented

g_o_not_reimplemented

g_r_not_reimplemented

g_w_not_reimplemented

cause_taxonomy_remains_explanatory

A_AI_not_treated_as_rule_existence

OPEN_L3_3_resolution_B_preserved

no_CAUTION_Go_rule_created

OPEN_L3_1C_preserved

OPEN_L3_1D_preserved

GAP_03_preserved

Batch3_code_unchanged

canonical_files_unchanged

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

---

# 33. Stop Conditions

STOP and report OPEN if:

* executable representation requires Layer 3 to duplicate a Layer 2 classifier;
* component-state exposure requires changing the canonical architecture;
* R-SAFE-001 is shown to collapse into an unsupported automatic SAFE→Go mapping;
* rule antecedent authority is insufficient;
* exclusion/fault semantics cannot be preserved;
* a rule requires new scientific evidence;
* interface enrichment changes the meaning of S or Safety Dominance.

Do not force closure to increase the number of executable rules.

A scientifically defensible deferred rule is preferable to an unsupported executable rule.

---

# 34. Possible Outcomes

### Outcome A — Model B accepted

```text
Layer 2 component-state interface accepted
R-CAUTION-002/003/004 executable in principle
R-SAFE-001 separately resolved
Batch 4B implementation authorised
```

### Outcome B — Partial acceptance

Example:

```text
some rules executable
some remain deferred
```

This is acceptable.

### Outcome C — All remain deferred

This is also acceptable if required by scientific provenance.

Then F1–F3 must be designed around the actually executable rule set and its limitations must be reported.

### Outcome D — Canonical change required

STOP.

Do not modify canonical authority in this task.

---

# 35. Closure Line

Only if the authority question is fully resolved use:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 4A CLOSED —
EXECUTABLE RULE-SET AUTHORITY AND LAYER-BOUNDARY INTERFACE RESOLVED
```

If unresolved:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 4A REMAINS OPEN —
<EXACT BLOCKER>
```

---

# 36. Required Final Response

Return:

1. Verdict
2. Branch and HEAD
3. Authorities inspected
4. Current executable-rule state
5. Model A assessment
6. Model B assessment
7. Model C assessment
8. Model D assessment
9. Selected interface model
10. R-SAFE-001 state-restatement analysis
11. R-CAUTION-001 disposition
12. R-CAUTION-002 disposition
13. R-CAUTION-003 disposition
14. R-CAUTION-004 disposition
15. Exclusion/fault semantics result
16. Layer 2 / Layer 3 boundary result
17. Whether canonical change is required
18. Whether Batch 4B implementation is authorised
19. Whether F1–F3 are ready
20. Verification PASS / FAIL / OPEN counts
21. Files created
22. Files modified
23. Protected OPEN items
24. Remaining blockers
25. Exact closure/status line

Do not implement Batch 4B automatically.
Do not run F1–F3 automatically.
