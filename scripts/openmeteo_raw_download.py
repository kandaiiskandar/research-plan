#!/usr/bin/env python3
"""
Open-Meteo Raw Data Downloader
================================
Downloads raw historical data from Open-Meteo APIs and saves as CSV.
No processing, no classification, no labels — just the raw API data.

Usage:
    python3 scripts/openmeteo_raw_download.py --start 2020-01-01 --end 2024-12-31
"""

import argparse
import urllib.request
import urllib.parse
from pathlib import Path

LATITUDE  = 5.98
LONGITUDE = 116.01
TIMEZONE  = "Asia/Kuching"
OUTPUT_DIR = Path(__file__).parent.parent / "data"


def download(url: str, output_path: Path):
    print(f"Downloading: {url}")
    urllib.request.urlretrieve(url, output_path)
    size_kb = output_path.stat().st_size / 1024
    print(f"Saved: {output_path} ({size_kb:.1f} KB)")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", default="2020-01-01")
    parser.add_argument("--end",   default="2024-12-31")
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # --- Marine API: wave height, wave period ---
    #
    # MODEL CHOICE (documented 2026-09-06): era5_ocean is 0.5 deg (~50 km) —
    # the COARSEST of the nine wave models Open-Meteo offers. It is used because
    # it is the only one covering 1940-present; every finer model starts later:
    #   MeteoFrance MFWAM  ~8 km   from Oct 2021
    #   NCEP GFS Wave 0.16 ~16 km  from Oct 2024 (covers Borneo)
    #   ECMWF WAM           9 km   from Nov 2025
    # For a 2020-2024 retrospective this is forced. But wave height carries
    # 97.5% of daylight CAUTION decisions, so a ~50 km open-water average is
    # driving the classifier. See finding F-12 and open question Q6.
    #
    # cell_selection is NOT set here, but the Marine API defaults to "sea" —
    # so the wave data correctly came from a sea cell (6.0, 116.0). The
    # land/sea mismatch in F-10 affects only the weather request below.
    #
    # The wind_wave_* and swell_wave_* columns return all-NaN: era5_ocean does
    # not provide partitioned components. Not a download error. wave_period IS
    # populated and currently unused (Q5).
    marine_params = urllib.parse.urlencode({
        "latitude":   LATITUDE,
        "longitude":  LONGITUDE,
        "hourly":     "wave_height,wave_period,wind_wave_height,wind_wave_period,swell_wave_height,swell_wave_period",
        "models":     "era5_ocean",
        "start_date": args.start,
        "end_date":   args.end,
        "timezone":   TIMEZONE,
        "format":     "csv",
    })
    marine_url = f"https://marine-api.open-meteo.com/v1/marine?{marine_params}"
    download(marine_url, OUTPUT_DIR / "raw_marine.csv")

    # --- Historical Weather API: wind speed, wind direction, precipitation ---
    #
    # WARNING (2026-09-06): cell_selection is NOT set below, so it defaults to
    # "land". The 2020-2024 archive in data/ was collected this way and returned
    # a LAND grid cell (5.940246, 116.100006) while raw_marine.csv came from a
    # SEA cell (6.0, 116.0) ~12 km away. Wind over land is materially lower than
    # over open water, and sustained wind in that archive never exceeds 17.8 kn
    # against a 22 kn CAUTION threshold.
    #
    # Before re-downloading, resolve open question Q1a in
    # docs/canonical/decision-record-empirical-first.md: re-run with
    # "cell_selection": "sea" and compare. If sea-cell wind is materially
    # higher, finding F-1 (g_w never fires) is a collection artefact.
    #
    # Note also: weather_code returns ZERO thunderstorm codes (95/96/99) over
    # five years here. Open-Meteo documents that thunderstorm estimation is not
    # possible outside Central Europe, so g_r's storm branch is reachable only
    # via precipitation > 20 mm/hr. See finding F-11.
    weather_params = urllib.parse.urlencode({
        "latitude":        LATITUDE,
        "longitude":       LONGITUDE,
        "hourly":          "wind_speed_10m,wind_direction_10m,wind_gusts_10m,precipitation,weather_code",
        "wind_speed_unit": "kn",
        "start_date":      args.start,
        "end_date":        args.end,
        "timezone":        TIMEZONE,
        "format":          "csv",
        # "cell_selection": "sea",   # <-- Q1a: uncomment and compare
    })
    weather_url = f"https://archive-api.open-meteo.com/v1/archive?{weather_params}"
    download(weather_url, OUTPUT_DIR / "raw_weather.csv")

    print("\nDone. Files saved to data/")
    print("  raw_marine.csv  — wave height, wave period, swell")
    print("  raw_weather.csv — wind speed (knots), wind gusts, precipitation")


if __name__ == "__main__":
    main()
