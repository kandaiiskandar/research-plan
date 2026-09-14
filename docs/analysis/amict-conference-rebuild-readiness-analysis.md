# AMICT Conference Rebuild — Task Readiness Analysis

**Date:** 2026-09-14
**Analyses:** `docs/tasks/AMICT CONFERENCE PAPER REBUILD — ARCHITECTURE TO EMPIRICAL EVALUATION.md`
**Status:** PRE-EXECUTION ANALYSIS ONLY. No task artefact has been created, no manuscript drafted, no existing file modified.
**Purpose:** establish whether the task is executable as written, verify its factual premises against the canonical record, and surface the decisions that must be made before drafting begins.

---

## 1. What the task actually is

A **retargeting job, not a research job.**

The IPSci 2026 / AMICT submission (v2.5) was rejected. Review 3: *"lacks the technical and empirical evidence necessary to establish its novelty, effectiveness, and safety claims."* Since submission, Journal 1 has closed P1–P4 (formal), F1–F3 (implementation fidelity) and E1–E4/E6 (empirical). The task instructs that this already-closed evidence be spent on a conference resubmission, with the frozen evidence base as a hard ceiling.

Approximately 80% of the instruction text is prohibition. The real deliverable is a **claim-discipline apparatus** — 11 artefacts and 8 audits — with a 6-page paper attached. The paper is the smaller half of the work.

**Unmentioned thread.** `publications/active/ipsci-2026/revision-notes.md` records that Review 2 reviewed a *different paper* (Twitter bot detection, TwiBot-22, AMICT Machine Intelligence/Cybersecurity track) and instructs raising this with the chairs. Discounting it leaves 1 accept-minor / 1 reject — borderline rather than clear rejection. The rebuild is correct regardless, but the chair query is an open administrative thread the task does not address.

---

## 2. Premise verification — every number in the task resolves

Each quantity asserted by the task was checked against its canonical artefact. Nothing was taken on trust.

| Task assertion | Canonical source | Result |
|---|---|---|
| 292 episodes · 454 advisory records · 244 with advisory · 162 UNSAFE gate-off | `data/journal1-layer3-prototype/batch5-fidelity-evaluation/fidelity-results.json`, `state-space-manifest.json` | VERIFIED |
| 32 SAFE / 260 CAUTION / 16 CAUTION-with-no-advisory | `batch5-fidelity-evaluation/reporting-repair.json` (carries the explicit 244-of-260 rationale) | VERIFIED |
| F1 = 0, F2 = 0, F3 = 0 | `fidelity-results.json`, `verification.json` | VERIFIED |
| 162 not inside the 292 denominator | `state-space-manifest.json` (`GATED_UNSAFE_cases` is a separate space) | VERIFIED |
| 43,848 hourly records ≈ 5 yr | `data/journal1-manuscript-evidence-sync/quantitative-provenance.csv` → `scripts/condition_comparison.py` | VERIFIED |
| C0↔C1 42.88 / C0↔C2 48.69 / C1↔C2 5.81 / C1↔C3 0.00 (PRIMARY) | same provenance CSV | VERIFIED |
| RESOLUTION 41.08 / 45.56 / 4.48 / 0.00 | same | VERIFIED |
| ΔL2 = 5.81 = 48.69 − 42.88 | provenance CSV, explicit derivation field | VERIFIED |
| 3,661 transitions · 3,439 scheduled · 222 non-scheduled · 26 oscillations · 10.36% | → `scripts/hysteresis_analysis.py` | VERIFIED |
| E3 mandatory scope = {E1, E2, E6}; `E4_RESOLUTION = NOT_REQUIRED_BY_CURRENT_E3_DESIGN` | `publications/active/journal-1/evaluation-specification.md` §13 | VERIFIED |
| E5 OPEN · `E5_HARNESS` CLOSED · MacBook = development-machine reference · Android `DEFERRED_MANDATORY` · H3 OPEN/UNSUPPORTED | evaluation-specification.md §11, §17 | VERIFIED |
| R-SAFE-001 DEFERRED; 32 SAFE episodes generated zero advisories | `batch5-fidelity-evaluation/`, `data/journal1-f1-f3-e5-status-repair/` | VERIFIED |
| Canonical theorem home = §6, Theorems 6.1/6.2/6.3; no 5.x | live Journal 1 manuscript: **0** occurrences of `Theorem 5.` | VERIFIED |

**Conclusion:** no numerical contradiction exists across canonical artefacts. **STOP condition 2 does not fire.**

### 2.1 Two refinements the task under-specifies

**(a) The 454 advisory records are 454 instances of one conclusion type.** `rule-activation-summary.csv` shows exactly four implemented rules — `R-CAUTION-001` … `R-CAUTION-004` — each selected 260 times, each emitting `Delay`, with 130 / 108 / 108 / 108 firings. There is no rule in the fidelity configuration capable of emitting `Go`, `DepartureTime` or `Duration`. This is consistent with what the task says, but the paper must not let "454 advisory records" read as advisory *diversity*.

**(b) `Property 5.1 / 5.2 / 5.3` in Journal 1 §5 is a legitimate separate object family, not theorem residue.** The numbering repair (`data/journal1-theorem-numbering-repair/verification.json`, 56 PASS / 0 FAIL, 18/18 negative controls discriminating) demoted `Theorem 5.1` and repaired 8 cross-references. The Property numbering is correct and must **not** be "fixed" by the formal-reference audit. The audit predicate is `Theorem 5.x`, not `5.x`.

**(c) One stale instruction survives.** `publications/active/journal-1/section-5-plan.md` L273 still instructs *"Use Section 5 numbering (Theorem 5.1, 5.2, 5.3) in the journal paper"*. Already logged as OOS-2 in the repair report and superseded. **Do not read it as guidance during this task.**

---

## 3. The real baseline is v3, not the rejected v2.5

The task says to use the rejected paper as "structural and historical baseline". The repository holds three distinct objects and conflating them will cause errors:

| Artefact | Role |
|---|---|
| v2.5 `.docx` | **What reviewers actually saw.** Contains six wrong TABLE II reference numbers, a blank `[35]`, and a placeholder acknowledgment |
| `submissions/v2-post-review/manuscript-v2.5-submitted.md` | Frozen `.md` transcription — **do not edit** |
| `submissions/v3-revision/manuscript-v3.md` | Working fork (2026-09-06, 634 lines, 40 references). Contains Formal Properties, Algorithm Specification, Computational Complexity, Generalisation, Deployment Challenges, Threats to Validity, and a full Empirical Characterisation with current post-SDR-001 figures |

**Reviewers saw none of the v3 material.** Review 3's objection was made against a version containing no formal proofs and no empirical results.

v3 is in substantially better condition than the task's §7 treatment table implies. It already carries 5.81 / 4.48, the four-condition comparison, C1↔C3 = 0.00%, the `g_w` two-activations/zero-bindings statement, the `g_m` lower-bound disclosure, the qualified hysteresis framing and the `g_t` discontinuity disclosure. It also passed a full adversarial reviewer audit (`docs/canonical/report-conference-reviewer-audit-2026-09-09.md`) in which **every published figure reproduced live from the canonical scripts**.

**Implication:** the rebuild is closer to a *fidelity-and-framing upgrade of v3* than a rewrite from v2.5. Treating v2.5 as the base would discard verified work.

### 3.1 Stale text in v3 that the rebuild must repair

These statements were true when written and are now superseded by Batch 5 (2026-09-11):

| Location | Stale text | Superseded by |
|---|---|---|
| v3 L391 | "The architecture **is being developed as** a formally specified prototype" | Layer 3 implemented; task §7 explicitly names this phrase for removal |
| v3 L527 | "**Prototype fidelity has not yet been verified empirically.** The reasoning engine is specified but not implemented, so AI(E) cannot be observed" | F1–F3 CLOSED PASS |
| v3 L527 | "the three-condition comparison of advisory output has not been run" | Fidelity evaluation run; note the replay is four-condition (C0–C3) and is a *governance-layer* comparison, not advisory output |
| v3 L537 | secondary metric "decision support utility" presented as available | `evaluation-specification.md` §9: utility construct is **OPEN — CONSTRUCT DEFINITION REQUIRED**; must not be offered as a mitigation |

This is a concrete, bounded repair list — good news for schedule, and it is the single highest-value input the rebuild inherits.

---

## 4. Constraints from project instructions the task does not restate

`CLAUDE.md` carries binding rules that the task file does not mention. Violating them would fail the audits even though the task text is silent.

**4.1 Superseded-figure blacklist.** Do not reintroduce: **7.72% / 5.98%** (provenance only, superseded fixed-clock `g_t`), 12.4%, 8.3%, lone 6.1%, 7.84% / 6.15%, **5,416** transitions (except as the deliberate P09 historical exception), 5,220, 5,201, `22 kn`, `7.5 mm/hr`, the `06:00 / 17:00 / 19:00` fixed clock and its 17:00–19:00 CAUTION band. Current authority is `scripts/canonical_figures.py` → `empirical-findings-2026-09-06.md` §0a.

**4.2 `g_w` two-number rule.** Always quote **2 activations, 0 bindings**. Never "never fires", never "wind is irrelevant". P16 is CONFIRMED; P01 is REFUTED.

**4.3 `g_m` lower-bound rule.** `m` is unmeasured; replays run `D = {m}` pinned at SAFE. **Every severity figure is a lower bound.** This must survive compression into 6 pages — it is a limitation, not a caveat that can be cut for space. The same applies to κ = 0 throughout the record, which makes every `g_r` figure a lower bound by an unknown margin.

**4.4 Mode-chattering.** The unqualified claim is withdrawn. Hysteresis is framed as a low-cost precaution, not a mitigation for observed instability, and the measured figures plus the hourly-resolution bound must appear alongside it. This matters because the task lists hysteresis as a *secondary result* — reporting 10.36% without the "precaution not requirement" framing would restate a withdrawn claim.

**4.5 Solar provenance naming.** The term is *NOAA-style low-precision solar-position formulation*, validated against USNO API v4.0.1. **Not** Meeus, NOAA/Meeus, Meeus/NOAA or NOAA/Spencer.

**4.6 Citation `[[notes]]` rule.** Any new document in this project citing a corpus paper must carry `[[notes]](path)` links, with path prefix by directory depth and URL-encoded filenames. This applies to `novelty-defence-matrix.md` — which is precisely a document full of corpus citations. From `data/amict-conference-rebuild/` the prefix is `../../notes/`. Master map: `docs/canonical/citation-notes-map.md`.

**4.7 Formal model consistency.** `docs/canonical/appendix-c-formalisation.md` is the single source of truth. Write `f(E)` only for the ideal case and `F_{D,τ}` for deployed behaviour. Do not reintroduce `g_v`. The classifier is five terms, not six.

**4.8 Novelty wording tension — reconcilable, but needs explicit handling.** `CLAUDE.md` frames the CAUTION mode as one "which no existing architecture implements". The task prohibits "first-ever", "globally novel", "uniquely novel". These are not in conflict *provided* the claim stays scoped to the review, as v3 L103 already does: *"no architecture identified"* from 72 papers plus three systematic reviews covering 532 primary references. The rebuild must preserve that scoping. An unscoped restatement of the house framing would fail overclaim audit B.

---

## 5. Blockers and open decisions

### B1 — The AMICT template is not in the repository (borderline STOP condition 5)

Task §12 makes the template the formatting authority. No `.docx`, `.dotx`, `.tex` or `.cls` template exists anywhere in the tree; `publications/templates/` holds only `journal-template.md` and `response-to-reviewers-template.md`.

The **page limit is establishable**: `docs/superpowers/specs/2026-07-27-amict-compression-design.md` records *"AMICT conference, hard 6-page limit (references included)"* with a per-section page allocation. But that is a July 2026 spec for the *previous* cycle.

**Needed:** the template file, and confirmation that 6 pages still holds for the new cycle. Without the template the manuscript can be authored in `.md` but cannot be finalised to format — which is consistent with the task's own terminal status (`DRAFT_COMPLETE_PENDING_FINAL_FORMAT_AND_SUBMISSION_REVIEW`), so this need not block drafting.

### B2 — C2 is the thinnest contribution and the most exposed (not a STOP condition; a framing decision)

The executable-fidelity contribution rests on a state space in which:

- the SAFE rule set is **empty** (R-SAFE-001 DEFERRED) — 32 SAFE episodes, zero advisories;
- all four implemented rules are CAUTION rules;
- all 454 advisory records carry the single conclusion type `Delay`;
- containment is therefore demonstrated **only on the restrictive side** — nothing was ever generated that a narrower state would have had to suppress.

The task's permitted wording is honest and correctly fenced. The risk is strategic, not disciplinary: a reviewer who rejected v2.5 for weak validation may read C2 as close to vacuous — *"you proved a rule engine containing only Delay rules emits only Delay"*.

**Decision required before drafting:** does C2 stand as a headline contribution, or fold into C1 as an implementation-conformance subsection, with C3 (the empirical replay) promoted? The audits will not catch this because it is a framing choice, not a claim violation.

### B3 — Novelty-audit corpus coverage is uneven

Corpus file-hit counts across the five mandated families:

| Family | Local coverage | Assessment |
|---|---|---|
| B — runtime assurance / Simplex | 22 / 7 files | Adequate |
| C — shielding / action masking | 50 / 1 files | Shielding adequate; **action masking thin** |
| A — selective prediction / abstention / deferral | 1 / 13 files | **Thin on selective prediction** |
| D — adjustable autonomy / mixed-initiative | 2 / 2 files | **Thin** |
| E — graduated runtime governance | Covered via Flehmig, Kang, Ghaleb, Sahoo, Baxi in v3 TABLE II (9 named systems) | Adequate |

Families A and D are where a materially equivalent prior mechanism would most plausibly surface, and they are the least covered locally. The task permits bounded external sourcing for exactly this purpose. **This is where STOP condition 1 would fire, if it fires at all.**

### B4 — Output path is ambiguous

Task §15 says "the appropriate conference submission directory" and forbids overwriting the rejected historical submission. Two readings:

1. `publications/active/ipsci-2026/submissions/v4-amict-rebuild/` — keeps review history contiguous under the existing tracker;
2. a new venue directory — cleaner if the venue is genuinely being changed.

Venue naming is muddled in the repository: IPSci appears to be a track within AMICT (Review 2 names the "AMICT Machine Intelligence/Cybersecurity track"). **Recommendation:** option 1, unless retargeting to a different conference is intended. Requires a decision.

### B5 — The RQ set leans formal, given the rejection reason

- **RQ1** ("can the mechanism enforce state-conditioned containment") is answered by Theorem 6.3 **by construction** — a formal question, not an empirical one.
- **RQ2** is bounded by the fidelity state space described in B2.
- **RQ3** is the only unambiguously empirical question. RQ4 (hysteresis) is optional.

For a paper rejected on empirical grounds, one genuinely empirical RQ out of three is worth a deliberate decision rather than inheritance. Note this is a presentation question — the underlying evidence is what it is, and inventing more is prohibited.

---

## 6. Stop-condition assessment

| # | Condition | Assessment |
|---|---|---|
| 1 | Materially equivalent prior work | **Unresolved until the novelty audit runs.** Highest residual risk in families A and D (see B3) |
| 2 | Numerical conflict across canonical artefacts | **Does not fire** — all figures reconcile (§2) |
| 3 | Old paper vs newer authority irreconcilable | **Does not fire** — conflicts are a bounded stale-text list (§3.1), all resolvable in favour of newer authority |
| 4 | Reference cannot be verified | **Does not fire on current evidence** — v3's 40 references survived the 2026-09-09 audit, which added and verified [39] and [40] |
| 5 | Page limit cannot be established | **Borderline** — 6 pages sourced from a prior-cycle spec; template absent (B1) |
| 6 | Claim requires a new experiment | **Does not fire** if C2 stays inside the permitted wording |
| 7 | Claim depends on E5 / H3 / human study / R-SAFE-001 | **Does not fire** if E5 is kept out of the RQ set as §6 instructs |

---

## 7. Proposed execution order

1. **Novelty audit first.** It gates everything and can terminate the paper. Families A and D need bounded external sourcing. Output: `novelty-defence-matrix.md` with `[[notes]]` links.
2. **Contribution freeze** — with the B2 question (C2 headline vs subsection) settled explicitly and recorded, not left implicit.
3. **Evidence boundary + quantitative provenance** — build these *before* prose, so the draft is written against a fixed number set rather than audited into compliance afterwards. Seed from `data/journal1-manuscript-evidence-sync/quantitative-provenance.csv`.
4. **Prior-paper change map** against **v3** (not v2.5), incorporating the §3.1 stale-text list.
5. **Outline, then draft** in `.md`, authored against the 6-page allocation.
6. **All eight audits last**, against finished text — with the §2.1(b) caveat that the formal-reference audit predicate is `Theorem 5.x`, not `5.x`.

---

## 8. Verdict

The task is **executable and internally consistent**. Its factual premises verify without exception against the canonical record; stop conditions 2, 3, 4, 6 and 7 are clear on present evidence.

Three things need resolving before drafting:

- **B1** — supply the AMICT template and confirm the 6-page limit (blocks final format, not drafting);
- **B2** — decide whether C2 is a headline contribution or a subsection (blocks the contribution freeze);
- **B4** — confirm the submission directory (blocks artefact creation).

**B3** is the genuine scientific risk and resolves only by running the novelty audit. **B5** is a presentation decision that can be taken alongside the contribution freeze.

Authoring convention for this task: **all artefacts and the manuscript are created in `.md` first.** Format conversion is deferred to the submission step, consistent with the task's terminal status `DRAFT_COMPLETE_PENDING_FINAL_FORMAT_AND_SUBMISSION_REVIEW`.

---

## 9. Files inspected

Read-only. Nothing in this analysis modified any existing file.

- `docs/tasks/AMICT CONFERENCE PAPER REBUILD — ARCHITECTURE TO EMPIRICAL EVALUATION.md`
- `publications/active/ipsci-2026/README.md`, `revision-notes.md`
- `publications/active/ipsci-2026/submissions/v3-revision/manuscript-v3.md`
- `publications/active/journal-1/evaluation-specification.md`
- `publications/active/journal-1/submissions/v1-initial-submission/manuscript.md`
- `data/journal1-layer3-prototype/batch5-fidelity-evaluation/` (`fidelity-results.json`, `state-space-manifest.json`, `reporting-repair.json`, `rule-activation-summary.csv`, `boundary-checks.json`)
- `data/journal1-manuscript-evidence-sync/quantitative-provenance.csv`
- `data/journal1-theorem-numbering-repair/` (`report.md`, `verification.json`)
- `docs/canonical/report-conference-reviewer-audit-2026-09-09.md`
- `docs/superpowers/specs/2026-07-27-amict-compression-design.md`
- `CLAUDE.md`
