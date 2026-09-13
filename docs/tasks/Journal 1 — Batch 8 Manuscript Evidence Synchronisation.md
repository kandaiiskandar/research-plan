# Journal 1 — Batch 8

## Manuscript Evidence Synchronisation & Claim Alignment

### Task Type

Evidence-to-manuscript synchronisation, claim-status reconciliation, bounded scientific writing repair, and internal consistency verification.

This task updates the active Journal 1 manuscript so that its formal, fidelity, and empirical claims accurately reflect the evidence already CLOSED in the repository.

This task is NOT:

* a new experiment;
* a new scientific evaluation;
* a new architecture design task;
* a Layer 3 implementation task;
* a retrospective replay task;
* a human study;
* an Android benchmark;
* an opportunity to invent missing E5 evidence.

---

# 1. Branch

Create:

```text
docs/journal1-manuscript-evidence-sync
```

Before modifying anything record:

```text
current branch
HEAD
working-tree status
Batch 7A closure commit
active manuscript SHA-256
evaluation-specification SHA-256
algorithm-specification SHA-256
layer3-prototype-specification SHA-256
```

Do not mix unrelated work into this branch.

---

# 2. Primary Manuscript Authority

The manuscript to synchronise is:

```text
publications/active/journal-1/submissions/v1-initial-submission/manuscript.md
```

Important:

The directory name `v1-initial-submission` does NOT mean the manuscript has already been submitted.

Treat it as the active Journal 1 manuscript.

Do not rename or relocate it in this task.

---

# 3. Scientific Evidence Authority

Read the following in full before editing the manuscript.

## Canonical architecture

```text
docs/canonical/appendix-c-formalisation.md
docs/canonical/architecture-illustration.md
```

## Journal 1 scientific specifications

```text
publications/active/journal-1/evaluation-specification.md
publications/active/journal-1/algorithm-specification.md
publications/active/journal-1/layer3-prototype-specification.md
```

## Layer 3 fidelity evidence

Locate and read the complete Batch 5 evidence under:

```text
data/journal1-layer3-prototype/
```

Identify specifically the final Batch 5:

```text
report
fidelity results
fidelity traces
state-space manifest
rule activation summary
boundary checks
verification
integrity
reporting consistency repair evidence
```

Do not rely on an earlier superseded Batch 5 report if a repaired final report exists.

## Post-fidelity evaluation authority

Read:

```text
data/journal1-post-fidelity-plan/
```

including:

```text
report.md
claim-status-matrix.csv
manuscript-coverage-audit.csv
evaluation-dependency-graph.md
e5-authority-assessment.md
replay-requirement-assessment.md
next-evaluation-decision.json
verification.json
integrity.json
```

## Batch 7A E5 evidence

Read:

```text
data/journal1-e5-benchmark/
```

including:

```text
execution-path-audit.md
benchmark-protocol.md
hardware-profile.json
workload-manifest.json
latency-raw.csv
latency-summary.csv
latency-results.json
resource-summary.json
reference-run.json
target-hardware-readiness.md
verification.json
integrity.json
report.md
```

Also inspect:

```text
scripts/journal1_e5_benchmark.py
```

only where necessary to verify claims made by Batch 7A.

---

# 4. Frozen Upstream Work

Treat the following as CLOSED.

Do not reopen them unless direct contradictory repository evidence is discovered:

```text
Conference manuscript audit

Appendix C rain signature synchronisation

Appendix C g_t totality synchronisation

Canonical repository drift synchronisation

Journal 1 canonical consistency synchronisation

Journal 1 evaluation baseline design

Journal 1 evaluation specification

Journal 1 algorithm specification

Layer 3 Batch 1

Layer 3 Batch 2

OPEN-L3-3 Resolution B

OPEN-L3-2 predicate failure policy

OPEN-L3-2 Algorithm-boundary taxonomy repair

Layer 3 Batch 3

Layer 3 Batch 4A

Layer 3 Batch 4B-1

Layer 3 Batch 4B-2

Layer 3 Batch 5 F1–F3 evaluation

Batch 5 reporting consistency micro-repair

Journal 1 Evaluation Batch 6

Journal 1 Evaluation Batch 7A
```

If an apparent contradiction is found:

```text
STOP
MANUSCRIPT_SYNC_BLOCKED —
UPSTREAM CONTRADICTION DISCOVERED: <exact contradiction>
```

Do not silently resolve it by changing scientific authority.

---

# 5. Current Evaluation Status

Recover these statuses from repository evidence and verify them independently.

Expected:

```text
P1 = CLOSED
P2 = CLOSED
P3 = CLOSED
P4 = CLOSED

F1 = CLOSED
F2 = CLOSED
F3 = CLOSED

E1 = CLOSED
E2 = CLOSED
E3 = CLOSED
E4 = CLOSED

E5 = OPEN

E6 = CLOSED
```

For E5 additionally preserve:

```text
E5_HARNESS = CLOSED

MACBOOK_REFERENCE = COMPLETE

E5_ANDROID_TARGET_BENCHMARK = DEFERRED_MANDATORY

target_hardware_evidence = false

H3 = OPEN/UNSUPPORTED
```

Do not infer E5 closure from Batch 7A.

---

# 6. Batch 7B Deferred Dependency

The following future task exists but has NOT been executed:

```text
Journal 1 Evaluation — Batch 7B
E5 Android Target-Hardware Performance Benchmark
```

Current status:

```text
BATCH_7B = DEFERRED_MANDATORY

CURRENT_BLOCKER =
REPRESENTATIVE_PHYSICAL_ANDROID_DEVICE_NOT_AVAILABLE
```

This does not block Batch 8.

It DOES prevent final target-hardware E5 completion.

The manuscript must preserve this distinction.

---

# 7. First Deliverable — Claim Inventory

Before editing the manuscript, produce:

```text
data/journal1-manuscript-evidence-sync/
    manuscript-claim-inventory.csv
```

Inspect the entire manuscript.

For every scientifically material claim classify:

```text
claim_id
manuscript_section
line_or_location
current_claim
claim_type
evidence_status
authoritative_evidence
evidence_value
revision_required
revision_reason
proposed_bounded_claim
```

Use claim types:

```text
FORMAL
IMPLEMENTATION_FIDELITY
EMPIRICAL_TRACE
PERFORMANCE_REFERENCE
PERFORMANCE_TARGET
DESIGN_INTERPRETATION
LIMITATION
FUTURE_WORK
```

Use evidence statuses:

```text
CLOSED
OPEN
DEFERRED
UNSUPPORTED
SUPERSEDED
```

Do not modify the manuscript until this inventory exists.

---

# 8. Second Deliverable — Evidence Matrix

Create:

```text
claim-evidence-matrix.csv
```

At minimum include:

```text
P1
P2
P3
P4
F1
F2
F3
E1
E2
E3
E4
E5
E6
```

Columns:

```text
claim_id
claim_class
status_before_batch8
status_authoritative
primary_evidence_file
primary_metric_or_result
manuscript_current_state
required_action
allowed_claim_scope
prohibited_overclaim
```

This matrix becomes the authority for manuscript editing during Batch 8.

---

# 9. Formal Claims P1–P4

Synchronise P1–P4 using existing formal evidence.

Do not convert formal properties into empirical hypotheses.

Maintain the distinction:

```text
formal theorem/proposition
≠
empirical observation
```

Where relevant preserve:

* totality;
* fail-safe behaviour;
* monotone degradation;
* monotonicity;
* Safety Dominance;
* C1 ≡ C3 admissible-set equivalence.

Do not describe theorem verification as empirical discovery.

---

# 10. C1 ≡ C3

Preserve the established result:

```text
C1 ≡ C3
```

at the admissible-set mapping level.

The 0.00 replay divergence is executable/trace confirmation of an already established structural equivalence.

Do NOT write that the replay "discovered" C1 and C3 are equivalent.

Where appropriate distinguish:

```text
formal/structural proposition
```

from:

```text
0.00 empirical trace confirmation
```

---

# 11. Experimental Conditions

Preserve the accepted Option C design.

Primary experimental conditions:

```text
C0 — Ungated

C1 — Binary

C2 — Proposed graduated governance
```

C3 Flehmig-style topology is:

```text
STRUCTURAL COMPARATOR / PROPOSITION
```

not a fourth primary experimental arm.

Do not accidentally reintroduce C3 as a fourth experiment.

---

# 12. F1–F3 Manuscript Synchronisation

The manuscript must no longer describe F1–F3 merely as future/planned evaluation if the final manuscript currently does so.

Synchronise them with Batch 5 evidence.

Required interpretation:

```text
F1 = implementation-fidelity containment

F2 = configured Safety-Dominance fidelity

F3 = rule-set selection correspondence
```

Do not broaden them into:

```text
real-world safety validation

decision-quality validation

optimality validation

human-behaviour validation
```

---

# 13. Batch 5 Authoritative Counts

Recover directly from the repaired Batch 5 evidence.

Expected authoritative values:

```text
primary episodes = 292

SAFE = 32

CAUTION = 260

advisory records = 454

episodes with advisory = 244

CAUTION episodes with empty advisory = 16
```

F1:

```text
episodes = 292
advisory records = 454
violations = 0
PASS
```

F2:

```text
episodes = 292
episodes_with_advisory = 244
advisory_records = 454
violations = 0
PASS
```

F3:

```text
episodes = 292
SAFE = 32
CAUTION = 260
UNSAFE gate-off = 162
mismatches = 0
PASS
```

Verify all values against files before inserting them.

Do not copy these numbers merely because they appear in this prompt.

Repository evidence is authoritative.

---

# 14. Important F1 Wording

Batch 5 contains a reporting phrase around:

```text
conclusion_types_evaluated = 244
```

Do not accidentally claim that 244 distinct advisory conclusion types exist.

The actual generated advisory type is:

```text
Delay
```

The value 244 refers to non-empty per-episode conclusion-type evaluations / episodes with advisory, according to the repaired reporting interpretation.

Write the manuscript so this cannot be misunderstood.

---

# 15. Empty Advisory Semantics

Preserve:

```text
AI(E) = ∅
```

as a legitimate result when no authorised rule fires.

In particular:

```text
16 CAUTION episodes
```

producing no advisory does NOT constitute an F1/F2/F3 failure.

Preserve the conceptual distinction:

```text
A_AI(S)
=
admissible advisory types
```

not:

```text
mandatory advisory generation
```

Do not imply:

```text
CAUTION → Delay
```

or:

```text
CAUTION → Go
```

---

# 16. Rule Activation

Where rule-level evidence is scientifically useful, preserve the final Batch 5 counts:

```text
R-CAUTION-001
selected = 260
TRUE = 130
FALSE = 130
fired = 130
advisories = 130

R-CAUTION-002
selected = 260
TRUE = 108
FALSE = 152
fired = 108
advisories = 108

R-CAUTION-003
selected = 260
TRUE = 108
FALSE = 152
fired = 108
advisories = 108

R-CAUTION-004
selected = 260
TRUE = 108
FALSE = 152
fired = 108
advisories = 108
```

Total:

```text
454 advisory records
```

Do not introduce deduplicated advisory counts unless explicitly labelled and derived.

---

# 17. F1–F3 Scope Limitation

The Batch 5 state-space evaluation is:

```text
interface-contract exhaustive
```

within its defined structural domain.

It is NOT:

```text
historical replay exhaustive

current D={m} deployment exhaustive

real-world environmental exhaustive
```

The structural state space may include EXCLUDED configurations broader than the current replay configuration.

Do not conflate structural reachability with current operational reachability.

---

# 18. E1 Synchronisation

Verify and preserve authoritative divergence values.

Expected PRIMARY:

```text
C0 ↔ C1 = 42.88%

C0 ↔ C2 = 48.69%

C1 ↔ C2 = 5.81%
```

Do not treat the 5.81% as a statistical estimate from a random population sample.

The replay is a deterministic census of the predefined retrospective study window.

---

# 19. E2 Synchronisation

Preserve:

```text
Δ_L2 PRIMARY = 5.81%

Δ_L2 RESOLUTION = 4.48%
```

Use the exact definition from the evaluation specification.

Do not reinterpret these values as:

```text
confidence intervals

prediction accuracy

risk reduction

safety improvement
```

unless directly supported by authority.

---

# 20. E3 Synchronisation

Recover E3's authoritative meaning and result directly from the evaluation specification and closed evidence.

Do not assume E3 from old manuscript wording.

If the manuscript still contains a placeholder where evidence now exists, replace it only with the repository-supported result.

If authoritative E3 evidence cannot be located:

```text
STOP
MANUSCRIPT_SYNC_BLOCKED —
E3 MARKED CLOSED BUT AUTHORITATIVE RESULT NOT LOCATED
```

Do not invent the missing result.

---

# 21. E4 Synchronisation

Verify:

```text
transitions = 3661

scheduled transitions = 3439

non-scheduled transitions = 222

oscillations = 26

hysteresis reduction = 10.36%
```

Preserve the correct causal provenance.

Do NOT claim:

```text
5416 → 3661
```

is purely attributable to g_t.

The established provenance chain is:

```text
5416
→ 5220 threshold
→ 5201 data
→ 3661 g_t
```

Only use causal language supported by that decomposition.

---

# 22. E6 Synchronisation

Preserve the C1↔C3 result according to the evaluation specification.

Expected:

```text
0.00
over 43,848 hours
```

Characterise this as trace confirmation of structural equivalence.

Do not present it as an independent empirical discovery.

---

# 23. Replay Wording

Where the manuscript describes the historical evaluation, use the established bounded wording:

> The replay is a deterministic census of all hourly records in the predefined retrospective study window, not a random sample from a broader climatological population.

Consequences:

Do not introduce:

```text
p-values

sampling confidence intervals

population inference

random-sample language
```

for deterministic replay results.

PRIMARY/RESOLUTION is sensitivity analysis, not a confidence interval.

---

# 24. E5 — Current Status

E5 MUST remain:

```text
OPEN
```

Current evidence:

```text
benchmark methodology validated

MacBook reference benchmark completed

target-hardware benchmark not completed

physical representative Android device not currently available

target_hardware_evidence = false
```

Do not write E5 as CLOSED.

---

# 25. MacBook Reference Result

Batch 7A may be reported only as:

```text
DEVELOPMENT_MACHINE_REFERENCE
```

If scientifically useful to the manuscript, the reference values may be included with explicit qualification.

Recover exact values from Batch 7A.

Expected approximate values:

```text
SAFE
mean ≈ 0.2066 ms
p95 ≈ 0.2342 ms
p99 ≈ 0.2537 ms

CAUTION
mean ≈ 0.2117 ms
p95 ≈ 0.2243 ms
p99 ≈ 0.2592 ms

UNSAFE
mean ≈ 0.1944 ms
p95 ≈ 0.2043 ms
p99 ≈ 0.2498 ms
```

Use exact repository values when editing.

Do not copy rounded prompt values if the source contains higher precision.

---

# 26. MacBook Hardware Context

If reference performance is reported, state the environment sufficiently:

```text
MacBook Pro
Apple M3 Pro
36 GB RAM
arm64
macOS 26.2
Python 3.9.6
```

Do not imply this is representative low-resource hardware.

---

# 27. Resource Results

If resource measurements are reported, preserve their measurement semantics.

MacBook Batch 7A approximately reported:

```text
peak RSS ≈ 66–67 MB
```

but this is:

```text
process-lifetime peak RSS
```

not per-episode memory consumption.

CPU result is:

```text
process user CPU time across the measured loop
```

not a normalised CPU utilisation percentage.

Do not transform these metrics into unsupported forms.

---

# 28. H3

Preserve:

```text
H3 = X ms
```

as:

```text
OPEN
UNSUPPORTED
```

No externally authorised latency threshold currently exists.

Do NOT invent:

```text
100 ms
200 ms
500 ms
1 second
interactive threshold
real-time threshold
acceptable latency
```

Do not classify MacBook performance as PASS/FAIL against H3.

---

# 29. Android Target Benchmark

Where future work / evaluation completion is discussed, state that final target-hardware characterisation remains pending on a representative physical Android device.

Do NOT state that:

```text
Android benchmark failed
```

It has not been executed.

Correct status:

```text
DEFERRED_MANDATORY
```

because the physical target device is not yet available.

---

# 30. No Android Results

Prohibited:

```text
estimated Android latency

simulated Android latency

MacBook-adjusted Android latency

emulator result presented as device evidence

CPU scaling projection

RAM scaling projection
```

No numerical Android performance result exists yet.

---

# 31. Environmental-State Semantics

Preserve the formal model:

```text
f : Y × V → S

ρ_D,τ : ∏Obs_i → Y

F_D,τ = f ∘ ρ_D,τ

S = F_D,τ(obs,v)
```

Preserve:

```text
D = {m}
```

for replay exclusion.

Do not imply dynamic growth of D.

Preserve:

```text
t ∉ D
```

Clock/time failure remains:

```text
t = ⊥
→ UNSAFE
```

---

# 32. UNSAFE Semantics

Throughout the manuscript ensure:

```text
UNSAFE
```

means the governance state where:

```text
G(S)=0
AI advisory unavailable
```

Do not automatically equate UNSAFE with:

```text
physical danger
legal prohibition
human prohibition
mandatory no-go
```

Human decision authority remains unconditional.

---

# 33. Hazard Wording

Where the reason taxonomy is discussed:

```text
fault
hazard
policy
```

is explanatory only.

`hazard` means valid environmental component crossing a configured CAUTION/UNSAFE band.

It does NOT automatically mean physical harm or proven danger.

Do not allow reason taxonomy to govern the safety state.

---

# 34. g_t Wording

Preserve the binary time classifier:

```text
SAFE:
sunrise(date, φ, λ) ≤ t < sunset(date, φ, λ)

UNSAFE:
otherwise
```

No CAUTION output.

Do not describe nighttime as proven physical danger.

Correct interpretation:

```text
nighttime
→ g_t UNSAFE
→ governance policy disables AI advisory
```

This is architecture policy.

---

# 35. Solar Method Wording

If discussed, preserve the exact established characterisation:

> faithful implementation of NOAA's published general solar-position equations with two documented simplifications

Do NOT call it:

```text
Meeus
```

USNO may be described as independent validation authority where supported.

---

# 36. Rain Classifier

Preserve the canonical two-input signature:

```text
g_r : ℝ≥0 × K → {SAFE, CAUTION, UNSAFE}

K = {0,1}
```

Preserve the WMO mapping and missing-data semantics from Appendix C.

Do not revert to an older single-input rainfall classifier.

---

# 37. Layer 3 Semantics

Preserve:

```text
G(SAFE)=1
G(CAUTION)=1
G(UNSAFE)=0
```

and:

```text
A_AI(SAFE)
=
{Go, Delay, DepartureTime, Duration}

A_AI(CAUTION)
=
{Go, Delay}

A_AI(UNSAFE)
=
∅
```

These are configured admissible sets.

Do NOT imply all admissible types are necessarily generated.

---

# 38. CAUTION-Go Resolution

Preserve Resolution B.

Correct:

```text
S = CAUTION
∧
Go ∈ AI(E)
→
Present(Go, caution_qualifier)
```

Incorrect:

```text
S = CAUTION
→
Go ∈ AI(E)
```

Do not reintroduce automatic CAUTION→Go wording.

---

# 39. Predicate Failure Semantics

Where relevant preserve:

```text
TRUE
FALSE
ERROR
```

Rule fires only if all predicates are TRUE.

Any ERROR causes episode-level refusal:

```text
AI(E)=∅
evaluation_failure=true
```

while:

```text
S
G(S)
A_AI(S)
```

remain unchanged.

Do not describe ERROR as FALSE.

---

# 40. ComponentStateTrace

Preserve the Layer 2 → Layer 3 interface semantics.

Layer 3 consumes already-computed component states.

It does NOT recompute:

```text
wind thresholds
rain thresholds
wave thresholds
solar classification
```

Do not accidentally describe Layer 3 as performing Layer 2 classification.

---

# 41. Safety Dominance

Use bounded wording.

Allowed:

> The implementation enforces the configured admissible-set constraint by construction.

Allowed:

> No generated advisory conclusion type may exceed A_AI(S).

Not allowed:

> Safety Dominance proves the recommendations are scientifically optimal.

Not allowed:

> Safety Dominance proves the system is safe in real-world operation.

The theorem verifies governance enforcement.

---

# 42. Human Authority

Ensure no manuscript wording implies the architecture replaces human authority.

Preserve:

```text
human decision authority is unconditional
```

The system governs AI participation and advisory scope.

It does not govern the fisher's final decision.

---

# 43. Domain Re-instantiability

Preserve the distinction:

```text
structural re-instantiability
```

versus:

```text
domain-specific thresholds
evidence
empirical findings
```

Do not claim that Sabah thresholds automatically generalise to another safety-critical domain.

---

# 44. Results vs Validation

Use:

```text
characterisation
formal verification
implementation-fidelity evaluation
retrospective evaluation
descriptive benchmark
```

where appropriate.

Avoid broad:

```text
validated
proven safe
demonstrated real-world safety
```

unless specifically bounded to what was actually evaluated.

---

# 45. Manuscript Structure

Do not rewrite the entire manuscript merely for style.

Make evidence-driven changes only.

Prioritise:

```text
Abstract
Introduction / contributions
Methods
Formal architecture
Evaluation design
Results
Discussion
Threats to Validity / Limitations
Conclusion
```

Only edit sections requiring scientific synchronisation.

Preserve good existing text when already correct.

---

# 46. Abstract

Audit every quantitative and contribution claim in the Abstract.

The Abstract must not contain:

```text
future result presented as completed
E5 target result
Android result
unsupported latency suitability claim
overgeneralised safety validation
```

Any quantitative result must be traceable to CLOSED evidence or explicitly identified as development-machine reference evidence.

---

# 47. Contributions

Ensure contributions distinguish:

```text
formal architecture contribution

governance implementation contribution

implementation-fidelity evidence

deterministic retrospective characterisation

performance methodology/reference evidence
```

Do not claim completed target-hardware feasibility if E5 remains open.

---

# 48. Methods / Evaluation

The evaluation section should clearly distinguish:

```text
FORMAL
IMPLEMENTATION-FIDELITY
EMPIRICAL-TRACE
PERFORMANCE
```

Do not place all evidence under a generic "experimental validation" label.

---

# 49. Results

Results must clearly distinguish:

```text
closed results
```

from:

```text
pending target-hardware evaluation
```

E5 must not appear in a completed-results table without a status qualifier.

If the manuscript uses a summary table, use something equivalent to:

```text
E5 — Target-hardware performance
Status: Pending / Deferred
```

while MacBook may be reported separately as:

```text
development-machine reference
```

---

# 50. Discussion

Update Discussion only where needed to reflect newly closed F1–F3 evidence and Batch 7A reference results.

Do not convert reference benchmark speed into deployment feasibility proof.

Appropriate interpretation:

```text
the benchmark harness is executable and produces stable descriptive measurements on the development environment
```

while:

```text
representative Android target-hardware characterisation remains pending
```

---

# 51. Threats to Validity

Ensure the manuscript explicitly captures relevant limitations.

At minimum consider:

```text
D={m} replay exclusion

deterministic retrospective window

site-specific environmental thresholds

structural state-space fidelity evaluation

absence of target-hardware E5 result

MacBook reference hardware not representative of deployment hardware

absence of human utility evaluation in Journal 1
```

Do not invent a limitation merely to lengthen the section.

---

# 52. Conclusion

The Conclusion must match the actual evidence status.

It may conclude that:

```text
formal governance properties are established

implementation fidelity has been verified within the defined state-space contract

retrospective behaviour has been characterised

benchmark methodology has been validated
```

It must NOT conclude:

```text
Android deployment feasibility established

target-hardware E5 completed

human utility demonstrated

real-world operational safety proven
```

---

# 53. No New Citations Unless Required

Do not perform a new literature search in Batch 8.

Do not introduce new external citations merely to strengthen prose.

This is repository evidence synchronisation.

If an existing manuscript claim requires external authority that is absent from the repository:

```text
OPEN
```

or flag it for later literature repair.

Do not fabricate a citation.

---

# 54. No New Experiments

Do not execute:

```text
historical replay

Layer 3 replay

new state-space experiment

new rule activation experiment

new benchmark

Android emulator

MacBook benchmark rerun

human study

simulation
```

Batch 8 consumes existing evidence only.

---

# 55. No Scientific Code Changes

Do not modify:

```text
governance/
scripts/condition_comparison.py
scripts/journal1_layer3_fidelity_evaluation.py
scripts/journal1_e5_benchmark.py
```

This is a manuscript task.

If manuscript synchronisation appears to require code repair:

```text
STOP
MANUSCRIPT_SYNC_BLOCKED —
SCIENTIFIC IMPLEMENTATION CHANGE REQUIRED
```

Do not perform the repair.

---

# 56. Quantitative Provenance

Create:

```text
quantitative-provenance.csv
```

For every number added or retained in the manuscript record:

```text
manuscript_section
quantity
value
unit
claim_id
source_file
source_field_or_location
status
```

No load-bearing number may lack repository provenance.

---

# 57. Before/After Claim Audit

Create:

```text
claim-change-log.csv
```

Columns:

```text
claim_id
section
before
after
reason
evidence
semantic_change
```

Use semantic change categories:

```text
STATUS_SYNC
RESULT_SYNC
BOUNDING
TERMINOLOGY
CAUSALITY_REPAIR
SCOPE_REPAIR
NO_CHANGE
```

---

# 58. Manuscript Diff Audit

After editing, inspect the complete diff.

Classify every changed paragraph:

```text
evidence synchronisation
claim bounding
terminology correction
result insertion
limitation update
```

Flag any paragraph that introduces a scientific proposition absent from the evidence matrix.

Such a paragraph must be removed or marked OPEN.

---

# 59. Internal Consistency Search

Search the final manuscript for outdated or risky wording including:

```text
planned
will evaluate
will test
future experiment
H1
H2
H3
H4
validated
proven safe
real-time
acceptable latency
low-resource performance confirmed
C3
CAUTION
Go recommendation
UNSAFE
utility
human study
Layer 3 replay
```

Do not blindly remove these terms.

Inspect each occurrence for semantic consistency.

---

# 60. Numerical Consistency Search

Search the manuscript for all important values including:

```text
42.88
48.69
5.81
4.48
3661
3439
222
26
10.36
43848
292
260
244
454
130
108
```

Verify every occurrence against authoritative evidence and context.

Do not require every value to appear.

Only verify those that do.

---

# 61. E5 Number Search

If Batch 7A MacBook numbers are included, verify:

```text
0.206615
0.211715
0.194423

0.234216
0.224271
0.204335

0.253667
0.259178
0.249837
```

against authoritative Batch 7A files.

If manuscript rounding differs, document the rounding rule.

---

# 62. Integrity

Hash before/after all frozen scientific files.

Expected unchanged:

```text
docs/canonical/appendix-c-formalisation.md
docs/canonical/architecture-illustration.md

publications/active/journal-1/evaluation-specification.md
publications/active/journal-1/algorithm-specification.md
publications/active/journal-1/layer3-prototype-specification.md

governance/*.py

scripts/condition_comparison.py
scripts/journal1_layer3_fidelity_evaluation.py
scripts/journal1_e5_benchmark.py
```

Expected changed:

```text
publications/active/journal-1/submissions/v1-initial-submission/manuscript.md
```

and new Batch 8 evidence artefacts.

---

# 63. Batch 8 Evidence Directory

Create:

```text
data/journal1-manuscript-evidence-sync/
```

Required:

```text
manuscript-claim-inventory.csv
claim-evidence-matrix.csv
quantitative-provenance.csv
claim-change-log.csv
manuscript-diff-audit.md
e5-status-audit.md
integrity.json
verification.json
report.md
```

---

# 64. e5-status-audit.md

This file must explicitly verify that the final manuscript does not accidentally close E5.

Record:

```text
E5 = OPEN

E5_HARNESS = CLOSED

MACBOOK_REFERENCE = COMPLETE

MACBOOK_CLASSIFICATION =
DEVELOPMENT_MACHINE_REFERENCE

target_hardware_evidence = false

BATCH_7B =
DEFERRED_MANDATORY

TARGET =
physical representative Android smartphone

H3 =
OPEN/UNSUPPORTED
```

List every manuscript occurrence discussing E5 and verify its wording.

---

# 65. Verification

At minimum verify:

```text
active_manuscript_correct

P1_status_synced
P2_status_synced
P3_status_synced
P4_status_synced

F1_status_synced
F2_status_synced
F3_status_synced

F1_counts_verified
F2_counts_verified
F3_counts_verified

E1_synced
E2_synced
E3_synced
E4_synced
E6_synced

C1_C3_structural_semantics_preserved

Option_C_conditions_preserved

deterministic_replay_wording_preserved

PRIMARY_RESOLUTION_not_CI

E5_remains_open

MacBook_reference_bounded

target_hardware_evidence_false

Android_result_not_invented

H3_open_unsupported

no_latency_threshold_invented

no_real_time_claim

no_deployment_suitability_claim

no_CAUTION_to_Go

no_CAUTION_to_Delay

UNSAFE_governance_semantics_preserved

human_authority_preserved

Safety_Dominance_bounded

ComponentStateTrace_boundary_preserved

predicate_failure_semantics_preserved

Batch5_state_space_scope_bounded

no_new_experiment

no_new_external_evidence

no_scientific_code_change

canonical_files_unchanged

specification_files_unchanged

quantitative_provenance_complete

manuscript_diff_audited

no_unresolved_internal_contradiction
```

Use:

```text
PASS
FAIL
OPEN
```

---

# 66. Batch 8 Success Condition

Batch 8 succeeds when:

```text
all CLOSED claims are accurately represented in the manuscript

F1–F3 are synchronised with final Batch 5 evidence

E1–E4 and E6 are synchronised with closed evidence

all load-bearing quantitative values have provenance

formal claims remain distinguished from empirical claims

MacBook benchmark remains reference-only

E5 remains explicitly open

Android target benchmark remains deferred

H3 remains open/unsupported

no unsupported scientific claim is introduced

no frozen scientific implementation is changed

final manuscript is internally consistent with current repository authority
```

---

# 67. Important Closure Boundary

Batch 8 is NOT:

```text
FINAL JOURNAL 1 REVIEWER-READY CLOSURE
```

because E5 target-hardware evidence remains pending.

Do not use:

```text
JOURNAL 1 MANUSCRIPT REVIEWER-READY
```

or equivalent final wording.

The purpose is evidence synchronisation, not final manuscript closure.

---

# 68. Exact Closure

If all verification checks pass:

```text
JOURNAL 1 MANUSCRIPT BATCH 8 CLOSED —
CLOSED EVIDENCE SYNCHRONISED AND OPEN E5 TARGET-HARDWARE DEPENDENCY PRESERVED
```

Post-Batch status:

```text
P1-P4 = CLOSED

F1-F3 = CLOSED

E1-E4 = CLOSED

E5 = OPEN
E5_HARNESS = CLOSED
MACBOOK_REFERENCE = COMPLETE
E5_ANDROID_TARGET_BENCHMARK = DEFERRED_MANDATORY
H3 = OPEN/UNSUPPORTED

E6 = CLOSED

MANUSCRIPT_EVIDENCE_SYNC = CLOSED

FINAL_REVIEWER_READY = false
```

---

# 69. Next Task Decision

After Batch 8, do NOT automatically execute Batch 7B.

The physical Android device is still unavailable.

Instead identify exactly one next executable task that:

1. does not require the Android device;
2. does not duplicate closed work;
3. does not fabricate E5 evidence;
4. moves Journal 1 closer to reviewer readiness.

The likely next task should be a bounded manuscript consistency / reviewer audit, but determine this from the actual Batch 8 result.

Do not execute it automatically.

---

# 70. Required Final Response

Return:

1. Verdict
2. Branch
3. HEAD before
4. HEAD after
5. Active manuscript path
6. Manuscript SHA-256 before
7. Manuscript SHA-256 after
8. Number of material claims inventoried
9. P1–P4 final statuses
10. F1–F3 final statuses
11. E1–E6 final statuses
12. F1 authoritative counts
13. F2 authoritative counts
14. F3 authoritative counts
15. E1 values
16. E2 values
17. E3 result
18. E4 values
19. E6 result
20. E5 status
21. MacBook reference status
22. Android target benchmark status
23. H3 status
24. Number of manuscript claims changed
25. Number of quantitative values provenance-verified
26. Any unsupported claim removed/bounded
27. Any contradiction discovered
28. Canonical integrity result
29. Scientific specification integrity result
30. Governance/code integrity result
31. Verification PASS/FAIL/OPEN totals
32. Files created
33. Files modified
34. Exact closure/status line
35. Exactly one recommended next task

Do not start the next task automatically.
