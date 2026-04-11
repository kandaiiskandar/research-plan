---
layout: document
---

# Chapter 2: Literature Review — Writing Plan

**Dissertation**: A Graduated Safety-State-Gated Architecture for AI Decision Support in Low-Resource Environments  
**Output file**: `docs/chapter-2-draft.md` (written section by section)  
**Status**: Planning phase — not yet started

---

## Writing Rules

- Synthesised prose — mechanisms and patterns, not paper-by-paper summaries
- 4-paragraph structure per section: **What exists → How it works → Limitation → Gap transition**
- APA 7th edition in-text citations: (Author, Year) or Author (Year)
- Every cited paper includes a `[[notes]]` link immediately after the citation for traceability
- No new arguments — only what is already justified in the source documents
- No repetition across sections — each section hands off cleanly to the next

**Style guide** (`docs/writing-skill.md`):
- One idea per sentence — split long sentences
- Simple and precise words — avoid complex or inflated phrasing
- Clear subject → verb → object structure
- Logical flow: old → new information within each sentence
- Light reasoning signals: *because*, *this means*, *this shows*
- Avoid AI-like patterns: no repetitive transitions (*Furthermore*, *Moreover*), no over-smoothed parallel structure
- After drafting each section: apply the writing-skill as editor (not rewriter) — preserve meaning and tone, improve clarity only

---

## Section Plan

---

### 2.1 AI Decision Support in Safety-Critical Systems

**Argument**: AI decision support is widely deployed and beneficial — but incorrect AI recommendations in safety-critical contexts create a governance problem that accuracy improvements alone cannot solve.

| Paragraph | Content | Key papers |
|---|---|---|
| 1 — Context | AI used across maritime, aviation, healthcare, industry; advisory role; predictions, risk assessments, recommendations | Perez-Cerrolaza et al. (2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md); Ramos et al. (2024) [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md); Bengio et al. (2026) [[notes]](../notes/International%20AI%20Safety%20Report%202026.md) |
| 2 — Benefits | Improves decision quality; reduces cognitive load; handles data complexity; enhances situational awareness | Bloomfield & Rushby (2025) [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md); Ramos et al. (2024) [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md); Bengio et al. (2024) [[notes]](../notes/Managing%20extreme%20AI%20risks%20amid%20rapid%20progress.md) |
| 3 — Problem | Incorrect recommendations anchor decisions; automation bias; over-reliance; distributional shift degrades reliability; corrective feedback and transparency alone do not fix over-reliance — transparency increases agree-bias | Wen et al. (2025) [[notes]](../notes/Risk%20Perception%20in%20Complex%20Systems-%20A%20Comparative%20Analysis%20of%20Process%20Control%20and%20Autonomous%20Vehicle%20Failures.md); Newcomb & Ochoa (2026) [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md); Bloomfield & Rushby (2025) [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md); Tatasciore & Loft (2025) [[notes]](../notes/Calibrating%20Reliance%20on%20Automated%20Advice-%20Transparency%20and%20Trust%20Calibration%20Feedback.md) |
| 4 — Gap transition | Research focuses on accuracy and explainability; missing: governing AI participation and advisory scope as a function of operational conditions | Perez-Cerrolaza et al. (2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md); Newcomb & Ochoa (2026) [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md) |

**Source files**: `literature-review-writing-plan.md` §2.1 · `review-plan.md` §2.1 + Links 1–2 · `justification-ai-necessity.md`  
**Transition**: *"AI decision support improves decisions — but as AI moves into safety-critical environments, the question of how to constrain AI behaviour becomes critical. The first response in the literature has been deterministic safety constraints."*

---

### 2.2 Deterministic Safety Constraints and Safety Gating

**Argument**: Safety constraints govern whether AI acts — but all existing mechanisms are binary and do not restrict what AI is allowed to recommend.

| Paragraph | Content | Key papers |
|---|---|---|
| 1 — What exists | Rule-based safety systems; runtime verification; safety filters; safety shields; probabilistic shields; adaptive shields | Könighofer et al. (2025) [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md); Dalrymple et al. (2024) [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md); Bajcsy & Fisac (2024) [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md); Hamel-De le Court et al. (2025) [[notes]](../notes/Probabilistic%20Shielding%20for%20Safe%20Reinforcement%20Learning.md); Kwon et al. (2025) [[notes]](../notes/Runtime%20Safety%20through%20Adaptive%20Shielding-%20From%20Hidden%20Parameter%20Inference%20to%20Provable%20Guarantees.md) |
| 2 — Mechanism | Binary gate: allow or block; prevent unsafe actions; switch to fallback; formal safety guarantees; probabilistic shield via state-augmented MDP (Hamel-De le Court: Theorems 1–2); adaptive shield with environment-centric features and ACP uncertainty margin (Kwon: Theorem 1); per-action semantic suppression; constrained output generation via grammar intersection; IoT binary classifier φ(X(t)) ∈ {0,1} from multivariate sensor input (Zhang: Eq. 4) | Corsi et al. (2024) [[notes]](../notes/Verification-Guided%20Shielding%20for%20Deep%20Reinforcement%20Learning.md); Abella et al. (2025) [[notes]](../notes/SAFEXPLAIN-%20a%20Complete%20Approach%20Towards%20Trustworthy%20AI-Based%20Safety-Critical%20Systems.md); Vermaelen & Holvoet (2025) [[notes]](../notes/umato%202.0%20%E2%80%94%20A%20Constraint-Based%20Planning%20Approach%20for%20Safe%20and%20Robust%20Robot%20Behavior.md); Seong, Lim & Yoon (2025) [[notes]](../notes/clguard-extraction.md); Banerjee et al. (2025) [[notes]](../notes/CRANE-%20Reasoning%20with%20Constrained%20LLM%20Generation.md); Hamel-De le Court et al. (2025) [[notes]](../notes/Probabilistic%20Shielding%20for%20Safe%20Reinforcement%20Learning.md); Kwon et al. (2025) [[notes]](../notes/Runtime%20Safety%20through%20Adaptive%20Shielding-%20From%20Hidden%20Parameter%20Inference%20to%20Provable%20Guarantees.md); Zhang et al. (2025) [[notes]](../notes/Developing%20real-time%20IoT-based%20public%20safety%20alert%20and%20emergency%20response%20systems.md) |
| 3 — Limitation | Binary governance is universal — confirmed across 91 papers, 46 formal methods studies, 11 international frameworks; no intermediate state; no advisory scope restriction; even the most environment-aware adaptive shield (Kwon et al.) uses E ∈ ℝ^n₂ to modulate a continuous safety boundary, not to classify into discrete governance modes; Zhang et al. Eq. 4 reduces rich heterogeneous sensor input to a single binary threshold; CRANE formally proves binary output constraint reduces LLM capability to TC⁰ (Proposition 3.1) — strongest theoretical motivation for why binary is suboptimal | Ramos et al. (2024) [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md); Newcomb & Ochoa (2026) [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md); Bengio et al. (2026) [[notes]](../notes/International%20AI%20Safety%20Report%202026.md); Odriozola-Olalde et al. (2023) [[notes]](../notes/Shielded%20Reinforcement%20Learning-%20A%20review%20of%20reactive%20methods%20for%20safe%20learning.md); Banerjee et al. (2025) [[notes]](../notes/CRANE-%20Reasoning%20with%20Constrained%20LLM%20Generation.md); Kwon et al. (2025) [[notes]](../notes/Runtime%20Safety%20through%20Adaptive%20Shielding-%20From%20Hidden%20Parameter%20Inference%20to%20Provable%20Guarantees.md); Zhang et al. (2025) [[notes]](../notes/Developing%20real-time%20IoT-based%20public%20safety%20alert%20and%20emergency%20response%20systems.md) |
| 4 — Gap transition | Safety constraints govern participation only (Level 1); do not control what AI recommends (Level 2); decision authority allocation is a separate, unresolved question | Perez-Cerrolaza et al. (2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) |

**Source files**: `literature-review-writing-plan.md` §2.2 · `review-plan.md` §2.2 + Link 3 · `justification-novelty-gap.md`  
**Transition**: *"Safety constraints govern whether AI acts — but they do not govern what AI is allowed to recommend, or when AI should participate based on conditions. This raises a deeper question: how should decision authority be allocated between human and AI?"*

---

### 2.3 Human–AI Decision Authority

**Argument**: Human-AI authority frameworks define who decides — but do not specify when AI should participate based on safety conditions, or restrict what AI produces.

| Paragraph | Content | Key papers |
|---|---|---|
| 1 — Concept | Human-in-the-loop; human-on-the-loop; levels of automation; supervisory control; levels of autonomy for AI agents | Ramos et al. (2024) [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md); Porter et al. (2025) [[notes]](../notes/INSYTE-%20A%20Classification%20Framework%20for%20Traditional%20to%20Agentic%20AI%20Systems.md); Bach et al. (2024) [[notes]](../notes/Unpacking%20Human-AI%20Interaction%20in%20Safety-Critical%20Industries-%20A%20Systematic%20Literature%20Review.md); Feng et al. (2025) [[notes]](../notes/Levels%20of%20Autonomy%20for%20AI%20Agents.md) |
| 2 — Mechanism | Decision authority shifts between human and AI; AI suggests, human decides; authority varies by context and task; Feng et al. distinguish agency (what tools AI can access) from autonomy (how much human involvement required) — five discrete levels (L1 Operator → L5 Observer) with graduated human roles; autonomy certificates as digital governance artefacts | Saup et al. (2026) [[notes]](../notes/From%20pilots%20to%20decision%20systems-%20embedding%20generative%20AI%20into%20strategic%20decision-making%20through%20a%20socio-technical%20and%20governance%20lens.md); Madsen & Kim (2024) [[notes]](../notes/A%20state-of-the-art%20review%20of%20AI%20decision%20transparency%20for%20autonomous%20shipping.md); Leppinen et al. (2026) [[notes]](../notes/A%20Stage-Gate%20Decision%20Process%20for%20Guiding%20the%20Development%20of%20AI%20Solutions%20for%20Preventive%20Maintenance.md); Feng et al. (2025) [[notes]](../notes/Levels%20of%20Autonomy%20for%20AI%20Agents.md) |
| 3 — Limitation | Controls who decides; does not control what AI recommends; AI outputs remain unchanged across risk levels; authority allocation is static, not runtime-adaptive; Feng et al. reveal three critical limitations: (a) autonomy levels are **design-time** constants fixed at deployment — changing level requires certificate renewal, not automatic state-triggered transition; (b) agency and autonomy are two governance levers but **advisory scope** (what types of recommendations AI may generate) is a missing third lever; (c) environment is treated as constant "deployment context", not variable E triggering S = f(E) | Porter et al. (2025) [[notes]](../notes/INSYTE-%20A%20Classification%20Framework%20for%20Traditional%20to%20Agentic%20AI%20Systems.md); Ramos et al. (2024) [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md); Feng et al. (2025) [[notes]](../notes/Levels%20of%20Autonomy%20for%20AI%20Agents.md) |
| 4 — Gap transition | No structured control over AI advisory content; risk level does not change what AI is permitted to recommend; need advisory scope governance independent of authority allocation; Feng et al.'s design-time vs runtime distinction motivates the next question: can systems adapt governance at runtime? | Madsen & Kim (2024) [[notes]](../notes/A%20state-of-the-art%20review%20of%20AI%20decision%20transparency%20for%20autonomous%20shipping.md); Feng et al. (2025) [[notes]](../notes/Levels%20of%20Autonomy%20for%20AI%20Agents.md) |

**Source files**: `literature-review-writing-plan.md` §2.3 · `review-plan.md` §2.3 + Link 3 cont. · `justification-unified-governance.md`  
**Transition**: *"If static authority allocation is insufficient, the natural next step is systems that adapt the level of autonomy or AI participation based on risk at runtime."*

---

### 2.4 Adaptive Autonomy and Risk-Based Systems

**Argument**: Risk-adaptive systems change autonomy level — but govern monitoring intensity or operational domain, not AI advisory scope. No architecture formally restricts what AI is allowed to recommend based on classified environmental state.

| Paragraph | Content | Key papers |
|---|---|---|
| 1 — What exists | Adaptive autonomy; risk-aware systems; degraded modes; traffic-light governance; adaptive shielding with environment-centric features | Flehmig et al. (2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md); Gyllenhammar et al. (2025) [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md); Baxi (2026) [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md); Kwon et al. (2025) [[notes]](../notes/Runtime%20Safety%20through%20Adaptive%20Shielding-%20From%20Hidden%20Parameter%20Inference%20to%20Provable%20Guarantees.md) |
| 2 — Mechanism | Behaviour changes based on risk; switches between modes; Flehmig: traffic-light index from performance metrics; Baxi: K-tier graduated permissions with containment; **Kwon et al.: closest near-miss** — adaptive shield with environment-centric features E ∈ ℝ^n₂ (gravity, damping, mass, friction) + online hidden-parameter inference via function encoder + ACP uncertainty margin Γ_t; adapts safety boundary at runtime based on inferred environmental parameters; formal guarantee (Theorem 1: average cost rate ξ^π ≤ δ + ε̄(1−δ)); CRANE: augmented grammar G_a = R_M·G alternates unconstrained reasoning + constrained output — structural precursor to graduated scope but syntactically-triggered, not state-conditioned | Flehmig et al. (2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md); Baxi (2026) [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md); Li et al. (2026) [[notes]](../notes/Safety-Enhanced%20Deep%20Reinforcement%20Learning%20for%20Autonomous%20Driving-%20Dare%20to%20Make%20Mistakes%20to%20Learn%20Better%20and%20Faster.md); Banerjee et al. (2025) [[notes]](../notes/CRANE-%20Reasoning%20with%20Constrained%20LLM%20Generation.md); Kwon et al. (2025) [[notes]](../notes/Runtime%20Safety%20through%20Adaptive%20Shielding-%20From%20Hidden%20Parameter%20Inference%20to%20Provable%20Guarantees.md) |
| 3 — Limitation | Changes monitoring intensity or control authority — not advisory scope; AI still produces same recommendation types across modes; no formal containment of recommendation types; **Kwon et al. gap**: adapts quantitatively (tightens ACP threshold Γ_t as environment becomes more dangerous) but not qualitatively (no discrete governance modes); SafetyScore is still binary (>0 permit, ≤0 block); environment modulates safety *boundary* (continuous), not governance *mode* (discrete); no classification of E into {SAFE, CAUTION, UNSAFE}; no Level 2 advisory scope; no unified governance pair conditioned on environmental state | Flehmig et al. (2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md); Baxi (2026) [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md); Kwon et al. (2025) [[notes]](../notes/Runtime%20Safety%20through%20Adaptive%20Shielding-%20From%20Hidden%20Parameter%20Inference%20to%20Provable%20Guarantees.md) |
| 4 — Gap transition | Need to restrict advisory capability itself — not just autonomy level or monitoring response; even the most environment-aware adaptive shield (Kwon et al.) does not classify environmental state into discrete governance modes; no architecture unifies participation governance and advisory scope governance under the same environmental state | Könighofer et al. (2025) [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md); Flehmig et al. (2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md); Kwon et al. (2025) [[notes]](../notes/Runtime%20Safety%20through%20Adaptive%20Shielding-%20From%20Hidden%20Parameter%20Inference%20to%20Provable%20Guarantees.md) |

**Source files**: `literature-review-writing-plan.md` §2.4 · `review-plan.md` §2.4 + Links 4–5 · `justification-three-states.md` · `justification-advisory-scope-restriction.md`  
**Transition**: *"Graduated autonomy literature reveals the architectural gap: systems change autonomy level but never formally restrict what AI is allowed to recommend. Before examining the domain, two further bodies of literature require review: AI governance and guardrails, and hybrid AI."*

---

### 2.5 AI Governance and Guardrails

**Argument**: Guardrails restrict AI outputs — but operate statically and post-hoc, not conditioned on classified environmental safety state.

| Paragraph | Content | Key papers |
|---|---|---|
| 1 — What exists | Guardrails; policy constraints; output filtering; multi-layer defence-in-depth; agentic AI security frameworks | Shamsujjoha et al. (2025) [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md); Chen et al. (2025) [[notes]](../notes/AI%20Safety%20Landscape%20for%20Large%20Language%20Models-%20Taxonomy%2C%20State-of-the-art%2C%20and%20Future%20Directions.md); Wang et al. (2026) [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md); OWASP (2025) [[notes]](../notes/OWASP%20Top%2010%20for%20Agentic%20Applications%202026.md) |
| 2 — Mechanism | Post-hoc filtering: AI generates output, guardrail evaluates and accepts/rejects; 13 guardrail action types; per-action or per-artifact enforcement; pre-hoc grammar constraint: CRANE intersects output grammar with safety grammar to restrict admissible tokens during generation; OWASP Agentic Top 10: 10 threat categories (goal hijack, tool misuse, privilege abuse, supply chain, RCE, memory poisoning, inter-agent comm, cascading failures, human-trust exploitation, rogue agents) with hundreds of mitigations — all binary (permit/block, allow/deny, approve/reject, execute/quarantine); ASI09 "Adaptive Trust Calibration" adjusts human oversight level based on contextual risk — closest near-miss for Level 2 but on human side, not AI-side scope restriction | Shamsujjoha et al. (2025) [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md); Chen, Kang & Li (2025) [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md); Liang et al. (2025) [[notes]](../notes/Safeguarded%20AI-Driven%20Semantic%20Communication-%20Design%20Principles%2C%20Architecture%2C%20and%20Challenges.md); Banerjee et al. (2025) [[notes]](../notes/CRANE-%20Reasoning%20with%20Constrained%20LLM%20Generation.md); OWASP (2025) [[notes]](../notes/OWASP%20Top%2010%20for%20Agentic%20Applications%202026.md) |
| 3 — Limitation | Static rules — same configuration regardless of environmental state; post-hoc does not prevent unsafe reasoning; no state-conditioned activation mechanism; no formal Safety Dominance Property; OWASP confirms global industry consensus: all mitigations across all 10 threat categories are binary; governance conditioned on agent behaviour/identity/policy, not external environmental state | Shamsujjoha et al. (2025) [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md); Bengio et al. (2026) [[notes]](../notes/International%20AI%20Safety%20Report%202026.md); OWASP (2025) [[notes]](../notes/OWASP%20Top%2010%20for%20Agentic%20Applications%202026.md) |
| 4 — Gap transition | Need pre-hoc output space definition — not post-hoc filtering; need state-conditioned governance where the permitted recommendation types change with classified environmental safety state | Wang et al. (2026) [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md); Abella et al. (2025) [[notes]](../notes/SAFEXPLAIN-%20a%20Complete%20Approach%20Towards%20Trustworthy%20AI-Based%20Safety-Critical%20Systems.md) |

**Source files**: `literature-review-writing-plan.md` §2.5 · `review-plan.md` §2.5 + Link 4 · `justification-architecture-differentiation.md`  
**Transition**: *"Governance frameworks define what AI should be permitted to do — but the mechanism by which AI combines deterministic rules with probabilistic inference determines what is technically possible to govern."*

---

### 2.6 Hybrid AI Systems

**Argument**: Hybrid AI improves accuracy and explainability — but does not govern AI participation or restrict advisory scope.

| Paragraph | Content | Key papers |
|---|---|---|
| 1 — What exists | Rule-based + machine learning; neuro-symbolic systems; supervisory hybrid architectures | Castagnone & Nitti (2026) [[notes]](../notes/A%20Neuro-Symbolic%20Framework%20for%20Ensuring%20Deterministic%20Reliability%20in%20AI-Assisted%20Structural%20Engineering-%20The%20SYNAPSE%20Architecture.md); Punzi et al. (2024) [[notes]](../notes/AI%2C%20Meet%20Human-%20Learning%20Paradigms%20for%20Hybrid%20Decision-Making%20Systems.md); Bhuvaneswari et al. (2025) [[notes]](../notes/A%20human-centered%20hybrid%20AI%20framework%20for%20optimizing%20emergency%20triage%20in%20resource-constrained%20settings.md) |
| 2 — Purpose | Improve accuracy; improve explainability; improve robustness; combine deterministic reliability with probabilistic reasoning | Kalmykov & Kalmykov (2025) [[notes]](../notes/Towards%20eXplicitly%20eXplainable%20Artificial%20Intelligence.md); Yuzui & Kaneko (2025) [[notes]](../notes/Toward%20a%20hybrid%20approach%20for%20the%20risk%20analysis%20of%20maritime%20autonomous%20surface%20ships-%20a%20systematic%20review.md); Vermaelen & Holvoet (2025) [[notes]](../notes/umato%202.0%20%E2%80%94%20A%20Constraint-Based%20Planning%20Approach%20for%20Safe%20and%20Robust%20Robot%20Behavior.md) |
| 3 — Limitation | Focus on performance — not on governing when AI participates or what it recommends; hybrid architecture is the enabling mechanism, not the governance solution | Mussi et al. (2025) [[notes]](../notes/Human-AI%20interaction%20in%20safety-critical%20network%20infrastructures.md); Pitale et al. (2025) [[notes]](../notes/HySAFE-AI-%20Hybrid%20Safety%20Architectural%20Analysis%20Framework%20for%20AI%20Systems-%20A%20Case%20Study.md) |

**Source files**: `literature-review-writing-plan.md` §2.6 · `review-plan.md` §2.6 + Link 2 · `justification-contribution-characterisation.md`  
**Transition**: *"Hybrid AI is the enabling architecture. The deployment context determines the constraints. In low-resource environments, those constraints are particularly severe."*

---

### 2.7 AI in Low-Resource Environments

**Argument**: Low-resource environments impose structural constraints that most AI safety architectures do not accommodate — making binary governance especially costly.

| Paragraph | Content | Key papers |
|---|---|---|
| 1 — Context | Limited connectivity; limited computation; mobile-based usage; no data infrastructure; IoT+AI already deployed in aquaculture but with resource barriers | Katende (2026) [[notes]](../notes/Rethinking%20data-efficient%20artificial%20intelligence%20for%20low-resource%20settings.md); Longobardi et al. (2025) [[notes]](../notes/Peskas-%20Automated%20analytics%20for%20small-scale%2C%20data-deficient%20fisheries.md); Bhuvaneswari et al. (2025) [[notes]](../notes/A%20human-centered%20hybrid%20AI%20framework%20for%20optimizing%20emergency%20triage%20in%20resource-constrained%20settings.md); Chandran et al. (2025) [[notes]](../notes/Smart%20technologies%20in%20aquaculture-%20An%20integrated%20IoT%2C%20AI%2C%20and%20blockchain%20framework%20for%20sustainable%20growth.md); Tandel et al. (2025) [[notes]](../notes/Smart%20Aquaculture-%20IoT%20and%20AI%20Application%20for%20Sustainable%20Fisheries.md) |
| 2 — Challenges | Sparse and noisy data; limited institutional capacity; users with varying digital literacy; no cloud compute; intermittent connectivity; Chandran et al. document small-scale farm barriers: cost, remote connectivity (NB-IoT, LoRaWAN for off-grid), technical expertise gap; Tandel et al.: "High initial costs restrict small-scale farmer accessibility", "limited internet connectivity" in remote areas, "farmers lack technical expertise"; Ogenyi et al. confirm resource constraints in autonomous IoT devices | Katende (2026) [[notes]](../notes/Rethinking%20data-efficient%20artificial%20intelligence%20for%20low-resource%20settings.md); Yamin et al. (2025) [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md); Zhao & Yuan (2025) [[notes]](../notes/AI%20in%20Healthcare%20for%20Resource%20Limited%20Settings-%20An%20Exploration%20and%20Ethical%20Evaluation.md); Chandran et al. (2025) [[notes]](../notes/Smart%20technologies%20in%20aquaculture-%20An%20integrated%20IoT%2C%20AI%2C%20and%20blockchain%20framework%20for%20sustainable%20growth.md); Tandel et al. (2025) [[notes]](../notes/Smart%20Aquaculture-%20IoT%20and%20AI%20Application%20for%20Sustainable%20Fisheries.md); Ogenyi et al. (2025) [[notes]](../notes/Securing%20the%20future-%20AI-driven%20cybersecurity%20in%20the%20age%20of%20autonomous%20IoT.md) |
| 3 — Gap | No safety-aware AI governance architecture designed for low-resource deployment; binary governance is particularly costly here — blocking AI entirely under moderate risk wastes a scarce resource; IoT+AI systems in aquaculture demonstrate feasibility (Chandran: 45% mortality reduction) but implement no governance layer | Perez-Cerrolaza et al. (2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md); Katende (2026) [[notes]](../notes/Rethinking%20data-efficient%20artificial%20intelligence%20for%20low-resource%20settings.md); Chandran et al. (2025) [[notes]](../notes/Smart%20technologies%20in%20aquaculture-%20An%20integrated%20IoT%2C%20AI%2C%20and%20blockchain%20framework%20for%20sustainable%20growth.md) |

**Source files**: `literature-review-writing-plan.md` §2.7 · `review-plan.md` §2.7 + Link 7 · `justification-low-resource-environments.md`  
**Transition**: *"Within the class of low-resource, safety-critical environments, coastal fisheries is the domain that most directly motivates and empirically validates the proposed architecture."*

---

### 2.8 Fisheries Decision Context

**Argument**: Small-scale fisheries are a safety-critical, low-resource domain where tripartite decision-making already exists informally — and where binary governance creates a documented decision support vacuum.

| Paragraph | Content | Key papers |
|---|---|---|
| 1 — Context | Small-scale fisheries; high environmental variability; human-driven decisions; declining traditional knowledge | Yamin et al. (2025) [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md); Gao (2024) [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md); Rahim et al. (2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) |
| 2 — Risk factors | Wind, sea state, rainfall, marine warnings, vessel category, time of day — form the empirical basis for E; night navigation elevates accident risk; restricted visibility is highest-rated risk factor; environmental conditions degrade all maritime sensor modalities simultaneously (SAR, optical, AIS, RF); three wind-speed regimes as empirical precursor to S=f(E) | Atacan & Düzbastılar (2023) [[notes]](../notes/Determination%20of%20risk%20perception%20in%20small-scale%20fishing%20and%20navigation.md); Dominguez-Péry et al. (2023) [[notes]](../notes/A%20holistic%20view%20of%20maritime%20navigation%20accidents%20and%20risk%20indicators-%20examining%20IMO%20reports%20from%202011%20to%202021.md); Yamin et al. (2025) [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md); Ryu & Han (2025) [[notes]](../notes/Environment-Aware%20Multi-Sensor%20Fusion%20for%20Maritime%20Domain%20Awareness-%20A%20Comprehensive%20Review.md) |
| 3 — Gap | No formal safety governance in fisheries AI; tripartite go/cautious-go/don't-go decision structure exists informally but is unsupported; flexibility is the weakest adaptive capacity domain; binary governance replicates warnings already ignored; IoT+AI is deployed in aquaculture/fisheries (Chandran et al.: 111-paper systematic review; Tandel et al.: Arduino + SMS alerts) — environmental sensors (pH, temperature, dissolved oxygen) feed AI as input but never trigger governance changes; all recommendation types always available regardless of environmental conditions = **environment-as-input-not-governance pattern** | Gao (2024) [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md); Rahim et al. (2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md); Yamin et al. (2025) [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md); Chandran et al. (2025) [[notes]](../notes/Smart%20technologies%20in%20aquaculture-%20An%20integrated%20IoT%2C%20AI%2C%20and%20blockchain%20framework%20for%20sustainable%20growth.md); Tandel et al. (2025) [[notes]](../notes/Smart%20Aquaculture-%20IoT%20and%20AI%20Application%20for%20Sustainable%20Fisheries.md) |

**Source files**: `literature-review-writing-plan.md` §2.8 · `review-plan.md` §2.8 + Link 7 cont. · `justification-safety-state-design.md` · new papers (Atacan, Dominguez-Péry)  
**Transition**: *"The fisheries domain validates and motivates the proposed architecture — but the architecture must also be evaluated. The following section compares existing approaches at the architectural level."*

---

### New paper: Attard-Frost & Lyons (2025)

**Notes**: `AI governance systems- A multi-scale analysis framework, empirical findings, and future directions. AI and Ethics.md`  
**Citation map link**: `[[notes]](../notes/AI%20governance%20systems-%20A%20multi-scale%20analysis%20framework%2C%20empirical%20findings%2C%20and%20future%20directions.%20AI%20and%20Ethics.md)`

**Key findings for use in Chapter 2**:
- 610-topic empirical mapping of Canada's national AI governance system — zero topics reference runtime environmental state classification, state-conditioned advisory scope restriction, or anything analogous to the CAUTION mode
- Guardrails appear only twice in the 610 topics, framed exclusively in binary terms — confirming practitioners share the binary mental model
- Practitioners recognise a spectrum of policy instrument stringency (legislation → voluntary guidance), but this graduated intuition exists only at the institutional layer, not the runtime architectural layer
- Knowledge/expertise gaps are the most-cited governance constraint even in Canada — strengthens the case for architecturally embedded governance in low-resource environments

**Where to use**:
- **2.9 Comparative Analysis** — P7 (key insight): institutional governance layer confirms binary framing at both technical and practitioner levels
- **2.11 Research Gap** — P1/P3: single-sentence empirical anchor: "a 610-topic mapping of a national AI governance system contains no reference to state-conditioned runtime advisory scope restriction" — strongest available evidence that Level 2 is genuinely absent

---

### New paper: Banerjee et al. (2025) — CRANE

**Notes**: `CRANE- Reasoning with Constrained LLM Generation.md`  
**Citation map link**: `[[notes]](../notes/CRANE-%20Reasoning%20with%20Constrained%20LLM%20Generation.md)`

**Key findings for use in Chapter 2**:
- Proposition 3.1: binary output grammar constraints reduce LLM expressivity to TC⁰ — strongest theoretical motivation for why binary restriction is suboptimal
- Proposition 3.3: augmented grammar G_a = R_M·G restores full expressivity by alternating unconstrained reasoning + constrained output
- Structural precursor to CAUTION mode: output set containment (constrained ⊂ unconstrained) parallels A_AI(CAUTION) ⊂ A_AI(SAFE)
- Syntactically-triggered 2-mode alternation (delimiter-based), NOT environmental-state-conditioned — this is the gap

**Where to use**:
- **2.2 Safety Constraints** — P2 (Mechanism): constrained output generation via grammar intersection; P3 (Limitation): Prop. 3.1 as formal proof binary is suboptimal
- **2.4 Adaptive Autonomy** — P2 (Mechanism): augmented grammar as structural precursor to graduated scope
- **2.9 Comparative Analysis** — P4 (Safety gating): comparator with formal proofs but binary and syntactically-triggered

---

### New paper: Ryu & Han (2025)

**Notes**: `Environment-Aware Multi-Sensor Fusion for Maritime Domain Awareness- A Comprehensive Review.md`  
**Citation map link**: `[[notes]](../notes/Environment-Aware%20Multi-Sensor%20Fusion%20for%20Maritime%20Domain%20Awareness-%20A%20Comprehensive%20Review.md)`

**Key findings for use in Chapter 2**:
- Environmental conditions (wind, wave height, swell, atmospheric state) are first-order determinants of maritime sensor reliability across SAR, optical, AIS, and RF
- All modalities degrade simultaneously under adverse conditions — strongest evidence for externalising governance trigger to environmental state
- Three wind-speed regimes (<2, 2–8, >10–12 m/s) with distinct detection behaviours = empirical precursor to S=f(E) tripartite classification
- Fixed thresholds fail under non-stationary clutter; DL models suffer domain shift — motivates adaptive governance
- No governance architecture proposed — evidence paper only

**Where to use**:
- **2.8 Fisheries Context** — P2 (Risk factors): sensor degradation evidence; three wind-speed regimes as empirical precursor to S=f(E)

---

### New paper: Hamel-De le Court et al. (2025)

**Notes**: `Probabilistic Shielding for Safe Reinforcement Learning.md`
**Citation map link**: `[[notes]](../notes/Probabilistic%20Shielding%20for%20Safe%20Reinforcement%20Learning.md)`

**Key findings for use in Chapter 2**:
- Probabilistic shield with formal guarantee: Theorem 1 (safety), Theorem 2 (convergence) — strongest formal safety proof among comparators
- Shield intervenes when policy action exceeds probabilistic risk threshold — binary gate (intervene/permit)
- No graduated states; shield provides single-threshold binary override, not multi-mode governance
- AAAI-25 venue confirms mainstream recognition of shielding approach

**Where to use**:
- **2.2 Safety Constraints** — P1 (What exists): probabilistic shield as state-of-art safety mechanism; P2 (Mechanism): probabilistic threshold + formal theorems; P3 (Limitation): still binary gate
- **2.9 Comparative Analysis** — P4 (Safety gating): comparator with formal proofs but binary intervention

---

### New paper: Kwon et al. (2025)

**Notes**: `Runtime Safety through Adaptive Shielding- From Hidden Parameter Inference to Provable Guarantees.md`
**Citation map link**: `[[notes]](../notes/Runtime%20Safety%20through%20Adaptive%20Shielding-%20From%20Hidden%20Parameter%20Inference%20to%20Provable%20Guarantees.md)`

**Key findings for use in Chapter 2**:
- Closest near-miss to proposed architecture: environment-centric features E ∈ ℝ^n₂ + runtime adaptation via ACP threshold Γ_t + formal safety guarantee (Theorem 1)
- SafetyScore is still binary (safe/unsafe); adaptation is quantitative (threshold adjustment) not qualitative (governance mode change)
- No discrete SAFE/CAUTION/UNSAFE states; no advisory scope restriction; no unified governance pair
- SRO (Shielded Reward Objective) combines task reward + safety penalty — single objective, not multi-mode

**Where to use**:
- **2.2 Safety Constraints** — P1 (What exists): adaptive shielding; P2 (Mechanism): E ∈ ℝ^n₂ + ACP; P3 (Limitation): binary SafetyScore
- **2.4 Adaptive Autonomy** — P1/P2/P3/P4: closest near-miss; quantitative not qualitative adaptation
- **2.9 Comparative Analysis** — P5 (Adaptive autonomy): primary comparator for near-miss analysis
- **2.11 Research Gap** — P2: closest near-miss still binary

---

### New paper: Feng, McDonald & Zhang (2025)

**Notes**: `Levels of Autonomy for AI Agents.md`
**Citation map link**: `[[notes]](../notes/Levels%20of%20Autonomy%20for%20AI%20Agents.md)`

**Key findings for use in Chapter 2**:
- Identifies two governance dimensions: agency (what tools AI can access) and autonomy (how much human involvement required)
- Five autonomy levels (L1–L5) with "autonomy certificates" — most conceptually revealing framework
- Three critical limitations: (a) levels fixed at design-time not runtime, (b) missing third lever — advisory scope restriction, (c) environment treated as constant deployment context not variable E
- Agency ≠ autonomy distinction is valuable but missing unified conditioning on environmental state

**Where to use**:
- **2.3 Human-AI Authority** — P1/P2/P3/P4: levels of autonomy, agency ≠ autonomy, design-time limitation
- **2.9 Comparative Analysis** — P5 (Adaptive autonomy): design-time vs runtime distinction
- **2.11 Research Gap** — P2: two dimensions but wrong two, design-time not runtime

---

### New paper: Zhang et al. (2025) — IoT Public Safety

**Notes**: `Developing real-time IoT-based public safety alert and emergency response systems.md`
**Citation map link**: `[[notes]](../notes/Developing%20real-time%20IoT-based%20public%20safety%20alert%20and%20emergency%20response%20systems.md)`

**Key findings for use in Chapter 2**:
- Most explicit binary formalisation in the literature: Eq. 4 φ(X(t)) = {1 if P_alert(X(t)) ≥ θ; 0 otherwise}
- IoT environmental sensors feed AI classification, but safety response is hard binary alert/no-alert
- Environment is input to the AI system, never triggers governance changes — environment-as-input-not-governance pattern
- Real-time public safety context confirms binary ceiling across domains

**Where to use**:
- **2.2 Safety Constraints** — P3 (Limitation): Eq. 4 as explicit binary ceiling formalisation
- **2.7 Low-Resource** — P7 (IoT+AI systems): environment-as-input-not-governance pattern
- **2.9 Comparative Analysis** — P7 (IoT+AI): binary despite environmental sensing
- **2.11 Research Gap** — P1: most explicit binary formalisation

---

### New paper: OWASP (2025) — Agentic AI Top 10

**Notes**: `OWASP Top 10 for Agentic Applications 2026.md`
**Citation map link**: `[[notes]](../notes/OWASP%20Top%2010%20for%20Agentic%20Applications%202026.md)`

**Key findings for use in Chapter 2**:
- Global industry consensus document: 10 threat categories for agentic AI, hundreds of mitigations — all binary (permit/block)
- ASI09 "Adaptive Trust Calibration" is closest to graduated governance but adjusts human oversight intensity, not AI advisory scope
- No mitigation conditions AI scope on environmental state; no intermediate governance mode
- Strongest evidence that binary governance is not just academic default but industry consensus

**Where to use**:
- **2.5 Guardrails** — P2 (Mechanism): 10 categories, all binary; ASI09 adjusts oversight not scope; P3 (Limitation): industry consensus confirmation
- **2.9 Comparative Analysis** — P6 (Guardrails): global industry consensus comparator
- **2.11 Research Gap** — P1: industry-scale binary confirmation

---

### New paper: Chandran et al. (2025)

**Notes**: `Smart technologies in aquaculture- An integrated IoT, AI, and blockchain framework for sustainable growth.md`
**Citation map link**: `[[notes]](../notes/Smart%20technologies%20in%20aquaculture-%20An%20integrated%20IoT%2C%20AI%2C%20and%20blockchain%20framework%20for%20sustainable%20growth.md)`

**Key findings for use in Chapter 2**:
- Aquaculture IoT+AI+blockchain system: environmental sensors (pH, DO, temperature, turbidity) feed AI prediction models
- Blockchain for data integrity and traceability — but no governance layer between environment and AI
- Environment-as-input-not-governance pattern: sensors inform AI, never trigger changes to AI participation or advisory scope
- Closest domain to small-scale fisheries — confirms gap extends to nearest-domain systems

**Where to use**:
- **2.7 Low-Resource** — P2 (Small-scale barriers): IoT+AI feasibility in aquaculture
- **2.8 Fisheries Context** — P3: environment-as-input-not-governance with specific IoT examples
- **2.9 Comparative Analysis** — P7 (IoT+AI): domain comparator
- **2.11 Research Gap** — P3: domain confirmation of gap

---

### New paper: Ogenyi et al. (2025)

**Notes**: `Securing the future- AI-driven cybersecurity in the age of autonomous IoT.md`
**Citation map link**: `[[notes]](../notes/Securing%20the%20future-%20AI-driven%20cybersecurity%20in%20the%20age%20of%20autonomous%20IoT.md)`

**Key findings for use in Chapter 2**:
- A-IoT "adaptive security" framework: scales protection intensity (encryption strength, monitoring frequency) based on threat level
- Adaptive security ≠ adaptive governance: adapts security measures quantitatively, not AI governance mode qualitatively
- Confirms that even "adaptive" IoT systems adapt operational parameters, not the governance relationship between human and AI
- Useful as counter-example: "adaptive" in the IoT literature means parameter tuning, not governance mode switching

**Where to use**:
- **2.7 Low-Resource** — P3: adaptive security ≠ adaptive governance distinction
- **2.9 Comparative Analysis** — P7 (IoT+AI): adaptive but not governance-adaptive
- **2.11 Research Gap** — P3: domain confirmation

---

### New paper: Tandel et al. (2025)

**Notes**: `Smart Aquaculture- IoT and AI Application for Sustainable Fisheries.md`
**Citation map link**: `[[notes]](../notes/Smart%20Aquaculture-%20IoT%20and%20AI%20Application%20for%20Sustainable%20Fisheries.md)`

**Key findings for use in Chapter 2**:
- Aquaculture IoT+AI system achieving 45% mortality reduction — strongest quantitative evidence of IoT+AI benefit in small-scale aquaculture
- Binary SMS alerts when parameters exceed thresholds — no graduated response
- Environmental sensors feed AI models but governance is absent: environment → AI → binary alert → human
- Demonstrates that IoT+AI technical feasibility is proven but governance layer is missing

**Where to use**:
- **2.7 Low-Resource** — P2 (Small-scale barriers): 45% mortality reduction as feasibility evidence; P3: binary SMS despite IoT capability
- **2.8 Fisheries Context** — P3: environment-as-input-not-governance with specific examples
- **2.9 Comparative Analysis** — P7 (IoT+AI): domain comparator with quantitative evidence
- **2.11 Research Gap** — P3: domain confirmation

---

### 2.9 Comparative Analysis

**Argument**: No existing system jointly governs AI participation and advisory scope under the same classified environmental state.

| Paragraph | Content | Key papers |
|---|---|---|
| 1 — Purpose | Compare systems at architecture level; focus on decision governance dimensions | Review-plan.md §3 Governance Level Distribution |
| 2 — Dimensions | Participation control (L1: G(S)); advisory restriction (L2: A_AI(S)); unified governance; environmental state conditioning | `justification-novelty-gap.md` §12 comparison table |
| 3 — Table | Summary comparison table (reproduced from comparison-table.md) | `papers/comparison-table.md` Architecture Comparison Summary |
| 4 — Safety gating | Participation only; binary; no advisory scope restriction; Hamel-De le Court: probabilistic shield with formal guarantees (Theorems 1–2) but binary safe/unsafe; CRANE: output grammar restricts admissible outputs but binary (constrained/unconstrained), Prop. 3.1 proves binary reduces capability | Könighofer et al. (2025) [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md); Bajcsy & Fisac (2024) [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md); Corsi et al. (2024) [[notes]](../notes/Verification-Guided%20Shielding%20for%20Deep%20Reinforcement%20Learning.md); Seong, Lim & Yoon (2025) [[notes]](../notes/clguard-extraction.md); Banerjee et al. (2025) [[notes]](../notes/CRANE-%20Reasoning%20with%20Constrained%20LLM%20Generation.md); Hamel-De le Court et al. (2025) [[notes]](../notes/Probabilistic%20Shielding%20for%20Safe%20Reinforcement%20Learning.md) |
| 5 — Adaptive autonomy | Authority only; governs monitoring not scope; Flehmig closest but governs intensity not types; **Kwon et al. closest near-miss**: environment-centric features E ∈ ℝ^n₂ + runtime adaptation + formal guarantee, but SafetyScore still binary; Feng et al.: five autonomy levels but design-time not runtime, reveals missing third lever (advisory scope) | Flehmig et al. (2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md); Baxi (2026) [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md); Kwon et al. (2025) [[notes]](../notes/Runtime%20Safety%20through%20Adaptive%20Shielding-%20From%20Hidden%20Parameter%20Inference%20to%20Provable%20Guarantees.md); Feng et al. (2025) [[notes]](../notes/Levels%20of%20Autonomy%20for%20AI%20Agents.md) |
| 6 — Guardrails | Output filtering only; post-hoc or pre-hoc grammar constraint; static; no environmental state conditioning; CRANE restricts admissible outputs via grammar but syntactically-triggered, not state-conditioned; OWASP confirms global industry consensus: 10 threat categories, hundreds of mitigations, all binary; ASI09 adjusts human oversight not AI advisory scope | Shamsujjoha et al. (2025) [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md); Chen, Kang & Li (2025) [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md); Banerjee et al. (2025) [[notes]](../notes/CRANE-%20Reasoning%20with%20Constrained%20LLM%20Generation.md); OWASP (2025) [[notes]](../notes/OWASP%20Top%2010%20for%20Agentic%20Applications%202026.md) |
| 7 — IoT+AI systems | Environmental sensors exist in IoT+AI systems but are used as AI *input*, never as governance *trigger*; Zhang Eq. 4 is the most explicit binary formalisation: rich heterogeneous sensor input → single binary threshold; Chandran (111-paper review) and Tandel show aquaculture IoT+AI has all pipeline components (E→processing→AI) but no governance layer; Ogenyi: "adaptive security" scales protection intensity not governance mode — adaptive security ≠ adaptive governance | Zhang et al. (2025) [[notes]](../notes/Developing%20real-time%20IoT-based%20public%20safety%20alert%20and%20emergency%20response%20systems.md); Chandran et al. (2025) [[notes]](../notes/Smart%20technologies%20in%20aquaculture-%20An%20integrated%20IoT%2C%20AI%2C%20and%20blockchain%20framework%20for%20sustainable%20growth.md); Tandel et al. (2025) [[notes]](../notes/Smart%20Aquaculture-%20IoT%20and%20AI%20Application%20for%20Sustainable%20Fisheries.md); Ogenyi et al. (2025) [[notes]](../notes/Securing%20the%20future-%20AI-driven%20cybersecurity%20in%20the%20age%20of%20autonomous%20IoT.md) |
| 8 — Key insight | Each existing system implements one governance mechanism only; no system unifies both levels under classified environmental state; confirmed across safety shields, agent governance, guardrails, and IoT+AI systems | Ramos et al. (2024) [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md); Newcomb & Ochoa (2026) [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md); Perez-Cerrolaza et al. (2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md); OWASP (2025) [[notes]](../notes/OWASP%20Top%2010%20for%20Agentic%20Applications%202026.md) |

**Source files**: `literature-review-writing-plan.md` §2.9 · `review-plan.md` §3 + §4 · `justification-architecture-differentiation.md` · `papers/comparison-table.md`  
**Transition**: *"The comparative analysis confirms the gap — leading to the literature summary and formal research gap statement."*

---

### 2.10 Literature Summary

**Argument**: Existing approaches are fragmented — each governs one dimension of AI behaviour but none achieves unified governance.

| Paragraph | Content | Key papers |
|---|---|---|
| 1 — Synthesis | Safety gating → participation only; adaptive autonomy → authority only; guardrails → output filtering; hybrid AI → no governance | All prior sections |
| 2 — Limitation | Fragmented approaches; no integration; binary governance universal; no state-conditioned unified governance pair | Ramos et al. (2024) [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md); Bengio et al. (2026) [[notes]](../notes/International%20AI%20Safety%20Report%202026.md) |

**Source files**: `literature-review-writing-plan.md` §2.10 · `review-plan.md` §8 Coverage Summary · all justification docs

---

### 2.11 Research Gap

**Argument**: No architecture jointly governs AI participation and advisory scope as a unified pair conditioned on classified environmental safety state — with formal safety properties.

| Paragraph | Content | Key papers |
|---|---|---|
| 1 — Core gap | No system defines both G(S) and A_AI(S) conditioned on the same S = f(E); no intermediate CAUTION mode; no advisory containment A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ ∅. Zhang et al. (2025) [[notes]](../notes/Developing%20real-time%20IoT-based%20public%20safety%20alert%20and%20emergency%20response%20systems.md) provides the most explicit binary formalisation: φ(X(t)) = {1 if P_alert ≥ θ; 0 otherwise} (Eq. 4) — a hard binary ceiling with no intermediate state. OWASP (2025) [[notes]](../notes/OWASP%20Top%2010%20for%20Agentic%20Applications%202026.md) confirms this at industry scale: 10 threat categories, hundreds of mitigations, all binary (permit/block); ASI09 "Adaptive Trust Calibration" adjusts human oversight intensity, not AI advisory scope | `justification-novelty-gap.md` §12; four SLR confirmations; Zhang et al. (2025) [[notes]](../notes/Developing%20real-time%20IoT-based%20public%20safety%20alert%20and%20emergency%20response%20systems.md); OWASP (2025) [[notes]](../notes/OWASP%20Top%2010%20for%20Agentic%20Applications%202026.md) |
| 2 — Closest near-miss | Kwon et al. (2025) [[notes]](../notes/Runtime%20Safety%20through%20Adaptive%20Shielding-%20From%20Hidden%20Parameter%20Inference%20to%20Provable%20Guarantees.md) is the closest architecture: environment-centric features E ∈ ℝ^n₂, runtime adaptation via ACP threshold Γ_t, formal safety guarantee (Theorem 1). But SafetyScore remains binary; adaptation is quantitative (threshold adjustment) not qualitative (governance mode change); no discrete SAFE/CAUTION/UNSAFE states. Feng et al. (2025) [[notes]](../notes/Levels%20of%20Autonomy%20for%20AI%20Agents.md) identifies two governance dimensions (agency + autonomy) but both are fixed at design-time, missing the third lever (advisory scope restriction) and treating environment as constant deployment context not variable E | Kwon et al. (2025) [[notes]](../notes/Runtime%20Safety%20through%20Adaptive%20Shielding-%20From%20Hidden%20Parameter%20Inference%20to%20Provable%20Guarantees.md); Feng et al. (2025) [[notes]](../notes/Levels%20of%20Autonomy%20for%20AI%20Agents.md); Newcomb & Ochoa (2026) [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md); Ramos et al. (2024) [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md) |
| 3 — Domain confirmation | IoT+AI systems in aquaculture and public safety confirm environment-as-input-not-governance pattern: Chandran et al. (2025) [[notes]](../notes/Smart%20technologies%20in%20aquaculture-%20An%20integrated%20IoT%2C%20AI%2C%20and%20blockchain%20framework%20for%20sustainable%20growth.md) uses environmental sensors to feed AI predictions but no governance layer; Tandel et al. (2025) [[notes]](../notes/Smart%20Aquaculture-%20IoT%20and%20AI%20Application%20for%20Sustainable%20Fisheries.md) achieves 45% mortality reduction via IoT+AI but only binary SMS alerts; Ogenyi et al. (2025) [[notes]](../notes/Securing%20the%20future-%20AI-driven%20cybersecurity%20in%20the%20age%20of%20autonomous%20IoT.md) "adaptive security" scales protection intensity not governance mode. Even closest-domain systems treat environment as AI input, never as governance trigger | Chandran et al. (2025) [[notes]](../notes/Smart%20technologies%20in%20aquaculture-%20An%20integrated%20IoT%2C%20AI%2C%20and%20blockchain%20framework%20for%20sustainable%20growth.md); Tandel et al. (2025) [[notes]](../notes/Smart%20Aquaculture-%20IoT%20and%20AI%20Application%20for%20Sustainable%20Fisheries.md); Ogenyi et al. (2025) [[notes]](../notes/Securing%20the%20future-%20AI-driven%20cybersecurity%20in%20the%20age%20of%20autonomous%20IoT.md) |
| 4 — Contribution link | Need a graduated safety-state-gated architecture with unified governance (G(S), A_AI(S)); need evaluation comparing graduated vs. binary governance; need socio-technical evaluation of CAUTION mode. The binary ceiling is confirmed across formal methods (Zhang Eq. 4), industry consensus (OWASP), adaptive shielding (Kwon), autonomy frameworks (Feng), and domain-specific IoT+AI (Chandran, Tandel, Ogenyi) — strengthening the case that the gap is structural, not incidental | `justification-novelty-gap.md`; `review-plan.md` §2.10 gap statement |

**Source files**: `literature-review-writing-plan.md` §2.11 · `review-plan.md` §2.10 Research Gap Statement · `justification-novelty-gap.md`  
**Closing sentence**: *"Therefore, this research proposes a graduated safety-state-gated architecture for AI decision support that defines how safety conditions govern both AI participation and advisory scope."*

---

## Execution Order

| Round | Section | Status |
|---|---|---|
| 1 | 2.1 AI Decision Support | ✅ Draft complete |
| 2 | 2.2 Safety Constraints | ✅ Draft complete |
| 3 | 2.3 Human-AI Authority | ✅ Draft complete |
| 4 | 2.4 Adaptive Autonomy | ✅ Draft complete |
| 5 | 2.5 Guardrails | ✅ Draft complete |
| 6 | 2.6 Hybrid AI | ✅ Draft complete |
| 7 | 2.7 Low-Resource | ✅ Draft complete |
| 8 | 2.8 Fisheries Context | ✅ Draft complete |
| 9 | 2.9 Comparative Analysis | ✅ Draft complete |
| 10 | 2.10 Literature Summary | ✅ Draft complete |
| 11 | 2.11 Research Gap | ✅ Draft complete |

---

## Output File

All written sections will be appended to:  
`docs/chapter-2-draft.md`

Each round: write the section → user reviews → update status above → proceed to next.
