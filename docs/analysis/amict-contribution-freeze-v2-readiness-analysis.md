# AMICT Contribution Freeze V2 — Task Readiness Analysis

**Date:** 2026-09-14
**Analyses:** `docs/tasks/AMICT CONTRIBUTION FREEZE V2 — POST-NOVELTY REPOSITIONING.md`
**Status:** PRE-EXECUTION ANALYSIS ONLY. No freeze performed. `contribution-freeze-v2.md` and `contribution-claim-matrix.csv` do not exist. No manuscript touched.
**Companions:** [`amict-conference-rebuild-readiness-analysis.md`](amict-conference-rebuild-readiness-analysis.md) · [`amict-source-validation-readiness-analysis.md`](amict-source-validation-readiness-analysis.md)

---

## 1. What the task is

The **binding gate**. Its output becomes authority for RQ redesign, the conference outline, manuscript drafting and the claim-evidence audit. Everything downstream inherits whatever wording is frozen here, so a phrase that survives this task by inertia will survive into the submitted paper.

The task is correctly framed as an **audit of candidate wording**, not a drafting exercise: §4 explicitly says "Do NOT automatically accept this wording. Treat it as the candidate to audit." That is the right posture, because the candidate C1 contains at least two phrases the evidence does not carry at full strength.

---

## 2. Premise verification

### 2.1 Numbers reconcile — stop condition 8 does not fire

Every figure in §8 and §9 was checked against canonical artefacts during the two preceding tasks and re-spot-checked here. Fidelity (292 / 32 / 260 / 454 / 244 / 16 / 162, F1–F3 = 0), PRIMARY divergence (42.88 / 48.69 / 5.81 / 0.00), ΔL2 (5.81 / 4.48), temporal (3,661 / 3,439 / 222 / 26 / 10.36%) and the E5/H3/R-SAFE-001 statuses all hold with no conflict.

### 2.2 One provenance asymmetry worth knowing before C2 is worded

The RESOLUTION **pairwise** values — C0↔C1 = 41.08%, C0↔C2 = 45.56% — are canonical. They appear in the Journal 1 manuscript with their derivations (2,438 / 5,935 = 41.08%), in the prediction register as P24 and P23, and in `report-c8-migration-2026-09-08.md`. They are produced by `scripts/condition_comparison.py`, which runs both configurations.

**But `data/journal1-manuscript-evidence-sync/quantitative-provenance.csv` carries no row for either.** It records C0↔C1 and C0↔C2 for PRIMARY, and ΔL2 for both configurations, and stops there.

This is not a conflict and not a stop condition. It matters because the claim matrix this task produces requires an `evidence_source` per clause, and the conference-rebuild claim-evidence audit will key off that CSV.

**Recommendation:** found frozen C2 on **ΔL2 (5.81 / 4.48)** and **C1↔C3 (0.00 / 0.00)** — both fully provenanced — and treat the full pairwise matrix as supporting context. If the pairwise RESOLUTION values are used in the manuscript, a provenance row must be added first.

Secondary note: P23 and P24 are **REFUTED** predictions at these values (28.19 predicted against 45.56 actual; 22.21 against 41.08). Citing them drags refuted-prediction context along. The v3 manuscript already handles refutations honestly, so this is a drafting awareness point, not a defect.

---

## 3. The generalisation audit is the load-bearing question

§6 flags this as high priority and is right to. After mechanism novelty is withdrawn, "generalisation" is carrying weight it did not carry before.

### 3.1 What actually exists as evidence

**No canonical authority articulates a generalisation claim.** `appendix-c-formalisation.md` contains zero occurrences of "generalis*", "generaliz*", "reinstant*" or "transferab*". The formal apparatus is there; the *claim about it* is not.

The generalisation claim exists in exactly one place: **v3's Generalisation section**, which already states "The architecture is domain-independent at the structural level", gives a three-step re-instantiation recipe, and argues that Totality, Monotonicity and Safety Dominance "transfer automatically to any correct instantiation, because they are proved from the structure of the governance pair rather than from the fisheries-specific values."

It is accompanied by **TABLE V — two illustrative rows** (emergency triage; industrial/transportation safety), and by a hedge already present in v3: *"Whether the three-state governance structure is practically appropriate for any given domain remains an empirical question that domain-specific prototype work must address."*

**There is no cross-domain instantiation, implementation or evaluation anywhere in the repository.**

### 3.2 Dimension-by-dimension pre-assessment

| Dim | Claim | Assessment | Basis |
|---|---|---|---|
| A | single scalar → `E = (w, r, m, o, v, t)` | **YES** | Five component classifiers with max-severity aggregation; contrasts directly and verifiably with the TCAS single scalar + configuration discretes |
| B | device table → `S = f(E)`, `(G(S), A_AI(S))` | **YES** | Appendix C and the algorithm specification define both as general objects, not as a lookup table |
| C | generator-independent admissibility contract | **YES** | `RS(S)` pre-reasoning contract (algorithm spec §8) supplies the rule set *before* inference; admissibility is defined over recommendation types, not over the Layer 3 engine |
| D | `ρ_{D,τ}` — missing / stale / invalid semantics | **YES — and strongest** | Four distinguished ⊥ conditions, declared exclusion set `D`, Theorem C.1b operational totality, the fault-versus-exclusion distinction, `t ∉ D` as structural, and explicit lower-bound propagation |
| E | severity ordering + monotone admissible sets | **YES formally, NOT distinctive** | Proved here, but Baxi (2026) and Kang (2026) both carry monotone nested restriction proved by construction |
| F | re-instantiation via domain-specific classifiers | **PARTIAL** | Argued structurally, illustrated in two table rows, never demonstrated |

### 3.3 "Domain-independent" overstates; recommend a narrower formulation

Two different claims are being conflated:

- *"The proved properties hold for any correct instantiation, because they are proved over the structure of the governance pair."* This is a **FORMAL** claim and it is **defensible** — it follows from the proofs quantifying over the structure rather than over fisheries values.
- *"The architecture is domain-independent."* In a contributions list this reads as an **INTERPRETATION / engineering-applicability** claim, and nothing demonstrates it. Dimension F is the gap: re-instantiation is described, never performed.

This is exactly the silent category crossing §16 warns about. **Recommended frozen formulation: "domain-reinstantiable"** or **"domain-agnostic at the governance-contract level"**, with the transfer argument stated as the formal property it is. "Generalised beyond a single hazard variable" is also accurate and is the formulation that most directly earns its keep against the TCAS precedent.

**Stop condition 1 does not fire** — generalisation is supportable without a new experiment, at the narrower strength.

---

## 4. Stop condition 2 is the real intellectual risk

*"C1 materially duplicates the validated prior work after removing mechanism novelty."*

The sharpest threat is **Kang (2026), GAIE**, recorded as N-16 in the addendum. Its Oversight Classification Model is a **deterministic total function** over a four-dimensional vector producing discrete governance levels, with **monotonicity, fail-safety and totality established by construction**.

That is three of C1's four candidate formal properties, in a governance framework, published 2026. Add Baxi (2026) — nested permission sets with proved monotone scaling — and ACAS X — formal verification of state-conditioned advisory logic — and the position is:

> **C1's formal apparatus is not distinctive. The properties exist in our formalism; they are not novel.**

§5's instruction to separate `PROPERTY_EXISTS_IN_OUR_FORMALISM` from `PROPERTY_IS_NOVEL` is therefore not a formality — it is the crux, and every one of totality, monotonicity and containment will land as `PASS_WITH_SCOPE` at best.

### What remains genuinely distinctive

Two things, and the candidate C1 wording mentions neither:

1. **The combination** — governed object is an admissible *recommendation-type* set presented to a human, conditioned on a *multi-component externally classified environmental state*, with containment proved over that set. Kang conditions on task metadata and governs oversight; Baxi conditions on agent robustness and governs executable permissions; TCAS conditions on one scalar and does not abstract.
2. **The operational-form semantics** — `ρ_{D,τ}`, the four distinguished ⊥ conditions, Theorem C.1b operational totality, declared exclusions pinned at SAFE with lower-bound propagation, the fault-versus-exclusion distinction, and the explicit fail-open/fail-safe asymmetry for κ. **No validated precedent carries anything comparable.** This is the most under-sold element in the whole evidence base.

**Recommendation:** C1 should lead on the combination and the operational-form treatment, and should present totality/monotonicity/containment as *properties the formalism establishes* rather than as contributions in themselves.

---

## 5. A structural consequence the task does not spell out

Going from three headline contributions to two does **not** demote implementation fidelity from a headline slot — fidelity was never one of v3's three.

v3's current contributions are: **(1) a review**, (2) the architecture, (3) empirical characterisation. Contribution 1 reads: *"from 72 papers… it is concluded that no architecture identified restricts AI advisory scope as a function of classified environmental safety state."*

That is the exact claim the novelty audit falsified in unscoped form. So the contribution that dissolves in this freeze is **the review**. It becomes Related Work positioning — which is also where the TCAS precedent must be acknowledged. Worth stating explicitly in the freeze so the outline task does not carry a phantom third contribution forward.

---

## 6. Corpus count — low risk, answer already exists

`docs/canonical/review-protocol.md` §Corpus reconciliation (resolved 2026-09-07) already fixes **72** as "the subset that advanced to full review at manuscript submission… the reviewer-facing figure", against 111 active corpus and 112 (now 118) files.

The four questions in §13 answer cleanly:

1. **Yes** — the structured review sample remains 72.
2. **Yes** — the six validated sources are described separately as targeted post-review literature added during reviewer-driven novelty validation.
3. **No** — targeted novelty-defence citations are not an SLR sample; they were found by a bounded mechanism audit, not by the search protocol.
4. **Yes** — merging them into 72 without re-running search and screening would compromise methodological consistency, and would also misrepresent how they were found.

One wrinkle to name rather than trip over: review-protocol says 72 should not change *"unless the manuscript is resubmitted with a new methodology"*. The rebuild **is** a resubmission, but the review methodology is unchanged and the sample is unchanged, so 72 stands. **Stop condition 7 does not fire.**

---

## 7. Dispositions I would recommend

| Item | Recommendation | Reasoning |
|---|---|---|
| Implementation fidelity | `SUPPORTING_IMPLEMENTATION_EVIDENCE`, sited inside C1 as an executable-conformance subsection | Containment was demonstrated only on the restrictive side — four CAUTION rules, `Delay` only, empty SAFE rule set. With the mechanism no longer novel, "we built one and it conformed" carries less independent weight |
| C1↔C3 = 0.00% | **Inside C2**, as its sharpest single result | It is the result showing an intermediate state does not automatically produce advisory differentiation. Demoting it to Discussion wastes the strongest empirical finding |
| Hysteresis | **Omit from the contribution story**; Discussion only if space, with the precautionary qualification intact | E4 is PRIMARY-only, secondary, and the six-page budget is tight. Reporting 10.36% without the qualification would restate a withdrawn claim |
| Human authority invariance | Architecture description **and** the comparison table; **not** C1 wording | The audit found the distinction real but thin against TCAS, where authority is procedurally constrained rather than structurally unconditional |
| Title | **RETAIN** | "*Evaluating* Graduated Advisory-Scope Governance for AI Decision Support" — the operative verb claims evaluation, not invention, which is precisely the repositioned contribution. No symbols, no subtitle |

---

## 8. RQ-direction pre-assessment

| RQ | Verdict | Reasoning |
|---|---|---|
| RQ1 — specification as a general runtime governance abstraction | **NEEDS_REWORDING** | Directionally right, but "general" must be scoped to match whatever replaces "domain-independent" in §3.3. Also note it is answered by construction, not by experiment |
| RQ2 — how often outcomes differ from participation-only governance | **ALIGNED** | Maps directly onto ΔL2 and the comparator set; fully provenanced |
| RQ3 — are differences preserved under the alternative configuration | **NEEDS_REWORDING** | "Preserved" hints at robustness or replication. PRIMARY and RESOLUTION are **alternative configurations**, not confidence intervals, repeated trials or error bars, and E3's mandatory scope is `{E1, E2, E6}`. Reword toward "how the quantities differ under the alternative environmental-data configuration" |

---

## 9. Stop-condition pre-assessment

| # | Condition | Assessment |
|---|---|---|
| 1 | Generalisation needs a new experiment | **Does not fire** at the narrower strength (§3.3); *would* fire if "domain-independent" were forced |
| 2 | C1 duplicates validated prior work | **Does not fire, but narrowly.** Survives on the combination plus operational-form semantics (§4), not on the formal properties |
| 3 | C2 unstateable without implying improved safety | **Does not fire** — "governance-outcome divergence" states it without any safety claim |
| 4–6 | Wording requires E5 / H3 / human study | **Do not fire** — none of the candidate wording touches these |
| 7 | Corpus count requires reopening the review | **Does not fire** (§6) |
| 8 | Numerical conflict between frozen authorities | **Does not fire** (§2.1); one provenance asymmetry, not a conflict |
| 9 | Wording requires changing architecture / thresholds / comparators / evidence | **Does not fire** |

Expected outcome: **`CONTRIBUTION_FREEZE_V2 = CLOSED` with `HEADLINE_CONTRIBUTIONS = 2`.**

---

## 10. Decisions to settle during execution

1. **The generalisation formulation** — "domain-reinstantiable", "domain-agnostic at the governance-contract level", or "generalised beyond a single hazard variable". This choice propagates into C1, RQ1 and the title check.
2. **Whether C1 leads on the operational-form semantics** (§4). My view: it should, because that is the part no precedent touches.
3. **Whether frozen C2 cites the pairwise RESOLUTION values** (§2.2), and if so, whether a provenance row is added first.
4. **Explicit recording that the review contribution dissolves** (§5), so the outline task does not carry a phantom third contribution.

---

## 11. Verdict

The task is **executable**. No stop condition fires on present evidence, and the two-contribution structure is supportable.

The work concentrates in one place: **the C1 phrase audit**. Most phrases will land `PASS_WITH_SCOPE` rather than `PASS`, "domain-independent" should land `WEAK` and be replaced, and the honest version of C1 is narrower than the candidate wording but rests on two things — the combination, and the operational-form treatment — that no validated precedent occupies.

C2 is the stronger contribution of the two. No validated source empirically characterises how often an intermediate governance level changes the outcome relative to participation-only governance. That should be reflected in how the two are ordered and weighted.

---

## 12. Files inspected

Read-only. Nothing modified; no task artefact created.

- `docs/tasks/AMICT CONTRIBUTION FREEZE V2 — POST-NOVELTY REPOSITIONING.md`
- `data/amict-conference-rebuild/` — all four existing artefacts
- `publications/active/journal-1/algorithm-specification.md`, `evaluation-specification.md`, `submissions/v1-initial-submission/manuscript.md`
- `publications/active/ipsci-2026/submissions/v3-revision/manuscript-v3.md`
- `docs/canonical/appendix-c-formalisation.md`, `review-protocol.md`, `report-c8-migration-2026-09-08.md`
- `data/journal1-manuscript-evidence-sync/quantitative-provenance.csv`
- `scripts/condition_comparison.py`
- `notes/` — the six validated novelty comparators plus Kang (2026), Baxi (2026), Flehmig et al. (2024)
