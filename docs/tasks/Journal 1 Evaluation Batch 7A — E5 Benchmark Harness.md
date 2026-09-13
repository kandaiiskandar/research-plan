# Journal 1 Evaluation

## Batch 7A — E5 Benchmark Harness & MacBook Reference Run

### Task Type

Performance benchmark methodology implementation, engineering validation, and development-machine reference measurement.

This task prepares the executable benchmark methodology required for E5.

This task MAY execute the benchmark on the researcher's MacBook.

However:

> The MacBook result is a development-machine reference benchmark only.

It MUST NOT be reported as the final target-hardware E5 result unless independent evidence establishes that the MacBook belongs to the authorised low-resource target deployment hardware class.

The purpose of Batch 7A is therefore:

1. implement the E5 benchmark harness;
2. define a reproducible workload and instrumentation procedure;
3. validate that the benchmark measures the authorised governance execution path;
4. run a MacBook reference benchmark;
5. determine whether the methodology is ready for target-hardware execution.

---

# 1. Branch

Create:

```text
eval/journal1-e5-benchmark-harness
```

Record before work:

```text
current branch
HEAD
working-tree status
Batch 6 closure commit
MacBook hardware information
macOS version
Python version
```

Do not mix unrelated work into this branch.

---

# 2. Frozen Upstream State

Treat as CLOSED and frozen:

```text
P1–P4

F1
F2
F3

E1
E2
E3
E4
E6

Layer 3 Batch 1
Layer 3 Batch 2
Layer 3 Batch 3
Layer 3 Batch 4A
Layer 3 Batch 4B-1
Layer 3 Batch 4B-2
Layer 3 Batch 5
Journal 1 Evaluation Batch 6
```

Batch 6 established:

```text
E5 = READY
evaluation_mode = DESCRIPTIVE

L3_RETROSPECTIVE_REPLAY = NOT_REQUIRED

UTILITY_CONSTRUCT = DEFER_TO_HUMAN_STUDY

HUMAN_STUDY_REQUIRED_FOR_J1 = false
```

Do not reopen these decisions.

---

# 3. E5 Scientific Authority

Read in full:

```text
publications/active/journal-1/evaluation-specification.md
publications/active/journal-1/algorithm-specification.md
publications/active/journal-1/layer3-prototype-specification.md
```

Read Batch 6 evidence:

```text
data/journal1-post-fidelity-plan/
    report.md
    claim-status-matrix.csv
    evaluation-dependency-graph.md
    e5-authority-assessment.md
    next-evaluation-decision.json
    verification.json
    integrity.json
```

Do not redefine E5.

---

# 4. Authorised E5 Measurements

The benchmark methodology must support measurement of:

```text
wall-clock latency:
    mean
    maximum
    p95
    p99

resource measurements:
    peak memory
    CPU usage
```

for the authorised governance execution path.

Recover the exact measured path from `evaluation-specification.md`.

Expected conceptual path:

```text
environmental input
        ↓
classification
        ↓
G(S)
        ↓
A_AI(S)
        ↓
RS(S) supply
```

Do not blindly implement this diagram.

Use the exact repository authority to determine what constitutes one E5 governance pass.

---

# 5. Critical Layer Boundary Check

Before writing the benchmark, determine exactly which existing executable functions correspond to:

```text
classification
G(S)
A_AI(S)
RS(S)
```

Produce:

```text
data/journal1-e5-benchmark/
    execution-path-audit.md
```

For each stage document:

```text
stage
authoritative specification
implementation file
implementation function/class
input
output
included_in_E5
reason
```

Do NOT duplicate Layer 2 logic merely to make benchmarking convenient.

Use existing implementation wherever available.

If an authorised E5 stage has no executable implementation:

```text
STOP
E5_HARNESS_BLOCKED —
AUTHORISED EXECUTION STAGE NOT IMPLEMENTED: <stage>
```

Do not substitute a mock and call it E5.

---

# 6. MacBook Scientific Boundary

The MacBook run MUST be classified:

```text
DEVELOPMENT_MACHINE_REFERENCE
```

NOT:

```text
TARGET_HARDWARE_E5
```

unless repository authority explicitly establishes otherwise.

Every artefact containing MacBook results must include:

> These measurements are development-machine reference measurements used to validate the E5 benchmark methodology. They are not the final target-hardware E5 evidence and do not establish deployment suitability.

Do not omit this boundary.

---

# 7. Hardware Capture

Automatically capture, where available:

```text
Mac model
chip / processor
CPU architecture
physical memory
OS version
Python version
power mode if detectable
```

For Apple Silicon record at minimum whether the machine is:

```text
M1
M2
M3
M4
M5
or other
```

Do not infer missing specifications.

Record unknown fields as:

```text
UNKNOWN
```

Create:

```text
hardware-profile.json
```

---

# 8. Benchmark Workload

Design a deterministic workload representative of one authorised E5 governance pass.

The workload must:

```text
exercise the real governance implementation

avoid network requests

avoid LLM calls

avoid random environmental inputs unless a fixed seed and scientific reason exist

avoid disk I/O inside the timed region unless E5 explicitly requires it

avoid logging overhead inside the timed region where possible

avoid benchmark setup inside the measured governance pass
```

Separate:

```text
benchmark setup
```

from:

```text
timed governance execution
```

---

# 9. Workload Coverage

Do not benchmark only one convenient state.

At minimum determine whether execution characteristics differ for:

```text
SAFE
CAUTION
UNSAFE
```

because governance behaviour differs by state.

In particular:

```text
UNSAFE
→ G(S)=0
→ gate-off
```

while SAFE/CAUTION may proceed to rule-set supply.

If the execution path differs materially, benchmark states separately.

Do NOT combine them into one average before preserving per-state results.

---

# 10. Representative Episodes

Construct benchmark episodes using already-authorised input semantics.

Do not invent new thresholds or new governance states.

Episodes should cover the relevant execution paths, for example:

```text
SAFE path
CAUTION path
UNSAFE gate-off path
```

If ComponentStateTrace is required for the executable path, construct only states consistent with the frozen interface contract.

Do not include inconsistent states in primary performance measurements.

Interface-invalid cases may be benchmarked separately only as supplementary engineering diagnostics.

---

# 11. R-CAUTION Rules

Preserve the currently authorised rules:

```text
R-CAUTION-001
R-CAUTION-002
R-CAUTION-003
R-CAUTION-004
```

Preserve:

```text
R-SAFE-001 = deferred
```

Do not implement R-SAFE-001.

Do not introduce:

```text
CAUTION → Go

DepartureTime

Duration
```

Do not change rule predicates.

---

# 12. Warm-Up

Runtime benchmarking may be affected by:

```text
imports
cache population
memory allocation
interpreter warm-up
OS scheduling
```

Implement an explicit warm-up phase.

Warm-up iterations MUST NOT be included in the primary latency distribution.

Record:

```text
warmup_iterations
measurement_iterations
```

Do not choose counts silently.

Explain the engineering rationale.

The counts are benchmark-method parameters, not scientific thresholds.

---

# 13. Repetitions

Run enough repeated measurements to estimate:

```text
mean
maximum
p95
p99
```

without using the 43,848-hour replay as the repetition mechanism.

The repetition count must be explicitly recorded.

Do not treat repeated timing observations as independent environmental observations.

They are runtime measurements of the same bounded workload.

---

# 14. Clock

Use a high-resolution monotonic clock suitable for microbenchmarking.

For Python, inspect whether:

```text
time.perf_counter_ns()
```

is appropriate.

Prefer nanosecond capture internally.

Convert to:

```text
milliseconds
```

for reporting.

Do not use wall-calendar timestamps to measure elapsed execution time.

---

# 15. Raw Timing Preservation

Never retain only summary statistics.

Create raw timing output containing at least:

```text
run_id
state
episode_id / workload_id
iteration
latency_ns
latency_ms
```

Create:

```text
latency-raw.csv
```

All summary statistics must be reproducible from this file.

---

# 16. Latency Statistics

Calculate:

```text
n
mean
median
minimum
maximum
p50
p95
p99
standard deviation
```

E5 requires at least:

```text
mean
maximum
p95
p99
```

Median, minimum and standard deviation may be included as descriptive supplementary statistics.

Do NOT create an acceptance test.

---

# 17. Confidence Intervals

The evaluation specification permits inferential treatment for timing because runtime measurements carry genuine variance.

However, do not add confidence intervals merely because they are statistically possible.

First determine whether the authoritative E5 specification requires them.

If required or clearly authorised, document the method.

If not required:

```text
CI = NOT_REQUIRED
```

Do not confuse timing variance with uncertainty in the deterministic environmental replay.

---

# 18. CPU Measurement

Implement CPU measurement using an appropriate reproducible mechanism available on macOS.

Document:

```text
measurement tool/library
sampling interval if applicable
whether CPU is process-level or system-level
normalisation
limitations
```

Do not report a CPU percentage without explaining its denominator.

If reliable process-level CPU measurement cannot be obtained:

```text
CPU_MEASUREMENT = LIMITED
```

and document why.

Do not fabricate a value.

---

# 19. Memory Measurement

Measure peak memory using a reproducible method.

Document whether the measurement represents:

```text
RSS
Python allocation peak
process memory
system memory
```

Prefer a metric that can later be reproduced on target hardware.

Do not call Python allocation memory "total device memory usage."

Clearly name the metric actually measured.

---

# 20. Instrumentation Overhead

Determine whether CPU/memory instrumentation materially affects latency.

Where practical:

```text
latency benchmark
```

and:

```text
resource benchmark
```

may be separate runs.

If separated, explicitly state this.

Do not silently include expensive monitoring inside the latency critical section.

---

# 21. Benchmark Harness

Create an executable benchmark script under an appropriate repository location, for example:

```text
scripts/journal1_e5_benchmark.py
```

Use repository naming conventions if an existing convention differs.

The harness should support:

```text
--warmup
--iterations
--output-dir
```

and, if useful:

```text
--state
--workload
```

Do not overengineer a benchmark framework.

---

# 22. Determinism

Where the governance result itself is deterministic, verify before timing that repeated execution returns the expected governance result.

Performance variance is allowed.

Governance output variance is not.

Before benchmark collection verify:

```text
same input
→
same governance output
```

for each benchmark workload.

If governance outputs vary:

```text
STOP
E5_HARNESS_INVALID —
NONDETERMINISTIC GOVERNANCE OUTPUT
```

---

# 23. Existing Engineering Tests

Before benchmark:

```text
run existing governance engineering test suite
```

Expected upstream baseline:

```text
139 tests PASS
```

If repository test count has legitimately increased since Batch 4B-2, report the actual count and explain provenance.

Do not silently accept regressions.

If any frozen governance test fails:

```text
STOP
E5_HARNESS_BLOCKED —
UPSTREAM GOVERNANCE REGRESSION
```

---

# 24. Benchmark Harness Tests

Add engineering tests for the benchmark harness where appropriate.

At minimum verify:

```text
warm-up excluded from measured samples

requested iteration count respected

raw timing rows equal expected count

percentile calculation reproducible

summary derived from raw timing

hardware metadata emitted

state/workload labels preserved

governance outputs deterministic
```

Do not modify scientific governance behaviour merely to make tests pass.

---

# 25. MacBook Reference Run

After harness validation, execute the benchmark on the current MacBook.

This run is authorised.

Classification:

```text
run_type = DEVELOPMENT_MACHINE_REFERENCE
```

NOT:

```text
run_type = TARGET_HARDWARE_E5
```

Record exact:

```text
hardware
OS
Python
git commit
benchmark configuration
warm-up count
measurement count
instrumentation
date/time
```

---

# 26. MacBook Results

Report per execution path/state where appropriate:

```text
SAFE
CAUTION
UNSAFE
```

At minimum:

```text
n
mean_ms
max_ms
p95_ms
p99_ms
peak_memory
CPU
```

Do not report only a global mean.

If a combined distribution is produced, retain per-state results as primary diagnostics.

---

# 27. No H3 PASS/FAIL

The following remains frozen:

```text
H3 = X ms
```

Status:

```text
OPEN
UNSUPPORTED
```

Therefore prohibited statements include:

```text
E5 passed the latency requirement.

The architecture satisfies the latency threshold.

The system is sufficiently fast.

The architecture is real-time.

The system is suitable for low-resource deployment because latency is below X ms.
```

unless future external authority establishes such a criterion.

---

# 28. Allowed MacBook Claims

Allowed:

> On the development MacBook reference environment, the frozen governance implementation exhibited a mean execution latency of X ms, with p95 Y ms and p99 Z ms under the stated benchmark workload.

Allowed:

> These measurements validate the executable benchmark methodology and provide a development-machine reference baseline.

Not allowed:

> These measurements establish deployment performance for low-resource coastal-fisher hardware.

Not allowed:

> These measurements prove the system is fast enough.

---

# 29. Target-Hardware Readiness

After the MacBook run, determine whether the benchmark methodology can be transferred unchanged or with only environment-specific instrumentation changes to:

```text
commodity smartphone
or
low-cost SBC
```

Produce:

```text
target-hardware-readiness.md
```

Classify:

```text
TARGET_HARDWARE_BENCHMARK_READY = true | false
```

If false, state exact blocker.

---

# 30. Do Not Select Target Device Arbitrarily

Batch 7A does NOT need to select the final target device.

It should document the minimum device-selection criteria implied by existing authority.

Examples may include:

```text
representative of authorised hardware class
able to execute required software stack
resource-constrained relative to development machine
reproducibly identifiable model/specification
available for repeatable benchmarking
```

Do not introduce arbitrary RAM, CPU, price or latency cut-offs unless already authorised.

---

# 31. No Retrospective Replay

Do not connect Layer 3 to the 43,848-hour historical replay.

Batch 6 already determined:

```text
L3_RETROSPECTIVE_REPLAY = NOT_REQUIRED
```

Do not reopen it.

---

# 32. No Human Study

Do not:

```text
recruit fishers
measure trust
measure usability
measure utility
measure decision quality
```

These are outside Batch 7A.

---

# 33. No Scientific Architecture Changes

Do not modify:

```text
canonical thresholds

f

ρ_Dτ

F_Dτ

G(S)

A_AI(S)

RS(S)

Safety Dominance

ComponentStateTrace semantics

predicate failure policy

human authority

advisory rules
```

If benchmark execution exposes an implementation bug:

```text
STOP
E5_HARNESS_BLOCKED —
IMPLEMENTATION DEFECT DISCOVERED
```

Document the defect.

Do not repair scientific implementation inside Batch 7A.

---

# 34. Evidence Directory

Create:

```text
data/journal1-e5-benchmark/
```

Required artefacts:

```text
execution-path-audit.md
benchmark-protocol.md
hardware-profile.json
workload-manifest.json
latency-raw.csv
latency-summary.csv
resource-summary.json
reference-run.json
target-hardware-readiness.md
verification.json
integrity.json
report.md
```

If CPU or memory requires additional raw files, include them.

---

# 35. benchmark-protocol.md

Document:

```text
scientific purpose
E5 authority
measured execution path
hardware classification
workloads
warm-up procedure
iteration procedure
clock
latency measurement
CPU measurement
memory measurement
instrumentation overhead treatment
statistics
reproducibility procedure
claim boundary
target-hardware transfer procedure
```

This protocol should be reusable unchanged, as far as possible, for the later target-hardware run.

---

# 36. workload-manifest.json

For every workload record:

```text
workload_id
expected_S
expected_G
expected_A_AI
expected_RS
input_source
interface_consistency
included_in_primary_benchmark
reason
```

Do not introduce unsupported advisory semantics.

---

# 37. latency-summary.csv

At minimum:

```text
run_type
hardware_id
state
workload_id
n
mean_ms
median_ms
min_ms
max_ms
p95_ms
p99_ms
std_ms
```

Do not include:

```text
PASS
FAIL
acceptable
unacceptable
```

performance labels.

---

# 38. reference-run.json

Include:

```text
run_type = DEVELOPMENT_MACHINE_REFERENCE

scientific_status = REFERENCE_ONLY

target_hardware_evidence = false

hardware_profile
git_HEAD
benchmark_script_hash
warmup_iterations
measurement_iterations
workloads
latency_summary
resource_summary
limitations
```

---

# 39. Integrity

Hash before/after:

```text
docs/canonical/appendix-c-formalisation.md
docs/canonical/architecture-illustration.md

publications/active/journal-1/
    submissions/v1-initial-submission/manuscript.md
    evaluation-specification.md
    algorithm-specification.md
    layer3-prototype-specification.md

governance/*.py

scripts/condition_comparison.py
scripts/journal1_layer3_fidelity_evaluation.py
```

Expected:

```text
UNCHANGED
```

The new benchmark script is allowed.

Existing scientific implementation is not.

---

# 40. Verification

At minimum:

```text
Batch6_frozen

E5_authority_recovered

E5_execution_path_audited

no_Layer2_logic_duplicated

MacBook_classified_reference_only

target_hardware_evidence_false

hardware_profile_recorded

workload_manifest_valid

SAFE_path_covered

CAUTION_path_covered

UNSAFE_path_covered

warmup_excluded

iteration_count_correct

monotonic_high_resolution_clock_used

raw_timings_preserved

summary_reproducible_from_raw

mean_reported

max_reported

p95_reported

p99_reported

memory_measurement_documented

CPU_measurement_documented

instrumentation_limitations_documented

governance_output_deterministic

existing_governance_tests_pass

benchmark_harness_tests_pass

H3_threshold_not_invented

no_latency_acceptability_claim

no_target_deployment_claim_from_MacBook

no_retrospective_replay

no_human_study

no_new_rule

no_new_threshold

no_canonical_change

no_manuscript_change

frozen_governance_unchanged

TARGET_HARDWARE_BENCHMARK_READY_resolved
```

Use:

```text
PASS
FAIL
OPEN
```

---

# 41. Batch 7A Success Condition

Batch 7A succeeds when:

```text
benchmark harness exists

authorised E5 execution path is measured

methodology is reproducible

MacBook reference run completes

raw measurements are preserved

summary statistics reproduce from raw measurements

CPU/memory methodology is documented

MacBook result remains reference-only

no H3 threshold is invented

no target-hardware suitability claim is made

target-hardware benchmark readiness is explicitly resolved
```

Batch 7A does NOT close E5.

---

# 42. Post-Batch Status

If successful:

```text
E5_HARNESS = CLOSED
MACBOOK_REFERENCE = COMPLETE
E5_TARGET_HARDWARE = PENDING
```

and:

```text
TARGET_HARDWARE_BENCHMARK_READY = true
```

if methodology can proceed.

Do NOT set:

```text
E5 = CLOSED
```

from the MacBook reference run.

---

# 43. Exact Closure

If successful:

```text
JOURNAL 1 EVALUATION BATCH 7A CLOSED —
E5 BENCHMARK HARNESS VALIDATED AND MACBOOK REFERENCE BASELINE ESTABLISHED
```

If target-hardware transfer is ready, additionally report:

```text
E5 TARGET-HARDWARE BENCHMARK READY
```

If blocked:

```text
JOURNAL 1 EVALUATION BATCH 7A REMAINS OPEN —
<EXACT BLOCKER>
```

---

# 44. Next Task Decision

After Batch 7A, select exactly one:

```text
Batch 7B — E5 Target-Hardware Performance Benchmark
```

if:

```text
TARGET_HARDWARE_BENCHMARK_READY = true
```

or:

```text
E5 Benchmark Methodology Repair
```

if the harness itself is scientifically or technically invalid.

Do not begin Batch 7B automatically.

---

# 45. Required Final Response

Return:

1. Verdict
2. Branch
3. HEAD
4. Batch 6 closure commit
5. MacBook model
6. Processor/chip
7. RAM
8. macOS version
9. Python version
10. E5 execution path actually benchmarked
11. Benchmark script
12. Benchmark script SHA-256
13. Workloads used
14. Warm-up iterations
15. Measurement iterations
16. Timing clock
17. SAFE latency summary
18. CAUTION latency summary
19. UNSAFE latency summary
20. Overall reference latency summary, if calculated
21. Peak memory result
22. CPU result
23. Instrumentation limitations
24. Existing governance test result
25. Benchmark harness test result
26. Governance determinism result
27. H3 status
28. MacBook scientific classification
29. `target_hardware_evidence`
30. `TARGET_HARDWARE_BENCHMARK_READY`
31. Any blocker
32. Files created
33. Integrity result
34. Verification PASS/FAIL/OPEN totals
35. Exact closure/status line
36. Exactly one next task

Do NOT start the next task automatically.
