#!/usr/bin/env python3
"""
N1-N4 non-degeneracy gate for the proposed advisory-comparison study.

READ-ONLY with respect to every canonical artefact. This script
  - reads data/raw_weather_sea.csv and data/raw_marine_era5_sea.csv
  - imports scripts/canonical_gt.g_t (for the daylight component only)
  - writes nothing except its own output files under this directory
It modifies no canonical script, dataset, figure or result.

PRE-REGISTRATION. Everything in the PRE-REGISTERED block below was fixed
before this script was executed for the first time, and the gate is run once.
A generator tuned until it passes is a generator tuned to produce the result.

THE GENERATOR IS STIMULUS MATERIAL, NOT A PROPOSED SYSTEM.
It exists only to supply candidate advice that the three governance filters can
act on. It is deliberately independent of the architecture:
  - it never reads the safety state S, G(S) or A_AI(S);
  - it uses NO architecture threshold (not 21.6/27.0 kn, not 10/20 mm/hr,
    not 1.0/1.25 m). Its only parameters are percentiles of the record's own
    empirical distribution;
  - it aggregates by arithmetic MEAN of percentiles, deliberately not by
    max-severity, so it does not mirror the classifier's aggregation rule.
"""
from pathlib import Path
import json
import sys

import numpy as np
import pandas as pd

REPO = Path(__file__).resolve().parent.parent.parent
DATA = REPO / "data"
OUT = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO / "scripts"))
from canonical_gt import g_t as _canonical_g_t  # noqa: E402  (read-only import)

# ──────────────────────────────────────────────────────────────────────────
# PRE-REGISTERED — fixed before first execution
# ──────────────────────────────────────────────────────────────────────────
WINDOW_HOURS = (5, 6, 7, 8, 9)      # 05:00-09:00 inclusive, UTC+8
TRIP_HORIZON_H = 9                   # a day trip: departure hour + 8

P_GO = 60        # exposure percentile at or below which "Go" is generated
P_OK = 70        # exposure percentile defining a workable forward hour
MIN_GAIN_PCTL = 5.0   # percentile-point improvement needed to name a better hour
MIN_DURATION_H = 2    # consecutive workable hours needed to state a Duration

# N1-N4 thresholds, as published in research/next-research-decision-package.md
N1_MIN_TYPE_SHARE = 0.10
N2_MIN_ARM_DIVERGENCE = 0.20
N3_MIN_WITHHELD_REALISATION = 0.50
N4_MIN_BOUNDARY_SHARE = 0.30

# Boundary-case epsilons. Sourced from the project's own sensitivity step
# granularity (0.05 m wave) and the data resolution of each variable.
EPS = {"wave": 0.05, "wind": 0.5, "rain": 0.5}

# Architecture thresholds — used ONLY to compute S for the C1/C2 filters and
# the N4 boundary test. NEVER passed to the generator.
W_CAUTION, W_UNSAFE = 21.6, 27.0
R_CAUTION, R_UNSAFE = 10.0, 20.0
O_CAUTION, O_UNSAFE = 1.0, 1.25          # "small" vessel, < 10 GRT
A_AI = {0: {"Go", "Delay", "DepartureTime", "Duration"},
        1: {"Go", "Delay"},
        2: set()}
TYPES = ["Go", "Delay", "DepartureTime", "Duration"]
# ──────────────────────────────────────────────────────────────────────────


def load():
    w = pd.read_csv(DATA / "raw_weather_sea.csv", skiprows=3)
    m = pd.read_csv(DATA / "raw_marine_era5_sea.csv", skiprows=3)
    w["time"] = pd.to_datetime(w["time"])
    m["time"] = pd.to_datetime(m["time"])
    j = w.merge(m, on="time", how="inner").dropna(
        subset=["wind_speed_10m (kn)", "wave_height (m)", "precipitation (mm)"])
    d = pd.DataFrame({
        "time": j["time"].values,
        "wind": j["wind_speed_10m (kn)"].values,
        "wmo": j["weather_code (wmo code)"].values,
        "wave": j["wave_height (m)"].values,
        "precip": j["precipitation (mm)"].values,
    })
    d["hour"] = pd.to_datetime(d["time"]).dt.hour
    d["date"] = pd.to_datetime(d["time"]).dt.date
    return d.reset_index(drop=True)


# ── the architecture side: S per hour (read-only reproduction) ────────────
def g_w(v):
    return 2 if v > W_UNSAFE else (1 if v > W_CAUTION else 0)


def g_r(p, c):
    if p > R_UNSAFE or c in (95, 96, 99):
        return 2
    return 1 if p > R_CAUTION else 0


def g_o(v):
    return 0 if v < O_CAUTION else (1 if v <= O_UNSAFE else 2)


def classify(d):
    terms = np.vstack([
        d["wind"].apply(g_w).values,
        np.array([g_r(p, c) for p, c in zip(d["precip"], d["wmo"])]),
        _canonical_g_t(pd.to_datetime(d["time"]), d["hour"]),
        d["wave"].apply(g_o).values,
        np.zeros(len(d), dtype=int),          # g_m: structurally excluded, D = {m}
    ])
    return np.max(terms, axis=0)


# ── the generator side: exposure index and candidate advice ───────────────
def exposure_index(d):
    """Mean of the three variables' empirical percentiles over the whole record.

    Percentile ranks are computed on the full 43,848-hour record, so the index
    is a property of the site's own distribution. No absolute threshold is used,
    and no architecture threshold is consulted.
    """
    pct = {}
    for col in ("wind", "wave", "precip"):
        pct[col] = d[col].rank(pct=True).values * 100.0
    return (pct["wind"] + pct["wave"] + pct["precip"]) / 3.0


def generate(d, e):
    """Candidate advice per departure-window hour. Returns a list of sets."""
    e_go = np.percentile(e, P_GO)
    e_ok = np.percentile(e, P_OK)
    by_key = {(r.date, r.hour): i for i, r in enumerate(d.itertuples())}
    out = []
    for i, r in enumerate(d.itertuples()):
        if r.hour not in WINDOW_HOURS:
            out.append(None)
            continue
        s = set()
        # Go / Delay — mutually exclusive, one is always produced
        s.add("Go" if e[i] <= e_go else "Delay")
        # DepartureTime — a strictly better later hour inside the same window
        later = [by_key[(r.date, h)] for h in WINDOW_HOURS
                 if h > r.hour and (r.date, h) in by_key]
        if later:
            best = min(later, key=lambda k: e[k])
            if e[i] - e[best] >= MIN_GAIN_PCTL and e[best] <= e_ok:
                s.add("DepartureTime")
        # Duration — a run of workable forward hours from this departure
        run = 0
        for h in range(r.hour, r.hour + TRIP_HORIZON_H):
            k = by_key.get((r.date, h))
            if k is None or e[k] > e_ok:
                break
            run += 1
        if run >= MIN_DURATION_H:
            s.add("Duration")
        out.append(s)
    return out


# ── N4: boundary cases ───────────────────────────────────────────────────
def is_boundary(r):
    for v, lo, hi, key in (
        (r.wave, O_CAUTION, O_UNSAFE, "wave"),
        (r.wind, W_CAUTION, W_UNSAFE, "wind"),
        (r.precip, R_CAUTION, R_UNSAFE, "rain"),
    ):
        eps = EPS[key]
        if abs(v - lo) <= eps or abs(v - hi) <= eps:
            return True
    return False


def main():
    d = load()
    e = exposure_index(d)
    S = classify(d)
    cand = generate(d, e)

    win = [i for i in range(len(d)) if d.at[i, "hour"] in WINDOW_HOURS]
    n = len(win)
    rows = []
    for i in win:
        c0 = cand[i]
        c1 = set(c0) if S[i] != 2 else set()
        c2 = set(c0) & A_AI[int(S[i])]
        rows.append({
            "time": str(d.at[i, "time"]), "S": int(S[i]),
            "wind": float(d.at[i, "wind"]), "wave": float(d.at[i, "wave"]),
            "precip": float(d.at[i, "precip"]), "exposure_pctl": float(e[i]),
            "C0": "|".join(sorted(c0)), "C1": "|".join(sorted(c1)),
            "C2": "|".join(sorted(c2)),
            "C1_ne_C2": int(c1 != c2),
            "boundary": int(is_boundary(d.iloc[i])),
        })
    t = pd.DataFrame(rows)
    t.to_csv(OUT / "n1-n4-case-table.csv", index=False)

    # ---- N1 : type coverage in the ungated candidate pool
    n1 = {ty: float((t["C0"].str.split("|").apply(lambda s: ty in s)).mean())
          for ty in TYPES}
    n1_pass = all(v >= N1_MIN_TYPE_SHARE for v in n1.values())

    # ---- N2 : C1 vs C2 content divergence
    n2_all = float(t["C1_ne_C2"].mean())
    caution = t[t["S"] == 1]
    n2_caution_pool = float(caution["C1_ne_C2"].mean()) if len(caution) else 0.0
    n2_pass_all = n2_all >= N2_MIN_ARM_DIVERGENCE
    n2_pass_strat = n2_caution_pool >= N2_MIN_ARM_DIVERGENCE

    # ---- N3 : withheld types actually realised inside CAUTION
    withheld = caution["C0"].str.split("|").apply(
        lambda s: ("DepartureTime" in s) or ("Duration" in s))
    n3 = float(withheld.mean()) if len(caution) else 0.0
    n3_pass = n3 >= N3_MIN_WITHHELD_REALISATION

    # ---- N4 : boundary-case availability
    n4 = float(t["boundary"].mean())
    n4_pass = n4 >= N4_MIN_BOUNDARY_SHARE

    res = {
        "record_hours": int(len(d)),
        "departure_window_cases": n,
        "state_distribution": {
            "SAFE": int((t["S"] == 0).sum()),
            "CAUTION": int((t["S"] == 1).sum()),
            "UNSAFE": int((t["S"] == 2).sum()),
        },
        "P_S_CAUTION_pct": round(100.0 * float((t["S"] == 1).mean()), 4),
        "exposure_cutoffs": {"P_GO": float(np.percentile(e, P_GO)),
                             "P_OK": float(np.percentile(e, P_OK))},
        "N1_type_share": {k: round(v, 4) for k, v in n1.items()},
        "N1_threshold": N1_MIN_TYPE_SHARE, "N1_PASS": n1_pass,
        "N2_divergence_all_cases": round(n2_all, 6),
        "N2_divergence_caution_only_pool": round(n2_caution_pool, 6),
        "N2_threshold": N2_MIN_ARM_DIVERGENCE,
        "N2_PASS_unstratified": n2_pass_all,
        "N2_PASS_caution_stratified": n2_pass_strat,
        "N3_withheld_realised_in_CAUTION": round(n3, 6),
        "N3_threshold": N3_MIN_WITHHELD_REALISATION, "N3_PASS": n3_pass,
        "N4_boundary_share": round(n4, 6),
        "N4_threshold": N4_MIN_BOUNDARY_SHARE, "N4_PASS": n4_pass,
        "N4_boundary_count": int(t["boundary"].sum()),
        "GATE_PASS_as_preregistered": bool(
            n1_pass and n2_pass_all and n3_pass and n4_pass),
    }
    (OUT / "n1-n4-results.json").write_text(json.dumps(res, indent=2))
    print(json.dumps(res, indent=2))

    # supporting breakdowns, reported whatever they say
    print("\n--- C0 pool composition (top 12) ---")
    print(t["C0"].value_counts().head(12).to_string())
    print("\n--- C2 presented content by state ---")
    print(t.groupby("S")["C2"].value_counts().head(20).to_string())
    print("\n--- boundary cases by component ---")
    for key, (lo, hi, col) in {
        "wave": (O_CAUTION, O_UNSAFE, "wave"),
        "wind": (W_CAUTION, W_UNSAFE, "wind"),
        "rain": (R_CAUTION, R_UNSAFE, "precip"),
    }.items():
        eps = EPS[key]
        m = ((t[col] - lo).abs() <= eps) | ((t[col] - hi).abs() <= eps)
        print(f"{key:6s} eps={eps}: {int(m.sum()):5d} cases "
              f"({100*m.mean():.2f}%)")


if __name__ == "__main__":
    main()
