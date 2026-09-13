#!/usr/bin/env python3
import csv, io, json, pathlib
import pandas as pd
H = pathlib.Path(__file__).resolve().parent

INV = ["claim_id","manuscript_section","line_or_location","current_claim","claim_type",
       "evidence_status","authoritative_evidence","evidence_value","revision_required",
       "revision_reason","proposed_bounded_claim"]
inv = [
 # ---------- FORMAL (P1-P4) ----------
 ("M-01","5.3.3 / 6.2","L244, L416-440","Theorem 5.1/6.1 Totality of f: f(E) defined, returns exactly one element","FORMAL","CLOSED","claim-status-matrix P1; appendix-c Theorem C.1/C.1b","P1 CLOSED","NO","Already correct; two-argument g_r and g_o totality cases present; operational extension stated","(unchanged)"),
 ("M-02","6.3","L448-486","Theorem 6.2 Monotonicity + Corollaries 6.2/6.3","FORMAL","CLOSED","claim-status-matrix P2; appendix-c Theorem C.2","P2 CLOSED","NO","Exhaustive three-case proof; strict containment stated","(unchanged)"),
 ("M-03","6.4","L492-525","Theorem 6.3 Safety Dominance, AI(E) subset A_AI(f(E)), by construction under A1-A4","FORMAL","CLOSED","claim-status-matrix P3; appendix-c Theorem C.3","P3 CLOSED","NO","Bounded; assumptions explicit","(unchanged)"),
 ("M-04","6.5","L541-543","Composite guarantee + 'what it does not establish'","FORMAL","CLOSED","claim-status-matrix P1-P3","configured admissible scope","NO","Repaired in the semantic closure repair; epistemic boundary explicit","(unchanged)"),
 ("M-05","5.4.3 / 6.x","Def 5.8, Table 2","A_AI containment chain SAFE superset CAUTION superset UNSAFE = empty","FORMAL","CLOSED","appendix-c C.4","P2 CLOSED","NO","Correct","(unchanged)"),
 ("M-06","(absent)","--","Proposition J1-P1: C1 = C3 at admissible-set level","FORMAL","CLOSED","claim-status-matrix P4; evaluation-specification Section 4/6","C1 = C3 by mapping-literal identity","OPEN-8B","P4 has no manuscript locus; Section 6 does not yet state Proposition J1-P1","Belongs in Batch 8B when Section 6 gains the proposition, or Section 2/4 relates work"),
 # ---------- IMPLEMENTATION FIDELITY (F1-F3) ----------
 ("M-07","5.6.2","L356","'Layer 3 is specified as a production rule engine; runtime fidelity is not yet demonstrated.'","IMPLEMENTATION_FIDELITY","SUPERSEDED","Batch 5 fidelity-results.json; reporting-repair.json","F1/F2/F3 PASS, 0 violations, 0 mismatches","YES","False since Batch 5. Layer 3 is built and fidelity evaluated","Runtime fidelity has been evaluated on the interface-contract state space (F1-F3, Batch 5): 292 episodes, 454 advisory records, zero violations and zero rule-set mismatches"),
 ("M-08","5.6.2","L360","'The actual content of RS(SAFE) and RS(CAUTION) ... remains to be implemented and documented in Section 9'","IMPLEMENTATION_FIDELITY","SUPERSEDED","governance/ modules; layer3-prototype-specification.md; Batch 5 rule-activation-summary.csv","R-CAUTION-001..004 implemented and exercised","YES","Rules exist and were exercised; Section 9 remains undrafted","Rule sets are implemented and specified in layer3-prototype-specification.md; Section 9 (undrafted) will present them"),
 ("M-09","5.7","L394","'Section 9 is reserved for the prototype and complete rule sets; Section 10 plans the comparative evaluation. These sections are not completed empirical results.'","IMPLEMENTATION_FIDELITY","SUPERSEDED","Batch 5; E1-E4/E6 closed evidence","F1-F3 and E1-E4,E6 CLOSED","YES","Evidence is closed; only the manuscript sections are undrafted. Current wording implies the evidence is pending","Distinguish closed evidence from undrafted sections; note E5 target-hardware remains open"),
 ("M-10","6.5","L545","'Section 10 plans to evaluate implementation fidelity and advisory behaviour in empirical test scenarios'","IMPLEMENTATION_FIDELITY","SUPERSEDED","Batch 5 report.md","F1-F3 CLOSED PASS","YES","Fidelity already evaluated","Implementation fidelity has been evaluated (F1-F3); the comparative empirical-trace results are E1-E4 and E6"),
 ("M-11","7.3 note","L649","'L3 is the runtime assumption a future implementation-fidelity test (F1, F2 - see §10 ...)'","IMPLEMENTATION_FIDELITY","SUPERSEDED","Batch 5 fidelity-results.json","F1/F2 PASS","YES","'future' is false","Refer to F1/F2 as evaluated rather than future"),
 ("M-12","8","L718","'no engine invocation, as when Layer 3 is not yet built'","IMPLEMENTATION_FIDELITY","SUPERSEDED","governance/ modules; Batch 5","Layer 3 built","YES","False since Batch 3/5","Refer to the classification-and-governance-only pipeline as a configuration, not as Layer 3 being unbuilt"),
 ("M-13","5.6.3","L366","'Full justification ... provided in the supplementary design rationale (available from the authors)'","DESIGN_INTERPRETATION","SUPERSEDED","layer3-prototype-specification.md","In-repository specification exists","YES","Points to an unavailable supplement when a repository specification now exists","Cite layer3-prototype-specification.md"),
 ("M-14","11 stub","L801","'Do NOT report fidelity metrics (F1-F3) here - they are deferred to the Layer 3 build (see §9)'","IMPLEMENTATION_FIDELITY","SUPERSEDED","Batch 5","F1-F3 CLOSED","YES","A drafting instruction that contradicts frozen authority; would mis-steer Batch 8B","Replace with instruction reflecting closed F1-F3 and their correct section placement"),
 ("M-15","9 stub","L738","'Describe the planned software prototype and, once implemented, its fidelity evaluation'","IMPLEMENTATION_FIDELITY","SUPERSEDED","Batch 5; governance/","Prototype implemented, fidelity evaluated","YES","'planned' and 'once implemented' are false","Describe the implemented prototype and its completed fidelity evaluation"),
 # ---------- EMPIRICAL TRACE ----------
 ("M-16","(absent)","--","E1 pairwise divergence values","EMPIRICAL_TRACE","CLOSED","condition_comparison.py; claim-status-matrix E1","PRIMARY 42.88/48.69/5.81; RESOLUTION 41.08/45.56/4.48","OPEN-8B","No manuscript locus yet (Section 11 undrafted)","Batch 8B: report under both configurations per E3"),
 ("M-17","(absent)","--","E2 isolated Level 2 contribution","EMPIRICAL_TRACE","CLOSED","condition_comparison.py; claim-status-matrix E2","Delta_L2 5.81% PRIMARY / 4.48% RESOLUTION","OPEN-8B","No manuscript locus yet","Batch 8B"),
 ("M-18","(absent)","--","E3 resolution sensitivity reporting","EMPIRICAL_TRACE","CLOSED","evaluation-specification Section 13 (scope-corrected 2026-09-13)","Mandatory scope {E1,E2,E6}","OPEN-8B","No manuscript locus yet","Batch 8B: apply the corrected E3 scope"),
 ("M-19","(absent)","--","E4 transition/hysteresis characterisation","EMPIRICAL_TRACE","CLOSED","hysteresis_analysis.py; claim-status-matrix E4","3661/3439/222/26/10.36% PRIMARY only","OPEN-8B","No manuscript locus yet","Batch 8B: label PRIMARY temporal-dynamics; no RESOLUTION analogue exists"),
 ("M-20","(absent)","--","E6 C1-C3 trace confirmation","EMPIRICAL_TRACE","CLOSED","condition_comparison.py; claim-status-matrix E6","0.00% both configurations over 43,848 hours","OPEN-8B","No manuscript locus yet","Batch 8B: trace confirmation of a structural equivalence, not a discovery"),
 # ---------- PERFORMANCE ----------
 ("M-21","8","L713-732","Complexity analysis; explicit statement that O(1) does not imply deployment suitability","PERFORMANCE_TARGET","CLOSED","evaluation-specification; algorithm-specification","Asymptotic only","NO","Already correctly bounded; defers to E5","(unchanged)"),
 ("M-22","(absent)","--","E5 governance latency on target hardware","PERFORMANCE_TARGET","OPEN","Batch 7A latency-results.json target_hardware_evidence=false","No target-hardware result exists","OPEN-8B","E5 OPEN; must not appear as a completed result","Batch 8B: Status Pending/Deferred in any results table"),
 ("M-23","(absent)","--","MacBook reference latency","PERFORMANCE_REFERENCE","CLOSED (reference only)","Batch 7A latency-results.json run_type=DEVELOPMENT_MACHINE_REFERENCE","SAFE 0.206615/0.234216/0.253667; CAUTION 0.211715/0.224271/0.259178; UNSAFE 0.194423/0.204335/0.249837 ms","OPEN-8B","No manuscript locus yet","Batch 8B: development-machine reference only, explicitly not target hardware"),
 ("M-24","(absent)","--","H3 latency threshold","PERFORMANCE_TARGET","UNSUPPORTED","evaluation-specification RQ-J2 threshold OPEN","No authorised threshold exists","OPEN-8B","H3 retired into E5/RQ-J2 with threshold OPEN","Batch 8B: no PASS/FAIL against any latency threshold"),
 # ---------- MODEL / SEMANTICS ----------
 ("M-25","5.2","L136 Def 5.1 table row r","'r | R>=0 | [0, inf) | Rainfall intensity (mm/hr)'","FORMAL","SUPERSEDED","appendix-c C.2.0.1; manuscript Def 5.2a","X_r = R>=0 x K, K={0,1}","YES","Contradicts Definition 5.2a in the same section","Type r as the structured pair (rate, kappa)"),
 ("M-26","5.2","L154-162 Def 5.2a","kappa/chi definition, non-escalating default, kappa not in D","FORMAL","CLOSED","appendix-c C.2.0.4a","g_r : R>=0 x K -> S","NO","Correct","(unchanged)"),
 ("M-27","5.2","L164","Solar provenance: NOAA equations, two simplifications, USNO agreement check","DESIGN_INTERPRETATION","CLOSED","Solar Citation Closure; appendix-c","max 0.92 min / 0.75 min; bounds 0.116/0.141/0.457/0.483 min","NO","Bounded; no Meeus attribution","(unchanged)"),
 ("M-28","5.2","L166","Operational exclusion and fail-safe; D={m}; t not in D","FORMAL","CLOSED","appendix-c C.2.0.5-7","D={m} replay","NO","Correct","(unchanged)"),
 ("M-29","5.2","L172","reasons : Q -> P({fault,hazard,policy}) provenance-only contract","DESIGN_INTERPRETATION","CLOSED","appendix-c C.2.0.8","annotation only","NO","Correct","(unchanged)"),
 ("M-30","5.3.1","L182","UNSAFE = governance consequence, not proven danger; human authority unconditional","DESIGN_INTERPRETATION","CLOSED","appendix-c C.2","governance semantics","NO","Correct","(unchanged)"),
 ("M-31","5.3.2","L196-200 Table 1","g_w 21.6/27.0; g_r two-input; g_t Model B no CAUTION","FORMAL","CLOSED","appendix-c C.2; canonical scripts","21.6/27.0; sunrise<=t<sunset","NO","Canonical","(unchanged)"),
 ("M-32","5.3.2","L204-208 Table 1b","Vessel-conditional wave thresholds 1.0/1.25, 1.4/2.8, 1.5/3.5","FORMAL","CLOSED","appendix-c TABLE IIIb","canonical","NO","Canonical","(unchanged)"),
 ("M-33","5.4.4","L292-294","A_AI(CAUTION) is a conservative architecture policy; CAUTION-Go qualifier is Layer 4 rendering","DESIGN_INTERPRETATION","CLOSED","appendix-c; OPEN-L3-3 Resolution B","Resolution B","NO","Correct; no automatic CAUTION->Go","(unchanged)"),
 ("M-34","5.6.1","L340-344","Four-layer structure; unidirectional flow; human authority final","FORMAL","CLOSED","appendix-c; layer3-prototype-specification","Layer 2 -> Layer 3 interface","NO","Correct","(unchanged)"),
 # ---------- STUBS / STRUCTURE ----------
 ("M-35","Abstract","L34-36","'(To be written last - after all sections drafted)'","FUTURE_WORK","N/A","--","stub","YES-MARK","No prose exists to bound; must be authored against the evidence matrix in Batch 8B","Mark for Batch 8B authoring against claim-evidence-matrix"),
 ("M-36","1-4","L46-101","Purpose/Draft here stubs","FUTURE_WORK","N/A","--","stub","YES-MARK","Undrafted; outside 8A scope","Mark for Batch 8B"),
 ("M-37","9-15","L736-905","Purpose/Draft here/To be written stubs","FUTURE_WORK","N/A","--","stub","YES-MARK","Undrafted; outside 8A scope","Mark for Batch 8B, with corrected drafting instructions"),
 ("M-38","12 stub","L809-825","Ablation stub referencing evaluation-specification as maintained authority","FUTURE_WORK","N/A","evaluation-specification.md","--","NO","Already points at correct authority","(unchanged)"),
]
with open(H/"manuscript-claim-inventory.csv","w",newline="",encoding="utf-8") as fh:
    w=csv.DictWriter(fh,fieldnames=INV,quoting=csv.QUOTE_MINIMAL); w.writeheader()
    for r in inv: w.writerow(dict(zip(INV,r)))

MAT = ["claim_id","claim_class","status_before_batch8","status_authoritative","primary_evidence_file",
       "primary_metric_or_result","manuscript_current_state","required_action","allowed_claim_scope","prohibited_overclaim"]
mat = [
 ("P1","FORMAL","CLOSED","CLOSED","data/journal1-post-fidelity-plan/claim-status-matrix.csv; appendix-c Theorem C.1/C.1b","f(E) total; F_D,tau total after resolution","Stated and proved (Sec 5.3.3, 6.2)","NONE","Totality of the classifier over ideal and operational inputs","Do not present totality as an empirical finding"),
 ("P2","FORMAL","CLOSED","CLOSED","claim-status-matrix; appendix-c Theorem C.2","A_AI monotone; strict containment","Stated and proved (Sec 6.3)","NONE","Advisory scope never expands as state worsens","Do not claim the configured sets are optimal"),
 ("P3","FORMAL","CLOSED","CLOSED","claim-status-matrix; appendix-c Theorem C.3","AI(E) subset A_AI(f(E)) by construction","Stated and proved (Sec 6.4-6.5)","NONE","Enforcement of the configured admissible scope","Do not claim real-world safety or recommendation optimality"),
 ("P4","FORMAL","CLOSED","CLOSED","claim-status-matrix; evaluation-specification Sec 4","C1 = C3 by mapping-literal identity","ABSENT from manuscript","DEFER to Batch 8B","Structural proposition with Flehmig fairness qualification","Do not say the replay discovered the equivalence"),
 ("F1","IMPLEMENTATION_FIDELITY","described as not yet demonstrated","CLOSED PASS","data/journal1-layer3-prototype/batch5-fidelity-evaluation/fidelity-results.json","292 episodes; 454 advisory records; 244 conclusion-type evaluations; 0 violations","Section 5.6.2 says fidelity not yet demonstrated","REPAIR status statements in Sec 5-8","Implementation-fidelity containment over the interface-contract state space","Not real-world safety, decision quality, optimality or human behaviour; 244 is not a count of distinct conclusion types"),
 ("F2","IMPLEMENTATION_FIDELITY","described as future","CLOSED PASS","fidelity-results.json","292 episodes; 244 with advisory; 454 records; 0 violations","Section 7 calls F1/F2 a future test","REPAIR","Configured Safety-Dominance fidelity: zero observed violations","Not proof of real-world safety"),
 ("F3","IMPLEMENTATION_FIDELITY","not represented","CLOSED PASS","fidelity-results.json","292 episodes; SAFE 32; CAUTION 260; UNSAFE gate-off 162; 0 mismatches","ABSENT","DEFER results prose to 8B; repair status statements in 8A","Rule-set selection correspondence RS_selected = RS(S_e)","Do not fold the 162 UNSAFE gate-off cases into the 292 SAFE/CAUTION primary episodes"),
 ("E1","EMPIRICAL_TRACE","not represented","CLOSED","scripts/condition_comparison.py","PRIMARY 42.88/48.69/5.81; RESOLUTION 41.08/45.56/4.48","ABSENT","DEFER to Batch 8B","Deterministic census of the predefined retrospective window","No p-values, CIs, sampling or population inference"),
 ("E2","EMPIRICAL_TRACE","not represented","CLOSED","scripts/condition_comparison.py","Delta_L2 = 5.81% PRIMARY / 4.48% RESOLUTION","ABSENT","DEFER to Batch 8B","Isolated Level 2 contribution","Not risk reduction, safety improvement, accuracy or a confidence interval"),
 ("E3","EMPIRICAL_TRACE","scope contradicted E4","CLOSED (scope {E1,E2,E6})","publications/active/journal-1/evaluation-specification.md Sec 13","Mandatory dual-config scope {E1,E2,E6}","ABSENT","DEFER to Batch 8B","Resolution sensitivity for like-for-like comparable quantities","Do not require or imply a RESOLUTION analogue for E4"),
 ("E4","EMPIRICAL_TRACE","not represented","CLOSED (PRIMARY only)","scripts/hysteresis_analysis.py; claim-status-matrix E4","3661 transitions; 3439 scheduled; 222 non-scheduled; 26 oscillations; 10.36% reduction","ABSENT","DEFER to Batch 8B","PRIMARY temporal-dynamics characterisation with provenance chain 5416->5220->5201->3661","Do not attribute 5416->3661 to g_t alone; do not imply a RESOLUTION E4 result exists"),
 ("E5","PERFORMANCE","OPEN","OPEN","data/journal1-e5-benchmark/latency-results.json","target_hardware_evidence = false","ABSENT","KEEP OPEN","E5_HARNESS CLOSED; MacBook = DEVELOPMENT_MACHINE_REFERENCE","Do not close E5; no Android result; no latency threshold; no deployment suitability claim"),
 ("E6","EMPIRICAL_TRACE","not represented","CLOSED","scripts/condition_comparison.py","C1 <-> C3 = 0.00% in both configurations over 43,848 hours","ABSENT","DEFER to Batch 8B","Trace confirmation of an already-established structural equivalence","Do not present as an independent empirical discovery"),
]
with open(H/"claim-evidence-matrix.csv","w",newline="",encoding="utf-8") as fh:
    w=csv.DictWriter(fh,fieldnames=MAT,quoting=csv.QUOTE_MINIMAL); w.writeheader()
    for r in mat: w.writerow(dict(zip(MAT,r)))

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
print("material claims inventoried:",len(inv))
