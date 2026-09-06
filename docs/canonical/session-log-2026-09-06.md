# Session Log — 2026-09-06

**One working day.** Started with a rejected conference paper and a formal model that had never been run against data. Ended with the model corrected, the data audited, and fifteen empirical findings (F-1 to F-15) — one of which contradicts a claim in both papers.

---

## Part 1 — Formal model correction

**Trigger:** audit of `evaluation-design-rq4.md` found that `g_v(small) = CAUTION` unconditionally made SAFE unreachable for the entire deployment population.

**The defect, precisely stated:** a constant term inside a maximum is a **floor**, not a **threshold shift**. `g_v` therefore had *zero* effect on the CAUTION/UNSAFE boundary — a 5 m boat and a 20 m boat were classified UNSAFE at identical wave heights, contradicting Yaakob et al.

**Resolution:** `g_v` removed. Vessel category now conditions `g_o(o, v)`, shifting thresholds rather than flooring output.

```
f(E) = max_≻ { g_w(w), g_r(r), g_m(m), g_o(o,v), g_t(t) }     five terms, not six
```

| v (GRT) | SAFE | CAUTION | UNSAFE |
|---|---|---|---|
| small (< 10) | o < 1.0 m | 1.0–**1.25 m** | > **1.25 m** |
| medium (10–25) | o < 1.4 m | 1.4–2.8 m | > 2.8 m |
| big (> 25) | o < 1.5 m | 1.5–3.5 m | > 3.5 m |

*Small-vessel row shown as amended later the same day (Part 5): UNSAFE moved 1.9 m → 1.25 m, from Yaakob's NORDFORSK failure point to his operational ceiling. At the time of Part 1 this row read 1.0–1.9 m / > 1.9 m.*

**Theorem impact:** only Theorem 1 (Totality) required amendment. Theorems 2 and 3 verified unaffected — neither references `f`'s internals. **The CS contribution was never at risk.**

---

## Part 2 — Consistency audit

43 files checked across `docs/canonical/`, `docs/justification/`, `docs/implementation/`, `docs/reference/`, `CLAUDE.md`.

**Every canonical document contained errors predating this work.**

| Where | Found |
|---|---|
| `architecture-illustration.md` | **6 misclassifications** — `w=18 kn→CAUTION` (SAFE), `r=moderate→CAUTION` (SAFE), `r=heavy→UNSAFE` (CAUTION), a nonexistent "15 kn threshold", plus two wave readings valid only for small vessels |
| `traceability-table.md` | **`m` and `o` swapped**; and the consistency checklist **certified the swap as verified**, listing the definitions in the wrong order |
| `viva-formalisation-architecture.md` | **Three mutually inconsistent wind threshold sets** (25/22, 25/35, 13/22 kn — none matching canonical 22/27); thresholds misattributed to **MMEA** in 7 places; `v` called "vessel condition" with invented thresholds; malformed example vectors |
| `formal-model.md` | Same `m`/`o` swap; 2 of 3 worked examples mis-annotated |
| `safety-state-design.md` | Rainfall thresholds wrong (moderate → CAUTION) |
| `data-source-met-malaysia.md` | Same rainfall error, independently |
| 4 files | **Tide conflated with `o`** — tide is not in E at all |

**Method note:** two misses in my own first pass traced to grep-based triage — truncated output, and one file (`environmental-state-governance.md`) that discusses the model without using any of its symbols. *A document can be wrong about the model without containing the model's notation.* Any future sweep needs a content pass, not just token matching.

---

## Part 3 — First empirical execution

Five years of hourly data had been sitting in `data/` since May. This was the first time the classifier ran against it.

### Findings

| # | Finding |
|---|---|
| **F-1** | **`g_w` never fires.** Zero activations in 5 years. Sustained wind 0–17.8 kn against a 22 kn threshold |
| **F-2** | Superseded model's UNSAFE was effectively "it is dark" — 10 of 20,097 daylight hours |
| **F-3** | `g_v(small)` floor made SAFE **0.0%** reachable — the analytical prediction, measured |
| **F-4** | Vessel conditioning is operative: small vs big differ in **10.7%** of departure hours |
| **F-5** | **Level 2 governance binds 12.4% of departure hours** — the result the papers were missing |
| **F-6** | **Mode-chattering is NOT a demonstrated problem.** 70 events in 5 years (14/yr); hysteresis helps by 6.2% |
| **F-7** | Only **3 of 5** functions ever bind: `g_o` (97.5% of daylight CAUTION *as first measured; 97.40% / 95.05% after the Part 6 recomputation*), `g_t`, `g_r` |
| **F-8** | MET's criteria are **disjunctive** ("and/or") — independent institutional support for max-severity, currently uncited |

### Data provenance problems, found by checking

| # | Finding |
|---|---|
| **F-9** | **My error, corrected.** I claimed `wind_speed_10m` is an hourly mean. It is **instantaneous**; `10m` is height above ground |
| **F-10** | **Wind sampled over LAND, waves over SEA**, 12.9 km apart. `cell_selection` defaults to `land` and was never set |
| **F-11** | **Zero thunderstorm codes in 5 years** in equatorial Borneo. Open-Meteo cannot detect them — so `g_r`'s storm branch, anchored to Ribut Petir, is unobservable |
| **F-12** | Wave data is **ERA5-Ocean at ~50 km** — the coarsest of nine models — carrying 97.5% of CAUTION decisions |

### Re-collection and resolution

Data re-collected with `cell_selection=sea` and a finer wave model. **v1 files preserved** so the prediction register stays valid.

| # | Finding |
|---|---|
| **F-13** | **Q1a resolved.** Sea-cell wind +57.3% (max 17.8 → **21.8 kn**) — but `g_w` **still never fires**. Threshold 22.0, missed by **0.2 kn**. F-1 is a real property of the site. *The land/sea error was real and changed nothing* |
| **F-14** | **Q6 resolved.** MFWAM 8 km vs ERA5 50 km: r = 0.953, max 1.84 vs 2.60 m. **Headline drops 12.4% → 8.3%**, a 33% relative reduction |

### The MET–hydrodynamic gap → `finding-met-hydrodynamic-gap.md`

**Structural discovery:** MET states Category 1 covers waves *"up to 3.5 m."* That is where Cat 1 **ends**. **MET never states where it begins.** The official criteria therefore *structurally cannot* supply the SAFE/CAUTION boundary.

**Quantified gap:** MET Cat 1 sits **2.8×–7.0×** above the measured operability limits of actual Malaysian boats.

> **Yaakob's 5.03 m boat is outside its documented seakeeping envelope 54% of the time, while no official warning would ever be in force.**

Jeong & Im's Korean finding — 82% of capsizings with no warning issued — reproduced at the Malaysian site with the mechanism visible.

**Position agreed:** MET remains authoritative wherever MET speaks; hydrodynamic evidence fills only where MET is silent.

---

## Part 4 — Method: pre-registration

**24 predictions registered before their analyses ran** (P01–P18 during the diagnostic work, P19–P20 with the threshold amendment, P21–P24 with the four-condition comparison), in `data/prediction-register.csv` with machine-comparable bounds. Scripts populate `actual`/`status` automatically.

**23 confirmed, 1 refuted** (24 predictions).

The refutation (P16 — I predicted sea-cell wind would cross 22 kn) is the most useful result of the day: it converted F-1 from *suspected artefact* to *established property of the site*.

Two predictions were deliberately uncomfortable and both held: **P13** (mode-chattering is not a real problem — contradicting both papers) and **P14** (the classifier reduces to a wave gate plus night curfew).

*The value is not the pass rate. It is that F-6 and F-7 were written down as expectations before they could be reframed as intentions.*

---

## Files produced

**New canonical documents**

| File | Purpose |
|---|---|
| `decision-record-empirical-first.md` | The sequencing decision; open questions Q1–Q8 |
| `empirical-findings-2026-09-06.md` | F-1 to F-15 with consequences for both papers |
| `finding-met-hydrodynamic-gap.md` | **Source of truth** for threshold provenance |
| `data-provenance.md` | Where each variable comes from; **check before citing any figure** |
| `session-log-2026-09-06.md` | This document |

**New scripts** — all re-runnable

`canonical_figures.py` (**the figure authority**) · `condition_comparison.py` · `historical_replay.py`\* · `diagnostic_binding.py`\* · `hysteresis_analysis.py`\* · `collect_raw_v2.py` · `compare_v1_v2.py` · `threshold_comparison.py`

\* *still read the v1 land-cell files. Retained to reproduce historical findings; do not quote their figures as current.*

**New data** — v1 preserved

`raw_weather_sea.csv` · `raw_marine_era5_sea.csv` · `raw_marine_mfwam.csv` · `prediction-register.csv`

**Substantially revised**

`appendix-c-formalisation.md` (C.1, C.2, Theorem C.1, new C.9) · `CLAUDE.md` · `architecture-illustration.md` · `traceability-table.md` · `viva-formalisation-architecture.md` · `formal-model.md` · `safety-state-design.md` · `low-resource-environments.md` · `environmental-state-governance.md` · `dataset-label-derivation.md` · `data-source-met-malaysia.md` · `explainer-per-component-classification-functions.md` · Journal 1 §5.3/§6.2 · conference `manuscript-v3.md` (forked) · `revision-notes.md`

---

## NEXT SESSION

## Part 5 — Threshold amendment (decision taken)

**Small-vessel UNSAFE: 1.9 m → 1.25 m.** Adopted 2026-09-06.

Yaakob tested Boat A at the mean of successive sea-state bands: it **passes** SS3 (0.875 m) and **fails** SS4 (1.875 m). Two distinct quantities follow — the **operational ceiling** (1.25 m, top of the last passing band) and the **failure point** (1.875 m). The prior threshold used the failure point. For a departure gate the conservative reading is the ceiling: stop at the edge of the demonstrated-safe envelope, not at demonstrated failure.

| | Daylight UNSAFE | Weather-driven share of UNSAFE | Departure CAUTION |
|---|---|---|---|
| 1.90 m (prior) | 3 hrs (0.02%) | 0.1% | 8.3% |
| **1.25 m (adopted)** | **409 hrs (3.13%)** | **7.0%** | **6.1%** |

**The headline figure drops to 6.1%.** The amendment was adopted on the provenance argument, not the numbers — it produces a *smaller* result. What it buys is that `G(S) = 0` becomes reachable by sea state rather than only by darkness, removing the "UNSAFE is just a night curfew" criticism.

**Propagated:** `appendix-c` first, then 10 documents and 4 scripts. Registered as P19/P20.

**Still open:** the medium and big rows use failure-point-style reasoning scaled from MET. Neither has vessel-specific NORDFORSK data, so neither can be given the same treatment without new evidence.

---

### Decisions needed first — these gate everything else

**All three are now resolved. Nothing gates the writing work below.**

1. ~~**Threshold amendment**~~ — ✅ **RESOLVED, see Part 5.** 1.25 m adopted.

2. ~~**F-7 framing**~~ — ✅ **RESOLVED 2026-09-06.** Report the binding profile as a finding **and** retain all five functions with explicit scope statements (options 1 + 3). The classifier is **not** reduced — that would fit the specification to one site's weather and cost the transferability claim. `g_w` (measured, never reached — a site property, results section, with its 0.2 kn margin) and `g_m` (never measured — threats to validity, lower-bound consequence) are to be presented **separately**, not as one "components that don't fire" discussion. Reasoning in `empirical-findings-2026-09-06.md` §3; recorded against Q1 and Q4 in the decision record.

3. ~~**Which headline figure**~~ — ✅ **RESOLVED.** **6.1%**, superseding both 8.3% and 12.4%. The authoritative statement of what to report, and what each predecessor is conditioned on, is `empirical-findings-2026-09-06.md` **§0a**. The 12.4% → 8.3% → 6.1% sequence is presentable as a strength: a resolution correction followed by a provenance correction, both adopted on methodological grounds, both *lowering* the result.

### Work queued

4. ~~**Withdraw the mode-chattering claim**~~ — ✅ **DONE 2026-09-06.** Qualified rather than dropped: hysteresis is retained as a low-cost precaution, with the measured figures (5,416 transitions, 95.8% scheduled, 70 oscillations, 6.2% reduction) and the hourly-resolution bound stated alongside. Applied to `manuscript-v3.md` ×2, Journal 1 §9/§12 plans, and `safety-state-design.md` §2.5. **Not applied to archived submissions** — those are records of what was submitted.

5. **Cite F-8** — MET's "and/or" is free institutional support for max-severity, currently unused.

6. **Rewrite `evaluation-design-rq4.md`** around historical replay. The 20 scenarios become boundary and fail-safe cases inside a larger empirical frame. **Do this after decision 1 resolves, not before.**

7. **Build Layer 3** (Q8) — rule engine, `RS(SAFE)`, `RS(CAUTION)`. Needed for the C0/C1/C2 output comparison. Implementation work, not data collection. Note the headline result does not depend on it.

8. ~~**Add C3 — Flehmig-style baseline**~~ — ✅ **DONE 2026-09-06.** `scripts/condition_comparison.py`, four conditions over the MFWAM record. **C3 diverges from C1 in 0.00% of hours** — the closest structural precedent is output-equivalent to a plain binary gate, and its intermediate level is invisible in AI output. Level decomposition: participation gate 22.21%, Level 2 alone **6.15%**. P21–P24 registered before the run, all confirmed. Written up as F-15 and as Result 6 / TABLE VII in the conference paper.

9. **Finish Tier 4 propagation** — Journal 1 section plans, `supervisor-feedback-response.md`.

10. ~~**Re-collect rainfall from the sea cell**~~ — ✅ **DONE 2026-09-06 (Part 6).** `canonical_figures.py` and `condition_comparison.py` both take precipitation from `raw_weather_sea.csv`. `raw_rainfall.csv` is retained only for reproducing historical findings.

### Part 6 — Coverage check and dual-configuration reporting (late addition)

**Trigger:** the question *"can we confirm we have 5 years of data?"*

**Answer: no — not for the headline figure.** MFWAM starts October 2021, so 6.1% was a **3.25-year** result being reported as five years.

**The larger problem found by the same check.** F-4 (10.7%) and F-7 (97.5% / 3.4% / 88.2%) reproduce to 2 d.p. **only** under v1 land-cell data *and* the pre-amendment 1.9 m threshold. When the threshold was propagated, script constants were updated but the derived findings were never recomputed — and three of four scripts still read the land cell that F-10 had already condemned. §0a was listing figures from two incompatible configurations as though one analysis produced them.

**Resolution — "option C".** Every figure now reported in two configurations, both sea-cell, both at 1.25 m:

| | PRIMARY | RESOLUTION |
|---|---|---|
| | 5.00 yr · ERA5-Ocean ~50 km | 3.25 yr · MFWAM ~8 km |
| Level 2 binds | **7.84%** | **6.15%** |
| Daylight UNSAFE | 1,170 hrs (5.82%) | 409 hrs (3.13%) |
| Small vs big differ | 12.14% | 7.92% |
| C3 vs C1 divergence | **0.00%** | **0.00%** |

The 1.7-point spread is the grid-resolution sensitivity, reported rather than resolved. F-15 holds at exactly 0.00% in both — it is structural, not data-dependent.

**Single generator adopted:** `scripts/canonical_figures.py`. §0a is now regenerated, never hand-edited. A recomputation rule is recorded in `CLAUDE.md`.

**One near-miss worth recording.** Switching `condition_comparison.py` to the new primary config silently flipped P22–P24 to REFUTED, because they had been registered against MFWAM. Fixed by scoring each prediction against the configuration it was registered on. *A register whose verdicts change when a reporting decision changes is worthless.*

**Rainfall provenance resolved as a side effect** — the new scripts take precipitation from `raw_weather_sea.csv` rather than the land-sited `raw_rainfall.csv`.

---

### Standing limitations — state, do not attempt to fix

- **Q7 — no ground truth.** No incident data for Kota Kinabalu. The evaluation is a **characterisation, not a validation**: we can say the architecture *would have restricted advice on 6.1% of mornings*, not that those were the *right* mornings. **No further data collection from Open-Meteo can fix this.**
- **Q2 — `m` unmeasured.** No marine warning archive. All severity figures are **lower bounds**. Candidate: myMETdata, RM20/CSV, station WMKK.
- **Q1b — thunderstorms undetectable** in this data source.
- **ERA5 vs MET provenance.** Thresholds from one organisation, measurements from another. Permanent; belongs in Threats to Validity.

### Conference paper

**Empirical results are now written in (2026-09-06).** New *Empirical Characterisation* section after Domain Instantiation: five results plus TABLE VI (component binding shares). Headline 6.1%. Framing updated for a third contribution across abstract, introduction, conclusion and next steps; Generalisation carries the F-7 scope statement.

**Two live errors were found and fixed while writing it:**

1. **Fig. 4 contradicted TABLE IIIb.** Its header note still read `1.0 / 1.9 m`, and the mid-morning value `o = 1.4 m → CAUTION` would classify **UNSAFE** under the amended small-vessel row. Now 1.1 m. Missed by the earlier propagation because the value sits inside an ASCII-art block that pattern matching did not reach.
2. **Threats to Validity asserted an evaluation that never ran** — *"100% Safety Dominance compliance across all 20 test scenarios constitutes the fidelity check."* The reasoning engine is unimplemented (Q8), so `AI(E)` has never been observed. Three paragraphs (Internal, Construct, Conclusion validity) referenced those 20 scenarios; all rewritten to state what was actually done. **This was the most dangerous sentence in the paper** given Review 3 rejected on absent empirical evidence.

Still open: acknowledgment placeholder only. Review 2 was for a **different paper** — worth raising with the chairs, since discounting it leaves 1 accept-minor and 1 reject, which is borderline rather than a clear rejection.
