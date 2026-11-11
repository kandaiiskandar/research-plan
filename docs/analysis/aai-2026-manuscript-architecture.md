# AAI 2026 — IEEE 6-Page Manuscript Architecture

**Date:** 2026-09-23
**Status:** Drafting blueprint. No manuscript prose written.
**Governed by:** `aai-2026-locked-research-chain.md` — no locked element is changed here.
**Supporting detail drawn from:** `experiment-report-delta-l2.md` only where the locked chain requires it.

> **RESEARCH CHAIN REOPEN REQUIRED: NO.** Every element of this architecture is derivable from the locked chain. One supply-side issue is flagged in §15 (three required citations have no corpus note) — that is a sourcing action, not a chain change.

---

## 1. Manuscript identity

| | |
|---|---|
| **Title** | From Declared Risk Levels to Admissible Recommendations: Measuring the Operational Effect of AI Governance |
| **Venue** | AAI 2026 · Track 3 · *Responsible, Ethical & Human-Centred AI* — strictly under **Responsible** |
| **Format** | IEEE conference, A4, two-column, 10pt, English, **6 pages absolute maximum** including everything |
| **Review mode** | ⚠️ Appears **non-blind** — author names, affiliations and corresponding email required on page 1. Confirm before submission; v4 was written double-blind and must be de-anonymised |
| **Genre** | Short empirical measurement paper |
| **Object measured** | `A_AI(S)` — the admissible recommendation set |
| **What is NOT measured** | Any model, any generated advice, any human, any outcome |

**One-line brief for the drafting agent:** *this is a measurement paper about whether a declared governance level does anything, evaluated on a fisheries environmental record; it is not a paper about the architecture, the mechanism, or the fisheries.*

---

## 2. Six-page budget

**Basis:** 6 pages × 2 columns = 12 columns; ≈ 480 body words per full column.

| Element | Columns | Notes |
|---|---|---|
| Title + author block | 0.35 | Non-blind |
| Abstract + index terms | 0.45 | 150–200 words |
| **Body text** | **7.70** | **≈ 3,700 words** |
| Table 1 (contract) | 0.30 | |
| Table 2 (comparator) | 0.35 | |
| Table 3 (results) | 0.80 | Largest float |
| Figure 1 + caption | 0.55 | |
| References | 1.10 | ≈ 22 refs |
| Heading / float whitespace overhead | 0.40 | |
| **Total** | **12.00** | |

### Allocation by section

| Section | Columns | Words | Page position |
|---|---|---|---|
| I. Introduction | 1.50 | ~720 | p1 col1–col2 |
| II. Background and Positioning | 1.10 | ~530 | p2 col1 |
| III. Governance Contract, Criterion and Metric | 1.50 | ~720 | p2 col2 – p3 col1 |
| IV. Evaluation Design | 0.90 | ~430 | p3 col2 |
| V. Results and Discussion | 1.90 | ~910 | p4 – p5 col1 |
| VI. Limitations and Conclusion | 0.80 | ~390 | p5 col2 |
| References | 1.10 | — | p6 |

> **Deviation from the suggested allocation.** The task brief proposed one page each for six blocks. That over-funds Related Work and under-funds Results. Results carries nine reported quantities plus their interpretive qualifications — it is the section that answers RQ1 and it gets the largest share. Related Work is compressed to three short clusters because its only job is to concede prior art, not to survey.

> 🔴 **Hard reserve: 1.1 columns for references.** Do not let the body expand into it. A 6-page IEEE paper that overflows on references is rejected at the format check, and AAI states papers exceeding six pages are rejected.

---

## 3. Section architecture

**Six numbered top-level sections.**

### I. Introduction

- **PURPOSE.** Establish the governance-measurement problem, concede the mechanisms, state the gap, the RQ and the contribution — in that order.
- **MUST ESTABLISH.** (a) Declared risk levels do not establish operational effect. (b) Mechanisms for state-conditioned restriction already exist and are not this paper's claim. (c) A measurement question remains. (d) What this paper contributes and what it does not. ~~(e) That two headline figures were previously reported.~~ 🔴 **(e) removed 2026-09-23** — the earlier abstract is accepted but not confirmed published; no prior-publication statement appears.
- **CONTENT.** Six paragraphs — §4.
- **DO NOT INCLUDE.** The architecture. The four-layer structure. `S = f(E)`. Fisheries motivation beyond one clause. Any safety framing.
- **EVIDENCE.** Locked chain §§2, 3, 4, 5, 6, 13.
- **SPACE.** 1.50 col / ~720 words.
- **TRANSITION.** *"We first situate the measurement question against the mechanism literature it does not compete with."*

### II. Background and Positioning

- **PURPOSE.** Concede prior art and establish that the measurement question is what remains open.
- **MUST ESTABLISH.** Restriction mechanisms are established (runtime assurance, shielding, advisory inhibition); behavioural individuation of levels is established (levels of automation); Responsible AI has a principles-to-practice measurement gap; nobody has characterised activation frequency for advisory scope.
- **CONTENT.** Three clusters — §5.
- **DO NOT INCLUDE.** A general Responsible AI review. Fairness, explainability or trust literature. Any AI-in-fisheries survey. Any claim that prior frameworks are deficient.
- **EVIDENCE.** Locked chain §§3, 4, 5.
- **SPACE.** 1.10 col / ~530 words. **Three paragraphs maximum.**
- **TRANSITION.** *"We therefore specify the governance object, the criterion by which a level is judged to constrain it, and the metric."*

### III. Governance Contract, Criterion and Metric

- **PURPOSE.** Define the measured object, state the criterion, define the comparator ladder and the metric, and state the metric's identity **before** any number.
- **MUST ESTABLISH.** `A_AI(S)` and its three states (Table 1); the criterion; C0–C3 (Table 2) and that C1 and C3 are the same governance function by construction; `Δ_L2` and its isolation by subtraction; `Δ_L2 ≡ P(S = CAUTION)` and what that means for interpretation.
- **CONTENT.** §6.
- **DO NOT INCLUDE.** Proofs of P1–P3. The full classifier. The five component classifiers in detail. Any architecture diagram. `G(S)` as a separate formal object — see §6.
- **EVIDENCE.** Locked chain §§7, 8, 9, 10.
- **SPACE.** 1.50 col / ~720 words.
- **TRANSITION.** *"We instantiate this on a five-year environmental record."*

### IV. Evaluation Design

- **PURPOSE.** State what was replayed, over what, with which denominator, and where the thresholds come from.
- **MUST ESTABLISH.** Two configurations (PRIMARY / RESOLUTION); records and departure-window denominators; site and period; that four thresholds trace to named authorities and three choices are researcher-defined; that one component is structurally excluded; that this is a deterministic census, not a sample.
- **CONTENT.** Data paragraph; provenance paragraph; exclusion paragraph.
- **DO NOT INCLUDE.** The full threshold table (wave onset and its source only). Design-science methodology framing. Planned future validation.
- **EVIDENCE.** Locked chain §§8, 11; report §§5.1, 7.1.
- **SPACE.** 0.90 col / ~430 words.
- **TRANSITION.** *"We report the isolated contribution, then the conditions under which it moves."*

### V. Results and Discussion

- **PURPOSE.** Answer RQ1 and immediately bound what the answer supports.
- **MUST ESTABLISH.** The nine-step narrative in §9, in that order.
- **CONTENT.** §9 + Table 3 + Figure 1.
- **DO NOT INCLUDE.** Any comparison to a baseline that is not C0–C3. Any statement of benefit. Any speculation about fisher behaviour. Any p-value or confidence interval.
- **EVIDENCE.** Locked chain §§11, 12, 17.
- **SPACE.** 1.90 col / ~910 words.
- **TRANSITION.** *"These results are bounded in five specific ways."*

### VI. Limitations and Conclusion

- **PURPOSE.** State the binding limitations and close without new claims.
- **MUST ESTABLISH.** The five limitation statements in §12; the six conclusion sentences in §17.
- **DO NOT INCLUDE.** Any new number. Any future-work promise beyond one clause. Any restatement of contribution stronger than §14 of the locked chain.
- **EVIDENCE.** Locked chain §§14, 17.
- **SPACE.** 0.80 col / ~390 words.
- **TRANSITION.** → References.

---

## 4. Introduction blueprint

Six paragraphs. **No polished prose here — purpose, claim and citation type only.**

**P1 — The governance-measurement problem** *(~110 words)*
- *Purpose:* open on the problem, not the domain and not AI generally.
- *Claim:* AI governance frameworks specify controls and risk levels; whether a declared level constrains what a system may do, and how often, is not established by declaring it.
- *Citation type:* AI-governance framework / review; NIST AI RMF MEASURE.
- 🔴 *Forbidden openings:* "Coastal fisheries are dangerous…", "Artificial intelligence is rapidly transforming…", anything beginning with the architecture.

**P2 — The concession** *(~120 words)*
- *Purpose:* remove mechanism novelty from the table before a reviewer does.
- *Claim:* mechanisms that restrict permitted actions by external state are established practice — runtime assurance bounding a complex function, preemptive shielding supplying a safe action list before the agent acts, advisory-type inhibition in certified avionics — and this paper claims none of them.
- *Citation type:* ASTM F3269; Alshiekh et al.; FAA AC 20-151C.
- *Note:* this is **binding condition 2** and must appear on page 1.

**P3 — What is already established about levels** *(~90 words)*
- *Purpose:* source the criterion's principle so it is not claimed as new.
- *Claim:* automation levels are individuated by what function is allocated, not by how many labels a taxonomy declares.
- *Citation type:* Parasuraman, Sheridan & Wickens (2000); optionally SAE J3016.

**P4 — The gap** *(~110 words)*
- *Purpose:* state the narrow, falsifiable empirical gap.
- *Claim:* no empirical characterisation was identified of how often an intermediate advisory-scope level changes the admissible recommendation set relative to a participation-only gate, replayed over a multi-year record.
- *Citation type:* none required — an absence statement, scoped to "within the reviewed literature".

**P5 — RQ and approach** *(~140 words)*
- *Purpose:* state RQ1 verbatim from the locked chain and the approach in two sentences.
- *Claim:* RQ1; approach = a criterion, a four-configuration comparator ladder isolating one level, and a replay over five years of hourly environmental records at one site.
- *Citation type:* data sources (Open-Meteo; ERA5).

**P6 — Contribution and non-claims** *(~120 words)* — ⚠️ **revised 2026-09-23**
- *Purpose:* state the contribution and the non-claims. **No prior-work disclosure sentence.**
- *Claim:* (i) an interpretive apparatus for governance-activation measurement; (ii) an auditable criterion with a worked instance; (iii) a site-specific negative finding on component dominance. Explicitly: no safety, decision-quality, human-oversight or optimality claim is made.
- *Citation type:* **none.**
- 🔴 *Correction:* the earlier IPoSCI extended abstract is **accepted but not confirmed published**, so it is **not cited** and nothing is described as previously published or previously reported. Revised **binding condition 4** is that the differentiation is carried by content, not by a citation — the paper's distinctness rests on the removal test in locked chain §18, which it passes. **Frees ~30 words** against the budget.

**Flow check against the locked chain.** The brief's preferred movement — Responsible AI governance → controls declared → declared levels do not establish effect → mechanisms exist → measurement question remains → gap → RQ → contribution — is **fully consistent** with locked §§2–6 and is adopted, with the concession moved to P2 so it lands on page 1 as required, and prior-work disclosure appended to P6.

---

## 5. Related-work blueprint

**Three clusters. Three paragraphs. ~530 words total. This is a concession section, not a survey.**

### Cluster A — Responsible AI: from declared controls to measured effect *(~180 words, 1 para)*
- **Why necessary.** Supplies the paper's positioning and the only defensible Responsible AI connection.
- **Establishes.** Governance controls are specified far more often than their operational effect is measured; the NIST AI RMF's MEASURE function exists for that reason.
- **Concedes.** Nothing — this cluster is the frame, not prior art to concede.
- **Remains open.** Measurement of whether a specific declared level constrains permitted actions.
- **Max paragraphs:** 1.

### Cluster B — Restriction mechanisms *(~210 words, 1 para)*
- **Why necessary.** Binding condition 2. Without it the paper reads as claiming a mechanism.
- **Establishes.** Bounding a complex function with a verified runtime monitor; preemptive versus post-posed shielding; advisory-type inhibition conditioned on externally measured state; supervisory switching.
- **Concedes.** 🔒 All of it. `MECHANISM_NOVELTY = WITHDRAWN`. One explicit sentence: *this paper contributes no restriction mechanism.*
- **Remains open.** How often a given restriction is reached in deployment.
- **Max paragraphs:** 1.

### Cluster C — Individuation of levels *(~140 words, 1 para)*
- **Why necessary.** Sources the criterion so it is not claimed as new, and pre-empts "the criterion is obvious".
- **Establishes.** Levels of automation are defined by function allocation, not by label count.
- **Concedes.** The principle underlying the criterion.
- **Remains open.** Its explicit statement and application as an audit test for AI governance designs.
- **Max paragraphs:** 1.

### Explicitly excluded from Related Work

| Excluded | Reason |
|---|---|
| Fairness, bias, explainability literature | Not engaged; would invite expectations the paper cannot meet |
| Trust / user-acceptance literature | No users studied; would signal a human-centred claim |
| AI-in-fisheries surveys | Converts the paper into a domain application |
| Selective prediction / reject-option literature | Analogous but **confidence-triggered**, not external-state-triggered; a correct treatment costs a paragraph the budget cannot fund. ⚠️ If a reviewer raises it, that is a rebuttal matter |
| Formal methods / runtime verification in depth | P1–P4 are not claimed as theory; one citation suffices |
| EU AI Act / ISO 42001 / ISO 23894 | Applicability unestablished; regulatory framing invites scope questions |
| Design-science methodology | Not a contribution of this paper |

---

## 6. Method blueprint

**Minimum formal apparatus. Four displayed items maximum.**

### Decision: omit `G(S)` from the formalism

🔒 The locked chain permits `G(S)` as "one mention, not built upon". **This architecture goes further and omits it as a formal object**, because `G(S) = 1 ⟺ A_AI(S) ≠ ∅` in this instantiation — so it carries no information the admissible set does not — and because retaining it invites the objection that the two controls are not independent.

**Replacement:** one parenthetical clause in §III — *participation gating is the special case in which the admissible set is empty.* Table 1 keeps a `G` column for readability only, with a footnote stating it is determined by emptiness of `A_AI`. This saves ~60 words and removes an attack surface. **No locked element is altered: the locked chain lists `G(S)` as USE IF SPACE.**

### Displayed items

**(1) The admissible-set map** — Table 1, not an equation.

**(2) The criterion** *(displayed, ~30 words)*
> A declared risk level changes governance behaviour only if it contracts the admissible action set. Two configurations assigning identical admissible sets at every state denote the same governance function, irrespective of state cardinality.

Stated as a **criterion**, never as a theorem, proposition or result. One sentence immediately after: it restates for AI governance a principle established in the levels-of-automation literature [cite].

**(3) The metric** *(one equation)*

> Δ = (N_restricted / N_eval) × 100%, and Δ_L2 = (C0↔C2) − (C0↔C1)

Plus one sentence: the subtraction isolates the intermediate level; a direct pairwise C1↔C2 computation cross-checks it.

**(4) The identity** *(one displayed line — MUST precede all numbers)*

> For the evaluated C1 and C2 mappings, which differ only at CAUTION: **Δ_L2 ≡ P(S = CAUTION)**

Followed by two sentences of interpretation: the measure identifies **how often the intermediate restriction is activated**; it is invariant to the content of `A_AI(CAUTION)`, since any strict subset of FULL yields the same value; therefore it does not evaluate whether `{Go, Delay}` is the right restriction.

🔴 **Placement is non-negotiable.** The identity appears in §III, before §V. Stated first it is rigour; encountered by a reviewer after the result it is fatal.

### P1–P4 treatment

| | Treatment |
|---|---|
| **P1 Totality** | One sentence in §IV: classification remains total under the declared exclusion, which is what makes the lower-bound reading available. No proof |
| **P2 Containment** | One clause, labelled *true by construction*. No proof |
| **P3 Safety Dominance** | **Omit from body.** One clause in §IV noting implementation conformance was checked |
| **P4** | Appears **as the criterion's instance**, not as a property. Never labelled a theorem or a result |

### Not included
The five component classifiers in full · `S = f(E)` as an equation (one prose clause only) · the four-layer architecture · any proof · any architecture figure.

---

## 7. Table specifications

### TABLE I — Governance contract

**Caption:** *Admissible recommendation set by safety state. FULL = {Go, Delay, DepartureTime, Duration}.*

| State | G | A_AI(S) |
|---|---|---|
| SAFE | 1 | FULL |
| CAUTION | 1 | {Go, Delay} |
| UNSAFE | 0 | ∅ |

**Footnote:** *G is determined by emptiness of A_AI and is shown for readability only. A_AI(CAUTION) = {Go, Delay} is a researcher-defined design choice with a domain rationale; it is not empirically validated, shown optimal, or established as safer.*
**Claim supported:** defines the measured object.
**Why it deserves space:** the paper is unreadable without it; it costs 0.30 column.

### TABLE II — Comparator design

**Caption:** *Four governance configurations. C1 and C3 assign identical admissible sets at every state and therefore denote the same governance function.*

| | A_AI(SAFE) | A_AI(CAUTION) | A_AI(UNSAFE) |
|---|---|---|---|
| C0 Ungated | FULL | FULL | FULL |
| C1 Participation-only | FULL | FULL | ∅ |
| **C2 Proposed** | FULL | **{Go, Delay}** | ∅ |
| C3 Three-state topology | FULL | FULL | ∅ |

**Footnote:** *C3 ports the governance topology of [Flehmig] onto an environmental conditioning variable; [Flehmig] condition on AI degradation rather than environmental state. C3 is not a reproduction of that system, not a test of it on its own problem, and not a claim that it is deficient.*
**Claim supported:** the criterion, by inspection — **the reader sees C1 and C3 are row-identical before any measurement appears**, and sees that C2 differs in exactly one cell.
**Why it deserves space:** 🔒 **the single highest-value float in the paper.** It converts the criterion from an assertion into something the reader verifies visually. **Never cut.**

### TABLE III — Results and sensitivity

**Caption:** *Isolated contribution of the intermediate advisory-scope level, with sensitivity and scope dependence. Deterministic census over all departure-window hours; ranges are deterministic sensitivity ranges, not confidence intervals.*

**Two-panel design — one float, visually separated.** A single flat table with all six categories is unreadable; two labelled panels inside one float keeps it to 0.80 column.

**Panel A — Isolation and configurations**

| Quantity | PRIMARY | RESOLUTION |
|---|---|---|
| Hourly records | 43,848 | 28,501 |
| Departure-window hours | 9,135 | 5,935 |
| C0↔C1 (Level 1 alone) | 42.88% | withheld† |
| C0↔C2 (Levels 1+2) | 48.69% | withheld† |
| **Δ_L2 (Level 2 isolated)** | **5.81%** | **4.48%** |
| C1↔C3 (entailed) | 0.00% | 0.00% |

**Panel B — Sensitivity and scope dependence (PRIMARY unless stated)**

| Condition | Δ_L2 |
|---|---|
| Sourced-threshold envelope, small vessel | 5.67 – 9.56% (RES 4.26 – 6.64%) |
| Alternative reading of the same wave source‡ | 9.22% |
| Wave onset ±0.25 m | 2.54 – 14.75% |
| Vessel class: medium / large | 1.96% / 1.26% (RES 0.66% / 0.37%) |
| Daylight-only denominator | 9.59% (RES 7.40%) |
| Dominant component `g_o` | 518/531 CAUTION hours = 97.6% |
| Component `g_w` | 0/531 — does not bind |

**Footnotes:**
† *Withheld pending provenance repair; Δ_L2 is unaffected.*
‡ *The wave source supports two readings of the small-vessel boundary — operational ceiling and failure point — giving 5.81% and 9.22% respectively. The operational-ceiling reading is used throughout.*
§ *All figures are lower bounds: one conceptually relevant component has no historical archive and is held at its least-severe value under a declared exclusion; it can only raise severity.*

**Claim supported:** every quantity in the central claim.
**Why it deserves space:** it is **binding condition 3** made structural — the headline cannot be read without its qualifications because they share the float.

---

## 8. Figure specification

**Verdict: YES, one figure — and it is necessary.**

**Reasoning.** Table 3 Panel B states the envelope as endpoints. It cannot show the *shape* — that Δ_L2 sits on a steep monotone gradient rather than a plateau. The locked central claim depends on the headline not being a stable property, and a reviewer challenged on that point is more persuaded by seeing the slope than by reading two numbers. This is the one place where a figure outperforms a table row.

**FIGURE 1**
- **x-axis:** wave CAUTION onset `O_C` (m), across the sourced range.
- **y-axis:** Δ_L2 (%), 0 to ~16.
- **PRIMARY trace:** solid line with markers.
- **RESOLUTION trace:** dashed line — include; it shows the gradient is not an artefact of one wave model.
- **Sourced-threshold region:** light shaded band spanning the sourced envelope.
- **Baseline marker:** vertical line at the operational-ceiling value with the 5.81% point marked.
- **Second-reading marker:** a second vertical line or point annotation at the failure-point reading giving 9.22%, labelled. ⚠️ Include only if it does not crowd the plot; otherwise leave it to the Table 3 footnote.
- **NOT shown:** confidence bands (none exist) · trend fits · extrapolation beyond the sourced range · any second variable · colour-only encoding (must read in greyscale).
- **Caption:** *Δ_L2 against the wave CAUTION onset for both environmental-data configurations. The shaded band spans externally sourced threshold values; the marked point is the operational-ceiling reading used throughout. The relationship is a deterministic sensitivity range, not a confidence interval.*
- **Claim supported:** the headline is a point on a steep gradient, not a stable site property — and the wave component is the dominant determinant.

🔴 **Do not create an architecture figure.** The locked chain omits it: highest IPoSCI overlap, lowest information density.

---

## 9. Results narrative

**Locked order. The narrative is "here is what the measurement identifies, here is the value, here is everything that moves it" — never "5.81% is our main finding".**

**R1 — Comparator isolation**
- *Number:* C0↔C1 = 42.88%; C0↔C2 = 48.69%.
- *Interpretation:* the participation gate alone accounts for 42.88%; adding advisory-scope contraction accounts for 48.69%; the difference isolates the intermediate level.
- *Permitted:* the level's contribution is separable from the participation gate.
- *Prohibited:* that either figure measures benefit.

**R2 — Identity restated in one clause**
- *Number:* none.
- *Interpretation:* recall from §III that this difference is identically P(S = CAUTION).
- *Permitted:* an activation reading.
- *Prohibited:* any reading as restriction quality. *(Restated here, not first stated here.)*

**R3 — Observed activation**
- *Number:* **Δ_L2 = 5.81% PRIMARY, 4.48% RESOLUTION**; direct pairwise C1↔C2 = 5.81% confirms the subtraction.
- *Interpretation:* the intermediate restriction is reached in 5.81% of departure-window hours; the level is **non-vacuous**.
- *Permitted:* non-vacuity at this site for this class; a lower bound.
- *Prohibited:* stability, benefit, correctness, generalisation.

**R4 — Entailed comparator**
- *Number:* C1↔C3 = 0.00%.
- *Interpretation:* follows from the configurations in Table 2; the replay confirms the encoding. **Label explicitly as entailed and as an executable conformance check.**
- *Permitted:* the criterion is instantiated.
- *Prohibited:* 🔴 presenting 0.00% as a discovered result.

**R5 — Sourced-threshold envelope**
- *Number:* 5.67–9.56% PRIMARY; 4.26–6.64% RESOLUTION; second source reading 9.22%.
- *Interpretation:* non-vacuous across every sourced configuration, but not a point property.
- *Permitted:* a disclosed deterministic range.
- *Prohibited:* "robust"; "5.81% ± x"; any confidence-interval language.

**R6 — Wave dominance**
- *Number:* ≈ −1.4 pts per 0.05 m; ±0.25 m → 2.54–14.75%. Rainfall moves 0.48 pts; wind is a structural zero across 18–25 kn.
- *Interpretation:* one threshold governs the magnitude; the non-MET rainfall boundary is **not** driving the headline.
- *Permitted:* identification of the dominant determinant.
- *Prohibited:* that the threshold is correct or optimal.

**R7 — Component attribution**
- *Number:* `g_o` 518/531 = **97.6%**; `g_r` 2.4%; `g_w` 0/531.
- *Interpretation:* the intermediate classification is effectively single-component at this site; `g_w` does not bind empirically. 🔒 Report `g_t` (emits no CAUTION **by construction**) and `g_m` (**structurally excluded**) separately and labelled — they are not empirical non-binding findings.
- *Permitted:* the evaluated record does not warrant equal component importance at this site.
- *Prohibited:* that the components are wrong in general, or that three components "never bind".

**R8 — Scope dependence**
- *Number:* medium 1.96%, large 1.26% (0.66% / 0.37% RESOLUTION); daylight-only denominator 9.59% / 7.40%.
- *Interpretation:* the figure is class-specific, approaching vacuity for larger classes, and not denominator-invariant.
- *Permitted:* explicit scoping to vessels under 10 GRT and to the stated denominator policy.
- *Prohibited:* generalisation across classes — an explicit non-claim.

**R9 — Lower-bound interpretation**
- *Number:* none.
- *Interpretation:* one component has no historical archive, is held at its least-severe value under a declared exclusion, and can only raise severity; every figure above is therefore a lower bound.
- *Permitted:* a directional bound by standard partial-identification reasoning.
- *Prohibited:* any point estimate of what the true value would be.

**Closing discussion (~120 words).** Two moves only: (i) the contrast — the configuration that looks most different on a diagram (C3, three states) is governance-identical to the simplest (C1), while the one differing in a single table cell (C2) is the only one that changes anything; (ii) the consequence for practice — a declared level should be audited against admissible sets, and its activation measured, before it is credited as governance. **No third move.**

---

## 10. 5.81% presentation strategy

🔒 **Binding condition 3.** ⚠️ **Revised 2026-09-23 — the prior-publication disclosure is removed.**

| Where | What appears | Form |
|---|---|---|
| **Abstract** (part 4–5) | 5.81% and 4.48%, immediately followed by the envelope 5.67–9.56% and "lower bound" | Never the point figure alone, even in the abstract |
| **Introduction P6** | Contribution and non-claims only | **No citation. No prior-work sentence** |
| **Method §III** | The identity, before any number | Displayed |
| **Results R3** | First formal presentation, with the pairwise cross-check | **No citation attached** |
| **Table III** | Headline and all qualifications share one float | Structural guarantee of binding condition 3 |
| **Limitations** | Threshold sensitivity, class dependence, lower-bound status | Grouped — §12 |

### 🔴 Revised handling of provenance

The earlier IPoSCI extended abstract is **accepted but not confirmed published**, so it cannot be cited as a published reference and nothing may be called *previously published*, *previously reported*, or *prior publication*.

**What the manuscript does:** reports the figures as outputs of the evaluation it describes, which is accurate — the paper describes that replay, and the figures were reproduced from canonical scripts on 2026-09-21. It claims no priority over them and makes no statement about when they were first computed.

**What the manuscript must NOT do:** present material developed for the earlier study as newly created for AAI. This is the surviving obligation and it is enforced by the §11 differentiation control, which becomes the primary safeguard now that no disclosure sentence carries it.

**Where disclosure goes instead:** ⚠️ the submission form or cover letter, where venues normally ask for related work by the same authors that is submitted or accepted elsewhere. That meets the obligation without a bibliography entry. **Recommended, not optional.**

**Before submission:** re-check publication status. If published, add the proceedings citation and an explicit relationship sentence. If not, invent no citation and follow the AAI/IEEE policy for accepted-but-unpublished related work.

---

## 11. IPoSCI differentiation control

**Internal drafting control. Not a manuscript table.**

| Section | Prior IPoSCI material | AAI extension |
|---|---|---|
| Abstract | The two figures | Criterion, comparator isolation, envelope, dominance, class dependence, lower bound |
| I. Introduction | — | Entire framing: governance-measurement problem, concession, gap, RQ |
| II. Background | — | All three clusters; the concession itself |
| III. Contract | Table 1 (states and admissible sets) | The criterion; C0–C3; Δ decomposition; the identity |
| IV. Evaluation | Site, period, data sources, denominator | Provenance split (sourced vs researcher-defined); declared exclusion as a bound |
| V. Results | 5.81% / 4.48% | 42.88% / 48.69% decomposition; 0.00%; envelope; 9.22% second reading; wave dominance; attribution; class and denominator variants |
| VI. Limitations | Brief limitations | Sensitivity, dominance, class near-vacuity, lower bound, no-inference scope |

🔴 **Drafting rule — revised 2026-09-23, now the PRIMARY safeguard.** With no disclosure sentence and no citation, this control is the only thing preventing earlier material from reading as new. Every sentence in column 3 may use contribution voice. Column 2 material is presented **neutrally** — described, not claimed: "the architecture classifies…", never "we introduce…", "we propose…" or "this paper develops…". If a paragraph mixes both, split it.

🔴 **Tripwire.** Any sentence that would survive unchanged in the IPoSCI abstract is a warning sign — rewrite or delete.

---

## 12. Limitations blueprint

**Five statements. Grouped, not enumerated defensively. ~200 words.**

**L1 — Scope of measurement.** The metric is computed from the classifier and governance layer alone; the content of generated advice is never compared, and no AI model is exercised. *(Covers: no generated advice, no model.)*

**L2 — What the figure is sensitive to.** The value depends strongly on the wave CAUTION onset, spans 5.67–9.56% across sourced configurations, admits a second defensible source reading at 9.22%, and is 97.6% attributable to one component; it is not a stable site property. *(Covers: threshold sensitivity, wave dominance, component dominance.)*

**L3 — Scope of the population.** The result is specific to vessels under 10 GRT at one site and to the stated departure-window and night policies; it approaches vacuity for larger classes and changes materially under a daylight-only denominator. *(Covers: site, class, denominator, generalisation.)*

**L4 — Characterisation, not validation.** No incident record exists for the site; the architecture *would have* restricted advisory scope in those hours, not that those were the correct hours to restrict. The advisory set at CAUTION is a researcher-defined choice with a domain rationale and no empirical validation — and the reported measure is invariant to it. No contextual validation with users has been conducted. *(Covers: safety, decision quality, researcher-defined set, no user study.)*

**L5 — Bound and inference.** One conceptually relevant component has no historical archive and is excluded by declaration; since it can only raise severity, all figures are lower bounds. The evaluation is a deterministic census of a predefined window, so no confidence intervals or significance tests apply. *(Covers: missing archive, lower bound, no statistical inference.)*

---

## 13. Responsible AI terminology check

**Sentence-level risks and their safe replacements.**

| Risky idea | Where it would creep in | Safer formulation |
|---|---|---|
| "Our Responsible AI architecture" | Intro, conclusion | "Responsible AI supplies the positioning for this measurement" |
| "Restricting advice makes the system safer" | Intro P1, discussion | "restricts what the system is permitted to recommend" |
| "The human retains meaningful control" | Method, conclusion | "the architecture does not automate the departure decision" |
| "Human oversight is preserved / effective" | Intro, discussion | Omit. If unavoidable: "no recommendation is binding" |
| "Ensures responsible behaviour" | Discussion | "makes the operational effect of a declared level measurable" |
| "Improves decision making" | Anywhere | 🔴 Delete. Explicit non-claim |
| "Trustworthy AI" | Intro | 🔴 Delete — a term of art with its own criteria |
| "Graduated governance is better than binary" | Discussion | "C2 is the only configuration that changes the admissible set" |
| "Our approach guarantees…" | Method | "the implementation was checked for conformance to the contract" |
| "Fishers benefit from…" | Anywhere | 🔴 Delete |
| "Validated thresholds" | Evaluation | "thresholds traced to named authorities" / "researcher-defined" |
| "Robust to thresholds" | Results | "non-vacuous across sourced configurations, within a 5.67–9.56% range" |

**Global rule:** the paper may state *"Responsible AI provides the positioning"*; it may never imply *"this system has been demonstrated to be responsible."*

---

## 14. Claim-language guide

**PREFERRED**
admissible recommendation set · governance activation / activation frequency · operational effect · declared risk level · contracts the admissible set · specification-level criterion · executable conformance check · entailed by the configurations · deterministic sensitivity range · sourced-threshold envelope · component attribution · dominant determinant · lower bound under a declared exclusion · evaluation setting · deterministic census · non-vacuous · participation-only gate.

**AVOID**
AI behaviour · system behaviour *(when meaning generated output)* · safety improvement / safer · optimal / best / correct · robust *(unqualified)* · accurate / accuracy · human-centred · meaningful human control · human oversight *(unqualified)* · trustworthy · ethical · novel architecture / new mechanism / first · guarantees · validated · stable · significant *(statistical connotation)* · confidence interval · ± notation · intelligent decision improvement · proves / demonstrates that the restriction is right · "we discovered/found" *(for 5.81% or 0.00%)*.

**🔴 Added 2026-09-23**
- **pre-inference · before model inference · before the forward pass** — the shielding literature restricts the action set *before the agent selects*, not before inference; and this evaluation exercises no model. Use **"before the agent selects an action"** or **"preemptive"**.
- **previously reported · previously published · prior publication · in proceedings** *(of the earlier IPoSCI abstract)* — it is accepted, not confirmed published. Say nothing about its publication status.
- **we introduce / we propose / this paper develops** *(applied to the architecture, the three states, or the graduated advisory-scope concept)* — that material was developed in the earlier study. Describe it neutrally; reserve contribution voice for the C0–C3 isolation, the criterion, the metric semantics, the sensitivity work and the attribution.

**Two terms needing care**
- **"behaviour"** — permitted only as *governance behaviour* (the admissible-set mapping). 🔴 Never as system or AI behaviour, which implies generated output the paper never evaluates.
- **"governance"** — always bounded by *advisory-scope* or *admissible recommendations* on first use in a sentence making a claim.

---

## 15. Citation plan

**Target: 20–24 references. Reference-light by design.**

| # | Purpose | Verified? | Placement | Claim supported |
|---|---|---|---|---|
| 1 | AI governance principles-to-practice gap | ✅ corpus (`AI governance: a systematic literature review`) | I-P1, II-A | Controls declared more than measured |
| 2 | Risk-management measurement function | ⚠️ **NIST AI RMF — no corpus note** | I-P1, II-A | MEASURE exists to show controls function |
| 3 | **Runtime assurance / bounding a complex function** | 🔴 **ASTM F3269 — NO corpus note** | I-P2, II-B | Mechanism concession |
| 4 | **Preemptive vs post-posed shielding** | 🔴 **Alshiekh et al. AAAI 2018 — NO corpus note** | I-P2, II-B | Pre-inference restriction is prior art |
| 5 | Shielding, contemporary | ✅ corpus (`Probabilistic Shielding…`, `Adaptive Shielding…`) | II-B | Supports 4 |
| 6 | Advisory-type inhibition by external state | ✅ corpus (`FAA AC 20-151C`) | I-P2, II-B | Mechanism concession |
| 7 | TAWS advisory inhibition on input validity | 🔴 **TSO-C151c — NO corpus note** | II-B | Optional; drop if unobtainable |
| 8 | **Levels individuated by function allocation** | ✅ corpus (`A model for types and levels of human interaction with automation`) | I-P3, II-C | Sources the criterion |
| 9 | Graduated governance topology → **C3 provenance** | ✅ corpus (Flehmig et al.) | III, Table II footnote | C3's origin + fairness note |
| 10 | Multi-layered guardrails | ✅ corpus (Shamsujjoha et al.) | II-B | Graduated governance conceded |
| 11 | Fail-safe / MRC on ODD exit | ✅ corpus (`The Road to Safe Automated Driving Systems`) | II-B | Fail-safe conceded |
| 12 | Runtime verification / totality | ✅ corpus (`AgentGuard`) | IV | P1 in one sentence |
| 13 | Partial identification / directional bounds | 🔴 **Manski — NO corpus note** | IV, R9, L5 | Lower-bound reasoning |
| 14 | Wave threshold, small vessels | ✅ (Yaakob et al. 2015) | IV, Table III‡ | Wave onset + two readings |
| 15 | Vessel-dependent wave restriction | ✅ (Jeong & Im 2023) | IV | Optional support |
| 16 | Wind warning criteria | ✅ (MET Malaysia) | IV | Threshold provenance |
| 17 | Rainfall categories | ✅ (JPS/DID) | IV | Non-MET CAUTION boundary |
| 18 | Thunderstorm criteria | ✅ (MET Malaysia) | IV | Rainfall UNSAFE |
| 19 | Sunrise/sunset boundary | ✅ (COLREGs Rule 20(b)) | IV | Time boundary; policy is researcher-defined |
| 20 | Weather API | ✅ (Zippenfenig 2023) | IV | Data source |
| 21 | Reanalysis dataset | ✅ (Hersbach et al. 2023) | IV | Data source |
| ~~22~~ | ~~IPoSCI extended abstract~~ | 🔴 **REMOVED 2026-09-23** | — | Accepted but not confirmed published; not citable as a published reference. Handled as an internal provenance control and via the submission form |

### 🔴 Pre-drafting action — four citations have no corpus note

**ASTM F3269, Alshiekh et al. (AAAI 2018), NIST AI RMF and Manski** were verified during discovery via primary sources but have **no note file in `notes/`**. TSO-C151c likewise. Three of them (3, 4, 8-adjacent) are required by **binding condition 2** — the page-1 concession.

**Required before drafting:** obtain and verify full bibliographic details, and create the corpus notes. 🔴 **The drafting agent must not approximate or reconstruct these from memory.** If ASTM F3269 or Alshiekh cannot be obtained, **stop and report** — the concession cannot be written without them, and binding condition 2 fails.

*Optional/droppable if space is tight:* 7 (TSO-C151c), 15 (Jeong & Im), 5 (contemporary shielding).

---

## 16. Abstract content map

**150–200 words. Six parts. No number appears unqualified.**

| Part | Content permitted | Words |
|---|---|---|
| **1 Context** | AI governance designs declare risk levels; frameworks call for controls to be measured in operation. **No domain, no fisheries, no "AI is transforming".** | ~25 |
| **2 Problem** | A declared level constrains a system only if it changes what the system is permitted to do; whether it does, and how often, is not established by the specification. | ~30 |
| **3 Method** | A specification-level criterion; four governance configurations isolating one level; replay over five years of hourly environmental records at one coastal site. State that the measure is identically the intermediate-state rate. | ~45 |
| **4 Main observation** | A three-state configuration that does not contract the admissible set is identical to a binary gate (0.00%, entailed); the contracting level is reached in **5.81%** (4.48% alternative configuration). | ~35 |
| **5 Qualification** | Lower bound; sourced-threshold envelope **5.67–9.56%**; 97.6% attributable to one component; 1.96%/1.26% for larger vessel classes. **Mandatory — cannot be cut.** | ~30 |
| **6 Contribution** | An interpretive apparatus for governance-activation measurement plus an auditable criterion. One clause: no safety, decision-quality or human-oversight claim is made. | ~25 |

**Index terms:** AI governance; runtime governance measurement; admissible action sets; advisory scope; responsible AI; deterministic sensitivity analysis. *(Not: human-centred, ethical, trustworthy, safety.)*

---

## 17. Conclusion content map

**Six sentences. ~110 words. No new claims, no new numbers beyond those already reported.**

1. **Question addressed** — whether a declared intermediate risk level changes what an advisory system is permitted to recommend, and how often.
2. **What the method did** — stated a criterion on admissible sets and isolated one governance level with a four-configuration comparator.
3. **What was measured** — the contracting level was reached in 5.81% of departure-window hours; the non-contracting three-state configuration was identical to a binary gate.
4. **Most important qualification** — a lower bound within a 5.67–9.56% sourced envelope, 97.6% attributable to one component, and class-specific.
5. **Contribution** — the apparatus that makes an activation figure interpretable, plus the criterion.
6. **Future validation** — contextual validation with users and a second governance design remain open. *(One clause. No promise of outcome.)*

---

## 18. Compression plan

**If the draft reaches 7 pages, delete in this exact order.**

| Order | Cut | Recovers |
|---|---|---|
| **1** | Fisheries background paragraph (§IV) | ~60 words |
| **2** | Contemporary-shielding citation [5] and its clause | ~40 words |
| **3** | `E` definition line; keep only "a multi-component environmental state" | ~35 words |
| **4** | P2 containment sentence | ~30 words |
| **5** | Jeong & Im [15] and its clause | ~35 words |
| **6** | Daylight-only denominator → move from Results text to a Table III row only | ~50 words |
| **7** | Prediction-register sentence | ~30 words |
| **8** | RESOLUTION trace from Figure 1 (single trace) | ~0.1 col |
| **9** | P1 totality sentence → fold into the lower-bound sentence | ~35 words |
| **10** | Closing-discussion move (ii); keep move (i) | ~60 words |
| **11** | TSO-C151c citation [7] | ~25 words |

### 🔒 NEVER CUT

Table II · the criterion statement · the Δ identity and its placement before results · the sourced-threshold envelope · wave dominance · `g_o` 97.6% · vessel-class figures · the lower-bound statement · the page-1 mechanism concession · the IPoSCI disclosure sentence · L1, L2, L4 · any reference required by the concession.

> Cutting any NEVER-CUT item breaks a binding condition or removes a component of the locked central claim. If the paper still overruns after item 11, **reduce Results prose around Table III** — the table carries the numbers — rather than cutting a qualification.

---

## 19. Reviewer reading test

**Simulated: title → abstract → page 1 → floats → conclusion.**

**What will they think it contributes?** A measurement of whether a declared governance level has operational effect, plus a criterion for auditing that, demonstrated on an environmental record. ✅ **Matches the locked primary contribution.**

| Risk | Trigger | Mitigation in this architecture |
|---|---|---|
| **"This is the IPoSCI paper again"** | Architecture-first framing; fisheries in title; Table 1 as the lead float | Title names neither architecture nor fisheries · architecture figure omitted · Table 2, not Table 1, carries the argument · IPoSCI disclosed in Intro P6 and at first numeric appearance · Intro never describes the architecture |
| **"This is a runtime-assurance paper"** | Mechanism language; F3269 framing without concession | Concession is Intro **P2**, page 1, with an explicit sentence that no mechanism is contributed · Related Work cluster B concedes rather than positions · title says *measuring*, not *bounding* or *assuring* |
| **"Where is the AI model evaluation?"** | "AI governance" in the title; Responsible AI framing | Abstract part 3 states the object is the admissible recommendation set · L1 states the model is never exercised, and appears in Limitations which a skimming reviewer reaches · index terms avoid model-related words · "behaviour" never used for generated output |
| **"Just a fisheries application"** | Domain material early | Fisheries appears first in §IV as the evaluation setting · background capped at 3 sentences and is cut item 1 · absent from title, abstract parts 1–2, and conclusion |
| **"0.00% is trivial"** | Presenting it as a finding | Labelled entailed in Table 2 caption, in §III, and in R4 · never called a result |
| **"5.81% is just the base rate"** | Identity placed after results | Identity is in §III, before every number, and restated in R2 |
| **"Contribution too small"** | 🔴 **Unresolved.** Structural to a modest, honest six-page paper | Partially mitigated by Table 3 density and by the criterion giving a transferable takeaway. Accepted risk |

**Architecture modifications already made in response to this test:** `G(S)` demoted out of the formalism (§6) to remove the independence attack surface; Table 2 promoted to the argument-carrying float; IPoSCI disclosure moved from footnote to Introduction body; the second source reading (9.22%) given a Table III row so the sensitivity story cannot be read as cherry-picked.

---

## 20. Final research-chain traceability

Every arrow explicit. No section introduces a new objective.

```
PROBLEM   declared levels do not establish operational effect        → I-P1
   ↓
GAP       no characterisation of intermediate-level activation       → I-P4, II
   ↓
RQ1       how often, and how sensitive                               → I-P5
   ↓
METHOD    criterion on admissible sets                               → III
   ↓
COMPARATOR C0–C3; C1≡C3 entailed; C2 differs in one cell             → III, Table II
   ↓
METRIC    Δ_L2 = (C0↔C2) − (C0↔C1);  Δ_L2 ≡ P(S=CAUTION)             → III
   ↓
EVIDENCE  43,848 / 28,501 records; 9,135 / 5,935 window hours        → IV, Table III-A
   ↓
RESULT    5.81% / 4.48%, lower bound, envelope 5.67–9.56%,
          97.6% one component, class- and denominator-dependent      → V, R1–R9, Table III, Fig 1
   ↓
CONTRIBUTION  interpretive apparatus + criterion + negative finding  → I-P6, VI
   ↓
CONCLUSION    restates 1–9, adds nothing                             → VI
```

**Checks passed.** No result exists that does not answer RQ1 or bound its interpretation. No claim exceeds the locked claim/evidence matrix. No section introduces a second research objective. The criterion appears as method, never as a question. Every prohibited claim in locked §17 has a corresponding entry in §13 or §14 of this architecture.

---

FINAL SECTION ORDER: I. Introduction · II. Background and Positioning · III. Governance Contract, Criterion and Metric · IV. Evaluation Design · V. Results and Discussion · VI. Limitations and Conclusion.

FINAL TABLE COUNT: 3 — Governance contract; Comparator design; Results and sensitivity (two-panel, single float).

FINAL FIGURE COUNT: 1 — Δ_L2 against wave CAUTION onset, both configurations, sourced-threshold band.

ESTIMATED BODY WORD COUNT: ~3,700 words (7.7 columns at ~480 words/column), excluding abstract, captions and references.

ESTIMATED REFERENCE COUNT: 20–24, target 22.

PRIMARY RQ LOCATION: Section I, paragraph P5, stated verbatim from the locked chain.

CRITERION LOCATION: Section III, displayed immediately after Table I, as a criterion — never as a theorem, proposition or research question.

DELTA IDENTITY LOCATION: Section III, displayed after the metric definition and before any numerical result; restated in one clause at Results R2.

5.81% FIRST APPEARANCE: Abstract part 4, immediately followed by the qualification in part 5; first formal presentation at Results R3.

IPOSCI DISCLOSURE LOCATION: **None in the manuscript** — the extended abstract is accepted but not confirmed published, so it is not cited and nothing is described as previously published. Disclosure is made in the submission form or cover letter, and the differentiation is carried by content via the §11 control. Re-check publication status before submission.

PRIMARY CONTRIBUTION FIRST CLEARLY STATED: Section I paragraph P6.

HIGHEST PAGE-LIMIT RISK: Section V — nine reported quantities each requiring an interpretive qualification, against 1.9 columns; mitigated by pushing numbers into Table III and by compression items 6 and 10.

HIGHEST REVIEWER-MISINTERPRETATION RISK: That "AI governance" in the title leads a Track 3 reviewer to expect evaluation of an AI model; mitigated by the abstract naming the admissible recommendation set as the object and by L1, but not eliminable.

ARCHITECTURE STATUS: **READY FOR DRAFTING** — conditional on the four citations in §15 (ASTM F3269, Alshiekh et al., NIST AI RMF, Manski) being obtained and verified first. Binding condition 2 cannot be satisfied without the first two.

---

*Manuscript architecture complete. No prose drafted. No locked element changed.*
