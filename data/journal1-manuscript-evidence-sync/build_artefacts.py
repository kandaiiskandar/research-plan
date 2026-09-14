#!/usr/bin/env python3
import csv, io, json, pathlib
import pandas as pd
H = pathlib.Path(__file__).resolve().parent

QP = ["manuscript_section","quantity","value","unit","claim_id","source_file","source_field_or_location","status"]
qp = [
 ("8 (Complexity)","retrospective replay scale","43,848","hourly records","E1/E4 context","scripts/condition_comparison.py","PRIMARY record count","CLOSED"),
 ("9 (stub, retained figure)","genuine oscillations","26","events over 5 yr","E4","scripts/hysteresis_analysis.py","oscillation count, PRIMARY","CLOSED"),
 ("9 (stub, retained figure)","oscillation rate","5.2","per year","E4","scripts/hysteresis_analysis.py","derived 26/5yr, PRIMARY","CLOSED"),
 ("10 (stub, retained figure)","retrospective replay scale","43,848","hourly records","E1","scripts/condition_comparison.py","PRIMARY record count","CLOSED"),
 ("10 (stub, retained figure)","Delta_L2 PRIMARY","5.81","% of departure-window hours","E2","scripts/condition_comparison.py","C0-C2 minus C0-C1, PRIMARY departure window","CLOSED"),
 ("10 (stub, retained figure)","Delta_L2 RESOLUTION","4.48","% of departure-window hours","E2","scripts/condition_comparison.py","C0-C2 minus C0-C1, RESOLUTION departure window","CLOSED"),
 ("12 (stub, retained figure)","C0-C2 divergence PRIMARY","48.69","% of departure-window hours","E1","scripts/condition_comparison.py","PRIMARY divergence matrix","CLOSED"),
 ("12 (stub, retained figure)","C0-C1 divergence PRIMARY","42.88","% of departure-window hours","E1","scripts/condition_comparison.py","PRIMARY divergence matrix","CLOSED"),
 ("12 (stub, retained figure)","Delta_L2 PRIMARY","5.81","% of departure-window hours","E2","scripts/condition_comparison.py","48.69 minus 42.88","CLOSED"),
 ("12 (stub, retained figure)","Delta_L2 RESOLUTION","4.48","% of departure-window hours","E2","scripts/condition_comparison.py","RESOLUTION divergence matrix","CLOSED"),
 ("12 (stub, retained figure)","state transitions","3,661","transitions over 5 yr","E4","scripts/hysteresis_analysis.py","PRIMARY total transitions","CLOSED"),
 ("12 (stub, retained figure)","genuine oscillations","26","events (5.2/yr)","E4","scripts/hysteresis_analysis.py","PRIMARY oscillation count","CLOSED"),
 ("12 (stub, retained figure)","hysteresis reduction","10.36","% of non-scheduled transitions","E4","scripts/hysteresis_analysis.py","PRIMARY, 222 -> 199","CLOSED"),
 ("5.2 (Solar provenance)","intra-day simplification bound","0.116 / 0.141","minutes (sunrise/sunset)","M-27","data/solar-citation-closure/noaa-simplification-check.json","experiment A max","CLOSED"),
 ("5.2 (Solar provenance)","leap-denominator bound","0.457 / 0.483","minutes (sunrise/sunset)","M-27","data/solar-citation-closure/noaa-simplification-check.json","experiment B max","CLOSED"),
 ("5.2 (Solar provenance)","USNO agreement, all events","0.92","minutes max","M-27","data/solar/usno-validation-2026-09-08.csv","28 sampled comparisons","CLOSED"),
 ("5.2 (Solar provenance)","USNO agreement, sunrise/sunset","0.75","minutes max","M-27","data/solar/usno-validation-2026-09-08.csv","events g_t reads","CLOSED"),
 ("5.3.2 (Table 1)","g_w thresholds","21.6 / 27.0","knots","M-31","scripts/canonical_figures.py W_CAUTION/W_UNSAFE","MET Cat 1/2 onsets","CLOSED"),
 ("5.3.2 (Table 1)","g_r thresholds","10.0 / 20.0","mm/hr","M-31","scripts/canonical_figures.py R_CAUTION/R_UNSAFE","JPS-DID / MET Ribut Petir","CLOSED"),
 ("5.3.2 (Table 1b)","small-vessel wave thresholds","1.0 / 1.25","metres","M-32","docs/canonical/appendix-c-formalisation.md TABLE IIIb","canonical","CLOSED"),
 ("5.3.2 (Table 1b)","medium-vessel wave thresholds","1.4 / 2.8","metres","M-32","appendix-c TABLE IIIb","canonical (2.8 interpolated)","CLOSED"),
 ("5.3.2 (Table 1b)","big-vessel wave thresholds","1.5 / 3.5","metres","M-32","appendix-c TABLE IIIb","canonical","CLOSED"),
 ("10 (stub)","C1-C3 divergence","0.00","% of hours","E6","scripts/condition_comparison.py","both configurations","CLOSED"),
]
with open(H/"quantitative-provenance.csv","w",newline="",encoding="utf-8") as fh:
    w=csv.DictWriter(fh,fieldnames=QP,quoting=csv.QUOTE_MINIMAL); w.writeheader()
    for r in qp: w.writerow(dict(zip(QP,r)))

CL = ["claim_id","section","before","after","reason","evidence","semantic_change"]
cl = [
 ("M-25","5.2 Definition 5.1 table","r | R>=0 | [0, inf) | Rainfall intensity (mm/hr)","r | R>=0 x K, K={0,1} | ... | rate paired with derived indicator kappa (Def 5.2a)","Contradicted Definition 5.2a in the same section","appendix-c C.2.0.1 / C.2.0.4a","TERMINOLOGY"),
 ("M-07","5.6.2","Layer 3 is specified as a production rule engine; runtime fidelity is not yet demonstrated.","...and its runtime fidelity has been evaluated against this specification (F1-F3, Section 9).","F1-F3 CLOSED PASS at Batch 5","batch5-fidelity-evaluation/fidelity-results.json","STATUS_SYNC"),
 ("M-08","5.6.2","RS(SAFE)/RS(CAUTION) content remains to be implemented and documented in Section 9","...is implemented and specified in the Layer 3 prototype specification; Section 9 presents it","Rules R-CAUTION-001..004 implemented and exercised","governance/ ; rule-activation-summary.csv","STATUS_SYNC"),
 ("M-13","5.6.3","supplementary design rationale (available from the authors)","Layer 3 prototype specification accompanying this work","In-repository specification now exists","layer3-prototype-specification.md","SCOPE_REPAIR"),
 ("M-09","5.7","Section 9 is reserved ...; Section 10 plans ...; These sections are not completed empirical results.","Section 9 presents the implemented prototype ...; evidence is closed except E5 target-hardware, which remains open","Conflated undrafted sections with pending evidence","claim-evidence-matrix.csv","STATUS_SYNC"),
 ("M-10","6.5","Section 10 plans to evaluate implementation fidelity and advisory behaviour...","Implementation fidelity has been evaluated separately from these theorems (F1-F3, Section 9)...","Fidelity already evaluated; also clarifies theorem-vs-fidelity distinction","fidelity-results.json","STATUS_SYNC"),
 ("M-11","7.3 note","L3 is the runtime assumption a future implementation-fidelity test (F1, F2) validates","...that the implementation-fidelity evaluation tests, and which it found upheld with zero observed violations","'future' false","fidelity-results.json","STATUS_SYNC"),
 ("M-12","8","no engine invocation, as when Layer 3 is not yet built","no engine invocation - the configuration in which the participation gate is closed, or Layer 2 is evaluated in isolation","Layer 3 is built","governance/ ; Batch 5","STATUS_SYNC"),
 ("M-15","9 stub purpose","Describe the planned software prototype and, once implemented, its fidelity evaluation","Describe the implemented software prototype and its completed implementation-fidelity evaluation (F1-F3)","Prototype implemented, fidelity evaluated","Batch 5","STATUS_SYNC"),
 ("M-15b","9 stub content","Planned implementation stack targets","Implementation stack","Same reason","Batch 5","TERMINOLOGY"),
 ("M-14","11 stub instruction","Do NOT report fidelity metrics (F1-F3) here - they are deferred to the Layer 3 build","Do NOT report fidelity metrics here. F1-F3 are CLOSED, but are implementation-fidelity not empirical-trace evidence: they belong in Section 9","Instruction contradicted frozen authority and would mis-steer Batch 8B","Batch 5; evaluation-specification","SCOPE_REPAIR"),
 ("E4-a","9 stub figure","Measured on five years of site data under the canonical specification: 26 oscillation events","...under the canonical PRIMARY configuration (E4; no RESOLUTION analogue exists - evaluation-specification Sec 13): 26 oscillation events","Repaired E3/E4 contract requires E4 values identified as PRIMARY","evaluation-specification Sec 13 (2026-09-13)","SCOPE_REPAIR"),
 ("E4-b","12 stub figure","measured on historical replay under the canonical specification: 3,661 state transitions...","...under the canonical PRIMARY configuration (E4; E4_RESOLUTION = NOT_REQUIRED_BY_CURRENT_E3_DESIGN): 3,661 state transitions...","Same","evaluation-specification Sec 13","SCOPE_REPAIR"),
 ("M-35","Abstract","(To be written last)","(To be written last) + UNDRAFTED Batch 8B marker with authoring constraints","No prose existed to bound; must be authored against the evidence matrix","claim-evidence-matrix.csv","BOUNDING"),
 ("M-36/37","1-4 and 9-15","stubs without status markers","UNDRAFTED - reserved for Batch 8B markers naming the evidence matrix and E5 OPEN","Isolate undrafted sections for evidence-grounded authoring","claim-evidence-matrix.csv","BOUNDING"),
 ("M-01..M-06","5.3.3, 6.2-6.5","formal theorem statements and proofs","unchanged","Already correct and bounded","claim-status-matrix P1-P3","NO_CHANGE"),
 ("M-26..M-34","5.2-5.6","kappa/chi, solar, D={m}, reasons, UNSAFE semantics, thresholds, Resolution B, layers","unchanged","Already canonical","appendix-c; canonical scripts","NO_CHANGE"),
 ("M-21","8","complexity bounded, defers to E5","unchanged","Already correctly bounded","evaluation-specification","NO_CHANGE"),
]
with open(H/"claim-change-log.csv","w",newline="",encoding="utf-8") as fh:
    w=csv.DictWriter(fh,fieldnames=CL,quoting=csv.QUOTE_MINIMAL); w.writeheader()
    for r in cl: w.writerow(dict(zip(CL,r)))

rep={}
for p in sorted(H.glob("*.csv")):
    raw=p.read_text(encoding="utf-8"); rdr=csv.reader(io.StringIO(raw)); hdr=next(rdr); n=len(hdr)
    bad=[(i+2,len(r)) for i,r in enumerate(rdr) if len(r)!=n]
    dr=len(list(csv.DictReader(io.StringIO(raw)))); df=pd.read_csv(io.StringIO(raw))
    rep[p.name]={"fields":n,"rows":dr,"pandas_rows":int(df.shape[0]),"malformed":bad,
                 "parse":"PASS" if not bad and dr==df.shape[0] and n==df.shape[1] else "FAIL"}
(H/"parser-test.json").write_text(json.dumps(rep,indent=2)+"\n")
for k,v in rep.items(): print("%-5s %-34s fields=%2d rows=%2d"%(v["parse"],k,v["fields"],v["rows"]))
print("ALL PASS:",all(v["parse"]=="PASS" for v in rep.values()))
