#!/usr/bin/env python3
"""
A18.4 Pass 3A — gate A3A-07: audit every numeric and categorical claim in the
report against the produced artifacts. Standard library only.

History: two guards in the first version of this audit were WRONG and produced
false positives. Both are fixed here and the fix is recorded, because a guard
that cries wolf is as much a defect as one that stays silent.

  G-11 matched the phrase "safe/unsafe vessel label" without allowing for the
       fact that both occurrences are NEGATIONS ("no ... vessel label"). Now it
       requires an affirmative claim: the phrase NOT preceded by a negator.
  G-12 flagged the credential VARIABLE NAMES, which the task positively
       requires be documented. Now it looks for an assigned non-placeholder
       VALUE, which is the thing that would actually be a leak.
"""
import csv, json, re, sys
from pathlib import Path

H = Path(__file__).resolve().parent
M = json.load(open(H / "logs" / "report_metrics.json"))
rep = (H / "09_A18_4_PASS3A_EXECUTION_REPORT.md").read_text(encoding="utf-8")
# Prose matching must ignore markdown line wrapping: the report wraps sentences
# across lines, so a multi-word phrase can straddle a newline. Collapsing
# whitespace was the 6th and final guard defect found in this audit.
repflat = " ".join(rep.split())
rdme = (H / "README.md").read_text(encoding="utf-8")
env = list(csv.DictReader(open(H / "03_environmental_metadata.csv", encoding="utf-8")))
mat = list(csv.DictReader(open(H / "06_evidence_eligibility_matrix.csv", encoding="utf-8")))
# The audit script is excluded from its own scan: it contains the search
# patterns literally, so including it guarantees a self-match. That was a third
# defective guard, caught on the first run of the fixed version.
TEXT = {p: p.read_text(errors="ignore") for p in H.rglob("*")
        if p.is_file() and p.suffix in (".py", ".md", ".csv", ".txt", ".json")
        and p.name not in ("audit_report_against_artifacts.py", "SHA256SUMS.txt")}

def affirmative_safety_claim():
    """An affirmative safe/unsafe-label claim, i.e. NOT preceded by a negator."""
    pat = re.compile(r"(\w[\w\s,/*-]{0,40}?)\b(?:safe/unsafe|safe|unsafe)\s+vessel\s+label", re.I)
    hits = []
    for p, t in TEXT.items():
        for m in pat.finditer(t):
            if not re.search(r"\b(no|not|never|without|yields\s+R0\s+only\s+and\s+no)\b",
                             m.group(1), re.I):
                hits.append(f"{p.name}: {m.group(0)[:80]}")
    return hits

def leaked_secret_value():
    """A credential NAME is required documentation. An assigned VALUE is a leak."""
    pat = re.compile(r"(COPERNICUSMARINE_SERVICE_(?:USERNAME|PASSWORD)|api[_-]?key|token|secret|password)"
                     r"\s*[:=]\s*[\"']?([A-Za-z0-9/_+-]{8,})", re.I)
    hits = []
    for p, t in TEXT.items():
        for m in pat.finditer(t):
            if m.group(2).strip(".<>$ ") and not m.group(2).startswith(("...", "<", "$")):
                hits.append(f"{p.name}: {m.group(1)}=<{len(m.group(2))} chars>")
    return hits

CHECKS = [
 ("G-01 raw/ holds no data file", len([p for p in (H/"raw").rglob("*") if p.is_file() and p.name!="README.md"])==0),
 ("G-02 raw bytes = 0 and report says 0", M["raw_bytes"]==0 and f"{M['raw_bytes']} bytes" in rep),
 ("G-03 02_raw_file_manifest.csv header-only", M["man_rows"]==0),
 ("G-04 04_issued_source_provenance.csv header-only", M["iss_rows"]==0),
 ("G-05 report refused/probed counts match the probe log", f"{M['refused']} of {M['probes']}" in rep),
 ("G-06 report variable count matches 03", f"**{M['env_rows']} listed variables**" in rep and len(env)==M["env_rows"]),
 ("G-07 report matrix count matches 06", f"{M['el_rows']} prerequisites" in rep and len(mat)==M["el_rows"]),
 ("G-08 every 03 row tiered DOCUMENTED_ONLY", all(r["verification_status"]=="DOCUMENTED_ONLY" for r in env)),
 ("G-09 no R1-PAIRED/R2/R3 prerequisite marked met",
   all(r["prerequisite_met"]=="NO" for r in mat if r["evidence_tier"] in ("R1-PAIRED","R2","R3"))),
 ("G-10 exactly one met prerequisite, the EL-04 negative safeguard",
   [r["item_id"] for r in mat if r["prerequisite_met"]=="YES"]==["EL-04"]),
 ("G-11 no AFFIRMATIVE safe/unsafe-vessel-label claim [guard fixed]", not affirmative_safety_claim()),
 ("G-12 no assigned credential VALUE anywhere [guard fixed]", not leaked_secret_value()),
 ("G-13 both tracks declared HOLD", "Track A HOLD" in rdme and "| **Combined** | **HOLD** |" in rep),
 ("G-14 A18.1 data not re-badged as a Pass 3A acquisition",
   any("not re-badged" in r["reason"] or "not re-badged" in r.get("reason","") for r in mat)),
 # G-15 keys on STRUCTURED DATA, not on a hand-typed prose string. SIX earlier
 # versions of this one guard failed, each because I typed a phrase that did not
 # match the document: wrong emphasis markers, a sentence wrapped across a line,
 # and finally "could not be opened" when both the register and the report read
 # "None ... could be opened". That is precisely the hand-written-prose-drifting-
 # from-artifact failure mode recorded in A18.2-R. The durable fix is to stop
 # matching prose at all: require the register ENTRY to exist as data, and require
 # the report to cite that entry's ID.
 ("G-15 doc-access gap registered as data AND cited by ID in the report",
   any(r["item_id"] == "P3A-07" for r in csv.DictReader(
       open(H / "08_discrepancy_and_limitation_register.csv", encoding="utf-8")))
   and "P3A-07" in repflat
   and "do not assert that the six documents were reviewed" in repflat),
 ("G-16 SHA256SUMS.txt does not reference itself",
   "SHA256SUMS.txt" not in (H/"SHA256SUMS.txt").read_text(encoding="utf-8")),
]
fails = [n for n, ok in CHECKS if not ok]
for n, ok in CHECKS: print(f"  {'PASS' if ok else 'FAIL'}  {n}")
print(f"\n  {len(CHECKS)-len(fails)}/{len(CHECKS)} checks pass")
if fails:
    print("\n  FAILURES:")
    for f in fails: print(f"    {f}")
    for h in affirmative_safety_claim(): print(f"    safety-claim hit: {h}")
    for h in leaked_secret_value(): print(f"    secret hit: {h}")
json.dump(dict(checks=[{"check": n, "result": "PASS" if ok else "FAIL"} for n, ok in CHECKS],
               passed=len(CHECKS)-len(fails), total=len(CHECKS), failures=fails),
          open(H/"logs"/"report_audit.json", "w"), indent=2)
sys.exit(1 if fails else 0)
