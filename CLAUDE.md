# Project Instructions

---

## Research Context and Identity

**Read this section first in every session before doing any work on this project.**

### What this research is

**Title:** *A Graduated Safety-State-Gated Architecture for AI Decision Support in Low-Resource Environments: Design and Comparative Evaluation in Coastal Fisheries*

**Core CS contribution:** A two-level AI governance architecture — the governance pair **(G(S), A_AI(S))** — that formally constrains both whether AI participates and what AI is permitted to recommend, conditioned on classified environmental safety state. This produces a novel intermediate CAUTION mode where AI participates within a formally restricted advisory scope, which no existing architecture implements.

**Formal pipeline:**

```
E → S = f(E) → (G(S), A_AI(S)) → AI(E) → Human Decision
```

**The three safety states and their governance configurations:**

| State | G(S) | A_AI(S) | AI scope |
|---|---|---|---|
| SAFE | 1 (enabled) | {Go, Delay, DepartureTime, Duration} | Full |
| CAUTION | 1 (enabled) | {Go, Delay} | Restricted |
| UNSAFE | 0 (disabled) | ∅ | None |

**The formal containment property:** A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅

**The Safety Dominance Property:** For all E, AI(E) ⊆ A_AI(S) — the AI can only generate recommendations within the admissible space defined by the current safety state.

**Domain:** Small-scale coastal fisheries in Malaysia (Terengganu, Penang). The departure decision problem — whether a fisher should go to sea given current environmental conditions — is the application context. The domain motivates and validates the architecture; it is not the research contribution.

---

### Research Positioning — CS First

**This is a computer science thesis.** The primary contribution is the formal governance architecture (RQ1, RQ2). Do not drift the framing toward socio-technical systems theory or treat socio-technical evaluation as a co-equal contribution.

**Role of each research question:**

| RQ | Role | Status |
|---|---|---|
| RQ1 | Architecture design — the three-mode graduated governance structure | Primary CS contribution |
| RQ2 | Formal specification — E, S = f(E), G(S), A_AI(S), Safety Dominance Property | Primary CS contribution |
| RQ3 | Prototype implementation — low-resource coastal fisheries deployment | Implementation |
| RQ4 | Technical validation — three-condition comparison (ungated vs. binary-gated vs. two-level graduated) | Technical evaluation |
| RQ5 | Contextual validation — user study with fishers across three safety states | Contextual evaluation, not a primary contribution |

**RQ5 is evaluation, not contribution.** It tests whether the architecture works with real users. It does not define a new theoretical strand. Socio-technical literature (Flehmig et al. 2025 STA variable, Rasmussen 1997, Zarei 2024) may appear in the discussion of RQ5 results as an interpretive lens — not in Chapter 2 or the methodology as a primary framework.

---

### The Gap Argument — Four-Layer Structure

The research gap is established by four independent sources, each confirming the same absence from a different body of literature:

1. **The problem statement** — no existing architecture restricts AI advisory scope (A_AI(S)) based on classified environmental safety state. Existing systems are binary: AI fully on or fully off.
2. **Indykov et al. (2025)** — after surveying 206 papers and 16 architectural tactics for ML-enabled systems, AT11 (rule-based models) → Safety = 0 (no demonstrated formal impact on Safety). The gap persists across the broader ML systems architecture literature.
3. **Dalrymple et al. (2024)** — Guaranteed Safe AI is the theoretical umbrella. The proposed architecture is a domain-specific, state-conditioned instantiation of GS principles. GS AI is binary at the verification level (no CAUTION analogue). The proposed architecture fills this with (G(S), A_AI(S)).
4. **Flehmig et al. (2024)** — closest structural precedent. Their traffic-light degradation index has three levels but the intermediate level (Orange) governs supervisory behaviour, not AI advisory scope. The AI gives identical full-scope output at Level 1 and Level 2. This is the most precise available evidence that the CAUTION mode gap is real.

---

### Canonical Documents Map

Always go to the right document — do not reconstruct content that already exists.

| Document | Role |
|---|---|
| `docs/appendix-c-formalisation.md` | **Single source of truth** for all formal variable definitions and governance properties |
| `docs/architecture-illustration.md` | Full architecture walkthrough — layers, governance table, scenario, limitations |
| `docs/discussion-notes-governance-gap-precedents-and-formal-foundations.md` | The four-layer gap argument; comparisons with Indykov, Dalrymple, Flehmig (2024) |
| `docs/research-alignment-table.md` | RQ → Objective → Methodology traceability; the novelty thread |
| `docs/chapter-2-draft.md` | Literature review draft — Sections 2.1–2.9 with bridge paragraph to Chapter 3 |
| `docs/citation-notes-map.md` | Master citation → notes file mapping for all corpus papers |
| `docs/justification-layer3-enforcement.md` | Layer 3 decision (rule-based engine), enforcement mechanism, and proof by construction of Safety Dominance Property |
| `docs/evaluation-design-rq4.md` | RQ4 three-condition comparative evaluation design — scenarios, metrics, and C1 vs C2 discriminator logic |
| `docs/rq5-study-design.md` | RQ5 contextual validation study design — three questions, instrument, participants, scope exclusions |
| `docs/research-improvement-plan.md` | Six-step improvement plan produced 25 April 2026 — all steps completed |
| `docs/justification-*.md` | Justification documents for specific design decisions |
| `notes/` | Per-paper extraction notes for all 63 corpus papers |

---

### Layer 3 Specification — Resolved

**Layer 3 is a rule-based engine.** The Safety Dominance Property (AI(E) ⊆ A_AI(S)) is enforced by construction: the governance layer (Layer 2) supplies a rule set RS(S) to Layer 3 before any reasoning begins. RS(CAUTION) contains only rules producing {Go, Delay} — no rule in that configuration can produce DepartureTime or Duration. The property holds by definition of the rule sets, not by runtime filtering.

- Full justification: `docs/justification-layer3-enforcement.md`
- Proof by construction: `docs/appendix-c-formalisation.md` Section C.7.2
- Architecture update: `docs/architecture-illustration.md` Layer 3 and Section 2

**The Safety Dominance Property now holds by implementation, not only by design intent.**

---

### What NOT to Do in This Project

- Do not introduce socio-technical systems theory (Rasmussen, Zarei, STA variable) as a primary theoretical framework — it belongs only in RQ5 discussion.
- Do not treat Flehmig et al. (2025) "The Missing Variable" as a core corpus paper unless actively working on the RQ5 evaluation chapter.
- Do not redefine formal variables without updating `docs/appendix-c-formalisation.md` first.
- Do not frame the research as a socio-technical study with a CS component — it is a CS architecture thesis with a contextual evaluation component.
- Do not treat RQ5 as a co-equal contribution to RQ1/RQ2 in any framing, abstract, or introduction.

---

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
