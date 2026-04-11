# The Binary Governance Gap: External Evidence from Safety Shields, Agent Governance, IoT, and Autonomy Frameworks

**Document type**: Gap evidence synthesis / examiner response
**For**: Chapter 2 — Literature Summary and Research Gap
**Question addressed**: What external evidence — beyond the main corpus of 63 papers — confirms that no existing work unifies AI participation governance (Level 1) and advisory scope governance (Level 2) under a classified environmental state variable? Why does every identified system implement binary governance only, and why has no one bridged this gap?

---

## 1. The Argument Structure

The novelty claim of the proposed architecture rests on a specific absence: no existing work implements a governance pair (G(S), A\_AI(S)) conditioned on a classified environmental safety state S ∈ {SAFE, CAUTION, UNSAFE}, where S = f(E) and E is a vector of observable environmental parameters, such that G(S) determines whether AI may participate, A\_AI(S) determines what AI is permitted to recommend, and the containment property A\_AI(SAFE) ⊃ A\_AI(CAUTION) ⊃ A\_AI(UNSAFE) = ∅ ensures graduated restriction as conditions deteriorate.

To stress-test this claim, eight external papers were selected from four distinct research communities — safety shields, agent governance frameworks, IoT/sensor systems, and autonomy level taxonomies — and examined in full text. Each was selected as a plausible counterexample: a system that might already implement environment-state-conditioned graduated governance. None does. This document presents the evidence, ranks it by impact on the novelty argument, explains the structural distinction between design-time and runtime governance, identifies why the gap persists, and analyses the specific pattern in IoT systems where environmental sensors are used as AI input but never as governance triggers.

---

## 2. Impact Ranking: Eight Papers by Strength of Novelty Evidence

The eight papers are ranked by their contribution to the novelty argument, from strongest to weakest. Strength is determined by three criteria: (a) how close the paper comes to the proposed architecture — the closer the near-miss, the more definitively it establishes the gap; (b) how formally explicit the binary governance pattern is — mathematical formalisation is harder to argue away than vague descriptions; and (c) how much institutional or methodological weight the paper carries.

### 2.1 Zhang et al. (2025) — The Most Explicit Formalisation of Binary Governance

**Impact: Highest**

Zhang et al. (2025) [[notes]](../notes/Developing%20real-time%20IoT-based%20public%20safety%20alert%20and%20emergency%20response%20systems.md) provide the single most mathematically explicit proof of the binary governance paradigm. Their Equation 4 defines the alert classification function:

> φ(X(t)) = {1, if P\_alert(X(t)) ≥ θ; 0, otherwise}

This is the governance function reduced to its starkest form: a binary classifier that maps environmental sensor input X(t) to {0, 1}. The system monitors environmental data through a sensor network S = {s₁, s₂, ..., sₙ} (Equation 1), processes it through edge computing with bounded latency (Equations 2–3), evaluates the binary classifier (Equation 4), and produces a total response within 410–450ms (Equation 5, Table 1).

The contrast with the proposed architecture is formally precise. Where Zhang defines φ: X(t) → {0, 1}, the proposed architecture defines S = f(E) → {SAFE, CAUTION, UNSAFE} — a tripartite classification from the same type of environmental input, but producing three governance states rather than two. Where Zhang's φ triggers a binary alert/no-alert, the proposed (G(S), A\_AI(S)) pair produces graduated governance: full AI scope under SAFE, restricted AI scope under CAUTION, no AI under UNSAFE. The containment property A\_AI(SAFE) ⊃ A\_AI(CAUTION) ⊃ A\_AI(UNSAFE) = ∅ has no analogue in Zhang's system.

This paper's impact is highest because it provides a formal equation that can be placed side-by-side with the proposed f(E), making the gap visible as a mathematical structure rather than a conceptual description. An examiner can see, at the level of notation, that one maps to {0, 1} and the other maps to {SAFE, CAUTION, UNSAFE} with differentiated governance at each level.

### 2.2 Feng, McDonald & Zhang (2025) — The Conceptual Revelation of a Missing Governance Dimension

**Impact: Very High**

Feng, McDonald & Zhang (2025) [[notes]](../notes/Levels%20of%20Autonomy%20for%20AI%20Agents.md) contribute the most conceptually significant evidence. Their framework identifies two distinct governance dimensions for AI agents: *agency* (what tools and capabilities the AI can access) and *autonomy* (how much human involvement is required in decision-making). Five levels of autonomy are defined, from Level 0 (no task delegated) to Level 4 (full automation), each specifying a different human-AI interaction pattern (Figure 1).

The decisive finding is twofold. First, both agency and autonomy are "deliberate design decision[s]" (p.2) assigned at deployment time for "a fixed set of capabilities and a fixed operational environment" (p.4). Once an agent is configured as Level 3 (human-confirmed autonomy), it remains Level 3 regardless of whether environmental conditions are calm or dangerous. The governance is a constant — it does not respond to the state of the world.

Second, and more importantly, the agency/autonomy distinction inadvertently reveals a third governance dimension that the framework does not address: *advisory scope* — what the AI is permitted to recommend. Agency controls tool access. Autonomy controls human oversight intensity. Neither controls the *content range* of AI recommendations. An agent with fixed agency (access to weather API, navigation tools) and fixed autonomy (Level 2, human-in-the-loop) can still recommend anything from "optimal fishing route" to "proceed to sea in dangerous conditions" — because nothing in the governance framework restricts recommendation scope based on environmental conditions.

The proposed architecture fills precisely this gap. A\_AI(S) is the missing third dimension: advisory scope governance that changes at runtime based on classified environmental state. Feng et al.'s framework, by being the most rigorous taxonomy of AI governance dimensions, makes the absence of this third dimension formally visible.

### 2.3 Kwon et al. (2025) — The Closest Near-Miss

**Impact: Very High**

Kwon et al. (2025) [[notes]](../notes/Runtime%20Safety%20through%20Adaptive%20Shielding-%20From%20Hidden%20Parameter%20Inference%20to%20Provable%20Guarantees.md) present Adaptive Shielding — the closest existing system to the proposed architecture. It is environment-aware (environment-centric features E ∈ ℝ^n₂ explicitly modelled alongside agent state e(s) ∈ ℝ^n₁, Section 4.2), it adapts at runtime (the shield changes as the system infers hidden parameters), and it operates in safety-critical domains with formal provable guarantees.

The SafetyScore computation (Equations 11–12) evaluates each candidate action against a safety threshold. The pre-safety check (Equation 10) adds an additional layer: if the system detects that it is operating in an out-of-distribution (OOD) range, it triggers fallback. This is a binary decision: within distribution → proceed to SafetyScore evaluation; out of distribution → fallback.

The SafetyScore itself produces a binary outcome for each action: safe (score above threshold) or unsafe (score below threshold). There is no intermediate "proceed with restricted scope" mode. The system either permits the action or blocks it. Despite having all the technical ingredients — environment-centric features, runtime adaptation, formal guarantees — the governance output is binary.

This paper's impact is very high precisely because it is the strongest near-miss. It demonstrates that the AI safety community has built systems with environment-aware, runtime-adaptive governance — and still implemented binary governance at the output level. The gap is not due to technical impossibility; the components exist. The gap is conceptual: no one has connected environment-state classification to graduated advisory scope restriction.

### 2.4 OWASP (2025) — Industry Consensus on Binary Governance

**Impact: High**

The OWASP Top 10 for Agentic Applications (2025) [[notes]](../notes/OWASP%20Top%2010%20for%20Agentic%20Applications%202026.md) carries weight not from formal novelty but from institutional authority. This is the global industry consensus framework for agentic AI security, developed by John Sotiropoulos, Keren Katz, Ron F. Del Rosario and community contributors, published December 2025. It defines 10 vulnerability categories (ASI01–ASI10) with mitigation strategies that collectively represent the security community's current understanding of how to govern AI agents.

Every mitigation across all 10 categories is binary: ASI01#4 (pause/block agent execution), ASI02#1 (least privilege — grant or deny), ASI02#4 (Intent Gate with Policy Enforcement Point/Policy Decision Point — binary authorise/reject), ASI03#3 (per-action authorisation — approve/deny), ASI10#4 (kill-switches — terminate/continue). The Security Mapping Matrix in Appendix A cross-references all vulnerabilities against controls; no control implements graduated scope restriction.

The closest near-miss is ASI09#5 "Adaptive Trust Calibration," which recommends adjusting human oversight level based on task context. This adjusts *how much the human watches* — not *what the AI may recommend*. The oversight level changes; the AI's advisory scope does not.

When an examiner asks "but surely industry has addressed this?", OWASP provides the definitive answer: the global security community's best current framework for agentic AI governance is uniformly binary.

### 2.5 Ogenyi et al. (2025) — The "Adaptive Security ≠ Adaptive Governance" Distinction

**Impact: High**

Ogenyi, Ugwu & Ugwu (2025) [[notes]](../notes/Securing%20the%20future-%20AI-driven%20cybersecurity%20in%20the%20age%20of%20autonomous%20IoT.md) review the entire landscape of AI-driven cybersecurity for Autonomous IoT (A-IoT) — the third generation of IoT that is explicitly "self-governing, adaptive, and capable of autonomous decision-making" (p.3, Figure 1). This is the domain where environment-state-conditioned governance would most naturally appear: sensor-rich environments, autonomous AI systems, explicit discussion of adaptive security.

The paper's most valuable contribution to the gap argument is the conceptual distinction between *adaptive security* and *adaptive governance*. Section 9 articulates the A-IoT community's vision: "security models that can dynamically adapt the level of protection to the level of threat, the state of devices, and the priorities of the work" (p.12). This sounds like graduated governance — but it means adapting *protection intensity* (encryption strength, monitoring depth, detection thresholds), not *governance mode* or *AI advisory scope*.

Three concrete examples confirm this:

- Section 5.5 (p.7): "dynamically switch key sizes, cypher strength, and mode of operation based on the degree of threat" — adapts encryption parameters, not what AI may recommend
- Section 5.4 (p.7): "adjust access privileges on a real-time basis depending on the level of risk" — adapts privilege scope, but the access decision remains binary (authorised/unauthorised)
- Section 5.6 (p.7): Autonomous response systems "take immediate actions without human intervention" including isolating nodes, reorganising networks, deploying decoy services — with no restriction on what response types are permitted based on environmental conditions

The A-IoT review covers 9 AI technique categories (Table 3), 5 application domains (Figure 3), and 100+ references. Across all of them, "adaptive" means adaptive monitoring intensity, not adaptive governance modes with graduated advisory scope.

### 2.6 Chandran et al. (2025) — Environment-as-Input in Aquaculture Engineering

**Impact: Moderate–High**

Chandran et al. (2025) [[notes]](../notes/Smart%20technologies%20in%20aquaculture-%20An%20integrated%20IoT%2C%20AI%2C%20and%20blockchain%20framework%20for%20sustainable%20growth.md) present a systematic review of IoT, AI, and blockchain in aquaculture following PRISMA methodology (350 → 111 papers). Their three-tier architecture (Fig. 7: Edge Subsystem → Digital Farming Platform → Portals) from Qatar University represents the state of the art in aquaculture IoT engineering.

The gap evidence is the environment-as-input pattern. Section 5.2 explicitly discusses climate-aware forecasting — environmental sensors feed AI models that predict conditions — but environmental conditions never govern what the AI system may recommend. Smart contract governance on the blockchain layer (p.11) implements binary execution rules (conditions met → execute, conditions not met → do not execute). The quantitative findings (mortality reduced 45%, water management +30%, CNN accuracy 92%, hybrid AI 95%) demonstrate sophisticated AI capability — deployed entirely within a binary governance framework.

The paper explicitly discusses small-scale adoption barriers, confirming T4 (low-resource environment) relevance for the proposed architecture's target domain.

### 2.7 Tandel et al. (2025) — Domain-Specific Binary Governance in Fisheries

**Impact: Moderate**

Tandel et al. (2025) [[notes]](../notes/Smart%20Aquaculture-%20IoT%20and%20AI%20Application%20for%20Sustainable%20Fisheries.md) review IoT and AI applications in sustainable fisheries from the College of Fisheries Science, Kamdhenu University, Veraval, India. As a practitioner-oriented article (published in *The Science World* e-magazine), its methodological weight is lower than peer-reviewed sources. Its value is domain-specific: it directly addresses the proposed architecture's target application area.

Three concrete examples confirm binary governance in fisheries IoT:

- Arduino Uno fish tank management: "sends automated SMS alerts in case of abnormal conditions" (p.4) — binary: abnormal → alert, normal → no alert
- Smart control systems: "automatically adjusting temperature, oxygen levels and other critical factors to maintain ideal conditions" (p.3) — binary: out-of-range → adjust, in-range → no action
- Cloud-based management: "Automated alert systems notify operators of any deviations, allowing for immediate corrective actions" (p.5) — binary: deviation → alert → corrective action

The paper explicitly identifies small-scale fisheries barriers: "less accessible to small-scale aquaculture farmers who may lack the necessary capital" (p.6) and "remote areas where internet connectivity is limited or unreliable" (p.6). Claims should be corroborated with Chandran et al. (2025) [[notes]](../notes/Smart%20technologies%20in%20aquaculture-%20An%20integrated%20IoT%2C%20AI%2C%20and%20blockchain%20framework%20for%20sustainable%20growth.md) which covers similar ground with higher methodological rigour.

### 2.8 Hamel-De le Court, Belardinelli & Goodall (2025) — Probabilistic but Still Binary

**Impact: Moderate**

Hamel-De le Court, Belardinelli & Goodall (2025) [[notes]](../notes/Probabilistic%20Shielding%20for%20Safe%20Reinforcement%20Learning.md) extend safety shields with probabilistic guarantees — P(safe) ≥ 1 − ε — which is a formal advance over deterministic shields. The probabilistic threshold ε allows tuning the trade-off between safety and performance. But the governance output remains binary: each action is either permitted or replaced by the shield. There is no intermediate "permitted with restricted scope" category. The probability threshold is set at design time, not conditioned on runtime environmental state classification.

This paper confirms that even when the shield literature moves from deterministic to probabilistic guarantees, the fundamental governance structure — permit or block — does not change. The proposed architecture's tripartite classification and graduated advisory scope remain absent.

---

## 3. Design-Time Assignment vs. Runtime Environment-State-Conditioned Governance

The distinction between design-time assignment and runtime environment-state-conditioned governance is the central structural difference between the proposed architecture and all existing work. It can be stated formally.

**Design-time governance** assigns governance parameters as constants before deployment. In Feng et al.'s framework, the autonomy level L is chosen at design time and remains fixed:

> G = L, where L ∈ {0, 1, 2, 3, 4} is a constant

Regardless of whether the wind is 5 knots or 50 knots, the agent's autonomy level does not change. In SAFEXPLAIN (Abella et al., 2025), the DL usage level — whether AI provides a suggestion or a decision — is configured per deployment scenario, not adjusted by runtime conditions. In Feng et al.'s own words, the framework applies to "a fixed set of capabilities and a fixed operational environment" (p.4). When the environment is not fixed — when conditions change — the governance framework has no response mechanism.

**Runtime environment-state-conditioned governance** makes governance a function of current environmental conditions:

> S(t) = f(E(t)), where E(t) = {w(t), r(t), m(t), o(t), v(t), t}

At each time t, the environmental state vector E(t) — wind speed w, rainfall r, marine warning m, ocean state o, vessel category v, time of day t — is evaluated, producing a classified safety state S(t) ∈ {SAFE, CAUTION, UNSAFE}. The governance pair (G(S(t)), A\_AI(S(t))) then determines both whether AI participates and what it may recommend — and these determinations change as the environment changes.

The structural consequences are:

1. **Design-time governance cannot respond to environmental deterioration.** A Level 3 agent in Feng's taxonomy remains Level 3 during a storm. The governance provides no mechanism to reduce AI advisory scope as conditions deteriorate. An "emergency off-switch" (Feng, p.8) provides binary termination — not graduated restriction.

2. **Runtime governance enables the CAUTION mode that no existing work implements.** The CAUTION state is the critical innovation. In CAUTION, AI participates (G(CAUTION) = 1) but with restricted scope (A\_AI(CAUTION) ⊂ A\_AI(SAFE)). This is impossible under design-time governance, which has no mechanism to restrict scope without terminating participation. In binary runtime governance (Kwon, Zhang, OWASP), the options are "full scope" or "blocked" — the intermediate state does not exist.

3. **The containment property is a runtime invariant, not a design-time configuration.** A\_AI(SAFE) ⊃ A\_AI(CAUTION) ⊃ A\_AI(UNSAFE) = ∅ must hold at every point in time as conditions change. This is a dynamic property — it constrains the system's trajectory through governance states, not a static configuration. No design-time framework defines or enforces such a property.

4. **The Safety Dominance Property — AI(E) ⊆ A\_AI(S) for all E — requires runtime enforcement.** The guarantee that the AI's actual output is always within the permitted advisory scope for the current environmental state must be verified continuously. Design-time governance provides this trivially (the scope never changes), but cannot provide graduated restriction — it offers the safety of a locked door, not the nuance of a door that opens wider in calm conditions and narrows in dangerous ones.

---

## 4. Why Nobody Has Done This: Three Structural Explanations

The eight papers reveal three structural reasons why the gap persists. These are not failings of individual researchers but structural features of how the relevant communities organise their work.

### 4.1 The Disciplinary Boundary Between AI Safety and Environmental Sensing

The AI safety community (represented by Kwon et al., Hamel-De le Court et al., Feng et al., OWASP) builds governance mechanisms but conceptualises the world in terms of *internal system states*: agent capabilities, model confidence, action safety scores, threat levels, policy compliance. The environmental sensing community (represented by Zhang et al., Chandran et al., Tandel et al., Ogenyi et al.) has rich environmental data — pH, temperature, wave height, wind speed — but uses it exclusively as *input to AI reasoning*, never as a trigger for governing AI output scope.

Kwon et al. (2025) [[notes]](../notes/Runtime%20Safety%20through%20Adaptive%20Shielding-%20From%20Hidden%20Parameter%20Inference%20to%20Provable%20Guarantees.md) come closest to bridging this boundary: they explicitly model environment-centric features E ∈ ℝ^n₂. But these features feed into a SafetyScore that evaluates individual actions — they do not classify the environmental state into governance modes. The environment is a parameter of the safety evaluation, not a governance trigger. Zhang et al. (2025) [[notes]](../notes/Developing%20real-time%20IoT-based%20public%20safety%20alert%20and%20emergency%20response%20systems.md) have sensors, edge computing, and real-time classification — all the infrastructure for environment-state-conditioned governance — but their classification function φ maps to {0, 1}, not to graduated governance states.

The proposed architecture sits precisely at this disciplinary intersection. It takes the governance mechanisms of the AI safety community (participation control, advisory scope restriction, formal safety properties) and the environmental sensing infrastructure of the IoT community (real-time environmental monitoring, state classification) and connects them: environmental state classification → governance mode selection → graduated AI advisory scope restriction.

### 4.2 Binary Governance as the Default Mental Model

Across all eight papers and all four research communities, the default governance output is binary: permit/block, safe/unsafe, alert/no-alert, authorise/reject. This is true even when researchers explicitly discuss "adaptive" systems.

Ogenyi et al. (2025) [[notes]](../notes/Securing%20the%20future-%20AI-driven%20cybersecurity%20in%20the%20age%20of%20autonomous%20IoT.md) are the clearest example. The entire A-IoT review discusses "adaptive security" — systems that adapt to threats — and every adaptation is an adjustment of binary monitoring intensity, not a change in governance mode. "Dynamically adapt the level of protection to the level of threat" (p.12) means: detect more carefully, encrypt more strongly, authenticate more stringently — but the governance decision for any specific action remains permit or block. The OWASP framework (2025) [[notes]](../notes/OWASP%20Top%2010%20for%20Agentic%20Applications%202026.md) similarly defines "Adaptive Trust Calibration" (ASI09#5) as adjusting oversight intensity, not as changing what the AI may recommend.

The conceptual leap required is from "how intensely do we monitor/protect?" to "what is the AI permitted to recommend given current conditions?" This is a shift from governance-as-intensity to governance-as-scope. The binary model treats governance as a filter with adjustable sensitivity. The proposed model treats governance as a scope selector with environmentally-conditioned modes. No paper in the eight makes this shift.

### 4.3 The Two-Level Unification Has No Precedent

The most structurally novel aspect of the proposed architecture is not Level 1 (participation control — well-established in shields) or Level 2 (output restriction — well-established in guardrails) individually, but their *unification under a single classified environmental state variable*.

Feng et al. (2025) [[notes]](../notes/Levels%20of%20Autonomy%20for%20AI%20Agents.md) govern participation (autonomy levels) but not advisory scope. OWASP (2025) [[notes]](../notes/OWASP%20Top%2010%20for%20Agentic%20Applications%202026.md) implements per-action output filtering but not state-conditioned participation governance. Kwon et al. (2025) [[notes]](../notes/Runtime%20Safety%20through%20Adaptive%20Shielding-%20From%20Hidden%20Parameter%20Inference%20to%20Provable%20Guarantees.md) provide runtime adaptive participation control but not graduated advisory scope. No paper governs both simultaneously via the same classified state.

The governance pair (G(S), A\_AI(S)) means that a single state classification S = f(E) simultaneously answers two questions: "Does AI participate?" (G(S)) and "What may AI recommend?" (A\_AI(S)). The answers change together as environmental conditions change. This unification creates a formally parsimonious architecture — one classification, two governance functions, three states — that is absent from all existing work.

---

## 5. The IoT+AI Gap: Environment as Input, Not Governance Trigger

Four of the eight papers (Zhang et al., Chandran et al., Tandel et al., Ogenyi et al.) come from the IoT domain. Together they confirm a universal pattern: **environmental sensors → AI input → binary output**. The environment feeds the AI; it does not govern the AI.

### 5.1 The Pattern Across IoT Domains

**Public safety (Zhang et al.):** Environmental sensors S = {s₁, s₂, ..., sₙ} collect data → edge computing processes it → binary classifier φ(X(t)) → alert or no alert. The sensors are the governance infrastructure, but the governance output is {0, 1}.

**Aquaculture engineering (Chandran et al.):** Environmental sensors (pH, temperature, dissolved oxygen) → AI prediction models (CNN 92%, hybrid 95%) → automated intervention. Smart contract governance on the blockchain: conditions met → execute, conditions not met → do not execute. Environmental data drives AI reasoning; it does not restrict AI recommendation scope.

**Fisheries practice (Tandel et al.):** Arduino Uno sensors (pH, turbidity, water levels) → threshold comparison → SMS alert. Smart control systems → auto-adjust to maintain ideal parameters. Cloud platforms → deviation alerts. Every path leads to a binary output: alert/no-alert, adjust/maintain, deviate/normal.

**Autonomous IoT cybersecurity (Ogenyi et al.):** IDS/IPS → block/allow. Anomaly detection → normal/anomalous. Malware classification → malware/benign. Authentication → authorised/unauthorised. Across all six cybersecurity technique categories (Section 5), every AI governance decision is binary.

### 5.2 Why IoT Has the Infrastructure but Not the Architecture

The irony is that IoT systems already possess every technical component the proposed architecture requires:

1. **Environmental sensors** — real-time monitoring of physical conditions (temperature, pH, wind, waves, dissolved oxygen)
2. **Edge computing** — local processing with bounded latency (Zhang: 410–450ms)
3. **AI models** — trained on environmental data for prediction, classification, and optimisation
4. **Communication infrastructure** — data transmission to cloud platforms and mobile interfaces
5. **Automated actuation** — ability to change system behaviour based on sensor readings

What is missing is a single architectural layer: the **environmental state classifier** that maps sensor readings to governance modes, and the **governance pair** that uses those modes to simultaneously control AI participation and advisory scope. The sensors exist. The AI exists. The actuation exists. The graduated governance layer that connects them does not.

Chandran et al. (2025) [[notes]](../notes/Smart%20technologies%20in%20aquaculture-%20An%20integrated%20IoT%2C%20AI%2C%20and%20blockchain%20framework%20for%20sustainable%20growth.md) describe a three-tier architecture (Edge Subsystem → Digital Farming Platform → Portals). The proposed architecture adds a governance tier between the sensor layer and the AI advisory layer — a tier that classifies environmental state and uses that classification to govern what the AI tier may produce. This is an architectural insertion, not a replacement. It is compatible with existing IoT infrastructure and does not require new sensor technology.

### 5.3 The Conceptual Leap

The conceptual leap required is this:

**Current paradigm:** Environment → AI input → AI processes data → AI recommends → Human decides

**Proposed paradigm:** Environment → State classifier S = f(E) → Governance pair (G(S), A\_AI(S)) → AI recommends *within permitted scope* → Human decides

The difference is a governance layer *between* the environmental sensing and the AI advisory function. This layer does not exist in any of the four IoT papers, nor in any of the four AI safety papers. The sensors see the environment but do not govern the AI based on what they see. The AI safety systems govern the AI but do not see the environment as a governance trigger. The proposed architecture connects what IoT systems observe to how AI safety systems govern.

---

## 6. Synthesis

The eight papers collectively establish four findings:

1. **Binary governance is universal.** Every paper — from Zhang's mathematical φ(X(t)) = {0, 1} to OWASP's 10 vulnerability categories to Ogenyi's entire A-IoT landscape — implements binary governance at the output level. The most sophisticated systems (Kwon's Adaptive Shielding) have environment-aware, runtime-adaptive internal mechanisms, but the governance output is still permit/block.

2. **Design-time governance cannot address dynamic environments.** Feng et al.'s autonomy levels, OWASP's security controls, and Hamel-De le Court et al.'s probabilistic thresholds are all fixed at configuration time. When environmental conditions change — when weather deteriorates, when sea state shifts — these frameworks provide no mechanism to graduate AI governance. The only response available is binary: continue unchanged or terminate.

3. **IoT systems have the infrastructure but not the governance architecture.** Zhang, Chandran, Tandel, and Ogenyi collectively demonstrate that environmental sensing, edge computing, AI models, and automated actuation all exist in deployed systems. The missing component is the graduated governance layer that classifies environmental state and uses it to govern AI advisory scope. The proposed architecture fills this specific gap with a formally defined mechanism.

4. **The gap persists because of disciplinary boundaries and the binary mental model.** The AI safety community thinks in terms of internal system states; the IoT community uses environmental data as AI input, not governance trigger. Both communities default to binary governance (permit/block) even when discussing "adaptive" systems. The proposed architecture bridges these communities by connecting environmental state classification (from IoT) to graduated governance (extending AI safety) through the unified governance pair (G(S), A\_AI(S)).

The proposed architecture is not a marginal extension of existing work. It is a structural innovation that introduces a governance mechanism — environment-state-conditioned graduated advisory scope restriction — that is absent from all four research communities examined. The evidence from eight full-text verified papers, spanning safety shields, agent governance, IoT systems, and autonomy frameworks, confirms that this gap is genuine and the contribution is novel.
