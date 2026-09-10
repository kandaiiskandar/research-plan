#!/usr/bin/env python3
import csv, json, hashlib, pathlib, io, collections
import pandas as pd
H=pathlib.Path(__file__).resolve().parent
F=["id","file","locator","semantic_class","claim","classification","canonical_authority","action","status","notes"]
rows=[
 ("S1-01","manuscript.md","Section 6 Composite Guarantee, closing sentence","EPISTEMIC - Safety Dominance","no formally identifiable path by which an AI recommendation can exceed the scope warranted by the current environmental conditions","ACTIVE-CANONICAL-DRIFT","Theorem 6.3 proves AI(E) subset A_AI(f(E)) under the RS(S)/Layer 3 assumptions","Replaced with 'the configured admissible scope associated with the current governance state'","REPAIRED","THE NAMED RESIDUE. 'Warranted by the current environmental conditions' claims the environment determines which advice is correct - the theorem establishes enforcement of a configured mapping, not the soundness of that configuration"),
 ("S1-02","manuscript.md","Same sentence, monotonicity clause","EPISTEMIC - Monotonicity","Monotonicity ensures that state appropriately restricts scope as risk increases","ACTIVE-CANONICAL-DRIFT","Theorem 6.2 proves A_AI(S1) subset A_AI(S2) whenever S1 > S2","Replaced with 'the configured admissible sets contract, never expand, as the classified state worsens'","REPAIRED","NOT IN THE BRIEF. 'Appropriately' is the same overclaim in a quieter word: monotonicity proves the direction of change, not that the restriction is fitting"),
 ("S1-03","manuscript.md","Section 6, after the Composite Guarantee","EPISTEMIC - scope of the theorems","No statement bounding what the three theorems do NOT establish","ACTIVE-CANONICAL-DRIFT (omission)","conference manuscript limitation 1; appendix-c","New paragraph: the theorems verify enforcement, not the soundness of the configuration; A_AI(CAUTION)={Go,Delay} is a conservative architecture policy and its derivation remains outstanding","REPAIRED","Closes the gap positively rather than only removing a word, so the boundary cannot drift back in"),
 ("S1-04","manuscript.md","Section 13 discussion plan","DOMAIN-TRANSFER","Generalisation: which aspects of the architecture are domain-independent","ACTIVE-CANONICAL-DRIFT","canonical distinction: structurally re-instantiable vs empirically domain-specific","Rewritten to separate re-instantiable structures from domain-specific thresholds, inputs, evidence and findings","REPAIRED","A writing instruction, so the more dangerous kind: it would have propagated the retired overclaim into prose not yet written"),
 ("S1-05","manuscript.md","Theorem summary table, row 6.3","EPISTEMIC","AI output is bounded within the admissible scope at every state, by construction","ACTIVE-CORRECT","-","NO EDIT","Already uses 'admissible scope' without epistemic loading"),
 ("S1-06","manuscript.md","Section 5, A_AI(CAUTION) paragraph","EPISTEMIC","The restriction of A_AI(CAUTION) to {Go, Delay} is a conservative architecture policy","ACTIVE-CORRECT","-","NO EDIT","Correctly labels the partition a policy; now cross-referenced from the new Section 6 paragraph"),
 ("S1-07","manuscript.md","Section 6.3 statement and proof","EPISTEMIC","AI(E) subset A_AI(f(E)) for all E","ACTIVE-CORRECT","-","NO EDIT - theorem untouched","The repair changes only the prose interpreting the theorem, never the theorem or its proof"),
 ("S1-08","manuscript.md","Evaluation conditions mapping table","SCOPE-PRESERVED","canonical C0->C1, C1->C2, C2->C3, C3 Flehmig no equivalent","ACTIVE-CORRECT","condition_comparison.py","NO EDIT - deliberately preserved","J1-SR3: conditions not renamed, mapping left exactly as accepted in the prior closure"),
 ("S1-09","manuscript.md","Evaluation conditions open item","DEFERRED","Journal 1 has no Flehmig-style C3 baseline","OPEN - evaluation design","empirical-findings F-15","NO EDIT - deliberately preserved","J1-SR3: not added. Not canonical drift - the Journal 1 experiments have not been executed, so this is future research-design work"),
 ("S1-10","section-5-plan.md; section-6-plan.md; session-log.md","various","EPISTEMIC / DOMAIN-TRANSFER","no occurrences of either residue class","IRRELEVANT","-","NO EDIT","Full-line sweep found zero hits in the historical and planning files"),
 ("S1-11","research-design.md; README.md; correspondence/notes.md","various","EPISTEMIC / DOMAIN-TRANSFER","no occurrences of either residue class","ACTIVE-CORRECT","-","NO EDIT","Clean"),
]
with open(H/"semantic-closure-audit.csv","w",newline="",encoding="utf-8") as fh:
    w=csv.DictWriter(fh,fieldnames=F,quoting=csv.QUOTE_MINIMAL); w.writeheader()
    for r in rows: w.writerow(dict(zip(F,r)))
v=json.load(open(H/"semantic-closure-verification.json"))
v.update({
 "trigger":"independent review after the prior Journal 1 closure",
 "prior_audit_false_negative":{
   "claim_made":"the phrase 'warranted scope' does not occur",
   "reality":"it occurred in the Composite Guarantee sentence of the maintained manuscript",
   "cause":"the regex DID match the line; the audit command piped results through sed 's/\\(.\\{170\\}\\).*/\\1…/' and the matching word sat beyond character 170, so the displayed evidence was truncated before the match. Classification was made on the visible fragment.",
   "lesson":"a search that truncates its own output can report a hit and hide the reason it hit. Match context must be shown, not the head of the line."},
 "repairs":["S1-01 warranted -> configured admissible scope",
            "S1-02 appropriately restricts -> contract, never expand",
            "S1-03 new does-not-establish paragraph",
            "S1-04 domain-independent -> re-instantiable vs domain-specific"],
 "preserved":{"condition_mapping":"unchanged","flehmig_baseline":"still deferred, open item intact",
              "theorems":"statements and proofs untouched"},
 "canonical_state":{"g_r":"g_r(r, kappa)","kappa":"chi(c)=1 iff c in {95,96,99}","D":"{m}",
   "g_w":"21.6 / 27.0","wave_small_UNSAFE":">1.25 m","g_t":"Model B, exact sunrise SAFE, exact sunset UNSAFE",
   "level2":"5.81% / 4.48%","register":"24 = 15 CONFIRMED / 9 REFUTED"},
 "authorities_unchanged":True,"empirical_unchanged":True,"prediction_unchanged":True,
 "stop_conditions":{"J1-SR1":False,"J1-SR2":False,"J1-SR3":False,"J1-SR4":False}})
(H/"semantic-closure-verification.json").write_text(json.dumps(v,indent=2)+"\n")
rep={}
for p in sorted(H.glob("*.csv")):
    raw=p.read_text(encoding="utf-8"); rdr=csv.reader(io.StringIO(raw)); hdr=next(rdr); n=len(hdr)
    bad=[(i+2,len(r)) for i,r in enumerate(rdr) if len(r)!=n]
    dr=len(list(csv.DictReader(io.StringIO(raw)))); df=pd.read_csv(io.StringIO(raw))
    rep[p.name]={"fields":n,"dictreader_rows":dr,"pandas_rows":int(df.shape[0]),"malformed":bad,
      "parse":"PASS" if not bad and dr==df.shape[0] and n==df.shape[1] else "FAIL"}
(H/"parser-test.json").write_text(json.dumps(rep,indent=2)+"\n")
for k,x in rep.items(): print("%-5s %-38s fields=%2d DictReader=%2d pandas=%2d"%(x["parse"],k,x["fields"],x["dictreader_rows"],x["pandas_rows"]))
print("ALL PASS:",all(x["parse"]=="PASS" for x in rep.values()))
print("classification:",dict(collections.Counter(r[5] for r in rows)))
