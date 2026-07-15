# PhD Organization System — Final Reference

**Version:** 1.0  
**Date:** 2026-07-12  
**Purpose:** Single source of truth for file structure, version control, publication tracking, and cross-linking

---

## 1. MASTER FOLDER STRUCTURE

```
project-root/
│
├── docs/                              ← ALL thesis documentation
│   ├── canonical/                     ← Single sources of truth (from CLAUDE.md)
│   │   ├── appendix-c-formalisation.md
│   │   ├── architecture-illustration.md
│   │   ├── discussion-notes-governance-gap-precedents-and-formal-foundations.md
│   │   ├── research-alignment-table.md
│   │   ├── traceability-table.md
│   │   ├── citation-notes-map.md
│   │   ├── evaluation-design-rq4.md
│   │   ├── rq5-study-design.md
│   │   ├── justification-layer3-enforcement.md
│   │   └── CHANGELOG.md               ← Track all canonical doc changes here
│   │
│   ├── chapters/                      ← Versioned chapter drafts
│   │   ├── chapter-1-introduction/
│   │   │   ├── v1-initial-draft.md
│   │   │   ├── v2-supervisor-feedback.md
│   │   │   ├── v3-added-related-work.md
│   │   │   └── archive/
│   │   │       ├── v1-initial-draft.md
│   │   │       └── v2-supervisor-feedback.md
│   │   ├── chapter-2-literature-review/
│   │   │   ├── v1-initial-draft.md
│   │   │   ├── v2-added-SLR-results.md
│   │   │   └── archive/
│   │   ├── chapter-3-methodology/
│   │   ├── chapter-4-results-rq4/
│   │   ├── chapter-5-results-rq5/
│   │   ├── chapter-6-discussion/
│   │   └── chapter-7-conclusion/
│   │
│   ├── writing-plans/                 ← Forward-looking plans (NOT drafts)
│   │   ├── plan-chapter-1-introduction.md
│   │   ├── plan-chapter-2-lit-review.md
│   │   ├── plan-chapter-3-methodology.md
│   │   ├── plan-chapter-4-rq4.md
│   │   ├── plan-chapter-5-rq5.md
│   │   └── plan-layer3-model-type.md
│   │
│   ├── justification/                 ← Design decision justifications
│   │   ├── advisory-scope-restriction.md
│   │   ├── ai-necessity.md
│   │   ├── architectural-comparison.md
│   │   ├── architecture-differentiation.md
│   │   ├── big-questions.md
│   │   ├── binary-governance-external-evidence.md
│   │   ├── caution-mode-operation.md
│   │   ├── contribution-characterisation.md
│   │   ├── environmental-state-governance.md
│   │   ├── formal-model.md
│   │   ├── literature-review-methodology.md
│   │   ├── low-resource-environments.md
│   │   ├── novelty-gap.md
│   │   ├── rainfall-intensity-mapping.md
│   │   ├── safety-state-design.md
│   │   ├── socio-technical-evaluation.md
│   │   ├── three-states.md
│   │   ├── unified-governance.md
│   │   └── viva-formalisation-architecture.md
│   │
│   ├── evaluation/                    ← RQ4 and RQ5 study designs
│   │   ├── rq4-study-design.md
│   │   └── rq5-study-design.md
│   │
│   ├── analysis/                      ← Synthesis, verification, viva prep
│   │   ├── synthesis-shamsujjoha-alignment.md
│   │   ├── verification-flehmig-shamsujjoha.md
│   │   ├── viva-qa-novelty-problem-gap.md
│   │   └── ai-detection.md
│   │
│   ├── reference/                     ← Lookup/reference docs
│   │   ├── research-improvement-plan.md
│   │   ├── improvement-plan-1.md
│   │   ├── literature-review-improvement-plan-2.md
│   │   ├── review-comments-1.md
│   │   ├── caution-state-technical-novelty-ref.md
│   │   └── keyword-novelty-check-dua-patel-2024.md
│   │
│   ├── implementation/                ← Data, prototype, dataset docs
│   │   ├── data-source-met-malaysia.md
│   │   ├── dataset-label-derivation.md
│   │   ├── extraction-prompt-methodological.md
│   │   └── extraction-prompt-search-methodology.md
│   │
│   ├── admin/                         ← Administrative docs
│   │   ├── part-i-student-report.md
│   │   ├── part-ii-research-goals.md
│   │   └── instruction-plan.md
│   │
│   ├── obsolete/                      ← Superseded files (keep, don't delete)
│   │   ├── research-proposal-draft.md
│   │   ├── research-proposal-v2.md
│   │   ├── architectural-layering-design.md
│   │   ├── architecture_graphic_final4.html
│   │   └── writing-skill.md
│   │
│   ├── images/                        ← Existing (no change)
│   ├── superpowers/                   ← Existing (no change)
│   └── MASTER_LOG.md                  ← Your current sprint tracker (see Section 6)
│
├── publications/                      ← ALL publication outputs
│   ├── active/                        ← Current submissions in progress
│   │   └── ipsci-2026/                ← One folder per venue
│   │       ├── submissions/
│   │       │   ├── v1-initial-submission/
│   │       │   │   ├── manuscript.md
│   │       │   │   ├── abstract.md
│   │       │   │   └── figures/
│   │       │   ├── v2-post-review/
│   │       │   │   ├── manuscript.md
│   │       │   │   ├── response-to-reviewers.md
│   │       │   │   └── figures/
│   │       │   ├── v3-camera-ready/
│   │       │   │   ├── manuscript.md
│   │       │   │   └── figures/
│   │       │   └── archive/           ← Superseded versions
│   │       ├── reviews/
│   │       │   ├── reviewer-1-comments.md
│   │       │   ├── reviewer-2-comments.md
│   │       │   └── meta-review.md
│   │       ├── correspondence/
│   │       │   ├── submission-email.md
│   │       │   ├── acceptance-email.md
│   │       │   └── camera-ready-email.md
│   │       └── README.md              ← Publication tracking log
│   │
│   ├── rejected/                      ← Rejected submissions
│   │   └── [venue-name]/
│   │       ├── submissions/
│   │       ├── reviews/
│   │       └── rejection-notice.md
│   │
│   ├── published/                     ← Final accepted versions
│   │   └── [venue-name]/
│   │       ├── final-manuscript.md
│   │       ├── published-pdf.pdf
│   │       └── doi.txt
│   │
│   └── templates/                     ← Reusable templates
│       ├── conference-template.md
│       ├── journal-template.md
│       ├── response-to-reviewers-template.md
│       └── abstract-template.md
│
├── notes/                             ← Your paper journal / literature notes
│   ├── summaries/                     ← One file per paper (4-bullet summary)
│   │   ├── smith-2022-neural-networks.md
│   │   ├── dua-patel-2024-governance.md
│   │   └── [Author_Year_Topic].md
│   ├── themes/                        ← Thematic collections
│   │   ├── theme-1-theory.md
│   │   ├── theme-2-methodology.md
│   │   ├── theme-3-case-studies.md
│   │   └── theme-4-counter-arguments.md
│   └── reading-list.md                ← Papers to read / tracking
│
├── root-level-files/                  ← Keep these at root
│   ├── CLAUDE.md                      ← Project config (update paths)
│   ├── README.md                      ← Repo entry point
│   ├── index.md                       ← Jekyll site index
│   ├── _config.yml                    ← Jekyll config
│   ├── mohd-iskandar-samsuddin.pdf    ← CV
│   ├── PUBLICATION-THESIS-SYNC.md     ← Cross-linking tracker (see Section 7)
│   └── PhD-ORGANIZATION-SYSTEM.md     ← This file (you're reading it)
│
└── methodologies/                     ← (Deprecated — moved to docs/implementation/)
    └── (empty, remove after migration)
```

---

## 2. VERSION CONTROL RULES

### The Golden Rule
**NEVER edit the document you just opened.**

### Chapter Draft Workflow
1. Open `chapter-X/v2-filename.md`
2. Click **"Save As"** → rename to `chapter-X/v3-what-changed.md`
3. **Now** start editing
4. Move old versions to `chapter-X/archive/` when they pile up (keep last 3 active versions)

### Publication Submission Workflow
1. Copy entire `v1-initial-submission/` folder to `v2-post-review/`
2. Make changes in the new folder
3. Never edit the submitted version directly

### Justification Files (Lightweight Versioning)
Add a changelog section at the top of each justification file:

```markdown
# Justification: [Topic Name]

## Changelog
| Date | Version | Change |
|------|---------|--------|
| 2026-07-12 | v3 | Added counter-argument from Patel (2024) — updated section 4.2 |
| 2026-06-28 | v2 | Restructured to align with new architecture diagram |
| 2026-06-10 | v1 | Initial draft |

## Current Content
[Your justification text here...]
```

### Canonical Documents
Use `docs/canonical/CHANGELOG.md` for high-level tracking:

```markdown
# Canonical Documents Changelog

## 2026-07-12
- **architecture-illustration.md** — v4: Updated Layer 2 diagram to reflect new governance state transitions (supervisor request)
- **traceability-table.md** — v3: Added mapping for RQ4 evaluation metrics

## 2026-07-05
- **appendix-c-formalisation.md** — v2: Corrected notation in Definition 3.2 (typo fix)
```

---

## 3. PAPER JOURNAL (LITERATURE NOTES)

### Storage: Thematic PDF Organization
Save PDFs by **theme**, not by author:

```
notes/
├── pdfs/
│   ├── theme-1-theory/
│   ├── theme-2-methodology/
│   ├── theme-3-case-studies/
│   └── theme-4-counter-arguments/
```

### Synthesis: The 4-Bullet Summary
For EVERY paper you read, create `notes/summaries/[Author_Year_Topic].md` with exactly this structure:

```markdown
# [Author, Year] — [Title]

**Citation:** [Full citation]

**The Big Claim:** [Main argument in one sentence]

**The Method:** [How did they prove it?]

**The Key Quote:** "[Quote]" (p. XX)

**My Connection:** [Does this support Chapter X, contradict Chapter Y, or fill a gap?]

**Tags:** #theory #methodology #case-study #[topic]
```

### How to Use This
- When writing a chapter, **search your summaries**, not your PDFs
- Use tags to quickly find relevant papers
- Update `my-connection` field as your argument evolves

---

## 4. PUBLICATION TRACKING LOG

### Per-Venue README.md Template

Copy this into `publications/active/[venue-name]/README.md`:

```markdown
# [Venue Name] Submission Tracking

## Venue Details
- **Conference/Journal:** [Name]
- **Track/Special Issue:** [If applicable]
- **Type:** [Full paper / Short paper / Extended abstract]
- **Status:** [Submitted / Under review / Accepted / Rejected]

## Deadlines
| Milestone | Date | Status |
|-----------|------|--------|
| Submission | YYYY-MM-DD | ✅ / ⏳ / ❌ |
| Reviews due | YYYY-MM-DD | ✅ / ⏳ / ❌ |
| Camera-ready | YYYY-MM-DD | ✅ / ⏳ / ❌ |
| Conference | YYYY-MM-DD | ✅ / ⏳ / ❌ |

## Version History
| Version | Date | Status | Notes |
|---------|------|--------|-------|
| v1 | YYYY-MM-DD | Submitted | Initial submission |
| v2 | YYYY-MM-DD | In progress | Addressing reviewer comments |
| v3 | YYYY-MM-DD | Camera-ready | Final formatting |

## Reviewer Feedback Summary
| Reviewer | Decision | Major Issue | Our Response Status |
|----------|----------|-------------|---------------------|
| R1 | [Accept / Reject] | [Summary] | ✅ / ⏳ / ❌ |
| R2 | [Accept / Reject] | [Summary] | ✅ / ⏳ / ❌ |
| R3 | [Accept / Reject] | [Summary] | ✅ / ⏳ / ❌ |

## Traceability to Thesis Chapters
| Publication Section | Thesis Chapter | Notes |
|---------------------|----------------|-------|
| Introduction | Chapter 1 | Expanded in thesis |
| Methodology | Chapter 3 | Same content, more detail |
| Results | Chapter 4 | Direct mapping |
| Discussion | Chapter 5 | Expanded in thesis |

## Next Actions
- [ ] Action 1
- [ ] Action 2
- [ ] Action 3
```

---

## 5. RESPONSE TO REVIEWERS TEMPLATE

Copy this into `publications/active/[venue]/submissions/v2-post-review/response-to-reviewers.md`:

```markdown
# Response to Reviewers — [Venue Name]

**Manuscript ID:** [ID]  
**Authors:** [Your name + co-authors]  
**Date:** YYYY-MM-DD

---

## Reviewer 1

**Summary:** [Briefly restate their overall assessment]

### Comment 1: [Copy or paraphrase the reviewer's comment]

> *"Original reviewer text..."*

**Response:** Thank you for this observation. We have [explain what you did].

**Change in manuscript:** [Describe where/how you changed the text, e.g., "We have revised Section 3.2 (p. 5) to..."]

---

### Comment 2: [Copy or paraphrase]

> *"Original reviewer text..."*

**Response:** [...]

**Change in manuscript:** [...]

---

## Reviewer 2

[Repeat structure...]

---

## Summary of Major Changes

| Location | Original | Revised | Reason |
|----------|----------|---------|--------|
| Section 2.1 | [Original text summary] | [New text summary] | Addressed R1 Comment 2 |
| Figure 3 | [Original] | [New] | Addressed R2 Comment 1 |

---

## Additional Notes

[Any other information for the editor/reviewers]
```

---

## 6. MASTER LOG (Your Daily / Weekly Tracker)

Save this as `docs/MASTER_LOG.md`:

```markdown
# PhD Writing Master Log

**Last Updated:** YYYY-MM-DD

---

## Current Sprint (YYYY-MM-DD to YYYY-MM-DD)
**Goal:** [One sentence describing this week's focus]  
**Blockers:** [Anything stopping you?]

---

## File Status

| Chapter | Current Version | Status | Next Action |
|---------|----------------|--------|-------------|
| Ch 1 | v3 | With supervisor | Awaiting feedback |
| Ch 2 | v2 | In progress | Add SLR results → v3 |
| Ch 3 | v1 | Drafted | Send to supervisor |
| Ch 4 | v0.1 | Rough notes | No action yet |
| Ch 5 | - | Not started | - |
| Ch 6 | - | Not started | - |
| Ch 7 | - | Not started | - |

---

## Publication Status

| Venue | Version | Status | Next Action |
|-------|---------|--------|-------------|
| IPSci 2026 | v2 | Addressing reviews | Submit by YYYY-MM-DD |
| [Journal] | - | Planned | Outline by YYYY-MM-DD |

---

## Daily Log

### YYYY-MM-DD
- **Done:** [What you accomplished]
- **Issues:** [Problems encountered]
- **Tomorrow:** [What you plan to do]

### YYYY-MM-DD
- **Done:** [...]
- **Issues:** [...]
- **Tomorrow:** [...]
```

---

## 7. PUBLICATION ↔ THESIS SYNC TRACKER

Save this as `PUBLICATION-THESIS-SYNC.md` at your project root:

```markdown
# Publication ↔ Thesis Sync Tracker

**Purpose:** Ensure insights from publications are incorporated into thesis, and vice versa.

**Last Updated:** YYYY-MM-DD

---

## From Publications → Thesis

### [Venue Name] — [Status: Accepted / Rejected / Under Review]

| Publication Change | Thesis Impact | Status |
|-------------------|---------------|--------|
| Added new citation (Author, Year) | Update Chapter 2 Literature Review | ✅ / ⏳ / ❌ |
| Rewrote methodology based on reviewer feedback | Update Chapter 3 Methodology | ✅ / ⏳ / ❌ |
| Added new Figure X (concept diagram) | Add to Chapter 3 or Appendix | ✅ / ⏳ / ❌ |
| Reviewer comment about novelty gap | Strengthen Chapter 2 gap analysis | ✅ / ⏳ / ❌ |

### [Next Venue] — [Status]

| Publication Change | Thesis Impact | Status |
|-------------------|---------------|--------|
| [...] | [...] | [...] |

---

## From Thesis → Publications

| Thesis Section | Target Publication | Status |
|----------------|-------------------|--------|
| Chapter 3 (Formal Model) | Journal paper on governance formalisation | Outline done |
| Chapter 4 (RQ4 results) | Conference paper | Not started |
| Chapter 5 (RQ5 results) | Conference paper | Not started |
| Appendix C (Formalisation) | Supplementary material for journal | Needs expansion |

---

## Priority Actions

| Priority | Action | Due Date | Status |
|----------|--------|----------|--------|
| High | Update Ch 2 with Dua & Patel (2024) | YYYY-MM-DD | ⏳ |
| Medium | Add RQ4 methodology justification | YYYY-MM-DD | ⏳ |
| Low | Outline journal paper structure | YYYY-MM-DD | ⏳ |
```

---

## 8. FILE MIGRATION CHECKLIST

Use this to move your existing files into the new structure:

### Move into `docs/canonical/`
- [ ] `docs/appendix-c-formalisation.md` → `docs/canonical/`
- [ ] `docs/architecture-illustration.md` → `docs/canonical/`
- [ ] `docs/discussion-notes-governance-gap-precedents-and-formal-foundations.md` → `docs/canonical/`
- [ ] `docs/research-alignment-table.md` → `docs/canonical/`
- [ ] `docs/traceability-table.md` → `docs/canonical/`
- [ ] `docs/citation-notes-map.md` → `docs/canonical/`
- [ ] `docs/evaluation-design-rq4.md` → `docs/canonical/`
- [ ] `docs/rq5-study-design.md` → `docs/canonical/`
- [ ] `docs/justification-layer3-enforcement.md` → `docs/canonical/`

### Move into `docs/justification/`
- [ ] All `justification-*.md` files from `docs/` → `docs/justification/` (remove the `justification-` prefix)

### Move into `docs/chapters/`
- [ ] `docs/chapter-2-draft.md` → `docs/chapters/chapter-2-literature-review/v1-initial-draft.md`
- [ ] `docs/chapter-2-writing-plan.md` → `docs/writing-plans/plan-chapter-2-lit-review.md`
- [ ] `docs/literature-review-writing-plan.md` → `docs/writing-plans/plan-chapter-2-lit-review.md`
- [ ] `docs/plan-chapter-1-introduction.md` → `docs/writing-plans/`
- [ ] `docs/plan-layer3-model-type.md` → `docs/writing-plans/`
- [ ] `docs/research-proposal-v3.md` → `docs/chapters/archive/`
- [ ] `docs/research-proposal-final.docx` → `docs/chapters/archive/`

### Move into `docs/publication/` (or new `publications/` folder)
- [ ] `docs/ipsci2026-extended-abstract-draft.md` → `publications/active/ipsci-2026/submissions/v1-initial-submission/manuscript.md`
- [ ] `docs/ipsci2026-introduction.md` → `publications/active/ipsci-2026/submissions/archive/`
- [ ] `docs/publication-plan.md` → `publications/active/ipsci-2026/README.md`
- [ ] Root-level IPSci files → `publications/active/ipsci-2026/submissions/archive/`

### Move into `docs/reference/`
- [ ] `docs/caution-state-technical-novelty-ref.md` → `docs/reference/`
- [ ] `docs/research-improvement-plan.md` → `docs/reference/`
- [ ] Root-level `keyword-novelty-check-dua-patel-2024.md` → `docs/reference/`
- [ ] `improvement-plan/` contents → `docs/reference/`
- [ ] `review-comments/` contents → `docs/reference/`

### Move into `docs/implementation/`
- [ ] `docs/data-source-met-malaysia.md` → `docs/implementation/`
- [ ] `docs/dataset-label-derivation.md` → `docs/implementation/`
- [ ] `methodologies/` contents → `docs/implementation/`

### Move into `docs/analysis/`
- [ ] `docs/synthesis-shamsujjoha-alignment.md` → `docs/analysis/`
- [ ] `docs/verification-flehmig-shamsujjoha.md` → `docs/analysis/`
- [ ] `docs/viva-qa-novelty-problem-gap.md` → `docs/analysis/`
- [ ] `docs/ai-detection.md` → `docs/analysis/`

### Move into `docs/admin/`
- [ ] Root-level `part-i-student-report.md` → `docs/admin/`
- [ ] Root-level `part-ii-research-goals.md` → `docs/admin/`
- [ ] Root-level `instruction-plan.md` → `docs/admin/` (if still active)

### Move into `docs/obsolete/`
- [ ] `docs/Architectural Layering Design and Graphic Representation.md`
- [ ] `docs/architectural-layering-design.md`
- [ ] `docs/architecture_graphic_final4.html`
- [ ] `docs/research-proposal-draft.md`
- [ ] `docs/research-proposal-v2.md`
- [ ] `docs/research-proposal.docx`
- [ ] `docs/writing-skill.md`

### Remove empty directories
- [ ] `improvement-plan/`
- [ ] `review-comments/`
- [ ] `methodologies/`

---

## 9. UPDATE CLAUDE.md

After moving files, update the **Canonical Documents Map** section in `CLAUDE.md` to reflect new paths:

```markdown
## Canonical Documents Map

| Document | Location |
|----------|----------|
| Appendix C (Formalisation) | `docs/canonical/appendix-c-formalisation.md` |
| Architecture Illustration | `docs/canonical/architecture-illustration.md` |
| Discussion Notes (Governance Gap) | `docs/canonical/discussion-notes-governance-gap-precedents-and-formal-foundations.md` |
| Research Alignment Table | `docs/canonical/research-alignment-table.md` |
| Traceability Table | `docs/canonical/traceability-table.md` |
| Citation Notes Map | `docs/canonical/citation-notes-map.md` |
| Evaluation Design (RQ4) | `docs/canonical/evaluation-design-rq4.md` |
| Study Design (RQ5) | `docs/canonical/rq5-study-design.md` |
| Justification (Layer 3 Enforcement) | `docs/canonical/justification-layer3-enforcement.md` |
```

---

## 10. QUICK REFERENCE CHEAT SHEET

| What | Where |
|------|-------|
| Current thesis chapters | `docs/chapters/chapter-X/` |
| Chapter writing plans | `docs/writing-plans/` |
| Justification docs | `docs/justification/` |
| Literature notes (summaries) | `notes/summaries/` |
| Literature notes (PDFs) | `notes/pdfs/theme-X/` |
| Active publication | `publications/active/[venue]/` |
| Accepted publication | `publications/published/[venue]/` |
| Rejected publication | `publications/rejected/[venue]/` |
| Templates | `publications/templates/` |
| Daily/weekly tracking | `docs/MASTER_LOG.md` |
| Publication ↔ thesis sync | `PUBLICATION-THESIS-SYNC.md` |

---

## 11. DAILY WRITING WORKFLOW

**Every time you write:**

1. Open `docs/MASTER_LOG.md` — know what you're working on
2. Navigate to the appropriate chapter folder
3. **Save As** to create a new version
4. Write/edit in the new file
5. Update `MASTER_LOG.md` with what you did

**Every time you get feedback:**

1. Save feedback in the appropriate folder
2. Create a new version of the document
3. Log the changes in `CHANGELOG.md` or the file's changelog section
4. If relevant, update `PUBLICATION-THESIS-SYNC.md`

**Every time you submit a publication:**

1. Copy entire submission folder to next version
2. Update `README.md` with new status
3. Update `MASTER_LOG.md`
4. After acceptance/rejection, move folder to `published/` or `rejected/`

---

## 12. ONE FINAL RULE

**Delete NOTHING. Archive everything.**

If a file is superseded:
- Move it to `docs/obsolete/` or `publications/[venue]/submissions/archive/`
- Keep it for reference
- You never know when you need to recover a deleted paragraph or trace your argument's evolution

---

**End of System Document**

---

> **Pro Tip:** Bookmark this file (`PhD-ORGANIZATION-SYSTEM.md`) in your editor or keep it open in a separate tab. Refer to it every time you're unsure where to save a new file or how to version something.