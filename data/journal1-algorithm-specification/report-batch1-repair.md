# Report — Journal 1 Algorithm Specification, Batch 1 · Transition Consistency Repair

**Task:** Journal 1 Algorithm Specification Batch 1 — Transition Consistency Repair
**Task file:** [`docs/tasks/JOURNAL 1 ALGORITHM SPECIFICATION BATCH 1 repair.md`](../../docs/tasks/JOURNAL%201%20ALGORITHM%20SPECIFICATION%20BATCH%201%20repair.md)
**Branch:** `design/journal1-algorithm-specification`
**Reported on:** 2026-09-10
**Maintained authority:** [`publications/active/journal-1/algorithm-specification.md`](../../publications/active/journal-1/algorithm-specification.md)
**Evidence directory:** [`data/journal1-algorithm-specification/`](.)

---

## What the repair does

Removes one bounded implementation over-specification in [`algorithm-specification.md`](../../publications/active/journal-1/algorithm-specification.md) §8 without altering any canonical science.

**Before (over-specified):**

> "When S changes across ticks, the active rule set must be swapped atomically. No stale rule set may persist across a transition."

**After (bounded — mechanism-agnostic):**

> "When `S` changes across decision episodes, the rule set used for the next reasoning episode must be `RS(S_new)`. A reasoning episode must not execute with a rule set inconsistent with the state governing that same episode. The **implementation mechanism** that enforces this consistency — for example atomic swap, immutable snapshot, locking, transactional update, or serialized execution — **is not yet specified** (OPEN-B1-8; §10). Fidelity criterion F3 (evaluation-specification.md §7) tests that no stale or inconsistent rule set is used across a state transition, and its scope is preserved by this bounded wording."

The **consistency requirement is mandatory**; the **enforcement mechanism is bounded OPEN**. That is the whole scientific content of the repair.

---

## Scope guard — nothing else moved

Not touched:

- Any canonical file — `docs/canonical/*`, `scripts/*`, `data/prediction-register.csv`, `data/solar/*`, `data/raw_*`, submitted conference manuscripts.
- Classifier semantics, thresholds, RS(S) rule contents, governance mappings `G(S)` / `A_AI(S)`, Theorem C.3 assumptions A1–A4.
- F3 as a fidelity criterion — its wording in [`evaluation-specification.md`](../../publications/active/journal-1/evaluation-specification.md) §7 is unchanged and remains the authority for testing stale/inconsistent rule-set use across a state transition.
- The seven prior OPEN items OPEN-B1-1..7 — all preserved.

---

## New OPEN item

**OPEN-B1-8 — State/rule-set consistency enforcement mechanism.**

| Field | Value |
|---|---|
| **Status** | OPEN — IMPLEMENTATION DECISION |
| **Item** | The architecture requires state/rule-set consistency for each reasoning episode (algorithm-specification.md §8): the rule set used for the next reasoning episode must be `RS(S_new)` and no reasoning episode may execute with a rule set inconsistent with the state governing that same episode. The concurrency/atomicity primitive that enforces this consistency — atomic swap, immutable snapshot, locking, transactional update, serialized execution, or another equivalent mechanism — is not prescribed. |
| **Reason** | The architecture requires state/rule-set consistency but does not prescribe the concurrency/atomicity mechanism used to achieve it. |
| **Does not block** | Algorithm specification, provided Algorithms 3–4 express the consistency requirement as a precondition/postcondition rather than prescribing an implementation primitive. Fidelity criterion F3 continues to test that no stale or inconsistent rule set is used across a state transition. |
| **Authority section** | algorithm-specification.md §8; evaluation-specification.md §7 (F3). |
| **Do not invent** | Yes — do not select a specific concurrency mechanism in Batch 1. |

---

## Files touched (all appends or bounded edits)

| File | Change |
|---|---|
| [`publications/active/journal-1/algorithm-specification.md`](../../publications/active/journal-1/algorithm-specification.md) | §8 wording repair (atomic-swap sentence replaced); §10 table gains OPEN-B1-8 row |
| [`open-decisions.csv`](open-decisions.csv) | OPEN-B1-8 appended (7 columns, header unchanged) |
| [`semantic-verification-batch1.json`](semantic-verification-batch1.json) | `transition_consistency_requirement_bounded` check added (verdict PASS); `summary` counts refreshed to 19 PASS / 0 FAIL / 1 OPEN; `post_repair_note` added |
| [`closure-batch1.json`](closure-batch1.json) | `post_repair_closure_line`, `post_repair_note`, refreshed OPEN-listing wording, and refreshed semantic-check counts |
| [`change-map-batch1.csv`](change-map-batch1.csv) | Five repair rows appended, one per file touched |
| [`report-batch1.md`](report-batch1.md) | Post-repair section appended with the second closure line |
| [`report-batch1-repair.md`](report-batch1-repair.md) | This standalone report — new |

**No canonical file was modified.**

---

## Semantic check added

`transition_consistency_requirement_bounded` — added by the repair. **Verdict PASS.**

**Evidence.** The algorithm specification requires state/rule-set consistency for each reasoning episode — the rule set used for the next episode must be `RS(S_new)`, and no episode may execute with a rule set inconsistent with the state governing it — while leaving the enforcement mechanism (atomic swap, immutable snapshot, locking, transactional update, serialized execution, or an equivalent) unspecified. This preserves the C.7.1 / Theorem C.3 A2 obligation that `RS(S)` is the rule set actually supplied before reasoning begins, and preserves F3's scope in [`evaluation-specification.md`](../../publications/active/journal-1/evaluation-specification.md) §7. The prior wording ("swapped atomically") over-specified an implementation primitive; the repair removes that over-specification without weakening the requirement. Recorded as OPEN-B1-8.

Updated semantic-verification counts:

| Metric | Before repair | After repair |
|---|---|---|
| PASS | 18 | **19** |
| FAIL | 0 | 0 |
| OPEN | 1 | 1 |
| OPEN ids | `tau_not_invented` (OPEN-B1-1) | `tau_not_invented` (OPEN-B1-1) |

The OPEN-count is unchanged because OPEN-B1-8 is an *implementation decision*, not a specification-semantics gap; the new semantic check itself resolves PASS.

---

## Re-verification

```
python3 data/journal1-algorithm-specification/build.py
integrity: PASS — 16 unchanged, 0 changed
parser:    PASS — 4 CSVs checked
```

- Protected-file integrity — [`integrity-after.json`](integrity-after.json) — 16 canonical files byte-identical to the prior pin.
- CSV parser verification — [`parser-test-batch1.json`](parser-test-batch1.json) — `authority-map.csv`, `operational-contract.csv`, `open-decisions.csv`, `change-map-batch1.csv` all parse under `csv.reader` (strict field-count), `csv.DictReader` and `pandas.read_csv`.

---

## Closure condition

The task's closure condition:

> "Closure only if the implementation mechanism remains OPEN while the state/rule-set consistency requirement remains mandatory."

**Met.**

- **Mechanism OPEN** — OPEN-B1-8 records this explicitly; algorithm-specification.md §8 defers primitive choice; open-decisions.csv row 9 carries the bounded item.
- **Consistency requirement mandatory** — algorithm-specification.md §8 states the requirement in mandatory form ("must be `RS(S_new)`", "must not execute with a rule set inconsistent with the state governing that same episode"); F3 in evaluation-specification.md §7 continues to test conformance.

---

## Verdict

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 1 CLOSED —
TRANSITION CONSISTENCY CONTRACT REPAIRED
```

Batch 1 remains closed on the operational contract ([`report-batch1.md`](report-batch1.md)) and now additionally on the transition-consistency wording. No workstream-closing commit is triggered by this repair; that is deferred to the end of Batch 3 per the task §Branch instruction inherited from Batch 1.

---

*Author: iskandar · Batch 1 Transition Consistency Repair report · 2026-09-10 · Branch: `design/journal1-algorithm-specification`*
