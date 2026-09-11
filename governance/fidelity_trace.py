"""FidelityTrace — conceptual fidelity instrumentation for Layer 3 episodes.

Authority: layer3-prototype-specification.md §11 (Batch 1 fields);
           Batch 3 task §20 (OPEN-L3-2 additions: evaluation_failure, failed_rule_ids,
           failure_category).

Always produced — never None. Configuration failures recorded in trace rather than
silently suppressed.

F1–F3 mapping (layer3-prototype-specification.md §11.2):
  F1 — generated_advisory_types ⊆ A_AI, active_rule_conclusion_types ⊆ A_AI
  F2 — count(t ∉ A_AI) == 0
  F3 — rule_set_bound_for_state == S_new; ConclusionTypes(RS_used) ⊆ A_AI(S_new)

Status: DESIGNED — NOT YET TESTED (fidelity evaluation is a separate downstream task).
"""
from __future__ import annotations

import dataclasses


@dataclasses.dataclass
class FidelityTrace:
    """Instrumentation record for one governed reasoning episode.

    Distinguishes normal no-fire from evaluation failure:
      fired_rule_ids=[], evaluation_failure=False → normal no-fire (no rule matched)
      fired_rule_ids=[], evaluation_failure=True  → reasoning failed (ERROR in predicate)

    failure_category is None for configuration failures and normal outcomes;
    it records the first runtime failure category when evaluation_failure=True.
    """

    # ── Core episode identity ────────────────────────────────────────────────
    episode_id: str
    state: str                          # S for this episode
    G: int                              # G(S): 0 or 1
    A_AI: frozenset                     # A_AI(S): admissible recommendation types

    # ── Rule-set fields (Batch 1 §11.1) ─────────────────────────────────────
    active_rule_ids: list               # all rule_ids in RS(S) supplied to engine
    active_rule_conclusion_types: frozenset  # ConclusionTypes(RS(S))
    fired_rule_ids: list                # rule_ids whose conditions all evaluated TRUE
    generated_advisory_types: list      # conclusion_type of each Advisory produced

    # ── Failure flags ────────────────────────────────────────────────────────
    configuration_failure: bool         # True iff ConfigurationError raised this episode
    evaluation_failure: bool            # True iff any predicate returned ERROR during reason()

    # ── Transition fields (for F3) ───────────────────────────────────────────
    S_old: str | None                   # state of the immediately preceding episode
    S_new: str                          # state of this episode (equals state field)
    rule_set_bound_for_state: str | None  # state passed to select_rule_set(); equals S_new in valid episodes

    # ── OPEN-L3-2 runtime failure fields (Batch 3 task §20) ─────────────────
    failed_rule_ids: list               # rule_ids where predicate ERROR occurred
    failure_category: str | None        # first runtime failure category string, or None
    # Permitted values: "PREDICATE_EXCEPTION" | "NUMERIC_CONVERSION_FAILURE" |
    #                   "MALFORMED_VALUE" | "INTERNAL_ERROR" | None
