# Section 5 Plan: Formal Architecture

**Document type:** Writing plan  
**For:** Journal 1 — Safety Science submission  
**Date:** 2026-08-08  
**Status:** Approved — ready to draft

---

## 1. Role of Section 5 in the Paper

Section 5 is the **formal specification** of the architecture. It defines every symbol, function, and structural component precisely enough that a reader could independently implement or verify the system. It does not prove properties — that is Section 6's job. Section 5 states the definitions and asserts the key properties; Section 6 proves them.

The boundary is strict:
- **Section 5:** Define E, f(E), G(S), A_AI(S), the layer structure, RS(S) supply — state Theorems C.1, C.2, C.3 but do not prove them here
- **Section 6:** Prove all three theorems with full case analysis

This separation keeps Section 5 readable as a specification document and keeps Section 6 self-contained as a theoretical contribution.

---

## 2. Section Outline

### 5.1 Architecture Overview (~0.5 page)

**Purpose:** Orient the reader with the formal pipeline before the definitions begin.

**Content:**
- The four-step formal pipeline: E → S = f(E) → (G(S), A_AI(S)) → AI(E) → Human Decision
- One-sentence role of each step
- Forward-reference to the four-layer structure (Section 5.6)
- Statement that all components are formally defined in Sections 5.2–5.6

**Source:** `architecture-illustration.md` Section 1 (pipeline diagram); `appendix-c-formalisation.md` Section C.8

**Tone:** Formal but accessible — this is the last paragraph that can assume no prior technical vocabulary.

---

### 5.2 Environmental State Representation (~1 page)

**Purpose:** Formally define the input domain of the system.

**Content:**
- Definition of E = {w, r, m, o, v, t} as a tuple of six observable parameters
- For each component: symbol, type (ℝ≥0, ordinal categorical, or interval), and domain
- Table: symbol | type | domain | variable name
- Brief justification for each parameter's inclusion (one sentence each — full empirical justification is in the Foundations section, not here)
- Statement that all six parameters are observable by non-AI sensors — this is a formal requirement for governance independence (the governance layer must not depend on the system it governs)
- Note that v (vessel category) is a fixed operational parameter, not a dynamic environmental reading

**Source:** `appendix-c-formalisation.md` Section C.1 (full definitions); `architecture-illustration.md` Section 5.1

**Key judgment:** Do not reproduce the full empirical justification paragraphs from C.1 here. Section 5 is specification, not justification. One sentence per parameter is enough; cite the full justification in a footnote or forward-reference to the Related Work / Foundations section.

---

### 5.3 Safety State Classification Function (~1.5 pages)

**Purpose:** Define S = f(E) precisely, including the severity order, per-component functions, threshold values, and aggregation rule.

**Content in order:**

**(a) Severity order (Definition 5.1)**
- Define the total strict order ≻ on {SAFE, CAUTION, UNSAFE}: UNSAFE ≻ CAUTION ≻ SAFE
- State transitivity and totality
- This is the formal basis for worst-case aggregation and for Theorem 5.2 (Monotonicity) in Section 6

**(b) Per-component classification functions**
- Define g_i : domain(xᵢ) → {SAFE, CAUTION, UNSAFE} for each of the six parameters
- Threshold table (MET Malaysia verified, August 2026):

| Parameter | SAFE | CAUTION | UNSAFE | MET basis |
|---|---|---|---|---|
| g_w(w) | < 22 kn | 22–27 kn | > 27 kn | Category 1 onset 40 km/h; Category 2 onset 50 km/h |
| g_r(r) | {none, light, moderate} | {heavy} | {storm} | Ribut Petir threshold: > 20 mm/hr |
| g_m(m) | {none} | {Category 1 advisory} | {Category 2/3, Ribut Petir, Ribut Taufan} | MET three-tier warning system |
| g_o(o) | < 1.5 m | 1.5–3.5 m | > 3.5 m | Category 1 max wave 3.5 m |
| g_v(v) | {big} | {small, medium} | — | No UNSAFE for vessel category alone |
| g_t(t) | 06:00–17:00 | 17:00–19:00 | 19:00–06:00 | Night navigation risk (Atacan & Düzbastılar 2023) |

- Source citation for thresholds: MET Malaysia Kriteria Amaran Angin Kencang dan Laut Bergelora (https://www.met.gov.my/en/ramalan/angin-kencang-and-laut-bergelora/, verified August 2026)
- Note on g_v: vessel category alone does not trigger UNSAFE; its classification contributes to max-severity aggregation

**(c) Worst-case aggregation and Theorem 5.1 (Totality)**
- Define: f(E) = max-severity(g_w(w), g_r(r), g_m(m), g_o(o), g_v(v), g_t(t))
- Explain max-severity: returns the element greatest under ≻
- State **Theorem 5.1 (Totality of f):** for all E ∈ domain(E), f(E) is defined and returns exactly one element of {SAFE, CAUTION, UNSAFE}
- Proof deferred to Section 6.1 — note here that totality follows from exhaustive domain coverage of each gᵢ and totality of max-severity over a finite set

**Source:** `appendix-c-formalisation.md` Sections C.2, Theorem C.1; `data-source-met-malaysia.md` Section 4

---

### 5.4 Governance Pair: G(S) and A_AI(S) (~1 page)

**Purpose:** Define the two-level governance mechanism — the core architectural contribution.

**Content in order:**

**(a) Recommendation type space**
- Define R = {Go, Delay, DepartureTime, Duration}
- One sentence on what each type represents
- Grounding: these four types map to the departure decision structure documented by Gao (2024) — forward reference

**(b) AI participation gate G(S) — Level 1**
- Define G : {SAFE, CAUTION, UNSAFE} → {0, 1}
  - G(SAFE) = 1, G(CAUTION) = 1, G(UNSAFE) = 0
- G = 0: AI disabled; G = 1: AI enabled
- Note: G alone cannot express CAUTION — it is binary

**(c) AI-admissible recommendation space A_AI(S) — Level 2**
- Define A_AI : {SAFE, CAUTION, UNSAFE} → 2^R
  - A_AI(SAFE) = {Go, Delay, DepartureTime, Duration}
  - A_AI(CAUTION) = {Go, Delay}
  - A_AI(UNSAFE) = ∅
- Containment property (stated, proved in Section 6): A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅

**(d) The governance pair**
- The architecture is governed by the pair **(G(S), A_AI(S))**
- Governance table:

| S | G(S) | A_AI(S) | Advisory scope |
|---|---|---|---|
| SAFE | 1 | {Go, Delay, DepartureTime, Duration} | Full |
| CAUTION | 1 | {Go, Delay} | Restricted |
| UNSAFE | 0 | ∅ | None |

- Emphasise: CAUTION is the architectural contribution. Under SAFE and CAUTION, G(S) = 1 in both — participation gate is identical. The distinction lives entirely in A_AI(S). A binary governance architecture cannot express this; it has no Level 2.

**(e) Go recommendation under CAUTION**
- When S = CAUTION, Go ∈ A_AI(CAUTION) but is presented with a caution qualifier
- Recommendation *type* is unchanged; presentation is state-dependent
- This preserves set containment while communicating the risk level

**Source:** `appendix-c-formalisation.md` Sections C.3, C.4, C.5; `architecture-illustration.md` Sections 3, 4

---

### 5.5 Formal Properties (~0.5 page)

**Purpose:** State the three formal properties the architecture must satisfy. Proofs in Section 6.

**Content:**

**(a) Participation Constraint**
- G(S) = 0 ⇒ A_AI(S) = ∅
- Deterministic safety classification overrides AI advisory reasoning unconditionally

**(b) Advisory Restriction Constraint**
- S = CAUTION ⇒ A_AI(CAUTION) ⊊ A_AI(SAFE)
- CAUTION is a governance state with a formally smaller recommendation space, not merely SAFE with a warning label

**(c) Safety Dominance Property**
- For all E, AI(E) ⊆ A_AI(f(E))
- The AI can only generate recommendations within the admissible space defined by the current safety state
- Corollary: if f(E) = UNSAFE then AI(E) = ∅

State that all three are proved in Section 6 (Theorems 6.1, 6.2, 6.3 respectively).

**Source:** `appendix-c-formalisation.md` Sections C.6, C.7

---

### 5.6 Layer Architecture and RS(S) Supply Mechanism (~1.5 pages)

**Purpose:** Describe the four-layer implementation structure and how the Safety Dominance Property is enforced by construction.

**Content in order:**

**(a) Four-layer structure**

| Layer | Name | Function | Computational character |
|---|---|---|---|
| 1 | Environment Input | Produces E = {w, r, m, o, v, t} from sensors/APIs | Observable, non-AI |
| 2 | Deterministic Governance | Computes S = f(E); outputs G(S), A_AI(S) | Deterministic, O(1), threshold comparisons |
| 3 | AI Advisory Reasoning | Generates recommendations AI(E) within RS(S) | Rule-based, configurable per safety state |
| 4 | Human Decision | Fisher receives advisory; makes final go/no-go | Human authority, always final |

- Causal flow is unidirectional: Layer 1 → Layer 2 → Layer 3 → Layer 4
- No feedback from Layer 3 to Layer 2 — the advisory engine cannot influence its own governance configuration
- Layer 2 is computationally independent of Layer 3: governance holds even if the advisory engine is unavailable

**(b) RS(S) rule set supply mechanism**

- Layer 3 is implemented as a production rule system
- Before any reasoning begins, Layer 2 supplies rule set RS(S) to Layer 3:
  - RS(SAFE) = rules producing recommendations in {Go, Delay, DepartureTime, Duration}
  - RS(CAUTION) = rules producing recommendations in {Go, Delay} only
  - RS(UNSAFE) = ∅ — never passed; G(UNSAFE) = 0 gates off Layer 3 entirely
- The rule engine fires only rules present in the active RS(S)
- No rule in RS(CAUTION) produces DepartureTime or Duration → those types cannot appear in AI(E) when S = CAUTION
- The constraint is structural: it holds before generation begins, not by filtering outputs after the fact

**(c) Why rule-based at Layer 3**

Brief justification (2–3 sentences): rule-based engine makes the Safety Dominance Property provable by construction rather than by testing; both Layer 2 and Layer 3 are then verifiable by the same methods (static analysis + exhaustive testing of finite configurations); O(1) inference time satisfies low-resource deployment constraints. Full justification in `justification-layer3-enforcement.md`.

**(d) Governance independence requirement**

All Layer 1 inputs (E vector components) must be observable without depending on the AI system. This is a formal requirement: the governance layer must not depend on the system it governs. A governance configuration that could be influenced by Layer 3's own outputs would not be a formal safety constraint.

**Source:** `architecture-illustration.md` Section 2; `appendix-c-formalisation.md` Sections C.7.1, C.7.2; `justification-layer3-enforcement.md` Sections 2, 3

---

### 5.7 Section Summary (~0.25 page)

**Purpose:** Collect all symbols in one place and restate the formal pipeline.

**Content:**
- Summary table:

| Symbol | Meaning |
|---|---|
| E = {w, r, m, o, v, t} | Environmental–operational state vector |
| S = f(E) | Safety state classification |
| G(S) | AI participation gate |
| A_AI(S) | AI-admissible recommendation space |
| (G(S), A_AI(S)) | Governance pair — the core architectural contribution |
| RS(S) | Rule set supplied to Layer 3 |
| AI(E) | AI-generated recommendations |

- The formal pipeline: E → S = f(E) → (G(S), A_AI(S)) → AI(E) → Human Decision
- Forward reference: Section 6 proves the three formal properties; Section 7 specifies the algorithms; Section 10 describes the experimental evaluation

---

## 3. Target Length

~6 pages of journal text (excluding figures). Section 5 is specification-heavy — precision matters more than length.

**Planned figures:**
- **Figure 1:** Four-layer architecture diagram — adapt from `architecture-illustration.md` Section 2
- **Figure 2:** Advisory scope containment table (SAFE / CAUTION / UNSAFE × recommendation types) — adapt from `architecture-illustration.md` Section 4

---

## 4. Scope Boundaries — What Section 5 Does NOT Do

| Topic | Goes where instead |
|---|---|
| Proofs of Theorems 5.1, 5.2, 5.3 | Section 6 (Theoretical Analysis) |
| Full empirical justification for each E vector component | Section 3 (Foundations) or Section 2 (Related Work) |
| Full justification for rule-based Layer 3 choice | Footnote + `justification-layer3-enforcement.md` |
| Comparison with other governance architectures | Section 2 (Related Work) and Section 6 |
| Experimental evaluation | Section 10 |
| RS(S) rule set contents (actual rules) | Section 9 (Prototype Implementation) |

---

## 5. Source Document Map

| Subsection | Primary source | Secondary source |
|---|---|---|
| 5.1 Overview | `appendix-c-formalisation.md` C.8 | `architecture-illustration.md` S.1 |
| 5.2 E vector | `appendix-c-formalisation.md` C.1 | `architecture-illustration.md` S.5.1 |
| 5.3 f(E) | `appendix-c-formalisation.md` C.2, Theorem C.1 | `data-source-met-malaysia.md` S.4 |
| 5.4 Governance pair | `appendix-c-formalisation.md` C.3–C.5 | `architecture-illustration.md` S.3, S.4 |
| 5.5 Formal properties | `appendix-c-formalisation.md` C.6, C.7 | — |
| 5.6 Layers + RS(S) | `architecture-illustration.md` S.2 | `justification-layer3-enforcement.md` S.2–3 |
| 5.7 Summary | `appendix-c-formalisation.md` Summary | — |

---

## 6. Writing Decisions Resolved Before Drafting

1. **Theorem numbering:** Use Section 5 numbering (Theorem 5.1, 5.2, 5.3) in the journal paper, not the appendix C numbering from the thesis
2. **Proof placement:** All proofs go in Section 6 — do not include them in Section 5, even sketch proofs
3. **Threshold source:** MET Malaysia https://www.met.gov.my/en/ramalan/angin-kencang-and-laut-bergelora/ (verified August 2026) — cite explicitly in the threshold table
4. **Vessel category:** g_v has no UNSAFE classification — small/medium both map to CAUTION. State this explicitly in the table with a note
5. **CAUTION positioning:** Every time CAUTION is introduced, frame it explicitly as the contribution — "the intermediate mode that binary governance architectures cannot express"
6. **Conference paper overlap:** Sections 5.1–5.4 cover similar ground to the conference paper's Section IV. The difference is formalism depth — use Definition/Theorem notation, domain types, and explicit set notation throughout. Do not copy conference paper prose
7. **RS(S) mechanism:** Introduce RS(S) in Section 5.6 but defer the actual rule content to Section 9. Section 5.6 only needs to define the supply mechanism and state its governance role

---

## 7. Next Step

Begin drafting Section 5.1 (Architecture Overview) using this plan as the guide. Work through subsections 5.1 → 5.2 → 5.3 → 5.4 → 5.5 → 5.6 → 5.7 in order. Each subsection can be drafted, reviewed, and refined independently before moving to the next.

---

## 8. Deferred Notation Reference

### max-severity pseudo-code

The manuscript uses `max_≻` formal notation (Definition 5.5) for the worst-case aggregation operator. The original pseudo-code form is preserved here for use in Section 7 (Algorithm Specification) and Section 9 (Prototype Implementation), where algorithmic clarity matters more than mathematical formalism.

**Pseudo-code:**

```
function max-severity(s1, s2, s3, s4, s5, s6):
    # severity order: UNSAFE > CAUTION > SAFE
    for s in [s1, s2, s3, s4, s5, s6]:
        if s == UNSAFE:
            return UNSAFE
    for s in [s1, s2, s3, s4, s5, s6]:
        if s == CAUTION:
            return CAUTION
    return SAFE
```

**Equivalence note:** `max-severity(s1, ..., s6)` = `max_≻ {s1, ..., s6}` — the pseudo-code is an explicit implementation of the formal operator. Both are O(n) in the number of components (O(1) for the fixed six-component E vector).

**Usage guidance:**
- Section 5 (Formal Architecture): use `max_≻` notation
- Section 7 (Algorithm Specification): use pseudo-code form
- Section 9 (Prototype Implementation): use concrete language implementation (Python, etc.)
- Section 6 (Theoretical Analysis): use `max_≻` notation in proofs
