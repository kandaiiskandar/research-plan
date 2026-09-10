# Task — Journal 1 Algorithm Specification

## Batch 4: Complexity Analysis & Manuscript Integration

### Goal

Complete the final specification batch for Journal 1 by:

```text
1. deriving bounded time and space complexity for Algorithms 1–4;
2. separating fixed-architecture complexity from generalized complexity;
3. parameterising any complexity that depends on an unspecified rule-engine strategy;
4. integrating the four algorithms and their complexity claims into the active Journal 1 manuscript;
5. closing the full Algorithm Specification & Complexity Analysis workstream.
```

This is still a **specification and manuscript-integration task**.

Do not build the Layer 3 prototype.
Do not run F1–F3.
Do not run E5.
Do not benchmark latency, CPU, memory or energy.
Do not invent rule-engine internals.
Do not claim deployability from asymptotic complexity.
Do not change canonical scientific state.

---

# 1. Branch

Continue on:

```text
design/journal1-algorithm-specification
```

Do not create a new branch.

Batch 3 is CLOSED with:

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 3 CLOSED —
RULE-SET ENFORCEMENT AND GOVERNED ADVISORY CONTRACT VERIFIED
```

Do not reopen Algorithms 1–4 unless a direct contradiction is discovered.

---

# 2. Immediate authorities

Primary maintained authority:

```text
publications/active/journal-1/algorithm-specification.md
```

This now contains:

```text
Batch 1 — Operational contract
Batch 2 — Algorithms 1 & 2
Batch 3 — Algorithms 3 & 4
```

Canonical authorities remain read-only:

```text
docs/canonical/appendix-c-formalisation.md
docs/canonical/architecture-illustration.md
docs/canonical/justification-layer3-enforcement.md
publications/active/journal-1/evaluation-specification.md
publications/active/journal-1/research-design.md
```

The active Journal 1 manuscript to integrate into is:

```text
publications/active/journal-1/v1-initial-submission/manuscript.md
```

Do not treat the path name "initial-submission" as evidence that the manuscript was submitted.

---

# 3. Protected scientific state

Before editing, verify the same protected canonical state used in Batches 1–3.

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

If protected state differs unexpectedly, STOP:

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 4 OPEN —
PROTECTED CANONICAL STATE DRIFT
```

---

# 4. Complexity-analysis principle

The analysis must distinguish:

```text
fixed current architecture
≠
generalized architecture
≠
concrete implementation performance
```

Do not conflate asymptotic complexity with runtime performance.

Do not write:

```text
O(1), therefore suitable for low-resource environments.
```

That claim requires implementation evidence.

The correct bounded framing is:

```text
The current architecture has a fixed number of environmental components,
so several governance operations are constant-size with respect to the
current model definition. This does not establish device-level performance,
latency, memory suitability, energy efficiency or deployability.
```

E5 remains the empirical performance workstream.

---

# 5. Complexity notation

Use a compact, explicit parameter set.

At minimum consider:

```text
n     = number of condition components
|S|   = number of governance states
|R|   = number of recommendation types
k_S   = number of rules in RS(S)
k     = size of the configured rule repository
q     = number of rule evaluations / firings performed by the engine
c     = cost of one rule-condition evaluation
```

If another variable is needed, introduce it only when necessary and define it explicitly.

Current architecture values include:

```text
n = 5
|S| = 3
|R| = 4
```

Do not silently generalize empirical thresholds or scientific semantics when generalizing computational complexity.

---

# 6. Algorithm 1 complexity

Analyse:

```text
Algorithm 1 — Operational Safety Classification
```

Current fixed architecture:

```text
C = {w,r,m,o,t}
```

Therefore only five component channels exist.

Analyse separately:

```text
startup validation
exclusion handling
observation validation/freshness
κ derivation
solar lookup
component classification
max-severity aggregation
```

Expected direction:

```text
fixed current architecture:
O(1)
```

because `n=5` is fixed by the architecture.

Also give generalized form:

```text
O(n + T_solar_lookup)
```

or the exact justified equivalent.

Do not assume solar lookup is automatically O(1) unless the actual representation supports that claim.

Inspect the maintained implementation contract / frozen solar artefact usage.

If lookup implementation is not sufficiently specified, write:

```text
T_solar_lookup
```

rather than inventing:

```text
O(1)
O(log d)
```

---

# 7. Algorithm 1 space complexity

Separate:

```text
static configuration storage
per-decision working memory
```

Generalized working memory should be expressed in terms of `n` where appropriate.

For the fixed architecture, a constant-size resolved observation vector and five component states may justify:

```text
O(1)
```

working memory.

Do not count raw external datasets as per-decision working memory.

Do not count the entire historical replay dataset as Algorithm 1 memory complexity.

---

# 8. Algorithm 2 complexity

Analyse:

```text
Algorithm 2 — Governance Configuration
```

The current mapping has exactly three states and four recommendation types.

Current implementation:

```text
switch S
→ return (G(S), A_AI(S))
```

Expected current complexity:

```text
Time:  O(1)
Space: O(1)
```

Generalized design table may be expressed as:

```text
storage O(|S| · |R|)
```

if represented explicitly as a state-to-admissible-set mapping.

Distinguish:

```text
lookup complexity
```

from:

```text
static mapping storage
```

Do not imply the architecture dynamically searches all recommendation types on every decision unless the algorithm actually does so.

---

# 9. Algorithm 3 complexity

Analyse:

```text
Algorithm 3 — Rule-Set Supply
```

This is implementation-sensitive.

Current contract contains:

```text
candidate(repository, S)
```

and a compliance check:

```text
ConclusionTypes(RS_candidate) ⊆ A_AI(S)
```

Distinguish at least two conceptual costs:

```text
rule-set selection/reference cost
rule-set validation/materialisation cost
```

If a prevalidated state-indexed rule set is referenced directly, selection may be constant-time.

If Algorithm 3 materialises or scans `k_S` candidate rules and validates every conclusion type, the cost may be:

```text
O(k_S)
```

Do NOT choose one implementation as canonical unless authority requires it.

Use parameterised language such as:

```text
T_A3 = T_select(S) + O(k_S)
```

where the `O(k_S)` term applies when per-supply compliance validation scans the candidate set.

If compliance is prevalidated at configuration time, record that as an implementation option, not a scientific conclusion.

Do not silently eliminate OPEN-B3-1 or OPEN-B1-8.

---

# 10. Algorithm 3 space complexity

Distinguish:

```text
reference-only RS(S)
```

versus:

```text
materialised rule-set copy
```

Possible bounded forms:

```text
O(1) auxiliary space
```

for reference selection, or:

```text
O(k_S)
```

if a fresh materialised rule set is constructed.

Do not choose a representation without evidence.

Record the representation dependency explicitly.

---

# 11. Algorithm 4 complexity

Analyse:

```text
Algorithm 4 — Governed Advisory Generation
```

The governance wrapper itself is simple:

```text
check G(S)
if 0 → return ∅
else → invoke engine.reason(E, RS(S))
```

Separate:

```text
governance wrapper cost
```

from:

```text
rule-engine reasoning cost
```

The wrapper may be:

```text
O(1)
```

but the total Algorithm 4 cost must be parameterised by the rule engine.

Do not write:

```text
Algorithm 4 = O(1)
```

for the entire reasoning path unless the engine is proven constant-cost.

---

# 12. Rule-engine complexity

OPEN-B3-2 remains authoritative:

```text
Rule-engine evaluation strategy unspecified
```

Therefore do not assume:

```text
forward chaining
backward chaining
RETE
first-match
all-match
agenda priority
conflict resolution
```

Use a bounded parameterised expression.

At minimum consider:

```text
T_engine(k_S, q, c)
```

or an equivalent clearly defined function.

If a generic linear scan is discussed, label it explicitly as an example implementation:

```text
Example only — not canonical:
O(k_S · c)
```

Do not convert an illustrative complexity into the architecture's official complexity.

---

# 13. Algorithm 4 space complexity

Separate:

```text
governance wrapper auxiliary memory
```

from:

```text
rule-engine working memory
```

The wrapper can likely remain:

```text
O(1)
```

but total memory must be expressed as:

```text
O(1) + M_engine(...)
```

or equivalent.

Do not invent engine agenda size, RETE network size or caching behaviour.

---

# 14. Full pipeline complexity

Provide a bounded end-to-end expression for one decision episode:

```text
Algorithm 1
+
Algorithm 2
+
Algorithm 3
+
Algorithm 4
```

A generalized expression may take a form equivalent to:

```text
T_episode
=
O(n)
+ T_solar_lookup
+ T_A2
+ T_A3
+ T_engine
```

with current fixed architecture simplifying only the governance/classification terms.

Do not hide the rule-engine term.

Do not claim the full pipeline is O(1) merely because `n=5`, `|S|=3`, and `|R|=4`.

---

# 15. Complexity table

Create a concise table containing at minimum:

```text
Algorithm
Current fixed-model time
Generalized time
Auxiliary space
Primary dependency
Bounded OPEN / implementation dependency
```

Expected broad shape:

```text
A1
fixed O(1)
generalized O(n + T_solar_lookup)

A2
O(1)
generalized mapping storage O(|S|·|R|)

A3
parameterised by selection/materialisation and k_S

A4
O(1) governance wrapper + T_engine(...)
```

Do not force uniform notation if it hides important implementation uncertainty.

---

# 16. Low-resource claim boundary

Audit every new sentence relating complexity to low-resource environments.

Allowed:

```text
The classifier and governance mappings operate over small fixed state spaces.
```

Allowed:

```text
The architecture avoids model-size growth with the number of replay records
during a single decision episode.
```

Not allowed without E5:

```text
The architecture is lightweight.
The architecture is efficient on low-end phones.
The architecture is deployable in low-resource settings.
The latency is negligible.
Memory use is minimal.
Energy use is low.
```

If existing manuscript text makes such claims without evidence, repair them.

---

# 17. Complexity vs replay dataset size

Explicitly distinguish per-decision complexity from retrospective evaluation complexity.

Do not write that historical replay over 43,848 records is O(1).

If manuscript needs this distinction, state:

```text
Per-decision classification complexity is independent of replay length
for the fixed architecture, whereas replaying N historical records requires
N decision evaluations and therefore scales linearly in N, excluding
external data-loading costs.
```

If using a replay-size variable, define it separately, e.g.:

```text
N = number of replay records
```

Then:

```text
replay classification cost ≈ O(N · T_episode_without_engine)
```

only where applicable.

Do not mix replay complexity into Algorithm 1's single-decision complexity table.

---

# 18. Manuscript integration

Inspect the active Journal 1 manuscript:

```text
publications/active/journal-1/v1-initial-submission/manuscript.md
```

Identify the appropriate sections for:

```text
Algorithm 1
Algorithm 2
Algorithm 3
Algorithm 4
complexity analysis
implementation-fidelity boundary
```

Integrate publication-ready versions without duplicating large sections unnecessarily.

The manuscript should contain sufficient pseudocode / algorithm summaries for reviewer understanding.

The maintained `algorithm-specification.md` remains the detailed internal authority.

Do not turn the manuscript into a repository specification document.

---

# 19. Algorithm naming consistency

Use exactly:

```text
Algorithm 1 — Operational Safety Classification
Algorithm 2 — Governance Configuration
Algorithm 3 — Rule-Set Supply
Algorithm 4 — Governed Advisory Generation
```

Audit manuscript and specification for conflicting algorithm names.

Do not introduce:

```text
Safety Algorithm
Gating Algorithm
AI Safety Filter
Decision Algorithm
```

as alternate formal names unless used descriptively and clearly non-authoritatively.

---

# 20. Formal notation consistency

Audit manuscript integration for:

```text
F_{D,τ}
ρ_{D,τ}
f
S
G(S)
A_AI(S)
RS(S)
AI(E)
```

Preserve:

```text
F_{D,τ} = f ∘ ρ_{D,τ}
```

Do not regress to:

```text
S = f(E)
```

as the operational algorithm.

Do not reintroduce `g_v`.

Do not alter rainfall signature.

Do not alter solar boundary.

---

# 21. Safety Dominance manuscript wording

The manuscript should describe the dependency in bounded form:

```text
A_AI(S)
→ RS(S)
→ rule-engine restriction
→ AI(E) ⊆ A_AI(S)
```

Do not write:

```text
the algorithm guarantees safe decisions
```

or:

```text
the AI cannot produce unsafe advice
```

Use the precise architecture claim:

```text
the governed advisory output is constrained to the configured admissible
recommendation types for the current safety state, subject to the stated
rule-engine fidelity assumptions.
```

Do not equate advisory-scope containment with correctness of advice.

---

# 22. Human authority wording

Ensure manuscript integration preserves:

```text
Human Decision unconditional
```

and that Algorithms 3–4 constrain AI output only.

Do not introduce wording suggesting:

```text
UNSAFE prohibits departure
SAFE approves departure
CAUTION requires delay
```

unless describing AI advisory types rather than human authority.

---

# 23. F1–F3 boundary in manuscript

Ensure manuscript does not imply Algorithms 1–4 are already implemented and fidelity-tested unless the prototype exists.

Use language equivalent to:

```text
The algorithms define the implementation contract.
Implementation fidelity will be evaluated separately using F1–F3.
```

Do not report:

```text
F1 PASS
F2 PASS
F3 PASS
```

in this batch.

---

# 24. E5 boundary

Do not run or fabricate:

```text
mean latency
median latency
p95
p99
CPU
memory
energy
throughput
```

Do not set:

```text
H3 = X ms
```

OPEN-B1-6 remains OPEN.

Complexity analysis is not E5 evidence.

---

# 25. OPEN items

Preserve all prior OPEN items.

Batch 1:

```text
OPEN-B1-1 freshness parameters
OPEN-B1-2 runtime provenance capture
OPEN-B1-3 medium-vessel evidence limitation
OPEN-B1-4 concrete Layer 3 rules
OPEN-B1-5 live g_m configuration
OPEN-B1-6 latency threshold
OPEN-B1-7 utility construct
OPEN-B1-8 state/rule-set consistency enforcement mechanism
```

Batch 3:

```text
OPEN-B3-1 invalid rule-repository runtime handling
OPEN-B3-2 rule-engine evaluation strategy
OPEN-B3-3 decision-episode implementation boundary
```

Do not silently close any through asymptotic analysis.

If complexity analysis reveals a new implementation-dependent item, add a bounded OPEN.

---

# 26. Update maintained authority

Extend:

```text
publications/active/journal-1/algorithm-specification.md
```

Suggested sections:

```text
25. Complexity Analysis — Notation and Scope
26. Algorithm 1 Complexity
27. Algorithm 2 Complexity
28. Algorithm 3 Complexity
29. Algorithm 4 Complexity
30. End-to-End Decision-Episode Complexity
31. Space Complexity
32. Complexity Claim Boundaries
33. Manuscript Integration Trace
```

Do not alter prior algorithms except to fix a genuine contradiction.

---

# 27. Evidence artefacts

In:

```text
data/journal1-algorithm-specification/
```

add:

```text
complexity-analysis-batch4.csv
complexity-traceability-batch4.csv
manuscript-integration-batch4.csv
semantic-verification-batch4.json
parser-test-batch4.json
change-map-batch4.csv
closure-batch4.json
report-batch4.md
```

Update `build.py` only as needed to validate Batch 4 evidence.

Do not replace prior evidence artefacts.

---

# 28. Required complexity traceability

For every complexity claim record:

```text
algorithm
operation
current fixed-model bound
generalized bound
space bound
assumption
implementation dependency
authority
claim status
```

Claim status should distinguish:

```text
DERIVED
PARAMETERISED
OPEN
ILLUSTRATIVE ONLY
```

Do not label an illustrative engine example as DERIVED.

---

# 29. Required semantic checks

At minimum:

```text
algorithm1_fixed_vs_generalized_complexity_distinguished
solar_lookup_complexity_not_invented
algorithm1_space_bounded
algorithm2_time_constant_for_fixed_mapping
algorithm2_storage_generalization_bounded
algorithm3_selection_vs_materialization_distinguished
algorithm3_kS_dependency_explicit
algorithm4_wrapper_vs_engine_cost_separated
rule_engine_complexity_parameterized
rule_engine_strategy_not_invented
end_to_end_complexity_retains_engine_term
space_complexity_separates_static_and_working_memory
replay_N_not_confused_with_per_decision_complexity
low_resource_claim_not_inferred_from_big_O
E5_not_substituted_by_complexity
F1_F3_not_reported_as_results
H3_threshold_remains_open
all_prior_open_items_preserved
manuscript_algorithms_consistent
manuscript_formal_notation_consistent
safety_dominance_wording_bounded
human_authority_preserved
no_new_scientific_decision
protected_state_unchanged
```

Each:

```text
PASS
FAIL
OPEN
```

with evidence.

---

# 30. Manuscript integration verification

Verify at minimum:

```text
all four algorithm names consistent
F_{D,τ} remains operational classifier
no g_v
rainfall two-input signature preserved
g_t no CAUTION
exact sunrise/sunset semantics not contradicted
G(S) exact
A_AI(S) exact
RS(S) pre-reasoning
no post-hoc filtering substitution
Safety Dominance wording bounded
human authority unconditional
F1–F3 future
E5 future
```

Do not make unrelated manuscript edits.

---

# 31. Stop conditions

If a complexity claim requires selecting a rule-engine strategy:

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 4 OPEN —
RULE-ENGINE COMPLEXITY REQUIRES IMPLEMENTATION DECISION
```

If manuscript integration exposes a contradiction with Algorithms 1–4:

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 4 OPEN —
MANUSCRIPT ALGORITHM CONTRACT CONFLICT
```

If a claim about low-resource suitability requires empirical evidence:

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 4 OPEN —
LOW-RESOURCE PERFORMANCE CLAIM REQUIRES E5
```

If a new scientific decision is required:

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 4 OPEN —
NEW SCIENTIFIC DECISION REQUIRED
```

If protected canonical state changes:

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 4 OPEN —
PROTECTED CANONICAL STATE DRIFT
```

Do not silently resolve these.

---

# 32. Closure criteria

Close only when:

```text
[ ] A1 fixed and generalized complexity derived
[ ] A1 solar lookup cost bounded without invention
[ ] A1 time/space separated

[ ] A2 time complexity derived
[ ] A2 static mapping storage distinguished

[ ] A3 selection/materialisation distinction explicit
[ ] A3 k_S dependency explicit
[ ] A3 representation dependency bounded

[ ] A4 governance wrapper separated from engine cost
[ ] rule-engine term parameterised
[ ] no engine strategy invented

[ ] end-to-end expression retains rule-engine dependency
[ ] per-decision vs replay-N complexity distinguished
[ ] static storage vs working memory distinguished

[ ] no low-resource deployability claim inferred from asymptotics
[ ] E5 remains future empirical performance evidence
[ ] H3 remains OPEN

[ ] Algorithms 1–4 integrated consistently into manuscript
[ ] formal notation preserved
[ ] Safety Dominance wording bounded
[ ] human authority preserved
[ ] F1–F3 remain future fidelity evidence

[ ] all prior OPEN items preserved
[ ] parser checks PASS
[ ] protected canonical state unchanged
[ ] no new scientific decision introduced
```

---

# 33. Required report

Return:

## Complexity summary

Provide a concise table for Algorithms 1–4.

## Algorithm 1

Explain fixed vs generalized time and space complexity.

## Algorithm 2

Explain lookup and static mapping storage.

## Algorithm 3

Explain `k_S`, selection/materialisation dependency and relevant OPEN items.

## Algorithm 4

Separate governance wrapper from engine reasoning cost.

## End-to-end

Give one bounded decision-episode expression.

## Replay complexity distinction

Explain single-decision versus N-record retrospective replay.

## Low-resource boundary

State exactly what asymptotic results do and do not establish.

## Manuscript integration

List sections edited and scientific effect.

## OPEN items

Confirm prior OPEN items remain open.

## Protected integrity

Report:

```text
unchanged
changed
verdict
```

---

# 34. Closure line

If all mandatory criteria PASS:

```text
JOURNAL 1 ALGORITHM SPECIFICATION AND COMPLEXITY ANALYSIS CLOSED —
FOUR-ALGORITHM CONTRACT, COMPLEXITY BOUNDS AND MANUSCRIPT INTEGRATION VERIFIED
```

Otherwise:

```text
JOURNAL 1 ALGORITHM SPECIFICATION AND COMPLEXITY ANALYSIS REMAINS OPEN —
COMPLEXITY OR MANUSCRIPT CONTRACT GAP REMAINS
```

---

# Guiding principle

The full workstream must preserve:

```text
formal definition
≠ algorithm specification
≠ asymptotic complexity
≠ implementation
≠ implementation-fidelity evidence
≠ performance evidence
≠ human/outcome validation
```

Batch 4 closes only the first three layers:

```text
formal architecture
→ algorithm contract
→ bounded complexity analysis
```

The next workstream after successful closure is:

```text
Layer 3 Prototype Implementation
→ F1–F3 implementation-fidelity testing
→ E5 performance measurement
```

Do not cross that boundary in Batch 4.
