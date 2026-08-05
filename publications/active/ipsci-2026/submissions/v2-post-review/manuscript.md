A Graduated Safety-State-Gated Architecture for AI Decision Support

Abstract— How should AI advisory behaviour adapt as operational conditions deteriorate? Existing governance mechanisms are uniformly binary: the AI either generates its full recommendation set or is blocked entirely. This paper reviews the AI governance, runtime assurance, human-AI collaboration, and low-resource deployment literature to determine whether existing architectures restrict AI advisory scope as environmental risk increases and to motivate a new governance architecture. Mechanistic studies reveal three limitations: the inference pipeline is structurally fixed, reasoning exploration is a property of the decoding procedure rather than a content-conditioned adaptation, and self-assessed confidence is unreliable and insensitive to past performance. Large-scale systematic reviews found that none of the reviewed architectural tactics demonstrated a formally positive impact on safety, while the most comprehensive guardrail taxonomy contains no mechanism for restricting advisory scope based on environmental risk. Binary governance therefore leaves intermediate-risk conditions structurally unaddressed: operators in low-resource environments receive either full-scope tactical recommendations or none at all. To address this gap, we propose a graduated safety-state-gated architecture, in which a participation gate and an AI advisory gate, both conditioned on the environmental safety state, produce an intermediate caution mode with formally restricted advisory scope. The proposed architecture is illustrated through a small-scale coastal fisheries deployment context.

Keywords—AI governance, safety-critical systems, decision support, graduated architecture, coastal fisheries

# Introduction

AI decision support is expanding into safety-critical, human-in-the-loop settings across healthcare, industrial operations, autonomous transportation, and maritime activity. The governance accompanying this expansion is not keeping pace. Reuel et al. surveyed 1,000 organisations spanning 20 industries and found that none had reached both planning and operational AI governance maturity simultaneously, a systematic gap they warned "could lead to increased (public) risks from AI systems" [28]. If process-level governance cannot be relied on, the safety argument falls to the architecture. The question is what that architecture should do as conditions deteriorate, specifically during the marginal conditions between the safe-to-dangerous endpoints.

Existing frameworks treat this as a binary: the AI either generates its full recommendation set or is shut off. When a binary gate encounters marginal conditions, it defaults to treating them as safe, leaving the operator with full-scope tactical advice that the underlying data may no longer support. Wen et al. document the consequence: users receiving AI output under deteriorating conditions tend toward over-reliance, accepting recommendations they should question [4]. What this review asks is whether any existing mechanism restricts what an AI may recommend, as distinct from whether it may participate at all.

The stakes are highest in settings where no institutional layer exists to compensate when governance fails. Small-scale fishers along Malaysia's coastline make this decision each morning alone, without support, on vessels under 40 gross register tonnage, drawing on traditional weather knowledge that is eroding as climate patterns shift [1]. The risk profile is documented: wind, weather, and visibility account for 26.7% of maritime accident causes, and small vessels record the highest mean fatality rank across vessel categories [2]; combined night navigation and heavy weather produces the highest consequence scores of any condition tested [3].

Three governance dimensions frame the space of possible mechanisms (Fig. 1). Dimensions 1 and 3 are addressed in existing work; dimension 2 (advisory scope restriction) is not.

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

Two contributions follow. A structured review of 72 papers, supplemented by three large-scale systematic reviews covering 532 primary references, finds no architecture identified in this review that restricts AI advisory scope as a function of classified environmental safety state, and gives mechanistic reasons why this gap cannot be closed from within the AI component. The second contribution is a graduated safety-state-gated architecture that addresses the gap through a formally bounded governance pair consisting of a participation gate G(S) and an admissible recommendation space A_AI(S), both conditioned on the environmental safety state, producing an intermediate CAUTION mode: restricted advisory scope under marginal conditions, with neither full output nor complete AI withdrawal.

# Methodology

The review is structured rather than systematic: search and coding are disciplined, but scope is purposive, covering only the bodies of literature where an advisory-scope restriction mechanism could plausibly appear. Papers came from Scopus, IEEE Xplore, Web of Science, and ACM Digital Library, using search strings spanning AI governance, runtime assurance, safety filters, decision support, autonomy levels, and guardrails; secondary searches covered fisheries AI and low-resource deployment. Three large-scale systematic reviews within the initial candidate set were retained as secondary evidence: Indykov et al. [5] (206 papers, 16 architectural tactics), Shamsujjoha et al. [6] (13 guardrail actions, 32 agent studies), and Perez-Cerrolaza et al. [21] (294 references). Seventy-two papers proceeded to full review, each coded on four dimensions (Table I). Papers sharing a governance topology were grouped into three paradigms plus an application domain.

**Table I.** Coding dimensions applied to all reviewed papers.

| Dimension | Values |
|---|---|
| **Primary governance target** | Participation / Advisory scope / Execution / Oversight |
| **Runtime adaptation** | Binary (on/off) / Graduated (3+ levels) / None |
| **Conditioning variable** | Environmental state / AI robustness / Task risk / Human authority / None |
| **Recommendation restriction** | Yes (bounded output set) / No |



# Literature Review

## Overview of Existing Governance Paradigms

The reviewed frameworks sort into three paradigms: deterministic safety constraints, which provide provable runtime guarantees; authority allocation, which distributes decision rights between human and AI; and adaptive risk-based systems, which vary AI behaviour across graduated operational levels. Across all three, the governance target is participation, authority, or execution, not advisory scope. A fourth body, fisheries AI and low-resource deployment, is reviewed to establish whether this pattern holds in the intended application domain. The review process is summarised in Fig. 2.



Fig. 2. Structured review process showing how four bodies of literature converge on the same gap and motivate the proposed architecture.

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

Könighofer et al. formalise shields: runtime mechanisms that intercept AI actions before they reach the environment [8]. Dalrymple et al. require formal proof certificates before AI output is deployed [9]. Bajcsy and Fisac implement a control-theoretic safety filter [10]. The governance topology is the same in all three: the AI either operates within its safety boundary or is replaced, and the object of governance is execution. The same binary structure appears in constraint-based planning approaches such as Tumato 2.0 [14]. In every case, the semantic content of AI output is not addressed.

## Authority Allocation: Who Decides, Not What AI May Recommend

Authority allocation frameworks ask who decides, not what the AI may recommend. Ramos et al., reviewing 91 collaborative intelligence studies, find AI-assisted decision-making dominant across safety-critical industries, but no system varies advisory scope by safety state [11]. Feng et al. propose five autonomy levels, fixed at design time [12]. At cross-domain scale, Mussi et al. identify every ingredient of state-conditioned governance across power grids, railway networks, and air traffic management, yet assemble none into a runtime model: automation levels are set before deployment and do not change [30]. When conditions evolve, the advisory scope does not.

## Adaptive Risk-Based Systems: The Closest Precedents

The adaptive systems literature yields three distinct governance postures. In the first, oversight intensification, Flehmig et al.'s traffic-light degradation index (green/orange/red) triggers progressively intensive supervisory responses by level [7]. At the intermediate orange level, supervisory checks intensify; the AI's advisory scope, however, is identical at green and orange. The intermediate level changes what the human supervisor does, not what the AI may say. Kang's GAIE framework routes code generation through three oversight tiers; at the intermediate tier, a deployment-gate is added, yet the coding agent generates full-scope, unconstrained output at every tier [22].

In execution deferral and re-sensing, Ghaleb et al.'s three-regime gating wrapper (Safe, Borderline, Unsafe) forces execution slowdown and re-observation at the Borderline regime [24]. The policy's output capability remains uncontracted throughout; at Unsafe, the learned policy is replaced by a classical planner.

In autonomous action-class restriction, Sahoo's Agentic Military AI Governance Framework throttles tool access across five response levels using a real-time Control Quality Score; at intermediate levels, the agent is restricted to reversible actions [23]. Of the reviewed frameworks, this comes closest to graduated advisory scope contraction. The difference is the object of governance: an acting autonomous agent, with restriction conditioned on measured control degradation rather than classified environmental state. Baxi's K-tier permission architecture similarly varies permission sets by tier, conditioned on the AI's own verified robustness [13].

Across all three postures, graduated operational posture is technically feasible. The question is not whether intermediate levels are possible, but where graduation is applied: in every reviewed case, it targets human workflows, execution deferral, or agent action classes, not the recommendation content the human decision-maker receives.

## Synthesis: Cross-Paradigm Comparison and the Research Gap

The pattern holds at the application level. No fisheries AI system identified in this review implements formal advisory scope restriction conditioned on environmental state [17]; the only external advisory available to coastal fishers is a binary government warning [16]; and safety governance in low-resource deployment contexts has not been designed from the deployment floor up [15][19].

The four bodies point in the same direction. Deterministic constraints are binary by construction; authority allocation frameworks fix advisory scope at design time; adaptive risk-based systems apply their intermediate levels to human workflows or execution deferral rather than output scope; and the fisheries and low-resource literature lacks formal runtime governance altogether [15][16][17]. Across all reviewed paradigms, the object of governance differs, but none conditions AI advisory scope on classified environmental safety state.

Four literature streams point to the same absence independently. Indykov et al. surveyed 206 papers and found a Safety score of zero for AT11 (rule-based models): despite Safety being one of the two most frequently cited quality attributes, no architectural tactic has demonstrated a formally positive impact on it [5]. Shamsujjoha et al.'s Swiss Cheese Model covers 13 guardrail actions across content filtering, blocking, and validation; none conditions advisory scope on dynamic environmental risk [6]. The adaptive architectures reviewed here, Flehmig et al. [7], Kang [22], and Ghaleb et al. [24], apply their intermediate tiers to human audit escalation or execution deferral, not to what the AI may say. Behavioural frameworks such as Sahoo's [23] throttle the execution space of acting agents, not the recommendation menus presented to human decision-makers.

What differs across every reviewed framework is not just the governance target but the conditioning variable. Baxi gates on AI robustness [13]; Flehmig et al. on AI degradation [7]; Kang on task regulatory impact [22]; Sahoo on control quality [23]; Ghaleb et al. on epistemic uncertainty [24]. In each case, the trigger is internal to the AI system. The proposed architecture departs from this: it conditions on an independently classified environmental safety state S = f(E), computed outside the AI component.

**Table II.** Coding of reviewed architectures against the four governance dimensions (see Table I). The proposed architecture is the only framework in the corpus that targets advisory scope and formally bounds the output set a human decision-maker may receive, conditioned on environmental safety state.

| Framework | Governance target | Conditioning variable | Runtime adaptation | Output restriction |
|---|---|---|---|---|
| Shields [8], Guaranteed Safe AI [9], safety filter [10] | Participation | Safety boundary | Binary (on/off) | No |
| Tumato 2.0 [14] | Execution | Constraint predicate | Binary per action | No |
| Pro2Guard [31] | Execution | Predicted unsafe-state probability | Binary (threshold-triggered) | No |
| Flehmig et al. traffic-light [7] | Oversight | AI degradation index | Graduated (3 levels) | No |
| Kang GAIE [22] | Oversight | Task regulatory impact | Graduated (3 tiers) | No |
| Ghaleb et al. safety gate [24] | Execution | Epistemic uncertainty | Graduated (3 regimes) | No |
| Sahoo AMAGF [23] | Execution | Control quality score | Graduated (5 bands) | No |
| Baxi K-tier [13] | Execution | AI robustness (verified) | Graduated (K tiers) | No |
| **Proposed architecture** | **Advisory scope** | **Environmental safety state** | **Graduated (3 states)** | **Yes** (A_AI(CAUTION) = {Go, Delay}) |

*Shamsujjoha et al.'s Swiss Cheese Model [6] describes 13 guardrail actions applied to agent artifacts and pipeline stages. All actions are content-focused; none condition AI advisory scope on environmental safety state.*

## The Mechanistic Basis for External Governance

The proposed architecture uses a Symbolic AI Reasoning Engine [34]. The mechanistic evidence below applies more broadly: it establishes that no AI component, whatever technique underlies it, can reliably self-restrict as conditions deteriorate. Three points from the LLM systems literature make the case. LLM inference runs through fixed prefill and decode phases; decisions about batching, scheduling, and kernel selection are driven by token counts and hardware utilisation, not by the semantic content of the input, leaving the pipeline with no hook at which advisory scope could vary with environmental state [25]. Probing studies find that reasoning breadth is a property of the decoding procedure rather than of what the input contains; externally injected randomness scatters reasoning but cannot produce systematically conservative output under worsening conditions [26]. LLM confidence judgements are poorly calibrated, biased toward overconfidence, and fail to improve with experience, which means a safety-critical system cannot treat the AI's self-reported uncertainty as a reliable risk signal [27]. All three limitations point in the same direction: governance cannot be delegated to the AI component.

#  Proposed Architecture

An *AI decision support system* generates recommendations for a human decision-maker who retains final authority, distinct from an autonomous agent that executes actions directly. A *safety-critical system* is one in which incorrect output can contribute to harm to life, health, or property. *Runtime governance* refers to mechanisms that constrain AI behaviour during operation, distinct from design-time controls. Within runtime governance, this paper separates *participation gating* (whether the AI may participate) from *advisory scope* (A_AI(S)): the set of recommendation types the AI is permitted to generate while participating. An *environmental safety state* is a classified summary S of an observation vector E, produced by a function S = f(E) computed independently of the AI. A *low-resource environment* lacks reliable connectivity, computing infrastructure, and institutional support.

The proposed architecture uses a Symbolic AI Reasoning Engine, a knowledge-based expert system in the classical symbolic AI tradition [34], to generate recommendations within the scope the governance layer permits. As the Mechanistic Basis section establishes, internal self-restraint cannot be relied upon; the solution must be external. The graduated safety-state-gated architecture conditions both AI participation and advisory scope on a classified environmental safety state, enforced by a layer outside the AI component (Fig. 3). The design also responds to a specific gap in governance theory: Engin and Hand argue that governance categories should be built as explicit thresholds over continuously monitored dimensions rather than as static classifications [29], but their proposal lacks an enforcement mechanism. The proposed architecture realises that pattern as an enforced runtime mechanism: continuous environmental observation E, deterministic thresholding S = f(E), and three actionable categories each carrying formally differentiated constraints, enforced by construction rather than by design intent.


Fig. 3. Graduated safety-state-gated architecture showing environmental classification, governance pair (G(S), A_AI(S)), and advisory-scope restriction.

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

These sets satisfy the containment relationship AAI(SAFE) ⊃ AAI(CAUTION) ⊃ AAI(UNSAFE) = ∅, which implies the Safety Dominance Property: for all E, AI(E) ⊆ AAI(S). Recommendations are bounded to whatever the current safety state permits. This holds by construction: the governance layer supplies a state-specific rule set to the reasoning engine before inference begins, so no rule in the CAUTION configuration can produce recommendations outside {Go, Delay}.

**Design Principle.** Each safety state admits only those recommendation types that can be justified by the environmental information available in that state. A domain deployment instantiates A_AI(S) by mapping each candidate recommendation type to its evidential requirements and verifying whether those requirements hold at each classified state.

## The CAUTION Mode

CAUTION is what none of the reviewed architectures implements. At CAUTION, the AI remains engaged and provides guidance that acknowledges marginal conditions, but within a formally restricted scope. The system withholds precise tactical outputs (departure time, trip duration) because the environmental data can no longer reliably support them. The human operator receives a participation signal from the AI alongside an implicit signal that conditions have restricted its scope, enabling calibrated reliance rather than over-reliance.

The CAUTION admissible set contains only recommendations that remain epistemically supportable under marginal environmental conditions. Go and Delay require only a coarse assessment of whether current conditions are acceptable for departure. DepartureTime and Duration, by contrast, presuppose confidence in the stability and predictability of future conditions: a departure window requires accurate short-term forecasting, and a trip duration estimate requires stable sea state over the full planning horizon. Once the system enters CAUTION, that predictive confidence is no longer available. The governance layer therefore withdraws tactical optimisation and preserves only coarse operational guidance: the conservative middle position between full advisory capability and complete AI disengagement.

Runtime assurance evidence supports the operational case. All-or-nothing gating enforces safety but destroys utility precisely where bounded operation could preserve it [24][31]; in low-resource settings this creates an unworkable trade-off between a decision vacuum during marginal weather and governance fatigue from disabling the tool when bounded advice could still be safely rendered. Kolt et al. argue that effective governance must intervene early, at calibrated thresholds, before certainty arrives [32]; CAUTION is that early intervention, contracting scope while conditions remain marginal.

## Domain Instantiation

The architecture is being pursued as a formally specified prototype for AI departure decision support in small-scale coastal fisheries in Malaysia (Kota Kinabalu, Sabah), where lightweight AI has demonstrated feasibility in data-deficient and resource-constrained contexts [18][19]. E = {w, r, m, o, v, t} where w is wind speed, r is rainfall intensity, m is marine warning level, o is ocean state, v is vessel category, and t is time of day. The Symbolic AI Reasoning Engine enforces the Safety Dominance Property by construction and meets the offline-first and computationally lightweight requirements of the low-resource deployment context. To minimise mode-chattering at the classification boundaries of S = f(E) during marginal weather transitions, a dual-threshold hysteresis smoothing layer over the discrete state transitions is a deployment-floor design consideration, drawing on the empirically verified runtime-gating stability of Ghaleb et al. [24].

This scenario reflects the documented departure decision process of small-scale fishers in coastal Malaysia, where assessment of environmental conditions (weather, tide, and safety) governs whether fishing proceeds normally, is modified, or is abandoned [33]; the runtime governance mechanism illustrated here is domain-independent.

**Illustrative scenario.** As environmental conditions deteriorate across three time points, advisory scope contracts from full recommendations at SAFE, to {Go, Delay} at CAUTION, to complete AI disengagement at UNSAFE. The fisher receives calibrated guidance at each state rather than full-scope output until abrupt shutdown. The full sequence is shown in Fig. 4.

Fig. 4. Illustrative state transitions across SAFE, CAUTION, and UNSAFE, showing advisory scope contracting as environmental conditions deteriorate.

```
=======================================================================================================================
                                 GRADUATED SAFETY-STATE-GATED ARCHITECTURE
                                           (Illustrative Values)
=======================================================================================================================

  INPUT VECTOR E                       SAFETY CLASSIFIER S = f(E)              AI GATING & ADMISSIBLE SPACE A_AI(S)
-----------------------------------------------------------------------------------------------------------------------

[0600 - Early Morning]
 • Wind (w): 8 kt                      ┌────────────────────────┐              ┌─────────────────────────────────────┐
 • Rain (r): none                      │          SAFE          │              │ G(SAFE) = 1 (Active)                │
 • Warning (m): none                   └────────────────────────┘              │                                     │
 • Ocean State (o): calm swell                                                 │ Admissible Scope A_AI(SAFE):        │
 • Vessel Cat (v): small                          │                            │ { Go, Delay, DepartureTime,         │
 • Time (t): 0600                                 │                            │   Duration }                        │
                                                  ▼                            └─────────────────────────────────────┘
                                   Condition Deteriorates
                                                  │
[Mid-Morning]                                     ▼
 • Wind (w): 18 kt                     ┌────────────────────────┐              ┌─────────────────────────────────────┐
 • Rain (r): moderate                  │        CAUTION         │              │ G(CAUTION) = 1 (Active)             │
 • Warning (m): advisory               └────────────────────────┘              │                                     │
 • Ocean State (o): moderate swell                                             │ Scope Contracts A_AI(CAUTION):      │
 • Vessel Cat (v): small                          │                            │ { Go, Delay }                       │
 • Time (t): 1000                                 │                            │                                     │
                                                  ▼                            │ (DepartureTime & Duration withheld) │
                                   Condition Exceeds Safety Limit              └─────────────────────────────────────┘
                                                  │
[Afternoon]                                       ▼
 • Wind (w): 28 kt (sustained)         ┌────────────────────────┐              ┌─────────────────────────────────────┐
 • Rain (r): heavy                     │         UNSAFE         │              │ G(UNSAFE) = 0 (Disengaged)          │
 • Warning (m): warning                └────────────────────────┘              │                                     │
 • Ocean State (o): rough seas                                                 │ Admissible Scope A_AI(UNSAFE):      │
 • Vessel Cat (v): small                                                       │ ∅ (Empty Set — Static Alert Only)   │
 • Time (t): 1400                                                              └─────────────────────────────────────┘
=======================================================================================================================
```

# Conclusion

Four independent bodies of literature converge on the same gap: AI governance in safety-critical decision support addresses participation and agent execution, but not advisory scope. No reviewed architecture implements a recommendation space that contracts as a function of classified environmental safety state. The three closest structural precedents, Flehmig et al.'s traffic-light index [7], Sahoo's five-level protocol [23], and Ghaleb et al.'s safety gate [24], each approach intermediate-risk conditions from a different angle, governing supervisory behaviour, agent action classes, and execution deferral respectively, while leaving AI recommendation content unchanged. The fisheries and low-resource literature finds no exception [15][16][17].

What the mechanistic review adds is that the gap cannot be closed from inside the AI component. Prior research governs whether the AI operates and which actions an agent may execute; a recommendation space that contracts with classified environmental risk does not appear in any reviewed architecture. The consequence falls on the operator: during marginal conditions, they receive full-scope tactical advice at the moment the underlying data can no longer support it, with no architectural signal that anything has changed [4].

The graduated safety-state-gated architecture proposed here addresses this gap through a two-level governance pair (G(S), A_AI(S)) that produces an intermediate CAUTION mode, which no reviewed architecture implements. Advisory scope contracts as environmental safety state worsens: A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅, enforced by construction rather than at the discretion of the operator. The architecture draws on Guaranteed Safe AI principles [9] and the dependability perspective of surrounding opaque AI components with deterministic guards [20]. In the settings this architecture targets, no institutional layer compensates for a governance failure in the tool; whatever the system enforces is all the governance the operator has. The core claim is that runtime AI governance need not compress participation and advisory scope into a single binary variable. They are distinct governance dimensions, each specifiable and enforceable by construction. The proposed architecture specifies and enforces both.

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

[11] I.F. Ramos, G. Gianini, M.C. Leva, and E. Damiani, "Collaborative intelligence for safety-critical industries: A literature review," Information, vol. 15, no. 11, p. 728, 2024. doi: 10.3390/info15110728

[12] Z. Feng, J. McDonald, and C. Zhang, "Levels of autonomy for AI agents," arXiv preprint arXiv:2506.12469, 2025.

[13] A. Baxi, "The comprehension-gated agent economy: A robustness-first architecture for AI economic agency," arXiv preprint arXiv:2603.15639, 2026.

[14] J. Vermaelen and T. Holvoet, "Tumato 2.0: A constraint-based planning approach for safe and robust robot behavior," Annals of Mathematics and Artificial Intelligence, vol. 93, pp. 541–567, 2025. doi: 10.1007/s10472-024-09949-3

[15] M. S. Haque and S. Al Jufaili, "Applications of artificial intelligence in fisheries: From data to decisions," Big Data and Cognitive Computing, vol. 10, no. 1, art. 19, 2026. doi: 10.3390/bdcc10010019

[16] Abd. Rahim et al., "Survival decisions and adaptation strategies of small-scale fishers in the face of extreme weather impacts in coastal areas," Journal of Marine and Island Cultures, vol. 13, no. 3, 2024. doi: 10.21463/jmic.2024.13.3.05

[17] A. Katende, "Rethinking data-efficient artificial intelligence for low-resource settings," Machine Learning with Applications, vol. 23, p. 100796, 2026. doi: 10.1016/j.mlwa.2025.100796

[18] A. Longobardi et al., "Peskas: Automated analytics for small-scale, data-deficient fisheries," SoftwareX, vol. 29, p. 102028, 2025. doi: 10.1016/j.softx.2024.102028

[19] P. Bhuvaneswari, K. D. V. Prasad, M. Ashraf, and S. Jadhav, "A human-centered hybrid AI framework for optimizing emergency triage in resource-constrained settings," Intelligence-Based Medicine, vol. 12, p. 100311, 2025. doi: 10.1016/j.ibmed.2025.100311

[20] R. Bloomfield and J. Rushby, Assurance of AI Systems from a Dependability Perspective, SRI Technical Report SRI-CSL-2024-02R3, SRI International, 2025. doi: 10.48550/arXiv.2407.13948

[21] J. Perez-Cerrolaza, J. Abella, M. Borg, C. Donzella, J. Cerquides, F. J. Cazorla, C. Englund, M. Tauber, G. Nikolakopoulos, and J. L. Flores, "Artificial intelligence for safety-critical systems in industrial and transportation domains: A survey," ACM Computing Surveys, vol. 56, no. 7, article 176, 2024. doi: 10.1145/3626314

[22] R. Kang, "Governed AI-assisted engineering: Graduated human oversight for agentic code generation in regulated domains," arXiv preprint arXiv:2606.22484v2 [cs.HC], Jul. 2026.

[23] S. Sahoo, "The controllability trap: A governance framework for military AI agents," in Proc. ICLR 2026 Workshop on Agents in the Wild, Mar. 2026. arXiv:2603.03515.

[24] A. M. Ghaleb, A. S. Allahloh, S. Mejjaouli, M. A. H. Ali, and A. Al-Shayea, "Uncertainty-calibrated safety gating for vision–language–action manipulation under domain shift: Reliability gains and intervention–efficiency trade-offs," Sensors, vol. 26, no. 10, p. 3140, May 2026. doi: 10.3390/s26103140

[25] A. K. Kamath, R. Prabhu, J. Mohan, S. Peter, R. Ramjee, and A. Panwar, "POD-Attention: Unlocking full prefill-decode overlap for faster LLM inference," in Proc. 30th ACM Int. Conf. Architectural Support for Programming Languages and Operating Systems, Volume 2 (ASPLOS '25), Rotterdam, Netherlands, 2025, pp. 897–912. doi: 10.1145/3676641.3715996

[26] C. Wu, J. Lu, Z. Ren, G. Hu, Z. Wu, D. Dai, and H. Wu, "LLMs are single-threaded reasoners: Demystifying the working mechanism of soft thinking," arXiv preprint arXiv:2508.03440, 2025.

[27] T. N. Cash, D. M. Oppenheimer, S. Christie, and M. Devgan, "Quantifying uncert-AI-nty: Testing the accuracy of LLMs' confidence judgments," Memory & Cognition, vol. 54, pp. 375–400, 2025. doi: 10.3758/s13421-025-01755-4

[28] A. Reuel, P. Connolly, K. J. Meimandi, S. Tewari, J. Wiatrak, D. Venkatesh, and M. Kochenderfer, "Responsible AI in the global context: Maturity model and survey," in Proc. 2025 ACM Conf. Fairness, Accountability, and Transparency (FAccT '25), Athens, Greece, 2025, pp. 2505–2541. doi: 10.1145/3715275.3732165

[29] Z. Engin and D. Hand, "Towards adaptive categories: Dimensional governance for agentic AI," arXiv preprint arXiv:2505.11579, 2025.

[30] M. Mussi et al., "Human-AI interaction in safety-critical network infrastructures," iScience, vol. 28, p. 113400, 2025. doi: 10.1016/j.isci.2025.113400

[31] H. Wang, C. M. Poskitt, J. Sun, and J. Wei, "Pro2Guard: Proactive runtime enforcement of LLM agent safety via probabilistic model checking," arXiv preprint arXiv:2508.00500, 2025.

[32] N. Kolt, M. Shur-Ofry, and R. Cohen, "Lessons from complex systems science for AI governance," Patterns, vol. 6, p. 101341, 2025. doi: 10.1016/j.patter.2025.101341

[33] T. Gao, "Mapping the Decision-Making Factors of Small-Scale Fishers: A Case Study of Penang," M.Sc. thesis, International Master of Science in Rural Development, University of Pisa / WorldFish (CGIAR), 2024. [Online]. Available: https://hdl.handle.net/10568/152289

[34] V. Belle, "On the relevance of logic for artificial intelligence, and the promise of neurosymbolic learning," Neurosymbolic Artificial Intelligence, 2025. doi: 10.1177/29498732251339951
