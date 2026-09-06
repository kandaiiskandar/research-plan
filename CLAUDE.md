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

**Domain:** Small-scale coastal fisheries in Malaysia (Kota Kinabalu, Sabah). The departure decision problem — whether a fisher should go to sea given current environmental conditions — is the application context. The domain motivates and validates the architecture; it is not the research contribution.

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
| `docs/canonical/session-log-2026-09-06.md` | **START HERE.** What was done on 2026-09-06, the fifteen findings, and the work queue. The three gating decisions (threshold, F-7 framing, headline figure) are all resolved |
| `docs/canonical/decision-record-empirical-first.md` | **Read before any domain-instantiation work.** Records the 2026-09-06 decision that site data now drives the classifier specification, not the reverse. Carries open questions **Q1–Q8** |
| `docs/canonical/empirical-findings-2026-09-06.md` | **Findings F-1 to F-15** from 5 years of site data. **F-15 answers Review 3's novelty objection: a Flehmig-style traffic-light baseline (C3) diverges from a plain binary gate (C1) in 0.00% of hours.** **§0a "Current reportable figures" is the authoritative list, generated by `scripts/canonical_figures.py` — do not hand-edit it.** Figures are reported in TWO configurations ("option C"): **PRIMARY** 5.00 yr / ERA5-Ocean 50 km and **RESOLUTION** 3.25 yr / MFWAM 8 km. Headline: **Level 2 binds 7.84% (primary) / 6.15% (resolution)**. 12.4%, 8.3% and lone-6.1% are superseded. **§0b records why the earlier table was wrong — read it before trusting any derived figure.** Also carries one claim that must be withdrawn (mode-chattering) |
| `docs/canonical/finding-met-hydrodynamic-gap.md` | **Source of truth for threshold provenance.** MET defines where Category 1 *ends* (3.5 m), never where it *begins* — so MET cannot supply the SAFE/CAUTION boundary. MET criteria sit 2.8–7× above the measured operability limits of actual Malaysian boats |
| `docs/canonical/data-provenance.md` | **Check before citing any empirical figure.** Where each variable actually comes from, at what resolution, and whether it is fit for the threshold it is compared against |
| `docs/canonical/appendix-c-formalisation.md` | **Single source of truth** for all formal variable definitions and governance properties |
| `docs/canonical/architecture-illustration.md` | Full architecture walkthrough — layers, governance table, scenario, limitations |
| `docs/canonical/discussion-notes-governance-gap-precedents-and-formal-foundations.md` | The four-layer gap argument; comparisons with Indykov, Dalrymple, Flehmig (2024) |
| `docs/canonical/research-alignment-table.md` | RQ → Objective → Methodology traceability; the novelty thread |
| `docs/chapters/chapter-2-literature-review/v1-initial-draft.md` | Literature review draft — Sections 2.1–2.9 with bridge paragraph to Chapter 3 |
| `docs/canonical/citation-notes-map.md` | Master citation → notes file mapping for all corpus papers |
| `docs/canonical/justification-layer3-enforcement.md` | Layer 3 decision (rule-based engine), enforcement mechanism, and proof by construction of Safety Dominance Property |
| `docs/canonical/evaluation-design-rq4.md` | RQ4 three-condition comparative evaluation design — scenarios, metrics, and C1 vs C2 discriminator logic |
| `docs/canonical/rq5-study-design.md` | RQ5 contextual validation study design — three questions, instrument, participants, scope exclusions |
| `docs/reference/research-improvement-plan.md` | Six-step improvement plan produced 25 April 2026 — all steps completed |
| `docs/justification/*.md` | Justification documents for specific design decisions |
| `notes/` | Per-paper extraction notes for all 63 corpus papers |

---

### Layer 3 Specification — Resolved

**Layer 3 is a rule-based engine.** The Safety Dominance Property (AI(E) ⊆ A_AI(S)) is enforced by construction: the governance layer (Layer 2) supplies a rule set RS(S) to Layer 3 before any reasoning begins. RS(CAUTION) contains only rules producing {Go, Delay} — no rule in that configuration can produce DepartureTime or Duration. The property holds by definition of the rule sets, not by runtime filtering.

- Full justification: `docs/canonical/justification-layer3-enforcement.md`
- Proof by construction: `docs/canonical/appendix-c-formalisation.md` Section C.7.2
- Architecture update: `docs/canonical/architecture-illustration.md` Layer 3 and Section 2

**The Safety Dominance Property now holds by implementation, not only by design intent.**

---

### What NOT to Do in This Project

- Do not introduce socio-technical systems theory (Rasmussen, Zarei, STA variable) as a primary theoretical framework — it belongs only in RQ5 discussion.
- Do not treat Flehmig et al. (2025) "The Missing Variable" as a core corpus paper unless actively working on the RQ5 evaluation chapter.
- Do not redefine formal variables without updating `docs/canonical/appendix-c-formalisation.md` first.
- Do not frame the research as a socio-technical study with a CS component — it is a CS architecture thesis with a contextual evaluation component.
- Do not treat RQ5 as a co-equal contribution to RQ1/RQ2 in any framing, abstract, or introduction.

---

## Citation Reference Rule

**Whenever a paper from the corpus is cited or referenced in any document in this project, add a `[[notes]]` link immediately after the paper name.**

### Format

```
Author (Year) [[notes]](../notes/filename.md)
```

- From `docs/` (root level) → path prefix is `../notes/`
- From `docs/canonical/` → path prefix is `../../notes/`
- From `docs/justification/` → path prefix is `../../notes/`
- From `docs/chapters/` subdirectories → path prefix is `../../../notes/`
- From `papers/` → path prefix is `../notes/`
- Spaces in filenames must be URL-encoded as `%20`
- Special characters: `:` → `%3A`, `?` → `%3F`, `'` → `%27`, `,` → `%2C`, `&` → `%26`

### Reference lookup

The master citation → notes file mapping is at:
`docs/canonical/citation-notes-map.md`

This file contains ready-to-paste `[[notes]](path)` quick links for all 63 papers in the corpus.

**Special case**: Muhamad et al. (2024) notes file is in `../papers/sources/` not `../notes/`.

### When this rule applies

- Writing or updating any justification document (`docs/justification/*.md`)
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

`docs/canonical/appendix-c-formalisation.md` is the single source of truth for all formal variable definitions.

### Current canonical definitions

| Symbol | Type | Definition |
|---|---|---|
| w | ℝ≥0 | Wind speed (knots, sustained) |
| r | ordinal categorical | Rainfall intensity {none, light, moderate, heavy, storm} |
| m | ordinal categorical | Marine warning level {none, advisory, warning, alert} |
| o | ℝ≥0 × ℝ≥0 | Ocean state (wave height m, swell period s). Classification uses the wave height component only; swell period is retained but unused — see appendix-c C.9.3 |
| v | ordinal categorical | Vessel category {small, medium, big}, defined by **GRT**: small < 10, medium 10–25, big > 25 (Yunus 2007, via Yaakob et al. 2015). Tonnage rather than LOA because the source LOA bands overlap |
| t | [0, 24) | Time of day (hour, 24-hour clock) |

### g_w never fires — this is a site finding, and it is settled

`g_w` **never fires** at the deployment site: sustained wind over five years of hourly data reaches a maximum of **21.8 kn** (sea grid cell) against thresholds of 22 and 27 kn. Zero activations, in **both** reporting configurations.

**Q1 is answered (2026-09-06): `g_w` is retained, reading sustained wind, unchanged.** Redefining `w` over gusts is **rejected** — that would be choosing whichever definition makes the component fire. Do not repair `g_w` to preserve the model.

**F-7 framing decision (2026-09-06):** only **three** functions ever bind at this site — `g_o` (97.40% / 95.05% of daylight CAUTION), `g_t`, `g_r`. **The classifier is NOT reduced.** All five functions are retained with explicit scope statements, and the binding profile is reported as a site characterisation. Reducing it would fit the specification to one site's weather and cost the transferability claim both papers make.

**Present `g_w` and `g_m` separately — they are not the same case:**

- `g_w` — **measured and never reached.** A property of the site, established against a pre-registered prediction (P16) that it *would* be crossed, and refuted. Belongs in results. **Always quote the 0.2 kn margin** — the honest claim is "essentially never reaches the threshold", not "wind does not matter here".
- `g_m` — **never measured.** No marine warning archive exists; `m` is held at `none` throughout. Belongs in threats to validity. **All severity figures are therefore lower bounds.**

Full reasoning: `empirical-findings-2026-09-06.md` §3.

### ⚠️ Mode-chattering claim is unsupported — qualified 2026-09-06

**Measured: 5,416 state transitions in five years, 95.8% of them scheduled clock events; 70 genuine oscillations (14/yr); hysteresis reduces condition-driven transitions by 6.2%.** The claim is not supported at hourly resolution.

**Resolved: hysteresis is retained, framed as a low-cost precaution rather than a mitigation for an observed instability.** The measured figures and the hourly-resolution bound must appear alongside it. Applied to `manuscript-v3.md` (both the prototype paragraph and the Deployment Challenges subsection), the Journal 1 §9 and §12 section plans, and `docs/justification/safety-state-design.md` §2.5, which now carries a qualifying banner.

Do not restate the original unqualified claim. See `empirical-findings-2026-09-06.md` F-6.

### Classification structure (amended 2026-09-06)

**f(E) = max-severity(g_w(w), g_r(r), g_m(m), g_o(o, v), g_t(t))** — five terms, not six.

`v` is a **conditioning parameter, not an independent classifier**. There is no `g_v`. Vessel category parameterises the ocean state thresholds:

| v (GRT) | SAFE | CAUTION | UNSAFE |
|---|---|---|---|
| small (< 10) | o < 1.0 m | 1.0 ≤ o ≤ 1.25 m | o > 1.25 m |
| medium (10–25) | o < 1.4 m | 1.4 ≤ o ≤ 2.8 m | o > 2.8 m |
| big (> 25) | o < 1.5 m | 1.5 ≤ o ≤ 3.5 m | o > 3.5 m |

**Do not reintroduce `g_v`.** A prior formulation defined `g_v(v)` with codomain {SAFE, CAUTION} contributing an independent severity term. It was superseded because a constant term in a maximum is a floor, not a threshold shift — vessel category had no effect on the CAUTION/UNSAFE boundary, under-classifying small-vessel risk across the 1.5–3.5 m band, and made SAFE unreachable for the entire deployment population. Full rationale in `appendix-c-formalisation.md` C.2 ("Note: there is no g_v") and `docs/superpowers/plans/2026-09-06-formal-model-and-evaluation-realignment.md`.

Note that `notes/Stability, Seakeeping and Safety Assessment...md` §4.2 still argues for the superseded design; treat that section as historical.

### ⚠️ Recomputation rule — added 2026-09-06 after §0b

**Propagating a parameter is NOT the same as recomputing what depends on it.** When the 1.9 → 1.25 m amendment was applied, the threshold constants in every script were updated but the *findings derived from them* were not re-run. F-4 and F-7 kept pre-amendment values for half a day inside a document whose threshold table already said 1.25 m.

Therefore, whenever a threshold, a data source, or a grid cell changes:

1. Update the constant.
2. **Re-run `scripts/canonical_figures.py`** and replace §0a wholesale.
3. Re-run `scripts/condition_comparison.py`.
4. Annotate any finding whose published numbers were computed under the old configuration — do not silently overwrite it; it remains a valid record of what was found then.

Note that `historical_replay.py`, `diagnostic_binding.py` and `hysteresis_analysis.py` **still read the v1 land-cell files** (`raw_weather.csv`, `raw_marine.csv`, `raw_rainfall.csv`). They are retained to reproduce the historical findings. **Do not quote figures from them as current** — `canonical_figures.py` is the authority.

### When a variable definition changes

1. **Update `docs/canonical/appendix-c-formalisation.md` first** — this is the canonical source
2. **Search all docs for the old definition** and update every occurrence
3. **Check these files every time** — they all reference E vector components:
   - `docs/justification-formal-model.md`
   - `docs/justification-safety-state-design.md`
   - `docs/justification-low-resource-environments.md`
   - `docs/justification-environmental-state-governance.md`
   - `papers/review-plan.md`
4. **Never define the same symbol differently in different documents**
