#!/usr/bin/env python3
"""C-6: controlled, additive annotation of the prediction register.

MUTATION POLICY
---------------
The register schema carries ONE active `status` and ONE active `actual`.
Model B is APPROVED but NOT CANONICAL, so the canonical outcome of every
prediction is still the incumbent one. Writing candidate statuses into
`status` would either destroy the canonical verdict or publish a 15/9 count
for an architecture that does not yet exist.

Therefore:
  * `actual`, `status`, `resolved`, `metric`, `scope`, `pred_lo`, `pred_hi`,
    `pred_stated`, `rationale`, `registered`, `analysis`, `pred_type`
    are NOT touched for any prediction.
  * A pointer is APPENDED to `notes` for every re-resolved prediction, naming
    the candidate actual, candidate status and the evidence artefact.
  * Top-level totals therefore remain 22 CONFIRMED / 2 REFUTED, which is the
    correct canonical count until C-8 completes.

Guard: the script refuses to run if any protected field would differ.
"""

import csv
import hashlib
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
DATA = ROOT / "data"
REG = DATA / "prediction-register.csv"
RES = DATA / "c6" / "prediction-reresolution.csv"

PROTECTED = ["id", "registered", "analysis", "scope", "metric", "pred_type",
             "pred_lo", "pred_hi", "pred_stated", "rationale", "actual",
             "status", "resolved"]


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    before = sha(REG)
    rows = list(csv.DictReader(REG.open()))
    fields = list(rows[0].keys())
    original = {r["id"]: dict(r) for r in rows}

    res = {r["prediction_id"]: r for r in csv.DictReader(RES.open())}

    n = 0
    for r in rows:
        rr = res.get(r["id"])
        if rr is None or rr["change_attribution"] == "unaffected":
            continue
        flip = rr["status_changed"] == "YES"
        note = (f"[C-6 2026-09-08 — CANDIDATE ONLY, NOT APPLIED] Under the APPROVED "
                f"MIGRATION CANDIDATE (SDR-001 Model B, not yet canonical) this "
                f"prediction's actual would be {rr['candidate_actual']} -> "
                f"{rr['candidate_status']}"
                + (" (STATUS FLIP)" if flip else " (status unchanged)")
                + (f"; flip attributable to SDR-001: {rr['flip_attributable_to_sdr_001']}"
                   if flip else "")
                + f". The canonical actual and status above are UNCHANGED and remain "
                  f"authoritative until C-8 completes. Evidence: "
                  f"data/c6/prediction-reresolution.csv.")
        r["notes"] = (r["notes"] + " " if r["notes"].strip() else "") + note
        n += 1

    # --- guard: protected fields must be byte-identical ---
    for r in rows:
        o = original[r["id"]]
        for f in PROTECTED:
            if r[f] != o[f]:
                raise SystemExit(f"GUARD TRIPPED: {r['id']}.{f} changed "
                                 f"{o[f]!r} -> {r[f]!r}. Aborting, nothing written.")

    shutil.copy2(REG, DATA / "c6" / "prediction-register.pre-c6.csv")
    with REG.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    after = sha(REG)
    check = list(csv.DictReader(REG.open()))
    from collections import Counter
    print(f"annotated rows            : {n}")
    print(f"entries                   : {len(check)}")
    print(f"status totals             : {dict(Counter(x['status'] for x in check))}")
    print(f"protected fields unchanged: True (guard passed)")
    print(f"register sha256 BEFORE    : {before}")
    print(f"register sha256 AFTER     : {after}")
    print(f"backup                    : data/c6/prediction-register.pre-c6.csv "
          f"sha256 {sha(DATA/'c6'/'prediction-register.pre-c6.csv')}")


if __name__ == "__main__":
    main()
