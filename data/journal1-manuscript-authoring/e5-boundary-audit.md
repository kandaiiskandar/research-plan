# Batch 8B-1 — E5 Boundary Audit

**Scope:** the region authored by this sub-batch — manuscript Sections 9–12 (lines 745–1162 after authoring).
**Manuscript:** `publications/active/journal-1/submissions/v1-initial-submission/manuscript.md`
**Hash before:** `c1ef469e98101233` · **Hash after:** recorded in `integrity.json`

E5 is the boundary most easily crossed by accident, because the reference measurements exist, are precise, and look like results. Every occurrence of a performance-adjacent term in the authored region is classified below. No occurrence was REVISED or REMOVED, because none was written in a prohibited form in the first place — each was authored inside its bound.

---

## 1. Term scan

| Term | Occurrences in §§9–12 | Lines |
|---|---|---|
| `E5` | 6 | 889, 891, 942, 946, 1084, 1086 |
| `benchmark` | 5 | 889, 944, 1088, 1090, 1104 |
| `performance` | 10 | 767, 889, 915, 940, 948, 968, 1084, 1086, 1100, 1102 |
| `latency` | 8 | 767, 889, 891, 942, 948, 960, 1100, 1102 |
| ` ms` | 2 | 948, 1102 |
| `CPU` | 2 | 942, 1098 |
| `memory` | 3 | 767, 942, 1098 |
| `MacBook` | 1 | 1090 |
| `M3` | 1 | 1090 |
| `Android` | 1 | 1100 |
| `mobile` | 1 | 1100 |
| `target hardware` | 3 | 863, 889, 946 |
| `real-time` | 2 | 1100, 1102 |
| `deployment` / `deploy` | 11 | 749, 789, 824, 859, 863, 891, 942, 1022, 1086, 1100, 1102 |
| `milliseconds` (spelled out) | 0 | — |

---

## 2. Occurrence-by-occurrence classification

| Line | Context | Classification | Basis |
|---|---|---|---|
| 749 | "research prototype, not a deployed system" | **ALLOWED** | Negates deployment; no field trial claimed |
| 767 | Offline-first operation, with explicit disclaimer that it is not a latency/memory/energy claim | **ALLOWED** | Structural property, bounded in the same paragraph |
| 789 | Table 4 caption — "deployment site" (geographic reference) | **ALLOWED** | Refers to the study site, not to a deployed system |
| 824 | "not exhaustive over deployment conditions" | **ALLOWED** | Negation of a prohibited scope claim |
| 859, 863 | §9.7 Deployment context; "Whether the implementation actually meets the resource constraints of representative target hardware is an empirical question that §11.7 addresses and does not close" | **ALLOWED** | States the open status explicitly |
| 889 | Table 7 row: E5 = PERFORMANCE, **OPEN** | **ALLOWED** | Status statement |
| 891 | RQ-J2 described as answered by E5, "which is open" | **ALLOWED** | Status statement |
| 915 | "performance decay" — describes the precedent architecture's degradation index | **ALLOWED** | Unrelated to E5; refers to comparator semantics |
| 940–948 | §10.4 protocol: harness validated; target-hardware measurement not completed; `H3 = X ms` OPEN | **ALLOWED** | Protocol plus explicit open status and no threshold |
| 960 | Latency admits distributional treatment, "bounded, as that subsection makes explicit, to the machine on which it was measured" | **ALLOWED** | Bound stated inline |
| 968 | "performance evidence remain separable" — evidence-class taxonomy | **ALLOWED** | Structural reference |
| 1022 | "decision changed" / C0 never deployed | **ALLOWED** | Negation |
| 1084–1088 | §11.7 heading and "**E5 is OPEN.**" | **ALLOWED** | Status statement |
| 1090 | Table 12 caption, hardware profile, "**Reference only — not target-hardware evidence.**" | **ALLOWED** | Labelled development-machine reference at point of use |
| 1098 | Peak RSS as process-lifetime peak, not per-episode; CPU as measured-loop user time, not utilisation | **ALLOWED** | Measurement semantics preserved exactly |
| 1100 | "They are not deployment performance, target-hardware performance, mobile performance, **Android** performance, real-time performance or production performance" | **ALLOWED** | The sole Android and mobile occurrence is a **prohibition**, not a result |
| 1102 | `H3 = X ms` remains OPEN and UNSUPPORTED; low reference latency is not a threshold pass | **ALLOWED** | Explicit refusal to close H3 |
| 1104 | Target-hardware benchmarking outstanding and mandatory; no emulator/CI/cloud substitute | **ALLOWED** | Future-work statement with substitution explicitly refused |

**Totals: ALLOWED 100% · REVISED 0 · REMOVED 0.**

---

## 3. Success criteria

| Criterion | Result | Evidence |
|---|---|---|
| No target-hardware result invented | **PASS** | No numeric latency, memory or CPU value is attributed to target hardware anywhere in §§9–12. Every numeric value in Table 12 is captioned `DEVELOPMENT_MACHINE_REFERENCE`. |
| No Android result invented | **PASS** | One `Android` occurrence (line 1100), inside a sentence prohibiting the reading. No Android numeric value exists in the manuscript. |
| No H3 threshold invented | **PASS** | Both `H3` occurrences in the authored region are the form `H3 = X ms` with OPEN/UNSUPPORTED status. No numeric substitution for `X`. |
| No MacBook → Android extrapolation | **PASS** | Line 1100 explicitly forbids scaling; no scaling factor, estimate or projection appears. |
| E5 remains OPEN | **PASS** | Stated at lines 889, 946, 1086; `target_hardware_evidence = false` unchanged in the source artefact. |

---

## 4. Note carried to Batch 8B-2

Sections 13–15 and the Abstract are undrafted and will introduce new opportunities to cross this boundary — particularly the Abstract, where a performance sentence is tempting and where §42 of the original brief permits mention only of the fact that target-hardware characterisation is pending. This audit covers §§9–12 only. **The whole-manuscript E5 audit must be re-run over the complete text in 8B-2**, not assumed to hold from this pass.
