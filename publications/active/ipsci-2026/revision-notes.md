# IPSCI-2026 Revision Notes

**Status:** **REJECTED** (v2.5). Revision in progress for resubmission or retargeting.
**Submitted artifact:** v2.5 **.docx** — authoritative record of what reviewers saw
**Active working file:** `submissions/v3-revision/manuscript-v3.md` *(forked 2026-09-06)*
**Frozen:** `submissions/v2-post-review/manuscript-v2.5-submitted.md` — do not edit

> **The v2.5 .md is not the submitted paper.** It carried post-submission corrections (TABLE II, [37]→[33]) and then, on 2026-08-20, six new sections added in response to supervisor feedback — Formal Properties, Algorithm Specification, Computational Complexity, Generalisation, Deployment Challenges, Threats to Validity — plus a rewritten Conclusion. **Reviewers saw none of that.** Review 3's objection that the paper lacks technical evidence for its safety claims was made against a version containing no formal proofs.

## Review outcome (v2.5)

| Review | Verdict | Substance |
|---|---|---|
| 1 | Accept, minor revision | Check the comparative table; add experimental validation or case studies |
| 2 | Accept, minor revision | **Disregard — reviews a different paper.** Twitter bot detection, TwiBot-22, F1 0.552, SHAP beeswarm, BotRGCN/BIC/ETS-MM baselines; names the AMICT Machine Intelligence/Cybersecurity track. No overlap with this submission. **Raise with chairs** — discounting it leaves 1 accept-minor and 1 reject, which is borderline rather than a clear rejection |
| 3 | **Reject** | "Lacks the technical and empirical evidence necessary to establish its novelty, effectiveness, and safety claims" |

**Converged signal from Reviews 1 and 3:** no empirical validation. The evaluation is designed (`docs/canonical/evaluation-design-rq4.md`) but has not been run. Review 1's comparative-table comment likely refers to TABLE II, which has six wrong reference numbers — listed below.

---

## Known Errors in Submitted Paper

These errors exist in the submitted .docx but are corrected in the .md. Fix in any revised submission.

> **Verified 2026-09-06 against `v3-revision/manuscript-v3.md`:** all six TABLE II reference numbers below are **already correct in the .md**. They are wrong only in the submitted .docx. The `[37]`→`[33]` fix is also already applied.
>
> **One error not previously recorded, now fixed in v3:** Domain Instantiation cited "Ghaleb et al. **[27]**" for runtime-gating stability. Reference [27] is Cash et al., *Quantifying uncert-AI-nty*; Ghaleb et al. is **[24]**. Corrected in v3. Worth checking whether the same error appears in the .docx.

| Location | Error | Correction |
|---|---|---|
| TABLE II, row Tumato 2.0 | `[16]` | `[14]` |
| TABLE II, row Pro2Guard | `[34]` | `[31]` |
| TABLE II, row Kang GAIE | `[25]` | `[22]` |
| TABLE II, row Ghaleb et al. | `[27]` | `[24]` |
| TABLE II, row Sahoo AMAGF | `[26]` | `[23]` |
| TABLE II, row Baxi K-tier | `[15]` | `[13]` |
| Domain Instantiation, body text | `[37]` (Gao) | `[33]` |
| Reference list | `[35]` is blank | Remove or fill |
| Acknowledgment section | Placeholder text "Will be add later!" | Add actual acknowledgment |

---

## Items to Address on Revision

### If reviewer flags citation issues
- Apply all TABLE II corrections above
- Fix `[37]` → `[33]` in Domain Instantiation
- Remove blank `[35]` from reference list

### If reviewer requests methodology clarification
- The StLR vs SLR distinction is already explained in the Methodology section
- Coding dimensions are derived from the RQ — can be made more explicit if needed
- The four-stream purposive scope justification can be expanded

### If reviewer requests stronger novelty framing
- The three-governance-dimensions argument (Fig. 1) is the cleanest entry point
- The conditioning variable column in TABLE II (all "internal to AI" vs "environmental safety state") is the sharpest discriminator
- CAUTION mode is the concrete deliverable that no reviewed architecture implements

### If reviewer questions the Symbolic AI / rule-based engine choice
- Full justification: `docs/canonical/justification-layer3-enforcement.md`
- Safety Dominance Property proof by construction: `docs/canonical/appendix-c-formalisation.md` Section C.7.2

### If reviewer requests evaluation results
- RQ4 evaluation design: `docs/canonical/evaluation-design-rq4.md`
- RQ5 user study design: `docs/canonical/rq5-study-design.md`
- Note: this paper covers architecture contribution only; evaluation is thesis scope

### If reviewer requests domain evidence / Malaysia fisheries detail
- Notes: `notes/Survival Decisions and Adaptation Strategies of Small-scale Fishers in the Face of Extreme Weather Impacts in Coastal Areas.md`
- Notes: `notes/Mapping the decision-making factors of small-scale fishers- a case study of Penang.md`
- Notes: `notes/Overview of the fishery and aquaculture sectors in Malaysia.md`

### General revision checklist
- [ ] Fix all TABLE II reference numbers (see table above)
- [ ] Fix `[37]` → `[33]` in Domain Instantiation
- [ ] Remove or fill blank `[35]`
- [ ] Add acknowledgment text
- [ ] Re-run humanizer on any new or rewritten passages
- [ ] Verify any new citations against `docs/canonical/citation-notes-map.md` and add `[[notes]]` links

---

## Version Log

| Version | File | Notes |
|---|---|---|
| v1–v7 | `submissions/archive/` | Archived drafts |
| v2.5 (submitted) | `submissions/v2-post-review/manuscript-v2.5-submitted.md` | Submitted .docx converted to .md; TABLE II and [37] corrected in .md |
| v3 (future) | — | Post-review revision, to be created when reviews arrive |
