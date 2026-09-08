#!/usr/bin/env python3
"""C-6: build data/c6/prediction-reresolution.csv.

Mechanical outcome assignment only: a candidate actual inside the ORIGINAL
expected band is CONFIRMED, otherwise REFUTED. No softening categories.
Original prediction text and expected bands are read from the register and
copied verbatim; nothing is written back to the register by this script.
"""

import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
DATA = ROOT / "data"
OUT = DATA / "c6"
REG = DATA / "prediction-register.csv"
CAND = OUT / "c6-candidate-actuals.json"
C5 = DATA / "c5" / "c5-three-stage-metrics.csv"
SOLAR = DATA / "solar" / "solar-events-daily.csv"


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


reg = {r["id"]: r for r in csv.DictReader(REG.open())}
cand = json.load(CAND.open())
inc, mb = cand["incumbent"], cand["model_b_candidate"]
c5 = {r["stage"]: r for r in csv.DictReader(C5.open())}
s1, s2, s3 = (c5["stage1_v1_incumbent"], c5["stage2_v2_incumbent"],
              c5["stage3_v2_modelb"])

EV_C5 = f"data/c5/c5-three-stage-metrics.csv sha256={sha(C5)[:16]}"
EV_C6 = f"data/c6/c6-candidate-actuals.json (solar sha256={sha(SOLAR)[:16]})"
EV_STRUCT = "condition_comparison.py COND map: C1 and C3 identical"

CAND_SPEC = cand["candidate_spec"]
PREV_SPEC = cand["previous_spec"]


def band(pid):
    r = reg[pid]
    lo, hi = r["pred_lo"], r["pred_hi"]
    return (float(lo), float(hi)) if lo and hi else (None, None)


def verdict(pid, actual):
    lo, hi = band(pid)
    if lo is None:
        return None
    return "CONFIRMED" if lo <= float(actual) <= hi else "REFUTED"


def f4(x):
    return f"{float(x):.4f}"


# id: (candidate actual, comparable baseline, delta components, attribution, evidence)
rows = []


# Verdict the prediction would already receive under the INCUMBENT g_t at the
# current canonical configuration. This separates flips caused by SDR-001 from
# flips already caused by the threshold and data changes that predate it.
INCUMBENT_AT_CURRENT = {
    "P04": inc.get("P04"), "P05": inc.get("P05"), "P06": inc.get("P06"),
    "P07": inc.get("P07"), "P08": inc.get("P08"), "P18": inc.get("P18"),
    "P19": inc.get("P19"), "P20": inc.get("P20"), "P21": inc.get("P21"),
    "P22": inc.get("P22"), "P23": inc.get("P23"), "P24": inc.get("P24"),
    "P09": float(s2["P09_total_transitions"]), "P10": float(s2["P10_non_scheduled"]),
    "P11": float(s2["P11_oscillations"]), "P12": float(s2["P12_reduction_pct"]),
    "P03": 0.0,
}


def add(pid, cand_actual, baseline, deltas, attribution, evidence, cand_status=None,
        note=""):
    r = reg[pid]
    st = cand_status or verdict(pid, cand_actual)
    iv = INCUMBENT_AT_CURRENT.get(pid)
    inc_status = verdict(pid, iv) if iv is not None else None
    already = "YES" if (inc_status == "REFUTED" and r["status"] == "CONFIRMED") else "NO"
    attributable = "n/a"
    if st != r["status"]:
        attributable = "NO — already REFUTED under incumbent" if already == "YES" \
            else "YES — flip caused by the g_t design change"
    rows.append({
        "prediction_id": pid,
        "original_prediction_text": r["metric"],
        "original_scope": r["scope"],
        "original_expected_band": r["pred_stated"],
        "band_lo": r["pred_lo"], "band_hi": r["pred_hi"],
        "previous_specification": PREV_SPEC,
        "previous_actual": r["actual"],
        "previous_status": r["status"],
        "comparable_baseline": baseline,
        "candidate_specification": CAND_SPEC,
        "candidate_actual": cand_actual,
        "candidate_status": st,
        "status_changed": "YES" if st != r["status"] else "NO",
        "incumbent_at_current_config": ("" if iv is None else
                                        (f"{iv:.4f}" if isinstance(iv, float) else str(iv))),
        "status_under_incumbent_at_current_config": inc_status or "",
        "already_refuted_before_model_b": already,
        "flip_attributable_to_sdr_001": attributable,
        "delta_components": deltas,
        "change_attribution": attribution,
        "evidence_source": evidence,
        "reason_for_reresolution": ("SDR-001 approved migration candidate replaces "
                                    "g_t with the solar-event two-state classifier"),
        "reresolution_date": "2026-09-08",
        "condition": "C-6",
        "applies_only_if_migration_completes": "YES",
        "notes": note,
    })


# ---------------- unaffected ----------------
for pid, why in (("P01", "g_w activations; independent of g_t"),
                 ("P02", "superseded vessel-blind g_o; independent of g_t"),
                 ("P15", "max sustained wind; independent of g_t"),
                 ("P16", "g_w activations, sea cell; independent of g_t")):
    r = reg[pid]
    rows.append({
        "prediction_id": pid, "original_prediction_text": r["metric"],
        "original_scope": r["scope"], "original_expected_band": r["pred_stated"],
        "band_lo": r["pred_lo"], "band_hi": r["pred_hi"],
        "previous_specification": PREV_SPEC, "previous_actual": r["actual"],
        "previous_status": r["status"], "comparable_baseline": r["actual"],
        "incumbent_at_current_config": "", "status_under_incumbent_at_current_config": "",
        "already_refuted_before_model_b": "NO", "flip_attributable_to_sdr_001": "n/a",
        "candidate_specification": CAND_SPEC, "candidate_actual": r["actual"],
        "candidate_status": r["status"], "status_changed": "NO",
        "delta_components": "none", "change_attribution": "unaffected",
        "evidence_source": "n/a — metric does not read g_t",
        "reason_for_reresolution": "not re-resolved; g_t-independent",
        "reresolution_date": "2026-09-08", "condition": "C-6",
        "applies_only_if_migration_completes": "n/a", "notes": why,
    })

# ---------------- scope-only ----------------
add("P03", "0.0000", "0.0 (v1)", "delta_g_t=0.0000",
    "scope wording only (daylight 06-17); outcome invariant",
    EV_C6, note="SAFE unreachable under the superseded g_v floor in any window")

# ---------------- PRIMARY-config, computed ----------------
add("P04", f4(mb["P04"]), f4(inc["P04"]) + " (v2/incumbent = canonical 7.72%)",
    f"registered 12.4 -> {f4(inc['P04'])} threshold+data; -> {f4(mb['P04'])} delta_g_t="
    f"{mb['P04']-inc['P04']:+.4f} pp",
    "threshold amendment + data/configuration + g_t design change",
    EV_C6,
    note="ALREADY outside band at v2/incumbent (7.72). Band exit is NOT attributable to SDR-001")
add("P05", f4(mb["P05"]), f4(inc["P05"]) + " (v2/incumbent = canonical 98.66%)",
    f"delta_g_t={mb['P05']-inc['P05']:+.4f} pp",
    "data/configuration + g_t design change", EV_C6)
add("P06", f4(mb["P06"]), f4(inc["P06"]),
    f"delta_g_t={mb['P06']-inc['P06']:+.4f} pp",
    "data/configuration + g_t design change", EV_C6)
add("P07", f4(mb["P07"]), f4(inc["P07"]) + " (v2/incumbent = canonical 87.63%)",
    f"register 87.58 (v1) -> {f4(inc['P07'])} data; -> {f4(mb['P07'])} delta_g_t="
    f"{mb['P07']-inc['P07']:+.4f} pp",
    "data/configuration + g_t design change", EV_C6)
add("P08", f"{mb['P08']:.0f}", f"{inc['P08']:.0f}",
    f"delta_g_t={mb['P08']-inc['P08']:+.0f}",
    "data/configuration + g_t design change", EV_C6,
    note="g_t still binds pre-sunrise inside the 05-09 window")

# ---------------- FROZEN C-5 ----------------
add("P09", s3["P09_total_transitions"], f"{s1['P09_total_transitions']} (v1/current thresholds)",
    "5416 -(threshold -196)-> 5220 -(data -19)-> 5201 -(g_t -1540)-> 3661",
    "threshold amendment (-196) + data/configuration (-19) + g_t design change (-1540)",
    EV_C5,
    note="MANDATORY: registered 5416 is the PRE-AMENDMENT vintage. Do NOT report "
         "5416->3661 as a g_t effect; that would overstate SDR-001 by 14x")
add("P10", s3["P10_non_scheduled"], f"{s1['P10_non_scheduled']} (v1/current thresholds)",
    "230 -(data -23)-> 207 -(g_t +15)-> 222", "data/configuration + g_t design change",
    EV_C5)
add("P11", s3["P11_oscillations"], f"{s1['P11_oscillations']} (v1/current thresholds)",
    "37 -(data -10)-> 27 -(g_t -1)-> 26", "data/configuration + g_t design change",
    EV_C5, note="stale 70 is the pre-amendment vintage; provenance only")
add("P12", s3["P12_reduction_pct"], f"{s1['P12_reduction_pct']} (v1/current thresholds)",
    "7.83 -(data +0.87)-> 8.70 -(g_t +1.66)-> 10.36 pp",
    "data/configuration + g_t design change", EV_C5,
    note="stale 6.17 is the pre-amendment vintage; provenance only")

_p13 = (f"non-sched={s3['P10_non_scheduled']}, osc={s3['P11_oscillations']}")
add("P13", _p13, f"non-sched={s1['P10_non_scheduled']}, osc={s1['P11_oscillations']}",
    "non-sched 230->207->222; osc 37->27->26",
    "data/configuration + g_t design change", EV_C5,
    cand_status="CONFIRMED",
    note="original criteria: non-scheduled<=500 AND oscillations<=100. "
         "222<=500 and 26<=100 -> chattering still NOT demonstrated -> NO")

_p14 = (f"g_o {mb['P14_g_o_dayCAUTION']:.2f}% daylight CAUTION; "
        f"g_t {mb['P14_g_t_nonSAFE']:.2f}% all non-SAFE; g_w & g_m never bind")
add("P14", _p14,
    f"g_o {inc['P14_g_o_dayCAUTION']:.2f}%; g_t {inc['P14_g_t_nonSAFE']:.2f}%",
    "g_o and g_t shares shift slightly; g_w/g_m binding remain 0.00%",
    "data/configuration + g_t design change", EV_C6,
    cand_status="CONFIRMED",
    note="wave gate + night curfew reading holds, and holds MORE strongly: "
         "under Model B g_t is purely a curfew (no time-driven CAUTION)")

# ---------------- RESOLUTION-config, computed ----------------
add("P17", f"MFWAM {mb['P17_mfwam']:.2f}% vs ERA5 {mb['P17_era5']:.2f}%",
    f"MFWAM {inc['P17_mfwam']:.2f}% vs ERA5 {inc['P17_era5']:.2f}%",
    "both CAUTION rates fall; ordering preserved",
    "data/configuration + g_t design change", EV_C6,
    cand_status="CONFIRMED" if mb["P17_mfwam_lower"] else "REFUTED",
    note="Boolean prediction: MFWAM LOWER. Holds under the candidate")
add("P18", f4(mb["P18"]), f4(inc["P18"]) + " (v2/incumbent = canonical 5.98%)",
    f"registered 8.32 -> {f4(inc['P18'])} threshold+data; -> {f4(mb['P18'])} delta_g_t="
    f"{mb['P18']-inc['P18']:+.4f} pp",
    "threshold amendment + data/configuration + g_t design change", EV_C6,
    note="ALREADY outside band at v2/incumbent (5.98). Band exit predates SDR-001")
add("P19", f4(mb["P19"]), f4(inc["P19"]) + " (v2/incumbent = canonical 5.98%)",
    f"registered 6.1 -> {f4(inc['P19'])} data; -> {f4(mb['P19'])} delta_g_t="
    f"{mb['P19']-inc['P19']:+.4f} pp",
    "data/configuration + g_t design change", EV_C6)
add("P20", f"{mb['P20']:.0f}", f"{inc['P20']:.0f} (v2/incumbent = canonical 409)",
    f"delta_g_t={mb['P20']-inc['P20']:+.0f} hours",
    "g_t design change (dominant)", EV_C6,
    note="'daylight' held at the REGISTERED scope 06:00-17:00. Under Model B the "
         "06:00 hour is UNSAFE (sunrise 06:01-06:34), so UNSAFE now intrudes into "
         "the registered window. The TERM is redefined, not merely recomputed — C-8")
add("P21", f4(mb["P21"]), f4(inc["P21"]) + " (canonical 0.00%)",
    "delta_g_t=0.0000 — structurally invariant",
    "structurally invariant", EV_STRUCT,
    note="C1 and C3 are the IDENTICAL admissible-set map, so divergence is 0 for "
         "ANY classifier. No empirical rerun needed. Supports the F-15 novelty / "
         "Review-3 response, which this decision cannot disturb")
add("P22", f4(mb["P22"]), f4(inc["P22"]) + " (v2/incumbent = canonical 5.98%)",
    f"registered 5.98 -> {f4(inc['P22'])} unchanged; -> {f4(mb['P22'])} delta_g_t="
    f"{mb['P22']-inc['P22']:+.4f} pp",
    "g_t design change", EV_C6,
    note="Was REFUTED and remains REFUTED — but for a different reason and a "
         "larger margin. Status unchanged; magnitude changed")
add("P23", f4(mb["P23"]), f4(inc["P23"]) + " (v2/incumbent = canonical 28.19%)",
    f"delta_g_t={mb['P23']-inc['P23']:+.4f} pp",
    "g_t design change", EV_C6,
    note="Rises because Model B enlarges UNSAFE, widening C0-vs-C2 divergence")
add("P24", f4(mb["P24"]), f4(inc["P24"]) + " (v2/incumbent = canonical 22.21%)",
    f"delta_g_t={mb['P24']-inc['P24']:+.4f} pp",
    "g_t design change", EV_C6,
    note="Rises for the same reason as P23")

rows.sort(key=lambda r: r["prediction_id"])
p = OUT / "prediction-reresolution.csv"
with p.open("w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)

print(f"{'id':5s}{'prev':>10}{'cand':>34}{'prev st':>11}{'cand st':>11}  chg")
print("-" * 76)
flips = 0
for r in rows:
    if r["status_changed"] == "YES":
        flips += 1
    print(f"{r['prediction_id']:5s}{r['previous_actual'][:9]:>10}"
          f"{r['candidate_actual'][:33]:>34}{r['previous_status']:>11}"
          f"{r['candidate_status']:>11}  {r['status_changed']}")

from collections import Counter
att = [r["prediction_id"] for r in rows if r["flip_attributable_to_sdr_001"].startswith("YES")]
pre = [r["prediction_id"] for r in rows if r["flip_attributable_to_sdr_001"].startswith("NO")]
print(f"\nrows: {len(rows)}   status flips: {flips}")
print(f"  flips ATTRIBUTABLE to SDR-001 g_t change : {len(att)}  {att}")
print(f"  flips ALREADY refuted under incumbent    : {len(pre)}  {pre}")
print("previous totals :", dict(Counter(r["previous_status"] for r in rows)))
print("candidate totals:", dict(Counter(r["candidate_status"] for r in rows)))
print(f"\nartefact: {p.relative_to(ROOT)}  sha256 {sha(p)}")
print(f"register sha256 (unchanged by this script): {sha(REG)}")
