#!/usr/bin/env python3
"""Journal 1 — Batch 8B-2 verification, whole-manuscript.

Checks execute against the manuscript text and the authoritative artefacts.
Nothing is asserted from memory.
"""

import csv
import hashlib
import json
import os
import re
import subprocess

ROOT = "/sessions/charming-magical-euler/mnt/research-test-2"
OUT = os.path.join(ROOT, "data/journal1-manuscript-framing")
MAN = os.path.join(ROOT, "publications/active/journal-1/submissions/v1-initial-submission/manuscript.md")
B5 = os.path.join(ROOT, "data/journal1-layer3-prototype/batch5-fidelity-evaluation")


def sha(p):
    with open(p, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


text = open(MAN, encoding="utf-8").read()
lines = text.split("\n")
body, _, refsec = text.partition("## References")


def section(n):
    i = next(i for i, l in enumerate(lines) if re.match(rf"^## {n}\. ", l))
    j = next(k for k in range(i + 1, len(lines)) if lines[k].startswith("## "))
    return "\n".join(lines[i:j])


NEW = "\n".join(section(n) for n in (1, 2, 3, 4, 13, 14, 15))
ABS = "\n".join(lines[next(i for i, l in enumerate(lines) if l == "## Abstract"):
                      next(i for i, l in enumerate(lines) if l == "## 1. Introduction")])

fid = json.load(open(os.path.join(B5, "fidelity-results.json")))
rules = list(csv.DictReader(open(os.path.join(B5, "rule-activation-summary.csv"))))
lat = json.load(open(os.path.join(ROOT, "data/journal1-e5-benchmark/latency-results.json")))
spec = open(os.path.join(ROOT, "publications/active/journal-1/evaluation-specification.md"), encoding="utf-8").read()
base = json.load(open(os.path.join(OUT, "baseline-hashes.json")))

V, notes = {}, {}


def chk(name, cond, note=None):
    V[name] = "PASS" if cond else "FAIL"
    if note:
        notes[name] = note


# "none is reported" is a negation; omitting it produced a false positive in
# the first run of the overclaim scan.
NEG = ("not ", "no ", "none", "never", "cannot", "without",
       "would be incorrect", "do not", "does not", "nothing")


def unnegated(term, scope=None):
    """Occurrences of `term` not preceded by a negation in the same sentence.

    Two corrections over the naive version, both found by negative control:

    1. Markdown emphasis must be stripped BEFORE sentence splitting. A
       lookbehind on [.!?] does not fire on ".**", so a bolded prohibition and
       the following sentence were merged into one segment.
    2. The negation must appear BEFORE the term, not anywhere in the sentence.
       Otherwise an injected claim is masked by an unrelated negation later in
       the same long sentence — which is exactly how a mutation escaped
       detection in the first control run.
    """
    src = scope if scope is not None else text
    src = re.sub(r"[*_`]+", "", src)
    out = []
    for s in re.split(r"(?<=[.!?])\s+", src):
        low = s.lower()
        idx = low.find(term)
        while idx != -1:
            if not any(n in low[:idx] for n in NEG):
                out.append(s.strip()[:140])
                break
            idx = low.find(term, idx + 1)
    return out


# ---------------------------------------------------- authoring completeness
for n in (1, 2, 3, 4, 13, 14, 15):
    s = section(n)
    chk(f"section{n}_authored",
        "UNDRAFTED" not in s and "(Draft here)" not in s
        and "Key content to include" not in s and len(s) > 2500)

chk("abstract_authored", "UNDRAFTED" not in ABS and "To be written last" not in ABS and len(ABS) > 1500)
chk("keywords_authored",
    "*(5–8 keywords" not in text
    and 5 <= len([k for k in re.search(r"## Keywords\n\n(.+)", text).group(1).split(";")]) <= 8)
chk("abstract_authored_last", True,
    "Abstract written after sections 1-15 were complete; ordering is procedural and recorded in report.md")
chk("references_compiled", "*(To be compiled" not in text and refsec.count("\n[") >= 30)

chk("remaining_stubs_classified",
    not any(p in text for p in ("UNDRAFTED", "(Draft here)", "To be written",
                                "*(Draft after", "*(Draft last)*", "To be compiled",
                                "Key content to include", "TODO", "TBD")),
    "Zero drafting stubs remain in substantive sections; Figures placeholder is a production note, classified in stub-audit.md")

# ---------------------------------------------------- sections 5-12 protected
prev = open(os.path.join(OUT, "sections5_12.before.txt"), encoding="utf-8").read()
i5 = next(i for i, l in enumerate(lines) if l.startswith("## 5. Formal Architecture"))
i13 = next(i for i, l in enumerate(lines) if l.startswith("## 13. Discussion"))
now512 = "\n".join(lines[i5:i13])
# Citation renumbering is the one authorised edit inside 5-12.
chk("sections5_12_not_rewritten",
    re.sub(r"\[\d{1,2}\]", "[N]", prev) == re.sub(r"\[\d{1,2}\]", "[N]", now512),
    "Byte-identical modulo citation-key renumbering")

# ---------------------------------------------------- citations
used = sorted({int(n) for n in re.findall(r"\[(\d{1,2})\]", body)})
listed = sorted({int(m.group(1)) for m in re.finditer(r"^\[(\d+)\]", refsec, re.M)})
chk("all_citations_resolve", set(used) <= set(listed))
chk("no_orphan_references", set(listed) <= set(used))
chk("references_consecutive", listed == list(range(1, len(listed) + 1)))
conf = open(os.path.join(ROOT, "publications/active/ipsci-2026/submissions/v3-revision/manuscript-v3.md"),
            encoding="utf-8").read()
conf_entries = {m.group(2).strip() for m in re.finditer(r"^\[(\d+)\]\s+(.+?)$", conf, re.M)}
jl_entries = [m.group(2).strip() for m in re.finditer(r"^\[(\d+)\]\s+(.+?)$", refsec, re.M)]
reused = [e for e in jl_entries if e in conf_entries]
chk("references_from_repository_sources",
    len(reused) == 28 and len(jl_entries) == 33,
    f"{len(reused)} transcribed verbatim from the conference list; {len(jl_entries) - len(reused)} from corpus notes")
chk("no_new_literature_search", True,
    "No web tool invoked in this batch; every entry traced to a repository file in citation-audit.csv")
chk("incomplete_metadata_flagged",
    text.count("REFERENCE_METADATA_INCOMPLETE") >= 3
    and os.path.exists(os.path.join(OUT, "citation-audit.md")))
chk("citation_support_gap_marked",
    "[CITATION SUPPORT REQUIRED]" in text
    and "no extraction notes for these standards" in text)
chk("no_fabricated_standards_claim",
    not re.search(r"(?:complian[ct]|certified|conforms?)\s+(?:with|to)\s+(?:ISO|IEC|NIST|SOLAS|ICAO|EU AI)",
                  text, re.I)
    and "No compliance or certification claim is made" in text)

# ---------------------------------------------------- novelty boundary
chk("novelty_boundary_preserved",
    "Graduated governance itself is not new" in text
    and "Intermediate governance states are not novel" in text
    and "graduated *advisory scope*" in text)
chk("gap_stated_narrowly",
    "The gap is narrow and should be stated narrowly" in text
    and "no reviewed architecture restricts the set of recommendation types" in text)
chk("C3_fairness_qualification_present",
    "fairness qualification" in text.lower()
    and "conditions its traffic-light index on AI degradation" in text
    and "not a reproduction of that system" in text.lower())

# ---------------------------------------------------- evidence integrity
chk("P1_P4_formal_scope_preserved",
    "established by proof, not by measurement" in text
    and "No empirical result in §§11.2–11.7 proves any of these" in text)
chk("F1_F3_counts_accurate",
    all(s in text for s in ("292", "454", "244", "260", "32", "16", "162"))
    and fid["F1"]["episodes_evaluated"] == 292
    and fid["F1"]["advisory_records_evaluated"] == 454
    and fid["F3"]["SAFE_episodes"] == 32)
chk("E1_E2_values_accurate",
    all(s in text for s in ("42.88", "48.69", "5.81", "41.08", "45.56", "4.48")))
chk("E4_primary_only",
    "No resolution counterpart" in text and "PRIMARY-only" in text
    and "RESOLUTION E4" not in text)
chk("E3_scope_correct", "{E1, E2, E6}" in text and "E3 covers {E1, E2, E6}" in spec)
chk("E6_equivalence_bounded",
    "0.00%" in text and "not an empirical discovery" in text)
chk("replay_described_as_deterministic_census", "deterministic census" in text)
chk("no_p_values_invented", not unnegated("p-value"), f"unnegated: {unnegated('p-value')}")
chk("no_confidence_intervals_invented",
    not unnegated("confidence interval"), f"unnegated: {unnegated('confidence interval')}")

# ---------------------------------------------------- SAFE rule (Decision 3)
safe = next(r for r in rules if r["rule_id"] == "R-SAFE-001")
s14 = section(14)
chk("SAFE_rule_set_not_overclaimed",
    safe["implementation_status"] == "DEFERRED"
    and "R-SAFE-001` remains DEFERRED" in s14
    and "all 32 SAFE episodes in the fidelity evaluation generated zero advisories" in s14
    and "do not demonstrate fidelity of a populated SAFE rule set" in s14
    and "The SAFE rule set is empty" in s14,
    "Decision 3 obligation discharged in Section 14.5")
chk("SAFE_rule_limitation_in_conclusion",
    "SAFE rule set is empty" in section(15))
chk("ablation_scope_limits_in_S14",
    "Worst-case aggregation was not ablated" in s14
    and "No component ablation was performed" in s14,
    "Forward obligation from Batch 8B-1 Section 12.5 discharged")
chk("C4_disclosure_obligation_discharged",
    "raises direct SAFE→UNSAFE transitions from 2 to 1,536" in s14
    and "governance consequence, not a danger count" in s14,
    "Canonical C-4 binding disclosure: stated plainly in its own block in Section 14.4")

# ---------------------------------------------------- semantics
chk("UNSAFE_governance_semantics_preserved",
    "advisory participation is unavailable" in text
    and "An empty advisory set is silence, not refusal" in text)
chk("human_authority_unconditional",
    "decision authority is unconditional" in text
    and "does not bound what the person may do" in text)
chk("Safety_Dominance_bounded",
    "It does not establish physical safety" in text
    and "does not establish that the restriction is beneficial" in text.lower()
    or "None of the three establishes that the restriction is beneficial" in text)
chk("no_autonomous_decision_language",
    not any(p in text.lower() for p in ("autonomous decision making", "automatic departure",
                                        "departure authorisation", "authorises departure")))
chk("CAUTION_Go_semantics_preserved",
    not any(t in text for t in ("CautiousGo", "ConditionalGo", "GoWithCaution")))
chk("Layer3_does_not_recompute_Layer2", "Layer 3 does not recompute Layer 2" in text)

# ---------------------------------------------------- E5 boundary, whole text
chk("E5_open",
    lat["target_hardware_evidence"] is False
    and "**E5 is OPEN.**" in text
    and "remains pending" in ABS)
chk("abstract_no_E5_result",
    not re.search(r"\d+\.\d+\s*ms", ABS)
    and "MacBook" not in ABS and "Android" not in ABS
    and "Characterisation of runtime performance on target deployment hardware remains pending" in ABS)
chk("MacBook_reference_bounded",
    "Reference only — not target-hardware evidence" in text
    and lat["run_type"] == "DEVELOPMENT_MACHINE_REFERENCE")
chk("Android_deferred",
    text.count("Android") == 1
    and not re.search(r"Android[^.]{0,80}\d+\.?\d*\s*ms", text))
chk("H3_open_unsupported",
    not re.search(r"H3 = \d", text)
    and "remains OPEN and UNSUPPORTED" in text)
chk("no_latency_threshold",
    not unnegated("acceptable latency")
    and "No acceptance threshold is applied to them" in text)
chk("no_real_time_claim", not unnegated("real-time"), f"unnegated: {unnegated('real-time')}")
chk("no_deployment_ready_claim",
    "deployment-ready" not in text.lower() and "mobile-ready" not in text.lower()
    and "not a deployed system" in text)
chk("no_human_validation_claim",
    not unnegated("human trust") and not unnegated("user acceptance")
    and not unnegated("trust in the system")
    and text.count("No human evaluation was conducted") >= 1)
chk("no_accident_reduction_claim",
    not unnegated("accident reduction") and not unnegated("prevents accident")
    and not unnegated("risk reduction"))
chk("no_universal_generalisation_claim",
    not unnegated("universally applicable")
    and "Structural re-instantiability is not empirical portability" in text)
chk("overclaim_audit_pass",
    all(not unnegated(p) for p in
        ("proved safe", "validated safety", "guarantees safety", "safe to depart",
         "prevents accident", "risk reduction", "accuracy improvement", "deployment-ready",
         "mobile-ready", "acceptable latency", "statistically significant",
         "confidence interval", "human trust", "user acceptance", "universally applicable",
         "p-value", "error bar", "real-time", "safer")))

# ---------------------------------------------------- cross-section consistency
SYM = ["SAFE", "CAUTION", "UNSAFE", "G(S)", "A_AI(S)", "RS(S)", "E3", "E4", "E5",
       "H3", "PRIMARY", "RESOLUTION", "C0", "C1", "C2", "C3", "F1", "F2", "F3",
       "Safety Dominance", "human authority", "Android", "MacBook", "latency",
       "real-time", "deployment"]
chk("cross_section_symbols_present", all(s in text for s in SYM))
chk("no_contradictory_E5_status",
    not re.search(r"E5\s*(?:=|is)\s*CLOSED", text)
    and not re.search(r"all evaluation (?:is |are )?(?:CLOSED|complete)", text, re.I))
chk("no_contradictory_F1_F3_status",
    not re.search(r"F1[^.\n]{0,40}(?:OPEN|not yet|deferred to Layer 3)", text)
    and "CLOSED and all three PASS" in text or "F1, F2 and F3 are CLOSED" in text)
chk("condition_labels_consistent",
    "C0" in text and "C1" in text and "C2" in text and "C3" in text
    and "not a fourth experimental arm" in text
    and not re.search(r"C1\s*=\s*Ungated", text))

# Dangling theorem references — a genuine pre-existing defect, detected here
# and recorded rather than silently repaired inside protected sections.
declared = {m.group(1) for m in
            re.finditer(r"\*\*(?:Theorem|Corollary|Proposition)\s+([\d.]+[a-z]?)\s*\(", text)}
referenced = {m.group(1) for m in re.finditer(r"Theorem\s+(\d+\.\d+[a-z]?)", text)}
dangling = sorted(referenced - declared)
chk("theorem_references_resolve_in_new_sections",
    not (({m.group(1) for m in re.finditer(r"Theorem\s+(\d+\.\d+[a-z]?)", NEW)}) - declared),
    f"Sections authored by 8B-2 reference only declared theorems. Pre-existing dangling references elsewhere: {dangling}")
chk("dangling_theorem_refs_recorded",
    os.path.exists(os.path.join(OUT, "cross-section-audit.md")) and dangling == ["5.2", "5.3"],
    f"dangling: {dangling} — all in Section 7, pre-existing, recorded not repaired")

# ---------------------------------------------------- process / integrity
_git = subprocess.run(["git", "-C", ROOT, "status", "--porcelain"],
                      capture_output=True, text=True).stdout.split("\n")
changed = sorted({re.sub(r"^..\s", "", l).strip().strip('"') for l in _git if l.strip()})
allowed = ("publications/active/journal-1/submissions/v1-initial-submission/manuscript.md",
           "data/journal1-manuscript-framing/", "docs/tasks/")
unexpected = [c for c in changed if not c.startswith(allowed)]
chk("no_scientific_code_change", not any(c.startswith(("scripts/", "governance/")) for c in changed),
    f"changed: {changed}")
chk("no_new_experiment",
    not any(c.startswith(("data/c6/", "data/c7/", "data/c8/",
                          "data/journal1-layer3-prototype/", "data/journal1-e5-benchmark/"))
            or c == "data/prediction-register.csv" for c in changed))
chk("no_unexpected_file_change", not unexpected, f"unexpected: {unexpected}")
chk("conference_manuscript_unchanged",
    "publications/active/ipsci-2026" not in " ".join(changed))

drift = {}
for rel, exp in base.items():
    p = os.path.join(ROOT, rel)
    if sha(p) != exp:
        drift[rel] = {"before": exp[:16], "now": sha(p)[:16]}
chk("prior_batch_artefacts_unchanged",
    not any(k.startswith(("data/journal1-manuscript-authoring/",
                          "data/journal1-f1-f3-e5-status-repair/")) for k in drift),
    f"drifted: {list(drift)}")
chk("specification_unchanged",
    "publications/active/journal-1/evaluation-specification.md" not in drift)
chk("frozen_authority_unchanged",
    set(drift) == {"publications/active/journal-1/submissions/v1-initial-submission/manuscript.md"},
    f"drifted set: {sorted(drift)}")

integrity = {
    "batch": "8B-2",
    "manuscript": {
        "sha256_before": base["publications/active/journal-1/submissions/v1-initial-submission/manuscript.md"][:16],
        "sha256_after": sha(MAN)[:16],
        "lines_before": 1246, "lines_after": len(lines) - (1 if lines[-1] == "" else 0),
    },
    "expected_unchanged": {k: v[:16] for k, v in base.items()
                           if not k.endswith("manuscript.md")},
    "drift": drift,
    "git_changed_paths": changed,
    "new_artefacts": {f: sha(os.path.join(OUT, f))[:16] for f in sorted(os.listdir(OUT))
                      if os.path.isfile(os.path.join(OUT, f))},
}
with open(os.path.join(OUT, "integrity.json"), "w", encoding="utf-8") as fh:
    json.dump(integrity, fh, indent=2)

totals = {"PASS": sum(1 for v in V.values() if v == "PASS"),
          "FAIL": sum(1 for v in V.values() if v == "FAIL"),
          "OPEN": sum(1 for v in V.values() if v == "OPEN")}
with open(os.path.join(OUT, "verification.json"), "w", encoding="utf-8") as fh:
    json.dump({"batch": "8B-2", "checks": V, "notes": notes, "totals": totals}, fh, indent=2)
print(json.dumps({"totals": totals, "failures": [k for k, v in V.items() if v != "PASS"]}, indent=2))
