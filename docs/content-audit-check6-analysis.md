# Content Audit — Check 6: Abstract / Contribution Alignment

**Scope:** Abstract of `ipsci-2026-paper-v5.md` vs §1, §4.6, §5, §6  
**Date:** 2026-07-20  
**Status:** Complete — 1 issue found and corrected, 2 notes

---

## Method

Each substantive claim and framing choice in the abstract is matched against the corresponding body text. The test is whether the abstract accurately and completely represents the paper's gap argument, evidence base, and contribution — without overclaiming, underclaiming, or using terminology that diverges from the body.

---

## Claim-by-claim comparison

| Abstract sentence | Body counterpart | Match? |
|---|---|---|
| "AI advisory behaviour should change as operational conditions deteriorate remains an open governance question" | §1: "a fundamental architectural question remains unresolved: how should AI advisory behaviour change as operational conditions deteriorate" | ✓ |
| "reviews the AI governance, runtime assurance, human-AI collaboration, and fisheries/low-resource literature" | §3.1: same four bodies named | ✓ |
| "existing governance mechanisms are uniformly binary: the AI either generates its full recommendation set or is blocked entirely" | §4.1, §4.6, §6: consistent claim | ✓ |
| Mechanistic evidence: "inference pipeline is structurally fixed, reasoning exploration is a property of the decoding procedure rather than a content-conditioned adaptation, and self-assessed confidence is unreliably calibrated and insensitive to past performance" | §4.7: three sub-claims map to fixed pipeline (§4.7.1), reasoning dynamics (§4.7.2), self-assessed uncertainty (§4.7.3) | ✓ |
| "Indykov et al. (206 papers, 16 architectural tactics), Shamsujjoha et al. (13 guardrail actions across 32 studies), and Perez-Cerrolaza et al. (294 references)" | §4.6 stream 1: same three papers, same figures | ✓ (see Note 1) |
| "Flehmig et al.'s three-level traffic-light degradation index (the closest advisory-governance precedent) changes human supervisory behaviour at its intermediate level but leaves AI advisory output unchanged" | §4.4, §4.6: consistent | ✓ |
| "Sahoo's five-level framework (the closest behavioural precedent) restricts autonomous action classes but governs an executing military agent rather than a human-facing recommendation menu" | §4.4, §4.6: consistent | ✓ |
| Gap statement: "the distinct dimension of what the AI is permitted to recommend to a human decision-maker (an admissible recommendation space that contracts as classified operational risk increases) remains unaddressed" | §4.6, §6: consistent | ✓ |
| "binary governance leaves intermediate-risk conditions structurally unaddressed: a fisher in marginal weather receives either full-scope tactical recommendations or none at all" | §4.5, §5.2: consistent | ✓ |
| "**A graduated governance architecture** addresses this gap through a participation gate G(S) and an advisory gate A_AI(S)…producing an intermediate CAUTION mode" | §1 (line 26), §4.8, §5, §6: "**graduated safety-state-gated** [governance] architecture" | **Issue 1** |

---

## Issue Detail

### Issue 1 — Architecture name drops "safety-state-gated" (abstract, final sentence)

**Abstract:**
> "A **graduated governance architecture** addresses this gap through a participation gate G(S) and an advisory gate A_AI(S), both conditioned on the current environmental safety state S, producing an intermediate CAUTION mode in which the AI advises within a formally restricted scope."

**Paper title:**
> "…A PROPOSED ARCHITECTURE" (generic in title; the specific name appears in body)

**Body (all occurrences):**
- §1 (line 26): "a **graduated safety-state-gated governance architecture**"
- §4.8 (line 230): "a **graduated safety-state-gated governance architecture**"
- §5 intro (line 238): "a **graduated safety-state-gated architecture**"
- Figure 3 caption (line 240): "The **graduated safety-state-gated architecture**"
- §6 (line 316): "The **graduated safety-state-gated architecture**"

The abstract uses "graduated governance architecture" — a generic label that could describe any graduated governance approach. "Safety-state-gated" is the paper's distinguishing label: it specifies that the gate is conditioned on a classified safety state S, which is the novel mechanism. Dropping it in the abstract removes the paper's most precise self-identification at the point of first contact for readers.

**Proposed fix:** Add "safety-state-gated" to the final abstract sentence:

> "A **graduated safety-state-gated governance architecture** addresses this gap through a participation gate G(S) and an advisory gate A_AI(S), both conditioned on the current environmental safety state S, producing an intermediate CAUTION mode in which the AI advises within a formally restricted scope."

---

## Notes (no correction required)

### Note 1 — Shamsujjoha: "13 guardrail actions" vs "13 guardrail actions and 14 quality attributes"

The abstract describes Shamsujjoha as "(13 guardrail actions across 32 studies)." Following the Check 4 fix, §4.6 and the conclusion now both read "13 guardrail actions and 14 quality attributes." The abstract remains at the shorter form. This is acceptable abstract compression — the 14 quality attributes figure is supporting detail, not a gap-confirming statistic. No correction required, but the abstract is now one step behind the body on this description.

### Note 2 — "Four independent bodies of literature" not signalled in abstract

§1 and §6 both say "a gap confirmed from four independent bodies of literature." The abstract names the evidence without counting the streams. The fisheries/low-resource stream (stream 4) is not mentioned as a gap-confirming body — it appears only as a domain example ("small-scale coastal fisheries"). This is defensible compression: the fisheries stream confirms the gap by omission rather than measurement, making it the least sharp of the four. No correction required.

---

## Summary

| Result | Count |
|---|---|
| Accurate and consistent | 9 claims |
| Issue requiring correction | 1 |
| Notes (no correction) | 2 |

The abstract accurately represents the paper's evidence base, gap argument, mechanistic rationale, and contribution. The single correction is to restore "safety-state-gated" to the architecture name in the final sentence.

---

## Recommended Action

| Priority | Action | Location |
|---|---|---|
| High | Add "safety-state-gated" to architecture name in final abstract sentence | Abstract (line 10, final sentence) |
