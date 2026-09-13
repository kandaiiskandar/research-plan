# Journal 1 Evaluation — Batch 7A
## E5 Benchmark Harness & MacBook Reference Run

---

### 1. Verdict

JOURNAL 1 EVALUATION BATCH 7A CLOSED — E5 BENCHMARK HARNESS VALIDATED AND MACBOOK REFERENCE BASELINE ESTABLISHED

E5 itself remains open. Batch 7A closes two sub-items only: E5_HARNESS (benchmark methodology validated) and MACBOOK_REFERENCE (development-machine baseline established). Target-hardware E5 evidence is not obtained in this batch and is not claimed here.

---

### 2. Branch and HEAD

**Branch:** `eval/journal1-e5-benchmark-harness`
**HEAD:** `57c46c352ce0922159b3cce29712d4956725484a`

---

### 3. Batch 6 closure commit

**Commit:** `b9a61f9` — "docs(journal1): resolve post-fidelity evaluation sequence"

Batch 6 is confirmed closed. The eval/journal1-e5-benchmark-harness branch was created from that commit.

---

### 4. Hardware

| Field | Value |
|---|---|
| Mac model | MacBook Pro |
| Chip / processor | Apple M3 Pro |
| Architecture | arm64 |
| Physical RAM | 36.0 GB |
| macOS version | macOS 26.2 |
| Python version | 3.9.6 |
| Power mode at capture | AC Power |

Full profile recorded in `data/journal1-e5-benchmark/hardware-profile.json`.

---

### 5. MacBook scientific classification

**DEVELOPMENT_MACHINE_REFERENCE** — not TARGET_HARDWARE_E5.

The MacBook Pro M3 Pro is a high-performance development machine. It is not representative of the target deployment hardware (commodity smartphones or low-cost single-board computers). Measurements produced in Batch 7A establish a reference baseline for methodology validation only. They do not constitute E5 target-hardware evidence and do not establish deployment suitability for the governance system.

---

### 6. E5 execution path benchmarked

The benchmark exercises the complete Layer 3 execution path as audited in Task 1 (execution-path-audit.md):

1. Episode input received (pre-classified safety state S; no g-functions invoked inside Layer 3)
2. G(S) evaluated — gate enabled (1) or disabled (0)
3. If UNSAFE (G=0): short-circuit, AI(E) = empty set, return
4. A_AI(S) determined — full set for SAFE, restricted set for CAUTION
5. RS(S) assembled from canonical rule repository — only rules with applicable_state matching S
6. Rule evaluation: each rule's predicates evaluated against episode context
7. Advisory emission: fired rules produce advisories within A_AI(S) only
8. Fidelity trace constructed and returned

The path covers three distinct code branches: SAFE (full rule set, no fire), CAUTION (restricted rule set, R-CAUTION-002 fires), and UNSAFE (gate-off, no reasoning).

---

### 7. Benchmark script

**Path:** `scripts/journal1_e5_benchmark.py`
**SHA-256:** `fec6c819b5e076f75757a152e272cd3df5ddaf9109fabea06e7641927f709787`

---

### 8. Workloads

| Workload | State | G(S) | A_AI(S) | Notes |
|---|---|---|---|---|
| W-SAFE | SAFE | 1 | {Go, Delay, DepartureTime, Duration} | No rules fire (R-SAFE-001 deferred) |
| W-CAUTION | CAUTION | 1 | {Go, Delay} | R-CAUTION-002 fires on component_o_state=CAUTION |
| W-UNSAFE | UNSAFE | 0 | empty | Gate-off; no reasoning engine invoked |

All workloads use constructed deterministic episodes. No connection to the 43,848-hour retrospective replay.

---

### 9. Benchmark parameters

**Warmup:** 50 iterations (excluded from all measurements)
**Measurement:** 500 iterations per workload
**States benchmarked:** all (SAFE, CAUTION, UNSAFE)

---

### 10. Timing clock

time.perf_counter_ns() — monotonic, nanosecond-resolution. One call before and one call after each governance engine invocation. Delta recorded per iteration. Converted to milliseconds for summary statistics.

---

### 11. SAFE latency summary

| Metric | Value |
|---|---|
| n | 500 |
| mean_ms | 0.2066 |
| median_ms | 0.2031 |
| min_ms | 0.1885 |
| max_ms | 0.4365 |
| p95_ms | 0.2342 |
| p99_ms | 0.2537 |
| std_ms | 0.0172 |

---

### 12. CAUTION latency summary

| Metric | Value |
|---|---|
| n | 500 |
| mean_ms | 0.2117 |
| median_ms | 0.2126 |
| min_ms | 0.1965 |
| max_ms | 0.2640 |
| p95_ms | 0.2243 |
| p99_ms | 0.2592 |
| std_ms | 0.0114 |

---

### 13. UNSAFE latency summary

| Metric | Value |
|---|---|
| n | 500 |
| mean_ms | 0.1944 |
| median_ms | 0.1961 |
| min_ms | 0.1803 |
| max_ms | 0.2553 |
| p95_ms | 0.2043 |
| p99_ms | 0.2498 |
| std_ms | 0.0120 |

---

### 14. Peak memory result

**Metric:** Peak RSS (resource.getrusage(RUSAGE_SELF).ru_maxrss)
**Platform note:** On macOS, ru_maxrss is in bytes (not kilobytes as on Linux).

| Workload | peak_rss_mb |
|---|---|
| W-SAFE | 66.34 |
| W-CAUTION | 66.66 |
| W-UNSAFE | 66.88 |

**Scope limitation:** ru_maxrss is the peak RSS for the entire process lifetime, not a per-iteration measurement.

---

### 15. CPU result

**Metric:** User CPU time (resource.getrusage(RUSAGE_SELF).ru_utime)
**Scope:** Total user CPU time consumed during the 500-iteration measured loop only (bookend measurement).

| Workload | cpu_user_time_s |
|---|---|
| W-SAFE | 0.1035 |
| W-CAUTION | 0.1060 |
| W-UNSAFE | 0.0975 |

---

### 16. Instrumentation limitations

1. ru_maxrss is peak RSS for the process lifetime, not per-iteration.
2. CPU time (ru_utime) is total user CPU during the measured pass; not per-iteration.
3. No per-iteration memory probe — inserting resource probes inside the timed loop would alter the latency measurement.
4. On macOS, ru_maxrss is bytes; on Linux it is kilobytes. The target hardware run must apply the correct unit conversion.
5. Resource and CPU measurements are bookend-only, outside the timed loop.

---

### 17. Existing governance test result

**tests/test_governance_engine.py: 139 passed in 0.07s — 0 failures**

Run before the benchmark (Step 2). Confirmed governance implementation is correct before measurement begins.

---

### 18. Benchmark harness test result

**tests/ full suite: 149 passed in 0.27s — 0 failures**

Breakdown: 139 governance engine tests + 10 benchmark harness tests (tests/test_journal1_e5_benchmark.py). Run after the benchmark (Step 4).

---

### 19. Governance determinism

**PASS — all three workloads deterministic.**

The benchmark script ran determinism checks for W-SAFE, W-CAUTION, and W-UNSAFE before the measurement loop. Benchmark output: "All determinism checks passed."

---

### 20. H3 status

**H3 is OPEN/UNSUPPORTED.**

No latency threshold for the governance engine's E5 evaluation exists in any authority document. No threshold has been invented in Batch 7A. No acceptability claim is made about the measured latency values.

---

### 21. target_hardware_evidence

**false**

MacBook Pro measurements are development-machine reference data only.

---

### 22. TARGET_HARDWARE_BENCHMARK_READY

**true**

The benchmark methodology is portable to target hardware. Required adaptations documented in target-hardware-readiness.md. Batch 7B is responsible for selecting a specific target device and running the benchmark on it.

---

### 23. Integrity result

**UNCHANGED — all 17 monitored files.**

SHA-256 hashes computed before and after the benchmark run. All hashes are identical. Full record: data/journal1-e5-benchmark/integrity.json.

---

### 24. Verification summary

**37 items total — 37 PASS, 0 FAIL, 0 OPEN**

Full record: data/journal1-e5-benchmark/verification.json.

---

### 25. Next task

**Batch 7B — E5 Target-Hardware Performance Benchmark**

Since TARGET_HARDWARE_BENCHMARK_READY = true, Batch 7B may proceed with device selection and target-hardware benchmarking. E5 remains open until target-hardware measurements are obtained.

---

## Artefacts produced (Batch 7A — all tasks)

**Task 1 (pre-existing):**
- data/journal1-e5-benchmark/execution-path-audit.md
- data/journal1-e5-benchmark/hardware-profile.json

**Task 2 (pre-existing):**
- scripts/journal1_e5_benchmark.py
- data/journal1-e5-benchmark/benchmark-protocol.md
- data/journal1-e5-benchmark/workload-manifest.json

**Task 3 (pre-existing):**
- tests/test_journal1_e5_benchmark.py

**Task 4 (this run):**
- data/journal1-e5-benchmark/latency-raw.csv
- data/journal1-e5-benchmark/latency-summary.csv
- data/journal1-e5-benchmark/latency-results.json
- data/journal1-e5-benchmark/resource-summary.json
- data/journal1-e5-benchmark/reference-run.json
- data/journal1-e5-benchmark/target-hardware-readiness.md
- data/journal1-e5-benchmark/integrity.json
- data/journal1-e5-benchmark/verification.json
- data/journal1-e5-benchmark/report.md (this document)
