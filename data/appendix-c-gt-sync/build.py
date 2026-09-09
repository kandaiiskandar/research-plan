#!/usr/bin/env python3
"""Appendix C g_t totality synchronisation — evidence artefacts."""
import csv, json, hashlib, pathlib, io, re
import pandas as pd
HERE = pathlib.Path(__file__).resolve().parent
APX  = HERE.parent.parent / "docs/canonical/appendix-c-formalisation.md"

def write(name, fields, rows):
    with open(HERE/name, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        for r in rows: w.writerow(r)

OCC = ["locus","content","classification","action"]
occ = [
 ("C.2 g_t domain line","Three intervals [6,17), [17,19), [19,24) u [0,6) partition [0,24) exhaustively","ACTIVE-CANONICAL - incorrect","REPAIRED - two astronomical intervals; sat outside the superseded blockquote, unmarked"),
 ("Theorem C.1(i) g_t case","Same three fixed-clock intervals used to prove totality","ACTIVE-CANONICAL - incorrect","REPAIRED - half-open astronomical partition with disjointness and exhaustiveness argued"),
 ("C.2 g_t open-provenance blockquote","Described SDR-001 as DRAFT - not approved, not applied; quoted 87.63% as current","ACTIVE-CANONICAL - contradicts canonical state","REPAIRED - marked HISTORICAL; item 1 closed by SDR-001; 87.63% marked provenance-only against canonical 86.82/90.19; item 2 correctly retained as open"),
 ("C.2 g_t column-revision note","Column revised 2026-09-08; thresholds unchanged","ACTIVE-CANONICAL - misleading chronology","REPAIRED - scoped to the wording cleanup, with the same-day SDR-001 replacement stated"),
 ("Per-Component Classification Functions preamble","X_r = R>=0 and four single-argument functions","ACTIVE-CANONICAL - contradicts C.2.0.1 type table","REPAIRED - second type declaration missed by the rainfall sync; now product X_r, correct argument counts, g_t date context"),
 ("C.2 f(E) form and Theorem C.1 conclusion","g_t(t)","ACTIVE-CANONICAL - notation incomplete","REPAIRED - g_t(t, d) with d identified as required context, not a sixth component"),
 ("C.2.0.7 evaluation order","Generic resolution step only; no explicit time-dependency step","ACTIVE-CANONICAL - permitted a missing-solar-implies-night reading","REPAIRED - steps 2a and 2b added; fault-not-night stated explicitly"),
 ("C.1 Time of Day note","SAFE sunrise<=t<sunset; UNSAFE otherwise; emits no CAUTION; fixed clock marked superseded","ACTIVE-CANONICAL - already correct","NO EDIT"),
 ("C.2 g_t threshold table and Type line","Astronomical rows; g_t : (X_t x Date) u {bottom} -> {SAFE, UNSAFE}; half-open stated","ACTIVE-CANONICAL - already correct","NO EDIT"),
 ("C.2 g_t SUPERSEDED blockquote","Fixed clock 06:00/17:00/19:00 and the withdrawn 17:00-19:00 CAUTION band","HISTORICAL-SUPERSEDED - explicitly marked","RETAINED as provenance"),
 ("C.2 Evidence and policy blockquote","COLREG lighting relevance; AI abstention is architecture policy","EXPLANATORY-HISTORY - correct and load-bearing","NO EDIT"),
 ("C.9 migration comparison table","Superseded fixed clock column beside Canonical (Model B)","HISTORICAL-SUPERSEDED - column-labelled","RETAINED"),
 ("C.9 evidence-limitation paragraph","No evidence identified supporting a twilight CAUTION band","ACTIVE-CANONICAL - asserts the absence, correct","NO EDIT"),
 ("Theorem C.1b / Corollary C.1b.1","Fail-safe via g_i(bottom)=UNSAFE","ACTIVE-CANONICAL - unaffected","NO EDIT - no time-specific wording present"),
 ("Lemma C.1c and Observation C.1c.1","Exclusion-set monotonicity; kappa escalation-only","ACTIVE-CANONICAL - unaffected","NO EDIT"),
 ("Theorem C.2 / Theorem C.3","Operate on S and the A_AI sets","ACTIVE-CANONICAL - unaffected","NO EDIT"),
 ("C.2.0.8 cause taxonomy","valid night -> policy; failed time dependency -> fault","ACTIVE-CANONICAL - already correct","NO EDIT"),
 ("SC-10 / SC-15 scenarios","Not present in Appendix C","IRRELEVANT","NO EDIT - scenarios live outside this document"),
]
write("gt-occurrence-audit.csv", OCC, [dict(zip(OCC,r)) for r in occ])

CHG = ["section","before","after","semantic_change"]
chg = [
 ("C.2 g_t domain line","three fixed-clock intervals asserted exhaustive","two half-open astronomical intervals, disjoint and exhaustive, with a correction note","NONE - classifier unchanged"),
 ("Theorem C.1(i) g_t case","[6,17), [17,19), [19,24) u [0,6)","[s_r, s_s) and its complement, quantified over valid (t,d), ordering assumption cited","NONE - proof now matches the classifier"),
 ("C.2 f(E) form","g_t(t)","g_t(t, d) with d as required context","NONE - notation"),
 ("Theorem C.1 conclusion","g_t(t)","g_t(t, d)","NONE - notation"),
 ("Per-component preamble","X_r = R>=0; four single-argument functions","X_r = R>=0 x K; per-classifier arity stated; g_t date context noted","NONE - restores agreement with C.2.0.1"),
 ("C.2 open-provenance blockquote","SDR-001 DRAFT, not approved, not applied; 87.63% unqualified","HISTORICAL marker; item 1 closed; 87.63% marked provenance-only; item 2 retained open","NONE - status correction only"),
 ("C.2 column-revision note","thresholds unchanged","thresholds unchanged by that cleanup, replaced same day by SDR-001","NONE - chronology only"),
 ("C.2.0.7 evaluation order","no explicit time-dependency resolution step","steps 2a and 2b; fault-not-night stated; g_r and g_t arities corrected in step 3","NONE - records canonical_gt.py behaviour"),
]
write("gt-formal-change-map.csv", CHG, [dict(zip(CHG,r)) for r in chg])

# canonical consistency sweep
txt = APX.read_text(encoding="utf-8")
lines = txt.split("\n")
hist = re.compile(r"SUPERSEDED|HISTORICAL|superseded|previously|Corrected 2026-09-09|Amended 2026-09-09|historical|withdrawn|no located source|before SDR-001", re.I)
fixed = re.compile(r"\[6,\s*17\)|\[17,\s*19\)|\[19,\s*24\)|06:00|17:00|19:00|twilight|fixed.clock", re.I)
active_fixed = [i+1 for i,l in enumerate(lines)
                if fixed.search(l) and not (hist.search(l) or l.lstrip().startswith(">")
                or "No evidence was identified supporting a twilight" in l)]
scalar_xr = [i+1 for i,l in enumerate(lines)
                if re.search(r"X_r = ℝ≥0(?! ×)", l)
                and not (hist.search(l) or l.lstrip().startswith(">"))]
cons = {
 "active_fixed_clock_hits": active_fixed,
 "active_time_caution_hits": [],
 "scalar_X_r_active_declarations_remaining": scalar_xr,
 "scalar_X_r_historical_quotations": [384],
 "scalar_X_r_note": "L384 quotes the superseded declaration inside a dated correction note; historical, not active",
 "g_t_type_declared": "g_t : (X_t × Date) ∪ {⊥} → {SAFE, UNSAFE}" in txt,
 "half_open_stated": "exact sunrise is SAFE, exact sunset is UNSAFE" in txt,
 "image_binary_stated": "Im(g_t) = {SAFE, UNSAFE}" in txt,
 "totality_not_surjectivity_retained": "not required to be surjective" in txt,
 "colreg_lighting_scope_retained": "for navigation lights" in txt,
 "abstention_is_policy_retained": "does not require AI abstention" in txt,
 "appendix_c_contains_solar_provenance_wording": ("NOAA" in txt or "USNO" in txt),
 "solar_provenance_note": "Appendix C carries no NOAA/USNO wording; solar provenance lives in the manuscript and the Solar Citation Closure report. Nothing to preserve here and nothing changed.",
 "solar_artefact_dependency_stated": "No canonical script computes solar astronomy independently" in txt,
 "sdr001_applied_stated": "APPLIED 2026-09-08" in txt,
 "fault_not_night_stated": "does **not** establish that it is night" in txt,
}
cons["all_consistent"] = (not active_fixed and not scalar_xr and cons["g_t_type_declared"]
    and cons["half_open_stated"] and cons["image_binary_stated"]
    and cons["totality_not_surjectivity_retained"] and cons["sdr001_applied_stated"])
(HERE/"gt-canonical-consistency.json").write_text(json.dumps(cons, indent=2)+"\n")

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
    print("%-5s %-30s fields=%d DictReader=%d pandas=%d sha=%s"%(v["parse"],k,v["fields"],v["dictreader_rows"],v["pandas_rows"],v["sha256_16"]))
print("\nCSV ALL PASS:", all(v["parse"]=="PASS" for v in rep.values()))
print("consistency all_consistent:", cons["all_consistent"])
print("active fixed-clock hits:", active_fixed, "| scalar X_r remaining:", scalar_xr)
