#!/usr/bin/env python3
"""
Diagnostic: which classification function actually binds?

For every hour where f(E) != SAFE, identify which g function(s) sit at the
maximum. Ties are counted for every tied function, so shares may sum above
100%. This is deliberate: when two functions are jointly at the maximum,
both are binding.

Resolves pre-registered predictions P05-P08 and P14
(see data/prediction-register.csv).

Data: Open-Meteo archive, Kota Kinabalu, 2020-01-01 to 2024-12-31.

CAVEAT: m (marine warning) has no historical archive and is held at 'none'.
It therefore never binds here. That is a data limitation, not a finding
about the model.
"""

import pandas as pd
import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

VESSEL_THRESHOLDS = {"small": (1.0, 1.9), "medium": (1.4, 2.8), "big": (1.5, 3.5)}
FUNCS = ["g_w", "g_r", "g_m", "g_o", "g_t"]


def load():
    w = pd.read_csv(DATA / "raw_weather.csv", skiprows=3)
    m = pd.read_csv(DATA / "raw_marine.csv", skiprows=3)
    r = pd.read_csv(DATA / "raw_rainfall.csv", skiprows=3)
    d = pd.DataFrame({
        "time": pd.to_datetime(w["time"]),
        "wind": w["wind_speed_10m (kn)"].values,
        "wmo":  w["weather_code (wmo code)"].values,
        "wave": m["wave_height (m)"].values,
        "precip": r["precipitation (mm)"].values,
    })
    d["hour"] = d["time"].dt.hour
    return d


def classify_all(d, vessel):
    """Return an (n, 5) array of per-function severities in FUNCS order."""
    lo, hi = VESSEL_THRESHOLDS[vessel]
    g_w = np.where(d["wind"] > 27, 2, np.where(d["wind"] > 22, 1, 0))
    storm = (d["precip"] > 20) | d["wmo"].isin([95, 96, 99])
    g_r = np.where(storm, 2, np.where(d["precip"] > 7.5, 1, 0))
    g_m = np.zeros(len(d), dtype=int)                      # no historical data
    g_o = np.where(d["wave"] > hi, 2, np.where(d["wave"] >= lo, 1, 0))
    g_t = np.where((d["hour"] >= 6) & (d["hour"] < 17), 0,
                   np.where((d["hour"] >= 17) & (d["hour"] < 19), 1, 2))
    return np.column_stack([g_w, g_r, g_m, g_o, g_t])


def binding_report(G, label, target_state=None):
    """target_state: None = all non-SAFE; 1 = CAUTION only; 2 = UNSAFE only."""
    f = G.max(axis=1)
    if target_state is None:
        mask = f > 0
        desc = "non-SAFE"
    else:
        mask = f == target_state
        desc = {1: "CAUTION", 2: "UNSAFE"}[target_state]
    n = int(mask.sum())
    print(f"\n{label} — {desc} hours: {n:,}")
    if n == 0:
        print("  (none)")
        return {}, 0
    at_max = (G[mask] == f[mask, None])
    shares = {}
    for i, name in enumerate(FUNCS):
        cnt = int(at_max[:, i].sum())
        shares[name] = 100 * cnt / n
        bar = "#" * int(shares[name] / 2.5)
        print(f"  {name:5s} at max: {cnt:7,}  {shares[name]:6.1f}%  {bar}")
    return shares, n


def main():
    d = load()
    print(__doc__)
    print(f"Loaded {len(d):,} records: {d.time.min()} to {d.time.max()}")

    day = (d.hour >= 6) & (d.hour < 17)
    dep = (d.hour >= 5) & (d.hour <= 9)

    results = {}

    G_all = classify_all(d, "small")
    G_day = classify_all(d[day].reset_index(drop=True), "small")
    G_dep = classify_all(d[dep].reset_index(drop=True), "small")

    print("\n" + "=" * 78)
    print("BINDING ANALYSIS — small vessel (< 10 GRT), the deployment population")
    print("=" * 78)

    s, _ = binding_report(G_all, "ALL HOURS (n=43,848)")
    results["P07"] = s.get("g_t", 0)

    s_day_c, _ = binding_report(G_day, "DAYLIGHT 06:00-17:00", target_state=1)
    results["P05"] = s_day_c.get("g_o", 0)

    s_day_all, _ = binding_report(G_day, "DAYLIGHT 06:00-17:00")
    results["P06"] = s_day_all.get("g_r", 0)

    binding_report(G_dep, "DEPARTURE WINDOW 05:00-09:00")

    # P08 — how many distinct functions are ever observed at the maximum
    f_dep = G_dep.max(axis=1)
    mask = f_dep > 0
    ever = [FUNCS[i] for i in range(5) if (G_dep[mask][:, i] == f_dep[mask, None][:, 0]).any()]
    results["P08"] = len(ever)
    print(f"\nDistinct functions ever at the maximum (departure window): "
          f"{len(ever)} — {', '.join(ever)}")
    never = [f for f in FUNCS if f not in ever]
    if never:
        print(f"NEVER binds: {', '.join(never)}")

    # Vessel comparison
    print("\n" + "=" * 78)
    print("g_o BINDING SHARE BY VESSEL CLASS (daylight, CAUTION hours)")
    print("=" * 78)
    for v in VESSEL_THRESHOLDS:
        Gv = classify_all(d[day].reset_index(drop=True), v)
        fv = Gv.max(axis=1)
        mk = fv == 1
        if mk.sum() == 0:
            print(f"  {v:7s}: no CAUTION hours")
            continue
        share = 100 * (Gv[mk][:, 3] == 1).sum() / mk.sum()
        print(f"  {v:7s}: {int(mk.sum()):6,} CAUTION hours, g_o at max in {share:5.1f}%")

    print("\n" + "=" * 78)
    print("PRE-REGISTERED PREDICTION CHECK")
    print("=" * 78)
    reg = pd.read_csv(DATA / "prediction-register.csv")
    checks = {
        "P05": (results["P05"], "min", 90, 100),
        "P06": (results["P06"], "max", 0, 5),
        "P07": (results["P07"], "min", 70, 100),
        "P08": (results["P08"], "max", 2, 4),
    }
    for pid, (actual, kind, lo, hi) in checks.items():
        if kind == "min":
            ok = actual >= lo
        elif kind == "max":
            ok = actual <= hi
        else:
            ok = lo <= actual <= hi
        status = "CONFIRMED" if ok else "REFUTED"
        stated = reg.loc[reg.id == pid, "pred_stated"].iloc[0]
        print(f"  {pid}  predicted {stated:>16}   actual {actual:8.1f}   {status}")
        reg.loc[reg.id == pid, "actual"] = round(float(actual), 2)
        reg.loc[reg.id == pid, "status"] = status
        reg.loc[reg.id == pid, "resolved"] = "2026-09-06"

    reg.to_csv(DATA / "prediction-register.csv", index=False)
    print(f"\nRegister updated: {DATA / 'prediction-register.csv'}")


if __name__ == "__main__":
    main()
