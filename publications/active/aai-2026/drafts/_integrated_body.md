# From Declared Risk Levels to Admissible Recommendations: Measuring the Operational Effect of AI Governance

# I. Introduction

Systems supporting consequential decisions are increasingly placed under explicit operating controls, commonly described by the risk levels they declare. A declared level constrains a system only if it changes the set of actions the system is permitted to take, and the presence of the level in a specification does not by itself establish that it does. Neither does it establish how often the constraint is encountered once the system runs against real conditions. Risk-management guidance directs that AI risks and related impacts be analysed, assessed, benchmarked and monitored, and that systems be tested before deployment and regularly while in operation [NIST]. These properties can therefore be treated as measurement questions rather than assumed from the design specification.

Mechanisms for restricting what a system may do are established. Run-time assurance is standardised practice in aviation, where an independently assured architecture bounds the behaviour of a component containing complex functions [ASTM]. In safe reinforcement learning, a shield may compute the set of safe actions and remove the unsafe ones before the agent selects, rather than substituting a corrected action after selection [ALSHIEKH]. Certified collision-avoidance avionics inhibit advisory categories progressively as an externally measured state worsens, while leaving final authority with the crew [FAA]. The canonical model of human interaction with automation already describes graduated contraction of the alternatives presented to a person, from offering a complete set, to narrowing it, to suggesting one [PARASURAMAN]. This paper contributes none of these mechanisms.

That model also holds that automation cannot be assigned a single overall level, because a level is always stated relative to a specific function [PARASURAMAN]. What separates one level from another is the allocation it changes, not its position in a taxonomy. Applied to a declared risk level, this yields a question that can be checked rather than assumed: does the level alter the set of recommendations the system may produce, or does it appear only in the specification? A level that leaves the permitted set unchanged describes the design without constraining it.

Measuring how often such a boundary is encountered is not an unexplored activity, and Section II identifies work that performs parts of it. The narrower case concerns an intermediate level that contracts the permitted set while the system continues to operate, examined against a configuration that gates participation alone. Within the reviewed literature, no empirical characterisation was identified of how often an intermediate advisory-scope level changes the admissible recommendation set relative to a participation-only gate when replayed over a multi-year environmental record. That statement is scoped to the literature examined here, and to the combination of properties just described, rather than being a claim about the field as a whole.

This study addresses one question. **RQ1.** Over a multi-year environmental record for one deployment site, how often does an intermediate advisory-scope governance level change the admissible recommendation set relative to a participation-only gate, and how sensitive is that frequency to defensible threshold, vessel-class and denominator-policy configurations? The approach has three parts. A specification-level criterion states the condition under which a declared level changes system behaviour. Four configurations, C0 to C3, are then defined so that a participation-only gate and an intermediate-scope configuration differ at one state only, which allows the intermediate level to be isolated. The configurations are then replayed over five years of hourly environmental records for a single coastal-fisheries deployment site, and the resulting frequency is examined across the defensible threshold, vessel-class and denominator-policy settings that the evaluation permits.

The contribution is a measurement assembly and its interpretation rather than any of its constituent techniques. It comprises the isolation of an intermediate advisory-scope level against a participation-only configuration differing from it at one state; the interpretation of the resulting quantity as the frequency with which the active contraction binds, under the specified comparator construction; the sensitivity of that binding rate to the threshold that governs it; and the attribution of which state component produces the intermediate classification in the evaluated record. The study does not establish improved safety, improved decision quality, the optimality of the restricted recommendation set, effective human oversight, or generalisation beyond the evaluated site and vessel class. Each of these lies outside what the evaluation can support.

# II. Background and Positioning

Responsible AI has produced a substantial body of frameworks, principles and risk-management guidance. Reviews of this literature report that published governance frameworks frequently lack real-world implementation detail and validation, and that few studies specify together who governs, what is governed, when, and how [AI-GOV-SLR]. Risk-management guidance addresses part of this by directing that AI risks and related impacts be analysed, assessed, benchmarked and monitored, and that systems be tested before deployment and regularly while in operation [NIST]. Operational measurement of deployed controls is therefore an established activity rather than an absent one. The question taken up here is narrower: whether one particular declared level has an observable effect on the set of recommendations a system may produce.

The mechanisms by which available actions can be restricted at run time are well developed, and they appear in both standardised and research settings. ASTM F3269 standardises run-time assurance for aircraft systems containing complex functions, in which an independently assured architecture bounds the behaviour of the component it supervises [ASTM]. Work on safe reinforcement learning distinguishes a shield that computes the safe actions and removes the unsafe ones before the agent selects from one that substitutes a corrected action afterwards [ALSHIEKH]. Certified collision-avoidance avionics inhibit advisory categories progressively as an externally measured state worsens, and state explicitly that the crew retains authority [FAA]. Together these establish that state-conditioned restriction is not itself the open contribution. The question addressed here is not whether a system can restrict its available actions, but how the operational effect of one declared level is measured.

The individuation of levels has a longer history in human-automation research. The canonical model holds that a level of automation is always stated relative to a specific function, and it describes graduated restriction of what is offered to a person across adjacent levels: a complete set of alternatives, a narrowed selection, or a single suggestion [PARASURAMAN]. That model is design-time and defines no run-time state variable. It nonetheless supplies the grounding for examining a declared level through the behaviour it permits or suppresses, rather than through its position in a scheme, which is the criterion stated in Section III.

Three recent studies each perform part of the measurement assembled here. Aarab specifies graduated run-time autonomy modes in which the permitted execution directives contract as severity rises while operation continues [AARAB]; the reported directive-frequency simulation is conducted under the permissive mode rather than as a comparison of graduated configurations. Miller evaluates alternative enforcement operators, including an ungoverned baseline, approval-only gating and projection-based repair, through systematic ablation [MILLER]; those configurations compare operators rather than graduated risk levels, and do not measure how often an intermediate contraction binds. Kim et al. quantify the burden of an intermediate zone requiring mandatory human review, and characterise it across reliability targets on real clinical data [KIM]; that zone withdraws automated action rather than retaining an active contracted recommendation set. Within the reviewed literature, these works do not combine active intermediate scope contraction, a participation-only comparator, marginal isolation, and binding-frequency measurement.

# III. Governance Contract, Criterion and Metric

Measuring that combination requires the governed object to be stated explicitly. We take it to be *A*<sub>AI</sub>(*S*), the set of recommendation types admissible when the classified operating state is *S*. Each evaluated hour is assigned one of three states, SAFE, CAUTION or UNSAFE, and FULL denotes the unrestricted recommendation set {Go, Delay, DepartureTime, Duration}. Table I states the contract. The admissible sets contract monotonically across the three states by construction. Participation gating is the special case in which the admissible set is empty, and so requires no separate formalism here.

*A*<sub>AI</sub>(CAUTION) = {Go, Delay} is a researcher-defined design choice used to instantiate a strict intermediate contraction for the evaluation. It is not empirically validated, shown correct, shown optimal, or established as safer or more beneficial. As Section III-E makes explicit, the measurement reported in this paper does not validate it.

**TABLE I**
*Admissible recommendation set by safety state. FULL = {Go, Delay, DepartureTime, Duration}.*

| State | *G* | *A*<sub>AI</sub>(*S*) |
|---|---|---|
| SAFE | 1 | FULL |
| CAUTION | 1 | {Go, Delay} |
| UNSAFE | 0 | ∅ |

*G* is determined by emptiness of *A*<sub>AI</sub> and is shown for readability only. *A*<sub>AI</sub>(CAUTION) = {Go, Delay} is researcher-defined; it is not empirically validated, shown optimal, or established as safer.

Following the functional interpretation of levels set out above, we evaluate a declared state through the recommendation set it permits.

**Criterion.** A declared risk level changes governance behaviour only if it changes the admissible recommendation set. Two configurations that assign identical admissible sets at every state denote the same governance function, irrespective of how many states each declares.

This is an operational measurement rule rather than a result. It restates, for a declared state, the position already established in the levels-of-automation literature that a level is meaningful through the function allocation it changes [PARASURAMAN].

Table II defines four configurations over the same classifier. C0 applies no restriction. C1 gates participation alone. C2 is the evaluated intermediate-scope configuration. C3 declares three states without contracting scope at the intermediate one.

C1 and C2 are identical at SAFE and identical at UNSAFE, and differ only at CAUTION, where C1 admits FULL and C2 admits a strict subset of FULL. Any difference between them therefore arises exactly where the intermediate state contracts the admissible set, which supplies the isolation structure used below. Ablation across governance configurations is established practice [MILLER]; what it is used for here is the isolation of one declared level.

C1 and C3 assign identical admissible sets at every state. Under the criterion they denote the same governance function, and their pairwise difference is zero by construction. The replayed value reported later is an executable conformance check on the implementation rather than an empirical finding, and it is not evidence that three-state designs are ineffective.

**TABLE II**
*Four governance configurations. C1 and C3 assign identical admissible sets at every state and therefore denote the same governance function.*

| Configuration | *A*<sub>AI</sub>(SAFE) | *A*<sub>AI</sub>(CAUTION) | *A*<sub>AI</sub>(UNSAFE) |
|---|---|---|---|
| C0 Ungated | FULL | FULL | FULL |
| C1 Participation-only | FULL | FULL | ∅ |
| C2 Evaluated intermediate-scope | FULL | {Go, Delay} | ∅ |
| C3 Three-state topology | FULL | FULL | ∅ |

C3 ports the governance topology of [FLEHMIG] onto an environmental conditioning variable. [FLEHMIG] condition on AI degradation rather than environmental state. C3 is not a reproduction or evaluation of their system and does not imply that their framework is deficient.

Let *N*<sub>eval</sub> be the number of evaluated departure-window hours and *N*<sub>restricted</sub> the number of those hours in which one configuration admits a strictly smaller set than another. The difference rate between two configurations is

Δ = (*N*<sub>restricted</sub> / *N*<sub>eval</sub>) × 100%.

The isolated quantity is

Δ<sub>L2</sub> = (C0↔C2) − (C0↔C1).

Here C0↔C1 captures participation gating alone and C0↔C2 captures participation gating together with the intermediate contraction, so their difference isolates the increment associated with the intermediate level under this comparator construction. A direct C1↔C2 comparison is computed as an implementation cross-check.

The identity governing interpretation follows from the mappings rather than from the data. C1 and C2 agree at SAFE and at UNSAFE and differ at CAUTION, where C2 admits a strict subset of FULL. The two configurations therefore differ on exactly the CAUTION hours, so that

Δ<sub>L2</sub> ≡ *P*(*S* = CAUTION)

for the evaluated mappings. This is a metric-interpretation identity, not a result.

Two consequences follow. One is that the value of Δ<sub>L2</sub> is invariant to the content of *A*<sub>AI</sub>(CAUTION), provided that set remains a strict subset of FULL: replacing one strict subset with another leaves the binding frequency unchanged when the state classification is unchanged. The other is that Δ<sub>L2</sub> measures how often the intermediate restriction binds, not how much the recommendation set contracts. It does not indicate whether {Go, Delay} is correct or optimal, whether the restriction improves safety or decision quality, or whether human oversight is effective.

Because the identity holds, the CAUTION base rate yields the same number and the comparator ladder is not required to compute it. The ladder serves a different purpose. It separates participation gating from the intermediate contraction, it makes the isolation structure explicit, it establishes the identity rather than assuming it, and it supplies the cross-check noted above.

# IV. Evaluation Design

The replay covers one deployment site, Kota Kinabalu, Sabah, a low-resource coastal-fisheries setting, with a small-vessel baseline under 10 GRT.

Two environmental-data configurations are evaluated. The PRIMARY configuration covers January 2020 to December 2024, comprising 43,848 hourly records with wave data from ERA5-Ocean at approximately 50 km resolution, giving a departure-window denominator of 9,135 hours. The RESOLUTION configuration covers October 2021 to December 2024, comprising 28,501 hourly records with wave data from MFWAM at approximately 8 km resolution, giving a denominator of 5,935 hours. Records were retrieved through the Open-Meteo archive [OPEN-METEO], [ERA5].

The evaluation window is 05:00–09:00, which defines *N*<sub>eval</sub>. This window is an evaluation-policy choice rather than an observed departure period, and other denominators are defensible.

Each hour is assigned a state using the maximum severity among the available component classifications, covering wind, rainfall, marine warning, ocean state and time. Vessel class parameterises the ocean-state component rather than contributing an independent severity term.

Threshold provenance is separated from design choice. The wind boundary follows Malaysian Meteorological Department strong-wind criteria [MET-WIND], and the rainfall UNSAFE boundary follows the same department's thunderstorm criteria [MET-THUNDERSTORM]. The ocean-state boundary for the small-vessel class follows the operational ceiling reported by [YAAKOB], and the day boundary follows COLREGs Rule 20(b) [IMO-COLREG]. The rainfall CAUTION boundary is source-supported through the DID light-rainfall limit [DID-RAINFALL] but is not a Meteorological Department threshold, since no criterion is published below the thunderstorm level. Source provenance indicates where a boundary comes from; it does not establish that it is optimal. Researcher-defined choices are the three-state cardinality, *A*<sub>AI</sub>(CAUTION), the policy treating non-daylight hours as UNSAFE, the evaluation window, and the declared exclusion described next.

The marine-warning component has no usable historical archive for the replay period. It is handled by declared exclusion rather than imputation, and held at its least-severe value throughout. Because the classifier aggregates by maximum severity, a non-least-severe marine-warning observation could only maintain or raise the resulting severity. Intermediate-or-higher state activation frequencies reported later are therefore interpreted as lower bounds under this exclusion, which is a qualification on the measurement rather than a method.

Classification remains total under the exclusion: every evaluated hour receives a state from the available component rules and the declared treatment of the excluded component.

The replay is a deterministic census of all evaluated departure-window hours in the specified records. No sampling inference is performed, and no p-values, confidence intervals or significance claims apply. Ranges reported later are deterministic configuration ranges rather than confidence intervals. Implementation checks confirmed the configured admissible-set mappings were applied as specified.

# V. Results and Discussion

## A. Binding Frequency and Comparator Decomposition

The PRIMARY replay gave Δ<sub>L2</sub> = 5.81% and the RESOLUTION configuration gave 4.48%. These are proportions of evaluated departure-window hours in which the intermediate advisory-scope restriction binds. As established in Section III, this equals CAUTION occupancy under these mappings.

The PRIMARY comparator decomposition separates the two levels. C0↔C1 gave 42.88%, the frequency associated with participation gating alone, and C0↔C2 gave 48.69%, the frequency associated with participation gating together with the intermediate contraction. The difference, 48.69 − 42.88 = 5.81 percentage points, isolates the incremental binding frequency associated with the intermediate level under the comparator construction. The direct C1↔C2 comparison returned the same value. The RESOLUTION pairwise components are not reported because their provenance is incomplete; Δ<sub>L2</sub> is unaffected.

The two configurations differ in both wave source and record period, and the gap between 5.81% and 4.48% indicates that the measured binding frequency depends on the environmental-data configuration used for replay. Neither value is treated here as more accurate than the other, and the difference is not attributed to spatial resolution alone.

Both configurations returned C1↔C3 = 0.00%. This is the entailed result rather than an empirical finding: C1 and C3 assign identical admissible sets at every state, so the replay provides a conformance check on the configured mappings. It indicates that C1 and C3 are equivalent as governance functions under the admissible-set criterion, and nothing about whether three-state designs are useful in general.

**TABLE III**
*Binding frequency, comparator decomposition and robustness results.*

| Metric | PRIMARY | RESOLUTION |
|---|---|---|
| Period | 2020–2024 | 2021-10–2024 |
| Departure-window hours | 9,135 | 5,935 |
| C0↔C1 | 42.88% | — |
| C0↔C2 | 48.69% | — |
| Δ<sub>L2</sub> | 5.81% | 4.48% |
| C1↔C3 | 0.00% | 0.00% |
| Sourced-threshold envelope | 5.67–9.56% | 4.26–6.64% |
| Small-vessel baseline | <10 GRT | <10 GRT |

— indicates pairwise resolution components withheld because provenance is incomplete; Δ<sub>L2</sub> is unaffected. C1↔C3 = 0.00% is entailed by the mappings and is reported as an implementation conformance check. The sourced-threshold envelope is a deterministic configuration range, not a confidence interval.

## B. Threshold Sensitivity

Across externally sourced threshold configurations for the small-vessel baseline, Δ<sub>L2</sub> spans 5.67–9.56% in PRIMARY and 4.26–6.64% in RESOLUTION. These are deterministic configuration ranges obtained by replaying defensible threshold settings, not confidence intervals or uncertainty estimates. The measured binding frequency is therefore not a threshold-invariant property of the site.

Provenance does not by itself remove designer interpretation. The small-vessel wave source supports two defensible readings of the UNSAFE boundary, an operational ceiling and a failure point, which give 5.81% and 9.22% respectively. Both are traceable to the same source [YAAKOB], and neither is selected here as correct.

A separate perturbation of the wave CAUTION onset by ±0.25 m moves Δ<sub>L2</sub> across 2.54–14.75%. This is a controlled movement of one boundary rather than a survey of sourced configurations, and the two ranges answer different questions. Over the evaluated perturbation the sensitivity is approximately −1.4 percentage points per 0.05 m, which describes how the measurement responds across the evaluated range rather than a causal derivative.

Other components contribute far less. Varying the rainfall CAUTION boundary moves Δ<sub>L2</sub> by 0.48 percentage points in PRIMARY and 0.78 in RESOLUTION, so the non-MET boundary identified in Section IV had comparatively little influence on the result in this evaluation. The wind boundary is a structural zero across the evaluated range *W*<sub>C</sub> = 18–25 kn: no setting within that range altered the classification of any evaluated hour.

**FIGURE 1** *(placeholder — plot data not yet exported)*
*Δ<sub>L2</sub> against the wave CAUTION onset for the PRIMARY and RESOLUTION configurations. The sourced-threshold region is marked as a shaded band, and the operational-ceiling reading used throughout is marked on the PRIMARY trace.*

## C. Component Attribution and Scope Dependence

Within the PRIMARY departure window, 531 hours were classified CAUTION, and attribution across the component classifiers is uneven. The ocean-state component accounted for 518 of those 531 hours, or 97.6%, and the rainfall component for the remaining 13, or 2.4%. These are attributions of CAUTION classification, not of incidents or unsafe outcomes, none of which is observed here.

The three remaining components register zero, for three different reasons, and the distinction matters. No PRIMARY CAUTION hour was attributed to wind, which is an empirical negative finding for the evaluated record and is separate from the structural zero reported for the wind threshold range above. The time component emits no CAUTION by construction, so its zero is definitional. The marine-warning component is structurally excluded, and its zero reflects unavailability rather than evidence that marine warnings never bind.

The measured frequency also depends on configuration choices fixed in Section IV. Under the medium- and large-vessel threshold configurations the PRIMARY value falls to 1.96% and 1.26% respectively, and to 0.66% and 0.37% in RESOLUTION. Replacing the departure-window denominator with a daylight-only denominator raises it to 9.59% in PRIMARY and 7.40% in RESOLUTION. Vessel class and denominator are evaluation-policy settings, and neither variant is presented as more appropriate than the departure-window baseline. Because the marine-warning component was held at its least-severe value and classification aggregates by maximum severity, the activation frequencies reported here are interpreted as lower bounds under that exclusion.

RQ1 can now be answered. For the PRIMARY configuration at the evaluated site and small-vessel baseline, the intermediate advisory-scope contraction binds in 5.81% of departure-window hours, and in 4.48% under the RESOLUTION configuration. That frequency is conditional rather than fixed: it spans 5.67–9.56% across sourced threshold configurations, moves across 2.54–14.75% under a ±0.25 m wave-onset perturbation, falls to 1.96% and 1.26% for the medium and large vessel classes, and rises to 9.59% under a daylight-only denominator. The intermediate level therefore measurably changes the admissible recommendation set under the evaluated contract, while the frequency of that change is conditional on threshold, vessel-class and denominator choices.

The interpretation this supports is narrow. A declared intermediate level can be audited through whether, and how often, it changes the admissible recommendation set, and for this contract it does bind in historical replay. The resulting rate cannot be read without also examining threshold provenance, component attribution, vessel-class assumptions, denominator policy and the treatment of the excluded component. The results do not establish that the restriction is correct, optimal, safer or beneficial, that decision quality or oversight improved, or that these figures extend to other sites, vessel classes or periods.

# VI. Limitations and Conclusion

The replay concerns one deployment site and should not be read as a population estimate for other locations. The activation frequency is conditional on threshold interpretation, with the wave CAUTION onset producing the largest sensitivity. Several governance choices remain researcher-defined rather than empirically validated: the three-state cardinality, the evaluation policies fixed in Section IV, and the admissible set A<sub>AI</sub>(CAUTION) = {Go, Delay}. The evaluation measures how often that restriction binds. It does not establish that {Go, Delay} is the correct, optimal or safer set at CAUTION, and the reported measure is invariant to its content. The marine-warning component has no usable archive for the replay period and was held at its least-severe value, so activation frequencies are interpreted as lower bounds.

The study characterises governance activation; it does not validate it. No incident or outcome record exists for the site, so activation is not linked to unsafe departures or avoided harm. No generated advice is evaluated: the metric ranges over admissible recommendation types, not over the correctness, quality or usefulness of any recommendation. No user study has been conducted, so interpretation, acceptance, trust, behavioural response and human oversight in use remain untested. The replay is a deterministic census rather than a sample, so no statistical inference applies, and the vessel-class variants are configuration checks, not evidence of generalisation across classes, sites or periods. Field work should test the threshold mappings and the restricted set with domain stakeholders, examine how users interpret the advice, and relate activation to operational outcomes before any safety or generalisation claim is made.

The question addressed was whether a declared intermediate risk level changes what an advisory system is permitted to recommend, and how often. Stating a criterion on admissible sets and isolating the intermediate level with a four-configuration comparator, the contracting level was reached in 5.81% of PRIMARY departure-window hours and 4.48% under RESOLUTION: a lower bound, within a 5.67–9.56% sourced envelope, 97.6% attributable to one component, and falling to 1.96% and 1.26% for larger vessel classes. These are conditional measurements rather than stable site properties; the contribution is the assembly that makes such a figure interpretable, together with the criterion. For Responsible AI governance, the implication is that a declared risk level can be examined not only by its label, but by the admissible recommendations it changes and the conditions under which that change binds.
