"""Algorithm 4 — Governed Advisory Generation: deterministic linear scan engine.

Authority: layer3-prototype-specification.md §9.3; algorithm-specification.md §19–§20.
Predicate result domain and failure taxonomy: Batch 3 task §12–§16.

Engine strategy chosen: linear scan O(k_S × c).
  k_S = |RS(S)| (number of rules in active rule set)
  c   = average number of conditions per rule

Failure collection strategy: Model B (collect all ERROR-producing rules before refusing episode).
Within each rule: abort after first ERROR predicate.
Across rules: continue collecting all failed rules, then refuse if any errors found.

Both strategies produce AI(E) = ∅ on any ERROR — the choice affects diagnostics only.
This is an engineering decision and does not claim scientific superiority.
Production chaining strategy (RETE, agenda priority, first-match, all-match, backward
chaining) remains OPEN-B3-2 for production deployment.
"""
from __future__ import annotations

import dataclasses
import enum
from typing import Optional

from .rule import Rule, ConditionPredicate
from .advisory import Advisory


# ── PredicateResult ───────────────────────────────────────────────────────────

class PredicateResult(enum.Enum):
    """Three-valued result domain for predicate evaluation.

    TRUE  — predicate successfully evaluated and satisfied.
    FALSE — predicate successfully evaluated and not satisfied.
    ERROR — predicate could not be established because evaluation failed.

    CRITICAL: ERROR ≠ FALSE and ERROR ≠ TRUE.
    An ERROR must never be silently reinterpreted as FALSE (no-fire) or TRUE (fire).
    """
    TRUE = "TRUE"
    FALSE = "FALSE"
    ERROR = "ERROR"


# ── FailureCategory ───────────────────────────────────────────────────────────

class FailureCategory(enum.Enum):
    """Runtime predicate evaluation failure categories (F-T-07 through F-T-10).

    These are runtime failures distinct from V1–V4 configuration failures.
    The taxonomy maps to the Batch 3 task §15 specification.
    """
    PREDICATE_EXCEPTION = "PREDICATE_EXCEPTION"         # F-T-07: exception during evaluation
    NUMERIC_CONVERSION_FAILURE = "NUMERIC_CONVERSION_FAILURE"  # F-T-08: type incompatibility
    MALFORMED_VALUE = "MALFORMED_VALUE"                 # F-T-09: None where value required
    INTERNAL_ERROR = "INTERNAL_ERROR"                   # F-T-10: unexpected internal error


# ── evaluate_predicate ────────────────────────────────────────────────────────

def evaluate_predicate(
    pred: ConditionPredicate,
    context: object,  # DecisionContext — typed as object to avoid circular import
) -> tuple[PredicateResult, Optional[FailureCategory], Optional[str]]:
    """Evaluate a single ConditionPredicate against the DecisionContext.

    Returns (PredicateResult, failure_category, message):
      (TRUE,  None,     None)    — predicate satisfied
      (FALSE, None,     None)    — predicate not satisfied (normal no-fire)
      (ERROR, category, message) — evaluation failure

    CRITICAL: ERROR is structurally distinct from FALSE.
    - None actual value with comparison operator → MALFORMED_VALUE (F-T-09)
    - TypeError from incompatible types → NUMERIC_CONVERSION_FAILURE (F-T-08)
    - Other exception during evaluation → PREDICATE_EXCEPTION (F-T-07)
    - Missing variable (should be caught by V1) → INTERNAL_ERROR (F-T-10)
    - Unknown operator (should not reach here after V3) → INTERNAL_ERROR (F-T-10)
    """
    try:
        # AttributeError here means V1 was not run — guard as INTERNAL_ERROR
        try:
            actual = getattr(context, pred.variable)
        except AttributeError:
            return (
                PredicateResult.ERROR,
                FailureCategory.INTERNAL_ERROR,
                f"Variable {pred.variable!r} not found in context; "
                f"V1 structural validation should have caught this (F-T-10)",
            )

        op = pred.operator
        val = pred.value

        # ── Null operators ────────────────────────────────────────────────────
        if op == "is_none":
            return (
                PredicateResult.TRUE if actual is None else PredicateResult.FALSE,
                None, None,
            )
        if op == "is_not_none":
            return (
                PredicateResult.TRUE if actual is not None else PredicateResult.FALSE,
                None, None,
            )

        # ── None actual value with ordering operator → MALFORMED_VALUE (F-T-09) ─
        # Only ordering operators are incompatible with None; Python raises TypeError
        # for None < x etc. Equality (==) and membership (in/not_in) handle None
        # natively: None == "advisory" → False, so the predicate is not satisfied.
        if actual is None and op in {"<", "<=", ">=", ">"}:
            return (
                PredicateResult.ERROR,
                FailureCategory.MALFORMED_VALUE,
                f"Variable {pred.variable!r} is None but ordering operator {op!r} "
                f"requires a non-None comparable value (F-T-09)",
            )

        # ── Membership operators ──────────────────────────────────────────────
        if op == "in":
            try:
                result = actual in val
                return (PredicateResult.TRUE if result else PredicateResult.FALSE, None, None)
            except TypeError as exc:
                return (
                    PredicateResult.ERROR,
                    FailureCategory.PREDICATE_EXCEPTION,
                    f"'in' membership test failed for {pred.variable!r} "
                    f"(actual={actual!r}, collection={val!r}): {exc} (F-T-07)",
                )

        if op == "not_in":
            try:
                result = actual not in val
                return (PredicateResult.TRUE if result else PredicateResult.FALSE, None, None)
            except TypeError as exc:
                return (
                    PredicateResult.ERROR,
                    FailureCategory.PREDICATE_EXCEPTION,
                    f"'not_in' membership test failed for {pred.variable!r} "
                    f"(actual={actual!r}, collection={val!r}): {exc} (F-T-07)",
                )

        # ── Comparison operators ──────────────────────────────────────────────
        try:
            if op == "<":
                result = actual < val
            elif op == "<=":
                result = actual <= val
            elif op == "==":
                result = actual == val
            elif op == ">=":
                result = actual >= val
            elif op == ">":
                result = actual > val
            else:
                # Unknown operator — should not reach here if V3 validation ran
                return (
                    PredicateResult.ERROR,
                    FailureCategory.INTERNAL_ERROR,
                    f"Unknown operator {op!r} reached evaluation; "
                    f"V3 structural validation should have caught this (F-T-10)",
                )
            return (PredicateResult.TRUE if result else PredicateResult.FALSE, None, None)

        except TypeError as exc:
            return (
                PredicateResult.ERROR,
                FailureCategory.NUMERIC_CONVERSION_FAILURE,
                f"TypeError comparing {pred.variable!r} "
                f"(actual={actual!r}, type={type(actual).__name__!r}) "
                f"with value {val!r} (type={type(val).__name__!r}) "
                f"using operator {op!r}: {exc} (F-T-08)",
            )
        except Exception as exc:
            return (
                PredicateResult.ERROR,
                FailureCategory.PREDICATE_EXCEPTION,
                f"Exception during comparison for {pred.variable!r}: {exc} (F-T-07)",
            )

    except Exception as exc:
        # Outer guard — truly unexpected internal error
        return (
            PredicateResult.ERROR,
            FailureCategory.INTERNAL_ERROR,
            f"Unexpected internal error evaluating predicate for "
            f"{pred.variable!r}: {exc} (F-T-10)",
        )


# ── ReasonResult ──────────────────────────────────────────────────────────────

@dataclasses.dataclass
class ReasonResult:
    """Return value of ReasoningEngine.reason() — consumed by execute_episode()."""
    advisories: list              # list[Advisory] — empty on evaluation_failure
    fired_rule_ids: list[str]     # rule_ids that fired (all predicates TRUE)
    evaluation_failure: bool      # True if any predicate returned ERROR
    failed_rule_ids: list[str]    # rule_ids where predicate ERROR occurred
    failure_category: Optional[FailureCategory]  # first failure category seen
    failure_messages: list[str]   # diagnostic messages (one per failed rule)


# ── ReasoningEngine ───────────────────────────────────────────────────────────

class ReasoningEngine:
    """Algorithm 4 — deterministic linear scan over RS(S).

    For each rule:
      1. Evaluate conditions conjunctively.
      2. If all TRUE → fire rule, emit Advisory.
      3. If any FALSE → normal no-fire (skip rule, continue).
      4. If any ERROR → mark rule failed, continue to next rule (Model B collection).

    After full scan:
      - If any failed rules → evaluation_failure=True, AI(E)=∅ (Model C+D refusal).
      - Otherwise → return all fired advisories.

    The engine does not compute or mutate S. It receives RS(S) from the validated
    rule-set provider and fires only rules present in that set.

    OPEN-B3-2 status: linear scan prototype strategy partially closes the implementation
    question. Production chaining strategy remains OPEN-B3-2.
    """

    def reason(
        self,
        context: object,       # DecisionContext
        rule_set: list[Rule],
    ) -> ReasonResult:
        """Evaluate all rules in rule_set against context.

        Complexity: O(k_S × c) where k_S = |rule_set|, c = avg conditions/rule.
        Deterministic: given identical (context, rule_set) produces identical output.
        """
        fired_advisories: list[Advisory] = []
        fired_rule_ids: list[str] = []
        failed_rule_ids: list[str] = []
        first_failure_category: Optional[FailureCategory] = None
        failure_messages: list[str] = []

        for rule in rule_set:
            outcome, advisory, cat, msg = self._evaluate_rule(rule, context)

            if outcome == "ERROR":
                failed_rule_ids.append(rule.rule_id)
                if first_failure_category is None:
                    first_failure_category = cat
                if msg:
                    failure_messages.append(msg)
            elif outcome == "FIRED":
                fired_advisories.append(advisory)
                fired_rule_ids.append(rule.rule_id)
            # "NO_FIRE": normal semantic result — rule did not apply

        evaluation_failure = bool(failed_rule_ids)

        if evaluation_failure:
            # Model C+D: any ERROR → refuse advisory generation for the episode
            return ReasonResult(
                advisories=[],
                fired_rule_ids=[],
                evaluation_failure=True,
                failed_rule_ids=failed_rule_ids,
                failure_category=first_failure_category,
                failure_messages=failure_messages,
            )

        return ReasonResult(
            advisories=fired_advisories,
            fired_rule_ids=fired_rule_ids,
            evaluation_failure=False,
            failed_rule_ids=[],
            failure_category=None,
            failure_messages=[],
        )

    def _evaluate_rule(
        self,
        rule: Rule,
        context: object,
    ) -> tuple[str, Optional[Advisory], Optional[FailureCategory], Optional[str]]:
        """Evaluate one rule's predicates conjunctively.

        Returns one of:
          ("FIRED",   advisory, None, None)   — all predicates TRUE
          ("NO_FIRE", None,     None, None)   — some predicate FALSE
          ("ERROR",   None,     cat,  msg)    — some predicate ERROR
        """
        for pred in rule.conditions:
            pred_result, cat, msg = evaluate_predicate(pred, context)

            if pred_result == PredicateResult.ERROR:
                return ("ERROR", None, cat, msg)
            if pred_result == PredicateResult.FALSE:
                return ("NO_FIRE", None, None, None)
            # PredicateResult.TRUE — continue to next predicate

        # All predicates evaluated TRUE (or rule has no conditions)
        advisory = Advisory(
            type=rule.conclusion_type,
            payload=dict(rule.conclusion_payload),
            rule_id=rule.rule_id,
            explanation=rule.conclusion_payload.get(
                "reason",
                f"Rule {rule.rule_id} fired (state: {rule.applicable_state})",
            ),
        )
        return ("FIRED", advisory, None, None)
