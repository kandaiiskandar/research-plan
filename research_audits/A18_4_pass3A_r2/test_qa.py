#!/usr/bin/env python3
"""
Behavioural tests for the Track A QA, on SYNTHETIC NetCDF fixtures.

r3 review finding: the internal G-22 gate searched the source text for keywords,
which cannot tell whether a check EVALUATES anything. It passed while
BOUNDS:time_vs_request only described the window instead of testing containment.
These tests build real NetCDF files with known properties and assert on the
values qa_netcdf() actually produces.

The fixtures are synthetic and clearly labelled. They are written to a temporary
directory, never to raw/, and they are not provider data.

Run:  python3 test_qa.py
"""
import importlib.util, json, sys, tempfile, unittest
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
_s = importlib.util.spec_from_file_location("ra", HERE / "reproduce_acquisition.py")
RA = importlib.util.module_from_spec(_s); _s.loader.exec_module(RA)

try:
    import numpy as np, xarray as xr
except ImportError as e:  # noqa: F401
    # Exit 3 == BLOCKED: the tests could not RUN. Distinct from exit 1 == a test
    # FAILED. Both are non-zero, so neither is ever read as a pass; the caller
    # must not be able to confuse "QA logic is wrong" with "this machine lacks
    # netCDF4", which is what a single failure code did.
    import json as _j
    (HERE / "logs").mkdir(exist_ok=True)
    _j.dump(dict(tests_run=0, failures=0, errors=0, passed=0, ok=False,
                 blocked=True, blocked_reason=f"test dependency absent: {e}"),
            open(HERE / "logs" / "qa_behavioural_tests.json", "w"), indent=2)
    print(f"BLOCKED: cannot run the behavioural QA tests -- {e}")
    print("  pip3 install -r requirements.txt   then re-run")
    sys.exit(3)

def fixture(path, t0="2024-01-01", nt=8, lat=(5.6, 6.4), lon=(115.6, 116.4),
            varname="VHM0", with_fill=True):
    """A small synthetic wave-like file: 3-hourly times, a 3x3 grid."""
    times = np.array([np.datetime64(t0) + np.timedelta64(3 * i, "h") for i in range(nt)])
    la = np.linspace(lat[0], lat[1], 3)
    lo = np.linspace(lon[0], lon[1], 3)
    data = np.random.default_rng(0).uniform(0.2, 2.0, size=(nt, 3, 3))
    if with_fill:
        data[0, 0, 0] = np.nan
    ds = xr.Dataset({varname: (("time", "latitude", "longitude"), data,
                               {"standard_name": "sea_surface_wave_significant_height",
                                "long_name": "significant wave height", "units": "m"})},
                    coords={"time": times, "latitude": la, "longitude": lo})
    ds[varname].encoding["_FillValue"] = -9999.0
    ds.to_netcdf(path)
    ds.close()
    return path

def run_qa(tmp, **req):
    a = SimpleNamespace(lon_min=115.5, lon_max=116.5, lat_min=5.5, lat_max=6.5,
                        start="2024-01-01T00:00:00", end="2024-01-07T23:59:59",
                        variables=["VHM0"])
    for k, v in req.items(): setattr(a, k, v)
    RA.HERE = tmp                      # keep all QA output inside the temp dir
    (tmp / "processed").mkdir(exist_ok=True)
    files = sorted(tmp.glob("*.nc"))
    status = RA.qa_netcdf(files, a)
    import csv as _csv
    rows = list(_csv.DictReader(open(tmp / "processed" / "netcdf_qa.csv", encoding="utf-8")))
    return status, rows

def find(rows, var):
    return next((r for r in rows if r["variable"] == var), None)


class TimeBounds(unittest.TestCase):
    def test_time_within_request_is_true_when_inside(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d); fixture(tmp / "in.nc")
            st, rows = run_qa(tmp)
            r = find(rows, "BOUNDS:time_vs_request")
            self.assertIsNotNone(r, "no BOUNDS:time_vs_request row was produced")
            self.assertIn("within_request=", r["verification_status"],
                          "the time bounds row does not EVALUATE containment")
            self.assertIn("within_request=True", r["verification_status"])
            self.assertTrue(st["qa_pass"])

    def test_time_within_request_is_false_when_outside(self):
        """The decisive test: data outside the requested window must FAIL."""
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d); fixture(tmp / "out.nc", t0="2024-03-01")
            st, rows = run_qa(tmp)
            r = find(rows, "BOUNDS:time_vs_request")
            self.assertIn("within_request=False", r["verification_status"])
            self.assertFalse(st["qa_pass"], "QA passed despite times outside the requested window")
            self.assertIn("BOUNDS:time_vs_request", st["bounds_failures"])


class SpatialBounds(unittest.TestCase):
    def test_lat_lon_within_request_true(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d); fixture(tmp / "in.nc")
            st, rows = run_qa(tmp)
            for c in ("BOUNDS:latitude_vs_request", "BOUNDS:longitude_vs_request"):
                self.assertIn("within_request=True", find(rows, c)["verification_status"])

    def test_lon_outside_request_fails(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d); fixture(tmp / "wide.nc", lon=(110.0, 120.0))
            st, rows = run_qa(tmp)
            self.assertIn("within_request=False",
                          find(rows, "BOUNDS:longitude_vs_request")["verification_status"])
            self.assertFalse(st["qa_pass"])


class DecodingAndVars(unittest.TestCase):
    def test_time_is_cf_decoded_with_step_and_duplicate_reporting(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d); fixture(tmp / "in.nc")
            st, rows = run_qa(tmp)
            r = find(rows, "DECODED:time")
            self.assertIn("CF-DECODED", r["verification_status"])
            self.assertIn("steps_s=[10800]", r["verification_status"])   # 3-hourly
            self.assertIn("duplicate_times=0", r["verification_status"])

    def test_missing_variable_is_reported(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d); fixture(tmp / "in.nc", varname="VHM0")
            st, rows = run_qa(tmp, variables=["VHM0", "VTM10"])
            r = find(rows, "EXPECTED_VARIABLE_SET")
            self.assertIn("missing=['VTM10']", r["verification_status"])

    def test_nan_and_fill_are_counted_separately(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d); fixture(tmp / "in.nc")
            st, rows = run_qa(tmp)
            v = next(r for r in rows if r["variable"] == "VHM0" and r["item_id"].startswith("QA-"))
            self.assertNotEqual(v["nan_count"], "", "NaN count missing")
            self.assertIn("fill_value_hits", v, "fill-value hits are not a separate column")


class QAStatusGate(unittest.TestCase):
    def test_status_dict_shape(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d); fixture(tmp / "in.nc")
            st, _ = run_qa(tmp)
            for k in ("qa_ran", "qa_pass", "rows", "bounds_failures", "decode_errors"):
                self.assertIn(k, st)
            self.assertTrue(st["qa_ran"])


if __name__ == "__main__":
    r = unittest.main(exit=False, verbosity=2).result
    json.dump(dict(tests_run=r.testsRun, failures=len(r.failures), errors=len(r.errors),
                   passed=r.testsRun - len(r.failures) - len(r.errors),
                   ok=r.wasSuccessful(), blocked=False, blocked_reason=None),
              open(HERE / "logs" / "qa_behavioural_tests.json", "w"), indent=2)
    sys.exit(0 if r.wasSuccessful() else 1)
