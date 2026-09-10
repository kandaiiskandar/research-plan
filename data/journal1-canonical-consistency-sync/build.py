#!/usr/bin/env python3
import csv, json, hashlib, pathlib, io, collections
import pandas as pd
H=pathlib.Path(__file__).resolve().parent
def w(name,fields,rows):
    with open(H/name,"w",newline="",encoding="utf-8") as fh:
        wr=csv.DictWriter(fh,fieldnames=fields,quoting=csv.QUOTE_MINIMAL); wr.writeheader()
        for r in rows: wr.writerow(dict(zip(fields,r)))

FC=["file","classification","maintained_target","rationale"]
fc=[
 ("publications/active/journal-1/submissions/v1-initial-submission/manuscript.md","ACTIVE-MAINTAINED","YES","README names it 'Current working manuscript ... aligned to Appendix C'; its own header says 'active working manuscript'; project status is research-design phase with target submission early 2027. The directory name v1-initial-submission is misleading - nothing has been submitted, so J1-R6 does not apply"),
 ("publications/active/journal-1/research-design.md","ACTIVE-MAINTAINED","NO","RQs, hypotheses, metrics and open checklist for work not yet done"),
 ("publications/active/journal-1/README.md","ACTIVE-MAINTAINED","NO","Submission tracking, venue, deadlines; names the maintained target"),
 ("publications/active/journal-1/correspondence/notes.md","SUPPORTING","NO","Correspondence notes; no canonical claims"),
 ("publications/active/journal-1/section-5-plan.md","HISTORICAL","NO","Carries a document-level 2026-09-09 banner: 'historical drafting plan, superseded for implementation and publication reuse', pointing to the maintained manuscript"),
 ("publications/active/journal-1/section-6-plan.md","HISTORICAL","NO","Same document-level supersession banner"),
 ("publications/active/journal-1/session-log.md","HISTORICAL","NO","Dated session records (## Session: 2026-08-09 etc). Contains g_v and 1.5 m references that record what was believed on those dates"),
 ("publications/active/journal-1/submissions/.DS_Store","IRRELEVANT","NO","macOS filesystem artefact"),
]
w("journal1-file-classification.csv",FC,fc)

A=["id","file","locator","category","claim_or_structure","classification","canonical_authority","expected_state","action","status","notes"]
a=[
 ("J1-01","manuscript.md","Table 1 threshold table, g_r row","RAINFALL","g_r(r) | ... | r > 20.0 mm/hr; specified storm indication where available","ACTIVE-CANONICAL-DRIFT","appendix-c C.2 and C.2.0.4a","g_r(r, kappa) with kappa=1 -> UNSAFE for any rate","Row retyped to the four canonical cases","REPAIRED","'Storm indication where available' is the pre-kappa formulation: an untyped second input with no declared domain"),
 ("J1-02","manuscript.md","Section 5 f(E) definition","FORMAL","f(E) = max_> {g_w(w), g_r(r), ...}","ACTIVE-CANONICAL-DRIFT","appendix-c C.2","g_r(r, kappa)","Updated","REPAIRED","Scalar signature in the paper's central classifier definition"),
 ("J1-03","manuscript.md","Theorem 6.1 totality proof, g_r case","FORMAL","Numeric rate intervals are exhaustive and disjoint; the specified storm indication also maps to UNSAFE where available","ACTIVE-CANONICAL-DRIFT","appendix-c Theorem C.1(i)","Two-case proof over kappa in {0,1}","Rewritten as a product-domain proof","REPAIRED","Same defect Appendix C carried before its own synchronisation: the rate partition alone was claimed to exhaust g_r's domain"),
 ("J1-04","manuscript.md","Theorem 6.1 max_> restatement and conclusion","FORMAL","g_r(r) in both restatements","ACTIVE-CANONICAL-DRIFT","appendix-c","g_r(r, kappa)","Updated in both","REPAIRED","Notation consistency inside the proof"),
 ("J1-05","manuscript.md","Section 5, before Solar-event provenance","RAINFALL","No definition of kappa, chi, or the rainfall input type existed anywhere in the paper","ACTIVE-CANONICAL-DRIFT (omission)","appendix-c C.2.0.4a","X_r = R>=0 x K; kappa = chi(c); required rate vs derived indicator","New Definition 5.2a added","REPAIRED","The paper used the classifier without ever declaring its input type. Definition states: c is not the classifier input; chi is total and never returns bottom; the kappa=0 default is non-escalating and NOT fail-safe; rate remains required; kappa is escalation-only; kappa is not in D"),
 ("J1-06","manuscript.md","Section 5 governance-pair paragraph","NOVELTY","Prior governance architectures implement only a participation gate G(S)","ACTIVE-CANONICAL-DRIFT","canonical novelty framing; conference manuscript repair","Graduated governance exists; graduated ADVISORY-SCOPE governance is the gap","Rewritten to concede graduated governance and scope the binary claim to the advisory-scope axis","REPAIRED","Same universal overclaim corrected in the conference manuscript. TABLE II of that paper lists five graduated architectures"),
 ("J1-07","manuscript.md","Evaluation conditions table","EMPIRICAL / REPORTABILITY","C1 Ungated, C2 Binary-gated, C3 Graduated (proposed)","ACTIVE-CANONICAL-DRIFT","scripts/condition_comparison.py; conference TABLE VII","Canonical: C0 Ungated, C1 Binary-gated, C2 Proposed, C3 Flehmig traffic-light","Mapping table added; labels NOT renamed","REPAIRED","ALL THREE LABELS COLLIDE and C2 INVERTS - canonical C2 is the proposed architecture, Journal 1's C2 is the binary baseline. Renaming would ripple into H1-H4 and the section plans, so an explicit mapping is the minimal complete fix"),
 ("J1-08","research-design.md","Next actions checklist","EMPIRICAL / REPORTABILITY","Finalise three-condition comparison design (C1 Ungated, C2 Binary-gated, C3 Graduated)","ACTIVE-CANONICAL-DRIFT","scripts/condition_comparison.py","Same mapping","Cross-reference to the mapping table added","REPAIRED","The label scheme also appears in the planning document that will drive the evaluation"),
 ("J1-09","manuscript.md","Evaluation conditions","EMPIRICAL","No counterpart to the canonical C3 Flehmig-style traffic-light baseline","OPEN - evaluation design","empirical-findings F-15","A Flehmig-style baseline establishes the gap as a measurement (0.00% divergence)","RECORDED, NOT ADDED","J1-R2: adding a baseline is an evaluation-design decision, not a synchronisation. Recorded as an open item in the manuscript"),
 ("J1-10","manuscript.md","g_w row of Table 1","WIND","w <= 21.6 kn | 21.6 < w <= 27.0 | > 27.0","ACTIVE-CORRECT","canonical scripts W_CAUTION=21.6","-","NO EDIT","Already canonical; no 22 kn anywhere in maintained prose"),
 ("J1-11","manuscript.md","Table 1b","WAVE","small 1.0/1.25, medium 1.4/2.8, big 1.5/3.5","ACTIVE-CORRECT","appendix-c TABLE IIIb","-","NO EDIT","Canonical; no active 1.9 m"),
 ("J1-12","manuscript.md","g_t row and header banner","TIME","SAFE sunrise <= t < sunset; no CAUTION; UNSAFE on clock/date/solar failure","ACTIVE-CORRECT","SDR-001; canonical_gt.py","-","NO EDIT","Model B already applied; no active fixed clock"),
 ("J1-13","manuscript.md","Solar-event provenance paragraph","SOLAR","implements NOAA's published general solar-position equations with two disclosed simplifications; frozen daily table; 5.98N 116.01E UTC+8 zenith 90.833","ACTIVE-CORRECT","Solar Citation Closure","-","NO EDIT","Zero occurrences of 'Meeus' in the file"),
 ("J1-14","manuscript.md","Time and observation context; operational exclusion","OBSERVATION","Obs_i = (X_i x T) u {bottom}; rho_{D,tau}; F_{D,tau}; t not in D; exclusions before faults; D={m} retrospective","ACTIVE-CORRECT","appendix-c C.2.0","-","NO EDIT","Already aligned"),
 ("J1-15","manuscript.md","Provenance-only paragraph","GOVERNANCE","reasons : Q -> P({fault,hazard,policy})","ACTIVE-CORRECT","appendix-c C.2.0.8","-","NO EDIT","Contract stated correctly"),
 ("J1-16","manuscript.md","Severity order paragraph; COLREG note","EPISTEMIC","UNSAFE means AI advisory participation is unavailable; nighttime abstention is architecture policy, COLREGs provides a navigation-light boundary not a mandate","ACTIVE-CORRECT","appendix-c C.2 evidence/policy block","-","NO EDIT","Governance semantics correctly bounded"),
 ("J1-17","manuscript.md","Theorem 6.3 summary; A_AI(CAUTION) paragraph","GOVERNANCE","AI output is bounded within the admissible scope at every state, by construction; restriction is a conservative architecture policy","ACTIVE-CORRECT","conference manuscript repair","-","NO EDIT","Uses 'admissible scope'; zero occurrences of 'warranted scope'"),
 ("J1-18","manuscript.md","Layer 3 specification","EPISTEMIC","Layer 3 is specified as a production rule engine; runtime fidelity is not yet demonstrated","ACTIVE-CORRECT","canonical: Layer 3 unbuilt","-","NO EDIT","Correctly disclaims validation of engine content"),
 ("J1-19","manuscript.md","Ablation plan note","EMPIRICAL","canonical specification: 3,661 transitions","ACTIVE-CORRECT","hysteresis_analysis.py","-","NO EDIT","Canonical transition count"),
 ("J1-20","section-5-plan.md","Threshold table; f(E) with g_v","FORMAL / WIND / RAINFALL","g_w < 22 kn; g_r categorical {none,light,moderate}/{heavy}/{storm}; f(E) includes g_v(v)","HISTORICAL-SUPERSEDED","-","-","NO EDIT","Document-level 2026-09-09 banner marks it a historical drafting plan superseded for publication reuse and points to the maintained manuscript"),
 ("J1-21","section-6-plan.md","Totality checklist","RAINFALL","g_r: all five values {none, light, moderate, heavy, storm} assigned","HISTORICAL-SUPERSEDED","-","-","NO EDIT","Same document-level banner"),
 ("J1-22","session-log.md","2026-08-09 entries","FORMAL / WAVE","g_v empirical support; 1.5 m CAUTION boundary for g_o","HISTORICAL","-","-","NO EDIT","Dated session records of what was done and believed on those dates"),
 ("J1-23","README.md; correspondence/notes.md","whole file","PROVENANCE","venue, deadlines, tracking; correspondence","IRRELEVANT","-","-","NO EDIT","No canonical claims"),
]
w("journal1-canonical-audit.csv",A,a)

C=["file","finding_ids","change_class","reason"]
c=[
 ("publications/active/journal-1/submissions/v1-initial-submission/manuscript.md","J1-01;J1-02;J1-03;J1-04;J1-05;J1-06;J1-07;J1-09","FORMAL-MODEL + NOVELTY + REPORTABILITY","Five g_r loci retyped to the canonical product domain, Definition 5.2a added for kappa/chi, novelty overclaim scoped, condition-label mapping and missing-baseline open item recorded"),
 ("publications/active/journal-1/research-design.md","J1-08","REPORTABILITY","Condition-label collision flagged where the evaluation design is planned"),
]
w("journal1-change-map.csv",C,c)

# verification JSONs
(H/"formal-model-verification.json").write_text(json.dumps({
 "g_r_signature":"g_r : R>=0 x K -> {SAFE, CAUTION, UNSAFE}, K={0,1}","kappa":"chi(c)=1 iff c in {95,96,99}",
 "kappa_never_bottom":True,"kappa_default_non_escalating_not_failsafe":True,"kappa_in_D":False,
 "rate_required_bottom_to_UNSAFE":True,"totality_two_cases_over_kappa":True,
 "g_w":"21.6 / 27.0","g_o_small":"1.0 / 1.25","g_o_medium":"1.4 / 2.8","g_o_big":"1.5 / 3.5",
 "g_t":"SAFE iff sunrise(date) <= t < sunset(date); no CAUTION; bottom -> UNSAFE",
 "D":"{m} retrospective","t_in_D":False,
 "observation_model":"Obs_i = (X_i x T) u {bottom}; rho_{D,tau}; F_{D,tau} = f o rho",
 "reasons_contract":"Q -> P({fault,hazard,policy})",
 "safety_dominance_wording":"admissible scope; no 'warranted scope' present"},indent=2)+"\n")
(H/"empirical-verification.json").write_text(json.dumps({
 "level2":"5.81% / 4.48%","daylight_unsafe":"1262 / 455","g_o":"98.71% / 97.66%",
 "g_t":"86.82% / 90.19%","g_r_daylight":"1.48% / 2.70%","g_r_all_hours":"0.20% / 0.26%",
 "transitions":"3661 / 3439 / 222 / 26 / 10.36%",
 "journal1_empirical_content":"Sections 1-6 drafted are formal/theoretical; empirical sections remain plans. Only canonical figure quoted is 3,661 transitions, which is correct.",
 "unchanged":True},indent=2)+"\n")
(H/"prediction-verification.json").write_text(json.dumps({
 "total":24,"CONFIRMED":15,"REFUTED":9,
 "refuted_ids":["P01","P04","P09","P18","P19","P20","P22","P23","P24"],
 "P16":"CONFIRMED","P01":"REFUTED","P09":3661,
 "P09_provenance":"5416 -> 5220 (threshold) -> 5201 (data) -> 3661 (g_t); not a pure g_t effect",
 "P20":1529,"P20_scope":"registered 06:00-17:00 scope; distinct from 455 astronomical-daylight RESOLUTION",
 "sdr001_attributable":["P20","P23","P24"],
 "journal1_references_prediction_state":False,"register_unchanged":True},indent=2)+"\n")
(H/"data-provenance-verification.json").write_text(json.dumps({
 "canonical_weather":"raw_weather_sea.csv supplies wind, precipitation and raw weather code c",
 "PRIMARY_waves":"raw_marine_era5_sea.csv","RESOLUTION_waves":"raw_marine_mfwam.csv",
 "historical_land":["raw_weather.csv","raw_rainfall.csv","raw_marine.csv"],
 "separations_km":{"PRIMARY":7.2,"RESOLUTION":2.7,"v1_historical":12.9},
 "journal1_states_data_sources":False,
 "note":"Journal 1's drafted sections do not yet state data sources; empirical sections remain plans. No land-cell configuration is presented as current.",
 "datasets_unchanged":True},indent=2)+"\n")

rep={}
for p in sorted(H.glob("*.csv")):
    raw=p.read_text(encoding="utf-8"); rdr=csv.reader(io.StringIO(raw)); hdr=next(rdr); n=len(hdr)
    bad=[(i+2,len(r)) for i,r in enumerate(rdr) if len(r)!=n]
    dr=len(list(csv.DictReader(io.StringIO(raw)))); df=pd.read_csv(io.StringIO(raw))
    rep[p.name]={"fields":n,"dictreader_rows":dr,"pandas_rows":int(df.shape[0]),"malformed":bad,
      "sha256_16":hashlib.sha256(p.read_bytes()).hexdigest()[:16],
      "parse":"PASS" if not bad and dr==df.shape[0] and n==df.shape[1] else "FAIL"}
(H/"parser-test.json").write_text(json.dumps(rep,indent=2)+"\n")
for k,v in rep.items(): print("%-5s %-38s fields=%2d DictReader=%2d pandas=%2d"%(v["parse"],k,v["fields"],v["dictreader_rows"],v["pandas_rows"]))
print("ALL PASS:",all(v["parse"]=="PASS" for v in rep.values()))
print("classification:",dict(collections.Counter(r[5] for r in a)))
