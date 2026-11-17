# Evaluation Feasibility — Surviving Gaps

**Prepared:** 17 November 2026 · **Author:** Claude (Cowork session) · **Status:** exploratory research branch. Frozen RQ1–RQ3 and all canonical artefacts untouched. No experiment was run and no licence was requested for this document.

**Scope.** Only the gaps that survived `candidate-research-gaps.md` are assessed: **G2-staleness** (partially supported, narrow) and **G4** (reachability versus support, supported). G1 and G3 are contradicted and are not assessed.

**A hard constraint, taken from the brief and independently confirmed in this project.** The existing ERA5 retrospective record **cannot** support claims about operational recommendations. This is not a caution — it is a measured finding: the record is reanalysis with days-to-months production latency, so **nothing in it was available at the decision instant it describes**, and the project's own availability attestation records *"C1 (chronological causality) satisfied; C2 (operational availability) NOT satisfied for any condition"*. Every protocol below is therefore designed on **public ML benchmarks**, with the fisheries record used only as an illustrative case study that claims no operational validity.

---

## 1. G4 — reachability versus support

### 1.1 Falsifiable problem statement

> For a system with a finite set of output types `T`, each type `t` requiring an evidence class `E_t` to derive, and an available evidence class `E` at decision time: **is there a decision procedure that partitions `T` into unreachable, reachable-but-unsupported, and reachable-and-supported, such that (a) it never admits an unsupported type, (b) it admits every supported type, and (c) a system using it achieves strictly better selective risk at matched coverage than an action-conditional risk-control baseline that is given the same information?**

**How it is falsified.** Clause (c) is the falsifiable one. If an admissibility policy conditioned on reachability-plus-support does **not** beat AC-RAC at matched coverage on AC-RAC's own benchmarks, the contribution claim fails — because the distinction would then be a relabelling of what confidence-based calibration already achieves. Clauses (a) and (b) are provable or refutable analytically.

**A second, independent falsification route.** If the support statistic can be shown to be a monotone function of model confidence on real data, the (i)/(ii) separation collapses into existing selective prediction and the gap closes. **This is the cheaper test and should be run first** (§1.6).

### 1.2 Independently evaluable outcome

The outcome must not be scored by the system's own criterion — that is the circularity trap this project has already been caught by once. Three candidate outcomes, in descending preference:

| | Outcome | Independent of the method? | Why |
|---|---|---|---|
| **O1** | **Selective risk at matched coverage**, against ground-truth labels in a public benchmark | **Yes** | Labels are external to both the method and the baseline. Matched coverage removes the trivial way to win |
| **O2** | **Admission of a type the evidence cannot support, measured against held-out future observations** | **Yes** | The held-out observation is external. This is the clause-(a) soundness test made empirical |
| **O3** | **Agreement with a declared reachability oracle** on synthetic tasks where the evidence class is controlled by construction | **Yes, but weaker** | The oracle is constructed, so it tests implementation correctness rather than scientific claim. Useful as a unit test, not as evidence |

**O1 is primary. O2 is the safety-relevant companion and must be reported separately from O1, never netted against it** — the two errors have different costs, and this project has already made the mistake of reporting a symmetric accuracy where asymmetric errors were the point.

### 1.3 Public datasets and benchmarks

| | Benchmark | Why it fits | Status |
|---|---|---|---|
| **B1** | **AC-RAC's own experimental setting** — code at `github.com/Telvc/AC-RAC`, with clinical actions including `Quarantine` and a binary `{No-Rec, Rec}` recommender | **The required comparison.** A contribution positioned as a refinement of AC-RAC must be evaluated where AC-RAC was | Code located; **datasets not yet identified** — Appendix D was read only in fragments. **Must be confirmed before committing** |
| **B2** | **Zaffran et al.'s missing-data conformal setting** (ICML 2023, PMLR 202) | Supplies a peer-reviewed evidence-availability structure with theorems, so reachability can be defined over missingness masks rather than invented | Paper read in full; benchmark suite not inventoried |
| **B3** | **Multi-horizon time-series forecasting benchmarks** (e.g. the standard long-horizon suites) | The only public setting that naturally has **lead-time structure**, which is what makes a type forecast-dependent. Reachability over lead time is directly expressible | Not yet selected. **Must be chosen on stated criteria, not convenience** |
| **B4** | **RAG sufficiency benchmarks** — CROWN-QA (5,000 synthetic + 1,599 real), RINSE's setting, SURE-RAG's setting | Supply graded evidence-coverage levels already labelled, so support can be tested against an external sufficiency annotation | All three are **2026 preprints**; availability and licence of their data not checked |
| **B5** | The project's fisheries record | **Illustrative case study only.** Claims no operational validity (see Scope) | In hand, with the worked instance already computed |

**A gap in this assessment.** No benchmark has been confirmed to contain **both** multiple semantically distinct output types **and** controlled evidence-class variation. B3 has lead-time structure but one output type; B4 has evidence grading but one answer type; B1 has multiple actions but complete inputs. **If no such benchmark exists, one must be constructed — and a constructed benchmark is weak evidence for a novelty claim.** This is the single largest feasibility risk and is reflected in the decision criteria.

### 1.4 Strongest baselines

| | Baseline | Why it is the strongest |
|---|---|---|
| **S1** | **AC-RAC** (Zhu et al., ICML 2026) | Peer-reviewed, four months old, per-action calibration with action-conditional coverage. **If the contribution does not beat this, there is no contribution** |
| **S2** | **A plain confidence-margin threshold at matched coverage** | Deceptively strong. The one head-to-head found in the literature is a **negative result for the candidate's side**: a conflict/sufficiency-aware rule reached 90.05% selective accuracy at 53.58% coverage against **90.36% for a plain confidence margin at matched coverage** (Pandian, Research Square rs-11110025/v1, unreviewed). **A committee will raise this, so it must be pre-empted by including S2 from the start** |
| **S3** | **Zaffran et al. CP-MDA-Exact / -Nested** | The peer-reviewed standard for evidence-availability-conditioned validity |
| **S4** | **Sadinle et al. per-class α_y** (*JASA* 2019) | The oldest per-type-requirement baseline; cheap to implement and it tests whether per-type *risk budgets* already capture what per-type *evidence requirements* are supposed to add |

**S2 and S4 are the two that can kill the contribution cheaply, so both go in the first experiment, not a later ablation.**

### 1.5 Evaluation protocol

| Step | Content |
|---|---|
| **1. Pre-registration** | Hypotheses, the support statistic's definition, the reachability predicate, matched-coverage procedure, primary outcome O1, secondary O2, and all thresholds — fixed before any run. Published alongside results whatever they show |
| **2. Evidence-class construction** | Evidence classes defined by **ablation of the input**, not by model behaviour: remove features (missingness), lag them (staleness), inject source disagreement (conflict), degrade them (reliability). Each ablation declared and reproducible |
| **3. Reachability determination** | For each output type and evidence class, determine analytically whether the type's derivation predicate is satisfiable. **This must be decidable from the specification, not estimated from data** — otherwise reachability collapses into support |
| **4. Support determination** | For each reachable type, compute residual information beyond the trivial baseline on that evidence class. **The statistic must be exactly zero under the trivial baseline by construction** (§1.7) |
| **5. Matched-coverage comparison** | O1 against S1, S2, S3, S4 at several matched coverage levels, with per-type breakdowns |
| **6. Soundness audit** | O2 reported separately per output type, never aggregated with O1 |
| **7. Sensitivity** | Over evidence-class severity, trivial-baseline choice, and the support threshold. Reported as a range, not a point |

### 1.6 Avoiding circular evaluation

Four circularity routes exist here, and three of them have already been encountered in this project.

| | Route | Guard |
|---|---|---|
| **C1** | **The reference is derived from the method's own thresholds.** The method says "unsupported", and "unsupported" is defined by the method | Outcomes O1 and O2 are scored against **external labels or held-out observations only**. The method's own support statistic may never appear in the outcome |
| **C2** | **The trivial baseline is chosen to make the support statistic look informative** | The trivial baseline is **fixed in pre-registration** and must be the *weakest defensible* predictor on that evidence class — persistence for a time series, the marginal for a classifier. Chosen before, not after |
| **C3** | **Reachability is inferred from observed rates.** If a type is produced 0% of the time and that is *called* unreachability, the claim is circular | Reachability must be **established analytically from the derivation predicate**, with the observed rate used only as a consistency check. The worked instance satisfies this: `DepartureTime`'s 0.00% is *predicted* from the predicate before it is measured |
| **C4** | **The benchmark is constructed so that the distinction exists** | If B1–B4 cannot supply a suitable setting and one is constructed, the construction must be published, its labels must come from an independent process, and the result must be presented as **existence-of-mechanism, not effect size** |

### 1.7 A property that makes the design testable

The support statistic must be **exactly zero under the trivial baseline by construction**, not merely small. This is a design rule learned the hard way in this project: an earlier version of the same test used within-bin variance and was defeated by bin width, because a bin straddling the threshold produced non-zero variance from the bin's own geometry rather than from information. The corrected form uses an **episode-specific margin**, under which the residual is exactly 0.000000 and the baseline R² exactly 1.000000.

**A criterion that can return a non-zero value for structural reasons is not a test.** Any support statistic proposed must be shown analytically to be identically zero on a deterministic function of the available evidence.

### 1.8 Expected limitations

1. **The contribution may be a refinement, not a new object.** G4 survives, but AC-RAC's per-action machinery is close, and a reviewer may reasonably read reachability-versus-support as a special case of utility elimination under a degenerate prediction set.
2. **No confirmed benchmark with both properties** (§1.3). The largest risk.
3. **S2 has already beaten a sufficiency-aware rule once** in the one head-to-head found, albeit in an unreviewed preprint on one dataset.
4. **Monitorability is a strong antecedent for reachability** and the project has already conceded Bauer et al. 2011, so the claim must rest on support and the separation, which is the narrower half.
5. **Three of the four RAG sufficiency benchmarks are 2026 preprints** whose data availability, licensing and durability are unchecked.
6. **No guarantee has been identified yet.** Soundness and maximality of the admissibility partition are plausible targets, but neither has been formulated, let alone proved. **Until one exists this is an empirical paper, not a methodological one.**

---

## 2. G2-staleness

### 2.1 Falsifiable problem statement

> **Does conditioning output admissibility on measured data recency produce lower selective risk at matched coverage than conditioning on model confidence alone, on a benchmark where staleness is controlled by construction?**

### 2.2 Feasibility, honestly

| Dimension | Assessment |
|---|---|
| **Outcome** | O1 and O2 as above, with staleness as the controlled evidence axis |
| **Benchmarks** | **Constructible rather than available.** Staleness can be injected into any temporal benchmark by lagging features — which is cheap and controlled, but **it is a synthetic manipulation, and synthetic degradation is weak evidence** for a novelty claim. No public benchmark was found whose native task is staleness-conditioned admissibility |
| **Baseline** | S2 (confidence margin) and #18 Shraga et al.'s validity-horizon approach, the only existing staleness-conditioned method found — a preprint with no guarantee |
| **Circularity** | **The main risk is C2**: injected staleness makes the stale features uninformative *by construction*, so a staleness-conditioned rule wins trivially. The guard is to inject staleness **without** removing information — lag the feature while preserving its marginal distribution, so a confidence-based method retains access to a genuinely predictive but outdated signal |
| **Expected contribution** | **Low on its own.** Staleness is one axis among five; a method that handles only staleness is an increment on #3 and #18 rather than a contribution |

### 2.3 Verdict on G2-staleness as a standalone branch

**Not viable alone.** It has no native benchmark, its evaluation is synthetic, and its novelty is one axis of an occupied framework. It is worth carrying **only as a component of G4** — as one evidence class among several over which reachability and support are evaluated — where it adds breadth without bearing the novelty claim.

---

## 3. The minimum experiment capable of falsifying the contribution claim

Specified now, unexecuted, so that the claim is falsifiable before any method is built.

| | Step | Decides |
|---|---|---|
| **M1** | **Compute the support statistic and model confidence on the same public benchmark, and test whether they are monotonically related.** No method required; existing baselines only | **If they are monotone, G4 collapses into selective prediction and the branch ends.** This is the cheapest decisive test and it comes first |
| **M2** | Verify analytically that the support statistic is identically zero on a deterministic function of the evidence class (§1.7) | Whether the criterion is a test at all |
| **M3** | On one benchmark with ≥3 output types and ≥2 evidence classes, compare the admissibility partition against **S1, S2 and S4 at matched coverage**, reporting O1 and O2 separately | Whether the distinction changes outcomes |
| **M4** | Report the per-type breakdown and the soundness audit | Whether any gain is concentrated in types where the distinction is supposed to act |

**Pre-registered failure conditions.** M1 showing monotonicity ⇒ **stop**. M2 failing ⇒ **stop and re-specify**. M3 failing to beat S2 at matched coverage ⇒ **the contribution claim is refuted**, and that result is published as a negative.

**M1 and M2 require no new method, no licence, no participants and no external request.** They are the entry criteria for the whole branch.
