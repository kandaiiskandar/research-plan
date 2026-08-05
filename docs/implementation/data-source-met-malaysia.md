# Data Source: MET Malaysia — Environmental Variables for f(E)

**Document type**: Data acquisition and variable mapping note  
**For**: Chapter 3 (Architecture Design) — prototype implementation (RQ3) and evaluation dataset (RQ4)  
**Prepared**: May 2026  
**Study site**: Kota Kinabalu, Sabah — Western Sabah and Labuan coastal waters

---

## 1. Overview of MET Malaysia as a Data Source

Jabatan Meteorologi Malaysia (MET Malaysia) is the primary institutional source for environmental data required by the classification function **S = f(E)**. MET Malaysia publishes marine forecast data specifically for the **Western Sabah and Labuan** coastal zone — the waters directly relevant to the Kota Kinabalu study site.

MET Malaysia operates two relevant data channels:

| Channel | URL | Type | Use |
|---|---|---|---|
| **Kawasan Perairan** (Marine Waters Forecast) | `met.gov.my/forecast/marine/waters` | 7-day rolling forecast | Primary data source for prototype and evaluation |
| **myMETdata** | `mymetdata.met.gov.my` | Historical paid data | Supplementary historical wind and rainfall |
| **MET API** | `api.met.gov.my` | Free JSON API | Programmatic access to forecast data |
| **Warning bulletins** | `met.gov.my/data/IDM20016.html` | Live official warnings | Marine warning level (m) ground truth |

The primary focus for this research is **Kawasan Perairan** — the marine waters forecast page for Western Sabah and Labuan, which provides all four MET-sourced E vector variables in a single structured feed.

---

## 2. Variable Mapping: E Vector to MET Data Fields

The environmental state vector **E = {w, r, m, o, v, t}** maps to MET Malaysia data fields as follows:

### 2.1 Direct Variables from Kawasan Perairan

| E symbol | Variable | MET field (Malay) | MET field (English) | Format | Example |
|---|---|---|---|---|---|
| **w** | Wind speed | Kelajuan Angin | Wind speed | Range in km/h | 10–20 km/h, 20–30 km/h, 40–50 km/h |
| **o** | Wave height | Ketinggian Ombak | Wave height | Range in metres | 0.5–1.0 m, 1.0–1.5 m, 3.0–3.5 m |
| **r** | Rainfall intensity | Cuaca / Pagi / Petang / Malam | Weather / AM / PM / Night | Categorical text | Tiada hujan, Hujan, Ribut petir |

These three variables are directly readable from the Kawasan Perairan page for Western Sabah and Labuan.

### 2.2 Derived Variable

| E symbol | Variable | Derivation method |
|---|---|---|
| **m** | Marine warning level | Inferred from weather condition text (Ribut petir → warning-level event) and cross-referenced with the official warning bulletin at `IDM20016.html`. Formal Category 1/2/3 warnings for Sabah Barat are issued separately from the forecast page. |

The **m** variable is not explicitly present as a categorical field in the Kawasan Perairan forecast. It is derived by:
1. Checking the official warning bulletin for Western Sabah (Sabah Barat dan Labuan)
2. Mapping the weather condition text to the warning tier: "Ribut petir" corresponds to a Ribut Petir warning (>20 mm/hr rainfall trigger); wind speeds ≥40 km/h in the forecast correspond to Category 1 (Angin Kencang Kategori Pertama) conditions

### 2.3 Non-MET Variables

| E symbol | Variable | Source |
|---|---|---|
| **v** | Vessel category | Study participant data — fixed attribute of each fisher's vessel (small/medium/big) |
| **t** | Time of day | System clock — derived from the timestamp of the departure decision query |

---

## 3. Data Fields Observed — Kawasan Perairan, Western Sabah

The Kawasan Perairan page for Western Sabah and Labuan provides the following structured forecast per day:

```
Date / Day
Weather condition (daily summary icon + text)
  Morning (Pagi):   [condition text]
  Afternoon (Petang): [condition text]
  Evening (Malam):  [condition text]
Wind direction (Arah Angin): [compass code]
Wind speed (Kelajuan Angin): [range] km/h
Wave height (Ketinggian Ombak): [range] m
```

**Wind speed range bands observed for Western Sabah:**

| Band | km/h | Approximate knots | Typical condition |
|---|---|---|---|
| Band 1 | 10–20 | 5–11 | Calm — normal fishing conditions |
| Band 2 | 20–30 | 11–16 | Light wind — generally safe |
| Band 3 | 30–40 | 16–22 | Moderate — approaching CAUTION threshold |
| Band 4 | 40–50 | 22–27 | Strong — Category 1 warning zone (UNSAFE for small vessels) |
| Band 5 | >50 | >27 | Category 2/3 — UNSAFE for all fishing |

**Wave height range bands observed:**

| Band | Metres | Typical condition |
|---|---|---|
| Band 1 | 0.5–1.0 | Calm — full advisory scope |
| Band 2 | 1.0–1.5 | Slight — full to restricted scope transition |
| Band 3 | 1.5–2.5 | Moderate — CAUTION zone |
| Band 4 | 3.0–3.5 | Rough — approaching Category 1 UNSAFE threshold |
| Band 5 | >3.5 | Very rough — Category 1+ UNSAFE |

**Value interpretation rule**: For classification purposes, the **upper bound** of each range is used. This is consistent with the worst-case (max-severity) aggregation principle of the architecture — if conditions are anywhere in the 40–50 km/h band, the system treats wind as 50 km/h (the most adverse plausible reading).

---

## 4. Safety State Thresholds Anchored to MET Malaysia Criteria

The UNSAFE boundary for w and o is anchored to MET Malaysia's published **Kriteria Amaran Angin Kencang dan Laut Bergelora**. The CAUTION boundary sits below the formal warning threshold, in the pre-warning elevated zone.

| Parameter | SAFE | CAUTION | UNSAFE | MET authority basis |
|---|---|---|---|---|
| **Wind speed (w)** | < 22 knots (< 40 km/h) | 22–27 knots (40–50 km/h) | > 27 knots (> 50 km/h) | Category 1 onset: 40 km/h; Category 2 onset: 50 km/h |
| **Wave height (o)** | < 1.5 m | 1.5–3.5 m | > 3.5 m | Category 1 wave threshold: 3.5 m (dangerous to small craft) |
| **Rainfall (r)** | None/light (< 5 mm/hr) | Moderate (5–20 mm/hr) | Heavy/storm (> 20 mm/hr) | Ribut Petir warning threshold: > 20 mm/hr |
| **Marine warnings (m)** | None | Category 1 (Angin Kencang Kategori Pertama) | Category 2/3, Ribut Petir, or Ribut Taufan |  MET Malaysia three-tier warning system |
| **Vessel category (v)** | Medium / big | Small (≤ 22 ft / < 40 GRT) | — | Small craft = primary risk group in Category 1 criteria |
| **Time of day (t)** | 06:00–17:00 | 17:00–19:00 | 19:00–06:00 | Empirical basis: Atacan & Düzbastılar (2023) night navigation risk |

**MET Malaysia warning category summary (for reference):**

| Category | Wind | Wave | Danger to |
|---|---|---|---|
| Category 1 (Kategori Pertama) | 40–50 km/h | ≤ 3.5 m | Small craft, recreational, water sports |
| Category 2 (Kategori Kedua) | 50–60 km/h | ≤ 4.5 m | All fishing, ferry, coastal activities |
| Category 3 (Kategori Ketiga) | > 60 km/h | > 4.5 m | All vessels, oil platforms |
| Ribut Petir | — | — | Triggered at rainfall > 20 mm/hr |
| Ribut Taufan | — | — | Tropical cyclone advisory (lat 0–20°N, lon 95–130°E) |

---

## 5. Data Acquisition Plan

### 5.1 Primary Source: Kawasan Perairan (Prospective Collection)

**URL**: `https://www.met.gov.my/forecast/marine/waters/`  
**Location**: Western Sabah and Labuan  
**Granularity**: Daily forecast (morning / afternoon / evening conditions)  
**Coverage**: Wind speed, wave height, weather condition (3 of 4 MET variables)  
**Cost**: Free

Since the Kawasan Perairan page only displays the current 7-day forecast with no historical archive, data must be collected **prospectively** via a daily scraper or API call. A scraper records each day's forecast row at a fixed time each morning (e.g., 06:00 MYT), building up the dataset day by day.

**Minimum collection period for RQ4**: Sufficient scenario coverage across all three safety states. Western Sabah experiences varied conditions across the inter-monsoon and monsoon periods — a full year captures both the Southwest Monsoon (May–September, generally milder) and Northeast Monsoon (November–March, higher wind and wave activity), providing natural coverage of SAFE, CAUTION, and UNSAFE conditions.

### 5.2 Marine Warning Level (m): Official Bulletin

**URL**: `https://www.met.gov.my/data/IDM20016.html`  
**Update frequency**: Issued as needed by the National Weather and Earthquake Operations Centre  
**Zone**: Sabah Barat dan Labuan (Western Sabah and Labuan)

The official warning bulletin is checked alongside the forecast. If an active warning for Sabah Barat is present, the **m** value is set to the appropriate category. If no warning is active, **m = None**.

### 5.3 Supplementary: myMETdata (Historical, If Required)

**URL**: `https://mymetdata.met.gov.my`  
**Products**: Hourly Surface Wind (RM20/CSV), Hourly Rainfall (RM20/CSV)  
**Station**: Kota Kinabalu (WMKK)  
**Use case**: Retrospective threshold calibration or validation against observed station data

This is a paid service. It provides CSV-format historical data for wind and rainfall at the KK station, which can supplement or validate the forecast-based dataset if needed. Wave height from myMETdata is PDF-only (Marine Parameter Data, RM20) and requires parsing effort.

### 5.4 Evaluation Scenario Construction (RQ4)

For the three-condition comparative evaluation (C1: ungated, C2: binary-gated, C3: two-level graduated), test scenarios are constructed from the Kawasan Perairan range vocabulary to ensure coverage of all three safety states:

| Scenario type | w | o | r | m | Expected S |
|---|---|---|---|---|---|
| SAFE | 10–20 km/h | 0.5–1.0 m | Tiada hujan (no rain) | None | SAFE |
| SAFE (borderline) | 30–40 km/h | 1.0–1.5 m | Hujan ringan (light rain) | None | SAFE |
| CAUTION | 30–40 km/h | 1.5–2.5 m | Hujan (rain) | None | CAUTION |
| CAUTION (near-UNSAFE) | 40–50 km/h | 2.5–3.0 m | Ribut petir (thunderstorm) | Category 1 | CAUTION |
| UNSAFE | 40–50 km/h | 3.0–3.5 m | Ribut petir | Category 1 | UNSAFE |
| UNSAFE (severe) | > 50 km/h | > 3.5 m | Ribut petir | Category 2/3 | UNSAFE |

All scenario values are drawn directly from MET Malaysia's published range bands and warning criteria — they are grounded in the official data vocabulary, not synthetic.

---

## 6. Summary

MET Malaysia's **Kawasan Perairan** page for Western Sabah and Labuan is the primary data source for this research. It directly provides three of the four MET-sourced E vector components (w, o, r) and allows derivation of the fourth (m) via the official warning bulletin. The UNSAFE classification thresholds are anchored to MET Malaysia's published Kriteria Amaran, providing institutional authority for the boundary values.

The main constraint is the absence of a historical archive — data must be collected prospectively, or supplemented with myMETdata historical records and constructed evaluation scenarios grounded in MET's range vocabulary.

| Variable | Source | Status |
|---|---|---|
| w (wind speed) | Kawasan Perairan — Kelajuan Angin | ✅ Direct |
| r (rainfall) | Kawasan Perairan — Cuaca / weather text | ✅ Direct (categorical) |
| o (wave height) | Kawasan Perairan — Ketinggian Ombak | ✅ Direct |
| m (marine warning) | Official bulletin IDM20016.html | ✅ Derived / cross-referenced |
| v (vessel category) | Study participants | ✅ From fieldwork |
| t (time of day) | System clock | ✅ Deterministic |
