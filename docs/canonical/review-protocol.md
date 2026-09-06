# Review Protocol (canonical source of truth)

**Date:** 2026-09-07
**Role:** Single source of truth for the Search and Selection Protocol figures (Table 1) and the primary comparator inclusion rationale (Table 2). Both tables are the reviewer-facing deliverables; every Table 1 cell traces to a §-section further down. Do NOT edit downstream artefacts (manuscript, chapter, CLAUDE.md, citation map) without updating the relevant §-section here first.

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

## Comparator inclusion rationale (table)

**Table 2. Primary comparator inclusion rationale (18 systems from Chapter 2 Table 2.1).**

| Paper | Role | Inclusion rationale |
|---|---|---|
| Abella et al. (2025) — SAFEXPLAIN [[notes]](../../notes/SAFEXPLAIN-%20a%20Complete%20Approach%20Towards%20Trustworthy%20AI-Based%20Safety-Critical%20Systems.md) | Safety envelope + fallback (L1) | EU-project reference implementation of envelope-based binary switching with a non-AI fallback subsystem; comparator for the "AI operates within predefined envelope or is replaced" pattern in automotive/space contexts. |
| Bajcsy & Fisac (2024) [[notes]](../../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md) | Safety filter (L1 binary) | Formalises the Human-AI Safety Filter as a control-theoretic mechanism that overrides AI output when it crosses a safety threshold; establishes the sophistication ceiling of Level-1 participation control. |
| Banerjee et al. (2025) — CRANE [[notes]](../../notes/CRANE-%20Reasoning%20with%20Constrained%20LLM%20Generation.md) | Grammar constraint (formal analogue) | Structural precursor: augmented grammar G_a = R_M·G produces an output-set containment relationship formally analogous to A_AI(CAUTION) ⊂ A_AI(SAFE); alternation is syntactically triggered rather than state-conditioned. The closest formal analogue to A_AI containment in the corpus. |
| Baxi (2026) — CGAE [[notes]](../../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) | Nested permission tiers (adaptive) | Structurally nearest formal comparator with nested permission sets E(T_k) ⊂ E(T_{k+1}); tier conditions on verified agent robustness, not on environmental state — establishes that the conditioning-variable distinction is the actual gap, not the containment structure. |
| Chen, Kang & Li (2025) — SHIELDAGENT [[notes]](../../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md) | Policy-based agent shield (L2 static) | LTL rule extraction from policy documents + formal verification of each planned agent action; comparator for policy-driven per-action validation that does not condition on environmental state. |
| Corsi et al. (2024) [[notes]](../../notes/Verification-Guided%20Shielding%20for%20Deep%20Reinforcement%20Learning.md) | Verification-guided shield (L1 refined) | Refined binary shield using formal DNN verification to partition the input space into provably safe and potentially unsafe regions (25–71% overhead reduction); comparator for the claim that even sophisticated shield refinements retain binary character. |
| Dalrymple et al. (2024) — GS AI [[notes]](../../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md) | Theoretical framework | Guaranteed Safe AI is the theoretical umbrella the proposed architecture instantiates; included as the closest theoretical precedent and to establish that GS AI is binary at the verification level with no CAUTION analogue. |
| Feng, McDonald & Zhang (2025) [[notes]](../../notes/Levels%20of%20Autonomy%20for%20AI%20Agents.md) | Authority allocation (design-time) | Most conceptually granular authority-allocation framework — two governance dimensions (agency, autonomy) plus autonomy certificates — both configured at design time; reveals that advisory-scope restriction is a missing third governance lever. |
| Flehmig et al. (2024) [[notes]](../../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md) | Traffic-light degradation index (adaptive) | Closest structural precedent: three-level classification (green/orange/red) triggered by AI performance monitoring; intermediate level governs supervisory intensity, not advisory scope. Central to the F-15 empirical comparison showing a Flehmig-style C3 baseline diverges from a plain binary gate C1 in 0.00% of hours. |
| Gyllenhammar et al. (2025) [[notes]](../../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md) | ODD → ROD → MRC hierarchy (adaptive) | Three-level degradation hierarchy for automated driving; comparator for domain-confinement adaptation (narrows where the system operates, not what it recommends). |
| Hamel-De le Court, Belardinelli & Goodall (2025) [[notes]](../../notes/Probabilistic%20Shielding%20for%20Safe%20Reinforcement%20Learning.md) | Probabilistic shield (L1 stochastic) | Extends shielding to stochastic environments with two formal guarantees (Theorem 1: ≥ 1 − δ safety; Theorem 2: convergence preservation); comparator for the claim that probabilistic formulation does not change the binary character of the intervention. |
| Könighofer et al. (2025) [[notes]](../../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md) | Shield formalism (L1 canonical) | Formalises shields synthesised from LTL safety specifications and environment models; provides the reference implementation of a Level-1 binary gate against which the proposed architecture is contrasted. |
| Kwon et al. (2025) [[notes]](../../notes/Runtime%20Safety%20through%20Adaptive%20Shielding-%20From%20Hidden%20Parameter%20Inference%20to%20Provable%20Guarantees.md) | Adaptive shielding with hidden-parameter inference | Closest near-miss: environment-centric features E ∈ ℝ^n₂ as governance input, runtime adaptation, formal safety guarantee (Theorem 1); but SafetyScore remains binary and adaptation is quantitative (ACP threshold Γ_t) rather than qualitative governance-mode change. Retained to preclude the "you missed the environment-input case" objection. |
| Odriozola-Olalde et al. (2023) [[notes]](../../notes/Shielded%20Reinforcement%20Learning-%20A%20review%20of%20reactive%20methods%20for%20safe%20learning.md) | Shielded-RL SLR (anchor-adjacent) | SLR classifying methods into three Safety Levels — all binary per-action gates; establishes that "graduated" in shielded RL refers to implementation-tier gradation, not advisory-scope gradation. |
| Perez-Cerrolaza et al. (2024) [[notes]](../../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) | Cross-domain safety survey (anchor SLR) | Anchor SLR (294 references) classifying AI safety compliance into three classes without an intermediate advisory-scope tier; establishes binary participation governance across industrial and transportation domains. |
| Ramos et al. (2024) [[notes]](../../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md) | 91-paper SLR (anchor) | Anchor SLR (91 papers, 6 industries) confirming binary governance is universal across collaborative-intelligence systems; refutes the possibility that an unnoticed state-conditioned mechanism exists in that literature. |
| Shamsujjoha et al. (2025) [[notes]](../../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md) | Multi-layered guardrail taxonomy (L2 static) | Definitive multi-layered guardrail taxonomy (13 action types across 14 pipeline targets); the most comprehensive Level-2 (output-restriction) comparator and the reference source for the claim that no reviewed guardrail conditions on classified environmental state. |
| Wang et al. (2026) — AgentSpec [[notes]](../../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md) | Runtime enforcement DSL (L2 static) | Domain-specific language for structured trigger–predicate–action rules over LLM agents (prevents 90%+ of unsafe code executions); illustrates the state-of-the-art in per-action runtime enforcement and its invariance to environmental conditions. |

The 18 rows are the comparator set from Chapter 2 Table 2.1. Each entry was included on one of two grounds: it is the strongest available exemplar of a governance mechanism the proposed architecture is contrasted with (safety filter, shield, guardrail taxonomy, permission tier, degradation hierarchy, authority allocation), or it is a near-miss a reviewer would otherwise raise as counter-example (Baxi's nested-permission structure, Kwon's environment-conditioned adaptation, Flehmig's three-level index, Banerjee's grammar-containment analogue). Three anchor SLRs (Ramos, Perez-Cerrolaza, Odriozola-Olalde) sit inside the same set because the absence claim is only credible when confirmed across large-scale reviews of adjacent literature, not just within the primary comparators. No row is here on convenience; each carries a specific comparison load in the Chapter 2 argument.

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
