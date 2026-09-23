# RQ Redesign and Conference Narrative Freeze — AMICT Conference Rebuild

**Date:** 2026-09-14
**Task:** `docs/tasks/AMICT RQ REDESIGN AND CONFERENCE NARRATIVE FREEZE.md`
**Prerequisite gates:** `NOVELTY_AUDIT = STOP_MATERIAL_EQUIVALENCE_FOUND` · `SOURCE_CORPUS_VALIDATION = CLOSED` · `CONTRIBUTION_FREEZE_V2 = CLOSED`
**Companion artefact:** [`rq-evidence-map.csv`](rq-evidence-map.csv)
**Binding on:** conference outline · manuscript drafting · claim-evidence audit

---

## 1. Executive verdict

    RQ_NARRATIVE_FREEZE = CLOSED
    RQ_COUNT            = 3

Three RQs frozen, mapping one-to-one onto the frozen contributions. The narrative, gap statement, novelty-positioning sentence, evidence hierarchy and section strategy are frozen. Title reconfirmed.

    STOP_CONDITION_9 = MANAGED_NOT_FIRED

The six-page story fits, **but only on the lower bound of every section band, with visual material capped at three items.** §12.3 sets out the arithmetic in full, including the scenarios that do not fit. The overflow is not hidden; it is converted into a drafting constraint and a named reserve.

---

## 2. Final RQ1

> **RQ1.** How can graduated advisory-scope governance be specified and verified operationally, separating AI participation from admissible advisory scope under incomplete, stale or excluded environmental observations?

**Contribution:** C1. **Claim types:** FORMAL, with IMPLEMENTATION_FIDELITY supporting the "verified" clause.

---

## 3. Final RQ2

> **RQ2.** How often does graduated advisory-scope governance produce governance outcomes that differ from participation-only governance in retrospective environmental replay?

**Contribution:** C2. **Claim type:** EMPIRICAL_TRACE.

Audited for wording defects; none found. Frozen unchanged from the direction carried through the contribution freeze.

---

## 4. Final RQ3

> **RQ3.** How does the measured governance-outcome divergence differ under the alternative environmental-data configuration?

**Contribution:** C2. **Claim type:** EMPIRICAL_TRACE.

---

## 5. RQ design rationale

### 5.1 RQ1 — why this wording

The previous candidate asked how the governance could be "specified as a **general** runtime governance abstraction … while preserving explicit **containment** properties". Three defects, all now removed:

- **"general"** risked importing domain-independent applicability, which the contribution freeze rejected as an engineering claim.
- **Foregrounding containment** made the question read as a property-novelty claim. Containment, totality and monotonicity are `PASS_WITH_SCOPE` with `PROPERTY_IS_NOVEL = NO`; an RQ built on them would invite exactly the reading the freeze forbids.
- **It omitted the strongest part of C1** — the operational observation-resolution semantics.

The frozen wording foregrounds *operational* specification and the observation conditions (`incomplete, stale or excluded`), which is where the scoped distinction actually lives. It names the participation / advisory-scope separation without asserting that the separation is new.

**"Specify and verify", not "specify".** The specification is accompanied by bounded executable conformance evidence, so the question has a verifiable component and is not answered by construction alone.

**The scope of "verify" is bounded and must be stated wherever RQ1 is expanded:** verification means *formal properties plus bounded implementation conformance*. It does **not** mean deployment validation, real-world effectiveness or safety validation.

Deliberately excluded from the wording: `F_{D,τ}`, `ρ_{D,τ}`, the four ⊥ conditions, declared exclusions, pre-reasoning rule-set supply. These belong in Section III, not in a conference RQ. Forcing them into the question would make it read as an algorithm specification.

### 5.2 RQ2 — why unchanged

"How often" matches the measured quantity exactly: a rate over departure-window hours. "Governance outcomes" is retained verbatim; **safety outcomes**, **decision outcomes**, **risk outcomes** and **effectiveness** are prohibited substitutions. "Retrospective environmental replay" fixes the evidence type and prevents the question being read as a live-deployment claim.

### 5.3 RQ3 — why "differ"

`differ` is the most scientifically accurate of the candidate verbs.

- **"preserved"** — prohibited. Implies robustness, replication or statistical stability.
- **"change"** — implies a process acting on one quantity over time. PRIMARY and RESOLUTION are not a before and an after.
- **"vary"** — carries variance implicature.
- **"differ"** — states that two separately computed quantities are unequal, which is exactly the relationship.

PRIMARY and RESOLUTION are **alternative environmental-data configurations**: different wave models and different record lengths. They are not repeated trials, confidence intervals, uncertainty bounds or independent datasets. `robust`, `stable`, `preserved` and `replicated` are prohibited in RQ3 and in its answering text.

### 5.4 Why three, and why not more

One RQ per contribution, with RQ3 separating the second configuration because E3's mandatory dual-configuration scope is `{E1, E2, E6}` and the configuration comparison is a distinct question rather than a robustness check on RQ2.

No RQ was created for an evidence block merely because the block exists. Explicitly **not** created: a performance/E5 RQ, an implementation-fidelity RQ, a hysteresis RQ, a human-study RQ, a safety-effectiveness RQ, a novelty RQ.

---

## 6. RQ → contribution mapping

| RQ | Contribution | Role |
|---|---|---|
| RQ1 | **C1** — formal operational specification / scoped generalisation | Answered by the specification itself, verified by formal properties and bounded executable conformance |
| RQ2 | **C2** — empirical characterisation | The paper's primary empirical question |
| RQ3 | **C2** — empirical characterisation | Configuration comparison within the same contribution |

Implementation fidelity is **not** an RQ. It is supporting verification for RQ1.

---

## 7. RQ → evidence mapping

Full clause-level mapping in [`rq-evidence-map.csv`](rq-evidence-map.csv).

| RQ | Primary evidence | Supporting evidence | Excluded |
|---|---|---|---|
| RQ1 | Appendix C formalisation: `S = f(E)`, `(G(S), A_AI(S))`, `F_{D,τ} = f ∘ ρ_{D,τ}`, Theorem C.1b operational totality, four ⊥ responses, declared exclusion `D`, `RS(S)` pre-reasoning supply with no post-generation filter | Executable conformance: 292 episodes, 454 advisory records of type `Delay`, F1 = F2 = F3 = 0 | E5, H3, target-hardware timing, human study, cross-domain demonstration |
| RQ2 | ΔL2 = **5.81%** PRIMARY; **C1↔C3 = 0.00%** PRIMARY as control | C0↔C1 = 42.88%, C0↔C2 = 48.69% (PRIMARY context); replay scale 43,848 hourly records | Hysteresis; any safety or effectiveness reading |
| RQ3 | ΔL2 = **4.48%** RESOLUTION | C1↔C3 = 0.00% RESOLUTION as cross-configuration support | C0↔C1 = 41.08% and C0↔C2 = 45.56% — `PROVENANCE_INCOMPLETE`, see §18 |

RQ2 and RQ3 are fully supportable on ΔL2 and C1↔C3 alone. Neither depends on the provenance-incomplete pair.

---

## 8. C1↔C3 control disposition

    C1_C3_PRIMARY_RQ        = RQ2
    C1_C3_SECONDARY_SUPPORT = RQ3

**Primary attribution RQ2.** The result supports the interpretation that the measured ΔL2 difference is associated with **advisory-scope differentiation** rather than with the mere existence of a third labelled governance state. That is a control on the RQ2 claim, and it is what makes ΔL2 interpretable rather than incidental.

**Secondary support RQ3.** The RESOLUTION value (0.00%) is reported alongside ΔL2 RESOLUTION as cross-configuration evidence. RQ3 is not its primary home.

**Frozen interpretation, not to be exceeded:**

> Under the evaluated comparator definitions, adding an intermediate labelled governance state without advisory-scope differentiation produces no admissible-set divergence.

**Prohibited generalisations:** all traffic-light systems are equivalent · all three-state systems add no value · advisory-scope governance is universally superior · any claim about traffic-light or three-state systems in general.

---

## 9. Implementation-fidelity narrative role

    IMPLEMENTATION_FIDELITY = SUPPORTING_VERIFICATION_FOR_RQ1

**Placement: Section III, as a short executable-conformance subsection.** Not a Results subsection, not an RQ, not a headline finding.

**Only allowed core statement:**

> The executable implementation produced zero violations of the configured advisory admissibility contract within the bounded deterministic interface-contract fidelity state space.

**Limitations that must accompany it, without exception:** `R-SAFE-001 = DEFERRED`; the SAFE rule set is empty; all four implemented rules are CAUTION rules; the single generated advisory conclusion type is `Delay`; **454 advisory records, not 454 advisory types**; containment was therefore exercised **on the restrictive side only** — no advisory was generated that a narrower state would have had to suppress.

Bounded figures: 292 primary episodes (32 SAFE, 260 CAUTION), 244 with advisory, 16 CAUTION episodes with no advisory, 162 UNSAFE gate-off cases **outside** the 292 denominator.

---

## 10. Frozen conference narrative

The paper is frozen to this argument order:

1. **Established mechanism precedent** — restriction of the advisory types an automated system may present to a human, conditioned on an externally measured state, is established practice in certified collision-avoidance avionics, and formal verification of state-conditioned advisory logic has precedent.
2. **Unresolved operational formalisation gap in AI governance** — within the reviewed literature, that pattern has not been given an operational treatment combining a classified multi-component environmental state, explicit observation-resolution and exclusion semantics, and a state-conditioned advisory-type admissibility contract.
3. **Formal operational specification** — `S = f(E)` over five component classifiers; the governance pair `(G(S), A_AI(S))`; the operational classifier `F_{D,τ} = f ∘ ρ_{D,τ}`; four distinguished responses to invalid, absent, stale and unmeasured inputs; declared exclusions with lower-bound propagation; admissibility enforced by pre-reasoning rule-set supply rather than post-generation filtering.
4. **Bounded executable conformance** — the specification is executable and the configured contract held across the bounded fidelity state space, on the restrictive side only.
5. **Retrospective empirical characterisation** — how often the intermediate advisory-scope level produces a governance outcome distinct from participation-only governance, under two environmental-data configurations, with a zero-divergence control.
6. **Bounded interpretation and limitations.**

**The paper must not read as:** *literature review → architecture proposal → small evaluation.*
**It must read as:** *known governance pattern → operational formalisation → empirical evaluation.*

**Introduction discipline.** The avionics precedent is acknowledged explicitly and early, in one or two sentences, and then left. The Introduction must not revolve around TCAS; the precedent is the starting point of the argument, not its subject.

---

## 11. Evidence hierarchy

Frozen. **This hierarchy controls page allocation.**

| Tier | Content |
|---|---|
| **PRIMARY SCIENTIFIC EVIDENCE** | C2 empirical replay — ΔL2 under both configurations, C1↔C3 control |
| **SECONDARY SCIENTIFIC CONTRIBUTION** | C1 operational formalisation |
| **SUPPORTING VERIFICATION** | Implementation fidelity |
| **POSITIONING / BACKGROUND** | Original 72-paper structured review; targeted post-review novelty sources; prior-work comparison |
| **OPTIONAL** | Hysteresis |
| **EXCLUDED** | E5 · H3 · human study · target-hardware performance |

**On the ordering.** Contribution numbering (C1 first) and evidence priority (C2 first) deliberately diverge. Numbering is retained for continuity with the contribution freeze; space and prominence follow evidence. The paper was rejected for insufficient empirical evidence, and the empirical contribution is also the one with no equivalent in the validated comparison set — so Results plus Evaluation Method together receive more space than the Formalisation section. **The paper must not become architecture-heavy merely because C1 is numbered first.**

---

## 12. Six-page section strategy

Planning target only. No formatting performed.

### 12.1 Allocation

| § | Section | Words | Purpose | Must keep | Compress | Omit |
|---|---|---|---|---|---|---|
| I | Introduction | 450–550 | Establish precedent, scoped gap, two contributions | Avionics acknowledgement; scoped gap statement; C1 and C2 in one sentence each | Motivation prose; domain background | Extended fisheries framing; governance-maturity digression |
| II | Related Work | 450–550 | Show mechanism precedent exists and locate the scoped remaining gap | **Comparison table** across seven families; three-sentence synthesis | All per-paradigm subsections from v3 | Review methodology; corpus counts in prose; mini-SLR structure |
| III | Operational Governance Formalisation | 750–850 | Deliver C1 | `(G(S), A_AI(S))`; `S = f(E)` five components; `F_{D,τ} = f ∘ ρ_{D,τ}`; four ⊥ responses; declared exclusion + lower bounds; pre-reasoning `RS(S)`, no post-filter; properties **stated** with proof reference | Proofs → statements with a citation to the journal treatment; complexity analysis | Full proof text; algorithm pseudocode; `g_v` history; threshold provenance narrative |
| III.x | — executable conformance | *(within III)* | Verify RQ1's "verify" clause | The single allowed statement + R-SAFE-001, `Delay`-only, restrictive-side-only | Episode breakdown to one sentence | Rule-by-rule activation detail |
| IV | Evaluation Method | 550–650 | Define what was measured and against what | Four comparators C0–C3; two configurations; replay scale; admissible-set divergence metric | Data-provenance narrative | Threshold derivation; solar-artefact detail; prediction-register mechanics |
| V | Results | 900–1,050 | Deliver C2 — **largest allocation** | ΔL2 5.81% / 4.48%; C1↔C3 0.00% / 0.00%; comparator context; results table | Component binding shares to one or two sentences | Hysteresis; `g_w`/`g_r`/`g_m` per-component results beyond the required disclosures |
| VI | Discussion and Limitations | 600–700 | Bounded interpretation + protected disclosures | The full disclosure set (§12.2) | Interpretation prose | External-validity essay; deployment-challenge narrative |
| VII | Conclusion | 180–250 | Restate contributions at their frozen strength | Two contributions; one limitation sentence; future work in one clause | — | Any new claim; any figure restatement |

### 12.2 Protected disclosure budget — 350–550 words

Budgeted as an explicit line item inside §VI, **not** left for Discussion to absorb. Nineteen items, none removable:

R-SAFE-001 deferred · SAFE rule set empty · `Delay`-only generated conclusion type · 454 records not types · containment exercised on the restrictive side only · `D = {m}` · severity figures therefore lower bounds · κ = 0 throughout the replay · rainfall figures therefore lower-bound constrained · `g_w` 2 activations / 0 bindings · `ageᵢ` unparameterised · `reasons` runtime capture unimplemented · cross-domain re-instantiation not demonstrated · PRIMARY and RESOLUTION are alternative configurations, not uncertainty bounds · C1↔C3 bounded to the evaluated comparators · avionics precedent acknowledgement · structured review 72 versus targeted post-review additions · E5/H3 open with no target-hardware evidence · no human study and no human-outcome validation.

Permitted compression: one dense Limitations paragraph; a disclosure column in the results or comparison table; short parenthetical qualifiers beside quantitative claims (for example, *"5.81% of departure-window hours (lower bound; `D = {m}`)"*).

**Disclosures must not be deleted to satisfy page count.** If the budget cannot hold, cut per §12.4 instead.

### 12.3 Budget arithmetic — stated in full

Section bands sum to:

    lower bound   3,880 words
    midpoint      4,240 words
    upper bound   4,600 words

Visual material occupies column space; costed as word-equivalents:

    architecture / governance-flow figure     ~150
    empirical results table                   ~200
    Related Work comparison table             ~280
    total visual equivalent                   ~630

Combined against a six-page envelope (references 0.8–1.0 page; body 5.0–5.2 pages):

| Scenario | Prose + visuals | Fits at 850 w/pp (4,250–4,420) | 900 w/pp (4,500–4,680) | 1,000 w/pp (5,000–5,200) |
|---|---|---|---|---|
| Lower bound | **4,510** | no | **yes** | yes |
| Midpoint | 4,870 | no | no | yes |
| Upper bound | 5,230 | no | no | marginal |

**Conclusion, stated plainly.** Only the **lower-bound** scenario fits at a realistic column density, and it fails under the most conservative density assumption. The midpoint and upper-bound scenarios do **not** fit.

**Therefore the bands in §12.1 are ceilings, and the lower bound is the drafting target.** Drafting to midpoint will overrun.

**Named reserve — approximately 300 words**, available without touching protected content:

1. drop the architecture figure, deferring the visual to the journal paper — **−150**
2. reduce Related Work synthesis prose from three sentences to two, letting the table carry more — **−150**

Applying the reserve brings the lower-bound scenario to ~4,210, which fits even at 850 words per page.

### 12.4 Cut order

1. Hysteresis — already excluded from the contribution story
2. Redundant Related Work prose
3. Secondary architecture explanation already visible in equations or the table
4. Non-essential examples
5. Duplicated formal-property explanation

**Never cut:** C2 core results · operational-semantics constructs needed for C1 · the novelty-precedent acknowledgement · the required limitations · the R-SAFE-001 disclosure · the lower-bound disclosures.

---

## 13. Related Work positioning

**Table-led, not prose-led.** One compact comparison table carrying the principal mechanism distinctions across seven precedent families, plus a short synthesis.

| Family | Representative source |
|---|---|
| TCAS II / ACAS II advisory inhibition | FAA AC 20-151C (2017) |
| ACAS X formal verification | Cleaveland, Mitsch & Platzer (2023) |
| Levels of automation | Parasuraman, Sheridan & Wickens (2000) |
| Adaptive automation | Bernabei & Costantino (2024) |
| Selective prediction / deferral | Kwon & Kim (2026); Punzi et al. (2024) |
| Shielding / action masking | Könighofer et al. (2025) and the shielding line |
| Graduated runtime governance | Flehmig et al. (2024); Baxi (2026); Kang (2026) |

Suggested discriminating columns: *governed object · runtime state source · runtime or design-time · recommendation-type scope conditioned? · human final authority · formal guarantee*.

**The synthesis prose establishes only three things:** (1) mechanism precedent exists; (2) formal-property precedent exists; (3) the scoped operational-semantic combination remains distinct within the reviewed literature.

**Corpus distinction, required in the text:** the **original structured review of 72 papers** is reported separately from the **targeted post-review literature added during novelty validation and the conference rebuild**. The two populations are never merged, and the figure 78 is never written.

**Not a second systematic review.** No screening counts, no PRISMA-style reporting, no per-paradigm subsections.

---

## 14. Frozen gap statement

> Within the reviewed AI decision-support and governance literature, we did not identify a formal operational treatment that combines a classified multi-component environmental state, explicit observation-resolution and exclusion semantics, and a state-conditioned advisory-type admissibility contract. Analogous restriction of advisory types conditioned on an externally measured state is established practice in certified collision-avoidance avionics.

**Clause audit:**

| Clause | Status |
|---|---|
| "Within the reviewed … literature" | Scoped. Required |
| "we did not identify" | Reports the search outcome, not the state of the world |
| "formal operational treatment" | Matches C1's frozen object |
| "classified multi-component environmental state" | Supported — five component classifiers, max-severity aggregation |
| "explicit observation-resolution and exclusion semantics" | Supported — `ρ_{D,τ}`, four ⊥ conditions, declared exclusion `D` |
| "state-conditioned advisory-type admissibility contract" | Supported — `A_AI(S)` with pre-reasoning `RS(S)` |
| Second sentence | **Mandatory.** The precedent must be acknowledged in the same statement, not deferred |

**Prohibited in this statement and anywhere else:** no prior work · no existing architecture · first · unprecedented.

---

## 15. Frozen novelty-positioning sentence

Exactly one canonical sentence, reused verbatim in the Introduction, the contribution paragraph and the Discussion:

> This work formalises an existing governance pattern — runtime restriction of advisory types by an externally measured state, established in certified collision-avoidance avionics — as an operational specification over a classified multi-component environmental state, and characterises empirically how often its intermediate advisory-scope level produces a governance outcome distinct from participation-only governance.

It positions the work as **formalisation + scoped generalisation + empirical characterisation** of an existing mechanism pattern. It claims no mechanism invention, no property novelty, and no outcome.

---

## 16. Title confirmation

    TITLE = RETAIN

> **Evaluating Graduated Advisory-Scope Governance for AI Decision Support**

Reconfirmed against the frozen RQs and narrative. *Evaluating* matches an RQ set whose weight sits on RQ2 and RQ3. No symbols, no mathematics, no footnotes, no subtitle. No contradiction found, so no alternatives proposed.

---

## 17. Excluded claims and evidence

**Excluded evidence:** E5 · H3 · MacBook reference timing · target-hardware performance · human study · any human-outcome measurement.

**Excluded RQ types:** performance/E5 · implementation-fidelity · hysteresis · human-study · safety-effectiveness · novelty.

**Excluded claims:** first · first-ever · unprecedented · globally novel · uniquely novel · no existing architecture · no prior system restricts advisory scope · totality/monotonicity/Safety Dominance/containment as novel properties · domain-independent as an engineering claim · demonstrated cross-domain applicability · safer · safety improvement · risk reduction · accident prevention · improved decision quality · improved trust · calibrated reliance · effectiveness · real-world validation · validated deployed system · smartphone feasibility · real-time performance validated.

**Excluded interpretations:** ΔL2 as a safety figure · `5.81 ± 4.48` or equivalent · PRIMARY/RESOLUTION as uncertainty bounds · deterministic census as statistical inference · formal containment as empirical safety · prototype fidelity as real-world effectiveness · 454 advisory types · hysteresis as evidence that stabilisation was required.

---

## 18. Provenance-open item

    RESOLUTION_PAIRWISE_C0_C1_C0_C2 = PROVENANCE_INCOMPLETE
    PROVENANCE_OPEN_ITEMS           = 1

C0↔C1 = 41.08% and C0↔C2 = 45.56% are canonical in the Journal 1 manuscript, in the prediction register (P24, P23) and in `report-c8-migration-2026-09-08.md`, but have **no row** in `data/journal1-manuscript-evidence-sync/quantitative-provenance.csv`.

**Not usable as headline manuscript evidence until a provenance row exists.** Not recomputed. Not repaired in this task. RQ2 and RQ3 are fully supportable without them, on ΔL2 (5.81% / 4.48%) and C1↔C3 (0.00% / 0.00%).

---

## 19. Downstream manuscript rules

1. **Baseline is v3.** Do not rebuild from v2.5. Do not modify `manuscript-v3.md`; the rebuild is authored as a new version.
2. **Three RQs, two contributions, no third.** The old review-based headline contribution is withdrawn; the review appears as positioning and background only.
3. **Draft to the lower bound of each section band** (§12.3). Midpoint drafting will overrun.
4. **The disclosure budget is protected** (§12.2). If space fails, cut per §12.4 and use the §12.3 reserve.
5. **Gap statements are always scoped** — "Within the reviewed literature…", "We did not identify prior work in the reviewed literature that…".
6. **The novelty-positioning sentence (§15) is used verbatim** in all three sites.
7. **Stale v3 text to repair:** the "being developed as a prototype" framing; "Prototype fidelity has not yet been verified empirically"; "the reasoning engine is specified but not implemented"; and the offer of decision-support utility as a secondary metric (the utility construct is `OPEN — CONSTRUCT DEFINITION REQUIRED`).
8. **v3 contribution 1 is not restated** in its current form — *"from 72 papers… no architecture identified restricts AI advisory scope as a function of classified environmental safety state"* is falsified in unscoped form.
9. **Standing repository constraints remain in force:** superseded-figure blacklist; `g_w` reported as 2 activations / 0 bindings; `g_m` and κ lower-bound disclosures travelling with every severity figure; hysteresis qualified if used at all; solar provenance described as a NOAA-style low-precision solar-position formulation validated against USNO; `f(E)` for the ideal case and `F_{D,τ}` for deployed behaviour; `Property 5.x` legitimate, `Theorem 5.x` obsolete.
10. **Figure and table priority** (§12.1, §12.3): the Related Work comparison table and the empirical results table are load-bearing; the architecture figure is the first visual to drop.

---

## 20. Changed files

**Created:**

- `data/amict-conference-rebuild/rq-narrative-freeze.md` (this file)
- `data/amict-conference-rebuild/rq-evidence-map.csv`

**Untouched, as required:** `manuscript-v3.md` and all publication manuscripts · all six prior AMICT evidence artefacts · all empirical artefacts and scripts · all CLOSED Journal 1 workstreams · the 72-paper sample · `notes/` and `citation-notes-map.md`.

No manuscript prose drafted. No `manuscript.md`, `.docx`, `.pdf` or `.tex` created. No experiment run. No empirical result recomputed. No contribution, threshold, architecture or comparator definition changed. The provenance gap was not repaired.

---

## 21. Stop-condition assessment

| # | Condition | Result |
|---|---|---|
| 1 | An RQ requires new experiments | **Did not fire** — all three rest on closed evidence |
| 2 | An RQ depends on E5/H3 | **Did not fire** — excluded by design |
| 3 | An RQ requires human-study evidence | **Did not fire** |
| 4 | RQ1 phraseable only by restoring mechanism novelty | **Did not fire** — RQ1 asks how the governance is specified and verified operationally, which requires no novelty claim |
| 5 | RQ2/RQ3 require a safety or effectiveness reading | **Did not fire** — both are stated as governance-outcome divergence |
| 6 | Narrative cannot distinguish the contribution from TCAS/ACAS X | **Did not fire** — §10 and §14 distinguish on the operational-semantic combination, discharged by the contribution freeze's scoped-combination test |
| 7 | Narrative requires changing frozen C1 or C2 | **Did not fire** |
| 8 | Numerical contradiction | **Did not fire** — one provenance-completeness item (§18), not a conflict |
| 9 | Six-page story cannot carry both contributions plus required limitations | **MANAGED_NOT_FIRED** — feasible on the lower bound with three visuals and a ~300-word reserve; the non-fitting scenarios are stated in §12.3 rather than hidden |

---

    RQ_NARRATIVE_FREEZE   = CLOSED
    RQ_COUNT              = 3
    RQ1                   = FROZEN
    RQ2                   = FROZEN
    RQ3                   = FROZEN
    CONFERENCE_NARRATIVE  = FROZEN
    GAP_STATEMENT         = FROZEN
    NOVELTY_POSITIONING   = FROZEN
    TITLE                 = RETAIN
    SIX_PAGE_STORY        = FEASIBLE_WITH_MANDATORY_COMPRESSION
    STOP_CONDITION_9      = MANAGED_NOT_FIRED
    PROVENANCE_OPEN_ITEMS = 1
    CONFERENCE_MANUSCRIPT = NOT_DRAFTED
