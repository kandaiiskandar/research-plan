#!/usr/bin/env python3
"""C-6: re-resolve g_t-affected predictions under the APPROVED MIGRATION CANDIDATE.

STATUS OF THE SPECIFICATION BEING EVALUATED
-------------------------------------------
Model B is APPROVED but NOT YET CANONICAL. Every value produced here is a
"candidate actual" under the **approved migration candidate specification**,
never a canonical actual. Canonical g_t remains the incumbent fixed clock and
the canonical headline figures remain 7.72% / 5.98% until C-8 completes.

WHAT THIS SCRIPT DOES NOT DO
----------------------------
* It NEVER writes data/prediction-register.csv. It only reads it.
  (canonical_figures.py, condition_comparison.py, diagnostic_binding.py and
  hysteresis_analysis.py all write the register on every run, so none of them
  is executed here. Their component logic is reproduced from the canonical
  constants instead, and P09-P13 are taken from the FROZEN C-5 artefact.)
* It does not recompute solar astronomy. Model B reads the frozen C-3 artefact
  data/solar/solar-events-daily.csv (solar-spec-v1 / solar-v1).
* It does not propagate anything to Appendix C, scripts, manuscripts or figures.

EVIDENCE PRECEDENCE
-------------------
1. FROZEN C-5 artefact for P09, P10, P11, P12, P13 -- not recomputed.
2. Structural argument for P21 -- C1 and C3 are the identical admissible-set
   map in condition_comparison.py, so their divergence is 0 for ANY classifier.
3. Computed here, read-only, for everything else that g_t can move.

CONFIGURATION PER PREDICTION SCOPE
----------------------------------
A prediction is evaluated in the configuration its own registered scope names:
  scope mentions MFWAM        -> RESOLUTION config (raw_weather_sea + MFWAM)
  otherwise                   -> PRIMARY config    (raw_weather_sea + ERA5-sea)
This preserves each prediction's original question. Changing a prediction's
configuration would be rewriting the prediction, which the protocol forbids.
"""

import csv
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent.parent
DATA = ROOT / "data"
OUT = DATA / "c6"
OUT.mkdir(parents=True, exist_ok=True)

SOLAR = DATA / "solar" / "solar-events-daily.csv"
C5 = DATA / "c5" / "c5-three-stage-metrics.csv"
REG = DATA / "prediction-register.csv"

# Canonical constants (identical to canonical_figures.py / diagnostic_binding.py)
W_CAUTION, W_UNSAFE = 21.6, 27.0
R_CAUTION, R_UNSAFE = 10.0, 20.0
TH = {"small": (1.0, 1.25), "medium": (1.4, 2.8), "big": (1.5, 3.5)}
SAFE, CAUTION, UNSAFE = 0, 1, 2

CONFIGS = {
    "PRIMARY": ("raw_weather_sea.csv", "raw_marine_era5_sea.csv"),
    "RESOLUTION": ("raw_weather_sea.csv", "raw_marine_mfwam.csv"),
}

CANDIDATE_SPEC = ("APPROVED MIGRATION CANDIDATE — Model B: g_t SAFE when "
                  "sunrise<=t<sunset else UNSAFE; g_t(bottom)=UNSAFE; "
                  "solar-spec-v1 @ 5.98N,116.01E; all other components canonical")
PREV_SPEC = ("canonical incumbent — g_t fixed clock 06:00/17:00/19:00; "
             "w 21.6/27.0; r 10.0/20.0; o_small 1.0/1.25")


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def load(cfg):
    wf, mf = CONFIGS[cfg]
    w = pd.read_csv(DATA / wf, skiprows=3)
    m = pd.read_csv(DATA / mf, skiprows=3)
    w["time"] = pd.to_datetime(w["time"])
    m["time"] = pd.to_datetime(m["time"])
    d = w.merge(m, on="time", how="inner").rename(columns={
        "wind_speed_10m (kn)": "wind", "weather_code (wmo code)": "wmo",
        "precipitation (mm)": "precip", "wave_height (m)": "wave"})
    d = d.dropna(subset=["wave", "wind", "precip"])
    d["hour"] = d["time"].dt.hour
    return d.sort_values("time").reset_index(drop=True)


def g_t_incumbent(d):
    return np.where((d["hour"] >= 6) & (d["hour"] < 17), SAFE,
                    np.where((d["hour"] >= 17) & (d["hour"] < 19), CAUTION, UNSAFE))


_SOL = None


def g_t_modelb(d):
    """Model B from the FROZEN C-3 artefact. No astronomy computed here."""
    global _SOL
    if _SOL is None:
        s = pd.read_csv(SOLAR)
        s["date"] = pd.to_datetime(s["date"]).dt.date
        _SOL = (dict(zip(s["date"], s["sunrise_hours"].astype(float))),
                dict(zip(s["date"], s["sunset_hours"].astype(float))))
    sr, ss = _SOL
    out = np.full(len(d), UNSAFE, dtype=int)          # fail-safe default
    dates = d["time"].dt.date.values
    hours = d["hour"].values.astype(float)
    for i in range(len(d)):
        a, b = sr.get(dates[i]), ss.get(dates[i])
        if a is not None and b is not None:
            out[i] = SAFE if (a <= hours[i] < b) else UNSAFE
    return out


def components(d, vessel, gt):
    lo, hi = TH[vessel]
    g_w = np.where(d["wind"] > W_UNSAFE, UNSAFE,
                   np.where(d["wind"] > W_CAUTION, CAUTION, SAFE))
    storm = (d["precip"] > R_UNSAFE) | d["wmo"].isin([95, 96, 99])
    g_r = np.where(storm, UNSAFE, np.where(d["precip"] > R_CAUTION, CAUTION, SAFE))
    g_m = np.zeros(len(d), dtype=int)                  # D = {m}, pinned SAFE
    g_o = np.where(d["wave"] > hi, UNSAFE, np.where(d["wave"] >= lo, CAUTION, SAFE))
    G = np.column_stack([g_w, g_r, g_m, g_o, gt])
    return G.max(axis=1), G


FUNCS = ["g_w", "g_r", "g_m", "g_o", "g_t"]


def at_max_share(G, mask, idx):
    if mask.sum() == 0:
        return 0.0
    f = G.max(axis=1)
    am = (G[mask] == f[mask, None])
    return 100.0 * am[:, idx].sum() / mask.sum()


# ---- admissible-set maps, verbatim from condition_comparison.py ----
FULL, RESTRICTED, EMPTY = "FULL", "RESTRICTED", "EMPTY"
COND = {
    "C0": {SAFE: FULL, CAUTION: FULL, UNSAFE: FULL},
    "C1": {SAFE: FULL, CAUTION: FULL, UNSAFE: EMPTY},
    "C3": {SAFE: FULL, CAUTION: FULL, UNSAFE: EMPTY},   # identical to C1
    "C2": {SAFE: FULL, CAUTION: RESTRICTED, UNSAFE: EMPTY},
}


def divergence(f, mask, a, b):
    if mask.sum() == 0:
        return 0.0
    sa = np.array([COND[a][s] for s in f[mask]])
    sb = np.array([COND[b][s] for s in f[mask]])
    return 100.0 * (sa != sb).mean()


def compute(gt_fn):
    """Every g_t-movable registered metric, under the supplied g_t."""
    r = {}
    dP = load("PRIMARY")
    gtP = gt_fn(dP)
    fP, GP = components(dP, "small", gtP)
    fP_big, _ = components(dP, "big", gtP)

    dayP = ((dP.hour >= 6) & (dP.hour < 17)).values     # registered scope wording
    depP = ((dP.hour >= 5) & (dP.hour <= 9)).values

    r["P03"] = 0.0                                       # superseded g_v floor: SAFE unreachable
    r["P04"] = 100.0 * (fP[depP] == CAUTION).mean()
    cautionday = dayP & (fP == CAUTION)
    r["P05"] = at_max_share(GP, cautionday, FUNCS.index("g_o"))
    r["P06"] = at_max_share(GP, dayP & (fP > SAFE), FUNCS.index("g_r"))
    r["P07"] = at_max_share(GP, fP > SAFE, FUNCS.index("g_t"))
    nsd = fP[depP] > SAFE
    if nsd.sum():
        amd = (GP[depP][nsd] == fP[depP][nsd, None])
        r["P08"] = float((amd.sum(axis=0) > 0).sum())
    else:
        r["P08"] = 0.0
    r["P14_g_o_dayCAUTION"] = r["P05"]
    r["P14_g_t_nonSAFE"] = r["P07"]
    r["P14_g_w_bind"] = at_max_share(GP, fP > SAFE, FUNCS.index("g_w"))
    r["P14_g_m_bind"] = at_max_share(GP, fP > SAFE, FUNCS.index("g_m"))
    r["P_primary_level2"] = r["P04"]

    dR = load("RESOLUTION")
    gtR = gt_fn(dR)
    fR, GR = components(dR, "small", gtR)
    dayR = ((dR.hour >= 6) & (dR.hour < 17)).values
    depR = ((dR.hour >= 5) & (dR.hour <= 9)).values

    # P17: MFWAM CAUTION rate vs ERA5 over the SAME period
    per = dP.time.isin(dR.time).values
    fP_same = fP[per]
    r["P17_mfwam"] = 100.0 * (fR == CAUTION).mean()
    r["P17_era5"] = 100.0 * (fP_same == CAUTION).mean()
    r["P17_mfwam_lower"] = bool(r["P17_mfwam"] < r["P17_era5"])

    r["P18"] = 100.0 * (fR[depR] == CAUTION).mean()
    r["P19"] = r["P18"]                                  # same metric, post-amendment
    r["P20"] = float(((fR == UNSAFE) & dayR).sum())
    r["P21"] = divergence(fR, np.ones(len(fR), bool), "C1", "C3")
    r["P22"] = divergence(fR, depR, "C2", "C1")
    r["P23"] = divergence(fR, depR, "C0", "C2")
    r["P24"] = divergence(fR, depR, "C0", "C1")
    r["_resolution_level2"] = r["P18"]
    return r


def main():
    reg_before = sha(REG)
    print("=" * 78)
    print("C-6  RE-RESOLUTION UNDER THE APPROVED MIGRATION CANDIDATE")
    print("=" * 78)
    print(f"register sha256 BEFORE : {reg_before}")
    print(f"C-3 solar artefact     : {sha(SOLAR)}")
    print(f"C-5 metrics artefact   : {sha(C5)}")
    print(f"\ncandidate spec: {CANDIDATE_SPEC}\n")

    inc = compute(g_t_incumbent)
    mb = compute(g_t_modelb)

    print(f"{'metric':22s}{'incumbent':>14}{'ModelB cand':>14}")
    print("-" * 50)
    for k in sorted(set(inc) | set(mb)):
        a, b = inc.get(k), mb.get(k)
        fa = f"{a:.4f}" if isinstance(a, float) else str(a)
        fb = f"{b:.4f}" if isinstance(b, float) else str(b)
        print(f"{k:22s}{fa:>14}{fb:>14}")

    c5 = {r["stage"]: r for r in csv.DictReader(C5.open())}
    print("\nFROZEN C-5 (not recomputed):")
    for s in ("stage1_v1_incumbent", "stage2_v2_incumbent", "stage3_v2_modelb"):
        v = c5[s]
        print(f"  {s:22s} P09={v['P09_total_transitions']:>6} "
              f"P10={v['P10_non_scheduled']:>5} P11={v['P11_oscillations']:>4} "
              f"P12={v['P12_reduction_pct']:>6}")

    json.dump({"generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
               "candidate_spec": CANDIDATE_SPEC, "previous_spec": PREV_SPEC,
               "incumbent": inc, "model_b_candidate": mb,
               "frozen_c5": c5,
               "evidence": {"solar_artefact_sha256": sha(SOLAR),
                            "c5_metrics_sha256": sha(C5)},
               "register_sha256_before": reg_before},
              (OUT / "c6-candidate-actuals.json").open("w"), indent=2, default=str)

    reg_after = sha(REG)
    print(f"\nregister sha256 AFTER  : {reg_after}")
    print(f"REGISTER UNCHANGED BY THIS SCRIPT : {reg_before == reg_after}")
    print(f"\nwrote {(OUT/'c6-candidate-actuals.json').relative_to(ROOT)}")
    print("\nNOTE: canonical g_t unchanged. 7.72% / 5.98% remain canonical.")


if __name__ == "__main__":
    main()
