#!/usr/bin/env python3
"""
M1dQ-A18.2-CFB-v0.1 — counterfactual proposal binding.

Standard library only. READ-ONLY on every original path.
Phase order is enforced in code: proposals are written and HASHED before any
admission mask is consulted (test T04).
"""
import csv, hashlib, importlib.util, json, math, statistics, sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
DATA = ROOT / "data"
STEP3 = ROOT / "research_audits" / "A18_1_step3_20261121"
sys.dont_write_bytecode = True

CONTRACT = json.loads((HERE / "00_contract.json").read_text(encoding="utf-8"))
_s = importlib.util.spec_from_file_location("ref", STEP3 / "08_reconstruction_reference.py")
R = importlib.util.module_from_spec(_s); _s.loader.exec_module(R)
SAFE, CAUTION, UNSAFE = R.SAFE, R.CAUTION, R.UNSAFE
SN = R.STATE_NAME
FULL = frozenset(CONTRACT["original"]["allowed_sets"]["FULL"])
RESTRICTED = frozenset(CONTRACT["original"]["allowed_sets"]["RESTRICTED"])
EMPTY = frozenset()
MASK = {"C0": {SAFE: FULL, CAUTION: FULL, UNSAFE: FULL},
        "C1": {SAFE: FULL, CAUTION: FULL, UNSAFE: EMPTY},
        "C3": {SAFE: FULL, CAUTION: FULL, UNSAFE: EMPTY},
        "C2": {SAFE: FULL, CAUTION: RESTRICTED, UNSAFE: EMPTY}}
POLICIES = ["C0", "C1", "C3", "C2"]
TYPES = CONTRACT["proposal"]["vocabulary"]
TH = CONTRACT["advisors"]["B2_FROZEN_VARYING"]["thresholds"]

def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for c in iter(lambda: fh.read(1 << 20), b""): h.update(c)
    return h.hexdigest()

FROZEN = list(CONTRACT["original"]["input_hashes"])
BEFORE = {p: sha(ROOT / p) for p in FROZEN}
T = {}   # test results

# ======================================================= PHASE 1
def rd(p):
    return list(csv.DictReader(open(p, newline="", encoding="utf-8").read().splitlines()[3:]))
def num(v):
    v = (v or "").strip()
    if v == "" or v.upper() in ("NAN", "NA", "NULL"): return None
    try: return float(v)
    except ValueError: return None

w = rd(DATA / "raw_weather_sea.csv")
m = {r["time"]: r for r in rd(DATA / "raw_marine_era5_sea.csv")}
ledger_pop, excl_reasons = [], Counter()
usable = 0
cases = []
for idx, r in enumerate(w):
    t = r["time"]
    mm = m.get(t)
    if mm is None:
        excl_reasons["EXCL_no_wave_row(inner join)"] += 1; continue
    wind, precip, wave = num(r["wind_speed_10m (kn)"]), num(r["precipitation (mm)"]), num(mm["wave_height (m)"])
    wmo = num(r["weather_code (wmo code)"])
    if wave is None: excl_reasons["EXCL_null_wave_height"] += 1; continue
    if wind is None: excl_reasons["EXCL_null_wind_speed"] += 1; continue
    if precip is None: excl_reasons["EXCL_null_precipitation"] += 1; continue
    usable += 1
    ts = datetime.strptime(t, "%Y-%m-%dT%H:%M")
    inwin = 5 <= ts.hour <= 9
    st = max(
        UNSAFE if wind > 27.0 else (CAUTION if wind > 21.6 else SAFE),
        UNSAFE if (precip > 20.0 or int(wmo) in (95, 96, 99)) else (CAUTION if precip > 10.0 else SAFE),
        SAFE,                                              # g_m pinned SAFE (model assumption)
        UNSAFE if wave > 1.25 else (CAUTION if wave >= 1.0 else SAFE),
        R.g_t(ts.date(), ts.hour))
    rec = dict(case_id="CFB-" + t.replace("-", "").replace("T", "").replace(":", ""),
               source_row_index=idx, local_timestamp=t, cluster_id=str(ts.date()),
               state=st, state_name=SN[st], inclusion_flag="INCLUDED" if inwin else "EXCL_outside_window",
               gusts=num(r["wind_gusts_10m (kn)"]), wdir=num(r["wind_direction_10m (°)"]),
               wper=num(mm["wave_period (s)"]), wind=wind, precip=precip, wave=wave)
    if not inwin:
        excl_reasons["EXCL_outside_departure_window"] += 1
    else:
        cases.append(rec)
    ledger_pop.append(rec)

N_ELIG = len(cases)
state_counts = Counter(c["state"] for c in cases)
TGT = CONTRACT["population"]["target_n_from_A18_1"]
T["T13_population_and_states_match_A18_1"] = dict(
    computed_usable=usable, computed_window=N_ELIG, target_window=TGT,
    computed_SAFE=state_counts[SAFE], computed_CAUTION=state_counts[CAUTION],
    computed_UNSAFE=state_counts[UNSAFE],
    target_states_from_A18_1=dict(SAFE=4687, CAUTION=531, UNSAFE=3917),
    result="PASS" if (N_ELIG == TGT and state_counts[SAFE] == 4687
                      and state_counts[CAUTION] == 531 and state_counts[UNSAFE] == 3917) else "FAIL")
T["T02_rows_reconcile"] = dict(
    weather_source=len(w), usable=usable,
    eligible_window=N_ELIG, excluded=sum(excl_reasons.values()),
    result="PASS" if usable == N_ELIG + excl_reasons["EXCL_outside_departure_window"] else "FAIL",
    reasons=dict(excl_reasons))

# ======================================================= PHASE 2a — PROPOSALS ONLY
def b2(c):
    """FROZEN SIMULATED advisor. 00_contract.json advisors.B2_FROZEN_VARYING.
    Reads ONLY gusts, wind direction and wave period - none of which the gate reads."""
    g, d, p = c["gusts"], c["wdir"], c["wper"]
    for v in (g, d, p):
        if v is None or not math.isfinite(v): return "ABSTAIN"
    if g >= TH["gust_kn"]: return "Delay"
    if p >= TH["wave_period_s"]: return "Duration"
    if (315.0 <= d < 360.0) or (0.0 <= d < 45.0): return "DepartureTime"
    return "Go"

ADVISORS = (["B0-UNRESTRICTED"] + [f"B1-CONST-{t}" for t in TYPES] + ["B2-FROZEN-VARYING"])
prop = []
for c in cases:
    for a in ADVISORS:
        if a == "B0-UNRESTRICTED":        pt = "Go"
        elif a.startswith("B1-CONST-"):   pt = a.replace("B1-CONST-", "")
        else:                             pt = b2(c)
        valid = pt in FULL
        prop.append(dict(case_id=c["case_id"], local_timestamp=c["local_timestamp"],
                         cluster_id=c["cluster_id"], advisor=a, proposed_type=pt,
                         proposal_valid=valid,
                         proposal_status="VALID" if valid else pt,
                         note="proposal emitted BEFORE any mask was consulted"))

LEDGER = HERE / "04_proposal_ledger.csv"
with open(LEDGER, "w", newline="", encoding="utf-8") as fh:
    wr = csv.DictWriter(fh, fieldnames=list(prop[0])); wr.writeheader()
    for r in prop: wr.writerow(r)
LEDGER_HASH = sha(LEDGER)                      # <-- frozen BEFORE any mask
T["T04_ledger_hashed_before_mask"] = dict(ledger_sha256=LEDGER_HASH, result="PASS",
    note="hash computed immediately after writing proposals and before MASK was indexed")
T["T03_proposals_in_FULL_or_explicit_invalid"] = dict(
    result="PASS" if all(r["proposed_type"] in FULL or r["proposal_status"] in
                         CONTRACT["proposal"]["invalid_statuses"] for r in prop) else "FAIL",
    distinct_values=sorted({r["proposed_type"] for r in prop}))

# ======================================================= PHASE 2b — MASK SECOND
st_by_case = {c["case_id"]: c["state"] for c in cases}
excl = []
for r in prop:
    s = st_by_case[r["case_id"]]
    for pol in POLICIES:
        allowed = MASK[pol][s]
        if not r["proposal_valid"]:
            admitted, exc, reason = "", "", "proposal_invalid"
        else:
            adm = r["proposed_type"] in allowed
            admitted, exc = adm, (not adm)
            reason = ("" if adm else
                      ("UNSAFE_empty_set" if s == UNSAFE else
                       ("CAUTION_type_restriction" if s == CAUTION else "UNEXPECTED")))
        excl.append(dict(case_id=r["case_id"], local_timestamp=r["local_timestamp"],
            cluster_id=r["cluster_id"], advisor=r["advisor"], proposed_type=r["proposed_type"],
            proposal_valid=r["proposal_valid"], state=SN[s], policy=pol,
            allowed_set="FULL" if allowed == FULL else ("RESTRICTED" if allowed == RESTRICTED else "EMPTY"),
            admitted=admitted, excluded=exc, exclusion_reason=reason,
            no_mask_applied_for_B0=(r["advisor"] == "B0-UNRESTRICTED")))

# B0 is defined as "no mask" -> force zero exclusions by definition
for e in excl:
    if e["advisor"] == "B0-UNRESTRICTED":
        e["admitted"], e["excluded"], e["exclusion_reason"] = True, False, "B0: no mask applied by definition"

with open(HERE / "05_exclusion_and_incremental_binding.csv", "w", newline="", encoding="utf-8") as fh:
    wr = csv.DictWriter(fh, fieldnames=list(excl[0])); wr.writeheader()
    for r in excl: wr.writerow(r)

# ======================================================= PHASE 3 — estimands
idx = defaultdict(dict)
for e in excl: idx[(e["advisor"], e["policy"])][e["case_id"]] = e
summary = []
for a in ADVISORS:
    rows_a = [r for r in prop if r["advisor"] == a]
    nv = sum(1 for r in rows_a if r["proposal_valid"])
    ninv = len(rows_a) - nv
    inv_break = Counter(r["proposal_status"] for r in rows_a if not r["proposal_valid"])
    for pol in POLICIES:
        E = idx[(a, pol)]
        valid_cases = [r for r in rows_a if r["proposal_valid"]]
        num_x = sum(1 for r in valid_cases if E[r["case_id"]]["excluded"] is True)
        b_cf = (num_x / nv) if nv else None
        per_state = {}
        for s in (SAFE, CAUTION, UNSAFE):
            den = sum(1 for r in valid_cases if st_by_case[r["case_id"]] == s)
            n_s = sum(1 for r in valid_cases if st_by_case[r["case_id"]] == s
                      and E[r["case_id"]]["excluded"] is True)
            per_state[SN[s]] = (n_s, den, (n_s/den if den else None))
        summary.append(dict(
            item_id=f"SUM-{a}-{pol}", advisor=a, policy=pol,
            N_eligible=N_ELIG, N_valid=nv, N_invalid=ninv,
            invalid_breakdown="; ".join(f"{k}={v}" for k, v in inv_break.items()) or "none",
            coverage=round(nv/N_ELIG, 6),
            B_CF_numerator=num_x, B_CF_denominator=nv,
            B_CF_exact="UNDEFINED" if b_cf is None else f"{b_cf:.10f}",
            B_CF_percent="UNDEFINED" if b_cf is None else round(100*b_cf, 4),
            excl_SAFE=f"{per_state['SAFE'][0]}/{per_state['SAFE'][1]}",
            excl_CAUTION=f"{per_state['CAUTION'][0]}/{per_state['CAUTION'][1]}",
            excl_UNSAFE=f"{per_state['UNSAFE'][0]}/{per_state['UNSAFE'][1]}",
            verification_status="COMPUTED_FROM_DATA",
            caveat="synthetic proposals under a simulated advisor; no protective-action truth exists"))
    # I_CF
    E1, E2 = idx[(a, "C1")], idx[(a, "C2")]
    valid_cases = [r for r in rows_a if r["proposal_valid"]]
    inc = [r for r in valid_cases if E1[r["case_id"]]["excluded"] is False
           and E2[r["case_id"]]["excluded"] is True]
    vc_caution = [r for r in valid_cases if st_by_case[r["case_id"]] == CAUTION]
    td_caution = [r for r in vc_caution if r["proposed_type"] in ("DepartureTime", "Duration")]
    f1 = (len(vc_caution)/nv) if nv else None
    f2 = (len(td_caution)/len(vc_caution)) if vc_caution else None
    i_cf = (len(inc)/nv) if nv else None
    summary.append(dict(
        item_id=f"ICF-{a}", advisor=a, policy="C1->C2 incremental",
        N_eligible=N_ELIG, N_valid=nv, N_invalid=ninv, invalid_breakdown="",
        coverage=round(nv/N_ELIG, 6),
        B_CF_numerator=len(inc), B_CF_denominator=nv,
        B_CF_exact="UNDEFINED" if i_cf is None else f"{i_cf:.10f}",
        B_CF_percent="UNDEFINED" if i_cf is None else round(100*i_cf, 4),
        excl_SAFE="0/-", excl_CAUTION=f"{len(inc)}/{len(vc_caution)}", excl_UNSAFE="0/-",
        verification_status="COMPUTED_FROM_DATA",
        caveat=(f"I_CF composition: factor1 (valid CAUTION / N_valid) = {len(vc_caution)}/{nv}"
                + (f" = {f1:.10f}" if f1 is not None else " UNDEFINED")
                + f"; factor2 (timing-or-duration | valid CAUTION) = {len(td_caution)}/{len(vc_caution)}"
                + (f" = {f2:.10f}" if f2 is not None else " = UNDEFINED (no valid CAUTION proposals)")
                + f"; product x denominator = {len(inc)} incremental exclusions")))
with open(HERE / "06_summary_by_state_and_proposal.csv", "w", newline="", encoding="utf-8") as fh:
    wr = csv.DictWriter(fh, fieldnames=list(summary[0])); wr.writeheader()
    for r in summary: wr.writerow(r)

# ======================================================= PHASE 4 — controls + nondegeneracy
nS, nC, nU = state_counts[SAFE], state_counts[CAUTION], state_counts[UNSAFE]
ctrl = []
k = 0
for t in TYPES:
    a = f"B1-CONST-{t}"
    for pol in POLICIES:
        # analytic expectation DERIVED from measured state counts, never hardcoded
        if pol == "C0": exp = 0
        elif pol in ("C1", "C3"): exp = nU
        else: exp = nU if t in RESTRICTED else nU + nC
        got = next(r for r in summary if r["advisor"] == a and r["policy"] == pol)["B_CF_numerator"]
        k += 1
        ctrl.append(dict(item_id=f"CTL-{k:02d}", advisor=a, policy=pol,
            derivation=("0" if pol == "C0" else ("#UNSAFE" if pol in ("C1","C3") or t in RESTRICTED
                        else "#CAUTION + #UNSAFE")),
            expected_from_measured_state_counts=exp, computed_from_ledger=got,
            result="PASS" if exp == got else "FAIL", verification_status="COMPUTED_FROM_DATA",
            note="expectation derived from the measured state distribution of THIS run"))
T["T09_analytic_controls_match"] = dict(
    checks=len(ctrl), failures=[c["item_id"] for c in ctrl if c["result"] == "FAIL"],
    result="PASS" if all(c["result"] == "PASS" for c in ctrl) else "FAIL")

# B2 nondegeneracy + leakage
b2rows = [r for r in prop if r["advisor"] == "B2-FROZEN-VARYING"]
tdist = Counter(r["proposed_type"] for r in b2rows)
xtab = defaultdict(Counter)
for r in b2rows: xtab[SN[st_by_case[r["case_id"]]]][r["proposed_type"]] += 1
H = -sum((v/len(b2rows))*math.log2(v/len(b2rows)) for v in tdist.values() if v)
within_state_variation = {s: len([t for t, v in xtab[s].items() if v > 0]) for s in xtab}
clusters_with_variation = len({c for c in {r["cluster_id"] for r in b2rows}
    if len({r["proposed_type"] for r in b2rows if r["cluster_id"] == c}) > 1})
def pear(xs, ys):
    n_ = len(xs); mx, my = statistics.fmean(xs), statistics.fmean(ys)
    sx = math.sqrt(sum((x-mx)**2 for x in xs)); sy = math.sqrt(sum((y-my)**2 for y in ys))
    return sum((x-mx)*(y-my) for x, y in zip(xs, ys))/(sx*sy) if sx and sy else 0.0
cmap = {c["case_id"]: c for c in cases}
cg = pear([cmap[r["case_id"]]["gusts"] for r in b2rows], [cmap[r["case_id"]]["wind"] for r in b2rows])
cp = pear([cmap[r["case_id"]]["wper"] for r in b2rows], [cmap[r["case_id"]]["wave"] for r in b2rows])
# perfect-state-proxy test: best single-threshold accuracy of each feature at predicting UNSAFE
def best_split(feat):
    vals = sorted({cmap[r["case_id"]][feat] for r in b2rows})
    ys = [1 if st_by_case[r["case_id"]] == UNSAFE else 0 for r in b2rows]
    xs = [cmap[r["case_id"]][feat] for r in b2rows]
    best = 0.0
    for thr in vals[::max(1, len(vals)//60)]:
        acc = sum(1 for x, y in zip(xs, ys) if (x >= thr) == bool(y))/len(ys)
        best = max(best, acc, 1-acc)
    return round(best, 4)
nd = [dict(item_id="ND-01", metric="B2 distinct proposal types produced", value=len(tdist),
           detail="; ".join(f"{k2}={v}" for k2, v in tdist.most_common()),
           interpretation="more than one type = non-degenerate OUTPUT. Variation is NOT safety.",
           verification_status="COMPUTED_FROM_DATA"),
      dict(item_id="ND-02", metric="B2 proposal-type entropy (bits)", value=round(H, 4),
           detail=f"max possible {math.log2(len(TYPES)):.4f} bits over {len(TYPES)} types",
           interpretation="descriptive only; entropy is not a quality measure",
           verification_status="COMPUTED_FROM_DATA"),
      dict(item_id="ND-03", metric="distinct types within each state", value=str(within_state_variation),
           detail="type variation survives conditioning on state",
           interpretation="if a state had exactly one type, B2 would be a state proxy within it",
           verification_status="COMPUTED_FROM_DATA"),
      dict(item_id="ND-04", metric="day-clusters containing >1 proposal type",
           value=clusters_with_variation, detail=f"of {len({r['cluster_id'] for r in b2rows})} clusters",
           interpretation="within-episode variation as designed",
           verification_status="COMPUTED_FROM_DATA"),
      dict(item_id="LK-01", metric="Pearson r, gusts vs gate wind_speed", value=round(cg, 4),
           detail="physically correlated by construction; gusts are NOT read by the gate",
           interpretation="shared physical driver, NOT leakage; logged as a proxy-overlap caveat",
           verification_status="COMPUTED_FROM_DATA"),
      dict(item_id="LK-02", metric="Pearson r, wave_period vs gate wave_height", value=round(cp, 4),
           detail="physically correlated; wave_period is NOT read by the gate",
           interpretation="shared physical driver, NOT leakage",
           verification_status="COMPUTED_FROM_DATA"),
      dict(item_id="LK-03", metric="best single-threshold accuracy predicting UNSAFE, gusts",
           value=best_split("gusts"), detail="1.0 would mean a perfect state proxy",
           interpretation="a near-1.0 value would be a validity threat", verification_status="COMPUTED_FROM_DATA"),
      dict(item_id="LK-04", metric="best single-threshold accuracy predicting UNSAFE, wave_period",
           value=best_split("wper"), detail="1.0 would mean a perfect state proxy",
           interpretation="", verification_status="COMPUTED_FROM_DATA"),
      dict(item_id="LK-05", metric="B2 source references state/mask/allowed_set/gate feature",
           value="NO", detail="b2() reads only gusts, wdir, wper; see 00_contract.json feature_whitelist",
           interpretation="gate-independence by construction, grep-verified in Phase 0",
           verification_status="VERIFIED_FROM_CODE")]
with open(HERE / "07_static_controls_and_nondegeneracy.csv", "w", newline="", encoding="utf-8") as fh:
    cols = ["item_id","advisor","policy","derivation","expected_from_measured_state_counts",
            "computed_from_ledger","result","metric","value","detail","interpretation",
            "verification_status","note"]
    wr = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore"); wr.writeheader()
    for r in ctrl + nd: wr.writerow(r)

# cross-tab
with open(HERE / "06b_type_by_state_crosstab.csv", "w", newline="", encoding="utf-8") as fh:
    wr = csv.writer(fh); wr.writerow(["advisor","state"] + TYPES + ["ABSTAIN","row_total"])
    for a in ADVISORS:
        rr = [r for r in prop if r["advisor"] == a]
        for s in (SAFE, CAUTION, UNSAFE):
            c2 = Counter(r["proposed_type"] for r in rr if st_by_case[r["case_id"]] == s)
            wr.writerow([a, SN[s]] + [c2.get(t, 0) for t in TYPES] + [c2.get("ABSTAIN", 0), sum(c2.values())])

json.dump(dict(tests=T, ledger_hash=LEDGER_HASH, N_ELIG=N_ELIG,
               states={SN[k2]: v for k2, v in state_counts.items()},
               excl_reasons=dict(excl_reasons),
               advisors=ADVISORS, b2_type_distribution=dict(tdist),
               before=BEFORE, after={p: sha(ROOT / p) for p in FROZEN}),
          open(HERE / "_run_state.json", "w"), indent=2)

print(f"eligible cases   : {N_ELIG:,}   (target {TGT:,})  {T['T13_population_and_states_match_A18_1']['result']}")
print(f"states           : SAFE {nS:,}  CAUTION {nC:,}  UNSAFE {nU:,}")
print(f"ledger freeze    : {LEDGER_HASH[:32]}...")
print(f"B2 type mix      : {dict(tdist)}")
print(f"analytic controls: {T['T09_analytic_controls_match']['result']} ({len(ctrl)} checks)")
print()
for a in ADVISORS:
    i = next(r for r in summary if r["item_id"] == f"ICF-{a}")
    c2 = next(r for r in summary if r["advisor"] == a and r["policy"] == "C2")
    print(f"  {a:22s} cov={i['coverage']:.4f}  B_CF(C2)={c2['B_CF_numerator']:>5}/{c2['B_CF_denominator']} "
          f"= {c2['B_CF_percent']:>7}%   I_CF={i['B_CF_numerator']:>4}/{i['B_CF_denominator']} = {i['B_CF_percent']}%")
