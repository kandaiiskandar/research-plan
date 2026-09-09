"""Capture a stopped, partial publication audit. Does not edit source files.
Numeric extraction is a coverage queue, not completed metric verification.
"""
from pathlib import Path
import hashlib,json,csv,re,collections
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
before=json.loads((OUT/'integrity-before.json').read_text())
after={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in before}
assert before==after, 'Source files changed after audit stop'
reg=list(csv.DictReader((ROOT/'data/prediction-register.csv').open()))
assert len(reg)==24
statuses=dict(collections.Counter(r['status'] for r in reg))
assert statuses=={'REFUTED':9,'CONFIRMED':15}
(OUT/'integrity-after.json').write_text(json.dumps(after,indent=2)+'\n')
(OUT/'integrity-result.json').write_text(json.dumps({'status':'PASS','unchanged_files':len(before),'register_entries':len(reg),'register_statuses':statuses,'source_edits':0},indent=2)+'\n')
conf='publications/active/ipsci-2026/submissions/v3-revision/manuscript-v3.md'
journal='publications/active/journal-1/submissions/v1-initial-submission/manuscript.md'
app='docs/canonical/appendix-c-formalisation.md'
c8='data/c8/canonical-results-post-migration.txt'
findings=[]
def record(file, needle, metric, expected, status, rationale, kind='number'):
    lines=(ROOT/file).read_text().splitlines();section='Preamble'
    for n,line in enumerate(lines,1):
        if line.startswith('#'):section=line.lstrip('# ')
        if needle in line:
            findings.append({'file':file,'section':section,'line':n,'item_type':kind,'metric_name':metric,'current_text':line,'expected_canonical':expected,'status':status,'action':'retained' if status=='PASS' else 'flagged','rationale':rationale})
            return
    raise AssertionError((file,needle))
record(conf,'(under USD 50)','hardware price ceiling','No canonical price/requirement artefact located. A dated bill of materials or explicit canonical budget assumption is needed.','UNSUPPORTED','SC-3 stop: repetitions in the submitted v2.5 paper and supervisor response are not canonical provenance. No replacement value selected.')
record('publications/active/ipsci-2026/supervisor-feedback-response.md','(< $50)','hardware price ceiling','Same unresolved provenance as manuscript-v3.md:504','UNSUPPORTED','Supporting repetition; does not establish cost or a canonical requirement.')
record(conf,'*Abstract---','abstract headline and prediction outcomes','5.81% / 4.48%; 15 confirmed / 9 refuted; 3 SDR-001 flips and 4 earlier corrections. C-8 §§7–13.','STALE','Current abstract says 7.7% / 6.0% and 22/2; not corrected because the audit stopped.')
record(conf,'twenty-three were confirmed','prediction outcomes, Methods','data/prediction-register.csv: 24 entries, 15 CONFIRMED / 9 REFUTED','STALE','Known issue A confirmed; remains unedited after stop.')
record(conf,'The architecture is being developed as','prototype hysteresis','C-8 §9: 26 oscillations / 5 yr = 5.2 per year; 10.36% reduction in non-scheduled transitions','STALE','Prototype still says approximately fourteen per year and 6.2%; known issue B.')
record(conf,'Of 5,416 state transitions','Deployment Challenges transition metrics','C-8 §9: 3,661 total, 222 non-scheduled, 26 oscillations, 10.36% reduction','STALE','Contains 5,416 / 95.8% / 227 / 70 / fourteen / 6.2%. No global numeric replacement is warranted; 95.8% needs its own metric mapping.')
record(conf,'| **C0 ungated** |','TABLE VII C0 divergence row','C-8 output departure PRIMARY: 42.88% / 42.88% / 48.69%','STALE','24.64% / 24.64% / 32.36% retained in C0 row while reciprocal rows have current values; matrix is asymmetric.')
record(conf,'**TABLE VII.**','TABLE VII denominator','C-8 output: PRIMARY departure 05:00–09:00 n=9,135','STALE','Caption says 9,133; historical F-15 had that denominator. Same window label is not enough to reuse an earlier sample count.')
record(conf,'| *g*_r (rainfall) |','TABLE VI rainfall binding shares','Current daylight CAUTION: 1.48% / 2.70%, empirical findings §0a; all-hours shares require separate C-8 mapping','STALE','Daylight row retains 1.55% / 2.99%. Do not substitute daylight percentages into all-hours columns.')
record(conf,'Theorem 1 (Totality)','totality theorem statement',app+' C.7 ideal and operational distinction','AMBIGUOUS','The following proof mixes superseded intervals and ideal/raw-fault treatment; statement and scope require joint review.','definition')
record(conf,'g_w partitions ℝ≥0 into [0, 22]','totality proof partitions',app+' C.2: wind 21.6; rainfall numeric 10/20; time binary solar-event; C.1b operational totality','STALE','Proof still contains 22, categorical rainfall and fixed-clock twilight CAUTION.','definition')
record(conf,'[0600 - Early Morning]','Fig.4 illustrative time classification','canonical_gt: time needs date; 06:00 SAFE not established by the illustration','STALE','Fig.4 labels 0600 SAFE with no date. A corrected illustration must provide valid canonical time context.','definition')
record(conf,'Note: wind at 18 kt','Fig.4 wind boundary',app+' C.2 g_w: CAUTION above 21.6 kn','STALE','Caption note still says above 22 kt.','definition')
record(conf,'restricted advisory scope on 7.7%','interpretation headline','C-8 PRIMARY 5.81% / RESOLUTION 4.48% of departure-window hours','STALE','Current interpretation retains old rounded headline.')
record(conf,'**A discontinuous governance boundary','time transition consequence','C-8: 2→1,536 direct SAFE→UNSAFE; 1,545→0 time-driven SAFE→CAUTION; no physical-risk inference','PASS','Required design consequence and policy caveat already disclosed; does not imply entire Threats section passes.','claim')
record(conf,'Human override is unconditional','human final authority',app+' C.8.2: unconditional human authority','PASS','Explicitly retained even when AI withholds output.','claim')
record(conf,'*g*_m is a different case','retrospective marine-warning exclusion',app+' D={m} for historical replay; no archive; not runtime default','AMBIGUOUS','No-archive disclosure present; full exclusion/runtime distinction not completed before stop.','definition')
record(conf,'The governance layer therefore withdraws tactical','epistemic justification of CAUTION','Architecture policy versus evidence requires review against Appendix C.4','AMBIGUOUS','Epistemic support language needs classification; no material scientific-claim rewrite attempted.','claim')
record(conf,'The NIST AI Risk Management Framework','standards-to-policy mapping','External standard support must be distinguished from architecture policy','AMBIGUOUS','Risk-tier mapping is unverified in this stopped audit; no external research begun.','claim')
record(journal,'**⚠️ SDR-001 APPLIED','Journal 1 current-status banner','C-8: 5.81% / 4.48%, 15/9, binary solar time','PASS','Explicitly an active working manuscript despite v1-initial-submission path; later sections not certified aligned.','definition')
record(journal,'26 oscillation events (5.2/yr)','Journal 1 prototype plan hysteresis','C-8: 26 in 5 yr; 10.36%','PASS','Current matched metrics; section is a plan, not an implementation claim.')
record(journal,'3,661 transitions, the large majority','Journal 1 ablation plan transition metrics','C-8: 3,661 / 26 / 10.36%','PASS','Current matched figures; no replay needed.')
record(app,'| SAFE | w ≤ **21.6**','canonical wind boundary','21.6 kn SAFE upper boundary; 27.0 kn CAUTION upper boundary','PASS','Authoritative formal table explicitly amends 22→21.6.')
record('docs/canonical/architecture-illustration.md','| **w** — Wind speed','supporting wind table',app+' g_w table: 21.6 kn with canonical endpoint conventions','STALE','22-kn table is stale supporting prose. File explicitly defers formal definitions to Appendix C; preliminary SC-1 concern is not a confirmed unresolved canonical conflict.','definition')
record('docs/canonical/evaluation-design-rq4.md','| w (wind speed)','superseded scenario-design threshold','Historical-labelled by document-opening SUPERSEDED banner','PASS','Historical preservation applies. Initial suspicion of active SC-1 conflict withdrawn after banner check.','definition')
fields=['file','section','line','item_type','metric_name','current_text','expected_canonical','status','action','rationale']
with (OUT/'audit-table.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(findings)
# Extract only a coverage queue; no new metric evaluation after the stop.
queue=[]
for file in (conf,journal):
    section='Preamble';comment=False
    for n,line in enumerate((ROOT/file).read_text().splitlines(),1):
        if '<!--' in line:comment=True
        if line.startswith('#'):section=line.lstrip('# ')
        for match in re.finditer(r'(?<![\w])\d+(?:,\d{3})*(?:\.\d+)?%?',line):
            queue.append({'file':file,'section':section,'line':n,'metric_name':'not yet mapped: numeric token','value':match.group(),'canonical_expected':'PENDING — SC-3 stopped traceability review','classification':'ambiguous','audit_status':'AMBIGUOUS','context':line,'note':'comment/provenance' if comment else 'Numeric extraction only; may be citation, date, identifier, illustration or result; semantic inventory incomplete.'})
        if '-->' in line:comment=False
with (OUT/'quantitative-coverage-queue.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=list(queue[0]));w.writeheader();w.writerows(queue)
files=[]
for p in sorted(k for k in before if k.startswith('publications/')):
    if '/archive/' in p or '/submissions/v2-' in p or ('/ipsci-2026/submissions/v1-' in p): role='historical/frozen'
    elif 'session-log' in p or '/correspondence/' in p:role='historical record'
    elif p in (conf,journal):role='active working manuscript'
    elif p.endswith('.pdf'):role='supporting rendered asset; version not yet assessed'
    else:role='publication-supporting document'
    coverage='partially inspected' if p in {x['file'] for x in findings} or p.endswith('README.md') else 'inventoried only; audit not completed'
    files.append({'file':p,'role':role,'coverage':coverage,'action':'preserved; no edits'})
for p in sorted(k for k in before if k.startswith('docs/') and k.endswith('.md')):
    role='historical/provenance' if '/obsolete/' in p or '/archive/' in p or Path(p).name.startswith(('finding-','report-','cleanup-report-','approval-report-','session-log','decision-record-')) else 'canonical source or supporting document; scope review pending'
    if p=='docs/canonical/evaluation-design-rq4.md':role='explicitly superseded scenario design; later time annotation retained'
    files.append({'file':p,'role':role,'coverage':'partially inspected' if p in {x['file'] for x in findings} else 'inventoried only; audit not completed','action':'preserved; no edits'})
with (OUT/'file-inventory.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=list(files[0]));w.writeheader();w.writerows(files)
print('Evidence:',len(findings),'reviewed rows;',len(queue),'unresolved numeric tokens;',len(files),'file inventory rows')
