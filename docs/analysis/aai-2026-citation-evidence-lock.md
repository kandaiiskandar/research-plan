# AAI 2026 — Citation and Evidence Lock

**Date:** 2026-09-23
**Status:** Verification only. No manuscript prose drafted. No locked element changed.
**Governed by:** `aai-2026-locked-research-chain.md` (claims) · `aai-2026-manuscript-architecture.md` (what literature is needed).

> **Verification convention used throughout:** *VERIFIED FROM FULL TEXT* vs *VERIFIED FROM PRIMARY METADATA* vs *UNVERIFIED — DO NOT CITE YET*. No page number, DOI, edition or section identifier appears below unless it was read from a primary source.

---

## A. Critical-source verification

### A.1 NIST AI RMF — ⚠️ **PARTIALLY SUPPORTED as originally worded**

**Bibliographic — VERIFIED FROM FULL TEXT** (`nvlpubs.nist.gov`)

| Field | Value |
|---|---|
| Title | *Artificial Intelligence Risk Management Framework (AI RMF 1.0)* |
| Publication | **NIST AI 100-1** |
| Organisation | National Institute of Standards and Technology, U.S. Dept. of Commerce |
| Date | January 2023 |
| DOI | **10.6028/NIST.AI.100-1** |
| MEASURE location | **§5.3, pp. 28–30**; categories MEASURE 1 (1.1–1.3), 2 (2.1–2.13), 3 (3.1–3.3), 4 (4.1–4.3) |

**A. What MEASURE actually says** — verbatim:
> *"The MEASURE function employs quantitative, qualitative, or mixed-method tools, techniques, and methodologies to analyze, assess, benchmark, and monitor AI risk and related impacts."*

On operation, verbatim:
> *"AI systems should be tested before their deployment and regularly while in operation."*
> *"The functionality and behavior of the AI system and its components…are monitored when in production."*

**B. What it refers to.** **Risk and related impacts**, plus system functionality, behaviour and performance in deployed contexts. 🔴 **It does not say that declared *controls* must be measured for operational effect.** That is the specific step our positioning wanted from it.

**C. Can it support the positioning?** Partially. It supports *measurement and monitoring in operation are called for*. It does not supply *controls must be shown to change system behaviour*.

**D. 🔴 Wording that would OVERSTATE NIST:**
- ✗ "NIST requires that governance controls be measured for operational effect"
- ✗ "NIST mandates measurement of whether declared risk levels change system behaviour"
- ✗ "the MEASURE function requires control-effectiveness evidence"
- ✗ any use of "requires" — the framework is voluntary and uses *should*

**✅ SAFE WORDING (locked):**
> *"The NIST AI Risk Management Framework directs that AI systems be tested before deployment and regularly while in operation, and that AI risks and related impacts be analysed, benchmarked and monitored [ref]."*

Then the paper's own step, **unattributed to NIST**: *whether a declared governance level changes what a system is permitted to do is a property that can likewise be measured rather than assumed.*

**Classification: PARTIALLY SUPPORTED** — supported for the measurement-in-operation premise; **not** supported for control-effectiveness. 🔒 **LOCKED with narrowed wording.**

### A.2 ASTM F3269 — ✅ SUPPORTED

**Bibliographic — VERIFIED FROM PRIMARY METADATA** (ASTM store record). 🔴 **Not verified from full text** — the standard is paywalled.

| Field | Value |
|---|---|
| Designation | **ASTM F3269-21** |
| Title | *Standard Practice for Methods to Safely Bound Behavior of Aircraft Systems Containing Complex Functions Using Run-Time Assurance* |
| Edition | 2021 (supersedes F3269-17) |
| Publisher | ASTM International, West Conshohocken, PA |
| DOI | **10.1520/F3269-21** |

**C/D. What it establishes.** An architectural framework for Run-Time Assurance: a set of RTA system components, requirements for determining safe boundaries and coverage, enabling use of functions for which conventional DO-178/DO-254 assurance artefacts may be unobtainable. It **does** support the statement that the behaviour of a complex function can be bounded by an independently assured monitoring architecture — that is the standard's title and scope.

**E. Is "runtime assurance" accurate?** ✅ Yes — it is the standard's own term.

**F. 🔴 What we must NOT claim:**
- ✗ Any specific section, clause or requirement number — **not read from full text**
- ✗ That our architecture conforms to F3269, is assessed against it, or implements it
- ✗ That F3269 covers advisory systems, human-facing decision support, or environmental conditioning — its scope is aircraft systems, developed with UAS in mind
- ✗ Any quotation beyond the title and the publicly published scope

🔒 **LOCKED — for the concession only.** Cite by title and designation; make no clause-level claim.

### A.3 Alshiekh et al. 2018 — ✅ SUPPORTED, with one term rejected

**⚠️ Verification conflict, resolved.** A fetch of the AAAI camera-ready PDF returned *"the paper does not define or use the terms 'preemptive shielding' or 'post-posed shielding'"* and described only post-selection substitution. A fetch of the arXiv full text (1708.08611) returned both definitions with section numbers. **The arXiv full-text read is definitive; the PDF read was incomplete.** Recorded here because the earlier discovery reports relied on a partial read.

**Bibliographic — VERIFIED FROM FULL TEXT**

| Field | Value |
|---|---|
| Authors | M. Alshiekh, R. Bloem, R. Ehlers, B. Könighofer, S. Niekum, U. Topcu |
| Title | *Safe Reinforcement Learning via Shielding* |
| Venue | Proc. 32nd AAAI Conference on Artificial Intelligence (AAAI-18) |
| Year | 2018 |
| Pages | **2669–2678** |
| Preprint | arXiv:1708.08611 |

**Definitions — verbatim:**
- **Preemptive shielding (§5.1):** *"At every time step t, the shield computes a set of all safe actions {a_t^1, …, a_t^k}, i.e., it takes the set of all actions available, and removes all unsafe actions"* — the restricted list is provided **before the agent selects**.
- **Post-posed shielding (§5.2):** *"The shield monitors the actions of the agent, and substitutes the selected actions by safe actions whenever this is necessary to prevent"* — correction **after selection**.

**What the shield restricts:** the **set of actions available for selection**. The agent's own computation is untouched.

**Assessment of our planned wording:**

| Wording | Verdict |
|---|---|
| "preemptive restriction of an admissible action set" | ✅ **SUPPORTED** — their mechanism, their term |
| "restriction of available actions before the agent selects" | ✅ **SUPPORTED** — near-verbatim |
| **"pre-inference restriction"** | 🔴 **MISLEADING — REJECT** |

🔴 **"Pre-inference" must be removed from the manuscript vocabulary.** Alshiekh restrict before **action selection**, not before model inference or a forward pass; the paper contains no description of restricting anything before inference. Using "pre-inference" would retrofit our terminology onto their mechanism — exactly what the task forbids — and would also assert something about our own system that the evaluation never tests (locked chain limitation L1: no model is exercised).

🔒 **LOCKED.** Add *pre-inference* to the §14 AVOID list of the manuscript architecture. Use **"before the agent selects an action"** or **"preemptive"**.

### A.4 Manski — **NOT REQUIRED (Option 3)**

**A. Most relevant source if used.** Manski, *Nonparametric Bounds on Treatment Effects*, American Economic Review 80(2), 1990, pp. 319–323. **VERIFIED FROM PRIMARY METADATA** only.

**B. Is our situation truly partial identification?** ⚠️ **Not in the technical sense.** Partial identification concerns identifying a *set* of parameter values consistent with observed data when point identification fails, typically from selection or missing outcomes, under a sampling model. Our situation has **no sampling model, no estimand and no inference** — the evaluation is a deterministic census (report limitation 8: *"no p-values, confidence intervals or significance tests apply"*).

**C. Is "directional bound" defensible?** ✅ Yes, as plain description. It is not a term of art being borrowed.

**D. Are we using Manski too broadly?** ⚠️ **Yes.** The bound here is an arithmetic consequence: `f` aggregates by maximum severity, `max` is monotone non-decreasing in each argument, the excluded component is held at its least-severe value, therefore the computed severity is a lower bound. Invoking partial-identification theory for `max(a, b) ≥ max(a, min b)` is heavier machinery than the claim needs, and invites a reviewer to observe that there is no identification problem to solve.

**E. Clearer without Manski?** ✅ **Yes, decisively.**

🔒 **DECISION — OPTION 3: do not cite Manski.** State the bound as a direct consequence of monotone aggregation, in one sentence. This is shorter, unimpeachable, frees a reference slot in a 6-page budget, and removes a framing a reviewer could contest.

**Locked wording:**
> *"Because the classifier aggregates component severities by maximum and the excluded component can only raise severity, holding it at its least-severe value yields a lower bound on every reported figure."*

**Chain impact: none.** The locked chain requires the *lower-bound claim*, which stands on monotonicity alone; Manski appeared in the chain's concession list, and not citing a source is not claiming novelty over it. **This is a wording calibration, not a chain change.** *Fallback:* if a reviewer challenges the bound's framing, Manski can be added at revision as conceptual precedent (Option 2).

### A.5 TSO-C151c — **DROP**

FAA AC 20-151C already establishes advisory-type inhibition conditioned on externally measured state, which is the entire job of the concession. TSO-C151c would add a distinct nuance — inhibition triggered by *input validity* rather than by external state — which is **not a claim the manuscript makes**. It has no corpus note and no verified bibliographic record in this project. Under the §3 rule (*every source must have a job*), it has none.

🔒 **DROP.** Frees one reference slot.

---

## B. Gap-B falsification result

**Gap B under test:** *no empirical characterisation was identified of how often an intermediate advisory-scope governance level changes the admissible recommendation set relative to a participation-only gate, when replayed over a multi-year environmental record.*

Searches run across: graduated advisory scope · state-conditioned admissible action sets · runtime governance levels · action-set contraction · advisory inhibition · multi-level runtime assurance · governance activation frequency · shielding activation frequency · safety-filter intervention frequency.

### Closest candidates

**1. *The Safety Filter: A Unified View of Safety-Critical Control in Autonomous Systems* (Annual Reviews)**
- *Measures:* a unifying technical structure across safety-filter classes.
- *Does not measure:* intervention frequency empirically over an operational record; no graduated or multi-level filter that partially restricts an action set — the treatment is binary intervene / do-not-intervene.
- **Invalidates Gap B? NO.**

**2. *Mission-Level Runtime Assurance Framework for Autonomous Driving* (arXiv:2606.06996)** — the closest found.
- *Measures:* mission success under faults (0.44 → 0.73), per-episode fallback counts (5.43 ± 1.21), detection rate (0.59 ± 0.09), false-rejection rates; compares six complete configurations.
- *Does not measure:* activation frequency over an extended operational record (counts are per-episode); and it **does not disable individual levels within a multi-level stack to isolate a level's marginal contribution** — there is no two-level versus three-level comparison holding other factors constant. The nearest ablation varies prediction horizon, not architectural layers.
- **Invalidates Gap B? NO — and it is instructive:** it confirms that multi-level RTA work reports *whether the stack works*, not *what the intermediate level adds*.

**3. Shielding literature (Alshiekh 2018; probabilistic and adaptive shielding)**
- *Measures:* safety violations, learning performance, convergence.
- *Does not measure:* how often the shield's restriction binds, as a characterisation in its own right, against an unshielded-but-gated baseline.
- **Invalidates Gap B? NO.**

🔒 **GAP B: SURVIVES FALSIFICATION.** No located work isolates an intermediate governance level's marginal contribution against a participation-only baseline, nor reports its activation frequency over a multi-year record. The gap remains narrow and correctly scoped to *"within the reviewed literature"*.

---

## C. Responsible AI positioning calibration

**Intended claim:** *"Responsible AI principles and governance commitments are more commonly specified than their operational effects are measured."*

**What the systematic review actually reports** (*AI governance: a systematic literature review*, AI & Ethics, 2024) — verbatim:
- *"ethical guidelines are merely 'suggestions' with no enforceable regulations to ensure compliance, leading to ethical principles being either overlooked or poorly integrated into AI systems"*
- *"except for study [A11], these studies lack real-world implementation details"*
- frameworks *"exhibit a potential limitation in terms of proper structure and validation"*
- *"Only 3 studies have provided all the answers to questions (who is governing, what is being governed, when it is being governed, and how it is being governed)"*

**Our interpretation vs the review.** The review documents an **implementation-and-validation** gap: frameworks lack real-world implementation detail and validation. It does **not** state that operational *effects* go unmeasured — that is our extrapolation, and it is one step further than the evidence.

⚠️ **Classification: PARTIALLY SUPPORTED as worded.**

**✅ LOCKED CONSERVATIVE WORDING:**
> *"Reviews of AI governance report that published frameworks frequently lack real-world implementation detail and validation [ref]. Risk-management guidance correspondingly directs that AI systems be tested before deployment and monitored while in operation [ref]."*

Then the paper's own inference, stated as the authors' own and attributed to neither source:
> *"Whether a declared governance level changes what a system is permitted to do is, on this view, a property to be measured rather than assumed."*

🔒 **The research gap is unchanged.** This calibrates only the sentence that introduces it.

---

## D. Criterion-literature calibration

**Criterion:** *a declared risk level changes governance behaviour only if it changes the admissible action set.*

**Source — from the project's own verified extraction of Parasuraman, Sheridan & Wickens (2000)**, metadata verified against Crossref for DOI 10.1109/3468.844354: *IEEE Trans. Systems, Man, and Cybernetics — Part A*, vol. 30, no. 3, pp. 286–297.

**What it supports — DIRECT:**
> *"The paper is explicit that a system cannot have a single overall level of automation; a level is always stated relative to a specific function."*

That is direct support for **levels are individuated by the function they apply to, not by a single overall label**.

### 🔴 A broader concession is required than the architecture currently makes

The same verified note records Parasuraman's levels 2–4:

| Level | Content |
|---|---|
| 2 | the computer *"offers a complete set of decision/action alternatives"* |
| 3 | the computer *"narrows the selection down to a few"* |
| 4 | the computer *"suggests one alternative"* |

The project's own note concludes: *"Levels 2–4 are the sharpest historical precedent for graduated restriction of what an automated system presents to a human… the claim belongs to the original."*

**Consequence.** Levels 2–4 are **graduated contraction of the alternative set offered to a human** — structurally the same move as `A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅`. 🔒 **The manuscript must concede this explicitly**, not merely cite Parasuraman for the individuation point.

**What remains ours** (also from the note): Parasuraman's model is **design-time**, assigns levels per function by design decision, and **has no state variable** — it does not prescribe runtime switching conditioned on external state, and it measures nothing. Our addition is that the contraction is **conditioned on a runtime external state** and its **activation frequency is measured**.

**Relationship classification:**
- *Levels individuated by function, not label* → **DIRECT SUPPORT**
- *Graduated contraction of the set offered to a human* → **DIRECT SUPPORT — must be conceded**
- *Our exact admissible-set criterion for governance designs* → **CONCEPTUAL PRECEDENT**, not direct support

**✅ SAFE MANUSCRIPT WORDING (locked):**
> *"Graduated restriction of the alternatives an automated system presents to a human is long established: the canonical levels-of-automation model distinguishes offering a complete set of alternatives, narrowing it, and suggesting one, and holds that a level is always stated relative to a specific function rather than as a single overall label [ref]. That model is design-time and defines no runtime state variable. We restate the individuation point as an explicit criterion on admissible sets and measure how often a state-conditioned contraction binds."*

🔴 **Do NOT write** that Parasuraman states our criterion, or that graduated contraction of offered alternatives is new. **Gap B is unaffected** — Parasuraman measures no activation frequency and has no state variable.

---

## E. Claim-to-citation matrix

| # | Manuscript claim | Source | Exact support | ✅ Safe wording | 🔴 Overclaim to avoid |
|---|---|---|---|---|---|
| 1 | Responsible AI measurement positioning | AI-governance SLR + NIST AI 100-1 | SLR: frameworks "lack real-world implementation details" and proper "validation". NIST: test before deployment and "regularly while in operation"; analyse/benchmark/monitor "AI risk and related impacts" | "Reviews report frameworks frequently lack implementation detail and validation; risk-management guidance directs testing before deployment and monitoring in operation" | ✗ "NIST requires controls to be measured for effect" ✗ "the literature shows governance controls are never measured" |
| 2 | Runtime assurance is established | ASTM F3269-21 | Title and scope: methods to safely bound behaviour of systems containing complex functions using run-time assurance | "Bounding the behaviour of a complex function with an independently assured run-time architecture is standardised practice in aviation [ref]" | ✗ any clause/section number ✗ conformance ✗ that it covers advisory or human-facing systems |
| 3 | Shielding is established | Alshiekh et al. 2018 §5.1–5.2 | Preemptive: shield "takes the set of all actions available, and removes all unsafe actions" before selection. Post-posed: substitutes after selection | "Restricting the set of actions available to an agent before it selects, rather than correcting afterwards, is established as preemptive shielding [ref]" | 🔴 ✗ **"pre-inference"** ✗ "before model inference" ✗ that the agent's computation is restricted |
| 4 | Advisory inhibition is established | FAA AC 20-151C | Advisory-type inhibition conditioned on externally measured state, in certified avionics | "Advisory types are progressively inhibited as an externally measured state worsens in certified collision-avoidance avionics [ref]" | ✗ that our thresholds derive from it ✗ that it governs AI |
| 5 | Levels individuated by function allocation | Parasuraman et al. 2000 | "a system cannot have a single overall level of automation; a level is always stated relative to a specific function" | See §D locked wording | ✗ that it states our admissible-set criterion |
| 5b | **Graduated contraction of offered alternatives is established** | Parasuraman et al. 2000, levels 2–4 | "offers a complete set of decision/action alternatives" → "narrows the selection down to a few" → "suggests one alternative" | Concede explicitly; note it is design-time with no state variable | 🔴 ✗ presenting contraction of the offered set as our idea |
| 6 | Graduated governance topology exists | Flehmig et al. 2024 | Multi-level governance conditioned on AI degradation | "C3 ports this topology onto an environmental conditioning variable" + fairness note | ✗ that their framework is deficient ✗ that we reproduce or test their system |
| 7 | Lower-bound interpretation | **None — arithmetic** | Monotone max aggregation; excluded component held at least-severe value | "Because the classifier aggregates by maximum severity and the excluded component can only raise severity, every reported figure is a lower bound" | ✗ "partial identification" ✗ "bounds" as a statistical estimand ✗ any CI language |
| 8 | Wave threshold | Yaakob et al. 2015 | Operational ceiling for small vessels; source also admits a failure-point reading | "Threshold traced to [ref]; the source admits two readings, giving 5.81% and 9.22%" | ✗ that the threshold is validated or optimal |
| 9 | Wind / rain thresholds | MET Malaysia ×2; JPS/DID | Wind Cat 1/2 onsets; thunderstorm rainfall criterion; DID light-rainfall limit | "Four boundaries trace to named authorities; the CAUTION rainfall boundary is sourced but non-MET, as MET publishes no criterion below 20 mm/hr" | ✗ that any boundary is an official fishing-safety limit |
| 10 | Time boundary | COLREGs Rule 20(b) | Sunset-to-sunrise navigation-light requirement | "The boundary is taken from [ref]; the abstention policy at night is researcher-defined" | 🔴 ✗ that COLREGs requires AI abstention |
| 11 | Environmental data sources | Zippenfenig 2023; Hersbach et al. 2023 | API and ERA5 reanalysis | Standard data citation | ✗ that reanalysis equals observation |
| 12 | ~~Previously reported figures~~ → **Provenance of the headline figures** | 🔴 **NO CITATION** — the earlier abstract is accepted but not confirmed published | — | Report the figures as outputs of the evaluation described in this paper, reproduced from canonical scripts. Make no statement about when they were first computed | 🔴 ✗ "previously published / previously reported / prior publication" ✗ inventing a proceedings citation ✗ presenting earlier-developed material as newly created for AAI |

---

## F. Final bibliography

**[1]** AUTHORS: *(SLR author list — see note)* · TITLE: AI governance: a systematic literature review · VENUE: AI and Ethics (Springer) · YEAR: 2024 · DOI: 10.1007/s43681-024-00653-w · PURPOSE: implementation-and-validation gap (claim 1) · **REQUIRED** · VERIFIED FROM FULL TEXT (content); ⚠️ **author list to be taken from the corpus note before drafting**

**[2]** AUTHORS: National Institute of Standards and Technology · TITLE: Artificial Intelligence Risk Management Framework (AI RMF 1.0) · ORG: NIST, U.S. Dept. of Commerce, NIST AI 100-1 · YEAR: 2023 · DOI: 10.6028/NIST.AI.100-1 · PURPOSE: measurement/monitoring in operation (claim 1) · **REQUIRED** · **VERIFIED FROM FULL TEXT**

**[3]** ORG: ASTM International · TITLE: Standard Practice for Methods to Safely Bound Behavior of Aircraft Systems Containing Complex Functions Using Run-Time Assurance · DESIGNATION: ASTM F3269-21 · YEAR: 2021 · DOI: 10.1520/F3269-21 · PURPOSE: runtime-assurance concession (claim 2) · **REQUIRED** · **VERIFIED FROM PRIMARY METADATA** — 🔴 no clause-level claim permitted

**[4]** AUTHORS: M. Alshiekh, R. Bloem, R. Ehlers, B. Könighofer, S. Niekum, U. Topcu · TITLE: Safe Reinforcement Learning via Shielding · VENUE: Proc. 32nd AAAI Conf. on Artificial Intelligence (AAAI-18) · YEAR: 2018 · PAGES: 2669–2678 · PREPRINT: arXiv:1708.08611 · PURPOSE: shielding concession (claim 3) · **REQUIRED** · **VERIFIED FROM FULL TEXT** · ⚠️ DOI not established — cite by proceedings

**[5]** AUTHORS: Federal Aviation Administration · TITLE: Airworthiness Approval of Traffic Alert and Collision Avoidance Systems (TCAS II), AC 20-151C · PURPOSE: advisory-inhibition concession (claim 4) · **REQUIRED** · VERIFIED — corpus note

**[6]** AUTHORS: R. Parasuraman, T. B. Sheridan, C. D. Wickens · TITLE: A model for types and levels of human interaction with automation · VENUE: IEEE Trans. Systems, Man, and Cybernetics — Part A · YEAR: 2000 · VOL/PP: 30(3), 286–297 · DOI: 10.1109/3468.844354 · PURPOSE: criterion precedent **and** graduated-contraction concession (claims 5, 5b) · **REQUIRED** · VERIFIED — corpus note, metadata Crossref-checked

**[7]** AUTHORS: N. Flehmig, M. A. Lundteigen, S. Yin · TITLE: Implementing Artificial Intelligence in Safety-Critical Systems during Operation: Challenges and Extended Framework for a Quality Assurance Process · VENUE: IECON 2024 · YEAR: 2024 · DOI: 10.1109/IECON55916.2024.10906021 · PURPOSE: C3 provenance (claim 6) · **REQUIRED** · VERIFIED — corpus note + EA reference list

**[8]** AUTHORS: O. Yaakob, F. E. Hashim, M. R. Jalal, M. A. Mustapa · TITLE: Stability, seakeeping and safety assessment of small fishing boats operating in southern coast of Peninsular Malaysia · VENUE: J. Sustainability Science and Management · YEAR: 2015 · VOL/PP: 10(1), 50–65 · PURPOSE: wave threshold + two readings (claim 8) · **REQUIRED** · VERIFIED — corpus note + EA reference list

**[9]** ORG: Malaysian Meteorological Department · TITLE: Kriteria Amaran Angin Kencang dan Laut Bergelora · PURPOSE: wind boundaries (claim 9) · **REQUIRED** · VERIFIED — EA reference list

**[10]** ORG: Malaysian Meteorological Department · TITLE: Kriteria Amaran Ribut Petir · PURPOSE: rainfall UNSAFE boundary (claim 9) · **REQUIRED** · VERIFIED — EA reference list

**[11]** ORG: Department of Irrigation and Drainage Malaysia · TITLE: Categorization of Rainfall Intensity, Public Infobanjir · PURPOSE: rainfall CAUTION boundary, non-MET (claim 9) · **REQUIRED** · VERIFIED — EA reference list

**[12]** ORG: International Maritime Organization · TITLE: Convention on the International Regulations for Preventing Collisions at Sea (COLREGs), Rule 20(b) · PURPOSE: time boundary (claim 10) · **REQUIRED** · VERIFIED — EA reference list

**[13]** AUTHOR: P. Zippenfenig · TITLE: Open-Meteo.com Weather API · YEAR: 2023 · DOI: 10.5281/zenodo.7970649 · PURPOSE: data source (claim 11) · **REQUIRED** · VERIFIED — EA reference list

**[14]** AUTHORS: H. Hersbach et al. · TITLE: ERA5 hourly data on single levels from 1940 to present · VENUE: Copernicus CDS · YEAR: 2023 · DOI: 10.24381/cds.adbb2d47 · PURPOSE: reanalysis source (claim 11) · **REQUIRED** · VERIFIED — EA reference list

**~~[15]~~ REMOVED 2026-09-23** — IPoSCI extended abstract, *A Graduated Safety-State-Gated Architecture for AI Decision Support in Low-Resource Coastal Fisheries*. 🔴 **ACCEPTED but NOT CONFIRMED PUBLISHED.** No stable, citable proceedings version exists, so it is not cited and is never described as published prior work. It remains an **internal provenance constraint** on drafting. **Re-check before submission:** if formally published, reinstate with the proceedings citation and an explicit relationship sentence; if not, invent no citation and follow the AAI/IEEE policy for accepted-but-unpublished related work. ⚠️ Disclose instead in the submission form or cover letter.

**[16]** AUTHORS: M. Shamsujjoha, Q. Lu, D. Zhao, L. Zhu · TITLE: Swiss Cheese Model for AI Safety: A Taxonomy and Reference Architecture for Multi-Layered Guardrails of Foundation Model Based Agents · VENUE: IEEE ICSA 2025, pp. 37–48 · DOI: 10.1109/ICSA65012.2025.00014 · PURPOSE: multi-layer guardrail concession · **SHOULD KEEP** · VERIFIED — corpus + EA

**[17]** AUTHORS: *(see corpus note)* · TITLE: The Road to Safe Automated Driving Systems: A Review of Methods Providing Safety Evidence · PURPOSE: fail-safe / MRC concession · **DROP IF SPACE** · VERIFIED — corpus note

**[18]** TITLE: *(contemporary shielding — e.g. Probabilistic Shielding for Safe Reinforcement Learning)* · PURPOSE: supports [4] · **DROP IF SPACE** · VERIFIED — corpus note

**[19]** AUTHORS: Y. Jeong, N. Im · TITLE: Proposal of restrictions on the departure of Korea small fishing vessel according to wave height · VENUE: J. Marine Science and Engineering, 11(7), 1302 · YEAR: 2023 · DOI: 10.3390/jmse11071302 · PURPOSE: vessel-dependent wave restriction · **DROP IF SPACE** · VERIFIED — EA reference list

**[20]** TITLE: *(runtime verification / totality — corpus candidate)* · PURPOSE: P1 totality, one sentence · **DROP IF SPACE** · ⚠️ **UNVERIFIED for this purpose — select and verify before use**

### Removed

| Source | Reason |
|---|---|
| **Manski (1990/1997); Manski & Pepper (2000)** | §A.4 Option 3 — the bound follows from monotone aggregation; partial-identification framing is heavier than the claim and technically inapt for a deterministic census |
| **TSO-C151c** | §A.5 — AC 20-151C already carries the concession; no distinct necessary claim; no verified record |
| Simplex (Sha) | Subsumed by [3]; no distinct claim in a 6-page paper |
| Puterman / MDP `A(s)` | No manuscript claim depends on it; the criterion is sourced to [6] |
| Selective prediction / reject-option | Analogous but confidence-triggered; correct treatment costs a paragraph the budget cannot fund |
| EU AI Act, ISO/IEC 42001, ISO/IEC 23894 | Applicability unestablished; invites scope questions |
| Indykov et al.; Hevner et al.; Gao; Rahim et al. | No job in this manuscript |

**Count: 14 REQUIRED · 1 SHOULD KEEP · 4 DROP IF SPACE → 15–19 references.** ⚠️ Revised 2026-09-23: [15] removed. Within the 20–24 target, at the lean end. ✅

---

## G. Page-1 concession package

**Establishes only:** *mechanisms for state-conditioned restriction already exist.* Nothing more. Three claims, ~110 words in the eventual draft.

**CLAIM 1 — Bounding a complex function at runtime is standardised practice.**
- *Source:* [3] ASTM F3269-21.
- *Safe wording:* "Bounding the behaviour of a system containing complex functions by an independently assured run-time architecture is established aviation practice, and is standardised."
- *Limits:* title-level only; no clause number; no conformance claim.

**CLAIM 2 — Restricting the available action set before selection is established.**
- *Source:* [4] Alshiekh et al. 2018, §5.1.
- *Safe wording:* "In safe reinforcement learning, a shield may compute the set of safe actions and remove unsafe ones before the agent selects, rather than correcting the action afterwards."
- *Limits:* 🔴 never "pre-inference"; never "before model inference".

**CLAIM 3 — Advisory-type inhibition conditioned on external state is established, including graduated contraction of what is offered to a human.**
- *Sources:* [5] FAA AC 20-151C; [6] Parasuraman et al. 2000, levels 2–4.
- *Safe wording:* "Certified collision-avoidance avionics progressively inhibit advisory types as an externally measured state worsens, and the canonical levels-of-automation model already describes graduated contraction of the alternatives presented to a human."
- *Limits:* concede the contraction itself; note only that the automation model is design-time and defines no runtime state variable.

**Closing sentence of P2 — mandatory:**
> *"This paper contributes none of these mechanisms."*

🔒 **PAGE-1 CONCESSION: READY.**

---

## H. Sources removed

Manski · TSO-C151c · Simplex (Sha) · Puterman · selective prediction / reject-option · EU AI Act · ISO/IEC 42001 · ISO/IEC 23894 · Indykov et al. · Hevner et al. · Gao (2024) · Rahim et al. (2024). Each removed under the §3 rule: no necessary manuscript claim depends on it.

🔴 **Removed 2026-09-23 for a different reason — [15] IPoSCI extended abstract.** Not removed because no claim needs it, but because **it is accepted and not confirmed published**, so no stable citable version exists. This is a status removal, not a relevance removal: if it is published before submission it must be reinstated and the relationship disclosed.

---

## I. Remaining unresolved items

| # | Item | Severity | Action before drafting |
|---|---|---|---|
| 1 | **[1] author list** for the AI-governance SLR not captured | 🟠 Medium | Read from the corpus note `AI governance- a systematic literature review.md` |
| 2 | **[17] author list** for the automated-driving review not captured | 🟢 Low | Read from corpus note, or drop |
| 3 | **[20] runtime-verification source** not selected | 🟢 Low | Select and verify, or omit the P1 sentence entirely |
| 4 | **[4] DOI** not established | 🟢 Low | Cite by proceedings and pages — standard for AAAI |
| 5 | **[3] full text not read** | 🟠 Medium | Acceptable: title-and-scope citation only. 🔴 Do not add clause numbers later |
| 6 | 🔴 **IPoSCI publication status** — accepted, not confirmed published | 🔴 **High** | **Re-check immediately before submission.** Published → add proceedings citation + relationship sentence. Not published → no citation; disclose in the submission form/cover letter |
| 7 | **Corpus notes missing** for NIST AI RMF, ASTM F3269, Alshiekh et al. | 🟢 Low | Bibliographic details are locked above; create notes for the record |
| 8 | Architecture §14 AVOID list lacks **"pre-inference"** | 🟠 Medium | Add — §A.3 |
| 9 | Architecture §5 cluster C understates the Parasuraman concession | 🟠 Medium | Broaden to include levels 2–4 — §D |

**None blocks drafting.** Items 1–4 are lookups; 8 and 9 are wording corrections recorded here and binding on the drafting agent.

---

NIST AI RMF: **LOCKED** — with narrowed wording; supports measurement and monitoring in operation, **not** control-effectiveness.

ASTM F3269: **LOCKED** — F3269-21, DOI 10.1520/F3269-21, verified from primary metadata; title-and-scope citation only, no clause-level claim.

ALSHIEKH 2018: **LOCKED** — AAAI-18, pp. 2669–2678; preemptive (§5.1) and post-posed (§5.2) verified from full text; 🔴 the term **"pre-inference" is rejected as misleading** and must not appear.

MANSKI: **NOT REQUIRED** — Option 3 adopted; the lower bound follows directly from monotone severity aggregation, which is shorter, unimpeachable and frees a reference slot.

TSO-C151c: **DROP** — AC 20-151C already carries the concession; no distinct necessary claim.

GAP B: **SURVIVES FALSIFICATION** — the closest candidate (mission-level RTA) reports per-episode fallback counts and compares complete configurations, but performs no hierarchical isolation of a level's marginal contribution and no activation-frequency characterisation over an extended record.

PAGE-1 CONCESSION: **READY** — three claims, sources [3], [4], [5], [6], with the mandatory closing sentence *"This paper contributes none of these mechanisms."*

REFERENCE PACKAGE: **READY** — 14 required, 1 should-keep, 4 droppable; 15–19 references against a 20–24 target. [15] removed 2026-09-23 on publication status.

IPoSCI CITATION: **REMOVED — DO NOT CITE.** Accepted but not confirmed published. Not described as published, previously published, previously reported, or a prior publication. Retained as an internal provenance constraint; disclosed via the submission form or cover letter; **status to be re-checked immediately before submission.**

MANUSCRIPT DRAFTING: **READY**

---

*Citation and evidence lock complete. No manuscript prose drafted. No locked research-chain element changed; §§A.4, C and D are wording calibrations recorded as binding on the drafting agent. Revised 2026-09-23: reference [15] removed on IPoSCI publication status — see locked chain §0, I-6.*
