# Full Conference Reviewer Audit — IPSci 2026 `manuscript-v3.md`

**Date:** 2026-09-09
**Role adopted:** skeptical senior academic reviewer and scientific auditor
**Target:** `publications/active/ipsci-2026/submissions/v3-revision/manuscript-v3.md`
**Governing constraint:** *Do not improve the paper by inventing stronger science.* Where a reviewer concern could not be answered from existing evidence, it was recorded as a limitation.
**Baseline:** `data/conference-reviewer-audit/integrity-before.json` (19 protected artefacts)
**Manuscript:** `8443d121cd9ef18a` → `41404b98007a41e2` (624 → 631 lines)

---

## 1. Scope and method

The entire manuscript was read title through references before any assessment or edit. Every published empirical figure was then regenerated live from the canonical scripts rather than accepted from the text. Only after both steps was any edit made.

## 2. Reproduction of the canonical record

All three canonical generators were re-run during this audit.

| Quantity | Manuscript | Live re-run | |
|---|---|---|---|
| Level 2 binds (departure 05–09) | 5.81% / 4.48% | 5.81% / 4.48% | ✓ |
| Daylight UNSAFE hours | 1,262 / 455 | 1,262 / 455 | ✓ |
| Weather-driven share of UNSAFE | 10.9% / 6.4% | 10.9% / 6.4% | ✓ |
| Small vs big differ | 9.11% / 5.86% | 9.11% / 5.86% | ✓ |
| `g_o` daylight CAUTION | 98.71% / 97.66% | 98.71% / 97.66% | ✓ |
| `g_t` all-hours non-SAFE | 86.82% / 90.19% | 86.82% / 90.19% | ✓ |
| `g_r` daylight CAUTION | 1.48% / 2.70% | 1.48% / 2.70% | ✓ |
| TABLE VII (C0–C1 / C0–C2 / C3–C1 / C1–C2) | 42.88 / 48.69 / 0.00 / 5.81 | identical | ✓ |
| Transitions / scheduled / non-sched | 3,661 / 3,439 / 222 | identical | ✓ |
| Oscillations, hysteresis reduction | 26, 10.36% | 26, 10.4% | ✓ |
| Wave correlation | r = 0.953 | 0.9526 | ✓ |
| Register | 15 CONFIRMED / 9 REFUTED | identical | ✓ |

**Not a single published figure failed to reproduce.** For a paper rejected on "lacks the technical and empirical evidence", this is the strongest thing about it and it is currently under-sold.

## 3. Argument chain, reconstructed

Governance in safety-critical decision support is binary → binary gates treat marginal conditions as safe → operators over-rely on advice the data no longer supports → no reviewed architecture conditions *advisory scope* on classified environmental state → therefore specify `(G(S), A_AI(S))` → prove totality, monotonicity, safety dominance → instantiate for one site → measure that CAUTION is reached → measure that the closest precedent is output-equivalent to a binary gate.

The chain holds. Its one genuine break is at the penultimate link: the instantiation exercises the classifier and the governance pair, never the AI. That break is disclosed in three places in the body, and was — until this audit — not disclosed in the abstract.

## 4–7. Novelty, contribution, formalism, evaluation design

**Novelty** survives scrutiny. The claim is narrow and structural, and TABLE II codes it against nine named systems. The C3 = 0.00% measurement converts the review's assertion into a result; that is the paper's best move and it is honestly qualified as a comparison of structures, not systems.

**Contributions.** Review: SUPPORTED. Architecture: SUPPORTED (proofs verified). Empirical characterisation: SUPPORTED as a governance-layer characterisation — and the paper says exactly that, without inflation.

**Formalism.** The three proofs are correct by exhaustive case analysis; no error was found. Two typing irregularities were found (§9).

**Evaluation design.** Four conditions over a common record, with Level 1 and Level 2 cleanly isolated. The metric is admissible-set divergence, correctly described as a property of the governance layer.

## 8. Findings by classification

Full table: `data/conference-reviewer-audit/findings.csv` (14 findings).

- **R1 (critical, must fix):** 4 — three fixed, one recorded as a limitation.
- **R2 (major):** 5 — all fixed.
- **R3 (open/out of scope):** 3 — recorded, not patched.
- **R4 (project drift, not manuscript defects):** 2.

## 9. The four R1 findings

**R1-01 — the threshold evidence was uncited.** `g_o` carries 98.71% of all CAUTION decisions. Its two grounding sources — Yaakob et al. on Malaysian hull seakeeping, Jeong and Im on the 23-year Korean capsizing record — were named in prose, given no reference number, and absent from the reference list entirely. The paper's headline number rested on evidence a reviewer could not look up. Both sources exist in the project corpus with complete bibliographic records and their specific claims (6.54 m hull, Hs ≈ 1.875 m, 82% of 2017–2022 capsizings) were verified against the extraction notes before citing. Added as [39] and [40] at four sites.

**R1-02 — an insufficient-evidence code was read as a finding of no effect.** The paper stated that no architectural tactic has demonstrated formal positive safety impact. In Indykov et al. the score 0 means *insufficient evidence*, it is recorded for AT11 with AT4 ambivalent, and the remaining tactics are not assessed on Safety at all. The manuscript generalised across sixteen tactics from evidence about two, and converted an evidentiary gap into a substantive negative result. Narrowed in both abstract and body to the reading the source supports.

**R1-03 — the Conclusion contradicted the body.** The Conclusion asserted that no AI component, *regardless of technique*, can reliably self-restrict. The Mechanistic Basis section explicitly disclaims that generalisation, and the proposed system's own AI component is symbolic, so the LLM evidence does not even apply to it. Rescoped to match the body.

**R1-04 — `A_AI(CAUTION)` is stipulated, not derived.** *This one has no fix available and is now a limitation.* The Design Principle promises that a deployment instantiates the admissible sets by mapping recommendation types to evidential requirements. That mapping is never performed. `{Go, Delay}` is asserted, justified only by the judgement that the withheld types make heavier forecasting demands. The sharpest form of the objection: *Delay* is itself a temporal judgement, so a system that cannot say when to depart is arguably not equipped to say how long to wait. Nothing in the manuscript or Appendix C answers this. It is now stated in the reviewer's own terms as the first of four limitations.

## 10–15. Attack simulation

Twenty attacks were constructed with severity, evidence status, response availability and disposition: `data/conference-reviewer-audit/reviewer-attacks.csv`.

Nine were fixed. **Eleven were deliberately left unedited**, because the paper's existing treatment is already the defensible one and any change would have been advocacy rather than correction:

- **A07** — the `g_t` step (2 → 1,536) in a paper arguing against binary steps. The Threats paragraph names the tension, bounds it three ways, and concedes the rule is a policy choice no source establishes. That is the correct handling; smoothing it would be the error.
- **A12** — "5.81% is small". Result 1 states the rate plainly and Result 6 shows every comparator leaves those hours unrestricted. Arguing for significance would exceed the evidence.
- **A14** — "62.5% prediction hit rate is not a strength". The paper reports refutations with attribution rather than the ratio, which is right. Reframing would be spin.
- **A11, A13, A15, A17, A18, A19, A20** — each already carries an adequate in-text qualification.

## 16. One attack that dissolved on inspection

Result 5 compares a five-year maximum (2.60 m) against a 3.25-year maximum (1.84 m), which looks like a period mismatch manufacturing the resolution effect. Direct check of both archived series: the ERA5 peak occurs 2022-12-26, inside the MFWAM window, and both maxima lie in the 28,501-hour overlap. The comparison was sound; only the wording invited the attack. Now stated explicitly.

## 17. Two typing irregularities

Fixed: `E` was called an environmental observation vector containing `v` in Fig. 3 and Domain Instantiation, while the Formal Structure states `v` is a startup configuration and not an observation.

**Open (R3-01, recorded not patched):** Algorithm 1 and the Theorem 1 proof sketch admit a storm indication as an UNSAFE trigger for `g_r`, but `r` is declared over mm/hr and the proof partitions only that numeric domain. The phrase "where available" describes an unavailable required input that is silently skipped rather than mapped to ⊥ — coherent only if the storm indication is a declared exclusion, which the paper never says. This is a real formal defect. It is recorded rather than repaired, because repairing it means either changing the specification or asserting an exclusion the canonical record does not declare.

The related *empirical* fact was disclosable and has been disclosed: zero thunderstorm codes appear in five years, so that route never fires and `g_r` figures are lower bounds by an unknown margin (canonical F-11, previously absent from the manuscript).

## 18–30. Dimension scores

Twenty-four dimensions, pre- and post-edit: `data/conference-reviewer-audit/dimension-scores.csv`.

| | Pre | Post |
|---|---|---|
| STRONG | 9 | 14 |
| ADEQUATE | 11 | 10 |
| WEAK | 3 | 0 |
| CRITICAL | 1 | 0 |

Movements: Citation integrity CRITICAL → STRONG; Internal consistency WEAK → STRONG; Formal specification clarity, Contribution–evidence alignment WEAK → ADEQUATE; Evidence-class discipline and Limitations honesty ADEQUATE → STRONG.

## 31. Edits applied

Nine, all listed with rationale and an explicit invents-evidence check in `data/conference-reviewer-audit/edits-applied.csv`. **Every edit either narrows a claim, adds a disclosure, adds a limitation, or corrects a citation.** No edit strengthens a result, and no number in the manuscript changed.

## 32. What was deliberately not done

No experiment, citation, threshold, validation, user study, deployment result, significance test, hardware measurement or safety outcome was invented. No canonical result was altered. Two items were left visibly unfixed (the `g_r` storm typing; the Fig. 1/Fig. 2 image placeholders, which are a submission-packaging step) rather than papered over.

## 33. Project-file drift found in passing (R4)

Neither is a manuscript defect; the manuscript is correct in both cases.

- `CLAUDE.md` quotes `g_o` daylight CAUTION as 98.66% / 97.41%. `canonical_figures.py` and the manuscript both give **98.71% / 97.66%**.
- The trailer text of `canonical_figures.py` still reads "against a 22 kn threshold". The canonical threshold is **21.6 kn**.

## 34. Integrity

`integrity-after.json`: 19 protected artefacts checked, **one changed** — the manuscript, as intended. The prediction register, `canonical_gt.py`, the frozen solar implementation, the solar artefact, the USNO record and all eight canonical scripts are byte-identical. `__pycache__` swept.

## 35. Artefacts

All CSVs written through `csv.DictWriter` with `QUOTE_MINIMAL` and independently re-parsed with a strict field-count check.

```
PASS  dimension-scores.csv    fields=4 rows=24 sha=f7a06ad007a3fb0e
PASS  edits-applied.csv       fields=4 rows=9  sha=f24dad8d96ef1d70
PASS  findings.csv            fields=5 rows=14 sha=0b77c650ee796943
PASS  reviewer-attacks.csv    fields=6 rows=20 sha=83e0b9abea8ce918
```

## 36. Reviewer decision, pre-edit

**Major revision.** Not because the science was weak, but because a reviewer checking the reference list would have found the wave thresholds unciteable and the Indykov claim overstated — and would reasonably have generalised that to the rest.

## 37. Reviewer decision, post-edit

**Accept with minor revision**, conditional on embedding Fig. 1 and Fig. 2.

## 38. The residual weakness

The reasoning engine is unimplemented. The third contribution is therefore a characterisation of a governance layer, not an evaluation of AI advisory behaviour. This is now disclosed in the abstract as well as the body. It is honest, it is bounded, and it remains the most likely ground on which this paper is rejected again — v2.5's Review 3 rejected precisely here. Defensibility is not the same as acceptance, and no edit within this audit's remit could close that gap.

## 39. Standing pattern

The recurring project failure mode held once more: **a claim in the document with its justification somewhere else, and nothing comparing them.** 7.5 mm/hr, 22 kn, 116.07, "Meeus", P09 5,416 — and now Yaakob/Jeong named in prose but never in the reference list, and an "insufficient evidence" code read as a finding. Both were invisible to any check that did not open the source.

## 40. Outcome

**OUTCOME A — the manuscript is scientifically defensible as revised.**

Taking the stated target — *a skeptical reviewer should be unable to identify a claim that exceeds its evidence* — every claim now carries evidence of the right class and strength, or is labelled a policy choice, a lower bound, a limitation or an open item. The paper is narrower than it was this morning and stronger for it: two overstated claims withdrawn, one internal contradiction removed, one unanswerable objection promoted to a first-class limitation, and the empirical spine independently re-derived from scratch without a single discrepancy.

---

*Artefacts:* `data/conference-reviewer-audit/` — `findings.csv`, `reviewer-attacks.csv`, `dimension-scores.csv`, `edits-applied.csv`, `parser-test.json`, `integrity-before.json`, `integrity-after.json`, `build_artefacts.py`.

---
---

# Independent Reviewer Closure Repair

**Date:** 2026-09-09 (same day, continuing the audit branch)
**Trigger:** independent review of the audit above identified four reviewer-facing issues blocking acceptance of Outcome A.
**Scope:** narrow closure repair. No new audit, no new experiments, no canonical result altered.

## 1. Binary-premise correction

The independent review was right, and the error was one the original audit missed because it read the abstract for *overstatement* rather than for *self-contradiction*. The manuscript's own TABLE II lists five graduated architectures — Flehmig (3 levels), Kang (3 tiers), Ghaleb (3 regimes), Sahoo (5 bands), Baxi (K tiers) — while the abstract opened by asserting that existing governance mechanisms are *uniformly binary*. The paper refuted its own first sentence eight pages later.

The novelty claim never needed that premise, and is stronger without it. The defensible form: **graduated governance exists; graduated *advisory-scope* governance does not.** Graduation in the reviewed literature acts on oversight intensity, participation, execution, authority or an agent's action space — never on the recommendation set offered to a human decision-maker as a function of independently classified environmental safety state.

## 2. All affected locations

Seven sites carry a binary premise. Three were rewritten, four were classified accurate and retained — the distinction matters, because indiscriminate softening would have destroyed a correct claim. Full table: `binary-premise-classification.csv`.

| Location | Verdict | Action |
|---|---|---|
| Abstract, opening | False universal | Rewritten |
| Introduction, para 2 | False universal | Rewritten |
| Introduction, contribution para | Ambiguous, reads universal | Narrowed |
| Heading "Deterministic Safety Constraints: Binary by Construction" | Accurate — one named paradigm | Retained |
| Cross-paradigm synthesis | Accurate — already differentiates the two senses | Retained |
| Result 1 "a binary architecture…" | Accurate — the instantiated C1 baseline | Retained |
| Fisheries application level | Accurate — scoped to the domain | Retained |

## 3. `g_r` resolution, and why it preserves canonical semantics

**Option A. The decisive evidence reverses the expected answer.**

Before choosing, the canonical implementation was inspected. **All eight canonical scripts implement `g_r` as a two-argument function:**

```python
g_r(precip, wmo) = UNSAFE  if precip > 20.0 or wmo in (95, 96, 99)
                   CAUTION if precip > 10.0
                   SAFE    otherwise
```

`canonical_figures.py:127`, `condition_comparison.py:161`, `diagnostic_binding.py:101`, `compare_v1_v2.py:44`, `historical_replay.py:92`. The storm indication is not decorative prose — it is a live second argument in the code that produced **every published figure**.

This eliminates Options B and C:

- **Option B (remove the route)** would have deleted a signal the canonical replay genuinely consumes, making the conference paper describe a classifier other than the one that produced 5.81%. That *is* a change of canonical semantics.
- **Option C (declared exclusion)** would require inventing `D` membership. `D = {m}` in the replays; `r` is not excluded. Prohibited.

**Option A changes no semantics — it corrects a type declaration to describe semantics that already exist.** `g_r : ℝ≥0 × {0,1} → {SAFE, CAUTION, UNSAFE}`, with `κ = 1 ⇒ UNSAFE` for any rate. This follows the project's established C-0 principle: *evidence follows implementation, not the reverse* — the same rule applied to the Meeus/NOAA attribution.

**No empirical figure moves,** and the reason is instructive: `κ = 0` in all 43,848 hours (distinct WMO codes present: 0, 1, 2, 3, 51, 53, 55, 61, 63, 65 — no 95/96/99). The disjunct never fires. That inertness is precisely why the mis-typing survived undetected.

Updated in five places as required: domain declaration, classifier signature, Theorem 1 totality proof (now over the product domain), Algorithm 1, and the operational-resolution wording. The resolution semantics are stated honestly: `⊥` attaches to the rate, which is the required quantity, while an unsupplied `κ` resolves to 0 and yields the rate-only classification rather than a fault — so `κ` can only raise a classification, which is exactly why the `g_r` figures are lower bounds.

> **Appendix C carries the identical defect and was NOT changed here.** `appendix-c-formalisation.md:445` declares `g_r : ℝ≥0 → {SAFE, CAUTION, UNSAFE}` with the numeric partition called exhaustive, while adjacent prose states the WMO route is "formally part of the specification". The manuscript is now correct and Appendix C is not. This is recorded in `repository-drift.csv` as a **canonical** item requiring its own bounded repair. It was not performed here because silently amending Appendix C was explicitly out of scope.

## 4. Domain-independence wording

*"The case shown here is domain independent"* asserted the opposite of what the sentence went on to describe — a Kota Kinabalu fisheries case. Reworded to separate the re-instantiable governance structure from the domain-specific instantiation. The two already-bounded statements elsewhere ("domain-independent **at the structural level**", and the next-step to "validate the claim of domain independence **empirically**") were verified as correctly qualified and retained. No cross-domain empirical validation is claimed anywhere.

## 5. "Warranted scope" correction

The Conclusion claimed no path by which recommendations "exceed their **warranted** scope". With `A_AI(CAUTION)` acknowledged as stipulated, the theorem cannot support an epistemic reading. Replaced with **configured admissible scope**, plus an explicit sentence that the guarantee is structural and does not assert the configured set is the epistemically correct one. Search for `warranted` / `justified scope` / `evidence-supported scope` / `appropriate scope` now returns nothing in the body. The first limitation on the stipulated mapping is intact and is now cross-referenced from the Conclusion.

## 6. Manuscript hash

| | Hash | Lines |
|---|---|---|
| Pre-audit baseline | `8443d121cd9ef18a` | 624 |
| After main audit | `41404b98007a41e2` | 631 |
| **After closure repair** | **`27b33b846ae327cb`** | **634** |

## 7. Protected-state verification

19 protected artefacts re-hashed: **one changed — the manuscript.** Canonical generators re-run after the edits:

- Level 2 binds **5.81% / 4.48%** ✓
- Daylight UNSAFE **1,262 / 455** ✓
- `g_o` daylight CAUTION **98.71% / 97.66%** ✓ · `g_t` all-hours non-SAFE **86.82% / 90.19%** ✓
- Register **24 entries, 15 CONFIRMED / 9 REFUTED**, P09 actual **3,661**, P20 actual **1,529** ✓
- References: 40, zero orphan, zero dangling ✓

Model B canonical status, P20/P23/P24 as the only SDR-attributable flips, the P09 provenance chain, the P20 1,529 vs 455 scope distinction, UNSAFE as a governance state, unconditional human authority, COLREG as lighting relevance only, the NOAA/USNO evidence boundary, the medium-vessel 2.8 m interpolation, `A_AI(CAUTION)` derivation as outstanding, the unimplemented engine, and the characterisation-not-validation framing — all preserved.

## 8. Final open scientific items

1. `A_AI(CAUTION)` stipulated rather than derived — limitation 1, unanswerable from existing evidence.
2. Reasoning engine unimplemented — the third contribution is a governance-layer characterisation.
3. `g_m` never measured; `κ` never non-zero — all severity figures are lower bounds in two independent directions.
4. No incident record — correctness of the classifications is unestablished and unestablishable at this site.
5. **Appendix C `g_r` signature** — newly identified canonical typing defect, out of scope here.

## 9. Packaging checklist

`submission-packaging-checklist.csv` — Fig. 1 and Fig. 2 not embedded; the working-header checklist's Acknowledgment entry is stale (no placeholder text exists in the body); section numbering to be verified through docx conversion. None is a scientific closure blocker.

## 10. Stop-condition assessment

| Q | Question | Result |
|---|---|---|
| Q1 | Any claim that all governance is binary? | **NO** — verified by search |
| Q2 | `g_r` well-typed across domain, signature, Theorem 1, Algorithm 1, resolution? | **YES** — all five, without invented semantics |
| Q3 | Domain-agnostic specification distinguished from domain-specific instantiation? | **YES** |
| Q4 | Safety Dominance establishes only `AI(E) ⊆ configured A_AI(S)`? | **YES** — epistemic reading removed |

Decision-rule conditions: no false binary premise ✓; `g_r` resolved without invented semantics ✓; generalisation bounded ✓; theorem wording refers to configured admissible scope ✓; no protected scientific state changed ✓; REV-1 through REV-10 all CLOSED or RECORDED ✓.

**Outcome A retained.**

---

*Closure artefacts:* `closure-rev-items.csv`, `binary-premise-classification.csv`, `submission-packaging-checklist.csv`, `repository-drift.csv`, `parser-test-closure.json`, `build_closure_artefacts.py`.
