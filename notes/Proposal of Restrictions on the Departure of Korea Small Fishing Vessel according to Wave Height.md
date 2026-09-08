# Proposal of Restrictions on the Departure of Korea Small Fishing Vessel according to Wave Height

**Citation:** Jeong, C.-H. & Im, N. (2023). Proposal of Restrictions on the Departure of Korea Small Fishing Vessel according to Wave Height. *Journal of Marine Science and Engineering*, 11, 1302. https://doi.org/10.3390/jmse11071302

**Corpus status:** Added August 2026 — threshold validation for g_o(o), wave height CAUTION boundary

---

## 1. What the paper does

Analyzes 66 small fishing vessel capsizing incidents in Korean coastal waters over 23 years (1999–2022) to argue that Korea's current 3 m departure restriction threshold is too lenient. Derives a vessel-length-specific departure restriction formula (Hs_KIMO) based on the UK Wolfson Unit MCA capsize research, and proposes new graduated restriction guidelines for Korean fishing vessels by size class.

**This paper does NOT:**
- Conduct its own wave tank or physical experiments — it applies the UK Wolfson Unit formula (references 19, 26, 27 in the paper) to Korean vessel specifications
- Establish a single universal threshold — it gives a length-dependent formula with outputs ranging from ~1.1m to ~2.1m

---

## 2. Key findings

### 2.1 Accident data (23-year record)
- 66 capsizing cases analyzed; Korean coast, 1999–2022
- **82% of 2017–2022 capsizing accidents occurred on days WITHOUT any weather warning** — the alert system failed to catch the risk
- **38% (25/66) of all capsizing incidents occurred at Hs ≤ 3 m** — below Korea's current 3 m departure restriction threshold
- 58% of wave-caused capsizing accidents occurred at Hs ≤ 3 m
- **89% of vessel accidents involve vessels < 10 tons** (gross tonnage)
- Capsizing incidents documented at Hs as low as 1.0 m (Table 8, cases 39, 40, 52 — LOA ~8–14m)

### 2.2 The Hs_KIMO formula
Derived from the UK Wolfson Unit critical wave height formula, adapted to Korean fishing vessel proportions:

```
Hs_KIMO = √(1 + 0.4 × (0.88 × LOA)) − 1
```

Where LOA is vessel length (metres).

**Departure restriction thresholds by vessel length (Table 11):**

| LOA (m) | Hs_KIMO (m) |
|---------|-------------|
| 10      | 1.13        |
| 14      | 1.43        |
| 16      | 1.58        |
| 18      | 1.71        |
| 24      | 2.07        |

**Verification:**
- 14m: √(1 + 0.4 × 12.32) − 1 = √5.928 − 1 ≈ 1.43 ✓
- 16m: √(1 + 0.4 × 14.08) − 1 = √6.632 − 1 ≈ 1.58 ✓
- 18m: √(1 + 0.4 × 15.84) − 1 = √7.336 − 1 ≈ 1.71 ✓

### 2.3 Cross-country comparison (Table 7)
| Country | Small craft caution threshold |
|---------|-------------------------------|
| USA     | Hs ≥ 1.8 m                   |
| Canada  | Hs ≥ 2–3 m                   |
| China   | Hs ≥ 2 m                     |
| Korea   | Hs ≥ 3 m (current, proposed to be reduced) |

### 2.4 Proposed management framework (Table 12)
- Vessels ≤ 10m: caution at Hs ≥ 1.0 m
- Vessels ≤ 24m: caution at Hs ≥ 2.0 m
- (Three-tier graduated system proposed — similar in structure to the architecture in this thesis)

---

## 3. Relevance to this research

### 3.1 What it supports
The paper provides the strongest available peer-reviewed empirical evidence that small fishing vessel departure restrictions anchored to 3 m significantly underestimate when capsizing risk materializes. The Hs_KIMO formula gives outputs of approximately **1.4–1.6 m for typical small fishing vessel sizes of 14–16 m LOA** — which aligns with the 1.5 m CAUTION boundary used in this architecture.

Use this paper to support the claim that 1.5 m as the SAFE/CAUTION boundary for g_o(o) is empirically grounded, not arbitrary.

### 3.2 What it does NOT support
- **Do not cite this paper as proving "Hs ≥ 1.5 m causes small vessel capsizing."** The formula gives length-dependent thresholds (1.13–2.07 m), not a universal 1.5 m cutoff.
- **Do not say the paper conducted wave tank experiments.** It applies existing UK Wolfson Unit MCA research to Korean vessel specifications.
- **Do not cite the 1.5 m boundary as directly validated.** The formula's outputs for 14–16m vessels are 1.43–1.58 m, which *straddles* 1.5 m — providing strong support but not a direct match.

### 3.3 Accurate citation text for Section 5.3 (g_o threshold justification)

> Jeong & Im (2023), analyzing 66 capsizing incidents in Korean coastal waters over 23 years (1999–2022), demonstrate that 38% of small fishing vessel capsizing incidents occurred at wave heights below 3 m — including incidents at Hs as low as 1.0 m — establishing that departure restrictions anchored to 3 m significantly underestimate the wave height at which capsizing risk materializes. Applying the Wolfson Unit critical wave height framework to Korean vessel specifications, they derive a length-dependent formula (Hs_KIMO) that produces departure caution thresholds of approximately 1.1–1.6 m for vessels in the 10–16 m LOA range, consistent with the 1.5 m CAUTION boundary used in this architecture.

### 3.4 Geographic limitation
The Hs_KIMO formula was calibrated for Korean fishing vessel geometry. Malaysian traditional fishing vessels (wooden sampans, Zone A/B) may have different beam-to-length ratios, potentially yielding different capsizing thresholds. This is a limitation to acknowledge in the discussion when citing this paper. The paper nonetheless provides the closest available empirical anchor for the 1-2 m range as the appropriate departure restriction zone for small fishing vessels.

---

## 4. What the other agent's summary got wrong

The agent summary (from prior session) stated: *"proves that small fishing vessels under 15 gross tons encounter severe capsizing hazards at significant wave heights Hs ≥ 1.5m, far below standard 3.0m commercial shipping limits."*

**Corrections:**
1. The paper does not "prove Hs ≥ 1.5m." The formula gives length-dependent thresholds from 1.13m to 2.07m.
2. The paper did not conduct physical experiments — it applied the UK Wolfson Unit formula.
3. The relevant comparison is not "3.0m commercial shipping limits" — it is Korea's current 3m small fishing vessel threshold (not a commercial shipping standard).
4. The paper's accident data includes vessels in the < 10 ton range, but the formula is length-based, not tonnage-based.

The agent's directional claim (capsizing risk materializes well below 3m) is accurate; the specific threshold claim (1.5m specifically) is overstated.

---

## 5. Placement in corpus

| Role | Tier |
|------|------|
| Threshold validation | Tier 2 (empirical risk/behavior) in the Three-Tier Triangulation framework |
| Relationship to MET Malaysia | MET Malaysia is Tier 3 (state policy); Jeong & Im provides Tier 2 empirical grounding |
| Documents to update | `appendix-c-formalisation.md` Section C.2 (g_o justification) |

---

## 6. Bibliographic details

- **Full title:** Proposal of Restrictions on the Departure of Korea Small Fishing Vessel according to Wave Height
- **Authors:** Cheong-Hwan Jeong, Namkug Im
- **Journal:** Journal of Marine Science and Engineering
- **Year:** 2023
- **Volume/Issue:** 11, 1302
- **DOI:** https://doi.org/10.3390/jmse11071302
- **Access:** Open access (MDPI)
- **Pages:** 16
- **Study period:** 1999–2022 (Korean coast)
- **n:** 66 capsizing incidents
