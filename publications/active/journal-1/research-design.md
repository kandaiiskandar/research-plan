# Journal 1 — Research Design

**Date:** 2026-08-06  
**Status:** Research design phase  
**Target submission:** Early 2027

---

## Framing

The conference paper (IPSci 2026 / AMICT) introduced the architecture and established the gap.  
This journal paper is the **definitive scientific account**: formal theory + algorithms + implementation + experimental evidence.

| | Conference | Journal 1 |
|---|---|---|
| **Contribution** | New architecture | New architecture + theory + implementation + evidence |
| **How it will be cited** | "where the idea was first introduced" | "the definitive description of the architecture" |
| **Sections overlapping** | — | Sections 1–5 |
| **Sections new** | — | Sections 6–14 |

---

## Research Questions

> **Maintained authority.** The Journal 1 RQ set, its evidence-type tagging, and the tables that map RQs to metrics live in [`evaluation-specification.md`](evaluation-specification.md) §5. The summary below is a *reader's overview*; the authoritative wording, evidence type and required change per RQ are in the specification and in `data/journal1-evaluation-specification/rq-audit.csv`.

| RQ | Question | Evidence type | Maps to section |
|----|----------|---------------|-----------------|
| RQ-J1 | Can the Safety Dominance Property be proved formally, and under what assumptions does it hold? | **FORMAL** (Theorem 6.3 in Section 6) | Section 6 |
| RQ-J2 | What runtime latency and computational overhead does Layer 2 introduce on the target deployment hardware? | **PERFORMANCE** (descriptive, requires prototype) | Section 8, Section 11 |
| RQ-J3 | On the retrospective replay, how do the admissible-recommendation-set outputs of the proposed graduated architecture (C2) differ from a binary-gated (C1) and ungated (C0) baseline, and what share of the divergence is attributable to Level 2 alone? | **EMPIRICAL-TRACE** (deterministic census; pairwise divergence and isolated Level 2 contribution) | Sections 10–11 |
| RQ-J4 | Which architectural component of the governance pair (G(S) vs. A_AI(S)) accounts for the observed C2 vs. C1 divergence? | **EMPIRICAL-TRACE** (Δ_L2 ablation on the replay) | Section 12 |

*(Wording updated 2026-09-10, Journal 1 Evaluation Specification Alignment. RQ-J3 was previously phrased as "outperform … on advisory scope compliance"; that phrasing collapses a formal invariant, a fidelity claim and an empirical measurement, and it is corrected here to a purely empirical-trace comparison. See `evaluation-specification.md` §5 for the full audit.)*

---

## Formal claims, fidelity criteria and empirical hypotheses

> **Maintained authority.** The claim-type separation and the reclassification of H1–H4 live in [`evaluation-specification.md`](evaluation-specification.md) §6–§8 and `data/journal1-evaluation-specification/hypothesis-audit.csv`. The summary below reflects the *closed* Journal 1 Evaluation Specification Alignment; the historical H1–H4 statements are recorded in the audit CSV.

**Formal propositions** *(proved, not tested)*

- **P1 Totality** — for every valid input, `f(E)` and its operational extension `F_{D,τ}` return exactly one element of `{SAFE, CAUTION, UNSAFE}` (Theorem 6.1).
- **P2 Monotonicity** — `S₁ ≻ S₂ ⇒ A_AI(S₁) ⊆ A_AI(S₂)` (Theorem 6.2), with strict containment `A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅`.
- **P3 Safety Dominance** — for all E, `AI(E) ⊆ A_AI(f(E))`, by construction from the RS(S) supply mechanism under the stated engine assumptions (Theorem 6.3).
- **P4 (J1-P1) C1 ≡ C3 admissible-set equivalence** — the binary participation gate C1 and the Flehmig-style governance topology C3 are output-equivalent on the admissible-set axis: `A_C1(S) = A_C3(S)` for all S (one-line finite-mapping proof).

**Implementation-fidelity criteria** *(test conformance to specification; require Layer 3 build)*

- **F1** (replaces H1) — The Layer 3 rule engine produces no recommendation type outside `A_AI(S)` across an exhaustive test suite / replay. *This tests specification conformance, not that the architecture gives better advice.*
- **F2** (replaces H2) — The count of recommendations outside `A_AI(S)` is exactly zero. *Follows analytically from P3 under a conforming implementation; test verifies conformance.*
- **F3** — RS(S) rule-set switching follows state transitions correctly; no stale rule-set persists across a transition.

**Empirical / trace results** *(deterministic census on retrospective replay; already available for E1, E2, E3, E4)*

- **E1** — Pairwise admissible-set divergence between C0, C1, C2 (canonical departure-window values: `C0↔C1 = 42.88%`, `C0↔C2 = 48.69%` PRIMARY; RESOLUTION mirrored).
- **E2** — Isolated Level 2 contribution `Δ_L2 = div(C0,C2) − div(C0,C1)`: **5.81% PRIMARY / 4.48% RESOLUTION**. *This is the load-bearing empirical result (replaces H4).*
- **E3** — Resolution sensitivity: reporting `E2` in both PRIMARY and RESOLUTION configurations; the spread is a resolution-sensitivity result, not an error bar.
- **E4** — Transition and hysteresis characterisation: 3,661 transitions, 26 genuine oscillations (5.2/yr), 10.36% reduction from hysteresis at hourly resolution (F-6). Frame as measurement, not as remediation of an observed instability.

**Performance criteria** *(genuinely empirical; require prototype)*

- **E5 / RQ-J2** — Governance latency and computational overhead on the target deployment hardware. *Threshold `X ms` for a pass/fail hypothesis is **OPEN** — no externally justified value exists; report as descriptive performance measurement until one does. `H3 threshold = OPEN`.*

**Human / future validation** *(explicitly out of Journal 1 scope)*

- Decision-support utility as a construct is **OPEN — CONSTRUCT DEFINITION REQUIRED**. No operational definition on the replay alone has been established; deferred to a future user study (thesis RQ5).
- Trust, calibrated reliance, advisory utility, task completion and real-world safety outcomes are outside Journal 1's evidence base.

*(The historical H1–H4 hypothesis set was reclassified 2026-09-10 by the Journal 1 Evaluation Specification Alignment. H1 and H2 were analytically predetermined under Theorem 6.3 and became F1/F2; H3's `[X ms]` placeholder was resolved to OPEN; H4 was formalised as `Δ_L2`. See `evaluation-specification.md` and `data/journal1-evaluation-specification/hypothesis-audit.csv`.)*

---

## Research Modules

Each module can be developed, reviewed, and refined independently before integration.

---

### Module 1 — Formal Theory
*Target: Section 6*

**Tasks:**
- [ ] Formalise the Safety Dominance Property as a theorem with stated preconditions
- [ ] Write proof by construction (RS(S) supplies only rules in A_AI(S))
- [ ] Prove monotonicity of A_AI across safety states
- [ ] Prove completeness of f(E) classification
- [ ] Prove worst-case aggregation correctness
- [ ] Identify and document all assumptions explicitly

**Input documents:**
- `docs/canonical/appendix-c-formalisation.md` — all sections
- `docs/canonical/justification-layer3-enforcement.md` — proof by construction

**Deliverable:** A self-contained theory document (4–6 theorems with proofs)

---

### Module 2 — Architecture Specification
*Target: Section 5 + diagrams*

**Tasks:**
- [ ] Produce formal definitions for E, f(E), S, G(S), A_AI(S) — ready for journal-quality typesetting
- [ ] Expand architecture diagram to show all four layers clearly (improve on conference paper Fig. 3)
- [ ] Add state transition diagram with formal notation (S → S' under E change)
- [ ] Add sequence diagram showing runtime flow (observation → classification → gating → reasoning → output)
- [ ] Document hysteresis smoothing mechanism formally

**Input documents:**
- `docs/canonical/architecture-illustration.md`
- `docs/canonical/appendix-c-formalisation.md`

**Deliverable:** Formal architecture specification + 3 publication-quality diagrams

---

### Module 3 — Algorithms
*Target: Section 7 + Section 8*

**Tasks:**
- [ ] Write Algorithm 1: Safety classification (threshold evaluation + worst-case aggregation)
- [ ] Write Algorithm 2: Governance gate evaluation
- [ ] Write Algorithm 3: Rule set supply (RS(S) injection)
- [ ] Write Algorithm 4: Advisory generation within RS(S)
- [ ] Analyse time complexity of each algorithm
- [ ] Analyse space complexity of RS(S) storage
- [ ] Compute worst-case decision latency
- [ ] Compare complexity against low-resource deployment constraints

**Deliverable:** 4 pseudocode algorithms + complexity analysis table

---

### Module 4 — Experimental Framework
*Target: Sections 10–12*

**Tasks:**
- [ ] Finalise three-condition primary comparison design under canonical labels: **C0 Ungated · C1 Binary-gated · C2 Proposed graduated architecture**; **C3 (Flehmig-style topology) is retained as a structural comparator, not a fourth experimental arm** — see `evaluation-baseline-decision.md` (Option C accepted) and `evaluation-specification.md` §4. *(Labels normalised 2026-09-10 from the earlier Journal-local C1/C2/C3 = Ungated/Binary/Proposed scheme; the temporary mapping table has been retired.)*
- [ ] Select/compile historical weather scenarios covering SAFE, CAUTION, and UNSAFE conditions — retained as boundary/fail-safe cases within the larger empirical frame; the retrospective replay is the primary evidence base (see `evaluation-specification.md` §3, §10)
- [ ] Operationalise the metric set per the closed specification (`evaluation-specification.md` §9): **F1–F3** implementation-fidelity criteria (test conformance to A_AI(S); deferred to Layer 3 build); **E1–E4 and E6** empirical-trace metrics (pairwise admissible-set divergence; isolated Level 2 contribution Δ_L2; resolution sensitivity; transition/hysteresis characterisation; C1 ↔ C3 confirmation); **E5** descriptive performance measurement (governance latency and computational overhead). Decision-support utility remains **OPEN — CONSTRUCT DEFINITION REQUIRED** and is outside Journal 1's replay evidence base; deferred to a future user study (RQ5 scope). Do not adopt any metric outside this list.
- [ ] Select baselines and confirm they are comparable: C0 (Ungated) and C1 (Binary-gated) as comparators for C2 (Proposed); C3 (Flehmig-style topology) reported only as J1-P1 structural comparator, not as an experimental arm
- [ ] Design ablation conditions per `evaluation-specification.md` §10: **primary** Δ_L2 = div(C0,C2) − div(C0,C1); **secondary** participation-gate ablation (subsumed by C0 vs. C1), hysteresis removal (measured near-null under canonical spec — do not re-run), worst-case-aggregation via boundary scenarios
- [ ] **Reporting protocol for replay metrics.** The retrospective replay is a **deterministic census of all hourly records in the predefined retrospective study window**. Report exact descriptive values for the analysed trace and configuration under both PRIMARY (5.00 yr, ERA5-Ocean ~50 km) and RESOLUTION (3.25 yr, MFWAM ~8 km). **Do not** apply p-values, significance tests or confidence intervals to any replay metric; the PRIMARY / RESOLUTION spread is a resolution-sensitivity result, not an error bar. The **only** measurement admitting inferential treatment is governance latency (E5), because timing carries genuine runtime variance — for that measurement, report mean, maximum and tail percentiles with the hardware and workload stated. Do not invent an acceptance threshold `X ms` — `H3 threshold = OPEN`.
- [ ] Build simulation/replay environment

**Input documents:**
- `docs/canonical/evaluation-design-rq4.md` — full three-condition design
- `data/` — weather and marine data files

**Deliverable:** Experimental protocol document (can become Section 10 directly)

---

### Module 5 — Results and Writing
*Target: Sections 11–14*

**Tasks:**
- [ ] Run experiments across all conditions and scenarios
- [ ] Produce results tables and figures
- [ ] Run ablation experiments
- [ ] Write Section 11 (Results)
- [ ] Write Section 12 (Ablation Study)
- [ ] Write Section 13 (Discussion) — generalisation, deployment challenges, standards
- [ ] Write Section 14 (Threats to Validity)
- [ ] Write Sections 1–4 (Introduction, Related Work, Foundations, Problem Formulation)
- [ ] Write Section 15 (Conclusion)
- [ ] Write Abstract

**Deliverable:** Complete manuscript draft

---

## Module Sequencing

```
Now (Aug–Sep 2026)
  Module 1 — Formal Theory       ← start here, no implementation needed
  Module 2 — Architecture        ← parallel with Module 1

Oct–Nov 2026
  Module 3 — Algorithms          ← depends on Module 1 being stable
  Module 4 — Experimental Design ← depends on Module 2 being stable

Dec 2026 – Jan 2027
  Module 4 — Run experiments
  Module 5 — Write results

Feb–Mar 2027
  Module 5 — Complete manuscript
  Supervisor review

Apr 2027
  Submit
```

---

## Target Journal — Safety Science

- **Publisher:** Elsevier
- **Quartile:** Scopus Q1 (CiteScore ~10)
- **Submission portal:** https://www.editorialmanager.com/sas/
- **Typical review time:** ~3 months
- **Fit:** Publishes AI safety governance research; safety-critical systems; formal analysis

**Why this fits Safety Science:**
- The formal safety properties (Safety Dominance Property) are directly within scope
- The low-resource deployment context (fisheries safety) is applied safety science
- The comparative evaluation characterises measurable differences in governance behaviour on a deterministic retrospective census and isolates the contribution of graduated advisory-scope restriction (metric E2, Δ_L2). *(Wording bounded 2026-09-10 by the Downstream Instruction Residue Repair: Journal 1 does not measure safety outcomes and does not claim measurable safety improvement — no incident data exists at the study site, Layer 3 is not yet implemented, and human-outcome constructs are out of scope. See `evaluation-specification.md` §15 and §16.)*

**Fallback targets:**
1. Artificial Intelligence Review (Springer) — Q1, CiteScore ~19
2. AI & Ethics (Springer) — Q1–Q2

---

## Pre-Writing Checklist

Before writing any section, confirm these are resolved. The evidence categories reflect the closed [`evaluation-specification.md`](evaluation-specification.md); the historical H1–H4 checklist has been retired.

- [ ] **RQs confirmed** — RQ-J1 (FORMAL) · RQ-J2 (PERFORMANCE, threshold OPEN) · RQ-J3 (EMPIRICAL-TRACE) · RQ-J4 (EMPIRICAL-TRACE, Δ_L2). See `evaluation-specification.md` §5.
- [ ] **Formal claims (P1–P4) proved** — P1 Totality, P2 Monotonicity, P3 Safety Dominance, P4 (J1-P1) C1 ≡ C3 admissible-set equivalence. Proofs in manuscript §6 and §J1-P1 in `evaluation-specification.md` §6. *These are proved, not tested.*
- [ ] **Fidelity criteria (F1–F3) scoped pending Layer 3** — F1 (no output outside A_AI(S)), F2 (zero recommendations outside A_AI(S)), F3 (RS(S) switching correctness at transitions). Not evaluated in Journal 1 unless Layer 3 is built before submission; if so, report as implementation-fidelity measurements, not as behavioural hypotheses (see `evaluation-specification.md` §7, §14).
- [ ] **Empirical-trace evidence (E1–E4, E6) available on classifier alone** — E1 (pairwise divergence), E2 (Δ_L2 = 5.81% PRIMARY / 4.48% RESOLUTION), E3 (resolution sensitivity), E4 (transition/hysteresis characterisation), E6 (C1 ↔ C3 = 0.00%, J1-P1 confirmation). Canonical values already known — report exact descriptive census values, not estimates.
- [ ] **Performance evidence (E5) scoped, threshold OPEN** — governance latency and computational overhead of Layer 2 on target deployment hardware; report as descriptive measurement. **H3 acceptance threshold remains OPEN**; do not invent a value.
- [ ] **Utility construct OPEN, deferred to future human study** — decision-support utility has no operational definition on replay alone; deferred to a future user study (RQ5 scope). Do not invent a utility formula. Trust, calibrated reliance and real-world safety outcomes are outside Journal 1's evidence base.
- [ ] **Baselines justified** — C0 (Ungated) and C1 (Binary-gated) as comparators for C2 (Proposed graduated architecture). C3 (Flehmig-style topology) is a structural comparator only.
- [ ] **Data available** — does `data/` contain sufficient historical hourly records for the retrospective census (43,848 hours over 2020–2024 confirmed under both PRIMARY and RESOLUTION configurations)?
- [ ] **Journal confirmed** — Safety Science vs. fallback decision made.
