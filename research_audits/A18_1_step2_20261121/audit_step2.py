#!/usr/bin/env python3
"""
A18.1 Step 2 — Dataset Provenance and Integrity Audit (READ-ONLY).

Standard library only (csv, hashlib, json, statistics, datetime, zoneinfo).
Deliberately avoids pandas so the audit does not share a dependency with the
artefact under audit, and so every count is derived by a streaming reader
independent of the original code path.

Writes ONLY into its own directory. Opens every input 'rb'/'r' and never 'w'
on an input path.
"""
import csv, hashlib, json, statistics, sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent.parent      # repo root
DATA = ROOT / "data"
OUT = Path(__file__).resolve().parent
KUCHING = ZoneInfo("Asia/Kuching")

# ---------------------------------------------------------------- lineage map
# Classification taken from in-code comments, cited per row in the registers.
ARTEFACTS = {
    "raw_weather_sea.csv": dict(
        role="RAW_SOURCE", stream="wind+precip+WMO", config="CANONICAL_v2_SEA",
        provider_documented="Open-Meteo archive (ERA5 land/sea reanalysis)",
        evidence="scripts/historical_replay.py:117-132 (CANONICAL v2 SEA-CELL)"),
    "raw_marine_era5_sea.csv": dict(
        role="RAW_SOURCE", stream="wave", config="PRIMARY",
        provider_documented="Open-Meteo marine archive, ERA5-Ocean",
        evidence="scripts/condition_comparison.py:124"),
    "raw_marine_mfwam.csv": dict(
        role="RAW_SOURCE", stream="wave", config="RESOLUTION",
        provider_documented="Open-Meteo marine archive, MFWAM",
        evidence="scripts/condition_comparison.py:125"),
    "raw_weather.csv": dict(
        role="RAW_SUPERSEDED", stream="wind+precip+WMO", config="v1_LAND_condemned",
        provider_documented="Open-Meteo archive",
        evidence="scripts/historical_replay.py:118-121 (land cell F-10 condemned)"),
    "raw_marine.csv": dict(
        role="RAW_SUPERSEDED", stream="wave", config="v1_LAND_condemned",
        provider_documented="Open-Meteo marine archive",
        evidence="scripts/historical_replay.py:118-121"),
    "raw_rainfall.csv": dict(
        role="RAW_SUPERSEDED", stream="precip", config="v1_LAND_condemned",
        provider_documented="Open-Meteo archive",
        evidence="scripts/condition_comparison.py:132 (precip taken from sea file, NOT this)"),
    "raw_tide_marea.csv": dict(
        role="RAW_UNUSED_BY_REPLAY", stream="tide", config="not_in_classifier",
        provider_documented="Marea / tide service (see scripts/tide_marea_download.py)",
        evidence="no read of this file found in the four canonical scripts"),
}
OPENMETEO_META_ROWS = 3   # 2 metadata lines + 1 blank; matches pandas skiprows=3

def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def read_openmeteo(p):
    """Return (meta dict, header list, list of row dicts). Streaming-ish: these
    files are <2MB so a single pass into memory is bounded and safe."""
    with open(p, newline="", encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    meta = {}
    if lines and lines[0].startswith("latitude"):
        keys = next(csv.reader([lines[0]]))
        vals = next(csv.reader([lines[1]]))
        meta = dict(zip(keys, vals))
        body = lines[OPENMETEO_META_ROWS:]
    else:
        body = lines                       # tide file: no metadata block
    rdr = csv.DictReader(body)
    return meta, rdr.fieldnames, list(rdr)

def num(v):
    if v is None: return None
    v = v.strip()
    if v == "" or v.upper() in ("NAN", "NA", "NULL", "-"): return None
    try: return float(v)
    except ValueError: return None

def parse_ts(s):
    s = s.strip()
    for fmt in ("%Y-%m-%dT%H:%M", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M"):
        try: return datetime.strptime(s, fmt)
        except ValueError: pass
    return None

# =============================================================== main
inventory, schema, temporal, spatial, missing, lineage = [], [], [], [], [], []
status = {"generated": datetime.now(KUCHING).isoformat(), "artefacts": {},
          "computed_counts": {}, "manuscript_targets": {
              "PRIMARY_records": 43848, "PRIMARY_window_hours": 9135,
              "RESOLUTION_usable_records": 28501, "RESOLUTION_window_hours": 5935,
              "RESOLUTION_missing_wave_excluded": 11},
          "blockers": []}
loaded = {}
n = 0

for fname, info in ARTEFACTS.items():
    p = DATA / fname
    n += 1
    iid = f"INV-{n:02d}"
    if not p.exists():
        inventory.append(dict(item_id=iid, source_path_or_uri=str(p.relative_to(ROOT)),
            verification_status="MISSING", evidence_reference="filesystem",
            finding="file absent", limitation_or_unknown="cannot audit",
            next_action="user must supply", **{k: info[k] for k in ("role","stream","config")}))
        status["blockers"].append(f"{fname} absent")
        continue

    meta, header, rows = read_openmeteo(p)
    loaded[fname] = (meta, header, rows)
    tcol = header[0]
    ts = [parse_ts(r[tcol]) for r in rows]
    good = [t for t in ts if t]
    st = sha256(p)

    inventory.append(dict(
        item_id=iid, source_path_or_uri=str(p.relative_to(ROOT)),
        verification_status="VERIFIED_FROM_FILE",
        evidence_reference=info["evidence"],
        finding=(f"{len(rows)} data rows; cols={len(header)}; "
                 f"range {good[0].isoformat() if good else 'NA'}..{good[-1].isoformat() if good else 'NA'}"),
        limitation_or_unknown=("provider identity is DOCUMENTED_ONLY: no provider manifest or "
                               "published checksum is stored locally; local hash proves local "
                               "integrity only, NOT agency authenticity"),
        next_action="retain hash; obtain provider manifest if authenticity must be asserted",
        role=info["role"], stream=info["stream"], config=info["config"],
        provider_documented=info["provider_documented"],
        sha256=st, size_bytes=p.stat().st_size,
        rows_data=len(rows), columns=len(header),
        column_names="; ".join(header),
        meta_latitude=meta.get("latitude", "ABSENT_IN_FILE"),
        meta_longitude=meta.get("longitude", "ABSENT_IN_FILE"),
        meta_timezone=meta.get("timezone", "ABSENT_IN_FILE"),
        meta_utc_offset_seconds=meta.get("utc_offset_seconds", "ABSENT_IN_FILE"),
        mtime_informational=datetime.fromtimestamp(p.stat().st_mtime).isoformat()))
    status["artefacts"][fname] = dict(sha256=st, rows=len(rows), role=info["role"])

    # ---- B. schema & units
    for col in header:
        vals = [num(r[col]) for r in rows] if col != tcol else []
        nulls = sum(1 for r in rows if (r[col] or "").strip() in ("", "NaN", "nan"))
        unit = col.split("(")[1].rstrip(")") if "(" in col else ""
        nn = [v for v in vals if v is not None]
        schema.append(dict(
            item_id=f"SCH-{n:02d}-{header.index(col):02d}",
            source_path_or_uri=f"{p.relative_to(ROOT)}::{col}",
            verification_status="COMPUTED_FROM_FILE",
            evidence_reference=f"header row {OPENMETEO_META_ROWS+1} of {fname}",
            finding=(f"nulls={nulls}" + (f"; min={min(nn)}; median={statistics.median(nn)}; max={max(nn)}" if nn else "")),
            limitation_or_unknown=("unit string parsed from column header; SOURCE_VERIFIED only in the "
                                   "sense that the provider wrote it into the header, not cross-checked "
                                   "against a provider data dictionary" if unit else
                                   "no unit declared in header -> UNKNOWN"),
            next_action="cross-check against provider data dictionary" if unit else "determine unit",
            column=col, declared_unit=unit or "UNKNOWN",
            unit_status="HEADER_DECLARED" if unit else "UNKNOWN",
            dtype_observed=("timestamp" if col == tcol else
                            ("numeric" if nn else "empty/non-numeric")),
            non_null=len(nn), null_or_nan=nulls))

# =============================================================== C. temporal
def window_counts(ts_list, lo, hi, inclusive_hi):
    return sum(1 for t in ts_list if t and (lo <= t.hour <= hi if inclusive_hi else lo <= t.hour < hi))

for fname, (meta, header, rows) in loaded.items():
    tcol = header[0]
    ts = [parse_ts(r[tcol]) for r in rows]
    good = [t for t in ts if t]
    dup = [k for k, c in Counter(good).items() if c > 1]
    ordered = all(good[i] <= good[i+1] for i in range(len(good)-1))
    gaps = []
    if len(good) > 1:
        for i in range(len(good)-1):
            d = (good[i+1] - good[i]).total_seconds()
            if d != 3600: gaps.append((good[i].isoformat(), d))
    days = len({t.date() for t in good})
    tz_declared = meta.get("timezone", "ABSENT")
    off = meta.get("utc_offset_seconds", "ABSENT")
    temporal.append(dict(
        item_id=f"TMP-{fname}", source_path_or_uri=f"data/{fname}",
        verification_status="COMPUTED_FROM_FILE",
        evidence_reference=f"metadata row 2 of {fname}; timestamps column '{tcol}'",
        finding=(f"rows={len(rows)}; parsed={len(good)}; distinct_days={days}; "
                 f"monotonic={ordered}; duplicates={len(dup)}; non_3600s_steps={len(gaps)}; "
                 f"window_05_09_inclusive={window_counts(good,5,9,True)}; "
                 f"window_05_09_exclusive_hi={window_counts(good,5,9,False)}"),
        limitation_or_unknown=(
            f"timestamps are NAIVE in-file and the metadata declares timezone='{tz_declared}', "
            f"utc_offset_seconds={off}. They are therefore ALREADY LOCAL (Asia/Kuching) as written "
            "by the provider; NO UTC->local conversion is applied anywhere in the pipeline. "
            "This is an ASSUMPTION INHERITED FROM THE PROVIDER REQUEST, not independently "
            "verifiable from the file alone."),
        next_action=("re-issue one provider request with timezone=UTC and compare a sample hour "
                     "to confirm the local-time claim"),
        declared_timezone=tz_declared, declared_utc_offset_seconds=off,
        tz_conversion_applied="NONE_REQUIRED_ALREADY_LOCAL",
        first_ts=good[0].isoformat() if good else "", last_ts=good[-1].isoformat() if good else "",
        duplicate_timestamps=len(dup), non_hourly_steps=len(gaps),
        example_irregular_step=str(gaps[:2]) if gaps else "",
        distinct_days=days,
        window_hours_inclusive_0509=window_counts(good,5,9,True),
        window_hours_halfopen_0509=window_counts(good,5,9,False)))

# =============================================================== D. spatial
TARGETS = {"weather_grid": (5.940, 116.025), "era5_wave": (6.00, 116.00),
           "mfwam_wave": (5.958, 116.042)}
def hav_km(a, b):
    import math
    (la1, lo1), (la2, lo2) = a, b
    p = math.pi/180
    x = (math.sin((la2-la1)*p/2)**2 + math.cos(la1*p)*math.cos(la2*p)*math.sin((lo2-lo1)*p/2)**2)
    return 2*6371*math.asin(math.sqrt(x))

for fname, (meta, header, rows) in loaded.items():
    if "latitude" not in meta:
        spatial.append(dict(item_id=f"SPA-{fname}", source_path_or_uri=f"data/{fname}",
            verification_status="UNKNOWN",
            evidence_reference="no metadata block in file",
            finding="file carries NO lat/lon; coordinates are code-documented only",
            limitation_or_unknown="cannot file-verify coordinates",
            next_action="read retrieval script parameters",
            file_lat="ABSENT", file_lon="ABSENT", nearest_target="", displacement_km="",
            selection_method="UNKNOWN"))
        continue
    fl, fo = float(meta["latitude"]), float(meta["longitude"])
    best, bestd = None, 1e9
    for name, tgt in TARGETS.items():
        d = hav_km((fl, fo), tgt)
        if d < bestd: best, bestd = name, d
    spatial.append(dict(
        item_id=f"SPA-{fname}", source_path_or_uri=f"data/{fname}",
        verification_status="VERIFIED_FROM_FILE",
        evidence_reference=f"metadata row 2 of {fname}",
        finding=(f"file grid centre ({fl}, {fo}); closest manuscript target '{best}' "
                 f"at {bestd:.2f} km"),
        limitation_or_unknown=("Open-Meteo returns the NEAREST GRID CENTRE for a requested point; "
                               "the requested point is NOT recorded in the file, so displacement "
                               "between request and returned cell is INFERRED, not file-verified. "
                               "No interpolation flag is present."),
        next_action="read lat/lon arguments in the retrieval script to recover the requested point",
        file_lat=fl, file_lon=fo, nearest_target=best,
        displacement_km=round(bestd, 3),
        selection_method="PROVIDER_NEAREST_GRID_CENTRE (inferred from Open-Meteo behaviour)"))

# =============================================================== E. missingness / join
def wave_col(header):
    for c in header:
        if "wave_height" in c or "wave" in c.lower(): return c
    return None

recon = []
for cfg, wavefile in (("PRIMARY", "raw_marine_era5_sea.csv"),
                      ("RESOLUTION", "raw_marine_mfwam.csv")):
    wmeta, wheader, wrows = loaded["raw_weather_sea.csv"]
    mmeta, mheader, mrows = loaded[wavefile]
    wt, mt = wheader[0], mheader[0]
    wc = wave_col(mheader)
    wmap = {r[wt]: r for r in wrows}
    mmap = {r[mt]: r for r in mrows}
    keys_m = list(mmap)
    inner = [k for k in keys_m if k in wmap]
    miss_wave = [k for k in inner if num(mmap[k][wc]) is None]
    miss_in_win = [k for k in miss_wave if (parse_ts(k) and 5 <= parse_ts(k).hour <= 9)]
    usable = [k for k in inner if k not in set(miss_wave)]
    win_all = [k for k in inner if parse_ts(k) and 5 <= parse_ts(k).hour <= 9]
    win_usable = [k for k in usable if parse_ts(k) and 5 <= parse_ts(k).hour <= 9]
    recon.append(dict(
        item_id=f"REC-{cfg}", source_path_or_uri=f"data/raw_weather_sea.csv + data/{wavefile}",
        verification_status="COMPUTED_FROM_FILE",
        evidence_reference=f"inner join on '{wt}' == '{mt}'; wave column '{wc}'",
        finding=(f"wave_rows={len(mrows)}; weather_rows={len(wrows)}; inner_join={len(inner)}; "
                 f"missing_wave={len(miss_wave)}; usable={len(usable)}; "
                 f"window_hours_all={len(win_all)}; window_hours_usable={len(win_usable)}; "
                 f"missing_wave_inside_window={len(miss_in_win)}"),
        limitation_or_unknown=("join reconstructed by this audit from documented column names; "
                               "the original code path uses pandas.merge and was NOT re-executed"),
        next_action="Step 3: confirm the original merge semantics (how/validate) line by line",
        config=cfg, wave_file=wavefile, wave_column=wc,
        wave_rows=len(mrows), weather_rows=len(wrows), inner_join_rows=len(inner),
        join_cardinality="1:1 (no duplicate time keys on either side)"
            if len(set(wmap)) == len(wrows) and len(set(mmap)) == len(mrows) else "NON_1:1",
        missing_wave_total=len(miss_wave),
        missing_wave_timestamps="; ".join(miss_wave) if len(miss_wave) <= 20 else f"{len(miss_wave)} ts",
        missing_wave_in_window=len(miss_in_win),
        missing_wave_in_window_timestamps="; ".join(miss_in_win),
        usable_records=len(usable),
        window_hours_before_exclusion=len(win_all),
        window_hours_after_exclusion=len(win_usable)))
    status["computed_counts"][cfg] = dict(
        inner_join=len(inner), usable=len(usable),
        window_hours_all=len(win_all), window_hours_usable=len(win_usable),
        missing_wave=len(miss_wave), missing_wave_in_window=len(miss_in_win))
missing.extend(recon)

# marine warning column audit
warn_cols = []
for fname, (meta, header, rows) in loaded.items():
    for c in header:
        if "warn" in c.lower() or "marine" in c.lower():
            warn_cols.append(f"{fname}::{c}")
missing.append(dict(
    item_id="REC-WARN", source_path_or_uri="all raw files",
    verification_status="VERIFIED_FROM_FILE" if not warn_cols else "PARTIALLY_VERIFIED",
    evidence_reference="column-name scan of every loaded header",
    finding=(f"no marine-warning column exists in any raw file (scanned {len(loaded)} files)"
             if not warn_cols else f"candidate columns: {warn_cols}"),
    limitation_or_unknown=("Because no warning column exists, any conference treatment of "
                           "historical marine warnings is a MODELLING ASSUMPTION. A constant "
                           "SAFE must NOT be read as observed absence of warnings."),
    next_action="state the assumption explicitly in Step 3 rule reconstruction",
    config="n/a", wave_file="", wave_column="", wave_rows="", weather_rows="",
    inner_join_rows="", join_cardinality="", missing_wave_total="",
    missing_wave_timestamps="", missing_wave_in_window="",
    missing_wave_in_window_timestamps="", usable_records="",
    window_hours_before_exclusion="", window_hours_after_exclusion=""))

# =============================================================== F. lineage
LIN = [
 ("LIN-01","scripts/openmeteo_raw_download.py","retrieval","weather/wind/precip raw pull"),
 ("LIN-02","scripts/openmeteo_raw_rainfall.py","retrieval","rainfall raw pull (land cell, superseded)"),
 ("LIN-03","scripts/collect_raw_v2.py","retrieval","v2 sea-cell collection"),
 ("LIN-04","scripts/tide_marea_download.py","retrieval","tide pull (not used by replay)"),
 ("LIN-05","scripts/canonical_gt.py","transform","shared solar/ground-truth module"),
 ("LIN-06","scripts/historical_replay.py","transform","deterministic replay; selects v1 land vs v2 sea config"),
 ("LIN-07","scripts/condition_comparison.py","analysis","PRIMARY vs RESOLUTION comparison; resolves P21-P24"),
 ("LIN-08","scripts/diagnostic_binding.py","analysis","binding diagnostics"),
 ("LIN-09","data/prediction-register.csv","artefact","pre-registered predictions P21-P24"),
 ("LIN-10","data/solar/solar-events-daily.csv","artefact","C-3 frozen solar artefact used by g_t"),
]
for iid, rel, kind, what in LIN:
    p = ROOT / rel
    lineage.append(dict(
        item_id=iid, source_path_or_uri=rel,
        verification_status="VERIFIED_FROM_FILE" if p.exists() else "MISSING",
        evidence_reference=f"{rel} present on disk" if p.exists() else "not found",
        finding=f"{kind}: {what}" + (f"; sha256={sha256(p)[:16]}..." if p.exists() else ""),
        limitation_or_unknown=("script text read; NOT re-executed in this step"
                               if p.exists() else "artefact absent"),
        next_action="Step 3 reads rule logic from this file" if p.exists() else "locate artefact",
        artefact_kind=kind,
        size_bytes=p.stat().st_size if p.exists() else "",
        sha256=sha256(p) if p.exists() else ""))

# =============================================================== write
def dump(name, rows_):
    if not rows_: return
    keys, seen = [], set()
    for r in rows_:
        for k in r:
            if k not in seen: seen.add(k); keys.append(k)
    lead = ["item_id","source_path_or_uri","verification_status","evidence_reference",
            "finding","limitation_or_unknown","next_action"]
    cols = lead + [k for k in keys if k not in lead]
    with open(OUT / name, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in rows_: w.writerow(r)
    print(f"  wrote {name} ({len(rows_)} rows)")

dump("02_source_data_inventory.csv", inventory)
dump("03_schema_units_quality.csv", schema)
dump("04_temporal_integrity.csv", temporal)
dump("05_spatial_integrity.csv", spatial)
dump("06_missingness_join_reconciliation.csv", missing)
dump("07_transformation_lineage.csv", lineage)
with open(OUT / "audit_status.json", "w", encoding="utf-8") as fh:
    json.dump(status, fh, indent=2)
print("  wrote audit_status.json")
print(json.dumps(status["computed_counts"], indent=2))
