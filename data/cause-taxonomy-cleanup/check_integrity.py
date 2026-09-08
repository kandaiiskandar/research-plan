"""Compare captured pre-cleanup bytes; never write frozen inputs."""
from pathlib import Path
import collections
import csv
import hashlib
import json
ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
before = json.loads((OUT/'integrity-before.json').read_text())
allowed = {'CLAUDE.md', 'docs/canonical/appendix-c-formalisation.md', 'docs/canonical/CHANGELOG.md'}
after = {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in before['hashes']}
changed = [p for p in after if after[p] != before['hashes'][p]]
assert set(changed) <= allowed, changed
rows = list(csv.DictReader((ROOT/'data/prediction-register.csv').open()))
statuses = dict(collections.Counter(r['status'] for r in rows))
assert len(rows) == 24 and statuses == {'REFUTED': 9, 'CONFIRMED': 15}
headline = next(x for x in (ROOT/'docs/canonical/empirical-findings-2026-09-06.md').read_text().splitlines() if '**Level 2 binding rate**' in x)
assert headline == before['headline_row'] and '**5.81%**' in headline and '**4.48%**' in headline
for p in ('CLAUDE.md', 'docs/canonical/appendix-c-formalisation.md'):
    text = (ROOT/p).read_text()
    assert 'Q → 𝒫({fault, hazard, policy})' in text
    assert 'Y → {fault, hazard}' not in text
    assert 'cause(y)' not in text
result = {'status': 'PASS', 'changed_existing_files': changed, 'hashes': after,
          'register_entries': len(rows), 'register_statuses': statuses, 'headline_row': headline,
          'unchanged_existing_files': len(after)-len(changed),
          'scope': 'All pre-snapshotted docs and active publications, all Python scripts, all solar artefacts, CLAUDE and prediction register. New cleanup artefacts are not part of the pre-snapshot.'}
(OUT/'integrity-after.json').write_text(json.dumps(result, indent=2)+'\n')
print('PASS: only allowed existing files changed; register and frozen scripts/data/publications unchanged.')
