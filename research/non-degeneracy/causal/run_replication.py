#!/usr/bin/env python3
"""Runner for the R3 causal replication. `leakcheck` then `run`."""
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

from causal_replication import (
    load, classify, build_calibration, generate, leak_checks,
    WINDOW, EVAL_START, WARMUP_END, HORIZON, P_GO, P_OK, MIN_GAIN, MIN_DUR,
)
import causal_metrics as M

OUT = Path(__file__).resolve().parent


def episodes_of(d):
    return [i for i in d.index
            if d.at[i, "hour"] in WINDOW and d.at[i, "time"] >= EVAL_START]


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "run"
    d = load()
    eps = episodes_of(d)
    print(f"record hours {len(d):,} | evaluation episodes {len(eps):,} "
          f"| warm-up ends {WARMUP_END}")

    if mode == "leakcheck":
        res, _, _ = leak_checks(d, eps)
        (OUT / "leakage-checks.json").write_text(json.dumps(res, indent=2))
        print(json.dumps(res, indent=2))
        print("\nGATES_PASS_for_causal_conditions:",
              res["GATES_PASS_for_causal_conditions"])
        return

    # availability attestation (A-CHK) — declarations, not gates
    a_chk = {
        "A-CHK-1_products": {
            "waves": "ERA5-Ocean reanalysis via raw_marine_era5_sea.csv (v2 sea cell)",
            "wind_precip_wmo": "Open-Meteo archive via raw_weather_sea.csv (v2 sea cell)"},
        "A-CHK-2_production_latency": "reanalysis: days (preliminary) to months (final) "
                                      "— exceeds the decision horizon by orders of magnitude",
        "A-CHK-3_existed_at_episode_date": "partly: ERA5 existed; this sea-cell extraction did not",
        "A-CHK-4_reachable_at_site": "NOT ASSESSED — would require fieldwork",
        "A-CHK-5_spatial_representativeness": "9-55 km grid; site may sit offshore of its "
                                              "own sheltered water",
        "A-CHK-6_VERDICT": "C1 (chronological causality) SATISFIED for G-A and G-B. "
                           "C2 (operational availability) NOT SATISFIED for any condition, "
                           "including G-A and G-B. Declared, not a gate.",
    }
    (OUT / "availability-attestation.json").write_text(json.dumps(a_chk, indent=2))

    S, gt = classify(d)
    cal_c = build_calibration(d, causal=True)
    cal_l = build_calibration(d, causal=False)

    results = {}
    frames = {}
    for cond in ("G-L", "G-A", "G-B"):
        cal = cal_l if cond == "G-L" else cal_c
        df = generate(d, cond, cal, eps)
        df["month"] = [d.at[i, "month"] for i in df["idx"]]
        frames[cond] = df
        print(f"\n{'='*70}\n{cond}: {len(df):,} episodes generated")
        r = {"condition": cond,
             "calibration": "whole-record (LEAKY, L1/L2)" if cond == "G-L"
                            else "causal, monthly epochs, prior data only",
             "forecast": {"G-L": "realised future values (LEAKY, L3)",
                          "G-A": "persistence",
                          "G-B": "damped persistence toward causal climatology"}[cond]}
        r["GC"] = M.gc(df)
        r["ES"] = M.es(df, d, cal, cond)
        r["GE"], r["CA"] = M.ge_ca(df, d, S, gt)
        results[cond] = r
        df.drop(columns=["fc"]).to_csv(
            OUT / f"case-table-{cond}.csv", index=False)

    # E-ES-8 is a property of the index vs the classifier, not of a forecast:
    # computed once, on observed values, under causal calibration.
    results["E-ES-8_index_state_concordance"] = M.es8(
        frames["G-A"], d, cal_c, S, gt)

    # validation
    sdf = np.array([int(S[i]) for i in eps])
    results["validation"] = {
        "V-1_P_S_CAUTION_pct": round(100 * float((sdf == 1).mean()), 4),
        "V-1_UNSAFE_share_pct": round(100 * float((sdf == 2).mean()), 4),
        "V-1_note": "published canonical figures on the full 9,135-episode window "
                    "are 5.81% and 42.88%; this window is 2021-2024 only",
        "V-3_G-L_on_eval_window_type_shares":
            results["G-L"]["GC"]["E-GC-1_type_share"],
        "V-3_published_9135_window":
            {"Go": 0.6938, "Delay": 0.3062,
             "DepartureTime": 0.3612, "Duration": 0.7256},
    }
    results["preregistration"] = {
        "P_GO": P_GO, "P_OK": P_OK, "MIN_GAIN_PCTL": MIN_GAIN,
        "MIN_DURATION_H": MIN_DUR, "TRIP_HORIZON_H": HORIZON,
        "note": "thresholds unchanged from the original gate; no threshold was "
                "adjusted after seeing any result",
    }
    (OUT / "results-causal-replication.json").write_text(
        json.dumps(results, indent=2, default=str))

    # terse console verdict matrix
    print(f"\n{'='*70}\nVERDICT MATRIX (exploratory)\n{'='*70}")
    keys = [("GC", "E-GC-1_PASS"), ("GC", "E-GC-2b-i_PASS"),
            ("GC", "E-GC-2b-ii_PASS"), ("GC", "E-GC-2b-iii_PASS"),
            ("GC", "E-GC-2b-iv_PASS"), ("GC", "E-GC-3_PASS_at_0500"),
            ("ES", "E-ES-5_PASS"), ("GE", "E-GE-2_MEETS_MARKER"),
            ("CA", "E-CA-1_PASS"), ("CA", "E-CA-2_PASS"), ("CA", "E-CA-3_PASS")]
    print(f"{'criterion':<28}{'G-L':>10}{'G-A':>10}{'G-B':>10}")
    for blk, k in keys:
        row = f"{k.replace('_PASS','').replace('_MEETS_MARKER',''):<28}"
        for c in ("G-L", "G-A", "G-B"):
            row += f"{str(results[c][blk].get(k)):>10}"
        print(row)
    print("\nNo composite pass is computed. Dimension-level verdicts only.")


if __name__ == "__main__":
    main()
