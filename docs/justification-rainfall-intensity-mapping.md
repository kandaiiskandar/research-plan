# Justification: Rainfall intensity mapping from ERA5 mm/hr to ordinal categorical r

**Decision:** The rainfall variable `r` in the environmental input vector E = {w, r, m, o, v, t} is defined as an ordinal categorical variable with five levels: {none, light, moderate, heavy, storm}. ERA5 historical precipitation data (mm/hr) is mapped to these levels using the official rainfall intensity thresholds published by the Department of Irrigation and Drainage Malaysia (JPS/DID) and operationalised through the national flood monitoring system Infobanjir. MET Malaysia qualitative forecasts (e.g., "Ribut petir", "Hujan lebat") are mapped to the same scale using direct terminological correspondence.

---

## 1. The canonical threshold table

| `r` value | ERA5 precipitation (mm/hr) | MET Malaysia / Kawasan Perairan term |
|---|---|---|
| `none` | 0.0 | Tiada hujan |
| `light` | 0.1 – 10.0 | Hujan ringan |
| `moderate` | 10.1 – 30.0 | Hujan / Hujan di beberapa tempat |
| `heavy` | 30.1 – 60.0 | Hujan lebat |
| `storm` | > 60.0 | Ribut petir / Hujan lebat dan ribut petir |

**Source:** JPS/DID Malaysia via Infobanjir (publicinfobanjir.water.gov.my) — the official national flood and rainfall monitoring system of the Department of Irrigation and Drainage Malaysia. Infobanjir classifies hourly rainfall gauges in real time using these thresholds and applies them consistently across all monitoring stations in Malaysia including Sabah.

**Secondary reference:** JPS Hydrological Procedure No. 1 (HP1, revised 2015) — the primary design rainstorm estimation procedure for Malaysia, published by JPS/DID. HP1 is the upstream authority from which Infobanjir's operational thresholds derive.

---

## 2. Why these thresholds and not alternatives

Three alternative threshold systems were considered:

**WMO international standard:** Light < 2.5 mm/hr, moderate 2.5–10 mm/hr, heavy > 10 mm/hr. These are designed for temperate regions and significantly underrepresent the intensity of tropical rainfall in Malaysia. The 99th percentile hourly ERA5 value for Kota Kinabalu (2020–2024) is 9.5 mm/hr — under WMO's threshold, this would be classified as `moderate`, despite representing an extreme event for the region. WMO thresholds are not appropriate for a Malaysia-specific study.

**MET Malaysia mm/day classification:** MET Malaysia also publishes a daily classification — slight (< 10 mm/day), moderate (10–60 mm/day), heavy (60–150 mm/day), extreme (> 150 mm/day). These are cumulative daily totals, not hourly rates, and cannot be directly applied to hourly ERA5 data without an hourly disaggregation assumption. The JPS/DID hourly thresholds (Infobanjir) are the correct authority for hourly classifications.

**Custom thresholds calibrated from ERA5 data alone:** Deriving thresholds from the ERA5 distribution for KK without reference to an official source would introduce arbitrariness that cannot be defended in the thesis. The Safety Classifier f(E) must apply thresholds that are independently grounded and that correspond to thresholds used by Malaysian maritime and weather authorities.

The JPS/DID Infobanjir classification is chosen because: (1) it is the authoritative operational standard for hourly rainfall intensity in Malaysia; (2) it aligns with the qualitative terminology used by MET Malaysia in Kawasan Perairan forecasts; (3) it is applied in Sabah; and (4) it is publicly documented.

---

## 3. Correspondence with Kawasan Perairan forecast language

MET Malaysia's Kawasan Perairan bulletins describe rainfall qualitatively (e.g., "Ribut petir di beberapa tempat", "Hujan di beberapa tempat", "Tiada hujan") without publishing numerical thresholds. The following mappings are used to convert live Kawasan Perairan text to `r` values at inference time:

| Kawasan Perairan text | `r` value |
|---|---|
| Tiada hujan | `none` |
| Hujan ringan / Beberapa tempat hujan | `light` |
| Hujan / Hujan di beberapa tempat | `moderate` |
| Hujan lebat / Hujan lebat di beberapa tempat | `heavy` |
| Ribut petir / Hujan lebat dan ribut petir | `storm` |

This mapping is one-to-one with the JPS/DID intensity categories. The Kawasan Perairan text is a qualitative forecast; ERA5 mm/hr is a historical reanalysis measurement. Both are mapped to the same ordinal categorical scale to ensure that `r` has a consistent domain across training data (ERA5) and live inference (Kawasan Perairan).

---

## 4. ERA5 data characteristics for Kota Kinabalu (2020–2024)

The ERA5 historical precipitation data downloaded for KK (5.98°N, 116.01°E) has the following distribution over 43,848 hourly records:

| Metric | Value |
|---|---|
| Non-zero hours | 15,377 (35.1%) |
| 50th percentile (non-zero) | 0.30 mm/hr |
| 75th percentile (non-zero) | 0.90 mm/hr |
| 90th percentile (non-zero) | 2.60 mm/hr |
| 95th percentile (non-zero) | 4.40 mm/hr |
| 99th percentile (non-zero) | 9.50 mm/hr |
| Maximum | 39.20 mm/hr |

Under the JPS/DID mapping, the ERA5 record contains hours in `none`, `light`, `moderate`, and `heavy` categories. No `storm` hours (> 60 mm/hr) appear in the ERA5 record. This is consistent with the known limitation of ERA5: the reanalysis systematically underestimates peak convective rainfall intensity in tropical coastal areas because its spatial grid (approximately 31 km resolution) cannot resolve sub-grid convective cells. ERA5 precipitation values should be understood as area-averaged estimates rather than point measurements. The `storm` category remains valid in the architecture — it applies in live inference when Kawasan Perairan text indicates "Ribut petir" — but it is underrepresented in the ERA5 training data.

This limitation does not affect the architecture's formal properties. The Safety Dominance Property (AI(E) ⊆ A_AI(S)) holds regardless of the empirical distribution of `r` values in training data. The underrepresentation of `storm` in ERA5 is noted as a data limitation relevant to empirical classifier training, not to the formal design.

---

## 5. File produced

`data/raw_rainfall.csv` — ERA5 hourly precipitation downloaded from Open-Meteo Historical Weather API (ERA5 reanalysis), covering 2020-01-01 to 2024-12-31 for coordinates 5.98°N, 116.01°E. Columns: `time`, `precipitation (mm)`, `rain (mm)`.

The `precipitation` column (total precipitation including all forms) is used for `r` mapping. The `rain` column (liquid rain only, excluding snow) is equivalent at tropical sea-level coordinates.

Script: `scripts/openmeteo_raw_rainfall.py`

---

## 6. Sources

- JPS/DID Malaysia — [Infobanjir Rainfall Data](https://publicinfobanjir.water.gov.my/hujan/data-hujan/?lang=en)
- JPS Hydrological Procedure No. 1 (HP1, Revised 2015) — [http://h2o.water.gov.my/man_hp1/HP1_2015.pdf](http://h2o.water.gov.my/man_hp1/HP1_2015.pdf)
- Open-Meteo Historical Weather API (ERA5) — [https://archive-api.open-meteo.com/v1/archive](https://archive-api.open-meteo.com/v1/archive)
- MET Malaysia Kawasan Perairan — [https://www.met.gov.my/kawasan-perairan](https://www.met.gov.my/kawasan-perairan)
