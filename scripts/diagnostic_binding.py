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

# --- SDR-001 APPLIED 2026-09-08: g_t is the canonical solar-event classifier.
# Imported from scripts/canonical_gt.py, which reads the frozen C-3 artefact
# data/solar/solar-events-daily.csv. No solar astronomy is computed here.
# "Daylight" now means sunrise <= t < sunset, NOT the superseded 06:00-17:00.
import sys as _sys
_sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonical_gt import g_t as _canonical_g_t, is_daylight as _is_daylight


ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

# Wind thresholds — anchored 2026-09-08. MET Malaysia Cat 1 / Cat 2 onsets,
# preserved at the source value rather than rounded:
#   W_CAUTION  40 km/h / 1.852 = 21.598 kn -> 21.6 at data resolution.
#   W_UNSAFE   50 km/h / 1.852 = 26.998 kn -> 27.0 at data resolution.
# Superseded: W_CAUTION was 22, an undocumented rounding of 21.598. That
# rounding suppressed 2 activations in 5 years and made F-1 read "never
# fires" rather than "almost never binds". See appendix-c C.2 and F-17.
W_CAUTION, W_UNSAFE = 21.6, 27.0

# Rainfall thresholds — anchored 2026-09-08. See
# docs/canonical/finding-met-lower-boundary-gap.md and appendix-c C.2.
#   R_UNSAFE  MET Malaysia Ribut Petir warning trigger (> 20 mm/hr).
#   R_CAUTION JPS/DID Infobanjir Light-category upper limit (10 mm/hr).
#             MET publishes NO criterion below 20 mm/hr, so this boundary
#             is necessarily non-MET — the same structure as the wave case.
# Superseded: R_CAUTION was 7.5, which matched no published source.
R_CAUTION, R_UNSAFE = 10.0, 20.0

VESSEL_THRESHOLDS = {"small": (1.0, 1.25), "medium": (1.4, 2.8), "big": (1.5, 3.5)}
FUNCS = ["g_w", "g_r", "g_m", "g_o", "g_t"]


def load():

# --- SDR-001 / C-8 data-source migration ------------------------------------
# CANONICAL configuration is v2 SEA-CELL: raw_weather_sea.csv (wind, precip,
# WMO) joined to raw_marine_era5_sea.csv (waves). raw_rainfall.csv and
# raw_weather.csv sit on the LAND cell that F-10 condemned and are retained
# only behind --v1-historical for reproducing pre-migration findings.
    if "--v1-historical" in __import__("sys").argv:
        w = pd.read_csv(DATA / "raw_weather.csv", skiprows=3)
        m = pd.read_csv(DATA / "raw_marine.csv", skiprows=3)
        r = pd.read_csv(DATA / "raw_rainfall.csv", skiprows=3)
        precip = r["precipitation (mm)"].values
        time = pd.to_datetime(w["time"])
        wave = m["wave_height (m)"].values
        wind = w["wind_speed_10m (kn)"].values
        wmo = w["weather_code (wmo code)"].values
    else:
        w = pd.read_csv(DATA / "raw_weather_sea.csv", skiprows=3)
        m = pd.read_csv(DATA / "raw_marine_era5_sea.csv", skiprows=3)
        w["time"] = pd.to_datetime(w["time"])
        m["time"] = pd.to_datetime(m["time"])
        j = w.merge(m, on="time", how="inner").dropna(
            subset=["wind_speed_10m (kn)", "wave_height (m)", "precipitation (mm)"])
        time = j["time"]
        wind = j["wind_speed_10m (kn)"].values
        wmo = j["weather_code (wmo code)"].values
        wave = j["wave_height (m)"].values
        precip = j["precipitation (mm)"].values
    d = pd.DataFrame({
        "time": time,
        "wind": wind,
        "wmo":  wmo,
        "wave": wave,
        "precip": precip,
    })
    d["hour"] = d["time"].dt.hour
    return d


def classify_all(d, vessel):
    """Return an (n, 5) array of per-function severities in FUNCS order."""
    lo, hi = VESSEL_THRESHOLDS[vessel]
    g_w = np.where(d["wind"] > W_UNSAFE, 2, np.where(d["wind"] > W_CAUTION, 1, 0))
    storm = (d["precip"] > R_UNSAFE) | d["wmo"].isin([95, 96, 99])
    g_r = np.where(storm, 2, np.where(d["precip"] > R_CAUTION, 1, 0))
    g_m = np.zeros(len(d), dtype=int)                      # no historical data
    g_o = np.where(d["wave"] > hi, 2, np.where(d["wave"] >= lo, 1, 0))
    g_t = _canonical_g_t(d["time"], d["hour"])
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



# --- SDR-001 / C-8: register writes are OPT-IN, never silent -------------
# C-5 and C-7 found that this script wrote data/prediction-register.csv on
# every run. An analysis script that rewrites resolved verdicts whenever the
# specification moves records nothing. Writing now requires an explicit flag.
def _register_write_enabled():
    import os, sys
    return ("--write-register" in sys.argv
            or os.environ.get("ALLOW_REGISTER_WRITE") == "1")


def _register_guard(reg, pid):
    """Refuse to overwrite an already-resolved prediction.

    Added 2026-09-08. Twice, re-running an analysis after a SPECIFICATION
    change silently rewrote verdicts for predictions registered against an
    earlier configuration (P09, P18 — both restored by hand). A register whose
    verdicts move whenever the specification moves records nothing. Resolved
    entries are therefore immutable here: a prediction that no longer holds
    under a new specification is handled by an explicit, documented
    re-resolution (as P16 and P22 were), never by a silent re-run.
    """
    row = reg.loc[reg.id == pid]
    return not (len(row) and str(row["status"].iloc[0]).strip() in ("CONFIRMED", "REFUTED"))


def main():
    d = load()
    print(__doc__)
    print(f"Loaded {len(d):,} records: {d.time.min()} to {d.time.max()}")

    day = _is_daylight(d["time"], d["hour"])   # astronomical daylight
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

    s_day_c, _ = binding_report(G_day, "DAYLIGHT (sunrise-sunset)", target_state=1)
    results["P05"] = s_day_c.get("g_o", 0)

    s_day_all, _ = binding_report(G_day, "DAYLIGHT (sunrise-sunset)")
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
        if _register_guard(reg, pid):
            reg.loc[reg.id == pid, "actual"] = round(float(actual), 2)
        if _register_guard(reg, pid):
            reg.loc[reg.id == pid, "status"] = status
        if _register_guard(reg, pid):
            reg.loc[reg.id == pid, "resolved"] = "2026-09-06"

    if _register_write_enabled():
        reg.to_csv(DATA / "prediction-register.csv", index=False)
        print("Register updated (explicit --write-register).")
    else:
        print("Register NOT written (read-only default; pass --write-register to enable).")


if __name__ == "__main__":
    main()
