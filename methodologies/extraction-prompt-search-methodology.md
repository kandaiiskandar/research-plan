# Search Methodology Documentation Prompt

*For: "A Graduated Safety-State-Gated Architecture for AI Decision Support in Low-Resource Environments: Design and Socio-Technical Evaluation in Coastal Fisheries"*

---

You are assisting with documenting the literature search methodology for a PhD literature review. The goal is to produce a PRISMA-compliant search protocol document saved as `papers/search-methodology.md`.

**Most of the information needed can be derived directly from the existing notes files.** Read all 55 notes files in `notes/` plus `papers/paper_tracker.md` and `papers/review-plan.md` to auto-populate as much as possible. Flag only what genuinely requires user input.

---

## Step 1: Extract from Notes (auto-derivable)

Read all notes files in `notes/` and extract the following:

### 1A — Venue Distribution (→ infer databases searched)

From Section 1 (Paper Identity) of each note, extract the venue. Group into database categories:

| Database | Venue types | Papers found |
|---|---|---|
| ACM Digital Library | ACM journals, ACM conferences, Communications of the ACM | count |
| IEEE Xplore | IEEE journals, IEEE conferences, IEEE Transactions | count |
| Springer / SpringerLink | Springer journals, Lecture Notes | count |
| Elsevier / ScienceDirect | Elsevier journals (e.g., Safety Science, Ocean & Coastal Management) | count |
| Taylor & Francis | Taylor & Francis journals (e.g., Int. J. Human-Computer Interaction) | count |
| arXiv | arXiv preprints | count |
| MDPI | MDPI journals (e.g., AI, Sensors, Applied Sciences) | count |
| Wiley | Wiley journals (e.g., ICES Journal) | count |
| Other / Multiple | Reports, standards, interdisciplinary venues | count |

List all unique venues found across all 55 papers under each category.

### 1B — Date Range

From Section 1 of each note, extract all publication years. Report:
- Earliest year in corpus
- Latest year in corpus
- Distribution by year (count per year)

### 1C — Extraction Path Distribution

From `papers/paper_tracker.md` Status column, count:
- Full extraction: n = 25
- Reduced extraction: n = 24
- Methodological foundation: n = 6
- Early stop: n = 0
- Total: n = 55

### 1D — Citation Relationships Within the Set (snowball sampling evidence)

From Section 15 (Quotable/Citable Points) or Section 6 (Citation Chain) in each note, identify any paper in the set that is explicitly cited by another paper in the set. These represent snowball/forward-citation discoveries.

Format as:
```
[Paper A] → cites → [Paper B in set]
```

This documents which papers were likely discovered through citation chasing rather than direct database search.

### 1E — Theme Distribution (search strand coverage)

From `papers/review-plan.md` Section 1 (Theme Gap Analysis), extract the Yes/Partial/No counts per theme. These demonstrate that the search was broad enough to cover all 8 themes.

### 1F — Year Cutoffs by Theme

Note whether any theme is dominated by recent papers (suggesting a time-bounded search) or spans the full date range.

---

## Step 2: Produce the Document

Using all extracted information plus the user-supplied items below, write `papers/search-methodology.md` with this structure:

---

### Document Structure

```markdown
# Literature Search Methodology

**Dissertation**: A Graduated Safety-State-Gated Architecture for AI Decision Support
in Low-Resource Environments: Design and Socio-Technical Evaluation in Coastal Fisheries

**Candidate**: Iskandar
**Date of last search**: [from notes — latest paper year/publication date]
**Total papers included**: 55

---

## 1. Research Questions Driving the Search

[Map each of RQ1–RQ5 to the search strands it motivated. Use the definitions from
`docs/research-alignment-table.md`.]

## 2. Search Strands and Keywords

Four search strands were used, each targeting a distinct research question cluster:

**Strand 1 — AI Safety Governance and Hybrid AI Architecture** (RQ1, RQ2)
Keywords: "AI governance", "safety governance", "graduated governance", "hybrid AI",
"safety-critical AI", "runtime enforcement", "AI participation", "advisory scope",
"safety shield", "guardrail", "formal verification", "decision architecture"

**Strand 2 — Formal Methods and Safety Properties** (RQ2)
Keywords: "formal methods", "safety properties", "Safety Dominance", "reachability analysis",
"control barrier function", "verified AI", "safe reinforcement learning",
"environmental state classification"

**Strand 3 — Low-Resource Environments and Fisheries Domain** (RQ3)
Keywords: "fisheries AI", "maritime AI", "coastal fishing", "low-resource AI",
"resource-constrained", "edge AI", "offline AI", "decision support fisheries",
"small-scale fisheries"

**Strand 4 — Trust, Evaluation, and Human Factors** (RQ4, RQ5)
Keywords: "trust in automation", "trust calibration", "levels of automation",
"graduated automation", "human factors AI", "socio-technical evaluation",
"automation mode confusion", "AI decision support evaluation"

## 3. Databases and Sources Searched

[Fill with venue distribution from Step 1A. List databases inferred from venues,
with paper counts per database category.]

## 4. Inclusion Criteria

| Criterion | Specification |
|---|---|
| Language | English only |
| Date range | [from Step 1B — earliest to latest year] |
| Publication type | Peer-reviewed articles, conference papers, arXiv preprints |
| Relevance | Addresses at least one of 8 core themes (T1–T8) |
| Content | Safety-critical AI, AI governance, hybrid AI, formal decision models,
low-resource deployment, fisheries/maritime AI, human role in AI decisions,
or socio-technical evaluation of AI systems |

## 5. Exclusion Criteria

| Criterion | Specification |
|---|---|
| Language | Non-English |
| Duplicates | Same paper found in multiple databases or sources |
| Scope | No relation to AI governance, safety-critical systems, or any of 8 themes |
| Accessibility | Full text unavailable |
| Domain-only | Fisheries/maritime papers with no AI or governance component |

## 6. Screening and Extraction Process

**Stage 1 — Title and Abstract Screening**
Titles and abstracts were reviewed against the 8 core themes and inclusion/exclusion
criteria. Papers with any relevance to safety-critical AI, hybrid AI, AI governance,
or fisheries/maritime AI were retained for full-text review.

**Stage 2 — Full-Text Screening and Relevance Gate**
Full texts were reviewed using a structured extraction template
(`methodologies/extraction-prompt-methodological.md` for methodology papers;
`.claude/prompts/paper_extraction_prompt.md` for architectural papers).
An early relevance check (hard stop) was applied: papers scoring ⭐ Minimal were excluded.
A mid-extraction relevance gate determined extraction depth:
- ≥ 3 Yes ratings → Full extraction (17 sections): 25 papers
- 1–2 Yes or ≥ 2 Partial → Reduced extraction (7 sections): 24 papers
- 0 Yes and ≤ 1 Partial → Early stop: 0 papers

**Methodological Foundation Papers** (6 papers)
Added in a second phase using a separate extraction prompt
(`methodologies/extraction-prompt-methodological.md`) targeting trust, levels of
automation, and socio-technical evaluation literature for PS4/PS5 evaluation design.

## 7. Additional Search Methods

**Backward snowball sampling**
Reference lists of key papers were scanned for additional relevant works.
[List citation relationships from Step 1D — papers discovered through snowball sampling.]

**Forward citation chasing**
Citing papers of core comparators (Flehmig et al., Shields/Könighofer, Dalrymple et al.,
Baxi) were checked for relevant extensions.

**Expert recommendation**
[Note any papers added on supervisor or examiner recommendation — e.g., trust papers
added following examiner feedback in review-comments/comments-1.md.]

## 8. PRISMA Flow Diagram

[Fill PRISMA numbers. The included count is known (55). Work backwards with estimates
for identified/screened/excluded. Use "(estimated)" where exact counts are unavailable.]

\`\`\`
IDENTIFICATION
Records identified through database searching (n = estimated)
  + Additional records from snowball/expert recommendation (n = [from Step 1D count])

SCREENING
Records after duplicates removed (n = estimated)
Records screened at title/abstract (n = estimated)
  Records excluded (n = estimated)

ELIGIBILITY
Full-text records assessed (n = estimated)
  Full-text excluded — out of scope (n = estimated)
  Full-text excluded — inaccessible (n = estimated)
  Full-text excluded — early stop (n = 0)

INCLUDED
Studies included (n = 55)
  Full extraction: n = 25
  Reduced extraction: n = 24
  Methodological foundation: n = 6
\`\`\`

## 9. Venue Distribution

[Table from Step 1A — databases inferred from venues, paper counts, example papers.]

## 10. Date Range and Coverage

[From Step 1B — year range, distribution chart, note on currency of literature.]

## 11. Search Limitations

1. **Date cutoff**: Papers published after [latest search date] not included.
2. **Language bias**: English-only — may miss work from Malaysia, Indonesia, or other fishing nations.
3. **Grey literature**: arXiv preprints included; unpublished technical reports excluded.
4. **Methodological papers added retrospectively**: The 6 trust/evaluation papers (50–55) were added in response to examiner feedback, not the initial search.
5. **Keyword sensitivity**: Search strings optimised for governance/safety framing; papers using different terminology (e.g., "autonomy levels" rather than "AI governance") may have been missed.
6. **Snowball incompleteness**: Backward snowball was limited to reference lists of core papers; full systematic backward snowball was not conducted.
```

---

## Step 3: Flag Items Requiring User Input

After generating the document, flag these items that cannot be derived from the notes:

```
USER INPUT REQUIRED:
□ Actual databases searched (confirm or correct the inferred list from Step 1A)
□ Actual search strings used (if recorded — otherwise the keyword clusters in Section 2 serve as a retrospective reconstruction)
□ Date(s) searches were conducted
□ Approximate number of records identified at database search stage (for PRISMA)
□ Approximate number excluded at title/abstract and full-text stages (for PRISMA)
□ Papers added on supervisor/examiner recommendation (specify which ones)
□ Any additional exclusion criteria applied
```

---

## Notes on PRISMA Completeness

A fully PRISMA-compliant flow requires exact counts at each stage. Since exact pre-screening counts may not have been recorded, the document should:

1. State exact counts where known (55 included; 25 full, 24 reduced, 6 methodological)
2. Use "(estimated)" for counts reconstructed from memory
3. Include a transparency note: *"This review followed a semi-systematic search protocol. Exact counts at identification and screening stages are estimated retrospectively; future updates should record these prospectively."*

This is acceptable for a PhD literature review — the key requirement is transparency, not perfect record-keeping.
