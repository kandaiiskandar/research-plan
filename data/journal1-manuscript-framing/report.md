# Journal 1 — Batch 8B-2: Framing, Interpretation, Abstract, References and Whole-Manuscript Audit

**Date:** 2026-09-13 · **Branch:** `docs/journal1-manuscript-evidence-sync` · **HEAD:** `c3ab3eb`
**Manuscript:** `a91ede5ff8518e46` → **`7b571aac8d6f9b7a`** (1,246 → 1,661 lines; ~28,900 words)
**Verification:** 68 PASS · 0 FAIL · 0 OPEN

---

## 1. Objective and scope as executed

Batch 8B-2 completed the manuscript: the sections that frame and interpret the evidence 8B-1 established, the Abstract, the reference list, and the whole-manuscript audits that could only run once the text was complete.

**Authored:** Abstract, Keywords, §1 Introduction, §2 Related Work, §3 AI Governance Foundations, §4 Problem Formulation, §13 Discussion, §14 Threats to Validity, §15 Conclusion, References.

**Not performed:** no experiment, no replay, no script execution, no scientific code change, no web search, no new literature search, no closure of E5.

**Sections 5–12 preserved.** Verified byte-identical to the committed baseline modulo citation-key renumbering — the one edit inside them that reference compilation requires.

---

## 2. The four standing decisions

**Decision 1 — References.** Compiled from repository sources only: **33 entries**, of which **28 were transcribed programmatically from the conference manuscript's verified list** and **5 from corpus extraction notes**. No web search; no DOI, volume, issue or page value reconstructed. Three entries carry partial metadata and are flagged `REFERENCE_METADATA_INCOMPLETE` in the reference list itself, with the missing fields itemised in `citation-audit.md`.

The conference numbering could not be carried over — only 28 of its 40 entries are cited here, so retaining the keys would have left gaps. In-text keys were remapped in a single pass to order of first appearance; the full mapping is in `reference-compilation.json`. Every key resolves, no entry is uncited, and numbering is consecutive — all three verified programmatically.

**Decision 2 — Section 3 standards.** The §3 stub called for IEC 61508, ISO 26262, ICAO SAL and SOLAS. **The repository has no extraction notes for any of them**, so the comparison was omitted rather than asserted from general knowledge, and §2.6 carries an explicit `[CITATION SUPPORT REQUIRED]` marker naming what is missing and why. Two repository-supported observations were retained in its place. §13.8 declines the same comparison for the same reason and states that no compliance or certification claim is made.

**Decision 3 — R-SAFE-001.** Discharged in §14.5, which states that `RS(SAFE)` is empty, that all 32 SAFE episodes generated zero advisories, that `Delay` is the only generated conclusion type, and that F1/F2 therefore do not demonstrate fidelity of a populated SAFE rule set. It also appears in §15. The required check `SAFE_rule_set_not_overclaimed` **PASSES** and fails under negative control.

**Decision 4 — Structure.** Manuscript structure treated as authority throughout. No section renamed, none created.

---

## 3. Obligations carried in from earlier batches

| Obligation | Source | Where discharged |
|---|---|---|
| SAFE-rule limitation in Threats to Validity | 8B-1 Decision 3 | §14.5 |
| Ablation-scope limits (worst-case aggregation, component ablation not performed) | 8B-1 §12.5 forward reference | §14.6 |
| **Binding disclosure: 2 → 1,536 direct SAFE→UNSAFE transitions stated plainly, not absorbed into surrounding text** | Canonical **C-4** | §14.4, in its own set-off block |
| E4 PRIMARY-only, no resolution-insensitivity claim | E3/E4 micro-repair | §14.6 |
| E5 OPEN, no target-hardware claim, H3 unsupported | Throughout | §1.5, §14.7, §15, Abstract |

The C-4 obligation was found during authoring rather than supplied by the brief: the canonical approval record requires that figure to appear in Threats to Validity stated plainly. It now does.

---

## 4. Authoring notes

**The novelty boundary is stated three times and narrowed each time.** §1.2 says graduated governance is not new and names what the precedents graduate; §2.5 states the gap in one sentence and corroborates it from two independent findings; §13.3 bounds the structural-comparator result by its disclosed modelling premise. The claim throughout is *graduated advisory scope conditioned on classified environmental state*, never graduated governance as such.

**§13 separates RESULT from INTERPRETATION explicitly**, subsection by subsection, so the interpretive claims can be rejected without disturbing the evidence. §13.9 lists what the work does not demonstrate before a reader has to infer it.

**§14 runs to nine subsections** and bounds results the paper depends on — including that the central fidelity result does not cover a populated SAFE rule set, that the marine-warning component was never measured, that the nighttime policy is an architectural choice with a 1,536-transition cost, and that target-hardware performance is unmeasured.

**The Abstract was written last**, after §§1–15 cohered. It carries `5.81%`, `4.48%`, `0.00%`, `292` and `454`, all traceable to closed evidence, and it states that target-hardware characterisation **remains pending**. No MacBook figure, no Android mention, no latency value.

---

## 5. Defect found and deliberately not repaired

**Section 7 contains seven dangling references to theorems that are declared nowhere in the manuscript** — `Theorem 5.2` (×2) and `Theorem 5.3` (×5). The results exist as **Theorem 6.2** and **Theorem 6.3** in §6. Section 5 separately declares a `Theorem 5.1` that duplicates §6's `Theorem 6.1`, so one result carries two numbers.

This is pre-existing, predates all three 8B batches, and **a reviewer would find it immediately.** It was not repaired because §§5–8 are modifiable only where drafting exposes a direct scientific contradiction — this is a numbering defect, not a wrong claim — and because the fix requires choosing between two restructurings with different consequences for §§5–6. That choice is not this batch's to make.

All sections authored by 8B-2 use the §6 numbering exclusively, verified by check. Full detail in `cross-section-audit.md` §4. **This is the recommended next task.**

---

## 6. Audits

- **Cross-section consistency** — 26 symbols and status values traced across every section that uses them. **No contradiction found.** One apparent §8/§13.6 tension on resource claims examined and confirmed consistent as written.
- **Overclaim audit, whole manuscript** — 18 prohibited phrases scanned; 15 occurrences found, **0 unnegated**. Every one sits inside a sentence that forbids the reading.
- **Citation audit** — 33 entries, provenance recorded per entry; 1 `[CITATION SUPPORT REQUIRED]` gap and 3 incomplete-metadata entries, none hidden.
- **Stub audit** — **0 drafting stubs remain.** All twelve Batch 8A `UNDRAFTED` markers discharged. Four remaining markers are classified: one justified citation gap, three justified metadata gaps, plus a figures production note and an author-affiliation placeholder that are not scientific content.
- **E5 boundary** — re-run over the complete text, including the newly authored sections and the Abstract. E5 OPEN in all eight mentions; one Android occurrence, inside a prohibition; H3 never numeric.

---

## 7. Verification — 68 PASS, 0 FAIL, 0 OPEN

**Fourteen negative controls were injected and all fourteen were caught** — overclaimed SAFE coverage, an E5 result in the Abstract, a numeric H3 threshold, an uncited reference entry, a reversed novelty claim, an asserted human-validation result, a falsely claimed ablation, a softened C-4 disclosure, a fabricated standards-compliance claim, text inserted into a protected section, an accident-reduction claim, a real-time claim, an invented RESOLUTION E4, and an unresolvable citation key.

**The first control run exposed two real defects in my own detector, not in the manuscript.**

1. The sentence splitter used a lookbehind on `[.!?]` followed by whitespace, which does not fire on `.**` — so a bolded prohibition and the sentence after it merged into one segment. Markdown emphasis is now stripped before splitting.
2. The negation test accepted a negation *anywhere* in the sentence. An injected claim was therefore masked by an unrelated negation later in the same long sentence, and `no_human_validation_claim` passed a mutation it should have caught. The test now requires the negation to precede the term.

Tightening rule 2 then flagged a genuine ambiguity in my own §14.9 prose, where the prohibition trailed the terms it prohibited. **The manuscript sentence was rewritten to lead with the negation** rather than the check loosened — clearer prose and a stricter test. This is the fourth batch in which a verification check turned out to be testing the wrong property; the pattern is consistent enough to be worth stating plainly.

**Integrity.** One existing file changed: the manuscript. The evaluation specification, canonical architecture, all scripts, governance code, every evidence artefact, and all 8B-1 and status-repair artefacts are hash-identical to their preflight values. The conference manuscript was read only.

---

## 8. Status

```
Abstract, Keywords, Sections 1–15, References = AUTHORED
P1–P4 = CLOSED · F1–F3 = CLOSED · E1–E4 = CLOSED · E6 = CLOSED
E5 = OPEN · E5_HARNESS = CLOSED · MACBOOK_REFERENCE = COMPLETE
E5_ANDROID_TARGET_BENCHMARK = DEFERRED_MANDATORY
H3 = OPEN/UNSUPPORTED · R_SAFE_001 = DEFERRED
E3_SCOPE = {E1, E2, E6} · E4_RESOLUTION = NOT_REQUIRED_BY_CURRENT_E3_DESIGN
MANUSCRIPT_STATUS = DRAFT_COMPLETE_WITH_OPEN_E5_DEPENDENCY
OPEN: theorem-numbering defect in §7; standards citation gap in §2.6;
      3 incomplete reference entries; 6 figures unproduced
FINAL_REVIEWER_READY = false
```

**Closure:**

```
JOURNAL 1 MANUSCRIPT BATCH 8B-2 CLOSED —
FRAMING, INTERPRETATION, ABSTRACT AND REFERENCES AUTHORED; WHOLE-MANUSCRIPT
AUDIT COMPLETED WITH E5 TARGET-HARDWARE DEPENDENCY PRESERVED
```
