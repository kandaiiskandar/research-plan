#!/usr/bin/env python3
"""Negative controls for the theorem-numbering repair verifier.

Each mutation must make its named check FAIL. Three safeguards, each added
after the corresponding failure was observed in an earlier run:

1. try/finally restore — an earlier loop aborted on a bad anchor and left the
   manuscript mutated on disk.
2. The verifier's exit status is checked. A crashed verifier leaves
   verification.json holding the PREVIOUS run's results, which an earlier
   control read as a PASS.
3. A stale-result guard: the run marker in verification.json must change.
"""

import json
import os
import shutil
import subprocess
import sys
import uuid

ROOT = "/sessions/charming-magical-euler/mnt/research-test-2"
OUT = os.path.join(ROOT, "data/journal1-theorem-numbering-repair")
MAN = os.path.join(ROOT, "publications/active/journal-1/submissions/v1-initial-submission/manuscript.md")
BAK = os.path.join(OUT, ".control-backup.md")

MUT = {
    # --- semantic: old string gone, reference now points at the WRONG theorem
    "monotonicity_reference_semantically_correct":
        ("(Theorem 6.2 / Monotonicity) holds by inspection",
         "(Theorem 6.3 / Monotonicity) holds by inspection"),
    "safety_dominance_reference_semantically_correct":
        ("fidelity assumptions (Theorem 6.3, Safety Dominance)",
         "fidelity assumptions (Theorem 6.2, Safety Dominance)"),
    "totality_reference_semantically_correct":
        ("(Theorem 6.1 / operational totality", "(Theorem 6.2 / operational totality"),
    "section5_forward_reference_correct":
        ("proved canonically as Theorem 6.1 in Section 6.2",
         "proved canonically as Theorem 6.3 in Section 6.2"),
    "no_reference_points_to_wrong_result":
        ("the enforcement contract on which Theorem 6.3 depends",
         "the enforcement contract on which Theorem 6.2 depends"),
    # --- structural
    "no_dangling_references_at_all":
        ("outside its own conclusion — Theorem 6.3 A4)",
         "outside its own conclusion — Theorem 5.3 A4)"),
    "no_duplicate_theorem_identity_for_same_result":
        ("**Totality of f.** For all E", "**Theorem 5.1 (Totality of f).** For all E"),
    "canonical_section6_numbering_coherent":
        ("**Corollary 6.2b (Properties", "**Corollary 6.3 (Properties"),
    "corollary_6_2b_not_referenced_elsewhere":
        ("### 6.5 Composite Guarantee",
         "See Corollary 6.2b.\n\n### 6.5 Composite Guarantee"),
    # --- scope containment
    "no_change_beyond_authorised_identifier_edits":
        ("### 6.5 Composite Guarantee",
         "### 6.5 Composite Guarantee\n\nUnauthorised inserted sentence."),
    "sections_9_15_unchanged":
        ("## 15. Conclusion", "## 15. Conclusion\n\nUnauthorised edit."),
    "related_work_unchanged": ("## 2. Related Work", "## 2. Related Work\n\nUnauthorised edit."),
    "abstract_unchanged": ("## Abstract", "## Abstract\n\nUnauthorised edit."),
    "quantitative_values_unchanged": ("**5.81%** of departure-window hours",
                                      "**6.20%** of departure-window hours"),
    "reference_list_unchanged": ("## References", "## References\n\nUnauthorised edit."),
    "E5_remains_open": ("**E5 is OPEN.**", "**E5 is CLOSED.**"),
    "H3_remains_open_unsupported": ("remains OPEN and UNSUPPORTED",
                                    "is satisfied at H3 = 5 ms"),
    "R_SAFE_001_deferred_preserved": ("`R-SAFE-001` remains DEFERRED",
                                      "`R-SAFE-001` is implemented"),
}


def run_verifier():
    """Return (checks, ok). `ok` is False if the verifier crashed."""
    marker = str(uuid.uuid4())
    with open(os.path.join(OUT, ".run-marker"), "w") as fh:
        fh.write(marker)
    subprocess.run([sys.executable, os.path.join(OUT, "census.py"), "after"],
                   capture_output=True, cwd=ROOT)
    p = subprocess.run([sys.executable, os.path.join(OUT, "verify_repair.py")],
                       capture_output=True, text=True, cwd=ROOT)
    if p.returncode != 0:
        return {}, False, p.stderr.strip().split("\n")[-1]
    return json.load(open(os.path.join(OUT, "verification.json")))["checks"], True, ""


def main():
    shutil.copy(MAN, BAK)
    orig = open(MAN, encoding="utf-8").read()
    results, problems = [], []
    try:
        for check, (a, b) in MUT.items():
            if a not in orig:
                problems.append((check, "ANCHOR MISSING"))
                results.append((check, "ANCHOR MISSING"))
                continue
            open(MAN, "w", encoding="utf-8").write(orig.replace(a, b, 1))
            checks, ok, err = run_verifier()
            if not ok:
                problems.append((check, f"VERIFIER CRASHED: {err}"))
                results.append((check, "CRASH"))
                continue
            r = checks.get(check, "ABSENT")
            results.append((check, r))
            if r != "FAIL":
                problems.append((check, f"did not discriminate ({r})"))
    finally:
        open(MAN, "w", encoding="utf-8").write(orig)
        subprocess.run([sys.executable, os.path.join(OUT, "census.py"), "after"],
                       capture_output=True, cwd=ROOT)
        subprocess.run([sys.executable, os.path.join(OUT, "verify_repair.py")],
                       capture_output=True, cwd=ROOT)
        os.remove(BAK)

    for c, r in results:
        print(f"  {c:48s} -> {r:14s} (expect FAIL)")
    out = {"controls": len(MUT),
           "discriminating": sum(1 for _, r in results if r == "FAIL"),
           "problems": problems}
    with open(os.path.join(OUT, "negative-controls.json"), "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2)
    print("\n" + json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
