# Structured Extraction: Muhamad et al. (2024)

## 1. Citation & Metadata

- **Authors:** Mazlina Muhamad, Puspa Liza Ghazali, Rasheedul Haque, Noorhidayah Salehhudin
- **Title:** Validation of Factor Weights Affecting Productivity Efficiency in Malaysia's Small-Scale Fisheries Sector
- **Year:** 2024
- **Venue:** Pakistan Journal of Life and Social Sciences (PJLSS), 22(2), 12024–12040
- **DOI:** [10.57239/PJLSS-2024-22.2.00857](https://doi.org/10.57239/PJLSS-2024-22.2.00857)
- **Peer-reviewed:** Yes (indexed in Scopus and Web of Science per journal header), though venue is outside the core fisheries/AI/governance journal tier
- **Type:** Empirical — fuzzy model development with statistical validation

---

## 2. Research Problem (as relevant to this study)

The paper validates weightings of environmental, socio-economic, and technological factors affecting productivity efficiency in Malaysian small-scale fisheries. Its potential relevance lies in (a) confirming that environmental factors are significant determinants of productivity in the target domain, (b) providing a fuzzy logic approach to handling uncertainty in fisheries factor assessment, and (c) offering additional domain characterisation of Malaysian small-scale fisheries constraints.

---

## 3. Relevance Gate: Eight Core Research Themes

| # | Theme | Relevant? | Notes |
|---|---|---|---|
| 1 | Hybrid AI (rule-based + probabilistic) | ❌ | Fuzzy model is used for factor weighting, not hybrid AI decision support |
| 2 | Safety-critical AI decision-making | ❌ | Productivity efficiency, not safety-critical decisions |
| 3 | AI governance/control mechanisms | ❌ | No governance, gating, or scope restriction |
| 4 | Low-resource environments | ✅ Moderate | Malaysian small-scale fisheries; confirms low-income, low-technology-access population |
| 5 | Decision architecture formalisation | ❌ | Fuzzy weighting model, not decision architecture |
| 6 | Human role in decision-making | ❌ | Not addressed |
| 7 | Socio-technical evaluation | ✅ Weak | Factor validation touches socio-economic dimensions but not socio-technical system evaluation |
| 8 | Coastal fisheries/maritime domain | ✅ Strong | Malaysian small-scale fisheries — exact domain |

**Gate result:** 3/8 themes (1 strong, 1 moderate, 1 weak). Passes on **reduced path** — domain-context paper with limited architectural relevance.

---

## 4. Environmental Factors as Productivity Determinants

The paper's core finding relevant to the dissertation is that **environmental factors are validated as significant determinants of productivity** in Malaysian small-scale fisheries, alongside socio-economic and technological factors.

Environmental factors identified include:
- Water quality
- Weather patterns
- Marine biodiversity

**Mapping to E = {w, r, m, o, v, t}:**

| E component | Muhamad et al. coverage | Strength |
|---|---|---|
| **w (wind condition)** | Subsumed under "weather patterns" — not disaggregated | ⚠️ Indirect |
| **r (rainfall intensity)** | Subsumed under "weather patterns" — not disaggregated | ⚠️ Indirect |
| **m (marine warning level)** | Not addressed | ❌ |
| **o (ocean condition)** | "Water quality" and "marine biodiversity" partially overlap — these are ecological/biological ocean conditions rather than physical ocean state (wave, tide, current) | ⚠️ Different framing |
| **v (vessel class)** | Not addressed as an environmental parameter | ❌ |
| **t (trip state)** | Not addressed | ❌ |

**Assessment:** The environmental factors in this paper are framed at a higher level of abstraction than the proposed E vector. "Weather patterns" encompasses w and r but does not disaggregate them. "Water quality" and "marine biodiversity" relate to ecological ocean conditions rather than the physical ocean state (wave, tide, current) that drives safety classification. The paper confirms that environmental factors matter but does not provide the parameter-level specificity needed to ground individual E components. Shaffril et al. (2017) provides stronger, more specific evidence for each E parameter.

---

## 5. Fuzzy Logic for Handling Uncertainty in Fisheries

The paper employs fuzzy models to handle uncertainty and variability in factor assessment. Key methodological elements:

- **Membership functions** defined for each variable (environmental, socio-economic, technological)
- **Fuzzy inference** used to derive factor weightages
- **Statistical validation** via regression analysis, factor analysis, and sensitivity analysis
- **Cross-validation** using Procrustes Cross-Validation technique

**Relevance to S = f(E):** The safety state classifier S = f(E) in the proposed architecture must also handle uncertainty in environmental parameter assessment. The paper demonstrates that fuzzy logic is a viable approach for factor weighting in Malaysian fisheries contexts. However, the fuzzy model here weights *productivity* factors, not *safety state* classification — a fundamentally different objective. Productivity weighting asks "how much does each factor contribute to catch efficiency?" whereas safety state classification asks "given these environmental conditions, what is the safety state?"

**Potential methodological parallel:** If the implementation of S = f(E) uses fuzzy logic for state classification (e.g., fuzzy membership functions for wind condition thresholds), this paper provides a domain-specific precedent for applying fuzzy methods to Malaysian small-scale fisheries data. However, this is an implementation detail (deferred to O3 per the established formalisation principle), not an architectural contribution.

---

## 6. Domain Characterisation (Incremental to Shaffril et al. 2017)

The paper adds the following domain context beyond what Shaffril et al. (2017) already provides:

| Factor | Evidence | Incremental value |
|---|---|---|
| **Technological access** | Fishing gear, navigation systems, and fish preservation techniques identified as productivity factors; technology assistance flagged as main obstacle for small-scale fishermen (citing Adnan et al., 2021) | Confirms low-technology-access constraint; relevant to deployment platform considerations for any decision support system |
| **Market dynamics** | Fish prices, market accessibility identified as productivity factors | Not directly relevant to environmental state governance |
| **COVID-19 governance failures** | Cites Sowman et al. (2021) on pandemic exposing governance failures in small-scale fishing communities | Tangentially relevant — confirms governance vulnerability, but at policy level not architectural level |
| **Fuzzy logic in fisheries management** | Cites Paterson et al. (2007) on fuzzy-logic multi-criteria decision tool for fisheries; Sylaios et al. (2010) on fuzzy ranking of fishing areas | Potentially useful secondary references if fuzzy methods are used in S = f(E) implementation |

---

## 7. Mapping onto Architecture Components

| Component | Mapping | Strength |
|---|---|---|
| **E = {w, r, m, o, v, t}** | Environmental factors confirmed as productivity determinants, but at aggregate level ("weather patterns", "water quality") — no parameter-level mapping | ⚠️ Weak |
| **S = f(E)** | Fuzzy model demonstrates viability of fuzzy logic for factor assessment in Malaysian fisheries, but applied to productivity not safety classification | ⚠️ Methodological parallel only |
| **G(S)** | ❌ Not addressed | — |
| **A_AI(S)** | ❌ Not addressed | — |
| **CAUTION mode** | ❌ Not addressed | — |
| **Safety Dominance Property** | ❌ Not addressed | — |

---

## 8. Relevance to PS4 and PS5

| Study | Relevance |
|---|---|
| **PS4 (graduated vs. binary governance)** | No direct relevance. The fuzzy model does not implement governance of any kind. |
| **PS5 (socio-technical evaluation)** | Marginal. The validation of socio-economic and technological factors confirms the multi-dimensional constraints PS5 must account for, but does not provide evaluation methodology or instruments applicable to PS5. |

---

## 9. Relevance Score

### ⭐⭐ (Two Stars) — Supplementary Domain-Context Reference with Recency Value

**Justification:** The paper confirms that environmental factors are significant productivity determinants in Malaysian small-scale fisheries and demonstrates fuzzy logic as viable in this domain context. Its environmental factors are at a higher abstraction level than the proposed E vector, the fuzzy model addresses productivity not safety classification, and the paper contains no governance, architecture, or safety-critical content. However, its **recency (2024) provides critical temporal coverage** that Shaffril et al. (2017) cannot: it confirms that the domain conditions documented in 2017 — environmental factor significance, low-technology-access constraints, socio-economic vulnerability — persist as of 2024. For a dissertation submitted in 2026, a 9-year gap between the primary domain characterisation source and the submission date is an examiner vulnerability. Muhamad et al. (2024) closes this gap, demonstrating that the domain context grounding the architecture remains current.

---

## 10. Positioning Paragraph

Muhamad et al. (2024) validate that environmental, socio-economic, and technological factors are significant determinants of productivity efficiency in Malaysian small-scale fisheries, using a fuzzy model with statistical cross-validation. While the paper's environmental factors ("weather patterns", "water quality", "marine biodiversity") are framed at a higher abstraction level than the proposed environmental state vector E = {w, r, m, o, v, t}, the finding that environmental conditions remain statistically significant productivity drivers as recently as 2024 provides critical temporal continuity for the domain characterisation established by Shaffril et al. (2017). For a dissertation submitted in 2026, pairing these two sources — Shaffril et al. (2017) for parameter-level specificity, Muhamad et al. (2024) for recency — demonstrates that the environmental state grounding of the architecture reflects current, not merely historical, domain conditions. The paper's use of fuzzy logic for factor assessment in Malaysian fisheries also establishes a domain-specific methodological precedent, should the implementation of S = f(E) employ fuzzy membership functions for environmental parameter classification. However, the paper's fuzzy model addresses productivity weighting, not safety state classification, and contains no governance, gating, or advisory scope restriction — the gap between factor-weighted productivity models and runtime state-conditioned governance remains unaddressed.

---

## 11. Citation Placement Recommendations

| Section | Use | Priority |
|---|---|---|
| **Environmental state vector justification (recency anchor)** | Paired with Shaffril et al. (2017) to show temporal continuity: "Environmental factors have been consistently identified as significant productivity determinants in Malaysian small-scale fisheries (Shaffril et al., 2017; Muhamad et al., 2024)" — closes the 2017–2026 gap | **Medium** — recency function is strategically important |
| **Implementation chapter (S = f(E) methodology)** | Domain precedent for fuzzy logic application in Malaysian small-scale fisheries, if fuzzy methods are used in safety state classification | Medium — but only if fuzzy implementation is adopted |
| **Low-resource environment characterisation** | Technological access as a persisting constraint for small-scale fishermen; confirms deployment must accommodate low-technology users as recently as 2024 | Medium — adds temporal currency to Shaffril et al.'s 2017 characterisation |
| **Chapter 1 — Application domain (supporting)** | Recent confirmation that the domain characteristics (environmental vulnerability, socio-economic constraints, governance gaps) documented in earlier literature remain current | Medium |

---

## 12. Provenance & Citability Notes

- **Venue:** PJLSS is indexed in Scopus and Web of Science per the journal header. However, it is not a core fisheries, AI, or governance venue. Impact and standing should be verified independently.
- **Self-citation pattern:** The reference list contains approximately 15 citations involving the same research group (Haque, Senathirajah, and collaborators) across diverse topics (fashion apparel, digital marketing, job hopping, workplace romance, SME sustainability). This pattern is atypical for a focused fisheries study and warrants awareness.
- **Recommendation:** Usable as a supplementary citation for domain-context claims. Should not be load-bearing for core architectural arguments, gap claims, or E vector justification where stronger primary sources exist (Shaffril et al., 2017; Omar & Quah, 2005; Razali et al., 2010).
