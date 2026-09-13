#!/usr/bin/env python3
"""E3/E4 resolution-sensitivity authority micro-repair — evidence artefacts."""
import csv, json, hashlib, pathlib, io
import pandas as pd
H = pathlib.Path(__file__).resolve().parent

SUP = ["file","location","historical_assertion","current_status","superseded_by"]
sup = [
 ("data/journal1-post-fidelity-plan/report.md","line 42, claim-status summary table, E3 row",
  "Dual-configuration values for E1, E2, E4, E6 from canonical_figures.py",
  "SUPERSEDED","E3/E4 resolution-sensitivity authority micro-repair"),
 ("data/journal1-post-fidelity-plan/replay-requirement-assessment.md","line 54, Evidence already captured",
  "Dual-configuration values exist for E1, E2, E4, E6 from canonical scripts.",
  "SUPERSEDED","E3/E4 resolution-sensitivity authority micro-repair"),
 ("data/journal1-post-fidelity-plan/evaluation-dependency-graph.md","line 175, dependency-graph footnote",
  "* = reporting dependency only (E3 reports dual-config values for E1, E2, E4, E6)",
  "SUPERSEDED","E3/E4 resolution-sensitivity authority micro-repair"),
 ("data/journal1-evaluation-specification/evaluation-specification.csv","row E3, column question_or_claim",
  "Resolution sensitivity: report every empirical figure under PRIMARY and RESOLUTION",
  "SUPERSEDED","E3/E4 resolution-sensitivity authority micro-repair"),
 ("data/journal1-post-fidelity-plan/claim-status-matrix.csv","row E3 (REPAIRED, not historical)",
  "required_evidence: 'Both configurations computed and reported for every empirical value in E1 E2 E4 E6.'; "
  "next_action: 'None - dual-configuration values exist for all empirical claims.'",
  "REPAIRED IN PLACE","E3/E4 resolution-sensitivity authority micro-repair"),
 ("publications/active/journal-1/evaluation-specification.md","section 13 global contract (REPAIRED, not historical)",
  "Every empirical figure in Journal 1 must be reported under both configurations.",
  "REPAIRED IN PLACE","E3/E4 resolution-sensitivity authority micro-repair"),
]
with open(H/"historical-supersession-record.csv","w",newline="",encoding="utf-8") as fh:
    w=csv.DictWriter(fh,fieldnames=SUP,quoting=csv.QUOTE_MINIMAL); w.writeheader()
    for r in sup: w.writerow(dict(zip(SUP,r)))

rep={}
for p in sorted(H.glob("*.csv")):
    raw=p.read_text(encoding="utf-8"); rdr=csv.reader(io.StringIO(raw)); hdr=next(rdr); n=len(hdr)
    bad=[(i+2,len(r)) for i,r in enumerate(rdr) if len(r)!=n]
    dr=len(list(csv.DictReader(io.StringIO(raw)))); df=pd.read_csv(io.StringIO(raw))
    rep[p.name]={"fields":n,"dictreader_rows":dr,"pandas_rows":int(df.shape[0]),"malformed":bad,
      "parse":"PASS" if not bad and dr==df.shape[0] and n==df.shape[1] else "FAIL"}
(H/"parser-test.json").write_text(json.dumps(rep,indent=2)+"\n")
for k,v in rep.items():
    print("%-5s %-38s fields=%d rows=%d"%(v["parse"],k,v["fields"],v["dictreader_rows"]))
print("ALL PASS:",all(v["parse"]=="PASS" for v in rep.values()))
