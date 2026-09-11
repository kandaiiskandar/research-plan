# Canonical Rule Activation Analysis — Batch 4B-2

**Date:** 2026-09-11  
**Branch:** `feat/journal1-layer3-component-state-rules`  
**Authority:** Batch 4B-1 component-state-interface-contract.md; Batch 4A resolution.json

---

## 1. Canonical Repository after Batch 4B-2

| Rule | State | Predicate | Conclusion | Status |
|---|---|---|---|---|
| R-CAUTION-001 | CAUTION | `resolved_m == "advisory"` | Delay | IMPLEMENTED (Batch 3) |
| R-CAUTION-002 | CAUTION | `component_o_state == "CAUTION"` | Delay | IMPLEMENTED (Batch 4B-2) |
| R-CAUTION-003 | CAUTION | `component_r_state == "CAUTION"` | Delay | IMPLEMENTED (Batch 4B-2) |
| R-CAUTION-004 | CAUTION | `component_w_state == "CAUTION"` | Delay | IMPLEMENTED (Batch 4B-2) |
| R-SAFE-001 | SAFE | (deferred) | Go | DEFERRED — STATE_RESTATEMENT |

---

## 2. Retrospective Replay Activation Projection

**D = {m}, replay covers 43,848 hours (PRIMARY configuration)**

| Rule | Expected activations | Reasoning |
|---|---|---|
| R-CAUTION-001 | 0 | `m ∈ D` → `resolved_m = None` throughout → predicate always FALSE |
| R-CAUTION-002 | ~ binding rate of g_o | Fires whenever g_o(o,v)=CAUTION and S=CAUTION |
| R-CAUTION-003 | ~ binding rate of g_r | Fires whenever g_r(r,κ)=CAUTION and S=CAUTION |
| R-CAUTION-004 | 0 (or near 0) | g_w activates 2 times in 43,848 hours (F-17); binds 0 times |

**Note:** R-CAUTION-004 activation count follows g_w binding profile: g_w activates at 21.6–27.0 kn range in 2 of 43,848 hours but never binds (another component always more severe). Since R-CAUTION-004 fires when S=CAUTION AND component_w_state=="CAUTION", and component_w_state=="CAUTION" requires g_w=CAUTION, the rule activation count equals the count of hours where both g_w=CAUTION and S=CAUTION. This is 0 in the PRIMARY configuration (g_w never binds; when g_w activates, S is already determined by another component).

**Note on R-CAUTION-001 (0 activations):** This is the expected lower-bound result from D={m}. All severity figures derived from this replay are lower bounds. See GAP-05 in layer3-prototype-specification.md §25.

---

## 3. No Layer 2 Recomputation

All three new rules consume already-computed g_i(·) outputs from ComponentStateTrace. They do NOT:
- Compare `resolved_w` against 21.6 or 27.0 kn (g_w thresholds)
- Compare `resolved_r_rate` against 10.0 or 20.0 mm/hr (g_r thresholds)
- Compare `resolved_o_wave_height` against vessel-conditioned bands (g_o thresholds)

This satisfies the No-Layer-2-Recomputation requirement (layer3-prototype-specification.md §7.1).

---

## 4. EXCLUDED Non-Activation

In the D={m} replay: `component_m_state = "EXCLUDED"` in all hours.

R-CAUTION-001 uses `resolved_m == "advisory"` (not a component state predicate), so it doesn't interact with EXCLUDED semantics directly. No rule uses `component_m_state` as a firing condition in the current canonical set.

EXCLUDED domains are correctly validated by V4: component_m_state="EXCLUDED" is in its declared domain; it satisfies `component_m_state == "EXCLUDED"` predicates (TRUE) and doesn't satisfy `component_m_state == "CAUTION"` predicates (FALSE). This is verified by tests B01–B05.

---

## 5. Concurrent Activation Semantics

When multiple component states are CAUTION simultaneously, multiple rules fire. Each fired rule produces one Delay advisory attributed to its rule_id. No deduplication is performed — if three rules fire, three advisories are emitted, each traceable to its rule.

All Delay advisories are within A_AI(CAUTION) = {Go, Delay}. Safety Dominance (AI(E) ⊆ A_AI(S)) holds by construction.

---

## 6. S/Trace Consistency and Rule Activation Interaction

The consistency check (Step 2.5) ensures that before any rule fires:
- S=CAUTION → at least one active component is CAUTION

This means R-CAUTION-002/003/004 can only fire when the consistency invariant is satisfied. If a context incorrectly claims S=CAUTION with all-SAFE components, the consistency check fires `configuration_failure=True` and no rules execute. The rules thus never produce advisories from an inconsistent S/trace pair.

---

## 7. Protected OPEN Items Confirmed Unaffected

| Item | Status after Batch 4B-2 |
|---|---|
| OPEN-L3-3 Resolution B | PRESERVED — no CAUTION→Go rule added |
| OPEN-L3-1C (DepartureTime) | PRESERVED — no DepartureTime rule added |
| OPEN-L3-1D (Duration) | PRESERVED — no Duration rule added |
| GAP-03 (Go under CAUTION) | PRESERVED — no Go rule under CAUTION |
| R-SAFE-001 STATE_RESTATEMENT | PRESERVED — deferred, not implemented |
| R-CAUTION-001 migration | NOT ACTIONED — future consistency consideration |
