#!/usr/bin/env python3
"""
Four-condition governance comparison, including a Flehmig-style baseline (C3).

Answers Review 3's novelty objection empirically. The paper claims no existing
architecture restricts AI advisory scope as a function of classified safety
state. That claim currently rests on a literature coding table. This script
instantiates the CLOSEST STRUCTURAL PRECEDENT in the corpus on the same site
data and measures whether it diverges from a plain binary gate.

Conditions
----------
C0  Ungated          A_AI = full set at every hour. No governance.
C1  Binary-gated     G(S) gates participation. A_AI = full when G = 1, else empty.
C3  Flehmig-style    Three-level traffic-light. AI stays the safety function at
                     green AND orange with UNCHANGED scope; switches to non-AI
                     backup at red. Only the SUPERVISORY response varies across
                     the intermediate level.
C2  Proposed         Two-level governance pair. A_AI contracts at CAUTION.

FAIRNESS NOTE — read before quoting any number from this script.
Flehmig et al. condition their index on AI DEGRADATION (drift, outliers,
performance decay), not on environmental state. C3 ports their GOVERNANCE
TOPOLOGY onto our conditioning variable so the two can be compared on the same
axis. It is not a claim about their system on their problem, and it is not a
reproduction of their results. Their framework answers a different question and
is correct for it. What is being compared is the structure of the mapping from
a three-level classification to admissible AI output.

Metric
------
Admissible-set divergence: for each hour and each pair of conditions, do the
two conditions permit the same set of recommendation types? This is defined by
the architecture, NOT by the reasoning engine, so it runs without Layer 3.
What Layer 3 would add is the actual AI(E) content inside each set.

Resolves pre-registered predictions P21-P24 (data/prediction-register.csv).
"""

import pandas as pd
import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

# Small vessel (< 10 GRT) — the deployment population. Amended 2026-09-06:
# UNSAFE at Yaakob's operational ceiling, not his NORDFORSK failure point.
LO, HI = 1.0, 1.25

SAFE, CAUTION, UNSAFE = 0, 1, 2
STATE_NAME = {SAFE: "SAFE", CAUTION: "CAUTION", UNSAFE: "UNSAFE"}

FULL = frozenset({"Go", "Delay", "DepartureTime", "Duration"})
RESTRICTED = frozenset({"Go", "Delay"})
EMPTY = frozenset()


# --------------------------------------------------------------------------
# The four conditions, as maps from safety state to admissible set
# --------------------------------------------------------------------------

A_AI = {
    # No governance at all — full scope regardless of state.
    "C0": {SAFE: FULL, CAUTION: FULL, UNSAFE: FULL},

    # Level 1 only. Participation gated; scope never restricted while active.
    "C1": {SAFE: FULL, CAUTION: FULL, UNSAFE: EMPTY},

    # Flehmig-style traffic light. green -> AI in control, full scope.
    # orange -> AI STILL in control, STILL full scope; supervisor investigates.
    # red -> switch to non-AI backup, AI out.
    # The intermediate level changes supervisory intensity, not AI scope.
    "C3": {SAFE: FULL, CAUTION: FULL, UNSAFE: EMPTY},

    # The proposed architecture. Scope contracts at the intermediate state.
    "C2": {SAFE: FULL, CAUTION: RESTRICTED, UNSAFE: EMPTY},
}

ORDER = ["C0", "C1", "C3", "C2"]
LABEL = {
    "C0": "C0 ungated",
    "C1": "C1 binary-gated",
    "C3": "C3 Flehmig-style",
    "C2": "C2 proposed",
}


# --------------------------------------------------------------------------
# Data + classifier
# --------------------------------------------------------------------------

# Two configurations, per the reporting decision of 2026-09-06 ("option C").
# PRIMARY is the full five-year record; RESOLUTION is the finer-wave check.
# See scripts/canonical_figures.py for why both are reported.
CONFIGS = {
    "PRIMARY  (5.00 yr, sea wind + ERA5-Ocean ~50 km)": "raw_marine_era5_sea.csv",
    "RESOLUTION (3.25 yr, sea wind + MFWAM ~8 km)": "raw_marine_mfwam.csv",
}


def load(marine_file):
    """Sea-cell weather joined to the configured wave model.

    Precipitation comes from the sea-cell weather file, not raw_rainfall.csv,
    which is still sited on the land cell (F-10).
    """
    w = pd.read_csv(DATA / "raw_weather_sea.csv", skiprows=3)
    m = pd.read_csv(DATA / marine_file, skiprows=3)

    w["time"] = pd.to_datetime(w["time"])
    m["time"] = pd.to_datetime(m["time"])

    d = w.merge(m, on="time", how="inner", suffixes=("", "_m"))
    d = d.rename(columns={
        "wind_speed_10m (kn)": "wind",
        "precipitation (mm)": "precip",
        "weather_code (wmo code)": "wmo",
        "wave_height (m)": "wave",
    })
    d = d.dropna(subset=["wave", "wind", "precip"])
    d["hour"] = d["time"].dt.hour
    return d.sort_values("time").reset_index(drop=True)


def classify(d):
    """f(E) = max-severity over the five component functions, small vessel.

    g_m is held at `none` throughout — no marine warning archive exists.
    Because aggregation is by maximum, g_m can only RAISE severity, so every
    figure produced here is a lower bound.
    """
    g_w = np.where(d["wind"] > 27, UNSAFE, np.where(d["wind"] > 22, CAUTION, SAFE))
    storm = (d["precip"] > 20) | d["wmo"].isin([95, 96, 99])
    g_r = np.where(storm, UNSAFE, np.where(d["precip"] > 7.5, CAUTION, SAFE))
    g_o = np.where(d["wave"] > HI, UNSAFE, np.where(d["wave"] >= LO, CAUTION, SAFE))
    g_t = np.where((d["hour"] >= 6) & (d["hour"] < 17), SAFE,
                   np.where((d["hour"] >= 17) & (d["hour"] < 19), CAUTION, UNSAFE))
    g_m = np.full(len(d), SAFE)
    return np.max(np.column_stack([g_w, g_r, g_m, g_o, g_t]), axis=1)


def admissible(states, cond):
    table = A_AI[cond]
    return [table[s] for s in states]


# --------------------------------------------------------------------------
# Reporting
# --------------------------------------------------------------------------

def divergence_matrix(states, mask, label):
    sub = states[mask]
    n = len(sub)
    sets = {c: admissible(sub, c) for c in ORDER}

    print(f"\n{'='*78}")
    print(f"{label}   (n = {n:,} hours)")
    print("=" * 78)

    dist = {STATE_NAME[s]: int((sub == s).sum()) for s in (SAFE, CAUTION, UNSAFE)}
    print("  state distribution: " + "   ".join(
        f"{k} {v:,} ({100*v/n:.1f}%)" for k, v in dist.items()))

    print(f"\n  Pairwise admissible-set divergence (% of hours the two")
    print(f"  conditions permit DIFFERENT recommendation sets)\n")
    print("                     " + "".join(f"{LABEL[c]:>20}" for c in ORDER))
    results = {}
    for a in ORDER:
        row = f"  {LABEL[a]:<18}"
        for b in ORDER:
            diff = sum(1 for x, y in zip(sets[a], sets[b]) if x != y)
            pct = 100 * diff / n
            results[(a, b)] = pct
            row += f"{'—' if a == b else f'{pct:6.2f}%':>20}"
        print(row)
    return results, n


def run_config(cfg_label, marine_file):
    d = load(marine_file)
    states = classify(d)
    print(f"\n\n{'#'*78}\n# {cfg_label}\n{'#'*78}")
    print(f"Loaded {len(d):,} hourly records  "
          f"{d.time.min():%Y-%m-%d} to {d.time.max():%Y-%m-%d}")

    dep = (d.hour >= 5) & (d.hour <= 9)
    allh = pd.Series(True, index=d.index)

    r_all, _ = divergence_matrix(states, allh.values, "ALL HOURS")
    r_dep, _ = divergence_matrix(states, dep.values, "DEPARTURE WINDOW 05:00-09:00")
    return r_all, r_dep


def main():
    print(__doc__)

    results = {}
    for label, mf in CONFIGS.items():
        results[label] = run_config(label, mf)

    # Headline reporting uses PRIMARY. The PREDICTION CHECK, however, must be
    # scored against the configuration each prediction was REGISTERED on —
    # P21-P24 were registered against MFWAM on 2026-09-06. Scoring them against
    # a configuration adopted afterwards would let a later reporting decision
    # retroactively "refute" a prediction that was correct for what it claimed.
    # A register that changes verdicts when the reporting config changes is
    # worthless.
    primary_label = list(CONFIGS)[0]
    r_all, r_dep = results[primary_label]
    reg_all, reg_dep = results[list(CONFIGS)[1]]   # MFWAM — registration config

    print(f"\n\n{'='*78}")
    print("C1 vs C3 DIVERGENCE — BOTH CONFIGURATIONS")
    print("=" * 78)
    for label, (ra, rd) in results.items():
        print(f"  {label}")
        print(f"      all hours {ra[('C1','C3')]:6.2f}%      departure window {rd[('C1','C3')]:6.2f}%")

    # ----------------------------------------------------------------------
    print(f"\n{'='*78}")
    print("THE RESULT THAT ANSWERS THE NOVELTY OBJECTION")
    print("=" * 78)
    c1c3_all = r_all[("C1", "C3")]
    c1c3_dep = r_dep[("C1", "C3")]
    print(f"""
  C3 (Flehmig-style, three-level) vs C1 (plain binary gate):

      all hours          {c1c3_all:6.2f}%  divergence
      departure window   {c1c3_dep:6.2f}%  divergence

  The closest structural precedent in the reviewed literature produces the
  SAME admissible recommendation set as a binary gate in every hour of the
  record. Its intermediate level is not observable in AI output at all.

  C2 (proposed) vs C1:   {r_dep[('C2','C1')]:6.2f}%  of departure hours
  C2 (proposed) vs C3:   {r_dep[('C2','C3')]:6.2f}%  of departure hours

  Those hours are the CAUTION state. They are where the proposed architecture
  restricts advisory scope and every other condition does not.
""")

    # ----------------------------------------------------------------------
    print("=" * 78)
    print("ISOLATING THE LEVEL 2 CONTRIBUTION")
    print("=" * 78)
    lvl1 = r_dep[("C0", "C1")]
    both = r_dep[("C0", "C2")]
    print(f"""
  C0 vs C1  = {lvl1:6.2f}%   attributable to Level 1 (participation gate)
  C0 vs C2  = {both:6.2f}%   attributable to Levels 1 + 2 combined
  difference= {both - lvl1:6.2f}%   attributable to LEVEL 2 ALONE

  Level 2 is the contribution no reviewed architecture implements.
""")

    # ----------------------------------------------------------------------
    print("=" * 78)
    print("PRE-REGISTERED PREDICTION CHECK")
    print("=" * 78)
    reg = pd.read_csv(DATA / "prediction-register.csv")
    print("  Scored against the MFWAM configuration these were registered on.\n")
    checks = {
        "P21": (reg_all[("C1","C3")],  "exact", 0.0,  0.0),
        "P22": (reg_dep[("C2","C1")],  "range", 6.0,  6.2),
        "P23": (reg_dep[("C0","C2")],  "range", 20.0, 30.0),
        "P24": (reg_dep[("C0","C1")],  "range", 14.0, 24.0),
    }
    for pid, (actual, kind, lo, hi) in checks.items():
        ok = (actual == lo) if kind == "exact" else (lo <= actual <= hi)
        status = "CONFIRMED" if ok else "REFUTED"
        stated = reg.loc[reg.id == pid, "pred_stated"].iloc[0]
        print(f"  {pid}  predicted {str(stated):>10}   actual {actual:8.2f}   {status}")
        reg.loc[reg.id == pid, "actual"] = round(float(actual), 2)
        reg.loc[reg.id == pid, "status"] = status
        reg.loc[reg.id == pid, "resolved"] = "2026-09-06"

    reg.to_csv(DATA / "prediction-register.csv", index=False)
    print("\nRegister updated.")

    print(f"""
{'='*78}
SCOPE OF THIS RESULT — state these alongside any figure above
{'='*78}
  1. Admissible-set level only. The reasoning engine is not implemented, so
     AI(E) content within each set is not compared. Layer 3 would add that.
  2. C3 ports Flehmig's governance topology onto environmental state. Their
     index conditions on AI degradation. This compares structures, not systems.
  3. g_m held at `none` throughout — no archive. All figures are LOWER BOUNDS.
  4. No incident data exists for this site. This measures what the conditions
     DO, not whether what they do is correct.
""")


if __name__ == "__main__":
    main()
