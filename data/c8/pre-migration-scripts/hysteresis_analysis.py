#!/usr/bin/env python3
"""
Hysteresis / mode-chattering analysis.

Both papers assert mode-chattering at classification boundaries as a
deployment concern, mitigated by dual-threshold hysteresis. Neither presents
evidence. The 20-scenario evaluation design could not test it — all scenarios
were static single-point evaluations. The hourly time series can.

Resolves pre-registered predictions P09-P13 (data/prediction-register.csv).

Method
------
1. Classify f(E) for every hour, small vessel.
2. Count state transitions f[i] != f[i-1].
3. Separate SCHEDULED transitions (g_t changed across the boundary — these
   are deterministic clock events at 06:00 / 17:00 / 19:00 and are not
   chattering) from NON-SCHEDULED ones.
4. Count A->B->A round trips within a 3-hour window, excluding scheduled.
5. Re-run with dual-threshold hysteresis on g_o and g_r and measure the
   reduction in non-scheduled transitions.

CAVEAT: hourly resolution. Sub-hourly oscillation is invisible in this data.
A null result here bounds the claim at hourly resolution only.
"""

import pandas as pd
import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

# Wind thresholds — anchored 2026-09-08. MET Malaysia Cat 1 / Cat 2 onsets,
# preserved at the source value rather than rounded:
#   W_CAUTION  40 km/h / 1.852 = 21.598 kn -> 21.6 at data resolution.
#   W_UNSAFE   50 km/h / 1.852 = 26.998 kn -> 27.0 at data resolution.
# Superseded: W_CAUTION was 22, an undocumented rounding of 21.598. That
# rounding suppressed 2 activations in 5 years and made F-1 read "never
# fires" rather than "almost never binds". See appendix-c C.2 and F-17.
W_CAUTION, W_UNSAFE = 21.6, 27.0

# Rainfall thresholds — anchored 2026-09-08. See
# docs/canonical/finding-met-lower-boundary-gap.md and appendix-c C.2.
#   R_UNSAFE  MET Malaysia Ribut Petir warning trigger (> 20 mm/hr).
#   R_CAUTION JPS/DID Infobanjir Light-category upper limit (10 mm/hr).
#             MET publishes NO criterion below 20 mm/hr, so this boundary
#             is necessarily non-MET — the same structure as the wave case.
# Superseded: R_CAUTION was 7.5, which matched no published source.
R_CAUTION, R_UNSAFE = 10.0, 20.0

LO, HI = 1.0, 1.25         # g_o small-vessel thresholds — amended 2026-09-06
MARGIN = 0.10              # 10% return margin for hysteresis


def load():
    w = pd.read_csv(DATA / "raw_weather.csv", skiprows=3)
    m = pd.read_csv(DATA / "raw_marine.csv", skiprows=3)
    r = pd.read_csv(DATA / "raw_rainfall.csv", skiprows=3)
    d = pd.DataFrame({
        "time": pd.to_datetime(w["time"]),
        "wind": w["wind_speed_10m (kn)"].values,
        "wmo":  w["weather_code (wmo code)"].values,
        "wave": m["wave_height (m)"].values,
        "precip": r["precipitation (mm)"].values,
    })
    d["hour"] = d["time"].dt.hour
    return d.sort_values("time").reset_index(drop=True)


def g_t_series(d):
    return np.where((d["hour"] >= 6) & (d["hour"] < 17), 0,
                    np.where((d["hour"] >= 17) & (d["hour"] < 19), 1, 2))


def classify_plain(d):
    g_w = np.where(d["wind"] > W_UNSAFE, 2, np.where(d["wind"] > W_CAUTION, 1, 0))
    storm = (d["precip"] > R_UNSAFE) | d["wmo"].isin([95, 96, 99])
    g_r = np.where(storm, 2, np.where(d["precip"] > R_CAUTION, 1, 0))
    g_o = np.where(d["wave"] > HI, 2, np.where(d["wave"] >= LO, 1, 0))
    g_t = g_t_series(d)
    return np.max(np.column_stack([g_w, g_r, g_o, g_t]), axis=1), g_t


def classify_hysteretic(d):
    """Dual-threshold: rising uses nominal, falling requires a lower return."""
    wave = d["wave"].values
    precip = d["precip"].values
    storm = ((d["precip"] > R_UNSAFE) | d["wmo"].isin([95, 96, 99])).values
    g_t = g_t_series(d)
    g_w = np.where(d["wind"] > W_UNSAFE, 2, np.where(d["wind"] > W_CAUTION, 1, 0))

    n = len(d)
    go = np.zeros(n, dtype=int)
    gr = np.zeros(n, dtype=int)
    prev_o, prev_r = 0, 0
    lo_dn, hi_dn = LO * (1 - MARGIN), HI * (1 - MARGIN)
    r_dn = R_CAUTION * (1 - MARGIN)

    for i in range(n):
        # g_o with hysteresis
        if prev_o == 0:
            s = 2 if wave[i] > HI else (1 if wave[i] >= LO else 0)
        elif prev_o == 1:
            s = 2 if wave[i] > HI else (0 if wave[i] < lo_dn else 1)
        else:
            s = 1 if wave[i] <= hi_dn else 2
            if s == 1 and wave[i] < lo_dn:
                s = 0
        go[i] = s
        prev_o = s

        # g_r with hysteresis
        if storm[i]:
            s = 2
        elif prev_r >= 1:
            s = 1 if precip[i] > r_dn else 0
        else:
            s = 1 if precip[i] > R_CAUTION else 0
        gr[i] = s
        prev_r = s

    return np.max(np.column_stack([g_w, gr, go, g_t]), axis=1), g_t


def transition_stats(f, g_t, label):
    ch = f[1:] != f[:-1]
    t_ch = g_t[1:] != g_t[:-1]
    total = int(ch.sum())
    scheduled = int((ch & t_ch).sum())
    non_sched = int((ch & ~t_ch).sum())
    print(f"\n{label}")
    print(f"  total state transitions      : {total:6,}")
    print(f"  scheduled (g_t changed)      : {scheduled:6,}  ({100*scheduled/max(total,1):4.1f}%)")
    print(f"  NON-scheduled                : {non_sched:6,}  ({100*non_sched/max(total,1):4.1f}%)")
    print(f"  transitions per day          : {total/1827:6.2f}")
    return total, scheduled, non_sched


def count_oscillations(f, g_t, window=3):
    """A->B->A round trips within `window` hours, ignoring scheduled changes."""
    n = len(f)
    osc = 0
    examples = []
    for i in range(1, n):
        if f[i] == f[i - 1] or g_t[i] != g_t[i - 1]:
            continue
        a, b = f[i - 1], f[i]
        for j in range(i + 1, min(i + 1 + window, n)):
            if g_t[j] != g_t[j - 1]:
                break
            if f[j] == a and f[j - 1] == b:
                osc += 1
                if len(examples) < 5:
                    examples.append((i, a, b, j - i))
                break
    return osc, examples


def _register_guard(reg, pid):
    """Refuse to overwrite an already-resolved prediction.

    Added 2026-09-08. Twice, re-running an analysis after a SPECIFICATION
    change silently rewrote verdicts for predictions registered against an
    earlier configuration (P09, P18 — both restored by hand). A register whose
    verdicts move whenever the specification moves records nothing. Resolved
    entries are therefore immutable here: a prediction that no longer holds
    under a new specification is handled by an explicit, documented
    re-resolution (as P16 and P22 were), never by a silent re-run.
    """
    row = reg.loc[reg.id == pid]
    return not (len(row) and str(row["status"].iloc[0]).strip() in ("CONFIRMED", "REFUTED"))


def main():
    d = load()
    print(__doc__)
    print(f"Loaded {len(d):,} records over {len(d)/24:.0f} days")

    f_plain, g_t = classify_plain(d)
    f_hyst, _ = classify_hysteretic(d)

    print("\n" + "=" * 78)
    print("TRANSITION COUNTS — small vessel, all hours")
    print("=" * 78)
    tot_p, sch_p, non_p = transition_stats(f_plain, g_t, "WITHOUT hysteresis")
    tot_h, sch_h, non_h = transition_stats(f_hyst, g_t, f"WITH hysteresis ({int(MARGIN*100)}% return margin)")

    reduction = 100 * (non_p - non_h) / non_p if non_p else 0.0
    print(f"\n  Reduction in non-scheduled transitions: {non_p:,} -> {non_h:,}  ({reduction:.1f}%)")

    print("\n" + "=" * 78)
    print("MODE-CHATTERING: A->B->A round trips within 3 hours (scheduled excluded)")
    print("=" * 78)
    osc_p, ex = count_oscillations(f_plain, g_t)
    osc_h, _ = count_oscillations(f_hyst, g_t)
    print(f"  without hysteresis : {osc_p:5,}   ({osc_p/5:.1f} per year)")
    print(f"  with hysteresis    : {osc_h:5,}   ({osc_h/5:.1f} per year)")
    if ex:
        print("  examples (index, from, to, hours to return):")
        for e in ex:
            print(f"    {d.time.iloc[e[0]]}  {e[1]}->{e[2]}->{e[1]}  after {e[3]}h")

    print("\n" + "=" * 78)
    print("PRE-REGISTERED PREDICTION CHECK")
    print("=" * 78)
    reg = pd.read_csv(DATA / "prediction-register.csv")
    checks = {
        "P09": (tot_p,      "range", 5400, 8000),
        "P10": (non_p,      "max",      0,  500),
        "P11": (osc_p,      "max",      0,  100),
        "P12": (reduction,  "range",    5,   40),
    }
    for pid, (actual, kind, lo, hi) in checks.items():
        ok = (actual >= lo) if kind == "min" else (actual <= hi) if kind == "max" else (lo <= actual <= hi)
        status = "CONFIRMED" if ok else "REFUTED"
        stated = reg.loc[reg.id == pid, "pred_stated"].iloc[0]
        print(f"  {pid}  predicted {stated:>12}   actual {actual:9.1f}   {status}")
        if _register_guard(reg, pid):
            reg.loc[reg.id == pid, "actual"] = round(float(actual), 2)
        if _register_guard(reg, pid):
            reg.loc[reg.id == pid, "status"] = status
        if _register_guard(reg, pid):
            reg.loc[reg.id == pid, "resolved"] = "2026-09-06"

    # P13 — interpretation
    p13 = "CONFIRMED" if (non_p <= 500 and osc_p <= 100) else "REFUTED"
    if _register_guard(reg, "P13"):
        reg.loc[reg.id == "P13", "actual"] = f"non-sched={non_p}, osc={osc_p}"
    if _register_guard(reg, "P13"):
        reg.loc[reg.id == "P13", "status"] = p13
    if _register_guard(reg, "P13"):
        reg.loc[reg.id == "P13", "resolved"] = "2026-09-06"
    print(f"  P13  predicted           NO   (chattering not demonstrated)   {p13}")

    reg.to_csv(DATA / "prediction-register.csv", index=False)
    print(f"\nRegister updated.")


if __name__ == "__main__":
    main()
