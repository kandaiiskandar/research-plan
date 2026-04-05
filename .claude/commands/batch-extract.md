# Batch Extract

Extract multiple PDFs in parallel using sub-agents. Each PDF gets its own agent running the full extraction workflow.

---

## Usage

```
/batch-extract
/batch-extract paper1.pdf paper2.pdf paper3.pdf
```

- No arguments: extracts all unprocessed PDFs in `papers/sources/`
- With arguments: extracts only the specified files (allows re-extraction even if already processed)

---

## Step 1: Determine which PDFs to extract

List all PDFs in `papers/sources/`:

```bash
ls papers/sources/*.pdf
```

List all existing notes in `notes/`:

```bash
ls notes/*.md 2>/dev/null
```

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
```bash
node /Users/iskandar/.claude/plugins/marketplaces/claude-paper/plugin/skills/study/scripts/parse-pdf.js "papers/sources/<FILENAME>"
```

If parsing fails, fall back to:
```bash
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
```

**Step 2: Read the extraction prompt**

Read the file at `.claude/prompts/paper_extraction_prompt.md`. This contains the full 17-section extraction template. Apply every section rigorously.

**Step 3: Perform the extraction**

Using the parsed PDF content and the extraction prompt, perform the full 17-section analysis. Identify the paper's full title.

**Step 4: Extract images**

Derive a paper slug from the title: lowercase, spaces to `-`, special characters (`:`, `/`, `*`, `?`, `"`, `<`, `>`, `|`, `\`) to `-`, collapse consecutive `-`, trim leading/trailing `-`.

```bash
mkdir -p "notes/images/<paper-slug>"
python3 /Users/iskandar/.claude/plugins/marketplaces/claude-paper/plugin/skills/study/scripts/extract-images.py "papers/sources/<FILENAME>" "notes/images/<paper-slug>"
```

List extracted images:
```bash
ls "notes/images/<paper-slug>" 2>/dev/null
```

If no images were extracted, set `images: none` in frontmatter. Rename key images descriptively where identifiable.

**Step 5: Save notes**

Save to `notes/<paper-slug>.md` with this format:

```yaml
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
```

If images were extracted, add a Figures table after frontmatter before Section 1.

Then include the full 17-section extraction.

**Step 6: Update tracker**

Read `papers/paper_tracker.md`. Check if the paper's title already exists:
- If it exists with Type = `previewed` or `studied`: replace that row with full data
- If it exists with full extraction data: replace with updated data
- If not in tracker: append a new row

Row format:

| Title | Authors | Year | Venue | Type | Relevance | Notes |
|-------|---------|------|-------|------|-----------|-------|
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
