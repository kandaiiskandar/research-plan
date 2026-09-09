#!/usr/bin/env python3
"""Appendix C rainfall signature synchronisation — evidence artefacts."""
import csv, json, hashlib, pathlib, io
import pandas as pd
HERE = pathlib.Path(__file__).resolve().parent

def write(name, fields, rows):
    with open(HERE/name, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        for r in rows: w.writerow(r)

IMP = ["file","line","form","reads_rate","reads_wmo","storm_codes","rate_in_dropna","wmo_in_dropna","kappa_on_missing_code"]
imp = [
 ("scripts/canonical_figures.py","127-128","(precip > R_UNSAFE) | wmo.isin([95,96,99])","YES","YES","95;96;99","YES","NO","0 (pandas isin on NaN is False)"),
 ("scripts/condition_comparison.py","161-162","(precip > R_UNSAFE) | wmo.isin([95,96,99])","YES","YES","95;96;99","YES","NO","0 (pandas isin on NaN is False)"),
 ("scripts/diagnostic_binding.py","101-102","(precip > R_UNSAFE) | wmo.isin([95,96,99])","YES","YES","95;96;99","YES","NO","0 (pandas isin on NaN is False)"),
 ("scripts/hysteresis_analysis.py","111-112, 122, 148-149","(precip > R_UNSAFE) | wmo.isin([95,96,99]); storm checked before hysteresis","YES","YES","95;96;99","YES","NO","0 (pandas isin on NaN is False)"),
 ("scripts/historical_replay.py","79-94","def g_r(precip_mm_hr, wmo_code); precip > R_UNSAFE or wmo_code in (95,96,99)","YES","YES","95;96;99","YES","NO","0 (Python in on NaN is False)"),
 ("scripts/compare_v1_v2.py","44","def g_r(p, c); (p > R_UNSAFE) | np.isin(c, [95,96,99])","YES","YES","95;96;99","NO (v1/v2 compare path)","NO","0 (numpy isin on NaN is False)"),
 ("scripts/threshold_decision.py","63-64","(precip > R_UNSAFE) | wmo.isin([95,96,99])","YES","YES","95;96;99","NO (wave only)","NO","0 (pandas isin on NaN is False)"),
 ("scripts/c5/three_stage_hysteresis.py","146-147, 156, 262-263","(precip > R_UNSAFE) | wmo.isin([95,96,99]); storm overrides hysteresis","YES","YES","95;96;99","YES","NO","0 (pandas isin on NaN is False)"),
 ("scripts/c6/reresolve_predictions.py","124-125","(precip > R_UNSAFE) | wmo.isin([95,96,99])","YES","YES","95;96;99","YES","NO","0 (pandas isin on NaN is False)"),
]
write("gr-implementation-audit.csv", IMP, [dict(zip(IMP,r)) for r in imp])

OCC = ["path","locus","classification","action"]
occ = [
 ("docs/canonical/appendix-c-formalisation.md","C.2.0.1 type table; C.2.0.2; new C.2.0.4a; C.2 g_r block; C.2 domain line; secondary-route prose; Theorem C.1(i); C.1 conclusion; C.1b note; Observation C.1c.1; C.2.0.8 trace clause","CANONICAL - requires synchronisation","SYNCHRONISED in this task"),
 ("publications/active/ipsci-2026/submissions/v3-revision/manuscript-v3.md","classifier signature; Theorem 1; Algorithm 1; domain declaration; resolution wording; Result 4","ACTIVE PUBLICATION - already correct","NO EDIT - verified to agree with implementation"),
 ("scripts/canonical_figures.py + 8 further canonical scripts","g_r evaluation sites","IMPLEMENTATION - canonical executable semantics","NO EDIT - authoritative source of the semantics"),
 ("data/c8/pre-migration-scripts/*.py","frozen pre-migration copies","HISTORICAL - preserve","NO EDIT"),
 ("publications/active/ipsci-2026/submissions/v2-post-review/manuscript-v2.5-submitted.md","categorical g_r(r) over none/light/moderate/heavy/storm","HISTORICAL - submitted record","NO EDIT"),
 ("publications/active/ipsci-2026/supervisor-feedback-response.md","categorical S_r <- g_r(r)","HISTORICAL - preserve","NO EDIT"),
 ("docs/canonical/session-log-2026-09-06.md","f(E) five-term line with scalar g_r(r)","HISTORICAL - dated session record","NO EDIT"),
 ("docs/superpowers/plans/2026-09-06-formal-model-and-evaluation-realignment.md","scalar g_r references","HISTORICAL - plan record","NO EDIT"),
 ("docs/canonical/report-conference-reviewer-audit-2026-09-09.md","records the scalar-vs-implementation defect","HISTORICAL - must NOT be rewritten to imply kappa was always typed","NO EDIT"),
 ("publications/active/journal-1/submissions/v1-initial-submission/manuscript.md","lines 187, 226, 424, 426 scalar g_r(r)","STALE DOCUMENTATION - repair separately","DEFERRED - Journal 1 work is out of scope"),
 ("publications/active/journal-1/section-5-plan.md","superseded categorical g_r bands","STALE DOCUMENTATION - repair separately","DEFERRED - Journal 1 out of scope"),
 ("docs/justification/formal-model.md","line 41 S_r = g_r(r)","STALE DOCUMENTATION - repair separately","DEFERRED - recorded as drift"),
 ("docs/reference/explainer-per-component-classification-functions.md","scalar rainfall classifier description","STALE DOCUMENTATION - repair separately","DEFERRED - recorded as drift"),
 ("docs/canonical/data-provenance.md","rainfall/WMO provenance wording","STALE DOCUMENTATION - repair separately","DEFERRED - recorded as drift"),
 ("docs/implementation/dataset-label-derivation.md","rainfall label derivation","IRRELEVANT - derives Layer 3 training labels, not classifier thresholds","NO EDIT"),
 ("docs/canonical/appendix-c-formalisation.md","Theorem C.1 g_t case still lists the superseded fixed-clock intervals [6,17),[17,19),[19,24)u[0,6)","CANONICAL - unrelated drift found in passing","NOT FIXED - out of scope for a rainfall repair; recorded for a bounded g_t follow-up"),
]
write("gr-occurrence-audit.csv", OCC, [dict(zip(OCC,r)) for r in occ])

CHG = ["section","before","after","semantic_change"]
chg = [
 ("C.2.0.1 type table","X_r = R>=0","X_r = R>=0 x K with K = {0,1}","NONE - type declaration only"),
 ("C.2.0.2 what bottom attaches to","o tuple rule only","adds the rainfall pair rule: rate required, kappa derived and non-faulting","NONE - documents existing behaviour"),
 ("C.2.0.4a (NEW)","did not exist","chi mapping from raw WMO code to kappa; kappa classified as category C derived feature; D unchanged; fail-open recorded without overclaim","NONE - new documentation of existing behaviour"),
 ("C.2 g_r block","g_r : R>=0 -> S, three rate cases","g_r : R>=0 x K -> S, four cases with kappa=1 first; thresholds unchanged","NONE - thresholds and outputs identical"),
 ("C.2 g_r domain line","three intervals partition R>=0 exhaustively","product domain covered; rate partition alone is no longer the whole domain","NONE - corrects a false exhaustiveness claim"),
 ("C.2 secondary-route prose","route described in prose as formally part of the specification","route carried by kappa and chi; prose retained and cross-referenced","NONE"),
 ("Theorem C.1(i) g_r case","rate partition asserted exhaustive over the g_r domain","two-case proof over kappa in {0,1}, each total","NONE - proof now covers the true domain"),
 ("Theorem C.1 conclusion + C.2 f(E) form","g_r(r)","g_r(r, kappa)","NONE - notation"),
 ("Theorem C.1b proof","no note on structured components","note that Y absorbs the product; y_r = bottom denotes rate failure only; chi never yields bottom","NONE - preserves Corollary C.1b.1 scope exactly"),
 ("Observation C.1c.1 (NEW)","did not exist","g_r(r,0) precedes-or-equals g_r(r,1); kappa escalation-only; bound direction stated; explicitly not a physical claim","NONE - derived from the definition"),
 ("C.2.0.8 trace clause","resolved reading and applicable band","adds which route applied for r; states kappa satisfies existing hazard label; no new reason category","NONE - reasons() contract untouched"),
]
write("formal-change-map.csv", CHG, [dict(zip(CHG,r)) for r in chg])

# parser test: DictReader AND pandas, per requirement 25
rep={}
for p in sorted(HERE.glob("*.csv")):
    raw=p.read_text(encoding="utf-8")
    rdr=csv.reader(io.StringIO(raw)); hdr=next(rdr); n=len(hdr)
    bad=[(i+2,len(r)) for i,r in enumerate(rdr) if len(r)!=n]
    dr=len(list(csv.DictReader(io.StringIO(raw))))
    df=pd.read_csv(io.StringIO(raw))
    rep[p.name]={"fields":n,"dictreader_rows":dr,"pandas_rows":int(df.shape[0]),
                 "pandas_cols":int(df.shape[1]),"malformed":bad,
                 "sha256_16":hashlib.sha256(p.read_bytes()).hexdigest()[:16],
                 "parse":"PASS" if not bad and dr==df.shape[0] and n==df.shape[1] else "FAIL"}
(HERE/"parser-test.json").write_text(json.dumps(rep,indent=2)+"\n")
for k,v in rep.items():
    print("%-5s %-30s fields=%d DictReader=%d pandas=%d sha=%s"%(
        v["parse"],k,v["fields"],v["dictreader_rows"],v["pandas_rows"],v["sha256_16"]))
print("\nALL PASS:", all(v["parse"]=="PASS" for v in rep.values()))
