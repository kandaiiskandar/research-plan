#!/usr/bin/env python3
import csv, json, hashlib, pathlib, io
import pandas as pd
HERE = pathlib.Path(__file__).resolve().parent
F = ["file","line_or_locator","matched_text","class","action","notes"]
rows = [
 ("docs/canonical/appendix-c-formalisation.md","C.1 Time of Day Classification Note (was L42)",
  "The thresholds 06:00 / 17:00 / 19:00 are unchanged.","ACTIVE-CANONICAL (Class A chronology)",
  "REPAIRED - three-step chronology stated: cleanup was wording-only; SDR-001 superseded the thresholds later the same day; fixed clock is not canonical",
  "Missed by the previous sweep: the line-level heuristic saw the word 'previously' (referring to the row wording) and marked the whole line historical"),
 ("docs/canonical/appendix-c-formalisation.md","C.1 governance-response paragraph (was L44)",
  "the boundaries themselves have no located source","ACTIVE-CANONICAL (Class A chronology)",
  "REPAIRED - scoped to the superseded values; COLREG 20(b) supplies the canonical boundary for navigation lights; what has no source is the POLICY, not the boundary",
  "Equivalent residue in the same note, found by the Class A audit rather than named in the brief"),
 ("docs/canonical/appendix-c-formalisation.md","(D1) t not in D (was L278)",
  "g_t determines 87.63% of all non-SAFE classifications at the study site (F-7)","ACTIVE-CANONICAL (Class B superseded metric)",
  "REPAIRED - D1 restated structurally with no empirical dependency; superseded figure removed from the argument",
  "Wrong twice: the figure is fixed-clock provenance, and the reasoning was inverted - a structural constraint cannot rest on a site-specific binding share"),
 ("docs/canonical/appendix-c-formalisation.md","(D1) correction note",
  "previously justified the constraint empirically - 87.63%","HISTORICAL-SUPERSEDED",
  "RETAINED","Dated correction note quoting the superseded figure; canonical 86.82 PRIMARY / 90.19 RESOLUTION given as context only, explicitly carrying no part of the argument"),
 ("docs/canonical/appendix-c-formalisation.md","C.2 g_t open-provenance blockquote",
  "The 87.63% figure quoted here was computed under the superseded fixed clock and is provenance only","HISTORICAL-SUPERSEDED",
  "RETAINED","Repaired in the preceding task; already correctly labelled provenance-only against canonical 86.82 / 90.19"),
 ("docs/canonical/appendix-c-formalisation.md","C.2 SUPERSEDED blockquote; C.9 migration table; C.1 superseded note",
  "fixed clock 06:00 / 17:00 / 19:00 and the withdrawn 17:00-19:00 CAUTION band","HISTORICAL-SUPERSEDED",
  "RETAINED","Legitimate provenance, unmistakably labelled; not deleted to obtain zero textual hits"),
 ("docs/canonical/appendix-c-formalisation.md","C.9 evidence-limitation paragraph",
  "No evidence was identified supporting a twilight CAUTION band","IRRELEVANT",
  "NO EDIT","Asserts the absence of a twilight band; correct active canonical text"),
]
with open(HERE/"residue-occurrence-audit.csv","w",newline="",encoding="utf-8") as fh:
    w=csv.DictWriter(fh,fieldnames=F,quoting=csv.QUOTE_MINIMAL); w.writeheader()
    for r in rows: w.writerow(dict(zip(F,r)))
rep={}
for p in sorted(HERE.glob("*.csv")):
    raw=p.read_text(encoding="utf-8")
    rdr=csv.reader(io.StringIO(raw)); hdr=next(rdr); n=len(hdr)
    bad=[(i+2,len(r)) for i,r in enumerate(rdr) if len(r)!=n]
    dr=len(list(csv.DictReader(io.StringIO(raw)))); df=pd.read_csv(io.StringIO(raw))
    rep[p.name]={"fields":n,"dictreader_rows":dr,"pandas_rows":int(df.shape[0]),
      "pandas_cols":int(df.shape[1]),"malformed":bad,
      "sha256_16":hashlib.sha256(p.read_bytes()).hexdigest()[:16],
      "parse":"PASS" if not bad and dr==df.shape[0] and n==df.shape[1] else "FAIL"}
(HERE/"parser-test.json").write_text(json.dumps(rep,indent=2)+"\n")
for k,v in rep.items():
    print("%-5s %-30s fields=%d DictReader=%d pandas=%d sha=%s"%(v["parse"],k,v["fields"],v["dictreader_rows"],v["pandas_rows"],v["sha256_16"]))
print("ALL PASS:",all(v["parse"]=="PASS" for v in rep.values()))
