# IPSci 2026 — Session Log

**Paper:** A Graduated Safety-State-Gated Architecture For AI Decision Support  
**Venue:** IPSci 2026  
**Submitted file:** `submissions/v2-post-review/manuscript-v2.5-submitted.md`  
**Status:** Under review — supervisor feedback revision in progress

---

## Session: 2026-08-21

### What was completed

Supervisor feedback revision — 9 of 13 points addressed. All points that could be written from existing material are done. Source for all content: `supervisor-feedback-response.md` (pre-written content map) + journal manuscript Sections 5 and 6 (formal content).

| Point | Title | What was done |
|-------|-------|---------------|
| 1 | Novelty emphasis | Novelty paragraph added to Introduction after Fig. 1: "The contribution is the second dimension — advisory scope — which existing architectures leave entirely unaddressed." Separates G(S) from A_AI(S) explicitly. Closes: "CAUTION is not a softer version of SAFE; it is a formally distinct governance position that binary architectures cannot express." |
| 2 | Formal proofs | `## Formal Properties` subsection added to Proposed Architecture after Formal Structure. Theorem 1 (Totality), Theorem 2 (Monotonicity) with case table, Theorem 3 (Safety Dominance Property) with constructive proof sketch. Conference paper numbering (1–3). |
| 3 | Pseudocode | `## Algorithm Specification` subsection added. Algorithms 1–3: Safety Classification, Governance Gate Evaluation, RS(S) Supply and Advisory Generation. Closing paragraph explains Step 3 of Algorithm 3 as the enforcement point; Step 6 is an invariant assertion, not a runtime check. |
| 4 | Complexity | `## Computational Complexity` subsection added with TABLE IV (six-row complexity table). Three-point narrative: O(1) governance layer, CAUTION cheaper than SAFE, latency dominated by data acquisition. Closes with Katende [17] low-resource deployment requirement. |
| 7 | Deployment challenges | `## Deployment Challenges and Limitations` subsection added as final PA subsection. Paragraph 1: four challenges (connectivity/fail-safe, hardware, threshold maintenance, mode-chattering). Paragraph 2: three limitations (domain-specific R, rule correctness vs. Safety Dominance, human override unconditional + RQ5 forward reference). |
| 8 | Generalisation | `## Generalisation` subsection added before Deployment Challenges. Three-step recipe (define E → f(E) → R and A_AI(S)). TABLE V with two domain examples: emergency triage [19], industrial/transportation [21]. Formal properties transfer statement. |
| 9 | Threats to Validity | `# Threats to Validity` added as standalone section between Proposed Architecture and Conclusion. Four paragraphs: internal (threshold selection, rule completeness, prototype fidelity), external (single domain, engine type), construct (compliance ≠ quality, simulation fidelity), conclusion validity (20 scenarios vs. construction proof). |
| 10 | Conclusion | Conclusion fully rewritten with four-paragraph structure: (1) gap + consequences, (2) two contributions named explicitly, (3) Theorems 1–3 with completeness/consistency/effectiveness, (4) future work naming C0/C1/C2, RQ5, domain generalisation, IEC 61508, ML extension caveat. |
| 13 | Governance standards | Three sentences added before Formal Structure: NIST AI RMF [35] runtime tier mapping; IEC 61508/ISO 26262 graduated constraint precedent; Bloomfield & Rushby [20] deterministic guard at advisory scope level. Placeholder [35] replaced with full NIST AI 100-1 citation. |

---

### Current Proposed Architecture section structure

After this session, the Proposed Architecture section has nine subsections:

1. [Intro paragraph — standards + Engin & Hand]
2. `## Formal Structure` — TABLE III governance pair
3. `## Formal Properties` — Theorems 1–3 *(new)*
4. `## Algorithm Specification` — Algorithms 1–3 *(new)*
5. `## Computational Complexity` — TABLE IV *(new)*
6. `## The CAUTION Mode` — rationale for CAUTION mode
7. `## Domain Instantiation` — E = (w,r,m,o,v,t), Fig. 4 scenario
8. `## Generalisation` — TABLE V domain examples *(new)*
9. `## Deployment Challenges and Limitations` — 4 challenges + 3 limitations *(new)*

---

### Points still pending (require execution)

| Point | Title | What's needed | Source for design |
|-------|-------|---------------|-------------------|
| 5 | Experiments | Run 20-scenario evaluation under C0/C1/C2. Tabulate results — especially CAUTION rows where C0 and C1 produce DepartureTime/Duration but C2 does not. | `docs/canonical/evaluation-design-rq4.md` |
| 6 | Ablation | Run 4 ablation conditions against same 20 scenarios. Most critical: remove A_AI restriction (reduces to binary gate) to isolate Level 2 contribution. | `publications/active/journal-1/submissions/v1-initial-submission/manuscript.md` §12 |
| 11 | Figures | Redraw Figs 3 and 4 with colour coding (green/amber/red for SAFE/CAUTION/UNSAFE). Improve Fig. 3 labels: add G(S) and A_AI(S) on branching arrows. | ASCII art currently in manuscript. |
| 12 | LR methodology | Expand only if reviewer requests. Three-subsection text already exists in `docs/superpowers/plans/2026-07-16-ipsci-paper-v4-revision.md` §3.1–3.3. | — |

---

### Files modified this session

| File | Change |
|------|--------|
| `submissions/v2-post-review/manuscript-v2.5-submitted.md` | Points 1, 2, 3, 4, 7, 8, 9, 10, 13 applied — see table above |
| `supervisor-feedback-response.md` | Status updated for all nine completed points; summary table updated |
| `session-log.md` | Created (this file) |

---

### Known errors in submitted .docx (pre-existing — fix on next submission)

See `revision-notes.md` for full list. Key items: TABLE II reference numbers incorrect; [35] was blank (now filled with NIST AI RMF); acknowledgment placeholder still present.
