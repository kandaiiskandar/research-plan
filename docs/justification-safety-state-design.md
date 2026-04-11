---
layout: document
---

# Safety State Design Details: Naming, Boundaries, Thresholds, Dynamics, and Misclassification

**Document type**: Theoretical justification / argumentation note  
**For**: Chapter 3 (Architecture Design) and viva preparation  
**Questions addressed**: Why SAFE–CAUTION–UNSAFE naming (not low/medium/high risk)? How are boundaries defined? What if classification is wrong? Who defines thresholds? Are thresholds universal or domain-specific? Can states change during operation? How frequently? What data?

**Cross-references**: For why *three* states (not binary/continuous/five-level), see `justification-three-states.md`. For why *environmental state* is the governance trigger (not AI confidence/uncertainty/risk score), see `justification-environmental-state-governance.md`.

---

## 1. Why SAFE–CAUTION–UNSAFE and Not Low/Medium/High Risk?

### 1.1 The Core Claim

The safety states are named SAFE, CAUTION, and UNSAFE rather than low/medium/high risk. This is not cosmetic. The naming reflects a fundamental design choice about what the states *mean* and what they *govern*.

### 1.2 Why Risk Levels Fail as Governance States

**Risk levels describe a continuum; governance states define discrete operational modes.** "Low risk" implies a position on a scale — it invites the question "how low?" and suggests that the boundary between low and medium is arbitrary. SAFE, CAUTION, and UNSAFE are not positions on a scale — they are categorically distinct operational modes, each with a formally defined governance configuration:

- **SAFE**: G(S) = 1, A_AI(S) = R_full — AI participates with full advisory scope
- **CAUTION**: G(S) = 1, A_AI(S) = R_restricted ⊂ R_full — AI participates with restricted advisory scope
- **UNSAFE**: G(S) = 0, A_AI(S) = ∅ — AI does not participate

Each state has qualitatively different governance semantics, not merely a different risk magnitude. "Medium risk" does not communicate that AI is active but with restricted scope. "CAUTION" does.

**Risk levels are observer-relative; safety states are system-defined.** "Low risk" depends on who is assessing risk and their risk tolerance. A novice fisher and a 40-year veteran may disagree about what constitutes "medium risk." The governance states are not subjective risk assessments — they are system-defined operational modes determined by a deterministic classification function f(E) applied to objective environmental measurements. The fisher does not assess risk to determine the governance mode; the system classifies environmental state and applies the corresponding governance configuration.

**Risk levels conflate probability and consequence; safety states map to governance actions.** Risk in safety engineering is typically defined as P(harm) × C(harm) — the product of probability and consequence. A "medium risk" event could be moderately probable with moderate consequences, or highly probable with low consequences, or improbable with severe consequences. These require different governance responses. SAFE/CAUTION/UNSAFE map directly to governance actions without requiring the user or system to decompose risk into probability and consequence components.

**Domain precedent favours operational mode naming.** The proceed/caution/stop grammar is the foundational behavioural vocabulary of safety-critical decision-making. Gyllenhammar et al. (2025) [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md) document the ODD → ROD → MRC hierarchy in automated driving — Operational Design Domain, Restricted Operational Domain, Minimal Risk Condition — using operational mode names, not risk levels. Flehmig et al. (2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md) use green/orange/red with operational semantics (AI fully operational, enhanced monitoring required, switch to backup). Madsen & Kim (2024) [[notes]](../notes/A%20state-of-the-art%20review%20of%20AI%20decision%20transparency%20for%20autonomous%20shooting.md) document that maritime collision avoidance systems use colour-coded categorical classifications that map to the same proceed/caution/stop logic. The naming convention follows established safety engineering practice.

**Fishers already think in operational modes.** Gao (2024) [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md) documents Penang fishers' decision-making as go/cautious-go/don't-go — operational decisions, not risk assessments. Fishers do not say "the risk is medium today"; they say "I'll go, but stay close to shore and come back early." SAFE/CAUTION/UNSAFE aligns with this operational framing; low/medium/high risk does not.

### 1.3 Summary

The naming is SAFE/CAUTION/UNSAFE because the states are operational governance modes with formally defined semantics, not positions on a risk continuum. Each name communicates a distinct operational configuration — something risk levels cannot do.

---

## 2. How Are the Boundaries Defined?

### 2.1 The Classification Function

The boundary between safety states is defined by the deterministic classification function S = f(E), where E = {w, r, m, o, v, t} is the environmental parameter vector:

| Parameter | Symbol | Measurement |
|---|---|---|
| Wind speed | w | Sustained wind velocity (knots) |
| Rainfall | r | Precipitation intensity (mm/hr) or categorical |
| Marine warnings | m | Official maritime authority warnings (categorical) |
| Ocean state | o | Wave height (m), swell period (s) |
| Vessel condition | v | Vessel operational readiness (categorical) |
| Time of day | t | Hour of day (24-hour clock) |

### 2.2 Threshold-Based Classification

f(E) is a threshold-based classifier. Each environmental parameter has defined thresholds that partition its range into three zones corresponding to SAFE, CAUTION, and UNSAFE. The overall safety state is determined by a **worst-case (conservative) rule**: S = max-severity(S_w, S_r, S_m, S_o, S_v, S_t) — if any parameter classifies as UNSAFE, the overall state is UNSAFE; if any classifies as CAUTION and none as UNSAFE, the overall state is CAUTION.

This worst-case rule is formally equivalent to the weakest-link formulation used by Baxi (2026) [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) in the CGAE architecture: k = min(g₁(CC), g₂(ER), g₃(AS)), where the overall tier is determined by the worst-performing dimension. The principle is the same: safety governance should be determined by the most concerning condition, not by averaging across conditions.

### 2.3 The SAFE–CAUTION Boundary

The SAFE–CAUTION boundary marks the transition from full AI advisory scope to restricted advisory scope. This boundary should be set at the point where the reliability of *detailed* recommendations (departure time, trip duration, fishing area) begins to degrade, even though *directional* recommendations (go/no-go, delay guidance) remain reliable.

**Empirical calibration from domain practice**: Gao (2024) [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md) documents that Penang fishers begin adopting cautious-go behaviour — shortened trips, near-shore operations, increased weather monitoring — at conditions that experienced fishers describe as "manageable but elevated." Rahim et al. (2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) document that during the East season (vigorous winds but calm seas), fishers shift to near-shore operations and reduce trip frequency — an intermediate behavioural regime that defines the empirical CAUTION zone. Yamin et al. (2025) [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md), surveying 136 fishers in central Terengganu, document that the dominant climate hazards — stronger winds/waves (95%), more intense weather events (91%), erratic rainfall (91%) — map directly onto E vector components w, o, and r.

**Example thresholds** (illustrative; final values require domain expert validation):

| Parameter | SAFE | CAUTION | UNSAFE |
|---|---|---|---|
| Wind speed (w) | < 15 knots | 15–25 knots | > 25 knots |
| Wave height (o) | < 1.0 m | 1.0–2.0 m | > 2.0 m |
| Rainfall (r) | None/light | Moderate | Heavy/storm |
| Marine warnings (m) | None | Advisory | Warning/alert |
| Vessel condition (v) | Good | Minor issues | Major deficiency |
| Time of day (t) | 06:00–17:00 | 17:00–19:00 | 19:00–06:00 |

These specific values are parameters of the architecture, not structural features. The architecture's formal properties (containment, Safety Dominance) hold for *any* valid threshold assignment. The thresholds themselves are calibrated through domain expertise and validated empirically.

**Independent physical validation from maritime sensing**: Ryu & Han (2025) [[notes]](../notes/Environment-Aware%20Multi-Sensor%20Fusion%20for%20Maritime%20Domain%20Awareness-%20A%20Comprehensive%20Review.md), reviewing environment-aware multi-sensor fusion for maritime domain awareness, identify three wind-speed regimes with distinct detection behaviours across all maritime sensing modalities (SAR, optical, AIS, RF): below ~2 m/s (~4 knots), 2–8 m/s (~4–16 knots), and above ~10–12 m/s (~20–24 knots). These physically-grounded regimes — derived from sensor reliability analysis, not governance design — align with the proposed threshold structure: the transition from reliable to degraded sensor performance at ~10–12 m/s corresponds to the SAFE–CAUTION boundary region, while the regime above this threshold where white-cap contamination and breaking waves overwhelm detection algorithms maps onto CAUTION–UNSAFE. This convergence between independently-derived sensor reliability regimes and the governance boundary design provides physical validation for the threshold structure.

**Empirical basis for the time-of-day thresholds.** Atacan & Düzbastılar (2023) [[notes]](../notes/Determination%20of%20risk%20perception%20in%20small-scale%20fishing%20and%20navigation.md) demonstrate through a bridge navigation simulator study with 30 small-scale fishing vessel captains that night navigation elevates accident probability (mean 4.08 vs. 3.43 in calm conditions) and consequence (mean 12.80 vs. 8.53), and that combined night with heavy weather produces the highest risk scores across all tested conditions (consequence mean 37.03). Restricted visibility — the primary mechanism of nighttime risk elevation for small vessels — is the single most dangerous factor for sea navigation accident probability (mean 7.90). Dominguez-Péry et al. (2023) [[notes]](../notes/A%20holistic%20view%20of%20maritime%20navigation%20accidents%20and%20risk%20indicators-%20examining%20IMO%20reports%20from%202011%20to%202021.md), reviewing 504 IMO accident reports, identify external environmental factors including visibility as the largest risk cluster (26.7% of text segments), with time of day recorded as a standard field in maritime accident investigation. The CAUTION zone (17:00–19:00) captures the approach to darkness — the transition from full to restricted visibility that Atacan & Düzbastılar's findings identify as the critical safety boundary for small-vessel operations.

### 2.4 The CAUTION–UNSAFE Boundary

The CAUTION–UNSAFE boundary marks the transition from restricted AI advisory scope to no AI participation. This boundary should be set at the point where even *directional* recommendations (go/no-go) become unreliable — where environmental conditions exceed the AI system's ability to provide any useful guidance.

This boundary also corresponds to the point where the physical risk of maritime operations becomes unacceptable regardless of decision support quality. Rahim et al. (2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) document that during the West season (winds 30–40 knots, waves exceeding 2m), even experienced fishers dramatically curtail operations — from 5–6 trips per week to 2–3, and from 7–10 hours to 3–5 hours. At the extreme, fishers "do not go to sea at all" during peak adverse conditions.

The UNSAFE boundary is inherently more conservative than the CAUTION boundary because the governance consequence is more severe: complete AI withdrawal. The asymmetry is deliberate — it is better to provide restricted guidance under genuinely unsafe conditions (the AI says go/no-go when it should say nothing) than to withhold guidance under genuinely cautionary conditions (the AI says nothing when it should say go/no-go).

### 2.5 Hysteresis

Boundary transitions incorporate hysteresis to prevent rapid oscillation between states when environmental conditions hover near a threshold. Once the system transitions from SAFE to CAUTION, it requires conditions to improve beyond the SAFE threshold by a margin before transitioning back. This prevents governance mode flickering that would undermine user trust and mode awareness.

McGrath et al. (2025) [[notes]](../notes/Collaborative%20Human-AI%20Trust%20(CHAI-T)-%20A%20Process%20Framework%20for%20Active%20Management%20of%20Trust%20in%20Human-AI%20Collaboration.md) — CHAI-T identify predictability — "consistency or regularity of behaviour" — as a distinct trustworthiness dimension. A governance system that oscillates between SAFE and CAUTION every few minutes as wind speed fluctuates around 15 knots would violate this requirement. Hysteresis ensures that governance mode transitions are stable and infrequent enough for users to track and respond to appropriately.

Schrills et al. (2025) [[notes]](../notes/Questioning%20Trust%20in%20AI%20Research-%20Exploring%20the%20Influence%20of%20Trust%20Assessment%20on%20Dependence%20in%20AI-Assisted%20Decision-Making.md) demonstrate empirically that users engage in "probability matching" — calibrating their reliance to the communicated system capability. Rapid mode switching would prevent the stable reliance calibration this finding describes: users cannot match their behaviour to a system state that changes faster than their cognitive recalibration cycle.

---

## 3. What Happens If the Safety State Classification Is Wrong?

### 3.1 Two Types of Misclassification

The classification function f(E) can err in two directions:

| Misclassification | Actual state | Classified state | Governance consequence | Safety consequence |
|---|---|---|---|---|
| **Over-classification** | SAFE | CAUTION | AI restricts scope unnecessarily | Loss of decision support value; no safety hazard |
| | SAFE | UNSAFE | AI withdraws unnecessarily | Fisher decides alone; no safety hazard |
| | CAUTION | UNSAFE | AI withdraws when restricted scope was appropriate | Loss of go/no-go guidance; no safety hazard |
| **Under-classification** | CAUTION | SAFE | AI provides full scope when restriction was warranted | False precision risk — unreliable detailed recommendations delivered |
| | UNSAFE | CAUTION | AI provides restricted scope when withdrawal was warranted | Go/no-go guidance under conditions where even directional advice is unreliable |
| | UNSAFE | SAFE | AI provides full scope under dangerous conditions | Full false precision risk under genuinely dangerous conditions |

### 3.2 Asymmetric Consequences

Over-classification is **safe but costly** — the system provides less information than it could. The fisher loses decision support value but is not exposed to unreliable recommendations. The worst case is equivalent to operating without the AI system at all — which is the status quo.

Under-classification is **unsafe** — the system provides recommendations whose reliability is compromised by conditions the governance layer failed to recognise. This is the failure mode the architecture must minimise.

### 3.3 Architectural Mitigations

**Conservative threshold setting**: Thresholds should be set to favour over-classification (false CAUTION, false UNSAFE) over under-classification (false SAFE). This is the standard approach in safety engineering: set alarm thresholds to favour false positives over false negatives. Perez-Cerrolaza et al. (2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) document this principle across automotive, avionics, railway, and industrial domains: safety mechanisms are calibrated to err on the side of restriction, with the caveat that "excessive false alarms could lead to new system-level hazards" — which is why the architecture uses three states rather than binary (binary blocking at conservative thresholds produces the excessive false alarm problem; CAUTION provides a proportionate intermediate response).

**Worst-case aggregation**: The worst-case rule (S = max-severity across all parameters) means that a single parameter exceeding a CAUTION threshold triggers CAUTION governance regardless of all other parameters. This structural conservatism provides a safety margin against individual parameter measurement errors.

**Independent observability**: Because f(E) operates on physical sensor measurements (wind speed, wave height, visibility), misclassification can be detected by the human operator through direct observation. A fisher who sees calm seas and light winds while the system displays CAUTION can identify a potential sensor fault. This is a unique advantage of environmental-state-conditioned governance over AI-confidence-conditioned governance: the human can independently verify the governance trigger. Bloomfield & Rushby (2025) [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md) identify this as a defining property of assuredly guarded systems — guards that can be verified by means independent of the system they protect.

**Sensor redundancy and validation**: Implementation-level mitigations include redundant sensors, cross-validation between sensor readings (e.g., wind speed corroborated by wave state), and comparison with external data sources (weather service APIs when connectivity permits). These are implementation concerns, not architectural features — the architecture specifies that f(E) must be deterministic and based on observable parameters; the implementation determines how robustly those parameters are measured.

### 3.4 The Residual Risk

No classification system achieves zero misclassification. The architecture's safety argument does not require perfect classification — it requires that the *consequences* of misclassification are bounded and asymmetric:

- Over-classification: bounded by loss of decision support value (equivalent to no-AI baseline)
- Under-classification: bounded by the Safety Dominance Property applying to the *classified* state — even if the classification is wrong, the AI's recommendations are still constrained to A_AI(S_classified), which is at least as restrictive as no governance (full scope) and potentially more restrictive than the actual conditions warrant

The architecture is therefore **fail-safe in one direction** (over-classification produces safe degradation) and **fail-bounded in the other** (under-classification provides AI recommendations that, while inappropriate for the actual conditions, are still formally bounded by the classified state's scope constraint).

---

## 4. Who Defines the Safety Thresholds?

### 4.1 The Threshold Governance Hierarchy

Safety thresholds in the proposed architecture are defined through a three-source governance hierarchy:

**Source 1 — Regulatory and institutional standards**: Maritime authority regulations (e.g., Malaysian Maritime Enforcement Agency sea condition warnings, Indonesian KKP advisories) provide floor-level thresholds that the system must respect. If a maritime authority issues a storm warning, the system must classify at least CAUTION regardless of local sensor readings. Bengio et al. (2026) [[notes]](../notes/International%20AI%20Safety%20Report%202026.md) document that all 11 Frontier AI Safety Frameworks embed institutional safety thresholds — the proposed architecture extends this principle to the domain level.

**Source 2 — Domain expert calibration**: Thresholds for the SAFE–CAUTION and CAUTION–UNSAFE boundaries require calibration by domain experts with knowledge of local conditions, vessel capabilities, fishing practices, and historical incident data. This calibration is analogous to the threshold-setting process documented across safety-critical domains: SIL levels in IEC 61508, ASIL levels in ISO 26262, and DAL levels in DO-178C are all calibrated through expert assessment against domain-specific evidence. Perez-Cerrolaza et al. (2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) confirm that threshold calibration is a standard safety engineering process, not a design innovation.

**Source 3 — Empirical domain evidence**: Thresholds are validated against empirical evidence of fisher behaviour and incident history. Gao (2024) [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md) documents the environmental factor importance ratings from 25 semi-structured interviews: tide (4.55/5), fishing resource (4.45/5), weather (3.75/5), safety concern (3.40/5). These ratings indicate which parameters fishers themselves weight most heavily — threshold sensitivity should be proportionate to these empirical importance ratings. Yamin et al. (2025) [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md) document that wind/wave intensification (95%), weather events (91%), and erratic rainfall (91%) are the dominant climate hazards perceived by the target population — confirming that w, o, and r require the most conservative threshold calibration.

### 4.2 Thresholds Are Parameters, Not Architecture

A critical distinction: thresholds are **parameters** of the classification function f(E), not structural features of the governance architecture. The architecture's formal properties — the containment hierarchy A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅, the Safety Dominance Property AI(E) ⊆ A_AI(S), and the governance pair (G(S), A_AI(S)) — hold for *any* valid threshold assignment. Changing the threshold for CAUTION wind speed from 15 knots to 18 knots does not change the architecture; it changes a parameter.

This parametric design means the system can be calibrated for different deployment contexts without architectural modification — a property that directly addresses the next question.

---

## 5. Are Safety Thresholds Universal or Domain-Specific?

### 5.1 The Architecture Is Universal; the Thresholds Are Domain-Specific

The governance architecture — S = f(E) → (G(S), A_AI(S)) with the containment property and Safety Dominance Property — is domain-general. The formal structure applies to any safety-critical decision support context where:
- Environmental conditions affect decision safety
- AI advisory scope should be conditioned on those conditions
- Graduated governance (not just binary) is appropriate

The thresholds within f(E) are necessarily domain-specific because they encode domain knowledge about:
- What environmental conditions constitute elevated risk (different for coastal fishing, offshore oil, aviation, mining)
- What vessel/equipment capabilities define operational limits (a 22-foot fishing boat vs. a 200-foot trawler)
- What regulatory requirements apply (Malaysian waters vs. Indonesian waters vs. North Sea)
- What historical incident patterns reveal about condition-outcome relationships

### 5.2 Even Within One Domain, Thresholds Vary

Within coastal fisheries, thresholds vary by:

| Factor | Why thresholds differ | Evidence |
|---|---|---|
| **Geography** | Strait of Malacca conditions differ from South China Sea; sheltered vs. exposed waters | Gao (2024) [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md): Penang fishers operate in relatively sheltered waters; Yamin et al. (2025) [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md): Terengganu fishers face open South China Sea monsoon conditions |
| **Vessel type** | A 22-foot wooden boat has different wave tolerance than a 40-foot fiberglass vessel | Rahim et al. (2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md): vessel size is a primary factor in fisher risk assessment |
| **Fishing method** | Net fishing requires calmer conditions than line fishing; bottom trawling is less wave-sensitive than surface longlining | Gao (2024) [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md): gear type affects which conditions are operationally tolerable |
| **Season** | Monsoon patterns create different baseline conditions that shift the SAFE–CAUTION boundary | Rahim et al. (2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md): West season (30–40 knots, >2m waves) vs. East season (vigorous wind, calm seas) vs. Fishing season (low wind, mild swells) represent fundamentally different operational baselines |

### 5.3 Implication for the Contribution

The contribution is the governance architecture, not the specific thresholds. An examiner should evaluate whether the architectural mechanism (state-conditioned scope restriction) is sound and novel, not whether a specific wind speed threshold is correctly calibrated. Threshold calibration is an implementation and validation concern — essential for deployment but not for the architectural contribution claim.

---

## 6. Can Safety States Change During Operation? How Frequently?

### 6.1 Runtime Reclassification

Yes, safety states change during operation. This is a fundamental design requirement: environmental conditions change continuously, and the governance mode must track these changes to remain valid.

The classification function f(E) is evaluated continuously (or at a defined polling interval) during system operation. When environmental parameters cross a threshold, the safety state transitions and the governance configuration updates accordingly.

### 6.2 Operational Timescale

Environmental conditions in coastal fisheries change at a physical timescale:
- **Wind speed**: changes over minutes to hours (gradual trends with occasional rapid shifts)
- **Wave height**: changes over hours (responds to wind with a lag)
- **Rainfall**: changes over minutes (squalls) to hours (sustained precipitation)
- **Marine warnings**: updated on hour-to-day timescales by maritime authorities
- **Visibility**: changes over minutes (fog, rain squalls) to hours
- **Vessel condition**: changes on day-to-trip timescales (unless in-trip damage occurs)

The governance mode changes at the environmental timescale — typically hours, occasionally minutes. This is fundamentally different from AI-confidence-based governance, which would change with every inference cycle (seconds or faster). Environmental-state governance provides stable governance periods aligned with actual operational decisions.

### 6.3 Transition Scenarios

| Scenario | State transition | Governance response | Operational implication |
|---|---|---|---|
| Weather deterioration during trip | SAFE → CAUTION | AI restricts to go/no-go + delay guidance; drops detailed recommendations | Fisher receives "consider returning" guidance; no longer receives fishing area or duration recommendations |
| Sudden squall | SAFE → UNSAFE (or CAUTION → UNSAFE) | AI withdraws entirely | Fisher relies on own judgement and any operational safety systems |
| Conditions improving during wait | CAUTION → SAFE (with hysteresis) | AI restores full advisory scope | Fisher receives full recommendation set including departure timing |
| Morning departure assessment | System starts in current state based on conditions | Governance configured for assessed state | Fisher receives recommendations appropriate to current conditions |

### 6.4 Why Runtime Reclassification Matters

A system that classifies environmental state only at the start of a trip and maintains that classification throughout would fail to protect against condition deterioration — the most common maritime safety scenario. Rahim et al. (2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) document that fishers adaptively adjust behaviour during trips when conditions change: shifting from open-sea to near-shore, reducing trip duration. The governance architecture must support this adaptive pattern by reclassifying state as conditions evolve.

This is a distinguishing feature relative to Baxi (2026) [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) — CGAE, where tier assignment is static between adversarial audits (with temporal decay providing some dynamism). CGAE's conditioning variable (verified agent robustness) changes on audit-cycle timescales (weeks to months); the proposed architecture's conditioning variable (environmental state) changes on physical timescales (minutes to hours). The runtime reclassification capability is essential for physical safety-critical domains where the governed variable — environmental conditions — is dynamic.

---

## 7. What Data Is Used to Determine the Safety State?

### 7.1 The Environmental Parameter Vector

The safety state is determined from E = {w, r, m, o, v, t} — six observable environmental parameters. Each parameter is measurable through sensors independent of the AI system:

| Parameter | Data sources | Independence from AI |
|---|---|---|
| Wind speed (w) | Anemometer, weather station, weather service API | Fully independent — physical sensor |
| Rainfall (r) | Rain gauge, weather radar, visual observation | Fully independent — physical sensor |
| Marine warnings (m) | Maritime authority broadcasts, weather service API | Fully independent — institutional source |
| Ocean state (o) | Wave buoy, visual observation, satellite altimetry | Fully independent — physical sensor |
| Vessel condition (v) | Pre-departure checklist, maintenance records | Fully independent — operator assessment |
| Time of day (t) | Clock (24-hour) | Fully independent — deterministic |

### 7.2 Why These Six Parameters

The selection of E vector components is not arbitrary — it is grounded in empirical evidence of what drives fisher safety decisions:

**Yamin et al. (2025)** [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md) document the target population's own hazard identification: wind/wave intensification (95% of 136 fishers), weather events (91%), erratic rainfall (91%). These map directly onto w, o, and r.

**Gao (2024)** [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md) documents environmental factor importance ratings: tide (4.55/5 — captured in o as ocean state), weather (3.75/5 — captured across w, r, and m), safety concern (3.40/5 — captured across all parameters as the aggregated classification).

**Rahim et al. (2024)** [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) document that wind velocity, wave height, precipitation, season, and vessel size are the primary inputs to fisher operational decisions in coastal Indonesia — confirming w, o, r, and v as cross-nationally validated parameters.

### 7.3 The Independence Property

The critical property of the data sources is their **independence from the AI system**. Every parameter in E is measurable by non-AI sensors. This means:

1. The governance classification f(E) does not depend on AI outputs — no circular dependency
2. The governance layer functions even if the AI component is unavailable
3. The human operator can independently verify the governance inputs against direct perception

This independence is not incidental — it is a formal requirement for the Safety Dominance Property proof. Bloomfield & Rushby (2025) [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md) identify this independence as the defining property of assuredly guarded systems. Dalrymple et al. (2024) [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md) specify that the world model providing safety specifications must be independent of the AI policy. The environmental parameter vector E satisfies both requirements: it provides the governance basis from sources that share no dependency with the AI reasoning layer.

---

## 8. Comparative Summary Table

| Design question | Answer | Justification basis |
|---|---|---|
| **Why SAFE/CAUTION/UNSAFE naming?** | Operational governance modes, not risk levels | States define discrete governance configurations with qualitatively different AI behaviour; aligns with proceed/caution/stop grammar in safety engineering (Gyllenhammar et al., 2025) [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md); (Flehmig et al., 2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md) and fisher operational framing (Gao, 2024) [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md) |
| **SAFE–CAUTION boundary?** | Where detailed recommendation reliability degrades while directional guidance remains reliable | Calibrated from domain expert knowledge and empirical fisher behaviour (Gao, 2024) [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md); (Rahim et al., 2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md); (Yamin et al., 2025) [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md) |
| **CAUTION–UNSAFE boundary?** | Where even directional guidance becomes unreliable and/or physical risk is unacceptable | Calibrated conservatively; corresponds to conditions where experienced fishers cease operations (Rahim et al., 2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) |
| **Misclassification?** | Asymmetric consequences: over-classification is safe (loss of value); under-classification is bounded by scope constraint | Conservative thresholds, worst-case aggregation, and independent observability mitigate under-classification |
| **Who defines thresholds?** | Regulatory standards → domain experts → empirical validation | Thresholds are parameters, not architecture; formal properties hold for any valid threshold assignment |
| **Universal or domain-specific?** | Architecture is universal; thresholds are domain-specific | Even within coastal fisheries, thresholds vary by geography, vessel type, fishing method, and season |
| **Runtime reclassification?** | Yes — continuous or at defined polling interval | Environmental conditions change at physical timescales (minutes to hours); governance must track this |
| **What data?** | E = {w, r, m, o, v, t} from non-AI sensors | Independence from AI is a formal requirement (Bloomfield & Rushby, 2025) [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md); (Dalrymple et al., 2024) [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md); parameters empirically validated across three fisher studies |

---

## 9. One-Paragraph Summary (for use in Chapter 3)

> The safety states are named SAFE, CAUTION, and UNSAFE — not low/medium/high risk — because they are categorically distinct operational governance modes with formally defined AI behaviour configurations, not positions on a risk continuum: SAFE permits full AI advisory scope, CAUTION permits AI with restricted scope (A_AI(CAUTION) ⊂ A_AI(SAFE)), and UNSAFE withdraws AI entirely (A_AI(UNSAFE) = ∅). The proceed/caution/stop naming aligns with established safety engineering practice across automotive (Gyllenhammar et al., 2025) [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md), industrial AI (Flehmig et al., 2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md), and maritime (Madsen & Kim, 2024) [[notes]](../notes/A%20state-of-the-art%20review%20of%20AI%20decision%20transparency%20for%20autonomous%20shooting.md) domains, and with the operational decision framing documented in fisher practice — go/cautious-go/don't-go (Gao, 2024) [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md). Boundaries between states are defined by a threshold-based classification function S = f(E) operating on six independently observable environmental parameters (wind, rainfall, marine warnings, ocean state, vessel category, time of day), with a worst-case aggregation rule analogous to Baxi's (2026) [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) weakest-link formulation. Thresholds are calibrated through regulatory standards, domain expert knowledge, and empirical validation against fisher-reported hazard perception (Yamin et al., 2025) [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md): wind/waves 95%, weather events 91%, rainfall 91%) and observed behavioural transitions (Gao, 2024) [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md); (Rahim et al., 2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md)). Misclassification consequences are asymmetric by design: over-classification (false CAUTION or false UNSAFE) produces safe degradation equivalent to the no-AI baseline; under-classification (false SAFE) is mitigated by conservative threshold setting, worst-case aggregation, and the independent observability that Bloomfield & Rushby (2025) [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md) identify as the defining property of assuredly guarded systems. Thresholds are parameters of the architecture, not structural features — the formal properties (containment hierarchy, Safety Dominance Property) hold for any valid threshold assignment, making the architecture domain-general while threshold calibration remains domain-specific. Safety states are reclassified continuously at runtime as environmental conditions evolve, operating at the physical timescale (minutes to hours) rather than the inference timescale (seconds), with hysteresis preventing mode oscillation that would violate the predictability requirement for trust calibration (McGrath et al., 2025) [[notes]](../notes/Collaborative%20Human-AI%20Trust%20(CHAI-T)-%20A%20Process%20Framework%20for%20Active%20Management%20of%20Trust%20in%20Human-AI%20Collaboration.md); (Schrills et al., 2025) [[notes]](../notes/Questioning%20Trust%20in%20AI%20Research-%20Exploring%20the%20Influence%20of%20Trust%20Assessment%20on%20Dependence%20in%20AI-Assisted%20Decision-Making.md)).
