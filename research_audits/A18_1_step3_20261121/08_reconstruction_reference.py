#!/usr/bin/env python3
"""
A18.1 Step 3 — ISOLATED REFERENCE RECONSTRUCTION of the AAI2026 governance
contract. READ-ONLY. Standard library only.

Every value and every comparison operator below is transcribed from the local
source with a line citation. Nothing is inferred unless the docstring says
INFERRED_FILL_IN. No original file is imported, so no import side effect can
occur: the original scripts import pandas/numpy and canonical_gt at module
level, and condition_comparison.py writes data/prediction-register.csv on one
guarded path (scripts/condition_comparison.py:333-334, behind
_register_write_enabled() / --write-register). This module reproduces the rules
instead of importing them, and reads the frozen solar artefact with csv.

PROVENANCE OF EACH RULE
  g_w  scripts/historical_replay.py:41,76   and condition_comparison.py:63,160
  g_r  scripts/historical_replay.py:49,92-94 and condition_comparison.py:72,161-162
  g_m  scripts/historical_replay.py:160      and condition_comparison.py:165
  g_o  scripts/historical_replay.py:58,105   and condition_comparison.py:76,163
  g_t  scripts/canonical_gt.py:105           (half-open sunrise <= t < sunset)
  f    scripts/historical_replay.py:172      and condition_comparison.py:166
  A_AI scripts/condition_comparison.py:81-105
"""
import csv
from datetime import date as _date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
SOLAR_ARTEFACT = ROOT / "data" / "solar" / "solar-events-daily.csv"

# --- states -----------------------------------------------------------------
# VERIFIED_FROM_CODE historical_replay.py:54 / condition_comparison.py:78
SAFE, CAUTION, UNSAFE = 0, 1, 2
STATE_NAME = {SAFE: "SAFE", CAUTION: "CAUTION", UNSAFE: "UNSAFE"}

# --- thresholds -------------------------------------------------------------
# VERIFIED_FROM_CODE historical_replay.py:41, condition_comparison.py:63,
# diagnostic_binding.py:43 — all three agree.
W_CAUTION, W_UNSAFE = 21.6, 27.0
# VERIFIED_FROM_CODE historical_replay.py:49, condition_comparison.py:72,
# diagnostic_binding.py:52 — all three agree.
R_CAUTION, R_UNSAFE = 10.0, 20.0
# VERIFIED_FROM_CODE historical_replay.py:92 / condition_comparison.py:161
STORM_WMO = (95, 96, 99)
# VESSEL PROFILE. Canonical analysis is SMALL ONLY: condition_comparison.py:76
# hard-codes LO, HI = 1.0, 1.25 with no vessel parameter. historical_replay.py:
# 57-61 additionally carries medium/big, which the canonical comparison never
# uses. The <10 m LOA -> <10 GRT transfer is a RESEARCHER ASSUMPTION, not a
# certified marine safety threshold (see 05_rule_assumptions_and_discrepancies).
VESSEL_THRESHOLDS = {"small": (1.0, 1.25), "medium": (1.4, 2.8), "big": (1.5, 3.5)}

# --- admissible sets --------------------------------------------------------
# VERIFIED_FROM_CODE condition_comparison.py:81-105, transcribed verbatim.
FULL = frozenset({"Go", "Delay", "DepartureTime", "Duration"})
RESTRICTED = frozenset({"Go", "Delay"})
EMPTY = frozenset()
A_AI = {
    "C0": {SAFE: FULL,    CAUTION: FULL,       UNSAFE: FULL},
    "C1": {SAFE: FULL,    CAUTION: FULL,       UNSAFE: EMPTY},
    "C3": {SAFE: FULL,    CAUTION: FULL,       UNSAFE: EMPTY},
    "C2": {SAFE: FULL,    CAUTION: RESTRICTED, UNSAFE: EMPTY},
}
ORDER = ["C0", "C1", "C3", "C2"]


# --- component classifiers --------------------------------------------------
def g_w(wind_kn):
    """Wind, sustained knots. STRICT > at BOTH boundaries.
    historical_replay.py:76 — `2 if w_kn > W_UNSAFE else (1 if w_kn > W_CAUTION else 0)`
    Exactly 21.6 kn -> SAFE. Exactly 27.0 kn -> CAUTION."""
    return UNSAFE if wind_kn > W_UNSAFE else (CAUTION if wind_kn > W_CAUTION else SAFE)


def g_r(precip_mm_hr, wmo_code):
    """Rainfall intensity with a WMO thunderstorm override to UNSAFE.
    historical_replay.py:92-94. STRICT > at both boundaries.
    Exactly 10.0 -> SAFE. Exactly 20.0 -> CAUTION unless the WMO code storms."""
    if precip_mm_hr > R_UNSAFE or wmo_code in STORM_WMO:
        return UNSAFE
    return CAUTION if precip_mm_hr > R_CAUTION else SAFE


def g_m(_warning_level=None):
    """Marine warning. HELD AT SAFE THROUGHOUT.
    historical_replay.py:160 `d["c_warn"] = 0`; condition_comparison.py:165
    `g_m = np.full(len(d), SAFE)`.
    This is a MODEL ASSUMPTION: Step 2 confirmed no warning column exists in any
    raw file. It is NOT an observed absence of warnings. Because aggregation is
    by maximum, g_m can only RAISE severity, so every state is a LOWER BOUND."""
    return SAFE


def g_o(wave_m, vessel="small"):
    """Wave height, conditioned on vessel category. ASYMMETRIC OPERATORS:
    INCLUSIVE at the CAUTION onset, STRICT at the UNSAFE onset.
    historical_replay.py:105 `0 if wave_m < lo else (1 if wave_m <= hi else 2)`
    condition_comparison.py:163 `where(wave > HI, UNSAFE, where(wave >= LO, CAUTION, SAFE))`
    The two forms are logically equivalent; verified by exhaustive fixture.
    Exactly 1.0 m -> CAUTION. Exactly 1.25 m -> CAUTION. 1.25+eps -> UNSAFE."""
    lo, hi = VESSEL_THRESHOLDS[vessel]
    return SAFE if wave_m < lo else (CAUTION if wave_m <= hi else UNSAFE)


_SOLAR = None
def _solar():
    """Load the frozen C-3 solar artefact with csv (not pandas).
    canonical_gt.py:70-73 consumes sunrise_hours / sunset_hours as floats and
    NEVER the HH:MM:SS display columns."""
    global _SOLAR
    if _SOLAR is None:
        sr, ss = {}, {}
        with open(SOLAR_ARTEFACT, newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                y, m, d = (int(x) for x in row["date"].split("-"))
                k = _date(y, m, d)
                sr[k] = float(row["sunrise_hours"])
                ss[k] = float(row["sunset_hours"])
        _SOLAR = (sr, ss)
    return _SOLAR


def g_t(the_date, hour):
    """Time of day. HALF-OPEN: sunrise <= t < sunset -> SAFE, else UNSAFE.
    canonical_gt.py:105 `out[i] = SAFE if (a <= hi < b) else UNSAFE`.
    g_t EMITS NO CAUTION — Im(g_t) = {SAFE, UNSAFE} by deliberate design
    (canonical_gt.py:15-18). Fail-safe: a missing date or non-finite hour
    resolves to UNSAFE (canonical_gt.py:97-104, Corollary C.1b.1).

    NOTE ON GRANULARITY: the original compares the INTEGER hour-of-day against
    float sunrise/sunset hours, so an hourly bucket is judged by its START.
    With sunrise 6.424 on 2020-01-01, hour 6 is UNSAFE. Transcribed as-is."""
    if hour is None or not isinstance(hour, (int, float)) or hour != hour:
        return UNSAFE
    sr, ss = _solar()
    a, b = sr.get(the_date), ss.get(the_date)
    if a is None or b is None:
        return UNSAFE
    return SAFE if (a <= hour < b) else UNSAFE


# --- aggregation ------------------------------------------------------------
def f(wind_kn, precip_mm_hr, wmo_code, wave_m, the_date, hour,
      vessel="small", warning_level=None):
    """f(E) = max_> { g_w, g_r, g_m, g_o, g_t }.
    historical_replay.py:167-172 (np.max over vstack of five terms);
    condition_comparison.py:166 (np.max over column_stack, same five, same order).
    Maximum-severity combination: ANY component at UNSAFE forces UNSAFE."""
    return max(g_w(wind_kn),
               g_r(precip_mm_hr, wmo_code),
               g_m(warning_level),
               g_o(wave_m, vessel),
               g_t(the_date, hour))


def components(wind_kn, precip_mm_hr, wmo_code, wave_m, the_date, hour, vessel="small"):
    """Per-component states, for truth tables and attribution."""
    return {"g_w": g_w(wind_kn), "g_r": g_r(precip_mm_hr, wmo_code),
            "g_m": g_m(), "g_o": g_o(wave_m, vessel), "g_t": g_t(the_date, hour)}


def admissible(state, config):
    """A_AI(S) under a configuration. condition_comparison.py:169-171."""
    return A_AI[config][state]


def in_departure_window(hour):
    """05:00 <= hour <= 09:00, FIVE slots, inclusive both ends.
    historical_replay.py:238 `(d.hour >= 5) & (d.hour <= 9)`.
    Step 2 confirmed inclusive: 1,827 days x 5 = 9,135. Half-open gives 7,308."""
    return 5 <= hour <= 9
