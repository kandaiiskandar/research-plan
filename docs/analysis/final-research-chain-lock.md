# Final Research Chain Lock

**Date:** 2026-09-21
**Status:** Authoritative specification. Subsequent canonical revisions must follow this document.
**Canonical report and evaluation specification: UNCHANGED.**
No new literature search, experiment, or computation performed; arithmetic re-verified only.

---

## A. Frozen literature position

Established prior work. The thesis concedes all of the following and claims novelty for none:

state-conditioned advisory restriction · advisory-category inhibition · **human-facing advisory inhibition based on observation validity** (TSO-C151c §5.6: invalid position ⇒ FLTA and PDA inhibited, GPWS retained, inhibit annunciated to crew) · nested admissible sets contracting to empty · deterministic gating outside the generator · multi-level graduated governance · multi-component runtime state (TCAS II: radio altitude, flap/slat/gear discretes, weight–altitude–temperature, airspeed margin, bank angle, OEI) · weakest-link / max-severity aggregation · human final authority (AC 20-151C §2.1.1) · fail-safe / fail-degraded / fail-operational behaviour · totality over incomplete observations (Bauer et al. 2011; Taleb et al. 2023) · conservative handling of unusable observations · directional bounds from unmeasured variables (Manski 1990, 1997; Manski & Pepper 2000).

No report wording may imply generic novelty for any of these.

---

## B. Frozen research problems

**Domain.** Small-scale fishers at Kota Kinabalu make departure decisions under conditions they cannot instrument, with no marine-warning archive, no incident register, and official criteria that define where warnings begin but never where caution should begin.

**CS / design.** The governance mechanisms above exist across certified avionics, autonomous-agent frameworks and runtime verification, each with its own conditioning variable and governed object. Composing them for an unattended multi-source environmental classifier requires decisions none of the source domains supplies.

**Evidence.** Whether an intermediate advisory-scope level is reached often enough to matter has not been measured on a multi-year record.

---

## C. Frozen Gap A — operationalisation

> Advisory-type restriction conditioned on an externally measured state is established practice in certified collision-avoidance and terrain-awareness avionics; totality of classification over incomplete observations is established in runtime verification; and directional bounds from declared unmeasured variables are standard in partial-identification methodology. Within the reviewed literature, these were not found composed into a single operational specification in which participation `G(S)` and admissible advisory scope `A_AI(S)` are separately specified over a classified multi-component environmental state, for a human-facing decision-support system in a low-resource setting where some conceptually required components are structurally unavailable.

**Modest.** The three ingredients come from unrelated fields; their non-combination is largely disciplinary. Not to be described as an architecture gap.

## D. Frozen Gap B — empirical characterisation

> Within the reviewed literature, no empirical characterisation was identified of how often an intermediate advisory-scope state changes the admissible recommendation set relative to a participation-only gate, when replayed over a multi-year environmental record.

**The stronger gap. Supports the primary contribution.**

---

## E. Frozen RQ1–RQ3

> **RQ1 — Operational specification.** Can AI participation and admissible advisory scope be specified as two separate state-conditioned functions over a classified multi-component environmental state such that classification remains total and the containment property is preserved when some conceptually required components are structurally unavailable — and which elements of that specification must be decided by the designer rather than derived from published sources?

> **RQ2 — Empirical characterisation and robustness.** Over a multi-year historical environmental record for the deployment site, how frequently does the intermediate safety state produce a stricter admissible recommendation set than a participation-only gate, and how sensitive is that frequency to defensible environmental-threshold and data configurations?

> **RQ3 — Structural warrant of the multi-component classifier.** Which components of the environmental state actually determine the intermediate classification at the deployment site, and is the multi-component structure warranted by the evaluated record?

**Not reintroduced:** prototype implementation as an RQ; contextual fisher validation as a completed RQ; target-hardware latency as an RQ; Safety Dominance as an independent thesis-level RQ.

**RQ-J2 decision, permanent:** *Target-hardware benchmarking is deferred deployment/prototype evaluation and is not required evidence for the current research contribution.* `E5_ANDROID_TARGET_BENCHMARK = DEFERRED_MANDATORY` must be re-designated. Its absence is **not** a thesis-evaluation limitation.

---

## F. Frozen architecture framing

**An operational architecture and specification that composes established safety-governance mechanisms for a low-resource environmental decision-support setting.** Not a wholly novel safety architecture.

| | Content |
|---|---|
| **Inherited** | Advisory-type restriction by external state; nested contracting admissible sets; deterministic gating outside the generator; max-severity aggregation; fail-safe resolution; human final authority |
| **Domain adaptations** | Avionics inhibition pattern moved from one certified platform with a validity-checked navigation input to an unattended multi-source environmental classifier; RV totality moved from trace monitoring to component-wise environmental classification; vessel-conditional ocean thresholds |
| **Researcher-defined** | `A_AI(CAUTION) = {Go, Delay}`; three-state cardinality; policy `night ⇒ UNSAFE`; departure window 05:00–09:00; exclusion `D = {m}`; dual-configuration reporting |
| **Empirically evaluated** | Intermediate-state activation frequency; its threshold and data-configuration sensitivity; component attribution |

---

## G. Frozen governance contract

| State | `G(S)` | `A_AI(S)` |
|---|---|---|
| SAFE | 1 | {Go, Delay, DepartureTime, Duration} |
| CAUTION | 1 | **{Go, Delay}** |
| UNSAFE | 0 | ∅ |

> **`A_AI(CAUTION) = {Go, Delay}` is a researcher-defined design choice.** It is **not** externally validated, **not** empirically validated, **not** shown optimal, and **not** established as safer.

**Correction to an earlier characterisation in this analysis series.** This choice is not wholly unsupported: `architecture-illustration.md` §203 gives a domain rationale citing Gao (2024) and Rahim et al. (2024) — under marginal conditions fishers continue to make go/no-go and near-shore decisions but do not attempt to optimise departure timing or trip duration. That is a **domain-derived rationale from cited sources**, which is weaker than validation and stronger than designer fiat. Earlier documents in this series described it as having no source; that was too strong and is corrected here. The rationale does not establish optimality, and the experiment cannot test it (§H).

---

## H. Δ_L2 identity

$$\boxed{\;\Delta_{L2} = P(S = \text{CAUTION})\;}$$

for the evaluated C1/C2 mappings. Verified from `condition_comparison.py`, not from documentation: the tables agree at SAFE (FULL = FULL) and UNSAFE (∅ = ∅) and differ only at CAUTION. Re-confirmed numerically on every sensitivity run, identity holding to < 1e-9.

**Consequence, which must appear wherever the figure appears:** the experiment measures **how frequently the intermediate restriction is activated**. It does **not** determine whether the content of the restriction is appropriate. Any strict subset of FULL at CAUTION yields the same number.

---

## I. Frozen empirical results

| | PRIMARY | RESOLUTION |
|---|---|---|
| Records | 43,848 | 28,501 |
| Departure-window denominator | 9,135 | 5,935 |
| **Δ_L2 (canonical)** | **5.81%** | **4.48%** |
| P(SAFE) / P(CAUTION) / P(UNSAFE) | 51.31 / 5.81 / 42.88 | 54.44 / 4.48 / 41.08 |
| **Sourced-threshold envelope, small vessel** | **5.67% – 9.56%** | 4.26% – 6.64% |

**Classification: sensitive but still informative.** 5.81% must not be presented as a universal or stable site property, and must not appear without the envelope.

---

## J. Threshold sensitivity — frozen

| Component | Finding |
|---|---|
| **Wind** | **Structural zero.** Δ_L2 unchanged to 2 d.p. across `W_C` 18–25 kn. Two departure-window observations within ±2 kn of 21.6; max 21.80 kn (PRIMARY) / 19.30 kn (RESOLUTION); binds in zero CAUTION hours |
| **Rainfall** | **Minimal.** `R_C` 5.0 → 19.9 mm/hr moves Δ_L2 by 0.48 points (PRIMARY) / 0.78 (RESOLUTION). **The non-MET lower boundary is not driving the result** |
| **Wave** | **Dominant.** `O_C` is the principal determinant. Approximate descriptive influence **−1.4 percentage points per 0.05 m** over 0.80–1.25 m. `O_U` contributes ≈ +0.2 pp per 0.05 m below 1.6 m, saturating above ~1.9 m |

Descriptive influence only. **Not causal.** Ranges are deterministic sensitivity, **never** written as "5.81% ± x".

---

## K. Component attribution — frozen

PRIMARY, departure window, 531 CAUTION hours (5.81% × 9,135 = 530.7 ≈ 531; 518 + 13 = 531 ✓):

| Component | Binding | Share |
|---|---|---|
| `g_o` | **518 / 531** | **97.6%** |
| `g_r` | 13 / 531 | 2.4% |
| `g_w` | 0 | 0% (activates twice in 43,848 hours, decisive in neither) |
| `g_t` | 0 | 0% (emits no CAUTION by construction) |
| `g_m` | 0 | structurally excluded, `D = {m}` |
| ties | 0 | — |

RESOLUTION: 266 CAUTION hours; `g_o` 253, `g_r` 13 ✓.

> **Frozen interpretation.** The five-component state remains defensible as a transferable specification, but the evaluated record does not empirically warrant equal importance of all five components at this deployment site.

**This is a negative empirical result and must not be hidden.** Note the scope distinction: F-7's statement that "three functions ever bind" refers to max-severity binding across all states, where `g_t` dominates non-SAFE via darkness; the table above is CAUTION-specific within the departure window. Both are correct at their own scope and must not be conflated.

---

## L. PRIMARY vs RESOLUTION decomposition — frozen

**Do not repeat:** "the 1.33-point difference is the grid-resolution effect."

| Quantity | Value |
|---|---|
| Wave-model / data-resolution effect, record period held constant | 6.45% − 4.48% = **+1.97 points** |
| Record-length effect, wave model held constant | 5.81% − 6.45% = **−0.64 points** |
| Combined = reported spread | 1.97 − 0.64 = **1.33 points** ✓ |

The two effects act in opposite directions. The direction of the canonical claim (the coarse model classifies more conservatively) is correct; the magnitude is not. Source: common-period comparison over the shared 28,501 hours, `scripts/sensitivity/threshold_sensitivity.py`.

---

## M. Vessel-class and time-policy limits — frozen

**Vessel class.** Using the same source's thresholds for other vessel classes: medium (1.4 / 2.8 m) gives 1.96% PRIMARY / 0.66% RESOLUTION; big (1.5 / 3.5 m) gives 1.26% / 0.37%. **The intermediate state approaches vacuity for larger vessels.** The headline is **population-specific to the operative small-vessel class (< 10 GRT)** and must not be generalised across vessel classes.

**Time policy.** `night ⇒ UNSAFE` is researcher-defined; COLREGs Rule 20(b) supplies the sunrise/sunset boundary for navigation lights, not an abstention requirement. The canonical denominator includes non-daylight departure-window hours classified UNSAFE. A daylight-only denominator gives **9.59% / 7.40%** — roughly two-thirds higher. The headline is conditional on the canonical time policy and denominator. Night operation must not be described as physically or legally unsafe.

---

## N. Formal claim status — frozen

| Claim | Status |
|---|---|
| **Totality** (P1; Thm 6.1, C.1, C.1b) | Formalisation of an established mechanism |
| **Containment / monotonicity** (P2; Thm 6.2) | Design property — true by definition of `A_AI` |
| **Safety Dominance** (P3; Thm 6.3, C.3, C.7.2) | Implementation / contract-conformance property under A1–A4 |
| **C1 ≡ C3** (P4 / J1-P1) | Supporting structural proof; the 0.00% replay value is harness consistency, not discovery |

**None is presented as novel theory.** All are retained because they establish that the implementation satisfies the governance contract.

---

## O. Contribution hierarchy — frozen

**Primary — empirical characterisation** of intermediate advisory-scope activation over multi-year environmental replay: canonical activation rates, robustness envelope, threshold sensitivity, component attribution, common-period data-configuration comparison, and the negative findings.

**Secondary — domain operationalisation** for small-scale Malaysian coastal fisheries.

**Secondary — operational specification** separating `G(S)` from `A_AI(S)`.

**Supporting — formal contract-conformance analysis.**

**Supporting — reproducibility and provenance methodology.**

Architecture composition must not be promoted above empirical characterisation.

---

## P. Explicit non-claims

The thesis does **not** establish: accident reduction · improved safety outcomes · fisher decision quality · classification accuracy · optimal thresholds · optimal number of states · optimal `A_AI(CAUTION)` · generalisation across Sabah · generalisation across vessel classes · AI prediction accuracy · causal effectiveness · a novel fail-safe mechanism · a novel state-gating mechanism · a novel totality mechanism · a novel advisory-inhibition mechanism.

---

## Q. RQ → evidence → contribution map

| RQ | Evidence | Result | Contribution | Limitation |
|---|---|---|---|---|
| **RQ1** | `appendix-c-formalisation.md`; P1–P3; `D = {m}` with lower-bound consequence; threshold provenance table | Totality and containment hold jointly under structural unavailability. Four boundaries sourced (MET Cat 1/2, MET *Ribut Petir*, JPS/DID *Light*, Yaakob ceiling, COLREGs 20(b)); three load-bearing choices researcher-defined | Operational specification (secondary) | Answered by construction and proof, not measurement |
| **RQ2** | Replay + `scripts/sensitivity/threshold_sensitivity.py` | Δ_L2 = 5.81% / 4.48%; envelope 5.67–9.56%; `O_C` dominant; wind structural zero; rainfall < 0.5 pp | **Empirical characterisation (primary)** | Single site; invariant to `A_AI(CAUTION)` content; no incident data |
| **RQ3** | Component attribution over the same replay | `g_o` 97.6%, `g_r` 2.4%, three components never bind | Empirical characterisation (primary, negative) | Site-specific; does not refute transferability |

No RQ lacks evidence. No completed experiment lacks an RQ.

---

## R. Headline number audit

| Number | Source | Meaning | Denominator | Allowed | Prohibited |
|---|---|---|---|---|---|
| 43,848 | `canonical_figures.py` | PRIMARY hourly records 2020-01→2024-12 | — | Record size | Not "observations of fishing activity" |
| 28,501 | same | RESOLUTION hourly records 2021-10→2024-12 | — | Record size; also the common-period overlap | — |
| 9,135 | `condition_comparison.py` | PRIMARY departure-window hours, 05:00–09:00 | — | Denominator for all PRIMARY rates | Not all daylight hours |
| 5,935 | same | RESOLUTION departure-window hours | — | Denominator for RESOLUTION rates | — |
| **5.81%** | same | Δ_L2 = P(CAUTION), small vessel | 9,135 | Activation rate of the intermediate state | Not effectiveness, safety, accuracy, or threshold-independent |
| **4.48%** | same | as above, RESOLUTION | 5,935 | as above | as above |
| 5.67–9.56% | `threshold_sensitivity.py` | Envelope over sourced small-vessel thresholds | 9,135 | Deterministic sensitivity range | **Never** a confidence interval; never "±" |
| 6.45% | same, common-period | PRIMARY wave model over shared 28,501 h | 5,935 | Like-for-like comparator | Not the canonical PRIMARY figure |
| +1.97 pts | derived | Wave-model effect, period held constant | — | Grid-resolution sensitivity | Not the reported spread |
| −0.64 pts | derived | Record-length effect, model held constant | — | Period effect | Not a data error |
| 518 / 531 | same | `g_o` binding CAUTION hours, PRIMARY | 531 | Component attribution | Not a recommendation share |
| 97.6% | derived | 518 / 531 | 531 | as above | Not `g_o`'s share of all hours |
| 13 / 531 | same | `g_r` binding CAUTION hours | 531 | as above | — |
| 2.4% | derived | 13 / 531 | 531 | as above | — |

All arithmetic re-verified: 0.0581 × 9,135 = 530.7 ≈ 531 = 518 + 13 ✓; 0.0448 × 5,935 = 265.9 ≈ 266 = 253 + 13 ✓; 1.97 − 0.64 = 1.33 ✓.

---

## S. Documentation corrections required

| File | Section | Change |
|---|---|---|
| `CLAUDE.md` | line 13 | *"a **novel** intermediate CAUTION mode … **which no existing architecture implements**"* — **contradicts the frozen position.** Replace |
| `CLAUDE.md` | line 59 (gap layer 1) | *"no existing architecture restricts AI advisory scope…"* — replace with Gap A wording |
| `CLAUDE.md` | line 49, 51, 86, 107 | RQ5 listed as an active RQ — re-designate as future socio-technical validation |
| `docs/canonical/discussion-notes-governance-gap…` | line 218 | *"no existing architecture formally restricts AI advisory scope…"* — replace |
| `docs/chapters/chapter-2-literature-review/v1-initial-draft.md` | §67 | *"no existing architecture defines intermediate operating modes"*; *"This asymmetry is absent from every safety architecture reviewed"* — both contradict TSO-C151c. Rewrite with the concession first |
| `docs/canonical/empirical-findings-2026-09-06.md` | §0a line 45 | *"The 1.3-point gap … IS the grid-resolution sensitivity"* — replace with the §L decomposition |
| `docs/canonical/session-log-2026-09-06.md` | line 209 | *"The 1.7-point spread is the grid-resolution sensitivity"* — historical; annotate rather than rewrite |
| `publications/active/journal-1/evaluation-specification.md` | §5, §11, §13, §17 | Remove RQ-J2 from active RQs; re-designate `E5_ANDROID_TARGET_BENCHMARK`; merge RQ-J4 into RQ-J3 |
| `publications/active/journal-1/…v1…/manuscript.md` | line 1136 | *"the gap between them is the grid-resolution sensitivity"* — submitted version; **do not edit**, supersede in the next revision |
| **`experiment-report-delta-l2.md`** | throughout | Revised Gap A/B, RQ1–RQ3, contribution hierarchy, Δ_L2 identity, robustness envelope, component attribution, wave-threshold dependence, vessel-class limit, time-policy limit, `A_AI(CAUTION)` invariance limit, corrected PRIMARY/RESOLUTION interpretation |
| `docs/analysis/open-issues-log.md` | ISSUE-1 | Mark **RESOLVED** — common-period comparison performed |

**Already correct, retain and propagate:** `report-journal1-canonical-consistency-sync-2026-09-09.md` §197 and `evaluation-baseline-decision.md` §159 already state that `A_AI(CAUTION) = {Go, Delay}` is not epistemically warranted or optimal, and that no safety-outcome claim is supported. This language should be reused rather than rewritten.

---

## T. Canonical wording bank

**1. Research problem.** Small-scale fishers at Kota Kinabalu decide whether to put to sea under conditions they cannot instrument, in a setting with no marine-warning archive, no incident register, and official weather criteria that state where warnings are issued but never where caution should begin.

**2. Gap A.** *(as §C verbatim)*

**3. Gap B.** *(as §D verbatim)*

**4–6. RQ1–RQ3.** *(as §E verbatim)*

**7. Architecture.** An operational architecture and specification that composes established safety-governance mechanisms — advisory-type restriction by externally measured state, totality of classification over incomplete observations, and conservative resolution of unusable inputs — for a human-facing decision-support setting in low-resource coastal fisheries.

**8. Primary contribution.** An empirical characterisation, over five years of hourly environmental records for one deployment site and under two environmental-data configurations, of how often an intermediate advisory-scope state admits a strictly smaller recommendation set than a participation-only gate, together with its robustness envelope across defensible threshold configurations and an attribution of which state components produce it.

**9. Secondary contributions.** A domain operationalisation for small-scale Malaysian coastal fisheries in which every threshold is traced to a named authority, the absence of an official lower criterion is documented rather than filled, and researcher-defined choices are separated from externally supported ones; and an operational specification in which AI participation and admissible advisory scope are expressed as two separately state-conditioned functions rather than a single graduated index.

**10. Interpretation of 5.81%.** For the operative small-vessel class, the intermediate advisory-scope state was reached in 5.81% of departure-window hours under the primary configuration and 4.48% under the alternative environmental-data configuration. Because the compared conditions differ only at CAUTION, this figure is the activation rate of the intermediate state. These are exact descriptive values for the analysed traces and configurations.

**11. Threshold sensitivity.** Across externally sourced threshold values for this vessel class the rate ranges from 5.67% to 9.56%. It is governed almost entirely by the wave CAUTION onset, which moves it by approximately 1.4 percentage points per 0.05 m; the rainfall CAUTION boundary moves it by less than half a point across a fourfold variation, and the wind boundaries by nothing measurable. Reported as a deterministic sensitivity range, not a confidence interval.

**12. Component attribution.** Of five component classifiers, the ocean-state function is the binding component in 97.6% of intermediate-state hours and the rainfall function in 2.4%; the wind, time and marine-warning functions bind in none. The five-component state remains defensible as a transferable specification, but the evaluated record does not empirically warrant equal importance of all five components at this site.

**13. `A_AI(CAUTION)` limitation.** Because the compared conditions differ only in the CAUTION cell, the measured rate is invariant to the content of `A_AI(CAUTION)` provided it remains a strict subset of the full recommendation set. The evaluation therefore characterises how often the intermediate restriction is activated and provides no evidence that restricting advisory scope to {Go, Delay} is appropriate. That choice rests on a domain rationale drawn from the fisheries literature and is not empirically validated, shown optimal, or established as safer.

**14. Vessel-class limitation.** The result is specific to vessels under 10 GRT. Under the same source's thresholds for medium and large vessels the intermediate state is reached in 1.96% and 1.26% of departure-window hours respectively, approaching vacuity for the larger classes.

**15. Time-policy limitation.** The classification of non-daylight hours as UNSAFE is a conservative architectural policy, not a physical or legal determination; COLREGs Rule 20(b) supplies the sunrise-to-sunset boundary for navigation lights, not a requirement that AI abstain. The canonical denominator includes those hours; a daylight-only denominator gives 9.59% and 7.40% respectively.

**16. Formal properties.** The proved properties — classifier totality over the observation space, admissible-set containment, and safety dominance — establish that the implementation satisfies its intended governance contract. Totality over incomplete observations and conservative resolution of unusable inputs are established in prior work; these results are not offered as new theory.

**17. Overall contribution statement.** *(as `research-chain-lock.md` §Q, amended by item 13 above)*

---

## U. Contradiction audit — findings in existing canonical documents

| # | Contradiction | Location | Severity |
|---|---|---|---|
| 1 | Architecture novelty asserted after mechanism novelty conceded — *"novel intermediate CAUTION mode … which no existing architecture implements"* | `CLAUDE.md` :13 | **Blocking for revision** |
| 2 | *"no existing architecture restricts AI advisory scope based on classified environmental safety state"* | `CLAUDE.md` :59 | **Blocking for revision** |
| 3 | Same claim | `discussion-notes-governance-gap…` :218 | **Blocking for revision** |
| 4 | *"no existing architecture defines intermediate operating modes"*; *"absent from every safety architecture reviewed"* | Chapter 2 v1 draft :67 | **Blocking for revision** |
| 5 | 1.33 points described as pure grid-resolution sensitivity | `empirical-findings-2026-09-06.md` §0a :45 | **Blocking for revision** |
| 6 | 1.7-point spread described as grid-resolution sensitivity | `session-log-2026-09-06.md` :209 | Historical — annotate only |
| 7 | Same claim in submitted manuscript | journal-1 v1 manuscript :1136 | Archived — supersede, do not edit |
| 8 | RQ-J2 / `DEFERRED_MANDATORY` present in 6 files | eval-spec, research-design, algorithm-spec, baseline-decision, CHANGELOG, v1 manuscript | Revision required |
| 9 | RQ5 listed as an active RQ without fisher evidence | `CLAUDE.md` :49, 51, 86, 107 | Revision required |
| 10 | Five-component necessity — *"The classifier is NOT reduced"* | `CLAUDE.md` :214 | **Not a contradiction.** It is a design decision, correctly scoped; pair it with §K's negative result rather than removing it |

**Not found (clean):** no document calls 5.81% advisory effectiveness; no document calls `{Go, Delay}` validated — two already state the opposite; no document claims incident or safety validation; no document describes the formal properties as new theory.

---

## V. Final lock decision

> # **RESEARCH CHAIN LOCKED — READY FOR CANONICAL REVISION**

The chain is internally consistent and every link carries evidence. Both gaps are stated conservatively with the established mechanisms conceded first. Three research questions each have evidence in hand, each could have returned a different answer, and none asks a question the experiment cannot address. The primary contribution — empirical characterisation with a robustness envelope and a negative attribution result — rests on figures reproduced from authoritative scripts and re-verified arithmetically in this document. The formal properties are retained and correctly labelled as contract conformance. The exclusion list in §P is explicit, and the two limitations that most threaten the headline (invariance to `A_AI(CAUTION)` content, and dominance of the wave threshold) are frozen into the wording bank rather than left to a reader to discover.

Nine contradictions exist in the canonical tree, and all nine are wording that predates the audit sequence rather than evidential problems. Four assert architecture novelty that the primary-source verification retired; three attribute the PRIMARY/RESOLUTION spread wholly to grid resolution, which the common-period comparison has now decomposed; one carries a removed research question; one carries an RQ the thesis does not answer. None requires new research to fix, and §S names the file and line for each. They are blocking for the *revision*, not for the *lock*: the lock is what tells the revision what to write.

Two corrections in this document are to earlier analyses in this series rather than to the canonical tree, and both matter. `A_AI(CAUTION) = {Go, Delay}` has a domain rationale from cited fisheries literature — Gao (2024) and Rahim et al. (2024), that fishers under marginal conditions continue to make go/no-go and near-shore decisions without optimising timing or duration — which earlier documents described as having no source; that was too strong, and the frozen wording in §T.13 now says rationale rather than fiat while still denying validation and optimality. And F-7's statement that three functions bind is correctly scoped to max-severity binding across all states, not to CAUTION within the departure window; both readings are true at their own scope and §K now says so, so the revision must not present them as a correction of one another.
