# Journal 1 — Theorem and Definition Numbering Consistency Micro-Repair

**Date:** 2026-09-14 · **Branch:** `docs/journal1-manuscript-evidence-sync` · **HEAD:** `dca5aed`
**Manuscript:** `7b571aac8d6f9b7a` → **`9fbf75fe050a4d91`** (8 lines changed, +8 / −8)
**Verification:** 56 PASS · 0 FAIL · 0 OPEN · **18/18 negative controls discriminating**

---

## 1. Objective

Repair the formal-object numbering defect identified after Batch 8B-2, preserving all scientific meaning. Documentation-level repair only: no scientific claim, equation, proof, value, citation or status was changed.

---

## 2. Independent verification of the defect

The task brief required the Batch 8B-2 report to be re-verified rather than trusted. A full census of every Definition, Property, Theorem, Lemma, Proposition and Corollary was built before any edit — **21 declarations and 72 references**. All six premises held:

| Premise | Verified |
|---|---|
| §5 declares `Theorem 5.1 (Totality of f)` | ✔ L457 |
| §6 contains the canonical proofs | ✔ §6.2 → 6.1, §6.3 → 6.2, §6.4 → 6.3 |
| §7 references `Theorem 5.2` / `Theorem 5.3` | ✔ 7 references across 4 lines |
| Neither is declared anywhere | ✔ |
| The results exist in §6 | ✔ Monotonicity 6.2, Safety Dominance 6.3 |
| One result carries duplicate numbering | ✔ Totality |

**The census also found two things the brief did not list**, both material:

1. **An eighth reference.** §7 L792 cited `Theorem 5.1` — resolving *before* the repair, but orphaned *by* the demotion. Had the repair been confined to the seven known dangling references, it would have created a new dangling reference while fixing the old ones.
2. **`Corollary 6.3` collides with `Theorem 6.3`** — reported during the pre-execution analysis and resolved by decision.

---

## 3. Repairs applied — 9 changes across 8 lines

**NUMBERING_REPAIR (2):** `Theorem 5.1` demoted to an unnumbered statement; `Corollary 6.3` → `Corollary 6.2b`.
**CROSS_REFERENCE_REPAIR (6):** `Theorem 5.1` → `6.1` (×1), `5.2` → `6.2` (×2), `5.3` → `6.3` (×5).
**MINIMAL_GRAMMAR_REPAIR (1):** "Proof deferred to Section 6.2." → "This result is proved canonically as Theorem 6.1 in Section 6.2."

No global string replacement was used. Each reference was read in context and matched against the target theorem's declared title before editing. Full classification: `diff-audit.md`.

---

## 4. Result

| | Before | After |
|---|---|---|
| Declarations | 21 | 20 |
| References | 72 | 73 |
| **Dangling references** | **7** | **0** |
| Duplicate identifiers | 0 | 0 |
| Same result, two theorem identities | 1 (Totality) | **0** |

Final formal structure, as specified:

```
§5  specification-level Definitions 5.1–5.11 and Properties 5.1–5.3
    Totality statement — unnumbered, forward-referencing Theorem 6.1
§6  Theorem 6.1  = Totality            (§6.2)
    Theorem 6.2  = Monotonicity        (§6.3)
    Corollary 6.2  — Strict Monotonicity        (§6.3, from Theorem 6.2)
    Corollary 6.2b — Properties 5.1 and 5.2     (§6.3, from Theorem 6.2)
    Theorem 6.3  = Safety Dominance    (§6.4)
§7  and all downstream references resolve only to these identities
```

**`Property 5.3 (Safety Dominance Property)` was preserved deliberately.** It is not a duplicate theorem identity but the third instance of a pattern the manuscript applies uniformly — §5 states a property, §6 discharges it. Properties 5.1 and 5.2 are discharged by Corollary 6.2b, whose title names them explicitly. Evidence: `duplicate-result-audit.md` §2.

---

## 5. Verification — 56 PASS, 0 FAIL, 0 OPEN

The brief required more than string disappearance: each repaired reference had to be shown to point at the **correct semantic theorem**. Semantic checks therefore read the target theorem's declared title from the manuscript and require it to match the concept named in the referring sentence — so a reference repaired to the wrong theorem fails even though the old string is gone.

**All 18 negative controls discriminate**, including five that mis-point a reference while removing the old string — exactly the failure a string-only verifier cannot see.

**Four defects were found in the verifier itself, none in the manuscript.** Each was caught by control and fixed in the tool:

1. **Titles came back empty.** The verifier re-derived theorem titles with a second parser whose preview-exclusion searched the *whole document* for a bullet form; because §6.1 previews Theorems 6.1–6.3, it skipped their real declarations too. Replaced by reading the census, which already excludes previews correctly — removing the duplicated parsing logic rather than fixing it twice.
2. **Semantic checks accepted one correct occurrence.** L811 and L849 each cite their theorem twice; mis-pointing one went undetected. Now *every* theorem citation on the line must equal the expected identifier.
3. **The verifier crashed instead of failing.** Direct dictionary indexing raised `KeyError` when a control removed a key; the verifier aborted, `verification.json` kept the previous run's results, and the control read a stale PASS. Key access is now defensive, and the control harness checks the verifier's exit status and restores the manuscript under `try/finally` — an earlier run had aborted on a bad anchor and left the file mutated on disk.
4. **Hard-coded line numbers.** Inserting a line shifted every number below it, so four controls crashed the verifier rather than failing it. All lookups are now anchored on content.

A fifth issue was a **false positive in the verifier, not a defect in the manuscript**: the wrong-target scan matched across adjacent rows of the Table 7 evaluation matrix, pairing "Theorem 6.1" in the P1 row with "Monotonicity" in the P2 row. The gap pattern now excludes newlines and table pipes. Table 7 was inspected directly and is correct.

This is the fifth consecutive batch in which a verification check was testing the wrong property. The pattern is stable enough to be worth stating: **a check that passes on first run has not been shown to work.**

---

## 6. Integrity

One file changed: the manuscript, 8 lines. Byte-level confirmation that nothing else moved — normalising the committed pre-repair text by exactly the authorised substitutions reproduces the post-repair text exactly.

Unchanged and individually verified: all Definitions and Properties; proofs and equations; all 15 quantitative values; citation keys and the reference list; Abstract, Keywords, §§1–4, §2, §8 and §§9–15 by byte comparison; the evaluation specification, algorithm specification, Layer 3 specification and Appendix C by hash; and all 31 artefacts from the three preceding batches.

---

## 7. Out-of-scope findings

| ID | Finding | Risk |
|---|---|---|
| **OOS-1** | `Definition 5.11` declared before `Definition 5.10` | None — no gap, every reference resolves. Left per decision 4. |
| **OOS-2** | `section-5-plan.md` L273 instructs *"Use Section 5 numbering (Theorem 5.1, 5.2, 5.3) in the journal paper"* | **Low but real** — a stale *instruction*, now contradicted by the manuscript. The file carries a superseded banner and is a non-maintained artefact, but a future batch reading it as guidance could reintroduce the defect. |
| **OOS-3** | `session-log.md` records the old numbering at three lines | None — a historical record; correcting it would falsify what was planned at the time. |

---

## 8. Status

```
THEOREM_NUMBERING_DEFECT = CLOSED
MANUSCRIPT_STATUS = DRAFT_COMPLETE_WITH_OPEN_E5_DEPENDENCY
P1–P4 = CLOSED · F1–F3 = CLOSED · E1–E4 = CLOSED · E6 = CLOSED
E5 = OPEN · E5_HARNESS = CLOSED · MACBOOK_REFERENCE = DEVELOPMENT_MACHINE_REFERENCE
E5_ANDROID_TARGET_BENCHMARK = DEFERRED_MANDATORY
H3 = OPEN/UNSUPPORTED · R_SAFE_001 = DEFERRED
FINAL_REVIEWER_READY = false
```

**Closure:**

```
JOURNAL 1 THEOREM AND DEFINITION NUMBERING CONSISTENCY MICRO-REPAIR CLOSED —
CANONICAL SECTION 6 THEOREM IDENTITIES RESTORED AND ALL FORMAL CROSS-REFERENCES
RESOLVED WITHOUT SCIENTIFIC CHANGE
```
