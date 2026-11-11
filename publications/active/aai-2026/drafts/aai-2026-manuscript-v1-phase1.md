# From Declared Risk Levels to Admissible Recommendations: Measuring the Operational Effect of AI Governance

> **Draft v1 — Phase 1 only.** Sections I and II. Abstract, Method, Evaluation Design, Results, Discussion, Limitations and Conclusion are not drafted.
> Venue: AAI 2026, Track 3 (positioned strictly under Responsible AI). IEEE conference format, A4, two-column, 6 pages maximum including references.
> Citation keys are temporary and resolve to `aai-2026-citation-evidence-lock-v2.md` §3 and §9.

---

## I. Introduction

Systems supporting consequential decisions are increasingly placed under explicit operating controls, commonly described by the risk levels they declare. A declared level constrains a system only if it changes the set of actions the system is permitted to take, and the presence of the level in a specification does not by itself establish that it does. Neither does it establish how often the constraint is encountered once the system runs against real conditions. Risk-management guidance directs that AI risks and related impacts be analysed, assessed, benchmarked and monitored, and that systems be tested before deployment and regularly while in operation [NIST]. Both properties are therefore open to measurement rather than settled by design.

Mechanisms for restricting what a system may do are established. Run-time assurance is standardised practice in aviation, where an independently assured architecture bounds the behaviour of a component containing complex functions [ASTM]. In safe reinforcement learning, a shield may compute the set of safe actions and remove the unsafe ones before the agent selects, rather than substituting a corrected action after selection [ALSHIEKH]. Certified collision-avoidance avionics inhibit advisory categories progressively as an externally measured state worsens, while leaving final authority with the crew [FAA]. The canonical model of human interaction with automation already describes graduated contraction of the alternatives presented to a person, from offering a complete set, to narrowing it, to suggesting one [PARASURAMAN]. This paper contributes none of these mechanisms.

That model also holds that automation cannot be assigned a single overall level, because a level is always stated relative to a specific function [PARASURAMAN]. What separates one level from another is the allocation it changes, not its position in a taxonomy. Applied to a declared risk level, this yields a question that can be checked rather than assumed: does the level alter the set of recommendations the system may produce, or does it appear only in the specification? A level that leaves the permitted set unchanged describes the design without constraining it.

Measuring how often such a boundary is encountered is not an unexplored activity, and Section II identifies work that performs parts of it. The narrower case concerns an intermediate level that contracts the permitted set while the system continues to operate, examined against a configuration that gates participation alone. Within the reviewed literature, no empirical characterisation was identified of how often an intermediate advisory-scope level changes the admissible recommendation set relative to a participation-only gate when replayed over a multi-year environmental record. That statement is scoped to the literature examined here, and to the combination of properties just described, rather than being a claim about the field as a whole.

This study addresses one question. **RQ1.** Over a multi-year environmental record for one deployment site, how often does an intermediate advisory-scope governance level change the admissible recommendation set relative to a participation-only gate, and how sensitive is that frequency to defensible threshold, vessel-class and denominator-policy configurations? The approach has three parts. A specification-level criterion states the condition under which a declared level changes system behaviour. Four configurations, C0 to C3, are then defined so that a participation-only gate and an intermediate-scope configuration differ at one state only, which allows the intermediate level to be isolated. The configurations are then replayed over five years of hourly environmental records for a single coastal-fisheries deployment site, and the resulting frequency is examined across the defensible threshold, vessel-class and denominator-policy settings that the evaluation permits.

The contribution is a measurement assembly and its interpretation rather than any of its constituent techniques. It comprises the isolation of an intermediate advisory-scope level against a participation-only configuration differing from it at one state; the interpretation of the resulting quantity as the frequency with which the active contraction binds, under the specified comparator construction; the sensitivity of that binding rate to the threshold that governs it; and the attribution of which state component produces the intermediate classification in the evaluated record. The study does not establish improved safety, improved decision quality, the optimality of the restricted recommendation set, effective human oversight, or generalisation beyond the evaluated site and vessel class. Each of these lies outside what the evaluation can support.

## II. Background and Positioning

Responsible AI has produced a substantial body of frameworks, principles and risk-management guidance. Reviews of this literature report that published governance frameworks frequently lack real-world implementation detail and validation, and that few studies specify together who governs, what is governed, when, and how [AI-GOV-SLR]. Risk-management guidance addresses part of this by directing that AI risks and related impacts be analysed, assessed, benchmarked and monitored, and that systems be tested before deployment and regularly while in operation [NIST]. Operational measurement of deployed controls is therefore an established activity rather than an absent one. The question taken up here is narrower: whether one particular declared level has an observable effect on the set of recommendations a system may produce.

The mechanisms by which available actions can be restricted at run time are well developed. ASTM F3269 standardises run-time assurance for aircraft systems containing complex functions, in which an independently assured architecture bounds the behaviour of the component it supervises [ASTM]. Work on safe reinforcement learning distinguishes a shield that computes the safe actions and removes the unsafe ones before the agent selects from one that substitutes a corrected action afterwards [ALSHIEKH]. Certified collision-avoidance avionics inhibit advisory categories progressively as an externally measured state worsens, and state explicitly that the crew retains authority [FAA]. Together these establish that restriction of this kind can be specified, implemented and, in the aviation cases, certified for operational use. The question addressed here is not whether a system can restrict its available actions, but how the operational effect of one declared level is measured.

The individuation of levels has a longer history in human-automation research. The canonical model holds that a level of automation is always stated relative to a specific function, and it describes graduated restriction of what is offered to a person across adjacent levels: a complete set of alternatives, a narrowed selection, or a single suggestion [PARASURAMAN]. That model is design-time and defines no run-time state variable. It nonetheless supplies the grounding for examining a declared level through the behaviour it permits or suppresses, rather than through its position in a scheme, which is the criterion stated in Section III.

Three recent studies each perform part of the measurement assembled here. Aarab specifies graduated run-time autonomy modes in which the permitted execution directives contract as severity rises while operation continues [AARAB]; the reported directive-frequency simulation is conducted under the permissive mode rather than as a comparison of graduated configurations. Miller evaluates alternative enforcement operators, including an ungoverned baseline, approval-only gating and projection-based repair, through systematic ablation [MILLER]; those configurations compare operators rather than graduated risk levels, and do not measure how often an intermediate contraction binds. Kim et al. quantify the burden of an intermediate zone requiring mandatory human review, and characterise it across reliability targets on real clinical data [KIM]; that zone withdraws automated action rather than retaining an active contracted recommendation set. Within the reviewed literature, these works do not combine active intermediate scope contraction, a participation-only comparator, marginal isolation, and binding-frequency measurement.

---

## Drafting Audit

All figures below were computed from the drafted prose, not estimated.

| # | Check | Result |
|---|---|---|
| 1 | Introduction word count | **690** (target 680–720) ✅ |
| 2 | Background word count | **501** (target 500–520) ✅ |
| 3 | Total Phase-1 word count | **1,191** |
| 4 | Six Introduction paragraphs | ✅ **Confirmed** — P1 113 · P2 122 · P3 93 · P4 110 · P5 131 · P6 121. Every paragraph inside its individual target |
| 5 | Four Background clusters | ✅ **Confirmed** — A 117 · B 140 · C 99 · D 145. Every cluster inside its individual target |
| 6 | RQ copied verbatim | **YES** — exact string match against §6 of the patched locked research chain |
| 7 | "pre-inference" absent | **YES** — Correction D1 applied; the concession uses *"before the agent selects"* |
| 8 | IPoSCI citation absent | **YES** — no reference, no allusion, no publication-status language |
| 9 | Aarab / Miller single-author discipline | **PASS** — both cited without "et al."; "Kim et al." used correctly |
| 10 | All absence claims scoped | **PASS** — two absence statements, both opening *"Within the reviewed literature"* (Intro P4, Cluster D close) |
| 11 | Generic mechanism novelty absent | **PASS** — no instance of *novel · first · unique · unprecedented · never studied · no one has measured · no prior work*. P2 closes with *"This paper contributes none of these mechanisms."* Cluster B closes by relocating the open question to measurement |
| 12 | Cluster D contains all three near-neighbours | **PASS** — Aarab, Miller, Kim et al. in the prescribed order, each with its verified limit stated |
| 13 | Comparator-necessity claim absent | **PASS** — Intro P5 states only that four configurations differ at one state, "which allows the intermediate level to be isolated". No claim that the ladder is needed to obtain the value; no numerical result given in Phase 1 |
| 14 | Unresolved citation placeholder | **One: `[AI-GOV-SLR]`.** The author list for the AI-governance systematic literature review is still uncaptured. The corpus note exists at `notes/AI governance- a systematic literature review.md`, so this is a lookup rather than a gap. All other keys resolve to publisher-verified records in Citation Lock v2 §3 and §9 |

**Additional style verification**

| Item | Result |
|---|---|
| Em dashes in manuscript prose | **0** |
| "governance" occurrences in prose | **2** (both load-bearing: the RQ, and the near-neighbour framing) |
| Bullet lists in prose | **None** |
| Banned openers (*Interestingly*, *Importantly*, *Remarkably*, *To the best of our knowledge*) | **None** |
| Citation keys used | AARAB · AI-GOV-SLR · ALSHIEKH · ASTM · FAA · KIM · MILLER · NIST · PARASURAMAN — all present in Citation Lock v2; none invented |
| Bibliographic detail invented | **None.** No page numbers, volumes or dates appear in prose |

**Contract items exercised in Phase 1**

Items 1, 2, 3, 7, 8, 9, 10, 11, 14, 17, 20 of the §14 drafting contract are directly exercised and satisfied. Items 4, 5, 6, 12, 13, 15, 16, 18, 19 apply to Method, Results and Limitations and are carried forward to later phases.

**Notes for the reviewer**

The first mention of the application domain is a single clause in Intro P5 (*"a single coastal-fisheries deployment site"*), consistent with the locked role of the domain as evaluation setting. Fisheries does not appear in the title, in P1 through P4, or anywhere in Section II.

Intro P4 deliberately concedes that binding-rate measurement is not unexplored before stating the gap, and forwards the detail to Section II. This prevents the gap sentence from reading as a broader absence claim than the evidence supports.

Cluster A states plainly that operational measurement of deployed controls is established, which removes the strongest available misreading of the paper's positioning.

---

PHASE 1 STATUS: READY FOR REVIEW
