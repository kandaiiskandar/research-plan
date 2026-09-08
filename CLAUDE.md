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
| `docs/canonical/session-log-2026-09-08.md` | **START HERE.** The `g_t` provenance work: audits → SDR-001 approval → execution conditions C-0…C-7. **C-6 and C-8 are the only open items.** Carries the resume instructions, the baseline authority rule, and the artefact index |
| `docs/canonical/session-log-2026-09-06.md` | The preceding session — fifteen findings and the three gating decisions (threshold, F-7 framing, headline figure), all resolved |
| `docs/canonical/decision-record-empirical-first.md` | **Read before any domain-instantiation work.** Records the 2026-09-06 decision that site data now drives the classifier specification, not the reverse. Carries open questions **Q1–Q8** |
| `docs/canonical/empirical-findings-2026-09-06.md` | **Findings F-1 to F-18** from 5 years of site data. **F-15 answers Review 3's novelty objection: a Flehmig-style traffic-light baseline (C3) diverges from a plain binary gate (C1) in 0.00% of hours.** **§0a "Current reportable figures" is the authoritative list, generated by `scripts/canonical_figures.py` — do not hand-edit it.** Figures are reported in TWO configurations ("option C"): **PRIMARY** 5.00 yr / ERA5-Ocean 50 km and **RESOLUTION** 3.25 yr / MFWAM 8 km. Headline: **Level 2 binds 7.72% (primary) / 5.98% (resolution)**. 12.4%, 8.3%, lone-6.1% and 7.84%/6.15% are superseded. **§0b records why the earlier table was wrong — read it before trusting any derived figure.** Also carries one claim that must be withdrawn (mode-chattering) |
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
| `notes/` | Per-paper extraction notes for the 111 active corpus papers (plus one archived stub for a paper superseded by OWASP Top 10 for Agentic Applications 2026); the manuscript's reviewer-facing figure is 72, which is the subset that "advanced to full review" at manuscript submission — see `docs/canonical/review-protocol.md` §Corpus reconciliation |

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

This file contains ready-to-paste `[[notes]](path)` quick links for all 111 papers in the active corpus.

**No special cases** — all corpus notes files live in `../notes/`. (An earlier version of this doc noted Muhamad et al. (2024) as a `papers/sources/` special case; the file was consolidated into `notes/` on 2026-09-07.)

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

**Condition components — C = {w, r, m, o, t}.** Time-varying quantities the classifier reads. Each has a value domain `Xᵢ` and an observation space `Obsᵢ = (Xᵢ × 𝕋) ∪ {⊥}`.

| Symbol | Value domain `Xᵢ` | Definition |
|---|---|---|
| w | ℝ≥0 | Wind speed (knots, sustained) |
| r | ℝ≥0 | Rainfall intensity (mm/hr). **Numeric, not categorical** — redefined 2026-09-08. `g_r` performs the classification; JPS/DID intensity categories are provenance for the 10.0 boundary, not the domain of `r` |
| m | {none, advisory, warning, alert} | Marine warning level (ordinal). **No data source exists for the study site** — the replays run with `m ∈ D`; see the ⊥ block below |
| o | ℝ≥0 × ℝ≥0 | Ocean state (wave height m, swell period s). `g_o` reads **the wave height component only**; ⊥ attaches to what is read, so an unavailable swell period does **not** fault `o` (appendix-c C.2.0.2) |
| t | [0, 24) | Time of day (hour, 24-hour clock). **Read from the device clock, not an external source** — hence `t ∉ D` always (appendix-c C.2.0.5 D1) |

**Configuration parameter — not a condition component, not sampled, not in any `Obsᵢ`:**

| Symbol | Domain | Definition |
|---|---|---|
| v | V = {small, medium, big} | Vessel category by **GRT**: small < 10, medium 10–25, big > 25 (Yunus 2007, via Yaakob et al. 2015). Tonnage rather than LOA because the source LOA bands overlap. **Supplied at configuration time.** Unconfigured `v` is a *startup precondition failure*, not a classification (appendix-c C.2.0.6) |

**Spaces and functions** (appendix-c C.2.0.1 — do not conflate the ideal and operational forms):

| Symbol | Type | Meaning |
|---|---|---|
| `Obsᵢ` | (Xᵢ × 𝕋) ∪ {⊥} | Observation — a value with the instant it was taken, or a fault |
| `Y` | ∏_{i∈C} (Xᵢ ∪ {⊥}) | Resolved input — what the classifier actually consumes |
| `D` | D ⊆ {w, r, m, o} | Declared exclusion set. **`t ∉ D`.** Replays run `D = {m}` |
| `ρ_{D,τ}` | ∏Obsᵢ → Y | Resolution map — discharges exclusion, validation, freshness |
| **`f`** | **Y × V → S** | **Resolved classifier.** `f(E)` is the *ideal-form* abbreviation, every component valid |
| **`F_{D,τ}`** | **f ∘ ρ_{D,τ}** | **Operational classifier** — what a deployment executes |
| `gᵢ` | Xᵢ ∪ {⊥} → S | Component classifier, with `gᵢ(⊥) = UNSAFE` |
| `cause` | Y → {fault, hazard} | Provenance of a non-SAFE state. **No effect on G(S) or A_AI(S)** |

**Write `f(E)` only for the ideal case; write `F_{D,τ}` for deployed behaviour.** Theorem C.1 covers the first, Theorem C.1b the second. Safety Dominance (Theorem C.3) holds for both, and its proof depends only on the *value* of S — so it covers fault-driven UNSAFE unchanged.

### g_w — thresholds 21.6 / 27.0 kn, and it DOES fire (restated 2026-09-08)

**`g_w` thresholds are 21.6 kn (CAUTION) and 27.0 kn (UNSAFE)** — MET Malaysia Cat 1 (40 km/h = 21.598 kn) and Cat 2 (50 km/h = 26.998 kn) onsets, preserved at source value rather than rounded.

**Do not reintroduce 22 kn.** It was an undocumented rounding of 21.598, and it changed an empirical result: at 22 kn `g_w` never activates; at 21.6 kn it activates **twice** in five years.

**Current claim: `g_w` activates 2 times in 43,848 hours (0.005%) and BINDS in none of them** — on both occasions another component was already more severe. Do not write "never fires". Do not write "wind is irrelevant". `g_w`'s binding share of 0.00% in F-7 is correct and is *not* contradicted by the two activations. See F-17.

**P16 is CONFIRMED, not refuted** (re-resolved 2026-09-08). P01, the zero-activation regression lock, is now REFUTED.

**Q1 is answered (2026-09-06): `g_w` is retained, reading sustained wind, unchanged.** Redefining `w` over gusts is **rejected** — that would be choosing whichever definition makes the component fire. Do not repair `g_w` to preserve the model.

**F-7 framing decision (2026-09-06):** only **three** functions ever bind at this site — `g_o` (98.66% / 97.41% of daylight CAUTION), `g_t`, `g_r`. **The classifier is NOT reduced.** All five functions are retained with explicit scope statements, and the binding profile is reported as a site characterisation. Reducing it would fit the specification to one site's weather and cost the transferability claim both papers make.

**Present `g_w` and `g_m` separately — they are not the same case:**

- `g_w` — **measured, reached twice, never decisive.** A property of the site. P16 predicted it *would* be crossed and is **CONFIRMED** at the corrected 21.6 kn threshold. Belongs in results. **Always quote both numbers: 2 activations, 0 bindings.** Do not write "never fires"; do not write "wind does not matter here".
- `g_m` — **never measured.** No marine warning archive exists; `m` is held at `none` throughout. Belongs in threats to validity. **All severity figures are therefore lower bounds.**

Full reasoning: `empirical-findings-2026-09-06.md` §3.

### ⚠️ Mode-chattering claim is unsupported — qualified 2026-09-06

**Measured on v1 site data, current thresholds: 5,220 state transitions in five years, the large majority scheduled clock events; 37 genuine oscillations (7.4/yr); hysteresis reduces non-scheduled transitions by 7.83%.** The claim is not supported at hourly resolution.

> **⚠️ Figures corrected 2026-09-08 (C-7 baseline reconciliation).** This block previously read *"5,416 transitions … 70 genuine oscillations (14/yr) … 6.2%"*. **Those are not wrong numbers — they are a coherent snapshot of a superseded threshold specification** (v1 data with `r_CAUTION = 7.5 mm/hr` and small-vessel `o_UNSAFE = 1.9 m`, both since amended). Under the current thresholds (10.0 mm/hr, 1.25 m) the same v1 data gives **5,220 / 37 / 7.83%**, which is what the prediction register holds for P10, P11 and P12. **Use the current figures.** Full provenance: `report-c7-closure-2026-09-08.md` and `data/c7/baseline-provenance.csv`.
>
> **One register value is a deliberate exception: P09 = 5,416**, which is the *pre-amendment* figure, retained as the historical actual recorded when P09 was resolved. **Do not treat 5,416 as reproducible under the current specification** — the comparable current-threshold baseline is **5,220**.

**Resolved: hysteresis is retained, framed as a low-cost precaution rather than a mitigation for an observed instability.** The measured figures and the hourly-resolution bound must appear alongside it. Applied to `manuscript-v3.md` (both the prototype paragraph and the Deployment Challenges subsection), the Journal 1 §9 and §12 section plans, and `docs/justification/safety-state-design.md` §2.5, which now carries a qualifying banner.

Do not restate the original unqualified claim. See `empirical-findings-2026-09-06.md` F-6.

### Classification structure (amended 2026-09-06)

**f(E) = max-severity(g_w(w), g_r(r), g_m(m), g_o(o, v), g_t(t))** — five terms, not six.

**Current thresholds (all anchored to a named source):**

| | SAFE | CAUTION | UNSAFE | Source of boundaries |
|---|---|---|---|---|
| `g_w` (kn) | ≤ 21.6 | 21.6–27.0 | > 27.0 | MET Cat 1 / Cat 2 onsets (40 / 50 km/h) |
| `g_r` (mm/hr) | ≤ 10.0 | 10.0–20.0 | > 20.0 | JPS/DID *Light* limit / MET Ribut Petir |
| `g_t` (hr) | 06:00–17:00 | 17:00–19:00 | else | ⚠️ **exact cut-offs undefended — see below** |

`v` is a **conditioning parameter, not an independent classifier**. There is no `g_v`. Vessel category parameterises the ocean state thresholds:

| v (GRT) | SAFE | CAUTION | UNSAFE |
|---|---|---|---|
| small (< 10) | o < 1.0 m | 1.0 ≤ o ≤ 1.25 m | o > 1.25 m |
| medium (10–25) | o < 1.4 m | 1.4 ≤ o ≤ 2.8 m | o > 2.8 m |
| big (> 25) | o < 1.5 m | 1.5 ≤ o ≤ 3.5 m | o > 3.5 m |

**Do not reintroduce `g_v`.** A prior formulation defined `g_v(v)` with codomain {SAFE, CAUTION} contributing an independent severity term. It was superseded because a constant term in a maximum is a floor, not a threshold shift — vessel category had no effect on the CAUTION/UNSAFE boundary, under-classifying small-vessel risk across the 1.5–3.5 m band, and made SAFE unreachable for the entire deployment population. Full rationale in `appendix-c-formalisation.md` C.2 ("Note: there is no g_v") and `docs/superpowers/plans/2026-09-06-formal-model-and-evaluation-realignment.md`.

Note that `notes/Stability, Seakeeping and Safety Assessment...md` §4.2 still argues for the superseded design; treat that section as historical.

### Rainfall thresholds — anchored to MET 2026-09-08

**`g_r`: SAFE ≤ 10.0 mm/hr · CAUTION 10.1–20.0 · UNSAFE > 20.0.**

- **20.0 mm/hr is MET Malaysia's Ribut Petir warning trigger** — official.
- **10.0 mm/hr is the JPS/DID Infobanjir *Light* upper limit** — MET publishes **no** criterion below 20 mm/hr, so this boundary is necessarily non-MET.

**Do not reintroduce 7.5 mm/hr.** It matched no published source and descends from a mapping recorded as an error in `docs/implementation/data-source-met-malaysia.md` line 125.

**Do not use MET's *Hujan Berterusan* tiers** (> 60 mm/period, > 150 mm/24 hr) — cumulative totals, unusable on hourly data without an unsourced disaggregation assumption.

Full rationale: `finding-met-lower-boundary-gap.md`. **That document generalises the MET gap: warning criteria state where an alert is issued, never where caution should begin — established independently for waves and rainfall.**

### ⚠️ g_t — replacement design APPROVED 2026-09-08, but the INCUMBENT REMAINS CANONICAL

**Use the incumbent `g_t` in all work: SAFE 06:00–17:00 · CAUTION 17:00–19:00 · UNSAFE otherwise.** It is unchanged and remains the canonical and runtime specification. **7.72% / 5.98% remain the authoritative figures.**

`g_t` carries **87.63% of all non-SAFE classifications** — more than every other component combined — yet its boundaries (06:00, 17:00, 19:00) are the least defended in the specification. Atacan & Düzbastılar establish that night navigation elevates accident probability and consequence; they do not establish 17:00 and 19:00. That audit is complete, and its outcome is:

**SDR-001 — APPROVED, NOT YET APPLIED** (`finding-gt-evidence-closure.md` Part 6). The approved *design* replaces `g_t` with a solar-event two-state classifier — SAFE from sunrise to sunset, UNSAFE otherwise, `g_t(⊥) = UNSAFE` — on COLREGs Rule 20(b) as the boundary authority. **`g_t` becomes deliberately binary; the architecture stays three-state**, since `g_o` and `g_r` continue to produce CAUTION (2,091 h under Model B).

> **🚧 APPROVAL IS NOT MIGRATION. Do not implement Model B.** Do not introduce sunrise/sunset into Appendix C or any canonical script. Do not quote the Model B sensitivity values (5.81% / 4.48%) as results. Do not re-resolve predictions.
>
> **Execution-condition status as of 2026-09-08 — six closed, two open:**
>
> | | | |
> |---|---|---|
> | **C-0** solar algorithm provenance | ✅ CLOSED | Implementation is **NOAA-style**, not Meeus |
> | **C-1** pin the solar implementation | ✅ CLOSED | `solar-spec-v1` · `solar-v1` · **coordinate resolved to 5.98 N, 116.01 E** |
> | **C-2** 28-row USNO validation artefact | ✅ CLOSED | `data/solar/usno-validation-2026-09-08.csv` — reconstructed; historical record retained |
> | **C-3** daily solar timestamps | ✅ CLOSED | `data/solar/solar-events-daily.csv`, 1,827 rows |
> | **C-4** design consequences documented | ✅ CLOSED | Appendix C **C.2** non-surjectivity · **C.9.5** step cost **2 → 1,536** · **C.9.6** notification separation |
> | **C-5** three-stage hysteretic isolation | ✅ CLOSED | Gate passed. **P12: 7.83 → 8.70 → 10.36** |
> | **C-6** re-resolve predictions | 🔴 **OPEN** | Use `data/c7/baseline-provenance.csv`. **For P09 compare from 5,220, not 5,416** |
> | **C-7** baseline reconciliation | ✅ CLOSED | All stale values are one **pre-amendment threshold vintage** |
> | **C-8** propagation | 🔴 **OPEN** | **8 scripts** (incl. `threshold_comparison.py`), **~17 documents** (incl. RQ4 **SC-10**, Journal 1 manuscript) |
>
> **Migration requires a separate controlled task.** Resume instructions: `session-log-2026-09-08.md` §9. Full detail: `finding-sdr-001-readiness-audit.md` §11 and `approval-report-sdr-001-2026-09-08.md`.

**Solar provenance — use the corrected term.** The validated implementation is the **NOAA-style low-precision solar-position formulation in `scripts/sensitivity/solar.py`**, validated against **USNO API v4.0.1** (28 comparisons, max 0.9 min, mean 0.37 min). **Do not call it Meeus, NOAA/Meeus, Meeus/NOAA or NOAA/Spencer** — no project evidence supports those; see `cleanup-report-c0-solar-provenance-2026-09-08.md`.

### ⊥ semantics — four conditions, four responses (formalised 2026-09-08)

**Do not treat `⊥` as one thing.** appendix-c C.2.0 separates four conditions that were previously collapsed:

| Condition | Response |
|---|---|
| **Invalid** (out of physical range) | ⊥ → UNSAFE |
| **Absent** (no reading now) | ⊥ → UNSAFE |
| **Stale** (beyond `ageᵢ`) | ⊥ → UNSAFE, via the freshness map upstream of `gᵢ` |
| **Unmeasured** (no source exists) | **Declared exclusion** `D`, pinned at **SAFE**, all figures are **lower bounds** |
| `v` unconfigured | **Startup precondition** — refuse to start, not a classification |

**The replays run with D = {m}.** Never write that `m` unavailable means `m = ⊥` without distinguishing live deployment from retrospective replay — applied literally to the replay it classifies all 43,848 hours UNSAFE and voids the headline. See F-18 and `finding-bottom-semantics.md`.

**`⊥` attaches to the quantity a classifier reads, not the declared variable** — otherwise `o` is permanently faulted, since no source provides swell period.

**The fail-safe rule is Corollary C.1b.1, not a pre-check.** It follows from `gᵢ(⊥) = UNSAFE` plus the maximality of UNSAFE under ≻. **Theorem C.1b (Operational Totality)** extends totality from ideal domains to the observation space.

**`ageᵢ` is unspecified** — the freshness machinery exists, the parameters do not. Do not invent a value; that is the 7.5 mm/hr error.

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
