#!/usr/bin/env python3
"""
Raw data collection v2 — Kota Kinabalu
=======================================
Collects two additional raw datasets to resolve open questions Q1a and Q6.
See docs/canonical/decision-record-empirical-first.md

WHAT THIS FIXES
---------------
Q1a — the v1 weather request did not set cell_selection, which defaults to
      "land". It returned a LAND grid cell (5.940246, 116.100006) while the
      marine request returned a SEA cell (6.0, 116.0), ~12 km away. Wind over
      land is materially lower than over water, and sustained wind in v1 never
      exceeds 17.8 kn against a 22 kn threshold. This run forces sea cells.

Q6  — v1 wave data used era5_ocean at 0.5 deg (~50 km), the coarsest model
      available. It carries 97.5% of daylight CAUTION decisions. This run also
      collects MeteoFrance MFWAM at ~8 km for the overlapping period so the
      resolution sensitivity can be measured rather than assumed.

DOES NOT OVERWRITE v1
---------------------
Writes to *_sea.csv and *_mfwam.csv. The v1 files are the baseline that
predictions P01-P04 in data/prediction-register.csv are locked against.
Overwriting them would flip those predictions for the wrong reason — because
the data changed, not because the model was wrong.

SAME-LOCATION DISCIPLINE
------------------------
The weather and marine APIs use different models on different grids, so they
can never resolve to an identical cell. What this script does instead:
  1. requests every dataset at the SAME lat/lon
  2. records the coordinates each API actually returns
  3. computes the separation in km and prints a reconciliation table
  4. warns if any pair is more than SEPARATION_WARN_KM apart

Usage:
    python3 scripts/collect_raw_v2.py
    python3 scripts/collect_raw_v2.py --start 2020-01-01 --end 2024-12-31
"""

import argparse
import csv
import json
import math
import urllib.request
import urllib.parse
from pathlib import Path

# --- Study site. Kota Kinabalu, Sabah. Keep identical across all requests. ---
LATITUDE = 5.98
LONGITUDE = 116.01
TIMEZONE = "Asia/Kuching"

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "data"
SEPARATION_WARN_KM = 15.0

# MFWAM coverage begins Oct 2021 — earlier dates will return empty or error.
MFWAM_MIN_START = "2021-10-01"


def haversine_km(lat1, lon1, lat2, lon2):
    R = 6371.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * R * math.asin(math.sqrt(a))


def download(url, path, label):
    print(f"\n[{label}]")
    print(f"  GET {url[:110]}...")
    try:
        urllib.request.urlretrieve(url, path)
    except Exception as e:
        print(f"  FAILED: {e}")
        return None
    kb = path.stat().st_size / 1024
    print(f"  saved {path.name}  ({kb:.0f} KB)")
    return read_returned_coords(path, label)


def read_returned_coords(path, label):
    """Open-Meteo CSV puts metadata on row 2. Returns (lat, lon, rows)."""
    try:
        with open(path) as f:
            rows = list(csv.reader(f))
        lat, lon = float(rows[1][0]), float(rows[1][1])
        n = sum(1 for r in rows[4:] if r and r[0])
        print(f"  returned grid cell: {lat}, {lon}   ({n:,} data rows)")
        return {"label": label, "lat": lat, "lon": lon, "rows": n, "file": path.name}
    except Exception as e:
        print(f"  could not parse coordinates: {e}")
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", default="2020-01-01")
    ap.add_argument("--end", default="2024-12-31")
    args = ap.parse_args()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 74)
    print("RAW COLLECTION v2")
    print(f"requested location : {LATITUDE}, {LONGITUDE}   ({TIMEZONE})")
    print(f"period             : {args.start} to {args.end}")
    print("=" * 74)

    results = []

    # ---- 1. Weather with cell_selection=sea  (Q1a) -----------------------
    wx = urllib.parse.urlencode({
        "latitude": LATITUDE, "longitude": LONGITUDE,
        "hourly": "wind_speed_10m,wind_direction_10m,wind_gusts_10m,precipitation,weather_code",
        "wind_speed_unit": "kn",
        "start_date": args.start, "end_date": args.end,
        "timezone": TIMEZONE, "format": "csv",
        "cell_selection": "sea",          # <-- the fix
    })
    r = download(f"https://archive-api.open-meteo.com/v1/archive?{wx}",
                 OUTPUT_DIR / "raw_weather_sea.csv", "weather / SEA cell")
    if r: results.append(r)

    # ---- 2. Marine, era5_ocean, sea cell, same point (baseline re-check) --
    mar = urllib.parse.urlencode({
        "latitude": LATITUDE, "longitude": LONGITUDE,
        "hourly": "wave_height,wave_period",
        "models": "era5_ocean",
        "start_date": args.start, "end_date": args.end,
        "timezone": TIMEZONE, "format": "csv",
        "cell_selection": "sea",
    })
    r = download(f"https://marine-api.open-meteo.com/v1/marine?{mar}",
                 OUTPUT_DIR / "raw_marine_era5_sea.csv", "marine / ERA5-Ocean ~50km")
    if r: results.append(r)

    # ---- 3. Marine, MFWAM ~8 km, overlap period only  (Q6) ---------------
    mfwam_start = max(args.start, MFWAM_MIN_START)
    print(f"\n  note: MFWAM coverage starts {MFWAM_MIN_START}; using {mfwam_start}")
    mf = urllib.parse.urlencode({
        "latitude": LATITUDE, "longitude": LONGITUDE,
        "hourly": "wave_height,wave_period",
        "models": "meteofrance_wave",
        "start_date": mfwam_start, "end_date": args.end,
        "timezone": TIMEZONE, "format": "csv",
        "cell_selection": "sea",
    })
    r = download(f"https://marine-api.open-meteo.com/v1/marine?{mf}",
                 OUTPUT_DIR / "raw_marine_mfwam.csv", "marine / MFWAM ~8km")
    if r: results.append(r)
    else:
        print("  If this failed, the model identifier may differ. Check")
        print("  https://open-meteo.com/en/docs/marine-weather-api for the")
        print("  current name (the docs list it as 'MeteoFrance Wave').")

    # ---- Same-location reconciliation ------------------------------------
    print("\n" + "=" * 74)
    print("SAME-LOCATION CHECK")
    print("=" * 74)
    if not results:
        print("No datasets collected — nothing to reconcile.")
        return

    print(f"{'dataset':<28}{'returned cell':<26}{'km from request':>16}")
    for r in results:
        d = haversine_km(LATITUDE, LONGITUDE, r["lat"], r["lon"])
        print(f"{r['label']:<28}{r['lat']:.4f}, {r['lon']:.4f}{'':<6}{d:>13.1f}")

    print(f"\n{'pair separation':<52}{'km':>10}")
    worst = 0.0
    for i in range(len(results)):
        for j in range(i + 1, len(results)):
            a, b = results[i], results[j]
            d = haversine_km(a["lat"], a["lon"], b["lat"], b["lon"])
            worst = max(worst, d)
            flag = "  <-- CHECK" if d > SEPARATION_WARN_KM else ""
            print(f"{a['label']} <-> {b['label']:<20}{d:>10.1f}{flag}")

    print()
    if worst > SEPARATION_WARN_KM:
        print(f"WARNING: largest separation {worst:.1f} km exceeds "
              f"{SEPARATION_WARN_KM} km.")
        print("The classifier would again be combining variables measured at")
        print("materially different places. Record this in data-provenance.md")
        print("before using the data.")
    else:
        print(f"OK: all datasets within {SEPARATION_WARN_KM} km "
              f"(largest separation {worst:.1f} km).")
    print("\nv1 baseline for comparison: weather 5.9402,116.1000 (LAND) vs")
    print("marine 6.0000,116.0000 (sea) = 12.3 km apart.")

    print("\n" + "=" * 74)
    print("NEXT: predictions P15-P18 in data/prediction-register.csv were")
    print("registered before this run. Compare results against them.")
    print("=" * 74)


if __name__ == "__main__":
    main()
