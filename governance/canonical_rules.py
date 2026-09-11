"""Canonical Layer 3 scientific rule repository.

Loads scientifically admitted rules from the Batch 2 closed authority:
  publications/active/journal-1/layer3-prototype-specification.md §24
  data/journal1-layer3-prototype/closure-batch2.json

IMPLEMENTED rules (loaded by build_canonical_repository()):
  R-CAUTION-001  — antecedent m == "advisory" → directly expressible as
                   ConditionPredicate(variable="resolved_m", operator="==", value="advisory")
  R-CAUTION-002  — antecedent component_o_state == "CAUTION" (Batch 4B-2)
  R-CAUTION-003  — antecedent component_r_state == "CAUTION" (Batch 4B-2)
  R-CAUTION-004  — antecedent component_w_state == "CAUTION" (Batch 4B-2)

DEFERRED rules (blocked from implementation):
  R-SAFE-001     — see DEFERRED_RULES below (STATE_RESTATEMENT — Batch 4A)

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
            "STATE_RESTATEMENT (Batch 4A): antecedent is logically equivalent to S=SAFE under "
            "max-severity aggregation. Implementing as a component-state conjunction would restate "
            "what S already encodes. Requires bounded scientific decision before implementation."
        ),
        "authority_gap": (
            "layer3-prototype-specification.md §20 — STATE_RESTATEMENT finding from Batch 4A; "
            "see data/journal1-layer3-prototype/batch4a-executable-rule-authority/resolution.json"
        ),
        "conclusion_type": "Go",
        "applicable_state": "SAFE",
        "batch4a_status": "DEFERRED — STATE_RESTATEMENT",
    },
}


# ── Canonical repository builder ──────────────────────────────────────────────

def build_canonical_repository() -> RuleRepository:
    """Build the canonical Layer 3 rule repository from Batch 2 closed authority.

    Loads R-CAUTION-001 through R-CAUTION-004. R-CAUTION-002/003/004 use
    ComponentStateTrace predicates (component_o/r/w_state) authorised by Batch 4A
    Model B selection and implemented in Batch 4B-2.

    R-SAFE-001 remains deferred. See DEFERRED_RULES for the STATE_RESTATEMENT reason.
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

    # ── R-CAUTION-002 ─────────────────────────────────────────────────────────
    # Batch 2 antecedent: "g_o(o, v) == CAUTION"
    # ComponentStateTrace predicate: component_o_state == "CAUTION"
    # Batch 4A Model B authorisation; Batch 4B-2 implementation
    repo.insert(Rule(
        rule_id="R-CAUTION-002",
        applicable_state="CAUTION",
        conditions=(
            ConditionPredicate(
                variable="component_o_state",
                operator="==",
                value="CAUTION",
            ),
        ),
        conclusion_type="Delay",
        conclusion_payload={
            "reason": (
                "Ocean state classified CAUTION by g_o(o,v) — "
                "vessel-conditioned wave height in CAUTION band"
            ),
        },
        provenance=(
            "EV-02 (MMEA 2021 / NAHRIM 2014, via Yaakob et al. 2015). "
            "Status: CONDITIONALLY SUPPORTED. "
            "P_ENV: Level A (Malaysian coastal vessel operability data). "
            "P_ADV: Level B (Delay from CAUTION ocean state). "
            "Batch 4A Model B authorisation (component_o_state predicate). "
            "Authority: layer3-prototype-specification.md §21; "
            "data/journal1-layer3-prototype/closure-batch2.json; "
            "data/journal1-layer3-prototype/batch4a-executable-rule-authority/resolution.json; "
            "data/journal1-layer3-prototype/batch4b1-interface-amendment/component-state-interface-contract.md"
        ),
        enabled=True,
    ))

    # ── R-CAUTION-003 ─────────────────────────────────────────────────────────
    # Batch 2 antecedent: "g_r(r, κ) == CAUTION"
    # ComponentStateTrace predicate: component_r_state == "CAUTION"
    # Batch 4A Model B authorisation; Batch 4B-2 implementation
    repo.insert(Rule(
        rule_id="R-CAUTION-003",
        applicable_state="CAUTION",
        conditions=(
            ConditionPredicate(
                variable="component_r_state",
                operator="==",
                value="CAUTION",
            ),
        ),
        conclusion_type="Delay",
        conclusion_payload={
            "reason": (
                "Rainfall classified CAUTION by g_r(r,κ) — "
                "precipitation rate in CAUTION band"
            ),
        },
        provenance=(
            "EV-03 (JPS/DID Infobanjir Light upper limit 10.0 mm/hr; "
            "MET Malaysia Ribut Petir 20.0 mm/hr). "
            "Status: CONDITIONALLY SUPPORTED. "
            "P_ENV: Level A (Malaysian meteorological thresholds). "
            "P_ADV: Level B (Delay from CAUTION rainfall rate). "
            "Batch 4A Model B authorisation (component_r_state predicate). "
            "Authority: layer3-prototype-specification.md §21; "
            "data/journal1-layer3-prototype/closure-batch2.json; "
            "data/journal1-layer3-prototype/batch4a-executable-rule-authority/resolution.json; "
            "data/journal1-layer3-prototype/batch4b1-interface-amendment/component-state-interface-contract.md"
        ),
        enabled=True,
    ))

    # ── R-CAUTION-004 ─────────────────────────────────────────────────────────
    # Batch 2 antecedent: "g_w(w) == CAUTION"
    # ComponentStateTrace predicate: component_w_state == "CAUTION"
    # Batch 4A Model B authorisation; Batch 4B-2 implementation
    repo.insert(Rule(
        rule_id="R-CAUTION-004",
        applicable_state="CAUTION",
        conditions=(
            ConditionPredicate(
                variable="component_w_state",
                operator="==",
                value="CAUTION",
            ),
        ),
        conclusion_type="Delay",
        conclusion_payload={
            "reason": (
                "Wind speed classified CAUTION by g_w(w) — "
                "sustained wind in CAUTION band (21.6–27.0 kn, MET Cat 1–2)"
            ),
        },
        provenance=(
            "EV-04 (MET Malaysia wind speed category boundaries: "
            "Cat 1 onset 40 km/h = 21.598 kn, Cat 2 onset 50 km/h = 26.998 kn). "
            "Status: CONDITIONALLY SUPPORTED. "
            "P_ENV: Level A (MET Malaysia official category boundaries). "
            "P_ADV: Level B (Delay from CAUTION wind). "
            "Batch 4A Model B authorisation (component_w_state predicate). "
            "Authority: layer3-prototype-specification.md §21; "
            "data/journal1-layer3-prototype/closure-batch2.json; "
            "data/journal1-layer3-prototype/batch4a-executable-rule-authority/resolution.json; "
            "data/journal1-layer3-prototype/batch4b1-interface-amendment/component-state-interface-contract.md"
        ),
        enabled=True,
    ))

    return repo
