# A Formally Verified Runtime AI Governance Architecture Based on Graduated Safety-State Gating

> **⚠️ SDR-001 APPLIED 2026-09-08 — active working manuscript.** `g_t` is the canonical solar-event classifier: **SAFE sunrise ≤ t < sunset, UNSAFE otherwise**, `g_t(⊥) = UNSAFE`, and it emits **no CAUTION**. The fixed clock 06:00 / 17:00 / 19:00 and its 17:00–19:00 CAUTION band are superseded. **"Daylight" means sunrise ≤ t < sunset.** Canonical figures: Level 2 binds **5.81% / 4.48%**; prediction register **15 CONFIRMED / 9 REFUTED**. Earlier values (7.72% / 5.98%, 22/2, 5,416 / 70 / 6.2%) are provenance only. Submitted and archived versions are historical and are not edited. See `report-c8-migration-2026-09-08.md`.


**Journal:** Safety Science (Elsevier) — primary target  
**Fallback:** Artificial Intelligence Review (Springer) / AI & Ethics (Springer)  
**Type:** Full research article  
**Status:** Research design phase — v1  
**Date started:** 2026-08-06  
**Target submission:** Early 2027

---

> **Note on relationship to conference paper**
> 
> The IPSci 2026 conference paper (AMICT) introduced the graduated safety-state-gated architecture and established the binary governance gap through a structured literature review. That paper is submitted and complete.
>
> This journal paper is an independent research contribution. It shares the same architecture but treats it as the subject of formal analysis, algorithmic specification, prototype implementation, and experimental validation — objectives that are distinct from the conference contribution. Approximately Sections 1–5 overlap significantly with the conference paper in topic; Sections 6–14 are essentially new research.
>
> **Conference contribution:** New architecture  
> **Journal contribution:** New architecture + formal theory + implementation + experimental evidence

---

## Author Information

- **Author:** Mohd Iskandar Samsuddin
- **Affiliation:** [Your university]
- **Email:** iskandarsamsuddin@gmail.com

---

## Abstract

Runtime governance of AI in safety-critical systems is overwhelmingly binary: a shield, verifier or guardrail decides whether the AI participates, while what it may recommend remains unconstrained. This suits systems that act, but fits poorly where an AI advises a human operator under conditions that vary in severity, because it cannot express the position that marginal conditions require — the AI remaining available while the categories of advice it may offer are narrowed. Graduated governance itself is not new; what the reviewed literature does not provide is graduated *advisory scope*, formally conditioned on a classified environmental state.

We specify a two-level governance pair `(G(S), A_AI(S))` that separates AI participation from AI advisory scope, conditioning both on a deterministic classification of environmental state into SAFE, CAUTION or UNSAFE. We prove three properties: totality of the classifier over ideal and operational inputs including faults; monotonicity of the admissible-set map with strict containment `A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅`; and Safety Dominance, `AI(E) ⊆ A_AI(f(E))`, established by construction from a rule-set supply mechanism under stated engine assumptions rather than by filtering output after generation.

The architecture is instantiated for small-scale coastal fisheries departure decisions at Kota Kinabalu, Malaysia, and evaluated along three separate lines of evidence. A prototype rule engine consuming a read-only component-state interface from the governance layer was evaluated exhaustively over its interface contract — 292 episodes, 454 advisory records — with zero admissible-set violations and zero rule-set mismatches. A deterministic replay over 43,848 hourly records isolates the contribution of the second governance level: advisory-scope restriction changes the admissible recommendation set on **5.81%** of departure-window hours relative to binary participation-only governance (**4.48%** under a higher-resolution sensitivity configuration, the spread being a resolution-sensitivity result rather than an uncertainty interval). Over the same record, a traffic-light governance topology instantiating the closest structural precedent diverges from a plain binary gate on **0.00%** of hours — its intermediate level is not observable in AI output.

The evidence is bounded in ways that constrain its reading. Safety Dominance bounds what the AI may recommend; it does not establish physical safety, recommendation optimality, or accident reduction, and operator authority is unconditional throughout. All empirical values are exact descriptive values for one site and window, not estimates. The marine-warning component was unmeasured, making every severity figure a lower bound; the benign-state rule set is unpopulated, so implementation fidelity is demonstrated for the restricted state and the gate-off path only; and no human evaluation was conducted. **Characterisation of runtime performance on target deployment hardware remains pending**, and no acceptance threshold for governance latency exists against which to claim it. The contribution is a formally specified and executable pattern for separating AI participation from state-dependent advisory scope.

---

## Keywords

AI governance; safety-critical decision support; runtime enforcement; formal verification; graduated autonomy; advisory scope restriction; human-AI decision support; small-scale fisheries

---

## 1. Introduction

Safety-critical decision support asks a question that most AI governance mechanisms cannot express. When conditions are marginal — not benign enough to trust an automated recommendation, not dangerous enough to withhold assistance altogether — what should an AI advisory system be permitted to say?

The prevailing answer is: the same thing it says when conditions are benign. Runtime governance for AI in safety-critical settings is overwhelmingly **binary**. A shield, verifier, safety monitor or guardrail decides whether the AI participates, and if it participates its output scope is unconstrained. Surveys covering 91 collaborative-intelligence papers [1] and industrial and transportation domains across automotive, avionics, railway and robotics [2] find the same pattern throughout: the governance decision is *whether*, never *what*. A systematic review of 206 papers and 16 architectural tactics for ML-enabled systems reports that rule-based architectural mechanisms have **no demonstrated formal impact on the Safety quality attribute** — the evidence is scored as insufficient — despite safety being among the most frequently cited attributes in that literature [3].

This binary framing is adequate when the governed system acts. It is a poor fit when the governed system *advises a person who acts*. A human operator facing marginal conditions does not need the AI switched off; they need the AI to stop offering the categories of recommendation that marginal conditions cannot support. An advisory system that answers "depart at 06:40 for a seven-hour trip" under deteriorating sea state is not merely imprecise — it is projecting a confidence the conditions do not warrant, in a form the operator is likely to act on.

### 1.1 Participation and advisory scope are different governance decisions

This paper separates two decisions that binary architectures collapse into one.

**AI participation** — whether the advisory system contributes at all — is governed by a gate `G(S) ∈ {0, 1}`. Every reviewed runtime governance mechanism implements some form of this.

**AI advisory scope** — which *types* of recommendation are admissible — is governed by a map `A_AI(S)` from the safety state to a subset of the recommendation type space. This is the governance level the reviewed literature does not implement against a classified environmental state.

The distinction is not cosmetic. It creates a third governance position that binary mechanisms cannot represent: the AI is **enabled but restricted**. Under this position the operator continues to receive advisory support, and the support is confined to the recommendation types the conditions can bear.

### 1.2 Graduated governance exists; graduated advisory scope is what is investigated

**The contribution claimed here is narrow, and the boundary matters.** Intermediate governance states are not novel. Several reviewed architectures interpose a level between normal operation and shutdown: a traffic-light degradation index that escalates supervisory investigation [4]; restricted operational domains in automated driving; tiered permission sets for economic agents [5]. Intermediate safety or governance states are, by now, a familiar design.

What those architectures graduate is supervisory intensity, execution deferral, operational domain, or the action space of an agent that acts on its own behalf. **On the axis this paper is concerned with — the set of recommendation types presented to a human decision-maker — their control reduces to a participation gate.** The closest structural precedent is explicit about its own design: at the intermediate level the AI continues to operate with unrestricted scope, and what changes is what the human supervisor does [4].

So the claim is not that graduated governance is new. It is that **graduated *advisory scope*, formally conditioned on a classified environmental state and proved to constrain AI output, is the mechanism the reviewed literature does not provide** — and this paper specifies it, proves its properties, implements it, and measures how often it makes a difference.

### 1.3 Why formal proof, implementation fidelity and replay are all required

Three kinds of evidence are needed, and none substitutes for another.

A governance mechanism that cannot be *proved* to constrain output is not a guarantee but an aspiration, so the containment property must be established formally rather than tested empirically. But a proof about a specification says nothing about the software built from it, so implementation fidelity must be measured separately against the built engine. And neither a proof nor a fidelity test says whether the mechanism ever *engages* — an architecture whose restricted state never occurs in practice is formally elegant and operationally empty. That question is empirical, and it is answered by replaying the governance pipeline over a real environmental record.

Keeping the three separate is a matter of not overstating any of them. A theorem is not a hypothesis; an invariant is not a behavioural outcome; a deterministic census value is not a population estimate; and evidence that code matches a specification is not evidence that the specification is correct.

### 1.4 Contributions

This paper makes four bounded contributions.

1. **A formal specification of two-level AI governance.** The governance pair `(G(S), A_AI(S))` is defined over a deterministic classification of environmental state, with the recommendation type space, the participation gate, the admissible-set map and the rule-set supply mechanism given explicit types and semantics (Section 5).
2. **Three proved properties.** Totality of the classifier, monotonicity of the admissible-set map with strict containment, and **Safety Dominance** — `AI(E) ⊆ A_AI(f(E))` under stated engine assumptions — established by construction from the rule-set supply mechanism rather than by runtime filtering (Section 6), with algorithms and complexity bounds (Sections 7–8).
3. **An implemented prototype with measured fidelity.** A Layer 3 rule engine consuming a read-only component-state interface from the governance layer, evaluated exhaustively over its interface contract with zero admissibility violations and zero rule-set mismatches (Sections 9, 11.2).
4. **A retrospective replay quantifying when the second governance level engages.** Over five years of hourly environmental records for a coastal fisheries site, advisory-scope restriction changes the admissible set on **5.81%** of departure-window hours relative to binary participation-only governance (**4.48%** under a higher-resolution sensitivity configuration), while a traffic-light topology instantiating the closest structural precedent diverges from a plain binary gate on **0.00%** of hours (Sections 11.3–11.6).

### 1.5 Research questions

Four questions carry the evaluation, each answered by exactly one kind of evidence.

- **RQ-J1** — Can the Safety Dominance Property be proved formally, and under what assumptions does it hold? *(Formal)*
- **RQ-J2** — What runtime latency and computational overhead does the governance layer introduce on the target deployment hardware? *(Performance)*
- **RQ-J3** — On the retrospective replay, how do the admissible-set outputs of the graduated architecture differ from binary and ungoverned baselines, and what share of the divergence is attributable to advisory-scope restriction alone? *(Empirical trace)*
- **RQ-J4** — Which component of the governance pair accounts for the observed divergence? *(Empirical trace)*

**RQ-J2 is not answered in this paper.** The benchmark harness is validated and a development-machine reference run is complete, but measurement on representative target hardware is outstanding and no acceptance threshold for governance latency exists in the literature. Section 11.7 reports the reference measurement and states plainly what it does not establish.

### 1.6 Scope and application context

The architecture is instantiated for small-scale coastal fisheries at Kota Kinabalu, Sabah, Malaysia, where the departure decision — whether to go to sea given current conditions — is taken daily under exactly the marginal conditions that motivate the work. Small-scale fishers face weather risk with limited forecast access and limited margin for error [6], [7], [8], and the maritime accident record attributes a substantial share of incidents to decision factors rather than equipment failure [9]. The setting also imposes genuine resource constraints, which is why the governance layer is deterministic, offline-capable and small enough to specify exhaustively.

**The domain motivates and constrains the architecture; it is not the contribution.** No claim is made that the thresholds, rules or measured rates transfer to another site or fleet.

### 1.7 What this paper does not claim

Safety Dominance bounds what the AI may recommend. It does not establish physical safety, the correctness or optimality of any recommendation, that departure is safe, or that accidents are prevented. UNSAFE is a governance state in which advisory participation is unavailable — not a determination that harm is certain or that departure is prohibited. **Human decision authority is unconditional throughout.** No component of this work models, records or constrains the operator's decision, and no result here bears on human trust, reliance or behaviour.

### 1.8 Organisation

Section 2 reviews governance mechanisms across the shielding, verification, guardrail and supervisory-control literatures and states the gap narrowly. Section 3 establishes the governance vocabulary and the properties a runtime mechanism must satisfy. Section 4 gives the formal problem statement. Sections 5–8 specify the architecture, prove its properties, present the algorithms and bound their complexity. Section 9 describes the prototype and its fidelity evaluation. Section 10 sets out the experimental design; Sections 11 and 12 report results and ablations. Sections 13–15 discuss, bound and conclude.

---

## 2. Related Work

Runtime AI governance has been approached from several directions that rarely cite one another: shielding in reinforcement learning, policy-level verification, runtime guardrails for language-model agents, supervisory control in industrial safety, and tiered permission systems for autonomous agents. This section organises them by **what each mechanism governs**, because that is the axis on which they differ from the architecture proposed here — not by venue, method or application domain.

Five categories are distinguished, and the distinction between the last two is where the gap lies.

### 2.1 Execution restriction — governing which action is taken

The largest body of work restricts the *action an agent executes*. Shielding for reinforcement learning is the archetype: a formal model of the environment defines a safe region, and a shield blocks or substitutes any action that would leave it [10]. The approach has been extended in many directions — verification-guided shields that activate only in input regions proved unsafe, reducing overhead substantially [11]; probabilistic and adaptive variants that maintain guarantees under shifting dynamics [12]; and constraint-based planners that establish safety by construction over all foreseeable action outcomes [13]. A review of reactive shielding methods finds that the formal machinery differs considerably across approaches while the governance decision does not: every reviewed method implements a binary safe/unsafe boundary, and the review's own safety levels denote constraint *strength* — soft, probabilistic, hard — rather than governance graduation [14].

These mechanisms govern an agent that acts. They filter individual actions, not categories of recommendation, and there is no human decision between the AI output and the world.

### 2.2 Policy-level verification — governing whether the system may operate

A second line verifies the system as a whole before or during deployment. The Guaranteed Safe AI framework formalises this as a world model, a safety specification and a verifier, and argues that empirical testing alone cannot support the guarantees that safety-critical deployment requires [15]. Safety filters for human–AI systems provide the closest formal analogue to a containment property, deriving a safety value function whose boundary determines when a task policy is overridden by a fallback [16]. Assurance from a dependability perspective situates these techniques within established safety-case practice [17].

**This framework is binary at the verification level.** A policy passes and operates, or fails and is disabled. There is no intermediate outcome in which a verified-marginal policy continues to operate with a formally narrowed output space. The architecture proposed here is best read as a domain-specific, state-conditioned instantiation of these principles that adds exactly that intermediate outcome — operating per interaction and per environmental state rather than per policy.

### 2.3 Output filtering and guardrails — governing what is emitted, post hoc

A third line governs the output after generation. Runtime enforcement languages for language-model agents intercept proposed actions and evaluate them against user-authored trigger–predicate–enforcement rules [18]; guardrail agents extract formal specifications from policy documents and verify per-action compliance [19]; and a reference architecture for foundation-model agents catalogues thirteen guardrail action types across fourteen pipeline targets, the most comprehensive taxonomy of output-level controls available [20].

Output filtering is genuinely a control over *what* the system emits, and in that respect it is closer to advisory-scope governance than shielding is. Two differences remain. The controls are applied **per artefact, post generation**, rather than by constraining the admissible space before reasoning begins; and their selection is conditioned on properties of the output or the policy, **not on a classified state of the operating environment**. The taxonomy enumerates governance options comprehensively while leaving the state-conditioned selection mechanism open.

### 2.4 Graduated supervisory control and agent action-space restriction

A fourth category does graduate governance, and two variants matter here.

**Graduated supervisory control.** The closest structural precedent monitors AI degradation — concept drift, outliers, performance decay — and combines the signals into a traffic-light index with three levels, switching to a non-AI backup at the most severe [4]. The three-level design is independently arrived at and independently motivated, which supports the choice of a tripartite classification over a binary one. But the framework is explicit that at the intermediate level the AI continues to operate at unchanged scope; what the index escalates is **supervisory investigation intensity**. The AI has two modes inside a three-level framework: fully on at levels one and two, blocked at level three.

**Agent action-space restriction.** A formally rigorous alternative defines nested permission tiers for economic agents, where a verified robustness vector selects a tier and each tier admits a strictly larger action set than the one below, with bounded-exposure theorems proved over the construction [5]. Structurally this is very close to the containment property used here. It differs in what the gate reads and what the tier constrains: the tier is conditioned on **properties of the agent** — comprehension, robustness, alignment — rather than on a classified state of the environment, and it bounds what an agent may **do on its own behalf** rather than what an advisory system may **say to a person**.

Taxonomic work on agent autonomy sharpens the same point from another direction: autonomy levels are typically fixed deployment-time configurations rather than runtime state-conditioned governance [21].

### 2.5 Human-facing advisory-scope governance — the gap

Restating the five categories against the two governance decisions of Section 1.1:

| Category | Governs | Conditioned on | Participation `G(S)` | Advisory scope `A_AI(S)` |
|---|---|---|---|---|
| Execution restriction [10], [13], [11], [14], [12] | Action executed | Model state / safe region | Yes | No |
| Policy-level verification [15], [16], [17] | System operation | Policy vs. specification | Yes | No |
| Output filtering / guardrails [20], [18], [19] | Emitted artefact | Output or policy properties | Partial | Per artefact, post hoc |
| Graduated supervisory control [4] | Supervisory intensity | AI degradation | Partial | No |
| Agent action-space restriction [5] | Agent action set | Agent robustness | Yes | Yes — but not environment-conditioned |
| **This work** | **Recommendation types offered to a human** | **Classified environmental state** | **Yes** | **Yes** |

**The gap is narrow and should be stated narrowly.** It is not that graduated governance is absent from the literature — Section 2.4 shows it is not. It is that **no reviewed architecture restricts the set of recommendation types an AI may present to a human decision-maker as a function of a classified environmental safety state, with the restriction formally proved to hold.** Each reviewed mechanism has some part of this: three-level classification [4], nested permission sets with proved containment [5], comprehensive output-type taxonomies [20], formal runtime guarantees [10], [15]. None combines them on the advisory axis against environmental state.

Two independent findings corroborate that the absence is real rather than an artefact of the search. The architectural-tactics review reports insufficient evidence that rule-based mechanisms formally deliver safety properties at all [3], which is precisely the mechanism class this architecture uses for governance. And the closest precedent states that no existing framework indexes AI degradation in the graduated manner it proposes [4] — confirming the three-level design space is sparsely occupied, while stopping short of restricting advisory scope within it.

**A fairness qualification travels with the comparison.** The precedent framework conditions its index on AI degradation, not environmental state, and answers a different question correctly. Section 10.1 ports its governance *topology* onto the shared state axis in order to compare admissible-output structure; that is a modelling choice, disclosed as such, and it is neither a reproduction of that system nor a claim that it is deficient.

### 2.6 Standards and governance frameworks

Governance frameworks for AI risk provide vocabulary rather than runtime mechanism. A widely adopted risk-management framework structures organisational AI governance around govern, map, measure and manage functions [22]; maturity modelling surveys responsible-AI practice in a global context [23]; dimensional approaches argue for continuous governance descriptors over discrete categories [24]; and complex-systems perspectives caution against governance designs that assume predictable system behaviour [25]. These operate at organisational and lifecycle level. They do not specify what an advisory system may output under a given environmental condition, and this paper claims no compliance or certification against any of them.

> **[CITATION SUPPORT REQUIRED]** — A comparison against functional-safety integrity-level schemes (for example IEC 61508 SIL, ISO 26262 ASIL) and against maritime regulatory instruments beyond COLREGs Rule 20(b) [26] was planned for this section. **The repository contains no extraction notes for these standards**, and no bibliographic entry for them is supported by repository evidence. The comparison is therefore omitted rather than asserted from general knowledge. Two observations can be made from repository-supported sources: integrity-level schemes assign criticality at **design time** to a system or function, whereas the governance pair here is evaluated **at runtime** per decision episode; and a cross-domain survey notes that design-time criticality classifications are distinct from runtime governance mechanisms [2]. Closing this gap requires a literature pass that this work has not performed.

### 2.7 Domain literature

The application setting is supported by empirical work on small-scale fisher decision-making. Studies of survival decisions and adaptation under extreme weather [6], traditional knowledge and adaptive capacity [7], decision factors mapped at a comparable Malaysian site [27], and risk perception in small-scale fishing and navigation [8] together characterise how departure decisions are actually taken and which environmental factors dominate them. The maritime accident record provides the risk context [9]. Vessel-level operability evidence for Malaysian small fishing boats [28] and wave-height-based departure restriction for small vessels in a comparable fleet [29] ground the vessel-conditioned ocean-state thresholds used in Section 5.

Work on AI in fisheries [30] and automated analytics for data-deficient small-scale fisheries [31] establishes that the computational setting is data-poor rather than data-rich. Research on data-efficient AI for low-resource settings [32] and human-centred hybrid AI under resource constraints [33] motivates a deterministic, offline-capable governance layer over a learned one.

**None of this domain literature establishes the governance gap**, and none is offered as evidence for it. The gap argument rests entirely on Sections 2.1–2.5.

---

## 3. AI Governance Foundations

This section fixes the vocabulary the rest of the paper uses and states the properties a runtime governance mechanism must satisfy to be worth proving anything about. It introduces no new standards framework and claims no compliance with any.

### 3.1 Five things that are routinely conflated

Discussions of "AI safety governance" move between levels of abstraction that behave differently. The paper keeps five separate.

| Level | What it is | Example in this work |
|---|---|---|
| **Coding mechanism** | The implementation technique that realises a constraint | A production rule engine performing a linear scan over a supplied rule set |
| **Governance principle** | The design commitment the mechanism serves | Advisory scope should narrow as conditions worsen |
| **Formal property** | A mathematical statement, provable about the specification | `AI(E) ⊆ A_AI(f(E))` — Safety Dominance, Theorem 6.3 |
| **Runtime enforcement** | The execution-time arrangement that makes the property hold in the built system | Rule sets validated and supplied before reasoning begins (Algorithm 3) |
| **Institutional standard** | An external normative instrument | COLREGs Rule 20(b) [26]; risk-management frameworks [22] |

Confusing these produces two characteristic errors. A mechanism is described as safe because a principle motivated it. Or a property proved about a specification is reported as though it had been demonstrated of the deployed system. This paper treats the formal property (Section 6), the enforcement arrangement (Sections 7, 9) and the evidence that the implementation honours it (Section 11.2) as three distinct claims with three distinct kinds of evidence.

**Referencing a standard is not certification against it.** COLREGs Rule 20(b) supplies a sunset-to-sunrise temporal boundary for navigation lights, and that boundary is used as the source of a threshold. It does not require an AI advisory system to abstain at night; the abstention policy is an architectural choice made here, and Section 14 records it as such. Similarly, a risk-management framework [22] supplies governance vocabulary, not a conformance claim.

### 3.2 Three governance decisions, not one

Section 1.1 distinguished participation from advisory scope. The full set is three, and the third is what most of the reviewed literature governs.

- **Participation** — *may the AI contribute?* A gate `G : S → {0, 1}`.
- **Advisory scope** — *which categories of recommendation are admissible?* A map `A_AI : S → 2^R` over the recommendation type space `R`.
- **Execution** — *may a selected action be performed?* A filter over actions, applied where the system acts rather than advises.

Execution restriction and advisory-scope restriction look similar and are not. Execution restriction operates where the AI output causes the effect; there is no human between output and consequence, and the filter is applied per action. Advisory-scope restriction operates where the AI output is an input to a person's decision; the constraint is over recommendation *types*, and the human remains free to act against any of them or without any of them. **A decision-support system has no execution level to govern** — which is why transplanting execution-restriction mechanisms into an advisory setting yields a participation gate and nothing more.

### 3.3 What a runtime governance mechanism must satisfy

Four properties are required for a state-conditioned governance mechanism to be enforceable rather than aspirational. The first three are proved in Section 6; the fourth is an implementation obligation discharged in Sections 7 and 9.

**Totality.** The classifier must return exactly one state for every input it can encounter, including degraded and incomplete inputs. A classifier that can fail to return leaves the governance pair undefined at exactly the moment governance matters. Totality must extend from ideal inputs to the observation space — faults, absent readings and stale values included (Theorem 6.1).

**Monotonicity.** Admissible scope must never expand as the state worsens. Without it an architecture could, in principle, permit broader advisory output under worse conditions than under better ones. The requirement is a containment ordering over the admissible sets, and strictness matters: if the intermediate state's admissible set equalled the benign state's, the intermediate state would be governance-inert — which is precisely the condition Section 11.6 measures in the traffic-light comparator (Theorem 6.2).

**Enforcement.** The property must constrain actual output, not merely describe intent. Enforcement can be achieved by filtering output after generation or by constructing the generator so that inadmissible output cannot arise. This work takes the second route: the governance layer supplies the rule set before reasoning begins, and the admissibility check occurs at supply time rather than at emission time. Nothing downstream can generate a type absent from the rules it was given (Theorem 6.3).

**Decidability and boundedness.** The governance decision must be computable within the decision episode, over a small fixed state space, with no dependence on the advisory engine's internal state. A governance layer that consulted the AI it governs would be circular; one whose cost grew with the reasoning it governs would be unusable in the settings that motivate it (Sections 7–8).

### 3.4 Determinism as a governance requirement

The governance layer here is deterministic and rule-based — a design choice worth defending, since the reviewed evidence on rule-based mechanisms is not straightforwardly favourable [3].

The relevant limitation of rule-based models is poor adaptability to patterns outside their predefined rules. That is a genuine weakness when rules are used to *approximate* learned behaviour. It is not a weakness when rules are used to *govern* learned behaviour. A governance boundary should be stable, inspectable and identical on every evaluation; it should not drift, learn from the outputs it governs, or vary with an input distribution. **Non-adaptability is the property that makes the boundary trustworthy**, and it is why the governance layer is specified so that it can be enumerated exhaustively (Section 9.5) rather than sampled.

This also bears on the resource setting. A deterministic classifier over a small fixed state space requires no inference at decision time and no network dependency, which is what makes offline operation feasible in low-resource deployment contexts [32], [33]. Whether the resulting implementation meets any particular device budget is an empirical question, open at Section 11.7.

### 3.5 Human authority as a fixed constraint

Every element above operates under one constraint that is not derived from any of them: **the human operator's decision authority is unconditional**. The governance pair bounds what the AI may say. It does not bound what the person may do, does not confer approval, does not withhold permission, and is not modelled anywhere in this work as influencing the operator's choice.

This has a direct consequence for how results are read. `A_AI(UNSAFE) = ∅` means advisory participation is unavailable — not that departure is prohibited, dangerous with certainty, or disallowed. An empty advisory set is silence, not refusal.

---

## 4. Problem Formulation

This section states the problem precisely. It introduces no mathematical model of its own: every symbol used here is defined canonically in Section 5, and this section only fixes what is given, what is required, and what would count as a solution.

### 4.1 Setting

An operator must take a recurring decision under environmental conditions that vary continuously and are observed imperfectly. An AI advisory system is available. The system does not act: its output is an input to the operator's decision, and the operator retains unconditional authority (Section 3.5).

The following are **given**:

- a set of observable environmental quantities and a configured operational parameter, from which a resolved input is obtained;
- a finite set `S` of safety states, ordered by severity;
- a finite recommendation type space `R` — the categories of advice the system can express;
- an advisory engine that, unconstrained, generates recommendations drawn from `R`.

The following are **to be constructed**:

- a classification function assigning exactly one state to every resolved input;
- a governance pair determining, from that state alone, whether the engine participates and which recommendation types are admissible;
- a supply mechanism ensuring the engine cannot produce inadmissible output.

### 4.2 The pipeline and where the problem sits

```
observations ──ρ──▶ resolved input ──f──▶ S ──▶ (G(S), A_AI(S)) ──▶ AI(E) ──▶ human decision
   Layer 1              Layer 1         Layer 2      Layer 2          Layer 3       Layer 4
```

Two boundaries carry the formulation.

**Between Layer 1 and Layer 2** lies resolution: observations may be absent, stale, out of range, or unmeasurable at the deployment site, and the classifier consumes a resolved input rather than raw observations. The operational classifier is the composition of classification with resolution, and totality must hold for the composition — not only for the ideal case (Section 5.2, Theorem 6.1).

**Between Layer 2 and Layer 3** lies the governance interface. The governance layer must determine the state and the admissible set **without consulting the advisory engine**, and the engine must receive its permitted scope as a precondition of reasoning rather than as a filter on its results. A governance layer that read Layer 3 output would be circular; one that filtered after generation would make the containment property contingent on the filter's completeness.

### 4.3 Requirements

A solution must satisfy five requirements. R1–R3 correspond to the properties of Section 3.3; R4 and R5 are boundary conditions.

- **R1 (Totality).** The operational classifier returns exactly one element of `S` for every input in the observation space, including faulted, absent and stale components, under valid startup configuration.
- **R2 (Graduated containment).** `A_AI` is monotone under the severity order, with **strict** containment between adjacent states. Strictness is required: equality at the intermediate state would make that state governance-inert.
- **R3 (Enforcement).** For every input, the generated recommendation set is contained in the admissible set for the governing state; and when participation is withheld, the generated set is empty.
- **R4 (Non-circularity and boundedness).** The governance decision depends only on the resolved input and configuration, never on advisory-engine output or internal state, and is computable within a decision episode over a fixed finite state space.
- **R5 (Human authority).** No element of the mechanism approves, prohibits, overrides or records the operator's decision. An empty admissible set withholds advice; it does not withhold permission.

R3 is the load-bearing requirement, and how it is discharged matters as much as whether it holds. It is established **by construction** — the admissible-type check occurs when the rule set is supplied, before reasoning begins — rather than by inspecting output after the fact.

### 4.4 What "better" means here

The architecture is compared against two baselines over the same environmental record: an **ungoverned** configuration in which the full recommendation set is always admissible, and a **binary** configuration implementing participation gating alone. Both are defined formally in Section 10.1.

"Better" is defined **only** through the authorised evaluation quantities, and the definition is deliberately modest:

- **Divergence** — the share of hours on which two configurations admit different recommendation sets. This measures *whether the mechanisms differ in behaviour*, and nothing else.
- **Isolated second-level contribution** — the divergence attributable to advisory-scope restriction after removing the participation-gate term. This measures *how often the contributed governance level engages*.
- **Implementation fidelity** — whether the built engine honours the admissible sets it was supplied.
- **Formal properties** — whether R1–R3 hold of the specification.

**"Better" is not defined as accident reduction, risk reduction, improved decision quality, higher recommendation accuracy, or increased operator trust.** None of those is measurable on the evidence available here, and a governance architecture that engages more often is not thereby safer. What the isolated second-level contribution establishes is that the contributed mechanism is **not vacuous** at this site — that there exist hours, in a real record, where binary governance leaves the full recommendation set available and graduated governance does not. Whether withholding those types benefits the operator is a separate question requiring evidence this study does not have (Section 14).

### 4.5 Assumptions and scope conditions

The formulation holds under four assumptions about the advisory engine, carried through the proof of Theorem 6.3 and tested as implementation fidelity in Section 11.2: the engine is a rule-based system; the governance layer supplies its rule set before reasoning; participation gating is enforced ahead of rule-set supply; and the engine generates only conclusion types present in the rule set it was given. **If a future engine violates any of these, the containment property ceases to hold as an operational guarantee** — which is why fidelity is measured rather than assumed.

Three scope conditions bound the problem. The state space is small, finite and totally ordered by severity. The recommendation type space is finite and fixed at specification time. And the classification is **deterministic**: identical resolved inputs yield identical states on every evaluation, which is what permits exhaustive enumeration of the governance state space rather than sampling from it.

Finally, the problem as posed is **architectural, not epistemic**. It asks whether advisory scope can be formally restricted as a function of classified environmental state, and whether the restriction can be proved, implemented and observed to engage. It does not ask whether the particular thresholds separating the states are the right ones, or whether the particular admissible sets are optimal. Those are questions about the instantiation, and Section 14 records them as limitations rather than answering them.

---

## 5. Formal Architecture

### 5.1 Architecture Overview

The proposed architecture formalises AI governance for departure decision support as a four-step causal pipeline:

**E → S = f(E) → (G(S), A_AI(S)) → AI(E) → Human Decision**

Each step is formally specified. The environmental–operational state vector **E** captures the observable conditions relevant to departure risk. The deterministic classification function **S = f(E)** maps E to exactly one of three safety states: SAFE, CAUTION, or UNSAFE. The governance pair **(G(S), A_AI(S))** — the core architectural contribution — then determines both whether the AI advisory system participates and what it is permitted to recommend. Finally, the AI generates recommendations **AI(E)** within the scope permitted by the governance pair, and the human decision-maker receives this output and makes the final go/no-go determination.

Human authority is unconditional and final. The architecture provides decision support; it does not automate the departure decision.

The architectural contribution resides in the governance pair (G(S), A_AI(S)). **Graduated governance is not itself novel** — several reviewed architectures interpose intermediate levels between normal operation and shutdown. What they graduate is supervisory intensity, execution deferral, or the action space of an acting agent. **On the axis that matters here — the set of recommendation types presented to a human decision-maker — the control they provide reduces to a participation gate G(S)**: the AI is either enabled (G = 1) or disabled (G = 0). The proposed architecture adds a second governance level A_AI(S) that constrains the AI's advisory scope independently of whether it participates. Under the CAUTION state — the novel intermediate mode that binary architectures cannot express — the AI remains active (G(S) = 1) but operates within a formally restricted recommendation space. Binary architectures have no mechanism to distinguish CAUTION from SAFE: their G(S) returns 1 for both states, leaving scope entirely unconstrained in marginal conditions. The governance pair makes a formally distinct third governance position possible.

The four-step pipeline is specified across four computationally distinct layers, described in Section 5.6. Sections 5.2–5.5 define each component of the pipeline formally. Section 6 proves the formal properties the architecture satisfies.

---

### 5.2 Environmental State Representation

The ideal-input shorthand E combines five condition components with configured vessel category v. Operational observations are resolved before classification; v is not a sampled observation.

**Definition 5.1 (Environmental State Vector).** The environmental–operational state vector is:

**E = (w, r, m, o, v, t)**

where:

| Symbol | Type | Domain | Meaning |
|--------|------|--------|---------|
| w | ℝ≥0 | [0, ∞) | Wind speed (sustained, knots) |
| r | ℝ≥0 × K, K = {0,1} | [0, ∞) × {0,1} | Rainfall: precipitation rate (mm/hr) paired with the derived thunderstorm indicator κ (Definition 5.2a) |
| m | Ordinal categorical | {none, advisory, warning, alert} | Marine warning level |
| o | ℝ≥0 × ℝ≥0 | Wave height and swell-period tuple | g_o reads only significant wave height (metres) |
| v | Configuration | {small, medium, big} | Vessel category by GRT; required before startup |
| t | ℝ | [0, 24) | Time of day (hour, 24-hour clock) |

Vessel category is defined by gross registered tonnage following the Malaysian small boat classification of Yunus (2007), reproduced by Yaakob et al. (2015): small < 10 GRT, medium 10–25 GRT, big > 25 GRT. Tonnage rather than length overall is the discriminating variable because the length bands in that classification overlap — a 12 m vessel falls within both the medium and large length ranges — whereas the tonnage bands are disjoint and exhaustive.

The first four parameters (w, r, m, o) are dynamic: they vary over time and are sourced from external meteorological and marine data feeds. The specific data products, update frequencies, and spatial resolutions for each variable are implementation-level concerns addressed in Section 9. The parameter t is derived from the system clock.

The parameter v differs in kind from the other five. It is not a time-varying condition but a fixed attribute of the operator, constant across every decision episode for a given vessel. This distinction is not merely descriptive: it determines how v enters the classification. Whereas each of the five condition parameters is classified independently and contributes a term to the worst-case aggregation, v is a **conditioning parameter** — it selects the threshold set applied to wave height, rather than producing a classification of its own. Section 5.3.2 gives the formal treatment and the reasoning behind it.

**Definition 5.2 (Governance Independence).** The computation of S = f(E) and the governance pair (G(S), A_AI(S)) at Layer 2 must not depend on any output or internal state of Layer 3. All six components of E must be observable independently of the AI advisory engine.

This is a stronger requirement than simply noting that the inputs are sensor-derived. It is a formal constraint on the causal structure of the architecture: Layer 3 must not influence its own governance configuration, directly or indirectly. A governance layer whose classification could be affected by Layer 3's predictions, outputs, or learned representations would not constitute a formal safety constraint — f(E) would then be defined partly in terms of the system it is intended to govern, creating a feedback path that could undermine the Safety Dominance Property (Property 5.3). In the current architecture, all six components of E are sourced from external meteorological feeds, vessel registry records, and the system clock — none require Layer 3 participation.

*Time and observation context.* For C = {w,r,m,o,t}, Obs_i = (X_i × 𝕋) ∪ {⊥}; y = ρ_{D,τ}(obs) is the resolved input and S = F_{D,τ}(obs,v) = f(y,v). Time retains its clock value in [0,24) and is evaluated with a valid date and canonical solar lookup. g_t is SAFE iff sunrise(date) ≤ t < sunset(date), and UNSAFE otherwise. It emits no CAUTION; exact sunrise is SAFE and exact sunset UNSAFE. Daylight means this astronomical interval. E and f(E) elsewhere abbreviate the valid-input case, with this time context understood.

**Definition 5.2a (Rainfall input and the thunderstorm indicator κ).** The rainfall classifier consumes a structured input, **X_r = ℝ≥0 × K with K = {0, 1}**, so that

**g_r : ℝ≥0 × K → {SAFE, CAUTION, UNSAFE}**,  g_r(r, 1) = UNSAFE for every r.

Here *r* is the precipitation rate in mm/hr and **κ = χ(c)** is a **derived** thunderstorm indicator obtained from the provider's raw present-weather code *c* by the total map

**χ(c) = 1 iff c ∈ {95, 96, 99}, and χ(c) = 0 otherwise, including when c is absent or unrecognised.**

Three properties matter for the formal treatment. First, **c is not the classifier input** — κ is, and κ is computed rather than measured; no instrument observes it. Second, **χ is total into K and never returns ⊥**, so an unavailable weather code does not fault the rainfall component: it yields κ = 0 and the rate-only classification stands. That default is **non-escalating — fail-open for the storm disjunct — and is not a fail-safe**; the required coordinate is the rate, and a missing, invalid or stale *rate* resolves to ⊥ and yields UNSAFE as a fault in the usual way. Third, **κ is escalation-only**: since g_r(r, 1) = UNSAFE and max_≻ is monotone in each argument, an active indication can only raise or preserve f(E), never lower it. Consequently, where the code feed is absent or incomplete, reported g_r figures are lower bounds. κ is **not** a member of the declared exclusion set D; the unexercised storm route and the marine-warning archive gap are distinct phenomena.

*Solar-event provenance.* Sunrise and sunset are read from a frozen daily table computed once for the study site (5.98° N, 116.01° E, UTC+8, no daylight saving); no analysis script recomputes solar geometry. The formulation implements NOAA's published general solar-position equations — the fractional-year equation-of-time and declination series, and the sunrise/sunset hour angle evaluated at the 90.833° zenith NOAA specifies as the approximate combined correction for atmospheric refraction and solar-disc size. Two simplifications are adopted and disclosed: the fractional-year term omits NOAA's intra-day refinement, and the day-angle denominator is held at 365 in leap years; measured against the unsimplified equations at this site these contribute at most 0.116/0.141 min (sunrise/sunset) and 0.457/0.483 min respectively. These are deterministic implementation-sensitivity bounds comparing two models, not an astronomical validation. Classification consumes stored decimal-hour values, not minute-rounded display times. Across 28 sampled comparisons at the study coordinate the implementation differed from the U.S. Naval Observatory Astronomical Applications reference by under one minute in every case (maximum 0.92 min; 0.75 min across the sunrise and sunset events used by *g*_t). This is a bounded agreement check, not a general accuracy claim. COLREG Rule 20(b) requires navigation lights from sunset to sunrise, which establishes the maritime relevance of that boundary; it does not require AI advisory abstention, and the abstention rule is an architecture policy choice.

*Operational exclusion and fail-safe.* v must be configured and D well-formed before startup; t ∉ D. Exclusions are resolved before faults and contribute SAFE. For each remaining component, missing, invalid or stale required observations resolve to ⊥; g_i(⊥) = UNSAFE, so maximum severity gives operational UNSAFE as a corollary, not a separate override preceding all classification. Required clock/date/solar failures use the same fail-safe. Missing swell period does not fault o because g_o consumes wave height only. Historical replay declares D = {m} because no warning archive exists; this is not an instruction to ignore a required live warning feed. Under valid startup configuration, the operational classifier is total.

The inclusion of each parameter in E is empirically grounded: w and o are the primary meteorological departure risk factors identified across three independent fisher studies in the Malaysian coastal context (Rahim et al., 2024; Gao, 2024; Yamin et al., 2025); r uses numeric JPS/DID and MET rainfall bands and m encodes marine-warning level; v captures the well-documented vessel-size fatality gradient across 504 IMO maritime accident reports (Dominguez-Péry et al., 2023); and t reflects empirical findings that night navigation significantly elevates both accident probability and consequence severity for small-vessel operations (Atacan & Düzbastılar, 2023).

---

**Provenance only.** The canonical contract is reasons : Q → 𝒫({fault,hazard,policy}) over the evaluated resolution/classification trace. Fault requires a failed required non-excluded input; hazard denotes a valid environmental non-SAFE band; policy denotes valid nighttime. Labels overlap, SAFE has ∅, and reasons never change S, G(S), A_AI(S), RS(S) or human authority. Runtime reason-set instrumentation is not implemented. Safety Dominance extends to operational S = F_{D,τ} under the same rule-engine assumptions because its proof depends only on S.

### 5.3 Safety State Classification Function

#### 5.3.1 Severity Order

**Definition 5.3 (Severity Order).** Define a total strict order ≻ on the safety state set {SAFE, CAUTION, UNSAFE} as:

**UNSAFE ≻ CAUTION ≻ SAFE**

The order is transitive and total. Its state meanings are governance consequences: UNSAFE means AI advisory participation is unavailable, CAUTION permits restricted advisory scope, and SAFE permits full scope. UNSAFE can arise from environmental bands, required-input faults or valid nighttime policy; it does not establish that departure is prohibited or that physical harm is certain. Human authority remains unconditional.

This ordering is the formal basis for the worst-case aggregation rule applied across the five condition classification functions (Section 5.3.3) and for the Monotonicity Theorem proved in Section 6.

#### 5.3.2 Per-Component Classification Functions

For each condition component xᵢ ∈ {w, r, m, o, t}, define a classification function gᵢ that maps xᵢ to a safety state in {SAFE, CAUTION, UNSAFE}. g_o is conditioned on configured vessel category; g_t uses date and solar context as well as clock time.

**Definition 5.4 (Classification Functions).** The five condition classification functions and their threshold values are:

**Table 1. Condition classification thresholds.**

| Function | SAFE | CAUTION | UNSAFE | Basis |
|----------|------|---------|--------|-------|
| g_w(w) | w ≤ 21.6 kn | 21.6 < w ≤ 27.0 kn | w > 27.0 kn | MET Category 1 onset 40 km/h (21.598 kn, represented as 21.6); Category 2 onset 50 km/h (26.998 kn, represented as 27.0) |
| g_r(r, κ) | κ = 0 and r ≤ 10.0 mm/hr | κ = 0 and 10.0 < r ≤ 20.0 mm/hr | κ = 0 and r > 20.0 mm/hr, **or κ = 1** | JPS/DID lower boundary; MET hourly-rate trigger; advisory governance policy, not a departure prohibition |
| g_m(m) | {none} | {advisory} | {warning, alert} | MET Malaysia three-tier marine warning system |
| g_o(o, v) | *vessel-conditional* | | | See Table 1b |
| g_t(t, date) | sunrise(date) ≤ t < sunset(date) | *(none — g_t emits no CAUTION)* | otherwise; UNSAFE on required clock/date/solar resolution failure | **Boundary: COLREGs Rule 20(b), "from sunset to sunrise" (SDR-001, applied 2026-09-08).** Atacan & Düzbastılar (2023) establish elevated night risk, not the boundary |

**Table 1b. Vessel-conditional wave height thresholds, g_o(o, v).**

| v (GRT) | SAFE | CAUTION | UNSAFE | Basis |
|---|---|---|---|---|
| small (< 10) | o < 1.0 m | 1.0 ≤ o ≤ 1.25 m | o > 1.25 m | Jeong & Im (2023) Table 12 restriction for vessels ≤ 10 m LOA (CAUTION onset); Yaakob et al. (2015) **operational ceiling Hs ≈ 1.25 m** for a 6.54 m hull — top of Sea State 3, the highest band the vessel passes under NORDFORSK |
| medium (10–25) | o < 1.4 m | 1.4 ≤ o ≤ 2.8 m | o > 2.8 m | Hs_KIMO evaluated across 10–15 m LOA (1.13–1.48 m); UNSAFE boundary interpolated |
| big (> 25) | o < 1.5 m | 1.5 ≤ o ≤ 3.5 m | o > 3.5 m | MET Malaysia Category 1 maximum wave height 3.5 m; Hs_KIMO = 1.58 m at 16 m LOA |

Thresholds for g_w are anchored to MET Malaysia's published Kriteria Amaran Angin Kencang dan Laut Bergelora (Strong Wind and Rough Seas Warning Criteria, verified August 2026). Note that g_w is defined over *sustained* wind speed; fisher-interview sources frequently report gust values, and the two must not be conflated when drawing empirical corroboration.

The vessel-conditional thresholds for g_o are supported by a Three-Tier Triangulation, in which each tier contributes to a different row of Table 1b rather than to a single vessel-independent boundary.

*Tier 1 — Hydrodynamics.* Yaakob et al. (2015), applying naval architecture methods (Maxsurf, JONSWAP spectrum, NORDFORSK 1987 criteria) to two traditional Malaysian small fishing boats from the Johor coast (LOA 5.03 and 6.54 m, both < 10 GRT), established vessel-specific operability limits: the 6.54 m hull remained within NORDFORSK limits to Sea State 3 (operational ceiling Hs ≈ 1.25 m) and exceeded them at Sea State 4 (Hs ≈ 1.875 m), while the 5.03 m hull remained within limits only to Sea State 2 (ceiling Hs ≈ 0.5 m). Both passed IMO static stability criteria at every loading condition, establishing that dynamic seakeeping rather than static stability is the binding constraint — and, critically, that the binding wave height differs by vessel. This grounds the small-vessel row.

*Tier 2 — Empirical Risk.* Jeong & Im (2023), analysing 66 Korean small fishing vessel capsizing incidents over 23 years, show that 38% occurred at wave heights at or below 3 m, including incidents at Hs as low as 1.0 m. They derive a length-dependent departure restriction formula from the Wolfson Unit critical wave height framework — Hs_KIMO = √(1 + 0.4 × (0.88 × LOA)) − 1 — producing thresholds from 1.13 m at 10 m LOA to 2.07 m at 24 m LOA, and propose a graduated management scheme restricting vessels ≤ 10 m at Hs ≥ 1.0 m. Their central finding is that 82% of capsizing accidents between 2017 and 2022 occurred on days with no active weather warning, establishing that vessel-independent institutional thresholds systematically fail to capture small-vessel risk. This informs the medium row and corroborates the small row; the medium 2.8 m upper boundary remains conservative interpolation, not a directly measured operating limit.

*Tier 3 — State Policy.* MET Malaysia's Category 1 maximum wave height of 3.5 m anchors the big-vessel CAUTION/UNSAFE boundary, and Hs_KIMO independently returns 1.58 m at 16 m LOA — bracketing the 1.5 m SAFE/CAUTION boundary for that row.

The three tiers converge on a single conclusion: the wave height at which conditions become dangerous is a function of the vessel, not a constant. A 1.5 m threshold corresponds under Hs_KIMO to a vessel of roughly 15 m LOA; the Malaysian hulls studied in the cited seakeeping analysis measure 5.03 and 6.54 m. Applying a single institutional threshold across all vessel classes would classify a 6 m traditional hull as merely marginal in conditions well beyond its documented operability envelope.

**Why vessel category conditions a threshold rather than contributing a term.** An alternative formulation would treat vessel category as a sixth classification function g_v, assigning CAUTION to small and medium vessels and SAFE to big ones, with the result entering the worst-case aggregation alongside the five condition classifications. That formulation is rejected here, and the reason is structural rather than empirical.

Under worst-case aggregation, a term whose value is constant for a given operator establishes a floor on the output but cannot shift a boundary. If g_v(small) = CAUTION unconditionally, then f(E) ≥ CAUTION for every small vessel — but the CAUTION/UNSAFE boundary is determined entirely by the remaining terms, none of which is vessel-aware. A 5 m traditional hull and a 20 m vessel would therefore be classified UNSAFE at precisely the same wave height (3.5 m) and the same wind speed (27 kn). This contradicts Tier 1: Yaakob et al. (2015) report the 6.54 m hull exceeding NORDFORSK operability limits at Hs ≈ 1.875 m, roughly half the wave height at which such a formulation would first classify it UNSAFE. Across the 1.5–3.5 m band — precisely the range in which the CAUTION mode is intended to operate — the formulation would under-classify risk for the vessels the architecture is designed to serve.

The objection that correlated parameters would compensate, high wave heights implying high winds or an active marine warning, is not supported by the accident record. Jeong & Im (2023) report that 82% of capsizing accidents in their 2017–2022 sample occurred on days with no weather warning in force. Distant-storm swell under locally calm wind, with no issued advisory, is the specific case a vessel-independent threshold set fails to capture.

Conditioning g_o on v shifts the boundary rather than flooring the output, which is what the hydrodynamic evidence requires. It also removes a double-count: wave-related risk would otherwise be represented twice for small vessels, once through g_o and again through a constant vessel penalty.

Two consequences follow. First, a small vessel in genuinely benign conditions — Hs below 1.0 m, wind within limits, daylight, no warning — classifies SAFE and receives full advisory scope. Under the alternative formulation SAFE would be unreachable for any vessel below 25 GRT, and since the deployment population operates below 40 GRT (Yamin et al., 2025), the strict containment A_AI(SAFE) ⊃ A_AI(CAUTION) would never be exercised in the target domain. Second, the empirical sources previously invoked to justify a vessel term — the vessel-size fatality gradient across 504 IMO accident reports (Dominguez-Péry et al., 2023), the vessel capacity constraint documented by Rahim et al. (2024), and the population characterisations of Shaffril et al. (2017) and Yamin et al. (2025) — are retained. They justify setting the small-vessel thresholds conservatively: a smaller vessel warrants greater margin because the consequence of misclassification is more severe. That is an argument for tighter boundaries, not for a constant floor.

#### 5.3.3 Classification Function and Totality Theorem

**Definition 5.5 (Safety State Classification Function).** The overall classification function is:

**f(E) = max_≻ {g_w(w), g_r(r, κ), g_m(m), g_o(o, v), g_t(t, date)}**

where max_≻ denotes the maximum under the severity order ≻ from Definition 5.3, returning the greatest element of the set under that order. The output S = f(E) ∈ {SAFE, CAUTION, UNSAFE}.

The aggregation is over five terms. Vessel category v appears within g_o rather than as an independent argument to max_≻, for the reasons given in Section 5.3.2.

The worst-case aggregation rule implements three strict operational principles: (i) UNSAFE dominance — if any condition classifies as UNSAFE, f(E) = UNSAFE, regardless of all others; (ii) CAUTION priority — if no condition is UNSAFE but at least one is CAUTION, f(E) = CAUTION; (iii) SAFE unanimity — f(E) = SAFE only if every condition classifies as SAFE. This reflects the non-compensatory nature of maritime safety risk: calm seas cannot compensate for extreme wind, and a valid nighttime advisory-policy trigger is not cancelled by lower environmental component states. Navigation-light equipment is not a classifier input.

**Totality of f.** For all E in its domain, f(E) is defined and returns exactly one element of {SAFE, CAUTION, UNSAFE}.

This result is proved canonically as Theorem 6.1 in Section 6.2. Totality follows from exhaustive domain coverage of each gᵢ (the domain partition for each component is complete and non-overlapping) and from the fact that max_≻ over a finite totally ordered set is always defined and unique.

Totality is a necessary operational property: a classifier that could fail to return a safety state would leave the governance layer without a basis for enforcing the governance pair (G(S), A_AI(S)) at runtime.

---

### 5.4 Governance Pair: G(S) and A_AI(S)

#### 5.4.1 Recommendation Type Space

**Definition 5.6 (Recommendation Type Space).** Let R = {Go, Delay, DepartureTime, Duration} be the set of AI recommendation types available to the advisory system. *Go* recommends departure within the configured advisory scope without authorising or legally permitting it; *Delay* advises postponement without specifying an alternative time; *DepartureTime* specifies an optimised departure window; and *Duration* specifies a recommended trip duration, not a guarantee of physical safety. The four types correspond to the full structure of the small-scale fisher departure decision — whether to go, when to go, and for how long.

#### 5.4.2 Level 1: AI Participation Gate G(S)

**Definition 5.7 (AI Participation Gate).** Define G : {SAFE, CAUTION, UNSAFE} → {0, 1} as:

- G(SAFE) = 1 (AI enabled)
- G(CAUTION) = 1 (AI enabled)
- G(UNSAFE) = 0 (AI disabled)

When G(S) = 0, the AI advisory engine is disabled and generates no output. When G(S) = 1, the engine is active. A binary governance architecture implements only G: it can express AI-on and AI-off but has no mechanism to express any intermediate governance position. Under SAFE and CAUTION, G(S) = 1 in both states — the participation gate alone cannot distinguish between them.

#### 5.4.3 Level 2: AI-Admissible Recommendation Space A_AI(S)

**Definition 5.8 (AI-Admissible Recommendation Space).** Define A_AI : {SAFE, CAUTION, UNSAFE} → 2^R as:

- A_AI(SAFE) = {Go, Delay, DepartureTime, Duration}
- A_AI(CAUTION) = {Go, Delay}
- A_AI(UNSAFE) = ∅

The containment chain A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ follows directly from these definitions.

#### 5.4.4 The Governance Pair

**Definition 5.9 (Governance Pair).** The architecture is governed by the pair (G(S), A_AI(S)). Table 2 summarises the governance configuration across all three safety states.

**Table 2. Governance configurations by safety state.**

| S | G(S) | A_AI(S) | Advisory scope |
|---|------|---------|----------------|
| SAFE | 1 | {Go, Delay, DepartureTime, Duration} | Full |
| CAUTION | 1 | {Go, Delay} | Restricted |
| UNSAFE | 0 | ∅ | None |

The CAUTION state is the architectural contribution. Under SAFE and CAUTION, G(S) = 1 in both — the participation gate is identical. The governance distinction between SAFE and CAUTION lies entirely in A_AI(S): under CAUTION, the admissible recommendation space contracts to {Go, Delay}, excluding DepartureTime and Duration. A binary governance architecture, having no Level 2 mechanism, cannot express this: it must either permit the full recommendation space or produce no advisory output at all.

The restriction of A_AI(CAUTION) to {Go, Delay} is a conservative architecture policy motivated by the additional forecasting demands of DepartureTime and Duration. The classifier does not measure the accuracy of individual recommendations or prove that coarse guidance is correct. The theorem constrains recommendation types; empirical validation of advice and user reliance remains separate.

When f(E) = CAUTION and Go ∈ A_AI(CAUTION), the specified interface may present a state-dependent qualifier (e.g., "Departure is possible — exercise caution"). To be precise: Layer 3 returns the recommendation type Go ∈ R, unchanged. The qualifier string is a pure rendering operation applied at Layer 4 (the Human Decision interface), not a modification of the type. This distinction is important for formal correctness: Go under CAUTION is the same element of R as Go under SAFE — the set A_AI(CAUTION) = {Go, Delay} contains exactly those two types, with no sub-typed variants. Set containment is preserved; the qualifier is presentation logic external to the formal model.

---

### 5.5 Formal Properties

The architecture must satisfy three formal properties. All three are proved in Section 6.

**Property 5.1 (Participation Constraint).** G(S) = 0 ⟹ A_AI(S) = ∅.

When the participation gate is closed (S = UNSAFE), the admissible recommendation space must be empty. Deterministic safety classification overrides AI advisory reasoning unconditionally. This follows from Definitions 5.7–5.8: A_AI(UNSAFE) = ∅ is a direct definition, not a runtime check. A system in which G(S) = 0 but A_AI(S) ≠ ∅ could admit advisory output despite a closed participation gate — a governance failure.

**Property 5.2 (Advisory Restriction Constraint).** S = CAUTION ⟹ A_AI(CAUTION) ⊊ A_AI(SAFE).

The CAUTION state produces a strictly smaller admissible recommendation space than SAFE. This property formally distinguishes CAUTION from SAFE: CAUTION is not SAFE with a warning label but a governance state with a reduced advisory scope. The strict subset relationship (⊊ rather than ⊆) confirms that the restriction is non-trivial — at least one recommendation type is excluded under CAUTION that is permitted under SAFE. From Definition 5.8: A_AI(SAFE) \ A_AI(CAUTION) = {DepartureTime, Duration} ≠ ∅. ∎

**Definition 5.11 (AI Output Mapping).** Let AI(E) denote the set of recommendation types generated by the advisory engine for environmental state E. The mapping is defined as:

AI(E) = Reasoning Engine(E, RS(S)) &nbsp;&nbsp; if G(S) = 1  
AI(E) = ∅ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if G(S) = 0

where S = f(E). When G(S) = 0 (S = UNSAFE), the advisory engine receives no input and its output is defined as the empty set by this mapping — not merely by the engine's behaviour. This explicit definition makes the proof of Property 5.3 for the UNSAFE case immediate: AI(E) = ∅ = A_AI(UNSAFE).

**Property 5.3 (Safety Dominance Property).** For all E, AI(E) ⊆ A_AI(f(E)).

The AI can only generate recommendations within the admissible space defined by the current safety state. This is the load-bearing safety property of the architecture. It guarantees that no environmental state can elicit an AI recommendation that exceeds the admissible scope for that state. The UNSAFE case follows directly from Definition 5.11: when f(E) = UNSAFE, G(S) = 0, so AI(E) = ∅ = A_AI(UNSAFE), and ∅ ⊆ ∅ holds trivially.

Proof deferred to Section 6.4. The proof is constructive and depends only on the RS(S) rule set supply mechanism described in Section 5.6.

---

### 5.6 Layer Architecture and RS(S) Supply Mechanism

#### 5.6.1 Four-Layer Structure

The formal pipeline is implemented as four computationally distinct layers:

**Table 3. Four-layer architecture.**

| Layer | Name | Function | Computational character |
|-------|------|----------|------------------------|
| 1 | Environment Input | Supplies observations for {w,r,m,o,t} with clock/date/solar context; v is configured separately | Observable, non-AI |
| 2 | Deterministic Governance | Computes S = f(E); derives G(S) and A_AI(S); selects RS(S) | Deterministic, O(1), threshold comparisons |
| 3 | AI Advisory Reasoning | Generates AI(E) within RS(S) | Rule-based, configured per safety state by Layer 2 |
| 4 | Human Decision | Fisher receives advisory; makes final go/no-go | Human authority, always final |

Causal flow is strictly unidirectional: Layer 1 → Layer 2 → Layer 3 → Layer 4. No feedback exists from Layer 3 to Layer 2. The advisory engine cannot influence its own governance configuration — a configuration that Layer 3 outputs could affect would not constitute a formal safety constraint. Layer 2 is computationally independent of Layer 3: if the advisory engine is unavailable, the governance layer continues to classify environmental states and can signal that no AI output is available. Governance holds independently of advisory engine availability.

Layer 1 inputs must all be observable without invoking the AI system. This is the governance independence requirement: the classification function f(E) must not depend on Layer 3 in any way. In the current architecture, all six components of E are sourced from meteorological APIs, vessel registry records, and the system clock — none require Layer 3 participation.

Layer 4 represents human authority, which is unconditional. The fisher may override any AI recommendation. The governance pair constrains what the AI can say; it does not constrain what the human can decide.

#### 5.6.2 RS(S) Rule Set Supply Mechanism

The Safety Dominance Property (Property 5.3) holds by construction rather than by runtime filtering. The construction depends on the following mechanism.

**Definition 5.10 (RS(S) Rule Set Supply).** For each safety state S, define the rule set RS(S) as the set of production rules supplied by Layer 2 to Layer 3 before any advisory reasoning begins:

- RS(SAFE) = rules producing recommendations in {Go, Delay, DepartureTime, Duration}
- RS(CAUTION) = rules producing recommendations in {Go, Delay} only
- RS(UNSAFE) = ∅ — never supplied; G(UNSAFE) = 0 disables Layer 3 entirely

Layer 3 is specified as a production rule engine, and its runtime fidelity has been evaluated against this specification (F1–F3, Section 9). The engine fires only rules present in the currently active RS(S). Crucially, no rule in RS(CAUTION) has a conclusion that produces DepartureTime or Duration — those recommendation types are structurally absent from the CAUTION rule set. The engine has no mechanism to generate a type for which no active rule exists. Under the stated engine assumptions, the Safety Dominance Property holds by construction: it is a structural consequence of how RS(CAUTION) is constructed, not an assertion that must be checked at runtime.

This is the formal basis for the proof by construction in Section 6.4. The distinction between construction-time enforcement and runtime filtering is material. A runtime filter applied to Layer 3 outputs — one that inspects the generated recommendation and discards it if the type is not in A_AI(S) — could fail, be bypassed, or have edge cases in which the filter condition is evaluated incorrectly. RS(S) supply eliminates these failure modes: the constraint is in place before generation begins. A correct rule engine with a correctly constructed RS(CAUTION) cannot produce DepartureTime or Duration under any input E.

The actual content of RS(SAFE) and RS(CAUTION) — the individual production rules and their conditions — is implemented and specified in the Layer 3 prototype specification; Section 9 presents it. Section 5 only defines the supply mechanism and its governance role.

#### 5.6.3 Rule-Based Implementation at Layer 3

Layer 3 is specified as a rule-based symbolic reasoning engine, rather than a machine learning model or large language model, for three reasons. First, the Safety Dominance Property must be provable, not merely tested: a rule-based engine with finite, explicitly defined rule sets RS(S) admits exhaustive static verification — every rule's conclusion type can be inspected against A_AI(S) at design time. A learned model does not admit this: its output space is not enumerable from its parameters. Second, the fixed-size classifier and governance lookups are O(1); rule-engine execution cost depends on the active rules and evaluation strategy and remains an implementation/evaluation concern in Sections 8–9. Third, governance independence is structurally maintained when Layer 3 is a deterministic rule engine: there is no learned representation that could drift, be fine-tuned, or adapt in a way that affects governance behaviour. A machine learning model at Layer 3 could, in principle, learn to produce recommendation types outside its training distribution — the rule-based engine cannot.

Full justification for the Layer 3 design decision, including formal arguments against alternative implementations and the implemented rule set, is provided in the Layer 3 prototype specification accompanying this work.

---

### 5.7 Section Summary

Table 4 collects the formal symbols defined in this section.

**Table 4. Symbol summary for Section 5.**

| Symbol | Meaning |
|--------|---------|
| E = (w, r, m, o, v, t) | Environmental–operational state vector (Definition 5.1) |
| ≻ | Severity order: UNSAFE ≻ CAUTION ≻ SAFE (Definition 5.3) |
| gᵢ | Classification function for condition xᵢ ∈ {w, r, m, o, t} (Definition 5.4) |
| g_o(o, v) | Wave height classification, conditioned on vessel category (Definition 5.4, Table 1b) |
| S = f(E) | Safety state classification function — worst-case aggregation (Definition 5.5) |
| R | Recommendation type space {Go, Delay, DepartureTime, Duration} (Definition 5.6) |
| G(S) | AI participation gate — Level 1 governance (Definition 5.7) |
| A_AI(S) | AI-admissible recommendation space — Level 2 governance (Definition 5.8) |
| (G(S), A_AI(S)) | Governance pair — the core architectural contribution (Definition 5.9) |
| RS(S) | Rule set supplied to Layer 3 before advisory reasoning begins (Definition 5.10) |
| AI(E) | AI-generated recommendations: Reasoning Engine(E, RS(S)) if G(S) = 1; ∅ if G(S) = 0 (Definition 5.11) |

The formal pipeline:

**E → S = f(E) → (G(S), A_AI(S)) → AI(E) → Human Decision**

Section 6 proves Theorems 5.1–5.3 (Totality, Monotonicity, Safety Dominance Property) with full case analysis. Section 7 specifies the algorithms implementing f(E) and the RS(S) supply mechanism. Section 9 presents the implemented prototype and its rule sets, and Section 10 the evaluation design. The underlying evidence is closed — implementation fidelity (F1–F3) and the empirical-trace results (E1–E4, E6) have been evaluated — with the exception of target-hardware performance (E5), which remains open pending benchmarking on a representative physical device.

---

## 6. Theoretical Analysis

### 6.1 Overview

This section proves the three formal properties stated in Section 5. All proofs proceed by exhaustive case analysis over the finite state set {SAFE, CAUTION, UNSAFE} — no induction is required. The proofs are by construction: they depend only on the definitions given in Section 5, not on runtime behaviour or empirical observation.

The three theorems and their dependencies are:

- **Theorem 6.1 (Totality of f):** every environmental state E maps to exactly one safety state S. This is a necessary precondition for the other two theorems — they presuppose that f(E) is always defined.
- **Theorem 6.2 (Monotonicity of A_AI):** as the safety state becomes more severe, the AI admissible recommendation space never expands. Properties 5.1 and 5.2 follow as corollaries.
- **Theorem 6.3 (Safety Dominance Property):** the AI can only generate recommendations within the admissible space defined by the current safety state. This is the load-bearing safety theorem; it holds by construction from the RS(S) supply mechanism.

Together, the three theorems characterise the full safety behaviour of the governance pair (G(S), A_AI(S)): the classifier is total, the advisory scope tightens monotonically with risk, and AI output is bounded within that scope at every state.

---

### 6.2 Theorem 6.1: Totality of f

**Theorem 6.1 (Totality of f).** For all E in its domain, f(E) is defined and returns exactly one element of {SAFE, CAUTION, UNSAFE}.

**Proof.** It suffices to show (i) each condition classification function is total over its domain, and (ii) max_≻ over a finite totally ordered set is always defined and unique.

*(i) Totality of each classification function.*

- **g_w:** The three intervals [0, 21.6], (21.6, 27.0], (27.0, +∞) partition ℝ≥0 exhaustively with no gaps and no overlaps. Every w ∈ ℝ≥0 falls in exactly one interval. ✓
- **g_r:** Two-argument, with domain ℝ≥0 × K where K = {0, 1}. Totality follows in two exhaustive cases over κ. At **κ = 1**, g_r(r, 1) = UNSAFE for every r, independently of the rate. At **κ = 0**, the rate intervals [0, 10.0], (10.0, 20.0], (20.0, +∞) partition ℝ≥0 exhaustively with no gaps and no overlaps. The two cases are disjoint and cover K, so every pair (r, κ) receives exactly one classification. ✓ *(The rate partition alone does not exhaust the domain of g_r — see Definition 5.2a.)*
- **g_m:** The four values {none, advisory, warning, alert} constitute the complete domain of m. Each is assigned to exactly one classification (SAFE, CAUTION, UNSAFE, UNSAFE respectively). ✓
- **g_o:** Two-argument, with domain ℝ≥0 × {small, medium, big}. Totality follows in two steps. First, for each fixed v, the corresponding row of Table 1b induces three intervals partitioning ℝ≥0 exhaustively with no overlap — [0, 1.0), [1.0, 1.25], (1.25, +∞) for small; [0, 1.4), [1.4, 2.8], (2.8, +∞) for medium; [0, 1.5), [1.5, 3.5], (3.5, +∞) for big. Second, {small, medium, big} is finite and exhausts the domain of v. Every pair (o, v) therefore selects exactly one row and falls within exactly one interval of that row. ✓
- **g_t:** Given valid date and solar context, [sunrise(date),sunset(date)) and its complement partition [0,24). They map to SAFE and UNSAFE respectively; the component is total without being surjective onto all three states. Required time-dependency failures map to UNSAFE in the operational extension. ✓

In each case the domain is partitioned into exhaustive, mutually exclusive subsets, each mapped to exactly one element of {SAFE, CAUTION, UNSAFE}. Each function is therefore total.

Note that the two-argument form of g_o does not weaken the argument. Parameterisation by a finite index set preserves totality provided each induced partition is itself exhaustive, which the three rows of Table 1b are by construction.

*(ii) Totality of max_≻.*

max_≻ takes the set {g_w(w), g_r(r, κ), g_m(m), g_o(o, v), g_t(t, date)} ⊆ {SAFE, CAUTION, UNSAFE} and returns the greatest element under ≻ (Definition 5.3). Since ≻ is a total strict order on a finite non-empty set, the maximum always exists and is unique. ✓

Therefore f(E) = max_≻ {g_w(w), g_r(r, κ), g_m(m), g_o(o, v), g_t(t, date)} is defined and returns exactly one element of {SAFE, CAUTION, UNSAFE} for all E. ∎

**Operational extension.** With configured v and well-formed D, resolution first discharges exclusions, then validation/freshness of required inputs. Each required ⊥ has g_i(⊥) = UNSAFE, so max-severity yields UNSAFE. This establishes totality of F_{D,τ} including required resolution failures. Missing v refuses startup and is not a runtime classification. This is the Appendix C C.1b extension of the ideal theorem.

**Significance.** Theorem 6.1 establishes **completeness**: the safety classifier has no undefined states — every combination of observable environmental conditions, including incomplete inputs, maps to exactly one safety state. This is a necessary operational property: a classifier that could fail to return a state would leave Layer 2 without a basis for deriving G(S) and A_AI(S) at runtime, making the governance pair unenforceable. Totality is therefore the precondition that enables the remaining two theorems.

---

### 6.3 Theorem 6.2: Monotonicity of A_AI

Formal safety architectures require that safety constraints tighten consistently as risk increases. Bloomfield & Rushby (2025) establish this as a core expectation of deterministic guards surrounding AI components; Dalrymple et al. (2024) require it of world model safety specifications under increasing uncertainty. The following theorem proves the proposed architecture satisfies this requirement.

**Theorem 6.2 (Monotonicity of A_AI).** For all S₁, S₂ ∈ {SAFE, CAUTION, UNSAFE}, if S₁ ≻ S₂ then A_AI(S₁) ⊆ A_AI(S₂).

*Informally:* as the safety state becomes more severe, the AI admissible recommendation space never expands — it either contracts or remains a subset of the less severe state's space.

**Proof.** From Definition 5.3, the severity order ≻ on {SAFE, CAUTION, UNSAFE} produces exactly three ordered pairs: (UNSAFE, CAUTION), (CAUTION, SAFE), and (UNSAFE, SAFE). We verify each case using the set definitions from Definition 5.8.

**Case 1: S₁ = UNSAFE, S₂ = CAUTION (UNSAFE ≻ CAUTION).**

A_AI(UNSAFE) = ∅ and A_AI(CAUTION) = {Go, Delay}.

∅ ⊆ {Go, Delay} holds trivially — the empty set is a subset of every set. ✓

**Case 2: S₁ = CAUTION, S₂ = SAFE (CAUTION ≻ SAFE).**

A_AI(CAUTION) = {Go, Delay} and A_AI(SAFE) = {Go, Delay, DepartureTime, Duration}.

Every element of A_AI(CAUTION) — namely Go and Delay — is also an element of A_AI(SAFE). Therefore {Go, Delay} ⊆ {Go, Delay, DepartureTime, Duration}. ✓

**Case 3: S₁ = UNSAFE, S₂ = SAFE (UNSAFE ≻ SAFE, by transitivity of ≻).**

A_AI(UNSAFE) = ∅ and A_AI(SAFE) = {Go, Delay, DepartureTime, Duration}.

∅ ⊆ {Go, Delay, DepartureTime, Duration} holds trivially. ✓

All three ordered pairs satisfy the subset condition. Theorem 6.2 holds. ∎

**Corollary 6.2 (Strict Monotonicity).** The inclusions in Cases 1 and 2 are strict: A_AI(UNSAFE) ⊊ A_AI(CAUTION) ⊊ A_AI(SAFE). This produces the containment chain:

**A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅**

The containment is not coincidental — it follows necessarily from the severity ordering on S and the set definitions of A_AI(S).

**Corollary 6.2b (Properties 5.1 and 5.2).** Both governance constraints stated in Section 5.5 follow directly.

*Property 5.1 (Participation Constraint):* G(S) = 0 ⟹ A_AI(S) = ∅. G(S) = 0 if and only if S = UNSAFE (Definition 5.7). A_AI(UNSAFE) = ∅ by Definition 5.8. Therefore G(S) = 0 ⟹ A_AI(S) = ∅. ✓

*Property 5.2 (Advisory Restriction Constraint):* S = CAUTION ⟹ A_AI(CAUTION) ⊊ A_AI(SAFE). This is precisely Case 2 of Theorem 6.2, with the strict subset confirmed by Corollary 6.2: A_AI(SAFE) \ A_AI(CAUTION) = {DepartureTime, Duration} ≠ ∅. ✓

**Significance.** Theorem 6.2 establishes **consistency**: the architecture never relaxes safety constraints as risk increases. As environmental conditions deteriorate — as S moves up the severity order — the AI advisory scope never suddenly expands. The CAUTION state is not SAFE with extra information: it is a governance state with a formally smaller and provably distinct advisory scope. Any architecture that does not satisfy Monotonicity could, in principle, permit broader AI advisory output under worse conditions than under better ones — a governance failure that Theorem 6.2 structurally prevents.

---

### 6.4 Theorem 6.3: Safety Dominance Property

**Theorem 6.3 (Safety Dominance Property).** For all E in its domain:

**AI(E) ⊆ A_AI(f(E))**

and as a special case: if f(E) = UNSAFE then AI(E) = ∅.

**Proof.** The proof proceeds by exhaustive case analysis on S = f(E), which is total by Theorem 6.1. Since S ∈ {SAFE, CAUTION, UNSAFE}, there are exactly three cases. The proof relies on four assumptions about the Layer 3 implementation, which correspond to the causal flow illustrated in Figure 2: Layer 2 supplies RS(S) to Layer 3 *before* inference begins, and Layer 3 is a deterministic rule engine that cannot generate types outside its active rule set.

- **(A1) Rule-based engine.** Layer 3 generates only recommendation types for which an active rule exists in its current rule set.
- **(A2) RS(S) supply.** Layer 2 supplies RS(S) to Layer 3 before any reasoning begins (Definition 5.10): RS(SAFE) contains only rules producing recommendations in {Go, Delay, DepartureTime, Duration}; RS(CAUTION) contains only rules producing recommendations in {Go, Delay}; RS(UNSAFE) = ∅ and is never supplied.
- **(A3) Gate enforcement.** If G(S) = 0, Layer 3 receives no input and AI(E) = ∅ (Definition 5.11).
- **(A4) Engine fidelity.** The rule engine fires only rules present in the active RS(S). No rule produces a recommendation type outside its stated conclusion.

**Case 1: f(E) = UNSAFE.**

By Definition 5.7, G(UNSAFE) = 0. By (A3), Layer 3 receives no input and AI(E) = ∅. By Definition 5.8, A_AI(UNSAFE) = ∅. Therefore AI(E) = ∅ = A_AI(UNSAFE), and in particular AI(E) ⊆ A_AI(UNSAFE). ✓

**Case 2: f(E) = CAUTION.**

By Definition 5.7, G(CAUTION) = 1, so Layer 3 is active. By (A2), Layer 3 receives RS(CAUTION), which contains only rules producing recommendations in {Go, Delay}. By (A4), the engine produces only recommendation types present in RS(CAUTION). Therefore AI(E) ⊆ {Go, Delay} = A_AI(CAUTION). ✓

**Case 3: f(E) = SAFE.**

By Definition 5.7, G(SAFE) = 1, so Layer 3 is active. By (A2), Layer 3 receives RS(SAFE), which contains only rules producing recommendations in {Go, Delay, DepartureTime, Duration}. By (A4), the engine produces only recommendation types present in RS(SAFE). Therefore AI(E) ⊆ {Go, Delay, DepartureTime, Duration} = A_AI(SAFE). ✓

In all three cases, AI(E) ⊆ A_AI(f(E)). The Safety Dominance Property holds. ∎

**Remarks.**

The proof is constructive: it depends only on the definitions of RS(S) (Definition 5.10), the gate function G(S) (Definition 5.7), and the AI output mapping (Definition 5.11) — all of which are fully under the designer's control. No runtime checking or monitoring is required.

The property holds before generation begins. RS(S) is supplied to Layer 3 as a precondition; the engine has no mechanism to generate types outside its active rule set. This is fundamentally different from a post-hoc output filter, which could fail, be bypassed, or have edge cases in which the filter condition evaluates incorrectly. The construction-time enforcement means the Safety Dominance Property is not a test result — it is a structural guarantee.

**Significance.** Theorem 6.3 establishes **effectiveness**: the safety constraints are actually enforced on the AI output. The AI cannot — by construction — produce a recommendation outside the scope defined by the current safety state. No environmental condition can cause the AI to generate DepartureTime or Duration under CAUTION, and no condition can cause any recommendation under UNSAFE. This guarantee holds for all E, not just for tested scenarios. It is the load-bearing safety guarantee of the architecture.

---

### 6.5 Composite Guarantee

The three theorems together characterise the full formal safety behaviour of the architecture.

**Table 5. Formal guarantees of the graduated safety-state-gated architecture.**

| Theorem | Guarantee | Implication |
|---------|-----------|-------------|
| 6.1 (Totality) | f(E) is total on ideal inputs; F_{D,τ} is total after resolution under valid startup configuration | No environmental state can leave the governance layer without a safety classification |
| 6.2 (Monotonicity) | A_AI(S₁) ⊆ A_AI(S₂) whenever S₁ ≻ S₂ | Advisory scope never expands as conditions worsen; CAUTION is provably stricter than SAFE |
| 6.3 (Safety Dominance) | AI(E) ⊆ A_AI(f(E)) for all E | AI output is bounded within the admissible scope at every state, by construction |

These guarantees are complementary. The Safety Dominance case analysis uses totality to establish that a state exists, together with the state-indexed rule-set and gate assumptions. Totality ensures the governance layer always has a state to enforce. Monotonicity ensures that the configured admissible sets contract, never expand, as the classified state worsens. Safety Dominance ensures that the AI advisory engine actually respects that restriction. An architecture satisfying all three has no formally identifiable path by which an AI recommendation can exceed the **configured admissible scope associated with the current governance state**.

**What the composite guarantee does not establish.** The three theorems verify *enforcement* of the configured governance mapping. They say nothing about whether that configuration is the right one. In particular, none of them establishes that `A_AI(CAUTION) = {Go, Delay}` is epistemically warranted, scientifically optimal, or derivable from the environmental evidence: that partition is a conservative architecture policy (Section 5), and deriving admissible sets from stated evidential requirements rather than stipulating them remains outstanding work. Soundness of the *configuration* is a separate question from soundness of the *enforcement*, and only the second is proved here.

Implementation fidelity has been evaluated separately from these theorems (F1–F3, Section 9): the theorems establish what the construction guarantees, while the fidelity evaluation tests whether the built engine honours the assumptions A1–A4 they rest on. The comparative behaviour of the graduated architecture against the ungated and binary-gated conditions is an empirical-trace question, reported in Section 11.

---

## 7. Algorithms

The governance pipeline `obs → S → (G(S), A_AI(S)) → RS(S) → AI(E)` is realised by four algorithms. Each has a bounded contract and each is deliberately scoped to a single responsibility. The detailed specification (full pseudocode, preconditions, postconditions and traceability) is maintained in [`algorithm-specification.md`](../../algorithm-specification.md); this section provides the publication summary reviewers need.

### 7.1 Algorithm 1 — Operational Safety Classification

Realises `S = F_{D,τ}(obs, v) = f(ρ_{D,τ}(obs), v)`. This is the operational classifier — not the ideal shorthand `S = f(E)` — because a deployed system consumes observations, not values. The ten-step ordering below is fixed by Appendix C C.2.0.7.

```text
Algorithm 1: Operational Safety Classification
Input:  obs = (obs_i){i∈C};  v ∈ V ∪ {⊥_cfg};  D ⊆ C (well-formed: t ∉ D, D ⊊ C);
        τ_now ∈ 𝕋;  age = (age_i){i∈C∖D} (symbolic);  date ∈ Date;
        solar : Date → (sunrise, sunset)   ; frozen canonical artefact
Output: S ∈ {SAFE, CAUTION, UNSAFE}  or startup refusal (no S)

 1: if v ∉ V then refuse startup                                       ; C.2.0.6
 2: if t ∈ D or D ⊄ C then refuse startup                              ; C.2.0.5 (D1), (D2)
 3: for i ∈ D:  s_i ← SAFE                                             ; exclusion before fault
 4: for i ∈ (C∖D) ∩ {w, m, o}:  y_i ← fresh_i(val_i(obs_i), τ_now, age_i)
 5: if r ∉ D: y_rate ← fresh_r(val_r(obs_r.rate), τ_now, age_r);
              κ ← χ(obs_r.code)                                        ; χ total; χ(absent)=0
              y_r ← ⊥ if y_rate = ⊥ else (y_rate, κ)
 6: if valid_clock ∧ valid_date ∧ available(solar(date)):
        y_t ← time_of(obs_t);  (sunrise_d, sunset_d) ← solar(date)
    else y_t ← ⊥
 7: s_w ← g_w(y_w);  s_r ← g_r(y_r);  s_m ← g_m(y_m);  s_o ← g_o(y_o, v);  s_t ← g_t(y_t, date)
 8: S ← max-severity(s_w, s_r, s_m, s_o, s_t)                          ; UNSAFE ≻ CAUTION ≻ SAFE
 9: return S
```

**Invariants.** For every well-formed startup, exactly one `S` is returned (Theorem 6.1 / operational totality, Appendix C Theorem C.1b). Any required non-excluded observation resolving to `⊥` yields `gᵢ(⊥) = UNSAFE` and — by max-severity — `S = UNSAFE` (Corollary C.1b.1). Startup failure returns no `S`; the two modes are disjoint. Excluded components contribute `SAFE`; every severity figure produced under `D ≠ ∅` is reported as a lower bound.

### 7.2 Algorithm 2 — Governance Configuration

Realises the finite mapping `S → (G(S), A_AI(S))` from Definitions 5.5 and 5.6. Performs no reasoning, no rule selection and no advisory generation.

```text
Algorithm 2: Governance Configuration
Input:  S ∈ {SAFE, CAUTION, UNSAFE}                    ; valid output of Algorithm 1
Output: (G(S), A_AI(S))
        G(S)    ∈ {0, 1};  A_AI(S) ⊆ R = {Go, Delay, DepartureTime, Duration}

 1: switch S:
 2:     SAFE    → G ← 1;  A_AI ← {Go, Delay, DepartureTime, Duration}
 3:     CAUTION → G ← 1;  A_AI ← {Go, Delay}
 4:     UNSAFE  → G ← 0;  A_AI ← ∅
 5: return (G, A_AI)
```

**Invariants.** The strict containment `A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅` (Theorem 6.2 / Monotonicity) holds by inspection of lines 2–4. `G(S) = 0 ⇒ A_AI(S) = ∅` (Participation Constraint) is discharged by line 4. Algorithm 2 *implements* the finite mapping on which Theorem 6.2 is established; it does not experimentally validate it.

### 7.3 Algorithm 3 — Rule-Set Supply

Supplies the rule set `RS(S)` that Layer 3 is permitted to use for the current decision episode, **before any Layer 3 rule firing begins**. Rule contents remain a Layer 3 build decision (see §9 and OPEN-B1-4); Algorithm 3 defines the shape and admissibility contract only.

```text
Algorithm 3: Rule-Set Supply
Input:  S; G(S); A_AI(S); rule repository; candidate selector
Output: RS(S) with ConclusionTypes(RS(S)) ⊆ A_AI(S) and RS(UNSAFE) = ∅
        or a bounded CONFIGURATION_FIDELITY_FAILURE (no reasoning begins)

 1: if G(S) = 0 then RS ← ∅; return RS                             ; short-circuit; RS(UNSAFE) = ∅
 2: RS_candidate ← candidate(repository, S)
 3: if ∃ρ ∈ RS_candidate : type(ρ) ∉ A_AI(S) then
 4:     refuse supply and return CONFIGURATION_FIDELITY_FAILURE   ; no silent filtering; S unchanged
 5: RS ← RS_candidate;  return RS                                  ; ConclusionTypes(RS) ⊆ A_AI(S)
```

**Invariants.** `ConclusionTypes(RS(S)) ⊆ A_AI(S)` is enforced by *choosing* the rules Layer 3 is permitted to fire (line 5 gates on the compliance check at line 3), not by filtering outputs after generation. When `S` changes across episodes (`S_old → S_new`), Algorithm 3 is re-invoked and the `RS(S_new)` it returns is what the next reasoning episode uses. The concurrency primitive that enforces this consistency at runtime — atomic swap, immutable snapshot, locking, transactional update, serialized execution or equivalent — is not prescribed here (OPEN-B1-8).

### 7.4 Algorithm 4 — Governed Advisory Generation

Invokes Layer 3 only when participation is permitted, using only the active `RS(S)`. `AI(E) ⊆ A_AI(S)` holds by construction from Algorithm 3's postcondition combined with the rule-engine fidelity assumption.

```text
Algorithm 4: Governed Advisory Generation
Input:  E; S; G(S); A_AI(S); RS(S) from Algorithm 3; production rule engine
        (engine fires only rules present in the active RS(S); no active rule
         produces a conclusion type outside its own conclusion — Theorem 6.3 A4)
Output: AI(E) ⊆ A_AI(S)                                            ; holds by construction

 1: if G(S) = 0 then AI ← ∅; return AI                              ; no rule firing, no advisory
 2: AI ← engine.reason(E, RS)                                        ; engine has RS(S) in scope,
                                                                    ; no other rule sets accessible
 3: return AI                                                        ; AI ⊆ A_AI(S) by A3 + engine fidelity
```

**Invariants.** The governed advisory output is constrained to the configured admissible recommendation types for the current safety state, subject to the stated rule-engine fidelity assumptions (Theorem 6.3, Safety Dominance). Algorithm 4 *implements* the enforcement contract on which Theorem 6.3 depends — it does not independently prove Safety Dominance. **Human decision authority is unconditional across all three states**: `AI(E) = ∅` does not forbid human action; `Go ∈ AI(E)` does not automatically approve departure.

### 7.5 Safety-Dominance Dependency

Safety Dominance is delivered by a four-link chain that must be read together:

```
A_AI(S)  →  ConclusionTypes(RS(S)) ⊆ A_AI(S)  →  engine fires only rules in RS(S)  →  AI(E) ⊆ A_AI(S)
   L1                    L2                                 L3                              L4
definition       algorithmic contract              implementation assumption         formal theorem
(Def 5.6)           (Algorithm 3)                   (Theorem 6.3 A4; A4 pre)         (Theorem 6.3)
```

L2 is the algorithmic enforcement contract the implementation makes explicit; L3 is the runtime assumption that the implementation-fidelity evaluation (F1, F2 — see §9 and `evaluation-specification.md` §7) tests, and which it found upheld with zero observed violations.

---

## 8. Complexity Analysis

This section derives **bounded asymptotic complexity** for Algorithms 1–4. It distinguishes three levels that must not be conflated:

- **Fixed current architecture** — the specification with `n = 5` condition components, `|S| = 3` governance states, `|R| = 4` recommendation types as literal constants.
- **Generalized architecture** — the same algorithms parameterised by `n`, `|S|`, `|R|`, `k_S`.
- **Concrete implementation performance** — wall-clock latency, memory footprint, CPU and energy on target hardware.

**This section addresses only the first two.** Asymptotic complexity is not runtime performance; the pattern *"O(1), therefore suitable for low-resource environments"* is not admissible here. Device-level performance evidence is the E5 workstream (§11 / evaluation-specification.md §11), which sets no acceptance threshold in this manuscript (`H3 = X ms` remains OPEN).

**Notation.**

| Symbol | Meaning |
|---|---|
| `n` | number of condition components in `C` (fixed value: 5) |
| `|S|`, `|R|` | governance states (3) and recommendation types (4), both fixed by the current architecture |
| `k_S`, `k` | rules in active `RS(S)`; size of the full rule repository |
| `T_solar_lookup` | cost of one solar-event lookup for a given date; representation-dependent (OPEN-B4-1) |
| `T_select(S)` | cost of `candidate(repository, S)` selection in Algorithm 3; representation-dependent |
| `T_engine(k_S, q, c)` | rule-engine cost per episode; strategy unspecified (OPEN-B3-2) |
| `M_engine` | rule-engine working memory (parameterised) |
| `N` | number of records in a retrospective replay (per-decision vs. replay distinction only) |

### 8.1 Per-algorithm complexity

**Table 3. Per-algorithm complexity for one decision episode.** *Fixed* columns use the current architecture (`n = 5`, `|S| = 3`, `|R| = 4`); *generalized* columns retain the parameters. `T_solar_lookup`, `T_select(S)` and `T_engine(k_S, q, c)` are left symbolic because their representations are deployment / implementation decisions (OPEN-B4-1, OPEN-B3-2).

| Algorithm | Fixed time | Generalized time | Auxiliary space | Primary dependency |
|---|---|---|---|---|
| **A1** — Operational Safety Classification | `O(1) + T_solar_lookup` | `O(n) + T_solar_lookup` | `O(1)` fixed / `O(n)` generalized | Frozen solar artefact representation |
| **A2** — Governance Configuration | `O(1)` | `O(1)` lookup; `O(|S| · |R|)` static mapping storage | `O(1)` | Independent of any dynamic input |
| **A3** — Rule-Set Supply | `T_select(S) + O(k_S)` — the specified pseudocode always scans `RS_candidate` for compliance | `T_select(S) + O(k_S)` | `O(1)` reference *or* `O(k_S)` materialised | Rule-repository representation; `k_S = \|RS_candidate\|` is variable |
| **A4** — Governed Advisory Generation | `O(1) + T_engine(k_S, q, c)` | `O(1) + T_engine(k_S, q, c)` | `O(1) + M_engine` | Rule-engine evaluation strategy |

Notes on individual algorithms:

- **A1.** The five component classifiers are threshold comparisons; the max-severity aggregation is over a fixed-size tuple. Exclusion pin, validation and freshness stages are linear in `|D|` and in `n − |D|`, respectively, and collapse to `O(1)` at `n = 5`.
- **A2.** Static mapping storage `O(|S| · |R|)` is a configuration property, not a per-decision cost — the switch does not scan `|R|` on every decision.
- **A3.** The two conceptual costs must be kept separate. The **currently specified pseudocode** always runs the compliance scan on lines 5–9, so `T_A3_current = T_select(S) + O(k_S)`; under an `O(1)` state-indexed selector this reduces to `O(1) + O(k_S)`, **not** `O(1)`. The fixed architecture constants `n = 5`, `|S| = 3`, `|R| = 4` do not make `k_S` constant. An **implementation variant** that prevalidates the conclusion-type constraint at configuration time and holds `RS(S)` as an immutable reference could remove the runtime scan, reducing `T_A3` to `T_select(S)` alone; that variant is a future optimisation, not the currently specified algorithm.
- **A4.** The governance wrapper (`if G(S) = 0 then return ∅ else invoke engine`) is `O(1)`. **The total is not `O(1)` for the reasoning path.** An illustrative naïve linear scan of `RS(S)` would give `O(k_S · c)`, but that is an example, not the architecture's official complexity. `T_engine(k_S, q, c)` is retained as an explicit dependency and its concrete form is OPEN-B3-2.

### 8.2 End-to-end decision-episode complexity

Summing across A1–A4 for one decision episode:

```
T_episode = O(n) + T_solar_lookup + T_select(S) + O(k_S) + T_engine(k_S, q, c)
```

Under the fixed architecture (`n = 5`, `|S| = 3`, `|R| = 4`):

```
T_episode_fixed = O(1) + T_solar_lookup + T_select(S) + O(k_S) + T_engine(k_S, q, c)
```

**The rule-engine term is retained.** `T_episode` is not `O(1)` merely because the classifier's parameter space is small — Layer 3 reasoning dominates any classification / governance constant.

### 8.3 Per-decision versus replay complexity

Per-decision complexity is independent of replay length. A retrospective replay of `N` records requires `N` decision evaluations:

```
T_replay(N) = O(N · T_episode)
```

For the classification-and-governance-only pipeline (no engine invocation — the configuration in which the participation gate is closed, or in which Layer 2 is evaluated in isolation):

```
T_replay_no_engine(N) = O(N · (n + T_solar_lookup))
```

**The historical replay over 43,848 hourly records is not `O(1)`.** It scales linearly in `N`, excluding external data-loading cost, and it does not enter Algorithm 1's single-decision complexity.

### 8.4 What the complexity results establish, and what they do not

The results above support these bounded statements: the classifier and governance mappings operate over small fixed state spaces; per-decision cost does not grow with the number of replay records `N`; and the rule-engine cost is retained as a parameter rather than collapsed to a fixed complexity.

They do **not** support the following without independent E5 evidence: that the architecture is lightweight, efficient on low-end phones, or deployable in low-resource settings; that latency is negligible; that memory or energy use is minimal. Any such statement requires the empirical performance measurement scheduled for §11 (E5), for which no acceptance threshold has been set (`H3 = X ms` remains OPEN).

**Implementation-fidelity is a separate workstream.** Complexity analysis does not test whether a built Layer 3 prototype honours the engine-fidelity assumption. The fidelity criteria F1–F3 in `evaluation-specification.md` §7 remain future implementation-fidelity evidence.

---

## 9. Prototype Implementation

Sections 5–8 specify the architecture and establish its formal properties. This section describes the executable prototype built from that specification, and reports the implementation-fidelity evaluation carried out against it. The distinction between the two is load-bearing and is maintained throughout: Theorems 6.1–6.3 establish that the *specification* has the stated properties; the fidelity evaluation establishes that the *implementation* conforms to the specification it was built from. Neither result substitutes for the other, and neither is evidence about physical safety, operator behaviour or real-world outcomes.

**The prototype is a research prototype, not a deployed system.** It has not been installed on any operator's device, has not been used by any fisher to make a departure decision, and has produced no advisory that any person has acted on. No field trial, pilot deployment or user study underlies any statement in this manuscript.

### 9.1 Implementation scope and layer boundaries

The prototype implements Layer 2 governance and the Layer 3 reasoning engine. Layer 1 (observation and resolution) is supplied by the retrospective data pipeline, and Layer 4 is the human decision, which no software component in this work represents, records or constrains.

```
observations
→ ρ_{D,τ}              resolution map                     [data pipeline]
→ F_{D,τ} = f ∘ ρ_{D,τ}  classification → S               [Layer 2]
→ G(S), A_AI(S)        governance configuration           [Layer 2]
→ RS(S)                rule-set selection and supply      [Layer 2 → Layer 3, Algorithm 3]
→ AI(E)                governed advisory generation       [Layer 3, Algorithm 4]
→ Human Decision                                          [Layer 4 — not implemented]
```

The implementation is a Python package (`governance/`) comprising a rule representation, an advisory representation, a state-indexed rule repository, a rule-set provider implementing Algorithm 3, a linear-scan reasoning engine implementing Algorithm 4, a reasoning-episode driver, and a fidelity-trace emitter. The component classifiers `g_w`, `g_r`, `g_o` and `g_t` are the canonical implementations used for all empirical work in this paper; the prototype calls them rather than reimplementing them, so no second classifier exists anywhere in the system.

**Offline-first operation.** The classifier depends on no network service at decision time. The solar-event boundaries required by `g_t` are read from a frozen daily artefact rather than computed astronomically or fetched remotely, so classification is a table lookup plus four threshold comparisons. This is a structural property of the design. It is **not** a claim about device-level latency, memory or energy cost, which require the performance evidence discussed in §11.7 and remain open.

### 9.2 The Layer 2 → Layer 3 interface

Layer 3 does not recompute Layer 2. The two layers communicate through `ComponentStateTrace`, a read-only object that Layer 2 produces from the same resolved component results that determined `S`, and that Layer 3 consumes without modification. Rule predicates may inspect an already-computed component classification (`component_o_state == "CAUTION"`); they may not re-derive it from raw values (`resolved_wave_height >= 1.0`). Reproducing a threshold comparison inside Layer 3 would duplicate the classifier and create a second, unverified path to a safety state, and the implementation prohibits it.

Three interface semantics are preserved exactly and are easily conflated:

- **`UNSAFE` is unreachable at the Layer 3 interface.** If any component classifier returns UNSAFE then `S = UNSAFE`, `G(UNSAFE) = 0`, and Layer 3 is never invoked. The component classifiers can and do return UNSAFE; Layer 3 simply never observes it. This is an execution-boundary consequence, not a restriction on the codomain of any `g_i`.
- **`EXCLUDED` is not observed `SAFE`.** A component in the declared exclusion set `D` is pinned SAFE for aggregation (Definition 5.5 and Appendix C C.2.0.5), but the interface exposes its true status as `EXCLUDED`. The retrospective configuration declares `D = {m}`, so `component_m_state = EXCLUDED` throughout — which asserts that the marine-warning component was not measured, not that no marine hazard was present.
- **Episode consistency.** `S` and `ComponentStateTrace` must originate in the same Layer 2 evaluation; the episode identifier enforces the correspondence. A trace from one episode may never govern reasoning for another.

`ComponentStateTrace` does not modify `G(S)`, `A_AI(S)` or `RS(S)`, and Safety Dominance is unaffected by it: the proof of Theorem 6.3 depends only on the value of `S`.

### 9.3 Rule sets and their bounded content

`RS(UNSAFE) = ∅` is the *absence* of a rule set rather than an empty collection: the UNSAFE path never calls selection or validation, and the episode returns an empty advisory list directly.

`RS(SAFE)` and `RS(CAUTION)` are state-indexed subsets of a rule repository. Algorithm 3 selects the candidate set for the governing state and validates `ConclusionTypes(RS) ⊆ A_AI(S)` before supply; reasoning begins only after validation succeeds.

The rule content implemented in the prototype is deliberately narrow, because rule content is a scientific question rather than an engineering one. A recommendation type being *permitted* by `A_AI(S)` does not make a rule producing it *warranted*: permission is a governance-layer constraint, warrant is an evidential one. Candidate rules were assessed against a five-level evidence hierarchy, and only those with a defensible antecedent were implemented.

**Table 4. Implemented and deferred Layer 3 rules.** Evidence level A denotes direct normative or operational authority; level C denotes domain evidence requiring bounded geographic or vessel-type adaptation to the study site. No level B evidence — direct empirical evidence from small-scale fisheries at the study site or a closely matched context — was identified for this deployment site.

| Rule | State | Antecedent | Conclusion | Evidence level | Implementation status |
|---|---|---|---|---|---|
| R-CAUTION-001 | CAUTION | marine warning at advisory level | Delay | A (environmental premise); C (advisory premise, inferred) | IMPLEMENTED |
| R-CAUTION-002 | CAUTION | `g_o(o, v) = CAUTION` | Delay | C | IMPLEMENTED |
| R-CAUTION-003 | CAUTION | `g_r(r, κ) = CAUTION` | Delay | C | IMPLEMENTED |
| R-CAUTION-004 | CAUTION | `g_w(w) = CAUTION` | Delay | C | IMPLEMENTED |
| R-SAFE-001 | SAFE | all components in their SAFE band | Go | C | **DEFERRED** |

**`RS(SAFE)` is empty in the current prototype.** R-SAFE-001 was assessed as conditionally supported but was deferred because its antecedent is functionally a restatement of `S = SAFE`, and resolving whether a state-restatement rule is scientifically warranted requires a bounded decision that has not been taken. Two consequences follow and are carried through §11 and §14:

1. **The only advisory conclusion type the prototype generates is `Delay`.** `Go`, `DepartureTime` and `Duration` remain admissible under `A_AI(SAFE)` and — for `Go` — under `A_AI(CAUTION)`, but no implemented rule produces them. `DepartureTime` and `Duration` have no repository authority for their payload content at all and are registered as open evidential gaps.
2. **The fidelity evaluation therefore exercises a populated CAUTION rule set and the UNSAFE gate-off path, but not a populated SAFE rule set.** It does not demonstrate that the full admissible space `A_AI(SAFE) = {Go, Delay, DepartureTime, Duration}` is correctly enforced against rules that attempt to fill it, because no such rules exist to be enforced against.

A `Delay` advisory is not a prohibition and a `Go` advisory would not be an approval. Neither the advisory object nor any other output carries a field for approval, prohibition, override or automated decision, and an empty advisory list says nothing about whether departure is safe or permitted.

### 9.4 Predicate semantics and bounded refusal

Rule predicates evaluate over a three-valued domain `{TRUE, FALSE, ERROR}`. A rule fires if and only if every predicate evaluates `TRUE`; `ERROR` is never reinterpreted as `FALSE`. If any predicate returns `ERROR` during an episode, the engine produces `AI(E) = ∅` and records the failure in the trace, while `S`, `G(S)` and `A_AI(S)` remain exactly as Layer 2 determined them.

This is a bounded advisory refusal, and it is distinct from three things it superficially resembles. It is not `S = UNSAFE`: Layer 3 never mutates the safety state. It is not a configuration failure: malformed rule definitions — unknown variables, type mismatches, invalid operators — are caught by Algorithm 3's validation *before* reasoning begins and raise a configuration error that disables Layer 3 for the episode without producing an advisory. And it is not a Layer 2 input fault, which resolves through the fail-safe semantics `g_i(⊥) = UNSAFE` upstream and never reaches Layer 3 at all. The trace distinguishes a normal no-fire episode from an aborted one without requiring any other field to be inspected.

An unconfigured vessel category is a startup precondition failure, consistent with Appendix C C.2.0.6: the episode refuses to begin rather than producing a classification.

### 9.5 Implementation-fidelity evaluation (F1–F3)

The three fidelity criteria test whether the implementation conforms to the specification. They do not re-derive Safety Dominance, and they are not behavioural hypotheses.

- **F1** — no generated advisory conclusion type lies outside `A_AI(S)`.
- **F2** — the count of `AI(E) ⊄ A_AI(S)` violations is exactly zero.
- **F3** — `RS_selected(e) = RS(S_e)` for every episode; no stale rule set persists across a transition.

**Evaluation scope: interface-contract exhaustive.** The evaluation enumerates the Layer 3 interface state space — every combination of global state and component-state values admitted by the interface type domains, filtered by the reachability rules that relate component states to `S` — and executes one reasoning episode per reachable consistent case. It is a deterministic census of that state space. No random sampling was used, no inferential statistic was computed, and **the fidelity evaluation is not the retrospective replay**: it runs over constructed interface-contract episodes, not over historical hours. This is what allows R-CAUTION-001 to be exercised at all, since the marine-warning component is excluded from the historical replay and the rule could not otherwise be tested.

The scope is exhaustive **over the interface contract**. It is not historically exhaustive, not environmentally exhaustive, not exhaustive over deployment conditions, and not exhaustive over the situations a fisher may encounter at sea.

**Table 5. Implementation-fidelity results.** Deterministic census over the interface-contract state space. All three criteria PASS.

| Criterion | Scope evaluated | Observed | Criterion | Result |
|---|---|---|---|---|
| **F1** | 292 primary episodes; 454 advisory records | 0 conclusion types outside `A_AI(S)` | violations = 0 | **PASS** |
| **F2** | 292 primary episodes; 244 episodes with a non-empty advisory; 454 advisory records | 0 occurrences of `AI(E) ⊄ A_AI(S)` | violation count = 0 | **PASS** |
| **F3** | 292 primary episodes; 292 rule sets examined (32 SAFE, 260 CAUTION) | 0 rule-set/state mismatches | mismatches = 0 | **PASS** |

A further 162 cases exercise the `G(S) = 0` gate-off path, in which Layer 3 is not invoked. These are reported separately and are **not** part of the 292 primary episodes; the two counts must not be summed or conflated.

**Episode composition.** Of the 292 primary episodes, 260 were CAUTION and 32 were SAFE. Of the 260 CAUTION episodes, 244 generated at least one advisory and 16 generated `AI(E) = ∅` because no implemented rule predicate evaluated `TRUE`. This is not a fidelity failure: `A_AI(S)` defines what is admissible, not a requirement that an advisory must exist. **All 32 SAFE episodes generated zero advisories**, for the reason given in §9.3 — `RS(SAFE)` is empty.

One quantity in the underlying evidence invites a specific misreading and is stated explicitly here: the figure of **244 conclusion-type evaluations is not a count of 244 distinct advisory conclusion types.** It is the number of episodes in which a non-empty conclusion-type set was evaluated. The prototype generates exactly one conclusion type, `Delay`.

**Table 6. Layer 3 rule activation over the 260 CAUTION episodes.**

| Rule | Times selected | Predicate TRUE | Predicate ERROR | Times fired | Advisories generated |
|---|---|---|---|---|---|
| R-CAUTION-001 | 260 | 130 | 0 | 130 | 130 |
| R-CAUTION-002 | 260 | 108 | 0 | 108 | 108 |
| R-CAUTION-003 | 260 | 108 | 0 | 108 | 108 |
| R-CAUTION-004 | 260 | 108 | 0 | 108 | 108 |
| R-SAFE-001 | 0 | 0 | 0 | 0 | 0 |
| **Total** | | | **0** | | **454** |

Activation counts characterise which predicates were satisfied across the enumerated state space. They are not evidence of behavioural effectiveness, of how often the corresponding conditions occur in the field, or of whether a `Delay` advisory would be useful, heeded or correct. No predicate evaluation error occurred, so the refusal path of §9.4 was not exercised by a runtime failure in this evaluation.

### 9.6 Hysteresis smoothing

The prototype retains dual-threshold hysteresis at classification boundaries. It is presented here as a **retained low-cost precaution, not as a mitigation for an observed instability**, because the instability it would mitigate was measured and found to be small.

Under the canonical PRIMARY configuration over five years of site data, the classifier produces 26 genuine oscillation events — approximately 5.2 per year — and hysteresis reduces non-scheduled transitions by 10.36%. The full temporal-dynamics characterisation is reported in §11.5. **These figures bound the phenomenon at hourly resolution only**; sub-hourly oscillation is invisible in hourly data and is neither measured nor excluded by this result. Because the measured effect is near-null at the resolution available, hysteresis is justified by its negligible cost rather than by a demonstrated need.

### 9.7 Deployment context

The architecture is instantiated for small-scale coastal fisheries at Kota Kinabalu, Sabah, Malaysia. The vessel-conditioned ocean-state thresholds, the rainfall and wind boundaries, the solar-event artefact and the evidential basis of the Layer 3 rules are all specific to that setting. The instantiation motivates and constrains the architecture; it is not itself the contribution, and no claim in this manuscript asserts that these particular thresholds or rules transfer to another site or fleet.

The prototype targets a low-resource deployment context, which is why offline operation and a small fixed classification state space are design priorities. Whether the implementation actually meets the resource constraints of representative target hardware is an empirical question that §11.7 addresses and does not close.

---

## 10. Experimental Design

The evaluation is organised around a principle that governs everything reported in §§11–12: **different claims about this architecture require different kinds of evidence, and the kinds must not be substituted for one another.** A theorem is not a hypothesis. An invariant is not a behavioural outcome. A deterministic census value is not a population estimate. Implementation fidelity is evidence that code matches a specification; it is not evidence that the specification is correct. Collapsing these under a single heading of "experimental validation" would make the evaluation look broader than it is, and would let a proof stand in for a measurement or a measurement stand in for a proof.

The design therefore carries four evidence classes, each with its own instrument and its own reporting boundary.

**Table 7. Evaluation matrix.** Each claim carries exactly one evidence class. Status is as at submission.

| ID | Claim | Evidence class | Instrument | Status |
|---|---|---|---|---|
| **P1** | Totality of `f` (and of `F_{D,τ}` under valid startup) | FORMAL | Proof — Theorem 6.1 | CLOSED |
| **P2** | Monotonicity of `A_AI` with strict containment | FORMAL | Proof — Theorem 6.2 | CLOSED |
| **P3** | Safety Dominance, `AI(E) ⊆ A_AI(f(E))` | FORMAL | Proof by construction — Theorem 6.3, assumptions A1–A4 | CLOSED |
| **P4** | `C1 ≡ C3` at the admissible-set level (Proposition J1-P1) | FORMAL (structural) | Finite-mapping comparison | CLOSED |
| **F1** | No conclusion type outside `A_AI(S)` | IMPLEMENTATION_FIDELITY | Interface-contract exhaustive census | CLOSED — PASS |
| **F2** | Zero `AI(E) ⊄ A_AI(S)` violations | IMPLEMENTATION_FIDELITY | Interface-contract exhaustive census | CLOSED — PASS |
| **F3** | `RS_selected(e) = RS(S_e)` at every episode | IMPLEMENTATION_FIDELITY | Interface-contract exhaustive census | CLOSED — PASS |
| **E1** | Pairwise admissible-set divergence across C0, C1, C2 | EMPIRICAL_TRACE | Retrospective replay census | CLOSED |
| **E2** | Isolated Level 2 contribution `Δ_L2` | EMPIRICAL_TRACE | Retrospective replay census | CLOSED |
| **E3** | Resolution sensitivity across configurations | EMPIRICAL_TRACE (sensitivity) | PRIMARY/RESOLUTION comparison over `{E1, E2, E6}` | CLOSED |
| **E4** | Transition and hysteresis characterisation | EMPIRICAL_TRACE | Retrospective replay, PRIMARY chronology | CLOSED (PRIMARY only) |
| **E6** | `C1 ↔ C3` divergence | EMPIRICAL_TRACE (consistency confirmation) | Retrospective replay census | CLOSED |
| **E5** | Governance latency and computational overhead on target hardware | PERFORMANCE | Benchmark harness | **OPEN** |

Four research questions carry the evaluation, and each is answered by exactly one evidence class. **RQ-J1** asks whether Safety Dominance can be proved formally and under what assumptions — answered by P1–P3. **RQ-J2** asks what runtime latency and computational overhead Layer 2 introduces on the target deployment hardware — answered by E5, which is open. **RQ-J3** asks how the admissible-recommendation-set outputs of C2 differ from C1 and C0 on the retrospective replay, and what share of the divergence is attributable to Level 2 alone — answered by E1, E2 and E3. **RQ-J4** asks which component of the governance pair accounts for the observed C2 versus C1 divergence — answered by E2, with E4 in support.

Two constructs that a reader might expect are deliberately absent. **Decision-support utility** has no operational definition over replay data alone — ground-truth recommendation correctness, fisher preference, decision quality and real-world outcome each require a different data source — and no formula is invented to close it. **Trust, calibrated reliance and real-world safety outcomes** require field data this study does not have. Both are deferred to a future user study and are outside the evidence base of this manuscript entirely.

### 10.1 Experimental conditions

The primary experiment compares three conditions over the same environmental record.

| Condition | Label | `A_AI(SAFE)` | `A_AI(CAUTION)` | `A_AI(UNSAFE)` | Governance active |
|---|---|---|---|---|---|
| **C0** | Ungated | FULL | FULL | FULL | None |
| **C1** | Binary-gated | FULL | FULL | ∅ | Level 1 only (participation gate `G`) |
| **C2** | Proposed graduated architecture | FULL | {Go, Delay} | ∅ | Level 1 + Level 2 (`G` and `A_AI`) |

where `FULL = {Go, Delay, DepartureTime, Duration}`. **C1 and C2 differ in exactly one cell** — `A_AI(CAUTION)` — and that cell is the architectural contribution. Any divergence between them is therefore attributable to advisory-scope restriction and to nothing else, which is what makes the comparison informative rather than merely descriptive.

A fourth mapping, **C3**, instantiates the traffic-light governance topology of the closest structural precedent in the reviewed literature: three levels, with AI withdrawn only at the most severe.

| Condition | Label | `A_AI(SAFE)` | `A_AI(CAUTION)` | `A_AI(UNSAFE)` |
|---|---|---|---|---|
| **C3** | Traffic-light topology (structural comparator) | FULL | FULL | ∅ |

**C3 is not a fourth experimental arm and is not reported as one.** It is a structural comparator that exists to address the novelty question directly: if a three-level governance topology already produces what this architecture produces, the contribution is not what it claims to be. Comparing the mapping literals answers that question analytically, and the replay confirms the harness computed what the mappings say.

**Fairness qualification.** The precedent architecture conditions its traffic-light index on AI degradation — drift, outliers, performance decay — and not on environmental state. C3 ports its *governance topology* onto the shared state axis so that admissible-output structure can be compared. It is not a reproduction of that system, it was not run as that system, and no result here indicates that the precedent framework is deficient: it answers a different question and is appropriate for it. The modelling premise `A_C3(CAUTION) = FULL` is a reading of that topology — the intermediate level alters supervisory intensity rather than AI advisory scope — and it is the premise a reviewer can legitimately dispute. Everything C3 contributes follows from it.

*Condition labels were normalised before any result reported in this manuscript was produced.* An earlier journal-local scheme used `C1/C2/C3 = Ungated/Binary/Proposed`, inverting `C2` relative to the canonical harness. No result requires label translation.

### 10.2 Retrospective replay protocol

The empirical-trace evidence comes from replaying the governance pipeline over hourly environmental records for the study site, classifying each hour under each condition and comparing the resulting admissible sets.

Results are reported in two configurations, which differ in wave-model resolution and in record length:

| Configuration | Period | Records | Wave source | Role |
|---|---|---|---|---|
| **PRIMARY** | 2020-01 → 2024-12 (5.00 yr) | 43,848 hourly | ERA5-Ocean, ~50 km | Headline configuration |
| **RESOLUTION** | 2021-10 → 2024-12 (3.25 yr) | 28,501 hourly | MFWAM, ~8 km | Resolution-sensitivity check |

Divergence metrics are reported over the **departure window 05:00–09:00**, the hours in which the departure decision is actually taken: 9,135 hours under PRIMARY and 5,935 under RESOLUTION. All-hours figures are reported alongside them in §11.3 to show that the window is not doing the work.

**Neither configuration is "the right one."** Reporting both is the point: the gap between them is the grid-resolution sensitivity of the result, made visible rather than hidden behind a single number. PRIMARY is the headline because it covers the full five-year record; RESOLUTION is the check because an 8 km wave model resolves nearshore island sheltering that a 50 km cell averages away.

The replay declares the exclusion set `D = {m}`. No marine-warning archive exists for the study site, so the marine-warning component is excluded and pinned SAFE for aggregation rather than treated as faulted — applying `⊥` semantics to an unmeasured variable would classify every hour UNSAFE and destroy the analysis. **Every severity figure in §11 is therefore a lower bound:** a live required marine-warning feed could only raise binding rates, never lower them.

### 10.3 Implementation-fidelity protocol

The fidelity evaluation is a separate instrument over a separate state space and is described in §9.5. It enumerates the Layer 3 interface contract exhaustively rather than sampling from it, and it is not the retrospective replay. Its scope is exhaustive over that interface contract and over nothing else.

### 10.4 Performance protocol and its current status

E5 measures the wall-clock latency of a full governance pass — classification through gate, admissible-set selection, rule-set supply and reasoning — together with its memory and CPU cost, on representative target deployment hardware.

The benchmark protocol is defined and the harness is implemented and validated. Three workloads exercise the three execution paths: `W-SAFE` (`G = 1`, full admissible set, no rule fires), `W-CAUTION` (`G = 1`, restricted admissible set, rules fire) and `W-UNSAFE` (`G = 0`, gate-off, no reasoning). Each is executed for 500 measured repetitions after 50 warm-up iterations, with per-iteration timing taken inside the measured loop and resource probes taken as bookends around it.

**E5 is nevertheless OPEN, and this is the most important boundary in the evaluation.** What has been completed is harness validation and a reference run on the development machine. What has not been completed is measurement on representative target hardware, which requires a physical device that was not available. §11.7 reports the development-machine reference and states plainly what it is not.

**No acceptance threshold exists.** The performance criterion `H3 = X ms` remains open and unsupported: no external standard, prior study or operational requirement supplies a justified latency bound for this application, and none is invented here. A latency measurement without a threshold is a description, not a pass or a failure, and §11.7 reports it as such.

### 10.5 Statistical treatment

The retrospective replay is a **deterministic census of all hourly records in the predefined retrospective study window**, not a random sample from a broader climatological population. The classifier is deterministic; there is no sampling and no stochastic component. Divergence percentages, binding rates, component shares, transition counts and `Δ_L2` are therefore reported as **exact descriptive values for the analysed trace and configuration**, and no p-value, confidence interval or significance test is applied to any of them. Doing so would impute sampling variability to an enumeration that has none.

These values are exact for the record analysed. They are **not** estimates of future operating conditions at the study site or anywhere else.

**The PRIMARY/RESOLUTION spread is a resolution-sensitivity result, not an error bar.** The two configurations are different measurements, not two draws from one distribution, and the notation `5.81 ± something` would be incorrect. Dual-configuration reporting is mandatory for quantities whose evaluation design supports a like-for-like comparison — `{E1, E2, E6}` — and §11.4 reports that comparison. It does not extend to E4, for reasons given in §11.5.

The fidelity evaluation is likewise a deterministic census over a constructed state space and carries no inferential statistics.

Governance latency is the one quantity in the design that admits distributional treatment, because timing carries genuine variance from the runtime environment. It is reported with mean, median, tail percentiles and standard deviation in §11.7 — bounded, as that subsection makes explicit, to the machine on which it was measured.

---

## 11. Results

Every empirical value in this section is an **exact descriptive value for the analysed trace and configuration**, produced by a deterministic census as described in §10.5. None is an estimate, and none carries sampling uncertainty. Percentages are reported to two decimal places where the underlying enumeration supports it. Because the replay declares `D = {m}`, every severity figure is a lower bound.

Results are reported in the order of the evidence classes in Table 7, so that formal, fidelity, empirical-trace and performance evidence remain separable at a glance.

### 11.1 Formal results

P1–P4 are established by proof, not by measurement, and are stated here only for completeness; the proofs are in §6 and the structural proposition in §10.1.

| ID | Result | Basis |
|---|---|---|
| **P1** | `f` is total: every environmental state maps to exactly one element of `{SAFE, CAUTION, UNSAFE}`, and `F_{D,τ}` is total under valid startup configuration | Theorem 6.1 |
| **P2** | `A_AI` is monotone under the severity order, with strict containment `A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅` | Theorem 6.2 |
| **P3** | `AI(E) ⊆ A_AI(f(E))` for all `E`, and `f(E) = UNSAFE ⇒ AI(E) = ∅`, under assumptions A1–A4 | Theorem 6.3 |
| **P4** | `A_C1(S) = A_C3(S)` at every `S`: the binary participation gate and the traffic-light topology are output-equivalent at the admissible-set level | Finite-mapping comparison |

No empirical result in §§11.2–11.7 proves any of these, and none of them establishes that the configured mappings are the *right* mappings. P2 shows that advisory scope never expands as conditions worsen; it does not show that `{Go, Delay}` is the correct restriction for CAUTION. P3 shows that the AI cannot exceed the configured admissible scope; it does not show that operating within that scope is physically safe.

### 11.2 Implementation-fidelity results

F1, F2 and F3 are CLOSED and all three PASS: zero conclusion types outside `A_AI(S)`, zero Safety-Dominance violations, and zero rule-set/state mismatches across 292 primary episodes and 454 advisory records.

These are reported in full in §9.5, alongside the implementation they characterise, rather than here. The separation is deliberate: implementation fidelity is evidence that code matches a specification, and folding it into a results section organised around empirical-trace measurements would present two different kinds of claim as one. §9.5 also carries the three bounds that travel with these results — the interface-contract scope, the 244-count semantics, and the empty `RS(SAFE)`.

### 11.3 Governance divergence (E1)

Each hour of the record is classified once and the resulting admissible recommendation set is compared pairwise across conditions. Divergence is the share of hours on which two conditions permit different admissible sets.

**Table 8. Pairwise admissible-set divergence, departure window 05:00–09:00.** PRIMARY `n = 9,135` hours; RESOLUTION `n = 5,935` hours.

| Pair | What it isolates | PRIMARY | RESOLUTION |
|---|---|---|---|
| C0 ↔ C1 | Participation gate alone (Level 1) | 42.88% | 41.08% |
| C0 ↔ C2 | Levels 1 and 2 combined | 48.69% | 45.56% |
| C1 ↔ C2 | Advisory-scope restriction alone (Level 2) | 5.81% | 4.48% |
| C1 ↔ C3 | Traffic-light topology against binary gate | 0.00% | 0.00% |

**Table 9. Pairwise admissible-set divergence, all hours.** PRIMARY `n = 43,848`; RESOLUTION `n = 28,501`.

| Pair | PRIMARY | RESOLUTION |
|---|---|---|
| C0 ↔ C1 | 53.27% | 52.11% |
| C0 ↔ C2 | 58.03% | 56.00% |
| C1 ↔ C2 | 4.77% | 3.89% |
| C1 ↔ C3 | 0.00% | 0.00% |

The underlying state distributions are given below, because the divergence figures are not interpretable without them.

| Configuration and window | SAFE | CAUTION | UNSAFE |
|---|---|---|---|
| PRIMARY, all hours | 18,401 (42.0%) | 2,091 (4.8%) | 23,356 (53.3%) |
| PRIMARY, departure window | 4,687 (51.3%) | 531 (5.8%) | 3,917 (42.9%) |
| RESOLUTION, all hours | 12,540 (44.0%) | 1,110 (3.9%) | 14,851 (52.1%) |
| RESOLUTION, departure window | 3,231 (54.4%) | 266 (4.5%) | 2,438 (41.1%) |

Two structural checks follow directly and both hold exactly. C1 and C2 agree at SAFE (both full) and at UNSAFE (both empty), so they can differ only at CAUTION, and their divergence must equal the CAUTION rate: 531 / 9,135 = 5.8128% against a measured 5.81%, and 266 / 5,935 = 4.4819% against a measured 4.48%. C0 differs from C1 only where the gate closes, so C0 ↔ C1 must equal the UNSAFE rate: 3,917 / 9,135 = 42.88% and 2,438 / 5,935 = 41.08%. The harness reproduces both identities, which is a consistency check on the implementation rather than an independent finding.

**What these figures are.** They are counts of hours on which the admissible recommendation *set* differs. They are not counts of hours on which a recommendation was actually produced, on which a fisher was affected, or on which a decision changed. C0 is a hypothetical ungoverned configuration that was never deployed and never advised anyone.

### 11.4 Isolated Level 2 contribution and resolution sensitivity (E2, E3)

C0 and C1 differ only in Level 1; C0 and C2 differ in Levels 1 and 2 combined. Subtracting removes the Level 1 term and isolates the contribution of advisory-scope restriction:

```
Δ_L2 = div(C0, C2) − div(C0, C1)
```

**Table 10. Isolated Level 2 contribution (E2), departure window.**

| Configuration | div(C0,C1) | div(C0,C2) | **Δ_L2** |
|---|---|---|---|
| PRIMARY (5.00 yr, ERA5-Ocean ~50 km) | 42.88% | 48.69% | **5.81%** |
| RESOLUTION (3.25 yr, MFWAM ~8 km) | 41.08% | 45.56% | **4.48%** |

`Δ_L2` is the load-bearing empirical result of this manuscript. It quantifies **the additional advisory-scope governance the graduated architecture introduces relative to binary participation-only governance**, measured as the share of departure-window hours on which the two permit different admissible sets. In those hours the binary baseline leaves the full recommendation set available while the proposed architecture withholds the tactical types.

It is not a safety improvement, a risk reduction, an accident-prevention rate or an accuracy gain, and it should not be read as "5.81% safer". It measures a difference in governance behaviour. Whether restricting advisory scope in those hours produces any benefit to a fisher is a question this study does not address and has no evidence bearing on.

**Resolution sensitivity (E3).** The mandatory dual-configuration scope covers E1, E2 and E6, and Tables 8–10 report both configurations for all three. The 1.3-percentage-point gap between PRIMARY and RESOLUTION on `Δ_L2` **is** the resolution-sensitivity result: a finer wave model resolves nearshore island sheltering that a 50 km cell averages away, and the measured Level 2 contribution falls accordingly. Both numbers are reported because neither alone is the result, and the gap quantifies grid-resolution dependence rather than concealing it. The two configurations are different measurements, not two draws from one distribution; the spread is not an interval estimate.

### 11.5 Temporal dynamics and hysteresis (E4)

The classifier was replayed over the PRIMARY record and state transitions counted. *Scheduled* transitions are those in which `g_t` changed across the hourly boundary — sunrise and sunset — and are deterministic daily events rather than instability. *Non-scheduled* transitions are all others. A genuine oscillation is an A→B→A round trip within a three-hour window, excluding scheduled transitions.

**Table 11. Transition and hysteresis characterisation, PRIMARY configuration, small vessel, all hours over 1,827 days.**

| Quantity | Without hysteresis | With hysteresis |
|---|---|---|
| Total state transitions | 3,661 | 3,575 |
| Scheduled (`g_t` changed) | 3,439 (93.9%) | 3,376 |
| Non-scheduled | 222 | 199 |
| Genuine oscillations (A→B→A within 3 h) | 26 (5.2/yr) | 20 (4.0/yr) |
| Reduction in non-scheduled transitions | — | **10.36%** |

The great majority of transitions — 93.9% — are the daily sunrise and sunset boundary crossings. Genuine oscillation is rare: 26 events across five years. **This is a near-null result, and it qualifies rather than supports the mode-chattering concern** that motivated including hysteresis. Hysteresis is retained as a low-cost precaution, not as a mitigation for a demonstrated instability (§9.6).

**The result is bounded at hourly resolution.** Sub-hourly oscillation is invisible in hourly data. The finding bounds chattering at the resolution measured and says nothing about finer time scales.

**Provenance of the transition count.** The figure 3,661 supersedes three earlier counts, and the chain matters because the differences are not all attributable to the same cause:

```
5,416  →  5,220  →  5,201  →  3,661
        threshold    data      g_t
```

5,416 was measured under superseded rainfall and wave thresholds; amending those thresholds gives 5,220 on the same data; correcting the weather grid cell gives 5,201; and adopting the solar-event time classifier gives the canonical 3,661. **The drop from 5,416 to 3,661 must not be attributed to the time classifier alone** — two prior corrections account for part of it.

**E4 is a PRIMARY-only characterisation.** No RESOLUTION analogue is reported, and none exists. This is a scoped exclusion rather than a gap: a valid cross-configuration comparison of transition, oscillation and hysteresis counts would require an explicitly comparable temporal design, and raw event counts drawn from windows of different length and coverage are not comparable merely because both configurations carry a name. Accordingly, this manuscript does **not** claim that E4 is insensitive to resolution, that it would reproduce under the finer wave model, or that a RESOLUTION result would equal the PRIMARY one. None of these has been tested. Any future E4 sensitivity evaluation would need to control for common temporal coverage, comparable input availability and normalised rates under equivalent hysteresis parameters.

### 11.6 Structural comparator confirmation (E6)

The traffic-light topology C3 and the binary gate C1 diverge on **0.00% of hours** — in both configurations, over both the full record and the departure window, with no exceptions.

This is **confirmation of an equivalence already established structurally**, not an empirical discovery. P4 proves `A_C1(S) = A_C3(S)` from the mapping literals in one line; the two conditions are literally identical mappings in the comparison harness; and the replay confirms that the harness computed what the mappings say. The 0.00% is a harness-consistency check, and it could not have come out otherwise without indicating an implementation error.

Its significance is nonetheless direct. At the admissible-recommendation-set level, the closest structural precedent in the reviewed literature produces what a plain binary gate produces, in every hour of the record: **its intermediate level is not observable in AI output at all.** Under the same comparison, C2 diverges from both C1 and C3 on 5.81% of PRIMARY departure-window hours. That gap is the architectural contribution, and it is bounded by the modelling premise stated in §10.1 — a reader who rejects the reading `A_C3(CAUTION) = FULL` rejects this result with it.

The comparison does not establish that the precedent framework is deficient, that it was reproduced, or that its intermediate level is useless for the purpose it was designed to serve. It establishes that a governance topology conditioned on AI degradation does not, when ported onto the environmental-state axis, restrict advisory scope.

### 11.7 Performance status and development-machine reference (E5)

**E5 is OPEN.** Target-hardware performance for the intended low-resource deployment context has not been measured, and no result in this manuscript establishes it.

What has been completed is the benchmark harness and a reference run on the development machine, undertaken to validate the measurement methodology. Those measurements are reported below as **development-machine reference measurements** and as nothing else.

**Table 12. Development-machine reference benchmark.** MacBook Pro, Apple M3 Pro, arm64, 36 GB RAM, macOS 26.2, Python 3.9.6, AC power. 500 measured repetitions per workload after 50 warm-up iterations; per-iteration timing inside the measured loop. **Reference only — not target-hardware evidence.**

| Workload | Mean (ms) | Median (ms) | p95 (ms) | p99 (ms) | Std. dev. (ms) |
|---|---|---|---|---|---|
| W-SAFE (`G = 1`, full scope, no rule fires) | 0.2066 | 0.2031 | 0.2342 | 0.2537 | 0.0172 |
| W-CAUTION (`G = 1`, restricted scope, rules fire) | 0.2117 | 0.2126 | 0.2243 | 0.2592 | 0.0114 |
| W-UNSAFE (`G = 0`, gate-off, no reasoning) | 0.1944 | 0.1961 | 0.2043 | 0.2498 | 0.0120 |

Resource measurements accompany the timings and carry their own semantics. Peak resident set size was 66.3–66.9 MB across the three workloads; this is **process-lifetime peak RSS, not per-episode memory**, and it includes the interpreter and all loaded data. User CPU time was 0.097–0.106 s for the measured loop as a whole; this is **measured-loop user CPU time, not a CPU utilisation percentage and not a per-episode figure**. Neither should be read as a device resource budget.

**What these numbers are not.** They are not deployment performance, target-hardware performance, mobile performance, Android performance, real-time performance or production performance. They were taken on a development workstation on AC power with a desktop-class processor, and nothing about that configuration licenses an inference about a low-cost handset. They must not be scaled, extrapolated or adjusted to estimate target-device latency.

**No acceptance threshold is applied to them.** The performance criterion `H3 = X ms` remains OPEN and UNSUPPORTED: no externally justified latency bound exists for this application, and a low measured latency on a fast machine does not constitute passing a threshold that has never been set. The figures above are descriptive, and they are not evidence that the architecture is lightweight, efficient on low-end devices, real-time capable or suitable for deployment.

**Target-hardware benchmarking remains outstanding and mandatory.** It is deferred because representative physical hardware was not available for this study, not because it was judged unnecessary. No emulator, continuous-integration or cloud measurement is offered as a substitute, and none would be valid as one. Until that measurement exists, RQ-J2 is unanswered and the manuscript makes no claim about device-level feasibility.

---

## 12. Ablation Study

This section isolates what each governance level contributes, using the results already reported in §11. No additional experiment was run for it. Two constraints on interpretation apply throughout. First, the architecture's components are related by construction rather than by estimation, so an "ablation" here removes a mapping and observes the difference in admissible sets — it does not estimate an effect. Second, **a descriptive difference between two configurations is not a causal effect**: the figures below say how governance behaviour differs, not what difference that behaviour makes to any outcome.

### 12.1 Primary ablation — removing Level 2

Removing the advisory-scope restriction reduces C2 to C1 exactly. With `A_AI(S)` set to the full recommendation set at every state, C2's mapping collapses onto C1's; the participation gate remains, the scope restriction disappears. The ablation is therefore not an approximation of C1 but literally C1, which is what makes the subtraction in §11.4 clean:

```
Δ_L2 = div(C0, C2) − div(C0, C1)
```

C0 and C1 differ only in Level 1, and C0 and C2 differ in Levels 1 and 2 combined, so the subtraction removes the Level 1 term and leaves the Level 2 contribution alone. The measured values are **5.81% (PRIMARY) and 4.48% (RESOLUTION)** of departure-window hours (Table 10).

The equivalent ablation in the other direction — **removing Level 1** by setting `G(S) = 1` always — is realised by C0's configuration for AI participation, and its contribution is the C0 ↔ C1 divergence: **42.88% PRIMARY and 41.08% RESOLUTION**. This is reported as an interpretive comparison rather than as a separately implemented arm, since C0 already instantiates the ungoverned configuration.

**Table 13. Governance-level contribution, departure window.**

| Ablation | Realised by | Contribution (PRIMARY) | Contribution (RESOLUTION) |
|---|---|---|---|
| Remove Level 2 (advisory scope) | C2 → C1 | 5.81% | 4.48% |
| Remove Level 1 (participation gate) | C1 → C0 | 42.88% | 41.08% |
| Remove both | C2 → C0 | 48.69% | 45.56% |

The two levels are not comparable in magnitude for a reason that is structural rather than empirical: Level 1 acts on every UNSAFE hour, and UNSAFE is common at this site because darkness alone produces it, whereas Level 2 acts only on CAUTION hours, which are 5.8% of the departure window under PRIMARY. **The larger figure does not indicate that the participation gate is more valuable.** It indicates that the two mechanisms operate over differently sized portions of the record, and only the smaller portion is where existing architectures leave advisory scope unrestricted.

### 12.2 Sensitivity to input resolution

The PRIMARY and RESOLUTION configurations differ in wave model and record length, and the comparison functions as a sensitivity analysis over the empirical quantities whose design supports it (§11.4). `Δ_L2` moves from 5.81% to 4.48% — a 1.3-percentage-point spread — and the Level 1 contribution from 42.88% to 41.08%. Both move in the same direction and by comparable proportions, which is consistent with a finer wave model resolving nearshore sheltering that the coarser cell averages away.

The spread is the sensitivity result. It is not an uncertainty interval on a single true value, and the two configurations should not be averaged.

### 12.3 Structural equivalence of the traffic-light comparator

Substituting the traffic-light topology for the binary gate changes the admissible set on 0.00% of hours in both configurations (§11.6). As an ablation this is degenerate by construction — the two mappings are identical — and it is reported because that degeneracy is precisely the finding: an intermediate governance level that does not restrict advisory scope makes no difference to admissible AI output.

### 12.4 Removing hysteresis

Disabling dual-threshold hysteresis changes total transitions from 3,575 to 3,661, non-scheduled transitions from 199 to 222, and genuine oscillations from 20 to 26 over five years (Table 11). Hysteresis accounts for a **10.36%** reduction in non-scheduled transitions.

The effect is small because the phenomenon it addresses is small: genuine oscillation occurs approximately 5.2 times per year, and 93.9% of all transitions are the scheduled sunrise and sunset boundaries that hysteresis neither targets nor affects. The ablation therefore supports retaining hysteresis on cost grounds rather than on necessity grounds, and it is bounded to hourly resolution.

This ablation is available under the PRIMARY configuration only, for the reason given in §11.5. No RESOLUTION counterpart is reported, and none should be inferred.

### 12.5 Ablations not performed

Two further ablations are identified by the evaluation design and are **not** reported here, because no closed evidence supports them.

**Removing worst-case aggregation.** Replacing the max-severity aggregation in `f` with a different rule — a majority vote, a mean, or any scheme in which a single UNSAFE component does not dominate — would test whether worst-case aggregation is doing necessary work. A boundary-scenario set was specified for this purpose, but it was defined against threshold and time-classifier values that the specification has since superseded, and it has not been executed under the canonical configuration. It is future work, and no result is claimed for it.

**Component-level contribution.** The binding profile of the individual component classifiers at this site is documented elsewhere in the research record, but it characterises which component decides the state rather than ablating a component from the architecture, and the two are not interchangeable. No component ablation was run.

Reporting either as a completed ablation would overstate what the evaluation covers, and both are recorded in §14 as limitations of the ablation scope rather than omitted silently.

---

## 13. Discussion

This section separates two things that a results discussion easily merges. A **result** is what was measured or proved. An **interpretation** is what it is taken to mean. Each subsection below states the result first and marks the interpretation explicitly, because the interpretive claims are the ones a reader should be able to reject without disturbing the evidence.

### 13.1 What the evidence establishes

**Result.** The containment property holds by proof under stated assumptions (Theorem 6.3); the built engine honoured its admissible sets with zero violations and zero rule-set mismatches across the interface-contract state space (Section 11.2); advisory-scope restriction changed the admissible set on 5.81% of PRIMARY departure-window hours and 4.48% under the resolution configuration (Section 11.4); and a traffic-light topology ported onto the same state axis diverged from a plain binary gate on 0.00% of hours (Section 11.6).

**Interpretation.** Taken together these support a bounded claim: *advisory-scope governance conditioned on environmental state is formally specifiable, implementable within a small deterministic layer, and non-vacuous on a real environmental record.* Each element carries a different kind of weight. The proof establishes that the mechanism constrains output by construction. The fidelity evaluation establishes that this particular implementation does what the specification says. The replay establishes that the mechanism engages — that there exist hours where binary governance leaves the full recommendation set available and this architecture does not.

**None of the three establishes that the restriction is beneficial.** That would require evidence about operator behaviour and outcomes, which this study does not have.

### 13.2 The isolated second-level contribution is the load-bearing empirical result

**Result.** `Δ_L2 = 5.81%` (PRIMARY) / `4.48%` (RESOLUTION) of departure-window hours.

**Interpretation.** This figure is what makes the architecture more than a formal exercise. A governance level that never engages is indistinguishable in practice from its absence; the measured value shows that at this site, in this record, the CAUTION state occurs often enough to matter and that binary governance treats those hours as fully permissive.

The number should be read carefully in two respects. It is **small in absolute terms**, and this is expected rather than disappointing: the mechanism is designed to engage only in marginal conditions, and marginal conditions are by definition a minority of hours. A large value would indicate either a site with unusual conditions or thresholds drawn too widely. And it is a **behavioural difference between governance configurations**, not a safety delta — the phrase "5.81% safer" has no meaning here, and Section 11.4 states so explicitly.

The comparison also carries a structural check worth noting: because the two configurations differ only at the intermediate state, the divergence must equal the CAUTION rate exactly, and it does (Section 11.3). The measurement is therefore not an independent discovery so much as a quantification of how often the architecture's distinguishing state arises.

### 13.3 The structural comparator and the novelty question

**Result.** `C1 ↔ C3 = 0.00%` in both configurations, over all hours and the departure window, with the equivalence also established analytically from the mapping literals.

**Interpretation.** This addresses the most natural objection to the contribution — that a three-level governance topology already exists, so an intermediate state is not new. The comparison answers at the level the objection is posed: **at the admissible-recommendation-set level, a traffic-light topology and a plain binary gate are the same mechanism.** The intermediate level is not observable in AI output, because what it graduates is supervisory intensity rather than advisory scope.

Three caveats belong with this reading, and none is optional. The result is **confirmation of a structural equivalence, not an empirical discovery**; it follows in one line from the mapping definitions, and the replay confirms the harness computed what the tables say. It is **bounded by a disclosed modelling premise** — that the intermediate level leaves advisory scope unrestricted — and a reader who rejects that reading of the precedent rejects this result with it. And it is **not a criticism of the precedent framework**, which conditions its index on AI degradation for purposes of supervisory escalation and is appropriate for that purpose; it was not reproduced, not tested, and is not shown to be deficient.

Novelty is not carried by this result alone. It rests on the combination of the literature comparison (Section 2), the structural proposition, and the primary three-condition evaluation — no one of which is sufficient by itself.

### 13.4 Formal and empirical evidence answer different questions

**Result.** P1–P3 proved; F1–F3 closed with zero violations; E1–E4 and E6 measured on a deterministic census.

**Interpretation.** The separation maintained throughout this paper is itself a finding of sorts. A formal proof about advisory-scope containment is cheap to state and easy to over-read: it guarantees that the AI cannot exceed the configured scope, and nothing about whether the configured scope is the right one. Conversely, replay evidence quantifies engagement without establishing constraint — a measured divergence would be equally consistent with a mechanism that merely usually behaves as intended.

The implementation-fidelity layer is what connects them, and it is the layer most often omitted. It is also the layer with the narrowest scope here: exhaustive over the interface contract, and silent about everything outside it.

### 13.5 Policy, environment and fault must remain distinguishable

**Result.** The UNSAFE state is reachable by three distinct routes — an environmental hazard band, a required-input fault, or the nighttime policy — and the architecture records which (Sections 5, 9).

**Interpretation.** Collapsing these would be a design error with practical consequences, because they have different remedies and different epistemic status. A hazard band reflects measured conditions. A fault reflects the system's own degraded observation, and withholding advice under a fault is an admission of ignorance rather than a judgement about the sea. The nighttime policy is neither: it is **an architectural choice**, conservative by design, for which no source establishes that AI abstention is required. A navigation-lights rule supplies a temporal boundary [26]; it does not mandate that an advisory system fall silent.

That distinction matters most where it is least visible. At this site the temporal component accounts for the large majority of non-SAFE hours, so a reader who assumed UNSAFE meant "dangerous" would substantially misread the state distribution in Section 11.3. Section 14 records the consequence.

### 13.6 Implications for low-resource safety-critical decision support

**Result.** The governance layer is deterministic, requires no inference at decision time, reads solar boundaries from a frozen artefact rather than computing or fetching them, and operates over a small fixed state space (Sections 8, 9.1).

**Interpretation.** These are structural properties that make offline operation feasible, and they matter in settings where connectivity is intermittent and devices are modest [32], [33]. The design choice they reflect — governing a learned or complex advisory component with a simple deterministic layer — is transferable in principle: the governance layer's cost does not scale with the sophistication of what it governs.

**This paragraph is a design argument, not a performance result.** Whether the implementation meets the resource budget of any particular device is exactly what Section 11.7 does not establish, and nothing here should be read as evidence that it does.

### 13.7 What transfers, and what does not

**Result.** The architecture was specified generically and instantiated for one site.

**Interpretation.** Two kinds of portability must be kept apart.

**Structurally re-instantiable.** The governance pair `(G(S), A_AI(S))`, the containment ordering, the three theorems, the rule-set supply mechanism, the component-state interface and the separation of participation from advisory scope all transfer **by construction** to any correct instantiation. They depend on the *shape* of the problem — a finite ordered state space, a finite recommendation type space, an advisory engine that can be supplied its permitted scope — and not on the domain. Any setting exhibiting that shape, where an AI advises a person under conditions that vary in severity, can instantiate the pattern.

**Domain-specific.** The thresholds, the data sources and their resolutions, the vessel-conditioned parameterisation, the evidential basis of the rules, the component binding profile, and every measured rate in Section 11 are specific to Kota Kinabalu coastal fisheries. They were derived from site data and site-relevant literature, and **this study establishes no empirical portability beyond its site.**

**Structural re-instantiability is not empirical portability.** That the pattern can be re-instantiated elsewhere says nothing about what it would measure there, and a reader should not carry `Δ_L2 = 5.81%` into another domain as an expectation.

### 13.8 Relationship to governance frameworks

**Result.** The architecture references a navigation rule [26] as a threshold source and a risk-management framework [22] as vocabulary.

**Interpretation.** The mechanism is potentially complementary to organisational governance frameworks, which structure how AI risk is identified and managed but do not specify what an advisory system may output under a given environmental condition. A runtime state-conditioned scope restriction is the kind of concrete control such frameworks describe at a higher level of abstraction.

**No compliance or certification claim is made or implied**, and a comparison against functional-safety integrity-level schemes is not offered because the repository provides no basis for it (Section 2.6).

### 13.9 What this work does not demonstrate

Stated plainly, because the preceding subsections are the ones a reader will quote.

This work does **not** demonstrate: that operators trust, understand or prefer graduated advisory scope; that any recommendation changed any decision; that accidents are reduced or risk lowered; that real-world safety improves; that the architecture performs adequately on target deployment hardware; that it generalises empirically to other domains or sites; that the configured thresholds are optimal or correctly placed; that the configured admissible sets are optimal; or that the implemented rule set is complete for the domain. Several of these are not merely unmeasured but unmeasurable on retrospective replay, and Section 14 sets out which.

**Design rationale is not empirical validation.** Where this section explains why a choice was made, that explanation is an argument for the choice, not evidence that it was correct.

---

## 14. Threats to Validity

A limitations section that minimises its limitations is worth little. This one is deliberately long, and several entries bound results the paper depends on.

### 14.1 Construct validity

**Does `Δ_L2` measure what it claims?** The isolated second-level contribution is defined as `div(C0,C2) − div(C0,C1)`. The subtraction is exact rather than approximate — C0 and C1 differ only in the participation gate — so the residual is attributable to advisory-scope restriction by construction. The threat is not arithmetic but interpretive: `Δ_L2` measures *how often the two configurations admit different recommendation sets*, which is a statement about governance behaviour and not about safety, risk, accuracy or decision quality. Any reading of it as a safety delta is a construct error, and Sections 11.4 and 13.2 guard against it explicitly.

**Is divergence the right construct at all?** It counts admissible-set differences, not differences in what was actually recommended or what an operator would have done. A configuration could diverge on many hours while producing identical advisory content, if the withheld types would not have been generated anyway. In this prototype that gap is real and measurable: only one conclusion type is generated (Section 14.5), so the withheld types are withheld from a rule set that could not have produced them.

**Is the admissible set the right unit?** The architecture governs recommendation *types*. If the operationally meaningful distinction were finer — the same type with different content, or the confidence attached to it — then type-level governance would be too coarse a construct. No evidence here bears on that question.

### 14.2 Internal validity

**Threshold selection.** Every threshold is anchored to a named source: wind to national meteorological category onsets, rainfall to a published warning trigger and a hydrological intensity limit, the temporal boundary to a navigation-lights rule [26], and the ocean-state bands to vessel operability evidence [28], [29]. Anchoring is not validation. No threshold was optimised against an outcome, because no outcome data exists — there is no incident record for the site against which a classification could be scored. **The thresholds are defensible in provenance and untested in effect.**

**The medium-vessel boundary is interpolated.** The 2.8 m CAUTION/UNSAFE boundary for the medium vessel category is a conservative interpolation between the small and large categories rather than a directly sourced value, and it is weaker evidence than the small-vessel boundary it sits between.

**Rule-set completeness.** The implemented rule set is not exhaustive for the domain and does not claim to be. It contains four CAUTION rules, all concluding the same advisory type, derived from evidence requiring geographic or vessel-type adaptation. No level-B evidence — direct empirical evidence from small-scale fisheries at this site or a closely matched context — was identified for the deployment site. This is an evidential gap in the literature, not a search failure.

**Prototype fidelity.** Whether the implementation realises the specification was measured rather than assumed (Section 11.2), which removes this threat for the evaluated scope and leaves it open outside that scope (Section 14.5).

### 14.3 Data validity

**The marine-warning component was never measured.** No marine-warning archive exists for the study site, so the replay declares it excluded and pins it SAFE for aggregation. Two consequences follow. **Every severity figure in Section 11 is a lower bound** — a live required feed could only raise binding rates. And one implemented rule, whose antecedent is a marine-warning level, cannot be exercised on the historical record at all; it was exercised only in the constructed interface-contract evaluation.

**Grid resolution materially changes the result.** The PRIMARY and RESOLUTION configurations differ by 1.3 percentage points on `Δ_L2`. This is reported as a sensitivity result rather than resolved to a single number, but it is a genuine dependence on an input choice: a coarse wave cell averages away nearshore sheltering that a finer one resolves. A third wave model could move the figure again.

**The two configurations do not cover the same period.** PRIMARY spans five years, RESOLUTION three and a quarter. Their difference therefore confounds wave-model resolution with record length and with whatever conditions distinguish the two windows. The comparison is a sensitivity check, not a controlled experiment.

**Solar artefact provenance.** The frozen solar-event artefact was produced by a low-precision solar-position formulation and validated against an authoritative astronomical service to within a minute across a sample of dates. The formulation's publication-reference closure remains outstanding as a documentation matter.

### 14.4 Temporal and policy validity

> **The nighttime policy raises direct SAFE→UNSAFE transitions from 2 to 1,536, and removes 1,545 time-driven SAFE→CAUTION transitions, leaving zero.**

This is stated plainly because it is the largest single consequence of a design decision in this work. Adopting a solar-event temporal classifier that emits no intermediate state means the system moves from full advisory scope to no advisory participation without passing through the restricted state, once at sunset and once at sunrise on almost every day of the record.

**This is a governance consequence, not a danger count.** It does not mean conditions became hazardous 1,536 times; it means the governance configuration changed abruptly that many times. The step was accepted rather than smoothed: a twilight band or warning interval would soften it, and neither has a source. It is disclosed here as a cost of the design.

**Nighttime abstention is architectural policy, not a regulatory requirement.** A navigation-lights rule [26] supplies the sunset-to-sunrise boundary. It does not require an AI advisory system to abstain, night operation is neither prohibited nor physically unsafe as such, and operator authority is unconditional. A reader who regards the policy as too conservative is disagreeing with a design choice, not with evidence.

**The temporal component dominates the state distribution.** Because darkness alone produces the UNSAFE state, that state is common in the record for reasons having nothing to do with sea conditions. The state distributions in Section 11.3 must be read with this in mind; equating UNSAFE with "dangerous" would badly misread them.

**Configuration validity.** The admissible sets are *configured*, not empirically optimised. That `A_AI(CAUTION) = {Go, Delay}` rather than some other subset is a design decision. Monotonicity is proved of whatever sets are configured; it does not establish that these sets are the right ones.

### 14.5 Implementation validity

**The SAFE rule set is empty, and the fidelity result is bounded accordingly.**

`R-SAFE-001` remains DEFERRED: its antecedent is functionally a restatement of the SAFE state, and whether a state-restatement rule is scientifically warranted has not been decided. Consequently:

- `RS(SAFE)` contains no rules, and **all 32 SAFE episodes in the fidelity evaluation generated zero advisories**;
- the only advisory conclusion type the prototype generates is `Delay`;
- `Go`, `DepartureTime` and `Duration` remain *admissible* under the governance configuration but are produced by no implemented rule, and the latter two have no repository authority for their payload content at all;
- **F1 and F2 therefore exercise a populated CAUTION rule set and the gate-off path, but do not demonstrate fidelity of a populated SAFE rule set.** Nothing in this paper establishes that the full admissible space of the SAFE state is correctly enforced against rules attempting to fill it, because no such rules exist.

**The fidelity evaluation is exhaustive over the interface contract and nothing else.** It enumerates the Layer 3 interface state space and executes one episode per reachable consistent case. It is not the retrospective replay, not historically or environmentally exhaustive, and not exhaustive over deployment conditions or the situations an operator may encounter at sea.

**Fidelity holds under four assumptions** about the advisory engine (Section 4.5). If a future engine violates any of them, the containment property ceases to hold operationally regardless of the proof.

**Applicability to non-symbolic engines is untested.** The enforcement mechanism relies on the engine generating only conclusion types present in a supplied rule set. Whether an equivalent pre-generation constraint can be imposed on a learned or generative advisory component — as opposed to filtering its output afterwards, which this architecture deliberately avoids — is outside the scope of this work.

**Scalability to larger state vectors is untested.** Exhaustive enumeration is feasible because the state space is small; complexity bounds are given in Section 8, but no larger instantiation was built or measured.

### 14.6 Evaluation-scope validity

**Two ablations identified by the evaluation design were not performed**, and their absence bounds what Section 12 covers.

- **Worst-case aggregation was not ablated.** Whether taking the maximum severity across components is doing necessary work — as against a majority, mean or other rule — was not tested. A boundary-scenario set was specified for this purpose but defined against threshold and temporal-classifier values that have since been superseded, and it has not been executed under the canonical configuration.
- **No component ablation was performed.** The site binding profile characterises which component decides the state; it does not remove a component from the architecture, and the two are not interchangeable.

**E4 is a PRIMARY-only characterisation.** No resolution counterpart to the transition and hysteresis figures is reported, and none exists. This is a scoped exclusion with a methodological reason — event counts from windows of differing length and coverage are not comparable merely because both configurations have names — and it is **not** a claim that those figures are insensitive to resolution. That has not been tested.

**Hysteresis findings are bounded at hourly resolution.** Sub-hourly oscillation is invisible in hourly data. The near-null oscillation result bounds chattering at the resolution measured and says nothing below it.

### 14.7 Performance validity

**No target-hardware performance evidence exists.** E5 is open. What was completed is benchmark-harness validation and a reference run on a development workstation; measurement on representative physical hardware for the intended deployment context was not performed, because such hardware was not available.

- The reference measurements are **development-machine reference measurements**, taken on a desktop-class processor on mains power. They are not deployment, target-hardware, mobile, real-time or production performance, and **must not be scaled or extrapolated** to estimate device latency. No emulator, continuous-integration or cloud measurement is offered as a substitute, and none would be valid as one.
- **No acceptance threshold exists.** The latency criterion remains open and unsupported: no external standard or study supplies a justified bound for this application, and a low measured latency on a fast machine is not a threshold pass.
- Resource figures carry narrow semantics — process-lifetime peak memory rather than per-episode, and measured-loop CPU time rather than a utilisation percentage — and should not be read as a device budget.
- **Target-hardware benchmarking remains outstanding and mandatory.** Until it exists, RQ-J2 is unanswered and no claim about device-level feasibility is available from this work.

Asymptotic complexity (Section 8) does not substitute for it. "Small fixed state space, therefore suitable for low-resource deployment" is not a valid inference.

### 14.8 External validity

**Single site, single fleet, single instantiation.** All empirical values are exact for one coastal location over one window under one vessel parameterisation. They are not estimates of future conditions at that site and carry no expectation for any other.

**Retrospective replay is not prospective deployment.** The replay reconstructs what the governance layer would have output given recorded conditions. It involves no operator, no interface, no advisory delivery and no decision. A deployed system would encounter live data faults, freshness constraints, interface effects and human responses that the replay cannot represent.

**No human evaluation was conducted.** Nothing in this work bears on whether operators understand graduated advisory scope, trust it, prefer it to binary governance, or behave differently under it. Decision-support utility has no operational definition on replay data alone, and no formula was invented to supply one. Trust, calibrated reliance, advisory usefulness and real-world safety outcomes all require field data outside this study's evidence base.

**The comparator's modelling premise is disputable.** The structural equivalence result depends on reading the precedent's intermediate level as leaving advisory scope unrestricted. That reading is stated explicitly (Sections 10.1, 13.3) precisely so it can be challenged; if it is wrong, the equivalence result falls with it.

**No compliance claim.** The architecture is not certified against any standard, and the absence of a comparison to functional-safety integrity-level schemes is an acknowledged gap (Section 2.6) rather than an implicit claim of equivalence.

### 14.9 Statistical validity

The replay is a **deterministic census**, not a sample. No p-value, confidence interval or significance test is reported anywhere in this paper, because reporting one would impute sampling variability to an enumeration that has none. The PRIMARY/RESOLUTION spread is a sensitivity result between two measurements, not an interval estimate of one quantity, and the two should not be averaged.

The one quantity admitting distributional treatment is latency, which carries genuine runtime variance — and it is precisely the quantity whose target-hardware value is unknown.

---

## 15. Conclusion

Runtime AI governance in safety-critical settings is overwhelmingly binary: mechanisms decide whether an AI participates, and leave what it may say unconstrained. That framing suits systems that act. It fits poorly where an AI advises a person under conditions that vary in severity, because it offers no way to express the position that matters most in marginal conditions — the AI remaining available while the categories of advice it may offer are narrowed.

This paper specified a two-level governance pair `(G(S), A_AI(S))` conditioned on a deterministic classification of environmental state, separating AI participation from AI advisory scope. Three properties were proved: totality of the classifier over ideal and operational inputs, monotonicity of the admissible-set map with strict containment, and Safety Dominance — that generated recommendations are contained in the admissible set for the governing state — established by construction from the rule-set supply mechanism under stated engine assumptions, rather than by filtering output after generation.

The architecture was implemented as a prototype whose rule engine consumes a read-only component-state interface from the governance layer and never recomputes it. Evaluated exhaustively over its interface contract — 292 episodes producing 454 advisory records — the implementation produced zero admissible-set violations and zero rule-set mismatches, bounded by an empty SAFE rule set that leaves the benign state's full advisory space unexercised.

Replaying the governance pipeline over five years of hourly environmental records for a coastal fisheries site isolated the contribution of the second governance level: advisory-scope restriction changes the admissible recommendation set on **5.81%** of departure-window hours relative to binary participation-only governance, and **4.48%** under a higher-resolution sensitivity configuration, the spread between them being a resolution-sensitivity result rather than an uncertainty interval. Over the same record, a traffic-light governance topology instantiating the closest structural precedent diverges from a plain binary gate on **0.00%** of hours — its intermediate level is not observable in AI output at all. That comparison confirms a structural equivalence established analytically; it is not an empirical discovery, and it is bounded by a disclosed reading of the precedent.

**The limitations are substantial and several bound the central results.** All empirical values are exact descriptive values for one site over one window, not estimates of anything else. The marine-warning component was never measured, making every severity figure a lower bound. The SAFE rule set is empty, so implementation fidelity is demonstrated for the restricted state and the gate-off path but not for a populated benign-state rule set. The nighttime abstention policy is an architectural choice, not a regulatory requirement, and it raises direct transitions from full scope to no participation from 2 to 1,536 across the record. No human evaluation was conducted, so nothing here bears on operator trust, reliance or behaviour. **And target-hardware performance remains unmeasured**: the benchmark harness is validated and a development-machine reference run is complete, but no device-level feasibility claim is available from this work, and no latency acceptance threshold exists to claim it against.

Future work follows from those boundaries rather than from ambition. Target-hardware benchmarking on representative physical devices is outstanding and mandatory before any deployment-suitability claim can be made. A populated SAFE rule set requires resolving whether a state-restatement rule is scientifically warranted, and the two unrealised recommendation types require domain evidence the repository does not contain. Field evaluation with operators is the only route to the questions this study cannot reach — whether graduated advisory scope is understood, trusted, or useful. Re-instantiation in a second domain would test whether the pattern transfers structurally, as the construction suggests it should and as no evidence here demonstrates. And a comparison against functional-safety integrity-level schemes requires a literature pass this work has not performed.

What this paper contributes, stated at the level the evidence supports: **a formally specified and executable pattern for separating AI participation from state-dependent advisory scope** — proved to constrain output by construction, implemented and measured for fidelity within a bounded scope, and shown to engage on a real environmental record rather than only in principle.

---

## References

*Compiled from repository sources only — verified entries reused from the conference manuscript and from corpus extraction notes. No new literature search was performed and no bibliographic metadata was reconstructed. Entries marked `REFERENCE_METADATA_INCOMPLETE` carry the metadata the repository supports; the missing fields are recorded in `data/journal1-manuscript-framing/citation-audit.md` and must be completed before submission.*

[1] I.F. Ramos, G. Gianini, M.C. Leva, and E. Damiani, "Collaborative intelligence for safety-critical industries: A literature review," *Information*, vol. 15, no. 11, p. 728, 2024. doi: 10.3390/info15110728

[2] J. Perez-Cerrolaza, J. Abella, M. Borg, C. Donzella, J. Cerquides, F. J. Cazorla, C. Englund, M. Tauber, G. Nikolakopoulos, and J. L. Flores, "Artificial intelligence for safety-critical systems in industrial and transportation domains: A survey," *ACM Computing Surveys*, vol. 56, no. 7, article 176, 2024. doi: 10.1145/3626314

[3] V. Indykov, D. Strüber, and R. Wohlrab, "Architectural tactics to achieve quality attributes of machine-learning-enabled systems: A systematic literature review," *Journal of Systems and Software*, vol. 223, p. 112373, 2025. doi: 10.1016/j.jss.2025.112373

[4] N. Flehmig, M. A. Lundteigen, and S. Yin, "Implementing artificial intelligence in safety-critical systems during operation: Challenges and extended framework for a quality assurance process," in *Proc. IEEE IECON 2024: 50th Annual Conf. IEEE Industrial Electronics Society*, 2024. doi: 10.1109/IECON55916.2024.10906021

[5] A. Baxi, "The comprehension-gated agent economy: A robustness-first architecture for AI economic agency," *arXiv preprint* arXiv:2603.15639, 2026.

[6] Abd. Rahim et al., "Survival decisions and adaptation strategies of small-scale fishers in the face of extreme weather impacts in coastal areas," *Journal of Marine and Island Cultures*, vol. 13, no. 3, 2024. doi: 10.21463/jmic.2024.13.3.05

[7] L. Yamin, T.-C. Kuo, and N. Aziz, "Interplay of traditional knowledge and adaptive capacity in climate change adaptation of small-scale fishers in central Terengganu, Malaysia," *Frontiers in Marine Science*, vol. 12, p. 1492131, 2025. doi: 10.3389/fmars.2025.1492131

[8] C. Atacan and F. O. Düzbastılar, "Determination of risk perception in small-scale fishing and navigation," *Ege Journal of Fisheries and Aquatic Sciences*, vol. 40, no. 1, pp. 1–14, 2023. doi: 10.12714/egejfas.40.1.01

[9] C. Dominguez-Péry, R. Tassabehji, F. Corset, and Z. Chreim, "A holistic view of maritime navigation accidents and risk indicators: examining IMO reports from 2011 to 2021," *Journal of Shipping and Trade*, vol. 8, p. 11, 2023. doi: 10.1186/s41072-023-00135-y

[10] B. Könighofer et al., "Shields for safe reinforcement learning," *Communications of the ACM*, vol. 68, no. 11, pp. 80–90, 2025. doi: 10.1145/3715958

[11] D. Corsi, G. Amir, A. Rodríguez, C. Sánchez, G. Katz, and R. Fox, "Verification-guided shielding for deep reinforcement learning," in *Proc. 1st Reinforcement Learning Conf. (RLC)*, 2024. doi: 10.48550/arXiv.2406.06507

[12] M. Kwon, T. Ingebrand, U. Topcu, and L. Feng, "Adaptive shielding for safe reinforcement learning under hidden-parameter dynamics shifts," *arXiv preprint* arXiv:2506.11033v2, 2026.

[13] J. Vermaelen and T. Holvoet, "Tumato 2.0: A constraint-based planning approach for safe and robust robot behavior," *Annals of Mathematics and Artificial Intelligence*, vol. 93, pp. 541–567, 2025. doi: 10.1007/s10472-024-09949-3

[14] H. Odriozola-Olalde, M. Zamalloa, and N. Arana-Arexolaleiba, "Shielded reinforcement learning: A review of reactive methods for safe learning," in *Proc. 2023 IEEE/SICE Int. Symp. System Integration (SII)*, 2023. doi: 10.1109/SII55687.2023.10039301 [REFERENCE_METADATA_INCOMPLETE — no page range in repository evidence]

[15] D. Dalrymple et al., "Towards guaranteed safe AI: A framework for ensuring robust and reliable AI systems," *arXiv preprint* arXiv:2405.06624, 2024.

[16] A. Bajcsy and J. F. Fisac, "Human–AI safety: A descendant of generative AI and control systems safety," *arXiv preprint* arXiv:2405.09794, 2024.

[17] R. Bloomfield and J. Rushby, *Assurance of AI Systems from a Dependability Perspective*, SRI Technical Report SRI-CSL-2024-02R3, SRI International, 2025. doi: 10.48550/arXiv.2407.13948

[18] H. Wang, C. M. Poskitt, and J. Sun, "AgentSpec: Customizable runtime enforcement for safe and reliable LLM agents," in *Proc. IEEE/ACM 48th Int. Conf. Software Engineering (ICSE '26)*, Rio de Janeiro, Brazil, Apr. 2026. [REFERENCE_METADATA_INCOMPLETE — no DOI or page range in repository evidence]

[19] Z. Chen, M. Kang, and B. Li, "SHIELDAGENT: Shielding agents via verifiable safety policy reasoning," in *Proc. 42nd Int. Conf. Machine Learning (ICML)*, Vancouver, Canada, PMLR 267, 2025. arXiv:2503.22738v2 [REFERENCE_METADATA_INCOMPLETE — no DOI or page range in repository evidence]

[20] Md. Shamsujjoha, Q. Lu, D. Zhao, and L. Zhu, "Swiss cheese model for AI safety: A taxonomy and reference architecture for multi-layered guardrails of foundation model based agents," in *Proc. IEEE 22nd Int. Conf. Software Architecture (ICSA)*, 2025, pp. 37–48. doi: 10.1109/ICSA65012.2025.00014

[21] Z. Feng, J. McDonald, and C. Zhang, "Levels of autonomy for AI agents," *arXiv preprint* arXiv:2506.12469, 2025.

[22] National Institute of Standards and Technology, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1, Gaithersburg, MD: NIST, Jan. 2023. doi: 10.6028/NIST.AI.100-1

[23] A. Reuel, P. Connolly, K. J. Meimandi, S. Tewari, J. Wiatrak, D. Venkatesh, and M. Kochenderfer, "Responsible AI in the global context: Maturity model and survey," in *Proc. 2025 ACM Conf. Fairness, Accountability, and Transparency (FAccT '25)*, Athens, Greece, 2025, pp. 2505–2541. doi: 10.1145/3715275.3732165

[24] Z. Engin and D. Hand, "Towards adaptive categories: Dimensional governance for agentic AI," *arXiv preprint* arXiv:2505.11579, 2025.

[25] N. Kolt, M. Shur-Ofry, and R. Cohen, "Lessons from complex systems science for AI governance," *Patterns*, vol. 6, p. 101341, 2025. doi: 10.1016/j.patter.2025.101341

[26] International Maritime Organization, *Convention on the International Regulations for Preventing Collisions at Sea, 1972 (COLREGs), as amended*, Rule 20(b). London: IMO.

[27] T. Gao, "Mapping the Decision-Making Factors of Small-Scale Fishers: A Case Study of Penang," M.Sc. thesis, International Master of Science in Rural Development, University of Pisa / WorldFish (CGIAR), 2024. [Online]. Available: https://hdl.handle.net/10568/152289

[28] O. Yaakob, F. E. Hashim, M. R. Jalal, and M. A. Mustapa, "Stability, seakeeping and safety assessment of small fishing boats operating in southern coast of Peninsular Malaysia," *Journal of Sustainability Science and Management*, vol. 10, no. 1, pp. 50–65, 2015.

[29] C.-H. Jeong and N. Im, "Proposal of restrictions on the departure of Korea small fishing vessel according to wave height," *Journal of Marine Science and Engineering*, vol. 11, no. 7, p. 1302, 2023. doi: 10.3390/jmse11071302

[30] M. S. Haque and S. Al Jufaili, "Applications of artificial intelligence in fisheries: From data to decisions," *Big Data and Cognitive Computing*, vol. 10, no. 1, art. 19, 2026. doi: 10.3390/bdcc10010019

[31] A. Longobardi et al., "Peskas: Automated analytics for small-scale, data-deficient fisheries," *SoftwareX*, vol. 29, p. 102028, 2025. doi: 10.1016/j.softx.2024.102028

[32] A. Katende, "Rethinking data-efficient artificial intelligence for low-resource settings," *Machine Learning with Applications*, vol. 23, p. 100796, 2026. doi: 10.1016/j.mlwa.2025.100796

[33] P. Bhuvaneswari, K. D. V. Prasad, M. Ashraf, and S. Jadhav, "A human-centered hybrid AI framework for optimizing emergency triage in resource-constrained settings," *Intelligence-Based Medicine*, vol. 12, p. 100311, 2025. doi: 10.1016/j.ibmed.2025.100311

---

## Figures

*(Place figures in `/figures/` subfolder and reference here)*

**Planned figures:**
- Figure 1: Three governance dimensions (adapted from conference paper)
- Figure 2: Full architecture diagram with all four layers (expanded from conference paper Fig. 3)
- Figure 3: State transition diagram with formal notation
- Figure 4: Algorithm flow diagrams
- Figure 5: Experimental results — condition comparison across metrics
- Figure 6: Ablation results
