# Journal 1 Algorithm Specification — Batch 4

## Final Complexity and Authority Residue Repair

Batch 4 is NOT yet accepted as closed.

Do not reopen the scientific architecture.
Do not change Algorithms 1–4 semantics.
Do not change canonical files.
Do not build the prototype.
Do not run F1–F3 or E5.

Two bounded closure repairs remain.

---

## Repair 1 — Algorithm 3 complexity must match the actual pseudocode

The current CLOSED Algorithm 3 explicitly performs:

```text
RS_candidate ← candidate(repository, S)

if ∃ ρ ∈ RS_candidate :
    type(ρ) ∉ A_AI(S)
then
    refuse supply
```

Therefore the currently specified Algorithm 3 performs a candidate-set
compliance check before supply.

Let:

```text
k_S = |RS_candidate|
```

For the algorithm AS CURRENTLY SPECIFIED, preserve:

```text
T_A3
=
T_select(S)
+
O(k_S)
```

unless `k_S` itself is explicitly fixed by an authoritative implementation,
which it is not.

### Required correction

Do NOT report the current Algorithm 3 as:

```text
T_A3_fixed = O(1)
```

merely because:

```text
n = 5
|S| = 3
|R| = 4
```

Those fixed architecture constants do not make `k_S` constant.

A prevalidated state-indexed rule-set implementation that eliminates the
per-supply compliance scan may be discussed only as:

```text
IMPLEMENTATION VARIANT / FUTURE OPTIMISATION
```

not as the complexity of the current Algorithm 3 pseudocode.

If such an implementation removes lines 5–9 from runtime execution, it is
a different implementation realisation and must remain clearly separated
from the complexity derived from the maintained pseudocode.

### Preferred bounded formulation

Current specified algorithm:

```text
T_A3_current
=
T_select(S) + O(k_S)
```

Selection examples may remain parameterised:

```text
state-indexed selector:
T_select(S) may be O(1)

repository scan:
T_select(S) may be O(k)
```

Thus:

```text
T_A3_current
=
O(1) + O(k_S)
```

under an O(1) selector,

NOT simply:

```text
O(1)
```

unless `k_S` is fixed.

Space may remain:

```text
O(1)
```

for reference-only storage or:

```text
O(k_S)
```

for materialisation, provided the representation distinction remains
explicit.

Update every affected occurrence in:

```text
algorithm-specification.md
complexity-analysis-batch4.csv
complexity-traceability-batch4.csv
report-batch4.md
closure-batch4.json
semantic-verification-batch4.json
manuscript complexity table/text
```

Audit the end-to-end equation after repair.

It should continue retaining:

```text
T_select(S)
O(k_S)
T_engine(...)
```

and must not collapse the full pipeline to O(1).

---

## Repair 2 — Maintained-authority status residue

The top of:

```text
publications/active/journal-1/algorithm-specification.md
```

still describes the document as:

```text
Status: Batch 1 CLOSED
```

and says Batches 2 and 3 will populate the algorithms later.

That statement is now historical and inaccurate.

Update the status/header so it accurately reflects the current state:

```text
Batches 1–4 completed
Algorithms 1–4 specified
Complexity analysis integrated
workstream closure pending/closed according to this repair outcome
```

Use concise wording.

Do not rewrite the historical Batch 1 body.

Also repair the known count residue in §10:

```text
"seven bounded OPEN items"
```

when the table contains:

```text
OPEN-B1-1 ... OPEN-B1-8
```

Change only the count wording:

```text
eight bounded OPEN items
```

Do not alter any OPEN item's meaning or status.

---

## Re-verify

After repair, verify:

```text
algorithm3_current_complexity_includes_kS
prevalidated_A3_variant_not_misreported_as_current_algorithm
end_to_end_engine_and_kS_terms_retained
full_pipeline_not_claimed_O1

authority_header_current
batch1_open_item_count_correct

solar_lookup_remains_parameterised
rule_engine_strategy_remains_OPEN_B3_2
low_resource_claim_not_inferred_from_complexity
E5_not_run
F1_F3_not_reported
all_prior_OPEN_items_preserved
protected_canonical_state_unchanged
```

Each must be:

```text
PASS / FAIL / OPEN
```

with evidence.

---

## Do not change

Do not change:

```text
F_{D,τ}
ρ_{D,τ}
g_w
g_r
g_m
g_o
g_t
G(S)
A_AI(S)
RS(S)
AI(E)
```

Do not change thresholds.

Do not change recommendation types.

Do not choose a rule-engine strategy.

Do not choose the state/rule-set concurrency mechanism.

Do not close OPEN-B4-1.

---

## Closure condition

Close only if the complexity table now distinguishes:

```text
fixed environmental/governance architecture constants
```

from:

```text
variable rule-set size k_S
```

and the maintained authority no longer contains stale workstream-status
language.

If PASS, use:

```text
JOURNAL 1 ALGORITHM SPECIFICATION AND COMPLEXITY ANALYSIS CLOSED —
ALGORITHM 3 COMPLEXITY AND AUTHORITY RESIDUE REPAIRED
```

Otherwise:

```text
JOURNAL 1 ALGORITHM SPECIFICATION AND COMPLEXITY ANALYSIS REMAINS OPEN —
COMPLEXITY OR AUTHORITY RESIDUE REMAINS
```
