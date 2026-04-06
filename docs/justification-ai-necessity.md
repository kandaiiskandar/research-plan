# Why Does This Need AI? Justification for the Necessity of AI in the Architecture

**Document type**: Theoretical justification / argumentation note  
**For**: Chapter 1 (Introduction), Chapter 3 (Architecture Design), and viva preparation  
**Question addressed**: Q10 — If the governance layer is deterministic, could the whole thing work without AI? Why not just use rules?

---

## 1. The Core Claim

The governance layer of the proposed architecture — S = f(E) → (G(S), A_AI(S)) — is deterministic. It classifies environmental conditions and restricts the AI output space using rule-based logic that requires no machine learning, no neural networks, and no probabilistic inference. This is a deliberate design choice: governance must be independent of the AI it governs.

But the architecture requires AI because **governance constrains; it does not recommend**. The governance layer defines the boundary of what may be recommended. The AI reasoning layer (Layer 3) generates the actual recommendations within those boundaries. Without AI, the governance layer would constrain an empty recommendation space — a safety architecture with nothing to govern.

The question is legitimate: if the critical safety contribution is deterministic, why not make the entire system deterministic? Four alternative approaches are examined and each is shown to be insufficient for the recommendation generation task that the governance layer constrains.

---

## 2. Why Not Pure Rules for Recommendation Generation?

### 2.1 What Pure Rules Would Mean

A pure rule-based recommendation system would generate fishing recommendations using if-then rules: "If wind < 15 knots AND waves < 1.5m AND visibility > 5km, THEN recommend go with departure at high tide." Rules would be authored by domain experts and encoded into a decision tree or expert system.

### 2.2 Why Rules Fail for Recommendation Generation

**Multi-variate interaction complexity**: Fishing decisions depend on the interaction of at least six environmental parameters (wind, rainfall, marine warnings, ocean state, vessel condition, time of day), plus operational parameters (fuel, crew availability, gear type, target species, market conditions). The interaction space is combinatorial. A rule system covering all meaningful parameter combinations would require an impractically large rule base that no domain expert could author or validate.

Gao (2024), through 25 semi-structured interviews with Penang fishers, documents the complexity of fisher decision-making through causal maps revealing interconnected factors: tide (importance 4.55/5), fishing resource (4.45/5), previous catch (4.38/5), weather (3.75/5), and safety concern (3.40/5) all interact. Fisher statements reveal conditional reasoning that defies simple rule encoding: the decision to go depends on which species is targeted, which depends on season, which depends on gear available, which depends on vessel condition. No single decision tree captures this interaction structure without becoming unmanageably large.

**Continuous parameter spaces**: Departure time recommendations, trip duration estimates, and fishing area suggestions depend on continuous variables (wind speed, wave height, tide timing) in ways that cannot be discretised into rules without losing operational value. A rule saying "depart at high tide" is less useful than "depart at 06:15 when tide peaks at 06:42 with 27 minutes of favourable current." The latter requires computation over continuous parameters — the kind of interpolation and optimisation that AI provides and rules cannot.

**Temporal dynamics**: Conditions change during a fishing trip. A recommendation that was valid at departure may become invalid as weather shifts. AI can incorporate forecast trajectories and temporal patterns (learning from historical trips that afternoon wind acceleration in the Strait of Malacca typically reaches x knots by y hours after dawn). Rules encode static thresholds; AI learns dynamic patterns.

**Data-driven improvement**: A rule system is static — it does not improve with experience. An AI system learns from operational data: which recommendations led to safe, productive trips; which conditions correlated with trip curtailment; which departure times historically avoided afternoon squalls. Rahim et al. (2024) document that Indonesian fishers' own decision-making improves through experience — "older fishers with more years of experience demonstrated higher adaptive capacity scores" — and that this experiential learning is precisely what is lost when traditional knowledge erodes. AI can capture and codify this experiential pattern recognition in a way that static rules cannot.

### 2.3 The Boundary

Rules are *exactly right* for the governance layer — classifying environmental state and restricting AI scope — because the governance function is categorical and finite: three states, a fixed containment hierarchy, threshold-based classification. Rules are *exactly wrong* for the recommendation layer because the recommendation function is continuous, multi-variate, and benefits from learning.

---

## 3. Why Not Traditional Knowledge Alone?

### 3.1 What Traditional Knowledge Provides

Traditional knowledge (TK) — also termed local ecological knowledge (LEK) or indigenous knowledge — is the cumulative body of knowledge, practice, and belief about the marine environment developed by small-scale fishing communities through generations of observation and experience. TK includes weather prediction from natural indicators (cloud patterns, wind direction, animal behaviour), understanding of tidal and seasonal patterns, knowledge of fishing ground locations and species behaviour, and risk assessment heuristics.

### 3.2 Why TK Alone Is Insufficient

**TK is eroding**. Yamin et al. (2025), in a primary survey of 136 small-scale fishers in central Terengganu — the exact target population — document that traditional weather prediction ability is declining as climate unpredictability intensifies. The study finds that fishers increasingly rely on weather apps (Windy, Windfinder) for raw data, but these apps provide environmental information without translating it into scope-restricted decision support. This creates a *decision support vacuum*: the traditional knowledge that previously informed intermediate-risk decisions is weakening, and no formal system fills the gap. The proposed architecture, with its CAUTION mode, is designed to fill precisely this vacuum.

**Climate change invalidates historical patterns**. Yamin et al. (2025) find near-unanimous fisher-reported identification of climate hazards: stronger monsoonal winds and larger waves (95%), more intense weather events (91%), and erratic rainfall patterns (91%). These findings document that the environmental patterns on which TK is built are changing. Historical knowledge that "the east wind brings calm seas in April" becomes unreliable when climate patterns shift. AI, trained on recent data and updateable with new observations, can adapt to changing environmental patterns in ways that inherited TK cannot.

**TK is binary**. Yamin et al. (2025) document that the empirical knowledge item "I know if it's suddenly windy/change of weather, I can't go fishing" is the dominant decision heuristic. This is binary: go or don't go. Gao (2024) documents a tripartite informal classification (go, cautious-go, don't-go) in Penang — but the cautious-go decision is made intuitively, without formal support, and Gao's study shows this intermediate decision draws on tacit pattern recognition that younger and less experienced fishers may not possess. The proposed architecture formalises the intermediate decision mode and supports it with AI-generated recommendations within the restricted scope.

**TK does not scale across individuals**. The experiential knowledge of a 40-year veteran fisher is not transferable to a 20-year-old new entrant through any documented mechanism in the fisheries literature. Rahim et al. (2024) find that "fishers with more years of experience demonstrated higher adaptive capacity" — but this relationship is individual. AI can aggregate patterns across many fishers' experiences and make them available to all users, including those who lack the decades of personal observation that TK requires.

### 3.3 The Complementary Relationship

The proposed architecture does not replace TK — it formalises the governance structure that TK provides intuitively (the go/cautious-go/don't-go classification) and supplements the recommendation function where TK is eroding. The governance layer (S = f(E)) encodes domain-validated environmental thresholds — the same thresholds that experienced fishers apply intuitively. The AI layer provides the detailed recommendations (departure timing, trip duration, fishing area selection) that experienced fishers derive from tacit pattern recognition but that less experienced fishers lack access to. The architecture thus bridges the TK erosion gap that Yamin et al. (2025) document as a population-level adaptive capacity deficit.

---

## 4. Why Not Lookup Tables?

### 4.1 What Lookup Tables Would Mean

A lookup table approach would pre-compute recommendations for every combination of environmental parameters: "If wind = 15–20 knots AND waves = 1.0–1.5m AND tide = rising AND season = west, THEN departure = high tide + 30min, duration = 4 hours, area = zone B." This is deterministic, requires no AI, and could be encoded on a laminated card.

### 4.2 Why Lookup Tables Fail

**Combinatorial explosion**: With six environmental parameters, each discretised into even five levels, the lookup table has 5^6 = 15,625 entries. Adding operational parameters (vessel type, gear, crew size, target species) multiplies this further. Each entry requires a validated recommendation — authored by whom? Validated against what data? The table becomes unmanageably large and unvalidatable.

**Loss of continuous precision**: Discretising continuous parameters into table buckets loses the precision that makes recommendations operationally useful. "Depart between 06:00 and 07:00" is less useful than "depart at 06:15 given current tide and forecast wind." AI interpolates continuously; tables discretise.

**No temporal reasoning**: Lookup tables cannot incorporate forecast trajectories, temporal trends, or dynamic condition changes. A table encodes current conditions → static recommendation. AI encodes current conditions + forecast + historical patterns → dynamic recommendation. Rahim et al. (2024) document that the most effective fisher adaptive strategies involve temporal adjustments — shifting from 5–6 trips per week to 2–3, and from 7–10 hours to 3–5 hours — decisions that require assessment of temporal condition evolution, not point-in-time lookup.

**No learning**: A lookup table, like a rule system, does not improve with operational experience. It cannot learn that "trips departing after 07:00 in March have a 23% higher early return rate due to wind acceleration." AI learns these patterns from operational data.

**Maintenance burden**: Environmental conditions, seasonal patterns, and fishing ground productivity change over time. A lookup table requires manual updating by domain experts — experts who may not exist in the target community. Yamin et al. (2025) document that only 58% of fishers consider alternative livelihood strategies and 67.6% rely solely on fishing income — these are not populations with resources for systematic lookup table maintenance.

### 4.3 The Boundary

Lookup tables are functionally equivalent to the governance layer's classification function f(E) for a small number of parameters and discrete outputs — which is precisely what f(E) is. The classification SAFE/CAUTION/UNSAFE from six parameters with defined thresholds could be implemented as a lookup table. This is fine for governance because the output is categorical (three states) and the parameter space is manageable. It does not work for recommendation generation because the output is continuous and multi-variate.

---

## 5. Why Not a Warning-Only System?

### 5.1 What a Warning-Only System Would Mean

A warning-only system would classify environmental conditions (SAFE/CAUTION/UNSAFE) and communicate the classification to the fisher — without generating any recommendations. The fisher would receive "CAUTION: winds 22 knots, waves 2.1m" and make their own decisions. This is the governance layer without the AI layer.

### 5.2 Why Warnings Alone Are Insufficient

**Binary warnings are already ignored**. Rahim et al. (2024) document that Indonesian fishers routinely override binary "do not sail" warnings from the Ministry of Maritime Affairs (KKP) because these warnings do not accommodate the adaptive scope restriction behaviour fishers actually employ. Fishers do not need to be told "conditions are dangerous" — they can observe conditions directly. What they need is decision support for the intermediate case: "given that conditions are elevated, should I go at all? If so, when and for how long?" A warning system provides the first but not the second.

**Warnings do not fill the TK erosion gap**. The decision support vacuum documented by Yamin et al. (2025) is not a lack of warning — fishers know when conditions are dangerous. The vacuum is in the *decision logic* for intermediate conditions: what to do when conditions are neither clearly safe nor clearly dangerous. Warning-only systems leave this vacuum unfilled. The proposed architecture fills it by providing scope-restricted AI recommendations under CAUTION conditions — go/no-go and delay guidance that supports the intermediate decision without providing false-precision detailed recommendations.

**Warnings do not exploit available data**. Small-scale fisheries are data-scarce relative to commercial operations, but operational data does exist: historical catch data, trip logs, weather records, satellite oceanography. A warning-only system ignores this data. AI can learn from it to generate recommendations that are more informative than the raw environmental parameters alone. The value proposition of AI in this context is precisely its ability to convert heterogeneous data sources into actionable recommendations — something warnings cannot do.

**The governance layer alone has no operational value**. A classification S ∈ {SAFE, CAUTION, UNSAFE} with no downstream recommendations is a weather warning system, not a decision support system. The research contribution is not the classification — environmental risk classification exists in every maritime warning system. The contribution is the *governance pair* (G(S), A_AI(S)) that connects classification to AI advisory scope restriction. Without the AI layer, A_AI(S) constrains nothing; G(S) gates nothing; the governance pair is vacuous.

### 5.3 The Structural Argument

The governance layer without the AI layer is a safety classification system. The AI layer without the governance layer is an unconstrained DSS. Neither alone solves the problem. The contribution is their *integration* — the formal mechanism by which environmental state classification constrains AI advisory scope. This integration requires both layers: deterministic governance *and* AI recommendation generation.

---

## 6. The Architectural Separation: Why Governance Is Deterministic While Recommendations Require AI

### 6.1 Different Functions, Different Computational Requirements

The governance function and the recommendation function have fundamentally different computational characters:

| Property | Governance function (Layer 2) | Recommendation function (Layer 3) |
|---|---|---|
| **Input** | Environmental parameters (6 variables) | Environmental parameters + operational context + historical data |
| **Output** | Categorical: S ∈ {SAFE, CAUTION, UNSAFE} | Continuous: departure time, duration, area, go/no-go |
| **Logic** | Threshold-based classification | Multi-variate interpolation, pattern recognition, optimisation |
| **Learning** | Not needed — thresholds are domain-validated | Essential — patterns are data-derived and evolve |
| **Verifiability** | Exhaustively testable (finite input-output space) | Statistically validated (infinite input-output space) |
| **Assurance** | Conventional software engineering | Probabilistic AI assurance methods |
| **Failure consequence** | Wrong governance mode → wrong scope | Wrong recommendation → wrong decision |
| **Independence requirement** | Must be independent of AI | May depend on any data source |

### 6.2 Why This Separation Matters

The separation is not a convenience — it is a formal requirement for the Safety Dominance Property to be provable.

**Provability**: The property AI(E) ⊆ A_AI(S) requires that A_AI(S) is determined independently of AI(E). If the same probabilistic system both generated recommendations and determined the scope within which recommendations were permissible, the proof would be circular: "the AI's output is within the scope that the AI determined for itself." Dalrymple et al. (2024) specify this independence requirement in the Guaranteed Safe AI framework: the verifier must produce proof certificates independently of the AI policy. Bajcsy & Fisac (2024) prove their safety filter guarantee (Theorem 1) under the analogous requirement that the safety monitor be computed independently of the task policy. The architectural separation satisfies both requirements.

**Assurability**: Bloomfield & Rushby (2025) define *assuredly guarded* systems as those whose guards "do not themselves use AI/ML and can therefore be assured conventionally." The deterministic governance layer is assuredly guarded by this definition. An AI-based governance layer would be *unassuredly guarded* — dependent on the same type of system it is supposed to constrain.

**Robustness**: If the AI component fails (model degradation, data pipeline interruption, hardware fault), the governance layer continues to function. S = f(E) still classifies environmental state from sensor inputs. G(S) still determines whether AI should participate. A_AI(S) still defines the permissible scope. The governance layer does not need the AI layer to function — it needs the AI layer only to have something to govern. This means the safety properties of the architecture survive AI failure: in the worst case (AI unavailable), G(S) = 0 for all S and the system safely reverts to unassisted human decision-making.

### 6.3 The Necessity Argument Stated Precisely

1. The governance layer must be deterministic (for provability, assurability, and robustness)
2. The governance layer constrains recommendation scope, but does not generate recommendations
3. Recommendation generation requires AI (because rules, lookup tables, TK alone, and warnings alone are insufficient for multi-variate, continuous, learning-capable recommendation generation in this domain)
4. Therefore, the architecture requires both: deterministic governance AND AI recommendation generation
5. The contribution is their formal integration — the governance pair (G(S), A_AI(S)) that connects deterministic state classification to AI output space restriction

The architecture could not work without AI because the governance layer would have nothing to govern. The architecture could not work without deterministic governance because the AI would have no formal safety constraints. Both layers are necessary; neither is sufficient alone.

---

## 7. Comparative Summary Table

| Alternative (no AI) | What it provides | What it lacks | Why AI is necessary |
|---|---|---|---|
| **Pure rules** | Categorical decisions (go/no-go) | Continuous recommendations, multi-variate interaction handling, learning from experience | Recommendation generation over continuous parameter spaces with complex interactions exceeds rule system capacity |
| **Traditional knowledge alone** | Decades of experiential pattern recognition | Transferability across individuals, adaptation to climate change, support for less experienced fishers | TK is eroding (Yamin et al., 2025), binary (Yamin et al., 2025; Gao, 2024), non-transferable (Rahim et al., 2024) |
| **Lookup tables** | Deterministic mapping from discretised conditions to pre-computed recommendations | Continuous precision, temporal reasoning, learning, maintenance feasibility | Combinatorial explosion, loss of precision, no adaptation to changing patterns |
| **Warnings only** | Environmental state classification communicated to the human | Actionable recommendations, TK erosion gap filling, data exploitation | Warnings are already ignored (Rahim et al., 2024); decision support vacuum exists at intermediate conditions (Yamin et al., 2025) |

---

## 8. One-Paragraph Summary (for use in Chapter 1 or Chapter 3)

> The governance layer of the proposed architecture is deterministic — S = f(E) classifies environmental conditions into safety states using rule-based threshold logic — but the architecture requires AI because governance constrains recommendation scope without generating recommendations. Four alternatives to AI-based recommendation generation are insufficient: pure rules cannot handle the multi-variate continuous parameter interactions documented in fisher decision-making (Gao, 2024), where tide, weather, species targeting, and gear selection interact in ways that defy tractable rule encoding; traditional knowledge alone is eroding under climate change — Yamin et al. (2025) document declining weather prediction ability, near-universal recognition of intensifying hazards (95% wind/waves, 91% weather events), and a decision support vacuum at intermediate risk states that no existing system fills; lookup tables face combinatorial explosion when discretising six environmental parameters and multiple operational parameters, lose the continuous precision that makes recommendations operationally useful, and impose a maintenance burden unsustainable in low-resource communities; and warning-only systems replicate the binary governmental warnings that Rahim et al. (2024) document are routinely overridden by fishers who adaptively self-restrict scope rather than cease fishing entirely. The architectural separation between deterministic governance (Layer 2) and AI recommendation generation (Layer 3) is not merely convenient but formally necessary: the Safety Dominance Property AI(E) ⊆ A_AI(S) requires that the admissible recommendation space be determined independently of the AI output it constrains, satisfying the independence requirement specified by Dalrymple et al. (2024) and Bajcsy & Fisac (2024) for formal safety guarantees, and meeting Bloomfield & Rushby's (2025) criterion for *assuredly guarded* systems. Without AI, the governance layer constrains an empty recommendation space — a safety architecture with nothing to govern. Without deterministic governance, the AI operates without formal safety constraints — a DSS with no safety guarantee. The contribution is their formal integration: the governance pair (G(S), A_AI(S)) that connects deterministic environmental state classification to AI advisory scope restriction, enabling graduated decision support under conditions where both unconstrained AI and the absence of AI are inadequate.
