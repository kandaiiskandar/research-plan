# Literature Review Extraction: Obi et al. (2025)

---

## 1. Paper Identity

- **Title:** Overview of the fishery and aquaculture sectors in Malaysia
- **Authors:** Chinedu Obi, Eric Brako Dompreh, Timothy Manyise, Shau Hwai Tan, Sau Pinn Woo, Cristiano M. Rossignoli
- **Year:** 2025
- **Venue:** *Frontiers in Sustainable Food Systems*, 9:1545263
- **DOI:** 10.3389/fsufs.2025.1545263
- **Type:** Literature-based review (policy-oriented sector overview)

---

## 2. Core Contribution

- **Problem addressed:** Malaysia's fishery and aquaculture sectors lack a comprehensive, policy-oriented analysis linking production trends with governance, economic constraints, and sustainability challenges. Existing literature focuses primarily on technical aspects (species productivity, environmental impacts) rather than integrated policy dynamics.
- **Proposed solution / key finding:** A historical-to-contemporary overview integrating production data (1990–2022), regulatory frameworks, economic constraints, and a SWOT analysis of Malaysia's aquaculture policy framework. Key findings include: total fishery production of 1.89 million metric tons in 2022; capture fisheries stagnation offset by aquaculture expansion (30% of production); declining self-sufficiency ratio (92.7% in 2017 → 90.2% in 2022); widening trade deficit; and persistent challenges from overfishing, climate change, water pollution, and regulatory inefficiencies.
- **Main contributions:** (1) Policy-oriented synthesis linking production challenges to governance gaps; (2) Updated production statistics and trade performance data; (3) SWOT analysis of the aquaculture policy framework; (4) Strategic recommendations including technology adoption (RAS, biofloc), R&D investment, biosecurity strengthening, and market access improvements.
- **Novelty:** Unlike prior Malaysia-focused studies that emphasise technical or environmental dimensions, this paper provides a holistic policy-governance perspective, identifying structural weaknesses (implementation gaps, coordination failures, rural–urban disparities) that constrain sector development.

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | **No** | No AI content whatsoever |
| Safety-critical AI decision-making | **No** | No decision system or safety architecture discussed |
| AI governance / control mechanisms | **No** | Governance discussed is fisheries policy governance, not AI governance |
| Low-resource environments | **Partial** | Documents resource constraints faced by small-scale fisheries producers (limited infrastructure, poor cold chain, financing gaps, rural–urban disparities); provides empirical context for what "low-resource" means in Malaysian coastal fisheries |
| Decision architecture formalisation | **No** | No formal decision models |
| Human role in decision-making | **No** | Not addressed in AI-decision context |
| Socio-technical evaluation | **No** | No socio-technical evaluation of technology systems |
| Coastal fisheries / maritime domain | **Yes** | Directly and comprehensively addresses Malaysian fisheries — the specific national context for my case study domain |

**Mid-Extraction Relevance Gate:** 1 Yes + 1 Partial → **REDUCED EXTRACTION** (Sections 4–7, 12–13, 16–17 only)

---

## 4. Decision Architecture Analysis

**Not applicable.** This paper contains no AI decision system, no layered architecture, no safety constraint mechanism, and no computational governance structure. It reviews fisheries sector performance, policy frameworks, and production economics — not decision-making architectures.

The only "governance" discussed is institutional fisheries governance: regulatory frameworks (GAqP, MyGAP certification), fishing zone designations (Zones A–C2+C3), seasonal fishing bans, and marine protected areas — all of which are human policy instruments, not computational decision structures.

---

## 5. Formal Model and Mathematical Representation

**Not applicable.** No formal model, mathematical representation, state variables, gate functions, or action spaces are defined. The paper is entirely descriptive and policy-analytical, relying on production statistics, trade data, and qualitative SWOT analysis.

No comparison possible to the DSR pipeline **E → S = f(E) → (G(S), A_AI(S)) → AI(E)**.

---

## 6. Safety State Classification

**Not applicable.** No operational or environmental conditions are classified into discrete safety or risk levels. The paper does not implement any safety state classification scheme.

The closest analogue is Malaysia's fishing zone system (Zones A, B, C, C2+C3), which regulates permitted vessel types and gear by zone — but this is a static spatial regulatory scheme, not a dynamic safety state classification.

---

## 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? | **No** | No AI system present |
| **Level 2 — Advisory scope governance** | What may AI recommend? | **No** | No AI recommendations |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | **No** | N/A |

The paper discusses fisheries *policy* governance (regulations, certifications, institutional coordination) but not AI governance in any form. It neither supports nor contradicts the two-level governance pair (G(S), A_AI(S)) — it operates in an entirely different domain of discourse (sector policy vs. computational architecture).

---

## 12. Key Concepts and Definitions

The following domain-specific concepts from this paper are relevant as contextual background for my research's case study domain:

- **Fishing zone system (Zones A–C2+C3):** Malaysia's spatial regulatory framework dividing marine waters into zones with permitted vessel/gear types — an example of static, rule-based fisheries governance (not AI-mediated)
- **Self-sufficiency ratio (SSR):** Percentage of domestic fish demand met by domestic production; declined from 92.7% (2017) to 90.2% (2022) — provides motivation for why decision support tools could benefit the sector
- **Good Aquaculture Practice (GAqP) / MyGAP:** Malaysian certification standards for aquaculture farms; only 37% compliance among freshwater farms — illustrates governance implementation gaps
- **IUU fishing:** Illegal, unreported, and unregulated fishing; estimated at ~30% of total marine fish landings — a major enforcement challenge
- **Small-scale fisheries constraints:** Rising production costs (feed up to 60% of total costs), limited cold chain infrastructure, inadequate financing, rural–urban disparities in infrastructure
- **Production composition (2022):** Marine capture 69%, aquaculture 30%, inland fisheries 1%; aquaculture dominated by seaweed (54%), brackish water fish (26%), freshwater fish (20%)
- **Workforce:** 149,630 directly employed (2022); marine capture = 116,613, aquaculture = 20,925

---

## 13. Limitations and Unsolved Problems

**Stated limitations:**
- Reliance on secondary, often aggregated data; absence of household-level microdata restricting understanding of socioeconomic dynamics among small-scale producers
- Limited data on the role of the private sector and small-scale aquaculture
- Some policy reports and trade documents are restricted, limiting insight into regulatory and market dynamics
- Literature availability varies across subsectors

**Unsolved problems / future work:**
- Bridging rural–urban infrastructure disparities for aquaculture
- Strengthening enforcement of IUU fishing regulations
- Improving disease management and biosecurity
- Developing alternative aquafeed sources to reduce import dependency
- Expanding household-level data collection for targeted policy

**Alignment with my research problem:**
- The paper does **not** identify any gap related to AI governance, two-level governance models, or computational decision architectures — it operates entirely in the policy-governance domain
- However, the documented constraints (limited data, poor connectivity in rural/coastal areas, small-scale producer resource limitations) empirically substantiate the "low-resource environment" characterisation that motivates my architecture's design requirements
- The governance implementation gaps (only 37% GAqP compliance, coordination failures, enforcement challenges) could contextually support the argument that technology-assisted decision support is needed in this domain

---

## 16. Relation to My Research and Positioning

- **Level 1 governance:** Not implemented (no AI system)
- **Level 2 governance:** Not implemented
- **State-conditioned governance pair:** Not applicable
- **Formal safety property:** None defined
- **Gap my research addresses:** This paper documents the operational realities of Malaysian fisheries without any AI decision support component. The gap is total — no AI architecture, no safety-state classification, no governance mechanism for AI participation or advisory scope exists in this context.

**Positioning paragraph:** This paper serves as **domain background** for my research, providing a comprehensive, peer-reviewed, and current (2025) characterisation of Malaysia's fishery and aquaculture sectors — the national context within which my case study (coastal fisheries) is situated. It documents the specific resource constraints (limited data, infrastructure disparities, small-scale producer challenges), governance gaps (certification compliance, enforcement weaknesses), and environmental pressures (overfishing, climate change, water pollution) that define the operating environment for my architecture. While the paper contains no AI or decision architecture content, it provides citable evidence for: (a) the low-resource nature of the Malaysian coastal fisheries environment, (b) the sector's need for improved decision support, and (c) the specific environmental factors (weather, marine conditions, vessel characteristics) that shape operational safety in this domain. It is best positioned in the **domain background subsection** of the literature review, providing sectoral context before the discussion turns to AI governance and safety-critical architecture.

---

## 17. Overall Relevance Score

### ⭐⭐ Low

**Justification:** The paper is directly relevant to the case study domain (Malaysian fisheries) and provides useful, peer-reviewed, current background data on production, policy, and sector challenges. However, it contains no AI content, no decision architecture, no formal models, no safety-state classification, and no governance mechanisms relevant to the core architectural contribution. Its value is strictly as domain context — providing empirical grounding for the "low-resource coastal fisheries environment" characterisation, but contributing nothing to the literature review's core themes of AI governance, safety-critical architecture, or decision formalisation.
