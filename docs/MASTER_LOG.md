# PhD Writing Master Log

**Last Updated:** 2026-08-06

---

## Current Sprint (2026-08-06 onwards)

**Goal:** Set up Journal 1 as an independent research project and complete Module 1 (Formal Theory) of Appendix C.  
**Blockers:** None — Module 1 complete. Next: Module 2 (architecture diagrams, publication quality).

---

## File Status

| Chapter | Current Version | Status | Next Action |
|---------|----------------|--------|-------------|
| Ch 1 | — | Not started | — |
| Ch 2 | v1-initial-draft | Drafted | Awaiting next revision cycle |
| Ch 3 | — | Not started | Begins after Journal 1 Module 4 (experimental design) |
| Ch 4 (RQ4) | — | Not started | Begins after experiments run |
| Ch 5 (RQ5) | — | Not started | — |
| Ch 6 (Discussion) | — | Not started | — |
| Ch 7 (Conclusion) | — | Not started | — |

---

## Publication Status

| Venue | Version | Status | Next Action |
|-------|---------|--------|-------------|
| IPSci 2026 (conference) | v8 | Submitted — awaiting reviewer feedback | Wait; do not edit |
| Journal 1 (Safety Science) | v1 skeleton | Research design phase | Module 2: architecture diagrams |
| Journal 2 (Expert Systems) | — | Planned | After Journal 1 submitted |
| Journal 3 (Pertanika JTAS) | — | Planned | 2027–2028 |

---

## Daily Log

### 2026-08-06

**Done:**

*Journal 1 setup*
- Reviewed PhD-ORGANIZATION-SYSTEM.md and understood full project structure
- Set up `publications/active/journal-1/` folder: README, submissions/v1-initial-submission/manuscript.md, correspondence/notes.md
- Reframed Journal 1 as an independent paper (not a conference extension): new title, 15-section structure, research module plan
- Created `publications/active/journal-1/research-design.md` — 4 RQs, 4 hypotheses, 5 research modules with sequencing through April 2027
- Updated journal-1 README: Safety Science as primary target, correct milestone dates, key contributions distinct from conference paper

*Appendix C — Module 1 (Formal Theory)*
- Full analysis of existing `docs/canonical/appendix-c-formalisation.md`: identified what was complete (Safety Dominance proof, E vector justifications, worst-case aggregation) and what was missing (severity ordering, monotonicity theorem, full threshold table, proof formatting)
- **Added Definition C.1 (Severity Order):** UNSAFE ≻ CAUTION ≻ SAFE — formal basis for max-severity
- **Added Theorem C.1 (Totality of f):** f(E) returns exactly one state for all E — per-component partition proof for all six gᵢ functions
- **Added full threshold table:** per-component classification functions (g_w, g_r, g_m, g_o, g_v, g_t) with MET Malaysia threshold values anchored to Rahim et al. 2024, Gao 2024, Yamin et al. 2025
- **Added Theorem C.2 (Monotonicity of A_AI):** if S₁ ≻ S₂ then A_AI(S₁) ⊆ A_AI(S₂) — three-case proof; Corollary C.2 (strict monotonicity); citations to Bloomfield & Rushby (2025) and Dalrymple et al. (2024)
- **Reformatted Theorem C.3 (Safety Dominance Property):** four explicit assumptions (A1–A4), exhaustive case analysis, formal remarks
- Removed "Hybrid AI Decision" label — architecture is fully symbolic/rule-based; no ML component
- Removed "illustrative, not exhaustive" placeholder from C.2
- Fixed g_w domain notation: (−∞, 22] → [0, 22]
- Added g_v UNSAFE clarification note
- Added forward reference for max-severity in C.1
- Renumbered theorems in document order (C.2 Totality → C.1, C.1 Monotonicity → C.2); updated all cross-references throughout

**Issues:** None.

**Next session:**
- Module 2 — architecture diagrams at publication quality
  - Expand Layer 2/3 architecture diagram (improve on conference paper Fig. 3)
  - Add state transition diagram with formal notation
  - Add sequence diagram (observation → classification → gating → reasoning → output)
  - Document hysteresis smoothing mechanism formally

---

## Canonical Documents Status

| Document | Last updated | Notes |
|---|---|---|
| `docs/canonical/appendix-c-formalisation.md` | 2026-08-06 | Module 1 complete — 1 definition, 3 theorems, full threshold table |
| `docs/canonical/architecture-illustration.md` | Pre-2026-08-06 | To be updated in Module 2 |
| `docs/canonical/evaluation-design-rq4.md` | Pre-2026-08-06 | Will feed Module 4 (experimental design) |
| `docs/canonical/rq5-study-design.md` | Pre-2026-08-06 | No changes needed yet |
| `docs/canonical/citation-notes-map.md` | Pre-2026-08-06 | No new papers added this session |
