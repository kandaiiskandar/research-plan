#!/usr/bin/env python3
"""
Threshold comparison: MET Malaysia official criteria vs hydrodynamic evidence.

POSITION (agreed 2026-09-06): MET Malaysia remains the authoritative source for
classification thresholds. Yaakob et al. (2015) and Jeong & Im (2023) are used
as a comparison, not a replacement. The gap between them is itself a finding.

Question: how often would each candidate threshold fire on five years of real
site data, and what does that say about whether national warning criteria
transfer to small-vessel departure decisions?

Data: MFWAM ~8 km (best available), 2021-10 to 2024-12, Kota Kinabalu.
"""

import pandas as pd
import numpy as np
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

# ---------------------------------------------------------------------------
# Candidate wave-height thresholds for a SMALL vessel (< 10 GRT)
# ---------------------------------------------------------------------------
THRESHOLDS = [
    # label                                  value  source
    ("MET Cat 1 — 'dangerous to small craft'", 3.50, "MET Malaysia Kriteria Amaran (official)"),
    ("MET Cat 2 — 'dangerous to all fishing'", 4.50, "MET Malaysia Kriteria Amaran (official)"),
    ("Current model — small UNSAFE",           1.90, "This architecture (SS4 = 1.875 m, rounded)"),
    ("Yaakob Boat A (6.54 m) — fails SS4",     1.875, "NORDFORSK seakeeping failure"),
    ("Yaakob Boat A — operational ceiling",    1.25, "NORDFORSK, top of Sea State 3"),
    ("Current model — small CAUTION onset",    1.00, "This architecture"),
    ("Jeong & Im — vessels <= 10 m LOA",       1.00, "Wolfson/Hs_KIMO, 66 capsizings"),
    ("Yaakob Boat B (5.03 m) — fails SS3",     0.875, "NORDFORSK seakeeping failure"),
    ("Yaakob Boat B — operational ceiling",    0.50, "NORDFORSK, top of Sea State 2"),
]


def main():
    m = pd.read_csv(DATA / "raw_marine_mfwam.csv", skiprows=3)
    m.columns = ["time", "wave", "period"]
    m["time"] = pd.to_datetime(m["time"])
    m = m.dropna(subset=["wave"])
    m["hr"] = m["time"].dt.hour
    day = m[(m.hr >= 6) & (m.hr < 17)]
    dep = m[(m.hr >= 5) & (m.hr <= 9)]

    n, nd = len(m), len(day)
    print("=" * 88)
    print("THRESHOLD COMPARISON — MET official criteria vs hydrodynamic evidence")
    print("=" * 88)
    print(f"Data: MFWAM ~8 km, {m.time.min().date()} to {m.time.max().date()}")
    print(f"      {n:,} hourly records   |   observed wave range "
          f"{m.wave.min():.2f} – {m.wave.max():.2f} m   mean {m.wave.mean():.2f} m")
    print()
    print(f"{'threshold':<42}{'m':>7}{'hrs exceeded':>14}{'% all':>8}{'% daylight':>12}")
    print("-" * 88)
    for label, val, _ in THRESHOLDS:
        ex = int((m.wave > val).sum())
        exd = int((day.wave > val).sum())
        mark = "  <-- NEVER" if ex == 0 else ""
        print(f"{label:<42}{val:>7.3f}{ex:>14,}{100*ex/n:>7.1f}%{100*exd/nd:>11.1f}%{mark}")

    print()
    print("=" * 88)
    print("THE GAP")
    print("=" * 88)
    met = 3.50
    for label, val, src in THRESHOLDS:
        if "Yaakob" in label or "Jeong" in label:
            print(f"  MET Cat 1 ({met} m) is {met/val:5.1f}x above  {label}  ({val} m)")

    print()
    print("=" * 88)
    print("WHAT EACH THRESHOLD SET WOULD PRODUCE — small vessel, departure window 05-09")
    print("=" * 88)
    sets = {
        "MET-anchored (current model)":        (1.00, 1.90),
        "MET Category 1 literal":              (1.75, 3.50),   # midpoint / Cat1 max
        "Yaakob Boat A (6.54 m hull)":         (0.875, 1.25),
        "Yaakob Boat B (5.03 m hull)":         (0.30, 0.50),
        "Jeong & Im <=10 m LOA":               (1.00, 2.00),
    }
    print(f"{'threshold set':<34}{'SAFE':>10}{'CAUTION':>10}{'UNSAFE':>10}   basis")
    for label, (lo, hi) in sets.items():
        g = np.where(dep.wave > hi, 2, np.where(dep.wave >= lo, 1, 0))
        c = np.bincount(g, minlength=3) / len(dep) * 100
        print(f"{label:<34}{c[0]:>9.1f}%{c[1]:>9.1f}%{c[2]:>9.1f}%")

    print()
    print("=" * 88)
    print("READING")
    print("=" * 88)
    print("MET criteria are NATIONAL WARNING thresholds — designed to trigger public")
    print("broadcast alerts, and therefore designed to be rare. They are not calibrated")
    print("to the departure decision of an individual 5-7 m hull.")
    print()
    print("Yaakob et al. measured two actual Malaysian boats against NORDFORSK criteria.")
    print("Their operability ceilings sit far below anything MET would warn about.")
    print()
    print("Both are correct for their own purpose. The gap between them is the finding:")
    print("a vessel can be well outside its documented seakeeping envelope while no")
    print("official warning is in force — which is precisely what Jeong & Im observed")
    print("in Korea, where 82% of capsizings occurred on days with no warning issued.")


if __name__ == "__main__":
    main()
