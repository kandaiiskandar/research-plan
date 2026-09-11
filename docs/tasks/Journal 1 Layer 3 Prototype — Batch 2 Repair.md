# Journal 1 Layer 3 Prototype — Batch 2 Repair

## Evidence-Semantics and Artefact-Integrity Repair

**Opened:** 2026-09-11  
**Closed:** 2026-09-11  
**Branch:** design/journal1-algorithm-specification  
**Predecessor:** Batch 2 closure — `JOURNAL 1 LAYER 3 PROTOTYPE BATCH 2 CLOSED WITH BOUNDED OPEN ITEMS — ADVISORY RULE EVIDENCE AND SEMANTICS PARTIALLY SPECIFIED`

---

## Findings

Three issues were identified in the Batch 2 artefacts after closure:

### Repair 1 — Cross-reference error in semantic-verification-batch2.json

**Finding:** `semantic-verification-batch2.json`, check `human_authority_unconditional`, evidence string referenced "layer3-prototype-specification.md §29" — a section that does not exist. The specification runs from §1 (Batch 1) through §27 (Batch 2 Traceability). §29 was the task file's own section numbering for the human authority boundary, not a specification section.

**Correct reference:** §17 (Recommendation Semantics), which explicitly states: "Go does not mean permission"; "Delay does not mean prohibition"; "Human authority over the departure decision is unconditional."

**Action taken:** Updated the evidence string to reference §17 with the specific content located there.

**File modified:** `data/journal1-layer3-prototype/semantic-verification-batch2.json`

---

### Repair 2 — Missing `scientific_rationale` column in rule-candidate-register-batch2.csv

**Finding:** Task §16 (Rule provenance requirement) specifies that every concrete rule must include a `scientific_rationale` field. The CSV was built following the §30 column list, which omits `scientific_rationale` as a named column. The rationale content was embedded across `classifier_duplication` and `limitation` fields, but §16's named field was absent.

**Resolution:** `scientific_rationale` was added as a separate column between `adaptation_required` and `conflict_risk`. Content was derived from the rationale text already present in `rule-evidence-matrix-batch2.csv` and the candidate descriptions in `report-batch2.md`.

**Key scientific rationale entries:**
- R-SAFE-001: three independent empirical studies converge on fisher Go behavior under SAFE-equivalent conditions; independent of architectural permission
- R-CAUTION-001: MET Malaysia Category 1 directly names small boats as at-risk population; minimal inferential steps
- R-CAUTION-002: Jeong & Im (2023) and Yaakob et al. (2015) reach convergent thresholds from independent methodologies (incident analysis vs. naval architecture)
- R-CAUTION-003: Rahim et al. (2024) East season is the direct behavioral analog for rainfall-driven restriction; source-verified as rainfall-primary
- R-CAUTION-004: Gao (2024) and Atacan & Düzbastılar (2023) are methodologically independent studies (behavioral ethnography vs. simulator) from independent locations
- R-REJ-001 through R-REJ-005: explicit rejection rationale added

**File modified:** `data/journal1-layer3-prototype/rule-candidate-register-batch2.csv`

---

### Repair 3 — Humanizer pass on written documents

**Finding:** Memory rule `feedback_use_humanizer.md` requires the humanizer skill to be invoked before finalising any written document. `report-batch2.md` and the new specification sections §§16–27 were written with humanizer guidelines applied inline but without a formal skill invocation.

**Humanizer audit findings (AI detection baseline ~25–35%):**
- Bureaucratic "should be stated explicitly / clearly" constructions → replaced with direct phrasing
- Passive "was identified / was assessed / was established" → made active where the actor is recoverable
- Copula avoidance "This is the most directly evidenced rule in the candidate set" → named the subject
- False agency "The absence reflects a genuine gap" → rewritten as a direct statement
- "This is assessed as MODERATE" → "The risk is MODERATE"
- Passive "Seven conflict scenarios were assessed" → "The conflict analysis covered seven scenarios"
- One instance of "should be stated clearly" in Limitations section → removed

**Files modified:**
- `data/journal1-layer3-prototype/report-batch2.md`
- `publications/active/journal-1/layer3-prototype-specification.md` (§§16, 18, 19)

**Technical content unchanged:** formal notation, table structure, CSV references, section numbers, evidence source citations, status verdicts.

---

## Closure

All three repairs applied. The closure line for Batch 2 is unchanged:

```
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 2 CLOSED WITH BOUNDED OPEN ITEMS —
ADVISORY RULE EVIDENCE AND SEMANTICS PARTIALLY SPECIFIED
```

Semantic verification: 27 PASS / 0 FAIL / 0 OPEN (unchanged — all checks still pass after repair).

Protected canonical state: PASS — 16 unchanged, 0 changed (verified by build.py before repair; no canonical files modified by repair).

---

## Files changed by repair

| File | Change |
|---|---|
| `data/journal1-layer3-prototype/semantic-verification-batch2.json` | §29 → §17 in human_authority_unconditional evidence |
| `data/journal1-layer3-prototype/rule-candidate-register-batch2.csv` | Added `scientific_rationale` column (16 columns total) |
| `data/journal1-layer3-prototype/report-batch2.md` | Humanizer pass — 9 targeted prose edits |
| `publications/active/journal-1/layer3-prototype-specification.md` | Humanizer pass — 3 targeted prose edits in §§16, 18, 19 |
| `docs/tasks/Journal 1 Layer 3 Prototype — Batch 2 Repair.md` | This file — repair task documentation |
