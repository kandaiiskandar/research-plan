# CAUTION State Architecture: Technical Novelty & Hypotheses
## Reference Document — Not for Submission

*Extracted from research-proposal-draft.md for use in thesis chapters, viva preparation, and journal paper drafts.*

---

## Technical Novelty: The CAUTION State Architecture

The primary architectural innovation of this research lies in the formalisation and implementation of the transitional CAUTION state within a graduated safety-gated framework.

Contemporary AI runtime assurance literature remains constrained by a binary control loop where actions are either entirely permitted or entirely blocked. This research resolves this dilemma by introducing a third discrete state, S = CAUTION, calculated via a deterministic environmental classification function S = f(E). The CAUTION state serves as an architectural pivot point characterised by two distinct properties.

The first is Pre-Inference Governance Coupling (G(S) = 1, A_AI(S) = Restricted). Unlike binary systems that completely shut down when risk escalates, removing all advisory capability precisely when partial guidance remains possible, the CAUTION state keeps the rule-based advisory engine active but structurally shrinks its operational boundaries to a formally bounded advisory scope. This maintains user engagement while preventing the generation of recommendations that exceed what the current conditions can reliably support.

The second is Reasoning-Tier Rule-Set Starvation, a localised architectural protocol defined in this research. Upon triggering the CAUTION state, the system supplies only the restricted rule set RS(CAUTION) to the advisory engine, withholding the production rules in RS(SAFE) \ RS(CAUTION) that are required to compute high-specificity outputs such as departure times and trip durations. By constraining the Admissible Advisory Scope to A_AI(CAUTION) = {Go, Delay} by construction, the architecture suppresses over-precise outputs through an architectural governance mechanism that operates before advisory reasoning begins, not after.

---

## Research Hypotheses

Two hypotheses guide the empirical phases of this research, corresponding to the technical evaluation (RQ4) and contextual validation (RQ5) respectively.

**H1 (Technical):** A graduated safety-state-gated architecture utilising a transitional CAUTION mode will achieve 100% Safety Dominance Property compliance under C2, producing measurably different recommendation output sets under CAUTION conditions compared to binary-gated (C1) and ungated (C0) baselines.

**H2 (Contextual):** Users interacting with the graduated architecture will produce different decision behaviour under the CAUTION state than under the SAFE and UNSAFE states, and will correctly interpret the CAUTION restriction as a scope limitation rather than a display change, without exhibiting system rejection.

---

## Viva Defense Matrix

| Formal Component | Narrow Interpretation | Architectural Interpretation |
|---|---|---|
| Vector E | Weather variables | Operational Design Domain (ODD) parameter array |
| Function f(E) | Threshold check script | Deterministic, immutable pre-inference circuit breaker |
| State S = CAUTION | Warning indicator | Reasoning-tier Rule-Set Starvation toggle |
| Containment property | Feature list | Formal enclosure guaranteeing Safety Dominance by construction |

---

## Placement Notes

- **Thesis Chapter 1 (Introduction):** The two CAUTION properties (Pre-Inference Governance Coupling + Rule-Set Starvation) can be introduced as a dedicated subsection after the problem statement.
- **Thesis Chapter 3 (Methodology):** Rule-Set Starvation and the RS(SAFE) \ RS(CAUTION) mechanism belong in the formal specification section.
- **Thesis Chapter 5 (Discussion):** H1 and H2 outcomes tie directly to the evaluation and user study results chapters.
- **Viva preparation:** The defense matrix reframes each formal component against examiner challenges about whether the work is "just weather thresholds."
