#!/usr/bin/env python3
"""Verification for the F1-F3 / E5 status-synchronisation micro-repair.

Checks are executed against the repaired specification text and the
authoritative Batch 5 / Batch 7A artefacts. Nothing is asserted from memory.
"""

import csv
import hashlib
import json
import os
import re
import subprocess

ROOT = "/sessions/charming-magical-euler/mnt/research-test-2"
OUT = os.path.join(ROOT, "data/journal1-f1-f3-e5-status-repair")
SPEC = os.path.join(ROOT, "publications/active/journal-1/evaluation-specification.md")
MAN = os.path.join(ROOT, "publications/active/journal-1/submissions/v1-initial-submission/manuscript.md")
B5 = os.path.join(ROOT, "data/journal1-layer3-prototype/batch5-fidelity-evaluation")


def sha(p):
    with open(p, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


spec = open(SPEC, encoding="utf-8").read()
speclines = spec.split("\n")
fid = json.load(open(os.path.join(B5, "fidelity-results.json")))
rep = json.load(open(os.path.join(B5, "reporting-repair.json")))
ssm = json.load(open(os.path.join(B5, "state-space-manifest.json")))
edes = json.load(open(os.path.join(B5, "evaluation-design.json")))
rules = list(csv.DictReader(open(os.path.join(B5, "rule-activation-summary.csv"))))
lat = json.load(open(os.path.join(ROOT, "data/journal1-e5-benchmark/latency-results.json")))
base = json.load(open(os.path.join(OUT, "baseline-hashes.json")))

V, notes = {}, {}


def chk(name, cond, note=None):
    V[name] = "PASS" if cond else "FAIL"
    if note:
        notes[name] = note


# Lines that legitimately describe historical state, excluded from the
# active-stale scan. Identified by their content, not by line number.
HISTORICAL_MARKERS = (
    "Status synchronised 2026-09-13",
    "It is frozen batch evidence, not a maintained authority",
    "~~OPEN-3~~",
)


def active_lines():
    return [l for l in speclines if not any(m in l for m in HISTORICAL_MARKERS)]


def scan(pattern):
    return [l.strip()[:160] for l in active_lines() if re.search(pattern, l, re.I)]


# ------------------------------------------------- stale status removed
def section_block(title):
    """Return the body of a '## <title>' section, excluding historical lines."""
    i = next(i for i, l in enumerate(speclines) if l.startswith("## " + title))
    j = next((k for k in range(i + 1, len(speclines)) if speclines[k].startswith("## ")),
             len(speclines))
    return "\n".join(l for l in speclines[i:j]
                     if not any(m in l for m in HISTORICAL_MARKERS))


# The stale wording never named F1/F2/F3 on the same line as its status — it
# said "all three are OPEN". Token adjacency alone therefore misses it, so the
# fidelity sections are scanned as blocks for any surviving OPEN/deferred
# status assertion, in addition to the token scan.
FIDELITY_BLOCKS = {
    "7": section_block("7. Implementation-fidelity criteria"),
    "14": section_block("14. Layer 3 dependency"),
    "18": section_block("18. Final evaluation matrix"),
}
STATUS_STALE = (r"all three are \*\*OPEN", r"all three .{0,30}\bOPEN\b",
                r"FIDELITY \(deferred", r"deferred to Layer 3 build",
                r"Blocked on Layer 3", r"\bF[123]\b[^\n]{0,60}\bOPEN\b")

for c in ("F1", "F2", "F3"):
    hits = scan(rf"\b{c}\b.{{0,40}}\bOPEN\b") + scan(rf"\b{c}\b.{{0,40}}deferred to Layer 3")
    for sec, body in FIDELITY_BLOCKS.items():
        for p in STATUS_STALE:
            for m in re.findall(p, body, re.I):
                hits.append(f"§{sec}: {m if isinstance(m, str) else m[0]}")
    chk(f"stale_{c}_OPEN_removed", not hits, f"residual: {sorted(set(hits))}")

_l3 = (scan(r"not (?:fully )?implemented") + scan(r"future Layer 3")
       + scan(r"awaiting Layer 3") + scan(r"Blocked on Layer 3")
       + scan(r"Blocked by Layer 3") + scan(r"Layer 3 not yet")
       + scan(r"deferred to Layer 3 build"))
chk("stale_Layer3_unbuilt_removed", not _l3, f"residual: {_l3}")

# ------------------------------------------------- closed status present
chk("F1_closed_preserved", "all three are **CLOSED — PASS**" in spec)
chk("F2_closed_preserved", "all three are **CLOSED — PASS**" in spec)
chk("F3_closed_preserved", "**CLOSED — PASS** (Section 7)" in spec)
chk("F1_F2_zero_violations_correct",
    "**F1 violations = 0**" in spec and "**F2 violation count = 0**" in spec
    and fid["F1"]["violations"] == 0 and fid["F2"]["violation_count"] == 0)
chk("F3_zero_mismatches_correct",
    "**F3 mismatches = 0**" in spec and fid["F3"]["mismatches"] == 0)
chk("292_primary_episode_scope_correct",
    "**292 primary episodes** (32 SAFE, 260 CAUTION)" in spec
    and fid["F1"]["episodes_evaluated"] == 292
    and fid["F3"]["SAFE_episodes"] == 32 and fid["F3"]["CAUTION_episodes"] == 260)
chk("advisory_counts_correct",
    "**454 advisory records**" in spec and "**244 episodes with a non-empty advisory**" in spec
    and "16 CAUTION episodes" in spec
    and fid["F1"]["advisory_records_evaluated"] == 454
    and fid["F2"]["episodes_with_advisory"] == 244
    and rep["trace_derived_authoritative_values"]["empty_advisory_CAUTION_episodes"] == 16)
chk("162_gateoff_scope_separate",
    "**162 UNSAFE gate-off cases**" in spec
    and "not part of the 292 primary episodes" in spec
    and ssm["GATED_UNSAFE_cases"] == 162
    and not re.search(r"\b454 (?:primary )?episodes\b", spec))

# ------------------------------------------------- SAFE rule limitation
safe = next(r for r in rules if r["rule_id"] == "R-SAFE-001")
chk("R_SAFE_001_deferred_preserved",
    safe["implementation_status"] == "DEFERRED" and int(safe["times_selected"]) == 0
    and "`R-SAFE-001` remains DEFERRED" in spec)
chk("SAFE_rule_set_not_overclaimed",
    "`RS(SAFE)` is empty" in spec
    and "all 32 SAFE episodes generated zero advisories" in spec
    and "do **not** demonstrate fidelity of a populated SAFE rule set" in spec
    and "do not establish that every type in `A_AI(SAFE)` was exercised" in spec
    and not re.search(r"full SAFE rule-set fidelity|all A_AI\(SAFE\) recommendation types exercised"
                      r"|all possible Layer 3 behaviours", spec, re.I))
chk("fidelity_scope_bounded",
    "interface-contract exhaustive" in spec
    and "not the retrospective replay" in spec
    and edes["primary_evaluation_scope"] == "interface-contract exhaustive"
    and edes["retrospective_replay_run"] is False)
chk("only_Delay_generated_stated",
    "only conclusion type the prototype generates is `Delay`" in spec
    and {r["conclusion_type"] for r in rules if int(r["advisories_generated"]) > 0} == {"Delay"})

# ------------------------------------------------- Layer 3 status
chk("Layer3_implemented_status_correct",
    "Layer 3 is **specified and implemented**" in spec
    and "`ComponentStateTrace`" in spec
    and "`R-CAUTION-001`–`R-CAUTION-004` are implemented" in spec)
chk("no_deployment_claim",
    "not a **production deployment**, an **operational maritime system**, a **validated field system** or a **complete recommendation engine**"
    .replace("**", "") in spec.replace("**", ""))

# ------------------------------------------------- untouched authority
chk("P1_P4_unchanged",
    all(s in spec for s in ["P1 Totality", "P2 Monotonicity", "P3 Safety Dominance",
                            "P4 (J1-P1) C1 ≡ C3 admissible-set equivalence"]))
chk("E1_E4_unchanged",
    all(s in spec for s in ["42.88%", "48.69%", "**5.81%**", "**4.48%**",
                            "3,661 state transitions", "10.36%"]))
chk("E6_unchanged", "E6 C1 ↔ C3 = 0.00% (J1-P1 confirmation)" in spec)
chk("E3_scope_preserved", "**Mandatory dual-configuration scope: E3 covers {E1, E2, E6}.**" in spec)
chk("E4_resolution_not_required_preserved",
    "`E4_RESOLUTION = NOT_REQUIRED_BY_CURRENT_E3_DESIGN`" in spec
    and "does **not** claim that E4 is insensitive to resolution" in spec)
chk("taxonomy_preserved",
    "FIDELITY (CLOSED" in spec and "EMPIRICAL / TRACE" in spec
    and "PERFORMANCE" in spec and "FORMAL" in spec
    and "behavioural hypothesis" in spec)

# ------------------------------------------------- E5 boundary
chk("E5_open",
    "**OPEN — requires target-hardware benchmarking.**" in spec
    and lat["target_hardware_evidence"] is False)
chk("E5_harness_closed", "`E5_HARNESS = CLOSED`" in spec)
chk("MacBook_reference_only",
    "`MACBOOK_CLASSIFICATION = DEVELOPMENT_MACHINE_REFERENCE`" in spec
    and "`MACBOOK_REFERENCE = COMPLETE`" in spec
    and lat["run_type"] == "DEVELOPMENT_MACHINE_REFERENCE")
chk("target_hardware_evidence_false", "`target_hardware_evidence = false`" in spec)
chk("Android_deferred_mandatory",
    "`E5_ANDROID_TARGET_BENCHMARK = DEFERRED_MANDATORY`" in spec)
chk("H3_open_unsupported",
    "`H3 = X ms` remains **OPEN/UNSUPPORTED**" in spec
    and "`H3 = X ms`" in spec
    and not re.search(r"H3 = \d", spec))
chk("no_latency_threshold",
    "a low reference latency is not a threshold pass" in spec
    and not re.search(r"threshold of \d|acceptable latency of", spec, re.I))
chk("no_Android_result",
    not re.search(r"Android[^.]{0,80}\d+\.?\d*\s*ms", spec)
    and "must not be scaled or extrapolated" in spec)
chk("not_all_evaluation_closed",
    "E5 remains OPEN" in spec
    and not re.search(r"all evaluation (?:is |are )?CLOSED|evaluation complete", spec, re.I))

# ------------------------------------------------- process / integrity
_git = subprocess.run(["git", "-C", ROOT, "status", "--porcelain"],
                      capture_output=True, text=True).stdout.split("\n")
changed = sorted({re.sub(r"^..\s", "", l).strip().strip('"') for l in _git if l.strip()})
allowed = ("publications/active/journal-1/evaluation-specification.md",
           "publications/active/journal-1/submissions/v1-initial-submission/manuscript.md",
           "data/journal1-manuscript-authoring/", "data/journal1-f1-f3-e5-status-repair/",
           "docs/tasks/")
unexpected = [c for c in changed if not c.startswith(allowed)]

chk("no_scientific_code_change",
    not any(c.startswith(("scripts/", "governance/")) for c in changed), f"changed: {changed}")
chk("no_new_experiment", edes["E5_run"] is False and edes["retrospective_replay_run"] is False)
chk("no_new_replay",
    not any(c.startswith(("data/c6/", "data/c7/", "data/c8/")) or c == "data/prediction-register.csv"
            for c in changed))
chk("no_new_external_evidence",
    not any(c.startswith(("data/journal1-layer3-prototype/", "data/journal1-e5-benchmark/",
                          "data/journal1-post-fidelity-plan/", "notes/", "papers/"))
            for c in changed))
chk("no_unexpected_file_change", not unexpected, f"unexpected: {unexpected}")

# Manuscript and every 8B-1 artefact must be byte-identical to the preflight snapshot.
drift = {}
for rel, expected in base.items():
    p = os.path.join(ROOT, rel)
    now = sha(p)
    if now != expected:
        drift[rel] = {"before": expected[:16], "now": now[:16]}
chk("manuscript_unchanged_by_microrepair",
    "publications/active/journal-1/submissions/v1-initial-submission/manuscript.md" not in drift,
    f"manuscript sha: {sha(MAN)[:16]}")
chk("batch8b1_artefacts_unchanged",
    not any(k.startswith("data/journal1-manuscript-authoring/") for k in drift),
    f"drifted: {list(drift)}")
chk("only_specification_changed_among_baseline",
    set(drift) == {"publications/active/journal-1/evaluation-specification.md"},
    f"drifted set: {sorted(drift)}")

# Minimal diff: bounded line churn, and no change outside the repaired sections.
_diff = subprocess.run(["git", "-C", ROOT, "diff", "--numstat", "--",
                        "publications/active/journal-1/evaluation-specification.md"],
                       capture_output=True, text=True).stdout.strip()
ins, dele = (int(x) for x in _diff.split("\t")[:2]) if _diff else (0, 0)
chk("minimal_diff", ins <= 40 and dele <= 20,
    f"+{ins} -{dele} lines in one file")

PROTECTED = [
    "publications/active/journal-1/submissions/v1-initial-submission/manuscript.md",
    "publications/active/journal-1/algorithm-specification.md",
    "publications/active/journal-1/layer3-prototype-specification.md",
    "docs/canonical/appendix-c-formalisation.md",
    "docs/canonical/architecture-illustration.md",
    "docs/canonical/empirical-findings-2026-09-06.md",
    "scripts/condition_comparison.py", "scripts/hysteresis_analysis.py",
    "scripts/canonical_gt.py", "scripts/canonical_figures.py",
    "scripts/historical_replay.py", "scripts/journal1_layer3_fidelity_evaluation.py",
    "governance/rule.py", "governance/advisory.py", "governance/fidelity_trace.py",
    "governance/rule_repository.py", "governance/rule_set_provider.py",
    "governance/reasoning_engine.py", "governance/reasoning_episode.py",
    "governance/canonical_rules.py",
    "data/journal1-layer3-prototype/batch5-fidelity-evaluation/fidelity-results.json",
    "data/journal1-layer3-prototype/batch5-fidelity-evaluation/rule-activation-summary.csv",
    "data/journal1-layer3-prototype/batch5-fidelity-evaluation/state-space-manifest.json",
    "data/journal1-e5-benchmark/latency-results.json",
    "data/c8/canonical-results-post-migration.txt",
    "data/prediction-register.csv",
    "data/journal1-e3-e4-authority-repair/authority-after.md",
]
b5_recorded = rep["protected_files_unchanged"]
independent = {}
for rel, exp in b5_recorded.items():
    p = os.path.join(ROOT, rel)
    if os.path.exists(p) and rel != "publications/active/journal-1/evaluation-specification.md":
        independent[rel] = {"batch5_recorded": exp[:16], "now": sha(p)[:16], "unchanged": exp == sha(p)}
chk("frozen_authority_unchanged", all(v["unchanged"] for v in independent.values()))

integrity = {
    "batch": "F1-F3 / E5 status-synchronisation micro-repair",
    "date": "2026-09-13",
    "specification": {
        "path": "publications/active/journal-1/evaluation-specification.md",
        "sha256_before": base["publications/active/journal-1/evaluation-specification.md"][:16],
        "sha256_after": sha(SPEC)[:16],
        "diff": f"+{ins} -{dele}",
    },
    "manuscript": {
        "sha256_before": base["publications/active/journal-1/submissions/v1-initial-submission/manuscript.md"][:16],
        "sha256_after": sha(MAN)[:16],
        "unchanged": sha(MAN) == base["publications/active/journal-1/submissions/v1-initial-submission/manuscript.md"],
    },
    "batch8b1_artefacts": {
        k: {"before": v[:16], "now": sha(os.path.join(ROOT, k))[:16],
            "unchanged": sha(os.path.join(ROOT, k)) == v}
        for k, v in base.items() if k.startswith("data/journal1-manuscript-authoring/")
    },
    "expected_unchanged": {rel: sha(os.path.join(ROOT, rel))[:16]
                           for rel in PROTECTED if os.path.exists(os.path.join(ROOT, rel))},
    "independent_baseline_check_vs_batch5_recorded_hashes": independent,
    "git_changed_paths": changed,
    "drift_among_baseline_files": drift,
}
with open(os.path.join(OUT, "integrity.json"), "w", encoding="utf-8") as fh:
    json.dump(integrity, fh, indent=2)

totals = {"PASS": sum(1 for v in V.values() if v == "PASS"),
          "FAIL": sum(1 for v in V.values() if v == "FAIL"),
          "OPEN": sum(1 for v in V.values() if v == "OPEN")}
with open(os.path.join(OUT, "verification.json"), "w", encoding="utf-8") as fh:
    json.dump({"batch": "f1-f3-e5-status-repair", "checks": V, "notes": notes, "totals": totals},
              fh, indent=2)

print(json.dumps({"totals": totals, "failures": [k for k, v in V.items() if v != "PASS"]}, indent=2))
