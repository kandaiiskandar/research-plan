"""Algorithm 3 — Rule-Set Supply: select → validate → supply.

Authority: layer3-prototype-specification.md §8; algorithm-specification.md §17–§18.
Structural validation V1–V4: Batch 3 task §11.
"""
from __future__ import annotations

import dataclasses
from typing import Any

from .rule import (
    Rule, ConditionPredicate, ConfigurationError,
    VALID_CONCLUSION_TYPES, VALID_OPERATORS,
)
from .rule_repository import RuleRepository


# ── GovernanceConfig ──────────────────────────────────────────────────────────

@dataclasses.dataclass(frozen=True)
class GovernanceConfig:
    """Governance pair (G(S), A_AI(S)) for one safety state.

    G: participation gate — 0 means Layer 3 does not participate.
    A_AI: admissible recommendation types for this state.

    Authority: appendix-c C.3 (G mapping) and C.4 (A_AI mapping).
    """
    G: int              # 0 or 1
    A_AI: frozenset     # subset of R = {"Go","Delay","DepartureTime","Duration"}


# ── Governance mapping (Algorithm 2 output, consumed by Algorithm 3) ──────────

GOVERNANCE_MAP: dict[str, GovernanceConfig] = {
    "SAFE": GovernanceConfig(
        G=1,
        A_AI=frozenset({"Go", "Delay", "DepartureTime", "Duration"}),
    ),
    "CAUTION": GovernanceConfig(
        G=1,
        A_AI=frozenset({"Go", "Delay"}),
    ),
    "UNSAFE": GovernanceConfig(
        G=0,
        A_AI=frozenset(),
    ),
}

ALL_STATES: frozenset[str] = frozenset(GOVERNANCE_MAP.keys())


# ── DecisionContext schema for V1–V4 structural validation ────────────────────
#
# Each entry: field_name → {kind, nullable, domain}
#   kind:     "float" | "int" | "str" — base Python type family
#   nullable: True if field can legitimately be None at runtime
#   domain:   frozenset of valid categorical values, or None for continuous fields
#
# Authority: layer3-prototype-specification.md §7 (DecisionContext fields).

DECISION_CONTEXT_SCHEMA: dict[str, dict[str, Any]] = {
    "episode_id": {
        "kind": "str", "nullable": False, "domain": None,
    },
    "vessel_category": {
        "kind": "str", "nullable": False,
        "domain": frozenset({"small", "medium", "big"}),
    },
    "resolved_w": {
        "kind": "float", "nullable": True, "domain": None,
    },
    "resolved_r_rate": {
        "kind": "float", "nullable": True, "domain": None,
    },
    "resolved_r_kappa": {
        "kind": "int", "nullable": True, "domain": frozenset({0, 1}),
    },
    "resolved_m": {
        "kind": "str", "nullable": True,
        "domain": frozenset({"none", "advisory", "warning", "alert"}),
    },
    "resolved_o_wave_height": {
        "kind": "float", "nullable": True, "domain": None,
    },
    "resolved_o_swell_period": {
        "kind": "float", "nullable": True, "domain": None,
    },
    "resolved_t": {
        "kind": "float", "nullable": True, "domain": None,
    },
}

_NUMERIC_KINDS: frozenset[str] = frozenset({"float", "int"})
_NULL_OPERATORS: frozenset[str] = frozenset({"is_none", "is_not_none"})
_MEMBERSHIP_OPERATORS: frozenset[str] = frozenset({"in", "not_in"})
_COMPARISON_OPERATORS: frozenset[str] = frozenset({"<", "<=", "==", ">=", ">"})
# String fields: numeric ordering operators (<, <=, >=, >) are not valid
_STRING_VALID_OPERATORS: frozenset[str] = frozenset({"==", "in", "not_in", "is_none", "is_not_none"})


# ── Helpers ───────────────────────────────────────────────────────────────────

def _value_type_compatible(value: object, kind: str) -> bool:
    """Return True if value is a compatible Python type for the declared field kind.

    int values are accepted for float fields (numerically compatible in Python comparisons).
    bool is excluded from both (bool is a subclass of int in Python but is not a valid
    domain value for any numeric field in this schema).
    """
    if isinstance(value, bool):
        return False
    if kind == "float":
        return isinstance(value, (int, float))
    if kind == "int":
        return isinstance(value, int)
    if kind == "str":
        return isinstance(value, str)
    return False


# ── Algorithm 3 public interface ──────────────────────────────────────────────

def get_governance_config(state: str) -> GovernanceConfig:
    """Return the GovernanceConfig for a valid state.

    Raises ConfigurationError for unrecognised state values.
    """
    if state not in GOVERNANCE_MAP:
        raise ConfigurationError(
            f"Unrecognised state {state!r}; must be one of {sorted(ALL_STATES)!r}",
            failure_type="UNKNOWN_STATE",
            state=state,
        )
    return GOVERNANCE_MAP[state]


def select_rule_set(repository: RuleRepository, state: str) -> list[Rule]:
    """Algorithm 3 lines 1–5: extract enabled rules for the given state.

    RS(UNSAFE) = ∅ — returns [] immediately without touching the repository.
    Unknown state raises ConfigurationError.

    Postconditions (if no error):
      - All returned rules have applicable_state == state and enabled == True.
      - RS(UNSAFE) is always [].
    """
    if state not in ALL_STATES:
        raise ConfigurationError(
            f"Unrecognised state {state!r}; must be one of {sorted(ALL_STATES)!r}",
            failure_type="UNKNOWN_STATE",
            state=state,
        )
    if state == "UNSAFE":
        return []   # RS(UNSAFE) = ∅ — gate-off handled by execute_episode before this is reached
    return [r for r in repository.rules if r.applicable_state == state and r.enabled]


def validate_rule_set(
    candidate: list[Rule],
    state: str,
    episode_id: str,
) -> None:
    """Algorithm 3 lines 6–9 + V1–V4 structural checks.

    Checks (executed in order):
      1. A_AI containment: ConclusionTypes(candidate) ⊆ A_AI(state)
      2. V1 — referenced variable exists in DecisionContext schema  (F-T-11)
      3. V2 — predicate value type compatible with declared variable type  (F-T-04)
      4. V3 — operator valid for declared variable type  (F-T-05)
      5. V4 — categorical predicate value in declared domain  (F-T-06)

    V1 runs before V2 because an unknown variable has no declared type to check.

    Raises ConfigurationError on the first violation found.
    S is NOT modified. No advisory is generated. No reasoning begins.

    These are design-interpretation checks of Algorithm 3's structural-validation role
    (Batch 3 task §11). They are NOT promoted into new external scientific claims.
    """
    config = get_governance_config(state)
    a_ai = config.A_AI

    # ── 1. A_AI containment ───────────────────────────────────────────────────
    offending = [r.rule_id for r in candidate if r.conclusion_type not in a_ai]
    if offending:
        raise ConfigurationError(
            f"A_AI containment violation: rules {offending!r} have conclusion types "
            f"outside A_AI({state!r}) = {sorted(a_ai)!r}",
            failure_type="A_AI_CONTAINMENT",
            episode_id=episode_id,
            state=state,
            offending_rules=offending,
        )

    # ── 2–5. V1–V4 per-predicate checks ──────────────────────────────────────
    for rule in candidate:
        for pred in rule.conditions:

            # V1: variable exists in schema
            if pred.variable not in DECISION_CONTEXT_SCHEMA:
                raise ConfigurationError(
                    f"Rule {rule.rule_id!r}: predicate variable {pred.variable!r} "
                    f"is not a field in DecisionContext schema (V1 / F-T-11)",
                    failure_type="F-T-11",
                    episode_id=episode_id,
                    state=state,
                    offending_rules=[rule.rule_id],
                    offending_predicates=[{
                        "variable": pred.variable,
                        "operator": pred.operator,
                    }],
                )

            field_info = DECISION_CONTEXT_SCHEMA[pred.variable]
            field_kind = field_info["kind"]
            field_domain = field_info["domain"]

            # V2: type compatibility
            if pred.operator in _NULL_OPERATORS:
                if pred.value is not None:
                    raise ConfigurationError(
                        f"Rule {rule.rule_id!r}: operator {pred.operator!r} requires "
                        f"value=None; got {pred.value!r} (type {type(pred.value).__name__!r}) "
                        f"(V2 / F-T-04)",
                        failure_type="F-T-04",
                        episode_id=episode_id,
                        state=state,
                        offending_rules=[rule.rule_id],
                    )
            elif pred.operator in _MEMBERSHIP_OPERATORS:
                if (
                    pred.value is None
                    or isinstance(pred.value, str)
                    or not hasattr(pred.value, "__iter__")
                ):
                    raise ConfigurationError(
                        f"Rule {rule.rule_id!r}: operator {pred.operator!r} requires an "
                        f"iterable (non-string) value; got "
                        f"{type(pred.value).__name__!r} (V2 / F-T-04)",
                        failure_type="F-T-04",
                        episode_id=episode_id,
                        state=state,
                        offending_rules=[rule.rule_id],
                    )
                for elem in pred.value:
                    if not _value_type_compatible(elem, field_kind):
                        raise ConfigurationError(
                            f"Rule {rule.rule_id!r}: collection element {elem!r} "
                            f"(type {type(elem).__name__!r}) is incompatible with field "
                            f"{pred.variable!r} kind {field_kind!r} (V2 / F-T-04)",
                            failure_type="F-T-04",
                            episode_id=episode_id,
                            state=state,
                            offending_rules=[rule.rule_id],
                        )
            else:
                # Comparison operators: value type must match field kind
                if not _value_type_compatible(pred.value, field_kind):
                    raise ConfigurationError(
                        f"Rule {rule.rule_id!r}: predicate value {pred.value!r} "
                        f"(type {type(pred.value).__name__!r}) incompatible with field "
                        f"{pred.variable!r} kind {field_kind!r} (V2 / F-T-04)",
                        failure_type="F-T-04",
                        episode_id=episode_id,
                        state=state,
                        offending_rules=[rule.rule_id],
                    )

            # V3: operator valid for field type
            if field_kind not in _NUMERIC_KINDS:
                # String fields: numeric ordering operators are not valid
                if pred.operator not in _STRING_VALID_OPERATORS:
                    raise ConfigurationError(
                        f"Rule {rule.rule_id!r}: operator {pred.operator!r} is not valid "
                        f"for string field {pred.variable!r}; "
                        f"allowed: {sorted(_STRING_VALID_OPERATORS)!r} (V3 / F-T-05)",
                        failure_type="F-T-05",
                        episode_id=episode_id,
                        state=state,
                        offending_rules=[rule.rule_id],
                    )
            # Numeric fields accept all operators — no additional V3 check needed.

            # V4: categorical value in declared domain
            if field_domain is not None:
                if pred.operator == "==" and isinstance(pred.value, (str, int)):
                    if pred.value not in field_domain:
                        raise ConfigurationError(
                            f"Rule {rule.rule_id!r}: predicate value {pred.value!r} not in "
                            f"declared domain {sorted(str(v) for v in field_domain)!r} "
                            f"for field {pred.variable!r} (V4 / F-T-06)",
                            failure_type="F-T-06",
                            episode_id=episode_id,
                            state=state,
                            offending_rules=[rule.rule_id],
                        )
                elif pred.operator in _MEMBERSHIP_OPERATORS and pred.value is not None:
                    for elem in pred.value:
                        if elem not in field_domain:
                            raise ConfigurationError(
                                f"Rule {rule.rule_id!r}: collection element {elem!r} not in "
                                f"declared domain {sorted(str(v) for v in field_domain)!r} "
                                f"for field {pred.variable!r} (V4 / F-T-06)",
                                failure_type="F-T-06",
                                episode_id=episode_id,
                                state=state,
                                offending_rules=[rule.rule_id],
                            )
