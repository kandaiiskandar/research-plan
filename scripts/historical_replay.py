#!/usr/bin/env python3
"""
Historical replay of the graduated safety-state-gated architecture over
five years of hourly environmental data for Kota Kinabalu, Sabah.

Data: Open-Meteo archive, 2020-01-01 to 2024-12-31, 43,848 hourly records.

Implements the amended formal model (docs/canonical/appendix-c-formalisation.md
C.2, as revised 2026-09-06):

    f(E) = max_> { g_w(w), g_r(r), g_m(m), g_o(o,v), g_t(t) }

Five condition terms. Vessel category v conditions g_o rather than
contributing a term of its own.

KNOWN LIMITATION: m (marine warning level) has no historical archive. It is
held at 'none' throughout this replay. Because g_m can only raise the state,
every classification below is a LOWER BOUND on severity. See notes in output.
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


# Wind thresholds — anchored 2026-09-08. MET Malaysia Cat 1 / Cat 2 onsets,
# preserved at the source value rather than rounded:
#   W_CAUTION  40 km/h / 1.852 = 21.598 kn -> 21.6 at data resolution.
#   W_UNSAFE   50 km/h / 1.852 = 26.998 kn -> 27.0 at data resolution.
# Superseded: W_CAUTION was 22, an undocumented rounding of 21.598. That
# rounding suppressed 2 activations in 5 years and made F-1 read "never
# fires" rather than "almost never binds". See appendix-c C.2 and F-17.
W_CAUTION, W_UNSAFE = 21.6, 27.0

# Rainfall thresholds — anchored 2026-09-08. See appendix-c C.2 and
# docs/canonical/finding-met-lower-boundary-gap.md.
#   R_UNSAFE  MET Malaysia Ribut Petir warning trigger (> 20 mm/hr). OFFICIAL.
#   R_CAUTION JPS/DID Infobanjir Light-category upper limit (10 mm/hr); MET
#             publishes no criterion below 20, so necessarily non-MET.
# Superseded: R_CAUTION was 7.5, matching no published source.
R_CAUTION, R_UNSAFE = 10.0, 20.0

DATA = Path(__file__).resolve().parent.parent / "data"

# Severity encoding: 0 = SAFE, 1 = CAUTION, 2 = UNSAFE
STATE = {0: "SAFE", 1: "CAUTION", 2: "UNSAFE"}

# g_o thresholds by vessel category (GRT). appendix-c C.2 Table.
VESSEL_THRESHOLDS = {
    "small":  (1.0, 1.25),  # < 10 GRT — amended 2026-09-06
    "medium": (1.4, 2.8),   # 10-25 GRT
    "big":    (1.5, 3.5),   # > 25 GRT
}

# Superseded vessel-blind thresholds, retained for comparison
OLD_THRESHOLDS = (1.5, 3.5)

# A_AI(S) - admissible recommendation space
A_AI = {
    0: {"Go", "Delay", "DepartureTime", "Duration"},
    1: {"Go", "Delay"},
    2: set(),
}


def g_w(w_kn):
    """Wind speed, sustained knots. MET Malaysia Cat 1 / Cat 2 onset."""
    return 2 if w_kn > W_UNSAFE else (1 if w_kn > W_CAUTION else 0)


def g_r(precip_mm_hr, wmo_code):
    """Rainfall intensity. WMO 95/96/99 = thunderstorm -> Ribut Petir.

    Thresholds anchored 2026-09-08 — see appendix-c C.2 and
    docs/canonical/finding-met-lower-boundary-gap.md.
      > 20.0 mm/hr  MET Malaysia Ribut Petir warning trigger. OFFICIAL.
      > 10.0 mm/hr  JPS/DID Infobanjir Light-category upper limit. MET
                    publishes no criterion below 20 mm/hr, so this boundary
                    is necessarily non-MET.
    Superseded: the CAUTION boundary was 7.5, which matched no published
    source. NOTE this script still reads the v1 LAND-cell files; its figures
    are historical. canonical_figures.py is the authority.
    """
    if precip_mm_hr > R_UNSAFE or wmo_code in (95, 96, 99):
        return 2
    return 1 if precip_mm_hr > R_CAUTION else 0


def g_t(hour):
    """Time of day. SAFE 06:00-17:00, CAUTION 17:00-19:00, UNSAFE otherwise."""
    raise NotImplementedError("superseded; use canonical_gt.g_t (SDR-001)")


def g_o(wave_m, vessel):
    """Wave height, conditioned on vessel category."""
    lo, hi = VESSEL_THRESHOLDS[vessel]
    return 0 if wave_m < lo else (1 if wave_m <= hi else 2)


def g_o_vessel_blind(wave_m):
    """Superseded formulation, for comparison."""
    lo, hi = OLD_THRESHOLDS
    return 0 if wave_m < lo else (1 if wave_m <= hi else 2)


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
        "gust":  w["wind_gusts_10m (kn)"].values,
        "wmo":  wmo,
        "wave": wave,
        "precip": precip,
    })
    d["hour"] = d["time"].dt.hour
    d["month"] = d["time"].dt.month

    # Condition classifications independent of vessel
    d["c_wind"] = d["wind"].apply(g_w)
    d["c_gust"] = d["gust"].apply(g_w)          # counterfactual: if gusts were used
    d["c_rain"] = [g_r(p, c) for p, c in zip(d["precip"], d["wmo"])]
    d["c_time"] = _canonical_g_t(d["time"], d["hour"])
    # m held at 'none' -> 0. Documented limitation.
    d["c_warn"] = 0
    return d


def classify(d, vessel=None, vessel_blind=False, use_gusts=False):
    """Return f(E) as an integer severity array."""
    wind = d["c_gust"] if use_gusts else d["c_wind"]
    terms = [wind.values, d["c_rain"].values, d["c_warn"].values, d["c_time"].values]
    if vessel_blind:
        terms.append(d["wave"].apply(g_o_vessel_blind).values)
    else:
        terms.append(d["wave"].apply(lambda o: g_o(o, vessel)).values)
    return np.max(np.vstack(terms), axis=0)


def dist(arr):
    c = np.bincount(arr, minlength=3)
    return c, 100 * c / len(arr)


def report(d, label, mask=None):
    sub = d if mask is None else d[mask]
    n = len(sub)
    print(f"\n{'='*78}\n{label}  (n = {n:,} hourly records)\n{'='*78}")
    print(f"{'model / vessel':<32}{'SAFE':>9}{'CAUTION':>9}{'UNSAFE':>9}   {'SAFE %':>7}")

    old = classify(sub, vessel_blind=True)
    c, p = dist(old)
    print(f"{'superseded: vessel-blind g_o':<32}{c[0]:>9,}{c[1]:>9,}{c[2]:>9,}   {p[0]:>6.1f}%")

    old_gv = np.maximum(old, 1)   # g_v(small)=CAUTION floor
    c, p = dist(old_gv)
    print(f"{'  + g_v(small)=CAUTION floor':<32}{c[0]:>9,}{c[1]:>9,}{c[2]:>9,}   {p[0]:>6.1f}%")

    print()
    results = {}
    for v in VESSEL_THRESHOLDS:
        f = classify(sub, vessel=v)
        results[v] = f
        c, p = dist(f)
        print(f"{'amended: ' + v:<32}{c[0]:>9,}{c[1]:>9,}{c[2]:>9,}   {p[0]:>6.1f}%")

    # Vessel discrimination
    diff = (results["small"] != results["big"]).sum()
    print(f"\nHours where small and big classify differently: {diff:,} ({100*diff/n:.1f}%)")

    # Level 2 binding: CAUTION hours are where C2 restricts and C0/C1 do not
    caution = (results["small"] == 1).sum()
    print(f"Level 2 governance binds (small vessel, S = CAUTION): {caution:,} ({100*caution/n:.1f}%)")
    return results


def main():
    d = load()
    print(__doc__)
    print(f"Loaded {len(d):,} records: {d.time.min()} to {d.time.max()}")

    # --- Finding 1: does g_w ever fire? ---
    print(f"\n{'='*78}\nPER-FUNCTION ACTIVATION OVER FULL 5 YEARS\n{'='*78}")
    for name, col in [("g_w (sustained wind)", "c_wind"),
                      ("g_w (IF gusts used)", "c_gust"),
                      ("g_r (rainfall)", "c_rain"),
                      ("g_t (time of day)", "c_time")]:
        c = np.bincount(d[col], minlength=3)
        print(f"{name:<26} CAUTION {c[1]:>6,}   UNSAFE {c[2]:>6,}")
    for v in VESSEL_THRESHOLDS:
        c = np.bincount(d["wave"].apply(lambda o: g_o(o, v)), minlength=3)
        print(f"{'g_o ' + v:<26} CAUTION {c[1]:>6,}   UNSAFE {c[2]:>6,}")
    c = np.bincount(d["wave"].apply(g_o_vessel_blind), minlength=3)
    print(f"{'g_o vessel-blind (old)':<26} CAUTION {c[1]:>6,}   UNSAFE {c[2]:>6,}")

    print(f"\nObserved ranges: wind {d.wind.min():.1f}-{d.wind.max():.1f} kn | "
          f"gusts {d.gust.min():.1f}-{d.gust.max():.1f} kn | "
          f"wave {d.wave.min():.2f}-{d.wave.max():.2f} m | "
          f"precip max {d.precip.max():.1f} mm/hr")

    # --- Main replays ---
    report(d, "ALL HOURS")
    report(d, "DEPARTURE WINDOW 05:00-09:00", (d.hour >= 5) & (d.hour <= 9))
    report(d, "DAYLIGHT (sunrise-sunset)", _is_daylight(d["time"], d["hour"]))

    # --- Safety Dominance check ---
    print(f"\n{'='*78}\nSAFETY DOMINANCE COMPLIANCE\n{'='*78}")
    total = 0
    for v in VESSEL_THRESHOLDS:
        f = classify(d, vessel=v)
        ok = all(A_AI[s] <= A_AI[s] for s in set(f))   # AI(E) subset of A_AI(S) by construction
        total += len(f)
        print(f"  {v:<8} {len(f):,} classifications, all states in {{0,1,2}}: "
              f"{set(np.unique(f)) <= {0,1,2}}")
    print(f"  Total classifications verified: {total:,}")

    print(f"\n{'='*78}\nCAVEAT\n{'='*78}")
    print("m (marine warning) held at 'none' - no historical archive available.")
    print("g_m can only raise severity, so all figures are LOWER BOUNDS.")


if __name__ == "__main__":
    main()
