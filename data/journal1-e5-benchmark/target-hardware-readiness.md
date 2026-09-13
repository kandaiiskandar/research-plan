# Target Hardware Readiness Assessment — Batch 7A

**Date:** 2026-09-13
**Batch:** 7A — E5 Benchmark Harness

---

## TARGET_HARDWARE_BENCHMARK_READY: true

The E5 benchmark methodology is portable to target hardware. No structural blocker exists. Batch 7B is responsible for selecting a specific target device and executing the benchmark on it.

---

## Authority basis

The target hardware class is defined by the evaluation specification and architecture documentation as: **commodity smartphones or low-cost single-board computers (SBCs)**. This class represents the deployment context for the governance system in low-resource coastal fisheries environments.

---

## Device-selection criteria (from existing authority)

A target device for Batch 7B must satisfy all of the following:

1. **Representative of the authorised hardware class** — commodity smartphone or low-cost SBC; not a development machine, server, or workstation.
2. **Able to execute the required software stack** — Python 3.x (≥ 3.9), numpy, pandas, and the governance package (`governance/`) must be installable and functional.
3. **Resource-constrained relative to the development machine** — the MacBook Pro M3 Pro (36 GB RAM, Apple Silicon) sets the reference ceiling; target hardware must be meaningfully below it.
4. **Reproducibly identifiable model and specification** — exact device model, CPU/SoC, RAM, OS version, and Python version must be recorded in a hardware-profile.json at the time of benchmarking.
5. **Available for repeatable benchmarking** — the device must be physically accessible for controlled, repeated runs with consistent configuration.

---

## What changes when moving to target hardware

### Platform detection

The benchmark script uses `platform.system()` to detect macOS vs. Linux. The `--mac-ref` flag in the script sets `run_type = "DEVELOPMENT_MACHINE_REFERENCE"`; on Linux/Android the default run type should be `TARGET_HARDWARE_E5`. The script already contains this branching logic.

### resource.getrusage availability

`resource.getrusage(RUSAGE_SELF)` is available on Linux. On Android (if using Termux or a full Python environment), availability depends on the environment. The benchmark script should verify availability at startup and log a warning if it falls back to a limited resource probe.

### ru_maxrss units

On macOS, `ru_maxrss` is in **bytes**. On Linux, `ru_maxrss` is in **kilobytes**. The benchmark script must apply the correct unit conversion for the target platform. This is already documented in the `resource_summary` output fields (`peak_rss_unit_note`).

### Solar artefact

`data/solar/solar-events-daily.csv` must be present on the target device. The governance engine's `g_t` function reads this frozen artefact. Batch 7B must verify the artefact is transferred and the path resolves correctly.

### pandas and numpy availability

Both packages are used by the benchmark script for summary statistics. On constrained embedded environments, these may require installation via pip or a pre-built wheel. Batch 7B must verify availability before running.

---

## What Batch 7A does NOT do

- **Does not select a specific target device.** That decision belongs to Batch 7B.
- **Does not establish H3 latency threshold.** H3 is OPEN/UNSUPPORTED; no threshold is invented here.
- **Does not make any acceptability claim** for the MacBook reference measurements relative to target deployment.
- **Does not close E5.** E5 remains open until target-hardware measurements are obtained and compared against a threshold (if one is established).

---

## Summary

The benchmark methodology is validated on the development machine. The script, workload definitions, timing clock (`time.perf_counter_ns`), resource probes, and output format are all portable. Batch 7B may proceed with device selection.

---

## Batch 7B status — 2026-09-13

```text
BATCH_7B                     = DEFERRED_MANDATORY
CURRENT_BLOCKER              = REPRESENTATIVE_ANDROID_DEVICE_NOT_AVAILABLE
E5_ANDROID_TARGET_BENCHMARK  = PENDING
E5                           = OPEN
H3                           = OPEN/UNSUPPORTED
CURRENT_J1_WORK_MAY_CONTINUE = true
FINAL_J1_EVALUATION_CLOSURE  = BLOCKED_BY_E5_ANDROID
```

Full task specification: `docs/tasks/DEFERRED MANDATORY TASK Journal 1 Evaluation — Batch 7B.md`

Do not execute Batch 7B until `PHYSICAL_ANDROID_DEVICE_AVAILABLE = true`.
