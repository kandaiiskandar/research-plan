#!/usr/bin/env python3
import csv, json, hashlib, pathlib, io, collections
import pandas as pd
HERE=pathlib.Path(__file__).resolve().parent
F=["id","file","locator","assertion_class","claim","classification","canonical_authority","action","status","notes"]
rows=[
 ("EA-01","docs/canonical/empirical-findings-2026-09-06.md","F-11 opening paragraph","A - thunderstorm epistemic overclaim","Zero thunderstorms in five years, in equatorial Borneo","ACTIVE-CANONICAL-DRIFT","raw weather code audit: kappa=1 in 0 of 43,848 hours, both cells","Replaced with the provider-code boundary: no activating code occurs, so the route is unexercised; explicitly not evidence that no thunderstorms occurred","REPAIRED","THE KNOWN DEFECT. Absence of a provider code is evidence about the provider code, not about the weather. The very next sentence ('This is not climatology') was making that point while the claim above it stated the opposite"),
 ("EA-02","docs/canonical/empirical-findings-2026-09-06.md","F-11 consequence sentence","A - stale quantitative","precipitation > 20 mm/hr occurs 14 times in five years","ACTIVE-CANONICAL-DRIFT","raw_weather_sea.csv: 21 hours >20 mm/hr; raw_weather.csv and raw_rainfall.csv: 14","Corrected to 21 with the 14 retained and identified as the v1 land-cell figure","REPAIRED","Reconciled, not merely replaced: 14 is exactly right for the land cell and exactly wrong for the canonical sea cell. Land also gives 131 hours >10 mm/hr against 113"),
 ("EA-03","docs/canonical/empirical-findings-2026-09-06.md","F-13 heading","B - wind","F-13 - Q1a RESOLVED: F-1 is real. Wind genuinely never reaches the threshold","ACTIVE-CANONICAL-DRIFT","canonical W_CAUTION 21.6 kn; 2 activations","Heading replaced with 'Q1a RESOLVED: sea-cell recollection materially raises measured wind'; ID F-13 preserved","REPAIRED","A heading governs how every sentence beneath it is read, so a supersession banner mid-section could not neutralise it"),
 ("EA-04","docs/canonical/empirical-findings-2026-09-06.md","F-13 comparison table, g_w activations row","B - wind","g_w activations | 0 | 0 | unchanged","ACTIVE-CANONICAL-DRIFT (unscoped)","canonical 21.6 kn","Row relabelled 'at the then-specified 22.0 kn boundary' with a scope note giving the canonical result","REPAIRED","Historically correct but the column carried no boundary, so it read as a current result"),
 ("EA-05","docs/canonical/empirical-findings-2026-09-06.md","F-13 Consequence paragraph","B - wind","Sustained wind does not reach MET Malaysia's Category 1 criterion in five years of data, at either grid cell","ACTIVE-CANONICAL-DRIFT","canonical 21.6 kn; 21.7 and 21.8 kn crossings","Replaced by a restatement block deferring to F-17","REPAIRED","Stood AFTER the existing F-17 banner and still read as the section's conclusion"),
 ("EA-06","docs/canonical/empirical-findings-2026-09-06.md","F-13 Caveat on the margin","B - wind","The honest statement is 'sustained wind essentially never reaches the threshold'","ACTIVE-CANONICAL-DRIFT","canonical 21.6 kn","Caveat retained and annotated: it correctly identified that the result hung on 0.2 kn, but anticipated the wrong side of the comparison moving","REPAIRED","Worth preserving - it was the prescient paragraph in the finding"),
 ("EA-07","docs/canonical/empirical-findings-2026-09-06.md","F-13 methodological note","B - wind","Because g_w never fires either way, the wind data never influenced any classification","ACTIVE-CANONICAL-DRIFT","canonical 21.6 kn: 2 activations, 0 bindings","Scoped to the 22.0 kn configuration; canonical activation/binding split stated","REPAIRED","'Never governed a classification' is true; 'never fires' is not"),
 ("EA-08","docs/canonical/empirical-findings-2026-09-06.md","3.1 conflation paragraph","B - wind","one component was tested and found inactive at this site","ACTIVE-CANONICAL-DRIFT","canonical 21.6 kn","Changed to 'found non-binding', with both counts","REPAIRED","Found beyond F-11/F-13 by the repository-wide sweep"),
 ("EA-09","docs/canonical/empirical-findings-2026-09-06.md","3.2 opening","B - wind","Sustained wind does not reach MET Malaysia's Category 1 criterion in five years of hourly data","ACTIVE-CANONICAL-DRIFT","canonical 21.6 kn","Replaced with 'reaches the criterion just twice ... and governs no classification on either occasion'","REPAIRED","In a section already partly maintained - its adjacent item 1 and closing paragraph had been corrected, this had not"),
 ("EA-10","docs/canonical/empirical-findings-2026-09-06.md","3.2 item 2","B - wind","changed the classification results by nothing, because g_w never fires either way (F-13)","ACTIVE-CANONICAL-DRIFT","canonical 21.6 kn","Scoped to the 22.0 kn configuration with the canonical result stated","REPAIRED","Same section, second instance"),
 ("EA-11","docs/canonical/empirical-findings-2026-09-06.md","F-11 heading","A","Thunderstorms are undetectable in this dataset","ACTIVE-CORRECT","-","NO EDIT","Accurate: a claim about detectability, not occurrence"),
 ("EA-12","docs/canonical/empirical-findings-2026-09-06.md","F-13 'at the then-specified 22 kn boundary'; existing F-17 banner","B","g_w still never fired at the then-specified boundary","ACTIVE-CORRECT","-","NO EDIT","Correctly scoped to the historical boundary"),
 ("EA-13","docs/canonical/empirical-findings-2026-09-06.md","F-1 as-first-measured block","B","Zero activations","HISTORICAL-SUPERSEDED","-","NO EDIT","Block-marked by the F-17 restatement banner and 'as first measured' framing"),
 ("EA-14","docs/canonical/data-provenance.md","r row, Fit for threshold","A","zero activating codes ... not evidence that no thunderstorms occurred","ACTIVE-CORRECT","-","NO EDIT","Already carries the epistemic boundary, added in the earlier drift repair"),
 ("EA-15","docs/canonical/data-provenance.md","w row, Fit for threshold","B","activates twice, binds in neither","ACTIVE-CORRECT","-","NO EDIT","Repaired in the wind-assertion closure"),
 ("EA-16","docs/canonical/finding-met-hydrodynamic-gap.md","Section on literal MET reading","B","never restricts anything","IRRELEVANT","-","NO EDIT","Concerns MET WAVE criteria at 3.5 m, not g_w"),
 ("EA-17","publications/active/journal-1/*","various","A and B","thunderstorm and wind assertions","DEFERRED - Journal 1","-","RECORDED, NOT FIXED","Out of scope for this branch"),
]
with open(HERE/"empirical-assertion-residue-audit.csv","w",newline="",encoding="utf-8") as fh:
    w=csv.DictWriter(fh,fieldnames=F,quoting=csv.QUOTE_MINIMAL); w.writeheader()
    for r in rows: w.writerow(dict(zip(F,r)))
ver={
 "rainfall_counts":{"canonical_sea_gt20":21,"canonical_sea_gt10":113,"canonical_sea_max":45.8,
   "v1_land_gt20":14,"v1_land_gt10":131,"v1_land_max":39.2,
   "reconciliation":"F-11's 14 is the v1 land-cell count; canonical sea cell gives 21. No conflict - EA-R2 not triggered"},
 "kappa":{"kappa_1_hours":0,"missing_raw_code":0,"invalid_raw_code":0,"evaluated_hours":43848,
   "both_cells":"kappa=1 is 0 on BOTH land and sea cells, so the code absence is not a cell artefact"},
 "wind":{"W_CAUTION":21.6,"W_UNSAFE":27.0,"max_sea":21.8,"max_land":17.8,
   "activations_sea_at_21_6":2,"activations_sea_at_22_0":0,"activations_land":0,"bindings":0,
   "governing_components":["g_o on 2021-01-17 06:00","g_t on 2024-04-30 23:00"]},
 "authority_chain":"F-1 (historical, 22 kn) -> F-13 (sea recollection) -> F-17 (canonical restatement, 21.6 kn). F-17 is later and governs.",
 "active_residues":{"A_thunderstorm_occurrence":0,"B_wind_never_reaches":0},
 "empirical":{"level2":"5.81% / 4.48%","g_o":"98.71% / 97.66%","g_t":"86.82% / 90.19%",
   "g_r_daylight":"1.48% / 2.70%","g_r_all_hours":"0.20% / 0.26%","daylight_unsafe":"1262 / 455",
   "transitions":"3661 / 3439 / 222 / 26 / 10.36%"},
 "register":{"total":24,"CONFIRMED":15,"REFUTED":9,"P01":"REFUTED","P16":"CONFIRMED","P09":3661,"P20":1529},
 "data_flow_unchanged":"raw_weather_sea.csv supplies wind, precipitation and raw code c; land files historical only",
 "stop_conditions":{f"EA-R{i}":False for i in range(1,7)},
 "files_changed":["docs/canonical/empirical-findings-2026-09-06.md"],
 "all_clear":True}
(HERE/"empirical-assertion-closure-verification.json").write_text(json.dumps(ver,indent=2)+"\n")
rep={}
for p in sorted(HERE.glob("*.csv")):
    raw=p.read_text(encoding="utf-8"); rdr=csv.reader(io.StringIO(raw)); hdr=next(rdr); n=len(hdr)
    bad=[(i+2,len(r)) for i,r in enumerate(rdr) if len(r)!=n]
    dr=len(list(csv.DictReader(io.StringIO(raw)))); df=pd.read_csv(io.StringIO(raw))
    rep[p.name]={"fields":n,"dictreader_rows":dr,"pandas_rows":int(df.shape[0]),"malformed":bad,
      "parse":"PASS" if not bad and dr==df.shape[0] and n==df.shape[1] else "FAIL"}
(HERE/"parser-test.json").write_text(json.dumps(rep,indent=2)+"\n")
for k,v in rep.items(): print("%-5s %-42s fields=%d DictReader=%d pandas=%d"%(v["parse"],k,v["fields"],v["dictreader_rows"],v["pandas_rows"]))
print("ALL PASS:",all(v["parse"]=="PASS" for v in rep.values()))
print("classification:",dict(collections.Counter(r[5].split(" (")[0].split(" - ")[0] for r in rows)))
