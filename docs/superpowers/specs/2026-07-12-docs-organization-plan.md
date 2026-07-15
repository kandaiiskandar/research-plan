# Docs Organization Plan
*Generated 2026-07-12*

---

## Current Problem

`docs/` has ~60 files dumped flat — justification docs, chapter drafts, evaluation designs, publication files, canonical reference docs, and miscellaneous all mixed together. Several files also live at root level when they belong in `docs/`. Some near-duplicate files exist.

---

## Proposed Folder Structure

```
docs/
├── canonical/              ← single sources of truth (CLAUDE.md canonical docs map)
├── justification/          ← all 20 justification-*.md files
├── chapters/               ← chapter drafts + per-chapter writing plans
├── evaluation/             ← RQ4 and RQ5 study/evaluation designs
├── publication/            ← conference and journal submission files
├── reference/              ← lookup/reference docs (discussion notes, novelty refs)
├── implementation/         ← data, prototype, and dataset docs
├── analysis/               ← synthesis, verification, viva prep docs
├── archive/                ← obsolete or superseded files (keep, don't delete)
├── images/                 ← existing (no change)
└── superpowers/            ← existing (no change)
```

Root level directories `improvement-plan/` and `review-comments/` are absorbed into `docs/`.

---

## File Mapping

### `docs/canonical/` — sources of truth

These are the files named in CLAUDE.md's Canonical Documents Map. Moving them requires updating path references in CLAUDE.md and any cross-document links.

| From | To |
|---|---|
| `docs/appendix-c-formalisation.md` | `docs/canonical/appendix-c-formalisation.md` |
| `docs/architecture-illustration.md` | `docs/canonical/architecture-illustration.md` |
| `docs/discussion-notes-governance-gap-precedents-and-formal-foundations.md` | `docs/canonical/discussion-notes-governance-gap-precedents-and-formal-foundations.md` |
| `docs/research-alignment-table.md` | `docs/canonical/research-alignment-table.md` |
| `docs/traceability-table.md` | `docs/canonical/traceability-table.md` |
| `docs/citation-notes-map.md` | `docs/canonical/citation-notes-map.md` |
| `docs/evaluation-design-rq4.md` | `docs/canonical/evaluation-design-rq4.md` |
| `docs/rq5-study-design.md` | `docs/canonical/rq5-study-design.md` |
| `docs/justification-layer3-enforcement.md` | `docs/canonical/justification-layer3-enforcement.md` |

> **Note:** After moving, update `CLAUDE.md` (Canonical Documents Map section) and any `../docs/` relative links inside these files.

---

### `docs/justification/` — design decision justifications

All `justification-*.md` files go here. The `justification-layer3-enforcement.md` is listed in the canonical map — it moves to `canonical/` instead (see above).

| From | To |
|---|---|
| `docs/justification-advisory-scope-restriction.md` | `docs/justification/advisory-scope-restriction.md` |
| `docs/justification-ai-necessity.md` | `docs/justification/ai-necessity.md` |
| `docs/justification-architectural-comparison.md` | `docs/justification/architectural-comparison.md` |
| `docs/justification-architecture-differentiation.md` | `docs/justification/architecture-differentiation.md` |
| `docs/justification-big-questions.md` | `docs/justification/big-questions.md` |
| `docs/justification-binary-governance-external-evidence.md` | `docs/justification/binary-governance-external-evidence.md` |
| `docs/justification-caution-mode-operation.md` | `docs/justification/caution-mode-operation.md` |
| `docs/justification-contribution-characterisation.md` | `docs/justification/contribution-characterisation.md` |
| `docs/justification-environmental-state-governance.md` | `docs/justification/environmental-state-governance.md` |
| `docs/justification-formal-model.md` | `docs/justification/formal-model.md` |
| `docs/justification-literature-review-methodology.md` | `docs/justification/literature-review-methodology.md` |
| `docs/justification-low-resource-environments.md` | `docs/justification/low-resource-environments.md` |
| `docs/justification-novelty-gap.md` | `docs/justification/novelty-gap.md` |
| `docs/justification-rainfall-intensity-mapping.md` | `docs/justification/rainfall-intensity-mapping.md` |
| `docs/justification-safety-state-design.md` | `docs/justification/safety-state-design.md` |
| `docs/justification-socio-technical-evaluation.md` | `docs/justification/socio-technical-evaluation.md` |
| `docs/justification-three-states.md` | `docs/justification/three-states.md` |
| `docs/justification-unified-governance.md` | `docs/justification/unified-governance.md` |
| `docs/justification-viva-formalisation-architecture.md` | `docs/justification/viva-formalisation-architecture.md` |

---

### `docs/chapters/` — chapter drafts and writing plans

| From | To |
|---|---|
| `docs/chapter-2-draft.md` | `docs/chapters/chapter-2-draft.md` |
| `docs/chapter-2-writing-plan.md` | `docs/chapters/chapter-2-writing-plan.md` |
| `docs/literature-review-writing-plan.md` | `docs/chapters/literature-review-writing-plan.md` |
| `docs/plan-chapter-1-introduction.md` | `docs/chapters/plan-chapter-1-introduction.md` |
| `docs/plan-layer3-model-type.md` | `docs/chapters/plan-layer3-model-type.md` |
| `docs/research-proposal-v3.md` | `docs/chapters/research-proposal-v3.md` |
| `docs/research-proposal-final.docx` | `docs/chapters/research-proposal-final.docx` |

---

### `docs/publication/` — conference and journal submissions

Pulls in root-level ipsci files too.

| From | To |
|---|---|
| `docs/ipsci2026-extended-abstract-draft.md` | `docs/publication/ipsci2026-extended-abstract-draft.md` |
| `docs/ipsci2026-introduction.md` | `docs/publication/ipsci2026-introduction.md` |
| `docs/publication-plan.md` | `docs/publication/publication-plan.md` |
| `ipsci-2026-extended-abstract-v2.md` *(root)* | `docs/publication/ipsci-2026-extended-abstract-v2.md` |
| `ipsci-2026-extended-abstract-v2-humanized.md` *(root)* | `docs/publication/ipsci-2026-extended-abstract-v2-humanized.md` |
| `ipsci-2026-extended-abstract-v3-slr.md` *(root)* | `docs/publication/ipsci-2026-extended-abstract-v3-slr.md` |
| `ipsci-2026-paper-v1.md` *(root)* | `docs/publication/ipsci-2026-paper-v1.md` |

---

### `docs/reference/` — lookup and reference docs

| From | To |
|---|---|
| `docs/caution-state-technical-novelty-ref.md` | `docs/reference/caution-state-technical-novelty-ref.md` |
| `docs/research-improvement-plan.md` | `docs/reference/research-improvement-plan.md` |
| `keyword-novelty-check-dua-patel-2024.md` *(root)* | `docs/reference/keyword-novelty-check-dua-patel-2024.md` |

---

### `docs/implementation/` — data, prototype, and dataset docs

| From | To |
|---|---|
| `docs/data-source-met-malaysia.md` | `docs/implementation/data-source-met-malaysia.md` |
| `docs/dataset-label-derivation.md` | `docs/implementation/dataset-label-derivation.md` |

---

### `docs/analysis/` — synthesis, verification, and viva prep

| From | To |
|---|---|
| `docs/synthesis-shamsujjoha-alignment.md` | `docs/analysis/synthesis-shamsujjoha-alignment.md` |
| `docs/verification-flehmig-shamsujjoha.md` | `docs/analysis/verification-flehmig-shamsujjoha.md` |
| `docs/viva-qa-novelty-problem-gap.md` | `docs/analysis/viva-qa-novelty-problem-gap.md` |
| `docs/ai-detection.md` | `docs/analysis/ai-detection.md` |

---

### Root level directories → `docs/`

| From | To |
|---|---|
| `improvement-plan/improvement-plan-1.md` | `docs/reference/improvement-plan-1.md` |
| `improvement-plan/literature_review_improvement_plan-2.md` | `docs/reference/literature-review-improvement-plan-2.md` |
| `review-comments/comments-1.md` | `docs/reference/review-comments-1.md` |
| `methodologies/extraction-prompt-methodological.md` | `docs/implementation/extraction-prompt-methodological.md` |
| `methodologies/extraction-prompt-search-methodology.md` | `docs/implementation/extraction-prompt-search-methodology.md` |

> After moving, the empty `improvement-plan/`, `review-comments/`, and `methodologies/` directories can be removed.

---

### Root level — stay as-is

| File | Reason |
|---|---|
| `CLAUDE.md` | Project config, must stay at root |
| `README.md` | Repo entry point |
| `index.md` | Jekyll site index |
| `_config.yml` | Jekyll config |
| `mohd-iskandar-samsuddin.pdf` | Personal CV — leave at root or move to a `personal/` folder |
| `part-i-student-report.md` | Consider moving to `docs/chapters/` if it's thesis content |
| `part-ii-research-goals.md` | Same as above |
| `instruction-plan.md` | Review — if still active, move to `docs/reference/`; if obsolete, `docs/archive/` |

---

### `docs/archive/` — obsolete or superseded files

Keep these but move out of the way. Do not delete until you confirm they are truly unused.

| File | Why archived |
|---|---|
| `docs/Architectural Layering Design and Graphic Representation.md` | Has spaces in filename; likely superseded by `architecture-illustration.md` |
| `docs/architectural-layering-design.md` | Likely superseded by `architecture-illustration.md` |
| `docs/architecture_graphic_final4.html` | HTML prototype; superseded by `docs/images/architecture/` |
| `docs/research-proposal-draft.md` | Superseded by v2/v3 |
| `docs/research-proposal-v2.md` | Superseded by v3 |
| `docs/research-proposal.docx` | Superseded by `research-proposal-final.docx` |
| `docs/writing-skill.md` | Meta-file, not thesis content |

---

## After Moving: What Needs Updating

### 1. `CLAUDE.md` — Canonical Documents Map

The table in `CLAUDE.md` lists file paths for the 9 canonical docs. Every moved file needs its path updated there.

### 2. Internal cross-references

Many docs link to each other with relative paths (e.g., `../notes/`, `docs/appendix-c-formalisation.md`). After moving, grep for broken relative links:

```bash
grep -rn '\.\./' docs/ | grep -v '\.DS_Store'
grep -rn 'docs/' CLAUDE.md
```

### 3. Citation notes links

The `citation-notes-map.md` uses `../notes/` paths. Moving it from `docs/` to `docs/canonical/` shifts the relative depth — links must be updated to `../../notes/`.

### 4. `notes/` files

Many notes files link back to docs with `../docs/` paths. Moving files inside `docs/` changes those relative paths too.

---

## Summary Count

| Action | Count |
|---|---|
| Files moved within `docs/` | ~45 |
| Root files moved into `docs/` | ~10 |
| Files archived (not deleted) | ~7 |
| Root directories removed after emptying | 2–3 |
| Files requiring path updates | CLAUDE.md + any file with `../docs/` or `../notes/` relative links |
