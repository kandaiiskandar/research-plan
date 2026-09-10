# Task — Journal 1 Algorithm Specification

## Batch 3: Algorithms 3 & 4 — Rule-Set Supply and Governed Advisory Generation

### Goal

Formalise exactly two publication-quality algorithms:

```text
Algorithm 3 — Rule-Set Supply
Algorithm 4 — Governed Advisory Generation
```

These algorithms must complete the formal governance pipeline:

```text
S
→ (G(S), A_AI(S))
→ RS(S)
→ Layer 3 reasoning
→ AI(E)
```

subject to:

```text
AI(E) ⊆ A_AI(S)
```

The purpose of this batch is to specify **how the architecture enforces advisory-scope governance by construction**.

This is an **algorithm-specification task**, not a prototype implementation task.

Do not implement a production rule engine.
Do not invent concrete Layer 3 rules.
Do not run F1–F3.
Do not run E5.
Do not benchmark latency.
Do not perform the final complexity analysis.
Do not modify canonical scientific state.

---

# 1. Branch

Continue on:

```text
design/journal1-algorithm-specification
```

Do not create another branch.

Batch 2 is CLOSED with:

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 2 CLOSED —
EXCLUSION-SET DOMAIN CONTRACT REPAIRED
```

Do not reopen Algorithms 1–2 unless a direct contradiction with an authoritative source is discovered.

---

# 2. Immediate maintained authority

Primary maintained authority:

```text
publications/active/journal-1/algorithm-specification.md
```

In particular inspect:

```text
§7  Governance mappings
§8  RS(S) pre-reasoning contract
§9  Human-decision boundary
§10 Open implementation decisions
§11–§16 Algorithms 1–2 and Batch 2 traceability
```

Canonical authorities to verify against:

```text
docs/canonical/appendix-c-formalisation.md
docs/canonical/architecture-illustration.md
docs/canonical/justification-layer3-enforcement.md
publications/active/journal-1/evaluation-specification.md
publications/active/journal-1/research-design.md
```

The maintained specification already establishes that Layer 3 is a production rule system and that the rule set is supplied **before reasoning begins**.

---

# 3. Protected scientific state

Before editing, verify the same 16 protected canonical files used by Batches 1–2.

Do not modify canonical formalisation, canonical scripts, raw/replay datasets, prediction register, solar artefact or submitted conference manuscripts.

If unexpected protected-state drift exists before starting, STOP:

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 3 OPEN —
PROTECTED STATE MISMATCH
```

---

# 4. Fixed recommendation space

Preserve exactly:

```text
R = {Go, Delay, DepartureTime, Duration}
```

and:

```text
A_AI(SAFE)
= {Go, Delay, DepartureTime, Duration}

A_AI(CAUTION)
= {Go, Delay}

A_AI(UNSAFE)
= ∅
```

Do not introduce:

```text
GoWithCaution
Cancel
Abort
Proceed
ReturnToShore
ChangeArea
FishingArea
Species
```

or any other recommendation type/subtype.

A caution qualifier attached to `Go` does not create a new recommendation type.

---

# 5. Participation gate

Preserve:

```text
G(SAFE)    = 1
G(CAUTION) = 1
G(UNSAFE)  = 0
```

Therefore:

```text
G(S)=0
⇒
A_AI(S)=∅
⇒
no Layer 3 advisory reasoning
```

Do not interpret this as a prohibition on human action.

---

# 6. Algorithm 3 — Rule-Set Supply

Create publication-quality pseudocode for:

```text
Algorithm 3 — Rule-Set Supply
```

Its responsibility is to supply the rule set that Layer 3 is permitted to use for the **current decision episode**.

Conceptual input:

```text
S
G(S)
A_AI(S)
configured rule repository
```

Conceptual output:

```text
RS(S)
```

Do not generate recommendations in Algorithm 3.

---

# 7. Required Algorithm 3 mapping

Preserve the maintained contract:

```text
RS(SAFE)
→ rules whose conclusion types are contained in
  {Go, Delay, DepartureTime, Duration}

RS(CAUTION)
→ rules whose conclusion types are contained in
  {Go, Delay}

RS(UNSAFE)
= ∅
```

Formally preserve:

```text
ConclusionTypes(RS(S)) ⊆ A_AI(S)
```

and:

```text
RS(UNSAFE) = ∅
```

The specification constrains **rule conclusion types**.

Do not fabricate concrete rule antecedents, thresholds, scoring functions, priorities or recommendation content.

---

# 8. Pre-reasoning enforcement

Algorithm 3 must make explicit that:

```text
RS(S)
```

is established **before any Layer 3 rule firing begins**.

The required dependency is:

```text
S
→ A_AI(S)
→ RS(S)
→ reasoning
```

not:

```text
reasoning
→ generated recommendation
→ filter against A_AI(S)
```

A post-hoc recommendation filter must NOT become the primary enforcement mechanism.

Safety Dominance is intended to hold because disallowed recommendation types are absent from the supplied rule set.

---

# 9. State/rule-set consistency

Preserve the repaired Batch 1 contract:

```text
For a decision episode governed by S,
the reasoning engine must use RS(S).
```

When the state changes:

```text
S_old → S_new
```

the next reasoning episode must use:

```text
RS(S_new)
```

and must not reason using stale:

```text
RS(S_old)
```

if that rule set is inconsistent with the governing state of the new episode.

However:

**DO NOT prescribe how this consistency is implemented.**

Do not require:

```text
atomic swap
mutex
lock
transaction
immutable snapshot
single-thread execution
event loop
```

unless an authoritative implementation source already requires it.

Preserve:

```text
OPEN-B1-8 —
State/rule-set consistency enforcement mechanism
```

The algorithm specifies the invariant, not the concurrency primitive.

---

# 10. Algorithm 3 failure/configuration semantics

The configured rule repository must satisfy:

```text
ConclusionTypes(RS(S)) ⊆ A_AI(S)
```

before the rule set is eligible for supply.

If the repository violates this condition, do **not** silently filter disallowed rules and continue.

Treat this as a **configuration/fidelity failure** unless canonical authority explicitly defines another response.

Do not invent a new safety state.

Do not map this failure to environmental `UNSAFE`.

Do not modify `S`.

If the authoritative sources do not specify exact runtime handling of an invalid rule repository, record:

```text
OPEN — INVALID RULE-REPOSITORY HANDLING
```

while preserving the mandatory precondition that an inconsistent `RS(S)` must not be supplied.

---

# 11. Algorithm 3 contract

Document explicitly:

### Inputs

```text
S
G(S)
A_AI(S)
configured rule repository
```

### Output

```text
RS(S)
```

or a bounded configuration/fidelity failure if the repository cannot satisfy the governance contract.

### Preconditions

At minimum:

```text
S is a valid Algorithm 1 output

(G(S), A_AI(S))
is the corresponding Algorithm 2 output

rule repository is configured

reasoning has not yet begun for this episode
```

### Postconditions

At minimum:

```text
ConclusionTypes(RS(S)) ⊆ A_AI(S)
```

and:

```text
G(S)=0 ⇒ RS(S)=∅
```

and:

```text
RS(UNSAFE)=∅
```

No recommendation has yet been generated.

---

# 12. Algorithm 4 — Governed Advisory Generation

Create publication-quality pseudocode for:

```text
Algorithm 4 — Governed Advisory Generation
```

Algorithm 4 consumes the governance configuration already established by Algorithms 1–3 and invokes Layer 3 only when participation is permitted.

Conceptual input:

```text
resolved decision context E
S
G(S)
A_AI(S)
RS(S)
rule engine
```

Use the exact maintained notation if canonical authority uses something more precise than `E`.

Do not silently redefine `E`.

---

# 13. Algorithm 4 UNSAFE path

The first governance branch must preserve:

```text
if G(S)=0:
    return ∅
```

Under the current mapping this corresponds to:

```text
S=UNSAFE
→ G=0
→ A_AI=∅
→ RS=∅
→ AI(E)=∅
```

No Layer 3 rule firing should occur on this path.

Do not generate a recommendation such as:

```text
Do Not Go
Cancel Trip
Return Home
```

Those would themselves be AI advisory outputs and are not members of the current recommendation space.

State-reporting UI behaviour belongs outside `AI(E)` unless canonical authority explicitly says otherwise.

---

# 14. Algorithm 4 participating path

When:

```text
G(S)=1
```

Algorithm 4 may invoke the production rule engine using only:

```text
RS(S)
```

for the current decision episode.

Conceptually:

```text
AI(E) ← Reason(E, RS(S))
```

The rule engine must not have access to an additional rule set capable of producing recommendation types outside `A_AI(S)`.

Preserve the canonical assumption:

```text
the engine fires only rules present in active RS(S)
```

and:

```text
no active rule produces a conclusion type
outside the conclusion types permitted by RS(S)
```

Do not invent a concrete inference strategy.

---

# 15. Safety Dominance dependency chain

Make the dependency explicit:

```text
A_AI(S)
      ↓
ConclusionTypes(RS(S)) ⊆ A_AI(S)
      ↓
engine fires only rules in RS(S)
      ↓
AI(E) ⊆ A_AI(S)
```

Categorise each arrow correctly.

Do not claim Algorithm 4 independently proves Safety Dominance.

The formal theorem already exists.

Algorithms 3–4 specify the executable contract required to preserve its assumptions.

Distinguish:

```text
formal theorem
algorithmic enforcement contract
implementation assumption
future implementation-fidelity evidence
```

---

# 16. No post-hoc filtering substitution

The following architecture is NOT acceptable as the primary contract:

```text
all_rules
→ reason freely
→ generate recommendation
→ filter recommendation against A_AI(S)
```

Do not specify Algorithm 4 this way.

The required architecture is:

```text
A_AI(S)
→ choose compliant RS(S)
→ supply RS(S)
→ reason only within RS(S)
→ AI(E)
```

A defensive assertion/check may potentially exist in a future implementation, but it must not replace rule-set restriction as the governance mechanism.

Do not introduce such a defensive mechanism in this batch unless already authoritative.

---

# 17. Human authority

Algorithms 3–4 must preserve:

```text
Human Decision
```

outside the AI advisory restriction.

Therefore:

```text
AI(E)=∅
```

does NOT mean:

```text
human action forbidden
```

and:

```text
AI(E) contains Go
```

does NOT mean:

```text
departure approved automatically
```

Do not introduce automated approval, prohibition, override or enforcement semantics.

The maintained specification explicitly states that human authority is unconditional across all three states.

---

# 18. Concrete Layer 3 rules remain OPEN

Do not construct rules such as:

```text
IF wave < X AND rain < Y THEN Go
```

or any equivalent concrete production-rule logic.

That belongs to:

```text
OPEN-B1-4 — Layer 3 prototype build
```

Algorithm 3 may define the **shape and admissibility contract** of `RS(S)`.

It may not invent its scientific contents.

---

# 19. Rule-engine strategy remains unspecified

Do not assume:

```text
forward chaining
backward chaining
RETE
agenda priority
first-match
all-match
conflict resolution
rule salience
```

unless authoritative documentation already fixes one.

If the strategy is not specified, record:

```text
OPEN — RULE ENGINE EVALUATION STRATEGY
```

This does not necessarily block Algorithm 3 or Algorithm 4 because their governance contracts can remain engine-agnostic.

This OPEN will matter later for complexity analysis.

---

# 20. Decision-episode semantics

Inspect authoritative sources for the meaning of a decision/reasoning episode.

Specify only what is necessary to establish:

```text
one governing S
one corresponding governance configuration
one corresponding RS(S)
```

for a reasoning episode.

Do not invent:

```text
episode duration
polling interval
refresh frequency
thread model
concurrency model
transaction boundary
```

If the exact episode boundary is not authoritative, record it as bounded OPEN rather than defining one.

---

# 21. Required transition specification checks

Add specification checks for at least:

```text
SAFE → CAUTION
CAUTION → SAFE
CAUTION → UNSAFE
UNSAFE → CAUTION
SAFE → UNSAFE
UNSAFE → SAFE
```

For each transition, verify the **next decision episode** uses the governance configuration and `RS(S_new)` corresponding to the new state.

Examples:

```text
SAFE → CAUTION

old:
A_AI = {Go, Delay, DepartureTime, Duration}

new:
A_AI = {Go, Delay}

next episode:
RS(CAUTION)

DepartureTime and Duration conclusion types
must not remain available.
```

and:

```text
CAUTION → UNSAFE

new:
G = 0
A_AI = ∅
RS = ∅
AI(E) = ∅
```

These are specification checks, not runtime fidelity results.

Do not claim F3 PASS.

---

# 22. Required state checks

Verify Algorithm 3 for all three states:

```text
SAFE
CAUTION
UNSAFE
```

Verify Algorithm 4 for:

```text
SAFE with compliant RS(SAFE)
CAUTION with compliant RS(CAUTION)
UNSAFE
```

Also specify checks for an invalid rule repository whose conclusion types exceed `A_AI(S)`.

Expected:

```text
must not be supplied for reasoning
```

but exact runtime failure handling remains OPEN if not authoritative.

---

# 23. Correctness traceability

Create traceability for Algorithms 3–4.

At minimum include:

```text
G(S)
A_AI(S)
RS(S)
ConclusionTypes(RS(S))
pre-reasoning supply
state/rule-set consistency
engine fidelity assumption
AI(E) ⊆ A_AI(S)
UNSAFE empty advisory
human authority
```

For each identify whether it is:

```text
Definition
Algorithm implementation of definition
Formal theorem/property
Implementation assumption
Future fidelity test
OPEN implementation decision
```

Do not collapse these categories.

---

# 24. Relationship to F1–F3

Inspect the current `evaluation-specification.md` and map Algorithms 3–4 to future fidelity criteria.

Do NOT report any criterion as empirically PASS.

At minimum preserve the distinction that:

```text
Batch 3 defines what implementation fidelity must satisfy.
```

It does not supply implementation evidence.

In particular, transition consistency may define the future F3 test contract, but does not constitute an F3 result.

---

# 25. Update maintained authority

Update:

```text
publications/active/journal-1/algorithm-specification.md
```

Add only the sections necessary for Algorithms 3–4.

Suggested structure:

```text
17. Algorithm 3 — Rule-Set Supply
18. Algorithm 3 — Preconditions and Postconditions
19. Algorithm 4 — Governed Advisory Generation
20. Algorithm 4 — Preconditions and Postconditions
21. Batch 3 State and Transition Verification
22. Safety-Dominance Dependency Trace
23. Batch 3 Correctness Traceability
24. Batch 3 Open Implementation Decisions
```

Do not add final complexity analysis yet.

Do not rewrite Algorithms 1–2 except for a genuine contradiction that triggers a stop condition.

---

# 26. Evidence artefacts

In:

```text
data/journal1-algorithm-specification/
```

add:

```text
algorithm-contracts-batch3.csv
state-cases-batch3.csv
transition-cases-batch3.csv
safety-dominance-trace-batch3.csv
algorithm-traceability-batch3.csv
open-decisions-batch3.csv
semantic-verification-batch3.json
parser-test-batch3.json
change-map-batch3.csv
closure-batch3.json
report-batch3.md
```

Do not replace Batch 1 or Batch 2 evidence.

CSV files must parse cleanly using the established strict parser workflow.

---

# 27. Required semantic checks

At minimum:

```text
algorithm3_consumes_algorithm2_governance
algorithm3_supplies_RS_before_reasoning
RS_safe_conclusion_types_bounded
RS_caution_conclusion_types_bounded
RS_unsafe_empty
conclusion_types_subset_AAI
invalid_RS_not_silently_filtered
invalid_RS_handling_bounded_if_unspecified
transition_consistency_requirement_preserved
atomicity_mechanism_not_invented
algorithm3_generates_no_advisory

algorithm4_respects_participation_gate
unsafe_path_skips_reasoning
unsafe_output_empty
participating_path_uses_only_RS_S
engine_fidelity_assumption_explicit
no_posthoc_filter_substitution
AI_subset_AAI_dependency_preserved
safety_dominance_not_reclaimed_as_new_proof
human_authority_preserved

concrete_rules_not_invented
rule_engine_strategy_not_invented
F1_F3_not_reported_as_results
E5_not_run
complexity_not_finalised
protected_state_unchanged
```

Each must be:

```text
PASS
FAIL
OPEN
```

with evidence.

---

# 28. Existing OPEN items

Do not silently close:

```text
OPEN-B1-1 — freshness parameters
OPEN-B1-2 — runtime provenance capture
OPEN-B1-3 — medium-vessel evidence limitation
OPEN-B1-4 — Layer 3 prototype
OPEN-B1-5 — live g_m configuration
OPEN-B1-6 — latency threshold
OPEN-B1-7 — utility construct
OPEN-B1-8 — state/rule-set consistency enforcement mechanism
```

Batch 3 may add bounded OPEN items if required, particularly:

```text
invalid rule-repository runtime handling
rule-engine evaluation strategy
decision-episode implementation boundary
```

Only add them if the authorities genuinely leave them unspecified.

Do not invent an answer merely to avoid OPEN status.

---

# 29. Stop conditions

If canonical authorities disagree about whether `RS(S)` is supplied before reasoning:

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 3 OPEN —
RS ENFORCEMENT AUTHORITY CONFLICT
```

If Algorithm 3 requires post-hoc filtering to satisfy the maintained architecture:

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 3 OPEN —
PRE-REASONING ENFORCEMENT CONTRACT INCOMPLETE
```

If Safety Dominance cannot be traced through:

```text
A_AI(S) → RS(S) → engine → AI(E)
```

without introducing a new scientific assumption:

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 3 OPEN —
SAFETY DOMINANCE DEPENDENCY GAP
```

If a new recommendation type, threshold or governance policy is required:

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 3 OPEN —
NEW SCIENTIFIC DECISION REQUIRED
```

If protected canonical state changes:

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 3 OPEN —
PROTECTED CANONICAL STATE DRIFT
```

Do not silently repair any of these.

---

# 30. Closure criteria

Close Batch 3 only when:

```text
[ ] Algorithm 3 supplies RS(S) before reasoning
[ ] ConclusionTypes(RS(S)) ⊆ A_AI(S)
[ ] RS(UNSAFE) = ∅
[ ] Algorithm 3 generates no advisory
[ ] invalid RS cannot silently enter reasoning
[ ] invalid-RS runtime handling remains bounded if unspecified

[ ] Algorithm 4 returns ∅ when G(S)=0
[ ] UNSAFE path does not invoke Layer 3 reasoning
[ ] participating path uses only RS(S)
[ ] engine-fidelity assumption is explicit
[ ] AI(E) ⊆ A_AI(S) dependency is preserved
[ ] no post-hoc filtering substitution exists

[ ] SAFE/CAUTION/UNSAFE state checks PASS
[ ] all required transition specification checks PASS
[ ] state/rule-set consistency invariant preserved
[ ] OPEN-B1-8 remains OPEN
[ ] no concurrency primitive invented

[ ] no concrete Layer 3 rules invented
[ ] no rule-engine strategy invented
[ ] human authority preserved

[ ] F1–F3 remain future fidelity evidence
[ ] E5 not run
[ ] complexity analysis not finalised

[ ] traceability complete
[ ] CSV parser checks PASS
[ ] protected canonical state unchanged
[ ] no new scientific decision introduced
```

---

# 31. Required report

Return:

## Algorithm 3

Final pseudocode and contract.

## Algorithm 4

Final pseudocode and contract.

## Safety Dominance dependency

Show explicitly:

```text
A_AI(S)
→ ConclusionTypes(RS(S))
→ engine restriction
→ AI(E) ⊆ A_AI(S)
```

and classify each dependency as definition, algorithmic contract, formal assumption or future fidelity obligation.

## State verification

Report SAFE / CAUTION / UNSAFE cases.

## Transition verification

Report all required state transitions.

## OPEN decisions

List only genuine unresolved implementation decisions.

## F1–F3 boundary

Explain what Batch 3 specifies versus what future prototype testing must demonstrate.

## Files changed

List each file and its scientific effect.

## Protected integrity

Report:

```text
unchanged
changed
verdict
```

---

# 32. Closure line

If all mandatory criteria PASS:

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 3 CLOSED —
RULE-SET ENFORCEMENT AND GOVERNED ADVISORY CONTRACT VERIFIED
```

Otherwise:

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 3 REMAINS OPEN —
LAYER 3 GOVERNANCE CONTRACT INCOMPLETE
```

---

# Guiding principle

Batch 1 established:

```text
what the algorithms must preserve
```

Batch 2 established:

```text
observations
→ F_{D,τ}
→ S
→ (G(S), A_AI(S))
```

Batch 3 establishes:

```text
(G(S), A_AI(S))
→ RS(S)
→ governed reasoning
→ AI(E) ⊆ A_AI(S)
```

It does **not** establish:

```text
concrete rule contents
prototype correctness
F1–F3 empirical results
latency
CPU/memory performance
decision-support utility
human outcome validity
real-world safety improvement
```

The objective is to make the governance enforcement contract precise enough that the **next implementation agent has no freedom to silently change the scientific architecture**.
