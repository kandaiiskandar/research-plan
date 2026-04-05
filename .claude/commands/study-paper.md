# Study Paper

Deep interactive study of a research paper using claude-paper's full study environment, with study materials linked back to the research notes and tracker.

---

## Usage

```
/study-paper <filename.pdf>
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

## Step 2: Invoke claude-paper:study

Invoke the `claude-paper:study` skill with the full path:

```
papers/sources/$ARGUMENTS
```

Follow all steps of the claude-paper:study skill (parse PDF, assess paper, generate study materials, extract images, update index, launch web UI). This generates materials in `~/claude-papers/papers/<paper-slug>/`.

**IMPORTANT**: Complete the full claude-paper:study workflow (Steps 0-8) before proceeding to Step 3 below. Note the `<paper-slug>` used by claude-paper.

---

## Step 3: Link study materials to notes

After study materials are generated, determine the paper slug from the claude-paper output (the folder name under `~/claude-papers/papers/`).

Check if a notes file exists in `notes/` for this paper by searching for the paper title in the YAML frontmatter of files in `notes/`:

```bash
grep -rl "<paper title>" notes/ 2>/dev/null
```

- **If a matching notes file exists**: Add a `study_materials:` field to its YAML frontmatter:
  ```yaml
  study_materials: "~/claude-papers/papers/<paper-slug>/"
  ```
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
