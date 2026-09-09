#!/usr/bin/env python3
"""Conference Reviewer Audit — artefact generation. All CSVs written through
csv.DictWriter (QUOTE_MINIMAL) and parser-tested after write."""
import csv, json, hashlib, pathlib, io

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent

def write(name, fields, rows):
    with open(HERE/name, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    return HERE/name

DIM = ["dimension","pre_edit","post_edit","basis"]
dims = [
 ("Problem significance","STRONG","STRONG","Documented fatality and accident statistics for the target population; gap is consequential not decorative"),
 ("Gap establishment","STRONG","STRONG","Four independent literature streams plus a measured baseline (C3 vs C1 = 0.00%)"),
 ("Novelty of the governance pair","STRONG","STRONG","No reviewed architecture conditions advisory scope on classified environmental state; TABLE II codes the comparison"),
 ("Positioning against related work","ADEQUATE","ADEQUATE","Closest precedents named and compared; C3 port is disclosed as a structural not a system comparison"),
 ("Formal specification clarity","WEAK","ADEQUATE","E/C/v conflation between Fig. 3, Domain Instantiation and Formal Structure corrected"),
 ("Proof correctness","STRONG","STRONG","Three proofs verified by exhaustive case analysis over a three-element set; no error found"),
 ("Proof assumption disclosure","STRONG","STRONG","A1-A4 stated explicitly; external validity notes that ML/LLM engines would need a different argument"),
 ("Architecture description","ADEQUATE","ADEQUATE","Layers and enforcement point are clear; Fig. 1 and Fig. 2 remain external image placeholders"),
 ("Algorithm specification","ADEQUATE","ADEQUATE","Three algorithms given; Algorithm 1 storm-indication branch remains a typed input not in the declared domain of r"),
 ("Evaluation design","ADEQUATE","ADEQUATE","Four conditions over a common record; admissible-set level only, disclosed"),
 ("Baseline adequacy","STRONG","STRONG","C0/C1/C3 span ungated, binary and the closest structural precedent"),
 ("Ablation and level isolation","STRONG","STRONG","C0-C1 and C0-C2 isolate Level 1 from Level 2; difference reproduces exactly"),
 ("Statistical treatment","ADEQUATE","ADEQUATE","Descriptive rates over a full population census; no inferential claim is made, correctly"),
 ("Data provenance","STRONG","STRONG","Two configurations reported; land/sea cell error corrected and documented; solar artefact frozen and hash-pinned"),
 ("Reproducibility","STRONG","STRONG","Every published figure regenerated live from canonical scripts during this audit"),
 ("Result interpretation restraint","STRONG","STRONG","Characterisation-not-validation stated in abstract, results and conclusion"),
 ("Threats to validity","STRONG","STRONG","Unusually candid; includes the architecture's own principal cost (2 to 1,536 step)"),
 ("Generalisation claims","ADEQUATE","ADEQUATE","Structural transfer argued; TABLE V instantiations are illustrative and labelled as such"),
 ("Internal consistency","WEAK","STRONG","Conclusion universal-impossibility claim contradicted the scoped mechanistic section; corrected"),
 ("Citation integrity","CRITICAL","STRONG","Two threshold sources named but uncited and absent from the reference list; two orphan references; all resolved"),
 ("Evidence-class discipline","ADEQUATE","STRONG","Solar bounds already separated model-vs-model from USNO comparison; g_r inert storm route now disclosed"),
 ("Figures and tables","ADEQUATE","ADEQUATE","TABLE VI and VII reproduce exactly; Fig. 4 values verified against TABLE IIIb; Fig. 1-2 not embedded in this file"),
 ("Contribution-evidence alignment","WEAK","ADEQUATE","Third contribution is measured; abstract now discloses the engine is unimplemented"),
 ("Limitations honesty","ADEQUATE","STRONG","Stipulated A_AI(CAUTION) added as a first-class limitation rather than left implicit"),
]
write("dimension-scores.csv", DIM, [dict(zip(DIM,d)) for d in dims])

ATT = ["id","attack","reviewer_severity","evidence_status","response_available","disposition"]
attacks = [
 ("A01","The vessel-conditional wave thresholds carry 98.71% of all CAUTION decisions, yet the two sources that ground them (Yaakob et al.; Jeong and Im) are named in prose with no citation and appear nowhere in the reference list. The paper's headline number rests on unciteable evidence.","CRITICAL","Sources exist in the project corpus with complete bibliographic records; claims verified against extraction notes","YES","FIXED - added as [39] and [40] and cited at all four use sites"),
 ("A02","The paper claims no architectural tactic has demonstrated formal positive safety impact. Indykov's score of 0 codes INSUFFICIENT EVIDENCE, and only two of sixteen tactics are discussed. Absence of evidence is presented as evidence of absence, generalised across a corpus.","CRITICAL","Source notes state the 0 code means insufficient evidence; AT4 is ambivalent; other tactics not assessed for Safety","YES","FIXED - narrowed in abstract and body to the two tactics and the weaker reading"),
 ("A03","The Conclusion asserts that no AI component, regardless of technique, can reliably self-restrict. The paper's own Mechanistic Basis section explicitly disclaims that generalisation, and the proposed system's AI component is a symbolic engine to which the LLM evidence does not apply.","CRITICAL","Internal contradiction between two sections of the same manuscript","YES","FIXED - Conclusion rescoped to match the body"),
 ("A04","A_AI(CAUTION) = {Go, Delay} is stipulated. The Design Principle promises a mapping from recommendation types to evidential requirements; that mapping is never performed. Why is Delay admissible when DepartureTime is not, given that Delay is itself a temporal judgement?","CRITICAL","No derivation exists in the manuscript or in Appendix C; the sets are defined by fiat","NO","RECORDED AS LIMITATION - added as the first of four limitations, including the Delay/DepartureTime objection stated in the reviewer's own terms"),
 ("A05","The AI is never run. The reasoning engine is unimplemented, the comparison is at the admissible-set level, and no AI(E) is ever observed. This is an evaluation of a classifier, presented as an evaluation of AI governance.","MAJOR","True and already disclosed in Result 6 and Threats to Validity, but absent from the abstract","PARTIAL","FIXED (disclosure) - abstract now states the engine is unimplemented and the comparison is admissible-set level; the underlying limitation stands"),
 ("A06","Fig. 3 and the Domain Instantiation call E an environmental observation vector containing v, while the Formal Structure states that v is a startup configuration and not an observation. The paper contradicts its own type signature.","MAJOR","Verified inconsistency across three locations","YES","FIXED - both locations aligned to C plus configured v"),
 ("A07","g_t transitions directly SAFE to UNSAFE 1,536 times against 2 previously. A paper arguing that graduated governance beats a binary step contains a component whose most predictable daily transition is a binary step.","MAJOR","Reproduced from canonical artefacts; already disclosed with the tension left intact","YES","NO EDIT - the existing Threats paragraph states the tension, its three bounding qualifications, and that the rule is a policy choice no source establishes. Nothing further is defensible"),
 ("A08","Algorithm 1 admits a storm indication as an UNSAFE trigger for g_r, but r is declared over the reals in mm/hr. The totality proof partitions only that numeric domain, and the phrase where available describes an unavailable required input that is silently skipped rather than mapped to bottom.","MAJOR","Appendix C records the route as formally specified but inert; zero thunderstorm codes in five years","PARTIAL","DISCLOSED - the inert route and its lower-bound consequence added to Result 4. The typing irregularity in the proof sketch is recorded as an open formal item, not papered over"),
 ("A09","The 50 km model's five-year maximum is compared against the 8 km model's 3.25-year maximum. The shorter record may simply have missed the peak, which would manufacture the resolution effect.","MAJOR","Checked directly: the ERA5 peak of 2.60 m occurs 2022-12-26, inside the MFWAM window; both maxima lie in the 28,501-hour overlap","YES","FIXED - period-matching stated explicitly, converting the objection into a verified strength"),
 ("A10","Two references are listed but never cited, which suggests the reference list was not checked against the body.","MAJOR","Confirmed by parse: [18] and [20] orphaned","YES","FIXED - both cited at accurate and substantively appropriate points"),
 ("A11","g_m is never measured, so the marine-warning component of a five-term classifier is inert throughout the entire evaluation. Four of five terms are effectively doing nothing.","MAJOR","True; g_m excluded, g_w activates twice and binds never","YES","NO EDIT - already stated three times, with the lower-bound consequence in bold and the retention argument given on transferability grounds"),
 ("A12","Level 2 binds in 5.81% of hours. Is a governance mechanism that engages one hour in seventeen worth an architecture?","MAJOR","The figure is what it is; the paper does not editorialise it","YES","NO EDIT - Result 1 states the rate plainly and Result 6 shows every comparator leaves those hours unrestricted. Arguing for significance would exceed the evidence"),
 ("A13","C3 is the authors' own port of Flehmig's topology onto their conditioning variable. A baseline built by the authors to lose is not a baseline.","MAJOR","The 0.00% result is a property of the classification-to-set mapping, invariant to data and configuration","YES","NO EDIT - the qualification paragraph already concedes this is a structural comparison, not a reproduction, and states the result is not a deficiency in the source framework"),
 ("A14","Fifteen of twenty-four predictions confirmed is a 62.5% hit rate. Registering predictions and then missing more than a third of them is not obviously a strength.","MODERATE","Register verified: 15 CONFIRMED / 9 REFUTED, with attribution preserved per entry","YES","NO EDIT - the paper reports the refutations and their attribution rather than the ratio, which is the correct handling; inflating the framing would be the error"),
 ("A15","Complexity is characterised for a rule engine that does not exist. O(n) over n rules is a definition, not a measurement.","MODERATE","Correct; no engine, no latency data","YES","NO EDIT - the third property in that section already distinguishes acquisition and engine execution from the fixed-size computations and states that no measured latency is reported"),
 ("A16","Fig. 1 and Fig. 2 are placeholders pointing at images in a different file. A reviewer cannot see the figure that establishes the three governance dimensions.","MODERATE","Confirmed in the working file","YES","NOT FIXED - image embedding is a submission-packaging step outside this audit's edit scope; recorded for the submission checklist"),
 ("A17","Fig. 4 sets the marine warning to advisory to reach CAUTION, using a component the evaluation declares unmeasured.","MODERATE","The figure is labelled Illustrative Values and the ocean component independently yields CAUTION at 1.1 m","YES","NO EDIT - the figure's own footnote already attributes mid-morning CAUTION to the advisory AND the sea state, and the sea state alone suffices"),
 ("A18","Result 2 says the remainder of UNSAFE hours has no weather component, then says this is not a mutually exclusive partition. Which is it?","MINOR","Both are true: the split by presence of a weather component is exhaustive, while provenance reasons overlap","YES","NO EDIT - the sentence distinguishes a binary split from a reason partition; rewording risks introducing an error for a cosmetic gain"),
 ("A19","The three systematic reviews are summed to 532 primary references, but the constituents count different things: papers reviewed, agent studies and cited references.","MINOR","206 + 294 + 32 = 532; units are heterogeneous","YES","NO EDIT - flagged for the authors; the figure is arithmetically correct and the constituents are itemised in the Methodology"),
 ("A20","The classifier is called deterministic and external to the AI, but a rule-based expert system is itself the AI being governed. The architecture governs symbolic AI with symbolic logic.","MINOR","The paper cites a neurosymbolic source for the engine and states the governance layer is outside the AI component","YES","NO EDIT - a fair conceptual point, but the separation the paper needs is between the governed component and the governing layer, which holds regardless of technique"),
]
write("reviewer-attacks.csv", ATT, [dict(zip(ATT,a)) for a in attacks])

FIN = ["id","classification","finding","location","action"]
findings = [
 ("F-R1-01","R1","Threshold sources Yaakob et al. and Jeong and Im named in prose, uncited, absent from reference list","Classification and role of vessel category; Domain Instantiation; Threats internal validity","Added [39] [40]; cited at four sites"),
 ("F-R1-02","R1","Indykov safety-score claim generalises an insufficient-evidence code across sixteen tactics","Abstract; Synthesis","Narrowed to the source's supported reading"),
 ("F-R1-03","R1","Conclusion asserts universal AI self-restriction impossibility, contradicting the paper's own scoped mechanistic section","Conclusion","Rescoped to LLM systems"),
 ("F-R1-04","R1","A_AI(CAUTION) stipulated, not derived; Design Principle promises a mapping never performed","Design Principle; Deployment Challenges and Limitations","Recorded as limitation - no evidence exists to answer it"),
 ("F-R2-01","R2","Abstract silent on the reasoning engine being unimplemented","Abstract","Disclosure clause added"),
 ("F-R2-02","R2","E typed inconsistently as an observation vector containing v across three locations","Fig. 3; Domain Instantiation","Aligned to C plus configured v"),
 ("F-R2-03","R2","g_r inert thunderstorm route and its lower-bound consequence undisclosed in the manuscript","Result 4","Disclosed"),
 ("F-R2-04","R2","Wave-maximum comparison open to a false period-mismatch objection","Result 5","Period-matching verified and stated"),
 ("F-R2-05","R2","Two orphan references","Reference list","Both cited appropriately"),
 ("F-R3-01","R3","Algorithm 1 storm-indication branch is an input outside the declared domain of r; totality proof partitions only the numeric domain","Theorem 1 proof sketch; Algorithm 1","Open formal item - recorded, not silently patched"),
 ("F-R3-02","R3","Fig. 1 and Fig. 2 are external image placeholders in this working file","Introduction; Literature Review","Submission-packaging item, outside edit scope"),
 ("F-R3-03","R3","532 primary references sums heterogeneous units","Introduction","Flagged; arithmetic correct, constituents itemised"),
 ("F-R4-01","R4","CLAUDE.md quotes g_o daylight CAUTION as 98.66/97.41; canonical_figures.py and the manuscript both give 98.71/97.66","Project instruction file","Project-file drift, not a manuscript defect - manuscript is correct"),
 ("F-R4-02","R4","canonical_figures.py reporting text still says 'against a 22 kn threshold'","scripts/canonical_figures.py trailer","Stale script prose; canonical threshold is 21.6 and the manuscript states it correctly"),
]
write("findings.csv", FIN, [dict(zip(FIN,f)) for f in findings])

ED = ["id","edit","rationale","invents_evidence"]
edits = [
 ("E1","Added references [39] Yaakob et al. 2015 and [40] Jeong and Im 2023; cited at four use sites","Recovers bibliographic records already held in the project corpus for sources the manuscript already relies on","NO - existing corpus records, claims verified against extraction notes"),
 ("E2","Narrowed the Indykov claim in abstract and body","Restates what the source's coding scheme supports","NO - weakens a claim"),
 ("E3","Rescoped the Conclusion's mechanistic claim to LLM systems","Removes an internal contradiction with the body","NO - weakens a claim"),
 ("E4","Aligned E/C/v typing in Fig. 3 and Domain Instantiation","Makes the paper consistent with its own Formal Structure","NO - notation only"),
 ("E5","Disclosed the inert thunderstorm route for g_r","Surfaces canonical finding F-11 into the manuscript","NO - adds a lower-bound caveat"),
 ("E6","Stated that both wave maxima fall inside the 28,501-hour overlap","Verified directly from the two archived series","NO - reports an existing property of existing data"),
 ("E7","Abstract now discloses the unimplemented reasoning engine","Aligns the abstract with the Threats section","NO - weakens a claim"),
 ("E8","Cited orphan references [18] and [20] at substantively appropriate points","Removes uncited list entries","NO - placement only"),
 ("E9","Added stipulated-A_AI(CAUTION) as the first of four limitations","Records a reviewer objection that existing evidence cannot answer","NO - adds a limitation"),
]
write("edits-applied.csv", ED, [dict(zip(ED,e)) for e in edits])

# ---- parser test: independent re-parse with strict field-count check ----
report = {}
for p in sorted(HERE.glob("*.csv")):
    raw = p.read_text(encoding="utf-8")
    rdr = csv.reader(io.StringIO(raw))
    hdr = next(rdr)
    n = len(hdr)
    bad = [(i+2, len(r)) for i, r in enumerate(rdr) if len(r) != n]
    rows = len(list(csv.DictReader(io.StringIO(raw))))
    report[p.name] = {"fields": n, "rows": rows, "malformed": bad,
                      "sha256_16": hashlib.sha256(p.read_bytes()).hexdigest()[:16],
                      "parse": "PASS" if not bad else "FAIL"}
(HERE/"parser-test.json").write_text(json.dumps(report, indent=2)+"\n")
for k, v in report.items():
    print(f"{v['parse']:5} {k:28} fields={v['fields']} rows={v['rows']} sha={v['sha256_16']}")
print("\nALL PASS:", all(v["parse"] == "PASS" for v in report.values()))
