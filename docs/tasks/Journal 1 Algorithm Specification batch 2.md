# Task — Journal 1 Algorithm Specification

## Batch 2: Algorithms 1 & 2

### Goal

Formalise exactly two publication-quality algorithms from the CLOSED Batch 1 operational contract:

```text
Algorithm 1 — Operational Safety Classification
Algorithm 2 — Governance Configuration
```

This is a **formal algorithm-specification task**.

Do not implement production code.
Do not implement Layer 3.
Do not design Algorithms 3–4.
Do not perform complexity analysis.
Do not run experiments or benchmarks.
Do not change canonical scientific state.

---

## Branch

Continue on:

```text
design/journal1-algorithm-specification
```

Do not create a new branch.

No workstream-closing commit is required yet.

---

# 1. Immediate authority

The primary maintained authority for this batch is:

```text
publications/active/journal-1/algorithm-specification.md
```

Batch 1 is CLOSED with:

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 1 CLOSED —
TRANSITION CONSISTENCY CONTRACT REPAIRED
```

Treat §§1–10 of `algorithm-specification.md` as the interface contract that Algorithms 1–2 must implement.

Use canonical sources only to verify that the algorithms faithfully instantiate that contract.

Do not reopen Batch 1 unless a direct contradiction is discovered.

---

# 2. Protected scientific state

Before editing, capture integrity of the same 16 protected canonical files used by Batch 1.

Do not modify:

```text
docs/canonical/*
scripts/canonical_gt.py
scripts/canonical_figures.py
scripts/condition_comparison.py
scripts/historical_replay.py
scripts/hysteresis_analysis.py
scripts/diagnostic_binding.py
data/prediction-register.csv
data/solar/solar-events-daily.csv
data/raw_weather_sea.csv
data/raw_marine_era5_sea.csv
data/raw_marine_mfwam.csv
submitted conference manuscripts
```

If protected state differs unexpectedly before work begins, STOP:

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 2 OPEN —
PROTECTED STATE MISMATCH
```

---

# 3. Algorithm 1

Create publication-quality pseudocode for:

```text
Algorithm 1 — Operational Safety Classification
```

It must implement:

```text
S = F_{D,τ}(obs,v)
```

where:

```text
ρ_{D,τ} : ∏ Obs_i → Y

f : Y × V → S

F_{D,τ} = f ∘ ρ_{D,τ}
```

Algorithm 1 must NOT be reduced to:

```text
S = f(E)
```

---

# 4. Algorithm 1 required sequence

The pseudocode must make this ordering explicit:

```text
1. Validate startup configuration v.
2. Validate exclusion set D.
3. Apply declared exclusions before fault handling.
4. Resolve required non-excluded observations.
5. Apply validation and freshness semantics.
6. Derive κ from the raw weather code.
7. Resolve time/date/solar dependency.
8. Evaluate component classifiers.
9. Aggregate using max severity.
10. Return exactly one S.
```

Do not introduce new scientific branches.

---

# 5. Startup configuration

Preserve:

```text
v ∈ {small, medium, big}
```

`v` is startup configuration.

If `v` is missing or invalid:

```text
REFUSE STARTUP / CONFIGURATION ERROR
```

Do NOT return:

```text
UNSAFE
```

as though missing `v` were a runtime observation fault.

---

# 6. Exclusion semantics

Preserve the Batch 1 contract:

```text
t ∉ D
D ⊊ C
```

and:

```text
for i ∈ D:
    component contribution = SAFE
```

Exclusion occurs before fault evaluation.

Do not inspect an excluded component and then convert its missing value to `⊥`.

The retrospective replay uses:

```text
D = {m}
```

but Algorithm 1 must remain general over a valid deployment-specific `D`.

Do not hard-code `{m}` into the general algorithm.

---

# 7. Observation resolution

For each required non-excluded observation, preserve:

```text
invalid → ⊥
absent  → ⊥
stale   → ⊥
```

Freshness remains parameterised by `τ` / `age_i`.

Do not invent concrete freshness values.

Then preserve:

```text
g_i(⊥) = UNSAFE
```

for the required classifier input.

Do not add a scientifically separate global missing-data shortcut.

---

# 8. Rainfall handling

Algorithm 1 must explicitly preserve the two-input rainfall classifier.

Use:

```text
κ = χ(c)
```

where:

```text
χ(c)=1 iff c ∈ {95,96,99}
χ(c)=0 otherwise
```

including absent or unrecognised raw codes.

Therefore:

```text
missing rainfall rate
→ ⊥
→ UNSAFE
```

but:

```text
missing/unrecognised raw weather code
→ κ=0
```

not `⊥`.

Do not “improve” this behaviour.

---

# 9. Component classification

Algorithm 1 must call the canonical component classifiers:

```text
g_w
g_r
g_m
g_o
g_t
```

There must be exactly five classifier contributions.

Do not introduce:

```text
g_v
```

`v` only conditions:

```text
g_o(o,v)
```

---

# 10. Time / solar handling

Preserve:

```text
SAFE:
sunrise(date) ≤ t < sunset(date)

UNSAFE:
otherwise
```

Therefore:

```text
exact sunrise → SAFE
exact sunset  → UNSAFE
```

and:

```text
g_t emits no CAUTION
```

Required clock/date/solar lookup failure follows the canonical fault path.

Algorithm 1 should consume the canonical frozen solar-event dependency according to the Batch 1 contract.

Do not recompute astronomical geometry inside Algorithm 1.

Do not introduce fixed 06:00 / 17:00 / 19:00 boundaries.

---

# 11. Aggregation

The final classification must be:

```text
S = max-severity(
    s_w,
    s_r,
    s_m,
    s_o,
    s_t
)
```

under:

```text
UNSAFE ≻ CAUTION ≻ SAFE
```

Therefore:

```text
any UNSAFE → UNSAFE
else any CAUTION → CAUTION
else SAFE
```

Do not redefine UNSAFE as physical danger, legal prohibition, or forced human action.

---

# 12. Algorithm 1 contract

Document explicitly:

### Inputs

At minimum:

```text
obs
v
D
τ
required date/solar dependency
```

Use exact maintained notation where possible.

### Output

```text
S ∈ {SAFE, CAUTION, UNSAFE}
```

### Preconditions

Include only authority-supported requirements.

### Postconditions

At minimum:

```text
exactly one S is returned for a valid startup configuration
```

and required non-excluded resolution failure causes the corresponding component to become UNSAFE.

### Failure behaviour

Distinguish:

```text
startup/configuration failure
```

from:

```text
runtime observation fault
```

---

# 13. Algorithm 2

Create publication-quality pseudocode for:

```text
Algorithm 2 — Governance Configuration
```

Input:

```text
S
```

Output:

```text
G(S)
A_AI(S)
```

Do NOT make Algorithm 2 perform Layer 3 reasoning.

Do NOT make Algorithm 2 generate recommendations.

---

# 14. Algorithm 2 mapping

The algorithm must implement exactly:

```text
SAFE
→
G = 1
A_AI = {Go, Delay, DepartureTime, Duration}

CAUTION
→
G = 1
A_AI = {Go, Delay}

UNSAFE
→
G = 0
A_AI = ∅
```

No additional state.

No recommendation subtype.

No dynamic threshold.

No probability.

---

# 15. Algorithm 2 contract

Document:

### Input

```text
S ∈ {SAFE, CAUTION, UNSAFE}
```

### Output

```text
(G(S), A_AI(S))
```

### Preconditions

`S` must be a valid output of Algorithm 1 / `F_{D,τ}`.

### Postconditions

Preserve:

```text
G(S)=0 ⇒ A_AI(S)=∅
```

and:

```text
A_AI(SAFE)
⊃
A_AI(CAUTION)
⊃
A_AI(UNSAFE)=∅
```

Do not claim Algorithm 2 experimentally validates Monotonicity.

It implements the finite mapping on which the formal property is established.

---

# 16. RS(S) boundary

Batch 2 may reference:

```text
RS(S)
```

only to define the handoff to the next algorithm.

Do NOT implement rule-set selection in Algorithm 2 unless the existing formal authority explicitly defines it as part of Algorithm 2.

Preferred boundary:

```text
Algorithm 1
obs → S

Algorithm 2
S → (G(S), A_AI(S))

Algorithm 3 — future Batch 3
(S, G(S), A_AI(S)) → RS(S)
```

Preserve the Batch 1 transition-consistency contract for future Algorithm 3.

Do not choose an atomicity/concurrency mechanism.

`OPEN-B1-8` remains OPEN.

---

# 17. Boundary verification

Create specification-level tests for Algorithm 1.

At minimum:

```text
w = 21.6
→ g_w SAFE

w = 27.0
→ g_w CAUTION

w > 27.0
→ g_w UNSAFE

r = 10, κ=0
→ g_r SAFE

r = 20, κ=0
→ g_r CAUTION

κ=1
→ g_r UNSAFE

small o = 1.0
→ g_o CAUTION

small o = 1.25
→ g_o CAUTION

medium o = 1.4
→ g_o CAUTION

medium o = 2.8
→ g_o CAUTION

big o = 1.5
→ g_o CAUTION

big o = 3.5
→ g_o CAUTION

exact sunrise
→ g_t SAFE

exact sunset
→ g_t UNSAFE

nighttime
→ g_t UNSAFE

missing rainfall rate
→ rainfall component UNSAFE

missing raw weather code + valid rate
→ κ=0, classify from rate

excluded m
→ SAFE contribution

missing non-excluded m
→ UNSAFE contribution

missing/invalid v
→ startup refusal
```

These are:

```text
SPECIFICATION CHECKS
```

not empirical experiments.

---

# 18. Algorithm 2 verification

Verify all three possible inputs exhaustively:

```text
SAFE
CAUTION
UNSAFE
```

Check:

```text
G(S)
A_AI(S)
```

against the maintained mapping.

Also verify:

```text
A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE)
```

No statistical test is needed.

---

# 19. Correctness mapping

For Algorithms 1–2, explicitly distinguish:

```text
definition
algorithm implementation of definition
formal theorem/property
future implementation-fidelity test
```

Algorithm 1 should be mapped to operational totality / fail-safe semantics.

Algorithm 2 should be mapped to participation, advisory restriction and monotonicity.

Do not write:

```text
Algorithm 1 proves safety.
Algorithm 2 validates monotonicity experimentally.
```

Use bounded formal language.

---

# 20. Update maintained authority

Update:

```text
publications/active/journal-1/algorithm-specification.md
```

Add only the sections required for Algorithms 1–2.

Suggested additions:

```text
11. Algorithm 1 — Operational Safety Classification
12. Algorithm 1 — Preconditions and Postconditions
13. Algorithm 2 — Governance Configuration
14. Algorithm 2 — Preconditions and Postconditions
15. Batch 2 Boundary Verification
16. Batch 2 Correctness Traceability
```

Do not populate Algorithms 3–4 or complexity analysis yet.

---

# 21. Evidence

In:

```text
data/journal1-algorithm-specification/
```

add:

```text
algorithm-contracts-batch2.csv
boundary-cases-batch2.csv
algorithm-traceability-batch2.csv
semantic-verification-batch2.json
parser-test-batch2.json
change-map-batch2.csv
closure-batch2.json
report-batch2.md
```

You may extend the existing `build.py` to validate these files.

Do not replace Batch 1 evidence.

---

# 22. Required semantic checks

At minimum:

```text
algorithm1_implements_F_D_tau
algorithm1_not_reduced_to_ideal_f
startup_v_semantics_preserved
D_wellformedness_preserved
exclusion_before_fault_preserved
tau_not_invented
rainfall_two_input_preserved
kappa_total_mapping_preserved
missing_rate_semantics_preserved
missing_code_semantics_preserved
exactly_five_component_classifiers
no_g_v
solar_half_open_boundary_preserved
gt_no_caution
frozen_solar_dependency_preserved
worst_case_aggregation_preserved
algorithm1_returns_exactly_one_state
algorithm2_G_mapping_exact
algorithm2_AAI_mapping_exact
monotone_scope_containment_preserved
algorithm2_no_advisory_generation
RS_selection_deferred_to_batch3
human_authority_not_modified
```

Each:

```text
PASS
FAIL
OPEN
```

with evidence.

---

# 23. OPEN items

Do not attempt to close Batch 1 OPEN items merely because Algorithms 1–2 are being written.

In particular preserve:

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

If an OPEN item does not affect Algorithms 1–2, leave it untouched.

---

# 24. Stop conditions

If Algorithm 1 cannot be written without contradicting the Batch 1 operational contract:

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 2 OPEN —
ALGORITHM 1 SEMANTIC CONFLICT
```

If Algorithm 2 cannot reproduce the exact governance mapping:

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 2 OPEN —
ALGORITHM 2 GOVERNANCE CONFLICT
```

If completing either algorithm requires a new threshold, classifier, recommendation type or scientific policy:

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 2 OPEN —
NEW SCIENTIFIC DECISION REQUIRED
```

If protected canonical state changes unexpectedly:

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 2 OPEN —
PROTECTED CANONICAL STATE DRIFT
```

Do not silently resolve any of these.

---

# 25. Closure criteria

Close only when:

```text
[ ] Algorithm 1 implements F_{D,τ}
[ ] startup v semantics preserved
[ ] D well-formedness preserved
[ ] exclusion-before-fault preserved
[ ] τ remains parameterised
[ ] rainfall rate/κ distinction preserved
[ ] five classifiers only
[ ] no g_v
[ ] solar half-open boundary preserved
[ ] exact sunrise SAFE
[ ] exact sunset UNSAFE
[ ] worst-case aggregation preserved
[ ] Algorithm 1 returns exactly one valid state

[ ] Algorithm 2 exactly implements G(S)
[ ] Algorithm 2 exactly implements A_AI(S)
[ ] containment preserved
[ ] no recommendation generated
[ ] no RS(S) implementation pulled forward from Batch 3

[ ] boundary cases PASS
[ ] correctness traceability complete
[ ] all CSV parser checks PASS
[ ] protected canonical state unchanged
[ ] no new scientific decision introduced
```

---

# 26. Required report

Return a concise report containing:

## Algorithm 1

Show final pseudocode and contract.

## Algorithm 2

Show final pseudocode and contract.

## Boundary verification

Report PASS/FAIL for each boundary case.

## Correctness mapping

State which properties are definition-derived, theorem-derived, or deferred to future implementation fidelity.

## OPEN items

Report only items relevant to Algorithms 1–2 plus confirmation that existing Batch 1 OPEN items were not silently closed.

## Files changed

List each file and scientific effect.

## Protected integrity

Report:

```text
unchanged
changed
verdict
```

---

# 27. Closure line

If all mandatory criteria PASS:

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 2 CLOSED —
ALGORITHMS 1 AND 2 VERIFIED AGAINST OPERATIONAL CONTRACT
```

Otherwise:

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 2 REMAINS OPEN —
ALGORITHMIC SEMANTIC CONFLICT REMAINS
```

---

# Guiding principle

Batch 1 established:

```text
what the algorithms must preserve
```

Batch 2 establishes only:

```text
how Algorithm 1 computes S
and
how Algorithm 2 maps S to governance scope
```

Do not move ahead to:

```text
RS(S) execution
Layer 3 reasoning
Algorithms 3–4
prototype implementation
complexity analysis
F1–F3
E5 benchmarking
human/outcome validation
```

Those belong to later batches.

The objective is precision, not completeness.
