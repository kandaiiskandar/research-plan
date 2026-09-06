# Search and Selection Protocol Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a defensible Search and Selection Protocol table — sourced from the actual review process — as a stand-alone canonical Markdown artefact. No downstream documents (manuscript, chapter, CLAUDE.md, citation map) are modified in this plan; those insertions and the corpus-count reconciliation are deferred to follow-up work.

**Architecture:** One canonical file, `docs/canonical/review-protocol.md`, carries both the reviewer-facing table (top section) and the source-of-truth detail sections that back every table cell (below). This single-file design eliminates the drift risk of maintaining two parallel documents. Task 1 elicits the facts and writes the file with the detail sections filled. Task 2 adds the table section on top, humanises the prose, posts to the user for sign-off, and commits only after the user approves.

**Tech Stack:** Markdown only; no code. Verification via `grep`. Humanizer skill for the caption and limitations prose.

**Spec:** Reviewer critique in the 2026-09-06 conversation turn ("Your literature review is good, but the methodology remains vulnerable"). The reviewer asked for a small table listing database, search date, search string families, inclusion/exclusion criteria, initial records, screened records, and final n = 72.

## Global Constraints

- **No fabrication.** Every figure in the table must trace either to an elicited user answer or to a marked "not recorded" limitation. If a value cannot be recovered, disclose it verbatim as `Not recorded — disclosed as limitation` rather than invent a plausible one.
- **Single source of truth.** Every table cell must trace to a §-section within the same file (`review-protocol.md`) — except for rows explicitly footnoted as sourced from another artefact (see the "Anchor systematic reviews" row, which is footnoted as sourced from `manuscript-v3.md:107`).
- **Citation notes rule.** If the table names a corpus paper (e.g., an anchor systematic review), the paper name carries a `[[notes]](path)` link per CLAUDE.md. Path prefix from `docs/canonical/` is `../../notes/`.
- **Figure abbreviation style.** "Fig. X", never "Figure X" — per user memory.
- **Humanizer required.** The caption paragraph and the §Limitations bullets must pass through the `humanizer` skill before commit. Table cells themselves are structured data and are not humanised.
- **Do not touch downstream documents.** No edits to `manuscript-v3.md`, the Chapter 2 draft, `CLAUDE.md`, or `citation-notes-map.md` in this plan.
- **Corpus count in this table = 72.** That is the manuscript's own figure and the reviewer-quoted figure; reconciliation with the 63 in CLAUDE.md and the 111/112 in the citation map / notes directory is a separate task and not in scope here. Record the discrepancy in the §Corpus reconciliation section as a known open item; the table row `Final corpus | 72` carries a live dependency on that reconciliation and must re-issue if the reconciled figure differs.
- **User sign-off before commit.** Both tasks end with a post-to-user step; commits happen only after the user approves the file contents.
- **Branch discipline.** Work on the current branch (`organize-file`). No push unless the user asks.

---

### Task 1: Elicit facts and draft the detail sections of `review-protocol.md`

**Files:**
- Create: `docs/canonical/review-protocol.md` (detail sections only; the table section is added in Task 2)

**Interfaces:**
- Consumes: user answers to the 13 elicitation questions below.
- Produces: A canonical document with every field either filled from the user's answer or carrying the literal `Not recorded — disclosed as limitation`. Task 2 reads this file to build the table.

- [ ] **Step 0: Check for an existing draft**

Run:
```bash
ls /Users/iskandar/Documents/my_stuff/research-test-2/docs/canonical/review-protocol.md 2>/dev/null
```
If the file exists, `Read` it and merge with the elicited answers instead of overwriting. If a merge conflict arises (existing value contradicts the user's fresh answer), pause and ask the user which value stands.

- [ ] **Step 1: Post the elicitation questions to the user in one message**

Ask, verbatim, for the following. For each, record either the answer or the literal string `Not recorded — will be disclosed as limitation`.

1. Databases actually searched. Manuscript currently claims: Scopus, IEEE Xplore, Web of Science, ACM Digital Library. Confirm or amend.
2. Search date(s) — single sweep date, or a rolling window (start → end)?
3. Publication date range applied as an inclusion filter (e.g., 2020–2026).
4. Search string families — actual query strings, or the concept blocks composed. Manuscript currently lists: AI governance, runtime assurance, safety filters, decision support, autonomy levels, guardrails; secondary: fisheries AI, low-resource deployment. Confirm or amend.
5. Initial candidate count (records returned before any screening).
6. Post-duplicate-removal count.
7. Post title/abstract screening count.
8. Final full-text corpus. Manuscript says 72; confirm this is authoritative for the table.
9. Inclusion criteria. v6 archive had: "addressed a mechanism that constrains or shapes AI behaviour during operation, targeted a safety-critical or human-in-the-loop context, or addressed AI deployment in low-resource / resource-constrained environments." Confirm or amend.
10. Exclusion criteria. v6 archive had: "training-time, fine-tuning, or static-configuration approaches with no runtime governance component." Confirm or amend.
11. Snowballing / citation chasing — used or not? If used, off which seed papers?
12. Coding — single reviewer or multiple? If single, was any dual-coding audit performed on a sample?
13. Disagreement / ambiguity handling — how was "Partial" adjudicated in the manuscript's TABLE I (and, later, in Table 2.1 of the thesis)?

- [ ] **Step 2: Write the detail sections of `review-protocol.md`**

Once the user answers, write the file using this structure. The table section at the top is a placeholder marker only — Task 2 fills it. Every detail field below is filled from the user's answers verbatim, or carries `Not recorded — disclosed as limitation`:

```markdown
# Review Protocol (canonical source of truth)

**Date:** 2026-09-06
**Role:** Single source of truth for all Search and Selection Protocol figures. The table in the top section below is the reviewer-facing deliverable; every cell traces to a §-section further down. Do NOT edit downstream artefacts without updating the relevant §-section here first.

## Search and Selection Protocol (table)

<!-- FILLED IN TASK 2 -->

---

## Databases

- [database, one per line]

## Dates

- Search executed: [date or range]
- Publication window (inclusion filter): [start–end]

## Search string families

- Primary: [list]
- Secondary: [list]

## Screening counts

| Stage | N |
|---|---|
| Initial records returned | [n] |
| After duplicate removal | [n] |
| After title/abstract screening | [n] |
| Retained for full-text review | [n] |
| Final corpus | 72 |

## Inclusion criteria

1. [criterion]
2. ...

## Exclusion criteria

1. [criterion]
2. ...

## Snowballing

[Statement]

## Anchor systematic reviews (secondary evidence)

Sourced from `manuscript-v3.md:107` — not from the elicitation.

- Indykov et al. — 206 papers, 16 architectural tactics
- Shamsujjoha et al. — 13 guardrail actions across 32 agent studies
- Perez-Cerrolaza et al. — 294 references

Total: 532 secondary references.

## Coding

- Reviewers: [single / N reviewers]
- Dimensions: Primary governance target · Runtime adaptation · Conditioning variable · Recommendation restriction (see manuscript-v3 TABLE I)
- Dual-coding audit: [performed on N% sample / not performed]
- Ambiguity adjudication: [how "Partial" was decided]

## Limitations (unrecorded elements)

- [Each item the user marked unrecorded, one bullet per line.]

## Corpus reconciliation (open — not resolved in this plan)

- **72** = final full-text-reviewed corpus (manuscript claim; used in the table).
- **111** = data rows in `citation-notes-map.md` as of 2026-09-06.
- **112** = `.md` files in `notes/` as of 2026-09-06.
- **63** = stale figure in `CLAUDE.md:82,137` as of 2026-09-06.
- Reconciliation of these four numbers is deferred to a follow-up task. If that reconciliation concludes n ≠ 72, the table row `Final corpus | 72` and every downstream artefact quoting 72 must re-issue.
```

- [ ] **Step 3: Verify every placeholder is resolved**

Run:
```bash
grep -nE '\[(date or range|start–end|list|n|criterion|single / N reviewers|performed on N% sample / not performed|how "Partial" was decided|database, one per line|Statement|Each item the user marked unrecorded, one bullet per line\.)\]' \
  /Users/iskandar/Documents/my_stuff/research-test-2/docs/canonical/review-protocol.md
```
Expected: zero matches. Each match is a template token that still needs replacing with either the user's answer or the literal `Not recorded — disclosed as limitation`.

Then read the file end-to-end to catch anything the token grep misses.

- [ ] **Step 4: Post the drafted detail sections to the user for sign-off**

Show the file contents (or the diff, if merging into an existing draft) and ask: "Detail sections drafted. Any corrections before I add the table section on top?"

- [ ] **Step 5: Apply any user edits, then commit**

```bash
git add docs/canonical/review-protocol.md
git commit -m "Add canonical review-protocol.md with elicited search and screening facts"
```

---

### Task 2: Add the Search and Selection Protocol table to `review-protocol.md`

**Files:**
- Modify: `docs/canonical/review-protocol.md` (fill the top `## Search and Selection Protocol (table)` section)

**Interfaces:**
- Consumes: every §-section written in Task 1.
- Produces: The reviewer-facing table + caption + provenance footnote, sitting at the top of `review-protocol.md`. This is the stand-alone artefact the user can copy into any downstream document when the deferred insertion tasks run.

- [ ] **Step 1: Write the table**

Fill the top `## Search and Selection Protocol (table)` section with the following structure. Values are pulled verbatim from the §-sections below. Rows whose value is `Not recorded — disclosed as limitation` display that phrase italicised and carry a footnote link to §Limitations.

**Live dependency callout:** the row `Final corpus | 72` depends on the deferred corpus-count reconciliation. If that reconciliation concludes n ≠ 72, this row re-issues.

```markdown
**Table 1. Search and Selection Protocol.**

| Protocol element | Value |
|---|---|
| Databases | [from §Databases] |
| Search executed | [from §Dates] |
| Publication window | [from §Dates] |
| Search string families (primary) | [from §Search string families] |
| Search string families (secondary) | [from §Search string families] |
| Inclusion criteria | [from §Inclusion criteria — one sentence per criterion, semicolon-separated] |
| Exclusion criteria | [from §Exclusion criteria — same treatment] |
| Snowballing | [from §Snowballing] |
| Initial records returned | [from §Screening counts] |
| After duplicate removal | [from §Screening counts] |
| After title/abstract screening | [from §Screening counts] |
| Retained for full-text review | [from §Screening counts] |
| Final corpus | 72 |
| Anchor systematic reviews (secondary evidence)ᵃ | Indykov et al. (206 papers) · Shamsujjoha et al. (32 agent studies) · Perez-Cerrolaza et al. (294 references) — 532 refs total |
| Coding — reviewers | [from §Coding] |
| Coding — dual-coding audit | [from §Coding] |
| Coding — ambiguity adjudication | [from §Coding] |

ᵃ Sourced from `manuscript-v3.md:107`, not from the elicitation. See §Anchor systematic reviews.
```

- [ ] **Step 2: Apply the screening-flow collapse rule if triggered**

Count the screening-count rows whose value is `Not recorded — disclosed as limitation`:
- If **fewer than 3** are unrecorded, keep the four rows as separate lines.
- If **3 or more** are unrecorded, collapse rows 9–12 into a single row:

```markdown
| Screening flow (initial → dedup → title/abstract → full-text) | *Not recorded — reconstructed from the retained corpus (n = 72); see §Limitations* |
```

Add a matching bullet to §Limitations explaining that intermediate screening counts were not archived at the time of the review and that only the retained corpus size is verifiable in artefacts.

- [ ] **Step 3: Add the caption paragraph immediately below the table**

Write one short paragraph (≤ 120 words) that:
(a) states the review is structured-purposive, not systematic (matches the manuscript's framing at `manuscript-v3.md:107`);
(b) refers the reader to the table;
(c) explicitly names the unrecorded elements from §Limitations as acknowledged limitations, in the reviewer's own vocabulary (initial records / duplicate removal / screening process / coder count / disagreement handling).

- [ ] **Step 4: Add `[[notes]]` links to the three anchor systematic reviews**

In the "Anchor systematic reviews (secondary evidence)ᵃ" table row, add `[[notes]](../../notes/…)` after each of Indykov, Shamsujjoha, and Perez-Cerrolaza. Look up filenames in `docs/canonical/citation-notes-map.md`.

- [ ] **Step 5: Humanize the caption paragraph and any prose in §Limitations**

Invoke: `Skill(humanizer)` on the caption and the §Limitations bullets. Apply the returned revisions. Do not humanise table cells or the §-sections' structured content.

- [ ] **Step 6: Verify every table cell traces to a §-section (or the footnoted external source)**

For each row, either:
- The value matches a §-section field in the same file (run `grep -F "<value>" docs/canonical/review-protocol.md` and confirm the hit is inside the §-section, not just the table itself), OR
- The row carries a footnote pointing to an external source (currently only the "Anchor systematic reviews" row, footnoted to `manuscript-v3.md:107`).

Any cell that satisfies neither is a fabrication — fix by pulling the correct value from the §-section, or (if legitimate compression) add a short "compression note" footnote below the table stating how the compression was done.

- [ ] **Step 7: Verify every `[[notes]]` link resolves**

Run:
```bash
grep -oE '\[\[notes\]\]\(([^)]+)\)' /Users/iskandar/Documents/my_stuff/research-test-2/docs/canonical/review-protocol.md | \
  sed -E 's/\[\[notes\]\]\(([^)]+)\)/\1/' | while read path; do
    resolved="/Users/iskandar/Documents/my_stuff/research-test-2/docs/canonical/$path"
    test -f "$resolved" && echo "OK  $path" || echo "MISSING  $path"
  done
```
Expected: every line prints `OK`.

- [ ] **Step 8: Verify the reviewer's 9-item request is satisfied**

Walk the reviewer's original list and confirm each item maps to a visible row (or an explicit §Limitations entry):

| Reviewer's ask | Table row / §Limitations entry |
|---|---|
| Databases | Row: Databases |
| Search date | Row: Search executed |
| Search string families | Rows: primary + secondary |
| Inclusion criteria | Row: Inclusion criteria |
| Exclusion criteria | Row: Exclusion criteria |
| Duplicate removal | Row 10 or collapsed screening-flow row |
| Initial records | Row 9 or collapsed screening-flow row |
| Screened records | Rows 10–11 or collapsed screening-flow row |
| Final n = 72 | Row: Final corpus |
| Coding — single vs multi researcher | Row: Coding — reviewers |
| Disagreement / ambiguity handling | Row: Coding — ambiguity adjudication |

Every item must have a row or a §Limitations entry. If any item is missing entirely, add it before proceeding.

- [ ] **Step 9: Post the completed file to the user for sign-off**

Show the top of `review-protocol.md` (table + caption + first ~30 lines) and ask: "Table drafted and verified. Any edits before I commit?"

- [ ] **Step 10: Apply any user edits, then commit**

```bash
git add docs/canonical/review-protocol.md
git commit -m "Add Search and Selection Protocol table to review-protocol.md"
```

---

## Self-Review

**Spec coverage.** Reviewer's list: databases, search date, search string families (primary + secondary), inclusion criteria, exclusion criteria, duplicate removal, initial records, screened records, final n = 72, coding process, disagreement handling. All 13 elicitation questions map to at least one row or §Limitations entry in Task 2's table, and Step 8 walks the reviewer's request explicitly.

**Placeholder scan.** Bracketed markers like `[from §Databases]` in the Task 2 table template are deliberate — they instruct the executor to pull values from the §-sections Task 1 fills. They are template markers, not implementation gaps. The literal string `Not recorded — disclosed as limitation` is the actual text that ships for any unrecovered field, not a placeholder. Task 1 Step 3 verifies every template token was resolved before the file is committed.

**Type consistency.** Row labels in Task 2's table match §-section names in Task 1's file. The final-corpus figure is fixed at 72 in both the table and §Screening counts, with an explicit live-dependency note tying them to the deferred reconciliation.

**Single-file design.** Both the reviewer-facing table and its supporting detail sections live in `review-protocol.md`. There is no second file to keep in sync.

**User sign-off gates.** Task 1 Step 4 and Task 2 Step 9 both require user approval before commit. Corrections travel back into the same file rather than accreting as fixup commits.

**Deferred work (out of scope, called out for the user).** (a) Reconciliation of the 63/72/111/112 corpus counts. (b) Restoration of the v6 screening paragraph into `manuscript-v3.md`. (c) Insertion of the table into `manuscript-v3.md`. (d) Insertion of the equivalent into the Chapter 2 draft. (e) Update to CLAUDE.md. Each is a separate plan when the user is ready.
