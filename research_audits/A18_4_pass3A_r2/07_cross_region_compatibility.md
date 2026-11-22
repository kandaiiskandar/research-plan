# 07 — Cross-Region Compatibility

**A18.4 Pass 3A · 22 November 2026**

Assessed against the M1d-Q v2.5 scope: eligible small-scale coastal fisheries in Malaysia **or
comparable international regions**. Sabah is optional. Under-10-GRT is a **legacy experimental subgroup,
not a universal cutoff and not a certified safety threshold.** `PRE_DEPARTURE` remains the initial
decision phase.

**Standing constraint on everything below.** No dataset was acquired, so every judgement here is about
the product **as the provider describes it**, tier `DOCUMENTED_ONLY`. None is a measurement.

## 1. Dimension-by-dimension

| Dimension | Assessment | Tier |
|---|---|---|
| **Geographic / coastal resolution** | 0.2° ≈ 22 km at the equator. For a global reanalysis that is coarse for **coastal** small-scale fisheries, whose operating waters are often narrower than one cell. A18.1 already demonstrated the consequence: one requested point returned three different cells, separated by 2.73–7.20 km, and that separation turned out to be a confound (Step 2 D-12). At 0.2° the problem is larger, not smaller. | DOCUMENTED_ONLY |
| **Physical variables** | Rich on the wave side — total, swell and wind-wave heights, several period definitions, directions, Stokes drift. **No wind, no precipitation.** The A18.1 classifier needs `g_w` (wind) and `g_r` (rain), so this product alone cannot drive it. | DOCUMENTED_ONLY |
| **Bathymetry / tide / coastal exposure** | Bathymetry is available as a static dataset (`...static...bathy`). **No tide.** The repository holds `raw_tide_marea.csv`, which Step 2 found is read by no canonical script and has no declared timezone or coordinates. Tide remains outside the contract. | DOCUMENTED_ONLY |
| **Vessel length, GT/GRT, equipment, loading** | **Not present and not inferable.** No vessel attribute exists in any environmental product. This is not a gap this track can close. | NOT AVAILABLE |
| **Decision stage and trip route** | **Not present.** A grid-hour is not a trip. The A18.2 unit was explicitly "one eligible historical grid-hour — not a trip, not a vessel, not a person." Nothing here changes that. | NOT AVAILABLE |
| **Issued-source availability at decision time** | **Not satisfiable by this product at all.** It is a reanalysis: produced after the fact, from assimilated observations. `decision_time_availability` stays UNKNOWN (D-08). | STRUCTURAL |
| **Local warning definitions** | **Not present.** MET Malaysia thresholds (used in A18.1 for `g_w` and `g_r`) are national criteria, unrelated to this product. A document describing warning thresholds is **not an issued warning**, a distinction the task states and this assessment keeps. | NOT AVAILABLE |
| **Unit conversions and uncertainty** | Cannot be assessed: the pages state **no units**. The product does assimilate significant wave height, so SWH is observation-constrained while derived periods and directions are more model-dependent — but no uncertainty field is listed. | UNKNOWN |
| **Sampling bias** | A global model on a regular grid has no catch-dependent or reporting bias, which is a genuine advantage over fisher-reported data. It carries model bias instead, which is not quantified on the pages. | DOCUMENTED_ONLY |
| **Public access and reuse rights** | Favourable: worldwide, non-exclusive, royalty-free, perpetual, free of charge, with attribution and a DOI citation required. Users must keep usage records (s2.6) and the licence is revisable at any time (s8.1). | DOCUMENTED_ONLY |
| **Local action catalogue applicability** | **No mapping exists.** The conference vocabulary is `{Go, Delay, DepartureTime, Duration}`; the later fisheries catalogue is A1/A2/A3. A18.2 established there is no protective-action truth for any of the four types. An environmental product cannot supply one. | NOT AVAILABLE |

## 2. What this product could legitimately support

**One thing, and it is worth having.** A **resolution and co-location sensitivity check** on the A18.1
replay. Step 2 finding D-12 showed PRIMARY vs RESOLUTION changes the wave product *and* the wind–wave
separation together, and Step 4 measured the two effects at +1.97 pp and −0.64 pp. A third independent
wave source at a third resolution would add a point to that comparison.

Its value is bounded and should be stated as such: still R0, still hindsight, still no safe/unsafe
label, and it **cannot** separate the resolution factor from the co-location factor, because that needs
a wind field co-located with each wave cell and this product has no wind at all.

## 3. Explicit non-merges

Recording what must **not** be done, since the task requires it:

1. **Do not substitute a Copernicus wave variable for an A18.1 `wave_height (m)` value** without mapping
   by `standard_name` and `units`. Several candidate definitions exist and they are not interchangeable
   (`P3A-06`).
2. **Do not combine this wave product with A18.1 wind or precipitation** without recording that they
   come from different providers, grids, and processing chains — which is the same co-location problem
   D-12 already identified, in a worse form.
3. **Do not generalise any vessel-safety threshold across locations.** The 1.0 m / 1.25 m band is a
   researcher transfer from vessel **length** to **tonnage** (A18.1 Step 3 A-03), not certified, and
   derived from Peninsular Malaysia and Korean sources. It does not transfer to another coast by virtue
   of a dataset being global.
4. **Do not treat reanalysis as an issued product.** They are distinct evidence sources with distinct
   estimands, as are vessel tracks, fisher decision records, domain surveys and expert judgments.

## 4. Scope note on the v2.5 amendment

The amendment widens eligibility beyond Sabah, which genuinely helps **Track A**: a global product makes
the region a free choice, and `reproduce_acquisition.py` takes the bounding box as a parameter.

It does **not** help Track B in the same way. Issued marine warnings are produced by **national** meteorological
services under national thresholds and formats, so widening the geography changes *which* authority's
archive is needed rather than removing the need for one. The NOAA/NCEI route is the most open of the
candidates for precisely this reason, and it covers US waters — so an issued-source acquisition would
likely come from a **different region** than any Malaysian environmental subset. That mismatch is
acceptable for an R1-SOURCE-ONLY demonstration of provenance mechanics, and **disqualifying** for
R1-PAIRED, which needs source, vessel, geography and time to coincide.
