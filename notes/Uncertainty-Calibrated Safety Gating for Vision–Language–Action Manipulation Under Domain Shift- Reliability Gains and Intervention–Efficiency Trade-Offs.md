## Literature Review Extraction: Ghaleb et al. (2026)

---

### 1. Paper Identity

- **Title:** Uncertainty-Calibrated Safety Gating for Vision–Language–Action Manipulation Under Domain Shift: Reliability Gains and Intervention–Efficiency Trade-Offs
- **Authors:** Atef M. Ghaleb, Ali S. Allahloh, Sobhi Mejjaouli, Mohammed A. H. Ali, Adel Al-Shayea (Alfaisal University; Aligarh Muslim University; Universiti Malaya; King Saud University)
- **Year:** 2026 (published 15 May 2026)
- **Venue:** *Sensors*, vol. 26, no. 10, art. 3140 (MDPI)
- **DOI:** 10.3390/s26103140
- **Type:** Empirical runtime-supervision study — simulation benchmark (NVIDIA Isaac Sim 5.0), no real-robot validation
- **Citation quality note:** Peer-reviewed journal article — strongest provenance among the recent graduated-precedent additions (vs. Kang preprint, Sahoo workshop paper, Baxi preprint). Authors explicitly bound all claims to the cleaned simulation benchmark; no formal guarantees, no deployment claims. Safe to cite as a load-bearing domain precedent for three-regime runtime gating.

---

### 2. Core Contribution

- **Problem:** Vision–Language–Action (VLA) robot policies are overconfident under domain shift; blind trust causes collisions and task failure. Deployment needs reliable uncertainty estimates AND a workable runtime-assurance policy.
- **Solution:** A model-agnostic **uncertainty-calibrated safety-gating wrapper** (meta-controller / "mediator architecture") that estimates online failure risk r_t = 1 − p̂_succ(o_t, w) (temperature-scaled calibration) and routes control among **three regimes** via hysteresis thresholds 0 < δ_low < δ_high < 1 (operating point: δ_low = 0.2, δ_high = 0.5):
  - **Safe to proceed** (r_t < δ_low): execute the VLA policy action normally
  - **Borderline** (δ_low ≤ r_t < δ_high): pause and re-observe — feed a new camera frame from a slightly different viewpoint, re-estimate risk (cautious slowdown / re-sensing strategy)
  - **Unsafe to proceed** (r_t ≥ δ_high): disengage the learned policy entirely; hand control to a classical MoveIt 2 fallback planner (retreat to safe pose, re-orient for visibility, complete subtask via planner, recovery behaviours)
- **Results:** Under structured domain shifts (lighting, texture, occlusion, sensor, combined), calibrated gating improves mean shifted success 57.5% → 77.2% and aggregate ECE 0.303 → 0.100 vs. the ungated VLA. Key trade-off finding: an aggressive *uncalibrated* threshold baseline achieves better raw success/collision numbers but needs ~2× the interventions per shifted episode (21.6 vs. 11.5). Contribution framed as characterising the **reliability–intervention frontier**, not a universally best controller.
- **Explicitly no formal guarantees:** chance-constrained interpretation offered as rationale only; "calibration error is nonzero, contacts are history-dependent, and fallback is empirical rather than certified." 63.7% of residual collision contacts occur during pause/reobserve and 28.1% during fallback.

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | Yes | Learned VLA policy + deterministic gating logic + classical (non-AI) MoveIt 2 planner — explicit hybrid autonomy, deterministic guard around opaque AI component |
| Safety-critical AI decision-making | Yes | Physical manipulation safety (collisions, contact forces); runtime assurance framing |
| AI governance / control mechanisms | Yes | Three-regime runtime gate conditioned on calibrated failure risk — a graduated participation-gating instance |
| Low-resource environments | No | RTX 4080 GPU, 7B-parameter model, ensembles/MC-dropout, ROS 2 + MoveIt 2 stack |
| Decision architecture formalisation | Partial | Formal risk definition, calibration objective, threshold semantics; but no admissible sets, no proven properties — explicitly declines formal guarantees |
| Human role in decision-making | No | Fully autonomous loop; human assistance only mentioned as future work ("learning when to ask for help") |
| Socio-technical evaluation | No | Simulation benchmark only |
| Coastal fisheries / maritime domain | No | Robotic manipulation (drawer task, clutter sort) |

**Mid-Extraction Relevance Gate:** 3 Yes, 1 Partial → **FULL EXTRACTION** (targeted — gap-argument precedent)

---

### 4. Decision Architecture Analysis

- **Architecture:** Wrapper/meta-controller pattern: VLA policy runs in parallel with an uncertainty estimator (ensemble of 5 variants or MC dropout ×20; channels: confidence 1−c_t, entropy h_t, ensemble variance v_t → composite u_t) and a calibration map f_c (temperature scaling fitted on held-out episodes) producing r_t. A safety supervisor gates control authority per Algorithm 1. Model-agnostic: applied post hoc, no retraining of the base policy.
- **The three regimes — what actually changes:**
  - Safe: AI acts, full scope.
  - **Borderline: the AI's output scope is untouched.** The system alters *execution behaviour* — pause, slow down, gather a new observation, re-evaluate. It is a temporal/informational deferral strategy: the same full-scope policy is re-consulted with better input. Nothing about what the policy may output is restricted.
  - Unsafe: the AI is **replaced** by a non-AI classical planner — functionally G = 0 (cf. Flehmig red level's transfer to non-AI backup; Abella's supervision-function switch).
- **Consequence:** from the AI's perspective the gate is binary (execute vs. disengaged); the intermediate regime is a re-sensing loop, not a restricted operating mode. Three regimes of *system behaviour*, two modes of *AI participation*, zero graduation of *AI output scope*.
- **Failure modes / fallback:** fallback planner explicitly not certified — planning timeouts, incomplete collision scenes, stale perception; episodes still fail during pause and fallback states. Hysteresis (two thresholds) prevents mode chattering.

**Critical architectural comparison:**

| Aspect | Ghaleb et al. (2026) | My DSR architecture |
|---|---|---|
| **What is classified** | Calibrated runtime failure risk r_t of the AI policy (model uncertainty under domain shift) | Environmental state E = {w, r, m, o, v, t} |
| **Classification** | Continuous r_t ∈ [0,1], two hysteresis thresholds → three regimes | S = f(E) → three discrete states |
| **Conditioning variable** | AI-internal confidence (epistemic uncertainty) | World-side environmental danger, classified independently of the AI |
| **Intermediate mode** | Pause/re-observe — execution deferral + re-sensing; AI output scope unchanged | CAUTION — A_AI contracts to {Go, Delay}; AI stays engaged with restricted advisory scope |
| **Maximum-risk mode** | AI replaced by classical planner (binary handoff) | G = 0, A_AI = ∅ |
| **Governed object** | Physical execution behaviour of an acting robot | Advisory recommendation space facing a human decision-maker |
| **Formal property** | None claimed ("rationale but no formal proof") | Safety Dominance Property, proof by construction |

---

### 5. Formal Model and Mathematical Representation

- **Risk metric:** r_t := P̂_f(o_t, w) = 1 − p̂_succ(o_t, w), where p̂_succ = σ(z/T), z = logit of raw success estimate, T fitted by NLL minimisation on calibration set D_cal (temperature scaling; isotonic regression compared).
- **Gating rule (Algorithm 1):** r_t < δ_low → execute; δ_low ≤ r_t < δ_high → new observation, recompute; r_t ≥ δ_high → fallback controller → safe state. Hysteresis via two thresholds.
- **Threshold semantics:** calibration gives thresholds concrete probability meaning ("intervene if predicted success < 80%") — the paper's strongest formal virtue: governance thresholds with calibrated risk semantics rather than arbitrary scores.
- **Chance-constrained rationale only:** idealised union-bound argument (risk ≤ δ_high per step ⇒ ≤ δ_high·H over horizon) explicitly does NOT hold — nonzero calibration error, history-dependent contacts, uncertified fallback. No containment property, no admissible action sets, no proofs.
- **Contrast with my formalisation:** thresholds partition a *scalar risk estimate produced by the AI itself*; my f(E) classifies an *independently observed environmental vector*. Their gate output selects *who controls*; my governance pair selects *what may be recommended*.

---

### 6. Safety State Classification

- **Discrete levels:** Three regimes over a continuous calibrated risk score, with hysteresis. Structurally the closest surface match to SAFE/CAUTION/UNSAFE naming in the corpus — the labels are even semantically parallel ("Safe to proceed" / "Borderline" / "Unsafe to proceed").
- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:**
  - Both: three-level, threshold-based, conservative-by-design (calibrated risk; hysteresis stability). The hysteresis mechanism is independently useful — a precedent for preventing state chattering at classification boundaries in S = f(E) (worth citing in the state-classification design discussion).
  - Difference 1 — input: r_t is the AI's self-assessed (calibrated) failure probability; S is a classification of the external environment. An environment lethal to a fisher but visually familiar to the model would yield low r_t; the wrapper gates on model ignorance, not world danger.
  - Difference 2 — intermediate semantics: Borderline buys *information* (re-observe, re-estimate); CAUTION contracts *scope* (restricted recommendation set). Deferral vs. restriction.
- **AI recommendation scope across levels:** **No.** Scope is full at Safe and Borderline, and the AI is absent at Unsafe. No level provides restricted-scope AI participation.

---

### 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (G(S)) | Yes | Unsafe regime disengages the learned policy and hands control to the classical planner — functional G = 0. Binary from the AI's perspective |
| **Level 2 — Advisory scope governance** | What may AI recommend/do? (A_AI(S)) | **No** | Borderline alters execution behaviour (pause, slow, re-sense) while the policy's output space is unchanged; there is no restricted-scope operating mode and no advisory dimension at all |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified state? | No | The risk classification drives a participation/handoff decision plus an execution-strategy adjustment; scope is never a governed variable |

- **Governance type:** **Graduated-looking but binary-participation runtime assurance.** A three-regime wrapper whose intermediate regime is temporal-informational (defer + re-sense), not scope-restrictive; whose terminal regime is a binary AI→non-AI handoff.
- **Key evidence for my gap argument:** this is the robotics/runtime-assurance instantiation of the pattern. The corpus now shows three distinct designs of intermediate mode, none of which contracts a human-facing recommendation space: (a) intensify human oversight (Flehmig 2024; Kang 2026), (b) restrict autonomous action classes (Sahoo 2026), (c) defer and re-observe (Ghaleb et al. 2026). Physical/embodied domains handle marginal risk with physical-execution degradation — slowdown, re-sensing, handoff — because their AI *acts*. A decision-support AI *advises*; the analogous intermediate mechanism (contraction of the advisory menu) exists nowhere. Peer-reviewed 2026 evidence that the gap persists in the runtime assurance literature specifically.

---

### 8. Human Role in Decision-Making

- **Human role:** None in the loop. The supervisor, fallback, and recovery are fully autonomous. "Learning when to ask for help" (triggering human assistance instead of autonomous fallback) is listed as future work — i.e., even the human-escalation variant of the intermediate mode is unrealised.
- **Decision support vs. automation:** Pure automation. No recommendations, no operator. The absence of any advisory dimension is what makes the three-regime structure inapplicable to the departure decision problem without the architectural work my thesis contributes.

---

### 9. System Constraints and Environment

- **Real-world deployment:** None — Isaac Sim 5.0 only; authors explicitly disclaim real-robot transfer, deployment readiness, and safety certification. Staged physical validation outlined as future work.
- **Resources:** RTX 4080 GPU, OpenVLA-7B (~200 ms/step inference), 5-member ensembles or 20-pass MC dropout, ROS 2 + MoveIt 2 (0.5–1.0 s planning). High-compute stack — opposite of offline-first, computationally lightweight requirements (Katende).

---

### 10. Hybrid AI Taxonomy

- **Type:** **Runtime assurance / mediator architecture** (their own term): deterministic supervisory gate + learned policy + classical fallback. The "surround opaque AI with deterministic guards" pattern (Bloomfield & Rushby) implemented concretely.
- **Safety enforcement:** At decision time, per step, before action execution. Enforcement selects controller and execution strategy — never output content or scope.
- **Two-level governance support:** Level 1 only (binary, with a deferral buffer).

---

### 11. Baseline Comparison and Evaluation

- **Baselines:** Ungated VLA; aggressive uncalibrated threshold baseline; fallback-on-failure hybrid. Two long-horizon tasks (drawer-object; cluttered pick-and-sort) × five shift families, cleaned aggregation.
- **Evaluation:** Success rate, collision metrics, ECE/NLL/reliability diagrams, interventions per episode, runtime overhead, threshold sensitivity, per-channel uncertainty diagnostics, residual-failure phase analysis. Methodologically strong empirical protocol.
- **Directly relevant finding — the over-intervention cost:** the aggressive threshold baseline wins on raw safety metrics but doubles interventions (21.6 vs. 11.5/episode), degrading efficiency and discarding reliable AI behaviour. This is empirical evidence for the cost my RQ4 C2-vs-C3 comparison measures: binary/aggressive gating buys safety by over-blocking. Citable quantification that intervention burden is a first-class metric and that "two separate problems — (i) estimating risk accurately and (ii) mapping risk to the right intervention policy" — the second being exactly what (G(S), A_AI(S)) addresses for advisory systems.
- **CAUTION zone equivalent:** Borderline band — but deferral/re-sensing, not restricted-scope participation.
- **Safety Dominance verification:** N/A — no containment concept.

---

### 12. Key Concepts and Definitions

- **Safety gating / gating wrapper:** post hoc supervisory layer routing control among policy execution, pause-and-reobserve, and fallback planning based on calibrated risk.
- **Calibrated risk r_t:** 1 − temperature-scaled success probability; gives thresholds concrete failure-probability semantics.
- **Hysteresis thresholds (δ_low, δ_high):** two-threshold design creating a stable intermediate band and preventing mode chattering — transferable to S = f(E) boundary design.
- **Reliability–intervention frontier:** trade-off between predictive reliability/intervention economy and raw terminal success — the paper's central empirical object.
- **Mediator architecture:** supervisory layer monitoring a learned policy and intervening when necessary (their positioning of the pattern; cf. MCF, HG-DAgger, UNISafe).
- **Intervention burden as first-class metric:** interventions per episode reported alongside success/collisions — methodological precedent for RQ4 metrics.

---

### 13. Limitations and Unsolved Problems

- **Stated limitations:** simulation-only; visual shifts only (no dynamics shifts); assumes usable uncertainty signal; needs hundreds of calibration runs; fallback not formally verified; no formal guarantees (would require bounded calibration error, verified fallback, temporal dependence treatment); modality generalisation open.
- **Stated open problem:** "mapping calibrated risk into efficient intervention policies" — the field has risk estimation but not principled risk-to-action governance. My governance pair is a formal answer to this question for the advisory (non-acting) setting.
- **Alignment with my research gaps:**
  - No environmental-state conditioning — the gate reads the model's own uncertainty, not classified world danger.
  - No advisory scope concept — acting-robot paradigm.
  - No formal properties — explicitly declined.
  - High-resource stack — inapplicable to the low-resource deployment floor.

---

### 14. Methodology Notes

- **Method:** Controlled simulation benchmark with structured domain randomisation; four-method comparison; extensive diagnostics; unusually candid scope-of-evidence section (§6.5, §7.2) separating supported from unsupported claims.
- **DSR alignment:** Not DSR, but the four-method comparative evaluation under systematically varied conditions is a useful methodological reference for RQ4's three-condition design (ungated vs. binary-gated vs. graduated) — theirs is effectively ungated vs. two gating variants vs. hybrid, measured on success, safety, AND intervention burden.

---

### 15. Quotable / Citable Points

1. "We introduce two threshold parameters 0 < δ_low < δ_high < 1 to implement a simple hysteresis, enabling three regimes: Safe to proceed… Borderline… Unsafe to proceed." (§4.1) — the three-regime structure, for direct comparison.
2. Borderline definition: "Invoke a cautious slowdown or re-observation strategy… pausing and feeding the next camera frame (from a slightly different viewpoint) to π_θ to see if r_t changes." (§4.1) — the intermediate mode is re-sensing, not scope restriction; the exact quote for differentiation.
3. "Unsafe to proceed (r_t ≥ δ_high): Disengage the learned policy and hand control to the fallback controller." (§4.1) — binary AI participation at maximum risk.
4. "There are at least two separate problems in uncertainty-aware robot supervision: (i) estimating failure risk accurately and (ii) mapping that risk to the right intervention policy… the second problem remains open." (§7) — field-internal acknowledgement that risk-to-governance mapping is unsolved.
5. "An aggressive uncalibrated threshold baseline attains stronger raw success and collision metrics, but requires nearly twice as many interventions per shifted episode (21.6 vs. 11.5)." (Abstract) — empirical cost of over-aggressive gating; supports the RQ4 argument that governance design, not just blocking, matters.
6. "The real system does not satisfy the assumptions needed for a formal guarantee." (§4.3) — explicit absence of formal properties in the closest three-regime runtime-assurance precedent.

---

### 16. Relation to My Research and Positioning

- **Governance implementation:** Level 1 yes (binary disengagement at Unsafe); Level 2 no (Borderline is deferral, not scope contraction); no unified state-conditioned governance of scope.
- **State conditioning:** Fifth distinct conditioning variable across the graduated-precedent set — Baxi: AI robustness; Kang: task regulatory risk; Flehmig: AI degradation; Sahoo: control quality; **Ghaleb: calibrated AI failure risk**. All five condition on properties *of the AI system or its task*; none classifies the *external environment's danger to humans*. My S = f(E) remains the only environment-conditioned gate.
- **The intermediate-mode design space (key synthesis):** the corpus now documents three realised designs for the intermediate level — (a) intensified human oversight (Flehmig, Kang), (b) restricted autonomous action classes (Sahoo), (c) execution deferral + re-sensing (Ghaleb) — and one unrealised design: **contraction of a human-facing advisory space (mine)**. Embodied systems degrade *physically* at intermediate risk because their AI acts in the world; decision-support systems have no analogous mechanism in the literature. This taxonomy is a strong organising device for the gap-precedents discussion.
- **Convergent design elements to cite:** hysteresis thresholds for state-boundary stability; calibrated-risk semantics for thresholds; intervention burden as first-class evaluation metric (RQ4); deterministic-guard-around-opaque-AI implementation (Bloomfield & Rushby lineage); empirical demonstration that binary/aggressive gating over-intervenes (~2×) — the operational cost my CAUTION mode is designed to avoid.

**Positioning paragraph:** Ghaleb et al. (2026) implement a three-regime uncertainty-calibrated safety gate for vision–language–action robot manipulation: calibrated runtime failure risk routes control among policy execution ("Safe to proceed"), pause-and-reobserve ("Borderline"), and handoff to a classical non-AI planner ("Unsafe to proceed"). Despite the surface parallel to SAFE/CAUTION/UNSAFE, the intermediate regime alters physical execution behaviour — the system slows down, re-senses, and re-evaluates — while the AI's output scope is untouched, and the maximum-risk regime removes the AI entirely. The gate is conditioned on the model's own calibrated uncertainty, not on a classification of environmental danger, and the authors explicitly claim no formal guarantees. The paper strengthens the gap argument in two ways: it shows that in embodied runtime assurance, intermediate risk is handled by physical degradation (deferral, slowdown, re-observation) rather than advisory scope contraction — a mechanism only meaningful for acting systems, unavailable to decision support; and it names the open problem directly, observing that "mapping calibrated risk into efficient intervention policies" remains unsolved. Its empirical finding that aggressive binary-style thresholding doubles intervention burden (21.6 vs. 11.5 per episode) provides peer-reviewed quantification of the over-restriction cost that a graduated advisory architecture is designed to avoid. As a peer-reviewed 2026 journal article, it is safely citable as a load-bearing domain precedent.

---

### 17. Overall Relevance Score

**⭐⭐⭐ Moderate-High**

**Justification:** The runtime-assurance/robotics instantiation of the intermediate-mode pattern, completing a three-way design-space taxonomy (human-oversight intensification / action-class restriction / execution deferral) that sharpens the advisory scope gap. Peer-reviewed journal provenance makes it the most safely citable of the recent graduated-precedent additions. Adds two independently valuable design precedents (hysteresis thresholds; calibrated-risk threshold semantics) and RQ4-relevant empirical evidence on over-intervention costs of aggressive gating. Held at ⭐⭐⭐ because: simulation-only, acting-robot paradigm orthogonal to advisory decision support, no formal properties, high-resource stack, and its gap-confirming role is supplementary to the established shields/safety-filter line ([8], [10]) rather than opening a new argument layer.

---

### Recommended Citation Uses

| Use | Section in dissertation | Specific point |
|---|---|---|
| Intermediate-mode design-space taxonomy | Gap argument / precedents discussion | Third realised intermediate design (defer + re-sense) alongside Flehmig/Kang (human oversight) and Sahoo (action classes) — none contracts an advisory space |
| Three-regime surface parallel, differentiated | Related work comparison | "Safe/Borderline/Unsafe" naming parallel to SAFE/CAUTION/UNSAFE; conditioned on model uncertainty not environmental state; Borderline = re-sensing, not scope restriction; Unsafe = binary AI removal |
| Over-intervention cost of aggressive gating | RQ4 evaluation design / discussion | Aggressive thresholding ≈ 2× interventions (21.6 vs. 11.5/episode) for marginal raw gains — empirical cost of non-graduated gating |
| Hysteresis threshold design | S = f(E) classification design | Two-threshold hysteresis prevents state chattering at boundaries — directly transferable to safety-state transition stability |
| Risk-to-intervention as open problem | Gap argument / conclusion | Field-internal statement that mapping calibrated risk to intervention policy is unsolved — (G(S), A_AI(S)) is a formal answer for the advisory setting |
| Deterministic guard around opaque AI | Architecture justification (supporting) | Concrete implemented instance of the Bloomfield & Rushby dependability pattern |
