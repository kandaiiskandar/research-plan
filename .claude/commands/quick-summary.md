# Quick Summary

Generate a fast preview of a research paper and add it to the tracker as "previewed".

---

## Usage

```
/quick-summary <filename.pdf>
```

`<filename.pdf>` is the filename inside `papers/sources/`.

---

## Step 1: Resolve the PDF path

The input is: `$ARGUMENTS`

Verify the file exists:

```bash
ls "papers/sources/$ARGUMENTS"
```

If it doesn't exist, stop and tell the user which file was not found.

---

## Step 2: Parse the PDF

Run the claude-paper parser to extract structured text:

```bash
node /Users/iskandar/.claude/plugins/marketplaces/claude-paper/plugin/skills/study/scripts/parse-pdf.js "papers/sources/$ARGUMENTS"
```

If parsing fails, fall back to pymupdf:

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
" "papers/sources/$ARGUMENTS"
```

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
