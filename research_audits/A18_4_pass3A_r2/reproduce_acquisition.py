#!/usr/bin/env python3
"""
A18.4 Pass 3A — reproducible acquisition and verification.

STATUS: this script has NEVER completed an acquisition. Every provider host was
refused at the executing environment's egress proxy (HTTP 403), so Track A and
Track B are both HOLD. The script is written to be run from an environment with
provider access; it verifies and hashes whatever it genuinely retrieves and
writes nothing it did not retrieve.

Credentials are read from ENVIRONMENT VARIABLES only and are never written to
any file or printed:
    COPERNICUSMARINE_SERVICE_USERNAME
    COPERNICUSMARINE_SERVICE_PASSWORD

Safety: every download is bounded. --probe performs status-only checks with no
payload. Nothing runs against a provider unless a track flag is passed.

Usage
-----
  python3 reproduce_acquisition.py --probe
  python3 reproduce_acquisition.py --track-a [--lon-min .. --lat-max ..] [--start --end]
  python3 reproduce_acquisition.py --track-b-ndfd
  python3 reproduce_acquisition.py --verify
"""
import argparse, csv, hashlib, json, mimetypes, os, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
RAW = HERE / "raw"; LOGS = HERE / "logs"
RAW.mkdir(exist_ok=True); LOGS.mkdir(exist_ok=True)

PRODUCT_ID  = "GLOBAL_MULTIYEAR_WAV_001_032"
DATASET_ID  = "cmems_mod_glo_wav_my_0.2deg_PT3H-i_202411"   # provider-listed, NOT file-verified
PRODUCT_DOI = "10.48670/moi-00022"

# DEFAULT bounded subset. PROPOSAL ONLY - never executed against the provider.
# Rationale: a 1.0 deg x 1.0 deg box off Kota Kinabalu, Sabah, covering the
# A18.1 grid cells (weather 5.940N/116.025E, ERA5 wave 6.00N/116.00E, MFWAM
# 5.958N/116.042E), over 7 days. At 0.2 deg and 3-hourly that is about
# 6x6 cells x 56 steps - small enough for a proof of acquisition and large
# enough to exercise coordinate ordering, fill values and duplicate checks.
DEFAULT = dict(lon_min=115.5, lon_max=116.5, lat_min=5.5, lat_max=6.5,
               start="2024-01-01T00:00:00", end="2024-01-07T23:59:59",
               variables=["VHM0", "VTM10", "VMDR"])   # names to CONFIRM from the file
HOSTS = {
 "copernicus_description": f"https://data.marine.copernicus.eu/product/{PRODUCT_ID}/description",
 "copernicus_download":    f"https://data.marine.copernicus.eu/product/{PRODUCT_ID}/download",
 "nws_alerts_api":         "https://api.weather.gov/alerts/active?area=LM",
 "ncei_ndfd_thredds":      "https://www.ncei.noaa.gov/thredds/model/ndfd.html",
 "ncei_ndfd_product":      "https://www.ncei.noaa.gov/products/weather-climate-models/national-digital-forecast-database",
 "aws_ndfd_registry":      "https://registry.opendata.aws/noaa-ndfd/",
 "control_pypi":           "https://pypi.org/simple/",
}
UA = "A18.4-Pass3A-research (set a real contact address before running; NWS requires a User-Agent)"

def now(): return datetime.now(timezone.utc).isoformat()

def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for c in iter(lambda: fh.read(1 << 20), b""): h.update(c)
    return h.hexdigest()

def probe():
    out = []
    for name, url in HOSTS.items():
        r = subprocess.run(["curl", "-sS", "-o", "/dev/null", "-w", "%{http_code}",
                            "--max-time", "20", "-A", UA, url], capture_output=True, text=True)
        code = r.stdout.strip() or "000"
        detail = ""
        if code == "000":
            v = subprocess.run(["curl", "-sS", "-v", "-o", "/dev/null", "--max-time", "20", "-A", UA, url],
                               capture_output=True, text=True).stderr
            detail = next((l.strip().lstrip("< ") for l in v.splitlines()
                           if "403" in l or "Forbidden" in l or "agent proxy" in l), "")
        print(f"  {code}  {name:24s} {detail[:72]}")
        out.append(dict(name=name, url=url, http_code=code, proxy_response=detail))
    p = LOGS / f"connectivity_probe_{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}.json"
    p.write_text(json.dumps(dict(probed_at_utc=now(), probes=out), indent=2), encoding="utf-8")
    print(f"\n  wrote {p.relative_to(HERE)}")
    return all(o["http_code"].startswith("2") for o in out if o["name"] != "control_pypi")

def track_a(a):
    """Copernicus Marine subset via the official Toolbox. Requires an account."""
    # Credentials may come from EITHER environment variables OR a prior
    # `copernicusmarine login`, which stores them in the user's own config.
    # The earlier version demanded env vars only and would have returned a
    # FALSE HOLD for a user who had logged in properly.
    env_creds = bool(os.environ.get("COPERNICUSMARINE_SERVICE_USERNAME")
                     and os.environ.get("COPERNICUSMARINE_SERVICE_PASSWORD"))
    cfg = [Path.home() / ".copernicusmarine" / ".copernicusmarine-credentials",
           Path.home() / ".copernicusmarine-credentials"]
    file_creds = any(c.exists() for c in cfg)
    if not (env_creds or file_creds):
        print("HOLD: no Copernicus credentials found.")
        print("  Either run:  copernicusmarine login")
        print("  or export COPERNICUSMARINE_SERVICE_USERNAME / _PASSWORD.")
        print("  Never put credentials in a file in this folder, or in a report.")
        return False
    print(f"  credentials: {'environment variables' if env_creds else 'copernicusmarine login config'}")
    try:
        import copernicusmarine as cm
    except ImportError:
        print("HOLD: `pip install copernicusmarine` (pinned in requirements.txt), then re-run.")
        return False
    dest = RAW / "copernicus"
    dest.mkdir(parents=True, exist_ok=True)
    # The dataset id carries a release suffix (…_202411) that the provider bumps.
    # It is overridable at the CLI so a suffix change never requires editing a
    # file that the SHA-256 manifest covers.
    ds_id = getattr(a, "dataset_id", None) or DATASET_ID
    if ds_id != DATASET_ID:
        print(f"  dataset id OVERRIDDEN at the CLI: {ds_id}  (built-in default: {DATASET_ID})")
    print(f"  requesting {ds_id}")
    print(f"  bbox lon [{a.lon_min},{a.lon_max}] lat [{a.lat_min},{a.lat_max}]  {a.start} .. {a.end}")
    t0 = now()
    res = cm.subset(dataset_id=ds_id, variables=a.variables,
                    minimum_longitude=a.lon_min, maximum_longitude=a.lon_max,
                    minimum_latitude=a.lat_min, maximum_latitude=a.lat_max,
                    start_datetime=a.start, end_datetime=a.end,
                    output_directory=str(dest), force_download=True)
    files = sorted(dest.glob("*.nc"))
    if not files:
        print("HOLD: the Toolbox returned no NetCDF file. Nothing is recorded.")
        return False
    rows = []
    for f in files:
        rows.append(dict(item_id=f"RAW-A-{len(rows)+1:02d}", relative_path=str(f.relative_to(HERE)),
            sha256=sha256(f), byte_size=f.stat().st_size,
            mime_type=mimetypes.guess_type(f.name)[0] or "application/x-netcdf",
            download_query=(f"copernicusmarine.subset(dataset_id='{ds_id}', variables={a.variables}, "
                f"lon=[{a.lon_min},{a.lon_max}], lat=[{a.lat_min},{a.lat_max}], "
                f"time=['{a.start}','{a.end}'])"),
            provider="Copernicus Marine Service", product_or_dataset_id=f"{PRODUCT_ID} / {ds_id}",
            retrieved_at_utc=t0,
            provenance_note=(f"Toolbox result={res}; DOI {PRODUCT_DOI}; REANALYSIS HINDSIGHT PRODUCT - "
                "not an issuance-time forecast and not fisher safety information; tier R0 ONLY")))
        print(f"  got {f.name}  {f.stat().st_size:,} bytes  sha256 {rows[-1]['sha256'][:16]}...")
    write_manifest(rows)
    qa = qa_netcdf(files, a)
    # r3 review finding: a download alone is not a data-quality PASS. Track A
    # succeeds only if QA RAN and PASSED and the manifest re-verifies on disk.
    v = verify()
    ok = bool(qa.get("qa_pass")) and v == EXIT_OK
    if not ok:
        print(f"  TRACK A NOT A PASS: qa_ran={qa.get('qa_ran')} qa_pass={qa.get('qa_pass')} "
              f"verify_exit={v} ({qa.get('reason','')})")
    return ok

def qa_netcdf(files, a=None):   # returns a status dict, never None
    """Track A step 5: verify from the FILE. Reports only what it reads.

    Audit finding F3: the earlier version read raw attributes with
    decode_cf=False, which is NOT time decoding, and did not test the requested
    bounds, fill values separately from NaN, time gaps, duplicate coordinates or
    the expected variable set. All of those are covered below. The following is still NOT covered and
    must not be claimed as checked: physical plausibility against an external
    reference, cross-variable consistency, and provider semantic correctness."""
    try:
        import xarray as xr, numpy as np
    except ImportError:
        print("  QA NOT RUN: xarray/numpy not installed. Metadata stays NOT FILE-VERIFIED.")
        # r3 review finding: a skipped QA previously left track_a returning True.
        return dict(qa_ran=False, qa_pass=False, reason="xarray/numpy unavailable",
                    rows=0, bounds_failures=[], decode_errors=[])
    rows = []
    for f in files:
        ds = xr.open_dataset(f, decode_cf=False)
        for vn, v in ds.variables.items():
            arr = np.asarray(v.values, dtype="float64") if v.dtype.kind in "fiu" else None
            fill = v.attrs.get("_FillValue", v.attrs.get("missing_value"))
            nan = int(np.isnan(arr).sum()) if arr is not None else ""
            nfill = ""                                   # counted SEPARATELY from NaN (F3)
            if arr is not None and fill is not None:
                try: nfill = int((arr == float(fill)).sum())
                except (TypeError, ValueError): nfill = "uncomparable"
            rows.append(dict(item_id=f"QA-{len(rows)+1:03d}", file=f.name, variable=vn,
                standard_name=v.attrs.get("standard_name", "ABSENT"),
                long_name=v.attrs.get("long_name", "ABSENT"),
                units=v.attrs.get("units", "ABSENT"),
                dims=str(v.dims), shape=str(v.shape), dtype=str(v.dtype),
                fill_value=str(fill) if fill is not None else "ABSENT",
                nan_count=nan, fill_value_hits=nfill,
                vmin=(float(np.nanmin(arr)) if arr is not None and arr.size else ""),
                vmax=(float(np.nanmax(arr)) if arr is not None and arr.size else ""),
                verification_status="COMPUTED_FROM_FILE"))
        for c in ("time", "latitude", "longitude", "lat", "lon"):
            if c in ds.coords:
                cv = np.asarray(ds[c].values)
                rows.append(dict(item_id=f"QA-{len(rows)+1:03d}", file=f.name, variable=f"COORD:{c}",
                    standard_name="", long_name="", units=ds[c].attrs.get("units", "ABSENT"),
                    dims=str(ds[c].dims), shape=str(cv.shape), dtype=str(cv.dtype),
                    fill_value="", nan_count="",
                    vmin=str(cv.min()) if cv.size else "", vmax=str(cv.max()) if cv.size else "",
                    verification_status=("MONOTONIC_INCREASING" if cv.size > 1 and bool((cv[1:] > cv[:-1]).all())
                                         else "NOT_MONOTONIC_OR_SINGLETON")
                                        + f"; duplicates={int(cv.size - len(set(cv.tolist())))}"))
        # --- CF time decoding, as a SECOND open with decoding ON (F3)
        try:
            import numpy as _np
            dsd = xr.open_dataset(f, decode_cf=True)
            if "time" in dsd.coords:
                tv = dsd["time"].values
                gaps = ""
                if tv.size > 1:
                    d = _np.diff(tv).astype("timedelta64[s]").astype("int64")
                    uq = sorted(set(d.tolist()))
                    gaps = f"steps_s={uq[:5]}{'…' if len(uq)>5 else ''}; irregular={int((d!=d[0]).sum())}"
                rows.append(dict(item_id=f"QA-{len(rows)+1:03d}", file=f.name, variable="DECODED:time",
                    standard_name="", long_name="", units="CF-decoded datetime64",
                    dims=str(dsd["time"].dims), shape=str(tv.shape), dtype=str(tv.dtype),
                    fill_value="", nan_count="", fill_value_hits="",
                    vmin=str(tv.min()), vmax=str(tv.max()),
                    verification_status=f"CF-DECODED; {gaps}; duplicate_times={int(tv.size-len(set(tv.tolist())))}"))
                if a is not None:
                    # r3 review finding: this row previously only DESCRIBED the
                    # requested window and the decoded extent. It now EVALUATES
                    # containment and emits within_request, as lat/lon already did.
                    req_lo = _np.datetime64(str(a.start).replace(" ", "T"))
                    req_hi = _np.datetime64(str(a.end).replace(" ", "T"))
                    within = bool(tv.min() >= req_lo and tv.max() <= req_hi)
                    rows.append(dict(item_id=f"QA-{len(rows)+1:03d}", file=f.name,
                        variable="BOUNDS:time_vs_request", standard_name="", long_name="", units="",
                        dims="", shape="", dtype="", fill_value="", nan_count="", fill_value_hits="",
                        vmin=str(tv.min()), vmax=str(tv.max()),
                        verification_status=(f"requested [{req_lo} .. {req_hi}]; "
                                             f"within_request={within}")))
            for cn, lo, hi in (("latitude", getattr(a,"lat_min",None), getattr(a,"lat_max",None)),
                               ("longitude", getattr(a,"lon_min",None), getattr(a,"lon_max",None))):
                if a is not None and cn in dsd.coords and lo is not None:
                    cv = dsd[cn].values
                    rows.append(dict(item_id=f"QA-{len(rows)+1:03d}", file=f.name,
                        variable=f"BOUNDS:{cn}_vs_request", standard_name="", long_name="", units="",
                        dims="", shape=str(cv.shape), dtype="", fill_value="", nan_count="",
                        fill_value_hits="", vmin=str(cv.min()), vmax=str(cv.max()),
                        verification_status=(f"requested [{lo},{hi}]; "
                                             f"within_request={bool(cv.min()>=lo and cv.max()<=hi)}")))
            got, want = set(dsd.data_vars), set(a.variables) if a is not None else set()
            rows.append(dict(item_id=f"QA-{len(rows)+1:03d}", file=f.name,
                variable="EXPECTED_VARIABLE_SET", standard_name="", long_name="", units="", dims="",
                shape="", dtype="", fill_value="", nan_count="", fill_value_hits="", vmin="", vmax="",
                verification_status=(f"requested={sorted(want)}; present={sorted(got)}; "
                                     f"missing={sorted(want-got)}; unexpected={sorted(got-want)}")))
            dsd.close()
        except Exception as e:
            rows.append(dict(item_id=f"QA-{len(rows)+1:03d}", file=f.name, variable="DECODE_ERROR",
                standard_name="", long_name="", units="", dims="", shape="", dtype="", fill_value="",
                nan_count="", fill_value_hits="", vmin="", vmax="",
                verification_status=f"CF decoding FAILED: {type(e).__name__}: {e}"))
        ds.close()
    out = HERE / "processed" / "netcdf_qa.csv"
    out.parent.mkdir(exist_ok=True)
    cols = []
    for r in rows:
        for k in r:
            if k not in cols: cols.append(k)
    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader(); w.writerows(rows)
    bounds_fail = [r["variable"] for r in rows
                   if r["variable"].startswith("BOUNDS:") and "within_request=False" in r["verification_status"]]
    decode_err = [r["file"] for r in rows if r["variable"] == "DECODE_ERROR"]
    status = dict(qa_ran=True, qa_pass=(not bounds_fail and not decode_err),
                  reason=("" if not (bounds_fail or decode_err)
                          else f"bounds_failures={bounds_fail}; decode_errors={decode_err}"),
                  rows=len(rows), bounds_failures=bounds_fail, decode_errors=decode_err)
    print(f"  wrote {out.relative_to(HERE)} ({len(rows)} rows, parent hashes in 02_raw_file_manifest.csv)")
    print(f"  QA status: ran={status['qa_ran']} pass={status['qa_pass']} {status['reason']}")
    json.dump(status, open(HERE / "processed" / "qa_status.json", "w"), indent=2)
    return status

def track_b_ndfd():
    """NCEI NDFD is the viable archive for the 2020-2024 window.
    The NWS /alerts API is NOT: it retains seven days only."""
    print("Track B target: NCEI NDFD archive (NOT the NWS alerts API).")
    print("  Reason: the NWS /alerts endpoint retains SEVEN DAYS of alerts and the provider")
    print("  directs users to NCEI for an official CAP archive. A current alert is authentic")
    print("  but is NOT a historical 2020-2024 record and must never be presented as one.")
    print("  NDFD periods of record (provider-stated): WMO header 2004-06-06 to present;")
    print("  AWS Open Data mirror 2020-04-16 to present.")
    print("  Endpoints to try, in order:")
    for u in ("https://registry.opendata.aws/noaa-ndfd/",
              "https://www.ncei.noaa.gov/thredds/model/ndfd.html",
              "https://www.ncei.noaa.gov/oa/prod-model/index.html#national-digital-forecast-database/"):
        print(f"    {u}")
    print("\n  NOT IMPLEMENTED as an automatic download: the exact object layout must be read from")
    print("  the AWS registry first, and a blind recursive fetch would be an unbounded download.")
    print("  HOLD. No bytes retrieved, nothing recorded.")
    return False

MANIFEST_COLS = ["item_id","relative_path","sha256","byte_size","mime_type","download_query",
                 "provider","product_or_dataset_id","retrieved_at_utc","provenance_note"]

def write_manifest(rows):
    """Deterministic rebuild keyed on relative_path. Audit finding F4: the
    previous append left duplicate rows and stale hashes across reruns.

    A rerun REPLACES the row for a path it re-downloaded, KEEPS rows whose file
    is still on disk, and DROPS rows whose file is gone. Output is sorted by
    path with item_id reassigned, so the same set of files always produces a
    byte-identical manifest regardless of acquisition order."""
    p = HERE / "02_raw_file_manifest.csv"
    keep, drifted = {}, []
    if p.exists():
        for r in csv.DictReader(open(p, encoding="utf-8")):
            f = HERE / r["relative_path"]
            if not f.exists():
                continue
            # r3 review finding: retained rows previously kept their OLD hash, so a
            # file changed on disk stayed stale until --verify happened to run.
            h, b = sha256(f), f.stat().st_size
            if h != r.get("sha256") or str(b) != str(r.get("byte_size")):
                drifted.append(r["relative_path"])
                r = dict(r, sha256=h, byte_size=b,
                         provenance_note=(r.get("provenance_note","") +
                                          " | HASH RECOMPUTED ON REBUILD: file changed on disk since"
                                          " it was recorded"))
            keep[r["relative_path"]] = r
    for r in rows:
        keep[r["relative_path"]] = r
    out = sorted(keep.values(), key=lambda r: r["relative_path"])
    for i, r in enumerate(out, 1):
        r["item_id"] = f"RAW-{i:03d}"
    with open(p, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=MANIFEST_COLS, extrasaction="ignore")
        w.writeheader(); w.writerows(out)
    print(f"  manifest rebuilt deterministically: {len(out)} rows, no duplicates")
    if drifted:
        print(f"  WARNING: {len(drifted)} retained row(s) had stale hashes, recomputed: {drifted}")
    return out

# Exit statuses. Audit finding F2: an empty manifest previously returned 0, so
# "nothing was acquired" was indistinguishable from "everything verified".
EXIT_OK             = 0   # manifest non-empty AND every row matches disk
EXIT_MISMATCH       = 1   # a manifest row disagrees with the file on disk
EXIT_NO_ACQUISITION = 3   # manifest empty: consistent, but nothing was acquired

def verify():
    """Re-verify the manifest. Returns an exit status, not a boolean.

    Manifest CONSISTENCY and acquisition SUCCESS are deliberately separate: an
    empty manifest is internally consistent and is still a failed acquisition."""
    p = HERE / "02_raw_file_manifest.csv"
    rows = list(csv.DictReader(open(p, encoding="utf-8"))) if p.exists() else []
    if not rows:
        nf = len([x for x in RAW.rglob("*") if x.is_file() and x.name != "README.md"])
        print("  02_raw_file_manifest.csv is HEADER ONLY and raw/ holds "
              f"{nf} data files. Manifest is CONSISTENT but NOTHING WAS ACQUIRED.")
        print(f"  Tracks A and B are HOLD. Exit status {EXIT_NO_ACQUISITION} (EXIT_NO_ACQUISITION).")
        return EXIT_NO_ACQUISITION
    ok = True
    for r in rows:
        f = HERE / r["relative_path"]
        if not f.exists(): print(f"  MISSING {r['relative_path']}"); ok = False; continue
        h, b = sha256(f), f.stat().st_size
        good = (h == r["sha256"] and str(b) == str(r["byte_size"]))
        ok &= good
        print(f"  {'OK  ' if good else 'FAIL'} {r['relative_path']}  {b:,} bytes")
    print(f"\n  manifest verification over {len(rows)} rows: {'PASS' if ok else 'FAIL'}")
    return EXIT_OK if ok else EXIT_MISMATCH

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--probe", action="store_true", help="status-only connectivity check, no payload")
    ap.add_argument("--track-a", action="store_true", help="Copernicus subset (needs account + Toolbox)")
    ap.add_argument("--track-b-ndfd", action="store_true", help="print the NDFD route and HOLD")
    ap.add_argument("--verify", action="store_true", help="re-hash every manifest entry")
    ap.add_argument("--dataset-id", default=None,
                    help=f"override the dataset id (default {DATASET_ID}); the "
                         "release suffix is provider-controlled and may change")
    for k, v in DEFAULT.items():
        if k != "variables": ap.add_argument(f"--{k.replace('_','-')}", default=v, type=type(v))
    ap.add_argument("--variables", nargs="+", default=DEFAULT["variables"])
    a = ap.parse_args()
    if not any([a.probe, a.track_a, a.track_b_ndfd, a.verify]):
        ap.print_help(); sys.exit(0)
    rc = 0
    if a.probe:        probe()                            # probe never fails the run
    if a.track_a:      rc = max(rc, EXIT_OK if track_a(a) else 2)
    if a.track_b_ndfd: rc = max(rc, 2)                    # documented route, always HOLD
    if a.verify:       rc = max(rc, verify())
    sys.exit(rc)
