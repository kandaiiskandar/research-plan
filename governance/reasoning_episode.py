"""Governed episode orchestration — combined Algorithm 3 + Algorithm 4 pipeline.

Authority: layer3-prototype-specification.md §9; algorithm-specification.md §17–§20.
Episode result structure: layer3-prototype-specification.md §9.2.

execute_episode() implements the nine-step orchestration:
  1. Establish governance configuration from state
  2. If G(S) == 0 (UNSAFE): return empty set with trace — no reasoning
  3. Select RS_candidate(S) from repository
  4. Validate RS_candidate (A_AI containment + V1–V4)
  5. Supply RS(S)
  6. engine.reason(context, RS(S))
  7. Produce AI(E)
  8. Emit fidelity trace
  9. Return EpisodeResult

Layer 3 receives S from the caller. It never computes or mutates S.
"""
from __future__ import annotations

import dataclasses
from typing import Optional

from .rule import ConfigurationError
from .rule_repository import RuleRepository
from .rule_set_provider import (
    GovernanceConfig, get_governance_config, select_rule_set, validate_rule_set,
)
from .reasoning_engine import ReasoningEngine, FailureCategory
from .fidelity_trace import FidelityTrace

# Re-export GovernanceConfig from rule_set_provider per layer3-prototype-specification.md §9.1
__all__ = [
    "GovernanceConfig",
    "DecisionContext",
    "ReasoningEpisode",
    "EpisodeResult",
    "execute_episode",
]


# ── DecisionContext ───────────────────────────────────────────────────────────

@dataclasses.dataclass(frozen=True)
class DecisionContext:
    """Resolved environmental state as received from the upstream classifier.

    Corresponds directly to canonical condition components C = {w, r, m, o, t}
    plus vessel category v. None values indicate excluded (D-set) or faulted (⊥)
    components.

    This does NOT extend canonical E. No new scientific variable is introduced here.
    See layer3-prototype-specification.md §7.

    If a future batch identifies implementation-level inputs beyond canonical E,
    they must be documented in §7 explicitly — not silently added here.
    """

    episode_id: str
    vessel_category: str              # v ∈ {"small","medium","big"} — configured parameter

    # Resolved component values from ρ_{D,τ} — None where excluded or faulted
    resolved_w: Optional[float]                 # wind speed, knots; None if w faulted
    resolved_r_rate: Optional[float]            # rainfall rate, mm/hr; None if r excluded/faulted
    resolved_r_kappa: Optional[int]             # thunderstorm indicator κ ∈ {0,1}; None if r excluded/faulted
    resolved_m: Optional[str]                   # marine warning level; None (D={m} in replay)
    resolved_o_wave_height: Optional[float]     # wave height, metres; None if o faulted
    resolved_o_swell_period: Optional[float]    # swell period, seconds; may be None (not read by g_o)
    resolved_t: Optional[float]                 # time of day, hours [0,24); None only if t faulted


# ── ReasoningEpisode ──────────────────────────────────────────────────────────

@dataclasses.dataclass
class ReasoningEpisode:
    """Container grouping all fields for one governed decision episode.

    Invariant: all four fields belong to the same classification event.
    No field from a previous episode may carry over.
    """
    state: str                    # S ∈ {"SAFE","CAUTION","UNSAFE"}
    governance: GovernanceConfig  # G(S) and A_AI(S)
    rule_set: list                # list[Rule] — RS(S) as validated and supplied
    context: DecisionContext


# ── EpisodeResult ─────────────────────────────────────────────────────────────

@dataclasses.dataclass
class EpisodeResult:
    """Return value of execute_episode().

    advisories: empty on UNSAFE, configuration failure, evaluation failure, or no rules firing.
    trace:      always present — never None.
    error:      ConfigurationError if configuration failed; None on success or evaluation failure.

    Distinguishing normal no-fire from failure:
      advisories==[], trace.evaluation_failure==False, error==None
        → normal: no rule in RS(S) matched the current context
      advisories==[], trace.evaluation_failure==True, error==None
        → evaluation failure: predicate ERROR occurred during reasoning
      advisories==[], trace.configuration_failure==True, error is ConfigurationError
        → configuration failure: rule set invalid before reasoning began
    """
    advisories: list          # list[Advisory]
    trace: FidelityTrace      # always present
    error: Optional[Exception]  # ConfigurationError or None


# ── execute_episode ───────────────────────────────────────────────────────────

def execute_episode(
    state: str,
    repository: RuleRepository,
    context: DecisionContext,
    s_old: Optional[str] = None,
    _engine: Optional[ReasoningEngine] = None,
) -> EpisodeResult:
    """Governed episode orchestration (Algorithm 3 + Algorithm 4).

    state:      S ∈ {"SAFE","CAUTION","UNSAFE"} — supplied by the caller, never computed here.
    repository: the configured rule repository.
    context:    resolved DecisionContext from the upstream classifier.
    s_old:      state of the preceding episode (for F3 traceability); None if first episode.
    _engine:    optional engine injection for structural testing (default: ReasoningEngine()).

    Returns EpisodeResult with trace always populated.
    """
    engine = _engine if _engine is not None else ReasoningEngine()

    # ── Step 1: establish governance configuration ────────────────────────────
    try:
        gov_config = get_governance_config(state)
    except ConfigurationError as exc:
        exc.episode_id = context.episode_id
        trace = _make_trace(
            episode_id=context.episode_id,
            state=state,
            G=0,
            A_AI=frozenset(),
            active_rule_ids=[],
            active_rule_conclusion_types=frozenset(),
            fired_rule_ids=[],
            generated_advisory_types=[],
            configuration_failure=True,
            S_old=s_old,
            S_new=state,
            rule_set_bound_for_state=None,
            evaluation_failure=False,
            failed_rule_ids=[],
            failure_category=None,
        )
        return EpisodeResult(advisories=[], trace=trace, error=exc)

    # ── Step 2: UNSAFE gate-off — G(S) = 0 → AI(E) = ∅, no RS, no reasoning ─
    if gov_config.G == 0:
        trace = _make_trace(
            episode_id=context.episode_id,
            state=state,
            G=0,
            A_AI=frozenset(),
            active_rule_ids=[],
            active_rule_conclusion_types=frozenset(),
            fired_rule_ids=[],
            generated_advisory_types=[],
            configuration_failure=False,
            S_old=s_old,
            S_new=state,
            rule_set_bound_for_state=None,  # no RS selected for UNSAFE
            evaluation_failure=False,
            failed_rule_ids=[],
            failure_category=None,
        )
        return EpisodeResult(advisories=[], trace=trace, error=None)

    # ── Step 3: select RS_candidate(S) ───────────────────────────────────────
    try:
        rs_candidate = select_rule_set(repository, state)
    except ConfigurationError as exc:
        exc.episode_id = context.episode_id
        trace = _make_trace(
            episode_id=context.episode_id,
            state=state,
            G=gov_config.G,
            A_AI=gov_config.A_AI,
            active_rule_ids=[],
            active_rule_conclusion_types=frozenset(),
            fired_rule_ids=[],
            generated_advisory_types=[],
            configuration_failure=True,
            S_old=s_old,
            S_new=state,
            rule_set_bound_for_state=state,
            evaluation_failure=False,
            failed_rule_ids=[],
            failure_category=None,
        )
        return EpisodeResult(advisories=[], trace=trace, error=exc)

    # ── Step 4: validate RS_candidate (A_AI containment + V1–V4) ─────────────
    try:
        validate_rule_set(rs_candidate, state, context.episode_id)
    except ConfigurationError as exc:
        trace = _make_trace(
            episode_id=context.episode_id,
            state=state,
            G=gov_config.G,
            A_AI=gov_config.A_AI,
            active_rule_ids=[r.rule_id for r in rs_candidate],
            active_rule_conclusion_types=frozenset(r.conclusion_type for r in rs_candidate),
            fired_rule_ids=[],
            generated_advisory_types=[],
            configuration_failure=True,
            S_old=s_old,
            S_new=state,
            rule_set_bound_for_state=state,
            evaluation_failure=False,
            failed_rule_ids=[],
            failure_category=None,
        )
        return EpisodeResult(advisories=[], trace=trace, error=exc)

    # ── Step 5: RS(S) is now the validated rs_candidate ──────────────────────
    rs = rs_candidate

    # ── Step 6: engine.reason(context, RS(S)) ────────────────────────────────
    reason_result = engine.reason(context, rs)

    # ── Steps 7–8: produce AI(E) and emit fidelity trace ─────────────────────
    failure_cat_str: Optional[str] = (
        reason_result.failure_category.value
        if reason_result.failure_category is not None
        else None
    )

    trace = _make_trace(
        episode_id=context.episode_id,
        state=state,
        G=gov_config.G,
        A_AI=gov_config.A_AI,
        active_rule_ids=[r.rule_id for r in rs],
        active_rule_conclusion_types=frozenset(r.conclusion_type for r in rs),
        fired_rule_ids=reason_result.fired_rule_ids,
        generated_advisory_types=[a.type for a in reason_result.advisories],
        configuration_failure=False,
        S_old=s_old,
        S_new=state,
        rule_set_bound_for_state=state,
        evaluation_failure=reason_result.evaluation_failure,
        failed_rule_ids=reason_result.failed_rule_ids,
        failure_category=failure_cat_str,
    )

    # ── Step 9: return EpisodeResult ──────────────────────────────────────────
    return EpisodeResult(
        advisories=reason_result.advisories,
        trace=trace,
        error=None,
    )


# ── Internal helper ───────────────────────────────────────────────────────────

def _make_trace(**kwargs) -> FidelityTrace:
    """Construct a FidelityTrace. Centralises field construction for execute_episode()."""
    return FidelityTrace(**kwargs)
