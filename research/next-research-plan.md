# Next PhD research plan
## Decision after reviewing the consolidated Scopus AI matrix · 17 November 2026

---

## Contributors and attribution

| Tag | Contributor | Contributed here |
|---|---|---|
| **[GPT]** | GPT | Sections 1–5: the decision, the evidence review, the research sequence, the preparation block, the confirmatory comparison and the exit criteria. Section 7: follow-up citation checks and response to Claude’s review |
| **[Claude]** | Claude (Cowork session, 16–17 Nov 2026) | Section 6: primary-source verification of the citations in §1, and the open items raised against §3 and §4. Section 8: manual verification queue for the citations that cannot be checked automatically, and the close-out of O-1 to O-3. Also `pilot-preparation-audit.md`, which §3 draws on |
| **[Iskandar]** | Iskandar Samsuddin | Direction and final decision on every item |

Untagged text is the agreed plan. A tagged block is one contributor's finding, comment or
correction; it does not amend another contributor's text, and the original author decides
what to carry into the next version.

---


**Decision — start preparation for the comparative advisory study.** Keep a degraded-information permission method as a conditional follow-on. Use formal policy definitions to fix the treatments, outputs and assumptions for both studies. The immediate deliverable is a reviewable feasibility package for a small-vessel predeparture task.

This plan draws on the [Scopus AI working matrix](../papers/consolidated-literature-review-gap-matrix.md), [independent novelty assessment](../docs/analysis/graduated-advisory-safety-novelty-assessment.md), and [pilot readiness audit](pilot-preparation-audit.md). The Scopus AI material identifies papers for screening. This plan uses targeted primary-source checks for the following decisions. It does not report a new systematic database search.

## 1. What the matrix changes  ·  *[GPT]*

| Evidence checked | Consequence for our study |
|---|---|
| Kim et al. use two reliability-qualified clinical decision zones and a gray zone that requires human review. They quantify the workload transferred to reviewers. [Primary paper](https://www.nature.com/articles/s41746-026-02450-7) | A third state and a metric for its prevalence or burden are established prior art. Test the quality and usefulness of advice retained in the middle region. |
| Ghaleb et al. use calibrated execution, pause/re-observe and planner fallback. Their simulation evaluates success, collisions and intervention burden under domain shift. [Primary paper](https://doi.org/10.3390/s26103140) | Uncertainty-aware thresholds, three modes and degraded-input trade-offs already have an empirical precedent. Include a tuned uncertainty-aware comparator. A future method needs to solve a specific, observed failure. |
| Tayebati et al.'s CAP selects point predictions, set-valued predictions or abstention based on context and downstream utility. [Primary paper](https://proceedings.mlr.press/v304/tayebati26a.html) | Add CAP to the core comparison even though it is absent from Matrix A. Partial output at adjustable risk is already established. Score the operational effect of advice type, omission and fallback separately. |
| Vaaler et al. combine maritime RL with predictive safety filters. Miller et al. simulate risk-adaptive maritime oversight with escalation and fallback. [Vaaler et al.](https://www.sciencedirect.com/science/article/pii/S0004370224001371), [Miller et al.](https://doi.org/10.3390/app16146903) | Maritime application and hybrid filtering offer little priority by themselves. Use a small-vessel advisory decision and an independently assessed recommendation endpoint. |
| Corsi et al.'s dynamic shield adapts permissions to a parameterized specification at runtime. ProSh uses a learned cost critic and a risk-budget augmentation in model-free RL. The public manuscripts have different titles and authorships from the two related papers held locally. [Corsi et al., ATVA 2025](https://software.imdea.org/~cesar/publication/2025-corsi25efficient/), [ProSh, AAMAS 2026 extended abstract](https://doi.org/10.65109/KCVZ6904), [AAAI-25 comparison record](https://ojs.aaai.org/index.php/AAAI/article/view/33767) | Read the corresponding full texts for the methodological comparison. Compare the assumptions behind any proposed action-specific evidence requirement with adaptive and probabilistic shielding. |

Treat Matrix G as an inventory of local holdings. Some papers absent locally are reachable online. Matrix G now records CARAC separately as untraceable in the local corpus. Keep it out of the evidence for the novelty claim until a primary source is identified.

## 2. Research sequence and publication mapping  ·  *[GPT]*

| Work | Research question | Role |
|---|---|---|
| Formal foundation, matrix RQ1/C1 | What information is available to a policy at decision time, and what counts as an advisory, a withheld message or an available fallback? | Specify observations, permissions, outputs and assumptions. Reuse the existing thesis and Journal 1 formal work. |
| Next empirical study, matrix RQ2/C2 | Under what conditions does withholding specific categories of advice reduce independently judged harm, and can partial advice preserve more useful coverage than tuned whole-message abstention? | Main study. Addresses G4/G5/G9, with a defined degraded-input analysis contributing to G6. Provisionally use the repository's existing **Journal 2** slot. Matrix F's “Journal Paper 1” describes this first new study and could be confused with the existing formal Journal 1. |
| Conditional methods study, matrix RQ3/C3 | Can advice-specific information requirements improve on shared uncertainty cutoffs and conservative fallback under observed failures? | Independent follow-on only if a reproducible failure, a distinct mechanism and an informative baseline comparison emerge. Resource cost (C4) supports this claim if measured on representative hardware. |

Use **predeparture advice for one small-vessel class and one route type near Kota Kinabalu** as the working case. Confirm the vessel and route definition with the data audit. Keep final human decision authority fixed. Example candidate contents are a specific departure window, a conditional verification step, a delay message, and an empty advisory with a common status cue. Use examples as calibration stimuli. Freeze the final action taxonomy after checking the actual forecasts, available verification channels and expert interpretation.

## 3. First preparation block  ·  *[GPT]*

| Workstream | First action | Reviewable output and exit condition |
|---|---|---|
| Primary-paper challenge | Read the methods and comparisons of Kim, Ghaleb, CAP, Vaaler, Carr and Gerold–Lucia, then use the results to direct a second pass to Corsi, Miller, ProSh and unresolved CARAC. Record DOI/version, decision authority, inputs, intermediate behaviour, harm reference, comparator calibration, fault assumptions and key evidence locations. | A method-by-method comparison with the strongest equivalent near-match and a claim scoped to actual differences. Separate publication records, full-text findings and Scopus-only leads. |
| Matched data | Seek a sample of maritime forecast records containing issue time, valid time, horizon, source/version, location/grid and variables. For prospective collection also record retrieval time and outages. Join a sample to independent observations and a vessel/route dossier. Document retention and licensing. | A sample join that reconstructs what the policy could know, with a separate reference dossier. If a local historical archive cannot be secured, evaluate prospective capture lead time. Use reanalysis for scenario sampling and engineering checks. |
| Independent reference | Draft a rubric for inappropriate specificity, operationally useful guidance, harmful omission and justified silence. Build paired cases just below, at and just above applicable gate cutoffs, including 1.00 m and 1.25 m wave height, 21.6 kn wind, 10.0 mm/hr rain and exact sunrise. Add matched cases that hold gate inputs fixed while varying route exposure, verified sea conditions or vessel/load evidence. Blind raters to gate states and document the evidence supporting each label. Draft institutional ethics materials as applicable before involving raters. | A small blinded calibration exercise with scored examples, per-construct agreement before adjudication, indeterminate rates and a provenance check showing how reference criteria were selected independently. Agreement with the gate alone can neither prove nor disprove independence. |
| Candidate advice | Hand-author contrasting messages for the reference exercise, including plausible unsafe and useful outputs. Separately plan a reproducible generator or fixed ranked pool defined before held-out scoring. Use the same pool and display conventions across policies. | Candidate inventory with full text and type, enough eligible messages to exercise the intermediate filter, and labeled cases where a filter can remove, preserve or introduce a safety issue. Hand-authored examples establish scoring feasibility. Estimate prevalence from a representative cohort. |
| Precision and comparator check | Identify event clusters and prespecify meaningful harm and useful-coverage margins. Use preparation data to estimate paired discordance and assessor uncertainty. Draft a validation-only threshold calibration rule. | A precision plan based on events and discordant outcomes, with event-level splits and a comparator that uses matching observations. The readiness audit's rough 85–123 CAUTION weather-event groups are a planning sensitivity range. |

Start with primary-source extraction, a data inventory/request draft and a draft rubric in parallel as workstreams. A representative availability check should consider archived issue-time products, a prospective collection option, and independent observations or vessel-specific engineering assessment. Prepare the data request and any applicable ethics materials now. The first supervisor review should assess those drafts and select the route class and feasibility sample. Once the project lead authorizes the relevant actions and data access is in place, submit the requests and start prospective capture of permitted forecast records in parallel with supervisor review. Log the earliest recoverable issue time and expected time to accumulate usable events. Begin rater recruitment after any required ethics approval.

## 4. Confirmatory comparison after preparation  ·  *[GPT]*

1. **Core paired contrast.** Compare C1 participation-only (Matrix E B1) with C2 static graduated (Matrix E B3) using the same outer cutoff, candidate ranking and common status information. Estimate the paired difference in severe inappropriate advice per eligible episode. Record harmful omissions separately and report actual differences in displayed content. Use C0 unrestricted as an ungated reference and B2 conservative binary (withhold at CAUTION and UNSAFE) as a secondary comparison. C1 also represents the permissive binary policy, so it appears once in the analysis.
2. **Fair safety–usefulness comparison.** Calibrate an uncertainty-aware whole-message binary policy on validation events using the same information available to the graduated policy. Compare severe harm at matched useful coverage, or coverage at a prespecified harm level. Account for whether a person can actually access any suggested verification or fallback. Report false suppression and newly introduced harm. Compare against a simple action-specific evidence rule if it is implementable from the same inputs.
3. **Robustness analysis.** Start with forecast staleness and critical-channel dropout that can be characterized from available data. Add source disagreement or correlated failure when supported. Keep the underlying reference dossier fixed for within-episode input perturbations. Report clustered intervals across weather events and test whether observed failures recur on a withheld season or distinct site. Simulated perturbations support claims about the tested perturbation regimes.

A later methods paper is warranted if these results reveal a repeatable failure that tuned abstention, static graduated gating and a simple advice-specific rule cannot resolve. One candidate to investigate is separate evidence requirements and expiry for different advice types, allowing a verification step when specific timing advice has lost its support. Treat this as a design hypothesis. Compare it with confidence-only gating and straightforward per-type freshness thresholds before claiming a new mechanism. A resource-constrained contribution would additionally need a specified budget and measurements on representative hardware.

## 5. Decision at the end of preparation  ·  *[GPT]*

- **Advance** if an issue-time data path and independent reference are viable, candidate contrasts are meaningful, and the study can resolve prespecified practical margins with independent event clusters.
- **Narrow** to a scenario-based feasibility study if expert reference testing works but issue-time records or independent hazard matching are insufficient. Bound conclusions to the sampled vignettes and defer real-input robustness claims.
- **Stop the safety-effectiveness claim** if the reference reduces to the gate's rules or meaningful contrasts cannot be estimated. Report the feasibility result and reassess the direction with the supervisor.
- **Defer the second paper** until the comparative study identifies a failure worth solving and primary-source analysis shows how the solution would differ from existing methods.


---

## 6. Review record  ·  *[Claude]*

*Added 17 November 2026. Nothing in sections 1–5 was changed. This section records what
primary-source checks returned, and three items that are open for GPT and Iskandar to settle.*

### 6.1 Citation checks on §1

Every URL cited in §1 was fetched and read from the publisher's page. Six of eight resolved.
Full records are in [Matrix H](../papers/consolidated-literature-review-gap-matrix.md).

- **The Corsi / ProSh question raised in §1 is resolved.** §1 notes that "the public manuscripts
  have different titles and authorships from the two related papers held locally." They do, and
  they are different papers. *Efficient Dynamic Shielding for Parametric Safety Specifications*
  (Corsi, Mallik, Rodriguez, Sanchez, arXiv:2505.22104) is not the locally held
  *Verification-Guided Shielding*; *ProSh* (Hamel-De le Court, **Ohlmann**, Belardinelli,
  arXiv:2510.15720, **October 2025**) is not the locally held AAAI-25 paper, which lists Goodall
  and never uses the name ProSh. Both of the new records are **preprints**, and ProSh is 2025,
  not the 2026 Matrix A gives.
- **CAP should be cited as ACML 2025, PMLR v304**, not 2026. The full title is *CAP: Conformalized
  Abstention Policies for Context-Adaptive Risk Management for LLMs and VLMs*.
- **Ghaleb et al. is a robot-manipulation paper** (Vision–Language–Action under domain shift),
  not an advisory or maritime one. The mechanism precedent §1 draws from it stands; the domain
  proximity implied by Matrix A's "very close competitor" does not.
- **CAIS is single-authored** — Tymoteusz Miller — and the same Miller as the Adaptive Human
  Oversight paper, so §2's treatment of them as one programme is right.
- **Two could not be verified.** The ScienceDirect PII for Vaaler et al. and the AAAI record for
  the shielding paper both refused automated retrieval. Neither is contradicted; both are simply
  unconfirmed, and should be checked by hand before either is relied on.
- **CARAC is weaker than §1 states.** §1 asks that its title, DOI and provenance be marked
  unresolved. It is not only absent from the reports under that acronym — it has no traceable
  source anywhere in this corpus. Matrix G's position statement has been corrected accordingly.

### 6.2 Open items

| ID | Item | Why it matters | Proposed resolution |
|---|---|---|---|
| **O-1** | §3 ends "No experiment results, external requests or participant recruitment are part of this planning step," and gates the data route on the first supervisor review | The pilot audit put ethics submission and prospective issue-time capture on the critical path *because delay there is unrecoverable* — reanalysis cannot be back-filled with issue times, so each month of drafting-without-sending is a month of data the study will never have | Split "draft" from "submit" explicitly. Draft the data request and the ethics materials in the first block as §3 says, but let the ethics submission and prospective capture start **in parallel with** the supervisor review rather than after it |
| **O-2** | §4.1 names B1 as the main paired comparator ("B1 participation-only") and then uses "permissive and conservative binary policies as bounds" — B1 is both the treatment contrast and a bound. Matrix E defines B1 as the permissive binary gate and B2 as the conservative one | The main contrast and the bracketing baselines would be reported under the same label. In the repository's existing comparator language the participation-only arm is C1 | Rename so the paired contrast is explicit and separate from the two bounds, and align the labels with the C0/C1/C2 scheme already used in `scripts/condition_comparison.py` and the Journal 1 evaluation specification |
| **O-3** | §3 requires "a provenance check showing how reference criteria were selected independently," and correctly notes that agreement with the gate alone settles nothing — but no procedure follows | Reference independence is the single condition that decides whether the safety-effectiveness claim is possible at all. Without a stated test it cannot be evidenced at the review | Name the boundary-scenario test from the pilot audit: rate the cases sitting exactly on 1.00 m, 1.25 m, 21.6 kn, 10.0 mm/hr and exact sunrise, and report whether rater judgement tracks those thresholds or diverges at the margin. A reference that reproduces the gate's cut points is procedurally but not substantively independent |

### 6.3 Points of agreement worth recording

- §2's observation that Matrix F's "Journal Paper 1" collides with the existing `publications/active/journal-1/` is correct; that slot holds the formal-architecture paper, still in research-design phase and unsubmitted.
- §3's use of the 85–123 CAUTION weather-event range as a *planning sensitivity range* rather than a result is the correct reading of the audit.
- §1's instruction to treat Matrix G as an inventory of local holdings, not of availability, is right and has been carried into Matrix G itself.


## 7. Response to the review · *[GPT]*

*Added 17 November 2026. Sections 1, 3 and 4 incorporate the changes below. Section 6 records Claude’s original review.*

- **O-1 — Timing.** Separate drafting from submission and capture. Issue-time capture can begin in parallel with supervisor review once authorized and feasible. Confirm the forecast source and operational definition of an episode early. Ethics approval, where required, precedes rater recruitment.
- **O-2 — Comparator identity.** The primary paired contrast is C1 versus C2. C1 and B1 denote the same permissive participation-only policy. C0 and B2 are named separately as secondary comparisons, alongside the separately calibrated whole-message comparator.
- **O-3 — Reference independence.** The preparation block now names the threshold-boundary and matched-context tests. Agreement at a threshold can be justified by independent physical evidence. Evaluate it alongside source provenance, rater reasoning, and whether off-gate context appropriately changes judgments with the policy inputs held fixed.
- **Citation follow-up.** The indexed publisher records confirm the two identities left open in §6.1. Vaaler et al. is an *Artificial Intelligence* article published in 2024. The AAAI-25 shielding paper lists Hamel-De le Court, Belardinelli and Goodall. These checks establish bibliographic identity and abstract-level scope. [Vaaler et al.](https://doi.org/10.1016/j.artint.2024.104201), [AAAI proceedings record](https://ojs.aaai.org/index.php/AAAI/article/view/33767)
- **Publication versions.** Corsi et al. has an ATVA 2025 proceedings version. ProSh has a 2025 arXiv manuscript and a distinct AAMAS 2026 proceedings extended abstract of the same work. Use the 2026 citation when citing the proceedings abstract and identify the fuller manuscript where it supplies method details. [Corsi coauthor’s publication record](https://software.imdea.org/~cesar/publication/2025-corsi25efficient/), [ProSh proceedings abstract](https://doi.org/10.65109/KCVZ6904), [ProSh manuscript](https://arxiv.org/abs/2510.15720)


---

## 8. Manual verification queue  ·  *[Claude]*

*Added 17 November 2026. Six citations cannot be settled from this session: four pages refuse
automated retrieval, one DOI does not resolve, and one record has no identifier at all. Each
needs a human with a browser. Open the link, read the publisher's own page, and write the
answer into the **Found** column — then the matching row in Matrix H can be closed.*

### 8.1 Status of §7's citation follow-up

§7 states that "the indexed publisher records confirm the two identities left open in §6.1."
Re-checking on 17 November returned a more mixed result, so the three claims are separated here:

- **Corsi / ATVA 2025 — corroborated.** A co-author's institutional publication page gives
  *Efficient Dynamic Shielding for Parametric Safety Specifications*, Corsi, Mallik, Rodríguez,
  Sánchez, ATVA'25, LNCS 16145, pp. 157–179, Springer 2025. This is a real improvement on the
  preprint citation, and it withdraws my earlier "both are preprints" remark. Still worth one
  publisher-side check (MV-4) because a personal page is a secondary source.
- **Vaaler — advanced but not confirmed.** The DOI `10.1016/j.artint.2024.104201` does redirect
  to PII `S0004370224001371`, which reconciles §1's PII with §7's DOI — they are the same
  article. The article page itself then returned empty, so the title, authors, journal and year
  are **still unverified** (MV-1).
- **AAAI-25 and the ProSh AAMAS abstract — not confirmed.** The AAAI page is still bot-blocked
  (MV-2) and the DOI `10.65109/KCVZ6904` does not resolve (MV-3).

### 8.2 The queue

| ID | Item | Link to open | What to record | Why it matters | Found |
|---|---|---|---|---|---|
| ~~**MV-1**~~ | Vaaler et al. (2024), marine navigation | — | — | — | **CLOSED 17 Nov [Iskandar supplied, Claude verified].** Every detail in §7 confirmed. Record in §8.8 |
| ~~**MV-2**~~ | AAAI-25 shielding paper | — | — | — | **CLOSED 17 Nov [Iskandar supplied, Claude verified].** Record below in §8.6. The `ojs.aaai.org` page is still bot-blocked, but the publisher PDF settles it directly |
| ~~**MV-3**~~ | ProSh proceedings version | — | — | — | **CLOSED 17 Nov [Iskandar supplied, Claude verified].** The DOI is real and §7's reading was right. Record in §8.7 |
| ~~**MV-4**~~ | Corsi et al. ATVA 2025 | — | — | — | **CLOSED 17 Nov [Claude].** The proceedings version exists, so the row is peer-reviewed — but the citation year is **2026**, not 2025. §8.12 |
| ~~**MV-5**~~ | Li et al. (2024), **CARAC** | — | — | — | **CLOSED 17 Nov [Iskandar supplied, Claude verified].** Record confirmed from the publisher PDF. The open question is no longer the citation but whether the row belongs in Matrix A — §8.10 |
| ~~**MV-6**~~ | CAP citation year | — | — | — | **CLOSED 17 Nov [Iskandar flagged, Claude verified].** Cite 2025. PMLR assigns no DOI — see §8.11 |

### 8.3 How to close a row

Record what the page actually says, including when it contradicts the expectation — a
mismatch is the finding, not a failure. Paste the result into the **Found** column with
your initials and the date, then update the matching row in
[Matrix H](../papers/consolidated-literature-review-gap-matrix.md) and delete nothing: the
superseded reading stays visible so the trail from Scopus AI summary to verified record is
auditable at the defence.

### 8.4 Open items O-1 to O-3 are closed  ·  *[Claude]*

§7 resolves all three, and §3 and §4 carry the changes. Recorded for the trail:

- **O-1 closed.** §3 now separates drafting from submission, authorises capture to begin in
  parallel with supervisor review, and asks for the earliest recoverable issue time to be
  logged. The sentence O-1 quoted no longer appears in §3; §6.2 preserves it as the
  historical record.
- **O-2 closed.** §4.1 now reads C1 participation-only (Matrix E B1) against C2 static
  graduated (Matrix E B3), with C0 ungated and B2 conservative as separate secondary
  comparisons, and states explicitly that C1 appears once. The double-duty label is gone.
- **O-3 closed, with a correction I accept.** §7 is right that agreement at a threshold can be
  justified by independent physical evidence, so threshold agreement alone does not show
  dependence. My framing treated it as close to decisive; the multi-signal version in §7 —
  provenance, rater reasoning, and whether off-gate context shifts judgement with policy
  inputs held fixed — is the better test.

### 8.5 Correction: a source supplied as Vaaler et al.  ·  *[Claude]*

*17 November 2026.* A PDF was added to the discussion as "from Vaaler et al." The file is a
different paper:

| Field | Value |
|---|---|
| Title | *Safe reinforcement learning via adaptive robust model predictive shielding* |
| Authors | Hilde Gerold, Sergio Lucia (Chair of Process Automation Systems, TU Dortmund University) |
| Venue | Computers and Chemical Engineering **206** (2026), art. 109521 |
| Dates | Received 31 Jul 2025; revised 8 Dec 2025; accepted 9 Dec 2025; online 10 Dec 2025 |
| DOI | 10.1016/j.compchemeng.2025.109521 · open access CC BY 4.0 |
| Domain | Chemical process control — nonlinear continuous stirred tank reactor under parametric uncertainty |

This is the **Gerold–Lucia** entry already on the §3 reading list and already cited in the novelty
assessment, not the Vaaler maritime paper. Two consequences:

- **MV-1 stays open.** Vaaler et al. is still unverified and still not held. The DOI
  `10.1016/j.artint.2024.104201` and PII `S0004370224001371` are confirmed to be the same record,
  but nothing about its title, authors or subject has been read from a publisher page.
- **Gerold and Lucia is now held**, at
  `papers/sources/Safe reinforcement learning via adaptive robust model predictive shielding.pdf`.
  It was previously cited but not in the corpus, so one item on the §3 reading list is now closed.

**Why this one matters more than its filing.** The paper puts an adaptive safety parameter into the
RL observation space so the agent varies its own conservativeness at run time. Its evaluation shows
the adaptive-robust configuration holding constraint violations at zero while using the backup policy
less often than the fixed-robust configuration. That is the same claim shape as RQ3 and C3 — safety
preserved at lower cost in unnecessary restriction — already demonstrated in a published, peer-reviewed
setting. It does not pre-empt the PhD, whose setting is advisory rather than control and whose
restriction is over recommendation categories rather than actions, but C3's stated obstacle ("need a
new mechanism beyond existing uncertainty-aware methods") should be argued directly against this paper.
Matrix A has no row for it; it should.

### 8.6 MV-2 closed: the AAAI-25 shielding paper  ·  *[Claude]*

*17 November 2026.* A PDF was supplied for MV-2. Its own embedded metadata and title page settle the
record without needing the blocked `ojs.aaai.org` page.

| Field | Value | Source |
|---|---|---|
| Title | *Probabilistic Shielding for Safe Reinforcement Learning* | PDF `Title` field and title page |
| Authors | Edwin Hamel-De le Court, Francesco Belardinelli, Alexander W. Goodall (Imperial College London) | PDF `Author` field and title page |
| Venue | The Thirty-Ninth AAAI Conference on Artificial Intelligence (**AAAI-25**), proceedings p. 16091 | PDF `Subject` field and page footer |
| Year | 2025 — "Copyright © 2025, Association for the Advancement of Artificial Intelligence" | Title page |
| Length | 9 pages | PDF |

**The supplied file is byte-identical to the copy already in the corpus** — SHA-256
`8598908f…a2bd6679`, matching `papers/sources/Probabilistic Shielding for Safe Reinforcement
Learning.pdf`. Nothing was added; the holding recorded in Matrix G was already correct.

**This confirms the two papers are distinct, on four independent grounds.** The AAAI-25 paper and
ProSh (arXiv:2510.15720) differ in title, in third author (Goodall against Ohlmann), in method — the
AAAI-25 paper augments the MDP state and derives the shield from Value Iteration over safety costs,
while ProSh uses a learned cost critic with risk-budget augmentation in model-free RL — and in
naming: the string "ProSh" appears **zero** times in the AAAI-25 PDF. Matrix A's row describes
"probabilistic shielding using risk budgets", which is ProSh, so Matrix A is pointing at the preprint
and the corpus holds the other paper. Both belong in the comparison; only one is currently listed.

### 8.7 MV-3 closed: the ProSh proceedings version  ·  *[Claude]*

*17 November 2026.* A PDF was supplied for MV-3. It is the AAMAS proceedings artefact, and it settles
the DOI question directly.

| Field | Value |
|---|---|
| Title | *ProSh: Probabilistic Shielding for Model-free Reinforcement Learning* |
| Authors | Edwin Hamel-de le Court† (Imperial College London), Gaspard Ohlmann† (Independent Researcher, Mulhouse), Francesco Belardinelli (Imperial College London). † equal contribution |
| Venue | **Extended Abstracts**, Proc. of the 25th International Conference on Autonomous Agents and Multiagent Systems (**AAMAS 2026**), Paphos, Cyprus, 25–29 May 2026, IFAAMAS — proceedings p. 3411 |
| Length | **3 pages** |
| DOI | **10.65109/KCVZ6904** — printed in the paper's own ACM reference format and footer |
| Licence | CC BY 4.0 |
| Full version | arXiv:2510.15720, cited in the abstract as reference [7]: "The full version of this paper is available at [7]" |

**§7 was right on every point.** The DOI exists, the AAMAS 2026 extended abstract exists, and it is
the same work as the 2025 arXiv manuscript. The earlier failure was the DOI resolver, not the record.
Cite as §7 proposed: **the AAMAS 2026 extended abstract for the proceedings record, the arXiv
manuscript where method detail is needed.**

**One qualification for the defence.** This is a 3-page extended abstract, not a full paper. The
method is public either way, but a reviewer weighing prior art may treat a short abstract differently
from a full peer-reviewed paper, so it is worth citing both forms rather than the abstract alone.

**Bonus — MV-2 gains a canonical DOI.** The reference list of this abstract cites the AAAI-25 paper as
`doi.org/10.1609/AAAI.V39I15.33767`. That is the canonical DOI for *Probabilistic Shielding for Safe
Reinforcement Learning*, and its article id `33767` matches the `ojs.aaai.org` link in §7 — so the link
GPT supplied was pointing at the right record all along, and only the bot protection stood in the way.

The file is held at `papers/sources/ProSh - Probabilistic Shielding for Model-free Reinforcement
Learning.pdf`. With Gerold–Lucia (§8.5) and this, the corpus has gained two primary sources today.

### 8.8 MV-1 closed: Vaaler et al.  ·  *[Claude]*

*17 November 2026.* The paper was supplied and verified from the publisher's own typeset PDF.

| Field | Value |
|---|---|
| Title | *Modular control architecture for safe marine navigation: Reinforcement learning with predictive safety filters* |
| Authors | Aksel Vaaler, Svein Jostein Husa, Daniel Menges, Thomas Nakken Larsen, Adil Rasheed — Dept. of Engineering Cybernetics, NTNU; Rasheed also SINTEF Digital |
| Venue | **Artificial Intelligence 336 (2024), art. 104201**, Elsevier |
| Dates | Received 15 Jul 2023; revised 21 May 2024; accepted 8 Aug 2024; online 13 Aug 2024 |
| DOI | **10.1016/j.artint.2024.104201** · open access CC BY 4.0 · 24 pages |

**Everything §7 claimed is confirmed**, including the DOI, the journal and the 2024 year. Matrix A's
description — RL combined with predictive safety filters, maritime, "very close competitor" — is
accurate. Held at `papers/sources/Modular control architecture for safe marine navigation -
Reinforcement learning with predictive safety filters.pdf`.

**What it actually does, and where the PhD differs.** A predictive safety filter takes a potentially
unsafe control action from the main controller and solves an optimisation for the *minimal
perturbation* satisfying physical and safety constraints, allowing arbitrary control policies in a
task-agnostic way. It is evaluated on a simulated Cybership II supply-ship replica for path following
and collision avoidance, and the headline result is that the filter keeps the vessel safe **without
degrading the RL agent's learning rate or performance** — a safety-at-no-usefulness-cost claim, in a
maritime setting.

That is the closest domain match in Matrix A, so the difference has to be stated precisely rather than
by domain. Vaaler et al. filter **control actions of an autonomous vessel**, using a dynamics model and
an optimisation over continuous actions. The proposed study restricts **advisory recommendation
categories offered to a human operator**, with no vessel dynamics model, no actuation, no control loop
to filter, and unconditional human authority preserved throughout. §1's judgement that "maritime
application and hybrid filtering offer little priority by themselves" is right, and this is the paper
that makes it so.

### 8.9 MV-4 narrowed, not closed: the Corsi upload is the preprint  ·  *[Claude]*

*17 November 2026.* A PDF was supplied with the question "is this MV-4?" — **not quite.** It is the
arXiv preprint, which is useful but is the one artefact MV-4 already had.

| Field | Value |
|---|---|
| Title | *Efficient Dynamic Shielding for Parametric Safety Specifications* |
| Authors | Davide Corsi (University of California, Irvine), Kaushik Mallik (IMDEA Software Institute), Andoni Rodríguez (IMDEA / Universidad Politécnica de Madrid), César Sánchez (IMDEA) |
| Version | **arXiv:2505.22104v2 [cs.AI], 18 August 2026** — stamped down the left margin; PDF `Creator` is "arXiv GenPDF" |
| Length | 23 pages |

**Why it does not close MV-4.** MV-4 asks for *publisher-side* confirmation of the ATVA 2025
proceedings version — LNCS volume, page range, year. This document carries no Springer copyright
page, no LNCS pagination, and **no statement that a version appeared at ATVA**. Its single mention of
ATVA is a bibliography entry for somebody else's ATVA 2021 paper. The typography is the Springer
`llncs` class, which is what a camera-ready submission looks like before the publisher typesets it,
but that is a style, not a publication record.

**What it does settle.** The title and the four-author list are now confirmed **from the paper
itself**, where before they rested only on a co-author's homepage. The v2 date of 18 August 2026 also
falls after the October 2025 conference, which is consistent with a post-conference revision and
explains Matrix A's "(2025/2026)" hedge.

**What would close MV-4:** the Springer chapter page at `doi.org/10.1007/978-3-032-08707-2_8`, or the
ATVA 2025 proceedings front matter, or a Springer-typeset PDF showing pp. 157–179 of LNCS 16145. Any
one of those settles whether this row is peer-reviewed or preprint-only — which is exactly the
distinction §8.1 flagged as mattering to a reviewer.

Held at `papers/sources/Efficient Dynamic Shielding for Parametric Safety Specifications - arXiv
preprint v2.pdf`, named so the preprint is not later mistaken for the proceedings version.

### 8.10 MV-5 closed: CARAC identified, and it is not what Matrix A implies  ·  *[Claude]*

*17 November 2026.* The paper was located by web search, then supplied and verified from the publisher's typeset PDF.

| Field | Value |
|---|---|
| Title | *Context-Aware Risk Attribute Access Control* |
| Authors | **Binyong Li**, Fan Yang (corresponding), Shaowei Zhang — School of Cybersecurity, Chengdu University of Information Technology; Zhejiang Geely Holding Group; Advanced Cryptography and System Security Key Laboratory of Sichuan Province |
| Venue | *Mathematics* (MDPI) **12**(16), art. 2541 |
| Published | 17 August 2024 · open access |
| DOI | **10.3390/math12162541** |
| Acronym | Defined in §3.1 as "context-aware risk attribute access control (CARAC) model" |

**The attribution in Matrix A is correct.** First author Li, year 2024, acronym CARAC — all three match.
A follow-up search for any other 2024 CARAC in an AI-safety sense returned nothing.

**But the domain does not match, and this is the finding.** The paper is **information-security access
control**: it decides which *users* may access which *resources*, by scoring each access request against
a multi-level contextual risk indicator system, weighting the risk factors with a game-theoretic
combination of subjective and objective weights, and using smart contracts to monitor behaviour during
a session and revoke privileges. It does not restrict the actions of an AI or autonomous system at all.

Matrix A grades it a **"very close conceptual competitor"** whose relationship to the PhD is "mapping
risk to permitted actions." That is true only in a loose analogical sense: the permitted actions are a
user's requests to read data, not an advisory system's recommendations, and the risk is a security risk
score, not an environmental hazard state. This is the RBAC/ABAC/RAdAC access-control literature, which
is a different field from AI action restriction.

**It also explains the Matrix G anomaly.** CARAC is absent from all 21 Scopus AI reports because those
searches were framed in AI-safety terms. The paper was never missing; it simply does not live in that
literature.

**Recommendation to GPT and Iskandar — this is a judgement call, not a correction, so it is left open.**
Either withdraw the row, or keep it and relabel it explicitly as a cross-domain analogy from access
control rather than a competitor, downgraded from "very close conceptual competitor". Leaving it as it
stands is the risky option: a reviewer who looks it up will find a cybersecurity access-control paper
listed among runtime shielding and safe-RL work, and will question how the rest of Matrix A was graded.

**Confirmed from the PDF (17 Nov).** Received 28 Jun 2024, revised 12 Aug, accepted 15 Aug, published
17 Aug 2024; CC BY 4.0; 20 pages; MSC 68U01; keywords "game theory-based weight assignment; risk
assessment; adaptive access control". The acronym is real and load-bearing — **CARAC appears 21 times**
and §3 is headed "CARAC Access Control Model". The author-order doubt raised from the MDPI web page is
**resolved**: the paper's own citation block reads *Li, B.; Yang, F.; Zhang, S.*, so "Li et al. (2024)"
is correct, with Fan Yang as corresponding author.

**The domain mismatch is now measured, not inferred.** Word counts across the full text: *access
control* 106, *user* 156, *smart contract* 37 — against *autonomous* **0**, *reinforcement learning*
**0**, *shield* **0**, *advisory* **0**, *AI agent* **0**. The paper contains no AI-safety content of
any kind.

Held at `papers/sources/Context-Aware Risk Attribute Access Control.pdf`.

### 8.11 MV-6 closed: CAP cites as 2025, and there is no DOI  ·  *[Claude]*

*17 November 2026.* Checked against the PMLR volume front matter and the paper's own citation block.
Iskandar's point that the paper has no DOI is correct and is itself half the answer.

| Field | Value |
|---|---|
| Title | *CAP: Conformalized Abstention Policies for Context-Adaptive Risk Management for LLMs and VLMs* |
| Authors | Sina Tayebati, Divake Kumar, Nastaran Darabi, Dinithi Jayasuriya, Theja Tulabandhula, Ranganath Krishnan, Amit Ranjan Trivedi |
| Venue | Proceedings of the **17th Asian Conference on Machine Learning**, 9–12 December 2025, HNBK International Convention Center, Taipei, Taiwan |
| Editors | Hung-yi Lee, Tongliang Liu (series editor Neil D. Lawrence) |
| Citation | **PMLR 304:926–941, 2025** · volume published 13 November 2025 |
| Identifiers | Abstract `https://proceedings.mlr.press/v304/tayebati26a.html` · BibTeX key `pmlr-v304-tayebati26a` · **no DOI** |

**Year: 2025.** The paper's citation line, BibTeX (`year = {2025}`), APA and EndNote entries all give
2025, consistent with a December 2025 conference and a 13 November 2025 volume. Every 2026 value on the
page comes from web-publication metadata (`citation_publication_date: 2026/04/06`), the copyright
footer, or the site compile stamp — none of which is citation data.

**The `26a` in the key is not a year claim.** It is a PMLR filename convention assigned at
web-publication time. Worth recording here so that nobody later "corrects" the citation to 2026 on the
strength of the URL.

**No DOI exists**, for the paper or the volume — PMLR identifies papers by the abstract URL, the
volume:page range and the BibTeX key. A reference list should carry the PMLR form rather than leave a
DOI field blank as though one were missing.

**Still outstanding for CAP:** the PDF is not held in the corpus (the only conformal-related file is an
unrelated extraction note on clinical triage deferral), and **Matrix A has no row for it** even though
§1 treats it as a core comparator. Both are noted in Matrix H; neither is a citation defect.

### 8.12 MV-4 closed: the ATVA version is real, and the year is 2026  ·  *[Claude]*

*17 November 2026.* The `doi.org` resolver is blocked from here, but the Springer chapter page reads
fine at `link.springer.com/chapter/10.1007/978-3-032-08707-2_8`.

| Field | Value |
|---|---|
| Chapter | *Efficient Dynamic Shielding for Parametric Safety Specifications* |
| Authors | Davide Corsi, Kaushik Mallik, Andoni Rodríguez, César Sánchez |
| In | *Automated Technology for Verification and Analysis* — **ATVA 2025** |
| Editors | Meenakshi D'Souza, Raghavan Komondoor, B. Srivathsan |
| Series | Lecture Notes in Computer Science, **vol. 16145**, **pp. 157–179** |
| Publisher | Springer, Cham · print ISBN 978-3-032-08706-5 · online ISBN 978-3-032-08707-2 |
| DOI | 10.1007/978-3-032-08707-2_8 |
| Dates | **First online 26 October 2025**; book citation and copyright give **2026** |

**The substantive question is settled: a peer-reviewed proceedings version exists.** GPT's ATVA claim
was right, the IMDEA page was accurate on venue, volume and pages, and the row is **peer-reviewed prior
art, not a preprint**. With ProSh's AAMAS abstract (§8.7), both shielding rows now have published forms.

**But the year is 2026, not 2025.** Springer's own citation block reads *Corsi, D., Mallik, K.,
Rodríguez, A., Sánchez, C. (2026)*, the copyright line is © 2026, and the publication date field is
2026. "Springer 2025" — as the IMDEA page and §7 give it — is the **first-online** date, not the
citation year. Cite as:

> Corsi, D., Mallik, K., Rodríguez, A., Sánchez, C. (2026). Efficient Dynamic Shielding for Parametric
> Safety Specifications. In: D'Souza, M., Komondoor, R., Srivathsan, B. (eds) *Automated Technology for
> Verification and Analysis. ATVA 2025.* LNCS vol. 16145, pp. 157–179. Springer, Cham.
> https://doi.org/10.1007/978-3-032-08707-2_8

Matrix A's "(2025/2026)" hedge was therefore tracking something real: ATVA **2025** is the conference,
**2026** is the publication year.

**A caution against normalising this against MV-6.** The two look alike and resolve opposite ways. CAP's
conference ran in December 2025 and PMLR's citation says 2025, so CAP cites as **2025**. Corsi's
conference ran in October 2025 but Springer's citation says 2026, so Corsi cites as **2026**. In both
cases the rule is the same — follow the publisher's citation block, not the conference name or the
online date — and in both cases it is the URL or acronym that misleads.

**The queue is now empty.** All six items opened on 17 November are closed.
