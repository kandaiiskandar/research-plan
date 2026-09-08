# Stability, Seakeeping and Safety Assessment of Small Fishing Boats Operating in Southern Coast of Peninsular Malaysia

**Citation:** Yaakob, O., Hashim, F.E., Jalal, M.R., & Mustapa, M.A. (2015). Stability, Seakeeping and Safety Assessment of Small Fishing Boats Operating in Southern Coast of Peninsular Malaysia. *Journal of Sustainability Science and Management*, 10(1), 50–65. ISSN: 1823-8556.

**Corpus status:** Added August 2026 — Tier 1 (Hydrodynamics) threshold validation; addresses geographic limitation of Jeong & Im (2023) by studying actual Malaysian vessels

---

> ## ⚠️ Partial revision notice — 2026-09-06
>
> **Sections 1, 2, 3, 5 and 6 of these notes are unaffected.** The paper's findings — the two vessels, the NORDFORSK and IMO results, the operability limits, the safety equipment survey — are reported accurately and remain the corpus record for this source.
>
> **Section 4 contained architectural inferences that have been superseded.** Those inferences argued that the paper justifies `g_v(small) = CAUTION always` — a per-component classification function contributing a constant severity term to max-severity. That formulation was removed from the formal model on 2026-09-06.
>
> **Why:** a constant term inside a maximum establishes a floor on the output but cannot shift a threshold. Under that formulation, vessel category had no effect at all on the CAUTION/UNSAFE boundary — a 5 m boat and a 20 m boat were classified UNSAFE at identical wave heights (3.5 m) and wind speeds (27 kn). This paper's own data contradicts that: Boat A exceeds NORDFORSK operability limits at Hs ≈ 1.875 m, roughly half the wave height at which the superseded model would have declared it UNSAFE.
>
> **What the paper actually supports:** vessel-specific wave height limits. That is now implemented directly as `g_o(o, v)` — vessel category parameterises the ocean state thresholds rather than voting independently.
>
> Section 4 below has been revised in place. Superseded reasoning is retained in blockquote for the record.
>
> Full rationale: `docs/canonical/appendix-c-formalisation.md` C.2 and `docs/superpowers/plans/2026-09-06-formal-model-and-evaluation-realignment.md`.

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

**However — this validates the need for vessel-specific thresholds, not the 1.5m number.**

**Current interpretation (2026-09-06).** The paper's core contribution to the formal model is that *the wave height at which conditions become dangerous depends on the vessel*. Boat B (5.03 m) reaches its operational ceiling at Sea State 2; Boat A (6.54 m) at Sea State 3. Same water, different limits. This is a conditional relationship, and it is implemented as `g_o(o, v)` — vessel category selects the threshold row:

| v (GRT) | SAFE | CAUTION | UNSAFE |
|---|---|---|---|
| small (< 10) | o < 1.0 m | 1.0 ≤ o ≤ 1.9 m | o > 1.9 m |
| medium (10–25) | o < 1.4 m | 1.4 ≤ o ≤ 2.8 m | o > 2.8 m |
| big (> 25) | o < 1.5 m | 1.5 ≤ o ≤ 3.5 m | o > 3.5 m |

The small-vessel row is grounded in this paper: the 1.9 m UNSAFE boundary corresponds to SS4 (Hs ≈ 1.875 m), where Boat A failed NORDFORSK on multiple parameters. The 1.0 m CAUTION onset comes from Jeong & Im's Table 12 recommendation for vessels ≤ 10 m, corroborated by Boat A's ≈ 1.25 m operational limit.

*Caveat:* reading NORDFORSK operability failure as an UNSAFE trigger is an interpretation. This paper reports that the crew cannot safely perform heavy manual work at that sea state; it does not characterise this as a departure prohibition. Recorded as a design decision in appendix-c C.9.1.

> **Superseded reasoning (retained for the record).**
>
> *The architecture captures this risk correctly through TWO mechanisms:*
> 1. *`g_v(small) = CAUTION always` — for any small vessel (GRT < 10, Zone A), the vessel category itself contributes CAUTION to max-severity, regardless of wave height*
> 2. *`g_o(o)` contributes wave-height-specific CAUTION when Hs ≥ 1.5m*
>
> *For a small vessel at Hs = 0.875m: g_o = SAFE, g_v = CAUTION → f(E) = CAUTION. Correct — the architecture restricts the AI advisory scope.*
>
> *For a small vessel at Hs = 1.875m: g_o = CAUTION, g_v = CAUTION → f(E) = CAUTION. Correct — still restricted.*
>
> **Why this was wrong.** The two worked cases above are both correct as far as they go, but they only test the SAFE→CAUTION transition, where the `g_v` floor does work. They never test the CAUTION→UNSAFE boundary, where it does nothing. Extending the same reasoning to Hs = 3.0 m: `g_o` = CAUTION (1.5 ≤ 3.0 ≤ 3.5), `g_v` = CAUTION → f(E) = **CAUTION** — a 6.5 m boat in a 3 m sea, 2.4× past its own operability limit, receiving "Go, with caution." The mechanism that was supposed to protect small vessels contributed nothing at exactly the point it mattered most.

### 4.2 ~~What it validates about g_v design~~ — SUPERSEDED 2026-09-06

**There is no `g_v` in the current model.** This section argued for it. Retained below for the record, with the counter-argument.

> *The paper provides hydrodynamic justification for why g_v(small) = CAUTION (never SAFE):*
> - *Zone A small boats fail seakeeping criteria at Hs as low as 0.875m*
> - *Even under static stability pass, they have operability and survivability risks*
> - *These boats should never receive full-scope AI advisory output (DepartureTime, Duration) in any sea state, because their safety envelope is narrow and dynamic conditions quickly exceed it*
>
> ***This supports the architectural choice that vessel category alone never returns SAFE for small vessels.** The paper provides the hydrodynamic reason why.*

**Why this was rejected.**

*It is not the paper's claim.* Yaakob et al. report seakeeping and stability results. They make no statement about advisory systems, recommendation scope, or what information should be provided to operators. The third bullet — "should never receive full-scope AI advisory output" — is an architectural inference layered on top of the source, not a finding transferred from it.

*It made the contribution unobservable.* Because `g_v(small) = CAUTION` held unconditionally, `f(E) ≥ CAUTION` for every vessel under 25 GRT. The deployment population is predominantly below 40 GRT, so for real users SAFE was unreachable and the three-state architecture collapsed to two reachable states. The strict containment `A_AI(SAFE) ⊃ A_AI(CAUTION)` — the thesis's principal formal claim — could never be exercised in the target domain, and RQ5 ("user study across three safety states") was unrunnable as designed.

*The premise doesn't require the mechanism.* If the concern is that these vessels have a narrow envelope, the correct response is thresholds tight enough to reflect that envelope — which `g_o(o, v)` now provides, with the small-vessel UNSAFE boundary at 1.9 m rather than 3.5 m. A blanket floor was a coarse substitute for a threshold the model didn't yet have.

*The safety-equipment argument belongs elsewhere.* Section 3.3 of these notes documents both vessels failing IMO/Torremolinos requirements. That is a genuine risk factor and genuinely condition-independent — but it concerns vessel *certification*, not environmental state. `f(E)` classifies environmental conditions; encoding a compliance judgment inside it conflates two distinct governance questions. If advisory restriction on compliance grounds is wanted, it needs its own gate. Recorded in appendix-c C.9.3.

**What survives:** the hydrodynamic finding that these vessels have operability limits far below conventional wave height thresholds. That finding is now expressed through the small-vessel row of `g_o`, where it does the work it was always meant to do.

### 4.3 What it validates about the g_o threshold rows

*Revised 2026-09-06.*

This paper studies only small vessels (5.03 m and 6.54 m, both < 10 GRT), so it grounds the **small row** of `g_o` directly and says nothing about the others:

- **small (< 10 GRT)** — grounded here. UNSAFE at 1.9 m from Boat A's SS4 NORDFORSK failure (Hs ≈ 1.875 m); CAUTION onset at 1.0 m corroborated by Boat A's ≈ 1.25 m operational ceiling.
- **medium (10–25 GRT)** — not studied here. Grounded in Jeong & Im's Hs_KIMO across 10–15 m LOA (1.13–1.48 m). UNSAFE boundary interpolated, no direct source.
- **big (> 25 GRT)** — not studied here. MET Malaysia Category 1 criteria; Hs_KIMO = 1.58 m at 16 m LOA.

The 1.5 m figure that previously applied to all vessels corresponds, under Hs_KIMO, to a vessel of roughly 15 m LOA. This paper's boats are 5–6.5 m. Applying a 15 m vessel's threshold to a 6 m hull was the underlying error; that threshold is now confined to the big row where it belongs.

> **Superseded (retained for the record):** *"...small vessels are already in constrained territory at much lower wave heights — but their risk is captured via g_v, leaving g_o to capture the wave-specific risk contribution that applies to all vessel sizes... the smallest vessels have additional protection via g_v."* — The "additional protection" did not extend to the CAUTION/UNSAFE boundary. See §4.1 and §4.2.

### 4.4 Accurate citation text for Section 5.3 or Foundations section

> Yaakob et al. (2015), assessing seakeeping and stability performance of two traditional Malaysian small fishing boats (LOA 5.0–6.5 m, < 10 GRT) from the Johor coast using Maxsurf naval architecture software (JONSWAP spectrum, NORDFORSK 1987 criteria), found that the smaller vessel (5.03 m LOA) failed seakeeping criteria at Sea State 3 (Hs ≈ 0.875 m), while the larger (6.54 m LOA) failed at Sea State 4 (Hs ≈ 1.875 m). Both passed static stability criteria. This establishes that Malaysian Zone A small fishing vessels have dynamic operability limits well within the conditions under which they routinely operate, and that static stability alone does not capture the wave height risk these vessels face.

**For justifying the vessel-conditional thresholds** *(replaces the former g_v justification text, 2026-09-06)*:
> The hydrodynamic operability limits documented by Yaakob et al. (2015) establish that the wave height at which conditions become unsafe is vessel-specific: the 5.03 m vessel reached its NORDFORSK ceiling at Sea State 2 (Hs ≈ 0.5 m) and the 6.54 m vessel at Sea State 3 (Hs ≈ 1.25 m), with the latter failing multiple criteria at Sea State 4 (Hs ≈ 1.875 m). This justifies the design decision to parameterise the ocean state classification function by vessel category, g_o(o, v), rather than applying a single vessel-independent threshold set. A vessel-blind threshold calibrated for larger vessels would classify a 6.5 m hull as merely marginal in conditions well beyond its documented operability envelope.

> **Superseded (retained for the record):** *"The hydrodynamic operability limits documented by Yaakob et al. (2015) — as low as Hs ≈ 0.875 m for the smallest Zone A vessels — justify the design decision that vessel category alone (g_v(v ∈ {small, medium}) = CAUTION) contributes CAUTION to the worst-case aggregation regardless of other parameters, ensuring the AI advisory scope is restricted even in nominally safe wave conditions."*
>
> Note also that 0.875 m is the sea state at which Boat B *fails*, not its operational limit — the limit is the top of SS2, Hs ≈ 0.5 m. The superseded text conflated failure points with operational ceilings throughout.

### 4.5 Placement in Three-Tier Triangulation

| Tier | Role | Source |
|------|------|--------|
| Tier 1 (Hydrodynamics) | **This paper** — physical basis for wave height limits on Malaysian vessels | Yaakob et al. (2015) |
| Tier 2 (Empirical risk) | 23-year accident record | Jeong & Im (2023) |
| Tier 3 (State policy) | MET Malaysia warning criteria | MET Malaysia (verified Aug 2026) |

---

## 5. What this paper does NOT support

- It does not validate 1.5 m as a CAUTION boundary for the vessels it studies — both boats reach their operability ceilings well below that. It grounds the **small row** of g_o (CAUTION onset 1.0 m, UNSAFE 1.9 m); the medium and big rows rest on other sources.
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
