# Evaluating Graduated Advisory-Scope Governance for AI Decision Support

<!--
================================================================================
AMICT CONFERENCE REBUILD — V4 (working draft, Markdown)

Version:      v4-amict-rebuild
Baseline:     v3-revision/manuscript-v3.md (source material only; structure NOT inherited)
Status:       DRAFT — pre-format. No .docx / .pdf / .tex produced.
Review mode:  DOUBLE-BLIND — no author names, affiliations or identifying
              acknowledgements appear in this file.

Frozen authorities implemented by this draft:
  data/amict-conference-rebuild/contribution-freeze-v2.md
  data/amict-conference-rebuild/rq-narrative-freeze.md
  data/amict-conference-rebuild/novelty-audit-report.md (+ addendum-001)
  data/amict-conference-rebuild/source-validation-report.md

MECHANISM_NOVELTY = WITHDRAWN. The paper claims formalisation, scoped
generalisation and empirical characterisation of an existing mechanism
pattern. It does not claim invention of the mechanism.

Visuals: 3 tables. Architecture figure OMITTED_FOR_SPACE (restore for journal).
Pagination: designed to the historical six-page envelope by word-budget proxy;
final pagination requires the current official AMICT template.
================================================================================
-->

## Abstract

Governance of AI decision support in safety-critical settings is commonly framed in the reviewed literature as one binary question: whether the AI may participate. A second question — which types of recommendation it may present — is answered at runtime in certified collision-avoidance avionics, where advisory types are progressively inhibited as an externally measured state worsens, but we did not identify a corresponding operational treatment in that literature. We specify graduated advisory-scope governance as an operational contract: participation gating and advisory-scope restriction as separate mappings over a multi-component environmental state, a classifier defined over observations rather than ideal values, explicit handling of invalid, absent, stale and unmeasured inputs, and admissible recommendation types supplied to the reasoning layer before inference. A bounded executable evaluation found no violation of the configured admissibility contract. Over five years of retrospective environmental traces, the intermediate level changed the admissible recommendation set in 5.81 percent of departure-window hours relative to a participation-only gate, and in 4.48 percent under an alternative environmental-data configuration, while a three-level comparator lacking advisory-scope differentiation diverged from a binary gate in 0.00 percent. These are governance-layer measurements; they do not establish safety or decision-quality outcomes.

**Keywords** — AI governance, runtime governance, decision support, advisory scope, safety-critical systems, formal specification

## I. Introduction

A common governance framing in the reviewed AI decision-support literature is binary: whether the AI may participate at all. Under that framing, when conditions degrade the AI is switched off, or it continues to offer its full range of advice on evidence that no longer supports it. A second governance question is available and less often asked — not whether the AI participates, but which *types* of recommendation it may present to the human who decides.

That second question is not new. Certified collision-avoidance avionics already answers it: as an externally measured state worsens, specific advisory types are progressively inhibited and the admissible set contracts to empty [9]. Formal verification of state-conditioned advisory logic has precedent in the same domain [10]. Any contribution in this area must start from that precedent rather than around it.

Within the reviewed AI decision-support and governance literature, we did not identify a formal operational treatment that combines a classified multi-component environmental state, explicit observation-resolution and exclusion semantics, and a state-conditioned advisory-type admissibility contract. Analogous restriction of advisory types conditioned on an externally measured state is established practice in certified collision-avoidance avionics.

This work formalises an existing governance pattern — runtime restriction of advisory types by an externally measured state, established in certified collision-avoidance avionics — as an operational specification over a classified multi-component environmental state, and characterises empirically how often its intermediate advisory-scope level produces a governance outcome distinct from participation-only governance.

We ask three questions.

**RQ1.** How can graduated advisory-scope governance be specified and verified operationally, separating AI participation from admissible advisory scope under incomplete, stale or excluded environmental observations?

**RQ2.** How often does graduated advisory-scope governance produce governance outcomes that differ from participation-only governance in retrospective environmental replay?

**RQ3.** How does the measured governance-outcome divergence differ under the alternative environmental-data configuration?

The paper makes two contributions. **C1** is a formal operational specification of graduated advisory-scope governance: it separates participation from admissible advisory scope, conditions on a classified multi-component environmental state rather than a single hazard variable, and defines explicit observation-resolution, declared-exclusion, failure and containment semantics, with bounded executable conformance evidence (Section III). **C2** is an empirical characterisation, over five years of retrospective environmental traces, of when advisory-scope graduation produces governance outcomes distinct from participation-only governance, under two environmental-data configurations and against an intermediate-state control (Sections IV and V).

The deployment context — small-scale coastal fisheries — instantiates and evaluates the construct. It is not the claim.
## II. Related Work

Prior work informing this study is considered in two groups. The first comprises AI decision-support and governance literature examined for the governance framing and comparator set [1]–[5]. The second comprises targeted sources examined specifically for comparison with the closest mechanism precedents [9]–[14]. Keeping these groups distinct separates the governance framing from the mechanism-level comparisons developed below.

TABLE I codes the closest mechanism families against the construct developed here.

**TABLE I.** Closest prior mechanism families. "Scope conditioned" asks whether the set of recommendation types presented to a human is restricted by the runtime state.

| Family | Governed object | Runtime state source | Scope conditioned | Formal guarantee | Relation to this work |
|---|---|---|---|---|---|
| Collision-avoidance advisory inhibition [9] | Advisory types issuable to a pilot | Radio altitude, banded; configuration discretes | **Yes** — nested, contracting to empty | Certified design requirement | **Operational precedent for the mechanism** |
| Verified collision-avoidance advisory logic [10] | Advisory selection | Encounter state | Yes — safe advisory set is state-dependent | **Yes** — game-logic proof | Precedent for formal treatment of advisory logic |
| Levels of automation [11] | Degree of automation per stage | None — assigned at design time | Partly: narrows the number of alternatives | No | Historical precedent for graduated option narrowing |
| Adaptive automation [12] | Function allocation, automation level | Operator state, task, environment, performance | No | No | Runtime adaptation exists; the governed object differs |
| Selective prediction and deferral [13] | Whether the model predicts at all | Model-internal calibrated confidence | No | Coverage guarantee | Governs participation, not scope |
| Shielding and action masking [5] | Executable action set of an agent | Automaton or safety specification | No — no human adviser | Yes | Admissible sets exist; enforcement is by output filtering |
| Graduated runtime governance [4], [6], [7] | Supervisory intensity; agent permissions; oversight tier | Degradation index; robustness audit; task metadata | No | Partly — monotone properties by construction | Graduation exists; the graduated variable is not advisory scope |

Three conclusions follow. First, the mechanism precedent exists: advisory-type restriction conditioned on an externally measured state is established practice in certified avionics, where the admissible sets are nested and contract to empty as the measured state worsens [9]. Governance frameworks in current use identify graduated, risk-proportionate control as an objective without specifying a runtime mechanism that enforces it [8]. Second, the formal-property precedent exists: monotone restriction of an admissible set, totality of a deterministic classifier, and proved bounds on what a governed component may emit all appear in prior work [6], [7], [10], so none of those properties is offered here as a new result. Third, what we did not identify in the reviewed AI-governance literature is the combination: a classified multi-component environmental state, explicit observation-resolution and exclusion semantics, and a state-conditioned advisory-type admissibility contract defined independently of the generator.

This work formalises an existing governance pattern — runtime restriction of advisory types by an externally measured state, established in certified collision-avoidance avionics — as an operational specification over a classified multi-component environmental state, and characterises empirically how often its intermediate advisory-scope level produces a governance outcome distinct from participation-only governance.
## III. Operational Governance Formalisation

### A. The governance pair

An environmental state *E* is classified into a safety state by a total classifier *S* = *f*(*E*). The classifier is composed of five component classifiers — wind, rainfall, marine warning level, ocean state and time of day — aggregated by maximum severity over the order SAFE ≺ CAUTION ≺ UNSAFE, with vessel category supplied as a configuration parameter rather than sampled. Conditioning on five components rather than on a single hazard variable is the sense in which the construct generalises beyond the operational precedent discussed in Section II.

The safety state determines a **governance pair** (*G*(*S*), *A*_AI(*S*)). The participation gate *G*(*S*) ∈ {0, 1} determines whether the AI participates at all. The admissible advisory space *A*_AI(*S*) determines which recommendation *types* may be presented when it does. The two are distinct mappings under two constraints: *G*(*S*) = 0 implies *A*_AI(*S*) = ∅, and the intermediate state admits a strictly smaller set than the permissive state. The resulting containment is *A*_AI(SAFE) ⊃ *A*_AI(CAUTION) ⊃ *A*_AI(UNSAFE) = ∅. Human decision authority is unconditional in all three states; the architecture constrains what the AI may recommend, not what the operator may do.

### B. Ideal and operational classification

A deployed classifier does not consume ideal values. Each component is read as an observation Obs_i = (X_i × 𝕋) ∪ {⊥}, a value paired with the instant it was taken, or a fault. A resolution map ρ_{D,τ} discharges exclusion, validation and freshness before classification, giving the **operational classifier** *F*_{D,τ} = *f* ∘ ρ_{D,τ}. We write *f*(*E*) for the ideal case and *F*_{D,τ} for deployed behaviour; the distinction is load-bearing, and conflating the two misstates what a deployment actually computes.

Four observation conditions receive four distinct responses, summarised in TABLE II. Three of them are faults and resolve to ⊥, which each component classifier maps to the most severe state, so the fail-safe follows from the component mapping together with the maximality of that state rather than from a separate pre-check. The fourth is not a fault at all: a component for which no data source exists in a deployment is handled by a declared exclusion set *D*, evaluated **before** fault resolution and pinned at the least severe value. The distinction is not cosmetic. Applied to the retrospective record of Section IV, treating an unmeasured component as a fault would classify every one of the 43,848 hours as most severe and void the evaluation.

**TABLE II.** Observation conditions and their governance treatment.

| Condition | Treatment under ρ_{D,τ} | Governance effect | Interpretation |
|---|---|---|---|
| Required observation **invalid** (outside physical range) | Resolves to ⊥ | Component maps to UNSAFE; participation closes by maximum severity | Fault |
| Required observation **absent** | Resolves to ⊥ | As above | Fault |
| Required observation **stale** (older than the permitted age) | Resolves to ⊥ via the freshness map | As above | Fault |
| Component **unmeasured** — no data source exists in this deployment | Declared in *D*, evaluated before faults, pinned SAFE | Cannot raise the classification | Not a fault; every severity figure becomes a lower bound |

*D* is declared and fixed for a deployment rather than expanding at runtime, cannot contain the time component — a clock or solar-lookup failure is a fault, never an exclusion — and cannot contain every component. Its three obligations are indivisible: *D* is declared, the pin is at the least severe value, and every severity figure produced under a non-empty *D* is reported as a lower bound.

### C. Formal properties and pre-reasoning admissibility

The formalisation establishes totality of the operational classifier over the observation space, monotonicity of *A*_AI over the severity order, and the containment of generated advisories within the admissible set. These properties verify the specification; they are **not** claimed as new. Related formal properties are established in the prior graduated-governance and shielding work discussed in Section II. Full proofs are omitted here for space; only the properties used by the evaluation are stated.

What is worth stating is the enforcement route. Admissibility is not achieved by filtering generated output. The governance layer supplies a rule set *RS*(*S*) to the reasoning layer **before** any reasoning begins, and no rule producing an inadmissible type exists in the active set. Correctness is therefore a property of the active rule set rather than of a runtime check, and the admissibility contract is defined over recommendation types independently of the generator that produces them.

### D. Bounded executable conformance

The executable implementation produced **zero violations of the configured advisory admissibility contract within the bounded deterministic interface-contract fidelity state space**. The evaluation covered 292 primary episodes — 32 in the permissive state, 260 in the intermediate state — of which 244 generated at least one advisory and 16 generated none, yielding **454 advisory records**. A further 162 structural cases in which participation was gated off sit outside that denominator.

This evidence is bounded in one direction that must be stated plainly. The permissive-state rule set is **empty**: the corresponding requirement is deferred, all four implemented rules are intermediate-state rules, and the single generated conclusion type is *Delay*. The 454 figure counts advisory **records**, not advisory types. Containment was therefore exercised only on the restrictive side — no advisory was generated that a narrower state would have had to suppress.
## IV. Evaluation Method

### A. Setting and record

The governance layer was instantiated for small-scale coastal fisheries at a coastal site in Sabah, Malaysia (5.98° N, 116.01° E) and executed against hourly environmental data for that location, classifying the safety state at every hour and recording which component determined the outcome. The primary configuration covers **43,848 hourly records**, approximately five years. Results are reported over the departure window, the morning hours in which the departure decision is actually taken, for the small-vessel class that dominates the deployment population.

Component thresholds are anchored to independently established sources rather than chosen for the evaluation. Wind and rainfall boundaries follow published national meteorological warning criteria; the vessel-conditional wave-height rows draw on seakeeping analysis of Malaysian hulls [18] together with a length-dependent departure formula derived from a 23-year Korean accident record [19]; the time component takes its boundary from the navigation-lights obligation in COLREGs Rule 20(b) [17] and evaluates sunrise and sunset per date from a frozen daily table computed once for the site. That table implements a NOAA-style low-precision solar-position formulation [15], checked against the U.S. Naval Observatory reference service [16] at the site coordinate with a maximum difference below one minute across the sampled events. The time boundary is a conservative governance policy choice; no source establishes that AI advisory participation must be withdrawn at sunset, and none is claimed.

### B. Comparators

Four conditions were run over the same record.

- **C0 — ungated.** The full recommendation set is available at every hour.
- **C1 — binary gated.** Participation is controlled by the classified state; advisory scope is never restricted while the AI is active.
- **C3 — traffic-light baseline.** A three-level structure in the manner of the closest structural precedent identified in the review [4]: the AI remains the active component at both the permissive and the intermediate level with unchanged scope, and is replaced by a non-AI backup only at the most severe level.
- **C2 — the proposed configuration.** Both governance levels active.

The metric is **admissible-set divergence**: for each hour, whether two conditions permit the same set of recommendation types. This is a property of the governance layer and is computed without invoking the reasoning engine.

### C. Two environmental-data configurations

Every reported quantity is computed under two configurations. The **primary** configuration uses the longer record with a coarser reanalysis wave field. The **resolution** configuration uses a shorter record with a finer-resolution wave model. These are **alternative environmental-data configurations**, not repeated trials, confidence intervals, uncertainty bounds or independent replications; both values are reported and neither is resolved into the other.

### D. Declared exclusions and their consequence

No historical archive of marine warning levels exists for the site. The replay therefore declares that component as an exclusion, pinned at the least severe value throughout, and **every severity figure reported in this paper is consequently a lower bound**. Separately, the storm-code input to the rainfall classifier is zero across the whole record, because the data provider documents thunderstorm estimation as unavailable for this region; because that input can only escalate a classification, rainfall-driven figures are lower bounds by an unknown margin. Neither exclusion is a property of the specification: a deployment with a live marine-warning feed or a reliable storm-code feed declares no exclusion and carries no such bound.
## V. Results

All figures reported here are governance-layer quantities. They describe divergence between admissible recommendation sets, and they do not describe human, operational or physical outcomes. Every severity figure is a lower bound, for the reasons given in Section IV. The departure window over the primary record comprises 9,135 hourly observations.

### A. Level 2 contribution (RQ2)

Over the primary configuration the two governance levels separate cleanly. C0 and C1 differ on **42.88%** of departure-window hours. This is the contribution of the participation gate alone: the hours in which the classified state closes participation while the ungated condition continues to offer the full recommendation set. C0 and C2 differ on **48.69%**.

The difference between those two quantities is attributable to the advisory-scope level alone. **Δ_L2 = 5.81%** of departure-window hours: hours in which the participation gate is open, the AI is active, and the proposed condition nonetheless admits a strictly smaller set of recommendation types than a participation-only gate would admit. In those hours a binary gate leaves the full recommendation set available.

The answer to RQ2 is therefore that graduated advisory-scope governance produces a governance outcome distinct from participation-only governance in 5.81% of departure-window hours under the primary configuration.

Two structural identities follow from the comparator definitions and both hold exactly, which is a consistency check on the implementation rather than an independent finding. C1 and C2 agree at the permissive state, where both admit the full set, and at the most severe state, where both admit the empty set; they can therefore differ only at the intermediate state, and their divergence must equal the intermediate-state rate. C0 differs from C1 only where the gate closes, so their divergence must equal the gate-closure rate. The measured values reproduce both identities.

### B. Intermediate-state control (RQ2)

The 5.81% figure is interpretable only if the difference is attributable to advisory-scope differentiation rather than to the presence of a third labelled governance state. C3 isolates that question. It instantiates a three-level traffic-light structure in the manner of Flehmig et al. [4], in which the AI remains the active component at both the permissive and the intermediate level with unchanged scope, and is replaced by a non-AI backup only at the most severe level.

**C1 and C3 diverge on 0.00% of hours**, under both configurations, across every hour of both records. The result does not move with the wave model, because it is a property of the mapping from classification to admissible set rather than of the environmental data. A three-level classification whose intermediate level governs supervisory response rather than advisory scope produces, at the point of AI output, exactly what a two-level gate produces. The third level is not observable in what the system is permitted to recommend.

Under the evaluated comparator definitions, adding an intermediate labelled governance state without advisory-scope differentiation produces no admissible-set divergence. The measured Δ_L2 is therefore associated with the advisory-scope restriction itself rather than with the existence of a third state. This interpretation is bounded to the comparator definitions given in Section IV; it does not extend to traffic-light or three-state systems in general, and it is a statement about one instantiated structure rather than about a class of designs.

### C. Alternative environmental-data configuration (RQ3)

The resolution configuration recomputes the same comparison over a shorter record using a finer-resolution wave model. **Δ_L2 = 4.48%** of departure-window hours, and **C1 against C3 remains 0.00%**.

The answer to RQ3 is that the measured governance-outcome divergence differs between the two configurations, moving from 5.81% to 4.48% — a spread of approximately 1.3 percentage points — while the intermediate-state control is unchanged at zero. The configurations differ in both wave model and record length; this evaluation does not isolate which difference accounts for the observed spread.

These are two alternative computations over different environmental records. They are not repeated trials, confidence intervals, uncertainty bounds or independent replications, and the spread between them is not an error estimate. The paper reports both values rather than resolving them to a single figure.

What the metric does not capture should be stated alongside what it does. Admissible-set divergence measures whether two governance configurations permit the same set of recommendation types in a given hour. It does not measure whether the recommendations that are permitted are useful, well calibrated, or acted upon, and it does not measure what a human operator would have decided under either configuration. The comparison exercises the classifier and the governance pair over the environmental record; it does not exercise the reasoning engine, which is evaluated separately and on different grounds in Section III.

### D. Summary of results

**TABLE III.** Admissible-set divergence, departure window, small-vessel class. Percentages are of departure-window hours. Quantities marked "not reported" are available under the primary configuration only in the current provenance record.

| Quantity | Primary | Resolution | RQ role |
|---|---|---|---|
| Δ_L2 (C1 against C2) — advisory-scope level | **5.81%** | **4.48%** | RQ2 headline; RQ3 comparison |
| C1 against C3 — intermediate-state control | **0.00%** | **0.00%** | RQ2 control; RQ3 support |
| C0 against C1 — participation gate alone | 42.88% | not reported | RQ2 context |
| C0 against C2 — both governance levels | 48.69% | not reported | RQ2 context |

Two component-level observations bound the interpretation. The wind classifier reached its threshold **twice in 43,848 hours and determined the classification in neither case**; it is neither inactive at this site nor decisive there. The storm-code route of the rainfall classifier was never exercised, because the data provider documents thunderstorm estimation as unavailable for this region, so every rainfall-driven figure is a lower bound by an unknown margin. Which components carry the classification is a property of the site rather than of the specification, and is reported per deployment.
## VI. Discussion and Limitations

This work formalises an existing governance pattern — runtime restriction of advisory types by an externally measured state, established in certified collision-avoidance avionics — as an operational specification over a classified multi-component environmental state, and characterises empirically how often its intermediate advisory-scope level produces a governance outcome distinct from participation-only governance.

**What the formalisation establishes.** A governance contract in which participation and admissible advisory scope are separate mappings over a classified multi-component state, with the classifier total over an observation space rather than over ideal values, with four distinct responses to invalid, absent, stale and unmeasured inputs, and with admissibility supplied to the reasoning layer before inference rather than enforced by filtering its output. The formal properties verify that contract. They are not offered as new results, and the enforcement route — pre-reasoning rule-set supply — is the part that differs from output-filtering approaches such as shielding [5].

**What the empirical characterisation establishes.** That the intermediate advisory-scope level is not vacuous on the evaluated record. It changes the admissible recommendation set in 5.81% of departure-window hours under the primary configuration and 4.48% under the resolution configuration, relative to a participation-only gate. This is a measurement of governance behaviour at one site over the evaluated period.

**Why the zero-divergence control matters.** Without it, the 5.81% figure would be consistent with a simpler explanation: that any three-level scheme differs from a two-level one. The traffic-light comparator shows it does not. Under the evaluated comparator definitions, an intermediate state whose semantics govern supervisory response rather than advisory scope is output-equivalent to a binary gate. The graduation that matters is in the admissible set, not in the number of labels. This is a statement about the comparator structures defined in Section IV and not about three-state designs in general.

**What the results do not establish.** Nothing here measures safety, risk, accident frequency, operator trust, reliance, or decision quality, and no such claim is made. Admissible-set divergence is a property of the governance layer. The formal containment result is a statement about what the system may output, not evidence that outputs are correct or that outcomes improve. No human study was conducted, and the deployment context motivates and instantiates the architecture rather than validating its effects.

**Relation to prior mechanisms.** The mechanism pattern is not new. Certified collision-avoidance equipment already inhibits advisory types progressively as an externally measured state worsens, with nested sets that contract to empty [9], and formal verification of state-conditioned advisory logic has precedent in that same domain [10]. Graduated restriction of the options presented to an operator is long established in human-factors models of automation, assigned at design time per function [11]; runtime adaptation exists in adaptive automation, but conditions predominantly on operator state and governs task allocation [12]; selective prediction governs whether a model predicts at all, conditioned on its own calibrated confidence [13]. Regulatory practice already distinguishes a list of options from a specific directive [14]. What this work adds is the operational treatment combining these elements, not the elements themselves.

**Generalisation boundary.** The construct is generalised beyond a single hazard variable and is domain-reinstantiable at the governance-structure level: a new domain redefines the observed components, the classifier and the admissible sets, and the proved properties hold for any correct instantiation satisfying the stated assumptions. That is a formal statement. **Re-instantiation has been specified and illustrated, not empirically demonstrated across domains**, and no cross-domain implementation or evaluation is reported here.

**Limitations.** The bounded conformance evidence exercises containment on the restrictive side only, with an empty permissive-state rule set and a single generated conclusion type. The freshness parameter is specified but unparameterised; no value is proposed, because no source supports one. Runtime capture of classification provenance is specified but not implemented. Every severity figure is a lower bound: one component is declared unmeasured for the whole record and the storm-code route is never exercised. The two environmental-data configurations are alternative computations, not an uncertainty estimate. Runtime latency and computational overhead on representative target hardware remain open and are not evidenced here; a development-machine reference run is not target-hardware evidence, and no acceptance threshold is established. Results are from one site, one period, and one vessel class.
## VII. Conclusion

Restriction of the advisory types an automated system may present to a human, conditioned on an externally measured state, is established practice in certified avionics. This paper gives that pattern an operational specification for AI decision support: participation and admissible advisory scope as separate mappings over a classified multi-component environmental state, with a classifier total over an observation space, four distinct responses to invalid, absent, stale and unmeasured inputs, declared exclusions that render every severity figure a lower bound, and admissibility supplied to the reasoning layer before inference rather than imposed on its output.

Over five years of retrospective environmental traces, the intermediate advisory-scope level changed the admissible recommendation set in 5.81% of departure-window hours relative to a participation-only gate, and in 4.48% under an alternative environmental-data configuration. A traffic-light comparator lacking advisory-scope differentiation diverged from a binary gate in 0.00% of hours under both configurations, indicating that the measured difference is associated with the scope restriction rather than with the presence of a third governance state.

These are governance-layer measurements at one site. They do not establish safety, effectiveness or decision-quality outcomes. Cross-domain re-instantiation, target-hardware performance and human evaluation remain open.
## References

[1] V. Indykov, D. Strüber, and R. Wohlrab, "Architectural tactics to achieve quality attributes of machine-learning-enabled systems: A systematic literature review," *Journal of Systems and Software*, 2025.

[2] Md. Shamsujjoha, Q. Lu, D. Zhao, and L. Zhu, "Swiss cheese model for AI safety: A taxonomy and reference architecture for multi-layered guardrails of foundation model based agents," in *Proc. IEEE Int. Conf. Software Architecture (ICSA)*, 2025.

[3] D. Dalrymple et al., "Towards guaranteed safe AI: A framework for ensuring robust and reliable AI systems," *arXiv preprint* arXiv:2405.06624, 2024.

[4] N. Flehmig, M. A. Lundteigen, and S. Yin, "Implementing artificial intelligence in safety-critical systems during operation: Challenges and extended framework for a quality assurance process," 2024.

[5] B. Könighofer et al., "Shields for safe reinforcement learning," *Communications of the ACM*, vol. 68, no. 11, pp. 80–90, 2025. doi: 10.1145/3715958


[6] A. Baxi, "The comprehension-gated agent economy: A robustness-first architecture for AI economic agency," *arXiv preprint* arXiv:2603.15639, 2026.

[7] R. Kang, "Governed AI-assisted engineering: Graduated human oversight for agentic code generation in regulated domains," *arXiv preprint* arXiv:2606.22484v2, 2026.

[8] National Institute of Standards and Technology, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1. Gaithersburg, MD: NIST, Jan. 2023. doi: 10.6028/NIST.AI.100-1

[9] Federal Aviation Administration, *Airworthiness Approval of Traffic Alert and Collision Avoidance Systems (TCAS II), Versions 7.0 & 7.1 and Associated Mode S Transponders*, Advisory Circular 20-151C. Washington, DC: U.S. Dept. of Transportation, Jul. 21, 2017.

[10] R. Cleaveland, S. Mitsch, and A. Platzer, "Formally verified next-generation airborne collision avoidance games in ACAS X," *ACM Transactions on Embedded Computing Systems*, vol. 22, no. 1, art. 10, pp. 1–30, 2023. doi: 10.1145/3544970

[11] R. Parasuraman, T. B. Sheridan, and C. D. Wickens, "A model for types and levels of human interaction with automation," *IEEE Transactions on Systems, Man, and Cybernetics — Part A: Systems and Humans*, vol. 30, no. 3, pp. 286–297, 2000. doi: 10.1109/3468.844354

[12] M. Bernabei and F. Costantino, "Adaptive automation: Status of research and future challenges," *Robotics and Computer-Integrated Manufacturing*, vol. 88, art. 102724, 2024. doi: 10.1016/j.rcim.2024.102724

[13] H. Kwon and D.-J. Kim, "Conformal selective prediction with cost aware deferral for safe clinical triage under distribution shift," *Scientific Reports*, vol. 16, art. 10016, 2026. doi: 10.1038/s41598-026-40637-w

[14] U.S. Food and Drug Administration, *Clinical Decision Support Software: Guidance for Industry and Food and Drug Administration Staff*. Silver Spring, MD: FDA, Jan. 29, 2026. Docket FDA-2017-D-6569.

[15] National Oceanic and Atmospheric Administration, Global Monitoring Laboratory, *General Solar Position Calculations*. Boulder, CO: NOAA GML.

[16] U.S. Naval Observatory, Astronomical Applications Department, *Astronomical Applications API v4.0.1*, service `rstt/oneday`. Washington, DC: USNO.

[17] International Maritime Organization, *Convention on the International Regulations for Preventing Collisions at Sea, 1972 (COLREGs), as amended*, Rule 20(b). London: IMO.

[18] O. Yaakob, F. E. Hashim, M. R. Jalal, and M. A. Mustapa, "Stability, seakeeping and safety assessment of small fishing boats operating in southern coast of Peninsular Malaysia," 2015.

[19] C.-H. Jeong and N. Im, "Proposal of restrictions on the departure of Korea small fishing vessel according to wave height," *Journal of Marine Science and Engineering*, 2023.
