# G4 — Final Prior-Art Closure

**Prepared:** 17 November 2026 · **Author:** Claude (Cowork session) · **Status:** exploratory research branch, v3 (closure). All v1 and v2 documents preserved unedited. **Frozen thesis RQ1–RQ3 and all canonical artefacts untouched. No algorithm implemented, no experiment run, no restricted data obtained.**

**Evidence labels, used throughout.** **[V]** verified from a primary source this session, with reading depth stated · **[F]** formal argument, mine, from verified premises · **[A]** assumption required for a conclusion to hold · **[U]** untested interpretation.

---

## Decision

# NO-GO confirmed

**No defensible distinct methodological problem was identified.** Evidential adequacy's full structure — per-type risk levels, a declared procedure class, an existential over that class, and withholding when nothing in the class can be certified — is **stated in Learn-then-Test, Remark 1**. The existential quantifier is thresholded realizability. And the one piece of genuine white space found during this closure is **not G4**; claiming it would be the terminology-change rescue this task forbade, and it has no evaluable benchmark in any case.

Two of my own v2 claims are **withdrawn as wrong** (§5).

---

## 1. Evidential adequacy — three concepts, and an asymmetry that settles the matter

### 1.1 The distinction

| | Concept | Formal statement | Estimable? |
|---|---|---|---|
| **(i)** | **Average predictive validity** | `PV(g; t, E) = −𝔼[L_t(g_t(E), Y)]`, or selective risk `R(f,g) = 𝔼[ℓ·g]/𝔼[g]` | **Yes.** Standard holdout estimation; the quantity selective prediction has measured since El-Yaniv & Wiener (JMLR 11:1605–1641, 2010) **[V, full text]** |
| **(ii)** | **Instance-level adequacy** | For *this* `x`: is the evidence adequate? A conditional statement, `𝔼[L_t ∣ X = x] ≤ 1 − τ_t` | **No, not distribution-free.** Exact conditional validity is unattainable without distributional assumptions; the achievable relaxation is group- or taxonomy-conditional (Mondrian-style). **[F]**, resting on the known impossibility results for distribution-free conditional predictive inference — **I did not re-verify those theorems this session, so treat the citation as owed** |
| **(iii)** | **Existence of a suitable procedure** | `∃g ∈ G : PV(g; t, E) ≥ τ_t`, equivalently `inf_{g∈G} R(g; t, E) ≤ 1 − τ_t` | **Asymmetric — see §1.2.** This is the crux |

### 1.2 The asymmetry, which is the single most useful finding in this closure

**Existence is certifiable. Non-existence is not.** **[V]**

- **Existence:** finite-sample distribution-free certification exists. Learn-then-Test (arXiv:2110.01052v4) Definition 1 gives `P(R(T_λ̂) ≤ α) ≥ 1 − δ`; Theorem 1 gives FWER-controlled selection with `P(sup_{λ∈Λ̂} R(λ) ≤ α) ≥ 1 − δ`, "where the supremum over an empty set is defined as −∞". **[V, full text]**
- **Non-existence** is a statement about a supremum over `G`, so it needs an *upper* bound on `sup_{g∈G} PV`. That requires either **(a)** a one-sided uniform bound under a capacity assumption — Bartlett & Mendelson (JMLR 3:463–482, 2002) Theorem 8 is the template, with the complexity term failing to vanish for unconstrained `G` **[V, full text]**; or **(b)** an in-model minimax lower bound, which transfers only through the model assumption. **[A]**

**What the prior art actually delivers, and already says so honestly.** Learn-then-Test's **Remark 1 is titled "Not all risks can be controlled at any requested level"** and reads: *"we may abstain from returning a function T if no risk-controlling function can be **certifiably** found."* **[V, verbatim]** Rava & Gang (arXiv:2610.04233, 2026 preprint) likewise *"returns ĥ ≡ 0 if A_G is empty"*. **[V, full text]**

**[F]** So the strongest claim any adequacy system can make at deployment is *"no permissible procedure could be **certified** adequate on this evidence"* — a property of the certification procedure and the declared class, **not a fact about the world**. **This is already stated in the prior art.** Framing G4 as closing that gap would be a false claim; framing it as *noticing* the gap is not a contribution, because Remark 1 noticed it first.

---

## 2. Value of information — my v2 claim was wrong, and the correction does not help G4

### 2.1 EA is **not** the acquire-or-decide stopping condition **[V]**

v2 asserted that adequacy is "probably a restatement of the acquire-or-decide stopping condition". **That is wrong and is withdrawn.**

The stopping rules, as the primary sources state them **[V, full text of ISPOR Reports 1 and 2]**:

> *"A population EV(P)PI that is less than the estimated costs of any research study is a sufficient condition for establishing that research is not of value."* (Rothery et al. 2020, *Value in Health* 23(3):277–286)
> *"Where the expected costs of research exceed the EVPI then research is not worthwhile and the VOI process should stop."* (Fenwick et al. 2020, Recommendation 5)

In active feature acquisition the analogue is myopic: *"if Δ_k(x_S, a\*) ≤ 0 we stop the acquisition process"* (Aronsson et al., arXiv:2502.11067, 2025 preprint) **[V, full text]**; and in Bilgic & Getoor (*JAIR* 41:69–95, 2011), acquisition *"stops … when there are no more features with a positive benefit value"*, after which *"we need to make a classification decision"* **[V, full text]**.

**Three findings establish the distinctness:**

1. **Classical VOI has no withhold-output action. [V]** The decision space is *"a set of mutually exclusive decision options, indexed d in the decision space D"*, and the rule is unconditional expected-utility maximisation over it. "Abstain", "withhold" and "reject" appear in none of the VOI sources read. Where *"reject"* appears in the acquisition literature it means acquire more, not withhold — Clertant et al. (AISTATS 2019): *"Abstention in the sense of 'reject' corresponds to the acquisition branch."* **[V]**
2. **The unacquirable-evidence counterexample is sound, and the literature is silent. [V]** With the acquisition set empty or unboundedly costly, every stopping rule fires trivially and returns a substantive action **however poor the evidence** — the predicate is a function of *(belief, candidate experiment, cost)*, never of evidence adequacy. None of the four VOI sources addresses the case. The nearest adjacent construct, Claxton et al.'s Approve / AWR / OIR / Reject algorithm (*Value in Health* 19(6):885–891, 2016), is substantive coverage guidance motivated by *"costs which once committed cannot be recovered"* — not evidential inadequacy — and states **no formal rule**. **[V, full text]**
3. **[F]** The two predicates have different type signatures: VOI-stop ranges over {acquire, decide now} at a *preposterior* node; EA ranges over {issue, withhold} at a *terminal* node. They are **logically independent in both directions**: stop-true with EA-false (counterexample 2), and stop-false with EA-true (a cheap informative test exists while some `g` already clears `τ_t`).

### 2.2 Why the correction does not rescue G4

**[F]** "Distinct from VOI" is not "novel". The correction relocates EA's prior art rather than removing it: EA is not a VOI object, it is a **selective-risk-control** object, and in that literature it is largely present already (§3.1). The positioning against VOI is *correct*; the prior art is simply in a different field.

---

## 3. Prior-art completeness

### 3.1 Learn-then-Test and Rava & Gang — EA's structure, stated **[V]**

| EA component | Prior art |
|---|---|
| Type-specific thresholds | LTT §2.4: *"control m risks R₁,…,R_m at levels α₁,…,α_m"* **[V, verbatim]**. Also Sadinle, Lei & Wasserman (*JASA* 114(525):223–234, 2019): per-class levels `α_y` with an explicit **null region** `N = {x : H(x) = ∅}`, where `H_t(x) = ∅` iff `p(y∣x) < t_y` **for all y** — a per-point instance of universally-quantified failure **[V, full text]** |
| A declared procedure class | LTT's search space `Λ` ↔ `G` **[V]** |
| The existential `∃g ∈ G` | `Λ̂ ≠ ∅` **[V]** |
| Withhold on non-existence | LTT Remark 1 **[V, verbatim]**; Rava & Gang's `ĥ ≡ 0` on empty feasible set, with Remark 3.5 exhibiting a case where *"no rule with positive coverage satisfies both constraints strictly"* **[V, full text]** |
| Selective error conditioned on issuing | Rava & Gang's `R₁, R₂` are selective class-wise errors; abstention is the minimised slack **[V]** |

LTT also already covers the application: its §4 treats *"classification with a reject option or classification with abstention"*, with the empty set encoding abstention. **[V]**

**[F] EA is per-type selective risk control.** The one conjunction not located in a single source is **per-type thresholds *derived from error consequence* together with existential-over-`G` withholding**. Consequence-derived thresholds are the classical cost-sensitive move — Mozannar & Sontag's Bayes rejector sets the threshold at indifference against the expert's error **[V, full text]**; Bilgic & Getoor use a cost matrix `c_ij`. **[U]** So the residual is a composition of two standard moves, not a new primitive — and composition is explicitly not novelty under this task's own rule.

**Also already fused, and closer than anything in v1 or v2:** ActiveEvidence (arXiv:2610.20532, Oct 2026 preprint) has a terminal `ABSTAIN` state emitted *"for missing, conflicting, stale, or out-of-root evidence"*, an acquisition-gap certificate, and states *"the decision problem itself connects to value-of-information analysis"*. It declares its own limit — *"The certificate is model-relative"* — which is the §1.2 asymmetry again. **[V, full text]**

### 3.2 The existential is realizability **[V/F]**

`∃g ∈ G : PV ≥ τ_t ⟺ inf_{g∈G} R(g) ≤ 1 − τ_t` **[F]**, which is the agnostic-PAC benchmark term — Shalev-Shwartz & Ben-David Definition 3.3 returns `h` with *"LD(h) ≤ min_{h'∈H} LD(h') + ε"* **[V, verbatim]** — i.e. a τ-relaxation of realizability (their Definition 2.1). Conditioning on `E` changes the index set, not the structure. **[F]** There is no established name in the acquisition literature; the name with precedent is **"feasibility"**, from ease.ml/snoopy (arXiv:2010.08410), which poses it almost verbatim: *"Is my current data artefact D clean/good enough for some ML models to reach a target accuracy α_target?"* **[V, full text]**

### 3.3 AC-RAC — verified in paper **and** source code **[V]**

**Correcting v2.** v2 said AC-RAC "already has the type-specific-threshold component". **Imprecise, and now corrected.** AC-RAC has per-action *thresholds*; it does **not** have per-action *risk levels*.

- **α is a single shared scalar.** The constraint is `ℙ(u(a(X),Y) ≥ ν(X) ∣ a(X) = a) ≥ 1 − α` **for all a** — α carries no subscript anywhere. The subgradient is `g_a = q_a(p_a − (1−α))`. The released code confirms it first-hand: `one_minus_alpha = 1.0 - alpha` is a scalar broadcast across a length-`|A|` `lambdas` vector; the result CSVs carry a **single `alpha` column**. **[V, first-hand code and artifact read]**
- **λ_a is an endogenous dual variable fitted to equalise coverage at one exogenous α** — not an exogenous, consequence-indexed level. The paper never raises per-action levels; searches for "severity", "consequence", "cost of error", "user-specified" returned nothing relevant. **[V]**
- **[U]** Substituting a vector `(α_a)` is a one-line edit, since the subgradient is already coordinatewise. **[A]** But whether Theorem 4.3's finite-sample bound survives it is **unverified** — Appendix C.3.2 could not be read, and the `|A|/((n+1)ℙ(a_RA=a))` term would need rederivation. **This is the obvious examiner challenge to any claim built on per-action levels.**
- **AC-RAC represents no input-evidence properties.** No missingness, no timestamps, no source conflict, no reliability — verified in code: every entry point takes only a dense `probs` array. **[V]**
- **Verified degradation worth recording.** At `|A| = 10`, worst-case action-conditional coverage falls to **0.8276** (worst-action miscoverage 0.1724 against a nominal 0.05 — a ~3.4× overshoot) while **overall** miscoverage *improves* across `|A|` ∈ {4,6,8,10} (0.0543 → 0.0324 → 0.0191 → 0.0328). **The marginal guarantee masks per-action failure inside AC-RAC itself at larger action spaces.** Rare-action: target coverage flat at 0.927–0.934 as prevalence falls ~53× to 0.0997%. **[V, read first-hand from the authors' released CSVs and figure PDFs, not from the appendix prose, which could not be read via seven routes]**

### 3.4 Gorostiaga & Sánchez — venue now established **[V]**

**Citation resolved:** NFM 2022, *LNCS* 13260:693–712, Springer, DOI 10.1007/978-3-031-06773-0_37; refereed LNCS symposium (47-member PC). **[V]** v2 recorded the venue as unknown; that is now closed.

- Finite dismissibility and admissibility are **unnumbered paragraphs in §3** — *"We say a value v ∈ D is Finitely Dismissible for a formula ϕ and a behavior s ∈ I^ω if there is an observation ls ∈ I\*, ls ≺ s such that for all s′ continuation of ls, ⟦ϕ⟧(s′) ≠ v."* **[V, verbatim]** Do not cite as "Definition 3.1".
- **Purely logical, two-valued.** No degrees, confidences, weights or probabilities over verdicts. The quantitative content is in the verdict *domain* (QLTL, DiscLTL assign values in [0,1]); the predicate "is this value dismissed after some finite prefix?" stays all-or-nothing. **[V]**
- **Per-value requirements differ, and this is the paper's core move** — Lemmas 3, 5, 7 each exhibit a value dismissible while another is not admissible. **[V]** So the per-output-value version of reachability is **established prior art**, more so than v2 allowed.
- **Evidence absence only, not quality.** Missing prefixes and unobservable events are modelled; **no staleness, no source conflict, no reliability**. The phrase *"loss or corruption of events"* appears informally with no observation function given — worth quoting in related work rather than letting an examiner find it. **[V]**
- **Unread successor:** "General monitorability of totally ordered verdict domains", *Innovations in Systems and Software Engineering*, DOI 10.1007/s11334-024-00557-2. Extends the same framework. **Not read.**

### 3.5 The one capability established methods cannot represent — and why it is not G4

**[V]** AC-RAC has **no notion of an action being unavailable or non-derivable from a given input, as distinct from being unsafe.** The action set is fixed and fully available for every input; verified first-hand in `conformal.py`, where `select_action_max_min` scores every action in `actions` on every call, with no availability predicate, feasibility mask or x-indexed action set. An action is only ever *not chosen* because its worst-case utility is lower. The subagent that read the code called this clean white space, and on the evidence it is.

**[F] But this is a different problem from G4, and three things stop it being a rescue:**

1. **It is not evidential adequacy.** It is input-dependent action *availability* — a question about the action set's domain, not about whether evidence warrants a recommendation. Relabelling G4 as this would be exactly the terminology-change rescue this task forbids.
2. **[A]** Its technical content, if any, is that input-dependent availability interacts badly with action-conditional calibration: the calibration subset for action `a` shrinks to cases where `a` was both available and selected, and AC-RAC's `|A|/((n+1)ℙ(a_RA=a))` term degrades accordingly. **This is an inference, not a verified result**, and §3.3's measured `|A|`-scaling degradation is adjacent but not the same phenomenon — there the action was always available, merely rarely selected.
3. **An unread paper may already close it.** *Macro Mondrian Conformal Risk Control* (arXiv:2610.35035) concerns group-specific conformal risk levels and was **rate-limited on five attempts, unread**. Mondrian conditioning on an availability pattern is the obvious existing instrument.

**So it is recorded as a possible future problem, explicitly not claimed as established, and it is not G4.**

---

## 4. Evaluation feasibility — MIMIC-IV assessed, and it does not qualify

### 4.1 Do MIMIC's prediction types represent distinct recommendation categories? **No. [F]**

v2 named mortality, length-of-stay, decompensation and phenotype as "semantically distinct output types". **They are distinct prediction *targets*, not distinct *recommendation categories*.** They differ in what fact is predicted, not in what action is advised. The structure G4 needs — output types that differ in *what they recommend*, so that each carries its own evidentiary precondition and its own consequence-derived `τ_t` — is absent. **This alone disqualifies the setting.**

### 4.2 Decision-time availability, verified against the published schema **[V]**

**Partly verified, partly refuted.**

| Table | Column | Documentation, verbatim |
|---|---|---|
| `hosp.labevents` | `charttime` | *"usually the time at which the specimen was acquired, and is usually significantly earlier than the time at which the measurement is available"* |
| `hosp.labevents` | `storetime` | *"The time at which the measurement was made available in the laboratory system. This is when the information would have been available to care providers."* — **explicit availability semantics** ✓ |
| `icu.chartevents` | `storetime` | *"the time at which an observation was manually input or manually validated by a member of the clinical staff"* — **this is not availability.** A materially weaker proxy, and v2's claim is **refuted for this table** |

**Three documented caveats, all of which undercut naive availability reconstruction: [V]**

1. **Ordering can invert.** Core concepts: *"it's also possible that the `storetime` occurs before the `charttime`"*, with a worked GCS example. The assumption `storetime ≥ charttime` — on which availability reconstruction usually rests — is explicitly not guaranteed.
2. **Microbiology `storetime` is a last-update time:** *"the times here are the time of the last known update"*, while *"many interim results are made available during the process"*. First availability is unrecoverable.
3. **Microbiology `charttime` is nullable**, degrading pertinence to date granularity.

**And the schema carries no evidence-quality representation at all** — no staleness flag, no source-conflict field, no reliability score. A `warning` column exists in `chartevents`; the documentation page read does not define it as a reliability measure. **[V]**

### 4.3 The A/B/C/D comparison

Specified as asked, and then set aside:

| Arm | Content |
|---|---|
| **A** | Calibrated confidence only, no evidence-quality variables |
| **B** | Confidence **with** evidence-quality variables as ordinary input features, recalibrated |
| **C** | Arm A's model plus a separate type-level admissibility constraint |
| **D** | **Arm B's model plus the separate admissibility constraint** |

**[F] The decisive comparison is D versus B**, not C versus A. It asks whether the admissibility mechanism earns its existence *once the information is already in the feature vector*. If `D ≈ B`, the evidence-quality information is useful but needs no new machinery — a feature-engineering result, and the methodological claim is refuted. **[U]** My expectation is that `D ≈ B`, but that is untested.

**Why the design is not run.** §4.1 removes the setting: without distinct recommendation categories there are no type-specific `τ_t` to differentiate, so arms C and D collapse toward B by construction. No alternative benchmark was identified with distinct recommendation types *and* native evidence-quality variation *and* independent outcomes: AC-RAC's own setting has complete, reliable inputs and a fixed action set **[V]**; multi-horizon forecasting suites have one output type; RAG sufficiency sets have one answer type. **The brief forbids constructing a synthetic benchmark to make the distinction appear useful, and that is the only remaining route.**

---

## 5. Corrections to my own v2 claims

| v2 claim | Status | Basis |
|---|---|---|
| "Adequacy is probably a restatement of the acquire-or-decide stopping condition" | **WRONG — withdrawn.** The two are logically independent in both directions; classical VOI has no withhold action and the literature is silent on unacquirable evidence | **[V]** §2.1 |
| "AC-RAC already has the type-specific-threshold component" | **Imprecise — corrected.** Per-action *thresholds* `λ_a` as endogenous duals at one shared exogenous α; **no** per-action risk levels, **no** consequence derivation | **[V]** §3.3 |
| "MIMIC availability is reconstructible" | **Partly verified, partly refuted.** Explicit for `labevents.storetime`; **not availability** for `chartevents.storetime`; three documented caveats | **[V]** §4.2 |
| "Gorostiaga & Sánchez venue unknown" | **Closed.** NFM 2022, LNCS 13260:693–712, refereed | **[V]** §3.4 |
| "Reachability = realizability" | **Confirmed and strengthened.** Per-*value* reachability is also established (Lemmas 3, 5, 7) | **[V]** §3.2, §3.4 |
| NO-GO verdict | **Confirmed, on different and stronger grounds** — LTT Remark 1 rather than the VOI equivalence v2 wrongly relied on | — |

**Nothing in v1 or v2 is deleted.** Both remain readable in their own files with their original verdicts.

---

## 6. Unresolved items

| | Item | Why it matters | Status |
|---|---|---|---|
| **1** | **Macro Mondrian Conformal Risk Control** (arXiv:2610.35035) | Group-specific conformal risk levels; the obvious existing instrument for §3.5's availability question | **Rate-limited on five attempts; unread** |
| **2** | **AC-RAC Appendix C.3.2** (Theorem 4.3's proof) | Decides whether per-action `α_a` breaks the finite-sample guarantee — the one place a per-type-level claim must be defended | **Unread; seven access routes failed** |
| **3** | **Claxton (1999), "The irrelevance of inference"** | The canonical statement that evidential inadequacy is *not* a ground for withholding a decision — the most important source for §2.1's crux | **Citation record only; DOI was constructed from a PII and not confirmed. Relied on for nothing** |
| **4** | **Gorostiaga & Sánchez (2024) journal successor** (DOI 10.1007/s11334-024-00557-2) | Extends the same framework; may move §3.4's answers | **Unread** |
| **5** | **Conditional-validity impossibility theorems** | Underpins §1.1(ii) | **[F]** stated from known results; **not re-verified this session. Citation owed** |
| **6** | **Howard (1966); Raiffa & Schlaifer (1961)** | Foundational VOI | **Not read.** All VOI formulations here come from ISPOR Reports 1–2 and Ades et al. 2004 |

**None of these would convert NO-GO to GO**, because item 1 can only *close* the remaining white space and the evaluation obstacle in §4 is independent of all six.

---

## 7. What survives, and what to do

**What survives is a limitation statement for the thesis, requiring no novelty claim** — unchanged from v2 §3 and permitted by the lock:

> The admissible advisory set `A_AI(SAFE)` ranges over output types whose derivation depends on information the specified inputs do not provide. Under the procedures implemented, one type is not produced at all and another is produced as a deterministic function of the present observation. Whether either would be *warranted* is a separate question this work does not answer, since warrant requires outcome data and a consequence-grounded threshold, and the domain supplies neither.

**Three things not to say**, each because an earlier version said it and was wrong: that the unproduced type is unreachable in principle; that the deterministic type is unsupported; that any of it is novel.

**Recommendation.** Close the branch. Keep v1, v2 and this closure together as the record of a novelty claim that was tested against primary sources and withdrawn — including the two places where my own reasoning was refuted. Record §3.5's AC-RAC white space as an observation for a future reader, flagged as unevaluated and explicitly not as G4's survival.

**[F] The strongest argument for closing rather than deferring:** the obstacle is not a missing experiment. Learn-then-Test Remark 1 states EA's structure *and* its one-sided limitation, and no benchmark exists in which the proposed mechanism could be shown to matter. Both halves of a GO are absent, and neither is a reading task away.
