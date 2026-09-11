# Utility Construct Assessment — Decision-Support Utility and Human Study Boundary

**Date:** 2026-09-11
**Branch:** `design/journal1-post-fidelity-evaluation-plan`
**Batch context:** Batch 6, Task 3 (post-Batch-5, F1=F2=F3=PASS)
**Questions:** (B) Is the utility construct required for Journal 1, and can it be operationalised? (C) Does any open Journal 1 claim require human participants?

---

## §1 What Is the Utility Construct? Evidence of Where It Appears

The decision-support utility construct is an OPEN metric in the Journal 1 evaluation framework. Its definition in `publications/active/journal-1/evaluation-specification.md` §9:

> "Decision-support utility — OPEN — CONSTRUCT DEFINITION REQUIRED. No operational definition on the replay alone has been established. Possible operational meanings (ground-truth recommendation correctness, fisher preference, decision quality, actionability, task completion, real-world outcome) each require a different data source and study design. Do not invent a utility formula. Deferred to a future user study (thesis RQ5 scope). Marking this OPEN does not block the rest of the specification."

In `data/journal1-evaluation-specification/evaluation-specification.csv`, it appears as row `H-DEFERRED-utility`:

| Field | Value |
|---|---|
| `id` | H-DEFERRED-utility |
| `question_or_claim` | Decision-support utility — construct definition required |
| `evidence_type` | HUMAN-EVALUATION |
| `conditions` | C0/C1/C2 (proposed comparators) |
| `metric` | undefined — no operational definition |
| `current_status` | OPEN — CONSTRUCT DEFINITION REQUIRED |
| `expected_source` | future user study (thesis RQ5 scope) |
| `analytical_or_empirical` | neither — construct is undefined |
| `requires_layer3` | NO (utility construct is not resolved by Layer 3) |
| `requires_humans` | YES (user study) |
| `reporting_boundary` | Human study; not resolvable on retrospective replay alone; excluded from Journal 1 evidence base |

In `evaluation-specification.md` §9 (metric table):

> "Decision-support utility — OPEN — CONSTRUCT DEFINITION REQUIRED"

In `evaluation-specification.md` §17, it is listed as OPEN-2:

> "Decision-support utility construct — No operational definition on replay alone — Only the utility metric; other metrics are unaffected."

In `evaluation-specification.md` §15 (human-validation boundary):

> "Decision-support utility (construct definition OPEN — see Section 9). […] Explicitly deferred to a future study (thesis RQ5 scope)."

The construct also appears in the following files in `publications/active/journal-1/`:
- `evaluation-baseline-decision.md` — deferred question 4 references utility; baseline decision §14 correction removed "If Layer 3 is built before submission, do H1/H2 become genuinely empirical?" and reframed
- `layer3-prototype-specification.md` — references utility as outside Layer 3 scope
- `algorithm-specification.md` — does not define or operationalise it
- `research-design.md` — lists it as deferred
- `submissions/v1-initial-submission/manuscript.md` — references it as construct-undefined

In all locations, the construct appears as an explicitly OPEN, construct-undefined, deferred item.

---

## §2 What Claim Requires It?

**No currently authorised, open Journal 1 claim requires the utility construct.**

The utility construct is carried in the evaluation framework as `H-DEFERRED-utility` — a deferred row, not an active evaluation item. Its `current_status` is "OPEN — CONSTRUCT DEFINITION REQUIRED" and its `reporting_boundary` is "excluded from Journal 1 evidence base."

The four authorised Journal 1 research questions and their evidence chains are:

| RQ | Evidence type | Status |
|---|---|---|
| RQ-J1 (Safety Dominance proof) | FORMAL | CLOSED (P1–P4, F1–F3) |
| RQ-J2 (governance latency) | PERFORMANCE | READY_DESCRIPTIVE (E5) |
| RQ-J3 (empirical divergence) | EMPIRICAL-TRACE | CLOSED (E1–E3) |
| RQ-J4 (Level 2 contribution) | EMPIRICAL-TRACE | CLOSED (E2, E4) |

None of the four RQs references a utility construct. No metric in the final metric set (`evaluation-specification.md` §9 metric table) is classified as requiring a utility score. M-Fidelity-F1 through M-Performance-E5 all have concrete, already-closed or already-specified operational definitions that do not involve utility.

`evaluation-specification.md` §15 explicitly classifies the utility construct as outside Journal 1: "Journal 1 makes no claim about human decision quality, trust, calibrated reliance, actionability, task completion or real-world safety outcomes."

---

## §3 Can It Be Operationalised from Existing Deterministic Traces?

**No.**

The retrospective replay produces:
- A sequence of safety states S = f(E) for each hourly record
- Admissible recommendation sets A_AI(S) for each state
- Pairwise divergence values between conditions C0/C1/C2 (E1, E2)
- Rule activation sequences (if Layer 3 is connected, per the Batch 4B-2 projection)

None of these outputs provides a basis for operationalising decision-support utility, because utility requires a reference against which the recommendation is judged. The possible operational meanings enumerated in `evaluation-specification.md` §9 are:

- **Ground-truth recommendation correctness:** requires knowing whether each departure decision in the historical record was actually safe — this is not recorded in the replay data (ERA5-Ocean and MFWAM provide hindcast environmental conditions, not outcomes)
- **Fisher preference:** requires asking fishers which recommendation they preferred or found useful — requires human participants
- **Decision quality:** requires a normative standard for what a correct departure decision is — requires domain expert judgement or a validated reference benchmark
- **Actionability:** requires knowing whether fishers could act on the recommendation — requires user study
- **Task completion:** requires a defined task and observation of completion — requires a study design with participants
- **Real-world outcome:** requires incident/safety records or catch data — field data that the study does not have

The environmental replay provides the advisory input side of the equation (what the architecture recommends) but not the outcome side (whether the recommendation produced a good decision, was trusted, was acted upon, or correlated with safety). Without the outcome side, no utility score can be computed from the trace.

**Could a proxy be constructed?** Constructing a proxy utility on the replay alone would require either (a) an assumption that a specific recommendation type (e.g., Delay) is always correct when S = CAUTION, or (b) an arbitrary weighting across recommendation types. Both are prohibited by `evaluation-specification.md` §16: "Do not close the utility metric by inventing a formula on replay data." A proxy is an invented formula.

---

## §4 Does It Require Arbitrary Weighting or Human Judgement?

**Yes, on both counts.**

Any operationalisation of decision-support utility on the retrospective replay would require at least one of:

1. **Arbitrary weighting:** Assigning relative utility values to recommendation types (e.g., Delay = 0.8, Go = 1.0, no recommendation = 0.0) without a source. No authority document provides or endorses any such weights. The evaluation-specification explicitly prohibits inventing them.

2. **Human judgement:** Determining whether a Go or Delay recommendation was the appropriate one in a given condition requires either (a) a domain expert to evaluate each condition against a reference standard, or (b) fisher feedback on the acceptability and actionability of recommendations. Both require participants.

3. **Unrecorded outcome data:** Utility requires knowing what happened after the recommendation — whether the fisher went to sea, whether conditions were as predicted, whether the decision was safe. The retrospective ERA5-Ocean/MFWAM replay records hindcast environmental conditions, not departure decisions or outcomes.

The `evaluation-specification.csv` row for H-DEFERRED-utility confirms: `requires_humans = YES`.

---

## §5 Journal 1 vs. Human Study Placement

The utility construct belongs to the human study (thesis RQ5 scope), not Journal 1. The authority for this placement is:

- `evaluation-specification.md` §9: "Deferred to a future user study (thesis RQ5 scope). Marking this OPEN does not block the rest of the specification."
- `evaluation-specification.md` §15: "Decision-support utility (construct definition OPEN — see Section 9). [...] Explicitly deferred to a future study (thesis RQ5 scope)."
- `evaluation-specification.md` §17 (OPEN-2): "Decision-support utility construct — No operational definition on replay alone — Only the utility metric; other metrics are unaffected."
- `evaluation-specification.csv` row H-DEFERRED-utility: `reporting_boundary` = "Human study; not resolvable on retrospective replay alone; excluded from Journal 1 evidence base."
- `docs/canonical/rq5-study-design.md` (CLAUDE.md canonical document index): RQ5 contextual validation study design covers the user study, including decision quality and trust under the graduated advisory scope.

Journal 1's evidence base is defined in `evaluation-specification.md` §15 as: "formal proofs, mapping-literal comparisons, retrospective replay statistics, and Layer 2 performance measurements." Decision-support utility requires none of these — it requires field data or a user study.

The CAUTION OPEN state of the utility metric does not block any Journal 1 claim or evaluation. OPEN-2 in `evaluation-specification.md` §17 explicitly scopes its impact: "Only the utility metric; other metrics are unaffected."

---

## §6 Conclusion

```
UTILITY_CONSTRUCT = DEFER_TO_HUMAN_STUDY
```

**Justification:** The decision-support utility construct has no operational definition that can be derived from the retrospective replay. All candidate operationalisations require either arbitrary weighting (prohibited by the evaluation-specification), human participants (outside Journal 1 scope), or outcome data that is not recorded in the replay. The construct is explicitly deferred to the future user study (thesis RQ5 scope) by the evaluation-specification authority chain. No currently authorised Journal 1 claim requires the utility construct; `H-DEFERRED-utility` is a deferred row in the evaluation-specification matrix, not an active evaluation target. Operationalising the utility construct for Journal 1 would require inventing a formula without an external source — this is prohibited by `evaluation-specification.md` §16.

---

## §7 Human Study Boundary

```
HUMAN_STUDY_REQUIRED_FOR_J1 = false
```

**Dependency trace across all open Journal 1 claims:**

| Claim | Status | Requires human participants? | Authority |
|---|---|---|---|
| P1 Totality | CLOSED | NO — formal proof | appendix-c C.1, C.1b |
| P2 Monotonicity | CLOSED | NO — formal proof | appendix-c C.2, C.6 |
| P3 Safety Dominance | CLOSED | NO — formal proof under A1–A4 | appendix-c C.3, C.7.2 |
| P4 (J1-P1) C1 ≡ C3 | CLOSED | NO — finite-mapping comparison | evaluation-specification.md §6 |
| F1 Advisory admissibility | CLOSED (PASS) | NO — deterministic fidelity test | Batch 5 report.md §13 |
| F2 Violation count | CLOSED (PASS) | NO — deterministic fidelity test | Batch 5 report.md §14 |
| F3 RS(S) switching | CLOSED (PASS) | NO — deterministic fidelity test | Batch 5 report.md §15 |
| E1 Pairwise divergence | CLOSED | NO — deterministic census | scripts/condition_comparison.py |
| E2 Δ_L2 | CLOSED | NO — deterministic census | scripts/condition_comparison.py |
| E3 Resolution sensitivity | CLOSED | NO — dual-configuration reporting | scripts/canonical_figures.py |
| E4 Hysteresis characterisation | CLOSED | NO — deterministic census | scripts/hysteresis_analysis.py |
| E5 Governance latency | READY_DESCRIPTIVE | NO — hardware benchmarking | evaluation-specification.md §11 |
| E6 C1↔C3 confirmation | CLOSED | NO — deterministic census | scripts/condition_comparison.py |
| H-DEFERRED-utility | OPEN (DEFERRED) | YES — but explicitly OUTSIDE Journal 1 | evaluation-specification.csv; evaluation-specification.md §15 |
| H-DEFERRED-trust | OPEN (DEFERRED) | YES — but explicitly OUTSIDE Journal 1 | evaluation-specification.csv; evaluation-specification.md §15 |

**Analysis:** Every claim that is active within Journal 1 (P1–P4, F1–F3, E1–E6) requires either formal proof, deterministic computation, implementation-fidelity testing, or hardware performance measurement. None requires human participants. The two deferred items (H-DEFERRED-utility, H-DEFERRED-trust) do require human participants, but both are explicitly classified as OUTSIDE Journal 1's evidence base in `evaluation-specification.md` §15 and in `evaluation-specification.csv` under `reporting_boundary`.

The boundary instruction from `evaluation-specification.md` §15 is unambiguous: "Journal 1 makes no claim about human decision quality, trust, calibrated reliance, actionability, task completion or real-world safety outcomes. These constructs require field data (a user study, incident records) that Journal 1 does not have."

Adding human participants to Journal 1 to strengthen the paper would constitute introducing participants where no authorised claim requires them — this is explicitly ruled out by the task brief constraint "Do not introduce participants merely to strengthen the paper."

---

*Author: iskandar · Date: 2026-09-11 · Batch 6 Task 3*
