# Journal 1 Layer 3 Prototype — Batch 1

## Fidelity and Failure-Semantics Repair

Batch 1 is **not yet accepted as closed**.

Do not design concrete advisory rules.
Do not invent Layer 2-derived Layer 3 rules.
Do not run F1–F3.
Do not run E5.
Do not modify canonical scientific state.

Perform only the bounded repairs below.

---

# 1. Resolve Batch 1 closure-status contradiction

Current artefacts disagree:

```text
report-batch1.md
→ OPEN — CONCRETE RULE CONTENT REQUIRES SCIENTIFIC SPECIFICATION
```

while:

```text
layer3-prototype-specification.md
→ Batch 1 CLOSED
→ OPEN-L3-1 does not block Batch 1 closure
```

Choose one interpretation and make every artefact consistent.

For this workstream, use the following boundary:

```text
Batch 1 = prototype contract and fidelity-testability design
Concrete rule CONTENT = next scientific subtask
```

Therefore concrete rule content does **not** need to exist for the
contract-design batch itself to close, provided the absence of rule
content is explicitly bounded and no fabricated rules are introduced.

Accordingly:

```text
OPEN-L3-1 remains OPEN
```

but it blocks:

```text
full executable prototype completion
F1–F3 execution
```

not the Batch 1 contract-design closure.

Update:

```text
report-batch1.md
layer3-prototype-specification.md
closure-batch1.json
semantic-verification-batch1.json
open-decisions-batch1.csv
```

so they all express the same status.

Do not mark OPEN-L3-1 itself closed.

---

# 2. Repair F3 assertion

Current wording incorrectly requires:

```text
if S_old != S_new:
    rule_set_id changes
```

This is not a valid general fidelity requirement.

A state transition does not logically require a different identifier.
For example:

```text
RS(SAFE) = ∅
RS(CAUTION) = ∅
```

is possible before concrete rule population.

Even after rule population, two states may share some or all rule
objects while still satisfying their admissibility contracts.

Replace identifier-change semantics with correspondence semantics.

Required F3 principle:

```text
For every new reasoning episode:

RS_used = RS(S_new)

and

no rule inconsistent with S_new is active.
```

For a transition:

```text
S_old → S_new
```

verify:

```text
active RS was freshly selected / bound for S_new
ConclusionTypes(RS_used) ⊆ A_AI(S_new)
∀ r ∈ RS_used:
    r is admissible for S_new
```

Do not require:

```text
rule_set_id_new != rule_set_id_old
```

unless the chosen identifier explicitly encodes state plus repository
version and that representation is documented.

A better trace field may be:

```text
rule_set_state
repository_version / snapshot_id
active_rule_ids
```

but do not invent a versioning system unless needed.

The minimum requirement is provenance sufficient to demonstrate that
the active rule set corresponds to `S_new`.

Update all F3 instrumentation tables, schemas, test plans, and report
text accordingly.

---

# 3. Do not treat predicate evaluation failure as FALSE without authority

Current specification says:

```text
condition predicate raises exception
→ rule does not fire
→ continue evaluating remaining rules
```

Remove this as an established runtime policy.

A predicate evaluation failure is not equivalent to:

```text
condition == false
```

unless separately justified.

Introduce a bounded OPEN item:

```text
OPEN-L3-2 — Rule-condition evaluation failure handling
```

State:

```text
If a rule predicate cannot be evaluated correctly,
the prototype must not silently reinterpret the failure
as a false predicate.
```

Until a failure policy is selected, permitted specification behaviour
is only:

```text
reasoning episode reports an evaluation failure
and no unsupported advisory is emitted from the failed evaluation
```

Do not yet decide whether the engine:

```text
aborts the episode
skips the rule
continues remaining rules
returns partial advisories
raises an exception
```

unless there is existing authority.

Those are implementation-policy choices.

Keep this bounded OPEN for the next implementation batch if necessary.

---

# 4. Repair ConfigurationError / FidelityTrace contract

Current text simultaneously states:

```text
execute_episode(...) → (advisories, FidelityTrace)
```

and:

```text
ConfigurationError propagates to caller
```

and:

```text
FidelityTrace always emitted
```

These statements require an explicit compatible interface.

Do not invent hidden side-channel behaviour.

Choose a simple contract-level representation.

Preferred options include either:

```text
A. Result object:
EpisodeResult {
    advisories
    trace
    error
}
```

or:

```text
B. exception carrying / exposing the trace explicitly
```

or another repository-native equivalent.

Whichever is chosen must guarantee:

```text
configuration failure is observable
fidelity trace remains obtainable
no advisory is emitted
S is unchanged
```

Do not imply that a normal tuple is returned while an uncaught exception
simultaneously prevents the return.

Document the exact function contract.

---

# 5. Preserve the strong parts

Do not change the following already-correct decisions:

```text
R = {Go, Delay, DepartureTime, Duration}

G(SAFE)=1
G(CAUTION)=1
G(UNSAFE)=0

A_AI(SAFE)=FULL
A_AI(CAUTION)={Go, Delay}
A_AI(UNSAFE)=∅
```

Preserve:

```text
RS selection
→ RS validation
→ reasoning
```

Preserve:

```text
no post-hoc advisory filtering as the primary governance mechanism
```

Preserve:

```text
UNSAFE
→ no Layer 3 reasoning
→ AI(E)=∅
```

Preserve unconditional human authority.

---

# 6. Concrete rule content remains OPEN

Do not invent any IF–THEN rule.

Retain:

```text
OPEN-L3-1 —
Concrete Layer 3 advisory rule content requires scientific specification
```

The report correctly found that Layer 2 thresholds do not automatically
become Layer 3 advisory rules.

Keep this explicit.

---

# 7. Engine strategy status

The linear-scan prototype strategy may remain as a bounded
implementation design choice if desired.

However, phrase the status carefully:

```text
prototype evaluation strategy = linear scan
production strategy = OPEN-B3-2
```

Do not say Theorem C.3 depends on the linear-scan choice.

Do not claim production engine strategy is closed.

---

# 8. New semantic verification checks

Add at minimum:

```text
batch1_status_consistent_across_artifacts
open_L3_1_does_not_silently_close
F3_requires_state_correspondence_not_identifier_change
empty_SAFE_and_CAUTION_rule_sets_do_not_false_fail_F3
predicate_error_not_reinterpreted_as_false_without_authority
rule_condition_failure_policy_bounded_OPEN
configuration_failure_trace_contract_coherent
configuration_failure_emits_no_advisory
S_unchanged_on_configuration_failure
F1_F3_not_run
E5_not_run
protected_canonical_state_unchanged
```

Each:

```text
PASS
FAIL
OPEN
```

with evidence.

`OPEN-L3-1` and `OPEN-L3-2` may remain OPEN without preventing the
contract-design batch from closing.

---

# 9. Closure criteria

Close this repair only when:

```text
[ ] report and maintained specification agree on Batch 1 status
[ ] OPEN-L3-1 remains explicit
[ ] no concrete rules were invented
[ ] F3 no longer requires rule_set_id to change
[ ] F3 verifies correspondence to S_new
[ ] predicate evaluation failure is not silently treated as FALSE
[ ] OPEN-L3-2 records unresolved evaluation-failure policy
[ ] ConfigurationError / FidelityTrace interface is coherent
[ ] no advisory emitted on configuration failure
[ ] S remains unchanged
[ ] F1–F3 remain NOT YET TESTED
[ ] E5 remains unexecuted
[ ] protected canonical state unchanged
```

---

# 10. Closure line

If all repair criteria pass:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 1 CLOSED —
FIDELITY TRACE AND FAILURE-SEMANTICS CONTRACT REPAIRED
```

Otherwise:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 1 REMAINS OPEN —
FIDELITY OR FAILURE-SEMANTICS CONTRACT GAP REMAINS
```

---

# Guiding distinction

Preserve:

```text
state changed
≠ rule-set identifier must change
```

Preserve:

```text
predicate evaluation failed
≠ predicate evaluated FALSE
```

Preserve:

```text
configuration failure
≠ environmental UNSAFE
```

and:

```text
instrumentation designed
≠ implementation fidelity demonstrated
```
