# E5 Benchmark Protocol

**Batch:** 7A — Journal 1 E5 Benchmark Harness  
**Task:** 2 — Benchmark Harness + Protocol Documents  
**Date:** 2026-09-13  
**Status:** PROTOCOL DOCUMENT — for use with `scripts/journal1_e5_benchmark.py`

---

## 1. Scientific purpose

This benchmark measures per-episode latency of the full governance pipeline implemented as the Journal 1 Layer 3 prototype. It provides descriptive latency characterisation to satisfy the **E5 criterion** defined in `evaluation-specification.md §11` (RQ-J2: prototype feasibility on low-resource hardware).

**E5 is a descriptive measurement only.** There is no pass/fail threshold. No latency value produced by this benchmark establishes or refutes deployment suitability on its own. The measurements are labelled `DEVELOPMENT_MACHINE_REFERENCE` and are not the final target-hardware E5 evidence.

The research claim being evaluated is that the graduated safety-state-gated governance architecture (formal pipeline: `E → S = f(E) → (G(S), A_AI(S)) → AI(E) → Human Decision`) is feasible to execute at interactive response times on low-resource hardware. This benchmark validates the measurement methodology and produces reference latency distributions from which execution characteristics can be described.

**H3 (latency hypothesis) status: OPEN/UNSUPPORTED** — no threshold value has been established. This benchmark does not assert that latency is "acceptable" or "unacceptable". Those labels are not produced in any output file.

---

## 2. E5 authority

`evaluation-specification.md §11` — RQ-J2 prototype feasibility evaluation. Confidence intervals are permitted but not required; they are recorded as `"CI": "NOT_REQUIRED"` in the output.

---

## 3. Measured execution path (timed region)

The timed region covers one complete governance pass from environmental inputs to `EpisodeResult`. Two top-level operations are included:

**Step 1 — Classification: f(E) / F\_{D,τ}**

```
s_w = g_w(w_kn)
s_r = g_r(r_rate, wmo_code)
s_o = g_o(wave_height, vessel)
s_t_arr = canonical_g_t([timestamp])   # returns array of length 1
s_t = int(s_t_arr[0])
s_m = 0  # g_m excluded (D={m}); pinned SAFE
S_int = max(s_w, s_r, s_m, s_o, s_t)
state_str = {0: "SAFE", 1: "CAUTION", 2: "UNSAFE"}[S_int]
```

**Step 2 — Governed episode: execute_episode(state, repository, context)**

Includes: G(S) lookup, gate-off check (UNSAFE), S/ComponentStateTrace consistency check, RS candidate selection, RS validation (A\_AI containment + V1–V4), reasoning engine call, fidelity trace emission, EpisodeResult construction.

**Outside the timed region:**

- `build_canonical_repository()` — called once before the benchmark loop. Repository construction (loading four CAUTION rules) is a one-time initialisation cost, not a per-episode cost.
- Warm-up iterations — discarded before the measured loop begins.
- Resource measurement probes — CPU and memory bookends are around the measured loop, not inside the per-iteration timed region (see §12 Instrumentation overhead treatment).

**No existing classifier logic is duplicated.** The harness imports `g_w`, `g_r`, `g_o` from `scripts/historical_replay.py` and `g_t` from `scripts/canonical_gt.py`. No scientific implementation is introduced by the benchmark script.

---

## 4. Hardware classification

**Classification: `DEVELOPMENT_MACHINE_REFERENCE`**

The benchmark machine (Apple MacBook Pro, Apple M3 Pro, 36 GB RAM) is a development machine, not the target deployment hardware. Target deployment is a low-resource coastal fishing vessel device (e.g. Raspberry Pi class). Measurements from this machine are used to validate the E5 methodology and characterise the pipeline execution path; they are not submitted as final E5 evidence for the deployment target.

Hardware profile is recorded in `data/journal1-e5-benchmark/hardware-profile.json` and included in the JSON output of each run.

---

## 5. Workloads

Three workloads, one per governance path. All inputs are constructed deterministic episodes — not samples from the historical replay dataset.

### W-SAFE

Exercises the SAFE governance path: G(S)=1, A\_AI full (Go, Delay, DepartureTime, Duration), no rules fire (R-SAFE-001 is deferred — STATE\_RESTATEMENT, Batch 4A).

| Parameter | Value | Classifier output |
|---|---|---|
| vessel\_category | small | — |
| w\_kn | 5.0 | g\_w = 0 (SAFE; threshold 21.6 kn) |
| r\_rate | 1.0 mm/hr | g\_r = 0 (SAFE; threshold 10.0 mm/hr) |
| wmo\_code | 0 | g\_r thunderstorm indicator κ = 0 |
| wave\_height | 0.5 m | g\_o = 0 (SAFE; small vessel threshold 1.0 m) |
| timestamp | 2023-06-15 10:00:00+08:00 | g\_t = SAFE (daytime, Kota Kinabalu) |
| m | EXCLUDED (D={m}) | s\_m = 0 (pinned SAFE) |

Expected governance outputs: S = SAFE, G = 1, A\_AI = {Go, Delay, DepartureTime, Duration}, RS = [], advisories = []

Component states: w=SAFE, r=SAFE, m=EXCLUDED, o=SAFE, t=SAFE

Interface consistency: REACHABLE\_CONSISTENT

### W-CAUTION

Exercises the CAUTION governance path: G(S)=1, A\_AI restricted (Go, Delay), R-CAUTION-002 fires (component\_o\_state == "CAUTION").

| Parameter | Value | Classifier output |
|---|---|---|
| vessel\_category | small | — |
| w\_kn | 5.0 | g\_w = 0 (SAFE) |
| r\_rate | 1.0 mm/hr | g\_r = 0 (SAFE) |
| wmo\_code | 0 | κ = 0 |
| wave\_height | 1.1 m | g\_o = 1 (CAUTION; small vessel: 1.0 ≤ 1.1 ≤ 1.25 m) |
| timestamp | 2023-06-15 10:00:00+08:00 | g\_t = SAFE (daytime) |
| m | EXCLUDED | s\_m = 0 |

Expected governance outputs: S = CAUTION, G = 1, A\_AI = {Go, Delay}, RS = [R-CAUTION-001, R-CAUTION-002, R-CAUTION-003, R-CAUTION-004], fired = [R-CAUTION-002], advisories = [Advisory(type="Delay", rule\_id="R-CAUTION-002")]

Component states: w=SAFE, r=SAFE, m=EXCLUDED, o=CAUTION, t=SAFE

Interface consistency: REACHABLE\_CONSISTENT

### W-UNSAFE

Exercises the UNSAFE gate-off path: G(S)=0, no reasoning, AI(E)=∅.

| Parameter | Value | Classifier output |
|---|---|---|
| vessel\_category | small | — |
| w\_kn | 5.0 | g\_w = 0 (SAFE) |
| r\_rate | 1.0 mm/hr | g\_r = 0 (SAFE) |
| wmo\_code | 0 | κ = 0 |
| wave\_height | 0.5 m | g\_o = 0 (SAFE) |
| timestamp | 2023-06-15 02:00:00+08:00 | g\_t = 2 (UNSAFE; nighttime 02:00) |
| m | EXCLUDED | s\_m = 0 |

Expected governance outputs: S = UNSAFE, G = 0, A\_AI = ∅, RS = [], advisories = []

Component states: w=SAFE, r=SAFE, m=EXCLUDED, o=SAFE, t=SAFE (component\_t\_state domain is {SAFE, EXCLUDED} only — UNSAFE state propagates via S\_int; gate-off fires before consistency check)

Interface consistency: GATED\_UNSAFE

---

## 6. Warm-up procedure and rationale

**Default warm-up: 50 iterations per workload** (configurable via `--warmup`).

Warm-up iterations are run before the measured loop and discarded. They do not appear in latency distributions. Warm-up addresses:

- **Import caching** — Python bytecode and module caches populated on first import.
- **Solar CSV load** — `canonical_gt.py` reads and caches `data/solar/solar-events-daily.csv` on first call; subsequent calls use the in-process `_CACHE` dict.
- **JIT and branch prediction** — modern CPUs and Python's bytecode evaluator exhibit run-to-run variance on first execution due to branch predictor state and code cache warming.
- **OS scheduling** — initial scheduling jitter on a cold execution path.

50 iterations is sufficient to stabilise caches without incurring excessive pre-benchmark cost.

---

## 7. Iteration procedure

**Default: 500 measured iterations per workload** (configurable via `--iterations`).

500 iterations provides a stable p99 estimate. With 500 samples, the p99 estimate reflects the 5th-highest latency observed, giving a distribution-tail characterisation that is meaningful for interactive response time analysis. Fewer samples would produce noisier p99 estimates. More samples are possible but not required for methodology validation.

---

## 8. Clock

**Clock: `time.perf_counter_ns()`**

Python's `time.perf_counter_ns()` is the appropriate clock for microbenchmarking on macOS and Linux:

- Monotonic — not affected by NTP adjustments or wall-clock changes.
- Nanosecond resolution — sufficient for sub-millisecond governance pipeline execution.
- Per-process — measures elapsed time including any system calls within the timed region, which is correct for full-pipeline latency.
- Standard library — no dependency on psutil or platform-specific APIs.

The clock is read immediately before the timed region (`t0 = time.perf_counter_ns()`) and immediately after (`t1 = time.perf_counter_ns()`). Elapsed time is `t1 - t0` in nanoseconds, converted to milliseconds for reporting.

---

## 9. Latency measurement method

One measurement per iteration: nanosecond wall time for one complete governance pass (classification + execute\_episode). All measurements in the warm-up phase are discarded. The measured loop records one nanosecond timestamp pair per iteration; no averaging or batching is applied within iterations.

---

## 10. CPU measurement method

**Module:** `resource.getrusage(resource.RUSAGE_SELF)`  
**Field:** `ru_utime` — user CPU time, in seconds  
**Scope:** Process-level user CPU time consumed during the measured pass only (bookend around measured loop, not inside it)

Limitations:
- Process-level, not thread-level or per-iteration.
- On Apple Silicon, process scheduling may distribute work across efficiency and performance cores; `ru_utime` captures total user-mode CPU time without core assignment information.
- If `resource.getrusage` is unavailable (non-POSIX platform), the harness records `"CPU_MEASUREMENT": "LIMITED"`.

---

## 11. Memory measurement method

**Module:** `resource.getrusage(resource.RUSAGE_SELF)`  
**Field:** `ru_maxrss` — peak resident set size  
**Unit on macOS:** BYTES (not kilobytes as on Linux)  
**Converted to:** MB for reporting (`ru_maxrss / (1024 * 1024)`)  
**Metric name in output:** `peak_rss_mb`  
**Scope:** Peak RSS for the process lifetime after the measured pass completes. This is process-level; it includes all allocations (imports, repository construction, warm-up) — not per-iteration allocation.

---

## 12. Instrumentation overhead treatment

Latency and resource measurements are separated to avoid contaminating the timed loop:

- **Latency** is measured per-iteration inside the timed loop using `time.perf_counter_ns()`. No resource probes are inside the timed loop.
- **CPU time** is measured as a bookend pair (`ru_utime` before and after the measured loop).
- **Memory** is measured once after the measured loop (`ru_maxrss`).

This separation is the §20 instrumentation overhead contract. The latency distribution reflects only the governance pipeline execution cost, not the cost of resource measurement.

---

## 13. Statistics reported

For each workload: n, mean\_ms, median\_ms, min\_ms, max\_ms, p95\_ms, p99\_ms, std\_ms.

**Percentile method:** `numpy.percentile` with linear interpolation (default NumPy method). This matches standard practice for continuous latency distributions.

**Confidence intervals:** NOT\_REQUIRED (evaluation-specification.md §11). Recorded as `"CI": "NOT_REQUIRED"` in JSON output.

---

## 14. Reproducibility procedure

To reproduce these measurements at the same commit:

1. Check out the repository at the same git commit as the run (recorded in run metadata if captured).
2. Run: `python3 scripts/journal1_e5_benchmark.py --warmup 50 --iterations 500 --state all`
3. Output is written to `data/journal1-e5-benchmark/latency-raw.csv`, `latency-summary.csv`, `latency-results.json`.

Note: latency values will vary across runs on the same machine due to OS scheduling, thermal state, and background processes. The distribution shape and order of magnitude are expected to be stable. For scientific reproducibility, run on the same hardware under controlled conditions (AC power, no background load).

---

## 15. Claim boundary

**This benchmark produces DEVELOPMENT\_MACHINE\_REFERENCE measurements only.**

- No H3 threshold has been established. No latency value is labelled "acceptable" or "unacceptable".
- No output file contains PASS, FAIL, acceptable, or unacceptable labels.
- Measurements from the MacBook Pro (Apple M3 Pro) are not transferable as-is to target deployment hardware.
- Target hardware E5 evidence requires running this benchmark (or an equivalent) on the target device class.

---

## 16. Target-hardware transfer procedure

To generate target-hardware E5 evidence:

1. Deploy the repository to the target device (e.g. Raspberry Pi 4 or equivalent).
2. Verify that all dependencies are available (`pandas`, `numpy`; no `psutil` required).
3. Run `scripts/journal1_e5_benchmark.py` with the same flags.
4. On Linux, `ru_maxrss` is in kilobytes (not bytes) — the script handles this only for macOS. Update the conversion factor if running on Linux.
5. Record `hardware_id` from the target device's `hardware-profile.json` (must be recaptured on the target).
6. The `run_type` field will still read `DEVELOPMENT_MACHINE_REFERENCE` unless the script is updated to reflect the target classification — update `MACHINE_CLASSIFICATION` constant in `scripts/journal1_e5_benchmark.py` before a target-hardware run.
7. Report latency distributions alongside hardware specification. The E5 claim is descriptive: state the measured values and the hardware they were measured on, without implying a pass/fail threshold.
