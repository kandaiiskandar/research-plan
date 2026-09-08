# Journal 1 — Session Log

**Paper:** A Formally Verified Runtime AI Governance Architecture Based on Graduated Safety-State Gating  
**Target:** Safety Science (Elsevier, Q1)

---

## Session: 2026-08-09

### What was completed

#### 1. Section 5 — peer-review revisions applied (continued from previous session)

| Change | Detail |
|--------|--------|
| `max-severity` → `max_≻` | Replaced pseudo-code notation with formal order notation throughout Section 5. `max-severity` pseudo-code preserved in `section-5-plan.md` Section 8 for use in Sections 7 and 9. |
| Table 1 `t` column | Standardised from HH:MM format to decimal reals (6.0 ≤ t < 17.0 etc.) — consistent with Definition 5.1 domain [0, 24) ⊂ ℝ |
| Fail-safe rule | Added xᵢ = ⊥ → f(E) = UNSAFE in Section 5.2 — conservative failure for missing/corrupted sensor data |
| Caution qualifier | Clarified Go under CAUTION: Layer 3 returns Go ∈ R unchanged; qualifier is a Layer 4 rendering operation only |
| Definition 5.11 (AI Output Mapping) | Added explicit two-case piecewise definition of AI(E) before Property 5.3 — makes UNSAFE proof trivial |
| MET Malaysia source claim | Softened from "sourced from MET Malaysia" to "external meteorological and marine data feeds"; data sourcing deferred to Section 9 |
| Governance Independence | Promoted from informal sentence to Definition 5.2 — formal causal constraint on Layer 2/Layer 3 relationship |
| Cyclic time note | Added remark on sin/cos encoding for downstream distance computations |
| Definition renumbering | All definitions 5.2–5.10 renumbered to 5.3–5.11 after inserting Definition 5.2 (Governance Independence); summary table in 5.7 updated |

#### 2. NIST AI RMF — added to corpus

| Item | Status |
|------|--------|
| Notes file | `notes/Artificial Intelligence Risk Management Framework (AI RMF 1.0).md` |
| PDF link | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf |
| Citation map | Entry added: `NIST (2023) [AI RMF 1.0]` |
| Role | Primary governance framework for Section 3. Notes include GOVERN sub-category → architecture mapping table and ready-to-paste citation paragraph. |

#### 3. Figures — markdown illustration

Figure 2 (four-layer architecture) and Figure 3 (advisory scope containment table) illustrated in markdown/ASCII format. SVG rendering deferred — layouts confirmed correct before investing in vector graphics.

#### 4. Reference explainer created

`docs/reference/explainer-per-component-classification-functions.md` — plain-language + formal + operational explanation of the gᵢ functions. Includes worked examples (CAUTION scenario, UNSAFE scenario), full threshold table, and "why gᵢ is critical" summary. For author reading reference.

#### 5. Section 6 — Theoretical Analysis — drafted and revised

**Status: Complete (submission quality per peer review)**

**Plan:** `publications/active/journal-1/section-6-plan.md`

**Subsections drafted:**

| Subsection | Content |
|------------|---------|
| 6.1 Overview | Three theorems, their dependencies, proof method (exhaustive case analysis, no induction) |
| 6.2 Theorem 6.1 (Totality) | Six-case gᵢ domain verification + max_≻ uniqueness + fail-safe extension |
| 6.3 Theorem 6.2 (Monotonicity) | Three-case proof; Corollary 6.2 (strict containment chain); Corollary 6.3 (Properties 5.1 + 5.2) |
| 6.4 Theorem 6.3 (Safety Dominance) | Four assumptions A1–A4; three-case constructive proof; Remarks on construction vs. filtering |
| 6.5 Composite Guarantee | Table 5 collecting all three theorems; cumulative guarantee statement; forward ref to Section 10 |

**Peer-review revisions applied:**

| Change | Detail |
|--------|--------|
| "relationship" → "dependencies" in 6.1 | More precise — logical dependency, not just thematic grouping |
| Figure 2 reference added in 6.4 | Sentence added before A1–A4 grounding proof in architecture diagram |
| Significance paragraphs | Each now has a distinctive single-word characterisation: **completeness** (6.2), **consistency** (6.3), **effectiveness** (6.4) |

**Reviewer verdict:** No correctness issues. All definition cross-references, theorem numbering, and set notation verified correct.

---

### Current manuscript status

| Section | Status |
|---------|--------|
| 1. Introduction | Placeholder |
| 2. Related Work | Placeholder |
| 3. AI Governance Foundations | Placeholder |
| 4. Problem Formulation | Placeholder |
| **5. Formal Architecture** | **Complete — submission quality** |
| **6. Theoretical Analysis** | **Complete — submission quality** |
| 7. Algorithms | Placeholder |
| 8–14 | Placeholder |

---

### What to do next

| Priority | Task | Notes |
|----------|------|-------|
| 1 | Draft Section 3 — AI Governance Foundations | Use NIST AI RMF as primary framework. Citation paragraph ready in `notes/Artificial Intelligence Risk Management Framework (AI RMF 1.0).md` Section 5. |
| 2 | Draft Section 7 — Algorithm Specification | Use `max-severity` pseudo-code from `section-5-plan.md` Section 8. Algorithms for f(E) and RS(S) supply mechanism. |
| 3 | Draft Section 4 — Problem Formulation | Formal problem statement: given E, define requirements on governance mechanism M such that M(E) ⊆ A_AI(S). |
| 4 | Render Figure 2 and Figure 3 as SVG | Layouts confirmed in markdown — ready to convert. |

---

### Files modified this session

| File | Change |
|------|--------|
| `publications/active/journal-1/submissions/v1-initial-submission/manuscript.md` | Section 5 peer-review revisions applied; Section 6 fully drafted + peer-review revisions applied |
| `publications/active/journal-1/section-5-plan.md` | Section 8 (max-severity pseudo-code reference) added |
| `publications/active/journal-1/section-6-plan.md` | Created |
| `docs/canonical/citation-notes-map.md` | NIST AI RMF entry added |
| `docs/reference/explainer-per-component-classification-functions.md` | Created |
| `notes/Artificial Intelligence Risk Management Framework (AI RMF 1.0).md` | Created |

---

## Session: 2026-08-08

### What was completed

#### 1. Three-Tier Triangulation — papers processed

Three papers were evaluated as threshold validation support for Section 5.3. Two were added to the corpus; one was rejected.

| Paper | Tier | Decision | Notes file |
|-------|------|----------|------------|
| Jeong & Im (2023) — Korean small fishing vessel capsizing, 23-year dataset | Tier 2 (Empirical risk) | Added | `notes/Proposal of Restrictions on the Departure...` |
| Yaakob et al. (2015) — Malaysian small fishing boat seakeeping, Johor coast | Tier 1 (Hydrodynamics) | Added | `notes/Stability, Seakeeping and Safety Assessment...` |
| Abu Samah et al. (2019) — social science paper on fisher behaviour | — | Rejected — not threshold validation | Notes file deleted; citation map entry removed |

**Key insight from Yaakob et al.:** Boat B (5.03 m) fails seakeeping at Hs ≈ 0.875 m, below the 1.5 m CAUTION boundary for g_o. This initially appeared to challenge the threshold but is correctly handled by the architecture: g_v(small) = CAUTION always, so a small vessel at Hs < 1.5 m still classifies as f(E) = CAUTION via max_≻. The architecture captures small-vessel risk through two mechanisms: g_v contribution and g_o contribution.

**Citation map:** Two new entries added to `docs/canonical/citation-notes-map.md`.

**appendix-c-formalisation.md:** Two empirical support paragraphs added — one under g_o (Jeong & Im) and one under g_v (Yaakob et al.).

---

#### 2. NIST AI RMF 1.0 — added to corpus

| Item | Status |
|------|--------|
| Notes file | Created: `notes/Artificial Intelligence Risk Management Framework (AI RMF 1.0).md` |
| Citation map | Entry added: `NIST (2023) [AI RMF 1.0]` |
| PDF link | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf |

**Role in paper:** Primary governance framework reference for Section 3 (AI Governance Foundations). The notes file includes a mapping table (GOVERN sub-category → architecture mechanism) and a ready-to-paste citation paragraph for Section 3. Key positioning: AI RMF describes *what* governance should achieve; the proposed architecture provides the *technical mechanism* to enforce it at runtime. AI RMF has no CAUTION analogue — supports the gap argument.

---

#### 3. Section 5 — drafted and revised

**Status: Complete (draft quality, peer-review revisions applied)**

Section 5 of `publications/active/journal-1/submissions/v1-initial-submission/manuscript.md` was drafted from scratch and revised through one peer-review pass.

**Subsections drafted:**

| Subsection | Content | Definitions |
|------------|---------|-------------|
| 5.1 Architecture Overview | Four-step pipeline; CAUTION as contribution; binary gap framing | — |
| 5.2 Environmental State Representation | E = (w, r, m, o, v, t) with typed domain table | Def 5.1 (E vector), Def 5.2 (Governance Independence) |
| 5.3 Safety State Classification | Severity order; per-component functions; threshold Table 1; f(E); Theorem 5.1 | Def 5.3 (Severity Order), Def 5.4 (gᵢ), Def 5.5 (f(E)) |
| 5.4 Governance Pair | R; G(S); A_AI(S); governance Table 2; CAUTION rationale | Def 5.6 (R), Def 5.7 (G), Def 5.8 (A_AI), Def 5.9 (Governance Pair) |
| 5.5 Formal Properties | Properties 5.1–5.3; AI(E) formal mapping | Def 5.11 (AI Output Mapping) |
| 5.6 Layer Architecture + RS(S) | Four-layer Table 3; causal flow; RS(S) supply; construction vs filtering; rule-based rationale | Def 5.10 (RS(S)) |
| 5.7 Section Summary | Symbol Table 4; pipeline restatement; forward refs | — |

**Peer-review revisions applied (2026-08-08):**

| Issue | Fix |
|-------|-----|
| `max-severity` pseudo-code in formal definition | Replaced with `max_≻ {gᵢ(xᵢ)}` notation throughout |
| t column in Table 1 used HH:MM format | Standardised to decimal reals (6.0 ≤ t < 17.0, etc.) |
| No fail-safe for missing/corrupted sensor inputs | Added xᵢ = ⊥ → f(E) = UNSAFE rule in Section 5.2 |
| Caution qualifier could imply Go is sub-typed | Clarified qualifier is Layer 4 rendering only; Layer 3 returns Go ∈ R unchanged |
| AI(E) = ∅ for UNSAFE was implicit | Added Definition 5.11 (AI Output Mapping) with explicit two-case piecewise definition |
| MET Malaysia claimed as single source for all four dynamic variables | Softened to "external meteorological and marine data feeds"; data sourcing deferred to Section 9 |
| "All six parameters are observable" was a weak sentence | Elevated to Definition 5.2 (Governance Independence) — formal causal constraint, not just an observation |
| t is linear but clock time is cyclic | Added note on cyclic encoding (sin/cos) for any downstream distance computation |

---

#### 4. Deferred notation reference saved

`publications/active/journal-1/section-5-plan.md` — Section 8 added with `max-severity` pseudo-code, equivalence note, complexity note, and usage guide (which notation to use in which section).

---

### Current definition numbering (Section 5)

| Number | Name |
|--------|------|
| Definition 5.1 | Environmental State Vector |
| Definition 5.2 | Governance Independence |
| Definition 5.3 | Severity Order |
| Definition 5.4 | Per-Component Classification Functions (gᵢ) |
| Definition 5.5 | Safety State Classification Function f(E) |
| Definition 5.6 | Recommendation Type Space R |
| Definition 5.7 | AI Participation Gate G(S) |
| Definition 5.8 | AI-Admissible Recommendation Space A_AI(S) |
| Definition 5.9 | Governance Pair (G(S), A_AI(S)) |
| Definition 5.10 | RS(S) Rule Set Supply |
| Definition 5.11 | AI Output Mapping AI(E) |

Theorems: Theorem 5.1 (Totality). Properties: 5.1 (Participation Constraint), 5.2 (Advisory Restriction Constraint), 5.3 (Safety Dominance Property).

---

### What to do next

| Priority | Task | Notes |
|----------|------|-------|
| 1 | Draft Section 6 — Theoretical Analysis | Prove Theorem 5.1 (Totality), Theorem 5.2 (Monotonicity), Theorem 5.3 (Safety Dominance Property). Proofs already exist in `appendix-c-formalisation.md` Sections C.6–C.7 — adapt to journal numbering. |
| 2 | Draft Section 3 — AI Governance Foundations | Use NIST AI RMF as primary framework. Citation paragraph ready in `notes/Artificial Intelligence Risk Management Framework (AI RMF 1.0).md` Section 5. |
| 3 | Draft Section 7 — Algorithm Specification | Use `max-severity` pseudo-code from `section-5-plan.md` Section 8. |
| 4 | Draft Section 4 — Problem Formulation | Formal problem statement using E, f(E), M(E) ⊆ A_AI(S). |

---

### Files modified this session

| File | Change |
|------|--------|
| `publications/active/journal-1/submissions/v1-initial-submission/manuscript.md` | Section 5 fully drafted + peer-review revisions applied |
| `publications/active/journal-1/section-5-plan.md` | Section 8 (deferred notation) added |
| `docs/canonical/appendix-c-formalisation.md` | Empirical support paragraphs added under g_o and g_v |
| `docs/canonical/citation-notes-map.md` | Three entries added (Jeong & Im 2023, Yaakob et al. 2015, NIST AI RMF 2023) |
| `notes/Proposal of Restrictions on the Departure of Korea Small Fishing Vessel according to Wave Height.md` | Created |
| `notes/Stability, Seakeeping and Safety Assessment of Small Fishing Boats Operating in Southern Coast of Peninsular Malaysia.md` | Created |
| `notes/Artificial Intelligence Risk Management Framework (AI RMF 1.0).md` | Created |
