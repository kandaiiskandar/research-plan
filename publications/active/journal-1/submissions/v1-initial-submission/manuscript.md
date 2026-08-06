# A Formally Verified Runtime AI Governance Architecture Based on Graduated Safety-State Gating

**Journal:** Safety Science (Elsevier) — primary target  
**Fallback:** Artificial Intelligence Review (Springer) / AI & Ethics (Springer)  
**Type:** Full research article  
**Status:** Research design phase — v1  
**Date started:** 2026-08-06  
**Target submission:** Early 2027

---

> **Note on relationship to conference paper**
> 
> The IPSci 2026 conference paper (AMICT) introduced the graduated safety-state-gated architecture and established the binary governance gap through a structured literature review. That paper is submitted and complete.
>
> This journal paper is an independent research contribution. It shares the same architecture but treats it as the subject of formal analysis, algorithmic specification, prototype implementation, and experimental validation — objectives that are distinct from the conference contribution. Approximately Sections 1–5 overlap significantly with the conference paper in topic; Sections 6–14 are essentially new research.
>
> **Conference contribution:** New architecture  
> **Journal contribution:** New architecture + formal theory + implementation + experimental evidence

---

## Author Information

- **Author:** Mohd Iskandar Samsuddin
- **Affiliation:** [Your university]
- **Email:** iskandarsamsuddin@gmail.com

---

## Abstract

*(To be written last — after all sections drafted)*

---

## Keywords

*(5–8 keywords — draft after abstract)*

---

## 1. Introduction

**Purpose:** Frame the problem and position the journal contribution distinctly from the conference paper.

**Key content to include:**
- The governance gap (binary vs. graduated) — brief, since this is established in the conference paper
- Why formal analysis, algorithms, and experiments are needed beyond the conference contribution
- The research questions this paper answers (see Research Design section below)
- Paper structure roadmap

*(Draft here)*

---

## 2. Related Work

**Purpose:** Broader and deeper than the conference paper's literature review.

**Key content to include:**
- Full comparison table of governance architectures (expanded from Table II in conference paper)
- Governance standards context: ISO 26262, IEC 61508, ICAO SAL levels, maritime safety standards
- Formal verification literature for AI systems
- Complexity results for related governance problems

> **Source:** Expand from `papers/comparison-table.md` and `papers/review-plan.md`

*(Draft here)*

---

## 3. AI Governance Foundations

**Purpose:** Establish the theoretical substrate — governance standards, formal properties, and the vocabulary the rest of the paper uses.

**Key content to include:**
- Safety governance in regulated industries: what "formally verified" means in this context
- Relevant standards: IEC 61508 SIL levels, ISO 26262 ASIL, maritime safety regulations (SOLAS, COLREGS)
- The participation / advisory scope / execution distinction formalised
- Properties required of a runtime governance mechanism: completeness, monotonicity, decidability

*(Draft here)*

---

## 4. Problem Formulation

**Purpose:** State the problem precisely and formally, distinguishing it from the conference paper's informal framing.

**Key content to include:**
- Formal statement: given E, define the requirements on a runtime governance mechanism M such that M(E) ⊆ A_AI(S)
- What "better" means: compared to what baselines, measured by what metrics
- Assumptions and scope conditions

> **Source:** `docs/canonical/appendix-c-formalisation.md` Sections C.1–C.4

*(Draft here)*

---

## 5. Formal Architecture

**Purpose:** Full formal specification of the architecture — more rigorous than the conference paper's Section IV.

**Key content to include:**
- E = {w, r, m, o, v, t} with formal domain definitions
- S = f(E): formal definition of the classification function, including the threshold structure
- Governance pair (G(S), A_AI(S)): formal definitions
- The containment property: A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅
- Layer structure: Layer 1 (observation), Layer 2 (governance), Layer 3 (rule-based engine)
- How RS(S) is supplied to Layer 3 before inference begins

> **Source:** `docs/canonical/appendix-c-formalisation.md` (all sections)  
> **Source:** `docs/canonical/architecture-illustration.md`  
> **Source:** `docs/canonical/justification-layer3-enforcement.md`

*(Draft here)*

---

## 6. Theoretical Analysis

**Purpose:** Prove the key properties of the architecture. This section does not exist in the conference paper.

**Key properties to prove:**
- **Safety Dominance Property:** For all E, AI(E) ⊆ A_AI(S) — holds by construction (proof by construction from rule set RS(S))
- **Monotonicity:** A_AI is monotone-decreasing in risk: if S₁ is riskier than S₂ then A_AI(S₁) ⊆ A_AI(S₂)
- **Completeness of classification:** f(E) is total — every E maps to exactly one S
- **Worst-case aggregation correctness:** when E contains conflicting signals, the conservative classification wins

> **Source:** `docs/canonical/appendix-c-formalisation.md` Sections C.6–C.7  
> **Source:** `docs/justification/justification-layer3-enforcement.md`

*(Draft here)*

---

## 7. Algorithms

**Purpose:** Pseudocode for each computational component. This section does not exist in the conference paper.

**Algorithms to specify:**
- Algorithm 1: Safety classification S = f(E) — threshold evaluation with worst-case aggregation
- Algorithm 2: Governance gate evaluation — G(S) and A_AI(S) selection
- Algorithm 3: Rule set supply to reasoning engine — RS(S) construction and injection
- Algorithm 4: Runtime advisory generation — symbolic reasoning within RS(S)

**For each algorithm:**
- Inputs, outputs, preconditions, postconditions
- Pseudocode
- Invariant maintained

*(Draft here)*

---

## 8. Complexity Analysis

**Purpose:** Characterise the computational cost of the governance mechanism. This section does not exist in the conference paper.

**Key questions to answer:**
- Time complexity of S = f(E) classification
- Time complexity of A_AI(S) enforcement
- Space complexity of RS(S) rule sets
- Worst-case decision latency
- How complexity scales with |E| and |A_AI|
- Is the governance overhead acceptable for low-resource deployment?

*(Draft here)*

---

## 9. Prototype Implementation

**Purpose:** Describe the software prototype built to demonstrate the architecture. Reference RQ3 from thesis.

**Key content to include:**
- Implementation stack (low-resource constraints: offline-first, lightweight)
- How the three layers are implemented in software
- How RS(S) is encoded and supplied to the reasoning engine
- Hysteresis smoothing at state transition boundaries (mode-chattering prevention)
- Deployment environment: Kota Kinabalu, Sabah, Malaysia fisheries context

> **Source:** `docs/implementation/` documents  
> **Source:** `data/` — weather and marine data files

*(Draft here)*

---

## 10. Experimental Design

**Purpose:** Define the evaluation methodology rigorously. Reference RQ4 from thesis.

**Three-condition comparison (from `docs/canonical/evaluation-design-rq4.md`):**

| Condition | Label | Description |
|-----------|-------|-------------|
| C1 | Ungated | AI generates full-scope output regardless of S |
| C2 | Binary-gated | AI enabled/disabled, no advisory scope restriction |
| C3 | Graduated (proposed) | Full (G(S), A_AI(S)) governance pair |

**Scenarios:** Historical weather replay across SAFE, CAUTION, and UNSAFE conditions

**Metrics:**
- Advisory scope compliance rate: P(AI(E) ⊆ A_AI(S))
- False positive rate: recommendations issued outside A_AI(S)
- Decision support utility: coverage of actionable recommendations within admissible set
- Governance overhead: latency added by governance layer

**Baselines:** C1 and C2 as per evaluation design

**Statistical analysis:** [TBD — specify tests]

> **Source:** `docs/canonical/evaluation-design-rq4.md` (full design)

*(Draft here)*

---

## 11. Results

**Purpose:** Present experimental results against the three conditions and across all metrics.

*(To be written after experiments are run)*

---

## 12. Ablation Study

**Purpose:** Isolate the contribution of each architectural component.

**Ablation conditions to test:**
- Remove advisory scope restriction (A_AI(S) = full set at all states) — reduces to binary gate
- Remove participation gate (G(S) = 1 always) — removes safety disengagement
- Remove hysteresis smoothing — measures mode-chattering frequency
- Remove worst-case aggregation — measures misclassification rate at E boundary conditions

*(To be written after experiments are run)*

---

## 13. Discussion

**Purpose:** Interpret results, generalise beyond the fisheries domain, address deployment challenges.

**Key content to include:**
- What the results mean for the binary governance gap
- Generalisation: which aspects of the architecture are domain-independent
- Deployment challenges in low-resource environments: connectivity, hardware, maintenance
- Relationship to governance standards (IEC 61508, ISO 26262, SOLAS)
- Limitations of the current prototype
- How the architecture could be extended to other safety-critical domains

*(Draft after results)*

---

## 14. Threats to Validity

**Purpose:** Systematic treatment of validity threats. Required for journal submission.

**Internal validity:**
- Classification threshold selection — are the SAFE/CAUTION/UNSAFE boundaries principled?
- Rule set completeness — are RS(S) sets exhaustive for the fisheries domain?
- Prototype fidelity — does the implementation faithfully realise the formal specification?

**External validity:**
- Generalisability beyond Malaysian coastal fisheries
- Applicability to non-symbolic AI reasoning engines
- Scalability to larger E vectors

**Construct validity:**
- Does advisory scope compliance rate measure what it claims?
- Is historical weather replay a valid proxy for real deployment?

*(Draft after results)*

---

## 15. Conclusion

**Purpose:** Summarise contributions, situate within CS literature, state future work.

**Key content to include:**
- The journal contribution in one paragraph (distinct from conference paper)
- Formal properties proved
- Experimental evidence summary
- Future work: multi-domain generalisation, formal certification pathways, user study (RQ5)

*(Draft last)*

---

## References

*(To be compiled — use `docs/canonical/citation-notes-map.md` for citation keys)*

---

## Figures

*(Place figures in `/figures/` subfolder and reference here)*

**Planned figures:**
- Figure 1: Three governance dimensions (adapted from conference paper)
- Figure 2: Full architecture diagram with all four layers (expanded from conference paper Fig. 3)
- Figure 3: State transition diagram with formal notation
- Figure 4: Algorithm flow diagrams
- Figure 5: Experimental results — condition comparison across metrics
- Figure 6: Ablation results
