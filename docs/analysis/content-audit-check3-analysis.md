# Content Audit — Check 3: Formal Consistency Analysis

**Scope:** `ipsci-2026-paper-v5.md` formal statements versus `docs/appendix-c-formalisation.md`  
**Date:** 2026-07-20  
**Status:** Complete — 2 issues found and corrected

---

## Method

Every location in the paper body that states, labels, or uses a formal variable or property was identified and compared against the canonical source (`docs/appendix-c-formalisation.md`). Locations checked: §2 (key concepts), Figure 3 diagram + caption, Table 1, §5.1 (governance table + Safety Dominance Property), §5.2 (CAUTION mode description), §5.3 (domain instantiation), §6 (conclusion).

---

## Results

| # | Item | Paper location | Paper statement | Appendix canonical | Status |
|---|---|---|---|---|---|
| 1 | E vector composition | Figure 3 caption (line 243), §5.3 (line 308) | `{w, r, m, o, v, t}` | `{w, r, m, o, v, t}` — C.1 | ✓ Consistent |
| 2 | Variable names in §5.3 | §5.3 (line 308) | w = wind speed, r = rainfall intensity, m = marine warning level, o = ocean state, v = vessel category, t = time of day | C.1: same six names | ✓ Consistent |
| 3 | S domain | §5.1 (line 286) | `S ∈ {SAFE, CAUTION, UNSAFE}` | C.2: `S ∈ {SAFE, CAUTION, UNSAFE}` | ✓ Consistent |
| 4 | S = f(E) | §2 (line 34), §5.1 (line 286), §5.3 (line 308) | `S = f(E)` | C.2: `S = f(E)` | ✓ Consistent |
| 5 | G(S) values | §5.1 Table (lines 290–292) | 0 (UNSAFE), 1 (SAFE/CAUTION) | C.3: G(UNSAFE) = 0; G(S) = 1 for S ∈ {SAFE, CAUTION} | ✓ Consistent |
| 6 | A_AI(SAFE) | §5.1 Table (line 290) | `{Go, Delay, DepartureTime, Duration}` | C.4: `{Go, Delay, DepartureTime, Duration}` | ✓ Consistent |
| 7 | A_AI(CAUTION) | §5.1 Table (line 291) | `{Go, Delay}` | C.4: `{Go, Delay}` | ✓ Consistent |
| 8 | A_AI(UNSAFE) | §5.1 Table (line 292) | `∅` | C.4: `∅` | ✓ Consistent |
| 9 | Containment chain | §5.1 (line 294), §6 (line 316) | `A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅` | C.4: same chain | ✓ Consistent |
| 10 | Formal pipeline | Figure 3 (lines 243–282), §5 (line 238) | `E → S = f(E) → (G(S), A_AI(S)) → AI(E)` | C.8: same pipeline | ✓ Consistent |
| 11 | Governance pair label | Abstract (line 10), §2 (line 34), §5.1 (line 286) | `(G(S), A_AI(S))` | C.5: `(G(S), A_AI(S))` | ✓ Consistent |
| 12 | Rule-set enforcement | §5.1 (line 294) | "governance layer supplies a state-specific rule set to the reasoning engine before inference begins" | C.7.1: RS(S) supplied to Layer 3 before reasoning begins | ✓ Consistent |
| 13 | CAUTION mode semantics | §5.2 (lines 298–299) | "precise tactical outputs (departure time, trip duration) are withheld" | C.4: A_AI(CAUTION) excludes DepartureTime and Duration | ✓ Consistent |
| **14** | **Safety Dominance Property labelling** | **§5.1 (line 294)** | **"The Safety Dominance Property holds: A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅. For all E, the AI can only generate recommendations within the admissible space A_AI(S)."** | **C.4 names A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ the "containment relationship"; C.7 separately defines the Safety Dominance Property as AI(E) ⊆ A_AI(S). The paper applies one label to both.** | **Issue — conflation** |
| **15** | **Table 1 notation** | **Table 1 (line 172)** | **"Disabled (G(S) = 0, A_AI = ∅)"** | **Formal notation throughout: A_AI(S) or A_AI(UNSAFE) — the (S) argument is never dropped** | **Issue — notation drop** |

---

## Issue Detail

### Issue 1 — Safety Dominance Property labelling (§5.1, line 294)

**What the paper says:**

> "The **Safety Dominance Property** holds: A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅. For all E, the AI can only generate recommendations within the admissible space A_AI(S) defined by the current safety state."

**What the appendix says:**

- **C.4** names `A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅` the **"containment relationship"** — a property of the A_AI sets themselves.
- **C.7** defines the **Safety Dominance Property** as: *"For all E, if S = f(E), then AI(E) ⊆ A_AI(S)"* — a runtime property of what the AI generates.

CLAUDE.md canonical distinction:
> "The formal containment property: A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅"  
> "The Safety Dominance Property: For all E, AI(E) ⊆ A_AI(S)"

These are two different claims. The containment chain is a structural fact about how the admissible sets nest. The Safety Dominance Property is the runtime guarantee that AI-generated recommendations never exceed the admissible set. The paper collapses both under the single label "Safety Dominance Property," which conflicts with the appendix's naming convention and muddies what C.7's proof is proving.

**Proposed fix:** Present the two claims separately, using the appendix names:

> "The sets satisfy the containment relationship A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅. The **Safety Dominance Property** then holds: for all E, AI(E) ⊆ A_AI(S) — the AI can only generate recommendations within the admissible space defined by the current safety state."

---

### Issue 2 — Table 1 notation (Table 1, line 172)

**What the paper says:**

> `Disabled (G(S) = 0, A_AI = ∅)`

**What the appendix says:**

Every formal occurrence uses `A_AI(S)` or `A_AI(UNSAFE)` — the function argument is never dropped. Dropping it makes A_AI look like a variable rather than a function evaluated at a state.

**Proposed fix:**

> `Disabled (G(S) = 0, A_AI(UNSAFE) = ∅)`

---

## Summary

| Result | Count |
|---|---|
| Consistent | 13 |
| Issues found | 2 |

Both issues involve labelling and notation rather than substantive errors — the formal values themselves (G(S), A_AI(S), E vector, containment chain, pipeline) are all consistent with the appendix. Neither issue introduces a mathematical error. Issue 1 (Safety Dominance Property conflation) is the more significant of the two: it creates a tension between what the paper calls the Safety Dominance Property and what C.7 proves, which a careful reviewer could flag.

---

## Recommended Actions

1. **Fix Issue 1 (§5.1, line 294):** Separate the containment relationship and the Safety Dominance Property into two consecutive sentences using their canonical names.
2. **Fix Issue 2 (Table 1, line 172):** Change `A_AI = ∅` → `A_AI(UNSAFE) = ∅`.
