# Research Commands Design Spec

**Date**: 2026-04-01
**Status**: Approved
**Scope**: 5 new Claude Code slash commands for the research paper extraction system

---

## Overview

Extend the existing `/extract-paper` workflow with 5 new commands that integrate available skills into a cohesive research pipeline. All commands are independent (Approach A) — each is a standalone `.claude/commands/*.md` file with no shared prompt fragments.

### Commands

| Command | Skill used | Purpose |
|---|---|---|
| `/batch-extract` | `dispatching-parallel-agents` | Extract multiple PDFs in parallel |
| `/quick-summary` | `claude-paper:summary` | Fast preview before full extraction |
| `/study-paper` | `claude-paper:study` | Deep interactive study with materials linked to notes |
| `/review-notes` | `simplify` (concept) | Review a single notes file for quality |
| `/plan-review` | `writing-plans` (concept) | Gap analysis + literature review outline |

---

## Command 1: `/batch-extract`

**File**: `.claude/commands/batch-extract.md`

**Usage**:
- `/batch-extract` — extracts all unprocessed PDFs in `papers/sources/`
- `/batch-extract paper1.pdf paper2.pdf` — extracts only specified files

**Workflow**:
1. List all PDFs in `papers/sources/`
2. List all notes in `notes/` to determine which papers are already extracted
3. If arguments given, use those files (even if already extracted — allows re-extraction); otherwise, use unprocessed files only
4. If no unprocessed files found, report "all papers already extracted" and stop
5. For each PDF, dispatch a parallel `general-purpose` agent with `model: opus` that performs the full extract-paper workflow:
   - Parse PDF with claude-paper's `parse-pdf.js`, fallback to pymupdf
   - Read extraction prompt from `.claude/prompts/paper_extraction_prompt.md`
   - Perform full 17-section extraction
   - Extract images with `extract-images.py`
   - Save notes to `notes/<slugified-title>.md` with YAML frontmatter and Figures table
   - Append row to `papers/paper_tracker.md`
6. After all agents complete, report results: which papers were extracted, relevance scores, any failures

**Key decisions**:
- Each agent gets the full extraction instructions inlined since sub-agents cannot invoke slash commands
- Agent model is set to `opus` for highest extraction quality
- Tracker updates may have concurrent write issues — each agent reads tracker before appending; acceptable risk given the append-only nature

---

## Command 2: `/quick-summary`

**File**: `.claude/commands/quick-summary.md`

**Usage**: `/quick-summary <filename.pdf>`

**Workflow**:
1. Verify the PDF exists in `papers/sources/`
2. Parse the PDF using claude-paper's `parse-pdf.js` (fallback to pymupdf)
3. Invoke `claude-paper:summary` skill to generate a concise summary (core ideas, key findings, methodology)
4. Extract basic metadata from the parsed content: title, authors, year, venue
5. Read `papers/paper_tracker.md`
6. Check if the paper is already in the tracker:
   - **Already fully extracted** (has a notes link): Skip tracker update, just show the summary
   - **Already previewed**: Skip tracker update, just show the summary
   - **Not in tracker**: Append a new row with Type = `previewed`, Relevance = `—`, Notes = `—`
7. Report the summary to the user

**Tracker row format for previewed papers**:

| Title | Authors | Year | Venue | Type | Relevance | Notes |
|-------|---------|------|-------|------|-----------|-------|
| Paper Title | Author et al. | 2024 | Venue | previewed | — | — |

**Key decisions**:
- No notes file is created — this is preview only
- When `/extract-paper` is later run on the same paper, it overwrites the "previewed" row (matches by title) with full data
- Relevance is `—` because the full 17-section analysis has not been performed

---

## Command 3: `/study-paper`

**File**: `.claude/commands/study-paper.md`

**Usage**: `/study-paper <filename.pdf>`

**Workflow**:
1. Verify the PDF exists in `papers/sources/`
2. Invoke `claude-paper:study` skill with the full path — generates study materials in `~/claude-papers/papers/<paper-slug>/`:
   - README.md, summary.md, insights.md, qa.md
   - method.md, mental-model.md, reflection.md (conditional)
   - Code demos in `code/` directory
   - Interactive HTML explorer at `index.html`
   - Extracted images in `images/`
   - Index entry in `~/claude-papers/index.json`
3. After study materials are generated, determine the paper slug used by claude-paper
4. Check if a notes file exists in `notes/` for this paper:
   - **If notes exist**: Add `study_materials: "~/claude-papers/papers/<paper-slug>/"` to the YAML frontmatter
   - **If no notes yet**: Do not create notes
5. Check `papers/paper_tracker.md`:
   - **If the paper has a row**: Append the study materials path as a second link in the Notes column: `[notes](...) · [study](~/claude-papers/papers/<paper-slug>/)`
   - **If no row yet**: Add a row with Type = `studied`, Relevance = `—`, Notes = `[study](~/claude-papers/papers/<paper-slug>/)`
6. Continue with claude-paper's interactive deep learning loop — ask user what to explore further

**Key decisions**:
- Study materials live in `~/claude-papers/` (claude-paper's default location), not copied into the project
- The link in the tracker and notes frontmatter connects the two systems
- Does not trigger `/extract-paper` automatically — user decides separately

---

## Command 4: `/review-notes`

**File**: `.claude/commands/review-notes.md`

**Usage**: `/review-notes <title>.md` (filename from `notes/`)

**Workflow**:
1. Verify the notes file exists in `notes/<argument>`
2. Read the notes file
3. Read the extraction prompt from `.claude/prompts/paper_extraction_prompt.md`
4. Review the notes against these criteria:
   - **Completeness**: All 17 sections present and substantively addressed
   - **Depth**: Answers are specific to the paper, not generic (e.g., "No" vs "No — the paper does not address X because...")
   - **Accuracy**: Frontmatter metadata (title, authors, year, venue, type) appears correct and consistent with content
   - **Research alignment**: Section 3 (Relevance) maps convincingly to all 8 research themes; Section 16 (Positioning) clearly articulates the gap
   - **Citable content**: Section 15 quotes are specific with page/section locations
   - **Consistency**: Relevance score in Section 17 matches the actual analysis across sections
5. Produce a review report:
   - Quality rating: Strong / Adequate / Needs Improvement
   - Specific issues found, grouped by section number
   - Suggested improvements with concrete rewrites where applicable
6. Ask: "Want me to apply these improvements to the notes file?"
   - If yes: Edit the notes file directly
   - If no: Leave the file unchanged

**Key decisions**:
- Does NOT re-read the source PDF — reviews notes as-is against the extraction prompt's requirements
- If the source PDF needs re-analysis, user should re-run `/extract-paper`
- Single file only (no batch mode) — keeps review focused and interactive

---

## Command 5: `/plan-review`

**File**: `.claude/commands/plan-review.md`

**Usage**: `/plan-review` (no arguments)

**Workflow**:
1. Read all notes files in `notes/` that have full 17-section extractions (skip any without)
2. Read the extraction prompt to get the 8 research themes:
   1. Hybrid AI (deterministic rule-based + probabilistic AI reasoning)
   2. Safety-critical AI decision systems
   3. AI governance — controlling *when* AI participates (Level 1) and *what* AI may recommend (Level 2)
   4. Low-resource environments (limited data, connectivity, computing)
   5. Decision architecture formalisation (E, S = f(E), G(S), A_AI(S), Safety Dominance Property)
   6. Human role in AI-assisted decision-making
   7. Socio-technical evaluation of AI systems
   8. Coastal fisheries as a safety-critical, low-resource domain
3. **Part 1 — Gap Analysis**: For each of the 8 themes:
   - List which papers address it (from Section 3 of each notes file: Yes / Partial / No)
   - Assess coverage depth (count of papers, strength of coverage)
   - Rate: Well-Covered / Partially Covered / Gap
   - For gaps: suggest what kind of paper to look for (domain, methodology, keywords)
4. **Part 2 — Literature Review Outline**: Organise extracted papers into a narrative structure:
   - Suggested section groupings (by theme or conceptual progression)
   - Which papers belong in each section and their role (supports motivation, fills background, represents baseline, highlights gap)
   - Suggested flow and transitions between sections
   - How each paper positions relative to the research gap
5. Save output to `papers/review-plan.md`
6. Report summary: total papers analysed, theme coverage overview, top gaps to fill

**Key decisions**:
- Read-only — does not modify notes files or tracker rows
- `papers/review-plan.md` is overwritten each run (living document, not versioned)
- Only analyses fully extracted papers (not previewed or studied-only)

---

## Project Structure After Implementation

```
research-test/
├── papers/
│   ├── sources/              # Drop PDF files here
│   ├── paper_tracker.md      # Table of all papers (extracted, previewed, studied)
│   └── review-plan.md        # Generated by /plan-review
├── notes/
│   ├── <title>.md            # Extracted notes
│   └── images/
│       └── <paper-slug>/     # Figures from each PDF
├── .claude/
│   ├── commands/
│   │   ├── extract-paper.md
│   │   ├── batch-extract.md
│   │   ├── quick-summary.md
│   │   ├── study-paper.md
│   │   ├── review-notes.md
│   │   └── plan-review.md
│   └── prompts/
│       └── paper_extraction_prompt.md
├── docs/
│   └── superpowers/
│       └── specs/
│           └── 2026-04-01-research-commands-design.md
└── README.md
```

---

## Tracker States

Papers can appear in `paper_tracker.md` in different states depending on which commands have been run:

| State | Type column | Relevance | Notes column | How it gets here |
|---|---|---|---|---|
| Previewed | `previewed` | `—` | `—` | `/quick-summary` |
| Studied | `studied` | `—` | `[study](...)` | `/study-paper` (no prior extraction) |
| Extracted | `review`, `empirical study`, etc. | Stars | `[notes](...)` | `/extract-paper` or `/batch-extract` |
| Extracted + Studied | `review`, `empirical study`, etc. | Stars | `[notes](...) · [study](...)` | `/extract-paper` then `/study-paper` |

When `/extract-paper` runs on a previously previewed paper, it overwrites the row (matches by title) with the full data.
