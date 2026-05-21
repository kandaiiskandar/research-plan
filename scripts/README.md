# Data Collection Scripts

## kawasan_perairan_collector.py

Daily scraper for MET Malaysia Kawasan Perairan (Marine Waters Forecast) —
Western Sabah and Labuan coastal zone.

### What it does

1. Fetches the 7-day rolling marine forecast from `met.gov.my/forecast/marine/waters/`
2. Checks the official warning bulletin at `met.gov.my/data/IDM20016.html`
3. Extracts E vector components for the current day:
   - `w` — wind speed (km/h range → upper bound)
   - `o` — wave height (metre range → upper bound)
   - `r` — rainfall category (from weather condition text)
   - `m` — marine warning level (from official bulletin)
4. Applies `f(E)` — rule-based safety state classification (NOT ML)
5. Derives `G(S)` and `A_AI(S)` governance values
6. Assigns training label (`Go` / `Delay` / `AI_off`)
7. Appends one row to `data/kawasan_perairan_western_sabah.csv`

### Setup

```bash
pip install requests beautifulsoup4
```

### Run manually

```bash
python3 scripts/kawasan_perairan_collector.py
```

### Schedule daily (macOS launchd or Linux cron)

**cron** (runs at 06:05 MYT each morning):
```
5 6 * * * cd /path/to/research-test-2 && python3 scripts/kawasan_perairan_collector.py
```

**launchd plist** — create `~/Library/LaunchAgents/com.research.kawasan.plist`:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.research.kawasan</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>/path/to/research-test-2/scripts/kawasan_perairan_collector.py</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>6</integer>
        <key>Minute</key>
        <integer>5</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>/path/to/research-test-2/data/collector.log</string>
    <key>StandardErrorPath</key>
    <string>/path/to/research-test-2/data/collector.log</string>
</dict>
</plist>
```

Load with: `launchctl load ~/Library/LaunchAgents/com.research.kawasan.plist`

### Output schema

| Column | Type | Description |
|---|---|---|
| `date` | Date | Collection date (MYT) |
| `collection_time_myt` | HH:MM | Time of collection run |
| `w_kmh` | Numeric | Wind speed upper bound (km/h) |
| `w_knots` | Numeric | Wind speed upper bound (knots) |
| `o_m` | Numeric | Wave height upper bound (metres) |
| `r_cat` | Categorical | Rainfall: none / light / moderate / heavy / storm |
| `m_warning` | Categorical | Warning: none / cat1 / cat2_3 / ribut_petir / ribut_taufan |
| `v_vessel` | Categorical | Vessel: small / medium / big |
| `t_hour` | Numeric | Hour of collection (0–23) |
| `S` | Categorical | Safety state: SAFE / CAUTION / UNSAFE |
| `G_S` | Binary | AI gate: 1 = active, 0 = off |
| `A_AI_S` | Categorical | Admissible scope: full / restricted / none |
| `label` | Categorical | Training label: Go / Delay / AI_off |
| `condition_text_raw` | Text | Raw weather condition text from MET page |
| `notes` | Text | Manual annotation field |

### Classification thresholds (f(E))

Anchored to MET Malaysia published Kriteria Amaran:

| Variable | SAFE | CAUTION | UNSAFE |
|---|---|---|---|
| Wind (w) | < 22 kts | 22–27 kts | > 27 kts |
| Wave (o) | < 1.5 m | 1.5–3.5 m | > 3.5 m |
| Rainfall (r) | none / light | moderate / heavy | storm |
| Warning (m) | none | cat1 | cat2_3 / ribut_petir / ribut_taufan |

### Site structure note

MET Malaysia's Kawasan Perairan page may change layout over time. The scraper
uses three progressive fallback strategies:
1. Structured section tag for Western Sabah
2. Embedded JSON data blob
3. Regex over full page text

If the scraper stops producing data, check `data/collector.log` and inspect
the current page structure at `met.gov.my/forecast/marine/waters/`.

### Data volume

One row per day. Minimum useful collection period for RQ4 coverage: 12 months
(captures both Southwest Monsoon May–Sep and Northeast Monsoon Nov–Mar, giving
natural SAFE/CAUTION/UNSAFE distribution without synthetic augmentation).
