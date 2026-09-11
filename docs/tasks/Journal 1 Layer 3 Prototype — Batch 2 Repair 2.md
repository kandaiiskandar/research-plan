# Journal 1 Layer 3 Prototype — Batch 2

## FINAL REPAIR: Evidence-Mapping Semantics, CAUTION-Go Authority, and Artefact Integrity

### Current independent-review verdict

Batch 2 is **NOT accepted as closed**.

Current verdict:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 2 REMAINS OPEN —
ADVISORY MAPPING EVIDENCE AND ARTEFACT INTEGRITY REPAIR INCOMPLETE
```

This is a bounded repair.

Do NOT start Batch 3.
Do NOT implement the Layer 3 engine.
Do NOT run F1–F3.
Do NOT run E5.
Do NOT invent new scientific thresholds.
Do NOT invent new recommendation types.
Do NOT modify protected canonical scientific state merely to obtain closure.
Do NOT perform a broad repository consistency audit.

Repair only the defects identified below.

---

# 1. Files requiring repair

At minimum inspect and repair:

```text
publications/active/journal-1/layer3-prototype-specification.md

data/journal1-layer3-prototype/
├── rule-candidate-register-batch2.csv
├── rule-evidence-matrix-batch2.csv
├── semantic-verification-batch2.json
├── scientific-gap-register-batch2.csv
├── closure-batch2.json
└── report-batch2.md
```

Inspect related Batch 2 artefacts where necessary for consistency:

```text
recommendation-semantics-batch2.csv
rule-conflict-analysis-batch2.csv
change-map-batch2.csv
```

Do not rewrite unaffected scientific content.

---

# 2. Repair CSV integrity first

This is a hard prerequisite.

The previous repair still produced malformed CSV files.

Do not assume a required fixed number of columns from the task prompt.

Instead:

```python
expected_width = len(header)
```

must be derived from the actual written CSV header.

For each CSV:

```text
rule-candidate-register-batch2.csv
rule-evidence-matrix-batch2.csv
```

perform an actual standards-compliant parse using Python's:

```python
csv.reader
```

or:

```python
csv.DictReader
```

after writing the final file.

Do not validate by visual inspection.

---

# 3. Mandatory CSV parser verification

Execute an equivalent real check:

```python
import csv
from pathlib import Path

paths = [
    Path("data/journal1-layer3-prototype/rule-candidate-register-batch2.csv"),
    Path("data/journal1-layer3-prototype/rule-evidence-matrix-batch2.csv"),
]

for path in paths:
    with path.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))

    assert rows, f"{path}: empty file"

    header = rows[0]
    expected_width = len(header)

    assert expected_width > 0

    for line_no, row in enumerate(rows[1:], start=2):
        assert len(row) == expected_width, (
            f"{path}:{line_no}: "
            f"expected {expected_width} columns, got {len(row)}"
        )

    print(
        path,
        "header_width=", expected_width,
        "data_rows=", len(rows) - 1,
        "PASS"
    )
```

If using `DictReader`, also verify:

```python
row.get(None) is None
```

for every row.

No overflow columns are permitted.

No under-width rows are permitted.

---

# 4. CSV repair must preserve scientific content

When repairing quoting and delimiters:

Do NOT:

```text
drop text
truncate limitations
merge evidence fields accidentally
move scientific claims into the wrong column
delete rejected candidates
delete inference notes
```

If a cell contains commas, quote it correctly.

If a cell contains quotation marks, escape them according to CSV rules.

If multiline fields exist, ensure they remain valid CSV fields.

After structural repair, compare each rule/source against the maintained specification to ensure semantic content remains aligned.

Record:

```text
csv_content_preservation = PASS / FAIL
```

---

# 5. Separate environmental-premise evidence from advisory-action evidence

This is the central scientific repair.

For every candidate rule distinguish:

```text
P_ENV:
Evidence supporting the environmental or operational premise.

P_ADV:
Evidence supporting the specific advisory mapping.
```

For example:

```text
P_ENV:
MET Category 1 conditions are dangerous to small boats.

P_ADV:
When Category 1 is active, the AI should recommend Delay.
```

These are NOT the same proposition.

Formally preserve:

```text
environmental concern
≠
specific advisory action
```

and:

```text
evidence(condition is concerning)
does not automatically entail
evidence(condition → Delay)
```

---

# 6. Update evidence representation

Modify the evidence matrix or candidate register so the distinction is explicit.

Use fields equivalent to:

```text
premise_support
premise_support_level

advisory_mapping_support
advisory_mapping_support_level

mapping_inference_required

mapping_bridge_source

mapping_limitation
```

Exact column names may differ if the existing schema has a better representation.

The important requirement is that an auditor can determine separately:

```text
What evidence supports the condition?

What evidence supports the recommendation?

What inference connects them?
```

Do not hide this distinction inside a generic `evidence_level` field.

---

# 7. Reassess R-CAUTION-001

Current candidate:

```text
R-CAUTION-001

IF m == advisory
THEN Delay
```

Current treatment:

```text
SUPPORTED
Level A
```

This must be reassessed.

MET Malaysia Category 1 wording:

```text
"berbahaya kepada bot-bot kecil"
```

is strong Level-A authority for the environmental/operational premise.

Therefore it may support:

```text
P_ENV = Level A
```

But determine whether the actual MET authority explicitly states an action equivalent to:

```text
delay departure
defer departure
postpone departure
wait before departure
do not depart until conditions improve
```

Do not infer this from "dangerous to small boats" alone.

---

# 8. Required R-CAUTION-001 classification logic

If MET explicitly instructs delaying/defering/postponing departure:

```text
P_ENV = Level A
P_ADV = Level A
```

and `SUPPORTED` may be defensible.

If MET establishes danger to small boats but does NOT explicitly prescribe Delay:

```text
P_ENV = Level A
P_ADV = lower-level / inferred
mapping_inference_required = YES
```

Then the complete rule:

```text
m == advisory → Delay
```

must NOT be described simply as:

```text
SUPPORTED — Level A
```

unless an independent evidence bridge warrants that mapping.

A likely bounded status may be:

```text
CONDITIONALLY SUPPORTED
```

but determine this from the evidence.

Do not downgrade MET's authority.

Downgrade only the unsupported strength of the:

```text
condition → advisory action
```

mapping.

---

# 9. Reassess R-SAFE-001 correctly

Current rule:

```text
IF  g_w(w) == SAFE
AND g_r(r,κ) == SAFE
AND g_m(m) == SAFE
AND g_o(o,v) == SAFE
AND g_t(t,date) == SAFE
THEN Go
```

Under canonical max-severity aggregation:

```text
all five components SAFE
⇔
S == SAFE
```

Therefore:

```text
R-SAFE-001 antecedent
```

is functionally equivalent to:

```text
S == SAFE
```

Do not claim that expressing SAFE as its component conjunction removes classifier duplication.

It does not.

---

# 10. Correct scientific interpretation of R-SAFE-001

The external empirical evidence may support a broader relationship such as:

```text
favourable environmental/operational conditions
→ fishers tend to proceed
```

But unless the studies actually evaluated:

```text
canonical wind threshold
canonical rain threshold
canonical marine-warning condition
canonical vessel-conditioned wave threshold
canonical astronomical daylight gate
```

simultaneously, they do NOT independently validate the exact canonical five-component antecedent.

Therefore represent R-SAFE-001 as:

```text
canonical antecedent:
architecture-level operationalisation

behavioural mapping:
independently informed by fisher studies

local validity:
not yet established
```

A status such as:

```text
CONDITIONALLY SUPPORTED
```

may remain appropriate.

But its limitation must explicitly state that the empirical studies support the broader behavioural relationship, not the exact canonical conjunction.

---

# 11. Reconcile R-SAFE-001 with R-REJ-001

Current:

```text
R-REJ-001:
IF S == SAFE THEN Go
```

is rejected.

But R-SAFE-001 has an equivalent antecedent.

Do not maintain a logically inconsistent distinction where:

```text
S == SAFE → Go
```

is rejected purely as state restatement,

while:

```text
all component gates SAFE → Go
```

is accepted merely because the same state is written in expanded form.

Instead explain that the difference, if retained, comes from the **evidentiary rationale for the Go mapping**, not from antecedent structure.

Possible framing:

```text
R-REJ-001 rejects an architecture-only derivation:
SAFE → Go solely because Go ∈ A_AI(SAFE).

R-SAFE-001 is retained only as a conditionally supported candidate
because independent behavioural evidence provides a bounded empirical
bridge from favourable operating conditions to proceeding behaviour.

Its antecedent nevertheless remains functionally equivalent to SAFE
classification and therefore carries classifier-duplication limitations.
```

Do not claim threshold novelty.

---

# 12. Reassess R-CAUTION-002

Current:

```text
IF g_o(o,v) == CAUTION
THEN Delay
```

Separate:

```text
wave condition
→ operability/departure concern
```

from:

```text
wave condition
→ Delay recommendation
```

For EV-05 and EV-06 determine exactly whether they support:

```text
departure restriction
operability limitation
seakeeping concern
capsizing concern
```

and whether that evidence directly entails:

```text
Delay
```

If not:

```text
mapping_inference_required = YES
```

and preserve `CONDITIONALLY SUPPORTED` only with explicit bounded inference.

---

# 13. Reassess R-CAUTION-003

Current:

```text
IF g_r(r,κ) == CAUTION
THEN Delay
```

Do not equate:

```text
reduced trip frequency
near-shore operations
shortened trips
restricted operations
```

with:

```text
Delay
```

without an explicit inference bridge.

Determine separately whether Rahim et al. supports:

```text
heavy rainfall → changed/restricted fishing behaviour
```

versus:

```text
heavy rainfall → delay departure
```

If only the first is supported:

```text
P_ENV / behavioural premise = supported
P_ADV = inferred
```

and document the adaptation.

---

# 14. Reassess R-CAUTION-004

Current:

```text
IF g_w(w) == CAUTION
THEN Delay
```

Do not equate:

```text
increased accident-risk perception
cautious-go
restricted operations
heavy-weather concern
```

with:

```text
Delay
```

without an explicit bridge.

Record the mapping as inferential if necessary.

Do not overstate the exact 21.6–27.0 knot band as independently validated by studies unless they actually validate those canonical thresholds.

---

# 15. EV-08 must not be counted as independent scientific evidence

EV-08:

```text
dataset-label-derivation.md
```

is an internal project artefact synthesising:

```text
EV-02
EV-03
EV-04
```

It may be used as:

```text
design lineage
project interpretation
previous internal synthesis
label-design provenance
```

It must NOT be described as an additional independent empirical source.

Therefore avoid reasoning equivalent to:

```text
Rahim + Gao + Yamin + EV-08
=
four supporting scientific sources
```

Correct interpretation:

```text
three underlying empirical sources
+
one internal synthesis of those sources
```

---

# 16. Remove "decisive scientific evidence" treatment of EV-08

Do not describe EV-08 as:

```text
the decisive evidence source for Batch 2
```

if that wording implies independent scientific authority.

Instead use wording equivalent to:

```text
EV-08 provides internal design lineage showing how the project
previously synthesised EV-02, EV-03 and EV-04 into Go/Delay label logic.
It does not add independent empirical evidence beyond those sources.
```

If EV-08 contains a project design decision, label it:

```text
internal design authority
```

not:

```text
independent empirical evidence
```

---

# 17. Resolve the Appendix C CAUTION-Go tension

This is a BLOCKING issue for Batch 3.

The repository contains an Appendix C statement approximately equivalent to:

```text
When S = CAUTION the Go recommendation is automatically presented
by the system with a caution qualifier.
```

Batch 2 meanwhile finds:

```text
no scientific evidence currently supports Go under CAUTION
```

These cannot simply coexist as an unclassified `GAP-03`.

Trace the exact Appendix C statement and its surrounding context.

Determine whether it is:

```text
A. normative architecture semantics
B. presentation/UI behaviour
C. illustrative example
D. historical/stale residue
E. another bounded category
```

Provide exact provenance.

---

# 18. Do not silently modify Appendix C

Appendix C is protected canonical authority.

Do NOT modify it merely to resolve this repair.

First classify the tension.

If repository evidence demonstrates that the statement is non-normative presentation text and does not populate:

```text
RS(CAUTION)
```

document that conclusion explicitly.

If the meaning cannot be established confidently without a scientific decision:

create:

```text
OPEN-L3-3 —
CAUTION Go presentation-versus-rule semantics
```

Status:

```text
OPEN — BLOCKS CAUTION RULE IMPLEMENTATION
```

---

# 19. Batch 3 gating

If `OPEN-L3-3` is required:

Do NOT state:

```text
Batch 3 can proceed with Go and Delay rules.
```

Instead state:

```text
Batch 3 implementation remains blocked for CAUTION advisory behaviour
until OPEN-L3-3 is resolved.
```

If SAFE-only implementation could technically proceed, distinguish that engineering fact from permission to start Batch 3.

Do not recommend partial implementation unless explicitly authorised by a later task.

---

# 20. Synchronise OPEN-L3-1 status

The maintained authority currently contains:

```text
§14:
OPEN-L3-1 — NEW — OPEN
```

and later:

```text
§26:
OPEN-L3-1 — PARTIALLY RESOLVED
```

Preserve historical truth without maintaining two current statuses.

Repair §14 to say equivalent to:

```text
OPEN-L3-1
Batch 1 historical status: OPEN.
Superseded by Batch 2 assessment in §26.
```

Current status must appear exactly once as authoritative:

```text
OPEN-L3-1 — PARTIALLY RESOLVED
```

with successor items:

```text
OPEN-L3-1C — DepartureTime OPEN
OPEN-L3-1D — Duration OPEN
```

and, if required:

```text
OPEN-L3-3 — CAUTION Go presentation-versus-rule semantics OPEN
```

---

# 21. Do not close DepartureTime

Preserve:

```text
OPEN-L3-1C
```

unless new direct scientific authority has actually been introduced and verified.

Do not derive DepartureTime from:

```text
sunrise
g_t SAFE onset
daylight start
```

Do not add tide as a canonical E variable.

Evidence that tide matters does not itself provide an executable departure-time rule.

---

# 22. Do not close Duration

Preserve:

```text
OPEN-L3-1D
```

unless new direct scientific authority has actually been introduced and verified.

Do not derive Duration from:

```text
sunset - departure time
available daylight
historical trip duration in UNSAFE-equivalent conditions
```

without scientific justification.

---

# 23. Preserve OPEN-L3-2

Keep:

```text
OPEN-L3-2 —
Rule-condition evaluation failure handling
```

OPEN.

Do not resolve:

```text
abort
skip
continue
partial result
```

in this repair.

No engine is being implemented.

---

# 24. Tighten Go semantics

Current wording such as:

```text
No adverse environmental condition identified within the rule system's scope
```

may overstate what the Layer 3 rule system establishes.

Remember:

Layer 2 already classifies environmental state.

Layer 3 fires advisory rules.

A safer bounded formulation may be equivalent to:

```text
No configured advisory trigger requiring an alternative recommendation
was identified within the active rule set.
```

But do not automatically adopt this wording.

Choose wording consistent with the actual rule semantics.

Do not imply:

```text
environment is objectively safe
risk is absent
departure is approved
```

---

# 25. Tighten Delay semantics

Delay must remain advisory.

Do not describe Delay as proving:

```text
physical danger
prohibition
unsafe to depart
mandatory waiting
```

unless an authority explicitly supplies that normative meaning.

Preserve:

```text
Delay ≠ prohibition
```

and:

```text
human authority remains unconditional
```

---

# 26. Rule-conflict wording

Do not broadly state:

```text
current RS_candidate is conflict-free
```

unless all relevant conflict dimensions have actually been resolved.

Multiple Delay rules may produce:

```text
multiple advisory instances
multiple explanations
duplicate presentation
aggregation requirements
```

This is not necessarily a conclusion-type contradiction.

Prefer:

```text
No conclusion-type contradiction was identified in the current
candidate rule set.
```

Then separately note:

```text
advisory aggregation / presentation policy remains an implementation concern
```

if applicable.

---

# 27. Structural check is not Theorem validation

Do not say a schema-level check is:

```text
equivalent to verifying Theorem C.3
```

if that wording suggests empirical or independent theorem validation.

Instead say:

```text
candidate rules satisfy the theorem's admissibility precondition
at specification level
```

or equivalent.

Safety Dominance remains the formal result from upstream authority.

This Batch 2 structural check only verifies that candidate rule conclusion
types do not violate the fixed admissible sets.

---

# 28. Semantic verification must include repair-specific checks

Update:

```text
semantic-verification-batch2.json
```

with explicit checks equivalent to:

```text
candidate_csv_header_width_derived_from_actual_header
candidate_csv_all_rows_match_header_width
candidate_csv_no_overflow_columns
candidate_csv_no_underwidth_rows

evidence_csv_header_width_derived_from_actual_header
evidence_csv_all_rows_match_header_width
evidence_csv_no_overflow_columns
evidence_csv_no_underwidth_rows

csv_content_preservation_verified

environmental_premise_separated_from_advisory_mapping
premise_support_level_explicit
advisory_mapping_support_level_explicit
mapping_inference_explicit

met_danger_statement_not_equated_with_delay_without_bridge

safe_conjunction_acknowledged_equivalent_to_SAFE_state
safe_go_evidence_not_claimed_to_validate_exact_canonical_conjunction

wave_operability_not_equated_with_delay_without_bridge
rain_restricted_behaviour_not_equated_with_delay_without_bridge
wind_risk_perception_not_equated_with_delay_without_bridge

EV08_classified_as_internal_synthesis
EV08_not_double_counted_as_independent_empirical_evidence

appendix_c_caution_go_tension_resolved_or_OPEN_L3_3_created
batch3_not_authorised_if_blocking_tension_remains

OPEN_L3_1_current_status_synchronised
OPEN_L3_1C_remains_open
OPEN_L3_1D_remains_open
OPEN_L3_2_remains_open

go_semantics_bounded
delay_semantics_bounded
human_authority_unconditional

conflict_claim_bounded_to_conclusion_type
structural_check_not_claimed_as_theorem_validation

F1_F3_not_run
E5_not_run
prototype_not_implemented
protected_canonical_state_unchanged
```

Each check must be:

```text
PASS
FAIL
OPEN
```

with evidence.

---

# 29. Distinguish verification OPENs from scientific OPENs

Do not report:

```text
27 PASS / 0 FAIL / 0 OPEN
```

in a way that implies the workstream has no OPEN issues while:

```text
OPEN-L3-1C
OPEN-L3-1D
OPEN-L3-2
```

remain unresolved.

Report separately:

```text
Semantic verification checks:
X PASS / 0 FAIL / Y OPEN
```

and:

```text
Scientific / implementation OPEN register:
OPEN-L3-1C
OPEN-L3-1D
OPEN-L3-2
[OPEN-L3-3 if required]
...
```

This prevents a misleading `0 OPEN` closure statement.

---

# 30. Update report-batch2.md

The final report must explicitly state:

### CSV integrity

For each CSV:

```text
file
header_width
data_row_count
minimum_row_width
maximum_row_width
verdict
```

Closure requires:

```text
minimum_row_width
==
maximum_row_width
==
header_width
```

---

# 31. Report evidence decomposition

For every retained candidate rule report:

```text
Rule ID
Environmental premise
Premise support level
Advisory conclusion
Advisory mapping support level
Inference bridge
Overall status
```

At minimum cover:

```text
R-SAFE-001
R-CAUTION-001
R-CAUTION-002
R-CAUTION-003
R-CAUTION-004
```

---

# 32. Report EV-08 correctly

Explicitly report:

```text
EV-08 is internal project synthesis / design lineage.
It is not counted as an independent empirical study.
```

State which underlying studies it synthesises.

---

# 33. Report Appendix C resolution

Include a dedicated section:

```text
Appendix C CAUTION-Go Authority Resolution
```

Report:

```text
exact statement
context
authority classification
normative impact on RS(CAUTION)
resolution
remaining OPEN item, if any
Batch 3 implication
```

Do not simply call it `GAP-03`.

---

# 34. Protected canonical integrity

Recheck protected canonical state.

Report:

```text
protected_files_checked
unchanged_files
changed_files
verdict
```

Expected:

```text
changed_files = []
verdict = PASS
```

If a protected file changed:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 2 REMAINS OPEN —
PROTECTED CANONICAL STATE DRIFT
```

STOP.

---

# 35. Closure criteria

Batch 2 may be accepted only if all of the following hold:

```text
[ ] candidate CSV parses with uniform header-derived width
[ ] evidence CSV parses with uniform header-derived width
[ ] CSV scientific content preserved

[ ] environmental-premise evidence separated from advisory-action evidence
[ ] R-CAUTION-001 no longer overstates MET authority
[ ] R-SAFE-001 acknowledges exact equivalence with SAFE classification
[ ] R-SAFE-001 empirical evidence bounded to broader behavioural relationship
[ ] R-CAUTION-002 inference bridge explicit
[ ] R-CAUTION-003 inference bridge explicit
[ ] R-CAUTION-004 inference bridge explicit

[ ] EV-08 not counted as independent empirical evidence
[ ] EV-08 retained only as internal synthesis/design lineage

[ ] Appendix C CAUTION-Go tension resolved
    OR
    OPEN-L3-3 created as blocking OPEN

[ ] no claim that Batch 3 can proceed if OPEN-L3-3 blocks CAUTION semantics

[ ] OPEN-L3-1 historical/current statuses synchronised
[ ] OPEN-L3-1C remains OPEN
[ ] OPEN-L3-1D remains OPEN
[ ] OPEN-L3-2 remains OPEN

[ ] Go semantics bounded
[ ] Delay semantics bounded
[ ] human authority remains unconditional

[ ] conflict wording bounded
[ ] structural admissibility check not described as theorem validation

[ ] F1–F3 not run
[ ] E5 not run
[ ] no engine implementation

[ ] protected canonical state unchanged
```

---

# 36. Closure decision

### Case A — all repairs pass and Appendix C tension is resolved

Use:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 2 CLOSED WITH BOUNDED OPEN ITEMS —
ADVISORY EVIDENCE MAPPINGS AND ARTEFACT INTEGRITY VERIFIED
```

### Case B — all evidence repairs pass but Appendix C tension remains unresolved

Create:

```text
OPEN-L3-3 —
CAUTION Go presentation-versus-rule semantics
```

and use:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 2 REMAINS OPEN —
CAUTION ADVISORY SEMANTICS REQUIRE AUTHORITY RESOLUTION
```

### Case C — advisory mappings remain overstated

Use:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 2 REMAINS OPEN —
ADVISORY MAPPING EVIDENCE REQUIRES BOUNDED RECLASSIFICATION
```

### Case D — CSV integrity still fails

Use:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 2 REMAINS OPEN —
EVIDENCE ARTEFACT STRUCTURAL INTEGRITY FAILED
```

Do not choose the closure line based on progress preference.

Choose it from the evidence.

---

# 37. Required final response

Return:

```text
1. Final verdict
2. CSV parser results
3. Rule-by-rule evidence decomposition
4. R-SAFE-001 resolution
5. R-CAUTION-001 resolution
6. R-CAUTION-002/003/004 resolution
7. EV-08 evidence-status resolution
8. Appendix C CAUTION-Go authority resolution
9. OPEN register after repair
10. Semantic verification summary
11. Protected canonical integrity
12. Files changed
13. Exact closure line
```

For CSV parser results show actual values, for example:

```text
rule-candidate-register-batch2.csv
header_width = X
data_rows = Y
min_row_width = X
max_row_width = X
PASS

rule-evidence-matrix-batch2.csv
header_width = X
data_rows = Y
min_row_width = X
max_row_width = X
PASS
```

Do not state "parse cleanly" without these actual results.

---

# Guiding scientific distinctions

Preserve:

```text
environmental concern
≠
specific advisory recommendation
```

Preserve:

```text
MET says dangerous to small boats
≠
MET says Delay
```

unless the source explicitly says so.

Preserve:

```text
restricted fisher behaviour
≠
AI Delay rule
```

without an inference bridge.

Preserve:

```text
all component classifiers SAFE
⇔
S == SAFE
```

under the canonical max-severity model.

Preserve:

```text
internal synthesis
≠
independent empirical evidence
```

Preserve:

```text
A_AI(CAUTION) contains Go
≠
RS(CAUTION) must contain Go
```

Preserve:

```text
structural admissibility
≠
scientific validity
≠
implementation fidelity
≠
human/domain validation
```

And above all:

```text
scientific incompleteness
is preferable to
fabricated closure.
```
