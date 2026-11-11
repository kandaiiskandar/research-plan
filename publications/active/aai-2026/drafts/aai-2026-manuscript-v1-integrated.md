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

---
---

# PART 2 — PHASE 5 INTEGRATION AUDIT

## Phase 5 Integration Audit

### 1. Integration Integrity

**SUBSTANTIVE BODY CHANGES DURING INTEGRATION: 0**

Sections I–VI were extracted programmatically from the four approved phase files, cut at the workflow separator preceding each file's audit block, and concatenated in order. No sentence was edited, reordered, added or removed.

Mechanical changes applied, all within the authorised list:

- Removed the Phase 1 draft-status blockquote (venue, format and citation-key note) — a workflow note, not manuscript content.
- Removed all Drafting Audits, Micro-Revision Audits, Strict Diff Results, Final Logical Checks, Carried-Forward blocks, Declared-Adjustment notes and PHASE STATUS lines.
- Normalised heading depth. The phase files disagreed: Phase 1 used `##` for Sections I–II while Phases 2–4 used `#` for Sections III–VI. All six section headings are now `#`; Section V's three subsections remain `##`. Numbering I–VI, Tables I–III and Figure 1 are unchanged.
- Collapsed duplicated horizontal rules and runs of blank lines produced by concatenation.

Tables I, II and III and the Figure 1 placeholder are byte-identical to their approved phase files, including all table notes.

### 2. Research-Chain Consistency

| Transition | Verdict | Evidence in the integrated body |
|---|---|---|
| Problem → Gap | **PASS** | I-P1 states the problem as a measurement question; I-P4 narrows to the intermediate-versus-participation-only case and states the absence, scoped *"Within the reviewed literature"* and *"to the literature examined here"* |
| Gap → RQ | **PASS** | I-P5's RQ1 is verbatim from the patched chain and names the same three sensitivity dimensions the gap implies |
| RQ → Method | **PASS** | III defines A<sub>AI</sub>(*S*), the criterion, C0–C3, Δ and Δ<sub>L2</sub>; C1/C2 differ only at CAUTION, which is the isolation the RQ requires |
| Method → Results | **PASS** | V-A reports Δ<sub>L2</sub> and the decomposition using the Section III construction; V-B and V-C answer the sensitivity half of RQ1 |
| Results → Conclusion | **PASS** | VI restates the question, the measured frequency and its conditionality without introducing a new claim |

The II → III transition survives concatenation: Section II closes on *"these works do not combine active intermediate scope contraction, a participation-only comparator, marginal isolation, and binding-frequency measurement"* and Section III opens *"Measuring that combination requires…"*. The referent is intact.

### 3. Contribution Boundary

- Architecture novelty: **NO**
- Mechanism novelty: **NO**
- Generic technique novelty: **NO**
- Measurement-assembly contribution preserved: **YES**
- Criterion status preserved: **YES**

All six occurrences of `contribut*` were inspected. Two are concessions (*"This paper contributes none of these mechanisms"*, *"state-conditioned restriction is not itself the open contribution"*), two are the contribution statements in I-P6 and VI-P3, and two are ordinary verbs about severity terms and component influence. No occurrence of *novel*, *novelty*, *first*, *unique* or *unprecedented* appears anywhere in the body. *Distinctive* does not appear. *Operational effect* appears twice, both in the title and in non-claiming positions.

### 4. Metric and Comparator Consistency

| Check | Result |
|---|---|
| C0–C3 mappings correct | **YES** — Table II rows match FULL/FULL/FULL · FULL/FULL/∅ · FULL/{Go, Delay}/∅ · FULL/FULL/∅ |
| C1/C2 isolation correct | **YES** — identical at SAFE and UNSAFE, differ only at CAUTION |
| C1/C3 equivalence correct | **YES** — identical admissible sets at every state, same governance function under the criterion |
| C1↔C3 epistemic status correct | **YES** — *"zero by construction"* (III), *"the entailed result rather than an empirical finding"* and *"implementation conformance check"* (V), with the explicit guard that it is not evidence about three-state designs |
| Δ<sub>L2</sub> definition correct | **YES** — (C0↔C2) − (C0↔C1) |
| Δ<sub>L2</sub> ≡ *P*(*S* = CAUTION) preserved | **YES** — stated in Section III before any number, labelled *"a metric-interpretation identity, not a result"* |
| Comparator ladder not claimed necessary merely to compute 5.81% | **YES** — Section III states outright *"the CAUTION base rate yields the same number and the comparator ladder is not required to compute it"*, then gives the ladder's four actual purposes |

### 5. Numerical Ledger

| Quantity | Expected | Occurrences consistent? | Notes |
|---|---|---|---|
| PRIMARY hourly records | 43,848 | ✅ 1× | Section IV |
| PRIMARY period | Jan 2020 – Dec 2024 | ✅ | IV prose; Table III shows 2020–2024 |
| PRIMARY denominator | 9,135 | ✅ 2× | IV prose, Table III |
| PRIMARY Δ<sub>L2</sub> | 5.81% | ✅ 6× | V-A, V-B, V-C ×2, Table III, VI |
| PRIMARY C0↔C1 | 42.88% | ✅ 2× | V-A prose, Table III |
| PRIMARY C0↔C2 | 48.69% | ✅ 2× | V-A prose, Table III |
| Decomposition | 48.69 − 42.88 = 5.81 pp | ✅ | Percentage points, not a relative increase |
| RESOLUTION hourly records | 28,501 | ✅ 1× | Section IV |
| RESOLUTION period | Oct 2021 – Dec 2024 | ✅ | IV prose; Table III shows 2021-10–2024 |
| RESOLUTION denominator | 5,935 | ✅ 2× | IV prose, Table III |
| RESOLUTION Δ<sub>L2</sub> | 4.48% | ✅ 5× | |
| C1↔C3 | 0.00% both | ✅ 4× | |
| RESOLUTION C0↔C1 / C0↔C2 | **WITHHELD** | ✅ | Em dashes in Table III with the provenance note; no value stated, inferred or back-solved anywhere |

No numeral appears in the body that is not traceable to the locked chain §§11–12 or to Section IV's dataset facts.

### 6. Epistemic-Status Ledger

| Item | Required status | Manuscript status | Verdict |
|---|---|---|---|
| C1↔C3 = 0.00% | Entailed / conformance | Entailed by construction; executable conformance check; explicitly not evidence about three-state designs | **PASS** |
| *g*<sub>o</sub> 518/531 = 97.6% | Empirical dominant attribution | *"attributions of CAUTION classification, not of incidents or unsafe outcomes"* | **PASS** |
| *g*<sub>r</sub> 13/531 = 2.4% | Empirical attribution | Same sentence | **PASS** |
| *g*<sub>w</sub> = 0 | Empirical negative finding | Stated as such, and explicitly *"separate from the structural zero reported for the wind threshold range above"* | **PASS** |
| *g*<sub>t</sub> = 0 | Definitional | *"emits no CAUTION by construction, so its zero is definitional"* | **PASS** |
| *g*<sub>m</sub> | Structural exclusion | *"reflects unavailability rather than evidence that marine warnings never bind"* | **PASS** |
| Sourced-threshold envelope | Deterministic configuration range | *"not confidence intervals or uncertainty estimates"*, repeated in the Table III note | **PASS** |
| Wave perturbation ±0.25 m | Controlled perturbation, distinct from the envelope | *"the two ranges answer different questions"*; −1.4 pp per 0.05 m marked *"rather than a causal derivative"* | **PASS** |
| Vessel variants | Deterministic configuration variants | *"evaluation-policy settings"*; VI calls them *"configuration checks, not evidence of generalisation"* | **PASS** |
| Daylight denominator | Policy dependence | *"neither variant is presented as more appropriate"* | **PASS** |
| Lower bound | Measurement qualification | Scoped to *"intermediate-or-higher state activation frequencies"* in IV and to *"the activation frequencies reported here"* in V; not broadened to all results | **PASS** |

**AUDIT 13 (two wind zeros): PASS.** The threshold structural zero over *W*<sub>C</sub> = 18–25 kn and the attribution zero *g*<sub>w</sub> = 0 are in different subsections and the second explicitly names the first to keep them apart.

**AUDIT 16: PASS.** The lower bound is never broadened to *"all results are lower bounds"*. Partial identification, Manski and confidence bounds are absent.

**AUDIT 17 (threshold provenance): PASS.** Section IV keeps all six distinctions, including *"is not a Meteorological Department threshold, since no criterion is published below the thunderstorm level"* and *"Source provenance indicates where a boundary comes from; it does not establish that it is optimal."* No later section collapses source-supported into officially mandated.

**AUDIT 18 (data configuration): PASS.** *"The two configurations differ in both wave source and record period… Neither value is treated here as more accurate than the other, and the difference is not attributed to spatial resolution alone."*

### 7. Claim-Safety Audit

- Safety outcome claim: **NONE**
- Generated-advice validation: **NONE**
- Human-validation claim: **NONE**
- Optimality claim: **NONE**
- Generalisation claim: **NONE**
- Statistical inference: **NONE**

Every occurrence of *safety*, *safer*, *effective*, *improves* and *validate* was inspected in context. All fall into three legitimate classes: explicit non-claims (I-P6, III, V-C, VI), contextual terminology (*"safety state"*, *"safe reinforcement learning"*, *"safe actions"*), or negations (*"not evidence that three-state designs are ineffective"*). *Statistically significant*, *p-value*, *confidence interval*, *sampling error* and *population estimate* appear only inside sentences that deny their applicability, which the brief permits.

**AUDIT 5 (G vs A<sub>AI</sub>): PASS.** The symbol *G* appears only in Table I and its note, inside Section III. Sections IV–VI contain no occurrence of *G* at all, so the two are never treated as independently measured variables. Participation gating is defined once as the empty-admissible-set case and used consistently.

**AUDIT 6 (criterion status): PASS.** *Theorem*, *proposition*, *proof*, *formal guarantee*, *universal law* and *validated principle* are absent. Section III labels it *"an operational measurement rule rather than a result"*; Section VI refers to *"a criterion on admissible sets"*, which does not broaden it.

**AUDIT 9 (metric semantics): PASS.** *"Δ<sub>L2</sub> measures how often the intermediate restriction binds, not how much the recommendation set contracts"* is stated in Section III, and the invariance consequence is stated immediately before it. No later section treats 5.81% as a magnitude.

**AUDIT 24 (Responsible AI): PASS.** The connection runs through operational auditability only. Fairness, explainability, transparency, trustworthiness and human-centredness are absent as claims.

### 8. Terminology Audit

**NO MATERIAL TERMINOLOGY DRIFT.**

The state names, FULL, A<sub>AI</sub>(*S*), PRIMARY, RESOLUTION, *departure-window hours*, *sourced-threshold envelope*, *deterministic configuration range*, *lower bound* and *researcher-defined* are used consistently throughout. *Action set*, *permission set* and *recommendation scope* do not appear at all. *Admissible set* is used as a short form of *admissible recommendation set* within sections that have already introduced the full term, which does not change the object. *Binding frequency* and *activation frequency* both appear; they denote the same quantity and each is anchored to Δ<sub>L2</sub> where introduced, so the variation is legible rather than confusing.

One observation, not a defect: Section I-P4's gap sentence reads *"an intermediate advisory-scope level"* where the patched chain's Gap B reads *"an intermediate advisory-scope governance level"*. The technical object is unchanged and RQ1 in the next paragraph carries the full phrase. No action required.

### 9. Citation-Key Audit

Seventeen distinct keys appear. The Citation & Evidence Lock v2 §11 REQUIRED list also contains seventeen entries, and the sets correspond one to one.

| Key | Uses | Status |
|---|---|---|
| [AARAB] | 1 | **LOCKED** — used only for graduated runtime contraction; never *"Aarab et al."* |
| [AI-GOV-SLR] | 1 | **LOCKED (author list open)** — Lock v2 §16 item 2, author list still to be read from the corpus note |
| [ALSHIEKH] | 2 | **LOCKED** — preemptive removal before selection; *"pre-inference"* absent |
| [ASTM] | 2 | **LOCKED** — title-and-scope only; no clause number appears, per Lock v2 §16 item 4 |
| [DID-RAINFALL] | 1 | **LOCKED** |
| [ERA5] | 1 | **LOCKED** |
| [FAA] | 2 | **LOCKED** |
| [FLEHMIG] | 2 | **LOCKED** — with the non-deficiency qualification attached |
| [IMO-COLREG] | 1 | **LOCKED** |
| [KIM] | 1 | **LOCKED** — abstention framing preserved; no shared-estimand implication |
| [MET-THUNDERSTORM] | 1 | **LOCKED** |
| [MET-WIND] | 1 | **LOCKED** |
| [MILLER] | 2 | **LOCKED** — ablation conceded as established practice; no compliance-improvement implication |
| [NIST] | 2 | **LOCKED** |
| [OPEN-METEO] | 1 | **LOCKED** |
| [PARASURAMAN] | 4 | **LOCKED** |
| [YAAKOB] | 2 | **LOCKED** — carries both the 5.81% and 9.22% readings |

**AUDIT 28: PASS.** The three near-neighbour concessions sit in Section II Cluster D, each stated within its verified limit, and the paragraph closes with the scoped residue sentence *"Within the reviewed literature, these works do not combine…"*. No absence claim about them is broadened elsewhere.

**MFWAM is named in Section IV as a wave data source with no citation key.** That is the open resolution task, not a key error.

**AUDIT 29 (IPoSCI): PASS.** The string does not appear. *Previously published*, *previously reported* and any publication-status claim are absent.

### 10. Duplication Audit

| # | Location | Repeated idea | Classification |
|---|---|---|---|
| 1 | I-P1 and II-P1 | The NIST clause *"AI risks and related impacts be analysed, assessed, benchmarked and monitored, and that systems be tested before deployment and regularly while in operation"* appears **verbatim** in both, ~25 words | **COMPRESS LATER** |
| 2 | I-P2 and II-P2 | The ASTM / ALSHIEKH / FAA mechanism triplet is stated twice in near-identical terms, ~95 words of overlap | **COMPRESS LATER** |
| 3 | I-P2–P3 and II-P3 | The PARASURAMAN graduated-contraction description (complete set → narrowed → single suggestion) and the function-relative individuation point, ~55 words of overlap | **COMPRESS LATER** |
| 4 | III prose and Table I note | The {Go, Delay} researcher-defined / not-validated statement appears in the paragraph and again in the table note, ~20 words | **COMPRESS LATER** |
| 5 | IV, V-C and VI | Lower-bound qualification | **KEEP** — required wherever an activation figure is restated |
| 6 | V and VI | Headline figures with envelope, attribution and vessel-class context | **KEEP** — binding contract item 15 forbids the headline appearing alone |
| 7 | IV, Table III note and VI | Deterministic-census / no-inference statement | **KEEP** — each instance qualifies a different object |

Items 1–3 total roughly 175 words of genuine overlap between the Introduction and Background. Both passages are individually required — the page-1 concession is a NEVER-CUT item and Cluster B is mandated — but the second statement of each fact could be shortened to a back-reference without losing a concession. If typesetting overruns, this is a larger and safer recovery than several entries in the architecture's compression plan. **Not edited in Phase 5.**

### 11. Word and Layout Budget

Counting rule, applied uniformly: narrative paragraph text only. Excluded are the title, all section and subsection headings, table label lines, italic table and figure captions, all table rows, the Table I note, the Table III note and the Figure 1 caption. Displayed equations and the **Criterion** paragraph are counted as prose. Symbol-only tokens (`=`, `−`) are not counted as words.

| Section | Words | Architecture target |
|---|---|---|
| I. Introduction | **694** | ~720 |
| II. Background and Positioning | **501** | ~520 |
| III. Governance Contract, Criterion and Metric | **723** | ~720 |
| IV. Evaluation Design | **423** | ~430 |
| V. Results and Discussion | **888** | ~910 |
| VI. Limitations and Conclusion | **390** | ~390 |
| **TOTAL** | **3,619** | **~3,690** |

Tables: **3**. Figures: **1 placeholder**.

Three of these differ from the counts recorded in the phase audits — Section III 723 against 704, Section IV 423 against 434, Section V 888 against 899. The prose is unchanged; the phase counts were produced by differently configured scripts. The rule stated above is the one used here and should be the one used from now on.

**Layout risk: MODERATE.**

Body prose is 71 words under the architecture's aggregate target and every section is at or below its allocation, so the text itself is not the risk. The risk is that Figure 1 has no data and therefore no known height, the pre-draft feasibility check recorded essentially zero layout margin against the 1.1-column reference reserve, and the abstract, index terms and author block are not yet written. No page count can be asserted before IEEE typesetting.

### 12. Open Tasks

| Task | Status |
|---|---|
| **FIGURE DATA EXTRACTION REQUIRED** — Figure 1 has a caption and axis specification but no plotted data; no canonical sweep export exists in the repository | **PRE-FINAL BLOCKER** |
| **MFWAM CITATION RESOLUTION** — the RESOLUTION wave source is named in Section IV without a bibliographic record | **PRE-FINAL BLOCKER** |
| **IPoSCI PUBLICATION STATUS RECHECK** — accepted, not confirmed published; Lock v2 §16 item 5 | **PRE-SUBMISSION CHECK** |
| **[AI-GOV-SLR] author list** — Lock v2 §16 item 2, to be read from the corpus note before the reference list is built | **PRE-FINAL TASK** |
| **ASTM F3269-21 clause numbers** — Lock v2 §16 item 4; the citation must stay title-and-scope, so no clause number may be added | **PRE-SUBMISSION CHECK** |
| **RESOLUTION pairwise components** — provenance incomplete; remain withheld | **PRE-FINAL TASK** |

None solved in Phase 5.

### 13. Issues Requiring Manuscript Edits

**Two minor precision fixes and one optional alignment. No blocker.**

**ISSUE 1 — MINOR PRECISION FIX**
Section: III, second paragraph.
Phrase: *"As Section III-E makes explicit, the measurement reported in this paper does not validate it."*
Reason: Section III has no lettered subsections. Section V is the only section with A/B/C subsections, so *III-E* points at nothing and a reviewer will notice a broken internal reference on the first read of the method.
Recommended minimal change: replace *"As Section III-E makes explicit"* with *"As the consequences of the identity below make explicit"*. No claim changes.

**ISSUE 2 — MINOR PRECISION FIX**
Section: V, Table III caption.
Phrase: *"Binding frequency, comparator decomposition and robustness results."*
Reason: the claim-language guide maps *"robust to thresholds"* onto *"non-vacuous across sourced configurations"* precisely because the wave sensitivity is material — Δ<sub>L2</sub> moves across 2.54–14.75% under a ±0.25 m perturbation. A caption that labels the table *robustness results* invites the reading the guide exists to prevent, even though *robustness disclosure* is the chain's own term for the vessel-class rows. The body prose is correct; only the caption carries this risk.
Recommended minimal change: *"Binding frequency, comparator decomposition and sensitivity results."*

**ISSUE 3 — MINOR PRECISION FIX (optional, emphasis only)**
Sections: I-P6 and VI-P3.
Phrases: I-P6 lists the contribution as the measurement assembly and its four components and does **not** name the criterion; VI-P3 closes *"the contribution is the assembly that makes such a figure interpretable, together with the criterion."*
Reason: the criterion is SECONDARY CONTRIBUTION 1 in the patched chain, so Section VI is not inventing anything and this is a difference of emphasis rather than substance — **PASS WITH NOTE** under Audit 25. But a reviewer comparing the two statements sees one element in the conclusion that the introduction's contribution sentence omits.
Recommended minimal change, if taken: add the criterion to I-P6's list, or drop *"together with the criterion"* from VI-P3. Adding it to the Introduction is the better option because it matches the chain's ledger.

**Not applied.** No change was made to any locked sentence.

### 14. Abstract Readiness

**ABSTRACT READINESS: YES**

The chain holds end to end across the assembled paper, every locked value is consistent and correctly scoped, and no safety, optimality, human-validation or generalisation claim survives anywhere in the body. The three issues above are wording precision, not logic, and none of them changes a number, a claim or the contribution. Figure 1 and MFWAM remain pre-final blockers but neither constrains what the abstract can say.

### Final whole-paper questions

**A.** One question, asked in I-P5 and answered in V-C and VI-P3. **Yes.**
**B.** Architecture-novelty paper — **No.** The mechanisms are conceded in I-P2 and again in II-P2, and I-P6 states the contribution is the assembly rather than its constituent techniques.
**C.** 5.81% as safety improvement — **No.** It is introduced as a proportion of departure-window hours in which the restriction binds, and safety is denied in I-P6, III, V-C and VI.
**D.** Δ<sub>L2</sub> as magnitude of contraction — **No.** Section III states the distinction outright, before any number.
**E.** {Go, Delay} validated — **No.** Denied in III prose, the Table I note, the metric consequences and VI.
**F.** Thresholds optimal — **No.** *"Source provenance… does not establish that it is optimal"* in IV, and the envelope and perturbation in V-B.
**G.** C1↔C3 empirically discovered — **No.** Entailed in III, entailed again in V-A and in the Table III note.
**H.** 97.6% as waves causing 97.6% of risk — **No.** *"attributions of CAUTION classification, not of incidents or unsafe outcomes."*
**I.** Vessel-class variants as generalisation — **No.** Evaluation-policy settings in V-C, configuration checks in VI.
**J.** 5.81% versus 4.48% as spatial resolution alone — **No.** Denied explicitly in V-A.
**K.** Envelope as a confidence interval — **No.** Denied in V-B and in the Table III note.
**L.** Human-centred evaluation — **No.** Positioned under Responsible AI; VI states the human questions remain untested.
**M.** Validates safety or decision quality — **No.**
**N.** Conclusion preserves the Introduction's contribution — **Yes, with the emphasis note at Issue 3.**
**O.** Responsible AI connection is operational auditability — **Yes.**

No YES arises for B–M.

---

PHASE 5 STATUS: READY FOR ABSTRACT DRAFTING
