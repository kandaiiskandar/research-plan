# PhD Research Pilot Preparation Audit

**Repository:** `research-test-2` · branch `main` @ `2b08a79`
**Audit date:** 16 November 2026
**Scope:** Readiness of existing project materials to support a feasibility pilot for the proposed journal study
*When Do Intermediate Advisory Restrictions Improve Safety at Comparable Useful Coverage? Evidence from Small-Vessel Departure Advice under Degraded Observations*
**Method:** Read-only inspection of 1,127 files. No dataset, script, manuscript or experimental artefact was modified. One read-only analysis was executed outside the repository tree (§9.2); it writes nothing and reproduces the published headline figures exactly.

**Evidence conventions used throughout.** `NOT FOUND` means the artefact does not exist in the repository; it is not a softened statement about quality. `REQUIRES VERIFICATION` marks a claim the repository asserts but which this audit could not confirm from primary evidence. *Documented* means a repository file states it; *inferred* means this audit derived it. Line numbers were obtained by direct file inspection and eighteen of the most load-bearing citations were independently re-verified line by line.

---

## 1. Executive Summary

**The project is not ready to run the pilot as specified, and the gap is not one of preparation effort. Three of the six checklist areas rest on artefacts that do not exist anywhere in the repository and cannot be produced from it.**

The project's strengths are real and unusual. It holds a complete, internally consistent formal specification of the governance architecture (`docs/canonical/appendix-c-formalisation.md`); a deterministic, tested, hash-manifested implementation (`governance/`, 9 modules, 149 tests); a five-year hourly environmental record with checksums and a reproducibility manifest; and — most valuable for an audit of this kind — a body of candid self-assessment in which the authors have already identified most of the weaknesses recorded below. That disclosure culture is a methodological asset and should be preserved.

The blockers are these.

**First, the independent safety reference does not exist and cannot be constructed from existing materials.** The proposed study's primary endpoint is independently judged recommendation safety. The repository contains no incident record, no outcome data, no expert judgement, no rating rubric, no rater, and no ethics approval. Every candidate reference inside the repository derives from the same source set as the gate's own thresholds, so grading the gate against it would be circular. The repository states this itself: *"Every threshold comparison to date measures thresholds against each other, never against outcomes"* (`docs/canonical/decision-record-empirical-first.md:81`).

**Second, the candidate-advice pool is degenerate in exactly the way that defeats the comparison.** Across the full 292-episode census, the system emits one recommendation type — `Delay` — in 244 episodes and nothing at all in 48. Zero `Go`, `DepartureTime` or `Duration` records exist (verified directly: `data/journal1-layer3-prototype/batch5-fidelity-evaluation/fidelity-traces.csv`). The restricted state (CAUTION) produces output; the unrestricted state (SAFE) produces none, because `R-SAFE-001` is deferred. The contrast the study needs — what graduated restriction *removes* relative to participation-only gating — is empty in the direction that matters.

**Third, the degraded-observation axis has no data.** There are no issue-time forecasts anywhere in the repository. All seven environmental datasets are retrospective reanalysis or harmonic tide prediction, retrieved in one batch with no retrieval timestamp, no issue time and no lead time. Reanalysis cannot represent what an operator knew at the decision point, and the repository's own planning document says so.

A fourth constraint is quieter but equally binding on study design. This audit computed it directly: the 531 CAUTION hours in the PRIMARY window fall on **201 distinct days and roughly 85–123 independent weather events**, not 9,135 independent observations (§9.2). A paired safety comparison is powered by discordant *events*, not hours.

**Recommendation: REVISE — proceed to a protocol and data-feasibility stage, not to the safety-effectiveness pilot.** A tightly scoped preparation pilot is both feasible and worth running now; the safety-effectiveness pilot as framed is not. Full reasoning in §11.

| Checklist area | Status |
|---|---|
| 1. Define advisory task | **PARTIALLY READY** |
| 2. Audit available data | **NOT READY** |
| 3. Prepare candidate advice | **NOT READY** |
| 4. Independent safety reference | **NOT FOUND** |
| 5. Blinded pilot assessment | **NOT READY** |
| 6. Experimental feasibility | **NOT READY** |

---

## 2. Research Context

### 2.1 Existing contributions

| Work | Location | Status | Contribution |
|---|---|---|---|
| Conference 1 — *A Graduated Safety-State-Gated Architecture for AI Decision Support in Low-Resource Coastal Fisheries* | `publications/active/ipsci-2026/` | Extended abstract **accepted for presentation**; full paper **rejected**, v3 revision in progress | The architecture: three-state gate, two governance levels, admissible-set contract |
| Conference 2 — *From Declared Risk Levels to Admissible Recommendations* | `publications/active/aai-2026/drafts/` | Draft at v11 (27 Oct 2026); **7 pages against a 6-page limit** (`aai-2026-v11-citation-renumbering-report.md:10`) | The measurement: Δ_L2 = 5.81% PRIMARY / 4.48% RESOLUTION |
| Journal 1 — *A Formally Verified Runtime AI Governance Architecture Based on Graduated Safety-State Gating* | `publications/active/journal-1/` | Research-design phase; Sections 5–6 drafted; **not submitted** | Formal model, implementation fidelity (F1–F3), latency reference |
| Journal 2 — the proposed study | `publications/active/journal-2/README.md` | **Empty stub**; "Not started" | — |

The proposed study is named in exactly one repository file: `docs/analysis/graduated-advisory-safety-novelty-assessment.md`, dated 16 November 2026, **untracked in git** (`git status --short` → `?? docs/analysis/…`, verified). It is a 171-line scoping and novelty assessment whose own verdict is *"Revise before committing to implementation"* (line 164). This audit was conducted independently of that document and reaches a compatible conclusion by a different route; where the two agree, the agreement is noted rather than assumed.

### 2.2 The proposed next study

Three claims are proposed, drawn from `graduated-advisory-safety-novelty-assessment.md` §7:

- **RQ1** — incremental effect of intermediate restriction under a shared outer cutoff (graduated vs participation-only).
- **RQ2** — whether partial advice beats *tuned whole-message abstention* at comparable useful coverage.
- **RQ3** — how observation quality (forecast age, channel dropout) changes that advantage.

### 2.3 Boundaries of novelty

The project does not claim to have invented graduated safety gating, runtime shielding or state-dependent restriction, and the repository already documents the precedents (`scripts/condition_comparison.py:12-19` for the Flehmig-style comparator; `docs/analysis/aai-2026-manuscript-architecture.md:201` for the selective-prediction/reject-option literature, which was deliberately cut from the conference paper for space).

Two boundaries matter for the next study and should be stated explicitly in any protocol:

1. **What is already established by construction, not by experiment.** Δ_L2 ≡ P(S = CAUTION) follows from the definitions; C1 ≡ C3 holds because the two admissible-set maps are *identical dictionary literals* (`publications/active/journal-1/evaluation-baseline-decision.md:24-31`: *"Any design that presents 0.00% as an experimental outcome presents a tautology as a discovery"*). The fidelity results F1/F2 are *analytically zero under a conforming implementation* (`publications/active/journal-1/evaluation-specification.md:143`) and therefore cannot serve as a safety endpoint — they cannot vary.
2. **What remains genuinely open.** Whether removing specific advisory categories at an intermediate state reduces independently judged harm without a matching loss of useful advice, and under what observation conditions that advantage disappears. This is the study's real contribution, and it is unaddressed by any prior output of this project.

A working implementation is not the contribution. The architecture should be treated as a **fixed instrument**; the independent endpoint and the comparator are the experiment.

---

## 3. Project Evidence Inventory

| Path | Content | Relevance to the pilot | Evidence quality |
|---|---|---|---|
| `docs/canonical/appendix-c-formalisation.md` (129 KB) | Canonical formal model: E = (w,r,m,o,v,t), g_w/g_r/g_m/g_o/g_t, max-severity aggregation, A_AI, ⊥ and D semantics | **High** — the task definition | Strong; internally consistent; agrees with code term by term |
| `governance/` (9 modules) | Deterministic rule engine, governance map, rule validation, episode orchestration, fidelity trace | **High** — the candidate-advice generator | Strong implementation; **semantically degenerate output** (§6) |
| `scripts/condition_comparison.py` | C0/C1/C2/C3 comparator maps (`:81-113`); divergence metric | **High** — comparator definitions | Strong; metric is set-identity only |
| `scripts/historical_replay.py` | Replay harness, A_AI map (`:66-71`), vessel thresholds (`:57-61`) | Medium | Contains a **tautological "safety" check** at `:246` and four stale docstrings |
| `data/raw_weather_sea.csv`, `raw_marine_era5_sea.csv`, `raw_marine_mfwam.csv` | Sea-cell environmental record; 43,848 / 43,848 / 28,512 hourly rows | **High** — the sampling frame | Strong; SHA-256 verified against manifest; **reanalysis only** |
| `data/raw_weather.csv`, `raw_rainfall.csv`, `raw_marine.csv`, `raw_tide_marea.csv` | Land-cell v1 files; tide series | Low — superseded or unused | **Not in the manifest**: no checksum, no dictionary entry |
| `data/c8/aai-2026-reproducibility-manifest.json` | Data dictionary, checksums, config, limitations | **High** — provenance | Strong but covers **3 of 7** raw CSVs |
| `data/solar/solar-events-daily.csv` | 1,827 daily sunrise/sunset rows, self-certifying via `impl_sha256` | Medium | Strong |
| `data/journal1-layer3-prototype/batch5-fidelity-evaluation/fidelity-traces.csv` | 292-episode census, 454 advisory records | **High** — candidate message pool | Strong provenance; **no payload/explanation column** |
| `.../state-space-manifest.json` | 486 raw combinations → 292 primary episodes (32 SAFE, 260 CAUTION), 162 gated UNSAFE | **High** — ready case library | Strong |
| `docs/canonical/evaluation-design-rq4.md` | 20 hand-built scenarios in five categories | Medium — reusable stimuli | **Banner-marked SUPERSEDED** (`:1`); all 20 use `v = big` |
| `docs/canonical/rq5-study-design.md` | User-study design, 12–15 participants | Medium — pilot template | **Design only; never executed; ethics not applied for** (`:176`) |
| `docs/canonical/data-provenance.md` | Per-variable source, model, grid cell, fitness | **High** | Strong; states the threshold/measurement mismatch at `:12` |
| `docs/canonical/decision-record-empirical-first.md` | Q1–Q8 decision record | **High** — the ground-truth question | Strong; `:81` is the key admission |
| `docs/canonical/finding-met-*.md`, `finding-gt-*.md` | Threshold provenance audits | **High** — source-grounding status | Strong; explicitly label unsourced values |
| `docs/canonical/review-protocol.md` | Literature-coding protocol | Medium | `:142` — single coder, **no inter-rater reliability** |
| `docs/analysis/threshold-sensitivity-analysis.md` | Deterministic threshold perturbation | Medium | `:258` headline on a steep gradient; `:260` nothing establishes correctness |
| `docs/analysis/primary-source-verification-audit.md` | Evidence–claim alignment audit | **High** | `:115` observation-quality semantics **not evaluated** |
| `data/journal1-post-fidelity-plan/utility-construct-assessment.md` | Utility construct analysis | **High** | `:136` `UTILITY_CONSTRUCT = DEFER_TO_HUMAN_STUDY` |
| `publications/active/journal-1/evaluation-specification.md` | Maintained design authority | **High** | `:150` Delay-only; `:190` utility OPEN; `:288` non-claims |
| `docs/analysis/graduated-advisory-safety-novelty-assessment.md` | The proposed study's scoping assessment | **High** | **Untracked**; proposal only, zero execution |
| `scripts/README.md` | Documents an issue-time collector (`kawasan_perairan_collector.py`) and its schema | — | **The script and its output do not exist and never did** (no git history) |
| `research/` | — | — | **NOT FOUND** — created by this audit |

---

## 4. Pilot Preparation Checklist

### 4.1 Define Advisory Task — **PARTIALLY READY**

**Existing evidence.** The task is defined to an unusually high standard for a project at this stage.

- *Decision:* pre-departure go/no-go for a small-scale coastal fisher at Kota Kinabalu (5.98° N, 116.01° E). `publications/active/journal-1/submissions/v1-initial-submission/manuscript.md:255`.
- *Recommendation space:* R = {Go, Delay, DepartureTime, Duration}, Definition 5.6, `manuscript.md:469`; `appendix-c-formalisation.md:771-777`.
- *Vessel classes:* by gross registered tonnage after Yunus (2007) via Yaakob et al. (2015) — small < 10 GRT, medium 10–25, big > 25, with nominal LOA ranges and operating zones (`appendix-c-formalisation.md:21-29`). `v` is a configuration parameter, not a time-varying observation (`:31`); there is **no `g_v`** (`:621`).
- *Classification rules:* every threshold is specified and the implementation agrees with the specification term by term — g_w 21.6/27.0 kn, g_r 10.0/20.0 mm/hr with the storm disjunct κ = χ(c) for WMO codes {95,96,99}, g_o 1.0/1.25 m for the small class, g_t half-open sunrise ≤ t < sunset with `Im(g_t) = {SAFE, UNSAFE}`, aggregation by max-severity, declared exclusion D = {m} pinned at SAFE with all severity figures reported as lower bounds (`appendix-c-formalisation.md:274-306, 483-512, 546-564, 633-645`; `scripts/historical_replay.py:41,49,74-76,92-94,102-105`; `scripts/condition_comparison.py:160-166`; `scripts/canonical_gt.py:97-106`).
- *Permitted categories:* A_AI(SAFE) = FULL ⊃ A_AI(CAUTION) = {Go, Delay} ⊃ A_AI(UNSAFE) = ∅ (`appendix-c-formalisation.md:781-789`; `governance/rule_set_provider.py:35-48`).
- *Human authority:* unconditional, stated consistently in documentation and enforced in code — *"A Go advisory is NOT a departure approval. A Delay advisory is NOT a prohibition"* (`governance/advisory.py:20-24`; `manuscript.md:114,243,291,849,1008`).

**Missing requirements.**

- **Forecast horizon / lead time — NOT FOUND.** Zero occurrences of `forecast`, `lead_time` or `issue_time` in any `.py` file under `scripts/`, `governance/` or `tests/` (verified directly). The only horizon language in the corpus is motivational prose explaining why DepartureTime and Duration are withheld, and that sentence was itself replaced during a consistency audit (`data/publication-consistency-audit/resumed/audit-table-continuation.csv:19`).
- **Freshness budget `ageᵢ` deliberately unparameterised.** *"ageᵢ is a specified parameter per component, and no value is proposed here"* (`appendix-c-formalisation.md:242`, verified). Without it, staleness cannot be expressed at all — the classifier signature has no place for it (`docs/canonical/finding-bottom-semantics.md:61`).
- **The departure window is a researcher-defined evaluation parameter**, not an observed departure period: five hourly timestamps 05:00–09:00 inclusive (UTC+8), `(d.hour >= 5) & (d.hour <= 9)`, repeated in seven scripts. *"Because this window has not been validated against observed fisher departure behaviour, it is treated as an evaluation design parameter"* (`publications/active/ipsci-2026/submissions/extended-abstract-2026-09-16/extended-abstract.md:114`).
- **Tide is absent from E** despite Gao (2024) finding Penang fishers rate tide highest at 4.55/5, above weather at 3.75 (`appendix-c-formalisation.md:1061`). Tide data was collected (`data/raw_tide_marea.csv`) and is read by no classifier.

**Scientific risks.**

- Roughly 40% of the evaluation window is pre-sunrise and therefore UNSAFE by construction — computed sunrise ranges 05:59–06:32 across the year, the 05:00 hour is pre-sunrise on every day, and sunrise falls inside the 06:00 hour on 348 of 365 days, so *"2 of the 5 window hours (40.0%) are UNSAFE by the non-daylight policy alone"* under an hour-start convention (`publications/active/aai-2026/drafts/aai-2026-independent-presubmission-audit.md:161-165`). Two of five window hours are definitionally gated before any weather is consulted. A reviewer will ask why the denominator includes them.
- `g_t` accounts for 86.82% (PRIMARY) / 90.19% (RESOLUTION) of all-hours non-SAFE classification (`docs/canonical/report-c8-migration-2026-09-08.md:145`). The gate is, to first order, a clock.
- Applying length-parameterised guidelines (Jeong & Im; Yaakob) to a tonnage-defined class is a **researcher-defined transfer**, declared as such (`aai-2026-revision-change-control.md:67`). There is no length↔tonnage conversion formula in the repository.

**Recommended next actions.** Define a forecast horizon and an `ageᵢ` per component with sourced justification before RQ3 can be posed at all; state the window convention and timezone explicitly in the protocol; decide whether pre-sunrise hours belong in the eligible denominator and pre-register that decision; record vessel class, loading, route and shelter per episode as the reference layer will require them.

---

### 4.2 Audit Available Data — **NOT READY**

**Existing evidence.** Seven raw CSVs at `data/` root, all at 5.98° N, 116.01° E, `Asia/Kuching`:

| File | Cell returned | Coverage | Rows | Variables | Source |
|---|---|---|---|---|---|
| `raw_marine_era5_sea.csv` | 6.0, 116.0 | 2020-01-01 → 2024-12-31, 1 h | 43,848 | wave_height, wave_period | Open-Meteo marine, `era5_ocean`, `cell_selection=sea` |
| `raw_marine_mfwam.csv` | 5.958336, 116.04167 | 2021-10-01 → 2024-12-31, 1 h | 28,512 | wave_height, wave_period | Open-Meteo marine, `meteofrance_wave` |
| `raw_weather_sea.csv` | 5.940246, 116.025 | 2020-01-01 → 2024-12-31, 1 h | 43,848 | wind_speed_10m, direction, gusts, precipitation, weather_code | Open-Meteo **archive** (ERA5) |
| `raw_marine.csv` | 6.0, 116.0 | 2020–2024, 1 h | 43,848 | wave_height, period; 4 columns **100% NaN** | v1, superseded |
| `raw_weather.csv`, `raw_rainfall.csv` | 5.940246, 116.100006 (**land**) | 2020–2024, 1 h | 43,848 each | as above | v1, superseded |
| `raw_tide_marea.csv` | — | 2020-01-01T08:00 → 2025-01-01T07:20 | 43,855 | tide_height_m | Marea API, MSL |

SHA-256 for the three manifested files was recomputed during this audit and **matches** `data/c8/aai-2026-reproducibility-manifest.json`. A derived solar artefact (`data/solar/solar-events-daily.csv`, 1,827 rows) self-certifies against its generator's hash.

**Missing requirements — the decisive ones.**

- **Issue-time forecast records — NOT FOUND.** Every environmental file is a single best-estimate valid-time series with one row per hour. There is no (issue time, valid time) pair, no lead time, no forecast reference time. All three retrieval endpoints are `https://archive-api.open-meteo.com/v1/archive` or the marine archive. The repository states the consequence itself: *"The thresholds come from MET Malaysia. The measurements come from ERA5 reanalysis"* (`docs/canonical/data-provenance.md:12`, verified), and *"Reanalysis on its own cannot represent the information available to an operator at decision time"* (`docs/analysis/graduated-advisory-safety-novelty-assessment.md:124`).
  A collector that would have produced issue-time records is fully specified in `scripts/README.md:3-39` with a column dictionary at `:71-89`. **The script, its output file and its log do not exist, and `git log --all` shows they never did.** The intended source "only displays the current 7-day forecast with no historical archive, data must be collected **prospectively**" (`docs/implementation/data-source-met-malaysia.md:155`).
- **Independent observed hazard evidence — NOT FOUND.** No incident, capsize, SAR, accident, near-miss or buoy record for the site exists in `data/`, `docs/`, `notes/` or `papers/`. `docs/canonical/decision-record-empirical-first.md:81` (verified): *"Q7 — Is there any ground truth to validate against? Nothing… There is no incident data for Kota Kinabalu… Consequence: the evaluation is a CHARACTERISATION, not a VALIDATION."* MMEA and Department of Fisheries Malaysia appear only as **candidate** sources.
- **Degraded / missing / stale / noisy inputs — represented formally, never exercised.** The ⊥ semantics, the freshness predicate and the fail-safe resolution are fully specified, and value-level fault handling is implemented and tested (`governance/reasoning_engine.py:56,96-116`; `tests/test_governance_engine.py:1059-1087`). But the analysis pipeline's only real missing-data handling is **row deletion**: `dropna(subset=[...])` in eleven scripts. No imputation, no interpolation, no noise injection, no dropout anywhere. The repository names the gap precisely: *"The element that best survives primary-source verification — observation-quality semantics (G3) — is the one the experiment does not test… no hour manipulates staleness, invalidity or resolution"* (`docs/analysis/primary-source-verification-audit.md:115`, verified). Fault injection was deliberately deferred pending a sourced `ageᵢ`: *"Fault injection (staleness / invalidity) | NOT JUSTIFIED — yet | Requires inventing `ageᵢ`, which is OPEN"* (`docs/analysis/research-chain-lock.md:205`; repeated at `docs/analysis/rq-finalisation.md:107`). The minimum credible test is specified at `docs/analysis/g3-literature-falsification.md:130`.
- **Vessel-specific linkage — NOT FOUND.** No vessel registry, trip record, fleet file or vessel identifier. `v` is a three-valued configuration parameter and nothing more (`docs/canonical/data-provenance.md:118-123`: *"Not measured — a fixed registry attribute set per scenario"*).
- **`m` (marine warning) is unmeasured**, held at SAFE throughout under the declared exclusion D = {m}: *"Source | NONE — no historical data exists"* (`data-provenance.md:51`, verified). Because aggregation is by maximum, **every severity figure in the project is a lower bound**. Separately, the storm route is empirically unexercised: `weather_code` returns zero activating codes (95/96/99) in five years (`data-provenance.md:45`).

**Two defects found by this audit that no repository file records.**

- **Tide timestamp drift.** `raw_tide_marea.csv` contains three distinct minute-of-hour values (0, 20, 40) because `MAX_DURATION_MINUTES = 260_000` (`scripts/tide_marea_download.py:39`) is not a multiple of 60, so each chunk starts 20 minutes later; the series also overruns its stated end date to 2025-01-01T07:20. Consequence: tide rows will not join to the hourly `time` keys without re-gridding. Not currently harmful — no classifier reads tide — but it would bite immediately if tide entered E. `REQUIRES VERIFICATION` by the author before any use of this file.
- **A live third-party API key is committed in plaintext** at `scripts/tide_marea_download.py:27`. This is a repository-hygiene issue independent of the pilot and should be rotated and removed from history.

A third discrepancy: `docs/canonical/data-provenance.md:148,159` gives the v1-weather↔ERA5 cell separation as 12.9 km while `scripts/collect_raw_v2.py:191-192` prints 12.3 km. Independent haversine recomputation during this audit gives **12.90 km** — the provenance document is correct and the script string is stale.

**Scientific risks.** Any robustness result produced from this repository today would be *synthetic perturbation of a reanalysis series*, which the proposal itself identifies as low novelty (`graduated-advisory-safety-novelty-assessment.md:87`: *"Generic noise injection offers low novelty"*). Reanalysis is also systematically *better* than an operational forecast, so perturbing it understates real degradation by an unknown amount.

**Recommended next actions.** Begin prospective collection of issue-time forecasts now — every month of delay is a month of data the study will not have, and no retrospective action can recover it. Approach MMEA and the Department of Fisheries Malaysia in writing for incident records, and treat a negative answer as a study-design input rather than a setback. Extend the reproducibility manifest to all seven raw files.

---

### 4.3 Prepare Candidate Advice — **NOT READY**

**Existing evidence.** The generation mechanism works and is well engineered. There is exactly one `Advisory` construction site (`governance/reasoning_engine.py:301-309`); advisories carry type, payload, attributing `rule_id` and explanation; the type universe is `{Go, Delay, DepartureTime, Duration}` (`governance/rule.py:12-14`); and every episode is validated for A_AI containment before reasoning begins (`governance/rule_set_provider.py:206-216`). Outputs are persisted with SHA-256 manifests, and determinism is enforced at runtime with a hard failure on violation (`scripts/journal1_e5_benchmark.py:279-314`).

**Missing requirements — the decisive ones.**

- **The output is `Delay`-only.** All four implemented rules declare `conclusion_type="Delay"` (`governance/canonical_rules.py:88,120,155,191` — verified directly). The only `Go` rule, `R-SAFE-001`, is in `DEFERRED_RULES` and never loaded (`:52`). Verified across the full census: of 292 episodes, **244 emit `["Delay"]` and 48 emit `[]`; zero emit Go, DepartureTime or Duration**; 454 advisory records in total, all `Delay`.
- **The collapse is inverted relative to the permitted sets.** `select_rule_set` returns rules whose `applicable_state` matches; since every loaded rule is a CAUTION rule, `select_rule_set(repo, "SAFE")` returns `[]` for every SAFE episode (`governance/rule_set_provider.py:160-178`). So:

  | State | A_AI (permitted) | Rules loaded | Types actually emitted |
  |---|---|---|---|
  | SAFE | {Go, Delay, DepartureTime, Duration} | **∅** | **none, always** |
  | CAUTION | {Go, Delay} | 4 | **Delay only** |
  | UNSAFE | ∅ | ∅ (gate off) | none |

  The study needs to measure what graduated restriction *removes*. The unrestricted arm removes nothing because it produces nothing.
- **The system cannot emit inappropriate recommendations.** Compliance is enforced by construction, with the invariant documented at `governance/advisory.py:14-18` and three absence conditions asserted as PASS criteria (`scripts/journal1_layer3_fidelity_evaluation.py:779-781`) and locked by tests (`tests/test_governance_engine.py:849-868,939-945`). A safety study requires a generator that *can* produce unsafe output; this one is designed so that it cannot.
- **The same candidates cannot be replayed across governance configurations.** Two disjoint worlds exist. `scripts/condition_comparison.py` replays 43,848 hours across C0/C1/C2/C3 but compares only *permitted sets* — the metric is literally frozenset inequality (`:195-202`). `scripts/journal1_layer3_fidelity_evaluation.py` runs the engine, but `execute_episode` takes no governance parameter and reads a module-level `GOVERNANCE_MAP` that is never injected or overridden (`governance/reasoning_episode.py:152-173`; `governance/rule_set_provider.py:146-157`). The engine is hardwired to C2. **Nothing bridges them.**
- **Recommendation content is not logged.** The trace schema has `advisory_conclusion_types` and `advisory_record_count` but **no payload and no explanation column** (`scripts/journal1_layer3_fidelity_evaluation.py:607-618`). The text a rater would judge is never persisted. Separately, `DepartureTime` and `Duration` payload fields are recorded as `OPEN` with no authority identified (`data/journal1-layer3-prototype/recommendation-semantics-batch2.csv`; `publications/active/journal-1/layer3-prototype-specification.md:678`).
- **No LLM, prompt or learned model exists**, and none is needed. The pipeline is deterministic rule evaluation over two dependencies, `pandas` and `numpy`. This is a *strength* for reproducibility and should be preserved; the proposal agrees (`graduated-advisory-safety-novelty-assessment.md:130`).

**A defect found by this audit.** `scripts/historical_replay.py:246` (verified): the "SAFETY DOMINANCE COMPLIANCE" check is `ok = all(A_AI[s] <= A_AI[s] for s in set(f))` — each set compared to itself, unconditionally `True`, and the result never used. The section header promises a compliance check that the code does not perform. Harmless to published figures (nothing depends on `ok`), but it must not be cited as evidence of anything.

**Discrepancies between documentation and code.** `scripts/condition_comparison.py:343` still states *"the reasoning engine is not implemented"* (verified) — stale since the F1–F3 closure of 11 September 2026. The dependent claim (AI(E) content is not compared) remains true, so no result is invalidated, but the stated reason is wrong and would mislead a reviewer. `tests/test_governance_engine.py:843` has a docstring claiming R-CAUTION-002/003/004 are not loaded; they are. `scripts/historical_replay.py:97-99,11,88-90` carry three further stale docstrings. The excluded component `m` has **three unreconciled representations** across layers — `SAFE` in the formalisation (`appendix-c:296`), a distinct `EXCLUDED` marker required by the Layer 3 interface (`layer3-prototype-specification.md:242`), and `None` in the engine (`governance/canonical_rules.py:17-19`).

**Scientific risks.** The Delay-only configuration is not an implementation oversight to be patched quickly. Each missing rule is missing because the repository found **no scientific authority** for it: `OPEN-L3-1C` (DepartureTime), `OPEN-L3-1D` (Duration), `GAP-03` (Go under CAUTION) (`governance/canonical_rules.py:22-27`, verified). Populating the candidate pool means either sourcing that authority or declaring the candidates as researcher-defined study instruments — and the second choice must be disclosed, because it moves the candidate generator inside the circle of researcher judgement that the independent reference is supposed to stand outside.

**Recommended next actions.** Build the candidate generator as a **separate study instrument**, explicitly outside the governed architecture, capable of emitting all four types including deliberately over-specific or hazardous ones; log full payload text; parameterise `execute_episode` with a governance configuration so the identical candidate set can be replayed under U / B / G / B-tuned; and freeze whether filtering deletes, reranks or substitutes before any data is scored.

---

### 4.4 Develop Independent Safety Reference — **NOT FOUND**

**Existing evidence.** Threshold *provenance* is documented to a high standard — every boundary is traced to a named source, with dedicated audits for the hydrodynamic gap, the rainfall lower boundary and the solar rule (`docs/canonical/finding-met-hydrodynamic-gap.md`, `finding-met-lower-boundary-gap.md`, `finding-gt-provenance-audit.md`). Each executable rule carries a provenance string and an evidence level (`governance/canonical_rules.py:96-102,128-137,163-173,199-209`).

**But provenance is not validation, and the repository says so**: *"Every threshold is anchored to a named source… **Anchoring is not validation.** No threshold was optimised against an outcome, because no outcome data exists… The thresholds are defensible in provenance and untested in effect"* (`publications/active/journal-1/submissions/v1-initial-submission/manuscript.md:1468`).

**Missing requirements.** Searched repository-wide for expert, rater, inter-rater, kappa, annotation, ethics, IRB, consent, interview, survey, questionnaire, panel, validation and ground truth:

| Artefact | Status |
|---|---|
| Expert judgement records | **NOT FOUND** |
| Domain-expert or maritime-authority review | **NOT FOUND** |
| Fisherman / skipper input collected by this project | **NOT FOUND** (all fisher data is cited from third-party studies at other sites) |
| Interview / survey / questionnaire data | **NOT FOUND** |
| Ethics approval | **NOT FOUND — not applied for.** *"An ethical approval application is required before recruitment begins"* (`docs/canonical/rq5-study-design.md:176`, verified); still a future milestone at `docs/admin/part-ii-research-goals.md:120-121` |
| Consent forms, participant information sheets | **NOT FOUND** — *"Prepare…"* (`rq5-study-design.md:187`) |
| Rating rubric | **NOT FOUND** — proposed at `graduated-advisory-safety-novelty-assessment.md:120` |
| Inter-rater reliability | **NOT FOUND.** *"Coding was performed by a single reviewer (the thesis author). No dual-coding audit was performed on any sample, so inter-rater reliability is not available"* (`docs/canonical/review-protocol.md:142`, verified) |
| Ground-truth safety labels | **NOT FOUND** |

**A terminological warning for anyone searching this repository.** `kappa` / κ appears roughly sixty times and is **always the formal model's storm indicator χ(c) ∈ {0,1}**, never Cohen's kappa (`data-provenance.md:43`). Likewise, "expert-derived" at `docs/implementation/dataset-label-derivation.md:219` means *the thesis author mapping published qualitative descriptions onto MET bands*, not expert elicitation. Neither should be read as evidence of expert involvement.

**The repository's own position** is that no proxy may be constructed: ground-truth correctness *"requires knowing whether each departure decision in the historical record was actually safe — this is not recorded in the replay data"*; decision quality *"requires domain expert judgement or a validated reference benchmark"*; *"A proxy is an invented formula"*; verdict `UTILITY_CONSTRUCT = DEFER_TO_HUMAN_STUDY` (`data/journal1-post-fidelity-plan/utility-construct-assessment.md:88,90,97,136` — `:136` verified). The maintained specification repeats the instruction: *"Do not invent a utility formula"* (`publications/active/journal-1/evaluation-specification.md:190`, verified).

**Circular evaluation risks — identified precisely.**

| Proposed comparison | Circular? | Mechanism |
|---|---|---|
| Gate output vs the 20 expected states in `evaluation-design-rq4.md:116-179` | **Fully circular** | The expected-S column is computed by applying the gate's own thresholds to the E-vectors |
| Gate output vs the `Go / Delay / AI_off` labels in `dataset-label-derivation.md` | **Circular** | `:215` (verified): the labels use *"the same thresholds used to anchor the UNSAFE classification boundary… to ensure internal consistency between f(E) and the advisory AI's training labels"* |
| Gate output vs Jeong & Im Hs_KIMO, Yaakob NORDFORSK, MET Cat 1/2, MET Ribut Petir, JPS/DID, COLREGs 20(b) | **Circular** | Each is a *Basis* cell of the gate's own threshold table |
| F1/F2/F3 fidelity results read as safety evidence | **Category error** | *"The fidelity criteria do not empirically rediscover Safety Dominance. They test whether the implementation conforms to the specification"* (`evaluation-specification.md:282`); F1/F2 are analytically zero |
| C1 vs C3 divergence = 0.00% | **Admitted tautology** | Identical dictionary literals (`evaluation-baseline-decision.md:24-31`) |
| Δ_L2 read as a governance result | **Near-tautological** | Equals P(S = CAUTION) by construction; a property of the classifier, not of the contract |

**A construct-validity risk that survives even a successful expert panel**, already flagged in the project's own proposal and worth restating because it is the subtlest threat here: *"Experts ratify the same rules or classify a rule-compliant generic statement as safe useful advice"* (`graduated-advisory-safety-novelty-assessment.md:155`). Local skippers plausibly hold the same mental thresholds that MET publishes. If they do, an expert reference is only *procedurally* independent, not *substantively* independent. The protocol must test for this — for example by recording rater-stated thresholds before rating and reporting the agreement between rater judgements and gate output as a diagnostic, not as validation.

**Four self-assessments that must not be contradicted in any future write-up.** The repository classifies these as unvalidated; describing them as validated maritime criteria would be a misrepresentation of the project's own record:

1. The `g_t` boundary — a navigation-lights rule repurposed by policy choice. *"night ⇒ suppress AI advisory is an architectural governance policy choice. It is not an evidence-derived safety fact"* (`docs/canonical/finding-unsafe-semantics-audit.md:168`).
2. The 10.0 mm/hr rainfall SAFE/CAUTION onset — a hydrological (non-MET) intensity limit; MET publishes no lower hourly rate (`finding-met-lower-boundary-gap.md:23,60`).
3. The medium-vessel 1.4/2.8 m band — *"The medium-vessel boundary is interpolated"* (`publications/active/journal-1/submissions/v1-initial-submission/manuscript.md:1470`); described elsewhere as *"a conservative interpolation"* (`publications/active/ipsci-2026/submissions/v3-revision/manuscript-v3.md:531`).
4. A_AI(CAUTION) = {Go, Delay} — *"a researcher-defined design choice… not empirically validated, shown correct, shown optimal, or established as safer"* (`publications/active/aai-2026/drafts/aai-2026-manuscript-v1-phase2.md:5`), and formally under-determined: {DepartureTime, Duration} satisfies every stated constraint while inverting the rationale (`audit-M2-delta-l2-participation-vs-scope-investigation.md:309`).

**Recommended next actions.** Treat the reference layer as the study's principal construction task, not a step within it. Separate the **ex ante** reference (was this specificity supportable from information available at issue time?) from the **ex post** hazard reference (would following it have exposed the operator to verified concerning conditions?), and keep future measurements out of the ex ante dossier. Submit the ethics application now — it is on the critical path of every remaining option, and nothing involving a human rater can begin without it.

---

### 4.5 Plan Blinded Pilot Assessment — **NOT READY**

**Existing evidence — what genuinely exists.**

- A ready case library: 486 raw component combinations reduced to **292 primary episodes** (32 SAFE, 260 CAUTION) plus 162 gated-UNSAFE cases, with full enumeration provenance (`.../batch5-fidelity-evaluation/state-space-manifest.json`).
- A message pool of 454 advisory records across 292 episodes (`fidelity-traces.csv`) — *types only, no text* (§4.3).
- 20 hand-built scenarios in five categories, including 3 boundary and 2 adversarial cases (`docs/canonical/evaluation-design-rq4.md:112-179`) — **usable as stimuli only after discarding the expected-S column**, and the document is banner-marked `⚠️ SUPERSEDED 2026-09-06 — do not build from this document as-is` (`:1`, verified), with all 20 scenarios using `v = big` rather than the deployment class.
- Three decision tasks DT-SAFE / DT-CAUTION / DT-UNSAFE with display wording (`docs/canonical/rq5-study-design.md:73-77`).
- A 43,848-hour sampling frame with verified checksums.
- A methodological precedent for pre-registration: `data/prediction-register.csv`.

**Missing requirements.** Every component specific to blinded assessment:

| Requirement | Status |
|---|---|
| Independent reference labels | **NOT FOUND** |
| Rating rubric / severity scale | **NOT FOUND** — proposed only |
| Raters recruited | **NOT FOUND** |
| Blinding and randomisation procedure | **NOT FOUND** — proposed only |
| Inter-rater agreement plan and statistics | **NOT FOUND** |
| Actionability measure | **NOT FOUND** |
| Missing-advice / fallback assessment | **NOT FOUND** |
| Ethics approval | **NOT FOUND — not applied for** |

The design for all eight is sketched in a single untracked document (`graduated-advisory-safety-novelty-assessment.md:110-130`), dated the same day as this audit. **Nothing has been executed.**

**Has expert validation already occurred? NOT FOUND.** No ethics approval exists, so no human-participant work could lawfully have taken place. `publications/active/journal-1/submissions/v1-initial-submission/manuscript.md:1547`: *"No human evaluation was conducted."* The IPoSCI extended abstract states human-participant collection *"will commence only after the required institutional procedures"* (`:124`). The only external human review on record is academic supervision.

**Scientific risks.** A 30–50 scenario pilot drawn from the 292-episode library would be a *synthetic* state-space census, not a sample of real conditions — the repository is explicit that activation counts there *"are counts within the synthetic fidelity state space, not real-world prevalence estimates"* (`.../report.md:247`). Scenarios drawn instead from the 43,848-hour replay are real but, as §9.2 shows, heavily clustered. Both routes are defensible; they answer different questions and must not be mixed in one denominator.

**Recommended next actions.** Run a **rubric-development and rater-calibration pilot** rather than a safety-effectiveness pilot: develop the rubric with raters who have not seen the gate, rate a small scenario set, and measure whether raters can reliably distinguish the four categories the study depends on (plausibly hazardous specific advice; useful lower-specificity guidance; harmful omission; justified silence). That is exit criterion 2 of the project's own assessment, and it is the one test that can be run without issue-time data, without incident records and without a populated candidate pool — though still not without ethics approval.

---

### 4.6 Check Experimental Feasibility — **NOT READY**

**Comparator availability.**

| Arm | Status | Evidence |
|---|---|---|
| Unrestricted AI (C0 / U) | **Admissible-set level only** | `scripts/condition_comparison.py:81-113`; no candidate content |
| Participation-only gating (C1 / B) | **Admissible-set level only** | same |
| Graduated gating (C2 / G) | **Set level + engine, hardwired** | `governance/rule_set_provider.py:35-48`; engine runs C2 only |
| Calibrated binary abstention (B-tuned) | **NOT FOUND** | No abstention, reject-option, selective-prediction, calibration or coverage code anywhere |

For the fourth arm the negative evidence is exhaustive and was verified directly: zero `abstain` hits in any `.py`; one `calibrat` hit, which says the opposite (*"They are not calibrated"*, `scripts/threshold_comparison.py:101`); one `confidence` hit, which is *"Confidence intervals: NOT_REQUIRED"*; four `coverage` hits, all about data coverage or a figure check. **The pipeline produces no confidence score, probability or uncertainty estimate of any kind**, so there is nothing to threshold a calibrated abstention policy on. Within this repository, "abstention" names the night-time policy, not a baseline.

**Coverage and usefulness — not measured, and currently prohibited.** The only metric the harness computes is pairwise admissible-set divergence (`scripts/condition_comparison.py:191-202`). Decision-support utility is formally OPEN with an instruction not to invent one (`data/journal1-evaluation-specification/metric-audit.csv:4`; `evaluation-specification.md:190,310,321`). The required definition of useful coverage exists only in the untracked proposal (`graduated-advisory-safety-novelty-assessment.md:126`).

**Can the same inputs and candidates be used consistently?** Inputs yes — one loader, one classifier, and the same window mask in seven scripts. Candidates **no**: the comparator harness never invokes the engine, and the engine cannot be configured.

**Limitations against the brief's seven named risks.**

| Risk | Finding |
|---|---|
| Insufficient CAUTION cases | **Confirmed, and worse than the hour count suggests** — 531 PRIMARY CAUTION hours fall on 201 days / ~85–123 independent events (§9.2) |
| Lack of candidate diversity | **Confirmed** — one type emitted, zero in the unrestricted arm |
| Missing independent safety labels | **Confirmed** — none exist |
| Limited observation of actual operational conditions | **Confirmed** — reanalysis only; no issue-time data; no vessel or trip records |
| Insufficient independent experimental episodes | **Confirmed** — see §9.2; hours are not independent observations |
| Inability to measure actionable advice retention | **Confirmed** — construct OPEN, no payload logged, no actionability instrument |
| Missing provenance or reproducibility information | **Partially mitigated** — strong for 3 of 7 raw files and for the Layer 3 artefacts; the manifest itself records that *"EXTERNAL reproducibility is NOT established"* and that re-collection will not reproduce the original bytes |

**Recommended next actions.** Decide whether B-tuned is in scope at all. It requires a risk score, a calibration split and a fallback model, none of which exist; and the repository notes that significance testing over a deterministic census is not meaningful (`evaluation-baseline-decision.md:138-144`), so a calibration/test split must be constructed deliberately by site or time block rather than assumed.

---

## 5. Data Readiness Assessment

**Available and fit for purpose.** The sea-cell environmental record is the project's strongest asset: 43,848 hourly rows over five calendar years with verified checksums, a machine-readable data dictionary, documented grid-cell separations and a resolution cross-check at ~8 km over 3.25 years. The solar artefact is reproducible to the row. This is a sound **sampling frame** for episode construction and for checking the climatological representativeness of any scenario set.

**Missing variables and records.**

| Required for the proposed study | Status |
|---|---|
| Issue-time forecasts with lead time | **NOT FOUND** — and unobtainable retrospectively |
| Observed hazard outcomes (incidents, SAR, near-miss) | **NOT FOUND** |
| Marine warning archive (`m`) | **NOT FOUND** — D = {m}; all severity figures are lower bounds |
| Vessel / trip / fleet records | **NOT FOUND** |
| Observed fisher departure behaviour | **NOT FOUND** — the window is unvalidated |
| Measured latency, staleness or channel-failure statistics | **NOT FOUND** |
| Tide as a classifier input | Collected but unused; file has a join defect (§4.2) |
| Swell period | Collected, retained in E, does not enter `g_o` |

**Provenance.** Strong where documented, with three named gaps: the manifest covers 3 of the 7 raw CSVs; no retrieval timestamp was recorded at collection (`retrieval_timestamp: null`); and the Copernicus product lineage asserted in the manuscript citation is recorded as `"verified": false` — *"No request, response, manifest or log in the repository names the CMEMS product or its DOI."* That last item is `REQUIRES VERIFICATION` and should be resolved before any journal submission that cites the product.

**Suitability verdict.** Sufficient to **construct and characterise episodes**. Insufficient to **score them**, and insufficient to **represent decision-time information**. The first gap blocks RQ1 and RQ2; the second blocks RQ3 on real data.

---

## 6. Advisory Model Readiness

**What exists.** A deterministic, well-tested governance engine with by-construction containment guarantees, full SHA-256 integrity manifests, runtime determinism enforcement and a 292-episode exhaustive census closing F1–F3 at zero violations. For an architecture paper this is strong evidence. For a recommendation-quality study it is the wrong kind of evidence.

**Output diversity: one type.** 454 advisory records, every one `Delay`; 48 episodes with no output; zero `Go`, `DepartureTime`, `Duration`. The payload is a single `reason` string with no parameterised content — no time, no window, no hours.

**Why the gaps exist.** Not oversight. `OPEN-L3-1C`, `OPEN-L3-1D` and `GAP-03` each record that **no scientific authority was found** for the corresponding rule (`governance/canonical_rules.py:22-27`). `R-SAFE-001` was deferred as a `STATE_RESTATEMENT` — its antecedent is logically equivalent to S = SAFE under max-severity aggregation (`:39-55`).

**Governance comparators: present as data, absent as executable configurations.** The four admissible-set maps are defined once and duplicated verbatim in two further scripts. The engine reads a module-level constant and exposes no parameter. The measured quantity is set identity, which is invariant to the content of A_AI(CAUTION) — meaning the entire existing comparator apparatus is, by construction, unable to say anything about whether {Go, Delay} is the right restriction.

**Consequence for the study.** The architecture should be the **instrument**, and the candidate generator a **separate, declared study instrument** built outside it. Attempting to reach the candidate pool by adding rules to the canonical repository would import the authority gaps into the experiment and compromise the independence the study depends on.

---

## 7. Independent Safety Reference Assessment

**Existing evidence: none that is independent.** Every candidate inside the repository falls into one of three categories — the gate's own thresholds; a derivative of the same literature (MET Malaysia, Jeong & Im, Yaakob et al., COLREGs, JPS/DID); or a written plan. The closest thing to an independent-reference design in the entire corpus is a single table cell in an argumentation note — *"expert panel pre-classifies each scenario's safe decision envelope"* (`docs/justification/socio-technical-evaluation.md:132`) — in a document whose own header classifies it as *"Theoretical justification / argumentation note"*. No envelope, no panel, no classification exists.

**Requirements for a non-circular reference.** From this audit's analysis, a usable reference must satisfy all four:

1. **Source independence.** Thresholds justified separately from MET Cat 1/2, Jeong & Im Table 12, Yaakob's NORDFORSK limits, JPS/DID and COLREGs 20(b). Sharing *physical drivers* with the gate is acceptable and probably unavoidable; sharing *threshold values* is not.
2. **Information independence.** The ex ante dossier must contain only what was available at issue time. Any ex post hazard evidence must stay out of both the policy inputs and the ex ante dossier, with the two axes scored and reported separately.
3. **Procedural independence.** Rubric developed before raters see the gate; messages rated without policy identifiers or state labels; order randomised; a staged review checking whether wording reveals the treatment arm.
4. **Demonstrated discriminability.** Raters must be shown to distinguish hazardous specific advice, useful lower-specificity guidance, harmful omission and justified silence — with agreement reported *before* adjudication, and disagreement and indeterminate labels preserved rather than resolved away.

Condition 4 is the one that can be tested now, and condition 1 is the one most likely to fail quietly: if local skippers hold the same thresholds MET publishes, the reference is procedurally but not substantively independent. The protocol should measure that rather than assume it.

**No-go condition.** If safety labels can only be derived from the gate, the safety-effectiveness claim cannot be made at all. This audit reaches that conclusion independently; the project's own assessment states it in the same terms (`graduated-advisory-safety-novelty-assessment.md:171`).

---

## 8. Pilot Scenario Specification

**These are proposed scenario types, not experimental results. No scenario below has been constructed, run, rated or scored.**

Design principles. Scenarios should be drawn from the real 43,848-hour record wherever possible (for representativeness) and supplemented with constructed cases only where the real record is empty (notably the storm route and the marine-warning channel, which have zero and no observations respectively). Each scenario carries a **dossier** — vessel class, loading, route, shelter, available forecast at issue time, observation ages per channel — and the expected-state column is **withheld from raters**. Degraded-observation scenarios must be labelled as synthetic perturbations of reanalysis until issue-time data exists.

| # | Group | n | Scenario type | Construction source | Purpose |
|---|---|---|---|---|---|
| S-01…S-06 | **A. Clean SAFE** | 6 | All components SAFE, daylight, calm sea (wave < 1.0 m, wind ≤ 21.6 kn, no rain) | Sampled from real window hours | Establish the unrestricted baseline; detect over-restriction |
| S-07…S-14 | **B. Clean CAUTION** | 8 | CAUTION via ocean state alone (1.0 ≤ wave ≤ 1.25 m), all other components SAFE | Real; 518 of 531 PRIMARY CAUTION hours are ocean-state-driven | The primary contrast; the stratum where graduated restriction acts |
| S-15…S-17 | **C. CAUTION via rainfall** | 3 | 10.0 < precip ≤ 20.0 mm/hr, wave SAFE | Real but rare — only 13 of 531 hours | Component-attribution check; tests whether raters treat causes differently |
| S-18…S-21 | **D. UNSAFE** | 4 | One each: wave > 1.25 m; wind > 27.0 kn; precip > 20.0 mm/hr; pre-sunrise | Real | Tests justified silence and fallback adequacy |
| S-22…S-27 | **E. Boundary** | 6 | Exactly 1.00 m (inclusive onset); exactly 1.25 m; exactly 21.6 kn; exactly 27.0 kn; exactly 10.0 mm/hr; exact sunrise | Real where available — 97 PRIMARY hours sit at exactly 1.00 m | Probes whether rater judgement tracks the thresholds or diverges at the margin — a direct test of substantive independence |
| S-28…S-31 | **F. Missing data** | 4 | Wave channel absent; wind absent; solar lookup fails; two channels absent | Synthetic; engine resolves ⊥ → UNSAFE | Tests fail-safe behaviour and whether silence under fault is judged justified |
| S-32…S-35 | **G. Stale forecast** | 4 | Observation ages 3 h / 6 h / 12 h / 24 h past `ageᵢ`, conditions drifting across a threshold during the gap | Synthetic — **requires `ageᵢ` to be defined first** | The RQ3 core; currently unconstructable (§4.1) |
| S-36…S-39 | **H. Noisy inputs** | 4 | ±0.15 m wave bias near 1.0 m; ±3 kn wind near 21.6 kn; both; correlated block noise | Synthetic, magnitudes tied to documented model error | Tests boundary stability under plausible error |
| S-40…S-43 | **I. Conflicting information** | 4 | ERA5-Ocean and MFWAM disagree across a threshold; weather code contradicts precipitation rate; tide and wave suggest different risk; marine warning (hypothetical) contradicts measured state | Real for the wave-source disagreement — on the 5,935 matched hours the two wave products give binding rates 1.97 percentage points apart | Tests behaviour when the gate's inputs are not univocal |
| S-44…S-47 | **J. Adversarial / edge** | 4 | Rapid intra-window deterioration; conditions SAFE at 05:00 and UNSAFE at 09:00; sustained multi-day CAUTION; an event with no precedent in the record | Real where available | Stress cases for mechanism discovery |

**Total: 47 scenarios**, within the 30–50 range, distributed 27 real / 20 synthetic. Groups G and H cannot be built until `ageᵢ` and an error model are specified and sourced; until then the feasible set is **S-01…S-31 plus S-40…S-47 (39 scenarios)**.

**Sampling caution.** Group B should be drawn from *distinct weather events*, not distinct hours — with only ~85–123 independent PRIMARY events available (§9.2), eight scenarios drawn naively could easily come from two or three storms.

---

## 9. Experimental Feasibility Risks

### 9.1 Blockers that would prevent a meaningful PhD-level experiment

**B-1 — No independent safety labels (CRITICAL).** The primary endpoint cannot be measured. Every internal candidate is circular. *Blocks RQ1 and RQ2 entirely.*

**B-2 — No issue-time data (CRITICAL).** RQ3 concerns degradation relative to what was knowable at the decision point. Reanalysis cannot represent that, and no retrospective action can recover it. A study run on perturbed reanalysis would have to state that its degradation model is unvalidated against any observed failure — which the proposal itself identifies as low novelty. *Blocks RQ3 on real data.*

**B-3 — Degenerate candidate pool (CRITICAL).** One emitted type; the unrestricted arm emits nothing. The quantity the study wants to measure — what restriction removes — is currently zero by construction. *Blocks RQ1 and RQ2.*

**B-4 — No ethics approval (CRITICAL, and on the critical path).** Not applied for. Every route to B-1 passes through human raters. This is the longest-lead item in the project and nothing else can substitute for it.

**B-5 — No abstention comparator and nothing to calibrate it on (MAJOR).** The pipeline emits no confidence or probability. RQ2's comparator does not exist in any form. *Blocks RQ2.*

**B-6 — Useful coverage is formally undefined and its definition is currently prohibited (MAJOR).** The maintained specification instructs that no utility formula be invented on replay data. The construct must be defined with the reference panel, before test data are scored. *Blocks the shared denominator of RQ1 and RQ2.*

**B-7 — Recommendation content is not logged (MODERATE, tractable).** Raters judge text; the harness persists only type labels. A schema extension is required.

**B-8 — Precision (MAJOR).** See 9.2.

### 9.2 Independent-episode analysis — a computation performed by this audit

The brief asks specifically about "insufficient independent experimental episodes". No repository file quantifies this, so this audit computed it directly, reproducing the canonical classification pipeline read-only and outside the repository tree.

*Method:* `raw_weather_sea.csv` joined to the configured wave file, `dropna` on wave/wind/precip, the canonical small-vessel classifier (g_w 21.6/27.0; g_r 10.0/20.0 with the storm disjunct; g_o 1.0/1.25; `canonical_gt.g_t` imported from the repository; g_m pinned SAFE), max-severity aggregation, departure window `hour ∈ [5,9]`. **The method reproduces the published headline exactly — 531/9,135 = 5.81% PRIMARY and 266/5,935 = 4.48% RESOLUTION — which validates it against the project's own results.**

| Quantity | PRIMARY (ERA5-Ocean, 5.00 yr) | RESOLUTION (MFWAM, 3.25 yr) |
|---|---|---|
| Window hours | 9,135 | 5,935 |
| CAUTION hours (the binding set) | 531 (5.81%) | 266 (4.48%) |
| **Distinct calendar days** | **201** | **118** |
| Mean CAUTION hours per day (max) | 2.64 (3) | 2.25 (3) |
| **Independent events, gap > 1 day** | **123** | **80** |
| Independent events, gap > 2 days | 95 | 62 |
| Independent events, gap > 3 days | 85 | 54 |
| Days by year | 38 / 36 / 51 / 39 / 37 | 11 / 40 / 31 / 36 |

**Interpretation.** The headline "531 hours" overstates the available statistical material by roughly a factor of four to six. Weather is serially correlated; CAUTION hours arrive in clusters of two to three within a morning and in runs across consecutive days. For a paired comparison in which policies differ only on episodes with changed displayed advice, the effective sample is the number of **discordant independent events**, which is bounded above by ~123 (PRIMARY) and ~80 (RESOLUTION) and will be substantially smaller once discordance is required.

Note also that the maximum is 3 CAUTION hours per day out of 5 window hours — consistent with the ~40% of the window that is pre-sunrise and gated before weather is consulted.

**Consequences for design.**

- A 30–50 scenario pilot consumes a quarter to a half of the distinct PRIMARY binding events. Sampling must be deliberate and the frame documented, or the main experiment will reuse pilot episodes.
- Clustered resampling at the event or storm level is mandatory. Treating hours as independent would inflate precision by roughly the square root of the cluster factor.
- Power planning should assume on the order of 10² independent events, not 10³ hours, and should be based on pilot-measured discordance rather than on the 5.81% figure, which is a prevalence, not a discordance rate.
- External replication — a second coast or a different vessel/season mix — becomes more attractive for the same reason: it adds independent clusters rather than correlated hours.

*Status: computed by this audit, method stated, headline figures cross-validated against the repository's published results. The event-clustering figures themselves are new and `REQUIRE VERIFICATION` by the author before use in a manuscript.*

---

## 10. Prioritized Action Plan

### P0 — Required before any pilot

| # | Action | Addresses | Note |
|---|---|---|---|
| P0-1 | Submit the ethics application (`rq5-study-design.md:174-187` has the scope; consent forms and information sheets to be drafted in English and Malay) | B-4 | Longest lead time in the project; start first |
| P0-2 | Begin **prospective** issue-time forecast collection — implement the collector already specified in `scripts/README.md:3-39`, writing issue time, valid time, lead time and retrieval timestamp per record | B-2 | Every month of delay is unrecoverable data |
| P0-3 | Write formally to MMEA and the Department of Fisheries Malaysia requesting incident and near-miss records; record the response either way | B-1 | A negative answer is a study-design input, not a failure |
| P0-4 | Define the four rater-facing constructs — hazardous specific advice, useful lower-specificity guidance, harmful omission, justified silence — and the severity scale, **with raters, before any gate output is seen** | B-1, B-6 | Exit criterion 2 |
| P0-5 | Build the candidate generator as a separate declared study instrument, able to emit all four types including over-specific and hazardous candidates; log full payload text | B-3, B-7 | Must sit outside the governed architecture |
| P0-6 | Extend the trace schema with payload and explanation columns | B-7 | Small change; blocks rating without it |
| P0-7 | Pre-register the pilot: scenario frame, sampling unit (**event, not hour**), blinding, rater count, agreement statistic, and the practical margins | B-8 | Use `data/prediction-register.csv` as the precedent |

### P1 — Required before the main experiment

| # | Action | Addresses |
|---|---|---|
| P1-1 | Parameterise `execute_episode` with a governance configuration so one candidate set replays under U / B / G | B-3 |
| P1-2 | Source and justify `ageᵢ` per component, or declare RQ3 synthetic and bound the claim accordingly | B-2, §4.1 |
| P1-3 | Decide whether B-tuned is in scope; if yes, specify the risk score, the calibration split (by site or time block) and the fallback model | B-5 |
| P1-4 | Construct the ex ante / ex post reference separation and the per-episode dossier schema | B-1 |
| P1-5 | Define useful coverage with the reference panel and pre-register it | B-6 |
| P1-6 | Event-level power analysis using pilot-measured discordance | B-8 |
| P1-7 | Resolve the three representations of the excluded component (`SAFE` / `EXCLUDED` / `None`) into one documented convention | §4.3 |
| P1-8 | Secure an external regime — second coast, or a different vessel/season mix — for transportability | §9.2 |

### P2 — Desirable for journal quality and reproducibility

| # | Action |
|---|---|
| P2-1 | Rotate and remove the committed API key at `scripts/tide_marea_download.py:27`; purge from history |
| P2-2 | Fix the tide timestamp drift (`MAX_DURATION_MINUTES` not a multiple of 60) and the end-date overrun |
| P2-3 | Remove or correct the tautological "safety dominance" check at `scripts/historical_replay.py:246` |
| P2-4 | Correct the four stale docstrings (`condition_comparison.py:343`; `historical_replay.py:11,88-90,97-99`) and the test docstring at `test_governance_engine.py:843` |
| P2-5 | Extend the reproducibility manifest to all seven raw CSVs |
| P2-6 | Resolve the Copernicus product lineage (`"verified": false`) or remove the citation |
| P2-7 | Reconcile the 12.3 km / 12.9 km cell-separation discrepancy in favour of the provenance document |
| P2-8 | Retire or re-banner `docs/canonical/evaluation-design-rq4.md`; its expected-S column is a circularity trap for a future reader |
| P2-9 | Commit `docs/analysis/graduated-advisory-safety-novelty-assessment.md` — the study's only design document is currently untracked and one `git clean` from deletion |

---

## 11. Go / Revise / No-Go Recommendation

### **REVISE.** Proceed to a protocol and data-feasibility stage. Do not commit to the safety-effectiveness pilot.

**Why not Go.** Three of the study's required inputs — independent safety labels, issue-time observations, and a candidate pool capable of being wrong — are absent, and none can be produced from existing materials. A pilot run today would measure rule compliance, which the project has already established analytically and which the repository itself distinguishes from safety (`evaluation-specification.md:282`). It would also consume a quarter to a half of the available independent binding events (§9.2) to answer a question it cannot answer.

**Why not No-Go.** The proposed study addresses a real gap. The project holds an unusually strong instrument, a clean sampling frame, a ready case library and a disclosure culture that makes the weaknesses above visible rather than hidden. The no-go condition — *safety labels derivable only from the gate* — has not yet been tested. It becomes a No-Go only if P0-3 returns no outcome data **and** P0-4 shows that raters cannot distinguish the four constructs independently of the gate's thresholds. Both are answerable within months.

**What to run instead, now.** A **preparation pilot** with three deliverables and no safety claim:

1. **Rater calibration** — can blinded raters reliably distinguish hazardous specific advice, useful lower-specificity guidance, harmful omission and justified silence? Report agreement before adjudication. *This is the pivotal test; everything else is contingent on it.*
2. **Reference-independence probe** — using the boundary scenarios (S-22…S-27), measure whether rater judgement tracks the gate's thresholds or diverges at the margin. If it tracks them exactly, the reference is procedurally but not substantively independent, and that finding is itself worth reporting.
3. **Data-feasibility audit** — a matched-record check on whatever issue-time and incident data P0-2 and P0-3 return.

**Re-assess against four exit criteria** (these align with the project's own assessment at `graduated-advisory-safety-novelty-assessment.md:166-171`, reached here independently):

1. One well-defined predeparture decision with issue-time data and independent hazard evidence for enough materially different episodes.
2. Demonstrated rater discriminability across the four constructs.
3. Candidate diversity, enough changed delivered messages, and enough independent discordant **events** to estimate a materially sized effect — with a binary comparator that has access to the same evidence and realistic fallback.
4. Updated citation tracing around the independent-label comparison and documented overlap with the Journal 1 evidence plan.

**A note on publishability.** A rigorous negative or inconclusive result is publishable if the experiment can resolve the claimed advantage within useful margins. What is not publishable is a third comparison of admissible sets. The project's existing outputs have already extracted what the set-level analysis can yield; the remaining contribution is at the level of generated content, and that is exactly the level at which the project currently has no evidence.

---

## 12. Traceability Matrix

| Checklist requirement | Supporting project files | Missing evidence | Required action |
|---|---|---|---|
| **1a** Predeparture decision task | `publications/active/journal-1/submissions/v1-initial-submission/manuscript.md:255,469`; `appendix-c-formalisation.md:771-777` | — | None |
| **1b** Vessel classes and context | `appendix-c-formalisation.md:21-31,560`; `scripts/historical_replay.py:57-61` | Real vessel/trip records; length↔tonnage basis | P1-4 (dossier schema) |
| **1c** Environmental inputs | `appendix-c-formalisation.md:8-17`; `data/raw_weather_sea.csv:4`; `data/raw_marine_era5_sea.csv:4` | Tide in E; `m` archive | §4.1 note; P2-5 |
| **1d** Forecast horizons | — | **NOT FOUND** (0 `forecast` hits in any `.py`) | P0-2, P1-2 |
| **1e** SAFE/CAUTION/UNSAFE rules | `appendix-c-formalisation.md:483-512,546-564,633-645`; `scripts/historical_replay.py:41-105`; `scripts/condition_comparison.py:160-166`; `scripts/canonical_gt.py:97-106` | — | P2-4 (stale docstrings) |
| **1f** Permitted recommendation categories | `appendix-c-formalisation.md:781-789`; `governance/rule_set_provider.py:35-48`; `scripts/condition_comparison.py:81-113` | — | P1-1 (make configurable) |
| **1g** Human decision authority | `manuscript.md:114,243,291,849,1008`; `governance/advisory.py:20-24`; `governance/canonical_rules.py:27-28` | — | None |
| **2a** Historical environmental datasets | `data/raw_*.csv`; `data/c8/aai-2026-reproducibility-manifest.json` | Manifest covers 3 of 7 files | P2-5 |
| **2b** Issue-time forecast records | `scripts/README.md:3-39` (specification only) | **NOT FOUND** — script and output never existed | P0-2 |
| **2c** Independent observed hazard evidence | — | **NOT FOUND** (`decision-record-empirical-first.md:81`) | P0-3 |
| **2d** Missing / delayed / noisy inputs | `governance/reasoning_engine.py:56,96-116`; `appendix-c-formalisation.md:232-242` | No experiment; `ageᵢ` unspecified; pipeline drops rows | P1-2 |
| **2e** Vessel-linked records | `appendix-c-formalisation.md:21-31` (parameter only) | **NOT FOUND** | P1-4 |
| **2f** Data dictionary / provenance | `docs/canonical/data-provenance.md`; `data/c8/…manifest.json` | Retrieval timestamp null; CMEMS lineage `verified: false` | P2-5, P2-6 |
| **3a** Emittable recommendation categories | `governance/rule.py:12-14`; `governance/reasoning_engine.py:301-309` | Only `Delay` reachable | P0-5 |
| **3b** SAFE vs CAUTION output difference | `fidelity-traces.csv` (244 × `["Delay"]`, 48 × `[]`); `evaluation-specification.md:150` | **Inverted** — SAFE emits nothing | P0-5 |
| **3c** Inappropriate-output capability | `tests/test_governance_engine.py:86-97` (test-only hook) | **NOT FOUND** in any production path | P0-5 |
| **3d** Replay across configurations | `scripts/condition_comparison.py:81-113`; `governance/reasoning_episode.py:152-173` | Engine hardwired to C2; no bridge | P1-1 |
| **3e** Logging and reproducibility | `.../fidelity-traces.csv`; `.../integrity.json`; `journal1_e5_benchmark.py:279-314` | **No payload / explanation column** | P0-6 |
| **4a** Safety rules and provenance | `finding-met-hydrodynamic-gap.md`; `finding-met-lower-boundary-gap.md`; `finding-gt-provenance-audit.md`; `governance/canonical_rules.py:96-209` | Provenance ≠ validation (`manuscript.md:1468`) | — |
| **4b** Independent safety evidence | — | **NOT FOUND** — no experts, raters, rubric, labels, ethics | P0-1, P0-3, P0-4 |
| **4c** Circularity identification | `evaluation-baseline-decision.md:24-31`; `dataset-label-derivation.md:215`; `evaluation-specification.md:282`; `utility-construct-assessment.md:88-136` | — | §7 conditions 1–4 |
| **4d** Reference independent of the gate | `docs/justification/socio-technical-evaluation.md:132` (one table cell) | **NOT FOUND** as an artefact | P1-4 |
| **5a** Scenario construction | `.../state-space-manifest.json` (292 episodes); `evaluation-design-rq4.md:112-179` (20, superseded) | Expected-S column circular; all `v = big` | §8; P2-8 |
| **5b** Independent expert ratings | — | **NOT FOUND** | P0-1, P0-4 |
| **5c** Blinded evaluation procedure | `graduated-advisory-safety-novelty-assessment.md:120` (proposal) | **NOT FOUND** as a protocol | P0-7 |
| **5d** Inter-rater agreement | `docs/canonical/review-protocol.md:142` (single coder, none available) | **NOT FOUND** | P0-4, P0-7 |
| **5e** Severity labels | `graduated-advisory-safety-novelty-assessment.md:126` (proposal) | **NOT FOUND** | P0-4 |
| **5f** Actionability assessment | — | **NOT FOUND** | P0-4, P1-5 |
| **5g** Missing-advice / fallback assessment | — | **NOT FOUND** | P1-4 |
| **6a** Unrestricted AI arm | `scripts/condition_comparison.py:81-113` | Set level only; no candidates | P0-5, P1-1 |
| **6b** Participation-only arm | same | same | P0-5, P1-1 |
| **6c** Graduated arm | `governance/rule_set_provider.py:35-48` | Hardwired; Delay-only | P0-5, P1-1 |
| **6d** Calibrated binary abstention | `graduated-advisory-safety-novelty-assessment.md:117` (proposal) | **NOT FOUND** — no confidence score anywhere | P1-3 |
| **6e** Consistent inputs and candidates | `scripts/condition_comparison.py:129-150` (shared loader) | Candidates not shared across arms | P1-1 |
| **6f** Sufficient CAUTION cases | §9.2 (531 h / 201 d / ~85–123 events) | Precision bounded by events, not hours | P0-7, P1-6 |
| **6g** Candidate diversity | `fidelity-traces.csv` | One type | P0-5 |
| **6h** Independent safety labels | — | **NOT FOUND** | P0-3, P0-4 |
| **6i** Observations of actual conditions | `data/raw_*.csv` (reanalysis) | No issue-time, no outcomes, no vessels | P0-2, P0-3 |
| **6j** Independent episodes | §9.2 | Hours are not independent | P1-6, P1-8 |
| **6k** Actionable-advice retention | `metric-audit.csv:4`; `evaluation-specification.md:190,310,321` | Construct OPEN; formula prohibited | P1-5 |
| **6l** Provenance / reproducibility | `data/c8/…manifest.json`; `.../integrity.json` | External reproducibility not established | P2-5, P2-6 |

---

## Audit Limitations

1. This audit inspected the working tree at `main` @ `2b08a79` on 16 November 2026. It did not inspect git history except where noted (the `kawasan_perairan_collector.py` check).
2. Line numbers were obtained by direct file inspection; eighteen of the most load-bearing citations were independently re-verified line by line. The remainder are reported as read.
3. The `papers/` and `notes/` corpora (128 PDFs, 125 markdown notes) were searched by keyword for safety-reference and expert-validation artefacts but were not read exhaustively. A relevant item could have been missed; this is recorded as a limitation rather than a conclusion of absence for that corpus specifically. The conclusion of absence for *project-collected* expert evidence rests on the repository's own explicit statements, not only on search.
4. The event-clustering figures in §9.2 are this audit's own computation. The method reproduces the published headline figures exactly, but the clustering results themselves are new and unreviewed.
5. Claims about what the repository "does not contain" are claims about this repository. Materials held elsewhere — on the author's machine, with a supervisor, or at the institution — are outside the audit's reach.
