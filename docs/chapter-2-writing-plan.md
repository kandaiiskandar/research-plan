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
| 3 — Problem | Incorrect recommendations anchor decisions; automation bias; over-reliance; distributional shift degrades reliability | Wen et al. (2025) [[notes]](../notes/Risk%20Perception%20in%20Complex%20Systems-%20A%20Comparative%20Analysis%20of%20Process%20Control%20and%20Autonomous%20Vehicle%20Failures.md); Newcomb & Ochoa (2026) [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md); Bloomfield & Rushby (2025) [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md) |
| 4 — Gap transition | Research focuses on accuracy and explainability; missing: governing AI participation and advisory scope as a function of operational conditions | Perez-Cerrolaza et al. (2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md); Newcomb & Ochoa (2026) [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md) |

**Source files**: `literature-review-writing-plan.md` §2.1 · `review-plan.md` §2.1 + Links 1–2 · `justification-ai-necessity.md`  
**Transition**: *"AI decision support improves decisions — but as AI moves into safety-critical environments, the question of how to constrain AI behaviour becomes critical. The first response in the literature has been deterministic safety constraints."*

---

### 2.2 Deterministic Safety Constraints and Safety Gating

**Argument**: Safety constraints govern whether AI acts — but all existing mechanisms are binary and do not restrict what AI is allowed to recommend.

| Paragraph | Content | Key papers |
|---|---|---|
| 1 — What exists | Rule-based safety systems; runtime verification; safety filters; safety shields | Könighofer et al. (2025) [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md); Dalrymple et al. (2024) [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md); Bajcsy & Fisac (2024) [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md) |
| 2 — Mechanism | Binary gate: allow or block; prevent unsafe actions; switch to fallback; formal safety guarantees | Corsi et al. (2024) [[notes]](../notes/Verification-Guided%20Shielding%20for%20Deep%20Reinforcement%20Learning.md); Abella et al. (2025) [[notes]](../notes/SAFEXPLAIN-%20a%20Complete%20Approach%20Towards%20Trustworthy%20AI-Based%20Safety-Critical%20Systems.md); Vermaelen & Holvoet (2025) [[notes]](../notes/umato%202.0%20%E2%80%94%20A%20Constraint-Based%20Planning%20Approach%20for%20Safe%20and%20Robust%20Robot%20Behavior.md) |
| 3 — Limitation | Binary governance is universal — confirmed across 91 papers, 46 formal methods studies, 11 international frameworks; no intermediate state; no advisory scope restriction | Ramos et al. (2024) [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md); Newcomb & Ochoa (2026) [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md); Bengio et al. (2026) [[notes]](../notes/International%20AI%20Safety%20Report%202026.md); Odriozola-Olalde et al. (2023) [[notes]](../notes/Shielded%20Reinforcement%20Learning-%20A%20review%20of%20reactive%20methods%20for%20safe%20learning.md) |
| 4 — Gap transition | Safety constraints govern participation only (Level 1); do not control what AI recommends (Level 2); decision authority allocation is a separate, unresolved question | Perez-Cerrolaza et al. (2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) |

**Source files**: `literature-review-writing-plan.md` §2.2 · `review-plan.md` §2.2 + Link 3 · `justification-novelty-gap.md`  
**Transition**: *"Safety constraints govern whether AI acts — but they do not govern what AI is allowed to recommend, or when AI should participate based on conditions. This raises a deeper question: how should decision authority be allocated between human and AI?"*

---

### 2.3 Human–AI Decision Authority

**Argument**: Human-AI authority frameworks define who decides — but do not specify when AI should participate based on safety conditions, or restrict what AI produces.

| Paragraph | Content | Key papers |
|---|---|---|
| 1 — Concept | Human-in-the-loop; human-on-the-loop; levels of automation; supervisory control | Ramos et al. (2024) [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md); Porter et al. (2025) [[notes]](../notes/INSYTE-%20A%20Classification%20Framework%20for%20Traditional%20to%20Agentic%20AI%20Systems.md); Bach et al. (2024) [[notes]](../notes/Unpacking%20Human-AI%20Interaction%20in%20Safety-Critical%20Industries-%20A%20Systematic%20Literature%20Review.md) |
| 2 — Mechanism | Decision authority shifts between human and AI; AI suggests, human decides; authority varies by context and task | Saup et al. (2026) [[notes]](../notes/From%20pilots%20to%20decision%20systems-%20embedding%20generative%20AI%20into%20strategic%20decision-making%20through%20a%20socio-technical%20and%20governance%20lens.md); Madsen & Kim (2024) [[notes]](../notes/A%20state-of-the-art%20review%20of%20AI%20decision%20transparency%20for%20autonomous%20shipping.md); Leppinen et al. (2026) [[notes]](../notes/A%20Stage-Gate%20Decision%20Process%20for%20Guiding%20the%20Development%20of%20AI%20Solutions%20for%20Preventive%20Maintenance.md) |
| 3 — Limitation | Controls who decides; does not control what AI recommends; AI outputs remain unchanged across risk levels; authority allocation is static, not runtime-adaptive | Porter et al. (2025) [[notes]](../notes/INSYTE-%20A%20Classification%20Framework%20for%20Traditional%20to%20Agentic%20AI%20Systems.md); Ramos et al. (2024) [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md) |
| 4 — Gap transition | No structured control over AI advisory content; risk level does not change what AI is permitted to recommend; need advisory scope governance independent of authority allocation | Madsen & Kim (2024) [[notes]](../notes/A%20state-of-the-art%20review%20of%20AI%20decision%20transparency%20for%20autonomous%20shipping.md) |

**Source files**: `literature-review-writing-plan.md` §2.3 · `review-plan.md` §2.3 + Link 3 cont. · `justification-unified-governance.md`  
**Transition**: *"If static authority allocation is insufficient, the natural next step is systems that adapt the level of autonomy or AI participation based on risk at runtime."*

---

### 2.4 Adaptive Autonomy and Risk-Based Systems

**Argument**: Risk-adaptive systems change autonomy level — but govern monitoring intensity or operational domain, not AI advisory scope. No architecture formally restricts what AI is allowed to recommend based on classified environmental state.

| Paragraph | Content | Key papers |
|---|---|---|
| 1 — What exists | Adaptive autonomy; risk-aware systems; degraded modes; traffic-light governance | Flehmig et al. (2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md); Gyllenhammar et al. (2025) [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md); Baxi (2026) [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) |
| 2 — Mechanism | Behaviour changes based on risk; switches between modes; Flehmig: traffic-light index from performance metrics; Baxi: K-tier graduated permissions with containment | Flehmig et al. (2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md); Baxi (2026) [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md); Li et al. (2026) [[notes]](../notes/Safety-Enhanced%20Deep%20Reinforcement%20Learning%20for%20Autonomous%20Driving-%20Dare%20to%20Make%20Mistakes%20to%20Learn%20Better%20and%20Faster.md) |
| 3 — Limitation | Changes monitoring intensity or control authority — not advisory scope; AI still produces same recommendation types across modes; no formal containment of recommendation types; no unified governance pair conditioned on environmental state | Flehmig et al. (2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md); Baxi (2026) [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) |
| 4 — Gap transition | Need to restrict advisory capability itself — not just autonomy level or monitoring response; no architecture unifies participation governance and advisory scope governance under the same environmental state | Könighofer et al. (2025) [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md); Flehmig et al. (2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md) |

**Source files**: `literature-review-writing-plan.md` §2.4 · `review-plan.md` §2.4 + Links 4–5 · `justification-three-states.md` · `justification-advisory-scope-restriction.md`  
**Transition**: *"Graduated autonomy literature reveals the architectural gap: systems change autonomy level but never formally restrict what AI is allowed to recommend. Before examining the domain, two further bodies of literature require review: AI governance and guardrails, and hybrid AI."*

---

### 2.5 AI Governance and Guardrails

**Argument**: Guardrails restrict AI outputs — but operate statically and post-hoc, not conditioned on classified environmental safety state.

| Paragraph | Content | Key papers |
|---|---|---|
| 1 — What exists | Guardrails; policy constraints; output filtering; multi-layer defence-in-depth | Shamsujjoha et al. (2025) [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md); Chen et al. (2025) [[notes]](../notes/AI%20Safety%20Landscape%20for%20Large%20Language%20Models-%20Taxonomy%2C%20State-of-the-art%2C%20and%20Future%20Directions.md); Wang et al. (2026) [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md) |
| 2 — Mechanism | Post-hoc filtering: AI generates output, guardrail evaluates and accepts/rejects; 13 guardrail action types; per-action or per-artifact enforcement | Shamsujjoha et al. (2025) [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md); Chen, Kang & Li (2025) [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md); Liang et al. (2025) [[notes]](../notes/Safeguarded%20AI-Driven%20Semantic%20Communication-%20Design%20Principles%2C%20Architecture%2C%20and%20Challenges.md) |
| 3 — Limitation | Static rules — same configuration regardless of environmental state; post-hoc does not prevent unsafe reasoning; no state-conditioned activation mechanism; no formal Safety Dominance Property | Shamsujjoha et al. (2025) [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md); Bengio et al. (2026) [[notes]](../notes/International%20AI%20Safety%20Report%202026.md) |
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
| 1 — Context | Limited connectivity; limited computation; mobile-based usage; no data infrastructure | Katende (2026) [[notes]](../notes/Rethinking%20data-efficient%20artificial%20intelligence%20for%20low-resource%20settings.md); Longobardi et al. (2025) [[notes]](../notes/Peskas-%20Automated%20analytics%20for%20small-scale%2C%20data-deficient%20fisheries.md); Bhuvaneswari et al. (2025) [[notes]](../notes/A%20human-centered%20hybrid%20AI%20framework%20for%20optimizing%20emergency%20triage%20in%20resource-constrained%20settings.md) |
| 2 — Challenges | Sparse and noisy data; limited institutional capacity; users with varying digital literacy; no cloud compute; intermittent connectivity | Katende (2026) [[notes]](../notes/Rethinking%20data-efficient%20artificial%20intelligence%20for%20low-resource%20settings.md); Yamin et al. (2025) [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md); Zhao & Yuan (2025) [[notes]](../notes/AI%20in%20Healthcare%20for%20Resource%20Limited%20Settings-%20An%20Exploration%20and%20Ethical%20Evaluation.md) |
| 3 — Gap | No safety-aware AI governance architecture designed for low-resource deployment; binary governance is particularly costly here — blocking AI entirely under moderate risk wastes a scarce resource | Perez-Cerrolaza et al. (2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md); Katende (2026) [[notes]](../notes/Rethinking%20data-efficient%20artificial%20intelligence%20for%20low-resource%20settings.md) |

**Source files**: `literature-review-writing-plan.md` §2.7 · `review-plan.md` §2.7 + Link 7 · `justification-low-resource-environments.md`  
**Transition**: *"Within the class of low-resource, safety-critical environments, coastal fisheries is the domain that most directly motivates and empirically validates the proposed architecture."*

---

### 2.8 Fisheries Decision Context

**Argument**: Small-scale fisheries are a safety-critical, low-resource domain where tripartite decision-making already exists informally — and where binary governance creates a documented decision support vacuum.

| Paragraph | Content | Key papers |
|---|---|---|
| 1 — Context | Small-scale fisheries; high environmental variability; human-driven decisions; declining traditional knowledge | Yamin et al. (2025) [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md); Gao (2024) [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md); Rahim et al. (2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) |
| 2 — Risk factors | Wind, sea state, rainfall, marine warnings, vessel condition, time of day — form the empirical basis for E; night navigation elevates accident risk; restricted visibility is highest-rated risk factor | Atacan & Düzbastılar (2023) [[notes]](../notes/Determination%20of%20risk%20perception%20in%20small-scale%20fishing%20and%20navigation.md); Dominguez-Péry et al. (2023) [[notes]](../notes/A%20holistic%20view%20of%20maritime%20navigation%20accidents%20and%20risk%20indicators-%20examining%20IMO%20reports%20from%202011%20to%202021.md); Yamin et al. (2025) [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md) |
| 3 — Gap | No formal safety governance in fisheries AI; tripartite go/cautious-go/don't-go decision structure exists informally but is unsupported; flexibility is the weakest adaptive capacity domain; binary governance replicates warnings already ignored | Gao (2024) [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md); Rahim et al. (2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md); Yamin et al. (2025) [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md) |

**Source files**: `literature-review-writing-plan.md` §2.8 · `review-plan.md` §2.8 + Link 7 cont. · `justification-safety-state-design.md` · new papers (Atacan, Dominguez-Péry)  
**Transition**: *"The fisheries domain validates and motivates the proposed architecture — but the architecture must also be evaluated. The following section compares existing approaches at the architectural level."*

---

### 2.9 Comparative Analysis

**Argument**: No existing system jointly governs AI participation and advisory scope under the same classified environmental state.

| Paragraph | Content | Key papers |
|---|---|---|
| 1 — Purpose | Compare systems at architecture level; focus on decision governance dimensions | Review-plan.md §3 Governance Level Distribution |
| 2 — Dimensions | Participation control (L1: G(S)); advisory restriction (L2: A_AI(S)); unified governance; environmental state conditioning | `justification-novelty-gap.md` §12 comparison table |
| 3 — Table | Summary comparison table (reproduced from comparison-table.md) | `papers/comparison-table.md` Architecture Comparison Summary |
| 4 — Safety gating | Participation only; binary; no advisory scope restriction | Könighofer et al. (2025) [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md); Bajcsy & Fisac (2024) [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md); Corsi et al. (2024) [[notes]](../notes/Verification-Guided%20Shielding%20for%20Deep%20Reinforcement%20Learning.md) |
| 5 — Adaptive autonomy | Authority only; governs monitoring not scope; Flehmig closest but governs intensity not types | Flehmig et al. (2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md); Baxi (2026) [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) |
| 6 — Guardrails | Output filtering only; post-hoc; static; no environmental state conditioning | Shamsujjoha et al. (2025) [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md); Chen, Kang & Li (2025) [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md) |
| 7 — Key insight | Each existing system implements one governance mechanism only; no system unifies both levels under classified environmental state | Ramos et al. (2024) [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md); Newcomb & Ochoa (2026) [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md); Perez-Cerrolaza et al. (2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) |

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
| 1 — Core gap | No system defines both G(S) and A_AI(S) conditioned on the same S = f(E); no intermediate CAUTION mode; no advisory containment A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ ∅ | `justification-novelty-gap.md` §12; four SLR confirmations |
| 2 — Limitation of existing work | Binary safety models universal; no tripartite state classification; no Safety Dominance Property for graduated governance | Newcomb & Ochoa (2026) [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md); Ramos et al. (2024) [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md) |
| 3 — Contribution link | Need a graduated safety-state-gated architecture with unified governance (G(S), A_AI(S)); need evaluation comparing graduated vs. binary governance; need socio-technical evaluation of CAUTION mode | `justification-novelty-gap.md`; `review-plan.md` §2.10 gap statement |

**Source files**: `literature-review-writing-plan.md` §2.11 · `review-plan.md` §2.10 Research Gap Statement · `justification-novelty-gap.md`  
**Closing sentence**: *"Therefore, this research proposes a graduated safety-state-gated architecture for AI decision support that defines how safety conditions govern both AI participation and advisory scope."*

---

## Execution Order

| Round | Section | Status |
|---|---|---|
| 1 | 2.1 AI Decision Support | ⬜ Not started |
| 2 | 2.2 Safety Constraints | ⬜ Not started |
| 3 | 2.3 Human-AI Authority | ⬜ Not started |
| 4 | 2.4 Adaptive Autonomy | ⬜ Not started |
| 5 | 2.5 Guardrails | ⬜ Not started |
| 6 | 2.6 Hybrid AI | ⬜ Not started |
| 7 | 2.7 Low-Resource | ⬜ Not started |
| 8 | 2.8 Fisheries Context | ⬜ Not started |
| 9 | 2.9 Comparative Analysis | ⬜ Not started |
| 10 | 2.10 Literature Summary | ⬜ Not started |
| 11 | 2.11 Research Gap | ⬜ Not started |

---

## Output File

All written sections will be appended to:  
`docs/chapter-2-draft.md`

Each round: write the section → user reviews → update status above → proceed to next.
