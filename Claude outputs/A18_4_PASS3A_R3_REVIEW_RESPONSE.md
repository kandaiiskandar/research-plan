# A18.4 Pass 3A — Response to the r2 Correction-Package Review

**22 November 2026.** Review dated 22 November 2026 on `A18_4_PASS3A_R2_AUDIT_RESPONSE.md` and `A18_4_pass3A_r2.tar.gz`.

**The verdict is accepted in full and unchanged: Track A HOLD, Track B HOLD, acquisition HOLD.** Nothing below acquires anything.

The open QA defect was real, and the reviewer's diagnosis of *why my own gate missed it* is the more useful half of the finding.

---

## 1. The open defect: time bounds were described, not evaluated

**Confirmed exactly.** `BOUNDS:time_vs_request` printed the requested window and the decoded extent and stopped there. Latitude and longitude emitted `within_request=True/False`; time emitted nothing to test. So the claim that temporal bounds were checked was stronger than the code, and a file whose timestamps fell outside the requested window would have passed QA silently.

Fixed: the row now compares decoded `datetime64` extents against the request and emits `within_request`, and that boolean feeds the QA pass/fail status.

## 2. The reason it survived: G-22 was a keyword search

**This is the part that mattered.** G-22 searched the source for the literal strings `decode_cf=True` and `BOUNDS:time_vs_request`. Both were present. The gate passed while the check it claimed to verify evaluated nothing.

A static source search cannot distinguish a check that runs from one that mentions the right words. That is the **third variant of the same failure mode in this project**: a verification artefact asserting something it does not test. A18.2-R was hand-written prose drifting from computed artefacts; `P3A-11` was audit guards that cried wolf; this is a guard that stayed silent when it should have fired. Same root cause, different direction.

**G-22 now executes `test_qa.py`** — 8 behavioural tests against synthetic NetCDF fixtures built with xarray, written to a temp directory, never to `raw/`, and clearly labelled synthetic. Coverage:

| Test | Asserts |
|---|---|
| time inside the window | `within_request=True`, `qa_pass=True` |
| **time outside the window** | **`within_request=False`, `qa_pass=False`, listed in `bounds_failures`** |
| lat/lon inside | `within_request=True` on both |
| longitude outside | `within_request=False`, `qa_pass=False` |
| CF decoding | `CF-DECODED`, `steps_s=[10800]` for 3-hourly, `duplicate_times=0` |
| missing variable | `missing=['VTM10']` reported |
| NaN vs fill | counted in separate columns |
| status shape | `qa_ran`, `qa_pass`, `rows`, `bounds_failures`, `decode_errors` present |

The second row is the decisive one: it is the test that would have caught the original defect. **8/8 pass.** Missing test dependencies make G-22 **fail**, not silently pass.

## 3. Manifest rows retained without re-hashing

**Confirmed.** `write_manifest` kept rows for existing files without recomputing their hashes, so a file changed on disk stayed stale until `--verify` happened to run.

Fixed: every retained row is re-hashed on rebuild. A drift is recorded in that row's provenance note and printed as a warning. The reviewer's related instruction — that every acquisition run should verify before declaring success — is now enforced in code rather than left to discipline, as below.

## 4. QA could be skipped and Track A still reported success

**Confirmed, and this was the most consequential of the four.** `qa_netcdf` was called and its result discarded; `track_a` returned `True` unconditionally after a non-empty download. With xarray absent, QA printed "skipped" and the run still counted as a pass.

Fixed as the reviewer specified. `qa_netcdf` returns a status dict, and a skipped QA returns `qa_pass=False` rather than nothing. **Track A now succeeds only if QA ran, QA passed, and the manifest re-verifies against disk**:

```python
qa = qa_netcdf(files, a)
v  = verify()
ok = bool(qa.get("qa_pass")) and v == EXIT_OK
```

A download alone is no longer a data-quality PASS.

---

## 5. Audit limitations, restated rather than argued with

The reviewer's framing is right and worth keeping in front of anyone who reads the gate count. **26/26 passing means the package is self-consistent and the QA behaves correctly on synthetic fixtures. It says nothing about any real dataset, because there is no real dataset.** Hashes attest to packaged bytes, not authenticity or scientific validity. The probe logs verify their own existence and contents, not independent network tests.

Not validated, and not claimed: dataset identity, version or units from an original file; actual spatial or temporal completeness; issued-bulletin provenance; fisher decision context; R1-paired eligibility; R2 expert judgement; any safety benefit.

## 6. Changes in this package

Four findings registered as `P3A-14` to `P3A-17`. Four new gates: **G-22** rewritten as a behavioural test runner, **G-24** Track A gating, **G-25** hash recomputation, **G-26** time-bounds evaluation. Register 13 → 17 rows, with metrics and README following automatically, because G-17 and G-18 now refuse to pass otherwise. New file `test_qa.py`. Manifest 19 → 22 entries, all verifying.

**One dependency note:** xarray, netCDF4 and numpy were installed **in this audit sandbox** so the QA could be tested behaviourally, at the reviewer's request. They are recorded in `requirements.txt` as test-only. Nothing was installed on the user's machine, and no acquisition dependency changed.

## 7. Next run, unchanged

1. Authorized provider egress. No bypass.
2. A small original Copernicus NetCDF subset: download, hash, and parse identity, version, units, times and coordinates **from the file**. Track A stays HOLD until then.
3. A bounded original NDFD object selection or archived marine CAP record, with issuance and validity metadata. Track B stays HOLD until then.
4. QA **and** manifest verification must both pass before any acquisition is recorded as a success — now enforced by the code rather than by intention.
5. Keep R0 and R1-SOURCE-ONLY separate from operational R1 and R2.
