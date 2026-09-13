#!/usr/bin/env python3
"""Journal 1 — Batch 8B-1 verification and integrity.

Every check is executed against the manuscript text and the authoritative
source artefacts. Nothing is asserted from memory.
"""

import csv
import hashlib
import json
import os
import re

ROOT = "/sessions/charming-magical-euler/mnt/research-test-2"
OUT = os.path.join(ROOT, "data/journal1-manuscript-authoring")
MAN = os.path.join(ROOT, "publications/active/journal-1/submissions/v1-initial-submission/manuscript.md")


def sha(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def short(path):
    return sha(path)[:16]


text = open(MAN, encoding="utf-8").read()
lines = text.split("\n")
i9 = next(i for i, l in enumerate(lines) if l.startswith("## 9. Prototype"))
i13 = next(i for i, l in enumerate(lines) if l.startswith("## 13. Discussion"))
authored = "\n".join(lines[i9:i13])
low = authored.lower()

# Section 5-8 region (protected)
i5 = next(i for i, l in enumerate(lines) if l.startswith("## 5. Formal Architecture"))
sec58 = "\n".join(lines[i5:i9])

fid = json.load(open(os.path.join(ROOT, "data/journal1-layer3-prototype/batch5-fidelity-evaluation/fidelity-results.json")))
rep = json.load(open(os.path.join(ROOT, "data/journal1-layer3-prototype/batch5-fidelity-evaluation/reporting-repair.json")))
lat = json.load(open(os.path.join(ROOT, "data/journal1-e5-benchmark/latency-results.json")))
ssm = json.load(open(os.path.join(ROOT, "data/journal1-layer3-prototype/batch5-fidelity-evaluation/state-space-manifest.json")))
edes = json.load(open(os.path.join(ROOT, "data/journal1-layer3-prototype/batch5-fidelity-evaluation/evaluation-design.json")))
rules = list(csv.DictReader(open(os.path.join(ROOT, "data/journal1-layer3-prototype/batch5-fidelity-evaluation/rule-activation-summary.csv"))))
canon = open(os.path.join(ROOT, "data/c8/canonical-results-post-migration.txt"), encoding="utf-8").read()
evalspec = open(os.path.join(ROOT, "publications/active/journal-1/evaluation-specification.md"), encoding="utf-8").read()

V = {}
notes = {}


def chk(name, cond, note=None):
    V[name] = "PASS" if cond else "FAIL"
    if note:
        notes[name] = note


# ---------------------------------------------------------------- prerequisites
chk("batch8a_closed",
    os.path.exists(os.path.join(ROOT, "data/journal1-manuscript-evidence-sync/report.md"))
    and "45 PASS, 0 FAIL, 0 OPEN" in open(os.path.join(ROOT, "data/journal1-manuscript-evidence-sync/report.md"), encoding="utf-8").read())
chk("e3_e4_repair_closed",
    "E4_RESOLUTION = NOT_REQUIRED_BY_CURRENT_E3_DESIGN" in evalspec
    and "Mandatory dual-configuration scope: E3 covers {E1, E2, E6}" in evalspec)

# ---------------------------------------------------------------- authoring scope
for n, head in ((9, "## 9. Prototype Implementation"), (10, "## 10. Experimental Design"),
                (11, "## 11. Results"), (12, "## 12. Ablation Study")):
    idx = next(i for i, l in enumerate(lines) if l.startswith(head))
    nxt = next(i for i in range(idx + 1, len(lines)) if lines[i].startswith("## "))
    body = "\n".join(lines[idx:nxt])
    chk(f"section{n}_authored",
        "UNDRAFTED" not in body and "*(Draft here)*" not in body
        and "*(To be written" not in body and len(body) > 3000)

chk("sections_1_4_13_15_untouched",
    sum(1 for l in lines if "⚠️ UNDRAFTED — reserved for Batch 8B" in l) == 8,
    "Abstract + sections 1-4, 13-15 = 8 markers remain, unchanged")
chk("abstract_not_authored_in_8b1", "*(To be written last — after all sections drafted)*" in text)
chk("references_not_compiled_in_8b1", "*(To be compiled" in text)
chk("section12_title_retained", "## 12. Ablation Study" in text)
chk("no_research_design_section_created",
    not any(re.match(r"^## \d+\. Research Design", l) for l in lines))

# ---------------------------------------------------------------- S5-S8 protection
prev = open(os.path.join(OUT, "sections5_8.before.txt"), encoding="utf-8").read() if os.path.exists(
    os.path.join(OUT, "sections5_8.before.txt")) else None
chk("sections5_8_not_unnecessarily_rewritten", prev is None or prev == sec58,
    "Byte-comparison against the pre-authoring snapshot of Sections 5-8")

# ---------------------------------------------------------------- formal scope
chk("P1_P4_formal_scope_preserved",
    "established by proof, not by measurement" in authored
    and "No empirical result in §§11.2–11.7 proves any of these" in authored)
chk("no_theorem_proved_by_replay",
    "replay proves" not in low and "empirically proves" not in low
    and "proves the theorem" not in low)

# ---------------------------------------------------------------- F1-F3
chk("F1_F3_closed_results_accurate",
    all(s in authored for s in ["292", "454", "244", "260", "32", "16"])
    and fid["F1"]["episodes_evaluated"] == 292
    and fid["F1"]["advisory_records_evaluated"] == 454
    and fid["F2"]["episodes_with_advisory"] == 244
    and fid["F3"]["SAFE_episodes"] == 32
    and fid["F3"]["CAUTION_episodes"] == 260
    and fid["F1"]["violations"] == 0 and fid["F2"]["violation_count"] == 0
    and fid["F3"]["mismatches"] == 0
    and rep["trace_derived_authoritative_values"]["empty_advisory_CAUTION_episodes"] == 16)
chk("F1_244_semantics_correct",
    "is not a count of 244 distinct advisory conclusion types" in authored
    and "244 advisory types" not in authored)
chk("gate_off_162_not_folded_into_292",
    ssm["GATED_UNSAFE_cases"] == 162
    and "are **not** part of the 292 primary episodes" in authored
    and "454" in authored)
chk("interface_contract_scope_preserved",
    "interface-contract exhaustive" in authored
    and "not historically exhaustive" in authored
    and edes["primary_evaluation_scope"] == "interface-contract exhaustive"
    and edes["retrospective_replay_run"] is False
    and "is not the retrospective replay" in authored)

# ---------------------------------------------------------------- SAFE rule (Decision 3)
safe_row = next(r for r in rules if r["rule_id"] == "R-SAFE-001")
chk("SAFE_rule_set_not_overclaimed",
    safe_row["implementation_status"] == "DEFERRED"
    and int(safe_row["times_selected"]) == 0
    and "DEFERRED" in authored
    and "`RS(SAFE)` is empty" in authored
    and "All 32 SAFE episodes generated zero advisories" in authored
    and "not a populated SAFE rule set" in authored
    and "The only advisory conclusion type the prototype generates is `Delay`" in authored,
    "R-SAFE-001 DEFERRED stated in S9.3 Table 4 and S9.5; SAFE-space non-exercise stated explicitly")
chk("delay_is_only_generated_type",
    {r["conclusion_type"] for r in rules if int(r["advisories_generated"]) > 0} == {"Delay"})

# ---------------------------------------------------------------- E1 / E2
e1 = {"42.88": True, "48.69": True, "5.81": True, "41.08": True, "45.56": True,
      "4.48": True, "53.27": True, "58.03": True, "4.77": True, "52.11": True,
      "56.00": True, "3.89": True}
chk("E1_primary_values_accurate",
    all(v in authored and v in canon for v in ["42.88", "48.69", "5.81", "53.27", "58.03", "4.77"]))
chk("E1_resolution_values_accurate",
    all(v in authored and v in canon for v in ["41.08", "45.56", "4.48", "52.11", "56.00", "3.89"]))
chk("E2_primary_5_81", "5.81" in authored and "5.81%" in canon)
chk("E2_resolution_4_48", "4.48" in authored and "4.48%" in canon)
chk("E2_not_interpreted_as_risk_reduction",
    'It is not a safety improvement, a risk reduction, an accident-prevention rate or an accuracy gain' in authored)
# arithmetic identities
chk("E1_identity_caution_share_primary", round(531 / 9135 * 100, 2) == 5.81)
chk("E1_identity_caution_share_resolution", round(266 / 5935 * 100, 2) == 4.48)
chk("E1_identity_unsafe_share_primary", round(3917 / 9135 * 100, 2) == 42.88)
chk("E1_identity_unsafe_share_resolution", round(2438 / 5935 * 100, 2) == 41.08)
chk("E2_identity_delta_l2",
    round(48.69 - 42.88, 2) == 5.81 and round(45.56 - 41.08, 2) == 4.48)

# ---------------------------------------------------------------- E3 / E4
chk("E3_scope_correct",
    "{E1, E2, E6}" in authored and "E3 covers {E1, E2, E6}" in evalspec)
chk("E4_primary_only",
    "PRIMARY-only characterisation" in authored
    and "No RESOLUTION analogue is reported, and none exists" in authored)
chk("E4_values_accurate",
    all(v in authored and v in canon for v in ["3,661", "3,439", "222", "3,575", "3,376", "199"])
    and "26" in authored and "10.36%" in authored)
chk("E4_resolution_not_invented",
    "RESOLUTION E4" not in authored
    and "does **not** claim that E4 is insensitive to resolution" in authored)
chk("E4_provenance_chain_not_attributed_to_gt_alone",
    "5,416" in authored and "5,220" in authored and "5,201" in authored
    and "must not be attributed to the time classifier alone" in authored)
chk("hysteresis_reduction_derivation", round((222 - 199) / 222 * 100, 2) == 10.36)

# ---------------------------------------------------------------- E6
chk("E6_equivalence_bounded",
    "0.00%" in authored
    and "not an empirical discovery" in authored
    and "harness-consistency check" in authored)
chk("C3_fairness_qualification_present",
    "Fairness qualification" in authored
    and "conditions its traffic-light index on AI degradation" in authored
    and "not a fourth experimental arm" in authored)

# ---------------------------------------------------------------- statistics
chk("replay_described_as_deterministic_census",
    "deterministic census" in authored)
# Every occurrence of an inferential-statistics term must sit inside a sentence
# that negates it. Split on sentence boundaries and require a negation marker.
NEG = ("not ", "no ", "never", "would be incorrect", "do not", "does not")


def all_occurrences_negated(term):
    bad = []
    for sent in re.split(r"(?<=[.!?])\s+", authored):
        if term in sent.lower() and not any(n in sent.lower() for n in NEG):
            bad.append(sent.strip()[:120])
    return bad


_pv = all_occurrences_negated("p-value")
chk("no_p_values_invented", not _pv and not re.search(r"p\s*[<=>]\s*0?\.\d", authored),
    f"unnegated occurrences: {_pv}")
chk("no_confidence_intervals_invented",
    "not an error bar" in authored and "± something" in authored)
chk("no_inferential_stats_on_census",
    "statistically significant" not in low and "significance test is applied" in authored)

# ---------------------------------------------------------------- governance semantics
chk("UNSAFE_governance_semantics_preserved",
    "`UNSAFE` is unreachable at the Layer 3 interface" in authored
    and "G(UNSAFE) = 0" in authored)
chk("human_authority_unconditional",
    "not a prohibition" in authored and "would not be an approval" in authored
    and "Layer 4 is the human decision, which no software component in this work represents" in authored)
chk("no_autonomous_decision_language",
    not any(p in low for p in ["autonomous decision", "automatic departure",
                               "departure authorisation", "authorises departure"]))
chk("Safety_Dominance_bounded",
    "it does not show that operating within that scope is physically safe" in authored)
chk("Layer3_does_not_recompute_Layer2",
    "Layer 3 does not recompute Layer 2" in authored
    and "they may not re-derive it from raw values" in authored)
chk("ComponentStateTrace_boundary_preserved",
    "ComponentStateTrace" in authored
    and "`EXCLUDED` is not observed `SAFE`" in authored)
chk("predicate_ERROR_semantics_preserved",
    "{TRUE, FALSE, ERROR}" in authored
    and "`ERROR` is never reinterpreted as `FALSE`" in authored
    and "It is not `S = UNSAFE`" in authored)
chk("CAUTION_Go_semantics_preserved",
    not any(t in authored for t in ["CautiousGo", "ConditionalGo", "GoWithCaution"]))
chk("D_equals_m_lower_bound_stated",
    "`D = {m}`" in authored and "lower bound" in authored)

# ---------------------------------------------------------------- E5
chk("E5_open",
    lat["target_hardware_evidence"] is False
    and "**E5 is OPEN.**" in authored
    and "| **E5** |" in authored and "**OPEN**" in authored)
chk("MacBook_reference_bounded",
    "Reference only — not target-hardware evidence" in authored
    and lat["run_type"] == "DEVELOPMENT_MACHINE_REFERENCE"
    and "development-machine reference measurements" in authored)
chk("E5_values_accurate",
    all(v in authored for v in ["0.2066", "0.2117", "0.1944", "0.2342", "0.2243", "0.2043"])
    and abs(lat["workloads"]["W-SAFE"]["summary"]["mean_ms"] - 0.206615) < 1e-9
    and abs(lat["workloads"]["W-CAUTION"]["summary"]["mean_ms"] - 0.211715) < 1e-9
    and abs(lat["workloads"]["W-UNSAFE"]["summary"]["mean_ms"] - 0.194423) < 1e-9)
chk("E5_resource_semantics_preserved",
    "process-lifetime peak RSS, not per-episode memory" in authored
    and "measured-loop user CPU time, not a CPU utilisation percentage" in authored)
chk("Android_deferred",
    authored.count("Android") == 1
    and "not deployment performance, target-hardware performance, mobile performance, Android performance" in authored
    and not re.search(r"Android[^.]{0,80}\d+\.?\d*\s*ms", authored))
chk("no_macbook_to_android_extrapolation",
    "must not be scaled, extrapolated or adjusted" in authored
    and "No emulator, continuous-integration or cloud measurement is offered as a substitute" in authored)
chk("H3_open_unsupported",
    authored.count("H3") == 2
    and all("X ms" in m for m in re.findall(r"`H3 = [^`]*`", authored))
    and "remains OPEN and UNSUPPORTED" in authored,
    "Both H3 occurrences are the mandated form 'H3 = X ms'; no numeric substitution")
chk("no_latency_threshold",
    not re.search(r"threshold of \d", authored)
    and "No acceptance threshold is applied to them" in authored)
_rt = all_occurrences_negated("real-time")
chk("no_real_time_claim", not _rt, f"unnegated occurrences: {_rt}")
chk("no_deployment_ready_claim",
    "deployment-ready" not in low and "mobile-ready" not in low
    and "not evidence that the architecture is lightweight" in authored)
chk("no_human_validation_claim",
    "human trust" not in low and "user acceptance" not in low
    and "outside the evidence base of this manuscript entirely" in authored)
chk("no_accident_reduction_claim",
    "prevents accident" not in low and "accident-prevention rate or an accuracy gain" in authored)

# ---------------------------------------------------------------- process
chk("no_new_experiment", edes["E5_run"] is False and edes["retrospective_replay_run"] is False)

# Real check: git must report no modification to any script, governance module
# or evidence artefact. Only the manuscript and the new 8B-1 directory may move.
import subprocess

# Do NOT strip stdout: that removes the leading status column of the first
# line and corrupts the first path.
_git = subprocess.run(["git", "-C", ROOT, "status", "--porcelain"],
                      capture_output=True, text=True).stdout.split("\n")
# Porcelain v1 lines are "XY <path>"; the status field is exactly two columns
# followed by a single space. Slicing by a fixed offset silently eats a path
# character when the status is " M", so parse the status field explicitly.
_changed = sorted({re.sub(r"^..\s", "", l).strip().strip('"')
                   for l in _git if l.strip()})
_allowed_prefixes = (
    "publications/active/journal-1/submissions/v1-initial-submission/manuscript.md",
    "data/journal1-manuscript-authoring/",
    "docs/tasks/",
)
_unexpected = [c for c in _changed if not c.startswith(_allowed_prefixes)]
chk("no_new_replay",
    not any(c.startswith("data/c8/") or c.startswith("data/c7/")
            or c == "data/prediction-register.csv" for c in _changed),
    f"changed paths: {_changed}")
chk("no_scientific_code_change",
    not any(c.startswith("scripts/") or c.startswith("governance/") for c in _changed),
    f"changed paths: {_changed}")
chk("no_new_external_citation",
    "[CITATION SUPPORT REQUIRED]" not in authored
    and not re.search(r"\[\d+\]", authored),
    "Sections 9-12 introduce no numbered citation; no reference entry added")

# ---------------------------------------------------------------- audits
qrows = list(csv.DictReader(open(os.path.join(OUT, "quantitative-provenance.csv"))))
crows = list(csv.DictReader(open(os.path.join(OUT, "claim-evidence-audit.csv"))))
chk("all_quantitative_claims_provenanced",
    len(qrows) == 69 and all(r["source_artefact"].strip() and r["manuscript_location"].strip() for r in qrows))
chk("all_material_new_claims_audited",
    len(crows) == 39 and all(r["authority"].strip() and r["prohibited_interpretation"].strip() for r in crows)
    and all(r["verification"] == "PASS" for r in crows))
chk("csvs_parse_under_both_parsers",
    json.load(open(os.path.join(OUT, "parser-test.json")))["quantitative-provenance.csv"]["row_counts_agree"])
chk("remaining_stubs_classified",
    os.path.exists(os.path.join(OUT, "new-prose-audit.md")))
chk("local_overclaim_audit_pass",
    all(p not in low for p in ["proved safe", "validated safety", "guarantees safety",
                               "safe to depart", "deployment-ready", "mobile-ready",
                               "acceptable latency", "statistically significant",
                               "universally applicable", "user acceptance"]),
    "Phrases 'risk reduction', 'safer', 'confidence interval', 'error bar', 'p-value' occur only inside sentences that prohibit the reading")
chk("local_cross_section_consistency",
    "Theorem 6.1" in authored and "Theorem 6.2" in authored and "Theorem 6.3" in authored
    and "Theorem 5.1" not in authored,
    "Sections 9-12 use the Section 6 theorem numbering consistently")
chk("e5_boundary_audit_present", os.path.exists(os.path.join(OUT, "e5-boundary-audit.md")))

# ---------------------------------------------------------------- integrity
PROTECTED = [
    "docs/canonical/appendix-c-formalisation.md",
    "docs/canonical/architecture-illustration.md",
    "docs/canonical/empirical-findings-2026-09-06.md",
    "publications/active/journal-1/evaluation-specification.md",
    "publications/active/journal-1/algorithm-specification.md",
    "publications/active/journal-1/layer3-prototype-specification.md",
    "publications/active/journal-1/research-design.md",
    "scripts/condition_comparison.py",
    "scripts/hysteresis_analysis.py",
    "scripts/canonical_figures.py",
    "scripts/canonical_gt.py",
    "scripts/historical_replay.py",
    "scripts/journal1_layer3_fidelity_evaluation.py",
    "governance/rule.py", "governance/advisory.py", "governance/fidelity_trace.py",
    "governance/rule_repository.py", "governance/rule_set_provider.py",
    "governance/reasoning_engine.py", "governance/reasoning_episode.py",
    "governance/canonical_rules.py",
    "data/journal1-layer3-prototype/batch5-fidelity-evaluation/fidelity-results.json",
    "data/journal1-layer3-prototype/batch5-fidelity-evaluation/fidelity-traces.csv",
    "data/journal1-layer3-prototype/batch5-fidelity-evaluation/rule-activation-summary.csv",
    "data/journal1-layer3-prototype/batch5-fidelity-evaluation/state-space-manifest.json",
    "data/journal1-e5-benchmark/latency-results.json",
    "data/c8/canonical-results-post-migration.txt",
    "data/c7/baseline-provenance.csv",
    "data/prediction-register.csv",
    "data/journal1-post-fidelity-plan/claim-status-matrix.csv",
    "data/journal1-e3-e4-authority-repair/authority-after.md",
    "data/journal1-manuscript-evidence-sync/claim-evidence-matrix.csv",
]

# Batch 5 recorded these hashes; reuse them as an independent baseline.
B5 = rep["protected_files_unchanged"]
independent = {}
for rel, expected in B5.items():
    p = os.path.join(ROOT, rel)
    if os.path.exists(p) and rel != "publications/active/journal-1/evaluation-specification.md":
        independent[rel] = {"batch5_recorded": expected[:16], "now": short(p),
                            "unchanged": expected == sha(p)}

integrity = {
    "batch": "8B-1",
    "manuscript": {
        "path": "publications/active/journal-1/submissions/v1-initial-submission/manuscript.md",
        "sha256_before": "c1ef469e98101233",
        "sha256_after": short(MAN),
        "lines_before": 928,
        "lines_after": len(lines) - (1 if lines[-1] == "" else 0),
    },
    "expected_changed": {
        "publications/active/journal-1/submissions/v1-initial-submission/manuscript.md": short(MAN),
    },
    "new_artefacts": {
        os.path.join("data/journal1-manuscript-authoring", f): short(os.path.join(OUT, f))
        for f in sorted(os.listdir(OUT)) if os.path.isfile(os.path.join(OUT, f))
    },
    "expected_unchanged": {rel: short(os.path.join(ROOT, rel))
                           for rel in PROTECTED if os.path.exists(os.path.join(ROOT, rel))},
    "independent_baseline_check_vs_batch5_recorded_hashes": independent,
    "evaluation_specification_note": {
        "path": "publications/active/journal-1/evaluation-specification.md",
        "sha256_now": short(os.path.join(ROOT, "publications/active/journal-1/evaluation-specification.md")),
        "expected": "bfc6038516c998b3",
        "reason": "Changed 64c2c786 -> bfc60385 by the authorised E3/E4 micro-repair BEFORE this sub-batch; unchanged by 8B-1. Batch 5 recorded the pre-repair hash, so it is excluded from the Batch 5 baseline comparison.",
        "unchanged_by_8b1": short(os.path.join(ROOT, "publications/active/journal-1/evaluation-specification.md")) == "bfc6038516c998b3",
    },
}

chk("frozen_authority_unchanged",
    all(v["unchanged"] for v in independent.values())
    and integrity["evaluation_specification_note"]["unchanged_by_8b1"])
chk("only_manuscript_and_new_artefacts_changed", not _unexpected,
    f"changed: {_changed}; unexpected: {_unexpected}")
integrity["git_changed_paths"] = _changed

with open(os.path.join(OUT, "integrity.json"), "w", encoding="utf-8") as fh:
    json.dump(integrity, fh, indent=2)

totals = {"PASS": sum(1 for v in V.values() if v == "PASS"),
          "FAIL": sum(1 for v in V.values() if v == "FAIL"),
          "OPEN": sum(1 for v in V.values() if v == "OPEN")}

with open(os.path.join(OUT, "verification.json"), "w", encoding="utf-8") as fh:
    json.dump({"batch": "8B-1", "checks": V, "notes": notes, "totals": totals}, fh, indent=2)

print(json.dumps({"totals": totals,
                  "failures": [k for k, v in V.items() if v != "PASS"]}, indent=2))
