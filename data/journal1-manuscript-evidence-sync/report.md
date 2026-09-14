# Journal 1 — Batch 8A: Existing Manuscript Evidence Synchronisation & Claim Alignment

**Date:** 2026-09-13 · **Branch:** `docs/journal1-manuscript-evidence-sync` · **HEAD:** `fcbbe8d297a5`
**Manuscript:** `51bcd6f627090f26` → **`c1ef469e98101233`** (905 → 928 lines, 36 insertions / 13 deletions)

---

## 1. Scope as executed

Batch 8A synchronised the prose that already exists and isolated the prose that does not. It authored **no new scientific prose** for Sections 9–15, ran no experiment, changed no scientific code, added no citation, and did not close E5.

The scope decision rested on a finding from the blocked run: **Sections 1–4 and the Abstract are stubs as well**, not only 9–15. Only Sections 5–8 contain drafted prose. "Synchronise Sections 1–8" therefore resolved to **§§5–8**, and the success criterion "Abstract wording bounded to closed evidence" was satisfiable only by marking — there was no abstract prose to bound.

## 2. Deliverables

| Artefact | Content |
|---|---|
| `manuscript-claim-inventory.csv` | **38 material claims** across the whole manuscript, typed and status-classified |
| `claim-evidence-matrix.csv` | **13 rows** (P1–P4, F1–F3, E1–E6) — the editing authority |
| `quantitative-provenance.csv` | **23 quantities**, every one traced to a source file and field |
| `claim-change-log.csv` | **18 rows**, 15 with a semantic change, 3 NO_CHANGE groups |
| `manuscript-diff-audit.md` | Every changed paragraph classified; zero unmatched propositions |
| `e5-status-audit.md` | E5 occurrence-by-occurrence audit + eight absence checks |
| `integrity.json`, `verification.json`, `parser-test.json` | 45/45 PASS; all CSVs parse under `DictReader` and `pandas` |

## 3. Repairs applied — 13 loci

**Status statements falsified by closed evidence (8):** "runtime fidelity is not yet demonstrated"; rule-set content "remains to be implemented"; "Section 10 plans to evaluate implementation fidelity"; "a future implementation-fidelity test (F1, F2)"; "as when Layer 3 is not yet built"; Section 9's "planned … once implemented"; "Planned implementation stack targets"; and the Section 5.7 pointer that conflated closed evidence with undrafted sections.

**Internal contradiction (1):** Definition 5.1's table typed `r` as scalar `ℝ≥0` while Definition 5.2a in the same section defines `X_r = ℝ≥0 × K`. Retyped.

**Authority pointer (1):** "supplementary design rationale (available from the authors)" → the in-repository Layer 3 prototype specification.

**Dangerous stub instruction (1):** Section 11 instructed *"Do NOT report fidelity metrics (F1–F3) here — they are deferred to the Layer 3 build"*. F1–F3 are CLOSED; the instruction contradicted frozen authority and would have mis-steered Batch 8B. Rewritten to preserve the correct reason for keeping them out of §11 — they are implementation-fidelity, not empirical-trace evidence — rather than the false one.

**E3/E4 contract compliance (2):** the two loci carrying E4 figures now identify them as **PRIMARY** temporal-dynamics findings, per the E3/E4 authority micro-repair, one citing `E4_RESOLUTION = NOT_REQUIRED_BY_CURRENT_E3_DESIGN` directly.

## 4. Undrafted sections isolated

The Abstract and eleven sections (1–4, 9–15) carry an explicit marker naming `claim-evidence-matrix.csv` as the authority to draft against and stating that **E5 target-hardware performance remains OPEN and must not appear as a completed result**. The constraint now travels with every section Batch 8B will author, rather than living only in a task brief.

## 5. What was deliberately not inserted

**No empirical result was added to the manuscript.** E1, E2, E4 and E6 are closed and their values verified, but Sections 11–12 are undrafted; inserting results would have been authoring, not synchronisation. All values sit in `claim-evidence-matrix.csv` with `required_action = DEFER to Batch 8B`, each with its allowed scope and prohibited overclaim. The MacBook reference latencies (M-23) were likewise verified against Batch 7A at full precision and **not** placed in prose.

## 6. E5

`E5 = OPEN`. The manuscript names E5 only as an outstanding dependency — four occurrences, each verified. No Android result, no reference value in prose, no latency threshold, no PASS/FAIL against H3, and no statement that the Android benchmark failed. Both `H3` occurrences are the mandated form **`H3 = X ms` remains OPEN**.

## 7. Verification — 45 PASS, 0 FAIL, 0 OPEN

Three checks failed on first run and were **corrected rather than loosened**, because each tested the wrong property:

| Check | Why the original was wrong |
|---|---|
| `Android_result_not_invented` | Tested `"Android" not in manuscript`. The single occurrence is inside the Batch 8A Abstract marker *prohibiting* an Android result — a prohibition, not a result. Corrected to test for an Android numeric latency or a scaled/simulated value. |
| `H3_open_unsupported` | Tested `"H3" not in manuscript`. The brief **requires H3 to be preserved** as `H3 = X ms` OPEN/UNSUPPORTED, not removed. Corrected to test that every occurrence is that form with no numeric threshold substituted. |
| `specification_files_unchanged` | Compared against a baseline recorded *before* the E3/E4 micro-repair. `evaluation-specification.md` changed `64c2c786 → bfc60385` in that authorised separate task and is unchanged since. Corrected to compare against the micro-repair post-state. |

All three corrections are recorded in `verification.json` under `check_corrections` with the evidence for each.

**Batch 8A changed exactly one file:** the manuscript. Canonical architecture, all specification files, governance code, every evaluation script, Batch 5 evidence, Batch 7A evidence and the prediction register are byte-identical.

## 8. Status

```
P1–P4 = CLOSED
F1–F3 = CLOSED
E1–E4 = CLOSED
E5 = OPEN · E5_HARNESS = CLOSED · MACBOOK_REFERENCE = COMPLETE
E5_ANDROID_TARGET_BENCHMARK = DEFERRED_MANDATORY · H3 = OPEN/UNSUPPORTED
E6 = CLOSED
MANUSCRIPT_EVIDENCE_SYNC (8A) = CLOSED
FINAL_REVIEWER_READY = false
```

## 9. Note carried to Batch 8B

Two manuscript loci reference **§11** as the home of E5 performance evidence (lines 670, 739). Under §49 of the original Batch 8 brief, E5 must appear in a results table only with a Pending/Deferred qualifier. The references are correctly bounded as written — they defer to E5 rather than asserting a result — but Batch 8B should confirm the section numbering when §11 is drafted.
