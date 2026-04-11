---
layout: document
---

# What Makes This Different? Differentiating the Two-Level Governance Architecture

**Document type**: Theoretical justification / argumentation note  
**For**: Chapter 2 (Literature Review) and Chapter 3 (Architecture Design)  
**Questions addressed**: Q1 — How is this different from existing DSS? Q2 — How is this different from hybrid AI? Q3 — How is this different from adaptive autonomy? Q4 — How is this different from guardrails/safety filters? Q9 — Why is the architecture layered?

---

## 1. The Core Claim

The proposed architecture — a two-level governance pair (G(S), A_AI(S)) conditioned on classified environmental safety state S = f(E) — is structurally distinct from four well-established classes of AI systems that might appear to subsume it: conventional decision support systems, hybrid AI architectures, adaptive autonomy frameworks, and guardrail/safety filter mechanisms.

The distinction is not one of degree (a "better" version of an existing class) but of kind (a different architectural structure addressing a different problem). Each existing class solves a different problem and, critically, none implements the specific architectural mechanism that defines this contribution: environmental-state-conditioned restriction of AI advisory scope as a formal governance layer.

This document examines each class in turn, identifies the structural feature that differentiates the proposed architecture, and concludes with the rationale for the layered design.

---

## 2. How Is This Different from Conventional Decision Support Systems?

### 2.1 What Conventional DSS Do

Decision support systems provide information, analysis, and recommendations to human decision-makers. The canonical DSS architecture comprises a data management component, a model management component, a dialogue/interface component, and optionally a knowledge management component. The human retains decision authority; the system provides decision-relevant information.

The proposed architecture is a DSS in the sense that it provides recommendations to a human fisher who retains full decision authority. But this superficial classification conceals a fundamental structural difference.

### 2.2 The Structural Difference: No DSS Governs Its Own Recommendation Scope

Conventional DSS provide the same types of recommendations regardless of environmental conditions. A weather-informed fishing DSS might warn "conditions deteriorating" and still output departure time estimates, trip duration recommendations, and fishing area suggestions — leaving the human to judge which outputs remain reliable. The recommendation scope is fixed at design time.

The proposed architecture dynamically restricts which *types* of recommendations the AI is permitted to generate based on classified environmental safety state. In CAUTION mode, the AI provides go/no-go and delay guidance but is architecturally prevented from outputting departure times, trip durations, or fishing area recommendations. This is not a display-level filter (hiding information from the user) — it is an architectural constraint on the AI's output space itself.

Madsen & Kim (2024) [[notes]](../notes/A%20state-of-the-art%20review%20of%20AI%20decision%20transparency%20for%20autonomous%20shipping.md), reviewing AI decision transparency for autonomous shipping, document that existing maritime DSS implement colour-coded risk classification (green/amber/red) to display risk information at varying granularity. But they identify a critical gap: "none of the studies identified in this review evaluated how proposed strategies, visualization, or technology affect systems' or individual operators' [situational awareness]." The risk classification conditions the *display* to the human, not the *AI's permitted output types*. The proposed architecture operates at the architectural level — restricting what the AI may produce, not merely what the human sees.

Gao (2024) [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md), documenting Penang fisher decision-making from 25 semi-structured interviews, provides empirical evidence for why fixed-scope DSS are inadequate for this domain. Fishers already differentiate between three operational modes — go, cautious-go, and don't-go — with different decision scopes in each mode: full scope under favourable conditions (timing, location, species, duration), restricted scope under marginal conditions (near-shore only, shortened trips), and no operational decisions under adverse conditions. A DSS that provides the same recommendation types regardless of mode misaligns with the user's own decision structure.

### 2.3 The Formal Distinction

A conventional DSS can be characterised as: given input E, produce recommendations R from a fixed recommendation space R_full. The human decides what to act on.

The proposed architecture is: given input E, classify S = f(E), then produce recommendations R from A_AI(S) ⊆ R_full, where A_AI(S) varies by classified state and the containment property A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ is enforced as a formal invariant.

The difference is the governance layer between environment and AI reasoning. No conventional DSS has this layer. The existence of A_AI(S) as a formal, state-conditioned restriction on recommendation types is the architectural contribution that distinguishes this from any DSS.

---

## 3. How Is This Different from Hybrid AI Architectures?

### 3.1 What Hybrid AI Architectures Do

Hybrid AI architectures combine deterministic (rule-based, symbolic) components with probabilistic (learned, neural) components to achieve both reliability and adaptiveness. The deterministic component provides formal guarantees, domain knowledge enforcement, or structured reasoning; the probabilistic component provides pattern recognition, learning from data, or natural language processing.

The proposed architecture is hybrid in this sense: S = f(E) is a deterministic classification function, and the AI recommendation generator is probabilistic. But hybridness is a structural property, not an architectural contribution. The question is: what does the deterministic component *do*?

### 3.2 The Structural Difference: The Deterministic Component Governs Scope, Not Accuracy

In existing hybrid AI architectures, the deterministic component's purpose is to ensure *accuracy* or *correctness* of AI output. Consider the two most architecturally sophisticated hybrid systems in the corpus:

**Castagnone & Nitti (2026) — SYNAPSE**: A neuro-symbolic architecture for structural engineering where the neural component (LLM) handles interpretation and presentation while the symbolic component (deterministic calculation engine) performs all safety-critical calculations. A four-stage verification protocol (syntactic, semantic, dimensional, regulatory compliance) gates LLM-generated scripts before execution. The deterministic component ensures the AI never performs safety-critical calculations directly. This is a *static* governance arrangement: the LLM's role is permanently fixed regardless of environmental conditions. SYNAPSE does not need dynamic governance because the task does not change. There is no S = f(E); there is no CAUTION mode; the boundary between neural and symbolic is drawn once and enforced uniformly.

**Mussi et al. (2025)**: An interdisciplinary perspective on human-AI interaction in safety-critical network infrastructures (power grids, railway, air traffic management) that identifies the *knowledge-assisted AI* pattern — integrating "human-devised safety constraints into AI models as a foundation of reliability upon which learning-based improvements can build." The hierarchical decision-making pattern decomposes high-level goals into constrained low-level actions. But the governance mechanisms described are design-time architectural choices and organisational function allocation, not runtime state-conditioned governance. There is no formal pipeline. There is no S = f(E). There is no (G(S), A_AI(S)) pair.

Punzi et al. (2024) [[notes]](../notes/AI%2C%20Meet%20Human-%20Learning%20Paradigms%20for%20Hybrid%20Decision-Making%20Systems.md), surveying hybrid decision-making systems across three learning paradigms (Human Overseers, Learning to Abstain, Learning Together), provide the most comprehensive taxonomy of human-AI collaboration architectures. Their formal model defines machine predictor f, human predictor h, and rejection/deferral policy ρ_M — but this formalisation optimises prediction accuracy across agents, not safety state classification or governance functions. The three paradigms govern *who decides* (human or machine), not *what the machine may recommend given current conditions*.

### 3.3 The Formal Distinction

In existing hybrid architectures, the deterministic component constrains the *content* of AI output (is this calculation correct?) or the *authority* allocation (who decides?). In the proposed architecture, the deterministic component constrains the *scope* of AI output (what types of recommendation may the AI generate under current conditions?). This is a categorically different function. The deterministic governance layer does not check whether a departure time recommendation is correct — it determines whether departure time recommendations are *permitted at all* given the classified safety state.

This distinction means the proposed architecture is not a "better hybrid" or an "improved neuro-symbolic system." It is a hybrid architecture that uses its deterministic component for a purpose no prior hybrid architecture addresses: runtime, state-conditioned restriction of AI advisory recommendation types.

---

## 4. How Is This Different from Adaptive Autonomy?

### 4.1 What Adaptive Autonomy Does

Adaptive autonomy frameworks adjust the allocation of decision authority between human and AI based on operational conditions. When conditions are favourable, the AI operates with greater independence; when conditions degrade, authority shifts toward the human. The adjustment governs *who decides* — the balance between human and automation authority.

Ramos et al. (2024) [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md), reviewing 91 papers on collaborative intelligence for safety-critical industries, classify this extensively: supervisor controllers, shared control arbitration, simplex switching, and human intervention during RL training all implement authority redistribution between human and AI without changing the content of what the AI produces. Porter et al. (2025 — INSYTE) formalise this as two orthogonal classification dimensions: Dimension 7 (intervention independence — can AI act without human approval?) and Dimension 8 (oversight independence — can AI operate without human monitoring?). Both dimensions govern authority; neither governs recommendation content.

### 4.2 The Structural Difference: Authority vs. Scope

The proposed architecture does not change decision authority under any safety state. The fisher is always the decision-maker. The AI is always advisory. What changes is the *scope* of what the AI advises on — the set of recommendation *types* it is permitted to generate.

This distinction is precise and non-trivial:

| Governance action | Changes decision authority | Changes recommendation content | Example |
|---|---|---|---|
| **Adaptive autonomy** | Yes — shifts authority from AI to human | No — AI still recommends everything | "AI recommends departure at 06:15; you must now confirm" |
| **Binary gate (shields)** | Yes — removes AI entirely | Yes — by absence | "AI blocked; make your own decision" |
| **Advisory scope restriction** | No — AI remains advisory | Yes — only reliable types | "CAUTION: go/no-go and delay guidance available; no departure time or route recommendations" |

Flehmig et al. (2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md) present the closest adaptive autonomy system to the proposed architecture: a traffic-light degradation index with three levels. At Level 1 (green), AI operates normally. At Level 2 (orange), the supervisory component must conduct thorough checks. At Level 3 (red), the system switches to non-AI backup. This is the first framework for indexing AI degradation in safety-critical systems. But the notes identify the decisive difference: at both Level 1 and Level 2, the AI operates with identical, unrestricted advisory scope. Level 2 changes what the *human supervisor* does — not what the AI may recommend. There is no A_AI(CAUTION) ⊂ A_AI(SAFE). The gap is at Level 2 governance.

Gyllenhammar et al. (2025) [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md) review the MRC/ROD hierarchy in automated driving: ODD → ROD (Restricted Operational Domain) → MRC (Minimal Risk Condition). This is graduated degradation of the *system's operational domain*, not of its *advisory scope*. The ROD restricts what the system may operationally attempt; it does not restrict what types of recommendations the AI generates. The trigger is system degradation, not environmental state classification.

### 4.3 Why This Distinction Matters

Adaptive autonomy without scope restriction exposes humans to unreliable information. The AI still generates precise departure times, trip duration estimates, and route recommendations under degraded conditions — the human must evaluate whether to trust them. Schrills et al. (2025) [[notes]](../notes/Questioning%20Trust%20in%20AI%20Research-%20Exploring%20the%20Influence%20of%20Trust%20Assessment%20on%20Dependence%20in%20AI-Assisted%20Decision-Making.md) demonstrate that communicated system reliability is more influential on user behaviour than the user's own trust assessment: participants anchored their dependence on the instructed reliability level even under conditions where they had independent grounds to doubt it. A precise AI recommendation communicates high reliability implicitly, irrespective of whether that precision is warranted under current conditions. Scope restriction removes this false precision at source.

Wen et al. (2025), analysing 60 real-world accident reports across process control and autonomous vehicles, find that human intervention was ineffective in 83.3% of process control incidents and 66.7% of autonomous vehicle incidents. This confirms that shifting authority to the human without removing unreliable content does not reliably protect against automation bias.

---

## 5. How Is This Different from Guardrails and Safety Filters?

### 5.1 What Guardrails and Safety Filters Do

Guardrails and safety filters constrain AI output — they implement what might be called Level 2 governance (controlling what AI may produce). This is the closest existing category to the proposed architecture's A_AI(S) function.

Shamsujjoha et al. (2025) [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md) contribute the most comprehensive taxonomy: 13 guardrail action types (block, filter, flag, modify, validate, parallel calls, retry, fall back, human intervention, defer, isolate, redundancy, evaluate) across 14 quality attributes and 14 pipeline targets. This is a definitive catalogue of *what governance actions exist*. Chen et al. (2025) [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md) formally define the Guardrail System as an AI pipeline with input module → LLM → output module, where AI Safety Principle I requires Y ∩ Z_i = ∅ — the output space must be disjoint from prohibited output sets.

### 5.2 The Structural Difference: Static Per-Output vs. Dynamic Per-State

Guardrails evaluate individual outputs against static rules. The prohibited set Z does not vary with operational or environmental context. As Chen et al. (2025) [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md) observe: "In all guardrail implementations reviewed, the outcome is binary: the response is either delivered or blocked/rejected. There is no mechanism where AI still participates but with restricted output types."

The proposed architecture restricts recommendation *types* (departure time, trip duration, fishing area) based on classified environmental safety state. This is structurally different in three ways:

1. **Unit of governance**: Guardrails govern individual outputs (is this specific response safe?). The proposed architecture governs the output *space* (which categories of recommendation are permissible under current conditions?). The former is post-hoc filtering; the latter is pre-hoc scope definition.

2. **Conditioning variable**: Guardrails are triggered by output content (does this text contain harmful material?). The proposed architecture is triggered by environmental state (what are current wind/wave/visibility conditions?). These are independent variables — a recommendation can be content-safe but type-inappropriate for current conditions.

3. **Graduation**: Guardrails produce binary outcomes — pass or block. The proposed architecture produces graduated governance through the containment hierarchy A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅. The CAUTION mode is neither full pass nor full block — it is a formally defined intermediate scope.

Chen, Kang & Li (2025 [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md) — SHIELDAGENT) present the most sophisticated per-action guardrail in the corpus: LTL specifications derived from policy documents, verified through Markov Logic Networks and barrier certificates. Each planned action is individually evaluated against safety rules. But the governance remains per-action binary: each action passes or fails. There is no classified environmental state that restricts the *types* of actions the agent may attempt. The agent's action space A is the same regardless of environmental conditions.

Seong, Lim & Yoon (2025 [[notes]](../notes/clguard-extraction.md) — CLGuard) present a context-aware suppression framework for autonomous driving using VLM (OpenCLIP ViT-B/32) semantic scene–action alignment via Contrasting Language Goals (CLG). The suppression policy — suppress($a_t$) if $r_t^{CLG} < \tau_r$ AND ($|\dot{v}_t| > \tau_{acc}$ OR $|\dot{\psi}_t| > \tau_{yaw}$) — is the strongest exemplar of the *Action Suppression* paradigm: individual actions are evaluated post-hoc and either suppressed or permitted. The governance is binary per-action with no intermediate mode. Critically, CLGuard's multi-modal context buffer includes the AI's own recent CLG scores as input, making the semantic evaluation partially self-referential — the AI checks its own outputs rather than an independent external authority classifying the environmental state. There is no S = f(E), no A\_AI(S), and no CAUTION mode where the AI participates under restricted recommendation scope.

Wang et al. (2026 [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md) — AgentSpec) contribute the first framework for systematically enforcing customisable safety constraints on LLM agents at runtime. Rules are three-tuples r = (η_r, P_r, E_r): triggering events, predicates, and enforcement mechanisms. The framework achieves >90% unsafe code execution prevention. But as the analysis confirms: "AgentSpec does not define a state-conditioned admissible action space. It evaluates individual actions against individual rules. There is no formal structure that says 'under safety state S, only recommendation types {R₁, R₂} are permitted.'"

Safety filters in the formal methods tradition share this structure. Bajcsy & Fisac (2024) [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md) present the Human-AI Safety Filter with Theorem 1 guaranteeing the system never enters the failure set. Dalrymple et al. (2024) [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md) define the Guaranteed Safe AI framework where a verifier produces proof certificates. Könighofer et al. (2025) [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md) compute shields from formal specifications. All implement binary per-state or per-action governance: permit or override. None implements an intermediate mode where AI participates under restricted recommendation scope.

### 5.3 The Complementary Relationship

The proposed architecture does not replace guardrails — it provides the *state-conditioned selection mechanism* that determines which governance configuration applies under current conditions. Shamsujjoha et al. (2025) [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md) comprehensively catalogue the governance action space; the proposed architecture determines *when* each governance configuration activates based on S = f(E). The relationship is complementary: guardrails define the toolkit; the governance pair determines which tools apply in which state.

### 5.4 Examiner Question: "Why Not Just Use a Standard Output Filter?"

A common examiner challenge: "Your CAUTION mode restricts what the AI can recommend — why not achieve the same result with a post-hoc output filter that blocks certain recommendation types under elevated conditions?"

The answer operates at three levels: structural, computational-theoretic, and governance-architectural.

**1. Structural: Post-hoc filtering is the wrong unit of governance.** A standard output filter evaluates individual outputs after the AI has generated them. The proposed architecture restricts recommendation *types* before generation — it defines the admissible output space A_AI(S) that the AI reasons within. This is the difference between a security guard checking IDs at the door (post-hoc) and an invitation list that determines who is told about the event (pre-hoc). Post-hoc filtering allows the AI to expend reasoning on recommendation types that will be discarded, and — critically — the AI's internal reasoning is shaped by the expectation of producing those outputs. Removing the output does not undo the reasoning distortion.

**2. Computational-theoretic: Binary output constraints provably reduce AI capability.** Banerjee et al. (2025) [[notes]](../notes/CRANE-%20Reasoning%20with%20Constrained%20LLM%20Generation.md) provide the strongest formal result on this point. Their Proposition 3.1 proves via circuit complexity that constraining an LLM's output to conform to a grammar G during reasoning reduces the model's expressivity to TC⁰ — the complexity class of constant-depth threshold circuits. This means the model loses the ability to perform multi-step reasoning chains while its output is grammatically constrained. A standard output filter that applies binary pass/block to AI outputs operates in exactly this regime: it constrains what the AI may produce without providing a mechanism for the AI to reason unconstrained. CRANE's solution — the augmented grammar G_a = R_M·G, which alternates unconstrained reasoning segments with constrained output segments — demonstrates that the architecture of constraint matters, not just its presence. Simply filtering outputs post-hoc imposes exactly the capability reduction that Proposition 3.1 identifies. The proposed architecture avoids this by defining A_AI(S) as the *reasoning space*, not a post-hoc filter on outputs generated in an unrestricted space.

**3. Governance-architectural: Output filters are not state-conditioned.** A standard output filter applies the same filtering rules regardless of environmental conditions. The filter's prohibited set Z is static — it does not vary with S = f(E). The proposed architecture's A_AI(S) is fundamentally dynamic: the set of permitted recommendation types changes as the classified safety state changes. Under SAFE, departure time recommendations are permitted; under CAUTION, they are excluded — not because the content is unsafe in an absolute sense, but because the AI's reliability for that recommendation type is degraded under current environmental conditions. No standard output filter implements this state-conditioned scope variation, because output filters evaluate content properties (is this harmful? is this factual?) rather than reliability properties conditioned on external environmental state.

**4. Computational efficiency in low-resource deployment.** In edge-deployed, battery-limited, compute-scarce environments, a post-hoc filter wastes inference cycles generating recommendations that will be discarded. Under CAUTION conditions, where the majority of recommendation types are unreliable, the filter would discard most of what the AI generates. Pre-hoc scope restriction via A_AI(S) avoids this waste entirely — the AI only reasons about permitted recommendation types. Corsi et al. (2024) [[notes]](../notes/Verification-Guided%20Shielding%20for%20Deep%20Reinforcement%20Learning.md) demonstrate the same principle: region-selective shielding reduces overhead by 25–71% by avoiding unnecessary shield computation. See `justification-low-resource-environments.md` §2.4 for the full computational efficiency argument.

The combined answer: a standard output filter would need to (a) operate pre-hoc rather than post-hoc to avoid both capability reduction (Banerjee et al., 2025 [[notes]](../notes/CRANE-%20Reasoning%20with%20Constrained%20LLM%20Generation.md), Proposition 3.1) and compute waste in low-resource settings, (b) condition its filtering on classified environmental safety state rather than static content rules, and (c) implement graduated scope restriction rather than binary pass/block. A filter that did all three would no longer be a "standard output filter" — it would be the proposed governance architecture.

---

## 6. Why Is the Architecture Layered?

### 6.1 The Three-Layer Structure

The proposed architecture separates into three layers:

```
Layer 1: Environment/Sensor → E = {w, r, m, o, v, t}
Layer 2: Governance        → S = f(E) → (G(S), A_AI(S))
Layer 3: AI Reasoning      → AI(E) ⊆ A_AI(S) → Recommendations
```

This layering is a deliberate architectural choice, not a convenience of exposition. Each layer has a different computational character, a different assurance basis, and a different failure mode.

### 6.2 Why Layering Is Necessary

**Independence of governance from AI**: The governance layer (Layer 2) is deterministic. S = f(E) is a rule-based classification function operating on physical sensor inputs. It does not depend on the AI reasoning layer (Layer 3) for any input or assessment. This independence means governance functions even if the AI model is degraded, unavailable, or adversarial. Bloomfield & Rushby (2025) [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md) identify this as the defining property of *assuredly guarded* systems: guards that "do not themselves use AI/ML and can therefore be assured conventionally." A non-layered architecture — where AI reasoning and governance are interleaved — cannot satisfy this independence requirement.

**Different assurance regimes**: Layer 2 (deterministic governance) can be verified using conventional software engineering methods — static analysis, formal proofs, exhaustive testing of a finite classification function. Layer 3 (AI reasoning) requires the probabilistic, statistical, and empirical assurance methods that the safety-critical AI literature has developed. Perez-Cerrolaza et al. (2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) document this distinction through their Class I/II/III taxonomy: Class I systems (fully amenable to formal verification) have different assurance obligations than Class II systems (requiring compensatory safety bags). Layering allows the governance function to be in Class I (formally verifiable) while the AI reasoning remains in Class II (empirically validated with safety bag protection) — the governance layer *is* the safety bag.

**Causal flow alignment**: The layering mirrors the causal structure of the problem. Environmental conditions (Layer 1) cause real-world danger — they are causally upstream of all other signals. Safety state classification (Layer 2) translates environmental conditions into governance mode. AI recommendations (Layer 3) are generated within the scope permitted by governance. The causal flow is unidirectional: Environment → Governance → AI. There is no feedback from Layer 3 to Layer 2 — AI does not influence its own governance. Dalrymple et al. (2024) [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md) specify this independence requirement in their GS AI framework: the world model and safety specification must be independent of the AI policy, so that the verifier's guarantee is not circular. Bajcsy & Fisac (2024) [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md) prove their safety filter guarantee (Theorem 1) under the analogous requirement that the safety monitor be computed independently of the task policy. The layered architecture satisfies both requirements structurally.

**Formal property provability**: The Safety Dominance Property AI(E) ⊆ A_AI(S) is provable precisely because the layers are separated. The proof proceeds: (1) show that f(E) correctly classifies E into S for all E in the input domain; (2) show that A_AI(S) is well-defined for each S; (3) show that the AI output R is constrained to A_AI(S) by the governance layer. If governance and AI reasoning were interleaved, step (3) would require reasoning about the joint behaviour of deterministic and probabilistic components — a significantly harder formal problem. Newcomb & Ochoa (2026) [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md), reviewing 46 formal methods studies for safety-critical ML, confirm that all formal safety guarantees depend on clean separation between the safety mechanism and the system being governed. Layering provides this separation by construction.

### 6.3 Layering in Existing Safety-Critical Practice

The layered pattern is not novel in safety engineering — it is the standard approach in mature safety-critical domains:

| Domain | Layers | Source |
|---|---|---|
| Nuclear power | Operational control → Limitation system → Shutdown system | Bloomfield & Rushby (2025) [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md) |
| Automotive (ADS) | Perception → Planning/Safety monitor → Control | Gyllenhammar et al. (2025) [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md) |
| Aviation (fly-by-wire) | Pilot input → Envelope protection → Actuator | Standard aviation practice |
| SAFEXPLAIN | AI component → Supervision function → Safety control | Abella et al. (2025) [[notes]](../notes/SAFEXPLAIN-%20a%20Complete%20Approach%20Towards%20Trustworthy%20AI-Based%20Safety-Critical%20Systems.md) |
| Proposed architecture | Environment sensing → Governance (G(S), A_AI(S)) → AI reasoning | This work |

The contribution is not layering itself — it is what the governance layer *does*: state-conditioned restriction of AI advisory recommendation types. No prior layered architecture implements this specific governance function.

---

## 7. Comparative Summary Table

| Feature | Conventional DSS | Hybrid AI | Adaptive Autonomy | Guardrails/Safety Filters | Proposed Architecture |
|---|---|---|---|---|---|
| **Governs recommendation scope by state?** | No — fixed scope | No — fixed role allocation | No — changes authority, not scope | No — per-output, not per-state | **Yes — A_AI(S) varies by S** |
| **Environmental state classification?** | No | No | Partial (system degradation, not environment) | No | **Yes — S = f(E)** |
| **Intermediate governance mode?** | No | No | Partial (Flehmig: supervisory intensity only) | No — binary pass/block | **Yes — CAUTION mode** |
| **Formal containment property?** | No | No | No | No | **Yes — A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ ∅** |
| **Deterministic governance independent of AI?** | N/A | Partial (verification is deterministic but static) | No — often AI-assessed | Partial (some rule-based) | **Yes — f(E) is deterministic, non-AI** |
| **Runtime state-conditioned?** | No | No | Partial (Flehmig: runtime; Gyllenhammar: design-time) | No — static rules | **Yes — continuous runtime reclassification** |
| **What the deterministic component does** | N/A | Ensures output correctness/accuracy | Adjusts authority allocation | Filters individual outputs | **Restricts recommendation type scope** |
| **Key prior works** | Traditional DSS literature | SYNAPSE (Castagnone & Nitti, 2026); Mussi et al. (2025) | Flehmig et al. (2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md); Gyllenhammar et al. (2025) [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md) | Shamsujjoha et al. (2025) [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md); Chen et al. (2025) [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md); SHIELDAGENT (Chen, Kang & Li, 2025) [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md) | This work |

---

## 8. One-Paragraph Summary (for use in Chapter 2 or 3)

> The proposed two-level governance architecture — (G(S), A_AI(S)) conditioned on S = f(E) — is structurally distinct from four established classes of AI systems that partially address the same problem space. Conventional DSS provide the same recommendation types regardless of environmental conditions; the proposed architecture dynamically restricts which types of recommendations the AI is permitted to generate based on classified safety state, a gap confirmed in the maritime DSS literature by Madsen & Kim (2024) [[notes]](../notes/A%20state-of-the-art%20review%20of%20AI%20decision%20transparency%20for%20autonomous%20shipping.md). Hybrid AI architectures (Castagnone & Nitti, 2026; Mussi et al., 2025; Punzi et al., 2024 [[notes]](../notes/AI%2C%20Meet%20Human-%20Learning%20Paradigms%20for%20Hybrid%20Decision-Making%20Systems.md)) use deterministic components to ensure output *accuracy* or allocate *authority* between human and machine; the proposed architecture uses its deterministic component for a categorically different purpose — restricting the *scope* of AI advisory output at runtime. Adaptive autonomy frameworks (Flehmig et al., 2024 [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md); Gyllenhammar et al., 2025 [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md); Ramos et al., 2024 [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md)) adjust who decides but not what the AI recommends: Flehmig's traffic-light framework, the closest structural precedent, changes supervisory intensity at Level 2 but leaves AI advisory scope identical across Levels 1 and 2. Guardrails and safety filters (Shamsujjoha et al., 2025 [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md); Chen et al., 2025 [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md); Wang et al., 2026 [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md); SHIELDAGENT: Chen, Kang & Li, 2025 [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md); Bajcsy & Fisac, 2024 [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md); Dalrymple et al., 2024 [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md); Könighofer et al., 2025 [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md)) constrain individual AI outputs against static rules but do not condition the permitted output *space* on classified environmental state — producing binary pass/block outcomes rather than graduated scope restriction. The architecture is layered — Environment → Governance → AI Reasoning — because governance must be independent of the AI it governs (Bloomfield & Rushby, 2025 [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md)), differently assurable (Perez-Cerrolaza et al., 2024 [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md)), causally aligned with the problem structure (Dalrymple et al., 2024 [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md); Bajcsy & Fisac, 2024 [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md)), and formally separable to enable proof of the Safety Dominance Property (Newcomb & Ochoa, 2026 [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md)). No prior work in any of these four classes implements the specific mechanism that defines this contribution: environmental-state-conditioned, formally guaranteed restriction of AI advisory recommendation types through a unified governance pair.
