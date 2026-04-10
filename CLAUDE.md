# Project Instructions

## Citation Reference Rule

**Whenever a paper from the corpus is cited or referenced in any document in this project, add a `[[notes]]` link immediately after the paper name.**

### Format

```
Author (Year) [[notes]](../notes/filename.md)
```

- From `docs/` → path prefix is `../notes/`
- From `papers/` → path prefix is `../notes/`
- Spaces in filenames must be URL-encoded as `%20`
- Special characters: `:` → `%3A`, `?` → `%3F`, `'` → `%27`, `,` → `%2C`, `&` → `%26`

### Reference lookup

The master citation → notes file mapping is at:
`docs/citation-notes-map.md`

This file contains ready-to-paste `[[notes]](path)` quick links for all 63 papers in the corpus.

**Special case**: Muhamad et al. (2024) notes file is in `../papers/sources/` not `../notes/`.

### When this rule applies

- Writing or updating any justification document (`docs/justification-*.md`)
- Writing or updating the literature review plan (`papers/review-plan.md`)
- Writing or updating the comparison table (`papers/comparison-table.md`)
- Writing any new document that cites corpus papers
- Any time a new paper is added to the corpus — add it to `docs/citation-notes-map.md` first, then use the link wherever the paper is cited

### When a new paper is added

1. Create the notes file in `notes/`
2. Add a new row to `docs/citation-notes-map.md` with the citation key, filename, and quick link
3. Add `[[notes]]` links wherever the paper is cited in existing documents

---

## Formal Model Consistency Rule

**Whenever a formal variable (e.g. a symbol in E = {w, r, m, o, v, t}) is defined or redefined, it must be consistent across ALL documents in the project.**

### The canonical definition file

`docs/appendix-c-formalisation.md` is the single source of truth for all formal variable definitions.

### Current canonical definitions

| Symbol | Type | Definition |
|---|---|---|
| w | ℝ≥0 | Wind speed (knots, sustained) |
| r | ordinal categorical | Rainfall intensity {none, light, moderate, heavy, storm} |
| m | ordinal categorical | Marine warning level {none, advisory, warning, alert} |
| o | ℝ≥0 × ℝ≥0 | Ocean state (wave height m, swell period s) |
| v | ordinal categorical | Vessel category {small, medium, big} |
| t | [0, 24) | Time of day (hour, 24-hour clock) |

### When a variable definition changes

1. **Update `docs/appendix-c-formalisation.md` first** — this is the canonical source
2. **Search all docs for the old definition** and update every occurrence
3. **Check these files every time** — they all reference E vector components:
   - `docs/justification-formal-model.md`
   - `docs/justification-safety-state-design.md`
   - `docs/justification-low-resource-environments.md`
   - `docs/justification-environmental-state-governance.md`
   - `papers/review-plan.md`
4. **Never define the same symbol differently in different documents**
