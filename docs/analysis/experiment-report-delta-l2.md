# Experiment Report — Graduated Advisory-Scope Governance: Specification, Characterisation and Robustness

**Prepared for:** supervisory discussion
**Date:** 2026-09-21 (revised under `final-research-chain-lock.md`)
**Status:** Preliminary finding. Principal figures reproduced from canonical scripts on 2026-09-21.
**Subject:** Activation frequency of the intermediate advisory-scope state, Δ_L2 = 5.81% PRIMARY / 4.48% RESOLUTION, and its robustness.

---

## 1. What this report is

This report examines one question: where does the 5.81% come from, and what does it establish?

The experiment evaluates the isolated contribution of Level 2 advisory-scope governance by comparing the proposed graduated architecture against a participation-only gate over historical environmental conditions.

The principal experimental figures were reproduced from the canonical scripts on 2026-09-21: Δ_L2 = 5.81% under PRIMARY and 4.48% under RESOLUTION. Historical provenance and prediction-register figures reported later in this document are drawn from their authoritative records rather than recomputed by these scripts.

---

## 2. The research chain

```
+---------------------------------------------------------------------+
|  PROBLEM                                                            |
|  Fishers decide whether to put to sea under conditions they         |
|  cannot instrument. No marine-warning archive, no incident          |
|  register, and official criteria that state where warnings are      |
|  issued but never where caution should begin.                       |
+---------------------------------------------------------------------+
                              |
                              v
+---------------------------------------------------------------------+
|  PRIOR WORK — the underlying mechanisms are established             |
|                                                                     |
|  Restricting advisory types as conditions change                    |
|    → established in safety-critical aviation systems                |
|                                                                     |
|  Ensuring a classifier still returns a defined state when           |
|  observations are incomplete                                        |
|    → established in runtime verification                            |
|                                                                     |
|  Bounding conclusions when a required variable is unobserved        |
|    → established in partial-identification methods                  |
+---------------------------------------------------------------------+
                              |
                              v
+---------------------------------------------------------------------+
|  GAP A  operationalisation (modest)                                 |
|    Not found composed into ONE operational specification with       |
|    G(S) and A_AI(S) separately specified over a classified          |
|    multi-component ENVIRONMENTAL state, human-facing, low-resource  |
|                                                                     |
|  GAP B  empirical characterisation (stronger)                       |
|    No characterisation found of HOW OFTEN an intermediate           |
|    advisory-scope state changes the admissible set, over a          |
|    multi-year environmental record                                  |
+---------------------------------------------------------------------+
                              |
                              v
+---------------------------------------------------------------------+
|  RQ1 <- Gap A     RQ2, RQ3 <- Gap B                                 |
+---------------------------------------------------------------------+
                              |
                              v
+---------------------------------------------------------------------+
|  ARCHITECTURE — composition, not invention                          |
|                                                                     |
|     E  -->  S = f(E)  -->  (G(S), A_AI(S))  -->  AI(E)  -->  Human  |
|                                                                     |
|   SAFE     G=1   A_AI = {Go, Delay, DepartureTime, Duration}        |
|   CAUTION  G=1   A_AI = {Go, Delay}                                 |
|   UNSAFE   G=0   A_AI = {}                                          |
|                                                                     |
|   Containment: A_AI(SAFE) > A_AI(CAUTION) > A_AI(UNSAFE) = {}       |
+---------------------------------------------------------------------+
                              |
                              v
+---------------------------------------------------------------------+
|  EVALUATION — four conditions over 43,848 / 28,501 hourly records   |
|   C0 ungated · C1 participation-only · C2 proposed ·                |
|   C3 three-state with scope unchanged (structural comparator)       |
+---------------------------------------------------------------------+
                              |
                              v
+---------------------------------------------------------------------+
|  RESULTS                                                            |
|   EMPIRICAL   Delta_L2 = 5.81% PRIMARY / 4.48% RESOLUTION           |
|               envelope 5.67-9.56% over sourced thresholds           |
|               g_o binds 97.6% of intermediate-state hours           |
|   STRUCTURAL  C1 = C3 by construction; 0.00% on any trace           |
+---------------------------------------------------------------------+
```

**Reading the chain.** The underlying governance mechanisms are established; the research design problem therefore lies not in inventing those mechanisms, but in selecting, composing, and operationalising them for the target environmental decision-support setting, and that is Gap A. A composition that is never exercised on real conditions would be an empty formalism, and how often it is exercised cannot be derived by proof — that is Gap B, and it is the question the replay answers. A third state label changes nothing unless it changes the admissible set, which is why C3 exists and why its zero divergence is entailed rather than measured.

---

## 3. Prior work and the gap

### 3.1 What is conceded

The governance mechanisms used here are established, and the thesis claims novelty for none of them.

| Mechanism | Established by |
|---|---|
| Advisory-category inhibition conditioned on external state | FAA AC 20-151C (TCAS II) [[notes]](../../notes/Airworthiness%20Approval%20of%20Traffic%20Alert%20and%20Collision%20Avoidance%20Systems%20%28TCAS%20II%29%20%28FAA%20AC%2020-151C%29.md); TSO-C151c (TAWS) |
| **Human-facing advisory inhibition on observation validity** | TSO-C151c §5.6 — invalid position source ⇒ FLTA and PDA alerts inhibited, GPWS modes retained, inhibit annunciated to the crew |
| Multi-component classified runtime state | TCAS II: radio altitude, flap/slat/gear discretes, weight–altitude–temperature, airspeed margin, bank angle, one-engine-inoperative |
| Human final authority preserved | AC 20-151C §2.1.1 — *"TCAS II does not alter or diminish the pilot's basic authority and responsibility to ensure safe flight"* |
| Nested admissible sets, monotone contraction, weakest-link aggregation | Baxi (2026) [[notes]](../../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md); TCAS II inhibit schedule |
| Fail-safe / fail-degraded / fail-operational regimes | Gyllenhammar et al. (2025) [[notes]](../../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md) — ODD exit to Minimal Risk Condition |
| Totality of classification over incomplete observations | Bauer, Leucker & Schallhart (2011); Taleb, Hallé & Khoury (2023) |
| Directional bounds from declared unmeasured variables | Manski (1990, 1997); Manski & Pepper (2000) |
| Graduated multi-level governance; supervisory graduation | Flehmig et al. (2024) [[notes]](../../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md); Shamsujjoha et al. (2025) [[notes]](../../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md) |

### 3.2 Gap A — operationalisation

> Advisory-type restriction conditioned on an externally measured state is established practice in certified collision-avoidance and terrain-awareness avionics; totality of classification over incomplete observations is established in runtime verification; and directional bounds from declared unmeasured variables are standard in partial-identification methodology. Within the reviewed literature, these were not found composed into a single operational specification in which participation `G(S)` and admissible advisory scope `A_AI(S)` are separately specified over a classified multi-component environmental state, for a human-facing decision-support system in a low-resource setting where some conceptually required components are structurally unavailable.

This is a modest composition gap. The three ingredients come from unrelated fields, so their non-combination reflects disciplinary separation as much as an unexplored problem. It is not an architecture gap.

### 3.3 Gap B — empirical characterisation

> Within the reviewed literature, no empirical characterisation was identified of how often an intermediate advisory-scope state changes the admissible recommendation set relative to a participation-only gate, when replayed over a multi-year environmental record.

This is the stronger gap and it supports the primary contribution. It could have returned a null result.

---

## 4. Research questions

> **RQ1 — Operational specification.** Can AI participation and admissible advisory scope be specified as two separate state-conditioned functions over a classified multi-component environmental state such that classification remains total and the containment property is preserved when some conceptually required components are structurally unavailable — and which elements of that specification must be decided by the designer rather than derived from published sources?

> **RQ2 — Empirical characterisation and robustness.** Over a multi-year historical environmental record for the deployment site, how frequently does the intermediate safety state produce a stricter admissible recommendation set than a participation-only gate, and how sensitive is that frequency to defensible environmental-threshold and data configurations?

> **RQ3 — Structural warrant of the multi-component classifier.** Which components of the environmental state actually determine the intermediate classification at the deployment site, and is the multi-component structure warranted by the evaluated record?

Target-hardware latency is **not** a research question of this thesis. It is deferred deployment and prototype evaluation, outside the evidence required for the contribution. Contextual validation with fishers has **not** been conducted and is future socio-technical work, not a completed question.

---

## 5. Architecture

An operational architecture and specification that composes established safety-governance mechanisms — advisory-type restriction by externally measured state, totality of classification over incomplete observations, and conservative resolution of unusable inputs — for a human-facing decision-support setting in low-resource coastal fisheries. It is not a wholly novel safety architecture.

| | Content |
|---|---|
| **Inherited** | Advisory-type restriction by external state; nested contracting admissible sets; deterministic gating outside the generator; max-severity aggregation; fail-safe resolution; human final authority |
| **Domain adaptation** | The avionics inhibition pattern moved from one certified platform with a validity-checked navigation input to an unattended multi-source environmental classifier; runtime-verification totality moved from trace monitoring to component-wise environmental classification; vessel-conditional ocean thresholds |
| **Researcher-defined** | `A_AI(CAUTION) = {Go, Delay}`; three-state cardinality; the policy `night ⇒ UNSAFE`; departure window 05:00–09:00; exclusion `D = {m}`; dual-configuration reporting |
| **Empirically evaluated** | Intermediate-state activation frequency; its threshold and data-configuration sensitivity; component attribution |

### 5.1 The classifier

`f(E) = max-severity(g_w(w), g_r(r, κ), g_m(m), g_o(o, v), g_t(t, date))` — five component classifiers aggregated by worst case, with vessel category `v` parameterising the ocean-state thresholds rather than contributing an independent term.

| Component | SAFE | CAUTION | UNSAFE | Boundary source | Status |
|---|---|---|---|---|---|
| `g_w` (kn, sustained) | ≤ 21.6 | 21.6–27.0 | > 27.0 | MET Cat 1 / Cat 2 onsets (40 / 50 km/h) | Externally supported |
| `g_r` (mm/hr) | ≤ 10.0 | 10.0–20.0 | > 20.0 | UNSAFE: MET *Ribut Petir*. CAUTION: JPS/DID *Light* limit | UNSAFE externally supported; **CAUTION sourced but non-MET** |
| `g_o` small (m) | < 1.0 | 1.0–1.25 | > 1.25 | Yaakob et al. (2015) [[notes]](../../notes/Stability%2C%20Seakeeping%20and%20Safety%20Assessment%20of%20Small%20Fishing%20Boats%20Operating%20in%20Southern%20Coast%20of%20Peninsular%20Malaysia.md) operational ceiling | Externally supported |
| `g_t` | sunrise ≤ t < sunset | *(emits no CAUTION)* | otherwise | COLREGs Rule 20(b) | Boundary supported; **the abstention policy is researcher-defined** |

**Answering RQ1's second clause:** four boundaries trace to named authorities; three load-bearing choices — `A_AI(CAUTION) = {Go, Delay}`, the policy `night ⇒ UNSAFE`, and the three-state cardinality — are decided by the designer. MET publishes no criterion below 20 mm/hr, so the rainfall CAUTION boundary is necessarily non-MET; that is a documented gap in the source material, not a concealed choice.

### 5.2 The governance contract

| State | `G(S)` | `A_AI(S)` |
|---|---|---|
| SAFE | 1 | {Go, Delay, DepartureTime, Duration} |
| CAUTION | 1 | **{Go, Delay}** |
| UNSAFE | 0 | ∅ |

`A_AI(CAUTION) = {Go, Delay}` is a **researcher-defined design choice**. It has a domain rationale from cited fisheries literature — Gao (2024) and Rahim et al. (2024) indicate that under marginal conditions fishers continue to make go/no-go and near-shore decisions without necessarily optimising departure timing or trip duration. **That rationale does not constitute empirical validation, optimality evidence, or evidence of improved safety.**

---

## 6. Formal properties

Four properties are proved. They establish that the implementation satisfies its intended governance contract. **None is offered as new theory.**

| Property | What it means in this architecture | Status |
|---|---|---|
| **P1 — Totality** | Every valid environmental input is resolved to exactly one state: SAFE, CAUTION, or UNSAFE, including when a declared component is unavailable. | **Formalisation of an established mechanism** — totality over incomplete observations is established in runtime verification |
| **P2 — Advisory-Scope Containment** | As environmental severity increases, the set of advice that AI is allowed to provide can only stay the same or become smaller. | **Design property** — true by definition of `A_AI` |
| **P3 — Safety Dominance** | If the environmental state is UNSAFE, the AI advisory set must be empty; the AI cannot bypass the governance restriction. | **Contract-conformance property**, under assumptions A1–A4 |
| **P4 — Admissible-Set Equivalence of C1 and C3** | If CAUTION allows exactly the same advice as SAFE, adding the CAUTION label alone does not change governance behaviour relative to the participation-only comparator. | **Structural property** — the 0.00% replay value is harness consistency, not discovery |

**Formal traceability.** The formal results underlying P1–P3 are stated and proved in Appendix C — Formal Specification and Properties. The structural equivalence underlying P4 is established separately in the evaluation specification.

| Property | Formal result | Source |
|---|---|---|
| P1 — Totality | Theorem C.1 (ideal domains); Theorem C.1b (operational); Corollary C.1b.1 (fail-safe) | Appendix C §C.2 |
| P2 — Advisory-Scope Containment | Theorem C.2; Corollary C.2 (strict containment) | Appendix C §C.6 |
| P3 — Safety Dominance | Theorem C.3, under assumptions A1–A4 | Appendix C §C.7; proof in §C.7.2 |
| P4 — Admissible-Set Equivalence of C1 and C3 | Structural comparator proposition (`J1-P1` internally) | Evaluation Specification §6 |

Together, P1 and P2 establish that the classifier still returns a defined safety state and preserves the intended advisory containment even when a declared environmental component is structurally unavailable. This addresses the first part of RQ1. The mechanisms that achieve it are the declared exclusion set `D` and fail-safe resolution `gᵢ(⊥) = UNSAFE`: no value is fabricated for an unmeasured component, and the classifier is never left partial.

---

## 7. Evaluation

### 7.1 Site, data and unit of analysis

| | PRIMARY | RESOLUTION |
|---|---|---|
| Hourly records | 43,848 | 28,501 |
| Period | 2020-01 → 2024-12 (5.00 yr) | 2021-10 → 2024-12 (3.25 yr) |
| Weather source | `raw_weather_sea.csv` (5.940246 N, 116.025 E) | same |
| Wave source | ERA5-Ocean, ~50 km | MFWAM, ~8 km |
| **Departure-window denominator** | **9,135** | **5,935** |

Site: Kota Kinabalu, Sabah (5.98 N, 116.01 E), Open-Meteo archive. Unit of analysis: departure-window hours, 05:00–09:00, small vessel (< 10 GRT) — the deployment population.

### 7.2 The four conditions

Writing `FULL = {Go, Delay, DepartureTime, Duration}` and `∅` for the empty set:

| | Name | A_AI(SAFE) | A_AI(CAUTION) | A_AI(UNSAFE) | Purpose |
|---|---|---|---|---|---|
| **C0** | Ungated | FULL | FULL | FULL | Zero point. Not a proposal |
| **C1** | Binary-gated | FULL | FULL | ∅ | The comparator the contribution must differ from |
| **C2** | Proposed | FULL | **{Go, Delay}** | ∅ | Identical to C1 except one cell |
| **C3** | Traffic-light topology | FULL | FULL | ∅ | Structural comparator, not a fourth arm |

**Fairness qualification on C3.** Flehmig et al. condition their index on AI degradation — drift, outliers, performance decay — not on environmental state. C3 ports their governance *topology* onto our conditioning variable so the two structures can be compared on one axis. It is not a reproduction of their system, not a test of their architecture on their problem, and not a claim that their framework is deficient.

### 7.3 The identity that governs interpretation

```
    A_C1  and  A_C2  agree at SAFE (FULL = FULL)
                     agree at UNSAFE (empty = empty)
                     differ at CAUTION (FULL != {Go, Delay})

    therefore, for the evaluated C1/C2 mappings:

              Delta_L2  =  P(S = CAUTION)
```

Verified from the implementation in `condition_comparison.py`, not from documentation, and re-confirmed numerically on every run reported below (identity holds to < 1e-9).

**This is the interpretive key to the whole result.** The replay measures **how frequently the intermediate restriction is activated**. It does **not** measure whether `{Go, Delay}` is the correct restriction: any strict subset of FULL at CAUTION yields the same number.

### 7.4 The subtraction

```
    PRIMARY (43,848 hourly records, 9,135 departure-window hours)

    C0 <-> C1  =  42.88%   Level 1 alone (participation gate)
    C0 <-> C2  =  48.69%   Levels 1 + 2 combined
    -------------------------------------------------------
    difference =   5.81%   LEVEL 2 ALONE          <-- Delta_L2

    Cross-check, computed independently:
    C1 <-> C2  =   5.81%   (direct pairwise, same value)

    Structural check (entailed by the definitions, not measured):
    C1 <-> C3  =   0.00%   identical admissible sets by construction
```

---

## 8. Sensitivity

Governance mappings were held fixed throughout; only environmental classification thresholds varied. Source: `scripts/sensitivity/threshold_sensitivity.py`.

| Component | Finding |
|---|---|
| **Wind** | **Structural zero for the evaluated site and trace.** Δ_L2 unchanged to two decimal places across `W_C` 18–25 kn. Two departure-window observations lie within ±2 kn of 21.6; maximum 21.80 kn PRIMARY / 19.30 kn RESOLUTION |
| **Rainfall** | **Minimal.** `R_C` from 5.0 to 19.9 mm/hr moves Δ_L2 by 0.48 points PRIMARY / 0.78 RESOLUTION. **The non-MET lower rainfall boundary is not driving the headline result** |
| **Wave** | **Dominant.** The wave CAUTION onset `O_C` is the principal determinant, moving Δ_L2 by approximately **−1.4 percentage points per 0.05 m** over the evaluated range. Descriptive influence only — not causal |

**Robustness envelope, externally sourced thresholds, small vessel: 5.67% – 9.56%.** Reported as a deterministic sensitivity range, **not** a confidence interval, and never written as "5.81% ± x".

### 8.1 Component attribution

PRIMARY, departure window, 531 CAUTION hours:

| Component | Binding | Share |
|---|---|---|
| `g_o` | **518 / 531** | **97.6%** |
| `g_r` | 13 / 531 | 2.4% |
| `g_w` | 0 | activates twice in 43,848 hours, decisive in neither |
| `g_t` | 0 | emits no CAUTION by construction |
| `g_m` | 0 | structurally excluded, `D = {m}` |
| ties | 0 | — |

**Answering RQ3, as a negative result:** the five-component state remains defensible as a transferable specification, but the evaluated record does not empirically warrant equal importance of all five components at this deployment site.

**Scope note.** F-7's finding that three functions bind refers to max-severity binding **across all states**, where `g_t` dominates non-SAFE through darkness. The table above is **CAUTION-specific within the departure window**. Both are correct at their own scope and neither corrects the other.

---

## 9. Results

| Quantity | PRIMARY | RESOLUTION |
|---|---|---|
| **Δ_L2 — intermediate-state activation rate** *(empirical)* | **5.81%** | **4.48%** |
| Sourced-threshold envelope, small vessel | **5.67 – 9.56%** | 4.26 – 6.64% |
| C0 ↔ C1 (Level 1 alone) | 42.88% | *not reported* |
| C0 ↔ C2 (Levels 1 + 2) | 48.69% | *not reported* |
| C1 ↔ C3 *(structural — entailed by definitions)* | **0.00%** | **0.00%** |

The RESOLUTION pairwise components are withheld under `RESOLUTION_PAIRWISE_C0_C1_C0_C2 = PROVENANCE_INCOMPLETE` pending a provenance repair. Δ_L2 itself is unaffected.

**What 5.81% means.** For the operative small-vessel class, the intermediate advisory-scope state was reached in 5.81% of departure-window hours under the primary configuration and 4.48% under the alternative environmental-data configuration. Because the compared conditions differ only at CAUTION (§7.3), this figure is the **activation rate of the intermediate state**. These are exact descriptive values for the analysed traces and configurations. The result is **sensitive but still informative**: it is governed almost entirely by the best-sourced threshold in the set and is non-vacuous across every sourced small-vessel configuration, but it is a point on a steep gradient rather than a stable site property.

**What 0.00% is, and is not.** C1 ↔ C3 = 0.00% follows from the comparator definitions rather than from the data, and confirms that the implementation behaves consistently with those definitions. It is **not** independent empirical evidence. The claim it supports is structural:

> A three-state scheme whose intermediate state preserves the same advisory scope as the permissive state remains equivalent to the binary comparator at the admissible-set level.

Graduation comes from a change in the admissible recommendation set, not from an increase in the number of state labels.

### 9.1 PRIMARY versus RESOLUTION

The two configurations differ in **both** wave model and record length. A common-period comparison over the shared 28,501 hours separates them:

| Effect | Value |
|---|---|
| Wave-model / data-resolution effect, record period held constant | 6.45% − 4.48% = **+1.97 points** |
| Record-length effect, wave model held constant | 5.81% − 6.45% = **−0.64 points** |
| Combined = reported spread | 1.97 − 0.64 = **1.33 points** |

**The two effects operate in opposite directions.** The 1.33-point spread between the reported columns is therefore **not** the grid-resolution sensitivity; the like-for-like resolution effect is 1.97 points, partially offset by a record-length effect of −0.64. The direction of the earlier canonical claim — that the coarser model classifies more conservatively — is correct; its magnitude was not.

---

## 10. Contribution

**Primary — empirical characterisation.** An empirical characterisation, over five years of hourly environmental records for one deployment site and under two environmental-data configurations, of how often an intermediate advisory-scope state admits a strictly smaller recommendation set than a participation-only gate, together with its robustness envelope across defensible threshold configurations and an attribution of which state components produce it. This includes the negative findings: wind is a structural zero at this site, and three of five component classifiers never bind.

**Secondary — domain operationalisation.** A domain operationalisation for small-scale Malaysian coastal fisheries in which every threshold is traced to a named authority, the absence of an official lower criterion is documented rather than filled, and researcher-defined choices are separated from externally supported ones.

**Secondary — operational specification.** An operational specification in which AI participation and admissible advisory scope are expressed as two separately state-conditioned functions rather than a single graduated index.

**Supporting — formal contract-conformance analysis.** P1–P4 and the prototype fidelity criteria, establishing that the implementation satisfies its governance contract.

**Supporting — reproducibility and provenance methodology.** Predictions registered before the analysis that resolves them, refutations retained, a single authoritative figure generator, and a full supersession history.

---

## 11. Limitations and explicit non-claims

**1. Δ_L2 is invariant to the content of `A_AI(CAUTION)`.** Because the compared conditions differ only in that cell, the measured rate is unchanged for any strict subset of the full recommendation set. The evaluation therefore characterises how often the intermediate restriction is activated and provides **no evidence** that restricting advisory scope to `{Go, Delay}` is appropriate. That choice rests on a domain rationale drawn from the fisheries literature and is not empirically validated, shown optimal, or established as safer.

**2. The result depends strongly on the wave CAUTION onset.** A ±0.25 m perturbation moves it between 2.54% and 14.75%, and the source itself supports two readings of the small-vessel UNSAFE boundary — operational ceiling and failure point — giving 5.81% and 9.22%.

**3. Vessel-class specificity.** The result is specific to vessels under 10 GRT. Under the same source's thresholds for medium and large vessels the intermediate state is reached in **1.96%** and **1.26%** of departure-window hours respectively (0.66% and 0.37% under RESOLUTION), approaching vacuity for the larger classes. The headline must not be generalised across vessel classes.

**4. Time policy.** Classifying non-daylight hours as UNSAFE is a conservative architectural policy, not a physical or legal determination; COLREGs Rule 20(b) supplies the sunrise-to-sunset boundary for navigation lights, not a requirement that AI abstain. The canonical denominator includes those hours; a daylight-only denominator gives **9.59%** and **7.40%** respectively.

**5. Characterisation, not validation.** No incident record exists for the site — no accident reports, no capsizings, no near-misses. The result establishes that the architecture *would have* restricted advisory scope in those hours, not that they were the correct hours to restrict.

**6. All figures are lower bounds.** The marine-warning component `m` has no historical archive and is held at `none`; the replays run with declared exclusion `D = {m}`. Since `g_m` can only raise severity, every severity figure is a lower bound. The mechanism of this inference is standard partial-identification practice.

**7. Admissible-set level only.** The metric is computed from the classifier and governance layer alone. Layer 3 exists as a research prototype with fidelity criteria closed, but the replay does not compare the *content* of generated advice.

**8. Descriptive, not inferential.** A deterministic census of every hourly record in a predefined window, not a random sample. No p-values, confidence intervals or significance tests apply.

**9. Evidential provenance.** §3 is built from the project's coding and verification documents and from primary-source verification of the closest precedents. The readings of Flehmig, Shamsujjoha and Baxi are this project's.

### What this work does not establish

Accident reduction · improved safety outcomes · fisher decision quality · classification accuracy · optimal thresholds · optimal number of states · optimal `A_AI(CAUTION)` · generalisation across Sabah · generalisation across vessel classes · AI prediction accuracy · causal effectiveness · a novel fail-safe mechanism · a novel state-gating mechanism · a novel totality mechanism · a novel advisory-inhibition mechanism.

---

## 12. Provenance — why the figure moved

The headline has changed several times. Each move has a recorded cause that predates the recomputation.

| Figure | Configuration | Why superseded |
|---|---|---|
| 12.4% | Land-cell wind, ERA5 50 km waves, small-vessel UNSAFE at 1.9 m | F-10: Open-Meteo's `cell_selection` defaults to `land` |
| 8.3% | MFWAM 8 km, UNSAFE still at 1.9 m | 1.9 m was Yaakob's *failure point*, not his *operational ceiling* |
| 6.1% (as lone headline) | MFWAM 8 km, 1.25 m | Correct for its configuration, but a 3.25-year figure reported as five years |
| 7.84% / 6.15% | Sea-cell, `g_r` CAUTION at 7.5 mm/hr | 7.5 mm/hr matched no published source; re-anchored to the JPS/DID limit |
| 7.72% / 5.98% | Sea-cell, correct thresholds, fixed-clock `g_t` | SDR-001: the 06:00/17:00/19:00 clock had no located source |
| **5.81% / 4.48%** | **Current canonical** | — |

Two safeguards came out of this history. **Propagating a parameter is not the same as recomputing what depends on it** — any threshold, data-source or grid-cell change now requires re-running `canonical_figures.py` and replacing the figure table wholesale. And **predictions are registered before the analysis that resolves them**: `data/prediction-register.csv` holds P01–P24, of which P21–P24 were registered before this comparison ran, currently resolving 15 CONFIRMED / 9 REFUTED. P21 is the exception worth naming: it predicted C1 ↔ C3 = 0, which the comparator definitions entail, so it functions as a regression lock on the encoding rather than as a test of the site data.

---

## 13. Reproduction

```bash
cd <repo root>
python3 scripts/canonical_figures.py                      # figure table, both configurations
python3 scripts/condition_comparison.py                   # four-condition comparison, Delta_L2
python3 scripts/sensitivity/threshold_sensitivity.py      # sensitivity, attribution, common period
```

The first two were re-run on 2026-09-21 (Python 3, pandas 2.3.3, numpy 2.2.6) and reproduced 5.81% / 4.48% / 0.00% / 42.88% / 48.69% exactly. The §12 provenance figures and the prediction-register counts are not produced by these scripts. Neither writes to the register by default; register writes require `--write-register`.

Inputs: `data/raw_weather_sea.csv`, `data/raw_marine_era5_sea.csv`, `data/raw_marine_mfwam.csv`, and the frozen solar artefact `data/solar/solar-events-daily.csv`. `g_t` is imported from `scripts/canonical_gt.py`; no script computes solar astronomy.

**Sources**

- `docs/analysis/final-research-chain-lock.md` — authoritative framing, wording and non-claims
- `docs/analysis/threshold-sensitivity-analysis.md` — sensitivity, attribution, common-period comparison
- `docs/canonical/empirical-findings-2026-09-06.md` §0a — authoritative figure table
- `publications/active/journal-1/evaluation-specification.md` — conditions, metrics, statistical treatment
- `docs/canonical/appendix-c-formalisation.md` — formal definitions and governance properties
- `data/prediction-register.csv` — prediction state authority
