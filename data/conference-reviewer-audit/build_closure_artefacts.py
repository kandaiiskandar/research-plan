#!/usr/bin/env python3
"""Independent Reviewer Closure Repair — artefacts. csv.DictWriter + parser test."""
import csv, json, hashlib, pathlib, io
HERE = pathlib.Path(__file__).resolve().parent

def write(name, fields, rows):
    with open(HERE/name, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        for r in rows: w.writerow(r)

# --- REV items ---
REV = ["id","item","resolution","status"]
rev = [
 ("REV-1","Abstract asserts all governance is uniformly binary, contradicting TABLE II which lists five graduated architectures","Abstract, Introduction and Introduction contribution paragraph rewritten to the narrower defensible claim: graduated governance exists, graduated ADVISORY-SCOPE governance does not","CLOSED"),
 ("REV-2","Three further binary-premise sites required classification rather than edit","Deterministic-constraints heading, cross-paradigm synthesis and Result 1 verified as correctly scoped to a named paradigm or to the instantiated C1 baseline; retained unchanged","CLOSED"),
 ("REV-3","g_r formal typing defect: r typed over the reals, Theorem 1 partitions only that axis, Algorithm 1 admits a storm indication with no formal representation","Option A. g_r retyped as a product domain over rate and thunderstorm indication kappa, matching all eight canonical scripts; totality proof, signature, Algorithm 1, domain declaration and resolution wording all updated","CLOSED"),
 ("REV-4","Domain-independence overstatement in Domain Instantiation","Reworded to separate the re-instantiable governance structure from the domain-specific case; existing bounded claims elsewhere retained unchanged","CLOSED"),
 ("REV-5","Conclusion turns a structural containment theorem into an epistemic-validity claim via warranted scope","Replaced with configured admissible scope, plus an explicit statement that the theorem does not assert the configured set is epistemically correct","CLOSED"),
 ("REV-6","Protected scientific state must be unchanged","19 protected artefacts re-hashed; only the manuscript changed. Canonical generators re-run: 5.81/4.48, 1262/455, 98.71/97.66, 86.82/90.19 all reproduce","CLOSED"),
 ("REV-7","Prediction register must be untouched","24 entries, 15 CONFIRMED / 9 REFUTED, P09 actual 3661, P20 actual 1529 — all unchanged","CLOSED"),
 ("REV-8","Reference integrity must not regress","40 references, zero orphan, zero dangling","CLOSED"),
 ("REV-9","Packaging placeholders","Recorded in submission-packaging-checklist.csv; not scientific closure blockers","RECORDED"),
 ("REV-10","Repository drift outside the manuscript","Recorded in repository-drift.csv; recommended as a separate bounded cleanup after reviewer closure","RECORDED"),
]
write("closure-rev-items.csv", REV, [dict(zip(REV,r)) for r in rev])

# --- binary premise classification ---
BP = ["location","text_before","classification","action"]
bp = [
 ("Abstract","Existing governance mechanisms are uniformly binary","FALSE UNIVERSAL - contradicted by TABLE II","REWRITTEN to the oversight/participation/execution/authority/action-space distinction"),
 ("Introduction para 2","Current systems see this as a binary: the AI makes its entire set of recommendations or it is turned off","FALSE UNIVERSAL","REWRITTEN - graduated mechanisms acknowledged, binary restricted to the advisory-scope axis"),
 ("Introduction contribution para","Existing governance mechanisms conflate two distinct variables into a single binary","AMBIGUOUS - reads as universal","NARROWED to architectures that are graduated on some other dimension"),
 ("Literature Review heading","Deterministic Safety Constraints: Binary by Construction","ACCURATE - scoped to one named paradigm","RETAINED"),
 ("Cross-paradigm synthesis","Deterministic constraints are binary by construction; adaptive risk-based systems apply their intermediate levels to human workflows or execution deferral rather than output scope","ACCURATE - already differentiates graduated from advisory-scope-graduated","RETAINED"),
 ("Result 1","A binary architecture, having no state between participation and withdrawal, supplies the full recommendation set","ACCURATE - refers to the instantiated C1 baseline","RETAINED"),
 ("Fisheries application level","None of the fisheries AI systems identified implement formal advisory scope restriction","ACCURATE - scoped to the application domain","RETAINED"),
]
write("binary-premise-classification.csv", BP, [dict(zip(BP,b)) for b in bp])

# --- packaging checklist ---
PK = ["item","location","blocker_type","required_before"]
pk = [
 ("Fig. 1 not embedded - three governance dimensions","Introduction","PACKAGING - not a scientific closure blocker","Final submission"),
 ("Fig. 2 not embedded - structured review process","Literature Review","PACKAGING - not a scientific closure blocker","Final submission"),
 ("Acknowledgment section absent from body; working-header checklist still lists it as an outstanding placeholder","Working header comment block","PACKAGING - stale checklist entry; no placeholder text exists in the body","Final submission"),
 ("Section numbering assumed I-VI for cross-references to Section IV","Empirical Characterisation; Generalisation","PACKAGING - verify numbering survives docx conversion","Final submission"),
]
write("submission-packaging-checklist.csv", PK, [dict(zip(PK,p)) for p in pk])

# --- repository drift ---
DR = ["file","stale_value","canonical_value","severity","recommended_action"]
dr = [
 ("CLAUDE.md","g_o daylight CAUTION 98.66% / 97.41%","98.71% / 97.66%","Repository hygiene - manuscript is correct","Separate bounded cleanup after reviewer closure"),
 ("scripts/canonical_figures.py (trailer prose only)","against a 22 kn threshold","21.6 kn","Repository hygiene - computation unaffected, prose only","Separate bounded cleanup after reviewer closure"),
 ("docs/canonical/appendix-c-formalisation.md","g_r : R>=0 -> S declared, while the WMO 95/96/99 route is described in adjacent prose as formally part of the specification and is implemented as a second argument in all eight canonical scripts","g_r : R>=0 x {0,1} -> S","CANONICAL - newly identified, same defect the manuscript just resolved","Bounded Appendix C typing repair - NOT performed here, out of scope for this task"),
]
write("repository-drift.csv", DR, [dict(zip(DR,d)) for d in dr])

# --- parser test ---
rep={}
for p in sorted(HERE.glob("*.csv")):
    raw=p.read_text(encoding="utf-8"); rdr=csv.reader(io.StringIO(raw))
    hdr=next(rdr); n=len(hdr)
    bad=[(i+2,len(r)) for i,r in enumerate(rdr) if len(r)!=n]
    rows=len(list(csv.DictReader(io.StringIO(raw))))
    rep[p.name]={"fields":n,"rows":rows,"malformed":bad,
                 "sha256_16":hashlib.sha256(p.read_bytes()).hexdigest()[:16],
                 "parse":"PASS" if not bad else "FAIL"}
(HERE/"parser-test-closure.json").write_text(json.dumps(rep,indent=2)+"\n")
for k,v in rep.items():
    print("%-5s %-38s fields=%d rows=%d sha=%s"%(v["parse"],k,v["fields"],v["rows"],v["sha256_16"]))
print("\nALL PASS:", all(v["parse"]=="PASS" for v in rep.values()))
