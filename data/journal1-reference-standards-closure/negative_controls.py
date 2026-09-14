#!/usr/bin/env python3
"""The 14 negative controls mandated by task brief §21, plus 4 extras.

Safeguards carried forward from the previous batch: try/finally restore, and
the verifier's exit status is checked so a crash is never mistaken for a pass.
"""

import json
import os
import shutil
import subprocess
import sys

ROOT = "/sessions/charming-magical-euler/mnt/research-test-2"
OUT = os.path.join(ROOT, "data/journal1-reference-standards-closure")
MAN = os.path.join(ROOT, "publications/active/journal-1/submissions/v1-initial-submission/manuscript.md")

MUT = {
    # §21.1 fake DOI inserted into a repaired reference
    "only_authorised_dois_added":
        ("2023, pp. 1–8. doi: 10.1109/SII55687.2023.10039301",
         "2023, pp. 1–8. doi: 10.9999/fabricated.2023.000001"),
    # §21.2 changed publication year on a repaired reference
    "no_publication_year_changed":
        ('reasoning," in *Proc. 42nd Int. Conf. Machine Learning (ICML)*, Vancouver, Canada, in *Proceedings of Machine Learning Research*, vol. 267, 2025',
         'reasoning," in *Proc. 42nd Int. Conf. Machine Learning (ICML)*, Vancouver, Canada, in *Proceedings of Machine Learning Research*, vol. 267, 2024'),
    # §21.3 remove the source supporting the standards claim
    "retained_observation_cited_to_2":
        ("distinct from a runtime state classification governing system behaviour [2]",
         "distinct from a runtime state classification governing system behaviour"),
    # §21.4 replace direct support with context-only support.
    # The mutation must downgrade the ATTRIBUTION, not merely reword a framing
    # sentence — an earlier version changed the wrong sentence and the check
    # correctly passed, which made the control look broken when it was mis-aimed.
    "substantive_observation_retained":
        ("A cross-domain survey of AI in safety-critical industrial and transportation "
         "systems records that",
         "Industry commentary and vendor white papers suggest that"),
    # §21.5 compliance claim
    "no_compliance_or_certification_claim":
        ("The two are complementary rather than competing",
         "The architecture complies with IEC 61508 and the two are complementary"),
    # §21.6 certified safe
    "no_physical_safety_guarantee_introduced":
        ("no claim of compliance, conformance or certification against any integrity-level scheme is made or implied.",
         "the architecture is certified safe and guarantees the system is safe."),
    # §21.7 strengthened novelty
    "novelty_claim_not_strengthened":
        ("A related distinction concerns",
         "This is the first formally verified AI governance architecture. A related distinction concerns"),
    # §21.8 marker reintroduced
    "citation_support_required_removed":
        ("A related distinction concerns",
         "> **[CITATION SUPPORT REQUIRED]**\n\nA related distinction concerns"),
    # §21.9 orphan an in-text citation
    "all_citations_resolve":
        ("governing system behaviour [2]", "governing system behaviour [99]"),
    # §21.10 uncited reference entry
    "no_orphan_references":
        ("[33] P. Bhuvaneswari", "[34] Z. Uncited, \"An entry nobody cites,\" 2026.\n\n[33] P. Bhuvaneswari"),
    # §21.11 theorem number changed
    "theorem_numbering_still_closed":
        ("**Theorem 6.2 (Monotonicity of A_AI).**", "**Theorem 5.2 (Monotonicity of A_AI).**"),
    # §21.12 quantitative value changed
    "quantitative_values_unchanged":
        ("**5.81%** of departure-window hours", "**6.40%** of departure-window hours"),
    # §21.13 E5 flipped
    "E5_remains_open": ("**E5 is OPEN.**", "**E5 is CLOSED.**"),
    # §21.14 H3 passed
    "H3_remains_open_unsupported":
        ("remains OPEN and UNSUPPORTED", "is satisfied at H3 = 5 ms"),
    # --- extras beyond the mandated set
    "process_prose_removed":
        ("A related distinction concerns",
         "The repository contains no extraction notes for these standards. A related distinction concerns"),
    "no_new_standards_citation_added":
        ("used in functional safety", "used in functional safety such as ISO 26262"),
    "section5_plan_unmodified": ("__TOUCH_PLAN_FILE__", ""),
    "related_work_not_broadened":
        ("### 2.7 Domain literature",
         "Additional related work is surveyed here at length.\n\n### 2.7 Domain literature"),
    # Reinstate the venue-wide DOI-policy generalisation that the evidence does
    # not support. Must be caught.
    "no_venue_wide_doi_policy_claim":
        ("Proceedings of Machine Learning Research; no DOI is listed in its official "
         "PMLR publication record, so its",
         "Proceedings of Machine Learning Research, which assigns no DOI; its"),
    "pmlr_no_doi_scoped_to_its_record":
        ("no DOI is listed in its official PMLR publication record",
         "PMLR does not issue DOIs"),
}

PLAN = os.path.join(ROOT, "publications/active/journal-1/section-5-plan.md")


def run():
    subprocess.run([sys.executable, os.path.join(OUT, "census.py"), "after"],
                   capture_output=True, cwd=ROOT)
    p = subprocess.run([sys.executable, os.path.join(OUT, "verify_closure.py")],
                       capture_output=True, text=True, cwd=ROOT)
    if p.returncode != 0:
        return {}, False, p.stderr.strip().split("\n")[-1]
    return json.load(open(os.path.join(OUT, "verification.json")))["checks"], True, ""


def main():
    orig = open(MAN, encoding="utf-8").read()
    plan_orig = open(PLAN, encoding="utf-8").read()
    results, problems = [], []
    try:
        for check, (a, b) in MUT.items():
            if a == "__TOUCH_PLAN_FILE__":
                open(PLAN, "a", encoding="utf-8").write("\n<!-- unauthorised edit -->\n")
            elif a not in orig:
                problems.append((check, "ANCHOR MISSING"))
                results.append((check, "ANCHOR MISSING"))
                continue
            else:
                open(MAN, "w", encoding="utf-8").write(orig.replace(a, b, 1))
            checks, ok, err = run()
            open(MAN, "w", encoding="utf-8").write(orig)
            open(PLAN, "w", encoding="utf-8").write(plan_orig)
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
        open(PLAN, "w", encoding="utf-8").write(plan_orig)
        run()

    for c, r in results:
        print(f"  {c:44s} -> {r:14s} (expect FAIL)")
    out = {"controls": len(MUT),
           "mandated_by_brief_section_21": 14,
           "discriminating": sum(1 for _, r in results if r == "FAIL"),
           "problems": problems}
    with open(os.path.join(OUT, "negative-controls.json"), "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2)
    print("\n" + json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
