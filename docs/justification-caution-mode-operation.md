# How Does CAUTION Work? Operational Design, Scope Definition, and Human Factors

**Document type**: Theoretical justification / argumentation note  
**For**: Chapter 3 (Architecture Design), Chapter 5 (Evaluation), and viva preparation  
**Questions addressed**: What does AI do differently in CAUTION? What recommendations are allowed? How is restricted scope defined? Is CAUTION like degraded mode? What if CAUTION persists? Does it increase cognitive load? How do users distinguish SAFE from CAUTION? Is CAUTION domain-general?

**Cross-references**: For why the CAUTION state exists (not binary), see `justification-three-states.md`. For why CAUTION restricts scope rather than blocking AI or reducing autonomy, see `justification-advisory-scope-restriction.md`. For CAUTION's risk management theoretical foundations (ALARP, VOI, bounded rationality, trust calibration), see `justification-advisory-scope-restriction.md` §4.

---

## 1. What Does AI Do Differently in CAUTION Compared to SAFE?

### 1.1 The Operational Difference

In SAFE, the AI generates recommendations from the full recommendation space R = {Go, Delay, DepartureTime, Duration}. In CAUTION, the AI generates recommendations from a restricted subset A_AI(CAUTION) ⊂ R.

The difference is not in the AI's computational method — the same model, the same inference engine, the same data sources may be used. The difference is in the **output space**: the governance layer prevents certain recommendation *types* from reaching the user, regardless of whether the AI could technically generate them.

| Capability | SAFE | CAUTION | UNSAFE |
|---|---|---|---|
| Go/no-go directional guidance | Yes | **Yes** | No |
| Delay guidance (wait, defer to tomorrow) | Yes | **Yes** | No |
| Departure time (depart at 06:15) | Yes | **No** | No |
| Trip duration estimate (return by 14:00) | Yes | **No** | No |

### 1.2 Why These Specific Recommendations Are Retained or Suppressed

The partition of R into retained and suppressed recommendation types under CAUTION is not arbitrary. It follows the principle that different recommendation types have different **reliability envelopes** — the range of environmental conditions under which they remain accurate:

**Retained in CAUTION — Go/no-go directional guidance**: This recommendation depends on threshold-crossing logic: are conditions above or below the level where fishing is advisable? Threshold-crossing assessments are robust to moderate environmental uncertainty because they depend on the *direction* of conditions relative to a boundary, not on precise estimation. Even when environmental data is partially degraded (under CAUTION conditions), the AI can reliably assess whether conditions are above or below the go/no-go threshold.

**Retained in CAUTION — Delay guidance**: This recommendation depends on trend assessment: are conditions improving, stable, or deteriorating? Trend direction is robust to moderate uncertainty because it requires only ordinal comparison (better/worse), not cardinal precision. "Wait — conditions expected to improve by afternoon" is a reliable recommendation under CAUTION because it depends on forecast *direction*, not forecast *precision*.

**Suppressed in CAUTION — Departure time**: This recommendation requires precise sea-state estimation and temporal modelling. "Depart at 06:15 when tide peaks at 06:42 with 27 minutes of favourable current" depends on accurate predictions of multiple continuous variables at specific future time points. Under CAUTION conditions, the environmental uncertainty that triggered the CAUTION classification degrades precisely these fine-grained temporal predictions. The recommendation's apparent precision would be false.

**Suppressed in CAUTION — Trip duration estimate**: This recommendation requires reliable modelling of how conditions will evolve throughout the trip — a longer temporal horizon than departure timing, making it even more susceptible to the environmental uncertainty that triggered CAUTION.

### 1.3 The Formal Expression

Formally:

```
R = {Go, Delay, DepartureTime, Duration}
A_AI(SAFE) = R = {Go, Delay, DepartureTime, Duration}
A_AI(CAUTION) = {Go, Delay}
A_AI(UNSAFE) = ∅
```

The containment property holds: A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅

Each recommendation type r ∈ R is either permitted or not permitted in a given state — there is no partial permission or confidence-weighted inclusion. This discreteness is essential for both formal tractability and user interpretability.

---

## 2. How Is Restricted Advisory Scope Formally Defined?

### 2.1 Set-Theoretic Definition

The admissible advisory space A_AI(S) is a set-valued function mapping each safety state to a subset of the recommendation type space R:

```
A_AI: {SAFE, CAUTION, UNSAFE} → P(R)
```

where P(R) is the power set of R. The function satisfies three formal requirements:

1. **Full scope at SAFE**: A_AI(SAFE) = R
2. **Empty scope at UNSAFE**: A_AI(UNSAFE) = ∅
3. **Strict containment**: A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE)

### 2.2 What "Restriction" Means Architecturally

Advisory scope restriction is **pre-hoc output space definition**, not post-hoc output filtering:

| Mechanism | When it acts | What it constrains | Analogy |
|---|---|---|---|
| **Post-hoc filtering** (guardrails) | After AI generates output | Individual output content | Censoring a letter after it's written |
| **Pre-hoc scope definition** (proposed) | Before AI generates output | Categories of output permitted | Defining what topics the letter may address |

In a guardrail system, the AI generates a departure time recommendation and the guardrail evaluates whether to deliver it. In the proposed architecture, the governance layer defines that departure time recommendations are *not in the output space* under CAUTION — the AI is architecturally prevented from generating them. The distinction matters for formal provability: the Safety Dominance Property AI(E) ⊆ A_AI(S) is satisfied by construction when the output space is defined before generation, rather than depending on a filter that might fail.

Shamsujjoha et al. (2025) [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md) catalogue 13 guardrail action types — block, filter, flag, modify, validate, etc. — all of which operate post-hoc on generated outputs. The proposed architecture's scope restriction is not in their taxonomy because it operates at a different architectural point: defining the output space rather than filtering within it. Chen et al. (2025) [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md) define AI Safety Principle I as Y ∩ Z_i = ∅ — the output must be disjoint from prohibited sets — but Z is static. In the proposed architecture, the prohibited set varies by state: Z(CAUTION) = R \ A_AI(CAUTION) = {DepartureTime, Duration}, while Z(SAFE) = ∅ and Z(UNSAFE) = R.

### 2.3 Extensibility of R

The recommendation type space R = {Go, Delay, DepartureTime, Duration} is defined for the coastal fisheries domain. In other domains, R would contain different recommendation types, and A_AI(CAUTION) would retain the types whose reliability is robust to elevated environmental uncertainty while suppressing those that degrade. The formal structure — containment hierarchy over a domain-specific R — is domain-general; the content of R and the partition into retained/suppressed types is domain-specific. See §7 below.

---

## 3. Is CAUTION Similar to Degraded Mode in Safety Systems?

### 3.1 The Comparison

Safety-critical systems commonly implement degraded modes — reduced-functionality operation when full capability is compromised. The comparison to CAUTION is natural but imprecise.

### 3.2 What Degraded Mode Is

In safety engineering, degraded mode is a system response to *internal* failure: sensor loss, component fault, software error, hardware degradation. The system detects that its own capability is reduced and adjusts operation accordingly. Gyllenhammar et al. (2025) [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md) document the MRC/ROD hierarchy in automated driving: the Restricted Operational Domain (ROD) is an intermediate state between full ODD operation and the Minimal Risk Condition (MRC), triggered by system degradation such as sensor failure or actuator fault.

Flehmig et al. (2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md) implement the closest analogue: a traffic-light degradation index triggered by AI performance degradation. At Level 2 (orange), AI shows signs of degradation — concept drift, performance decline — and the supervisory component must conduct enhanced monitoring. This is degraded mode: the system responds to evidence of its own reduced capability.

### 3.3 Why CAUTION Is Not Degraded Mode

CAUTION is triggered by *external* environmental conditions, not by internal system degradation. The AI model may be operating perfectly — no drift, no faults, full capability — and the system still enters CAUTION because the *environment* has changed. The distinction is between:

| Property | Degraded mode | CAUTION mode |
|---|---|---|
| **Trigger** | Internal system fault/degradation | External environmental conditions |
| **What changes** | System capability is reduced | Environment becomes more dangerous |
| **AI model status** | Compromised | Fully operational |
| **Governance response** | Reduce system operation to match reduced capability | Restrict advisory scope to match environmental conditions |
| **Resolution** | Fix the fault, restore capability | Wait for conditions to improve |
| **Formal trigger** | Performance metric below threshold | S = f(E) → CAUTION |

Flehmig et al. (2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md) make this distinction operationally clear: their Level 2 is triggered when "the AI's performance falls below the acceptance criteria" — an AI-performance trigger. The proposed CAUTION mode is triggered when environmental conditions cross safety thresholds — an environment trigger. The AI at CAUTION may have performance that would be Level 1 (green) in Flehmig's framework; it is the *situation*, not the *system*, that has changed.

### 3.4 The Structural Analogy That Does Hold

CAUTION is analogous to degraded mode in one important respect: both provide a **proportionate intermediate response** between full operation and shutdown. Degraded mode recognises that "fault detected → shut down entirely" is disproportionate when reduced-but-useful operation is possible. CAUTION recognises that "conditions elevated → block AI entirely" is disproportionate when restricted-but-useful advisory scope is possible.

The ALARP principle applies to both: risk should be reduced to the lowest level that is *reasonably practicable*, not the lowest level that is *technically possible*. Full shutdown when reduced operation is adequate violates ALARP. Perez-Cerrolaza et al. (2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) confirm that binary blocking creates its own hazards: "excessive false alarms could lead to new system-level hazards" including cognitive overload. CAUTION and degraded mode both apply the same proportionality principle — but to different triggers (environment vs. system fault) governing different responses (scope restriction vs. capability reduction).

---

## 4. What Happens If the System Stays in CAUTION for a Long Time?

### 4.1 The Concern

An examiner might worry that sustained CAUTION creates a problematic steady state: the system provides only go/no-go and delay guidance for days or weeks during monsoon season, degrading user trust or creating habituation to restricted mode.

### 4.2 Why Sustained CAUTION Is Expected and Acceptable

**Sustained CAUTION reflects sustained environmental reality.** During the Malaysian northeast monsoon (November–February), environmental conditions are persistently elevated. Rahim et al. (2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) document that during the analogous West season in Indonesia, fishers reduce trip frequency from 5–6 to 2–3 per week and trip duration from 7–10 hours to 3–5 hours — for the entire season. Yamin et al. (2025) [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md) document that operating days during monsoon are reduced by up to 90%. Sustained CAUTION governance mirrors this sustained operational reality. The system is not "stuck" in CAUTION — CAUTION *is* the correct governance mode for the prevailing conditions.

**Go/no-go and delay guidance remain valuable during sustained CAUTION.** The CAUTION mode's retained recommendations (go/no-go, delay) are precisely the decisions fishers face daily during monsoon: should I fish today? Should I wait for tomorrow? The value of these recommendations does not diminish with time. If anything, sustained CAUTION makes daily go/no-go guidance *more* valuable: during extended periods of elevated conditions, each day's decision is higher-stakes than during calm weather.

**The alternative (sustained AI blocking) is worse.** If the architecture were binary (SAFE/UNSAFE only), the same sustained environmental conditions would trigger sustained AI withdrawal — no decision support at all for weeks or months. Fishers would face the full monsoon season without any AI guidance. The CAUTION mode provides sustained reduced-scope guidance rather than sustained absence of guidance.

### 4.3 Trust During Sustained CAUTION

McGrath et al. (2025 — CHAI-T) [[notes]](../notes/Collaborative%20Human-AI%20Trust%20(CHAI-T)-%20A%20Process%20Framework%20for%20Active%20Management%20of%20Trust%20in%20Human-AI%20Collaboration.md) establish that trust requires stable, predictable system behaviour. A system that consistently operates in CAUTION during monsoon conditions *is* predictable and stable — it matches the operational reality. The trust risk is not sustained CAUTION but *oscillation* between modes. Sustained CAUTION, punctuated by transitions to SAFE during clear-weather windows, creates a predictable pattern aligned with the physical environment.

Schrills et al. (2025) [[notes]](../notes/Questioning%20Trust%20in%20AI%20Research-%20Exploring%20the%20Influence%20of%20Trust%20Assessment%20on%20Dependence%20in%20AI-Assisted%20Decision-Making.md) find that users calibrate their reliance to communicated system capability. Under sustained CAUTION, users calibrate to the restricted advisory scope — expecting go/no-go and delay guidance, not expecting departure times or trip durations. This is appropriate trust calibration, not degraded trust.

---

## 5. Does CAUTION Increase Cognitive Load on the Human User?

### 5.1 The Concern

An examiner might argue that having three governance modes (SAFE/CAUTION/UNSAFE) increases the cognitive burden on users compared to binary (AI on/off) because users must track which mode the system is in and understand what each mode means.

### 5.2 Why CAUTION Reduces Net Cognitive Load

The concern confuses *mode tracking* load (which increases by one mode) with *decision-making* load (which decreases significantly under CAUTION). The net effect is a reduction in cognitive load for three reasons:

**CAUTION removes the meta-cognitive assessment burden.** Without scope restriction, the user receives all recommendation types and must assess *for each one* whether to trust it given current conditions. Under CAUTION, the architecture performs this meta-cognitive assessment: "departure time recommendations are unreliable under these conditions, so they are suppressed." The user does not need to evaluate whether a departure time recommendation is trustworthy — it simply is not presented. This removes the most cognitively demanding aspect of using a DSS under elevated conditions.

Mussi et al. (2025), reviewing human-AI interaction across power grid, railway, and air traffic management domains, propose "progressive disclosure" as a design principle for safety-critical systems — delivering information in phases to avoid cognitive overload. CAUTION mode operationalises progressive disclosure at the output level: under elevated conditions, the AI discloses only what the human can usefully process.

**Unreliable information is actively harmful.** Wen et al. (2025), analysing 60 real-world accident reports, find that human intervention was ineffective in 83.3% of process control incidents and 66.7% of autonomous vehicle incidents. A recurring pattern is operators processing excessive or unreliable information under time pressure and making worse decisions than if they had received less information. Removing unreliable recommendation types reduces the information processing burden during the moments when the user's cognitive capacity is most constrained.

**Three modes map to an existing cognitive grammar.** The proceed/caution/stop grammar is universally understood and does not require training. Traffic lights, maritime navigation marks, and construction site signage all use the same three-level schema. Wen et al. (2025) document that mode confusion — misidentifying which operational mode the system is in — contributed to 13.3% of process control failures and 10.0% of autonomous vehicle failures. But mode confusion is a problem of *many subtle modes*, not of three highly distinct modes. The SAFE/CAUTION/UNSAFE distinction is maximally distinguishable — each mode has a qualitatively different governance configuration that produces visibly different system behaviour (full recommendations / reduced recommendations / no recommendations).

### 5.3 The One-Mode-Tracking Cost

CAUTION does add one cognitive requirement: the user must understand that the system is in CAUTION and what that means. This is a one-time learning cost, not an ongoing cognitive burden. Once the user understands "CAUTION means I get go/no-go and delay guidance only — no departure times or trip durations," the mode is self-explaining through its output. The system's behaviour — the visible restriction of what it recommends — continuously communicates the mode.

Bach et al. (2024) [[notes]](../notes/A%20Systematic%20Literature%20Review%20of%20User%20Trust%20in%20AI-Enabled%20Systems-%20An%20HCI%20Perspective.md), reviewing 23 empirical studies on user trust in AI systems, find that "expectation mismatch between user expectations and system capabilities" is a primary risk to trust. CAUTION prevents this mismatch by making the system's current capability boundary explicit: the user knows exactly what the AI is and is not providing. An unconstrained system that provides all recommendation types at varying (but undisclosed) reliability levels creates far greater expectation mismatch.

---

## 6. How Do Users Understand the Difference Between SAFE and CAUTION?

### 6.1 Three Communication Channels

The difference between SAFE and CAUTION is communicated through three simultaneous channels:

**Channel 1 — Explicit state label**: The system communicates the current governance mode (SAFE/CAUTION/UNSAFE) directly. This is the primary mode awareness mechanism. The label maps to the universal proceed/caution/stop grammar that requires no technical training.

**Channel 2 — Environmental rationale**: The system displays the environmental conditions that triggered the governance mode: "CAUTION: Wind 22 knots, Waves 2.1 m." This allows the user to independently verify the governance classification against their own perception — a fisher who feels calm conditions while the system shows CAUTION can identify a potential error. Atf & Lewis (2026) [[notes]](../notes/Is%20Trust%20Correlated%20With%20Explainability%20in%20AI%3F%20A%20Meta-Analysis.md) distinguish between "trust enforcement" (presenting selective data to instil trust) and "trust empowerment" (providing all relevant information for the user to calibrate trust independently). Environmental rationale is a trust empowerment mechanism.

**Channel 3 — Behavioural difference**: The system's output *visibly changes* between modes. In SAFE, the user receives four recommendation types (go/no-go, delay, departure time, duration). In CAUTION, they receive two (go/no-go, delay). The absence of departure time and duration recommendations is itself a communication: the system is telling the user, through its behaviour, that those recommendation types are not reliable under current conditions.

### 6.2 Why Behavioural Difference Is the Strongest Channel

Schrills et al. (2025) [[notes]](../notes/Questioning%20Trust%20in%20AI%20Research-%20Exploring%20the%20Influence%20of%20Trust%20Assessment%20on%20Dependence%20in%20AI-Assisted%20Decision-Making.md) find that "instructed reliability appears to be more influential in determining behaviour compared to assessed trust." The CAUTION mode's restricted output functions as an instructed reliability signal — by providing only go/no-go and delay guidance, the architecture communicates that these are the reliable recommendation types under current conditions. The user's reliance behaviour anchors to this communicated scope.

McGrath et al. (2025 — CHAI-T) [[notes]](../notes/Collaborative%20Human-AI%20Trust%20(CHAI-T)-%20A%20Process%20Framework%20for%20Active%20Management%20of%20Trust%20in%20Human-AI%20Collaboration.md) establish that trust calibration requires "expectations aligned with the capabilities of system." The behavioural difference between SAFE and CAUTION automatically aligns user expectations with system capabilities: users cannot expect departure time recommendations when the system visibly does not provide them. This is calibration by design, not calibration by instruction.

### 6.3 User Interface Is Not the Contribution

The specific visual design of mode communication (colour coding, text labels, icons) is an implementation and HCI concern, not an architectural contribution. The architecture guarantees that the modes are behaviourally distinct — the user *will* notice the difference because the output changes. How best to *additionally* communicate the mode through interface design is a standard HCI problem with established solutions from traffic-light safety indexing (Flehmig et al., 2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md), maritime risk display (Madsen & Kim, 2024) [[notes]](../notes/A%20state-of-the-art%20review%20of%20AI%20decision%20transparency%20for%20autonomous%20shipping.md), and automotive status communication (Gyllenhammar et al., 2025) [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md).

---

## 7. Is CAUTION Necessary for All Safety-Critical Systems or Only Fisheries?

### 7.1 The Architectural Argument for Domain Generality

The CAUTION mode addresses a structural problem that exists in any safety-critical AI decision support system where:

1. **Environmental conditions affect recommendation reliability differently across recommendation types** — some recommendation types degrade faster than others under elevated conditions
2. **Binary governance (full AI / no AI) is disproportionate** — blocking all AI assistance removes valuable guidance along with unreliable guidance
3. **The human operator faces decisions under elevated conditions** — the moment when decision support is most needed is also the moment when unrestricted decision support is most dangerous

These conditions are not fisheries-specific. They apply to:

| Domain | Full-scope recommendations | Reliable under CAUTION | Unreliable under CAUTION |
|---|---|---|---|
| **Coastal fisheries** | Go/no-go, delay, departure time, trip duration | Go/no-go, delay | Departure time, trip duration |
| **Agricultural decision support** | Plant/don't plant, irrigation timing, fertiliser dosing, harvest scheduling | Plant/don't plant, delay planting | Specific timing, precise dosing |
| **Maritime navigation** | Route, speed, port selection, crew scheduling | Go/no-go, port selection | Optimal route, speed recommendations |
| **Emergency response** | Deploy, staging location, resource allocation, timeline | Deploy/don't deploy, staging area | Specific resource quantities, precise timelines |

In each case, the CAUTION principle is the same: under elevated environmental uncertainty, restrict AI advisory scope to recommendation types whose reliability is robust, while suppressing recommendation types whose reliability degrades.

### 7.2 Evidence of Domain Generality from the Corpus

The corpus provides evidence that the binary governance problem is universal, not fisheries-specific:

**Ramos et al. (2024)** [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md), reviewing 91 papers across manufacturing, automotive, aviation, maritime, nuclear, and rail, find binary governance universal across all six domains. The gap is cross-domain.

**Perez-Cerrolaza et al. (2024)** [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md), surveying automotive, avionics, railway, and industrial robotics, confirm binary governance across all four domains and note that "excessive false alarms" from binary blocking create domain-general system-level hazards.

**Gyllenhammar et al. (2025)** [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md) document the ODD → ROD → MRC hierarchy as the automotive domain's independently derived three-level graduated response — confirming that the proceed/caution/stop structure recurs across domains.

**Flehmig et al. (2024)** [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md) independently derive a three-level classification for AI quality assurance in safety-critical systems generally (not fisheries-specific), selecting three levels specifically because this is "the first framework or method for indexing AI degradation in safety-critical systems in such a manner."

### 7.3 Why Fisheries Is the Instantiation Domain

Fisheries is not chosen because CAUTION only works there. It is chosen because:

1. **The empirical evidence for tripartite decision-making is strongest** — Gao (2024) [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md) and Rahim et al. (2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) independently document go/cautious-go/don't-go across two national contexts
2. **The decision support vacuum at intermediate conditions is empirically documented** — Yamin et al. (2025) [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md) document TK erosion and the absence of intermediate-risk decision support
3. **The binary governance failure is directly observable** — Rahim et al. (2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) document that binary "don't sail" warnings are routinely overridden
4. **Low-resource constraints motivate architectural parsimony** — the three-state architecture is computationally lightweight, which matters for edge deployment

The architecture is domain-general; the thresholds, recommendation types, and evaluation are domain-specific. An implementation for agricultural decision support would use different E vector parameters (soil moisture, temperature, frost risk) and different R types (planting, irrigation, harvest) with the same governance structure: S = f(E) → (G(S), A_AI(S)) with A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅.

---

## 8. Comparative Summary Table

| Question | Answer | Key justification |
|---|---|---|
| **What does AI do differently in CAUTION?** | Generates recommendations from restricted scope: go/no-go and delay only; no departure time or trip duration | Different recommendation types have different reliability envelopes; CAUTION retains robust types, suppresses degraded types |
| **What types are allowed?** | A_AI(CAUTION) = {Go, Delay}; suppressed: {DepartureTime, Duration} | Go/no-go depends on threshold crossing (robust); departure time depends on precise estimation (degrades under uncertainty) |
| **How is restricted scope defined?** | Set-valued function A_AI(S) → P(R) with containment property; pre-hoc output space definition, not post-hoc filtering | Formal containment A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ ∅ enables Safety Dominance Property proof |
| **Is CAUTION like degraded mode?** | Analogous in proportionality but different in trigger: CAUTION is environment-triggered, degraded mode is fault-triggered | CAUTION responds to external conditions; degraded mode responds to internal system faults (Flehmig et al., 2024 [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md); Gyllenhammar et al., 2025 [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md)) |
| **Sustained CAUTION?** | Expected during monsoon seasons; go/no-go guidance remains valuable; better than sustained AI withdrawal | Rahim et al. (2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md): fishers reduce but don't cease operations for entire monsoon season; sustained restricted guidance > no guidance |
| **Cognitive load?** | Net reduction: removes meta-cognitive assessment burden and false-precision anchoring; one-time mode-tracking cost | Mussi et al. (2025): progressive disclosure; Wen et al. (2025): unreliable information causes worse decisions than less information |
| **How do users distinguish SAFE/CAUTION?** | Three channels: explicit label, environmental rationale, behavioural difference (visibly fewer recommendation types) | Schrills et al. (2025) [[notes]](../notes/Questioning%20Trust%20in%20AI%20Research-%20Exploring%20the%20Influence%20of%20Trust%20Assessment%20on%20Dependence%20in%20AI-Assisted%20Decision-Making.md): communicated capability shapes reliance; behaviour is the strongest signal |
| **Domain-general or fisheries-only?** | Architecture is domain-general; instantiated in fisheries because empirical evidence for tripartite decisions and binary governance failure is strongest there | Binary governance gap confirmed across 6 domains (Ramos et al., 2024) [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md), 4 domains (Perez-Cerrolaza et al., 2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md); three-level graduated response independently derived in automotive (Gyllenhammar et al., 2025) [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md) and industrial AI (Flehmig et al., 2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md) |

---

## 9. One-Paragraph Summary (for use in Chapter 3)

> In the CAUTION state, the AI generates recommendations from a formally restricted output space A_AI(CAUTION) = {Go, Delay} ⊂ R, suppressing departure time and trip duration recommendations whose reliability degrades under elevated environmental uncertainty while retaining go/no-go directional guidance and delay guidance whose reliability is robust to moderate uncertainty. This partition follows the principle that different recommendation types have different reliability envelopes: threshold-crossing assessments (go/no-go) and trend assessments (delay/proceed) are robust because they depend on ordinal comparison, not cardinal precision, while temporal recommendations (departure at 06:15, return by 14:00) require precise environmental modelling that CAUTION conditions invalidate. Restricted scope is defined as a set-valued function A_AI: S → P(R) satisfying the containment property A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅, implemented as pre-hoc output space definition rather than post-hoc filtering — distinguishing it from all guardrail mechanisms catalogued by Shamsujjoha et al. (2025) [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md) and the static prohibited sets defined in Chen et al.'s (2025) [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md) AI Safety Principle I. CAUTION is not degraded mode: it is triggered by environmental conditions (external), not system faults (internal), and the AI model may be fully operational — the distinction is that Flehmig et al.'s (2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md) traffic-light framework responds to AI performance degradation while CAUTION responds to environmental state classification via S = f(E). Sustained CAUTION during monsoon seasons is expected and appropriate, providing daily go/no-go guidance throughout periods when Rahim et al. (2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) document fishers reduce but do not cease operations. CAUTION reduces net cognitive load by performing the meta-cognitive assessment ("is this recommendation type reliable under current conditions?") at the architecture level — implementing the progressive disclosure principle advocated by Mussi et al. (2025) and removing the false-precision anchoring that Schrills et al. (2025) [[notes]](../notes/Questioning%20Trust%20in%20AI%20Research-%20Exploring%20the%20Influence%20of%20Trust%20Assessment%20on%20Dependence%20in%20AI-Assisted%20Decision-Making.md) demonstrate shapes user reliance more powerfully than subjective trust. Users distinguish SAFE from CAUTION through three simultaneous channels: explicit state label, environmental rationale enabling independent verification (the trust empowerment mechanism identified by Atf & Lewis, 2026) [[notes]](../notes/Is%20Trust%20Correlated%20With%20Explainability%20in%20AI%3F%20A%20Meta-Analysis.md), and visibly different system behaviour (fewer recommendation types). The architecture is domain-general — the binary governance gap that CAUTION resolves is confirmed across six safety-critical domains (Ramos et al., 2024) [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md) and four industrial/transportation domains (Perez-Cerrolaza et al., 2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md), and the three-level graduated response is independently derived in automotive safety (Gyllenhammar et al., 2025) [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md) and industrial AI quality assurance (Flehmig et al., 2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md) — with fisheries as the instantiation domain where empirical evidence for tripartite decision-making (Gao, 2024) [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md) and (Rahim et al., 2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) and the decision support vacuum at intermediate conditions (Yamin et al., 2025) [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md) is strongest.
