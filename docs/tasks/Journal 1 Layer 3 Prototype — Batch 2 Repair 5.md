# Journal 1 Layer 3 Prototype — Batch 2

## FINAL MICRO-REPAIR: Metadata, Evidence Register, and Closure JSON Synchronisation

Independent review confirms that all major scientific repairs are complete.

Current Batch 2 status remains:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 2 REMAINS OPEN —
CAUTION ADVISORY SEMANTICS REQUIRE AUTHORITY RESOLUTION
```

OPEN-L3-3 remains blocking.

Do NOT resolve OPEN-L3-3 in this task.
Do NOT implement Batch 3.
Do NOT modify Appendix C.
Do NOT repeat evidence research.
Do NOT alter scientific thresholds or candidate rule families.

Perform only the bounded synchronisation repairs below.

---

# 1. Synchronise semantic verification counts

The actual `semantic-verification-batch2.json` currently contains:

```text
PASS = 72
FAIL = 0
OPEN = 1
TOTAL = 73
```

This is the authoritative current verification count.

Update all current-status references in:

```text
report-batch2.md
layer3-prototype-specification.md
closure-batch2.json
```

so they state:

```text
72 PASS / 0 FAIL / 1 OPEN / 73 checks
```

Do not preserve `57 PASS / 58 checks` as a current result.

Historical references may remain only when explicitly labelled as an earlier repair-round result.

---

# 2. Repair R-SAFE-001 evidence-register inference field

The current report correctly states:

```text
favourable operating/environmental conditions
→ fishers proceeding to sea
```

and:

```text
the canonical all-SAFE conjunction is an
architecture-level operationalisation
of this broader empirical relationship
```

Therefore the actual candidate register must reflect an inference bridge.

For:

```text
R-SAFE-001
```

change:

```text
mapping_inference_required = NO
```

to:

```text
mapping_inference_required = YES
```

The mapping bridge must state equivalent to:

```text
empirical favourable-conditions/proceeding behaviour
→ architecture-level canonical all-SAFE operationalisation
→ Go advisory candidate
```

Preserve:

```text
premise_support_level = Level C
advisory_mapping_support_level = Level C
status = CONDITIONALLY SUPPORTED
```

Do not claim direct validation of the exact canonical conjunction.

---

# 3. Synchronise semantic verification check for R-SAFE-001

If `semantic-verification-batch2.json` currently contains wording equivalent to:

```text
R-SAFE-001 mapping_inference_required = NO
direct behavioral analog
```

repair that check.

The authoritative interpretation is now:

```text
mapping_inference_required = YES
```

because the scientific studies support the broader behavioural pattern,
while the exact canonical five-component SAFE antecedent is a project
operationalisation.

The verification check should PASS only after the CSV and report/spec
agree on this interpretation.

---

# 4. Remove stale EV-08 primary-evidence references from closure JSON

EV-08 is:

```text
internal synthesis / design lineage
```

not:

```text
independent empirical evidence
```

Therefore in `closure-batch2.json` remove EV-08 from all fields labelled:

```text
primary_evidence
Evidence:
supporting empirical evidence
```

where inclusion would imply independent scientific support.

In particular repair:

```text
OPEN_L3_1A_Go
RS_candidate_at_closure.RS_candidate_SAFE.R-SAFE-001.primary_evidence

RS_candidate_at_closure.RS_candidate_CAUTION.R-CAUTION-002.primary_evidence
RS_candidate_at_closure.RS_candidate_CAUTION.R-CAUTION-003.primary_evidence
RS_candidate_at_closure.RS_candidate_CAUTION.R-CAUTION-004.primary_evidence
```

Use only the independent source set:

```text
R-SAFE-001:
EV-02, EV-03, EV-04

R-CAUTION-001:
EV-01

R-CAUTION-002:
EV-05, EV-06
[plus EV-03 only if the maintained candidate register actually treats it as primary evidence]

R-CAUTION-003:
EV-02

R-CAUTION-004:
EV-03, EV-07
```

EV-08 may still appear in a separate field such as:

```text
internal_design_lineage
```

or explanatory prose that explicitly says:

```text
not independent evidence
```

---

# 5. Remove stale "SUPPORTED" Delay classification from closure JSON

The complete R-CAUTION-001 rule is:

```text
CONDITIONALLY SUPPORTED
```

because:

```text
P_ENV = Level A
P_ADV = Level C inferred
```

Therefore remove stale closure wording such as:

```text
Delay advisory in CAUTION state SUPPORTED (warning-driven)
```

Use:

```text
Delay advisory candidates in CAUTION state are CONDITIONALLY SUPPORTED.
R-CAUTION-001 has the strongest environmental-premise authority
(P_ENV Level A), but the Delay mapping remains inferred
(P_ADV Level C).
```

Similarly repair:

```text
OPEN-L3-1_concrete_rule_content
```

if it still states:

```text
Delay SUPPORTED/CONDITIONALLY SUPPORTED
```

Current maintained truth:

```text
Go = CONDITIONALLY SUPPORTED
Delay candidates = CONDITIONALLY SUPPORTED
DepartureTime = OPEN
Duration = OPEN
```

---

# 6. Keep closure JSON internally single-version

After repair, `closure-batch2.json` must not contain contradictory
current values such as:

```text
57 PASS
```

and later:

```text
72 PASS
```

unless the earlier number appears only in clearly labelled historical
repair records.

Current fields must consistently resolve to:

```text
semantic_verification:
72 PASS
0 FAIL
1 OPEN
73 total
```

The single OPEN verification check corresponds to:

```text
OPEN-L3-3 tracking / unresolved Appendix C CAUTION-Go authority
```

---

# 7. Re-run actual CSV parser checks

Re-run Python `csv.reader`.

Expected:

```text
rule-candidate-register-batch2.csv
header_width = 23
data_rows = 10
min_row_width = 23
max_row_width = 23
PASS

rule-evidence-matrix-batch2.csv
header_width = 13
data_rows = 9
min_row_width = 13
max_row_width = 13
PASS
```

Because R-SAFE-001 is being edited, confirm that no quoting or column
integrity regression occurs.

---

# 8. Re-run JSON parsing

Parse:

```text
semantic-verification-batch2.json
closure-batch2.json
```

with Python `json.load`.

Both must parse successfully.

Programmatically compute semantic verdict counts rather than manually
typing them.

Expected:

```text
PASS = 72
FAIL = 0
OPEN = 1
TOTAL = 73
```

If editing the semantic checks changes total count legitimately,
report the actual computed values and propagate them consistently.

Do not hard-code 72/73 if the check set itself changes.

---

# 9. Preserve OPEN-L3-3 and Batch 3 block

Do not alter:

```text
OPEN-L3-3 —
CAUTION Go presentation-versus-rule semantics
```

Status:

```text
OPEN — BLOCKING
```

Preserve:

```text
Batch 3 engine implementation must not begin
until OPEN-L3-3 is resolved.
```

Do not implement SAFE-only or Delay-only paths as a workaround.

---

# 10. Preserve current scientific OPENs

Keep:

```text
OPEN-L3-1C — DepartureTime
OPEN-L3-1D — Duration
OPEN-L3-2 — predicate evaluation failure policy
OPEN-L3-3 — CAUTION-Go semantics
```

plus existing upstream OPEN items unchanged.

---

# 11. Final consistency checks

Add/run checks equivalent to:

```text
semantic_count_matches_actual_json
semantic_count_consistent_report_spec_closure

R_SAFE_001_mapping_inference_required_yes
R_SAFE_001_bridge_matches_report_and_spec

EV08_not_primary_evidence_in_closure_json
EV08_internal_lineage_only

R_CAUTION_001_not_supported_as_complete_rule_in_closure_json
delay_candidate_status_consistent_conditionally_supported

closure_json_no_current_57_pass_residue
closure_json_current_semantic_summary_matches_computed_count

candidate_csv_integrity_pass
evidence_csv_integrity_pass
semantic_json_parse_pass
closure_json_parse_pass

OPEN_L3_3_preserved
batch3_block_preserved

protected_canonical_state_unchanged
```

---

# 12. Final status

This micro-repair does NOT close Batch 2.

The exact current status line remains:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 2 REMAINS OPEN —
CAUTION ADVISORY SEMANTICS REQUIRE AUTHORITY RESOLUTION
```

The purpose of this task is only to obtain a clean and internally
consistent Batch 2 OPEN state.

---

# 13. Required final response

Return:

```text
1. Micro-repair verdict
2. R-SAFE-001 register change
3. EV-08 closure JSON cleanup
4. R-CAUTION-001 / Delay status cleanup
5. Semantic verification computed counts
6. CSV parser results
7. JSON parser results
8. OPEN register
9. Batch 3 gating status
10. Protected canonical integrity
11. Files changed
12. Exact Batch 2 status line
```

Do not proceed to OPEN-L3-3 resolution in the same task.
