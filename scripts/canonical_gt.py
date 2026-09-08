#!/usr/bin/env python3
"""CANONICAL g_t — solar-event two-state time classifier.

SDR-001 APPLIED 2026-09-08. This module is the SINGLE canonical implementation
of g_t. Every canonical analysis script imports it. No script computes
sunrise/sunset independently, and no script embeds solar astronomy.

    g_t : (X_t x Date) u {bottom} -> {SAFE, UNSAFE}

        SAFE    sunrise(date) <= t < sunset(date)
        UNSAFE  t < sunrise(date)  or  t >= sunset(date)
        UNSAFE  bottom  -- missing/invalid clock, date or solar lookup

Half-open by construction: **exact sunrise is SAFE, exact sunset is UNSAFE**.
g_t emits NO CAUTION. Im(g_t) = {SAFE, UNSAFE}; CAUTION is not in the image, by
deliberate design (Appendix C C.2, "Component classifiers are not required to
be surjective"). The architecture remains three-state -- CAUTION is reached
through g_o and g_r.

SUPERSEDED 2026-09-08 by SDR-001: the incumbent fixed-clock classifier
    SAFE 06:00 <= t < 17:00 | CAUTION 17:00 <= t < 19:00 | UNSAFE otherwise
Its boundaries had no located source. Retained in `g_t_incumbent_superseded`
for historical reproduction ONLY -- never for current results.

DEPENDENCY (canonical)
----------------------
    stored solar artefact  ->  g_t  ->  f

    data/solar/solar-events-daily.csv   (C-3 frozen artefact)
    specification  solar-spec-v1
    implementation solar-v1  sha256 3b7dc371ebe5931b...c36c
    location       5.98 N, 116.01 E   UTC+8, no DST

Classification consumes `sunrise_hours` / `sunset_hours` (float, 6 dp), NEVER
the HH:MM:SS display columns -- comparing against a rounded rendering would
reintroduce error exactly at the boundary that matters.

EVIDENCE / POLICY SEPARATION (do not collapse these)
----------------------------------------------------
Evidence: night navigation carries ELEVATED operational risk (Atacan &
Duzbastilar 2023); COLREGs Rule 20(b) defines sunset-to-sunrise as the
navigation-LIGHT boundary; no source supports 06:00/17:00/19:00; no source
supports a twilight CAUTION band.
Policy: `night => g_t = UNSAFE => AI advisory unavailable` is a conservative
ARCHITECTURAL GOVERNANCE CHOICE. No source establishes it. COLREGs does not
require AI abstention, and nothing here asserts that night operation is
prohibited or physically unsafe. Human decision authority is unconditional.
"""

from pathlib import Path

import numpy as np
import pandas as pd

SAFE, CAUTION, UNSAFE = 0, 1, 2

ROOT = Path(__file__).resolve().parent.parent
SOLAR_ARTEFACT = ROOT / "data" / "solar" / "solar-events-daily.csv"

SOLAR_SPEC_VERSION = "solar-spec-v1"
SOLAR_IMPL_VERSION = "solar-v1"
CANONICAL_LAT, CANONICAL_LON, CANONICAL_TZ = 5.98, 116.01, 8

_CACHE = None


def _load():
    global _CACHE
    if _CACHE is None:
        s = pd.read_csv(SOLAR_ARTEFACT)
        s["date"] = pd.to_datetime(s["date"]).dt.date
        _CACHE = (dict(zip(s["date"], s["sunrise_hours"].astype(float))),
                  dict(zip(s["date"], s["sunset_hours"].astype(float))))
    return _CACHE


def solar_artefact_sha256():
    import hashlib
    return hashlib.sha256(SOLAR_ARTEFACT.read_bytes()).hexdigest()


def g_t(times, hours=None):
    """Canonical g_t over a pandas datetime Series (or array of Timestamps).

    `hours` may supply the hour-of-day explicitly; otherwise it is taken from
    `times`. Returns an int array of SAFE/UNSAFE. Never returns CAUTION.
    Any row whose date is absent from the artefact, or whose clock value is
    not finite, resolves to UNSAFE -- the g_t(bottom) = UNSAFE fail-safe of
    Corollary C.1b.1.
    """
    sr, ss = _load()
    t = pd.to_datetime(pd.Series(times).reset_index(drop=True))
    h = (t.dt.hour.to_numpy(dtype=float) if hours is None
         else np.asarray(hours, dtype=float))
    dates = t.dt.date.to_numpy()

    out = np.full(len(t), UNSAFE, dtype=int)          # fail-safe default
    for i in range(len(t)):
        hi = h[i]
        if not np.isfinite(hi):
            continue                                   # bottom -> UNSAFE
        a, b = sr.get(dates[i]), ss.get(dates[i])
        if a is None or b is None:
            continue                                   # bottom -> UNSAFE
        out[i] = SAFE if (a <= hi < b) else UNSAFE     # half-open
    return out


def is_daylight(times, hours=None):
    """Canonical ASTRONOMICAL daylight: sunrise(date) <= t < sunset(date).

    This replaces the superseded fixed 06:00-17:00 window. 'Daylight' in all
    current canonical analysis means this, and nothing else.
    """
    return g_t(times, hours) == SAFE


def g_t_incumbent_superseded(hours):
    """SUPERSEDED fixed-clock g_t. Historical reproduction ONLY.

    Superseded by SDR-001 on 2026-09-08. Do NOT use for current results.
    Retained so that pre-migration findings remain reproducible.
    """
    h = np.asarray(hours)
    return np.where((h >= 6) & (h < 17), SAFE,
                    np.where((h >= 17) & (h < 19), CAUTION, UNSAFE))


def provenance():
    return {
        "classifier": "Model B solar-event two-state (SDR-001, applied 2026-09-08)",
        "image": "{SAFE, UNSAFE} -- CAUTION not in image, by design",
        "boundary_rule": "half-open: sunrise <= t < sunset",
        "fail_safe": "g_t(bottom) = UNSAFE",
        "solar_artefact": str(SOLAR_ARTEFACT.relative_to(ROOT)),
        "solar_artefact_sha256": solar_artefact_sha256(),
        "solar_spec": SOLAR_SPEC_VERSION,
        "solar_impl": SOLAR_IMPL_VERSION,
        "location": f"{CANONICAL_LAT} N, {CANONICAL_LON} E, UTC+{CANONICAL_TZ}",
        "superseded": ("fixed clock 06:00/17:00/19:00 -- no located source; "
                       "superseded by SDR-001 on 2026-09-08"),
    }


if __name__ == "__main__":
    import json
    print(json.dumps(provenance(), indent=2))
