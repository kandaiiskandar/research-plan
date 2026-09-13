# Journal 1 — Evaluation Specification F1–F3 / E5 Status Synchronisation Micro-Repair

**Date:** 2026-09-13 · **Branch:** `docs/journal1-manuscript-evidence-sync` · **HEAD:** `34b7b00`
**Specification:** `bfc6038516c998b3` → **`5a0e706a9b982e92`** (+21 / −13)
**Manuscript:** `a91ede5ff8518e46` → **unchanged**
**Verification:** 43 PASS · 0 FAIL · 0 OPEN

---

## 1. Objective

The maintained evaluation specification still represented F1–F3 as OPEN and Layer 3 as unbuilt, two days after the Batch 5 evaluation closed all three PASS. Batch 8B-1 authored §§9–12 against the CLOSED status and recorded the discrepancy rather than fixing it in passing. This repair fixes it in isolation, before 8B-2 drafts interpretive prose against the same document.

This was documentation-authority synchronisation. No scientific evaluation was performed.

---

## 2. Contradiction established before editing

The whole file was searched — not only the three reported sections — using eleven status patterns. Thirty-three candidate lines were returned and every one was classified before any edit was made.

| Classification | Count | Meaning |
|---|---|---|
| **ACTIVE-STALE** | 7 | Asserted a status contradicted by closed evidence. Repaired. |
| **PARTIALLY-STALE** | 3 | Status correct, surrounding claim stale (E5's blocker; the "future build" phrasing). Repaired narrowly. |
| **HISTORICAL** | 2 | Describes a superseded state and is correct as such. Preserved. |
| **NOT-STALE** | 3 | Genuinely open items — H3, decision-support utility, RQ5. Preserved. |
| **OUT-OF-SCOPE** | 1 | The E3/E4 contract. Not reopened. |

Full inventory: `status-occurrence-inventory.csv` (16 rows, section / before / after / stale_status / authoritative_status / evidence / classification).

**The search found stale loci beyond the three reported sections.** §1 and §18 both carried stale wording that the 8B-1 report had not identified, and §16 carried a phrasing that implied no build existed. Had the repair been confined to §7, §14 and §17 as flagged, three loci would have survived.

---

## 3. Authoritative status, re-derived

Every figure was recomputed from Batch 5 artefacts rather than taken from the task brief. All 21 arithmetic and structural checks held:

```
292 primary episodes = 32 SAFE + 260 CAUTION
454 advisory records across 244 episodes with a non-empty advisory
260 CAUTION − 16 empty = 244
F1 violations = 0 · F2 violations = 0 · F3 mismatches = 0
162 UNSAFE gate-off cases — separate from the 292
rule advisory sum = 130 + 108 + 108 + 108 = 454
R-SAFE-001 = DEFERRED, times_selected = 0
only conclusion type generated = Delay
scope = interface-contract exhaustive; retrospective_replay_run = false
```

---

## 4. Repairs applied

Ten loci across §§1, 7, 11, 14, 16, 17 and 18. Full before/after in `diff-audit.md`. In summary:

- **§7** — `OPEN — deferred to Layer 3 build` → `CLOSED — PASS`, with the measured counts and a bounded-interpretation paragraph.
- **§11** — E5's **status stays OPEN**; its stale *blocker* ("Blocked by Layer 3 build") was corrected to target-hardware availability, and the full E5 boundary set was made explicit.
- **§14** — Layer 3 recorded as specified **and implemented**, with the four CAUTION rules and `ComponentStateTrace`, explicitly as a research prototype.
- **§17** — `OPEN-3` struck through and annotated CLOSED rather than deleted; new `OPEN-5` records the live E5 target-hardware dependency.
- **§18** — the fidelity block in the final matrix updated with per-criterion zero counts and scope.
- **§1, §16** — two short phrase corrections.

**The SAFE-rule limitation was added because the closure could not be stated accurately without it.** Recording F1–F3 as CLOSED without it would have converted a bounded result into an apparent demonstration that the full SAFE advisory space was exercised — which is precisely what Decision 3 of Batch 8B-1 forbids. §7 now carries the interface-contract scope, the `R-SAFE-001` deferral, the empty `RS(SAFE)`, the 32 zero-advisory SAFE episodes, and `Delay` as the only generated type.

---

## 5. Boundaries preserved

| Item | Status after repair |
|---|---|
| P1–P4 | CLOSED, FORMAL, unchanged |
| F1–F3 | **CLOSED — PASS**, IMPLEMENTATION_FIDELITY, bounded |
| E1–E4, E6 | CLOSED, EMPIRICAL_TRACE, unchanged — no value recomputed |
| E3 scope | `{E1, E2, E6}` — unchanged |
| E4 | CLOSED, PRIMARY-only; `E4_RESOLUTION = NOT_REQUIRED_BY_CURRENT_E3_DESIGN` — unchanged |
| **E5** | **OPEN** — target-hardware benchmarking outstanding |
| E5 harness | CLOSED |
| MacBook | `DEVELOPMENT_MACHINE_REFERENCE`, `target_hardware_evidence = false` |
| Android | `DEFERRED_MANDATORY` |
| H3 | `H3 = X ms` — OPEN/UNSUPPORTED |
| R-SAFE-001 | DEFERRED |

An explicit check, `not_all_evaluation_closed`, guards the specific failure this repair could have caused: turning "F1–F3 CLOSED" into "all evaluation CLOSED". It passes.

---

## 6. Verification — 43 PASS, 0 FAIL, 0 OPEN

**Negative controls.** Ten prohibited mutations were injected in turn and the corresponding checks observed. Nine failed as they should. **One did not**, and it was a defect in my check rather than in the repair:

> `stale_F1_OPEN_removed` **passed** a mutation that restored `all three are **OPEN — deferred to Layer 3 build**`. The check scanned for `F1` within 40 characters of `OPEN` on a single line — but the stale wording never named F1 on its status line; it said *"all three are OPEN"*. The check was testing a property the defect did not have.

The check was rewritten to scan the fidelity sections (§7, §14, §18) as **blocks** for any surviving OPEN or deferred status assertion, in addition to the token scan. Re-running the controls against all three criteria now fails each correctly, identifying the exact residual string and its section. This is the same class of error caught twice in Batch 8A and once in 8B-1: a check that passes because it is asking the wrong question.

**Historical-line exclusion.** The scan excludes three line classes that match stale patterns by design — this repair's own provenance note, §18's description of the frozen CSV's staleness, and the struck-through `OPEN-3` row. Excluding them is necessary; excluding them *by content* rather than by line number is what keeps the exclusion honest if the file moves.

**Integrity.** One scientific file changed: the specification. The manuscript is byte-identical at `a91ede5ff8518e46`. All eleven Batch 8B-1 artefacts are byte-identical to their preflight hashes. Every other protected file was checked against the hashes **Batch 5 independently recorded**, not against a baseline this repair took of itself. Diff is +21/−13 in a single file.

---

## 7. Status

```
P1–P4 = CLOSED
F1–F3 = CLOSED
R_SAFE_001 = DEFERRED
E1–E4 = CLOSED · E6 = CLOSED
E3_SCOPE = {E1, E2, E6}
E4_RESOLUTION = NOT_REQUIRED_BY_CURRENT_E3_DESIGN
E5 = OPEN
E5_HARNESS = CLOSED · MACBOOK_REFERENCE = COMPLETE
MACBOOK_CLASSIFICATION = DEVELOPMENT_MACHINE_REFERENCE
target_hardware_evidence = false
E5_ANDROID_TARGET_BENCHMARK = DEFERRED_MANDATORY
H3 = OPEN/UNSUPPORTED
BATCH_8B_1 = CLOSED
BATCH_8B_2 = READY
FINAL_REVIEWER_READY = false
```

**Closure:**

```
JOURNAL 1 EVALUATION SPECIFICATION F1–F3 / E5 STATUS SYNCHRONISATION MICRO-REPAIR CLOSED —
STALE IMPLEMENTATION-FIDELITY STATUS REMOVED, CLOSED F1–F3 EVIDENCE SYNCHRONISED,
AND OPEN E5 TARGET-HARDWARE BOUNDARY PRESERVED
```
