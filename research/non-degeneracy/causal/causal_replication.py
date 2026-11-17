#!/usr/bin/env python3
"""
R3 causal N1-N4 replication — EXPLORATORY.

READ-ONLY with respect to every canonical artefact. Reads the two raw CSVs and
imports scripts/canonical_gt.g_t. Writes only into this directory. Creates no
new canonical result and supersedes nothing.

Usage:
    python3 causal_replication.py leakcheck    # must pass before `run`
    python3 causal_replication.py run

PRE-REGISTERED per research/n1-n4-causal-replication-spec-r3.md. Thresholds are
NOT adjusted to obtain a pass; failures are reported as failures.

THREE CONDITIONS, identical evaluation window:
  G-L  original leaky generator      — whole-record calibration + realised future
  G-A  persistence                   — causal calibration, forecast = value at h
  G-B  damped persistence→climatology— causal calibration, skilful surrogate

E-GC-2b uses the EPISODE-SPECIFIC MARGIN m_ok = e_hat(h) - e_ok(epoch), not a
global breakpoint: under causal calibration e_ok varies by epoch, so a global
breakpoint would show residual from threshold drift alone — the same class of
artefact as the bin-width defect it replaced.
"""
from pathlib import Path
import json
import sys

import numpy as np
import pandas as pd

REPO = Path(__file__).resolve().parents[3]
DATA = REPO / "data"
OUT = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO / "scripts"))
from canonical_gt import g_t as _canonical_gt  # noqa: E402  read-only import

# ── PRE-REGISTERED ────────────────────────────────────────────────────────
WINDOW = (5, 6, 7, 8, 9)
HORIZON = 9                 # leads 0..8
P_GO, P_OK = 60, 70
MIN_GAIN = 5.0
MIN_DUR = 2
WARMUP_END = pd.Timestamp("2020-12-31 23:00")
EVAL_START = pd.Timestamp("2021-01-01 00:00")

E_GC1_MIN = 0.10
E_GC2BI_MIN_CARD = 4
E_GC2BII_MIN_UNEXPLAINED = 0.10
E_GC2BIII_TAU = 0.05
E_GC2BIII_FAR = 5.0
E_GC2BIII_MIN_SHARE = 0.50
E_GC2BIV_MAX_BASE_R2 = 0.95
E_GC3_MAX_MODAL = 0.70
E_ES5_FAR_BOUND = 0.10      # judgement, not evidence-derived
E_ES5_MIN_SHARE = 0.80
E_GE2_MARKER = 0.30
E_CA1_MIN, E_CA2_MIN, E_CA3_MIN = 120, 60, 100
MIN_CELL_N = 30

W_CAUTION, W_UNSAFE = 21.6, 27.0
R_CAUTION, R_UNSAFE = 10.0, 20.0
O_CAUTION, O_UNSAFE = 1.0, 1.25
EPS = {"wave": 0.05, "wind": 0.5, "rain": 0.5}
A_AI = {0: {"Go", "Delay", "DepartureTime", "Duration"},
        1: {"Go", "Delay"}, 2: set()}
TYPES = ["Go", "Delay", "DepartureTime", "Duration"]
VARS = ("wind", "wave", "precip")
T_PHYS = [("wave", O_CAUTION), ("wave", O_UNSAFE), ("wind", W_CAUTION),
          ("wind", W_UNSAFE), ("precip", R_CAUTION), ("precip", R_UNSAFE)]
# ──────────────────────────────────────────────────────────────────────────


def tkey(ts):
    """Canonical timestamp key. Numpy datetime64 and pandas Timestamp stringify
    differently ('...T05:00:00.000000000' vs '... 05:00:00'), which silently
    emptied L-CHK-1 and broke L-CHK-4 on the first run. One formatter only."""
    return pd.Timestamp(ts).isoformat()


class FutureAccessError(RuntimeError):
    pass


class CausalView:
    """Hard-enforces L-CHK-2 and L-CHK-8: raises on any read after the episode."""

    def __init__(self, arr, times, episode_idx):
        self._a, self._t, self._e = arr, times, episode_idx
        self.max_idx_read = -1

    def at(self, i):
        if i > self._e:
            raise FutureAccessError(
                f"read index {i} ({self._t[i]}) after episode {self._t[self._e]}")
        self.max_idx_read = max(self.max_idx_read, i)
        return self._a[i]


class FullView:
    """G-L only. Unrestricted — this IS the leak, made explicit in the type."""

    def __init__(self, arr, times, episode_idx):
        self._a, self._t, self._e = arr, times, episode_idx
        self.max_idx_read = -1

    def at(self, i):
        self.max_idx_read = max(self.max_idx_read, i)
        return self._a[i]


def load():
    w = pd.read_csv(DATA / "raw_weather_sea.csv", skiprows=3)
    m = pd.read_csv(DATA / "raw_marine_era5_sea.csv", skiprows=3)
    w["time"] = pd.to_datetime(w["time"])
    m["time"] = pd.to_datetime(m["time"])
    j = w.merge(m, on="time", how="inner").dropna(
        subset=["wind_speed_10m (kn)", "wave_height (m)", "precipitation (mm)"])
    d = pd.DataFrame({
        "time": j["time"].values,
        "wind": j["wind_speed_10m (kn)"].values,
        "wmo": j["weather_code (wmo code)"].values,
        "wave": j["wave_height (m)"].values,
        "precip": j["precipitation (mm)"].values,
    }).reset_index(drop=True)
    d["time"] = pd.to_datetime(d["time"])
    d["hour"] = d["time"].dt.hour
    d["month"] = d["time"].dt.month
    d["year"] = d["time"].dt.year
    d["epoch"] = d["time"].dt.to_period("M").astype(str)
    return d


# ── architecture side (read-only reproduction, evaluator only) ───────────
def classify(d):
    gw = np.where(d["wind"] > W_UNSAFE, 2, np.where(d["wind"] > W_CAUTION, 1, 0))
    gr = np.where((d["precip"] > R_UNSAFE) | d["wmo"].isin([95, 96, 99]), 2,
                  np.where(d["precip"] > R_CAUTION, 1, 0))
    go = np.where(d["wave"] < O_CAUTION, 0, np.where(d["wave"] <= O_UNSAFE, 1, 2))
    gt = np.asarray(_canonical_gt(d["time"], d["hour"]))
    gm = np.zeros(len(d), dtype=int)
    return np.max(np.vstack([gw, gr, go, gt, gm]), axis=0), gt


# ── calibration ─────────────────────────────────────────────────────────
def build_calibration(d, causal=True):
    """Per-epoch constants. causal=True -> prior data only (strictly before the
    epoch start). causal=False -> whole record (the G-L leak, L1/L2)."""
    cal = {}
    epochs = sorted(d.loc[d["time"] >= EVAL_START, "epoch"].unique())
    for ep in epochs:
        ep_start = pd.Period(ep).start_time
        src = d[d["time"] < ep_start] if causal else d
        c = {"src_max_time": str(src["time"].max()), "n_src": int(len(src))}
        for v in VARS:
            c[f"ecdf_{v}"] = np.sort(src[v].values)
        # exposure of prior window hours, through this epoch's own ECDFs
        sw = src[src["hour"].isin(WINDOW)]
        e_src = np.mean([pct(c[f"ecdf_{v}"], sw[v].values) for v in VARS], axis=0)
        c["e_go"] = float(np.percentile(e_src, P_GO))
        c["e_ok"] = float(np.percentile(e_src, P_OK))
        # climatology: prior years, same calendar month, by hour
        mth = int(pd.Period(ep).month)
        prior_m = src[src["month"] == mth]
        for v in VARS:
            cl = {}
            for hh in range(min(WINDOW), max(WINDOW) + HORIZON):
                s = prior_m[prior_m["hour"] == hh][v]
                cl[hh] = (float(s.mean()) if len(s) else
                          (float(prior_m[v].mean()) if len(prior_m)
                           else float(src[v].mean())))
            c[f"clim_{v}"] = cl
        # alpha_k by variable and lead, fitted on prior window-hour pairs.
        # Vectorised: clim looked up through a 24-slot array indexed by hour.
        hours_all = d["hour"].values
        n_all = len(d)
        i0_base = src.index.values[np.isin(src["hour"].values, WINDOW)]
        for v in VARS:
            vals_all = d[v].values
            clim_arr = np.full(24, np.nan)
            for hh, vv in c[f"clim_{v}"].items():
                clim_arr[hh] = vv
            a = {}
            for k in range(1, HORIZON):
                i0 = i0_base
                i1 = i0 + k
                keep = i1 < n_all
                i0, i1 = i0[keep], i1[keep]
                if len(i0) < 50:
                    a[k] = 1.0
                    continue
                cm = clim_arr[hours_all[i1]]
                good = ~np.isnan(cm)
                x = vals_all[i0][good] - cm[good]
                y = vals_all[i1][good] - cm[good]
                den = float(np.sum(x * x))
                a[k] = float(np.clip(np.sum(x * y) / den, 0.0, 1.0)) if den > 0 else 1.0
            c[f"alpha_{v}"] = a
        cal[ep] = c
    return cal


def pct(sorted_src, vals):
    """Empirical percentile rank of vals within sorted_src."""
    return np.searchsorted(sorted_src, vals, side="right") / max(len(sorted_src), 1) * 100.0


# ── generators ──────────────────────────────────────────────────────────
def forecast(cond, views, idx, hours, cal_ep, alpha_one=False):
    """Return {lead: {var: value}} for leads 0..HORIZON-1."""
    out = {}
    for k in range(HORIZON):
        j = idx + k
        if j >= len(hours):
            break
        vals = {}
        for v in VARS:
            if k == 0:
                vals[v] = views[v].at(j)                      # observed at h
            elif cond == "G-L":
                vals[v] = views[v].at(j)                      # L3: realised future
            elif cond == "G-A":
                vals[v] = views[v].at(idx)                    # persistence
            else:
                a = 1.0 if alpha_one else cal_ep[f"alpha_{v}"][k]
                cl = cal_ep[f"clim_{v}"][int(hours[j])]
                vals[v] = a * views[v].at(idx) + (1 - a) * cl
        out[k] = vals
    return out


def advise(fc, cal_ep, hour):
    """Advice set + numeric run length + margins, from the forecast only."""
    def expo(vals):
        return float(np.mean([pct(cal_ep[f"ecdf_{v}"], np.array([vals[v]]))[0]
                              for v in VARS]))
    e = {k: expo(v) for k, v in fc.items()}
    e_go, e_ok = cal_ep["e_go"], cal_ep["e_ok"]
    s = {"Go" if e[0] <= e_go else "Delay"}
    # DepartureTime — a strictly better later hour inside the same window
    best = None
    for k, ek in e.items():
        if k == 0 or hour + k > max(WINDOW):
            continue
        if ek <= e_ok and e[0] - ek >= MIN_GAIN and (best is None or ek < e[best]):
            best = k
    if best is not None:
        s.add("DepartureTime")
    # Duration — consecutive workable forward hours from this departure
    run = 0
    for k in range(len(e)):
        if k not in e or e[k] > e_ok:
            break
        run += 1
    if run >= MIN_DUR:
        s.add("Duration")
    return s, run, e[0] - e_go, e[0] - e_ok, e, best


def generate(d, cond, cal, episodes, alpha_one=False, record=None):
    rec = record if record is not None else d
    hours = rec["hour"].values
    times = rec["time"].values
    arrs = {v: rec[v].values for v in VARS}
    View = FullView if cond == "G-L" else CausalView
    rows = []
    for i in episodes:
        ep = rec.at[i, "epoch"]
        if ep not in cal:
            continue
        cal_ep = cal[ep]
        # G-L must see the whole record; G-A/G-B are hard-limited to <= i,
        # except lead 0 which IS the episode hour.
        views = {v: View(arrs[v], times, i) for v in VARS}
        fc = forecast(cond, views, i, hours, cal_ep, alpha_one)
        s, run, m_go, m_ok, e, best = advise(fc, cal_ep, int(hours[i]))
        rows.append({
            "idx": i, "time": tkey(times[i]), "hour": int(hours[i]),
            "epoch": ep, "C0": "|".join(sorted(s)), "run": run,
            "m_go": m_go, "m_ok": m_ok, "e0": e[0],
            "fc": {k: {v: float(fc[k][v]) for v in VARS} for k in fc},
            "dt_target": (int(hours[i]) + best) if best is not None else None,
        })
    return pd.DataFrame(rows)


# ── leakage checks ──────────────────────────────────────────────────────
def _advice_only(df):
    return df.set_index("time")["C0"].to_dict()


def leak_checks(d, episodes_all):
    res = {}
    cal_c = build_calibration(d, causal=True)
    cal_l = build_calibration(d, causal=False)

    # L-CHK-5 calibration provenance
    bad = [ep for ep, c in cal_c.items()
           if pd.Timestamp(c["src_max_time"]) >= pd.Period(ep).start_time]
    res["L-CHK-5_calibration_provenance"] = {
        "epochs": len(cal_c), "violations": len(bad),
        "PASS": len(bad) == 0}

    # L-CHK-1 chronological truncation invariance (cut at 2022-12-31)
    cut = pd.Timestamp("2022-12-31 23:00")
    dt = d[d["time"] <= cut].reset_index(drop=True)
    sub = [i for i in episodes_all if d.at[i, "time"] <= cut]
    sub_t = set(tkey(d.at[i, "time"]) for i in sub)
    dt_eps = [i for i in dt.index if dt.at[i, "hour"] in WINDOW
              and dt.at[i, "time"] >= EVAL_START]
    out = {}
    for cond in ("G-L", "G-A", "G-B"):
        cal_full = cal_l if cond == "G-L" else cal_c
        cal_trunc = (build_calibration(dt, causal=False) if cond == "G-L"
                     else build_calibration(dt, causal=True))
        a_full = _advice_only(generate(d, cond, cal_full, sub))
        a_tr = _advice_only(generate(dt, cond, cal_trunc, dt_eps, record=dt))
        common = [t for t in a_tr if t in a_full and t in sub_t]
        diff = sum(1 for t in common if a_full[t] != a_tr[t])
        out[cond] = {"compared": len(common), "differing": diff,
                     "PASS": bool(len(common) > 0 and diff == 0),
                     "VACUOUS": len(common) == 0}
    res["L-CHK-1_truncation_invariance"] = out

    # L-CHK-3 future-shuffle invariance (shuffle everything after 2023-12-31)
    rng = np.random.default_rng(20261117)
    ds = d.copy()
    tail = ds["time"] > pd.Timestamp("2023-12-31 23:00")
    for v in VARS:
        vals = ds.loc[tail, v].values.copy()
        rng.shuffle(vals)
        ds.loc[tail, v] = vals
    pre = [i for i in episodes_all if d.at[i, "time"] <= pd.Timestamp("2023-12-31 23:00")]
    out = {}
    for cond in ("G-L", "G-A", "G-B"):
        c0 = cal_l if cond == "G-L" else cal_c
        c1 = (build_calibration(ds, causal=False) if cond == "G-L"
              else build_calibration(ds, causal=True))
        a0 = _advice_only(generate(d, cond, c0, pre))
        a1 = _advice_only(generate(ds, cond, c1, pre, record=ds))
        diff = sum(1 for t in a0 if a0[t] != a1.get(t))
        out[cond] = {"compared": len(a0), "differing": diff,
                     "PASS": bool(len(a0) > 0 and diff == 0),
                     "VACUOUS": len(a0) == 0}
    res["L-CHK-3_future_shuffle"] = out

    # L-CHK-4 placebo-future (NaN out everything after each episode) — sampled
    samp = list(rng.choice(episodes_all, size=200, replace=False))
    out = {}
    for cond in ("G-L", "G-A", "G-B"):
        c = cal_l if cond == "G-L" else cal_c
        base = _advice_only(generate(d, cond, c, samp))
        ok = True
        errs = 0
        for i in samp[:60]:
            dp = d.copy()
            dp.loc[dp.index > i, list(VARS)] = np.nan
            try:
                g = generate(dp, cond, c, [int(i)], record=dp)
                if g.empty or g.at[0, "C0"] != base[tkey(d.at[int(i), "time"])]:
                    errs += 1
            except Exception as ex:
                errs += 1
                if out.get("_first_err") is None:
                    out["_first_err"] = f"{cond}: {type(ex).__name__}: {ex}"
        out[cond] = {"sampled": 60, "changed_or_failed": errs,
                     "PASS": errs == 0}
        if errs:
            ok = False
    res["L-CHK-4_placebo_future"] = out

    # L-CHK-7 alpha==1 identity: G-B with alpha forced to 1 == G-A
    a_a = _advice_only(generate(d, "G-A", cal_c, episodes_all))
    a_b1 = _advice_only(generate(d, "G-B", cal_c, episodes_all, alpha_one=True))
    diff = sum(1 for t in a_a if a_a[t] != a_b1.get(t))
    res["L-CHK-7_alpha_one_identity"] = {
        "compared": len(a_a), "differing": diff, "PASS": diff == 0}

    # L-CHK-2 / L-CHK-8 enforced by type: CausalView raises on future access
    probe = {}
    for cond in ("G-A", "G-B"):
        try:
            generate(d, cond, cal_c, episodes_all[:500])
            probe[cond] = "no FutureAccessError raised — causal view held"
        except FutureAccessError as e:
            probe[cond] = f"VIOLATION: {e}"
    res["L-CHK-2_8_causal_view"] = {
        "mechanism": "G-A/G-B receive CausalView, which raises on any read "
                     "with index > episode; G-L receives FullView by design",
        "probe": probe,
        "PASS": all("VIOLATION" not in v for v in probe.values())}

    res["GATES_PASS_for_causal_conditions"] = bool(
        res["L-CHK-5_calibration_provenance"]["PASS"]
        and res["L-CHK-1_truncation_invariance"]["G-A"]["PASS"]
        and res["L-CHK-1_truncation_invariance"]["G-B"]["PASS"]
        and res["L-CHK-3_future_shuffle"]["G-A"]["PASS"]
        and res["L-CHK-3_future_shuffle"]["G-B"]["PASS"]
        and res["L-CHK-4_placebo_future"]["G-A"]["PASS"]
        and res["L-CHK-4_placebo_future"]["G-B"]["PASS"]
        and res["L-CHK-7_alpha_one_identity"]["PASS"]
        and res["L-CHK-2_8_causal_view"]["PASS"])
    res["note_G-L_expected_to_fail"] = (
        "G-L is the leaky baseline. Its failures on L-CHK-1/3/4 are the "
        "intended demonstration that the checks detect leakage, not defects.")
    return res, cal_c, cal_l
