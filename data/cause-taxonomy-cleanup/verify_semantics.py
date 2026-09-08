"""Standalone abstract specification check; not a runtime implementation.
Run: python3 data/cause-taxonomy-cleanup/verify_semantics.py
Outputs verification.json beside this file. No production imports or writes.
"""
import csv
import itertools
import json
from collections import Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
ENV = ('w', 'r', 'm', 'o')
SAFE, CAUTION, UNSAFE = 0, 1, 2
SCOPES = (('Go', 'Delay', 'DepartureTime', 'Duration'), ('Go', 'Delay'), ())
# Abstract identities of the unchanged state-indexed rule sets; no engine exists.
RULE_SETS = ('RS(SAFE)', 'RS(CAUTION)', 'empty RS(UNSAFE)')

def evaluate(values, excluded, time, vessel='small'):
    if vessel not in ('small', 'medium', 'big') or not set(excluded) <= set(ENV):
        raise ValueError('Startup refused; no classified result')
    entries = tuple((i, 'excluded' if i in excluded else 'fault' if x == 'fault' else 'valid',
                     SAFE if i in excluded else UNSAFE if x == 'fault' else x)
                    for i, x in zip(ENV, values))
    time_severity = UNSAFE if time == 'fault' else time
    state = max([entry[2] for entry in entries] + [time_severity])
    return state, {'entries': entries, 'time_valid': time != 'fault',
                   'night': time == UNSAFE, 'time_severity': time_severity}

def annotate(state, trace):
    labels = set()
    if any(status == 'fault' for _, status, _ in trace['entries']) or not trace['time_valid']:
        labels.add('fault')
    if any(status == 'valid' and severity > SAFE for _, status, severity in trace['entries']):
        labels.add('hazard')
    if trace['time_valid'] and trace['night']:
        labels.add('policy')
    return state, frozenset(labels)

def existing_governance(state):
    return (int(state != UNSAFE), SCOPES[state], RULE_SETS[state])

counts = Counter()
for flags in itertools.product((False, True), repeat=4):
    excluded = {i for i, flag in zip(ENV, flags) if flag}
    for values in itertools.product(('fault', SAFE, CAUTION, UNSAFE), repeat=4):
        for time in ('fault', SAFE, UNSAFE):
            state, trace = evaluate(values, excluded, time)
            projected, labels = annotate(state, trace)
            assert projected == state
            assert existing_governance(projected) == existing_governance(state)
            assert (not labels) == (state == SAFE)
            assert 'fault' not in labels or state == UNSAFE
            assert ('policy' in labels) == (time == UNSAFE)
            # Changing excluded raw inputs cannot change the result or reasons.
            replaced = tuple('fault' if i in excluded else x for i, x in zip(ENV, values))
            s2, q2 = evaluate(replaced, excluded, time)
            assert annotate(s2, q2) == (projected, labels)
            counts['+'.join(sorted(labels)) or 'empty'] += 1
assert sum(counts.values()) == 12288
assert len(counts) == 8

cases = [
 ('daylight + all weather SAFE', (0,0,0,0), set(), 0, 0, set()),
 ('daylight + wave CAUTION', (0,0,0,1), set(), 0, 1, {'hazard'}),
 ('daylight + wave UNSAFE', (0,0,0,2), set(), 0, 2, {'hazard'}),
 ('valid night + weather SAFE', (0,0,0,0), set(), 2, 2, {'policy'}),
 ('valid night + wave CAUTION', (0,0,0,1), set(), 2, 2, {'hazard','policy'}),
 ('valid night + wave UNSAFE', (0,0,0,2), set(), 2, 2, {'hazard','policy'}),
 ('wave fault + daylight', (0,0,0,'fault'), set(), 0, 2, {'fault'}),
 ('wave fault + valid night', (0,0,0,'fault'), set(), 2, 2, {'fault','policy'}),
 ('wind fault + wave UNSAFE + valid night', ('fault',0,0,2), set(), 2, 2, {'fault','hazard','policy'}),
 ('clock failure + weather SAFE', (0,0,0,0), set(), 'fault', 2, {'fault'}),
 ('date failure + weather SAFE', (0,0,0,0), set(), 'fault', 2, {'fault'}),
 ('solar lookup failure + weather SAFE', (0,0,0,0), set(), 'fault', 2, {'fault'}),
 ('excluded m absent + daylight SAFE', (0,0,'fault',0), {'m'}, 0, 0, set()),
]
with (ROOT/'data/solar/solar-events-daily.csv').open() as f:
    solar = next(row for row in csv.DictReader(f) if row['date'] == '2024-03-20')
sr, ss = float(solar['sunrise_hours']), float(solar['sunset_hours'])
for label, hour, expected_state, expected_labels in (
    ('exact valid sunrise', sr, 0, set()), ('exact valid sunset', ss, 2, {'policy'})):
    # Existing half-open specification; does not execute production g_t.
    time = SAFE if sr <= hour < ss else UNSAFE
    cases.append((label, (0,0,0,0), set(), time, expected_state, expected_labels))
results = []
for name, values, excluded, time, expected_state, expected_labels in cases:
    state, trace = evaluate(values, excluded, time)
    actual = annotate(state, trace)
    assert actual == (expected_state, expected_labels), name
    results.append({'case': name, 'state': ('SAFE','CAUTION','UNSAFE')[state],
                    'reasons': sorted(actual[1]), 'status': 'PASS'})
for name, vessel, excluded in [('missing vessel', None, set()), ('excluded time', 'small', {'t'})]:
    try:
        evaluate((0,0,0,0), excluded, 0, vessel)
    except ValueError:
        results.append({'case': name, 'state': None, 'reasons': None, 'status': 'PASS: startup refused'})
    else:
        raise AssertionError(name)
result = {'status': 'PASS', 'abstract_cases': sum(counts.values()), 'reason_set_counts': dict(sorted(counts.items())),
          'checks': ['state projection', 'G', 'A_AI', 'abstract RS identity', 'SAFE empty iff', 'fault implies UNSAFE',
                     'all eight subsets', 'excluded-input invariance', 'valid night distinct from time failure'],
          'required_cases': results, 'solar_boundary_fixture': {'date': solar['date'], 'sunrise_hours': sr, 'sunset_hours': ss},
          'limitations': 'Abstract contract verification only. No classifier replay, raw resolution, runtime logger, UI, rule engine or production solar execution tested. RS comparison uses existing state-indexed identities.'}
(OUT/'verification.json').write_text(json.dumps(result, indent=2)+'\n')
print(f'PASS: {sum(counts.values())} abstract cases; {len(results)} explicit cases; all 8 reason subsets.')
