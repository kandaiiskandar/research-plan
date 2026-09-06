#!/usr/bin/env python3
"""
Compare v1 (land-cell wind, ERA5-Ocean 50km waves) against v2 (sea-cell wind,
MFWAM 8km waves). Resolves pre-registered predictions P15-P18.

See docs/canonical/decision-record-empirical-first.md open questions Q1a, Q6.
"""
import pandas as pd, numpy as np
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
TH = {"small": (1.0, 1.25), "medium": (1.4, 2.8), "big": (1.5, 3.5)}


def rd(name, cols):
    d = pd.read_csv(DATA / name, skiprows=3)
    d.columns = cols
    d["time"] = pd.to_datetime(d["time"])
    return d


def g_w(x):  return np.where(x > 27, 2, np.where(x > 22, 1, 0))
def g_r(p, c): return np.where((p > 20) | np.isin(c, [95, 96, 99]), 2, np.where(p > 7.5, 1, 0))
def g_t(h):  return np.where((h >= 6) & (h < 17), 0, np.where((h >= 17) & (h < 19), 1, 2))
def g_o(o, v):
    lo, hi = TH[v]; return np.where(o > hi, 2, np.where(o >= lo, 1, 0))


def main():
    w1 = rd("raw_weather.csv",     ["time","wind","dir","gust","precip","wmo"])
    w2 = rd("raw_weather_sea.csv", ["time","wind","dir","gust","precip","wmo"])
    m1 = rd("raw_marine_era5_sea.csv", ["time","wave","period"])
    m2 = rd("raw_marine_mfwam.csv",    ["time","wave","period"])

    print("=" * 76)
    print("1.  WIND — LAND CELL (v1) vs SEA CELL (v2)          P15, P16")
    print("=" * 76)
    print(f"{'':<22}{'max':>8}{'mean':>8}{'p99':>8}{'>22kn':>9}{'>27kn':>9}")
    for lab, d in [("v1 LAND 5.940,116.100", w1), ("v2 SEA  5.940,116.025", w2)]:
        a = d["wind"]; g = g_w(a)
        print(f"{lab:<22}{a.max():>8.1f}{a.mean():>8.2f}{a.quantile(.99):>8.1f}"
              f"{int((g==1).sum()):>9,}{int((g==2).sum()):>9,}")
    for lab, d in [("v1 gusts", w1), ("v2 gusts", w2)]:
        a = d["gust"]
        print(f"{lab:<22}{a.max():>8.1f}{a.mean():>8.2f}{a.quantile(.99):>8.1f}")
    upl = 100 * (w2["wind"].mean() - w1["wind"].mean()) / w1["wind"].mean()
    p15 = float(w2["wind"].max())
    p16 = int((g_w(w2["wind"]) > 0).sum())
    print(f"\n  mean uplift land->sea : {upl:+.1f}%")
    print(f"  P15 max sustained wind : {p15:.1f} kn")
    print(f"  P16 g_w activations    : {p16:,}")

    print("\n" + "=" * 76)
    print("2.  WAVES — ERA5-Ocean 50km vs MFWAM 8km (overlap only)      P17")
    print("=" * 76)
    ov = m2["time"].min()
    a1 = m1[m1["time"] >= ov].reset_index(drop=True)
    a2 = m2.reset_index(drop=True)
    n = min(len(a1), len(a2)); a1, a2 = a1.iloc[:n], a2.iloc[:n]
    print(f"  overlap: {ov.date()} to {a2['time'].max().date()}  ({n:,} hours)\n")
    print(f"{'':<22}{'max':>8}{'mean':>8}{'p99':>8}{'CAUTION':>10}{'UNSAFE':>9}")
    for lab, d in [("ERA5-Ocean ~50km", a1), ("MFWAM ~8km", a2)]:
        g = g_o(d["wave"].values, "small")
        print(f"{lab:<22}{d['wave'].max():>8.2f}{d['wave'].mean():>8.2f}"
              f"{d['wave'].quantile(.99):>8.2f}{int((g==1).sum()):>10,}{int((g==2).sum()):>9,}")
    c1 = 100*(g_o(a1['wave'].values,'small')==1).sum()/n
    c2 = 100*(g_o(a2['wave'].values,'small')==1).sum()/n
    print(f"\n  g_o CAUTION rate  ERA5 {c1:.1f}%   MFWAM {c2:.1f}%   "
          f"({'MFWAM LOWER' if c2 < c1 else 'MFWAM HIGHER'})")
    print(f"  mean wave         ERA5 {a1['wave'].mean():.2f} m   MFWAM {a2['wave'].mean():.2f} m")
    corr = np.corrcoef(a1['wave'], a2['wave'])[0,1]
    print(f"  correlation between models: {corr:.3f}")

    print("\n" + "=" * 76)
    print("3.  HEADLINE — Level 2 binding rate, departure window        P18")
    print("=" * 76)
    res = {}
    for lab, wdf, mdf in [("v1 (land wind, ERA5 50km)", w1, m1),
                          ("v2 (sea wind,  ERA5 50km)", w2, m1),
                          ("v2 (sea wind,  MFWAM 8km)", w2, m2)]:
        d = wdf.merge(mdf[["time","wave"]], on="time", how="inner")
        d = d[(d.time.dt.hour >= 5) & (d.time.dt.hour <= 9)]
        f = np.max(np.vstack([g_w(d["wind"].values), g_r(d["precip"].values, d["wmo"].values),
                              g_t(d.time.dt.hour.values), g_o(d["wave"].values, "small")]), axis=0)
        rate = 100*(f==1).sum()/len(f)
        res[lab] = rate
        c = np.bincount(f, minlength=3)
        print(f"  {lab:<28} n={len(f):>6,}  SAFE {100*c[0]/len(f):5.1f}%  "
              f"CAUTION {rate:5.1f}%  UNSAFE {100*c[2]/len(f):5.1f}%")
    p18 = res["v2 (sea wind,  MFWAM 8km)"]

    print("\n" + "=" * 76)
    print("PRE-REGISTERED PREDICTION CHECK")
    print("=" * 76)
    reg = pd.read_csv(DATA / "prediction-register.csv")
    checks = {
        "P15": (p15, 20, 30, "range"),
        "P16": (p16, 1, 500, "range"),
        "P17": (c2, None, c1, "lower"),
        "P18": (p18, 8, 12, "range"),
    }
    for pid, (act, lo, hi, kind) in checks.items():
        ok = (act < hi) if kind == "lower" else (lo <= act <= hi)
        st = "CONFIRMED" if ok else "REFUTED"
        stated = reg.loc[reg.id==pid, "pred_stated"].iloc[0]
        print(f"  {pid}  predicted {stated:>24}   actual {act:8.2f}   {st}")
        reg.loc[reg.id==pid, ["actual","status","resolved"]] = [round(float(act),2), st, "2026-09-06"]
    reg.to_csv(DATA / "prediction-register.csv", index=False)
    print("\n  register updated")


if __name__ == "__main__":
    main()
