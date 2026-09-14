# Contribution Freeze V2 — AMICT Conference Rebuild (Post-Novelty Repositioning)

**Date:** 2026-09-14
**Task:** `docs/tasks/AMICT CONTRIBUTION FREEZE V2 — POST-NOVELTY REPOSITIONING.md`
**Prerequisite gates:** `NOVELTY_AUDIT = STOP_MATERIAL_EQUIVALENCE_FOUND` · `SOURCE_CORPUS_VALIDATION = CLOSED`
**Companion artefact:** [`contribution-claim-matrix.csv`](contribution-claim-matrix.csv)
**Binding on:** RQ redesign · conference outline · manuscript drafting · claim-evidence audit

---

## 1. Executive verdict

    CONTRIBUTION_FREEZE_V2 = CLOSED
    HEADLINE_CONTRIBUTIONS  = 2

Two contributions are frozen. C1 survives, but only in a form materially narrower than the candidate wording: it leads on the **operational governance formalisation** rather than on the formal properties, because prior work already establishes closely related properties in other governance systems. C2 survives substantially intact and is the **stronger** of the two.

`domain-independent` is **rejected as an engineering claim**. Implementation fidelity is confirmed as supporting evidence for C1 only. The old review-based contribution is withdrawn. The structured-review sample stays at 72.

No stop condition fired.

---

## 2. Frozen novelty boundary

    MECHANISM_NOVELTY = WITHDRAWN

The mechanism pattern — externally measured runtime state → banded classification → progressively restricted advisory-type set → human operator — is established practice in certified collision-avoidance avionics (FAA AC 20-151C). Formal verification of state-conditioned advisory logic has precedent (Cleaveland, Mitsch & Platzer, 2023). Graduated governance with properties proved by construction has precedent (Baxi 2026; Kang 2026). Graduated narrowing of presented options has precedent (Parasuraman, Sheridan & Wickens, 2000). Environmental triggering of runtime governance change has precedent (Bernabei & Costantino, 2024). State-conditioned admissible-set restriction has precedent (shielding / action masking).

**None of this is claimed as new.** `graduated advisory-scope governance` is retained as a **descriptive term only**, and its first manuscript-facing use must acknowledge the avionics precedent.

---

## 3. C1 — phrase-by-phrase audit

`PROPERTY_EXISTS_IN_OUR_FORMALISM` and `PROPERTY_IS_NOVEL` are assessed separately throughout. A `PASS` on the first never implies the second.

| # | Phrase | Verdict | Required qualifier / note |
|---|---|---|---|
| P01 | **formalisation** | **PASS** | The formal specification exists and is canonical (Appendix C; algorithm specification). Claimed as *our* formalisation, never as the first formalisation of advisory constraints |
| P02 | **generalisation** | **PASS_WITH_SCOPE** | Only in the senses established in §4. Must appear as "generalises the conditioning state beyond a single hazard variable", never unqualified |
| P03 | **domain-independent** | **FAIL** as an engineering claim | No cross-domain implementation or evaluation exists. Prohibited in contribution wording |
| P04 | **domain-agnostic** | **WEAK** | Admissible only in the strict form "domain-agnostic at the governance-contract level". Not preferred; P05 is clearer |
| P05 | **domain-reinstantiable** | **PASS_WITH_SCOPE** | Must carry: "re-instantiation is specified and illustrated, not empirically demonstrated across domains" |
| P06 | **general governance abstraction** | **PASS_WITH_SCOPE** | Permitted where "general" means *defined independently of the advisory generator and of any one hazard variable*. Must not imply demonstrated cross-domain applicability |
| P07 | **separates participation from advisory scope** | **PASS** | `G(S)` and `A_AI(S)` are distinct mappings with distinct constraints (`G(S)=0 ⇒ A_AI(S)=∅`; `S=CAUTION ⇒ A_AI(CAUTION) ⊊ A_AI(SAFE)`). The separation is not claimed as novel — TCAS gates participation at its lowest bands too |
| P08 | **multi-component environmental state** | **PASS** | `E` over `C = {w, r, m, o, t}` with configuration parameter `v`, aggregated by max severity over five component classifiers. This is the clearest verifiable contrast with the single-scalar precedent |
| P09 | **totality** | **PASS_WITH_SCOPE** | `PROPERTY_EXISTS = YES`; `PROPERTY_IS_NOVEL = NO` — Kang (2026) establishes a deterministic **total** classifier by construction. Role: characterises and verifies the formalisation |
| P10 | **monotonicity** | **PASS_WITH_SCOPE** | `PROPERTY_EXISTS = YES`; `PROPERTY_IS_NOVEL = NO` — Baxi (2026) monotone nested permission sets; Kang (2026) monotonicity by construction; monotone "tighten-only" admissibility in 2026 runtime-governance preprints |
| P11 | **Safety Dominance** | **PASS_WITH_SCOPE** | Evaluated independently as instructed. The *property* `AI(E) ⊆ A_AI(f(E))` is a containment statement with analogues in prior work (Baxi's bounded exposure). What is **not** paralleled in the validated set is its **enforcement route**: by construction from a rule set `RS(S)` supplied *before* reasoning, with **no post-generation output filter**. Claim the enforcement route, not the property |
| P12 | **containment** | **PASS_WITH_SCOPE** | `A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅`. `PROPERTY_IS_NOVEL = NO` — nested admissible sets are established in shielding and in Baxi (2026) |

### 3.1 The operational-form semantics — C1's lead

Per the execution decision, C1 foregrounds the operational governance formalisation. Each element below was verified against `publications/active/journal-1/algorithm-specification.md` §§4, 6, 8, 9 and `docs/canonical/appendix-c-formalisation.md`.

| # | Construct | Status | Evidence |
|---|---|---|---|
| O01 | `Obsᵢ = (Xᵢ × 𝕋) ∪ {⊥}` — observation space with timestamp | **PASS** | Appendix C C.2.0.1 |
| O02 | `ρ_{D,τ} : ∏Obsᵢ → Y` — resolution map | **PASS** | Appendix C C.2.0.1; algorithm spec §4 |
| O03 | `F_{D,τ} = f ∘ ρ_{D,τ}` — operational classifier distinguished from ideal `f(E)` | **PASS** | Appendix C C.2.0.1; the ideal/operational distinction is stated and enforced in notation |
| O04 | Four distinguished ⊥ conditions with four responses — invalid, absent, stale → ⊥ → UNSAFE; unmeasured → declared exclusion | **PASS** | Algorithm spec §4 table; Appendix C C.2.0 |
| O05 | Missing required observation → ⊥ → UNSAFE | **PASS** | Corollary C.1b.1 |
| O06 | Stale required observation → ⊥ → UNSAFE | **PASS_WITH_SCOPE** | Mechanism specified; **`ageᵢ` is left symbolic with no proposed value**. Must be reported as a specified-but-unparameterised element |
| O07 | Invalid required observation → ⊥ → UNSAFE | **PASS** | Appendix C C.2.0.3 |
| O08 | Declared exclusion pinned at SAFE | **PASS** | Appendix C C.2.0.5; least element of ≻; the pin cannot raise the classification |
| O09 | Exclusion-before-fault evaluation order | **PASS** | Algorithm spec §4 step 1 before step 2, stated as load-bearing. Asserted literally to the replay, treating `m ∉ archive` as ⊥ would classify all 43,848 hours UNSAFE |
| O10 | `D` fixed and declared rather than dynamically expanding; `t ∉ D`, `D ⊊ C` | **PASS** | Appendix C C.2.0.5 (D1)–(D3) |
| O11 | Lower-bound interpretation under `D ≠ ∅` | **PASS** | (D3). The replay declares `D = {m}`, so every severity figure is a lower bound |
| O12 | Operational totality — totality extended from ideal domains to the observation space | **PASS** | Theorem C.1b |
| O13 | Fail-open / fail-safe asymmetry | **PASS** | κ defaults to 0 when the provider code is absent — non-escalating, therefore fail-**open** for that disjunct and explicitly *not* a fail-safe guarantee, with the consequence that `g_r` figures are lower bounds. The opposite rule applies to a required coordinate. Stated rather than inferred |
| O14 | ⊥ attaches to what a classifier reads, not to the declared variable | **PASS** | `g_o` reads wave height only, so an absent swell period is not a fault; `g_r` reads (rate, κ), so an absent rate is a fault and an absent raw code is not |
| O15 | Generator-independent admissibility: `RS(S)` supplied pre-reasoning, **no post-generation output filter** | **PASS** | Algorithm spec §8 postcondition (ii): "correctness is a property of the active rule set, not of a runtime check". This is a mechanism-level distinction from shielding and action masking, which filter candidate outputs at runtime |

**Limitations that travel with this block and must not be dropped:** `ageᵢ` is unspecified (O06); `reasons` runtime capture is unimplemented (OPEN-B1-2), and reasons never alter resolution, `G(S)`, `A_AI(S)`, `RS(S)` or human authority; and `RS(SAFE)` is empty in the evaluated configuration because `R-SAFE-001 = DEFERRED`, so the SAFE arm of the pre-reasoning contract is specified but never exercised.

### 3.2 Scoped literature statement

The only permitted comparative statement for the operational block is **LITERATURE-scoped**:

> Within the validated comparison set, no prior work identified combines these operational semantics with advisory-type scope governed by a classified multi-component environmental state.

Not an absolute claim. Not "unprecedented". Not "no existing work".

---

## 4. Generalisation audit

    DOMAIN_INDEPENDENT                        = FAIL_AS_ENGINEERING_CLAIM
    DOMAIN_REINSTANTIABLE                     = PASS_WITH_SCOPE
    GENERALIZED_BEYOND_SINGLE_HAZARD_VARIABLE = PASS

| Dim | Claim | Supported | Basis |
|---|---|---|---|
| A | Single scalar operational variable → `E = (w, r, m, o, v, t)` | **YES** | Five component classifiers aggregated by max severity, with `v` as a configuration parameter. Directly and verifiably contrasts with the single-scalar-plus-configuration-discretes precedent |
| B | Device-specific inhibition table → `S = f(E)`, `(G(S), A_AI(S))` | **YES** | Both defined as general objects in Appendix C, not as a lookup table |
| C | Particular advisory generator → generator-independent admissibility contract | **YES** | `RS(S)` pre-reasoning supply with no post-hoc filter (O15) |
| D | Explicit missing/stale/invalid semantics via `ρ_{D,τ}` | **YES** | §3.1, O01–O14 |
| E | Explicit severity ordering and monotone admissible sets | **YES formally, NOT distinctive** | Established in our formalism; paralleled by Baxi (2026) and Kang (2026) |
| F | Re-instantiation through domain-specific component classifiers | **PARTIAL** | Specified as a three-step recipe and illustrated for two further domains. **No cross-domain instantiation, implementation or evaluation exists anywhere in the repository** |

**Determination.** The evidence supports *generalised beyond a single hazard variable* and *domain-reinstantiable at the governance-structure level*. It does not support *domain-independent*.

**The formal conditional is retained and must not be converted.** The statement

> the proved properties hold for any correct instantiation satisfying the stated assumptions

is a **FORMAL** claim, defensible because the proofs quantify over the structure of the governance pair rather than over site-specific values. It must **not** become an empirical portability, deployment or applicability claim.

Note for drafting: no canonical authority currently articulates a generalisation claim — `appendix-c-formalisation.md` contains no "generalis\*", "reinstant\*" or "transferab\*" language. The claim rests on the structure of the proofs and on the v3 Generalisation section, which already carries the correct hedge that domain suitability "remains an empirical question that domain-specific prototype work must address."

---

## 5. Final frozen C1 wording

> **C1.** A formal operational specification of graduated advisory-scope governance that separates AI participation `G(S)` from admissible advisory scope `A_AI(S)`, generalises the conditioning state beyond a single hazard variable to a classified multi-component environmental state `S = f(E)`, and defines explicit observation-resolution, declared-exclusion, failure and containment semantics — including an operational classifier `F_{D,τ} = f ∘ ρ_{D,τ}` total over the observation space, four distinguished responses to invalid, absent, stale and unmeasured inputs, and an advisory-admissibility contract enforced by pre-reasoning rule-set supply rather than by post-generation filtering.

**Mandatory accompanying qualifiers**, all of which must appear in the manuscript wherever C1 is stated or expanded:

1. The governance mechanism itself is **not** claimed as new; advisory-type restriction conditioned on an externally measured state has operational precedent in certified collision-avoidance avionics.
2. Totality, monotonicity and containment are **not** claimed as novel properties; they characterise and verify the formalisation.
3. Re-instantiation across domains is **specified and illustrated, not empirically demonstrated**.
4. `ageᵢ` is specified but unparameterised; `reasons` runtime capture is unimplemented; `RS(SAFE)` is empty in the evaluated configuration.

---

## 6. Implementation-fidelity disposition

    IMPLEMENTATION_FIDELITY = SUPPORTING_EVIDENCE

Supports **C1 only**. Not a third contribution. Sited as an executable-conformance subsection inside the C1 material.

**Allowed role.** Evidence that the operational formal specification is executable, and that the configured admissibility contract was respected within the bounded deterministic interface-contract fidelity state space.

**Allowed statement, verbatim:**

> The executable implementation produced zero violations of the configured advisory admissibility contract within the bounded deterministic interface-contract fidelity state space.

**Bounded figures.** 292 primary fidelity episodes — 32 SAFE, 260 CAUTION. 244 episodes with advisory; 16 CAUTION episodes with no advisory. **454 advisory records** of the single generated conclusion type **`Delay`**. F1 = 0, F2 = 0, F3 = 0 violations/mismatches. 162 UNSAFE gate-off structural cases, **not part of the 292 primary episode denominator**.

**Never write "454 advisory types".** They are 454 records of one type.

**Prohibited interpretations:** complete SAFE advisory-space validation · all recommendation types exercised · strong empirical validation of containment · real-world validation · effectiveness evidence · safety-improvement evidence.

**The structural limitation must accompany every statement of this evidence:** `R-SAFE-001 = DEFERRED`, the SAFE rule set is empty, all four implemented rules are CAUTION rules, and every generated advisory is `Delay`. Containment was therefore exercised **only on the restrictive side** — no advisory was generated that a narrower state would have had to suppress.

---

## 7. C2 — empirical audit

The five-year retrospective replay is strong enough to be the second headline contribution, and is the **stronger** of the two: no source in the validated comparison set empirically characterises how often an intermediate governance level changes the outcome relative to participation-only governance.

**Core evidence, both configurations, both fully provenanced:**

| Quantity | PRIMARY | RESOLUTION |
|---|---|---|
| ΔL2 — intermediate-level contribution | **5.81%** | **4.48%** |
| C1↔C3 — intermediate-state control | **0.00%** | **0.00%** |

Scale: 43,848 hourly records, approximately five years (PRIMARY).

**Supporting context (PRIMARY only, provenanced):** C0↔C1 = 42.88%, C0↔C2 = 48.69%.

**Frozen interpretation:**

> The intermediate advisory-scope layer produces a measurable governance-outcome difference relative to participation-only governance, while merely introducing an intermediate state without advisory-scope differentiation does not produce such a difference under the evaluated comparator definitions.

**Prohibited interpretations of 5.81% / 4.48%:** safer · safety improvement · risk reduction · better decisions · improved effectiveness · accident prevention · any human or physical safety outcome. The contribution describes **governance-outcome divergence**, nothing else.

**PRIMARY and RESOLUTION are alternative environmental-data configurations.** They are not confidence intervals, uncertainty bounds, repeated trials or error bars. Never write `5.81 ± 4.48` or any equivalent. E3's mandatory dual-configuration scope is `{E1, E2, E6}`.

---

## 8. Final frozen C2 wording

> **C2.** An empirical characterisation, using five years of retrospective environmental traces, of when advisory-scope graduation produces governance outcomes distinct from participation-only governance — reporting the intermediate-level contribution under both the PRIMARY and RESOLUTION environmental-data configurations, together with a zero-divergence control against an intermediate-state comparator that lacks advisory-scope differentiation.

**Mandatory accompanying qualifiers:**

1. The measured quantity is divergence of admissible advisory sets at the governance layer — not a human, operational or physical safety outcome.
2. Results characterise one deployment site over the evaluated period under the evaluated comparator definitions.
3. All severity figures are **lower bounds**: the replay declares `D = {m}` (no marine-warning archive exists for the site), and κ = 0 throughout the record, so `g_r` figures are lower bounds by an unknown margin.
4. PRIMARY and RESOLUTION are alternative configurations, not uncertainty bounds.

---

## 9. C1↔C3 = 0.00% — interpretation rule

**Placement: inside C2.** Not a Discussion observation.

It is one of the strongest empirical controls available, because it shows the observed ΔL2 effect is tied to **advisory-scope differentiation** rather than to the mere addition of another labelled governance state. Under the evaluated comparator definitions, C1 and C3 are identical at the admissible-set level.

**Allowed interpretation:**

> Merely introducing an intermediate or traffic-light state does not necessarily produce a distinct admissible advisory-scope outcome.

**Prohibited generalisations:** all traffic-light systems are equivalent · all three-state systems add no value · advisory-scope governance is universally superior · any statement about traffic-light systems in general. The result is bounded to the evaluated comparator definitions.

---

## 10. Hysteresis disposition

    HYSTERESIS = SECONDARY_RESULT_OMITTED_FROM_CONTRIBUTION_STORY

Excluded from C1 and C2. May appear in Results or Discussion if page budget permits, and only with the established qualification:

> Hysteresis was evaluated as a precautionary stabilisation mechanism, not because a mode-chattering requirement had been established.

The mode-chattering claim was withdrawn and must not be restated. The 10.36% figure must never be used to support novelty or effectiveness. E4 is **PRIMARY-only** under the current E3 design (`E4_RESOLUTION = NOT_REQUIRED_BY_CURRENT_E3_DESIGN`); do not create a RESOLUTION hysteresis result.

---

## 11. Human-authority disposition

    HUMAN_AUTHORITY_INVARIANCE = ARCHITECTURAL_PROPERTY_NOT_HEADLINE_CONTRIBUTION

The property is real and canonical: human decision authority is unconditional in all three states; no algorithm introduces automated approval, prohibition or override semantics; UNSAFE state notices report the state and the operator's retained authority rather than instructing the operator; and fault-, hazard- and policy-driven UNSAFE receive the same governance response without constraining human authority.

**Placement:** architecture description, comparison table, and discussion. **Not** in C1 wording, and not as a load-bearing novelty clause — the novelty audit found the distinction real but thin relative to TCAS, where the crew remains the actor but compliance is the procedural expectation.

---

## 12. E5 / H3 / human-outcome exclusion boundary

    E5                            = OPEN
    E5_HARNESS                    = CLOSED
    MACBOOK_REFERENCE             = COMPLETE_REFERENCE_ONLY
    E5_ANDROID_TARGET_BENCHMARK   = DEFERRED_MANDATORY
    H3                            = OPEN_UNSUPPORTED
    HUMAN_STUDY                   = NOT_REQUIRED / DEFERRED

E5 supports no contribution and no research question. No performance RQ. Development-machine timing is not target-hardware evidence and must not be scaled or extrapolated.

**Excluded from the freeze entirely:** smartphone feasibility · low-resource deployment validation · real-time performance · target-hardware performance · trust · calibrated reliance · human decision quality · behavioural benefit · accident reduction · livelihood benefit · real-world operational safety improvement.

Target-hardware performance may be mentioned only as future work or as a limitation.

---

## 13. Corpus-count reconciliation

    STRUCTURED_REVIEW_SAMPLE      = 72
    CORPUS_COUNT_RECONCILIATION   = CLOSED

**Binding reporting rule for all subsequent drafting:**

1. The structured review sample remains **72 manuscript-facing papers**. Do not change it. Do not write 78.
2. The six validated novelty-defence sources are **targeted post-review additions**, introduced during reviewer-driven novelty validation and the conference rebuild. They must be described separately from the structured review.
3. **No systematic-review rerun is required**, because the review methodology has not changed. The six sources were located by a bounded mechanism audit, not by the search and screening protocol.
4. Merging them into the 72 count without re-running search and screening **would** compromise methodological consistency and would misrepresent how they were found.

Manuscript wording must distinguish *the original structured review of 72 papers* from *targeted post-review literature added during novelty validation*. Consistent with `docs/canonical/review-protocol.md` §Corpus reconciliation, which fixes 72 as the subset that advanced to full review at manuscript submission.

---

## 14. RQ-direction assessment

Directional only. RQs are not redesigned or inserted here.

| RQ | Verdict | Reasoning |
|---|---|---|
| RQ1 — "How can graduated advisory-scope governance be specified as a general runtime governance abstraction that separates AI participation from admissible recommendation scope while preserving explicit containment properties?" | **NEEDS_REWORDING** | Two problems. "General" must be scoped to match §4 — it cannot carry "domain-independent". And the phrasing risks implying the containment properties are themselves novel; it should ask how the governance is *specified operationally*, foregrounding observation-resolution and exclusion semantics per §3.1 |
| RQ2 — "How often does graduated advisory-scope governance produce governance outcomes that differ from participation-only governance in retrospective environmental replay?" | **ALIGNED** | Maps directly onto ΔL2 and the comparator set. Fully provenanced. No rewording required |
| RQ3 — "Are those governance differences preserved under the alternative environmental-data configuration?" | **NEEDS_REWORDING** | "Preserved" implies robustness, replication or statistical stability. PRIMARY and RESOLUTION are alternative configurations, not uncertainty bounds. Safer direction: *"How does the observed governance-outcome divergence differ under the alternative environmental-data configuration?"* |

---

## 15. Title decision

    TITLE = RETAIN

> **Evaluating Graduated Advisory-Scope Governance for AI Decision Support**

The operative verb is *Evaluating*, which claims evaluation rather than invention — precisely the repositioned contribution. No symbols, no mathematics, no footnotes, no subtitle. Consistent with the frozen C1 and C2.

---

## 16. Prohibited contribution wording

Absolute prohibitions, carried forward from the novelty audit and extended by this freeze:

**Novelty claims** — first · first-ever · unprecedented · globally novel · uniquely novel · no existing architecture · no prior system restricts advisory scope · first formal advisory-admissibility mechanism · first graduated governance architecture · first use of environmental state for governance · first nested advisory set · the first formalisation of advisory constraints.

**Property-novelty claims** — totality, monotonicity, Safety Dominance or containment described as novel properties, or as properties without precedent.

**Scope claims** — domain-independent (as an engineering or applicability claim) · demonstrated cross-domain applicability · validated in other domains · portable to any domain.

**Outcome claims** — safer · safety improvement · risk reduction · accident prevention · improved decision quality · improved trust · calibrated reliance · effectiveness · real-world validation · validated deployed system · operational safety improvement · livelihood benefit.

**Evidence-type crossings** — 5.81% as a safety figure · deterministic census presented as statistical inference · sensitivity configuration presented as an uncertainty interval · formal containment presented as empirical safety · prototype fidelity presented as real-world effectiveness · `5.81 ± 4.48` or equivalent.

**Fidelity misstatements** — 454 advisory types · complete SAFE advisory-space validation · all recommendation types exercised · strong empirical validation of containment.

**Performance claims** — smartphone feasibility demonstrated · low-resource deployment validated · real-time performance validated · target-hardware performance established · any H3 pass.

---

## 17. Claim-type classification

Every frozen clause is tagged in [`contribution-claim-matrix.csv`](contribution-claim-matrix.csv). Summary of the category boundaries this freeze enforces:

| Claim type | Frozen content |
|---|---|
| **FORMAL** | The governance pair and its constraints; totality; monotonicity; Safety Dominance; containment; operational totality; the conditional that proved properties hold for any correct instantiation satisfying the stated assumptions |
| **IMPLEMENTATION_FIDELITY** | The bounded conformance result — 292 episodes, 454 records of type `Delay`, zero F1/F2/F3 violations within the bounded deterministic interface-contract fidelity state space |
| **EMPIRICAL_TRACE** | ΔL2 (5.81% / 4.48%); C1↔C3 (0.00% / 0.00%); C0↔C1 and C0↔C2 PRIMARY; replay scale 43,848 hourly records |
| **LITERATURE** | The scoped statement in §3.2; the precedent acknowledgements in §2; the structured review of 72 papers; the targeted post-review additions |
| **INTERPRETATION** | "Governance-outcome divergence"; the intermediate-layer reading of ΔL2; the C1↔C3 control reading — all bounded to the evaluated comparator definitions |
| **LIMITATION** | R-SAFE-001 deferred and `Delay`-only advisories; `D = {m}` lower bounds; κ = 0 lower bounds; `ageᵢ` unparameterised; `reasons` unimplemented; re-instantiation not demonstrated; E5/H3 open; no human study |

**No clause may silently cross categories.** "The architecture guarantees Safety Dominance" is FORMAL; it must never become "the architecture improves operational safety", which would be an unsupported EMPIRICAL/human-outcome claim.

---

## 18. Downstream drafting rules

Binding on RQ redesign, outline and drafting.

1. **Baseline is v3** (`publications/active/ipsci-2026/submissions/v3-revision/manuscript-v3.md`), not v2.5.
2. **Exactly two headline contributions.** No phantom third inherited from the old outline.
3. `OLD_REVIEW_HEADLINE_CONTRIBUTION = WITHDRAWN`. v3's contribution 1 — *"from 72 papers… no architecture identified restricts AI advisory scope as a function of classified environmental safety state"* — is no longer defensible as a headline and is not restated in that form. The review survives as literature foundation, positioning evidence and the historical basis for the research gap.
4. **The avionics precedent must be acknowledged** at first manuscript-facing use of "graduated advisory-scope governance", in Related Work, and wherever the gap is stated.
5. **All gap statements are scoped** — "Within the reviewed literature…", "We did not identify prior work in the reviewed literature that…". Never unscoped.
6. **Stale v3 text to repair:** the "being developed as a prototype" framing; "Prototype fidelity has not yet been verified empirically"; "the reasoning engine is specified but not implemented"; and the offer of decision-support utility as a secondary metric (the utility construct is `OPEN — CONSTRUCT DEFINITION REQUIRED`).
7. **Superseded-figure blacklist remains in force**; `g_w` is always reported as 2 activations / 0 bindings; `g_m` and κ lower-bound disclosures travel with every severity figure; hysteresis carries its qualification; solar provenance is described as a NOAA-style low-precision solar-position formulation validated against USNO; formal-model consistency follows Appendix C, with `f(E)` for the ideal case and `F_{D,τ}` for deployed behaviour.
8. **`Property 5.1 / 5.2 / 5.3` are legitimate formal objects.** The obsolete pattern is `Theorem 5.x` only.
9. **Six-page budget.** Hysteresis is the first thing to cut; the operational-semantics block (§3.1) and C2 are the last.

---

## 19. OPEN items

| Item | Status | Blocking? |
|---|---|---|
| `RESOLUTION_PAIRWISE_C0_C1_C0_C2 = PROVENANCE_INCOMPLETE` | C0↔C1 = 41.08% and C0↔C2 = 45.56% are canonical in the Journal 1 manuscript, the prediction register (P24, P23) and `report-c8-migration-2026-09-08.md`, but have **no row** in `data/journal1-manuscript-evidence-sync/quantitative-provenance.csv`. Not recomputed; empirical result unmodified. **Downstream provenance-repair item.** The freeze does not depend on these two values | **No** |
| `ageᵢ` unparameterised | Freshness machinery specified; no value proposed. Do not invent one | **No** — reported as a specification limitation |
| `reasons` runtime capture | Unimplemented (OPEN-B1-2); specification contract only | **No** |
| `R-SAFE-001` | DEFERRED. `RS(SAFE)` empty in the evaluated configuration | **No** — carried as a limitation |
| E5 / H3 | OPEN / OPEN_UNSUPPORTED | **No** — excluded from the freeze |
| Cross-domain re-instantiation | Specified and illustrated, never demonstrated | **No** — bounds the generalisation claim |
| AMICT template and current-cycle page limit | Outstanding from the first readiness analysis | **No** — affects final formatting, not the freeze |

---

## 20. Changed files

**Created:**

- `data/amict-conference-rebuild/contribution-freeze-v2.md` (this file)
- `data/amict-conference-rebuild/contribution-claim-matrix.csv`

**Untouched, as required:** `manuscript-v3.md` and all publication manuscripts · all four prior AMICT evidence artefacts · all empirical artefacts and scripts · all CLOSED Journal 1 workstreams · all corpus-count figures · `notes/` and `citation-notes-map.md`.

No manuscript drafted. No `.docx`, `.pdf` or `.tex` created. No experiment run. No empirical result recomputed. No architecture, threshold or comparator changed.

---

## 21. Stop-condition assessment

| # | Condition | Result |
|---|---|---|
| 1 | Generalisation cannot be supported without a new experiment | **Did not fire** — supported at the narrower strength (§4) |
| 2 | C1 materially duplicates validated prior work after removing formal-property novelty | **Did not fire.** Tested per §15 of the execution decisions: the scoped combination — multi-component external environmental classification + operational observation-resolution semantics + advisory-type admissibility contract + formal containment + generator-independent governance abstraction — is not occupied by any comparator. **No source in the validated set carries the operational-resolution block at all.** TCAS has no exclusion calculus or operational totality; ACAS X proves collision-freedom for one system; Parasuraman is a design-time taxonomy; Bernabei governs allocation; Kwon & Kim govern participation on model confidence; Baxi conditions on agent robustness over executable permissions; Kang conditions on task metadata over oversight intensity; shielding filters executable actions at runtime rather than supplying an admissible rule set pre-reasoning |
| 3 | C2 unstateable without implying improved safety | **Did not fire** — stated as governance-outcome divergence (§8) |
| 4 | Wording requires E5 | **Did not fire** |
| 5 | Wording requires H3 | **Did not fire** |
| 6 | Wording requires human-study evidence | **Did not fire** |
| 7 | Corpus count requires reopening the structured review | **Did not fire** (§13) |
| 8 | Numerical conflict between frozen authorities | **Did not fire** — one provenance-completeness item, not a conflict (§19) |
| 9 | Wording requires modifying architecture, thresholds, comparators or evidence | **Did not fire** |

---

    CONTRIBUTION_FREEZE_V2       = CLOSED
    MECHANISM_NOVELTY            = WITHDRAWN
    HEADLINE_CONTRIBUTIONS       = 2
    C1                           = FROZEN (formalisation / scoped generalisation)
    C2                           = FROZEN (empirical characterisation)
    IMPLEMENTATION_FIDELITY      = SUPPORTING_EVIDENCE
    CORPUS_COUNT_RECONCILIATION  = CLOSED
    RQ_REDESIGN                  = NOT_STARTED
    CONFERENCE_MANUSCRIPT        = NOT_DRAFTED
