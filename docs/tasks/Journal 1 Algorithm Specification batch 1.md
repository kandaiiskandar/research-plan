# Task — Journal 1 Algorithm Specification

## Batch 1: Authority & Operational Contract

### Goal

Establish the authoritative operational contract that Algorithms 1–4 must later implement.

This batch is **specification only**.

Do not write the final four algorithms yet.
Do not implement Layer 3.
Do not run experiments or benchmarks.
Do not modify canonical scientific state.

---

## Branch

Use:

```text
design/journal1-algorithm-specification
```

No final closure commit is required until the whole algorithm-specification workstream is closed.

---

## Primary maintained authorities

Inspect at minimum:

```text
docs/canonical/appendix-c-formalisation.md
docs/canonical/architecture-illustration.md
docs/canonical/justification-layer3-enforcement.md

publications/active/journal-1/research-design.md
publications/active/journal-1/evaluation-specification.md
publications/active/journal-1/submissions/v1-initial-submission/manuscript.md
```

Canonical scripts may be inspected for semantic confirmation, but must not be changed.

---

## Protected state

Capture before-edit hashes for the same 16 protected canonical files used in the closed Journal 1 evaluation-specification workstream.

If any protected file differs unexpectedly before this task starts, stop and report:

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 1 OPEN —
PROTECTED STATE MISMATCH
```

---

# 1. Establish the operational classifier contract

The primary operational form must remain:

```text
f       : Y × V → S
ρ_{D,τ} : ∏ Obs_i → Y
F_{D,τ} = f ∘ ρ_{D,τ}

S = F_{D,τ}(obs,v)
```

Do not reduce Algorithm 1 later to only:

```text
S = f(E)
```

The ideal notation may remain as shorthand, but the operational contract must govern implementation.

---

# 2. Observation model

Verify and document:

```text
C = {w,r,m,o,t}

Obs_i = (X_i × 𝕋) ∪ {⊥}
```

Clarify exactly:

* what is an observation;
* what is configuration;
* where timestamps enter;
* where freshness `τ` enters;
* when `⊥` is produced.

Do not invent concrete freshness durations.

If freshness values are not specified, keep `τ` symbolic.

---

# 3. Vessel configuration

Verify and document that:

```text
v ∈ {small, medium, big}
```

is startup configuration, not a dynamic observation.

Missing/invalid `v` must be classified according to canonical authority.

Expected interpretation:

```text
startup refusal / configuration error
```

not runtime observation failure.

If authority differs, report the conflict rather than choosing silently.

---

# 4. Exclusion semantics

Verify:

```text
D = {m}
```

for historical replay.

But distinguish:

```text
historical replay exclusion
```

from:

```text
live deployment requirement
```

Confirm:

```text
t ∉ D
```

and that D does not dynamically grow.

Establish the exact meaning of:

```text
exclusion-before-fault
```

including what an excluded component contributes to the resolved classifier input.

Do not infer this from memory; verify from authority.

---

# 5. Fault semantics

For each required non-excluded observation, verify the canonical handling of:

```text
missing
invalid
stale
```

Expected chain:

```text
resolution failure
→ ⊥
→ component UNSAFE
→ global UNSAFE through max severity
```

Confirm whether this is exactly how the canonical formalisation defines it.

Do not introduce a separate global emergency shortcut unless formally equivalent and explicitly justified.

---

# 6. Rainfall operational contract

Verify and document exactly:

```text
g_r : ℝ≥0 × K → {SAFE, CAUTION, UNSAFE}
K = {0,1}
```

with:

```text
κ = χ(c)
```

and:

```text
χ(c)=1 iff c ∈ {95,96,99}
χ(c)=0 otherwise
```

including absent/unrecognised raw codes.

Preserve:

```text
missing raw code → κ=0
missing rainfall rate → ⊥
```

Do not redesign this behaviour.

Explicitly record that the raw weather-code default is:

```text
fail-open for the storm disjunct
```

and not a fail-safe.

---

# 7. Time / solar operational contract

Verify and document canonical `g_t`:

```text
SAFE
sunrise(date) ≤ t < sunset(date)

UNSAFE
otherwise
```

Required boundaries:

```text
exact sunrise = SAFE
exact sunset  = UNSAFE
```

`g_t` emits no CAUTION.

Required clock/date/solar-resolution failures must follow canonical fault semantics.

Do not reintroduce fixed clock windows.

Also confirm whether runtime classification consumes the frozen solar-event table rather than recomputing solar geometry.

---

# 8. Wind and wave contracts

Verify exact active boundaries.

Wind:

```text
SAFE      w ≤ 21.6
CAUTION   21.6 < w ≤ 27.0
UNSAFE    w > 27.0
```

Wave:

```text
small:
SAFE <1.0
CAUTION 1.0–1.25
UNSAFE >1.25

medium:
SAFE <1.4
CAUTION 1.4–2.8
UNSAFE >2.8

big:
SAFE <1.5
CAUTION 1.5–3.5
UNSAFE >3.5
```

Confirm that vessel category conditions `g_o`.

Do not introduce `g_v`.

---

# 9. Worst-case aggregation

Verify exact canonical aggregation:

```text
S = max-severity(
  g_w,
  g_r,
  g_m,
  g_o,
  g_t
)
```

Severity order:

```text
UNSAFE ≻ CAUTION ≻ SAFE
```

Document the resulting operational implications:

```text
any UNSAFE component → global UNSAFE

otherwise any CAUTION → global CAUTION

otherwise SAFE
```

Do not interpret UNSAFE as legal prohibition or certain physical danger.

---

# 10. Governance contract

Verify the finite mappings:

```text
G(SAFE)    = 1
G(CAUTION) = 1
G(UNSAFE)  = 0
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

Do not alter recommendation types or introduce subtypes.

---

# 11. RS(S) authority

Verify the maintained specification for:

```text
RS(SAFE)
RS(CAUTION)
RS(UNSAFE)
```

and the requirement that RS(S) is supplied before Layer 3 reasoning.

Do not yet design implementation details.

Record only:

* formal contract;
* preconditions;
* postconditions;
* unresolved implementation decisions.

---

# 12. Human authority

Confirm that:

```text
Human Decision
```

remains outside the AI governance restriction.

The architecture constrains AI advisory scope, not the human decision.

Do not introduce automated approval/prohibition semantics.

---

# 13. Create maintained Batch 1 artefact

Create:

```text
publications/active/journal-1/algorithm-specification.md
```

For this batch, populate only:

```text
1. Purpose and scope
2. Authority
3. Notation and interfaces
4. Operational observation-resolution contract
5. Component-classifier contract
6. Failure and exclusion semantics
7. Governance mappings
8. RS(S) pre-reasoning contract
9. Human-decision boundary
10. Open implementation decisions
```

Do not yet populate final pseudocode or complexity sections.

---

# 14. Evidence directory

Create:

```text
data/journal1-algorithm-specification/
```

For Batch 1 produce:

```text
integrity-before.json
authority-map.csv
operational-contract.csv
open-decisions.csv
semantic-verification-batch1.json
parser-test-batch1.json
change-map-batch1.csv
```

All CSV files must parse with:

```text
csv.DictReader
pandas.read_csv
```

with strict field counts.

---

# 15. Required semantic checks

At minimum verify:

```text
operational_F_D_tau_preserved
v_is_startup_configuration
D_replay_scope_preserved
exclusion_before_fault_preserved
tau_not_invented
rainfall_two_input_preserved
kappa_mapping_preserved
missing_raw_code_semantics_preserved
missing_rate_fault_semantics_preserved
wind_boundaries_preserved
wave_vessel_conditioning_preserved
no_g_v
solar_boundary_preserved
gt_no_caution
marine_replay_exclusion_not_live_policy
worst_case_aggregation_preserved
governance_mapping_preserved
RS_supply_before_reasoning_preserved
human_authority_preserved
```

Each must be:

```text
PASS
FAIL
OPEN
```

with evidence.

---

# 16. Stop conditions

If canonical sources disagree materially on operational semantics:

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 1 OPEN —
FORMAL AUTHORITY CONFLICT
```

If rainfall code/formal semantics disagree:

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 1 OPEN —
RAINFALL SEMANTIC CONFLICT
```

If solar semantics disagree:

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 1 OPEN —
SOLAR SEMANTIC CONFLICT
```

If a required implementation detail is genuinely unspecified, mark it as bounded OPEN.

Do not invent.

---

# 17. Closure criteria

Close Batch 1 only when:

```text
[ ] operational F_{D,τ} contract is explicit
[ ] observation vs configuration boundary is explicit
[ ] exclusion-before-fault is explicit
[ ] τ remains parameterised unless justified
[ ] rainfall κ semantics are explicit
[ ] solar boundaries are explicit
[ ] wind/wave boundaries are verified
[ ] g_o remains vessel-conditioned
[ ] no g_v introduced
[ ] governance mappings are explicit
[ ] RS(S) pre-reasoning contract is explicit
[ ] human authority is preserved
[ ] all open implementation decisions are listed
[ ] no canonical protected state changed
[ ] parser checks PASS
```

---

# Required report

Return:

## Authority findings

For each relevant construct, state its authoritative file and section.

## Confirmed operational contract

Summarise the exact contract Algorithms 1–4 must preserve.

## Open implementation decisions

List only genuinely unresolved items.

## Files changed

State scientific effect of each change.

## Protected state

Report integrity result.

## Verdict

If PASS:

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 1 CLOSED —
OPERATIONAL CONTRACT VERIFIED
```

Otherwise:

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 1 REMAINS OPEN —
OPERATIONAL SEMANTIC CONFLICT REMAINS
```

---

## Guiding rule

This batch answers only:

```text
"What exactly must the algorithms preserve?"
```

It does not yet answer:

```text
"How should all four algorithms be written?"
```

That is Batch 2 and Batch 3.
