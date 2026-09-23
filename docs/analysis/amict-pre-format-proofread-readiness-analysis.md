# AMICT V4 Pre-Format Mechanical Proofreading — Task Readiness Analysis

**Date:** 2026-09-14
**Analyses:** `docs/tasks/AMICT V4 — FINAL PRE-FORMAT MECHANICAL PROOFREADING.md`
**Status:** PRE-EXECUTION ANALYSIS ONLY. No edit made, no addendum written.
**Companions:** [manuscript V4](amict-manuscript-v4-readiness-analysis.md) · [post-draft audit](amict-post-draft-audit-readiness-analysis.md)

---

## 1. What the task is

A Level-0 mechanical pass before templating. Not a scientific review — the argument is frozen. It names one known defect and asks for a full read to catch other surgical-edit artefacts.

I ran the mechanical scans the execution would run. **The named defect is real. It is the only one.**

---

## 2. The known defect is confirmed, and it is mine

Section V.C currently reads:

> …while the intermediate-state control is unchanged at zero. **The two configurations differ in both wave model and record length. The configurations differ in both wave model and record length;** this evaluation does not isolate which difference accounts for the observed spread of approximately 1.3 percentage points.

**Cause.** During the post-draft audit's PC5 correction I replaced the causal clause *"The direction of movement is consistent with a finer model resolving nearshore sheltering…"* with a sentence that restated the sentence immediately preceding it. I matched on the text to remove and did not read the line above it. That is the exact artefact class this task exists to catch.

A near-duplicate scan across the whole manuscript ranks it at **91% word overlap between adjacent sentences — the highest in the document.** The next-highest legitimate pair sits at 83%.

### 2.1 A residual the prescribed fix does not clear

The task's §2 replacement removes the duplicated sentence but leaves **"approximately 1.3 percentage points" appearing twice in consecutive sentences** — once in the RQ3 answer, once in the retained clause:

> …moving from 5.81% to 4.48% — a spread of approximately 1.3 percentage points — while the intermediate-state control is unchanged at zero. The configurations differ in both wave model and record length; this evaluation does not isolate which difference accounts for the observed spread of approximately 1.3 percentage points.

Trimming the second occurrence to *"…which difference accounts for the observed spread"* loses nothing and reads better. Whether that is a Level-0 repetition fix or a stylistic rewrite is a genuine judgement call under §12, which says to report rather than edit when uncertain.

**Recommendation:** apply the §2 fix exactly as written, and raise the doubled figure as `REVIEW_REQUIRED` rather than deciding unilaterally. It is the only item in the manuscript where §12's boundary is ambiguous.

---

## 3. Everything else is clean

Scans run across the full manuscript, prose and tables, excluding the build comment.

| Check | Result |
|---|---|
| Exact duplicate sentences (>5 words) | **0** |
| Near-duplicate adjacent sentences | 5 flagged; **4 legitimate** (anaphoric link, adjacent frozen canonical strings, table lead-in plus caption, parallel primary/resolution construction); 1 is the §2 defect |
| Doubled words | **0** |
| Double period, double comma, space before punctuation, double space, orphan brackets | **0** each |
| Bold markers | 108 — paired |
| Italic markers | even |
| Structure | 9 sections, 12 subsections |
| Table blocks | 3, column counts consistent (6/4/4), 3 captions |
| Malformed citations `[ n ]` | **0** |
| Citation ranges | `[1]–[5]`, `[9]–[14]` — both well-formed |
| Period-before-citation | 1 hit, **false positive** — "Flehmig et al. [4]", the period belongs to the abbreviation |

### 3.1 Numerical integrity — all present, none stale

43,848 (×3) · 9,135 · 42.88% (×2) · 48.69% (×2) · 5.81% (×8) · 4.48% (×5) · 0.00% (×5) · 292 primary episodes · 32 permissive · 260 intermediate · 244 with advisory · 16 without · 454 advisory records · 162 gate-off cases · wind two-number rule intact.

**41.08 and 45.56 absent.** The provenance-open exclusion holds.

### 3.2 Table integrity

**TABLE I** citations are [4], [5], [6], [7], [9], [10], [11], [12], [13] — all inside 1–19, **no stale pre-renumbering number survived**. **TABLE II** keeps exclusion distinct from fault, with the three fault rows resolving to ⊥ and the unmeasured row declared in *D*, evaluated before faults, pinned SAFE, marked "Not a fault". **TABLE III** carries 5.81/4.48, 0.00/0.00, and "not reported" in both resolution pairwise cells.

### 3.3 Canonical text lock

Gap statement ×1 exact. Novelty sentence ×3 exact. RQ1, RQ2, RQ3 all exact. **No frozen string requires mechanical correction**, so §5's stop condition does not arise.

### 3.4 References, disclosures, double-blind

19 references, contiguous 1–19, **0 orphans, 0 dangling**. AC 20-151C present, AC 20-151A absent. Cleaveland correct, Cleveland absent. Protected disclosures **19/19**. Prohibited-claim scan clean across all fifteen expressions. Double-blind body scan clean — the single "Acknowledg" match is inside the build comment, stating that no acknowledgements appear.

---

## 4. Edit-boundary review (§13)

The task asks for particular attention at the boundaries touched by earlier surgical passes. Each was checked:

| Pass | Boundary | Finding |
|---|---|---|
| Post-draft audit PC1/PC1b | Abstract opening | Clean; sentence flow intact after two rewrites |
| PC2 | Introduction, TCAS sentence | Clean after clause removal |
| PC4 | Section III, proofs sentence | Clean |
| **PC5** | **Section V.C** | **Duplication — the §2 defect** |
| PC6 | Section IV, site wording | Clean |
| PC8/PC8b | Introduction opening | Clean; antecedent repair holds |
| Corpus reframe | Section II opening | Clean |
| Micro-repair | Section II opening and synthesis clause | Clean |
| Reference renumbering | Whole document, tables included | Clean; no stale number anywhere |

Nine boundaries, one defect. The renumbering pass in particular — the most mechanically risky of the edits — came through with no residue.

---

## 5. Stop-condition pre-assessment

| Condition | Assessment |
|---|---|
| Contradiction in scientific interpretation | **Does not fire** |
| Unsupported claim needing substantive repair | **Does not fire** |
| Canonical frozen text requiring modification | **Does not fire** — all five frozen strings verify exact |
| Empirical number mismatch | **Does not fire** — every §6 value present and correct |
| Comparator inconsistency | **Does not fire** — TABLE I and prose agree |
| Reference problem needing a new source | **Does not fire** |
| Protected disclosure unpreservable | **Does not fire** — 19/19 |
| Evidence/provenance contradiction | **Does not fire** — 41.08/45.56 remain excluded |

`SCIENTIFIC_REOPEN_REQUIRED = NO` on present evidence.

---

## 6. Expected outcome

One edit: the §2 duplication. Body count **3,674 → approximately 3,663**. Results stays the largest section by a wide margin.

    PRE_FORMAT_MECHANICAL_PROOFREAD = CLOSED
    KNOWN_RQ3_DUPLICATION           = FIXED
    MECHANICAL_DEFECTS_REMAINING    = 0
    SCIENTIFIC_REOPEN_REQUIRED      = NO
    REVIEW_REQUIRED                 = 1   (doubled "1.3 percentage points", §2.1)

Addendum C appended to `post-draft-audit.md`, leaving the original audit and Addenda A and B intact — a fourth layer on the same record.

---

## 7. Verdict

**Executable, single edit, no stop condition.** The task's premise is correct in every particular: the defect exists, it was produced by surgical editing, and a full mechanical sweep finds nothing else in a manuscript that has now been cut, reframed, renumbered and repaired across four separate passes.

The one thing worth deciding rather than assuming is §2.1 — whether removing the second "approximately 1.3 percentage points" is mechanical or stylistic. My reading is that it is repetition rather than style, but §12 is explicit that ambiguity goes to the report, not to the file.

---

## 8. Files inspected

Read-only. Nothing modified.

- `docs/tasks/AMICT V4 — FINAL PRE-FORMAT MECHANICAL PROOFREADING.md`
- `publications/active/ipsci-2026/submissions/v4-amict-rebuild/manuscript.md` — full mechanical sweep
- `publications/active/ipsci-2026/submissions/v4-amict-rebuild/post-draft-audit.md` — Addenda A and B for edit-boundary provenance
