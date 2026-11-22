#!/usr/bin/env python3
"""
A18.1 Step 4 — PATH B: independent numerical reproduction.

Standard library only (csv, hashlib, json, datetime). Does NOT import pandas,
numpy, or any original script. The classification contract comes from the
Step 3 reference implementation, which was itself transcribed from source with
line citations and is NOT a wrapper around the original code.

READ-ONLY on every original path. All output goes to this directory.
"""
import csv, hashlib, importlib.util, json, sys
from collections import Counter
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
DATA = ROOT / "data"
STEP3 = ROOT / "research_audits" / "A18_1_step3_20261121"
sys.dont_write_bytecode = True

_s = importlib.util.spec_from_file_location("ref", STEP3 / "08_reconstruction_reference.py")
R = importlib.util.module_from_spec(_s); _s.loader.exec_module(R)
SAFE, CAUTION, UNSAFE = R.SAFE, R.CAUTION, R.UNSAFE

CONFIGS = {"PRIMARY": "raw_marine_era5_sea.csv", "RESOLUTION": "raw_marine_mfwam.csv"}
# scripts/sensitivity/threshold_sensitivity.py:19
CANON = dict(W_C=21.6, W_U=27.0, R_C=10.0, R_U=20.0, O_C=1.0, O_U=1.25)
META_ROWS = 3   # pandas skiprows=3 equivalent


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for c in iter(lambda: fh.read(1 << 20), b""): h.update(c)
    return h.hexdigest()


def read_om(path):
    with open(path, newline="", encoding="utf-8") as fh:
        body = fh.read().splitlines()[META_ROWS:]
    return list(csv.DictReader(body))


def num(v):
    v = (v or "").strip()
    if v == "" or v.upper() in ("NAN", "NA", "NULL"): return None
    try: return float(v)
    except ValueError: return None


def load(marine_file):
    """Reproduces condition_comparison.py:135-150 / threshold_sensitivity.py:22-31
    with stdlib: inner join on `time`, then drop rows missing wave, wind or
    precip. Returns (rows, reject_reasons)."""
    w = read_om(DATA / "raw_weather_sea.csv")
    m = {r["time"]: r for r in read_om(DATA / marine_file)}
    rows, rej = [], Counter()
    for r in w:
        t = r["time"]
        mm = m.get(t)
        if mm is None:
            rej["no_wave_row_for_timestamp(inner join)"] += 1
            continue
        wind, precip, wave = num(r["wind_speed_10m (kn)"]), num(r["precipitation (mm)"]), num(mm["wave_height (m)"])
        wmo = num(r["weather_code (wmo code)"])
        if wave is None:
            rej["null wave_height (m)"] += 1; continue
        if wind is None:
            rej["null wind_speed_10m (kn)"] += 1; continue
        if precip is None:
            rej["null precipitation (mm)"] += 1; continue
        ts = datetime.strptime(t, "%Y-%m-%dT%H:%M")
        rows.append(dict(time=t, date=ts.date(), hour=ts.hour, wind=wind,
                         precip=precip, wmo=int(wmo) if wmo is not None else -1, wave=wave))
    rows.sort(key=lambda r: r["time"])
    return rows, rej


def comp(r, p, vessel_band=None):
    """Component states under a parameter set. Operators transcribed from
    threshold_sensitivity.py:34-40 (identical to condition_comparison.py:160-166)."""
    w = r["wind"]
    g_w = UNSAFE if w > p["W_U"] else (CAUTION if w > p["W_C"] else SAFE)
    storm = r["precip"] > p["R_U"] or r["wmo"] in (95, 96, 99)
    g_r = UNSAFE if storm else (CAUTION if r["precip"] > p["R_C"] else SAFE)
    oc, ou = (p["O_C"], p["O_U"]) if vessel_band is None else vessel_band
    o = r["wave"]
    g_o = UNSAFE if o > ou else (CAUTION if o >= oc else SAFE)
    g_t = R.g_t(r["date"], r["hour"])
    return dict(g_w=g_w, g_r=g_r, g_m=SAFE, g_o=g_o, g_t=g_t)


def state(r, p, vessel_band=None):
    return max(comp(r, p, vessel_band).values())


def dep(r):
    return 5 <= r["hour"] <= 9     # historical_replay.py:238, five slots


# =============================== E1 immutability
INPUTS = ["data/raw_weather_sea.csv", "data/raw_marine_era5_sea.csv",
          "data/raw_marine_mfwam.csv", "data/solar/solar-events-daily.csv",
          "data/prediction-register.csv", "scripts/condition_comparison.py",
          "scripts/historical_replay.py", "scripts/canonical_gt.py",
          "scripts/sensitivity/threshold_sensitivity.py"]
BEFORE = {p: sha(ROOT / p) for p in INPUTS}

# =============================== E2 population reconciliation
pop, occ, decomp, pol, sens, par = [], [], [], [], [], []
LOADED, STATES = {}, {}
n = 0
for cfg, mf in CONFIGS.items():
    rows, rej = load(mf)
    w_all = read_om(DATA / "raw_weather_sea.csv")
    m_all = read_om(DATA / mf)
    d = [r for r in rows if dep(r)]
    LOADED[cfg] = rows
    nulls = sum(1 for r in m_all if num(r["wave_height (m)"]) is None)
    null_ts = [r["time"] for r in m_all if num(r["wave_height (m)"]) is None]
    null_dep = [t for t in null_ts if 5 <= int(t[11:13]) <= 9]
    n += 1
    pop.append(dict(
        item_id=f"POP-{n:02d}", config=cfg, source_path_or_uri=f"data/raw_weather_sea.csv + data/{mf}",
        verification_status="COMPUTED_FROM_DATA",
        evidence_reference="stdlib inner join on 'time'; dropna on wave/wind/precip "
                           "(condition_comparison.py:141-148)",
        weather_source_rows=len(w_all), wave_source_rows=len(m_all),
        inner_join_rows=len(w_all) - rej["no_wave_row_for_timestamp(inner join)"],
        rejected_no_wave_row=rej["no_wave_row_for_timestamp(inner join)"],
        rejected_null_wave=rej["null wave_height (m)"],
        rejected_null_wind=rej["null wind_speed_10m (kn)"],
        rejected_null_precip=rej["null precipitation (mm)"],
        usable_rows=len(rows), departure_window_rows=len(d),
        first_ts=rows[0]["time"], last_ts=rows[-1]["time"],
        distinct_days=len({r["date"] for r in rows}),
        wave_nulls_in_source=nulls,
        wave_null_timestamps="; ".join(null_ts) if nulls <= 15 else f"{nulls} ts",
        wave_nulls_in_departure_window=len(null_dep),
        filter_logic="inner join on time, then drop rows with null wave_height/wind_speed/precipitation",
        limitation_or_unknown="wave_period and tide are NOT used for inclusion/exclusion (Step 2 D-02, D-06)"))

    # =============================== E3 occupancy + decomposition
    for scope, sub in (("all_hours", rows), ("departure_window", d)):
        S = [state(r, CANON) for r in sub]
        C = [comp(r, CANON) for r in sub]
        if scope == "departure_window": STATES[cfg] = (sub, S, C)
        cnt = Counter(S)
        N = len(sub)
        occ.append(dict(
            item_id=f"OCC-{cfg}-{scope}", config=cfg, scope=scope,
            source_path_or_uri=f"data/raw_weather_sea.csv + data/{mf}",
            verification_status="COMPUTED_FROM_DATA",
            evidence_reference="Step 3 pure functions (08_reconstruction_reference.py), not the original summary",
            denominator=N,
            n_SAFE=cnt[SAFE], n_CAUTION=cnt[CAUTION], n_UNSAFE=cnt[UNSAFE],
            pct_SAFE=round(100*cnt[SAFE]/N, 4), pct_CAUTION=round(100*cnt[CAUTION]/N, 4),
            pct_UNSAFE=round(100*cnt[UNSAFE]/N, 4),
            checksum_counts_sum_to_denominator=(cnt[SAFE]+cnt[CAUTION]+cnt[UNSAFE] == N),
            limitation_or_unknown="g_m pinned SAFE by model assumption: every state is a LOWER BOUND "
                                  "on severity (historical_replay.py:160). NOT observed warning absence."))
        if scope != "departure_window":
            continue
        # component decomposition, departure window only
        for k in ("g_w", "g_r", "g_o", "g_t", "g_m"):
            enters_c = sum(1 for c in C if c[k] == CAUTION)
            enters_u = sum(1 for c in C if c[k] == UNSAFE)
            binds = sum(1 for c, s in zip(C, S) if s == CAUTION and c[k] == s)
            masked = sum(1 for c, s in zip(C, S) if c[k] == CAUTION and s == UNSAFE)
            sole = sum(1 for c, s in zip(C, S) if s == CAUTION and c[k] == CAUTION
                       and sum(1 for kk in C[0] if c[kk] == CAUTION) == 1)
            decomp.append(dict(
                item_id=f"DEC-{cfg}-{k}", config=cfg, component=k, denominator=len(sub),
                source_path_or_uri=f"data/raw_weather_sea.csv + data/{mf}",
                verification_status="COMPUTED_FROM_DATA",
                evidence_reference="threshold_sensitivity.py:93-99 attribution definition, recomputed independently",
                enters_CAUTION=enters_c, enters_UNSAFE=enters_u,
                is_binding_component_of_final_CAUTION=binds,
                sole_CAUTION_component=sole,
                CAUTION_masked_by_overriding_UNSAFE=masked,
                limitation_or_unknown="OVERLAPS: a CAUTION hour may have several components at CAUTION, "
                                      "so these columns do NOT sum to the CAUTION total. 'binding' means "
                                      "the component equals the final state, which can tie."))
        ties = sum(1 for c, s in zip(C, S) if s == CAUTION
                   and sum(1 for kk in c if c[kk] == CAUTION) > 1)
        decomp.append(dict(
            item_id=f"DEC-{cfg}-ties", config=cfg, component="(ties)", denominator=len(sub),
            source_path_or_uri="", verification_status="COMPUTED_FROM_DATA",
            evidence_reference="threshold_sensitivity.py:98",
            enters_CAUTION="", enters_UNSAFE="", is_binding_component_of_final_CAUTION=ties,
            sole_CAUTION_component="", CAUTION_masked_by_overriding_UNSAFE="",
            limitation_or_unknown="hours where more than one component sits at CAUTION during a final CAUTION"))

# =============================== E4 policy divergence
PAIRS = [("C0","C1"),("C0","C2"),("C0","C3"),("C1","C2"),("C1","C3"),("C2","C3")]
IDENT = {("C1","C2"): "#CAUTION/n", ("C1","C3"): "0/n",
         ("C0","C1"): "#UNSAFE/n", ("C0","C2"): "(#CAUTION+#UNSAFE)/n"}
for cfg, (sub, S, C) in STATES.items():
    N = len(S)
    cnt = Counter(S)
    for a, b in PAIRS:
        diff = sum(1 for s in S if R.A_AI[a][s] != R.A_AI[b][s])
        exp = {"#CAUTION/n": cnt[CAUTION], "0/n": 0, "#UNSAFE/n": cnt[UNSAFE],
               "(#CAUTION+#UNSAFE)/n": cnt[CAUTION]+cnt[UNSAFE]}.get(IDENT.get((a, b)))
        per_state = {R.STATE_NAME[s]: sum(1 for x in S if x == s and R.A_AI[a][x] != R.A_AI[b][x])
                     for s in (SAFE, CAUTION, UNSAFE)}
        pol.append(dict(
            item_id=f"POL-{cfg}-{a}{b}", config=cfg, pair=f"{a} vs {b}",
            source_path_or_uri="scripts/condition_comparison.py:90-105 mapping; divergence :198",
            verification_status="COMPUTED_FROM_DATA",
            evidence_reference="set inequality over paired hours, departure window",
            numerator=diff, denominator=N, percent=round(100*diff/N, 4),
            claimed_identity=IDENT.get((a, b), "(none)"),
            identity_expected_numerator="" if exp is None else exp,
            identity_holds="" if exp is None else (diff == exp),
            diverging_at_SAFE=per_state["SAFE"], diverging_at_CAUTION=per_state["CAUTION"],
            diverging_at_UNSAFE=per_state["UNSAFE"],
            limitation_or_unknown="POLICY DIVERGENCE, NOT AI proposal exclusion: the replay has no "
                                  "proposal generator, so no recommendation was ever actually withheld. "
                                  "C0 vs C1 is a participation-restriction frequency, not action accuracy."))

# =============================== E5 sensitivity
VESSEL = {"small": (1.0, 1.25), "medium": (1.4, 2.8), "big": (1.5, 3.5)}
def dl2(sub, p, band=None, mask=None):
    rs = sub if mask is None else [r for r, m in zip(sub, mask) if m]
    S = [state(r, p, band) for r in rs]
    n_ = len(S)
    c = Counter(S)
    return dict(n=n_, nCAUTION=c[CAUTION], pct=round(100*c[CAUTION]/n_, 4),
                nUNSAFE=c[UNSAFE], pctUNSAFE=round(100*c[UNSAFE]/n_, 4))

k = 0
for cfg in CONFIGS:
    rows = LOADED[cfg]
    d = [r for r in rows if dep(r)]
    def add(tag, p, band, res, note, pid):
        global k; k += 1
        sens.append(dict(item_id=f"SENS-{k:03d}", register_id=pid, config=cfg, variant=tag,
            source_path_or_uri="scripts/sensitivity/threshold_sensitivity.py",
            verification_status="COMPUTED_FROM_DATA",
            evidence_reference=note,
            W_C=p["W_C"], W_U=p["W_U"], R_C=p["R_C"], R_U=p["R_U"],
            O_C=band[0] if band else p["O_C"], O_U=band[1] if band else p["O_U"],
            operators="wind/rain strict >; wave >= O_C and > O_U",
            denominator=res["n"], n_CAUTION=res["nCAUTION"], delta_l2_pct=res["pct"],
            n_UNSAFE=res["nUNSAFE"], pct_UNSAFE=res["pctUNSAFE"]))
    add("canonical small, departure window", CANON, None, dl2(d, CANON), "line 74; A1/A39", "A1/A39")
    for v in (5.0, 7.5, 10.0, 15.0, 19.9):
        add(f"R_C={v}", dict(CANON, R_C=v), None, dl2(d, dict(CANON, R_C=v)), "lines 103-106", "A2-A6/A40-A44")
    for v in (18.0, 20.0, 21.6, 22.0, 25.0):
        add(f"W_C={v}", dict(CANON, W_C=v), None, dl2(d, dict(CANON, W_C=v)), "lines 107-110", "A7-A11/A45-A49")
    for oc, ou, tag in [(0.75,1.25,"sens -0.25 on O_C"), (1.0,1.25,"CANONICAL small"),
                        (1.25,1.5,"sens +0.25 on O_C"), (1.0,1.9,"Yaakob failure point as O_U"),
                        (1.4,2.8,"medium vessel band"), (1.5,3.5,"big vessel band")]:
        add(f"wave ({oc},{ou}) {tag}", CANON, (oc, ou), dl2(d, CANON, (oc, ou)), "lines 111-116", "A12-A17/A50-A55")
    # DEFECT FOUND AND FIXED BY THE TWO-PATH COMPARISON: my first version applied
    # the daylight mask to ALL hours (n=21,754, 9.612%). threshold_sensitivity.py:120
    # reads `m2 = m.values & dl_mask` -- the daylight mask is ANDed with the
    # DEPARTURE-WINDOW mask, so the denominator is window AND daylight.
    dl_mask = [(R.g_t(r["date"], r["hour"]) == SAFE) and dep(r) for r in rows]
    add("daylight-only denominator (window AND daylight)", CANON, None,
        dl2(rows, CANON, None, dl_mask), "line 120: m2 = m.values & dl_mask", "A18/A56")
    grid = []
    for rc in (5.0, 7.5, 10.0, 15.0, 19.9):
        for oc, ou in [(1.0,1.25),(1.0,1.9),(1.4,2.8),(1.5,3.5)]:
            p = dict(CANON, R_C=rc)
            res = dl2(d, p, (oc, ou))
            grid.append(res["pct"])
            add(f"grid R_C={rc} wave=({oc},{ou})", p, (oc, ou), res, "lines 127-134", "A19-A38/A57-A76")
    # The register's "sourced envelope" spans the SMALL-VESSEL wave configurations
    # only: (1.0,1.25) and (1.0,1.9). The (1.4,2.8) and (1.5,3.5) rows are the
    # medium and big vessel bands -- a different vessel class, so they do not
    # belong to a small-vessel envelope. Both ranges are reported below.
    small_grid = []
    for rc in (5.0, 7.5, 10.0, 15.0, 19.9):
        for oc, ou in [(1.0,1.25),(1.0,1.9)]:
            small_grid.append(dl2(d, dict(CANON, R_C=rc), (oc, ou))["pct"])
    k += 1
    sens.append(dict(item_id=f"SENS-{k:03d}", register_id="A19-A38/A57-A76 sourced envelope (small vessel)",
        config=cfg, variant="SOURCED-THRESHOLD ENVELOPE, small-vessel wave configs only",
        source_path_or_uri="scripts/sensitivity/threshold_sensitivity.py:127-134",
        verification_status="COMPUTED_FROM_DATA",
        evidence_reference="min and max over R_C x {(1.0,1.25),(1.0,1.9)} -- 10 cells",
        W_C="", W_U="", R_C="5.0-19.9", R_U=20.0, O_C="1.0", O_U="1.25-1.9",
        operators="", denominator=len(d), n_CAUTION="",
        delta_l2_pct=f"{min(small_grid):.2f}-{max(small_grid):.2f}", n_UNSAFE="", pct_UNSAFE=""))
    k += 1
    sens.append(dict(item_id=f"SENS-{k:03d}", register_id="A19-A38/A57-A76 full grid", config=cfg,
        variant="FULL 20-CELL GRID RANGE (includes medium and big vessel bands)",
        source_path_or_uri="scripts/sensitivity/threshold_sensitivity.py:127-134",
        verification_status="COMPUTED_FROM_DATA", evidence_reference="min and max of the 20 grid cells",
        W_C="", W_U="", R_C="5.0-19.9", R_U=20.0, O_C="1.0-1.5", O_U="1.25-3.5",
        operators="", denominator=len(d), n_CAUTION="",
        delta_l2_pct=f"{min(grid):.2f}-{max(grid):.2f}", n_UNSAFE="", pct_UNSAFE=""))

# common-period
common = {r["time"] for r in LOADED["PRIMARY"]} & {r["time"] for r in LOADED["RESOLUTION"]}
for cfg in CONFIGS:
    sub = [r for r in LOADED[cfg] if r["time"] in common and dep(r)]
    res = dl2(sub, CANON)
    k += 1
    sens.append(dict(item_id=f"SENS-{k:03d}", register_id="A77/A78", config=f"{cfg} wave model",
        variant="COMMON PERIOD (de-confounds wave model from record length)",
        source_path_or_uri="scripts/sensitivity/threshold_sensitivity.py:tail",
        verification_status="COMPUTED_FROM_DATA",
        evidence_reference="intersection of the two configurations' timestamps",
        W_C=CANON["W_C"], W_U=CANON["W_U"], R_C=CANON["R_C"], R_U=CANON["R_U"],
        O_C=1.0, O_U=1.25, operators="canonical", denominator=res["n"],
        n_CAUTION=res["nCAUTION"], delta_l2_pct=res["pct"],
        n_UNSAFE=res["nUNSAFE"], pct_UNSAFE=res["pctUNSAFE"]))

# =============================== write
def dump(name, data):
    if not data: return
    keys, seen = [], set()
    for r in data:
        for kk in r:
            if kk not in seen: seen.add(kk); keys.append(kk)
    with open(HERE / name, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=keys, extrasaction="ignore"); w.writeheader()
        for r in data: w.writerow(r)
    print(f"  wrote {name} ({len(data)} rows)")

dump("03_population_reconciliation.csv", pop)
dump("04_state_occupancy.csv", occ)
dump("05_component_risk_decomposition.csv", decomp)
dump("06_policy_pairwise_divergence.csv", pol)
dump("08_sensitivity_and_secondary_results.csv", sens)

AFTER = {p: sha(ROOT / p) for p in INPUTS}
unchanged = all(BEFORE[p] == AFTER[p] for p in INPUTS)
summary = dict(
    originals_unchanged=bool(unchanged),
    input_hashes=AFTER,
    populations={r["config"]: dict(usable=r["usable_rows"], window=r["departure_window_rows"]) for r in pop},
    occupancy={f"{r['config']}/{r['scope']}": dict(n=r["denominator"], SAFE=r["n_SAFE"],
               CAUTION=r["n_CAUTION"], UNSAFE=r["n_UNSAFE"], pct_CAUTION=r["pct_CAUTION"]) for r in occ},
    divergence={f"{r['config']}/{r['pair']}": dict(num=r["numerator"], den=r["denominator"],
               pct=r["percent"], identity=r["claimed_identity"], holds=r["identity_holds"]) for r in pol})
json.dump(summary, open(HERE / "_pathB_summary.json", "w"), indent=2)
print(f"\noriginals byte-unchanged: {unchanged}")
for cfg in CONFIGS:
    o = [r for r in occ if r["config"] == cfg and r["scope"] == "departure_window"][0]
    p2 = [r for r in pol if r["config"] == cfg and r["pair"] == "C1 vs C2"][0]
    p1 = [r for r in pol if r["config"] == cfg and r["pair"] == "C0 vs C1"][0]
    p0 = [r for r in pol if r["config"] == cfg and r["pair"] == "C0 vs C2"][0]
    p3 = [r for r in pol if r["config"] == cfg and r["pair"] == "C1 vs C3"][0]
    print(f"\n{cfg}  departure-window n={o['denominator']:,}")
    print(f"  SAFE {o['n_SAFE']:,} ({o['pct_SAFE']}%)  CAUTION {o['n_CAUTION']:,} ({o['pct_CAUTION']}%)  UNSAFE {o['n_UNSAFE']:,} ({o['pct_UNSAFE']}%)")
    print(f"  D(C1,C2) = {p2['numerator']:,}/{p2['denominator']:,} = {p2['percent']}%   identity {p2['identity_holds']}")
    print(f"  D(C0,C1) = {p1['numerator']:,}/{p1['denominator']:,} = {p1['percent']}%   identity {p1['identity_holds']}")
    print(f"  D(C0,C2) = {p0['numerator']:,}/{p0['denominator']:,} = {p0['percent']}%   identity {p0['identity_holds']}")
    print(f"  D(C1,C3) = {p3['numerator']:,}/{p3['denominator']:,} = {p3['percent']}%   identity {p3['identity_holds']}")
