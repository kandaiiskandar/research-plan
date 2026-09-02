# Section 6 Plan: Theoretical Analysis

**Document type:** Writing plan  
**For:** Journal 1 — Safety Science submission  
**Date:** 2026-08-09  
**Status:** Approved — ready to draft

---

## 1. Role of Section 6 in the Paper

Section 6 proves the formal properties stated (but not proved) in Section 5. It is the primary theoretical contribution that distinguishes the journal paper from the conference paper — the conference paper asserted these properties; the journal paper proves them.

**The boundary is strict:**
- Section 5: state definitions and assert properties
- Section 6: prove them with full case analysis

All three proofs already exist in `docs/canonical/appendix-c-formalisation.md` (Theorems C.1, C.2, C.3). The work here is adapting them to journal numbering, updating definition references (C.X → Section 5 numbering), and framing each theorem for a Safety Science audience.

---

## 2. Section Outline

### 6.1 Overview (~0.25 page)

**Purpose:** Orient the reader — what is being proved, why it matters, and what the proof method is.

**Content:**
- Three theorems are proved: Totality (6.1), Monotonicity (6.2), Safety Dominance Property (6.3)
- Properties 5.1 and 5.2 (Participation Constraint, Advisory Restriction Constraint) follow directly from definitions and are verified as corollaries of Theorem 6.2
- All proofs are by exhaustive case analysis or by construction over a finite state set — no induction required
- Forward reference: Section 7 specifies the algorithms; Section 9 shows these properties hold in the prototype implementation

---

### 6.2 Theorem 6.1: Totality of f (~0.5 page)

**Statement:** For all E in its domain, f(E) is defined and returns exactly one element of {SAFE, CAUTION, UNSAFE}.

**Proof strategy:** Two-part:
- (i) Each gᵢ is total — every input maps to exactly one classification
- (ii) max_≻ over a finite totally ordered set is always defined and unique

**Case-by-case verification for (i):**
- g_w: [0, 22], (22, 27], (27, +∞) partition ℝ≥0 exhaustively — no gaps, no overlaps ✓
- g_r: all five values {none, light, moderate, heavy, storm} assigned ✓
- g_m: all four values {none, advisory, warning, alert} assigned ✓
- g_o: [0, 1.5), [1.5, 3.5], (3.5, +∞) partition ℝ≥0 exhaustively ✓
- g_v: all three values {small, medium, big} assigned ✓
- g_t: [6.0, 17.0), [17.0, 19.0), [19.0, 24.0) ∪ [0.0, 6.0) partition [0, 24) exhaustively ✓

**Fail-safe extension:** Also prove that the fail-safe rule (xᵢ = ⊥ → f(E) = UNSAFE) preserves totality — it adds a pre-condition that maps ⊥ to UNSAFE before any gᵢ is evaluated.

**Significance statement:** Totality is a necessary condition for runtime governance — a classifier that could fail to return a state would leave the governance layer without a basis for enforcing (G(S), A_AI(S)).

**Source:** `appendix-c-formalisation.md` Theorem C.1

---

### 6.3 Theorem 6.2: Monotonicity of A_AI (~0.75 page)

**Statement:** For all S₁, S₂ ∈ {SAFE, CAUTION, UNSAFE}, if S₁ ≻ S₂ then A_AI(S₁) ⊆ A_AI(S₂).

*Informally:* as the safety state becomes more severe, the AI admissible recommendation space never expands.

**Framing:** Formal safety architectures require that constraints tighten consistently as risk increases. Cite:
- Bloomfield & Rushby (2025) — core expectation of deterministic guards surrounding AI components
- Dalrymple et al. (2024) — required of world model safety specifications under increasing uncertainty

**Proof strategy:** Exhaustive case analysis over the three ordered pairs under ≻:

| Case | S₁ | S₂ | A_AI(S₁) | A_AI(S₂) | Holds? |
|------|----|----|----------|----------|--------|
| 1 | UNSAFE | CAUTION | ∅ | {Go, Delay} | ∅ ⊆ {Go, Delay} ✓ (trivially) |
| 2 | CAUTION | SAFE | {Go, Delay} | {Go, Delay, DepartureTime, Duration} | {Go,Delay} ⊆ {Go,Delay,DT,D} ✓ |
| 3 | UNSAFE | SAFE | ∅ | {Go, Delay, DepartureTime, Duration} | ∅ ⊆ {Go,Delay,DT,D} ✓ (trivially) |

**Corollary 6.2 (Strict Monotonicity):** The inclusions in Cases 1 and 2 are strict (⊊ not just ⊆), producing the containment chain: A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅.

**Corollary 6.3 (Properties 5.1 and 5.2):** Both follow immediately:
- Property 5.1 (Participation Constraint: G(S) = 0 ⟹ A_AI(S) = ∅): G(S) = 0 iff S = UNSAFE; A_AI(UNSAFE) = ∅ by Definition 5.8. ✓
- Property 5.2 (Advisory Restriction Constraint: CAUTION ⟹ A_AI(CAUTION) ⊊ A_AI(SAFE)): follows from Case 2 of Theorem 6.2 (strict subset). ✓

**Significance statement:** Monotonicity guarantees the architecture is well-behaved across state transitions — as conditions deteriorate, advisory scope never expands. Combined with Theorem 6.3, it characterises the full safety behaviour of (G(S), A_AI(S)).

**Source:** `appendix-c-formalisation.md` Theorem C.2

---

### 6.4 Theorem 6.3: Safety Dominance Property (~1 page)

**Statement:** For all E, AI(E) ⊆ A_AI(f(E)).

**Corollary:** If f(E) = UNSAFE then AI(E) = ∅.

**Framing:** This is the load-bearing safety theorem. It guarantees that no environmental state can elicit an AI recommendation that exceeds the admissible scope for that state. The proof is by construction — not by testing, not by runtime verification, but by the structural design of the RS(S) supply mechanism.

**Proof strategy:** Exhaustive case analysis on S = f(E). Uses four assumptions:

| Assumption | Statement |
|------------|-----------|
| A1 | Layer 3 is a rule-based engine — generates only types for which an active rule exists |
| A2 | Layer 2 supplies RS(S) before any reasoning begins (Definition 5.10) |
| A3 | G(S) = 0 ⟹ Layer 3 receives no input; AI(E) = ∅ (Definition 5.11) |
| A4 | The engine fires only rules in the active RS(S); no rule produces a type outside its conclusion |

**Case analysis:**

*Case 1: f(E) = UNSAFE*
- By A3, G(UNSAFE) = 0 → Layer 3 receives no input → AI(E) = ∅ (Definition 5.11)
- A_AI(UNSAFE) = ∅ (Definition 5.8)
- AI(E) = ∅ ⊆ ∅ = A_AI(UNSAFE) ✓

*Case 2: f(E) = CAUTION*
- By A3, G(CAUTION) = 1 → Layer 3 is active
- By A2, Layer 3 receives RS(CAUTION), which contains only rules producing {Go, Delay}
- By A4, AI(E) ⊆ {Go, Delay}
- A_AI(CAUTION) = {Go, Delay}
- Therefore AI(E) ⊆ A_AI(CAUTION) ✓

*Case 3: f(E) = SAFE*
- By A3, G(SAFE) = 1 → Layer 3 is active
- By A2, Layer 3 receives RS(SAFE), which contains only rules producing {Go, Delay, DepartureTime, Duration}
- By A4, AI(E) ⊆ {Go, Delay, DepartureTime, Duration}
- A_AI(SAFE) = {Go, Delay, DepartureTime, Duration}
- Therefore AI(E) ⊆ A_AI(SAFE) ✓

**Remarks to include:**
- Proof is constructive: depends only on RS(S) definitions and G(S), both under the designer's control
- Property holds before generation begins — not by runtime filtering
- This is the key difference from a post-hoc output filter, which could fail or be bypassed

**Source:** `appendix-c-formalisation.md` Theorem C.3 (C.7.2)

---

### 6.5 Composite Guarantee (~0.25 page)

**Purpose:** Summarise what the three theorems together mean for the architecture.

**Content:**
- Theorem 6.1 (Totality): every E produces exactly one S — no undefined governance states
- Theorem 6.2 (Monotonicity): as conditions worsen, advisory scope never expands
- Theorem 6.3 (Safety Dominance): AI output is always within the scope permitted by the current state
- Together: the architecture is total, monotone, and safe-by-construction — three independent guarantees, each proved from definitions alone
- Forward reference: Section 10 evaluates whether these formal guarantees translate to correct behaviour in empirical test scenarios

---

## 3. Target Length

~3 pages of journal text. Section 6 is tighter than Section 5 — the proofs are short (case analysis over three states) and the structure is predictable.

---

## 4. Numbering and Reference Adaptation

All references must use Section 5 definition numbers, not appendix C numbers:

| Appendix reference | Journal reference |
|-------------------|-------------------|
| Definition C.1 (Severity Order) | Definition 5.3 |
| Theorem C.1 (Totality) | Theorem 6.1 |
| Theorem C.2 (Monotonicity) | Theorem 6.2 |
| Theorem C.3 (Safety Dominance) | Theorem 6.3 |
| max-severity | max_≻ |
| RS(S) (C.7.1) | Definition 5.10 |
| AI(E) (C.7.2) | Definition 5.11 |
| A_AI(S) (C.4) | Definition 5.8 |
| G(S) (C.3) | Definition 5.7 |

---

## 5. Scope Boundaries — What Section 6 Does NOT Do

| Topic | Goes where instead |
|-------|--------------------|
| Full rule set contents (RS(SAFE), RS(CAUTION)) | Section 9 (Prototype Implementation) |
| Algorithm pseudocode for f(E) | Section 7 (Algorithms) |
| Empirical validation of thresholds | Section 5.3.2 (already done) |
| Comparison with other governance proofs | Section 2 (Related Work) |
| Experimental verification | Section 10 (Evaluation) |

---

## 6. Source Document Map

| Subsection | Primary source |
|------------|---------------|
| 6.1 Overview | This plan |
| 6.2 Theorem 6.1 (Totality) | `appendix-c-formalisation.md` Theorem C.1 |
| 6.3 Theorem 6.2 (Monotonicity) | `appendix-c-formalisation.md` Theorem C.2 |
| 6.4 Theorem 6.3 (Safety Dominance) | `appendix-c-formalisation.md` Theorem C.3 |
| 6.5 Composite Guarantee | `appendix-c-formalisation.md` Remarks after C.7.2 |
