A Graduated Safety-State-Gated Architecture For AI Decision Support

*Abstract--- How should AI advisory behaviour adapt as operational conditions deteriorate? Existing governance mechanisms are uniformly binary, meaning that the AI either generates its full recommendation set or is blocked entirely. This paper explores the available literature for the areas of AI governance, runtime assurance, human-AI collaboration, and deployment in low-resource settings, identifying how existing architectures limit the scope of AI advisory as environmental risk increases and providing motivation for a new governance architecture. Mechanistic studies show that there are three limitations: the inference pipeline is structurally fixed, the exploration of reasoning is a property of the decoding procedure and not a content-conditioned adaptation, and self-assessed confidence is unreliable and insensitive to past performance. Large-scale systematic reviews revealed that no architectural tactic demonstrated a formally positive impact on safety, while the most detailed guardrail taxonomy did not include a mechanism for restricting advisory scope based on environmental risk. Binary governance thus leaves intermediate-risk conditions structurally unaddressed: operators in low-resource settings either get full-scope tactical recommendations, or they do not get any. To address this gap, we propose a graduated safety-state-gated architecture, in which a participation gate and an AI advisory gate, both conditioned on the environmental safety state, produce an intermediate caution mode with formally restricted advisory scope. The proposed architecture is illustrated through a small-scale coastal fisheries deployment context.*

Keywords--- AI governance, safety-critical systems, decision support, graduated architecture, coastal fisheries

# Introduction

AI decision support is growing more prevalent in safety-critical, human-in-the-loop scenarios across healthcare, industrial operations, autonomous transportation, and maritime operations. The governance accompanying this expansion is not keeping pace. Reuel et al. surveyed 1,000 organisations across 20 industries and found that none had reached both planning and operational AI governance maturity simultaneously, a systematic gap they warned "could lead to increased (public) risks from AI systems" [28]. In the event that process-level governance is not reliable, the safety argument falls to the architecture. The question is what that architecture should do as conditions deteriorate, specifically during the marginal conditions between the safe-to-dangerous endpoints.

Current systems see this as a binary: the AI makes its entire set of recommendations or it is turned off. In cases where a binary gate receives marginal conditions, it simply assumes them to be safe, leaving the operator with full-scope tactical advice that the underlying data may no longer support. Wen et al. report the impact, noting that users receiving AI output under deteriorating conditions tend toward over-reliance, accepting recommendations they should question [4]. The question for this review is whether any existing mechanism limits what an AI may recommend, as distinct from whether it may participate at all.

Where a governance failure occurs without any institutional layer to compensate, the stakes are highest. In Malaysia, the choice is made by small-scale fishers on their own, every morning, without support, on vessels under 40 gross register tonnage, with traditional weather knowledge that is eroding as climate patterns shift [1]. The risk profile is documented: wind, weather, and visibility account for 26.7% of maritime accident causes, and small vessels have the highest mean fatality rank for all vessels tested [2]; combined night navigation and heavy weather has the highest consequence scores of any condition tested [3].

There are three governance dimensions framing the space of possible mechanisms (Fig. 1). Dimensions 1 and 3 are addressed in existing work; dimension 2 (advisory scope restriction) is not.

**Fig. 1.** Three governance dimensions in AI decision support systems. Dimensions 1 and 3 appear in existing work; dimension 2 is the gap this paper addresses.

*[Figure 1 — embedded image in submitted .docx]*

The contribution is the second dimension — advisory scope — which existing architectures leave entirely unaddressed. Existing governance mechanisms conflate two distinct variables into a single binary: whether the AI participates. This paper separates them. *G*(*S*) governs participation; *A*_AI(*S*) governs advisory scope. Under *CAUTION* — the novel intermediate state — *G*(*CAUTION*) = 1 (AI active) but *A*_AI(*CAUTION*) = {*Go, Delay*} ⊊ *A*_AI(*SAFE*). A binary architecture has no vocabulary to name this position: for any state where *G* = 1, the full recommendation set is available. *CAUTION* is not a softer version of *SAFE*; it is a formally distinct governance position that binary architectures cannot express.

Two contributions follow. From a review of 72 papers, complemented by three large-scale systematic reviews involving 532 primary references, it is concluded that no architecture identified in this review restricts AI advisory scope as a function of classified environmental safety state, and there is no mechanism within the AI component to cover this gap. The second is a graduated safety-state-gated architecture that fills in the missing space using a formally bounded governance pair between a participation gate *G*(*S*) and an admissible recommendation space *A*_AI(*S*), both conditioned on the environmental safety state, producing an intermediate *CAUTION* mode: restricted advisory scope under marginal conditions, with neither full output nor complete AI withdrawal.

# Methodology

The method of review is not systematic, but rather is structured, with search and coding disciplined, but scope is purposive, extending only to bodies of literature where an advisory-scope restriction mechanism could plausibly appear. Papers were sourced from Scopus, IEEE Xplore, Web of Science, and the ACM Digital Library, using search strings that include AI governance, runtime assurance, safety filters, decision support, autonomy levels, and guardrails; secondary searches focussed on fisheries AI and low-resource deployment. Within this pool of candidates, three systematic reviews were retained as secondary evidence: Indykov et al. [5] (206 papers, 16 architectural tactics), Shamsujjoha et al. [6] (13 guardrail actions, 32 agent studies) and Perez-Cerrolaza et al. [21] (294 references). Seventy-two papers advanced to full review and were coded on four dimensions (TABLE I). Papers sharing a governance topology were grouped into three paradigms plus an application domain.

**TABLE I.** Coding dimensions applied to all reviewed papers.

| Dimension | Values |
|---|---|
| Primary governance target | Participation / Advisory scope / Execution / Oversight |
| Runtime adaptation | Binary (on/off) / Graduated (3+ levels) / None |
| Conditioning variable | Environmental state / AI robustness / Task risk / Human authority / None |
| Recommendation restriction | Yes (bounded output set) / No |

# Literature Review

## Overview of Existing Governance Paradigms

The examined frameworks fall into three paradigms: deterministic safety constraints, which provide provable runtime guarantees; authority allocation, which distributes decision rights between human and AI; and adaptive risk-based systems, which vary AI behaviour across graduated operational levels. Across all three, the governance target is participation, authority, or execution, not advisory scope. A fourth body, fisheries AI and low-resource deployment, is reviewed to determine if this pattern holds in the intended domain of deployment. The review process is summarised in Fig. 2.

## Deterministic Safety Constraints: Binary by Construction

Könighofer et al. formalise shields: runtime mechanisms that intercept AI actions before they reach the environment [8]. Dalrymple et al. require formal proof certificates before AI output is deployed [9]. Bajcsy and Fisac adopt a control-theoretic safety filter [10]. The governance topology is the same in all three: the AI either operates within its safety boundary or is replaced, and the object of governance is execution. This structure also appears in constraint-based planning approaches such as Tumato 2.0 [14]. In every case, the semantic content of AI output is not addressed.

**Fig. 2.** Structured review process showing how four bodies of literature converge on the same gap and motivate the proposed architecture.

*[Figure 2 — embedded image in submitted .docx]*

## Authority Allocation: Who Decides, Not What AI May Recommend

Authority allocation frameworks ask who decides, not what the AI may recommend. Ramos et al., reviewing 91 collaborative intelligence studies, found AI-assisted decision-making dominant across safety-critical industries, but no system varies advisory scope by safety state [11]. Feng et al. propose five levels of autonomy, fixed at design time [12]. Within a cross-domain context, Mussi et al. find all elements of state-conditioned governance across power grids, railway networks and air traffic management, but never assemble these into a runtime model (automation levels are set before deployment and do not change) [30]. As conditions change, the advisory scope does not.

## Adaptive Risk-Based Systems: The Closest Precedents

The adaptive systems literature yields three distinct governance postures. Oversight intensification in Flehmig et al.'s traffic-light degradation index (green/orange/red) triggers progressively intensive supervisory responses by level [7]. The supervisory level of check increases at intermediate orange, but the AI's advisory scope, however, is the same at green and orange. It is the intermediate level that affects the action of the human supervisor, not in the wording of what the AI might say. Kang's GAIE framework cascades code generation across three oversight tiers; at the intermediate tier, a deployment-gate is inserted, and at every tier a broad spectrum of code is generated with no restrictions whatsoever [22].

In execution deferral and re-sensing, Ghaleb et al.'s three-regime gating wrapper (Safe, Borderline, Unsafe) forces execution slowdown and re-observation at the Borderline regime [24]. The policy's output capability remains uncontracted throughout; at Unsafe, the learned policy is replaced by a classical planner.

In autonomous action-class restriction, Sahoo's Agentic Military AI Governance Framework regulates tool access across five response levels, deploying a Control Quality Score to respond in real-time; at intermediate levels, the agent is restricted to reversible actions [23]. This is the closest to scope contraction in the reviewed frameworks and is graduated. The difference is the object of governance: an acting autonomous agent, with restriction conditioned on measured control degradation rather than classified environmental state. Equivalently, Baxi's K-tier permission architecture allows for different sets of permissions based on tiers, conditioned on the AI's own verified robustness [13].

There is a feasible pathway to graduated operational posture for all three postures. Whether or not intermediate levels exist is only a question of location; in all cases examined, the point at which graduation is applied is in human workflows, execution deferral, or agent action classes, not the recommendation content the human decision-maker receives.

## Synthesis: Cross-Paradigm Comparison and the Research Gap

The pattern holds at the application level. None of the fisheries AI systems identified in this review implement formal advisory scope restriction conditioned on environmental state [17]; the only external advisory available to coastal fishers is a binary government warning [16]; and safety governance in low-resource deployment contexts has not been designed from the deployment floor up [15][19].

The four bodies point in the same direction. Deterministic constraints are binary by construction; authority allocation frameworks fix advisory scope at design time; adaptive risk-based systems apply their intermediate levels to human workflows or execution deferral rather than output scope; and the fisheries and low-resource literature offer no formal concept of runtime governance [15][16][17]. Across all reviewed paradigms, the object of governance differs, but none conditions AI advisory scope on classified environmental safety state.

Four literature streams point to the same absence independently. Indykov et al. surveyed 206 papers and found a Safety score of zero for AT11 (rule-based models): despite Safety being one of the two most frequently cited quality attributes, no architectural tactic has been proven to have formal positive influence on it [5]. The Swiss Cheese Model by Shamsujjoha et al. covers 13 guardrail actions for content filtering, blocking and validation; none conditions advisory scope on dynamic environmental risk [6]. The adaptive architectures studied, Flehmig et al. [7], Kang [22], and Ghaleb et al. [24], apply their intermediate tiers to human audit escalation or execution deferral, not to what the AI may say. Behavioural frameworks like Sahoo's [23] throttle the execution space of acting agents, not the recommendation menus presented to human decision-makers.

What differs across every reviewed framework is not just the governance target but the conditioning variable. Baxi on AI robustness [13]; Flehmig et al. on AI degradation [7]; Kang on task regulatory impact [22]; Sahoo on control quality [23]; Ghaleb et al. on epistemic uncertainty [24]. In each case, the trigger is internal to the AI system. The proposed architecture departs from this: it conditions on an independently classified environmental safety state *S* = *f*(*E*), computed outside the AI component. The comparison is summarised in TABLE II.

## The Mechanistic Basis for External Governance

The proposed architecture uses a Symbolic AI Reasoning Engine [34]. The mechanistic evidence below applies more broadly and it establishes that no AI component, irrespective of the technique used, can reliably self-restrict as conditions deteriorate. Three points from the LLM systems literature make the case. LLM inference runs through fixed prefill and decode stages, and the batching, scheduling, and kernel selection are driven by token counts and hardware utilisation, not by the semantic content of the input, leaving no hook in the pipeline at which advisory scope could vary with environmental state [25]. Probing studies show that reasoning breadth is a property of the decoding procedure rather than of what the input contains; externally injected randomness scatters reasoning but cannot produce systematically conservative output under worsening conditions [26]. LLM confidence judgements are poorly calibrated, biased towards overconfidence, and fail to improve with experience, which means a safety-critical system cannot treat the AI's self-reported uncertainty as a reliable risk signal [27]. All three limitations point in the same direction: governance cannot be delegated to the AI component.

**TABLE II.** Coding of reviewed architectures against the four governance dimensions.

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

*Shamsujjoha et al.'s Swiss Cheese Model [6] describes 13 guardrail actions applied to agent artifacts (prompts, plans, tools, FMs) and pipeline stages. All actions are content-focused (block, filter, flag, modify, validate); none condition AI advisory scope on environmental safety state.*

# Proposed Architecture

An AI decision support system generates recommendations for a human decision-maker who retains final authority, rather than an autonomous agent that executes actions directly. A safety-critical system is one where incorrect output may contribute to loss of life, injury or harm to property. As opposed to design-time controls, runtime governance refers to the mechanisms in place to constrain AI behaviour during operation. This paper introduces participation gating, distinguishing whether the AI is allowed to participate or not, and distinguishes between gating and advisory scope, *A*_AI(*S*), which is the set of types of recommendations that the AI can make during participation. An environmental safety state is a classified summary *S* of an observation vector *E*, computed without using the AI, represented as *S* = *f*(*E*). A low-resource environment is characterised by the absence of reliable connectivity, computing infrastructure and institutional support.

Within the scope the governance layer allows, recommendations are generated with the help of a Symbolic AI Reasoning Engine, a classical symbolic artificial intelligence approach in the line of knowledge-based expert systems [34]. As the Mechanistic Basis section establishes, internal self-restraint cannot be relied upon; the solution must be external. The proposed graduated safety-state-gated architecture here conditions both AI participation and advisory scope on a classified environmental safety state, enforced by a layer outside the AI component (Fig. 3). An additional key element of the design is its attempt to address a gap in governance theory: Engin and Hand argue that governance categories should be built as explicit thresholds over continuously monitored dimensions [29], but their proposal lacks an enforcement mechanism. The proposed architecture realises that pattern as an enforced runtime mechanism: continuous environmental observation *E*, deterministic thresholding *S* = *f*(*E*), and three actionable categories each carrying formally differentiated constraints, enforced by construction rather than by design intent.

**Fig. 3.** Graduated safety-state-gated architecture showing environmental classification, the governance pair (*G*(*S*), *A*_AI(*S*)) and advisory scope restriction.

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

The architecture is situated within established governance standards. The NIST AI Risk Management Framework [35] defines risk tiers for AI systems in safety-critical applications; the SAFE/CAUTION/UNSAFE classification operationalises that tiered approach at runtime, with UNSAFE mapping to the highest risk tier where AI participation is suspended and CAUTION to an intermediate tier where advisory scope is formally bounded. Graduated safety constraints are a precedent in safety engineering: IEC 61508 Safety Integrity Levels and ISO 26262 Automotive Safety Integrity Levels both impose progressively stricter design and verification requirements as risk increases, and the A_AI(S) contraction from SAFE to CAUTION mirrors this principle at the advisory scope level. Taken together, the architecture realises the deterministic guard principle of Bloomfield and Rushby [20] — surrounding the AI component with a formally specified, state-conditioned constraint — at the level of advisory scope rather than execution.

## Formal Structure

Let *E* denote the environmental observation vector and *S* = *f*(*E*) a classifier that maps observations to a safety state *S* ∈ {*SAFE, CAUTION, UNSAFE*}. The governance pair (*G*(*S*), *A*_AI(*S*)) operates as TABLE III.

**TABLE III.** Governance pair configuration across the three safety states.

| State | G(S) | A_AI(S) | AI scope |
|---|---|---|---|
| SAFE | 1 (enabled) | {Go, Delay, DepartureTime, Duration} | Full |
| CAUTION | 1 (enabled) | {Go, Delay} | Restricted |
| UNSAFE | 0 (disabled) | ∅ | None |

These sets satisfy the containment relationship *A*_AI(*SAFE*) ⊃ *A*_AI(*CAUTION*) ⊃ *A*_AI(*UNSAFE*) = ∅, which implies the Safety Dominance Property: for all *E*, *AI*(*E*) ⊆ *A*_AI(*S*). Recommendations are bounded to whatever the current safety state permits. This holds by construction: the governance layer supplies a state-specific rule set to the reasoning engine before inference begins, so no rule in the *CAUTION* configuration can produce recommendations outside {*Go, Delay*}.

**Design Principle.** Each safety state admits only those recommendation types that can be justified by the environmental information available in that state. A domain deployment instantiates A_AI(S) by mapping each candidate recommendation type to its evidential requirements and verifying whether those requirements hold at each classified state.

## Formal Properties

Three properties characterise the safety behaviour of the architecture. All proofs are by exhaustive case analysis over the three-element set {SAFE, CAUTION, UNSAFE}; no induction is required.

**Theorem 1 (Totality).** *For all E in its domain, f(E) is defined and returns exactly one element of* {SAFE, CAUTION, UNSAFE}.

*Proof sketch.* Each per-component function gᵢ partitions its input domain exhaustively and without overlap: g_w partitions ℝ≥0 into [0, 22], (22, 27], (27, +∞); g_r and g_m enumerate all categorical values without omission; g_o partitions ℝ≥0 into [0, 1.5), [1.5, 3.5], (3.5, +∞); g_v enumerates {small, medium, big}; g_t partitions [0, 24) into [6.0, 17.0), [17.0, 19.0), [19.0, 24.0) ∪ [0.0, 6.0). Each gᵢ is therefore total. The aggregation f(E) = max_≻ {gᵢ(xᵢ)} over a finite totally ordered set is always defined and returns a unique maximum. The fail-safe rule — if any xᵢ = ⊥ then f(E) = UNSAFE — extends totality to corrupted or missing inputs. □

Totality is the necessary precondition for runtime governance: a classifier with undefined states would leave (G(S), A_AI(S)) without a basis for enforcement at those inputs.

**Theorem 2 (Monotonicity).** *For all S*₁*, S*₂ *∈* {SAFE, CAUTION, UNSAFE}*, if S*₁ *≻ S*₂ *then A_AI(S*₁*) ⊆ A_AI(S*₂*).*

*Proof sketch.* Exhaustive case analysis over the three ordered pairs under ≻:

| Case | S₁ | S₂ | A_AI(S₁) | A_AI(S₂) | Holds? |
|---|---|---|---|---|---|
| 1 | UNSAFE | CAUTION | ∅ | {Go, Delay} | ∅ ⊆ {Go, Delay} ✓ |
| 2 | CAUTION | SAFE | {Go, Delay} | {Go, Delay, DepartureTime, Duration} | {Go, Delay} ⊆ {Go, Delay, DT, D} ✓ |
| 3 | UNSAFE | SAFE | ∅ | {Go, Delay, DepartureTime, Duration} | ∅ ⊆ {Go, Delay, DT, D} ✓ |

Both inclusions in Cases 1 and 2 are strict (⊊), yielding the containment chain A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ stated in TABLE III. □

Monotonicity establishes that the architecture is *consistent*: advisory scope never expands as conditions worsen, regardless of which state transition occurs.

**Theorem 3 (Safety Dominance Property).** *For all E, AI(E) ⊆ A_AI(f(E)).*

*Proof sketch.* The proof is constructive, resting on four structural assumptions: (A1) the reasoning engine generates only recommendation types for which an active rule exists; (A2) the governance layer supplies RS(S) to the engine before any reasoning begins; (A3) G(S) = 0 implies the engine receives no input, so AI(E) = ∅; (A4) no rule produces a type outside its stated conclusion. Exhaustive case analysis on S = f(E):

- *f(E) = UNSAFE*: by A3, AI(E) = ∅ = A_AI(UNSAFE). ✓
- *f(E) = CAUTION*: by A2, the engine receives RS(CAUTION), which contains only rules producing {Go, Delay}; by A1 and A4, AI(E) ⊆ {Go, Delay} = A_AI(CAUTION). ✓
- *f(E) = SAFE*: by A2, the engine receives RS(SAFE); by A1 and A4, AI(E) ⊆ {Go, Delay, DepartureTime, Duration} = A_AI(SAFE). ✓ □

The property holds by construction rather than by runtime monitoring. There is no execution path by which the engine can produce a recommendation type outside its active rule set — the constraint is enforced before inference begins, not after.

## Algorithm Specification

The three algorithms below specify the full governance pipeline. Algorithm 1 implements the safety classifier; Algorithm 2 evaluates the governance pair; Algorithm 3 supplies the rule set and invokes the reasoning engine. Algorithm 3 is the critical path — it shows precisely where RS(S) is loaded relative to inference, which is what makes the Safety Dominance Property hold by construction rather than by monitoring.

```
Algorithm 1: Safety Classification  S = f(E)
Input:  E = (w, r, m, o, v, t)
Output: S ∈ {SAFE, CAUTION, UNSAFE}

1.  If any xᵢ ∈ E is undefined or corrupted: return UNSAFE   [fail-safe]
2.  Compute per-component states:
      S_w ← g_w(w)    // SAFE if w ≤ 22 kn; CAUTION if 22 < w ≤ 27; UNSAFE if w > 27
      S_r ← g_r(r)    // SAFE if r ∈ {none, light, moderate}; CAUTION if heavy; UNSAFE if storm
      S_m ← g_m(m)    // SAFE if none; CAUTION if advisory; UNSAFE if warning or alert
      S_o ← g_o(o)    // SAFE if o < 1.5 m; CAUTION if 1.5 ≤ o ≤ 3.5 m; UNSAFE if o > 3.5 m
      S_v ← g_v(v)    // SAFE if big; CAUTION if small or medium
      S_t ← g_t(t)    // SAFE if 6.0 ≤ t < 17.0; CAUTION if 17.0 ≤ t < 19.0; UNSAFE otherwise
3.  return max_≻ {S_w, S_r, S_m, S_o, S_v, S_t}
      // max_≻: UNSAFE ≻ CAUTION ≻ SAFE — worst-case component dominates
```

```
Algorithm 2: Governance Gate Evaluation
Input:  S ∈ {SAFE, CAUTION, UNSAFE}
Output: G(S) ∈ {0, 1},  A_AI(S) ⊆ R

1.  If S = UNSAFE:
        G(S) ← 0;  A_AI(S) ← ∅
2.  If S = CAUTION:
        G(S) ← 1;  A_AI(S) ← {Go, Delay}
3.  If S = SAFE:
        G(S) ← 1;  A_AI(S) ← {Go, Delay, DepartureTime, Duration}
4.  return G(S), A_AI(S)
```

```
Algorithm 3: RS(S) Supply and Advisory Generation
Input:  E, G(S), A_AI(S)
Output: AI(E) ⊆ A_AI(S)

1.  If G(S) = 0: return ∅               [AI disabled — no inference invoked]
2.  Select rule set:
        If S = SAFE:    RS ← RS(SAFE)    // rules producing {Go, Delay, DepartureTime, Duration}
        If S = CAUTION: RS ← RS(CAUTION) // rules producing {Go, Delay} only
3.  Load RS into reasoning engine         [RS(S) bound before any inference begins]
4.  Execute reasoning engine against E with active rule set RS
5.  AI(E) ← set of recommendation types fired by the engine
6.  Assert AI(E) ⊆ A_AI(S)              [invariant — holds by construction, see Theorem 3]
7.  return AI(E)
```

Step 3 of Algorithm 3 is the enforcement point. RS(CAUTION) contains only rules whose conclusions produce {Go, Delay} — there is no rule in that configuration that can fire DepartureTime or Duration. The Safety Dominance Property is not checked at Step 6; Step 6 is an invariant assertion that records what construction guarantees. An implementation that passes all three algorithms satisfies Theorem 3 without additional runtime verification.

## Computational Complexity

The governance layer is designed for bounded-time, resource-minimal execution. TABLE IV characterises the complexity of each pipeline component.

**TABLE IV.** Computational complexity of the governance pipeline components.

| Component | Time complexity | Space complexity | Notes |
|---|---|---|---|
| Safety classifier f(E) | O(1) | O(1) | Six independent threshold comparisons; no iteration |
| Governance gate G(S), A_AI(S) | O(1) | O(1) | Direct lookup on three-element enum |
| RS(S) selection | O(1) | O(1) | Pre-built rule sets; atomic swap on state change |
| Rule engine execution | O(n) | O(n) | n = number of rules in active RS(S); finite and bounded |
| Full governance pipeline | O(n) | O(n) | Dominated by rule engine; classifier and gate are O(1) |
| State transition (hysteresis) | O(1) | O(1) | Dual-threshold comparison at boundary |

Three properties follow directly from this characterisation. First, the governance layer (Layers 1 and 2, comprising the classifier and gate) runs entirely in O(1) — six threshold comparisons and a maximum over six elements, with no iteration, no learned inference, and no GPU dependency. Second, because RS(CAUTION) ⊂ RS(SAFE), the rule engine executes fewer rules under CAUTION than under SAFE: the more restrictive governance state is also the computationally cheaper one. Third, end-to-end decision latency is dominated by external data acquisition (obtaining w, r, m, o from meteorological feeds), not by governance computation; the pipeline itself adds negligible overhead.

This meets the hard requirement for AI deployed on constrained devices in low-resource settings [17]: bounded-time inference with no dependency on cloud compute or specialist hardware. The architecture runs on commodity smartphones or low-cost single-board computers with no modification to the computational requirements of the governance components.

## The CAUTION Mode

*CAUTION* is what none of the reviewed architectures implements. At *CAUTION*, the AI remains engaged and advises within a formally restricted scope, taking into account marginal conditions. The system withholds precise tactical outputs (departure time, trip duration) since the environmental data can no longer reliably support them. The human operator receives an implicit signal about the restrictions and a participation signal from the AI, enabling calibrated reliance rather than over-reliance.

Only recommendations that are epistemically supportable under marginal environmental conditions are included in the *CAUTION* admissible set. *Go* and *Delay* require only a general assessment of whether current conditions are acceptable for departure. *DepartureTime* and *Duration*, on the other hand, assume future stable and predictable conditions: a departure window requires accurate short-term forecasting, whereas a trip duration estimate assumes stable sea state for the entire planning horizon. Once the system is in *CAUTION*, that predictive confidence is no longer available. The governance layer therefore withdraws tactical optimisation and preserves only coarse operational guidance: the conservative middle position between full advisory capability and complete AI disengagement.

Runtime assurance evidence supports the operational case. All-or-nothing gating enforces safety but destroys utility precisely where bounded operation could preserve it [24][31]; in low-resource settings this creates an unworkable trade-off between a decision vacuum during marginal weather and governance fatigue from disabling the tool when bounded advice could still be safely rendered. Kolt et al. argue that effective governance must intervene early, at calibrated thresholds, before certainty arrives [32]; *CAUTION* is that early intervention, contracting scope while conditions remain marginal.

## Domain Instantiation

The architecture is being developed as a formally specified prototype for AI departure decision support in small-scale coastal fisheries in Malaysia (Kota Kinabalu, Sabah). *E* = {*w, r, m, o, v, t*} where *w* is wind speed, *r* is rainfall intensity, *m* is marine warning level, *o* is ocean state, *v* is vessel category and *t* is time of day. The Symbolic AI Reasoning Engine enforces the Safety Dominance Property by construction, satisfying the offline-first and computationally lightweight requirements of the low-resource deployment context. A dual-threshold hysteresis smoothing layer over the discrete state transitions is a deployment-floor consideration, drawing on the empirically verified runtime-gating stability of Ghaleb et al. [27], to minimise mode-chattering at the classification boundaries of *S* = *f*(*E*) during weather transitions near the margins.

The case shown here is domain independent, representing the documented departure decision process of small-scale fishers in coastal Malaysia, where assessment of environmental conditions (weather, tide, and safety) governs whether fishing proceeds normally, is modified, or is abandoned [33].

**Illustrative scenario.** As environmental parameters deteriorate across three time points, advisory scope contracts from full recommendations at *SAFE*, to {*Go, Delay*} at *CAUTION*, to complete AI disengagement at *UNSAFE*. The fisher receives calibrated guidance at each state rather than full-scope output until abrupt shutdown. The full sequence is shown in Fig. 4.

**Fig. 4.** Illustrative state transition across *SAFE*, *CAUTION*, and *UNSAFE*, showing advisory scope contracting as environmental conditions deteriorate.

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

## Generalisation

The architecture is domain-independent at the structural level. Three steps instantiate it for any new domain: (1) define *E* — the observable parameters relevant to that domain's risk classification; (2) define *S* = *f*(*E*) — per-component threshold functions and worst-case aggregation over the domain-relevant risk dimensions; (3) define *R* and *A*_AI(*S*) — the recommendation type space and the admissible subsets per safety state. The formal properties proved in Section IV — Totality, Monotonicity, and Safety Dominance — transfer automatically to any correct instantiation, because they are proved from the structure of the governance pair rather than from the fisheries-specific values.

**TABLE V.** Illustrative instantiations in two additional safety-critical domains.

| Domain | Example E components | CAUTION mode restriction |
|---|---|---|
| Emergency triage [19] | Patient acuity, resource availability, staffing level | Restrict to {Triage, Refer} — withhold specific treatment protocols under resource scarcity |
| Industrial/transportation safety [21] | Equipment state, worker proximity, ambient hazard | Restrict to {Stop, Alert} — withhold specific procedural steps under elevated hazard |

In each case, the participation gate *G*(*S*) and advisory gate *A*_AI(*S*) remain the two-level governance mechanism; only *E*, *f*(*E*), and *A*_AI(*S*) are re-instantiated for the domain. Whether the three-state governance structure is practically appropriate for any given domain remains an empirical question that domain-specific prototype work must address.

## Deployment Challenges and Limitations

Four deployment challenges are anticipated in the target context. **Connectivity.** The architecture is designed offline-first: the governance classifier f(E) and reasoning engine RS(S) must operate without real-time API access. Environmental data may be pre-cached or sourced from local sensors. The fail-safe rule — if any xᵢ = ⊥, return UNSAFE — ensures graceful degradation when a data feed is unavailable; the system defaults to the most restrictive governance state rather than failing open. **Hardware constraints.** The target deployment hardware is commodity smartphones or low-cost single-board computers (under USD 50). The O(1) governance layer and O(n) rule engine both execute without GPU or cloud compute, and the storage footprint for RS(SAFE) and RS(CAUTION) is minimal. **Threshold maintenance.** Classification thresholds (g_w, g_o, and others) are anchored to MET Malaysia published criteria. As climate patterns shift or MET Malaysia revises its warning thresholds, the gᵢ definitions and corresponding RS(S) must be recalibrated. Any recalibration must preserve the containment property A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅, which is a structural constraint on the recalibration process rather than a property of the thresholds themselves. **Mode-chattering.** At classification boundaries — for example, wind speed near 22 kn — rapid oscillation of S would produce unstable advisory output. This is mitigated by dual-threshold hysteresis: a state transition from SAFE to CAUTION requires sustained exceedance of the upper threshold, and a return transition requires sustained recovery below a lower threshold. Empirical validation of hysteresis parameters is part of the prototype evaluation work.

Three limitations bound the scope of the claims. First, the recommendation type space R = {Go, Delay, DepartureTime, Duration} is domain-specific to the coastal fisheries departure decision context. Extension to another domain requires instantiating a new R and A_AI(S) appropriate to that domain's recommendation vocabulary; the formal properties (Totality, Monotonicity, Safety Dominance) transfer automatically to any correct instantiation. Second, the rule sets RS(SAFE) and RS(CAUTION) require domain expert validation. Encoding errors do not violate the Safety Dominance Property — the construction proof holds regardless of rule content — but they can produce incorrect advisory output within the permitted scope. The Safety Dominance Property bounds what the AI may say, not whether what it says is correct. Third, the architecture governs advisory scope, not final decisions. Human override is unconditional; the operator may act contrary to any AI recommendation at any time. Whether the CAUTION mode produces the intended effect — calibrated reliance rather than over-reliance or non-reliance — is an empirical question that the proposed user study (RQ5) is designed to address.

# Threats to Validity

**Internal validity.** The primary internal threat is threshold selection: are the SAFE/CAUTION/UNSAFE boundaries principled rather than arbitrary? The thresholds for each gᵢ are anchored to independently established sources — MET Malaysia published warning criteria for wind (g_w), rainfall (g_r), and marine warning level (g_m); hydrodynamic seakeeping analysis and a 23-year empirical capsizing dataset for wave height (g_o); vessel-size fatality data for vessel category (g_v); and risk perception scoring for time of day (g_t) [3]. This convergence across methodologically distinct sources reduces the threat to low. A secondary internal threat is rule set completeness: RS(SAFE) and RS(CAUTION) are constructed for the fisheries domain and may not cover novel condition combinations encountered in deployment. This is partially mitigated by the fail-safe rule — any undefined or corrupted input returns UNSAFE — but cannot be fully eliminated without exhaustive domain testing. Prototype fidelity is verified through the three-condition comparative evaluation: 100% Safety Dominance compliance across all 20 test scenarios constitutes the fidelity check between specification and implementation.

**External validity.** Results are demonstrated in one domain — small-scale coastal fisheries in Kota Kinabalu, Sabah, Malaysia — with one vessel population and one regulatory context. The formal properties (Totality, Monotonicity, Safety Dominance) transfer by construction to any correct domain instantiation, but whether the three-state governance structure is practically appropriate in other domains has not been empirically validated. A further external threat concerns engine type: the Safety Dominance proof assumes a rule-based reasoning engine (A1–A4 in Theorem 3). Applicability to ML or LLM advisory components would require a different enforcement argument, since those components cannot provide the rule-conclusion guarantees that A4 requires.

**Construct validity.** The primary evaluation metric — advisory scope compliance rate P(AI(E) ⊆ A_AI(f(E))) — measures structural compliance, not advisory quality. A system can comply formally while producing advice within the permitted scope that is nonetheless unhelpful or poorly calibrated. This is addressed by a secondary metric (decision support utility), but the two measures are not equivalent: the architecture guarantees the first and only targets the second. A further construct threat is simulation fidelity: the 20-scenario evaluation uses historical weather replay and constructed boundary cases. Fishers encountering real departure decisions may produce interaction patterns not represented in the scenario set [16].

**Conclusion validity.** Twenty scenarios may be insufficient to inductively conclude that the formal guarantee holds universally. This threat is substantially mitigated by the construction proof: the Safety Dominance Property holds for all E by Theorem 3, not by passing a test set. Testing is a fidelity check on the implementation, not the primary basis for the safety claim.

# Conclusion

Four independent bodies of literature converge on the same gap. AI governance in safety-critical decision support addresses participation, authority, and agent execution — but not advisory scope. No reviewed architecture implements a recommendation space that contracts as a function of classified environmental safety state. The three closest structural precedents, Flehmig et al.'s traffic-light index [7], Sahoo's five-level protocol [23], and Ghaleb et al.'s safety gate [24], govern supervisory behaviour, agent action classes, and execution deferral respectively, while leaving AI recommendation content unchanged across all intermediate levels. The mechanistic evidence reinforces the gap: no AI component, regardless of technique, can reliably self-restrict as conditions deteriorate [25][26][27]. The consequence falls on the operator in marginal conditions — full-scope tactical advice at the moment the underlying data can no longer support it, with no architectural signal that anything has changed [4].

This paper contributes two things. First, a structured review of 72 papers plus three large-scale systematic reviews [5][6][21] confirms the binary governance gap independently from four bodies of literature, establishing that the absence is structural rather than incidental. Second, the graduated safety-state-gated architecture closes the gap through a formally specified governance pair (*G*(*S*), *A*_AI(*S*)) that produces a *CAUTION* mode — a formally distinct intermediate governance position that no reviewed architecture implements. Under *CAUTION*, *G*(*CAUTION*) = 1 (AI active) and *A*_AI(*CAUTION*) = {*Go, Delay*} ⊊ *A*_AI(*SAFE*): advisory scope is restricted, not participation. The Safety Dominance Property, *AI*(*E*) ⊆ *A*_AI(*f*(*E*)), holds by construction rather than by runtime monitoring — there is no execution path by which the reasoning engine can produce a recommendation type outside its active rule set.

Three formal properties are proved. Theorem 1 (Totality) establishes that *f*(*E*) is defined for all inputs, including corrupted sensor data, so the governance layer is never without a classification basis. Theorem 2 (Monotonicity) establishes that advisory scope never expands as conditions worsen: *A*_AI(*SAFE*) ⊃ *A*_AI(*CAUTION*) ⊃ *A*_AI(*UNSAFE*) = ∅. Theorem 3 (Safety Dominance Property) establishes that AI output is bounded within the admissible scope at every safety state, by construction. Together they characterise a governance mechanism with no formally identifiable path by which AI recommendations can exceed their warranted scope — completeness, consistency, and effectiveness as a composite guarantee.

Immediate next steps are: (1) prototype implementation and experimental validation across three conditions (ungated, binary-gated, and the proposed graduated architecture), measuring advisory scope compliance and decision support utility; (2) a contextual user study with small-scale fishers across the three safety states to assess whether *CAUTION* mode produces calibrated reliance rather than over-reliance or non-reliance; and (3) instantiation in at least one additional safety-critical domain to validate the claim of domain independence empirically. Longer-term work includes a formal certification pathway against IEC 61508 Safety Integrity Levels and maritime safety standards, and extension of *R* to cover recommendation types that require learned inference rather than rule-based reasoning, which would require a different enforcement argument for the Safety Dominance Property.

##### References

[1] L. Yamin, T.-C. Kuo, and N. Aziz, "Interplay of traditional knowledge and adaptive capacity in climate change adaptation of small-scale fishers in central Terengganu, Malaysia," *Frontiers in Marine Science*, vol. 12, p. 1492131, 2025. doi: 10.3389/fmars.2025.1492131

[2] C. Dominguez-Péry, R. Tassabehji, F. Corset, and Z. Chreim, "A holistic view of maritime navigation accidents and risk indicators: examining IMO reports from 2011 to 2021," *Journal of Shipping and Trade*, vol. 8, p. 11, 2023. doi: 10.1186/s41072-023-00135-y

[3] C. Atacan and F. O. Düzbastılar, "Determination of risk perception in small-scale fishing and navigation," *Ege Journal of Fisheries and Aquatic Sciences*, vol. 40, no. 1, pp. 1–14, 2023. doi: 10.12714/egejfas.40.1.01

[4] H. Wen, Z. Sajid, and R. Arunthavanathan, "Risk perception in complex systems: A comparative analysis of process control and autonomous vehicle failures," *AI*, vol. 6, no. 8, p. 164, 2025. doi: 10.3390/ai6080164

[5] V. Indykov, D. Strüber, and R. Wohlrab, "Architectural tactics to achieve quality attributes of machine-learning-enabled systems: A systematic literature review," *Journal of Systems and Software*, vol. 223, p. 112373, 2025. doi: 10.1016/j.jss.2025.112373

[6] Md. Shamsujjoha, Q. Lu, D. Zhao, and L. Zhu, "Swiss cheese model for AI safety: A taxonomy and reference architecture for multi-layered guardrails of foundation model based agents," in *Proc. IEEE 22nd Int. Conf. Software Architecture (ICSA)*, 2025, pp. 37–48. doi: 10.1109/ICSA65012.2025.00014

[7] N. Flehmig, M. A. Lundteigen, and S. Yin, "Implementing artificial intelligence in safety-critical systems during operation: Challenges and extended framework for a quality assurance process," in *Proc. IEEE IECON 2024: 50th Annual Conf. IEEE Industrial Electronics Society*, 2024. doi: 10.1109/IECON55916.2024.10906021

[8] B. Könighofer et al., "Shields for safe reinforcement learning," *Communications of the ACM*, vol. 68, no. 11, pp. 80–90, 2025. doi: 10.1145/3715958

[9] D. Dalrymple et al., "Towards guaranteed safe AI: A framework for ensuring robust and reliable AI systems," *arXiv preprint* arXiv:2405.06624, 2024.

[10] A. Bajcsy and J. F. Fisac, "Human–AI safety: A descendant of generative AI and control systems safety," *arXiv preprint* arXiv:2405.09794, 2024.

[11] I.F. Ramos, G. Gianini, M.C. Leva, and E. Damiani, "Collaborative intelligence for safety-critical industries: A literature review," *Information*, vol. 15, no. 11, p. 728, 2024. doi: 10.3390/info15110728

[12] Z. Feng, J. McDonald, and C. Zhang, "Levels of autonomy for AI agents," *arXiv preprint* arXiv:2506.12469, 2025.

[13] A. Baxi, "The comprehension-gated agent economy: A robustness-first architecture for AI economic agency," *arXiv preprint* arXiv:2603.15639, 2026.

[14] J. Vermaelen and T. Holvoet, "Tumato 2.0: A constraint-based planning approach for safe and robust robot behavior," *Annals of Mathematics and Artificial Intelligence*, vol. 93, pp. 541–567, 2025. doi: 10.1007/s10472-024-09949-3

[15] M. S. Haque and S. Al Jufaili, "Applications of artificial intelligence in fisheries: From data to decisions," *Big Data and Cognitive Computing*, vol. 10, no. 1, art. 19, 2026. doi: 10.3390/bdcc10010019

[16] Abd. Rahim et al., "Survival decisions and adaptation strategies of small-scale fishers in the face of extreme weather impacts in coastal areas," *Journal of Marine and Island Cultures*, vol. 13, no. 3, 2024. doi: 10.21463/jmic.2024.13.3.05

[17] A. Katende, "Rethinking data-efficient artificial intelligence for low-resource settings," *Machine Learning with Applications*, vol. 23, p. 100796, 2026. doi: 10.1016/j.mlwa.2025.100796

[18] A. Longobardi et al., "Peskas: Automated analytics for small-scale, data-deficient fisheries," *SoftwareX*, vol. 29, p. 102028, 2025. doi: 10.1016/j.softx.2024.102028

[19] P. Bhuvaneswari, K. D. V. Prasad, M. Ashraf, and S. Jadhav, "A human-centered hybrid AI framework for optimizing emergency triage in resource-constrained settings," *Intelligence-Based Medicine*, vol. 12, p. 100311, 2025. doi: 10.1016/j.ibmed.2025.100311

[20] R. Bloomfield and J. Rushby, *Assurance of AI Systems from a Dependability Perspective*, SRI Technical Report SRI-CSL-2024-02R3, SRI International, 2025. doi: 10.48550/arXiv.2407.13948

[21] J. Perez-Cerrolaza, J. Abella, M. Borg, C. Donzella, J. Cerquides, F. J. Cazorla, C. Englund, M. Tauber, G. Nikolakopoulos, and J. L. Flores, "Artificial intelligence for safety-critical systems in industrial and transportation domains: A survey," *ACM Computing Surveys*, vol. 56, no. 7, article 176, 2024. doi: 10.1145/3626314

[22] R. Kang, "Governed AI-assisted engineering: Graduated human oversight for agentic code generation in regulated domains," *arXiv preprint* arXiv:2606.22484v2 [cs.HC], Jul. 2026.

[23] S. Sahoo, "The controllability trap: A governance framework for military AI agents," in *Proc. ICLR 2026 Workshop on Agents in the Wild*, Mar. 2026. arXiv:2603.03515.

[24] A. M. Ghaleb, A. S. Allahloh, S. Mejjaouli, M. A. H. Ali, and A. Al-Shayea, "Uncertainty-calibrated safety gating for vision–language–action manipulation under domain shift: Reliability gains and intervention–efficiency trade-offs," *Sensors*, vol. 26, no. 10, p. 3140, May 2026. doi: 10.3390/s26103140

[25] A. K. Kamath, R. Prabhu, J. Mohan, S. Peter, R. Ramjee, and A. Panwar, "POD-Attention: Unlocking full prefill-decode overlap for faster LLM inference," in *Proc. 30th ACM Int. Conf. Architectural Support for Programming Languages and Operating Systems, Volume 2 (ASPLOS '25)*, Rotterdam, Netherlands, 2025, pp. 897–912. doi: 10.1145/3676641.3715996

[26] C. Wu, J. Lu, Z. Ren, G. Hu, Z. Wu, D. Dai, and H. Wu, "LLMs are single-threaded reasoners: Demystifying the working mechanism of soft thinking," *arXiv preprint* arXiv:2508.03440, 2025.

[27] T. N. Cash, D. M. Oppenheimer, S. Christie, and M. Devgan, "Quantifying uncert-AI-nty: Testing the accuracy of LLMs' confidence judgments," *Memory & Cognition*, vol. 54, pp. 375–400, 2025. doi: 10.3758/s13421-025-01755-4

[28] A. Reuel, P. Connolly, K. J. Meimandi, S. Tewari, J. Wiatrak, D. Venkatesh, and M. Kochenderfer, "Responsible AI in the global context: Maturity model and survey," in *Proc. 2025 ACM Conf. Fairness, Accountability, and Transparency (FAccT '25)*, Athens, Greece, 2025, pp. 2505–2541. doi: 10.1145/3715275.3732165

[29] Z. Engin and D. Hand, "Towards adaptive categories: Dimensional governance for agentic AI," *arXiv preprint* arXiv:2505.11579, 2025.

[30] M. Mussi et al., "Human-AI interaction in safety-critical network infrastructures," *iScience*, vol. 28, p. 113400, 2025. doi: 10.1016/j.isci.2025.113400

[31] H. Wang, C. M. Poskitt, J. Sun, and J. Wei, "Pro2Guard: Proactive runtime enforcement of LLM agent safety via probabilistic model checking," *arXiv preprint* arXiv:2508.00500, 2025.

[32] N. Kolt, M. Shur-Ofry, and R. Cohen, "Lessons from complex systems science for AI governance," *Patterns*, vol. 6, p. 101341, 2025. doi: 10.1016/j.patter.2025.101341

[33] T. Gao, "Mapping the Decision-Making Factors of Small-Scale Fishers: A Case Study of Penang," M.Sc. thesis, International Master of Science in Rural Development, University of Pisa / WorldFish (CGIAR), 2024. [Online]. Available: https://hdl.handle.net/10568/152289

[34] V. Belle, "On the relevance of logic for artificial intelligence, and the promise of neurosymbolic learning," *Neurosymbolic Artificial Intelligence*, 2025. doi: 10.1177/29498732251339951

[35] National Institute of Standards and Technology, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1, Gaithersburg, MD: NIST, Jan. 2023. doi: 10.6028/NIST.AI.100-1
