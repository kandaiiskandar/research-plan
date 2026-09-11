"""Canonical Layer 3 scientific rule repository.

Loads scientifically admitted rules from the Batch 2 closed authority:
  publications/active/journal-1/layer3-prototype-specification.md §24
  data/journal1-layer3-prototype/closure-batch2.json

IMPLEMENTABLE rules (loaded by build_canonical_repository()):
  R-CAUTION-001  — antecedent m == "advisory" → directly expressible as
                   ConditionPredicate(variable="resolved_m", operator="==", value="advisory")

DEFERRED rules (insufficient ConditionPredicate specification in Batch 2 artefacts):
  R-SAFE-001     — see DEFERRED_RULES below
  R-CAUTION-002  — see DEFERRED_RULES below
  R-CAUTION-003  — see DEFERRED_RULES below
  R-CAUTION-004  — see DEFERRED_RULES below

Note: R-CAUTION-001 will produce 0 activations in the retrospective replay because
m is held at None throughout (D = {m} — no marine warning archive exists for the
study site). This is the expected lower-bound result; the rule is structurally correct.
See GAP-05 in layer3-prototype-specification.md §25.

OPEN items preserved:
  OPEN-L3-1C — DepartureTime (no scientific authority; no rule loaded)
  OPEN-L3-1D — Duration (no scientific authority; no rule loaded)
  GAP-03     — Go under CAUTION (no evidence; no rule loaded)

Human-authority boundary preserved: no rule produces "Departure prohibited",
"Do not go", or any automated override.
"""
from __future__ import annotations

from .rule import Rule, ConditionPredicate
from .rule_repository import RuleRepository


# ── Deferred rules register ───────────────────────────────────────────────────

DEFERRED_RULES: dict[str, dict[str, str]] = {
    "R-SAFE-001": {
        "batch2_antecedent": (
            "all(g_w(w)==SAFE, g_r(r,κ)==SAFE, g_m(m)==SAFE, g_o(o,v)==SAFE, g_t(t,date)==SAFE)"
        ),
        "reason": (
            "Antecedent includes g_t(t, date)==SAFE which requires solar event lookup. "
            "Implementing this in Layer 3 would violate Batch 3 task §30 (no reimplementation of g_t). "
            "The vessel-dependent g_o SAFE threshold also requires per-vessel predicate expansion "
            "not specified as ConditionPredicate triplets in Batch 2 artefacts."
        ),
        "authority_gap": (
            "layer3-prototype-specification.md §20 — antecedent not expressed as ConditionPredicate "
            "triplets; g_t==SAFE requires solar-event lookup prohibited in Layer 3."
        ),
        "conclusion_type": "Go",
        "applicable_state": "SAFE",
    },
    "R-CAUTION-002": {
        "batch2_antecedent": "g_o(o, v) == CAUTION",
        "reason": (
            "Antecedent g_o(o,v)==CAUTION requires vessel-category-dependent wave height CAUTION "
            "bands (small: 1.0–1.25m, medium: 1.4–2.8m, big: 1.5–3.5m). Splitting into per-vessel "
            "rules would invent rule structure not present in the Batch 2 register. "
            "Exact ConditionPredicate triplets are not specified in Batch 2 artefacts."
        ),
        "authority_gap": (
            "layer3-prototype-specification.md §21 — antecedent expressed as g_o(o,v)==CAUTION "
            "shorthand only; vessel-category-dependent predicate decomposition not in Batch 2."
        ),
        "conclusion_type": "Delay",
        "applicable_state": "CAUTION",
    },
    "R-CAUTION-003": {
        "batch2_antecedent": "g_r(r, κ) == CAUTION",
        "reason": (
            "Antecedent g_r(r,κ)==CAUTION requires threshold expansion "
            "(resolved_r_rate > 10.0 AND resolved_r_rate <= 20.0 AND resolved_r_kappa == 0). "
            "Exact ConditionPredicate triplets are not specified in Batch 2 artefacts; "
            "expansion would draw from Layer 2 g_r specification rather than Batch 2 predicate authority."
        ),
        "authority_gap": (
            "layer3-prototype-specification.md §21 — antecedent expressed as g_r(r,κ)==CAUTION "
            "shorthand only; ConditionPredicate decomposition not in Batch 2."
        ),
        "conclusion_type": "Delay",
        "applicable_state": "CAUTION",
    },
    "R-CAUTION-004": {
        "batch2_antecedent": "g_w(w) == CAUTION",
        "reason": (
            "Antecedent g_w(w)==CAUTION requires threshold expansion "
            "(resolved_w >= 21.6 AND resolved_w <= 27.0). "
            "Exact ConditionPredicate triplets are not specified in Batch 2 artefacts; "
            "expansion would draw from Layer 2 g_w specification rather than Batch 2 predicate authority."
        ),
        "authority_gap": (
            "layer3-prototype-specification.md §21 — antecedent expressed as g_w(w)==CAUTION "
            "shorthand only; ConditionPredicate decomposition not in Batch 2."
        ),
        "conclusion_type": "Delay",
        "applicable_state": "CAUTION",
    },
}


# ── Canonical repository builder ──────────────────────────────────────────────

def build_canonical_repository() -> RuleRepository:
    """Build the canonical Layer 3 rule repository from Batch 2 closed authority.

    Loads only R-CAUTION-001 — the one Batch 2 rule whose predicate is directly
    expressible as a ConditionPredicate on DecisionContext fields without requiring
    threshold expansion or component classifier reimplementation.

    R-SAFE-001, R-CAUTION-002, R-CAUTION-003, R-CAUTION-004 are deferred.
    See DEFERRED_RULES for exact reasons and authority gaps.
    """
    repo = RuleRepository()

    # ── R-CAUTION-001 ─────────────────────────────────────────────────────────
    # Batch 2 antecedent: "m == advisory"
    # Directly expressible as: ConditionPredicate(variable="resolved_m", operator="==", value="advisory")
    # Evidence: EV-01 (MET Malaysia Category 1 marine warning bulletin)
    # Status: CONDITIONALLY SUPPORTED — P_ENV Level A (MET Malaysia); P_ADV Level C (inferred)
    # Authority: layer3-prototype-specification.md §21; data/journal1-layer3-prototype/closure-batch2.json
    repo.insert(Rule(
        rule_id="R-CAUTION-001",
        applicable_state="CAUTION",
        conditions=(
            ConditionPredicate(
                variable="resolved_m",
                operator="==",
                value="advisory",
            ),
        ),
        conclusion_type="Delay",
        conclusion_payload={
            "reason": (
                "MET Malaysia Category 1 marine warning active "
                "(berbahaya kepada bot-bot kecil — dangerous to small boats)"
            ),
        },
        provenance=(
            "EV-01 (MET Malaysia Category 1 marine warning bulletin). "
            "Status: CONDITIONALLY SUPPORTED. "
            "P_ENV: Level A (MET Malaysia, directly applicable to Malaysian waters including Sabah). "
            "P_ADV: Level C (Delay mapping inferred from standard maritime safety practice). "
            "Authority: layer3-prototype-specification.md §21; "
            "data/journal1-layer3-prototype/closure-batch2.json"
        ),
        enabled=True,
    ))

    return repo
