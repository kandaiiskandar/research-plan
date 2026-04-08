# Viva Preparation: Formalisation and Architecture Defence

**Dissertation**: A Graduated Safety-State-Gated Architecture for AI Decision Support in Low-Resource Environments

**Core notation**:
- E = {w, r, m, o, v, t} — environmental state vector
- S = f(E) — deterministic safety classification; S ∈ {SAFE, CAUTION, UNSAFE}
- G(S) — participation gate: G(SAFE)=1, G(CAUTION)=1, G(UNSAFE)=0
- A_AI(S) — admissible recommendation space
- Containment: A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅
- Safety Dominance: AI(E) ⊆ A_AI(S) for all E

---

## 🔴 High-Risk Questions

---

### HR-1. Why restrict recommendation *types* instead of restricting values within a type?

**Direct answer: Different recommendation types carry fundamentally different reliability envelopes under environmental uncertainty — restricting values within a type still presents the false-precision signal that anchors human decisions, whereas type-level suppression removes the hazard at source.**

Recommendation types are not interchangeable containers. A DepartureTime recommendation (e.g., "depart at 06:30") requires a precise temporal prediction of when wind speed will fall below a safe threshold. Under CAUTION conditions, the environmental variables in E — particularly wind speed w and ocean state o — are themselves uncertain or borderline. Even if the AI qualifies the value (e.g., "06:30 ± 2 hours"), the number anchors the fisher's mental model. Schrills et al. (2025) [[notes]](../notes/Questioning%20Trust%20in%20AI%20Research-%20Exploring%20the%20Influence%20of%20Trust%20Assessment%20on%20Dependence%20in%20AI-Assisted%20Decision-Making.md) demonstrate that instructed reliability — not subjective confidence — drives reliance behaviour. A fisher told the system is "reliable in good conditions" will anchor to a departure time even when a warning accompanies it. The hazard is the false-precision signal, not the specific value.

By contrast, Go and Delay recommendations are reliable in CAUTION conditions precisely because their semantic content does not presuppose precise temporal or durational prediction. Go says "conditions are acceptable now"; Delay says "conditions are not acceptable now." Both are tractable under partial environmental uncertainty. The type distinction is thus a reliability-of-inference distinction, not merely a content distinction. Suppressing DepartureTime and Duration under CAUTION is not an arbitrary constraint — it is a formal recognition that those types have different value-of-information profiles under the prevailing uncertainty level.

Perez-Cerrolaza et al. (2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) identify that binary blocking of all AI output creates new hazards by removing positive-value information the operator needed. Type-level restriction resolves this tension: it suppresses the types whose uncertainty-adjusted value-of-information is negative (DepartureTime, Duration under CAUTION) while retaining the types whose VOI remains positive (Go, Delay). A value-restriction approach cannot achieve this because it operates within a single type rather than selecting across types.

*Viva one-liner: The hazard under CAUTION is not a wrong number — it is the type of claim that presupposes a precision the environment cannot support, and restricting the value still presents that claim.*

---

### HR-2. Why not allow all recommendations but attach confidence scores or warnings instead?

**Direct answer: Empirical evidence shows that instructed reliability — not displayed confidence — governs reliance, and that explanations or warnings produce negligible trust recalibration, so attaching scores or warnings does not remove the anchoring hazard and may increase cognitive burden without safety benefit.**

Schrills et al. (2025) [[notes]](../notes/Questioning%20Trust%20in%20AI%20Research-%20Exploring%20the%20Influence%20of%20Trust%20Assessment%20on%20Dependence%20in%20AI-Assisted%20Decision-Making.md) find a correlation of r=0.42–0.45 between instructed reliability and dependence, and demonstrate that trust assessment interventions do not reliably reduce over-reliance. The implication is architectural: a warning label on an AI recommendation does not suppress the anchoring effect of seeing the recommendation. The fisher who reads "Depart at 06:30 (confidence: 62%)" still anchors to 06:30 — the confidence figure becomes a secondary qualifier that is cognitively processed after the anchor is set.

Atf & Lewis (2026) [[notes]](../notes/Is%20Trust%20Correlated%20With%20Explainability%20in%20AI%3F%20A%20Meta-Analysis.md) report that explanations have a weak trust effect (r=0.194) in a meta-analysis of 46 studies. If explanations — the richest form of contextual qualification — barely move trust, then a confidence score or warning badge will not materially alter reliance behaviour. This is not a failure of interface design; it reflects the bounded rationality of human decision-makers under time pressure, which is precisely the condition fishers face at departure time.

The alternative of suppressing the recommendation type removes the hazard at source. Dalrymple et al. (2024) [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md) argue that verifiers must not share failure modes with the AI system they govern. A confidence score generated by the same model that produced the recommendation shares its failure modes — both degrade under the same distributional shift in E. The governance layer in this architecture uses f(E) computed directly from physical sensor readings, entirely independent of AI model uncertainty.

*Viva one-liner: A warning attached to an unreliable recommendation does not prevent anchoring — it just adds cognitive overhead to a hazard that should have been suppressed at source.*

---

### HR-3. Is your 3-state model too coarse compared to a continuous risk score?

**Direct answer: Three states are not too coarse — they are the appropriate granularity for a governance layer that must be formally tractable, cognitively interpretable, and consistent with established domain decision categories; continuous risk scores cannot support the discrete formal properties that Safety Dominance requires.**

The Safety Dominance property AI(E) ⊆ A_AI(S) requires a mapping from S to a well-defined admissible set. For continuous S, A_AI(S) would need to be a continuously varying function of a real-valued score — meaning the output space changes at every infinitesimal shift in risk score. This makes formal verification of containment intractable and makes the governance layer unauditable. Discrete states permit exhaustive case analysis: there are exactly three governance configurations to verify, inspect, and certify.

Gyllenhammar et al. (2025) [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md) introduce ODD (Operational Design Domain), ROD (Reduced Operational Domain), and MRC (Minimal Risk Condition) — a three-level hierarchy for autonomous driving safety governance. This parallel is not coincidental: both domains require a governance structure that is interpretable by human operators and supports a progressive safety response. Flehmig et al. (2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md) use a traffic-light model with three levels to govern AI monitoring intensity in safety-critical systems. Gao (2024) [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md) documents that Malaysian fishers themselves use a tripartite decision schema — go/cautious-go/don't-go — aligning the architecture with the cognitive categories users already employ.

McGrath et al. (CHAI-T) [[notes]](../notes/Collaborative%20Human-AI%20Trust%20(CHAI-T)-%20A%20Process%20Framework%20for%20Active%20Management%20of%20Trust%20in%20Human-AI-Collaboration.md) argue that trust calibration requires discrete distinguishable modes: too few states under-calibrate trust (binary governance conflates conditions that warrant different responses), while too many states overwhelm operators who cannot maintain distinct mental models for each. Three states satisfy both bounds. Schrills et al. (2025) [[notes]](../notes/Questioning%20Trust%20in%20AI%20Research-%20Exploring%20the%20Influence%20of%20Trust%20Assessment%20on%20Dependence%20in%20AI-Assisted%20Decision-Making.md) further show that users think in categories, not continuous distributions — a precise risk score of 0.67 is not meaningfully more actionable than "CAUTION" for a fisher making a departure decision under time pressure.

*Viva one-liner: Three states are not coarse — they are the minimal granularity that adds something over binary governance while remaining formally tractable, cognitively interpretable, and empirically grounded in how fishers actually decide.*

---

### HR-4. Why is CAUTION necessary — not just SAFE/UNSAFE?

**Direct answer: CAUTION is the entire novel contribution — removing it collapses the architecture to binary governance, which is the universal status quo across 148+ papers in four independent systematic reviews and fails to match the intermediate environmental conditions fishers actually face.**

Ramos et al. (2024) [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md) review 91 papers on collaborative AI in safety-critical industries and find all governance schemes are binary. Newcomb & Ochoa (2026) [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md) survey 46 formal methods papers and find binary governance universal. Bengio et al. (2026) [[notes]](../notes/International%20AI%20Safety%20Report%202026.md) analyse 11 international AI safety frameworks — all binary. Without CAUTION, this architecture is just another instance of the mechanism four systematic reviews document as the universal status quo. There is nothing to defend.

The empirical case for CAUTION comes directly from the domain. Rahim et al. (2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) document that fishers in coastal Malaysia do not observe binary weather states — they adapt to intermediate conditions by restricting trip scope: fishing near-shore, shortening duration, changing target species. Binary governance (SAFE/UNSAFE) forces the system to classify these intermediate conditions as one extreme or the other. If classified SAFE, the AI provides full recommendations for a condition that warrants restriction. If classified UNSAFE, the AI is silenced for a condition where partial guidance would support safer scope-restricted operations. Yamin et al. (2025) [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md) confirm this pattern in a study of n=136 fishers in Terengganu, finding that binary go/no-go governance is the weakest domain in adaptive capacity.

CAUTION creates the space where Go and Delay remain valid and informative, while DepartureTime and Duration — which require precise temporal prediction under uncertain conditions — are suppressed. This is not a compromise between SAFE and UNSAFE; it is a distinct governance mode matched to a distinct class of environmental conditions with their own reliability profile.

*Viva one-liner: Without CAUTION there is no graduated architecture — there is only binary governance, which is the universal status quo this dissertation exists to advance beyond.*

---

### HR-5. What happens when inputs are near thresholds? Will the system oscillate?

**Direct answer: Four standard engineering mechanisms — hysteresis, time-windowed averaging, conservative default, and minimum dwell time — collectively eliminate oscillation at threshold boundaries, and all are standard practice in safety-critical control systems.**

Threshold oscillation (rapid alternation between states as a variable crosses the boundary) is a known hazard in any discrete-state system driven by continuous inputs. The architecture addresses this through four layered mechanisms. First, hysteresis: different thresholds are used for upward (worsening) and downward (improving) state transitions. If wind speed w crosses 25 knots to trigger CAUTION, it must fall below 22 knots to return to SAFE — not back to 25. This prevents single-measurement fluctuations from causing repeated state changes.

Second, time-windowed averaging: each environmental variable in E is computed as a rolling average over a configurable window (e.g., 10 minutes for w and r), not as an instantaneous reading. A brief gust does not trigger a state change; the sustained average must cross the threshold. Third, conservative default: when a variable is within a defined proximity band around a threshold (e.g., within 5% of the CAUTION/UNSAFE boundary), the system resolves to the more restrictive state. This implements the ALARP principle as identified by Perez-Cerrolaza et al. (2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) — uncertainty resolves conservatively. Fourth, minimum dwell time: once a state change occurs, the system requires a minimum period (e.g., 15 minutes) in the new state before another transition is permitted.

These are parameters, not structural properties — their values are calibrated domain-specifically via the design-science research cycle. The formal properties of the architecture (containment, Safety Dominance) hold for any threshold configuration; oscillation prevention is an implementation-level concern handled by standard engineering practice.

*Viva one-liner: Hysteresis, time-averaging, conservative defaults, and minimum dwell time eliminate threshold oscillation — these are standard control-engineering practices applied to the threshold parameters, not changes to the formal architecture.*

---

### HR-6. Why use max-severity aggregation instead of weighted or probabilistic methods?

**Direct answer: Max-severity implements the weakest-link principle appropriate for safety governance — weighted averaging can mask a single dangerous parameter, probabilistic methods require joint distribution data unavailable in low-resource settings, and max-severity produces deterministic auditable decisions consistent with ALARP.**

f(E) = max(severity(w), severity(r), severity(m), severity(o), severity(v), severity(t)) reflects a fundamental safety engineering principle: a system is only as safe as its most dangerous component. A vessel facing calm seas but gale-force winds is in a dangerous state — averaging wind severity (HIGH) with wave severity (LOW) and marine warning severity (NONE) would produce a misleadingly moderate aggregate. The max operator ensures that any single variable at HIGH severity escalates the overall classification, preventing masking effects.

Baxi (2026) [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) applies the identical weakest-link logic in the Comprehension-Gated Agent Economy: the gate function is conditioned on the minimum robustness across all evaluated dimensions, not the average. The reasoning is the same — in safety-relevant gating, the weakest dimension determines the appropriate governance response. Dalrymple et al. (2024) [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md) argue that governance systems must be verifiable and must not share failure modes with the AI system. Probabilistic aggregation introduces model-derived probability estimates into the governance layer, creating shared failure modes with the AI it is meant to govern — precisely the independence violation Dalrymple identifies.

Weighted methods require empirically validated weights across the joint distribution of {w, r, m, o, v, t} — data that is systematically unavailable in low-resource coastal fisheries contexts as documented by Katende (2026) [[notes]](../notes/Rethinking%20data-efficient%20artificial%20intelligence%20for%20low-resource%20settings.md). Max-severity requires only ordinal severity classification of each individual variable, which can be validated against existing MMEA (Malaysian Maritime Enforcement Agency) thresholds and meteorological standards independently and auditably. Perez-Cerrolaza et al. (2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) confirm ALARP: when uncertain, resolve conservatively. Max-severity is the ALARP-consistent aggregation function.

*Viva one-liner: Weighted averaging can hide a deadly variable behind benign ones — max-severity ensures the worst condition determines the governance response, which is the correct principle for a safety gate.*

---

### HR-7. Is your governance layer truly independent from the AI layer?

**Direct answer: Yes — the governance pipeline E → f(E) → (G, A_AI) is computed entirely from physical sensor observations before AI reasoning runs, with no path by which AI outputs can influence f(E), making the independence structural and not merely procedural.**

The independence argument has three components. First, the inputs to f(E) are physical measurements: wind speed (anemometer), rainfall (rain gauge), marine warnings (MMEA broadcast), ocean state (buoy or satellite), vessel condition (pre-departure checklist), and time of day (clock). None of these are AI outputs or AI-derived values. The AI system receives E as read-only input for generating recommendations; it has no write access to E.

Second, the pipeline is acyclic by design: E → f(E) → (G, A_AI) → AI(E) → human. AI outputs are recommendations to humans, not inputs to the governance computation. A fisher who receives a Go recommendation and departs does not update w or r — those are physical measurements of an external environment. Dalrymple et al. (2024) [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md) specifically require that the verifier must not share failure modes with the AI system — this is satisfied because f(E) degrades only when sensors fail, while the AI degrades when its training distribution shifts. These are distinct failure modes.

Third, Bajcsy & Fisac (2024) [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md) formalise an independence principle for safety filters: the filter must be computable without reference to the AI's internal state. f(E) satisfies this — it does not query the AI model, its weights, its confidence scores, or its intermediate representations. The governance layer is architecturally blind to AI internals. Bloomfield & Rushby (2025) [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md) warn against self-referential governance (a safety case that depends on the system it certifies). f(E) is not self-referential — it is externally grounded in physical observations.

*Viva one-liner: f(E) reads physical sensors and runs before the AI — there is no path by which AI outputs re-enter the governance computation, making independence structural.*

---

### HR-8. Can AI indirectly influence governance decisions (feedback loop)?

**Direct answer: No indirect feedback path exists — AI outputs are recommendations to human decision-makers, not inputs to environmental sensors, and the environmental state E is determined by physical conditions that AI recommendations cannot modify.**

The concern about indirect feedback is that a human acting on an AI recommendation could change behaviour in a way that eventually changes E. For example: the AI recommends Delay → fisher delays → weather improves → E updates to SAFE. But this is not a feedback loop in the problematic sense. The state transition is driven by physical weather change (w decreasing), not by the AI recommendation. The AI did not cause the wind to decrease. Any governance system operating in a dynamic environment will see state changes over time — this is correct behaviour, not a feedback vulnerability.

The more subtle concern would be: could an AI recommendation lead a fisher to report incorrect sensor data, which then feeds back into f(E)? This is a sensor integrity question, not an architectural feedback question. The architecture assumes sensor integrity (or sensor failure handling — addressed in HR-5 and PD-2). If sensors are tampered with, f(E) produces incorrect classifications — but this is true of any sensor-dependent safety system and is handled by standard sensor validation protocols.

Wang et al. (2026) [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md) identify feedback loops as a primary concern for LLM agents with tool access — agents that can write to databases or execute actions create genuine feedback paths. This architecture deliberately excludes AI tool access: the AI produces text recommendations consumed by a human; it has no write access to the sensor data store, the governance computation, or any system state.

*Viva one-liner: AI recommendations reach humans, not sensors — the physical environment updates E, not AI outputs, so no architectural feedback path exists.*

---

### HR-9. Why is restricting advisory scope better than reducing autonomy level?

**Direct answer: Autonomy reduction changes who decides; scope restriction changes what is decided — and autonomy reduction still exposes the human to unreliable precise information that anchors their judgment, whereas scope restriction removes unreliable content before the human sees it.**

Adaptive autonomy frameworks (e.g., sliding scale from full AI to full human control) operate on the authority dimension: under adverse conditions, the human takes more control and the AI takes less. But the human who takes control in CAUTION conditions still needs to make a departure time decision — and if the AI has already produced a departure time recommendation (even as "informational" input), that number anchors the human's judgment. Wen et al. (2025) [[notes]](../notes/Risk%20Perception%20in%20Complex%20Systems-%20A%20Comparative%20Analysis%20of%20Process%20Control%20and%20Autonomous%20Vehicle%20Failures.md) document that human intervention was ineffective in 83.3% of process control accidents and 66.7% of autonomous vehicle accidents where automation bias was present. The human nominally in control was still anchored by the automated system's prior output.

Scope restriction operates on a different dimension entirely: it determines which categories of claim the AI is permitted to make, not how much authority the AI holds. Under CAUTION, the AI cannot produce a DepartureTime recommendation — not because it lacks authority, but because the recommendation type is inadmissible. The human decision-maker is therefore not exposed to an unreliable temporal prediction at all. The hazard is suppressed before generation, not filtered after production.

This distinction is formally captured in the difference between G(S) and A_AI(S). G(S) is the participation gate — it corresponds to the autonomy-reduction concept (AI participates or does not). A_AI(S) is the admissible type space — it is the scope-restriction mechanism with no parallel in adaptive autonomy frameworks. The architecture contains both, but A_AI(S) is the primary safety mechanism and the novel contribution.

*Viva one-liner: Reducing autonomy still lets the AI say anything — restricting scope prevents the AI from making the category of claim whose reliability doesn't hold, which is where the hazard actually lives.*

---

### HR-10. What happens if safety thresholds are incorrect?

**Direct answer: Incorrect thresholds produce two distinct failure modes — over-conservative (false alarm) and under-conservative (missed escalation) — and the architecture prefers over-conservative failures by ALARP design while thresholds are parameters not structure, updatable without altering formal properties.**

The threshold values embedded in f(E) (e.g., wind speed w > 25 knots → CAUTION, w > 35 knots → UNSAFE) are domain parameters validated against MMEA guidelines and meteorological standards. They are not structural properties of the formal model. The Safety Dominance property AI(E) ⊆ A_AI(S) holds regardless of which specific threshold values are chosen — it is a property of the relationship between f, G, and A_AI, not of the threshold numbers themselves.

Over-conservative thresholds (triggering CAUTION when conditions are actually safe) result in unnecessarily restricted advisory scope — the AI cannot recommend DepartureTime when it arguably could. This is suboptimal but safe: the fisher receives less information than they could and makes a more cautious decision. Under-conservative thresholds (failing to trigger CAUTION when conditions are actually borderline) result in full advisory scope being applied to conditions that warrant restriction — a genuine safety failure. The architecture is designed to prefer over-conservative failures, consistent with the ALARP principle documented by Perez-Cerrolaza et al. (2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md).

Threshold calibration is part of the design-science research (DSR) cycle: thresholds are initialised from authoritative domain sources (MMEA, Malaysian Meteorological Department standards), validated against historical incident data, and refined through field evaluation. Bloomfield & Rushby (2025) [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md) argue that safety cases must be revisable as evidence accumulates — the threshold-as-parameter design supports this directly: threshold updates do not require formal re-verification of the architecture, only re-validation of the parameter values.

*Viva one-liner: Thresholds are parameters not structure — incorrect values are correctable through DSR iteration, and the architecture is designed to fail conservatively when thresholds err.*

---

## 🟠 Medium-Risk Questions

---

### MR-1. Why is type-level governance sufficient for safety?

**Direct answer: Type-level governance is sufficient because the safety-relevant property of a recommendation is which category of prediction it makes — not the specific value — and Safety Dominance guarantees that all AI outputs fall within the type-constrained admissible set.**

The sufficiency claim rests on the formal guarantee: Safety Dominance AI(E) ⊆ A_AI(S) ensures that no recommendation the AI produces falls outside the permitted type set for the current safety state. If the AI cannot produce a DepartureTime recommendation under CAUTION, then no dangerous false-precision temporal claim reaches the user — regardless of what value the AI would have recommended. Type-level suppression is a complete upper-bound on the categories of potential hazard.

Within each permitted type, the AI's value-generation reliability is assumed adequate for the corresponding safety state. Under SAFE, DepartureTime predictions are permitted because the environmental variables are stable enough that temporal predictions carry positive value-of-information. Under CAUTION, Go and Delay predictions are permitted because these binary assessments of current conditions are tractable under uncertainty. The type taxonomy was constructed specifically to align permitted types with reliability-under-state — so type-level governance is not an approximation; it is the appropriate granularity for this reliability-grounded design.

*Viva one-liner: Type-level governance is sufficient because the hazard is in making a certain category of claim — once that category is blocked, no value within it can cause harm.*

---

### MR-2. Could there be cases where CAUTION requires more detailed advice, not less?

**Direct answer: Under CAUTION, the fisher needs to know whether to go or delay — not when, or for how long — and the containment A_AI(CAUTION) = {Go, Delay} is calibrated to provide exactly the information whose reliability holds under intermediate conditions.**

The intuition behind this question is that a fisher facing difficult conditions might benefit from more detailed guidance — specific routes, timing windows, safety equipment checks. This conflates two distinct needs: guidance on current-conditions go/no-go (what CAUTION provides) and guidance on future-conditions optimisation (what requires DepartureTime and Duration predictions). Under CAUTION, the environmental variables are uncertain or borderline — precisely the conditions under which temporal and durational predictions degrade most severely.

Rahim et al. (2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) document that fishers in intermediate conditions restrict scope — they fish near-shore, shorten trips, avoid deep water. This is precisely the Go decision under self-imposed scope restriction, not a DepartureTime optimisation problem. The CAUTION advisory set supports the decision the fisher actually needs to make: should I go out today under these conditions? It does not attempt to optimise when to go, because that prediction is unreliable.

If a specific operational context genuinely requires detailed CAUTION-mode guidance, this is a signal to revisit the type taxonomy for that domain — A_AI(CAUTION) is a parameter of the architecture, not a fixed property. The architecture specifies that A_AI(CAUTION) ⊆ A_AI(SAFE) and A_AI(UNSAFE) = ∅; the specific types assigned to each state are domain-calibrated.

*Viva one-liner: CAUTION provides the advice whose reliability holds — go or delay — and withholds the advice whose reliability doesn't — when and for how long — which is exactly the right information at that uncertainty level.*

---

### MR-3. Is the containment assumption A_AI(SAFE) ⊃ A_AI(CAUTION) always valid?

**Direct answer: Containment is a design constraint imposed on the architecture — it is not an empirical assumption that could be violated — and it is satisfied by construction through the explicit definition of the type sets.**

A_AI(SAFE) = {Go, Delay, DepartureTime, Duration}, A_AI(CAUTION) = {Go, Delay}, A_AI(UNSAFE) = ∅. Since {Go, Delay} ⊂ {Go, Delay, DepartureTime, Duration} ⊃ ∅, strict containment holds by set theory. This is not an assumption that needs empirical validation — it is a logical consequence of how the type sets are defined. Any future expansion of the type set that maintains A_AI(CAUTION) ⊆ A_AI(SAFE) preserves containment; any expansion that violates this immediately fails the architectural constraint.

The question might be probing whether there is a type that should appear in A_AI(CAUTION) but not in A_AI(SAFE). This would violate containment and would require a domain argument that some recommendation type is appropriate under intermediate conditions but inappropriate under safe conditions. No such type exists in the fisheries domain — if a recommendation type is admissible under CAUTION (borderline conditions), it is a fortiori admissible under SAFE (benign conditions). The containment direction reflects the monotone relationship between safety state severity and advisory restrictiveness.

*Viva one-liner: Containment is satisfied by construction — the type sets are defined to satisfy it, making it a design property not an empirical assumption.*

---

### MR-4. Are you over-constraining AI usefulness?

**Direct answer: The architecture suppresses only the recommendation types whose reliability is inadequate for the prevailing safety state — types with positive value-of-information are retained at every safety state where they are admissible, so the constraint is calibrated to the reliability boundary, not set conservatively beyond it.**

The VOI framework (value of information) provides the principled answer. A recommendation type has positive VOI if acting on it produces better expected outcomes than not receiving it. DepartureTime has positive VOI under SAFE (accurate temporal predictions guide efficient departure planning) but negative VOI under CAUTION (uncertain temporal predictions anchor the fisher to a time that may be dangerously wrong). Suppressing DepartureTime under CAUTION removes a negative-VOI output — this is not over-constraint, it is accurate calibration.

Atf & Lewis (2026) [[notes]](../notes/Is%20Trust%20Correlated%20With%20Explainability%20in%20AI%3F%20A%20Meta-Analysis.md) provide the VOI framing explicitly: explanations that do not improve decisions add cognitive load without benefit. The same principle applies to recommendation types: outputs that degrade decisions under the prevailing conditions are not useful — they are harmful. Retaining them in the name of "not over-constraining" would be the actual error.

Under SAFE, the full type set {Go, Delay, DepartureTime, Duration} is available — maximum AI utility. Under CAUTION, {Go, Delay} remains — the AI continues to provide decision support on the most important question (go or not). Only under UNSAFE does the AI go silent, and in that state no maritime authority recommends fishing activity. The constraint follows the reliability boundary precisely.

*Viva one-liner: Restricting types with negative VOI under the current safety state is not over-constraint — it is the definition of useful AI output.*

---

### MR-5. What is the trade-off between safety and utility?

**Direct answer: The architecture is designed to eliminate the false safety-utility trade-off by suppressing only negative-VOI outputs — recommendations that appear to add utility but would degrade decisions — leaving genuine utility intact at every safety state where it exists.**

The conventional framing of safety-utility trade-offs assumes that every safety constraint reduces useful output. This assumption fails when the "useful" output is unreliable. A DepartureTime recommendation under CAUTION appears to add utility (specific guidance) but degrades decisions by anchoring the fisher to a temporally imprecise number. Removing it does not reduce utility — it removes the appearance of utility that masks an actual hazard.

The real trade-off in the architecture is between advisory scope and reliability: the system maximises advisory scope subject to the constraint that every admitted type has positive VOI under the current safety state. This is a Pareto-optimal design — it is not possible to expand scope without admitting a type whose VOI is negative under the prevailing conditions. Perez-Cerrolaza et al. (2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) document that binary blocking creates genuine safety-utility trade-offs by suppressing all advisory output including positive-VOI types. Graduated scope restriction resolves this by suppressing only the negative-VOI types.

*Viva one-liner: The architecture is designed to make the safety-utility trade-off disappear — constraining only where unreliable output would harm decisions, not where it would genuinely help.*

---

### MR-6. Why not use AI confidence or uncertainty instead of environmental state?

**Direct answer: AI confidence estimates share failure modes with the AI output they evaluate — both degrade under the same distributional shift — whereas E is observed from physical sensors whose failure modes are independent of AI model degradation.**

Dalrymple et al. (2024) [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md) require that the verifier not share failure modes with the AI. A confidence-gated architecture computes confidence from the same model that produces the recommendation — under distributional shift (novel weather patterns, unseen vessel conditions), both the recommendation and the confidence estimate degrade simultaneously. The governance layer fails at the same time as the AI it governs.

Environmental state E is computed from physical sensor readings that are epistemically independent of the AI model. Wind speed is not affected by model weight updates; rainfall is not affected by training data distribution. When E indicates CAUTION, this is a fact about the physical environment, not a fact about AI model performance. Bajcsy & Fisac (2024) [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md) formalise this independence requirement: safety filters must be computable without reference to AI internal state. f(E) satisfies this strictly.

Additionally, in low-resource environments, calibrated uncertainty quantification for AI models requires substantial held-out evaluation data, computational resources for ensemble methods or Bayesian inference, and ongoing recalibration. Katende (2026) [[notes]](../notes/Rethinking%20data-efficient%20artificial%20intelligence%20for%20low-resource%20settings.md) documents these as systematic constraints in low-resource settings. Environmental state observation requires only sensors and threshold tables — achievable on edge hardware with intermittent connectivity.

*Viva one-liner: AI confidence fails when the AI fails — environmental state is computed from physical sensors whose failure modes don't depend on the AI model, which is the independence property the governance layer requires.*

---

### MR-7. Why not combine governance into a single function instead of (G, A_AI)?

**Direct answer: G(S) and A_AI(S) govern distinct aspects of AI participation — whether the AI participates and what it may produce — and separating them makes each independently auditable, independently modifiable, and formally clearer.**

G(S) is a binary gate: does the AI participate in this safety state? A_AI(S) is a set-valued function: which recommendation types may the AI produce? Combining them into a single function obscures the distinct roles. A combined function Γ(S) → {output space or ∅} does not separate the participation decision from the scope decision, making it harder to reason about which property is responsible for which safety guarantee.

The separation also enables independent modification. If operational experience shows that UNSAFE conditions should permit a limited advisory output (e.g., "conditions are too dangerous to depart — contact maritime authority"), this can be implemented by modifying A_AI(UNSAFE) without touching G(S). If G(S) needs adjustment (e.g., UNSAFE permits read-only information display), this does not affect A_AI. Separating concerns makes each change localised and each component independently certifiable.

Bloomfield & Rushby (2025) [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md) argue that safety assurance requires clear compositional structure — each layer must have a well-defined responsibility that can be independently argued. The (G, A_AI) pair provides this: G's responsibility is participation control, A_AI's responsibility is scope control. A combined Γ function has a blended responsibility that is harder to argue and audit.

*Viva one-liner: G and A_AI govern different things — separating them makes both independently auditable and independently modifiable, which matters for certification.*

---

### MR-8. Why introduce S instead of mapping directly from E → A_AI?

**Direct answer: S is a semantically meaningful intermediate that compresses the six-dimensional E into a governance-relevant category, making the governance logic inspectable, auditable, and domain-interpretable — a direct E → A_AI mapping would be an opaque function across a high-dimensional input space.**

E = {w, r, m, o, v, t} is a six-dimensional mixed-type vector. A direct mapping E → A_AI would require specifying admissible recommendation sets for every possible combination of environmental values — an exponentially large specification that is neither auditable nor certifiable. More fundamentally, it would lose the semantic compression that makes the governance logic interpretable: a fisher, a regulator, or a certification authority can understand "CAUTION mode permits Go and Delay only" but cannot meaningfully inspect a raw function from weather sensor readings to output sets.

S serves as a canonical representation of governance-relevant information about E. The mapping f: E → S performs the safety-relevant aggregation (via max-severity), and S then determines governance configuration. This two-stage design means the governance logic (S → A_AI) is simple and fully enumerable (three cases), while the complexity of environmental observation is handled by f. Each stage is independently certifiable: f can be validated against domain standards for each variable, and the S → A_AI mapping can be validated by exhaustive case analysis.

Gyllenhammar et al. (2025) [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md) use ODD→ROD→MRC as exactly this kind of intermediate abstraction — the operational domain classification compresses complex real-world conditions into a governance-relevant category. S plays the same role in this architecture.

*Viva one-liner: S makes the governance logic auditable — three cases instead of an infinite-dimensional function over raw sensor readings.*

---

### MR-9. Why deterministic governance instead of probabilistic safety models?

**Direct answer: Deterministic governance produces auditable, reproducible decisions that can be formally certified — probabilistic governance introduces stochastic variability into the safety mechanism itself, which is incompatible with the determinism requirements of safety-critical system certification standards.**

Safety-critical system certification (e.g., IEC 61508, DO-178C) requires that safety functions produce deterministic outputs for given inputs — the same environmental state must always produce the same governance response. A probabilistic governance layer (e.g., P(CAUTION | E) > 0.7 → restrict scope) introduces variability: the same E might produce SAFE on one query and CAUTION on another, depending on sampling noise. This variability is incompatible with the reproducibility requirements of formal certification.

Newcomb & Ochoa (2026) [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md) survey 46 formal methods papers for safety-critical ML and find that all approaches requiring formal guarantees use deterministic verification. Probabilistic safety bounds are used for AI output analysis, but the governance/verifier layer is deterministic. The AI layer (recommendation generation) can be probabilistic — that is appropriate for a prediction task. The governance layer must be deterministic — that is the architectural invariant that makes safety guarantees tractable.

Additionally, probabilistic models for joint environmental distributions require training data from the target domain — data that Katende (2026) [[notes]](../notes/Rethinking%20data-efficient%20artificial%20intelligence%20for%20low-resource%20settings.md) identifies as systematically absent in low-resource settings. f(E) is deterministic and requires only ordinal threshold knowledge, not joint distributional data.

*Viva one-liner: Deterministic governance produces the same response to the same inputs every time — probabilistic governance introduces exactly the variability you are trying to eliminate from safety-critical decisions.*

---

### MR-10. Why not let AI learn governance dynamically?

**Direct answer: Learned governance fails the independence requirement — a governance mechanism trained on AI behaviour shares its failure modes with the AI it governs — and dynamic governance cannot provide the formal safety guarantees that pre-specified deterministic governance provides by construction.**

If the governance layer learns from AI performance (e.g., restricting scope when AI recommendations are historically unreliable in certain conditions), it becomes dependent on AI outputs. This creates the circular dependency that Dalrymple et al. (2024) [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md) identify as a critical failure: the verifier sharing failure modes with the AI. When the AI degrades under novel conditions, the learned governance may degrade simultaneously — failing precisely when safety governance is most needed.

Bloomfield & Rushby (2025) [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md) warn against self-referential safety cases — arguments whose premises depend on the system being argued about. Learned governance is self-referential: it learns what governance is appropriate from the AI it governs. Pre-specified governance derived from domain safety standards (MMEA thresholds, meteorological severity scales) is grounded in external authority, not AI performance.

Könighofer et al. (2025) [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md) design shields as static formal specifications precisely to avoid learned governance — the shield must be provably correct independently of the agent it constrains. This architecture applies the same principle: f(E) and A_AI(S) are specified from domain knowledge, not learned from AI behaviour.

*Viva one-liner: A governance layer that learns from the AI it governs shares its failure modes — governance must be grounded in external domain authority, not derived from AI performance.*

---

## 🟡 Formal Model Edge Cases

---

### EC-1. What happens if E contains missing or incomplete data?

**Direct answer: Missing data defaults to the most conservative severity classification for that variable, ensuring that data absence escalates rather than reduces the governance response — an unknown wind speed is treated as potentially severe, not as benign.**

Each variable in E has a defined default severity under data absence: if w is unavailable, severity(w) defaults to HIGH; if m (marine warnings) is unavailable, severity(m) defaults to HIGH (absence of a broadcast could indicate communication failure, not absence of a warning). Since f(E) = max(severity(w), severity(r), ...), a single HIGH-default variable escalates S to UNSAFE or CAUTION as appropriate. This implements ALARP under data uncertainty: when in doubt, resolve conservatively.

This is not an edge case requiring special architecture — it is a parameter of the severity function. The severity classification for each variable is a mapping from (observed value | missing) → {LOW, MEDIUM, HIGH}, and "missing" maps to HIGH. The formal properties of the architecture (containment, Safety Dominance) are unaffected by this choice — they hold regardless of how defaults are set. The default values are domain parameters validated against maritime safety practice.

Katende (2026) [[notes]](../notes/Rethinking%20data-efficient%20artificial%20intelligence%20for%20low-resource%20settings.md) documents intermittent connectivity and sensor dropout as systematic features of low-resource deployment environments — not exceptional conditions. The default-to-conservative design is a deliberate response to this deployment reality, not a fallback for rare failures.

*Viva one-liner: Missing data defaults to HIGH severity — data absence escalates the governance response rather than reducing it, implementing ALARP under sensor dropout.*

---

### EC-2. What if environmental variables produce conflicting signals?

**Direct answer: Max-severity aggregation by design resolves conflicts in favour of the most severe signal — conflicting signals (e.g., calm seas but high wind) produce the governance response appropriate for the worst-case component, which is the correct safety response.**

"Conflicting signals" in E means that different variables classify at different severity levels — wind HIGH, rain LOW, marine warnings NONE. This is not a conflict in the logical sense (variables do not contradict each other); it is a multi-factor assessment where one factor is more severe than others. Max-severity resolves this by treating each variable as an independent safety dimension: S = UNSAFE if any variable is at UNSAFE severity, S = CAUTION if no variable is at UNSAFE but at least one is at CAUTION, S = SAFE only if all variables are at SAFE severity.

This resolution is conservative and correct. A vessel facing calm seas but sustained gale-force winds is in a dangerous condition — the high wind is not "cancelled" by the calm seas. Weighted aggregation that averages wind severity down due to good sea state would mask the genuine hazard. Max-severity ensures the most dangerous component determines the governance response. This is the weakest-link principle: safety is determined by the weakest safety dimension.

*Viva one-liner: Variables don't conflict — they each represent an independent safety dimension, and max-severity correctly responds to the worst dimension regardless of the others.*

---

### EC-3. Is max-severity always correct in such cases?

**Direct answer: Max-severity is always correct for safety governance because it is the only aggregation function that guarantees no dangerous variable can be masked by benign values — any softer aggregation (weighted average, majority vote) creates the possibility of a masked hazard.**

The formal argument: define an aggregation function g: (severity_1, ..., severity_n) → {SAFE, CAUTION, UNSAFE} to be "hazard-safe" if g(..., UNSAFE, ...) = UNSAFE for any input containing at least one UNSAFE severity component. Max-severity satisfies this. A weighted average does not — sufficiently low weights on the UNSAFE component can produce a SAFE or CAUTION output. A majority vote does not — a minority of UNSAFE variables can be outvoted by SAFE variables. Only max-severity guarantees hazard-safety.

The cost of max-severity is over-classification: some states are classified more severely than a nuanced multi-factor assessment would suggest. This is the acceptable side of the ALARP trade-off — false alarms (over-conservative) are preferable to missed escalations (under-conservative). Perez-Cerrolaza et al. (2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) confirm ALARP as the appropriate principle for safety-critical governance under uncertainty.

*Viva one-liner: Max-severity is the only aggregation that guarantees no dangerous component can be masked — any softer function creates a masked-hazard vulnerability.*

---

### EC-4. Can f(E) handle extreme or unseen inputs?

**Direct answer: f(E) handles unseen inputs correctly because its logic is threshold-based, not learned — any input value either falls below, within, or above defined thresholds, and the highest applicable threshold determines severity regardless of whether that exact value appeared in historical data.**

f(E) is not a machine learning model — it does not generalise from training data or extrapolate from learned representations. It is a deterministic function that compares each variable against domain-defined thresholds. A wind speed of 150 knots has never been observed in deployment — but the threshold function correctly classifies it as UNSAFE (above the UNSAFE threshold), not as an out-of-distribution anomaly requiring special handling. The threshold logic is complete for all possible input values.

This robustness to extreme inputs is a consequence of the architecture's design choice to use a deterministic rule-based governance function rather than a learned one. Newcomb & Ochoa (2026) [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md) identify out-of-distribution robustness as a critical challenge for learned safety components — deterministic threshold functions do not share this challenge. Sensor saturation (a reading that exceeds the sensor's measurement range) is handled by the missing-data default (EC-1): a saturated reading is treated as unknown → defaults to HIGH severity.

*Viva one-liner: f(E) is threshold-based, not learned — extreme values are classified by the highest applicable threshold, not treated as out-of-distribution anomalies.*

---

### EC-5. Can the model scale if more variables are added to E?

**Direct answer: Yes — adding variables to E requires only defining their severity classification function and adding them to the max-severity computation; all formal properties (containment, Safety Dominance) are preserved because the architecture of f(E) is compositional.**

E can be extended to E' = {w, r, m, o, v, t, e₁, e₂, ...} where new variables carry their own severity classification. f(E') = max(severity(w), ..., severity(t), severity(e₁), ...) extends naturally. The safety argument for the new variables must be validated independently (what thresholds are appropriate for e₁?), but the formal architecture is unchanged. Adding variables can only leave S unchanged or escalate it — it cannot reduce S, since max-severity only responds to the maximum. This monotonicity is a useful extensibility property.

Adding variables does create domain validation work: each new variable requires threshold calibration against authoritative domain standards. This is not an architectural limitation but an epistemological one — any safety-relevant variable requires validated thresholds before inclusion. The architecture provides the formal structure; domain expertise provides the threshold values.

*Viva one-liner: Adding variables to E requires domain calibration for each new variable — the architecture composes them naturally through max-severity without changing any formal properties.*

---

### EC-6. Is the model still valid if E changes domain?

**Direct answer: The architecture is domain-independent — the formal structure (S = f(E), G(S), A_AI(S), containment, Safety Dominance) transfers to any domain; only E, the severity thresholds in f, and the type sets in A_AI(S) require domain-specific re-specification.**

The formal model makes no assumption about what variables populate E, what thresholds define severity levels, or what recommendation types populate A_AI. These are domain parameters. In a healthcare triage domain, E might contain {heart_rate, oxygen_saturation, blood_pressure, consciousness_level}; A_AI(SAFE) might contain {Diagnose, Prescribe, Refer}; A_AI(CAUTION) might contain {Refer, Alert}. The formal properties (containment, Safety Dominance) hold in the same way.

Gyllenhammar et al. (2025) [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md) demonstrate ODD/ROD/MRC applying across different road environments. Perez-Cerrolaza et al. (2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) survey safety AI across industrial, transportation, and healthcare domains — the governance principles transfer even though domain variables differ significantly. The architecture's contribution is the formal structure and the Safety Dominance property, both of which are domain-generic.

*Viva one-liner: The architecture transfers to any domain — the formal structure is domain-independent; only the variable definitions, thresholds, and type sets require domain-specific re-specification.*

---

### EC-7. Can different E produce the same S? Is that acceptable?

**Direct answer: Yes, many-to-one mapping from E to S is both expected and correct — S captures only the governance-relevant information about E, and different physical conditions with the same safety severity level should receive the same governance response.**

By design, S = f(E) compresses the six-dimensional E into three categories. Many distinct E configurations will map to CAUTION: {w=20, r=15, m=ADVISORY, o=MODERATE, v=GOOD, t=DAY} and {w=15, r=25, m=NONE, o=HIGH, v=GOOD, t=NIGHT} might both classify as CAUTION via different variables reaching MEDIUM severity. Both receive the same governance response: A_AI(CAUTION) = {Go, Delay}. This is correct — both environmental configurations warrant the same governance mode even though they have different physical characteristics.

The AI layer still receives the full E for reasoning — the many-to-one compression in S does not deprive the AI of environmental detail. The AI can use the full six-dimensional vector to distinguish between these two CAUTION configurations and tailor its Go/Delay recommendation accordingly (e.g., "Go — but rain is the primary concern, check waterproofing" vs. "Delay — ocean state is the primary constraint"). S compresses only the governance-relevant information; E preserves all detail for AI reasoning.

*Viva one-liner: Many-to-one mapping is correct — different conditions with the same severity warrant the same governance, and the AI still uses full E for recommendation detail.*

---

### EC-8. Does the model lose important information due to many-to-one mapping?

**Direct answer: No — the AI layer retains access to full E for recommendation generation; S compresses only governance-relevant information, and the information "lost" in compression is exactly the information that should not influence the governance decision.**

The governance question is: what category of recommendation is safe to produce? The answer depends on the severity level of environmental conditions, not on their specific physical values. Whether CAUTION results from high wind or high rainfall is irrelevant to the governance decision (A_AI(CAUTION) = {Go, Delay} in both cases). The many-to-one mapping discards information that is governance-irrelevant while the AI layer retains it for recommendation-relevant reasoning.

This is analogous to the ODD/ROD/MRC abstraction in Gyllenhammar et al. (2025) [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md): classifying a road environment as "Reduced Operational Domain" does not specify whether the limitation is fog, rain, or ice — but the governance response (reduced autonomous capability) is the same. The detail is retained in the sensor data the vehicle continues to use for navigation; the abstraction exists only for governance purposes.

*Viva one-liner: S discards only information irrelevant to governance — the AI keeps full E for reasoning, so no decision-relevant information is lost.*

---

### EC-9. Can advisory space become too limited to be useful?

**Direct answer: A_AI(CAUTION) = {Go, Delay} provides the minimum useful advisory content for a departure decision under intermediate conditions — it answers the primary decision question the fisher faces, and suppressing more would eliminate genuinely positive-VOI content.**

The test for "too limited to be useful" is whether the admitted types address the decision the user actually needs to make. Under CAUTION, the fisher's primary decision is: should I depart now or not? Go and Delay directly address this question. Removing either (e.g., only admitting Delay under CAUTION) would eliminate a positive-VOI output — there will be genuine CAUTION conditions under which Go is the correct and safe recommendation. A_AI(CAUTION) is therefore the minimal set that preserves decision usefulness.

If operational evaluation showed that {Go, Delay} was insufficient for some decision context (e.g., fishers needed route guidance even under CAUTION), the appropriate response would be to add a Route type to A_AI(CAUTION) after validating that Route predictions are reliable under CAUTION-level environmental conditions. The architecture supports this — A_AI is a parameter. The argument for any type's inclusion in any state's admissible set is a reliability-under-state argument, not a "more is better" argument.

*Viva one-liner: {Go, Delay} answers the primary question the fisher faces under CAUTION — it is the minimum useful set, not an arbitrary restriction.*

---

### EC-10. Can recommendation types expand beyond the defined set R?

**Direct answer: Yes — the type set R is a domain parameter, not a fixed formal property; new types can be added after validating their reliability under each safety state, and the formal architecture accommodates expansion without structural change.**

The formal architecture specifies that A_AI(S) ⊆ R for each S, with the containment and Safety Dominance properties holding for whatever R is defined. Adding a new type τ to R requires: (1) defining the safety states under which τ is admissible — i.e., specifying whether τ ∈ A_AI(SAFE), τ ∈ A_AI(CAUTION), both, or neither; (2) validating that τ has positive VOI in each state where it is admitted; (3) verifying that containment still holds after the update.

For example, adding a Route type (recommended fishing route) would likely be admitted under SAFE only, since route optimisation requires stable environmental predictions across the planned trip. This would update A_AI(SAFE) = {Go, Delay, DepartureTime, Duration, Route} — containment is preserved since A_AI(CAUTION) ⊆ A_AI(SAFE) still holds. Safety Dominance continues to hold since the AI cannot produce Route recommendations when Route ∉ A_AI(S) for the current S.

*Viva one-liner: R is a domain parameter — types can be added by validating reliability under each safety state and verifying containment is preserved.*

---

## 🟢 Architecture Design Questions

---

### AD-1. Why separate classification (f) and governance (G, A_AI)?

**Direct answer: Classification and governance serve distinct functions with different validation requirements — f maps physical conditions to safety categories and is validated against domain meteorological standards, while G and A_AI map categories to participation and scope decisions and are validated against reliability-of-recommendation-type evidence.**

f: E → S requires domain meteorological expertise to calibrate — what wind speed threshold distinguishes CAUTION from UNSAFE? This is validated against MMEA maritime guidelines and Malaysian Meteorological Department standards. The governance functions G: S → {0,1} and A_AI: S → 2^R require reliability-of-inference expertise — which recommendation types are reliable under CAUTION conditions? This is validated against evidence on AI prediction reliability under environmental uncertainty.

Mixing classification and governance into a single function would require simultaneously validating both meteorological thresholds and recommendation reliability with a single artefact — making the validation burden undifferentiated and harder to assign to domain experts. Separation allows meteorologists to certify f independently of AI reliability analysts certifying A_AI. This matches the principle of separation of concerns in dependable systems design and supports Bloomfield & Rushby's (2025) [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md) requirement for compositional safety assurance.

*Viva one-liner: f is a meteorological question; G and A_AI are a recommendation-reliability question — separating them lets each be validated by the appropriate domain experts.*

---

### AD-2. Why is governance applied before AI reasoning, not after?

**Direct answer: Pre-hoc governance defines the output space before generation, ensuring the AI never enters a reasoning process that would produce inadmissible outputs — post-hoc governance filters outputs after generation, leaving the AI free to reason toward outputs it cannot produce, which wastes computation and may influence intermediate reasoning.**

Shamsujjoha et al. (2025) [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md) identify 13 guardrail action types in existing AI safety architectures — all are post-hoc. They act on outputs after generation. The limitation is that the AI has already completed its reasoning toward a DepartureTime recommendation; the guardrail then discards it. This wastes the inference computation (significant in edge deployments with limited resources) and may produce coherence issues: an AI that has internally reasoned toward 06:30 departure but is told it cannot say so may produce inconsistent remaining outputs.

Pre-hoc governance (A_AI defined before AI reasoning begins) constrains the generation process from the start. The AI knows before reasoning begins that DepartureTime is not in its admissible set — it reasons toward a Go/Delay recommendation directly. This is more efficient computationally and produces more coherent outputs since the AI's full reasoning capacity is directed at the admissible types. Wang et al. (2026) [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md) implement per-action binary enforcement at runtime — a form of pre-hoc constraint on which actions may be taken, analogous to A_AI but at the action level.

*Viva one-liner: Pre-hoc governance means the AI reasons toward admissible outputs from the start — post-hoc filtering lets the AI reason toward outputs it cannot produce, wasting computation and risking coherence.*

---

### AD-3. Could governance be implemented as a post-processing filter only?

**Direct answer: A post-processing filter can enforce the same output constraints as pre-hoc governance, but it cannot provide the same formal guarantees by construction — Safety Dominance is a property of the system architecture, not just its outputs, and post-hoc filtering can fail or be bypassed in ways that pre-hoc definition cannot.**

A post-hoc filter that removes DepartureTime from AI outputs when S=CAUTION would produce the same visible outputs as the pre-hoc architecture. But the formal property AI(E) ⊆ A_AI(S) is satisfied by construction in the pre-hoc design — it follows from the definition of the output space. In a post-hoc design, it is satisfied contingently — only if the filter correctly identifies and removes all inadmissible outputs. The filter can fail (miss an inadmissible output, classify content incorrectly) in ways the pre-hoc design cannot.

Shamsujjoha et al. (2025) [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md) document that post-hoc guardrails are static and not state-conditioned — they apply the same filtering regardless of safety state. A post-hoc filter conditioned on S is possible in principle but requires the filter to correctly identify recommendation type in natural language outputs, which introduces its own failure modes. Pre-hoc governance eliminates this problem: if A_AI(CAUTION) = {Go, Delay}, the AI system's output generation mechanism is constrained to these types by design.

*Viva one-liner: Post-hoc filtering satisfies Safety Dominance contingently — pre-hoc governance satisfies it by construction, which is a stronger formal guarantee.*

---

### AD-4. Why not combine safety gating and advisory restriction into one layer?

**Direct answer: G(S) and A_AI(S) are logically independent functions that can vary independently — combining them obscures cases where one changes without the other and removes the ability to certify each independently.**

Consider a modified design where UNSAFE permits read-only information (current safety state display) but no recommendations: G(UNSAFE) = 0 for recommendations, but the system remains active for information display. In the current architecture, this is captured by modifying A_AI(UNSAFE) to include an Information type while G(UNSAFE) = 0 for advisory outputs — the two functions handle different participation modes. A combined layer would struggle to represent this distinction cleanly.

More fundamentally, G and A_AI are validated differently. G(S) is validated by the argument that AI participation is harmful when S=UNSAFE — this is a safety argument about participation risk. A_AI(S) is validated by the argument that specific recommendation types have negative VOI under specific safety states — this is a reliability argument about information quality. Mixing these arguments into a single combined layer conflates two distinct justificatory requirements. Bloomfield & Rushby (2025) [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md) require that each safety layer have a clear, independently arguable responsibility.

*Viva one-liner: G and A_AI answer different questions — participation risk vs. recommendation reliability — and each requires a different validation argument, so separating them is not redundant.*

---

### AD-5. Why is the architecture layered instead of integrated?

**Direct answer: Layered architecture ensures each component (sensor observation, classification, governance, AI reasoning) can fail independently and be certified independently — integrated architectures create shared failure modes between components that should be independent.**

Dalrymple et al. (2024) [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md) require that the safety verifier not share failure modes with the AI. This is only achievable in a layered architecture where the governance layer (f, G, A_AI) is implemented separately from the AI reasoning layer. An integrated architecture — where governance logic and recommendation generation share computational resources, training processes, or model weights — would create shared failure modes by construction.

Perez-Cerrolaza et al. (2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) review safety architectures in industrial and transportation domains and consistently find layered designs in certified systems. The layering allows incremental certification: the sensor layer, classification layer, governance layer, and AI layer can be certified against their respective standards independently before system-level integration testing. An integrated design requires the entire system to be re-certified whenever any component changes.

*Viva one-liner: Layering ensures the governance layer can fail independently from the AI layer — integration would create shared failure modes that invalidate the independence guarantee.*

---

### AD-6. What happens if governance fails but AI still runs?

**Direct answer: Governance failure (f(E) producing incorrect S) propagates through the architecture to incorrect A_AI, which is why governance failure modes are designed to be conservative — sensor dropout defaults to HIGH severity, threshold errors prefer over-classification — and sensor integrity monitoring provides a detection layer.**

If f(E) produces S=SAFE when S should be CAUTION (under-conservative governance failure), then A_AI(SAFE) = {Go, Delay, DepartureTime, Duration} is applied when A_AI(CAUTION) = {Go, Delay} should have been applied. The AI can produce DepartureTime and Duration recommendations under borderline conditions. This is the most dangerous failure mode and is addressed by: (1) conservative threshold design (near-threshold inputs default to higher severity, per HR-5); (2) sensor validation that rejects readings outside physical plausibility ranges; (3) conservative defaults for missing data (per EC-1).

If f(E) produces S=CAUTION when S should be SAFE (over-conservative governance failure), the AI is restricted unnecessarily. This is the ALARP-preferred failure mode. If f(E) produces S=UNSAFE when the AI should be participating, G(UNSAFE)=0 and the AI is silenced unnecessarily — the fisher makes an unassisted decision, which was the pre-AI baseline. The architecture degrades gracefully: governance failure in the conservative direction produces conservative AI behaviour, not unsafe AI behaviour.

*Viva one-liner: Conservative governance failures restrict the AI unnecessarily — which is the ALARP-preferred failure mode — and the architecture is designed to fail in this direction.*

---

### AD-7. Can the architecture be simplified without losing key properties?

**Direct answer: The minimal architecture is E → f(E) → A_AI(S) with Safety Dominance; G(S) can be derived as a special case where A_AI(UNSAFE) = ∅ implicitly gates participation — no further simplification is possible without losing either the graduated property or the formal Safety Dominance guarantee.**

G(S) is technically redundant given A_AI(UNSAFE) = ∅: if no recommendation types are admissible, the AI effectively does not participate. G(S) is included as an explicit architectural element for clarity (it makes participation control visible and independently certifiable) and to allow participation control independent of type control (e.g., a state where the AI participates for information display but not advisory purposes). If G is merged into A_AI, the architecture becomes E → f(E) → A_AI(S) with A_AI(UNSAFE) = ∅ making silence explicit. This is architecturally equivalent.

Further simplification is not possible without loss. Removing S (mapping directly E → A_AI) loses auditability (MR-8). Removing the type taxonomy (making A_AI a binary admit/reject function) loses the graduated property and collapses to binary governance. Removing f (mapping directly from raw E to A_AI) conflates meteorological thresholding with governance logic, losing independent certifiability. The architecture is already at its minimal structure for the properties it must satisfy.

*Viva one-liner: The minimal architecture is E → f(E) → A_AI(S) with Safety Dominance — removing any element loses either the graduated property or formal tractability.*

---

### AD-8. What is the minimal version of the architecture?

**Direct answer: The minimal version is a deterministic function f mapping the environmental state vector E to a safety state S, paired with a state-indexed admissible type set A_AI(S), satisfying strict containment across states and Safety Dominance for all AI outputs.**

Formally: (f, A_AI) where:
- f: E → {SAFE, CAUTION, UNSAFE} (deterministic, threshold-based)
- A_AI: {SAFE, CAUTION, UNSAFE} → 2^R (state-indexed type set)
- Containment: A_AI(UNSAFE) ⊆ A_AI(CAUTION) ⊆ A_AI(SAFE)
- Safety Dominance: ∀E, AI(E) ⊆ A_AI(f(E))

G(S) is implicit in A_AI(UNSAFE) = ∅. The minimal version requires four elements: an environmental observation mechanism, a deterministic classification function, a state-indexed admissible set satisfying containment, and an AI system constrained to produce outputs in the admissible set. Remove any one: without classification, governance is ungrounded; without admissible sets, there is no scope restriction; without containment, the graduated property is lost; without Safety Dominance, the formal guarantee disappears.

*Viva one-liner: The minimal version is (f, A_AI) with containment and Safety Dominance — four properties, no further reduction.*

---

## 🔵 Practical / Deployment Questions

---

### PD-1. How do you validate and calibrate safety thresholds?

**Direct answer: Thresholds are initialised from authoritative domain standards (MMEA maritime safety guidelines, Malaysian Meteorological Department Beaufort-scale equivalents), validated against historical incident data where available, and refined through DSR evaluation cycles with domain expert review.**

Each variable in E has established domain thresholds. Wind speed w thresholds are grounded in Beaufort scale categories used by MMEA and Malaysian fishing authority communications — Force 4 (>13 knots) for CAUTION, Force 6 (>22 knots) for UNSAFE, calibrated against the vessel classes typical in Malaysian coastal small-scale fisheries. Marine warning codes m directly import MMEA's categorical system (ADVISORY, WARNING, DANGER) as severity levels. Ocean state o thresholds reference WMO sea state scale categories. Vessel condition v thresholds are derived from pre-departure checklist standards in Malaysian maritime regulations.

Historical validation uses available incident data from MMEA maritime accident reports and Department of Fisheries Malaysia records — cross-referencing the environmental conditions at time of incident against what S classification those conditions would have produced. Katende (2026) [[notes]](../notes/Rethinking%20data-efficient%20artificial%20intelligence%20for%20low-resource%20settings.md) documents the limited availability of such data in low-resource settings — the architecture is designed so that thresholds can be set conservatively from domain standards even in the absence of rich historical datasets, with refinement possible as data accumulates.

*Viva one-liner: Thresholds start from authoritative domain standards that pre-exist the architecture, get cross-validated against historical incidents, and are refined through DSR evaluation — they are not designed from scratch.*

---

### PD-2. What happens if sensor data is incorrect or unavailable?

**Direct answer: Incorrect data within plausible physical ranges is handled by conservative threshold margins; out-of-range data triggers sensor failure detection and defaults to HIGH severity for the affected variable; unavailable data defaults to HIGH severity — all pathways resolve conservatively.**

The three sensor failure modes are handled distinctly. First, incorrect data within physical plausibility range (e.g., anemometer miscalibration reporting 18 knots instead of 22): threshold margins and hysteresis (HR-5) provide tolerance for small calibration errors. Near-threshold inputs default conservatively (HR-10). This mode cannot be eliminated without external reference sensors; the architecture's conservative defaults limit the damage from small calibration errors.

Second, out-of-range data (e.g., anemometer reporting −5 knots or 500 knots): a sensor validation layer rejects readings outside physically possible ranges and treats the variable as missing. Missing defaults to HIGH severity (EC-1). This ensures sensor hardware failure escalates rather than reduces the safety response. Third, unavailable data (sensor offline, communication failure, intermittent connectivity): treated identically to missing — HIGH severity default.

The marine warning variable m has special treatment: if the MMEA broadcast channel is unavailable, m defaults to HIGH severity (ADVISORY or higher assumed) rather than NONE (no warnings), because communication failure cannot be interpreted as confirmation of safe conditions.

*Viva one-liner: Every sensor failure pathway — bad data, out-of-range, unavailable — resolves conservatively to HIGH severity, so sensor failures escalate the governance response rather than reducing it.*

---

### PD-3. How robust is the system in low-resource environments?

**Direct answer: The architecture is specifically designed for low-resource constraints — deterministic governance requires no ML inference, sensor-based classification has minimal computational requirements, and edge deployment with offline-capable rule tables is feasible on commodity hardware.**

Katende (2026) [[notes]](../notes/Rethinking%20data-efficient%20artificial%20intelligence%20for%20low-resource%20settings.md) identifies the primary constraints in low-resource AI deployments: limited labelled training data, intermittent connectivity, low-power edge hardware, and limited maintenance capacity. The governance layer (f, G, A_AI) addresses each: f is a deterministic threshold function requiring no training data, no ML inference, and negligible computation — it can run on a microcontroller. The type-restriction logic (A_AI) is a lookup table. Neither requires connectivity to operate.

The AI recommendation layer does require more resources, but its governance wrapper is resource-light. The architecture separates the computationally intensive component (AI recommendation generation) from the safety-critical component (governance), allowing the governance layer to remain operational even if the AI layer has limited computational access. In an extreme resource constraint, the governance layer can operate as a standalone safety classifier even without the AI layer — providing S classification to inform human decisions directly.

*Viva one-liner: The governance layer runs on a lookup table — it is the lightest possible computational component and remains operational when the AI layer cannot run.*

---

### PD-4. Can the system operate offline or with partial data?

**Direct answer: Yes — the governance layer is fully offline-capable since f is a deterministic threshold computation requiring no connectivity; the AI recommendation layer may require connectivity for model inference depending on implementation, but governance continues to operate independently.**

The governance computation E → f(E) → (G, A_AI) requires only: (1) sensor readings from local hardware (anemometer, rain gauge, clock); (2) threshold tables stored locally; (3) a lookup table for A_AI. All three are local resources requiring no network connectivity. Marine warning data m may require receiving an MMEA broadcast signal — if unavailable, defaults to HIGH severity (EC-1). The system can classify E and enforce A_AI completely offline.

The AI recommendation layer, depending on implementation, may use a locally deployed model (fully offline) or a cloud API (requiring connectivity). The architecture supports both — the governance layer wraps the AI regardless of where the AI computation occurs. In a pure offline deployment, a lightweight local model operates within the governance constraints. In a connected deployment, a cloud model operates within the same constraints. The formal properties (Safety Dominance, containment) hold in both cases.

*Viva one-liner: Governance is fully offline — threshold tables and lookup tables require no connectivity; only the AI inference layer may need connectivity, and that is an implementation choice not an architectural requirement.*

---

### PD-5. How do users interpret CAUTION mode in practice?

**Direct answer: CAUTION mode corresponds directly to the "cautious-go" mental model that Malaysian fishers already use — Gao (2024) documents this tripartite schema in Penang fisheries — and the architecture's CAUTION advisory set {Go, Delay} operationalises that existing cognitive category.**

Gao (2024) [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md) documents that small-scale fishers in Penang employ a tripartite decision schema: go, cautious-go, don't-go. The "cautious-go" category represents conditions where departure is possible but requires care — corresponding directly to the CAUTION state where Go is admissible but DepartureTime precision is not. The architecture does not impose a foreign cognitive category on users; it formalises one they already use.

User interface design for CAUTION mode makes the state visible and its implications clear: a CAUTION indicator (amber/yellow signal consistent with traffic-light convention used by Flehmig et al. (2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md)) with a brief explanation of which advisory types are available. McGrath et al. (CHAI-T) [[notes]](../notes/Collaborative%20Human-AI%20Trust%20(CHAI-T)-%20A%20Process%20Framework%20for%20Active%20Management%20of%20Trust%20in%20Human-AI-Collaboration.md) argue that distinct distinguishable modes support trust calibration — CAUTION as a visually distinct state helps users build accurate expectations of what the system will and will not say in each mode.

*Viva one-liner: CAUTION maps to the "cautious-go" category fishers already use — the architecture formalises an existing cognitive category, it doesn't create a new one.*

---

### PD-6. Does CAUTION increase user confusion or cognitive load?

**Direct answer: CAUTION reduces cognitive load compared to binary governance by providing the advisory content that is reliable and withholding what is not — users receive a clear, actionable signal rather than either a full recommendation they cannot fully trust or complete silence.**

Under binary governance, a fisher facing intermediate conditions receives either: (a) a full advisory set including DepartureTime — which they should not fully trust but don't know which parts to discount — or (b) complete AI silence, leaving them to make all judgments without support. Both impose cognitive load: (a) requires the user to mentally discount unreliable elements; (b) requires the user to handle all decision-making without aid.

Under CAUTION, the user receives {Go, Delay} — exactly the admissible outputs. They do not need to discount unreliable elements (DepartureTime is absent) and they receive meaningful decision support on the core question. Wen et al. (2025) [[notes]](../notes/Risk%20Perception%20in%20Complex%20Systems-%20A%20Comparative%20Analysis%20of%20Process%20Control%20and%20Autonomous%20Vehicle%20Failures.md) document that mode confusion — not knowing what the automated system is doing — is a primary driver of over-reliance accidents. CAUTION is a clearly labelled mode with a distinct visual indicator and a defined advisory scope: mode confusion is minimised because the system's capabilities in CAUTION are explicit.

*Viva one-liner: CAUTION reduces confusion by making the system's scope explicit — users know what they are getting, which is less confusing than a full recommendation they cannot fully trust.*

---

### PD-7. What happens if users ignore AI recommendations?

**Direct answer: The architecture is advisory only — ignoring recommendations is the correct baseline behaviour for a decision-support system, and the formal properties ensure that what is ignored is reliable advisory content, not safety instructions that must be followed.**

Advisory AI systems produce recommendations that humans may accept, modify, or reject. This is the intended mode of operation — the system supports human decision-making, it does not supplant it. Rahim et al. (2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) document that fishers override binary warnings when economic necessity is high — this is not a system failure; it is human agency operating within a decision context the system cannot fully model (livelihood pressure, family obligations, knowledge of local conditions).

The architecture improves on this baseline not by preventing overrides but by ensuring that when the AI does speak (G(S)=1), what it says is within the reliable type set for the current conditions. If a fisher ignores a Delay recommendation under CAUTION and departs, they do so with full situational awareness — they have not been misled by a false-precision DepartureTime recommendation. The architecture's safety contribution is ensuring the AI does not mislead; it cannot and should not prevent human agency.

*Viva one-liner: Advisory systems are designed to be ignored — the architecture ensures that when the AI speaks, it speaks reliably; whether the human acts on it is appropriately the human's decision.*

---

### PD-8. What happens if users over-rely on AI?

**Direct answer: The architecture reduces over-reliance risk by suppressing the recommendation types that most strongly invite over-reliance (precise DepartureTime and Duration under CAUTION) while retaining the types that support, rather than replace, human judgment.**

Wen et al. (2025) [[notes]](../notes/Risk%20Perception%20in%20Complex%20Systems-%20A%20Comparative%20Analysis%20of%20Process%20Control%20and%20Autonomous%20Vehicle%20Failures.md) attribute over-reliance accidents in process control (20%) and autonomous vehicles (30%) to automation bias — users defer to system outputs even when the system is wrong. Automation bias is strongest for specific, precise outputs (a departure time of 06:30 is more easily over-relied upon than "Delay"). By suppressing DepartureTime under CAUTION, the architecture removes the recommendation type most susceptible to automation bias in the domain's highest-risk conditions.

Schrills et al. (2025) [[notes]](../notes/Questioning%20Trust%20in%20AI%20Research-%20Exploring%20the%20Influence%20of%20Trust%20Assessment%20on%20Dependence%20in%20AI-Assisted%20Decision-Making.md) show that instructed reliability drives dependence (r=0.42–0.45). The architecture's state-visible design (CAUTION indicator) instructs users that the system is operating in a restricted-reliability mode, calibrating their dependence expectations. McGrath et al. (S-TIAS) [[notes]](../notes/Measuring%20trust%20in%20artificial%20intelligence-%20validation%20of%20an%20established%20scale%20and%20its%20short%20form.md) provide a validated trust instrument that can be deployed in evaluation to measure whether CAUTION mode produces the appropriate reduction in dependence.

*Viva one-liner: Suppressing DepartureTime under CAUTION removes the recommendation type most susceptible to automation bias — the architecture reduces over-reliance by design, not by instruction.*

---

### PD-9. How do you ensure trust calibration?

**Direct answer: Trust calibration is achieved structurally — three distinct labelled states with different advisory scopes ensure users learn different reliance behaviours for each state, and the architecture's pre-hoc scope definition means the AI's actual capabilities in each state match what users are shown.**

McGrath et al. (CHAI-T) [[notes]](../notes/Collaborative%20Human-AI%20Trust%20(CHAI-T)-%20A%20Process%20Framework%20for%20Active%20Management%20of%20Trust%20in%20Human-AI-Collaboration.md) argue that effective trust calibration requires discrete distinguishable modes that users can develop distinct reliance strategies for. The three safety states provide exactly this: SAFE (full advisory set, high reliance appropriate), CAUTION (restricted advisory set, moderate reliance appropriate), UNSAFE (AI silent, human judgment exclusively). Each mode is visibly labelled and its advisory scope is predictable and consistent across interactions.

Calibration requires that stated system capabilities match actual capabilities. In a post-hoc filter design, the AI might generate a DepartureTime recommendation that the filter then removes — the gap between generation and display creates unpredictability in what users receive under each mode. In the pre-hoc architecture, what users see is what the type set defines: if the system is in CAUTION, users always see {Go, Delay} options and never see DepartureTime. Consistency across interactions enables learning of accurate reliance strategies. Atf & Lewis (2026) [[notes]](../notes/Is%20Trust%20Correlated%20With%20Explainability%20in%20AI%3F%20A%20Meta-Analysis.md) show explanations have minimal trust effect (r=0.194) — the architecture achieves calibration through behavioural consistency, not explanation.

*Viva one-liner: Trust calibration comes from consistent, predictable advisory scope in each state — users learn what to rely on by experiencing what the system does in each mode, not by reading warnings about it.*

---

## 🟣 Theoretical / Contribution Questions

---

### TC-1. Is the architecture truly novel or a combination of existing ideas?

**Direct answer: The specific combination — environment-conditioned graduated output-type restriction with formal Safety Dominance guarantee — does not appear in any of the 148+ papers across four independent systematic reviews; individual components have precedents, but the combination and the formal property are original contributions.**

Individual precedents exist: Baxi (2026) [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) provides K-tier graduated permissions with containment — but conditioned on AI robustness, not environmental state. Gyllenhammar et al. (2025) [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md) provide ODD/ROD/MRC three-level hierarchy — but governing autonomous system capabilities, not AI advisory scope. Flehmig et al. (2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md) provide traffic-light governance — but governing monitoring intensity, not output type space. None combine: (a) environmental-state conditioning, (b) type-level output space restriction, (c) pre-hoc definition, (d) formal Safety Dominance for graduated governance.

Novelty in formal system design regularly emerges from novel combinations of properties rather than wholly unprecedented primitives. The Safety Dominance property AI(E) ⊆ A_AI(S) formalised for graduated governance is a new property — the literature addresses safety as binary constraints (safe/unsafe action) not as graduated type-indexed admissible sets. Four systematic reviews confirm the gap is real: no reviewed paper contains an architecture with all four components.

*Viva one-liner: Each component has a precedent somewhere — what is novel is the specific combination conditioned on environmental state with formal Safety Dominance, which four independent systematic reviews confirm does not exist in the literature.*

---

### TC-2. How is this work different from safety shields, adaptive autonomy, guardrails, and hybrid AI?

**Direct answer: Safety shields govern at the action level (per-action binary), adaptive autonomy governs at the authority level (who decides), guardrails govern at the output level (post-hoc content evaluation), hybrid AI governs at the integration level (how human and AI combine) — this architecture governs at the type level (which categories of recommendation are admissible), which is a distinct governance dimension not present in any of these.**

Safety shields (Könighofer et al. (2025) [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md), Corsi et al. (2024) [[notes]](../notes/Verification-Guided%20Shielding%20for%20Deep%20Reinforcement%20Learning.md), Odriozola-Olalde et al. (2023) [[notes]](../notes/Shielded%20Reinforcement%20Learning-%20A%20review%20of%20reactive%20methods%20for%20safe%20learning.md)) intercept individual actions and classify each as safe or unsafe — binary, per-action, post-hoc. They do not restrict the space of action types available to the agent as a function of environmental state.

Adaptive autonomy frameworks redistribute authority between human and AI as conditions change — when conditions worsen, the human takes more control. The AI's output type space is not restricted; authority over acting on it is redistributed. Over-reliance under autonomy reduction is possible (Wen et al. (2025) [[notes]](../notes/Risk%20Perception%20in%20Complex%20Systems-%20A%20Comparative%20Analysis%20of%20Process%20Control%20and%20Autonomous%20Vehicle%20Failures.md)) because the AI can still produce DepartureTime recommendations that anchor human judgment even when the human nominally decides.

Guardrails (Shamsujjoha et al. (2025) [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md)) evaluate outputs after generation against static rules — not conditioned on environmental state, not pre-hoc, not type-indexed.

Type-level pre-hoc environment-conditioned restriction is absent from all three paradigms and from hybrid AI frameworks. The governance dimension is distinct.

*Viva one-liner: Shields gate actions, autonomy frameworks redistribute authority, guardrails filter outputs — this architecture restricts which categories of recommendation are generated, which is a different governance dimension.*

---

### TC-3. What is your main contribution in one sentence?

**Direct answer: This work contributes the first formally specified graduated safety-state-gated architecture in which the admissible AI recommendation type space is indexed to a classified environmental state, satisfying a novel Safety Dominance property by construction and addressing a gap confirmed by four independent systematic reviews.**

*Viva one-liner: The contribution is a formally specified architecture in which environmental state determines which recommendation categories the AI may produce — graduated, pre-hoc, type-level, and formally guaranteed — a combination absent from 148+ reviewed papers.*

---

### TC-4. Can the architecture be generalised beyond fisheries?

**Direct answer: Yes — the formal structure (f, G, A_AI) with Safety Dominance and containment is domain-agnostic; the fisheries domain provides the empirical grounding and validation context, but the architecture generalises to any domain with a classifiable environmental/operational state and a typed advisory output space.**

The generalisation requires: (1) an observable state vector E appropriate to the domain; (2) a classification function f: E → {discrete safety states} grounded in domain safety standards; (3) a type taxonomy R for advisory outputs in the domain; (4) assignment of types to admissible sets A_AI(S) based on reliability-under-state analysis. All four are domain parameters, not formal properties.

Candidate domains: emergency triage (E = {vital signs, resource availability, time-criticality}; advisory types = {Diagnose, Treat, Refer, Escalate}), maritime route planning (E = {weather, traffic density, vessel status}; advisory types = {Route, Speed, Waypoint, Abort}), agricultural decision support (E = {soil moisture, temperature, precipitation forecast, pest indicators}; advisory types = {Irrigate, Spray, Harvest, Wait}). In each domain, the graduated type restriction logic applies: under higher-severity states, types requiring precise future prediction are suppressed while types requiring only present-state assessment are retained.

*Viva one-liner: The formal structure is domain-generic — fisheries is the validation domain, not the scope of the architecture.*

---

### TC-5. What happens if we remove CAUTION — what remains?

**Direct answer: Removing CAUTION collapses the architecture to binary governance — the universal status quo documented across 148+ papers — eliminating the graduated property, reducing the architecture to a participation gate, and losing the VOI-calibrated type restriction that is the primary safety mechanism.**

Without CAUTION: S ∈ {SAFE, UNSAFE}, A_AI(SAFE) = {Go, Delay, DepartureTime, Duration}, A_AI(UNSAFE) = ∅, G(SAFE)=1, G(UNSAFE)=0. This is exactly the binary governance architecture that Ramos et al. (2024) [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md), Newcomb & Ochoa (2026) [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md), and Bengio et al. (2026) [[notes]](../notes/International%20AI%20Safety%20Report%202026.md) find universally in the literature. The Architecture with CAUTION removed makes no contribution to the field.

Additionally, removing CAUTION fails the domain: Rahim et al. (2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) and Yamin et al. (2025) [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md) document that intermediate conditions are the dominant operational reality for Malaysian coastal fishers — binary governance either over-restricts (classifying borderline conditions as UNSAFE) or under-governs (classifying them as SAFE). CAUTION is the state that makes the architecture fit the operational reality of the deployment domain.

*Viva one-liner: Remove CAUTION and you have binary governance — the universal status quo across 148+ reviewed papers, making no contribution.*

---

### TC-6. What is the core irreducible idea of your model?

**Direct answer: The core irreducible idea is that the reliability of a recommendation type depends on the environmental state, and therefore the admissible output type space should be indexed to the classified environmental state — not fixed, not filtered post-hoc, but defined pre-hoc as a function of f(E).**

Every other element of the architecture — the specific variables in E, the three-state classification, the specific types in A_AI, the max-severity aggregation — is a domain-specific or engineering-level instantiation of this core idea. The formal expression of the core idea is: A_AI: {SAFE, CAUTION, UNSAFE} → 2^R with A_AI(S₁) ⊆ A_AI(S₂) when S₁ is more severe than S₂. This says: as environmental conditions worsen, the permissible output type space contracts — because worse conditions reduce the reliability of more demanding recommendation types.

The idea is grounded in VOI theory (Atf & Lewis (2026) [[notes]](../notes/Is%20Trust%20Correlated%20With%20Explainability%20in%20AI%3F%20A%20Meta-Analysis.md)), empirically motivated by fishers' decision behaviour (Gao (2024) [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md)), formally validated by Safety Dominance, and distinguished from all existing governance paradigms by operating at the type level rather than the action, authority, or content level.

*Viva one-liner: The core idea is that type reliability depends on environmental state, so the admissible type space should contract as conditions worsen — everything else is instantiation.*

---

### TC-7. Why is this work PhD-level, not just system design?

**Direct answer: The work satisfies PhD-level criteria on four independent dimensions: it identifies and documents a gap across 148+ papers in four systematic reviews; it defines a new formal property (Safety Dominance for graduated governance) with tractable verification; it provides multi-source theoretical grounding (ALARP, VOI, bounded rationality, trust calibration theory); and it makes a contribution that advances the field's understanding of AI governance beyond the binary paradigm.**

System design produces an artefact that solves a problem. PhD-level research produces an artefact grounded in a formally identified gap, justified by rigorous theoretical argument, with provable formal properties and a contribution that extends the field's conceptual vocabulary. Each criterion is satisfied:

Gap identification: Four independent systematic reviews (Ramos 91 papers, Newcomb 46, Bengio 11 frameworks, Perez-Cerrolaza cross-domain) confirm that graduated type-level governance does not exist in the literature. This is not a gap identified by assertion — it is documented across 148+ independent papers.

New formal property: Safety Dominance AI(E) ⊆ A_AI(S) for graduated governance is a new property. The literature addresses safety as binary action-level constraints; this work formalises a graduated type-level analogue with a distinct verification structure.

Theoretical grounding: ALARP (Perez-Cerrolaza et al. (2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md)), VOI (Atf & Lewis (2026) [[notes]](../notes/Is%20Trust%20Correlated%20With%20Explainability%20in%20AI%3F%20A%20Meta-Analysis.md)), bounded rationality and mode effects (Wen et al. (2025) [[notes]](../notes/Risk%20Perception%20in%20Complex%20Systems-%20A%20Comparative%20Analysis%20of%20Process%20Control%20and%20Autonomous%20Vehicle%20Failures.md)), trust calibration (McGrath et al. (CHAI-T) [[notes]](../notes/Collaborative%20Human-AI%20Trust%20(CHAI-T)-%20A%20Process%20Framework%20for%20Active%20Management%20of%20Trust%20in%20Human-AI-Collaboration.md)) — four independent theoretical bodies provide converging justification.

Field contribution: The work extends the governance vocabulary from binary (safe/unsafe) to graduated (state-indexed type space), providing a reusable formal framework applicable beyond the specific domain.

*Viva one-liner: The contribution is not a deployed system — it is a formal architecture with a documented gap, a new formal property, multi-body theoretical grounding, and a governance vocabulary that extends the field beyond binary.*

---

## ⚫ Hardest Question

### Why is restricting AI advisory scope fundamentally different from safety filters, guardrails, adaptive autonomy, and rule-based constraints?

**Direct answer: Each existing paradigm governs at a different level — action, output content, authority, or content matching — none governs at the type level (which categories of recommendation are pre-hoc admissible as a function of classified environmental state), and the type level is the only governance level that can suppress false-precision hazards before they are generated while retaining positive-VOI types in every state where they are reliable.**

The distinction requires precise characterisation of each paradigm's governance level:

**Safety filters** (Bajcsy & Fisac (2024) [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md), Könighofer et al. (2025) [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md), Corsi et al. (2024) [[notes]](../notes/Verification-Guided%20Shielding%20for%20Deep%20Reinforcement%20Learning.md), Odriozola-Olalde et al. (2023) [[notes]](../notes/Shielded%20Reinforcement%20Learning-%20A%20review%20of%20reactive%20methods%20for%20safe%20learning.md)) govern at the **action level**: for each candidate action the AI proposes, a binary decision is made — is this specific action safe or unsafe? The filter does not distinguish between action types; it evaluates individual action instances. Binary, per-action, post-hoc.

**Guardrails** (Shamsujjoha et al. (2025) [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md), Wang et al. (2026) [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md)) govern at the **output content level**: generated outputs are evaluated against rules (does this output contain prohibited content? does this action violate a specified policy?). The evaluation is post-hoc (the output exists before being checked), static (rules do not change based on environmental state), and content-matching (the rule checks what the output says, not what category of claim it makes). Shamsujjoha identifies 13 guardrail action types — all post-hoc, none state-conditioned.

**Adaptive autonomy** frameworks govern at the **authority level**: as conditions change, the allocation of decision authority between human and AI shifts. The AI may be given less authority to act on its outputs, but the outputs themselves are not type-restricted. As documented by Wen et al. (2025) [[notes]](../notes/Risk%20Perception%20in%20Complex%20Systems-%20A%20Comparative%20Analysis%20of%20Process%20Control%20and%20Autonomous%20Vehicle%20Failures.md), even nominal human control does not prevent anchoring from AI outputs — the DepartureTime recommendation is still seen and anchors judgment even if the human is nominally deciding.

**Rule-based constraints** govern at the **content-matching level**: outputs are checked against rule databases (does the output contain prohibited terms, violate predefined logical constraints, exceed defined value ranges?). Content-matching can catch specific prohibited values but cannot reason about whether the category of claim (a temporal prediction vs. a binary present-state assessment) is appropriate given the current environmental uncertainty.

**Advisory scope restriction** governs at the **type level**: which categories of recommendation may the AI produce? This operates before generation (pre-hoc), varies with classified environmental state (state-conditioned), is grounded in the reliability profile of recommendation types under different uncertainty levels (reliability-grounded), and is formally guaranteed by construction (Safety Dominance AI(E) ⊆ A_AI(S)).

The type level is fundamentally different for five reasons:

**(1) Pre-hoc vs. post-hoc**: Type restriction defines the output space before generation — the AI cannot reason toward an inadmissible output because it does not exist as a possibility. Filters, guardrails, and content rules operate after generation. This is not merely a timing difference: pre-hoc restriction provides the formal guarantee by construction (AI(E) ⊆ A_AI(S) because A_AI(S) bounds what AI(E) can be), while post-hoc methods provide it contingently (only if the filter correctly classifies every generated output).

**(2) State-conditioned vs. static**: A_AI(S) changes as S changes — the permitted type space is different in SAFE, CAUTION, and UNSAFE. Safety filters have static safety specifications; guardrail rules are static; autonomy allocation changes but does not alter the AI's output type space. The state-conditioning is what makes the architecture graduated rather than binary — it is the mechanism by which CAUTION provides a distinct governance response rather than collapsing to one extreme or the other.

**(3) Reliability-grounded**: The type taxonomy is constructed based on which recommendation types have positive VOI under each safety state. DepartureTime requires precise temporal prediction — positive VOI under SAFE (stable environment), negative VOI under CAUTION (uncertain environment). Go/Delay require only present-state assessment — positive VOI under both SAFE and CAUTION. No other paradigm reasons about recommendation reliability by type — safety filters reason about action safety by instance, guardrails reason about output content by rule, autonomy frameworks reason about authority allocation by condition.

**(4) Hazard suppression at source**: False-precision temporal recommendations under CAUTION constitute a hazard before any specific value is generated — the hazard is the act of making a DepartureTime claim, not any particular claimed time. Type restriction suppresses this hazard at source by making the claim type inadmissible. Post-hoc filters can only suppress specific generated values; they cannot suppress the hazard of making the claim type in the first place, since the filter operates after the claim is generated.

**(5) VOI-preserving**: Every admitted type retains positive VOI under the safety state where it is admitted. Binary blocking (Perez-Cerrolaza et al. (2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) identifies this problem) suppresses all AI output including positive-VOI types. Type restriction suppresses only negative-VOI types, retaining maximum useful advisory content at every safety state.

The convergence of these five properties — pre-hoc, state-conditioned, reliability-grounded, source-suppressing, VOI-preserving — at the type level is what makes advisory scope restriction a distinct governance paradigm, not a variation of any existing one. Four independent systematic reviews confirm that this combination does not exist in the literature across 148+ papers.

*Viva one-liner: Every other governance paradigm operates at a different level — action safety, output content, authority allocation, or content matching — and none of those levels can suppress a false-precision hazard before it is generated while retaining the advisory types that remain reliable, which is what type-level pre-hoc environment-conditioned restriction uniquely achieves.*
