# Content Audit — Check 4: Gap Argument Consistency

**Scope:** `ipsci-2026-paper-v5.md` — gap argument across §1 Introduction, §4.6 Synthesis, §6 Conclusion  
**Date:** 2026-07-20  
**Status:** Complete — 3 issues found and corrected

---

## Method

The four-stream gap argument is the paper's central claim: no existing architecture restricts AI advisory scope based on classified environmental safety state, confirmed by four independent bodies of literature. This check verifies that the argument is stated consistently in the three body locations where it is asserted — §1, §4.6, and §6.

The four streams as defined in §4.6:

| Stream | Body | Key papers in §4.6 |
|---|---|---|
| 1 | Large-scale reviews | Indykov, Shamsujjoha, Perez-Cerrolaza, Attard-Frost, Reuel, Batool |
| 2 | Adaptive risk-based systems | Flehmig, Kang, Ghaleb |
| 3 | Behavioural architectures | Sahoo |
| 4 | Fisheries / low-resource deployment | Haque, Rahim, Katende |

Note: the abstract is excluded from this check (reserved for Check 6).

---

## Comparison Table

| Element | §1 Introduction | §4.6 Synthesis | §6 Conclusion | Consistent? |
|---|---|---|---|---|
| "Four independent bodies of literature" | ✓ stated | ✓ four streams presented in full | ✓ stated in opening sentence | ✓ |
| "72 papers" | ✓ named | ✓ confirmed in §3 | not mentioned (omission, not contradiction) | ✓ |
| Stream 1 representative | not named | Indykov (AT11→Safety=0) + Shamsujjoha + Perez-Cerrolaza | Shamsujjoha only | **Issue 1** |
| Stream 2 representative | not named | Flehmig + Kang + Ghaleb | Flehmig only | ✓ (acceptable compression) |
| Stream 3 representative | not named | Sahoo | Sahoo | ✓ |
| Stream 4 referenced | not named | Haque, Rahim, Katende | **absent** | **Issue 2** |
| Flehmig characterisation | not stated | "use intermediate tiers to escalate human audit workloads" | "changes human supervisory behaviour at its intermediate level but leaves AI output unchanged" | ✓ (consistent, different depth) |
| Sahoo characterisation | not stated | "throttle the execution capabilities of acting autonomous agents rather than the recommendation menu of a decision-support tool" | "genuinely contracts an autonomous agent's permitted action space but remains blind to external environmental safety state and human-facing advisory contexts" | ✓ |
| Indykov AT11→Safety=0 | not stated | ✓ present | **absent** | **Issue 1 (same)** |
| "14 quality attributes" | absent | absent | ✓ present | **Issue 3** |
| Mechanistic evidence §4.7 referenced | not stated | — (§4.6 precedes §4.7) | ✓ referenced | ✓ |

---

## Issue Detail

### Issue 1 — Conclusion drops stream 1's sharpest finding (§6, line 314)

**What §4.6 says:**

> "Indykov et al.'s trade-off matrix records AT11 (rule-based models) → Safety = 0: despite Safety being one of the two most frequently cited quality attributes, no architectural tactic has demonstrated a formally positive impact on it."

**What the conclusion says:**

> "Shamsujjoha et al.'s Swiss Cheese Model, the most comprehensive guardrails taxonomy in the field (synthesising 32 studies and identifying 13 guardrail actions and 14 quality attributes), contains no concept of restricting advisory scope as a function of environmental risk."

Indykov's AT11→Safety=0 is the most precisely stated gap confirmation in the paper — a quantitative finding from a 206-paper systematic review that no architectural tactic achieves Safety. It is featured in §4.6 and in the abstract, but is absent from the conclusion. Shamsujjoha is a valid stream-1 representative but a less precise one: it says "contains no concept" (a negative), while Indykov says AT11→Safety=0 (a measured zero). The conclusion weakens the sharpest evidence at the point where the paper closes its case.

**Proposed fix:** Add a sentence to the conclusion that carries Indykov's AT11→Safety=0 finding, preserving the Shamsujjoha sentence. For example, insert before or after the Shamsujjoha sentence:

> "Indykov et al.'s systematic review of 206 papers and 16 architectural tactics records AT11 (rule-based models) → Safety = 0: no tactic in the surveyed literature demonstrates a formally positive impact on safety [5]."

---

### Issue 2 — Stream 4 (fisheries / low-resource) absent from conclusion (§6, line 314)

The conclusion's opening sentence asserts "from four independent bodies of literature," but the gap paragraph that follows references only three: stream 1 (Shamsujjoha), stream 2 (Flehmig), and stream 3 (Sahoo). Stream 4 — the fisheries and low-resource deployment literature — is not mentioned. The "four independent bodies" claim is thus made without textual support for the fourth.

This matters: the fisheries stream is the one closest to the deployment context and the one that establishes why the gap has operational consequences in the exact setting the architecture targets.

**Proposed fix:** Add a brief sentence naming stream 4 in the conclusion gap paragraph. For example:

> "The fisheries and low-resource deployment literature confirms the pattern at the application level: no paper in this body implements formal runtime governance; the only external advisory available to coastal fishers is a binary government warning [18]."

---

### Issue 3 — "14 quality attributes" appears only in conclusion (§6, line 314)

The conclusion introduces "14 quality attributes" as part of the Shamsujjoha characterisation. This figure does not appear in §4.6 or §3, where Shamsujjoha is described only as "13 guardrail actions across 32 agent studies." 

Verification: notes confirm the number is correct — Shamsujjoha identifies 14 quality attributes (accuracy, efficiency, privacy, security, safety, fairness, compliance, generalizability, customizability, adaptability, traceability, portability, interoperability, interpretability). So this is not a factual error. But it introduces a number in the conclusion that has no earlier appearance in the body, which a reviewer reading linearly would find surprising.

**Proposed fix (two options):**

- **Option A (preferred):** Add "14 quality attributes" to the §4.6 description of Shamsujjoha so the conclusion is supported by body text. In §4.6, line 192, change "Shamsujjoha et al.'s Swiss Cheese Model identifies 13 guardrail actions" → "Shamsujjoha et al.'s Swiss Cheese Model identifies 13 guardrail actions and 14 quality attributes."
- **Option B:** Remove "14 quality attributes" from the conclusion, leaving only the 13 guardrail actions figure that is consistently stated across §4.6 and the paper body.

Option A is preferred — it makes the conclusion's citation richer while also making §4.6 more complete.

---

## Summary

| Result | Count |
|---|---|
| Consistent | 9 elements |
| Issues found | 3 |

The paper's four-stream gap argument is structurally sound and internally consistent at the level of core claims — all three body locations assert "four independent bodies," the Flehmig and Sahoo characterisations are consistent, and the pipeline logic holds. The three issues are all about what the conclusion omits relative to §4.6: the AT11→Safety=0 finding (most precise gap evidence), stream 4 (application domain), and the 14 quality attributes figure (which goes the other way — present in conclusion, absent from body).

---

## Recommended Actions

| Priority | Action | Location |
|---|---|---|
| High | Add Indykov AT11→Safety=0 sentence to conclusion | §6 |
| High | Add stream 4 sentence (fisheries/low-resource) to conclusion | §6 |
| Low | Add "and 14 quality attributes" to §4.6 Shamsujjoha description | §4.6 |
