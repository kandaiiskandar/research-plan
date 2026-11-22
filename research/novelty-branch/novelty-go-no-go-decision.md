# Novelty Research Decision

**Prepared:** 17 November 2026 · **Author:** Claude (Cowork session) · **Status:** exploratory research branch, separate from the thesis. **Frozen RQ1–RQ3 and all canonical artefacts untouched.** No experiment was run, no licence requested, no external request made.

**Companions:** `novelty-literature-matrix.md`, `candidate-research-gaps.md`, `evaluation-feasibility.md`.

---

## The decision

# CONDITIONAL

**Not GO**, because the three gaps the brief proposed are occupied — two of them by peer-reviewed work, one of it four months old — and the single gap that survives is a formal distinction without a method, a guarantee, or a confirmed benchmark.

**Not NO-GO**, because that surviving distinction is absent from all 33 verified sources, it has a worked and measurable empirical instance, and the cheapest test that could close it has not been run.

---

## The three questions the brief asked

### What specific problem remains unsolved?

**Prior art decides whether to emit an output. It does not ask whether the output is derivable from the evidence available, and it has no state for "derivable but unwarranted".**

Every verified method treats abstention as a choice about an output whose derivation is presupposed: emit or abstain on confidence (#4, #21, #32); emit within a risk budget (#1, #2, #5); emit with a qualifier (UpToDate); withhold the category (#8 USPSTF Grade I); or report that the property cannot be decided (#6, #7). None distinguishes:

- **evidential reachability** — whether an output type can be derived *at all* from the available evidence class, independent of confidence or risk budget; from
- **evidential support** — whether, given reachability, the derivation carries information beyond a trivial baseline.

**The unoccupied state is "reachable but unsupported".** It is distinct from "cannot produce" and from "unconfident", and no source has it.

### What evidence demonstrates it?

**Negative evidence — 33 verified sources, none with the distinction.** The two closest antecedents stop in identifiable places. Monitorability (#6, Bauer et al., *ACM TOSEM* 2011, peer-reviewed, read in full) is a reachability concept with theorems, but concerns **one property's decidability under any continuation** and has no graded support notion — its insufficiency is logical and binary. Finite dismissibility (#7b, Gorostiaga & Sánchez, read in full, **venue unknown**) classifies which individual verdict values survive a finite imperfect observation — closest overall — but within one property's verdict domain. AC-RAC (#1, ICML 2026, peer-reviewed, read in full) eliminates actions whose worst case collapses, which is **utility** elimination over a confidence-derived set; it assumes every action is derivable.

**A peer-reviewed negative that supports the gap.** Erokhin (*Sci* 8(11):363, 2026) shows that across five availability-aware strategies **the output label set never changes**, only the model behind it — the sensor-robustness tradition does not ask whether an output type is reachable.

**Positive evidence that the distinction is measurable, not merely stateable.** A worked instance exists, computed in this project for an unrelated purpose:

| Output type | Evidence class = present observation only | Result |
|---|---|---|
| `DepartureTime` | Derivation predicate requires a strictly better later hour; persistence predicts every later hour equal to the present ⇒ predicate unsatisfiable | **Unreachable. Observed rate exactly 0.00%** over 7,305 episodes — *predicted from the predicate before measurement* |
| `Duration` | Predicate satisfiable; produced in 69.68% of episodes | **Reachable but unsupported.** Step residual against the episode-specific margin **exactly 0.000000**; baseline R² **exactly 1.000000**; calendar contribution **0** |
| `Duration` under a forecast surrogate | — | **Reachable and supported.** Ten distinct values, 24.65% unexplained, calendar explaining 31.5% of residual |

The exactly-zero residual is what makes it a test: under a trivial baseline the statistic is zero **by construction**, not merely small.

### Why would the proposed method be scientifically distinct and testable?

**Distinct**, if and only if the claim is pitched at (ii) and the (i)/(ii) separation. Reachability alone cannot be claimed — monitorability has it, and **this project has already conceded Bauer et al. 2011 in its own frozen literature position**. What is distinct is: output types carrying **declared evidentiary preconditions derived from what the type requires**, rather than per-type **risk budgets chosen to equalise calibration** (#1, where α is uniform across actions by construction) or **assigned by risk** (#2).

**Testable**, by a pre-registered test that needs no new method: **compute the support statistic and model confidence on the same public benchmark and test whether they are monotonically related. If they are, the distinction collapses into selective prediction and the branch ends.**

---

## Why not GO

| | Obstacle | Severity |
|---|---|---|
| **1** | **AC-RAC (ICML 2026) occupies the core of G1 and much of G3.** Peer-reviewed, published four months before this search, same construction — finite discrete action set, per-action calibration, clinical and recommender experiments — and its max-min rule already makes uncertainty restrict reachable action categories. **Any claim must survive a head-to-head on AC-RAC's own benchmarks, and that has not been attempted** | **High** |
| **2** | **G3 is occupied by a non-ML source that is hard to argue around.** USPSTF Grade I withholds an entire recommendation category when evidence is "lacking, of poor quality, **or conflicting**", and Grades A–D carry different certainty requirements. That *is* evidence-sufficiency-conditioned output admissibility, institutionalised. The honest counter is level and mechanism — runtime and per-instance versus authoring-time and population-level — which is a real distinction but **not a distinction of idea** | **High** |
| **3** | **The closest single threat is an unreviewed preprint that may be published before submission.** Role-Stratified CRC (arXiv:2607.24343, Jul 2026) combines per-role risk budgets with an input-provenance admissibility score — category-differentiated requirements *and* evidence-based admissibility in one system | **Medium-high, and rising with time** |
| **4** | **No benchmark is confirmed to have both multiple semantically distinct output types and controlled evidence-class variation.** B1 has multiple actions with complete inputs; B3 has lead-time structure with one output type; B4 has evidence grading with one answer type. **If one must be constructed, that is weak evidence for a novelty claim** | **High — the largest feasibility risk** |
| **5** | **A plain confidence margin has already beaten a sufficiency-aware rule once.** 90.36% selective accuracy at matched coverage against 90.05% (Pandian, unreviewed, one dataset, acknowledged artifacts). Weak evidence, but a committee will raise it | **Medium** |
| **6** | **No guarantee has been formulated.** Soundness and maximality of the admissibility partition are plausible targets; neither exists. **Until one does, this is an empirical paper, not a methodological contribution** | **Medium-high** |
| **7** | **Two load-bearing sources are unread.** The *Medicine Discovery* commentary — the closest source in domain and framing — was read **only via a press release**, and the ACC/AHA Class-of-Recommendation × Level-of-Evidence link is **unverified** | **Medium** |
| **8** | **Two literatures were not covered.** Dempster–Shafer conflict and reliability discounting, and active feature acquisition / test selection. Both plausibly contain closer prior art, and neither was read beyond titles | **Medium** |

## Why not NO-GO

1. **The distinction is absent from every verified source**, and its absence is structural — prior art asks a different question — rather than an unexplored application.
2. **A worked, measurable instance already exists**, with a statistic that is exactly zero under a trivial baseline.
3. **The cheapest decisive test has not been run**, and it requires no method, no data licence, no participants and no external request.
4. **Erokhin provides a peer-reviewed negative** confirming that the adjacent tradition does not do this.

---

## Conditions to convert CONDITIONAL to GO or NO-GO

In order. **Each is cheap and each can end the branch.**

| | Condition | Resolves | Cost |
|---|---|---|---|
| **K1** | **Run M1** — test whether the support statistic is monotone in model confidence on one public benchmark, using existing baselines only. **Monotone ⇒ NO-GO** | Obstacle 5; the core question | Days. No new method |
| **K2** | **Verify analytically that the support statistic is identically zero on a deterministic function of the evidence class.** Failure ⇒ re-specify or stop | Whether the criterion is a test | Hours |
| **K3** | **Read AC-RAC's experimental section and Appendix D in full** (rare-action stress tests, action-space scaling) and determine whether a head-to-head is constructible on its benchmarks. **Not constructible ⇒ NO-GO** | Obstacles 1, 4 | Days |
| **K4** | **Obtain and read the *Medicine Discovery* paper**, and verify the ACC/AHA COR × LOE link | Obstacle 7 | One request each |
| **K5** | **Read the Dempster–Shafer discounting literature and the active-feature-acquisition primaries.** Either may contain the distinction | Obstacle 8 | Weeks |
| **K6** | **Formulate a candidate guarantee** — soundness and maximality of the partition under a stated evidence model. No guarantee ⇒ reposition as an empirical contribution and re-decide | Obstacle 6 | Weeks |

**K1 and K2 first.** Together they cost less than a week, need nothing external, and either can close the branch before any further effort.

---

## Relation to the thesis — unchanged

**Frozen RQ1–RQ3 are preserved and this branch does not touch them.** `final-research-chain-lock.md` records the experiment set as **SUFFICIENT**, and its frozen literature position already concedes *"advisory-category inhibition"*, *"human-facing advisory inhibition based on observation validity"* and *"totality over incomplete observations (Bauer et al. 2011)"*, with the instruction that **"no report wording may imply generic novelty for any of these."**

**Two consequences.** First, this branch cannot be folded into the thesis as a novelty claim without contradicting the lock — the mechanism is conceded, so only formal theory and guarantees remain available, and those do not yet exist. Second, the branch is **correctly placed as a separate post-thesis or parallel methodological strand**, which is how the brief framed it and how it should stay.

**The thesis's own route is unaffected:** the supervisor memorandum's Path B recommendation stands, and the reachability-versus-support distinction serves it as a *limitation statement* — which requires no novelty claim at all, and which the lock permits.

---

## Claim-to-source evidence table

**Legend.** **FULL** = PDF retrieved and text read · **PAGE** = page fetched, read as a summarising rendering · **ABSTRACT** = abstract/landing page · **RECORD** = metadata only · **PR** = press release only · **REPO** = this project's own artefact.

| # | Claim | Source | Read | Peer-reviewed | Supported / Interpretation |
|---|---|---|---|---|---|
| 1 | CAP (ACML 2025) exists: Tayebati et al., PMLR 304:926–941 | proceedings.mlr.press/v304/tayebati26a.html | FULL | **Yes** | Supported |
| 2 | Zhu et al. ICML 2026 exists: "Conformal Risk-Averse Decision Making with Action Conditional Guarantee", PMLR 306:167248–167276, method AC-RAC | proceedings.mlr.press/v306/zhu26z.html; openreview B5RiXueKqb; icml.cc/virtual/2026/poster/65697 | FULL | **Yes** | Supported |
| 3 | AC-RAC calibrates a per-action threshold vector λ=(λ_a) and guarantees action-conditional coverage ≥1−α for every action under exchangeability | as above | FULL | Yes | Supported |
| 4 | AC-RAC's abstention is confidence-driven, with no notion of missing, stale or conflicting input | as above | FULL | Yes | Supported |
| 5 | CAP's unit is the output *mode* (predict / set / abstain), i.e. granularity levels of one answer, not distinct categories | as above | FULL | Yes | Supported |
| 6 | CAP's authors concede RL may compromise the conformal guarantees | as above | FULL | Yes | Supported |
| 7 | Impute-then-predict with conformalisation preserves marginal coverage but under-covers for some missingness patterns, worst when important features are missing | Zaffran et al., ICML 2023, PMLR 202 | FULL | **Yes** | Supported |
| 8 | CP-MDA-Exact/-Nested give mask-conditional validity under MCAR (Thms 5.3, 5.4) | as above | FULL | Yes | Supported |
| 9 | LTL₃'s "?" is *defined* as the observed word being insufficient to determine φ under any continuation (Def. 2.4), with monitor correctness (Thm 2.7) | Bauer, Leucker & Schallhart, *ACM TOSEM*, DOI 10.1145/2000799.2000800 | FULL | **Yes** | Supported |
| 10 | Basin et al. give three-valued semantics over incomplete **and disagreeing** logs, with a consensus operator yielding ⊥ on conflict, plus knowledge-monotonicity and soundness; complete only for fragment L³_c | Basin et al., RV 2012, DOI 10.1007/978-3-642-35632-2_17 | FULL | **Yes** | Supported |
| 11 | USPSTF Grade I is triggered when evidence is "lacking, of poor quality, or conflicting" and withholds the for/against recommendation | uspreventiveservicestaskforce.org grade-definitions | FULL | Procedural | Supported |
| 12 | USPSTF Grades A–D carry different certainty requirements | as above | FULL | Procedural | Supported |
| 13 | GRADE 14 permits "no recommendation" and research-only recommendations, but **encourages** panels to recommend even at low confidence | Andrews et al., *J Clin Epidemiol* 66:719–725, DOI 10.1016/j.jclinepi.2012.03.013 | FULL | **Yes** | Supported |
| 14 | UpToDate's 1A–2C scheme has **no insufficiency category** | wolterskluwer.com grading-guide | FULL | Commercial | Supported |
| 15 | Sadinle et al. give per-class error levels α_y with finite-sample distribution-free guarantees | *JASA* 114(525):223–234; arXiv:1609.00451 | ABSTRACT | **Yes** | Supported |
| 16 | Role-Stratified CRC uses per-role risk budgets α(r) with an input-provenance admissibility score | arXiv:2607.24343 | PAGE | **No — preprint** | Supported |
| 17 | SURE-RAG keeps sufficiency architecturally separate from an uncertainty penalty, and reports **no** risk guarantees; conformal thresholds collapsed coverage | arXiv:2605.03534 | FULL | **No — preprint** | Supported |
| 18 | RINSE scores sufficiency from question + evidence alone, explicitly not generator confidence; does not measure conflict or staleness | arXiv:2609.37469 | FULL | **No — preprint** | Supported |
| 19 | Erokhin: across five availability-aware strategies the output label set never changes | *Sci* 8(11):363, DOI 10.3390/sci8110363 | PAGE (truncated) | **Yes** | Supported |
| 20 | Suresh et al.: MLLM refusal is not a direct readout of visual evidence | arXiv:2610.37430 | FULL | **No — preprint** | Supported |
| 21 | A conflict/sufficiency-aware rule reached 90.05% selective accuracy at 53.58% coverage vs 90.36% for a plain confidence margin at matched coverage | Research Square rs-11110025/v1 | PAGE | **No — unreviewed** | Supported, **weak**: single author, one dataset, acknowledged artifacts |
| 22 | Solozobov has a four-axis evidence model (completeness, freshness, reliability, representativeness) but leaves the mapping to action out of scope | arXiv:2604.15740 | PAGE | **No — preprint** | Supported |
| 23 | Shraga et al. is the only method found conditioning admissibility on staleness; no formal guarantee | arXiv:2608.26306 | ABSTRACT | **No — preprint** | Supported |
| 24 | Gorostiaga & Sánchez classify finite dismissibility/admissibility of individual verdict values | software.imdea.org PDF | FULL | **Venue and year not stated — unconfirmed** | Supported as to content; status unverified |
| 25 | Unlu's typed deferral gates on an explicit evidence-sufficiency dimension; ~91.7% typed-deferral accuracy; no formal guarantees | arXiv:2604.16752 | PAGE | **No — preprint** | Supported |
| 26 | `DepartureTime` rate exactly 0.00% and `Duration` step residual exactly 0.000000 with baseline R² exactly 1.000000 under persistence, over 7,305 episodes | `research/non-degeneracy/causal/results-causal-replication.json` | REPO | Exploratory | Supported |
| 27 | The project's frozen position concedes advisory-category inhibition on observation validity and totality over incomplete observations, citing Bauer et al. 2011 | `docs/analysis/final-research-chain-lock.md` §A | REPO | Authoritative | Supported |
| 28 | ERA5 cannot support operational-recommendation claims; C2 operational availability not satisfied | `research/non-degeneracy/causal/availability-attestation.json` | REPO | Exploratory | Supported |
| **I1** | The surviving gap is "reachable but unsupported" | — | — | — | **Interpretation** from the absence across #1–#25 |
| **I2** | G4 is a refinement of AC-RAC rather than virgin territory | — | — | — | **Interpretation** |
| **I3** | The clinical analogy breaks on level and mechanism, not on idea | — | — | — | **Interpretation** |
| **I4** | A constructed benchmark would be weak evidence for novelty | — | — | — | **Interpretation** |
| **U1** | *Medicine Discovery* (DOI 10.1016/j.medd.2026.100004) proposes evidence-sufficiency assessment before prediction, with staleness and cross-modal conflict in a graded composite | EurekAlert 1147431 | **PR ONLY** | **Journal peer-review status unverified** | **UNVERIFIED — must be read before any claim rests on it.** Closest source in domain and framing |
| **U2** | Evidence level constrains recommendation class in the ACC/AHA COR × LOE grid | ahajournals.org, jacc.org | **blocked** | — | **UNVERIFIED.** GRADE-14 body text, which *was* read, does not make the link |
| **U3** | AC-RAC's rare-action and action-space-scaling robustness | PMLR 306 Appendix D | **fragments only** | Yes | **UNVERIFIED** — the evidence most relevant to contesting AC-RAC |
| **U4** | Venue status of Mohri & Hashimoto (arXiv:2402.10978), Conformal Risk Control (arXiv:2208.02814), Learn-then-Test (arXiv:2110.01052) | — | RECORD | **Unverified — do not cite as peer-reviewed** | **UNVERIFIED** |
| **U5** | Dempster–Shafer conflict/reliability discounting; active feature acquisition primaries | — | **not read** | — | **ACKNOWLEDGED COVERAGE GAP** — either may contain closer prior art |

---

## Recommendation

**Proceed to K1 and K2 only.** Together they cost under a week, need nothing external, and either can close the branch. Do not build the method, do not select a benchmark suite, and do not write a paper outline until K1 returns a non-monotone result and K2 verifies the statistic is structurally zero on a trivial baseline.

**If K1 shows monotonicity, record NO-GO and stop.** That is the likeliest single outcome worth preparing for, and recording it as a negative is cheaper than discovering it after a benchmark has been built.

**Keep the branch separate from the thesis regardless of outcome.** Frozen RQ1–RQ3 stand, the lock's concessions bind, and the thesis's own route — Path B in the supervisor memorandum — needs none of this to proceed.
