"""Engineering verification tests for the Layer 3 governed reasoning engine.

These are implementation-level tests (T01–T25+), NOT Journal 1 F1–F3 scientific evaluation.
Test-only stub rules are used for engine mechanism tests; they are clearly labelled and
make no scientific claims.

Batch 3 task §27 requirement:
  "These are engineering verification tests, not yet Journal 1 F1–F3 scientific evaluation.
   Add more implementation tests where necessary, but do not turn them into new scientific claims."

Human-authority invariant: F1–F3 are NOT run here. E5 is NOT run here.
"""
import sys
import os
import dataclasses
import unittest

# Make governance importable from project root
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from governance.rule import Rule, ConditionPredicate, ConfigurationError, VALID_OPERATORS
from governance.advisory import Advisory
from governance.fidelity_trace import FidelityTrace
from governance.rule_repository import RuleRepository
from governance.rule_set_provider import (
    GovernanceConfig, get_governance_config, select_rule_set, validate_rule_set,
    GOVERNANCE_MAP, DECISION_CONTEXT_SCHEMA,
)
from governance.reasoning_engine import (
    PredicateResult, FailureCategory, evaluate_predicate, ReasoningEngine, ReasonResult,
)
from governance.reasoning_episode import (
    DecisionContext, ReasoningEpisode, EpisodeResult, execute_episode,
)
from governance.canonical_rules import build_canonical_repository, DEFERRED_RULES


# ── Helpers ───────────────────────────────────────────────────────────────────

def _ctx(**kwargs) -> DecisionContext:
    """Create a DecisionContext with safe defaults, overridable via kwargs."""
    defaults = dict(
        episode_id="test-ep-001",
        vessel_category="small",
        resolved_w=5.0,
        resolved_r_rate=2.0,
        resolved_r_kappa=0,
        resolved_m=None,
        resolved_o_wave_height=0.5,
        resolved_o_swell_period=None,
        resolved_t=10.0,
    )
    defaults.update(kwargs)
    return DecisionContext(**defaults)


def _test_rule(rule_id: str, state: str, conditions, conclusion_type: str,
               enabled: bool = True) -> Rule:
    """Create a test-only stub rule. NOT a scientific rule — for engine mechanism tests only."""
    return Rule(
        rule_id=rule_id,
        applicable_state=state,
        conditions=tuple(conditions),
        conclusion_type=conclusion_type,
        conclusion_payload={"reason": f"TEST-ONLY rule {rule_id} fired"},
        provenance=f"TEST-ONLY stub — not a scientific rule. Used for engine mechanism testing.",
        enabled=enabled,
    )


def _repo(*rules: Rule) -> RuleRepository:
    """Create a RuleRepository from a variable list of rules."""
    repo = RuleRepository()
    for r in rules:
        repo.insert(r)
    return repo


# ── Spy engine for structural testing ────────────────────────────────────────

class _SpyEngine(ReasoningEngine):
    """Records whether reason() was invoked. Used for T04 structural verification."""
    def __init__(self):
        super().__init__()
        self.reason_called = False

    def reason(self, context, rule_set):
        self.reason_called = True
        return super().reason(context, rule_set)


# ═════════════════════════════════════════════════════════════════════════════
# T01–T03  Governance gate mapping
# ═════════════════════════════════════════════════════════════════════════════

class TestGovernanceGateMapping(unittest.TestCase):

    def test_T01_SAFE_gate_enabled(self):
        """T01: G(SAFE) == 1."""
        config = get_governance_config("SAFE")
        self.assertEqual(config.G, 1)

    def test_T02_CAUTION_gate_enabled(self):
        """T02: G(CAUTION) == 1."""
        config = get_governance_config("CAUTION")
        self.assertEqual(config.G, 1)

    def test_T03_UNSAFE_gate_disabled(self):
        """T03: G(UNSAFE) == 0."""
        config = get_governance_config("UNSAFE")
        self.assertEqual(config.G, 0)

    def test_A_AI_SAFE_full(self):
        """A_AI(SAFE) == {Go, Delay, DepartureTime, Duration}."""
        config = get_governance_config("SAFE")
        self.assertEqual(config.A_AI, frozenset({"Go", "Delay", "DepartureTime", "Duration"}))

    def test_A_AI_CAUTION_restricted(self):
        """A_AI(CAUTION) == {Go, Delay}."""
        config = get_governance_config("CAUTION")
        self.assertEqual(config.A_AI, frozenset({"Go", "Delay"}))

    def test_A_AI_UNSAFE_empty(self):
        """A_AI(UNSAFE) == ∅."""
        config = get_governance_config("UNSAFE")
        self.assertEqual(config.A_AI, frozenset())

    def test_containment_property(self):
        """A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅."""
        safe = get_governance_config("SAFE").A_AI
        caution = get_governance_config("CAUTION").A_AI
        unsafe = get_governance_config("UNSAFE").A_AI
        self.assertTrue(caution < safe)         # proper subset
        self.assertTrue(unsafe < caution)       # proper subset
        self.assertEqual(unsafe, frozenset())   # empty


# ═════════════════════════════════════════════════════════════════════════════
# T04  UNSAFE short-circuit — engine must NOT be invoked
# ═════════════════════════════════════════════════════════════════════════════

class TestUNSAFEShortCircuit(unittest.TestCase):

    def test_T04_UNSAFE_no_engine_invocation(self):
        """T04: UNSAFE returns AI(E)=∅ without invoking engine.reason()."""
        spy = _SpyEngine()
        result = execute_episode("UNSAFE", _repo(), _ctx(), _engine=spy)

        self.assertFalse(spy.reason_called, "engine.reason() must NOT be called for UNSAFE")
        self.assertEqual(result.advisories, [])
        self.assertEqual(result.trace.G, 0)
        self.assertIsNone(result.trace.rule_set_bound_for_state)
        self.assertIsNone(result.error)

    def test_UNSAFE_trace_fields(self):
        """UNSAFE episode trace records correct governance values."""
        result = execute_episode("UNSAFE", _repo(), _ctx())
        t = result.trace
        self.assertEqual(t.state, "UNSAFE")
        self.assertEqual(t.G, 0)
        self.assertEqual(t.A_AI, frozenset())
        self.assertEqual(t.active_rule_ids, [])
        self.assertEqual(t.fired_rule_ids, [])
        self.assertFalse(t.configuration_failure)
        self.assertFalse(t.evaluation_failure)


# ═════════════════════════════════════════════════════════════════════════════
# T05–T07  Rule-set selection
# ═════════════════════════════════════════════════════════════════════════════

class TestRuleSetSelection(unittest.TestCase):

    def setUp(self):
        self.safe_rule = _test_rule("TS-SAFE-1", "SAFE",
                                    [ConditionPredicate("vessel_category", "==", "small")], "Go")
        self.caution_rule = _test_rule("TS-CAUTION-1", "CAUTION",
                                       [ConditionPredicate("vessel_category", "==", "small")], "Delay")
        self.disabled_rule = _test_rule("TS-DISABLED-1", "CAUTION",
                                        [ConditionPredicate("vessel_category", "==", "small")],
                                        "Delay", enabled=False)
        self.repo = _repo(self.safe_rule, self.caution_rule, self.disabled_rule)

    def test_T05_SAFE_selects_only_SAFE_rules(self):
        """T05: select_rule_set returns only SAFE rules for state=SAFE."""
        rs = select_rule_set(self.repo, "SAFE")
        self.assertIn(self.safe_rule, rs)
        self.assertNotIn(self.caution_rule, rs)
        self.assertNotIn(self.disabled_rule, rs)

    def test_T06_CAUTION_selects_only_CAUTION_rules(self):
        """T06: select_rule_set returns only enabled CAUTION rules for state=CAUTION."""
        rs = select_rule_set(self.repo, "CAUTION")
        self.assertIn(self.caution_rule, rs)
        self.assertNotIn(self.safe_rule, rs)
        self.assertNotIn(self.disabled_rule, rs)

    def test_T07_disabled_rules_excluded(self):
        """T07: disabled rules are never included in RS(S)."""
        rs = select_rule_set(self.repo, "CAUTION")
        rule_ids = [r.rule_id for r in rs]
        self.assertNotIn("TS-DISABLED-1", rule_ids)

    def test_RS_UNSAFE_empty(self):
        """RS(UNSAFE) = ∅ always."""
        rs = select_rule_set(self.repo, "UNSAFE")
        self.assertEqual(rs, [])


# ═════════════════════════════════════════════════════════════════════════════
# T08  A_AI containment violation
# ═════════════════════════════════════════════════════════════════════════════

class TestA_AIContainmentViolation(unittest.TestCase):

    def test_T08_A_AI_containment_violation_rejected(self):
        """T08: validate_rule_set raises ConfigurationError when ConclusionTypes ⊄ A_AI(S)."""
        # DepartureTime is NOT in A_AI(CAUTION) = {Go, Delay}
        bad_rule = _test_rule("TS-BAD-1", "CAUTION",
                              [ConditionPredicate("vessel_category", "==", "small")],
                              "DepartureTime")
        # Must change applicable_state to bypass Rule constructor validation:
        # Rule restricts to SAFE/CAUTION. DepartureTime is in R so Rule allows it.
        # The A_AI containment check in validate_rule_set is separate.
        with self.assertRaises(ConfigurationError) as cm:
            validate_rule_set([bad_rule], "CAUTION", "test-ep")
        self.assertEqual(cm.exception.failure_type, "A_AI_CONTAINMENT")
        self.assertIn("TS-BAD-1", cm.exception.offending_rules)

    def test_T08_containment_in_execute_episode(self):
        """T08: execute_episode returns configuration_failure=True for A_AI violation."""
        bad_rule = _test_rule("TS-BAD-2", "CAUTION",
                              [ConditionPredicate("vessel_category", "==", "small")],
                              "DepartureTime")
        repo = _repo(bad_rule)
        result = execute_episode("CAUTION", repo, _ctx())
        self.assertTrue(result.trace.configuration_failure)
        self.assertFalse(result.trace.evaluation_failure)
        self.assertEqual(result.advisories, [])
        self.assertIsInstance(result.error, ConfigurationError)


# ═════════════════════════════════════════════════════════════════════════════
# T09–T12  V1–V4 structural validation
# ═════════════════════════════════════════════════════════════════════════════

class TestStructuralValidation(unittest.TestCase):

    def _caution_rule_with_pred(self, rule_id, pred):
        return Rule(
            rule_id=rule_id,
            applicable_state="CAUTION",
            conditions=(pred,),
            conclusion_type="Delay",
            conclusion_payload={"reason": "test"},
            provenance="TEST-ONLY",
            enabled=True,
        )

    def test_T09_V1_unknown_variable_FT11(self):
        """T09: V1 — unknown variable in predicate → ConfigurationError F-T-11."""
        rule = self._caution_rule_with_pred(
            "TS-V1",
            ConditionPredicate("nonexistent_field", "==", "value"),
        )
        with self.assertRaises(ConfigurationError) as cm:
            validate_rule_set([rule], "CAUTION", "test-ep")
        self.assertEqual(cm.exception.failure_type, "F-T-11")

    def test_T09_V1_in_execute_episode(self):
        """T09: V1 failure propagates through execute_episode as configuration_failure."""
        rule = self._caution_rule_with_pred(
            "TS-V1b",
            ConditionPredicate("nonexistent_field", "==", "x"),
        )
        result = execute_episode("CAUTION", _repo(rule), _ctx())
        self.assertTrue(result.trace.configuration_failure)
        self.assertFalse(result.trace.evaluation_failure)
        self.assertEqual(result.advisories, [])

    def test_T10_V2_type_mismatch_FT04(self):
        """T10: V2 — value type incompatible with declared field type → F-T-04."""
        # resolved_m is "str" kind; passing int 42 is a type mismatch
        rule = self._caution_rule_with_pred(
            "TS-V2",
            ConditionPredicate("resolved_m", "==", 42),
        )
        with self.assertRaises(ConfigurationError) as cm:
            validate_rule_set([rule], "CAUTION", "test-ep")
        self.assertEqual(cm.exception.failure_type, "F-T-04")

    def test_T10_V2_null_operator_non_none_value_FT04(self):
        """T10: V2 — is_none operator with non-None value → F-T-04."""
        rule = self._caution_rule_with_pred(
            "TS-V2b",
            ConditionPredicate("resolved_m", "is_none", "oops"),
        )
        with self.assertRaises(ConfigurationError) as cm:
            validate_rule_set([rule], "CAUTION", "test-ep")
        self.assertEqual(cm.exception.failure_type, "F-T-04")

    def test_T11_V3_invalid_operator_FT05(self):
        """T11: V3 — numeric ordering operator on string field → F-T-05."""
        # resolved_m is "str" kind; "<" operator is not valid for string fields
        rule = self._caution_rule_with_pred(
            "TS-V3",
            ConditionPredicate("resolved_m", "<", "advisory"),
        )
        with self.assertRaises(ConfigurationError) as cm:
            validate_rule_set([rule], "CAUTION", "test-ep")
        self.assertEqual(cm.exception.failure_type, "F-T-05")

    def test_T12_V4_invalid_categorical_value_FT06(self):
        """T12: V4 — categorical value outside declared domain → F-T-06."""
        # vessel_category domain is {"small","medium","big"}; "giant" is outside it
        rule = self._caution_rule_with_pred(
            "TS-V4",
            ConditionPredicate("vessel_category", "==", "giant"),
        )
        with self.assertRaises(ConfigurationError) as cm:
            validate_rule_set([rule], "CAUTION", "test-ep")
        self.assertEqual(cm.exception.failure_type, "F-T-06")

    def test_V1_before_V2_ordering(self):
        """V1 must run before V2 — unknown variable should raise F-T-11, not F-T-04."""
        # Unknown variable with type-incompatible value: F-T-11 must come first
        rule = self._caution_rule_with_pred(
            "TS-V1V2",
            ConditionPredicate("totally_unknown_var", "==", 999),
        )
        with self.assertRaises(ConfigurationError) as cm:
            validate_rule_set([rule], "CAUTION", "test-ep")
        self.assertEqual(cm.exception.failure_type, "F-T-11",
                         "V1 (F-T-11) must fire before V2 (F-T-04)")

    def test_V4_kappa_out_of_domain(self):
        """V4 — resolved_r_kappa domain is {0,1}; value 5 is outside domain → F-T-06."""
        rule = self._caution_rule_with_pred(
            "TS-V4b",
            ConditionPredicate("resolved_r_kappa", "==", 5),
        )
        with self.assertRaises(ConfigurationError) as cm:
            validate_rule_set([rule], "CAUTION", "test-ep")
        self.assertEqual(cm.exception.failure_type, "F-T-06")


# ═════════════════════════════════════════════════════════════════════════════
# T13–T14  Rule firing semantics — TRUE / FALSE
# ═════════════════════════════════════════════════════════════════════════════

class TestRuleFiringSemantics(unittest.TestCase):

    def test_T13_all_predicates_TRUE_rule_fires(self):
        """T13: all predicates TRUE → rule fires, advisory emitted."""
        rule = _test_rule(
            "TS-FIRE-1", "CAUTION",
            [ConditionPredicate("vessel_category", "==", "small")],
            "Delay",
        )
        ctx = _ctx(vessel_category="small")
        result = execute_episode("CAUTION", _repo(rule), ctx)
        self.assertEqual(len(result.advisories), 1)
        self.assertEqual(result.advisories[0].type, "Delay")
        self.assertEqual(result.advisories[0].rule_id, "TS-FIRE-1")
        self.assertIn("TS-FIRE-1", result.trace.fired_rule_ids)

    def test_T13_multiple_predicates_all_TRUE_fires(self):
        """T13: conjunctive predicates — rule fires only when ALL are TRUE."""
        rule = _test_rule(
            "TS-FIRE-2", "CAUTION",
            [
                ConditionPredicate("vessel_category", "==", "small"),
                ConditionPredicate("resolved_r_kappa", "==", 0),
            ],
            "Delay",
        )
        ctx = _ctx(vessel_category="small", resolved_r_kappa=0)
        result = execute_episode("CAUTION", _repo(rule), ctx)
        self.assertEqual(len(result.advisories), 1)

    def test_T14_any_predicate_FALSE_normal_no_fire(self):
        """T14: any predicate FALSE → normal no-fire (not evaluation failure)."""
        rule = _test_rule(
            "TS-NOFIRE-1", "CAUTION",
            [ConditionPredicate("vessel_category", "==", "big")],  # ctx has "small"
            "Delay",
        )
        ctx = _ctx(vessel_category="small")
        result = execute_episode("CAUTION", _repo(rule), ctx)
        self.assertEqual(result.advisories, [])
        self.assertFalse(result.trace.evaluation_failure)
        self.assertFalse(result.trace.configuration_failure)
        self.assertIsNone(result.error)
        self.assertEqual(result.trace.fired_rule_ids, [])

    def test_T14_second_predicate_FALSE_no_fire(self):
        """T14: second predicate FALSE → no-fire even though first was TRUE."""
        rule = _test_rule(
            "TS-NOFIRE-2", "CAUTION",
            [
                ConditionPredicate("vessel_category", "==", "small"),  # TRUE
                ConditionPredicate("vessel_category", "==", "big"),    # FALSE
            ],
            "Delay",
        )
        ctx = _ctx(vessel_category="small")
        result = execute_episode("CAUTION", _repo(rule), ctx)
        self.assertEqual(result.advisories, [])
        self.assertFalse(result.trace.evaluation_failure)


# ═════════════════════════════════════════════════════════════════════════════
# T15–T20  Predicate ERROR — distinct from FALSE, episode refusal
# ═════════════════════════════════════════════════════════════════════════════

class TestPredicateErrorSemantics(unittest.TestCase):
    """Tests T15–T20 verify that ERROR ≠ FALSE and causes episode refusal (Model C+D)."""

    def _make_error_context(self) -> DecisionContext:
        """Context where resolved_w=None triggers MALFORMED_VALUE on a < comparison."""
        return _ctx(resolved_w=None)

    def _make_error_rule(self, rule_id: str = "TS-ERR-1") -> Rule:
        """Rule with resolved_w < 21.6 — passes V1-V4 but errors at runtime when resolved_w=None."""
        return Rule(
            rule_id=rule_id,
            applicable_state="CAUTION",
            conditions=(ConditionPredicate("resolved_w", "<", 21.6),),
            conclusion_type="Delay",
            conclusion_payload={"reason": "TEST-ONLY error trigger rule"},
            provenance="TEST-ONLY — triggers MALFORMED_VALUE for T15-T20",
            enabled=True,
        )

    def test_T15_ERROR_distinct_from_FALSE_via_evaluate_predicate(self):
        """T15: evaluate_predicate returns ERROR ≠ FALSE when actual value is None."""
        pred = ConditionPredicate("resolved_w", "<", 21.6)
        ctx_null = _ctx(resolved_w=None)
        ctx_false = _ctx(resolved_w=25.0)  # 25.0 < 21.6 is FALSE

        result_error, cat_error, _ = evaluate_predicate(pred, ctx_null)
        result_false, cat_false, _ = evaluate_predicate(pred, ctx_false)

        self.assertEqual(result_error, PredicateResult.ERROR)
        self.assertEqual(result_false, PredicateResult.FALSE)
        self.assertNotEqual(result_error, result_false,
                            "ERROR must be structurally distinct from FALSE")
        self.assertNotEqual(result_error, PredicateResult.TRUE)
        self.assertEqual(cat_error, FailureCategory.MALFORMED_VALUE)

    def test_T15_ERROR_distinct_from_TRUE(self):
        """T15: ERROR ≠ TRUE — evaluate_predicate with type mismatch returns ERROR not TRUE."""
        pred = ConditionPredicate("resolved_w", "<", 21.6)
        ctx_null = _ctx(resolved_w=None)

        result, cat, _ = evaluate_predicate(pred, ctx_null)
        self.assertNotEqual(result, PredicateResult.TRUE)
        self.assertEqual(result, PredicateResult.ERROR)

    def test_T16_predicate_ERROR_causes_episode_refusal(self):
        """T16: predicate ERROR → episode refuses to generate any advisory."""
        rule = self._make_error_rule()
        result = execute_episode("CAUTION", _repo(rule), self._make_error_context())
        self.assertEqual(result.advisories, [], "No advisory must be emitted on ERROR")

    def test_T17_runtime_failure_evaluation_failure_true(self):
        """T17: runtime predicate ERROR → trace.evaluation_failure == True."""
        rule = self._make_error_rule()
        result = execute_episode("CAUTION", _repo(rule), self._make_error_context())
        self.assertTrue(result.trace.evaluation_failure)

    def test_T18_runtime_failure_AI_empty(self):
        """T18: runtime failure → AI(E) = ∅."""
        rule = self._make_error_rule()
        result = execute_episode("CAUTION", _repo(rule), self._make_error_context())
        self.assertEqual(result.advisories, [])

    def test_T19_runtime_failure_does_not_mutate_S(self):
        """T19: runtime failure does not change S — trace.state equals input state."""
        rule = self._make_error_rule()
        input_state = "CAUTION"
        result = execute_episode(input_state, _repo(rule), self._make_error_context())
        self.assertEqual(result.trace.state, input_state)
        self.assertEqual(result.trace.S_new, input_state)

    def test_T20_no_partial_advisory_on_evaluation_failure(self):
        """T20: rule A → ERROR, rule B → TRUE: no advisory survives — AI(E) = ∅."""
        rule_err = self._make_error_rule("TS-ERR-PARTIAL-1")
        rule_ok = _test_rule(
            "TS-ERR-PARTIAL-2", "CAUTION",
            [ConditionPredicate("vessel_category", "==", "small")],  # always TRUE
            "Delay",
        )
        ctx = _ctx(resolved_w=None, vessel_category="small")  # rule_err will ERROR
        result = execute_episode("CAUTION", _repo(rule_err, rule_ok), ctx)
        self.assertEqual(result.advisories, [],
                         "No partial advisory must survive when any predicate returns ERROR")
        self.assertTrue(result.trace.evaluation_failure)
        self.assertEqual(result.trace.fired_rule_ids, [],
                         "fired_rule_ids must be empty when evaluation_failure=True")

    def test_failed_rule_ids_collected(self):
        """Model B: failed_rule_ids lists all rules that had ERROR predicates."""
        rule_err1 = self._make_error_rule("TS-ERR-COLL-1")
        rule_err2 = Rule(
            rule_id="TS-ERR-COLL-2",
            applicable_state="CAUTION",
            conditions=(ConditionPredicate("resolved_w", ">", 1.0),),
            conclusion_type="Delay",
            conclusion_payload={"reason": "test"},
            provenance="TEST-ONLY",
            enabled=True,
        )
        ctx = _ctx(resolved_w=None)  # both rules will ERROR
        result = execute_episode("CAUTION", _repo(rule_err1, rule_err2), ctx)
        self.assertTrue(result.trace.evaluation_failure)
        self.assertIn("TS-ERR-COLL-1", result.trace.failed_rule_ids)
        self.assertIn("TS-ERR-COLL-2", result.trace.failed_rule_ids)

    def test_numeric_conversion_failure_FT08(self):
        """F-T-08: TypeError from incompatible types → NUMERIC_CONVERSION_FAILURE."""
        # Create a context with a string where float expected (bypasses type hints)
        ctx = _ctx()
        # We must construct directly since DecisionContext is frozen
        ctx_bad = DecisionContext(
            episode_id="test-ft08",
            vessel_category="small",
            resolved_w="not_a_number",   # str injected for float field
            resolved_r_rate=2.0,
            resolved_r_kappa=0,
            resolved_m=None,
            resolved_o_wave_height=0.5,
            resolved_o_swell_period=None,
            resolved_t=10.0,
        )
        pred = ConditionPredicate("resolved_w", "<", 21.6)
        result, cat, msg = evaluate_predicate(pred, ctx_bad)
        self.assertEqual(result, PredicateResult.ERROR)
        self.assertEqual(cat, FailureCategory.NUMERIC_CONVERSION_FAILURE)


# ═════════════════════════════════════════════════════════════════════════════
# T21  Configuration failure vs evaluation failure are distinguishable
# ═════════════════════════════════════════════════════════════════════════════

class TestFailureDistinction(unittest.TestCase):

    def test_T21_config_failure_trace(self):
        """T21: configuration failure → configuration_failure=True, evaluation_failure=False."""
        # V1 violation: unknown variable
        rule = Rule(
            rule_id="TS-CFG-1",
            applicable_state="CAUTION",
            conditions=(ConditionPredicate("bad_var", "==", "x"),),
            conclusion_type="Delay",
            conclusion_payload={"reason": "test"},
            provenance="TEST-ONLY",
            enabled=True,
        )
        result = execute_episode("CAUTION", _repo(rule), _ctx())
        self.assertTrue(result.trace.configuration_failure)
        self.assertFalse(result.trace.evaluation_failure)
        self.assertIsInstance(result.error, ConfigurationError)

    def test_T21_eval_failure_trace(self):
        """T21: evaluation failure → configuration_failure=False, evaluation_failure=True."""
        rule = Rule(
            rule_id="TS-EVAL-1",
            applicable_state="CAUTION",
            conditions=(ConditionPredicate("resolved_w", "<", 21.6),),
            conclusion_type="Delay",
            conclusion_payload={"reason": "test"},
            provenance="TEST-ONLY",
            enabled=True,
        )
        result = execute_episode("CAUTION", _repo(rule), _ctx(resolved_w=None))
        self.assertFalse(result.trace.configuration_failure)
        self.assertTrue(result.trace.evaluation_failure)
        self.assertIsNone(result.error)

    def test_T21_normal_success_trace(self):
        """T21: normal success → configuration_failure=False, evaluation_failure=False."""
        rule = _test_rule("TS-OK-1", "CAUTION",
                          [ConditionPredicate("vessel_category", "==", "small")], "Delay")
        result = execute_episode("CAUTION", _repo(rule), _ctx(vessel_category="small"))
        self.assertFalse(result.trace.configuration_failure)
        self.assertFalse(result.trace.evaluation_failure)
        self.assertIsNone(result.error)

    def test_T21_normal_no_fire_trace(self):
        """T21: normal no-fire → configuration_failure=False, evaluation_failure=False, fired_rule_ids=[]."""
        rule = _test_rule("TS-NF-1", "CAUTION",
                          [ConditionPredicate("vessel_category", "==", "big")], "Delay")
        result = execute_episode("CAUTION", _repo(rule), _ctx(vessel_category="small"))
        self.assertFalse(result.trace.configuration_failure)
        self.assertFalse(result.trace.evaluation_failure)
        self.assertEqual(result.trace.fired_rule_ids, [])


# ═════════════════════════════════════════════════════════════════════════════
# T22–T23  Advisory attribution and admissibility
# ═════════════════════════════════════════════════════════════════════════════

class TestAdvisoryInvariants(unittest.TestCase):

    def test_T22_advisory_attributable_to_fired_rule(self):
        """T22: emitted advisory.rule_id matches a rule in fired_rule_ids."""
        rule = _test_rule("TS-ATTR-1", "CAUTION",
                          [ConditionPredicate("vessel_category", "==", "small")], "Delay")
        result = execute_episode("CAUTION", _repo(rule), _ctx(vessel_category="small"))
        self.assertEqual(len(result.advisories), 1)
        advisory = result.advisories[0]
        self.assertIn(advisory.rule_id, result.trace.fired_rule_ids)
        self.assertEqual(advisory.rule_id, "TS-ATTR-1")

    def test_T23_advisory_type_in_A_AI(self):
        """T23: generated advisory.type ∈ A_AI(S) for the governing state."""
        rule = _test_rule("TS-ADM-1", "CAUTION",
                          [ConditionPredicate("vessel_category", "==", "small")], "Delay")
        result = execute_episode("CAUTION", _repo(rule), _ctx(vessel_category="small"))
        gov = get_governance_config("CAUTION")
        for advisory in result.advisories:
            self.assertIn(advisory.type, gov.A_AI,
                          f"Advisory type {advisory.type!r} not in A_AI(CAUTION)={gov.A_AI!r}")

    def test_T22_no_advisory_without_fired_rule(self):
        """T22: advisory list is empty when no rules fired."""
        rule = _test_rule("TS-NOADV-1", "CAUTION",
                          [ConditionPredicate("vessel_category", "==", "big")], "Delay")
        result = execute_episode("CAUTION", _repo(rule), _ctx(vessel_category="small"))
        self.assertEqual(result.advisories, [])
        self.assertEqual(result.trace.fired_rule_ids, [])

    def test_advisory_fields_do_not_encode_human_decision(self):
        """Advisory fields must not encode automated approval, prohibition, or override."""
        advisory_fields = {f.name for f in dataclasses.fields(Advisory)}
        forbidden = {"approved", "prohibited", "override", "automated_decision",
                     "do_not_go", "cancel", "authorized", "denied"}
        overlap = advisory_fields & forbidden
        self.assertEqual(overlap, set(),
                         f"Advisory has forbidden human-authority fields: {overlap!r}")


# ═════════════════════════════════════════════════════════════════════════════
# T24  Determinism
# ═════════════════════════════════════════════════════════════════════════════

class TestDeterminism(unittest.TestCase):

    def test_T24_identical_input_produces_identical_output(self):
        """T24: given identical S, context, repository → identical AI(E) and trace fields."""
        rule = _test_rule("TS-DET-1", "CAUTION",
                          [ConditionPredicate("vessel_category", "==", "small")], "Delay")
        repo = _repo(rule)
        ctx = _ctx(vessel_category="small")

        result1 = execute_episode("CAUTION", repo, ctx)
        result2 = execute_episode("CAUTION", repo, ctx)

        self.assertEqual(
            [a.type for a in result1.advisories],
            [a.type for a in result2.advisories],
        )
        self.assertEqual(result1.trace.fired_rule_ids, result2.trace.fired_rule_ids)
        self.assertEqual(result1.trace.evaluation_failure, result2.trace.evaluation_failure)
        self.assertEqual(result1.trace.configuration_failure, result2.trace.configuration_failure)

    def test_T24_determinism_on_empty_result(self):
        """T24: deterministic no-fire result is identical across calls."""
        rule = _test_rule("TS-DET-2", "CAUTION",
                          [ConditionPredicate("vessel_category", "==", "big")], "Delay")
        repo = _repo(rule)
        ctx = _ctx(vessel_category="small")

        r1 = execute_episode("CAUTION", repo, ctx)
        r2 = execute_episode("CAUTION", repo, ctx)
        self.assertEqual(r1.advisories, r2.advisories)
        self.assertEqual(r1.trace.fired_rule_ids, r2.trace.fired_rule_ids)


# ═════════════════════════════════════════════════════════════════════════════
# T25  Human-authority boundary preserved structurally
# ═════════════════════════════════════════════════════════════════════════════

class TestHumanAuthorityBoundary(unittest.TestCase):

    def test_T25_advisory_class_no_authority_fields(self):
        """T25: Advisory dataclass has no fields encoding human decision authority."""
        advisory_fields = {f.name for f in dataclasses.fields(Advisory)}
        # These fields would encode human decisions and must not exist
        self.assertNotIn("approved", advisory_fields)
        self.assertNotIn("prohibited", advisory_fields)
        self.assertNotIn("override", advisory_fields)
        self.assertNotIn("automated_decision", advisory_fields)

    def test_T25_empty_advisory_not_prohibition(self):
        """T25: an empty advisory list is not equivalent to a prohibition.

        The absence of advisories says nothing about whether departure is safe or permitted.
        No 'Do Not Go' advisory may be emitted.
        """
        # UNSAFE state: AI(E) = ∅
        result_unsafe = execute_episode("UNSAFE", _repo(), _ctx())
        self.assertEqual(result_unsafe.advisories, [])
        # Verify there is no 'Do Not Go' or prohibition type advisory
        for adv in result_unsafe.advisories:
            self.assertNotIn("DoNotGo", adv.type)
            self.assertNotIn("Prohibited", adv.type)

    def test_T25_Go_advisory_not_departure_approval(self):
        """T25: Go advisory type does not encode departure approval."""
        # Go is in A_AI(SAFE) — verify the type string itself is not 'Approved' or similar
        self.assertIn("Go", get_governance_config("SAFE").A_AI)
        # The Advisory class has no 'approved' field
        advisory_fields = {f.name for f in dataclasses.fields(Advisory)}
        self.assertNotIn("approved", advisory_fields)

    def test_T25_UNSAFE_no_Do_Not_Go_advisory(self):
        """T25: UNSAFE path emits no advisory — including no 'Do Not Go'."""
        result = execute_episode("UNSAFE", _repo(), _ctx())
        # Structural check: result.advisories is empty
        self.assertEqual(result.advisories, [])


# ═════════════════════════════════════════════════════════════════════════════
# Additional: Fidelity trace integrity
# ═════════════════════════════════════════════════════════════════════════════

class TestFidelityTraceIntegrity(unittest.TestCase):

    def test_trace_always_present(self):
        """FidelityTrace is always returned — never None — for any episode outcome."""
        # UNSAFE
        r = execute_episode("UNSAFE", _repo(), _ctx())
        self.assertIsNotNone(r.trace)

        # Configuration failure
        bad_rule = Rule("TS-TRC-1", "CAUTION",
                        (ConditionPredicate("bad_var", "==", "x"),),
                        "Delay", {"reason": "t"}, "TEST-ONLY", True)
        r2 = execute_episode("CAUTION", _repo(bad_rule), _ctx())
        self.assertIsNotNone(r2.trace)

        # Normal success
        ok_rule = _test_rule("TS-TRC-2", "CAUTION",
                             [ConditionPredicate("vessel_category", "==", "small")], "Delay")
        r3 = execute_episode("CAUTION", _repo(ok_rule), _ctx())
        self.assertIsNotNone(r3.trace)

    def test_trace_rule_set_bound_for_state_equals_S_new(self):
        """F3 precondition: rule_set_bound_for_state == S_new in valid SAFE/CAUTION episodes."""
        ok_rule = _test_rule("TS-TRC-3", "CAUTION",
                             [ConditionPredicate("vessel_category", "==", "small")], "Delay")
        result = execute_episode("CAUTION", _repo(ok_rule), _ctx())
        t = result.trace
        self.assertEqual(t.rule_set_bound_for_state, t.S_new)

    def test_trace_active_rule_conclusion_types_subset_A_AI(self):
        """F1 precondition: ConclusionTypes(RS_used) ⊆ A_AI(S_new)."""
        ok_rule = _test_rule("TS-TRC-4", "CAUTION",
                             [ConditionPredicate("vessel_category", "==", "small")], "Delay")
        result = execute_episode("CAUTION", _repo(ok_rule), _ctx())
        t = result.trace
        self.assertTrue(t.active_rule_conclusion_types <= t.A_AI)

    def test_trace_generated_advisory_types_subset_A_AI(self):
        """F1 precondition: all generated_advisory_types ∈ A_AI(S)."""
        ok_rule = _test_rule("TS-TRC-5", "CAUTION",
                             [ConditionPredicate("vessel_category", "==", "small")], "Delay")
        result = execute_episode("CAUTION", _repo(ok_rule), _ctx())
        t = result.trace
        for advisory_type in t.generated_advisory_types:
            self.assertIn(advisory_type, t.A_AI)

    def test_trace_S_new_equals_state(self):
        """S_new field equals the state field in all outcomes."""
        for state in ("SAFE", "CAUTION", "UNSAFE"):
            result = execute_episode(state, _repo(), _ctx())
            self.assertEqual(result.trace.S_new, state)
            self.assertEqual(result.trace.state, state)


# ═════════════════════════════════════════════════════════════════════════════
# Additional: Canonical rule repository
# ═════════════════════════════════════════════════════════════════════════════

class TestCanonicalRepository(unittest.TestCase):

    def test_canonical_repo_contains_R_CAUTION_001(self):
        """R-CAUTION-001 is the only loaded canonical rule."""
        repo = build_canonical_repository()
        rule_ids = [r.rule_id for r in repo.rules]
        self.assertIn("R-CAUTION-001", rule_ids)

    def test_canonical_repo_R_CAUTION_001_is_enabled(self):
        """R-CAUTION-001 is enabled."""
        repo = build_canonical_repository()
        rule = next(r for r in repo.rules if r.rule_id == "R-CAUTION-001")
        self.assertTrue(rule.enabled)

    def test_canonical_repo_R_CAUTION_001_passes_V1_to_V4(self):
        """R-CAUTION-001 passes all V1–V4 structural validation checks."""
        repo = build_canonical_repository()
        caution_rs = select_rule_set(repo, "CAUTION")
        # Should not raise ConfigurationError
        validate_rule_set(caution_rs, "CAUTION", "test-canon-ep")

    def test_canonical_repo_deferred_rules_absent(self):
        """R-SAFE-001 and R-CAUTION-002/003/004 are NOT loaded."""
        repo = build_canonical_repository()
        rule_ids = [r.rule_id for r in repo.rules]
        for deferred_id in DEFERRED_RULES:
            self.assertNotIn(deferred_id, rule_ids)

    def test_OPEN_L3_1C_preserved_no_DepartureTime_rule(self):
        """OPEN-L3-1C preserved: no rule producing DepartureTime is loaded."""
        repo = build_canonical_repository()
        dt_rules = [r for r in repo.rules if r.conclusion_type == "DepartureTime"]
        self.assertEqual(dt_rules, [])

    def test_OPEN_L3_1D_preserved_no_Duration_rule(self):
        """OPEN-L3-1D preserved: no rule producing Duration is loaded."""
        repo = build_canonical_repository()
        dur_rules = [r for r in repo.rules if r.conclusion_type == "Duration"]
        self.assertEqual(dur_rules, [])

    def test_GAP_03_preserved_no_CAUTION_Go_rule(self):
        """GAP-03 preserved: no rule producing Go under CAUTION state exists."""
        repo = build_canonical_repository()
        caution_go = [
            r for r in repo.rules
            if r.applicable_state == "CAUTION" and r.conclusion_type == "Go"
        ]
        self.assertEqual(caution_go, [])

    def test_R_CAUTION_001_fires_on_advisory_m(self):
        """R-CAUTION-001 fires when resolved_m == 'advisory'."""
        repo = build_canonical_repository()
        ctx = _ctx(resolved_m="advisory")
        result = execute_episode("CAUTION", repo, ctx)
        self.assertEqual(len(result.advisories), 1)
        self.assertEqual(result.advisories[0].type, "Delay")
        self.assertEqual(result.advisories[0].rule_id, "R-CAUTION-001")

    def test_R_CAUTION_001_does_not_fire_when_m_is_None(self):
        """R-CAUTION-001 does not fire when resolved_m is None (D={m} replay scenario)."""
        repo = build_canonical_repository()
        ctx = _ctx(resolved_m=None)
        result = execute_episode("CAUTION", repo, ctx)
        self.assertEqual(result.advisories, [])
        self.assertFalse(result.trace.evaluation_failure)

    def test_R_CAUTION_001_does_not_fire_on_warning_level(self):
        """R-CAUTION-001 is specific to 'advisory'; does not fire on 'warning' or 'alert'."""
        repo = build_canonical_repository()
        for m_level in ("warning", "alert", "none"):
            ctx = _ctx(resolved_m=m_level)
            result = execute_episode("CAUTION", repo, ctx)
            self.assertEqual(result.advisories, [],
                             f"R-CAUTION-001 should not fire for resolved_m={m_level!r}")


# ═════════════════════════════════════════════════════════════════════════════
# Additional: OPEN-L3-3 Resolution B structural check
# ═════════════════════════════════════════════════════════════════════════════

class TestOpenL3_3ResolutionB(unittest.TestCase):
    """OPEN-L3-3 is CLOSED under Resolution B (Batch 2, 2026-09-11).

    Resolution B: S=CAUTION ∧ Go ∈ AI(E) → Present(Go, caution_qualifier)
    NOT: S=CAUTION → Go ∈ AI(E)

    Batch 3 engine verification:
      - No rule in canonical RS_candidate(CAUTION) produces Go.
      - Go ∈ A_AI(CAUTION) (admissibility is preserved, not rule existence).
      - No synthetic Go advisory is created merely to exercise the presentation path.
    """

    def test_no_CAUTION_Go_rule_in_canonical_repo(self):
        """No rule producing Go exists in RS_candidate(CAUTION)."""
        repo = build_canonical_repository()
        caution_go = [
            r for r in repo.rules
            if r.applicable_state == "CAUTION" and r.conclusion_type == "Go"
        ]
        self.assertEqual(caution_go, [],
                         "No CAUTION→Go rule may exist (GAP-03; OPEN-L3-3 Resolution B)")

    def test_Go_admissible_in_CAUTION_A_AI(self):
        """Go ∈ A_AI(CAUTION): admissibility preserved without implying rule existence."""
        self.assertIn("Go", get_governance_config("CAUTION").A_AI)

    def test_no_synthetic_Go_advisory_emitted(self):
        """Engine does not synthesize a Go advisory for CAUTION state merely because Go ∈ A_AI."""
        repo = build_canonical_repository()
        result = execute_episode("CAUTION", repo, _ctx())
        go_advisories = [a for a in result.advisories if a.type == "Go"]
        self.assertEqual(go_advisories, [],
                         "No synthetic Go advisory may be emitted under CAUTION (Resolution B)")


# ═════════════════════════════════════════════════════════════════════════════
# Additional: Layer 2 not reimplemented
# ═════════════════════════════════════════════════════════════════════════════

class TestLayer2NotReimplemented(unittest.TestCase):
    """Batch 3 task §30: Layer 3 must not reimplement Layer 2 classifiers."""

    def test_no_g_functions_imported_in_governance_modules(self):
        """Governance modules do not import canonical scripts (g_t, g_o, etc.)."""
        import governance.rule as rule_mod
        import governance.rule_set_provider as rsp_mod
        import governance.reasoning_engine as re_mod
        import governance.reasoning_episode as rep_mod

        for mod in (rule_mod, rsp_mod, re_mod, rep_mod):
            for attr in ("canonical_gt", "canonical_figures", "historical_replay",
                         "g_t", "g_w", "g_r", "g_m", "g_o"):
                self.assertFalse(
                    hasattr(mod, attr),
                    f"Module {mod.__name__} must not import {attr!r} (Layer 2 classifier)"
                )


# ═════════════════════════════════════════════════════════════════════════════
# Additional: Canonical files not modified
# ═════════════════════════════════════════════════════════════════════════════

class TestCanonicalFilesIntegrity(unittest.TestCase):
    """Batch 3 task §31: canonical files must not be modified."""

    def test_appendix_c_exists(self):
        """appendix-c-formalisation.md exists at canonical path."""
        import os
        path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "docs", "canonical", "appendix-c-formalisation.md"
        )
        self.assertTrue(os.path.exists(path), f"Canonical file not found: {path}")

    def test_architecture_illustration_exists(self):
        """architecture-illustration.md exists at canonical path."""
        import os
        path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "docs", "canonical", "architecture-illustration.md"
        )
        self.assertTrue(os.path.exists(path), f"Canonical file not found: {path}")


# ═════════════════════════════════════════════════════════════════════════════
# Additional: Rule constructor validation
# ═════════════════════════════════════════════════════════════════════════════

class TestRuleConstructorValidation(unittest.TestCase):

    def test_invalid_applicable_state_rejected(self):
        """Rule constructor rejects applicable_state not in {SAFE, CAUTION}."""
        with self.assertRaises(ValueError):
            Rule("id", "UNSAFE", (), "Go", {}, "prov", True)

    def test_invalid_conclusion_type_rejected(self):
        """Rule constructor rejects conclusion_type not in R."""
        with self.assertRaises(ValueError):
            Rule("id", "SAFE", (), "DoNotGo", {}, "prov", True)

    def test_empty_provenance_rejected(self):
        """Rule constructor rejects empty provenance string."""
        with self.assertRaises(ValueError):
            Rule("id", "SAFE", (), "Go", {}, "", True)

    def test_non_tuple_conditions_rejected(self):
        """Rule constructor rejects conditions that are not a tuple."""
        with self.assertRaises(TypeError):
            Rule("id", "SAFE", [], "Go", {}, "prov", True)


# ═════════════════════════════════════════════════════════════════════════════
# Additional: SAFE episode with test rule
# ═════════════════════════════════════════════════════════════════════════════

class TestSAFEEpisode(unittest.TestCase):

    def test_SAFE_episode_executes_correctly(self):
        """SAFE episode uses only SAFE rules; Go advisories are admissible."""
        rule = _test_rule("TS-SAFE-EP-1", "SAFE",
                          [ConditionPredicate("vessel_category", "==", "small")], "Go")
        result = execute_episode("SAFE", _repo(rule), _ctx(vessel_category="small"))
        self.assertEqual(len(result.advisories), 1)
        self.assertEqual(result.advisories[0].type, "Go")
        gov = get_governance_config("SAFE")
        self.assertIn(result.advisories[0].type, gov.A_AI)

    def test_SAFE_episode_does_not_use_CAUTION_rules(self):
        """SAFE episode does not include CAUTION rules in RS(SAFE)."""
        caution_rule = _test_rule("TS-SAFE-EP-CAUTION", "CAUTION",
                                  [ConditionPredicate("vessel_category", "==", "small")], "Delay")
        safe_rule = _test_rule("TS-SAFE-EP-SAFE", "SAFE",
                               [ConditionPredicate("vessel_category", "==", "small")], "Go")
        repo = _repo(safe_rule, caution_rule)
        result = execute_episode("SAFE", repo, _ctx(vessel_category="small"))
        active_ids = result.trace.active_rule_ids
        self.assertIn("TS-SAFE-EP-SAFE", active_ids)
        self.assertNotIn("TS-SAFE-EP-CAUTION", active_ids)


# ═════════════════════════════════════════════════════════════════════════════
# Additional: is_none / is_not_none operator tests
# ═════════════════════════════════════════════════════════════════════════════

class TestNullOperators(unittest.TestCase):

    def test_is_none_TRUE_when_field_is_None(self):
        """is_none returns TRUE when the field value is None."""
        pred = ConditionPredicate("resolved_m", "is_none", None)
        ctx = _ctx(resolved_m=None)
        result, _, _ = evaluate_predicate(pred, ctx)
        self.assertEqual(result, PredicateResult.TRUE)

    def test_is_none_FALSE_when_field_has_value(self):
        """is_none returns FALSE when the field value is not None."""
        pred = ConditionPredicate("resolved_m", "is_none", None)
        ctx = _ctx(resolved_m="advisory")
        result, _, _ = evaluate_predicate(pred, ctx)
        self.assertEqual(result, PredicateResult.FALSE)

    def test_is_not_none_TRUE_when_field_has_value(self):
        """is_not_none returns TRUE when the field value is not None."""
        pred = ConditionPredicate("resolved_m", "is_not_none", None)
        ctx = _ctx(resolved_m="advisory")
        result, _, _ = evaluate_predicate(pred, ctx)
        self.assertEqual(result, PredicateResult.TRUE)

    def test_is_not_none_FALSE_when_field_is_None(self):
        """is_not_none returns FALSE when the field value is None."""
        pred = ConditionPredicate("resolved_m", "is_not_none", None)
        ctx = _ctx(resolved_m=None)
        result, _, _ = evaluate_predicate(pred, ctx)
        self.assertEqual(result, PredicateResult.FALSE)

    def test_is_none_operator_in_rule_passes_V2(self):
        """is_none operator with value=None passes V2 validation."""
        rule = Rule("TS-NULL-1", "CAUTION",
                    (ConditionPredicate("resolved_m", "is_none", None),),
                    "Delay", {"reason": "test"}, "TEST-ONLY", True)
        # Should not raise
        validate_rule_set([rule], "CAUTION", "test-ep")


if __name__ == "__main__":
    unittest.main(verbosity=2)
