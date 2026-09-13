# DEFERRED MANDATORY TASK

## Journal 1 Evaluation — Batch 7B

## E5 Android Target-Hardware Performance Benchmark

### EXECUTION STATUS

```text
DO NOT EXECUTE NOW

STATUS = DEFERRED_MANDATORY
CURRENT_BLOCKER = REPRESENTATIVE_ANDROID_DEVICE_NOT_AVAILABLE
BLOCKING_CURRENT_J1_WORK = false
BLOCKING_FINAL_E5_CLOSURE = true
```

This task MUST be executed later when a representative Android device is physically available.

Do not substitute:

* MacBook results;
* desktop emulators;
* Android emulators;
* CI runners;
* cloud machines;
* development workstations;
* simulated CPU throttling;

for physical target-hardware evidence.

---

# 1. Purpose

Execute the final target-hardware component of Journal 1 E5:

> Descriptive performance characterisation of the frozen governance architecture on a representative commodity Android smartphone.

This task measures the same authorised governance execution path validated in Batch 7A.

It does NOT establish a new architecture.

It does NOT introduce a new scientific claim.

It does NOT establish an acceptance threshold.

---

# 2. Prerequisites

Do not begin execution until all prerequisites are satisfied.

Required:

```text
BATCH_7A = CLOSED

E5_HARNESS = CLOSED

TARGET_HARDWARE_BENCHMARK_READY = true

PHYSICAL_ANDROID_DEVICE_AVAILABLE = true
```

If:

```text
PHYSICAL_ANDROID_DEVICE_AVAILABLE = false
```

STOP immediately with:

```text
BATCH 7B DEFERRED —
REPRESENTATIVE PHYSICAL ANDROID TARGET DEVICE NOT YET AVAILABLE
```

Do not generate synthetic performance results.

---

# 3. Target Hardware Class

The target hardware class is:

```text
commodity Android smartphone
```

The device should represent the intended mobile deployment context for low-resource coastal fisheries.

Do not invent arbitrary scientific minimums for:

```text
CPU
RAM
price
Android version
benchmark latency
```

Device selection must be justified as representative rather than selected because it produces favourable benchmark results.

---

# 4. Hardware Selection Record

Before running any benchmark, record:

```text
manufacturer
model
commercial release class
SoC
CPU architecture
CPU configuration where available
physical RAM
Android version
kernel version where available
available storage
battery state
power source
thermal state where measurable
Python/runtime environment
benchmark dependencies
```

Unknown fields must be:

```text
UNKNOWN
```

Do not infer specifications.

Create:

```text
android-hardware-profile.json
```

---

# 5. Physical Device Requirement

The benchmark MUST run on the physical Android device.

Prohibited primary evidence:

```text
Android Studio emulator
AVD
Genymotion
MacBook-hosted Android environment
Docker
virtual machine
cloud Android instance
CI benchmark
CPU simulation
```

These may be used for engineering preparation but not E5 target-hardware evidence.

---

# 6. Android Runtime

Determine the minimum reproducible method required to execute the frozen governance implementation on Android.

Possible implementation mechanisms must be evaluated based on compatibility with the existing Python governance implementation.

Do not rewrite the governance architecture merely to make Android execution easier.

The preferred principle is:

> Preserve the frozen scientific implementation and benchmark semantics as closely as technically possible.

Document:

```text
runtime
Python version
dependency installation
numpy version
pandas version
execution command
environment configuration
```

---

# 7. Batch 7A Authority

Recover and read in full:

```text
data/journal1-e5-benchmark/execution-path-audit.md
data/journal1-e5-benchmark/benchmark-protocol.md
data/journal1-e5-benchmark/workload-manifest.json
data/journal1-e5-benchmark/reference-run.json
data/journal1-e5-benchmark/target-hardware-readiness.md
data/journal1-e5-benchmark/verification.json
data/journal1-e5-benchmark/integrity.json
```

Also inspect:

```text
scripts/journal1_e5_benchmark.py
```

Do not redefine the E5 execution path.

---

# 8. Frozen Scientific Authority

Do not modify:

```text
f

ρ_D,τ

F_D,τ

G(S)

A_AI(S)

RS(S)

Safety Dominance

ComponentStateTrace

predicate failure semantics

human authority

canonical thresholds

canonical advisory rules
```

Preserve:

```text
R-CAUTION-001
R-CAUTION-002
R-CAUTION-003
R-CAUTION-004
```

Preserve:

```text
R-SAFE-001 = DEFERRED
```

---

# 9. Workload Equivalence

Batch 7B must reproduce the Batch 7A benchmark workloads:

```text
W-SAFE
W-CAUTION
W-UNSAFE
```

Do not silently change their environmental inputs.

Verify their expected outputs before timing.

Required:

```text
W-SAFE
S = SAFE
G = 1

W-CAUTION
S = CAUTION
G = 1
R-CAUTION-002 fires

W-UNSAFE
S = UNSAFE
G = 0
AI(E) = ∅
```

If Android execution produces different governance outputs from Batch 7A:

```text
STOP

ANDROID GOVERNANCE FIDELITY FAILURE —
TARGET EXECUTION DOES NOT MATCH FROZEN GOVERNANCE OUTPUT
```

Do not benchmark further until independently reviewed.

---

# 10. Benchmark Methodology

Preserve the validated Batch 7A methodology as far as technically possible.

This includes:

```text
warm-up separated from measurement

high-resolution monotonic timing

raw timing preservation

per-state measurement

SAFE/CAUTION/UNSAFE separated

determinism verification before timing

resource instrumentation separated from latency critical section
```

Any Android-specific deviation must be explicitly documented.

---

# 11. Iterations

Recover the validated Batch 7A benchmark parameters.

Do not silently change them.

If Android limitations require a methodological change, document:

```text
Batch7A_parameter
Batch7B_parameter
reason_for_change
effect_on_comparability
```

The number of iterations is a measurement-design parameter, not an acceptance threshold.

---

# 12. Thermal Management

Android devices can change CPU frequency because of thermal conditions.

Before execution, document where technically observable:

```text
battery percentage
charging state
device temperature
thermal status
background applications
power-saving mode
```

Avoid intentionally cooling, heating, overclocking or modifying the device to obtain favourable results.

If thermal throttling occurs, record it.

Do not silently discard slow runs.

---

# 13. Background Activity

Minimise avoidable background workload where practical.

Document the procedure.

Do not claim the Android device is operating under laboratory-isolated conditions unless that is actually established.

---

# 14. Latency

Required primary descriptive statistics:

```text
n
mean
maximum
p95
p99
```

Also retain where available:

```text
median
minimum
standard deviation
```

Preserve every raw timing observation.

Do not report only summary statistics.

---

# 15. CPU

Measure CPU consumption using a method valid for the selected Android runtime.

Document exactly what the value represents.

Possible interpretations must not be conflated:

```text
process CPU time
CPU utilisation percentage
system CPU
single-core normalised utilisation
multi-core utilisation
```

If reliable CPU measurement cannot be obtained:

```text
CPU_MEASUREMENT = LIMITED
```

Explain the limitation.

Do not invent values.

---

# 16. Memory

Measure memory using the most reproducible process-level method available.

Document whether the metric is:

```text
RSS
PSS
Python allocation peak
process memory
system memory
```

Do not relabel one metric as another.

---

# 17. Raw Evidence

Create a new evidence directory:

```text
data/journal1-e5-android-benchmark/
```

Required:

```text
android-hardware-profile.json
android-environment.json
benchmark-protocol-android.md
workload-equivalence.json
latency-raw.csv
latency-summary.csv
resource-summary.json
android-run.json
macbook-reference-comparison.csv
verification.json
integrity.json
report.md
```

---

# 18. Comparison With MacBook

The MacBook reference result may be included for context.

Compare descriptively:

```text
Android mean
MacBook mean

Android p95
MacBook p95

Android p99
MacBook p99
```

Do not treat MacBook as a control group.

Do not perform significance testing merely to establish that Android is slower or faster.

Do not claim superiority.

---

# 19. No H3 Threshold

Preserve:

```text
H3 = X ms
STATUS = OPEN / UNSUPPORTED
```

Therefore Android E5 remains:

```text
DESCRIPTIVE PERFORMANCE CHARACTERISATION
```

Do NOT invent:

```text
100 ms
200 ms
500 ms
1 second
real-time threshold
interactive threshold
acceptable latency
```

unless a future independently authorised source establishes such a criterion.

---

# 20. Important E5 Closure Semantics

Obtaining Android measurements may close the **measurement requirement** for E5.

It does NOT automatically establish:

```text
acceptable performance
real-time performance
deployment suitability
operational safety
decision quality
utility
human trust
```

The correct bounded conclusion is:

> The governance implementation was executably characterised on the stated representative Android target device under the documented benchmark protocol.

---

# 21. No Historical Replay

Do not connect Layer 3 to the 43,848-hour historical replay.

Frozen:

```text
L3_RETROSPECTIVE_REPLAY = NOT_REQUIRED
```

---

# 22. No Human Study

Do not conduct:

```text
fisher interviews
user testing
trust evaluation
usability testing
decision utility evaluation
```

Human-study work remains outside E5.

---

# 23. Integrity

Verify that target-hardware execution did not modify frozen scientific authority.

Hash and compare relevant:

```text
canonical documents
evaluation specification
algorithm specification
Layer 3 specification
governance implementation
canonical rules
Batch 7A benchmark script
```

Expected:

```text
UNCHANGED
```

Android-specific execution wrappers may be added where technically necessary, but they must not alter governance semantics.

---

# 24. Verification

At minimum verify:

```text
physical_android_device_used

device_identity_recorded

runtime_recorded

Batch7A_methodology_recovered

workloads_equivalent

SAFE_output_equivalent

CAUTION_output_equivalent

UNSAFE_output_equivalent

governance_deterministic

warmup_excluded

raw_timings_preserved

mean_reported

max_reported

p95_reported

p99_reported

CPU_method_documented

memory_method_documented

thermal_conditions_documented

instrumentation_limitations_documented

MacBook_comparison_descriptive_only

H3_not_invented

no_acceptability_claim

no_real_time_claim

no_deployment_suitability_claim

no_historical_replay

no_human_study

no_new_threshold

no_new_rule

frozen_governance_unchanged
```

Use:

```text
PASS
FAIL
OPEN
```

---

# 25. Success Condition

Batch 7B succeeds when:

```text
physical representative Android device benchmarked

governance output equivalent to frozen implementation

SAFE/CAUTION/UNSAFE measured

raw timing evidence preserved

mean/max/p95/p99 reported

CPU and memory characterised or limitation explicitly recorded

hardware and runtime fully documented

methodology reproducible

no unsupported threshold introduced

no deployment suitability claim introduced

frozen scientific implementation unchanged
```

---

# 26. Closure

If successful:

```text
JOURNAL 1 EVALUATION BATCH 7B CLOSED —
E5 ANDROID TARGET-HARDWARE PERFORMANCE CHARACTERISATION COMPLETED
```

Then classify:

```text
E5_MEASUREMENT = CLOSED
H3_THRESHOLD = OPEN/UNSUPPORTED
```

Do NOT automatically classify:

```text
H3 = PASS
```

---

# 27. Deferred Status Until Device Exists

Until a physical representative Android device becomes available, preserve:

```text
BATCH_7B = DEFERRED_MANDATORY

E5_ANDROID_TARGET_BENCHMARK = PENDING

E5 = OPEN

H3 = OPEN/UNSUPPORTED

CURRENT_J1_WORK_MAY_CONTINUE = true

FINAL_J1_EVALUATION_CLOSURE = BLOCKED_BY_E5_ANDROID
```

Do not execute this task until the hardware prerequisite is satisfied.
