# Report — Journal 1 Algorithm Specification, Batch 3

**Task:** Journal 1 Algorithm Specification — Batch 3: Algorithms 3 & 4 (Rule-Set Supply and Governed Advisory Generation)
**Task file:** [`docs/tasks/Journal 1 Algorithm Specification batch 3.md`](../../docs/tasks/Journal%201%20Algorithm%20Specification%20batch%203.md)
**Branch:** `design/journal1-algorithm-specification`
**Reported on:** 2026-09-10
**Maintained authority:** [`publications/active/journal-1/algorithm-specification.md`](../../publications/active/journal-1/algorithm-specification.md) (Batches 1 & 2 sections unchanged; Batch 3 adds §§17–24)
**Evidence directory:** [`data/journal1-algorithm-specification/`](.)

---

## Algorithm 3 — Rule-Set Supply

Publication-quality pseudocode supplying `RS(S)` to Layer 3 for the current decision episode. Full text at [`algorithm-specification.md §17`](../../publications/active/journal-1/algorithm-specification.md), contract at §18 and [`algorithm-contracts-batch3.csv`](algorithm-contracts-batch3.csv).

**Signature.**

```text
Input  : S ∈ {SAFE, CAUTION, UNSAFE};  G(S) ∈ {0,1};  A_AI(S) ⊆ R;  repository;
         candidate : repository × S → 2^repository
Output : RS(S) satisfying ConclusionTypes(RS(S)) ⊆ A_AI(S) and RS(UNSAFE) = ∅
         OR a bounded CONFIGURATION_FIDELITY_FAILURE (no reasoning begins)
```

**Procedure summary.**

1. **Gate-off short-circuit** (lines 1–3). `G(S) = 0 ⇒ RS ← ∅ ⇒ return`. No rule set is supplied to reasoning.
2. **Compliance check on candidate rule set** (lines 5–9). If any `ρ ∈ candidate(repository, S)` has `type(ρ) ∉ A_AI(S)` → **refuse supply** and return `CONFIGURATION_FIDELITY_FAILURE`. **No silent filtering, no `S` modification, no new safety state.**
3. **Supply RS(S)** (lines 10). `RS ← RS_candidate`. Runs **before any Layer 3 rule firing**.

**Contract.** P1: `S` valid A1 output. P2: `(G(S), A_AI(S))` from A2. P3: repository configured with `type(ρ) ∈ R`. P4: reasoning has not yet begun. Q1: `ConclusionTypes(RS(S)) ⊆ A_AI(S)`. Q2: `G(S) = 0 ⇒ RS(S) = ∅`. Q3: `RS(UNSAFE) = ∅`. Q4: no `AI(E)` element produced. Q5: invalid repository refuses supply; `S` not modified; runtime handling beyond refusal is bounded OPEN-B3-1.

**State/rule-set consistency across episodes.** On `S_old → S_new`, A3 is re-invoked on `S_new`. The concurrency primitive is not chosen — OPEN-B1-8 preserved.

---

## Algorithm 4 — Governed Advisory Generation

Publication-quality pseudocode invoking Layer 3 only when participation is permitted. Full text at [`algorithm-specification.md §19`](../../publications/active/journal-1/algorithm-specification.md), contract at §20.

**Signature.**

```text
Input  : E (same as A1); S; G(S); A_AI(S); RS(S) from A3;
         engine (production rule symbolic reasoner satisfying Theorem C.3 A4)
Output : AI(E) ⊆ A_AI(S)   — holds by construction
```

**Procedure summary.**

1. **Gate-off path** (lines 1–3). `G(S) = 0 ⇒ AI ← ∅ ⇒ return`. No rule firing; no advisory. State-reporting UI is outside `AI(E)`.
2. **Participating path** (line 5). `AI ← engine.reason(E, RS)`. Engine has `RS(S)` in scope and **no other rule sets**. No post-hoc runtime filter on `AI`.

**Contract.** P1: `S` valid. P2: `(G(S), A_AI(S))` from A2. P3: `RS(S)` from A3 with A3 Q1–Q3 holding. **P4: Engine fidelity assumption** (Theorem C.3 A4) — implementation assumption; Batch 3 does not test it. P5: `RS(S)` is `RS(S_current)`, not stale. Q1: `AI(E) ⊆ A_AI(S)` — Safety Dominance (Theorem C.3); holds by construction. Q2: `G(S) = 0 ⇒ AI(E) = ∅`. Q3: no advisory type outside `A_AI(S)` — by P3 and P4, not by post-hoc filter. Q4: human authority unconditional.

**Bounded correctness language.** Algorithm 4 *implements* the enforcement contract on which Theorem C.3 depends (A1–A4). It **does not** independently prove Safety Dominance.

---

## Safety Dominance dependency

The runtime guarantee `AI(E) ⊆ A_AI(S)` is delivered by a four-link chain. Full detail at [`safety-dominance-trace-batch3.csv`](safety-dominance-trace-batch3.csv) and [`algorithm-specification.md §22`](../../publications/active/journal-1/algorithm-specification.md).

```
  A_AI(S)
    │                                                        L1 — definition (appendix-c C.4)
    ▼
  ConclusionTypes(RS(S)) ⊆ A_AI(S)
    │                                                        L2 — algorithmic enforcement contract (A3 Q1)
    ▼
  engine fires only rules present in active RS(S)
  and produces no output beyond fired-rule conclusion types
    │                                                        L3 — implementation assumption (Theorem C.3 A4; A4 P4)
    ▼
  AI(E) ⊆ A_AI(S)                                            L4 — formal theorem (Theorem C.3)
```

**Classification of each link:**

| Link | Statement | Category |
|---|---|---|
| **L1** | `A_AI : S → 2^R` | **Definition** — appendix-c C.4 |
| **L2** | `ConclusionTypes(RS(S)) ⊆ A_AI(S)` | **Algorithmic enforcement contract** — A3 Q1, enforced at §17 lines 5–9 (no silent filtering) |
| **L3** | Engine fires only rules in active `RS(S)`; no rule produces a type outside its own conclusion | **Implementation assumption** — Theorem C.3 A4; A4 P4. Future **fidelity obligation** F1/F2 |
| **L4** | `AI(E) ⊆ A_AI(S)` | **Formal theorem** — Theorem C.3 (Safety Dominance), proved in appendix-c C.7.2 |

**Consequence.** Batch 3 does **not** re-prove Safety Dominance. It makes L2 an explicit algorithmic contract and L3 an explicit engine-fidelity assumption, so that Theorem C.3's antecedents (A1–A4) are visibly discharged by the algorithm pipeline. F1–F3 validate L3 in future.

---

## State verification

Seven state-space checks at [`state-cases-batch3.csv`](state-cases-batch3.csv). **All PASS.**

| # | Algorithm | State / setup | Expected | Result |
|---|---|---|---|---|
| SC1 | A3 | S = SAFE, compliant repository | `RS(SAFE)` with types in `{Go, Delay, DepartureTime, Duration}` | **PASS** |
| SC2 | A3 | S = CAUTION, compliant repository | `RS(CAUTION)` with types in `{Go, Delay}` | **PASS** |
| SC3 | A3 | S = UNSAFE | `RS = ∅` (short-circuit) | **PASS** |
| SC4 | A4 | S = SAFE + `RS(SAFE)` | `AI ⊆ {Go, Delay, DepartureTime, Duration}` | **PASS** |
| SC5 | A4 | S = CAUTION + `RS(CAUTION)` | `AI ⊆ {Go, Delay}` | **PASS** |
| SC6 | A4 | S = UNSAFE | `AI = ∅` — no rule firing | **PASS** |
| SC7 | A3 | invalid rule repository | refuse supply; `S` unchanged; runtime handling beyond refusal is OPEN-B3-1 | **PASS** |

---

## Transition verification

Six transition checks at [`transition-cases-batch3.csv`](transition-cases-batch3.csv). **All PASS.**

| # | `S_old → S_new` | Expected on next episode | Result |
|---|---|---|---|
| TC1 | SAFE → CAUTION | `A_AI` shrinks to `{Go, Delay}`; `RS(CAUTION)` supplied; DepartureTime/Duration no longer available | **PASS** |
| TC2 | CAUTION → SAFE | `A_AI` expands to FULL; `RS(SAFE)` supplied; timing/duration re-available | **PASS** |
| TC3 | CAUTION → UNSAFE | `G = 0`; `A_AI = ∅`; `RS = ∅`; `AI = ∅`; Layer 3 not invoked | **PASS** |
| TC4 | UNSAFE → CAUTION | `G = 1`; `A_AI = {Go, Delay}`; `RS(CAUTION)` supplied; Layer 3 re-enabled restricted | **PASS** |
| TC5 | SAFE → UNSAFE | `G = 0`; `A_AI = ∅`; `RS = ∅`; `AI = ∅` | **PASS** |
| TC6 | UNSAFE → SAFE | `G = 1`; `A_AI` FULL; `RS(SAFE)` supplied; full scope | **PASS** |

**These are specification checks, not F3 fidelity results.** F3 is a future implementation-fidelity test on a built Layer 3 (evaluation-specification.md §7).

---

## OPEN decisions

Three new bounded OPEN items originate in Batch 3. Full audit at [`open-decisions-batch3.csv`](open-decisions-batch3.csv).

| ID | Item | Status | Blocks |
|---|---|---|---|
| **OPEN-B3-1** | Invalid rule-repository runtime handling | OPEN — IMPLEMENTATION DECISION | Fault-response wiring only; governance contract unaffected |
| **OPEN-B3-2** | Rule-engine evaluation strategy | OPEN — IMPLEMENTATION DECISION | Complexity analysis (deferred to a later batch) |
| **OPEN-B3-3** | Decision-episode implementation boundary | OPEN — IMPLEMENTATION DECISION | Runtime implementation and OPEN-B1-8 mechanism selection |

**All eight Batch 1 OPEN items preserved unchanged.** In particular:

- **OPEN-B1-4** (Layer 3 prototype / concrete rule contents) — Algorithm 3 defines only the shape and admissibility contract for `RS(S)`, not its scientific contents.
- **OPEN-B1-8** (state/rule-set consistency enforcement mechanism) — Algorithm 3's consistency invariant is specification-level; §17 explicitly lists atomic swap, immutable snapshot, locking, transactional update, serialized execution as admissible without choosing one.

No Batch 1 or Batch 2 OPEN item was silently closed.

---

## F1–F3 boundary

**Batch 3 defines what implementation fidelity must satisfy; it supplies no fidelity evidence.**

| | Batch 3 role | Future prototype role |
|---|---|---|
| **F1** — Recommendations outside `A_AI(S)` = 0 | Defines the L2 + L3 chain that F1 tests; specifies the engine-fidelity assumption (A4 P4) whose runtime satisfaction F1 measures | Layer 3 prototype under exhaustive test suite / replay — evaluation-specification.md §7 |
| **F2** — Zero violation count | Same as F1 above; L3 is what F2 counts against | Layer 3 prototype under replay |
| **F3** — RS(S) switching correctness at transitions | Defines the state/rule-set consistency invariant (A3 note; A4 P5); TC1–TC6 are the specification checks the future F3 test will operationalise | Layer 3 prototype running through simulated / real state transitions |

**The transition checks TC1–TC6 do not constitute F3 PASS.** They verify that the specification is internally coherent about which `RS(S)` should apply on which episode; F3 will verify that a built prototype honours the invariant at runtime.

---

## Files changed

Full record with scientific effect per file at [`change-map-batch3.csv`](change-map-batch3.csv).

**Maintained authority (edited):**

- [`publications/active/journal-1/algorithm-specification.md`](../../publications/active/journal-1/algorithm-specification.md) — eight new sections §§17–24 added. Scientific effect: **none** — new algorithm specification sections implementing the CLOSED Batch 1 operational contract and CLOSED Batch 2 Algorithms 1 & 2. No concrete rules, no engine strategy, no complexity analysis, no canonical file modified. Batches 1 & 2 sections unchanged.

**Evidence directory (created):**

| File | Rows | Purpose |
|---|---|---|
| [`algorithm-contracts-batch3.csv`](algorithm-contracts-batch3.csv) | 24 | A3 and A4 inputs, outputs, preconditions, postconditions, bounded-language notes |
| [`state-cases-batch3.csv`](state-cases-batch3.csv) | 7 | SC1–SC7 — three A3, three A4, one invalid-RS. All PASS |
| [`transition-cases-batch3.csv`](transition-cases-batch3.csv) | 6 | TC1–TC6 — all pairwise transitions among {SAFE, CAUTION, UNSAFE}. All PASS |
| [`safety-dominance-trace-batch3.csv`](safety-dominance-trace-batch3.csv) | 4 | Four-link dependency chain L1 → L2 → L3 → L4 with categories |
| [`algorithm-traceability-batch3.csv`](algorithm-traceability-batch3.csv) | 15 | Constructs mapped across six categories |
| [`open-decisions-batch3.csv`](open-decisions-batch3.csv) | 3 | OPEN-B3-1..3 |
| [`semantic-verification-batch3.json`](semantic-verification-batch3.json) | 25 checks | 23 PASS / 0 FAIL / 2 OPEN (matching bounded OPENs OPEN-B3-1 and OPEN-B3-2) |
| [`parser-test-batch3.json`](parser-test-batch3.json) | 7 CSVs | All PASS; auto-generated by `build.py` |
| [`change-map-batch3.csv`](change-map-batch3.csv) | 12 | File-level change record |
| [`closure-batch3.json`](closure-batch3.json) | closure record | Closure with §30 checklist |
| [`report-batch3.md`](report-batch3.md) | this report | — |

**Evidence directory (edited):**

- [`build.py`](build.py) — `partition_csvs()` extended for Batch 3; emits `parser-test-batch3.json`.

**Canonical files touched:** none.

---

## Protected integrity

Same 16 protected canonical files as Batches 1 & 2.

- **Unchanged:** 16
- **Changed:** 0
- **Verdict:** `PASS — 16 unchanged, 0 changed`

Full record at [`integrity-after.json`](integrity-after.json), regenerated by `python3 build.py`.

Stop conditions from task §29 — none raised:

| Stop condition | Status |
|---|---|
| `RS_ENFORCEMENT_AUTHORITY_CONFLICT` | NOT RAISED |
| `PRE_REASONING_ENFORCEMENT_CONTRACT_INCOMPLETE` | NOT RAISED |
| `SAFETY_DOMINANCE_DEPENDENCY_GAP` | NOT RAISED |
| `NEW_SCIENTIFIC_DECISION_REQUIRED` | NOT RAISED |
| `PROTECTED_CANONICAL_STATE_DRIFT` | NOT RAISED |

---

## Verdict

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 3 CLOSED —
RULE-SET ENFORCEMENT AND GOVERNED ADVISORY CONTRACT VERIFIED
```

Closure criteria in task §30 met: all items MET; state cases 7/7 PASS; transition cases 6/6 PASS; semantic checks 23 PASS / 0 FAIL / 2 OPEN (both matching bounded OPEN items introduced by this batch); protected canonical state unchanged; F1–F3 remain future fidelity evidence; complexity analysis and E5 benchmarking remain deferred.

**Workstream status.** The full four-algorithm specification workstream (Batches 1–3, plus two closed repairs) is now CLOSED at the specification level. Concrete Layer 3 rule contents (OPEN-B1-4), rule-engine evaluation strategy (OPEN-B3-2), state/rule-set consistency enforcement primitive (OPEN-B1-8), invalid RS runtime handling (OPEN-B3-1), decision-episode boundary (OPEN-B3-3), latency threshold (OPEN-B1-6), utility construct (OPEN-B1-7), runtime provenance capture (OPEN-B1-2), medium-vessel evidence (OPEN-B1-3), live `g_m` configuration (OPEN-B1-5), and freshness parameters (OPEN-B1-1) all remain bounded OPEN.

---

*Author: iskandar · Batch 3 report · 2026-09-10 · Branch: `design/journal1-algorithm-specification`*
