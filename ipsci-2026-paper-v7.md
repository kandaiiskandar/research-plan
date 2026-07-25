A Graduated Safety-State-Gated Architecture for AI Decision Support

Abstract— How should AI advisory behaviour adapt as operational conditions deteriorate? Existing governance mechanisms are uniformly binary: the AI either generates its full recommendation set or is blocked entirely. This paper reviews the AI governance, runtime assurance, human-AI collaboration, and low-resource deployment literature to determine whether existing architectures restrict AI advisory scope as environmental risk increases and to motivate a new governance architecture. Mechanistic studies reveal three limitations: the inference pipeline is structurally fixed, reasoning exploration is a property of the decoding procedure rather than a content-conditioned adaptation, and self-assessed confidence is unreliable and insensitive to past performance. Large-scale systematic reviews found that none of the reviewed architectural tactics demonstrated a formally positive impact on safety, while the most comprehensive guardrail taxonomy contains no mechanism for restricting advisory scope based on environmental risk. Binary governance therefore leaves intermediate-risk conditions structurally unaddressed: operators in low-resource environments receive either full-scope tactical recommendations or none at all. To address this gap, we propose a graduated safety-state-gated architecture, in which a participation gate and an AI advisory gate, both conditioned on the environmental safety state, produce an intermediate caution mode with formally restricted advisory scope. The proposed architecture is illustrated through a small-scale coastal fisheries deployment context.

Keywords—AI governance, safety-critical systems, decision support, graduated architecture, coastal fisheries

# Introduction

AI decision support is expanding into safety-critical, human-in-the-loop settings across domains including healthcare, industrial operations, autonomous transportation, and maritime activity. In these settings the AI does not act autonomously: it generates recommendations that a human decision-maker weighs and acts upon. Governance frameworks for such systems determine when the AI may participate in a decision and what safeguards surround its output. The governance that accompanies this expansion, however, is under-delivered in practice: in the largest survey of responsible AI adoption to date (1,000 organisations across 20 industries and 19 regions), Reuel et al. found that while 9% of organisations reach the highest stage of organisational AI governance maturity (policies, structures, risk processes), only 0.8% reach it operationally, and none reach both, a systematic gap between governance planning and execution that the authors warn "could lead to increased (public) risks from AI systems" [31]. Governance that depends on organizational processes being faithfully executed cannot, on this evidence, be relied upon; the burden of safety therefore falls on the architecture of the AI system itself. Yet a fundamental architectural question remains unresolved: how should AI advisory behaviour change as operational conditions deteriorate from safe, through marginal, to dangerous?

Existing frameworks address only the endpoints of this continuum: full recommendation generation or complete shutdown. The intermediate range is unaddressed. When binary-gated architectures encounter marginal conditions, they treat them as structurally safe, permitting full-scope tactical advice such as precise departure intervals; operators receiving full-scope AI output under deteriorating conditions tend toward over-reliance, accepting recommendations the environmental data can no longer reliably support [4]. This review examines one specific component of the governance problem: whether any existing mechanism restricts what an AI may recommend, as distinct from whether the AI may participate at all.

The question matters most in low-resource, safety-critical domains, those furthest from the well-resourced organizations where even partial governance maturity is concentrated [31]. In such settings there is no institutional layer, no control room, supervisor, or compliance function, to compensate for a governance failure in the tool itself: whatever governance the system embodies is all the governance the operator has. Each morning, small-scale fishers along Malaysia's coastline face a safety-critical decision: go to sea or stay ashore. They make this decision alone, without institutional support, on vessels under 40 gross register tonnage restricted to 0–5 nautical miles from shore, relying on traditional weather knowledge that is eroding as climate patterns become less predictable [1].

Runtime governance frameworks determine whether AI may participate in a decision. Autonomy research determines which actions an autonomous agent may execute. Neither addresses what AI may recommend to a human decision-maker as operating conditions deteriorate. This paper takes up that third question.

Five concepts are defined here to fix terminology. An AI decision support system generates recommendations for a human decision-maker who retains final decision authority; it is distinct from an autonomous agent, which executes actions directly. A safety-critical system is one in which incorrect or inappropriately scoped output can contribute to harm to human life, health, or property. Runtime governance refers to mechanisms that constrain AI behaviour during operation, as distinct from design-time controls such as training, fine-tuning, or static configuration. Within runtime governance, this paper separates two dimensions: participation gating (whether the AI participates in the decision at all) and advisory scope (A_AI(S)): the set of recommendation types the AI is permitted to generate while participating. Advisory scope restriction is the contraction of A_AI(S) (dimension 2, Fig. 1). Finally, an environmental safety state is a classified summary S of an environmental observation vector E, produced by a classification function S = f (E) that is computed independently of the AI component; a low-resource environment is a deployment context lacking reliable connectivity, computing infrastructure, and institutional support, imposing offline-first and computationally lightweight requirements on any deployed system.

Fig. 1. Three governance dimensions in AI decision support systems. Dimensions 1 and 3 appear in existing work; dimension 2 is the gap this paper addresses.

```
Governance Dimension 1 — Participation
Whether the AI may operate
(addressed by: shields, safety filters, binary gates)

          ↓

Governance Dimension 2 — Advisory Scope          ← this paper
What the AI is permitted to recommend
(the admissible recommendation space A_AI(S))

          ↓

Governance Dimension 3 — Execution
Which actions an autonomous agent may take
(addressed by: action-class restriction, autonomy levels)
```

The paper makes two contributions. First, it establishes from a structured literature review of 72 core papers, supplemented by three large-scale systematic reviews collectively covering 532 primary references, that existing architectures govern whether the AI participates, but not what it may recommend as conditions deteriorate (a gap confirmed from four independent bodies of literature and developed fully in the Synthesis section) and shows, from mechanistic evidence on how generative AI systems process information, why this gap cannot be closed within the AI component itself. Second, it outlines a graduated safety-state-gated governance architecture that the identified gap implies. The Literature Review section covers existing governance paradigms, a cross-paradigm synthesis characterising the gap, and the mechanistic basis for external governance. The Proposed Architecture section outlines the architecture the gap implies, and the Conclusion closes.

# Methodology

This study adopts a Structured Literature Review (StLR) approach, structured rather than systematic: search and coding are disciplined, but the scope is purposive, covering only the bodies of literature where such a mechanism could plausibly appear. The central question is whether any existing architecture restricts an AI system's advisory scope as a function of classified environmental safety state. A systematic review promises completeness and reproducibility; this one promises analytical rigour and transparent reasoning, and is held to that standard.

## Search Strategy

Papers were retrieved from Scopus, IEEE Xplore, Web of Science, and ACM Digital Library using search strings including AI governance, runtime assurance, safety filter, advisory scope, decision support, human-AI collaboration, autonomy levels, guardrails, action restriction, and AI safety-critical; secondary searches used fisheries AI, maritime decision support, and low-resource AI deployment. Three large-scale systematic reviews within the initial candidate set were retained as secondary evidence: Indykov et al. [5] (206 papers, 16 architectural tactics), Shamsujjoha et al. [6] (13 guardrail actions across 32 agent studies), and Perez-Cerrolaza et al. [24] (294 references). Papers were added through citation tracing until no new governance mechanisms emerged. 72 papers proceeded to full review.

## Screening, Inclusion, and Coding

Screening proceeded in two stages. At the title and abstract stage, a paper was included if it addressed a mechanism that constrains or shapes AI behaviour during operation, targeted a safety-critical or human-in-the-loop context, or addressed AI deployment in low-resource or resource-constrained environments. Papers dealing only with training-time, fine-tuning, or static-configuration approaches with no runtime governance component were excluded. 72 papers were retained for full review, each coded on the following four dimensions (TABLE I). Table II in the Adaptive Risk-Based Systems section presents the full coding of all frameworks that implement graduated adaptation.

The four dimensions were derived by decomposing the central research question: a mechanism that restricts AI advisory scope based on environmental safety state would need to target advisory scope, use graduated adaptation, condition on environmental state, and produce a formally bounded output set. Each requirement corresponds to one dimension; a paper coded Yes on all four would constitute a prior instance of the proposed mechanism.

**Table I.** Coding dimensions applied to all reviewed papers.

| Dimension | Values |
|---|---|
| **Primary governance target** | Participation / Advisory scope / Execution / Oversight |
| **Runtime adaptation** | Binary (on/off) / Graduated (3+ levels) / None |
| **Conditioning variable** | Environmental state / AI robustness / Task risk / Human authority / None |
| **Recommendation restriction** | Yes (bounded output set) / No |



## Theme Development and Synthesis

Papers sharing a governance topology (the same combination of governance target and conditioning variable) were grouped into themes. This produced three governance paradigms (deterministic safety constraints, authority allocation frameworks, adaptive risk-based systems) and one application-domain body (fisheries and low-resource deployment), reviewed in the subsequent sections.

Within each paradigm, papers were compared against the four coding dimensions to establish the paradigm's collective posture. The Synthesis section synthesises across them, tracing where all four dimensions point to the same absence. The closest structural precedents (papers that graduated some aspect of AI behaviour across three or more levels) were examined in greater detail to establish why they still did not satisfy dimension (d).



# Literature Review

## Overview of Existing Governance Paradigms

Existing AI governance frameworks in safety-critical systems fall into three paradigms: deterministic safety constraints (provable runtime guarantees by blocking unsafe behaviour), authority allocation frameworks (distributing decision rights between human and AI), and adaptive risk-based systems (varying behaviour across graduated operational levels). Across all three, the reviewed frameworks target participation, authority allocation, or execution; advisory scope remains outside their governance targets. A fourth body (fisheries AI and low-resource deployment) is reviewed to establish whether the pattern persists in the application domain. The review methodology is described in the Methodology section and summarised in Fig. 2.



Fig. 2. Conceptual review process: from research question to proposed architecture. The Search Strategy, Screening, and Theme Development steps trace the gap through the literature; the Mechanistic Basis section shows why it cannot be closed at the AI-component level; the Proposed Architecture section proposes the architecture the gap calls for.

```
Research Question
(Does any architecture restrict AI advisory scope
 as a function of environmental safety state?)
                    │
                    ▼
         Database Search
         Scopus · IEEE Xplore · Web of Science · ACM DL
                    │
                    ▼
         Screening & Inclusion
         72 papers retained
                    │
                    ▼
         Four-dimension Coding
         Primary governance target · Runtime adaptation ·
         Conditioning variable · Output restriction
                    │
                    ▼
         Theme Development
         Three paradigms + application domain
         (Literature Review)
                    │
                    ▼
         Cross-paradigm Synthesis
         All four coding dimensions converge
         on the same absence
                    │
                    ▼
         Mechanistic Evidence
         Gap cannot be closed within the AI component
                    │
                    ▼
         Proposed Architecture
         G(S) + A_AI(S) — graduated governance pair
```

## Deterministic Safety Constraints: Binary by Construction

Könighofer et al. formalise shields: runtime mechanisms that intercept AI actions before they reach the environment [8]. Dalrymple et al. propose Guaranteed Safe AI, requiring formal proof certificates before AI output is deployed [9]. Bajcsy and Fisac implement a control-theoretic safety filter [10]. All three share the same governance topology: the AI either operates within its safety boundary or is replaced. The most recent extension, Pro2Guard, adds predictive foresight (learning a Markov Chain of agent behaviour to intervene before violations occur [34]), but the governance topology is unchanged: the object of governance remains execution, and nothing conditions what the AI may recommend. Shielding variants such as verification-guided shielding [11] and SAFEXPLAIN [12] confirm the same binary topology. None of the papers in this body addresses the semantic content of AI output.

## Authority Allocation: Who Decides, Not What AI May Recommend

Authority allocation frameworks ask who decides rather than what the AI may recommend. Ramos et al., reviewing 91 collaborative intelligence studies, find AI-assisted decision-making dominant across safety-critical industries, but no system varies advisory scope by safety state [13]. Feng, McDonald, and Zhang propose five autonomy levels, but both dimensions are configured at design time [14]. At cross-domain scale, Mussi et al. identify every ingredient of state-conditioned governance across power grids, railway networks, and air traffic management, yet assemble none into a runtime model: automation levels remain fixed at design time [33]. The reviewed frameworks in this body fix advisory scope at design time, regardless of how operational conditions evolve. The adaptive risk-based literature shows that graduated runtime adaptation is technically feasible, but applies it to a different dimension.

## Adaptive Risk-Based Systems: The Closest Precedents

Flehmig et al. propose a three-level traffic-light degradation index (green/orange/red) that classifies AI operational status and triggers different supervisory responses per level [7]. At red, control is transferred to a conventional non-AI backup system, functionally removing the AI from the decision loop; at orange, supervisory checks intensify. The AI's advisory scope, however, is identical at green and orange: the intermediate level governs human supervisory behaviour, not AI recommendation content. The authors themselves state: "To our knowledge, there is currently no existing framework or method for indexing AI degradation in safety-critical systems in such a manner" [7]. The three-level design is novel by the authors' own account, yet it stops short of using the intermediate level to restrict AI output. Baxi formalises a K-tier permission architecture where permission sets vary by tier, but tiers are determined by the AI's own verified robustness, not by classified environmental state [15]. Vermaelen and Holvoet's Tumato 2.0 gates autonomous robot behaviour through an allowed(a,s) predicate, but as an absolute execution toggle: an action is either completely permitted or entirely blocked [16]. 

Three 2026 architectures extend this adaptive line and constitute the contemporary state of the art. Contemporary architectures attempting to move beyond binary governance typically deploy an intermediate mode to graduate the system's operational posture; structural analysis reveals, however, that these frameworks graduate human workflows or physical behaviours, leaving the semantic boundaries of AI generation unconstrained. The reviewed architectures cluster into three distinct paradigms.

#### Oversight intensification. Flehmig et al.'s traffic-light index [7] and Kang's Governed AI-Assisted Engineering (GAIE) framework [25] graduate the intensity of human supervisory auditing. GAIE routes agentic code generation tasks through three oversight tiers via a deterministic classification model with monotonicity, fail-safety, and totality properties established by construction. In its intermediate Human-over-the-Loop tier, the human workflow transitions to a deployment-gate check, yet the underlying coding agent continues to generate full-scope, unconstrained code artifacts at every tier [25].

#### Execution deferral and re-sensing. In embodied robotics, Ghaleb et al. implement a three-regime uncertainty-calibrated gating wrapper (Safe to proceed, Borderline, Unsafe to proceed) driven by calibrated runtime failure risk [27]. On entering the intermediate Borderline regime, the framework forces an execution slowdown and triggers a re-observation loop capturing alternative camera viewpoints, but the vision–language–action policy's output capability remains completely uncontracted; at Unsafe, the learned policy is disengaged entirely in favour of a classical planner. 

#### Autonomous action-class restriction. The closest behavioural precedent is Sahoo's Agentic Military AI Governance Framework (AMAGF), which leverages a real-time Control Quality Score (CQS) to dynamically throttle an autonomous agent's tool access across five response levels [26]. At intermediate CQS levels (0.4–0.6), the agent is programmatically restricted to reversible actions only. While this represents a genuine graduated contraction of AI behaviour, it governs the execution space of an acting autonomous agent, is conditioned on measured control degradation rather than classified environmental state, and specifies its restriction levels as procedural bands over a continuous score rather than formally enumerated admissible sets with a proven containment property. Whether the formal apparatus used here, procedural bands over a continuous score, could be adapted to produce formally bounded recommendation menus for human-facing decision support is an architectural question the reviewed literature leaves open.



Across all three paradigms, a state-conditioned, formally bounded recommendation menu AAI(S) for a human decision-maker has not been identified in the reviewed literature. Graduated operational posture is technically feasible; the gap is in where the graduation is applied. Intermediate governance levels target human workflows, execution deferral, or agent action classes, not the semantic content of AI output. The next section examines whether this pattern persists in the application domain.

## Fisheries and Low-Resource Deployment: The Gap Persists in the Application Domain

The application domain carries a measurable environmental risk profile. Dominguez-Péry et al., analysing 504 IMO maritime accident reports (2011–2021), found wind, weather, and visibility form the largest single risk cluster (26.7%), and small vessels record the highest mean fatality rank (p = 0.01) [2]. Atacan and Düzbastılar found that combined night navigation and heavy weather produces the highest accident consequence scores across all tested conditions (mean 37.03) [3].

Against this risk profile, the domain's AI literature shows the same governance pattern. Haque and Al Jufaili confirm that no fisheries AI system implements formal advisory scope restriction conditioned on environmental state [17]. Rahim et al. document that the only external advisory available to coastal fishers is a binary government warning to stop fishing [18]. Katende identifies safety governance as a systematic gap in low-resource AI deployment: it has not been designed from the deployment floor [19]. Longobardi et al. demonstrate that analytics are achievable in data-deficient fisheries contexts [20]; Bhuvaneswari et al. show lightweight AI for safety-critical decisions is feasible in resource-constrained settings [21]. Together, the literature establishes deployment feasibility and documents the risk profile, but provides no formal runtime governance architecture. The absence observed across the three governance paradigms thus extends to the application domain where the consequences are most direct.

## Synthesis: Cross-Paradigm Comparison and the Research Gap

Comparing across all four bodies reveals a consistent pattern: deterministic constraints prioritise provable safety over flexibility and remain binary by construction; authority allocation frameworks graduate human decision rights but leave AI output untouched; adaptive risk-based systems graduate operational posture but divert their intermediate levels away from advisory content; and the fisheries/low-resource literature demonstrates deployment feasibility without any formal governance architecture at all. Prior research thus provides robust mechanisms for whether the AI operates (participation gating) and which actions an autonomous agent may execute (action-class restriction), but not for what the AI is permitted to recommend to a human decision-maker under deteriorating environmental conditions.

**Table II.** Coding of reviewed architectures against the four governance dimensions (see Table I). The proposed architecture is the only framework in the corpus that targets advisory scope and formally bounds the output set a human decision-maker may receive, conditioned on environmental safety state.

| Framework | Governance target | Conditioning variable | Runtime adaptation | Intermediate mode variable | AI status at max risk | Output restriction |
|---|---|---|---|---|---|---|
| Shields [8], Guaranteed Safe AI [9], safety filter [10] | Participation | Safety boundary | Binary (on/off) | None | Blocked | No |
| Tumato 2.0 [16] | Execution | Constraint predicate | Binary per action | None | — | No |
| Pro2Guard [34] | Execution | Predicted unsafe-state probability | Binary (threshold-triggered) | None (intervention mode set at design time) | Execution halted | No |
| Flehmig et al. traffic-light [7] | Oversight | AI degradation index | Graduated (3 levels) | **Human** supervisory intensity | Control → non-AI backup | No |
| Kang GAIE [25] | Oversight | Task regulatory impact | Graduated (3 tiers) | **Human** audit and approval | Full scope, human-in-the-loop gated | No |
| Ghaleb et al. safety gate [27] | Execution | Epistemic uncertainty | Graduated (3 regimes) | **System** re-sensing loop | Switched to classical planner | No |
| Sahoo AMAGF [26] | Execution | Control quality score | Graduated (5 bands) | **Agent** reversible actions only | Autonomy disablement | No (action classes only) |
| Baxi K-tier [15] | Execution | AI robustness (verified) | Graduated (K tiers) | **Agent** permission set | — | No (economic actions) |
| **Proposed architecture** | **Advisory scope** | **Environmental safety state** | **Graduated (3 states)** | **AI** admissible recommendation space | Disabled (G(S) = 0, A_AI(UNSAFE) = ∅) | **Yes** (A_AI(CAUTION) = {Go, Delay}) |

*Shamsujjoha et al.'s Swiss Cheese Model [6] describes 13 guardrail actions applied to agent artifacts (prompts, plans, tools, FMs) and pipeline stages. All actions are content-focused (block, filter, flag, modify, validate); none condition AI advisory scope on environmental safety state.*

Four independent literature streams confirm this same absence. First, Indykov et al. [5] (16 architectural tactics across 206 papers), Shamsujjoha et al. [6] (13 guardrail actions across 32 agent studies), and Perez-Cerrolaza et al. [24] (294 references across safety-critical domains) record no mechanism that conditions the internal semantic boundaries of an AI's advisory scope on an environmental safety state. Indykov et al.'s trade-off matrix records a Safety score of zero for AT11 (rule-based models): despite Safety being one of the two most frequently cited quality attributes, no architectural tactic has demonstrated a formally positive impact on it [5]. Shamsujjoha et al.'s Swiss Cheese Model identifies 13 guardrail actions and 14 quality attributes, yet their "context-dependent" rules refer strictly to static deployment parameters (e.g., organisational policy, user location, regulatory jurisdiction), not dynamic environmental risk [6]. This absence extends beyond architectures to governance systems themselves: Attard-Frost and Lyons' empirical mapping of a national AI governance system, spanning 610 topics from expert interviews, contains no runtime state-conditioned advisory scope concepts; guardrails appear only in binary framing [22]. Even where governance is planned, it is not executed: Reuel et al.'s 1,000-organisation survey documents a systematic planning–execution gap in which formal AI governance structures exist but operational implementation lags [31], reinforcing the case for governance properties enforced by construction, as architectural invariants, rather than through organisational process. The pattern extends to the governance literature's own analytical categories: Batool et al.'s systematic review of 28 AI governance studies finds coverage fragmentary (only three studies address who governs, what, when, and how) and defines the temporal dimension of governance entirely over the AI development life cycle (pre-, during-, and post-development), so that governance conditioned on runtime operational state falls outside the field's own review vocabulary [36].

Second, within the adaptive risk-based systems literature, intermediate governance tiers are consistently diverted away from output scope across the reviewed systems: Flehmig et al. [7] and Kang [25] use intermediate tiers to escalate human audit workloads, whereas Ghaleb et al. [27] leverage them to trigger temporal execution deferrals and physical re-sensing. Third, while behavioural architectures such as Sahoo's [26] implement intermediate restrictions, they throttle the execution capabilities of acting autonomous agents rather than the recommendation menu of a decision-support tool. Fourth, the fisheries and low-resource deployment literature [17], [18], [19] lacks any formal runtime governance architecture entirely. 

A consistent misalignment appears in the variables used to condition runtime governance gates: Baxi conditions on AI robustness [15], Flehmig et al. on AI degradation [7], Kang on task regulatory impact [25], Sahoo on human-agent control quality [26], and Ghaleb et al. on epistemic model uncertainty [27]. All gate behaviour on properties internal to the AI system. Even the most adaptive strand of governance theory (Engin and Hand's dimensional governance [32]) defines its dimensions as properties of the human-AI relationship, not the operator's physical environment. The proposed architecture conditions its constraints on an independently classified environmental safety state (S = f(E)). 

Across the 72 reviewed papers, prior work addresses adjacent governance dimensions (participation, oversight intensity, execution deferral, and action classes), while an admissible recommendation space that contracts as a function of environmental safety state has no equivalent in any of the surveyed paradigms. The operational consequence is concrete: during marginal conditions, the human operator receives full-scope tactical recommendations at the moment when the underlying data can no longer support them, with no architectural signal that anything has changed [4].

## The Mechanistic Basis for External Governance

Can the AI component itself be expected to narrow its advisory scope as conditions deteriorate, making external governance unnecessary? Evidence from the LLM systems and cognition literatures (external to the governance corpus reviewed above) indicates it cannot be relied upon to do so, at any of the three points where such self-restraint would have to arise.

### Fixed inference pipeline

LLM inference runs through two fixed phases: a compute-bound prefill phase that processes the input, and a memory-bandwidth-bound decode phase that generates tokens autoregressively. Serving-level decisions (batching, scheduling, kernel selection) are driven by token counts and hardware utilisation, not by the semantic content or operational risk of the input [28]. The pipeline has no hook at which advisory behaviour could be conditioned on environmental safety state.

### Reasoning dynamics are not risk-adaptive

Probing studies of reasoning LLMs show that reasoning breadth is a property of the decoding procedure, not a function of input content. Wu et al. find that even when inputs carry full probability distributions over concepts, models collapse onto the single highest-probability component at each step, in a self-reinforcing greedy pattern, and exploration is restored only by externally injected, undirected randomness [29]. Undirected randomness can scatter reasoning, but it cannot produce systematically more conservative advice under deteriorating conditions.

### Self-assessed uncertainty is unreliable and non-learning

Across five studies comparing four LLMs with human participants, Cash et al. find that LLM confidence judgments are poorly calibrated, biased toward overconfidence, and (for the models tested most extensively) insensitive to past performance [30]. Unlike human participants, ChatGPT and Gemini failed to improve calibration after completing a task; the authors attribute this to LLMs' lack of mnemonic cues, the internal experiential signals that ground human metacognitive updating. A safety-critical system cannot delegate risk sensitivity to the AI component's self-reported uncertainty, and repeated operation does not make that self-assessment more trustworthy.

The three limitations above (fixed pipeline, non-adaptive reasoning, unreliable self-assessment) establish that internal governance cannot be relied upon; the gap must be addressed through an external architectural layer.

## Objectives of This Study

The review establishes a research gap: the reviewed AI governance and decision-support architectures provide mechanisms for AI participation gating and autonomous action restriction, but do not restrict AI advisory scope according to classified environmental safety state. The mechanistic evidence presented in the Mechanistic Basis for External Governance section further indicates that this gap cannot be resolved within the AI component itself, motivating the need for an externally enforced governance mechanism. This study has three objectives: (1) to determine whether existing architectures implement mechanisms that restrict AI advisory scope according to classified environmental safety state; (2) to characterise the advisory scope gap through a structured comparison across governance paradigms; and (3) to derive a graduated safety-state-gated governance architecture that addresses the gap through externally enforced governance.

#  Proposed Architecture

The proposed architecture employs a Symbolic AI Reasoning Engine, implemented as a knowledge-based expert system within the classical symbolic AI tradition [38], to generate recommendations within the constraints imposed by the participation and advisory-scope gates. The mechanistic evidence above establishes that internal self-restraint cannot be relied upon; the gap requires an external architectural solution. The graduated safety-state-gated architecture proposed here conditions both AI participation and advisory scope on a classified environmental safety state, enforced by a layer outside the AI component (Fig. 3). The design also responds to a specific gap in governance theory: Engin and Hand argue that governance categories should be built as explicit thresholds over continuously monitored dimensions rather than as static classifications [32], but their proposal lacks an enforcement mechanism. The proposed architecture realises that pattern as an enforced runtime mechanism: continuous environmental observation E, deterministic thresholding S = f(E), and three actionable categories each carrying formally differentiated constraints, enforced by construction rather than by design intent.


Fig. 3. The graduated safety-state-gated architecture. Before any inference begins, a deterministic external classifier computes the environmental safety state S = f (E) outside the AI component. Both gates, G(S) and AAI(S), are conditioned on S and together bound what the AI may recommend for the current observation. The Symbolic AI Reasoning Engine is a knowledge-based expert system that applies predefined knowledge rules to generate recommendations within the advisory scope enforced by the governance layer.

```
Environmental observation vector E = {w, r, m, o, v, t}
                    │
                    ▼
         ┌─────────────────────┐
         │  Safety Classifier  │  S = f(E)
         │  (deterministic,    │
         │   external to AI)   │
         └─────────┬───────────┘
                   │
         ┌─────────▼───────────┐
         │  S ∈ {SAFE,         │
         │       CAUTION,      │
         │       UNSAFE}       │
         └──┬──────┬───────────┘
            │      │
     ┌──────▼──┐ ┌─▼──────────────┐
     │ G(S) = 0│ │   G(S) = 1     │
     │ UNSAFE  │ │ SAFE / CAUTION │
     │ AI off  │ └────────┬───────┘
     └─────────┘          │
                 ┌────────▼───────────────────────┐
                 │  Advisory Gate A_AI(S)          │
                 │  SAFE:    {Go, Delay,           │
                 │            DepartureTime,       │
                 │            Duration}            │
                 │  CAUTION: {Go, Delay}           │
                 └────────┬───────────────────────┘
                          │
                 ┌────────▼───────────────┐
                 │  Symbolic AI           │
                 │  Reasoning Engine      │
                 │  (RS(S) supplied       │
                 │   before inference)    │
                 └────────┬───────────────┘
                          │
                 ┌────────▼───────────┐
                 │  AI(E) ⊆ A_AI(S)   │
                 │  Recommendations   │
                 │  to human operator │
                 └────────────────────┘
```

## Formal Structure

Let E denote the environmental observation vector and S = f (E) a classifier that maps observations to a safety state S ∈ {SAFE, CAUTION, UNSAFE}. The governance pair (G(S), AAI(S)) operates as follows:

**Table III.** Governance pair configurations across the three safety states.

| State | G(S) | A_AI(S) | AI scope |
|---|---|---|---|
| SAFE | 1 (enabled) | {Go, Delay, DepartureTime, Duration} | Full |
| CAUTION | 1 (enabled) | {Go, Delay} | Restricted |
| UNSAFE | 0 (disabled) | ∅ | None |

The sets satisfy the containment relationship AAI(SAFE) ⊃ AAI(CAUTION) ⊃ AAI(UNSAFE) = ∅. The Safety Dominance Property then holds: for all E, AI(E) ⊆ AAI(S). The AI can only generate recommendations within the admissible space defined by the current safety state. The property holds by construction: the governance layer supplies a state-specific rule set to the reasoning engine before inference begins, so no rule in the CAUTION configuration can produce recommendations outside {Go, Delay}.

**Design Principle.** Each safety state admits only those recommendation types that can be justified by the environmental information available in that state. A domain deployment instantiates A_AI(S) by mapping each candidate recommendation type to its evidential requirements and verifying whether those requirements hold at each classified state.

## The CAUTION Mode

The CAUTION mode is the novel contribution that none of the architectures identified in this review implements. At CAUTION, the AI remains engaged and provides guidance that acknowledges marginal conditions, but within a formally restricted scope. The system withholds precise tactical outputs (departure time, trip duration) because the environmental data can no longer reliably support them. The human operator receives a participation signal from the AI alongside an implicit signal that conditions have restricted its scope, enabling calibrated reliance rather than over-reliance.

The CAUTION admissible set contains only recommendations that remain epistemically supportable under marginal environmental conditions. Go and Delay require only a coarse assessment of whether current conditions are acceptable for departure. DepartureTime and Duration, by contrast, presuppose confidence in the stability and predictability of future conditions: a departure window requires accurate short-term forecasting, and a trip duration estimate requires stable sea state over the full planning horizon. Once the system enters CAUTION, that predictive confidence is no longer available. The governance layer therefore withdraws tactical optimisation and preserves only coarse operational guidance: the conservative middle position between full advisory capability and complete AI disengagement.

Existing three-level designs (Flehmig et al.) use the intermediate level to govern human supervisory behaviour; the proposed architecture uses it to govern AI advisory scope. 

Empirical trade-offs documented in contemporary runtime assurance make the operational case for an intermediate CAUTION mode directly. Ghaleb et al. show that an aggressive, uncalibrated binary-style threshold gate can enforce strong raw safety metrics, but at the cost of nearly doubling the intervention burden (21.6 vs. 11.5 interventions per shifted episode) [27]. At the enforcement frontier, Pro2Guard's aggressive stop-mode enforces safety on 93.6% of unsafe tasks but collapses task completion to 17.54%; a softer intervention mode recovers 80.4% [34]. The enforcement literature thus documents the cost directly: all-or-nothing gating destroys utility precisely where bounded operation could preserve it. In low-resource settings such as coastal fisheries, an over-aggressive binary gate creates an unworkable trade-off: it either leaves the fisher with a decision vacuum during marginal weather or induces governance fatigue by disabling the tool when helpful, bounded advice could still be safely rendered. 

CAUTION also has a theoretical basis independent of these operational trade-offs. Kolt, Shur-Ofry, and Cohen argue from complex systems science that effective governance must intervene early, at calibrated risk thresholds, on incomplete information. By the time danger is fully evidenced, intervention is less effective [35]. A binary gate that withholds restriction until conditions are provably unsafe is, by construction, a wait-for-certainty policy. CAUTION is the early, threshold-calibrated alternative: it contracts advisory scope while conditions are still marginal rather than deferring restriction to the point of unambiguous danger.

## Domain Instantiation

The architecture is being pursued as a formally specified prototype for AI departure decision support in small-scale coastal fisheries in Malaysia (Kota Kinabalu, Sabah). E = {w, r, m, o, v, t} where w is wind speed, r is rainfall intensity, m is marine warning level, o is ocean state, v is vessel category, and t is time of day. The rule-based reasoning engine enforces the Safety Dominance Property by construction, satisfying the offline-first and computationally lightweight requirements of the low-resource deployment context. To minimise mode-chattering at the classification boundaries of S = f(E) during marginal weather transitions, a dual-threshold hysteresis smoothing layer over the discrete state transitions is a deployment-floor design consideration, drawing on the empirically verified runtime-gating stability of Ghaleb et al. [27].

This scenario reflects the documented departure decision process of small-scale fishers in coastal Malaysia, where assessment of environmental conditions (weather, tide, and safety) governs whether fishing proceeds normally, is modified, or is abandoned [37]; the runtime governance mechanism illustrated here is domain-independent.

**Illustrative scenario.** A fisher prepares to depart at 0600. At SAFE state (wind 8 kt, no marine warning, calm swell), the system generates a full-scope recommendation: Go, with a suggested departure window of 0630–0700 and an estimated safe trip duration of four hours. Wind strengthens to 18 kt by mid-morning and the marine warning level rises to advisory; S = f(E) reclassifies the state to CAUTION. The AI remains engaged but its admissible space contracts to {Go, Delay}: it recommends Delay with a brief rationale, but withholds the departure time and duration it could no longer reliably support. By afternoon, sustained wind exceeds the UNSAFE threshold; G(S) = 0 disengages the AI entirely, and the system presents only the static government warning. The fisher receives calibrated guidance at each state rather than full-scope output until abrupt shutdown.

# Conclusion

This paper establishes, from four independent bodies of literature, that AI governance in safety-critical decision support is binary by design across the reviewed literature: participation gating exists in the reviewed literature, advisory scope gating does not. Shamsujjoha et al.'s Swiss Cheese Model, the most comprehensive guardrails taxonomy in the field (synthesising 32 studies and identifying 13 guardrail actions and 14 quality attributes), contains no concept of restricting advisory scope as a function of environmental risk. Indykov et al.'s systematic review of 206 papers and 16 architectural tactics records a Safety score of zero for AT11 (rule-based models): despite Safety being one of the two most frequently cited quality attributes, no architectural tactic has demonstrated a formally positive impact on it [5]. The closest structural precedents identified in this review approach intermediate-risk conditions from alternate dimensions: Flehmig et al.'s traffic-light index changes human supervisory behaviour at its intermediate level but leaves AI output unchanged, while Sahoo's five-level protocol genuinely contracts an autonomous agent's permitted action space but remains blind to external environmental safety state and human-facing advisory contexts. The low-resource deployment literature confirms the pattern at the application level: no paper in this body implements formal runtime governance [19]. In the coastal fisheries domain specifically, the only external advisory available to fishers facing escalating weather risk is a binary government warning to stop fishing [18]. Prior research thus governs whether the AI operates and which actions an agent may execute; an admissible recommendation space AAI(S) that contracts as classified operational risk increases has not appeared in any of the reviewed architectures. The gap is characterised, confirmed from multiple independent sources, and open; the mechanistic evidence reviewed in the Mechanistic Basis for External Governance section indicates it cannot be closed within the AI component itself. 

The graduated safety-state-gated architecture proposed here addresses this gap through a two-level governance pair (G(S), AAI(S)) that produces an intermediate CAUTION mode. This is a novel architectural paradigm in safety-critical decision support, formally enforcing a state-conditioned containment where AI advisory scope contracts as environmental safety state worsens: AAI(SAFE) ⊃ AAI(CAUTION) ⊃ AAI(UNSAFE) = ∅. The architecture draws on Guaranteed Safe AI principles [9] and the dependability perspective of surrounding opaque AI components with deterministic guards [23]. In the settings this architecture targets, no institutional layer compensates for a governance failure in the tool; whatever the system enforces is all the governance the operator has. The contribution is a reframing: runtime AI governance need not compress participation and advisory scope into a single binary variable. They are distinct governance dimensions, each specifiable and enforceable by construction. The proposed architecture specifies and enforces both.

##### Acknowledgment

Will be add later!

##### References

[1] L. Yamin, T.-C. Kuo, and N. Aziz, "Interplay of traditional knowledge and adaptive capacity in climate change adaptation of small-scale fishers in central Terengganu, Malaysia," Frontiers in Marine Science, vol. 12, p. 1492131, 2025. doi: 10.3389/fmars.2025.1492131

[2] C. Dominguez-Péry, R. Tassabehji, F. Corset, and Z. Chreim, "A holistic view of maritime navigation accidents and risk indicators: examining IMO reports from 2011 to 2021," Journal of Shipping and Trade, vol. 8, p. 11, 2023. doi: 10.1186/s41072-023-00135-y

[3] C. Atacan and F. O. Düzbastılar, "Determination of risk perception in small-scale fishing and navigation," Ege Journal of Fisheries and Aquatic Sciences, vol. 40, no. 1, pp. 1–14, 2023. doi: 10.12714/egejfas.40.1.01

[4] H. Wen, Z. Sajid, and R. Arunthavanathan, "Risk perception in complex systems: A comparative analysis of process control and autonomous vehicle failures," AI, vol. 6, no. 8, p. 164, 2025. doi: 10.3390/ai6080164

[5] V. Indykov, D. Strüber, and R. Wohlrab, "Architectural tactics to achieve quality attributes of machine-learning-enabled systems: A systematic literature review," Journal of Systems and Software, vol. 223, p. 112373, 2025. doi: 10.1016/j.jss.2025.112373

[6] Md. Shamsujjoha, Q. Lu, D. Zhao, and L. Zhu, "Swiss cheese model for AI safety: A taxonomy and reference architecture for multi-layered guardrails of foundation model based agents," in Proc. IEEE 22nd Int. Conf. Software Architecture (ICSA), 2025, pp. 37–48. doi: 10.1109/ICSA65012.2025.00014

[7] N. Flehmig, M. A. Lundteigen, and S. Yin, "Implementing artificial intelligence in safety-critical systems during operation: Challenges and extended framework for a quality assurance process," in Proc. IEEE IECON 2024: 50th Annual Conf. IEEE Industrial Electronics Society, 2024. doi: 10.1109/IECON55916.2024.10906021

[8] B. Könighofer et al., "Shields for safe reinforcement learning," Communications of the ACM, vol. 68, no. 11, pp. 80–90, 2025. doi: 10.1145/3715958

[9] D. Dalrymple et al., "Towards guaranteed safe AI: A framework for ensuring robust and reliable AI systems," arXiv preprint arXiv:2405.06624, 2024.

[10] A. Bajcsy and J. F. Fisac, "Human–AI safety: A descendant of generative AI and control systems safety," arXiv preprint arXiv:2405.09794, 2024.

[11] A. Corsi, G. Amir, A. Rodriguez, C. Sanchez, G. Katz, and R. Fox, "Verification-guided shielding for deep reinforcement learning," in Proc. 1st Reinforcement Learning Conference (RLC), 2024. doi: 10.48550/arXiv.2406.06507

[12] J. Abella et al., "SAFEXPLAIN: A complete approach towards trustworthy AI-based safety-critical systems," in Proc. 28th Euromicro Conf. Digital System Design (DSD), IEEE, 2025, pp. 324–331. doi: 10.1109/DSD67783.2025.00053

[13] I.F. Ramos, G. Gianini, M.C. Leva, and E. Damiani, "Collaborative intelligence for safety-critical industries: A literature review," Information, vol. 15, no. 11, p. 728, 2024. doi: 10.3390/info15110728

[14] Z. Feng, J. McDonald, and C. Zhang, "Levels of autonomy for AI agents," arXiv preprint arXiv:2506.12469, 2025.

[15] A. Baxi, "The comprehension-gated agent economy: A robustness-first architecture for AI economic agency," arXiv preprint arXiv:2603.15639, 2026.

[16] J. Vermaelen and T. Holvoet, "Tumato 2.0: A constraint-based planning approach for safe and robust robot behavior," Annals of Mathematics and Artificial Intelligence, vol. 93, pp. 541–567, 2025. doi: 10.1007/s10472-024-09949-3

[17] M. S. Haque and S. Al Jufaili, "Applications of artificial intelligence in fisheries: From data to decisions," Big Data and Cognitive Computing, vol. 10, no. 1, art. 19, 2026. doi: 10.3390/bdcc10010019

[18] Abd. Rahim et al., "Survival decisions and adaptation strategies of small-scale fishers in the face of extreme weather impacts in coastal areas," Journal of Marine and Island Cultures, vol. 13, no. 3, 2024. doi: 10.21463/jmic.2024.13.3.05

[19] A. Katende, "Rethinking data-efficient artificial intelligence for low-resource settings," Machine Learning with Applications, vol. 23, p. 100796, 2026. doi: 10.1016/j.mlwa.2025.100796

[20] A. Longobardi et al., "Peskas: Automated analytics for small-scale, data-deficient fisheries," SoftwareX, vol. 29, p. 102028, 2025. doi: 10.1016/j.softx.2024.102028

[21] P. Bhuvaneswari, K. D. V. Prasad, M. Ashraf, and S. Jadhav, "A human-centered hybrid AI framework for optimizing emergency triage in resource-constrained settings," Intelligence-Based Medicine, vol. 12, p. 100311, 2025. doi: 10.1016/j.ibmed.2025.100311

[22] B. Attard-Frost and K. Lyons, "AI governance systems: A multi-scale analysis framework, empirical findings, and future directions," AI and Ethics, vol. 5, pp. 2557–2604, 2025. doi: 10.1007/s43681-024-00569-5

[23] R. Bloomfield and J. Rushby, Assurance of AI Systems from a Dependability Perspective, SRI Technical Report SRI-CSL-2024-02R3, SRI International, 2025. doi: 10.48550/arXiv.2407.13948

[24] J. Perez-Cerrolaza, J. Abella, M. Borg, C. Donzella, J. Cerquides, F. J. Cazorla, C. Englund, M. Tauber, G. Nikolakopoulos, and J. L. Flores, "Artificial intelligence for safety-critical systems in industrial and transportation domains: A survey," ACM Computing Surveys, vol. 56, no. 7, article 176, 2024. doi: 10.1145/3626314

[25] R. Kang, "Governed AI-assisted engineering: Graduated human oversight for agentic code generation in regulated domains," arXiv preprint arXiv:2606.22484v2 [cs.HC], Jul. 2026.

[26] S. Sahoo, "The controllability trap: A governance framework for military AI agents," in Proc. ICLR 2026 Workshop on Agents in the Wild, Mar. 2026. arXiv:2603.03515.

[27] A. M. Ghaleb, A. S. Allahloh, S. Mejjaouli, M. A. H. Ali, and A. Al-Shayea, "Uncertainty-calibrated safety gating for vision–language–action manipulation under domain shift: Reliability gains and intervention–efficiency trade-offs," Sensors, vol. 26, no. 10, p. 3140, May 2026. doi: 10.3390/s26103140

[28] A. K. Kamath, R. Prabhu, J. Mohan, S. Peter, R. Ramjee, and A. Panwar, "POD-Attention: Unlocking full prefill-decode overlap for faster LLM inference," in Proc. 30th ACM Int. Conf. Architectural Support for Programming Languages and Operating Systems, Volume 2 (ASPLOS '25), Rotterdam, Netherlands, 2025, pp. 897–912. doi: 10.1145/3676641.3715996

[29] C. Wu, J. Lu, Z. Ren, G. Hu, Z. Wu, D. Dai, and H. Wu, "LLMs are single-threaded reasoners: Demystifying the working mechanism of soft thinking," arXiv preprint arXiv:2508.03440, 2025.

[30] T. N. Cash, D. M. Oppenheimer, S. Christie, and M. Devgan, "Quantifying uncert-AI-nty: Testing the accuracy of LLMs' confidence judgments," Memory & Cognition, vol. 54, pp. 375–400, 2025. doi: 10.3758/s13421-025-01755-4

[31] A. Reuel, P. Connolly, K. J. Meimandi, S. Tewari, J. Wiatrak, D. Venkatesh, and M. Kochenderfer, "Responsible AI in the global context: Maturity model and survey," in Proc. 2025 ACM Conf. Fairness, Accountability, and Transparency (FAccT '25), Athens, Greece, 2025, pp. 2505–2541. doi: 10.1145/3715275.3732165

[32] Z. Engin and D. Hand, "Towards adaptive categories: Dimensional governance for agentic AI," arXiv preprint arXiv:2505.11579, 2025.

[33] M. Mussi et al., "Human-AI interaction in safety-critical network infrastructures," iScience, vol. 28, p. 113400, 2025. doi: 10.1016/j.isci.2025.113400

[34] H. Wang, C. M. Poskitt, J. Sun, and J. Wei, "Pro2Guard: Proactive runtime enforcement of LLM agent safety via probabilistic model checking," arXiv preprint arXiv:2508.00500, 2025.

[35] N. Kolt, M. Shur-Ofry, and R. Cohen, "Lessons from complex systems science for AI governance," Patterns, vol. 6, p. 101341, 2025. doi: 10.1016/j.patter.2025.101341

[36] A. Batool, D. Zowghi, and M. Bano, "AI governance: A systematic literature review," AI and Ethics, vol. 5, pp. 3265–3279, 2025. doi: 10.1007/s43681-024-00653-w

[37] T. Gao, "Mapping the Decision-Making Factors of Small-Scale Fishers: A Case Study of Penang," M.Sc. thesis, International Master of Science in Rural Development, University of Pisa / WorldFish (CGIAR), 2024. [Online]. Available: https://hdl.handle.net/10568/152289