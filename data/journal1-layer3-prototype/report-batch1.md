# Journal 1 Layer 3 Prototype — Batch 1 Report

**Batch:** Prototype Contract, Rule Representation, and Fidelity Testability  
**Branch:** `feat/journal1-layer3-prototype`  
**Date:** 2026-09-11  
**Closure:** CLOSED — Fidelity Trace and Failure-Semantics Contract Repaired

---

## Prototype boundary

**Layer 3 prototype scope:** receives `S` from the upstream classifier, selects and validates `RS(S)`, executes the rule engine, returns an `EpisodeResult` containing the advisory list, fidelity trace, and any error. Does not re-implement the classifier (`F_{D,τ} = f ∘ ρ_{D,τ}`) or the resolution map (`ρ_{D,τ}`). Does not make or encode the Human Decision.

**Explicitly out of scope:** the classifier (Layers 1–2), the human departure decision, concrete advisory rule content (OPEN-L3-1), F1–F3 fidelity results, E5 performance benchmarking.

---

## Module design

Seven Python modules in `governance/`:

| Module | File | Responsibility |
|---|---|---|
| rule | `governance/rule.py` | `Rule` dataclass; `ConditionPredicate` schema |
| advisory | `governance/advisory.py` | `Advisory` dataclass; `type ∈ A_AI(S)` invariant |
| rule_repository | `governance/rule_repository.py` | State-indexed rule collection; insert-time validation |
| rule_set_provider | `governance/rule_set_provider.py` | Algorithm 3: `select_rule_set()` + `validate_rule_set()` |
| reasoning_engine | `governance/reasoning_engine.py` | Algorithm 4: linear scan, evaluate conditions, fire rules |
| reasoning_episode | `governance/reasoning_episode.py` | `ReasoningEpisode` struct; `execute_episode()` → `EpisodeResult` |
| fidelity_trace | `governance/fidelity_trace.py` | `FidelityTrace` schema; `emit_fidelity_trace()` |

---

## Rule representation

```python
Rule(
    rule_id: str,
    applicable_state: str,      # "SAFE" or "CAUTION"
    conditions: tuple[ConditionPredicate, ...],
    conclusion_type: str,       # ∈ {"Go","Delay","DepartureTime","Duration"}
    conclusion_payload: dict,   # OPEN-L3-1
    provenance: str,
    enabled: bool,
)
```

**Conclusion type invariant:** enforced at schema level (rule object) and at supply time (`validate_rule_set()`). Any rule with `applicable_state="CAUTION"` must have `conclusion_type ∈ {"Go","Delay"}` — checked before reasoning begins.

Full JSON schema: `data/journal1-layer3-prototype/rule-schema-batch1.json`.

---

## Rule-set representation

| State | Representation |
|---|---|
| SAFE | State-indexed list: enabled rules with `applicable_state="SAFE"` |
| CAUTION | State-indexed list: enabled rules with `applicable_state="CAUTION"` |
| UNSAFE | Empty set — no rule object exists; UNSAFE path does not supply a rule set |

Algorithm 3 contract preserved: `select_rule_set()` → `validate_rule_set()` → supply to engine — in that order. No reasoning begins before validation.

---

## Reasoning episode

**`ReasoningEpisode{state, governance, rule_set, context}`** — all four fields from the same classification event.

**`execute_episode(state, repository, context) → EpisodeResult`**

```python
EpisodeResult(
    advisories: list[Advisory],  # empty on UNSAFE, failure, or no rules firing
    trace: FidelityTrace,        # always present — never None
    error: Exception | None,     # ConfigurationError or None
)
```

UNSAFE path: `G=0` → return `EpisodeResult(advisories=[], trace=..., error=None)` immediately. No rule set selected. No reasoning.

SAFE/CAUTION path: `G=1` → `select_rule_set()` → `validate_rule_set()` → `reason()` → `emit_fidelity_trace()` → `EpisodeResult`.

Configuration failure path: `validate_rule_set()` raises `ConfigurationError` → `EpisodeResult(advisories=[], trace=FidelityTrace(configuration_failure=True, ...), error=ConfigurationError(...))`. S is not modified.

This resolves the Batch 1 contradiction: `trace` is always obtainable; `error` is always observable; no advisory is emitted on failure.

---

## Recommendation representation

```python
Advisory(
    type: str,          # ∈ A_AI(S) — guaranteed by construction
    payload: dict,      # type-specific content — OPEN-L3-1
    rule_id: str,
    explanation: str,
)
```

Empty advisory list is valid. A `Go` advisory is not a departure approval. No automated prohibition is encoded.

---

## Engine strategy

**Linear scan** (OPEN-B3-2 partially closed for prototype): iterate all enabled rules in `RS(S)`; evaluate each condition predicate; collect all that fire. O(k_S × c). Sufficient to test F1/F2/F3 governance contract.

**Does not affect Safety Dominance** — Theorem C.3 holds from rule-set content, not engine evaluation order. Linear scan is the prototype evaluation strategy; production strategy remains OPEN-B3-2.

**Predicate evaluation failure (OPEN-L3-2):** if a rule predicate raises an exception, the prototype must not silently treat this as a false predicate. Policy (abort / skip / continue / partial advisories / error result) is OPEN-L3-2.

---

## Concrete rule-content status

**OPEN-L3-1 — Concrete Layer 3 advisory rule content requires scientific specification.**

Inspected all six closed upstream authority documents. No authoritative concrete rule antecedents exist. Layer 2 classification thresholds (w, r, o) do not automatically define Layer 3 advisory rule conditions. No rules invented.

OPEN-L3-1 blocks full prototype completion (Batch 2+) and F1–F3 execution. It does not block Batch 1 contract-design closure.

---

## Fidelity instrumentation

**FidelityTrace** captures per episode: `episode_id`, `state`, `G`, `A_AI`, `active_rule_ids`, `active_rule_conclusion_types`, `fired_rule_ids`, `generated_advisory_types`, `configuration_failure`, `S_old`, `S_new`, `rule_set_bound_for_state`.

| Criterion | Required fields | Assertion | Status |
|---|---|---|---|
| F1 | `generated_advisory_types`, `A_AI` | all types ∈ A_AI | DESIGNED — NOT YET TESTED |
| F2 | `generated_advisory_types`, `A_AI` | violation count = 0 | DESIGNED — NOT YET TESTED |
| F3 | `rule_set_bound_for_state`, `S_new`, `active_rule_conclusion_types`, `A_AI`, `active_rule_ids` | `rule_set_bound_for_state == S_new`; `ConclusionTypes(RS) ⊆ A_AI(S_new)`; `∀ r ∈ active_rule_ids: r.applicable_state == S_new` | DESIGNED — NOT YET TESTED |

**F3 note:** does not require a different rule-set identifier when state changes. Two states may share rule objects while still satisfying their admissibility contracts. An empty RS(SAFE) or RS(CAUTION) satisfies F3 trivially (∅ ⊆ A_AI(S_new)).

---

## OPEN decisions

| ID | Status |
|---|---|
| OPEN-B1-1 through OPEN-B1-7 | OPEN — unchanged |
| OPEN-B1-8 (concurrency) | OPEN — interface defined, primitive not chosen |
| OPEN-B3-1 (invalid repository) | PARTIALLY CLOSED — EpisodeResult contract; implementation handling only |
| OPEN-B3-2 (engine strategy) | PARTIALLY CLOSED — linear scan for prototype; production OPEN |
| OPEN-B3-3 (episode boundary) | PARTIALLY CLOSED — ReasoningEpisode defined; duration/polling OPEN |
| OPEN-B4-1 (solar lookup) | OPEN — unchanged |
| **OPEN-L3-1** | **NEW — OPEN — concrete rule content requires scientific specification** |
| **OPEN-L3-2** | **NEW — OPEN — predicate evaluation failure policy not yet resolved** |

---

## Files changed

| File | Action | Scientific effect |
|---|---|---|
| `publications/active/journal-1/layer3-prototype-specification.md` | CREATED; repaired | Implementation authority — no scientific change |
| `data/journal1-layer3-prototype/integrity-before.json` | CREATED | Pins 16 protected files |
| `data/journal1-layer3-prototype/prototype-contract-batch1.csv` | CREATED | 8 batch deliverables |
| `data/journal1-layer3-prototype/rule-schema-batch1.json` | CREATED | Rule object schema |
| `data/journal1-layer3-prototype/module-map-batch1.csv` | CREATED | 7-module map |
| `data/journal1-layer3-prototype/fidelity-instrumentation-batch1.csv` | CREATED; repaired | F1/F2/F3 field mapping (F3 corrected) |
| `data/journal1-layer3-prototype/test-plan-batch1.csv` | CREATED | 13 test cases (NOT YET IMPLEMENTED) |
| `data/journal1-layer3-prototype/open-decisions-batch1.csv` | CREATED; repaired | 14 OPEN items (OPEN-L3-2 added) |
| `data/journal1-layer3-prototype/semantic-verification-batch1.json` | CREATED; repaired | 30 PASS / 0 FAIL / 2 OPEN (post-repair checks added) |
| `data/journal1-layer3-prototype/change-map-batch1.csv` | CREATED; repaired | File-level change map (repair rows added) |
| `data/journal1-layer3-prototype/build.py` | CREATED | Integrity + CSV parser |
| `data/journal1-layer3-prototype/closure-batch1.json` | CREATED; repaired | Closure record (CLOSED; repair record added) |
| `data/journal1-layer3-prototype/report-batch1.md` | CREATED; repaired | This file |

---

## Protected integrity

```
integrity:     PASS — 16 unchanged, 0 changed
parser batch1: PASS — 6 CSVs checked
```

No canonical formalisation, empirical findings, replay script, solar artefact, raw data, prediction register, or conference manuscript was modified.

---

## Semantic verification

Original: 19 PASS / 0 FAIL / 1 OPEN  
Post-repair: 11 PASS / 0 FAIL / 1 OPEN  
Combined: **30 PASS / 0 FAIL / 2 OPEN** (OPEN-L3-1 + OPEN-L3-2)

---

```
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 1 CLOSED —
FIDELITY TRACE AND FAILURE-SEMANTICS CONTRACT REPAIRED
```
