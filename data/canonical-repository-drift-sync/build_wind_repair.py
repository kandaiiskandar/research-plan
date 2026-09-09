#!/usr/bin/env python3
"""Independent wind-assertion closure repair — evidence artefacts."""
import csv, json, hashlib, pathlib, io
import pandas as pd
HERE = pathlib.Path(__file__).resolve().parent
F = ["id","file","locator","claim","classification","action","status","notes"]
rows = [
 ("W-01","docs/canonical/data-provenance.md","Checklist: 'Before citing any figure' item for w","g_w never fires at either cell; state that rather than implying wind is modelled","ACTIVE-CANONICAL-DRIFT","Replaced with: activates twice, binds in neither, at the canonical 21.6 kn boundary; both counts required; activation-vs-binding definitions stated inline","REPAIRED","THE KNOWN RESIDUE. True only under the superseded 22 kn rounding. Sits ~140 lines from the w provenance row repaired in the previous task, in a different section, phrased as an instruction rather than a figure"),
 ("W-02","scripts/openmeteo_raw_download.py","Pre-download planning comment, lines 74-82","sustained wind never exceeds 17.8 kn against a 22 kn CAUTION threshold; finding F-1 (g_w never fires) is a collection artefact if sea-cell wind is higher","ACTIVE-CANONICAL-DRIFT","Annotated with a RESOLVED block: Q1a answered (F-13), wind state corrected again (F-17), canonical 21.6 kn, 2 activations, 0 bindings; instruction not to quote 'never fires' from the comment","REPAIRED","NEW FINDING, not in the brief. Active because it is a maintained canonical collection script whose comment states 22 kn as the comparator and glosses F-1 with the banned phrasing, unmarked. Comment-only edit - no executable line changed"),
 ("W-03","docs/canonical/data-provenance.md","w provenance row, Fit for threshold","At the canonical 21.6 kn boundary g_w activates twice and binds in neither","ACTIVE-CORRECT","NO EDIT","VERIFIED","Repaired in the preceding task; independently re-verified this task"),
 ("W-04","docs/canonical/empirical-findings-2026-09-06.md","F-17 restated finding; 3.4 reporting bullet","g_w activates twice in 43,848 hours and binds in none. Not 'never fires'","ACTIVE-CORRECT","NO EDIT","VERIFIED","Already carries the activation-vs-binding distinction and the explicit prohibition"),
 ("W-05","CLAUDE.md","g_w section","activates 2 times and BINDS in none; do not write 'never fires'; binding share 0.00% is not contradicted by two activations","ACTIVE-CORRECT","NO EDIT","VERIFIED","The canonical guidance was already correct - and was the pattern the previous audit failed to search for"),
 ("W-06","scripts/canonical_figures.py","Reporting trailer","activated twice, decisive never (F-17). Do not report this as 'never fires'","ACTIVE-CORRECT","NO EDIT","VERIFIED","Repaired in the preceding task; byte-identical this task, so no executable change was required"),
 ("W-07","publications/active/ipsci-2026/submissions/v3-revision/manuscript-v3.md","Result 4","g_w never determines a classification, though it is not inactive","ACTIVE-CORRECT","NO EDIT","VERIFIED","Correctly distinguishes binding from activation; manuscript is protected regardless"),
 ("W-08","docs/canonical/appendix-c-formalisation.md","g_w amendment note","At a 22 kn boundary g_w never activates; at 21.6 kn it activates twice","ACTIVE-CORRECT","NO EDIT","VERIFIED","Explicitly contrastive and historical; Appendix C is protected regardless"),
 ("W-09","docs/canonical/decision-record-empirical-first.md","Section 1, Finding","g_w never fires ... thresholds are 22 kn and 27 kn. Zero activations","HISTORICAL-SUPERSEDED","NO EDIT","RETAINED","Carries the HISTORICAL block added in the g_t closure repair directly beneath it; the decision was taken on this basis"),
 ("W-10","docs/canonical/empirical-findings-2026-09-06.md","F-1 as-first-measured block; F-13 narrative","Zero activations; at the then-specified 22 kn boundary g_w still never fired","HISTORICAL-SUPERSEDED","NO EDIT","RETAINED","Block-marked by the F-17 restatement banner and by then-specified / as first measured framing"),
 ("W-11","docs/canonical/session-log-2026-09-06.md","F-1 and F-13 rows","g_w never fires ... against a 22 kn threshold; still never fires. Threshold 22.0","HISTORICAL-SUPERSEDED","NO EDIT","RETAINED","Dated session log; each row names the 22 kn threshold inline, which self-marks it"),
 ("W-12","data/c8/pre-migration-scripts/canonical_figures.py","Frozen trailer","g_w never binds in either configuration ... against a 22 kn threshold","HISTORICAL-SUPERSEDED","NO EDIT","RETAINED","Frozen pre-migration copy; must not be edited"),
 ("W-13","docs/canonical/finding-met-hydrodynamic-gap.md","Section 2 heading","MET criteria never fire at this site","IRRELEVANT","NO EDIT","VERIFIED","Concerns MET WAVE criteria at 3.50 m with a genuine 0 hours exceeded - not the wind assertion class"),
 ("W-14","docs/justification/unified-governance.md","Comparison tables","CAUTION mode never ...; CAUTION never activates","IRRELEVANT","NO EDIT","VERIFIED","Concerns the CAUTION governance mode in a hypothetical unified-governance design, not g_w"),
 ("W-15","docs/canonical/report-publication-consistency-audit-continuation-2026-09-09.md","SC-1 assessment","does not activate SC-1","IRRELEVANT","NO EDIT","VERIFIED","Different sense of activate - a stop condition, not a classifier component"),
 ("W-16","docs/canonical/report-canonical-repository-drift-sync-2026-09-09.md; report-conference-reviewer-audit-2026-09-09.md","Findings sections","quotes the g_w never fires defect; g_r storm route never fires","HISTORICAL-SUPERSEDED / IRRELEVANT","NO EDIT","RETAINED","Audit reports recording the defect - must not be rewritten to hide it. The g_r occurrences are a different component"),
 ("W-17","docs/canonical/empirical-findings-2026-09-06.md","Status line, head of document","All 24 pre-registered predictions resolved - 22 confirmed, 2 refuted","UNRELATED FINDING (prediction-state drift, not wind)","RECORDED, NOT FIXED","DEFERRED","WIND-R6: an unrelated contradiction found during the search. Canonical register is 15 CONFIRMED / 9 REFUTED. Does not prevent determining the wind assertion, so this task was not expanded. Recommend a bounded follow-up"),
]
with open(HERE/"wind-assertion-residue-audit.csv","w",newline="",encoding="utf-8") as fh:
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
    print("%-5s %-34s fields=%d DictReader=%d pandas=%d sha=%s"%(v["parse"],k,v["fields"],v["dictreader_rows"],v["pandas_rows"],v["sha256_16"]))
print("ALL PASS:",all(v["parse"]=="PASS" for v in rep.values()))
from collections import Counter
print("\nclassification counts:",dict(Counter(r[4].split(" /")[0].split(" (")[0] for r in rows)))
