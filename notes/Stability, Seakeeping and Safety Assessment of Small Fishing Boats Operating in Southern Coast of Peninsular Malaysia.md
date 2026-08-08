# Stability, Seakeeping and Safety Assessment of Small Fishing Boats Operating in Southern Coast of Peninsular Malaysia

**Citation:** Yaakob, O., Hashim, F.E., Jalal, M.R., & Mustapa, M.A. (2015). Stability, Seakeeping and Safety Assessment of Small Fishing Boats Operating in Southern Coast of Peninsular Malaysia. *Journal of Sustainability Science and Management*, 10(1), 50–65. ISSN: 1823-8556.

**Corpus status:** Added August 2026 — Tier 1 (Hydrodynamics) threshold validation; addresses geographic limitation of Jeong & Im (2023) by studying actual Malaysian vessels

---

## 1. What the paper does

Assesses seakeeping, static stability, and safety equipment compliance of two traditional Malaysian small fishing boats from the Johor coast (Southern Peninsular Malaysia), using Maxsurf Ship Design software (Hydromax module for stability, Seakeeper module for seakeeping). Evaluates both boats against NORDFORSK 1987 seakeeping criteria and IMO stability criteria for fishing vessels under 12m.

**Standards applied:**
- Seakeeping: NORDFORSK 1987 (heavy manual work category)
- Stability: IMO Safety Recommendations for Decked Fishing Vessels < 12m (Annex 29, Chapter 3)
- Safety equipment: IMO/Torremolinos Protocol 1977
- Wave spectrum: JONSWAP (coastal waters, Southern Peninsular Malaysia)

---

## 2. The two boats

| Property | Boat A (Mersing) | Boat B (Pontian) |
|----------|-----------------|-----------------|
| Operating area | South China Sea side | Straits of Malacca |
| LOA (m) | 6.54 | 5.03 |
| Breadth (m) | 1.48 | 1.32 |
| Depth (m) | 0.55 | 0.30 |
| Engine | Outboard 15 HP | Outboard 15 HP |
| GRT | < 10 | < 10 |

Both are Zone A vessels (< 10 nm from shore), traditionally built with no naval architecture input, wooden hull construction.

**Malaysian small boat classification (M. A. Yunus, 2007 — Table 1 of paper):**
| Category | LOA (m) | Breadth (m) | GRT | Zone |
|----------|---------|-------------|-----|------|
| Small | 5.5–10.0 | 1.0–2.0 | < 10 | < 10 nm |
| Medium | 7.5–15.0 | 1.8–3.5 | 10–25 | < 30 nm |
| Large | 11.0–25.0 | 2.8–5.0 | > 25 | > 30 nm |

---

## 3. Key findings

### 3.1 Seakeeping results (NORDFORSK 1987 criteria)

WMO sea state codes used (Table 4 of paper):
| SS Code | Significant Wave Height (m) | Description |
|---------|----------------------------|-------------|
| SS2 | 0.1–0.5 (mean 0.3) | Smooth |
| SS3 | 0.5–1.25 (mean 0.875) | Slight |
| SS4 | 1.25–2.5 (mean 1.875) | Moderate |

Sea state conditions used in analysis (Table 5):
| SS Code | Hs (m) | Period (s) |
|---------|--------|-----------|
| SS2 | 0.550 | 6.5 |
| SS3 | 0.875 | 7.5 |
| SS4 | 1.875 | 8.8 |

**Boat A (Mersing, 6.54m) — seakeeping outcome:**
- SS2 (Hs = 0.55m): PASS (all four parameters within NORDFORSK limits)
- SS3 (Hs = 0.875m): PASS (all four parameters within limits)
- SS4 (Hs = 1.875m): **FAIL** — RMS vertical acceleration at FP = 0.332 g (limit 0.275), Bridge = 0.195 g (limit 0.150)
- **Operational limit: Sea State 3 (Hs up to ~1.25m)**

**Boat B (Pontian, 5.03m) — seakeeping outcome:**
- SS2 (Hs = 0.55m): PASS (all four parameters within limits)
- SS3 (Hs = 0.875m): **FAIL** — RMS vertical acceleration at FP = 0.290 g (limit 0.275), Bridge = 0.160 g (limit 0.150)
- SS4 (Hs = 1.875m): **FAIL** — multiple parameters exceeded (FP = 0.452, Bridge = 0.253, Roll = 4.54°)
- **Operational limit: Sea State 2 (Hs up to ~0.5m)**

### 3.2 Static stability results (IMO criteria)

Both boats **PASS** all IMO stability criteria across all three loading conditions (departure to fishing ground, departure from fishing ground, arrival at home port). Key values for Boat A (departure loading):
- Initial GMt: 1.245 m (limit: > 0.35 m) — passes by 3.6×
- Maximum GZ ≥ 0.200 m at 30°: actual 0.625 m — passes by 3.1×
- Angle of max GZ: 76° (limit: > 30°)

Boat B has lower stability margins (GMt 1.128 m, max GZ 0.315 m) but also passes.

**Key conclusion:** Static stability is not the limiting factor. Both boats meet static stability requirements but have dynamic seakeeping limits well within the wave heights they encounter.

### 3.3 Safety equipment survey

Both boats **FAIL** multiple IMO/Torremolinos requirements:
- Missing: survival craft, rocket signals, smoke signals, fire extinguishers, navigation lights (GREEN, WHITE)
- Passing: life jackets (barely — 2 when 2-3 required), watertight bulkhead

---

## 4. Relevance to this research

### 4.1 What this paper validates (Tier 1 — Hydrodynamics)

**This is the only paper in the corpus studying actual Malaysian small fishing vessels using naval architecture methods.** It directly addresses the geographic limitation flagged for Jeong & Im (2023).

**Core finding relevant to thresholds:** Malaysian Zone A small fishing boats (< 10 GRT, 5–7m LOA) have seakeeping operability limits between Hs ≈ 0.55m (Boat B operational limit) and Hs ≈ 1.25m (Boat A operational limit). These boats begin experiencing operability failure well below the 1.5m SAFE/CAUTION boundary.

**However — this validates the architecture design, not necessarily the 1.5m number.**

The architecture captures this risk correctly through TWO mechanisms:
1. **g_v(small) = CAUTION always** — for any small vessel (GRT < 10, Zone A), the vessel category itself contributes CAUTION to max-severity, regardless of wave height
2. **g_o(o) contributes wave-height-specific CAUTION when Hs ≥ 1.5m**

For a small vessel at Hs = 0.875m (which causes Boat B to fail): g_o = SAFE (0.875 < 1.5), g_v = CAUTION → f(E) = CAUTION. Correct — the architecture restricts the AI advisory scope.

For a small vessel at Hs = 1.875m (which causes Boat A to fail): g_o = CAUTION (1.5 ≤ 1.875 ≤ 3.5), g_v = CAUTION → f(E) = CAUTION. Correct — still restricted.

**The architecture correctly captures the risk for the smallest vessels through g_v, not g_o alone.** This is consistent with the paper's finding that vessel size is the primary determinant of wave height operability limits.

### 4.2 What it validates about g_v design

The paper provides hydrodynamic justification for why g_v(small) = CAUTION (never SAFE):
- Zone A small boats fail seakeeping criteria at Hs as low as 0.875m
- Even under static stability pass, they have operability and survivability risks
- These boats should never receive full-scope AI advisory output (DepartureTime, Duration) in any sea state, because their safety envelope is narrow and dynamic conditions quickly exceed it

**This supports the architectural choice that vessel category alone never returns SAFE for small vessels.** The paper provides the hydrodynamic reason why.

### 4.3 What it validates about the 1.5m CAUTION boundary for g_o

For medium and large vessels (LOA 7.5-25m, GRT 10+), which are not studied in this paper, the 1.5m threshold for wave height CAUTION represents the wave condition at which even larger vessels begin encountering elevated risk. The paper establishes that small vessels are already in constrained territory at much lower wave heights — but their risk is captured via g_v, leaving g_o to capture the wave-specific risk contribution that applies to all vessel sizes.

The 1.5m boundary is conservative relative to what would be derived from this paper if only small vessels were considered — but the architecture is designed for multiple vessel sizes, and the smallest vessels have additional protection via g_v.

### 4.4 Accurate citation text for Section 5.3 or Foundations section

> Yaakob et al. (2015), assessing seakeeping and stability performance of two traditional Malaysian small fishing boats (LOA 5.0–6.5 m, < 10 GRT) from the Johor coast using Maxsurf naval architecture software (JONSWAP spectrum, NORDFORSK 1987 criteria), found that the smaller vessel (5.03 m LOA) failed seakeeping criteria at Sea State 3 (Hs ≈ 0.875 m), while the larger (6.54 m LOA) failed at Sea State 4 (Hs ≈ 1.875 m). Both passed static stability criteria. This establishes that Malaysian Zone A small fishing vessels have dynamic operability limits well within the conditions under which they routinely operate, and that static stability alone does not capture the wave height risk these vessels face.

**For justifying g_v design specifically:**
> The hydrodynamic operability limits documented by Yaakob et al. (2015) — as low as Hs ≈ 0.875 m for the smallest Zone A vessels — justify the design decision that vessel category alone (g_v(v ∈ {small, medium}) = CAUTION) contributes CAUTION to the worst-case aggregation regardless of other parameters, ensuring the AI advisory scope is restricted even in nominally safe wave conditions.

### 4.5 Placement in Three-Tier Triangulation

| Tier | Role | Source |
|------|------|--------|
| Tier 1 (Hydrodynamics) | **This paper** — physical basis for wave height limits on Malaysian vessels | Yaakob et al. (2015) |
| Tier 2 (Empirical risk) | 23-year accident record | Jeong & Im (2023) |
| Tier 3 (State policy) | MET Malaysia warning criteria | MET Malaysia (verified Aug 2026) |

---

## 5. What this paper does NOT support

- It does not directly validate 1.5m as the CAUTION boundary (the studied boats fail at much lower Hs — but their risk is captured via g_v)
- It does not study medium or large vessels
- Two boats is a very limited sample; the paper itself notes that "different design factor and different operating area may produce different results"
- The boats are from 2015 — though traditional Malaysian wooden boat design has not changed fundamentally

---

## 6. Bibliographic details

- **Full title:** Stability, Seakeeping and Safety Assessment of Small Fishing Boats Operating in Southern Coast of Peninsular Malaysia
- **Authors:** Omar Yaakob, Farah Ellyza Hashim, Mohd Rajali Jalal, Muhammad Adli Mustapa
- **Institution:** Marine Technology Centre, Universiti Teknologi Malaysia (UTM)
- **Journal:** Journal of Sustainability Science and Management
- **Year:** 2015
- **Volume/Issue:** 10(1), pages 50–65
- **ISSN:** 1823-8556
- **Publisher:** Penerbit UMT
- **Access:** Open access
- **Study location:** Mersing (South China Sea) and Pontian (Straits of Malacca), Johor, Peninsular Malaysia
- **Software:** Maxsurf Ship Design (Hydromax + Seakeeper modules)
