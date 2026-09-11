# Journal 1 — Layer 3 Prototype Specification

**Status:** Batch 1 CLOSED — fidelity trace and failure-semantics contract repaired (2026-09-11). Batch 2 CLOSED — CAUTION-Go presentation semantics resolved (2026-09-11, OPEN-L3-3 resolution B). OPEN-L3-2 CLOSED — predicate evaluation failure semantics explicitly governed (2026-09-11, three-valued semantics with episode-level refusal).  
**Closed on:** Batch 1: 2026-09-11 | Batch 2: 2026-09-11  
*(Historical — superseded: (i) Batch 2 CLOSED WITH BOUNDED OPEN ITEMS — advisory rule evidence and semantics partially specified. (ii) Batch 2 REMAINS OPEN — OPEN-L3-3 CAUTION-Go authority semantics unresolved. Current status set on OPEN-L3-3 Resolution B: appendix-c line 791 governs presentation of a rule-generated Go advisory, not automatic emission — see `data/journal1-layer3-prototype/open-l3-3-resolution/`.)*  
**Branch (document origin):** `design/journal1-algorithm-specification` *(OPEN-L3-2 resolution authored on `design/journal1-layer3-predicate-failure-policy`; OPEN-L3-2 micro-repair performed on the same branch)*  
**Task (Batch 1):** [`docs/tasks/Journal 1 Layer 3 Prototype Implementation batch 1.md`](../../../docs/tasks/Journal%201%20Layer%203%20Prototype%20Implementation%20batch%201.md)  
**Task (Batch 2):** [`docs/tasks/Journal 1 Layer 3 Prototype batch 2.md`](../../../docs/tasks/Journal%201%20Layer%203%20Prototype%20batch%202.md)  
**Repair task:** [`docs/tasks/Journal 1 Layer 3 Prototype — Batch 1 repair.md`](../../../docs/tasks/Journal%201%20Layer%203%20Prototype%20%E2%80%94%20Batch%201%20repair.md)  
**Evidence directory:** [`data/journal1-layer3-prototype/`](../../../data/journal1-layer3-prototype/)

---

## 1. Purpose and scope

This document is the implementation authority for the Journal 1 Layer 3 prototype. It defines **how the four-algorithm contract becomes executable software** — without turning engineering choices into new scientific claims.

The prototype implements the governance pair `(G(S), A_AI(S))` and the Layer 3 rule engine described in the closed algorithm specification workstream. It does not extend, modify, or reinterpret any element of the scientific architecture.

**This batch covers:**

- Prototype module boundaries
- Rule representation schema
- Rule-set representation
- Recommendation output representation
- Decision context representation
- Algorithm 3 implementation contract (rule-set selection and validation)
- Reasoning episode interface
- State/rule-set consistency contract
- Fidelity instrumentation design for F1–F3
- Error and configuration handling

**Explicitly out of scope for Batch 1:**

- Concrete advisory rule content (OPEN-L3-1 — requires scientific specification)
- Full prototype implementation (Batch 2 and later)
- F1–F3 fidelity results (deferred to Layer 3 build + test)
- E5 performance benchmarking (requires prototype; threshold remains OPEN)
- Any change to the scientific architecture, formal variables, governance mappings, thresholds, or recommendation types

---

## 2. Upstream authority

Treat the following as closed upstream authority. Read-only — no modification permitted.

| Document | Role |
|---|---|
| `publications/active/journal-1/algorithm-specification.md` | Algorithms 1–4 operational contracts |
| `publications/active/journal-1/evaluation-specification.md` | F1–F3 fidelity criteria; E5 performance criterion |
| `publications/active/journal-1/research-design.md` | Research module map |
| `docs/canonical/appendix-c-formalisation.md` | Single source of truth for all formal variable definitions |
| `docs/canonical/architecture-illustration.md` | Full architecture walkthrough |
| `docs/canonical/justification-layer3-enforcement.md` | Layer 3 model type (production rule system); Safety Dominance proof by construction |

The Algorithm Specification workstream closed with:

```
JOURNAL 1 ALGORITHM SPECIFICATION AND COMPLEXITY ANALYSIS CLOSED —
ALGORITHM 3 COMPLEXITY AND AUTHORITY RESIDUE REPAIRED
```

---

## 3. Prototype module boundaries

The prototype implements Layer 3 of the governance pipeline:

```
observations
→ ρ_{D,τ}                    [NOT in prototype scope — classifier is upstream]
→ F_{D,τ} = f ∘ ρ_{D,τ}     [NOT in prototype scope — classifier is upstream]
→ S
→ G(S), A_AI(S)              [GovernanceConfig — governance/ modules]
→ RS(S)                      [rule_set_provider.py — Algorithm 3]
→ Layer 3 reasoning           [reasoning_engine.py — Algorithm 4]
→ AI(E)                      [Advisory list — advisory.py]
→ Human Decision              [NOT in prototype scope — unconditional human authority]
```

The prototype receives `S` from the caller (already classified). It does not re-implement the classifier or the resolution map.

**Module structure (Python — consistent with existing `scripts/*.py` convention):**

```
governance/
  __init__.py
  rule.py              Rule dataclass
  advisory.py          Advisory dataclass
  rule_repository.py   State-indexed rule collection
  rule_set_provider.py Algorithm 3: select → validate → supply
  reasoning_engine.py  Algorithm 4: linear scan, fire rules
  reasoning_episode.py ReasoningEpisode struct + execute_episode()
  fidelity_trace.py    FidelityTrace dataclass + emit_fidelity_trace()
```

The `governance/` package is a new implementation directory. It does not overlap with any existing script in `scripts/`. No existing file is modified.

---

## 4. Rule representation

Each rule in the Layer 3 production rule engine is represented by the following dataclass:

```python
@dataclasses.dataclass(frozen=True)
class Rule:
    rule_id: str
    applicable_state: str           # "SAFE" or "CAUTION" — never "UNSAFE"
    conditions: tuple               # sequence of ConditionPredicate (see §4.1)
    conclusion_type: str            # ∈ R = {"Go","Delay","DepartureTime","Duration"}
    conclusion_payload: dict        # type-specific content — OPEN-L3-1
    provenance: str                 # scientific authority reference
    enabled: bool
```

**Invariants enforced at construction and at supply:**

- `applicable_state ∈ {"SAFE","CAUTION"}` — enforced by `rule_repository.py` on insert
- `conclusion_type ∈ R` — enforced by `rule.py` constructor
- For `applicable_state == "CAUTION"`: `conclusion_type ∈ {"Go","Delay"}` — enforced by `validate_rule_set()` at supply time (Algorithm 3 contract)
- `provenance` must be non-empty — enforced by `rule_repository.py` on insert

### 4.1 Condition predicate schema

A condition predicate is a triple `(variable, operator, value)` evaluated against the `DecisionContext` (§7):

```python
@dataclasses.dataclass(frozen=True)
class ConditionPredicate:
    variable: str     # field name in DecisionContext
    operator: str     # one of: "<", "<=", "==", ">=", ">", "in", "not_in",
                      #         "is_none", "is_not_none"
    value: object     # threshold or set — None for is_none / is_not_none operators
```

All conditions in a rule are evaluated as a conjunction (AND). A rule fires only when all conditions are satisfied.

**Content status:** **OPEN-L3-1.** The condition predicate schema is defined. Concrete predicates — which environmental variables, which thresholds, which operators — require scientific specification before any rule can be added to the repository. Do not invent predicates from Layer 2 thresholds.

The full JSON schema for a rule object is at `data/journal1-layer3-prototype/rule-schema-batch1.json`.

---

## 5. Rule-set representation

### RS(UNSAFE) = ∅

The empty rule set for UNSAFE is not a populated collection — it is the **absence** of a rule set. The UNSAFE path does not call `select_rule_set()` or `validate_rule_set()`. `execute_episode()` returns an empty advisory list directly when `G(state) == 0`.

### RS(SAFE) and RS(CAUTION)

Both are represented as **state-indexed lists of Rule objects** drawn from the repository:

```python
RS_SAFE    = [r for r in repository.rules if r.applicable_state == "SAFE"    and r.enabled]
RS_CAUTION = [r for r in repository.rules if r.applicable_state == "CAUTION" and r.enabled]
```

The repository holds all rules. `select_rule_set(repository, state)` extracts the relevant subset. `validate_rule_set(candidate, state)` verifies the containment invariant before supply.

**The Algorithm 3 contract is preserved:** selection and validation precede supply; supply precedes reasoning.

---

## 6. Recommendation representation

An advisory instance is distinct from a recommendation type:

```python
@dataclasses.dataclass(frozen=True)
class Advisory:
    type: str          # ∈ R; additionally ∈ A_AI(S) for the governing state
    payload: dict      # type-specific content (OPEN-L3-1)
    rule_id: str       # which rule in RS(S) fired
    explanation: str   # human-readable rationale text
```

**Invariant:** `advisory.type ∈ A_AI(S)` for every emitted advisory — guaranteed by construction because the engine fires only rules in the validated `RS(S)`, and `ConclusionTypes(RS(S)) ⊆ A_AI(S)` was verified by `validate_rule_set()` before reasoning began.

**The advisory list may be empty.** An empty list is a valid output; it is not equivalent to a prohibition.

**No advisory type encodes a human decision.** A `Go` advisory is not a departure approval. The `Advisory` class has no field for `approved`, `prohibited`, `override`, or `automated_decision`.

---

## 7. Decision context representation

The Layer 3 reasoning context is a `DecisionContext` object. It represents the resolved environmental state as received from upstream — not a redefinition of canonical `E`.

```python
@dataclasses.dataclass(frozen=True)
class DecisionContext:
    episode_id: str              # unique identifier for this reasoning episode
    vessel_category: str         # v ∈ {"small","medium","big"} — configured parameter

    # Resolved component values from ρ_{D,τ} — None where excluded or faulted
    resolved_w: float | None           # wind speed, knots; None if w faulted
    resolved_r_rate: float | None      # rainfall rate, mm/hr; None if r excluded/faulted
    resolved_r_kappa: int | None       # thunderstorm indicator κ ∈ {0,1}; None if r excluded/faulted
    resolved_m: str | None             # marine warning level; None (D={m} in replay)
    resolved_o_wave_height: float | None   # wave height, metres; None if o faulted
    resolved_o_swell_period: float | None  # swell period, seconds; may be None (not read by g_o)
    resolved_t: float | None           # time of day, hours [0,24); None only if t faulted (rare)
```

**This does not extend canonical `E`.** The fields correspond directly to the canonical condition components `C = {w, r, m, o, t}` plus vessel category `v`. No new scientific variable is introduced.

If Layer 3 implementation in later batches identifies a need for additional advisory inputs not derivable from canonical `E`, those inputs must be documented explicitly here as implementation-level additions — they must not silently extend the formal definition of `E` in `appendix-c-formalisation.md`.

### 7.1 ComponentStateTrace — Layer 2 component-state interface

*(Added Batch 4B-1, 2026-09-11. Implementation deferred to Batch 4B-2.)*

**Purpose.** `ComponentStateTrace` is an implementation-level interface object produced by Layer 2 and passed to Layer 3 alongside `S`. It carries the already-computed component classification results — the outputs of `g_w`, `g_r`, `g_m`, `g_o`, and `g_t` that Layer 2 produced during the same evaluation episode that determined `S`. Layer 3 rule predicates may inspect these values without reimplementing any Layer 2 classifier.

**Authority.** This interface is authorised by the Batch 4A resolution (2026-09-11, Model B accepted). The provision that implementation-level additions to `DecisionContext` must be documented explicitly here (§7 above) is the canonical gate for this entry. `appendix-c-formalisation.md` is unchanged — no formal variable is added to `E`, `ρ_{D,τ}`, `f`, or `F_{D,τ}`.

**Producer and consumer:**

```
Layer 2 computes g_i(·) as part of determining S.
Layer 2 produces ComponentStateTrace from the same resolved component results.
Layer 3 receives ComponentStateTrace as a read-only input.
Layer 3 does NOT recompute g_w, g_r, g_m, g_o, or g_t.
```

**Proposed fields and domains.**

```python
# ComponentStateTrace fields — to be added to DecisionContext in Batch 4B-2
component_w_state: str   # ∈ {"SAFE", "CAUTION", "EXCLUDED"}
component_r_state: str   # ∈ {"SAFE", "CAUTION", "EXCLUDED"}
component_m_state: str   # ∈ {"SAFE", "CAUTION", "EXCLUDED"}
component_o_state: str   # ∈ {"SAFE", "CAUTION", "EXCLUDED"}
component_t_state: str   # ∈ {"SAFE", "EXCLUDED"}   — g_t emits no CAUTION
```

The domain `{SAFE, CAUTION, EXCLUDED}` is the Layer 3-visible interface type domain. Valid runtime values are constrained further by canonical semantics:

- **`UNSAFE` is unreachable at the Layer 3 interface.** If any component produces UNSAFE, then `S = UNSAFE`, `G(UNSAFE) = 0`, and Layer 3 is never invoked. UNSAFE is an internal Layer 2 state; it does not appear in ComponentStateTrace at the Layer 3 reasoning boundary. This is an execution-boundary consequence, not a redefinition of `g_i` — the classifiers can and do return UNSAFE, but Layer 3 never sees it.
- **`EXCLUDED` is distinct from observed `SAFE`.** A component in the declared exclusion set `D` is pinned SAFE for aggregation purposes (appendix-c C.2.0.5), but the interface exposes its true status as `EXCLUDED`. `EXCLUDED ≠ observed SAFE`.
- **`component_t_state` domain is `{SAFE, "EXCLUDED"}` in the type.** However, `t ∉ D` always (appendix-c C.2.0.5 D1), so `EXCLUDED` is unreachable for `t` at runtime under the current canonical configuration. If `g_t` produces UNSAFE, gate-off applies before Layer 3 executes.
- **`component_m_state = EXCLUDED` in retrospective replay.** The replay runs with `D = {m}` because no historical marine warning archive exists for the study site. `component_m_state = EXCLUDED` means only that `m` is excluded under the declared replay configuration — it does not assert `m = none` or absence of marine hazard. All figures under `D = {m}` are lower bounds on hazard exposure.

**Fault semantics.** Faulted components (`obs_i = ⊥` → `g_i(⊥) = UNSAFE`) cause `S = UNSAFE` and Layer 3 gate-off. The fault resolves through existing Layer 2 fail-safe semantics (Corollary C.1b.1). Faulted states are not visible to Layer 3. `FAULTED` is not a new component governance state — it is absorbed by the UNSAFE gate-off path.

**Read-only requirement.** Layer 3 must not modify, cache, or feed back any component state value. The component states are facts about the current episode's Layer 2 classification; they must not carry over to the next episode.

**No Layer 2 recomputation.** Layer 3 rule predicates must not reproduce threshold comparisons — not `resolved_w >= 21.6`, not vessel-category wave bands, not rainfall rate ranges, not solar event lookups. A predicate such as `component_o_state == "CAUTION"` is permissible because it consumes an already-computed Layer 2 result. A predicate that re-derives the same result from raw values is a Layer 2 classifier duplication and is prohibited.

**Execution ordering contract.** The execution order is fixed:

```
1.  Layer 2 resolves observations via ρ_{D,τ}.
2.  Layer 2 evaluates component gates g_w, g_r, g_m, g_o, g_t.
3.  Layer 2 determines S = max-severity(g_i(·)).
4.  Layer 2 produces ComponentStateTrace from the same resolved component results.
5.  Governance configuration G(S), A_AI(S) is established.
6.  If G(S) = 0: no Layer 3 reasoning. Episode ends.
7.  Otherwise: Layer 3 receives S + ComponentStateTrace + other DecisionContext inputs.
8.  RS(S) is selected and validated (Algorithm 3).
9.  Structural validation occurs.
10. Rule predicates may inspect ComponentStateTrace fields.
11. Reasoning produces AI(E) (Algorithm 4).
12. Safety Dominance AI(E) ⊆ A_AI(S) remains enforced by construction.
```

ComponentStateTrace is produced in step 4. It cannot independently select a different RS than S or modify governance configuration.

**Episode consistency invariant.** ComponentStateTrace must correspond to the same Layer 2 evaluation episode that produced S. Layer 3 must never receive:

```
S from episode A  +  ComponentStateTrace from episode B
```

Implementation contract: `episode_id(S) = episode_id(ComponentStateTrace)`. The `episode_id` field in `DecisionContext` serves as the episode identifier.

**S / component-state consistency invariant.** ComponentStateTrace and S must be semantically consistent:

```
S = SAFE    → all active (non-excluded) components are SAFE
S = CAUTION → at least one active component is CAUTION; none is UNSAFE
S = UNSAFE  → Layer 3 is gated off; ComponentStateTrace not visible to Layer 3
```

`EXCLUDED` is not active for aggregation and does not contradict S. If an inconsistency is detected at an implementation boundary, it must be classified as a configuration/interface fidelity failure unless existing authority establishes another category. Handling is not specified here; it is Batch 4B-2 engineering work.

**Safety Dominance.** ComponentStateTrace does not modify `A_AI(S)`, `G(S)`, or `RS(S)`. `AI(E) ⊆ A_AI(S)` continues to hold by construction from the rule set (Theorem C.3, appendix-c §C.7.2). The proof depends only on the value of S; it is independent of interface content beyond S.

**Human authority.** ComponentStateTrace does not introduce automatic prohibition, automatic approval, or restriction of human override. No advisory generated by a rule whose predicate inspects a component state becomes mandatory. The human operator retains unconditional authority over the departure decision in all states.

**Future rule representations (informative, not yet implemented).** Based on Batch 4A dispositions, the three authorised-in-principle rules have the following candidate predicate representations when ComponentStateTrace is available:

```
R-CAUTION-002:  component_o_state == "CAUTION"
R-CAUTION-003:  component_r_state == "CAUTION"
R-CAUTION-004:  component_w_state == "CAUTION"
```

These representations are documented here for specification completeness. They must not be added to `governance/canonical_rules.py` until Batch 4B-2 is authorised and executed.

**R-SAFE-001** remains DEFERRED (STATE_RESTATEMENT, Batch 4A). No `component_*_state == "SAFE"` conjunction may be used to implement it without a bounded scientific decision resolving the state-restatement finding.

**R-CAUTION-001** future migration consideration: `resolved_m == "advisory"` is equivalent to `component_m_state == "CAUTION"` under the current `g_m` definition. Migration to the component-state form is a future consistency consideration; it is not authorised in Batch 4B-1 or Batch 4B-2 without separate review.

**Non-goals.** ComponentStateTrace is not:
- A new governance layer
- A replacement or extension of canonical E, ρ_{D,τ}, f, or F_{D,τ}
- A second classifier
- A source of reasons (fault/hazard/policy)
- A mechanism for S to be re-determined inside Layer 3
- A basis for automatic departure approval or prohibition

**OPEN-L3-3 protection.** ComponentStateTrace must not create a CAUTION→Go rule. The preserved resolution is: `S = CAUTION ∧ Go ∈ AI(E) → Present(Go, caution_qualifier)`. NOT: `S = CAUTION → Go ∈ AI(E)`.

---

## 8. Rule-set selection and validation (Algorithm 3 implementation)

`rule_set_provider.py` implements Algorithm 3 from `algorithm-specification.md` §17.

### 8.1 Interface contracts

**`select_rule_set(repository, state) → list[Rule]`**

| Field | Value |
|---|---|
| Inputs | `repository: RuleRepository`, `state: str` ∈ `{"SAFE","CAUTION","UNSAFE"}` |
| Outputs | `RS_candidate: list[Rule]` — enabled rules for the given state |
| Preconditions | `state ∈ {"SAFE","CAUTION","UNSAFE"}`; repository initialised |
| Postconditions | All returned rules have `applicable_state == state` and `enabled == True` |
| Failure | `state == "UNSAFE"`: returns `[]` immediately (RS(UNSAFE) = ∅); `state` not recognized: raises `ConfigurationError` |
| Scientific invariant | RS(UNSAFE) is never populated; G(UNSAFE) = 0 prevents this path in `execute_episode()` |

**`validate_rule_set(candidate, state) → None`**

| Field | Value |
|---|---|
| Inputs | `candidate: list[Rule]`, `state: str` ∈ `{"SAFE","CAUTION"}` |
| Outputs | None — raises on violation |
| Preconditions | `state ∈ {"SAFE","CAUTION"}`; candidate produced by `select_rule_set` |
| Postconditions | `ConclusionTypes(candidate) ⊆ A_AI(state)` verified |
| Failure | Violation: raises `ConfigurationError` with structured failure record (OPEN-B3-1 — see §12) |
| Scientific invariant | Invalid repository does not modify S; does not create an advisory; does not silently continue with invalid rules |

### 8.2 OPEN-B3-1 handling

Invalid repository → `ConfigurationError` raised with a structured record including:

```python
ConfigurationError(
    episode_id = context.episode_id,
    state = state,
    violation = "ConclusionTypes(RS_candidate) ⊄ A_AI(state)",
    offending_rules = [...],  # rule_ids of violating rules
)
```

Layer 3 is disabled for the episode. The caller receives the `ConfigurationError`. S is not modified. No advisory is created. `FidelityTrace` records `configuration_failure=True` and `generated_advisory_types=[]`.

This closes **OPEN-B3-1 at implementation level** — the scientific state model is unchanged.

---

## 9. Reasoning episode interface

### 9.1 ReasoningEpisode

```python
@dataclasses.dataclass(frozen=True)
class GovernanceConfig:
    G: int                     # 0 or 1
    A_AI: frozenset[str]       # admissible recommendation types

@dataclasses.dataclass
class ReasoningEpisode:
    state: str                 # S ∈ {"SAFE","CAUTION","UNSAFE"}
    governance: GovernanceConfig
    rule_set: list[Rule]       # RS(S) as validated and supplied by Algorithm 3
    context: DecisionContext
```

**Invariant:** all four fields belong to the same classification event. No field from a previous episode may carry over.

### 9.2 execute_episode()

`reasoning_episode.py` implements the combined Algorithm 3 + Algorithm 4 pipeline.

**Return type — `EpisodeResult`:**

```python
@dataclasses.dataclass
class EpisodeResult:
    advisories: list[Advisory]   # empty on UNSAFE, configuration failure, or no rules firing
    trace: FidelityTrace         # always present — never None
    error: Exception | None      # ConfigurationError or None; None on success
```

This ensures configuration failure is always observable (`error` field), the fidelity trace is always obtainable (`trace` field), and no advisory is emitted on failure (`advisories = []`).

**`execute_episode(state, repository, context) → EpisodeResult`**

| Field | Value |
|---|---|
| Inputs | `state: str`, `repository: RuleRepository`, `context: DecisionContext` |
| Outputs | `EpisodeResult` — always returned; `trace` is never None |
| Preconditions | `state` classified; repository initialised; context resolved from upstream classifier |
| Postconditions | `result.advisories` contains only types in A_AI(state). If `state == "UNSAFE"` or `result.error is not None`: `result.advisories == []`. `result.trace` records episode state, governance, and configuration failure status. |
| Failure | `ConfigurationError`: `result.error` is set; `result.advisories = []`; `result.trace.configuration_failure = True`; S unchanged. |
| Scientific invariant | One episode → one S → one G(S) → one A_AI(S) → one RS(S). No stale RS from a previous episode. |

**UNSAFE path (exact):**

```
state == "UNSAFE"
→ G = 0
→ A_AI = ∅
→ no rule set selected or validated
→ no reasoning
→ return EpisodeResult(
      advisories=[],
      trace=FidelityTrace(state="UNSAFE", G=0, A_AI=∅, active_rule_ids=[], ...),
      error=None,
  )
```

### 9.3 Engine strategy (OPEN-B3-2 — partially closed for prototype)

The prototype uses a **linear scan engine**:

1. Iterate all enabled rules in `RS(S)` in order.
2. For each rule, evaluate every condition predicate against `context`.
3. If all conditions are satisfied, the rule fires: append an `Advisory` with `type = rule.conclusion_type`.
4. Collect all fired advisories.

**Why chosen:** Simplest deterministic engine sufficient to test the governance contract (F1/F2/F3). No optimisation required at specification stage.

**Complexity:** O(k_S × c) where k_S = |RS(S)| and c = average number of conditions per rule. This closes the `T_engine = O(k_S, q, c)` parameterised bound from `algorithm-specification.md` §29 for the prototype case.

**What this choice does NOT affect:** Safety Dominance (Theorem C.3) holds by construction from rule-set content, not engine strategy. All formal propositions P1–P3 are independent of evaluation order.

**Production chaining strategy** (RETE, agenda priority, first-match, all-match, backward chaining) remains **OPEN-B3-2** for production deployment.

### 9.4 Episode boundary (OPEN-B3-3 — partially closed)

One episode = one `execute_episode()` call. The episode boundary is the function boundary. Episode duration, polling interval, and refresh frequency are **not specified** — they depend on the scheduling model of the deployment runtime, which is out of scope for Batch 1.

---

## 10. State/rule-set consistency contract

**Invariant:** one reasoning episode uses exactly one governing S, one corresponding G(S), one A_AI(S), and one RS(S).

The implementation enforces this through the call boundary: `execute_episode(state, repository, context)` performs selection, validation, and reasoning in a single synchronous call. The `state` argument determines which RS is selected; the same `state` argument determines the A_AI constraint passed to `validate_rule_set()`. No intermediate step can interleave a different S.

**OPEN-B1-8 (concurrency primitive) remains OPEN.** If the deployment runtime runs multiple goroutines or threads sharing the rule repository or the governance state, the choice of synchronisation mechanism (lock, atomic reference, transaction, immutable snapshotting) must be made explicitly at that level. The interface is designed to permit any of these without API change: `execute_episode()` takes a `repository` argument, so a concurrent runtime can pass a frozen snapshot without altering the function signature.

---

## 11. Fidelity instrumentation

`fidelity_trace.py` instruments each reasoning episode to support future F1–F3 testing.

### 11.1 FidelityTrace schema

```python
@dataclasses.dataclass
class FidelityTrace:
    episode_id: str
    state: str                          # S
    G: int                              # G(S)
    A_AI: frozenset[str]                # A_AI(S)
    active_rule_ids: list[str]          # all rules in RS(S) passed to engine
    active_rule_conclusion_types: frozenset[str]  # ConclusionTypes(RS(S))
    fired_rule_ids: list[str]           # rules whose conditions were satisfied
    generated_advisory_types: list[str] # conclusion_type of each Advisory produced
    configuration_failure: bool         # True if ConfigurationError raised this episode
    # Transition fields (for F3)
    S_old: str | None                   # state of the immediately preceding episode
    S_new: str                          # state of this episode (= state field)
    rule_set_bound_for_state: str       # the state value passed to select_rule_set(); must equal S_new in every valid episode — provides correspondence provenance without requiring an identifier-change check
```

**`emit_fidelity_trace()` always returns a trace.** Internal errors do not suppress trace emission. Configuration failures are recorded in the trace rather than silently swallowed.

### 11.2 F1–F3 mapping

| Fidelity criterion | Required field(s) | Required assertion | Status |
|---|---|---|---|
| **F1** — no type outside A_AI(S) | `generated_advisory_types`, `A_AI` | `∀ t ∈ generated_advisory_types: t ∈ A_AI` | DESIGNED — NOT YET TESTED |
| **F1** — exhaustive coverage | `active_rule_conclusion_types`, `A_AI` | `active_rule_conclusion_types ⊆ A_AI` | DESIGNED — NOT YET TESTED |
| **F2** — violation count zero | `generated_advisory_types`, `A_AI` | `count({t: t ∉ A_AI}) == 0` | DESIGNED — NOT YET TESTED |
| **F3** — RS corresponds to S_new | `rule_set_bound_for_state`, `S_new` | `rule_set_bound_for_state == S_new` — RS was freshly selected for the governing state of this episode | DESIGNED — NOT YET TESTED |
| **F3** — RS admissibility for S_new | `active_rule_ids`, `active_rule_conclusion_types`, `A_AI` | `ConclusionTypes(RS_used) ⊆ A_AI(S_new)`; `∀ r ∈ active_rule_ids: r.applicable_state == S_new` | DESIGNED — NOT YET TESTED |

Full field-level mapping at `data/journal1-layer3-prototype/fidelity-instrumentation-batch1.csv`.

**None of these are F1/F2/F3 PASS.** All are DESIGNED — NOT YET TESTED.

---

## 12. Error and configuration handling

**Invalid rule repository (OPEN-B3-1 — closed at implementation level):**

```
validate_rule_set() detects ConclusionTypes(RS_candidate) ⊄ A_AI(S)
→ EpisodeResult returned with:
    advisories = []
    trace = FidelityTrace(configuration_failure=True, generated_advisory_types=[], ...)
    error = ConfigurationError(structured record: episode_id, state, violation, offending_rules)
→ S is not modified
→ caller inspects result.error to detect the failure
→ Layer 3 is disabled for this episode
```

This closes OPEN-B3-1 for prototype implementation. The scientific state model is unchanged: `ConfigurationError` is an implementation-level fault, not a new safety state.

**Unknown state argument:**

```
execute_episode(state="FOOBAR", ...)
→ EpisodeResult(advisories=[], trace=FidelityTrace(configuration_failure=True, ...), error=ConfigurationError("Unknown state: FOOBAR"))
```

**Rule condition evaluation error (OPEN-L3-2 — CLOSED 2026-09-11):**

**Selected policy: Model C + Model D — three-valued predicate semantics with episode-level refusal.** Full evidence: `data/journal1-layer3-prototype/open-l3-2-resolution/`.

**Predicate result domain:** `{TRUE, FALSE, ERROR}`
- `TRUE` — antecedent successfully evaluated and satisfied
- `FALSE` — antecedent successfully evaluated and not satisfied
- `ERROR` — antecedent could not be established (evaluation failed)

**Rule firing condition:** A rule fires if and only if all predicates evaluate `TRUE`. Neither `FALSE` nor `ERROR` triggers rule firing. `ERROR` is not reinterpreted as `FALSE`.

**Episode-level behaviour on any predicate `ERROR`:**

```
any predicate evaluation ERROR in any rule
→ AI(E) = ∅
→ S unchanged; G unchanged; A_AI unchanged
→ evaluation_failure = True in trace
→ failed_rule_ids and failure_category recorded
→ human authority preserved (∅ does not constrain human decision)
```

Other rules do not continue after a predicate evaluation failure. No partial advisory output is produced. The trace always emits; evaluation failure cannot suppress it.

**Implementation note:** The engine may abort on first failure or complete evaluation of all rules before refusing advisory generation. Both produce `AI(E) = ∅`. If all rules are evaluated, all failed rule IDs should be recorded.

**Algorithm 3 boundary (extended by design interpretation):** `validate_rule_set()` catches rule-definition failures — unknown variable references (F-T-11), type mismatches (F-T-04), invalid operators (F-T-05), unsupported categorical values (F-T-06) — before reasoning begins, producing `ConfigurationError` with `configuration_failure = True`. These are not governed by this policy. Variable existence (F-T-11) is checked before type compatibility (F-T-04): an unknown variable has no declared type to check. See `data/journal1-layer3-prototype/open-l3-2-resolution/failure-taxonomy.csv` for the full four-class taxonomy.

**Algorithm 4 boundary:** Failures that depend on runtime context values (runtime predicate exceptions, numeric conversion failures, malformed values, unexpected internal errors) are caught by `engine.reason()` under this policy.

**Trace distinguishability requirement:** `fired_rule_ids = []` combined with `evaluation_failure = False` means normal no-fire. `fired_rule_ids = []` combined with `evaluation_failure = True` means the episode was aborted by predicate failure. These states must be distinguishable without inspecting any other field. The FidelityTrace requires three additional conceptual fields: `evaluation_failure` (bool), `failed_rule_ids` (list[str]), `failure_category` (str | None). Implementation is Batch 3 work.

**S mutation policy:** S is never mutated by Layer 3. A predicate evaluation failure does not change S, G(S), or A_AI(S). The policy does not map evaluation failure to `S = UNSAFE`.

**Unconfigured vessel category:**

Per `appendix-c-formalisation.md` C.2.0.6, unconfigured `v` is a startup precondition failure, not a classification. If `context.vessel_category` is absent or unrecognised, `execute_episode()` raises `ConfigurationError` before any reasoning begins.

---

## 13. Human-authority boundary

The prototype must not introduce any of the following:

- Automatic approval of departure
- Automatic prohibition of departure
- Automatic override of a human decision
- Encoding of the Human Decision as a field on any output object

**A `Go` advisory is not a departure approval.** It is an AI-generated recommendation within the admissible scope for the governing state. The human fisher retains unconditional authority over the departure decision.

**An empty advisory list is not a prohibition.** It means no rule in the active RS(S) fired for the current conditions — it says nothing about whether departure is safe or permitted.

**UNSAFE state does not generate an advisory.** When `G(UNSAFE) = 0`, `AI(E) = ∅`. The prototype does not generate any output that reads "Do Not Go", "Cancel", "Return Home", or "Stay Ashore". State reporting (communicating that the current state is UNSAFE) is outside `AI(E)` and belongs to a separate system layer not specified here.

---

## 14. OPEN implementation decisions

The following items are carried forward from the Algorithm Specification workstream. Status updates where applicable.

| ID | Item | Status | Action this batch |
|---|---|---|---|
| OPEN-B1-1 | Freshness parameters `age_i` | OPEN — unchanged | None |
| OPEN-B1-2 | Runtime provenance capture (`reasons`) | OPEN — unchanged | None |
| OPEN-B1-3 | Medium vessel evidence limitation | OPEN — unchanged | None |
| OPEN-B1-4 | Layer 3 concrete rule contents | OPEN — superseded by OPEN-L3-1 | Replaced by the more specific OPEN-L3-1 |
| OPEN-B1-5 | Live `g_m` configuration | OPEN — unchanged | None |
| OPEN-B1-6 | Latency acceptance threshold H3 | OPEN — unchanged | None |
| OPEN-B1-7 | Decision-support utility construct | OPEN — unchanged | None |
| OPEN-B1-8 | State/rule-set consistency concurrency mechanism | OPEN — interface defined, primitive not chosen | Interface permits later concurrency enforcement without API change |
| OPEN-B3-1 | Invalid repository runtime handling | **PARTIALLY CLOSED — implementation handling chosen** | ConfigurationError; disable episode; surface to caller. Scientific state model unchanged. |
| OPEN-B3-2 | Rule engine evaluation strategy | **PARTIALLY CLOSED — linear scan for prototype** | Linear scan O(k_S × c). Production strategy remains OPEN. |
| OPEN-B3-3 | Decision-episode implementation boundary | **PARTIALLY CLOSED — ReasoningEpisode struct defined** | One episode = one `execute_episode()` call. Duration/polling/refresh not specified. |
| OPEN-B4-1 | Solar lookup data structure | OPEN — unchanged | Layer 3 does not modify Algorithm 1 infrastructure |
| OPEN-L3-1 | **Concrete Layer 3 advisory rule content** | **Batch 1 historical status: OPEN. Current status: PARTIALLY RESOLVED — see §26 (authoritative).** | No authoritative rule antecedents found in upstream authority. Engine contract and interface complete. Scientific specification of rule content required before concrete rules can be added. |
| OPEN-L3-2 | **Rule-condition evaluation failure handling** | **CLOSED (2026-09-11) — Model C + Model D selected: three-valued semantics `{TRUE, FALSE, ERROR}` with episode-level refusal. Any predicate `ERROR` → `AI(E) = ∅`; `S` unchanged; `evaluation_failure = True` in trace. FidelityTrace extended with `evaluation_failure`, `failed_rule_ids`, `failure_category` (conceptual — implementation is Batch 3). Full evidence: `data/journal1-layer3-prototype/open-l3-2-resolution/`.** | See §12 resolved policy. OPEN-L3-2 no longer blocks engine implementation. |

**OPEN-L3-1 and OPEN-L3-2:** OPEN-L3-1C and OPEN-L3-1D block concrete rule content for DepartureTime and Duration. OPEN-L3-2 is now CLOSED. The engine contract, interface, schema, and fidelity instrumentation are complete. Full prototype implementation is gated by OPEN-L3-1C and OPEN-L3-1D independently.

---

## 15. Batch 1 implementation traceability

| Batch 1 deliverable | Where defined | Status |
|---|---|---|
| Executable Layer 3 prototype boundary | §3 (module map); §§8–9 (Algorithm 3+4 interface) | DEFINED |
| Concrete representation of RS(SAFE) and RS(CAUTION) | §5 (rule-set representation) | DEFINED — content OPEN-L3-1 |
| Rule object / schema | §4 + `rule-schema-batch1.json` | DEFINED |
| Decision-episode execution interface | §9 (`execute_episode`; `ReasoningEpisode`) | DEFINED |
| State-to-rule-set supply interface | §8 (`select_rule_set`; `validate_rule_set`) | DEFINED |
| Recommendation output representation | §6 (`Advisory` dataclass) | DEFINED |
| F1–F3 fidelity instrumentation | §11 + `fidelity-instrumentation-batch1.csv` | DESIGNED — NOT YET TESTED |
| Implementation decisions closable without changing architecture | §§9.3–9.4, §10, §12, §14 | DOCUMENTED |

**Algorithm 3 correspondence:** `rule_set_provider.py` — `select_rule_set()` + `validate_rule_set()` — implements the pre-reasoning supply and compliance check from `algorithm-specification.md` §17.

**Algorithm 4 correspondence:** `reasoning_engine.py` — `reason()` — implements the gate-off check and rule firing from `algorithm-specification.md` §19.

**Safety Dominance dependency chain preserved:**

- L1 (definition of A_AI): `GovernanceConfig.A_AI` holds the exact admissible set per state
- L2 (Algorithm 3 algorithmic contract): `validate_rule_set()` enforces `ConclusionTypes(RS) ⊆ A_AI(S)` before supply
- L3 (engine fidelity assumption): `reasoning_engine.reason()` fires only rules in the supplied RS(S); engine cannot generate types not represented in the rule set
- L4 (formal theorem): Theorem C.3 in `appendix-c-formalisation.md` C.7.2 — Safety Dominance holds for both the ideal form `f(E)` and the operational form `F_{D,τ}`

---

*Author: iskandar · Date: 2026-09-11 · Branch: `feat/journal1-layer3-prototype`*

---

## 16. Batch 2 scientific rule-specification scope

Batch 2 determined which advisory rules can be scientifically defended for inclusion in RS(SAFE) and RS(CAUTION). It was not an implementation task and produced no engine code.

The core distinction is between architectural permission and scientific justification:

- `A_AI(S)` defines what the AI is **permitted** to recommend under state S — a governance-layer constraint
- `RS(S)` defines what the evidence **warrants** the AI to recommend under specific environmental conditions — a scientific constraint

Permission is necessary but not sufficient. A recommendation type in A_AI(S) may still be absent from RS(S) if no defensible evidence supports a specific antecedent condition for it.

**This batch explicitly excluded:**

- Engine implementation or code generation
- F1–F3 fidelity test execution
- E5 performance benchmarking
- Invention of advisory rules to make the repository look complete
- Conversion of Layer 2 classification thresholds to Layer 3 rules without independent justification
- ~~Resolution of OPEN-L3-2~~ (OPEN-L3-2 was resolved 2026-09-11 — see §12 and §14)

**Artefacts produced:** `recommendation-semantics-batch2.csv`, `rule-evidence-matrix-batch2.csv`, `rule-candidate-register-batch2.csv`, `rule-conflict-analysis-batch2.csv`, `scientific-gap-register-batch2.csv`, `semantic-verification-batch2.json`, `change-map-batch2.csv`, `closure-batch2.json`, `report-batch2.md`.

---

## 17. Recommendation semantics

The four types in R = {Go, Delay, DepartureTime, Duration} carry the following advisory meanings, derived from `appendix-c-formalisation.md` Section C.4:

| Type | Meaning | What it does NOT mean |
|---|---|---|
| **Go** | No configured advisory trigger requiring an alternative recommendation was identified within the active rule set | Safe to depart; approved to depart; permission to depart; risk-free conditions |
| **Delay** | Recommend deferring departure pending improvement in the identified adverse condition | Departure is prohibited; fisher must not go; conditions are physically unsafe per MET classification |
| **DepartureTime** | Recommended departure window or time — **OPEN** | Guaranteed safe departure time; Layer 2 g_t SAFE onset (sunrise) reinterpreted as optimal time |
| **Duration** | Recommended safe trip duration — **OPEN** | Maximum permitted duration; a daylight-window fill |

**Go does not mean permission.** The Go recommendation reports that the rule system found no adverse condition in its current scope — it does not override the fisher's judgment or confer approval. Human authority over the departure decision is unconditional.

**Delay does not mean prohibition.** The Delay recommendation is an advisory; the fisher remains free to depart. The recommendation conveys that a specific environmental condition has been identified as warranting caution.

**DepartureTime and Duration payload fields are OPEN.** No scientific authority was identified in the repository for specifying these payloads. Both are explicitly deferred to RQ5 fieldwork in `dataset-label-derivation.md` Section 6.3.

---

## 18. Evidence hierarchy

Five evidence levels were defined for assessing candidate rules. The hierarchy appears in full in `rule-evidence-matrix-batch2.csv`.

| Level | Description | Examples |
|---|---|---|
| **A** | Direct normative or operational authority | MET Malaysia marine warning criteria, Department of Fisheries operational guidelines, IMO instruments |
| **B** | Direct empirical evidence from small-scale fisheries peer-reviewed literature at the study site or closely matched context | (No Level B evidence identified for this deployment site) |
| **C** | Strong domain evidence requiring bounded geographic or vessel-type adaptation to reach Kota Kinabalu Zone A fishers | Empirical fisher behavioral studies from Indonesia, Peninsular Malaysia, Korea, Turkey |
| **D** | Architecture or design interpretation; definitional only | appendix-c-formalisation.md formal semantic definitions |
| **UNSUPPORTED** | No defensible mapping between evidence and advisory content | State restatement, threshold reuse without independent grounding |

No Level B evidence was identified — a genuine gap in the Sabah coastal fisheries literature, not a search failure.

---

## 19. Evidence sources

Nine evidence sources (EV-01 through EV-09) are documented in full in `rule-evidence-matrix-batch2.csv`. The three most consequential:

**EV-01 — MET Malaysia Category 1 warning** (Level A). MET Malaysia's Kawasan Perairan bulletin explicitly describes Category 1 conditions as "berbahaya kepada bot-bot kecil" (dangerous to small boats). This is the only Level A evidence in the repository and directly justifies R-CAUTION-001.

**EV-08 — dataset-label-derivation.md** (internal synthesis, not an independent empirical source). This document synthesizes three underlying empirical studies — Rahim et al. 2024 [[notes]](../../../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) (EV-02), Gao 2024 [[notes]](../../../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md) (EV-03), Yamin et al. 2025 [[notes]](../../../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia.md) (EV-04) — into Go/Delay label logic for the ML training dataset. It is not a fourth independent empirical source: any claim attributable to EV-08 reduces to claims from EV-02, EV-03, or EV-04. Section 4 maps SAFE conditions to Go labels and CAUTION conditions (four antecedent types) to Delay labels. Section 6.3 explicitly defers DepartureTime and Duration to RQ5 fieldwork.

**EV-06 — Yaakob et al. (2015)** [[notes]](../../../notes/Stability%2C%20Seakeeping%20and%20Safety%20Assessment%20of%20Small%20Fishing%20Boats%20Operating%20in%20Southern%20Coast%20of%20Peninsular%20Malaysia.md) (Level C). The only peer-reviewed naval architecture study of actual Malaysian small fishing vessels in the repository. Two Zone A boats from Johor: operational ceilings approximately 1.25m (Boat A, 6.54m LOA) and 0.5m (Boat B, 5.03m LOA). Relevant to the CAUTION band for small vessels (1.0–1.25m).

---

## 20. SAFE rule candidates

One candidate rule was derived for RS_candidate(SAFE):

**R-SAFE-001**

```
IF  g_w(w) == SAFE
AND g_r(r, κ) == SAFE
AND g_m(m) == SAFE
AND g_o(o, v) == SAFE
AND g_t(t, date) == SAFE
THEN Go
```

| Field | Value |
|---|---|
| Status | CONDITIONALLY SUPPORTED |
| Evidence level | Level C |
| Primary evidence | EV-02, EV-03, EV-04 (EV-08 is an internal synthesis of these three — not an independent source) |
| Classifier duplication | MODERATE — antecedent is functionally equivalent to S == SAFE; independently grounded in three empirical studies |
| Governance admissible | STRUCTURAL CHECK — PASS (Go ∈ A_AI(SAFE)) |
| Adaptation required | Geographic adaptation from Indonesia, Penang, Terengganu to Kota Kinabalu |

**Rejected — R-REJ-001:** "IF S == SAFE THEN Go" — rejected because it has no empirical basis beyond architectural permission. R-SAFE-001 differs in having three empirical studies documenting fisher Go behavior under SAFE-equivalent conditions.

---

## 21. CAUTION rule candidates

Four candidate rules were derived for RS_candidate(CAUTION):

**R-CAUTION-001** — strongest environmental-premise authority (P_ENV Level A; P_ADV Level C inferred)

```
IF m == advisory
THEN Delay  [reason: MET Malaysia Category 1 marine warning active]
```

| Field | Value |
|---|---|
| Status | CONDITIONALLY SUPPORTED |
| Evidence level | Level A (P_ENV); Level C (P_ADV — inferred) |
| Primary evidence | EV-01 (MET Malaysia Category 1 = "berbahaya kepada bot-bot kecil") |
| Adaptation required | MINIMAL — MET Malaysia applies to Malaysian waters including Sabah |
| Governance admissible | STRUCTURAL CHECK — PASS (Delay ∈ A_AI(CAUTION)) |

**R-CAUTION-002**

```
IF g_o(o, v) == CAUTION
THEN Delay  [reason: wave height in CAUTION range for vessel category]
```

| Field | Value |
|---|---|
| Status | CONDITIONALLY SUPPORTED |
| Evidence level | Level C |
| Primary evidence | EV-05 (Jeong & Im 2023), EV-06 (Yaakob et al. 2015) |
| Adaptation required | Korean/Johor vessel geometry to Sabah small vessels |
| Governance admissible | STRUCTURAL CHECK — PASS |

**R-CAUTION-003**

```
IF g_r(r, κ) == CAUTION
THEN Delay  [reason: heavy rainfall in CAUTION range]
```

| Field | Value |
|---|---|
| Status | CONDITIONALLY SUPPORTED |
| Evidence level | Level C |
| Primary evidence | EV-02 (Rahim et al. 2024 East season) |
| Adaptation required | Indonesian coastal to Kota Kinabalu |
| Governance admissible | STRUCTURAL CHECK — PASS |

**R-CAUTION-004**

```
IF g_w(w) == CAUTION
THEN Delay  [reason: sustained wind in CAUTION range]
```

| Field | Value |
|---|---|
| Status | CONDITIONALLY SUPPORTED |
| Evidence level | Level C |
| Primary evidence | EV-03 (Gao 2024), EV-07 (Atacan & Düzbastılar 2023) |
| Adaptation required | Turkish Mediterranean and Penang to Kota Kinabalu |
| Governance admissible | STRUCTURAL CHECK — PASS |

**Rejected CAUTION candidates:**

- **R-REJ-002** — "IF S == CAUTION THEN Delay" — state restatement, no specific antecedent
- **R-REJ-003** — wave > CAUTION threshold in SAFE state — structurally impossible (antecedent implies CAUTION, not SAFE)

---

## 22. Rule interaction and conflict analysis

Seven conflict scenarios were assessed in `rule-conflict-analysis-batch2.csv`. No conclusion-type contradiction was identified in the current candidate rule set. Note: when multiple CAUTION rules fire simultaneously, all conclude Delay — no type-level conflict occurs. Advisory aggregation policy (which Delay explanation to surface first) is an implementation-level concern, not a scientific conflict in the current candidate set.

**Compatible — multiple Delay rules (CONF-002, CONF-003, CONF-004):** When multiple CAUTION conditions hold simultaneously, multiple Delay rules fire. All produce Delay conclusion type with distinct explanations. The engine should collect all fired rules and return all generated advisories. Multiple Delay advisories with different rule_ids give the fisher more information about which conditions are adverse.

**No Go + Delay conflict in current design (CONF-001, CONF-006):** RS_candidate(SAFE) contains only a Go rule; RS_candidate(CAUTION) contains only Delay rules. Cross-state conflict is architecturally impossible — each episode uses exactly one RS(S).

**Future boundary condition (CONF-005):** If a Delay rule is added to RS(SAFE) for any reason, a Go + Delay conflict within the same episode becomes possible. An advisory conflict policy would then be required. Not currently needed.

---

## 23. Payload semantics

The payload fields supported at Batch 2 closure:

| Type | Supported payload fields | Open payload fields |
|---|---|---|
| Go | reason (brief explanation of rule scope — "No adverse condition identified in current advisory scope") | departure_time, location, duration |
| Delay | reason (specific adverse condition: e.g. "MET Category 1 marine warning active"; "wave height 1.2m exceeds small vessel CAUTION onset") | recommended_wait_time, predicted_window |
| DepartureTime | (none) | all — OPEN-L3-1C |
| Duration | (none) | all — OPEN-L3-1D |

The reason field for Go and Delay is the only payload field with scientific grounding at this stage. All other payload fields require domain evidence not currently in the repository.

---

## 24. Concrete rule register summary

Full register: `rule-candidate-register-batch2.csv`.

| Rule ID | State | Antecedent | Conclusion | Status | Level |
|---|---|---|---|---|---|
| R-SAFE-001 | SAFE | All components in SAFE band | Go | CONDITIONALLY SUPPORTED | C |
| R-CAUTION-001 | CAUTION | m == advisory | Delay | CONDITIONALLY SUPPORTED | A (P_ENV); C (P_ADV) |
| R-CAUTION-002 | CAUTION | g_o(o, v) == CAUTION | Delay | CONDITIONALLY SUPPORTED | C |
| R-CAUTION-003 | CAUTION | g_r(r, κ) == CAUTION | Delay | CONDITIONALLY SUPPORTED | C |
| R-CAUTION-004 | CAUTION | g_w(w) == CAUTION | Delay | CONDITIONALLY SUPPORTED | C |
| R-REJ-001 | — | S == SAFE | Go | REJECTED | — |
| R-REJ-002 | — | S == CAUTION | Delay | REJECTED | — |
| R-REJ-003 | — | wave > CAUTION threshold in SAFE | Delay | REJECTED | — |
| R-REJ-004 | — | sunrise | DepartureTime | REJECTED | — |
| R-REJ-005 | — | sunset - departure | Duration | REJECTED | — |

**RS_candidate(SAFE)** = {R-SAFE-001}  
**RS_candidate(CAUTION)** = {R-CAUTION-001, R-CAUTION-002, R-CAUTION-003, R-CAUTION-004}  
**RS_candidate(UNSAFE)** = ∅

---

## 25. Evidence gaps

Full gap register: `scientific-gap-register-batch2.csv`.

| Gap | Type | What is missing | Successor |
|---|---|---|---|
| GAP-01 | DepartureTime | No authority for departure time recommendation to Zone A Kota Kinabalu fishers. Tide-gating evidence (Gao 2024) suggests timing is tide-conditioned and port-specific. Tide not in E. | OPEN-L3-1C |
| GAP-02 | Duration | No authority for trip duration recommendation under SAFE conditions. Duration evidence in repository is from UNSAFE-equivalent conditions when Layer 3 does not operate. | OPEN-L3-1D |
| GAP-03 | Go (CAUTION) | All three behavioral studies map CAUTION-equivalent conditions to Delay analog. No Go evidence under CAUTION. Tension with appendix-c line 791 — statement classified as B (UI/presentation guidance) but "automatically presented" wording is ambiguous with a normative reading. | OPEN-L3-3 |
| GAP-04 | Delay (sub-SAFE) | No evidence for Delay advisory within SAFE state below the CAUTION boundary. | (No new open item) |
| GAP-05 | All types | Marine warning archive absent for study site — R-CAUTION-001 cannot be tested on replay. All m-driven rates are lower bounds. | (Existing m data gap) |

---

## 26. Open scientific decisions after Batch 2

| Item | Status | Description |
|---|---|---|
| OPEN-L3-1C | OPEN | DepartureTime advisory derivation — requires RQ5 fieldwork or tidal data for Kota Kinabalu |
| OPEN-L3-1D | OPEN | Duration advisory derivation — requires RQ5 fieldwork or DoF Malaysia guidelines |
| OPEN-L3-2 | **CLOSED (2026-09-11) — three-valued semantics with episode-level refusal** | Full policy in §12; evidence in `data/journal1-layer3-prototype/open-l3-2-resolution/`. OPEN-L3-2 no longer gates engine implementation. |
| OPEN-L3-3 | **CLOSED (2026-09-11) — Resolution B** | **CAUTION-Go presentation vs. rule semantics — RESOLVED.** Interpretation B (presentation qualifier only) established. Formal semantics: `S = CAUTION ∧ Go ∈ AI(E) → Present(Go, caution_qualifier)`. NOT: `S = CAUTION → Go ∈ AI(E)`. Appendix C §C.4 line 791 clarified under task §15 permission to remove the "automatically presented" surface ambiguity: the sentence now reads "any Go advisory generated by the active Layer 3 rule set is presented with a caution qualifier." No CAUTION-Go rule required or introduced; Go remains admissible in A_AI(CAUTION). Algorithm 3/4 unchanged; Safety Dominance unchanged. Full evidence: [`data/journal1-layer3-prototype/open-l3-3-resolution/`](../../../data/journal1-layer3-prototype/open-l3-3-resolution/) (authority-trace.csv, semantic-decomposition.md, decision-matrix.csv, resolution.json, verification.json, report.md). Does not authorise Batch 3 engine implementation; other Batch 3 gating conditions (OPEN-L3-1C, OPEN-L3-1D, OPEN-L3-2) remain in force. |

OPEN-L3-1 is PARTIALLY RESOLVED. OPEN-L3-1C and OPEN-L3-1D carry the unresolved portions forward. **OPEN-L3-3 is CLOSED (Resolution B, 2026-09-11).** **OPEN-L3-2 is CLOSED (2026-09-11) — three-valued semantics with episode-level refusal; see §12.** Batch 3 engine implementation is unblocked on the OPEN-L3-3 and OPEN-L3-2 axes; remaining gating comes from OPEN-L3-1C and OPEN-L3-1D independently. Presentation layer must attach a caution qualifier to any Go advisory produced when S = CAUTION.

---

## 27. Batch 2 traceability

| Batch 2 deliverable | Where defined | Status |
|---|---|---|
| Recommendation semantics | §17; `recommendation-semantics-batch2.csv` | DEFINED — DepartureTime/Duration OPEN |
| Evidence hierarchy | §18; `rule-evidence-matrix-batch2.csv` | DEFINED |
| Evidence sources (EV-01–EV-09) | §19; `rule-evidence-matrix-batch2.csv` | DOCUMENTED |
| SAFE candidate rules | §20; `rule-candidate-register-batch2.csv` | CONDITIONALLY SUPPORTED (R-SAFE-001) |
| CAUTION candidate rules | §21; `rule-candidate-register-batch2.csv` | CONDITIONALLY SUPPORTED (R-CAUTION-001–004; R-CAUTION-001 P_ENV Level A, P_ADV Level C inferred) |
| Rejected candidates | §§20–21; `rule-candidate-register-batch2.csv` | DOCUMENTED (R-REJ-001–005) |
| Conflict analysis | §22; `rule-conflict-analysis-batch2.csv` | COMPLETE — no conclusion-type contradiction identified in current candidate set |
| Payload semantics | §23; `recommendation-semantics-batch2.csv` | reason field defined; DepartureTime/Duration OPEN |
| Evidence gaps | §25; `scientific-gap-register-batch2.csv` | REGISTERED (GAP-01–GAP-05) |
| Open scientific decisions | §26; `closure-batch2.json` | DOCUMENTED |
| Semantic verification | `semantic-verification-batch2.json` | 90 PASS / 0 FAIL / 0 OPEN — 90 checks total (OPEN-L3-3 tracking check → PASS after Resolution B, 2026-09-11) |

**Safety Dominance preserved through Batch 2:**

All five candidate rules have conclusion types within A_AI(S) for their applicable state. No rule targets UNSAFE. The structural check confirms that each accepted candidate's conclusion_type satisfies the admissibility precondition of Theorem C.3 at specification level — it verifies the construction is correct for these candidates, not that Theorem C.3 itself is verified here. The theorem holds by construction of RS(S); its proof is in `appendix-c-formalisation.md` C.7.2.

---

*Author: iskandar · Batch 2 added: 2026-09-11 · Branch: `design/journal1-algorithm-specification`*
