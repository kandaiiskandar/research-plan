# Discovery — AMICT 2026 v5 Submission

**Date:** 2026-09-23
**Purpose:** Self-contained discovery for a planning agent with no prior session context. Planning happens elsewhere; this document supplies verified facts and hard constraints.
**Status:** Discovery only. **No planning decisions made. No files modified.**

---

## 0. READ THIS FIRST — the standing constraint

A full adversarial audit sequence completed on 2026-09-21 and **locked** the research position. Its authority is `docs/analysis/final-research-chain-lock.md`.

> **Do not reopen the novelty question, the research questions, the gaps, the contribution hierarchy, the experiment, or the limitations.** Mechanism-level architecture novelty is **conceded to prior work** and must not be re-asserted anywhere in v5.

The most likely failure mode for a v5 plan is re-introducing an overclaim that a week of audit work removed, under conference-deadline pressure. §7 below lists the non-claims verbatim. Treat them as inviolable.

---

## 1. Situation

| | |
|---|---|
| **Target venue** | AMICT 2026 — 3rd International Conference on Advances in Machine Intelligence and Cybersecurity Technologies |
| **Dates / location** | 12–13 November 2026, Federal Territory of Labuan, Malaysia (hybrid) |
| **Host** | Universiti Malaysia Sabah (UMS) — the candidate's own institution |
| **Proceedings** | Accepted papers eligible for **IEEE Xplore** |
| **Review** | Double-blind, minimum two independent reviewers; Turnitin similarity **< 30%** |
| **Length** | **4–6 pages**, IEEE conference format |
| **Submission deadline** | **~2026-09-30 (7 days from 2026-09-23)** — confirm exact date/time and submission system with the organisers |

**Venue relationship, confirmed by the researcher:** AMICT is the **conference**; IPSci 2026 was an **e-proceeding**; **the same body handles both.** This is therefore a resubmission to an organisation that has already reviewed the work, into a higher-profile output.

---

## 2. Prior submission and rejection — verified

Source: `publications/active/ipsci-2026/revision-notes.md`.

**v2.5 was submitted to IPSci 2026 and REJECTED.**

| Review | Verdict | Substance |
|---|---|---|
| 1 | Accept, minor revision | Check the comparative table; **add experimental validation or case studies** |
| 2 | Accept, minor revision | **Reviews a different paper.** Twitter bot detection, TwiBot-22, F1 0.552, SHAP beeswarm, BotRGCN/BIC/ETS-MM baselines. Names the AMICT Machine Intelligence/Cybersecurity track. **No overlap with this submission** |
| 3 | **Reject** | "Lacks the technical and empirical evidence necessary to establish its novelty, effectiveness, and safety claims" |

**Converged signal (Reviews 1 and 3): no empirical validation.** At v2.5 the evaluation was designed but had not been run.

**Two facts the planner must carry:**

1. Reviewers of v2.5 **never saw** the Formal Properties, Algorithm Specification, Computational Complexity, Generalisation, Deployment Challenges or Threats to Validity sections — those were added post-submission on 2026-08-20. Review 3's "no technical evidence" objection was made against a version containing no formal proofs.
2. Discounting the misassigned Review 2 leaves **one accept-minor against one reject** — borderline, not a clear rejection. The revision notes already recommend raising this with the chairs.

### Why the rejection reason is now answered

| Review 3 objection | Current position |
|---|---|
| Novelty claims unsupported | **Mechanism novelty withdrawn entirely.** The claim is no longer made |
| Effectiveness claims unsupported | **Explicit non-claim.** Never asserted |
| Safety claims unsupported | **Explicit non-claim.** Never asserted |
| (R1 + R3) No empirical evidence | **Evaluation executed:** 43,848 hourly records; Δ_L2 = 5.81% / 4.48%; threshold sensitivity; component attribution; common-period decomposition |

Two of three objections are answered by *withdrawal*, one by *measurement*. The RQ set also improved structurally: `amict-conference-rebuild-readiness-analysis.md` §B5 warned that one empirical RQ out of three was weak for a paper rejected on empirical grounds; the locked set is now **two of three empirical**.

---

## 3. The base manuscript — v4

**Path:** `publications/active/ipsci-2026/submissions/v4-amict-rebuild/manuscript.md`
**Companions:** `drafting-report.md`, `post-draft-audit.md` (same directory)

| | |
|---|---|
| Length | **5,104 words** (includes a ~350-word HTML comment header that is not content) |
| Title | *"Evaluating Graduated Advisory-Scope Governance for AI Decision Support"* |
| Structure | Abstract · I. Introduction · II. Related Work · III. Operational Governance Formalisation · IV. Evaluation Method · V. Results · VI. Discussion and Limitations · VII. Conclusion · References |
| Assets | **3 tables** (TABLE I closest prior mechanism families; TABLE II observation conditions; TABLE III admissible-set divergence). Architecture figure **omitted for space** |
| References | **19** |
| Blinding | Double-blind; no author names or affiliations in the text body |

### Audit status (from `post-draft-audit.md`)

```
MANUSCRIPT_V4_SCIENTIFIC_TEXT   = REVIEWER_READY
FORMAT_READY                    = NO
RQ_INTEGRITY                    = PASS
GAP_STATEMENT_INTEGRITY         = PASS
NOVELTY_SENTENCE_INTEGRITY      = PASS
NUMERICAL_INTEGRITY             = PASS
TABLE_INTEGRITY                 = PASS
PROTECTED_DISCLOSURES           = PASS (19/19)
DOUBLE_BLIND_SCIENTIFIC_TEXT    = PASS
PROHIBITED_CLAIM_SCAN           = PASS
```

**The science was cleared on 2026-09-14. Format was not.** v4 already carries `MECHANISM_NOVELTY = WITHDRAWN`.

---

## 4. What v4 is missing — the 2026-09-21 findings

v4 predates the audit sequence by a week. Verified absent from `manuscript.md` (zero occurrences of each marker):

| Finding | Value | In v4? |
|---|---|---|
| Sourced-threshold robustness envelope | **5.67 – 9.56%** (PRIMARY, small vessel) | ✗ |
| Component attribution | `g_o` **518/531 = 97.6%**; `g_r` 13/531 = 2.4%; `g_w`, `g_t`, `g_m` zero binding; zero ties | ✗ |
| Δ_L2 identity | **Δ_L2 = P(S = CAUTION)** | ✗ |
| Resolution decomposition | wave-model **+1.97 pts**; record-length **−0.64 pts**; net 1.33 | ✗ |
| Vessel-class limitation | medium **1.96%**, large **1.26%** (PRIMARY) | ✗ |
| Time-policy limitation | daylight-only denominator **9.59% / 7.40%** | ✗ |
| TSO-C151c / TAWS concession | human-facing advisory inhibition on input validity | ✗ |

**None of these is a correction to v4.** All are improvements. In particular, v4 §165 currently reads *"The configurations differ in both wave model and record length; this evaluation does not isolate which difference accounts for the observed spread"* — which remains **true as written** for the evaluation v4 reports. It is superseded, not wrong.

**Consequence:** if time runs out, submitting v4 substantially as-is is a defensible fallback.

### Highest value per word, if space is constrained

1. **Δ_L2 invariance limitation** (~30 words) — now known; omitting it would be silence on a material limitation
2. **Threshold sensitivity envelope** (~150 words) — answers the most likely reviewer attack and converts the non-MET rainfall boundary from liability to defence
3. **Component attribution** (~100 words) — striking negative result
4. **Resolution decomposition** (~80 words) — upgrades "we cannot tell" to "we measured it"
5. **Vessel-class + time-policy limits** (~60 words)

---

## 5. Template requirements — verified from the supplied file

**File:** `TemplateAMICT2026 3.doc` — standard **IEEE conference template, A4 variant**, last saved by LEAU YU BENG, 2026-06-11. Template itself is 3 pages / 1,874 words of guidance.

### Geometry

| | |
|---|---|
| Page | A4, 8.27 × 11.69 in |
| Margins | Top **0.38″**, Bottom **1.00″**, Left/Right **0.62–0.63″** |
| Body | **Two columns**, equal width, **0.25″** gutter, no separator → ~**3.38″** per column |
| Title block | **Single column**, full width (title, author, abstract, keywords) |

### Styles

| Style | Spec |
|---|---|
| paper title | Times New Roman **24 pt** |
| Author | TNR 11 pt |
| Abstract | TNR **9 pt bold** |
| Keywords | Italic |
| Body Text | Inherits Normal — IEEE standard **10 pt** |
| Heading 1 | Small caps, **auto-numbered** (Roman) |
| Heading 2–4 | Italic |
| **Heading 5** | Small caps — **use for Acknowledgment and References** (unnumbered) |
| references | TNR **8 pt** |
| table head | TNR 8 pt small caps — **above** the table |
| figure caption | TNR 8 pt — **below** the figure |
| Save as | **Word 97-2003 `.doc`** |

### Rules that bite this specific paper

1. **`*CRITICAL: Do Not Use Symbols, Special Characters, Footnotes, or Math in Paper Title or Abstract.`** → **Δ_L2, %, ⊆, ⊥, ≻, A_AI(S), G(S) are all banned from title and abstract.** v4's abstract already writes "5.81 percent" (verified: three occurrences of "percent", zero of "%"). Any new title must also comply.
2. **All template guidance text must be removed.** The template states failure to do so *"may result in your paper not being published."*
3. **v4's HTML comment header must not survive conversion** — it names internal file paths and freeze authorities, and is a double-blind identity risk.
4. **Do not manually number headings.** v4 uses `## I. Introduction`, `## II. Related Work` etc. with hard-coded numerals; the template auto-numbers H1. Strip on import or headings will read "I. I. Introduction".
5. **Sub-titles are not captured in Xplore** and should not be used — rules out a colon-subtitle title.
6. **Figures and tables at top or bottom of columns only**, never mid-column, placed after first citation. Three tables in two-column layout is a real placement constraint.
7. No pagination. Define abbreviations on first use even if defined in the abstract. IEEE numeric citations `[1]`; give all author names unless six or more.

### Page budget — estimate only

Two-column 10 pt TNR on A4 runs roughly **900–1,000 words per full page**; the first page loses perhaps a third to the title block. Limit is **4–6 pages**.

v4 ≈ 4,700 words of real content + 3 tables + 19 references at 8 pt → **estimated 6 pages or slightly over**.

> ⚠️ **This is an estimate. Only converting the real text into the real template settles it.** The planner should treat "measure actual page count" as the first executable step, because every content decision depends on the answer. **v5 may need cuts before it can absorb any additions.**

---

## 6. Locked research position — what v5 must say

Authority: `docs/analysis/final-research-chain-lock.md`. Approved wordings are in its §T wording bank.

**Gap A (operationalisation, modest).** Advisory-type restriction by externally measured state is established in certified avionics; totality over incomplete observations in runtime verification; directional bounds from declared unmeasured variables in partial identification. Within the reviewed literature these were **not found composed** into one operational specification with `G(S)` and `A_AI(S)` separately specified over a classified multi-component environmental state for a human-facing low-resource DSS. **Not an architecture gap.**

**Gap B (empirical, stronger).** No characterisation identified of how often an intermediate advisory-scope state changes the admissible recommendation set relative to a participation-only gate over a multi-year environmental record.

**RQ1** — operational specification (can `G(S)` and `A_AI(S)` be separately specified with totality and containment preserved under structural unavailability; and which elements are designer-decided rather than source-derived).
**RQ2** — empirical characterisation and robustness.
**RQ3** — structural warrant of the multi-component classifier.

**Contribution hierarchy — do not reorder.** Primary: empirical characterisation. Secondary: domain operationalisation; operational specification separating `G(S)` from `A_AI(S)`. Supporting: formal contract-conformance; reproducibility/provenance methodology. **Architecture composition must not be promoted above the empirical contribution.**

**Formal properties — status labels are fixed.** P1 Totality = formalisation of an established mechanism. P2 Advisory-Scope Containment = design property. P3 Safety Dominance = contract-conformance under assumptions A1–A4. P4 Admissible-Set Equivalence of C1 and C3 = structural property; `C1 ↔ C3 = 0.00%` is **harness consistency, not empirical discovery**. None is new theory.

**Canonical figures — do not alter.** PRIMARY 43,848 records, departure-window n = 9,135, Δ_L2 = **5.81%**. RESOLUTION 28,501 records, n = 5,935, Δ_L2 = **4.48%**.

---

## 7. Explicit non-claims — inviolable

v5 must not be readable as claiming: accident reduction · improved safety outcomes · improved fisher decision quality · classification accuracy · optimal thresholds · optimal number of states · optimal `{Go, Delay}` · generalisation across Sabah · generalisation across vessel classes · AI prediction accuracy · causal effectiveness · novel fail-safe mechanism · novel state-gating mechanism · novel totality mechanism · novel advisory-inhibition mechanism.

Also preserve: `A_AI(CAUTION) = {Go, Delay}` is **researcher-defined** with a domain rationale from Gao (2024) and Rahim et al. (2024) — **not** empirically validated, optimal, or safer.

---

## 8. Open decisions for the planner

| # | Decision | Notes |
|---|---|---|
| 1 | **Output directory** | `amict-conference-rebuild-readiness-analysis.md` §B4 flagged this unresolved: keep under `publications/active/ipsci-2026/submissions/v5-*/` for contiguous review history, or open a new venue directory now that AMICT vs IPSci is clarified. **Do not overwrite v4 or any submitted artefact** |
| 2 | **Title** | Researcher wants a new title. Justified because the contribution changed, and safe because the prior round will be disclosed. Candidate: *"Empirical Characterisation of Graduated Advisory-Scope Governance in Low-Resource Maritime Decision Support"*. Must contain no symbols or math |
| 3 | **Content scope** | Which of the five additions in §4 fit the measured page budget. Recommend items 1–2 minimum |
| 4 | **What to cut** | If over 6 pages. Candidates: Related Work detail, TABLE I rows, parts of §III formalisation. **Not** the limitations |
| 5 | **Cover letter** | Must disclose the prior IPSci 2026 submission and outcome, state what changed, and raise the Review 2 misassignment factually for process reasons |
| 6 | **Architecture figure** | Omitted from v4 for space. Decide whether it returns |

---

## 9. Risks

| Risk | Note |
|---|---|
| **Format conversion is the critical path** | `FORMAT_READY = NO`; no .docx/.pdf/.tex has ever been produced from v4. Unknown duration. Measure page count first |
| **Overclaim creep under deadline pressure** | The single largest risk to research integrity. §7 is the guard |
| **Page limit may already be exceeded** | Additions may be impossible without cuts |
| **Same-body resubmission** | Non-disclosure would be discoverable at the candidate's own university. Disclose |
| **Turnitin < 30%** | v5 reuses substantial v4/v3 text; prior submission to the same body may already be in the index. Check early |
| **7-day window** | Falling back to v4 as-is is acceptable and defensible |

---

## 10. Authority order and key paths

1. `docs/analysis/final-research-chain-lock.md` — **wins on all research framing**; §T is the approved wording bank
2. `docs/analysis/canonical-revision-report.md` — what was already corrected and why
3. `docs/analysis/experiment-report-delta-l2.md` — current canonical wording of results, sensitivity, attribution, limitations
4. `docs/analysis/threshold-sensitivity-analysis.md` — full sensitivity, attribution, common-period data
5. `docs/analysis/rq-finalisation.md` — RQ structure and rationale
6. `docs/analysis/final-novelty-stress-test.md` — what is conceded to prior work and why
7. `publications/active/ipsci-2026/revision-notes.md` — rejection record and known v2.5 errors
8. `publications/active/ipsci-2026/submissions/v4-amict-rebuild/` — base manuscript and its audits
9. `publications/active/ipsci-2026/submissions/extended-abstract-2026-09-16/extended-abstract.md` — **submitted** IPSci 2026 extended abstract; see §12

**Do not edit:** submitted manuscripts · `.superpowers/**` · `*.before.md` · archived `data/**` artefacts · `docs/tasks/**` · historical session logs.

---

## 11. Known errors carried from v2.5 — check they are absent from v5

From `revision-notes.md`. All six TABLE II reference numbers were wrong in the submitted `.docx` and are already corrected in the `.md` lineage, but should be re-verified in v5: Tumato 2.0 `[16]→[14]` · Pro2Guard `[34]→[31]` · Kang GAIE `[25]→[22]` · Ghaleb et al. `[27]→[24]` · Sahoo AMAGF `[26]→[23]` · Baxi K-tier `[15]→[13]`. Also `[37]→[33]` (Gao) in body text; reference `[35]` was blank; the Acknowledgment contained placeholder text *"Will be add later!"*.

---

## 13. ADDENDUM 2 (2026-09-23) — the extended abstract was ACCEPTED; D-EA conditionally resolved

**Supersedes the risk framing in §12 in part. Read this before acting on §12.**

The IPoSCI 2026 committee has **accepted** the extended abstract for presentation. Full record: `publications/active/ipsci-2026/correspondence/2026-xx-xx-acceptance-iposci-2026.md`

### The decisive fact for v5

Accepted authors **choose one** publication route:

- IPoSCI 2026 e-Proceedings
- **AMICT IEEE Conference Proceedings**
- IJMIC

They are presented as **mutually exclusive**. So the AMICT track is not a parallel submission competing with an already-published abstract — it is one of three offered destinations for this work. If AMICT is elected and the abstract is consequently **not** published in the e-Proceedings, the prior-publication objection in §12 **largely dissolves**.

The committee states plainly that IPoSCI acceptance **does not** guarantee AMICT acceptance; AMICT applies its own submission, review and acceptance requirements. So v5 must still stand as a full paper on its own merits — nothing in §§1–11 is relaxed.

### D-EA — resolved, conditionally

> **D-EA (§12):** cite the extended abstract as prior work, or treat it as an unpublished precursor?

**Answer: treat it as an unpublished precursor — IF the author elects the AMICT route and the abstract is withdrawn from the e-Proceedings.** Under that condition v5 is the first publication of this work and needs no self-citation.

**This is conditional, not settled.** It holds only once the committee confirms **in writing** that electing AMICT keeps the abstract out of the e-Proceedings. Presentation at a symposium sometimes publishes the abstract regardless of the chosen full-paper venue. Until that answer arrives:

- Keep treating the **Turnitin <30%** exposure in §12 as live.
- Keep **rewriting** the Methodology and Results prose rather than lightly editing.
- Keep the **new title** requirement.

### 🔴 New blocker the planner must know about

The acceptance email set **15 September 2026** as the deadline to notify the committee of intent to submit a full paper to AMICT or IJMIC. **That date passed 8 days before this addendum was written.** Whether the AMICT route is still open is now an open question with the organisers — it is no longer safe to assume v5 has a guaranteed destination. **Planning may proceed, but the venue is unconfirmed.**

### Also newly known

- The final extended abstract must be delivered as **MS Word (.docx)** on the official **IPoSCI** template — a different document from the AMICT IEEE template in §5. Do not conflate them.
- **Reviewer comments exist but are not held.** They may contain substantive criticism relevant to v5's framing. Recover before planning is finalised.
- **CR3M is mandatory**: 3 minutes, one static slide, spoken word only.
- The call for abstracts states **3–5 pages**; the submitted artefact is 6.
- The organisers spell it **IPoSCI**.

---

## 12. ADDENDUM (2026-09-23) — a second submitted IPoSCI 2026 artefact exists

**This was not known when sections 1–11 were written. It changes the self-similarity picture and the planner must account for it.**

An **extended abstract** was submitted to the **IPSci 2026 proceeding** on **2026-09-16**, separately from the rejected full paper. It is now recorded at:

`publications/active/ipsci-2026/submissions/extended-abstract-2026-09-16/extended-abstract.md`

### What it contains

| Item | Value |
|---|---|
| Title | A GRADUATED SAFETY-STATE-GATED ARCHITECTURE FOR AI DECISION SUPPORT IN LOW-RESOURCE COASTAL FISHERIES |
| Authors | Mohd Iskandar bin Samsuddin; Rayner Alfred |
| Length | 6 pages, A4 |
| Headline results | **5.81% (PRIMARY, 9,135 records)** and **4.48% (alternative configuration, 5,935 records)** — the same figures v5 will report |
| Structure | Introduction (RQ1, RQ2) · Methodology (architecture, classification, historical evaluation, planned validation) · Results & Discussion · Conclusion |
| References | 12 — a subset of the v4 reference set |

### Why this matters for v5

1. **Title reuse.** The v5 plan already assumes a new title. This addendum makes that a requirement rather than a preference: the current title is attached to a submitted proceeding artefact *and* appears in `manuscript-v3.md`.
2. **Results reuse.** The 5.81% / 4.48% figures are already in a submitted IPSci artefact. v5 reporting the same numbers is normal research continuity, but the relationship must be **declared**, not silently repeated.
3. **Turnitin <30%.** The template rule in §5 is a hard gate. If the proceeding is indexed before AMICT similarity-checks v5, the extended abstract becomes a matching source against itself. The Methodology and Results prose are the highest-risk overlap — they must be **rewritten, not lightly edited**.
4. **Prior-publication policy.** Whether a published extended abstract in one venue's proceeding bars or constrains a full paper at AMICT is a **venue question, not a research question**. It must be confirmed with the organisers.
5. **RQ drift.** The extended abstract states RQ1 and RQ2 in wording that predates `rq-finalisation.md` and `final-research-chain-lock.md`. Where they differ, **the lock wins** — see §0. Do not import RQ wording from the extended abstract.

### Open decision added for the planner

> **D-EA.** Does v5 cite the IPSci 2026 extended abstract as prior work by the same authors, or treat it as an unpublished precursor? This affects the reference list, the novelty statement, and the similarity declaration. **Do not decide this without confirming the proceeding's publication status.**

### Provenance of the transcription

No Markdown or Word source existed in the repository — the document was authored outside the connected folder and printed to PDF from macOS on 2026-09-16 15:19 +08. 8-gram containment against all repo Markdown peaked at **6.58%** (`manuscript-v3.md`), almost entirely bibliography; the only non-bibliographic matches were the title string and the `E = {w, r, m, o, v, t}` notation. The `.md` is a frozen transcription for the provenance record; **the submitted PDF remains authoritative**. Figure 1 is a raster image and was not transcribable.

---

*Sections 1–11: discovery complete, no planning performed, no files modified other than the creation of this document. Section 12 added 2026-09-23 after the submitted extended abstract was located and transcribed. Section 13 added 2026-09-23 after the acceptance email was relayed — it partly supersedes §12 and adds an unresolved venue blocker.*
