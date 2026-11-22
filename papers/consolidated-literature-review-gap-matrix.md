# Consolidated PhD Literature Review and Research Gap Matrix

**Version 1.0 · 17 November 2026**

Based on 21 unique Scopus AI reports and the primary-paper checks discussed so far.

This is the current **working literature review matrix** for the PhD proposal defence. It separates established contributions, competing methods, potential research gaps, and what the research must demonstrate.

The matrix does not assume that every gap suggested by Scopus AI is valid. Publication details and contributions previously checked against primary sources are distinguished from papers that still require full-text methodological review.


---

## Contributors and attribution

This document is written jointly. Each matrix and each added finding carries the
author who produced it. Text without a tag is the agreed shared baseline.

| Tag | Contributor | Contributed here |
|---|---|---|
| **[GPT]** | GPT | Matrices A–F: the competing-research survey, gap assessment, candidate contributions, research questions, experiment design and journal mapping |
| **[Claude]** | Claude (Cowork session, 16–17 Nov 2026) | Matrix G (local holdings audit), Matrix H (primary-source verification), the Scopus AI PDF→Markdown corpus, and `research/pilot-preparation-audit.md` including the event-cluster analysis |
| **[Iskandar]** | Iskandar Samsuddin | Direction, source material, and final judgement on every entry |

Conventions: a tagged line is a finding, comment or correction attributable to one
contributor. A correction never silently overwrites another contributor's text —
it is recorded alongside it, and the original author decides whether to amend.

**Source material in this repository**

| Item | Location |
|---|---|
| The 21 Scopus AI reports (PDF) | `papers/scopus/` |
| The same reports as Markdown | `papers/scopus/markdown/` — 252 pages, 34 tables, 1,181 reference entries |
| Earlier novelty and scoping assessment | `docs/analysis/graduated-advisory-safety-novelty-assessment.md` (16 Nov 2026) |
| Pilot readiness audit for the next study | `research/pilot-preparation-audit.md` (16 Nov 2026) |
| Prior literature-review working set | `papers/review-plan.md`, `papers/comparison-table.md`, `papers/paper_tracker.md`, `papers/search-methodology.md` |

---

## Matrix A — Closest competing research  ·  *[GPT]*

| Study | Established contribution | Relationship to our PhD | Assessment |
| --- | --- | --- | --- |
| Hobbs et al. (2023), *Run Time Assurance for Safety-Critical Systems* | Runtime safety supervision and filtering | Independent deterministic safety layer | Established foundation |
| Peng et al. (2023), RTA-IR | Verifiable safety controller combined with AI-based planning | Layered safety–performance architecture | Strong competitor |
| Vaaler et al. (2024), *Modular Control Architecture for Safe Marine Navigation* | RL combined with predictive safety filters | Maritime AI and independent safety enforcement | Very close competitor |
| Li et al. (2024), CARAC | Contextual risk-dependent authorization | Mapping risk to permitted actions | Very close conceptual competitor |
| Charmet et al. (2024), ODD monitoring | Monitoring operational domains under uncertain measurements | Environmental uncertainty and admissibility | Strong competitor |
| Vermaelen & Holvoet (2025), Tumato 2.0 | Safe constraint-based planning with nondeterministic outcomes | Action selection and recovery constraints | Strong competitor |
| Corsi et al. (2025/2026), *Efficient Dynamic Shielding* | Efficient adaptation to changing safety specifications | Dynamic restrictions and resource efficiency | Strong competitor |
| Kim et al. (2026), SA-ROC | Three-zone clinical decisions and gray-zone workload measurement | Intermediate-state contribution evaluation | Strong methodological competitor |
| Miller et al. (2026), CAIS | Deterministic governance operator and controlled simulations | Formal restriction of AI-generated actions | Very close competitor |
| Miller et al. (2026), Adaptive Human Oversight | Risk-aware maritime AI governance and human oversight | Risk gating in maritime operations | Very close competitor |
| Xiong & Bao (2026), EdgeTalk-MCU | State-aware prompting, runtime shielding, edge deployment | Lightweight deterministic–AI architecture | Very close competitor |
| Ghaleb et al. (2026), Uncertainty-Calibrated Safety Gating | Calibrated execution, pause, and fallback policies | Safety–utility trade-offs under uncertainty | Very close competitor |
| Hamel-de le Court et al. (2026), ProSh | Probabilistic shielding using risk budgets | Constrained action selection | Strong competitor |
| Zhang et al. (2026), Health-ORSC-Bench | Benchmark for over-refusal and safe completion | Restricted AI advice versus refusal | Related competitor |
| Kwon & Kim (2026), Conformal Selective Prediction | Uncertainty-aware, cost-sensitive deferral | Retaining reliable decisions under uncertainty | Strong methodological competitor |
| Alves et al. (2024), DeCCaF | Cost-sensitive human deferral with workload constraints | AI–human decision authority | Related competitor |

**Interpretation:** These studies collectively establish much of the underlying mechanism. Our novelty must be demonstrated at the level of a new computational method, new formal property, or generalizable empirical finding.

The entries reflect our previous literature assessment. The strongest competing papers still need full-text, method-by-method comparison before they become the final thesis evidence matrix. Matrix G records which of them are currently held locally.

> **[Claude · 17 Nov 2026]** Primary-source checks on 17 November corrected the publication details of five rows above and could not verify two. The entries are left as written; **Matrix H** records what each check returned.

---

## Matrix B — Established knowledge versus candidate research gaps  ·  *[GPT]*

| ID | Research area | What is established | Candidate gap | Current confidence |
| --- | --- | --- | --- | --- |
| G1 | Layered AI safety architecture | Independent safety supervision and AI control | No sufficiently differentiated gap identified | Low |
| G2 | Graduated safety states | Multiple risk or decision states | Three-state classification alone is not novel | Low |
| G3 | Advisory admissibility | Rule-based restrictions, action masking, constrained outputs | Environmental-risk-specific advice semantics may require further investigation | Low–moderate |
| G4 | Intermediate-state contribution | Gray-zone evaluation, intervention and deferral metrics | Incremental effects of intermediate *advisory categories* against strong baselines | Moderate, unconfirmed |
| G5 | Safety–utility trade-off | Safety filtering, selective prediction, learning to defer | Conditions where partial advice offers defensible advantages | Moderate, unconfirmed |
| G6 | Unreliable environmental observations | Uncertainty-aware monitoring, robust control, shielding | Dependable permission decisions under stale, missing, delayed, and conflicting observations | Moderate; strongest candidate |
| G7 | Low-resource execution | Edge shielding and lightweight safety enforcement | Resource-bounded robust admissibility with a distinct computational advance | Low–moderate |
| G8 | Human decision-making | Trust calibration, reliance, selective AI advice | Behaviour under environmental-risk-based advisory restrictions | Low–moderate |
| G9 | Independent safety validation | Scenario testing, safety metrics, risk–coverage evaluation | Reproducible evaluation separating policy conformance from operational safety | Moderate, unconfirmed |

These confidence labels indicate the strength of evidence for an *unresolved gap*, not the probability that a contribution will be accepted or published.

---

## Matrix C — Potential original PhD contributions  ·  *[GPT]*

| ID | Candidate contribution | Novelty potential | Feasibility | Main obstacle |
| --- | --- | --- | --- | --- |
| C1 | Formal model of graduated advisory permissions | Limited alone | High | Similar formal models already exist |
| C2 | Controlled evaluation of intermediate-state decision value | Moderate as an empirical contribution | High | Need independent reference outcomes and strong comparators |
| C3 | Robust advisory-permission method under degraded environmental observations | Promising, unverified | Moderate–high | Need a new mechanism beyond existing uncertainty-aware methods |
| C4 | Efficient enforcement under resource and connectivity constraints | Conditional | Moderate–high | Must demonstrate a distinct computational improvement |
| C5 | Human-centred evaluation of restricted advice | Conditional | Moderate–low | Recruitment, ethics, experimental validity |

**Current preference:** Treat C1 as the formal foundation, C2 as the main comparative evaluation, and C3 as the principal candidate for technical originality. C4 can strengthen C3, but should not be claimed as new without evidence.

---

## Matrix D — Research questions and validation  ·  *[GPT]*

| RQ | Proposed research question | Experimental evidence required |
| --- | --- | --- |
| RQ1 | How can environmental risk, observation reliability, and advisory permissions be represented in a verifiable decision policy? | Formal definitions, properties, consistency checks, counterexamples |
| RQ2 | Under what conditions do intermediate advisory restrictions improve the safety–usefulness trade-off compared with binary and existing risk-adaptive policies? | Matched replay, calibrated baselines, independent safety criteria, statistical comparisons |
| RQ3 | How can advisory permissions remain dependable under missing, stale, delayed, or conflicting observations within resource constraints? | New method, fault injection, robustness comparisons, latency and resource measurements |

---

## Matrix E — Proposed experiments and baselines  ·  *[GPT]*

| Configuration | Policy | Purpose |
| --- | --- | --- |
| B1 | Permissive binary gate | Measures the risk of allowing full advice at intermediate hazard levels |
| B2 | Conservative binary gate | Measures useful advice lost through early restriction |
| B3 | Static graduated gate | Establishes the current architecture's behaviour |
| B4 | Conventional uncertainty-aware policy | Provides a stronger nontrivial baseline |
| P1 | Proposed degraded-information-aware policy | Isolates the contribution of the new method |
| P1 ablation | Proposed method without its key new mechanism | Tests whether that mechanism creates the improvement |

We should measure unsafe permissions, useful recommendations retained, unnecessary restrictions, safety-policy conformance, sensitivity to observation degradation, computational latency, and memory usage.

A critical requirement is that the safety reference must not simply repeat the rules used to construct the proposed policy.

---

## Matrix F — Two proposed journal papers  ·  *[GPT]*

| Dimension | Journal Paper 1 | Journal Paper 2 |
| --- | --- | --- |
| Focus | Intermediate advisory restrictions | Dependability under degraded observations |
| Main RQ | RQ2, supported by RQ1 | RQ3, supported by RQ1 |
| Potential contribution | Generalizable comparative findings or an evaluation methodology | New robustness or permission-control method |
| Data | Historical environmental replay and candidate recommendations | Same platform with controlled observation degradation |
| Main evaluation | Safety–usefulness trade-offs and policy comparisons | Robustness, fallback behaviour, recovery, resource cost |
| Main publication risk | Merely applying known policies | Reimplementing existing conservative or uncertainty-aware control |

---

## Matrix G — Local evidence availability for Matrix A  ·  *[Claude]*

*Added 17 November 2026. Compiled by filename and full-text search across `papers/`, `papers/sources/` and `notes/`, and by keyword search across `papers/scopus/markdown/`. This matrix records what the repository currently holds; it makes no judgement about the studies themselves.*

| Study | Primary source held? | Evidence in repository |
| --- | --- | --- |
| Hobbs et al. (2023), Run Time Assurance | **No** | Named in 1 of 21 Scopus AI reports |
| Peng et al. (2023), RTA-IR | **No** | Scopus AI summary only |
| Vaaler et al. (2024), Marine Navigation | **No** | Named in 1 of 21 reports |
| Li et al. (2024), CARAC | **No** | Not named in any of the 21 reports under that acronym |
| Charmet et al. (2024), ODD monitoring | **No** | Named in 1 of 21 reports |
| Vermaelen & Holvoet (2025), Tumato 2.0 | **Yes** | `papers/sources/Tumato 2.0 - a constraint-based planning approach for safe and robust robot behavior.pdf` |
| Corsi et al. (2025/2026), Efficient Dynamic Shielding | **Different paper held** | `papers/sources/Verification-Guided Shielding for Deep Reinforcement Learning.pdf` (Corsi, Amir, Rodríguez, Sánchez, Katz, Fox) — same group, different title. Confirm whether *Efficient Dynamic Shielding* is a separate work |
| Kim et al. (2026), SA-ROC | **Yes** | `papers/Defining operational safety in clinical artificial intelligence systems.pdf` — SA-ROC appears in its full text (verified) |
| Miller et al. (2026), CAIS | **Yes** | `papers/Controlled Agentic AI Systems- A Governance-Driven Architecture for Auditable and Reproducible Decision Pipelines.pdf` |
| Miller et al. (2026), Adaptive Human Oversight | **No** | Scopus AI summary only |
| Xiong & Bao (2026), EdgeTalk-MCU | **No** | Named in 1 of 21 reports |
| Ghaleb et al. (2026), Uncertainty-Calibrated Safety Gating | **Yes** | `papers/sources/Uncertainty-Calibrated Safety Gating.pdf`, with an extraction note in `notes/` |
| Hamel-de le Court et al. (2026), ProSh | **Related paper held** | `papers/sources/Probabilistic Shielding for Safe Reinforcement Learning.pdf` (Hamel-De le Court, Belardinelli, Goodall; AAAI-25). The name *ProSh* does not appear in it — confirm whether this is the same work or an earlier one |
| Zhang et al. (2026), Health-ORSC-Bench | **No** | Named in 2 of 21 reports |
| Kwon & Kim (2026), Conformal Selective Prediction | **Note only** | `notes/Conformal selective prediction with cost aware deferral for safe clinical triage under distribution shift.md` — no PDF held |
| Alves et al. (2024), DeCCaF | **No** | Named in 1 of 21 reports |

**Position:** 4 of the 16 competing studies are held as primary sources, 2 more are represented by a related paper from the same author group, 1 exists only as an extraction note, 8 are known solely through Scopus AI summaries, and **1 — CARAC — is traceable to no source in this corpus**: it is neither held locally nor named in any of the 21 reports. *(Identified off-corpus and verified from the publisher PDF on 17 Nov as an information-security access-control paper, now held in `papers/sources/` — see Matrix H and plan §8.10.)* This is the concrete form of the first item under *What is still missing*.

> **[Claude · 17 Nov 2026]** Correction to my own earlier wording, which counted CARAC among the Scopus-AI-only group while the row above recorded that the acronym appears in none of the reports. The two statements contradicted each other; the CARAC row was right. Flagged in `research/next-research-plan.md` §1 by GPT.

---

## Matrix H — Primary-source verification of Matrix A  ·  *[Claude]*

*Added 17 November 2026. Each URL cited in `research/next-research-plan.md` §1 was fetched and its
title, author list, venue and year read from the publisher's own page. Matrix A is left as GPT wrote
it; this matrix records what verification returned, so the original author can decide what to amend.*

| Matrix A entry | Verified record | Status |
| --- | --- | --- |
| Kim et al. (2026), SA-ROC | *Defining operational safety in clinical artificial intelligence systems* — Young-Tak Kim, Hyunji Kim, Manisha Bahl, Michael H. Lev, Ramon Gilberto González, Michael S. Gee, …, Synho Do. npj Digital Medicine 9, art. 281, 2026. doi 10.1038/s41746-026-02450-7 | **Confirmed.** The abstract names SA-ROC and describes a Rule-in Safe Zone, a Rule-out Safe Zone and a Gray Zone requiring human review |
| Ghaleb et al. (2026), Uncertainty-Calibrated Safety Gating | *Uncertainty-Calibrated Safety Gating for Vision–Language–Action Manipulation Under Domain Shift* — Atef M. Ghaleb, Ali S. Allahloh, Sobhi Mejjaouli, Mohammed A. H. Ali, Adel Al-Shayea. Sensors 26(10):3140, 2026 | **Confirmed, with a scope caveat.** The paper is about robot manipulation under domain shift, not advisory or maritime decision support. The calibrated execution / pause / fallback mechanism is a genuine precedent; the application domain is not adjacent |
| Miller et al. (2026), CAIS | *Controlled Agentic AI Systems: A Governance-Driven Architecture for Auditable and Reproducible Decision Pipelines* — **Tymoteusz Miller, sole author**. Mach. Learn. Knowl. Extr. 8(5), art. 125, 2026 | **Confirmed, cite as Miller (2026)**, not "Miller et al." Same author as the row below, so treating the two as one research programme is correct |
| Miller et al. (2026), Adaptive Human Oversight | *Adaptive Human Oversight for Maritime Agentic AI Systems: Balancing Operator Workload and Safety Through Risk-Aware Governance* — Tymoteusz Miller, Irmina Durlik, Paweł Biczak. Applied Sciences 16(14):6903, 2026 | **Confirmed** |
| Corsi et al. (2025/2026), Efficient Dynamic Shielding | *Efficient Dynamic Shielding for Parametric Safety Specifications* — Davide Corsi, **Kaushik Mallik**, Andoni Rodriguez, Cesar Sanchez. **arXiv:2505.22104**, May 2025 (v2 Aug 2026) | **Confirmed from the preprint 17 Nov:** arXiv:2505.22104**v2**, 18 Aug 2026, 23 pp., authors Corsi (UC Irvine), Mallik, Rodríguez, Sánchez (IMDEA) — read from the paper itself. **Published version CONFIRMED 17 Nov at Springer:** Corsi, Mallik, Rodríguez, Sánchez (**2026**), in D'Souza, Komondoor, Srivathsan (eds), *Automated Technology for Verification and Analysis. ATVA 2025*, LNCS **16145**, pp. **157–179**, Springer Cham, doi 10.1007/978-3-032-08707-2_8; first online 26 Oct 2025. **This row is peer-reviewed prior art. Cite the year as 2026** — "Springer 2025" is the first-online date, not the citation year (plan §8.12). **Cite the proceedings version, not the preprint.** Author set differs from the locally held *Verification-Guided Shielding* (Corsi, Amir, Rodríguez, Sánchez, Katz, Fox) — Matrix G's "same group, different title" caution resolves to two genuinely different papers |
| Hamel-de le Court et al. (**2026**), ProSh | *ProSh: Probabilistic Shielding for Model-free Reinforcement Learning* — Edwin Hamel-De le Court, **Gaspard Ohlmann**, Francesco Belardinelli. **arXiv:2510.15720, October 2025**. **Published version confirmed 17 Nov:** AAMAS 2026 Extended Abstracts, Paphos, 25–29 May 2026, p. 3411, 3 pp., doi 10.65109/KCVZ6904 — the arXiv manuscript is the full version (plan §8.7) | **Year and authors corrected.** The paper does use the name ProSh. It is distinct from the locally held AAAI-25 *Probabilistic Shielding for Safe Reinforcement Learning* (Hamel-De le Court, Belardinelli, **Goodall**), which does not use the name. Matrix G's second caution also resolves to two different papers |
| *(absent from Matrix A; added by the plan)* CAP | *CAP: Conformalized Abstention Policies for Context-Adaptive Risk Management for LLMs and VLMs* — Sina Tayebati, Divake Kumar, Nastaran Darabi, Dinithi Jayasuriya, Theja Tulabandhula, Ranganath Krishnan, Amit Ranjan Trivedi. **PMLR 304:926–941, 2025** — 17th Asian Conference on Machine Learning, Taipei, 9–12 Dec 2025; volume published 13 Nov 2025 | **Confirmed 17 Nov; cite as 2025.** **No DOI** — PMLR identifies by abstract URL, volume:pages and BibTeX key `pmlr-v304-tayebati26a`; the `26a` is a filename convention, not a year. Balances point prediction, set prediction and full abstention on downstream utility, as the plan states. Domain is LLMs and VLMs. **Not held in the corpus, and Matrix A has no row for it** (plan §8.11) |
| Vaaler et al. (2024), Marine Navigation | *Modular control architecture for safe marine navigation: Reinforcement learning with predictive safety filters* — Aksel Vaaler, Svein Jostein Husa, Daniel Menges, Thomas Nakken Larsen, Adil Rasheed (NTNU). Artificial Intelligence **336** (2024), art. 104201, doi 10.1016/j.artint.2024.104201, CC BY 4.0 | **CONFIRMED 17 Nov** from the publisher PDF (plan §8.8). Matrix A's description is accurate. Filters **control actions** of an autonomous vessel against a dynamics model — the PhD restricts **advisory categories** to a human, so the distinction is level of intervention, not domain |
| Hamel-de le Court, AAAI-25 record | *Probabilistic Shielding for Safe Reinforcement Learning* — Edwin Hamel-De le Court, Francesco Belardinelli, Alexander W. Goodall, Imperial College London. AAAI-25, proceedings p. 16091, © 2025 AAAI doi **10.1609/AAAI.v39i15.33767** | **CONFIRMED 17 Nov** from the publisher PDF's own metadata and title page (plan §8.6). The `ojs.aaai.org` link remains bot-blocked and is not needed. Distinct from ProSh in title, third author, method and naming |
| Li et al. (2024), CARAC | *Context-Aware Risk Attribute Access Control* — Binyong Li, Fan Yang, Shaowei Zhang. *Mathematics* **12**(16), art. 2541, 17 Aug 2024, doi 10.3390/math12162541 | **CONFIRMED 17 Nov from the publisher PDF; attribution correct, domain is not.** Byline *Li, B.; Yang, F.; Zhang, S.*, so "Li et al." is right. This is information-security access control — which users may access which resources. Full-text counts: *access control* 106, *user* 156, against *autonomous* 0, *reinforcement learning* 0, *shield* 0, *advisory* 0. "Very close conceptual competitor" is not supportable on the paper's content; withdraw the row or relabel it a cross-domain analogy (plan §8.10) |

> **[Claude · 17 Nov 2026]** A primary source was added to the corpus on 17 November and it is
> **not in Matrix A**: Hilde Gerold and Sergio Lucia, *Safe reinforcement learning via adaptive robust
> model predictive shielding*, Computers and Chemical Engineering 206 (2026), art. 109521,
> doi 10.1016/j.compchemeng.2025.109521, open access CC BY 4.0. Now held at
> `papers/sources/Safe reinforcement learning via adaptive robust model predictive shielding.pdf`.
> It is already cited in `docs/analysis/graduated-advisory-safety-novelty-assessment.md:28` and named
> on the §3 reading list of the plan, so its absence from Matrix A is a gap in the matrix rather than
> a new discovery. **It is also the closest published precedent for C3 that the corpus now contains**:
> an adaptive safety parameter placed in the RL observation space lets the agent vary its own
> conservativeness, cutting unnecessary backup interventions while keeping constraint violations at
> zero — the same safety-at-comparable-usefulness shape the PhD proposes to claim, demonstrated on a
> nonlinear reactor with parametric uncertainty. Matrix A should gain a row for it, and C3's "need a
> new mechanism beyond existing uncertainty-aware methods" obstacle should be read against it.

> **[Claude · 17 Nov 2026, revised]** Two cross-cutting points for the defence. First, on
> publication status: **both have peer-reviewed versions** — Corsi et al. at ATVA 2025 and ProSh
> as a 3-page AAMAS 2026 extended abstract, both confirmed on 17 Nov. My preprint-only reading of
> the two rows is withdrawn in full. The remaining nuance is that ProSh's peer-reviewed form is a
> short abstract whose full method sits in the arXiv manuscript, so cite both; Matrix A grades them "strong competitor" alongside peer-reviewed work, and a
> reviewer will separate the two categories. Second, **CAP, Ghaleb and Kim are all out-of-domain**
> (LLM/VLM risk management, robot manipulation, clinical triage), and the one confirmed maritime
> competitor, Vaaler et al., operates on a vessel's **control actions** rather than on advice to a
> person. So no competitor yet shares the maritime *advisory* setting. That is not a weakness in
> the comparison — it is the normal shape of method prior art — but the defence should state it
> as a difference in level of intervention, which is defensible, rather than let a reviewer reach
> for domain novelty, which is not.

---

## What is still missing?

We have enough Scopus AI synthesis material for a **preliminary literature review and research-gap matrix**. We do not yet have enough primary-paper analysis to defend the originality claims with high confidence.

The most important remaining evidence is:

1. Full algorithms, assumptions, guarantees, and baselines from the closest five or six technical studies.
2. Independent reference criteria for judging whether recommendations are actually appropriate or unsafe.
3. A precise definition of the new computational mechanism proposed for RQ3.
4. Evidence showing why that method is not equivalent to existing robust shielding, risk-adaptive authorization, or conservative fallback.

---

## Overall academic judgment

| Dimension | Assessment |
| --- | --- |
| Literature landscape | Well mapped |
| Research motivation | Defensible |
| Experimental feasibility | Generally high |
| PhD-level technical originality | Not yet established |
| Two journal publication directions | Plausible, provisional |

For proposal defence, the most important question is no longer whether a graduated risk-gated architecture can be implemented. It can.

The question is **what new Computer Science knowledge or method we can establish through that architecture that existing research has not already provided**.

This matrix is the working foundation for that argument.
