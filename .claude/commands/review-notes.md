# Review Notes

Review a single extracted notes file for quality, completeness, and analytical depth against the extraction prompt.

---

## Usage

```
/review-notes <filename>.md
```

`<filename>.md` is the notes filename inside `notes/` (e.g., `the-significance-of-artificial-intelligence-ai-in-fishing-crafts-and-gears.md`).

---

## Step 1: Resolve the notes file

The input is: `$ARGUMENTS`

Verify the file exists:

```bash
ls "notes/$ARGUMENTS"
```

If it doesn't exist, stop and tell the user which file was not found. List available notes files:

```bash
ls notes/*.md
```

---

## Step 2: Read the notes and extraction prompt

Read both files:
1. `notes/$ARGUMENTS` — the notes file to review
2. `.claude/prompts/paper_extraction_prompt.md` — the extraction template that defines what each section should contain

---

## Step 3: Determine extraction path

The extraction prompt defines three paths based on relevance gates. Determine which path this notes file followed:

| Path | Trigger | Sections expected |
|---|---|---|
| **Early stop** | All three screening questions = No | Paper Identity + Reason for Exclusion + ⭐ Minimal only |
| **Reduced extraction** | 1–2 Yes or ≥ 2 Partial in Section 3 | Sections 1–7, 12–13, 16–17 |
| **Full extraction** | ≥ 3 Yes in Section 3 | All 17 sections |

Identify the path by checking:
- If the file contains "Early Relevance Check: STOPPED" → **Early stop**
- If the file is missing Sections 8–11 and 14–15 but has Sections 1–7, 12–13, 16–17 → **Reduced extraction**
- If all 17 sections are present → **Full extraction**
- If the file doesn't match any pattern → flag as **unclear extraction path** (likely extracted before the current prompt version)

---

## Step 4: Review the notes

Evaluate the notes against the criteria below, **scoped to the extraction path identified in Step 3**.

### Completeness
- Are all sections expected for this extraction path present?
- Is each present section substantively addressed (not just a heading with no content)?
- Are there any sections that say only "No" or "N/A" without explanation?
- **If early stop**: Is the reason for exclusion clear and justified? Could the paper plausibly be relevant (was it stopped too aggressively)?
- **If reduced extraction**: Were the correct sections included (4–7, 12–13, 16–17)? Were Sections 8–11, 14–15 correctly omitted?
- **If full extraction**: Are all 17 sections present and substantive?

### Depth
- Are answers specific to the paper being reviewed, or are they generic/boilerplate?
- For "No" answers in Section 3 (Relevance table), is there an explanation of WHY the theme is not addressed?
- Does Section 4 (Decision Architecture Analysis) analyse the paper's actual structure, or just state "no architecture"?
- Does Section 5 (Formal Model) address comparison to the Safety Dominance Property (AI(E) ⊆ A_AI(S))?
- Does Section 7 (Governance Level Analysis) use the Level 1 / Level 2 framework table and classify the paper's governance approach?
- Does Section 16 (Positioning) clearly explain what gap remains — particularly regarding the two-level governance pair (G(S), A_AI(S))?

### Accuracy
- Does the YAML frontmatter match the content? (title, authors, year, venue, type)
- Is the paper type consistent between frontmatter and Section 1?
- Are author names spelled consistently throughout?

### Research Alignment
- Does Section 3 (Relevance) map convincingly to all 8 research themes?
- Are the Yes/Partial/No ratings in Section 3 consistent with the detailed analysis in Sections 4–7?
- Does Section 7 (Governance Level Analysis) correctly classify:
  - Level 1 — Participation governance (equivalent to G(S))
  - Level 2 — Advisory scope governance (equivalent to A_AI(S))
  - Whether both levels are unified and state-conditioned
- Does Section 16 (Positioning) articulate a clear, specific gap — does the paper implement Level 1, Level 2, or both? Is it state-conditioned or static?

### Citable Content (full extraction only)
- Does Section 15 include 3–5 quotable points?
- Are quotes accompanied by section or page locations?
- Are the quotes specific enough to be useful in a literature review?

### Consistency
- Does the relevance score in Section 17 match the overall analysis and the extraction path taken?
- A paper rated ⭐⭐⭐⭐⭐ should have many "Yes" entries in Section 3 and full extraction
- A paper rated ⭐ or ⭐⭐ should have mostly "No" entries in Section 3 and early stop or reduced extraction
- Do the conclusions in Section 16 align with the evidence in earlier sections?
- Does the relevance score use the updated scale? (⭐⭐⭐⭐⭐ = directly addresses two-level governance gap; ⭐⭐⭐⭐ = addresses governance, formalisation, or safety-critical architecture)

---

## Step 5: Produce review report

Present the review as:

### Extraction Path

State which path was identified (early stop / reduced / full) and whether it was correctly applied.

### Quality Rating

Assign one of:
- **Strong** — all expected sections well-addressed, specific analysis, consistent ratings
- **Adequate** — most expected sections addressed but some lack depth or specificity
- **Needs Improvement** — missing expected sections, generic analysis, inconsistent ratings, or wrong extraction path

### Issues Found

Group issues by section number. For each issue:
- State what the problem is
- Explain why it matters
- Provide a concrete suggested rewrite

Example format:
> **Section 3 (Relevance to My Research)**: The "Low-resource environments" row says "Partial" but the explanation is vague ("mentions some constraints"). Suggested rewrite: "Partial — acknowledges digital divide and cost barriers for small-scale fishermen (Pros/Cons section) but does not design for low-resource constraints such as limited connectivity, data scarcity, or lightweight compute requirements."

> **Section 7 (Governance Level Analysis)**: Missing the Level 1 / Level 2 classification table. The section discusses governance generally but does not map the paper's approach to the participation governance (G(S)) vs advisory scope governance (A_AI(S)) framework. Add the governance level table from the extraction prompt.

### Summary

One paragraph summarising the overall notes quality, whether the extraction path was appropriate, and the most important improvements to make.

---

## Step 6: Offer to apply improvements

Ask the user:

> "Want me to apply these improvements to the notes file?"

- **If yes**: Edit the notes file directly using the suggested rewrites. Report which sections were updated.
- **If no**: Leave the file unchanged.

**Important**: Do NOT re-read the source PDF. All improvements are based on making the existing analysis more specific, complete, and internally consistent. If the notes need fundamentally different analysis (e.g., the paper was mischaracterised, or the extraction used an outdated prompt version), advise the user to re-run `/extract-paper`.
