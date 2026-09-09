# Canonical Repository Drift Synchronisation Report

**Date:** 2026-09-09 · **Branch:** `chore/canonical-repository-drift-sync`
**Type:** documentation and reporting-prose synchronisation — **no new science**
**Appendix C:** `abee8715e842e0d9` unchanged · **Conference manuscript:** `27b33b846ae327cb` unchanged

---

## 1. Scope

Bring stale *supporting* documentation and reporting prose into line with the already-established canonical specification. No architecture semantics, thresholds, empirical results, predictions or evidence were created or changed.

## 2. Trigger

Three drift items were explicitly deferred by the preceding closures (DRIFT-1 `CLAUDE.md` `g_o` shares; DRIFT-2 `canonical_figures.py` wind trailer; DRIFT-3 scalar `g_r` in three supporting documents).

## 3. Protected before-state

25 artefacts hashed. Appendix C and the manuscript both matched their expected hashes at the outset, confirming the canonical authorities were the ones the closures left behind.

## 4. Canonical authorities

Appendix C for formal definitions; the canonical scripts for executable semantics and operator inclusivity; `canonical_figures.py` output for empirical figures; the prediction register for prediction state. No authority conflict was found — **CRD-2 not triggered**.

**One divergence is worth recording.** The task brief's `g_r` pseudocode used `rate >= 10.0` for CAUTION. The implementation uses strict `>` at both boundaries (10.0 → SAFE, 20.0 → CAUTION), which matches Appendix C exactly. Per the instruction that the implementation is the oracle for operator inclusivity, the strict form was used and the brief's form was not followed.

## 5. Audit method

Literal search first, then **assertion** search — the lesson carried forward from the Appendix C closure, where two consecutive sweeps declared closure because each hunted the form the previous defect had taken rather than the claim being made.

That lesson recurred here in a new guise. The residue scan produced false positives three times before it was correct: line-level matching flagged block-marked provenance; a backward-only section scan missed markers placed *beneath* the content they govern; and a naive fixed-clock pattern matched `06:00` inside data **timestamps** and inside a `DepartureTime` example string. The final detector is block-aware and bidirectional within a section, and excludes timestamps. **The scanner was fixed rather than the prose** — editing text to satisfy a regex would be making the repository look consistent, which is the opposite of the objective.

## 6. Known drift verification

**DRIFT-1 — confirmed.** `CLAUDE.md` carried `98.66% / 97.41%`.

**DRIFT-2 — confirmed as Class B, prose only.** `W_CAUTION = 21.6` is the executable constant (line 69), used in the classification at line 126; `22` appeared **solely inside a print string** (line 224). **CRD-1 not triggered.** The trailer also carried an inverted claim — *"a property of the site, not an artefact"* — when F-17 established the opposite: the zero-activation reading **was** the artefact, of the 22 kn rounding. Both the number and the assertion were repaired. Numerical outputs re-run and identical.

**DRIFT-3 — confirmed, and worse than described.** `formal-model.md` and the explainer did not merely carry a scalar `g_r`; both still used the **ordinal categorical** `r ∈ {none, light, moderate, heavy, storm}`, retired on 2026-09-08 *before* κ was typed. They were two amendments behind.

## 7. Additional drift discovered

23 findings in total (`repository-drift-audit.csv`), 17 repaired. Beyond the three known items:

- **The explainer's `g_t` block presented the fixed clock as the live definition** with the canonical form spliced between the superseded lines, so a reader could not tell which was current. Active fixed-clock semantics *and* active time-derived CAUTION — both closure-criteria blockers.
- **`architecture-illustration.md` carried the retired unsupported physical-safety claim.** Its user-facing display string read *"Darkness: insufficient visibility for safe small-vessel operation … Advisory will activate after 06:00."* The first clause is the exact wording Appendix C C.1 retired on 2026-09-08 — the evidence establishes *elevated* night risk, not that night operation is unsafe, and fishers demonstrably operate at night. The second is the superseded fixed clock. Replaced with the canonical policy wording and "at sunrise".
- **`data-provenance.md` stated a falsehood, not merely a stale figure:** *"the threshold is 22.0 kn … `g_w` never fires either way."* At the canonical 21.6 kn it activates twice. The same document also compared waves against the superseded **1.9 m** threshold and gave `g_r` at 3.7% of non-SAFE hours.
- **`empirical-findings-2026-09-06.md` §3.4 actively directed the papers** to report 98.66 / 97.41 and 87.63 / 91.10. The section is maintained post-migration — its adjacent `g_w` bullet was already corrected — so this was an oversight, not protected history. **§0a is generated and was not touched.**
- **F-6's table had no supersession banner at all**, presenting 5,416 / 5,189 / 227 / 70 / 6.2% and a `06:00 / 17:00 / 19:00` "scheduled events" label as current. Annotated.
- **`empirical-findings` still called P16 "the single refutation"**; P16 is CONFIRMED under F-17 and the register's refutation is now P01. Annotated.

## 8. `CLAUDE.md` repair

`98.66% / 97.41%` → **`98.71% / 97.66%`**, with the semantic boundary made explicit: these are `g_o`'s share **as the deciding component** of daylight CAUTION classifications, PRIMARY / RESOLUTION — *not* a Go-recommendation share, an AI recommendation frequency, an overall CAUTION rate, or the Level 2 binding rate. The `f(E)` form and the `r` type row were also synchronised.

## 9. Wind reporting repair

Trailer prose only; executable threshold untouched; outputs identical.

## 10. `g_r` documentation synchronisation

Signature `ℝ≥0 × K → {SAFE, CAUTION, UNSAFE}` with the storm route first, then the rate bands under `κ = 0`, using the implementation's strict `>` operators. Applied across `formal-model.md` (3 loci), the explainer (6 loci) and `CLAUDE.md` (2 loci). Thresholds 10.0 / 20.0 unchanged.

## 11. Raw code vs κ consistency

Every repaired document now distinguishes the **raw provider code `c`** from the **derived indicator `κ = χ(c)`**, χ(c) = 1 iff c ∈ {95, 96, 99}. `data-provenance.md` gained a dedicated *Derived κ* row stating plainly that **κ is not measured** — no provider reports it and no instrument observes it. Its evidence boundary is stated in the terms required: zero activating codes establishes only that *the activating provider codes did not occur in the replay*, and is **not** evidence that no thunderstorms occurred, that thunderstorms do not occur in Sabah, or that the route is unnecessary.

## 12. Required-rate vs supplementary-indicator consistency

Uniformly stated: the **rate is required** — ⊥ → UNSAFE as a **fault**; **κ is derived and never ⊥** — an absent or unrecognised code gives κ = 0 and the rate-only classification stands. The default is described as **non-escalating / fail-open for the storm disjunct**, and nowhere as fail-safe. No rainfall-rate fail-safe semantics were weakened.

## 13. Model B residue check

Zero active fixed-clock `g_t` definitions and zero active time-derived CAUTION across all repaired documents. `D = {m}` untouched; κ was not added to `D`; the marine-warning archive gap and the unexercised storm route are kept distinct.

## 14. Historical provenance retained

`evaluation-design-rq4.md` carries a top-level SUPERSEDED banner and was **not edited**. The SDR readiness audit, the C4/C6/C8 closure reports, `finding-met-lower-boundary-gap`, `finding-unsafe-semantics-audit`, the session logs, the v1 and v2.5 submitted manuscripts and the supervisor-feedback response all retain their historical figures. Where a record was stale but load-bearing for a decision taken on it — `decision-record-empirical-first.md`, F-6, the P16 narrative — it was **annotated, not overwritten**, per the project's own recomputation rule.

## 15. Files changed

Eight, each mapping to a verified `ACTIVE-CANONICAL-DRIFT` finding (`canonical-change-map.csv`): `CLAUDE.md`, `scripts/canonical_figures.py`, `docs/justification/formal-model.md`, `docs/reference/explainer-per-component-classification-functions.md`, `docs/canonical/data-provenance.md`, `docs/canonical/architecture-illustration.md`, `docs/canonical/empirical-findings-2026-09-06.md`, `docs/canonical/decision-record-empirical-first.md`.

## 16. Files intentionally unchanged

Appendix C, the conference manuscript, all canonical classifier implementations, the prediction register, the frozen solar artefacts, the raw datasets, the C5–C8 evidence, all historical audit reports and submitted manuscripts, `evaluation-design-rq4.md`, and Journal 1.

## 17. Empirical invariance

Level 2 **5.81% / 4.48%**; `g_o` daylight CAUTION **98.71% / 97.66%**; `g_t` all-hours non-SAFE **86.82% / 90.19%**; `g_r` daylight CAUTION **1.48% / 2.70%** and all-hours non-SAFE **0.20% / 0.26%**; daylight UNSAFE **1,262 / 455**; C0–C1 **42.88%**, C0–C2 **48.69%**, Level 2 isolated **5.81%**. **CRD-3 not triggered.**

## 18. Prediction-register invariance

**24 · 15 CONFIRMED / 9 REFUTED**, P09 **3,661**, P20 **1,529**. The P09 chain 5,416 → 5,220 → 5,201 → 3,661 is preserved and nowhere described as a pure `g_t` effect; the P20 registered 06:00–17:00 scope is kept distinct from the 455 astronomical-daylight RESOLUTION count; SDR-001 attribution remains P20/P23/P24 only. **CRD-4 not triggered.**

## 19. Protected after-state

25 artefacts re-hashed. The only protected-list file changed is `scripts/canonical_figures.py`, the intended prose-only repair. **Unexpected changes: none.** Appendix C `abee8715e842e0d9`; manuscript `27b33b846ae327cb`; register, solar artefact and Journal 1 byte-identical. `__pycache__` swept.

## 20. Parser verification

Both CSVs pass under `csv.DictReader` **and** `pandas.read_csv` with a strict field-count check: `repository-drift-audit.csv` (9 fields, 23 rows), `canonical-change-map.csv` (4 fields, 8 rows).

## 21. Deferred Journal 1 drift

**CRD-7 — recorded, not fixed.** `journal-1/submissions/v1-initial-submission/manuscript.md` and `journal-1/section-5-plan.md` carry scalar and categorical `g_r`, the 22 kn `g_w` boundary, and fixed-clock `g_t`. No canonical-authority conflict arises from them; they await their own task.

## 22. Stop-condition assessment

| | Condition | Triggered |
|---|---|---|
| CRD-1 | Executable semantic drift | **NO** — DRIFT-2 verified prose-only before editing |
| CRD-2 | Canonical authority conflict | **NO** |
| CRD-3 | Empirical drift | **NO** |
| CRD-4 | Prediction drift | **NO** |
| CRD-5 | Manuscript change required | **NO** |
| CRD-6 | Appendix C change required | **NO** |
| CRD-7 | Journal 1 contamination | **Recorded, deferred** |
| CRD-8 | Unsupported scientific claim required | **NO** — no new threshold, citation or rationale was needed |

## 23. Final decision

All closure criteria pass. Every active assertion in the repaired documents is now traceable to the established canonical state; historical statements remain historical and clearly marked; and no scientific state moved.

The most consequential find was not a stale number. `architecture-illustration.md` was still telling the operator that darkness means *"insufficient visibility for safe small-vessel operation"* — a physical-safety claim the specification had retired, in the one document that shows what the user actually sees. Numbers drift quietly; claims like that drift dangerously.

---

*Artefacts:* `data/canonical-repository-drift-sync/` — `integrity-before.json`, `integrity-after.json`, `repository-drift-audit.csv`, `canonical-change-map.csv`, `consistency-verification.json`, `parser-test.json`, `closure.json`, `build.py`.

---

## Independent Wind-Assertion Closure Repair

*Appended 2026-09-09. The closure above is left as written — the residue it missed is recorded here rather than edited out of it.*

### 1. Independent-review trigger

`data-provenance.md` states the wind state correctly in its `w` provenance row, but its **checklist** still carried an active instruction: *"Does it depend on `w`? → resolved (F-13). `g_w` never fires at either cell."* False under the canonical 21.6 kn boundary.

### 2. Why the previous audit missed it

The residue sat ~140 lines from the row that was repaired, in a different section, and was phrased as an **instruction** rather than a figure. But the real cause is narrower and less forgivable: the audit searched for stale **numbers** (`98.66`, `97.41`, `22 kn`) and stale **type signatures** (`g_r(r)`), and never searched for the stale **claim** `never fires` — even though `CLAUDE.md` states in bold, twice, *"Do not write 'never fires'"*. **The prohibition existed and was not turned into a search pattern.**

The previous report closed by observing that stale canon must be hunted as assertions rather than literals. It then hunted literals.

### 3. Canonical authority verification

Verified independently across four authorities, and then recomputed from raw data rather than trusting any of them:

| Authority | W_CAUTION / W_UNSAFE |
|---|---|
| `scripts/canonical_figures.py:69` (executable) | 21.6 / 27.0 |
| `appendix-c-formalisation.md` C.2 | 21.6 / 27.0 |
| `CLAUDE.md` § g_w | 21.6 / 27.0 |
| `empirical-findings` F-1 / F-17 | 21.6 / 27.0 |

Recomputed from `raw_weather_sea.csv` + `raw_marine_era5_sea.csv`, applying max-severity across all five components: **43,848 hours · max sustained wind 21.8 kn · activations 2 · bindings 0 · binding share 0.00%.** The two activations are **2021-01-17 06:00** (21.8 kn, governed by `g_o`) and **2024-04-30 23:00** (21.7 kn, governed by `g_t`) — matching the canonical narrative that a more severe component governed on both occasions. **WIND-R1 not triggered.**

### 4–5. Known residue and exact repair

The checklist item now reads: at the canonical **21.6 kn** boundary `g_w` **activates twice** and **binds in neither**; both counts must be quoted; *"never fires"* is prohibited; and a 0.00% binding share does **not** mean zero activations, with *activation* and *binding* defined inline.

### 6–8. Repository-wide assertion-equivalent search

Searched for the claim, not the words: `never fires`, `never activates`, zero/0 activations, `activations = 0`, `wind is irrelevant`, `wind does not matter`, and combinations with 21.6 / 21.7 / 21.8 / 22 / `W_CAUTION` / activation / binding.

**17 candidates.** ACTIVE-CANONICAL-DRIFT **2** · ACTIVE-CORRECT **6** · HISTORICAL-SUPERSEDED **5** · IRRELEVANT **3** · unrelated finding **1**. Full table: `wind-assertion-residue-audit.csv`.

Three candidates were rejected on subject rather than wording: `finding-met-hydrodynamic-gap.md`'s *"MET criteria never fire at this site"* concerns MET **wave** criteria at 3.50 m with a genuine zero; `unified-governance.md`'s *"CAUTION never activates"* concerns the governance mode; and the consistency-audit report's *"does not activate SC-1"* is a stop condition.

### 9. Additional active residue found

**W-02, not in the brief.** `scripts/openmeteo_raw_download.py` carried a pre-download planning comment stating *"sustained wind … never exceeds 17.8 kn against a **22 kn** CAUTION threshold"* and *"finding F-1 (**g_w never fires**) is a collection artefact"* — unmarked, in a maintained canonical collection script. The conditional it posed was subsequently answered in the affirmative, twice over: by the sea-cell re-collection (F-13) and by the threshold correction (F-17). Annotated with a RESOLVED block giving the canonical state. **Comment-only; no executable line changed.**

### 10. Activation-vs-binding verification

No maintained document equates a 0.00% binding share with zero activations. The distinction — *activation* = `g_w` reaches a non-SAFE component state; *binding* = `g_w` is the deciding component under max-severity — is now stated explicitly in `data-provenance.md`, and was already explicit in `CLAUDE.md`, F-17 and the `canonical_figures.py` trailer.

### 11–12. Empirical and prediction invariance

Level 2 **5.81% / 4.48%** · `g_o` daylight CAUTION **98.71% / 97.66%** · `g_t` all-hours non-SAFE **86.82% / 90.19%** · `g_r` **1.48% / 2.70%** and **0.20% / 0.26%** · daylight UNSAFE **1,262 / 455** · transitions **3,661 / 3,439 / 222 / 26 / 10.36%**. Register **24 · 15 CONFIRMED / 9 REFUTED**, **P16 CONFIRMED**, **P01 REFUTED**, P09 **3,661**, P20 **1,529**. P09 provenance and SDR attribution (P20/P23/P24 only) untouched. **WIND-R3 and WIND-R4 not triggered.**

### 13–15. Protected state and changed files

Appendix C **`abee8715e842e0d9`** unchanged; conference manuscript **`27b33b846ae327cb`** unchanged; both verified as matching *before* work began. `scripts/canonical_figures.py` **byte-identical** — no executable change was required, so **WIND-R2 not triggered**. Prediction register, frozen solar artefact and both Journal 1 files unchanged.

**Changed by this repair: two files** — `docs/canonical/data-provenance.md` (W-01) and `scripts/openmeteo_raw_download.py` (W-02), each mapped to a recorded finding. **Unexpected changes: none.** CSVs parser-tested with `csv.DictReader` and `pandas.read_csv`: PASS.

### Unrelated finding, recorded not fixed (WIND-R6)

`empirical-findings-2026-09-06.md` line 4 still reads *"All 24 pre-registered predictions resolved — **22 confirmed, 2 refuted**"*. The canonical register is **15 / 9**. This is prediction-state drift, not a wind assertion; it did not obstruct determining the wind state, so this task was not expanded. Recommended for a bounded follow-up.

### 16. Final closure decision

All criteria pass. The three canonical wind facts — **21.6 kn boundary, 2 activations, 0 bindings** — are now distinguishable everywhere they appear, historical provenance is retained and marked, and no scientific state moved.

**Method note.** The residue scan itself needed two corrections before it could be trusted, and in both cases the detector was fixed rather than the prose. The second is worth recording: the block-aware classifier treated `^\s*#` as a section header, which is correct in Markdown and wrong in Python — every comment line looked like a section break, so the scan stopped before reaching the annotation directly beneath the flagged line, reporting a false positive on text that had just been repaired. **A verification tool that is wrong about file type will manufacture exactly the residue it is meant to detect.**

---

## Independent Prediction-State Closure Repair

*Appended 2026-09-09. Earlier sections are left as written, including the wind-repair section's own note that it deferred this item.*

### 1. Trigger

The wind-assertion repair recorded, under WIND-R6, an unrelated active residue: `empirical-findings-2026-09-06.md` still summarised the register as **"22 confirmed, 2 refuted"** against a canonical **15 / 9**.

### 2. Canonical register verification

Read directly from `data/prediction-register.csv`, the authority — not from any prose document:

**24 entries · 15 CONFIRMED · 9 REFUTED.** Refuted: **P01, P04, P09, P18, P19, P20, P22, P23, P24**. **P01 REFUTED**, **P16 CONFIRMED**, P09 actual **3,661**, P20 actual **1,529**. Matches expected on every field — **PS-R1 not triggered**.

### 3–4. Stale assertion and repair

The document's **Status line** — the first thing a reader takes as the state — carried the stale count. Replaced with `15 CONFIRMED / 9 REFUTED`, the nine refuted IDs named, SDR-001 attribution held to **P20/P23/P24 only**, and the register named explicitly as the authority.

### 5–6. Assertion-equivalent audit

**14 occurrences classified** (`prediction-state-residue-audit.csv`): ACTIVE-CANONICAL-DRIFT **5** · ACTIVE-CORRECT **3** · HISTORICAL-SUPERSEDED **4** · deferred **1** · irrelevant **1**.

The large majority of `22 CONFIRMED / 2 REFUTED` hits are **integrity anchors inside dated C-series closure, approval and cleanup reports** — "Prediction register ✅ UNCHANGED, 24 entries, 22/2". Those are *correct records of the moment each task ran*, before C-6 and C-8 re-resolved the register, and they are historical audit reports, excluded from editing. They were retained. `scripts/c6/annotate_register.py` is self-scoping — "the correct canonical count **until C-8 completes**" — and needed nothing. Three hits matched only on the numeral `22` and were wind threshold sets (25/22, 13/22, 22/27), not prediction counts.

Four further active residues were repaired beyond the known one: the same document's Part 4 paragraph; `decision-record-empirical-first.md`, which was doubly wrong (stale count *and* naming P16 as the refutation); and `session-log-2026-09-06.md`, annotated rather than rewritten as a dated narrative.

### The residue I created

**PS-03 is mine.** The banner I added to this document *in the preceding closure repair* read: *"The register's refutation is now **P01**."* Singular. The canonical register has **nine** refutations. I wrote it while reasoning inside the 22/2 frame — correcting P16's status without checking the frame the correction sat in — and in doing so turned a correction annotation into a new stale authority in under a day. It is exactly the failure this task's guiding principle names: *do not allow a stale summary to become a second authority.* Now rewritten to state that no single refutation exists, with all nine named.

### 7–9. P01/P16, P09/P20 and SDR attribution

P01 **REFUTED** and P16 **CONFIRMED** verified against the register. P09 remains **3,661** with the chain **5,416 → 5,220 → 5,201 → 3,661** intact and nowhere described as a pure `g_t` effect. P20 remains **1,529** under its registered 06:00–17:00 scope, kept distinct from the **455** astronomical-daylight RESOLUTION count. SDR-001 attribution remains **P20/P23/P24 only**, and the repaired Status line now states that limit explicitly rather than leaving it inferable.

### 10–11. Empirical and wind-state invariance

Level 2 **5.81% / 4.48%** · `g_o` **98.71% / 97.66%** · `g_t` **86.82% / 90.19%** · `g_r` **1.48% / 2.70%** and **0.20% / 0.26%** · daylight UNSAFE **1,262 / 455** · transitions **3,661 / 3,439 / 222 / 26 / 10.36%**. Wind state from the just-closed repair holds: **21.6 kn**, max 21.8 kn, **2 activations, 0 bindings**; no `"never fires"` assertion reintroduced. **PS-R3 not triggered.**

### 12–14. Protected state, files changed, unexpected changes

Appendix C **`abee8715e842e0d9`** and the conference manuscript **`27b33b846ae327cb`** unchanged, both verified before work began. **Prediction register unchanged** — the repair was prose synchronisation only, so **PS-R2 was not triggered** and no prediction was re-resolved. Frozen solar artefact, all canonical scripts, and both Journal 1 files unchanged.

**Changed: three files** — `empirical-findings-2026-09-06.md`, `decision-record-empirical-first.md`, `session-log-2026-09-06.md` (14 insertions, 4 deletions). **Unexpected changes: none.** CSVs parser-tested with `csv.DictReader` and `pandas.read_csv`: PASS.

### 15. Final closure decision

All criteria pass. The register is the state; every maintained supporting document now describes that state or is explicitly marked as a record of an earlier one.

**Standing lesson, now demonstrated against my own work.** Across this branch the same failure recurred at four removes: a stale figure, a stale claim, a stale detector, and finally a stale *correction*. The annotation is the dangerous case, because it arrives wearing the authority of a fix. A correction must be checked against the canonical source in the frame that exists *now* — not against the frame that produced the error it is correcting.

---

## Independent Data-Configuration Caveat Closure Repair

*Appended 2026-09-09. Earlier sections stand as written.*

### 1. Trigger

§0a states both reportable configurations use sea-cell weather, while §0 *Standing caveats* — headed **"Applies to every figure below"** — still carried **"Weather data comes from a LAND grid cell; marine data from a SEA cell."** The superseded v1 configuration, framed as a current global caveat.

### 2. Executable source matrix

Traced through data flow, not filenames, across `canonical_figures.py`, `condition_comparison.py`, `diagnostic_binding.py`, `hysteresis_analysis.py`, `historical_replay.py`, `c5/three_stage_hysteresis.py` and `c6/reresolve_predictions.py`.

| Quantity | PRIMARY | RESOLUTION | Cell | Surface | Status |
|---|---|---|---|---|---|
| Wind | `raw_weather_sea.csv` | same | 5.940246, **116.025** | sea | current |
| Precipitation rate | `raw_weather_sea.csv` | same | 5.940246, **116.025** | sea | current |
| Raw weather code `c` | `raw_weather_sea.csv` | same | 5.940246, **116.025** | sea | current |
| Wave height | `raw_marine_era5_sea.csv` | `raw_marine_mfwam.csv` | 6.0, 116.0 / 5.958336, 116.04167 | sea | current |
| Time | `time` column + frozen solar artefact | same | 5.98, 116.01 (solar spec) | — | current |
| Marine warning `m` | none — declared exclusion `D = {m}` | none | — | — | unmeasured |
| `raw_weather.csv`, `raw_rainfall.csv`, `raw_marine.csv` | — | — | land / land / sea | — | **superseded, `--v1-historical` only** |

All seven scripts agree — **DATA-R1 not triggered.**

### 3–6. Wind, rainfall, raw code, wave

**Wind, precipitation and the raw weather code are all columns of the same file**, `raw_weather_sea.csv`. The task's caution against collapsing "weather" into one source was the right instinct but does not bite here: they genuinely do follow one path, and the sea re-collection moved all three together.

**The rainfall question, answered numerically rather than by reading comments.** Canonical precipitation sums to **14,019.4 mm**, matching `raw_weather_sea.csv` exactly, against **14,970.2 mm** for the land-sited `raw_rainfall.csv` — 113 hours above 10 mm/hr versus 131. **A real provenance difference, not a nominal one**, and canonical takes the sea series. So the land-cell caveat is stale for rainfall too, and no variable-specific exception was needed.

Cell separations recomputed by haversine from the file headers: **v1 land weather → ERA5 marine 12.9 km** (the F-10 mismatch), **v2 sea weather → ERA5 7.2 km**, **v2 sea weather → MFWAM 2.7 km**. These reproduce `data-provenance.md`'s existing pairwise table exactly — a useful cross-check that the document's own numbers were sound even where its prose was not.

### 7–8. Stale caveat and repair

Classified **ACTIVE-CANONICAL-DRIFT**, and stale twice over. Beyond the configuration, its consequence column read *"Likely the principal cause of F-1"* — but F-17 established the **22 kn rounding** as the cause: at 21.6 kn, `g_w` activates twice on the sea-cell series. The land cell was a genuine flaw; it was not what produced F-1.

The row now states the verified matrix with both separations, followed by a note that separates current configuration from provenance history and records what the row previously said.

### 9. Assertion-equivalent audit

**15 occurrences classified** (`data-configuration-residue-audit.csv`): ACTIVE-CANONICAL-DRIFT **7** · ACTIVE-CORRECT **4** · HISTORICAL-SUPERSEDED **3** · deferred **1**.

Six further active residues beyond the known one: `canonical_figures.py`'s docstring claiming three scripts *"still read"* the land cell — a present-tense falsehood since the C-8 migration, inside the docstring of the script that **is** the figure authority; and five in `data-provenance.md` and `rainfall-intensity-mapping.md` where `raw_rainfall.csv` was still described as the rainfall source, "still in use", or an "outstanding inconsistency".

### 10. Historical statements retained

F-10 and F-13 retained in full, as instructed. Also retained: the §0b method note, every superseded-figure banner, `data-provenance.md`'s "the **v1** classifier combined wind over land with waves 12.9 km away", and the configuration caveats in the dated C-series and sensitivity artefacts. **No dataset was changed and no historical narrative rewritten.**

### 11–13. Empirical, prediction and protected state

Level 2 **5.81% / 4.48%** · `g_o` **98.71% / 97.66%** · `g_t` **86.82% / 90.19%** · `g_r` **1.48% / 2.70%** and **0.20% / 0.26%** · daylight UNSAFE **1,262 / 455** · transitions **3,661 / 222**. Register **24 · 15 / 9**, P09 **3,661**, P20 **1,529**. Wind state **21.6 kn, 2 activations, 0 bindings**. Appendix C **`abee8715e842e0d9`** and manuscript **`27b33b846ae327cb`** unchanged. **All six raw datasets byte-identical** — DATA-R3 and DATA-R4 not triggered. Journal 1 unchanged.

### 14–15. Files changed

Four: `empirical-findings-2026-09-06.md`, `data-provenance.md`, `scripts/canonical_figures.py` (docstring only) and `docs/justification/rainfall-intensity-mapping.md`. **Unexpected changes: none.** Five CSVs parser-tested with `csv.DictReader` and `pandas.read_csv`: PASS.

### 16. Final decision

All criteria pass. The land/sea flaw remains in the audit trail as F-10 and F-13; it no longer stands as a current global caveat.

**Third detector failure, same family.** The residue scanner again reported a false positive on text I had just annotated — this time because the flagged line sits in a **module docstring**, whose lines carry no `#` prefix, so prefix-based block traversal could not reach the annotation one line above. Across this branch the block-detector has now been wrong about Markdown-versus-Python headers, about markers placed below their content, and about docstrings. Each time the correct response was to fix the tool, not the text. **A verification tool encodes assumptions about file format, and every one of those assumptions is a place where it can certify a clean result that is not clean.**

---

## Independent Empirical-Assertion Closure Repair

*Appended 2026-09-09. Earlier sections stand as written.*

### 1. Trigger

Two assertion classes inside `empirical-findings-2026-09-06.md`: an **epistemic overclaim** in F-11, and **incomplete restatement** in F-13, where sentences *below* an existing correction banner still read as current conclusions.

### 2–3. F-11 epistemic defect and the evidence boundary

F-11 read: *"`weather_code` never takes values 95, 96 or 99 across all 43,848 records. **Zero thunderstorms in five years**, in equatorial Borneo."*

The first sentence is supported. The second is not, and the defect is instructive: **the very next line — "This is not climatology" — was making exactly the right point while the claim above it stated the opposite.** The author knew the boundary and the prose crossed it anyway.

Absence of an activating provider code is evidence **about the provider code**. It establishes that κ = 1 in zero hours and the storm route is empirically unexercised. It does not establish that no thunderstorms occurred, that thunderstorms are absent from Sabah, or that the route is unnecessary. No occurrence count is available from this dataset and none is asserted.

Verified: κ = 1 in **0** hours, **0** missing codes, **0** invalid codes, across 43,848 records — **and on both grid cells**, so the code absence is a provider limitation rather than a cell artefact.

### 4. F-11 quantitative verification

F-11 stated precipitation exceeds 20 mm/hr **14 times**. Measured:

| Series | > 20 mm/hr | > 10 mm/hr | max |
|---|---|---|---|
| `raw_weather_sea.csv` (canonical) | **21** | 113 | 45.8 |
| `raw_weather.csv` (v1 land) | **14** | 131 | 39.2 |
| `raw_rainfall.csv` (v1 land) | **14** | 131 | 39.2 |

**14 is exactly right for the land cell and exactly wrong for the canonical sea cell.** Reconciled rather than overwritten: the text now gives 21 and identifies 14 as the v1 figure. **EA-R2 not triggered.**

### 5–6. F-13 heading and post-banner residues

The heading read *"F-13 — Q1a RESOLVED: F-1 is real. **Wind genuinely never reaches the threshold**."* A heading governs how every sentence beneath it is read, so a mid-section banner could not neutralise it. Replaced with *"Q1a RESOLVED: sea-cell recollection materially raises measured wind"*; **ID F-13 preserved**.

F-13 already carried an F-17 banner — and **three conclusions after it still asserted the superseded claim as fact**: that wind *"does not reach MET Malaysia's Category 1 criterion … at either grid cell"*, that *"sustained wind essentially never reaches the threshold"*, and that *"because `g_w` never fires either way, the wind data never influenced any classification"*. This is precisely the case the brief anticipated: **a supersession banner above a long section does not govern the claims below it.**

Replaced with a restatement deferring to F-17, preserving what survives — the land/sea correction changed no downstream figure at the configuration then in force. Two further instances were found in §3.2 by the repository-wide sweep, in a section otherwise already maintained.

The **activation/binding distinction** is now explicit wherever the claim appears: it is correct that wind never *governed* a classification; it is not correct that it never *activated*.

The margin caveat was retained deliberately — it was the prescient paragraph, correctly identifying that the result hung on 0.2 kn. It simply anticipated the wrong side of the comparison moving: the margin was closed by correcting the threshold to 21.598 → 21.6, not by the data shifting.

### 7. F-17 authority relationship

**F-1** (historical, 22 kn: zero activations) → **F-13** (sea recollection: max 17.8 → 21.8 kn) → **F-17** (canonical: 22 kn was an undocumented rounding; at 21.6 kn, 2 activations, 0 bindings; P16 CONFIRMED, P01 REFUTED). F-17 is later and governs; F-13 no longer overrides it anywhere.

### 8–9. Audit and retained history

**17 occurrences classified** (`empirical-assertion-residue-audit.csv`): ACTIVE-CANONICAL-DRIFT **10** · ACTIVE-CORRECT **4** · HISTORICAL-SUPERSEDED **1** · irrelevant **1** · deferred **1**.

Retained: F-11's heading (*"undetectable in this dataset"* — a claim about detectability, correct); F-13's *"at the then-specified 22 kn boundary"* framing and its v1/v2 comparison table, now with the boundary named; the F-1 as-first-measured block; and `finding-met-hydrodynamic-gap.md`'s *"never restricts anything"*, which concerns MET **wave** criteria.

### 10–15. Invariance, protected state, files changed

Level 2 **5.81% / 4.48%** · `g_o` **98.71% / 97.66%** · `g_t` **86.82% / 90.19%** · `g_r` **1.48% / 2.70%** and **0.20% / 0.26%** · daylight UNSAFE **1,262 / 455** · transitions **3,661 / 3,439 / 222 / 26 / 10.36%**. Register **24 · 15 / 9**, P01 REFUTED, P16 CONFIRMED, P09 **3,661**, P20 **1,529**. Canonical data flow unchanged — `raw_weather_sea.csv` still supplies wind, precipitation and the raw code. Appendix C **`abee8715e842e0d9`** and manuscript **`27b33b846ae327cb`** unchanged; all raw datasets, the solar artefact, every script and Journal 1 byte-identical.

**Changed: one file** — `docs/canonical/empirical-findings-2026-09-06.md`. **Unexpected changes: none.** Six CSVs parser-tested with `csv.DictReader` and `pandas.read_csv`: PASS.

### 16. Final decision

All criteria pass. No stop condition triggered.

**The lesson this repair adds.** The earlier residues were stale *facts*. These two were stale *inferences* — a number that was correct for a superseded dataset, and a conclusion that outlived the threshold it was measured against. Both sat in documents that had already been visited and banner-marked, which is why they survived: **a supersession marker attaches to the sentence a reader is looking at, not to the section it sits in.** F-11 is the sharper case, because the text contained its own correction one line later and still asserted the overclaim — evidence that knowing the epistemic boundary does not by itself keep prose inside it.

---

## Independent Reportable-Figure Guidance Closure Repair

*Appended 2026-09-09. Earlier sections stand as written.*

### 1. Trigger

Stale or scope-ambiguous **publication guidance** inside `empirical-findings-2026-09-06.md`: F-14 still instructing that MFWAM be the primary figure and that the primary is 6.1%, and F-15 presenting pre-SDR-001 divergence rates without adequate scoping.

### 2. §0a authority verification

`scripts/canonical_figures.py` and `scripts/condition_comparison.py` re-run and compared line by line against §0a: Level 2 **5.81% / 4.48%**, daylight UNSAFE **1,262 / 455**, `g_o` **98.71% / 97.66%**, `g_t` **86.82% / 90.19%**, `g_r` **1.48% / 2.70%** and **0.20% / 0.26%**, C1↔C3 **0.00% / 0.00%**, C0↔C1 **42.88%**, C0↔C2 **48.69%**. **Exact agreement — no output conflict.**

### 3. F-14 stale primary guidance

Three defects, and the central one is not merely stale — **it assigns the opposite roles to the canonical contract.**

F-14 argued: *"MFWAM is the better-sited measurement … The defensible presentation is **both**: the MFWAM figure as primary, ERA5 alongside it for the full five years."* The dual-configuration idea survived into "option C" and is now canonical. The **assignment did not**: §0a makes **ERA5 the PRIMARY headline on record length (5.81%)** and **MFWAM the RESOLUTION sensitivity check (4.48%)** — precisely the inverse of what F-14 recommended. Retained as the reasoning of the day, with the canonical contract stated above it.

Its supersession note compounded the problem: *"The primary figure is now **6.1%** — see §0a"* — a note that pointed at §0a while contradicting it. The full evolution is now recorded: **12.4 → 8.3 → 6.1 → 5.81 / 4.48**.

The heading asserted a headline figure superseded twice over, so it governed every sentence beneath it; replaced, with the ID preserved.

A fourth defect surfaced on verification. F-14 stated that under MFWAM *"small-vessel UNSAFE via wave height never occurs (max 1.84 m against a 1.9 m threshold)"*. At the **canonical 1.25 m** boundary, MFWAM exceeds in **937 hours** and ERA5-Ocean in **2,516** — wave-driven UNSAFE is reachable under both. Another near-miss margin closed by moving the threshold to its sourced value rather than by the data changing, exactly as in F-13.

### 4. F-15 historical/current distinction

F-15's table (24.64 / 32.36 / 7.72 over 9,133 hours) and its level decomposition were measured under the **superseded fixed-clock `g_t`**; canonical is **42.88 / 48.69 / 5.81 / 4.48 over 9,135 hours**. Its own note, *"Updated 2026-09-08 for the MET rainfall amendment"*, made it read as current when it predates the same day's migration. Both now carry PRE-SDR-001 markers with the canonical values inline; the isolation *method* is noted as unchanged.

**C3 ≡ C1 = 0.00% is untouched and reinforced.** It is a structural property of the mapping from classification to admissible set, not of the data, so no threshold, wave model or `g_t` change can move it — which is exactly why it answers the novelty objection and why it alone among F-15's numbers needed no scoping.

### 5. F-16 intermediate-state check

F-16's *"Level 2 binding 7.84% → 7.72% (primary), 6.15% → 5.98% (resolution)"*, with daylight UNSAFE 1,170 and weather-driven share 11.8%, is the state immediately after the rainfall amendment and **before** SDR-001 later the same day. Marked as intermediate, with canonical values given. The finding's conclusion — the amendment moved only CAUTION and left UNSAFE untouched — holds unchanged.

### 6–7. Audit and history retained

**16 occurrences classified** (`reportable-figure-residue-audit.csv`): ACTIVE-CANONICAL-DRIFT **7** · ACTIVE-CORRECT **5** · HISTORICAL-SUPERSEDED **3** · deferred **1**. The sweep counted a stale number as drift only when paired with reporting language (*current, primary, headline, report, should, use, now*) — historical figures on their own are provenance, not instructions.

Retained: the whole **12.4 → 8.3 → 6.1** evolution; §0a's *"Predecessors — do not report these"* table, which was already the correct pattern; the §0a regeneration banner; §0b's method note; and the equivalent amendment notes in `finding-met-lower-boundary-gap.md` and Appendix C.

### 8. Current reporting contract

**PRIMARY 5.81%** — 5.00 yr, ERA5-Ocean ~50 km — the headline. **RESOLUTION 4.48%** — 3.25 yr, MFWAM ~8 km — the sensitivity check. The 1.3-point gap is the grid-resolution result, not uncertainty about which number is true.

### 9–13. Invariance, protected state, files changed

Level 2 **5.81% / 4.48%** · `g_o` **98.71% / 97.66%** · `g_t` **86.82% / 90.19%** · `g_r` **1.48% / 2.70%** and **0.20% / 0.26%** · daylight UNSAFE **1,262 / 455** · transitions **3,661 / 3,439 / 222 / 26 / 10.36%**. Register **24 · 15 / 9**, P09 **3,661**, P20 **1,529**. Wind **21.6 kn, 2 activations, 0 bindings**. Rainfall **21 / 113 / κ=0**. Appendix C **`abee8715e842e0d9`** and manuscript **`27b33b846ae327cb`** unchanged; datasets, solar artefact, all scripts and Journal 1 byte-identical.

**Changed: one file** — `docs/canonical/empirical-findings-2026-09-06.md`. **Unexpected changes: none.** Seven CSVs parser-tested with both readers: PASS.

### 14. Final decision

All criteria pass. No stop condition triggered.

**What this class adds to the branch.** Every previous residue was a stale *statement*. These were stale *instructions* — guidance about what the paper should report, written when a different contract was in force. A stale fact misinforms a reader who checks it; **a stale instruction propagates into the next document someone writes.** F-14's is the clearest case: it did not merely name an old number, it recommended the opposite PRIMARY/RESOLUTION assignment from the one now canonical, while pointing at §0a as its authority.
