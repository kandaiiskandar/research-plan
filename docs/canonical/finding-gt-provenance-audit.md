# Finding: `g_t` Provenance Audit — The Most Load-Bearing Component Has the Weakest Boundaries

**Date:** 2026-09-08
**Status:** **Audit only. No specification change made.** `g_t`, Appendix C, the scripts, thresholds, figures, prediction outcomes and the prediction register are all unmodified. This document exists to be reviewed before any correction is approved.
**Headline:** the evidence supports *"night operation is riskier"*. It does **not** support *"therefore 17:00 and 19:00 are valid safety thresholds"*. Those are two different claims and the project has been treating the first as if it established the second.

---

## 1. Current canonical definition

```
             ⎧ SAFE     06:00 ≤ t < 17:00
    g_t(t) = ⎨ CAUTION  17:00 ≤ t < 19:00
             ⎩ UNSAFE   19:00 ≤ t < 06:00
```

Stated identically in `appendix-c-formalisation.md` (C.1 note, C.2 table, Theorem C.1 partition), `docs/reference/explainer-per-component-classification-functions.md`, `docs/implementation/dataset-label-derivation.md`, and implemented in six scripts. **No inconsistency was found between any of these** — the definition is uniform. The problem is not consistency; it is provenance.

**Appendix C's stated basis, verbatim:**

| Class | Threshold | Stated empirical basis |
|---|---|---|
| SAFE | 06:00 ≤ t < 17:00 | "Daytime — sufficient daylight for safe operation and return to port" |
| CAUTION | 17:00 ≤ t < 19:00 | "Approaching darkness — elevated visual risk; restricted visibility onset" |
| UNSAFE | 19:00–06:00 | "Night — restricted visibility; Atacan & Düzbastılar (2023): highest accident probability and consequence scores under night conditions" |

---

## 2. Four propositions, separately assessed

| # | Proposition | Evidence status |
|---|---|---|
| **P1** | Night fishing/navigation carries elevated risk | **Supported.** Multiple independent sources |
| **P2** | `06:00` is a defensible SAFE boundary | **Not supported.** And see §7 — it is *before sunrise every day of the year* |
| **P3** | `17:00` is a defensible SAFE→CAUTION boundary | **Not supported.** No source states it; it precedes sunset by ~1–1.5 hours |
| **P4** | `19:00` is a defensible CAUTION→UNSAFE boundary | **Not supported as stated**, though it happens to fall near the end of civil twilight — see §7 |

**P1 is well-evidenced.** Atacan & Düzbastılar (2023) [[notes]](../../notes/Determination%20of%20risk%20perception%20in%20small-scale%20fishing%20and%20navigation.md): 30 small-scale fishing captains, bridge simulator, Fine-Kinney method. Night navigation rated substantially more dangerous than daytime — accident probability 4.08 vs 3.43, consequence 12.80 vs 8.53; night + heavy weather produced the highest consequence score of any condition tested (37.03); restricted visibility was the single highest-rated probability factor (7.90). Dominguez-Péry et al. (2023) corroborate from 504 IMO reports.

**P2–P4 are a different claim, and the source does not address it.** Atacan & Düzbastılar tested *"night navigation"* as a simulator **condition** against *"calm weather/sea"*. **The study contains no clock times at all.** It does not partition the day, does not identify when night begins, and could not — the design compares two named conditions, not times.

**A search of the entire project found no source that states 06:00, 17:00, or 19:00 as a safety boundary.**

---

## 3. Provenance chain

| Threshold | First project occurrence | Cited source | What the source actually supports | Gap |
|---|---|---|---|---|
| **06:00** | appendix-c C.1 time-of-day note | none cited | — | **Unsupported jump.** No source cited at all; "sufficient daylight" asserted |
| **17:00** | appendix-c C.1 time-of-day note | Atacan & Düzbastılar via the general `t` justification | Night is riskier than day | **Unsupported jump.** P1 → P3 does not follow. Source has no clock times |
| **19:00** | appendix-c C.1 / C.2 table | Atacan & Düzbastılar, cited *in the row* | Night is riskier than day | **Unsupported jump.** Same. The citation sits in the row as if it fixed the value |

**The project already knew.** The extraction notes for Atacan & Düzbastılar carry this, written when the paper was first read:

> *"**For the CAUTION zone (17:00–19:00) specifically:** You still need a source anchoring these specific thresholds to Malaysian tropical twilight timing… A citation to Malaysian Meteorological Department data or a nautical almanac for the region would close this gap."*

**That gap was identified, recorded, and never closed.** The thresholds entered the specification anyway and have been in continuous use since.

**A second, compounding defect in the same note.** It reasons that *"civil twilight in peninsular Malaysia ends approximately 30–40 minutes after sunset, which occurs around 19:00–19:30 year-round near the equator."* That is approximately correct **for peninsular Malaysia** — and the deployment site is **Kota Kinabalu, Sabah**. See §7: the figure does not transfer, and the direction of the error matters.

**Geographic transfer, separately.** Atacan & Düzbastılar studied **two Turkish ports** (İskele n=20, Çeşmealtı n=10) in the Aegean, ~38°N. `g_t` governs a site at ~6°N. Day-length variation at 38°N is roughly 9–15 hours across the year; at 6°N it is 11.8–12.5 hours. The *qualitative* finding (night is riskier) transfers unproblematically. Any *quantitative* timing inference would not, and none is claimed — but the citation's placement in the UNSAFE row invites the reader to think otherwise.

---

## 4. How load-bearing `g_t` is

**Verified from existing published figures — nothing recomputed.**

| Measure | Value | Source | Status |
|---|---|---|---|
| `g_t` at maximum, all-hours non-SAFE | **87.63%** (primary) / 91.10% (resolution) | §0a, `canonical_figures.py` | ✅ Verified as published |
| `g_t` at maximum, daylight CAUTION | 0.00% | §0a | ✅ By construction — `g_t` is SAFE in daylight |
| Scheduled clock transitions (06:00/17:00/19:00) | **5,189 of 5,416 = 95.8%** of all state transitions | F-6, `hysteresis_analysis.py` | ✅ Verified as published |
| `g_t` activation rate | **54.17%** of all hours (13 of 24: 2 h CAUTION + 11 h UNSAFE) | Arithmetic from the specification | ✅ Derivable without touching data |

**One important qualification on the 87.63%.** Inspecting `canonical_figures.py` line 164, the metric is `(v[nonsafe] == f_small[nonsafe]).mean()` — the share of non-SAFE hours in which `g_t` **is at the maximum**, ties included. It is *not* the share in which `g_t` is the **sole** determinant. The published figure is an at-maximum share and should be described as such.

**Analyses that do not exist and were not invented:**

| Requested measure | Status |
|---|---|
| SAFE→CAUTION transitions attributable to `g_t` | ❌ **Not computed by any script.** `hysteresis_analysis.py` separates scheduled from non-scheduled transitions but does not split by direction |
| CAUTION→UNSAFE transitions attributable to `g_t` | ❌ **Not computed** |
| Exclusive binding — `g_t` as sole determinant | ❌ **Not computed.** No script contains binding-attribution logic; all report at-maximum shares |
| Hours where another component is at equal-or-higher severity | ❌ **Not computed** as a distinct figure |

**Consequence:** the claim *"`g_t` accounts for 87.63% of non-SAFE classifications"* is verified for the metric as defined, but the stronger reading — that `g_t` alone drives them — is **not currently supported by any computed figure.** If the specification changes, these four analyses would be needed to state the effect precisely.

---

## 5. Semantics of `t` — a formal/evidential mismatch

**What `t` is formally:** `t ∈ [0, 24)`, "time of day (hour, 24-hour clock)" — **local civil clock time**, fixed boundaries, no date, no location, no solar term.

**What the evidence is about:** *darkness and restricted visibility*. Appendix C says so explicitly — "restricted visibility — the principal mechanism by which nighttime elevates risk for small vessels without radar".

**These are not the same variable.** Civil clock time is being used as a **proxy** for solar illumination. The proxy is never declared as one, is never calibrated against the thing it proxies, and — per §7 — is materially misaligned at this site.

Nothing in the specification states which of the following `t` is meant to capture: daylight/darkness status, sunrise/sunset, nautical or civil twilight, or an operating-hours policy. **All four readings are consistent with the current text, and they imply different boundaries.** That ambiguity is itself an audit finding.

---

## 6. Which interpretation the evidence supports

| | Interpretation | Verdict |
|---|---|---|
| **A** | Evidence-derived safety thresholds | **Rejected.** No source states any of the three values. The one cited source contains no clock times |
| **B** | Policy thresholds operationalising a nighttime-risk principle | **Partially available, but not claimed.** This *would* be defensible — the architecture is entitled to design choices — but appendix-c presents the values as empirically based ("Atacan & Düzbastılar: highest accident probability…"), not as policy. Adopting B would require rewriting the justification, not merely relabelling |
| **C** | Proxy for sunrise/sunset or daylight | **Closest to intent, contradicted by the values.** Appendix C's language ("sufficient daylight", "approaching darkness") is proxy language, but §7 shows the values do not track the solar cycle at this site |
| **D** | Unsupported | **This is the current state for all three boundaries as presently justified.** |

**Assessment: D as it stands, with B available as an honest reframing and C as the strongest candidate for correction.** The values are not arbitrary in intent — the intent is plainly C — but no source supports the specific numbers, and the solar arithmetic does not.

---

## 7. Fixed clock time versus the phenomenon, at this site

**Authoritative solar data for Kota Kinabalu (5.98° N, 116.07° E), verified 2026-09-08 — see §10.**

| | Range across the year |
|---|---|
| **Sunrise** | **06:01** (24 May) – **06:34** (2 Feb) |
| **Sunset** | **17:57** (11 Nov) – **18:35** (17 Jul) |
| Day length | 11 h 46 m – 12 h 28 m |

Set against the thresholds:

| Boundary | Model says | Actual solar condition | Mismatch |
|---|---|---|---|
| **06:00** SAFE begins | full daylight | **sunrise is 06:01–06:34 — the sun has not risen** | **SAFE begins before sunrise on every day of the year**, by 1 to 34 minutes |
| **17:00** CAUTION begins | "approaching darkness" | sunset is 57–95 minutes away | **CAUTION is asserted in full daylight** |
| **19:00** UNSAFE begins | "night" | sunset 17:57–18:35; civil twilight ends roughly 20–25 min later | **Roughly defensible** — 19:00 falls at or after the end of civil twilight year-round. The only boundary the solar geometry supports, and it is supported by coincidence rather than derivation |

**The compounding error identified in §3 is now quantified.** The extraction note reasoned from *peninsular Malaysia*, where sunset is ~19:00–19:30. Kota Kinabalu sits ~13° further east in the **same UTC+8 zone**, so its solar day runs roughly 50–70 minutes earlier. **Sunset in Sabah is before 18:35 all year — it is never near 19:00.** The one piece of twilight reasoning in the project was performed for the wrong part of Malaysia, and it is the reasoning that made 19:00 look principled.

**A structural point about the CAUTION band.** Its stated purpose is to capture the transition into darkness. At this site that transition occupies roughly 17:57–19:00 in November and 18:35–19:00 in July. The band 17:00–19:00 is two hours wide and fixed; the phenomenon it targets is ~25 minutes wide and moves by ~38 minutes across the year. **The band is wide enough to contain the transition, but its leading hour is daylight.**

**Candidate alternative — recorded, not adopted.** A solar-referenced formulation (`g_t` conditioned on sunrise/sunset or civil twilight for the site's coordinates and date) appears more defensible than fixed clock times, because it tracks the phenomenon the evidence is actually about. **This is recorded as a candidate requiring its own evidence and evaluation. It is not proposed here and no such threshold has been introduced.** It would need: an authoritative solar source, a decision on which solar event (sunset vs civil vs nautical twilight), and a justification for any offset — each subject to the same provenance discipline that caught the 7.5 mm/hr and 22 kn errors.

---

## 8. Resolution options

| Option | Description | Cost |
|---|---|---|
| **1. Reframe as policy (B)** | Keep 06:00/17:00/19:00; rewrite the justification to state them as **design choices** operationalising a nighttime-risk principle, with the solar mismatch disclosed | No figures change. Honest, cheap. Leaves a component governing 87.63% of non-SAFE classifications on undefended values |
| **2. Solar-referenced `g_t` (C)** | Redefine against sunrise/sunset or civil twilight for the site | **All time-dependent figures change.** Requires new solar data, a new source, and full recomputation |
| **3. Correct the values, keep fixed clock** | Move boundaries to match observed solar range (e.g. SAFE from ~06:30, CAUTION from ~17:45) | Figures change; still a proxy, still needs justification for the specific numbers |
| **4. Report as a limitation, defer** | Document in C.9 and Threats to Validity; change nothing | No cost now. A reviewer who checks sunset times at 6°N will find the 06:00 problem |

**Not recommended: doing nothing silently.** The 06:00 boundary is wrong in a checkable way — SAFE begins before sunrise every day of the year — and it is the sort of thing an examiner familiar with the region would notice.

---

## 9. Propagation required if a correction is approved

**Documents:** `appendix-c-formalisation.md` (C.1 note, C.2 `g_t` table, Theorem C.1 partition, C.9.1); `docs/reference/explainer-per-component-classification-functions.md` (definition + worked examples); `docs/implementation/dataset-label-derivation.md`; `docs/justification/safety-state-design.md`; `CLAUDE.md` (threshold table, `g_t` open block); the Atacan & Düzbastılar extraction note (twilight paragraph is wrong for Sabah regardless of what is decided).

**Scripts (6):** `canonical_figures.py`, `condition_comparison.py`, `diagnostic_binding.py`, `hysteresis_analysis.py`, `historical_replay.py`, `compare_v1_v2.py`, `threshold_decision.py`.

**Figures — every time-dependent value in §0a:** Level 2 binding rate (7.72% / 5.98%), daylight UNSAFE hours, weather-driven share of UNSAFE, `g_t` and `g_o` binding shares, and the C0/C1/C2/C3 divergence matrix (all conditions share `g_t`).

**Predictions at risk:** **P07** (`g_t` share of non-SAFE, >70%), **P09** (total transitions 5400–8000 — *`g_t` generates ~3 scheduled transitions/day, so this is almost entirely a `g_t` figure*), **P10**, **P11**, **P12**, **P13** (all hysteresis, all partitioned on `g_t` changes), **P14** (the "wave gate plus night curfew" framing), **P19/P20/P22/P23/P24** (departure-window and daylight-window figures). **Any change to `g_t` is the largest propagation this project has faced** — larger than the wave, rainfall or wind amendments, because `g_t` participates in every windowed metric.

**Per the register guard installed 2026-09-08:** resolved predictions are immutable. A `g_t` change would require explicit, documented re-resolution of each affected prediction, in the manner of P16 and P22 — not a silent re-run.

---

## 10. Sources

| Source | Establishes |
|---|---|
| [timeanddate.com — Sunrise and sunset, Kota Kinabalu](https://www.timeanddate.com/sun/malaysia/kota-kinabalu) | Sunrise 06:01–06:34; sunset 17:57–18:35; day length 11h46m–12h28m |
| [timeanddate.com — Sun & moon times, Kota Kinabalu](https://www.timeanddate.com/astronomy/malaysia/kota-kinabalu) | Civil twilight bounds |
| [Gaisma — Kota Kinabalu, sunrise/sunset/dawn/dusk, whole year](https://www.gaisma.com/en/location/kota-kinabalu.html) | Corroborating annual curve |
| Atacan & Düzbastılar (2023) [[notes]](../../notes/Determination%20of%20risk%20perception%20in%20small-scale%20fishing%20and%20navigation.md) | P1 only — night navigation riskier than day. **Contains no clock times.** Turkish ports, ~38° N |

*Solar figures should be re-verified against a nautical almanac or MET Malaysia before any threshold is derived from them. They are used here as audit evidence, not as a proposed threshold source.*

---

## 11. The logical point, stated plainly

> **"Nighttime operation is riskier"** is well-evidenced, from a relevant population, by an appropriate method.
>
> **"Therefore 17:00 and 19:00 are valid safety thresholds"** does not follow, is not stated by any source in the corpus, and — at this site — is contradicted by the solar geometry for two of the three boundaries.

The first claim justifies **including `t` in E**. It does not justify **any particular partition of the day**. Appendix C currently uses evidence for the first to license the second, and does so in the component that determines the largest share of non-SAFE classifications in the entire model.

---

## 12. Related

| Document | Relationship |
|---|---|
| `appendix-c-formalisation.md` C.1, C.2, C.9.1 | Where `g_t` is defined and where the correction would land |
| `empirical-findings-2026-09-06.md` §0a, F-6, F-7 | The 87.63%, the 95.8% scheduled-transition figure, the binding profile |
| `finding-met-lower-boundary-gap.md` | The provenance discipline this audit applies — *a canonical threshold preserves its source value, and an unsourced threshold is a defect* |
| `finding-bottom-semantics.md` | `t ∉ D` (C.2.0.5 D1) rests on `g_t` being clock-derived; unaffected by this audit |
| `notes/Determination of risk perception…md` | Records the gap at first reading and was never actioned; its twilight paragraph is wrong for Sabah |
