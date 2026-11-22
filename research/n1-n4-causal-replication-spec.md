# Causally Valid N1–N4 Replication — Experiment Specification

> **REVISED BY REVISION 2 — 17 Nov 2026.** `research/n1-n4-causal-replication-spec-r2.md` corrects six items here: **E-GC-2 was unpassable** (`Delay ≡ ¬Go`, so it failed for every generator) and is replaced by a forecast-dependent-only, exposure-stratified test; **E-GC-3** is now computed within hour-of-window strata; **E-GE-3 was true by construction** and becomes a structural statement — at CAUTION, restriction removes advisory detail and never alters the primary departure recommendation; **E-ES** gains threshold-specific contingency metrics with false-acceptable rate as the headline; **L-CHK-6** is reclassified as diagnostic for want of a measured benchmark; and a new **A-CHK** family separates chronological causality from operational availability (the primary run is C1-valid, C2-invalid). R1's §2 claim that `Duration ≡ f(Go)` and its prediction 2 are **withdrawn**. **Nothing below is edited** — R1 stands as written, and §7 of R2 is the cumulative ledger.


**Prepared:** 17 November 2026 · **Author of this document:** Claude (Cowork session) · **Status:** **specification only. Nothing in it has been executed.**

**Nothing was run and nothing was changed.** No code was executed for this document, no data was read, and no frozen artefact was touched. Every number quoted below is carried over from runs already recorded in `research/d4-reference-validity-and-non-degeneracy.md` and is restated, not recomputed.

**Originals preserved.** The pre-registered N1–N4 criteria, their thresholds and the 17 Nov 2026 results stand unaltered in `research/d4-reference-validity-and-non-degeneracy.md` §6 and in `research/non-degeneracy/n1-n4-results.json`. They are the **confirmatory record**. Everything proposed here is labelled **exploratory** and carries an `E-` prefix, because it is being specified after seeing a result — which is exactly the circumstance in which a criterion stops being confirmatory. §9 is the preservation ledger.

**Why a replication rather than a repair.** `research/d4-critical-review.md` §2 identified three temporal leaks in the generator: whole-record percentile normalisation (L1), whole-record cutoffs (L2), and realised forward hours read by `DepartureTime` and `Duration` (L3). L3 makes the generator an oracle on the two advice types the comparison turns on, and it biases the comparison against the graduated arm. A patched generator would be a different instrument, so the original is kept and run alongside as the leakage estimate (§3, condition **G-L**).

---

## 1. The information model — what "before the episode" means

An **episode** is a departure-window hour: a pair `(d, h)` with `h ∈ {05, 06, 07, 08, 09}` local (UTC+8). This is the architecture's own unit, which keeps `S` unambiguous.

**Decision instant.** `t_dec(d, h) = (d, h)` — the fisher decides at the candidate departure hour. This is chosen for information parity: the architecture classifies on conditions *at* `h` (`g_w`, `g_r`, `g_o`, `g_t` all evaluated at `h`), so the generator must have the same concurrent reading and no more.

**Observable set.**

> `Obs(d, h) = { all record hours t : t ≤ (d, h) }`

**Unobservable set.** Everything strictly after `(d, h)`. Any value in it may enter the generator **only** through a forecast surrogate (§3).

Three consequences to state explicitly, because each one changes the design:

1. **The information set grows across the window.** An episode at 05:00 has observed nothing of its own day beyond 05:00; an episode at 09:00 has observed 05:00–09:00. Advice-type availability will therefore vary systematically by hour-of-window, and that variation must be **reported as a result, not averaged away** (§6, E-GC-4).
2. **Calibration constants are part of the generator and inherit the same rule.** Percentile cutoffs, climatologies and damping coefficients must each be computed from `Obs` only. This is what L1 and L2 violated.
3. **The evaluator may see the future; the generator may not.** Measuring forecast skill, scoring realised conditions, and computing `S` for the governance filters all legitimately use post-episode data. **This boundary is declared, auditable and enforced by §7's checks** — it is the one place future data is allowed, and it never flows back into advice generation.

**Warm-up and evaluation window.** A causal generator cannot normalise against data it has not yet seen, so the record's opening period is spent on warm-up.

| | |
|---|---|
| Record | 2020-01-01 → 2024-12-31, 43,848 hours, 9,135 departure-window episodes |
| **Warm-up (primary)** | 2020-01-01 → 2020-12-31 — calibration only, **no episodes evaluated** |
| **Evaluation window (primary)** | 2021-01-01 → 2024-12-31 = 1,461 days × 5 = **7,305 episodes** |

**This is the single most important comparability caveat in the specification.** Every revised criterion is computed on **7,305** episodes, not 9,135. The original N1–N4 figures were computed on 9,135. **They are therefore not directly comparable**, and condition **G-L** exists precisely so that a comparable baseline exists (§3).

---

## 2. Which advice types each method can legitimately generate

This is derivable analytically, before any run, and it is the specification's central result.

| Advice type | Information it requires | **A — persistence** | **B — damped persistence toward climatology** |
|---|---|---|---|
| `Go` | Concurrent conditions: is it acceptable now? | **Yes.** Fully supported by observation at `h` | **Yes.** Identical to A at lead 0 |
| `Delay` | Concurrent conditions: is it unacceptable now? | **Yes.** Fully supported | **Yes** |
| `DepartureTime` | A forecast: *when will it be better?* | **No — structurally impossible.** Persistence predicts `ŷ(d, h+k) = y(d, h)` for all `k`, so no later hour is ever predicted better than now. The rule requiring a ≥5 percentile-point improvement **can never fire**. Expected rate: exactly **0%** | **Yes, conditionally.** The climatological diurnal term produces genuine predicted variation between hours, so a better later hour can exist. Legitimacy is bounded by **measured skill at that lead time** (§6, E-ES-1/2) — capability without skill is not support |
| `Duration` | A forecast: *how long will it stay acceptable?* | **Vacuously yes.** Under persistence, if now is acceptable every forward hour is predicted acceptable, so `Duration` collapses to the capped horizon; if not, to zero. It becomes a **deterministic function of `Go`/`Delay`** and carries no independent information | **Yes, conditionally.** Damping toward climatology gives a non-trivial predicted run length. Legitimacy bounded by skill out to the horizon |

**What this means.** Two of the four admissible advice types are forecast-dependent by their semantics, so **a generator restricted to concurrent information cannot produce them** — one not at all, one only vacuously. Method A is therefore not merely a weaker generator; it is a generator for which half the recommendation space is unreachable.

**And that is the prototype's situation.** `A_AI(SAFE) = {Go, Delay, DepartureTime, Duration}` ranges over two types unreachable from the prototype's inputs, which is why the fidelity census shows `["Delay"]` × 244, `[]` × 48, and `R-SAFE-001` sitting `DEFERRED`. The specification predicts that degeneracy from first principles rather than observing it after the fact, and §8's validation V-2 is the test of that prediction.

---

## 3. Three generator conditions, one evaluation window

All three are evaluated on the identical 7,305 episodes so that differences between them are attributable to the generator and not to the window.

### G-L — the original leaky generator, unchanged, as the leakage estimate

The `research/non-degeneracy/non_degeneracy_gate.py` generator exactly as it stands, including L1, L2 and L3, re-evaluated on the 7,305-episode window. **Its purpose is not to be defended but to be measured.** `G-L` minus `G-A` and `G-L` minus `G-B`, criterion by criterion, is the quantified leak — which `research/d4-critical-review.md` §2.4 left explicitly **[UNQUANTIFIED]**. Running it is how that gap closes.

### G-A — persistence (the honest null)

`ŷ(d, h+k) = y(d, h)` for every variable and every `k ≥ 1`. Zero skill beyond lead 0, zero cost, zero leakage, and the correct null against which any surrogate must demonstrate added value.

### G-B — damped persistence toward a causal climatology (primary surrogate)

> `ŷ(d, h+k) = α_k · y(d, h) + (1 − α_k) · clim(m(d), h+k)`

where `m(d)` is the calendar month, `clim(·,·)` is a month-by-hour mean, and `α_k ∈ [0,1]` decays with lead time `k`.

Three reasons this is the primary choice rather than something more elaborate:

- **It nests both reference points.** `α_k ≡ 1` is exactly Method A; `α_k ≡ 0` is pure climatology. So the A-versus-B comparison reads directly as *how much forecast skill is needed before the forecast-dependent advice types become supportable*, which is the question worth answering.
- **It has real skill at a tropical coastal site.** Land–sea breeze gives wind a genuine diurnal cycle and convective rainfall a strong one, so the climatological term is not decoration.
- **It is cheap and fully auditable.** No model fitting beyond `α_k`, and every constant is traceable to a dated subset of `Obs`.

**Causal estimation rules, which are the whole point:**

| Constant | Rule |
|---|---|
| `clim(m, h)` | Computed from warm-up and prior evaluation data only — for an episode in month `m` of year `y`, the mean over the same calendar month in years strictly before `y`. **Never the same month of the same year** |
| `α_k` | Fitted by minimising lead-`k` error over `Obs` only, refitted on a fixed schedule (monthly, at month boundaries), never using any data after the refit instant |
| Percentile ranks (exposure index) | Expanding window over `Obs` only. **Primary:** all prior hours. Variants in §5 |
| `P_GO`, `P_OK` cutoffs | Percentiles of the exposure distribution over `Obs` only, recomputed at the same monthly schedule as `α_k` |

**A design tension that must be surfaced, not hidden.** A month-matched climatology has one prior January available in 2021 and four by 2024, so **climatology quality improves across the evaluation window**. That is a confound with calendar time. Two mitigations, both specified: report every criterion **by year** (§6, reporting rule R-3), and run the frozen-baseline variant in §5 where the climatology is computed once from the warm-up year and held fixed — constant quality, staler estimate. Neither is leakage; both are causal; they trade bias against variance in opposite directions.

**Advice-generation rules are held identical across G-L, G-A and G-B.** Only the information source changes. Thresholds `P_GO = 60`, `P_OK = 70`, `MIN_GAIN_PCTL = 5.0`, `MIN_DURATION_H = 2`, `TRIP_HORIZON_H = 9` keep their original values in the primary run so that the generator is not silently redesigned at the same time as being de-leaked.

---

## 4. Separating generator capability from governance effectiveness

The original gate reported a single `GATE_PASS_as_preregistered` boolean over four criteria measuring three different things. That was a design error: a composite boolean over heterogeneous quantities cannot be acted on, because its failure does not say what to fix. **It is retired here and replaced by a verdict matrix** — one row per dimension, one column per generator condition, no aggregate.

| Dimension | Question | Whose property | Original criteria |
|---|---|---|---|
| **GC — Generator capability** | What advice can this generator produce, and is it informative? | The generator alone. Measured on **C0 (ungated)** | N1 |
| **ES — Evidential support** | Is each generated type *justified* by information available at the decision instant? | The generator's **forecast skill**, per lead time | **None — new** |
| **GE — Governance effectiveness** | Given a pool, how much and in which direction does each filter change what is presented? | The **filter**, conditional on the pool | N2, N3 |
| **CA — Case availability** | Are there enough cases of each needed kind to run a study? | The **site and record** | N4 |

**Why ES is new and why it matters.** Capability without skill is the exact pathology L3 created: the original generator could emit `DepartureTime` in 36.12% of cases because it *knew* the later hour was better. ES asks whether the generator had any business making that claim. It is also the machine-side analogue of the appropriateness rubric's **R2 specificity support** (`research/d4-critical-review.md` §4.3), so the two instruments can be cross-checked against each other — if raters score R2 low exactly where ES is low, both are working.

**Why the separation changes interpretation.** GC and GE pull in opposite directions under de-leaking: removing L3 lowers GC (fewer forecast-dependent types) while leaving GE's structural ceiling untouched. A composite score would net these off and report something meaningless. Reported separately, the result is legible: *this generator can produce these types with this much support, and the filter changes this much of what reaches the user.*

---

## 5. Sensitivity analysis

**The primary configuration is pre-registered as the original values**, so the headline numbers are not selected after the fact. Sensitivity is reported as a **range across the grid**, mirroring how the project already reports Δ_L2 with its 5.67–9.56% envelope rather than as a point.

| | Dimension | Primary | Variants | Why it is in the grid |
|---|---|---|---|---|
| **S1** | Percentile normalisation | Expanding over all prior | Trailing 365 d; **month-matched prior climatology** | The month-matched form is the one Niclasen's local-monthly-quantile argument supports, so it is a literature-motivated variant, not an arbitrary one |
| **S2** | Warm-up length | 365 d (7,305 episodes) | 730 d (5,480 episodes) | Tests whether results depend on climatology sample size; a stable result across S2 blunts the §3 confound |
| **S3** | Climatology refresh | Expanding (improving) | **Frozen from warm-up** | The §3 tension, run both ways |
| **S4** | Exposure aggregation | Mean of percentiles | Median; **max** | `max` deliberately mirrors the classifier's own aggregation. Including it is how the "mean was an arbitrary choice" admission gets tested instead of merely declared |
| **S5** | Variable weights | Equal (1/3 each) | Wave-only; wave-dominant 0.6 / 0.2 / 0.2 | Wave drives 97.6% of activation, so equal weighting is the least defensible part of the index |
| **S6** | Damping | Fitted `α_k` | `α_k = 0.5^k`; `α_k ≡ 0` (climatology); `α_k ≡ 1` (**reduces to G-A**) | Makes the A-to-B continuum explicit and gives a built-in consistency check: `α ≡ 1` must reproduce G-A exactly |
| **S7** | `P_GO` / `P_OK` | 60 / 70 | 50 / 60; 70 / 80 | Directly sets `Go`/`Delay` balance and `Duration` availability |
| **S8** | `MIN_GAIN_PCTL`, `MIN_DURATION_H` | 5.0, 2 | 2.5 and 10.0; 3 and 4 | These two thresholds alone govern whether the forecast-dependent types fire |
| **S9** | `TRIP_HORIZON_H` | 9 | 6; 12 | Longer horizons need more skill, so this is where ES should degrade visibly |

**Reporting rule.** Full grid for the four GC and three ES criteria. For GE, the grid matters less — its ceiling is set by `P(S = CAUTION)`, not by the generator — so GE is reported at primary plus S4, S5 and S7 only, with the reason stated.

**Pre-registered guard against the garden of forking paths.** The grid is fixed in this document before execution. Any configuration added later is reported as **post hoc** and excluded from the headline range.

---

## 6. Revised exploratory criteria

All thresholds below are **exploratory**. Each is justified by what a study actually needs rather than by what a run happens to produce, and each is stated with its pre-registered expectation so that confirmation is distinguishable from accommodation.

### GC — generator capability (measured on C0, per condition)

| | Criterion | Exploratory threshold | Pre-registered expectation |
|---|---|---|---|
| **E-GC-1** | Each of the four advice types appears in ≥10% of episodes | ≥10% each (**original N1 threshold retained**) | **G-A fails**, `DepartureTime` at exactly 0% (§2). **G-B uncertain** — this is the open question. G-L passes |
| **E-GC-2** | **No advice type is a deterministic function of another.** Measured by conditional entropy `H(type_i │ type_j) > 0` for every ordered pair | All pairs non-zero | **G-A fails**: `Duration ≡ f(Go)` under persistence (§2). New criterion — the original gate could not have detected vacuous capability |
| **E-GC-3** | `DepartureTime` targets more than one distinct hour, and no single target hour takes >70% of them | ≤70% on the modal target | Guards against a generator that always says "go at 09:00". Not previously checked |
| **E-GC-4** | Type rates reported **separately by hour-of-window** (05–09) | Descriptive, no threshold | §1 predicts systematic variation. Reported because averaging it away would hide a real property of the information model |

### ES — evidential support (G-B primarily; G-A trivially, G-L diagnostically)

| | Criterion | Exploratory threshold | Note |
|---|---|---|---|
| **E-ES-1** | G-B's forecast skill score against persistence is **> 0** at every lead time at which a forecast-dependent type is emitted | Skill > 0 at those leads | If G-B has no skill at lead 3 h but issues `DepartureTime` for a 3 h-ahead slot, that advice is capability without support |
| **E-ES-2** | Share of `DepartureTime` and `Duration` advice emitted at leads where skill > 0 | ≥80% | The headline ES number |
| **E-ES-3** | Reliability of "predicted acceptable" hours — of hours forecast acceptable, the share that were acceptable — reported as a reliability diagram per lead | Descriptive | Evaluation-side only; uses realised conditions legitimately, never fed back |
| **E-ES-4** | **G-L's measured skill must be reported alongside.** It will be near-perfect, by construction | Descriptive | This is the leak made visible in skill terms, and it is the clearest way to show a supervisor what L3 did |

### GE — governance effectiveness

| | Criterion | Exploratory treatment | Change from the original |
|---|---|---|---|
| **E-GE-1** | C1 vs C2 content divergence, reported **both** unstratified and CAUTION-stratified, **always printed next to the structural ceiling `P(S = CAUTION)`** | **Descriptive. No pass/fail on the unstratified figure** | **Corrects my own error.** The original N2 set a 20% bar on a quantity structurally capped at 5.81%. Preserved as failed; never re-posed as a gate |
| **E-GE-2** | Withheld-type realisation within CAUTION — the original N3 quantity | **≥30% as an adequacy marker, not a gate** | Justified by pool need, not by the observed 46.33%: a 40-case pilot needs ~12 differing cases, and 531 × 0.30 ≈ 159 is ample headroom. The original 50% bar is preserved as failed |
| **E-GE-3** | **Direction of divergence.** Where C1 ≠ C2, does C2's presented content correspond to more conservative advice? | ≥95% of divergences in the conservative direction | New. Verifies the filter does what it claims rather than merely differing. A divergence in the permissive direction would be a specification defect |

### CA — case availability (absolute counts, which is the unit N4 should have used)

| | Criterion | Exploratory threshold | Rationale |
|---|---|---|---|
| **E-CA-1** | Boundary cases available | ≥120 | A 40-case pilot needs ≥12 boundary cases; 120 gives 10× sampling headroom |
| **E-CA-2** | CAUTION ∩ boundary cases | ≥60 | The intersection the design actually draws from |
| **E-CA-3** | Cases where C1 ≠ C2 | ≥100 | The study's effect channel, in cases rather than percentages |

**The original N4 share-based criterion (≥30%) is preserved as failed** and is not re-posed, because `research/d4-critical-review.md` §6.4 established it was in the wrong units: at ε = 0.05 m, reaching 30% would need ε ≈ 0.25 m, which is no longer a boundary.

**No composite pass.** Output is a verdict matrix: rows GC-1…4, ES-1…4, GE-1…3, CA-1…3; columns G-L, G-A, G-B. Dimension-level verdicts only.

---

## 7. Leakage checks

Specified as executable assertions, not as review intentions. **L-CHK-1 and L-CHK-2 are hard gates: a failure aborts the run and no results are reported.**

| | Check | Mechanism | Verdict on failure |
|---|---|---|---|
| **L-CHK-1** | **Chronological truncation invariance** — the decisive test | Run the generator on the record truncated at 2022-12-31. Every episode in 2021–2022 must receive **byte-identical** advice to the full-record run | **Abort.** Any difference proves the generator read data later than the episode |
| **L-CHK-2** | **Temporal access audit** | Instrument every read of the record so each access is logged with its timestamp; assert `max(accessed_timestamp) ≤ episode_timestamp` per episode, for generation code paths only | **Abort.** Names the offending line directly |
| **L-CHK-3** | **Future-shuffle invariance** | Randomly permute all record hours strictly after the evaluation period, re-run, compare outputs. Repeat with 5 seeds | Fail ⇒ leakage in calibration |
| **L-CHK-4** | **Placebo-future test** | Replace all post-episode values with `NaN`, re-run. The generator must produce identical advice and must not raise | Fail ⇒ the generator was reading forward values |
| **L-CHK-5** | **Calibration provenance audit** | Every calibration constant carries the dated subset it was computed from; assert each subset's maximum timestamp precedes the episode it is applied to | Fail ⇒ L1/L2-class leak |
| **L-CHK-6** | **Skill ceiling sanity bound** | G-B's measured skill must not exceed a plausible operational-forecast skill at the same lead. Damped persistence beating a real NWP forecast at 6 h would be impossible | Fail ⇒ investigate before reporting anything |
| **L-CHK-7** | **`α ≡ 1` identity check** | S6's `α_k ≡ 1` variant must reproduce G-A **exactly** | Fail ⇒ an implementation error in the surrogate |
| **L-CHK-8** | **Evaluator/generator boundary audit** | Static check that post-episode data enters only skill-scoring, `S` computation and outcome scoring, and never the advice path | Fail ⇒ the §1 declared boundary has been crossed |

**On the one place future data is permitted.** L-CHK-8 is the check that keeps §1's concession narrow. Skill measurement, state classification and outcome scoring are evaluation functions; they may see everything. The advice path may see nothing after the episode. Keeping these in separate modules with no shared mutable state is a design requirement, not a style preference.

---

## 8. Validation checks — does the replication reproduce what is already known?

| | Check | Expected | What a failure would mean |
|---|---|---|---|
| **V-1** | Re-derived `S` reproduces canonical figures on the evaluation window | `P(S = CAUTION)` and the UNSAFE share consistent with the published 5.81% and 42.88% **after allowing for the shortened window** | The read-only classifier reproduction is wrong, invalidating everything downstream |
| **V-2** | **G-A's advice-type profile should resemble the prototype's.** G-A is concurrent-information-only, which is the prototype's input situation | G-A yields `Go`/`Delay` and no `DepartureTime`; the prototype yields `Delay` only. **The residual difference should be fully explained by `R-SAFE-001` being `DEFERRED`** | If G-A produces types the prototype cannot, the §2 analysis of *why* the prototype is degenerate is incomplete |
| **V-3** | G-L on the 7,305-episode window should be close to, but not identical to, the published 9,135-episode figures | Small shifts attributable to the window | A large shift means the original figures were sensitive to the 2020 data in a way not yet understood |
| **V-4** | S6's `α ≡ 1` reproduces G-A, and `α ≡ 0` produces pure climatological advice | Exact and sensible respectively | Implementation error |

**V-2 is the scientifically interesting one.** It turns the prototype's degeneracy from an observation into a prediction that is tested, and it links the gate to the fidelity census through an independent route.

---

## 9. Preservation ledger

| Item | Where it lives | Status |
|---|---|---|
| N1–N4 criteria and thresholds as pre-registered | `research/d4-reference-validity-and-non-degeneracy.md` §6.1, `non_degeneracy_gate.py` PRE-REGISTERED block | **Unaltered. The confirmatory record** |
| N1–N4 results of 17 Nov 2026 — N1 pass; N2 2.69% / 46.33%; N3 46.33%; N4 6.17%; `GATE_PASS: false` | same, and `research/non-degeneracy/n1-n4-results.json` | **Unaltered.** Restated in this document, never revised |
| The 9,135-episode case table | `research/non-degeneracy/n1-n4-case-table.csv` | **Unaltered.** The replication writes new files under new names |
| The original leaky generator | `research/non-degeneracy/non_degeneracy_gate.py` | **Unaltered.** Re-used as condition G-L; any de-leaked generator is a **new file** |
| Original Stage A / Stage B | D-4 report §7 | Unaltered; superseded in use by A1/A2/A3 |
| K1–K4 constructs and the 5-point severity scale | decision package §4 | Unaltered; superseded in use by the appropriateness rubric |
| `GATE_PASS_as_preregistered` as a composite verdict | `n1-n4-results.json` | **Retired for future use** (§4). The recorded value stands |

**Reporting rule for the write-up.** Original and revised criteria are published **side by side**, with the reasons for each revision. `research/d4-critical-review.md` §2 already states why: *"pre-registered criteria failed, then were respecified"* is the pattern a reviewer distrusts, and the defence against that suspicion is disclosure, not tidiness.

---

## 10. Pre-registered predictions

Written before execution so that the run can confirm or refute rather than be interpreted after the fact.

1. **G-A fails E-GC-1 with `DepartureTime` at exactly 0%.** Structural, not probabilistic (§2).
2. **G-A fails E-GC-2**, because `Duration` is a deterministic function of `Go` under persistence.
3. **G-B's `DepartureTime` and `Duration` rates fall substantially below G-L's 36.12% and 72.56%.** The size of the drop is the leak's magnitude in capability terms, and it is currently unknown.
4. **G-B's skill will be positive at short leads and decay toward zero by the 9 h horizon**, so E-ES-2 is the criterion most likely to bind — and **S9's 12 h variant should fail it more clearly than the 6 h variant**.
5. **GE is essentially unchanged across G-L, G-A and G-B at the unstratified level**, because its ceiling is `P(S = CAUTION)`, a property of the classifier and the record, not of the generator. The CAUTION-stratified figure will move with the generator.
6. **E-GE-3 passes at or near 100%**, since `A_AI` is nested by construction. A failure would indicate a specification defect, which is why the check is worth its cost despite the expected result.
7. **Whether G-B passes E-GC-1 is genuinely open.** It is the question this replication exists to answer, and I am not predicting it.

**If G-B fails E-GC-1**, the conclusion is not that the study is impossible but that **it requires real forecast data** — which reinstates the issue-time archives audited in `research/next-research-decision-package.md` §3 and makes decision D-5 a precondition rather than a parallel strand.

---

## 11. What this specification cannot establish

1. **Nothing has been run.** Every expectation in §10 is an argument, not a result.
2. **It cannot create a safety reference.** The reference route is closed (`research/d4-critical-review.md` §1). This specification is about whether a *stimulus pool* can be built honestly; what the pool is scored against remains the appropriateness rubric, with the ceiling stated there.
3. **G-B is one surrogate among many.** A fitted lead-time regression or a real NWP archive would have more skill. G-B is the cheapest construction with non-trivial skill, chosen because it nests the null.
4. **Even a clean G-B leaves single-site, single-generator limits.** N1-style results are properties of this generator at this site, not of advisory systems generally.
5. **The warm-up cost is real and unavoidable.** 1,830 episodes — 20% of the record — are spent on calibration, and S2's 730-day variant spends 40%.
6. **The §3 climatology-quality confound is mitigated, not eliminated.** Reporting by year and running the frozen variant bound it; neither removes it.
7. **RESOLUTION (MFWAM) is out of scope here.** All of this is PRIMARY only, and whether conclusions carry across configurations is untested.
8. **ES measures forecast skill, not advice quality.** A perfectly skilful forecast can still underwrite bad advice if the advice rules are wrong, and these rules were written for a stimulus generator, not for deployment.

---

## 12. Execution plan and the decisions that gate it

**Nothing below has been done.**

| Step | Needs | Output |
|---|---|---|
| **1** | Authorization to write a new generator module (new files only; G-L untouched) | `research/non-degeneracy/causal/` with separate `generate/` and `evaluate/` paths per L-CHK-8 |
| **2** | — | L-CHK-1…8 implemented and passing **before** any criterion is computed. A leak check that is written after the results is not a check |
| **3** | — | V-1…V-4 validation run |
| **4** | — | Primary run: G-L, G-A, G-B on the 7,305-episode window; verdict matrix |
| **5** | — | Sensitivity grid S1–S9; criteria reported as ranges |
| **6** | — | Report with original and revised criteria side by side per §9 |

| | Decision | Who | Recommendation |
|---|---|---|---|
| **D-3‴** | Authorize steps 1–6. New files only; no canonical artefact touched; no participants | Author | **Proceed.** This is the cheapest step that can resolve whether the advisory comparison is feasible at all, and it is the one the current N1 pass cannot substitute for |
| **D-5″** | Accept that **if G-B fails E-GC-1, real issue-time forecast data becomes a precondition**, not a parallel strand | Supervisor | **Accept in advance.** Deciding this before the result removes the temptation to reinterpret a failure as a pass |
| **D-4g** | Whether E-GE-3's conservative-direction check should also be applied to the existing published Δ_L2 result | Supervisor | **Worth one look.** It is cheap, and it is better found by the author than by an examiner |

**What I would do first.** Step 2 before step 4 — implement and pass the leak checks before computing a single criterion. The failure mode this whole document exists to prevent is a number that looks respectable and was produced by a generator that knew the answer.
