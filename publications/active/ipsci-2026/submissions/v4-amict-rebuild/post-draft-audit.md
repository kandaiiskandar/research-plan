# Post-Draft Scientific and Reviewer Audit — AMICT Manuscript V4

**Date:** 2026-09-14
**Task:** `docs/tasks/AMICT MANUSCRIPT V4 — POST-DRAFT SCIENTIFIC AND REVIEWER AUDIT.md`
**Audited:** `manuscript.md` (this directory)
**Mode:** adversarial reviewer audit with authority for surgical correction

---

## 1. Executive verdict

    POST_DRAFT_AUDIT              = CLOSED
    MANUSCRIPT_V4_SCIENTIFIC_TEXT = REVIEWER_READY
    FORMAT_READY                  = NO

All seven priority checks named by the task were confirmed as genuine defects. Four further defects were found during the audit. All twelve have been corrected surgically. No stop condition fired, and no correction touched architecture, comparator definitions, thresholds or evidence.

**The finding that matters most.** The draft passed a nineteen-item disclosure check, a prohibited-phrase scan and a reference-integrity check, and still carried an unscoped literature claim in its most-read sentence, a citation that did not support its label, and a self-referential pointer to unpublished companion work that constituted a double-blind leak. **A clean mechanical audit is not evidence of a reviewer-ready manuscript.** The two gates were correctly kept separate.

---

## 2. Disposition counts

| Disposition | Count |
|---|---|
| REVISE | 10 |
| REMOVE | 1 |
| PASS_WITH_SCOPE (retained after refinement) | 1 |
| OPEN | 4 |
| **Submission-blocking after correction** | **0** |

    CLAIMS_REVISED = 10
    CLAIMS_REMOVED = 1
    OPEN_ITEMS     = 4

---

## 3. Submission-blocking defects

**None remain.** Three were blocking before correction:

| ID | Defect | Type | Why blocking |
|---|---|---|---|
| PC1 | Abstract asserted absence from "the AI governance literature" | `SCOPE_OVERCLAIM` | Unscoped absence claim in the most-read sentence, contradicting the frozen novelty boundary |
| PC3 | "three large-scale systematic reviews" attached to `[1]–[6]` | `CITATION_MISMATCH` | Exactly one of the six cited sources is a systematic review; a reviewer checking the citation would find the label unsupported |
| PC4 | "Proofs are given in the companion journal treatment" | `DOUBLE_BLIND_RISK` | Pointed reviewers to unpublished companion work by the same authors; also made a formal claim depend on inaccessible material |

All three are corrected.

---

## 4. Priority checks and corrections

### PC1 — Abstract literature scope · `SCOPE_OVERCLAIM` · REVISE

> **was:** "…but has not been given a corresponding operational treatment in the AI governance literature."
> **now:** "…but we did not identify a corresponding operational treatment in that literature."

Scope restored to search-outcome language, matching the frozen gap statement.

### PC1b — Abstract prevalence claim · `SCOPE_OVERCLAIM` · REVISE *(found during audit)*

The opening sentence carried the same defect class as PC8, in the Abstract, and was not on the task's list.

> **was:** "AI decision support in safety-critical settings is usually governed by a single binary question…"
> **now:** "Governance of AI decision support in safety-critical settings is commonly framed in the reviewed literature as one binary question…"

### PC2 — TCAS human-authority clause · `SCOPE_OVERCLAIM` + `LANGUAGE_CLARITY` · REMOVE

> **was:** "…and the admissible set contracts to empty while the crew retains the aircraft [10]."
> **now:** "…specific advisory types are progressively inhibited and the admissible set contracts to empty [10]."

The clause was not idiomatic and implied that TCAS preserves human authority. The novelty audit records that authority there is **procedurally constrained** — ICAO expects RA compliance. Removed without substitution; the sentence's only function is to establish mechanism precedent. No stronger comparison was introduced.

### PC3 — "three large-scale systematic reviews" · `CITATION_MISMATCH` · REVISE

> **was:** "…a structured review of **72 papers** that advanced to full review, complemented by three large-scale systematic reviews, which established the governance framing and the comparator set [1]–[6]."
> **now:** "…a structured review of **72 papers** that advanced to full review, which established the governance framing and the comparator set [1]–[6]."

Of the cited six, only [1] Indykov is a systematic literature review; [2] is a taxonomy, [3] and [4] are frameworks, [5] an overview, [6] an empirical study. The label was inherited from v3, where it was anchored to a different reference set and to a "532 primary references" figure that V4 does not carry.

**The citation range was deliberately retained.** Audit established that **[1], [2], [3] and [6] are cited in the body only through this range**. Narrowing it would have orphaned four references and failed the §21 check. The surviving claim — that these sources established the governance framing and comparator set — is one all six support, so the range is accurate as it now stands. No review count is asserted.

### PC4 — Companion journal treatment · `DOUBLE_BLIND_RISK` + `SELF_CONTAINMENT` · REVISE

> **was:** "Proofs are given in the companion journal treatment."
> **now:** "Full proofs are omitted here for space; only the properties used by the evaluation are stated."

Closes three problems at once: the pointer to unpublished work, the blind-review leak, and the dependence of a formal claim on material a reviewer cannot reach. No self-citation was added.

### PC5 — RQ3 causal explanation · `EVIDENCE_TYPE_CROSSING` · REVISE

> **was:** "The direction of movement is consistent with a finer model resolving nearshore sheltering that the coarser grid cell averages away, though the two records also cover different periods and the two effects are not separated here."
> **now:** "The configurations differ in both wave model and record length; this evaluation does not isolate which difference accounts for the observed spread of approximately 1.3 percentage points."

The original hedge was present but the explanatory clause led. No evidence isolates the wave-model effect from the record-period effect, so the physical explanation has been removed rather than qualified.

### PC6 — Site disclosure · `DOUBLE_BLIND_RISK` (apparent) · REVISE

> **was:** "a single site (5.98° N, 116.01° E)"
> **now:** "a coastal site in Sabah, Malaysia (5.98° N, 116.01° E)"

    SITE_DISCLOSURE = REPRODUCIBILITY_CHOICE_NOT_ANONYMISATION

Omitting the city while retaining exact coordinates does not anonymise the site and created a false impression of masking. The drafting report's characterisation of the coordinates-only form as "more conservative than v3" was incorrect and has been corrected (§12).

### PC7 — Build comment · `DOUBLE_BLIND_RISK` (formatting stage) · OPEN

    BUILD_COMMENT = REMOVE_BEFORE_SUBMISSION

Retained for this audit. It names internal repository paths and rebuild-programme metadata, and must not enter the formatted submission.

### PC8 — Introduction prevalence claim · `SCOPE_OVERCLAIM` · REVISE

> **was:** "AI decision-support systems deployed in safety-critical settings are typically governed by a binary question: may the AI participate, or not."
> **now:** "A common governance framing in the reviewed AI decision-support literature is binary: whether the AI may participate at all."

No prevalence statistic was introduced.

### PC8b — Antecedent repair · `LANGUAGE_CLARITY` · REVISE *(consequence of PC8)*

The PC8 rewrite left "such systems" without a clean antecedent. Now reads "Under that framing, when conditions degrade the AI is switched off, or it continues to offer its full range of advice on evidence that no longer supports it."

---

## 5. Abstract audit

Audited sentence by sentence. **193 words**, within the 170–200 target.

| Element | Status |
|---|---|
| Scoped novelty | **PASS** after PC1 and PC1b |
| No mechanism invention | **PASS** — precedent stated as precedent |
| No safety or effectiveness inference | **PASS** — closes on "do not establish safety or decision-quality outcomes" |
| Correct empirical denominator | **PASS** — "departure-window hours" stated |
| Correct reading of 5.81, 4.48, 0.00 | **PASS** — change in admissible set; configurations described as alternatives |
| Plain text, no symbols | **PASS** — no notation; "multi-component environmental state", "participation gating", "advisory-scope restriction" |
| No literature-wide statements | **PASS** after correction |

---

## 6. Introduction audit

| Check | Status |
|---|---|
| Canonical gap statement verbatim | **PASS** — 1 occurrence, exact match |
| Canonical novelty-positioning sentence verbatim | **PASS** — first of 3 |
| RQ1, RQ2, RQ3 verbatim | **PASS** — exact match against the frozen text |
| Exactly two contributions | **PASS** — C1 and C2, no third |
| Old review contribution absent | **PASS** |
| Prevalence claims scoped | **PASS** after PC8 |
| Avionics precedent acknowledged early | **PASS** — second paragraph |

---

## 7. Related Work citation audit

Every TABLE I row verified against the validated notes and the novelty-defence matrix.

| Row | Verdict |
|---|---|
| Collision-avoidance advisory inhibition [10] | **PASS** — governed object, banded radio-altitude source, nested contraction to empty, and "certified design requirement" rather than a proved property all match AC 20-151C and its note |
| Verified advisory logic [11] | **PASS_WITH_SCOPE → refined.** "Scope conditioned: Yes" was bare; now reads "Yes — safe advisory set is state-dependent", matching the note's caution that the paper's object is collision-freedom, not an abstracted admissible-type set |
| Levels of automation [12] | **PASS** — design-time assignment and "narrows the number of alternatives" reproduce the note's distinction exactly |
| Adaptive automation [13] | **PASS** — trigger categories condensed faithfully; governed object is allocation and automation level |
| Selective prediction and deferral [14] | **PASS** — participation, model-internal confidence, coverage guarantee |
| Shielding and action masking [5] | **PASS** — executable action set, no human adviser, enforcement by output filtering |
| Graduated runtime governance [4], [7], [8] | **PASS** — three sources grouped, "Partly" correctly signals that monotone-by-construction properties come from [7] and [8] and not [4] |

**Kang [8] non-load-bearing: confirmed.** It appears in one grouped table row alongside [4] and [7], and in one synthesis citation. No claim rests on it alone.

Synthesis prose verified: the three conclusions (mechanism precedent exists, formal-property precedent exists, the operational combination is what the reviewed literature does not supply) are each supported by the sources cited to them.

**Reference [6] disposition: KEEP.** After the PC3 correction the sentence claims that the cited sources established the governance framing and comparator set. Ghaleb is a comparator in the corpus record, so the citation is accurate. It is minimally cited rather than decorative, and it was **not** forced into TABLE I to justify its presence.

---

## 8. Formalisation audit

Notation checked against `appendix-c-formalisation.md` and `algorithm-specification.md`.

| Construct | Status |
|---|---|
| `S = f(E)`, five components, max-severity aggregation | **PASS** |
| `Obs_i = (X_i × 𝕋) ∪ {⊥}` | **PASS** |
| `ρ_{D,τ}`, `F_{D,τ} = f ∘ ρ_{D,τ}` | **PASS** — ideal/deployed distinction stated and described as load-bearing |
| Invalid / absent / stale → ⊥ → UNSAFE | **PASS** — in TABLE II and prose; fail-safe correctly derived from the component mapping plus maximality, not a pre-check |
| Declared exclusion, pinned SAFE | **PASS** |
| Exclusion-before-fault | **PASS** — with the 43,848-hour consequence stated |
| `D` fixed and declared; `t ∉ D` | **PASS** |
| Lower-bound consequence | **PASS** — stated as one of three indivisible obligations |
| Operational totality | **PASS** |
| Pre-reasoning `RS(S)`, no post-generation filter | **PASS** — the distinction from output-filtering approaches is explicit |

No sentence was found that simplifies these to the point of falsity.

### Formal-property framing

Totality, monotonicity, Safety Dominance and containment are introduced as properties that "verify the specification; they are **not** claimed as new", with prior work named. **PASS.** No wording turns formal verification into empirical validation.

---

## 9. Fidelity audit

| Figure | Manuscript | Status |
|---|---|---|
| Primary episodes | 292 | **PASS** |
| Permissive / intermediate split | 32 / 260 | **PASS** |
| Episodes with advisory / without | 244 / 16 | **PASS** |
| Advisory records | 454 | **PASS** |
| Gate-off structural cases, outside denominator | 162 | **PASS** |
| F1 / F2 / F3 | zero violations | **PASS** |

Wording checks: "advisory **records**, not advisory types" present; `Delay` named as the single generated conclusion type; permissive rule set stated as empty with the requirement deferred; "exercised only on the restrictive side" present. No occurrence of "validated", "proven", "complete", "comprehensive" or "exhaustive" in relation to this evidence.

---

## 10. Evaluation method and Results audit

**Method — PASS.** 43,848 hourly records; departure window and small-vessel scope stated; thresholds attributed to their sources; solar provenance described as a NOAA-style low-precision formulation checked against the USNO reference service, with the sub-minute bound; COLREGs used for the boundary with the policy status stated and no source claimed for AI withdrawal; four comparators defined individually; primary and resolution described as alternative configurations; `D = {m}` and the κ = 0 consequence both present. No superseded model description was restored.

**Results — PASS.** 42.88%, 48.69%, Δ_L2 5.81%, C1↔C3 0.00% (primary); Δ_L2 4.48%, C1↔C3 0.00% (resolution). **41.08% and 45.56% are absent**; TABLE III marks those cells "not reported". The structural-identity paragraph is explicitly framed as a consistency check on the implementation rather than an independent finding — no descriptive census is converted into statistical inference.

**Zero-divergence control — PASS.** Every statement of C1↔C3 is bounded to the evaluated comparator definitions, in both Results and Discussion, with an explicit denial of extension to traffic-light or three-state systems in general.

---

## 11. Discussion audit

| Check | Status |
|---|---|
| Mechanism precedent acknowledged | **PASS** |
| C1 at frozen strength | **PASS** — enforcement route claimed, properties not claimed as new |
| C2 at frozen strength | **PASS** — governance-layer measurement at one site |
| Zero-divergence interpretation bounded | **PASS** |
| No safety or effectiveness inference | **PASS** — "effectiveness" appears once, inside a negation |
| Generalisation conditional remains formal | **PASS** |
| Cross-domain demonstration explicitly absent | **PASS** |
| Target-hardware evidence absent | **PASS** |
| No human study | **PASS** |
| Canonical novelty sentence verbatim | **PASS** — third of 3 |

---

## 12. Reference audit

**20 references. 20 cited. Zero orphans. Zero dangling citations.** Verified after the PC3 edit.

- No reference added, removed or renumbered by this audit.
- AC 20-151C is cited as current authority; **AC 20-151A does not appear**.
- The spelling is **Cleaveland**; "Cleveland" does not appear.
- Reference types are now represented accurately in prose following PC3.
- No reference was retained merely to preserve count, and none was added to raise it.

---

## 13. Double-blind audit

    DOUBLE_BLIND_SCIENTIFIC_TEXT = PASS
    DOUBLE_BLIND_FORMATTING_PREP = FAIL

Scientific text passes after PC4. A re-scan of the body — excluding the build comment — returns no match for author names, affiliations, email addresses, acknowledgements, institutional relationships, or the terms "companion", "journal treatment", "our previous", "our earlier", "we previously", "forthcoming" or "under review".

Formatting prep fails on the build comment alone (§14).

**Recorded gap in the earlier check.** The drafting report's double-blind scan returned PASS. It searched for names, affiliations, emails and acknowledgements, and did **not** search for self-referential pointers to the authors' own unpublished work — a standard blind-review leak. PC4 passed that scan and should not have. The drafting report has been corrected (§16).

---

## 14. Site-disclosure and build-comment decisions

    SITE_DISCLOSURE = REPRODUCIBILITY_CHOICE_NOT_ANONYMISATION
    BUILD_COMMENT   = REMOVE_BEFORE_SUBMISSION

Site wording now names the region and retains coordinates. If the venue's blind-review rules require location masking, that is a separate decision to be taken at submission; nothing in the current wording pretends to mask.

---

## 15. Language and reviewer-friction audit

**Bold emphasis — the readiness estimate was wrong and is corrected here.** The pre-audit count of 59 bold spans, with roughly 34 characterised as decorative inline prose, did not survive categorisation. Of the inline spans: RQ and contribution labels (5), comparator definition labels (4), Discussion paragraph leads (7), headline empirical values (6), definitional term introductions (4), and protected-disclosure emphasis (6) are all legitimate in a formal paper.

**Only four were genuinely decorative**, and all four have been unbolded: "targeted sources added after that review", "mechanism precedent exists", "formal-property precedent exists", "no data source exists in a deployment". The first three sit inside a "First / Second / Third" structure that already signals them.

Other friction items: "crew retains the aircraft" removed (PC2); the causal clause that implied a mechanism from a descriptive comparison removed (PC5); no undefined shorthand found; all percentage claims carry a stated denominator.

---

## 16. Word counts after edits

| Section | Before | After | Δ |
|---|---|---|---|
| Abstract | 198 | **193** | −5 |
| I. Introduction | 408 | 404 | −4 |
| II. Related Work | 287 | 281 | −6 |
| III. Formalisation | 738 | 746 | +8 |
| IV. Evaluation Method | 525 | 528 | +3 |
| **V. Results** | **858** | **849** | −9 |
| VI. Discussion and Limitations | 696 | 696 | 0 |
| VII. Conclusion | 192 | 192 | 0 |
| **Body** | **3,704** | **3,696** | **−8** |

    BODY_WORD_COUNT         = 3,696
    RESULTS_SECTION_LARGEST = YES (849 against 746; margin 103)
    PROTECTED_DISCLOSURES   = PASS (19/19)

Body is within the ≤3,704 constraint and inside the expected 3,690–3,700 band. No protected disclosure was cut.

---

## 17. Changed files

**Edited:**

- `manuscript.md` — twelve surgical corrections (§4, §7, §15). No section added or removed; no reference added, removed or renumbered; no number changed.
- `drafting-report.md` — two corrections: the double-blind statement now records that the earlier mechanical scan was insufficient and that PC4 has been corrected; the site-disclosure statement no longer describes coordinates-only as more conservative or more anonymous.

**Created:**

- `post-draft-audit.md` (this file)

**Untouched:** `v3-revision/manuscript-v3.md` · all eight AMICT evidence artefacts · all empirical artefacts and scripts · `notes/` and `citation-notes-map.md` · all CLOSED Journal 1 workstreams. No `.docx`, `.pdf` or `.tex`. No experiment run, no result recomputed, no architecture, threshold or comparator changed. **The RESOLUTION provenance item was not repaired.**

---

## 18. Remaining open items

| # | Item | Owner stage |
|---|---|---|
| 1 | `BUILD_COMMENT = REMOVE_BEFORE_SUBMISSION` | Formatting |
| 2 | Current official AMICT template not obtained | Formatting |
| 3 | Current-cycle page limit unconfirmed; six pages assumed from the 2026-07 record | Formatting |
| 4 | `RESOLUTION_PAIRWISE_C0_C1_C0_C2 = PROVENANCE_INCOMPLETE` — unused by the manuscript | Separate provenance repair |

No scientific concern remains open. No stop condition fired.

---

    POST_DRAFT_AUDIT              = CLOSED
    MANUSCRIPT_V4_SCIENTIFIC_TEXT = REVIEWER_READY
    CLAIMS_REVISED                = 10
    CLAIMS_REMOVED                = 1
    OPEN_ITEMS                    = 4
    BODY_WORD_COUNT               = 3696
    RESULTS_SECTION_LARGEST       = YES
    PROTECTED_DISCLOSURES         = PASS
    DOUBLE_BLIND_SCIENTIFIC_TEXT  = PASS
    BUILD_COMMENT                 = REMOVE_BEFORE_SUBMISSION
    FORMAT_READY                  = NO

---

# Addendum A — Related-Work Corpus Reframe (2026-09-14)

**Task:** `docs/tasks/AMICT V4 — REFRAME RELATED-WORK CORPUS DESCRIPTION`
**Scope:** presentation only. Nothing above this line is rewritten; §1–§18 stand as the record of the post-draft audit as conducted.

> The conference manuscript no longer reports the structured-review corpus size or refers to an earlier review protocol. Related Work is now framed by literature function: broader AI-governance framing and targeted mechanism comparison. This presentation change does not alter the underlying literature corpus, source-validation record or novelty audit.

## A.1 Paragraph replaced

**Original (80 words):**

> Two literature populations inform this paper and are reported separately. The first is a structured review of **72 papers** that advanced to full review, which established the governance framing and the comparator set [1]–[6]. The second is a set of targeted sources added after that review, located by a bounded audit of the mechanism claim rather than by the original search and screening protocol [10]–[15]. They are not part of the 72-paper sample, and the two populations are not merged.

**Replacement (66 words):**

> Prior work informing this study falls into two groups. The first comprises AI decision-support and governance literature used to inform the governance framing and comparator set [1]–[5]. The second comprises targeted sources identified during a bounded audit of the mechanism claim [9]–[14]. The latter sources provide direct comparison with established advisory-scope, automation, deferral and regulatory governance mechanisms, and are treated separately from the broader AI-governance literature.

**One deviation from the supplied wording,** made under §8's instruction to narrow rather than overstate. The supplied collective phrase read "advisory-scope, automation and governance mechanisms". That does not cover selective prediction and deferral, which is what [13] contributes. The phrase now reads "advisory-scope, automation, deferral and regulatory governance mechanisms", which matches the six sources without implying that each demonstrates advisory-scope restriction. Citation ranges differ from the supplied text because a reference was removed (§A.3).

## A.2 Other review-history wording

A full-manuscript scan was run for: 72 · 72 papers · 72-paper · structured review · structured literature review · earlier review · original review · original review protocol · original search · screening protocol · review sample · full review · targeted post-review · post-review additions · systematic literature review · SLR · PRISMA · systematic search · comprehensive review · exhaustive review · inclusion criteria · corpus size.

| Occurrence | Location | Disposition |
|---|---|---|
| "structured review of 72 papers that advanced to full review" | II opening | **Removed** with the paragraph |
| "targeted sources added after that review" | II opening | **Reframed** to "targeted sources identified during a bounded audit of the mechanism claim" |
| "the original search and screening protocol" | II opening | **Removed** |
| "not part of the 72-paper sample, and the two populations are not merged" | II opening | **Removed**; the functional separation is retained by "treated separately from the broader AI-governance literature" |
| "systematic literature review" | Reference [1] title | **Retained** — a bibliographic title, not a methodology claim by this manuscript |
| "102724", "1972" | DOI and COLREGs title | **Retained** — digit coincidences, not review history |

No other manuscript-facing occurrence was found. `FORMAL_REVIEW_METHODOLOGY_CLAIM = NONE`.

## A.3 Reference disposition — [1]–[6] (old numbering)

The range was **not** retained wholesale to avoid orphans. Each reference was tested against the revised claim independently.

| Old ref | Standalone citations | Supports revised claim? | Disposition |
|---|---|---|---|
| [1] Indykov | 0 | **Yes** — AI-governance literature; architectural-tactics evidence informing the governance framing | `SUBSTANTIVELY_SUPPORTS_REVISED_CLAIM` — **retained as [1]** |
| [2] Shamsujjoha | 0 | **Yes** — runtime-guardrail taxonomy; governance framing | `SUBSTANTIVELY_SUPPORTS_REVISED_CLAIM` — **retained as [2]** |
| [3] Dalrymple | 0 | **Yes** — Guaranteed Safe AI framework; governance framing | `SUBSTANTIVELY_SUPPORTS_REVISED_CLAIM` — **retained as [3]** |
| [4] Flehmig | 3 (II, IV, V) | **Yes** — defines comparator C3 | `SUPPORTS_ANOTHER_SURVIVING_CLAIM` — **retained as [4]** |
| [5] Könighofer | 2 (II, VI) | **Yes** — shielding comparator and the output-filtering contrast | `SUPPORTS_ANOTHER_SURVIVING_CLAIM` — **retained as [5]** |
| [6] Ghaleb | 0 | **No** | `DECORATIVE_ONLY` — **REMOVED** |

**Why [6] was removed.** It is embodied runtime assurance for vision–language–action manipulation. It is a comparator in the internal corpus record, but it is not "AI decision-support and governance literature" in the sense the revised sentence uses, no surviving sentence depends on it, it has no TABLE I row, and it was flagged as range-only at three successive audit stages. Broadening the sentence to accommodate it would have been the overstatement §7 forbids. Removed rather than retained for count.

## A.4 Reference disposition — [10]–[15] (old numbering)

All six carry standalone substantive citations; none is range-only.

| Old ref | New | Standalone | Role in the collective phrase |
|---|---|---|---|
| [10] FAA AC 20-151C | [9] | 4 | Advisory-scope precedent |
| [11] Cleaveland et al. | [10] | 4 | Formal advisory-logic precedent |
| [12] Parasuraman et al. | [11] | 2 | Levels of automation |
| [13] Bernabei & Costantino | [12] | 2 | Adaptive automation |
| [14] Kwon & Kim | [13] | 2 | Selective prediction / deferral — the reason "deferral" was added to the collective phrase |
| [15] FDA CDS guidance | [14] | 1 | Regulatory recommendation/output framing |

No source is described as demonstrating advisory-scope restriction except [9], which does.

## A.5 Renumbering

Old [1]–[5] unchanged. Old [6] removed. Old [7]–[20] shifted to [6]–[19]. Ranges updated: `[1]–[6]` → `[1]–[5]`; `[10]–[15]` → `[9]–[14]`. TABLE I's graduated-governance row now cites [4], [6], [7]; the formal-property precedent sentence now cites [6], [7], [10].

## A.6 Integrity after edit

    REFERENCE_COUNT     = 19   (was 20)
    ORPHAN_REFERENCES   = 0
    DANGLING_CITATIONS  = 0
    numbering           = contiguous 1..19

| Section | Before | After | Δ |
|---|---|---|---|
| II. Related Work | 281 | **267** | −14 |
| References | 540 | 509 | −31 |
| **Body** | **3,696** | **3,682** | **−14** |

All other sections unchanged. `RESULTS_SECTION_LARGEST = YES` (849 against 746, margin 103). No prose was added to compensate for removed words.

## A.7 Preserved content

| Item | Status |
|---|---|
| Canonical gap statement | **Unchanged** — 1 verbatim occurrence, Introduction |
| Canonical novelty-positioning sentence | **Unchanged** — 3 verbatim occurrences |
| RQ1, RQ2, RQ3 | **Unchanged** — verbatim |
| Title, C1, C2, formal content, comparators, thresholds, results, site wording | **Unchanged** |
| Protected disclosures | **19/19 PASS** |

**One disclosure changed form, not substance.** Item 17 was "structured review 72 distinguished from targeted post-review additions". It is now "broader AI-governance literature distinguished from targeted mechanism-comparison sources". The two literature groups remain separated and are still never merged; only the historical framing was dropped, which is the object of this task.

Abstract and Introduction were re-checked: the scoped formulations "commonly framed in the reviewed literature" and "Within the reviewed AI decision-support and governance literature" remain, and neither depends on the removed narrative. Neither was weakened.

## A.8 Files changed

- `manuscript.md` — Section II opening paragraph replaced; reference [6] removed; [7]–[20] renumbered to [6]–[19]; two citation ranges updated.
- `post-draft-audit.md` — this addendum appended. Sections §1–§18 unmodified.

Internal historical records were **not** altered: the number 72 and the structured-review history remain intact in the contribution freeze, novelty audit, source-validation report, drafting report and provenance files.

---

    LITERATURE_CORPUS_COUNT_IN_MANUSCRIPT = REMOVED
    EARLIER_STRUCTURED_REVIEW_REFERENCE   = REMOVED
    ORIGINAL_REVIEW_PROTOCOL_REFERENCE    = REMOVED
    RELATED_WORK_FRAMING                  = FUNCTION_BASED
    FORMAL_REVIEW_METHODOLOGY_CLAIM       = NONE
    SCOPED_GAP_STATEMENT                  = PRESERVED
    NOVELTY_POSITIONING                   = PRESERVED
    REFERENCE_COUNT                       = 19
    ORPHAN_REFERENCES                     = 0
    DANGLING_CITATIONS                    = 0
    BODY_WORD_COUNT                       = 3682
    RESULTS_SECTION_LARGEST               = YES
    PROTECTED_DISCLOSURES                 = PASS
    MANUSCRIPT_V4_SCIENTIFIC_TEXT         = REVIEWER_READY
    FORMAT_READY                          = NO

---

# Addendum B — Related-Work Micro-Repair (2026-09-14)

**Task:** `docs/tasks/AMICT V4 — RELATED-WORK MICRO-REPAIR AFTER CORPUS REFRAME`
**Scope:** two sentence-level edits in Section II. Addendum A and §1–§18 above are unmodified and remain the record of their respective tasks.

The corpus reframe of Addendum A removed the review-history framing but left one piece of internal research-process vocabulary in the manuscript — "bounded audit of the mechanism claim" — and one absence attributed grammatically to the literature rather than to the search. Both are repaired here. No reference was changed, added or removed.

## B.1 Opening paragraph

**Before (66 words):**

> Prior work informing this study falls into two groups. The first comprises AI decision-support and governance literature used to inform the governance framing and comparator set [1]–[5]. The second comprises targeted sources identified during a bounded audit of the mechanism claim [9]–[14]. The latter sources provide direct comparison with established advisory-scope, automation, deferral and regulatory governance mechanisms, and are treated separately from the broader AI-governance literature.

**After (56 words):**

> Prior work informing this study is considered in two groups. The first comprises AI decision-support and governance literature examined for the governance framing and comparator set [1]–[5]. The second comprises targeted sources examined specifically for comparison with the closest mechanism precedents [9]–[14]. Keeping these groups distinct separates the governance framing from the mechanism-level comparisons developed below.

Three things changed, all of them reviewer-facing rather than scientific.

**"bounded audit of the mechanism claim" → "examined specifically for comparison with the closest mechanism precedents".** The original phrase is internal research-process vocabulary. It implied a separate audit methodology the conference paper neither reports nor needs, and invited questions — what was the audit, where is its protocol, was it systematic, what was searched — that bear on neither C1 nor C2. The replacement states the function: these sources were examined for mechanism comparison.

**"the broader AI-governance literature" removed.** As Addendum A's own wording, it was open to a population-level reading — as though the paper had characterised the field. The manuscript describes literature examined for this work. The closing clause now states why the two groups are kept apart, without any claim about what the field contains. The phrase no longer appears anywhere in the manuscript.

**"used to inform" → "examined for".** Removes the residual implication that the first group was assembled by a process the paper should describe.

## B.2 Synthesis clause

**Before:**

> Third, what the reviewed AI-governance literature does not supply is the combination: a classified multi-component environmental state, explicit observation-resolution and exclusion semantics, and a state-conditioned advisory-type admissibility contract defined independently of the generator.

**After:**

> Third, what we did not identify in the reviewed AI-governance literature is the combination: a classified multi-component environmental state, explicit observation-resolution and exclusion semantics, and a state-conditioned advisory-type admissibility contract defined independently of the generator.

The original attributed the absence to the literature; the revision attributes it to the search. The remainder of the sentence is character-for-character unchanged, and the clause is now grammatically parallel to the frozen Introduction gap statement — *"Within the reviewed AI decision-support and governance literature, we did not identify…"*. Neither statement was broadened.

## B.3 Citation integrity

No citation was altered. [1]–[5] support the first functional statement — AI decision-support and governance literature examined for the governance framing and comparator set. [9]–[14] support the second — sources examined for comparison with the closest mechanism precedents. Neither range became inaccurate under the revised wording, so §7's stop condition did not arise.

    REFERENCE_COUNT    = 19
    ORPHAN_REFERENCES  = 0
    DANGLING_CITATIONS = 0
    numbering          = contiguous 1..19

## B.4 Reviewer-question test

Section II was re-read for wording that would oblige the paper to report something it does not contain. Twenty expressions were scanned: bounded audit · audit of the mechanism claim · systematic audit · structured audit · audit protocol · targeted review protocol · search strategy · screening procedure · audit corpus · comprehensive search · exhaustive search · structured review · review protocol · original search · screening · database · PRISMA · SLR · 72 · broader AI-governance literature. **All return zero.** The two numeric matches for "72" are a DOI fragment (`102724`) and the year in the COLREGs title (`1972`).

    REVIEW_HISTORY_DEPENDENCY         = NONE
    CORPUS_SIZE_DEPENDENCY            = NONE
    FORMAL_SLR_DEPENDENCY             = NONE
    AUDIT_PROTOCOL_DEPENDENCY         = NONE
    POPULATION_LEVEL_LITERATURE_CLAIM = NONE

A reviewer may still disagree with the scoped literature conclusion. That is a disagreement about the claim, which is legitimate, rather than a request for a document the paper does not provide.

## B.5 Preserved

| Item | Status |
|---|---|
| Canonical gap statement | **Unchanged** — 1 verbatim occurrence |
| Canonical novelty-positioning sentence | **Unchanged** — 3 verbatim occurrences |
| RQ1, RQ2, RQ3 | **Unchanged** — verbatim |
| "commonly framed in the reviewed literature" (Abstract) | **Unchanged** |
| Title, C1, C2, TABLE I rows, formalisation, comparators, thresholds, empirical numbers, interpretation, site wording, R-SAFE-001, E5/H3, provenance-open item | **Unchanged** |
| Protected disclosures | **19/19 PASS** |

The Abstract and Introduction were checked for contradiction with the revised Section II. None was found, and neither was modified.

The Section II argument order is intact: literature examined for governance framing → targeted closest-mechanism sources → TABLE I → mechanism precedent exists → formal-property precedent exists → scoped combination not identified → contribution positioning.

## B.6 Word count

| Section | Before | After | Δ |
|---|---|---|---|
| II. Related Work | 267 | **259** | −8 |
| **Body** | **3,682** | **3,674** | **−8** |

All other sections unchanged. `RESULTS_SECTION_LARGEST = YES` (849 against 746, margin 103).

## B.7 Files changed

- `manuscript.md` — two sentence-level edits in Section II.
- `post-draft-audit.md` — this addendum appended. §1–§18 and Addendum A unmodified.

No other file was touched. Internal historical records retain the structured-review history in full.

---

    RELATED_WORK_FUNCTIONAL_FRAMING    = PASS
    REVIEW_HISTORY_DEPENDENCY          = NONE
    CORPUS_SIZE_DEPENDENCY             = NONE
    FORMAL_SLR_DEPENDENCY              = NONE
    AUDIT_PROTOCOL_DEPENDENCY          = NONE
    POPULATION_LEVEL_LITERATURE_CLAIM  = NONE
    SCOPED_SEARCH_OUTCOME_LANGUAGE     = PASS
    REFERENCE_COUNT                    = 19
    ORPHAN_REFERENCES                  = 0
    DANGLING_CITATIONS                 = 0
    BODY_WORD_COUNT                    = 3674
    PROTECTED_DISCLOSURES              = PASS
    MANUSCRIPT_V4_SCIENTIFIC_TEXT      = REVIEWER_READY
    FORMAT_READY                       = NO
