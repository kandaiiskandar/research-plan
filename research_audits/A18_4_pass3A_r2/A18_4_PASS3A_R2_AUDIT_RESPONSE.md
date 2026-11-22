# A18.4 Pass 3A r2 — Response to the Independent Archive Audit

**22 November 2026.** Audit dated 22 November 2026 on `A18_4_pass3A.tar.gz`.
**The audited r1 package is preserved unchanged.** Every correction below is in this r2 folder.

The audit's decision stands and is not contested: **Track A HOLD, Track B HOLD, acquisition NOT COMPLETE.** Nothing here changes the result. What changed is that two of the package's own claims were wrong, and three tooling weaknesses would have let the same class of error through again.

---

## 1. Findings accepted and corrected

### F1 / F6 — the discrepancy register said 11, the metrics said 10, the README said 10

**Confirmed exactly as reported.** Cause: `P3A-11` was appended to the register *after* `report_metrics.json` was generated, and the metrics were never regenerated.

The auditor's sharper point is the one that matters: **the internal 16/16 PASS missed it**, because `G-07` compared only the eligibility register and **no check compared the discrepancy register at all**. A gate that checks one register by name cannot notice a different register drifting.

Fixed structurally, not by editing a number. `G-17` now iterates a **register map** and compares every register against the metrics; `G-18` rejects any prose count that matches no register. Adding a register to the map is the only way to add a register, so the gate cannot silently omit one again.

That fix immediately proved itself: appending the two new findings below took the register from 11 to 13, `G-17` failed, and the metrics and README had to follow before the audit would pass.

### F5 — the second environment's probe had no log

**Confirmed.** The report asserted the linked computer was probed independently; only the container's log was in the package. That is a claim without an artefact, which is the precise failure class A18.2-R was about.

Fixed by producing the evidence rather than softening the claim. The device probe was re-run over its own egress path and `logs/connectivity_probe_device.json` is preserved: **7 hosts, 6 refused, `pypi.org` at 200** — the same pattern as the container. `G-19` now requires a log for every environment the report names.

One correction to the r1 report while doing this: it said "three provider hosts refused". The re-run probed the same seven hosts as the container, and six were refused. The report now states 6 of 7 for both environments, each citing its own log.

### F2 — `--verify` returned 0 on an empty manifest

**Confirmed, and it was a genuine design error**: manifest *consistency* and acquisition *success* were conflated, so "nothing was acquired" was indistinguishable from "everything verified".

Now tri-state, as the auditor asked, keeping the two concepts separate:

```
EXIT_OK             = 0   manifest non-empty AND every row matches disk
EXIT_MISMATCH       = 1   a manifest row disagrees with the file on disk
EXIT_NO_ACQUISITION = 3   manifest empty: consistent, but nothing was acquired
```

`--verify` now exits **3** here and says so in words. `G-20` asserts it.

### F4 — manifest appended on rerun, leaving duplicates and stale hashes

**Confirmed.** `append_manifest` concatenated old rows and new ones with no reconciliation.

Replaced with `write_manifest`, a deterministic rebuild keyed on `relative_path`: a rerun **replaces** the row for a path it re-downloaded, **keeps** rows whose file is still present, and **drops** rows whose file is gone. Output is sorted by path with `item_id` reassigned, so the same set of files produces a byte-identical manifest regardless of acquisition order. `G-21` asserts the append function no longer exists.

### F3 — Track A QA was thinner than implied, and `decode_cf=False` is not time decoding

**Confirmed on both counts.** The QA read raw attributes with decoding off, which inspects attributes rather than decoding time.

The QA now opens the file a **second time with `decode_cf=True`** and adds: decoded time extent, step regularity and gap detection, duplicate timestamps, **fill-value hits counted separately from NaN**, decoded latitude and longitude extents **compared against the requested bounding box**, decoded time extent compared against the requested window, and the **expected variable set** with missing and unexpected variables listed. A decode failure is recorded as `DECODE_ERROR` rather than passing silently.

The completeness claim is also bounded in the code itself, as the auditor asked. Still **not** covered and **not** to be claimed: physical plausibility against an external reference, cross-variable consistency, and provider semantic correctness. `G-22` and `G-23` assert both the new checks and the bounded wording.

---

## 2. Findings accepted without change

**Track B `--track-b-ndfd` is not an acquisition implementation.** Correct, and deliberate: it prints the NCEI and AWS pointers and returns HOLD rather than attempting a blind recursive fetch of an object layout nobody has read. It now exits **2** rather than 0, so it cannot be mistaken for a completed step. Implementing a bounded NDFD object selection is the next run's work, not something to fake now.

**The local agent should not claim direct review of the six Google Docs.** Agreed, and the r1 package already stated this. The claim stands unchanged: `docs.google.com` is unreachable from both environments, the six documents were **not reviewed from source**, and `P3A-07` records it. The auditor read them through a connected Drive and found the task constraints broadly consistent, which is useful corroboration but is the auditor's verification, not mine.

**Copernicus version and temporal metadata must be rechecked from the real file.** Agreed. All 18 variables remain tiered `DOCUMENTED_ONLY`, with `standard_name` and `units` recorded as not stated on the pages. `P3A-05` and `P3A-09` carry this.

**The internal checks are consistency tests, not data quality tests.** Agreed, and worth restating plainly: **23/23 passing says the package is self-consistent. It says nothing about any dataset, because there is no dataset.**

---

## 3. Two new findings this response added

`P3A-12` records the stale-count defect and its structural fix. `P3A-13` records the unevidenced probe claim and the preserved log.

Both are the same failure mode logged as `P3A-11` and before that in A18.2-R: **hand-maintained prose drifting from computed artefacts.** The r1 package named that problem and then committed two fresh instances of it. The response is the one the A18.2-R remediation spec called for: bind claims to artefact fields, iterate the registers rather than naming them, and emit the numbers machine-readably so a reviewer never has to trust a sentence.

Honesty about the limits of that fix: `G-18` itself produced a false positive on first run, reading the gate ID `A3A-03` as a count of variables. The tokenizer was tightened. The guards keep needing correction, which is why the machine-readable block below matters more than any prose in this folder.

---

## 4. Machine-readable claims

`logs/report_audit.json` now carries a `machine_readable_claims` block so no numeric claim needs to be read out of prose:

```
raw_data_files 0 · raw_bytes 0
register_rows {01:5, 02:0, 03:18, 04:0, 06:14, 08:13}
register_count_mismatches []   prose_count_mismatches []
environments_probed [container, device]
probe_logs [connectivity_probe_container.json, connectivity_probe_device.json]
refused_hosts {container: 6, device: 6}
verify_exit_status 3  (0=verified, 1=mismatch, 3=no acquisition)
track_a HOLD · track_b HOLD · combined HOLD
evidence_tiers_achieved []
tiers_not_achieved [R0, R1-SOURCE-ONLY, R1-PAIRED, R2, R3]
```

---

## 5. What is still HOLD, and what the next run must do

Unchanged from the audit's required-next-run list. No code change in r2 acquires anything.

1. Move execution to a system with authorized provider egress. Do not bypass controls.
2. Configure Copernicus authorization, download and hash a small real coastal NetCDF subset, and parse native variable units, time values and coordinates from the file. **Track A stays HOLD until then.**
3. Implement a bounded NCEI NDFD object selection, or an original archived marine CAP record, with the retrieved file and its issuance and validity metadata. **Track B stays HOLD until then.**
4. Keep R0, R1-SOURCE-ONLY, R1-PAIRED and R2 separate, and preserve a connectivity log for every environment tested.

**Acceptance position unchanged: documentation and integrity PASS with corrections applied; dataset acquisition HOLD.** No operational source evidence, independent judgement or hardware result is established by this package.
