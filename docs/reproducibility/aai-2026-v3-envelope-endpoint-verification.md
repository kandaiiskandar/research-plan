# AAI 2026 — V-3 Envelope Endpoint Verification

**Finding verified:** V-3, the sourced-threshold envelope endpoints
**Manuscript:** *From Declared Risk Levels to Admissible Recommendations: Measuring the Operational Effect of AI Governance Through Deterministic Historical Replay*
**Date:** 9 October 2026
**Mode:** read-only. No code, data, figure, table or manuscript was edited. **The sensitivity experiment was not rerun** — the existing preserved outputs were sufficient. The only computation performed was arithmetic on values already present in those outputs.

**Endpoints under verification**

| | Minimum | Maximum |
|---|---|---|
| PRIMARY | 5.67% | 9.56% |
| RESOLUTION | 4.26% | 6.64% |

---

## 1. Headline finding

**All four endpoints reproduce exactly.** Each is traceable to a single named grid cell, a single threshold tuple, a known denominator and a unique integer CAUTION-hour count.

**All four are nonetheless produced by a rainfall threshold that the project's own provenance table classifies as researcher-defined rather than externally sourced.**

`docs/analysis/threshold-sensitivity-analysis.md:55`:

> | `R_C` | 5.0, 15.0, 19.9 | mm/hr | Perturbation; 19.9 is the degenerate case `R_C → R_U` | **Researcher-defined sensitivity value** |

Only one `R_C` value in the repository is externally sourced — line 53:

> | `R_C` | **10.0** | mm/hr | JPS/DID Infobanjir *Light* upper limit | **Externally sourced, non-MET (canonical)** |

The two minima sit at `R_C` = 19.9 and the two maxima at `R_C` = 5.0. Neither value is sourced.

This puts §C and §J of that same document in direct contradiction. §J line 217 labels the envelope row:

> | **Externally sourced thresholds, small vessel only** (canonical; Yaakob failure-point variant; **sourced `R_C` values**) | **5.67%** | **5.81%** | **9.56%** |

while §C line 64 promises:

> No new value is introduced here that is later presented as externally validated.

That promise is not kept for `R_C` = 5.0 and `R_C` = 19.9.

---

## 2. Evidence integrity

| | |
|---|---|
| Branch | `AMIT-v5` |
| HEAD | `a7f77d8351ec94c586309d796aabd1230f4886dd` |
| Modified tracked files | **0** |
| `scripts/sensitivity/threshold_sensitivity.py` | `6ddaea583941134b147956cc0d45cd785431ea7290643ba35a910a17f07a5730` — matches the run manifest |
| `…/threshold-sensitivity-20261008-stdout.txt` | `9323489a990399d082cea77563242b3a3c8bef1e8b2cca3788a8f614d383c127` — matches, 6,924 B |
| `…/threshold-sensitivity-20261008-sens_out.txt` | `db246059ffbf1ea5670a8498761286b902e35c40ebc5efbb45045fad9d221b14` — matches, 6,923 B |

Existing artefacts inspected before any other step: `data/c8/reproducibility-verification/` (three preserved captures plus the run manifest) and `docs/reproducibility/` (the manifest, sensitivity and count/attribution verification reports). They proved sufficient, so the experiment was not rerun.

All output line numbers below refer to `data/c8/reproducibility-verification/threshold-sensitivity-20261008-stdout.txt`. Every cited figure also appears at the same position in the independent script-written `sens_out` capture.

---

## 3. Evidence table — four endpoints

| | **PRIMARY min** | **PRIMARY max** | **RESOLUTION min** | **RESOLUTION max** |
|---|---|---|---|---|
| **Reported** | 5.67% | 9.56% | 4.26% | 6.64% |
| **Configuration name** | combined-grid cell `R_C` = 19.9 × wave (1.0, 1.25) — "CANONICAL small vessel" wave pair | combined-grid cell `R_C` = 5.0 × wave (1.0, 1.9) — the script's `"Yaakob failure point as O_U"` | as PRIMARY min | as PRIMARY max |
| **Script invocation** | line 105 (`R_C` sweep) **and** line 134 (grid) — evaluated **twice** | line 134 (grid) **only** — evaluated **once** | lines 105, 134 | line 134 |
| **Environmental-data config** | PRIMARY — `raw_marine_era5_sea.csv` | PRIMARY | RESOLUTION — `raw_marine_mfwam.csv` | RESOLUTION |
| **Wave `O_C` / `O_U`** | 1.0 / **1.25** m | 1.0 / **1.90** m | 1.0 / 1.25 m | 1.0 / 1.90 m |
| **Rain `R_C` / `R_U`** | **19.9** / 20.0 mm/hr | **5.0** / 20.0 mm/hr | 19.9 / 20.0 | 5.0 / 20.0 |
| **Wind `W_C` / `W_U`** | 21.6 / 27.0 kn — canonical, never varied in the grid | 21.6 / 27.0 kn | 21.6 / 27.0 kn | 21.6 / 27.0 kn |
| **Denominator** | departure window 05:00–09:00, full record, **n = 9,135** | n = 9,135 | **n = 5,935** | n = 5,935 |
| **CAUTION hours *k*** | **518** | **873** | **253** | **394** |
| **Unrounded Δ<sub>L2</sub>** | **5.670498%** | **9.556650%** | **4.262848%** | **6.638585%** |
| **Displayed** | 5.67% | 9.56% | 4.26% | 6.64% |
| **Source-code lines** | `CANON` :19; `R_C` sweep :104–106; grid :128–139 | same | same | same |
| **Preserved output lines** | **:30** (`R_C= 19.9 -> Delta_L2 5.67%`), **:54** (grid row) | **:50** (grid row), **:56** (`grid max 9.56% at R_C=5.0, wave=(1.0,1.9)`) | **:86**, **:110** | **:106**, **:112** |
| **Envelope membership (item 5)** | **Qualified.** Clear of all three named disqualifiers; rainfall value researcher-defined | **Qualified.** Same | **Qualified.** Same | **Qualified.** Same |
| **Among the canonical 56? (item 6)** | **Yes** — tuple (21.6, 27.0, 19.9, 20.0, 1.0, 1.25), departure-window denominator | **Yes** — (21.6, 27.0, 5.0, 20.0, 1.0, 1.90) | **Yes** | **Yes** |
| **Unendorsed combination? (item 7)** | **Yes** — degenerate 0.1 mm/hr rainfall band, no source | **Yes** — sourced `O_U` joined to unsourced `R_C`; neither source speaks to the other's parameter | **Yes** | **Yes** |
| **Verdict** | **VERIFIED**, provenance qualified | **VERIFIED**, provenance qualified | **VERIFIED**, provenance qualified | **VERIFIED**, provenance qualified |

Nothing is marked UNVERIFIED. No threshold or count was invented.

---

## 4. How the integer counts were obtained

The script formats every percentage with `.2f`, so no integer count and no unrounded value appears in the preserved output for any sweep configuration. Both were **recovered exactly** by arithmetic on preserved values, not estimated.

One CAUTION hour is worth 100/9,135 = **0.01095** points in PRIMARY and 100/5,935 = **0.01685** points in RESOLUTION. The 2-decimal rounding interval is 0.01 points wide — narrower than both — so for each printed value **at most one** integer *k* can lie inside the interval. Uniqueness was asserted and confirmed for every value used below; had any value admitted two candidates, it would have been reported as such.

| Value | *n* | *k* | Exact Δ<sub>L2</sub> | Rounds to | Unique? |
|---|---|---|---|---|---|
| PRIMARY min 5.67% | 9,135 | 518 | 5.670498% | 5.67% | yes |
| PRIMARY max 9.56% | 9,135 | 873 | 9.556650% | 9.56% | yes |
| PRIMARY baseline 5.81% | 9,135 | 531 | 5.812808% | 5.81% | yes |
| PRIMARY `R_C`=5.0 only 6.15% | 9,135 | 562 | 6.152162% | 6.15% | yes |
| PRIMARY `O_U`=1.9 only 9.22% | 9,135 | 842 | 9.217296% | 9.22% | yes |
| RESOLUTION min 4.26% | 5,935 | 253 | 4.262848% | 4.26% | yes |
| RESOLUTION max 6.64% | 5,935 | 394 | 6.638585% | 6.64% | yes |
| RESOLUTION baseline 4.48% | 5,935 | 266 | 4.481887% | 4.48% | yes |
| RESOLUTION `R_C`=5.0 only 5.04% | 5,935 | 299 | 5.037911% | 5.04% | yes |
| RESOLUTION `O_U`=1.9 only 6.08% | 5,935 | 361 | 6.082561% | 6.08% | yes |

Full recovered grid, for completeness:

**PRIMARY** (*n* = 9,135), output lines :49–54

| `R_C` | wave (1.0, 1.25) | *k* | wave (1.0, 1.9) | *k* |
|---|---|---|---|---|
| 5.0 | 6.15% | 562 | **9.56% ← max** | **873** |
| 7.5 | 5.93% | 542 | 9.34% | 853 |
| 10.0 | 5.81% *(canonical)* | 531 | 9.22% | 842 |
| 15.0 | 5.70% | 521 | 9.11% | 832 |
| 19.9 | **5.67% ← min** | **518** | 9.07% | 829 |

**RESOLUTION** (*n* = 5,935), output lines :105–110

| `R_C` | wave (1.0, 1.25) | *k* | wave (1.0, 1.9) | *k* |
|---|---|---|---|---|
| 5.0 | 5.04% | 299 | **6.64% ← max** | **394** |
| 7.5 | 4.65% | 276 | 6.25% | 371 |
| 10.0 | 4.48% *(canonical)* | 266 | 6.08% | 361 |
| 15.0 | 4.31% | 256 | 5.91% | 351 |
| 19.9 | **4.26% ← min** | **253** | 5.86% | 348 |

---

## 5. Joint configurations verified directly, additivity tested separately

The instruction not to derive endpoints by adding individually reported sensitivity changes was observed. **The grid cells *are* the joint evaluations** — source line 134 builds `dict(CANON, R_C=rc, O_C=oc, O_U=ou)`, varying rainfall and wave together in a single classification pass — and the endpoint values were read straight from the grid rows at output lines :50 and :106. No additive reconstruction entered the verification.

Additivity was then tested as a **separate question**, and as it happens it holds exactly:

| | Baseline *k* | `R_C` → 5.0 alone | `O_U` → 1.9 alone | Additive prediction | **Actual joint *k*** | Result |
|---|---|---|---|---|---|---|
| PRIMARY | 531 | 562 (+31) | 842 (+311) | 531 + 31 + 311 = **873** | **873** | **holds exactly** |
| RESOLUTION | 266 | 299 (+33) | 361 (+95) | 266 + 33 + 95 = **394** | **394** | **holds exactly** |

This is a property of this record, not a guarantee. The two increments act on disjoint hour sets here — the rainfall increment adds hours crossing a lowered rainfall CAUTION onset, the wave increment reclassifies hours from UNSAFE down to CAUTION as the wave UNSAFE boundary rises — and had they overlapped, additivity would have failed. Reporting it is a finding; assuming it would have been an error.

---

## 6. What the minima actually are

PRIMARY *k* = **518** is exactly the canonical ocean-state binding count at output line :19. RESOLUTION *k* = **253** is its counterpart at line :75.

At `R_C` = 19.9 with `R_U` = 20.0 held fixed, the rainfall CAUTION band is **0.1 mm/hr wide** — rainfall must exceed 19.9 mm/hr without exceeding 20.0 and without a thunderstorm WMO code. The boundary-density block (lines :12, :68) records only 5 PRIMARY and 4 RESOLUTION departure-window hours anywhere within ±5 mm of the 20.0 boundary, and none falls in that 0.1 mm window. All 13 rainfall-attributed CAUTION hours therefore disappear:

- PRIMARY: 531 − 13 = **518** ✓
- RESOLUTION: 266 − 13 = **253** ✓

With `ties = 0` in both configurations (lines :22, :78), there is no double counting to complicate the subtraction.

**Both minima are "rainfall CAUTION effectively switched off" configurations** — ocean-state-only counts. The same report treats the analogous construct in the wave dimension as illegitimate: §K item 2 calls `O_C → O_U` (1.25 / 1.25) "**degenerate by construction** — a zero-width CAUTION band". The rainfall near-collapse at `R_C` → `R_U` is the same construct in a different dimension, and §C:55 names it as such ("19.9 is the degenerate case `R_C → R_U`"), yet §J admits it as an envelope endpoint.

---

## 7. Item-by-item findings

### Item 5 — does each endpoint belong to the sourced-threshold envelope?

Each endpoint is clear of all three disqualifiers named in the brief:

| Disqualifier | Present at any endpoint? | Evidence |
|---|---|---|
| Researcher-defined wave-onset perturbation | **No.** `O_C` = 1.0 in all four — the sourced Yaakob small-vessel onset. Neither (0.75, 1.25) "sens −0.25 on O_C" (:38, :94) nor (1.25, 1.5) "sens +0.25 on O_C" (:40, :96) appears | source :112–113 |
| Vessel-class variant | **No.** Neither (1.4, 2.8) "medium vessel" nor (1.5, 3.5) "big vessel" appears. The full grid minima — 1.11% PRIMARY (:55) and 0.15% RESOLUTION (:111) — are vessel-class cells and are correctly excluded from the envelope | source :114; §J:219–221 |
| Denominator-policy change | **No.** All four use the canonical departure window over the full record. Neither the daylight-only denominator (*n* = 5,536 / 3,594, lines :46, :102) nor the common-period restriction (:117–118) is involved | source :47, :119–121, :144–147 |

**But the contamination is in a fourth dimension the list does not name.** All four endpoints rest on a researcher-defined rainfall value, so membership is **qualified** rather than clean. The envelope excludes researcher-defined *wave* perturbations while admitting researcher-defined *rainfall* perturbations, and the label does not disclose the asymmetry.

### Item 6 — are these configurations among the canonical 56?

**Yes, all four.** The 26 unique threshold tuples enumerated from the script's configuration literals include both:

- `(21.6, 27.0, 19.9, 20.0, 1.0, 1.25)` — the minima
- `(21.6, 27.0, 5.0, 20.0, 1.0, 1.90)` — the maxima

Each appears for both environmental-data configurations under the departure-window denominator, accounting for 4 of the 56 distinct combinations. The minima occupy duplicate-invocation slots (evaluated twice per dataset — once in the `R_C` sweep, once in the grid, returning identical values both times); the maxima are evaluated once per dataset, in the grid only.

### Item 7 — do any endpoints combine threshold alternatives in ways the sources do not endorse?

**Yes — all four, for two distinct reasons.**

**The minima** set `R_C` = 19.9 mm/hr. No source specifies that value; §C:55 classifies it as a researcher-defined perturbation and names it the degenerate `R_C → R_U` case. The configuration is not a reading of any source — it is the near-removal of a rule.

**The maxima** join `O_U` = 1.90 m to `R_C` = 5.0 mm/hr. Taken separately:

- `O_U` = 1.90 m **is** sourced — §C:58 records it as "Yaakob NORDFORSK **failure point** as UNSAFE", an alternative reading of the same source that supplies the canonical 1.25 m, and the manuscript discloses the 1.875 → 1.90 m implementation rounding.
- `R_C` = 5.0 mm/hr **is not** sourced — §C:55.

Taken together, the joint configuration is endorsed by neither. Yaakob et al. (2015) is a vessel stability and seakeeping study; it is silent on rainfall. The JPS/DID Infobanjir rainfall classification is silent on wave height. Nothing in either source licenses the pairing, and the pairing is what produces the envelope ceiling.

The wind dimension raises no issue: `W_C` and `W_U` are held at their MET-sourced canonical values in every grid cell, and the one-at-a-time wind sweep is a structural zero across 18–25 kn (lines :32–36, :88–92).

---

## 8. Scientific assessment

> ## "Across externally sourced threshold configurations" — **REQUIRES QUALIFICATION**

Not fully supported. Not misleading either.

### Why it is not fully supported

The claim covers four configurations. In all four the dominant dimension — wave, which the project's own elasticity ranking (§J:229–232) puts first by a wide margin — is genuinely sourced. In all four the rainfall dimension is researcher-defined by the project's own classification, and in two of them it is a degenerate band collapse. A reviewer who reads §C and then §J of the paper's own evidence document finds the contradiction immediately, and §C:64's explicit promise makes it worse rather than better.

### Why it is not misleading

Restricting the envelope to genuinely sourced thresholds — `R_C` = 10.0, the only sourced value, with the canonical wave pair (1.0, 1.25) and the sourced alternative (1.0, 1.90) — gives:

| | Reported | **Strictly sourced** | Difference |
|---|---|---|---|
| PRIMARY | 5.67 – 9.56% | **5.81 – 9.22%** | floor 0.14 pts lower, ceiling 0.34 pts higher |
| RESOLUTION | 4.26 – 6.64% | **4.48 – 6.08%** | floor 0.22 pts lower, ceiling 0.56 pts higher |

Every claim the manuscript builds on the envelope survives the substitution:

- the envelope remains non-vacuous at both ends;
- the rate remains wave-dominated;
- the ceiling remains roughly 1.6× the canonical value (9.22 / 5.81 = 1.59);
- "the measured binding frequency is therefore not a threshold-invariant property of the site" (§V) remains true.

The reported envelope is **wider** than the defensible one at both ends in both configurations. The error therefore inflates apparent sensitivity rather than concealing it, which is why the verdict is qualification rather than misrepresentation. Adopting the strictly sourced envelope would make the paper's label exactly true **and** its central claim marginally stronger, since a tighter envelope that still spans a 1.6× range is a cleaner demonstration of conditionality than a wider one resting on a degenerate case.

---

## 9. Options for the author

**No edit was made to any manuscript, table, figure, script or data file.** Two routes are available.

### Option A — tighten the numbers *(recommended)*

Report **5.81–9.22%** (PRIMARY) and **4.48–6.08%** (RESOLUTION), and the existing label becomes exactly accurate.

- *Cost:* four numbers change — the §V sentence and the Table I "Sourced-threshold envelope" row.
- *Benefit:* both endpoints become the canonical configuration and a single sourced alternative reading of [17]. Both are already cited, both are already among the 56, both already carry machine evidence (output lines :5, :41, :61, :97). The §C/§J contradiction disappears, and no endpoint rests on a degenerate band.

### Option B — keep the numbers, fix the label

Replace "Across externally sourced threshold configurations" with wording that states what was varied, for example *"Across sourced wave thresholds combined with a rainfall-boundary sweep"*, and retitle the Table I row "Threshold-sensitivity envelope".

- *Cost:* one phrase and one row label.
- *Limitation:* stops the claim being wrong, but leaves the envelope floor resting on a rainfall band collapsed to 0.1 mm/hr — a construct §K:245 rejects when it occurs in the wave dimension.

### In either case

Reconcile §C:55 with §J:217 in `docs/analysis/threshold-sensitivity-analysis.md`. That document is the paper's own evidence trail, and it currently classifies the same two values both ways.

---

## 10. Verification summary

| | |
|---|---|
| Endpoints verified | **4 of 4** |
| Endpoints UNVERIFIED | **0** |
| Experiment rerun | **No** — existing preserved outputs were sufficient |
| Integer counts | Recovered exactly and uniquely from preserved values; none invented |
| Joint configurations | Read directly from the grid; additivity tested separately and found to hold |
| Configurations among the canonical 56 | 4 of 4 |
| Endpoints depending on a researcher-defined threshold | **4 of 4** (rainfall) |
| Endpoints depending on a researcher-defined wave perturbation | 0 |
| Endpoints depending on a vessel-class variant | 0 |
| Endpoints depending on a denominator-policy change | 0 |
| Assessment of "across externally sourced threshold configurations" | **REQUIRES QUALIFICATION** |
| Files edited | **none** |
| Envelope definition changed | **no** — the reported endpoints were verified against the definition as written, and the strictly sourced alternative is presented separately rather than substituted |
