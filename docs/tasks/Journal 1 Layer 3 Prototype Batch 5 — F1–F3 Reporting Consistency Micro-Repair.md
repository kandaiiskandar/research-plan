# Journal 1 Layer 3 Prototype

## Batch 5 — F1–F3 Reporting Consistency Micro-Repair

### Task Type

Bounded reporting-only micro-repair.

The Batch 5 executable scientific result has already been independently reviewed.

Scientific verdict:

```text
F1 = PASS
F2 = PASS
F3 = PASS
```

However, `report.md` contains advisory-count values that contradict the trace-derived evidence.

This task exists ONLY to repair that reporting inconsistency.

Do NOT reopen the scientific evaluation.

Do NOT rerun the evaluation unless a new contradiction is discovered that cannot be resolved from the existing evidence.

---

# 1. Branch

Remain on:

```text
eval/journal1-layer3-fidelity-f1-f3
```

Record before repair:

```text
current branch
HEAD
git status
```

Do not create a new scientific evaluation branch.

---

# 2. Authoritative Evidence

Treat these existing Batch 5 artefacts as the authority for the repair:

```text
data/journal1-layer3-prototype/batch5-fidelity-evaluation/
    fidelity-traces.csv
    fidelity-results.json
    rule-activation-summary.csv
    state-space-manifest.json
    evaluation-design.json
    verification.json
    boundary-checks.json
    integrity.json
    report.md
```

The executable trace/results are authoritative over manually written prose in `report.md`.

Do not change executable evidence merely to make it agree with the report.

---

# 3. Confirm the Trace-Derived Counts First

Before editing anything, independently derive from `fidelity-traces.csv`:

```text
primary episodes
SAFE episodes
CAUTION episodes

episodes with >=1 advisory
total advisory records

F1 violations
F2 violations
F3 mismatches
```

Also independently sum `advisories_generated` from:

```text
rule-activation-summary.csv
```

Expected existing evidence is:

```text
Primary episodes          = 292
SAFE episodes             = 32
CAUTION episodes          = 260

Episodes with advisory    = 244
Advisory records          = 454

F1 violations             = 0
F2 violations             = 0
F3 mismatches             = 0
```

Rule-level advisory total should independently reconcile as:

```text
R-CAUTION-001 = 130
R-CAUTION-002 = 108
R-CAUTION-003 = 108
R-CAUTION-004 = 108

TOTAL = 454
```

Do not assume these values merely because this prompt states them.

Verify them from the existing artefacts.

If they do NOT reproduce exactly:

```text
STOP
BATCH5_REPORTING_REPAIR_BLOCKED —
TRACE-DERIVED COUNTS DO NOT MATCH EXPECTED AUTHORITATIVE EVIDENCE
```

Report the exact discrepancy.

Do not repair code or rerun the evaluation.

---

# 4. Known Reporting Error

`report.md` currently reports incorrect values in the F1/F2 sections.

Repair:

```text
F1_advisory_records_evaluated

492
→
454
```

Repair:

```text
F2_episodes_with_advisory

260
→
244
```

Repair:

```text
F2_advisory_records

492
→
454
```

The values must come from the existing executable trace/results.

---

# 5. Explain the 244 / 260 Distinction

Add a concise clarification where appropriate:

```text
260 CAUTION episodes were evaluated.

244 of those episodes generated at least one advisory.

16 CAUTION episodes generated AI(E)=∅ because none of the currently executable rule predicates evaluated TRUE.
```

This is NOT a fidelity failure.

Preserve the distinction:

```text
A_AI(S)
= admissible advisory conclusion types

NOT

A_AI(S)
= requirement that an advisory must exist
```

Therefore:

```text
AI(E)=∅
```

is legitimate for a governed episode.

Do not invent a rule to eliminate those 16 empty-advisory episodes.

---

# 6. Verify the 16 Empty-Advisory Episodes

From `fidelity-traces.csv`, explicitly verify:

```text
260 - 244 = 16
```

For those 16 episodes confirm:

```text
state = CAUTION
advisory_record_count = 0
F1_violation = false
F2_violation = false
F3_mismatch = false
```

Also verify they are not:

```text
configuration_failure
evaluation_failure
```

unless existing traces say otherwise.

Record the result in the repair note/report.

Do not change those episodes.

---

# 7. Search report.md for Dependent Residue

Search the entire `report.md` for:

```text
492
260
244
454
episodes_with_advisory
advisory_records
advisories
all CAUTION
every CAUTION
```

Determine whether any prose implicitly claims that all 260 CAUTION episodes generated advisories.

Repair only statements that are contradicted by the trace.

Do not broadly rewrite the report.

---

# 8. Preserve Correct Counts

Do NOT change:

```text
292 primary episodes

32 SAFE episodes

260 CAUTION episodes

162 UNSAFE gate-off cases

486 raw S/component combinations

162 reachable component-state combinations

162 interface-inconsistent combinations
```

unless existing authoritative artefacts independently contradict them.

The state-space manifest currently remains authoritative for denominator construction.

---

# 9. Preserve Scientific Results

Do NOT change:

```text
F1 violations = 0
F1 verdict = PASS

F2 violation count = 0
F2 verdict = PASS

F3 mismatches = 0
F3 verdict = PASS

overall = PASS
```

unless the existing trace-derived evidence itself contradicts these values.

This micro-repair does not reopen F1–F3.

---

# 10. Preserve Scientific Interpretation

Keep the bounded claim:

> The frozen Layer 3 implementation produced zero violations of the configured advisory admissibility contract across the evaluated deterministic fidelity state space.

Do NOT strengthen it into:

```text
real-world safety proven
system proven safe
advisories scientifically optimal
fishers will make safer decisions
accidents will be prevented
```

F1/F2 remain implementation-fidelity evidence.

---

# 11. Files That May Change

Expected substantive change:

```text
data/journal1-layer3-prototype/batch5-fidelity-evaluation/report.md
```

If necessary, a small reporting-repair record may also be created, for example:

```text
data/journal1-layer3-prototype/batch5-fidelity-evaluation/
    reporting-repair.json
```

Do NOT modify the existing scientific evidence files merely to regenerate hashes.

---

# 12. Files That Must Remain Unchanged

Do NOT modify:

```text
fidelity-traces.csv
fidelity-results.json
rule-activation-summary.csv
state-space-manifest.json
evaluation-design.json
boundary-checks.json
```

Do NOT modify:

```text
scripts/journal1_layer3_fidelity_evaluation.py
```

Do NOT modify any:

```text
governance/*.py
```

Do NOT modify:

```text
docs/canonical/appendix-c-formalisation.md
docs/canonical/architecture-illustration.md

publications/active/journal-1/
    layer3-prototype-specification.md
    algorithm-specification.md
    evaluation-specification.md
```

---

# 13. Integrity Handling

Because `report.md` is intentionally changing, record:

```text
report_before_sha256
report_after_sha256
```

Confirm unchanged hashes for at least:

```text
fidelity-traces.csv
fidelity-results.json
rule-activation-summary.csv
state-space-manifest.json

scripts/journal1_layer3_fidelity_evaluation.py

all governance implementation files

canonical/specification authority files
```

Do not rewrite historical `integrity.json` in a way that pretends the repaired report was the original evaluation artefact.

If an integrity update is needed, prefer a separate repair record.

---

# 14. No Evaluation Rerun

Expected:

```text
evaluation_rerun = false
```

Do not rerun F1–F3 simply because `report.md` contains incorrect manually reported counts.

The existing executable traces already provide the evidence needed for this correction.

If you believe a rerun is necessary, STOP and explain exactly why.

---

# 15. No Implementation Changes

Expected:

```text
implementation_modified = false
rules_modified = false
evaluation_script_modified = false
canonical_modified = false
scientific_specification_modified = false
```

Any required change to these areas is outside this micro-repair.

STOP rather than expanding scope.

---

# 16. Verification

After the repair verify:

```text
report_primary_episodes_292 = PASS

report_SAFE_episodes_32 = PASS

report_CAUTION_episodes_260 = PASS

report_episodes_with_advisory_244 = PASS

report_advisory_records_454 = PASS

rule_activation_advisory_sum_454 = PASS

empty_advisory_CAUTION_episodes_16 = PASS

F1_zero_violations_preserved = PASS

F2_zero_violations_preserved = PASS

F3_zero_mismatches_preserved = PASS

F1_PASS_preserved = PASS

F2_PASS_preserved = PASS

F3_PASS_preserved = PASS

trace_unchanged = PASS

results_json_unchanged = PASS

rule_activation_summary_unchanged = PASS

evaluation_script_unchanged = PASS

governance_implementation_unchanged = PASS

canonical_authority_unchanged = PASS

evaluation_not_rerun = PASS

E5_not_run = PASS
```

There should be:

```text
0 FAIL
0 OPEN
```

for this reporting repair to close.

---

# 17. POST_FIDELITY_READY

After the repair classify:

```text
POST_FIDELITY_READY = true | false
```

Set TRUE only if:

```text
F1 = PASS
F2 = PASS
F3 = PASS

report is consistent with trace-derived evidence

all protected evidence remains unchanged

implementation remains frozen

canonical/specification authority remains unchanged
```

Do NOT interpret this as automatic authorisation for E5 or another scientific task.

---

# 18. Closure

If all checks pass, use:

```text
BATCH 5 F1–F3 REPORTING CONSISTENCY MICRO-REPAIR CLOSED —
TRACE-DERIVED ADVISORY COUNTS SYNCHRONISED
```

Then the scientific Batch 5 closure may remain:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 5 CLOSED —
EXECUTABLE F1–F3 SCIENTIFIC FIDELITY EVALUATION PASSED
```

If the trace-derived values do not reproduce:

```text
BATCH 5 F1–F3 REPORTING CONSISTENCY MICRO-REPAIR REMAINS OPEN —
<EXACT DISCREPANCY>
```

Do not force closure.

---

# 19. Required Final Response

Return:

1. Verdict
2. Branch
3. HEAD
4. Files inspected
5. Trace-derived primary episode count
6. SAFE episode count
7. CAUTION episode count
8. Trace-derived episodes with advisory
9. Trace-derived advisory-record count
10. Rule-level advisory sum
11. Empty-advisory CAUTION episode count
12. Empty-advisory episode integrity result
13. F1 result
14. F2 result
15. F3 result
16. Exact `report.md` corrections made
17. Any additional dependent prose corrected
18. Files modified
19. Files confirmed unchanged
20. Evaluation rerun status
21. Implementation-change status
22. Canonical/specification-change status
23. Repair verification PASS/FAIL/OPEN totals
24. POST_FIDELITY_READY
25. Reporting micro-repair closure line
26. Scientific Batch 5 closure line

Do NOT start E5 or another batch automatically.
