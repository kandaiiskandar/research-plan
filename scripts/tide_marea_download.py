#!/usr/bin/env python3
"""
Marea API Tide Downloader — Kota Kinabalu
==========================================
Downloads hourly tide predictions for 5.98°N, 116.01°E
using the Marea API (https://api.marea.ooo).

Fetches in 6-month chunks (API limit: ~half year per request).
5 years = ~10 requests, well within 100 free credits.

Usage:
    python3 scripts/tide_marea_download.py
"""

import csv
import json
import time
import urllib.request
import urllib.parse
from datetime import datetime, timezone, timedelta
from pathlib import Path

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

API_KEY   = "aa8baa81-a0f0-49db-8f9c-0a29daa67cc9"
LATITUDE  = 5.98
LONGITUDE = 116.01
START     = "2020-01-01"
END       = "2024-12-31"
INTERVAL  = 60        # minutes — hourly
DATUM     = "MSL"     # Mean Sea Level

OUTPUT_DIR = Path(__file__).parent.parent / "data"
OUTPUT_CSV = OUTPUT_DIR / "raw_tide_marea.csv"

API_URL = "https://api.marea.ooo/v2/tides"
MAX_DURATION_MINUTES = 260_000   # ~6 months, safely under 263,520 limit


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def date_chunks(start_str: str, end_str: str, chunk_minutes: int):
    """Yield (start_unix, duration_minutes) pairs."""
    start = datetime.fromisoformat(start_str).replace(tzinfo=timezone.utc)
    end   = datetime.fromisoformat(end_str).replace(tzinfo=timezone.utc) + timedelta(days=1)
    current = start
    while current < end:
        chunk_end = min(current + timedelta(minutes=chunk_minutes), end)
        duration  = int((chunk_end - current).total_seconds() / 60)
        yield int(current.timestamp()), duration
        current = chunk_end


def fetch_chunk(start_unix: int, duration_minutes: int) -> list:
    """Fetch one chunk from Marea API. Returns list of {time, height} dicts."""
    params = urllib.parse.urlencode({
        "latitude":  LATITUDE,
        "longitude": LONGITUDE,
        "timestamp": start_unix,       # Unix epoch seconds — correct param name per OpenAPI spec
        "duration":  duration_minutes,
        "interval":  INTERVAL,
        "datum":     DATUM,
    })
    url = f"{API_URL}?{params}"
    req = urllib.request.Request(
        url,
        headers={"x-marea-api-token": API_KEY}
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())
    return data.get("heights", [])


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    chunks = list(date_chunks(START, END, MAX_DURATION_MINUTES))
    print(f"Fetching {len(chunks)} chunks for {START} → {END}")

    all_rows = []
    for i, (start_unix, duration) in enumerate(chunks, 1):
        dt = datetime.fromtimestamp(start_unix, tz=timezone.utc)
        print(f"  Chunk {i}/{len(chunks)}: {dt.date()} ({duration // 1440} days) ...", end=" ", flush=True)

        try:
            heights = fetch_chunk(start_unix, duration)
            for h in heights:
                ts  = datetime.fromtimestamp(h["timestamp"], tz=timezone.utc)
                # Convert to MYT (UTC+8)
                ts_myt = ts + timedelta(hours=8)
                all_rows.append({
                    "timestamp_myt": ts_myt.strftime("%Y-%m-%dT%H:%M"),
                    "date":          ts_myt.date().isoformat(),
                    "hour":          ts_myt.hour,
                    "tide_height_m": round(h["height"], 3),
                })
            print(f"{len(heights)} rows")
        except Exception as e:
            print(f"FAILED: {e}")

        if i < len(chunks):
            time.sleep(1)

    # Write CSV
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp_myt", "date", "hour", "tide_height_m"])
        writer.writeheader()
        writer.writerows(all_rows)

    size_kb = OUTPUT_CSV.stat().st_size / 1024
    print(f"\nDone. {len(all_rows)} rows saved → {OUTPUT_CSV} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
