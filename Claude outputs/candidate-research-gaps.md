# Candidate Research Gaps — Adjudicated Against Evidence

**Prepared:** 17 November 2026 · **Author:** Claude (Cowork session) · **Status:** exploratory research branch. Frozen RQ1–RQ3 and all canonical artefacts untouched.

**Companion:** `novelty-literature-matrix.md`. Numbered references (#n) refer to its matrix.

**Adjudication rule, applied before looking at the evidence.** A gap is **CONTRADICTED** if a verified source implements the mechanism. **PARTIALLY SUPPORTED** if some constituent is implemented and a specific constituent is not. **SUPPORTED** if no verified source implements it and the absence is structural rather than incidental. **UNRESOLVED** if the deciding source could not be read. **An omitted experiment or an unexplored application domain is not evidence of novelty** and is not counted as support anywhere below.

---

## 0. A constraint from the project's own frozen position

Before any external adjudication, the thesis has **already conceded** the relevant mechanisms. `docs/analysis/final-research-chain-lock.md` §A, "Frozen literature position — established prior work; the thesis concedes all of the following and claims novelty for none", includes verbatim:

> *state-conditioned advisory restriction · advisory-category inhibition · **human-facing advisory inhibition based on observation validity** (TSO-C151c §5.6: invalid position ⇒ FLTA and PDA inhibited, GPWS retained, inhibit annunciated to crew) · nested admissible sets contracting to empty · … · **totality over incomplete observations (Bauer et al. 2011; Taleb et al. 2023)** · conservative handling of unusable observations …*

and the lock adds: *"No report wording may imply generic novelty for any of these."*

**Two consequences, and they are binding.**

1. **"Advisory-category inhibition based on observation validity" is already conceded.** That is, in substance, the candidate topic's mechanism. A new claim of novelty for the mechanism would contradict the project's own authoritative document.
2. **The lock already cites Bauer et al. 2011** — the LTL₃ paper (#6) that the prior-art search independently identified as the closest formal antecedent. The project has therefore already placed itself downstream of the runtime-verification treatment of evidentiary insufficiency.

**So any surviving novelty must be at the level of formal theory, decision procedure and guarantee — not mechanism.** This is stated first because it disqualifies the most natural framings before the literature is even consulted.

---

## G1 — Abstention at the level of output **category** rather than whole output or label

**Claim under test.** *No existing method restricts which category of output a system may issue, as opposed to abstaining from the whole output or withholding a label within one output space.*

### Verdict: **CONTRADICTED**

| Deciding source | Status | What it does |
|---|---|---|
| **#1 AC-RAC** (Zhu, Kiyani, Pappas, Hassani) | **ICML 2026, peer-reviewed, full text read** | Operates over a finite discrete action set with distinct operational meanings. The max-min rule `a(x)=argmax_a min_{y∈C(x)} u(a,y)` means that as the prediction set grows, high-stakes actions stop being selectable — **uncertainty restricts which action categories are reachable**. §4 calibrates a genuine per-action threshold vector λ=(λ_a) |
| **#2 Role-Stratified CRC** | preprint, Jul 2026 | Blocks individual argument fields of an action, **stratified by semantic role category**, each with its own risk budget |
| **#15 Set-Valued Policy Learning** | preprint, May 2026 | With >2 treatments, defers a *strict subset* — narrows the admissible action set without abstaining entirely |
| **#8 USPSTF** | official methods | Grade I **withholds the entire for/against recommendation category** and substitutes an I statement |
| **#10 Unlu**, **#12 CROWN-QA** | preprints, 2026 | Typed deferral; which answer *kind* is licensed |

**#4 CAP is a near-miss that must be named pre-emptively.** Its policy π: X → {predict, set, abstain} does restrict which *kind* of output is issued — but its three options are **granularity levels of one answer**, not semantically distinct categories. The same applies to specificity-rung abstention.

**Residual after contradiction, stated precisely.** In every ML instance, "category" is either a *point in one action space whose admissibility falls out of a utility calculation* (#1, #15) or a *component slot of one action* (#2). **None treats recommendation types as first-class objects carrying their own distinct evidentiary preconditions.** In #1 the per-action λ_a are **calibration artifacts chosen to equalise coverage**, and the guarantee is 1−α for *every* action — a uniform requirement. In #2 the α(r) differ but are **assigned by risk**, not *derived from what the output type requires*.

That residual is real. It is a **refinement of AC-RAC, not virgin territory**, and must be positioned that way.

---

## G2 — Admissibility conditioned on **evidence sufficiency** rather than model confidence

**Claim under test.** *No existing method conditions abstention on properties of the available input evidence — missingness, staleness, delay, source conflict, measurement reliability — rather than on the model's confidence.*

### Verdict: **PARTIALLY SUPPORTED** — three of five evidence dimensions are occupied; one is not; the combination is not

| Evidence dimension | Status | Deciding source |
|---|---|---|
| **Missingness** | **CONTRADICTED** | **#3 Zaffran et al., ICML 2023, peer-reviewed, full text read.** The canonical result: impute-then-predict with conformalisation preserves *marginal* coverage but **under-covers for specific missingness patterns, worst when important features are missing** — which is precisely the failure the candidate problem is premised on. CP-MDA-Exact/-Nested deliver **mask-conditional validity**, a guarantee indexed by which evidence is present. #29 extends it beyond MCAR |
| **Source conflict** | **CONTRADICTED** | **#7 Basin et al., RV 2012, peer-reviewed, full text read.** Three-valued L³ with a consensus operator yielding ⊥ exactly where logs conflict, **plus a knowledge-monotonicity theorem**. From 2012. Also #2 (provenance score: similarity to untrusted context minus similarity to trusted prompt), #24 |
| **Measurement reliability** | **CONTRADICTED** | **#19 FiReIQ** conditions per-field confidence on a 390-dimensional image-quality vector of the input itself |
| **Sufficiency decoupled from confidence** | **CONTRADICTED** | **#13 SURE-RAG** keeps a sufficiency classifier *architecturally separate* from an uncertainty penalty — exactly the separation the candidate proposes, already built and ablated. **#14 RINSE** scores sufficiency from question + evidence alone, explicitly not from generator confidence. **#21** uses an autorater independent of model output |
| **Staleness / recency / delay** | **SUPPORTED** | **No method was found whose admissibility decision is conditioned on measured data recency.** The only candidate is **#18 Shraga et al.** (preprint): per-approval validity horizons from safe-side margin and feature volatility, verdict-change rates 5.3–48.4% at an 8-step replay shift, **no formal guarantee**. #16 names freshness as one of four axes but **explicitly leaves the mapping from sufficiency to action out of scope**. #25 lists staleness in a graded composite but **was read only via press release** |
| **The combination as one admissibility criterion** | **SUPPORTED** | Across 33 verified sources, none fuses missingness + staleness + delay + conflict + reliability into a single sufficiency notion governing output admissibility. #17 fuses five signals and #19 two, but both fuse confidence *with* evidence rather than building a pure evidence criterion. **#16 has the richest evidence model (four axes including freshness) and no output-side consequence at all** |

**Honest assessment.** G2's general form is **occupied**, and the project should expect to be told so. What survives is narrow: **staleness as a measured admissibility condition, and the fusion of heterogeneous evidence-quality axes into one criterion with an output-side consequence.** "Nobody has combined these three things" is a weak novelty claim on its own, and the adjudication rule above forbids counting it as more than it is.

---

## G3 — **Different** evidence requirements for **different** output types in one system

**Claim under test.** *No existing system applies distinct evidence requirements to distinct output types.*

### Verdict: **CONTRADICTED**, and most decisively by a non-ML source

| Deciding source | Status | What it does |
|---|---|---|
| **#8 USPSTF Grade Definitions** | official methods, full text read | **The decisive instance.** Grade A requires high certainty of substantial net benefit; B admits two certainty/magnitude combinations; C requires "at least moderate certainty" of small net benefit; D requires "moderate or high certainty" of no net benefit or harm; **Grade I is triggered when evidence is "lacking, of poor quality, or conflicting"** and carries no practice suggestion at all. **Different output categories, different evidence requirements, with the insufficiency case withholding the category.** That *is* evidence-sufficiency-conditioned output admissibility |
| **#5 Sadinle, Lei, Wasserman** | *JASA* 2019, peer-reviewed | Explicit per-class error levels **α_y** with finite-sample distribution-free guarantees. Oldest instance found. The requirement is a *risk budget*, not an *evidence* requirement, and the output space is labels in one space |
| **#2 Role-Stratified CRC** | preprint, Jul 2026 | **The closest single threat.** Per-role risk budgets α(r), tighter for higher-risk roles, with an **input-evidence (provenance)** admissibility score. Category-differentiated requirements *and* evidence-based admissibility, in one system |
| **#9 GRADE 14** | peer-reviewed | Four-way output space — strong / weak / research-only / none — selected partly by certainty |

**Two points that cut in the project's favour and must not be overstated.**

First, **GRADE's official posture is *against* withholding.** It "encourage[s] panels to make recommendations even when confidence in effect estimate is low", warning that declining leaves users "without the guidance they are seeking", and the Handbook states strong recommendations "can result from low or even very low confidence in effect estimates". So the mature tradition **litigated whether evidence insufficiency should gate output category and came down largely on "attach a qualifier instead"**. The deployed commercial form (UpToDate 1A–2C) has **no insufficiency category at all**. That is a genuine argument that the gating design is contested rather than settled — but it is an argument about *desirability*, not about *novelty*.

Second, **the clinical analogy breaks on level and mechanism.** USPSTF and GRADE operate on a body of published literature, at authoring time, aggregate and population-level, assessed by a human panel over months. They have no machinery for staleness, delay or per-instance conflict, no computational representation, and no formal guarantees. The candidate problem is **per-case and at runtime**. That distinction is real — but it is a distinction of level and mechanism, **not of idea**, and a reviewer will say so.

---

## G4 — Emergent: **evidential reachability** distinguished from **evidential support**

This gap was not in the brief. It emerged from the adjudication and is the only one that survives on structural rather than incidental grounds.

**Claim under test.** *All existing abstention work treats the question as "should this output be emitted?", presupposing that the output is derivable from the available evidence. None distinguishes:*

- **(i) evidential reachability** — whether an output type is **derivable at all** from the available evidence class, independent of any confidence or risk budget; from
- **(ii) evidential support** — whether, given reachability, the derivation is **warranted by information beyond a trivial baseline**.

### Verdict: **SUPPORTED**, with two named formal antecedents that must be positioned against

| Antecedent | How close | Where it stops |
|---|---|---|
| **#6 Bauer, Leucker, Schallhart — monitorability (TOSEM 2011)** | **Very close on (i).** Monitorability *is* a reachability concept: an "ugly" prefix yields "?" forever, so no continuation can ever decide — a provable statement that the required evidence is unobtainable. Lemma 3.8 proves monitorable ⊋ safety ∪ co-safety | Concerns **one property's decidability under any continuation**, not which of several output types a given evidence class can derive. **No notion of (ii)** — insufficiency is logical and binary, with no "present but stale", "present but unreliable", or "60% sufficient" |
| **#7b Gorostiaga & Sánchez — finite dismissibility/admissibility** | **Closest overall.** Classifies which **individual verdict values** can be ruled out from a finite, imperfect observation, with imprecise observation functions for lost prefixes | Within **one property's verdict domain**. No graded support notion. Venue and year not stated in the PDF; **peer-review status unconfirmed** |
| **#1 AC-RAC** | Eliminates actions whose worst case over the plausible-label set collapses | That is a **utility** elimination over a confidence-derived set, not a reachability statement about evidence classes. AC-RAC assumes every action is derivable and asks which is safe |
| **#22 Erokhin** (peer-reviewed) | — | **A clean negative that supports G4:** across five availability-aware strategies the output label set never changes, only the model behind it. The sensor-robustness tradition does not ask whether an output type is reachable |

**Why "reachable but unsupported" is the formal object.** It is absent from all 33 verified sources. Prior art has: *emit or abstain* (confidence), *emit with a risk budget* (#1, #2, #5), *emit a qualifier* (UpToDate), *withhold the category* (#8), and *cannot decide* (#6, #7). It does not have **"this type can be produced from what is available, and producing it would not be warranted"** — a state distinct from both "cannot produce" and "unconfident".

**A worked empirical instance already exists in this project**, produced for an unrelated purpose, which is the strongest available evidence that the distinction is measurable rather than merely stateable (`research/non-degeneracy/causal/causal-replication-results.md`):

| Output type | Evidence class = concurrent observation only | Operationalisation |
|---|---|---|
| `DepartureTime` | **Unreachable.** Rate **exactly 0.00%** over 7,305 episodes — the rule requires a strictly better later hour, and persistence predicts every later hour equal to the present, so the predicate can never be satisfied | reachability = the predicate is unsatisfiable under the evidence class |
| `Duration` | **Reachable (69.68% of episodes) but unsupported.** Step residual against the episode-specific margin **exactly 0.000000**; base R² **exactly 1.000000**; calendar contribution **0** | support = residual information beyond a deterministic function of the present |
| `Duration` under a forecast surrogate | **Reachable and supported.** Ten distinct run lengths, 24.65% unexplained, calendar explaining 31.5% of residual | — |

**The exactly-zero residual is what makes this a test rather than an intuition**: under a trivial baseline, the support statistic is zero by construction, not merely small.

**Caveats that keep G4 honest.**

1. **It is a distinction plus an operationalisation, not yet a method.** To be a CS contribution it needs a formal definition, a decision procedure, a guarantee, and an evaluation showing it changes outcomes against #1.
2. **Monitorability is a genuine antecedent for (i)** and the project has **already conceded Bauer et al. 2011** (§0). So (i) cannot be claimed as new; the claim must rest on **(ii) and the (i)/(ii) separation**.
3. **One verified source could overturn it**: #7b, if its finite-dismissibility machinery turns out to include a graded support notion. Its full positioning has not been done, and its venue is unknown.

---

## Summary of adjudications

| Gap | Verdict | Decided by | What survives |
|---|---|---|---|
| **G1** category-level restriction | **CONTRADICTED** | #1 (ICML 2026, peer-reviewed), #2, #8, #15 | Only that per-type thresholds in prior art are calibration artifacts or risk budgets, not requirements derived from what the type needs. A refinement of #1 |
| **G2** evidence-conditioned admissibility | **PARTIALLY SUPPORTED** | occupied by #3 (ICML 2023, peer-reviewed), #7 (RV 2012, peer-reviewed), #19, #13, #14 | **Staleness** as a measured admissibility condition; and the fusion of heterogeneous evidence axes with an output-side consequence |
| **G3** per-type evidence requirements | **CONTRADICTED** | #8 USPSTF Grade I; #5 (*JASA* 2019); #2 | Only the runtime, per-instance level — a distinction of level and mechanism, not of idea |
| **G4** reachability vs support | **SUPPORTED** | absent from all 33 sources; antecedents #6, #7b positioned | The (i)/(ii) separation, the "reachable but unsupported" state, and a measurable support statistic that is exactly zero under a trivial baseline |

**One gap survives, and it is not one of the three the brief proposed.** G1 and G3 are occupied by peer-reviewed work, one of it four months old. G2 survives only in a narrow strip. G4 survives on structural grounds and has a worked instance — but it is a formal distinction in need of a method, two of its antecedents are strong, and one of them is already conceded in the project's own frozen literature position.
