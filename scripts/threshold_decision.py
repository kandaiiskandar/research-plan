#!/usr/bin/env python3
"""
Decision support: small-vessel UNSAFE at 1.90 m (current) vs 1.25 m (proposed).

Current 1.90 m derives from Yaakob Boat A's NORDFORSK *failure point* (SS4).
Proposed 1.25 m is Boat A's *operational ceiling* (top of SS3) — the same source,
a different quantity, and arguably the more apt one for a departure gate.

Produces the complete picture so the decision is not made on one number:
  - state distributions across three time windows
  - whether UNSAFE becomes weather-driven or stays a night curfew
  - effect on the Level 2 headline figure
  - sensitivity across the plausible range

Data: sea-cell wind + MFWAM 8 km (best available), 2021-10 to 2024-12.
"""

import pandas as pd
import numpy as np
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
CAUTION_ON = 1.0          # small-vessel CAUTION onset, unchanged
CANDIDATES = [1.90, 1.75, 1.50, 1.25, 1.00]


def load():
    w = pd.read_csv(DATA / "raw_weather_sea.csv", skiprows=3)
    w.columns = ["time", "wind", "dir", "gust", "precip", "wmo"]
    m = pd.read_csv(DATA / "raw_marine_mfwam.csv", skiprows=3)
    m.columns = ["time", "wave", "period"]
    for d in (w, m):
        d["time"] = pd.to_datetime(d["time"])
    d = w.merge(m[["time", "wave"]], on="time").dropna(subset=["wave"]).reset_index(drop=True)
    d["hr"] = d["time"].dt.hour
    d["g_w"] = np.where(d.wind > 27, 2, np.where(d.wind > 22, 1, 0))
    d["g_r"] = np.where((d.precip > 20) | d.wmo.isin([95, 96, 99]), 2,
                        np.where(d.precip > 7.5, 1, 0))
    d["g_t"] = np.where((d.hr >= 6) & (d.hr < 17), 0,
                        np.where((d.hr >= 17) & (d.hr < 19), 1, 2))
    return d


def classify(d, unsafe_at):
    g_o = np.where(d.wave > unsafe_at, 2, np.where(d.wave >= CAUTION_ON, 1, 0))
    f = np.max(np.vstack([d.g_w.values, d.g_r.values, d.g_t.values, g_o]), axis=0)
    return f, g_o


def dist(f):
    c = np.bincount(f, minlength=3)
    return 100 * c / len(f)


def main():
    d = load()
    print(__doc__)
    print(f"Records: {len(d):,}   wave range {d.wave.min():.2f}–{d.wave.max():.2f} m\n")

    windows = {
        "ALL HOURS":              np.ones(len(d), bool),
        "DEPARTURE 05:00-09:00": ((d.hr >= 5) & (d.hr <= 9)).values,
        "DAYLIGHT 06:00-17:00":  ((d.hr >= 6) & (d.hr < 17)).values,
    }

    print("=" * 78)
    print("1.  STATE DISTRIBUTION BY UNSAFE THRESHOLD")
    print("=" * 78)
    for wl, mask in windows.items():
        print(f"\n{wl}   (n = {mask.sum():,})")
        print(f"  {'UNSAFE at':<12}{'SAFE':>9}{'CAUTION':>10}{'UNSAFE':>9}")
        for u in CANDIDATES:
            f, _ = classify(d, u)
            p = dist(f[mask])
            tag = "  <- current" if u == 1.90 else ("  <- proposed" if u == 1.25 else "")
            print(f"  {u:<12.2f}{p[0]:>8.1f}%{p[1]:>9.1f}%{p[2]:>8.1f}%{tag}")

    print("\n" + "=" * 78)
    print("2.  IS UNSAFE WEATHER-DRIVEN OR JUST DARKNESS?")
    print("=" * 78)
    print(f"  {'UNSAFE at':<12}{'UNSAFE hrs':>12}{'by night':>11}{'by weather':>12}{'weather %':>11}")
    for u in CANDIDATES:
        f, g_o = classify(d, u)
        un = f == 2
        night = (d.g_t.values[un] == 2).sum()
        wx = ((g_o[un] == 2) | (d.g_w.values[un] == 2) | (d.g_r.values[un] == 2)).sum()
        tag = "  <- current" if u == 1.90 else ("  <- proposed" if u == 1.25 else "")
        print(f"  {u:<12.2f}{int(un.sum()):>12,}{night:>11,}{wx:>12,}{100*wx/max(un.sum(),1):>10.1f}%{tag}")
    print("\n  (night and weather overlap — an hour can be both)")

    print("\n" + "=" * 78)
    print("3.  DAYLIGHT-ONLY UNSAFE — the darkness-free test")
    print("=" * 78)
    day = windows["DAYLIGHT 06:00-17:00"]
    print(f"  {'UNSAFE at':<12}{'UNSAFE hrs in daylight':>26}{'% of daylight':>16}")
    for u in CANDIDATES:
        f, _ = classify(d, u)
        n = int((f[day] == 2).sum())
        tag = "  <- current" if u == 1.90 else ("  <- proposed" if u == 1.25 else "")
        print(f"  {u:<12.2f}{n:>26,}{100*n/day.sum():>15.2f}%{tag}")

    print("\n" + "=" * 78)
    print("4.  EFFECT ON THE HEADLINE (Level 2 binding, departure window)")
    print("=" * 78)
    dep = windows["DEPARTURE 05:00-09:00"]
    for u in [1.90, 1.25]:
        f, _ = classify(d, u)
        p = dist(f[dep])
        label = "current 1.90 m" if u == 1.90 else "proposed 1.25 m"
        print(f"  {label:<18} CAUTION {p[1]:.1f}%   UNSAFE {p[2]:.1f}%")

    print("\n" + "=" * 78)
    print("5.  READING")
    print("=" * 78)
    f19, _ = classify(d, 1.90)
    f12, _ = classify(d, 1.25)
    d19 = int((f19[day] == 2).sum())
    d12 = int((f12[day] == 2).sum())
    print(f"  At 1.90 m: daylight UNSAFE occurs {d19} times in {day.sum():,} hours.")
    print(f"  At 1.25 m: daylight UNSAFE occurs {d12} times.")
    print()
    print("  The question is not which number is larger. It is whether the UNSAFE")
    print("  state is exercised by ENVIRONMENTAL conditions at all, or is purely a")
    print("  function of the clock. At 1.90 m the participation gate is a night")
    print("  curfew. Whether 1.25 m changes that materially is the decision.")


if __name__ == "__main__":
    main()
