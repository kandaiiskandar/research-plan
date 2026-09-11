"""Rule and ConditionPredicate dataclasses — structural rule representation.

Authority: layer3-prototype-specification.md §4 (Rule schema), §4.1 (predicate schema).
"""
from __future__ import annotations

import dataclasses
from typing import Any


# ── Recommendation type universe R ───────────────────────────────────────────
VALID_CONCLUSION_TYPES: frozenset[str] = frozenset(
    {"Go", "Delay", "DepartureTime", "Duration"}
)

# Applicable states for rules — UNSAFE rules do not exist; RS(UNSAFE) = ∅
VALID_RULE_STATES: frozenset[str] = frozenset({"SAFE", "CAUTION"})

# All recognised predicate operators
VALID_OPERATORS: frozenset[str] = frozenset({
    "<", "<=", "==", ">=", ">",
    "in", "not_in",
    "is_none", "is_not_none",
})


# ── ConfigurationError ────────────────────────────────────────────────────────

class ConfigurationError(Exception):
    """Rule repository or rule-set structural failure occurring before reasoning begins.

    Raised by validate_rule_set() and execute_episode() on configuration-level violations.
    S is not modified when this is raised. Layer 3 is disabled for the episode.

    failure_type codes:
        "F-T-11"                  — V1: predicate references a variable not in DecisionContext schema
        "F-T-04"                  — V2: predicate value type incompatible with declared variable type
        "F-T-05"                  — V3: predicate operator invalid for declared variable type
        "F-T-06"                  — V4: categorical predicate value outside declared domain
        "A_AI_CONTAINMENT"        — ConclusionTypes(RS_candidate) ⊄ A_AI(S)
        "UNKNOWN_STATE"           — unrecognised state argument to select_rule_set / get_governance_config
        "MISSING_VESSEL"          — vessel_category absent or unrecognised at startup
        "STATE_TRACE_INCONSISTENCY" — S and ComponentStateTrace are mutually inconsistent
    """

    def __init__(
        self,
        message: str,
        *,
        failure_type: str | None = None,
        episode_id: str | None = None,
        state: str | None = None,
        offending_rules: list[str] | None = None,
        offending_predicates: list[dict] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(message)
        self.failure_type = failure_type
        self.episode_id = episode_id
        self.state = state
        self.offending_rules = list(offending_rules or [])
        self.offending_predicates = list(offending_predicates or [])
        self.details = kwargs


# ── ConditionPredicate ────────────────────────────────────────────────────────

@dataclasses.dataclass(frozen=True)
class ConditionPredicate:
    """A single predicate triple (variable, operator, value) evaluated against DecisionContext.

    variable: field name in DecisionContext schema — validated at V1 (F-T-11).
    operator: one of VALID_OPERATORS — validated at V3 (F-T-05).
    value:    threshold, iterable, or None (required for is_none / is_not_none) — validated at V2/V4.

    Predicate evaluation returns PredicateResult ∈ {TRUE, FALSE, ERROR}.
    ERROR is distinct from FALSE — never silently treated as FALSE.
    """

    variable: str
    operator: str
    value: object


# ── Rule ──────────────────────────────────────────────────────────────────────

@dataclasses.dataclass(frozen=True)
class Rule:
    """One production rule in the Layer 3 rule engine.

    applicable_state ∈ {"SAFE", "CAUTION"}. UNSAFE rules do not exist.
    conditions: conjunctive tuple of ConditionPredicate — all must evaluate TRUE to fire.
    conclusion_type ∈ R = {"Go", "Delay", "DepartureTime", "Duration"}.
    provenance: non-empty scientific authority reference — enforced at construction.
    enabled: disabled rules are excluded from RS(S) at rule-set selection time.

    Note: conclusion_payload is a mutable dict; Rule objects are not hashable due to this field.
    The frozen constraint prevents field reassignment but does not prevent dict mutation.
    """

    rule_id: str
    applicable_state: str
    conditions: tuple  # tuple[ConditionPredicate, ...]
    conclusion_type: str
    conclusion_payload: dict
    provenance: str
    enabled: bool

    def __post_init__(self) -> None:
        if self.applicable_state not in VALID_RULE_STATES:
            raise ValueError(
                f"applicable_state must be in {sorted(VALID_RULE_STATES)!r}; "
                f"got {self.applicable_state!r}"
            )
        if self.conclusion_type not in VALID_CONCLUSION_TYPES:
            raise ValueError(
                f"conclusion_type must be in {sorted(VALID_CONCLUSION_TYPES)!r}; "
                f"got {self.conclusion_type!r}"
            )
        if not self.provenance:
            raise ValueError("provenance must be a non-empty string")
        if not isinstance(self.conditions, tuple):
            raise TypeError(
                f"conditions must be a tuple of ConditionPredicate; "
                f"got {type(self.conditions).__name__!r}"
            )
