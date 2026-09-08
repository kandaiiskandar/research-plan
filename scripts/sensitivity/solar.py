"""NOAA solar position algorithm — sunrise, sunset, civil dawn, civil dusk.

Reproducible, dependency-free, no network. Used ONLY by the g_t counterfactual
sensitivity analysis. NOT part of the canonical model.

Reference: NOAA Global Monitoring Laboratory solar calculator equations
(Astronomical Almanac low-precision formulae). Accuracy ~1 min for
|latitude| < 72 deg, which is ample at 5.98 N.

Convention: longitude positive EAST. Returns local clock hours (float).
"""
import numpy as np

ZENITH_SUNRISE = 90.833   # deg — includes refraction + solar semi-diameter
ZENITH_CIVIL   = 96.0     # deg — civil twilight, sun 6 deg below horizon


def _events(doy, lat, lon, tz, zenith):
    g = 2*np.pi/365.0 * (doy - 1)
    eq = 229.18*(0.000075 + 0.001868*np.cos(g) - 0.032077*np.sin(g)
                 - 0.014615*np.cos(2*g) - 0.040849*np.sin(2*g))
    dec = (0.006918 - 0.399912*np.cos(g) + 0.070257*np.sin(g)
           - 0.006758*np.cos(2*g) + 0.000907*np.sin(2*g)
           - 0.002697*np.cos(3*g) + 0.00148*np.sin(3*g))
    la = np.radians(lat)
    c = (np.cos(np.radians(zenith))/(np.cos(la)*np.cos(dec)) - np.tan(la)*np.tan(dec))
    c = np.clip(c, -1.0, 1.0)
    ha = np.degrees(np.arccos(c))
    rise_utc_min = 720 + 4*(-lon - ha) - eq
    set_utc_min  = 720 + 4*(-lon + ha) - eq
    return rise_utc_min/60.0 + tz, set_utc_min/60.0 + tz


def solar_table(dates, lat=5.98, lon=116.07, tz=8):
    """dates: array of datetime64. Returns dict of local-hour arrays."""
    doy = np.array([d.timetuple().tm_yday for d in dates], dtype=float)
    sr, ss = _events(doy, lat, lon, tz, ZENITH_SUNRISE)
    cd, ck = _events(doy, lat, lon, tz, ZENITH_CIVIL)
    return {"sunrise": sr, "sunset": ss, "civil_dawn": cd, "civil_dusk": ck}
