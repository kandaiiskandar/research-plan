#!/usr/bin/env python3
"""Deterministic implementation-sensitivity verification for the two documented
simplifications in the canonical solar formulation.

EVIDENCE CLASS
--------------
    deterministic implementation-sensitivity verification

This is NOT USNO validation and NOT empirical astronomical validation. It compares
the project's canonical simplified equations against NOAA's published unsimplified
equations. Both sides are models. No observation, no external reference, and no
network access are involved, so the result is a bound on the effect of two coding
choices — not a measure of astronomical accuracy.

WHAT IS COMPARED
----------------
Canonical simplified form (scripts/sensitivity/solar.py, frozen, hash-pinned):

    gamma = 2*pi/365 * (doy - 1)                      # no intra-day term, fixed 365

NOAA published form (NOAA GML, "General Solar Position Calculations",
https://gml.noaa.gov/grad/solcalc/solareqns.PDF):

    gamma = 2*pi/D * (doy - 1 + (hour - 12)/24)       # D = 365, or 366 in leap years
    eqtime = 229.18*(0.000075 + 0.001868 cos g - 0.032077 sin g
                     - 0.014615 cos 2g - 0.040849 sin 2g)
    decl   = 0.006918 - 0.399912 cos g + 0.070257 sin g - 0.006758 cos 2g
             + 0.000907 sin 2g - 0.002697 cos 3g + 0.00148 sin 3g
    ha       = +/- arccos{ cos(90.833) / (cos lat cos decl) - tan lat tan decl }
    sunrise  = 720 - 4*(longitude + ha) - eqtime          [UTC minutes]
    sunset   = 720 - 4*(longitude - ha) - eqtime          [UTC minutes]
    local    = UTC/60 + tz

The equation-of-time series, declination series, hour angle, zenith and the
sunrise/sunset expressions are identical on both sides. ONLY the gamma argument
differs. Each experiment therefore isolates exactly one gamma difference.

TWO EXPERIMENTS
---------------
A. INTRA-DAY OMISSION. Both sides use denominator 365. NOAA side additionally
   includes (hour - 12)/24. Evaluated over doy 1..365.

B. LEAP DENOMINATOR. Both sides omit the intra-day term, so the ONLY difference
   is the denominator: canonical 365 vs NOAA 366. Evaluated over doy 1..366,
   i.e. a full leap year.

EVENT-TIME EVALUATION METHOD
----------------------------
NOAA's gamma depends on `hour`, and `hour` is the event time being solved for.
This is a fixed-point problem. The procedure used is a SINGLE-PASS substitution:
the canonical (simplified) event time is computed first and substituted as `hour`
into the NOAA gamma. No iteration to convergence is performed. This is stated
because it is a methodological choice that affects the third decimal place; the
alternative (iterating to convergence) is reported alongside as a robustness
check so the choice is visible rather than hidden.

MAX / MEAN DEFINITIONS
----------------------
For each day d and event e in {sunrise, sunset}:
    diff(d,e) = | canonical_local_hours(d,e) - noaa_local_hours(d,e) | * 60   [minutes]
    max(e)    = max over all days in range
    mean(e)   = arithmetic mean over all days in range
Values are reported to three decimal places and rounded half-up at that precision.

CONFIGURATION (frozen, from solar-spec-v1)
------------------------------------------
    latitude   5.98 N
    longitude  116.01 E        (east-positive)
    timezone   UTC+8, no daylight saving
    zenith     90.833 deg      (sunrise/sunset)

Deterministic: no randomness, no network, no I/O beyond writing the JSON result.
"""

import hashlib
import json
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "scripts" / "sensitivity"))

from solar import _events, ZENITH_SUNRISE  # frozen canonical implementation

LAT, LON, TZ = 5.98, 116.01, 8
ZENITH = ZENITH_SUNRISE  # 90.833


def noaa_events(doy, days, hour_for_gamma, lat=LAT, lon=LON, tz=TZ, zenith=ZENITH):
    """NOAA published form with an explicit gamma argument."""
    g = 2 * math.pi / days * (doy - 1 + (hour_for_gamma - 12) / 24.0)
    eq = 229.18 * (0.000075 + 0.001868 * math.cos(g) - 0.032077 * math.sin(g)
                   - 0.014615 * math.cos(2 * g) - 0.040849 * math.sin(2 * g))
    dec = (0.006918 - 0.399912 * math.cos(g) + 0.070257 * math.sin(g)
           - 0.006758 * math.cos(2 * g) + 0.000907 * math.sin(2 * g)
           - 0.002697 * math.cos(3 * g) + 0.00148 * math.sin(3 * g))
    la = math.radians(lat)
    c = math.cos(math.radians(zenith)) / (math.cos(la) * math.cos(dec)) \
        - math.tan(la) * math.tan(dec)
    c = max(-1.0, min(1.0, c))
    ha = math.degrees(math.acos(c))
    sunrise = (720 - 4 * (lon + ha) - eq) / 60.0 + tz
    sunset = (720 - 4 * (lon - ha) - eq) / 60.0 + tz
    return sunrise, sunset


def canonical(doy):
    """Frozen canonical implementation (gamma = 2pi/365*(doy-1))."""
    sr, ss = _events(float(doy), LAT, LON, TZ, ZENITH)
    return float(sr), float(ss)


def experiment(label, doy_range, noaa_days, include_intraday, iterate=False):
    dsr, dss = [], []
    for doy in doy_range:
        c_sr, c_ss = canonical(doy)
        if include_intraday:
            h_sr, h_ss = c_sr, c_ss
            if iterate:                       # robustness check only
                for _ in range(50):
                    n_sr, n_ss = noaa_events(doy, noaa_days, h_sr)
                    _, n_ss2 = noaa_events(doy, noaa_days, h_ss)
                    if abs(n_sr - h_sr) < 1e-12 and abs(n_ss2 - h_ss) < 1e-12:
                        break
                    h_sr, h_ss = n_sr, n_ss2
            n_sr, _ = noaa_events(doy, noaa_days, h_sr)
            _, n_ss = noaa_events(doy, noaa_days, h_ss)
        else:
            n_sr, n_ss = noaa_events(doy, noaa_days, 12.0)   # (hour-12)/24 == 0
        dsr.append(abs(c_sr - n_sr) * 60.0)
        dss.append(abs(c_ss - n_ss) * 60.0)
    return {
        "experiment": label,
        "days_evaluated": len(dsr),
        "noaa_denominator": noaa_days,
        "noaa_intraday_term_included": include_intraday,
        "iterated_to_convergence": iterate,
        "sunrise_max_min": round(max(dsr), 3),
        "sunrise_mean_min": round(sum(dsr) / len(dsr), 3),
        "sunset_max_min": round(max(dss), 3),
        "sunset_mean_min": round(sum(dss) / len(dss), 3),
    }


def main():
    impl = ROOT / "scripts" / "sensitivity" / "solar.py"
    A = experiment("A_intraday_omission", range(1, 366), 365, True, iterate=False)
    A_it = experiment("A_intraday_omission_iterated_robustness", range(1, 366), 365,
                      True, iterate=True)
    B = experiment("B_leap_denominator", range(1, 367), 366, False, iterate=False)

    expected = {"A_sunrise": 0.116, "A_sunset": 0.141,
                "B_sunrise": 0.457, "B_sunset": 0.483}
    got = {"A_sunrise": A["sunrise_max_min"], "A_sunset": A["sunset_max_min"],
           "B_sunrise": B["sunrise_max_min"], "B_sunset": B["sunset_max_min"]}
    reproduces = all(abs(got[k] - expected[k]) < 0.0005 for k in expected)

    out = {
        "evidence_class": "deterministic implementation-sensitivity verification",
        "not": ["USNO validation", "empirical astronomical validation"],
        "configuration": {
            "latitude_deg_north": LAT, "longitude_deg_east": LON,
            "timezone": f"UTC+{TZ}", "daylight_saving": "none",
            "zenith_deg": ZENITH, "spec_version": "solar-spec-v1",
            "impl_version": "solar-v1",
            "impl_sha256": hashlib.sha256(impl.read_bytes()).hexdigest(),
        },
        "date_ranges": {
            "A_intraday_omission": "day-of-year 1..365 (one common year)",
            "B_leap_denominator": "day-of-year 1..366 (one full leap year)",
        },
        "noaa_source": {
            "publisher": "NOAA Global Monitoring Laboratory",
            "title": "General Solar Position Calculations",
            "url": "https://gml.noaa.gov/grad/solcalc/solareqns.PDF",
        },
        "canonical_simplified_gamma": "2*pi/365*(doy-1)",
        "noaa_gamma": "2*pi/D*(doy-1+(hour-12)/24), D=365 or 366 in leap years",
        "shared_between_both_sides": [
            "equation of time series", "declination series",
            "hour angle", "zenith 90.833", "sunrise/sunset expressions",
            "timezone conversion",
        ],
        "event_time_evaluation_method":
            "single-pass substitution of the canonical event time into NOAA gamma; "
            "no iteration to convergence (iterated variant reported as robustness check)",
        "max_definition": "max over evaluated days of |canonical - noaa| in minutes",
        "mean_definition": "arithmetic mean over evaluated days of the same quantity",
        "rounding": "3 decimal places",
        "results": [A, B],
        "robustness_check": [A_it],
        "expected_published_values": expected,
        "observed_values": got,
        "reproduces_published_values": reproduces,
    }
    (HERE / "noaa-simplification-check.json").write_text(json.dumps(out, indent=2) + "\n")

    print("evidence class :", out["evidence_class"])
    print(f"config         : {LAT} N, {LON} E, UTC+{TZ}, zenith {ZENITH}")
    for r in (A, B):
        print(f"\n{r['experiment']}  (days={r['days_evaluated']}, "
              f"NOAA denominator={r['noaa_denominator']})")
        print(f"  sunrise  max {r['sunrise_max_min']:.3f} min   mean {r['sunrise_mean_min']:.3f}")
        print(f"  sunset   max {r['sunset_max_min']:.3f} min   mean {r['sunset_mean_min']:.3f}")
    print(f"\nrobustness (A iterated): sunrise max {A_it['sunrise_max_min']:.3f}  "
          f"sunset max {A_it['sunset_max_min']:.3f}")
    print(f"\nexpected  {expected}")
    print(f"observed  {got}")
    print(f"REPRODUCES PUBLISHED VALUES: {reproduces}")
    return 0 if reproduces else 1


if __name__ == "__main__":
    sys.exit(main())
