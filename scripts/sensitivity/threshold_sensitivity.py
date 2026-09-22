#!/usr/bin/env python3
"""Threshold sensitivity analysis for the headline Delta_L2 result.

Governance mappings are NOT varied. A_AI(CAUTION) = {Go, Delay} is frozen.
Only environmental classification thresholds vary. Reuses canonical_gt.
"""
import sys, itertools
from pathlib import Path
import pandas as pd, numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from canonical_gt import g_t as _g_t, is_daylight as _is_daylight

ROOT = HERE.parent.parent
DATA = ROOT / "data"
SAFE, CAUTION, UNSAFE = 0, 1, 2

CANON = dict(W_C=21.6, W_U=27.0, R_C=10.0, R_U=20.0, O_C=1.0, O_U=1.25)
CONFIGS = {"PRIMARY": "raw_marine_era5_sea.csv", "RESOLUTION": "raw_marine_mfwam.csv"}

def load(marine_file):
    w = pd.read_csv(DATA / "raw_weather_sea.csv", skiprows=3)
    m = pd.read_csv(DATA / marine_file, skiprows=3)
    w["time"] = pd.to_datetime(w["time"]); m["time"] = pd.to_datetime(m["time"])
    d = w.merge(m, on="time", how="inner", suffixes=("", "_m")).rename(columns={
        "wind_speed_10m (kn)": "wind", "precipitation (mm)": "precip",
        "weather_code (wmo code)": "wmo", "wave_height (m)": "wave"})
    d = d.dropna(subset=["wave", "wind", "precip"])
    d["hour"] = d["time"].dt.hour
    return d.sort_values("time").reset_index(drop=True)

def components(d, p):
    g_w = np.where(d["wind"] > p["W_U"], UNSAFE, np.where(d["wind"] > p["W_C"], CAUTION, SAFE))
    storm = (d["precip"] > p["R_U"]) | d["wmo"].isin([95, 96, 99])
    g_r = np.where(storm, UNSAFE, np.where(d["precip"] > p["R_C"], CAUTION, SAFE))
    g_o = np.where(d["wave"] > p["O_U"], UNSAFE, np.where(d["wave"] >= p["O_C"], CAUTION, SAFE))
    g_t = _g_t(d["time"], d["hour"])
    g_m = np.full(len(d), SAFE)
    return dict(g_w=g_w, g_r=g_r, g_m=g_m, g_o=g_o, g_t=np.asarray(g_t))

def classify(d, p):
    c = components(d, p)
    return np.max(np.column_stack([c["g_w"], c["g_r"], c["g_m"], c["g_o"], c["g_t"]]), axis=1), c

def dep_mask(d):
    return (d.hour >= 5) & (d.hour <= 9)

def run(d, p, mask=None):
    S, c = classify(d, p)
    m = dep_mask(d) if mask is None else mask
    s = S[m.values if hasattr(m, "values") else m]
    n = len(s)
    return dict(n=n,
                pSAFE=100*(s == SAFE).sum()/n,
                pCAUTION=100*(s == CAUTION).sum()/n,
                pUNSAFE=100*(s == UNSAFE).sum()/n,
                nCAUTION=int((s == CAUTION).sum())), S, c, m

# --- Delta_L2 computed the long way, from the admissible-set tables ---
FULL, REST, EMPTY = frozenset("abcd"), frozenset("ab"), frozenset()
T_C1 = {SAFE: FULL, CAUTION: FULL, UNSAFE: EMPTY}
T_C2 = {SAFE: FULL, CAUTION: REST, UNSAFE: EMPTY}
def delta_l2(S, m):
    s = S[m.values if hasattr(m, "values") else m]
    return 100*sum(1 for x in s if T_C1[x] != T_C2[x])/len(s)

if __name__ == "__main__":
    out = []
    P = lambda *a: (out.append(" ".join(str(x) for x in a)), print(*a))

    for cfg, f in CONFIGS.items():
        d = load(f)
        r, S, c, m = run(d, CANON)
        dl = delta_l2(S, m)
        P(f"\n{'='*70}\n{cfg}  records={len(d):,}  departure-window n={r['n']:,}\n{'='*70}")
        P(f"  BASELINE  Delta_L2(set-divergence) = {dl:.2f}%   P(CAUTION) = {r['pCAUTION']:.2f}%"
          f"   IDENTITY {'HOLDS' if abs(dl-r['pCAUTION'])<1e-9 else 'FAILS'}")
        P(f"  SAFE {r['pSAFE']:.2f}%   CAUTION {r['pCAUTION']:.2f}%   UNSAFE {r['pUNSAFE']:.2f}%")

        # boundary density (departure window)
        dd = d[m]
        P("\n  BOUNDARY DENSITY (departure-window observations within +/- window of boundary)")
        for name, col, b, w in [("wind 21.6kn", "wind", 21.6, 2.0), ("wind 27.0kn", "wind", 27.0, 2.0),
                                ("rain 10.0mm", "precip", 10.0, 3.0), ("rain 20.0mm", "precip", 20.0, 5.0),
                                ("wave 1.00m", "wave", 1.0, 0.15), ("wave 1.25m", "wave", 1.25, 0.15)]:
            k = int(((dd[col] >= b-w) & (dd[col] <= b+w)).sum())
            P(f"    {name:<13} +/-{w:<5} n={k:>6,}  ({100*k/len(dd):5.2f}% of window)   max={dd[col].max():.2f}")

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

        # one-at-a-time
        P("\n  ONE-AT-A-TIME SENSITIVITY  (Delta_L2 = P(CAUTION), departure window)")
        P("    --- rainfall R_C (R_U fixed 20.0) ---")
        for v in [5.0, 7.5, 10.0, 15.0, 19.9]:
            p = dict(CANON, R_C=v); rr, SS, _, mm = run(d, p)
            P(f"      R_C={v:>5} -> Delta_L2 {rr['pCAUTION']:6.2f}%   UNSAFE {rr['pUNSAFE']:6.2f}%")
        P("    --- wind W_C (W_U fixed 27.0) ---")
        for v in [18.0, 20.0, 21.6, 22.0, 25.0]:
            p = dict(CANON, W_C=v); rr, _, _, _ = run(d, p)
            P(f"      W_C={v:>5} -> Delta_L2 {rr['pCAUTION']:6.2f}%   UNSAFE {rr['pUNSAFE']:6.2f}%")
        P("    --- wave (O_C, O_U) ---")
        for oc, ou, tag in [(0.75,1.25,"sens -0.25 on O_C"), (1.0,1.25,"CANONICAL small vessel"),
                            (1.25,1.5,"sens +0.25 on O_C"), (1.0,1.9,"Yaakob failure point as O_U"),
                            (1.4,2.8,"Yaakob medium vessel"), (1.5,3.5,"Yaakob big vessel / MET Cat1 ceiling")]:
            p = dict(CANON, O_C=oc, O_U=ou); rr, _, _, _ = run(d, p)
            P(f"      ({oc:>4},{ou:>4}) -> Delta_L2 {rr['pCAUTION']:6.2f}%   UNSAFE {rr['pUNSAFE']:6.2f}%   [{tag}]")

        # time policy T1: daylight-only denominator
        dl_mask = np.asarray(_is_daylight(d["time"], d["hour"]))
        m2 = m.values & dl_mask
        r2, S2, _, _ = run(d, CANON, mask=m2)
        P(f"\n  TIME POLICY  T0 canonical (night->UNSAFE): Delta_L2 {r['pCAUTION']:.2f}%  n={r['n']:,}")
        P(f"               T1 daylight-only denominator : Delta_L2 {r2['pCAUTION']:.2f}%  n={r2['n']:,}"
          f"   UNSAFE {r2['pUNSAFE']:.2f}%")

        # combined grid on the two influential dims
        P("\n  COMBINED GRID  R_C x (O_C,O_U)   [Delta_L2 %]")
        waves = [(1.0,1.25),(1.0,1.9),(1.4,2.8),(1.5,3.5)]
        P("      R_C \\ wave " + "".join(f"{str(w):>14}" for w in waves))
        vals = []
        for rc in [5.0, 7.5, 10.0, 15.0, 19.9]:
            row = f"      {rc:>10}  "
            for oc, ou in waves:
                p = dict(CANON, R_C=rc, O_C=oc, O_U=ou); rr, _, _, _ = run(d, p)
                vals.append((rr['pCAUTION'], rc, oc, ou)); row += f"{rr['pCAUTION']:>13.2f}%"
            P(row)
        vals.sort()
        P(f"    grid min {vals[0][0]:.2f}% at R_C={vals[0][1]}, wave=({vals[0][2]},{vals[0][3]})")
        P(f"    grid max {vals[-1][0]:.2f}% at R_C={vals[-1][1]}, wave=({vals[-1][2]},{vals[-1][3]})")

    # common-period comparison
    P(f"\n{'='*70}\nCOMMON-PERIOD COMPARISON (de-confounds wave model from record length)\n{'='*70}")
    dp, dr = load(CONFIGS["PRIMARY"]), load(CONFIGS["RESOLUTION"])
    common = set(dp["time"]) & set(dr["time"])
    for tag, dd in (("PRIMARY wave model", dp), ("RESOLUTION wave model", dr)):
        sub = dd[dd["time"].isin(common)].reset_index(drop=True)
        rr, SS, _, mm = run(sub, CANON)
        P(f"  {tag:<24} common n={len(sub):,}  departure n={rr['n']:,}  Delta_L2 {rr['pCAUTION']:.2f}%  UNSAFE {rr['pUNSAFE']:.2f}%")

    Path("/tmp/sens_out.txt").write_text("\n".join(out))
