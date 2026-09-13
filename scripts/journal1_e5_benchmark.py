#!/usr/bin/env python3
"""Journal 1 E5 Benchmark — DEVELOPMENT MACHINE REFERENCE.

Measures per-episode latency of the full governance pipeline:
    classification (g_w, g_r, g_o, g_t → S) + governed episode (execute_episode).

Scientific purpose: E5 criterion (evaluation-specification.md §11) — descriptive
latency characterisation of the prototype governance pipeline. No pass/fail
threshold exists. Measurements on this machine carry the classification
DEVELOPMENT_MACHINE_REFERENCE and are not final target-hardware E5 evidence.

Hardware classification: DEVELOPMENT_MACHINE_REFERENCE
Scientific status: REFERENCE_ONLY
Target hardware evidence: FALSE

These measurements are development-machine reference measurements used to validate
the E5 benchmark methodology. They are not the final target-hardware E5 evidence
and do not establish deployment suitability.

Timing: time.perf_counter_ns() — monotonic, nanosecond resolution, suitable for
microbenchmarking on macOS/Linux. Not affected by wall-clock adjustments.

CPU/memory: resource.getrusage(RUSAGE_SELF) — process-level user CPU time and
peak RSS. Measured as bookends around the measured loop only; NOT probed inside
the timed loop (instrumentation overhead separation — §20).

On macOS, ru_maxrss is in BYTES (not kilobytes as on Linux).

Percentile calculation: numpy.percentile (linear interpolation).
Confidence intervals: NOT_REQUIRED (evaluation-specification.md §11).

Usage:
    python3 scripts/journal1_e5_benchmark.py \\
        [--warmup 50] [--iterations 500] \\
        [--output-dir data/journal1-e5-benchmark] \\
        [--state SAFE|CAUTION|UNSAFE|all] \\
        [--workload WORKLOAD_ID]
"""

import argparse
import csv
import datetime
import json
import pathlib
import platform
import resource
import statistics
import sys
import time
from typing import Any

import numpy as np
import pandas as pd

# ── Path setup ────────────────────────────────────────────────────────────────

_REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_REPO_ROOT))
sys.path.insert(0, str(_REPO_ROOT / "scripts"))

# ── Governance imports ────────────────────────────────────────────────────────
# canonical g_t — from scripts/canonical_gt.py; NOT from historical_replay.
# historical_replay.g_t raises NotImplementedError (SDR-001).
from canonical_gt import g_t as _canonical_g_t
from historical_replay import g_w, g_r, g_o, STATE
from governance.canonical_rules import build_canonical_repository
from governance.reasoning_episode import execute_episode, DecisionContext
from governance.rule_set_provider import GOVERNANCE_MAP

# ── Constants ─────────────────────────────────────────────────────────────────

MACHINE_CLASSIFICATION = "DEVELOPMENT_MACHINE_REFERENCE"
SCIENTIFIC_STATUS = "REFERENCE_ONLY"
TARGET_HARDWARE_EVIDENCE = False
DISCLAIMER = (
    "These measurements are development-machine reference measurements used to validate "
    "the E5 benchmark methodology. They are not the final target-hardware E5 evidence "
    "and do not establish deployment suitability."
)

# ComponentStateTrace mapping: component classifiers return int 0/1/2.
# DecisionContext schema only accepts {"SAFE","CAUTION","EXCLUDED"} for component
# state fields. For UNSAFE workloads the consistency check is skipped in
# execute_episode (G=0 gate-off fires first), so any valid domain value works.
# For SAFE/CAUTION workloads no component returns 2 (UNSAFE) in the timed path.
_SEVERITY_TO_COMPONENT_STATE: dict[int, str] = {0: "SAFE", 1: "CAUTION", 2: "SAFE"}


def _int_to_component_state(severity_int: int, excluded: bool = False) -> str:
    """Map int severity (0/1/2) to ComponentStateTrace string.

    excluded=True: component is in the D set → "EXCLUDED"
    severity 2 (UNSAFE): no ComponentStateTrace representation exists;
        use "SAFE" (consistency check is bypassed by gate-off for UNSAFE state).
    """
    if excluded:
        return "EXCLUDED"
    return _SEVERITY_TO_COMPONENT_STATE[severity_int]


# ── Workload definitions ──────────────────────────────────────────────────────

# W-SAFE: all components SAFE, daytime, small vessel
_W_SAFE_INPUTS = {
    "workload_id": "W-SAFE",
    "episode_id": "bench-SAFE-001",
    "vessel_category": "small",
    "w_kn": 5.0,
    "r_rate": 1.0,
    "wmo_code": 0,
    "wave_height": 0.5,
    "timestamp": pd.Timestamp("2023-06-15 10:00:00+08:00"),
    # expected
    "expected_S": "SAFE",
    "expected_G": 1,
    "expected_A_AI": frozenset({"Go", "Delay", "DepartureTime", "Duration"}),
    "expected_RS_rule_ids": [],
    "expected_advisories": [],
    "interface_consistency": "REACHABLE_CONSISTENT",
}

# W-CAUTION: wave height 1.1 m puts g_o in CAUTION band for small vessel (1.0–1.25 m)
_W_CAUTION_INPUTS = {
    "workload_id": "W-CAUTION",
    "episode_id": "bench-CAUTION-001",
    "vessel_category": "small",
    "w_kn": 5.0,
    "r_rate": 1.0,
    "wmo_code": 0,
    "wave_height": 1.1,
    "timestamp": pd.Timestamp("2023-06-15 10:00:00+08:00"),
    # expected
    "expected_S": "CAUTION",
    "expected_G": 1,
    "expected_A_AI": frozenset({"Go", "Delay"}),
    "expected_RS_rule_ids": ["R-CAUTION-001", "R-CAUTION-002", "R-CAUTION-003", "R-CAUTION-004"],
    "expected_fired_rule_ids": ["R-CAUTION-002"],
    "expected_advisories": [("Delay", "R-CAUTION-002")],
    "interface_consistency": "REACHABLE_CONSISTENT",
}

# W-UNSAFE: 02:00 nighttime → g_t=UNSAFE → S=UNSAFE → G=0 gate-off
_W_UNSAFE_INPUTS = {
    "workload_id": "W-UNSAFE",
    "episode_id": "bench-UNSAFE-001",
    "vessel_category": "small",
    "w_kn": 5.0,
    "r_rate": 1.0,
    "wmo_code": 0,
    "wave_height": 0.5,
    "timestamp": pd.Timestamp("2023-06-15 02:00:00+08:00"),
    # expected
    "expected_S": "UNSAFE",
    "expected_G": 0,
    "expected_A_AI": frozenset(),
    "expected_RS_rule_ids": [],
    "expected_advisories": [],
    "interface_consistency": "GATED_UNSAFE",
}

_ALL_WORKLOADS = {
    "W-SAFE": _W_SAFE_INPUTS,
    "W-CAUTION": _W_CAUTION_INPUTS,
    "W-UNSAFE": _W_UNSAFE_INPUTS,
}

_STATE_TO_WORKLOAD = {
    "SAFE": "W-SAFE",
    "CAUTION": "W-CAUTION",
    "UNSAFE": "W-UNSAFE",
}


# ── Classification helper ─────────────────────────────────────────────────────

def _classify(inputs: dict[str, Any]) -> tuple[str, dict[str, int]]:
    """Run component classifiers and return (state_str, component_severities).

    This is the timed Step 1. Returns state as string and a dict of int
    severities for each component (used to build ComponentStateTrace).

    g_m is excluded (D = {m}): pinned at 0 (SAFE).
    """
    s_w = g_w(inputs["w_kn"])
    s_r = g_r(inputs["r_rate"], inputs["wmo_code"])
    s_o = g_o(inputs["wave_height"], inputs["vessel_category"])
    s_t_arr = _canonical_g_t([inputs["timestamp"]])
    s_t = int(s_t_arr[0])
    s_m = 0  # g_m excluded (D={m}); pinned SAFE

    S_int = max(s_w, s_r, s_m, s_o, s_t)
    state_str = STATE[S_int]

    return state_str, {"s_w": s_w, "s_r": s_r, "s_o": s_o, "s_t": s_t, "s_m": s_m}


def _make_context(inputs: dict[str, Any], component_severities: dict[str, int]) -> DecisionContext:
    """Build DecisionContext from workload inputs and computed component severities."""
    s_w = component_severities["s_w"]
    s_r = component_severities["s_r"]
    s_o = component_severities["s_o"]
    # s_t domain is {"SAFE","EXCLUDED"} only — g_t emits no CAUTION
    # For UNSAFE workload, gate-off fires before consistency check; use "SAFE"
    component_t_str = "SAFE"  # g_t never returns CAUTION; UNSAFE propagates via S_int not trace

    return DecisionContext(
        episode_id=inputs["episode_id"],
        vessel_category=inputs["vessel_category"],
        resolved_w=inputs["w_kn"],
        resolved_r_rate=inputs["r_rate"],
        resolved_r_kappa=int(inputs["wmo_code"] in (95, 96, 99)),
        resolved_m=None,           # m is in D (excluded)
        resolved_o_wave_height=inputs["wave_height"],
        resolved_o_swell_period=None,   # swell period not read by g_o
        resolved_t=float(inputs["timestamp"].hour),
        component_w_state=_int_to_component_state(s_w),
        component_r_state=_int_to_component_state(s_r),
        component_m_state="EXCLUDED",  # m in D
        component_o_state=_int_to_component_state(s_o),
        component_t_state=component_t_str,
    )


# ── Timed pass ────────────────────────────────────────────────────────────────

def _run_one_pass(inputs: dict[str, Any], repository: object) -> int:
    """Execute one complete governance pass and return elapsed nanoseconds.

    Timed region covers:
      1. Component classification (g_w, g_r, g_o, g_t → S)
      2. execute_episode(state, repository, context)

    build_canonical_repository() is OUTSIDE the timed region (called once
    before the benchmark loop per the brief specification).

    Returns elapsed time in nanoseconds (time.perf_counter_ns() difference).
    """
    t0 = time.perf_counter_ns()

    # Step 1: Classification
    s_w = g_w(inputs["w_kn"])
    s_r = g_r(inputs["r_rate"], inputs["wmo_code"])
    s_o = g_o(inputs["wave_height"], inputs["vessel_category"])
    s_t_arr = _canonical_g_t([inputs["timestamp"]])
    s_t = int(s_t_arr[0])
    s_m = 0  # g_m excluded (D={m}); pinned SAFE

    S_int = max(s_w, s_r, s_m, s_o, s_t)
    state_str = STATE[S_int]

    # Component state strings for DecisionContext
    component_t_str = "SAFE"  # g_t emits no CAUTION; UNSAFE propagates via S_int

    # Step 2: Governed episode
    context = DecisionContext(
        episode_id=inputs["episode_id"],
        vessel_category=inputs["vessel_category"],
        resolved_w=inputs["w_kn"],
        resolved_r_rate=inputs["r_rate"],
        resolved_r_kappa=int(inputs["wmo_code"] in (95, 96, 99)),
        resolved_m=None,
        resolved_o_wave_height=inputs["wave_height"],
        resolved_o_swell_period=None,
        resolved_t=float(inputs["timestamp"].hour),
        component_w_state=_SEVERITY_TO_COMPONENT_STATE[s_w],
        component_r_state=_SEVERITY_TO_COMPONENT_STATE[s_r],
        component_m_state="EXCLUDED",
        component_o_state=_SEVERITY_TO_COMPONENT_STATE[s_o],
        component_t_state=component_t_str,
    )
    _result = execute_episode(state_str, repository, context)

    t1 = time.perf_counter_ns()
    return t1 - t0


# ── Determinism check ─────────────────────────────────────────────────────────

def _check_determinism(inputs: dict[str, Any], repository: object) -> None:
    """Run execute_episode twice and verify identical governance outputs.

    Checks: state, G, A_AI, advisory types, error presence.
    If outputs differ: prints diagnostic and raises SystemExit.
    """
    state1, comp1 = _classify(inputs)
    ctx1 = _make_context(inputs, comp1)
    r1 = execute_episode(state1, repository, ctx1)

    state2, comp2 = _classify(inputs)
    ctx2 = _make_context(inputs, comp2)
    r2 = execute_episode(state2, repository, ctx2)

    gov1 = GOVERNANCE_MAP.get(state1)
    gov2 = GOVERNANCE_MAP.get(state2)

    ok = (
        state1 == state2
        and (gov1.G if gov1 else None) == (gov2.G if gov2 else None)
        and (gov1.A_AI if gov1 else frozenset()) == (gov2.A_AI if gov2 else frozenset())
        and sorted(a.type for a in r1.advisories) == sorted(a.type for a in r2.advisories)
        and (r1.error is None) == (r2.error is None)
    )

    if not ok:
        print(
            f"E5_HARNESS_INVALID — NONDETERMINISTIC GOVERNANCE OUTPUT\n"
            f"  Workload: {inputs['workload_id']}\n"
            f"  Run 1: state={state1!r}, advisories={[a.type for a in r1.advisories]!r}, "
            f"error={r1.error!r}\n"
            f"  Run 2: state={state2!r}, advisories={[a.type for a in r2.advisories]!r}, "
            f"error={r2.error!r}",
            file=sys.stderr,
        )
        sys.exit(1)


# ── Statistics ────────────────────────────────────────────────────────────────

def _compute_stats(latencies_ns: list[int]) -> dict[str, float]:
    """Compute descriptive statistics over nanosecond latency samples.

    All values returned in milliseconds.
    Percentiles: numpy.percentile with linear interpolation.
    """
    arr = np.array(latencies_ns, dtype=float)
    arr_ms = arr / 1_000_000.0
    return {
        "n": len(arr_ms),
        "mean_ms": float(np.mean(arr_ms)),
        "median_ms": float(np.median(arr_ms)),
        "min_ms": float(np.min(arr_ms)),
        "max_ms": float(np.max(arr_ms)),
        "p95_ms": float(np.percentile(arr_ms, 95)),
        "p99_ms": float(np.percentile(arr_ms, 99)),
        "std_ms": float(np.std(arr_ms, ddof=1)),
    }


# ── Hardware profile helper ───────────────────────────────────────────────────

def _load_hardware_profile(output_dir: pathlib.Path) -> dict[str, Any]:
    """Read hardware-profile.json from the benchmark output directory."""
    hw_path = output_dir / "hardware-profile.json"
    if hw_path.exists():
        with open(hw_path) as f:
            return json.load(f)
    return {"error": "hardware-profile.json not found", "path": str(hw_path)}


def _hardware_id(hw_profile: dict[str, Any]) -> str:
    """Derive normalised hardware_id from hardware profile (spaces → underscores)."""
    mac_model = hw_profile.get("mac_model", "Unknown")
    chip_processor = hw_profile.get("chip_processor", "Unknown")
    raw = f"{mac_model}_{chip_processor}"
    return raw.replace(" ", "_")


# ── Main benchmark ────────────────────────────────────────────────────────────

def _run_benchmark(
    workload_inputs: dict[str, Any],
    repository: object,
    warmup: int,
    iterations: int,
    run_id: str,
) -> tuple[list[dict], dict[str, float], dict[str, Any]]:
    """Run one workload: warmup + measured loop + resource measurement.

    Returns:
        raw_rows: list of dicts (one per measured iteration)
        stats: descriptive statistics dict
        resource_info: CPU and memory measurements
    """
    wid = workload_inputs["workload_id"]
    state = workload_inputs["expected_S"]  # used only for labelling; not governance input

    # Warm-up: runs discarded; addresses import caching, solar CSV load, JIT, OS scheduling
    for _ in range(warmup):
        _run_one_pass(workload_inputs, repository)

    # Resource bookend — before measured loop
    ru_before = resource.getrusage(resource.RUSAGE_SELF)
    cpu_before = ru_before.ru_utime  # user CPU time, seconds

    # Measured loop
    latencies_ns = []
    for _ in range(iterations):
        latencies_ns.append(_run_one_pass(workload_inputs, repository))

    # Resource bookend — after measured loop
    ru_after = resource.getrusage(resource.RUSAGE_SELF)
    cpu_after = ru_after.ru_utime
    peak_rss_bytes = ru_after.ru_maxrss  # bytes on macOS (not kilobytes)

    cpu_time_s = cpu_after - cpu_before
    peak_rss_mb = peak_rss_bytes / (1024 * 1024)

    resource_info = {
        "cpu_user_time_s": cpu_time_s,
        "cpu_measurement": "resource.getrusage(RUSAGE_SELF).ru_utime — process-level user CPU time",
        "cpu_scope": "total user CPU time consumed during the measured pass only",
        "peak_rss_mb": peak_rss_mb,
        "peak_rss_measurement": "resource.getrusage(RUSAGE_SELF).ru_maxrss after measured loop",
        "peak_rss_unit_note": "ru_maxrss is BYTES on macOS (not kilobytes as on Linux)",
        "peak_rss_scope": "peak RSS for process lifetime, not per-iteration",
        "instrumentation_note": (
            "Latency measured per-iteration inside the timed loop (time.perf_counter_ns); "
            "resource probes (CPU, memory) are bookend measurements around the entire "
            "measured loop — no resource probe is inside the timed loop."
        ),
    }

    # Build raw rows
    raw_rows = [
        {
            "run_id": run_id,
            "state": state,
            "workload_id": wid,
            "iteration": i + 1,
            "latency_ns": ns,
            "latency_ms": ns / 1_000_000.0,
        }
        for i, ns in enumerate(latencies_ns)
    ]

    stats = _compute_stats(latencies_ns)

    return raw_rows, stats, resource_info


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Journal 1 E5 Benchmark — DEVELOPMENT MACHINE REFERENCE",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "E5 criterion: descriptive latency characterisation of the governance pipeline.\n"
            "No pass/fail threshold. Classification: DEVELOPMENT_MACHINE_REFERENCE.\n"
            f"\n{DISCLAIMER}"
        ),
    )
    parser.add_argument(
        "--warmup", type=int, default=50,
        help="Number of warm-up iterations per workload (not included in measurements). Default: 50.",
    )
    parser.add_argument(
        "--iterations", type=int, default=500,
        help="Number of measured iterations per workload. Default: 500.",
    )
    parser.add_argument(
        "--output-dir", type=pathlib.Path,
        default=pathlib.Path("data/journal1-e5-benchmark"),
        help="Output directory for latency-raw.csv and latency-summary.csv. Default: data/journal1-e5-benchmark.",
    )
    parser.add_argument(
        "--state", choices=["SAFE", "CAUTION", "UNSAFE", "all"], default="all",
        help="Which governance state workload to run. Default: all.",
    )
    parser.add_argument(
        "--workload", type=str, default=None,
        help="Run a specific workload by ID (W-SAFE, W-CAUTION, W-UNSAFE). Overrides --state.",
    )
    args = parser.parse_args()

    # Resolve output directory
    output_dir = args.output_dir
    if not output_dir.is_absolute():
        output_dir = _REPO_ROOT / output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    # Determine workloads to run
    if args.workload is not None:
        if args.workload not in _ALL_WORKLOADS:
            print(
                f"Unknown workload ID {args.workload!r}. Valid: {sorted(_ALL_WORKLOADS)!r}",
                file=sys.stderr,
            )
            sys.exit(1)
        workloads_to_run = {args.workload: _ALL_WORKLOADS[args.workload]}
    elif args.state == "all":
        workloads_to_run = _ALL_WORKLOADS
    else:
        wid = _STATE_TO_WORKLOAD[args.state]
        workloads_to_run = {wid: _ALL_WORKLOADS[wid]}

    # Run ID: UTC ISO-8601 timestamp, same for all rows in this execution
    run_id = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    # Load hardware profile
    hw_profile = _load_hardware_profile(output_dir)
    hw_id = _hardware_id(hw_profile)

    # Build repository ONCE outside the timed region
    print("Building canonical rule repository (outside timed region)...")
    repository = build_canonical_repository()

    # Determinism check — before any timing
    print("Running determinism checks...")
    for wid, inputs in workloads_to_run.items():
        print(f"  Checking {wid}...")
        _check_determinism(inputs, repository)
    print("  All determinism checks passed.")

    # Run benchmarks
    all_raw_rows: list[dict] = []
    all_summary_rows: list[dict] = []
    all_resource: dict[str, Any] = {}

    for wid, inputs in workloads_to_run.items():
        print(f"\nBenchmarking {wid} (warmup={args.warmup}, iterations={args.iterations})...")
        raw_rows, stats, resource_info = _run_benchmark(
            inputs, repository, args.warmup, args.iterations, run_id
        )
        all_raw_rows.extend(raw_rows)
        all_resource[wid] = resource_info

        summary_row = {
            "run_type": MACHINE_CLASSIFICATION,
            "hardware_id": hw_id,
            "state": inputs["expected_S"],
            "workload_id": wid,
            "n": stats["n"],
            "mean_ms": round(stats["mean_ms"], 6),
            "median_ms": round(stats["median_ms"], 6),
            "min_ms": round(stats["min_ms"], 6),
            "max_ms": round(stats["max_ms"], 6),
            "p95_ms": round(stats["p95_ms"], 6),
            "p99_ms": round(stats["p99_ms"], 6),
            "std_ms": round(stats["std_ms"], 6),
        }
        all_summary_rows.append(summary_row)

    # Write latency-raw.csv
    raw_csv_path = output_dir / "latency-raw.csv"
    raw_fieldnames = ["run_id", "state", "workload_id", "iteration", "latency_ns", "latency_ms"]
    with open(raw_csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=raw_fieldnames)
        writer.writeheader()
        writer.writerows(all_raw_rows)
    print(f"\nRaw latency data written to: {raw_csv_path}")

    # Write latency-summary.csv
    summary_csv_path = output_dir / "latency-summary.csv"
    summary_fieldnames = [
        "run_type", "hardware_id", "state", "workload_id",
        "n", "mean_ms", "median_ms", "min_ms", "max_ms", "p95_ms", "p99_ms", "std_ms",
    ]
    with open(summary_csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=summary_fieldnames)
        writer.writeheader()
        writer.writerows(all_summary_rows)
    print(f"Summary written to: {summary_csv_path}")

    # Build and write full JSON output
    full_output = {
        "run_id": run_id,
        "run_type": MACHINE_CLASSIFICATION,
        "scientific_status": SCIENTIFIC_STATUS,
        "target_hardware_evidence": TARGET_HARDWARE_EVIDENCE,
        "disclaimer": DISCLAIMER,
        "hardware_id": hw_id,
        "hardware_profile": hw_profile,
        "benchmark_parameters": {
            "warmup_iterations": args.warmup,
            "measurement_iterations": args.iterations,
            "percentile_method": "numpy.percentile (linear interpolation)",
            "CI": "NOT_REQUIRED",
        },
        "workloads": {},
    }
    for wid, inputs in workloads_to_run.items():
        row = next(r for r in all_summary_rows if r["workload_id"] == wid)
        full_output["workloads"][wid] = {
            "state": inputs["expected_S"],
            "summary": row,
            "resource": all_resource[wid],
        }

    json_path = output_dir / "latency-results.json"
    with open(json_path, "w") as f:
        json.dump(full_output, f, indent=2)
    print(f"Full JSON results written to: {json_path}")

    # Print summary table to stdout
    print("\n" + "=" * 72)
    print("E5 BENCHMARK RESULTS — DEVELOPMENT MACHINE REFERENCE")
    print("=" * 72)
    print(f"{'Workload':<14} {'State':<8} {'n':>6}  {'mean_ms':>10}  {'max_ms':>10}  {'p95_ms':>10}  {'p99_ms':>10}")
    print("-" * 72)
    for row in all_summary_rows:
        print(
            f"{row['workload_id']:<14} {row['state']:<8} {row['n']:>6}  "
            f"{row['mean_ms']:>10.4f}  {row['max_ms']:>10.4f}  "
            f"{row['p95_ms']:>10.4f}  {row['p99_ms']:>10.4f}"
        )
    print("=" * 72)
    print(f"\nHardware: {hw_id}")
    print(f"Run ID: {run_id}")
    print(f"\nMacBook scientific classification: {MACHINE_CLASSIFICATION}")
    print(
        "These measurements are development-machine reference measurements used to validate\n"
        "the E5 benchmark methodology. They are not the final target-hardware E5 evidence\n"
        "and do not establish deployment suitability."
    )


if __name__ == "__main__":
    main()
