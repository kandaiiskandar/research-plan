# Research Paper Extraction System

A Claude Code-powered workflow for extracting structured literature review notes from academic PDFs, tailored for PhD research on a **Graduated Safety-State-Gated Architecture for AI Decision Support in Low-Resource Environments: Design and Socio-Technical Evaluation in Coastal Fisheries**.

---

## Project Structure

```
research-test/
├── papers/
│   ├── sources/          # Drop PDF files here before extracting
│   └── paper_tracker.md  # Table of all extracted papers
├── notes/
│   ├── <title>.md        # Extracted notes, one file per paper
│   └── images/
│       └── <paper-slug>/ # Figures extracted from each PDF
├── .claude/
│   ├── commands/
│   │   └── extract-paper.md   # /extract-paper slash command
│   └── prompts/
│       └── paper_extraction_prompt.md  # 17-section extraction template
└── README.md
```

---

## Commands

### `/extract-paper <filename.pdf>`

Extracts structured research notes from a PDF.

**Steps performed:**
1. Verifies the PDF exists in `papers/sources/`
2. Parses the PDF using [claude-paper](https://github.com/alaliqing/claude-paper) (`parse-pdf.js`), falling back to pymupdf raw text extraction
3. Applies the full 17-section extraction prompt from `.claude/prompts/paper_extraction_prompt.md`
4. Extracts figures/images from the PDF into `notes/images/<paper-slug>/` using claude-paper's `extract-images.py`
5. Saves notes to `notes/<slugified-title>.md` with YAML frontmatter and a Figures table if images were found
6. Appends a row to `papers/paper_tracker.md`

**Usage:**
```
/extract-paper my-paper.pdf
```

**Requirements:**
- PDF must be placed in `papers/sources/` before running
- [claude-paper](https://github.com/alaliqing/claude-paper) must be installed (`~/.claude/plugins/marketplaces/claude-paper/`)
- Python 3 with `pymupdf` (`pip install pymupdf`) for fallback parsing

### `/quick-summary <filename.pdf>`

Fast preview of a paper before committing to full extraction.

**Steps performed:**
1. Parses the PDF using claude-paper
2. Generates a concise summary (overview, contribution, key findings, methodology)
3. Adds a "previewed" row to `papers/paper_tracker.md` (if not already tracked)

**Usage:**
```
/quick-summary my-paper.pdf
```

---

### `/batch-extract [file1.pdf file2.pdf ...]`

Extract multiple PDFs in parallel using sub-agents.

**Steps performed:**
1. Identifies unprocessed PDFs (or uses specified files)
2. Dispatches parallel agents (model: Opus) for each PDF
3. Each agent runs the full extraction workflow independently
4. Reports results with relevance scores

**Usage:**
```
/batch-extract                          # all unprocessed PDFs
/batch-extract paper1.pdf paper2.pdf    # specific files
```

---

### `/study-paper <filename.pdf>`

Deep interactive study using claude-paper's full study environment.

**Steps performed:**
1. Invokes `claude-paper:study` to generate study materials in `~/claude-papers/papers/<slug>/`
2. Links study materials to existing notes (if any) via `study_materials:` frontmatter
3. Updates `papers/paper_tracker.md` with a study link
4. Enters interactive deep learning loop for further exploration

**Usage:**
```
/study-paper my-paper.pdf
```

---

### `/review-notes <filename>.md`

Review a single extracted notes file for quality and completeness.

**Steps performed:**
1. Reads the notes file and the extraction prompt
2. Evaluates completeness, depth, accuracy, research alignment, citable content, and consistency
3. Produces a review report with quality rating and specific issues
4. Offers to apply improvements directly

**Usage:**
```
/review-notes the-significance-of-artificial-intelligence-ai-in-fishing-crafts-and-gears.md
```

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
```
/plan-review
```

---

## Extraction Template

The extraction prompt (`.claude/prompts/paper_extraction_prompt.md`) analyses each paper across **17 sections**:

| # | Section |
|---|---------|
| 1 | Paper Identity |
| 2 | Core Contribution |
| 3 | Relevance to My Research |
| 4 | Decision Architecture Analysis |
| 5 | Formal Model and Mathematical Representation |
| 6 | Safety State Classification |
| 7 | Governance Level Analysis |
| 8 | Human Role in Decision-Making |
| 9 | System Constraints and Environment |
| 10 | Hybrid AI Taxonomy |
| 11 | Baseline Comparison and Evaluation |
| 12 | Key Concepts and Definitions |
| 13 | Limitations and Unsolved Problems |
| 14 | Methodology Notes |
| 15 | Quotable / Citable Points |
| 16 | Relation to My Research and Positioning |
| 17 | Overall Relevance Score |

---

## Paper Tracker

`papers/paper_tracker.md` maintains a table of all extracted papers:

| Column | Description |
|---|---|
| Title | Full paper title |
| Authors | First author et al. |
| Year | Publication year |
| Venue | Journal or conference |
| Type | Paper type (review, empirical, conceptual, etc.) |
| Relevance | Star rating (⭐ to ⭐⭐⭐⭐⭐) from Section 17 |
| Notes | Link to the extracted notes file |

### Tracker States

Papers appear in different states depending on which commands have been run:

| State | Type column | Relevance | Notes column | Via command |
|---|---|---|---|---|
| Previewed | `previewed` | `—` | `—` | `/quick-summary` |
| Studied | `studied` | `—` | `[study](...)` | `/study-paper` |
| Extracted | actual type | Stars | `[notes](...)` | `/extract-paper` or `/batch-extract` |
| Extracted + Studied | actual type | Stars | `[notes](...) · [study](...)` | `/extract-paper` then `/study-paper` |

---

## Notes File Format

Each extracted file in `notes/` begins with YAML frontmatter:

```yaml
---
title: "Full Paper Title"
authors: "Author 1, Author 2, ..."
year: 2025
venue: "Journal or Conference"
type: "review | empirical study | conceptual framework | system design"
relevance: "⭐⭐⭐"
source: "papers/sources/filename.pdf"
images: "notes/images/<paper-slug>/"
extracted: "YYYY-MM-DD"
---
```

If images were extracted, a **Figures** table appears at the top of the notes (after frontmatter):

```markdown
## Figures

| File | Description |
|------|-------------|
| ![fig](images/<paper-slug>/architecture.png) | System architecture diagram |
```

Followed by the full 17-section extraction.

---

## Model Recommendation

The `/extract-paper` command runs in the active Claude Code session. For highest extraction quality (dense academic text, nuanced 17-section analysis), use **Claude Opus 4.6** (`claude-opus-4-6`). Claude Sonnet 4.6 is a good balance of quality and speed.

| Model | Quality | Speed | Recommended for |
|---|---|---|---|
| claude-opus-4-6 | Best | Slower | Deep analysis, complex papers |
| claude-sonnet-4-6 | Good | Fast | General use |
| claude-haiku-4-5 | Shallow | Fastest | Not recommended for extraction |

To switch models in Claude Code, use `/model` before running the command.

---

## Research Context

This system is built for a PhD literature review focused on:

- **Hybrid AI** (deterministic rule-based + probabilistic AI reasoning)
- **Safety-critical AI decision systems**
- **AI governance** — controlling *when* AI participates (Level 1) and *what* AI may recommend (Level 2)
- **Low-resource environments** (limited data, connectivity, computing)
- **Decision architecture formalisation** (E, S = f(E), G(S), A_AI(S), Safety Dominance Property)
- **Coastal fisheries** as the case study domain

The core architecture is formally defined as the pipeline:

**E → S = f(E) → (G(S), A_AI(S)) → AI(E)**

| Construct | Definition |
|---|---|
| Environmental state | E = {w, r, m, o, v, t} (wind, rainfall, marine warning, ocean condition, vessel class, trip state) |
| Safety state | S = f(E), where S ∈ {SAFE, CAUTION, UNSAFE} |
| AI participation gate (Level 1) | G(S) = 0 (AI blocked) or 1 (AI permitted) |
| AI-admissible recommendation space (Level 2) | A_AI(S) = set of permitted recommendation types per safety state |
| Recommendation types | R = {Go, Delay, DepartureTime, Duration} |
| Governance pair | (G(S), A_AI(S)) — two-level governance structure |
| Containment property | A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ |
| Safety Dominance Property | AI(E) ⊆ A_AI(S) — AI outputs bounded by safety state |
