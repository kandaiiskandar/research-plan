# Journal 1 Layer 3 Prototype — Batch 2

## FINAL CLOSURE RESIDUE REPAIR

Independent review confirms that the major Final Repair succeeded:

```text id="b2r1"
CSV structural integrity = PASS
P_ENV / P_ADV decomposition = repaired
EV-08 independent-evidence double counting = repaired
OPEN-L3-3 = correctly created
Appendix C ambiguity = correctly identified
```

Batch 2 nevertheless remains OPEN because a small number of stale statements contradict the repaired authority.

Perform ONLY the bounded residue repairs below.

Do not repeat the evidence search.
Do not change candidate rules.
Do not implement the prototype.
Do not run F1–F3.
Do not run E5.
Do not modify Appendix C.
Do not resolve OPEN-L3-3 in this task.

---

## 1. Synchronise Batch 2 status

The maintained specification currently says:

```text id="b2r2"
Batch 2 CLOSED WITH BOUNDED OPEN ITEMS
```

while the final report correctly says:

```text id="b2r3"
Batch 2 REMAINS OPEN
```

because:

```text id="b2r4"
OPEN-L3-3
```

blocks Batch 3.

Repair the specification header/current-status metadata so the maintained current truth is:

```text id="b2r5"
Batch 2 REMAINS OPEN —
OPEN-L3-3 CAUTION-Go authority semantics unresolved
```

Do not mark Batch 2 CLOSED while OPEN-L3-3 remains a blocking OPEN.

Historical statuses may be preserved only if explicitly labelled historical/superseded.

---

## 2. Remove stale Batch 3 permission

In `report-batch2.md` §9 remove or supersede:

```text id="b2r6"
The Batch 3 engine implementation task can proceed with Go and Delay rules specified.
```

This contradicts the final authority.

Replace with:

```text id="b2r7"
Batch 3 engine implementation must not begin while OPEN-L3-3 remains unresolved.

The current Batch 2 candidate set specifies conditionally supported
Go/Delay rule candidates, but executable CAUTION advisory behaviour
remains blocked by the unresolved Appendix C CAUTION-Go semantics.
```

Preserve:

```text id="b2r8"
DepartureTime = OPEN-L3-1C
Duration = OPEN-L3-1D
```

---

## 3. Repair stale R-CAUTION-001 overclaim

Remove stale wording equivalent to:

```text id="b2r9"
R-CAUTION-001 is the strongest rule in the candidate set
(Level A, SUPPORTED)
```

The authoritative classification is:

```text id="b2r10"
R-CAUTION-001

P_ENV = Level A
P_ADV = Level C inferred
mapping_inference_required = YES
overall_status = CONDITIONALLY SUPPORTED
```

MET directly supports:

```text id="b2r11"
dangerous to small boats
```

but does not directly state:

```text id="b2r12"
Delay departure
```

Therefore do not call the complete rule:

```text id="b2r13"
Level A rule
SUPPORTED rule
```

without qualification.

The specification heading:

```text id="b2r14"
R-CAUTION-001 (strongest — Level A)
```

must also be repaired.

Use wording such as:

```text id="b2r15"
R-CAUTION-001 — strongest environmental-premise authority
```

or simply:

```text id="b2r16"
R-CAUTION-001
```

---

## 4. Repair conflict-analysis overclaim

Replace:

```text id="b2r17"
The current RS_candidate design is conflict-free.
```

with:

```text id="b2r18"
No conclusion-type contradiction was identified in the current
candidate rule set.
```

Explicitly preserve that multiple Delay rules may generate:

```text id="b2r19"
multiple advisory instances
multiple explanations
duplicate presentation
aggregation requirements
```

Those are implementation/presentation questions and are not proven closed by Batch 2.

Do not invent an aggregation policy.

---

## 5. Tighten R-SAFE-001 evidence wording

Do not describe the empirical studies as directly observing:

```text id="b2r20"
all-SAFE-equivalent conditions
```

if this implies that the studies tested the exact canonical conjunction:

```text id="b2r21"
g_w SAFE
∧ g_r SAFE
∧ g_m SAFE
∧ g_o SAFE
∧ g_t SAFE
```

Replace the environmental-premise wording with something equivalent to:

```text id="b2r22"
Favourable operating/environmental conditions are associated with
fishers proceeding to sea.
```

Then state explicitly:

```text id="b2r23"
The canonical all-component-SAFE antecedent is an
architecture-level operationalisation of this broader empirical pattern.
```

Therefore the evidence decomposition should not say:

```text id="b2r24"
Inference bridge required = NO
```

without qualification.

Use:

```text id="b2r25"
Inference bridge required = YES
```

with a bridge equivalent to:

```text id="b2r26"
broader favourable-conditions behaviour
→ canonical all-SAFE operationalisation
→ Go advisory candidate
```

Overall status remains:

```text id="b2r27"
CONDITIONALLY SUPPORTED
```

Do not reject R-SAFE-001 solely because of this repair.

Do not claim local validation.

---

## 6. Preserve successful repairs

Do not regress any of these:

```text id="b2r28"
candidate CSV:
header_width = 23
rows = 10
min_width = 23
max_width = 23

evidence CSV:
header_width = 13
rows = 9
min_width = 13
max_width = 13
```

Preserve:

```text id="b2r29"
EV-08 = internal synthesis / design lineage
not independent empirical evidence
```

Preserve:

```text id="b2r30"
OPEN-L3-1C = OPEN
OPEN-L3-1D = OPEN
OPEN-L3-2 = OPEN
OPEN-L3-3 = OPEN and BLOCKING
```

Preserve:

```text id="b2r31"
F1–F3 = NOT RUN
E5 = NOT RUN
prototype implementation = NOT STARTED
```

Preserve protected canonical state unchanged.

---

## 7. Add residue-specific semantic checks

Add or rerun checks equivalent to:

```text id="b2r32"
batch2_status_consistent_across_current_artifacts
batch2_not_marked_closed_while_OPEN_L3_3_blocking

no_stale_batch3_permission
OPEN_L3_3_blocks_batch3_consistently

R_CAUTION_001_not_called_SUPPORTED_Level_A_as_complete_rule
R_CAUTION_001_P_ENV_Level_A_preserved
R_CAUTION_001_P_ADV_inference_preserved

candidate_set_not_broadly_called_conflict_free
conclusion_type_conflict_claim_bounded

R_SAFE_001_empirical_premise_bounded_to_favourable_conditions
R_SAFE_001_canonical_operationalisation_bridge_explicit
R_SAFE_001_not_claimed_locally_validated

EV08_internal_synthesis_status_preserved

candidate_csv_integrity_preserved
evidence_csv_integrity_preserved

F1_F3_not_run
E5_not_run
prototype_not_implemented
protected_canonical_state_unchanged
```

All residue-repair checks must PASS except known scientific OPEN items.

---

## 8. Do not close Batch 2

This task does NOT resolve OPEN-L3-3.

Therefore after successful residue repair the correct Batch 2 status remains:

```text id="b2r33"
OPEN
```

Use the exact closure/status line:

```text id="b2r34"
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 2 REMAINS OPEN —
CAUTION ADVISORY SEMANTICS REQUIRE AUTHORITY RESOLUTION
```

Do not use:

```text id="b2r35"
CLOSED WITH BOUNDED OPEN ITEMS
```

while OPEN-L3-3 remains blocking.

---

## 9. Required final report

Return:

```text id="b2r36"
1. Residue-repair verdict
2. Status synchronisation result
3. R-CAUTION-001 wording repair
4. R-SAFE-001 evidence-bridge repair
5. Conflict-analysis wording repair
6. Batch 3 gating statement
7. CSV parser recheck
8. OPEN register
9. Protected canonical integrity
10. Files changed
11. Exact Batch 2 status line
```

The expected result of this task is not Batch 2 closure.

It is a clean, internally consistent OPEN state ready for the next
scientific task:

```text id="b2r37"
OPEN-L3-3 resolution.
```

---

# Guiding distinctions

Preserve:

```text id="b2r38"
Level A environmental premise
≠
Level A advisory rule
```

Preserve:

```text id="b2r39"
favourable-condition behaviour
≠
empirical validation of the exact canonical SAFE conjunction
```

Preserve:

```text id="b2r40"
no conclusion-type contradiction
≠
all rule-conflict and aggregation questions closed
```

And preserve:

```text id="b2r41"
Batch 2 evidence specification substantially repaired
≠
Batch 2 scientifically closed
```
