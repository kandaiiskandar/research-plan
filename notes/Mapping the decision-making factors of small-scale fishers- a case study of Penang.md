## Literature Review Extraction
### Gao (2024) — Mapping the Decision-Making Factors of Small-Scale Fishers: A Case Study of Penang

---

## Early Relevance Check: PASSED

1. Does this paper address at least one of the 8 core research themes? **Yes** — directly addresses coastal fisheries/maritime domain and human role in decision-making.
2. Does this paper contribute to fisheries/maritime AI, human decision-making, or low-resource deployment contexts? **Yes** — provides empirical mapping of decision-making factors in the exact domain context (coastal small-scale fisheries in a developing country).
3. Could this paper plausibly be cited in a literature review about graduated AI governance for safety-critical decision support? **Yes** — provides the empirical grounding for what an AI decision support system in coastal fisheries would need to account for: environmental factors, safety concerns, decision types, and the human decision-making architecture that AI must support rather than replace.

**Proceed with reduced extraction (2 Yes, 3 Partial).**

---

### 1. Paper Identity

- **Full title:** Mapping the Decision-Making Factors of Small-Scale Fishers: A Case Study of Penang
- **Author:** Tianlin Gao
- **Supervisors:** Prof. Dr. Roberta Moruzzo (Promotor); Dr. Rodolfo Dam Lam (Co-promoter)
- **Year:** 2024 (defended June 2024)
- **Publication venue:** Unpublished M.Sc. thesis, International Master of Science in Rural Development (IMRD), Erasmus Mundus Joint Master Degree, defended at University of Pisa. Conducted in collaboration with WorldFish (CGIAR).
- **Type of paper:** Empirical qualitative case study using semi-structured interviews and causal mapping.

**Citation quality note:** Unpublished M.Sc. thesis, not peer-reviewed. However, it is deposited in the CGIAR/WorldFish institutional repository with a persistent identifier (hdl.handle.net/10568/152289), making it citable and retrievable. The WorldFish collaboration lends institutional credibility. Suitable for domain contextualisation and supporting empirical claims about fisher decision-making processes, but should be supplemented with peer-reviewed sources for formal claims.

---

### 2. Core Contribution

- **Main problem addressed:** Limited empirical understanding of the nuanced decision-making processes of small-scale fishers, particularly how local context shapes these processes across economic, social, and environmental dimensions.

- **Proposed solution / key finding:** Produces three causal decision-making maps for Penang's small-scale fishers through qualitative thematic analysis of 25 semi-structured interviews. Identifies 42 factors across three decision categories: (1) daily operational decisions, (2) strategic fishing and sales decisions, and (3) community involvement and collective action decisions.

- **Main contributions:**
  - Empirical identification and importance-ranking of decision factors for SSF in Penang, Malaysia
  - Three causal decision-making maps showing factor interrelationships
  - Discovery of a "vicious circle of resilience" where stability-focused strategies trap fishers in long-term financial vulnerability
  - Documentation of fishers' low government satisfaction and desire for public participation
  - Evidence that local context (community networks, institutions, cultural practices) significantly shapes decision-making

- **What is novel:** Application of causal mapping methodology to SSF decision-making in a Southeast Asian context; integration of expert interviews with fisher interviews to construct multi-dimensional decision maps; identification of the resilience trap mechanism.

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | No | No AI component; purely human decision-making study. |
| Safety-critical AI decision-making | No | Does not address AI systems. However, documents the safety-critical nature of fishing decisions (weather, trawler threats, gear limitations) that my AI system must account for. |
| AI governance / control mechanisms | No | No AI governance discussed. |
| Low-resource environments | Partial | Describes the low-resource operational context in detail: unpredictable income, limited savings, poor credit access, reliance on informal networks, basic technology (WhatsApp, walkie-talkies). Does not address low-resource *AI deployment*. |
| Decision architecture formalisation | Partial | Maps decision factors and causal relationships through causal mapping, but does not formalise these as mathematical models. The three decision categories and factor importance rankings provide empirical grounding for what a formal decision architecture must capture. |
| Human role in decision-making | Yes | Core focus. Documents how fishers make decisions across operational, strategic, and collective action domains. Shows the centrality of personal experience (importance 4.71), social networks, and environmental assessment in daily decisions — the exact human decision processes that my AI system must support. |
| Socio-technical evaluation | Partial | Qualitative case study with systematic coding and importance assessment. Provides a socio-technical lens on fisher decision-making but does not evaluate a technology intervention. |
| Coastal fisheries / maritime domain | Yes | Core domain. Set in Penang, Malaysia — small-scale fisheries in Zone A (0–5 nautical miles), gill net fishers, 1–3 person boats. Documents species targeted, fishing schedules, sales channels, and the regulatory zoning system. Directly relevant to my case study domain. |

**Yes/Partial count:** 2 Yes, 3 Partial → **REDUCED EXTRACTION** (Sections 4–7, 12–13, 16–17)

---

### 4. Decision Architecture Analysis

- **Decision-making structure:** The study identifies a **three-tier decision hierarchy** among small-scale fishers:
  1. **Daily Operational Decisions** (when to fish, where to fish, when to terminate a trip) — driven by immediate environmental conditions (tide, weather, fishing resources) and real-time information
  2. **Strategic Fishing and Sales Decisions** (how to fish, how to sell) — driven by long-term financial stability, market access, and buyer relationships
  3. **Community Involvement and Collective Action Decisions** (joining FA, joining protests) — driven by social identity, institutional pressures, and political engagement

  This hierarchy is sequential in timescale (immediate → medium-term → long-term) and moves from environmentally-dominated to socially-dominated factors.

- **Layered architecture / safety constraints:** Not formalised as a governance structure, but the study reveals an implicit safety constraint mechanism: **weather and safety concerns function as go/no-go gates** for daily operational decisions. Fishers report that adverse weather "can halt fishing trips altogether" (importance level 3.40 for safety concern, 3.75 for weather). Trawler intrusion at night creates safety risks that constrain location decisions. These function as informal Level 1 participation gates — fishers self-impose binary go/no-go decisions based on environmental assessment.

- **Rule-based constraints before AI/probabilistic decisions:** The study documents several rule-based constraints that fishers apply before operational decisions:
  - **Tide-based port access constraint:** "I have to depend on the tide and avoid leaving the port during low tide so that my boat can exit" — a hard physical constraint that gates all fishing activity
  - **Weather-based safety gate:** Adverse weather halts trips or forces location changes
  - **Seasonal species migration patterns:** Fishers adapt strategies based on known seasonal cycles
  - These are deterministic, environmental-state-based rules that precede any probabilistic reasoning about catch expectations — directly analogous to the deterministic safety classification S = f(E) in my architecture.

- **Boundary between deterministic and probabilistic reasoning:** The study implicitly reveals this boundary: environmental state assessment (tide, weather, season) operates as deterministic constraint, while catch prediction and location optimisation operate probabilistically through personal experience, social network information, and trial-and-error. The causal maps show environmental factors flowing *into* catch predictions, which then inform operational decisions — a pipeline structure that parallels E → S → decision.

- **Failure modes / fallback behaviour:** Documented: fishers terminate trips early when catch is poor, change locations based on real-time information, cancel trips in adverse weather, and maintain long-term buyer relationships as financial safety nets. The "vicious circle of resilience" is itself a systemic failure mode where risk-mitigation strategies create long-term vulnerability.

---

### 5. Formal Model and Mathematical Representation

- **Formal model defined?** No formal mathematical model. The study uses qualitative causal mapping with importance ratings (1–5 scale) and frequency counts, but does not define state variables, functions, or formal relationships.

- **Comparison to E → S = f(E) → (G(S), A_AI(S)) → AI(E):**

  The study's empirical findings map remarkably well onto my formal architecture, though without formalisation:

  | My Architecture Component | Empirical Equivalent in Gao (2024) |
  |---|---|
  | **E = {w, r, m, o, v, t}** (environmental state vector) | Weather (importance 3.75), fishing resource (4.45), tide (4.55), season (explaining factor), safety concern (3.40), previous catch (4.38) — these are the exact environmental variables fishers assess before operational decisions |
  | **S = f(E) → {SAFE, CAUTION, UNSAFE}** | Fishers implicitly classify conditions as: go fishing (SAFE), fish with caution/change location (CAUTION-like), or don't go/terminate early (UNSAFE). Weather can "halt fishing trips altogether" (UNSAFE) or force location changes (CAUTION-like). |
  | **G(S) = 0 or 1** (participation gate) | Fishers apply binary go/no-go decisions based on weather, tide, and safety: "If the wind is too strong, I don't go" — a self-imposed participation gate. |
  | **A_AI(S)** (admissible recommendation space) | Not formalised, but the study shows that under different conditions, fishers consider different *types* of decisions: in favourable conditions, they decide timing, location, and duration; in marginal conditions, they focus only on whether to go at all and basic safety. |

  The critical finding is that **fishers already operate an informal version of graduated, state-conditioned decision-making** — they assess environmental state, classify conditions, and adjust both their participation and the scope of their decisions accordingly. My architecture formalises what fishers do intuitively.

- **State-dependent recommendation restriction?** Not formalised, but empirically present. Under favourable conditions, fishers make full-scope decisions (when, where, how long, what species). Under marginal conditions, the decision collapses to binary go/no-go. Under deteriorating conditions mid-trip, fishers restrict decisions to "terminate now or change location." This is an informal analogue of A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅.

- **Safety Dominance Property?** Not defined. However, the study documents that safety concerns override economic goals: "adverse weather conditions can halt fishing trips altogether" regardless of economic need. This is an informal safety dominance — environmental safety constraints override economic optimisation.

---

### 6. Safety State Classification

- **Discrete risk/safety levels?** Not explicitly classified, but the study reveals an implicit tripartite classification in fisher behaviour:
  - **Favourable conditions:** Full operational scope — fishers choose optimal timing, location, species, duration
  - **Marginal/uncertain conditions:** Restricted scope — fishers monitor weather, share information actively, consider early termination, avoid certain locations (trawler-affected areas)
  - **Adverse conditions:** Operations halt — "adverse weather conditions can halt fishing trips altogether"; tidal constraints physically prevent port exit

- **Classification inputs:** The factors that drive this informal classification map directly to my environmental state vector:
  - **w (wind/weather):** Importance 3.75 — "If the wind is too strong, I don't go"
  - **r (rainfall):** Captured within weather factor; storms affect species availability
  - **m (marine warning):** Not formalised, but fishers monitor weather forecasts and share warnings through social networks
  - **o (ocean condition / tide):** Importance 4.55 — the highest-rated factor; dictates port access and net effectiveness
  - **v (vessel class):** Implicit — gear and vessel constraints limit how far fishers can safely venture; economic constraints prevent upgrades
  - **t (trip state):** Implicit — "when to terminate a trip" is a distinct decision category where mid-trip conditions (catch volume, changing weather) are assessed

- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:** The fisher decision-making process described in this study provides strong empirical validation for the tripartite safety state classification. Fishers do not operate in a binary world — they operate across a spectrum where conditions can be fully favourable, cautiously manageable, or prohibitive. My architecture formalises this observed behaviour.

- **AI recommendation scope variation across safety levels?** Not applicable (no AI system), but the study shows that *human* decision scope varies across conditions — full decision scope in favourable conditions, restricted to go/no-go in adverse conditions. This empirically grounds the CAUTION state concept: there exist real-world conditions where fishers still go to sea but with restricted operational scope (shorter trips, closer locations, heightened monitoring).

---

### 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does the fisher go to sea at all? | **Yes (informal)** | Fishers apply self-imposed go/no-go gates based on weather, tide, and safety. "If the wind is too strong, I don't go." Tide physically gates port access. These are binary participation decisions driven by environmental state assessment. |
| **Level 2 — Advisory scope governance** | What types of decisions does the fisher make? | **Partial (informal)** | Under different conditions, the *scope* of decisions changes: full scope (timing, location, species, duration) under favourable conditions; restricted to location change or early termination under marginal conditions. Not formalised, but empirically observed. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | **Partial (informal)** | Both the go/no-go decision and the scope of operational decisions are driven by the same environmental state assessment (weather, tide, fishing resources, safety). The study does not formalise this as a unified governance pair, but the empirical pattern is consistent with (G(S), A_AI(S)). |

- **Binary switch or graduated?** Fisher decision-making is empirically **graduated**: the study documents a spectrum from full operational freedom through restricted operations to complete halt. This is not binary. The informal CAUTION-equivalent is well-documented: fishers go to sea but with shortened trips, closer locations, heightened vigilance, and active information monitoring.

- **Support or contradict the two-level governance pair?** **Strongly supports.** The study provides empirical evidence that the human decision-making process my AI system must support already operates with informal two-level, state-conditioned governance. Formalising this in the AI architecture (G(S), A_AI(S)) preserves the natural decision structure that fishers already use.

---

### 12. Key Concepts and Definitions

- **Decision-making map / causal map:** Visual representation of causal relationships between factors influencing decisions. Nodes represent factors (coded as environmental, economic, or social), arrows indicate causal influence, and importance levels (1–5) are assigned. Three maps produced for operational, strategic, and collective action decisions.

- **Daily Operational Decisions:** When to fish, where to fish, when to terminate a trip. Dominated by environmental factors (tide 4.55, fishing resource 4.45, previous catch 4.38, weather 3.75) and personal experience (4.71). These are the decisions most directly relevant to my AI decision support system.

- **Coded factors vs. explaining factors:** Coded factors are those meeting frequency (>3) and importance (≥2) thresholds from interview data. Explaining factors are causal antecedents identified through causal coding that extend beyond the filtered set. This distinction is methodologically useful — it separates primary decision inputs from background causal drivers.

- **Vicious circle of resilience:** A pattern where fishers' stability-focused coping strategies (choosing stable-but-lower-income fishing methods, maintaining buyer relationships for credit access) perpetuate long-term financial vulnerability by preventing income maximisation and savings accumulation. Relevant to my research as context for why fishers need decision support — they are operating under compounding constraints.

- **Environmental state factors with importance ratings:**
  - Tide: 4.55 (highest rated)
  - Fishing resource: 4.45
  - Previous catch: 4.38
  - Weather: 3.75
  - Safety concern: 3.40
  - Season: explaining factor (not independently rated)

  These importance ratings empirically validate the composition of my environmental state vector E = {w, r, m, o, v, t}.

- **Zone A (small-scale fisheries zone):** 0–5 nautical miles from shore, vessels <40 GRT, traditional/artisanal methods. This is the regulatory boundary defining the SSF context in Penang.

---

### 13. Limitations and Unsolved Problems

**Stated limitations:**
- Small sample size (n=25) — qualitative insights but not generalisable
- Absence of government officials' perspectives
- Reliance on qualitative data with potential recall and social desirability biases
- Use of translators may introduce inaccuracies
- Stakeholder perspectives (buyers, trawlers, customers) absent

**Unsolved problems / future work:**
- Need for quantitative validation with larger samples
- Need for broader stakeholder perspectives
- Need for focused studies on specific factors (social networks, income stability, credit access)
- Need for robust decision-making models that can be validated statistically

**Gaps aligned with my research problem:**

1. **No formalisation of the decision architecture:** The study maps decision factors and causal relationships but does not formalise them mathematically. My architecture provides the formal structure (E → S = f(E) → (G(S), A_AI(S)) → AI(E)) that captures the decision pipeline this study describes informally.

2. **No AI decision support considered:** The study documents human decision-making processes but does not consider how AI could support these decisions. My research directly addresses this gap by designing an AI system that supports the decision types and factors identified here.

3. **No safety state classification:** The study reveals that fishers implicitly classify conditions into go/cautious-go/no-go states, but does not formalise this classification. My S = f(E) → {SAFE, CAUTION, UNSAFE} formalises what this study describes empirically.

4. **Information asymmetry and access gaps:** The study documents that fishers rely on personal experience and social networks for information, with significant variation in decision quality. This validates the need for an AI decision support system that can provide consistent, evidence-based recommendations to all fishers.

5. **Safety-income trade-off not resolved:** The study documents that fishers sometimes prioritise economic need over safety ("I will catch as much as possible because tomorrow maybe nothing"). My architecture's Safety Dominance Property (AI(E) ⊆ A_AI(S)) ensures that AI recommendations never override safety constraints for economic optimisation — addressing a tension this study documents but cannot resolve.

---

### 16. Relation to My Research and Positioning

- **Level 1 governance implemented?** Informally yes — fishers apply environmental-state-based go/no-go gates. Not formalised.
- **Level 2 governance implemented?** Informally partial — decision scope varies by conditions but is not formalised or explicitly governed.
- **State-conditioned?** Yes, informally — both participation and scope are driven by environmental state assessment (weather, tide, fishing resources, safety).
- **Proximity to (G(S), A_AI(S))?** Provides empirical evidence for the *need* for this governance pair, and documents the informal human equivalent, but does not formalise it.
- **Formal safety property?** No. Documents safety-income trade-offs but does not define formal properties.
- **Gap my research addresses:** The study provides the empirical domain knowledge — what decisions fishers make, what factors drive them, and how environmental conditions gate decision-making — but stops at qualitative description. My research takes the next step: formalising this decision architecture, embedding AI support within it, and ensuring through the Safety Dominance Property that AI recommendations respect the safety constraints that fishers sometimes override under economic pressure.

**Positioning paragraph:**

This thesis serves as a **primary domain background reference** for my research, providing detailed empirical evidence of how small-scale fishers in a Southeast Asian coastal context actually make decisions. Its three-tier decision hierarchy (operational, strategic, collective action), the identified environmental factors with importance ratings, and the documented safety-gating behaviour empirically validate the design rationale for my AI decision support architecture. Critically, the study's environmental factors — tide (4.55), fishing resource (4.45), weather (3.75), safety concern (3.40) — map directly onto the components of my environmental state vector E = {w, r, m, o, v, t}, confirming that these are the variables fishers actually assess. The documented informal tripartite safety classification (go freely / go cautiously / don't go) empirically grounds my formal S = f(E) → {SAFE, CAUTION, UNSAFE}. The study's identification of information asymmetries, the vicious circle of resilience, and safety-income trade-offs collectively motivate the need for AI decision support that is both safety-constrained and contextually appropriate. While the study does not address AI systems, it provides the human decision-making baseline against which my AI architecture is designed — ensuring that the AI supports, rather than disrupts, the decision processes fishers already use.

---

### 17. Overall Relevance Score

## ⭐⭐ Low

**Justification:** This is an unpublished master's thesis that provides valuable domain context but does not address AI systems, governance architectures, formalisation, or any of the core technical themes of my research. Its primary value lies in empirically documenting the decision-making factors and processes in the exact domain my AI system targets (coastal small-scale fisheries, Southeast Asian low-resource context). The environmental factors and their importance ratings validate my environmental state vector composition, and the informal safety-gating behaviour empirically grounds my tripartite safety classification. However, as an unpublished thesis with a small sample (n=25), it should be cited sparingly and supplemented with peer-reviewed domain literature. Best used as **domain background evidence** in a subsection establishing how fishers currently make decisions, alongside stronger peer-reviewed sources like Wing & Woodward (2024) and the FAO reports.

**Functional role in literature review:** Domain background — empirical baseline of fisher decision-making processes in a Southeast Asian coastal SSF context. Validates environmental state vector composition and the informal existence of graduated safety-gating in human decision-making.

**Citation quality concern:** Unpublished M.Sc. thesis — not peer-reviewed, but deposited in the CGIAR/WorldFish institutional repository with persistent identifier (https://hdl.handle.net/10568/152289). This makes it citable and verifiable. Use for domain contextualisation; supplement with peer-reviewed sources for formal claims.
