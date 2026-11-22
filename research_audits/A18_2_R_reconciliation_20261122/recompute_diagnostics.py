#!/usr/bin/env python3
"""
A18.2-R — recomputation of the four disputed proxy diagnostics (R-01..R-04),
plus two further report claims the external reviewer could not check (R-11, R-12).

Standard library only. READ-ONLY on every original path and on every
A18.2 v0.1 artefact. Writes only into this reconciliation folder.

B2's frozen proposals, 00_contract.json, the masking policies and all binding
results are NOT recomputed, refitted or tuned.
"""
import csv, hashlib, json, math, statistics
from collections import Counter
from datetime import datetime, timezone, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
DATA = ROOT / "data"
V01 = ROOT / "research_audits" / "A18_2_CFB_v0_1_20261121"
KCH = timezone(timedelta(hours=8))

def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for c in iter(lambda: fh.read(1 << 20), b""): h.update(c)
    return h.hexdigest()

SRC = {p: sha(ROOT / p) for p in
       ["data/raw_weather_sea.csv", "data/raw_marine_era5_sea.csv",
        "data/solar/solar-events-daily.csv"]}
FROZEN_V01 = {f.name: sha(f) for f in sorted(V01.iterdir()) if f.is_file()}

# ---------- rebuild the IDENTICAL frozen population (same pathway as v0.1)
def rd(p): return list(csv.DictReader(open(p, newline="", encoding="utf-8").read().splitlines()[3:]))
def num(v):
    v = (v or "").strip()
    if v == "" or v.upper() in ("NAN","NA","NULL"): return None
    try: return float(v)
    except ValueError: return None

import importlib.util
_s = importlib.util.spec_from_file_location(
    "ref", ROOT/"research_audits"/"A18_1_step3_20261121"/"08_reconstruction_reference.py")
R = importlib.util.module_from_spec(_s); _s.loader.exec_module(R)
SAFE, CAUTION, UNSAFE = R.SAFE, R.CAUTION, R.UNSAFE

w = rd(DATA/"raw_weather_sea.csv"); m = {r["time"]: r for r in rd(DATA/"raw_marine_era5_sea.csv")}
rows = []
for r in w:
    mm = m.get(r["time"])
    if mm is None: continue
    wind, precip, wave = num(r["wind_speed_10m (kn)"]), num(r["precipitation (mm)"]), num(mm["wave_height (m)"])
    wmo = num(r["weather_code (wmo code)"])
    if None in (wave, wind, precip): continue
    ts = datetime.strptime(r["time"], "%Y-%m-%dT%H:%M")
    if not (5 <= ts.hour <= 9): continue
    st = max(UNSAFE if wind > 27.0 else (CAUTION if wind > 21.6 else SAFE),
             UNSAFE if (precip > 20.0 or int(wmo) in (95,96,99)) else (CAUTION if precip > 10.0 else SAFE),
             SAFE,
             UNSAFE if wave > 1.25 else (CAUTION if wave >= 1.0 else SAFE),
             R.g_t(ts.date(), ts.hour))
    rows.append(dict(case_id="CFB-"+r["time"].replace("-","").replace("T","").replace(":",""),
        ts=r["time"], state=st,
        gusts=num(r["wind_gusts_10m (kn)"]), wdir=num(r["wind_direction_10m (°)"]),
        wper=num(mm["wave_period (s)"]), wind=wind, wave=wave))

# verify the population is the SAME one v0.1 used, by case_id set
v01_cases = {r["case_id"] for r in csv.DictReader(open(V01/"03_case_population_register.csv"))}
POP_MATCH = ({r["case_id"] for r in rows} == v01_cases)
N = len(rows)

# ---------- R-01/R-02: Pearson r, explicitly matched pairs
def pearson(pairs):
    xs = [a for a,b in pairs]; ys = [b for a,b in pairs]
    n = len(pairs); mx, my = statistics.fmean(xs), statistics.fmean(ys)
    sx = math.sqrt(sum((x-mx)**2 for x in xs)); sy = math.sqrt(sum((y-my)**2 for y in ys))
    return (sum((x-mx)*(y-my) for x,y in zip(xs,ys))/(sx*sy)) if sx and sy else None

def matched(fa, fb):
    out, dropped = [], 0
    for r in rows:
        a, b = r[fa], r[fb]
        if a is None or b is None or not (math.isfinite(a) and math.isfinite(b)):
            dropped += 1; continue
        out.append((a,b))
    return out, dropped

# ---------- R-03/R-04: best single-threshold accuracy for UNSAFE, EXHAUSTIVE
def best_threshold(feat):
    """Binary label y = 1[state == UNSAFE].
    Candidate cutpoints: EVERY distinct observed value of the feature (exhaustive).
    Two explicit directions:
        'ge'  predict UNSAFE iff x >= t
        'le'  predict UNSAFE iff x <= t
    Accuracy is IN-SAMPLE (no holdout, no cross-validation).
    Tie rule: scan cutpoints ascending, direction 'ge' before 'le'; keep the FIRST
    maximum and count how many (cutpoint, direction) pairs attain it."""
    xs = [r[feat] for r in rows]
    ys = [1 if r["state"] == UNSAFE else 0 for r in rows]
    cand = sorted(set(xs))
    best = dict(acc=-1.0)
    optima = 0
    for t in cand:
        for d in ("ge", "le"):
            pred = [(1 if x >= t else 0) if d == "ge" else (1 if x <= t else 0) for x in xs]
            tp = sum(1 for p,y in zip(pred,ys) if p==1 and y==1)
            tn = sum(1 for p,y in zip(pred,ys) if p==0 and y==0)
            acc = (tp+tn)/len(ys)
            if acc > best["acc"] + 1e-12:
                best = dict(acc=acc, cut=t, direction=d, tp=tp, tn=tn); optima = 1
            elif abs(acc - best["acc"]) <= 1e-12:
                optima += 1
    prev = sum(ys)/len(ys)
    best.update(n_candidate_cutpoints=len(cand),
                evaluations=2*len(cand), n_optima_tied=optima,
                class_prevalence_UNSAFE=round(prev,6),
                majority_class_baseline_accuracy=round(max(prev, 1-prev),6),
                lift_over_baseline=round(best["acc"] - max(prev, 1-prev), 6),
                in_sample=True)
    return best

res = {}
for rid, fa, fb in (("R-01","gusts","wind"), ("R-02","wper","wave")):
    pairs, dropped = matched(fa, fb)
    res[rid] = dict(quantity=f"Pearson r({fa}, gate {fb})",
        n_matched_pairs=len(pairs), n_dropped_missing=dropped,
        value=round(pearson(pairs), 4), value_full=repr(pearson(pairs)),
        definition="sample Pearson product-moment correlation over case_id-matched row pairs",
        missing_treatment="pairwise complete-case; zero pairs dropped (both columns have no nulls in PRIMARY)")
for rid, feat in (("R-03","gusts"), ("R-04","wper")):
    b = best_threshold(feat)
    res[rid] = dict(quantity=f"best single-threshold in-sample accuracy for UNSAFE using {feat}", **b,
        value=round(b["acc"],4))

out = dict(
 reconciliation_id="A18.2-R", recomputed_at=datetime.now(KCH).isoformat(),
 population=dict(n=N, scope="frozen PRIMARY 05:00-09:00 inclusive departure-window cases",
   case_id_set_identical_to_v0_1=POP_MATCH,
   states={ "SAFE":sum(1 for r in rows if r["state"]==SAFE),
            "CAUTION":sum(1 for r in rows if r["state"]==CAUTION),
            "UNSAFE":sum(1 for r in rows if r["state"]==UNSAFE)}),
 source_hashes=SRC,
 code_path=f"{HERE.name}/recompute_diagnostics.py :: pearson(), matched(), best_threshold()",
 results=res)

# ---------- R-11/R-12: two further report claims
tmix = {"Go":7882, "Duration":810, "DepartureTime":435, "Delay":8}
# recomputed from the FROZEN ledger, not from the report
led = [r for r in csv.DictReader(open(V01/"04_proposal_ledger.csv")) if r["advisor"]=="B2-FROZEN-VARYING"]
tc = Counter(r["proposed_type"] for r in led)
H = -sum((v/len(led))*math.log2(v/len(led)) for v in tc.values() if v)
cl = {}
for r in led: cl.setdefault(r["cluster_id"], set()).add(r["proposed_type"])
out["results"]["R-11"] = dict(quantity="B2 proposal-type entropy (bits)",
    value=round(H,4), definition="Shannon entropy over the B2 type distribution, log base 2",
    source="recomputed from the FROZEN proposal ledger", type_counts=dict(tc),
    max_possible=round(math.log2(4),4))
out["results"]["R-12"] = dict(quantity="day-clusters containing more than one proposal type",
    value=sum(1 for v in cl.values() if len(v)>1), total_clusters=len(cl),
    definition="count of calendar-date clusters whose B2 proposals span >1 type",
    source="recomputed from the FROZEN proposal ledger")
out["frozen_v0_1_hashes"] = FROZEN_V01
(HERE/"A18_2_R_recomputation.json").write_text(json.dumps(out,indent=2),encoding="utf-8")

print(f"population n={N}  case_id set identical to v0.1: {POP_MATCH}")
print(f"states: {out['population']['states']}\n")
for rid in ("R-01","R-02","R-03","R-04","R-11","R-12"):
    r = out["results"][rid]
    print(f"{rid}  {r['quantity'][:62]:62s} = {r['value']}")
    if rid in ("R-03","R-04"):
        print(f"      cut={r['cut']} dir={r['direction']}  cutpoints={r['n_candidate_cutpoints']}"
              f"  evals={r['evaluations']}  tied_optima={r['n_optima_tied']}")
        print(f"      prevalence(UNSAFE)={r['class_prevalence_UNSAFE']}  baseline={r['majority_class_baseline_accuracy']}"
              f"  lift={r['lift_over_baseline']}  in_sample={r['in_sample']}")
    if rid in ("R-01","R-02"):
        print(f"      matched pairs={r['n_matched_pairs']}  dropped={r['n_dropped_missing']}")
