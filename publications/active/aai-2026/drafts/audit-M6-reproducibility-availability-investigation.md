# Audit Investigation — M-6: Reproducibility and Availability

**Scope:** Finding M-6 only.
**Baseline:** `aai-2026-manuscript-v7-rewrite-v2.docx` (attached this session; saved to the drafts folder). sha256 `f8769389a5e5c681…`, 419,027 bytes, 5,041 words, **7 pages, US Letter**.
**Investigation date:** 8 October 2026
**Mode:** read-only. No file in the repository was modified, no experiment was run, no package installed, no dataset fetched, no repository created or published.

---

## A. Executive Finding

**Verdict: PARTIALLY CONFIRMED — category D (a combination), with the weights different from the auditor's framing.**

The absence of a public availability statement is **not** the substantive problem. Three findings reorder M-6:

1. **Internal reproducibility is unusually strong.** Every raw record, the solar artefact and the canonical results file are **tracked in version control** — `.gitignore` is three lines and excludes nothing but `.DS_Store`, `__pycache__/` and `*.pyc`. 399 files under `data/` and 984 files in total are tracked. The classifier, the governance mappings, the comparator and the sensitivity sweep are all present, complete and deterministic. A reviewer *with the repository* could rerun the headline experiment.

2. **The real gap is narrower and sharper than "no public code": the sensitivity and attribution layer has no preserved machine output.** The headline comparator figures — 43,848 / 28,501 / 9,135 / 5,935 / 531 / 266 / 42.88 / 48.69 / 41.08 / 45.56 / 5.81 / 4.48 / 0.00 — all sit in `data/c8/canonical-results-post-migration.txt`. **Nothing else does.** The 518/13 attribution, the 5.67–9.56% and 4.26–6.64% envelopes, the 1.26% / 0.37% vessel-class figures, the 9.59% / 7.40% denominator figures, the 9.22% alternative-threshold figure and the "56 distinct combinations" claim exist **only in dated analysis documents**. `threshold_sensitivity.py:150` writes its output to `/tmp/sens_out.txt`, which is not retained and is gone. Roughly **half the numbers in Table II and §V rest on prose, not on archived machine output.**

3. **Public availability cannot be asserted, and must not be.** A remote exists — `git@github.com:kandaiiskandar/research-plan.git` — but it is an SSH URL, this session has no GitHub access to it, and the attempted visibility check was declined. **Whether that repository is public is NOT VERIFIED.** It is also a full PhD research repository (264 MB of history, unpublished thesis material, in-progress manuscripts), so public release is a decision with consequences beyond this paper.

**And one finding that governs the recommendation.** The venue requirement is recorded locally and verified against the official page: *"Paper must be 4 to 6 pages of **A4** size"* and *"**Any submitted paper that exceeds six (6) pages will be rejected**"* (`aai-2026-phase9-layout-submission-audit.md:13,15`, sourced to aai.unimap.edu.my). **No code-availability, data-availability or artifact-evaluation requirement appears anywhere in the recorded venue requirements.** The attached manuscript is **7 pages on US Letter** — non-compliant on both counts, independently of M-6. Any M-6 recommendation that adds text is therefore actively harmful, and I make none.

**Submission implication: the availability question is not what stands between this paper and submission.** The page count and page size are. M-6's correct response is almost entirely **external** — re-capture the sensitivity run output, build a reproduction package — plus **one two-word insertion** in the manuscript that has nothing to do with availability and everything to do with whether a reader can interpret the result at all: **the evaluation window's time zone is never stated.**

---

## B. Canonical Artefact Inventory

Distinguishing canonical from superseded, diagnostic and exploratory.

### B.1 Canonical experiment path

| Role | Path | Evidence |
|---|---|---|
| **Data collection (v2, canonical)** | `scripts/collect_raw_v2.py` | Lines 135–151: both marine requests; line 145 `"models": "meteofrance_wave"`; line 150 the Open-Meteo marine endpoint |
| **Data collection (v1, superseded)** | `scripts/openmeteo_raw_download.py` | Line 61 `"models": "era5_ocean"`, land-cell defect F-10; **superseded** |
| **Time classifier (canonical)** | `scripts/canonical_gt.py` | Lines 8–14 `g_t`; lines 108–115 `is_daylight`; SDR-001 applied 2026-09-08; single canonical implementation, imported by every analysis script |
| **Solar artefact (frozen)** | `data/solar/solar-events-daily.csv` | Carries per-row `solar-v1` impl tag and sha256 `3b7dc371ebe5931b…c36c`, spec `solar-spec-v1` |
| **Classifier + governance mappings + comparator** | `scripts/condition_comparison.py` | Lines 85–87 set constants; 92–106 the four `A_AI` maps; 135–148 load/merge/`dropna`; 169–171 `admissible()`; **line 198** the divergence computation; line 213 the departure window |
| **Sensitivity sweep** | `scripts/sensitivity/threshold_sensitivity.py` | Line 19 `CANON`; line 37 `g_o`; lines 100–124 the one-at-a-time sweeps and time policy T1; **line 150 writes to `/tmp/sens_out.txt`** |
| **Counterfactual sweep** | `scripts/sensitivity/gt_counterfactual.py` | Line 25 `TH`; line 27 `CFG` |
| **Component attribution** | `scripts/diagnostic_binding.py` | Line 54 `VESSEL_THRESHOLDS`; lines 205–244 binding shares and prediction check; register writes gated behind `--write-register` |
| **Figure generation** | `scripts/canonical_figures.py` | Line 93 `TH`; lines 103–104 config map; described in the c8 header as *"THE authoritative figure generator"* |
| **Threshold provenance comparison** | `scripts/threshold_comparison.py` | Lines 31–41 the candidate table with conversion rules |

### B.2 Stored outputs

| Path | What it contains | Date |
|---|---|---|
| **`data/c8/canonical-results-post-migration.txt`** | **The only captured console run of the canonical scripts.** PRIMARY and RESOLUTION state distributions, pairwise divergence matrices, binding analysis, prediction checks | committed 2026-09-08 (`babe92f`) |
| `data/c8/pre-migration-scripts/` | Archived copies of eight superseded script versions | 2026-09-08 |
| `data/c8/pre-migration-anchors.txt` | Pre-migration figures, for comparison | 2026-09-08 |
| `data/c5/c5-run-manifest.json` | **A proper run manifest** — `generated_utc`, harness path **and sha256**, reused-implementation sha256, parameter record | 2026-09-08 |
| `data/c6/`, `data/c7/` | Prediction re-resolution and baseline provenance CSVs | 2026-09-08 |

**The project knows how to archive a run** — `c5-run-manifest.json` is a model of the practice, with script hashes and a UTC timestamp. It simply was never applied to the canonical experiment or to the 2026-09-21 sensitivity run.

### B.3 Specifications and reports (not machine output)

`docs/canonical/appendix-c-formalisation.md` (the formal architecture), `docs/canonical/data-provenance.md` (the source-of-truth provenance record), `docs/analysis/experiment-report-delta-l2.md` (dated 2026-09-21), `docs/analysis/threshold-sensitivity-analysis.md` (dated 2026-09-21, committed 2026-09-22 as `3c70a1d`), `README.md` (a research-programme overview — **not a reproduction guide**; it contains no "how to run", no dependency list, no execution order).

---

## C. Data Provenance and Availability

### C.1 PRIMARY

| Property | Value | Source |
|---|---|---|
| Provider | Open-Meteo | `collect_raw_v2.py:135` |
| Endpoint | `https://marine-api.open-meteo.com/v1/marine` (waves); `https://archive-api.open-meteo.com/v1/archive` (weather) | code |
| Model identifier | `era5_ocean` (waves) | `collect_raw_v2.py:129` |
| Coordinates requested | 5.98 N, 116.01 E, `cell_selection: "sea"` | lines 52–53, 133 |
| Cell returned | waves 6.0, 116.0; weather 5.940246, 116.025 | CSV headers |
| Temporal coverage | 2020-01-01T00:00 → 2024-12-31T23:00 | file inspection |
| Time zone | `Asia/Kuching`, `utc_offset_seconds=28800` — **timestamps are local** | CSV header |
| Variables / units | `wave_height (m)`, `wave_period (s)`; `wind_speed_10m (kn)`, `precipitation (mm)`, `weather_code (wmo code)` | CSV headers |
| Temporal resolution | hourly | file inspection |
| Missing values | **none** — 0 NaN in every column of both files | inspection |
| Raw files | `data/raw_marine_era5_sea.csv`, `data/raw_weather_sea.csv` | — |
| Preprocessing | inner join on timestamp, `dropna(["wave","wind","precip"])` | `condition_comparison.py:135–148` |
| Expected / usable | 1,827 days × 24 = 43,848 / **43,848** | reconstructed exactly |

### C.2 RESOLUTION — and the [11] lineage question

| Property | Value | Source |
|---|---|---|
| Provider | **Open-Meteo**, not Copernicus | `collect_raw_v2.py:150` |
| Endpoint | `https://marine-api.open-meteo.com/v1/marine` | code |
| Model identifier | **`meteofrance_wave`** | `collect_raw_v2.py:145` |
| Requested period | `max("2020-01-01", MFWAM_MIN_START="2021-10-01")` → 2021-10-01 … 2024-12-31 | lines 59, 100–101, 140 |
| Cell returned | 5.958336, 116.04167 | CSV header |
| Coverage returned | 2021-10-01T00:00 → 2024-12-31T23:00, 28,512 rows, 0 gaps, 0 duplicates | inspection |
| Missing values | **11 contiguous leading NaN** (2021-10-01T00:00 → T10:00); first valid 11:00 local | inspection |
| Expected / usable | 1,188 × 24 = 28,512 / **28,501** | reconciled exactly |

**Lineage to reference [11]: NOT VERIFIED.** No request, response, manifest or log in the repository names the Copernicus product `GLOBAL_ANALYSISFORECAST_WAV_001_027` or DOI `10.48670/moi-00017`. The identification of `meteofrance_wave` with that CMEMS product is an inference from Open-Meteo's documentation, recorded as such at `aai-2026-manuscript-v1-prefinal.md:265` (*"the October 2021 record start trace to the Open-Meteo documentation"*). **The repository does not establish that the Open-Meteo series and the CMEMS product are the same data**, and they should not be assumed identical merely because they share a model family. This is finding **C-1**, already reported separately; M-6 confirms it from the artefact side.

### C.3 Availability, in four distinct senses

| Sense | Status | Evidence |
|---|---|---|
| **1. Internal availability** | **FULL.** All raw records, the solar artefact and the canonical results file are tracked in git and present on disk | `git ls-files` confirms each; `.gitignore` excludes none of them |
| **2. Public availability** | **NOT VERIFIED.** A remote exists (`git@github.com:kandaiiskandar/research-plan.git`) but is SSH; this session has no GitHub access to it and the visibility check was declined | `git remote -v`; `gh api` returned 403 "not enabled for this session" |
| **3. Independent retrievability** | **PARTIAL.** The API calls are fully documented in `collect_raw_v2.py` and could be reissued — but Open-Meteo's archive is a live service with no versioning, no credentials and no payment required. A reissued request may or may not return identical values | code inspection |
| **4. Bitwise reproducibility of the original records** | **NOT GUARANTEED** from the provider; **GUARANTEED** from the repository | the CSVs are committed, so the exact bytes survive in git history regardless of what the API now returns |

**The implication is important and favourable:** because the raw CSVs are version-controlled, the numerical results do **not** depend on the API still returning the same values. Anyone with the repository has the exact inputs. What they lack is a dependency specification and an execution guide. **No checksums or archived snapshots of the raw files exist** beyond git's own object hashes, and no file records a retrieval timestamp — the retrieval date is known only to commit precision (`21695e0`, 2026-09-06 12:55:31 +0800).

---

## D. Code and Environment Reproducibility

| Question | Finding |
|---|---|
| Present? | **Yes** — every script in the chain |
| Complete? | **Yes** for the canonical path. `canonical_gt.py` is a single shared implementation; no script embeds its own solar astronomy |
| Executable in principle? | **Yes** — plain Python with pandas/numpy; no services, no credentials, no database |
| Version-controlled? | **Yes** — 984 tracked files |
| Publicly accessible? | **NOT VERIFIED** (§C.3) |
| Undocumented local files? | **No.** Paths resolve from `Path(__file__).resolve().parent.parent` — relative, portable |
| External services at analysis time? | **No.** Only `collect_raw_v2.py` touches the network, and its outputs are committed |
| Hard-coded paths? | **One** — `threshold_sensitivity.py:150` writes to `/tmp/sens_out.txt`, which is both platform-specific and ephemeral. This is the single defect that destroyed the sensitivity provenance |
| Credentials? | **None required** |
| **Dependency specification** | **ABSENT.** No `requirements.txt`, `pyproject.toml`, `setup.py`, `setup.cfg`, `Pipfile`, `environment.yml` or conda file exists anywhere in the repository |
| Python / package versions | Recorded **once, in prose**: `experiment-report-delta-l2.md:395` — *"re-run on 2026-09-21 (Python 3, pandas 2.3.3, numpy 2.2.6)"*. Not machine-readable, not pinned, and the Python minor version is unspecified |
| Environment configuration | **None** |
| Execution order | **Not documented anywhere.** No README section, no Makefile, no driver script. The order is inferable from imports and data dependencies by a reader who knows the project |
| Random seeds | **Not applicable** — no randomisation. Verified: no `random`, `np.random` or seed call in the canonical path |
| Platform assumptions | `/tmp` (POSIX) in the sensitivity script only |
| Output locations | **stdout for every canonical script.** `condition_comparison.py` and `diagnostic_binding.py` have `to_csv` calls, both gated behind `--write-register`. The only persisted run is a manual stdout redirect |

**Code completeness ≠ execution verification.** I did not run anything. The assessment above is static: the scripts appear complete and self-consistent, their imports resolve within the repository, and their data dependencies exist. Whether they execute cleanly under a current pandas/numpy was not tested and is **NOT VERIFIED**.

---

## E. End-to-End Reproduction Chain

Classification assumes a reviewer **with repository access** and no contact with the author.

| Stage | Input | Script | Config | Output | Verification evidence | Classification |
|---|---|---|---|---|---|---|
| **1. Data retrieval** | Open-Meteo APIs | `collect_raw_v2.py` | lat/lon/tz/models/cell_selection, lines 52–53, 129–151 | `raw_weather_sea.csv`, `raw_marine_era5_sea.csv`, `raw_marine_mfwam.csv` | CSV headers record the returned cell; counts reconcile exactly | **TRACEABLE WITH ASSUMPTIONS** — the call is fully specified, but the provider is unversioned and no retrieval timestamp or checksum was recorded |
| **2. Raw records** | — | — | — | three committed CSVs | tracked in git; byte-stable in history | **FULLY TRACEABLE** |
| **3. Preprocessing** | the CSVs | `condition_comparison.py:135–148` | `skiprows=3`, inner join, `dropna` | in-memory frame | counts reconcile: 43,848 and 28,512 − 11 = 28,501 | **FULLY TRACEABLE** |
| **4. Environmental classification** | frame | `condition_comparison.py` + `canonical_gt.py` | W 21.6/27.0, R 10.0/20.0, O 1.0/1.25, `g_m` = SAFE | state vector | solar artefact carries impl version and sha256; constants carry dated provenance comments | **FULLY TRACEABLE** |
| **5. Governance mappings** | states | `condition_comparison.py:92–106` | four explicit `frozenset` maps | admissible sets per hour | mappings are literal in code; C1↔C3 = 0.00% is an entailed conformance check | **FULLY TRACEABLE** |
| **6. Pairwise comparison** | sets | `condition_comparison.py:198` | set inequality | divergence matrix | matches `data/c8/…:223, 257` exactly | **FULLY TRACEABLE** |
| **7. Δ<sub>L2</sub>** | matrix | derived | — | 5.81% / 4.48% | stored artefact lines 226, 260 | **FULLY TRACEABLE** |
| **8. Sensitivity analysis** | frame | `threshold_sensitivity.py` | `CANON` + sweeps, lines 100–124 | **`/tmp/sens_out.txt` — not retained** | **none** | **PARTIALLY TRACEABLE** — the script is present and deterministic, so a reviewer could regenerate the figures, but nothing in the repository records what was actually run on 2026-09-21 |
| **9. Component attribution** | states | `diagnostic_binding.py` / `canonical_figures.py` | vessel thresholds line 54 | stdout | the stored artefact has **overlapping** "at max" counts (lines 368–374), **not** the 518/13 exclusive split the manuscript reports | **PARTIALLY TRACEABLE** |
| **10. Manuscript tables and claims** | §§8–9 | manual transcription | — | Table II, §V | no automated link; no script emits the manuscript's numbers in manuscript form | **TRACEABLE WITH ASSUMPTIONS** |

**Could a reviewer with repository access reproduce the experiment without contacting the author?** **The headline comparator results: yes**, with effort — they would have to infer the execution order and resolve dependency versions from a prose sentence. **The sensitivity and attribution results: they could regenerate them, but could not verify that what they regenerate matches what was reported**, because no record of the reported run survives.

---

## F. Numerical Provenance Matrix

Evidence grades: **A** machine-generated canonical output · **B** stored experiment result table · **C** dated research report · **D** manuscript statement only · **E** no supporting artefact.

| Reported result | Strongest evidence | Location |
|---|---|---|
| 43,848 PRIMARY records | **A** | `data/c8/…:198` *"Loaded 43,848 hourly records"* |
| 28,501 RESOLUTION usable records | **A** | `data/c8/…:232` |
| 9,135 evaluated hours | **A** | `data/c8/…:215` |
| 5,935 evaluated hours | **A** | `data/c8/…:249` |
| 531 CAUTION hours | **A** | `data/c8/…:217` |
| 266 CAUTION hours | **A** | `data/c8/…:251` |
| C0↔C1 42.88% / 41.08% | **A** | `data/c8/…:223, 257` |
| C0↔C2 48.69% / 45.56% | **A** | `data/c8/…:223, 257` |
| Δ<sub>L2</sub> 5.81% / 4.48% | **A** | `data/c8/…:226, 260` |
| C1↔C3 = 0.00% | **A** | `data/c8/…:224–225, 258–259` |
| **518 ocean-state / 13 rainfall attribution (97.6% / 2.4%)** | **C** | `experiment-report-delta-l2.md:282–283`. **Not in any machine artefact** — the stored file carries only overlapping "at max" counts for a different slice (`data/c8/…:368–374`) |
| **Envelope 5.67–9.56% (PRIMARY)** | **C** | `threshold-sensitivity-analysis.md:158, 217` |
| **Envelope 4.26–6.64% (RESOLUTION)** | **C** | `threshold-sensitivity-analysis.md` §E |
| **Large-vessel 1.26% / 0.37%** | **C** | `threshold-sensitivity-analysis.md:112–115` |
| **Daylight-only 9.59% / 7.40%** | **C** | `threshold-sensitivity-analysis.md:136` (denominators 5,536 / 3,594 published) |
| **Alternative wave UNSAFE 9.22%** | **C** | `threshold-sensitivity-analysis.md:114`. **Remains unresolved** — confirmed again here: `/tmp/sens_out.txt` is absent and no `data/` artefact contains `9.22` |
| **"56 distinct combinations"** | **E** | No artefact states 56. The figure was established by instrumenting `threshold_sensitivity.py` during an earlier audit (78 executions / 56 unique configurations); that instrumentation was not retained either |

**Eleven results grade A. Six grade C. One grades E.** Every grade-C figure traces to one of two documents dated 2026-09-21/22; a number appearing in several documents is one source copied, not independent corroboration, and has been counted once.

**Answering the brief's specific question on 9.22%: yes, it remains unresolved,** and the investigation shows the problem is systemic rather than isolated — the same missing-artefact defect covers every sensitivity and attribution figure, not just that one.

---

## G. Deterministic Reproducibility Assessment

| Claim | Classification | Evidence and limits |
|---|---|---|
| **A.** Identical input records and configuration produce identical outputs | **SUPPORTED** | No randomisation, no estimated parameters, no seeds in the canonical path. The classifier is a pure function of thresholds and inputs; aggregation is `max`; comparison is set inequality. `experiment-report-delta-l2.md:16, 395` records that a re-run on 2026-09-21 reproduced 5.81% / 4.48% / 0.00% / 42.88% / 48.69% exactly — an **independent re-execution two weeks after the stored capture**, which is the strongest determinism evidence available. Residual risk: floating-point comparison against `1.0`/`1.25` thresholds could in principle shift a boundary hour under a different numpy build. Not observed, not tested. |
| **B.** The canonical experiment can be rerun from existing local artefacts | **SUPPORTED WITH QUALIFICATION** | All inputs and scripts are present and version-controlled. Qualifications: no dependency specification; execution order undocumented; `threshold_sensitivity.py` writes to `/tmp`. These are friction, not blockers, for someone who knows the project. |
| **C.** The experiment can be independently reproduced from publicly available artefacts | **NOT VERIFIED** | Repository visibility unknown (§C.3). No public archive, no DOI, no supplementary package. This is the claim the manuscript must not make. |
| **D.** The exact original datasets can be regenerated from external providers | **NOT VERIFIED, and likely not** | Open-Meteo serves a live, unversioned archive; model reanalyses are revised. No checksum or retrieval timestamp was recorded. **This matters less than it appears**, because the raw CSVs are committed — reproduction from the repository does not require the API. |
| **E.** All manuscript results are supported by archived machine outputs | **NOT SUPPORTED** | §F: six results grade C and one grades E. Roughly a third of the reported numbers, including everything in the sensitivity and attribution sections, have no preserved machine output. |

**Determinism and reproducibility are not the same thing, and the manuscript's claims stay on the right side of the line.** It asserts determinism (*"replaying an identical record under an identical configuration reproduces an identical result"*) — which is **SUPPORTED**. It does **not** assert that anyone else can do the replaying. No false availability claim exists in the manuscript.

---

## H. Manuscript Methodological Sufficiency

### H.1 What a reader can reconstruct from the paper alone

| Element | Specified? | Note |
|---|---|---|
| Environmental state construction | **Yes** | Five components named in §IV |
| Maximum-severity aggregation | **Yes** | *"the maximum severity among the available component classifications"* |
| Threshold **provenance** | **Yes** | §IV, and improved in this version (see H.3) |
| Threshold **values** | **Partial** | Wave values now given (1.25 m, 1.875/1.90 m). **Wind (21.6 / 27.0 kn) and rainfall (10 / 20 mm/h) are named only by source, never numerically** |
| Researcher-defined choices | **Yes** | Enumerated in §IV, and the daylight policy is now explicitly so |
| Departure window | **Yes** | 05:00–09:00 |
| **Time zone** | **NO** | **Not stated anywhere.** See H.2 |
| Data source and period | **Yes** | Both configurations, with record counts |
| Missing-value handling | **Partial** | The marine-warning exclusion is fully explained; the 11 missing wave values are not mentioned (finding C-1) |
| Governance mappings | **Yes** | Fig. 1 and Table I |
| Comparator definitions | **Yes** | §III |
| Δ<sub>L2</sub> calculation | **Yes** | §III, with the identity derived |
| Sensitivity factors | **Yes** | Threshold, vessel class, denominator |
| Attribution method | **Partial** | The 97.6% / 2.4% split is reported but the tie-breaking rule under max-severity aggregation is unstated |
| Execution and reproducibility assumptions | **Yes** for determinism; **no** software environment | — |

### H.2 The one genuine sufficiency gap

**The manuscript never states the time zone.** "05:00–09:00" appears without qualification; a search for "local time", "Asia/Kuching", "UTC+8", "time zone" and "timezone" returns nothing. The data files are `Asia/Kuching` (`utc_offset_seconds = 28800`) and the solar artefact is computed for UTC+8.

This is **not** a pedantic point. The classifier's time component is a solar-event boundary, and sunrise at the site runs 05:59–06:32. Whether the window is local or UTC determines whether roughly 40% of it is pre-dawn — which is what makes the participation-gating figure 42.88% rather than something far smaller. **A reader cannot interpret the headline decomposition correctly without knowing the time zone**, and cannot infer it from the paper. Cost to fix: **two words.**

### H.3 Already improved in this version — noted, not re-raised

v7 has adopted recommendations from earlier audits, which is why it has grown to seven pages:

- §IV now reads *"the UNSAFE boundary is derived from the upper limit of the highest passing sea-state category reported in [17]"* — the M-1 conversion disclosure.
- §IV now reads *"The daylight boundary uses the sunset-to-sunrise interval specified in COLREGs Rule 20(b) [18]; treating non-daylight hours as UNSAFE is a researcher-defined governance policy, not a departure prohibition…"* — the M-7 qualification, which also strengthens the M-3 position.
- §V-B now names both metre values and declares the rounding: *"(1.25 m) and the tested failing condition (1.875 m, implemented as 1.90 m)"*.

**These are improvements and should be kept.** They are also the reason any further addition must be paid for by a deletion.

### H.4 What is *not* needed

Software versions, execution order, file paths and installation steps belong in a reproduction package, not in a 4–6 page conference paper. **I do not recommend inserting any of them.** The distinction the brief draws is the right one: details needed to *interpret* the result (time zone, thresholds, policy status) belong in the paper; details needed to *rerun the code* do not.

---

## I. Availability and Submission Requirements

### I.1 Verified venue requirements

From `publications/active/aai-2026/drafts/aai-2026-phase9-layout-submission-audit.md`, §1 "Venue Requirements", each row sourced to aai.unimap.edu.my — Manuscript Preparation:

| Requirement | Value | Status |
|---|---|---|
| Paper size | **A4** — *"Paper must be 4 to 6 pages of A4 size in length including all texts, references, figures and photographs"* | **VERIFIED** |
| Page limit | **4–6 pages**, references included — *"Any submitted paper that exceeds six (6) pages will be rejected"* | **VERIFIED** |
| PDF | IEEE PDF eXpress | **VERIFIED** |
| Submission system | EDAS, https://edas.info/N34957 | **VERIFIED** |
| **Code availability** | not mentioned | **NOT REQUIRED** (absent from the recorded requirements) |
| **Data availability** | not mentioned | **NOT REQUIRED** (absent) |
| **Supplementary materials** | not mentioned | **NOT VERIFIED** — no statement either way |
| **Artifact evaluation** | not mentioned | **NOT REQUIRED** (absent) |
| **Reproducibility statement** | not mentioned | **NOT REQUIRED** (absent) |
| **Ethics / data-management declaration** | not mentioned | **NOT VERIFIED** |
| Copyright notice | *"The manuscript-preparation page did not state a copyright-notice or eCF requirement at this stage. Not verified; check on EDAS at final submission."* | **NOT VERIFIED** |

I did not perform external verification of these requirements; the recorded audit cites the official page directly and I report it as found. **No IEEE-wide artifact policy should be assumed** — policies differ by conference, and this one records none.

### I.2 Compliance status of the attached manuscript

| | Required | Attached v7 | |
|---|---|---|---|
| Page size | A4 | **US Letter** | ✘ |
| Page count | ≤ 6 | **7** | ✘ |

Outside M-6's remit, but it determines the recommendation: **the manuscript is currently in a state the venue says will be rejected, and the binding constraint is space.**

---

## J. Impact on Scientific Contribution

| Aspect | Impact | Reasoning |
|---|---|---|
| **A. Mathematical validity** | **None** | Δ<sub>L2</sub> = P(CAUTION) is derived from the mappings; availability is irrelevant to it |
| **B. Correctness of reported numerical results** | **None established.** Eleven headline figures are backed by machine output and were independently re-executed on 2026-09-21. The six grade-C figures are **unverified, not wrong** | §F |
| **C. Internal computational reproducibility** | **Strong.** Data and code are version-controlled; the pipeline is deterministic; one re-execution is on record | §G claims A and B |
| **D. Independent external reproducibility** | **Not established.** Repository visibility unknown; no dependency spec; no execution guide; no package | §C.3, §D |
| **E. Transparency of researcher-defined choices** | **Good and improving.** §IV enumerates them, and v7 strengthened two of them. The repository is more candid still | §H.3 |
| **F. Novelty of the measurement assembly** | **None** | The contribution is the assembly, not its distribution |
| **G. Credibility of the empirical characterisation** | **Modestly affected.** A reviewer who asks "where did 9.22% come from?" has no artefact to be pointed at. The *headline* is well-evidenced; the *sensitivity envelope*, which the paper rightly insists must be read alongside the headline, is the part with the weaker provenance | §F |
| **H. Readiness for conference submission** | **Not blocked by M-6.** It is blocked by page size and page count | §I.2 |

**A lack of public code does not invalidate the contribution** — this is a deterministic replay of committed records, not a trained model, and the venue requires no artefact. **Equally, determinism does not confer reproducibility**: the experiment is deterministic *and* externally unreproducible, and both are true at once.

---

## K. Assessment of Auditor M-6

| Auditor claim | Verdict | Evidence |
|---|---|---|
| No public code repository | **PARTIALLY CONFIRMED** | A remote exists; its visibility is **NOT VERIFIED**. "No public repository" is not established — nor is the opposite |
| No data availability statement | **CONFIRMED** | Zero occurrences of "github", "repository", "available at", "code", "supplementary", "on request" in the manuscript |
| No archived configuration specification | **PARTIALLY CONFIRMED** | No dependency spec or environment file exists. But the *experimental* configuration — thresholds, mappings, window, solar artefact with sha256 — is specified in version-controlled code |
| No documented reproduction package | **CONFIRMED** | No README reproduction section, no Makefile, no driver script, no execution order anywhere |
| Readers or reviewers cannot independently reproduce the reported results | **PARTIALLY CONFIRMED** | *With* the repository: the headline results, yes, with effort. *Without* it: no. The sensitivity results: regenerable but not verifiable against what was reported |
| **(My own framing) "the paper's central methodological claim is determinism, yet there is no artefact by which anyone could test it"** | **OVERSTATED** | The artefact exists and is committed — `data/c8/canonical-results-post-migration.txt` plus the complete tracked inputs. What is missing is *public access* and a *dependency specification*. I should have distinguished "no artefact" from "no public artefact", and I withdraw the former |
| Classification A/B/C/D | **D — a combination**, weighted: **(A) largely true** (internal reproducibility is good), **(B) true** (external reproducibility is not established), **(C) true but narrower than stated** — the provenance gap is specific to the sensitivity and attribution layer, not to the experiment as a whole |

---

## L. Recommended Action

| Option | Transparency | External reproducibility | Feasibility | Submission req. | Reviewer risk | Page cost | Risk of unsupported claim |
|---|---|---|---|---|---|---|---|
| **1. No change** | Unchanged | Unchanged | Trivial | Satisfied — none required | Low–moderate | **0** | **None** |
| **2. Methodological clarification only** | Marginal — the manuscript already carries ~8 determinism sentences | None | Trivial | Satisfied | Low | +15–25 words | None |
| **3. Code availability statement** | High **if true** | High | **Blocked** — visibility NOT VERIFIED | Not required | **High if wrong** | +12 words | **HIGH — must not be written unverified** |
| **4. Code and data availability statement** | Highest **if true** | Highest | **Blocked** — same, plus the repo holds unpublished thesis material | Not required | **High if wrong** | +15 words | **HIGH** |
| **5. Supplementary reproduction package (external)** | High | **Materially improves it** | **Feasible** — data tracked, scripts complete, `c5-run-manifest.json` is a working template | Not required | Low | **0** | None |
| **6. Explicit limitation disclosure** | Honest | None | Trivial | Not required | Low | +12 words | None, but spends space on a non-requirement |

### Recommendation

**Option 5 (external package), with no availability statement in the manuscript, plus one two-word insertion unrelated to availability.**

**Rationale.** The venue requires no availability statement and will reject a seventh page. Options 3 and 4 cannot be written without a verification I was unable to obtain and must not guess at. Option 6 spends scarce space disclosing the absence of something nobody asked for. Option 2 duplicates what §IV already says at length. **Option 1 is defensible for the manuscript as it stands** — and would be my recommendation outright, were it not for the time-zone omission, which is a sufficiency gap rather than an availability one.

### Author actions, outside the manuscript and costing no pages

1. **Re-capture the sensitivity and attribution run output.** `threshold_sensitivity.py:150` writes to `/tmp`; redirecting a run into `data/` instead would turn six grade-C results into grade-A. The scripts and inputs are present; this is a redirect, not an experiment. **This is the highest-value action available and it changes nothing in the paper.**
2. **Add a run manifest** on the `data/c5/c5-run-manifest.json` pattern — UTC timestamp, script sha256s, package versions. The practice already exists in the repository.
3. **Write a `requirements.txt`** pinning the versions recorded in prose at `experiment-report-delta-l2.md:395` (pandas 2.3.3, numpy 2.2.6) and the exact Python version.
4. **Decide the repository's visibility deliberately.** If a public archive is created before 19 October — a trimmed package rather than the 264 MB research repository — then and only then does a 12-word availability statement become writable, and it should replace an equivalent number of words elsewhere.

---

## M. Exact Manuscript Changes

### M.1 §IV — state the time zone *(required; the only manuscript change recommended)*

**Original:**

> "The evaluation window is 05:00–09:00, which defines Neval."

**Minimal replacement:**

> "The evaluation window is 05:00–09:00 **local time (UTC+8)**, which defines Neval."

**Justification.** The classifier's time component is a solar-event boundary and sunrise at the site falls at 05:59–06:32, so whether the window is local or UTC decides whether ~40% of it is pre-dawn — and that is what produces the 42.88% participation-gating figure. Without the time zone a reader cannot interpret the decomposition, and it cannot be inferred from the paper. The data files carry `Asia/Kuching`, `utc_offset_seconds = 28800`, and the solar artefact is computed for UTC+8. **Cost: three words.**

**Page-neutral offset, if needed.** §V-A contains *"The direct C1↔C2 comparison returned the same value."* That sentence restates the cross-check already described in §III and could be dropped for a net saving.

### M.2 No availability statement

**I recommend adding none**, and specifically recommend **against** writing any sentence that asserts public availability of code or data. No verified basis for such a statement exists, the venue does not require one, and the manuscript has no page budget.

### M.3 No other change

The determinism claims in §IV — *"No parameter is estimated from the data and no randomisation is involved, so replaying an identical record under an identical configuration reproduces an identical result"* and *"Implementation checks confirmed the configured admissible-set mappings were applied as specified"* — are **accurate and supported** (§G claim A; the C1↔C3 = 0.00% conformance check is the implementation check, and it is in the stored artefact). No qualification is warranted.

---

## N. Unresolved Questions

1. **Repository visibility — NOT VERIFIED.** `git@github.com:kandaiiskandar/research-plan.git` exists as a remote; this session has no GitHub access to it and the visibility check was declined. **The author must establish this before any availability statement is contemplated.** Note also that the repository contains unpublished thesis material and in-progress manuscripts, so "make it public" is not a neutral act.
2. **The 9.22% provenance gap remains open**, and is broader than first reported: six sensitivity and attribution figures share it. Closing it requires a captured run, not new analysis.
3. **The "56 distinct combinations" claim has no artefact at all** (grade E). It was established by instrumenting the script during an earlier audit; that instrumentation was not retained. The manuscript states the number in §IV.
4. **Lineage from `meteofrance_wave` to CMEMS `GLOBAL_ANALYSISFORECAST_WAV_001_027` cannot be established from the repository** (finding C-1). No request or response artefact names the CMEMS product.
5. **Execution verification not performed.** No script was run. Static inspection suggests completeness; whether the canonical scripts execute cleanly under a current pandas/numpy is untested.
6. **Supplementary-material and ethics-declaration policies for AAI 2026 are NOT VERIFIED** — the recorded venue requirements are silent, which is not the same as prohibiting them.

---

## O. Final Verdict

> ## MINOR CLARIFICATION REQUIRED

**Three words in §IV** — "local time (UTC+8)" — and nothing else in the manuscript.

M-6's substance is real but misplaced. The experiment is **internally reproducible to an unusually high standard**: raw records, solar artefact and canonical results are all version-controlled, the pipeline is deterministic, and an independent re-execution on 2026-09-21 reproduced the headline figures exactly. **External** reproducibility is not established, but the venue requires no artefact, the manuscript makes no availability claim it cannot support, and there is no page budget to add one.

The one finding that deserves action is narrower and sharper than "no public code": **six of the manuscript's reported figures — the whole sensitivity and attribution layer — have no preserved machine output**, because the script that produced them writes to `/tmp`. That is fixed by a redirect, not by an experiment, and it costs the paper nothing.

**The binding obstacle to submission is not reproducibility.** It is that the attached manuscript is **7 pages on US Letter** against a verified requirement of **4–6 pages on A4**, with *"any submitted paper that exceeds six (6) pages will be rejected"*. That must be resolved first, and it is why this report recommends no addition beyond three words.
