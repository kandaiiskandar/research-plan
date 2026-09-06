#!/usr/bin/env python3
"""
THE authoritative figure generator. Every number in §0a of
`empirical-findings-2026-09-06.md` comes from here.

WHY THIS SCRIPT EXISTS
----------------------
On 2026-09-06 a coverage check found that the published binding-profile
figures (F-4 10.7%, F-7 97.5% / 3.4% / 88.2%) reproduced ONLY under the v1
land-cell data AND the superseded 1.9 m threshold. They had been left
untouched when the threshold amendment was propagated: the constants in the
analysis scripts were updated, but the findings were never recomputed. The
paper was printing them alongside 6.1%, which came from different data at a
different threshold, as though one analysis had produced all of them.

Three scripts (historical_replay, diagnostic_binding, hysteresis_analysis)
still read `raw_weather.csv` (the LAND cell that F-10 identified as wrong) and
`raw_marine.csv` (ERA5-Ocean 50 km). This script supersedes their figure
reporting. It reads sea-cell data only.

THE TWO CONFIGURATIONS (decision of 2026-09-06, "option C")
-----------------------------------------------------------
Both use sea-cell weather, so the F-10 land/sea error is corrected in both,
and both use the amended small-vessel thresholds 1.0 / 1.25 m.

  PRIMARY    sea wind + ERA5-Ocean waves (~50 km)   2020-01..2024-12   5.00 yr
  RESOLUTION sea wind + MFWAM waves      (~8 km)    2021-10..2024-12   3.25 yr

PRIMARY is the headline: full five-year record, sea cells throughout.
RESOLUTION is the sensitivity check: finer waves, shorter record. The gap
between them quantifies grid-resolution dependence rather than hiding it.

Neither is "the right one". Reporting both is the point — see F-14.

A NOTE ON THE PREDICTION REGISTER
---------------------------------
These figures are NOT registered as predictions. They are recomputations of
quantities whose values were already observed during the coverage check.
Registering them now would invert the method: the register exists so that
expectations are recorded before results are seen, and back-filling it with
known values would make it decorative. P01-P24 stand as they are. The
superseded entries (P04, P05, P19, P22) remain valid for the configurations
they were registered against and are annotated accordingly.
"""

import pandas as pd
import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

SAFE, CAUTION, UNSAFE = 0, 1, 2

# Vessel-conditional wave thresholds, amended 2026-09-06 (Yaakob operational
# ceiling rather than NORDFORSK failure point for the small row).
TH = {"small": (1.0, 1.25), "medium": (1.4, 2.8), "big": (1.5, 3.5)}

CONFIGS = {
    "PRIMARY": {
        "weather": "raw_weather_sea.csv",
        "marine": "raw_marine_era5_sea.csv",
        "wave_model": "ERA5-Ocean ~50 km",
    },
    "RESOLUTION": {
        "weather": "raw_weather_sea.csv",
        "marine": "raw_marine_mfwam.csv",
        "wave_model": "MFWAM ~8 km",
    },
}


def load(cfg):
    """Sea-cell weather joined to the configured wave model.

    Precipitation is taken from `raw_weather_sea.csv`, NOT `raw_rainfall.csv`.
    The latter is still sited on the land cell (F-10). This resolves the
    outstanding rainfall-provenance item as a side effect.
    """
    w = pd.read_csv(DATA / cfg["weather"], skiprows=3)
    m = pd.read_csv(DATA / cfg["marine"], skiprows=3)
    w["time"] = pd.to_datetime(w["time"])
    m["time"] = pd.to_datetime(m["time"])

    d = w.merge(m, on="time", how="inner").rename(columns={
        "wind_speed_10m (kn)": "wind",
        "weather_code (wmo code)": "wmo",
        "precipitation (mm)": "precip",
        "wave_height (m)": "wave",
    })
    d = d.dropna(subset=["wave", "wind", "precip"])
    d["hour"] = d["time"].dt.hour
    return d.sort_values("time").reset_index(drop=True)


def components(d, vessel):
    """The five component functions. g_m is held at `none` — no archive."""
    lo, hi = TH[vessel]
    g_w = np.where(d["wind"] > 27, UNSAFE, np.where(d["wind"] > 22, CAUTION, SAFE))
    storm = (d["precip"] > 20) | d["wmo"].isin([95, 96, 99])
    g_r = np.where(storm, UNSAFE, np.where(d["precip"] > 7.5, CAUTION, SAFE))
    g_o = np.where(d["wave"] > hi, UNSAFE, np.where(d["wave"] >= lo, CAUTION, SAFE))
    g_t = np.where((d["hour"] >= 6) & (d["hour"] < 17), SAFE,
                   np.where((d["hour"] >= 17) & (d["hour"] < 19), CAUTION, UNSAFE))
    g_m = np.full(len(d), SAFE)
    f = np.max(np.column_stack([g_w, g_r, g_m, g_o, g_t]), axis=1)
    return f, {"g_w": g_w, "g_r": g_r, "g_m": g_m, "g_o": g_o, "g_t": g_t}


def figures(name, cfg):
    d = load(cfg)
    f_small, g = components(d, "small")
    f_big, _ = components(d, "big")

    dep = ((d.hour >= 5) & (d.hour <= 9)).values
    day = ((d.hour >= 6) & (d.hour < 17)).values
    years = (d.time.max() - d.time.min()).days / 365.25

    caution_day = day & (f_small == CAUTION)
    nonsafe = f_small > SAFE

    r = {
        "n": len(d),
        "years": years,
        "start": d.time.min(),
        "end": d.time.max(),
        "wave_model": cfg["wave_model"],
        "level2_dep": 100 * (f_small[dep] == CAUTION).mean(),
        "unsafe_day_hrs": int(((f_small == UNSAFE) & day).sum()),
        "unsafe_day_pct": 100 * ((f_small == UNSAFE) & day).sum() / day.sum(),
        "vessel_dep": 100 * (f_small[dep] != f_big[dep]).mean(),
        "max_wind": d.wind.max(),
        "max_wave": d.wave.max(),
    }

    # Weather-driven share of UNSAFE: UNSAFE hours where something other than
    # g_t is at the maximum.
    uns = f_small == UNSAFE
    weather_driven = uns & ((g["g_o"] == UNSAFE) | (g["g_r"] == UNSAFE) | (g["g_w"] == UNSAFE))
    r["weather_unsafe_share"] = 100 * weather_driven.sum() / max(uns.sum(), 1)

    r["binding"] = {}
    for k, v in g.items():
        r["binding"][k] = {
            "day_caution": 100 * (v[caution_day] == f_small[caution_day]).mean() if caution_day.sum() else 0.0,
            "all_nonsafe": 100 * (v[nonsafe] == f_small[nonsafe]).mean() if nonsafe.sum() else 0.0,
        }
    return r


def main():
    print(__doc__)
    out = {k: figures(k, v) for k, v in CONFIGS.items()}

    print("=" * 78)
    print("CANONICAL FIGURES — small vessel (< 10 GRT), thresholds 1.0 / 1.25 m")
    print("=" * 78)
    print(f"\n{'':38}{'PRIMARY':>18}{'RESOLUTION':>18}")
    print(f"{'':38}{'5 yr, ERA5 50km':>18}{'3.25 yr, MFWAM':>18}")
    print("-" * 78)

    rows = [
        ("hourly records", "n", "{:,}"),
        ("years covered", "years", "{:.2f}"),
        ("Level 2 binds (departure 05-09)", "level2_dep", "{:.2f}%"),
        ("daylight UNSAFE hours", "unsafe_day_hrs", "{:,}"),
        ("daylight UNSAFE share", "unsafe_day_pct", "{:.2f}%"),
        ("weather-driven share of UNSAFE", "weather_unsafe_share", "{:.1f}%"),
        ("small vs big differ (departure)", "vessel_dep", "{:.2f}%"),
        ("max sustained wind (kn)", "max_wind", "{:.1f}"),
        ("max wave height (m)", "max_wave", "{:.2f}"),
    ]
    for label, key, fmt in rows:
        a = fmt.format(out["PRIMARY"][key])
        b = fmt.format(out["RESOLUTION"][key])
        print(f"  {label:<36}{a:>18}{b:>18}")

    print(f"\n{'  COMPONENT BINDING SHARES':<38}{'':>18}{'':>18}")
    print(f"  {'(share of hours at the maximum)':<36}")
    for comp in ["g_o", "g_t", "g_r", "g_w", "g_m"]:
        a = out["PRIMARY"]["binding"][comp]
        b = out["RESOLUTION"]["binding"][comp]
        print(f"  {comp + ' — daylight CAUTION':<36}{a['day_caution']:>17.2f}%{b['day_caution']:>17.2f}%")
        print(f"  {comp + ' — all-hours non-SAFE':<36}{a['all_nonsafe']:>17.2f}%{b['all_nonsafe']:>17.2f}%")

    p, s = out["PRIMARY"], out["RESOLUTION"]
    print(f"""
{'='*78}
HOW TO REPORT THESE
{'='*78}
  Headline           : Level 2 binds {p['level2_dep']:.1f}% of departure hours
                       (5 years, sea-cell weather, ERA5-Ocean 50 km waves)
  Resolution check   : {s['level2_dep']:.1f}% on MFWAM 8 km over 3.25 years
  The gap ({p['level2_dep']-s['level2_dep']:.1f} points) IS the grid-resolution sensitivity.
  Report both. Neither alone is the result.

  g_w never binds in either configuration. Max sustained wind {p['max_wind']:.1f} kn
  against a 22 kn threshold — a property of the site (F-13), not an artefact.
  g_m never binds because it was never measured. All figures are LOWER BOUNDS.
""")


if __name__ == "__main__":
    main()
