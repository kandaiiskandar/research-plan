# Research Commands Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create 5 new Claude Code slash commands (`/batch-extract`, `/quick-summary`, `/study-paper`, `/review-notes`, `/plan-review`) to extend the research paper extraction system.

**Architecture:** Each command is a standalone Markdown file in `.claude/commands/`. Commands are prompt-based instructions that Claude Code interprets at runtime — no code compilation, no build step. The README is updated at the end to document all commands.

**Tech Stack:** Claude Code custom commands (Markdown), claude-paper plugin scripts (Node.js, Python), Agent tool for parallel dispatch.

**Spec:** `docs/superpowers/specs/2026-04-01-research-commands-design.md`

---

## File Structure

| Action | File | Responsibility |
|---|---|---|
| Create | `.claude/commands/batch-extract.md` | Parallel extraction of multiple PDFs |
| Create | `.claude/commands/quick-summary.md` | Fast paper preview with tracker update |
| Create | `.claude/commands/study-paper.md` | Deep study with link-back to notes/tracker |
| Create | `.claude/commands/review-notes.md` | Quality review of a single notes file |
| Create | `.claude/commands/plan-review.md` | Gap analysis + literature review outline |
| Modify | `README.md` | Add documentation for all 5 new commands |
| Modify | `.claude/commands/extract-paper.md` | Add logic to overwrite "previewed" rows |

---

### Task 1: Create `/quick-summary` command

**Files:**
- Create: `.claude/commands/quick-summary.md`

This is the simplest command and introduces the "previewed" tracker state that `/extract-paper` will need to handle.

- [ ] **Step 1: Create the command file**

Write `.claude/commands/quick-summary.md` with the following content:

```markdown
# Quick Summary

Generate a fast preview of a research paper and add it to the tracker as "previewed".

---

## Usage

\`\`\`
/quick-summary <filename.pdf>
\`\`\`

`<filename.pdf>` is the filename inside `papers/sources/`.

---

## Step 1: Resolve the PDF path

The input is: `$ARGUMENTS`

Verify the file exists:

\`\`\`bash
ls "papers/sources/$ARGUMENTS"
\`\`\`

If it doesn't exist, stop and tell the user which file was not found.

---

## Step 2: Parse the PDF

Run the claude-paper parser to extract structured text:

\`\`\`bash
node /Users/iskandar/.claude/plugins/marketplaces/claude-paper/plugin/skills/study/scripts/parse-pdf.js "papers/sources/$ARGUMENTS"
\`\`\`

If parsing fails, fall back to pymupdf:

\`\`\`bash
python3 -c "
import sys
try:
    import fitz
    doc = fitz.open(sys.argv[1])
    text = '\n'.join(page.get_text() for page in doc)
    print(text)
except Exception as e:
    print(f'Error: {e}', file=sys.stderr)
" "papers/sources/$ARGUMENTS"
\`\`\`

---

## Step 3: Generate summary

Using the parsed content, invoke the `claude-paper:summary` skill approach — generate a concise summary covering:

- **What it's about**: One-paragraph overview
- **Core contribution**: Main problem addressed and proposed solution
- **Key findings**: 3-5 bullet points of the most important results
- **Methodology**: Research method used
- **Domain**: Field and application area

Keep it concise — this is a preview, not the full 17-section extraction.

---

## Step 4: Extract metadata

From the parsed content, identify:
- **Title**: Full paper title
- **Authors**: All authors (use "First Author et al." if more than 2 for tracker)
- **Year**: Publication year
- **Venue**: Journal or conference name

---

## Step 5: Update tracker

Read `papers/paper_tracker.md`.

Check if the paper's title already appears in the tracker table:
- **If the title is already in the tracker** (either as fully extracted or previously previewed): Do NOT modify the tracker. Skip to Step 6.
- **If the title is NOT in the tracker**: Append a new row:

| Title | Authors | Year | Venue | Type | Relevance | Notes |
|-------|---------|------|-------|------|-----------|-------|
| <Full Title> | <First Author et al.> | <Year> | <Venue> | previewed | — | — |

---

## Step 6: Report to the user

Display:
- The summary from Step 3
- Whether the paper was added to the tracker as "previewed", was already previewed, or was already fully extracted
- Suggest: "Run `/extract-paper $ARGUMENTS` for the full 17-section analysis."
```

- [ ] **Step 2: Verify the command file was created**

```bash
ls .claude/commands/quick-summary.md
```

Expected: file exists.

- [ ] **Step 3: Commit**

```bash
git add .claude/commands/quick-summary.md
git commit -m "feat: add /quick-summary command for fast paper previews

Generates a concise summary using claude-paper and adds a 'previewed'
row to paper_tracker.md. No notes file is created.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

### Task 2: Update `/extract-paper` to handle "previewed" rows

**Files:**
- Modify: `.claude/commands/extract-paper.md`

The existing `/extract-paper` command always appends a new row. It now needs to check for and overwrite any existing "previewed" row for the same paper.

- [ ] **Step 1: Update the tracker step in extract-paper.md**

In `.claude/commands/extract-paper.md`, find the section `## Step 7: Update \`papers/paper_tracker.md\`` and replace its content. The current text is:

```
Append a new row to the Markdown table in `papers/paper_tracker.md`.
```

Replace the entire Step 7 section with:

```markdown
## Step 7: Update `papers/paper_tracker.md`

Read the current content of `papers/paper_tracker.md`.

Check if the paper's title already appears in the tracker table:
- **If the title exists with Type = `previewed`**: Replace that entire row with the full extraction data.
- **If the title exists with Type = `studied`**: Replace that row, preserving any `[study]()` link in the Notes column by appending it after the new `[notes]()` link (e.g., `[notes](...) · [study](...)`).
- **If the title exists with full extraction data**: Replace the row with updated data (re-extraction).
- **If the title is NOT in the tracker**: Append a new row.

The table columns are:

| Title | Authors | Year | Venue | Type | Relevance | Notes |
|-------|---------|------|-------|------|-----------|-------|

- **Title**: Full paper title (plain text)
- **Authors**: First author et al. (if more than 2 authors), or all authors if 1–2
- **Year**: Publication year
- **Venue**: Journal or conference name
- **Type**: Paper type (empirical study, conceptual framework, review, system design, etc.)
- **Relevance**: The star rating from Section 17 (e.g. `⭐⭐⭐⭐`)
- **Notes**: A markdown link to the notes file, e.g. `[notes](../notes/<title>.md)`
```

- [ ] **Step 2: Verify the edit was applied**

Read `.claude/commands/extract-paper.md` and confirm Step 7 now includes the "previewed" row handling logic.

- [ ] **Step 3: Commit**

```bash
git add .claude/commands/extract-paper.md
git commit -m "feat: update /extract-paper to overwrite previewed/studied tracker rows

When a paper was previously previewed or studied, /extract-paper now
replaces the existing tracker row instead of appending a duplicate.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

### Task 3: Create `/study-paper` command

**Files:**
- Create: `.claude/commands/study-paper.md`

- [ ] **Step 1: Create the command file**

Write `.claude/commands/study-paper.md` with the following content:

```markdown
# Study Paper

Deep interactive study of a research paper using claude-paper's full study environment, with study materials linked back to the research notes and tracker.

---

## Usage

\`\`\`
/study-paper <filename.pdf>
\`\`\`

`<filename.pdf>` is the filename inside `papers/sources/`.

---

## Step 1: Resolve the PDF path

The input is: `$ARGUMENTS`

Verify the file exists:

\`\`\`bash
ls "papers/sources/$ARGUMENTS"
\`\`\`

If it doesn't exist, stop and tell the user which file was not found.

---

## Step 2: Invoke claude-paper:study

Invoke the `claude-paper:study` skill with the full path:

\`\`\`
papers/sources/$ARGUMENTS
\`\`\`

Follow all steps of the claude-paper:study skill (parse PDF, assess paper, generate study materials, extract images, update index, launch web UI). This generates materials in `~/claude-papers/papers/<paper-slug>/`.

**IMPORTANT**: Complete the full claude-paper:study workflow (Steps 0-8) before proceeding to Step 3 below. Note the `<paper-slug>` used by claude-paper.

---

## Step 3: Link study materials to notes

After study materials are generated, determine the paper slug from the claude-paper output (the folder name under `~/claude-papers/papers/`).

Check if a notes file exists in `notes/` for this paper by searching for the paper title in the YAML frontmatter of files in `notes/`:

\`\`\`bash
grep -rl "<paper title>" notes/ 2>/dev/null
\`\`\`

- **If a matching notes file exists**: Add a `study_materials:` field to its YAML frontmatter:
  \`\`\`yaml
  study_materials: "~/claude-papers/papers/<paper-slug>/"
  \`\`\`
- **If no matching notes file exists**: Do not create one.

---

## Step 4: Update tracker

Read `papers/paper_tracker.md`.

Check if the paper's title already appears in the tracker table:

- **If the paper has an existing row with a `[notes]` link**: Add the study link after the notes link in the Notes column:
  `[notes](../notes/<title>.md) · [study](~/claude-papers/papers/<paper-slug>/)`

- **If the paper has an existing row without a `[notes]` link** (e.g., previewed): Replace the row with:
  | Title | Authors | Year | Venue | Type | Relevance | Notes |
  |-------|---------|------|-------|------|-----------|-------|
  | <Title> | <Authors> | <Year> | <Venue> | studied | — | [study](~/claude-papers/papers/<paper-slug>/) |

- **If the paper is NOT in the tracker**: Append a new row:
  | Title | Authors | Year | Venue | Type | Relevance | Notes |
  |-------|---------|------|-------|------|-----------|-------|
  | <Title> | <Authors> | <Year> | <Venue> | studied | — | [study](~/claude-papers/papers/<paper-slug>/) |

---

## Step 5: Continue interactive study

Continue with the claude-paper:study interactive deep learning loop (Step 9 from the skill):

1. Ask the user:
   - What part is still unclear?
   - Do you want deeper mathematical breakdown?
   - Do you want implementation-level analysis?
   - Do you want comparison with another paper?

2. Generate additional study files as requested (deep-dives, comparisons, etc.) inside the `~/claude-papers/papers/<paper-slug>/` folder.
```

- [ ] **Step 2: Verify the command file was created**

```bash
ls .claude/commands/study-paper.md
```

Expected: file exists.

- [ ] **Step 3: Commit**

```bash
git add .claude/commands/study-paper.md
git commit -m "feat: add /study-paper command for deep interactive paper study

Invokes claude-paper:study to generate full study materials, then links
them back to the project's notes and paper_tracker.md.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

### Task 4: Create `/review-notes` command

**Files:**
- Create: `.claude/commands/review-notes.md`

- [ ] **Step 1: Create the command file**

Write `.claude/commands/review-notes.md` with the following content:

```markdown
# Review Notes

Review a single extracted notes file for quality, completeness, and analytical depth against the extraction prompt.

---

## Usage

\`\`\`
/review-notes <filename>.md
\`\`\`

`<filename>.md` is the notes filename inside `notes/` (e.g., `the-significance-of-artificial-intelligence-ai-in-fishing-crafts-and-gears.md`).

---

## Step 1: Resolve the notes file

The input is: `$ARGUMENTS`

Verify the file exists:

\`\`\`bash
ls "notes/$ARGUMENTS"
\`\`\`

If it doesn't exist, stop and tell the user which file was not found. List available notes files:

\`\`\`bash
ls notes/*.md
\`\`\`

---

## Step 2: Read the notes and extraction prompt

Read both files:
1. `notes/$ARGUMENTS` — the notes file to review
2. `.claude/prompts/paper_extraction_prompt.md` — the extraction template that defines what each section should contain

---

## Step 3: Review the notes

Evaluate the notes against these criteria:

### Completeness
- Are all 17 sections present (Paper Identity through Overall Relevance Score)?
- Is each section substantively addressed (not just a heading with no content)?
- Are there any sections that say only "No" or "N/A" without explanation?

### Depth
- Are answers specific to the paper being reviewed, or are they generic/boilerplate?
- For "No" answers in Section 3 (Relevance table), is there an explanation of WHY the theme is not addressed?
- Does Section 4 (Decision Architecture Analysis) analyse the paper's actual structure, or just state "no architecture"?
- Does Section 16 (Positioning) clearly explain what gap remains after this paper?

### Accuracy
- Does the YAML frontmatter match the content? (title, authors, year, venue, type)
- Is the paper type consistent between frontmatter and Section 1?
- Are author names spelled consistently throughout?

### Research Alignment
- Does Section 3 (Relevance) map convincingly to all 8 research themes?
- Are the Yes/Partial/No ratings in Section 3 consistent with the detailed analysis in Sections 4-10?
- Does Section 16 (Positioning) articulate a clear, specific gap that the user's research fills?

### Citable Content
- Does Section 15 include 3-5 quotable points?
- Are quotes accompanied by section or page locations?
- Are the quotes specific enough to be useful in a literature review?

### Consistency
- Does the relevance score in Section 17 match the overall analysis?
- A paper rated ⭐⭐⭐⭐⭐ should have many "Yes" entries in Section 3
- A paper rated ⭐ or ⭐⭐ should have mostly "No" entries in Section 3
- Do the conclusions in Section 16 align with the evidence in earlier sections?

---

## Step 4: Produce review report

Present the review as:

### Quality Rating

Assign one of:
- **Strong** — all sections well-addressed, specific analysis, consistent ratings
- **Adequate** — most sections addressed but some lack depth or specificity
- **Needs Improvement** — missing sections, generic analysis, or inconsistent ratings

### Issues Found

Group issues by section number. For each issue:
- State what the problem is
- Explain why it matters
- Provide a concrete suggested rewrite

Example format:
> **Section 3 (Relevance to My Research)**: The "Low-resource environments" row says "Partial" but the explanation is vague ("mentions some constraints"). Suggested rewrite: "Partial — acknowledges digital divide and cost barriers for small-scale fishermen (Pros/Cons section) but does not design for low-resource constraints such as limited connectivity, data scarcity, or lightweight compute requirements."

### Summary

One paragraph summarising the overall notes quality and the most important improvements to make.

---

## Step 5: Offer to apply improvements

Ask the user:

> "Want me to apply these improvements to the notes file?"

- **If yes**: Edit the notes file directly using the suggested rewrites. Report which sections were updated.
- **If no**: Leave the file unchanged.

**Important**: Do NOT re-read the source PDF. All improvements are based on making the existing analysis more specific, complete, and internally consistent. If the notes need fundamentally different analysis (e.g., the paper was mischaracterised), advise the user to re-run `/extract-paper`.
```

- [ ] **Step 2: Verify the command file was created**

```bash
ls .claude/commands/review-notes.md
```

Expected: file exists.

- [ ] **Step 3: Commit**

```bash
git add .claude/commands/review-notes.md
git commit -m "feat: add /review-notes command for notes quality review

Reviews a single notes file against the extraction prompt for
completeness, depth, accuracy, and consistency. Offers to apply fixes.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

### Task 5: Create `/plan-review` command

**Files:**
- Create: `.claude/commands/plan-review.md`

- [ ] **Step 1: Create the command file**

Write `.claude/commands/plan-review.md` with the following content:

```markdown
# Plan Review

Analyse all extracted papers to identify theme coverage gaps and produce a structured literature review outline.

---

## Usage

\`\`\`
/plan-review
\`\`\`

No arguments. Analyses all fully extracted papers in `notes/`.

---

## Step 1: Gather all extracted notes

List and read all `.md` files in `notes/`:

\`\`\`bash
ls notes/*.md
\`\`\`

Read each file. **Skip** any file that does not contain all 17 extraction sections (e.g., files without a `## 17. Overall Relevance Score` section). These are incomplete extractions.

Report how many papers were found and how many were skipped.

If no fully extracted papers are found, stop and report: "No fully extracted papers found in notes/. Run /extract-paper first."

---

## Step 2: Read the research themes

Read `.claude/prompts/paper_extraction_prompt.md` to get the 8 research themes:

1. Hybrid AI (deterministic rule-based + probabilistic AI reasoning)
2. Safety-critical AI decision systems
3. AI governance — controlling *when* AI participates (Level 1) and *what* AI may recommend (Level 2)
4. Low-resource environments (limited data, connectivity, computing)
5. Decision architecture formalisation (E, S = f(E), G(S), A_AI(S), Safety Dominance Property)
6. Human role in AI-assisted decision-making
7. Socio-technical evaluation of AI systems
8. Coastal fisheries as a safety-critical, low-resource domain

---

## Step 3: Gap Analysis

For each of the 8 themes, compile data from Section 3 (Relevance to My Research) across ALL extracted notes:

For each theme, produce:

### Theme: <Theme Name>

**Coverage**: <Well-Covered / Partially Covered / Gap>

| Paper | Rating | Summary |
|-------|--------|---------|
| <Paper Title 1> | Yes / Partial / No | <How it relates, from Section 3> |
| <Paper Title 2> | Yes / Partial / No | <How it relates, from Section 3> |

**Assessment**: <1-2 sentences on whether the theme has sufficient coverage for the literature review>

**If Gap or Partially Covered — Search Suggestions**:
- Suggested paper types to look for (e.g., "empirical study of hybrid AI in safety-critical domains")
- Suggested search keywords
- Suggested domains to look in (e.g., aviation, healthcare, maritime)

Use these rating rules:
- **Well-Covered**: 3+ papers rated "Yes", or 2 "Yes" + multiple "Partial"
- **Partially Covered**: 1-2 papers rated "Yes", or several "Partial"
- **Gap**: No papers rated "Yes", at most 1-2 "Partial"

---

## Step 4: Literature Review Outline

Based on the gap analysis, organise the extracted papers into a structured narrative:

### Suggested Structure

Propose a literature review outline with:

1. **Section groupings**: Group papers by theme or conceptual progression. Each section should have a clear purpose (e.g., "Domain Background", "Safety-Critical AI Systems", "Hybrid AI Architectures", "AI Governance Mechanisms", "Research Gap").

2. **Paper placement**: For each section, list which papers belong there and their role:
   - **Supports motivation**: Paper establishes why the research problem matters
   - **Fills background**: Paper provides necessary context or definitions
   - **Represents baseline**: Paper represents an approach the research compares against
   - **Highlights gap**: Paper demonstrates what is missing that the research addresses

3. **Flow and transitions**: For each section transition, suggest how to connect the ideas (e.g., "After establishing that hybrid AI is used in safety-critical domains, transition to the gap: none of these systems implement graduated AI governance").

4. **Positioning summary**: One paragraph explaining how the collected literature positions the research contribution — what is well-established, what is partially addressed, and what gap remains.

---

## Step 5: Save output

Save the complete gap analysis and literature review outline to:

\`\`\`
papers/review-plan.md
\`\`\`

The file should contain:
1. Header with date and number of papers analysed
2. Full gap analysis (all 8 themes)
3. Full literature review outline
4. Coverage summary table

Format the coverage summary as:

| Theme | Coverage | Papers (Yes) | Papers (Partial) | Papers (No) |
|-------|----------|--------------|-------------------|-------------|
| ... | ... | ... | ... | ... |

This file is overwritten each time `/plan-review` is run.

---

## Step 6: Report summary

Report to the user:
- Total papers analysed
- Coverage summary: which themes are well-covered, partially covered, or gaps
- Top 3 gaps to prioritise filling
- The file was saved to `papers/review-plan.md`
```

- [ ] **Step 2: Verify the command file was created**

```bash
ls .claude/commands/plan-review.md
```

Expected: file exists.

- [ ] **Step 3: Commit**

```bash
git add .claude/commands/plan-review.md
git commit -m "feat: add /plan-review command for gap analysis and review outline

Analyses all extracted papers against 8 research themes, identifies
coverage gaps, and produces a structured literature review outline.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

### Task 6: Create `/batch-extract` command

**Files:**
- Create: `.claude/commands/batch-extract.md`

This is the most complex command because it inlines the full extraction workflow for sub-agents.

- [ ] **Step 1: Create the command file**

Write `.claude/commands/batch-extract.md` with the following content:

```markdown
# Batch Extract

Extract multiple PDFs in parallel using sub-agents. Each PDF gets its own agent running the full extraction workflow.

---

## Usage

\`\`\`
/batch-extract
/batch-extract paper1.pdf paper2.pdf paper3.pdf
\`\`\`

- No arguments: extracts all unprocessed PDFs in `papers/sources/`
- With arguments: extracts only the specified files (allows re-extraction even if already processed)

---

## Step 1: Determine which PDFs to extract

List all PDFs in `papers/sources/`:

\`\`\`bash
ls papers/sources/*.pdf
\`\`\`

List all existing notes in `notes/`:

\`\`\`bash
ls notes/*.md 2>/dev/null
\`\`\`

**If `$ARGUMENTS` is provided** (one or more filenames separated by spaces):
- Use those filenames as the list of PDFs to extract
- Verify each file exists in `papers/sources/`; report any missing files and skip them
- These are extracted even if notes already exist (allows re-extraction)

**If `$ARGUMENTS` is empty** (no arguments):
- Compare the PDF list against existing notes to find unprocessed papers
- A PDF is "unprocessed" if no file in `notes/` has a `source:` frontmatter field matching `papers/sources/<filename>`
- Use only unprocessed PDFs
- If no unprocessed PDFs are found, report "All papers in papers/sources/ have already been extracted." and stop

Report which PDFs will be extracted and how many.

---

## Step 2: Dispatch parallel agents

For each PDF to extract, dispatch a `general-purpose` agent with `model: opus` using the Agent tool.

**All agents should be dispatched in a single message** (parallel execution).

Each agent's prompt must include the complete extraction workflow inlined (since sub-agents cannot invoke slash commands). Use this prompt template for each agent, replacing `<FILENAME>` with the actual PDF filename:

---

**Agent prompt template:**

You are extracting structured research notes from a PDF for a PhD literature review.

**Your task**: Extract the paper at `papers/sources/<FILENAME>`, save notes to `notes/`, and update `papers/paper_tracker.md`.

**Step 1: Parse the PDF**

Run:
\`\`\`bash
node /Users/iskandar/.claude/plugins/marketplaces/claude-paper/plugin/skills/study/scripts/parse-pdf.js "papers/sources/<FILENAME>"
\`\`\`

If parsing fails, fall back to:
\`\`\`bash
python3 -c "
import sys
try:
    import fitz
    doc = fitz.open(sys.argv[1])
    text = '\n'.join(page.get_text() for page in doc)
    print(text)
except Exception as e:
    print(f'Error: {e}', file=sys.stderr)
" "papers/sources/<FILENAME>"
\`\`\`

**Step 2: Read the extraction prompt**

Read the file at `.claude/prompts/paper_extraction_prompt.md`. This contains the full 17-section extraction template. Apply every section rigorously.

**Step 3: Perform the extraction**

Using the parsed PDF content and the extraction prompt, perform the full 17-section analysis. Identify the paper's full title.

**Step 4: Extract images**

Derive a paper slug from the title: lowercase, spaces to `-`, special characters (`:`, `/`, `*`, `?`, `"`, `<`, `>`, `|`, `\`) to `-`, collapse consecutive `-`, trim leading/trailing `-`.

\`\`\`bash
mkdir -p "notes/images/<paper-slug>"
python3 /Users/iskandar/.claude/plugins/marketplaces/claude-paper/plugin/skills/study/scripts/extract-images.py "papers/sources/<FILENAME>" "notes/images/<paper-slug>"
\`\`\`

List extracted images:
\`\`\`bash
ls "notes/images/<paper-slug>" 2>/dev/null
\`\`\`

If no images were extracted, set `images: none` in frontmatter. Rename key images descriptively where identifiable.

**Step 5: Save notes**

Save to `notes/<paper-slug>.md` with this format:

\`\`\`yaml
---
title: "<Full Title>"
authors: "<Author 1>, <Author 2>, ..."
year: <year>
venue: "<Journal or Conference>"
type: "<empirical study | conceptual framework | review | system design | other>"
relevance: "<star rating from Section 17>"
source: "papers/sources/<FILENAME>"
images: "notes/images/<paper-slug>/"
extracted: "<today's date YYYY-MM-DD>"
---
\`\`\`

If images were extracted, add a Figures table after frontmatter before Section 1.

Then include the full 17-section extraction.

**Step 6: Update tracker**

Read `papers/paper_tracker.md`. Check if the paper's title already exists:
- If it exists with Type = `previewed` or `studied`: replace that row with full data
- If it exists with full extraction data: replace with updated data
- If not in tracker: append a new row

Row format:
| Title | Authors | Year | Venue | Type | Relevance | Notes |
| <Full Title> | <First Author et al.> | <Year> | <Venue> | <type> | <stars> | [notes](../notes/<paper-slug>.md) |

**Step 7: Report**

Return a brief summary: paper title, relevance score, notes filename.

---

**End of agent prompt template.**

---

## Step 3: Report results

After all agents complete, compile results and report to the user:

- Total papers extracted
- For each paper: title, relevance score, notes file path
- Any failures (which PDFs failed and why)
- Reminder: "Run `/review-notes <filename>.md` to review any extraction."
```

- [ ] **Step 2: Verify the command file was created**

```bash
ls .claude/commands/batch-extract.md
```

Expected: file exists.

- [ ] **Step 3: Commit**

```bash
git add .claude/commands/batch-extract.md
git commit -m "feat: add /batch-extract command for parallel PDF extraction

Dispatches parallel agents (model: opus) to extract multiple PDFs
simultaneously. Supports both automatic unprocessed detection and
explicit file lists for re-extraction.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

### Task 7: Update README with all new commands

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Add new commands to README**

In `README.md`, find the section ending after the `/extract-paper` command documentation (after the `**Requirements:**` block and its closing `---`). Insert the following new command documentation before the `## Extraction Template` section:

```markdown
### `/quick-summary <filename.pdf>`

Fast preview of a paper before committing to full extraction.

**Steps performed:**
1. Parses the PDF using claude-paper
2. Generates a concise summary (overview, contribution, key findings, methodology)
3. Adds a "previewed" row to `papers/paper_tracker.md` (if not already tracked)

**Usage:**
\`\`\`
/quick-summary my-paper.pdf
\`\`\`

---

### `/batch-extract [file1.pdf file2.pdf ...]`

Extract multiple PDFs in parallel using sub-agents.

**Steps performed:**
1. Identifies unprocessed PDFs (or uses specified files)
2. Dispatches parallel agents (model: Opus) for each PDF
3. Each agent runs the full extraction workflow independently
4. Reports results with relevance scores

**Usage:**
\`\`\`
/batch-extract                          # all unprocessed PDFs
/batch-extract paper1.pdf paper2.pdf    # specific files
\`\`\`

---

### `/study-paper <filename.pdf>`

Deep interactive study using claude-paper's full study environment.

**Steps performed:**
1. Invokes `claude-paper:study` to generate study materials in `~/claude-papers/papers/<slug>/`
2. Links study materials to existing notes (if any) via `study_materials:` frontmatter
3. Updates `papers/paper_tracker.md` with a study link
4. Enters interactive deep learning loop for further exploration

**Usage:**
\`\`\`
/study-paper my-paper.pdf
\`\`\`

---

### `/review-notes <filename>.md`

Review a single extracted notes file for quality and completeness.

**Steps performed:**
1. Reads the notes file and the extraction prompt
2. Evaluates completeness, depth, accuracy, research alignment, citable content, and consistency
3. Produces a review report with quality rating and specific issues
4. Offers to apply improvements directly

**Usage:**
\`\`\`
/review-notes the-significance-of-artificial-intelligence-ai-in-fishing-crafts-and-gears.md
\`\`\`

---

### `/plan-review`

Analyse all extracted papers for theme coverage gaps and produce a literature review outline.

**Steps performed:**
1. Reads all fully extracted notes in `notes/`
2. Compiles coverage data for all 8 research themes
3. Produces gap analysis (Well-Covered / Partially Covered / Gap per theme)
4. Generates a structured literature review outline with section groupings and paper placement
5. Saves output to `papers/review-plan.md`

**Usage:**
\`\`\`
/plan-review
\`\`\`

---
```

- [ ] **Step 2: Add Tracker States section to README**

Find the `## Paper Tracker` section in `README.md`. After the existing column description table and before the `---`, add:

```markdown

### Tracker States

Papers appear in different states depending on which commands have been run:

| State | Type column | Relevance | Notes column | Via command |
|---|---|---|---|---|
| Previewed | `previewed` | `—` | `—` | `/quick-summary` |
| Studied | `studied` | `—` | `[study](...)` | `/study-paper` |
| Extracted | actual type | Stars | `[notes](...)` | `/extract-paper` or `/batch-extract` |
| Extracted + Studied | actual type | Stars | `[notes](...) · [study](...)` | `/extract-paper` then `/study-paper` |
```

- [ ] **Step 3: Verify README was updated**

Read `README.md` and confirm all 5 new commands are documented and the Tracker States section is present.

- [ ] **Step 4: Commit**

```bash
git add README.md
git commit -m "docs: add documentation for all new research commands

Documents /quick-summary, /batch-extract, /study-paper, /review-notes,
and /plan-review commands. Adds tracker states reference table.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

## Self-Review

**Spec coverage check:**
- `/batch-extract` — Task 6: parallel agents, auto-detect unprocessed, explicit file list, inlined workflow. Covered.
- `/quick-summary` — Task 1: parse, summarise, previewed tracker row. Covered.
- `/study-paper` — Task 3: invoke study skill, link to notes/tracker, interactive loop. Covered.
- `/review-notes` — Task 4: single file review, 6 criteria, quality rating, offer to apply. Covered.
- `/plan-review` — Task 5: 8 themes, gap analysis, lit review outline, save to review-plan.md. Covered.
- `/extract-paper` update for previewed rows — Task 2. Covered.
- README update — Task 7. Covered.
- Tracker states (previewed, studied, extracted, extracted+studied) — covered in Tasks 1-3 and Task 7.

**Placeholder scan:** No TBDs, TODOs, or "implement later" found. All command files have complete content.

**Type consistency:** Slugification rules are consistently described across Tasks 1, 3, 5, 6. Tracker column format is consistent. `paper_tracker.md` row format matches across all tasks.
