# Journal 1 Submission Tracking

## Venue Details
- **Journal:** Safety Science (Elsevier)
- **Fallback 1:** Artificial Intelligence Review (Springer)
- **Fallback 2:** AI & Ethics (Springer)
- **Type:** Full research article
- **Paper title (working):** A Formally Verified Runtime AI Governance Architecture Based on Graduated Safety-State Gating
- **Status:** Research design phase

## Relationship to Conference Paper
This is **not** an extension of the IPSci 2026 / AMICT conference paper. It is an independent paper that treats the same architecture as the subject of formal analysis, algorithmic specification, prototype implementation, and experimental validation.

| | Conference (IPSci 2026) | Journal 1 (this paper) |
|---|---|---|
| Contribution | New architecture | Architecture + theory + implementation + evidence |
| Sections overlapping | — | Sections 1–5 |
| Sections new | — | Sections 6–14 (formal proofs, algorithms, experiments, ablation) |

## Deadlines
| Milestone | Date | Status |
|-----------|------|--------|
| Research design confirmed (RQs, hypotheses, metrics) | 2026-08-31 | ⏳ |
| Module 1: Formal theory complete | 2026-09-30 | ⏳ |
| Module 2: Architecture specification + diagrams | 2026-09-30 | ⏳ |
| Module 3: Algorithms + complexity analysis | 2026-10-31 | ⏳ |
| Module 4: Experimental design + data ready | 2026-11-30 | ⏳ |
| Experiments run + results | 2027-01-31 | ⏳ |
| Full manuscript draft | 2027-02-28 | ⏳ |
| Supervisor review | 2027-03-31 | ⏳ |
| Submit to Safety Science | 2027-04-30 | ⏳ |
| Expected review decision | 2027-07-31 | ⏳ |
| Revision and resubmission | 2027-09-30 | ⏳ |
| Expected acceptance | Late 2027 | ⏳ |

## Version History
| Version | Date | Status | Notes |
|---------|------|--------|-------|
| v1 | — | In progress | Initial manuscript draft |

## Reviewer Feedback Summary
| Reviewer | Decision | Major Issue | Our Response Status |
|----------|----------|-------------|---------------------|
| — | — | Awaiting submission | — |

## Traceability to Thesis Chapters
| Publication Section | Thesis Chapter | Notes |
|---------------------|----------------|-------|
| Introduction / problem framing | Chapter 1 | Expanded in thesis |
| Literature review / theme analysis | Chapter 2 | This paper IS the lit review |
| Gap argument (binary governance) | Chapter 2 Sections 2.7–2.9 | Direct mapping |
| Review methodology (PRISMA) | Chapter 3 | Same protocol, more detail in thesis |

## Key Contributions (distinct from conference paper)
1. Formal proof of the Safety Dominance Property: AI(E) ⊆ A_AI(S) — holds by construction
2. Algorithmic specification of the full governance pipeline (4 algorithms with complexity analysis)
3. Prototype implementation in a low-resource deployment context (Malaysian coastal fisheries)
4. Experimental evidence: graduated vs. binary-gated vs. ungated baseline comparison
5. Ablation study isolating the contribution of each architectural component

## Existing Assets to Draw From
| Asset | Location |
|-------|----------|
| Formal model (canonical) | `docs/canonical/appendix-c-formalisation.md` |
| Architecture illustration | `docs/canonical/architecture-illustration.md` |
| Layer 3 enforcement + proof sketch | `docs/canonical/justification-layer3-enforcement.md` |
| RQ4 evaluation design (3-condition comparison) | `docs/canonical/evaluation-design-rq4.md` |
| Conference paper (do not copy, use as reference) | `publications/active/ipsci-2026/submissions/v2-post-review/manuscript.md` |
| Literature corpus (72 papers) | `papers/review-plan.md`, `papers/comparison-table.md` |
| Weather/marine data | `data/` |

## Next Actions (research design phase)
- [ ] Confirm RQs and hypotheses (see `research-design.md`)
- [ ] Confirm metrics are operationalised
- [ ] Confirm data in `data/` is sufficient for experiments
- [ ] Start Module 1: Formal theory (proofs)
- [ ] Start Module 2: Architecture diagrams (publication quality)
- [ ] See `research-design.md` for full module plan and sequencing
