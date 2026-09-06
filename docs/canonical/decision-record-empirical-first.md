# Decision Record: Empirical-First Revision of the Domain Instantiation

**Date:** 2026-09-06
**Status:** Agreed — supersedes the prior "specify then validate" sequencing
**Scope:** Domain instantiation (RQ3, RQ4). **Does not affect** the CS contribution (RQ1, RQ2).
**Trigger:** First execution of `f(E)` against five years of hourly site data revealed that a component of the formal model is inert at the deployment location.

---

## 1. What prompted this

`data/` has held five years of hourly environmental data for Kota Kinabalu (2020-01-01 to 2024-12-31, 43,848 records) since May 2026. On 2026-09-06 the classifier was run against it for the first time.

**Finding: `g_w` never fires.** Sustained wind at the site ranges 0–17.8 kn over five years. The `g_w` thresholds are 22 kn (CAUTION) and 27 kn (UNSAFE). Zero activations in either band.

Before this run, `g_w` had: threshold values in Table 1, an empirical justification paragraph, a totality case in Theorem 6.1, a row in Algorithm 1, a complexity entry, and answers in the viva preparation document. None of that was wrong in itself. It was simply never checked against the environment it describes.

**Secondary findings from the same run:**

| Finding | Figure |
|---|---|
| Superseded vessel-blind `g_o` produced UNSAFE | **0 times in 5 years** (max wave 2.60 m; threshold was 3.5 m) |
| Superseded model UNSAFE in daylight hours | **10 of 20,097** (0.05%), all from rainfall — UNSAFE was effectively "it is dark" |
| Superseded `g_v(small)` floor: SAFE reachability | **0.0%** in every time window — the analytical prediction, now measured |
| Amended model, small vessel, daylight | SAFE 84.3% / CAUTION 15.6% / UNSAFE 0.15% |
| Small vs big classify differently (departure window) | **10.7%** of hours |
| Level 2 governance binds (small vessel, departure window) | **12.4%** of hours |

---

## 2. The decision

**Sequencing is reversed. The data now drives the specification, not the other way round.**

Concretely, for the domain instantiation:

1. **Do not repair `g_w` to preserve the existing model.** Choosing a wind definition in order to make a pre-specified component fire is fitting the evidence to the model. Run the diagnostic first — establish what actually discriminates safe from unsafe departure conditions at this site — and let that determine what the classifier should contain.

2. **A smaller classifier that discriminates is preferred to a larger one with decorative components.** If waves, rainfall and time of day carry the discrimination, that is the finding, and it should be reported as such rather than padded.

3. **Treat MET Malaysia criteria as institutional anchoring, not as the primary evidential basis.** Those thresholds exist to trigger public warnings; they are not calibrated to departure safety for a 6 m hull. The Yaakob / Jeong & Im line of evidence is closer to the actual question. The vessel-conditional `g_o` change moved in this direction; going further is on the table.

4. **State the model's blind spots explicitly** rather than relying on them going unexamined. Each has a clean justification and is stronger stated than omitted.

---

## 3. Why — the underlying reasoning

The formalisation ran substantially ahead of validation. The model was specified across roughly fifteen documents, proved with three theorems, written into two papers, and defended in a 768-line viva preparation document before a single hour of site data was classified.

Everything downstream inherited unvalidated assumptions. That is what produced an inert component surviving into proofs, papers and prepared viva answers.

A related signal reinforced the same conclusion. The consistency audit conducted the same day found that **every canonical document contained errors predating this work**: six misclassifications in the architecture illustration, `m` and `o` swapped in two documents, three mutually inconsistent wind threshold sets in the viva preparation document, and a consistency checklist that certified its own error. Individually minor; collectively they indicate documents being *extended* rather than *checked*. The checklist item that would have caught the illustration errors — "do the worked scenarios classify correctly?" — did not exist until it was added on 2026-09-06.

---

## 4. Scope boundary — what this does NOT change

**The CS contribution is unaffected.** The governance pair (G(S), A_AI(S)), the containment property, and the three theorems are independent of how `f(E)` computes a state:

- **Theorem 2 (Monotonicity)** operates on `A_AI(S)` set definitions; it does not reference `f` or any classification function.
- **Theorem 3 (Safety Dominance)** requires `f` to be *total*, not to have any particular internal structure. Its assumptions A1–A4 concern the rule engine and the `RS(S)` supply mechanism.
- **Theorem 1 (Totality)** is the only one touched by changes to the classifier, and only in its per-component case list.

Adding, removing or redefining a classification function requires re-verifying Theorem 1 and nothing else. This was confirmed during the 2026-09-06 formal model amendment and holds for any future revision.

RQ1 and RQ2 stand. The revision is confined to RQ3 and RQ4.

---

## 5. Open questions carried forward

| # | Question | Blocking | Notes |
|---|---|---|---|
| Q1 | **Should `g_w` read sustained wind, gusts, or be removed?** | **Blocked on Q1a** | MET criteria state "wind speeds from 40–50 kmph" without specifying sustained or gust — **the ambiguity is in the source**. Gusts reach 36.9 kn and would fire 205 CAUTION / 24 UNSAFE. *Revised 2026-09-06: an earlier version of this row claimed ERA5 `wind_speed_10m` is an hourly mean that under-represents peaks. That was wrong — the variable is instantaneous, and `10m` is height above ground. See findings F-9.* |
| ~~**Q1a**~~ | ✅ **RESOLVED 2026-09-06 — see F-13.** Re-collected with `cell_selection=sea`: mean wind +57.3%, max 17.8 → 21.8 kn, but `g_w` activations still **0** (threshold 22.0 kn, missed by 0.2). **F-1 is a real property of the site, not a collection artefact.** Prediction P16 refuted. | resolved | The download script does not set `cell_selection`, which defaults to `land`. Returned coordinates confirm wind and rainfall came from a land cell (5.940246, 116.100006) while waves came from a sea cell (6.0, 116.0), ~12 km apart. Land surface roughness suppresses 10 m wind substantially. **If a `cell_selection=sea` re-run gives materially higher wind, F-1 is a collection artefact and Q1 dissolves.** Attempted and blocked — sandbox network refused the host and the fetch timed out. **Must be run locally.** Until then, F-1 must not be reported as a property of the site. |
| **Q1b** | **How should `r = storm` be detected?** | Data | `weather_code` returns **zero** thunderstorm codes (95/96/99) across five years in equatorial Borneo. Open-Meteo states thunderstorm estimation "is not possible" and hail codes are Central-Europe-only. Since Ribut Petir is MET's stated trigger for rainfall UNSAFE, the anchoring mechanism is unobservable in this dataset. `g_r = UNSAFE` reaches only via precipitation > 20 mm/hr — 14 hours in five years. |
| Q2 | **Does MET publish a marine warning archive?** | Data availability | `m` has no historical data; the scraper collects forward only. `g_m` can only raise severity, so all replay figures are **lower bounds**. If an archive exists, `m` may be the authoritative wind signal and could resolve Q1 — MET issues warnings on its own observations using its own convention. **Candidate found 2026-09-06:** `docs/implementation/data-source-met-malaysia.md` §5.3 lists **myMETdata** (`mymetdata.met.gov.my`) — paid, **RM20 per CSV**, hourly surface wind and rainfall for station **WMKK (Kota Kinabalu)**. That is *MET's own observed station data*, at the site, for the disputed variables. It would settle Q1 and Q1a outright: if WMKK sustained wind also never reaches 22 kn, F-1 is real; if it does, the ERA5 land-cell data was wrong. Wave height there is PDF-only, but `g_o` is not the variable in doubt. **RM20 is a cheap answer to a question currently blocking the classifier decision.** |
| Q3 | **Should tide enter E?** | Evidence | Gao (2024) rates tide **4.55/5**, the highest of any factor, above weather (3.75). It is not modelled. Tide data **exists** in `data/raw_tide_marea.csv` (5 years hourly). Safety-relevant via harbour access, bar crossing, grounding for shallow-draft hulls. Would need a `g_tide` with thresholds grounded in local bathymetry — no corpus source currently provides these. |
| Q4 | **Should thresholds be derived from site data rather than only anchored to MET?** | Q1 outcome | See §2.3. |
| Q5 | **Is swell period recoverable?** | Data | **Revised 2026-09-06.** The all-NaN `swell_wave_*` columns are explained: ERA5-Ocean does not provide partitioned wind-wave/swell components — not a download error, and no re-request will fix it. **However `wave_period` IS fully populated and unused.** Mean wave period is not swell period, but encounter period relative to hull natural period is a genuine seakeeping determinant and this is the nearest available proxy. Finer models (MFWAM ~8 km, GFS Wave 0.16°) do provide partitioned components but only from 2021/2024 onward. |
| ~~Q6~~ | ✅ **RESOLVED 2026-09-06 — see F-14.** MFWAM 8 km vs ERA5-Ocean 50 km over 28,512 overlapping hours: r = 0.953, MFWAM mean 8.5% lower, max 1.84 vs 2.60 m. **Headline drops 12.4% → 8.3%, a 33% relative reduction.** Report both figures as a resolution-sensitivity check. | resolved | **New 2026-09-06 (F-12).** `era5_ocean` is 0.5° ≈ 50 km — the coarsest of nine available models — and it carries 97.5% of daylight CAUTION decisions. The choice was forced for a 2020–2024 series, since every finer model starts in 2021+. Options: (a) keep ERA5-Ocean and state the resolution as a limitation; (b) shorten the study period to 2021–2024 and use MFWAM at ~8 km, trading years for resolution; (c) run both and report sensitivity. **(c) is the strongest** — it would quantify how much the 12.4% headline figure depends on grid resolution, which is otherwise an open flank. |

---

## 6. Findings worth using in the papers

Three results from this session that strengthen the argument and are not yet written up:

**(a) MET's criteria are disjunctive.** The published warning criteria read *"strong winds with wind speeds from 40–50 kmph **and/or** rough seas with wave heights of up to 3.5 metres."* This is independent institutional support for non-compensatory worst-case aggregation — MET itself does not average wind against sea state. Currently uncited.

**(b) The empirical result the papers were missing.** Over five years of real site conditions, **Level 2 governance binds in 12.4% of departure-window hours** for small vessels — conditions in which the architecture withholds `DepartureTime` and `Duration` where a binary architecture would supply them. This is the direct answer to Review 3's "lacks empirical evidence."

**(c) The vessel conditioning is empirically necessary, not cosmetic.** Under the superseded vessel-blind thresholds, UNSAFE-by-wave was **unreachable at the deployment site** — five years, zero occurrences. Small and big vessels now classify differently in 10.7% of departure hours.

---

## 6a. Pre-registered predictions

**`data/prediction-register.csv` — 14 predictions registered 2026-09-06, before the diagnostic and hysteresis analyses were run.**

The failure mode this record exists to correct is a model elaborated ahead of validation. The corresponding risk on the way back is *rationalising results after seeing them*. Predictions are therefore registered in machine-comparable form — `pred_lo` / `pred_hi` bounds, with `actual` and `status` columns left blank for the analysis scripts to populate — so that confirmation or refutation is checked rather than narrated.

Two are headline predictions and deliberately falsifiable:

- **P13 — mode-chattering is NOT a demonstrated deployment problem at this site.** If it holds, both papers currently assert hysteresis as a deployment concern without evidence, and that claim needs softening. Predicted as a negative result.
- **P14 — the architecture reduces empirically to a vessel-conditional wave gate plus a night curfew.** Follows from `g_w` never binding, `g_m` being unmeasured, and `g_r` firing 264 times in five years. Registered now precisely so it cannot be explained away later.

Four are regression locks on figures already measured (P01–P04). **P01 is the important one: if `g_w` ever registers a non-zero activation, distrust the code before the finding.**

---

## 7. Immediate next steps

1. ~~**Diagnostic analysis**~~ — ✅ **done 2026-09-06.** See `empirical-findings-2026-09-06.md` F-7: only three functions ever bind; `g_w` and `g_m` never do.
2. ~~**Hysteresis / mode-chattering test**~~ — ✅ **done 2026-09-06.** F-6: 70 chattering events in five years (14/yr); hysteresis reduces non-scheduled transitions by 6.2%. **Negative result — the mode-chattering claim in both papers is unsupported at hourly resolution and must be withdrawn or qualified.**
3. **Investigate the MET warning archive** (Q2) — still open. `g_m` cannot be evaluated without it.
4. **Rewrite `evaluation-design-rq4.md`** around historical replay rather than 20 constructed scenarios — the scenarios become boundary and fail-safe cases within a much larger empirical frame. *Do this after Q1 resolves, not before.*
5. **Add the C3 Flehmig-style baseline** — the external comparison answering Review 3's novelty objection.
6. **Decide the F-1/F-7 framing** — report the reduced classifier as a finding, reduce it, or retain with explicit scope statements. See `empirical-findings-2026-09-06.md` §3. Feeds Q1 and Q4.

**All 14 pre-registered predictions resolved: 14 confirmed, 0 refuted.**

---

## 8. Related records

| Document | Relationship |
|---|---|
| `docs/superpowers/plans/2026-09-06-formal-model-and-evaluation-realignment.md` | Full audit trail: findings F1–F37, tier-by-tier propagation, verification pass |
| `docs/canonical/appendix-c-formalisation.md` C.9 | Known limitations of the formal model |
| `scripts/historical_replay.py` | The analysis producing §1's figures — re-runnable |
| `docs/canonical/empirical-findings-2026-09-06.md` | **Findings F-1 to F-8** from the three analyses, with consequences for both papers |
| `data/prediction-register.csv` | 14 pre-registered predictions (§6a) — all resolved, 14 confirmed / 0 refuted. Do not edit `pred_*` columns after registration |
| `scripts/diagnostic_binding.py` | Which function binds when f(E) ≠ SAFE — resolves P05–P08, P14 |
| `scripts/hysteresis_analysis.py` | Transition and chattering analysis — resolves P09–P13 |
| `docs/canonical/evaluation-design-rq4.md` | To be rewritten per §7.4 |
| `publications/active/ipsci-2026/revision-notes.md` | Review outcomes; Review 2 misassignment |
