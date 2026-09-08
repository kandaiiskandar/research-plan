# Content Audit — Check 5: Terminology Consistency

**Scope:** `ipsci-2026-paper-v5.md` body — §1 through §6  
**Date:** 2026-07-20  
**Status:** Complete — no issues found

---

## Terms checked

| Term | Canonical form | Locations | Variants found | Verdict |
|---|---|---|---|---|
| Architecture name | "graduated safety-state-gated [governance] architecture" | §1 (line 26), §4.8 (line 230), §5 intro (line 238), Figure 3 caption (line 240), §6 (line 316) | "graduated safety-state-gated governance architecture" (§1, §4.8); "graduated safety-state-gated architecture" (§5, §6) — "governance" dropped in §5–6 but not contradictory | ✓ Consistent |
| Safety Dominance Property | "Safety Dominance Property": AI(E) ⊆ A_AI(S) | §5.1 (line 294), §5.3 (line 308) | Named consistently; formal definition AI(E) ⊆ A_AI(S) in both. Figure 3 diagram also shows "AI(E) ⊆ A_AI(S)" | ✓ Consistent |
| CAUTION terminology | "CAUTION mode" (operational); "CAUTION state" (formal S value); "CAUTION configuration" (rule set) | §5.2 heading, lines 298, 302, 304, 316, 294 | "CAUTION mode" for the operational concept (§5.2 heading, body, §6); "CAUTION state" at line 304 when referring to S = CAUTION specifically; "CAUTION configuration" at line 294 when referring to RS(CAUTION). Each form used in the contextually appropriate sense | ✓ Consistent |
| Governance pair | "(G(S), A_AI(S))" | §5.1 (line 286), §6 (line 316) | "participation gate G(S) and advisory gate A_AI(S)" (abstract, Figure 3 caption — referring to individual elements); "governance pair (G(S), A_AI(S))" (§5.1, §6 — referring to the pair); "two-level governance pair" (§6) | ✓ Consistent |
| Admissible recommendation space | "admissible recommendation space A_AI(S)" | §4.6 (line 198), §4.7 (line 218, 220), §6 (line 314) | "admissible space A_AI(S)" (shorthand, §5.1 line 294); "admissible sets" (§4.4, in description of Sahoo); "recommendation menu" (§4.3, §4.4 — informal, used only in contrast with autonomous-agent execution) | ✓ Consistent |
| Environmental safety state | "environmental safety state S" | Throughout | "safety state S", "classified environmental safety state", "environmental safety state" — all consistent in meaning; variation is stylistic only | ✓ Consistent |
| Participation gating | "participation gating" / "participation gate G(S)" | §2, abstract, §5.1, §6 | Stable across all occurrences | ✓ Consistent |
| Advisory scope | "advisory scope" | Title, §2, §4 passim, §6 | Used as the concept name throughout; "advisory gate A_AI(S)" for the gate that enforces it — distinction is clear and consistent | ✓ Consistent |
| Binary governance | "binary" (by construction / by design) | §4.2 ("binary by construction"), §6 ("binary by design"), §5.2 ("binary gate", "binary governance") | Minor wording variation ("by construction" vs "by design") reflects context (§4.2 is explaining why; §6 is stating the finding); not a contradiction | ✓ Consistent |
| Rule-based engine | "rule-based engine" / "rule-based reasoning engine" | §5.1 (line 294 vicinity), §5.3 (line 308) | "rule-based reasoning engine" in §5.3, consistent with §5.1 description | ✓ Consistent |

---

## Notes

**"Governance" in architecture name.** "Graduated safety-state-gated **governance** architecture" (§1, §4.8) vs "graduated safety-state-gated architecture" (§5, §6). The "governance" qualifier appears when the architecture is being named as a category and drops when the specific proposed architecture is the subject. This is stylistically consistent with how architecture papers introduce then refer back to a named contribution — not a terminology error.

**"Recommendation menu."** Used only in comparative sentences distinguishing the proposed architecture's target (human-facing recommendation set) from autonomous-agent action spaces ("throttle the execution capabilities of acting autonomous agents rather than the recommendation menu of a decision-support tool" — §4.4; §4.3). It is never used to denote A_AI(S) directly. Appropriate scope of use.

**"CAUTION state" vs "CAUTION mode."** The single occurrence of "CAUTION state" (line 304) is in the sentence: "the CAUTION state is the early, threshold-calibrated intervention, contracting advisory scope while conditions are still marginal." Here "CAUTION state" correctly refers to S = CAUTION (the formal state value). The CAUTION mode is the operational behaviour the system enters when S = CAUTION; these are related but distinct. The usage is correct and unambiguous in context.

---

## Summary

| Result | Count |
|---|---|
| Consistent | 10 terms |
| Issues requiring correction | 0 |

**Check 5 complete — no corrections required.** The paper uses its key technical terms consistently throughout the body. The abstract is excluded (reserved for Check 6).
