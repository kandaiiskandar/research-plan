# From Declared Risk Levels to Admissible Recommendations: Measuring the Operational Effect of AI Governance

> **Draft v1 — Phase 1 only.** Sections I and II. Abstract, Method, Evaluation Design, Results, Discussion, Limitations and Conclusion are not drafted.
> Venue: AAI 2026, Track 3 (positioned strictly under Responsible AI). IEEE conference format, A4, two-column, 6 pages maximum including references.
> Citation keys are temporary and resolve to `aai-2026-citation-evidence-lock-v2.md` §3 and §9.

---

## I. Introduction

Systems supporting consequential decisions are increasingly placed under explicit operating controls, commonly described by the risk levels they declare. A declared level constrains a system only if it changes the set of actions the system is permitted to take, and the presence of the level in a specification does not by itself establish that it does. Neither does it establish how often the constraint is encountered once the system runs against real conditions. Risk-management guidance directs that AI risks and related impacts be analysed, assessed, benchmarked and monitored, and that systems be tested before deployment and regularly while in operation [NIST]. These properties can therefore be treated as measurement questions rather than assumed from the design specification.

Mechanisms for restricting what a system may do are established. Run-time assurance is standardised practice in aviation, where an independently assured architecture bounds the behaviour of a component containing complex functions [ASTM]. In safe reinforcement learning, a shield may compute the set of safe actions and remove the unsafe ones before the agent selects, rather than substituting a corrected action after selection [ALSHIEKH]. Certified collision-avoidance avionics inhibit advisory categories progressively as an externally measured state worsens, while leaving final authority with the crew [FAA]. The canonical model of human interaction with automation already describes graduated contraction of the alternatives presented to a person, from offering a complete set, to narrowing it, to suggesting one [PARASURAMAN]. This paper contributes none of these mechanisms.

That model also holds that automation cannot be assigned a single overall level, because a level is always stated relative to a specific function [PARASURAMAN]. What separates one level from another is the allocation it changes, not its position in a taxonomy. Applied to a declared risk level, this yields a question that can be checked rather than assumed: does the level alter the set of recommendations the system may produce, or does it appear only in the specification? A level that leaves the permitted set unchanged describes the design without constraining it.

Measuring how often such a boundary is encountered is not an unexplored activity, and Section II identifies work that performs parts of it. The narrower case concerns an intermediate level that contracts the permitted set while the system continues to operate, examined against a configuration that gates participation alone. Within the reviewed literature, no empirical characterisation was identified of how often an intermediate advisory-scope level changes the admissible recommendation set relative to a participation-only gate when replayed over a multi-year environmental record. That statement is scoped to the literature examined here, and to the combination of properties just described, rather than being a claim about the field as a whole.

This study addresses one question. **RQ1.** Over a multi-year environmental record for one deployment site, how often does an intermediate advisory-scope governance level change the admissible recommendation set relative to a participation-only gate, and how sensitive is that frequency to defensible threshold, vessel-class and denominator-policy configurations? The approach has three parts. A specification-level criterion states the condition under which a declared level changes system behaviour. Four configurations, C0 to C3, are then defined so that a participation-only gate and an intermediate-scope configuration differ at one state only, which allows the intermediate level to be isolated. The configurations are then replayed over five years of hourly environmental records for a single coastal-fisheries deployment site, and the resulting frequency is examined across the defensible threshold, vessel-class and denominator-policy settings that the evaluation permits.

The contribution is a measurement assembly and its interpretation rather than any of its constituent techniques. It comprises the isolation of an intermediate advisory-scope level against a participation-only configuration differing from it at one state; the interpretation of the resulting quantity as the frequency with which the active contraction binds, under the specified comparator construction; the sensitivity of that binding rate to the threshold that governs it; and the attribution of which state component produces the intermediate classification in the evaluated record. The study does not establish improved safety, improved decision quality, the optimality of the restricted recommendation set, effective human oversight, or generalisation beyond the evaluated site and vessel class. Each of these lies outside what the evaluation can support.

## II. Background and Positioning

Responsible AI has produced a substantial body of frameworks, principles and risk-management guidance. Reviews of this literature report that published governance frameworks frequently lack real-world implementation detail and validation, and that few studies specify together who governs, what is governed, when, and how [AI-GOV-SLR]. Risk-management guidance addresses part of this by directing that AI risks and related impacts be analysed, assessed, benchmarked and monitored, and that systems be tested before deployment and regularly while in operation [NIST]. Operational measurement of deployed controls is therefore an established activity rather than an absent one. The question taken up here is narrower: whether one particular declared level has an observable effect on the set of recommendations a system may produce.

The mechanisms by which available actions can be restricted at run time are well developed, and they appear in both standardised and research settings. ASTM F3269 standardises run-time assurance for aircraft systems containing complex functions, in which an independently assured architecture bounds the behaviour of the component it supervises [ASTM]. Work on safe reinforcement learning distinguishes a shield that computes the safe actions and removes the unsafe ones before the agent selects from one that substitutes a corrected action afterwards [ALSHIEKH]. Certified collision-avoidance avionics inhibit advisory categories progressively as an externally measured state worsens, and state explicitly that the crew retains authority [FAA]. Together these establish that state-conditioned restriction is not itself the open contribution. The question addressed here is not whether a system can restrict its available actions, but how the operational effect of one declared level is measured.

The individuation of levels has a longer history in human-automation research. The canonical model holds that a level of automation is always stated relative to a specific function, and it describes graduated restriction of what is offered to a person across adjacent levels: a complete set of alternatives, a narrowed selection, or a single suggestion [PARASURAMAN]. That model is design-time and defines no run-time state variable. It nonetheless supplies the grounding for examining a declared level through the behaviour it permits or suppresses, rather than through its position in a scheme, which is the criterion stated in Section III.

Three recent studies each perform part of the measurement assembled here. Aarab specifies graduated run-time autonomy modes in which the permitted execution directives contract as severity rises while operation continues [AARAB]; the reported directive-frequency simulation is conducted under the permissive mode rather than as a comparison of graduated configurations. Miller evaluates alternative enforcement operators, including an ungoverned baseline, approval-only gating and projection-based repair, through systematic ablation [MILLER]; those configurations compare operators rather than graduated risk levels, and do not measure how often an intermediate contraction binds. Kim et al. quantify the burden of an intermediate zone requiring mandatory human review, and characterise it across reliability targets on real clinical data [KIM]; that zone withdraws automated action rather than retaining an active contracted recommendation set. Within the reviewed literature, these works do not combine active intermediate scope contraction, a participation-only comparator, marginal isolation, and binding-frequency measurement.

---

## Micro-Revision Audit

| # | Check | Result |
|---|---|---|
| 1 | Edit 1 applied | **YES** — Intro P1 closing sentence replaced with *"These properties can therefore be treated as measurement questions rather than assumed from the design specification."* Old sentence verified absent |
| 2 | Edit 2 applied | **YES** — Cluster B sentence replaced with *"Together these establish that state-conditioned restriction is not itself the open contribution."* Old sentence, including *"certified for operational use"*, verified absent |
| 3 | Introduction word count | **694** (target 680–720) ✅ |
| 4 | Background word count | **501** (target 500–520) ✅ |
| 5 | RQ unchanged verbatim | **YES** — exact string match retained |
| 6 | Gap B unchanged substantively | **YES** — Intro P4 byte-identical to the reviewed draft |
| 7 | Cluster D unchanged substantively | **YES** — byte-identical; scoped residue sentence intact |
| 8 | Contribution paragraph unchanged substantively | **YES** — Intro P6 byte-identical |
| 9 | New citation introduced | **NO** — key set unchanged: AARAB · AI-GOV-SLR · ALSHIEKH · ASTM · FAA · KIM · MILLER · NIST · PARASURAMAN. `[AI-GOV-SLR]` left unresolved as instructed |
| 10 | "pre-inference" absent | **YES** |
| 11 | IPoSCI absent | **YES** |
| 12 | Any unintended substantive change | **NONE.** A paragraph-level diff confirms exactly two paragraphs changed — Intro P1 and Cluster B. Intro P2–P6 and Clusters A, C, D are byte-identical to the reviewed draft |

### Declared adjustments beyond the two literal replacements

Two adjustments were made under the authority the brief grants. Both are declared rather than silent.

**1. Minimal grammatical adjustment in Cluster B (authorised by Edit 2's instruction).** The replacement sentence as specified ended *"…is not itself the open contribution addressed here."* The preserved transition that follows opens *"The question addressed here is not whether…"*, so the phrase *"addressed here"* would have appeared twice in consecutive sentences. The adjustment removes it from the **new** sentence, leaving the preserved transition verbatim. This modifies only text authored under instruction in this task, not protected text, and adds no claim.

**2. Non-substantive restoration to hold the Background budget.** Edit 2 removes ten words. Background would otherwise have fallen to **491**, below the 500–520 target. The opening sentence of Cluster B — the paragraph already under edit — was extended to *"…are well developed, and they appear in both standardised and research settings."* This describes the citation set already present in that paragraph (two standardised or regulatory sources, one research source). It makes no clause-level claim about any individual source, and in particular no claim about ASTM F3269 beyond the title-and-scope support locked in Citation Lock v2 §9.

### Verification of the concern behind each edit

**Edit 1.** The paragraph no longer asserts that the properties *are* open to measurement immediately after the NIST citation; it states they *can be treated as* measurement questions. The modal weakens the inference and the NIST-supported sentence preceding it is untouched. The antecedent of *"These properties"* remains the two properties named earlier in the paragraph — whether a declared level changes the permitted set, and how often the constraint is encountered — not anything attributed to NIST.

**Edit 2.** No implementation or certification breadth is now claimed anywhere in Cluster B. The paragraph cites ASTM for what the standard is, and draws no conclusion about how widely run-time assurance has been implemented or certified in practice.

---

PHASE 1 REVISION STATUS: READY FOR PHASE 2
