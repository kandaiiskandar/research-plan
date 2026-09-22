# Final External Novelty Stress-Test

**Date:** 2026-09-21
**Task:** External primary-source falsification of the three remaining candidate contributions R1, R2, R3.
**Posture:** Adversarial. Objective is falsification, not confirmation.
**Canonical report:** `experiment-report-delta-l2.md` **UNCHANGED**.

---

## A. Search method

**Engines:** WebSearch (general index), direct WebFetch of primary PDFs and publisher pages.
**Date range:** No restriction; sources returned span 1990–2026.
**Screening:** Search-family → identify candidate primary source → fetch primary document → extract formal definitions and quoted passages → code. Reviews used only to locate primaries. No conclusion below rests on an abstract, snippet or secondary description.

**Search families executed (5 priority areas, 6 query families):**

| Priority | Family | Terms |
|---|---|---|
| 3, 4 | Runtime verification under incompleteness | three-valued semantics, LTL3, monitor, inconclusive, incomplete trace, total function, lossy traces, partial observability, missing events, imprecise events, conservative verdict |
| 1, 2 | Fail-operational / sensor validity | position source fault, invalid input, inhibit, degraded navigation accuracy, annunciation, TSO, ETSO |
| — | Omitted-variable bounds | partial identification, Manski bounds, monotone treatment response, monotone confounding, one-sided bound, unmeasured confounder |
| — | Safety-engineering bounds | omitted hazard, conservative lower bound on risk, incomplete hazard list, monotone severity aggregation |
| 5 | Human-facing advisory degradation | clinical decision support suppression, insufficient data, advisory withheld, data-quality gating, TAWS/EGPWS alert inhibition |

**Sources examined:** 9 search result sets screened; **6 primary/authoritative documents fetched and read**; 5 coded.

**Stop condition:** **Condition A** — clear primary-source counterexamples falsified all three claims. Search halted after establishing how directly each maps.

---

## B. External primary sources

1. **Bauer, A., Leucker, M., Schallhart, C. (2011).** "Runtime Verification for LTL and TLTL." *ACM Transactions on Software Engineering and Methodology* 20(4). DOI: 10.1145/2000799.2000800
2. **Taleb, R., Hallé, S., Khoury, R. (2023).** "Uncertainty in runtime verification: A survey." *Computer Science Review* 50:100594. DOI: 10.1016/j.cosrev.2023.100594
3. **Assumption-based runtime verification under partial observability** (2024). arXiv:2409.05456 — "Exploiting Assumptions for Effective Monitoring of Real-Time Properties under Partial Observability"
4. **Federal Aviation Administration. TSO-C151c**, *Terrain Awareness and Warning System*. https://skybrary.aero/sites/default/files/bookshelf/4189.pdf
5. **Manski, C. F. (1990, 1997); Manski, C. F. & Pepper, J. V. (2000)**, via **"Monotone Confounding, Monotone Treatment Selection and Monotone Treatment Response."** *Journal of Causal Inference* (2014). DOI: 10.1515/jci-2012-0006
6. **Alechina, N., Dastani, M., Logan, B. (2014).** "Norm approximation for imperfect monitors." *AAMAS* 2014, 117–124.

---

## C. Counterexample matrix

| Source | Domain | R1 totality / incomplete obs. | R2 exclusion → bound | R3 obs. quality → human advisory scope | Autonomous or human-facing | Formal guarantee? | Threat |
|---|---|---|---|---|---|---|---|
| **FAA TSO-C151c** | Aviation, certified | PARTIAL — invalid position source must be dropped (§5.6); no totality theorem | NO | **YES.** §5.6: *"The TAWS must **inhibit FLTA and PDA alerts** when the position source in use is faulted or invalid."* GPWS modes continue on alternative altitude sources. §§9.1–9.2: *"Inhibit status must be annunciated to the flight crew."* §7.0 requires crew notification of loss of intended function | **Human-facing** — alerts to flight crew, pilot authority | Certification requirement, not a proof | **DIRECT COUNTEREXAMPLE (R3)** |
| **Taleb, Hallé & Khoury (2023)** | Runtime verification | **YES.** Survey of an entire subfield: incomplete traces, missing events, imprecise events; conservative approximation of possible verdicts; symbolic representation of missing events; interval semantics | PARTIAL — verdict sets are bounds under incompleteness | NO — monitors, not advisory sets | Neither; verification layer | Formal semantics throughout | **DIRECT COUNTEREXAMPLE (R1)** |
| **arXiv:2409.05456 (ABRV)** | Runtime verification | **YES.** Monitoring function 𝒱 total over its domain, **four-valued** {⊤, ⊥, ×, ?} — includes an explicit *out-of-model* verdict for observations violating assumptions. Def. 1; 𝒜-observations carry data and time uncertainty | PARTIAL | NO | Neither | **YES** — formal | **DIRECT COUNTEREXAMPLE (R1)** |
| **Manski (1990, 1997); Manski & Pepper (2000)** | Econometrics / causal inference | NO | **YES.** Monotonicity assumption on an unmeasured variable yields a **one-sided bound** on the estimand. Prop. 4 (JCI 2014) gives explicit one-sided constraints. Established since 1990 | NO | Neither | **YES** — sharp bounds | **DIRECT COUNTEREXAMPLE (R2)** |
| **Bauer, Leucker & Schallhart (2011)** | Runtime verification | PARTIAL — monitor is a total function over all finite traces (Def. 2.6, Thm. 2.7) with explicit "?" inconclusive value (Def. 2.4), but incompleteness is *temporal prefix*, not invalid/missing observations | NO | NO | Neither | **YES** | **STRONG PARTIAL COUNTEREXAMPLE (R1)** |

---

## D. Strongest counterexamples

### 1. FAA TSO-C151c — falsifies R3 outright

**What it establishes.** §5.6: *"If a position source generates a fault indication or any flag indicating the position is invalid or does not meet performance requirements, the TAWS must stop utilizing that position source"*, and *"The TAWS must inhibit FLTA and PDA alerts when the position source in use is faulted or invalid."*

This is precisely the mechanism R3 claimed: an **observation-quality condition** (position source invalid) determines **which categories of advisory may be presented to a human** (Forward-Looking Terrain Avoidance and Premature Descent Alert are withheld; GPWS modes continue on alternative altitude sources), with the restriction **annunciated to the crew** (§§9.1–9.2) and the pilot retaining authority. It is human-facing, not autonomous action restriction. It is mandatory in a certification standard, not a research proposal.

**What remains different.** TAWS conditions on the validity of a *single navigation input*, not on a classified multi-component environmental state; the inhibit is a fixed per-function rule rather than a state-indexed admissible set; and there is no formal totality or containment property. These are differences of scope and formalism, not of mechanism.

### 2. Taleb, Hallé & Khoury (2023) and assumption-based RV — falsify R1

*Uncertainty in runtime verification* surveys a mature subfield explicitly organised around missing events, imprecise events, unordered events and imprecise timestamps, and catalogues formal approaches that remain total over incomplete sequences: conservative approximation of the set of possible verdicts, symbolic representation of missing events, interval-based semantics, probabilistic models. The ABRV work goes further with a **four-valued** total monitoring function whose verdicts include an *out-of-model* value for observations that violate the assumption set — a finer semantic differentiation than the project's three states plus ⊥.

"Classification is total over the observation space rather than only over ideal measurement domains" is therefore not a new formal property. It is the organising premise of a surveyed research area.

### 3. Manski's partial identification — falsifies R2

Monotone Treatment Response (Manski 1990, 1997) and Monotone Treatment Selection (Manski & Pepper 2000) establish that a **monotonicity assumption about an unmeasured variable yields a one-sided bound on the estimand**. Proposition 4 of the 2014 *Journal of Causal Inference* treatment states the bounds explicitly. The structure `declared exclusion → known directional consequence → bound on the reported quantity` is standard methodology across econometrics, epidemiology and public health, and has been since 1990.

The project's `D = {m}` ⇒ "severity figures are lower bounds" is an instance of this pattern. Applying it is correct practice; it is not a contribution.

---

## E. R1 verdict — **FALSIFIED**

Totality over incomplete observation spaces is established in runtime verification, both classically (Bauer et al., total monitor with explicit inconclusive value) and specifically for missing/imprecise observations (Taleb et al. survey; ABRV four-valued total monitoring). The project's Theorem C.1b is a correct instance of a known property class, expressed in domain notation.

## F. R2 verdict — **FALSIFIED**

Exclusion-with-directional-consequence is Manski's partial identification, established 1990–2000 and standard in several fields. That the project applies it correctly — declaring `D`, noting `g_m` can only raise severity, reporting lower bounds — is methodological hygiene of a high standard. It is not novel.

## G. R3 verdict — **FALSIFIED**

TSO-C151c §5.6 mandates exactly this mechanism in a certified, human-facing system. This is the most damaging single finding of the entire audit sequence, because R3 was the element the previous internal analysis identified as the last substantive survivor.

---

## H. Conjunction test

R1 + R2 + R3 as a combined mechanism was **not identified** in any single searched source. TSO-C151c has R3 and partial R1 but neither R2 nor a formal property. The RV literature has R1 without human-facing advisory scope or exclusion bounds. Manski has R2 with no runtime governance at all.

**Verdict: COMBINATION GAP.**

But the combination must be weighed honestly. The three elements come from three unrelated fields — certified avionics, runtime verification, and causal inference. That no single paper combines them is close to uninformative: it reflects disciplinary separation rather than an unexplored problem. A combination gap is evidence of novelty only when the fields plausibly *should* have met. Here they have not, and the burden of showing that the combination does work beyond its parts sits with this project.

---

## I. Semantic-equivalence analysis

| Prior mechanism | Proposed mechanism | Substantive or terminological? |
|---|---|---|
| Position source invalid → inhibit FLTA/PDA → remaining alerts to pilot (TSO-C151c) | Observation ⊥ → S → A_AI(S) → human | **Terminological and scope.** Same causal shape. The project generalises from one input's validity to a classified multi-component state, and adds a state-indexed admissible set. That generalisation is real but incremental |
| Monitor total over incomplete traces with inconclusive/out-of-model verdicts (RV) | `gᵢ : Obsᵢ → S` total, `gᵢ(⊥) = UNSAFE` | **Terminological**, with one substantive difference: RV's third value is *inconclusive* (genuine indeterminacy), whereas this project **resolves** ⊥ to UNSAFE. Resolving rather than reporting indeterminacy is a design choice with a safety rationale, not a new formal property — and it is weaker in expressiveness than the four-valued ABRV treatment |
| Unmeasured variable + monotonicity → one-sided bound (Manski) | `D = {m}`, `g_m` monotone → lower bounds | **Terminological.** Identical structure |

No surviving difference is computationally substantive at the mechanism level.

---

## J. Final CS contribution, separated

**Established prior work — claim none of this.** State-conditioned advisory admissibility; nested admissible sets contracting to empty; deterministic safety gating; multi-level graduated governance; weakest-link aggregation; human-in-the-loop decision support; multi-component classified state; monotone contraction; fail-safe/fail-degraded/fail-operational regimes; totality over incomplete observation spaces; conservative resolution of unusable observations; declared exclusion with directional bound; **observation validity gating which advisory categories are shown to a human.**

**Domain adaptation.** Instantiation for small-scale Malaysian coastal fisheries: vessel-conditional wave thresholds from Yaakob's operational ceiling; MET/JPS boundary provenance with the documented gap where MET publishes no lower criterion; the solar-event classifier anchored to COLREGs Rule 20(b). This is real work and correctly documented.

**Formalisation contribution.** Narrow. The composition of the governance pair `(G(S), A_AI(S))` as **two separately specified state-conditioned functions** rather than a single graduated index remains unmatched in the searched literature — Baxi unifies them, TAWS has per-function fixed rules. Modest.

**Runtime-governance contribution.** Not supported. Each element has a certified or formal precedent.

**Empirical contribution.** The strongest surviving element. A five-year deterministic census quantifying how often an intermediate advisory-scope level changes the admissible set at one site (Δ_L2 = 5.81% / 4.48%), with a pre-registered prediction register resolving 15 CONFIRMED / 9 REFUTED, an auditable provenance chain across five figure revisions, and a structural comparator showing the intermediate level is not observable in output when scope is unchanged. No searched source supplies a comparable empirical characterisation of graduated advisory-scope governance.

**Methodological contribution.** The register-plus-provenance discipline itself — predictions registered before analysis, refutations retained, every figure regenerable from one authoritative script. Unusual in this literature and independently defensible.

---

## K. Evidence–claim alignment

| Surviving element | Status |
|---|---|
| Δ_L2 activation frequency (empirical) | **CURRENT EXPERIMENT SUPPORTS** |
| Structural claim: a third label alone does not graduate governance | **CURRENT EXPERIMENT SUPPORTS** (entailed by definitions, §3.3) |
| G(S)/A_AI(S) as two separate functions | **CURRENT EXPERIMENT PARTIALLY SUPPORTS** — C1↔C2 isolates the scope term but no condition varies the two functions independently |
| Domain threshold instantiation | **CURRENT EXPERIMENT PARTIALLY SUPPORTS** — thresholds drive the replay but are not themselves validated (no incident data) |
| R1 / R2 / R3 | **MOOT** — falsified; no longer require evidence |

The alignment problem reported in the previous two analyses **dissolves**, but not favourably: the unevaluated claims are gone because they are no longer claims. What remains is evaluated by the current experiment.

---

## L. Minimum additional experiment — and a critique of the proposed exclusion sweep

**The exclusion sweep should not be run as specified.** Assessing the six questions:

1. **Does varying `D` test the claimed epistemic consequence?** **No, not directly.** The claim concerns `m`, for which *no data exists*. Varying `D` over components that *do* have data measures the sensitivity of the result to excluding **other** variables. That is an analogue, not the thing claimed. The bound on `m` cannot be quantified by any manipulation of the existing record.
2. **Does it quantify the width or direction of the lower bound?** Direction is already known by monotonicity. Width for `m` — no. Width for a *proxy* variable — yes.
3. **Is `D = {m, w}` scientifically meaningful?** **No.** `g_w` activates twice in 43,848 hours and binds in none. Excluding it is guaranteed to change nothing. The result would be a structural zero, indistinguishable from a bug, and presenting it as a sensitivity finding would be misleading.
4. **Would removing wind create an unrealistic configuration?** It would create an *uninformative* one, which is worse.
5. **Better variable?** Yes. Sweep the components that actually bind: `D = {m, r}` and `D = {m, o}`. `g_o` carries 98.71% of daylight CAUTION, so excluding it bounds the maximum possible influence of a single excluded environmental channel. That is a meaningful sensitivity result.
6. **New thresholds needed?** **No** — and this is the sweep's main virtue. Exclusion pins a component at SAFE and introduces no researcher-defined constant, so it cannot repeat the 7.5 mm/hr error. Staleness and invalidity injection would both require inventing `ageᵢ`, which remains OPEN and should not be invented.

**Recommendation:** run `D ∈ {{m}, {m, r}, {m, o}}` as an exclusion-sensitivity analysis, reported as a robustness result rather than as evidence for a contribution. Do not run `D = {m, w}`. Do not run staleness or invalidity injection until `ageᵢ` has a sourced value.

---

## M. Recommended final research gap

> Within the reviewed literature, graduated restriction of advisory categories by an externally measured state is established in certified collision-avoidance and terrain-awareness avionics; formal totality of classification over incomplete observations is established in runtime verification; and directional bounds from declared unmeasured variables are established in partial-identification methodology. Within the reviewed literature, these have not been composed into a single operational governance contract in which participation and advisory scope are specified as two separate functions over a classified multi-component environmental state, nor has the frequency with which such an intermediate level changes the admissible recommendation set been empirically characterised on a multi-year environmental record.

The second sentence carries the contribution. The first concedes the mechanism.

---

## N. Recommended contribution statement

> This work composes established governance and observation-handling mechanisms into an operational specification for advisory-scope governance in a low-resource environmental decision-support setting, and provides the empirical characterisation that the composition lacks. The mechanisms are conceded to prior work: advisory-type inhibition conditioned on input validity is mandated in certified avionics; totality of classification over incomplete observations is established in runtime verification; and bounding a reported quantity from a declared unmeasured variable is standard partial-identification practice. The contributions are (i) the separation of participation control from advisory-scope control as two independently specified state-conditioned functions; (ii) a domain instantiation for small-scale Malaysian coastal fisheries with fully traced threshold provenance, including the documented absence of an official lower criterion; and (iii) a deterministic five-year characterisation of how often the intermediate level changes the admissible recommendation set, reported under two environmental-data configurations against a structural comparator, with predictions registered before analysis.

---

## O. Decision

> ## **ONLY A COMBINATION / DOMAIN-OPERATIONALISATION CONTRIBUTION SURVIVES**

All three remaining candidate contributions are falsified by external primary sources. R3, which the internal analysis identified as the last substantive survivor, is falsified most directly: FAA TSO-C151c §5.6 requires that invalid position data inhibit specific advisory categories — FLTA and PDA — while other alert types continue, with the inhibit annunciated to a flight crew retaining authority. That is observation-quality-gated human-facing advisory scope, mandated in a certification standard. R1 is falsified by a surveyed research area whose organising premise is monitoring under missing and imprecise observations, including four-valued total monitoring functions more expressive than the project's. R2 is falsified by Manski's partial identification, standard since 1990.

What survives is not a mechanism. It is a composition, a domain operationalisation, and an empirical result. The composition — two separate state-conditioned functions over a multi-component environmental classification — was not found in the searched literature, but its three ingredients come from three unrelated fields, so their non-combination is weak evidence of anything. The domain instantiation is genuine work with unusually good provenance discipline. The empirical characterisation is the strongest element: no searched source quantifies how often an intermediate advisory-scope level changes the admissible set over a multi-year environmental record, and the register-and-provenance method behind that figure is itself defensible.

The honest position is that this is an operationalisation-and-characterisation thesis, not an architecture thesis. Whether that is sufficient at doctoral level is a supervisor judgement. It is a narrower claim than the current report makes, it is supported by the experiment that already exists, and it would survive a reviewer who knows TCAS, TAWS, runtime verification and partial identification — which the current claim would not.
