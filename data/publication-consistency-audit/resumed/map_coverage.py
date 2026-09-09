"""Continue the original numeric queue; preserve original locations and record reviewed dispositions.
This is a documentation coverage ledger, not an empirical replay or test of scientific truth.
"""
from pathlib import Path
import csv,json,re,collections,difflib
ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).resolve().parent
original=list(csv.DictReader((OUT.parent/'quantitative-coverage-queue.csv').open()))
edits=json.loads((OUT/'edit-log.json').read_text())
APP='docs/canonical/appendix-c-formalisation.md'
C8='data/c8/canonical-results-post-migration.txt; docs/canonical/report-c8-migration-2026-09-08.md'
seen=collections.Counter();mapped=[]
for number,row in enumerate(original,1):
 file,context,value,section=row['file'],row['context'],row['value'],row['section']
 matches=list(re.finditer(r'(?<![\w])\d+(?:,\d{3})*(?:\.\d+)?%?',context))
 key=(file,row['line']);idx=seen[key];seen[key]+=1
 span=matches[idx].span()
 citation=any(m.start()<=span[0] and span[1]<=m.end() for m in re.finditer(r'\[\d+\]',context))
 related=[e for e in edits if e['file']==file and e['before'] in context]
 current=(ROOT/file).read_text();retained=context in current
 status='current';action='retained';metric='structural notation';source=APP
 if row['note']=='comment/provenance':
  category='historical/provenance value';status='historical-labelled';source='Original editorial comment; provenance only';metric='historical editing record'
 elif section.lower()=='references' or citation or re.match(r'^\[\d+\]',context) or (len(value)==4 and value.isdigit() and 1900<=int(value)<=2030 and not ('hours' in context and value in ('2020','2024'))):
  category='citation/year';metric='citation identifier, bibliographic metadata or date';source='Manuscript reference list / local citation-notes-map; not a governance result'
 elif context.startswith('#') or ('Figure' in context and ('planned' in context.lower() or 'embedded image' in context)) or re.match(r'^\s*\d+[.)]',context) or (context.startswith('**') and any(w in context for w in ('Date started','Target submission','TABLE','Table','Fig.','Theorem','Definition','Property','Case'))):
  category='identifier';metric='section/table/figure/theorem identifier or planning date';source='Document structure; not an empirical quantity'
 elif 'hypothetical' in context.lower() or ('Domain Instantiation' in section and any(w in context for w in ('•','0600','1000','1400','Vessel category','above 22'))):
  category='hypothetical example';metric='Fig.4 input or threshold annotation';source=APP+' C.2; data/solar/solar-events-daily.csv:2024-03-20'
 elif ('under USD 50' in context and value=='50'):
  category='historical/provenance value';metric='unsupported hardware-cost ceiling';source='data/hardware-cost-provenance/resolution.json';status='stale';action='removed by authorised hardware-cost delta'
 elif section in ('Empirical Characterisation','Deployment Challenges and Limitations','Conclusion') or (('26 oscillation' in context or '3,661 transitions' in context or 'fourteen' in context or '5,416' in context) and not context.startswith('>')):
  category='prediction value' if 'predict' in context.lower() else 'result';metric='State/admissible-set characterisation; scope as stated in source text';source=C8
  if value=='0.953':source='docs/canonical/data-provenance.md:76; empirical-findings F-14';metric='Wave-model correlation on 28,501 valid overlapping pairs'
  if value=='95.8%':source='docs/canonical/empirical-findings-2026-09-06.md F-6: 5189/5416 old; '+C8+':3439/3661=93.9%';metric='scheduled transitions / all transitions, no hysteresis'
 elif 'Abstract' in context or (context.startswith('Third, the architecture is instantiated')):
  category='result';metric='headline characterization / registered outcomes';source=C8+'; docs/canonical/review-protocol.md'
 elif section in ('Introduction','Methodology','Synthesis: Cross-Paradigm Comparison and the Research Gap','Authority Allocation: Who Decides, Not What AI May Recommend','Adaptive Risk-Based Systems: The Closest Precedents'):
  category='sample size' if value in ('1,000','20','72','532','206','294','32','91','504') else 'figure/table value'
  metric='Literature sample/coding or reported literature quantity'
  source='docs/canonical/review-protocol.md; '+APP+' C.1'
  if value in ('1,000','20'):source='notes/Responsible AI in the Global Context- Maturity Model and Survey.md:15'
  if value=='91':source='notes/Collaborative Intelligence for Safety-Critical Industries- A Literature Review.md:10'
 elif context.startswith('>') and ('superseded' in context.lower() or 'provenance' in context.lower()):
  category='historical/provenance value';status='historical-labelled';metric='Explicitly labelled current/historical banner';source=C8
 elif any(w in section for w in ('Classification','Environmental State','Domain Instantiation')) or any(w in context for w in ('Hs_KIMO','Yaakob','Jeong','NORDFORSK','1.25 m','21.6','22 kn','mm/hr')):
  category='threshold' if any(w in context for w in ('g_w','g_r','g_o','g_t','threshold','interval','kn','mm/hr','|')) else 'figure/table value'
  metric='Configured threshold or cited hull-study value; hypothetical contrasts remain illustrative';source=APP+' C.1/C.2'
 elif any(w in context for w in ('O(1)','O(n)','O(','sin(','cos(','2π','G(','A_AI','RS(','S₁','S₂','∅','max_')) or any(w in section for w in ('Theorem','Formal','Governance','Algorithm','Complexity','Composite')):
  category='equation constant';metric='State/gate/set/algorithm notation, not a measured performance claim';source=APP+' C.2–C.8'
 else:
  category='identifier';metric='Structural/citation/planning numeral (reviewed in context); not a new empirical result';source='Document structure / cited-reference context'
 if related or (not retained and category not in ('citation/year','identifier')):
  if status!='historical-labelled':status='stale'
  action='changed' if related else 'changed within reviewed paragraph'
  if related:source='; '.join(dict.fromkeys(e['canonical_source'] for e in related))
 mapped.append({'queue_id':number,'file':file,'section':section,'original_line':row['line'],'value':value,'category':category,'metric_definition':metric,'canonical_source':source,'original_status':status,'action':action,'current_text':context,'evidence_note':'Original queue location retained. Exact before/after text is in edit-log.json; category is not an empirical validation claim.'})
assert len(mapped)==1227
with (OUT/'quantitative-coverage-mapped.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(mapped[0]));w.writeheader();w.writerows(mapped)
# Carry the original finding table forward without altering its historical rows.
prior=list(csv.DictReader((OUT.parent/'audit-table.csv').open()));continued=[]
for row in prior:
 related=[e for e in edits if e['file']==row['file'] and e['before'] in row['current_text']]
 if row['metric_name']=='hardware price ceiling':resolution='RESOLVED — Outcome C; parenthesis removed in 8c2e836'
 elif related:resolution='CORRECTED — see exact replacements in edit-log.json'
 elif row['status']=='PASS':resolution='RETAINED — prior verified passage / historical status'
 elif row['metric_name']=='Fig.4 illustrative time classification':resolution='CORRECTED — dated 2024-03-20 07:00 fixture'
 elif row['metric_name']=='totality theorem statement':resolution='CORRECTED — ideal theorem plus explicit operational resolution extension'
 else:resolution='REVIEWED — see policy and language ledger plus revised manuscript'
 continued.append({**row,'continuation_status':resolution,'edit_references':json.dumps(related,ensure_ascii=False)})
with (OUT/'audit-table-continuation.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(continued[0]));w.writeheader();w.writerows(continued)
summary={'original_queue_rows':len(original),'mapped_rows':len(mapped),'categories':dict(collections.Counter(r['category'] for r in mapped)),'scope':'Both working manuscripts; numeric tokens include non-results. Final newly added numbers checked separately against edit-log sources. Bibliography metadata is classified, not independently revalidated as a citation audit.'}
(OUT/'coverage-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
