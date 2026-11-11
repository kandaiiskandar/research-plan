# AAI 2026 — Primary-Paper Threat Verification v1

**Date:** 2026-09-23
**Task:** Adversarial falsification of locked Gap B against five primary sources. Not a manuscript task. Not a defence of the gap.
**Sources:** full text of all five extractions in `notes/sources/aai-2026-threat-papers/`. Page/section references throughout are to those extractions.
**Internal reference:** `aai-2026-locked-research-chain.md` (used to establish the exact locked gap, not to justify it).

---

## 1. Executive verdict

**VERDICT B — GAP B SURVIVES, BUT MUST BE NARROWED.**

No paper performs the specific measurement Gap B claims is absent. But **three of the five perform measurements close enough that the current wording overclaims**, and two components of the locked primary contribution must be downgraded from distinctive to conceded.

**What survives.** No source isolates an intermediate level that contracts the admissible set *while the system remains active* against a *participation-only* configuration differing from it only at that level. That residue is real and is the defensible contribution.

**What does not survive.**

1. 🔴 **"Activation-frequency measurement" is no longer distinctive.** SA-ROC (paper 5) introduces **Gray Zone Area (ΓArea)**, explicitly *"a metric measuring the operational cost of indecision"* (p1 abstract), and the **Safety Profile Curve** plots Gray Zone proportion and ΓArea **across safety levels α** (p2, Fig. 1e; p5, Fig. 5) — on **real FDA-cleared algorithm data**. That is a governance-boundary binding rate characterised against a policy parameter, on real data. Our Δ_L2-versus-wave-onset sensitivity is structurally the same move.
2. 🔴 **"Comparator/ablation methodology" is no longer distinctive.** CAIS (paper 3) §3.4 evaluates three governance configurations *"each corresponding to a distinct interpretation of G and enabling a systematic ablation study"* (p16) — including an **ungoverned baseline** (`none`) — with pairwise Mann–Whitney U tests and Cliff's δ (Tables 3, 5, pp21–22).
3. ⚠️ **"FULL → RESTRICTED → NONE topology" is firmly prior art.** The Legitimacy Layer's four modes implement exactly this, with a strict contraction at the intermediate level (§IV-E, p6).

**The load-bearing distinctions that hold**, and they are narrow:

| Paper | Why it does not close Gap B |
|---|---|
| Legitimacy Layer | No participation-only comparator; no marginal isolation; the 1,000-instance simulation runs *"under Normal Autonomy mode assumptions"* (§V-G, p8) — **the graduated modes are never exercised in the frequency measurement at all** |
| CAIS | No graduated risk levels; the three configurations are **operator types** (reject vs repair), not risk states; estimand is violation rate and drift magnitude, not contraction frequency |
| SA-ROC | The Gray Zone is **mandatory human review**, not contracted AI scope — *"these cases are designated for mandatory human expert review"* (p3). The AI **abstains entirely**; it does not remain active with a smaller recommendation set |
| A⁴-Gov | **No evaluation exists.** *"The discussion is analytical rather than comparative"* (p5); *"The paper does not compare performance against alternative control models"* (p6) |
| DSA-SafetyBench | Classification/ranking benchmark; no runtime restriction of any kind |

---

## 2. Individual audits

### Paper 1 — The Legitimacy Layer (ICHCAI 2026, DOI 10.1109/ICHCAI70183.2026.11607581)

**T1 — State-conditioned restriction: YES.** Four governance modes constrain which of four execution directives the controller may issue. *"Rather than treating autonomy as a binary condition, it dynamically constrains which routing directives the Legitimacy Controller may issue under prevailing operational conditions"* (§IV-B, p4).

**T2 — Intermediate contraction: YES — genuine strict subset.** §IV-E (p6): Normal Autonomy — *"full routing capability is available"*. Reduced Autonomy — *"the execute directive is restricted to low-impact decisions, asynchronous execution remains available for reversible decisions"*. Human Oversight Required — *"both execute and execute_async are suppressed"*. Safe Halt — *"only halt is permitted"*.
This is **FULL ⊃ RESTRICTED ⊃ MORE RESTRICTED ⊃ NONE**, with the system remaining active at the intermediate level. 🔴 **This is the closest structural match to our topology in the entire set, and it is prior art.**

**T3 — Participation-only comparator: NO.** The evaluation contains no alternative governance configuration. Table V (p8) varies **uncertainty distribution × contestation probability** — these are *input regimes*, not governance configurations. No run removes Reduced Autonomy; no binary-gate baseline exists.

**T4 — Marginal isolation: NO.** Nothing isolates the intermediate mode's contribution. The 82.9% escalation rate is decomposed by **routing source** (contestation 20.0 pts, CRITICAL impact 16.0 pts, HIGH+uncertainty 9.6 pts, default fallthrough 36.4 pts — §V-G, p8), which attributes escalations to *rules*, not to *governance levels*.

**T5 — Activation frequency: PARTIAL, and narrower than it appears.** Table IV (p8) reports directive distribution over 1,000 instances: Execute 5.3%, Execute_Async 11.8%, Escalate 82.9%, Halt 0.0%. 🔴 **Decisive limitation:** the simulation was *"conducted under Normal Autonomy mode assumptions"* (§V-G, p8). The graduated modes are therefore **not exercised** in the only frequency measurement the paper contains. Table VI (p9) is *"a manually constructed decision sequence designed to traverse all four governance states"* — a demonstration, not a frequency.

**T6 — Empirical basis: D (synthetic/simulated).** Signals sampled from specified distributions; the authors state *"This minimal simulation does not constitute empirical validation"* (§V-G, p9) and list *"reliance on simulated signal injection rather than deployed execution"* as a limitation (§V-F, p8).

**T7 — Estimand match: NO.** It measures the distribution of routing directives under a single governance mode. It does not measure how often an intermediate level contracts the admissible set relative to a participation-only configuration.

**T8 — Consequence: B + C.** Requires narrowing (it reports a governance binding-rate with an input-regime sensitivity grid) **and** must be cited as the closest architectural prior art for graduated runtime restriction.

### Paper 2 — A⁴-Gov (IEEE SERA 2026, DOI 10.1109/SERA69989.2026.11618631)

**T1 — PARTIAL.** Bounded intervention and escalation conditioned on policy state; recalibration bounded by `B(t+1) = h(Bt, Dt, Wt, a*t)` (eq. 4, p4), and *"it may not alter immutable legal or safety constraints"*. Restriction is on **baseline recalibration authority**, not on a per-decision admissible action set.

**T2 — NO.** There is no graduated level structure. `Hₜ` is binary (escalation active or not, §IV-E p4). The architecture separates immutable from tunable constraints, which is a constraint taxonomy, not an intermediate admissible-set level.

**T3 / T4 / T5 — NO.** 🔴 **The paper contains no evaluation.** *"The discussion is analytical rather than comparative"* (§VI, p5); *"The paper does not compare performance against alternative control models, and the notation is descriptive rather than control-theoretic proof"* (§VII, p6). The comparator discussion (§VI-C, p6) is a prose contrast with a hypothetical static-threshold design, with no measurement.

**T6 — E (conceptual/formal demonstration only).** One illustrative public-service example plus a failure-oriented check.

**T7 — NO.** No quantity is measured.

**T8 — D (positioning only), tending to C.** Useful for the runtime-governance-layer framing and it cites NIST AI 100-1 [4] and Siebert et al. on meaningful human control [17]. Carries no empirical threat.

### Paper 3 — Controlled Agentic AI Systems (CAIS) (*Mach. Learn. Knowl. Extr.* 2026, 8, 125; DOI 10.3390/make8050125)

**T1 — YES.** A governance operator `G` transforms proposed actions into admissible executed actions over state-conditioned feasible sets `A_C(s_t)` (abstract, p1; §3.5, p16).

**T2 — NO.** There is **no graduated risk-level structure**. `A_C(s_t)` varies continuously with state via hard constraints (collision avoidance, exclusion zones, actuator bounds, §3.5 p16). No discrete intermediate level exists. *"progressively richer constraint sets"* (§3.5) is a sensitivity analysis over constraint complexity, not a risk-graduated topology.

**T3 — PARTIAL, and this is the paper's real threat.** §3.4 (p16) defines three configurations: **ungoverned baseline** (`a_t = ρ(d_t)`, *"without any constraint enforcement"*); **approval-only gating** (*"admissible proposals are executed unchanged but inadmissible proposals trigger a conservative fallback a⋆"*); **projection-based repair**. The ungoverned baseline is a genuine C0-equivalent. But approval-only versus projection differ in **how an inadmissible proposal is handled**, not in **what may be proposed at different risk levels** — and both operate **post-hoc on a single proposed action**, which is the post-posed rather than preemptive pattern.

**T4 — YES, for governance-operator type.** Explicitly *"enabling a systematic ablation study"* (§3.4, p16), with n=30 per mode, Mann–Whitney U and Cliff's δ (Tables 3 and 5, pp21–22). 🔴 **This is direct prior art for governance-configuration ablation against an ungoverned baseline.**

**T5 — NO for contraction frequency.** Measured: **violation rate** — *"Fraction of time steps where executed action violates at least one constraint"* (Table 1, p17) — `none` 1.0000, `gate_fallback` 0.0333, `project` 0.8317 (Table 2, p21). And **decision drift** `δt = Δ(at, ρ(dt))`, *"Measures intervention cost"* — `none` 0.0000, `gate_fallback` 10.3659, `project` 12.7434 (Table 4, p22). Drift is an **intervention magnitude**, conflating frequency and size; it is not an admissible-set contraction frequency.

**T6 — D (simulated).** *"controlled experiments in multi-agent and federated simulation environments"* (abstract, p1).

**T7 — NO.** Estimand is compliance and intervention cost across operator types, not contraction frequency relative to participation-only gating across risk levels.

**T8 — C (prior art that must be conceded and cited).** 🔴 **The strongest challenge to the comparator/ablation component of our secondary contribution.**

### Paper 4 — DSA-SafetyBench (*Energy and AI* 25 (2026) 100811; DOI 10.1016/j.egyai.2026.100811)

**T1–T5 — NO throughout.** This is a **benchmark for decision-level classification quality**, not a governance architecture. It *"tests whether machine-learning models produce useful frequency-security decisions, not only accurate trajectories"* (abstract, p1). No component restricts what any system may recommend at runtime.

**Special check — was the Scopus AI interpretation too strong? 🔴 YES, materially.** The three-class structure is a **classifier output head**, not an admissible-action restriction: *"A three-class auxiliary safety head improves ranking, but five-seed evaluation does not separate architectures"* (abstract, p1). It is evaluated by **PR-AUC, F2-opt, unsafe recall, false-alarm rate, seed-level ranking** (Tables 3–7, pp6–9). This is classification, ranking and calibration throughout. **It contains no runtime admissible-action restriction and no intermediate-level measurement.** Any suggestion that it measures intermediate restriction effects is unsupported by the paper.

**T6 — C** (experimental benchmark data derived from time-domain simulations: IEEE 39-bus, NPCC 140-bus, WECC 179-bus).
**T7 — NO. T8 — E (not materially relevant).**

### Paper 5 — Defining Operational Safety in Clinical AI / SA-ROC (*npj Digital Medicine* (2026) 9:281; DOI 10.1038/s41746-026-02450-7)

**T1 — YES, but as a score-space partition.** Two clinician-set reliability targets (α⁺, α⁻) yield score cutoffs partitioning predictions into three zones (p3).

**T2 — 🔴 NO — and this is the decisive finding for this paper.** The special check is correct and the distinction is real. Per p3:
- **Rule-in Safe Zone** — *"cases in this zone are deemed reliable enough for autonomous escalation or action"*
- **Rule-out Safe Zone** — *"deemed reliable enough for autonomous de-prioritization"*
- **Gray Zone** — *"signifying that these cases are designated for **mandatory human expert review**"*

And the workflow: *"having the AI system autonomously handle all cases within the resulting Safe Zones… while the diagnostically challenging cases within the Gray Zone are, by design, escalated"* (p3).

**The Gray Zone is option (b): mandatory human review / deferral.** The AI does **not** remain active with a contracted recommendation set — it **abstains entirely**. Mapped onto our topology the AI-facing structure is binary (act / abstain) with the abstention band in the middle of score space, not FULL → RESTRICTED → NONE across risk states.

**T3 — NO.** No participation-only comparator. The comparison is **between two FDA-cleared models** (p4), not between governance configurations.

**T4 — NO.** No isolation of an intermediate level's marginal contribution; the intermediate zone *is* the abstention region, and there is no variant in which it is removed.

**T5 — 🔴 YES for abstention frequency — the strongest activation-frequency prior art in the set.** **ΓArea** is *"a metric measuring the operational cost of indecision"* (p1) quantifying *"this non-automated workload"*; the **Safety Profile Curve** plots *"Gray Zone proportion and ΓArea across the safety levels (α)"* (p2). Reported values include ΓArea = 0.709 for overlapping distributions (p4) and 29.0% of cases safely ruled out at the highest safety level (p4). **This is a binding-rate measured as a function of a policy parameter.**

**T6 — B + D (strongest empirical basis in the set).** Simulation studies **plus** a real-world case study using two FDA-cleared cancer-screening algorithms and radiologist performance data (pp4–5).

**T7 — PARTIAL.** It measures how often the intermediate zone binds, against a policy parameter, on real data — structurally analogous to Δ_L2 against the wave onset. It does **not** measure contraction of an active system's recommendation set, and it has no participation-only comparator.

**T8 — B + C.** Requires narrowing (it removes activation-frequency-with-policy-sensitivity from our distinctive column) **and** must be cited.

---

## 3. T1–T8 comparison matrix

| Paper | T1 restriction | T2 intermediate contraction | T3 participation-only comparator | T4 marginal isolation | T5 activation frequency | T6 data | T7 estimand | T8 |
|---|---|---|---|---|---|---|---|---|
| **1 Legitimacy Layer** | YES | **YES** (strict, active) | NO | NO | PARTIAL — directive distribution, **Normal Autonomy only** | **D** | **NO** | **B + C** |
| **2 A⁴-Gov** | PARTIAL | NO | NO | NO | NO — no evaluation | **E** | **NO** | D→C |
| **3 CAIS** | YES | NO — operator types, not levels | **PARTIAL** — ungoverned baseline | **YES** — for operator type | NO — violation rate, drift | **D** | **NO** | **C** |
| **4 DSA-SafetyBench** | NO | NO | NO | NO | NO — PR-AUC, recall | C | **NO** | **E** |
| **5 SA-ROC** | YES | **NO — abstention, not contraction** | NO | NO | **YES** — ΓArea vs α | **B + D** | **PARTIAL** | **B + C** |

**Reading the matrix.** No row is YES across T2–T5 and T7. The threat is **distributed**: paper 1 supplies the topology, paper 3 supplies the ablation method, paper 5 supplies the frequency-with-sensitivity measurement on real data. **No paper assembles them, and no paper measures contraction against a participation-only baseline.**

### Answers to the six synthesis questions

**1. Does any paper satisfy T1–T7 closely enough to invalidate Gap B?**
**No.** Paper 1 fails T3, T4, T7. Paper 3 fails T2, T5, T7. Paper 5 fails T2, T3, T4 — and its T2 failure is categorical: abstention is not contraction.

**2. Does any paper require the gap to be narrowed?**
**Yes — papers 5 and 1, and to a lesser extent 3.** Paper 5 removes "measuring how often a governance boundary binds, characterised against a policy parameter" from the distinctive column. Paper 1 removes "graduated topology with strict intermediate contraction". Paper 3 removes "governance-configuration ablation against an ungoverned baseline".

**3. Which papers must be cited as prior-art concessions?**
**Papers 1, 3 and 5 — all three are required.** Omitting any one leaves a reviewer able to find an unconceded near-neighbour.

**4. Which are unnecessary for a six-page manuscript?**
**Paper 4 — drop entirely** (T8 = E; nothing in it bears on any claim). **Paper 2 — droppable**; it has no evaluation and its architectural framing is already covered by paper 1 at lower citation cost.

**5. Strongest prior-art challenge to the proposed contribution?**
**SA-ROC (paper 5).** It measures an intermediate-zone binding rate as a function of a policy parameter, on real clinical data, and publishes a dedicated metric for it. Our Δ_L2-with-sensitivity-envelope is the same *methodological move* on a different mechanism. The defence is narrow and must be stated precisely: SA-ROC's intermediate zone is **AI abstention with deferral to a human**, whereas ours is **contraction of an active system's recommendation set** — a distinction of mechanism, not of degree. **A runner-up worth naming: CAIS**, for the ablation methodology.

**6. What remains unaddressed after all five?**
Exactly one thing, and it is narrow: **no source isolates the marginal effect of an intermediate level that contracts the admissible set while the system remains active, against a participation-only configuration differing from it only at that level.** Paper 1 has the level but no comparator. Paper 3 has the comparator but no level. Paper 5 has the frequency measurement but the intermediate state is abstention. **The isolation is the residue.**

---

## 4. Strongest threat analysis

**The threat is not that someone did our study. It is that the three components we treated as an assembled contribution each exist separately, in stronger empirical form than ours in one case.**

| Component | Prior art | Their empirical basis | Ours |
|---|---|---|---|
| Graduated topology with strict intermediate contraction | Legitimacy Layer §IV-E | Simulated | Same topology |
| Ablation across governance configurations incl. ungoverned baseline | CAIS §3.4, Tables 2–5 | Simulated, n=30, non-parametric tests | Deterministic census, no tests |
| Binding-rate measured against a policy parameter | SA-ROC ΓArea, Safety Profile Curve | **Real FDA-cleared algorithm data + radiologist data** | Reanalysis replay |

🔴 **The uncomfortable comparison is the third row.** SA-ROC measures its boundary-binding metric on real clinical data with a published, named metric and an explicit policy-parameter sweep. Our equivalent runs on ERA5 reanalysis with researcher-defined thresholds. **On empirical strength, SA-ROC is ahead of us on the component we share.** Our advantage is not data quality; it is that the quantity being characterised is different (contraction versus abstention) and that we isolate it against a comparator, which they do not.

**A reviewer who knows SA-ROC will ask why ΓArea is not our related work.** It must be, and the answer must be the mechanism distinction, stated in one sentence, not avoided.

---

## 5. Gap falsification verdict

### 🔒 VERDICT B — GAP B SURVIVES BUT MUST BE NARROWED

**Why not A.** The current wording — *"no empirical characterisation… of how often an intermediate advisory-scope governance level changes the admissible recommendation set"* — is too broad to survive SA-ROC, which characterises exactly how often its intermediate zone binds, against a policy parameter, on real data. The wording's protection currently rests on "advisory-scope" doing silent work, and a reviewer will not grant that.

**Why not C.** No paper isolates the intermediate level against a participation-only configuration. Paper 5's intermediate state is abstention, which is categorically different: the system is inactive there, so there is no contracted set to measure. Paper 1 never exercises its graduated modes in its frequency measurement. Paper 3 has no risk levels at all.

**Why not D.** The evidence is sufficient and unambiguous on every load-bearing test; all five papers were read in full and every conclusion above is anchored to quoted text.

### Minimum necessary revised gap wording

> **Revised Gap B.** Measuring how often a governance boundary binds is established practice: the burden of an intermediate abstention zone has been quantified against a policy reliability target on real clinical data [SA-ROC], graduated-autonomy architectures have reported routing-directive distributions under simulated signal regimes [Legitimacy Layer], and governance-operator configurations have been ablated against an ungoverned baseline with statistical isolation [CAIS]. Within the reviewed literature, we did not identify a measurement in which an intermediate level that **contracts the admissible recommendation set while the system remains active** is **isolated against a participation-only configuration differing from it only at that level**.

**What changed and why each change is necessary:**

| Change | Necessity |
|---|---|
| Opening concession clause naming all three papers | Without it the gap claims absence of work that demonstrably exists |
| *"while the system remains active"* | Excludes SA-ROC's abstention design — the one distinction that survives scrutiny |
| *"isolated against a participation-only configuration differing from it only at that level"* | Excludes Legitimacy Layer (no comparator) and CAIS (no level). **This is the actual residue** |
| *"multi-year environmental record"* **removed as the differentiator** | It is a property of our dataset, not a scientific distinction. Retaining it as load-bearing would be defending the gap by domain accident. It may still appear as scope, not as the reason the gap holds |

🔴 **This narrowing is binding on the locked chain.** `aai-2026-locked-research-chain.md` §5 and §18, and `aai-2026-citation-evidence-lock.md` §B, carry the old wording and the finding that Gap B "survives falsification" unqualified. **Both must be updated before drafting.** The primary RQ is unaffected; the contribution ledger is affected — see §7.

---

## 6. Minimum gap correction — downstream consequences

| Document | Section | Required change |
|---|---|---|
| `aai-2026-locked-research-chain.md` | §5 Specific empirical gap | Replace with the revised wording above |
| `aai-2026-locked-research-chain.md` | §13 Contribution ledger | Downgrade comparator design and sensitivity envelope from PRIMARY components to conceded-method components — see §7 |
| `aai-2026-locked-research-chain.md` | §21 attack 16 | Update: "nothing beyond prior art" now has three named near-neighbours, not zero |
| `aai-2026-citation-evidence-lock.md` | §B | Replace "GAP B SURVIVES FALSIFICATION" with "survives as narrowed, v1 audit" |
| `aai-2026-manuscript-architecture.md` | §5 Related work | **Add a fourth cluster: near-neighbour governance measurement** (papers 1, 3, 5), ~120 words, taken from the Cluster A budget |
| `aai-2026-manuscript-architecture.md` | §15 citation plan | +3 required references |

⚠️ **Reference budget.** The citation lock closed at 14 required / 15–19 total. Adding three required takes it to **17 required / 18–22 total**, against a 20–24 target. Still inside, but the droppable margin is now thin. Papers 2 and 4 must **not** be added.

---

## 7. Novelty / contribution boundary after audit

| Item | Verdict | Evidence |
|---|---|---|
| Runtime restriction mechanism | **PRIOR ART EXISTS** | LL §IV; CAIS §3.4; already conceded to ASTM F3269 |
| Graduated risk states | **PRIOR ART EXISTS** | LL four modes §IV-E |
| **FULL → RESTRICTED → NONE topology** | **PRIOR ART EXISTS** | LL §IV-E — strict contraction at Reduced Autonomy with the system active. 🔴 Downgraded by this audit |
| **Activation-frequency measurement** | **PRIOR ART EXISTS** | SA-ROC ΓArea and Safety Profile Curve, on real data; LL Table IV. 🔴 **Downgraded — was treated as distinctive in the locked chain** |
| Governance operational measurement | **PRIOR ART EXISTS** | SA-ROC; CAIS Tables 2–5 |
| **Comparator / ablation methodology** | **PRIOR ART EXISTS** | CAIS §3.4 *"systematic ablation study"*, Tables 3 and 5. 🔴 **Downgraded** |
| **Participation-only vs intermediate-scope isolation** | ✅ **SUPPORTED AS DISTINCTIVE** | No source performs it — LL has no comparator, CAIS has no level, SA-ROC has neither |
| **Δ interpretation as frequency of scope contraction** | ✅ **SUPPORTED AS DISTINCTIVE** | No source states an identity between its governance metric and the intermediate-state base rate, nor derives invariance to the restriction's content |
| Threshold-sensitivity characterisation | **PRIOR ART EXISTS** | SA-ROC ΓArea across α; LL Table V input-regime grid. 🔴 Downgraded |
| Vessel-class dependence | **NOT ENOUGH EVIDENCE** | No comparable analysis located; but it is a domain-scoping result, not a CS contribution |
| **Denominator-policy dependence** | ✅ **SUPPORTED AS DISTINCTIVE** (weakly) | No source examines how the evaluation denominator changes its reported governance rate |
| **Missing-component / lower-bound interpretation** | ✅ **SUPPORTED AS DISTINCTIVE** | No source declares an excluded component and carries a directional bound; CAIS reports residual violations as approximation error, which is different |

**Net effect on the locked primary contribution.** It was *"an interpretive apparatus for governance-activation measurement: comparator isolation, metric semantics, sensitivity envelope, component attribution, scope dependence, lower-bound status."* After audit: **two of six components (comparator isolation as method, sensitivity envelope) are conceded**; four hold. **The contribution survives as an assembly claim, not as a set of individually distinctive parts** — and the assembly claim now rests primarily on the isolation and the metric identity.

This is a narrowing, not an invalidation. It is also a more honest position: the paper now says *these measurement moves exist separately; we assemble them and add the isolation and the identity*, which is defensible and checkable.

---

## 8. References that MUST enter the AAI paper

| Paper | Purpose | Placement |
|---|---|---|
| **Legitimacy Layer** — ICHCAI 2026, DOI 10.1109/ICHCAI70183.2026.11607581 | Concede graduated runtime topology with strict intermediate contraction; note its measurement runs under one mode and has no comparator | Related work, near-neighbour cluster |
| **CAIS** — *Mach. Learn. Knowl. Extr.* 8, 125, DOI 10.3390/make8050125 | Concede governance-configuration ablation against an ungoverned baseline; note its configurations are operator types, not risk levels | Related work + method, where the ladder is introduced |
| **SA-ROC** — *npj Digital Medicine* 9:281, DOI 10.1038/s41746-026-02450-7 | Concede binding-rate measurement against a policy parameter on real data; state the abstention-versus-contraction distinction in one sentence | Related work + the sensitivity subsection |

⚠️ All three carry DOIs read from the extraction headers. **They have not been verified against publisher records** to the standard of `aai-2026-citation-evidence-lock.md` §F. Verify before drafting.

## 9. References that may be dropped

- **DSA-SafetyBench** — T8 = E. Nothing in it bears on any claim. 🔴 Also record that the Scopus AI interpretation of this paper was **too strong** and should not be relied on again.
- **A⁴-Gov** — no evaluation; architectural framing duplicated by the Legitimacy Layer at lower citation cost. Retain only if a reviewer raises public-sector runtime governance.

## 10. Unresolved evidence requiring further verification

| # | Item | Severity |
|---|---|---|
| 1 | Publisher verification of the three new DOIs and full author lists | 🟠 Medium — blocks drafting of the concession |
| 2 | Whether the Legitimacy Layer's public prototype [31] contains a multi-mode frequency run absent from the paper. If it does, T5 strengthens and this audit may need revisiting | 🟠 Medium |
| 3 | SA-ROC supplementary tables 1–2 (policy configurations) were not in the extraction; they may contain further sensitivity analysis | 🟢 Low |
| 4 | Whether any **fourth-party** work assembles topology + comparator + frequency. This audit covers only the five supplied sources and does not constitute an exhaustive search | 🟠 Medium — the revised gap says "within the reviewed literature" and must keep that qualifier |
| 5 | CAIS reports `project` violation rate 0.8317 versus `gate_fallback` 0.0333 — projection performs *worse* on compliance. Not relevant to our claims, but if cited, the direction must be reported correctly | 🟢 Low |

---

*Audit complete. Five primary sources read in full. Gap B narrowed, not invalidated. No manuscript text drafted. The locked chain has NOT been edited by this task — §6 lists the changes it now requires, pending authorisation.*
