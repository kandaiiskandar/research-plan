# File Organization Migration Plan
*Date: 2026-07-12 — Review before executing*

---

## Final Folder Structure

```
project-root/
│
├── docs/
│   ├── canonical/           ← 9 single sources of truth (CLAUDE.md map)
│   ├── justification/       ← 19 justification-*.md files (prefix stripped)
│   ├── chapters/
│   │   └── chapter-2-literature-review/
│   │       └── v1-chapter-2-draft.md
│   ├── writing-plans/       ← forward-looking chapter plans
│   ├── student-reports/     ← semester-based student reports
│   │   ├── semester-1/
│   │   │   ├── part-i-student-report.md
│   │   │   ├── part-ii-research-goals.md
│   │   │   └── research-proposal/
│   │   │       ├── research-proposal-draft.md
│   │   │       ├── research-proposal-v2.md
│   │   │       ├── research-proposal-v3.md
│   │   │       ├── research-proposal-final.docx
│   │   │       └── research-proposal.docx
│   │   └── semester-2/      ← ready for future use (empty)
│   ├── reference/           ← improvement plans, review comments, novelty refs
│   ├── implementation/      ← data, dataset, extraction prompt docs
│   ├── analysis/            ← synthesis, verification, viva prep
│   ├── obsolete/            ← superseded files (keep, don't delete)
│   ├── images/              ← NO CHANGE
│   └── superpowers/         ← NO CHANGE
│
├── publications/            ← NEW top-level folder for all publication outputs
│   └── active/
│       └── ipsci-2026/
│           ├── submissions/
│           │   └── archive/
│           └── README.md
│
└── notes/                   ← NO CHANGE (97 files, link-repair risk too high)
```

---

## Migration Checklist

### `docs/canonical/`

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

> Note: No separate `docs/evaluation/` folder — evaluation design files stay in `canonical/` per CLAUDE.md.

---

### `docs/justification/`

The `justification-` prefix is stripped from filenames.

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

### `docs/chapters/`

Only create the folder that has actual content now.

| From | To |
|---|---|
| `docs/chapter-2-draft.md` | `docs/chapters/chapter-2-literature-review/v1-chapter-2-draft.md` |

> Other chapter folders (`chapter-1`, `chapter-3`, etc.) are created only when actual drafts exist.

---

### `docs/writing-plans/`

| From | To |
|---|---|
| `docs/chapter-2-writing-plan.md` | `docs/writing-plans/chapter-2-writing-plan.md` |
| `docs/literature-review-writing-plan.md` | `docs/writing-plans/literature-review-writing-plan.md` |
| `docs/plan-chapter-1-introduction.md` | `docs/writing-plans/plan-chapter-1-introduction.md` |
| `docs/plan-layer3-model-type.md` | `docs/writing-plans/plan-layer3-model-type.md` |

---

### `docs/student-reports/`

| From | To |
|---|---|
| `part-i-student-report.md` *(root)* | `docs/student-reports/semester-1/part-i-student-report.md` |
| `part-ii-research-goals.md` *(root)* | `docs/student-reports/semester-1/part-ii-research-goals.md` |
| `docs/research-proposal-draft.md` | `docs/student-reports/semester-1/research-proposal/research-proposal-draft.md` |
| `docs/research-proposal-v2.md` | `docs/student-reports/semester-1/research-proposal/research-proposal-v2.md` |
| `docs/research-proposal-v3.md` | `docs/student-reports/semester-1/research-proposal/research-proposal-v3.md` |
| `docs/research-proposal-final.docx` | `docs/student-reports/semester-1/research-proposal/research-proposal-final.docx` |
| `docs/research-proposal.docx` | `docs/student-reports/semester-1/research-proposal/research-proposal.docx` |

---

### `docs/reference/`

| From | To |
|---|---|
| `docs/caution-state-technical-novelty-ref.md` | `docs/reference/caution-state-technical-novelty-ref.md` |
| `docs/research-improvement-plan.md` | `docs/reference/research-improvement-plan.md` |
| `keyword-novelty-check-dua-patel-2024.md` *(root)* | `docs/reference/keyword-novelty-check-dua-patel-2024.md` |
| `instruction-plan.md` *(root)* | `docs/reference/instruction-plan.md` |
| `improvement-plan/improvement-plan-1.md` | `docs/reference/improvement-plan-1.md` |
| `improvement-plan/literature_review_improvement_plan-2.md` | `docs/reference/literature-review-improvement-plan-2.md` |
| `review-comments/comments-1.md` | `docs/reference/review-comments-1.md` |

---

### `docs/implementation/`

| From | To |
|---|---|
| `docs/data-source-met-malaysia.md` | `docs/implementation/data-source-met-malaysia.md` |
| `docs/dataset-label-derivation.md` | `docs/implementation/dataset-label-derivation.md` |
| `methodologies/extraction-prompt-methodological.md` | `docs/implementation/extraction-prompt-methodological.md` |
| `methodologies/extraction-prompt-search-methodology.md` | `docs/implementation/extraction-prompt-search-methodology.md` |

---

### `docs/analysis/`

| From | To |
|---|---|
| `docs/synthesis-shamsujjoha-alignment.md` | `docs/analysis/synthesis-shamsujjoha-alignment.md` |
| `docs/verification-flehmig-shamsujjoha.md` | `docs/analysis/verification-flehmig-shamsujjoha.md` |
| `docs/viva-qa-novelty-problem-gap.md` | `docs/analysis/viva-qa-novelty-problem-gap.md` |
| `docs/ai-detection.md` | `docs/analysis/ai-detection.md` |

---

### `publications/active/ipsci-2026/`

| From | To |
|---|---|
| `docs/ipsci2026-extended-abstract-draft.md` | `publications/active/ipsci-2026/submissions/ipsci2026-extended-abstract-draft.md` |
| `docs/ipsci2026-introduction.md` | `publications/active/ipsci-2026/submissions/archive/ipsci2026-introduction.md` |
| `docs/publication-plan.md` | `publications/active/ipsci-2026/README.md` |
| `ipsci-2026-extended-abstract-v2.md` *(root)* | `publications/active/ipsci-2026/submissions/archive/ipsci-2026-extended-abstract-v2.md` |
| `ipsci-2026-extended-abstract-v2-humanized.md` *(root)* | `publications/active/ipsci-2026/submissions/archive/ipsci-2026-extended-abstract-v2-humanized.md` |
| `ipsci-2026-extended-abstract-v3-slr.md` *(root)* | `publications/active/ipsci-2026/submissions/archive/ipsci-2026-extended-abstract-v3-slr.md` |
| `ipsci-2026-paper-v1.md` *(root)* | `publications/active/ipsci-2026/submissions/archive/ipsci-2026-paper-v1.md` |

---

### `docs/obsolete/`

Superseded or unclear files — keep, do not delete.

| File | Reason |
|---|---|
| `docs/Architectural Layering Design and Graphic Representation.md` | Filename has spaces; superseded by `architecture-illustration.md` |
| `docs/architectural-layering-design.md` | Likely superseded by `architecture-illustration.md` |
| `docs/architecture_graphic_final4.html` | HTML prototype, superseded by `images/architecture/` |
| `docs/writing-skill.md` | Meta-file, not thesis content |

---

### Root — stay as-is

| File | Reason |
|---|---|
| `CLAUDE.md` | Must stay at root — project config |
| `README.md` | Repo entry point |
| `index.md` | Jekyll site index |
| `_config.yml` | Jekyll config |
| `mohd-iskandar-samsuddin.pdf` | CV — leave at root |

---

### Empty directories to remove after migration

- `improvement-plan/`
- `review-comments/`
- `methodologies/`

---

## After Migration: Required Updates

### 1. Update `CLAUDE.md` — Canonical Documents Map

All 9 canonical file paths change from `docs/filename.md` to `docs/canonical/filename.md`.

Also update the `justification-*.md` paths in the Formal Model Consistency Rule section — they move to `docs/justification/`.

### 2. Check internal cross-references

Run these after migration to find broken links:

```bash
# Find relative links pointing to old docs/ paths
grep -rn '\.\./docs/' notes/
grep -rn 'docs/justification-' docs/

# Find citation-notes-map links (depth changes from docs/ to docs/canonical/)
grep -n '\.\./notes/' docs/canonical/citation-notes-map.md
```

`citation-notes-map.md` moves from `docs/` to `docs/canonical/` — its `../notes/` links must become `../../notes/`.

### 3. Notes/ stays unchanged

No files in `notes/` are moved. All existing `[[notes]](../notes/...)` links in docs remain valid relative to their new locations only if the depth doesn't change. Files moving from `docs/` to `docs/canonical/` or `docs/justification/` gain one extra level — their `../notes/` links must become `../../notes/`.

