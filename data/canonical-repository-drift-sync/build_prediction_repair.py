#!/usr/bin/env python3
"""Prediction-state residue closure repair — evidence artefacts."""
import csv, json, hashlib, pathlib, io, collections
import pandas as pd
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
F = ["id","file","locator","claim","classification","action","status","notes"]
rows = [
 ("PS-01","docs/canonical/empirical-findings-2026-09-06.md","Document Status line (line 4)","All 24 pre-registered predictions resolved - 22 confirmed, 2 refuted","ACTIVE-CANONICAL-DRIFT","Replaced with 15 CONFIRMED / 9 REFUTED, the nine refuted IDs named, SDR attribution limited to P20/P23/P24, register named as the authority","REPAIRED","THE KNOWN RESIDUE. A document-level status line is the highest-risk location for a stale summary - it is what a reader takes as the state before reading anything else"),
 ("PS-02","docs/canonical/empirical-findings-2026-09-06.md","Part 4 pre-registration paragraph","22 confirmed, 2 refuted","ACTIVE-CANONICAL-DRIFT","Scoped inline as the 2026-09-06 count and pointed at the corrected banner","REPAIRED","Same document, ~490 lines below the status line"),
 ("PS-03","docs/canonical/empirical-findings-2026-09-06.md","Banner above 'The single refutation...'","The register's refutation is now P01","ACTIVE-CANONICAL-DRIFT - SELF-INFLICTED","Rewritten: no single refutation exists; nine refuted IDs named; the earlier wording identified as a 22/2-era reading","REPAIRED","I ADDED THIS ERROR in the preceding closure repair. Written while reasoning in the 22/2 frame, it silently asserted a single refutation when the canonical register has nine. A correction annotation became a new stale authority in under a day"),
 ("PS-04","docs/canonical/decision-record-empirical-first.md","Outcome line, section 5/6 area","All 24 pre-registered predictions resolved: 22 confirmed, 2 refuted (P16 - the refutation...)","ACTIVE-CANONICAL-DRIFT","Replaced with 15/9 and the refuted IDs; superseded text quoted in a dated note; P16's CONFIRMED status stated","REPAIRED","Doubly wrong: stale count AND names P16 as the refutation when P16 is CONFIRMED"),
 ("PS-05","docs/canonical/session-log-2026-09-06.md","Part 4 - Method: pre-registration","22 confirmed, 2 refuted (24 predictions); The refutation (P16 ...)","ACTIVE-CANONICAL-DRIFT (dated narrative)","ANNOTATED, not rewritten","REPAIRED","Dated session log: annotated with a HISTORICAL banner giving the canonical count and P16's re-resolution, preserving the day's record per the annotate-don't-overwrite rule"),
 ("PS-06","CLAUDE.md","g_t section","Prediction register after migration: 15 CONFIRMED / 9 REFUTED (was 22/2). Seven flips, only three attributable to SDR-001","ACTIVE-CORRECT","NO EDIT","VERIFIED","Already canonical, including the attribution caveat"),
 ("PS-07","docs/canonical/report-publication-consistency-audit-2026-09-08.md","Stale-item table","Conference abstract | 22 confirmed / 2 refuted | 15 / 9 | STALE","ACTIVE-CORRECT","NO EDIT","VERIFIED","Correctly flags the stale value against the canonical target"),
 ("PS-08","publications/active/ipsci-2026/submissions/v3-revision/manuscript-v3.md","Abstract; Empirical Characterisation; Conclusion","fifteen of twenty-four are confirmed and nine refuted","ACTIVE-CORRECT","NO EDIT","VERIFIED","Manuscript already canonical and is protected regardless"),
 ("PS-09","docs/canonical/report-c1-c2/c2/c4/c5/c6/c7/c8-closure and cleanup reports","Integrity-anchor tables","Prediction register UNCHANGED - 24 entries, 22 CONFIRMED / 2 REFUTED","HISTORICAL-SUPERSEDED","NO EDIT","RETAINED","Dated C-series audit reports recording the register state at the moment each task ran, before C-6/C-8 re-resolved it. Correct records of their moment; historical audit reports are excluded from editing"),
 ("PS-10","docs/canonical/approval-report-sdr-001-2026-09-08.md; finding-sdr-001-readiness-audit.md; finding-gt-sensitivity-analysis.md","Integrity anchors","22 CONFIRMED / 2 REFUTED","HISTORICAL-SUPERSEDED","NO EDIT","RETAINED","Same class: pre-C-6 integrity anchors inside dated approval/audit artefacts"),
 ("PS-11","scripts/c6/annotate_register.py","Module docstring, line 18","Top-level totals therefore remain 22 CONFIRMED / 2 REFUTED, which is the correct canonical count until C-8 completes","HISTORICAL-SUPERSEDED (self-scoping)","NO EDIT","RETAINED","Explicitly bounded by 'until C-8 completes'. Accurate for the phase the script belongs to; a C-6 evidence artefact"),
 ("PS-12","docs/canonical/finding-gt-evidence-closure.md","C-6 planning tables","P22 REFUTED; P23, P24 CONFIRMED; 7 candidate flips","HISTORICAL-SUPERSEDED","NO EDIT","RETAINED","Pre-execution planning tables inside the SDR evidence document"),
 ("PS-13","publications/active/journal-1/submissions/v1-initial-submission/manuscript.md","Header banner","prediction-state references","DEFERRED - Journal 1","RECORDED, NOT FIXED","DEFERRED","PS-R5: Journal 1 is out of scope for this branch and has its own task"),
 ("PS-14","docs/canonical/session-log-2026-09-06.md; docs/justification/viva-formalisation-architecture.md; docs/superpowers/plans/2026-09-06-...md","Wind threshold-set findings","25/22, 25/35, 13/22 kn; none matched canonical 22/27","IRRELEVANT","NO EDIT","VERIFIED","Matched only by the numeral 22. These are wind threshold sets, not prediction counts"),
]
with open(HERE/"prediction-state-residue-audit.csv","w",newline="",encoding="utf-8") as fh:
    w=csv.DictWriter(fh,fieldnames=F,quoting=csv.QUOTE_MINIMAL); w.writeheader()
    for r in rows: w.writerow(dict(zip(F,r)))

reg=list(csv.DictReader(open(ROOT/"data/prediction-register.csv")))
cnt=collections.Counter(x["status"] for x in reg); d={x["id"]:x for x in reg}
ver={
 "canonical_register":{"total":len(reg),"CONFIRMED":cnt["CONFIRMED"],"REFUTED":cnt["REFUTED"],
   "refuted_ids":sorted(x["id"] for x in reg if x["status"]=="REFUTED"),
   "P01":d["P01"]["status"],"P16":d["P16"]["status"],
   "P09_actual":d["P09"]["actual"],"P20_actual":d["P20"]["actual"],
   "authority":"data/prediction-register.csv"},
 "sdr001_attributable_flips":["P20","P23","P24"],
 "P09_provenance_chain":"5416 -> 5220 -> 5201 -> 3661 (not a pure g_t effect)",
 "P20_scope_distinction":"P20 registered scope 06:00-17:00 actual 1529; astronomical-daylight RESOLUTION count 455 - different scopes, not interchangeable",
 "active_prediction_state_assertions":[],
 "wind_state_invariant":{"W_CAUTION":21.6,"W_UNSAFE":27.0,"activations":2,"bindings":0,
   "never_fires_reintroduced":False},
 "empirical":{"level2":"5.81% / 4.48%","g_o":"98.71% / 97.66%","g_t":"86.82% / 90.19%",
   "g_r_daylight":"1.48% / 2.70%","g_r_all_hours":"0.20% / 0.26%","daylight_unsafe":"1262 / 455",
   "transitions":"3661 / 3439 / 222 / 26 / 10.36%"},
 "files_changed":["docs/canonical/empirical-findings-2026-09-06.md",
   "docs/canonical/decision-record-empirical-first.md","docs/canonical/session-log-2026-09-06.md"],
 "protected_unchanged":["appendix-c-formalisation.md","manuscript-v3.md","prediction-register.csv",
   "solar-events-daily.csv","all canonical scripts","journal-1 manuscript and section-5-plan"],
 "stop_conditions":{f"PS-R{i}":False for i in (1,2,3,4,6)} | {"PS-R5":"Journal 1 recorded, not edited"},
}
ver["register_matches_expected"]=(len(reg)==24 and cnt["CONFIRMED"]==15 and cnt["REFUTED"]==9
  and d["P01"]["status"]=="REFUTED" and d["P16"]["status"]=="CONFIRMED"
  and d["P09"]["actual"]=="3661" and d["P20"]["actual"]=="1529")
ver["all_clear"]=ver["register_matches_expected"] and not ver["active_prediction_state_assertions"]
(HERE/"prediction-state-closure-verification.json").write_text(json.dumps(ver,indent=2)+"\n")

rep={}
for p in sorted(HERE.glob("*.csv")):
    raw=p.read_text(encoding="utf-8")
    rdr=csv.reader(io.StringIO(raw)); hdr=next(rdr); n=len(hdr)
    bad=[(i+2,len(r)) for i,r in enumerate(rdr) if len(r)!=n]
    dr=len(list(csv.DictReader(io.StringIO(raw)))); df=pd.read_csv(io.StringIO(raw))
    rep[p.name]={"fields":n,"dictreader_rows":dr,"pandas_rows":int(df.shape[0]),
      "malformed":bad,"sha256_16":hashlib.sha256(p.read_bytes()).hexdigest()[:16],
      "parse":"PASS" if not bad and dr==df.shape[0] and n==df.shape[1] else "FAIL"}
(HERE/"parser-test.json").write_text(json.dumps(rep,indent=2)+"\n")
for k,v in rep.items():
    print("%-5s %-38s fields=%d DictReader=%d pandas=%d sha=%s"%(v["parse"],k,v["fields"],v["dictreader_rows"],v["pandas_rows"],v["sha256_16"]))
print("ALL PASS:",all(v["parse"]=="PASS" for v in rep.values()))
print("register matches expected:",ver["register_matches_expected"])
print("classification:",dict(collections.Counter(r[4].split(" (")[0].split(" - ")[0] for r in rows)))
