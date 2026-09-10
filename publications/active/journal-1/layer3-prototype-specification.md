# Journal 1 — Layer 3 Prototype Specification

**Status:** Batch 1 CLOSED — fidelity trace and failure-semantics contract repaired (2026-09-11)  
**Closed on:** 2026-09-11  
**Branch:** `feat/journal1-layer3-prototype`  
**Task:** [`docs/tasks/Journal 1 Layer 3 Prototype Implementation batch 1.md`](../../../docs/tasks/Journal%201%20Layer%203%20Prototype%20Implementation%20batch%201.md)  
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

**Rule condition evaluation error (OPEN-L3-2):**

If a rule predicate cannot be evaluated correctly, the prototype must not silently reinterpret the failure as a false predicate. A predicate evaluation failure is not equivalent to `condition == False`.

Until OPEN-L3-2 is resolved, the only permitted specification behaviour is:

```
predicate evaluation raises an exception
→ episode reports an evaluation failure
→ no unsupported advisory is emitted from the failed evaluation
```

Whether the engine aborts, skips the rule, continues evaluating remaining rules, returns partial advisories, or returns an error result are **implementation-policy choices** not yet resolved. See OPEN-L3-2 in §14.

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
| OPEN-L3-1 | **Concrete Layer 3 advisory rule content** | **NEW — OPEN** | No authoritative rule antecedents found in upstream authority. Engine contract and interface complete. Scientific specification of rule content required before concrete rules can be added. |
| OPEN-L3-2 | **Rule-condition evaluation failure handling** | **NEW — OPEN** | If a predicate cannot be evaluated, the failure must not be silently treated as `False`. Implementation policy (abort / skip / continue / partial advisories / error result) is not yet resolved. Blocks concrete engine implementation but not Batch 1 contract closure. |

**OPEN-L3-1 and OPEN-L3-2 do not block Batch 1 closure** — the engine contract, interface, schema, and fidelity instrumentation are complete without concrete rules. It blocks full prototype completion (Batch 2 and later).

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
