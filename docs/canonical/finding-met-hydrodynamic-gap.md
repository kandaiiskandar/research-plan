# Finding: The MET–Hydrodynamic Threshold Gap

**Date:** 2026-09-06
**Status:** **Source of truth** for threshold provenance and the SAFE/CAUTION boundary question.
**Position agreed:** MET Malaysia remains the authoritative institutional source. Yaakob et al. (2015) and Jeong & Im (2023) are used as **comparison**, not replacement.
**Evidence:** `scripts/threshold_comparison.py` — MFWAM ~8 km, 28,501 hourly records, Kota Kinabalu, 2021-10 to 2024-12.

---

## 1. The structural discovery

MET Malaysia's *Kriteria Amaran Angin Kencang dan Laut Bergelora* reads:

> **FIRST** — Strong winds with wind speeds from 40–50 kmph **and/or** rough seas with wave heights of **up to 3.5 metres**. *Dangerous to small crafts.*
> **SECOND** — 50–60 kmph and/or waves **up to 4.5 metres**. *Dangerous to all shipping including fishing.*
> **THIRD** — exceeding 60 kmph and/or waves **exceeding 4.5 metres**.

Read carefully: **3.5 m is where Category 1 ends.** It is the Cat 1 / Cat 2 boundary.

**MET never states where Category 1 begins.**

The published criteria therefore supply an *upper* boundary and no *lower* one. **They structurally cannot provide the SAFE/CAUTION threshold.** This is not an omission in our reading — the value is absent from the source.

**Consequence for the architecture.** The existing design is already correct in structure: MET anchors the upper boundary (CAUTION/UNSAFE), hydrodynamic evidence fills the lower (SAFE/CAUTION). Using non-MET sources for the SAFE/CAUTION boundary is not a departure from official criteria — it is filling a gap those criteria leave open.

---

## 2. MET criteria never fire at this site

Observed wave range over 3.25 years: **0.04 – 1.84 m**, mean 0.59 m.

| Threshold | Value | Hours exceeded | % of all hours |
|---|---|---|---|
| **MET Cat 1** — "dangerous to small crafts" | 3.50 m | **0** | **0.0%** |
| **MET Cat 2** — "dangerous to all fishing" | 4.50 m | **0** | **0.0%** |
| Current model — small-vessel UNSAFE | 1.90 m | **0** | **0.0%** |
| Yaakob Boat A (6.54 m) — NORDFORSK failure, SS4 | 1.875 m | **0** | 0.0% |
| **Yaakob Boat A — operational ceiling, top of SS3** | **1.25 m** | **937** | **3.3%** |
| Jeong & Im — vessels ≤ 10 m LOA | 1.00 m | 2,997 | 10.5% |
| Current model — small-vessel CAUTION onset | 1.00 m | 2,997 | 10.5% |
| Yaakob Boat B (5.03 m) — NORDFORSK failure, SS3 | 0.875 m | 5,527 | 19.4% |
| **Yaakob Boat B — operational ceiling, top of SS2** | **0.50 m** | **15,395** | **54.0%** |

---

## 3. The gap, quantified

MET's small-craft criterion stands well above the measured operability limits of the vessels it nominally protects:

| MET Cat 1 (3.5 m) is… | …above |
|---|---|
| **1.9×** | Yaakob Boat A NORDFORSK failure (1.875 m) |
| **2.8×** | Yaakob Boat A operational ceiling (1.25 m) |
| **3.5×** | Jeong & Im ≤10 m LOA restriction (1.0 m) |
| **4.0×** | Yaakob Boat B NORDFORSK failure (0.875 m) |
| **7.0×** | Yaakob Boat B operational ceiling (0.5 m) |

**The consequential figure: Boat B — a real 5.03 m Malaysian fishing boat — is outside its documented seakeeping envelope 54% of the time, while no official warning would ever be in force.**

This is Jeong & Im's Korean finding reproduced at the Malaysian site with the mechanism made visible. They report that **82% of 2017–2022 capsizings occurred on days with no weather warning issued**. Here we can see why: the warning threshold sits up to seven times above the vessel's limit.

---

## 4. Neither source is wrong

**MET criteria are national warning thresholds.** Their function is to trigger public broadcast alerts across an entire coastal zone. They are *designed to be rare* — a Category 1 warning is an event, not a daily condition. They are correct for that purpose.

**Yaakob's limits are vessel-specific operability envelopes.** They answer a different question: at what sea state can *this hull* be worked safely, per NORDFORSK 1987. They are correct for that purpose.

The two are not in conflict. They answer different questions at different scales.

**The gap between them is the finding.** A small vessel can be far outside its documented seakeeping envelope while the national warning system is silent — because the warning system is not, and was never intended to be, a departure-decision instrument for an individual 5–7 m hull.

This is a *governance gap in the field*, structurally parallel to the governance gap in the architecture literature that motivates the thesis. Existing institutional mechanisms are binary and coarse-grained; what is missing is a graduated, vessel-conditional layer between "no warning" and "warning issued." That is precisely the space the CAUTION mode occupies.

---

## 5. What each threshold set would produce

Small vessel, departure window 05:00–09:00, MFWAM data:

| Threshold set | SAFE | CAUTION | UNSAFE |
|---|---|---|---|
| **MET Category 1 literal** (1.75 / 3.5 m) | **99.9%** | 0.1% | **0.0%** |
| **MET-anchored — current model** (1.0 / 1.9 m) | 89.9% | 10.1% | **0.0%** |
| Jeong & Im ≤10 m (1.0 / 2.0 m) | 89.9% | 10.1% | 0.0% |
| **Yaakob Boat A** (0.875 / **1.25** m) | 81.9% | 15.3% | **2.8%** |
| Yaakob Boat B (0.30 / 0.50 m) | 16.6% | 30.5% | **52.9%** |

A literal MET reading produces a system that classifies 99.9% of departure hours as SAFE and never restricts anything. The current model restricts 10.1% but **never reaches UNSAFE**.

---

## 6. Proposed amendment — one threshold

The small-vessel UNSAFE boundary of **1.9 m** was derived from Yaakob Boat A's *NORDFORSK failure point* (SS4, Hs ≈ 1.875 m).

Yaakob reports a second, distinct quantity: Boat A's **operational ceiling** of **1.25 m** — the top of Sea State 3, the last sea state the vessel passes.

These are different things. "Should not depart" maps more naturally to the ceiling than to the failure point: the failure point is where seakeeping criteria are breached, whereas the ceiling is the last condition under which the vessel remains operable.

**Proposed:** small-vessel UNSAFE at **1.25 m** rather than 1.90 m.

| | SAFE | CAUTION | UNSAFE |
|---|---|---|---|
| Current (UNSAFE 1.9 m) | 89.9% | 10.1% | **0.0%** |
| Proposed (UNSAFE 1.25 m) | 81.9% | 15.3% | **2.8%** |

This is **the same source, read more carefully** — not a recalibration chosen to make the model fire. The distinction between operational ceiling and failure point is Yaakob's own, and the ceiling is the more appropriate quantity for a departure gate.

**✅ ADOPTED 2026-09-06.** Applied to `appendix-c-formalisation.md` first, then propagated to 10 downstream documents and 4 analysis scripts. Registered as P19/P20.

**Why it was adopted despite producing a worse headline.** The Level 2 binding figure falls from 8.3% to 6.1%. The amendment was made on the provenance argument — the operational ceiling is the more defensible reading of Yaakob — and *not* on its effect on the numbers. Adopting a threshold because it produced a larger headline would have been the same error the decision record warns against for `g_w`.

**What it buys.** Daylight UNSAFE rises from **3 hours to 409** (0.02% → 3.13%), and the weather-driven share of all UNSAFE hours from **0.1% to 7.0%**. Under the prior threshold the participation gate was reachable only by darkness; it is now reachable by sea state. That removes the sharpest criticism available against the domain instantiation — that `G(S) = 0` was a night curfew rather than a weather gate.

**Reportable figure is now 6.1%**, superseding 8.3%. P18 remains valid for the threshold it was registered against.

**Open:** whether the medium and big rows need the same treatment. Both currently use failure-point-style reasoning scaled from MET. Neither has vessel-specific NORDFORSK data.

---

## 7. How to present this

**MET remains the authoritative source, and the paper should say so.** The provenance is:

| Boundary | Source | Status |
|---|---|---|
| CAUTION/UNSAFE, big vessel | MET Cat 1 maximum, 3.5 m | **Official** |
| Warning tiers for `g_m` | MET three-tier system | **Official** |
| Wind thresholds `g_w` | MET Cat 1 / Cat 2 onset | **Official** |
| Rainfall `g_r` | MET Ribut Petir | **Official** |
| **SAFE/CAUTION, all vessels** | Hydrodynamic — **MET provides no value** | Necessarily non-MET |
| **Small/medium vessel rows** | Hydrodynamic — **MET has no vessel-specific criteria** | Necessarily non-MET |

The honest framing: *the architecture adopts MET Malaysia's published criteria wherever MET speaks, and fills with peer-reviewed hydrodynamic evidence only where MET is silent — specifically, the onset of Category 1 conditions and any vessel-specific differentiation.*

That is defensible in a viva, cites the official authority, and turns the gap into a contribution rather than a weakness.

---

## 8. Related

| Document | Relationship |
|---|---|
| `empirical-findings-2026-09-06.md` | F-1 to F-14, including the wave-resolution and wind findings this builds on |
| `data-provenance.md` | Where the wave data comes from and its limitations |
| `decision-record-empirical-first.md` | The empirical-first sequencing that produced this |
| `appendix-c-formalisation.md` | Where §6's amendment must be applied first |
| `scripts/threshold_comparison.py` | Reproduces every figure above |
