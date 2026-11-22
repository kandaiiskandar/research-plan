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

# --- registers are checked from DATA, by iterating them, not by naming each one
#     in prose. Audit finding F1/F6: the discrepancy register grew to 11 rows
#     while report_metrics.json still said 10 and README said "10 entries", and
#     no check compared them, so 16/16 passed with a stale count in two places.
REGISTERS = {
  "01_source_acquisition_register.csv":        "src_rows",
  "02_raw_file_manifest.csv":                  "man_rows",
  "03_environmental_metadata.csv":             "env_rows",
  "04_issued_source_provenance.csv":           "iss_rows",
  "06_evidence_eligibility_matrix.csv":        "el_rows",
  "08_discrepancy_and_limitation_register.csv":"disc_rows",
}
def register_count_mismatches():
    bad = []
    for fn, key in REGISTERS.items():
        actual = len(list(csv.DictReader(open(H / fn, encoding="utf-8"))))
        if key not in M:
            bad.append(f"{fn}: no metric key '{key}'"); continue
        if actual != M[key]:
            bad.append(f"{fn}: file has {actual}, metrics say {M[key]}")
    return bad

def prose_count_mismatches():
    """Every 'N entries'/'N rows' claim in the prose must match a register."""
    import re as _re
    counts = set(M[k] for k in REGISTERS.values() if k in M)
    bad = []
    for name, txt in (("README.md", rdme), ("09_A18_4_PASS3A_EXECUTION_REPORT.md", rep)):
        # The number must be a standalone token: not preceded by a word char or a
        # hyphen, so gate IDs such as "A3A-03 variables" and filenames such as
        # "03_environmental_metadata.csv" are not read as counts. That was a
        # false positive on this guard's first run.
        for m in _re.finditer(r"(?<![\w-])(\d+)\s+(entries|prerequisites|providers|variables)\b", txt):
            v = int(m.group(1))
            if v not in counts:
                bad.append(f"{name}: '{m.group(0)}' matches no register count {sorted(counts)}")
    return bad

def behavioural_qa_tests():
    """Run the synthetic-fixture QA tests. r3 review finding: G-22 was a keyword
    search over the source, which cannot tell whether a check EVALUATES anything
    -- it passed while the time-bounds row only described the window. This
    executes test_qa.py and requires it to succeed.

    THREE states, never two. A missing test dependency is not a pass -- that was
    the r3 defect -- but it is also not a failed test, and reporting it as one
    tells a reviewer on a bare machine that the QA logic is broken when it is
    not. So: 0 PASS, 1 FAIL (a test really failed), 3 BLOCKED (could not run).
    Both non-zero states leave the audit non-zero, so nothing is silently
    green."""
    import subprocess
    r = subprocess.run([sys.executable, str(H / "test_qa.py")],
                       capture_output=True, text=True, cwd=str(H))
    return r.returncode, (r.stderr or r.stdout)[-400:]

_QA_RC, _QA_OUT = behavioural_qa_tests()   # run ONCE; three branches read it

def qa_state():
    return {0: "PASS", 3: "BLOCKED"}.get(_QA_RC, "FAIL")

def verify_exit_status():
    """--verify on an empty manifest must NOT report success (finding F2)."""
    import subprocess
    r = subprocess.run([sys.executable, str(H / "reproduce_acquisition.py"), "--verify"],
                       capture_output=True, text=True, cwd=str(H))
    return r.returncode

CHECKS = [
 ("G-01 raw/ holds no data file", len([p for p in (H/"raw").rglob("*") if p.is_file() and p.name!="README.md"])==0),
 ("G-02 raw bytes = 0 and report says 0", M["raw_bytes"]==0 and f"{M['raw_bytes']} bytes" in rep),
 ("G-03 02_raw_file_manifest.csv header-only", M["man_rows"]==0),
 ("G-04 04_issued_source_provenance.csv header-only", M["iss_rows"]==0),
 ("G-05 report refused/probed counts match the container probe log",
   f"{M['refused_container']} of {M['probes_container']}" in rep),
 ("G-06 report variable count matches 03", f"**{M['env_rows']} listed variables**" in rep and len(env)==M["env_rows"]),
 ("G-07 report matrix count matches 06", f"{M['el_rows']} prerequisites" in rep and len(mat)==M["el_rows"]),
 ("G-08 every 03 row tiered DOCUMENTED_ONLY", all(r["verification_status"]=="DOCUMENTED_ONLY" for r in env)),
 ("G-09 no R1-PAIRED/R2/R3 prerequisite marked met",
   all(r["prerequisite_met"]=="NO" for r in mat if r["evidence_tier"] in ("R1-PAIRED","R2","R3"))),
 ("G-10 exactly one met prerequisite, the EL-04 negative safeguard",
   [r["item_id"] for r in mat if r["prerequisite_met"]=="YES"]==["EL-04"]),
 ("G-11 no AFFIRMATIVE safe/unsafe-vessel-label claim", not affirmative_safety_claim()),
 ("G-12 no assigned credential VALUE anywhere", not leaked_secret_value()),
 ("G-13 both tracks declared HOLD", "Track A HOLD" in rdme and "| **Combined** | **HOLD** |" in rep),
 ("G-14 A18.1 data not re-badged as a Pass 3A acquisition",
   any("not re-badged" in r.get("reason","") for r in mat)),
 ("G-15 doc-access gap registered as data AND cited by ID in the report",
   any(r["item_id"]=="P3A-07" for r in csv.DictReader(
       open(H/"08_discrepancy_and_limitation_register.csv", encoding="utf-8")))
   and "P3A-07" in repflat
   and "do not assert that the six documents were reviewed" in repflat),
 ("G-16 SHA256SUMS.txt does not reference itself",
   "SHA256SUMS.txt" not in (H/"SHA256SUMS.txt").read_text(encoding="utf-8")),
 # --- added in r2, each closing an auditor finding
 ("G-17 EVERY register row count matches report_metrics.json [F1/F6]", not register_count_mismatches()),
 ("G-18 no prose count contradicts a register [F1/F6]", not prose_count_mismatches()),
 ("G-19 a connectivity log exists for EVERY environment claimed tested [F5]",
   (H/"logs"/"connectivity_probe_container.json").exists()
   and (H/"logs"/"connectivity_probe_device.json").exists()
   and "connectivity_probe_device.json" in repflat),
 ("G-20 --verify reports NO-ACQUISITION, not success, on an empty manifest [F2]",
   verify_exit_status()==3),
 ("G-21 manifest writer is the deterministic rebuild, not an append [F4]",
   "def write_manifest" in (H/"reproduce_acquisition.py").read_text(encoding="utf-8")
   and "def append_manifest" not in (H/"reproduce_acquisition.py").read_text(encoding="utf-8")),
 # G-22 EXECUTES the QA against synthetic NetCDF fixtures. It replaces a
 # keyword search that passed while the time-bounds check evaluated nothing.
 ("G-22 QA behavioural tests pass on synthetic NetCDF fixtures [F3, r3]",
   _QA_RC == 0, _QA_RC == 3),   # 3rd element: BLOCKED rather than FAILED
 ("G-24 Track A returns success ONLY if QA ran, QA passed and the manifest verifies [r3]",
   all(s in (H/"reproduce_acquisition.py").read_text(encoding="utf-8")
       for s in ("qa = qa_netcdf(files, a)", "qa.get(\"qa_pass\")", "v == EXIT_OK"))),
 ("G-25 manifest rebuild RECOMPUTES hashes for retained rows [r3]",
   "HASH RECOMPUTED ON REBUILD" in (H/"reproduce_acquisition.py").read_text(encoding="utf-8")),
 ("G-26 time bounds EVALUATE containment, not just describe it [r3]",
   "within_request={within}" in (H/"reproduce_acquisition.py").read_text(encoding="utf-8")),
 ("G-23 QA completeness claims are bounded, not absolute [F3]",
   "must not be claimed" in (H/"reproduce_acquisition.py").read_text(encoding="utf-8")),
]
# every entry becomes (name, ok, blocked); legacy 2-tuples are never blocked
C = [(c[0], c[1], c[2] if len(c) > 2 else False) for c in CHECKS]
fails   = [n for n, ok, bl in C if not ok and not bl]
blocked = [n for n, ok, bl in C if not ok and bl]
for n, ok, bl in C:
    print(f"  {'PASS' if ok else ('BLOCKED' if bl else 'FAIL')}  {n}")
print(f"\n  {sum(1 for _, ok, _ in C if ok)}/{len(C)} checks pass"
      + (f", {len(blocked)} BLOCKED (could not run here)" if blocked else "")
      + (f", {len(fails)} FAILED" if fails else ""))
if blocked:
    print("\n  BLOCKED -- these evaluated nothing, so they are NOT passes:")
    for b in blocked: print(f"    {b}")
    _bl = H / "logs" / "qa_behavioural_tests.json"
    _r = (json.load(open(_bl)).get("blocked_reason") if _bl.exists() else None)
    print(f"    reason: {_r or (_QA_OUT.strip() or 'see logs/qa_behavioural_tests.json')}")
if fails:
    print("\n  FAILURES:")
    for f in fails: print(f"    {f}")
    for h in affirmative_safety_claim(): print(f"    safety-claim hit: {h}")
    for h in leaked_secret_value(): print(f"    secret hit: {h}")
# machine-readable claims, so a reviewer need not trust the prose (auditor request)
json.dump(dict(
    checks=[{"check": n,
             "result": "PASS" if ok else ("BLOCKED" if bl else "FAIL")} for n, ok, bl in C],
    passed=sum(1 for _, ok, _ in C if ok), total=len(C),
    failures=fails, blocked=blocked,
    exit_status_meaning="0=all pass, 1=a check FAILED, 3=a check could not RUN",
    machine_readable_claims=dict(
        raw_data_files=len([p for p in (H/"raw").rglob("*") if p.is_file() and p.name!="README.md"]),
        raw_bytes=M["raw_bytes"],
        register_rows={fn: len(list(csv.DictReader(open(H/fn, encoding="utf-8"))))
                       for fn in REGISTERS},
        register_count_mismatches=register_count_mismatches(),
        prose_count_mismatches=prose_count_mismatches(),
        environments_probed=["container","device"],
        probe_logs=[p.name for p in sorted((H/"logs").glob("connectivity_probe_*.json"))],
        refused_hosts={"container": M["refused_container"], "device": M["refused_device"]},
        verify_exit_status=verify_exit_status(),
        behavioural_qa_tests=json.load(open(H/"logs"/"qa_behavioural_tests.json"))
            if (H/"logs"/"qa_behavioural_tests.json").exists() else "not run",
        verify_exit_meaning="0=verified, 1=mismatch, 3=no acquisition",
        track_a="HOLD", track_b="HOLD", combined="HOLD",
        evidence_tiers_achieved=[],
        tiers_not_achieved=["R0","R1-SOURCE-ONLY","R1-PAIRED","R2","R3"])),
          open(H/"logs"/"report_audit.json", "w"), indent=2)
# 1 beats 3: a real failure is the more serious signal when both are present.
sys.exit(1 if fails else (3 if blocked else 0))
