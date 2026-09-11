"""
Journal 1 Layer 3 Prototype — Batch 1 build script.

Verifies protected canonical state integrity and validates all batch CSVs
with strict field-count parsing. Emits integrity-after.json and parser-test-batch1.json.

Usage: python3 data/journal1-layer3-prototype/build.py
Must be run from the repository root.
"""

import csv
import json
import subprocess
from pathlib import Path

PROTECTED_FILES = {
    "docs/canonical/appendix-c-formalisation.md": "17ebfaba0dc0c8f5758e84a791d6b41b820ebd09",
    "docs/canonical/evaluation-design-rq4.md": "85a7cc5505efd819ce515ec7f889374691e5929d",
    "docs/canonical/empirical-findings-2026-09-06.md": "403b7aaf7d2d4d7b08667d73ab59e6c698d325cc",
    "scripts/condition_comparison.py": "935f1a1164eff89cd8c84d8a32cb39963d1b2428",
    "scripts/canonical_gt.py": "6cdea503156bbed51add8bd557598a488da134a4",
    "scripts/canonical_figures.py": "e9cd766ce8223de2e7e16f56ae0f349c168ec841",
    "scripts/historical_replay.py": "c002befa80f0e1a5def3fa711aaff8419cc49a2a",
    "scripts/hysteresis_analysis.py": "3466f34b260eb74e12181949fee3786141f0da48",
    "scripts/diagnostic_binding.py": "7373e91e280a9b623d250eec9750dde07336fe5a",
    "data/prediction-register.csv": "46486e2d1ac9e03a104d7b04f5851df5d2b10b5c",
    "data/solar/solar-events-daily.csv": "d2d05382d7989f283d28088f0b7a54cf7b1653d1",
    "data/raw_weather_sea.csv": "12812051be824c36d2db644f0b118f31d94c8e55",
    "data/raw_marine_era5_sea.csv": "380a4044f7e6c4567f773fe10635005848a43552",
    "data/raw_marine_mfwam.csv": "933dccb05e706c2c75229b3441bacfda69bab773",
    "publications/active/ipsci-2026/submissions/v3-revision/manuscript-v3.md": "dfd25f0ae6beee62499132cbfae7edc75ccf1937",
    "publications/active/ipsci-2026/submissions/v2-post-review/manuscript-v2.5-submitted.md": "315fd89e26e56574ab4e74c0faeb485f3dda32e4",
}

BATCH1_CSVS = [
    "data/journal1-layer3-prototype/prototype-contract-batch1.csv",
    "data/journal1-layer3-prototype/module-map-batch1.csv",
    "data/journal1-layer3-prototype/fidelity-instrumentation-batch1.csv",
    "data/journal1-layer3-prototype/test-plan-batch1.csv",
    "data/journal1-layer3-prototype/open-decisions-batch1.csv",
    "data/journal1-layer3-prototype/change-map-batch1.csv",
]

OUT_DIR = Path("data/journal1-layer3-prototype")


def git_hash(path: str) -> str:
    result = subprocess.run(
        ["git", "hash-object", path],
        capture_output=True, text=True, check=True,
    )
    return result.stdout.strip()


def strict_csv_check(path: str) -> dict:
    result = {"path": path, "status": "PASS", "errors": []}
    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            rows = list(reader)
        if not rows:
            result["status"] = "FAIL"
            result["errors"].append("Empty file")
            return result
        expected_fields = len(rows[0])
        for i, row in enumerate(rows[1:], start=2):
            if len(row) != expected_fields:
                result["status"] = "FAIL"
                result["errors"].append(
                    f"line {i}: got {len(row)} fields, expected {expected_fields}"
                )
        result["row_count"] = len(rows) - 1
        result["field_count"] = expected_fields
    except Exception as exc:
        result["status"] = "FAIL"
        result["errors"].append(str(exc))
    return result


def verify_integrity() -> dict:
    unchanged, changed = [], []
    for path, expected in PROTECTED_FILES.items():
        try:
            actual = git_hash(path)
        except subprocess.CalledProcessError as exc:
            changed.append({"path": path, "expected": expected, "actual": f"ERROR: {exc}"})
            continue
        if actual == expected:
            unchanged.append(path)
        else:
            changed.append({"path": path, "expected": expected, "actual": actual})

    verdict = "PASS" if not changed else "FAIL"
    return {
        "task": "Journal 1 Layer 3 Prototype Implementation — Batch 1",
        "verified_on": "2026-09-11",
        "branch": "feat/journal1-layer3-prototype",
        "hash_algorithm": "git-hash-object (SHA-1 with blob header)",
        "unchanged_count": len(unchanged),
        "changed_count": len(changed),
        "changed": changed,
        "verdict": f"{verdict} — {len(unchanged)} unchanged, {len(changed)} changed",
    }


def run_parser_checks(paths: list[str]) -> dict:
    results = [strict_csv_check(p) for p in paths]
    all_pass = all(r["status"] == "PASS" for r in results)
    return {
        "verdict": "PASS" if all_pass else "FAIL",
        "checked": len(results),
        "results": results,
    }


def main():
    integrity = verify_integrity()
    (OUT_DIR / "integrity-after.json").write_text(
        json.dumps(integrity, indent=2), encoding="utf-8"
    )

    batch1_checks = run_parser_checks(BATCH1_CSVS)
    (OUT_DIR / "parser-test-batch1.json").write_text(
        json.dumps(batch1_checks, indent=2), encoding="utf-8"
    )

    print(f"integrity:     {integrity['verdict']}")
    print(f"parser batch1: {batch1_checks['verdict']} — {batch1_checks['checked']} CSVs checked")


if __name__ == "__main__":
    main()
