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
    if not (os.environ.get("COPERNICUSMARINE_SERVICE_USERNAME")
            and os.environ.get("COPERNICUSMARINE_SERVICE_PASSWORD")):
        print("HOLD: Copernicus credentials absent from the environment.")
        print("  Register free at https://data.marine.copernicus.eu then export")
        print("  COPERNICUSMARINE_SERVICE_USERNAME and COPERNICUSMARINE_SERVICE_PASSWORD.")
        print("  Credentials must NEVER be placed in a file or a report.")
        return False
    try:
        import copernicusmarine as cm
    except ImportError:
        print("HOLD: `pip install copernicusmarine` (pinned in requirements.txt), then re-run.")
        return False
    dest = RAW / "copernicus"
    dest.mkdir(parents=True, exist_ok=True)
    print(f"  requesting {DATASET_ID}")
    print(f"  bbox lon [{a.lon_min},{a.lon_max}] lat [{a.lat_min},{a.lat_max}]  {a.start} .. {a.end}")
    t0 = now()
    res = cm.subset(dataset_id=DATASET_ID, variables=a.variables,
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
            download_query=(f"copernicusmarine.subset(dataset_id='{DATASET_ID}', variables={a.variables}, "
                f"lon=[{a.lon_min},{a.lon_max}], lat=[{a.lat_min},{a.lat_max}], "
                f"time=['{a.start}','{a.end}'])"),
            provider="Copernicus Marine Service", product_or_dataset_id=f"{PRODUCT_ID} / {DATASET_ID}",
            retrieved_at_utc=t0,
            provenance_note=(f"Toolbox result={res}; DOI {PRODUCT_DOI}; REANALYSIS HINDSIGHT PRODUCT - "
                "not an issuance-time forecast and not fisher safety information; tier R0 ONLY")))
        print(f"  got {f.name}  {f.stat().st_size:,} bytes  sha256 {rows[-1]['sha256'][:16]}...")
    append_manifest(rows)
    qa_netcdf(files)
    return True

def qa_netcdf(files):
    """Track A step 5: verify from the FILE. Reports only what it reads."""
    try:
        import xarray as xr, numpy as np
    except ImportError:
        print("  QA skipped: xarray/numpy not installed. Metadata stays NOT FILE-VERIFIED.")
        return
    rows = []
    for f in files:
        ds = xr.open_dataset(f, decode_cf=False)
        for vn, v in ds.variables.items():
            arr = np.asarray(v.values, dtype="float64") if v.dtype.kind in "fiu" else None
            fill = v.attrs.get("_FillValue", v.attrs.get("missing_value"))
            nan = int(np.isnan(arr).sum()) if arr is not None else ""
            rows.append(dict(item_id=f"QA-{len(rows)+1:03d}", file=f.name, variable=vn,
                standard_name=v.attrs.get("standard_name", "ABSENT"),
                long_name=v.attrs.get("long_name", "ABSENT"),
                units=v.attrs.get("units", "ABSENT"),
                dims=str(v.dims), shape=str(v.shape), dtype=str(v.dtype),
                fill_value=str(fill) if fill is not None else "ABSENT",
                nan_count=nan,
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
        ds.close()
    out = HERE / "processed" / "netcdf_qa.csv"
    out.parent.mkdir(exist_ok=True)
    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    print(f"  wrote {out.relative_to(HERE)} ({len(rows)} rows, parent hashes in 02_raw_file_manifest.csv)")

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

def append_manifest(rows):
    p = HERE / "02_raw_file_manifest.csv"
    cols = ["item_id","relative_path","sha256","byte_size","mime_type","download_query","provider",
            "product_or_dataset_id","retrieved_at_utc","provenance_note"]
    existing = list(csv.DictReader(open(p, encoding="utf-8"))) if p.exists() else []
    with open(p, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore"); w.writeheader()
        w.writerows(existing + rows)

def verify():
    """Deterministic re-verification: every manifest row must match the file on disk."""
    p = HERE / "02_raw_file_manifest.csv"
    rows = list(csv.DictReader(open(p, encoding="utf-8"))) if p.exists() else []
    if not rows:
        print("  02_raw_file_manifest.csv is HEADER ONLY. raw/ holds "
              f"{len(list(RAW.rglob('*')))} entries. Nothing to verify. Tracks A and B are HOLD.")
        return True
    ok = True
    for r in rows:
        f = HERE / r["relative_path"]
        if not f.exists(): print(f"  MISSING {r['relative_path']}"); ok = False; continue
        h, b = sha256(f), f.stat().st_size
        good = (h == r["sha256"] and str(b) == str(r["byte_size"]))
        ok &= good
        print(f"  {'OK  ' if good else 'FAIL'} {r['relative_path']}  {b:,} bytes")
    print(f"\n  manifest verification: {'PASS' if ok else 'FAIL'}")
    return ok

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--probe", action="store_true", help="status-only connectivity check, no payload")
    ap.add_argument("--track-a", action="store_true", help="Copernicus subset (needs account + Toolbox)")
    ap.add_argument("--track-b-ndfd", action="store_true", help="print the NDFD route and HOLD")
    ap.add_argument("--verify", action="store_true", help="re-hash every manifest entry")
    for k, v in DEFAULT.items():
        if k != "variables": ap.add_argument(f"--{k.replace('_','-')}", default=v, type=type(v))
    ap.add_argument("--variables", nargs="+", default=DEFAULT["variables"])
    a = ap.parse_args()
    if not any([a.probe, a.track_a, a.track_b_ndfd, a.verify]):
        ap.print_help(); sys.exit(0)
    rc = 0
    if a.probe:        rc |= 0 if probe() else 0        # probe never fails the run
    if a.track_a:      rc |= 0 if track_a(a) else 2
    if a.track_b_ndfd: rc |= 0 if track_b_ndfd() else 2
    if a.verify:       rc |= 0 if verify() else 1
    sys.exit(rc)
