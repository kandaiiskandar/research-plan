# Canonical Documents Changelog

Track all significant changes to canonical documents here.

---

## 2026-09-08
- **Cause taxonomy semantic cleanup CLOSED** — [standalone report](cleanup-report-cause-taxonomy-2026-09-08.md). Appendix C and CLAUDE now define `reasons : Q → 𝒫({fault, hazard, policy})`; SAFE has ∅, concurrent triggers survive, and provenance never participates in governance. Exhaustive 12,288-case verification and frozen-file integrity checks pass. Runtime implementation remains outstanding.
- **Post-migration cause taxonomy audit** — [findings and proposal](finding-cause-taxonomy-audit-2026-09-08.md). Confirmed night-policy mismatch, SAFE fallback, mixed-trigger loss and missing context. Proposed explicit policy provenance with a set of active reasons; 12,288 abstract cases checked. Audit complete; canonical definition and governance unchanged, migration still outstanding.

## 2026-08-05
- **Reorganisation** — All canonical docs moved from `docs/` root to `docs/canonical/` per organize.md spec.

## Prior history
- See individual document git histories via `git log --follow <filename>`
