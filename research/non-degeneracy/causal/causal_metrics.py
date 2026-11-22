#!/usr/bin/env python3
"""
Evaluator for the R3 causal replication. SEPARATE MODULE from the generator,
per L-CHK-8: this is the only place post-episode data may be read, and it is
never passed back into advice generation.
"""
import numpy as np
import pandas as pd

from causal_replication import (
    VARS, TYPES, WINDOW, HORIZON, A_AI, T_PHYS, pct, EPS,
    O_CAUTION, O_UNSAFE, W_CAUTION, W_UNSAFE, R_CAUTION, R_UNSAFE,
    E_GC1_MIN, E_GC2BI_MIN_CARD, E_GC2BII_MIN_UNEXPLAINED, E_GC2BIII_TAU,
    E_GC2BIII_FAR, E_GC2BIII_MIN_SHARE, E_GC2BIV_MAX_BASE_R2, E_GC3_MAX_MODAL,
    E_ES5_FAR_BOUND, E_ES5_MIN_SHARE, E_GE2_MARKER,
    E_CA1_MIN, E_CA2_MIN, E_CA3_MIN, MIN_CELL_N,
)


def has(series, t):
    return series.str.split("|").apply(lambda s: t in s)


# ── GC ──────────────────────────────────────────────────────────────────
def gc(df):
    n = len(df)
    shares = {t: float(has(df["C0"], t).mean()) for t in TYPES}
    out = {"n_episodes": n,
           "E-GC-1_type_share": {k: round(v, 4) for k, v in shares.items()},
           "E-GC-1_threshold": E_GC1_MIN,
           "E-GC-1_PASS": all(v >= E_GC1_MIN for v in shares.values()),
           "E-GC-1_failing_types": [k for k, v in shares.items()
                                    if v < E_GC1_MIN]}

    run = df["run"].values
    m = df["m_ok"].values

    # b-i cardinality of predicted run lengths
    card = sorted(set(int(x) for x in run))
    out["E-GC-2b-i_distinct_run_values"] = card
    out["E-GC-2b-i_cardinality"] = len(card)
    out["E-GC-2b-i_threshold"] = E_GC2BI_MIN_CARD
    out["E-GC-2b-i_PASS"] = len(card) >= E_GC2BI_MIN_CARD

    # b-ii step conformity against the EPISODE-SPECIFIC margin m_ok
    pred = np.where(m <= 0, HORIZON, 0)
    unexp = float(np.mean(pred != run))
    out["E-GC-2b-ii_step_unexplained_share"] = round(unexp, 6)
    out["E-GC-2b-ii_threshold"] = E_GC2BII_MIN_UNEXPLAINED
    out["E-GC-2b-ii_PASS"] = unexp >= E_GC2BII_MIN_UNEXPLAINED

    # b-iii near-tie discordance by distance from the margin breakpoint m=0
    o = np.argsort(m)
    ms, rs = m[o], run[o]
    disc = [(abs(ms[i]), abs(ms[i + 1]))
            for i in range(len(ms) - 1)
            if abs(ms[i + 1] - ms[i]) < E_GC2BIII_TAU and rs[i] != rs[i + 1]]
    far = sum(1 for a, b in disc if min(a, b) > E_GC2BIII_FAR)
    out["E-GC-2b-iii_discordant_near_tie_pairs"] = len(disc)
    out["E-GC-2b-iii_share_far_from_breakpoint"] = (
        round(far / len(disc), 4) if disc else None)
    out["E-GC-2b-iii_threshold"] = E_GC2BIII_MIN_SHARE
    out["E-GC-2b-iii_PASS"] = bool(
        disc and far / len(disc) >= E_GC2BIII_MIN_SHARE)

    # b-iv residual information from calendar, over the step baseline
    sstot = float(np.sum((run - run.mean()) ** 2))
    ssres = float(np.sum((run - pred) ** 2))
    base_r2 = 1.0 - ssres / sstot if sstot > 0 else 1.0
    resid = run - pred
    g = pd.DataFrame({"r": resid, "mo": df["month"].values,
                      "hr": df["hour"].values}).groupby(["mo", "hr"])["r"]
    gm = g.transform("mean").values
    expl = (1.0 - float(np.sum((resid - gm) ** 2)) / ssres) if ssres > 0 else 0.0
    out["E-GC-2b-iv_base_R2_step_on_margin"] = round(base_r2, 6)
    out["E-GC-2b-iv_calendar_share_of_residual"] = round(expl, 6)
    out["E-GC-2b-iv_threshold_base_R2_below"] = E_GC2BIV_MAX_BASE_R2
    out["E-GC-2b-iv_PASS"] = bool(base_r2 < E_GC2BIV_MAX_BASE_R2 and expl > 0)

    # E-GC-3 modal DepartureTime target, within hour-of-window strata
    strat = {}
    for h in WINDOW:
        s = df[(df["hour"] == h) & df["dt_target"].notna()]
        if len(s) == 0:
            strat[h] = {"n": 0}
            continue
        vc = s["dt_target"].value_counts(normalize=True)
        strat[h] = {"n": int(len(s)), "modal_target": int(vc.index[0]),
                    "modal_share": round(float(vc.iloc[0]), 4),
                    "distinct_targets": int(s["dt_target"].nunique())}
    out["E-GC-3_by_hour"] = strat
    p = strat.get(5, {})
    out["E-GC-3_threshold_modal_share_max"] = E_GC3_MAX_MODAL
    out["E-GC-3_PASS_at_0500"] = (
        bool(p.get("n", 0) > 0 and p["modal_share"] <= E_GC3_MAX_MODAL)
        if p.get("n", 0) > 0 else None)

    # E-GC-4 descriptive: type rates by hour-of-window
    out["E-GC-4_type_share_by_hour"] = {
        int(h): {t: round(float(has(df[df["hour"] == h]["C0"], t).mean()), 4)
                 for t in TYPES} for h in WINDOW}
    return out


# ── ES ──────────────────────────────────────────────────────────────────
def es(df, d, cal, cond):
    out = {"condition": cond}
    rows_int, rows_phys = [], []
    for _, r in df.iterrows():
        i, ep = int(r["idx"]), r["epoch"]
        c = cal[ep]
        e_ok = c["e_ok"]
        for k, f in r["fc"].items():
            k = int(k)
            j = i + k
            if j >= len(d):
                continue
            obs = {v: float(d.at[j, v]) for v in VARS}
            e_pred = float(np.mean([pct(c[f"ecdf_{v}"], np.array([f[v]]))[0]
                                    for v in VARS]))
            e_obs = float(np.mean([pct(c[f"ecdf_{v}"], np.array([obs[v]]))[0]
                                   for v in VARS]))
            rows_int.append({"lead": k, "pred_ok": e_pred <= e_ok,
                             "obs_ok": e_obs <= e_ok})
            for v, thr in T_PHYS:
                rows_phys.append({"lead": k, "var": v, "thr": thr,
                                  "pred_ok": f[v] <= thr,
                                  "obs_ok": obs[v] <= thr})
    ti = pd.DataFrame(rows_int)
    tp = pd.DataFrame(rows_phys)

    def contingency(g):
        n = len(g)
        pa = g["pred_ok"]
        oa = g["obs_ok"]
        n_pa = int(pa.sum())
        n_pr = int((~pa).sum())
        far = float((pa & ~oa).sum() / n_pa) if n_pa >= MIN_CELL_N else None
        frr = float((~pa & oa).sum() / n_pr) if n_pr >= MIN_CELL_N else None
        n_oe = int((~oa).sum())
        pod = float((~pa & ~oa).sum() / n_oe) if n_oe >= MIN_CELL_N else None
        return {"n": n, "n_pred_ok": n_pa, "n_obs_exceed": n_oe,
                "base_rate_exceed": round(float((~oa).mean()), 5),
                "FAR_acc": None if far is None else round(far, 5),
                "FRR": None if frr is None else round(frr, 5),
                "POD": None if pod is None else round(pod, 5),
                "insufficient_n": far is None or frr is None or pod is None}

    out["E-ES-1-4_T-INT_by_lead"] = {
        int(k): contingency(g) for k, g in ti.groupby("lead")}
    out["E-ES-1-4_T-PHYS_by_threshold_and_lead"] = {
        f"{v}>{t}": {int(k): contingency(gg)
                     for k, gg in g.groupby("lead")}
        for (v, t), g in tp.groupby(["var", "thr"])}

    # E-ES-5 share of forecast-dependent advice at leads with acceptable FAR_acc
    wave1 = out["E-ES-1-4_T-PHYS_by_threshold_and_lead"].get(
        f"wave>{O_CAUTION}", {})
    good = {k for k, c in wave1.items()
            if c["FAR_acc"] is not None and c["FAR_acc"] <= E_ES5_FAR_BOUND}
    fd = df[has(df["C0"], "DepartureTime") | has(df["C0"], "Duration")]
    if len(fd) == 0:
        share = None
    else:
        tot = ok = 0
        for _, r in fd.iterrows():
            leads = []
            if "DepartureTime" in r["C0"] and r["dt_target"] is not None:
                leads.append(int(r["dt_target"]) - int(r["hour"]))
            if "Duration" in r["C0"]:
                leads.extend(range(1, int(r["run"])))
            for L in leads:
                tot += 1
                ok += int(L in good)
        share = (ok / tot) if tot else None
    out["E-ES-5_leads_with_FAR_acc_le_bound"] = sorted(good)
    out["E-ES-5_share_advice_at_those_leads"] = (
        None if share is None else round(share, 5))
    out["E-ES-5_bound_is_a_judgement_not_evidence"] = E_ES5_FAR_BOUND
    out["E-ES-5_threshold"] = E_ES5_MIN_SHARE
    out["E-ES-5_PASS"] = (None if share is None
                          else bool(share >= E_ES5_MIN_SHARE))

    # E-ES-6 reliability of "predicted acceptable", T-INT, pooled over leads>=1
    sub = ti[ti["lead"] >= 1]
    out["E-ES-6_reliability_pred_ok"] = (
        round(float(sub[sub["pred_ok"]]["obs_ok"].mean()), 5)
        if int(sub["pred_ok"].sum()) >= MIN_CELL_N else None)
    return out


def es8(df, d, cal, S, gt):
    """Index-state concordance. Observed values only; no forecasting."""
    def block(mask, label):
        idx = df["idx"].values[mask]
        if len(idx) == 0:
            return {"label": label, "n": 0}
        acc, s_, drv = [], [], []
        for i in idx:
            c = cal[d.at[i, "epoch"]]
            e = float(np.mean([pct(c[f"ecdf_{v}"], np.array([float(d.at[i, v])]))[0]
                               for v in VARS]))
            acc.append(e <= c["e_ok"])
            s_.append(int(S[i]))
            if S[i] > 0:
                gw = 2 if d.at[i, "wind"] > W_UNSAFE else (1 if d.at[i, "wind"] > W_CAUTION else 0)
                gr = 2 if (d.at[i, "precip"] > R_UNSAFE or d.at[i, "wmo"] in (95, 96, 99)) else (1 if d.at[i, "precip"] > R_CAUTION else 0)
                go = 0 if d.at[i, "wave"] < O_CAUTION else (1 if d.at[i, "wave"] <= O_UNSAFE else 2)
                comp = {"wind": gw, "rain": gr, "wave": go, "time": int(gt[i])}
                mx = max(comp.values())
                drv.append("+".join(sorted(k for k, v in comp.items() if v == mx)))
        acc = np.array(acc)
        s_ = np.array(s_)
        nz = s_ > 0
        return {
            "label": label, "n": int(len(idx)),
            "n_S_elevated": int(nz.sum()), "n_S_safe": int((~nz).sum()),
            "E-ES-8a_permissive_mismatch": (
                round(float(acc[nz].mean()), 5) if nz.sum() >= MIN_CELL_N else None),
            "E-ES-8b_restrictive_mismatch": (
                round(float((~acc[~nz]).mean()), 5)
                if (~nz).sum() >= MIN_CELL_N else None),
            "E-ES-8c_driver_of_elevated_state": (
                pd.Series(drv).value_counts(normalize=True).round(4).to_dict()
                if drv else {}),
        }
    allm = np.ones(len(df), dtype=bool)
    dayl = np.array([gt[i] == 0 for i in df["idx"].values])
    return {"all_cases": block(allm, "all cases"),
            "daylight_only": block(dayl, "daylight only (g_t = SAFE)")}


# ── GE and CA ───────────────────────────────────────────────────────────
def ge_ca(df, d, S, gt):
    s = np.array([int(S[i]) for i in df["idx"].values])
    c0 = [set(x.split("|")) if x else set() for x in df["C0"]]
    c1 = [set() if st == 2 else set(a) for a, st in zip(c0, s)]
    c2 = [a & A_AI[st] for a, st in zip(c0, s)]
    ne = np.array([a != b for a, b in zip(c1, c2)])
    caution = s == 1
    n = len(df)
    out = {
        "n_episodes": n,
        "state_distribution": {"SAFE": int((s == 0).sum()),
                               "CAUTION": int(caution.sum()),
                               "UNSAFE": int((s == 2).sum())},
        "P_S_CAUTION_pct": round(100 * float(caution.mean()), 4),
        "STRUCTURAL_CEILING_note": (
            "C1 and C2 differ only at CAUTION, so unstratified divergence "
            "cannot exceed P(S = CAUTION). No pass/fail is set on it."),
        "E-GE-1_divergence_all_cases": round(float(ne.mean()), 6),
        "E-GE-1_divergence_caution_pool": (
            round(float(ne[caution].mean()), 6) if caution.sum() else None),
        "E-GE-1_treatment": "descriptive, no gate",
    }
    wr = np.array([("DepartureTime" in a) or ("Duration" in a) for a in c0])
    out["E-GE-2_withheld_realised_in_CAUTION"] = (
        round(float(wr[caution].mean()), 6) if caution.sum() else None)
    out["E-GE-2_adequacy_marker"] = E_GE2_MARKER
    out["E-GE-2_MEETS_MARKER"] = (
        bool(caution.sum() and wr[caution].mean() >= E_GE2_MARKER))

    bit1 = [a & {"Go", "Delay"} for a in c1]
    bit2 = [a & {"Go", "Delay"} for a in c2]
    out["E-GE-3a_go_delay_bit_identical_share"] = round(
        float(np.mean([x == y for x, y in zip(bit1, bit2)])), 6)
    dv = [i for i in range(n) if ne[i]]
    out["E-GE-3b_divergences_solely_withheld_forecast_types"] = (
        round(float(np.mean([(c1[i] - c2[i]) <= {"DepartureTime", "Duration"}
                             for i in dv])), 6) if dv else None)

    wave = np.array([float(d.at[i, "wave"]) for i in df["idx"].values])
    wind = np.array([float(d.at[i, "wind"]) for i in df["idx"].values])
    rain = np.array([float(d.at[i, "precip"]) for i in df["idx"].values])
    b = (np.abs(wave - O_CAUTION) <= EPS["wave"]) | (np.abs(wave - O_UNSAFE) <= EPS["wave"]) \
        | (np.abs(wind - W_CAUTION) <= EPS["wind"]) | (np.abs(wind - W_UNSAFE) <= EPS["wind"]) \
        | (np.abs(rain - R_CAUTION) <= EPS["rain"]) | (np.abs(rain - R_UNSAFE) <= EPS["rain"])
    ca = {
        "E-CA-1_boundary_cases": int(b.sum()), "E-CA-1_min": E_CA1_MIN,
        "E-CA-1_PASS": bool(b.sum() >= E_CA1_MIN),
        "E-CA-2_caution_and_boundary": int((b & caution).sum()),
        "E-CA-2_min": E_CA2_MIN,
        "E-CA-2_PASS": bool((b & caution).sum() >= E_CA2_MIN),
        "E-CA-3_C1_ne_C2_cases": int(ne.sum()), "E-CA-3_min": E_CA3_MIN,
        "E-CA-3_PASS": bool(ne.sum() >= E_CA3_MIN),
        "boundary_by_component": {
            "wave": int(((np.abs(wave - O_CAUTION) <= EPS["wave"]) | (np.abs(wave - O_UNSAFE) <= EPS["wave"])).sum()),
            "wind": int(((np.abs(wind - W_CAUTION) <= EPS["wind"]) | (np.abs(wind - W_UNSAFE) <= EPS["wind"])).sum()),
            "rain": int(((np.abs(rain - R_CAUTION) <= EPS["rain"]) | (np.abs(rain - R_UNSAFE) <= EPS["rain"])).sum()),
        },
    }
    return out, ca
