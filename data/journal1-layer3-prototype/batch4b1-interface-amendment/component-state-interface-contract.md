# ComponentStateTrace — Interface Contract

**Authority:** Batch 4B-1 (2026-09-11)  
**Branch:** `design/journal1-layer3-component-state-interface`  
**Specification source:** `publications/active/journal-1/layer3-prototype-specification.md` §7.1  
**Batch 4A basis:** `data/journal1-layer3-prototype/batch4a-executable-rule-authority/resolution.json`

---

## Purpose

`ComponentStateTrace` is an implementation-level interface object. Its purpose is to carry the already-computed component classification results from Layer 2 to Layer 3, so that Layer 3 rule predicates can inspect which component drove the current safety state without reimplementing any Layer 2 classifier.

---

## Authority

Authorised by Batch 4A (Model B selected, 2026-09-11). The specification provision at `layer3-prototype-specification.md` §7 — "If Layer 3 implementation in later batches identifies a need for additional advisory inputs not derivable from canonical E, those inputs must be documented explicitly here as implementation-level additions" — is the canonical gate for this contract.

---

## Producer

**Layer 2 (deterministic governance).** Layer 2 computes `g_i(·)` as part of determining `S = max-severity(g_w, g_r, g_m, g_o, g_t)`. ComponentStateTrace is populated from those same intermediate results before Layer 3 executes.

---

## Consumer

**Layer 3 (advisory reasoning engine).** Layer 3 receives ComponentStateTrace as a read-only input. Rule predicates may inspect component state values as already-computed facts.

---

## Fields

| Field | Type domain | Source | Notes |
|---|---|---|---|
| `component_w_state` | `{"SAFE", "CAUTION", "EXCLUDED"}` | `g_w(w)` output | Wind speed component |
| `component_r_state` | `{"SAFE", "CAUTION", "EXCLUDED"}` | `g_r(r, κ)` output | Rainfall component (two-input) |
| `component_m_state` | `{"SAFE", "CAUTION", "EXCLUDED"}` | `g_m(m)` output | Marine warning component |
| `component_o_state` | `{"SAFE", "CAUTION", "EXCLUDED"}` | `g_o(o, v)` output | Ocean state (vessel-conditioned) |
| `component_t_state` | `{"SAFE", "EXCLUDED"}` | `g_t(t, date)` output | Time-of-day component; g_t emits no CAUTION |

---

## Domains — Type vs. Runtime

The type domain is the interface type visible to Layer 3. Valid runtime values are further constrained:

| Value | Meaning | Notes |
|---|---|---|
| `SAFE` | Component classified SAFE by Layer 2 | Observed SAFE — a valid environmental measurement in the SAFE band |
| `CAUTION` | Component classified CAUTION by Layer 2 | Observed CAUTION — a valid measurement in the CAUTION band |
| `EXCLUDED` | Component is in declared exclusion set D | Not `SAFE`. Pinned SAFE for aggregation only; the interface exposes actual status |
| `UNSAFE` | — | **Unreachable at Layer 3 interface.** Any UNSAFE component → S=UNSAFE → G(UNSAFE)=0 → Layer 3 never invoked |
| `FAULTED` | — | **Unreachable at Layer 3 interface.** Faulted components → g_i(⊥)=UNSAFE → same path as UNSAFE |

---

## Exclusion Semantics

**`EXCLUDED ≠ observed SAFE.`**

A component with `EXCLUDED` was not measured — it is in the declared exclusion set `D`. Layer 2 pins it to SAFE for max-severity aggregation purposes (appendix-c C.2.0.5). At the Layer 3 interface, the true status is exposed as `EXCLUDED` to prevent misinterpretation.

- `component_m_state = EXCLUDED` in retrospective replay (`D = {m}`) — means marine warning was not measured. Does not assert absence of marine hazard. All severity figures under `D = {m}` are lower bounds.
- `component_t_state` — `t ∉ D` always (appendix-c C.2.0.5 D1). `EXCLUDED` is unreachable for `t` under the current canonical configuration.

---

## Fault Semantics

Faulted components (`obs_i = ⊥` → `g_i(⊥) = UNSAFE`) cause `S = UNSAFE` and Layer 3 gate-off (Corollary C.1b.1). The fault resolves entirely within Layer 2 fail-safe semantics. `FAULTED` is not a new component governance state; it is absorbed by the UNSAFE gate-off path. Layer 3 never receives a faulted component state.

---

## UNSAFE Gate-Off Relationship

```
Any component g_i(·) = UNSAFE
→ S = UNSAFE (max-severity)
→ G(UNSAFE) = 0
→ Layer 3 not invoked
→ ComponentStateTrace not visible to Layer 3
```

This is an execution-boundary consequence, not a redefinition of g_i. The classifiers can and do return UNSAFE; Layer 3 simply never executes in those episodes.

---

## Episode Consistency Invariant

ComponentStateTrace must correspond to the same Layer 2 evaluation episode that produced S:

```
episode_id(S) = episode_id(ComponentStateTrace)
```

Layer 3 must never receive S from episode A and ComponentStateTrace from episode B. The `episode_id` field in `DecisionContext` serves as the episode identifier; both S and the component states must originate from the same `execute_episode()` invocation.

---

## S / Component-State Consistency Invariant

ComponentStateTrace and S must be semantically consistent:

```
S = SAFE    → all active (non-EXCLUDED) components are SAFE
S = CAUTION → at least one active component is CAUTION; none is UNSAFE
S = UNSAFE  → Layer 3 gated off; ComponentStateTrace not visible to Layer 3
```

`EXCLUDED` is not active for aggregation and does not violate consistency with any S value. If inconsistency is detected at an implementation boundary, it must be classified as a configuration/interface fidelity failure.

---

## Read-Only Requirement

Layer 3 must not modify, mutate, cache across episodes, or feed back any component state value. Component states are facts from the current episode's Layer 2 classification. They must not carry over to the next episode.

---

## No Layer 2 Recomputation Requirement

Layer 3 rule predicates must not reproduce threshold comparisons:

- Not `resolved_w >= 21.6 AND resolved_w <= 27.0` (duplicates g_w)
- Not vessel-category wave height bands (duplicates g_o)
- Not rainfall rate thresholds + κ logic (duplicates g_r)
- Not solar event lookup (duplicates g_t — explicitly prohibited)

Permitted: `component_o_state == "CAUTION"` — consumes an already-computed Layer 2 result.  
Prohibited: re-deriving that result from raw resolved values.

---

## Safety Dominance Relationship

ComponentStateTrace does not modify:
- `A_AI(SAFE) = {Go, Delay, DepartureTime, Duration}`
- `A_AI(CAUTION) = {Go, Delay}`
- `A_AI(UNSAFE) = ∅`

`AI(E) ⊆ A_AI(S)` continues to hold by construction from RS(S) (Theorem C.3, appendix-c §C.7.2). The proof depends only on S; it is independent of interface content beyond S.

---

## Human-Authority Relationship

ComponentStateTrace does not introduce:
- Automatic prohibition
- Automatic approval
- Human override restriction

No advisory generated by a rule whose predicate inspects a component state becomes mandatory. Human authority is unconditional in all states.

---

## Future Rule Mappings (Informative)

Authorised in principle by Batch 4A; implementation deferred to Batch 4B-2:

| Rule | Candidate predicate | Conclusion |
|---|---|---|
| R-CAUTION-002 | `component_o_state == "CAUTION"` | Delay |
| R-CAUTION-003 | `component_r_state == "CAUTION"` | Delay |
| R-CAUTION-004 | `component_w_state == "CAUTION"` | Delay |

Deferred items:
- **R-SAFE-001**: STATE_RESTATEMENT — requires bounded scientific decision before implementation
- **R-CAUTION-001 migration**: `resolved_m == "advisory"` → `component_m_state == "CAUTION"` — future consistency consideration only, not authorised

---

## Explicit Non-Goals

ComponentStateTrace is NOT:

- A new governance layer
- A new environmental state vector
- A replacement or extension of canonical E, ρ_{D,τ}, f, or F_{D,τ}
- A second classifier
- A new source of scientific authority
- A mechanism for S to be re-determined inside Layer 3
- A basis for CAUTION→Go rule (OPEN-L3-3 Resolution B preserved)
- A way to implement R-SAFE-001 through component-state conjunction
- Equivalent to the `reasons` taxonomy (fault/hazard/policy) — reasons remain explanatory only
