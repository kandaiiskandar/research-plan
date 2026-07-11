## Literature Review Extraction: Kang (2026)

---

### 1. Paper Identity

- **Title:** Governed AI-Assisted Engineering: Graduated Human Oversight for Agentic Code Generation in Regulated Domains
- **Authors:** Richard Kang (DoiT International)
- **Year:** 2026 (arXiv v2, 4 July 2026)
- **Venue:** arXiv preprint (arXiv:2606.22484v2, cs.HC)
- **DOI:** none — arXiv eprint only (**not peer-reviewed**)
- **Type:** Framework/architecture paper with formal classification model; analytical evaluation only (no deployment data)
- **⚠️ Citation quality note:** arXiv preprint by a single industry author (DoiT International); no peer review, no empirical validation (expert validation with 5–8 practitioners is stated as *pending*, limitation L4). Regulatory mappings are the author's own analysis, explicitly not validated by any regulator. **Recommended use:** supplementary precedent in the gap argument (alongside Flehmig et al. 2024) showing that "graduated" governance in yet another domain means graduated *human oversight*, not graduated *AI advisory scope*. Cite as "Kang, 2026, preprint". Not load-bearing.

---

### 2. Core Contribution

- **Problem:** Agentic AI coding systems in regulated industries (banking, insurance, healthcare) face a "Productivity-Reliability Paradox": uniform human review of everything collapses velocity; reviewing nothing violates regulatory human-oversight expectations. Existing frameworks offer no mechanism for calibrating oversight intensity to regulatory impact.
- **Solution:** The Governed AI-Assisted Engineering (GAIE) framework — a **three-tier graduated human oversight model** for agentic code generation. Its core is the Oversight Classification Model (OCM), a deterministic total function OCM : T → {Tier1, Tier2, Tier3} that classifies each code generation task by a four-dimensional risk vector φ(t) = (RI, CP, RV, DS) (regulatory impact, customer proximity, reversibility, data sensitivity) and routes it to one of three oversight pathways:
  - **Tier 1 — Human-in-the-Loop (HITL):** strategic functions; agent halts (RETURN_CONTROL), human approves approach before generation and signs deployment
  - **Tier 2 — Human-over-the-Loop (HOTL):** customer-impacting; agent generates and tests autonomously, human approves deployment only
  - **Tier 3 — Automated with Monitoring (AWM):** internal tooling; fully autonomous pipeline with post-deployment monitoring and exception escalation
- **Main contributions:** GAIE framework; OCM with three properties established by construction (monotonicity, fail-safety under correct/uncertain metadata, totality); per-tier evidence artifact model (cryptographically-linked audit chain); regulatory traceability mapping (Bank of Thailand 2025 policy, plus MAS FEAT, NIST AI RMF, ISO/IEC 42001, EU AI Act); analytical productivity model (84–97% velocity preservation, central estimate 91%, vs. 45–65% under uniform HITL).
- **Gap claim:** "No existing work combines: (a) graduated human oversight, (b) calibrated to regulatory impact classification, (c) for agentic code generation specifically, (d) with per-tier evidence artifacts, (e) validated against real regulatory frameworks."

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | Partial | OCM is a deterministic rule engine governing probabilistic coding agents — governance layer + AI pattern (as in Baxi 2026), not integrated hybrid reasoning |
| Safety-critical AI decision-making | Partial | Regulated-domain consequence severity (financial/compliance), not physical safety. Explicitly invokes SAE J3016, aviation, clinical, nuclear graduated-autonomy precedents |
| AI governance / control mechanisms | Yes | Core contribution — deterministic state-conditioned routing of AI work through oversight tiers with formal properties |
| Low-resource environments | No | Enterprise CI/CD infrastructure, cloud services, cryptographic evidence stores |
| Decision architecture formalisation | Yes | OCM total function, four-dimension risk feature space, three theorems (monotonicity, fail-safety, totality), fail-safe default |
| Human role in decision-making | Yes | The entire graduation IS the human role: review-before-generation → approve-deploy-only → exception-based escalation |
| Socio-technical evaluation | No | Analytical evaluation only; practitioner validation pending |
| Coastal fisheries / maritime domain | No | Software engineering in regulated financial institutions |

**Mid-Extraction Relevance Gate:** 3 Yes, 3 Partial → **FULL EXTRACTION**

---

### 4. Decision Architecture Analysis

- **Architecture:** Governance layer between task intake and code deployment. Five design principles: P1 proportionality, P2 evidence-by-design, P3 fail-safe default (uncertain classification escalates to a *higher* tier, never lower), P4 separation of generation and approval (generating agent cannot approve its own deployment), P5 regulatory defensibility.
- **Classification:** OCM evaluates φ(t) = (RI, CP, RV, DS) through priority-ordered rules: RI = strategic → Tier 1; CP = direct → Tier 2; CP = indirect ∧ (DS = personal ∨ RV = irreversible) → Tier 2; confidence < θ → Tier 1 (fail-safe); dependency-graph path to a strategic function → Tier 1 (direct) or Tier 2 (transitive); else Tier 3.
- **What varies across tiers:** human gate placement (before generation + at deploy / at deploy only / none), evidence artifacts required, monitoring intensity, and approval signatures. **What does NOT vary: the agent's generative scope.** In all three tiers the agent produces full-scope output (complete code, tests, deployment artifacts); the tiers change when a human looks at it and what evidence is captured.
- **Failure modes / fallback:** fail-safe escalation on low classification confidence; tier reclassification lifecycle (downward requires ≥20 consecutive clean deployments + compliance approval; upward triggers immediately on anomaly, regulatory change, scope expansion, security incident, or new strategic dependency). Threat model with four categories (classification evasion, evidence tampering, governance fatigue, registry staleness).

**Critical architectural comparison:**

| Aspect | Kang (2026) GAIE | My DSR architecture |
|---|---|---|
| **What is classified** | Code generation task risk φ(t) = (RI, CP, RV, DS) | Environmental state E = {w, r, m, o, v, t} |
| **Classification function** | OCM : T → {Tier1, Tier2, Tier3} (deterministic, total) | S = f(E) → {SAFE, CAUTION, UNSAFE} |
| **Conditioning variable** | Static per-task metadata (regulatory impact of the artifact) | Dynamic environmental safety state |
| **What the tiers govern** | Human oversight intensity + evidence artifacts | AI participation G(S) AND AI advisory scope A_AI(S) |
| **AI output at intermediate tier** | Unchanged — full-scope generation, human approves deploy | Restricted — A_AI(CAUTION) = {Go, Delay} |
| **AI at maximum risk tier** | Still generates full scope; human gates approach + deployment | Disabled: G(UNSAFE) = 0, A_AI = ∅ |
| **Worst-case principle** | Fail-safe default: uncertainty → higher tier | Worst environmental component determines S |

---

### 5. Formal Model and Mathematical Representation

- **OCM:** total function OCM : T → {Tier1, Tier2, Tier3} over the set T of all code generation tasks
- **Risk feature space:** φ(t) = (RI(t), CP(t), RV(t), DS(t)); RI ∈ {strategic, non-strategic}, CP ∈ {direct, indirect, internal}, RV ∈ {irreversible, partial, full}, DS ∈ {personal, business, public}
- **Confidence threshold:** c < θ ⇒ Tier 1 (fail-safe escalation)
- **Theorem 1 (Monotonicity):** increasing any risk dimension never decreases the assigned tier; if φ(t1) ≤ φ(t2) component-wise then OCM(t1) ≤ OCM(t2)
- **Theorem 2 (Fail-safety):** under correct or uncertain metadata, OCM does not under-classify. Residual risk: *confident but incorrect* metadata can cause misclassification (limitation L6)
- **Theorem 3 (Totality):** every task receives exactly one tier assignment; deterministic
- **Properties are "established by construction"** via priority-ordered classification rules — same enforcement style as my Layer 3 rule-set construction (RS(S)), though what is enforced differs fundamentally (oversight routing vs. admissible recommendation space)
- **No Safety Dominance analogue:** there is no containment relation over AI output sets. Tiers are not nested permission sets for the AI; they are alternative human-workflow pathways. Nothing in GAIE contracts what the agent may generate.

---

### 6. Safety State Classification

- **Discrete levels:** Yes — three tiers via deterministic classification of a four-dimensional risk vector, with explicit fail-safe (conservative) default.
- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:**
  - Both use a deterministic classifier mapping a multi-dimensional vector to exactly one of three discrete governance levels
  - Both apply a conservative principle (fail-safe escalation ≈ worst-case component determination)
  - GAIE classifies the *task artifact's regulatory risk* (essentially static per task); my architecture classifies *dynamic environmental danger* re-evaluated in real time
- **AI recommendation scope across levels:** **No.** The agent's generative/advisory scope is identical at every tier. Graduation calibrates human oversight intensity, evidence requirements, and monitoring — never what the AI is permitted to propose.

---

### 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (G(S)) | Partial | No tier disables the agent. Even Tier 1 lets the agent generate full-scope output once the human approves the approach. There is no G = 0 analogue — no state in which the AI is removed from the loop |
| **Level 2 — Advisory scope governance** | What may AI recommend/generate? (A_AI(S)) | **No** | Generative scope is identical across all three tiers. Tiers vary human gates, evidence artifacts, and monitoring — not the admissible output space |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified state? | No | Classification conditions *human workflow routing*, not AI participation or scope |

- **Governance type:** **Graduated, risk-classified human oversight governance.** Structurally the same pattern as Flehmig et al. (2024): a multi-level classified index whose intermediate level intensifies human supervisory involvement while leaving AI output semantically unchanged.
- **Key evidence for my gap argument:** GAIE is a 2026 framework, explicitly built on graduated-autonomy precedents (SAE J3016, Parasuraman, clinical staged autonomy, NUREG), with a formal deterministic classifier and three proven properties — and it *still* does not restrict AI output scope at any tier. In the software-engineering/regulated-administrative domain, as in Flehmig's industrial domain, "graduated" means graduated human workload and auditability, not graduated AI semantic constraints. The advisory scope gap persists in yet another body of literature.

---

### 8. Human Role in Decision-Making

- **Human role is the graduated variable itself:** Tier 1 — human reviews/modifies approach before generation and signs deployment; Tier 2 — human approves deployment only; Tier 3 — human absent except on monitoring anomaly escalation.
- **Decision support vs. automation:** Automation governance. The AI is the producer (of code); the human is the approver. In my architecture the AI is the advisor and the human is the decision-maker — the authority relationship is inverted.
- **Governance fatigue** acknowledged as a threat (T3): review-duration tracking and modification-rate monitoring mitigate rubber-stamping, but "cannot force cognitive engagement" — relevant to my RQ5 discussion on calibrated reliance.

---

### 9. System Constraints and Environment

- **Real-world deployment:** None. Analytical evaluation only (regulatory coverage analysis, comparative framework analysis, productivity modeling). Reference implementation architecture described but not deployed. Empirical validation is future work.
- **Environment:** Enterprise regulated financial institutions; requires CI/CD infrastructure, dependency graphs, regulatory function registry, append-only cryptographic evidence store. Antithesis of low-resource deployment.

---

### 10. Hybrid AI Taxonomy

- **Type:** **Constitutional / governance-based.** Deterministic rule engine (OCM + classification rules) wrapped around probabilistic coding agents. Multi-agent supervisor pattern with separation of generation and validation (author ≠ tester).
- **Safety enforcement:** Before AI acts (Tier 1 halts pre-generation) and after (deploy gates, monitoring) — but enforcement targets *process checkpoints*, never *output content or scope*.
- **Two-level governance support:** None for Level 2. Graduation exists but governs the human side of the loop exclusively.

---

### 11. Baseline Comparison and Evaluation

- **Baselines (comparative analysis, Table IX):** ACMM maturity model, Farrag's specification-driven governance, Atlassian HITL agents (uniform oversight), Zabolotnii clinical staged autonomy, SAE J3016.
- **Evaluation:** (1) regulatory coverage: traceability to 17/17 applicable BOT control requirements — author's own reading, explicitly "not a compliance determination"; (2) comparative framework analysis; (3) analytical productivity model: 84–97% velocity preservation (central 91%) vs. ~55% uniform HITL. All analytical, no empirical data.
- **CAUTION zone equivalent:** Tier 2 (HOTL) is the intermediate level — but it is intermediate in *human involvement* (approve deploy only), not in AI output scope. Exactly parallel to Flehmig's Orange level.
- **Safety Dominance verification:** N/A — no output containment property exists to verify.

---

### 12. Key Concepts and Definitions

- **GAIE:** governance layer routing code generation tasks through proportionate oversight tiers based on regulatory risk classification.
- **OCM:** deterministic total function classifying tasks by (RI, CP, RV, DS) into three oversight tiers.
- **HITL / HOTL / AWM:** human-in-the-loop (pre-generation + deploy gates), human-over-the-loop (deploy gate only), automated-with-monitoring (exception escalation only).
- **Fail-safe default (P3):** classification uncertainty escalates to a higher tier, never lower.
- **Evidence-by-design (P2):** every oversight event automatically produces audit artifacts in a cryptographically-linked, append-only chain.
- **Productivity-Reliability Paradox (from Farrag):** uniform governance consumes agentic velocity; Kang's resolution — "the paradox is an artifact of uniform governance applied to heterogeneous risk."
- **Tier reclassification lifecycle:** downward slow and evidence-gated (≥20 clean deploys, <5% rejection, compliance approval); upward immediate on any risk trigger — asymmetric conservatism.

---

### 13. Limitations and Unsolved Problems

- **Stated limitations (L1–L7):** single-jurisdiction primary mapping; no production deployment data; classification boundary ambiguity at edges; expert validation pending; technology coupling in reference architecture; confident-but-incorrect metadata as failure mode; regulatory mappings not externally validated.
- **Alignment with my research gaps:**
  - **No advisory scope governance:** GAIE never asks "what should the AI be permitted to generate given the risk level?" — only "who must look at it and when?" The admissible output space is constant across tiers.
  - **Static conditioning:** classification derives from task metadata and dependency graphs, not from a dynamically sensed operational environment. No analogue of real-time S = f(E) re-evaluation.
  - **No participation disablement:** no tier removes the AI. The maximum-risk response is more human gates, not G = 0.

---

### 14. Methodology Notes

- **Method:** Framework design + formal classification model (properties by construction) + multi-method analytical evaluation (regulatory coverage, comparative analysis, sensitivity-analysed productivity model). Practitioner validation instrument designed (Appendix B) but not yet executed.
- **DSR alignment:** Framework-design paper without empirical iteration; closer to conceptual DSR artifact than to my build-and-evaluate cycle.

---

### 15. Quotable / Citable Points

1. "No existing work combines: (a) graduated human oversight, (b) calibrated to regulatory impact classification, (c) for agentic code generation specifically, (d) with per-tier evidence artifacts, (e) validated against real regulatory frameworks." (§II.H) — gap statement confirming graduated *oversight* is itself novel in SE; graduated *AI scope* is not even on the map.
2. "Not 'should agents code autonomously?' but 'what level of oversight is appropriate for this code's regulatory context?'" (§I.D) — the graduation question posed entirely in terms of oversight, never output scope.
3. "P3. Fail-safe default. When classification is uncertain, the OCM escalates to a higher oversight tier, never a lower one." (§III.B) — independent motivation for conservative worst-case classification.
4. "Our work observes that the paradox is an artifact of uniform governance applied to heterogeneous risk." (§II.D) — the case for graduation over uniform/binary governance.
5. "These domains share: oversight intensity should be proportionate to consequence severity." (§II.E, citing SAE J3016, Parasuraman, clinical, nuclear) — proportionality framed exclusively as *oversight* intensity across all cited graduated-autonomy precedents.

---

### 16. Relation to My Research and Positioning

- **Governance implementation:** Level 1 partial (no disablement state), Level 2 absent. Graduation calibrates human oversight intensity and auditability requirements only.
- **State conditioning:** Task-risk-conditioned (static regulatory metadata), not environment-conditioned. Third distinct conditioning variable in the corpus: Baxi gates on *AI robustness*, Kang gates on *task regulatory risk*, my architecture gates on *environmental safety state*.
- **Structural role in the gap argument:** GAIE is a **domain-transposed Flehmig**. Both build a three-level classified index with a formally specified intermediate level; both use the intermediate level to change what *humans* do (intensified checks / deploy-approval gates); both leave AI output identical across all levels where AI operates. Where Flehmig et al. (2024) show this in industrial safety-critical operation, Kang shows it in regulated software engineering — extending the gap's confirmed footprint into administrative/SE AI governance, and doing so with a formal deterministic classifier and monotonicity/fail-safety/totality properties. That formal rigour makes the absence sharper: even when graduated governance is fully formalised, the graduated variable chosen is human oversight, not AI advisory scope.
- **Convergent design principles worth noting:** deterministic classification function to discrete governance levels; fail-safe/worst-case defaults; properties by construction; asymmetric reclassification (fast escalation, slow relaxation). These independently validate design choices in my architecture while governing an entirely different variable.

**Positioning paragraph:** Kang (2026, preprint) proposes GAIE, a three-tier graduated human oversight framework for agentic code generation in regulated domains, built on a deterministic Oversight Classification Model with monotonicity, fail-safety, and totality properties established by construction. Like Flehmig et al.'s traffic-light degradation index, GAIE demonstrates that when the literature graduates governance across an intermediate level, the graduated variable is human oversight intensity and evidence/auditability requirements — the AI's generative scope is identical at every tier, and no tier disables the AI. GAIE thus extends the advisory scope gap's confirmed footprint from industrial safety-critical operation (Flehmig) into regulated software-engineering governance: even a 2026 framework that formalises graduation end-to-end, and explicitly grounds itself in the graduated-autonomy tradition (SAE J3016, aviation, clinical, nuclear), does not condition what the AI may generate on the classified risk level. **Citation caveat:** arXiv preprint, single industry author, analytical evaluation only, regulatory mappings not externally validated — cite as supplementary gap-confirming precedent (e.g., "Kang, 2026, preprint"), not as a load-bearing reference.

---

### 17. Overall Relevance Score

**⭐⭐⭐ Moderate-High**

**Justification:** Direct structural reinforcement of the gap argument: a second, independent, formally specified three-level graduated governance framework (after Flehmig et al. 2024) whose intermediate level governs human oversight rather than AI advisory scope — in a new domain (regulated SE) and with stronger formalisation (deterministic total classifier, three properties by construction). Also provides convergent independent motivation for fail-safe/worst-case classification and properties-by-construction enforcement. Capped at ⭐⭐⭐ because: not peer-reviewed (arXiv preprint, single industry author), no empirical validation, wrong domain (enterprise SE vs. low-resource physical safety), and its governance target (human workflow routing) makes it a contrast case rather than a formal parallel to (G(S), A_AI(S)). Use in the gap/precedents discussion alongside Flehmig; not in Chapter 2 core corpus unless the gap argument section is being strengthened.

---

### Recommended Citation Uses

| Use | Section in dissertation | Specific point |
|---|---|---|
| Gap confirmation in a new domain | Gap argument / precedents discussion | Second independent three-level graduated framework where intermediate level governs human oversight, not AI scope — gap persists in SE/administrative AI governance |
| Flehmig parallel | Related work comparison | GAIE Tier 2 (HOTL) ≈ Flehmig Orange: intermediate level changes human behaviour, AI output unchanged |
| Fail-safe default precedent | Architecture design rationale | P3 (uncertainty → higher tier, never lower) independently motivates conservative worst-case state classification |
| Properties by construction | Formalisation chapter (supporting) | OCM monotonicity/fail-safety/totality by construction parallels my RS(S) rule-set enforcement style — different governed variable |
| Third conditioning variable | Research positioning | Baxi gates on AI robustness, Kang on task regulatory risk, mine on environmental state — graduated governance literature never conditions AI *scope* on any of them |
