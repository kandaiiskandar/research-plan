# The Formal Model: Definitions, Properties, Assumptions, and Limitations

**Document type**: Theoretical justification / argumentation note  
**For**: Chapter 3 (Architecture Design), Appendix C (Mathematical Formalisation), and viva preparation  
**Questions addressed**: Formal definitions of S, G(S), A_AI(S), Safety Dominance Property, containment property. Deterministic vs. probabilistic. Formal verification. State machine characterisation. Assumptions. Limitations. Many-to-one mapping. Advisory space cardinality.

**Cross-references**: For why three states, see `justification-three-states.md`. For why environmental state as trigger, see `justification-environmental-state-governance.md`. For why unified governance, see `justification-unified-governance.md`. For domain generality, see `justification-caution-mode-operation.md` §7 and `justification-unified-governance.md` §9.

---

## 1. Formal Definitions

### 1.1 Environmental State Vector E

**Definition.** E = {w, r, m, o, v, t} is a vector of observable environmental parameters, where:
- w ∈ ℝ≥0 — wind speed (knots, sustained)
- r ∈ {none, light, moderate, heavy, storm} — rainfall intensity (ordinal categorical)
- m ∈ ℝ≥0 × ℝ≥0 — sea state (wave height in metres, swell period in seconds)
- o ∈ {none, advisory, warning, alert} — official marine warning level (ordinal categorical)
- v ∈ {small, medium, big} — vessel category (ordinal categorical)
- t ∈ [0, 24) — time of day (hour, 24-hour clock)

E is a mixed-type vector: some components are continuous (w, m, t), others are ordinal categorical (r, o, v). The domain of E is the Cartesian product of all component domains: E ∈ D_w × D_r × D_m × D_o × D_v × D_t.

**Why these six parameters.** The selection is empirically grounded: Yamin et al. (2025) [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md) document that the target population identifies wind/waves (95%), weather events (91%), and erratic rainfall (91%) as primary hazards — mapping onto w, o, and r. Gao (2024) [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md) documents factor importance ratings: tide (4.55/5, captured in o), weather (3.75/5, captured across w, r, m), safety concern (3.40/5, aggregated across all parameters). Rahim et al. (2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) independently confirm wind velocity, wave height, precipitation, and vessel size as primary fisher decision inputs. The E vector formalises the environmental inputs that domain practitioners already use.

**Why t (time of day) is included.** Time of day requires specific justification as a contextual amplifier rather than a direct physical hazard. Atacan & Düzbastılar (2023) [[notes]](../notes/Determination%20of%20risk%20perception%20in%20small-scale%20fishing%20and%20navigation.md) provide direct empirical evidence from a bridge navigation simulator study with 30 small-scale fishing vessel captains: night navigation produces significantly higher accident probability ratings than daytime conditions (mean 4.08 vs. 3.43 for calm conditions), and combined night with heavy weather yields the highest consequence scores across all tested environmental conditions (mean 37.03 — the maximum in the study). Critically, restricted visibility — the primary mechanism through which t elevates risk for small vessels without electronic navigation aids — is rated the single most dangerous factor for sea navigation accident probability (mean 7.90, highest across all six tested conditions). Dominguez-Péry et al. (2023) [[notes]](../notes/A%20holistic%20view%20of%20maritime%20navigation%20accidents%20and%20risk%20indicators-%20examining%20IMO%20reports%20from%202011%20to%202021.md), analysing 504 IMO maritime accident investigation reports across 2011–2021, confirm that external environmental factors including visibility constitute the largest single risk cluster in maritime accident reporting (26.7% of all text segments), with time of day embedded as a standard contextual field in the IMO reporting structure. Together, these two papers establish that time of day is a documented, empirically validated maritime safety factor. g_t(t) classifies t ∈ [0, 24) into three safety zones: SAFE (06:00–17:00), CAUTION (17:00–19:00, approaching darkness), and UNSAFE (19:00–06:00, night).

### 1.2 Safety State Classification S = f(E)

**Definition.** S = f(E) is a deterministic classification function:

```
f: D_E → {SAFE, CAUTION, UNSAFE}
```

where D_E is the domain of E. The function is implemented as a threshold-based classifier with worst-case aggregation:

1. Each component of E is independently classified: S_w = g_w(w), S_r = g_r(r), ..., S_t = g_t(t), where each g_i maps the component to {SAFE, CAUTION, UNSAFE} via domain-specific thresholds.

2. The overall state is the maximum severity across all components:

```
S = max-severity(S_w, S_r, S_m, S_o, S_v, S_t)
```

where the severity ordering is SAFE < CAUTION < UNSAFE.

**Properties of f:**
- **Deterministic**: The same E always produces the same S. No randomness, no learned parameters, no AI inference.
- **Total**: f is defined for every E in D_E. No environmental condition is unclassified.
- **Monotone in severity**: If any component worsens (moves to a higher severity level), S can only stay the same or increase in severity — it cannot decrease.
- **Conservative**: The worst-case aggregation ensures that a single dangerous parameter is sufficient to escalate governance, regardless of all other parameters being safe.

### 1.3 Participation Gate G(S)

**Definition.** G is a function from safety states to binary participation decisions:

```
G: {SAFE, CAUTION, UNSAFE} → {0, 1}
```

defined as:

```
G(SAFE) = 1      (AI participates)
G(CAUTION) = 1   (AI participates)
G(UNSAFE) = 0    (AI does not participate)
```

G(S) is a binary gate. Its role is to determine whether the AI reasoning layer is active at all. When G(S) = 0, no AI recommendations are generated; the human decides without AI assistance.

**Why G(CAUTION) = 1.** The participation gate permits AI under CAUTION because go/no-go and delay guidance remain reliable under elevated conditions. Blocking AI entirely at CAUTION (G(CAUTION) = 0) would reduce the architecture to binary governance — the status quo that Ramos et al. (2024) [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md) document across 91 papers. The novel intermediate mode requires G(CAUTION) = 1 combined with scope restriction via A_AI(CAUTION) ⊂ A_AI(SAFE). See `justification-advisory-scope-restriction.md` for the full argument.

### 1.4 Admissible Advisory Space A_AI(S)

**Definition.** A_AI is a set-valued function mapping each safety state to a subset of the recommendation type space R:

```
A_AI: {SAFE, CAUTION, UNSAFE} → P(R)
```

where R = {Go, Delay, DepartureTime, Duration} is the set of recommendation types and P(R) is the power set of R.

The function is defined as:

```
A_AI(SAFE) = {Go, Delay, DepartureTime, Duration} = R
A_AI(CAUTION) = {Go, Delay}
A_AI(UNSAFE) = ∅
```

A_AI(S) defines the *types* of recommendations the AI is permitted to generate under safety state S. It does not constrain the *content* of individual recommendations within a permitted type — it constrains which *categories* of recommendation are in scope.

### 1.5 The Containment Property

**Statement.** A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅

**Meaning.** As environmental conditions worsen (S transitions from SAFE to CAUTION to UNSAFE), the set of permitted recommendation types strictly contracts. Every recommendation type permitted at a more severe state is also permitted at every less severe state. No recommendation type is "unlocked" by worsening conditions.

**Why it is needed.** The containment property is the formal expression of graduated governance. Without it, the governance pair could exhibit non-monotone behaviour — permitting recommendation types under CAUTION that are not permitted under SAFE, or permitting some types under UNSAFE that are blocked under CAUTION. Such non-monotonicity would be operationally incoherent (why would worsening conditions expand the AI's advisory scope?) and would violate the safety engineering principle that risk controls should increase monotonically with assessed risk.

The containment hierarchy also enables the Safety Dominance Property proof by case analysis: if the property holds for A_AI(SAFE) (the largest set), it holds a fortiori for A_AI(CAUTION) ⊂ A_AI(SAFE) and for A_AI(UNSAFE) = ∅.

Baxi (2026) [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) independently derives the same formal structure: E(T_k) ⊂ E(T_{k+1}) — economic permission sets are nested by tier, with lower tiers (less trusted agents) having strictly smaller permission sets. Baxi proves (Theorem 6) that this containment produces monotonic safety scaling. The structural parallel confirms that containment is not an arbitrary constraint but a necessary property for graduated governance with formal guarantees.

### 1.6 The Safety Dominance Property

**Statement.** For all E ∈ D_E:

```
AI(E) ⊆ A_AI(S)   where S = f(E)
```

**Meaning.** Every recommendation the AI actually generates under environmental conditions E is a member of the admissible advisory space for the safety state classified from those conditions. The AI never produces a recommendation type that is outside the scope permitted by the current governance mode.

**Why it matters.** This is the architecture's central safety guarantee. It formalises the claim that governance *actually constrains* the AI — that the AI cannot circumvent the scope restriction. Without this property, the governance layer would be advisory rather than enforced; the AI could generate departure time recommendations under CAUTION conditions despite the governance layer classifying A_AI(CAUTION) = {Go, Delay}.

**Proof structure.** The property is proved by construction:
1. The governance layer defines A_AI(S) before the AI reasoning layer is invoked
2. The AI reasoning layer generates recommendations only from the recommendation types in A_AI(S)
3. The AI output is verified against A_AI(S) before delivery to the user

Step 2 provides the primary guarantee (pre-hoc scope definition). Step 3 provides a backup guarantee (post-hoc verification). Together, they ensure the property holds by architectural design, not by statistical observation.

**Precedent for this proof pattern.** Könighofer et al. (2025) [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md) prove an analogous property for shields: the shield ensures that the agent's selected action is always within the safe action set computed from the formal specification. Bajcsy & Fisac (2024) [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md) prove Theorem 1: the safety filter ensures the system never enters the failure set. Dalrymple et al. (2024) [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md) define the verifier's proof certificate as a guarantee that the AI policy satisfies the safety specification. All three prove safety properties by architectural separation — the safety mechanism is independent of the AI system it governs. The proposed architecture uses the same proof pattern, extended from binary to graduated governance.

---

## 2. Is the Model Deterministic or Probabilistic?

### 2.1 The Governance Layer Is Deterministic

Every component of the governance layer is deterministic:
- f(E) is a threshold-based classifier with fixed thresholds — no learned parameters, no stochastic elements
- G(S) is a simple lookup: three states, three predetermined values
- A_AI(S) is a simple lookup: three states, three predetermined recommendation type sets
- The containment property is a static structural constraint
- The Safety Dominance Property is enforced by architectural design

### 2.2 The AI Reasoning Layer May Be Probabilistic

The AI reasoning layer (Layer 3) — which generates actual recommendations within A_AI(S) — may use any computational method, including probabilistic ones (neural networks, Bayesian inference, ensemble methods). The architecture is agnostic to the AI method.

### 2.3 The Architectural Significance

The determinism of the governance layer is not incidental — it is a formal requirement. Bloomfield & Rushby (2025) [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md) define assuredly guarded systems as those whose guards "do not themselves use AI/ML and can therefore be assured conventionally." The deterministic governance layer satisfies this requirement: it can be verified by exhaustive testing of the finite classification function (three outputs from a bounded input space), standard software testing, and formal proof — conventional assurance methods that do not require the probabilistic assurance techniques needed for the AI layer.

This asymmetry — deterministic governance constraining probabilistic AI — is the formal basis for the safety guarantee. If the governance layer were itself probabilistic, the Safety Dominance Property would hold only with some probability, not as a formal invariant.

---

## 3. Can the Model Be Formally Verified?

### 3.1 The Governance Layer: Yes

The governance layer is amenable to formal verification because:
- f(E) has a finite output domain ({SAFE, CAUTION, UNSAFE}) and each component classifier g_i has a finite number of threshold comparisons
- G(S) and A_AI(S) are finite lookup functions (three inputs, three outputs)
- The containment property is a static set inclusion that can be checked by inspection
- The Safety Dominance Property reduces to verifying that the AI output interface enforces A_AI(S) — a standard software correctness property

These are all properties verifiable by conventional formal methods: model checking, theorem proving, or exhaustive testing. No probabilistic or statistical verification is needed.

### 3.2 The AI Reasoning Layer: Partially

The AI reasoning layer's correctness (does it generate good recommendations?) cannot be formally verified in the same sense — this is the fundamental challenge of AI safety that the entire field grapples with. Newcomb & Ochoa (2026) [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md), reviewing 46 formal methods studies for safety-critical ML, confirm that all formal verification approaches for AI operate with binary safety boundaries (safe/unsafe) and face scalability challenges for real-world neural networks.

However, the **Safety Dominance Property can be verified regardless of AI behaviour**, because it is enforced by the governance layer, not by the AI itself. Even if the AI model is incorrect, adversarial, or degraded, the governance layer ensures AI(E) ⊆ A_AI(S) by restricting the output space before (and verifying after) recommendation generation.

### 3.3 The Verification Asymmetry

This is the key insight: the architecture achieves formally verifiable safety guarantees *without* requiring the AI component to be formally verified. The governance layer is verified; the AI layer is constrained by the verified governance layer. This mirrors the approach documented across the safety-critical AI literature:
- Dalrymple et al. (2024) [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md): the verifier is verified; the AI policy is constrained by the verifier
- Könighofer et al. (2025) [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md): the shield is computed from a formal specification; the RL agent is constrained by the shield
- Abella et al. (2025 — SAFEXPLAIN) [[notes]](../notes/SAFEXPLAIN-%20a%20Complete%20Approach%20Towards%20Trustworthy%20AI-Based%20Safety-Critical%20Systems.md): the supervision function is verified; the AI component is bounded by the supervision function
- Flehmig et al. (2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md): the non-AI monitoring and supervisory components are verified; the AI component is monitored by them

---

## 4. Is the Architecture a State Machine?

### 4.1 Yes, at the Governance Layer

The governance layer can be characterised as a finite state machine with:
- **States**: {SAFE, CAUTION, UNSAFE}
- **Input alphabet**: D_E (the domain of environmental parameter vectors)
- **Transition function**: δ(S_current, E_new) = f(E_new) — the next state depends only on the new environmental observation, not on the current state (with the exception of hysteresis, below)
- **Output function**: λ(S) = (G(S), A_AI(S)) — each state produces a governance configuration

### 4.2 Memoryless Transitions (With Hysteresis Exception)

In the base formulation, the state machine is memoryless — the next state depends only on current environmental observations, not on the previous state. This is a Mealy machine where the transition depends only on input: δ(E) = f(E).

Hysteresis (see `justification-safety-state-design.md` §2.5) introduces limited memory: a transition from CAUTION back to SAFE requires conditions to exceed the SAFE threshold by a margin. This makes the transition function depend on the current state as well as the input:

```
δ(CAUTION, E) = SAFE    only if E satisfies SAFE thresholds + hysteresis margin
δ(CAUTION, E) = CAUTION  if E satisfies SAFE thresholds but not hysteresis margin
δ(S, E) = f(E)           for all other transitions
```

This is standard in safety-critical systems: hysteresis prevents oscillation at state boundaries. The state machine remains finite, deterministic, and formally verifiable.

### 4.3 What the State Machine Does Not Include

The AI reasoning layer is **not** part of the state machine. The state machine determines governance mode; the AI operates within the governance mode's constraints. The state machine has three states; the AI's internal computation may have arbitrarily many states. This separation is deliberate — the governance state machine is simple enough for formal verification; the AI's internal complexity is irrelevant to the governance guarantee.

---

## 5. What Assumptions Does the Formal Model Make?

### 5.1 Enumerated Assumptions

**A1 — Observable environment.** Environmental parameters in E are measurable by sensors available in the deployment context. This assumes the existence of wind measurement (anemometer or weather API), ocean state assessment (wave buoy, visual observation, or satellite data), and the other four parameters. In low-resource settings, some parameters may be assessed qualitatively rather than by instrument; vessel category (v) is a known vessel attribute that does not require runtime measurement.

**A2 — Correct sensor data.** f(E) produces a correct classification only if the input E accurately represents the actual environmental conditions. Sensor faults, calibration errors, or communication failures can cause misclassification. See `justification-safety-state-design.md` §3 for analysis of misclassification consequences.

**A3 — Valid thresholds.** The thresholds within f(E) are assumed to be correctly calibrated for the deployment context — that is, the SAFE–CAUTION boundary corresponds to the actual point where detailed recommendation reliability degrades, and the CAUTION–UNSAFE boundary corresponds to the actual point where even directional guidance becomes unreliable. Threshold calibration requires domain expert knowledge and empirical validation; incorrect thresholds degrade governance quality but do not violate the formal properties (the containment hierarchy and Safety Dominance Property hold for any threshold values).

**A4 — Complete recommendation type set.** R = {Go, Delay, DepartureTime, Duration} is assumed to be a complete enumeration of the AI's recommendation types for the fisheries domain. If the AI generates recommendation types not in R (e.g., species selection, gear choice), those types are outside the governance architecture's scope and would need to be added to R with appropriate state-conditioned scope assignments.

**A5 — Reliability differentiation.** Different recommendation types have different reliability profiles under CAUTION conditions — specifically, that Go and Delay are more robust to environmental uncertainty than DepartureTime and Duration. This assumption is justified by the structural argument in `justification-caution-mode-operation.md` §1.2: threshold-crossing assessments (go/no-go) depend on ordinal comparison, while temporal recommendations depend on cardinal precision.

**A6 — Governance enforcement.** The implementation correctly enforces A_AI(S) — the AI output interface actually prevents recommendation types outside A_AI(S) from reaching the user. This is a software correctness assumption verifiable by standard testing and formal methods.

**A7 — Human decision authority.** The human retains final decision authority in all states. The architecture provides recommendations; the human decides whether to follow them. This assumption means the architecture's safety guarantee is conditional on the human not being compelled to follow AI recommendations.

### 5.2 What the Model Does NOT Assume

- **AI model correctness**: The model does not assume the AI generates correct or optimal recommendations — only that the *types* of recommendations are within A_AI(S). The AI can be wrong within the permitted scope.
- **Specific AI method**: No assumption about whether the AI uses neural networks, Bayesian methods, expert systems, or any other technique.
- **Specific sensor hardware**: No assumption about sensor technology — parameters can be measured by instruments, estimated from weather APIs, or assessed qualitatively.
- **Specific threshold values**: The formal properties hold for any valid threshold assignment.
- **User behaviour**: No assumption about whether users follow AI recommendations, calibrate trust correctly, or use the system as intended. The Safety Dominance Property guarantees what the AI *outputs*; it does not guarantee what the human *does*.

---

## 6. What Are the Limitations of the Formal Model?

### 6.1 Scope Governance, Not Content Governance

The model governs which *types* of recommendations the AI may produce. It does not govern the *quality* of recommendations within a permitted type. An AI that is permitted to generate Go recommendations under CAUTION may generate a wrong Go recommendation — the governance layer does not prevent this. Content correctness is outside the formal model's scope; it is addressed by the AI reasoning layer's own quality mechanisms.

This is a deliberate design boundary, not an oversight. Dalrymple et al. (2024) [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md) draw the same boundary: the Guaranteed Safe AI verifier certifies that the AI satisfies the safety specification, not that the AI produces optimal outputs. Könighofer et al. (2025) [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md) draw it similarly: the shield ensures actions are safe, not that they are performance-optimal.

### 6.2 No Formal Model of Human Behaviour

The model formalises the AI system's governance; it does not formalise human decision-making. The human's response to restricted advisory scope (do they trust it? do they compensate correctly? do they understand the mode?) is an empirical question addressed by the socio-technical evaluation (PS5, O5), not by the formal model.

Bajcsy & Fisac (2024) [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md) note the same limitation: their safety filter models human behaviour through a "set of allowable human behaviors H" but acknowledges that the actual human response is empirical. The proposed model makes no formal assumptions about human behaviour.

### 6.3 Threshold Sensitivity

The governance quality depends on threshold calibration. Poorly calibrated thresholds produce excessive false CAUTION (reducing decision support value) or missed CAUTION (providing unreliable detailed recommendations). The formal model guarantees that governance is *correctly enforced* for the classified state; it does not guarantee that the classification is *appropriate* for the actual conditions.

### 6.4 Fixed Recommendation Type Set

R is defined as a fixed set at design time. If new recommendation types emerge (e.g., crew safety alerts, equipment recommendations), they must be explicitly added to R and assigned to appropriate state-conditioned scope levels. The model does not dynamically discover or incorporate new recommendation types.

### 6.5 No Temporal Properties

The current model formalises state-conditioned governance at a point in time. It does not formally model temporal properties: how quickly the system should transition between states, how long the system may remain in a state, or what happens during a transition. Hysteresis is specified as a transition modifier (§4.2) but is not formalised with temporal logic. LTL or CTL specifications for temporal governance properties are a potential extension.

### 6.6 Single Environmental Assessment

The model assumes a single, system-wide environmental assessment. It does not formalise scenarios where different spatial locations have different environmental conditions simultaneously — for example, conditions at the harbour differing from conditions at the fishing ground. The classification applies to a single assessment point, typically the vessel's current location or the intended fishing area.

---

## 7. Can Two Different Environmental States Produce the Same Safety State?

### 7.1 Yes — the Mapping Is Many-to-One

The classification function f: D_E → {SAFE, CAUTION, UNSAFE} is surjective and many-to-one. The domain D_E is a large (potentially uncountable) set of environmental parameter vectors; the codomain has only three elements. Many distinct environmental conditions map to the same safety state.

**Examples within CAUTION:**
- E₁ = {w=20 knots, r=none, m=1.5m, o=none, v=big, t=10hrs} → CAUTION (triggered by wind)
- E₂ = {w=10 knots, r=heavy, m=0.5m, o=none, v=big, t=10hrs} → CAUTION (triggered by rainfall)
- E₃ = {w=10 knots, r=none, m=0.8m, o=advisory, v=medium, t=6hrs} → CAUTION (triggered by marine warning + vessel category + time)

All three produce S = CAUTION and therefore the same governance configuration: G(S) = 1, A_AI(S) = {Go, Delay}. But the underlying conditions are different, and the AI's go/no-go and delay recommendations may differ accordingly — the governance scope is the same, but the recommendation *content* within that scope reflects the specific E.

### 7.2 Why Many-to-One Is Correct

The many-to-one mapping is a feature, not a limitation. The governance layer's purpose is to classify *governance mode* — what the AI is permitted to do — not to provide a lossless representation of environmental conditions. The full E vector is passed to the AI reasoning layer (Layer 3), which uses all parameters to generate recommendations within the governance scope. Information is not lost; it is used at different layers for different purposes:

- **Governance layer**: Uses E to determine S (three modes) — coarse classification for governance decisions
- **AI reasoning layer**: Uses full E to generate specific recommendations within A_AI(S) — fine-grained analysis for operational decisions

This separation mirrors the distinction in the shielding literature: Könighofer et al. (2025) [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md) compute shields from an *abstract* environment model (coarse, for safety) while the RL agent operates on the *full* state representation (fine-grained, for performance). The abstraction level differs by purpose.

---

## 8. Can the Advisory Action Space Be Infinite?

### 8.1 R Is Finite; Recommendation Content May Be Continuous

The recommendation *type* space R = {Go, Delay, DepartureTime, Duration} is finite (|R| = 4). The governance layer operates on types, not on specific recommendation values. A_AI(S) is always a finite subset of R.

Within each recommendation type, the actual recommendation value may be drawn from a continuous space:
- Go ∈ {yes, no} — binary
- Delay ∈ {immediate, wait_hours, wait_tomorrow, ...} — small discrete set
- DepartureTime ∈ ℝ (specific time of day) — continuous
- Duration ∈ ℝ≥0 (hours) — continuous

The governance model's formal properties operate on the finite type space R, not on the continuous value spaces. This is what makes the containment property and Safety Dominance Property tractable: they are statements about finite sets of recommendation types, not about infinite value spaces.

### 8.2 Why Type-Level Governance Suffices

Governing at the type level rather than the value level is both sufficient and practical:

**Sufficient**: The reliability differentiation under CAUTION is between recommendation *types* — go/no-go guidance as a category is robust while departure time estimation as a category degrades. The degradation is structural (threshold-crossing vs. precise estimation), not value-dependent (departure at 06:15 is not inherently less reliable than departure at 07:30 under the same conditions).

**Practical**: Value-level governance (permitting departure times within a "safe" range while blocking "unsafe" departure times) would require the governance layer to evaluate specific recommendation content — making it dependent on the AI model's predictions, violating the independence requirement that Bloomfield & Rushby (2025) [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md) identify as essential for assuredly guarded systems.

### 8.3 Extensibility

R can be extended for different domains or richer fisheries decision support (e.g., R' = {Go, Delay, DepartureTime, Duration, FishingArea, SpeciesTarget, GearSelection}). The formal properties hold for any finite R with a valid containment assignment. The constraint is that R must be finite — type-level governance over an infinite type space would not be operationally meaningful or formally tractable.

---

## 9. Comparative Summary Table

| Question | Answer | Formal basis |
|---|---|---|
| **What is S?** | S ∈ {SAFE, CAUTION, UNSAFE}, classified by f(E) — deterministic, total, monotone, conservative | Threshold-based classifier with worst-case aggregation |
| **What is G(S)?** | Binary participation gate: G(SAFE) = G(CAUTION) = 1, G(UNSAFE) = 0 | Permits AI under CAUTION (novelty); blocks under UNSAFE (safety) |
| **What is A_AI(S)?** | Set-valued function: A_AI(S) → P(R), defining permitted recommendation types per state | A_AI(SAFE) = R, A_AI(CAUTION) = {Go, Delay}, A_AI(UNSAFE) = ∅ |
| **Safety Dominance?** | AI(E) ⊆ A_AI(S) for all E — AI output is always within governance-permitted scope | Proved by construction: pre-hoc scope definition + post-hoc verification |
| **Why containment?** | A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ ∅ — graduated governance must be monotonically non-increasing in scope | Prevents non-monotone behaviour; enables proof by case analysis; independently derived by Baxi (2026) [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) |
| **Deterministic or probabilistic?** | Governance layer: deterministic. AI layer: may be probabilistic. | Determinism is a formal requirement for verifiable safety guarantees (Bloomfield & Rushby, 2025 [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md)) |
| **Formally verifiable?** | Governance layer: fully. AI layer: constrained by verified governance. | Verification asymmetry — safety guaranteed without verifying AI (Dalrymple et al., 2024 [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md); Könighofer et al., 2025 [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md)) |
| **State machine?** | Yes — three states, deterministic transitions from E, with hysteresis | Memoryless (Mealy-type) except for hysteresis at boundaries |
| **Key assumptions?** | Observable environment, correct sensors, valid thresholds, complete R, reliability differentiation, governance enforcement, human authority | Does NOT assume AI correctness, specific AI method, or user behaviour |
| **Key limitations?** | Scope not content governance, no human behaviour model, threshold sensitivity, fixed R, no temporal properties, single spatial assessment | Deliberately bounded scope — governance quality, not AI quality or human response |
| **Many-to-one mapping?** | Yes — many E produce the same S; governance mode is coarse, AI uses full E for recommendations | Feature: governance operates on abstracted state, AI operates on full environmental detail |
| **Infinite action space?** | R is finite (types); recommendation values within types may be continuous | Type-level governance is sufficient and preserves independence from AI model |
| **Domain-independent?** | Formal structure is domain-general; R, E, thresholds are domain-specific | See `justification-unified-governance.md` §9 |

---

## 10. One-Paragraph Summary (for use in Appendix C or Chapter 3)

> The formal model defines a governance pipeline E → S = f(E) → (G(S), A_AI(S)) → AI(E) where E = {w, r, m, o, v, t} is an empirically grounded environmental parameter vector (Yamin et al., 2025 [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md); Gao, 2024 [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md); Rahim et al., 2024 [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md)), S = f(E) is a deterministic, total, monotone, conservative classification function producing S ∈ {SAFE, CAUTION, UNSAFE} via threshold-based worst-case aggregation, G(S) is a binary participation gate permitting AI under both SAFE and CAUTION while blocking at UNSAFE, and A_AI(S) is a set-valued function defining the admissible recommendation types per state with A_AI(SAFE) = R ⊃ A_AI(CAUTION) = {Go, Delay} ⊃ A_AI(UNSAFE) = ∅. The containment property ensures governance scope contracts monotonically as conditions worsen — a structure independently derived by Baxi (2026) [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) for graduated economic governance and consistent with the monotonic safety scaling principle. The Safety Dominance Property AI(E) ⊆ A_AI(S) guarantees that all AI output falls within the governance-permitted scope, proved by construction through pre-hoc scope definition and post-hoc verification — following the same architectural proof pattern used for shields (Könighofer et al., 2025 [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md)), safety filters (Bajcsy & Fisac, 2024 [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md)), and GS AI verifiers (Dalrymple et al., 2024 [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md)). The governance layer is fully deterministic and formally verifiable by conventional methods, satisfying Bloomfield & Rushby's (2025) [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md) criterion for assuredly guarded systems; the AI reasoning layer may be probabilistic but is constrained by the verified governance layer — achieving formally guaranteed safety properties without requiring formal verification of the AI component itself. The model assumes observable environmental parameters, correct sensor data, valid threshold calibration, and complete enumeration of recommendation types; it does not assume AI model correctness, specific AI methods, specific sensor hardware, or particular user behaviour. The classification f(E) is many-to-one by design: governance mode is a coarse abstraction for scope decisions while the full E vector is passed to the AI layer for fine-grained recommendation generation within the permitted scope. Limitations include governance of recommendation types (not content quality), absence of a formal human behaviour model, threshold sensitivity to calibration quality, a fixed recommendation type set, and no temporal logic specification of transition properties.
