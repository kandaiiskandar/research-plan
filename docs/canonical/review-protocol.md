# Review Protocol (canonical source of truth)

**Date:** 2026-09-07
**Role:** Single source of truth for all Search and Selection Protocol figures. The table in the top section below is the reviewer-facing deliverable; every cell traces to a §-section further down. Do NOT edit downstream artefacts (manuscript, chapter, CLAUDE.md, citation map) without updating the relevant §-section here first.

**Provenance note.** Where the elicitation could not recover a value at drafting time, the §-section either quotes the corresponding passage from an existing project artefact (with source line) or carries the literal string `Not recorded — disclosed as limitation`. Elements sourced from artefacts remain subject to user confirmation and may be amended.

## Search and Selection Protocol (table)

**Table 1. Search and Selection Protocol.**

| Protocol element | Value |
|---|---|
| Databases | Scopus; IEEE Xplore; Web of Science; ACM Digital Library |
| Search executed | *Not recorded — disclosed as limitation* |
| Publication window | No pre-specified filter; observed range 2023–2026 for the bulk, with three older foundational references (2015, 2017, 2022) |
| Search string families (primary) | AI governance; runtime assurance; safety filters; decision support; autonomy levels; guardrails |
| Search string families (secondary) | fisheries AI; low-resource deployment |
| Inclusion criteria | Addresses a mechanism that constrains or shapes AI behaviour during operation; OR targets a safety-critical or human-in-the-loop context; OR addresses AI deployment in low-resource or resource-constrained environments |
| Exclusion criteria | Deals only with training-time, fine-tuning, or static-configuration approaches with no runtime governance component |
| Snowballing | Citation tracing off the initial database pool plus the three anchor systematic reviews, continued until no new governance mechanisms emerged; seed-paper list not archived |
| Screening flow (initial → dedup → title/abstract) | *Not recorded — reconstructed from the retained corpus; see §Limitations* |
| Retained for full-text review | 72 |
| Final corpus | 72 |
| Anchor systematic reviews (secondary evidence)ᵃ | Indykov et al. (2025) [[notes]](../../notes/Architectural%20tactics%20to%20achieve%20quality%20attributes%20of%20machine-learning-enabled%20systems-%20a%20systematic%20literature%20review.md) — 206 papers · Shamsujjoha et al. (2025) [[notes]](../../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md) — 32 agent studies · Perez-Cerrolaza et al. (2024) [[notes]](../../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) — 294 references. 532 refs total. |
| Coding — reviewers | Single reviewer (thesis author) |
| Coding — dual-coding audit | Not performed |
| Coding — ambiguity adjudication | "Partial" rating assigned when a paper addresses a governance dimension incompletely, per the column-definitions footnote to Table 2.1 of the thesis Chapter 2 |

ᵃ Sourced from `manuscript-v3.md:107`, not from the elicitation. See §Anchor systematic reviews.

The review is structured-purposive, not systematic. Scope covers the bodies of literature where an advisory-scope restriction mechanism could plausibly appear, and coding runs against the four fixed dimensions above rather than a full PRISMA protocol. Some elements were not archived at review time: search execution dates, the intermediate screening counts before the retained set was fixed, and any dual-coding audit. These are disclosed in §Limitations rather than reconstructed after the fact. Only the retained corpus of 72 papers is verifiable in artefacts.

**Live dependency.** The `Final corpus | 72` row depends on a deferred corpus-count reconciliation (see §Corpus reconciliation). If that reconciliation concludes n ≠ 72, the row and every downstream artefact quoting 72 re-issue.

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

- Indykov et al. (2025) [[notes]](../../notes/Architectural%20tactics%20to%20achieve%20quality%20attributes%20of%20machine-learning-enabled%20systems-%20a%20systematic%20literature%20review.md) — 206 papers, 16 architectural tactics
- Shamsujjoha et al. (2025) [[notes]](../../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md) — 13 guardrail actions across 32 agent studies
- Perez-Cerrolaza et al. (2024) [[notes]](../../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) — 294 references

Total: 532 secondary references.

## Coding

- Reviewers: Single reviewer (the thesis author). The thesis is single-authored (git author: iskandar); no second coder participated.
- Dimensions: Primary governance target · Runtime adaptation · Conditioning variable · Recommendation restriction (see `manuscript-v3.md` TABLE I).
- Dual-coding audit: Not performed. Disclosed as a limitation.
- Ambiguity adjudication: The "Partial" rating in Table 2.1 (thesis Chapter 2) and TABLE I (manuscript-v3) was assigned when a paper addressed a governance dimension incompletely. The rule is documented in the column-definitions footnote to Table 2.1 (`docs/chapters/chapter-2-literature-review/v1-initial-draft.md:107`): "'Partial' indicates the system addresses the dimension incompletely, e.g., participation control without formal specification (L1 Partial), design-time configuration only (Formal Model Partial), or governance without environmental state conditioning (Unified Governance Partial)."

## Limitations (unrecorded elements)

- Search execution dates were not archived.
- No publication-year filter was applied. The observed range (2023–2026 for the bulk, plus three older foundational references) reflects the retained corpus, not a policy.
- Initial records, post-duplicate count, and post-title-abstract count were not archived. Only the retained corpus size (n = 72) is verifiable in artefacts.
- Coding was performed by a single reviewer (the thesis author). No dual-coding audit was performed on any sample, so inter-rater reliability is not available.

## Corpus reconciliation (resolved 2026-09-07)

The four numbers count different populations. Each is correct at its own scope.

- **72** — Full-reviewed corpus at manuscript submission. The subset that "advanced to full review" per `manuscript-v3.md:107`, coded on the four dimensions in TABLE I. This remains the reviewer-facing figure and the value in Table 1 above. Do not change unless the manuscript is resubmitted with a new methodology.
- **111** — Current active corpus. The mapped rows in `citation-notes-map.md` as of 2026-09-07 — the thesis-level operational corpus that has grown since manuscript submission through added comparators and chapter drafting.
- **112** — `.md` files in `notes/` as of 2026-09-07. Equals the 111 active corpus plus one archived stub (`Agent Governance Toolkit- Runtime Security for Autonomous AI Agents.md`, superseded by OWASP Top 10 for Agentic Applications 2026; the stub file itself records the archival).
- **63** — Historical figure in `CLAUDE.md:82,137` that no longer reflected the corpus. Updated 2026-09-07 to reference 111 (active) and 72 (manuscript-facing).

Two filename typos in `citation-notes-map.md` were fixed as part of this reconciliation: the Newcomb & Ochoa row used `:` where the actual file uses `-`, and the Shaffril et al. row carried a trailing space before `.md` that the actual file does not have.

Because 72 is a properly-defined subset of the manuscript-time corpus rather than an out-of-date count, the `Final corpus | 72` row in Table 1 stands. The "Live dependency" note above Table 1 is retained as a historical marker; the dependency it warned about is now resolved.
