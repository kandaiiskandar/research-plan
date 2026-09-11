"""RuleRepository — repository of scientifically admitted Layer 3 production rules.

Authority: layer3-prototype-specification.md §5.
"""
from __future__ import annotations

from .rule import Rule, VALID_RULE_STATES, VALID_CONCLUSION_TYPES


class RuleRepository:
    """State-indexed repository of Layer 3 production rules.

    insert() enforces at load time:
      - applicable_state ∈ {"SAFE", "CAUTION"} (enforced by Rule constructor)
      - conclusion_type ∈ R (enforced by Rule constructor)
      - provenance is non-empty (enforced by Rule constructor)

    rules property returns a defensive copy — iteration order is stable (insertion order).
    RS(UNSAFE) = ∅ is not a repository property; it is enforced by select_rule_set().
    """

    def __init__(self) -> None:
        self._rules: list[Rule] = []

    def insert(self, rule: Rule) -> None:
        """Add a rule to the repository.

        Rule constructor already validates applicable_state, conclusion_type, provenance.
        """
        if not isinstance(rule, Rule):
            raise TypeError(f"Expected a Rule instance; got {type(rule).__name__!r}")
        self._rules.append(rule)

    @property
    def rules(self) -> list[Rule]:
        """All rules in the repository (defensive copy, stable order)."""
        return list(self._rules)

    def __len__(self) -> int:
        return len(self._rules)

    def __repr__(self) -> str:
        return (
            f"RuleRepository({len(self._rules)} rules: "
            f"{[r.rule_id for r in self._rules]!r})"
        )
