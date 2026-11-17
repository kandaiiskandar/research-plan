# G4 — Minimum Evaluation Design (K1/K2 Replaced)

**Prepared:** 17 November 2026 · **Author:** Claude (Cowork session) · **Status:** exploratory research branch, v2. v1 preserved unedited. Frozen RQ1–RQ3 untouched. **Nothing was executed and no data request was made.**

---

## 1. Why v1's K1 and K2 were invalid tests

**v1's K1:** compute the support statistic and model confidence on one benchmark; **if monotone ⇒ NO-GO**.

**Both directions of that inference are wrong.**

| | v1's inference | Why it fails |
|---|---|---|
| **Monotone ⇒ redundant** | Invalid | A monotone map can be non-injective and lose information; monotone-in-aggregate is compatible with large conditional variance; and a statistic monotone overall can be decision-relevant in a subpopulation. Monotonicity does not establish that one quantity can replace the other **in a decision** |
| **Non-monotone ⇒ novel or useful** | Invalid | Two quantities can be unrelated and both useless. Non-monotonicity establishes only statistical distinctness, which is not usefulness and certainly not novelty |

**v1's K2** — verify the support statistic is identically zero on a deterministic function of the evidence class — tested the wrong quantity. `g4-formal-definition-review.md` §3 shows that **II = 0 is compatible with high predictive validity and with adequacy**, so a criterion built to detect II = 0 cleanly is cleanly detecting something irrelevant.

**Both are withdrawn and replaced by §2.**

---

## 2. The replacement test: controlled incremental value over calibrated confidence

The question that matters is not whether evidence properties are *statistically distinct* from confidence. It is whether they **add decision-relevant information beyond a properly calibrated confidence model that has been given a fair chance to use them.**

That requires **three arms**, and the third comparison is the one v1 omitted entirely.

| Arm | Specification | What it isolates |
|---|---|---|
| **A — confidence only** | A calibrated selective predictor using the task features, **without** evidence-quality variables. Calibration verified (reliability diagram, calibration error reported) | The conventional baseline |
| **B — confidence with evidence features** | The same model, with evidence-quality variables (missingness mask, value age, source disagreement, reliability indicators) **supplied as ordinary input features**, recalibrated | Whether the evidence information is useful **at all** |
| **C — evidence as an admissibility constraint** | Arm A's confidence model, plus evidence properties entering as a **separate type-level admissibility condition** rather than as features | Whether the information needs **new machinery**, or merely needs to be in the feature vector |

### 2.1 The decisive comparison is B versus C, not A versus C

- **A vs B** answers: *do measured evidence properties carry useful information?* If B ≈ A, the evidence properties are uninformative here and the branch has nothing to work with.
- **B vs C** answers: *does the admissibility mechanism earn its existence?* **If B ≈ C, then evidence-quality information is useful but requires no new mechanism — it is a feature-engineering result, and G4 as a methodological contribution is refuted.**

v1 compared only A-like against C-like, which cannot distinguish "the information helps" from "the mechanism helps". **B is the arm that makes the test decisive**, and the honest prior is that B will be hard to beat.

### 2.2 Outcome, measured externally

- **Primary:** **selective risk at matched coverage**, against the benchmark's own labelled outcomes, at several pre-registered coverage levels.
- **Secondary, reported separately and never netted:** **false-admission rate** — the rate at which a type is admitted and the outcome contradicts it — broken down **per output type**, because `τ_t` is type-specific and an aggregate hides exactly the effect claimed.
- **Neither outcome may involve the method's own statistic.** This is the circularity guard that v1's design satisfied and that must be retained.

### 2.3 Pre-registered decision rule

| | Result | Verdict |
|---|---|---|
| B ≈ A within the equivalence margin | Evidence properties uninformative on this benchmark | **NO-GO** |
| B > A **and** C ≈ B within the margin | Information useful, mechanism not needed | **NO-GO on the methodological claim.** Report as a feature-importance finding |
| B > A **and** C > B beyond the margin, with the gain concentrated in types where `τ_t` is strictest | The mechanism earns its existence | **Proceed to a guarantee formulation** |
| C > B but the gain is uniform across types | Suspect a confounded implementation rather than the claimed effect | **Investigate before reporting** |

**The equivalence margin is fixed before any run** and justified in terms of the benchmark's own label noise, not chosen to make a result significant. Confidence intervals must account for clustering in the benchmark's unit of observation (patients, episodes), not treat rows as independent — the same error flagged in the supervisor memorandum's §3 correction.

---

## 3. One concrete public benchmark

**Required:** real, publicly documented, with independently evaluable outcomes, multiple semantically distinct output types, and **native** evidence-quality variation. The brief forbids constructing a synthetic benchmark to make the distinction look useful, so injected missingness and injected lag are excluded as the primary setting.

### MIMIC-IV (and MIMIC-III), PhysioNet

**Why this one and not another.** It is the only widely used public benchmark I can name where missingness and staleness are **properties of the data-generating process rather than manipulations**: a lab is absent because a clinician did not order it, and a value is old because nobody repeated it. That is the evidence-quality structure G4 is about, arising for the reasons it arises in deployment.

| | Specification |
|---|---|
| **Output types** | Semantically distinct clinical prediction types over the same patient-hour: **in-hospital mortality**, **length-of-stay / prolonged-stay**, **decompensation within a horizon**, **phenotype classification**. These are different questions with different consequences of error, so they admit genuinely different `τ_t` — which is what Example C in the definition review requires |
| **Evidence classes** | Native and not injected: **per-variable missingness** (lab not ordered); **value age** (hours since the most recent measurement of each variable) giving staleness without manipulation; **source disagreement** (e.g. nurse-charted versus device-recorded vitals for the same quantity); **measurement reliability** (flagged or out-of-range entries) |
| **Ground truth** | Discharge disposition, timestamps and diagnosis codes — **recorded independently of any model** and of this project's criteria |
| **Baselines** | Arm A: a calibrated gradient-boosted or recurrent selective predictor on the standard benchmark feature set. Arm B: the same plus the evidence-quality variables as features. Plus **Sadinle et al. per-class α_y** as the per-type-threshold baseline, and a **confidence-margin threshold at matched coverage** — the one head-to-head found in the literature favoured the plain margin, so it must be present from the start |
| **Operational availability** | **A genuine advantage over the thesis's own data.** MIMIC records both the time a value pertains to and the time it entered the record, so what was *actually available* at a decision instant can be reconstructed. The ERA5 record cannot support this at all — its availability attestation records C2 **not satisfied**. **The exact field semantics must be confirmed against the published schema before relying on this**; I have not opened the schema in this session |

### 3.1 Limitations, stated before any use

1. **Access requires credentialing and a data use agreement.** That is an external request, which the brief excludes, so **the benchmark is identified here but not obtained.** Any work on it is gated on that approval.
2. **Missingness in EHR data is informative.** A lab is ordered *because* the clinician was worried. So missingness correlates with the outcome, and an apparent benefit from evidence-quality features may be the model learning clinician behaviour rather than evidence sufficiency. **This is the central confound** and it must be addressed explicitly — at minimum by reporting whether the gain survives conditioning on ordering patterns.
3. **`τ_t` cannot be derived from consequence within MIMIC.** The data contain outcomes, not utilities. `τ_t` would have to be stipulated and declared as stipulated — which weakens the adequacy claim, since the type-specific threshold is where the recommendation-specificity lives.
4. **Retrospective and single-health-system.** No deployment claim follows.
5. **Heavy prior use.** The benchmark is well-trodden, so an improvement must clear strong published baselines, and a small gain will be attributed to tuning.

### 3.2 Benchmarks considered and rejected

| | Rejected because |
|---|---|
| Multi-horizon forecasting suites | Lead-time structure but **one output type**; evidence classes would have to be injected |
| RAG sufficiency sets (CROWN-QA, RINSE, SURE-RAG settings) | Graded evidence coverage but **one answer type**, and all three are 2026 preprints of unverified data availability |
| AC-RAC's own setting | **Must still be used for the head-to-head**, but its inputs are complete, so it carries no evidence-quality variation and cannot test the adequacy claim |
| A purpose-built synthetic benchmark | **Excluded by the brief, and rightly** — a benchmark constructed to exhibit the distinction is not evidence that the distinction matters |

---

## 4. The minimum design, in order

| | Step | Needs | Can it end the branch? |
|---|---|---|---|
| **M0** | **Read the VOI / active-feature-acquisition literature** (`g4-prior-art-challenge.md` R1) and AC-RAC's Appendix D (R3) | Nothing external | **Yes — and it comes first.** If adequacy is the acquire-or-decide stopping condition, no experiment is worth running |
| **M1** | Formalise `τ_t` grounding, or declare it stipulated | Nothing | Yes, if no grounding is defensible |
| **M2** | Obtain MIMIC access | **A data use agreement — outside this brief's authorization** | Procedural |
| **M3** | Build arms A, B, C; verify calibration of A and B before comparing | — | — |
| **M4** | Run the A/B/C comparison at matched coverage, with clustered intervals and per-type breakdowns | — | **Yes — B ≈ C refutes the methodological claim** |
| **M5** | Head-to-head against AC-RAC on its own setting | — | Yes |

**M0 precedes everything.** v1 placed a cheap experiment first; the corrected order places a cheap *reading* first, because the experiment is only worth running if the concept survives the literature.
