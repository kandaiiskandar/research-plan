"""Build script for Journal 1 Algorithm Specification — Batch 1.

Two duties:

1. Integrity check — re-hash the 16 protected canonical files pinned by
   ``integrity-before.json`` and confirm every entry is byte-identical to the
   pinned hash. Writes ``integrity-after.json`` with the verdict.

2. Parser check — for every CSV in this directory, verify that
   :mod:`csv.DictReader` reads it under a strict field-count check *and* that
   :func:`pandas.read_csv` reads it without raising. Writes
   ``parser-test-batch1.json`` with per-file verdicts.

The script is read-only against the wider project — it only writes into this
directory. Safe to re-run; every run overwrites the two output artefacts.
"""

from __future__ import annotations

import csv
import json
import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]  # data/journal1-algorithm-specification -> repo root


def git_hash(rel_path: str) -> str:
    """Return the git-hash-object SHA-1 for a repo-relative path."""
    result = subprocess.run(
        ["git", "hash-object", rel_path],
        cwd=REPO,
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def integrity_check() -> dict:
    before = json.loads((HERE / "integrity-before.json").read_text())
    expected: dict[str, str] = before["protected_files"]
    observed: dict[str, str] = {}
    diffs: list[str] = []
    for rel, want in expected.items():
        got = git_hash(rel)
        observed[rel] = got
        if got != want:
            diffs.append(f"{rel}: expected {want}, got {got}")
    verdict = "PASS" if not diffs else "FAIL"
    return {
        "verdict": verdict,
        "protected_file_count": len(expected),
        "unchanged": sum(1 for r in expected if observed[r] == expected[r]),
        "changed": len(diffs),
        "diffs": diffs,
        "observed": observed,
    }


def strict_csv_check(path: Path) -> dict:
    """Read a CSV under csv.DictReader with strict field count, then pandas."""
    result: dict[str, object] = {"file": path.name}
    # csv.DictReader strict field-count check
    try:
        with path.open(newline="", encoding="utf-8") as fh:
            reader = csv.reader(fh)
            header = next(reader)
            expected_fields = len(header)
            row_count = 0
            for lineno, row in enumerate(reader, start=2):
                if len(row) != expected_fields:
                    raise ValueError(
                        f"line {lineno}: got {len(row)} fields, expected {expected_fields}"
                    )
                row_count += 1
        result["csv_reader_strict"] = "PASS"
        result["header_field_count"] = expected_fields
        result["data_row_count"] = row_count
    except Exception as exc:  # pragma: no cover — surfaced in the JSON
        result["csv_reader_strict"] = f"FAIL — {exc}"
    # csv.DictReader — verify keys are stable
    try:
        with path.open(newline="", encoding="utf-8") as fh:
            dict_reader = csv.DictReader(fh)
            for row in dict_reader:
                assert None not in row, "csv.DictReader saw an unnamed extra field"
        result["csv_dictreader"] = "PASS"
    except Exception as exc:
        result["csv_dictreader"] = f"FAIL — {exc}"
    # pandas.read_csv
    try:
        import pandas as pd  # noqa: WPS433 — deliberate lazy import

        df = pd.read_csv(path)
        result["pandas_read_csv"] = "PASS"
        result["pandas_row_count"] = int(len(df))
    except Exception as exc:
        result["pandas_read_csv"] = f"FAIL — {exc}"
    result["overall"] = (
        "PASS"
        if all(
            str(result.get(key)).startswith("PASS")
            for key in ("csv_reader_strict", "csv_dictreader", "pandas_read_csv")
        )
        else "FAIL"
    )
    return result


def parser_check() -> dict:
    csv_paths = sorted(HERE.glob("*.csv"))
    files = [strict_csv_check(p) for p in csv_paths]
    overall = "PASS" if all(f["overall"] == "PASS" for f in files) else "FAIL"
    return {"overall": overall, "count": len(files), "files": files}


def main() -> int:
    integrity = integrity_check()
    (HERE / "integrity-after.json").write_text(json.dumps(integrity, indent=2) + "\n")

    parser = parser_check()
    (HERE / "parser-test-batch1.json").write_text(json.dumps(parser, indent=2) + "\n")

    print(f"integrity: {integrity['verdict']} — {integrity['unchanged']} unchanged, "
          f"{integrity['changed']} changed")
    print(f"parser:    {parser['overall']} — {parser['count']} CSVs checked")

    if integrity["verdict"] != "PASS" or parser["overall"] != "PASS":
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
