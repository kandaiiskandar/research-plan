# PhD Proposal Defence Readiness Package

**Prepared:** 17 November 2026 · **Author of this document:** Claude (Cowork session) · **Status:** critical review, not an endorsement

**Sources read in full:** [`research/next-research-plan.md`](next-research-plan.md) (GPT §1–5, §7; Claude §6, §8) and [`papers/consolidated-literature-review-gap-matrix.md`](../papers/consolidated-literature-review-gap-matrix.md) (GPT Matrices A–F; Claude Matrices G–H), including every verification record, correction and contributor note. Both are preserved unchanged; nothing in them is overwritten by this document.

**Primary evidence base:** nine of the eleven named competitor papers were read in full text from the publisher PDFs held in `papers/` and `papers/sources/`. Two — CAP (Tayebati et al.) and Miller's *Adaptive Human Oversight* — are **not held** and are marked as such throughout. No Scopus AI summary is treated as primary evidence anywhere in this package.

**Evidence conventions.** **[VERIFIED]** = read from a primary source or executed against the repository on 17 Nov 2026. **[DOCUMENTED]** = a repository file asserts it. **[PROPOSED]** = a plan, not an artefact. **[NOT FOUND]** = does not exist in this repository. **[UNRESOLVED]** = a live contradiction between sources, reported rather than settled. No planned experiment is reported as a result anywhere below.

---

## 1. Executive Summary

**The citation layer is now sound. The contribution layer is narrower than the plan implies. And the thesis has no chapter in which the proposed study's result can land.**

Three findings, in order of how much they should change what you do next.

**1.1 — The structural novelty claim survives, and it is narrower and better than the one currently written down.** Across nine primary sources, **seven restrict the actions of an autonomous system (P1, P2, P4, P5, P6, P7, P8); one restricts advice shown to a human (P3, Kim et al.); one restricts a human user's own data permissions (P9, CARAC — neither of the first two)**. **None of the nine restricts which *category* of output an advisory system may show.** That is a real structural position, but its force is bounded by the sample: see the scope limit below. But it is not the position the plan argues: the plan leans on maritime domain and on graduated gating, and both are occupied — Vaaler et al. own safe small-vessel marine control, Ghaleb et al. and Kim et al. both have genuine risk-indexed three-tier gates with measured intermediate-state costs. **The defensible claim is the object of restriction and the authority structure, not the domain, the gradation, or the architecture.** *(Count corrected 17 Nov 2026 from “eight restrict actions; one restricts advice”, which miscounted CARAC as an action-restricting paper and contradicted §2.4's own table, where P9 is already graded “Neither”.)*

**1.2 — The single biggest obstacle is not novelty. It is that the thesis has no slot for the result.** **[VERIFIED]** RQ5 — the user study — was re-designated out of the thesis on 21 September 2026 (`CLAUDE.md:51`), and the frozen thesis RQ set is now RQ1–RQ3 (`docs/analysis/final-research-chain-lock.md:44-50`), none of which is answered by human-scored advisory safety. Thesis RQ2 is already *"Empirical characterisation and robustness"*, answered by the existing replay. So the proposed comparative study, if run, produces evidence that **answers no frozen thesis research question and populates no thesis chapter**. This must be resolved with the supervisor before any data is collected, and it is a cheaper problem to fix now than after a pilot.

**1.3 — Feasibility has not moved since the 16 November audit, and three of its blockers are unchanged.** Re-verified against the live repository on 17 November: **[VERIFIED]** zero `issue_time`/`lead_time`/`valid_time` occurrences in any script; the prospective collector and its output file remain absent; no ethics, rubric, consent or rater artefact exists; the candidate pool still emits `Delay` only (244 episodes `["Delay"]`, 48 `[]`, zero `Go`/`DepartureTime`/`Duration`); the trace schema still has no payload column; `execute_episode` still takes no governance parameter. The plan's §3 now authorises submission and capture in parallel with supervisor review — that change is correct and is the most time-critical item in this package, because issue-time data cannot be back-filled.

**Overall verdict: REVISE, consistent with both prior independent assessments, but for a reason neither stated.** The proposed study is feasible in principle and structurally novel in a narrow sense. It is currently unsited in the thesis, its evidence standard is set by a clinical paper the project cannot presently match, and its strongest novelty claim needs rewriting away from domain and gradation toward object-of-restriction and authority.

| Deliverable | Finding |
|---|---|
| 1. Corrected matrix | **Done — §2.** 9 of 11 papers verified from primary sources; 2 not held. Four Matrix A rows need correction; one needs withdrawal or relabelling; two closest precedents are missing from Matrix A entirely |
| 2. Gap and novelty | **RQ1 weak alone; RQ2 defensible if narrowly stated; RQ3 weakest — §3** |
| 3. Feasibility | **NOT READY — §4.** Four critical blockers, all unchanged since 16 Nov |
| 4. Experimental design | **Specified — §5.** Six arms; the binding constraint is ~85–123 independent events, not 9,135 hours |
| 5. Publication alignment | **One paper fits; two break the structure — §6.** And no thesis chapter currently hosts either |
| 6. Roadmap | **§7.** Two items are time-critical and nothing else should precede them |

---

## 2. Corrected Literature Review Matrix

All records below were read from the publisher's own PDF or page. Where a Matrix A description is wrong, the correction is stated; Matrix A itself is untouched.

### 2.1 Bibliographic records [VERIFIED]

| # | Authors, year | Title | Venue | DOI / canonical URL | Held? |
|---|---|---|---|---|---|
| P1 | Vaaler, Husa, Menges, Larsen, Rasheed (2024) | Modular control architecture for safe marine navigation: Reinforcement learning with predictive safety filters | Artificial Intelligence **336**, art. 104201 | 10.1016/j.artint.2024.104201 | ✅ `papers/sources/` |
| P2 | Ghaleb, Allahloh, Mejjaouli, Ali, Al-Shayea (2026) | Uncertainty-Calibrated Safety Gating for Vision–Language–Action Manipulation Under Domain Shift | Sensors **26**(10):3140 | 10.3390/s26103140 | ✅ `papers/sources/` |
| P3 | Kim, Kim, Bahl, Lev, González, Gee, Do (2026) | Defining operational safety in clinical artificial intelligence systems | npj Digital Medicine **9**:281 | 10.1038/s41746-026-02450-7 | ✅ `papers/` |
| P4 | Miller, T. (2026) — **sole author** | Controlled Agentic AI Systems: A Governance-Driven Architecture for Auditable and Reproducible Decision Pipelines | Mach. Learn. Knowl. Extr. **8**(5), art. 125 | Zenodo 10.5281/zenodo.19110441; code `github.com/TyMill/CAIS-pub` | ✅ `papers/` |
| P5 | Corsi, Mallik, Rodríguez, Sánchez (**2026**) | Efficient Dynamic Shielding for Parametric Safety Specifications | *Automated Technology for Verification and Analysis* — **ATVA 2025**, LNCS **16145**, pp. 157–179, Springer Cham | 10.1007/978-3-032-08707-2_8 · preprint arXiv:2505.22104v2 | ✅ preprint only |
| P6 | Hamel-de le Court, Ohlmann, Belardinelli (2026) | ProSh: Probabilistic Shielding for Model-free Reinforcement Learning | **AAMAS 2026 Extended Abstracts**, p. 3411, **3 pp.** | 10.65109/KCVZ6904 · full version arXiv:2510.15720 | ✅ `papers/sources/` |
| P7 | Hamel-De le Court, Belardinelli, Goodall (2025) | Probabilistic Shielding for Safe Reinforcement Learning | **AAAI-25**, p. 16091, 9 pp. | 10.1609/AAAI.v39i15.33767 | ✅ `papers/sources/` |
| P8 | Gerold, Lucia (2026) | Safe reinforcement learning via adaptive robust model predictive shielding | Computers and Chemical Engineering **206**, art. 109521 | 10.1016/j.compchemeng.2025.109521 | ✅ `papers/sources/` |
| P9 | Li, Yang, Zhang (2024) — **CARAC** | Context-Aware Risk Attribute Access Control | Mathematics **12**(16), art. 2541 | 10.3390/math12162541 | ✅ `papers/sources/` |
| P10 | Tayebati, Kumar, Darabi, Jayasuriya, Tulabandhula, Krishnan, Trivedi (**2025**) | CAP: Conformalized Abstention Policies for Context-Adaptive Risk Management for LLMs and VLMs | ACML 2025, **PMLR 304:926–941** | **No DOI** — PMLR identifies by URL + volume:pages | ❌ **NOT HELD** |
| P11 | Miller, Durlik, Biczak (2026) | Adaptive Human Oversight for Maritime Agentic AI Systems | Applied Sciences **16**(14):6903 | 10.3390/app16146903 | ❌ **NOT HELD** |

**Four corrections to Matrix A** [VERIFIED]: ProSh is **2026** for the proceedings abstract, not the 2026 Matrix A gives for a preprint that is 2025; Corsi is **2026** (Springer citation year), not 2025 — ATVA 2025 is the conference; Miller's CAIS is **single-authored**, so "Miller (2026)", not "Miller et al."; CAP should be **2025**, and is absent from Matrix A entirely.

### 2.2 Mechanism, assumptions and guarantees [VERIFIED]

| # | Mechanism | Assumptions required | What is actually guaranteed |
|---|---|---|---|
| P1 | PPO proposes a control action; a **predictive safety filter** solves a finite-horizon OCP for the *minimally perturbed* admissible action; terminal control-invariant ellipsoid | Known 3-DOF vessel model with identified parameters; slowly-varying disturbances; obstacle positions **and velocities** known; Assumption 1 (control-invariant set exists) | **Derivations, not theorems.** Two self-stated defeats: the terminal set is *"only … an approximation … for the nonlinear dynamics"* (p. 13) and constraints are *"implemented as soft constraints to guarantee feasibility"* (p. 14) — violations are permitted by design |
| P2 | Ensemble/MC-dropout uncertainty → temperature-scaled calibrated risk `r_t` → **three-tier state machine with hysteresis** (δ_low 0.2, δ_high 0.5) → MoveIt 2 fallback planner | Access to a usable uncertainty signal; a held-out labelled calibration set; a collision scene model | **Nothing proven, and the authors say so twice**: *"We provide rationale but no formal proof"* (§8); *"The real system does not satisfy the assumptions needed for a formal guarantee"* (§4.3) |
| P3 | **SA-ROC**: clinician declares α⁺ (min PPV) and α⁻ (min NPV); empirical scan over sorted scores yields Rule-in Safe / **Gray** / Rule-out Safe zones; **Γ_Area** = FPR(τ⁻)×(1−TPR(τ⁺)) measures the cost of indecision | A continuous risk score; **a local labelled cohort with a reference standard**; clinician-declared α; prevalence-dependence acknowledged | **Nothing proven, deliberately.** Positions itself *against* conformal prediction's guarantees; constraints are empirical on the local cohort. Bootstrap CIs (2000 resamples) only. Defers finite-sample guarantees to future conformal risk control |
| P4 | **CAIS**: governance operator `G(d,s,C)` decomposed into approval / **repair** (projection to nearest admissible) / fallback, plus hash-chained audit traces and replay | `A_C(s)` non-empty, closed, **convex**; `∆` norm-induced; Lipschitz policy and transition. Author concedes upfront these may not hold | **Definition + an unproved "Bounded Drift Theorem"**, and the measurement contradicts the definition: *"CAIS does not guarantee absolute constraint satisfaction in practical settings"* (§5.5) |
| P5 | One **atomic shield per atomic hazard**, synthesised offline by abstraction-based control; composed online when the live specification is revealed; `SafeHandover` for specification change | A perturbed discrete-time **dynamical model**; a finite parameterised set of possible specifications; stationary obstacles (Thm 3); abstraction soundness | **Strongest and hardest of the nine.** Theorem 3 gives deterministic, infinite-horizon, worst-case safety **and** non-blockingness, correct by construction. Caveat (Remark 2): maximal permissiveness only w.r.t. the abstraction |
| P6 | Risk-budget **state augmentation** + shield applied to the **policy distribution before sampling**; learned backup cost critic `Q_b` | A CMDP with cost function and budget; **no simulator or environment abstraction required** — its selling point; critic accuracy `Δ_b` | Expected-cost bound `C(π̄) ≤ x₀ + 2Δ_b/(1−γ_c)` — **exact only as `Δ_b → 0`**. Optimality only in deterministic environments. Weakest guarantee of the shielding set, and it bounds *accumulated cost*, not state avoidance |
| P7 | Inductive ε-upper bound `β` on reach-unsafe probability by interval iteration; shield as a **safety-aware state-augmented MDP** where the agent allocates a forward risk budget | **Known safety dynamics of a finite MDP** — authors call this *"strong"*; Slater's condition for Thm 2.3 | **Hard probabilistic bound holding throughout training and at test**: `M_π̂ ⊨ P_{≤p}(Reach(u))` (Thm 1, Cor. 1). Residual risk confined to the `β`-computation phase |
| P8 | Robust MPS with an **adaptive safety parameter σ placed in the RL observation space**, letting the agent vary its own conservativeness before hard fallback fires; ARNMPC backup | Explicit nonlinear plant model for online rollouts; bounded uncertainty set; sampleable distribution (Assumption 1) | **Probabilistic, finite-horizon**: `N`-step probabilistic safe set at 1−ε = 0.995, confidence 1−10⁻⁶, 2,764 samples. Zero violations in experiments are **empirical**; the min–max rollout scheme *"does not ensure robust safety"* (§5.7) |
| P9 | Three-level risk attribute tree → AHP + entropy weights reconciled by game theory → fuzzy comprehensive evaluation → **graduated authorisation level**; smart contracts demote privileges mid-session | Expert-elicited AHP values; hand-drawn membership functions; asserted action-risk table; predefined thresholds | **Nothing. No theorem, lemma, proof or bound anywhere in the paper** |

### 2.3 Methodology, baselines, findings, limitations [VERIFIED]

| # | Baselines compared | Headline findings | Authors' own limitations |
|---|---|---|---|
| P1 | Standard PPO without PSF; penalty ablations; PSF on/off at train vs test | Zero collisions in training and test for Cases 1–3 vs PPO's 98/96/95% COLAV. **But 3 collisions in 300 real-environment simulations** — *"the predictive safety filter was not able to fully guarantee the safety of the agent"* (p. 20). Higher cross-track error is the price | Simulation only; *"measurement noise, modeling error, and sensor failure must be handled rigorously"*; PSF margins *"can hinder forward progress … even though a feasible path exists"*; baseline comparison *"slightly unfair"* on information |
| P2 | No gating; **uncalibrated thresholding**; calibrated gating; post-hoc oracle | Shifted success 57.5% → 77.2%; ECE 0.3025 → 0.1003. **The uncalibrated baseline beats it on raw metrics** (89.5% success) at 21.6 interventions/episode vs 11.5. **63.7% of residual collisions occur *inside* the pause state** | *"Near-zero collision claims … are not consistent with the cleaned benchmark exports"*; *"uncalibrated thresholding is stronger on raw success and collision metrics"*; simulation only; fallback not formally verified |
| P3 | Two FDA-cleared mammography AIs against each other; **the original reading radiologist** scored against the same reference standard | AUC reverses the ranking: AI#1 AUC 0.928 > AI#2 0.882, yet AI#2 safely cleared 290 vs 167 cases. Gray Zone 64.3% / 66.3% of cohort at α=100%. **Where the AI was most confident in rule-out, radiologist accuracy was *lowest*, by over-calling** | 1000 retrospective cases; thresholds near α=100% rely on sparse tails; *"prospective validation through user studies is essential"*; α variability complicates standardised comparison |
| P4 | Ungoverned; approval-only gating; projection repair; decentralised vs centralised; adversarial and poisoning stress | Violation rate: ungoverned 1.0000, **gating 0.0333, projection 0.8317**. Drift: gating 10.37, projection 12.74 | *"does not guarantee strict feasibility"*; controlled simulation only. **⚠️ The Abstract and Conclusions state the projection-vs-gating result backwards relative to Tables 2 and 4** — cite §4.1/§5.5, not the abstract |
| P5 | Pure-online shield; pure-offline shield (intractable: *"2^400 instances"*) | Dynamic shields up to **5× faster** than pure online; offline 2m12s–9m35s. Safety not measured — *"by-construction safe"* | *"sometimes the system would get stuck"*; safe handover is *"conservative but simple"*; stationary obstacles only |
| P6 | PPO-Saute, TD3-Lagrangian, PID-TD3, FOCOPS, CPO | Qualitative only in 3 pages: cost held under budget during training, *"best trade-off between safety and performance"* | **No limitations section exists** in the extended abstract. Full benchmark deferred to arXiv:2510.15720 |
| P7 | Unshielded PPO; PPO-Lagrangian; CPO | *"PPO-shield does indeed guarantee safety throughout training and at test time"* in all six environments; outperforms CPO and PPO-Lagrangian on reward | Known-safety-dynamics assumption *"is strong"*; augmented space *"may lead to slower convergence"*; state-avoidance safety only |
| P8 | RL-only with reward shaping; robust MPS; adaptive MPS; **adaptive robust MPS**; exact-NMPC backup; MC vs min–max rollouts | Adaptive robust: **zero violations with fewer backup interventions** (6.1 → 4.5 at λ=5e3) vs robust alone. Unshielded RL violates (6.5/3.5/3.1). Outside its design uncertainty range: *"systematic constraint violations"* | *"these findings are limited to a single case study and should therefore be validated more broadly"*; min–max *"does not ensure robust safety"* |
| P9 | **ABAC only** | No accuracy, no error rate, no detection rate — *"there is nothing to be right or wrong about"*. Claims only lower overhead and that authorisation level varies with risk | Entire limitations discussion is one paragraph on improving risk-assessment accuracy. No acknowledgement of absent ground truth or synthetic evaluation |

### 2.4 Relationship to this architecture — the decisive axis [VERIFIED]

| # | Restricts **actions** or **advice**? | Risk-indexed intermediate tier? | Independent reference used | Human authority | Competitor or cross-domain analogy? |
|---|---|---|---|---|---|
| P1 | **Actions** — rewrites surge force and yaw moment | No tier; continuous minimal perturbation | Simulator (`gym-auv`); real terrain + AIS tracks that never avoid | **None** | **Cross-domain analogy.** Shares the domain, not the object of restriction |
| P2 | **Actions** — execute / pause / fallback | **Yes, genuine, with hysteresis** | Simulator only (Isaac Sim) | No — human help is future work | **Closest mechanism competitor** |
| P3 | **Advice** — partitions what disposition a score licenses | **Yes — the Gray Zone is the subject** | **Biopsy + long-term follow-up, plus the unaided radiologist's own reading** | Yes in the Gray Zone; **the AI disposes autonomously inside the Safe Zones** | **The direct competitor on concept and the evidence benchmark** |
| P4 | **Actions** — rewrites the executed action | Three modes, **feasibility-switched, not risk-graded**; run as rival configurations, never composed | **None independent** — own constraints, own simulator, circular by construction | Auditors only, after the fact | **Analogy** — governance plumbing and audit replay, not restriction |
| P5 | **Actions** — overrides control inputs | No | None — correct by construction | **None** | **Analogy, but the most structurally transferable one** (see §3.1) |
| P6 | **Actions** — rewrites the policy distribution | No | Benchmark environments | **None** — the word "human" does not appear | **Analogy** |
| P7 | **Actions** — in an augmented action space | A forward risk budget, not a tier | Finite MDPs | **None** | **Analogy** |
| P8 | **Actions** — passes or substitutes reactor control | **σ varies conservativeness before hard fallback** | Own plant model | **None** | **Closest precedent for RQ3** (see §3.3) |
| P9 | **Neither** — restricts a *human user's* data permissions | Graduated authorisation level; in-session demotion — **never measured** | **None.** 100 simulated users with hand-set risk values | Human is the *subject* of control | **Not a competitor. Cross-domain analogy at best** |

**The finding that matters.** **Seven of nine restrict an autonomous system's actions** (P1, P2, P4, P5, P6, P7, P8); **one restricts advice to a human** (P3); **one restricts a human user's data permissions and so restricts neither** (P9). Two have genuine risk-indexed tiers. **None of the nine restricts which *category* of output an advisory system may show to a human who retains authority.** That gap is real within this sample. It is also narrow and sample-limited (§8.6), and §3 tests whether it is enough.

### 2.5 Two papers missing from Matrix A [VERIFIED]

**Gerold & Lucia (P8)** and **CAP (P10)** have no row in Matrix A, yet they are the two closest precedents for the contributions the plan leans on — P8 for C3/RQ3, CAP for RQ2's safety–coverage frontier. Both are cited in `docs/analysis/graduated-advisory-safety-novelty-assessment.md` and named on the plan's §3 reading list. **Matrix A therefore understates the prior art for the project's own preferred contributions.** This is the most consequential gap in the matrix.

### 2.6 CARAC — recommendation [VERIFIED]

CARAC has no connection to AI action restriction. Full-text counts: *access control* 106, *user* 156, *smart contract* 37, against **0 each** for *autonomous*, *reinforcement learning*, *shield*, *advisory*, *AI agent*. **Recommendation: withdraw the row, or relabel it a cross-domain analogy and drop "very close conceptual competitor".** Keeping it as it stands invites a reviewer to find a cybersecurity paper among safe-RL work and question how the rest of Matrix A was graded.

---

## 3. Research Gap and Novelty Assessment

**⚠️ A terminology collision that will cost you at the defence.** The matrix and plan use RQ1/RQ2/RQ3 for *verifiable decision policy / intermediate-restriction trade-off / dependability under degraded observations*. The **frozen thesis RQ set uses the same labels for different questions** — operational specification / empirical characterisation and robustness / structural warrant of the multi-component classifier (`docs/analysis/final-research-chain-lock.md:44-50`) **[VERIFIED]**. Two incompatible RQ1–RQ3 sets are live in one project. Renumber one of them before anything is written for examiners.

This section assesses the **matrix/plan** RQs.

### 3.1 RQ1 — representing risk, observation reliability and advisory permissions in a verifiable policy

**Established by others.** Formal runtime restriction with proof is a mature field, and the proofs are stronger than anything this project has. P7 gives a hard probabilistic reachability bound holding through training and test. P5 gives deterministic infinite-horizon safety *and* non-blockingness, correct by construction, with a **parametric** specification family composed online — structurally the closest formal analogue to "a hazard state selects which permission set applies". P4 offers the governance-operator formalism with audit-trace semantics and replay.

**Established by this project already.** **[DOCUMENTED]** Journal 1 claims the formal specification, three proved properties including Safety Dominance, and the implemented prototype (`manuscript.md:88-93`).

**The unresolved question.** Whether *observation reliability* can be made a first-class term in an admissibility policy alongside hazard state — i.e. permissions conditioned jointly on what the world is doing and on what is known about it. **[VERIFIED]** No competitor **in this nine-paper sample** does this: P5's parameters are hazard geometry, P7's are transition probabilities, P2's uncertainty drives a tier but not a permission *set*. The sample is not a systematic search (see §8.6), so this is an absence in the sample, not an established absence in the literature.

**Defensible novelty: low on its own.** The formalism is not new; the particular conditioning might be. **Matrix C's own verdict — "Limited alone" — is correct and should be retained.**

**Examiner objections.** *"This is Corsi's parametric shielding with the parameter renamed."* The answer must be precise: P5 composes shields over *safety specifications* with a known dynamics model; this project composes permission sets over *observation-quality states* with no dynamics model at all. *"You prove less than the papers you cite."* True, and conceding it costs nothing — the contribution is not a stronger guarantee.

**What would resolve it.** A specification in which observation quality and hazard state are separate arguments, with a property that fails if either is dropped. Nothing less distinguishes it from re-parameterised shielding.

### 3.2 RQ2 — when intermediate advisory restrictions improve the safety–usefulness trade-off

**Established by others, and more than the plan acknowledges.** P3 is the direct competitor: declared reliability targets partition a score into two safe zones and a gray zone, with **Γ_Area as a purpose-built metric for the cost of indecision** — the exact construct the plan calls "useful coverage". P2 measures intervention burden as a first-class metric and sweeps the threshold. CAP (P10, **not held**) selects point / set-valued / abstention output by downstream utility. **The question shape is occupied.**

**The unresolved question, stated precisely.** Whether restricting *which categories of recommendation* may be shown — as opposed to withholding the whole message, deferring the case, or filtering an action — reduces independently judged harm at comparable useful coverage, **where the human's authority is unconditional throughout**. [VERIFIED] P3 withdraws the AI's authority in the Gray Zone but grants it autonomously in the Safe Zones; P2 withholds the action entirely. Neither restricts output *type* while continuing to advise.

**Defensible novelty: moderate, and only if stated as above.** Four claims must be separated:

| Claim type | Status |
|---|---|
| **Architectural integration** | **Not novel.** Layered propose-then-restrict is standard across P1, P2, P4, P5, P8 |
| **Application novelty** | **Not defensible alone.** P1 occupies safe small-vessel marine control |
| **Empirical contribution** | **Defensible if the reference is independent** — a measured safety–coverage frontier for category-level restriction under unconditional human authority |
| **Original computational method** | **Not claimed here.** Belongs to RQ3 if anywhere |

**Examiner objections, and the answers.**

1. *"This is SA-ROC in a boat."* The strongest objection. Answer: SA-ROC partitions one score's disposition; this partitions the recommendation space, and keeps advising in the middle rather than deferring the case. **Your evidence must be at least as good as theirs, and currently it is far weaker** — see §4.
2. *"Your intermediate state is free by assumption."* P2 found **63.7% of residual collisions occurred inside the pause state**. The middle tier is not safe by default, and the study must measure what the restricted state costs, not assume it is a saving.
3. *"Δ_L2 is a tautology."* **[DOCUMENTED]** The repository concedes this (`evaluation-baseline-decision.md:31`). Any arm of the new study scored on admissible *sets* rather than displayed *advice* repeats Journal 1 and adds nothing.
4. *"Experts will ratify the rules that built the gate."* Live and unresolved — see §4.3.

**What would resolve them.** An outcome-level or independently-justified reference; a measured cost of the intermediate state; endpoints defined on displayed advice, never on admissible sets.

### 3.3 RQ3 — dependability under missing, stale, delayed or conflicting observations

**Established by others — and this is where the plan is most exposed.** **[VERIFIED]** P8 (Gerold & Lucia) puts an adaptive conservativeness parameter into the policy's observation space so the agent varies its own caution before hard fallback fires, and demonstrates **zero constraint violations with fewer backup interventions than fixed-robust shielding**, under parametric uncertainty, published in a peer-reviewed journal. That is RQ3's claim shape, already achieved. P2 is the degraded-observation analogue for perception. P6 handles cost uncertainty without any environment model.

**The unresolved question.** Whether *advice-type-specific* evidence requirements — different freshness or support thresholds for a departure window than for a delay message — beat a single shared cutoff. **[VERIFIED]** No competitor **in this nine-paper sample** differentiates requirements by output type, because none of the nine has output types at all. Sample-limited (§8.6).

**Defensible novelty: lowest of the three, and currently unsupportable.** Three independent blockers: **[VERIFIED]** no issue-time data exists and cannot be back-filled; `ageᵢ` is unspecified and the repository forbids inventing it (`algorithm-specification.md:115`; `research-chain-lock.md:205`: *"Fault injection … NOT JUSTIFIED — yet"*); and synthetic perturbation of reanalysis is explicitly low novelty by the project's own assessment.

**Examiner objection.** *"Gerold and Lucia did this in 2026 with a real plant model and a probabilistic guarantee."* There is no good answer today. **Keep RQ3 conditional, exactly as the plan has it**, and do not promote it without a reproducible failure that a shared cutoff cannot fix.

### 3.4 Where the defensible contribution actually sits

Stated plainly, and more narrowly than Matrix C:

> **An evaluation method, and a measured frontier, for restricting the *category* of advice an AI may show to a human who retains unconditional authority — scored against a reference that is independent of the rules that built the restriction.**

Not the architecture. Not the maritime domain. Not gradation. Not the formal model. The object of restriction, the authority structure, and — above all — **the independence of the reference**, which is the one thing none of the eight action-restriction papers needed and which P3 shows is both achievable and capable of producing an uncomfortable answer.

---

## 4. Comparative Study Feasibility

Re-verified against the live repository on 17 November 2026.

| Requirement | Status | Evidence |
|---|---|---|
| Issue-time forecast availability | **[NOT FOUND] — critical** | Zero `issue_time`/`lead_time`/`valid_time` in any script; collector and output absent; all seven datasets are reanalysis or harmonic tide |
| Independent observed conditions / reference labels | **[NOT FOUND] — critical** | No incident, SAR, buoy or outcome record for the site. Only third-party literature about other sites |
| Vessel and route definition | **[PARTIAL]** | Vessel class is a three-valued configuration parameter (`appendix-c-formalisation.md:21-31`); no vessel, trip or route record exists |
| Candidate recommendation categories | **[NOT READY] — critical** | 244 episodes emit `["Delay"]`, 48 emit `[]`, **zero** `Go`/`DepartureTime`/`Duration`. The unrestricted arm produces nothing |
| Independent safety and usefulness assessment | **[NOT FOUND] — critical** | No rubric, rater, agreement statistic or ethics artefact. Utility construct formally OPEN with an instruction not to invent one |
| Threshold-boundary and matched-context tests | **[PROPOSED]** | Now named in plan §3 (1.00 m, 1.25 m, 21.6 kn, 10.0 mm/hr, exact sunrise) — specified, not built |
| Sample size and event clustering | **[VERIFIED, constraining]** | 531 PRIMARY CAUTION hours → **201 days → ~85–123 independent events** |
| Research ethics | **[NOT FOUND] — critical path** | Not applied for. Every route to an independent reference passes through it |
| Reproducibility | **[STRONG for what exists]** | SHA-256 manifests, deterministic engine, 149 tests. But `execute_episode` still takes no governance parameter, and the trace schema still has **no payload column** |

### 4.1 Critical blockers and practical resolutions

**B-1 · No independent reference.** Every internal candidate derives from the gate's own source set. *Resolution:* build it as the study's principal construction task, following P3's template — a reference standard independent of both the model and the human, plus a record of what the unaided human would have decided. P3 achieved this with biopsy and long-term follow-up; the maritime equivalent is MMEA/DOF incident records, which must be requested now, with a negative answer treated as a study-design input.

**B-2 · No issue-time data.** *Resolution:* begin prospective capture immediately. **Unrecoverable delay — this is the only blocker that gets strictly worse with time.**

**B-3 · Degenerate candidate pool.** The quantity the study measures — what restriction removes — is zero by construction, and the *unrestricted* arm is the empty one. *Resolution:* build the candidate generator as a **separate, declared study instrument outside the governed architecture**. Adding rules to the canonical repository would import the authority gaps (`OPEN-L3-1C`, `OPEN-L3-1D`, `GAP-03`) into the experiment. Extend the trace schema with payload and explanation columns first — raters judge text, and the harness currently persists only type labels.

**B-4 · No ethics approval.** *Resolution:* submit now, in parallel with supervisor review, as plan §3 already authorises.

**B-5 · Precision.** ~85–123 independent events, not 9,135 hours. *Resolution:* cluster at the weather-event level; plan power on pilot-measured discordance; treat a second coast as adding independent clusters rather than correlated hours.

### 4.2 Expected limitations even if everything succeeds

Site-specific; one vessel class; `g_t` accounts for 86.82% of non-SAFE classification, so the gate is to first order a clock; `D = {m}` makes every severity figure a lower bound; ~40% of the evaluation window is pre-sunrise and gated before weather is consulted.

### 4.3 The circularity risk that survives a successful panel

**[VERIFIED]** The repository already names it: *"Experts ratify the same rules or classify a rule-compliant generic statement as safe useful advice."* If local skippers hold the thresholds MET publishes, the reference is procedurally but not substantively independent. The boundary-scenario test now in plan §3 is the right instrument; GPT's §7 correctly adds that threshold agreement can be justified by independent physical evidence, so the test must be read alongside provenance and rater reasoning rather than alone. **P3 shows what success looks like: the reference disagreed with the human precisely where the model was most confident.** A reference that never disagrees with the gate has not been shown to be independent.

---

## 5. Experimental Design [PROPOSED — no result is reported]

### 5.1 Arms

| Arm | Policy | Role |
|---|---|---|
| **C0** | Ungated: full candidate message at every state | Reference bound on harm available without governance |
| **C1 / B1** | Participation-only: full scope when active, nothing at UNSAFE | **Primary contrast partner** |
| **C2 / B3** | Static graduated: same outer cutoff, category restriction at CAUTION | **The treatment** |
| **B2** | Conservative binary: withhold at CAUTION and UNSAFE | Bounds the cost of shutting the middle region |
| **B4** | Calibrated uncertainty-aware abstention, threshold fitted on validation events | **The strong comparator.** Without it the study cannot answer "why not just abstain?" |
| **A1** | Action-specific evidence rule, if implementable from the same inputs | Optional; tests whether a simple per-type rule suffices |

**Primary contrast: C1 vs C2**, consistent with plan §4.1. C0 and B2 are secondary bounds. C1 doubles as the permissive binary and appears once.

### 5.2 Information parity

All arms consume the **same episode, same candidate pool, same ranking, same display conventions and the same status cues**, differing only in the permission map. B4's calibration uses only information available to C2 — P1 reports its own baseline comparison was *"slightly unfair due to the difference in available information"*, and that error is easy to repeat.

### 5.3 Ground truth — three distinct constructs, never merged

| Construct | What it measures | Source | Status |
|---|---|---|---|
| **Policy conformance** | Did output stay inside the permitted set? | The engine | **Analytically zero. Not an endpoint** — F1/F2 cannot vary |
| **Independently assessed advice safety** | Would following it have exposed the operator to verified concerning conditions? | Blinded rubric + ex-post hazard reference | **The primary endpoint** |
| **Human decision outcomes** | Did anyone decide differently? | Field study | **Out of scope. Do not claim** |

Separate the **ex ante** reference (was this specificity supportable from information available at issue time?) from the **ex post** hazard reference, score both axes separately, and keep future measurements out of the ex ante dossier.

### 5.4 Endpoints

Primary: severe inappropriate recommendations per eligible episode. Co-primary: useful coverage — fraction of eligible episodes with at least one acceptable, actionable, feasible next step, scoring generic checklists strictly. Secondary: harmful omission; false suppression; **cost of the intermediate state** (P2's lesson); fallback availability; risk–coverage curves. Diagnostics only: compliance, structural binding, change in displayed advice.

### 5.5 Calibration and analysis

Split development, calibration and test **by site or time block**, never by hour. Pair policies on the same episode and candidate message. Cluster at the weather-event level; cluster bootstrap intervals; exact McNemar only for independent paired binary episodes. Pre-register the main contrast, practical margins and multiplicity strategy. **[DOCUMENTED]** Significance testing over a deterministic census is not meaningful, so the calibration/test split must be constructed deliberately.

### 5.6 What this design cannot deliver

No claim about trust, reliance, decision quality or real-world safety outcomes. No claim that the thresholds are correct. No generalisation beyond the sampled site, season and vessel class without external replication.

---

## 6. Journal Publication Alignment

### 6.1 What Journal 1 already claims [VERIFIED]

`publications/active/journal-1/README.md:60` lists as contribution 4: *"Experimental evidence: graduated vs. binary-gated vs. ungated baseline comparison."* **The proposed study's C0/C1/C2 arms are already claimed.** What is genuinely new relative to Journal 1 is the independent reference scoring, the B4 abstention comparator, the useful-coverage endpoint, and displayed-advice-level measurement — not the comparison itself.

Journal 1's own boundary is clear and useful here: *"Journal 1 makes no claim about human decision quality, trust, calibrated reliance, actionability, task completion or real-world safety outcomes"*, and §14.1 concedes that *"only one conclusion type is generated … the withheld types are withheld from a rule set that could not have produced them."*

### 6.2 Three live inconsistencies [UNRESOLVED]

1. **Journal 1 internal.** The manuscript prints four RQs including RQ-J2; the maintained authority removed RQ-J2 and merged RQ-J4 (`evaluation-specification.md:83`). The README says *"research design phase … later empirical sections remain plans"* while the manuscript reports §11–12 as closed.
2. **Publication sequence.** `publication-plan.md` and `PUBLICATION-THESIS-SYNC.md` describe a three-paper plan whose Paper 2 (formal model → Expert Systems with Applications) has been absorbed by Journal 1. **Taking the Journal 2 slot therefore displaces a paper neither document has retired.** AAI 2026 appears in neither plan.
3. **Thesis structure.** Three mutually inconsistent chapter structures exist.

### 6.3 The decisive problem [VERIFIED]

**RQ5 was re-designated out of the thesis on 21 September 2026** (`CLAUDE.md:51`), and the frozen RQ set is RQ1–RQ3 (`final-research-chain-lock.md:44-50`). Thesis RQ2 — *"Empirical characterisation and robustness"* — is already answered by the existing replay.

**Consequence: the proposed study produces evidence that answers no frozen thesis research question and populates no thesis chapter.** Running it without resolving this yields a publishable paper that does not advance the thesis. **This is a supervisor decision and it should precede all other work**, because it is nearly free now and expensive after a pilot.

Three options, in order of preference:

| Option | Effect | Cost |
|---|---|---|
| **A. Reinstate a thesis RQ for independently assessed advisory safety** | Gives the study a home and a chapter | Reopens a deliberately frozen RQ set |
| **B. Run it as a publication-only output** | No thesis change | Thesis gains nothing; graduation checklist needs re-examination |
| **C. Widen thesis RQ2 to include independently assessed restriction effect** | Minimal structural change | RQ2 then spans replay characterisation and human-scored safety — arguably two questions |

### 6.4 Is a separate RQ3 methods paper justified?

**No — keep it conditional.** **[VERIFIED]** Thesis RQ2 already covers robustness; P8 has published the adaptive-conservativeness result; `ageᵢ` is unsourced and fault injection is recorded as *"NOT JUSTIFIED — yet"*. Promote it only on the plan's own trigger: a reproducible failure that tuned abstention, static graduated gating and a simple advice-specific rule cannot resolve. **One paper fits the current structure. Two break it.**

### 6.5 Venue

The endpoint is independently assessed advice safety with an explicit coverage trade-off, so **Safety Science** and **Decision Support Systems** fit better than the ocean-engineering or AI-methods venues — the contribution is an evaluation method and a measured frontier, not a new algorithm. Confirm against the existing Journal 1 venue choice to avoid submitting two papers to the same journal from one architecture.

---

## 7. Prioritized Research Roadmap

### P0 — before anything else

| # | Action | Dependency | Deliverable | Go/no-go | Risk |
|---|---|---|---|---|---|
| **P0-1** | **Resolve §6.3 with the supervisor**: does this study answer a thesis RQ, and which chapter hosts it? | None | A decision recorded against option A, B or C | **No-go on the whole programme if none** | Running a study whose result the thesis cannot use |
| **P0-2** | **Submit the ethics application** | None | Submitted application | — | Longest lead item; every reference route passes through it |
| **P0-3** | **Begin prospective issue-time capture** — implement the collector specified at `scripts/README.md:3-39` with issue time, valid time, lead time and retrieval timestamp | Authorisation | A growing archive; earliest recoverable issue time logged | — | **Unrecoverable delay. Strictly worsens daily** |
| **P0-4** | Write to MMEA and Department of Fisheries Malaysia for incident records | None | A written response either way | Negative answer narrows the study to ex ante reference only | Without it there is no ex-post hazard axis |
| **P0-5** | Define the four rater constructs and the severity scale **with raters, before any gate output is seen** | P0-2 | Rubric + calibration protocol | **No-go if raters cannot distinguish them** | The pivotal test |
| **P0-6** | Build the candidate generator as a separate declared instrument; extend the trace schema with payload and explanation | None | Candidate inventory with full text | No-go if the pool cannot produce both useful and unsafe output | Adding rules to the canonical repository would import the authority gaps |
| **P0-7** | Pre-register: scenario frame, **sampling unit = event**, blinding, rater count, agreement statistic, practical margins | P0-5 | Registered protocol | — | Post-hoc margins are indefensible |

### P1 — before the main experiment

| # | Action | Dependency |
|---|---|---|
| P1-1 | Parameterise `execute_episode` with a governance configuration so one candidate set replays under C0/C1/C2/B2/B4 | P0-6 |
| P1-2 | Source `ageᵢ` per component, or declare RQ3 synthetic and bound the claim | — |
| P1-3 | Specify B4: risk score, calibration split by site/time block, fallback model | P1-1 |
| P1-4 | Build the ex ante / ex post reference separation and the per-episode dossier schema | P0-4, P0-5 |
| P1-5 | Define useful coverage **with the reference panel** and pre-register it | P0-5 |
| P1-6 | Event-level power analysis from pilot-measured discordance | P0-7 |
| P1-7 | Add Matrix A rows for **Gerold & Lucia** and **CAP**; resolve the CARAC row; renumber one of the two RQ1–RQ3 sets | — |
| P1-8 | Obtain CAP and Miller's *Adaptive Human Oversight* as primary sources | — |

### P2 — quality and reproducibility

Resolve the three Journal 1 / publication-sequence inconsistencies (§6.2); reconcile the three thesis chapter structures; retire or re-banner `evaluation-design-rq4.md`, whose expected-S column is a circularity trap; commit `docs/analysis/graduated-advisory-safety-novelty-assessment.md`, currently untracked; **resolve the AAI 2026 manuscript's 7-page overrun against a 6-page limit** — a live submission defect unrelated to this package but still open.

### 7.1 Supervisor decisions required

1. **Thesis siting** (§6.3) — blocking.
2. **Journal 2 slot** — does the comparative study take it, and what happens to `publication-plan.md`'s Paper 2?
3. **Authorisation** to submit the data request and begin prospective capture.
4. **CARAC** — withdraw or relabel.
5. **Scope of the RQ3 paper** — confirm it stays conditional.

### 7.2 Go / Revise / No-Go

**REVISE.** Advance to a preparation stage, not to the safety-effectiveness study.

- **Advance** when: the thesis siting is resolved; raters demonstrably distinguish the four constructs; an issue-time path exists; and the candidate pool can produce both useful and plausibly unsafe output.
- **Narrow** to a scenario-based feasibility study if rater calibration succeeds but issue-time records or hazard matching do not materialise. Bound conclusions to the vignettes.
- **No-go on the safety-effectiveness claim** if the reference reduces to the gate's own rules, or if the independent event count cannot resolve a prespecified margin. A rigorous negative result remains publishable; a third comparison of admissible sets does not.

---

## 8. What This Package Does Not Establish

1. No new experiment was run. Every number from the repository is a re-verification of an existing result.
2. CAP and Miller's *Adaptive Human Oversight* were **not read as primary sources** — both are unheld. Statements about CAP rest on the publisher's abstract and citation block only.
3. The nine primary sources were read for mechanism, assumptions, guarantees, methodology and limitations — not replicated. Where a paper's own abstract contradicts its tables (P4), both are reported.
4. Novelty assessments are judgements about defensibility against a reviewer, not predictions of acceptance.
5. The thesis-structure finding (§6.3) rests on documents that disagree with each other. The frozen RQ set and the RQ5 re-designation are quoted directly, but which chapter structure is authoritative is **[UNRESOLVED]** and only the supervisor can settle it.

6. **The novelty claims are sample-limited, and this bounds every “none of the nine” statement in §1 and §3.** The nine-paper pool was not assembled by a systematic, protocol-registered search. It came from Scopus AI synthesis plus GPT's Matrix A, screened by a single reviewer with no second rater, no inter-rater agreement statistic, no documented database set, date range, query strings, inclusion/exclusion criteria or PRISMA flow, and no backward or forward citation chase. Two further named competitors (CAP, Miller) are unheld and therefore uncounted. **Correct form of the claim:** *“within a non-systematic sample of nine primary sources, none restricts which category of advisory output may be shown to a human who retains authority.”* **Incorrect form:** *“no prior work does this.”* A reviewer can overturn the second with one paper; the first survives, and converting it into the second requires a registered systematic review, which this project has not run for this question. The §1.1 and §3 novelty gradings should be read as *defensibility under a declared sample limit*, not as literature-wide absence.