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
    weather_params = urllib.parse.urlencode({
        "latitude":        LATITUDE,
        "longitude":       LONGITUDE,
        "hourly":          "wind_speed_10m,wind_direction_10m,wind_gusts_10m,precipitation,weather_code",
        "wind_speed_unit": "kn",
        "start_date":      args.start,
        "end_date":        args.end,
        "timezone":        TIMEZONE,
        "format":          "csv",
    })
    weather_url = f"https://archive-api.open-meteo.com/v1/archive?{weather_params}"
    download(weather_url, OUTPUT_DIR / "raw_weather.csv")

    print("\nDone. Files saved to data/")
    print("  raw_marine.csv  — wave height, wave period, swell")
    print("  raw_weather.csv — wind speed (knots), wind gusts, precipitation")


if __name__ == "__main__":
    main()
