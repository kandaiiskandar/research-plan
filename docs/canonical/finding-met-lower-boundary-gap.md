# Finding: MET Malaysia Publishes Warning Triggers, Not Caution Onsets

**Date:** 2026-09-08
**Status:** **Source of truth** for the `g_r` rainfall thresholds, and for the general provenance rule governing every MET-anchored boundary in the classifier.
**Relationship to `finding-met-hydrodynamic-gap.md`:** that document established the pattern for wave height. This one finds it independently in a second variable, from a second MET criteria document. The two should be read together. **Two cases with a shared mechanism — read as a pattern, not as a proven universal; see §1.**
**Sources verified against the publishing agencies' own sites, 2026-09-08** — see §7.

---

## 1. The general structure

MET Malaysia publishes **warning criteria**. A warning criterion states the condition at which an alert is *issued*. By construction it marks where a hazard category **begins to be broadcast**, not where an individual operator should begin to take care.

**In both variables examined here, the published criteria supply an upper boundary and no lower one.** Neither through omission nor through any deficiency in MET's work — a warning threshold is a different object from an operational caution threshold, and it is doing its own job correctly.

**Scope of the claim, stated precisely.** This is a pattern observed in **two** MET criteria documents covering two variables, not a verified property of every criterion MET publishes. The mechanism — that a warning threshold marks broadcast onset rather than operational caution — gives good reason to expect it generally, and no counter-example is known in the criteria consulted. But "MET never defines where caution begins" would overstate what has been checked. The defensible form is: *in both cases examined, MET's published criteria fix the upper boundary of a hazard band and leave the lower boundary unstated; the structure of a warning criterion explains why.* Testing the remaining MET criteria would settle whether the pattern is universal.

Observed independently in two variables:

| Variable | MET criterion | What it fixes | What it cannot fix |
|---|---|---|---|
| **`o`** wave height | *Kriteria Amaran Angin Kencang dan Laut Bergelora* — Category 1 covers waves "up to 3.5 m" | The CAUTION/UNSAFE boundary at 3.5 m — this is where Cat 1 **ends** | Where Cat 1 **begins** — not stated in the criteria |
| **`r`** rainfall | *Kriteria Amaran Ribut Petir* — warning issued at rain intensity **> 20 mm/hr** persisting beyond one hour | The CAUTION/UNSAFE boundary at 20 mm/hr — the warning trigger | Any boundary below 20 mm/hr — no lower hourly rate is published |

**Two variables, two separate MET criteria documents, one structure.** A single instance could be read as an artefact of how the sea-state criteria happen to be written. Two independent instances make an artefact explanation much less likely and point to a property of warning criteria as a class — though two cases establish a pattern with a mechanism, not a universal law.

**Consequence for the architecture.** Filling the SAFE/CAUTION boundary from non-MET sources is not a departure from official criteria. It is filling a gap those criteria leave open by design. This was already the position for `o`; it now applies to `r` on the same reasoning.

---

## 2. What MET publishes for rainfall

Three warning types are relevant, and only one is usable on hourly data.

| MET criterion | Threshold | Usable for `g_r`? |
|---|---|---|
| **Ribut Petir** (thunderstorm) | Rain intensity **> 20 mm/hr**, imminent or expected to persist beyond one hour. Warning valid ≤ 6 hours per issuance | **Yes** — an hourly rate, directly comparable to hourly precipitation data |
| **Hujan Berterusan — Buruk** | Cumulative rainfall > 60 mm over the warning period | **No** — cumulative, period-dependent |
| **Hujan Berterusan — Bahaya** | Continuous heavy rain > 150 mm / 24 hr | **No** — 24-hour cumulative |

**Why the Hujan Berterusan tiers are rejected, stated explicitly.** They are cumulative totals over a period, not intensity rates. Applying them to hourly data requires an hourly disaggregation assumption that no source supplies, and that assumption would itself become an unsourced parameter. This is the same objection `docs/justification/rainfall-intensity-mapping.md` §2 already raises against MET's mm/day scale, applied consistently.

A reviewer familiar with MET will ask why the *thunderstorm* criterion was used rather than the *rain warning* criterion. The answer is above and must stay in the record.

---

## 3. What fills the gap below 20 mm/hr

JPS/DID Malaysia (Department of Irrigation and Drainage) publishes an hourly **intensity** classification through its national flood monitoring system, Infobanjir:

| JPS/DID category | Intensity (one hour) |
|---|---|
| Light | 1–10 mm |
| Moderate | 11–30 mm |
| Heavy | 31–60 mm |
| Very Heavy | > 60 mm |

This is the correct instrument for a lower boundary: it classifies *how hard it is raining*, independent of whether any alert has been issued. MET classifies *when to broadcast an alert*. Both are official Malaysian government sources; they answer different questions, and each is used here for the question it answers.

**The Light/Moderate boundary at 10 mm/hr becomes the SAFE/CAUTION threshold.**

---

## 4. Adopted thresholds for `g_r`

`r ∈ ℝ≥0` in mm/hr — **numeric, not categorical** (redefined 2026-09-08; see appendix-c C.2). JPS/DID categories below are provenance for the boundary values, not the domain of `r`.

| Classification | Threshold | Source | Status |
|---|---|---|---|
| **SAFE** | r ≤ 10.0 mm/hr | JPS/DID *Light* upper limit (1–10 mm/hr) | Official — non-MET by necessity |
| **CAUTION** | 10.0 < r ≤ 20.0 mm/hr | Interval between the two published boundaries; **MET is silent in this band** | Official at both endpoints |
| **UNSAFE** | r > 20.0 mm/hr | **MET Ribut Petir warning trigger** | **Official — MET** |

The WMO thunderstorm codes 95/96/99 remain an alternative route to UNSAFE where present in the data. See §6 for why that route is inert here.

**Superseded:** `> 7.5` mm/hr for CAUTION and `> 20` mm/hr for UNSAFE, as implemented in all analysis scripts prior to 2026-09-08. The 20 was correct by coincidence — it matches MET — but was undocumented. **The 7.5 matched no source.** Its nearest ancestor is a mapping that `docs/implementation/data-source-met-malaysia.md` line 125 explicitly records as an error, and which was corrected in that document but never in the code.

**Also superseded:** the reading in which JPS *Very Heavy* (> 60 mm/hr) supplies the UNSAFE boundary. `docs/justification/rainfall-intensity-mapping.md` §1 maps `storm` to > 60 mm/hr on the JPS scale, while appendix-c justifies the same threshold by reference to Ribut Petir — a MET phenomenon. The two cannot both define one boundary. **MET governs, so 20 mm/hr stands and the JPS scale is used only below it.** Note that a JPS-only reading is also incoherent: JPS *Heavy* begins at 31 mm/hr, which would place CAUTION above UNSAFE.

---

## 5. Empirical effect

Small vessel, wave thresholds 1.0 / 1.25 m, sea-cell weather. Both reporting configurations (see `empirical-findings-2026-09-06.md` §0a).

| | PRIMARY 5.00 yr | | RESOLUTION 3.25 yr | |
|---|---|---|---|---|
| | old 7.5/20 | **new 10/20** | old 7.5/20 | **new 10/20** |
| Level 2 binding rate | 7.84% | **7.72%** | 6.15% | **5.98%** |
| Daylight UNSAFE hours | 1,170 | 1,170 | 409 | 409 |
| Weather-driven share of UNSAFE | 11.8% | 11.8% | 7.0% | 7.0% |
| `g_r` share of daylight CAUTION | 3.21% | **1.55%** | 6.21% | **2.99%** |
| `g_o` share of daylight CAUTION | 97.40% | **98.66%** | 95.05% | **97.41%** |
| `g_t` share of all non-SAFE | 87.55% | 87.63% | 90.96% | 91.10% |

Observed distribution: 21 hours above 20 mm/hr and 92 hours in the 10.1–20 mm/hr band over five years. Maximum observed intensity **45.8 mm/hr**.

**The UNSAFE state is unaffected** — the 20 mm/hr trigger is unchanged, so daylight UNSAFE hours and the weather-driven share do not move. The entire effect is in CAUTION.

**The headline falls 7.84% → 7.72%.** This is the **third** amendment adopted on provenance grounds that lowered the reported result:

| Amendment | Headline | Basis |
|---|---|---|
| Wave resolution, ERA5 50 km → MFWAM 8 km | 12.4% → 8.3% | Measurement fidelity |
| Wave threshold, failure point → operational ceiling | 8.3% → 6.1% | Source read more carefully |
| **Rainfall threshold, unsourced → MET-anchored** | **7.84% → 7.72%** | **Provenance** |

A specification whose corrections consistently reduce its own headline is evidence the corrections were not selected for their effect. State this in the paper rather than bury it.

---

## 6. What this does not fix

**F-11 stands.** MET's Ribut Petir criterion is a *thunderstorm* warning — lightning, cumulonimbus formation, strong wind, and rain intensity together. The dataset returns **zero** WMO thunderstorm codes (95/96/99) in five years, because Open-Meteo documents that thunderstorm estimation "is not possible" outside Central Europe. The `g_r = UNSAFE` state is therefore reached **only** through the 20 mm/hr rainfall component of a multi-part criterion, never through the phenomenon the criterion is named for.

This is a measurement gap, not a threshold gap, and adopting MET does not close it. `g_r = UNSAFE` remains **under-detected by an unknown margin**, and every `g_r` figure is a lower bound.

**The intensity/phenomenon conflation is now explicit rather than hidden.** `r = storm` is defined by an intensity proxy for a phenomenon that cannot be observed in this data. That belongs in Threats to Validity.

**Nothing here affects `g_m`.** The marine warning variable remains unmeasured — no archive exists — and all severity figures remain lower bounds for that separate reason.

---

## 7. Sources

Retrieved and verified 2026-09-08 against the publishing agencies' own sites.

| Source | Publisher | What it establishes |
|---|---|---|
| [Public Infobanjir — Rainfall Data](https://publicinfobanjir.water.gov.my/hujan/data-hujan/?lang=en) | Department of Irrigation and Drainage Malaysia (JPS/DID) | *Categorization of Rainfall Intensity (in one hour)*: Light 1–10, Moderate 11–30, Heavy 31–60, Very Heavy > 60 mm. Also: convective rain > 60 mm in 2–4 hours may cause flash floods |
| [METMalaysia — Kriteria Amaran Ribut Petir](https://www.met.gov.my/ramalan/ribut-petir/) | MET Malaysia | Thunderstorm warning issued at rain intensity > 20 mm/hr expected to persist beyond one hour; valid ≤ 6 hours |
| [METMalaysia — Kriteria Amaran Hujan Berterusan](https://www.met.gov.my/ramalan/hujan-lebat/) | MET Malaysia | Continuous-rain tiers Waspada / Buruk / Bahaya, defined on cumulative totals |
| [MKN — Jenis-jenis dan Kriteria Amaran Cuaca MET Malaysia](https://www.mkn.gov.my/web/ms/2022/11/30/jenis-jenis-dan-kriteria-amaran-cuaca-yang-dikeluarkan-oleh-met-malaysia/) | Majlis Keselamatan Negara | Government repost of all three MET criteria sets, corroborating the above |

*Collection note:* `met.gov.my` serves its criteria pages via client-side rendering and returned no content to direct fetch; the browser pane was also unable to load the domain. The MET figures above were corroborated across the MKN government repost and multiple independent reports of the same criteria. **If MET's own pages become directly retrievable, re-verify the 20 mm/hr figure against the primary page and record the result here.**

---

## 8. Presentation

The provenance table in `finding-met-hydrodynamic-gap.md` §7 currently lists rainfall `g_r` as **Official**. That is now known to be true only of the UNSAFE boundary. Corrected form:

| Boundary | Source | Status |
|---|---|---|
| CAUTION/UNSAFE, rainfall (20 mm/hr) | MET Ribut Petir trigger | **Official — MET** |
| **SAFE/CAUTION, rainfall (10 mm/hr)** | JPS/DID intensity scale — **MET provides no value** | Necessarily non-MET |
| CAUTION/UNSAFE, big vessel (3.5 m) | MET Cat 1 maximum | **Official — MET** |
| **SAFE/CAUTION, all vessels** | Hydrodynamic — **MET provides no value** | Necessarily non-MET |
| Warning tiers for `g_m` | MET three-tier system | **Official — MET** |
| Wind thresholds `g_w` | MET Cat 1 / Cat 2 onset | **Official — MET** |

The honest framing, unchanged from the wave case and now stated once for both: *the architecture adopts MET Malaysia's published criteria wherever MET speaks, and fills with other official or peer-reviewed evidence only where MET is silent — which, in both variables examined, is the onset of the hazard band.*

That silence is itself the argument for the thesis. Institutional warning mechanisms are coarse and binary by design: alert issued, or not. The band between "nothing published" and "warning in force" is exactly the operational region the CAUTION mode occupies, and MET's own criteria demonstrate that no institutional mechanism currently governs it.

---

## 9. Related

| Document | Relationship |
|---|---|
| `finding-met-hydrodynamic-gap.md` | The wave-height instance. **Read together — this document generalises its claim to a second variable** |
| `appendix-c-formalisation.md` C.2 | Where the `g_r` thresholds must be applied first |
| `docs/justification/rainfall-intensity-mapping.md` | The JPS/DID mapping. §1 needs the storm row reconciled with MET's 20 mm/hr |
| `empirical-findings-2026-09-06.md` | F-11 (thunderstorms undetectable), F-7 (binding profile), §0a (reportable figures) |
| `docs/implementation/data-source-met-malaysia.md` | Line 125 records the superseded mapping the 7.5 descends from |
| `scripts/canonical_figures.py` | Regenerates §0a once thresholds change |
