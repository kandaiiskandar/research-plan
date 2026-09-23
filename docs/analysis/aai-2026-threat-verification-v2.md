# AAI 2026 — Primary-Paper Threat Verification v2

**Date:** 2026-09-23
**Mode:** Second-pass adversarial audit **of v1**. v1 is a hypothesis, not evidence. Primary papers are authoritative.
**Scope:** Review report only. 🔒 No locked document edited. No manuscript text drafted.
**Sources:** full text, `notes/sources/aai-2026-threat-papers/`. Page/section refs are to those extractions.

---

## 1. Executive second-review verdict

🔴 **v1 reached the right posture for the wrong reason, and over-corrected in three places.**

**v1's central reasoning error.** v1 concluded the **original** gap wording *"is too broad to survive SA-ROC"* and that its *"protection currently rests on 'advisory-scope' doing silent work."* **That is wrong.** The original wording contains **two independent qualifiers** — *"intermediate advisory-scope level"* and *"relative to a participation-only gate"* — and **each one independently excludes SA-ROC**, which has no advisory-scope level (its intermediate zone is human review) and no participation-only comparator. Verified against the paper, **the original statement is true as written.**

**Consequence.** Narrowing is **useful** (a reviewer who knows these three papers will *suspect* the claim is false unless the near-neighbours are named) but it is **not required** (the claim is not false). v1 conflated a **related-work obligation** with a **gap correction**. The distinction Part E demands is decisive and v1 failed it.

**Three over-corrections identified:**

| # | v1 recommendation | v2 finding |
|---|---|---|
| 1 | Remove *"multi-year environmental record"* as differentiator | 🔴 **Directionally wrong.** Removing a qualifier from an **absence claim broadens it** and increases exposure. Keep it |
| 2 | Downgrade activation-frequency measurement and threshold-sensitivity to PRIOR ART EXISTS | ⚠️ **Half right.** The *technique* is prior art; the *measured object* is not. v1 changed contribution status on a generic methodological analogue — the precise error Part F warns against |
| 3 | SA-ROC is the strongest prior-art challenge | ⚠️ **Partially agree.** Strongest on *technique*, weakest on *object*. **CAIS is the harder challenge**, because its ablation is structurally the same move as our ladder |

**One v1 finding that strengthened on re-verification.** v1 called the Gray-Zone-as-abstention reading decisive; I tried to break it and could not. **The paper never once describes the AI providing a narrower set of recommendations in the Gray Zone.** Its language is uniformly removal-from-automation.

**Two v1 findings that weakened.** Denominator-policy dependence and lower-bound interpretation are **measurement qualifications, not contributions**. v1 listed both as distinctive contribution items. They are distinctive within the reviewed set, but that is not the same as contribution-bearing.

🔒 **V2 verdict: the ORIGINAL gap survives unchanged. The research chain does not require reopening. The manuscript architecture does require a related-work addition.**

---

## 2. Corrections to v1

| # | v1 claim | Status | Correction |
|---|---|---|---|
| C1 | Original gap *"too broad to survive SA-ROC"* | 🔴 **NOT SUPPORTED** | Both qualifiers exclude SA-ROC independently. Original is true |
| C2 | VERDICT B — narrowing **required** | 🔴 **OVERSTATED** | Narrowing is **useful, not required**. Correct status: original survives |
| C3 | Remove *"multi-year environmental record"* | 🔴 **DISAGREE** | Broadens an absence claim. Retain |
| C4 | Activation-frequency measurement → PRIOR ART EXISTS | ⚠️ **NEEDS SPLIT** | Generic technique: prior art. Specific estimand (frequency of *contraction* binding): distinctive within set |
| C5 | Threshold-sensitivity characterisation → PRIOR ART EXISTS | ⚠️ **NEEDS SPLIT** | Same split. SA-ROC sweeps α over an **abstention burden**, not a contraction rate |
| C6 | Comparator/ablation methodology → PRIOR ART EXISTS | ✅ **AGREE** | CAIS §3.4 is explicit and unambiguous |
| C7 | FULL→RESTRICTED→NONE topology → PRIOR ART EXISTS | ✅ **AGREE** | LL §IV-E verified |
| C8 | Gray Zone = abstention, not contraction | ✅ **AGREE — and stronger than v1 argued** | No textual support anywhere for a restricted-AI-set reading |
| C9 | Denominator-policy dependence → distinctive contribution | ⚠️ **PARTIALLY DISAGREE** | Distinctive within set, but it is an **evaluation sensitivity**, not a contribution |
| C10 | Lower-bound interpretation → distinctive contribution | ⚠️ **PARTIALLY DISAGREE** | A **measurement qualification / limitation-handling practice**, not a contribution |
| C11 | Three references MUST enter | ✅ **AGREE** | For related work, not because the gap changed |
| C12 | DSA-SafetyBench = E, drop | ✅ **AGREE** | Verified |
| C13 | A⁴-Gov has no evaluation | ✅ **AGREE** | Verified, nothing overlooked |

---

## 3. Legitimacy Layer verification

**(a) Normal Autonomy broadest — VERIFIED.** §IV-E p6: *"In Normal Autonomy, the system operates under standard conditions and the controller may issue execute or execute_async for decisions meeting signal thresholds, full routing capability is available."*

**(b) Reduced Autonomy contracts while active — VERIFIED, with a nuance v1 did not record.** §IV-E p6: *"In Reduced Autonomy, the execute directive is restricted to low-impact decisions, asynchronous execution remains available for reversible decisions, and escalation is triggered when individual signal thresholds are met as the system continues operating under tighter governance constraints."*

⚠️ **Nuance:** the contraction is **decision-conditional** — `execute` is narrowed by a predicate on impact class — rather than **vocabulary-wholesale**, which is how `A_AI(CAUTION) = {Go, Delay}` removes two recommendation *types* outright. Both are genuine contractions of the (state, decision) → permitted-output mapping. The nuance does not rescue any novelty and should not be leaned on.

**(c) HOR suppresses autonomous execution — VERIFIED.** §IV-E p6: *"In Human Oversight Required, both execute and execute_async are suppressed and all decisions are routed through escalate."*

**(d) Safe Halt — VERIFIED.** §IV-E p6: *"In Safe Halt, all execution is suspended, pending decisions are queued without processing, and only halt is permitted."*

**(e) Graduated contraction is prior art — VERIFIED.** The four modes form a monotone contraction chain with the system active at the intermediate level.

### The critical limitation — re-verified and confirmed

*"a minimal simulation of 1,000 decision instances was conducted **under Normal Autonomy mode assumptions**"* (§V-G, p8). Table V is an **analytical prediction** *"derived in closed form from Algorithm 1's priority-ordered rules"* — and Algorithm 1 lines 1–6 short-circuit on SAFE_HALT and HUMAN_OVERSIGHT_REQUIRED, so a Normal-Autonomy derivation never exercises them. The prototype [31] is described as *"reproducing Table IV"* — the same Normal-Autonomy run.

| Question | Answer | Evidence |
|---|---|---|
| Any measurement of how often Reduced Autonomy binds? | **NO** | No table reports mode occupancy or dwell |
| Any Normal-vs-Reduced comparison? | **NO** | Table V varies **input regimes**, not modes |
| Any ablation removing the intermediate mode? | **NO** | No configuration variants exist |
| Any marginal isolation of Reduced Autonomy? | **NO** | The 82.9% decomposition attributes to **rules** (contestation 20.0, CRITICAL 16.0, HIGH+unc 9.6, default 36.4 — §V-G p8), not to modes |

⚠️ **Table I (p7) does record mode transitions** — Scenario 1 *"Normal Autonomy → Reduced Autonomy"*, Scenario 2 *"Reduced Autonomy → Human Oversight Required"*, Scenario 4 *"Human Oversight Required → Safe Halt"*. These are **qualitative Pass/Fail logical traces under injected adversarial conditions**, not frequency measurements. Table VI (p9) is *"a manually constructed decision sequence designed to traverse all four governance states"*, and the authors state *"This minimal simulation does not constitute empirical validation"* (§V-G p9). **Neither warrants a frequency reading.** v1 was correct not to treat them as such.

### Final classification

| Test | Verdict |
|---|---|
| 1. Intermediate active contraction | **YES** |
| 2. Frequency of that contraction | **NO** — corrects v1's "PARTIAL". The directive distribution measures routing under one mode; it never measures the contraction binding |
| 3. Participation-only comparator | **NO** |
| 4. Marginal isolation | **NO** |

🔴 **This is a correction to v1**, which graded T5 PARTIAL. PARTIAL invited the reading that LL partially measures our estimand. It does not measure it at all.

---

## 4. SA-ROC verification — the decisive paper

**1. What may the AI do in the Gray Zone?** Nothing autonomously. p1: *"a Gray Zone, where human review is mandated."* p3: *"designated for mandatory human expert review."* Fig 1c caption (p2): *"essential human review (Gray Zone)"*.

**2. Any restricted recommendation subset there?** 🔴 **NO — and the paper never describes one.** I searched every Gray Zone mention. There is no statement anywhere that the AI may issue a narrower set of outputs in the Gray Zone. The zone is defined by what the *human* does.

**3. Is the model merely generating a score while authority transfers?** **Yes, and the paper measures the human, not the AI, there.** Fig 4 (p5) analyses *"human radiologist performance within safety and Gray Zones"*, reporting *"overall human accuracy within each zone"*. Operational authority is the human's.

**4. What does the paper call it?** *"non-automated workload"* (p1, p4), *"mandatory human expert review"* (p3), *"the operational cost of indecision"* (p1). Consistently **removal from automation**.

**5. Any reasonable FULL → RESTRICTED reading?** ⚠️ I constructed the strongest adversarial reading — *the AI still emits a score, so "score but do not act" is a smaller permitted set* — and **it has no textual support.** The paper's framing is uniformly binary at the level of AI authority: automate, or do not. p5 uses elimination language directly: *"the AI eliminates its ability…"*. **v1's classification holds, and more robustly than v1 itself argued.**

**6. What does ΓArea measure?** **Occupancy/burden of the Gray Zone.** p1: *"To quantify this non-automated workload, we introduce the Gray Zone Area (ΓArea), a metric measuring the operational cost of indecision."* Reported alongside a distinct *"% of Cohort in Gray Zone"*. **Not** contraction of an admissible AI action set.

### Policy-parameter sensitivity — verified and substantial

Fig 3c (p4): *"Safety Profile Curves comparing the two models across levels ranging from **50% to 100%**; top: **percentage of cases in the Gray Zone**; bottom: corresponding **ΓArea values**."* Zone definitions at α = 90%, 95%, 100%; Γ₁, Γ₀.₉₅, Γ₀.₉₀ reported with 95% CIs.

**Data are real.** Two FDA-cleared mammography AI solutions on a ~1,000-patient cohort with radiologist outcomes: AI #2 *"ruled out 290 true negative cases, which safely removed 29.0% of the entire patient cohort from the radiologist's workload"* versus AI #1's 167 cases (16.7%), difference 123 (95% CI 87.0–150.0) (p4).

### Critical question — is v1 justified in saying generic activation-frequency and threshold-sensitivity are no longer distinctive?

⚠️ **PARTIAL.**

**Justified for the technique.** Measuring how often a governance boundary binds, swept across a policy parameter, on real data, with a named metric and confidence intervals — that is done here, and better resourced than ours. Claiming the *technique* as distinctive would be indefensible.

**Not justified for the estimand.** ΓArea quantifies **how much work the AI hands to humans**. Δ_L2 quantifies **how often an active system's recommendation set contracts**. These differ in what is being counted, not merely in domain. Part F is explicit: *"Do not change contribution status merely because a generic methodological analogue exists."* **v1 did exactly that.**

🔒 **Correct split:** *technique* → PRIOR ART EXISTS. *Estimand* → SUPPORTED AS DISTINCTIVE WITHIN REVIEWED SET.

**And decisively for Part E:** SA-ROC has **no intermediate advisory-scope level** (its intermediate zone is human review) and **no participation-only comparator**. It therefore **does not contradict the original gap wording**.

---

## 5. CAIS verification

**Components — all VERIFIED**, §3.4 p16: ungoverned baseline *"at = ρ(dt)"*, *"without any constraint enforcement"*; approval-only gating *"admissible proposals are executed unchanged but inadmissible proposals trigger a conservative fallback a⋆"*; projection-based repair; *"enabling a systematic ablation study"*. Statistics: Mann–Whitney U, Cliff's δ (Tables 3, 5, pp21–22), n=30 per mode.

| Question | Answer |
|---|---|
| 1. Different risk states? | **NO** — no risk-level structure exists |
| 2. Different governance operator types? | **YES** — reject-to-fallback vs project-to-nearest-admissible |
| 3. FULL → FULL → NONE participation-only config? | **NO** |
| 4. FULL → RESTRICTED → NONE config? | **NO** |
| 5. Isolates an intermediate state? | **NO** — isolates an *operator*, not a *level* |
| 6. Measures action-set contraction frequency? | **NO** |
| 7. What do the metrics measure? | **Violation rate** = *"Fraction of time steps where executed action violates at least one constraint"* (Table 1 p17) — compliance. **Decision drift** δt = Δ(at, ρ(dt)) — *"Measures intervention cost"* |
| 8. Does drift combine frequency and magnitude? | **YES.** Mean drift = P(intervene) × E[Δ｜intervene]. `none` = 0.0000 (never intervenes); gate_fallback 10.3659; project 12.7434 (Table 4 p22). The two are not separable from the reported statistics |
| 9. Prior art for comparator/ablation generally? | **YES — unambiguously** |
| 10. Prior art for OUR specific estimand? | **NO** |

**Critical question — is v1 correct to downgrade generic ablation while retaining participation-only-vs-intermediate-scope isolation as the residue?**

✅ **YES.** This is v1's soundest judgement. CAIS establishes governance-configuration ablation against an ungoverned baseline as prior art; it establishes nothing about isolating an intermediate **risk level**, because it has none.

⚠️ **But v1 under-weighted CAIS.** It is the structurally closer analogue of our ladder than SA-ROC is: C0-equivalent baseline, configuration variants, statistical isolation. **CAIS — not SA-ROC — is the harder challenge to the comparator component**, and a reviewer familiar with it will ask why our C0 baseline is presented as methodologically interesting.

📌 **Direction check for any future citation:** CAIS reports `project` violation rate **0.8317** versus `gate_fallback` **0.0333** — projection performs **worse** on compliance while costing more drift. Cite the direction correctly.

---

## 6. A⁴-Gov verification

**VERIFIED as v1 described. Nothing overlooked.** *"The discussion is analytical rather than comparative"* (§VI, p5). *"The paper does not compare performance against alternative control models, and the notation is descriptive rather than control-theoretic proof"* (§VII, p6).

I checked the three items v1 might have missed: **Table 2** (p5) is an artifact/example-value table (Xₜ, Θₜ, Bₜ, Pₜ, Dₜ, aₜ*, Hₜ, Bₜ₊₁, Lₜ) — illustrative, no measurement; **the failure-oriented check** (§VI-D, p6) is a prose stress case in which a proposed recalibration is rejected — no data; **the comparator discussion** (§VI-C, p6) contrasts a hypothetical static-threshold design and an audit-only design in prose, with nothing measured.

`Hₜ` is **binary** (escalation active or not). The immutable/tunable constraint split is a **constraint taxonomy**, not a graduated admissible-action level. **No Gap-B threat. Positioning prior art at most.**

---

## 7. DSA-SafetyBench verification

**v1's conclusion CONFIRMED.** The three-class auxiliary safety head is a **classifier output structure**: *"A three-class auxiliary safety head improves ranking, but five-seed evaluation does not separate architectures"* (abstract p1). Evaluation is PR-AUC, F2-opt, unsafe recall, false-alarm rate, seed-level ranking, nadir MAE (Tables 3–9, pp6–11). Calibrated hard decisions are **screening classifications** — *"models… produce all-safe or all-unsafe policies"* — i.e. degenerate *classifier outputs*, not governance directives.

**Do any of its structures translate into runtime restriction of an admissible action or recommendation set? NO.** There is no governance layer, no state→permitted-behaviour mapping, and no runtime component of any kind.

🔒 **Stated plainly: classification / ranking / calibration ≠ governance-scope contraction.** The earlier Scopus AI interpretation was **too strong** and should not be relied on again.

---

## 8. Revised T1–T8 matrix

Changes from v1 marked 🔴.

| Paper | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 |
|---|---|---|---|---|---|---|---|---|
| **1 Legitimacy Layer** | YES | YES (decision-conditional) | NO | NO | 🔴 **NO** (was PARTIAL) | D | NO | 🔴 **C** (was B+C) |
| **2 A⁴-Gov** | PARTIAL | NO | NO | NO | NO | E | NO | D |
| **3 CAIS** | YES | NO | PARTIAL | YES (operator type) | NO | D | NO | **C** |
| **4 DSA-SafetyBench** | NO | NO | NO | NO | NO | C | NO | **E** |
| **5 SA-ROC** | YES | **NO** | NO | NO | YES (abstention burden) | B+D | 🔴 **NO** (was PARTIAL) | 🔴 **C** (was B+C) |

**Why T5 drops to NO for the Legitimacy Layer:** its only frequency measurement never exercises the graduated modes, so it does not partially measure our estimand — it does not measure it.

**Why T7 drops to NO for SA-ROC:** PARTIAL implied partial correspondence to *"frequency with which intermediate scope contraction changes the admissible set relative to participation-only governance."* SA-ROC measures a different quantity (abstention burden) with no comparator. The correspondence is **analogical, not partial**.

**Why T8 drops to C for both:** B meant *"requires narrowing Gap B."* Neither contradicts the gap, so neither requires narrowing. Both must be cited. **C, not B+C.**

---

## 9. Original gap versus v1's revised gap

### Clause-by-clause audit of v1's proposed wording

| # | Clause | Classification | Finding |
|---|---|---|---|
| 1 | *"Measuring how often a governance boundary binds is established practice"* | **SUPPORTED** | SA-ROC does exactly this |
| 2 | *"the burden of an intermediate abstention zone"* | **SUPPORTED** | Accurate for SA-ROC; "abstention" is the correct characterisation |
| 3 | *"against a policy reliability target"* | **SUPPORTED** | α is *"the clinical reliability target set by the clinician"* (p1) |
| 4 | *"graduated-autonomy architectures have reported routing-directive distributions"* | 🔴 **OVERSTATED — misleading** | Technically true but it **implies the distribution exercised the graduated modes. It did not** — Normal Autonomy only. A reader would conclude LL measured graduated behaviour |
| 5 | Could clause 4 falsely imply graduated modes were exercised? | 🔴 **YES** | This is the wording's worst defect |
| 6 | *"governance-operator configurations have been ablated against an ungoverned baseline with statistical isolation"* | **SUPPORTED** | CAIS §3.4, Tables 3 and 5 |
| 7 | *"intermediate level contracts the admissible recommendation set while the system remains active"* | **SUPPORTED** | Correctly excludes SA-ROC |
| 8 | *"participation-only configuration differing from it only at that level"* | **SUPPORTED** | Correctly excludes LL and CAIS. **The robust residue** |

**Minimum necessary rewrite of clause 4** (the only clause requiring change):

> ~~graduated-autonomy architectures have reported routing-directive distributions under simulated signal regimes~~
> → **"a graduated-autonomy architecture has reported a routing-directive distribution measured under its permissive mode alone"**

### Does SA-ROC contradict the ORIGINAL wording? — the critical question

**Original:** *"No empirical characterisation identified of how often an **intermediate advisory-scope level** changes the admissible set **relative to a participation-only gate** over a multi-year environmental record."*

**NO. It does not.** Two independent grounds:

1. **SA-ROC has no intermediate advisory-scope level.** Its intermediate zone is *"mandatory human expert review"* — the AI's advisory scope there is not narrowed, it is withdrawn. The paper describes no restricted AI output set in the Gray Zone anywhere.
2. **SA-ROC has no participation-only comparator.** Its comparison is between two FDA-cleared models, not between governance configurations.

Either ground alone excludes it. Neither depends on the phrase *"multi-year environmental record"*.

**The same test applied to the others:** LL is excluded by the participation-only clause (no comparator) and by the characterisation clause (no frequency of the intermediate binding). CAIS is excluded by the intermediate-level clause (no risk levels).

### The three-way distinction Part E demands

| Option | Verdict |
|---|---|
| Narrowing **required** because the original is false | ❌ **NO.** The original is true within the reviewed set |
| Narrowing **useful** because the original is ambiguous or could be misread | ✅ **YES.** A reviewer who knows these three papers will *suspect* the claim before reading the qualifiers closely. The remedy is **naming the near-neighbours in related work**, not weakening the gap |
| Narrowing **unnecessary** | ⚠️ Partly — unnecessary for truth, advisable for defensibility |

🔒 **v1's Verdict B is corrected to: the original gap survives; the related-work section, not the gap statement, must change.**

---

## 10. Contribution-boundary decision

Re-evaluated independently. *"SUPPORTED AS DISTINCTIVE WITHIN REVIEWED SET"* means only that: within these five papers. It is not a claim of global novelty.

| # | Item | v2 verdict | Reasoning |
|---|---|---|---|
| 1 | FULL → RESTRICTED → NONE topology | **PRIOR ART EXISTS** | LL §IV-E. Agrees with v1 |
| 2a | Activation-frequency measurement *as technique* | **PRIOR ART EXISTS** | SA-ROC ΓArea + α sweep on real data |
| 2b | Frequency with which an **intermediate contraction** binds *as estimand* | **SUPPORTED AS DISTINCTIVE WITHIN REVIEWED SET** | 🔴 **Restores what v1 collapsed.** No paper measures this quantity |
| 3 | Comparator / ablation methodology | **PRIOR ART EXISTS** | CAIS §3.4. Agrees with v1 |
| 4 | Governance operational measurement | **PRIOR ART EXISTS** | SA-ROC; CAIS |
| 5a | Threshold-sensitivity characterisation *as technique* | **PRIOR ART EXISTS** | SA-ROC Safety Profile Curves, α = 50–100% |
| 5b | Sensitivity of a **contraction rate** to its governing threshold | **SUPPORTED AS DISTINCTIVE WITHIN REVIEWED SET** | 🔴 Restores the split v1 collapsed |
| 6 | Participation-only vs intermediate-scope isolation | **SUPPORTED AS DISTINCTIVE WITHIN REVIEWED SET** | The robust residue. No source performs it |
| 7 | Δ interpretation as frequency of scope contraction | **SUPPORTED AS DISTINCTIVE WITHIN REVIEWED SET** | Checked specifically per the brief: SA-ROC reports ΓArea **and** *"% of Cohort in Gray Zone"* as **two separate metrics** and states no identity between them; LL decomposes its rate by **rule**, not by state occupancy; CAIS has no occupancy notion. **No paper states an identity collapsing its governance-effect measure to intermediate-state occupancy, nor derives invariance to the restriction's content** |
| 8 | Denominator-policy dependence | 🔴 **NOT CONTRIBUTION-BEARING** | Distinctive within the set, but it is an **evaluation sensitivity** — it shows the reported rate depends on an analyst choice. That is a robustness disclosure. **Downgrades v1** |
| 9 | Missing-component / lower-bound interpretation | 🔴 **NOT CONTRIBUTION-BEARING** | A **measurement qualification / limitation-handling practice**, rigorously executed. Strengthens credibility; is not a finding. **Downgrades v1** |

**Net.** The locked primary contribution — *"an interpretive apparatus… comparator isolation, metric semantics, sensitivity envelope, component attribution, scope dependence, lower-bound status"* — after v2:

- **Carrying weight:** the isolation (item 6), the metric identity (item 7), the contraction-specific estimand and its threshold sensitivity (2b, 5b), component attribution.
- **Conceded as technique:** comparator/ablation *method*, activation-frequency *technique*, sensitivity *technique*.
- **Reclassified as qualifications, not contributions:** denominator dependence, lower bound.

This is **narrower than the locked chain states and broader than v1 concluded.** v1 stripped 2b and 5b by conflating technique with estimand; v2 restores them and removes items 8 and 9, which v1 wrongly promoted.

---

## 11. Does the research chain require reopening?

🔒 **NO.**

| Locked element | Status |
|---|---|
| Problem (§2) | Unaffected |
| **Gap B (§5)** | ✅ **Survives unchanged.** No edit required |
| Primary RQ (§6) | Unaffected |
| Supporting criterion (§7) | Unaffected |
| Central claim (§14) | Unaffected — it claims activation at a site, not novelty of technique |
| **Contribution ledger (§13)** | ⚠️ **Overstates two components.** Needs a precision edit, not a reopen |
| **§21 attack 16** | ⚠️ *"nothing beyond prior art… what is not anticipated"* now has three named near-neighbours |
| Citation lock §B | ⚠️ *"GAP B SURVIVES FALSIFICATION"* is **correct** and should be annotated with the v2 audit, not reversed |
| **Architecture §5 related work** | 🔴 **Requires a fourth cluster.** The real obligation from this audit |

**The chain's substance is sound. The exposure is in related work, where three near-neighbours are currently unnamed.**

---

## 12. Exact minimum edits required (proposed, NOT applied)

| # | File | Section | Proposed edit | Priority |
|---|---|---|---|---|
| E1 | `aai-2026-manuscript-architecture.md` | §5 Related work | **Add Cluster D — near-neighbour governance measurement** (~120 words): SA-ROC (binding-rate against a policy target on real data; intermediate zone is human review), CAIS (governance-configuration ablation against an ungoverned baseline), LL (graduated topology; its reported distribution is measured under the permissive mode alone). Take the budget from Cluster A | 🔴 **Required** |
| E2 | `aai-2026-locked-research-chain.md` | §13 ledger | Annotate: comparator/ablation **method** and activation-frequency/sensitivity **technique** are prior art; the **estimand** and the **isolation** carry the contribution | 🟠 Recommended |
| E3 | `aai-2026-locked-research-chain.md` | §13 ledger | Reclassify denominator dependence and lower-bound from contribution components to **measurement qualifications** | 🟠 Recommended |
| E4 | `aai-2026-locked-research-chain.md` | §21 attack 16 | Update to name the three near-neighbours and the distinguishing test | 🟠 Recommended |
| E5 | `aai-2026-citation-evidence-lock.md` | §B | Annotate *"survives; re-tested against five primary sources, v2 audit 2026-09-23"* — **do not reverse** | 🟢 Housekeeping |
| E6 | `aai-2026-citation-evidence-lock.md` | §F | Add three references | 🔴 **Required** |
| E7 | — | — | 🔴 **Do NOT apply v1's removal of "multi-year environmental record"** | 🔴 **Blocking** |

**No edit to the gap statement, the RQ, the problem or the central claim is required.**

---

## 13. References that MUST enter Citation Lock v2

| Paper | Identifier (⚠️ from extraction headers — **publisher verification still required**) | Job |
|---|---|---|
| **SA-ROC** | *npj Digital Medicine* (2026) 9:281 · DOI 10.1038/s41746-026-02450-7 | Concede binding-rate measurement against a policy target on real data; state the review-versus-contraction distinction in one sentence |
| **CAIS** | *Mach. Learn. Knowl. Extr.* 2026, 8, 125 · DOI 10.3390/make8050125 | Concede governance-configuration ablation against an ungoverned baseline. **The harder challenge — do not under-weight** |
| **Legitimacy Layer** | ICHCAI 2026 · DOI 10.1109/ICHCAI70183.2026.11607581 | Concede graduated topology with strict intermediate contraction |

**Do not add:** A⁴-Gov (no evaluation; framing duplicated by LL), DSA-SafetyBench (not relevant).

**Budget:** 14 → 17 required; 18–22 total against a 20–24 target. Margin is thin; the four droppable references in the citation lock now carry real load.

---

## 14. Remaining unresolved evidence

| # | Item | Severity |
|---|---|---|
| 1 | Publisher verification of the three DOIs and full author lists | 🔴 **High** — blocks drafting the concession |
| 2 | LL prototype repository [31]: paper describes it as *"reproducing Table IV"* (Normal Autonomy). If it contains an unreported multi-mode frequency run, §3 T5 would need revisiting | 🟠 Medium |
| 3 | SA-ROC Supplementary Note 1 and Supplementary Tables 1–2 were **not in the extraction** and may contain further sensitivity analysis | 🟠 Medium |
| 4 | This audit covers **only the five supplied sources**. It is not an exhaustive search. 🔒 The gap's *"within the reviewed literature"* qualifier is load-bearing and must be retained verbatim | 🔴 **High** |
| 5 | CAIS `project` violation rate 0.8317 > `gate_fallback` 0.0333 — projection is *worse* on compliance. Report the direction correctly if cited | 🟢 Low |
| 6 | Whether a reviewer would accept decision-conditional contraction (LL) as equivalent to vocabulary-wholesale contraction (ours). Not resolvable from the texts; do not rely on the distinction | 🟠 Medium |

---

**V2 STATUS: ORIGINAL GAP SURVIVES**
