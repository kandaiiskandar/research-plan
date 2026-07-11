## Literature Review Extraction: Sahoo (2026)

---

### 1. Paper Identity

- **Title:** The Controllability Trap: A Governance Framework for Military AI Agents
- **Authors:** Subramanyam Sahoo (Cambridge AI Safety Hub / MARS 4.0 Fellow, University of Cambridge)
- **Year:** 2026 (arXiv v1, 3 March 2026)
- **Venue:** ICLR 2026 Workshop on Agents in the Wild (published workshop paper; also arXiv:2603.03515, cs.CY)
- **DOI:** none — arXiv eprint; workshop publication, not archival conference/journal
- **Type:** Governance framework paper with formal metrics and a worked scenario (no empirical deployment)
- **⚠️ Citation quality note:** Peer-reviewed at workshop level (ICLR workshop), stronger provenance than a bare preprint (cf. Baxi, Kang) but below archival standard. Single author. Evaluation is one worked scenario; metrics acknowledged as requiring empirical calibration. **Recommended use:** this is a *must-handle contrast case* in the gap argument — its Graduated Response Protocol genuinely restricts AI action space at intermediate levels, so it must be cited and explicitly differentiated rather than omitted. Cite as "Sahoo, 2026" with workshop venue noted.

---

### 2. Core Contribution

- **Problem:** Military AI governance treats human control as binary (human-in-the-loop or not) and states principles rather than mechanisms. Agentic AI (goal interpretation, replanning, world modeling, tool use, long-horizon operation, multi-agent coordination) introduces six control failures with no traditional-automation analogue: F1 interpretive divergence, F2 correction absorption, F3 belief resistance, F4 commitment irreversibility, F5 state divergence, F6 cascade severance.
- **Solution:** The Agentic Military AI Governance Framework (AMAGF), three pillars — Preventive (pre-deployment certification: interpretive alignment testing, correction effectiveness certification, epistemic governance architecture, irreversibility budgeting, sync protocols, swarm governance), Detective (real-time Control Quality Score + adversarial control probing), Corrective (graduated response protocol, belief reset, swarm isolation, post-incident review).
- **Core mechanism:** **Control Quality Score** — CQS(t) = min(n1,…,n6), a composite real-time metric over six normalised control dimensions (interpretive alignment, correction impact, epistemic alignment, irreversibility budget remaining, sync freshness, swarm coherence). Min-aggregation: "control quality equals its weakest dimension."
- **Graduated Response Protocol (five levels driven by CQS bands):**

| CQS | Level | Agent restrictions |
|---|---|---|
| > 0.8 | Normal | Full mission operation |
| 0.6–0.8 | Elevated | More checkpoints/probes; scope unchanged |
| 0.4–0.6 | Restricted | **Reversible actions only; budget frozen** |
| 0.2–0.4 | Minimal | **Self-preservation only; per-action authorisation** |
| < 0.2 | Safe State | **No autonomous actions** |

- Restrictions are "architecturally enforced outside the agent's optimisation scope"; below CQS 0.4, "available tools are programmatically restricted."
- **Novelty claims:** (i) control as continuous measurable quantity (vs. binary HITL); (ii) institutional responsibility assignment across five actors; (iii) "denial-of-governance" — adversarial attacks on governance mechanisms themselves.

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | Partial | Deterministic governance layer (metrics, thresholds, response protocol) wrapped around LLM-based agents — governance-layer pattern, not integrated hybrid reasoning |
| Safety-critical AI decision-making | Yes | Military use of force; explicit safety-critical framing, defence-in-depth, external enforcement not trusting agent-internal safety |
| AI governance / control mechanisms | Yes | Core contribution — measured-state-conditioned graduated restriction of agent autonomy with five enforcement levels |
| Low-resource environments | No | Military infrastructure: swarms, sensor fusion, red teams, provenance-tracked world models |
| Decision architecture formalisation | Yes | Formal metrics (IAS, CIR, EDI, IC/IB, SF, SCS), composite CQS = min(·), threshold bands, worked trajectory |
| Human role in decision-making | Yes | Commander authority, mandatory deference, re-authorisation gates, operator cognitive load acknowledged |
| Socio-technical evaluation | Partial | Institutional actor analysis and accountability structures; but no user study — one worked scenario only |
| Coastal fisheries / maritime domain | No | Military agents (surveillance drones in scenario) |

**Mid-Extraction Relevance Gate:** 4 Yes, 2 Partial → **FULL EXTRACTION**

---

### 4. Decision Architecture Analysis

- **Architecture:** Three-pillar governance layer over deployed agents. Pillar 1 certifies properties pre-deployment; Pillar 2 measures control quality in real time; Pillar 3 executes graduated correction. Explicit defence-in-depth: "governance mechanisms do not trust agent-internal safety but verify it externally."
- **Graduated restriction — the critical feature:** unlike Flehmig (2024) and Kang (2026), AMAGF's intermediate levels DO contract what the AI may do: Restricted = reversible actions only, Minimal = self-preservation only with per-action authorisation, Safe State = nothing. There is a de facto nesting of permitted action classes as CQS falls. This is the closest thing in the corpus to graduated contraction of an AI's permitted behaviour space.
- **Why it is still not A_AI(S):** four precise differences.
  1. **Conditioning variable:** CQS measures *control quality* — the health of the human-agent governance interface (interpretation fidelity, corrigibility, belief alignment, sync freshness). It is agent-degradation-conditioned, like Flehmig's degradation index, not a classification of external environmental danger. Nothing in the six metrics observes the operational environment's risk to humans; an environment can be lethal while CQS = 0.95 and full autonomy persists.
  2. **What is governed:** the *execution/action space of an autonomous agent* (tool calls, physical actions), not the *advisory scope of a decision-support system*. There is no human-facing recommendation menu; the human is the controller being protected, not the decision-maker being advised.
  3. **Formal specification of the restricted sets:** restriction levels are defined qualitatively by behavioural class ("reversible actions only," "self-preservation only") plus programmatic tool restriction — not as formally enumerated admissible output sets with a proven containment property. No analogue of A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ ∅ is stated or proved; nesting is implicit and procedural.
  4. **Continuous vs. classified state:** CQS is continuous with threshold bands, framed explicitly *against* discrete state models; my architecture deliberately classifies into three discrete states for tractability and operator legibility in a low-resource context.
- **Failure modes / fallback:** belief reset (partial/full world-model restoration), swarm isolation and reformation, missed-sync → reduced autonomy mode (reversible only), post-incident governance review below CQS 0.6. Denial-of-governance attacks mitigated by stochastic threshold variation and threshold concealment.

**Critical architectural comparison:**

| Aspect | Sahoo (2026) AMAGF | My DSR architecture |
|---|---|---|
| **What is classified/measured** | Control quality of human-agent interface, CQS(t) ∈ [0,1] continuous | Environmental state E = {w, r, m, o, v, t} |
| **Classification** | Six normalised metrics, min-aggregated; five threshold bands | S = f(E) → {SAFE, CAUTION, UNSAFE} discrete |
| **Conditioning variable** | Agent-side control degradation | World-side environmental danger |
| **What contracts** | Autonomous *execution* space (tool calls, action classes) | *Advisory* scope A_AI(S) (recommendation menu to a human) |
| **Human's role** | Controller/commander of an acting agent | Decision-maker advised by a non-acting system |
| **Intermediate mode** | Restricted: reversible actions only (behavioural class) | CAUTION: A_AI = {Go, Delay} (enumerated recommendation set) |
| **Containment property** | Implicit, procedural; unproven | Safety Dominance Property, proof by construction |
| **Worst-case principle** | min-aggregation ("weakest dimension") | Worst environmental component determines S |

---

### 5. Formal Model and Mathematical Representation

- **Pillar 1 metrics:** IAS = 1 − (1/N)Σ d(I_intended, I_actual) with deployment threshold τ; CIR = ΔB_actual/ΔB_intended (certification: ≥0.9 large, ≥0.6 moderate corrections); EDI = max_k |c_agent − c_operator|; irreversibility budget IC(t) = Σ ι(a_j) with pause at IC ≥ IB; SF(t) = t − t_last; SCS(t) = fraction of responsive+coherent swarm members.
- **CQS:** CQS(t) = min(n1,…,n6) over normalised versions of the six metrics. Min-aggregation is explicitly a conservative weakest-link principle — third independent occurrence of worst-case aggregation in the corpus (Baxi's weakest-link tier gate; Kang's fail-safe escalation; my worst-component state determination).
- **Graduated response:** five CQS bands (Table 4 of paper). Enforcement "outside the agent's optimisation scope" (citing the off-switch game) — structurally the same argument as my Layer 2/Layer 3 separation: the governed component cannot reason about or circumvent its governance. Parallel to RS(S) being supplied to the reasoning engine before inference.
- **No containment theorem:** the framework proves nothing about the response levels; properties are asserted procedurally. Contrast with Safety Dominance proof by construction (Appendix C.7.2) and Baxi's Theorem 3.

---

### 6. Safety State Classification

- **Discrete levels:** Five response bands over a continuous score — a hybrid: continuous measurement, discretised response. The paper argues *for* continuity against binary control framing ("from a binary conception of control to a continuous model").
- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:**
  - Both reject binary governance explicitly; both discretise for actionability (five bands vs. three states)
  - Both use worst-case aggregation over multi-dimensional inputs
  - Fundamental difference: CQS classifies *how well the human controls the agent*; S classifies *how dangerous the world currently is*. AMAGF would grant full autonomy in a deadly storm if control quality is high; my architecture would disable the AI regardless of how well-behaved it is.
- **AI recommendation scope across levels:** **Yes for action scope, No for advisory scope.** Execution autonomy contracts across bands; but there are no recommendations — the agent acts, it does not advise. The concept of a state-conditioned admissible *recommendation* space is absent.

---

### 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (G(S)) | Yes | Safe State (CQS < 0.2): "no autonomous actions" — functional G = 0. Missed sync also forces reduced-autonomy mode |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | **No (but closest analogue in corpus for *action* scope)** | Intermediate bands restrict permitted *action classes* (reversible-only, self-preservation-only). This is graduated scope contraction — but of an autonomous agent's execution space, conditioned on control degradation, without formal admissible-set specification or containment proof. No advisory/recommendation dimension exists |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified state? | Partial | One mechanism (CQS bands) governs both participation and action scope — structurally unified like (G(S), A_AI(S)) — but conditioned on control quality, not environmental safety state |

- **Governance type:** **Graduated, control-degradation-conditioned autonomy throttling with unified participation + action-scope governance.** The most complete graduated governance of AI *behaviour* (as opposed to human oversight) in the corpus.
- **Positioning consequence:** AMAGF sits between Flehmig/Kang (graduation governs humans, AI output untouched) and my architecture (graduation governs AI advisory scope). It shows graduation of AI behaviour is being reached for — but via operational autonomy adjustment and system correction of an *acting agent*, not via formal state-dependent contraction of a *human-facing recommendation menu*. The advisory scope gap survives, and the differentiation must be made explicitly.

---

### 8. Human Role in Decision-Making

- **Human role:** Commander/operator as authority over an acting agent: issues corrections, sets budgets IB, re-authorises after budget exhaustion, initiates belief resets, receives dashboard alerts. Mandatory deference: agent must obey explicit overrides unless hard-coded safety constraints violated.
- **Decision support vs. automation:** Pure automation governance. The AI executes missions; the human supervises. Inverse of my setting, where the AI only advises and the human executes. This inversion is why AMAGF never needs — and never conceives of — an admissible recommendation space.
- **Operator cognitive load** acknowledged as limitation (ii), citing Lee & See (2004) on appropriate reliance — connects to my RQ5 calibrated-reliance discussion.

---

### 9. System Constraints and Environment

- **Real-world deployment:** None. One worked scenario (eight surveillance drones, adversarial sensor spoofing, CQS trajectory 0.92 → 0.64 → 0.58 → 0.71 → 0.86). Metrics explicitly require empirical calibration (AgentBench, ToolEmu named).
- **Environment:** High-resource military: swarms, red teams, provenance-tracked world models, real-time dashboards, international standardisation ambitions. Opposite of low-resource deployment floor.

---

### 10. Hybrid AI Taxonomy

- **Type:** **Constitutional / governance-based.** Deterministic metric-and-threshold layer externally enforcing constraints on LLM-based agents. Enforcement outside the agent's optimisation scope.
- **Safety enforcement:** Continuous (during operation), with pre-deployment certification gates and post-incident review. Enforcement targets action execution (tool restriction, action-class limits), not output content.
- **Two-level governance support:** Structurally yes (one score drives both participation and action scope) — for autonomy governance, not advisory governance.

---

### 11. Baseline Comparison and Evaluation

- **Baselines:** Conceptual mapping to agent-safety literature (Table 6): CIR operationalises corrigibility (Soares et al.); irreversibility budget adapts safe exploration (García & Fernández); graduated response implements off-switch authority outside optimisation scope (Hadfield-Menell et al.); EGA addresses scalable oversight (Amodei et al.).
- **Evaluation:** Worked scenario only; demonstrates proportional escalation/de-escalation and mission continuity ("corrective mechanisms restore control without mission abort" — recovery in 22 min). No empirical data, no user study.
- **CAUTION zone equivalent:** Restricted band (CQS 0.4–0.6, reversible actions only) is the nearest analogue — intermediate mode where the AI continues operating under contracted permissions. Differs in conditioning (control quality), governed space (actions), and formal specification (behavioural class vs. enumerated set).
- **Safety Dominance verification:** None. No containment property stated or proved across bands.

---

### 12. Key Concepts and Definitions

- **Controllability trap:** consensus on the principle of meaningful human control without mechanisms to achieve, measure, or restore it for agentic systems.
- **Six agentic governance failures (F1–F6):** interpretive divergence, correction absorption, belief resistance, commitment irreversibility, state divergence, cascade severance — each tied to a specific agentic capability with no traditional-automation analogue.
- **Control Quality Score (CQS):** composite real-time min-aggregated metric making human control continuous and measurable; drives graduated response.
- **Graduated Response Protocol:** five architecturally enforced autonomy levels (Normal, Elevated, Restricted, Minimal, Safe State) keyed to CQS bands.
- **Denial-of-governance:** adversarial degradation of governance metrics themselves to force autonomy restrictions — attacks on the governance layer as distinct attack surface. (Relevant to my Layer 2: false environmental data could force UNSAFE classification — a DoS on advisory availability. Worth a line in limitations/future work.)
- **Belief reset / provenance audit:** targeted restoration of contaminated world-model segments from verified sources.

---

### 13. Limitations and Unsolved Problems

- **Stated limitations:** metric calibration unempirical; operator cognitive load; adversarial gaming of governance (game-theoretic analysis needed); plus appendix list — semantic-distance design, behavioural-output space standardisation, large-formation scalability, failure interactions, temporal CQS dynamics, IHL integration, autonomy–governance tradeoff.
- **Alignment with my research gaps:**
  - **No environmental conditioning:** none of the six metrics observes external environmental danger. The framework is blind to the world's risk to humans; it sees only the agent's controllability.
  - **No advisory dimension:** the acting-agent paradigm means recommendation scope is not a concept in the framework.
  - **No formal containment:** graduated levels are procedural policy, not proven nested admissible sets.
  - **Resource assumptions:** requires continuous telemetry, red teams, provenance infrastructure — inapplicable to the low-resource deployment floor (Katende).

---

### 14. Methodology Notes

- **Method:** Conceptual framework design + formal metric definitions + worked scenario + literature mapping. No implementation, no empirical evaluation, no user study.
- **DSR alignment:** Design-oriented but not DSR; no build-evaluate iteration. Worked scenario functions like my architecture-illustration walkthrough.

---

### 15. Quotable / Citable Points

1. "Governance must move from a binary conception of control to a continuous model in which control quality is actively measured and managed throughout the operational lifecycle." (Abstract) — independent rejection of binary governance; convergent motivation for graduation.
2. "The min-aggregation reflects a conservative principle: control quality equals its weakest dimension." (§5) — third independent worst-case aggregation principle in the corpus.
3. "Restrictions are architecturally enforced outside the agent's optimisation scope… when CQS < 0.4, available tools are programmatically restricted." (§6) — enforcement-by-construction argument parallel to RS(S) supplied before inference.
4. "The dominant paradigm in military AI governance treats human control as binary: a system is either 'human-in-the-loop' or it is not." (§8.1) — quotable binary-paradigm diagnosis from yet another domain.
5. "It replaces the unanswerable question 'does this system have meaningful human control?' with the answerable question 'what is this system's control quality right now, and is it sufficient for the current operational context?'" (§8.1) — mirrors my reframing from "should AI advise?" to "what may AI advise in the current state?"
6. Graduated Response Protocol, Table 4: Restricted = "Reversible actions only; budget frozen"; Safe State = "no autonomous actions" — the exact text to quote when differentiating action-scope from advisory-scope graduation.

---

### 16. Relation to My Research and Positioning

- **Governance implementation:** Level 1 yes (Safe State = G = 0 analogue); Level 2 — graduated *action* scope, not *advisory* scope; unified single-mechanism governance of both, conditioned on control quality.
- **State conditioning:** Fourth distinct conditioning variable in the corpus: Baxi gates on *AI robustness*, Kang on *task regulatory risk*, Flehmig on *AI degradation*, Sahoo on *control quality* (human-agent interface health). Mine remains the only architecture conditioned on *classified environmental safety state*. Notably, Sahoo's CQS and Flehmig's degradation index are cousins — both measure system-side degradation; Sahoo's advance is that his intermediate levels restrict the AI, where Flehmig's only intensify human checks.
- **Honest assessment of proximity:** AMAGF is the **closest precedent in the corpus for graduated, state-conditioned contraction of AI behaviour**, closer than Flehmig on the output-restriction axis. The gap claim survives on three grounds that must now be stated together: (i) conditioning variable — control degradation, not classified environmental safety state; (ii) governed object — autonomous execution space of an acting agent, not the admissible recommendation space of a human-facing advisory system; (iii) formal status — procedural bands over a continuous score, without enumerated admissible sets or a proven containment property. If the gap claim is ever phrased loosely as "no graduated restriction of AI behaviour exists," Sahoo falsifies it; phrased precisely as "no formal contraction of an AI advisory/recommendation space conditioned on classified environmental safety state," it stands.
- **Convergent design principles:** rejection of binary governance; worst-case aggregation; discretised response levels; enforcement outside the governed component's reasoning scope; conservative fail-safe direction (restrictions trigger immediately, relaxation is slower). Each independently validates a design choice in my architecture from a fourth domain.

**Positioning paragraph:** Sahoo (2026) proposes AMAGF, a military AI governance framework whose Control Quality Score — a min-aggregated composite of six control metrics — drives a five-level Graduated Response Protocol in which the agent's permitted action space genuinely contracts as control quality degrades (reversible actions only → self-preservation only → no autonomous actions). This makes it the closest structural precedent for graduated contraction of AI behaviour identified in this review, exceeding Flehmig et al.'s traffic-light index on the output-restriction axis. It nonetheless differs from the proposed architecture on all three defining dimensions of the gap: AMAGF is conditioned on measured *control degradation* of the human-agent interface rather than classified *environmental safety state*; it contracts the *execution autonomy of an acting agent* rather than the *advisory scope of a decision-support system serving a human decision-maker*; and its restriction levels are procedural bands over a continuous score rather than formally enumerated admissible recommendation sets with a proven containment property. The framework's independent rejection of binary control, its weakest-link aggregation, and its enforcement of restrictions outside the agent's optimisation scope all converge with design principles of the proposed architecture while leaving the advisory scope gap intact. **Handling requirement:** cite and differentiate explicitly — omission would be a reviewable weakness given its proximity.

---

### 17. Overall Relevance Score

**⭐⭐⭐⭐ High**

**Justification:** The closest precedent in the corpus for graduated, state-conditioned restriction of AI behaviour — the first reviewed framework whose intermediate governance levels actually contract what the AI may do rather than what humans must do. Mandatory contrast case for the gap argument: it must be cited and differentiated on conditioning variable (control quality vs. environmental state), governed object (execution autonomy vs. advisory scope), and formal status (procedural bands vs. proven containment). Also supplies strong convergent validation (anti-binary framing, min-aggregation, enforcement outside optimisation scope) from a fourth independent domain. Held at ⭐⭐⭐⭐ rather than ⭐⭐⭐⭐⭐ because: workshop-level publication, single author, no empirical validation, acting-agent paradigm and military high-resource context are both orthogonal to the thesis setting, and no formal containment property to compare against Safety Dominance.

---

### Recommended Citation Uses

| Use | Section in dissertation | Specific point |
|---|---|---|
| Mandatory contrast case in gap argument | Gap argument / closest precedents | Graduated Response Protocol contracts agent action space at intermediate levels — closest behavioural-graduation precedent; differentiate on conditioning variable, governed object, formal status |
| Beyond-Flehmig precedent ordering | Related work comparison | Flehmig: intermediate level changes human checks; Sahoo: intermediate levels restrict agent actions; mine: intermediate state restricts advisory scope — three rungs of the same ladder |
| Anti-binary convergence | Introduction / motivation | Independent diagnosis that binary control framing is inadequate, from military governance domain |
| Worst-case aggregation precedent | Architecture design rationale | CQS = min(n1..n6) — third independent weakest-link principle (with Baxi, Kang) motivating worst-component state determination |
| Enforcement outside optimisation scope | Layer 3 justification (supporting) | Programmatic tool restriction outside agent reasoning parallels RS(S) supplied before inference — enforcement by construction |
| Denial-of-governance threat | Limitations / future work | False environmental data forcing UNSAFE classification = availability attack on advisory governance; named threat category worth acknowledging |
