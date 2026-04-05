# Extract Paper

Extract structured research notes from a PDF in `papers/sources/` using the project extraction prompt, save to `notes/`, and update `papers/paper_tracker.md`.

---

## Usage

```
/extract-paper <filename.pdf>
```

`<filename.pdf>` is the filename inside `papers/sources/` (e.g. `my-paper.pdf`).

---

## Step 1: Resolve the PDF path

The input is: `$ARGUMENTS`

Set `PDF_PATH` to `papers/sources/$ARGUMENTS`.

Verify the file exists:

```bash
ls "papers/sources/$ARGUMENTS"
```

If it doesn't exist, stop and tell the user which file was not found.

---

## Step 2: Parse the PDF with claude-paper

Run the claude-paper parser to extract structured text:

```bash
node /Users/iskandar/.claude/plugins/marketplaces/claude-paper/plugin/skills/study/scripts/parse-pdf.js "papers/sources/$ARGUMENTS"
```

Capture the output. If parsing fails, fall back to reading the raw text content of the PDF using:

```bash
python3 -c "
import sys
try:
    import fitz  # pymupdf
    doc = fitz.open(sys.argv[1])
    text = '\n'.join(page.get_text() for page in doc)
    print(text)
except Exception as e:
    print(f'Error: {e}', file=sys.stderr)
" "papers/sources/$ARGUMENTS"
```

---

## Step 3: Read the extraction prompt

Read the file at `.claude/prompts/paper_extraction_prompt.md` to get the full extraction prompt.

---

## Step 4: Extract structured notes

Using the parsed PDF content and the extraction prompt, perform the full extraction analysis as described in the prompt. Apply every section (1 through 17) rigorously.

Identify the paper's **full title** from the parsed content. This will be used as the output filename.

---

## Step 5: Extract images from the PDF

Derive the paper slug (same slugification rules used for the notes filename: lowercase, spaces to `-`, special chars to `-`, collapse consecutive `-`).

Create the images directory:

```bash
mkdir -p "notes/images/<paper-slug>"
```

Run the claude-paper image extractor:

```bash
python3 /Users/iskandar/.claude/plugins/marketplaces/claude-paper/plugin/skills/study/scripts/extract-images.py \
  "papers/sources/$ARGUMENTS" \
  "notes/images/<paper-slug>"
```

After extraction, list the images found:

```bash
ls "notes/images/<paper-slug>"
```

If no images were extracted (empty folder or script error), note this in the frontmatter as `images: none` and continue. Do not stop the workflow.

Rename key images descriptively where their content is identifiable (e.g., `architecture.png`, `results_table.png`, `system_overview.png`). If content is unclear, keep the original filename.

---

## Step 6: Save notes to `notes/`

Create the output file at:

```
notes/<title>.md
```

Where `<title>` is the paper's full title with:
- All characters lowercased
- Spaces replaced with `-`
- Special characters (`:`, `/`, `*`, `?`, `"`, `<`, `>`, `|`, `\`) replaced with `-`
- Consecutive `-` collapsed to a single `-`
- Leading/trailing `-` trimmed

The notes file must begin with a YAML frontmatter block:

```yaml
---
title: "<Full Title>"
authors: "<Author 1>, <Author 2>, ..."
year: <year>
venue: "<Journal or Conference>"
type: "<empirical study | conceptual framework | review | system design | other>"
relevance: "<⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐>"
source: "papers/sources/$ARGUMENTS"
images: "notes/images/<paper-slug>/"
extracted: "<today's date YYYY-MM-DD>"
---
```

If images were extracted, add a section at the top of the notes (after frontmatter, before Section 1) listing them:

```markdown
## Figures

| File | Description |
|------|-------------|
| ![fig](images/<paper-slug>/architecture.png) | System architecture diagram |
| ... | ... |
```

Then include the full extraction output for all 17 sections.

---

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

---

## Step 8: Confirm completion

Report to the user:
- The notes file created: `notes/<title>.md`
- The images folder: `notes/images/<paper-slug>/` and how many images were extracted
- The row added to `papers/paper_tracker.md`
- The relevance score from Section 17
