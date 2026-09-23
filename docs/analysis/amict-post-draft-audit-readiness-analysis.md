# AMICT Manuscript V4 Post-Draft Audit — Task Readiness Analysis

**Date:** 2026-09-14
**Analyses:** `docs/tasks/AMICT MANUSCRIPT V4 — POST-DRAFT SCIENTIFIC AND REVIEWER AUDIT.md`
**Status:** PRE-EXECUTION ANALYSIS ONLY. No audit performed, no manuscript edit made, `post-draft-audit.md` does not exist.
**Companions:** [rebuild](amict-conference-rebuild-readiness-analysis.md) · [source validation](amict-source-validation-readiness-analysis.md) · [contribution freeze](amict-contribution-freeze-v2-readiness-analysis.md) · [RQ freeze](amict-rq-narrative-freeze-readiness-analysis.md) · [manuscript V4](amict-manuscript-v4-readiness-analysis.md)

---

## 1. What the task is

An adversarial reviewer audit of the drafted text, with authority to make surgical edits. It names **seven specific sentences** for priority checking. I have located all seven in the manuscript and checked each against the frozen authorities.

**All seven are real defects.** An eighth surfaced during the check. Two of them are mine to own: one is a double-blind risk my own drafting audit did not catch, and one is a claim in my drafting report that was simply wrong.

This is the task working as designed — the draft passed nineteen mechanical disclosure checks and a prohibited-phrase scan, and still carries eight wording defects that a mechanical scan cannot see.

---

## 2. Priority checks — all confirmed

### PC1 (§4) — Abstract gap clause · `SCOPE_OVERCLAIM` · REVISE

Present as written: *"but has not been given a corresponding operational treatment in the AI governance literature."*

This is an unscoped claim about the state of an entire literature. The frozen boundary permits only search-outcome language — *"Within the reviewed … we did not identify."* The Introduction carries the canonical statement correctly; the Abstract does not.

**Submission-blocking in substance**, because it is the strongest-read sentence in the paper and it is exactly the overclaim pattern the whole gate sequence exists to prevent. The task's suggested scoped form is correct and costs no words.

### PC2 (§5) — "while the crew retains the aircraft" · `SCOPE_OVERCLAIM` + `LANGUAGE_CLARITY` · REVISE

Two defects in one clause. It is not idiomatic — "retains the aircraft" does not clearly mean retains control — and it implies that human authority is preserved in TCAS, when the novelty audit found that authority there is **procedurally constrained**: ICAO expects RA compliance. Leaving it in makes this work's unconditional-authority property look like a larger distinction than the audit permits.

The sentence's job is to establish mechanism precedent. Deleting the clause does that job and removes both defects.

### PC3 (§6) — "three large-scale systematic reviews" · `CITATION_MISMATCH` · REVISE, with a hidden dependency

The label is inherited from v3, where it was anchored to a different reference set and to a "532 primary references" figure that V4 drops. In V4 it is attached to `[1]–[6]`, which are: Indykov (a systematic literature review), Shamsujjoha (a taxonomy), Dalrymple (a framework), Flehmig (a framework), Könighofer (an overview), Ghaleb (an empirical study). **Exactly one is a systematic review.** The claim is not supported by the citation attached to it.

**The dependency the task does not mention.** I checked which references survive on their own: **[1], [2], [3] and [6] are cited nowhere in the body except inside that single `[1]–[6]` range**, attached to the flagged sentence. [4] and [5] have three and two independent citations respectively.

So narrowing the citation range — the obvious fix — would orphan up to four references and fail the §21 orphan check.

**Clean fix:** delete only the clause *"complemented by three large-scale systematic reviews"* and keep the range on the surviving claim, which those six sources do support — they established the governance framing and comparator set. One deletion, no orphans, no reference-list change.

**Separate finding:** [6] Ghaleb is effectively decorative — it appears only in the range and has no substantive citation site, despite being a natural Related Work row (embodied intermediate-mode runtime assurance). Either give it a real citation or drop it.

### PC4 (§7) — "Proofs are given in the companion journal treatment." · `DOUBLE_BLIND_RISK` · REVISE

Three problems. The journal treatment is unpublished, so a conference reviewer cannot reach it. The paper therefore leans on inaccessible material for its formal claims. And the phrase tells reviewers that the authors have a companion journal paper on the same architecture — which, combined with the site coordinates and the domain, is identifying.

**This one I missed.** My drafting-report double-blind scan looked for names, affiliations, emails and acknowledgements. It did not look for **self-referential pointers to the authors' own unpublished work**, which is a standard blind-review leak. The scan returned PASS and should have returned a flag.

The task's suggested replacement — omit the proofs for space, state only the properties the evaluation uses — is correct and removes all three problems at once.

### PC5 (§16) — RQ3 causal interpretation · `EVIDENCE_TYPE_CROSSING` · PASS_WITH_SCOPE, leaning REVISE

Present as: *"consistent with a finer model resolving nearshore sheltering that the coarser grid cell averages away, though the two records also cover different periods and the two effects are not separated here."*

The hedge is already there, which keeps it defensible. But the explanatory clause leads, and no evidence isolates the mechanism — the two configurations differ in both wave model and record length. The task's alternative states the non-isolation directly and drops the speculation.

Since the mechanism claim buys nothing and the safer form is shorter, **REVISE is the better call** even though PASS_WITH_SCOPE is defensible.

### PC6 (§19) — Site disclosure · `DOUBLE_BLIND_RISK` (apparent, not actual) · REVISE

The task makes a point I got wrong. The manuscript gives `5.98° N, 116.01° E` without naming the city — and **my drafting report described this as "more conservative than v3."** It is not. Those coordinates are Kota Kinabalu. Omitting the name while keeping exact coordinates is the same disclosure, expressed less clearly, and it creates a false impression of masking.

The task's preferred wording — *"a coastal site in Sabah, Malaysia (5.98 N, 116.01 E)"* — is better science: reproducibility is served, and nothing pretends to anonymise. The right record is that coordinates are a **reproducibility choice, not an anonymisation device**.

### PC7 (§20) — Build comment · `DOUBLE_BLIND_RISK` (formatting stage) · `REMOVE_BEFORE_SUBMISSION`

The header comment names internal repository paths and the rebuild programme. It may stay for the audit. Its effect is precisely what §22 anticipates: `DOUBLE_BLIND_SCIENTIFIC_TEXT = PASS` while `DOUBLE_BLIND_FORMATTING_PREP = FAIL`.

### PC8 (§9, found during this check) — "typically governed by a binary question" · `SCOPE_OVERCLAIM` · REVISE

The Introduction's opening sentence asserts a prevalence claim about deployed AI decision-support systems in general, with no citation. It should be scoped to the reviewed systems or to the comparator framing this study uses. Not flagged by the task; same defect class as PC1.

---

## 3. What the mechanical checks got right, and what they could not see

The drafting report's checks hold up. I re-verified reference integrity independently: **20 listed, 20 cited, zero orphans, zero dangling**. The nineteen protected disclosures are present. The prohibited-phrase scan was accurate.

But every one of the eight defects above is invisible to that kind of check. `SCOPE_OVERCLAIM` in the abstract passes a banned-word scan because it uses no banned word. `CITATION_MISMATCH` passes because the citation exists and resolves. `DOUBLE_BLIND_RISK` from a self-referential pointer passes because no name appears. **A clean mechanical audit is not evidence of a clean manuscript**, and the two gates were right to be separate.

---

## 4. Reviewer-friction finding: bold density

§23 names "excessive bold emphasis". The body carries **59 bold spans** across 3,704 words: roughly 15 structural (RQ labels, C1/C2, table captions), ~10 table cells, leaving **~34 inline-prose emphases — about one every 110 words**. That is heavy for a formal venue and reads as unpolished.

Recommend reducing inline emphasis to the genuinely load-bearing few — the headline percentages, "not claimed as new", "records, not types" — and letting sentence structure carry the rest. Roughly 20 removals, zero word cost, low risk.

---

## 5. Word budget after the corrections

Every fix is a deletion or a same-length substitution:

| Fix | Δ words |
|---|---|
| PC1 scoped abstract clause | ≈ 0 |
| PC2 delete crew clause | −7 |
| PC3 delete "three large-scale systematic reviews" clause | −6 |
| PC4 replace companion-journal sentence | ≈ 0 |
| PC5 replace causal clause with non-isolation statement | −5 |
| PC6 add "a coastal site in Sabah, Malaysia" | +5 |
| PC8 scope "typically" | ≈ +3 |

Net change ≈ **−10 words**. Body moves from 3,704 to about 3,694, comfortably under the 3,800 ceiling, and Results (858) stays the largest section. **§26.7 does not fire.**

---

## 6. Stop-condition pre-assessment

| # | Condition | Assessment |
|---|---|---|
| 1 | A frozen contribution unsupported in the actual manuscript | **Does not fire** — C1 and C2 are delivered in III and IV–V at frozen strength |
| 2 | An RQ unanswerable from included evidence | **Does not fire** — RQ1 in III, RQ2 in V §A–B, RQ3 in V §C |
| 3 | A load-bearing Related Work distinction collapses | **Does not fire** — PC3 is a mislabel of the *review population*, not of a mechanism distinction |
| 4 | A required empirical number conflicts with authority | **Does not fire** — all figures verified during drafting |
| 5 | Self-containment requires new evidence | **Does not fire** — PC4 is fixed by removing a pointer, not by adding evidence |
| 6 | Correction requires changing architecture, comparators or thresholds | **Does not fire** — all eight fixes are wording-level |
| 7 | Budget cannot hold after corrections | **Does not fire** (§5) |

Expected outcome: **`POST_DRAFT_AUDIT = CLOSED`**, `MANUSCRIPT_V4_SCIENTIFIC_TEXT = REVIEWER_READY`, `CLAIMS_REVISED ≈ 8`, `CLAIMS_REMOVED = 0`, `FORMAT_READY = NO`.

---

## 7. Points to settle during execution

1. **PC3 fix shape** — delete the clause and keep the `[1]–[6]` range, rather than narrowing the range and orphaning four references (§2, PC3).
2. **Reference [6]** — give Ghaleb a substantive citation site or drop it.
3. **Site wording** — adopt the "coastal site in Sabah, Malaysia" form and record coordinates as a reproducibility choice, correcting the drafting report's characterisation.
4. **Bold reduction** — decide whether to include it; it is reviewer-friction, not a scientific defect.
5. **Correct the drafting report** alongside the audit, so the double-blind PASS and the site claim do not stand uncorrected in the record.

---

## 8. Verdict

**Executable, no stop condition, and the task earns its place.** Seven named checks, all confirmed; an eighth found; one hidden citation dependency that would have turned a one-line fix into an orphan failure.

Two of the findings are corrections to my own work rather than to the draft alone: the double-blind scan that returned PASS should have flagged the companion-journal pointer, and the drafting report's claim that coordinates-without-city was "more conservative than v3" was wrong. Both belong in the audit record explicitly.

Net effect on the manuscript is about ten words and no scientific change.

---

## 9. Files inspected

Read-only. Nothing modified; no audit artefact created.

- `docs/tasks/AMICT MANUSCRIPT V4 — POST-DRAFT SCIENTIFIC AND REVIEWER AUDIT.md`
- `publications/active/ipsci-2026/submissions/v4-amict-rebuild/manuscript.md` — all seven flagged sentences, reference-integrity analysis, bold-density count
- `publications/active/ipsci-2026/submissions/v4-amict-rebuild/drafting-report.md`
- `data/amict-conference-rebuild/` — all eight frozen artefacts
