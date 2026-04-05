# Plan Review

Analyse all extracted papers to identify theme coverage gaps, map coverage against research objectives and formal components, and produce a structured literature review outline.

---

## Usage

```
/plan-review
```

No arguments. Analyses all extracted papers in `notes/`.

---

## Step 1: Gather all extracted notes

List and read all `.md` files in `notes/`:

```bash
ls notes/*.md
```

Read each file. Include papers from all extraction paths:

- **Full extraction** (all 17 sections) — use all sections
- **Reduced extraction** (Sections 1–7, 12–13, 16–17) — use available sections
- **Early stop** (Paper Identity + exclusion reason only) — count but exclude from detailed analysis

**Skip** any file that does not contain at least Section 3 (Relevance to My Research). These have insufficient data for gap analysis.

Report:
- How many papers were found (total)
- How many are full extraction, reduced extraction, early stop
- How many were skipped (insufficient data)

If no usable papers are found, stop and report: "No extracted papers with relevance data found in notes/. Run /extract-paper first."

---

## Step 2: Read the reference documents

Read these files to establish the analysis framework:

1. `.claude/prompts/paper_extraction_prompt.md` — 8 research themes
2. `new doc/research-alignment-table.md` — 5 problem statements (PS1–PS5), research gaps, research questions (RQ1–RQ5), and objectives (O1–O5)
3. `new doc/traceability-table.md` — formal component traceability (Table 1), objective-to-architecture mapping (Table 2), problem-to-gap-to-architecture mapping (Table 3)

### 8 Research Themes (from extraction prompt)

1. Hybrid AI (deterministic rule-based + probabilistic AI reasoning)
2. Safety-critical AI decision systems
3. AI governance — controlling *when* AI participates (Level 1) and *what* AI may recommend (Level 2)
4. Low-resource environments (limited data, connectivity, computing)
5. Decision architecture formalisation (E, S = f(E), G(S), A_AI(S), Safety Dominance Property)
6. Human role in AI-assisted decision-making
7. Socio-technical evaluation of AI systems
8. Coastal fisheries as a safety-critical, low-resource domain

### 5 Problem Statements (from alignment table)

- **PS1**: No architecture formally defines an intermediate AI participation mode with restricted recommendation space
- **PS2**: No architecture classifies environmental conditions into safety states that determine AI recommendation scope via (G(S), A_AI(S))
- **PS3**: No safety governance architecture designed for low-resource fisheries environments
- **PS4**: No comparative evaluation of graduated two-level governance vs binary governance
- **PS5**: No socio-technical evaluation of graduated AI governance, particularly user response to CAUTION mode

### Key Formal Components (from traceability table)

- E = {w, r, m, o, v, t}
- S = f(E) → {SAFE, CAUTION, UNSAFE}
- G(S) — participation gate (Level 1)
- A_AI(S) — admissible recommendation space (Level 2)
- R = {Go, Delay, DepartureTime, Duration}
- A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅
- Two-level governance pair: (G(S), A_AI(S))
- Safety Dominance Property: AI(E) ⊆ A_AI(S)

---

## Step 3: Theme Gap Analysis

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

## Step 4: Problem Statement Coverage Analysis

For each of the 5 problem statements (PS1–PS5), assess whether the extracted papers collectively provide sufficient literature to:
- **Establish that the gap exists** (papers that come close but fall short)
- **Provide comparators** (papers that implement partial solutions, closest prior art)
- **Motivate the research** (papers that demonstrate the need)

For each PS, produce:

### PS<n>: <Problem statement summary>

**Coverage**: <Well-Supported / Partially Supported / Unsupported>

| Paper | Role | How it relates |
|-------|------|----------------|
| <Paper Title> | Establishes gap / Comparator / Motivates | <Brief explanation> |

**Assessment**: Can this problem statement be convincingly argued in the literature review with the current papers?

**If Unsupported or Partially Supported**:
- What specific type of paper is needed?
- Which comparators from the alignment table are missing from the extracted set? (e.g., Flehmig et al., Shamsujjoha et al., Liu et al.)

---

## Step 5: Governance Level Analysis

Using Section 7 (Governance Level Analysis) from all extracted notes, produce a summary of how papers distribute across governance levels:

| Paper | Level 1 (G(S)) | Level 2 (A_AI(S)) | Unified + State-conditioned | Governance type |
|-------|-----------------|--------------------|-----------------------------|-----------------|
| <Title> | Yes/Partial/No | Yes/Partial/No | Yes/Partial/No | Binary / Graduated / None |

**Summary**:
- How many papers implement Level 1 only (binary gate)?
- How many implement any form of Level 2 (advisory scope control)?
- How many implement Level 2 that is state-conditioned (varies by classified safety state)?
- How many implement both levels unified in a governance pair (G(S), A_AI(S))?

This directly maps to the core contribution gap: if no paper implements unified state-conditioned two-level governance, the gap is confirmed by the literature.

---

## Step 6: Formal Component Coverage

Using Section 5 (Formal Model) from all extracted notes, check whether any paper addresses the formal components from the traceability table:

| Formal Component | Papers that address it | Papers that come close | Gap? |
|---|---|---|---|
| Environmental state vector E | ... | ... | Yes/No |
| Safety state classification S = f(E) | ... | ... | Yes/No |
| Participation gate G(S) | ... | ... | Yes/No |
| Admissible recommendation space A_AI(S) | ... | ... | Yes/No |
| Containment: A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ ∅ | ... | ... | Yes/No |
| Two-level governance pair (G(S), A_AI(S)) | ... | ... | Yes/No |
| Safety Dominance Property: AI(E) ⊆ A_AI(S) | ... | ... | Yes/No |

**Assessment**: Which formal components have comparators in the literature, and which represent novel contributions with no direct precedent?

---

## Step 7: Literature Review Outline

Based on the gap analyses (Steps 3–6), organise the extracted papers into a structured narrative:

### A. Argumentative Chain

Build the literature review's logical argument as an explicit chain. Each link is a claim supported by papers, and each transition reveals a gap the next link addresses:

```
1. Safety-critical systems increasingly use AI (background)
   ↓ but AI in safety-critical contexts needs governance
2. Hybrid AI architectures combine rule-based + probabilistic reasoning
   ↓ but the boundary between deterministic and AI control must be governed
3. Existing governance is binary: AI on/off (Level 1 — participation governance)
   ↓ shields, gatekeepers, supervision functions all implement G(S) = {0,1}
4. Some systems restrict AI output scope (Level 2 — advisory scope governance)
   ↓ guardrails, runtime enforcement, output filtering constrain what AI produces
   ↓ but these are static or per-action, not conditioned on classified environmental state
5. No architecture unifies both levels conditioned on environmental safety state
   ↓ Flehmig et al. is closest: three-level traffic-light, but governs monitoring intensity
   ↓ triggered by AI performance, not environmental state; single governance level
6. No formal Safety Dominance Property defined for graduated (non-binary) governance
   ↓ formal safety properties exist (shields, safe RL) but only for binary gate
7. This gap matters especially in low-resource, safety-critical domains
   ↓ fisheries: no formal safety governance; data-deficient; intermittent connectivity
8. No evaluation compares graduated two-level governance against binary governance
   ↓ existing evaluations compare gated vs ungated, not two-level vs one-level
9. No socio-technical evaluation of user response to CAUTION mode
   ↓ users have never encountered "AI active but restricted" as distinct from "AI fully on"
```

For each link, list:
- The papers that support the claim
- The transition sentence that reveals the gap leading to the next link
- Which problem statement (PS1–PS5) the link maps to

### B. Citation Chain

Map the intellectual lineage by tracing citation relationships among the extracted papers. This shows how ideas flow through the literature and where the user's contribution enters the conversation.

For each key paper cluster, trace:

```
[Foundational paper] → cited by → [Extension paper] → cited by → [Recent paper]
                                                                       ↓
                                                          [Gap: what none of them do]
                                                                       ↓
                                                          [User's contribution fills this]
```

Identify and map these citation clusters:

1. **Safety governance cluster**: Which papers cite each other on AI safety mechanisms (shields, guardrails, safety frameworks)?
2. **Hybrid AI cluster**: Which papers cite each other on combining rule-based and probabilistic AI?
3. **Fisheries/maritime cluster**: Which papers cite each other on AI in fisheries or maritime domains?
4. **Formal methods cluster**: Which papers cite each other on formal models for safety-critical AI?

For each cluster, produce:

| Paper | Cites | Cited by (in our set) | Governance level | Gap relative to user's work |
|-------|-------|----------------------|------------------|----------------------------|
| ... | ... | ... | Level 1 / Level 2 / Both | ... |

**How to determine citations**: Check Section 2 (Core Contribution) and Section 16 (Positioning) of each notes file for references to other papers in the extracted set. Also check if the paper's key references (mentioned in the notes) match titles of other papers in the tracker.

**Citation chain output**:
- A visual lineage showing which papers build on which
- Where the lineage breaks (no paper in the set extends the idea further) — these are entry points for the user's contribution
- Which papers are foundational (cited by many), which are recent extensions (cite many), and which are isolated (no citation links in the set)

### C. Suggested Structure

Propose a literature review outline with:

1. **Section groupings**: Group papers by theme or conceptual progression, aligned with the argumentative chain (links 1–9 above). Each section should have a clear purpose (e.g., "Domain Background", "Safety-Critical AI Systems", "Hybrid AI Architectures", "AI Governance Mechanisms — Level 1", "AI Governance Mechanisms — Level 2", "The Two-Level Governance Gap", "Low-Resource Deployment", "Evaluation Gap").

2. **Paper placement**: For each section, list which papers belong there and their role:
   - **Supports motivation**: Paper establishes why the research problem matters
   - **Fills background**: Paper provides necessary context or definitions
   - **Represents baseline/comparator**: Paper represents an approach the research compares against (map to specific PS or comparator from alignment table)
   - **Highlights gap**: Paper demonstrates what is missing that the research addresses

3. **Flow and transitions**: For each section transition, use the argumentative chain's transition sentences. Each section should end by revealing the gap that motivates the next section.

4. **Citation integration**: For each section, note which citation cluster(s) it draws from and how the citation chain supports the argumentative flow. Papers that cite each other should appear in the same or adjacent sections.

5. **Positioning summary**: One paragraph explaining how the collected literature positions the two-level governance contribution — what is well-established (Level 1 governance), what exists separately (Level 2 governance in guardrails), and what gap remains (unified state-conditioned (G(S), A_AI(S)) pair). Reference both the argumentative chain (logical argument) and citation chain (intellectual lineage) to show that the gap is real and unfilled.

---

## Step 8: Save output

Save the complete analysis to:

```
papers/review-plan.md
```

The file should contain:
1. Header with date and number of papers analysed (by extraction path)
2. Theme gap analysis (all 8 themes) — Step 3
3. Problem statement coverage — Step 4
4. Governance level summary — Step 5
5. Formal component coverage — Step 6
6. Argumentative chain (with papers mapped to each link) — Step 7A
7. Citation chain (clusters, lineage, entry points) — Step 7B
8. Literature review outline (section groupings, paper placement, flow) — Step 7C
9. Coverage summary tables

Format the theme coverage summary as:

| Theme | Coverage | Papers (Yes) | Papers (Partial) | Papers (No) |
|-------|----------|--------------|-------------------|-------------|
| ... | ... | ... | ... | ... |

Format the problem statement coverage summary as:

| Problem Statement | Coverage | Comparators found | Key gaps |
|---|---|---|---|
| PS1 | ... | ... | ... |
| PS2 | ... | ... | ... |
| PS3 | ... | ... | ... |
| PS4 | ... | ... | ... |
| PS5 | ... | ... | ... |

This file is overwritten each time `/plan-review` is run.

---

## Step 9: Report summary

Report to the user:
- Total papers analysed (by extraction path)
- Theme coverage summary: which themes are well-covered, partially covered, or gaps
- Problem statement coverage: which PS are well-supported vs unsupported
- Governance level finding: how many papers implement Level 1 only vs Level 2 vs both
- Formal component gaps: which components have no precedent in the literature
- Argumentative chain: how many of the 9 links are well-supported by papers, and where the argument is weakest
- Citation chain: key clusters identified, where the user's work enters the lineage, any foundational papers missing from the set
- Top 3 priorities for additional papers
- The file was saved to `papers/review-plan.md`
