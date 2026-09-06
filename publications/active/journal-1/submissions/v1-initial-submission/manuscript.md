# A Formally Verified Runtime AI Governance Architecture Based on Graduated Safety-State Gating

**Journal:** Safety Science (Elsevier) — primary target  
**Fallback:** Artificial Intelligence Review (Springer) / AI & Ethics (Springer)  
**Type:** Full research article  
**Status:** Research design phase — v1  
**Date started:** 2026-08-06  
**Target submission:** Early 2027

---

> **Note on relationship to conference paper**
> 
> The IPSci 2026 conference paper (AMICT) introduced the graduated safety-state-gated architecture and established the binary governance gap through a structured literature review. That paper is submitted and complete.
>
> This journal paper is an independent research contribution. It shares the same architecture but treats it as the subject of formal analysis, algorithmic specification, prototype implementation, and experimental validation — objectives that are distinct from the conference contribution. Approximately Sections 1–5 overlap significantly with the conference paper in topic; Sections 6–14 are essentially new research.
>
> **Conference contribution:** New architecture  
> **Journal contribution:** New architecture + formal theory + implementation + experimental evidence

---

## Author Information

- **Author:** Mohd Iskandar Samsuddin
- **Affiliation:** [Your university]
- **Email:** iskandarsamsuddin@gmail.com

---

## Abstract

*(To be written last — after all sections drafted)*

---

## Keywords

*(5–8 keywords — draft after abstract)*

---

## 1. Introduction

**Purpose:** Frame the problem and position the journal contribution distinctly from the conference paper.

**Key content to include:**
- The governance gap (binary vs. graduated) — brief, since this is established in the conference paper
- Why formal analysis, algorithms, and experiments are needed beyond the conference contribution
- The research questions this paper answers (see Research Design section below)
- Paper structure roadmap

*(Draft here)*

---

## 2. Related Work

**Purpose:** Broader and deeper than the conference paper's literature review.

**Key content to include:**
- Full comparison table of governance architectures (expanded from Table II in conference paper)
- Governance standards context: ISO 26262, IEC 61508, ICAO SAL levels, maritime safety standards
- Formal verification literature for AI systems
- Complexity results for related governance problems

> **Source:** Expand from `papers/comparison-table.md` and `papers/review-plan.md`

*(Draft here)*

---

## 3. AI Governance Foundations

**Purpose:** Establish the theoretical substrate — governance standards, formal properties, and the vocabulary the rest of the paper uses.

**Key content to include:**
- Safety governance in regulated industries: what "formally verified" means in this context
- Relevant standards: IEC 61508 SIL levels, ISO 26262 ASIL, maritime safety regulations (SOLAS, COLREGS)
- The participation / advisory scope / execution distinction formalised
- Properties required of a runtime governance mechanism: completeness, monotonicity, decidability

*(Draft here)*

---

## 4. Problem Formulation

**Purpose:** State the problem precisely and formally, distinguishing it from the conference paper's informal framing.

**Key content to include:**
- Formal statement: given E, define the requirements on a runtime governance mechanism M such that M(E) ⊆ A_AI(S)
- What "better" means: compared to what baselines, measured by what metrics
- Assumptions and scope conditions

> **Source:** `docs/canonical/appendix-c-formalisation.md` Sections C.1–C.4

*(Draft here)*

---

## 5. Formal Architecture

### 5.1 Architecture Overview

The proposed architecture formalises AI governance for departure decision support as a four-step causal pipeline:

**E → S = f(E) → (G(S), A_AI(S)) → AI(E) → Human Decision**

Each step is formally specified. The environmental–operational state vector **E** captures the observable conditions relevant to departure risk. The deterministic classification function **S = f(E)** maps E to exactly one of three safety states: SAFE, CAUTION, or UNSAFE. The governance pair **(G(S), A_AI(S))** — the core architectural contribution — then determines both whether the AI advisory system participates and what it is permitted to recommend. Finally, the AI generates recommendations **AI(E)** within the scope permitted by the governance pair, and the human decision-maker receives this output and makes the final go/no-go determination.

Human authority is unconditional and final. The architecture provides decision support; it does not automate the departure decision.

The architectural contribution resides in the governance pair (G(S), A_AI(S)). Prior governance architectures implement only a participation gate G(S): the AI is either enabled (G = 1) or disabled (G = 0). The proposed architecture adds a second governance level A_AI(S) that constrains the AI's advisory scope independently of whether it participates. Under the CAUTION state — the novel intermediate mode that binary architectures cannot express — the AI remains active (G(S) = 1) but operates within a formally restricted recommendation space. Binary architectures have no mechanism to distinguish CAUTION from SAFE: their G(S) returns 1 for both states, leaving scope entirely unconstrained in marginal conditions. The governance pair makes a formally distinct third governance position possible.

The four-step pipeline is implemented across four computationally distinct layers, described in Section 5.6. Sections 5.2–5.5 define each component of the pipeline formally. Section 6 proves the formal properties the architecture satisfies.

---

### 5.2 Environmental State Representation

The governance layer's input is a tuple of six observable parameters that together characterise the environmental and operational conditions relevant to departure safety.

**Definition 5.1 (Environmental State Vector).** The environmental–operational state vector is:

**E = (w, r, m, o, v, t)**

where:

| Symbol | Type | Domain | Meaning |
|--------|------|--------|---------|
| w | ℝ≥0 | [0, ∞) | Wind speed (sustained, knots) |
| r | Ordinal categorical | {none, light, moderate, heavy, storm} | Rainfall intensity |
| m | Ordinal categorical | {none, advisory, warning, alert} | Marine warning level |
| o | ℝ≥0 | [0, ∞) | Significant wave height (metres) |
| v | Ordinal categorical | {small, medium, big} | Vessel category, by gross registered tonnage |
| t | ℝ | [0, 24) | Time of day (hour, 24-hour clock) |

Vessel category is defined by gross registered tonnage following the Malaysian small boat classification of Yunus (2007), reproduced by Yaakob et al. (2015): small < 10 GRT, medium 10–25 GRT, big > 25 GRT. Tonnage rather than length overall is the discriminating variable because the length bands in that classification overlap — a 12 m vessel falls within both the medium and large length ranges — whereas the tonnage bands are disjoint and exhaustive.

The first four parameters (w, r, m, o) are dynamic: they vary over time and are sourced from external meteorological and marine data feeds. The specific data products, update frequencies, and spatial resolutions for each variable are implementation-level concerns addressed in Section 9. The parameter t is derived from the system clock.

The parameter v differs in kind from the other five. It is not a time-varying condition but a fixed attribute of the operator, constant across every decision episode for a given vessel. This distinction is not merely descriptive: it determines how v enters the classification. Whereas each of the five condition parameters is classified independently and contributes a term to the worst-case aggregation, v is a **conditioning parameter** — it selects the threshold set applied to wave height, rather than producing a classification of its own. Section 5.3.2 gives the formal treatment and the reasoning behind it.

**Definition 5.2 (Governance Independence).** The computation of S = f(E) and the governance pair (G(S), A_AI(S)) at Layer 2 must not depend on any output or internal state of Layer 3. All six components of E must be observable independently of the AI advisory engine.

This is a stronger requirement than simply noting that the inputs are sensor-derived. It is a formal constraint on the causal structure of the architecture: Layer 3 must not influence its own governance configuration, directly or indirectly. A governance layer whose classification could be affected by Layer 3's predictions, outputs, or learned representations would not constitute a formal safety constraint — f(E) would then be defined partly in terms of the system it is intended to govern, creating a feedback path that could undermine the Safety Dominance Property (Property 5.3). In the current architecture, all six components of E are sourced from external meteorological feeds, vessel registry records, and the system clock — none require Layer 3 participation.

*Note on the representation of t.* Time of day is encoded as a real number in [0, 24), but clock time is cyclically structured: 23:59 and 00:01 are numerically far apart while operationally adjacent. In the current architecture, Layer 2 applies only explicit interval rules to t (e.g., t ≥ 19 ∨ t < 6 for the UNSAFE partition), so the numeric discontinuity at midnight does not affect classification correctness — the partition [6, 17), [17, 19), [19, 24) ∪ [0, 6) handles the wrap-around explicitly. However, if E is used downstream in any computation involving distances, scores, or similarity measures — for example, nearest-neighbour retrieval of historical decision scenarios — t must be re-encoded as a pair of cyclic coordinates: t_sin = sin(2πt/24), t_cos = cos(2πt/24). The linear representation in Definition 5.1 is appropriate for Layer 2's threshold-based classification and must not be carried forward to any distance-based computation without this transformation.

*Fail-safe rule for missing or corrupted inputs.* Definition 5.1 assumes all six components of E are available. In low-resource coastal deployments, API calls may time out or sensor feeds may drop. To satisfy the conservative bias required of safety-critical governance, the following rule applies: if any component xᵢ ∈ E is undefined or corrupted (denoted xᵢ = ⊥), then f(E) = UNSAFE. This ensures the architecture fails toward maximum restriction rather than toward permissiveness when the information basis for classification is incomplete. The fail-safe rule is a precondition check applied before any gᵢ evaluation; it takes priority over all threshold comparisons.

The inclusion of each parameter in E is empirically grounded: w and o are the primary meteorological departure risk factors identified across three independent fisher studies in the Malaysian coastal context (Rahim et al., 2024; Gao, 2024; Yamin et al., 2025); r and m encode MET Malaysia's structured warning system; v captures the well-documented vessel-size fatality gradient across 504 IMO maritime accident reports (Dominguez-Péry et al., 2023); and t reflects empirical findings that night navigation significantly elevates both accident probability and consequence severity for small-vessel operations (Atacan & Düzbastılar, 2023).

---

### 5.3 Safety State Classification Function

#### 5.3.1 Severity Order

**Definition 5.3 (Severity Order).** Define a total strict order ≻ on the safety state set {SAFE, CAUTION, UNSAFE} as:

**UNSAFE ≻ CAUTION ≻ SAFE**

The order is transitive (UNSAFE ≻ SAFE follows by transitivity from UNSAFE ≻ CAUTION and CAUTION ≻ SAFE) and total (every pair of distinct states is ordered). It reflects increasing operational risk: UNSAFE denotes conditions in which departure is not permissible for the given vessel category and no AI advisory output is generated; CAUTION denotes marginal conditions in which AI advisory output is restricted to coarse operational guidance; SAFE denotes conditions in which all environmental parameters are within acceptable bounds and full AI advisory scope is available.

This ordering is the formal basis for the worst-case aggregation rule applied across the five condition classification functions (Section 5.3.3) and for the Monotonicity Theorem proved in Section 6.

#### 5.3.2 Per-Component Classification Functions

For each condition component xᵢ ∈ {w, r, m, o, t}, define a classification function gᵢ that maps xᵢ to a safety state in {SAFE, CAUTION, UNSAFE}. Four of these take a single argument. The fifth, g_o, takes two: significant wave height and vessel category.

**Definition 5.4 (Classification Functions).** The five condition classification functions and their threshold values are:

**Table 1. Condition classification thresholds.**

| Function | SAFE | CAUTION | UNSAFE | Basis |
|----------|------|---------|--------|-------|
| g_w(w) | w ≤ 22 kn | 22 < w ≤ 27 kn | w > 27 kn | MET Malaysia Category 1 onset 40 km/h (≈22 kn); Category 2 onset 50 km/h (≈27 kn) |
| g_r(r) | {none, light, moderate} | {heavy} | {storm} | MET Malaysia Ribut Petir (thunderstorm/cyclone) = unconditional halt |
| g_m(m) | {none} | {advisory} | {warning, alert} | MET Malaysia three-tier marine warning system |
| g_o(o, v) | *vessel-conditional* | | | See Table 1b |
| g_t(t) | 6.0 ≤ t < 17.0 | 17.0 ≤ t < 19.0 | t ∈ [19.0, 24.0) ∪ [0.0, 6.0) | Night navigation risk: highest accident probability and consequence scores (Atacan & Düzbastılar, 2023) |

**Table 1b. Vessel-conditional wave height thresholds, g_o(o, v).**

| v (GRT) | SAFE | CAUTION | UNSAFE | Basis |
|---|---|---|---|---|
| small (< 10) | o < 1.0 m | 1.0 ≤ o ≤ 1.9 m | o > 1.9 m | Jeong & Im (2023) Table 12 restriction for vessels ≤ 10 m LOA; Yaakob et al. (2015) operational limit Hs ≈ 1.25 m for a 6.54 m hull; NORDFORSK failure at SS4 (Hs ≈ 1.875 m) |
| medium (10–25) | o < 1.4 m | 1.4 ≤ o ≤ 2.8 m | o > 2.8 m | Hs_KIMO evaluated across 10–15 m LOA (1.13–1.48 m); UNSAFE boundary interpolated |
| big (> 25) | o < 1.5 m | 1.5 ≤ o ≤ 3.5 m | o > 3.5 m | MET Malaysia Category 1 maximum wave height 3.5 m; Hs_KIMO = 1.58 m at 16 m LOA |

Thresholds for g_w are anchored to MET Malaysia's published Kriteria Amaran Angin Kencang dan Laut Bergelora (Strong Wind and Rough Seas Warning Criteria, verified August 2026). Note that g_w is defined over *sustained* wind speed; fisher-interview sources frequently report gust values, and the two must not be conflated when drawing empirical corroboration.

The vessel-conditional thresholds for g_o are supported by a Three-Tier Triangulation, in which each tier contributes to a different row of Table 1b rather than to a single vessel-independent boundary.

*Tier 1 — Hydrodynamics.* Yaakob et al. (2015), applying naval architecture methods (Maxsurf, JONSWAP spectrum, NORDFORSK 1987 criteria) to two traditional Malaysian small fishing boats from the Johor coast (LOA 5.03 and 6.54 m, both < 10 GRT), established vessel-specific operability limits: the 6.54 m hull remained within NORDFORSK limits to Sea State 3 (operational ceiling Hs ≈ 1.25 m) and exceeded them at Sea State 4 (Hs ≈ 1.875 m), while the 5.03 m hull remained within limits only to Sea State 2 (ceiling Hs ≈ 0.5 m). Both passed IMO static stability criteria at every loading condition, establishing that dynamic seakeeping rather than static stability is the binding constraint — and, critically, that the binding wave height differs by vessel. This grounds the small-vessel row.

*Tier 2 — Empirical Risk.* Jeong & Im (2023), analysing 66 Korean small fishing vessel capsizing incidents over 23 years, show that 38% occurred at wave heights at or below 3 m, including incidents at Hs as low as 1.0 m. They derive a length-dependent departure restriction formula from the Wolfson Unit critical wave height framework — Hs_KIMO = √(1 + 0.4 × (0.88 × LOA)) − 1 — producing thresholds from 1.13 m at 10 m LOA to 2.07 m at 24 m LOA, and propose a graduated management scheme restricting vessels ≤ 10 m at Hs ≥ 1.0 m. Their central finding is that 82% of capsizing accidents between 2017 and 2022 occurred on days with no active weather warning, establishing that vessel-independent institutional thresholds systematically fail to capture small-vessel risk. This grounds the medium row and corroborates the small row.

*Tier 3 — State Policy.* MET Malaysia's Category 1 maximum wave height of 3.5 m anchors the big-vessel CAUTION/UNSAFE boundary, and Hs_KIMO independently returns 1.58 m at 16 m LOA — bracketing the 1.5 m SAFE/CAUTION boundary for that row.

The three tiers converge on a single conclusion: the wave height at which conditions become dangerous is a function of the vessel, not a constant. A 1.5 m threshold corresponds under Hs_KIMO to a vessel of roughly 15 m LOA; the deployment population operates vessels of 5–7 m. Applying a single institutional threshold across all vessel classes would classify a 6 m traditional hull as merely marginal in conditions well beyond its documented operability envelope.

**Why vessel category conditions a threshold rather than contributing a term.** An alternative formulation would treat vessel category as a sixth classification function g_v, assigning CAUTION to small and medium vessels and SAFE to big ones, with the result entering the worst-case aggregation alongside the five condition classifications. That formulation is rejected here, and the reason is structural rather than empirical.

Under worst-case aggregation, a term whose value is constant for a given operator establishes a floor on the output but cannot shift a boundary. If g_v(small) = CAUTION unconditionally, then f(E) ≥ CAUTION for every small vessel — but the CAUTION/UNSAFE boundary is determined entirely by the remaining terms, none of which is vessel-aware. A 5 m traditional hull and a 20 m vessel would therefore be classified UNSAFE at precisely the same wave height (3.5 m) and the same wind speed (27 kn). This contradicts Tier 1: Yaakob et al. (2015) report the 6.54 m hull exceeding NORDFORSK operability limits at Hs ≈ 1.875 m, roughly half the wave height at which such a formulation would first classify it UNSAFE. Across the 1.5–3.5 m band — precisely the range in which the CAUTION mode is intended to operate — the formulation would under-classify risk for the vessels the architecture is designed to serve.

The objection that correlated parameters would compensate, high wave heights implying high winds or an active marine warning, is not supported by the accident record. Jeong & Im (2023) report that 82% of capsizing accidents in their 2017–2022 sample occurred on days with no weather warning in force. Distant-storm swell under locally calm wind, with no issued advisory, is the specific case a vessel-independent threshold set fails to capture.

Conditioning g_o on v shifts the boundary rather than flooring the output, which is what the hydrodynamic evidence requires. It also removes a double-count: wave-related risk would otherwise be represented twice for small vessels, once through g_o and again through a constant vessel penalty.

Two consequences follow. First, a small vessel in genuinely benign conditions — Hs below 1.0 m, wind within limits, daylight, no warning — classifies SAFE and receives full advisory scope. Under the alternative formulation SAFE would be unreachable for any vessel below 25 GRT, and since the deployment population operates below 40 GRT (Yamin et al., 2025), the strict containment A_AI(SAFE) ⊃ A_AI(CAUTION) would never be exercised in the target domain. Second, the empirical sources previously invoked to justify a vessel term — the vessel-size fatality gradient across 504 IMO accident reports (Dominguez-Péry et al., 2023), the vessel capacity constraint documented by Rahim et al. (2024), and the population characterisations of Shaffril et al. (2017) and Yamin et al. (2025) — are retained. They justify setting the small-vessel thresholds conservatively: a smaller vessel warrants greater margin because the consequence of misclassification is more severe. That is an argument for tighter boundaries, not for a constant floor.

#### 5.3.3 Classification Function and Totality Theorem

**Definition 5.5 (Safety State Classification Function).** The overall classification function is:

**f(E) = max_≻ {g_w(w), g_r(r), g_m(m), g_o(o, v), g_t(t)}**

where max_≻ denotes the maximum under the severity order ≻ from Definition 5.3, returning the greatest element of the set under that order. The output S = f(E) ∈ {SAFE, CAUTION, UNSAFE}.

The aggregation is over five terms. Vessel category v appears within g_o rather than as an independent argument to max_≻, for the reasons given in Section 5.3.2.

The worst-case aggregation rule implements three strict operational principles: (i) UNSAFE dominance — if any condition classifies as UNSAFE, f(E) = UNSAFE, regardless of all others; (ii) CAUTION priority — if no condition is UNSAFE but at least one is CAUTION, f(E) = CAUTION; (iii) SAFE unanimity — f(E) = SAFE only if every condition classifies as SAFE. This reflects the non-compensatory nature of maritime safety risk: calm seas cannot compensate for extreme wind, and safe wave heights cannot compensate for a vessel operating after dark without navigation lights.

**Theorem 5.1 (Totality of f).** For all E in its domain, f(E) is defined and returns exactly one element of {SAFE, CAUTION, UNSAFE}.

Proof deferred to Section 6.1. Totality follows from exhaustive domain coverage of each gᵢ (the domain partition for each component is complete and non-overlapping) and from the fact that max_≻ over a finite totally ordered set is always defined and unique.

Totality is a necessary operational property: a classifier that could fail to return a safety state would leave the governance layer without a basis for enforcing the governance pair (G(S), A_AI(S)) at runtime.

---

### 5.4 Governance Pair: G(S) and A_AI(S)

#### 5.4.1 Recommendation Type Space

**Definition 5.6 (Recommendation Type Space).** Let R = {Go, Delay, DepartureTime, Duration} be the set of AI recommendation types available to the advisory system. *Go* advises that departure is permissible under current conditions; *Delay* advises postponement without specifying an alternative time; *DepartureTime* specifies an optimised departure window; and *Duration* specifies a recommended safe trip duration. The four types correspond to the full structure of the small-scale fisher departure decision — whether to go, when to go, and for how long.

#### 5.4.2 Level 1: AI Participation Gate G(S)

**Definition 5.7 (AI Participation Gate).** Define G : {SAFE, CAUTION, UNSAFE} → {0, 1} as:

- G(SAFE) = 1 (AI enabled)
- G(CAUTION) = 1 (AI enabled)
- G(UNSAFE) = 0 (AI disabled)

When G(S) = 0, the AI advisory engine is disabled and generates no output. When G(S) = 1, the engine is active. A binary governance architecture implements only G: it can express AI-on and AI-off but has no mechanism to express any intermediate governance position. Under SAFE and CAUTION, G(S) = 1 in both states — the participation gate alone cannot distinguish between them.

#### 5.4.3 Level 2: AI-Admissible Recommendation Space A_AI(S)

**Definition 5.8 (AI-Admissible Recommendation Space).** Define A_AI : {SAFE, CAUTION, UNSAFE} → 2^R as:

- A_AI(SAFE) = {Go, Delay, DepartureTime, Duration}
- A_AI(CAUTION) = {Go, Delay}
- A_AI(UNSAFE) = ∅

The containment chain A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ follows directly from these definitions.

#### 5.4.4 The Governance Pair

**Definition 5.9 (Governance Pair).** The architecture is governed by the pair (G(S), A_AI(S)). Table 2 summarises the governance configuration across all three safety states.

**Table 2. Governance configurations by safety state.**

| S | G(S) | A_AI(S) | Advisory scope |
|---|------|---------|----------------|
| SAFE | 1 | {Go, Delay, DepartureTime, Duration} | Full |
| CAUTION | 1 | {Go, Delay} | Restricted |
| UNSAFE | 0 | ∅ | None |

The CAUTION state is the architectural contribution. Under SAFE and CAUTION, G(S) = 1 in both — the participation gate is identical. The governance distinction between SAFE and CAUTION lies entirely in A_AI(S): under CAUTION, the admissible recommendation space contracts to {Go, Delay}, excluding DepartureTime and Duration. A binary governance architecture, having no Level 2 mechanism, cannot express this: it must either permit the full recommendation space or produce no advisory output at all.

The restriction of A_AI(CAUTION) to {Go, Delay} is operationally motivated. DepartureTime and Duration require temporal and operational precision that is unreliable when environmental conditions are marginal. A fisher who receives a specific optimised departure window during CAUTION conditions has received false precision — a recommendation whose implied confidence is not warranted by the underlying state. The CAUTION mode eliminates that false precision without disabling advisory participation entirely. The AI continues to inform the fisher that departure may be possible or should be delayed, without committing to timing or duration recommendations that exceed what the current information reliably supports.

When f(E) = CAUTION and Go ∈ A_AI(CAUTION), the advisory output presented to the fisher includes a state-dependent qualifier (e.g., "Departure is possible — exercise caution"). To be precise: Layer 3 returns the recommendation type Go ∈ R, unchanged. The qualifier string is a pure rendering operation applied at Layer 4 (the Human Decision interface), not a modification of the type. This distinction is important for formal correctness: Go under CAUTION is the same element of R as Go under SAFE — the set A_AI(CAUTION) = {Go, Delay} contains exactly those two types, with no sub-typed variants. Set containment is preserved; the qualifier is presentation logic external to the formal model.

---

### 5.5 Formal Properties

The architecture must satisfy three formal properties. All three are proved in Section 6.

**Property 5.1 (Participation Constraint).** G(S) = 0 ⟹ A_AI(S) = ∅.

When the participation gate is closed (S = UNSAFE), the admissible recommendation space must be empty. Deterministic safety classification overrides AI advisory reasoning unconditionally. This is enforced by Definition 5.7: A_AI(UNSAFE) = ∅ is a direct definition, not a runtime check. A system in which G(S) = 0 but A_AI(S) ≠ ∅ could admit advisory output despite a closed participation gate — a governance failure.

**Property 5.2 (Advisory Restriction Constraint).** S = CAUTION ⟹ A_AI(CAUTION) ⊊ A_AI(SAFE).

The CAUTION state produces a strictly smaller admissible recommendation space than SAFE. This property formally distinguishes CAUTION from SAFE: CAUTION is not SAFE with a warning label but a governance state with a reduced advisory scope. The strict subset relationship (⊊ rather than ⊆) confirms that the restriction is non-trivial — at least one recommendation type is excluded under CAUTION that is permitted under SAFE. From Definitions 5.5 and 5.7: A_AI(SAFE) \ A_AI(CAUTION) = {DepartureTime, Duration} ≠ ∅. ∎

**Definition 5.11 (AI Output Mapping).** Let AI(E) denote the set of recommendation types generated by the advisory engine for environmental state E. The mapping is defined as:

AI(E) = Reasoning Engine(E, RS(S)) &nbsp;&nbsp; if G(S) = 1  
AI(E) = ∅ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if G(S) = 0

where S = f(E). When G(S) = 0 (S = UNSAFE), the advisory engine receives no input and its output is defined as the empty set by this mapping — not merely by the engine's behaviour. This explicit definition makes the proof of Property 5.3 for the UNSAFE case immediate: AI(E) = ∅ = A_AI(UNSAFE).

**Property 5.3 (Safety Dominance Property).** For all E, AI(E) ⊆ A_AI(f(E)).

The AI can only generate recommendations within the admissible space defined by the current safety state. This is the load-bearing safety property of the architecture. It guarantees that no environmental state can elicit an AI recommendation that exceeds the admissible scope for that state. The UNSAFE case follows directly from Definition 5.11: when f(E) = UNSAFE, G(S) = 0, so AI(E) = ∅ = A_AI(UNSAFE), and ∅ ⊆ ∅ holds trivially.

Proof deferred to Section 6.3. The proof is constructive and depends only on the RS(S) rule set supply mechanism described in Section 5.6.

---

### 5.6 Layer Architecture and RS(S) Supply Mechanism

#### 5.6.1 Four-Layer Structure

The formal pipeline is implemented as four computationally distinct layers:

**Table 3. Four-layer architecture.**

| Layer | Name | Function | Computational character |
|-------|------|----------|------------------------|
| 1 | Environment Input | Produces E = (w, r, m, o, v, t) from sensors and data feeds | Observable, non-AI |
| 2 | Deterministic Governance | Computes S = f(E); derives G(S) and A_AI(S); selects RS(S) | Deterministic, O(1), threshold comparisons |
| 3 | AI Advisory Reasoning | Generates AI(E) within RS(S) | Rule-based, configured per safety state by Layer 2 |
| 4 | Human Decision | Fisher receives advisory; makes final go/no-go | Human authority, always final |

Causal flow is strictly unidirectional: Layer 1 → Layer 2 → Layer 3 → Layer 4. No feedback exists from Layer 3 to Layer 2. The advisory engine cannot influence its own governance configuration — a configuration that Layer 3 outputs could affect would not constitute a formal safety constraint. Layer 2 is computationally independent of Layer 3: if the advisory engine is unavailable, the governance layer continues to classify environmental states and can signal that no AI output is available. Governance holds independently of advisory engine availability.

Layer 1 inputs must all be observable without invoking the AI system. This is the governance independence requirement: the classification function f(E) must not depend on Layer 3 in any way. In the current architecture, all six components of E are sourced from meteorological APIs, vessel registry records, and the system clock — none require Layer 3 participation.

Layer 4 represents human authority, which is unconditional. The fisher may override any AI recommendation. The governance pair constrains what the AI can say; it does not constrain what the human can decide.

#### 5.6.2 RS(S) Rule Set Supply Mechanism

The Safety Dominance Property (Property 5.3) holds by construction rather than by runtime filtering. The construction depends on the following mechanism.

**Definition 5.10 (RS(S) Rule Set Supply).** For each safety state S, define the rule set RS(S) as the set of production rules supplied by Layer 2 to Layer 3 before any advisory reasoning begins:

- RS(SAFE) = rules producing recommendations in {Go, Delay, DepartureTime, Duration}
- RS(CAUTION) = rules producing recommendations in {Go, Delay} only
- RS(UNSAFE) = ∅ — never supplied; G(UNSAFE) = 0 disables Layer 3 entirely

Layer 3 is implemented as a production rule engine. The engine fires only rules present in the currently active RS(S). Crucially, no rule in RS(CAUTION) has a conclusion that produces DepartureTime or Duration — those recommendation types are structurally absent from the CAUTION rule set. The engine has no mechanism to generate a type for which no active rule exists. The Safety Dominance Property therefore holds by implementation: it is a structural consequence of how RS(CAUTION) is constructed, not an assertion that must be checked at runtime.

This is the formal basis for the proof by construction in Section 6.3. The distinction between construction-time enforcement and runtime filtering is material. A runtime filter applied to Layer 3 outputs — one that inspects the generated recommendation and discards it if the type is not in A_AI(S) — could fail, be bypassed, or have edge cases in which the filter condition is evaluated incorrectly. RS(S) supply eliminates these failure modes: the constraint is in place before generation begins. A correct rule engine with a correctly constructed RS(CAUTION) cannot produce DepartureTime or Duration under any input E.

The actual content of RS(SAFE) and RS(CAUTION) — the individual production rules and their conditions — is specified in Section 9 (Prototype Implementation). Section 5 only defines the supply mechanism and its governance role.

#### 5.6.3 Rule-Based Implementation at Layer 3

Layer 3 is implemented as a rule-based symbolic reasoning engine, rather than a machine learning model or large language model, for three reasons. First, the Safety Dominance Property must be provable, not merely tested: a rule-based engine with finite, explicitly defined rule sets RS(S) admits exhaustive static verification — every rule's conclusion type can be inspected against A_AI(S) at design time. A learned model does not admit this: its output space is not enumerable from its parameters. Second, the O(1) inference time of a deterministic rule engine satisfies the low-resource deployment constraints of the coastal fisheries domain, where inference may execute on commodity hardware without reliable network access. Third, governance independence is structurally maintained when Layer 3 is a deterministic rule engine: there is no learned representation that could drift, be fine-tuned, or adapt in a way that affects governance behaviour. A machine learning model at Layer 3 could, in principle, learn to produce recommendation types outside its training distribution — the rule-based engine cannot.

Full justification for the Layer 3 design decision, including formal arguments against alternative implementations, is provided in the supplementary design rationale (available from the authors).

---

### 5.7 Section Summary

Table 4 collects the formal symbols defined in this section.

**Table 4. Symbol summary for Section 5.**

| Symbol | Meaning |
|--------|---------|
| E = (w, r, m, o, v, t) | Environmental–operational state vector (Definition 5.1) |
| ≻ | Severity order: UNSAFE ≻ CAUTION ≻ SAFE (Definition 5.3) |
| gᵢ | Classification function for condition xᵢ ∈ {w, r, m, o, t} (Definition 5.4) |
| g_o(o, v) | Wave height classification, conditioned on vessel category (Definition 5.4, Table 1b) |
| S = f(E) | Safety state classification function — worst-case aggregation (Definition 5.5) |
| R | Recommendation type space {Go, Delay, DepartureTime, Duration} (Definition 5.6) |
| G(S) | AI participation gate — Level 1 governance (Definition 5.7) |
| A_AI(S) | AI-admissible recommendation space — Level 2 governance (Definition 5.8) |
| (G(S), A_AI(S)) | Governance pair — the core architectural contribution (Definition 5.9) |
| RS(S) | Rule set supplied to Layer 3 before advisory reasoning begins (Definition 5.10) |
| AI(E) | AI-generated recommendations: Reasoning Engine(E, RS(S)) if G(S) = 1; ∅ if G(S) = 0 (Definition 5.11) |

The formal pipeline:

**E → S = f(E) → (G(S), A_AI(S)) → AI(E) → Human Decision**

Section 6 proves Theorems 5.1–5.3 (Totality, Monotonicity, Safety Dominance Property) with full case analysis. Section 7 specifies the algorithms implementing f(E) and the RS(S) supply mechanism. Section 9 describes the prototype implementation, including the complete rule sets RS(SAFE) and RS(CAUTION). Section 10 presents the experimental evaluation comparing the graduated architecture against ungated and binary-gated baselines.

---

## 6. Theoretical Analysis

### 6.1 Overview

This section proves the three formal properties stated in Section 5. All proofs proceed by exhaustive case analysis over the finite state set {SAFE, CAUTION, UNSAFE} — no induction is required. The proofs are by construction: they depend only on the definitions given in Section 5, not on runtime behaviour or empirical observation.

The three theorems and their dependencies are:

- **Theorem 6.1 (Totality of f):** every environmental state E maps to exactly one safety state S. This is a necessary precondition for the other two theorems — they presuppose that f(E) is always defined.
- **Theorem 6.2 (Monotonicity of A_AI):** as the safety state becomes more severe, the AI admissible recommendation space never expands. Properties 5.1 and 5.2 follow as corollaries.
- **Theorem 6.3 (Safety Dominance Property):** the AI can only generate recommendations within the admissible space defined by the current safety state. This is the load-bearing safety theorem; it holds by construction from the RS(S) supply mechanism.

Together, the three theorems characterise the full safety behaviour of the governance pair (G(S), A_AI(S)): the classifier is total, the advisory scope tightens monotonically with risk, and AI output is bounded within that scope at every state.

---

### 6.2 Theorem 6.1: Totality of f

**Theorem 6.1 (Totality of f).** For all E in its domain, f(E) is defined and returns exactly one element of {SAFE, CAUTION, UNSAFE}.

**Proof.** It suffices to show (i) each condition classification function is total over its domain, and (ii) max_≻ over a finite totally ordered set is always defined and unique.

*(i) Totality of each classification function.*

- **g_w:** The three intervals [0, 22], (22, 27], (27, +∞) partition ℝ≥0 exhaustively with no gaps and no overlaps. Every w ∈ ℝ≥0 falls in exactly one interval. ✓
- **g_r:** The five values {none, light, moderate, heavy, storm} constitute the complete domain of r. Each value is assigned to exactly one classification (SAFE, SAFE, SAFE, CAUTION, UNSAFE respectively). ✓
- **g_m:** The four values {none, advisory, warning, alert} constitute the complete domain of m. Each is assigned to exactly one classification (SAFE, CAUTION, UNSAFE, UNSAFE respectively). ✓
- **g_o:** Two-argument, with domain ℝ≥0 × {small, medium, big}. Totality follows in two steps. First, for each fixed v, the corresponding row of Table 1b induces three intervals partitioning ℝ≥0 exhaustively with no overlap — [0, 1.0), [1.0, 1.9], (1.9, +∞) for small; [0, 1.4), [1.4, 2.8], (2.8, +∞) for medium; [0, 1.5), [1.5, 3.5], (3.5, +∞) for big. Second, {small, medium, big} is finite and exhausts the domain of v. Every pair (o, v) therefore selects exactly one row and falls within exactly one interval of that row. ✓
- **g_t:** The intervals [6.0, 17.0), [17.0, 19.0), [19.0, 24.0) ∪ [0.0, 6.0) partition [0, 24) exhaustively. Every t ∈ [0, 24) falls in exactly one interval. ✓

In each case the domain is partitioned into exhaustive, mutually exclusive subsets, each mapped to exactly one element of {SAFE, CAUTION, UNSAFE}. Each function is therefore total.

Note that the two-argument form of g_o does not weaken the argument. Parameterisation by a finite index set preserves totality provided each induced partition is itself exhaustive, which the three rows of Table 1b are by construction.

*(ii) Totality of max_≻.*

max_≻ takes the set {g_w(w), g_r(r), g_m(m), g_o(o, v), g_t(t)} ⊆ {SAFE, CAUTION, UNSAFE} and returns the greatest element under ≻ (Definition 5.3). Since ≻ is a total strict order on a finite non-empty set, the maximum always exists and is unique. ✓

Therefore f(E) = max_≻ {g_w(w), g_r(r), g_m(m), g_o(o, v), g_t(t)} is defined and returns exactly one element of {SAFE, CAUTION, UNSAFE} for all E. ∎

**Fail-safe extension.** The fail-safe rule stated in Section 5.2 (if any xᵢ = ⊥ then f(E) = UNSAFE) preserves totality: the pre-condition check maps every ⊥ input to UNSAFE before any gᵢ is evaluated, extending the domain of f to include undefined or corrupted inputs without introducing any undefined output states. ✓

**Significance.** Theorem 6.1 establishes **completeness**: the safety classifier has no undefined states — every combination of observable environmental conditions, including incomplete inputs, maps to exactly one safety state. This is a necessary operational property: a classifier that could fail to return a state would leave Layer 2 without a basis for deriving G(S) and A_AI(S) at runtime, making the governance pair unenforceable. Totality is therefore the precondition that enables the remaining two theorems.

---

### 6.3 Theorem 6.2: Monotonicity of A_AI

Formal safety architectures require that safety constraints tighten consistently as risk increases. Bloomfield & Rushby (2025) establish this as a core expectation of deterministic guards surrounding AI components; Dalrymple et al. (2024) require it of world model safety specifications under increasing uncertainty. The following theorem proves the proposed architecture satisfies this requirement.

**Theorem 6.2 (Monotonicity of A_AI).** For all S₁, S₂ ∈ {SAFE, CAUTION, UNSAFE}, if S₁ ≻ S₂ then A_AI(S₁) ⊆ A_AI(S₂).

*Informally:* as the safety state becomes more severe, the AI admissible recommendation space never expands — it either contracts or remains a subset of the less severe state's space.

**Proof.** From Definition 5.3, the severity order ≻ on {SAFE, CAUTION, UNSAFE} produces exactly three ordered pairs: (UNSAFE, CAUTION), (CAUTION, SAFE), and (UNSAFE, SAFE). We verify each case using the set definitions from Definition 5.8.

**Case 1: S₁ = UNSAFE, S₂ = CAUTION (UNSAFE ≻ CAUTION).**

A_AI(UNSAFE) = ∅ and A_AI(CAUTION) = {Go, Delay}.

∅ ⊆ {Go, Delay} holds trivially — the empty set is a subset of every set. ✓

**Case 2: S₁ = CAUTION, S₂ = SAFE (CAUTION ≻ SAFE).**

A_AI(CAUTION) = {Go, Delay} and A_AI(SAFE) = {Go, Delay, DepartureTime, Duration}.

Every element of A_AI(CAUTION) — namely Go and Delay — is also an element of A_AI(SAFE). Therefore {Go, Delay} ⊆ {Go, Delay, DepartureTime, Duration}. ✓

**Case 3: S₁ = UNSAFE, S₂ = SAFE (UNSAFE ≻ SAFE, by transitivity of ≻).**

A_AI(UNSAFE) = ∅ and A_AI(SAFE) = {Go, Delay, DepartureTime, Duration}.

∅ ⊆ {Go, Delay, DepartureTime, Duration} holds trivially. ✓

All three ordered pairs satisfy the subset condition. Theorem 6.2 holds. ∎

**Corollary 6.2 (Strict Monotonicity).** The inclusions in Cases 1 and 2 are strict: A_AI(UNSAFE) ⊊ A_AI(CAUTION) ⊊ A_AI(SAFE). This produces the containment chain:

**A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅**

The containment is not coincidental — it follows necessarily from the severity ordering on S and the set definitions of A_AI(S).

**Corollary 6.3 (Properties 5.1 and 5.2).** Both governance constraints stated in Section 5.5 follow directly.

*Property 5.1 (Participation Constraint):* G(S) = 0 ⟹ A_AI(S) = ∅. G(S) = 0 if and only if S = UNSAFE (Definition 5.7). A_AI(UNSAFE) = ∅ by Definition 5.8. Therefore G(S) = 0 ⟹ A_AI(S) = ∅. ✓

*Property 5.2 (Advisory Restriction Constraint):* S = CAUTION ⟹ A_AI(CAUTION) ⊊ A_AI(SAFE). This is precisely Case 2 of Theorem 6.2, with the strict subset confirmed by Corollary 6.2: A_AI(SAFE) \ A_AI(CAUTION) = {DepartureTime, Duration} ≠ ∅. ✓

**Significance.** Theorem 6.2 establishes **consistency**: the architecture never relaxes safety constraints as risk increases. As environmental conditions deteriorate — as S moves up the severity order — the AI advisory scope never suddenly expands. The CAUTION state is not SAFE with extra information: it is a governance state with a formally smaller and provably distinct advisory scope. Any architecture that does not satisfy Monotonicity could, in principle, permit broader AI advisory output under worse conditions than under better ones — a governance failure that Theorem 6.2 structurally prevents.

---

### 6.4 Theorem 6.3: Safety Dominance Property

**Theorem 6.3 (Safety Dominance Property).** For all E in its domain:

**AI(E) ⊆ A_AI(f(E))**

and as a special case: if f(E) = UNSAFE then AI(E) = ∅.

**Proof.** The proof proceeds by exhaustive case analysis on S = f(E), which is total by Theorem 6.1. Since S ∈ {SAFE, CAUTION, UNSAFE}, there are exactly three cases. The proof relies on four assumptions about the Layer 3 implementation, which correspond to the causal flow illustrated in Figure 2: Layer 2 supplies RS(S) to Layer 3 *before* inference begins, and Layer 3 is a deterministic rule engine that cannot generate types outside its active rule set.

- **(A1) Rule-based engine.** Layer 3 generates only recommendation types for which an active rule exists in its current rule set.
- **(A2) RS(S) supply.** Layer 2 supplies RS(S) to Layer 3 before any reasoning begins (Definition 5.10): RS(SAFE) contains only rules producing recommendations in {Go, Delay, DepartureTime, Duration}; RS(CAUTION) contains only rules producing recommendations in {Go, Delay}; RS(UNSAFE) = ∅ and is never supplied.
- **(A3) Gate enforcement.** If G(S) = 0, Layer 3 receives no input and AI(E) = ∅ (Definition 5.11).
- **(A4) Engine fidelity.** The rule engine fires only rules present in the active RS(S). No rule produces a recommendation type outside its stated conclusion.

**Case 1: f(E) = UNSAFE.**

By Definition 5.7, G(UNSAFE) = 0. By (A3), Layer 3 receives no input and AI(E) = ∅. By Definition 5.8, A_AI(UNSAFE) = ∅. Therefore AI(E) = ∅ = A_AI(UNSAFE), and in particular AI(E) ⊆ A_AI(UNSAFE). ✓

**Case 2: f(E) = CAUTION.**

By Definition 5.7, G(CAUTION) = 1, so Layer 3 is active. By (A2), Layer 3 receives RS(CAUTION), which contains only rules producing recommendations in {Go, Delay}. By (A4), the engine produces only recommendation types present in RS(CAUTION). Therefore AI(E) ⊆ {Go, Delay} = A_AI(CAUTION). ✓

**Case 3: f(E) = SAFE.**

By Definition 5.7, G(SAFE) = 1, so Layer 3 is active. By (A2), Layer 3 receives RS(SAFE), which contains only rules producing recommendations in {Go, Delay, DepartureTime, Duration}. By (A4), the engine produces only recommendation types present in RS(SAFE). Therefore AI(E) ⊆ {Go, Delay, DepartureTime, Duration} = A_AI(SAFE). ✓

In all three cases, AI(E) ⊆ A_AI(f(E)). The Safety Dominance Property holds. ∎

**Remarks.**

The proof is constructive: it depends only on the definitions of RS(S) (Definition 5.10), the gate function G(S) (Definition 5.7), and the AI output mapping (Definition 5.11) — all of which are fully under the designer's control. No runtime checking or monitoring is required.

The property holds before generation begins. RS(S) is supplied to Layer 3 as a precondition; the engine has no mechanism to generate types outside its active rule set. This is fundamentally different from a post-hoc output filter, which could fail, be bypassed, or have edge cases in which the filter condition evaluates incorrectly. The construction-time enforcement means the Safety Dominance Property is not a test result — it is a structural guarantee.

**Significance.** Theorem 6.3 establishes **effectiveness**: the safety constraints are actually enforced on the AI output. The AI cannot — by construction — produce a recommendation outside the scope defined by the current safety state. No environmental condition can cause the AI to generate DepartureTime or Duration under CAUTION, and no condition can cause any recommendation under UNSAFE. This guarantee holds for all E, not just for tested scenarios. It is the load-bearing safety guarantee of the architecture.

---

### 6.5 Composite Guarantee

The three theorems together characterise the full formal safety behaviour of the architecture.

**Table 5. Formal guarantees of the graduated safety-state-gated architecture.**

| Theorem | Guarantee | Implication |
|---------|-----------|-------------|
| 6.1 (Totality) | f(E) is defined for all E, including inputs with ⊥ | No environmental state can leave the governance layer without a safety classification |
| 6.2 (Monotonicity) | A_AI(S₁) ⊆ A_AI(S₂) whenever S₁ ≻ S₂ | Advisory scope never expands as conditions worsen; CAUTION is provably stricter than SAFE |
| 6.3 (Safety Dominance) | AI(E) ⊆ A_AI(f(E)) for all E | AI output is bounded within the admissible scope at every state, by construction |

These guarantees are independent — each is proved from definitions alone, without relying on the others — and they are cumulative. Totality ensures the governance layer always has a state to enforce. Monotonicity ensures that state appropriately restricts scope as risk increases. Safety Dominance ensures that the AI advisory engine actually respects that restriction. An architecture satisfying all three has no formally identifiable path by which an AI recommendation can exceed the scope warranted by the current environmental conditions.

Section 10 evaluates whether these formal guarantees produce correct behavioural outcomes in empirical test scenarios, comparing the graduated architecture against ungated and binary-gated baselines across the three safety states.

---

## 7. Algorithms

**Purpose:** Pseudocode for each computational component. This section does not exist in the conference paper.

**Algorithms to specify:**
- Algorithm 1: Safety classification S = f(E) — threshold evaluation with worst-case aggregation
- Algorithm 2: Governance gate evaluation — G(S) and A_AI(S) selection
- Algorithm 3: Rule set supply to reasoning engine — RS(S) construction and injection
- Algorithm 4: Runtime advisory generation — symbolic reasoning within RS(S)

**For each algorithm:**
- Inputs, outputs, preconditions, postconditions
- Pseudocode
- Invariant maintained

*(Draft here)*

---

## 8. Complexity Analysis

**Purpose:** Characterise the computational cost of the governance mechanism. This section does not exist in the conference paper.

**Key questions to answer:**
- Time complexity of S = f(E) classification
- Time complexity of A_AI(S) enforcement
- Space complexity of RS(S) rule sets
- Worst-case decision latency
- How complexity scales with |E| and |A_AI|
- Is the governance overhead acceptable for low-resource deployment?

*(Draft here)*

---

## 9. Prototype Implementation

**Purpose:** Describe the software prototype built to demonstrate the architecture. Reference RQ3 from thesis.

**Key content to include:**
- Implementation stack (low-resource constraints: offline-first, lightweight)
- How the three layers are implemented in software
- How RS(S) is encoded and supplied to the reasoning engine
- Hysteresis smoothing at state transition boundaries (mode-chattering prevention)
- Deployment environment: Kota Kinabalu, Sabah, Malaysia fisheries context

> **Source:** `docs/implementation/` documents  
> **Source:** `data/` — weather and marine data files

*(Draft here)*

---

## 10. Experimental Design

**Purpose:** Define the evaluation methodology rigorously. Reference RQ4 from thesis.

**Three-condition comparison (from `docs/canonical/evaluation-design-rq4.md`):**

| Condition | Label | Description |
|-----------|-------|-------------|
| C1 | Ungated | AI generates full-scope output regardless of S |
| C2 | Binary-gated | AI enabled/disabled, no advisory scope restriction |
| C3 | Graduated (proposed) | Full (G(S), A_AI(S)) governance pair |

**Scenarios:** Historical weather replay across SAFE, CAUTION, and UNSAFE conditions

**Metrics:**
- Advisory scope compliance rate: P(AI(E) ⊆ A_AI(S))
- False positive rate: recommendations issued outside A_AI(S)
- Decision support utility: coverage of actionable recommendations within admissible set
- Governance overhead: latency added by governance layer

**Baselines:** C1 and C2 as per evaluation design

**Statistical analysis:** [TBD — specify tests]

> **Source:** `docs/canonical/evaluation-design-rq4.md` (full design)

*(Draft here)*

---

## 11. Results

**Purpose:** Present experimental results against the three conditions and across all metrics.

*(To be written after experiments are run)*

---

## 12. Ablation Study

**Purpose:** Isolate the contribution of each architectural component.

**Ablation conditions to test:**
- Remove advisory scope restriction (A_AI(S) = full set at all states) — reduces to binary gate
- Remove participation gate (G(S) = 1 always) — removes safety disengagement
- Remove hysteresis smoothing — measures mode-chattering frequency
- Remove worst-case aggregation — measures misclassification rate at E boundary conditions

*(To be written after experiments are run)*

---

## 13. Discussion

**Purpose:** Interpret results, generalise beyond the fisheries domain, address deployment challenges.

**Key content to include:**
- What the results mean for the binary governance gap
- Generalisation: which aspects of the architecture are domain-independent
- Deployment challenges in low-resource environments: connectivity, hardware, maintenance
- Relationship to governance standards (IEC 61508, ISO 26262, SOLAS)
- Limitations of the current prototype
- How the architecture could be extended to other safety-critical domains

*(Draft after results)*

---

## 14. Threats to Validity

**Purpose:** Systematic treatment of validity threats. Required for journal submission.

**Internal validity:**
- Classification threshold selection — are the SAFE/CAUTION/UNSAFE boundaries principled?
- Rule set completeness — are RS(S) sets exhaustive for the fisheries domain?
- Prototype fidelity — does the implementation faithfully realise the formal specification?

**External validity:**
- Generalisability beyond Malaysian coastal fisheries
- Applicability to non-symbolic AI reasoning engines
- Scalability to larger E vectors

**Construct validity:**
- Does advisory scope compliance rate measure what it claims?
- Is historical weather replay a valid proxy for real deployment?

*(Draft after results)*

---

## 15. Conclusion

**Purpose:** Summarise contributions, situate within CS literature, state future work.

**Key content to include:**
- The journal contribution in one paragraph (distinct from conference paper)
- Formal properties proved
- Experimental evidence summary
- Future work: multi-domain generalisation, formal certification pathways, user study (RQ5)

*(Draft last)*

---

## References

*(To be compiled — use `docs/canonical/citation-notes-map.md` for citation keys)*

---

## Figures

*(Place figures in `/figures/` subfolder and reference here)*

**Planned figures:**
- Figure 1: Three governance dimensions (adapted from conference paper)
- Figure 2: Full architecture diagram with all four layers (expanded from conference paper Fig. 3)
- Figure 3: State transition diagram with formal notation
- Figure 4: Algorithm flow diagrams
- Figure 5: Experimental results — condition comparison across metrics
- Figure 6: Ablation results
