# Review Protocol (canonical source of truth)

**Date:** 2026-09-07
**Role:** Single source of truth for all Search and Selection Protocol figures. The table in the top section below is the reviewer-facing deliverable; every cell traces to a §-section further down. Do NOT edit downstream artefacts (manuscript, chapter, CLAUDE.md, citation map) without updating the relevant §-section here first.

**Provenance note.** Where the elicitation could not recover a value at drafting time, the §-section either quotes the corresponding passage from an existing project artefact (with source line) or carries the literal string `Not recorded — disclosed as limitation`. Elements sourced from artefacts remain subject to user confirmation and may be amended.

## Search and Selection Protocol (table)

<!-- FILLED IN TASK 2 -->

---

## Databases

Sourced from `manuscript-v3.md:107` — the four databases named in the current Methodology paragraph.

- Scopus
- IEEE Xplore
- Web of Science
- ACM Digital Library

## Dates

- Search executed: Not recorded — disclosed as limitation
- Publication window (inclusion filter): No pre-specified filter was applied. Observed range across the mapped corpus (n = 111 rows in `citation-notes-map.md` on 2026-09-07): 2023–2026 for the bulk (108 papers), with three older references retained as foundational sources (2015, 2017, 2022 — each on domain-specific empirical grounds rather than governance architecture).

## Search string families

Sourced from `manuscript-v3.md:107`. If verbatim query strings were retained elsewhere, this section should be replaced with them.

- Primary: AI governance; runtime assurance; safety filters; decision support; autonomy levels; guardrails
- Secondary: fisheries AI; low-resource deployment

## Screening counts

| Stage | N |
|---|---|
| Initial records returned | Not recorded — disclosed as limitation |
| After duplicate removal | Not recorded — disclosed as limitation |
| After title/abstract screening | Not recorded — disclosed as limitation |
| Retained for full-text review | 72 |
| Final corpus | 72 |

The v6 archive at `ipsci-2026-paper-v6.md:51,95` corroborates the final figure of 72 papers retained for full review. Intermediate screening counts (initial, post-dedup, post-title/abstract) were not archived at the time of review and are disclosed as limitations rather than reconstructed.

## Inclusion criteria

Sourced from `ipsci-2026-paper-v6.md:51`. Two-stage screening; a paper was included at the title-and-abstract stage if it met at least one of the following:

1. Addressed a mechanism that constrains or shapes AI behaviour during operation.
2. Targeted a safety-critical or human-in-the-loop context.
3. Addressed AI deployment in low-resource or resource-constrained environments.

## Exclusion criteria

Sourced from `ipsci-2026-paper-v6.md:51`. A paper was excluded if it:

1. Dealt only with training-time, fine-tuning, or static-configuration approaches with no runtime governance component.

## Snowballing

Sourced from `ipsci-2026-paper-v6.md:47`. Papers were added through citation tracing off the initial database search until no new governance mechanisms emerged. Seed set was the initial pool retrieved from the four databases plus the three anchor systematic reviews listed in §Anchor systematic reviews. Specific seed-paper list not archived.

## Anchor systematic reviews (secondary evidence)

Sourced from `manuscript-v3.md:107` — not from the elicitation. These are the three large-scale systematic reviews retained as secondary evidence supporting the four-body absence claim.

- Indykov et al. — 206 papers, 16 architectural tactics
- Shamsujjoha et al. — 13 guardrail actions across 32 agent studies
- Perez-Cerrolaza et al. — 294 references

Total: 532 secondary references.

## Coding

- Reviewers: Single reviewer (the thesis author). The thesis is single-authored (git author: iskandar); no second coder participated.
- Dimensions: Primary governance target · Runtime adaptation · Conditioning variable · Recommendation restriction (see `manuscript-v3.md` TABLE I).
- Dual-coding audit: Not performed. Disclosed as a limitation.
- Ambiguity adjudication: The "Partial" rating in Table 2.1 (thesis Chapter 2) and TABLE I (manuscript-v3) was assigned when a paper addressed a governance dimension incompletely. The rule is documented in the column-definitions footnote to Table 2.1 (`docs/chapters/chapter-2-literature-review/v1-initial-draft.md:107`): "'Partial' indicates the system addresses the dimension incompletely, e.g., participation control without formal specification (L1 Partial), design-time configuration only (Formal Model Partial), or governance without environmental state conditioning (Unified Governance Partial)."

## Limitations (unrecorded elements)

- Search execution date(s) were not archived.
- No pre-specified publication-year filter was applied. The observed range (2023–2026 for the bulk; three older foundational references) reflects the retained corpus, not a policy.
- Initial records returned, post-duplicate count, and post-title/abstract count were not archived; only the retained corpus size (n = 72) is verifiable in artefacts.
- Coding was performed by a single reviewer (the thesis author). No dual-coding audit was performed on any sample; inter-rater reliability is therefore not available.

## Corpus reconciliation (open — not resolved in this plan)

- **72** = final full-text-reviewed corpus (manuscript claim; used in the table).
- **111** = data rows in `citation-notes-map.md` as of 2026-09-06.
- **112** = `.md` files in `notes/` as of 2026-09-06.
- **63** = stale figure in `CLAUDE.md:82,137` as of 2026-09-06.
- Reconciliation of these four numbers is deferred to a follow-up task. If that reconciliation concludes n ≠ 72, the table row `Final corpus | 72` and every downstream artefact quoting 72 must re-issue.
