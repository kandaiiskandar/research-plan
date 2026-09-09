"""Read-only consistency checks against frozen artefacts; no classifier execution."""
from pathlib import Path
import hashlib,json,csv,re
ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).resolve().parent
before=json.loads((OUT/'integrity-before.json').read_text())
changed=[p for p,h in before.items() if hashlib.sha256((ROOT/p).read_bytes()).hexdigest()!=h]
allowed={
 'publications/active/ipsci-2026/submissions/v3-revision/manuscript-v3.md',
 'publications/active/journal-1/submissions/v1-initial-submission/manuscript.md',
 'publications/active/ipsci-2026/supervisor-feedback-response.md',
 'publications/active/ipsci-2026/README.md','publications/active/journal-1/README.md',
 'publications/active/journal-1/section-5-plan.md','publications/active/journal-1/section-6-plan.md',
 'docs/canonical/architecture-illustration.md'}
assert set(changed)<=allowed,changed
reg=list(csv.DictReader((ROOT/'data/prediction-register.csv').open()))
assert len(reg)==24 and sum(r['status']=='CONFIRMED' for r in reg)==15 and sum(r['status']=='REFUTED' for r in reg)==9
cf=(ROOT/'publications/active/ipsci-2026/submissions/v3-revision/manuscript-v3.md').read_text()
j=(ROOT/'publications/active/journal-1/submissions/v1-initial-submission/manuscript.md').read_text()
body=re.sub(r'<!--.*?-->','',cf,flags=re.S)
abstract=next(p for p in body.split('\n\n') if p.startswith('*Abstract'))
conclusion=body.split('# Conclusion')[-1].split('##### References')[0]
for t in (abstract,conclusion):
 assert '5.81%' in t and '4.48%' in t
 assert 'fifteen' in t and 'nine refuted' in t
 assert 'three' in t and 'four' in t
 assert '7.7%' not in t and '6.0%' not in t and 'one departure morning' not in t
assert 'twenty-three were confirmed' not in body
assert '95.8%' not in body
for s in (body,j):
 assert '[0, 22]' not in s and '[17.0, 19.0)' not in s
 assert 'cause:Y' not in s and 'cause : Y' not in s
 assert 'under USD 50' not in s
 assert 'sunrise(date)' in s and 'sunset(date)' in s
 assert '2.8 m' in s and 'interpolat' in s
 assert 'unconditional' in s.lower()
 assert 'reasons' in s and 'policy' in s and 'not implemented' in s
# Matrix values are documentary comparisons to existing C-8, not recomputed replay statistics.
start=cf.index('| **C0 ungated** |');table=cf[start:].split('\n\n')[0]
rows=[line for line in table.splitlines() if line.startswith('| **C')]
vals=[[cell.strip() for cell in row.split('|')[2:-1]] for row in rows]
assert len(vals)==4
for x in range(4):
 for y in range(4):assert vals[x][y].replace('*','')==vals[y][x].replace('*','')
assert vals[0]==['—','42.88%','42.88%','48.69%']
assert '9,135 hourly records' in cf
assert '| *g*_r (rainfall) | 1.48% / 2.70% | 0.20% / 0.26% |' in cf
assert '3,439 (93.9%)' in cf and '222 to 199 (10.36%)' in cf
stages=json.loads((ROOT/'data/c5/c5-three-stage-deltas.json').read_text())['stages']
last=stages[-1]
assert (last['P09_total_transitions'],last['scheduled_transitions'],last['P10_non_scheduled'],last['P11_oscillations'],last['P12_reduction_pct'])==(3661,3439,222,26,10.36)
solar=next(r for r in csv.DictReader((ROOT/'data/solar/solar-events-daily.csv').open()) if r['date']=='2024-03-20')
assert solar['sunrise_hours']=='6.341591' and solar['sunset_hours']=='18.452345'
assert '6.341591 h, sunset 18.452345 h' in cf and '0700' in cf
# Fig.4 time examples agree with existing half-open definition using stored values.
for hour in (7,10,14):assert float(solar['sunrise_hours'])<=hour<float(solar['sunset_hours'])
assert '5,416 → 5,220 (threshold) → 5,201 (data) → 3,661 (g_t)' in cf
assert '1,529 under its registered 06:00–17:00 scope' in cf and 'astronomical daylight is 455' in cf
mapped=list(csv.DictReader((OUT/'quantitative-coverage-mapped.csv').open()))
assert len(mapped)==1227 and len({r['queue_id'] for r in mapped})==1227
assert all(r['canonical_source'] and r['category']!='unresolved' for r in mapped)
result={'status':'PASS','changed_existing_files':changed,'unchanged_existing_files':len(before)-len(changed),'register':{'entries':24,'CONFIRMED':15,'REFUTED':9},'queue_rows_mapped':len(mapped),'checks':['Frozen hashes','Headline and outcomes in abstract/conclusion','Table VII symmetry and C-8 values','TABLE VI rainfall metrics','95.8 historical / 93.9 current provenance','Proof intervals','Fig.4 stored solar-date check','P09 chain','P20 scopes','Reason-set and human authority statements'],'limits':'No replay, runtime engine test or solar citation closure. Numeric coverage categorisation and prose review complement these targeted checks.'}
after={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in before}
(OUT/'integrity-after.json').write_text(json.dumps(after,indent=2)+'\n')
(OUT/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
