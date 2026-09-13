# Journal 1 Evaluation

## E3/E4 Resolution-Sensitivity Authority Consistency Micro-Repair

### Task Type

Bounded scientific-authority consistency repair.

This task resolves a contradiction discovered before Journal 1 Manuscript Batch 8A.

It is NOT:

* a new experiment;
* a new sensitivity analysis;
* a replay rerun;
* an E4 recomputation;
* a manuscript drafting task;
* an opportunity to change closed empirical results.

---

# 1. Trigger

Batch 8A discovered the following contradiction.

Existing E3 authority states, in substance:

```text
Both configurations computed and reported for every empirical value in:
E1
E2
E4
E6
```

and prohibits reporting an empirical value without its PRIMARY/RESOLUTION pair.

However, authoritative E4 evidence contains only PRIMARY temporal-dynamics results:

```text
transitions = 3661
scheduled transitions = 3439
non-scheduled transitions = 222
oscillations = 26
hysteresis reduction = 10.36%
```

No authoritative RESOLUTION E4 result exists.

Repository inspection also established that the current hysteresis analysis is PRIMARY-based and has not been executed under the RESOLUTION/MFWAM configuration.

Therefore the current E3 and E4 contracts are internally inconsistent.

---

# 2. Branch

Remain on the current branch unless repository policy requires a dedicated branch.

Preferred dedicated branch if one is required:

```text
fix/journal1-e3-e4-authority-consistency
```

Record:

```text
branch
HEAD
working tree
```

before modification.

---

# 3. Governing Principle

Do NOT create missing E4 RESOLUTION evidence in this task.

Resolve the inconsistency by correcting the scope of E3.

The scientific principle is:

> Resolution sensitivity applies only to empirical quantities for which the evaluation design supports a like-for-like PRIMARY/RESOLUTION comparison.

Do not state that every empirical metric must automatically have a RESOLUTION analogue.

---

# 4. Corrected E3 Scope

Repair E3 so that its mandatory dual-configuration scope is:

```text
E1
E2
E6
```

Do not include E4 in the mandatory dual-configuration requirement.

The corrected interpretation must make clear that E3 evaluates:

```text
resolution sensitivity of cross-configuration-comparable empirical quantities
```

rather than:

```text
every empirical value produced anywhere in the evaluation
```

---

# 5. E4 Status

Preserve:

```text
E4 = CLOSED
```

E4 remains the authoritative PRIMARY temporal-dynamics / hysteresis characterisation.

Preserve the existing E4 values exactly.

Do NOT create or infer:

```text
RESOLUTION transitions
RESOLUTION oscillations
RESOLUTION hysteresis reduction
```

---

# 6. Why E4 Is Outside Mandatory E3 Scope

Document the methodological reason explicitly.

E4 characterises temporal dynamics over its predefined PRIMARY chronology.

A valid sensitivity comparison would require an explicitly comparable temporal design.

Do not assume that raw event counts from differing source windows or temporal coverage are directly comparable merely because both are called PRIMARY and RESOLUTION.

Therefore:

```text
E4_RESOLUTION = NOT_REQUIRED_BY_CURRENT_E3_DESIGN
```

This means:

```text
NOT_REQUIRED
```

not:

```text
ZERO
NOT_FOUND
FAILED
REFUTED
```

---

# 7. Important Boundary

Do NOT claim:

> E4 is insensitive to resolution.

That has not been tested.

Do NOT claim:

> E4 would produce the same result under MFWAM.

Unknown.

Correct bounded wording:

> E4 is reported as a PRIMARY temporal-dynamics characterisation; cross-configuration sensitivity for E4 is outside the current E3 comparison contract.

---

# 8. Future E4 Sensitivity

If future work evaluates E4 sensitivity, it must be a separately authorised experiment.

Such a future design may need to control for:

```text
common temporal coverage
comparable input availability
normalised transition rates
oscillation rates
equivalent hysteresis parameters
```

Do not design or execute that future experiment here.

---

# 9. Files To Inspect Before Modification

Read the authoritative files that define:

```text
E3
E4
claim status
evaluation design
```

including at minimum:

```text
publications/active/journal-1/evaluation-specification.md
```

and the current post-fidelity claim-status / dependency evidence.

Also read the Batch 8A blocker artefact documenting the contradiction.

Do not rely solely on this prompt.

---

# 10. Minimal Change Principle

Modify only files necessary to make E3 and E4 internally consistent.

Likely candidates include:

```text
publications/active/journal-1/evaluation-specification.md
```

and any authoritative claim-status artefact that currently states:

```text
E3 requires E4 dual-configuration evidence
```

Do not modify:

```text
canonical architecture
governance implementation
Layer 3 implementation
Batch 5 fidelity evidence
E1 results
E2 results
E4 results
E6 results
E5 status
manuscript prose
```

unless required solely to update an authority pointer.

---

# 11. Preserve Existing Dual-Configuration Results

Preserve existing PRIMARY/RESOLUTION evidence for E1, E2 and E6.

Do not recompute them.

Expected existing values include:

PRIMARY:

```text
C0↔C1 = 42.88%
C0↔C2 = 48.69%
C1↔C2 = 5.81%
C1↔C3 = 0.00%
```

RESOLUTION:

```text
C0↔C1 = 41.08%
C0↔C2 = 45.56%
C1↔C2 = 4.48%
C1↔C3 = 0.00%
```

Verify against repository authority rather than trusting the prompt.

---

# 12. E3 Status After Repair

If the repository confirms complete dual-configuration evidence for E1, E2 and E6:

```text
E3 = CLOSED
```

with the revised scope.

Do not leave a false statement such as:

> dual-configuration values exist for all empirical claims.

Replace with bounded wording equivalent to:

> dual-configuration evidence exists for all empirical quantities within the defined E3 cross-configuration sensitivity scope.

---

# 13. E4 Manuscript Contract After Repair

The manuscript may report E4 PRIMARY values without violating E3.

Allowed:

```text
3661 transitions
3439 scheduled transitions
222 non-scheduled transitions
26 oscillations
10.36% hysteresis reduction
```

provided the manuscript identifies them as PRIMARY temporal-dynamics findings.

The manuscript must NOT imply a RESOLUTION E4 sensitivity result exists.

---

# 14. No New Experiment

Prohibited:

```text
run hysteresis_analysis.py with MFWAM
modify hysteresis_analysis.py
generate RESOLUTION E4
rerun retrospective replay
run canonical figures
invent a paired temporal window
```

If authority repair unexpectedly requires new empirical evidence:

```text
STOP

E3/E4 AUTHORITY REPAIR BLOCKED —
NEW EXPERIMENT REQUIRED
```

---

# 15. Provenance Repair

Create a small evidence directory:

```text
data/journal1-e3-e4-authority-repair/
```

Required:

```text
authority-before.md
authority-after.md
scope-rationale.md
integrity.json
verification.json
report.md
```

`scope-rationale.md` must explain:

1. the original contradiction;
2. why E4 has PRIMARY-only evidence;
3. why E3 is narrowed;
4. why this does not constitute an E4 result change;
5. why no sensitivity claim about E4 is being made.

---

# 16. Integrity

Hash before/after all relevant authority files.

Expected unchanged:

```text
canonical architecture files
governance code
evaluation scripts
hysteresis result artefacts
Batch 5 evidence
Batch 7A evidence
active manuscript
```

Expected changed:

only the minimum E3/E4 authority/status files required to repair the contradiction.

---

# 17. Verification

At minimum verify:

```text
original_E3_E4_contradiction_documented

E3_scope_repaired

E3_scope_E1_true
E3_scope_E2_true
E3_scope_E6_true

E3_scope_E4_false

E1_dual_configuration_evidence_present
E2_dual_configuration_evidence_present
E6_dual_configuration_evidence_present

E4_PRIMARY_values_preserved
E4_RESOLUTION_not_invented

E4_remains_CLOSED

E3_remains_CLOSED_if_revised_scope_satisfied

no_claim_E4_resolution_insensitive

no_claim_E4_resolution_equivalent

no_new_experiment

no_replay_rerun

no_scientific_code_change

manuscript_unchanged

canonical_unchanged

governance_unchanged
```

Use:

```text
PASS
FAIL
OPEN
```

---

# 18. Success Condition

Success requires:

```text
E3 and E4 contracts are internally consistent

E3 sensitivity scope is scientifically bounded

E1/E2/E6 retain dual-configuration authority

E4 retains PRIMARY-only temporal-dynamics authority

no unsupported RESOLUTION E4 claim exists

no empirical result has been recomputed

no scientific implementation changed

manuscript remains untouched
```

---

# 19. Exact Closure

If all checks pass:

```text
JOURNAL 1 E3/E4 RESOLUTION-SENSITIVITY AUTHORITY MICRO-REPAIR CLOSED —
E3 CROSS-CONFIGURATION SCOPE BOUNDED AND E4 PRIMARY TEMPORAL-DYNAMICS AUTHORITY PRESERVED
```

Then report:

```text
E3 = CLOSED
E4 = CLOSED
E4_RESOLUTION = NOT_REQUIRED_BY_CURRENT_E3_DESIGN
BATCH_8A_BLOCKER = RESOLVED
```

---

# 20. Next Task

Recommend exactly:

```text
Resume Journal 1 Manuscript Batch 8A
```

Do not execute Batch 8A automatically.
