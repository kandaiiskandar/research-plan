"""g_t COUNTERFACTUAL SENSITIVITY ANALYSIS — read-only, non-canonical.

Compares three time-semantics models. Changes NOTHING: does not write to the
prediction register, does not emit canonical figures, does not touch g_w, g_r,
g_m or g_o. Same dataset, vessel, exclusion set D={m}, aggregation rule.

  A  incumbent fixed clock   SAFE 06-17, CAUTION 17-19, UNSAFE else
  B  sunrise/sunset          SAFE sunrise<=t<sunset, UNSAFE else  (2-state)
  C  civil twilight          SAFE sunrise<=t<sunset;
                             CAUTION civil_dawn<=t<sunrise or sunset<=t<civil_dusk;
                             UNSAFE else                          (exploratory)

Solar times: NOAA algorithm, scripts/sensitivity/solar.py. See finding for the
reproducibility caveat.
"""
import sys, numpy as np, pandas as pd
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from solar import solar_table

ROOT = Path(__file__).resolve().parent.parent.parent
DATA = ROOT / "data"
W_CAUTION, W_UNSAFE = 21.6, 27.0
R_CAUTION, R_UNSAFE = 10.0, 20.0
TH = {"small": (1.0, 1.25), "big": (1.5, 3.5)}
SAFE, CAUTION, UNSAFE = 0, 1, 2
CFG = {"PRIMARY": "raw_marine_era5_sea.csv", "RESOLUTION": "raw_marine_mfwam.csv"}


def load(mf):
    w = pd.read_csv(DATA/"raw_weather_sea.csv", skiprows=3)
    m = pd.read_csv(DATA/mf, skiprows=3)
    w["time"] = pd.to_datetime(w["time"]); m["time"] = pd.to_datetime(m["time"])
    d = w.merge(m, on="time", how="inner").rename(columns={
        "wind_speed_10m (kn)":"wind","weather_code (wmo code)":"wmo",
        "precipitation (mm)":"precip","wave_height (m)":"wave"})
    d = d.dropna(subset=["wave","wind","precip"]).sort_values("time").reset_index(drop=True)
    d["hour"] = d.time.dt.hour
    return d


def gt_models(d):
    h = d.hour.values.astype(float)
    A = np.where((h>=6)&(h<17), SAFE, np.where((h>=17)&(h<19), CAUTION, UNSAFE))
    s = solar_table([x.date() for x in d.time])
    sr, ss, cd, ck = s["sunrise"], s["sunset"], s["civil_dawn"], s["civil_dusk"]
    B = np.where((h>=sr)&(h<ss), SAFE, UNSAFE)
    C = np.where((h>=sr)&(h<ss), SAFE,
        np.where(((h>=cd)&(h<sr))|((h>=ss)&(h<ck)), CAUTION, UNSAFE))
    return {"A":A,"B":B,"C":C}, (sr,ss,cd,ck)


def others(d, vessel):
    lo, hi = TH[vessel]
    return {
      "g_w": np.where(d.wind>W_UNSAFE, UNSAFE, np.where(d.wind>W_CAUTION, CAUTION, SAFE)),
      "g_r": np.where((d.precip>R_UNSAFE)|d.wmo.isin([95,96,99]), UNSAFE,
                      np.where(d.precip>R_CAUTION, CAUTION, SAFE)),
      "g_m": np.full(len(d), SAFE),
      "g_o": np.where(d.wave>hi, UNSAFE, np.where(d.wave>=lo, CAUTION, SAFE)),
    }


def analyse(d, gt, oth, label):
    f = np.max(np.column_stack([oth["g_w"],oth["g_r"],oth["g_m"],oth["g_o"],gt]), axis=1)
    n = len(f)
    othmax = np.max(np.column_stack([oth["g_w"],oth["g_r"],oth["g_m"],oth["g_o"]]), axis=1)
    dep = ((d.hour>=5)&(d.hour<=9)).values
    r = {"label":label,"n":n}
    for k,v in [("SAFE",SAFE),("CAUTION",CAUTION),("UNSAFE",UNSAFE)]:
        r[f"h_{k}"]=int((f==v).sum()); r[f"p_{k}"]=100*(f==v).mean()
    r["gt_activations"]=int((gt>SAFE).sum())
    r["gt_act_pct"]=100*(gt>SAFE).mean()
    ns = f>SAFE
    r["gt_tied_at_max"]=100*(gt[ns]==f[ns]).mean() if ns.sum() else 0.0
    r["gt_exclusive"]=100*((gt[ns]==f[ns])&(othmax[ns]<f[ns])).mean() if ns.sum() else 0.0
    for c in ["g_w","g_r","g_m","g_o"]:
        ov = ns & (gt>SAFE) & (oth[c]>=gt)
        r[f"ovl_{c}"]=int(ov.sum())
    ch = f[1:]!=f[:-1]; gch = gt[1:]!=gt[:-1]
    r["trans_total"]=int(ch.sum()); r["trans_gt"]=int((ch&gch).sum())
    r["trans_per_day"]=r["trans_gt"]/ (n/24)
    a,b = f[:-1], f[1:]
    r["SC_gt"]=int(((a==SAFE)&(b==CAUTION)&gch).sum())
    r["CU_gt"]=int(((a==CAUTION)&(b==UNSAFE)&gch).sum())
    r["SU_all"]=int(((a==SAFE)&(b==UNSAFE)).sum())
    r["SU_gt"]=int(((a==SAFE)&(b==UNSAFE)&gch).sum())
    r["level2_dep"]=100*(f[dep]==CAUTION).mean()
    return r


def main():
    print(__doc__)
    out={}
    for cname, mf in CFG.items():
        d = load(mf); models,_ = gt_models(d)
        for mk in ["A","B","C"]:
            out[(cname,mk)] = analyse(d, models[mk], others(d,"small"), f"{cname}/{mk}")
    rows=[("hours SAFE","h_SAFE","{:,}"),("hours CAUTION","h_CAUTION","{:,}"),("hours UNSAFE","h_UNSAFE","{:,}"),
          ("% SAFE","p_SAFE","{:.2f}%"),("% CAUTION","p_CAUTION","{:.2f}%"),("% UNSAFE","p_UNSAFE","{:.2f}%"),
          ("g_t activations","gt_activations","{:,}"),("g_t activation %","gt_act_pct","{:.2f}%"),
          ("g_t tied-at-max (non-SAFE)","gt_tied_at_max","{:.2f}%"),
          ("g_t EXCLUSIVE binding","gt_exclusive","{:.2f}%"),
          ("overlap g_w >= g_t","ovl_g_w","{:,}"),("overlap g_r >= g_t","ovl_g_r","{:,}"),
          ("overlap g_m >= g_t","ovl_g_m","{:,}"),("overlap g_o >= g_t","ovl_g_o","{:,}"),
          ("total transitions","trans_total","{:,}"),("g_t-caused transitions","trans_gt","{:,}"),
          ("g_t transitions / day","trans_per_day","{:.2f}"),
          ("SAFE->CAUTION by g_t","SC_gt","{:,}"),("CAUTION->UNSAFE by g_t","CU_gt","{:,}"),
          ("SAFE->UNSAFE (any)","SU_all","{:,}"),("SAFE->UNSAFE by g_t","SU_gt","{:,}"),
          ("LEVEL 2 BINDING (dep 05-09)","level2_dep","{:.2f}%")]
    for cname in CFG:
        print("\n"+"="*84); print(f"{cname}   (n = {out[(cname,'A')]['n']:,} hours)"); print("="*84)
        print(f"  {'':32}{'A incumbent':>16}{'B sun':>16}{'C civil':>16}")
        print("  "+"-"*80)
        for lab,key,fmt in rows:
            v=[fmt.format(out[(cname,m)][key]) for m in "ABC"]
            print(f"  {lab:<32}{v[0]:>16}{v[1]:>16}{v[2]:>16}")
    print("\n"+"="*84); print("DELTA vs INCUMBENT — Level 2 binding"); print("="*84)
    for cname in CFG:
        a=out[(cname,'A')]['level2_dep']
        for m in "BC":
            x=out[(cname,m)]['level2_dep']
            print(f"  {cname:<12} A {a:6.2f}%  ->  {m} {x:6.2f}%   delta {x-a:+6.2f} pp")

main()
