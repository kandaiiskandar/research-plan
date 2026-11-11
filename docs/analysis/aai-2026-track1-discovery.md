# Discovery Report — AAI 2026 Track 1 Fit

**Date:** 2026-09-23
**Task:** Discovery only. No manuscript drafted. No research reframed. No novelty invented.
**Authoritative source:** `experiment-report-delta-l2.md` (RQs, design, results, contribution, limitations, non-claims). Terminology and claim boundaries preserved.
> ### ⚠️ Revision note — 2026-09-23, after a complete reading of the authoritative report
> This report was first drafted having read only §§3, 4, 5.2, 6, 7.3 and 7.4 of `experiment-report-delta-l2.md`. A subsequent full reading corrected the following. **Sections below carry the corrected values.**
>
> | # | First draft said | The report actually says |
> |---|---|---|
> | 1 | Headline is "robust"/"stable across the tested envelope" | 🔴 **Wrong.** Sourced-threshold envelope **5.67–9.56%**; wave ±0.25 m → **2.54–14.75%**. The report calls it *"a point on a steep gradient rather than a stable site property"* |
> | 2 | Sensitivity summarised by the 0.48-pt rainfall result | 🔴 **Misleading.** Rainfall is the *minimal* component; **wave is dominant** at ≈−1.4 pts per 0.05 m |
> | 3 | Component attribution "not load-bearing", USE IF SPACE | 🔴 **Wrong.** `g_o` binds **97.6%**; three of five never bind. §10 names these negative findings part of the **primary** contribution |
> | 4 | R4 — the G/A_AI separation "collapses", UNRESOLVED | ⚠️ **Overstated.** The report's claim is separation from *a single graduated index*, which is supported. Softened to PARTIAL |
> | 5 | 12 objections | ⚠️ **Incomplete.** Three were missing: single-component dominance (R13), vessel-class near-vacuity (R14), denominator policy (R15) |
>
> Findings **unchanged** by the full reading: the Track 1 fit assessment, the four executive findings in §1, the terminology audit, and the recommended paper identity. The sensitivity correction **strengthens** the case for Centre F — see RQ-β.

**Companion:** `aai-2026-track-fit-analysis.md` (all five tracks). This report tests **Track 1 specifically** and reaches a **more sceptical conclusion** than that document — §3 explains why.

---

## 1. Executive finding

**The research does not comfortably belong under Knowledge Representation, Reasoning & Decision Intelligence, and three specific findings from the literature are responsible.**

1. **A_AI(S) is a textbook construct, not a representational contribution.** A state-conditioned admissible action set is the standard `A(s)` of Markov decision process theory — present in Puterman and in every MDP treatment since the 1950s. Representing "which actions are available in which state" as a finite state→set mapping is not a knowledge-representation advance. It is a lookup table over three states.

2. **The pre-inference distinction is already established — and named.** Alshiekh et al. (AAAI 2018) distinguish **preemptive** shielding, where "the shield acts each time the learning agent is about to make a decision and provides a list of safe actions", from **post-posed** shielding, which "monitors the actions from the learner and corrects them only if the chosen action causes a violation". That is precisely the pre-inference-versus-post-hoc-filtering distinction this project treats as a differentiator. **It is prior art and must be conceded**, consistent with `MECHANISM_NOVELTY = WITHDRAWN`.

3. **No reasoning system is evaluated anywhere in the experiment.** The replay runs a deterministic threshold classifier over 43,848 hours of reanalysis data. No AI is invoked, no advice is generated, no inference occurs. For a track whose subject is *reasoning*, the evaluation does not touch the object the track cares about.

A fourth finding is internal to the specification rather than the literature, and is the most serious of the four for reviewers: **G(S) is derivable from A_AI(S).** Across all three states, `G(S) = 1 ⟺ A_AI(S) ≠ ∅`. The "separation of participation from advisory scope" — presented as the central conceptual move — **collapses in the instantiated mapping**, where G carries no information the admissible set does not already carry. See §12, objection R4.

**What this does not mean.** It does not mean the research is weak, and it does not mean there is no AAI paper. It means the *defensible* contribution is **empirical and specificational**, not representational. A Track 1 submission is possible on one narrow framing (§5, Centre C+D), but it will be read by reviewers whose primary interests — ML, generative models, agentic systems, formal reasoning — this work does not engage. **Track 3 (Responsible, Ethical & Human-Centred AI) remains the better-matched home**, for the reasons in the companion analysis and reinforced here.

---

## 2. What the existing research actually contributes

After `MECHANISM_NOVELTY = WITHDRAWN` and the non-claims in §4 of the task, this is what survives. Each line is evidenced.

| # | Surviving contribution | Evidence | Strength |
|---|---|---|---|
| 1 | **An empirical activation rate for an intermediate governance level**, measured by replay over a multi-year record | Δ_L2 = 5.81% / 4.48%; C0↔C1 = 42.88%, C0↔C2 = 48.69% | **Strongest** |
| 2 | **A comparator design that isolates the marginal contribution of one governance level** | C0–C3 ladder; C1↔C2 direct = 5.81% cross-check | **Strong** |
| 3 | **A structural negative result**: a three-state topology without scope restriction is governance-identical to a binary gate | P4; C1↔C3 = 0.00% by construction | **Strong, underused** |
| 4 | **An explicit interpretive identity limiting what the headline measures** | Δ_L2 ≡ P(S=CAUTION), verified from `condition_comparison.py` to <1e-9 | **Strong, honest** |
| 5 | **A disclosed sensitivity envelope**, showing the headline is wave-dominated and *not* a stable site property | Envelope **5.67–9.56%** PRIMARY (4.26–6.64% RESOLUTION); wave onset ≈ **−1.4 pts per 0.05 m**; ±0.25 m moves it **2.54%–14.75%** | **Strong as disclosure, weak as robustness** |
| 6 | **An operational specification that stays total when a required component is structurally unavailable** | P1 (Thm C.1, C.1b, Cor C.1b.1); D = {m}; g(⊥) = UNSAFE; lower-bound consequence | **Moderate** |
| 6b | **Negative findings on component warrant** — the five-component state is not empirically warranted at this site | `g_o` binds **518/531 = 97.6%** of CAUTION hours; `g_r` 2.4%; `g_w`, `g_t`, `g_m` never bind; wind a structural zero | **Strong — and named in §10 of the report as part of the PRIMARY contribution** |
| 6c | **Pre-registered prediction methodology** | `data/prediction-register.csv` P01–P24; P21–P24 registered before the comparison ran; 15 CONFIRMED / 9 REFUTED | **Moderate, unusual, currently unused** |
| 7 | Conformance of implementation to the governance contract | P1–P3; bounded executable conformance | **Moderate; not novel theory** |
| 8 | A composition gap across three unrelated fields | Gap A, self-described in the report as "a modest composition gap… not an architecture gap" | **Weak — the report already discounts it** |

**Contributions 1–5 are empirical and methodological. 6–8 are specificational.** Nothing in this list is representational or inferential, which is the root of the Track 1 difficulty.

> The report's own framing of Gap B is the honest centre: *"no empirical characterisation was identified of how often an intermediate advisory-scope state changes the admissible recommendation set relative to a participation-only gate, when replayed over a multi-year environmental record."* The report adds: **"It could have returned a null result."** That is the mark of a real empirical question, and it is the best claim available.

---

## 3. Track 1 literature fit

### 3.1 Concepts that genuinely correspond to G(S) and A_AI(S)

| Established concept | Primary source | Correspondence |
|---|---|---|
| **State-dependent action set `A(s)`** | Puterman, *Markov Decision Processes* (Wiley); standard in all MDP formalism | **Exact.** A_AI(S) *is* A(s) over a three-element state space |
| **Preemptive shielding** — shield supplies the safe action list before the agent decides | Alshiekh et al., AAAI 2018 | **Exact** for the pre-inference claim |
| **Post-posed shielding** — correct the action after selection | Alshiekh et al., AAAI 2018 | **Exact** for the "post-hoc filtering" contrast |
| **Invalid action masking** | Huang & Ontañón (2022) | **Close.** Same operation, learning-specific treatment |
| **Runtime verification / totality over incomplete observations** | Bauer, Leucker & Schallhart (2011); Taleb, Hallé & Khoury (2023) | **Exact** for P1 — already in the corpus |
| **Advisory-type inhibition on external state** | FAA AC 20-151C (TCAS II); TSO-C151c §5.6 (TAWS) | **Exact** for the mechanism — already conceded |
| **Simplex / supervisory safety architecture** | Sha, *The Simplex Architecture for Safe On-Line Control System Upgrades* | **Analogous** — supervisory restriction pattern |
| **ODD exit / Minimal Risk Condition** | Gyllenhammar et al. (2025) | **Analogous** — already in the corpus |
| **Partial identification under declared unmeasured variables** | Manski (1990, 1997); Manski & Pepper (2000) | **Exact** for the lower-bound argument |

### 3.2 The consequence

Every structural element of G(S) and A_AI(S) maps onto an established concept, and **the shielding literature covers the pre-inference/post-hoc distinction directly**. There is no representational or inferential residue left to claim.

### 3.3 The one genuine residue

The shielding and action-masking literature is formulated **for autonomous agents that act** — the shielded object is a policy selecting actions in an environment. No work was located applying shield-style admissible-set restriction to a **human-facing advisory system**, where the restricted object is the *vocabulary of recommendation types offered to a person who retains decision authority*, under structurally unavailable inputs, with the restriction's activation rate measured empirically.

**That transposition is narrow, real, and defensible — and it is a composition-and-characterisation claim, not a mechanism claim.** It is also, notably, *not* a KR&R claim.

### 3.4 Would Track 1 reviewers recognise this as a contribution to their area?

**Probably not, on the current evidence.** A KR&R reviewer would expect a representation language, an inference procedure, a complexity or expressiveness result, or an evaluation of reasoning quality. This paper has a three-row lookup table, no inference, and an evaluation of how often a weather classifier returns its middle value. A *Decision Intelligence* reviewer — if the track supplies one — might be more receptive, but see §4 on that term's standing.

**Honest assessment: Track 1 submission is defensible but disadvantaged.** The paper would be sound and would not be caught out on novelty, because the concessions are already made. It would compete poorly against papers doing reasoning.

---

## 4. Terminology audit

### Category 1 — Supported by literature; safe to use

| Term | Basis |
|---|---|
| **Admissible action set / admissible recommendation set** | MDP `A(s)`; used directly in shielding literature |
| **State-conditioned restriction** | Standard; describes the mechanism accurately |
| **Runtime governance / runtime enforcement** | Runtime verification literature; already in corpus |
| **Advisory-scope containment** | Project's own term, defined and proved (P2) — internally consistent |
| **Fail-safe resolution** | Established; conceded as non-novel |
| **Totality of classification** | Runtime verification (Bauer et al.) |
| **Comparator ladder / isolated level contribution** | Standard ablation methodology |
| **Lower bound under declared exclusion** | Partial identification (Manski) |
| **Graduated governance** | Flehmig et al. (2024); Shamsujjoha et al. (2025) — conceded |

### Category 2 — Approximately related; use only with explicit qualification

| Term | Problem |
|---|---|
| **Shielding** | Accurate as an analogy, but the literature means *agent* shielding. Using it requires stating that this is a human-facing advisory transposition, and citing Alshiekh et al. as prior art |
| **Constrained reasoning** | The system does not reason. The constraint is on a *set offered to* a reasoning layer that is never exercised |
| **Safety envelope** | Control-theoretic connotation of a continuous operating region; here it is three discrete labels |
| **Pre-inference restriction** | Descriptive and true, but **must be attributed** — this is preemptive shielding |
| **Decision intelligence** | Peer-reviewed grounding is thin. The literature is dominated by practitioner and vendor sources. Usable because AAI names it in the track, but it should not carry a novelty claim |

### Category 3 — Avoid

| Term | Why |
|---|---|
| **Knowledge representation** | A three-row table is not a KR contribution. Claiming it invites the objection that ends the review |
| **Agentic / agent governance** | No autonomy, no tool use, no planning loop. Unsupported and exactly the trend-chasing to avoid |
| **Reasoning architecture / reasoning governance** | No inference is performed or evaluated |
| **Novel / first / new mechanism** | Withdrawn by the locked chain |
| **Safe, safer, safety-improving** | Explicit non-claim |
| **Optimal, validated, correct (of A_AI(CAUTION))** | Explicit non-claim; the identity in §7.3 forbids it |
| **Human-centred** | No contextual validation has been conducted |
| **Intelligent decision support** *(as the paper's claim)* | Invites the applied-domain reading and duplicates IPoSCI |

---

## 5. Candidate scientific centres

*Presented without ranking, per the task.*

### Centre A — Representation: separating participation from admissible advisory scope

- **Question.** Can AI participation and admissible advisory scope be represented as two separately specified state-conditioned functions?
- **Actual novelty.** **Very low.** A(s) is textbook; and **G is derivable from A_AI in the instantiated mapping** (§12 R4), so the separation is not exercised by the evidence.
- **Evidence supporting.** The specification; P1–P3.
- **Evidence missing.** Any instance where G and A_AI vary independently. Any demonstration that the separation changes an outcome.
- **Track 1 relation.** Nominally the closest to KR — and the weakest on inspection.
- **IPoSCI overlap.** **High.** The abstract already presents G(S), A_AI(S) and the three-state table.
- **Six pages?** Yes, easily — but there would be little to fill them with.

### Centre B — Reasoning constraint: state-conditioned restriction before inference

- **Question.** Should the admissible recommendation set be supplied to the reasoning layer before inference rather than filtered afterwards?
- **Actual novelty.** **None as a mechanism** — preemptive vs post-posed shielding, Alshiekh et al. 2018. Residual novelty only in the human-facing advisory transposition (§3.3).
- **Evidence supporting.** Architectural specification; bounded executable conformance.
- **Evidence missing.** **Decisive.** No inference is ever run, so no evidence exists that pre-inference restriction behaves differently from post-hoc filtering *in this system*. The claim is asserted, not tested.
- **Track 1 relation.** The most *thematically* Track 1 centre and the least *evidenced*.
- **IPoSCI overlap.** Low.
- **Six pages?** Yes — but see §14; it needs an analysis that does not yet exist.

### Centre C — Empirical characterisation: how often the intermediate restriction binds

- **Question.** Over a multi-year environmental record, how frequently does an intermediate safety state produce a stricter admissible recommendation set than a participation-only gate, and how robust is that frequency?
- **Actual novelty.** **Genuine.** This is Gap B, which the report states could have returned a null result. No comparable characterisation was located.
- **Evidence supporting.** Complete — Δ_L2 = 5.81% / 4.48%, the 42.88% / 48.69% decomposition, sensitivity, component attribution, common-period comparison, the Δ_L2 ≡ P(S=CAUTION) identity bounding interpretation.
- **Evidence missing.** **None for the question as posed.** Generalisation beyond the site is an explicit non-claim, not a gap.
- **Track 1 relation.** **Weak.** This is measurement, not reasoning.
- **IPoSCI overlap.** Moderate on the headline numbers, **low** on the decomposition, sensitivity and identity — none of which the abstract contains.
- **Six pages?** **Yes, comfortably.** This is the best-proportioned centre.

### Centre D — Comparator methodology: isolating one governance level with C0–C3

- **Question.** How can the marginal contribution of a single governance level be isolated from a multi-level governance design?
- **Actual novelty.** **Moderate and under-argued.** The ladder plus two results that follow from it — C1≡C3 at 0.00%, and Δ_L2 ≡ P(S=CAUTION) — constitute a small methodological package for evaluating governance designs.
- **Evidence supporting.** Full: the ladder, the subtraction, the independent pairwise cross-check, P4.
- **Evidence missing.** Demonstration on a second governance design. Without it the method is exhibited once, not established.
- **Track 1 relation.** **Weak** directly; stronger if framed as evaluation methodology for decision systems.
- **IPoSCI overlap.** **Lowest of all centres.** Entirely absent from the abstract.
- **Six pages?** Yes.

### Centre E — Formal governance: properties and contract conformance

- **Question.** Does the implementation provably conform to its governance contract, including when a required component is unavailable?
- **Actual novelty.** **Low by declaration.** P1–P4 are explicitly "not offered as new theory"; P2 is "true by definition".
- **Evidence supporting.** Complete proofs, Appendix C.
- **Evidence missing.** Nothing — but nothing here is claimed as new either.
- **Track 1 relation.** Moderate; formal methods are recognisable to KR reviewers.
- **IPoSCI overlap.** Low.
- **Six pages?** Only as a component. Alone it is a page of definitions and four properties the authors already disclaim.

### Centre F — *(identified by this analysis)* Structural adequacy of governance topology

- **Question.** Does adding an intermediate state to a governance topology change governance behaviour, or only the labelling — and how is the difference detected?
- **Actual novelty.** **Genuine and currently buried.** The pairing of P4 (C1≡C3 structurally, 0.00% empirically) with Δ_L2 = 5.81% (C2 differs) makes a clean, generalisable point: **a three-state governance design does nothing unless the intermediate state restricts scope.** That is a transferable design finding, not a fisheries result.
- **Evidence supporting.** P4; C1↔C3 = 0.00%; C1↔C2 = 5.81%; the identity.
- **Evidence missing.** Second design instance for generality.
- **Track 1 relation.** Moderate — a statement about decision-policy structure.
- **IPoSCI overlap.** **None.**
- **Six pages?** Yes, and it pairs naturally with C.

> **Observation.** Centre F is the most interesting thing in the evidence and currently appears only as a consistency check. "The traffic-light comparator contributes exactly nothing, and here is the structural reason why" is a sharper claim than "our intermediate state activates 5.81% of the time."

---

## 6. Candidate research questions

Each shown as **RQ → Method → Evidence → Result → Claim permitted**. Flags mark anything the existing evidence cannot fully answer.

### RQ-α — Activation frequency and robustness ✅ fully answerable

> Over a multi-year environmental record for one deployment site, how frequently does an intermediate safety state produce a stricter admissible recommendation set than a participation-only gate, and how sensitive is that frequency to defensible threshold and data configurations?

- **Method.** Retrospective replay of C0–C3 over hourly reanalysis; subtraction to isolate Level 2; one-at-a-time and combined-grid threshold sensitivity; common-period comparison.
- **Evidence.** 43,848 / 28,501 hourly records; 9,135 / 5,935 departure-window hours; Δ_L2 = 5.81% / 4.48%; sourced-threshold envelope **5.67–9.56%**; wave onset ≈ −1.4 pts per 0.05 m; component attribution.
- **Result.** The intermediate restriction binds in 5.81% of evaluated hours (4.48% alternative), **non-vacuous across every sourced small-vessel configuration but strongly wave-dependent** — the report's own words: *"a point on a steep gradient rather than a stable site property."*
- **Claim permitted.** The intermediate level changes the admissible recommendation set at a measurable and **never-vacuous** rate at this site for these mappings, with a disclosed envelope. 🔴 **Do NOT claim stability or robustness.** Nothing about safety, quality or optimality.
- **Note.** This is RQ2 of the authoritative report, narrowed. It is the safest RQ available.

### RQ-β — Structural adequacy of the topology ✅ fully answerable

> Does adding an intermediate state to a governance topology change governance behaviour, or only its labelling — and what distinguishes the two cases?

- **Method.** Contrast C3 (three states, no scope restriction) against C1 (binary) and C2 (three states with scope restriction).
- **Evidence.** P4; C1↔C3 = 0.00% by construction and confirmed in replay; C1↔C2 = 5.81%.
- **Result.** A three-state topology is governance-identical to a binary gate unless the intermediate state restricts admissible scope. State count alone changes nothing.
- **Claim permitted.** A structural statement about governance topology, demonstrated on one design. Transferable as a **design caution**, not as a general theorem. Must be presented as **entailed by the comparator definitions**, not discovered — the report is explicit that the 0.00% "follows from the comparator definitions rather than from the data" and that P21 "functions as a regression lock on the encoding rather than as a test of the site data."
- **Note.** Centre F. The least IPoSCI overlap of any RQ. **And — established only on the full reading of §8–9 — it is the one claim in the paper that is invariant to the threshold sensitivity.** Every empirical figure sits on a steep wave gradient (5.67–9.56%, or 2.54–14.75% under ±0.25 m). C1 ≡ C3 = 0.00% holds **on any trace, under any threshold configuration**. That invariance is now the strongest argument for making it the centre.

### RQ-γ — What the activation measure does and does not identify ✅ fully answerable

> What property of a graduated governance design does an activation-rate measure actually identify?

- **Method.** Derive the identity from the C1/C2 mappings; verify numerically against implementation.
- **Evidence.** Δ_L2 ≡ P(S = CAUTION), verified from `condition_comparison.py` to <1e-9 on every run.
- **Result.** The measure identifies the intermediate-state base rate and is **invariant to the content of A_AI(CAUTION)** — any strict subset of FULL yields the same value.
- **Claim permitted.** A methodological caution for anyone evaluating graduated governance: activation rate measures classifier behaviour, not restriction design.
- **Note.** Turns the headline's principal weakness into a stated result. Strong under peer review; pairs with RQ-α.

### RQ-δ — Total classification under structurally unavailable components ✅ answerable, modest

> Can a governance classifier remain total and preserve advisory containment when a conceptually required component is structurally unavailable, and what interpretive consequence follows?

- **Method.** Declared exclusion set D = {m}; fail-safe g(⊥) = UNSAFE; proofs P1, P2; partial-identification argument.
- **Evidence.** Theorem C.1, C.1b, Corollary C.1b.1; Theorem C.2, Corollary C.2.
- **Result.** Classification stays total; containment preserved; the reported rate is a **lower bound**.
- **Claim permitted.** Conformance and a directional bound. **Not** new theory — the report disclaims it.
- **Note.** Best as a supporting subsection, not a paper centre.

### RQ-ε — Pre-inference restriction versus post-hoc filtering ⚠️ **FLAGGED — not answerable on existing evidence**

> Does supplying the admissible recommendation set to the reasoning layer before inference differ observably from filtering generated advice afterwards?

- **Method required.** Run an advisory layer under both regimes and compare observable behaviour.
- **Evidence available.** Architectural specification; bounded executable conformance that no inadmissible type was emitted.
- **Evidence missing.** 🔴 **No inference is performed anywhere in the experiment.** Nothing distinguishes the two regimes empirically. Additionally, Alshiekh et al. (2018) already establish the distinction conceptually, so a conceptual-only treatment adds nothing.
- **Claim permitted today.** Only that the implementation never emitted an inadmissible recommendation type under the configured contract. **The comparative claim is unsupported.**
- **See §14** for the smallest analysis that would change this.

### RQ-ζ — Comparator methodology ⚠️ partially answerable

> How can the marginal contribution of a single level in a multi-level governance design be isolated?

- **Evidence available.** The C0–C3 ladder and its two derived results, demonstrated once.
- **Evidence missing.** A second governance design. A methodology exhibited on one instance is an example, not a method.
- **Claim permitted.** "We use this design and it isolates the level cleanly" — not "we contribute a general methodology".

---

## 7. Candidate titles

For each: what it promises · whether the evidence delivers · reviewer expectation created · IPoSCI overlap risk.

**Empirical-characterisation family**

1. **"How Often Does an Intermediate Governance State Bind? A Multi-Year Replay of Graduated Advisory-Scope Restriction"**
 *Promises* an activation-frequency measurement. *Evidence* fully delivers. *Expectation*: a careful empirical study — correctly set. *Overlap*: low; the abstract reports the number without the question.

2. **"Measuring the Marginal Contribution of an Intermediate Level in Graduated AI Governance"**
 *Promises* isolation of one level's contribution. *Delivered* by the C0–C3 subtraction. *Expectation*: comparator rigour — met. *Overlap*: low.

3. **"Activation Frequency of Graduated Advisory-Scope Restriction Under Historical Environmental Conditions"**
 *Promises* exactly what was measured. *Delivered.* *Expectation*: modest, accurate. *Overlap*: low. Dry but unimpeachable.

**Structural / negative-result family**

4. **"Adding a State Is Not Adding Governance: Structural Equivalence of Three-State and Binary Advisory Gating"** ⭐
 *Promises* a structural finding with a negative result. *Delivered* by P4 and the 0.00% / 5.81% contrast. *Expectation*: a crisp claim with a clean demonstration — met. *Overlap*: **none**. The strongest title on novelty-per-page.

5. **"When Does an Intermediate Safety State Change Anything? Topology Versus Scope in Graduated Governance"**
 *Promises* the same finding, framed as a question. *Delivered.* *Overlap*: none.

**Formal-specification family**

6. **"An Operational Contract for Participation and Advisory Scope Under Structurally Unavailable Inputs"**
 *Promises* a specification contribution. *Partially delivered* — the contract exists and is proved, but P1–P4 are disclaimed as non-novel, and **G is derivable from A_AI**, so "participation and advisory scope" oversells the separation. *Expectation*: formal novelty — **not met**. *Overlap*: moderate. ⚠️ Risky.

7. **"Total Classification and Advisory Containment Under Declared Component Exclusion"**
 *Promises* conformance under missing inputs. *Delivered*, but narrow. *Expectation*: a formal-methods paper — the evidence is thin for that audience. *Overlap*: low.

**Methodological family**

8. **"A Comparator Ladder for Isolating Governance-Level Contributions in AI Decision Support"**
 *Promises* a reusable method. **Not delivered** — demonstrated once only. ⚠️ Overclaims.

9. **"What an Activation-Rate Measure Identifies in Graduated AI Governance"**
 *Promises* a methodological clarification. *Delivered* by the identity. *Expectation*: a short, sharp analysis paper — well matched. *Overlap*: none.

**Decision-intelligence / governance family**

10. **"State-Conditioned Admissible Recommendation Sets for Human-Facing Decision Support"**
 *Promises* a representational contribution. **Not delivered** — this is A(s). *Expectation*: KR novelty — **fails immediately**. ⚠️ Avoid.

11. **"Graduated Advisory-Scope Governance for AI Decision Support in Coastal Fisheries"**
 🔴 **This is effectively the IPoSCI title.** Avoid entirely.

12. **"Runtime Restriction of Advisory Scope in Human-Facing AI Decision Support: Specification and Empirical Characterisation"**
 *Promises* specification plus measurement. *Delivered* on both. *Expectation*: balanced — met. *Overlap*: low-moderate. A safe compound title.

### The three most accurate

- **#4** — *Adding a State Is Not Adding Governance* — highest novelty per page, zero IPoSCI overlap, and the claim is fully proved and measured.
- **#1** — *How Often Does an Intermediate Governance State Bind?* — the safest honest framing of the primary evidence.
- **#9** — *What an Activation-Rate Measure Identifies* — converts the headline's weakness into the contribution; the most methodologically mature option.

---

## 8. Evidence map

| Claim the paper might make | Evidence | Status |
|---|---|---|
| Intermediate restriction binds 5.81% / 4.48% | Replay, 9,135 / 5,935 window hours | ✅ Complete |
| Level-2 isolated by subtraction | 48.69% − 42.88% = 5.81%; pairwise cross-check | ✅ Complete |
| Three-state topology without scope ≡ binary | P4; 0.00% | ✅ Complete |
| Headline is invariant to A_AI(CAUTION) content | Identity verified <1e-9 | ✅ Complete |
| ~~Robust to threshold configuration~~ → **Sensitivity envelope disclosed** | 5.67–9.56%; wave ±0.25 m → 2.54–14.75% | ✅ Complete — but supports **disclosure**, not robustness |
| Rainfall boundary is not the driver | 0.48 pts PRIMARY / 0.78 RESOLUTION | ✅ Complete |
| **Wave onset is the dominant determinant** | ≈ −1.4 pts per 0.05 m | ✅ Complete |
| **Five-component state not empirically warranted at this site** | `g_o` 97.6%; three of five never bind | ✅ Complete — RQ3 negative result |
| Headline is vessel-class specific | Medium **1.96%**, large **1.26%** (0.66% / 0.37% RESOLUTION) | ✅ Complete — near-vacuity for larger classes |
| Denominator policy materially moves the headline | Daylight-only denominator → **9.59% / 7.40%** | ✅ Complete |
| Classification total under D = {m} | P1, Thm C.1/C.1b/Cor C.1b.1 | ✅ Complete |
| Reported rate is a lower bound | Declared exclusion + Manski | ✅ Complete |
| Implementation conforms to contract | P3; bounded executable conformance | ✅ Complete |
| Wave-model vs record-length attribution | Common-period: +1.97 / −0.64 pts | ✅ Complete |
| **Pre-inference ≠ post-hoc filtering, observably** | — | 🔴 **Absent** |
| **G and A_AI are independent controls** | — | 🔴 **Absent** (they are not, as instantiated) |
| **Comparator ladder is a general method** | One instance | ⚠️ Partial |
| A_AI(CAUTION) = {Go, Delay} is correct/optimal | Domain rationale only (Gao 2024; Rahim et al. 2024) | 🔴 Non-claim |
| Any safety, accuracy or decision-quality outcome | — | 🔴 Non-claim |
| Generalisation beyond site / vessel class | — | 🔴 Non-claim |

---

## 9. What belongs in the 6-page paper

Assumes the recommended identity in §15 (RQ-α + RQ-β + RQ-γ).

| Item | Verdict | Why |
|---|---|---|
| Complete E definition | **USE IF SPACE** | Name the six components in one line; the full definition is not load-bearing |
| Complete threshold table | **USE IF SPACE — but the wave onset MUST appear** | ⚠️ Revised. With `g_o` binding 97.6% of CAUTION hours and the headline moving ≈1.4 pts per 0.05 m, the wave threshold is the single most consequential number in the paper. Omitting the full table is fine; omitting the wave onset and its source is not |
| SAFE/CAUTION/UNSAFE + A_AI table | **MUST INCLUDE** | The object of the entire paper. One small table |
| G(S)/A_AI(S) formalisation | **MUST INCLUDE — but compressed to ~4 lines** | Needed to state the claim; **do not build the paper on the separation** (§12 R4) |
| P1 Totality | **USE IF SPACE** | Supports the lower-bound argument; one sentence plus citation to the report |
| P2 Containment | **USE IF SPACE** | "True by definition" — state, do not prove |
| P3 Safety Dominance | **OMIT** from the body | Conformance, not contribution. One clause in Evaluation |
| **P4 C1≡C3** | **MUST INCLUDE** | Carries RQ-β, the highest-novelty claim |
| **C0–C3 comparator design** | **MUST INCLUDE** | The method; without it no result is interpretable |
| 43,848-record dataset description | **MUST INCLUDE — compressed** | Site, period, source, denominator. Four lines |
| PRIMARY/RESOLUTION comparison | **MUST INCLUDE** | The robustness claim depends on it |
| **5.81% / 4.48%** | **MUST INCLUDE** | The result |
| **Δ_L2 ≡ P(S=CAUTION) identity** | **MUST INCLUDE — stated before the result** | RQ-γ; pre-empts the strongest reviewer attack (§12 R3) |
| Sensitivity analysis | **MUST INCLUDE — the full envelope, not the rainfall figure** | ⚠️ Revised. Report **5.67–9.56%** and wave dominance. Quoting only the 0.48-pt rainfall result would imply a robustness the evidence does not support, and a reviewer checking the sensitivity script would find it |
| Component attribution | **MUST INCLUDE** | ⚠️ Revised. `g_o` 97.6%, three of five never bind — §10 of the report names these negative findings as part of the **primary** contribution, and volunteering them defends against R13 |
| Vessel-class and denominator variants | **USE IF SPACE** | Medium 1.96% / large 1.26%; daylight-only 9.59%. Two rows; pre-empts R14 and R15 |
| Pre-registered prediction methodology | **USE IF SPACE** | P21–P24 registered before the comparison ran; 15 CONFIRMED / 9 REFUTED. Unusual and credible; one sentence |
| Lower-bound argument | **USE IF SPACE** | Two sentences: D = {m}, fail-safe, therefore lower bound |
| Provenance history | **OMIT** | Internal record-keeping. Belongs in the repo, not the paper |
| Four-layer architecture figure | **OMIT** | 🔴 **Highest-overlap item with IPoSCI.** Also the least informative per column-inch |

**Rough budget (6 pages):** Introduction + positioning 0.75 · Related work and concessions 0.75 · Specification 0.75 · Comparator design and method 1.0 · Results incl. identity 1.25 · Discussion, limitations, non-claims 0.75 · References 0.75.

> The concessions paragraph is **not optional**. Alshiekh et al., TCAS II/TSO-C151c, Puterman-style A(s) and the runtime-verification totality results must be cited as prior art in the first page. A reviewer who discovers preemptive shielding *after* reading an undisclosed pre-inference claim will reject. A reviewer who sees it conceded on page 1 reads the rest as disciplined.

---

## 10. Figure/table strategy

**Recommended: 1 figure, 3 tables.**

| # | Item | Content | Why it earns the space |
|---|---|---|---|
| **T1** | Governance contract | States × G(S) × A_AI(S) | Defines the object. Irreplaceable, tiny |
| **T2** | Comparator design | C0–C3 × behaviour at SAFE/CAUTION/UNSAFE | Makes C1≡C3 visible **by inspection** — the reader sees the negative result before it is measured |
| **T3** | Combined results | PRIMARY/RESOLUTION × records × window hours × C0↔C1 · C0↔C2 · Δ_L2 · C1↔C3, plus a sensitivity-envelope row | One table carrying every number the paper claims |
| **F1** | Sensitivity envelope | Δ_L2 against the rainfall boundary across the defensible range, both configurations | The only genuinely visual content; directly answers "your thresholds are arbitrary" |

**Rejected:** architecture diagram (highest IPoSCI overlap, low information density); component-attribution figure (T3 row or one sentence); separate C0–C3 result figure (duplicates T3).

> **T2 is doing the most work.** If a reader can look at the comparator table and see that C1 and C3 have identical admissible sets at every state, the paper's sharpest claim lands before any measurement is presented.

---

## 11. IPoSCI overlap audit

| Element | In IPoSCI abstract | In proposed paper | Risk |
|---|---|---|---|
| Four-layer architecture | ✅ | ❌ omitted | None |
| SAFE/CAUTION/UNSAFE + A_AI table | ✅ | ✅ | 🟠 Unavoidable — it is the object of study. Present as recap, cite the abstract |
| S = f(E), E = {w,r,m,o,v,t} | ✅ | Compressed to one line | 🟢 Low |
| Δ = (N_restricted/N_eval)×100% | ✅ | ✅ | 🟠 Same measure, **new decomposition** |
| **5.81% / 4.48%** | ✅ | ✅ **unchanged** | 🟠 Same numbers — correct and required. Disclose |
| C0–C3 ladder | ❌ | ✅ | 🟢 New |
| C0↔C1 = 42.88%, C0↔C2 = 48.69% | ❌ | ✅ | 🟢 New |
| **C1≡C3 = 0.00%** | ❌ | ✅ | 🟢 **New — core** |
| **Δ_L2 ≡ P(S=CAUTION)** | ❌ | ✅ | 🟢 **New — core** |
| Sensitivity / robustness envelope | ❌ | ✅ | 🟢 New |
| Component attribution | ❌ | Optional | 🟢 New |
| P1–P4 | ❌ | Compressed | 🟢 New |
| Declared exclusion / lower bound | ❌ | ✅ | 🟢 New |
| Fisheries framing as the contribution | ✅ | ❌ **setting only** | 🟢 Deliberately avoided |

**Assessment.** Overlap concentrates in exactly three places — the governance table, the measure definition, and the two headline numbers — and **all three must be retained**, because changing them would mean changing results. The new material (ladder, decomposition, structural equivalence, identity, sensitivity, lower bound) is substantial and is what makes the paper a legitimate extension.

🔴 **Unresolved dependency.** AAI is *not* one of the three IPoSCI publication routes. If the extended abstract defaults to the IPoSCI e-Proceedings it becomes **published prior work**, and this paper must be written and submitted as a disclosed extension. See `aai-2026-track-fit-analysis.md` §0 and §11.

---

## 12. Reviewer attack / falsification

Written as a sceptical Track 1 reviewer. No defence is manufactured; three objections are conceded as unresolved.

### R1 — "Where is the AI?"
**PARTIAL RESPONSE.** The paper studies the *governance layer around* an AI advisory system, not a model. That is a legitimate object of study and the AI-safety literature treats it as such. But the honest answer is that **no AI is present in the evaluation** — the replay exercises a deterministic classifier. The response must be scoped: *"this paper measures a governance mechanism's behaviour, not a model's."* Against a Track 1 reviewer expecting ML content this is a real disadvantage, not a rebuttable misunderstanding.

### R2 — "This is only a rule-based classifier."
**SUPPORTED RESPONSE.** Correct, and stated. The classifier is deliberately deterministic — governance conditioned on a learned component would be harder to certify. The contribution is not the classifier but the measured behaviour of the governance layer built over it, and the structural finding about topology (RQ-β), which holds regardless of how S is produced.

### R3 — "The 5.81% is simply the CAUTION base rate."
**SUPPORTED RESPONSE — and the paper says so first.** Δ_L2 ≡ P(S=CAUTION) is derived, verified to <1e-9, and stated *before* the result. The reviewer is right, and the paper's position is that this is a finding about what activation-rate measures identify, not a concealed weakness. **Strength depends entirely on disclosure order.** Stated first it is rigour; discovered by the reviewer it is fatal.

### R4 — "G(S) and A_AI(S) are not actually independent." ⚠️ **PARTIAL — revised**
Across all three states `G(S) = 1 ⟺ A_AI(S) ≠ ∅`, so G is a derived predicate of A_AI and no evaluated configuration exercises independent variation (G = 1 with A_AI = ∅ — AI present but recommending nothing — is permitted by the framework and never used).

**However, this objection as first drafted overstated the case.** §10 of the authoritative report claims the specification expresses participation and advisory scope as two state-conditioned functions **"rather than a single graduated index"** — the contrast is with a *scalar severity score*, not a claim that G and A_AI vary independently of each other. That narrower claim **is** supported: a scalar index cannot express "participate, but with a reduced vocabulary" without an additional decoding convention.

**Response available:** defend the contrast with a single graduated index, which the specification does establish. **Do not** claim the two functions are independent controls, which the instantiation does not show. Keep the separation as exposition, not as the paper's centre.

### R5 — "The advisory set is researcher-defined."
**SUPPORTED RESPONSE.** Conceded explicitly in the report: A_AI(CAUTION) = {Go, Delay} is a design choice with a domain rationale (Gao 2024; Rahim et al. 2024) that "does not constitute empirical validation, optimality evidence, or evidence of improved safety." The identity in R3 makes the concession costless — **the headline is invariant to that choice**, so the result does not depend on it being right.

### R6 — "Why is this Knowledge Representation or Decision Intelligence?"
🔴 **UNRESOLVED — and this is the decisive Track 1 objection.** A_AI(S) is the standard state-dependent action set A(s) of MDP theory. A three-row lookup table is not a representation contribution. **There is no defence, and none should be attempted.** The paper's honest position is that its contribution is empirical and specificational, which fits the track's *Decision Intelligence* clause loosely and its *Knowledge Representation* and *Reasoning* clauses not at all.

### R7 — "What is new beyond established safety gating?"
**SUPPORTED RESPONSE.** Nothing mechanistically — conceded. What is new is (i) the measured activation rate over a multi-year record, which no located work reports, and (ii) the structural result that state count without scope restriction changes nothing. Gap B is genuine and could have returned null.

### R8 — "What is new beyond the IPoSCI publication?"
**SUPPORTED RESPONSE.** The comparator ladder, the 42.88% / 48.69% decomposition, C1≡C3 = 0.00%, the Δ_L2 identity, the sensitivity envelope, the declared-exclusion lower bound and P1–P4 are all absent from the abstract. The headline numbers are shared and unchanged, which is correct for an extension. **Requires disclosure**, not defence.

### R9 — "Why an AI conference rather than a domain application?"
**PARTIAL RESPONSE.** Defensible only if the paper leads with the governance and topology results and treats fisheries as the setting. If it leads with the application the objection is correct. **This is a writing decision that determines the outcome**, and it is why the architecture figure and the applied framing are omitted in §9.

### R10 — "Does the experiment evaluate reasoning, or only the classifier?"
🔴 **UNRESOLVED — and already conceded by the report.** Limitation 7 states the metric "is computed from the classifier and governance layer alone… the replay does not compare the *content* of generated advice." Δ_L2 is a property of f(E). No reasoning is evaluated because none is performed. **No available evidence answers this**, and for a track named *Reasoning* it is serious. §14 gives the smallest analysis that would partially address it.

### R11 — "Does pre-inference restriction matter if no generated advice is evaluated?"
🔴 **UNRESOLVED.** No advice is generated anywhere. Bounded executable conformance shows no inadmissible type was emitted under the configured contract, which is weaker than the comparative claim. Compounding this, Alshiekh et al. (2018) already establish preemptive-versus-post-posed shielding, so the conceptual claim adds nothing. **Recommendation: drop the pre-inference claim from the paper's contribution**, or run the analysis in §14.

### R13 — "Your five-component state is effectively a one-component state." 🔴 **NEW — was missing**
**PARTIAL RESPONSE, and it must be volunteered rather than defended.** `g_o` binds 518 of 531 CAUTION hours — **97.6%**. `g_r` accounts for the remaining 2.4%. `g_w`, `g_t` and `g_m` never bind at all, and wind is a structural zero across `W_C` 18–25 kn. The report already states this as a **negative answer to RQ3**: the five-component specification "remains defensible as a transferable specification, but the evaluated record does not empirically warrant equal importance of all five components at this deployment site." That is the honest response and it is a finding, not a weakness — **provided the paper states it first.** A reviewer who derives it unaided will read the multi-component framing as padding.

### R14 — "The effect nearly vanishes for other vessel classes." 🔴 **NEW — was missing**
**SUPPORTED RESPONSE, narrowly.** Limitation 3: under the same source's thresholds the intermediate state is reached in **1.96%** (medium) and **1.26%** (large) of departure-window hours — **0.66% and 0.37%** under RESOLUTION, which the report itself calls "approaching vacuity." The claim is explicitly scoped to vessels under 10 GRT and generalisation across vessel classes is an explicit non-claim. The response is that the paper claims a class-specific characterisation — but a reviewer may reasonably read near-vacuity at two of three classes as limiting the finding's interest.

### R15 — "The denominator is a design choice that moves your headline by two-thirds." 🔴 **NEW — was missing**
**PARTIAL RESPONSE.** Classifying non-daylight hours as UNSAFE and retaining them in the denominator is an architectural policy, not a physical or legal determination — COLREGs Rule 20(b) governs navigation lights, not AI abstention. A daylight-only denominator yields **9.59% / 7.40%** against the canonical 5.81% / 4.48%. The policy is disclosed and defensible as conservative, but the headline is **not denominator-invariant** and the paper must report both.

### R12 — "One site, one configuration, no generalisation."
**SUPPORTED RESPONSE.** Explicit non-claim, stated as a limitation. The paper reports a characterisation for one deployment site, not a general rate.

**Summary: 5 supported · 5 partial · 5 unresolved** (revised after full reading of the authoritative report — R4 softened to partial; R13, R14, R15 added). The unresolved ones (R4, R6, R10, R11) are all *Track-1-specific* — they concern representation and reasoning. **None of them threatens the paper's soundness; all of them threaten its fit.** That is the core finding of this report.

---

## 13. Evidence gaps

| Gap | Blocks | Resolvable now? |
|---|---|---|
| No inference is performed or evaluated anywhere | R10, R11, RQ-ε, Centre B | Partially — see §14 |
| G and A_AI never vary independently | R4, Centre A | ❌ No — would require a configuration the design does not contain |
| Comparator ladder demonstrated once | RQ-ζ, Centre D as *method* | ❌ No — needs a second governance design |
| No second site or vessel class | R12 | ❌ No — explicit non-claim, not a defect |
| No contextual validation with fishers | Any human-centred claim | ❌ No — future work |
| `age_i` freshness parameter OPEN | Full specification completeness | ❌ No — do not invent a value |
| `RESOLUTION_PAIRWISE_C0_C1_C0_C2 = PROVENANCE_INCOMPLETE` | Pairwise reporting for RESOLUTION | ❌ Withheld — do not invent |

---

## 14. Minimal additional analysis, if genuinely necessary

**One candidate only.** Everything else in §13 either cannot be resolved before submission or is a declared non-claim.

### The only analysis worth running: an admissibility-conformance contrast over a stub advisory layer

- **Exact question resolved.** Does restriction applied before advice generation differ observably from filtering applied after, in this implementation? (R10, R11, RQ-ε)
- **Data required.** None new. The existing classified state sequence plus a trivial stub advisory generator that emits all four recommendation types.
- **Can current data answer it?** ✅ Yes. The replay already produces the state sequence; only the stub and two harness paths are needed.
- **What it would show.** Under pre-inference restriction the generator is never invoked for inadmissible types; under post-hoc filtering they are generated and discarded. The observable difference — inadmissible types produced and suppressed versus never produced — gives the architectural claim empirical content for the first time.
- **Expected paper value.** **Moderate.** Converts R10/R11 from UNRESOLVED to PARTIAL and makes a Track 1 framing materially more defensible. It does **not** create novelty — Alshiekh et al. still hold priority on the distinction — and it must not be presented as if it did.
- **Achievable before 19 October?** ✅ Yes. Small harness work, no new data, no new modelling.

**Honest caveat.** With a deterministic stub the result is entailed by the architecture, so this is a *demonstration*, not a discovery. It should be reported as executable conformance evidence, not as an experiment with an uncertain outcome. **If it cannot be framed that honestly, do not run it** — a contrived experiment is worse than a conceded limitation.

**Explicitly not recommended:** a second site, a second governance design, fisher validation, any accuracy or outcome measurement, any attempt to evidence the G/A_AI separation. Each is either a non-claim, unachievable before the deadline, or would expand the paper past six pages.

---

## 15. Recommended paper identity

**Centre: RQ-β (structural adequacy) carrying RQ-α (activation rate) and RQ-γ (what the measure identifies).** Centres A and B are excluded — A is textbook and undermined by R4, B is prior art and unevidenced. Centre E supports; Centre D contributes the ladder without claiming to be a method.

**Shape.** A short empirical-and-structural paper: here is a graduated governance contract; here is a comparator design that isolates the intermediate level; the intermediate level binds 5.81% of the time; a three-state design *without* scope restriction binds 0.00% of the time and is structurally identical to a binary gate; and the activation measure identifies the intermediate-state base rate rather than the quality of the restriction. All claims proved or measured, all mechanisms conceded, all non-claims stated.

**Recommended title:** *Adding a State Is Not Adding Governance: Structural Equivalence of Three-State and Binary Advisory Gating* — with #1 and #9 as alternates.

### Track recommendation — stated plainly

**Track 1 is submittable but disadvantaged.** The paper would be methodologically sound and honest, and it would survive a novelty check because the concessions are already made. It would compete against reasoning and learning papers while containing neither. Four of twelve reviewer objections are unresolved and **all four are Track-1-specific**.

**Track 3 — Responsible, Ethical & Human-Centred AI (positioned under *Responsible/Ethical*) remains the better-matched home** for the same paper with the same evidence and no change to its content. Reviewers there recognise governance mechanisms as legitimate objects of study, expect neither a model nor an inference procedure, and treat disciplined non-claims as a virtue rather than a missing result.

**If Track 1 is chosen anyway**, the recommended identity above is the strongest defensible version — provided the concessions appear on page 1, the pre-inference claim is dropped or evidenced per §14, the separation of G from A_AI is not load-bearing, and the identity is stated before the result.

---

THE PAPER IS ABOUT: how much a graduated governance design's intermediate level actually changes the admissible recommendation set, and the structural condition under which adding that level changes anything at all.

THE PAPER IS NOT ABOUT: a new governance mechanism, a knowledge representation, a reasoning procedure, or an AI decision-support system for coastal fisheries.

TRACK 1 FIT DEPENDS ON: whether reviewers accept an empirical and specificational study of a governance layer as a Decision Intelligence contribution, given that the work contains no representation contribution, no inference, and no evaluated reasoning.

EXISTING EVIDENCE IS SUFFICIENT FOR: the activation rate and its disclosed sensitivity envelope (5.67–9.56%, wave-dominated), the isolation of the intermediate level by the C0–C3 ladder, the structural equivalence of C1 and C3, the identity Δ_L2 ≡ P(S=CAUTION), the negative findings that wind is a structural zero and three of five component classifiers never bind, and conformance of the implementation to its governance contract under a declared component exclusion.

EXISTING EVIDENCE IS NOT SUFFICIENT FOR: any claim that pre-inference restriction differs observably from post-hoc filtering, that participation and advisory scope are independent controls, that the comparator ladder constitutes a general methodology, that the headline is a stable or threshold-robust site property, or that {Go, Delay} is a correct, optimal or safer restriction.

THE CLEAREST CONTRIBUTION BEYOND IPoSCI IS: the structural result that a three-state governance topology is behaviourally identical to a binary gate unless the intermediate state restricts advisory scope — measured at 0.00% against 5.81% — together with the identity showing what an activation-rate measure does and does not identify.

---

*Discovery complete. No manuscript drafted. No research reframed. Literature verified against primary sources on 2026-09-23. Revised the same day after a complete reading of `experiment-report-delta-l2.md` — see the revision note at the top.*
