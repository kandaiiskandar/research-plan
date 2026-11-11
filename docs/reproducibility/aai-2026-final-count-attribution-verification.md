# AAI 2026 — Verification of the Sensitivity Combination Count and Component Attribution

**Task:** M-6 independent verification of two remaining manuscript claims
**Date:** 8 October 2026
**Mode:** read-only. No experiment was executed, no scientific code was modified, no manuscript was edited, no Git state-changing command was used. One read-only static diagnostic was run; its full source is reproduced in section C.

---

## A. Executive Summary

Two claims were examined independently. They do not come out the same way, and the difference is in the *kind* of evidence available rather than in whether the numbers are right.

**Claim B — the 518 / 13 attribution — is MACHINE-VERIFIED, and the exclusivity is genuine.** Both preserved captures of the 2026-10-08 run print the figures directly, `518 + 13 = 531` closes exactly, and the percentages round to the reported 97.6% / 2.4%. More importantly, the implementation does **not** use a precedence rule. It counts, for each component independently, the hours where that component sits at CAUTION while the final state is CAUTION — so if two components were simultaneously at CAUTION, both would be counted and the column would over-sum. The script's own `ties` counter exists to detect exactly that case, and it reports **0**. Combined with max-severity aggregation — a final state of CAUTION entails at least one component at CAUTION — `ties = 0` means every one of the 531 hours had **exactly one** component at CAUTION. This is a *unique component trigger*, the strongest of the four interpretations the brief distinguishes, and not a precedence-assigned attribution. The manuscript's §V-C wording needs no change.

**Claim A — the 56-combination count — is STATICALLY VERIFIED, and the manuscript's description of it needs a wording clarification.** A read-only AST enumeration of the script's own configuration literals, which never imports the module and never touches the classifier or any dataset, reproduces the count exactly:

| | |
|---|---|
| Total evaluations performed (`run()` invocations) | **78** |
| Unique threshold tuples | **26** |
| Unique (threshold tuple, data configuration) | **52** |
| **Unique (threshold tuple, data configuration, denominator policy)** | **56** |
| Duplicate invocations | **22** |

So 56 is accurate and reproducible. Two things about the sentence that reports it are not.

1. **"Denominator policy" is doing more work than it looks.** The 56 breaks down as 52 departure-window + 2 daylight-only + 2 **common-period**. The common-period comparison restricts the *record* to the temporal intersection of the two wave datasets; it is an evaluation-period restriction rather than a within-day denominator rule. It does change the denominator, so the claim is true under a broad reading — but under the narrow reading a reader will apply, where "denominator policy" means departure-window versus daylight-only, the count is **54, not 56**. This is the one substantive finding on Claim A.

2. **"Each configuration is evaluated once rather than repeated" is literally false of the implementation.** 78 invocations collapse to 56 distinct combinations because **22 are recomputations of a configuration already evaluated** — the canonical tuple alone is re-evaluated five times per dataset, as it appears as the baseline and again as the mid-point of the rainfall sweep, the wind sweep, the wave sweep and the grid. The sentence's scientific intent is clearly that determinism removes any need for *replication*, which is correct and important; but as written it describes the code inaccurately. A reader checking 78 against 56 would find the clause contradicted.

Neither point touches a reported number. Both are wording.

**Repository integrity:** 15 recorded hashes re-verified, 0 mismatched, including the manuscript's own hash — its identity was confirmed against the recorded value, not from its filename. Branch `AMIT-v5`, HEAD `a7f77d8`, 0 modified tracked files. The working tree was already dirty before this task and still is; this task added one file.

---

## B. Repository and Evidence Integrity

| | |
|---|---|
| Branch | `AMIT-v5` |
| HEAD | `a7f77d8351ec94c586309d796aabd1230f4886dd` (2026-10-07 16:05:14 +0800) |
| Agreement with the run manifest | branch and HEAD both **MATCH** |
| Working tree before this task | **already dirty** — 45 `git status` entries, **0 modified tracked files** |
| Git operations used | `branch --show-current`, `rev-parse`, `log -1`, `status --short` — read-only only |

### Hashes

| Artefact | SHA-256 (first 16) | Recorded where | Result |
|---|---|---|---|
| `scripts/sensitivity/threshold_sensitivity.py` | `6ddaea583941134b` | run manifest, reproducibility manifest | **MATCH** |
| `scripts/canonical_gt.py` | `b330bf9f94e848aa` | both manifests | **MATCH** |
| `…threshold-sensitivity-20261008-stdout.txt` | `9323489a990399d0` | run manifest, 6,924 B | **MATCH** |
| `…threshold-sensitivity-20261008-sens_out.txt` | `db246059ffbf1ea5` | run manifest, 6,923 B | **MATCH** |
| `…threshold-sensitivity-20261008-stderr.txt` | `e3b0c44298fc1c14` | run manifest, 0 B | **MATCH** |
| `aai-2026-manuscript-v7-rewrite-v2.docx` | `f8769389a5e5c681` | reproducibility manifest, 419,027 B | **MATCH** |

**15 recorded hashes checked in total, 0 mismatched** (five canonical scripts, four input datasets, two guarded archived outputs, three preserved outputs, the manuscript). The manuscript's identity rests on the recorded hash, not on its name; the brief's caution is satisfied.

### Evidence inventory

Every file the brief lists is **present**: the sensitivity script, `canonical_gt.py`, both preserved output captures, the run manifest, the sensitivity verification report, the reproducibility manifest, the reproduction guide, and `docs/analysis/experiment-report-delta-l2.md`. Nothing had to be reported absent.

The two preserved captures are **independent records of the same run** — one is the shell's capture of stdout, the other the file the script wrote itself at line 150 — and both carry the attribution block with identical figures. That is a useful property for Claim B: the numbers are confirmed by two separate write paths, not one.

---

## C. Verification of the 56 Combinations

### C.1 The diagnostic

A static enumeration was run. It parses the script with `ast` and reads the configuration literals out of the syntax tree. It **does not import `threshold_sensitivity`** (its sweep literals live inside the `if __name__ == "__main__"` block and are not reachable by import anyway), does not import pandas or numpy, does not open any dataset, and never reaches the classifier, the replay or any Δ<sub>L2</sub> computation. No file was created: it was passed to `python3 -I` on stdin.

It confirms its own input by hashing the source it parsed: `6ddaea583941134b147956cc0d45cd785431ea7290643ba35a910a17f07a5730`, matching the recorded hash.

Its method: locate the `__main__` block; walk it statement by statement maintaining an environment of literal bindings; for every call to `run(...)`, record the enclosing `for` loops with their literal iterables, the second positional argument (the parameter expression), the first positional argument (which record), and whether a `mask=` keyword is present; then expand each call site over the Cartesian product of its enclosing loops and resolve `dict(CANON, …)` against the loop bindings to obtain a concrete threshold tuple.

> This is a **static enumeration**, not machine output from the canonical experiment. Per the evidence standard, it does not upgrade the claim to MACHINE-VERIFIED merely because a diagnostic printed a number.

```python
# READ-ONLY STATIC ENUMERATION DIAGNOSTIC (AST only).
# Does NOT import threshold_sensitivity, does NOT import pandas/numpy,
# does NOT read any dataset, does NOT invoke the classifier or any replay.
import ast, itertools, hashlib
from collections import Counter

SRC = 'scripts/sensitivity/threshold_sensitivity.py'
src = open(SRC).read()
print('script sha256:', hashlib.sha256(src.encode()).hexdigest())
tree = ast.parse(src)

mod = {}
for n in tree.body:
    if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
        try: mod[n.targets[0].id] = ast.literal_eval(n.value)
        except Exception:
            if isinstance(n.value, ast.Call) and getattr(n.value.func, 'id', '') == 'dict':
                mod[n.targets[0].id] = {k.arg: ast.literal_eval(k.value) for k in n.value.keywords}
CANON = mod['CANON']; CONFIGS = mod['CONFIGS']
KEYS = ('W_C','W_U','R_C','R_U','O_C','O_U')

main = None
for n in tree.body:
    if isinstance(n, ast.If) and "'__main__'" in ast.dump(n.test): main = n.body
assert main is not None

def softeval(node):
    try: return ast.literal_eval(node)
    except Exception: pass
    if isinstance(node, (ast.Tuple, ast.List)): return tuple(softeval(e) for e in node.elts)
    if isinstance(node, ast.Name): return '<name:' + node.id + '>'
    return '<expr>'

def lit(node, env):
    if isinstance(node, ast.Call) and getattr(node.func, 'attr', '') == 'items':
        base = getattr(node.func.value, 'id', None)
        if base in mod and isinstance(mod[base], dict): return list(mod[base].items())
    if isinstance(node, ast.Name) and node.id in env and isinstance(env[node.id], (list, tuple)):
        return list(env[node.id])
    if isinstance(node, (ast.Tuple, ast.List)): return [softeval(e) for e in node.elts]
    return None

sites = []
def walk(body, loops, env):
    env = dict(env)
    for st in body:
        if isinstance(st, ast.Assign) and isinstance(st.targets[0], ast.Name):
            try: env[st.targets[0].id] = ast.literal_eval(st.value)
            except Exception: env[st.targets[0].id] = st.value
        if isinstance(st, ast.For):
            items = lit(st.iter, env); tgt = st.target
            names = [e.id for e in tgt.elts] if isinstance(tgt, ast.Tuple) else [tgt.id]
            assert items is not None, f'unresolved loop iterable at line {st.lineno}'
            walk(st.body, loops + [(names, items, st.lineno)], env)
            continue
        for node in ast.walk(st):
            if isinstance(node, ast.Call) and getattr(node.func, 'id', '') == 'run':
                mask = next((k.value for k in node.keywords if k.arg == 'mask'), None)
                sites.append(dict(line=node.lineno, loops=list(loops),
                                  first=getattr(node.args[0], 'id', '<expr>'),
                                  pexpr=node.args[1],
                                  mask=None if mask is None else getattr(mask, 'id', ast.dump(mask)[:30]),
                                  env=dict(env)))
walk(main, [], {})

def resolve(pexpr, env, binding):
    node = pexpr
    if isinstance(node, ast.Name):
        if node.id == 'CANON': return tuple(CANON[k] for k in KEYS)
        v = env.get(node.id)
        if isinstance(v, dict): return tuple(v[k] for k in KEYS)
        if isinstance(v, ast.AST): node = v
    if isinstance(node, ast.Call) and getattr(node.func, 'id', '') == 'dict':
        base = dict(CANON)
        for kw in node.keywords:
            val = kw.value
            if isinstance(val, ast.Name) and val.id in binding: base[kw.arg] = binding[val.id]
            else: base[kw.arg] = ast.literal_eval(val)
        return tuple(base[k] for k in KEYS)
    raise AssertionError('unresolved param expr')

rows = []
for s in sites:
    iters = [d[1] for d in s['loops']]; namesets = [d[0] for d in s['loops']]
    for combo in (itertools.product(*iters) if iters else [()]):
        binding = {}
        for names, val in zip(namesets, combo):
            if len(names) == 1: binding[names[0]] = val
            else:
                for nm, v in zip(names, val): binding[nm] = v
        tup = resolve(s['pexpr'], s['env'], binding)
        denom = ('daylight-only' if s['mask'] == 'm2'
                 else 'common-period' if s['first'] == 'sub' else 'departure-window')
        cfg = str(binding.get('cfg') or binding.get('tag') or '?').replace(' wave model', '')
        rows.append(dict(line=s['line'], cfg=cfg, tup=tup, denom=denom))

k2 = {r['tup'] for r in rows}
k3 = {(r['tup'], r['cfg']) for r in rows}
k4 = {(r['tup'], r['cfg'], r['denom']) for r in rows}
print('1. TOTAL evaluations performed (run() invocations)      :', len(rows))
print('2. UNIQUE threshold tuples                              :', len(k2))
print('3. UNIQUE (threshold tuple, dataset config)             :', len(k3))
print('4. UNIQUE (threshold tuple, dataset config, denominator):', len(k4))
print('5. DUPLICATE invocations (total - unique on key 4)      :', len(rows) - len(k4))
```

### C.2 The seven `run()` call sites

Every evaluation in the script passes through `run()`. `classify()` is called only from inside `run()` (line 50), so no configuration is evaluated by another path. The enumeration found seven call sites:

| Source line | Enclosing loops | Invocations | Denominator | Record |
|---|---|---|---|---|
| 74 | data config (2) | 2 | departure window | full |
| 105 | data config (2) × `R_C` (5) | 10 | departure window | full |
| 109 | data config (2) × `W_C` (5) | 10 | departure window | full |
| 115 | data config (2) × wave pair (6) | 12 | departure window | full |
| 121 | data config (2) | 2 | **daylight-only** (`mask=m2`) | full |
| 134 | data config (2) × `R_C` (5) × wave pair (4) | 40 | departure window | full |
| 147 | wave model (2) | 2 | departure window | **common period** |
| **Total** | | **78** | | |

### C.3 Dimensions actually varied

| Dimension | Values | Source |
|---|---|---|
| Environmental-data configuration | `PRIMARY` (`raw_marine_era5_sea.csv`), `RESOLUTION` (`raw_marine_mfwam.csv`) | line 20 |
| Wind CAUTION `W_C` | 18.0, 20.0, **21.6**, 22.0, 25.0 — one-at-a-time | line 108 |
| Rainfall CAUTION `R_C` | 5.0, 7.5, **10.0**, 15.0, 19.9 — one-at-a-time, and factorial in the grid | lines 104, 131 |
| Wave `(O_C, O_U)` | (0.75, 1.25), **(1.0, 1.25)**, (1.25, 1.5), (1.0, 1.9), (1.4, 2.8), (1.5, 3.5) — one-at-a-time; the last four also factorial in the grid | lines 112, 128 |
| Denominator / evaluated set | departure window; departure window ∩ astronomical daylight; departure window ∩ common record period | lines 47, 119–121, 144–147 |
| **Not varied** | `W_U` = 27.0, `R_U` = 20.0, both governance mapping tables, `g_m` ≡ SAFE, the departure window 05:00–09:00 | lines 19, 39, 47, 62–63 |

**The sweep is one-at-a-time, with one factorial block.** The `R_C` and `W_C` sweeps and the wave sweep each vary a single dimension from canonical. Only the combined grid (lines 131–134) is factorial, and only over two of the three dimensions: 5 `R_C` values × 4 wave pairs. The wind dimension is never combined with anything, so there is no full factorial over all three.

**Vessel class is not an independent dimension.** The vessel classes are expressed entirely as `(O_C, O_U)` pairs — small (1.0, 1.25), medium (1.4, 2.8), large (1.5, 3.5) — and are therefore already inside the threshold tuple. Counting vessel class as a separate dimension would double-count, so the brief's instruction not to introduce unsupported dimensions rules it out.

### C.4 The counting key, and why

The counting key is the triple **(environmental-data configuration, threshold tuple, denominator policy)**, where the threshold tuple is `(W_C, W_U, R_C, R_U, O_C, O_U)`.

The justification is that Δ<sub>L2</sub> is a *frequency*, so its value is fixed by three things and only three: which record is classified, by what rules, and over which hours the resulting states are counted. Change any one and the measured number changes. Two evaluations sharing a threshold tuple but differing in denominator must therefore be counted as distinct — the canonical tuple yields **5.81%** on the departure window and **9.59%** on the daylight-only denominator, which is not one result reported twice but two different measurements. Conversely, two evaluations agreeing on all three produce bit-identical output and are one combination however many times the script computes them.

### C.5 The count

| Counting key | Count |
|---|---|
| 1. Total evaluations performed (`run()` invocations) | **78** |
| 2. Unique threshold tuples | **26** |
| 3. Unique (threshold tuple, data configuration) | **52** |
| 4. **Unique (threshold tuple, data configuration, denominator policy)** | **56** |
| 5. Duplicate invocations (78 − 56) | **22** |

Decomposition of the 56 by denominator:

| Denominator | Count |
|---|---|
| departure window | 52 (26 threshold tuples × 2 data configurations) |
| daylight-only | 2 (canonical tuple × 2 data configurations) |
| common period | 2 (canonical tuple × 2 wave models) |
| **Total** | **56** |

Symmetrically, 28 per data configuration (26 + 1 + 1), × 2 = 56.

### C.6 Duplicates

The 22 duplicate invocations are all baseline or shared-cell recomputations, 11 per data configuration:

| Threshold tuple | Invocations | Why repeated |
|---|---|---|
| canonical (21.6, 27.0, 10.0, 20.0, 1.0, 1.25) | **5** | baseline, plus the mid-point of the `R_C` sweep, the `W_C` sweep, the wave sweep and the grid |
| (…, `R_C` = 5.0 / 7.5 / 15.0 / 19.9, wave (1.0, 1.25)) | 2 each | `R_C` sweep, then the grid's first wave column |
| (…, `R_C` = 10.0, wave (1.0, 1.9) / (1.4, 2.8) / (1.5, 3.5)) | 2 each | wave sweep, then the grid's canonical `R_C` row |

Every duplicate is a recomputation of an identical configuration, so each yields an identical result — which incidentally is a small determinism demonstration inside the run itself.

**Nothing is counted that is not evaluated, and nothing evaluated is dropped.** All 56 keys derive from actual `run()` call sites expanded over their actual loop literals; the 78 invocations collapse onto exactly those 56 keys with no residue.

### C.7 Does the manuscript's wording describe this?

> "the canonical sensitivity script evaluates 56 distinct combinations of environmental-data configuration, threshold setting and denominator policy, of which this paper reports a subset"

The three named dimensions are precisely the counting key, and the figure is exactly right. The phrase "of which this paper reports a subset" is also accurate — the paper reports 8 of the 56, and does not report the common-period figures at all.

The difficulty is the scope of "denominator policy". It unambiguously covers the daylight-only variant. Whether it covers the common-period restriction is a judgement:

- **For:** the restriction does change the set of hours in the denominator, from 9,135 to 5,935 for PRIMARY.
- **Against:** it restricts the *record period* — the temporal intersection of the two wave datasets — rather than applying a rule about which hours of a day count. The script itself calls that block "COMMON-PERIOD COMPARISON (de-confounds wave model from record length)", not a denominator policy. A reader taking "denominator policy" to mean departure-window versus daylight-only would count **54** and conclude the manuscript is off by two.

So **56 is correct under a broader reading of "denominator policy" than the sentence makes explicit.** The count is not wrong; the description is under-specified by exactly the two common-period evaluations. Section F proposes the minimal fix.

A second, smaller problem sits in the same sentence. "Because the replay is deterministic, each configuration is evaluated once rather than repeated" is contradicted by the implementation: 22 of the 78 invocations re-evaluate a configuration already evaluated, and the canonical tuple is computed five times per dataset. The intended claim — that determinism makes replication unnecessary — is correct and worth keeping; the literal claim about the script is not.

---

## D. Verification of the 518 / 13 Attribution

### D.1 Numerical accounting

Both preserved captures carry the PRIMARY attribution block identically — stdout lines 16–22 and `sens_out` lines 17–22:

```
  COMPONENT ATTRIBUTION at canonical (departure window)
    g_w: enters CAUTION      1   is binding component of final CAUTION      0
    g_r: enters CAUTION     15   is binding component of final CAUTION     13
    g_o: enters CAUTION    877   is binding component of final CAUTION    518
    g_t: enters CAUTION      0   is binding component of final CAUTION      0
    g_m: enters CAUTION      0   is binding component of final CAUTION      0
    ties (>1 component at max during CAUTION): 0
```

| Quantity | Manuscript | Preserved output | Result |
|---|---|---|---|
| Total PRIMARY CAUTION hours | 531 | **531** (stdout:6, `CAUTION 5.81%` of n = 9,135) | **MATCH** |
| Ocean-state attribution | 518 | **518** | **MATCH** |
| Rainfall attribution | 13 | **13** | **MATCH** |
| Wind attribution | 0 | **0** | **MATCH** |
| Time attribution | 0 | **0** | **MATCH** |
| Marine-warning attribution | 0 | **0** | **MATCH** |
| Ties | — | **0** | — |
| Sum | 518 + 13 = **531** | closes exactly | **MATCH** |
| Ocean-state share | 97.6% | 518 / 531 = **97.5518%** → 97.6% | **MATCH** |
| Rainfall share | 2.4% | 13 / 531 = **2.4482%** → 2.4% | **MATCH** |

As the brief cautions, arithmetic closure alone proves nothing — a precedence rule would also produce a closing sum. The algorithm therefore has to be read.

### D.2 The attribution algorithm

Lines 90–99, verbatim:

```python
# component attribution at canonical
cm = {k: v[m.values] for k, v in c.items()}
sD = S[m.values]
P("\n  COMPONENT ATTRIBUTION at canonical (departure window)")
for k in ("g_w", "g_r", "g_o", "g_t", "g_m"):
    enters = int((cm[k] == CAUTION).sum())
    binds = int(((sD == CAUTION) & (cm[k] == sD)).sum())
    P(f"    {k}: enters CAUTION {enters:>6,}   is binding component of final CAUTION {binds:>6,}")
ties = int(((sD == CAUTION) & (np.column_stack([cm[k] for k in ("g_w","g_r","g_o","g_t","g_m")]) == CAUTION).sum(axis=1) > 1).sum())
P(f"    ties (>1 component at max during CAUTION): {ties:,}")
```

| Question from the brief | Answer, from the code |
|---|---|
| Same hours as the manuscript? | **Yes.** `m = dep_mask(d)` = `(hour >= 5) & (hour <= 9)` over the full PRIMARY record; `cm` and `sD` are both masked by `m.values`. 9,135 departure-window hours, 531 CAUTION — the same population the manuscript names. |
| Same state classifier? | **Yes.** `S` and `c` both come from the single `classify(d, CANON)` call at line 50 inside `run`, which calls `components()`. Attribution and the headline Δ<sub>L2</sub> are computed from the *same* classification pass, not a re-derivation. |
| Exactly one component per CAUTION hour? | **Yes, empirically** — see D.3. Not by construction. |
| Can multiple components trigger CAUTION at once? | **Yes, in principle.** Nothing in `components()` prevents it; `g_w`, `g_r` and `g_o` are independent `np.where` expressions over different variables. |
| How are ties detected? | Line 98 stacks all five component arrays, counts how many equal CAUTION in each hour, and counts the CAUTION hours where that count exceeds 1. |
| How are ties handled? | **They are not resolved — they are counted and reported.** There is no precedence rule, no `argmax`, no ordering of components. Had any tie occurred, both components would have been counted in their own `binds` totals and the column would have over-summed past 531. |
| Does a higher-severity component override a CAUTION trigger? | **Yes, and this is the `enters` / `binds` gap.** `g_o` enters CAUTION in 877 hours but binds in only 518; the other 359 are hours where some component sat at UNSAFE, so max-severity aggregation made the final state UNSAFE. Same for `g_r` (15 → 13) and `g_w` (1 → 0). The dominant cause is the night→UNSAFE rule inside the 05:00–09:00 window. |
| Does the night UNSAFE policy affect the attribution denominator? | **Not the denominator, but it does shape the numerator set.** The denominator is the 531 CAUTION hours (or the 9,135 departure hours). Night hours are classified UNSAFE and so cannot be CAUTION at all, which is why 359 of the 877 ocean-state CAUTION conditions never reach attribution. The 97.6% / 2.4% split is therefore conditional on the night policy. |
| Is marine-warning exclusion respected? | **Yes.** Line 39, `g_m = np.full(len(d), SAFE)` — held at the least-severe value for every row, the declared exclusion `D = {m}`. It can never be CAUTION, so its `enters` and `binds` are both 0 by construction. |
| Final-state attribution or component-level presence? | **Both are reported, as separate columns, and the manuscript uses the right one.** `enters` is component-level presence; `binds` is final-state attribution. The manuscript's 518 / 13 are the `binds` figures, which is what "accounted for 518 of those 531 hours" requires. |

### D.3 Is this a genuine exclusive partition?

Yes — and the reasoning matters more than the arithmetic.

The final state is `np.max` over the five components (line 44). So a final state of CAUTION implies **at least one** component at CAUTION and **none** at UNSAFE. The `ties` counter reports how many CAUTION hours had **more than one** component at CAUTION; it is **0**. At least one, and not more than one, gives **exactly one** component at CAUTION in every one of the 531 hours.

Because `binds` is computed independently per component with no precedence rule, the column sum equals the total number of (hour, component-at-CAUTION) pairs among CAUTION hours. With exactly one component per hour that sum must be 531, and it is: 0 + 13 + 518 + 0 + 0 = 531. The closure is not a coincidence to be explained away; it is entailed by `ties = 0`, and it would have failed visibly had any hour carried two triggers.

Against the four interpretations the brief asks to be distinguished:

| Interpretation | Supported? |
|---|---|
| **Unique component trigger** — exactly one component was at CAUTION in each attributed hour | **YES.** This is what the evidence supports. |
| Multiple simultaneous triggers | **NO** — `ties = 0` excludes it for this record and configuration. |
| Precedence-assigned attribution | **NO** — no precedence rule exists in the code. |
| Final-state attribution | **YES, and this is the right reading of it.** Attribution is conditioned on the final state being CAUTION (`sD == CAUTION`), so component-level CAUTION conditions overridden to UNSAFE are correctly excluded. |

Two qualifications belong on this result. First, exclusivity is an **empirical property of this record under this configuration**, not a structural guarantee: the components could overlap on other data or other thresholds, and the script's `ties` counter exists precisely because the author did not assume they could not. Second, the same holds in RESOLUTION — `g_o` 253, `g_r` 13, ties 0, 253 + 13 = 266 — so the property is not an artefact of one dataset. (RESOLUTION's split is 95.1% / 4.9%, which the manuscript does not report; only the PRIMARY split is claimed.)

For completeness: a *different* diagnostic elsewhere in the repository, `diagnostic_binding.py`, produces overlapping "at max" counts that sum past 100%, and the archived September capture contains those rather than this exclusive split. The two are answering different questions; only `threshold_sensitivity.py` produces the exclusive partition the manuscript reports. An earlier audit in this series stated that no script in the repository produces it. That statement was wrong, and this verification supersedes it.

### D.4 The three zeros

The manuscript distinguishes three kinds of zero. The code supports all three distinctions.

| Component | Manuscript | Code and output | Verdict |
|---|---|---|---|
| **Wind `g_w`** | "No PRIMARY CAUTION hour was attributed to wind, which is an empirical negative finding for the evaluated record" | `binds = 0` but `enters = 1` — wind did reach CAUTION in one departure-window hour, and that hour was classified UNSAFE overall. `g_w` is a live three-valued classifier (line 34). | **Correct, and precisely worded.** "Attributed to" is exactly the `binds` column. A looser phrasing such as "wind never reached CAUTION" would have been false. |
| **Time `g_t`** | "emits no CAUTION by construction, so its zero is definitional" | `canonical_gt.g_t` returns only SAFE or UNSAFE (line 105 of `canonical_gt.py`); its docstring states `Im(g_t) = {SAFE, UNSAFE}`, CAUTION not in the image, by deliberate design. `enters = 0` is structural. | **Correct.** |
| **Marine `g_m`** | "structurally excluded, and its zero reflects unavailability rather than evidence that marine warnings never bind" | Line 39 pins it at SAFE for every row. | **Correct, and it avoids the error the brief warns against** — the zero is not read as evidence about reality. §V-D reinforces this: "the reported binding frequencies are conditional on its exclusion and cannot be interpreted as lower bounds." |

None of the three zeros arises from attribution precedence, since no precedence rule exists. Wind's zero arises from severity override; time's from the classifier's image; marine's from the declared exclusion.

---

## E. Evidence Classification

| Claim | Evidence | Classification | Verdict |
|---|---|---|---|
| **56 distinct combinations** | Not emitted by the canonical run. Static AST enumeration of the script's own configuration literals (section C.1), reproducing 78 invocations → 56 unique on (data config, threshold tuple, denominator). | **STATICALLY VERIFIED** | Count **accurate and reproducible**. The description "denominator policy" needs clarification: 56 holds only if the common-period restriction is counted as a denominator policy; on the narrow reading it is 54. |
| **518 ocean-state CAUTION hours** | `data/c8/reproducibility-verification/threshold-sensitivity-20261008-stdout.txt:19`, and independently `…-sens_out.txt:19`; algorithm at source lines 91–97. | **MACHINE-VERIFIED** | Correct. 518 / 531 = 97.5518% → 97.6% as reported. |
| **13 rainfall CAUTION hours** | stdout:18 and `sens_out`:18; same algorithm. | **MACHINE-VERIFIED** | Correct. 13 / 531 = 2.4482% → 2.4% as reported. |
| **Zero attribution ties** | stdout:22 and `sens_out`:22, `ties … : 0`; detection logic at source line 98. | **MACHINE-VERIFIED** | Ties genuinely 0. With max-severity aggregation this entails exactly one component at CAUTION per attributed hour, so the partition is exclusive by *unique component trigger*, not by precedence. Empirical for this record and configuration, not structural. |
| **Other component zeros** | stdout:17, :20, :21; `g_w` line 34, `g_t` in `canonical_gt.py`, `g_m` line 39. | **MACHINE-VERIFIED** for the figures; **STATICALLY VERIFIED** for the three *reasons* (empirical / definitional / excluded), which come from reading the classifiers. | All three correct as the manuscript characterises them. Note that wind's `enters = 1` while `binds = 0` — the manuscript's "attributed to" wording accommodates this; a stronger claim would not. |

The two verdicts are deliberately kept apart: Claim B rests on preserved machine output, Claim A on a static reading of the source. A diagnostic printing 56 does not make 56 machine-generated.

---

## F. Manuscript Wording Assessment

**The DOCX was not edited.** Two changes are proposed, both in the same Section IV sentence. Claim B's wording needs nothing.

### F.1 Scope of "denominator policy" — terminology clarification

**Exact existing sentence** (§IV, paragraph beginning "The procedure is a deterministic historical replay"):

> Because the replay is deterministic, each configuration is evaluated once rather than repeated: the canonical sensitivity script evaluates 56 distinct combinations of environmental-data configuration, threshold setting and denominator policy, of which this paper reports a subset, and the four governance configurations are applied to each classified record rather than replayed separately.

**Proposed replacement:**

> Because the replay is deterministic, no configuration needs replication: the canonical sensitivity script evaluates 56 distinct combinations of environmental-data configuration, threshold setting and evaluation-set policy — the departure window, a daylight-only denominator, and a common-period record restriction — of which this paper reports a subset, and the four governance configurations are applied to each classified record rather than replayed separately.

**Scientific justification.** Two independent problems are fixed with one edit.

*"Denominator policy" → "evaluation-set policy", with the three values named.* The 56 decomposes as 52 + 2 + 2, and the final 2 are the common-period comparison, which restricts the record period rather than applying a within-day denominator rule. Naming the three values makes the count self-verifying: a reader can check 26 × 2 + 2 + 2 = 56 without having to guess what the dimension contains. As written, a reader applying the narrow reading of "denominator policy" would count 54 and believe the figure wrong.

*"each configuration is evaluated once rather than repeated" → "no configuration needs replication".* The script performs 78 invocations for 56 distinct combinations; 22 are recomputations and the canonical tuple is evaluated five times per dataset. The literal claim is false of the implementation, while the intended claim — determinism removes the need for replicate runs — is both true and the one the paragraph is making. The replacement keeps the intent and drops the false detail. It also keeps the sentence's length unchanged in substance, so the six-page layout is not disturbed.

**Evidence.** Source lines 74, 105, 109, 115, 121, 134, 147 (the seven `run()` sites); lines 104, 108, 112, 128, 131 (the sweep literals); lines 47 and 119–121 (the two within-day denominators); lines 144–147 (the common-period restriction). Static enumeration output in section C.5: 78 / 26 / 52 / 56 / 22.

### F.2 Claim B — no change required

> Within the PRIMARY departure window, 531 hours were classified CAUTION, and attribution across the component classifiers is uneven. The ocean-state component accounted for 518 of those 531 hours, or 97.6%, and the rainfall component for the remaining 13, or 2.4%. These are attributions of CAUTION classification, not of incidents or unsafe outcomes, none of which is observed here.

> The three remaining components register zero, for three different reasons, and the distinction matters. No PRIMARY CAUTION hour was attributed to wind, which is an empirical negative finding for the evaluated record and is separate from the structural zero reported for the wind threshold range above. The time component emits no CAUTION by construction, so its zero is definitional. The marine-warning component is structurally excluded, and its zero reflects unavailability rather than evidence that marine warnings never bind.

Every figure matches the preserved output, every interpretation matches the code, and the wording is already careful at the two places where it could have gone wrong: "accounted for 518 of those 531 hours" correctly uses final-state binding rather than component presence, and "attributed to wind" correctly leaves room for the one wind-CAUTION hour that was overridden to UNSAFE. **No change.**

One **optional** addition, offered only because it strengthens a claim rather than correcting one: the manuscript does not say that the attribution is exclusive, and it now can — `ties = 0` establishes that each of the 531 hours had exactly one component at CAUTION. A clause such as "each CAUTION hour was triggered by exactly one component" would be supported by the preserved output. Against adding it: the paper is at its page limit, the claim is empirical rather than structural and would need that caveat, and the existing sentence is not weaker for its absence. Recommended only if space allows.

---

## G. Remaining M-6 Limitations

### Resolved by this verification

1. **The 56-combination count is no longer unsupported.** It moves from grade E — no artefact anywhere in the repository stated it — to a reproducible static enumeration with its method and code recorded. The earlier instrumentation that established it was not retained; this one is.
2. **The exclusive 518 / 13 attribution is machine-verified**, and the exclusivity interpretation is settled as *unique component trigger* rather than precedence assignment. This closes the last open sensitivity-chain evidence gap from the M-6 manifest audit.
3. **An error in an earlier audit in this series is corrected.** The claim that no script produces the exclusive split was wrong; `threshold_sensitivity.py` lines 91–99 produce it.

### Open, and unrelated to these two claims

4. **The 56-count is static, not machine-generated.** The canonical script still prints no combination count. Adding one line to emit it would make the manuscript's figure machine-verifiable; that is a source-code change and was not made.
5. **The ephemeral-output defect persists.** Line 150 still writes to `/tmp/sens_out.txt`. The 2026-10-08 run was captured by redirection and a post-run copy; any future run needs the same workaround or a one-line path change.
6. **The historical September run cannot be byte-compared.** Its output is gone. Agreement with the manuscript is established at the 2-decimal printed precision, not bitwise.
7. **The historical execution environment is partly unknown** — Python minor version, OS, architecture. pandas 2.3.3 and numpy 2.2.6 match.
8. **Exclusivity is empirical, not structural.** `ties = 0` holds for this record under the canonical configuration. Nothing establishes that components cannot overlap on other data, and the manuscript should not be read as claiming otherwise.
9. **Untouched by this task:** the Copernicus product lineage for the RESOLUTION wave data, public repository accessibility, data retrieval timestamps, and the paper's page size and count against the venue requirement — all remain as previously recorded.

---

## H. Final Verdict

> ## BOTH CLAIMS VERIFIED WITH WORDING CLARIFICATION

Both numbers are right. **518 / 13 of 531** is confirmed by two independent captures of the preserved run, and the exclusivity is not merely asserted but entailed: no precedence rule exists in the code, `ties = 0`, and max-severity aggregation then forces exactly one component at CAUTION in every attributed hour. **56** is confirmed by a static enumeration of the script's own configuration literals, which also reconciles the 78 gross invocations and the 22 duplicates that the figure had previously left unexplained. The three component zeros are each correctly characterised, including the one that could easily have been overstated — wind reached CAUTION in one hour, and the manuscript's "attributed to wind" accommodates that where a looser phrasing would not.

The verdict is not **BOTH CLAIMS VERIFIED** because one sentence in Section IV does not describe what the script does. "Denominator policy" has to stretch to cover a common-period *record* restriction for the count to reach 56; on the narrower reading a checking reader gets 54 and concludes the paper is wrong. And "each configuration is evaluated once rather than repeated" is contradicted by 22 repeated evaluations, including a canonical configuration computed five times per dataset. Neither is a numerical error, and neither affects a reported result — which is why this is a clarification rather than a correction — but both would mislead a reader attempting exactly the verification performed here.

It is not **PARTIALLY VERIFIED** — no aspect of either claim is left uncertain, and the one interpretive question the brief raised about exclusivity is answered rather than deferred. It is not **CONTRADICTED** — nothing in the source or the preserved output conflicts with either number.

The single edit proposed in section F.1 fixes both wording problems at once and makes the 56 self-verifying from the sentence alone.

---

## Post-investigation checks

| Check | Result |
|---|---|
| No canonical script changed | **Confirmed** — all hashes unchanged |
| No dataset changed | **Confirmed** |
| No preserved output changed | **Confirmed** — all three output hashes match the run manifest |
| No experiment executed | **Confirmed** — `threshold_sensitivity.py` was not run; the only code executed was the AST diagnostic in section C.1, which imports neither the module nor pandas or numpy and opens no dataset |
| No manuscript edited | **Confirmed** — DOCX hash `f8769389a5e5c681…` unchanged |
| No Git state-changing command used | **Confirmed** — read-only commands only |
| Only the requested report created | **Confirmed** — `docs/reproducibility/aai-2026-final-count-attribution-verification.md` is the single new file; the diagnostic was passed on stdin and wrote nothing |
| Pre-existing dirty state preserved | **Confirmed and recorded** — the working tree was already dirty before this task, with 45 `git status` entries and 0 modified tracked files |
