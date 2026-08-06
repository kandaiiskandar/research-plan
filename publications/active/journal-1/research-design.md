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

*(Define these before writing any section — every section should be driven by these)*

| RQ | Question | Maps to section |
|----|----------|-----------------|
| RQ-J1 | Can the Safety Dominance Property be proved formally, and under what assumptions does it hold? | Section 6 |
| RQ-J2 | What is the computational complexity of the governance mechanism? Is it feasible for low-resource deployment? | Section 8 |
| RQ-J3 | Does a graduated governance mechanism outperform binary-gated and ungated baselines on advisory scope compliance? | Sections 10–11 |
| RQ-J4 | Which architectural components are responsible for the observed performance gains? | Section 12 |

---

## Hypotheses

*(Testable claims the experiments will confirm or refute)*

- **H1:** The graduated architecture achieves higher advisory scope compliance than binary-gated and ungated baselines across SAFE, CAUTION, and UNSAFE conditions.
- **H2:** The graduated architecture produces lower false positive rate (recommendations outside A_AI(S)) than both baselines.
- **H3:** The governance overhead (latency) added by the governance layer is below [X ms] — acceptable for low-resource deployment.
- **H4:** Removing the advisory scope restriction (ablation) reduces compliance to the level of the binary-gated baseline.

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
- [ ] Finalise three-condition comparison design (C1 Ungated, C2 Binary-gated, C3 Graduated)
- [ ] Select/compile historical weather scenarios covering SAFE, CAUTION, and UNSAFE conditions
- [ ] Define metrics formally: advisory scope compliance rate, false positive rate, utility, latency
- [ ] Select baselines and confirm they are comparable
- [ ] Design ablation conditions (4 ablations)
- [ ] Specify statistical tests (significance threshold, test type)
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
- The experimental comparison against baselines demonstrates measurable safety improvement

**Fallback targets:**
1. Artificial Intelligence Review (Springer) — Q1, CiteScore ~19
2. AI & Ethics (Springer) — Q1–Q2

---

## Pre-Writing Checklist

Before writing any section, confirm these are resolved:

- [ ] **RQs confirmed** — are RQ-J1 through RQ-J4 the right questions?
- [ ] **Hypotheses testable** — can H1–H4 be evaluated with available data?
- [ ] **Metrics defined** — advisory scope compliance rate, false positive rate, utility, latency — are these operationalised?
- [ ] **Baselines justified** — why C1 (ungated) and C2 (binary-gated) are the right comparators
- [ ] **Data available** — does `data/` contain sufficient historical weather scenarios for experiments?
- [ ] **Formal proofs scoped** — are the theorems in Module 1 provable from the current formal model?
- [ ] **Journal confirmed** — Safety Science vs. fallback decision made
