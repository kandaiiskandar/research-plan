#!/usr/bin/env python3
"""C-5: three-stage hysteretic isolation for P12 and the related P09-P13 metrics.

WHAT THIS IS
------------
SDR-001 is APPROVED but NOT YET APPLIED. Two independent changes exist:

    data/configuration :  v1 (land cell)  ->  v2 (sea cell)
    classifier         :  g_t incumbent   ->  g_t Model B

Comparing v1/incumbent directly against v2/ModelB confounds them. This script
therefore runs THREE stages so each effect is isolated:

    Stage 1  v1/incumbent    <- provenance gate: must reproduce P12 = 7.83
    Stage 2  v2/incumbent    <- Delta_data  = Stage2 - Stage1
    Stage 3  v2/ModelB       <- Delta_g_t   = Stage3 - Stage2

WHAT THIS IS NOT
----------------
* It does NOT re-resolve predictions and does NOT write the register.
  `hysteresis_analysis.py` writes the register on every run, so it is NEVER
  executed here. Its functions are imported and reused instead, unmodified.
* It does NOT perform canonical migration. Canonical g_t is untouched.
* It does NOT redesign hysteresis. `classify_hysteretic` semantics are reused
  verbatim for all three stages.
* It does NOT recompute solar astronomy. Stage 3 reads the frozen C-3 artefact
  `data/solar/solar-events-daily.csv`. No solar equations appear in this file.

HYSTERESIS SEMANTICS (reused, not redefined)
--------------------------------------------
* Applies to g_o and g_r ONLY. Never to g_w, never to g_t, never to the
  aggregate. It acts at COMPONENT level, BEFORE max-severity.
* Rising edge uses the nominal threshold; falling edge requires the value to
  drop below threshold*(1-MARGIN), MARGIN = 0.10.
* State memory: prev_o / prev_r carried across consecutive rows.
* Initialisation: prev_o = prev_r = 0 (SAFE). Identical in all three stages.
* g_r storm (precip > R_UNSAFE or WMO 95/96/99) overrides hysteresis to UNSAFE.
* D = {m}: g_m is pinned SAFE and is simply absent from the max, exactly as in
  the original script.

CONSEQUENCE FOR MODEL B, STATED EXPLICITLY
-------------------------------------------
Because hysteresis never touches g_t, the Model B sunrise/sunset transition is
NOT hysteretically delayed. No sunset smoothing, grace period or twilight band
is introduced. C-4 accepted the direct transition; C-5 measures it.
"""

import csv
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent.parent
DATA = ROOT / "data"
OUT = DATA / "c5"
OUT.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(ROOT / "scripts"))
import hysteresis_analysis as H  # noqa: E402  imported, never executed via main()

SOLAR = DATA / "solar" / "solar-events-daily.csv"


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


# ---------------------------------------------------------------- loaders
def load_v1():
    """EXACTLY the historical path: H.load() over the v1 land-cell files.

    Note the historical positional alignment (three frames read separately,
    `.values` taken without a join on time). Preserved deliberately — Stage 1
    must reproduce the historical number, not improve on it.
    """
    return H.load()


def load_v2():
    """v2 sea-cell, canonical PRIMARY configuration.

    Weather AND precipitation both from raw_weather_sea.csv (per
    canonical_figures.py: raw_rainfall.csv is still on the condemned land
    cell). Waves from raw_marine_era5_sea.csv. Explicit inner join on time.
    """
    w = pd.read_csv(DATA / "raw_weather_sea.csv", skiprows=3)
    m = pd.read_csv(DATA / "raw_marine_era5_sea.csv", skiprows=3)
    w["time"] = pd.to_datetime(w["time"])
    m["time"] = pd.to_datetime(m["time"])
    j = w.merge(m, on="time", how="inner")
    d = pd.DataFrame({
        "time": j["time"],
        "wind": j["wind_speed_10m (kn)"].values,
        "wmo": j["weather_code (wmo code)"].values,
        "wave": j["wave_height (m)"].values,
        "precip": j["precipitation (mm)"].values,
    }).dropna(subset=["wind", "wave", "precip"])
    d["hour"] = d["time"].dt.hour
    return d.sort_values("time").reset_index(drop=True)


# ---------------------------------------------------------------- g_t variants
def g_t_incumbent(d):
    """Delegates to the original implementation. Not reimplemented."""
    return H.g_t_series(d)


def g_t_modelb(d):
    """Model B from the FROZEN C-3 solar artefact. No astronomy computed here.

    SAFE when sunrise <= t < sunset (half-open, per solar-spec-v1), else UNSAFE.
    A date absent from the artefact, or a null timestamp, yields UNSAFE -- the
    g_t(bottom) = UNSAFE fail-safe of Corollary C.1b.1.
    """
    sol = pd.read_csv(SOLAR)
    sol["date"] = pd.to_datetime(sol["date"]).dt.date
    sr = dict(zip(sol["date"], sol["sunrise_hours"].astype(float)))
    ss = dict(zip(sol["date"], sol["sunset_hours"].astype(float)))

    out = np.full(len(d), 2, dtype=int)   # default UNSAFE = fail-safe
    dates = d["time"].dt.date.values
    # t is the hour label of the observation, consistent with the incumbent,
    # which also classifies on the integer hour.
    hours = d["hour"].values.astype(float)
    miss = 0
    for i in range(len(d)):
        a, b = sr.get(dates[i]), ss.get(dates[i])
        if a is None or b is None or not np.isfinite(a) or not np.isfinite(b):
            miss += 1
            continue                      # stays UNSAFE
        out[i] = 0 if (a <= hours[i] < b) else 2
    if miss:
        print(f"    !! {miss} rows had no solar entry -> UNSAFE (fail-safe)")
    return out


# ---------------------------------------------------------------- classifiers
def classify_plain_with(d, g_t):
    """H.classify_plain with an injected g_t. Component logic unchanged."""
    g_w = np.where(d["wind"] > H.W_UNSAFE, 2, np.where(d["wind"] > H.W_CAUTION, 1, 0))
    storm = (d["precip"] > H.R_UNSAFE) | d["wmo"].isin([95, 96, 99])
    g_r = np.where(storm, 2, np.where(d["precip"] > H.R_CAUTION, 1, 0))
    g_o = np.where(d["wave"] > H.HI, 2, np.where(d["wave"] >= H.LO, 1, 0))
    return np.max(np.column_stack([g_w, g_r, g_o, g_t]), axis=1)


def classify_hysteretic_with(d, g_t):
    """H.classify_hysteretic with an injected g_t. Hysteresis loop verbatim."""
    wave = d["wave"].values
    precip = d["precip"].values
    storm = ((d["precip"] > H.R_UNSAFE) | d["wmo"].isin([95, 96, 99])).values
    g_w = np.where(d["wind"] > H.W_UNSAFE, 2, np.where(d["wind"] > H.W_CAUTION, 1, 0))

    n = len(d)
    go = np.zeros(n, dtype=int)
    gr = np.zeros(n, dtype=int)
    prev_o, prev_r = 0, 0                      # initialisation: SAFE, SAFE
    lo_dn, hi_dn = H.LO * (1 - H.MARGIN), H.HI * (1 - H.MARGIN)
    r_dn = H.R_CAUTION * (1 - H.MARGIN)

    for i in range(n):
        if prev_o == 0:
            s = 2 if wave[i] > H.HI else (1 if wave[i] >= H.LO else 0)
        elif prev_o == 1:
            s = 2 if wave[i] > H.HI else (0 if wave[i] < lo_dn else 1)
        else:
            s = 1 if wave[i] <= hi_dn else 2
            if s == 1 and wave[i] < lo_dn:
                s = 0
        go[i] = s
        prev_o = s

        if storm[i]:
            s = 2
        elif prev_r >= 1:
            s = 1 if precip[i] > r_dn else 0
        else:
            s = 1 if precip[i] > H.R_CAUTION else 0
        gr[i] = s
        prev_r = s

    return np.max(np.column_stack([g_w, gr, go, g_t]), axis=1)


# ---------------------------------------------------------------- metrics
def metrics(d, g_t, label):
    f_p = classify_plain_with(d, g_t)
    f_h = classify_hysteretic_with(d, g_t)

    ch = f_p[1:] != f_p[:-1]
    t_ch = g_t[1:] != g_t[:-1]
    tot_p = int(ch.sum())
    sch_p = int((ch & t_ch).sum())
    non_p = int((ch & ~t_ch).sum())

    ch_h = f_h[1:] != f_h[:-1]
    tot_h = int(ch_h.sum())
    non_h = int((ch_h & ~t_ch).sum())

    osc_p, _ = H.count_oscillations(f_p, g_t)
    osc_h, _ = H.count_oscillations(f_h, g_t)

    reduction = 100.0 * (non_p - non_h) / non_p if non_p else 0.0
    days = len(d) / 24.0

    return {
        "stage": label,
        "rows": int(len(d)),
        "days": round(days, 2),
        "first": str(d["time"].iloc[0]),
        "last": str(d["time"].iloc[-1]),
        "P09_total_transitions": tot_p,
        "scheduled_transitions": sch_p,
        "P10_non_scheduled": non_p,
        "P11_oscillations": osc_p,
        "P12_reduction_pct": round(reduction, 2),
        "P12_reduction_pct_full": reduction,
        "hyst_total_transitions": tot_h,
        "hyst_non_scheduled": non_h,
        "hyst_oscillations": osc_h,
        "P13_non_sched": non_p,
        "P13_osc": osc_p,
    }


def temporal_check(d, label):
    t = d["time"]
    dup = int(t.duplicated().sum())
    mono = bool(t.is_monotonic_increasing)
    diffs = t.diff().dropna()
    gaps = int((diffs != pd.Timedelta(hours=1)).sum())
    span_h = int((t.iloc[-1] - t.iloc[0]).total_seconds() // 3600) + 1
    return {
        "stage": label, "rows": int(len(d)), "duplicates": dup,
        "monotonic_increasing": mono, "non_hourly_steps": gaps,
        "expected_rows_from_span": span_h,
        "complete_hourly": bool(span_h == len(d) and gaps == 0 and dup == 0),
    }


def p09_provenance(d):
    """Diagnose which configuration reproduces the registered P09 = 5416.

    Read-only. Stage 1 at CURRENT thresholds gives 5220, not 5416, so the
    registered baseline was produced under a different configuration. This
    sweeps the two threshold amendments applied since P09 was resolved:
        rainfall CAUTION  7.5  -> 10.0 mm/hr   (2026-09-08)
        small-vessel o    1.9  -> 1.25 m       (2026-09-06)
    Nothing is changed; the answer is evidence for C-7.
    """
    gt = H.g_t_series(d)
    out = []
    for r_c, r_lab in ((H.R_CAUTION, "10.0 current"), (7.5, "7.5 pre-amend")):
        for hi, o_lab in ((H.HI, "1.25 current"), (1.9, "1.9 pre-amend")):
            g_w = np.where(d["wind"] > H.W_UNSAFE, 2,
                           np.where(d["wind"] > H.W_CAUTION, 1, 0))
            storm = (d["precip"] > H.R_UNSAFE) | d["wmo"].isin([95, 96, 99])
            g_r = np.where(storm, 2, np.where(d["precip"] > r_c, 1, 0))
            g_o = np.where(d["wave"] > hi, 2, np.where(d["wave"] >= H.LO, 1, 0))
            f = np.max(np.column_stack([g_w, g_r, g_o, gt]), axis=1)
            tot = int((f[1:] != f[:-1]).sum())
            out.append({"r_caution": r_lab, "o_unsafe": o_lab,
                        "total_transitions": tot, "matches_registered_5416": tot == 5416})
    return out


def main():
    reg_before = sha(DATA / "prediction-register.csv")
    print("=" * 78)
    print("C-5  THREE-STAGE HYSTERETIC ISOLATION")
    print("=" * 78)
    print(f"register sha256 BEFORE : {reg_before}")
    print(f"hysteresis_analysis.py : {sha(ROOT/'scripts'/'hysteresis_analysis.py')}")
    print(f"solar artefact (C-3)   : {sha(SOLAR)}")
    print(f"hysteresis params      : MARGIN={H.MARGIN}  LO={H.LO} HI={H.HI}  "
          f"R_CAUTION={H.R_CAUTION} R_UNSAFE={H.R_UNSAFE}  "
          f"W_CAUTION={H.W_CAUTION} W_UNSAFE={H.W_UNSAFE}")

    # ---------- Stage 1 : provenance gate
    print("\n--- STAGE 1  v1/incumbent  (PROVENANCE GATE) ---")
    d1 = load_v1()
    tc1 = temporal_check(d1, "stage1_v1_incumbent")
    print(f"  temporal: {tc1}")
    m1 = metrics(d1, g_t_incumbent(d1), "stage1_v1_incumbent")
    print(f"  P09 total={m1['P09_total_transitions']}  P10 non-sched={m1['P10_non_scheduled']}  "
          f"P11 osc={m1['P11_oscillations']}  P12 reduction={m1['P12_reduction_pct']}%")

    print("\n  Register cross-check at Stage 1 (current thresholds):")
    for pid, got, reg_val in (("P09", m1["P09_total_transitions"], 5416),
                              ("P10", m1["P10_non_scheduled"], 230),
                              ("P11", m1["P11_oscillations"], 37),
                              ("P12", m1["P12_reduction_pct"], 7.83)):
        print(f"    {pid}: computed {got:>8}   registered {reg_val:>8}   "
              f"{'MATCH' if float(got) == float(reg_val) else 'DIFFERS'}")

    p09_diag = p09_provenance(d1)
    print("\n  P09 provenance sweep (read-only; which configuration gives 5416?):")
    for r in p09_diag:
        print(f"    r_CAUTION={r['r_caution']:14s} o_UNSAFE={r['o_unsafe']:14s} "
              f"total={r['total_transitions']:5d}"
              f"{'   <== registered 5416' if r['matches_registered_5416'] else ''}")

    AUTHORITATIVE_P12 = 7.83
    delta = abs(m1["P12_reduction_pct"] - AUTHORITATIVE_P12)
    gate = delta < 0.005
    print(f"\n  GATE: P12 computed {m1['P12_reduction_pct']:.2f}  vs authoritative "
          f"{AUTHORITATIVE_P12}  |diff| {delta:.4f}  -> {'PASS' if gate else 'FAIL'}")
    if not gate:
        print("\n  *** C-5 BLOCKED — P12 AUTHORITATIVE BASELINE NOT REPRODUCIBLE ***")
        print("  Stages 2 and 3 NOT executed. Nothing written. See C-7.")
        json.dump({"gate": "FAIL", "stage1": m1, "temporal": tc1,
                   "authoritative_P12": AUTHORITATIVE_P12},
                  (OUT / "c5-gate-failure.json").open("w"), indent=2)
        return 1

    # ---------- Stage 2 : data effect
    print("\n--- STAGE 2  v2/incumbent  (data/configuration effect) ---")
    d2 = load_v2()
    tc2 = temporal_check(d2, "stage2_v2_incumbent")
    print(f"  temporal: {tc2}")
    m2 = metrics(d2, g_t_incumbent(d2), "stage2_v2_incumbent")
    print(f"  P09 total={m2['P09_total_transitions']}  P10 non-sched={m2['P10_non_scheduled']}  "
          f"P11 osc={m2['P11_oscillations']}  P12 reduction={m2['P12_reduction_pct']}%")

    # ---------- Stage 3 : g_t effect
    print("\n--- STAGE 3  v2/ModelB  (g_t design effect, frozen C-3 solar) ---")
    gt3 = g_t_modelb(d2)
    print(f"  g_t from artefact: SAFE={int((gt3==0).sum())}  UNSAFE={int((gt3==2).sum())}  "
          f"CAUTION={int((gt3==1).sum())} (must be 0)")
    tc3 = dict(tc2, stage="stage3_v2_modelb")
    m3 = metrics(d2, gt3, "stage3_v2_modelb")
    print(f"  P09 total={m3['P09_total_transitions']}  P10 non-sched={m3['P10_non_scheduled']}  "
          f"P11 osc={m3['P11_oscillations']}  P12 reduction={m3['P12_reduction_pct']}%")

    # ---------- deltas
    print("\n" + "=" * 78)
    print("ISOLATED EFFECTS")
    print("=" * 78)
    keys = [("P09_total_transitions", "P09 total transitions"),
            ("P10_non_scheduled", "P10 non-scheduled"),
            ("P11_oscillations", "P11 oscillations"),
            ("P12_reduction_pct", "P12 reduction %")]
    print(f"{'metric':26s}{'v1/inc':>10}{'v2/inc':>10}{'v2/MdlB':>10}"
          f"{'D_data':>10}{'D_g_t':>10}{'D_total':>10}")
    deltas = {}
    for k, lab in keys:
        a, b, c = m1[k], m2[k], m3[k]
        dd, dg, dt = round(b - a, 2), round(c - b, 2), round(c - a, 2)
        deltas[k] = {"v1_incumbent": a, "v2_incumbent": b, "v2_modelb": c,
                     "delta_data": dd, "delta_g_t": dg, "delta_total": dt,
                     "additive_check": round(dd + dg, 2) == dt}
        print(f"{lab:26s}{a:>10}{b:>10}{c:>10}{dd:>10}{dg:>10}{dt:>10}")

    # ---------- freeze
    stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    rows = [m1, m2, m3]
    csv_p = OUT / "c5-three-stage-metrics.csv"
    with csv_p.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    json_p = OUT / "c5-three-stage-deltas.json"
    json.dump({"generated_utc": stamp, "gate": "PASS",
               "authoritative_P12": AUTHORITATIVE_P12,
               "stage1_P12": m1["P12_reduction_pct"],
               "stages": rows, "temporal": [tc1, tc2, tc3],
               "deltas": deltas,
               "register_crosscheck_stage1": {
                   "P09": {"computed": m1["P09_total_transitions"], "registered": 5416,
                           "match": m1["P09_total_transitions"] == 5416},
                   "P10": {"computed": m1["P10_non_scheduled"], "registered": 230,
                           "match": m1["P10_non_scheduled"] == 230},
                   "P11": {"computed": m1["P11_oscillations"], "registered": 37,
                           "match": m1["P11_oscillations"] == 37},
                   "P12": {"computed": m1["P12_reduction_pct"], "registered": 7.83,
                           "match": m1["P12_reduction_pct"] == 7.83}},
               "p09_provenance_sweep": p09_diag},
              json_p.open("w"), indent=2)

    manifest = {
        "condition": "C-5",
        "generated_utc": stamp,
        "sdr_001_status": "APPROVED - NOT YET APPLIED",
        "canonical_g_t": "incumbent fixed clock 06:00/17:00/19:00 - UNCHANGED",
        "harness": {"path": "scripts/c5/three_stage_hysteresis.py",
                    "sha256": sha(Path(__file__))},
        "reused_implementation": {
            "path": "scripts/hysteresis_analysis.py",
            "sha256": sha(ROOT / "scripts" / "hysteresis_analysis.py"),
            "note": "imported and reused; NEVER executed (its main() writes the register)"},
        "hysteresis": {"applies_to": ["g_o", "g_r"],
                       "not_applied_to": ["g_w", "g_t", "aggregate"],
                       "level": "component, before max-severity",
                       "margin": H.MARGIN, "init": "prev_o=prev_r=0 (SAFE)",
                       "LO": H.LO, "HI": H.HI,
                       "R_CAUTION": H.R_CAUTION, "R_UNSAFE": H.R_UNSAFE},
        "thresholds": {"W_CAUTION": H.W_CAUTION, "W_UNSAFE": H.W_UNSAFE,
                       "R_CAUTION": H.R_CAUTION, "R_UNSAFE": H.R_UNSAFE,
                       "o_small": [H.LO, H.HI]},
        "exclusions": {"D": ["m"], "note": "g_m pinned SAFE, absent from the max"},
        "stages": {
            "stage1_v1_incumbent": {
                "inputs": {p: sha(DATA / p) for p in
                           ["raw_weather.csv", "raw_marine.csv", "raw_rainfall.csv"]},
                "g_t": "incumbent 06:00/17:00/19:00", "solar_artefact": None,
                "rows": m1["rows"]},
            "stage2_v2_incumbent": {
                "inputs": {p: sha(DATA / p) for p in
                           ["raw_weather_sea.csv", "raw_marine_era5_sea.csv"]},
                "g_t": "incumbent 06:00/17:00/19:00", "solar_artefact": None,
                "rows": m2["rows"]},
            "stage3_v2_modelb": {
                "inputs": {p: sha(DATA / p) for p in
                           ["raw_weather_sea.csv", "raw_marine_era5_sea.csv"]},
                "g_t": "Model B: SAFE sunrise<=t<sunset else UNSAFE; g_t(bottom)=UNSAFE",
                "solar_artefact": {"path": "data/solar/solar-events-daily.csv",
                                   "sha256": sha(SOLAR),
                                   "spec": "solar-spec-v1", "impl": "solar-v1"},
                "rows": m3["rows"]},
        },
        "outputs": {"metrics_csv": {"path": str(csv_p.relative_to(ROOT)), "sha256": sha(csv_p)},
                    "deltas_json": {"path": str(json_p.relative_to(ROOT)), "sha256": sha(json_p)}},
        "register_sha256_before": reg_before,
    }
    man_p = OUT / "c5-run-manifest.json"
    json.dump(manifest, man_p.open("w"), indent=2)

    reg_after = sha(DATA / "prediction-register.csv")
    print(f"\nregister sha256 AFTER  : {reg_after}")
    print(f"REGISTER UNCHANGED     : {reg_before == reg_after}")
    print(f"\nfrozen: {csv_p.relative_to(ROOT)}  sha {sha(csv_p)[:16]}")
    print(f"frozen: {json_p.relative_to(ROOT)}  sha {sha(json_p)[:16]}")
    print(f"frozen: {man_p.relative_to(ROOT)}  sha {sha(man_p)[:16]}")
    print("\nNOTE: no prediction re-resolved. Canonical g_t unchanged.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
