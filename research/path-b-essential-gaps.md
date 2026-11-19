# Path B — Essential Evidence Gaps

**Prepared:** 17 November 2026 · **Author:** Claude (Cowork session) · **Status:** gap audit. **Frozen RQ1–RQ3 preserved; no canonical artefact modified; no experiment run.**

**Inclusion rule.** Only gaps that **threaten thesis validity or contribution sufficiency** are listed. Known limitations that are properly disclosed and do not threaten either — single site, single vessel class, no incident data, reanalysis provenance — are **not** gaps; they are limitations, and they belong in the limitations statement, where they already are. Four candidate gaps were considered and excluded on that basis (§3).

---

## 1. Essential gaps

### G1 — A canonical sensitivity figure does not reproduce, and the non-reproducing value is in the lock **[VALIDITY]**

| | |
|---|---|
| **The defect** | The wave-onset gradient is stated as **≈ −1.4 percentage points per 0.05 m** in `final-research-chain-lock.md` §J, in `experiment-report-delta-l2.md`, in `SESSION-HANDOVER-2026-09-21.md`, and in at least five further analysis documents. Re-computation from the canonical endpoints gives **−1.221** (PRIMARY) and **−1.252** (RESOLUTION). The AAI conference manuscript was corrected to **−1.2**; the lock and the experiment report were not |
| **Why it threatens validity** | It is a **reproducibility defect in the document that declares itself authoritative**, affecting the figure that quantifies the thesis's dominant sensitivity. An examiner who recomputes the gradient from the published endpoints will not obtain the published value. The direction and the dominance conclusion are unaffected — only the magnitude — which is what makes this cheap to fix and expensive to leave |
| **Scale** | Nine or more documents carry −1.4; one carries the corrected figure. The inconsistency is therefore *internal*, not merely stale |
| **Resolution** | A documentation decision, **not an experiment.** Either amend the figure to the recomputed value with a provenance note, or retain −1.4 with an explicit statement of how it was derived and why it differs from the endpoint calculation. **The one unacceptable outcome is leaving two values in circulation.** The researcher's decision; the handover has flagged it as open since 7 October 2026 |

### G2 — A superseded mandatory-task marker persists across twelve files **[CONTRIBUTION SUFFICIENCY]**

| | |
|---|---|
| **The defect** | `final-research-chain-lock.md` §E states permanently: *"Target-hardware benchmarking is deferred deployment/prototype evaluation and is not required evidence for the current research contribution. `E5_ANDROID_TARGET_BENCHMARK = DEFERRED_MANDATORY` must be re-designated. Its absence is **not** a thesis-evaluation limitation."* Lock §S records this as needing revision in **six** files. It is currently present in **twelve**, including the lock itself, `canonical-revision-report.md`, `rq-finalisation.md`, `docs/canonical/CHANGELOG.md` and `publications/active/journal-1/evaluation-specification.md` |
| **Why it threatens contribution sufficiency** | A marker reading `DEFERRED_MANDATORY` tells a reader that **mandatory evidence is missing**. The lock says the opposite. An examiner reading the evaluation specification before the lock will conclude the thesis is incomplete by its own account. This is the single cheapest sufficiency risk in the project to eliminate |
| **Resolution** | Re-designate the marker as the lock instructs, in all twelve files, with the lock's own wording as the replacement. **No experiment required** |

### G3 — The headline quantity's comparative interpretation is foreclosed, and the framing has not caught up **[CONTRIBUTION SUFFICIENCY]**

| | |
|---|---|
| **The defect** | `Δ_L2 ≡ P(S = CAUTION)` is verified from the implementation at <1e-9 on every configuration. Three consequences follow and are each individually disclosed somewhere, but **no document states them together at the point where the headline is introduced**: the result is invariant to the content of `A_AI(CAUTION)`; both `Go` and `Delay` survive the intermediate restriction, so the departure recommendation is never altered; and therefore the "comparison against a participation-only gate" has a closed-form answer rather than an empirical one |
| **Why it threatens contribution sufficiency** | Not because anything is hidden — the lock discloses each piece — but because the thesis's **primary** contribution is presented as a comparative empirical characterisation whose headline is definitionally a state frequency. The examiner's first question is *what does 5.81% compare?*, and the answer must be ready, consolidated, and offered before it is asked |
| **Resolution** | A framing change, costing one paragraph: state the identity and its three consequences where the headline is introduced, and reposition the robustness and structural-warrant results as the load-bearing empirical content. **No experiment, no new RQ, no change to any number.** `path-b-contribution-assessment.md` §3 and §5 give the wording and the chapter ordering |

### G4 — Two of five component-attribution zeros are definitional and are tabulated beside measured zeros **[VALIDITY]**

| | |
|---|---|
| **The defect** | Lock §K's attribution table lists five components with `g_t` at 0% (*"emits no CAUTION by construction"*) and `g_m` at 0% (structurally excluded by `D = {m}`), alongside `g_w`'s **measured** zero. The first two are definitional; only the third is a finding |
| **Why it threatens validity** | The negative result answering RQ3 is strongest when stated precisely: **one of three non-definitional components accounts for 97.6% of activations.** Stated as "three of five components never bind", it mixes a measurement with two tautologies and is weaker and more easily attacked than the truth. The lock already flags an adjacent scope confusion between CAUTION-specific and all-states binding, so the risk of conflation is live |
| **Resolution** | Annotate the table to separate definitional from measured zeros, and restate the RQ3 finding over the three non-definitional components. **No recomputation required** — the counts are unchanged |

---

## 2. The one gap that would require new work, and why it is not essential

**The absence of any independent safety or utility outcome.** Without one, no claim about effectiveness, decision quality or a safety–utility trade-off is available.

**This is not an essential gap, for three reasons.** The thesis does not make such a claim: lock §P explicitly disclaims *"accident reduction · improved safety outcomes · fisher decision quality · classification accuracy · causal effectiveness."* Lock §R prohibits reading 5.81% as *"effectiveness, safety, accuracy"*. And the independent D-4 investigation established that **no harm-severity reference exists for this vessel class in these waters**, and that the best independent hazard reference has no discriminating power at this site — so the gap is not closable by effort within this thesis.

**It is therefore a boundary of the contribution, correctly disclosed, not a defect.** Attempting to close it is Path A, which the supervisor memorandum recommends against on independent grounds.

---

## 3. Candidates considered and excluded

| Candidate | Excluded because |
|---|---|
| Single site; no generalisation to Sabah or across vessel classes | Disclosed in lock §P and §M; a scope boundary, not a validity threat |
| No incident or casualty data | Same, and not closable (§2) |
| Reanalysis provenance — nothing was available at the decision instant | A real and under-stated limitation, which is why it is in the limitations statement with a recommendation to move it to the abstract. It does not threaten the *validity* of an activation-frequency measurement over a historical record |
| Advisory types unreachable from the specified inputs (exploratory, this session) | A specification observation with a verified empirical illustration. Belongs in RQ1's chapter as a limitation; does not threaten the RQ2 or RQ3 results |
| The 2.54–14.75% researcher-perturbation range appearing alongside the 5.67–9.56% sourced envelope | A presentation risk rather than a defect — the two ranges answer different questions and both are documented. Worth one clarifying sentence wherever both appear |

---

## 4. Conclusion

# Conditionally supported

**The completed evidence supports a substantive empirical contribution, and the condition is a framing and documentation correction — not new experiments.**

### Why supported

Three completed results are neither definitional nor frequency counts, and together they constitute a genuine empirical characterisation: the **wind structural zero** (invariance across a seven-knot threshold range, zero binding hours), the **bounded influence of the least-grounded threshold** (0.48 points across its full defensible range, which converts a provenance weakness into a measured bound), and the **negative component-attribution result** answering frozen RQ3 — one of three non-definitional components accounting for 97.6% of activations, with the explicit finding that the evaluated record does not warrant the specified multi-component structure at this site. The **PRIMARY/RESOLUTION decomposition** adds a reproducibility correction, identifying two effects of opposite sign where a single grid-resolution effect had been claimed. All are complete, re-verified, and supported by 78 executions over 56 configurations.

### Why only conditionally

**The headline is a count.** `Δ_L2 ≡ P(S = CAUTION)` at <1e-9, so the thesis's primary number is the intermediate state's activation frequency, invariant to the content of the intermediate admissible set, and — because both `Go` and `Delay` survive the restriction — withholding advisory detail without altering the departure recommendation. **It is fragile**: the sourced envelope's upper bound is 1.65 times the headline, and precision is bounded by 85–123 independent weather events rather than 9,135 hours. And **four defects stand**: a canonical sensitivity figure that does not reproduce and is wrong in the lock itself (G1); a superseded "mandatory evidence missing" marker in twelve files (G2); a headline framing that has not absorbed its own identity (G3); and definitional zeros tabulated as findings (G4).

### What converts it to adequately supported

All four are documentation or framing work, and none requires repeating an experiment:

1. **Resolve G1** — settle the gradient figure to one value with stated provenance.
2. **Resolve G2** — re-designate the deferred-mandatory marker as the lock instructs, in all twelve files.
3. **Resolve G3** — state the identity and its three consequences where the headline is introduced, and reposition robustness and structural warrant as the load-bearing empirical content.
4. **Resolve G4** — separate definitional from measured zeros and restate the RQ3 finding over three components.

### The six literature summaries change nothing

They are Scopus AI syntheses over abstracts. The one directly relevant document asserts that no study compares intermediate to binary gating for safety outcomes — relevant, but self-rated moderate confidence, abstract-level, and supported by nine references that are almost all off-topic. **It cannot carry a novelty claim.** The other five supply methodological context, one on-point reference worth obtaining (Alshamlan 2026, *Bioengineering*, component-wise reliability), one self-declared inadequacy, and **two forward-dated 2027 records that must be verified before citation**. Their shared "safety–utility trade-off" framing is one this thesis must decline, since it has neither an independent utility outcome nor an independent safety outcome.

### The sentence that carries Path B

> *The strongest defensible contribution is not that the intermediate state activates in 5.81% of departure-window hours — it is that the activation is governed almost entirely by one component, that its most contestable threshold moves it by less than half a point, and that the multi-component structure the architecture specifies is not warranted by the record it was evaluated on.*

Two of those three are negative results. That is a defensible thesis, and it is already finished.
