# Batch 3 — Governed Core Engine: Closure Report

**Date:** 2026-09-11
**Branch:** feat/journal1-layer3-core-engine
**HEAD before:** 3983f9875726e0b14ab8f2fcc197004c1ae9be27

---

## 1. Verdict

**JOURNAL 1 LAYER 3 PROTOTYPE BATCH 3 CLOSED —
GOVERNED CORE ENGINE AND FAILURE CONTRACT IMPLEMENTED**

---

## 2. Authorities Inspected

| Document | Purpose |
|---|---|
| `publications/active/journal-1/layer3-prototype-specification.md` | Layer 3 module schemas, Algorithm 3 interface, FidelityTrace, DecisionContext, scientific rule candidates (§4–§11, §20–§26) |
| `publications/active/journal-1/algorithm-specification.md` | Algorithm 3 pseudocode (§17), Algorithm 4 pseudocode (§19) |
| `data/journal1-layer3-prototype/closure-batch2.json` | Closed Batch 2 rule register — RS_candidate_at_closure |
| `docs/canonical/appendix-c-formalisation.md` | Formal variable definitions, Safety Dominance Property |
| `docs/canonical/architecture-illustration.md` | Architecture walkthrough, Layer 3 enforcement mechanism |

---

## 3. Files Created

### Implementation

| File | Module |
|---|---|
| `governance/__init__.py` | Package initialiser |
| `governance/rule.py` | ConfigurationError, ConditionPredicate, Rule |
| `governance/advisory.py` | Advisory |
| `governance/fidelity_trace.py` | FidelityTrace |
| `governance/rule_repository.py` | RuleRepository |
| `governance/rule_set_provider.py` | GovernanceConfig, GOVERNANCE_MAP, select_rule_set, validate_rule_set |
| `governance/reasoning_engine.py` | PredicateResult, FailureCategory, evaluate_predicate, ReasoningEngine (Algorithm 4) |
| `governance/reasoning_episode.py` | DecisionContext, EpisodeResult, execute_episode (Algorithm 3 orchestration) |
| `governance/canonical_rules.py` | DEFERRED_RULES, build_canonical_repository |

### Tests

| File | Contents |
|---|---|
| `tests/__init__.py` | Package marker |
| `tests/test_governance_engine.py` | 82 engineering tests (T01–T25 + supporting) |

### Evidence

| File | Contents |
|---|---|
| `data/journal1-layer3-prototype/batch3-core-engine/implementation-manifest.json` | Branch, HEAD, file list, rule IDs, OPEN items |
| `data/journal1-layer3-prototype/batch3-core-engine/test-results.json` | 82 test names and pass/fail status |
| `data/journal1-layer3-prototype/batch3-core-engine/contract-verification.json` | 28 contract checks (26 PASS, 0 FAIL, 2 OPEN) |
| `data/journal1-layer3-prototype/batch3-core-engine/report.md` | This report |

---

## 4. Module Implementation Summary

### governance/rule.py
- `ConfigurationError`: structured exception carrying `failure_type`, `episode_id`, `state`, `offending_rules`, `offending_predicates`
- `ConditionPredicate`: frozen dataclass `(variable, operator, value)` — the predicate atom
- `Rule`: frozen dataclass with `__post_init__` validation; enforces `applicable_state ∈ {SAFE, CAUTION}`, `conclusion_type ∈ {Go, Delay, DepartureTime, Duration}`, non-empty provenance, tuple conditions

### governance/advisory.py
- `Advisory`: frozen dataclass `(type, payload, rule_id, explanation)` — no human-authority fields

### governance/fidelity_trace.py
- `FidelityTrace`: mutable dataclass with all fields specified in layer3-prototype-specification.md §11 plus OPEN-L3-2 additions: `evaluation_failure`, `failed_rule_ids`, `failure_category`

### governance/rule_repository.py
- `RuleRepository`: insert-and-list store; `insert()` enforces `Rule` type; `rules` property returns copy

### governance/rule_set_provider.py
- `GOVERNANCE_MAP`: maps SAFE/CAUTION/UNSAFE → `GovernanceConfig(G, A_AI)`; UNSAFE has G=0, A_AI=∅
- `DECISION_CONTEXT_SCHEMA`: declares type, nullability, and categorical domain for each DecisionContext field — used by V1–V4
- `get_governance_config()`: raises ConfigurationError on unknown state
- `select_rule_set()`: returns [] for UNSAFE immediately; filters by `applicable_state == state` and `enabled == True`
- `validate_rule_set()`: enforces A_AI containment + V1–V4 in order; V1 (unknown variable) before V2 (type mismatch)

### governance/reasoning_engine.py
- `PredicateResult`: three-valued enum `{TRUE, FALSE, ERROR}` — ERROR ≠ FALSE ≠ TRUE
- `FailureCategory`: `{PREDICATE_EXCEPTION, NUMERIC_CONVERSION_FAILURE, MALFORMED_VALUE, INTERNAL_ERROR}`
- `evaluate_predicate()`: handles null operators, None-actual guard (ordering operators only — `None == x` is valid Python and returns FALSE), membership, comparison, unknown operator
- `ReasoningEngine.reason()`: Model B collect-all-errors; Model C+D episode refusal on any ERROR

### governance/reasoning_episode.py
- `DecisionContext`: resolved environmental state with all canonical fields
- `EpisodeResult`: `(advisories, trace, error)` — trace always present
- `execute_episode()`: nine-step Algorithm 3 + Algorithm 4 orchestration; `_engine` parameter for structural test injection

### governance/canonical_rules.py
- `DEFERRED_RULES`: dict with reason and authority gap for R-SAFE-001, R-CAUTION-002/003/004
- `build_canonical_repository()`: loads only R-CAUTION-001

---

## 5. Algorithm 3 Implementation

Implemented in `governance/rule_set_provider.py` (steps 1–5) and `governance/reasoning_episode.py` (`execute_episode` steps 1–9):

1. Establish governance configuration from state
2. If G(S) = 0 (UNSAFE): return EpisodeResult(advisories=[], ...) — no reasoning, no RS
3. Select RS_candidate(S): filter by applicable_state + enabled
4. Validate RS_candidate: A_AI containment + V1–V4 structural checks
5. Supply RS(S) = validated RS_candidate
6. engine.reason(context, RS(S))
7. Produce AI(E) from reason result
8. Emit FidelityTrace
9. Return EpisodeResult

---

## 6. V1–V4 Validation

| Check | Failure Type | Implementation |
|---|---|---|
| V1: unknown variable | F-T-11 | `pred.variable not in DECISION_CONTEXT_SCHEMA` |
| V2: type mismatch | F-T-04 | `pred.value type ≠ declared kind` in schema (plus null-operator + non-None value guard) |
| V3: invalid operator | F-T-05 | `pred.operator not in VALID_OPERATORS` |
| V4: categorical value out of domain | F-T-06 | `schema[var]['domain'] is not None and pred.value not in domain` |

V1 runs before V2 — an unknown variable has no declared type to check.

---

## 7. Algorithm 4 Implementation

Linear scan in `ReasoningEngine.reason()`:

- For each rule in RS(S): evaluate conditions conjunctively
- All TRUE → fire rule, emit Advisory
- Any FALSE → normal no-fire (continue)
- Any ERROR → mark rule failed (Model B: collect all), continue
- After full scan: any failed rules → evaluation_failure=True, AI(E)=∅ (Model C+D)

Complexity: O(k_S × c) where k_S = |RS(S)|, c = avg conditions/rule.

---

## 8. Predicate TRUE / FALSE / ERROR Implementation

```
is_none, is_not_none   → TRUE/FALSE based on actual is None
None + ordering op     → ERROR (MALFORMED_VALUE, F-T-09)
None + ==, in, not_in  → comparison proceeds; None == "x" → FALSE (valid Python)
in, not_in             → membership test; TypeError → PREDICATE_EXCEPTION
comparison (<,<=,==,>=,>) → boolean result; TypeError → NUMERIC_CONVERSION_FAILURE (F-T-08)
unknown operator        → INTERNAL_ERROR (F-T-10)
AttributeError on getattr → INTERNAL_ERROR (F-T-10)
```

---

## 9. Model C+D Failure Handling

- Model B across rules: collect all ERROR-producing rules before refusing
- Model C+D refusal: any ERROR → `evaluation_failure=True`, `advisories=[]`, `fired_rule_ids=[]`
- Configuration failure (`configuration_failure=True`) is distinct from evaluation failure (`evaluation_failure=True`)
- Partial advisory output is impossible under Model C+D — all or nothing

---

## 10. UNSAFE Short-Circuit

- Step 2 of `execute_episode()`: if `gov_config.G == 0` → return immediately with empty advisories and trace
- `engine.reason()` is NOT called
- Verified structurally by `_SpyEngine` injection in T04

---

## 11. Rule Loading Status

| Rule ID | Status | Reason |
|---|---|---|
| R-CAUTION-001 | IMPLEMENTED | `resolved_m == "advisory"` directly expressible as ConditionPredicate |
| R-SAFE-001 | DEFERRED | g_t solar lookup prohibited in Layer 3; antecedent not in ConditionPredicate form |
| R-CAUTION-002 | DEFERRED | g_o(o,v)==CAUTION requires vessel-dependent predicate decomposition not in Batch 2 artefacts |
| R-CAUTION-003 | DEFERRED | g_r(r,κ)==CAUTION expressed as shorthand only; ConditionPredicate not in Batch 2 artefacts |
| R-CAUTION-004 | DEFERRED | g_w(w)==CAUTION expressed as shorthand only; ConditionPredicate not in Batch 2 artefacts |

Note: R-CAUTION-001 will produce zero activations in the retrospective replay because `m ∈ D` (no marine warning archive for study site). The rule is structurally correct; zero activation is the expected lower-bound result per GAP-05.

---

## 12. Fidelity Trace

`FidelityTrace` fields implemented per layer3-prototype-specification.md §11 plus OPEN-L3-2 additions:

- Core: `episode_id`, `state`, `G`, `A_AI`, `active_rule_ids`, `active_rule_conclusion_types`, `fired_rule_ids`, `generated_advisory_types`, `configuration_failure`, `S_old`, `S_new`, `rule_set_bound_for_state`
- OPEN-L3-2: `evaluation_failure`, `failed_rule_ids`, `failure_category`

Trace is always populated — never None — even on UNSAFE gate-off or configuration failure.

---

## 13. Configuration vs Evaluation Failure

| Failure mode | Flag | Error object | When |
|---|---|---|---|
| Configuration failure | `trace.configuration_failure=True` | `EpisodeResult.error` is `ConfigurationError` | V1–V4, A_AI containment, unknown state |
| Evaluation failure | `trace.evaluation_failure=True` | `EpisodeResult.error=None` | Predicate ERROR during reasoning |
| Normal no-fire | both False | None | No rule matched |
| Normal success | both False | None | Rules fired, advisories produced |

---

## 14. OPEN-B3-2 Status

Production reasoning strategy (RETE, agenda priority, first-match, all-match, backward chaining) remains OPEN-B3-2. The linear scan prototype partially closes the implementation question for Batch 3 — it demonstrates the engine is implementable and correct. Production strategy is an engineering decision deferred to a future batch.

---

## 15. Automated Test Results

```
Ran 82 tests in 0.002s

OK
```

All 82 tests pass. 0 failures. 0 errors.

---

## 16. Contract Verification Summary

| Count | Status |
|---|---|
| 26 | PASS |
| 0 | FAIL |
| 2 | OPEN (F1–F3 not run, E5 not run — correct) |

---

## 17. Canonical Integrity

- `docs/canonical/appendix-c-formalisation.md` — unchanged; existence verified by test
- `docs/canonical/architecture-illustration.md` — unchanged; existence verified by test
- `publications/active/journal-1/layer3-prototype-specification.md` — read-only authority; not modified
- `publications/active/journal-1/algorithm-specification.md` — read-only authority; not modified
- `data/journal1-layer3-prototype/closure-batch2.json` — read-only authority; not modified

---

## 18. Protected OPEN Items

| Item | Status |
|---|---|
| OPEN-L3-1C (DepartureTime) | PRESERVED — no rule loaded, no authority |
| OPEN-L3-1D (Duration) | PRESERVED — no rule loaded, no authority |
| OPEN-L3-3 Resolution B | PRESERVED — Go ∈ A_AI(CAUTION); no rule produces Go under CAUTION |
| GAP-03 (Go under CAUTION) | PRESERVED — no rule invented without supporting evidence |
| OPEN-B3-2 (production strategy) | PRESERVED — linear scan is the prototype strategy only |

---

## 19. F1–F3 Not Run

Confirmed. No retrospective replay, comparative analysis, or statistical evaluation was executed. These are scientific evaluations belonging to future batches.

---

## 20. E5 Not Run

Confirmed. No user study protocol was activated.

---

## 21. Remaining Blockers

None. All Batch 3 closure criteria are satisfied.

---

## 22. Closure Line

**JOURNAL 1 LAYER 3 PROTOTYPE BATCH 3 CLOSED —
GOVERNED CORE ENGINE AND FAILURE CONTRACT IMPLEMENTED**
