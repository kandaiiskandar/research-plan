# AAI 2026 — Locked Research Chain

**Date:** 2026-09-23
**Status:** Authoritative specification for all subsequent AAI manuscript work.
**Scope:** Research chain only. No manuscript drafted.
**Authority order:** `experiment-report-delta-l2.md` > verified primary literature > discovery reports > inference.

> Once locked, the problem, gap, RQ, contribution and central claim below may not be changed by a drafting task. Changing any of them requires explicitly reopening the research chain.

---

## 0. Inconsistencies identified — not silently reconciled

Five, resolved in favour of the authoritative report.

**I-1 · The three non-binding components are non-binding for three different reasons.** The task brief states *"g_w, g_t, g_m: do not bind CAUTION in the evaluated record."* True, but it collapses three distinct epistemic statuses that §8.1 keeps separate:

| Component | Binding | Status | Epistemic type |
|---|---|---|---|
| `g_w` | 0 | *"activates twice in 43,848 hours, decisive in neither"* | **Empirical negative finding** |
| `g_t` | 0 | *"emits no CAUTION by construction"* | **Definitional** — it cannot bind CAUTION |
| `g_m` | 0 | *"structurally excluded, D = {m}"* | **Data unavailability** |

🔒 **LOCKED:** the paper may claim **one** empirical non-binding component (`g_w`), not three. `g_t` is a design consequence and `g_m` an exclusion. Writing "three of five components never bind" without this breakdown is an overclaim, and it was stated loosely in `aai-2026-track1-discovery.md` §2 and `-track3-discovery.md` §2.

**I-2 · A second defensible headline exists from the same source.** Limitation 2: Yaakob et al. support **two readings** of the small-vessel UNSAFE boundary — *operational ceiling* and *failure point* — giving **5.81% and 9.22%**. §12 records that the superseded 8.3% figure arose from using the failure point. The current headline therefore depends on a documented, defensible, but **contestable** source reading. This is distinct from the ±0.25 m perturbation range (2.54–14.75%) and from the sourced-threshold envelope (5.67–9.56%). 🔒 **LOCKED: all three must be reported as different things.**

**I-3 · The two discovery reports disagree on the paper's centre.** Track 1 recommended the structural finding as the centre; Track 3 recommended the measurement, with the structural finding as framing. 🔒 **Resolved in favour of Track 3**, whose reasoning is later, literature-verified, and consistent with the structural result being definitional.

**I-4 · The two discovery reports disagree on the title.** Track 1 recommended *"Adding a State Is Not Adding Governance"*; Track 3 rejected it as over-promising. 🔒 **Resolved in favour of Track 3.** See §20.

**I-6 · 🔴 IPoSCI is ACCEPTED, not PUBLISHED — correction applied 2026-09-23.** Earlier versions of this chain, the manuscript architecture and the citation lock described the IPoSCI extended abstract as "published prior work" and required it as citation [15]. **That was wrong.** The abstract is accepted for presentation; no proceedings version is confirmed. Consequences, binding on all downstream work:
> - **Not cited.** Removed from the bibliography.
> - **Never** described as published, previously published, a prior publication, or in proceedings.
> - The figures are **not** labelled "previously reported".
> - The relationship becomes an **internal originality and provenance constraint**: material developed for the earlier study must not be presented as newly created for AAI.
> - **Substantive differentiation is preserved unchanged** — earlier study: architecture, the three states, the graduated advisory-scope concept, the initial 5.81% / 4.48% characterisation. AAI: C0–C3 isolation, the admissible-set criterion, Δ_L2 semantics and the identity, sensitivity envelope, component attribution, vessel-class and denominator dependence, lower-bound interpretation.
> - **Re-check before submission.** If formally published by then: add the proceedings citation, disclose the relationship, identify the extension. If still unpublished: invent no citation, and follow the AAI/IEEE policy for accepted-but-unpublished related work.
> - ⚠️ **Recommended separately:** declare the accepted abstract in the submission form or cover letter, where venues normally ask for related work by the same authors. That satisfies disclosure obligations without a bibliography entry.

**I-5 · `aai-2026-track1-discovery.md` contains corrected errors.** Its revision note lists five, including a reversed robustness claim. 🔒 **The corrected values in its revision note govern; the original text does not.**

---

## 1. Paper identity

A short empirical paper that treats a governance control as an object of measurement rather than of design. It asks whether a declared intermediate risk level actually changes what an advisory system is permitted to recommend, supplies a specification-level criterion for deciding that, an instrument for testing it, and a disclosed measurement at one site. Every mechanism is conceded to established prior art.

**It is not** an architecture paper, a runtime-assurance advance, a formal-methods paper, a human-centred study, or a coastal-fisheries application.

---

## 2. Problem

🔒 **LOCKED — three sentences, falsifiable, solution-independent.**

> AI governance designs are commonly specified by the risk levels they declare, but a declared level constrains system behaviour only if it changes the set of actions the governed system is permitted to take. Whether a given level does so, and how often that constraint is actually reached under operating conditions, is not determined by the specification and is not established by declaring the level. Both are therefore open to measurement, and neither is routinely measured.

**Why this form.** It is independent of the proposed architecture: it is a statement about governance specifications generally. It is falsifiable — a counterexample is any published governance design whose declared levels are shown to change permitted actions and whose activation is reported. It does not assume graduated governance is better than binary gating, and it does not mention fishers, safety or AI quality.

**Rejected problem statements and why:**

| Rejected | Reason |
|---|---|
| "Coastal fishers need safer AI decision support" | Domain motivation, not a research problem; and safety is a non-claim |
| "Binary gating is insufficient" | Assumes the conclusion; C1 is the comparator, not a deficiency |
| "Graduated governance improves outcomes" | Unsupported by any evidence here |
| "There is no operational specification combining these mechanisms" | This is Gap A, which the report itself calls *"a modest composition gap… not an architecture gap"* |

---

## 3. Prior art boundary

🔒 **`MECHANISM_NOVELTY = WITHDRAWN`. The following are conceded on page 1 of the manuscript and may never be claimed.**

| Mechanism | Conceded to |
|---|---|
| Runtime assurance; bounding a complex function with a verified monitor | **ASTM F3269** — *Methods to Safely Bound Behavior of Aircraft Systems Containing Complex Functions Using Run-Time Assurance* |
| Supervisory switching to a safe controller | Sha, Simplex architecture |
| Pre-inference / preemptive restriction of the action set | **Alshiekh et al., AAAI 2018** — preemptive vs post-posed shielding |
| Advisory-type inhibition conditioned on external state | FAA AC 20-151C (TCAS II); TSO-C151c §5.6 (TAWS) |
| State-conditioned admissible action sets `A(s)` | Standard MDP formalism (Puterman) |
| Totality of classification over incomplete observations | Bauer, Leucker & Schallhart (2011); Taleb, Hallé & Khoury (2023) |
| Fail-safe / degraded-mode resolution; ODD exit | Gyllenhammar et al. (2025) |
| Graduated multi-level governance | Flehmig et al. (2024); Shamsujjoha et al. (2025) |
| Levels individuated by function allocation rather than label count | **Parasuraman, Sheridan & Wickens (2000)**, *IEEE Trans. SMC-A* 30(3):286–297 |
| Directional bounds from declared unmeasured variables | Manski (1990, 1997); Manski & Pepper (2000) |
| Human final authority as an architectural pattern | AC 20-151C §2.1.1 |

**P1–P4 are not new theory.** They support the chain and carry no novelty. P2 is "true by definition of `A_AI`" (report). P4 is definitional — see §17.

---

## 4. General literature problem

🔒 **LOCKED.**

> Responsible AI has a documented **principles-to-practice gap**: governance commitments and controls are specified far more often than their operational effect is measured. The NIST AI RMF addresses this structurally through its **MEASURE** function, which exists because a declared control must be shown to function in deployment. Existing mechanism literature — runtime assurance, shielding, supervisory control, levels of automation — establishes *how* to restrict a system's permitted actions by state, but not *whether or how often* a particular declared level does so in a given deployment.

**This is positioning, not novelty.** The gap is a property of the field; the paper contributes one measurement into it.

---

## 5. Specific empirical gap

🔒 **LOCKED — this is Gap B from the authoritative report, narrowed.**

> Within the reviewed literature, no empirical characterisation was identified of **how often an intermediate advisory-scope governance level changes the admissible recommendation set relative to a participation-only gate**, when replayed over a multi-year environmental record.

**Why it is defensible:** the report states it "could have returned a null result" — it is a question whose answer was not entailed. It is narrow, site-scoped, and does not claim that no one has measured anything adjacent.

### NOT the gap

| Not the gap | Because |
|---|---|
| No one restricts AI capability by risk state | ASTM F3269, TCAS II, shielding all do |
| No one restricts before inference | Alshiekh et al. 2018, preemptive shielding |
| No one separates participation from scope | ⚠️ And in this instantiation `G(S) = 1 ⟺ A_AI(S) ≠ ∅`, so the two are not independent. The report's claim is separation from *a single graduated index*, which is narrower |
| No one has stated that levels must change behaviour | Implicit in Parasuraman et al. (2000) and SAE J3016 |
| No operational specification composes these mechanisms | Gap A — the report calls it modest and "not an architecture gap" |
| No one governs AI for coastal fisheries | A domain absence, not a research gap |

---

## 6. Primary research question

🔒 **LOCKED — ONE primary RQ.**

> **RQ1.** Over a multi-year environmental record for one deployment site, how often does an intermediate advisory-scope governance level change the admissible recommendation set relative to a participation-only gate, and how sensitive is that frequency to defensible threshold, vessel-class and denominator-policy configurations?

**Answerable in full from existing evidence.** Requires no new experiment, no users, no generated advice, no second site.

---

## 7. Supporting criterion — not a second RQ

🔒 **LOCKED: the candidate RQ2 is demoted to a specification criterion stated in the method.**

The candidate was: *"Under what condition does adding an intermediate risk level to a governance design change system behaviour rather than only its description?"*

**It must not be an RQ.** Its answer follows entirely from the definitions of C1, C2 and C3 — a question whose answer is known from definitions alone is not a research question, and presenting it as one invites reviewer attack 3 ("identical by definition") with no defence. The report is explicit that the 0.00% "follows from the comparator definitions rather than from the data."

🔒 **Locked form — stated in the method section as a criterion, before any result:**

> **Criterion (admissible-set individuation).** A declared risk level changes the governance behaviour of a system only if it changes the admissible action set. Two governance configurations that assign identical admissible sets at every state are the same governance function, whatever their state cardinality.

**Status:** a specification-level criterion, restating for AI governance a principle already implicit in the levels-of-automation literature. Its contribution is that it is stated explicitly, made auditable, and instantiated.

### The metric identity — locked as metric interpretation

🔒 `Δ_L2 ≡ P(S = CAUTION)` is **a metric-interpretation proposition stated in the method, before results.** It is not a result, not a finding, not a contribution in itself.

**Why method and not results.** It is derived from the C1/C2 mappings, not measured; the numerical verification (<1e-9) is a conformance check on the implementation. Stating it before the result converts reviewer attack 4 from an exposure into evidence of rigour. Stating it after — or omitting it — is fatal.

---

## 8. Formal object being evaluated

🔒 **LOCKED.**

```
E  →  S = f(E)  →  (G(S), A_AI(S))  →  AI(E)  →  Human
```

| State | `G(S)` | `A_AI(S)` |
|---|---|---|
| SAFE | 1 | FULL = {Go, Delay, DepartureTime, Duration} |
| CAUTION | 1 | **{Go, Delay}** |
| UNSAFE | 0 | ∅ |

`f(E) = max-severity(g_w, g_r, g_m, g_o, g_t)`; vessel category `v` parameterises `g_o` rather than contributing an independent term.

**The evaluated object is `A_AI(S)` — the admissible recommendation set.** `G(S)` is mentioned once and never built upon, because `G(S) = 1 ⟺ A_AI(S) ≠ ∅` in this instantiation.

**Researcher-defined and declared as such:** `A_AI(CAUTION) = {Go, Delay}`; the three-state cardinality; the policy `night ⇒ UNSAFE`; the 05:00–09:00 departure window; the exclusion `D = {m}`.
**Externally sourced:** `g_w` (MET Cat 1/2); `g_r` UNSAFE (MET *Ribut Petir*); `g_o` (Yaakob et al. 2015, operational ceiling); `g_t` boundary (COLREGs Rule 20(b)). `g_r` CAUTION is sourced (JPS/DID *Light* limit) but **non-MET**, because MET publishes no criterion below 20 mm/hr.

---

## 9. Comparator logic

🔒 **LOCKED.**

| | Name | A_AI(SAFE) | A_AI(CAUTION) | A_AI(UNSAFE) | Role |
|---|---|---|---|---|---|
| **C0** | Ungated | FULL | FULL | FULL | Zero point. Not a proposal |
| **C1** | Binary-gated | FULL | FULL | ∅ | The comparator the contribution must differ from |
| **C2** | Proposed | FULL | **{Go, Delay}** | ∅ | Identical to C1 except one cell |
| **C3** | Three-state topology | FULL | FULL | ∅ | Structural comparator |

**C3's provenance is load-bearing and must be stated.** §7.2: C3 ports **Flehmig et al.'s** governance *topology* onto this paper's environmental conditioning variable. Flehmig condition on AI degradation, not environmental state. 🔒 The manuscript must carry the report's fairness qualification verbatim in substance: C3 is **not** a reproduction of their system, **not** a test of their architecture on their problem, and **not** a claim that their framework is deficient.

---

## 10. Metric and interpretation

🔒 **LOCKED.**

`Δ_L2` = proportion of departure-window hours in which C2 admits a strictly smaller recommendation set than C1.

- **Isolation:** Δ_L2 = (C0↔C2) − (C0↔C1) = 48.69% − 42.88% = 5.81%, cross-checked by direct pairwise C1↔C2 = 5.81%.
- **Identity:** Δ_L2 ≡ P(S = CAUTION) — stated in the method (§7).
- **Status:** a deterministic census over every hourly record in a predefined window. **No p-values, confidence intervals or significance tests apply** (limitation 8). The envelope is a deterministic sensitivity range and must never be written as "5.81% ± x".

---

## 11. Evidence

| Quantity | PRIMARY | RESOLUTION |
|---|---|---|
| Hourly records | 43,848 | 28,501 |
| Period | 2020-01 → 2024-12 (5.00 yr) | 2021-10 → 2024-12 (3.25 yr) |
| Wave source | ERA5-Ocean ~50 km | MFWAM ~8 km |
| Departure-window denominator (05:00–09:00, <10 GRT) | **9,135** | **5,935** |
| **Δ_L2** | **5.81%** | **4.48%** |
| C0↔C1 (Level 1 alone) | 42.88% | *withheld* |
| C0↔C2 (Levels 1+2) | 48.69% | *withheld* |
| C1↔C3 (entailed) | **0.00%** | **0.00%** |

Site: Kota Kinabalu, Sabah. Reproduced from canonical scripts on 2026-09-21 (Python 3, pandas 2.3.3, numpy 2.2.6).

🔒 RESOLUTION pairwise components remain withheld under `RESOLUTION_PAIRWISE_C0_C1_C0_C2 = PROVENANCE_INCOMPLETE`. **Do not invent them.** Δ_L2 is unaffected.
🔒 `age_i` freshness parameter remains **OPEN**. Do not invent a value.

---

## 12. Sensitivity and negative findings

🔒 **All of the following are MUST-REPORT. The headline may never be presented alone.**

**Three distinct sensitivity statements — do not conflate (see I-2):**

| Statement | Value | What it is |
|---|---|---|
| Sourced-threshold envelope, small vessel | **5.67 – 9.56%** PRIMARY · 4.26 – 6.64% RESOLUTION | Range across externally sourced threshold configurations |
| Wave-onset perturbation ±0.25 m | **2.54 – 14.75%** | Deterministic perturbation range |
| **Two defensible readings of the same source** | **5.81% and 9.22%** | Yaakob et al. support both *operational ceiling* and *failure point* for the small-vessel UNSAFE boundary |

**Component dominance.** Wave onset is the principal determinant at ≈ **−1.4 percentage points per 0.05 m**. Rainfall is minimal (0.48 pts PRIMARY / 0.78 RESOLUTION) — **the non-MET rainfall boundary is not driving the headline.** Wind is a **structural zero** across `W_C` 18–25 kn.

**Attribution — PRIMARY, departure window, 531 CAUTION hours:**

| Component | Binding | Share | Status (see I-1) |
|---|---|---|---|
| `g_o` | 518 / 531 | **97.6%** | Dominant |
| `g_r` | 13 / 531 | 2.4% | |
| `g_w` | 0 | — | **Empirical negative finding** |
| `g_t` | 0 | — | Definitional — emits no CAUTION by construction |
| `g_m` | 0 | — | Structurally excluded, D = {m} |

🔒 Report as: **one component dominates at 97.6%; one further component (`g_w`) fails to bind empirically.** Not "three of five never bind."
🔒 Carry the report's scope note: F-7's "three functions bind" refers to max-severity binding **across all states**, where `g_t` dominates non-SAFE through darkness. The attribution table is **CAUTION-specific within the departure window**. Both are correct at their own scope.

**Scope dependence.** Vessel class: medium **1.96%**, large **1.26%** (0.66% / 0.37% RESOLUTION) — the report's word is "approaching vacuity." Denominator policy: daylight-only gives **9.59% / 7.40%**.

**Lower bound.** `g_m` has no historical archive and is held at `none` under `D = {m}`; since `g_m` can only raise severity, **every severity figure is a lower bound**.

**RQ3 answer, as a negative result.** The five-component specification "remains defensible as a transferable specification, but the evaluated record does not empirically warrant equal importance of all five components at this deployment site."

---

## 13. Contribution ledger

**Target met: three contributions.**

| # | Candidate | Classification |
|---|---|---|
| 1 | Architecture | **NOT A CONTRIBUTION** — conceded to ASTM F3269 / Simplex / TCAS II; and developed in the earlier study |
| 2 | Three-state classifier | **NOT A CONTRIBUTION** — developed in the earlier study |
| 3 | `G(S)` | **NOT A CONTRIBUTION** — derivable from `A_AI(S)` |
| 4 | `A_AI(S)` | **NOT A CONTRIBUTION** — textbook `A(s)`; developed in the earlier study |
| 5 | Separating participation from advisory scope | **NOT A CONTRIBUTION** — not independent as instantiated; the narrower claim (separation from a single graduated index) is exposition |
| 6 | **C0–C3 comparator design** | **PRIMARY** (component) |
| 7 | **Audit criterion** | **SECONDARY** |
| 8 | C1 ≡ C3 | **SUPPORTING** — definitional; the criterion's instance |
| 9 | 0.00% replay | **SUPPORTING** — executable conformance check, not evidence |
| 10 | 5.81% / 4.48% | **SUPPORTING** — originate in the earlier study; enter as the measured quantity, not as novelty |
| 11 | **Δ_L2 ≡ P(S=CAUTION)** | **PRIMARY** (component) |
| 12 | **Threshold sensitivity + envelope** | **PRIMARY** (component) |
| 13 | **Component attribution** | **SECONDARY** |
| 14 | Vessel-class sensitivity | **PRIMARY** (component) |
| 15 | Denominator sensitivity | **PRIMARY** (component) |
| 16 | P1–P4 | **SUPPORTING** — explicitly not new theory |
| 17 | Declared-exclusion lower bound | **PRIMARY** (component) |
| 18 | Threshold provenance | **SUPPORTING** |
| 19 | Explicit non-claims | **SUPPORTING** |
| 20 | Coastal-fisheries operationalisation | **NOT A CONTRIBUTION** — the setting; and the IPoSCI framing |

### PRIMARY CONTRIBUTION

> **An interpretive apparatus for governance-activation measurement, instantiated once.** The activation rate of an intermediate advisory-scope level, isolated by a comparator ladder (C0–C3), reported with the interpretation of what the metric identifies (Δ_L2 ≡ P(S=CAUTION)), its sourced-threshold envelope, its dominant determinant, its vessel-class and denominator-policy dependence, and its lower-bound status under a declared exclusion.

- **What exactly is new:** not the number, and not any mechanism — the **composition** of isolation, metric-semantics, sensitivity, scope-dependence and bounding into a single reported characterisation of whether and how often a declared governance level takes effect. No comparable characterisation was located (Gap B).
- **Evidence:** §§11–12 in full; reproduced from canonical scripts 2026-09-21.
- **Prior art it does NOT replace:** ASTM F3269, Simplex, shielding, TCAS II, levels of automation, MDP `A(s)`, runtime-verification totality, Manski. None of these is displaced or improved upon.
- **Narrowest defensible claim:** *"At one site, for one vessel class, under a declared exclusion, we characterise how often an intermediate advisory-scope level changes the admissible recommendation set, and we report what that measurement does and does not identify."*

### SECONDARY CONTRIBUTION 1

> **An auditable criterion for whether a declared risk level changes governance behaviour**, with a worked instance in which a published governance topology, ported to this conditioning variable, does not.

- **What exactly is new:** the explicit statement of a behavioural-individuation criterion **for AI governance designs**, made auditable, with an instance. Not the underlying principle.
- **Evidence:** the C1/C2/C3 specifications; C1↔C3 = 0.00% as conformance.
- **Prior art it does NOT replace:** Parasuraman, Sheridan & Wickens (2000) and SAE J3016 already individuate levels by function allocation. 🔒 **This must be cited as the source of the principle.**
- **Narrowest defensible claim:** *"We state a criterion, and exhibit one ported topology where a declared level does not satisfy it."* Not that governance designs generally fail it.

### SECONDARY CONTRIBUTION 2

> **A negative finding on component warrant:** at this site the intermediate classification is 97.6% attributable to one component, and one further component fails to bind at all.

- **What exactly is new:** an empirical demonstration that a multi-component governance classifier may be effectively single-component in deployment — which the activation figure alone conceals.
- **Evidence:** §8.1 attribution over 531 CAUTION hours; wind structural zero across 18–25 kn.
- **Prior art it does NOT replace:** nothing; this is a site-specific empirical observation.
- **Narrowest defensible claim:** the specification remains defensible as transferable; **the evaluated record does not warrant equal component importance at this site.**

---

## 14. Central claim

🔒 **LOCKED.**

> **This paper establishes that** a declared intermediate risk level changes an advisory system's permitted recommendations only if it contracts the admissible set — a three-state topology that does not contract it is the same governance function as a binary gate — and that for one governance design at one site the contracting level is reached in 5.81% of departure-window hours as a lower bound, within a sourced-threshold envelope of 5.67–9.56% that is 97.6% attributable to a single environmental component and falls to 1.96% and 1.26% for larger vessel classes.

> **This paper does NOT establish that** the restriction is correct, optimal, safer, or beneficial; that `{Go, Delay}` is the right admissible set; that the measured rate is a stable property of the site; that any human understood, trusted or acted differently because of the restriction; that any safety or decision-quality outcome changed; or that the criterion or the measurement generalises beyond the single design, site and vessel class evaluated.

### Attack survival

| Attack | Survives? | Why |
|---|---|---|
| 5.81% is P(CAUTION) | ✅ | The claim says "is reached in", an activation statement. The identity is stated in the method |
| C1 ≡ C3 is definitional | ✅ | The claim says "is the same governance function" — a definitional statement, asserted as such |
| Wave threshold dominates | ✅ | "97.6% attributable to a single environmental component" is **in the claim** |
| {Go, Delay} is researcher-defined | ✅ | The claim asserts nothing about the set's content; the non-claim says so explicitly |
| No generated advice evaluated | ✅ | "Permitted recommendations", never "recommendations given" |
| No users studied | ✅ | No human term appears in the claim |
| No safety outcome | ✅ | No outcome term appears; the non-claim excludes it |

---

## 15. Responsible AI connection

🔒 **LOCKED.**

> **RESPONSIBLE AI CONNECTION:** Responsible AI governance is specified far more often than its operational effect is measured — the documented principles-to-practice gap — and the NIST AI RMF's **MEASURE** function exists precisely because a declared control must be shown to function in deployment; this paper contributes one such measurement, together with a criterion for distinguishing a risk level that constrains permitted actions from one that only appears in the specification.

> **RESPONSIBLE AI NON-CLAIM:** The paper contributes **no** Responsible AI mechanism, no ethical analysis, no fairness, explainability or accountability result, no evidence that human oversight is effective, and no claim that the governed system is safer, more trustworthy or better aligned; the architecture itself is conceded to established runtime-assurance practice.

**Literature test — does it hold?** Partially, and the partiality is stated rather than hidden. Supported: the principles-to-practice gap is documented in the AI-governance review literature, and MEASURE is a real anchor. Not supported: any claim that this constitutes a Responsible AI *advance*. 🔒 The connection is **positioning**, not contribution — the contribution is the measurement.

⚠️ **Known unresolved risk.** A substantial part of the Responsible AI reviewer population works on fairness, bias and explainability of learned models and may not recognise a model-free governance measurement as belonging to their area. Not fixable by writing. Accepted as a submission risk.

---

## 16. Role of coastal fisheries

🔒 **LOCKED — one sentence.**

> **Coastal fisheries functions in this paper as** the evaluation setting that supplies a multi-year environmental record and a vessel-class-specific threshold set against which the governance measurement is performed — not as the subject, contribution, or motivation of the paper.

**Consequences.** Fisheries does not appear in the title. Domain background is at most three sentences, present only to establish why the environmental record exists and why one component is structurally unavailable. Any sentence that would survive unchanged in the IPoSCI abstract is a warning sign.

---

## 17. Claim/evidence matrix

🔒 **Any claim not in this matrix may not enter the manuscript.**

| Claim | Evidence | Status | Where used |
|---|---|---|---|
| A declared level changes governance behaviour only if it contracts the admissible set | C1/C2/C3 specifications | **DEFINITIONAL** | Method — criterion |
| C1 and C3 are the same governance function | Identical `A_AI` at all states | **DEFINITIONAL** | Method — criterion |
| C1↔C3 = 0.00% on the evaluated trace | Replay | **DEFINITIONAL** (conformance check) | Results — one line, labelled entailed |
| Δ_L2 ≡ P(S = CAUTION) | Derived from C1/C2; verified <1e-9 | **DEFINITIONAL** | Method — metric interpretation |
| The intermediate level is reached in 5.81% / 4.48% of window hours | 9,135 / 5,935 hours | **SUPPORTED** | Results — headline |
| Level 2's contribution is isolable from Level 1 | 48.69% − 42.88%; pairwise cross-check | **SUPPORTED** | Results |
| The figure is a lower bound | D = {m}; `g_m` can only raise severity; Manski | **SUPPORTED** | Results + limitations |
| Sourced-threshold envelope is 5.67–9.56% | Sensitivity | **SUPPORTED** | Results — reported with the headline |
| The same source admits a second reading giving 9.22% | Limitation 2 (Yaakob: ceiling vs failure point) | **SUPPORTED** | Limitations |
| Wave onset is the dominant determinant (≈ −1.4 pts / 0.05 m) | Sensitivity | **SUPPORTED** | Results |
| The rainfall boundary is not driving the headline | 0.48 / 0.78 pts | **SUPPORTED** | Results |
| `g_o` accounts for 97.6% of CAUTION hours | 518/531 | **SUPPORTED** | Results |
| `g_w` fails to bind empirically | 0/531; two activations in 43,848 h | **SUPPORTED** | Results |
| `g_t` cannot bind CAUTION | By construction | **DEFINITIONAL** | Results — labelled |
| `g_m` does not bind | Structural exclusion D = {m} | **DEFINITIONAL** | Results — labelled |
| The record does not warrant equal component importance at this site | Attribution | **SUPPORTED WITH QUALIFICATION** — site-specific | Results / discussion |
| Near-vacuity for larger vessel classes (1.96% / 1.26%) | Limitation 3 | **SUPPORTED** | Limitations |
| Daylight-only denominator gives 9.59% / 7.40% | Limitation 4 | **SUPPORTED** | Limitations |
| Classification is total under a declared exclusion | P1 | **SUPPORTED** | Method — one sentence |
| Containment holds | P2 | **DEFINITIONAL** ("true by definition") | Method — one sentence |
| Implementation conforms to its governance contract | P3; fidelity criteria | **SUPPORTED** | Method — one clause |
| Four thresholds trace to named authorities; three choices are researcher-defined | §5.1 | **SUPPORTED** | Method |
| The rainfall CAUTION boundary is sourced but non-MET | §5.1; MET publishes nothing below 20 mm/hr | **SUPPORTED** | Method |
| C3 ports Flehmig et al.'s topology onto this conditioning variable | §7.2 | **SUPPORTED WITH QUALIFICATION** — not a reproduction, not a test of their system | Method — with fairness note |
| The architecture does not automate the departure decision | Specification | **SUPPORTED** (specification register only) | Method — one sentence |
| No statistical inference applies | Limitation 8 — deterministic census | **SUPPORTED** | Method/limitations |
| Anything about generated advice content | — | **PROHIBITED** (limitation 7) | Nowhere |
| Human oversight is effective / meaningful human control | — | **PROHIBITED** | Nowhere |
| Human-centred, trusted, accepted, usable | — | **PROHIBITED** | Nowhere |
| Safety, accident reduction, decision quality, accuracy | — | **PROHIBITED** | Nowhere |
| Optimality of thresholds, state count, or `A_AI(CAUTION)` | — | **PROHIBITED** | Nowhere |
| Generalisation across sites, Sabah, or vessel classes | — | **PROHIBITED** | Nowhere |
| Any mechanism novelty | — | **PROHIBITED** (`MECHANISM_NOVELTY = WITHDRAWN`) | Nowhere |
| The headline is a stable site property | Contradicted by §8 | **PROHIBITED** | Nowhere |
| The criterion or ladder generalises | One instance | **NOT SUPPORTED** | Nowhere as a claim |

---

## 18. IPoSCI differentiation

**ALREADY REPORTED IN IPoSCI:** four-layer architecture · SAFE/CAUTION/UNSAFE · S = f(E), E = {w,r,m,o,v,t} · the governance contract table · graduated safety-state gating · Δ = (N_restricted/N_eval)×100% · **5.81% / 4.48%**.

**NEW ANALYSIS FOR AAI:** C0–C3 comparator design · C0↔C1 = 42.88% and C0↔C2 = 48.69% decomposition · threshold sensitivity and the 5.67–9.56% envelope · wave-dominance quantification · component attribution (`g_o` 97.6%; `g_w` non-binding) · vessel-class variants · daylight-only denominator variant · common-period attribution (+1.97 / −0.64).

**NEW INTERPRETATION:** Δ_L2 ≡ P(S=CAUTION) and its consequence that the headline is invariant to the content of `A_AI(CAUTION)` · the reframing of 5.81% from a headline figure into a lower-bounded, threshold-sensitive, single-component-dominated, class-specific activation measurement · C1 ≡ C3 recast as an auditable criterion.

**SUPPORTING EXTENSION:** P1–P4 · declared-exclusion lower-bound argument · threshold provenance table · prediction register.

**PROVENANCE STATUS (revised 2026-09-23):** 🔒 The IPoSCI extended abstract is **ACCEPTED but NOT CONFIRMED PUBLISHED**. It is therefore **not cited** in the manuscript and is **never described as published, previously published, or prior publication**. The figures are **not** labelled "previously reported". The relationship is an **internal originality and provenance control** during drafting, not a manuscript disclosure. **Re-check publication status before submission** — see §0, I-6.

### The decisive test

> *Would the proposed AAI paper still contain a substantive contribution if the 5.81% and 4.48% values — which originate in the earlier study — were removed from the novelty claim?*

🔒 **YES.**

The primary contribution is explicitly **not the number** (ledger item 10 is classified SUPPORTING, not a contribution). Removing 5.81%/4.48% from the novelty claim leaves intact: the comparator ladder and the isolation it enables; the criterion and its instance; the metric-interpretation proposition; the sensitivity envelope and wave dominance; the component-attribution negative finding; the vessel-class and denominator dependence; and the lower-bound status.

**The paper's position is that a bare activation figure is uninterpretable, and that what makes it interpretable is exactly the apparatus IPoSCI does not contain.** That is a different question about the same object, not the same paper with more detail.

⚠️ **This survives only if the manuscript leads with the criterion and the measurement apparatus.** If it leads with the architecture, the answer becomes NO and the chain must be reopened.

🔴 **Unresolved external dependency.** AAI is not one of IPoSCI's three publication routes. If the extended abstract defaults to the IPoSCI e-Proceedings it becomes **published** prior work. This changes disclosure obligations, not the research chain.

---

## 19. Six-page content boundary

| Item | Verdict |
|---|---|
| Responsible AI principles-to-practice motivation | **MUST INCLUDE** — ~3 sentences with the NIST MEASURE anchor |
| Runtime assurance prior art (ASTM F3269) | **MUST INCLUDE** — page 1 concession |
| Shielding prior art (Alshiekh et al.) | **MUST INCLUDE** — one citation in the concession |
| Levels-of-automation prior art (Parasuraman et al.) | **MUST INCLUDE** — sources the criterion's principle |
| Fisheries background | **USE IF SPACE** — max 3 sentences |
| Full architecture | **OMIT** |
| Architecture figure | **OMIT** — highest IPoSCI overlap, lowest density |
| E definition | **USE IF SPACE** — one line |
| Threshold table | **USE IF SPACE** — but the **wave onset and its source MUST appear** |
| SAFE/CAUTION/UNSAFE contract | **MUST INCLUDE** — Table 1 |
| `G(S)` | **USE IF SPACE** — one mention, not built upon |
| `A_AI(S)` | **MUST INCLUDE** |
| C0–C3 | **MUST INCLUDE** — Table 2 |
| P1 | **USE IF SPACE** — one sentence |
| P2 | **USE IF SPACE** — one sentence, labelled definitional |
| P3 | **OMIT** from body — one clause in evaluation |
| P4 | **MUST INCLUDE** — as the criterion, never as a result |
| Δ definition | **MUST INCLUDE** |
| Δ identity | **MUST INCLUDE — in the method, before results** |
| PRIMARY dataset | **MUST INCLUDE** — compressed to ~4 lines |
| RESOLUTION dataset | **MUST INCLUDE** — one table column |
| 5.81% | **MUST INCLUDE** |
| 4.48% | **MUST INCLUDE** |
| 5.67–9.56% envelope | **MUST INCLUDE — never the point figure alone** |
| Wave dominance | **MUST INCLUDE** |
| Component attribution | **MUST INCLUDE** |
| Vessel-class analysis | **MUST INCLUDE** — one table row (it is in the central claim) |
| Denominator analysis | **USE IF SPACE** — one sentence |
| Lower-bound interpretation | **MUST INCLUDE** — two sentences |
| Prediction register | **USE IF SPACE** — one sentence |
| Provenance history | **OMIT** |
| Explicit limitations | **MUST INCLUDE** |
| IPoSCI extension disclosure | **OMIT from the manuscript** — see §0, I-6. Internal provenance control only |

**Budget (6 pages incl. references):** Intro + governance-measurement problem 0.75 · Prior art and concessions 0.75 · Contract and criterion 0.75 · Comparator instrument and metric interpretation 0.75 · Results with envelope, attribution, class 1.5 · Limitations, non-claims, IPoSCI disclosure 0.75 · References 0.75.

**Figures/tables: 1 figure, 3 tables.** T1 governance contract · T2 comparator design (shows C1≡C3 by inspection) · T3 combined results incl. envelope, `g_o` share, vessel classes, denominator · F1 Δ_L2 against wave CAUTION onset with the envelope band marked.

---

## 20. Locked title candidates

| Candidate | Assessment |
|---|---|
| **A.** *Does Declaring a Risk Level Change What an AI May Do? Measuring Advisory-Scope Governance* | ✅ Precise — "may do" is permissions, not behaviour. Question form is honest. ⚠️ "AI" slightly strained (no model is exercised) |
| **B.** *Measuring Whether Graduated AI Governance Is Graduated in Behaviour* | 🔴 **Rejected.** "Behaviour" is readable as *generated AI behaviour*, which is never evaluated (limitation 7). Fatal ambiguity |
| **C.** *From Declared Risk Levels to Admissible Recommendations: Measuring the Operational Effect of AI Governance* | ✅ **Strongest.** "Admissible recommendations" is the exact evaluated object with no behavioural ambiguity; "operational effect" matches NIST MEASURE; the subtitle scopes the broad "AI governance" |
| **D.** *When Risk Levels Do Not Restrict: An Auditable Criterion for Graduated AI Governance* | ⚠️ Foregrounds the **criterion**, which is definitional and the *secondary* contribution. Promises the weaker half |
| *Adding a State Is Not Adding Governance…* | 🔴 **Rejected** (I-4). Announces a discovery; delivers a definition |

**Checks applied to the primary:** "AI" is justified because the governed object is an AI advisory layer, even though no model is exercised — and the abstract states this. "Governance" is broad, but bounded by "admissible recommendations". "Behaviour" is avoided entirely. Fisheries is absent. No reviewer expectation is created that the evidence cannot meet.

🔒 **PRIMARY TITLE:** *From Declared Risk Levels to Admissible Recommendations: Measuring the Operational Effect of AI Governance*
🔒 **ALTERNATIVE 1:** *Does Declaring a Risk Level Change What an AI May Do? Measuring Advisory-Scope Governance*
🔒 **ALTERNATIVE 2:** *Measuring the Operational Effect of an Intermediate Advisory-Scope Governance Level*

**Why the primary is safest:** it names the exact object (`admissible recommendations`), promises a measurement rather than a discovery or a mechanism, anchors to the one Responsible AI framing the literature supports, avoids every prohibited term, and cannot be confused with the IPoSCI architecture paper.

---

## 21. Final reviewer falsification

| # | Attack | Verdict | Response |
|---|---|---|---|
| 1 | "Just runtime assurance" | ⚠️ **PARTIAL** | Correct about the mechanism, conceded on page 1 to ASTM F3269. The contribution is the measurement, not the mechanism. Fatal only if the paper leads with the architecture — which §19 forbids |
| 2 | "The criterion is obvious" | ⚠️ **PARTIAL** | Agreed; it is definitional and its principle is cited to Parasuraman et al. (2000). It is stated because it is *not* routinely applied to AI governance designs, and C3 is a worked instance where it fails |
| 3 | "C1 and C3 are identical by definition" | ✅ **SUPPORTED — by agreeing** | Stated as definitional in the method; the 0.00% is labelled a conformance check, never a result |
| 4 | "5.81% is just P(CAUTION)" | ✅ **SUPPORTED** | Derived and stated in the method before results; reframed as what the metric identifies |
| 5 | "Depends heavily on the wave threshold" | ⚠️ **PARTIAL — volunteered** | Envelope 5.67–9.56%, ±0.25 m → 2.54–14.75%, and the same source's second reading giving 9.22%, all reported. The headline is never called stable |
| 6 | "No AI in the replay" | ⚠️ **PARTIAL** | True and conceded (limitation 7). The object of study is the governance layer, whose admissible sets are well-defined independently of what they govern. A genuine scope limitation |
| 7 | "No users" | ✅ **SUPPORTED — by claiming nothing** | Human authority appears only in the specification register. No human-centred term appears anywhere |
| 8 | "No safety outcomes" | ✅ **SUPPORTED** | Explicit non-claim; no incident record exists for the site (limitation 5) |
| 9 | "The advisory restriction is researcher-defined" | ✅ **SUPPORTED** | Conceded with its domain rationale labelled as not constituting validation — and the identity makes it **costless**, since the headline is invariant to that choice |
| 10 | "This overlaps earlier work by the same authors" | ⚠️ **PARTIAL — answered by content, not by a disclosure sentence** | The figures were; the ladder, decomposition, identity, envelope, attribution, class and denominator analyses were not. §18's test answers YES |
| 11 | "Only a fisheries application" | ⚠️ **PARTIAL** | Defensible only because fisheries is the evaluation setting and appears in neither title nor contribution. A writing-dependent outcome |
| 12 | "Too small for an AI conference" | ⚠️ **PARTIAL — the weakest point** | The contribution is deliberately modest: one measurement, one criterion, one negative finding, at one site. In a 4–6 page format that is a proportionate contribution. **Not resolvable by evidence**, and compounded by the reviewer-population risk in §15 |

**Tally: 5 supported · 7 partial · 0 unresolved.**

🔒 **No attack invalidates the PRIMARY contribution.** Attacks 1, 6, 10 and 11 constrain how the paper must be written — all four are already binding constraints in §19. Attack 12 is a reviewer-judgement risk, not a defect in the chain.

---

## 22. Lock decision

**CHAIN STATUS: LOCKED**, subject to four binding conditions that drafting may not relax.

1. **Lead with the criterion and the measurement.** Leading with the architecture makes §18's test fail and reopens the chain.
2. **Concede all mechanisms on page 1** — ASTM F3269, Alshiekh et al., TCAS II/TSO-C151c, Parasuraman et al.
3. **Never report the headline alone.** The envelope, wave dominance, `g_o` share and vessel-class figures travel with it.
4. **Carry the differentiation in the content, not in a citation.** The IPoSCI abstract is accepted but unpublished: it is not cited, and nothing is called previously published. The paper's distinctness must therefore rest entirely on §18's removal test, which it passes. **Re-check publication status before submission.**

**Honest assessment.** This is a modest contribution, and the chain is locked as modest rather than inflated. Its strength is that every claim is either measured or labelled definitional, and every known weakness is volunteered in the paper rather than left for a reviewer. Its risk is audience, not soundness.

---

TRACK: Track 3 — Robotics, Autonomous & Human-Centred Intelligent Systems.

SUBTOPIC: Responsible, Ethical & Human-Centred AI — positioned strictly under *Responsible*, with no ethical and no human-centred claim.

PAPER IS ABOUT: whether a declared intermediate risk level actually changes the set of recommendations an advisory system is permitted to make, how that can be audited, and how often it does so at one evaluated site.

PAPER IS NOT ABOUT: a new governance mechanism, a runtime-assurance advance, a knowledge representation, a human-centred or ethical evaluation, or an AI decision-support system for coastal fisheries.

PROBLEM: AI governance designs are specified by the risk levels they declare, but a declared level constrains behaviour only if it changes the permitted action set, and neither that property nor the frequency with which the level is reached is established by the specification.

GAP: No empirical characterisation was identified of how often an intermediate advisory-scope governance level changes the admissible recommendation set relative to a participation-only gate, replayed over a multi-year environmental record.

PRIMARY RQ: Over a multi-year environmental record for one deployment site, how often does an intermediate advisory-scope governance level change the admissible recommendation set relative to a participation-only gate, and how sensitive is that frequency to defensible threshold, vessel-class and denominator-policy configurations?

SUPPORTING CRITERION: A declared risk level changes governance behaviour only if it contracts the admissible action set; two configurations assigning identical admissible sets at every state are the same governance function regardless of state cardinality — stated in the method as a criterion, not as a research question.

PRIMARY CONTRIBUTION: An interpretive apparatus for governance-activation measurement — comparator isolation, metric-semantics, sensitivity envelope, component attribution, scope dependence and lower-bound status — instantiated once on a real environmental record.

SECONDARY CONTRIBUTION: An auditable criterion for whether a declared risk level changes governance behaviour, with a worked instance in which a ported published topology does not satisfy it; and the negative finding that the intermediate classification is 97.6% attributable to one component while a second fails to bind empirically.

CENTRAL CLAIM: A declared intermediate risk level changes an advisory system's permitted recommendations only if it contracts the admissible set, and for one governance design at one site the contracting level is reached in 5.81% of departure-window hours as a lower bound, within a sourced-threshold envelope of 5.67–9.56% that is 97.6% attributable to a single environmental component and falls to 1.96% and 1.26% for larger vessel classes.

RESPONSIBLE AI CONNECTION: Responsible AI governance is specified far more often than its operational effect is measured, and the NIST AI RMF MEASURE function exists because a declared control must be shown to function in deployment — this paper contributes one such measurement plus a criterion for telling a constraining level from a declared one.

COASTAL FISHERIES ROLE: The evaluation setting supplying the environmental record and vessel-class thresholds — not the subject, contribution or motivation.

C1/C3 STATUS: Definitional — C1 and C3 assign identical admissible sets at every state and are therefore the same governance function; the 0.00% replay value is an executable conformance check on the encoding and must never be presented as a discovered empirical result.

DELTA_L2 STATUS: An activation measurement, identically the CAUTION base rate for the evaluated mappings and therefore invariant to the content of A_AI(CAUTION), reported as a lower bound with its full sourced-threshold envelope rather than as a point figure.

PRIMARY TITLE: From Declared Risk Levels to Admissible Recommendations: Measuring the Operational Effect of AI Governance.

IPOSCI DIFFERENTIATION: The earlier study (accepted, not confirmed published — not cited) covered the architecture and the two headline figures; this paper contributes the comparator ladder, the decomposition, the metric-interpretation identity, the sensitivity envelope, the component attribution, the vessel-class and denominator dependence and the lower-bound status — the apparatus that makes an activation figure interpretable — and the paper survives with a substantive contribution even if the two figures are removed from the novelty claim.

NEW EXPERIMENT REQUIRED BEFORE DRAFTING: NO.

IF YES, EXACTLY WHAT: Not applicable. All evidence required by the locked chain exists and was reproduced from canonical scripts on 2026-09-21. `age_i` remains OPEN and `RESOLUTION_PAIRWISE_C0_C1_C0_C2` remains withheld; neither is required by any locked claim, and neither may be invented.

CHAIN STATUS: **LOCKED** — subject to the four binding conditions in §22.

---

*Research chain locked 2026-09-23. `experiment-report-delta-l2.md` read in full and treated as authoritative; both discovery reports used analytically and their disagreements resolved explicitly in §0. No manuscript drafted.*
