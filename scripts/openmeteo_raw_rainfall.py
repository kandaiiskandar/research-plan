#!/usr/bin/env python3
"""
Open-Meteo Raw Rainfall Downloader
=====================================
Downloads raw historical precipitation data for Kota Kinabalu
from Open-Meteo Historical Weather API (ERA5, 1940–present).

Usage:
    python3 scripts/openmeteo_raw_rainfall.py --start 2020-01-01 --end 2024-12-31
"""

import argparse
import urllib.request
import urllib.parse
from pathlib import Path

LATITUDE   = 5.98
LONGITUDE  = 116.01
TIMEZONE   = "Asia/Kuching"
OUTPUT_DIR = Path(__file__).parent.parent / "data"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", default="2020-01-01")
    parser.add_argument("--end",   default="2024-12-31")
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    params = urllib.parse.urlencode({
        "latitude":   LATITUDE,
        "longitude":  LONGITUDE,
        "hourly":     "precipitation,rain",
        "start_date": args.start,
        "end_date":   args.end,
        "timezone":   TIMEZONE,
        "format":     "csv",
    })
    url = f"https://archive-api.open-meteo.com/v1/archive?{params}"

    output_path = OUTPUT_DIR / "raw_rainfall.csv"
    print(f"Downloading: {url}")
    urllib.request.urlretrieve(url, output_path)
    size_kb = output_path.stat().st_size / 1024
    print(f"Saved: {output_path} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
