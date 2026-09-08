#!/usr/bin/env python3
"""C-8: promote C-6 candidate outcomes to CANONICAL outcomes.

Runs only after the migrated canonical pipeline has reproduced the C-6
candidate evidence. Promotes `actual` and `status` for affected predictions;
preserves original prediction text, scope and expected bands byte-identically;
preserves the previous canonical actual/status inside `notes`.

Guards
------
* PROTECTED fields must be unchanged: id, registered, analysis, scope, metric,
  pred_type, pred_lo, pred_hi, pred_stated, rationale.
* Every promoted row must carry its previous actual and status in `notes`.
* Totals are recomputed from the rows, never asserted.
"""

import csv
import hashlib
import shutil
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
DATA = ROOT / "data"
REG = DATA / "prediction-register.csv"
RES = DATA / "c6" / "prediction-reresolution.csv"
OUT = DATA / "c8"
OUT.mkdir(parents=True, exist_ok=True)

PROTECTED = ["id", "registered", "analysis", "scope", "metric", "pred_type",
             "pred_lo", "pred_hi", "pred_stated", "rationale"]

NEW_SPEC = ("CANONICAL after SDR-001 applied 2026-09-08 — g_t solar-event "
            "two-state (solar-spec-v1, frozen artefact); v2 sea-cell data; "
            "w 21.6/27.0; r 10.0/20.0; o_small 1.0/1.25")

P20_NOTE = (" DEFINITION MIGRATION: this prediction's registered scope uses the "
            "fixed 06:00-17:00 window, and the canonical actual above is computed "
            "in THAT window so the original prediction is answered as asked. The "
            "canonical architecture now defines daylight astronomically "
            "(sunrise <= t < sunset); under that definition the RESOLUTION "
            "daylight-UNSAFE count is 455, not 1529. Same phenomenon, two "
            "definitions — not one quantity measured twice.")


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    before = sha(REG)
    rows = list(csv.DictReader(REG.open()))
    fields = list(rows[0].keys())
    original = {r["id"]: dict(r) for r in rows}
    res = {r["prediction_id"]: r for r in csv.DictReader(RES.open())}

    promoted = flips = 0
    for r in rows:
        rr = res.get(r["id"])
        if rr is None or rr["change_attribution"] == "unaffected":
            continue
        prev_actual, prev_status = r["actual"], r["status"]
        new_actual, new_status = rr["candidate_actual"], rr["candidate_status"]

        note = (f" [C-8 2026-09-08 — SDR-001 APPLIED, CANONICAL] Previous canonical "
                f"actual {prev_actual} ({prev_status}) under the superseded "
                f"specification: {rr['previous_specification']}. New canonical "
                f"actual {new_actual} ({new_status}) under: {NEW_SPEC}. "
                f"Delta: {rr['delta_components']}. Attribution: "
                f"{rr['change_attribution']}.")
        if new_status != prev_status:
            flips += 1
            note += (f" STATUS FLIP {prev_status} -> {new_status}; "
                     f"attributable to SDR-001: {rr['flip_attributable_to_sdr_001']}.")
        note += " Evidence: data/c6/prediction-reresolution.csv."
        if r["id"] == "P20":
            note += P20_NOTE

        # retire the C-6 "candidate only" wording, keep everything else
        r["notes"] = r["notes"].replace(
            "[C-6 2026-09-08 — CANDIDATE ONLY, NOT APPLIED]",
            "[C-6 2026-09-08 — candidate, since APPLIED at C-8]") + note
        r["actual"] = new_actual
        r["status"] = new_status
        r["resolved"] = "2026-09-08"
        promoted += 1

    for r in rows:
        o = original[r["id"]]
        for f in PROTECTED:
            if r[f] != o[f]:
                raise SystemExit(f"GUARD TRIPPED: {r['id']}.{f} changed. Nothing written.")
        if r["actual"] != o["actual"] and o["actual"] not in r["notes"]:
            raise SystemExit(f"GUARD TRIPPED: {r['id']} previous actual not preserved.")

    shutil.copy2(REG, OUT / "prediction-register.pre-c8.csv")
    with REG.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    check = list(csv.DictReader(REG.open()))
    totals = Counter(x["status"] for x in check)
    print(f"promoted rows   : {promoted}   status flips: {flips}")
    print(f"entries         : {len(check)}")
    print(f"totals (from rows): {dict(totals)}")
    print(f"protected fields unchanged / history preserved : guards passed")
    print(f"register BEFORE : {before}")
    print(f"register AFTER  : {sha(REG)}")
    print(f"backup          : data/c8/prediction-register.pre-c8.csv "
          f"{sha(OUT/'prediction-register.pre-c8.csv')}")


if __name__ == "__main__":
    main()
