# Report — Post-SDR-001 Cause Taxonomy Semantic Cleanup

**Date:** 2026-09-08  
**Status:** CLOSED at canonical specification level.  
**Authority:** SDR-001 APPLIED — MODEL B CANONICAL.  
**Scope:** Bounded semantic/provenance cleanup; no new SDR, classifier redesign, replay, prediction re-resolution or Publication Consistency Audit.

## 1. Previous contract and defects

The pre-cleanup canonical contract was `cause : Y → {fault, hazard}`: fault for any required non-excluded bottom, hazard otherwise. This is historical here, not a second active definition.

| Audit defect | Resolution |
|---|---|
| CT-1: valid night fell into hazard | Valid nighttime explicitly contributes policy. |
| CT-2: SAFE also fell into hazard | SAFE has an empty reason set; no residual hazard branch. |
| CT-3: concurrent triggers lost | Independent membership predicates preserve every active label. |
| CT-4: UNSAFE conflated night and time failure | Trace retains clock/date/solar validity; failed resolution cannot establish policy. |
| CT-5: Y signature hid context | Domain Q explicitly carries evaluated component/context information. |
| CT-6: hazard was unbounded | Defined positively as a valid environmental non-SAFE band, not danger proven. |

The earlier [audit](finding-cause-taxonomy-audit-2026-09-08.md) remains unchanged as the record preceding this cleanup.

## 2. Final canonical trace and reason contract

**`reasons : Q → 𝒫({fault, hazard, policy})`.**

q ∈ Q is an explanatory abstraction over existing resolution/classification information, restricted to completed and internally consistent evaluated traces. It is not a new environmental state variable, replacement for Y, classifier input, or implemented runtime data structure.

The trace names D, applicable resolution/freshness context τ, configured v, component identities, exclusions, validity/fault status, component severities and the existing aggregate S. Environmental entries retain readings and applicable bands; g_o retains vessel context. Time retains clock/date validity, solar lookup validity, used boundaries and artefact identity, and resulting g_t. Unevaluated dependencies following an earlier failure are not asserted valid.

- **fault:** iff any required non-excluded component or required time dependency fails resolution. Missing, invalid and applicable stale observations qualify. Failure of clock/date/solar resolution does not establish night.
- **hazard:** iff a valid non-excluded component in {w,r,m,o} is CAUTION or UNSAFE. This records a band crossing, not physical danger, harm, navigation prohibition or causal evidence beyond the classifier.
- **policy:** iff valid canonical clock/date/solar inputs establish time before sunrise or at/after sunset. The detailed trigger may be `nighttime_advisory_policy`.
- **Empty set:** no active restriction gives ∅. For consistent canonical traces, reasons(q) = ∅ iff S = SAFE.

Membership predicates are independent. Lower-severity environmental restrictions remain present when another component determines UNSAFE. This is active-trigger provenance, not exclusive binding attribution. Band evidence and conservative threshold choices remain separate details; in particular medium-vessel interpolation does not become a nighttime-policy label.

Exclusions contribute no reason even when raw data are absent; existing exclusion-before-fault order remains. Missing unconsumed swell period does not fault g_o. Missing v and ill-formed D refuse startup without a classified state or reason set. No startup failure was converted to a runtime fault.

## 3. Governance invariance

For every existing resolvable input under valid startup configuration, compute the unchanged `S = F_{D,τ}(obs,v)`. Annotation gives `(S, reasons(q))`; projection onto the first coordinate is S by construction. Thus G(S), A_AI(S) and RS(S) are pointwise identical. Reasons cannot alter resolution, max-severity, state order, rule selection, gate state, admissible recommendation types or human authority.

C.7.2 still proves Safety Dominance through the same cases on S under A1–A4. Fault, environmental UNSAFE, nighttime policy and mixed reasons all enter the existing UNSAFE case. Environmental CAUTION enters the existing CAUTION case. No reason predicate occurs in the proof's governing case selection. This is specification invariance; an unimplemented engine's fidelity is not asserted.

## 4. Explicit required-case verification

All other environmental inputs are SAFE unless named. Clock/date/solar are valid unless the case names a failure.

| Case | State | Reasons | Result |
|---|---|---|---|
| daylight + all weather SAFE | SAFE | ∅ | PASS |
| daylight + wave CAUTION | CAUTION | {hazard} | PASS |
| daylight + wave UNSAFE | UNSAFE | {hazard} | PASS |
| valid night + weather SAFE | UNSAFE | {policy} | PASS |
| valid night + wave CAUTION | UNSAFE | {hazard, policy} | PASS |
| valid night + wave UNSAFE | UNSAFE | {hazard, policy} | PASS |
| wave fault + daylight | UNSAFE | {fault} | PASS |
| wave fault + valid night | UNSAFE | {fault, policy} | PASS |
| wind fault + wave UNSAFE + valid night | UNSAFE | {fault, hazard, policy} | PASS |
| clock failure + weather SAFE | UNSAFE | {fault} | PASS |
| date failure + weather SAFE | UNSAFE | {fault} | PASS |
| solar lookup failure + weather SAFE | UNSAFE | {fault} | PASS |
| excluded m absent + daylight SAFE | SAFE | ∅ | PASS |
| exact valid sunrise | SAFE | ∅ | PASS |
| exact valid sunset | UNSAFE | {policy} | PASS |
| missing vessel | startup refused | no classified record | PASS |
| excluded time | startup refused | no classified record | PASS |

Exact-boundary cases use the frozen 2024-03-20 sunrise/sunset decimal-hour values and the canonical half-open comparison. They verify the abstract specification, not production g_t execution. Clock, date and lookup failures are separate named examples of the same required-time-failure abstraction.

## 5. Exhaustive verification

**PASS: 12,288 cases** = 16 environmental exclusion sets × 4⁴ environmental statuses × 3 time statuses. All eight subsets of {fault,hazard,policy} occurred. Additional explicit checks total **17**, including the requested 13 scenarios, expanded dependency failures, and startup refusals.

The checker verifies state projection, G, A_AI, abstract state-indexed RS identity, SAFE/empty equivalence, fault ⇒ UNSAFE, all eight subsets, invariance to changing excluded raw inputs, and valid night versus time-resolution failure. The RS check uses the existing three rule-set identities; it does not pretend to execute a rule engine. The invariance checks encode the annotation contract and supplement the formal argument, not an empirical replay of the classifier.

Reproduce from repository root:

```sh
python3 data/cause-taxonomy-cleanup/verify_semantics.py
python3 data/cause-taxonomy-cleanup/check_integrity.py
```

Artefacts: [verification source](../../data/cause-taxonomy-cleanup/verify_semantics.py), [verification results](../../data/cause-taxonomy-cleanup/verification.json), [integrity checker](../../data/cause-taxonomy-cleanup/check_integrity.py). These standalone checkers live with cleanup evidence, not in production scripts/.

## 6. Authoritative document changes

**Appendix C was edited first.** C.2.0.8 replaces the scalar taxonomy and closes its OPEN note with the trace/reason contract. C.1 cross-references overlapping routes and bounds fault wording to the failed input, allowing other observations to remain valid. C.7.2 A3 and explanatory paragraph cover policy and mixed sets without rewriting theorem cases. C.8.2 specifies the annotation without claiming implemented recording. The symbol summary replaces cause with q/Q and reasons.

**CLAUDE.md:** the active type table and accompanying guidance now agree with Appendix C. The explicit rule is: “Provenance reasons are annotations only and never participate in governance.” Trace context, exclusions, startup, bounded labels, concurrency and runtime limits are stated. The canonical changelog links this closure while preserving the preceding audit entry as history.

## 7. Active-document sweep and historical preservation

The sweep searched textual files in docs/, publications/active/ and CLAUDE.md for the whole word cause, the old two-label set, fault/hazard variants in both orders, “fault or hazard”, “hazard or fault”, “exactly one cause”, and “single cause”. Ordinary causal-language hits were also classified; they are not provenance definitions.

The pre-report final sweep records **103 hits**: 26 active canonical, 2 superseded/provenance, 74 historical, 1 archived. [Per-hit inventory](../../data/cause-taxonomy-cleanup/active-document-sweep.csv) contains path, line, classification, relevance, disposition and exact text. It is a snapshot after canonical edits and before adding this report.

Only Appendix C and CLAUDE carried active scalar contracts requiring replacement. Remaining active hits are bounded provenance wording, changelog references or ordinary causal prose. The new report quotes the old contract solely in §1 as pre-cleanup history. Active manuscripts contained no scalar contract needing edits.

C-8, the earlier cause audit, SDR-001 reports, session logs, archived documents and all submitted/working manuscripts were preserved byte-for-byte. Historical “OPEN” and old-type statements describe their original task boundary; the new canonical definition and this closure supersede them prospectively. No retroactive rewrite was performed.

## 8. Integrity evidence

The pre-cleanup snapshot was captured before editing Appendix C. It hashes all existing docs, active publications, Python scripts, solar artefacts, CLAUDE and the prediction register. The after-check allows only Appendix C, CLAUDE and the changelog to differ among these files. All other captured files remain byte-identical.

| Frozen item | SHA-256 before | SHA-256 after | Result |
|---|---|---|---|
| `data/prediction-register.csv` | `5574b88ea65168b6ef5e308629f3eb14fb70f8688a592fde279103ea4b37eae6` | `5574b88ea65168b6ef5e308629f3eb14fb70f8688a592fde279103ea4b37eae6` | MATCH |
| `scripts/canonical_gt.py` | `b330bf9f94e848aad282a71d226c85c7e73f4ec8c0f2f8c88bfd7112b6e9a577` | `b330bf9f94e848aad282a71d226c85c7e73f4ec8c0f2f8c88bfd7112b6e9a577` | MATCH |
| `data/solar/solar-events-daily.csv` | `057c46a19d0e8ea7956cdc38ae3d7615cf43cf800e7bc33ab286dfdc20ce1894` | `057c46a19d0e8ea7956cdc38ae3d7615cf43cf800e7bc33ab286dfdc20ce1894` | MATCH |
| `scripts/sensitivity/solar.py` | `3b7dc371ebe5931b3336f9982c5806a06a515dc2032569f5da7720470c1ec36c` | `3b7dc371ebe5931b3336f9982c5806a06a515dc2032569f5da7720470c1ec36c` | MATCH |
| `docs/canonical/empirical-findings-2026-09-06.md` | `667161e288d5e403ac068edab31b21c86c8694ca6fa6b35288ae2096f685b556` | `667161e288d5e403ac068edab31b21c86c8694ca6fa6b35288ae2096f685b556` | MATCH |

Full manifests: [before](../../data/cause-taxonomy-cleanup/integrity-before.json), [after](../../data/cause-taxonomy-cleanup/integrity-after.json). **173 existing files** match their pre-cleanup hashes. All Python files under scripts/ and all files under data/solar/ match; no canonical classifier code or solar calculation changed. Diff review confirms no formal classifier, threshold, state-order, exclusion or fail-safe definition changed.

The canonical empirical headline row remains **PRIMARY 5.81% / RESOLUTION 4.48%**, byte-identical. The register remains **24 entries: 15 CONFIRMED / 9 REFUTED**. A whole-file hash match covers every actual, status, scope, text and band, including original ordering and bytes. The SDR-001 attribution remains three of seven flips: P20, P23, P24. No prediction was re-resolved and no replay was run.

## 9. Runtime boundary and wording

No implemented cause function or consumer exists in the inspected scripts/. This cleanup implements the **specification contract**, not a production logger, UI display or reasoning engine. A future implementation must capture the evaluated trace and validity context, rather than reconstruct reasons from S alone.

Canonical example wording is “AI advisory unavailable: nighttime policy applies.” For a simultaneous wave trigger it adds “Wave reading exceeds the configured band.” It does not claim unsafe-to-sail, legal prohibition or certain harm. Human authority remains unconditional.

Reason labels overlap. Neither this cleanup nor its artefacts introduce reason percentages summing to 100%, and the existing weather-driven UNSAFE metric retains its original definition.

## 10. Files modified and added

Existing files modified in this task:

- `docs/canonical/appendix-c-formalisation.md`
- `CLAUDE.md`
- `docs/canonical/CHANGELOG.md` (already had the previous audit entry at task start; that entry is preserved)

New files:

- `docs/canonical/cleanup-report-cause-taxonomy-2026-09-08.md` (this report)
- `data/cause-taxonomy-cleanup/verify_semantics.py`
- `data/cause-taxonomy-cleanup/verification.json`
- `data/cause-taxonomy-cleanup/check_integrity.py`
- `data/cause-taxonomy-cleanup/integrity-before.json`
- `data/cause-taxonomy-cleanup/integrity-after.json`
- `data/cause-taxonomy-cleanup/active-document-sweep.csv`

The earlier audit Markdown and audit-check JSON were already present at task start and remain unchanged. No runtime module or manuscript was edited.

## 11. Closure criteria

| # | Criterion | Evidence / result |
|---|---|---|
| 1 | Scalar contract no longer canonical | Appendix C and CLAUDE checks PASS |
| 2 | SAFE explicitly has no active reason | C.2.0.8 and verification PASS |
| 3 | Valid night maps to policy | Explicit and exhaustive cases PASS |
| 4 | Environmental non-SAFE maps to hazard | Positive membership predicate; PASS |
| 5 | Resolution failure maps to fault | Required-input/time cases PASS |
| 6 | Concurrent triggers retained | All eight subsets represented; PASS |
| 7 | Exclusion semantics unchanged | Excluded-input invariance; PASS |
| 8 | Startup semantics unchanged | No classified result for failed startup; PASS |
| 9 | Trace/context explicit | Q definition names all required dependencies; PASS |
| 10 | Governance reason-independent | Projection argument and G/A_AI/RS checks PASS |
| 11 | Appendix sections agree | C.1, C.2.0.8, C.7.2, C.8.2 and summary reviewed; PASS |
| 12 | CLAUDE agrees | Type table and guidance reviewed; PASS |
| 13 | Active canonical references consistent | Per-hit sweep and scalar-contract checks PASS |
| 14 | Historical records retained | Before/after hashes PASS |
| 15 | Exhaustive verification | 12,288 cases PASS |
| 16 | No classifier changes | Script hashes and formal diff PASS |
| 17 | No threshold changes | Script hashes and formal diff PASS |
| 18 | No prediction changes | Register hash PASS |
| 19 | 5.81% / 4.48% unchanged | Exact headline row and findings hash PASS |
| 20 | 15 / 9 unchanged | 24 CSV rows counted; register hash PASS |

## 12. Remaining work outside this task

The known conference Methods sentence still says 23 confirmed / 1 refuted, and prototype/Deployment Challenges retain old hysteresis figures. These remain for the next Publication Consistency Audit; no manuscript-wide audit or cleanup was begun. Older session-log migration status also remains historical, with C-8 as the current authority.

Solar publication citation closure, the later full conference reviewer audit, ageᵢ instantiation, anticipatory notification and Layer 3 implementation remain outside scope. Runtime trace capture and reason-set consumption are future implementation work, not a blocker to closure of this semantic specification repair.

# `CAUSE TAXONOMY CLEANUP CLOSED — PROVENANCE SEMANTICS CANONICAL`
