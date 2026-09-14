# Journal 1 — E3/E4 Resolution-Sensitivity Authority Consistency Micro-Repair

**Date:** 2026-09-13 · **Branch:** `docs/journal1-manuscript-evidence-sync` · **HEAD at start:** `fcbbe8d297a5`
**Type:** bounded scientific-authority consistency repair — no experiment, no recomputation, no manuscript edit

---

## 1. Trigger

Journal 1 Manuscript Batch 8A halted before its first manuscript edit on a contradiction between two CLOSED claims: E3 placed E4 inside a mandatory dual-configuration reporting scope, while E4's authoritative evidence is PRIMARY-only. E3's own prohibition forbade E4's own permitted reporting.

## 2. Resolution

E3's scope was narrowed; E4 was left untouched. Full reasoning in `scope-rationale.md`.

The scientific principle adopted: *resolution sensitivity applies only to empirical quantities for which the evaluation design supports a like-for-like PRIMARY/RESOLUTION comparison.* E1, E2 and E6 are share-of-hours divergence **rates**, normalised by their own denominators — comparable across configurations. E4's transitions, oscillations and hysteresis reduction are **event counts over a window**, and PRIMARY spans 5.00 years against RESOLUTION's 3.25. Comparing them would confound resolution with window length.

## 3. Files changed — two, both live authority

| File | Loci | Change |
|---|---|---|
| `publications/active/journal-1/evaluation-specification.md` | §13 global contract; line 168 M-Empirical-E3; M-Empirical-E4; §18 pointer | Scope bounded to {E1, E2, E6}; E4 excluded with `NOT_REQUIRED` semantics stated; E4 row marked PRIMARY-only; §18 no longer designates a stale artefact as master authority |
| `data/journal1-post-fidelity-plan/claim-status-matrix.csv` | Row E3 only — `definition`, `required_evidence`, `existing_evidence`, `next_action`, `manuscript_claim_prohibited` | Rewritten to bounded scope; `status` remains CLOSED |

**E4 row verified content-identical** field by field, as were all eleven other non-E3 rows.

## 4. Additional locus found beyond the brief

The brief named §13 and the E3 metric row. A full-file search found a **fourth live route** to the old contract: **§18** designated the frozen `evaluation-specification.csv` as "the single-source-of-truth master table", and that CSV's E3 row still carries the pre-repair wording. Repairing §13 alone would have left a back door — a reader following §18 would have found the superseded contract presented as authoritative. §18 now records the CSV as frozen batch evidence with a stale `current_status` column, and names the Markdown authoritative where they differ.

## 5. Provenance check — `evaluation-specification.csv` is **Interpretation B (historical)**

Resolved on repository evidence, against the filename and the Markdown's own claim:

| Evidence | Direction |
|---|---|
| `current_status` for F1–F3 reads `OPEN — requires Layer 3 build`; Batch 5 closed all three PASS | **B** — stale by two batches |
| `build.py` contains **zero** references to the CSV; it only writes `integrity-after.json` and `parser-test.json` | **B** — not generated, hand-authored |
| Listed in that batch's `closure.json` artefact inventory beside `integrity-before/after.json` | **B** — frozen batch evidence |
| Batch 6 cited it as *corroboration* and recorded its F1–F3 statuses as superseded rather than updating it | **B** |
| `evaluation-specification.md` §18 called it "single-source-of-truth master table" | A — but itself stale drift, and repaired |

**Action:** the CSV was **not modified**. Its old E3 wording is recorded as superseded.

## 6. Historical provenance preserved

Three Batch 6 narrative artefacts retain the original "E1, E2, E4, E6" assertion, deliberately — erasing them would destroy the provenance of the contradiction. All six historical loci are enumerated in `historical-supersession-record.csv` with `current_status = SUPERSEDED` and `superseded_by = E3/E4 resolution-sensitivity authority micro-repair`.

## 7. What this repair does **not** claim

Not that E4 is resolution-insensitive. Not that E4 would reproduce under MFWAM. Not that a RESOLUTION E4 result exists or equals the PRIMARY one. Not that a required experiment was omitted. `NOT_REQUIRED` is a statement about the comparison contract, not about the world — and all four prohibitions are written into §13 itself, not only into this report.

## 8. Verification

**32 checks, 32 PASS, 0 FAIL, 0 OPEN** (`verification.json`). Manuscript, canonical architecture, governance code, all evaluation scripts, Batch 5 evidence and Batch 7A evidence byte-identical. `hysteresis_analysis.py` not run and not modified — confirmed still to contain no MFWAM path. CSV parser-tested with `csv.DictReader` and `pandas.read_csv`: PASS.

## 9. Status

```
E3 = CLOSED
E4 = CLOSED
E3_SCOPE = {E1, E2, E6}
E4_RESOLUTION = NOT_REQUIRED_BY_CURRENT_E3_DESIGN
BATCH_8A_BLOCKER = RESOLVED
```
