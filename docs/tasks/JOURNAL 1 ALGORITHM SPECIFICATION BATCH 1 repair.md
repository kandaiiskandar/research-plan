JOURNAL 1 ALGORITHM SPECIFICATION BATCH 1 —
TRANSITION CONSISTENCY REPAIR

Do not reopen Batch 1 science.
Do not change canonical files, classifier semantics, governance mappings,
thresholds, RS(S) semantics, or human authority.

Repair one bounded implementation over-specification in:

publications/active/journal-1/algorithm-specification.md
§8 RS(S) pre-reasoning contract

Current wording:

"When S changes across ticks, the active rule set must be swapped atomically.
No stale rule set may persist across a transition."

The scientific requirement is state/rule-set consistency for each reasoning
episode. Atomic swap is only one possible implementation mechanism and is not
yet established as canonical architecture.

Replace with bounded wording equivalent to:

"When S changes across decision episodes, the rule set used for the next
reasoning episode must be RS(S_new). A reasoning episode must not execute with
a rule set inconsistent with the state governing that same episode. The
implementation mechanism that enforces this consistency (for example atomic
swap, immutable snapshot, locking, transactional update, or serialized
execution) is not yet specified."

Preserve:

F3 tests that no stale/inconsistent rule set is used across a state transition.

Add a bounded OPEN item:

OPEN-B1-8 — State/rule-set consistency enforcement mechanism

Status:
OPEN — IMPLEMENTATION DECISION

Reason:
The architecture requires state/rule-set consistency but does not prescribe
the concurrency/atomicity mechanism used to achieve it.

Does not block:
Algorithm specification, provided Algorithms 3–4 express the consistency
requirement as a precondition/postcondition rather than prescribing an
implementation primitive.

Also:

1. Update open-decisions.csv.
2. Update semantic-verification-batch1.json with a check such as:
   transition_consistency_requirement_bounded
3. Update closure-batch1.json.
4. Re-run CSV parser verification.
5. Re-run protected-file integrity verification.
6. Do not modify canonical authorities.

Closure only if the implementation mechanism remains OPEN while the
state/rule-set consistency requirement remains mandatory.

Report:

JOURNAL 1 ALGORITHM SPECIFICATION BATCH 1 CLOSED —
TRANSITION CONSISTENCY CONTRACT REPAIRED