#!/usr/bin/env python3
"""
Build / verify the Journal 1 Evaluation Specification evidence directory.

What it does
------------
- Recomputes SHA-1 hashes for every protected file listed in integrity-before.json
  and writes integrity-after.json.
- Parses every CSV in this directory with (i) csv.DictReader and (ii)
  pandas.read_csv, with strict field-count checking, and writes parser-test.json.
- Reports whether protected hashes are unchanged (task §36 requirement).

Usage
-----
    python data/journal1-evaluation-specification/build.py

Read-only. Writes only to this directory.
"""

from __future__ import annotations

import csv
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent


def git_hash(path: Path) -> str:
    """Return git-hash-object (blob SHA-1) for a file, or 'MISSING' if absent."""
    if not path.is_file():
        return "MISSING"
    result = subprocess.run(
        ["git", "hash-object", str(path)],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def load_integrity_before() -> dict:
    """Load the frozen pre-edit hash record."""
    with (HERE / "integrity-before.json").open() as f:
        return json.load(f)


def build_integrity_after(before: dict) -> dict:
    """Recompute hashes for every protected file listed in integrity-before.json."""
    after_files: dict[str, str] = {}
    for rel_path in before["protected_files"]:
        after_files[rel_path] = git_hash(REPO / rel_path)
    return {
        "purpose": "Recompute protected canonical hashes after Journal 1 Evaluation Specification Alignment edits and verify no protected canonical state changed.",
        "captured_on": "2026-09-10",
        "branch": before["branch"],
        "hash_algorithm": before["hash_algorithm"],
        "protected_files": after_files,
        "verification": _diff_hashes(before["protected_files"], after_files),
    }


def _diff_hashes(before: dict, after: dict) -> dict:
    changed = [k for k in before if before[k] != after.get(k)]
    return {
        "unchanged_files": len(before) - len(changed),
        "changed_files": changed,
        "verdict": "PASS" if not changed else "FAIL — protected canonical change required (JES-R6)",
    }


def parser_test() -> dict:
    """Parse every CSV in this directory with csv.DictReader and pandas.read_csv."""
    results: list[dict] = []
    for csv_path in sorted(HERE.glob("*.csv")):
        record: dict = {"file": csv_path.name}
        # csv.DictReader with strict field-count checking
        try:
            with csv_path.open(newline="") as f:
                reader = csv.reader(f)
                header = next(reader)
                expected = len(header)
                rows_read = 0
                for lineno, row in enumerate(reader, start=2):
                    if len(row) != expected:
                        raise ValueError(
                            f"Row {lineno}: {len(row)} fields, expected {expected}"
                        )
                    rows_read += 1
            record["csv_DictReader"] = {
                "status": "PASS",
                "columns": expected,
                "data_rows": rows_read,
            }
        except Exception as exc:
            record["csv_DictReader"] = {"status": "FAIL", "error": str(exc)}

        # pandas.read_csv strict parse
        try:
            import pandas as pd  # imported lazily so the script runs without pandas installed
            df = pd.read_csv(csv_path)
            record["pandas_read_csv"] = {
                "status": "PASS",
                "columns": len(df.columns),
                "data_rows": len(df),
            }
        except ImportError:
            record["pandas_read_csv"] = {"status": "SKIPPED", "reason": "pandas not installed"}
        except Exception as exc:
            record["pandas_read_csv"] = {"status": "FAIL", "error": str(exc)}

        results.append(record)

    overall = "PASS" if all(
        r["csv_DictReader"]["status"] == "PASS"
        and r["pandas_read_csv"]["status"] in {"PASS", "SKIPPED"}
        for r in results
    ) else "FAIL"

    return {
        "purpose": "Verify every CSV in this directory parses cleanly with csv.DictReader and pandas.read_csv (strict field-count checking).",
        "captured_on": "2026-09-10",
        "overall_verdict": overall,
        "files": results,
    }


def main() -> None:
    before = load_integrity_before()
    after = build_integrity_after(before)
    (HERE / "integrity-after.json").write_text(json.dumps(after, indent=2) + "\n")

    parser_result = parser_test()
    (HERE / "parser-test.json").write_text(json.dumps(parser_result, indent=2) + "\n")

    print("integrity-after.json:", after["verification"]["verdict"])
    if after["verification"]["changed_files"]:
        for f in after["verification"]["changed_files"]:
            print(f"  CHANGED: {f}")
    print("parser-test.json:  ", parser_result["overall_verdict"])
    for r in parser_result["files"]:
        d = r["csv_DictReader"]
        p = r["pandas_read_csv"]
        print(f"  {r['file']:52s} DictReader={d['status']:6s} pandas={p['status']:8s}")


if __name__ == "__main__":
    main()
