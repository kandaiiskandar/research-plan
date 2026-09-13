"""Engineering tests for the Journal 1 E5 benchmark harness.

These tests verify that the harness *behaves correctly* — correct row counts,
correct field names, reproducible statistics, hardware metadata emission, label
preservation, and governance determinism.  They make NO scientific claims and
assert NO specific latency values (performance is environment-dependent).

Test IDs BH01–BH08 map to the eight required test cases in Batch 7A §24.
"""

import pathlib
import sys

import numpy as np
import pytest

# ── Path setup (mirrors the harness) ─────────────────────────────────────────
_REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_REPO_ROOT))
sys.path.insert(0, str(_REPO_ROOT / "scripts"))

from scripts.journal1_e5_benchmark import (
    _run_benchmark,
    _compute_stats,
    _check_determinism,
    _load_hardware_profile,
    _hardware_id,
    _W_SAFE_INPUTS,
    _W_CAUTION_INPUTS,
    _W_UNSAFE_INPUTS,
    _ALL_WORKLOADS,
)
from governance.canonical_rules import build_canonical_repository

# ── Module-level fixture — repository is built ONCE for the whole module ──────
# Building the canonical rule repository is expensive; share it across all tests.

@pytest.fixture(scope="module")
def repository():
    """Canonical rule repository shared across all harness tests."""
    return build_canonical_repository()


# ── BH01: Warm-up excluded from measured samples ─────────────────────────────

def test_bh01_warmup_excluded(repository):
    """Warm-up iterations must NOT appear in the returned raw rows.

    _run_benchmark(warmup=5, iterations=10) must return exactly 10 rows.
    """
    raw_rows, _stats, _resource = _run_benchmark(
        _W_SAFE_INPUTS, repository, warmup=5, iterations=10, run_id="test-bh01"
    )
    assert len(raw_rows) == 10, (
        f"Expected 10 rows (iterations only), got {len(raw_rows)}; "
        "warm-up rows must be discarded."
    )


# ── BH02: Requested iteration count respected ─────────────────────────────────

def test_bh02_iteration_count(repository):
    """_run_benchmark with iterations=20 must return exactly 20 raw rows."""
    raw_rows, _stats, _resource = _run_benchmark(
        _W_CAUTION_INPUTS, repository, warmup=3, iterations=20, run_id="test-bh02"
    )
    assert len(raw_rows) == 20, (
        f"Expected 20 rows, got {len(raw_rows)}."
    )


# ── BH03: Raw timing rows — sequential iteration numbers and required fields ──

def test_bh03_row_fields_and_sequence(repository):
    """Each raw row must have the required fields and iteration numbers 1..N (no gaps)."""
    n = 15
    raw_rows, _stats, _resource = _run_benchmark(
        _W_UNSAFE_INPUTS, repository, warmup=2, iterations=n, run_id="test-bh03"
    )

    required_fields = {"run_id", "state", "workload_id", "iteration", "latency_ns", "latency_ms"}

    for row in raw_rows:
        missing = required_fields - set(row.keys())
        assert not missing, f"Row missing fields: {missing!r}. Row: {row!r}"

    iterations_seen = sorted(row["iteration"] for row in raw_rows)
    assert iterations_seen == list(range(1, n + 1)), (
        f"Expected iteration values 1–{n}, got {iterations_seen}."
    )


# ── BH04: Percentile calculation reproducible ─────────────────────────────────

def test_bh04_percentile_reproducible():
    """_compute_stats percentiles must agree with numpy.percentile to float tolerance."""
    latencies_ns = list(range(1, 101))          # 1..100 ns
    latencies_ms = [ns / 1_000_000.0 for ns in latencies_ns]

    stats = _compute_stats(latencies_ns)

    expected_p95 = float(np.percentile(latencies_ms, 95))
    expected_p99 = float(np.percentile(latencies_ms, 99))

    assert abs(stats["p95_ms"] - expected_p95) < 1e-9, (
        f"p95_ms mismatch: got {stats['p95_ms']}, expected {expected_p95}."
    )
    assert abs(stats["p99_ms"] - expected_p99) < 1e-9, (
        f"p99_ms mismatch: got {stats['p99_ms']}, expected {expected_p99}."
    )


# ── BH05: Summary derived from raw timing ────────────────────────────────────

def test_bh05_summary_from_raw(repository):
    """Stats returned by _run_benchmark must equal stats re-computed from raw latency_ns."""
    raw_rows, stats, _resource = _run_benchmark(
        _W_SAFE_INPUTS, repository, warmup=3, iterations=20, run_id="test-bh05"
    )

    latencies_ns = [row["latency_ns"] for row in raw_rows]
    recomputed = _compute_stats(latencies_ns)

    assert abs(stats["mean_ms"] - recomputed["mean_ms"]) < 1e-9, (
        f"mean_ms from _run_benchmark ({stats['mean_ms']}) does not match "
        f"re-computed value ({recomputed['mean_ms']})."
    )


# ── BH06: Hardware metadata emitted ──────────────────────────────────────────

def test_bh06_hardware_metadata():
    """_load_hardware_profile must return mac_model and chip_processor as non-empty strings.

    _hardware_id must return a non-empty string with no spaces.
    """
    output_dir = _REPO_ROOT / "data" / "journal1-e5-benchmark"
    hw_profile = _load_hardware_profile(output_dir)

    assert "mac_model" in hw_profile, (
        f"'mac_model' key missing from hardware profile: {hw_profile!r}"
    )
    assert "chip_processor" in hw_profile, (
        f"'chip_processor' key missing from hardware profile: {hw_profile!r}"
    )

    mac_model = hw_profile["mac_model"]
    chip_processor = hw_profile["chip_processor"]

    assert isinstance(mac_model, str) and mac_model.strip(), (
        f"'mac_model' must be a non-empty string, got {mac_model!r}."
    )
    assert isinstance(chip_processor, str) and chip_processor.strip(), (
        f"'chip_processor' must be a non-empty string, got {chip_processor!r}."
    )

    hw_id = _hardware_id(hw_profile)

    assert isinstance(hw_id, str) and hw_id.strip(), (
        f"_hardware_id must return a non-empty string, got {hw_id!r}."
    )
    assert " " not in hw_id, (
        f"_hardware_id must contain no spaces, got {hw_id!r}."
    )


# ── BH07: State/workload labels preserved in raw rows ────────────────────────

def test_bh07_labels_preserved(repository):
    """Every raw row from the W-SAFE workload must carry state='SAFE' and workload_id='W-SAFE'."""
    raw_rows, _stats, _resource = _run_benchmark(
        _W_SAFE_INPUTS, repository, warmup=2, iterations=10, run_id="test-bh07"
    )

    for row in raw_rows:
        assert row["state"] == "SAFE", (
            f"Expected state='SAFE', got {row['state']!r} in row {row!r}."
        )
        assert row["workload_id"] == "W-SAFE", (
            f"Expected workload_id='W-SAFE', got {row['workload_id']!r} in row {row!r}."
        )


# ── BH08: Governance outputs deterministic ───────────────────────────────────

def test_bh08_determinism_safe(repository):
    """_check_determinism for W-SAFE must not raise SystemExit."""
    _check_determinism(_W_SAFE_INPUTS, repository)


def test_bh08_determinism_caution(repository):
    """_check_determinism for W-CAUTION must not raise SystemExit."""
    _check_determinism(_W_CAUTION_INPUTS, repository)


def test_bh08_determinism_unsafe(repository):
    """_check_determinism for W-UNSAFE must not raise SystemExit."""
    _check_determinism(_W_UNSAFE_INPUTS, repository)
