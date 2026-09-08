#!/usr/bin/env python3
"""Build the frozen solar reproducibility artefacts for SDR-001 conditions C-1/C-2/C-3.

SCOPE — READ THIS FIRST
-----------------------
This script does NOT change the canonical classifier. `g_t` remains the
incumbent fixed clock (SAFE 06:00-17:00 / CAUTION 17:00-19:00 / UNSAFE else).
SDR-001 is APPROVED but NOT YET APPLIED. This script only creates the frozen
inputs that a later, separate migration task would consume.

It writes three artefacts and nothing else:

  data/solar/usno-validation-2026-09-08.csv   28 rows  (C-2)
  data/solar/solar-events-daily.csv           1827 rows (C-3)
  data/solar/solar-boundary-audit.csv         summary   (C-3 verification)

It writes NO safety states, NO governance values, and NO prediction outcomes.
The solar table contains astronomical values only, per the C-3 requirement that
the input boundary stay separate from the governance interpretation.

PINNED SPECIFICATION — solar-spec-v1
------------------------------------
Implementation : NOAA-style low-precision solar-position formulation,
                 scripts/sensitivity/solar.py, UNMODIFIED and re-used here.
                 sha256 3b7dc371ebe5931b3336f9982c5806a06a515dc2032569f5da7720470c1ec36c
                 Do NOT call it Meeus / NOAA-Meeus / NOAA-Spencer — no project
                 evidence supports those names (see the C-0 cleanup report).
Location       : 5.98 N, 116.01 E  -- the REQUESTED site coordinate, declared in
                 openmeteo_raw_download.py, collect_raw_v2.py and
                 openmeteo_raw_rainfall.py, and recorded in data-provenance.md.
                 116.07 (the old solar.py default) matches NOTHING in the
                 project and is superseded. See the C-1/C-2/C-3 report.
Timezone       : UTC+8 fixed. Malaysia observes no daylight saving; the dataset
                 headers carry utc_offset_seconds=28800 throughout.
Zenith         : sunrise/sunset 90.833 deg (34' refraction + 16' semi-diameter)
                 civil dawn/dusk  96.0  deg (sun 6 deg below horizon)
Day-of-year    : calendar tm_yday, 1..365 (366 in leap years). The series
                 denominator is a fixed 365. See the report for the measured
                 leap-day consequence — it is bounded and documented, not
                 silently absorbed.
Boundary rule  : half-open, sunrise <= t < sunset. Exact sunrise = SAFE,
                 exact sunset = UNSAFE. (Recorded for the later migration;
                 this script does not classify.)
Precision      : compute float64; STORE 6 dp of an hour (~3.6 ms) plus an
                 HH:MM:SS rendering; COMPARE on the stored float, never on a
                 display string.
Invalid input  : any invalid date/lat/lon or non-finite result yields the
                 sentinel INVALID rather than a plausible timestamp. Under
                 Model B a missing/invalid clock is t = bottom, and
                 g_t(bottom) = UNSAFE by Corollary C.1b.1 — never SAFE.
"""

import csv
import hashlib
import math
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "sensitivity"))
from solar import _events, ZENITH_SUNRISE, ZENITH_CIVIL  # noqa: E402  UNMODIFIED

ROOT = Path(__file__).resolve().parent.parent.parent
OUT = ROOT / "data" / "solar"
OUT.mkdir(parents=True, exist_ok=True)

SPEC_VERSION = "solar-spec-v1"
IMPL_PATH = ROOT / "scripts" / "sensitivity" / "solar.py"
IMPL_SHA = hashlib.sha256(IMPL_PATH.read_bytes()).hexdigest()
IMPL_VERSION = "solar-v1"

LAT = 5.98
LON = 116.01          # authoritative, resolved under C-1
LON_AS_VALIDATED = 116.07   # superseded solar.py default, retained for comparison
TZ = 8

REPLAY_START = date(2020, 1, 1)   # PRIMARY  first date
REPLAY_END = date(2024, 12, 31)   # PRIMARY  last date
RESOLUTION_START = date(2021, 10, 1)

INVALID = "INVALID"

# --- USNO reference values ---------------------------------------------------
# CAPTURED 2026-09-08 from USNO Astronomical Applications API v4.0.1,
# endpoint /api/rstt/oneday, coords=5.98,116.01 tz=8.
#
# *** RECONSTRUCTED DATASET — NOT THE ORIGINAL CAPTURED RESPONSE. ***
# The original validation stored only summary statistics; no per-event values
# were retained anywhere in the project. These were re-queried. USNO reports to
# whole minutes, so every reference value below has 1-minute granularity.
USNO = {
    "2024-02-02": {"civil_dawn": "06:12", "sunrise": "06:33", "sunset": "18:26", "civil_dusk": "18:47"},
    "2024-03-20": {"civil_dawn": "05:59", "sunrise": "06:20", "sunset": "18:27", "civil_dusk": "18:47"},
    "2024-05-24": {"civil_dawn": "05:38", "sunrise": "06:00", "sunset": "18:26", "civil_dusk": "18:48"},
    "2024-06-21": {"civil_dawn": "05:41", "sunrise": "06:04", "sunset": "18:32", "civil_dusk": "18:55"},
    "2024-07-17": {"civil_dawn": "05:47", "sunrise": "06:09", "sunset": "18:35", "civil_dusk": "18:57"},
    "2024-11-11": {"civil_dawn": "05:42", "sunrise": "06:04", "sunset": "17:56", "civil_dusk": "18:18"},
    "2024-12-21": {"civil_dawn": "05:58", "sunrise": "06:21", "sunset": "18:07", "civil_dusk": "18:30"},
}
USNO_SOURCE = "USNO AA API v4.0.1 /api/rstt/oneday"
USNO_CAPTURED = "2026-09-08"

SELECTION = {
    "2024-02-02": "annual latest sunrise",
    "2024-03-20": "March equinox",
    "2024-05-24": "annual earliest sunrise",
    "2024-06-21": "June solstice",
    "2024-07-17": "annual latest sunset",
    "2024-11-11": "annual earliest sunset",
    "2024-12-21": "December solstice",
}


EVENTS = ("sunrise", "sunset", "civil_dawn", "civil_dusk")


def compute(d, lon, lat=LAT, tz=TZ):
    """Local implementation values for one date. Returns hours, or INVALID.

    The input guard lives HERE, not in solar.py. `solar.py` is deliberately
    unmodified (it is the hash-pinned validated artefact), and it has no input
    validation of its own: `np.clip(c, -1, 1)` will happily return a
    plausible-looking time for an out-of-range latitude. C-1 requires that
    invalid input never yield a plausible timestamp, so the guard is specified
    and exercised here and MUST be carried into the canonical solar module at
    migration (C-8), not left in this builder.
    """
    try:
        if not isinstance(d, date):
            return {k: INVALID for k in EVENTS}
        if not (-90.0 <= lat <= 90.0):
            return {k: INVALID for k in EVENTS}
        if not (-180.0 <= lon <= 180.0):
            return {k: INVALID for k in EVENTS}
        if not (-12.0 <= tz <= 14.0):
            return {k: INVALID for k in EVENTS}

        doy = float(d.timetuple().tm_yday)

        # No-event guard: |cos(zenith)/(cos φ cos δ) − tan φ tan δ| > 1 means the
        # sun neither rises nor sets that day. solar.py clips this to ±1 and
        # returns a value anyway; at 5.98 N it never triggers, but the canonical
        # module must signal it rather than fabricate an event.
        g = 2 * math.pi / 365.0 * (doy - 1)
        dec = (0.006918 - 0.399912 * math.cos(g) + 0.070257 * math.sin(g)
               - 0.006758 * math.cos(2 * g) + 0.000907 * math.sin(2 * g)
               - 0.002697 * math.cos(3 * g) + 0.00148 * math.sin(3 * g))
        la = math.radians(lat)
        for z in (ZENITH_SUNRISE, ZENITH_CIVIL):
            c = (math.cos(math.radians(z)) / (math.cos(la) * math.cos(dec))
                 - math.tan(la) * math.tan(dec))
            if abs(c) > 1.0:
                return {k: INVALID for k in EVENTS}

        sr, ss = _events(doy, lat, lon, tz, ZENITH_SUNRISE)
        cd, ck = _events(doy, lat, lon, tz, ZENITH_CIVIL)
        vals = {"sunrise": float(sr), "sunset": float(ss),
                "civil_dawn": float(cd), "civil_dusk": float(ck)}
        for v in vals.values():
            if not math.isfinite(v) or not (0.0 <= v < 24.0):
                return {k: INVALID for k in EVENTS}
        return vals
    except Exception:
        return {k: INVALID for k in EVENTS}


def hhmmss(h):
    if h == INVALID:
        return INVALID
    total = round(h * 3600)
    return f"{total // 3600:02d}:{(total % 3600) // 60:02d}:{total % 60:02d}"


def to_hours(hhmm):
    hh, mm = hhmm.split(":")
    return int(hh) + int(mm) / 60.0


def build_validation():
    rows = []
    for ds in sorted(USNO):
        d = date.fromisoformat(ds)
        local_auth = compute(d, LON)
        local_asval = compute(d, LON_AS_VALIDATED)
        for ev in ("sunrise", "sunset", "civil_dawn", "civil_dusk"):
            ref = to_hours(USNO[ds][ev])
            a, v = local_auth[ev], local_asval[ev]
            rows.append({
                "date": ds,
                "selection_reason": SELECTION[ds],
                "latitude": LAT,
                "longitude": LON,
                "timezone": f"UTC+{TZ}",
                "event": ev,
                "local_hours": f"{a:.6f}",
                "local_time": hhmmss(a),
                "usno_time": USNO[ds][ev],
                "usno_hours": f"{ref:.6f}",
                "diff_signed_min": f"{(a - ref) * 60:+.2f}",
                "diff_abs_min": f"{abs(a - ref) * 60:.2f}",
                "local_time_at_116_07": hhmmss(v),
                "diff_abs_min_at_116_07": f"{abs(v - ref) * 60:.2f}",
                "impl_version": IMPL_VERSION,
                "impl_sha256": IMPL_SHA,
                "spec_version": SPEC_VERSION,
                "validation_source": USNO_SOURCE,
                "validation_captured": USNO_CAPTURED,
                "artefact_status": "RECONSTRUCTED-2026-09-08",
            })
    p = OUT / "usno-validation-2026-09-08.csv"
    with p.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    return rows, p


def stats(rows, key):
    vals = [float(r[key]) for r in rows]
    sr_ss = [float(r[key]) for r in rows if r["event"] in ("sunrise", "sunset")]
    return {
        "n": len(vals),
        "max": max(vals),
        "mean": sum(vals) / len(vals),
        "srss_n": len(sr_ss),
        "srss_max": max(sr_ss),
        "srss_mean": sum(sr_ss) / len(sr_ss),
    }


def build_daily():
    rows = []
    d = REPLAY_START
    while d <= REPLAY_END:
        v = compute(d, LON)
        rows.append({
            "date": d.isoformat(),
            "latitude": LAT,
            "longitude": LON,
            "timezone": f"UTC+{TZ}",
            "utc_offset_seconds": TZ * 3600,
            "sunrise_hours": f"{v['sunrise']:.6f}",
            "sunrise_local": hhmmss(v["sunrise"]),
            "sunset_hours": f"{v['sunset']:.6f}",
            "sunset_local": hhmmss(v["sunset"]),
            "zenith_deg": ZENITH_SUNRISE,
            "in_primary": "Y",
            "in_resolution": "Y" if d >= RESOLUTION_START else "N",
            "impl_version": IMPL_VERSION,
            "impl_sha256": IMPL_SHA,
            "spec_version": SPEC_VERSION,
        })
        d += timedelta(days=1)
    p = OUT / "solar-events-daily.csv"
    with p.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    return rows, p


def boundary_audit(daily):
    def near(h):
        return abs(h - round(h)) * 60.0

    out = []
    for label, lo in (("sunrise", "sunrise_hours"), ("sunset", "sunset_hours")):
        gaps = [near(float(r[lo])) for r in daily]
        out.append({
            "event": label,
            "n_days": len(gaps),
            "within_1_min": sum(1 for g in gaps if g < 1.0),
            "within_2_min": sum(1 for g in gaps if g < 2.0),
            "closest_min": f"{min(gaps):.4f}",
        })
    p = OUT / "solar-boundary-audit.csv"
    with p.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0]))
        w.writeheader()
        w.writerows(out)
    return out, p


def main():
    print(__doc__)
    print("=" * 78)
    print(f"impl {IMPL_VERSION}  sha256 {IMPL_SHA}")
    print(f"spec {SPEC_VERSION}  lat {LAT}  lon {LON}  tz UTC+{TZ}")
    print("=" * 78)

    vrows, vpath = build_validation()
    s_auth = stats(vrows, "diff_abs_min")
    s_asval = stats(vrows, "diff_abs_min_at_116_07")

    print(f"\nC-2  {vpath.relative_to(ROOT)}  ({len(vrows)} rows)")
    print(f"  at 116.01 (authoritative) : max {s_auth['max']:.2f} min   "
          f"mean {s_auth['mean']:.4f} min   "
          f"sunrise/sunset mean {s_auth['srss_mean']:.4f}")
    print(f"  at 116.07 (as validated)  : max {s_asval['max']:.2f} min   "
          f"mean {s_asval['mean']:.4f} min   "
          f"sunrise/sunset mean {s_asval['srss_mean']:.4f}")
    print("  recorded in the finding   : max 0.90 min   mean 0.3700   "
          "sunrise/sunset mean 0.3500")

    drows, dpath = build_daily()
    print(f"\nC-3  {dpath.relative_to(ROOT)}  ({len(drows)} rows)")
    print(f"  {drows[0]['date']} .. {drows[-1]['date']}  "
          f"PRIMARY {sum(1 for r in drows if r['in_primary']=='Y')}  "
          f"RESOLUTION {sum(1 for r in drows if r['in_resolution']=='Y')}")

    brows, bpath = boundary_audit(drows)
    print(f"\n     {bpath.relative_to(ROOT)}")
    for r in brows:
        print(f"  {r['event']:8s} within 1 min {r['within_1_min']:4d}   "
              f"within 2 min {r['within_2_min']:4d}   "
              f"closest {r['closest_min']} min")
    print("  previously recorded: sunrise 160 / sunset 60 within 1 min, "
          "closest 0.02 min  (computed at 116.07)")

    # --- Leap-year semantics: measured, not assumed -------------------------
    # doy is the calendar day-of-year; the series denominator is a fixed 365.
    # In a leap year every date from 01 Mar carries a doy one higher than the
    # same calendar date in a common year, so the series is evaluated one day
    # further along. This is a real, bounded, one-directional effect.
    print("\nLeap-year semantics (fixed-365 denominator, calendar tm_yday):")
    print("  Feb 29 exists and is computed (doy=60); it is NOT skipped.")
    worst, worst_d = 0.0, None
    for md in [(3, 1), (3, 20), (6, 21), (9, 22), (12, 21)]:
        a = compute(date(2023, *md), LON)["sunrise"]   # common year
        b = compute(date(2024, *md), LON)["sunrise"]   # leap year
        delta = abs(a - b) * 60
        if delta > worst:
            worst, worst_d = delta, f"{md[0]:02d}-{md[1]:02d}"
        print(f"  {md[0]:02d}-{md[1]:02d}: common-year {hhmmss(a)}  "
              f"leap-year {hhmmss(b)}  delta {delta:.2f} min")
    print(f"  worst sampled post-Feb-29 leap offset: {worst:.2f} min at {worst_d}")

    # --- Invalid input: must return INVALID, never a plausible timestamp ----
    print("\nInvalid-input check (C-1) — expect INVALID for every case:")
    cases = [
        ("valid control (2024-03-20)", dict(d=date(2024, 3, 20), lon=LON)),
        ("latitude 95 (out of range)", dict(d=date(2024, 3, 20), lon=LON, lat=95.0)),
        ("latitude 89.9 (polar, no event)", dict(d=date(2024, 6, 21), lon=LON, lat=89.9)),
        ("longitude 400 (out of range)", dict(d=date(2024, 3, 20), lon=400.0)),
        ("timezone 99 (out of range)", dict(d=date(2024, 3, 20), lon=LON, tz=99)),
        ("date is not a date", dict(d="2024-03-20", lon=LON)),
        ("date is None (clock unavailable)", dict(d=None, lon=LON)),
    ]
    for label, kw in cases:
        r = compute(**kw)["sunrise"]
        print(f"  {label:38s} -> {hhmmss(r) if r != INVALID else INVALID}")
    print("  Under Model B an INVALID/absent clock is t = ⊥, and g_t(⊥) = UNSAFE")
    print("  (Corollary C.1b.1) — never SAFE, and never a fabricated timestamp.")

    print("\nNOTE: canonical g_t is UNCHANGED. Nothing here is applied.")


if __name__ == "__main__":
    main()
