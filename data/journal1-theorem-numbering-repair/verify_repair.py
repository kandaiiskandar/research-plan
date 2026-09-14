#!/usr/bin/env python3
"""Verification for the theorem/definition numbering micro-repair.

Per the task brief: "A verifier that only confirms that expected strings
disappeared is insufficient. It must also establish that each repaired
reference points to the correct semantic theorem."

Semantic checks therefore work in two steps: read the TITLE of the theorem the
repaired reference now points at, and require that title to match the concept
named in the referring sentence. A reference repaired to the wrong theorem
fails even though the old string is gone.
"""

import csv
import hashlib
import json
import os
import re
import subprocess

ROOT = "/sessions/charming-magical-euler/mnt/research-test-2"
OUT = os.path.join(ROOT, "data/journal1-theorem-numbering-repair")
MAN = os.path.join(ROOT, "publications/active/journal-1/submissions/v1-initial-submission/manuscript.md")


def sha(p):
    with open(p, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


text = open(MAN, encoding="utf-8").read()
lines = text.split("\n")
before = json.load(open(os.path.join(OUT, "census-before.json")))
after = json.load(open(os.path.join(OUT, "census-after.json")))
base = json.load(open(os.path.join(OUT, "baseline-hashes.json")))
V, notes = {}, {}


def chk(name, cond, note=None):
    V[name] = "PASS" if cond else "FAIL"
    if note:
        notes[name] = note


def line(n):
    return lines[n - 1]


def line_of(anchor):
    """Locate a line by content, not by number.

    Hard-coded line numbers made four negative controls crash the verifier
    instead of failing it: inserting a line shifts every number below it, so
    the check then inspects the wrong line or indexes past the end. Every
    content lookup below is anchored on text that the repair does not move.
    """
    for l in lines:
        if anchor in l:
            return l
    return ""


# Titles of the canonical declarations, taken from the census snapshot.
#
# An earlier version re-derived these with a second parser whose
# preview-exclusion test searched the WHOLE document for a bullet form: because
# §6.1 previews Theorems 6.1-6.3, that test skipped their real declarations too
# and the title map came back missing every theorem. The census already
# excludes previews correctly, so it is used as the single source rather than
# duplicating the parsing logic.
TITLE = {k: v[0]["title"] for k, v in after["declarations"].items()}

chk("canonical_titles_readable",
    TITLE.get("Theorem 6.1") == "Totality of f"
    and TITLE.get("Theorem 6.2") == "Monotonicity of A_AI"
    and TITLE.get("Theorem 6.3") == "Safety Dominance Property",
    f"{ {k: v for k, v in TITLE.items() if k.startswith(('Theorem', 'Corollary'))} }")


def semantic(name, anchor, ident, concept):
    """The referring line names `concept`; EVERY theorem it cites must be `ident`,
    and `ident`'s declared title must carry `concept`.

    Requiring *every* citation on the line — not merely one — is the correction
    that made this check discriminate. The first version accepted the line if
    `ident` appeared anywhere on it, so mis-pointing one of two references on a
    line (L811 and L849 each cite their theorem twice) went undetected by
    negative control even though the reference was now semantically wrong.
    """
    ctx = line_of(anchor)
    tgt = TITLE.get(ident, "")
    cited = set(re.findall(r"Theorem \d+\.\d+[a-z]?", ctx))
    chk(name,
        bool(ctx) and cited == {ident}
        and concept.lower() in ctx.lower() and concept.lower() in tgt.lower(),
        f"line anchored on {anchor!r} cites {sorted(cited)} in a context naming "
        f"'{concept}'; {ident} is titled '{tgt}'")


# ------------------------------------------------ 1-3: references resolve
declared = set(after["declarations"])
dang = after["dangling_references"]
chk("every_theorem_reference_resolves",
    not [d for d in dang if d["type"] == "Theorem"], f"dangling: {dang}")
chk("every_definition_reference_resolves",
    not [d for d in dang if d["type"] == "Definition"], f"dangling: {dang}")
chk("every_property_reference_resolves",
    not [d for d in dang if d["type"] == "Property"], f"dangling: {dang}")
chk("every_corollary_reference_resolves",
    not [d for d in dang if d["type"] == "Corollary"], f"dangling: {dang}")
chk("no_dangling_references_at_all", len(after["dangling_references"]) == 0,
    f"before={len(before['dangling_references'])} after={len(after['dangling_references'])}")

# ------------------------------------------------ 4-6: identities
chk("no_duplicate_theorem_identity_for_same_result",
    "Totality of f" not in after["same_title_two_identities"],
    f"remaining same-title pairs: {list(after['same_title_two_identities'])}")
chk("no_references_to_Theorem_5_2", "Theorem 5.2" not in text)
chk("no_references_to_Theorem_5_3", "Theorem 5.3" not in text)
chk("no_references_to_Theorem_5_1", "Theorem 5.1" not in text)
chk("no_duplicate_identifiers", not after["duplicate_identifiers"],
    f"{after['duplicate_identifiers']}")

# ------------------------------------------------ 7: canonical §6 coherent
# Missing keys must FAIL the check, never raise. An earlier version indexed
# after["declarations"][...] directly; under a negative-control mutation that
# removed the key, the verifier crashed instead of failing, verification.json
# was left holding the previous run's results, and the control appeared to pass.
def sub_of(ident):
    d = after["declarations"].get(ident)
    return d[0]["subsection"] if d else None


chk("canonical_section6_numbering_coherent",
    all(k in declared for k in ("Theorem 6.1", "Theorem 6.2", "Theorem 6.3",
                                "Corollary 6.2", "Corollary 6.2b"))
    and "Corollary 6.3" not in declared
    and sub_of("Theorem 6.1") == "6.2"
    and sub_of("Theorem 6.2") == "6.3"
    and sub_of("Theorem 6.3") == "6.4"
    and sub_of("Corollary 6.2b") == "6.3",
    f"declared corollaries: {[k for k in declared if k.startswith('Corollary')]}")
chk("corollary_6_2b_sited_with_parent_theorem",
    sub_of("Corollary 6.2b") is not None
    and sub_of("Corollary 6.2b") == sub_of("Theorem 6.2"),
    "Corollary 6.2b sits in §6.3 with Theorem 6.2, from which it derives")
chk("corollary_6_2b_not_referenced_elsewhere",
    text.count("Corollary 6.2b") == 1, "No cascade — declaration only")

# ------------------------------------------------ 8-10: SEMANTIC targets
semantic("totality_reference_semantically_correct",
         "exactly one `S` is returned", "Theorem 6.1", "totality")
semantic("monotonicity_reference_semantically_correct",
         "The strict containment `A_AI(SAFE)", "Theorem 6.2", "Monotonicity")
semantic("safety_dominance_reference_semantically_correct",
         "The governed advisory output is constrained", "Theorem 6.3", "Safety Dominance")
chk("safety_dominance_diagram_reference_correct",
    "(Theorem 6.3 A4; A4 pre)" in text and "formal theorem" in text
    and TITLE.get("Theorem 6.3") == "Safety Dominance Property")
chk("safety_dominance_pseudocode_reference_correct",
    "Theorem 6.3 A4)" in line_of("conclusion type outside its own conclusion"))
chk("section5_forward_reference_correct",
    "proved canonically as Theorem 6.1 in Section 6.2" in text
    and TITLE.get("Theorem 6.1") == "Totality of f")
# Concept and identifier can appear in either order within a sentence, so the
# wrong-target scan must be bidirectional. A one-directional version missed a
# mis-pointed reference where the concept followed the identifier.
WRONG = [("Monotonicity", r"6\.[13]"),
         ("Safety Dominance", r"6\.[12]"),
         ("[Tt]otality", r"6\.[23]")]
_wrong_hits = []
for concept, badnum in WRONG:
    # The gap must exclude newlines and table pipes: an earlier version used
    # [^.] and matched across adjacent rows of the Table 7 evaluation matrix,
    # pairing "Theorem 6.1" in the P1 row with "Monotonicity" in the P2 row.
    for pat in (rf"{concept}[^.\n|]{{0,80}}Theorem {badnum}\b",
                rf"Theorem {badnum}\b[^.\n|]{{0,80}}{concept}"):
        _wrong_hits += [m.group(0)[:90] for m in re.finditer(pat, text)]
chk("no_reference_points_to_wrong_result", not _wrong_hits, f"hits: {_wrong_hits}")

# ------------------------------------------------ 11-16: science invariant
chk("safety_dominance_equation_unchanged",
    text.count("AI(E) ⊆ A_AI(f(E))") == before_count_sd
    if (before_count_sd := open(os.path.join(OUT, "manuscript.before.md"),
                                encoding="utf-8").read().count("AI(E) ⊆ A_AI(f(E))")) else False)
prev = open(os.path.join(OUT, "manuscript.before.md"), encoding="utf-8").read()


def norm(s):
    """Strip only the identifiers this repair is allowed to touch."""
    s = s.replace("**Theorem 5.1 (Totality of f).**", "**Totality of f.**")
    s = s.replace("Proof deferred to Section 6.2.",
                  "This result is proved canonically as Theorem 6.1 in Section 6.2.")
    s = re.sub(r"Theorem 5\.1", "Theorem 6.1", s)
    s = re.sub(r"Theorem 5\.2", "Theorem 6.2", s)
    s = re.sub(r"Theorem 5\.3", "Theorem 6.3", s)
    s = s.replace("Corollary 6.3 (Properties", "Corollary 6.2b (Properties")
    return s


chk("no_change_beyond_authorised_identifier_edits", norm(prev) == text,
    "Normalising the before-text by exactly the seven authorised substitutions reproduces the after-text byte for byte")
chk("definitions_unchanged",
    {k: v for k, v in before["declarations"].items() if k.startswith("Definition")}
    == {k: v for k, v in after["declarations"].items() if k.startswith("Definition")})
chk("properties_unchanged",
    {k: v for k, v in before["declarations"].items() if k.startswith("Property")}
    == {k: v for k, v in after["declarations"].items() if k.startswith("Property")})
chk("property_5_3_pattern_preserved",
    "Property 5.3 (Safety Dominance Property)" in text
    and "Theorem 6.3 (Safety Dominance Property)" in text,
    "Specification-level property in §5, canonical proved theorem in §6 — intentional, per decision 3")
chk("proofs_scientifically_unchanged",
    prev.count("∎") == text.count("∎")
    and all(s in text for s in ("Proof.", "by exhaustive case analysis", "assumptions A1–A4")))
chk("equations_unchanged",
    all(text.count(e) == prev.count(e) for e in
        ("AI(E) ⊆ A_AI(f(E))", "A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅",
         "A_AI(UNSAFE) ⊊ A_AI(CAUTION) ⊊ A_AI(SAFE)", "G(S) = 0 ⟹ A_AI(S) = ∅")))
chk("quantitative_values_unchanged",
    all(text.count(v) == prev.count(v) for v in
        ("5.81", "4.48", "42.88", "48.69", "41.08", "45.56", "0.00%",
         "3,661", "3,439", "10.36", "292", "454", "244", "162", "1,536")))
def prev_line_of(anchor):
    for l in prev.split("\n"):
        if anchor in l:
            return l
    return ""


_now_cols = line_of("   L1                    L2")
_was_cols = prev_line_of("   L1                    L2")
_now_row = line_of("(Def 5.6)           (Algorithm 3)")
_was_row = prev_line_of("(Def 5.6)           (Algorithm 3)")
chk("fixed_width_diagram_alignment_preserved",
    bool(_now_cols) and _now_cols == _was_cols
    and len(_now_row) == len(_was_row)
    and _now_row.index("(Theorem") == _was_row.index("(Theorem"),
    "Column header row unchanged; the repaired row is the same length and starts "
    "the theorem column at the same offset (5.3 → 6.3 is equal width)")

# ------------------------------------------------ 17-21: untouched regions
chk("citation_keys_unchanged",
    re.findall(r"\[\d{1,2}\]", prev) == re.findall(r"\[\d{1,2}\]", text))
chk("reference_list_unchanged",
    prev.partition("## References")[2] == text.partition("## References")[2])


def sect(src, n):
    L = src.split("\n")
    i = next(i for i, l in enumerate(L) if re.match(rf"^## {n}\. ", l))
    j = next(k for k in range(i + 1, len(L)) if L[k].startswith("## "))
    return "\n".join(L[i:j])


def named(src, h):
    L = src.split("\n")
    i = next(i for i, l in enumerate(L) if l == h)
    j = next(k for k in range(i + 1, len(L)) if L[k].startswith("## "))
    return "\n".join(L[i:j])


chk("abstract_unchanged", named(prev, "## Abstract") == named(text, "## Abstract"))
chk("keywords_unchanged", named(prev, "## Keywords") == named(text, "## Keywords"))
chk("related_work_unchanged", sect(prev, 2) == sect(text, 2))
chk("sections_9_15_unchanged",
    all(sect(prev, n) == sect(text, n) for n in range(9, 16)),
    "Sections 9-15 byte-identical")
chk("sections_1_4_unchanged", all(sect(prev, n) == sect(text, n) for n in range(1, 5)))
chk("only_sections_5_and_7_changed",
    sect(prev, 6) != sect(text, 6)  # Corollary renumber lives in §6
    and sect(prev, 8) == sect(text, 8)
    and all(sect(prev, n) == sect(text, n) for n in (1, 2, 3, 4, 9, 10, 11, 12, 13, 14, 15)),
    "Changed: §5 (demotion), §6 (Corollary 6.2b), §7 (references). All others byte-identical")

# ------------------------------------------------ 22-30: frozen status
chk("E5_remains_open",
    "**E5 is OPEN.**" in text
    and json.load(open(os.path.join(ROOT, "data/journal1-e5-benchmark/latency-results.json")))
    ["target_hardware_evidence"] is False)
chk("H3_remains_open_unsupported",
    not re.search(r"H3 = \d", text) and "remains OPEN and UNSUPPORTED" in text)
chk("no_target_hardware_result_introduced",
    text.count("Android") == prev.count("Android") == 1
    and "Reference only — not target-hardware evidence" in text)
chk("R_SAFE_001_deferred_preserved", "R-SAFE-001` remains DEFERRED" in text)
chk("safety_dominance_meaning_not_strengthened",
    "It does not establish physical safety" in text
    and "does not bound what the person may do" in text)
chk("UNSAFE_semantics_preserved",
    "advisory participation is unavailable" in text
    and "An empty advisory set is silence, not refusal" in text)
chk("governance_pair_preserved",
    "A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅" in text)

_git = subprocess.run(["git", "-C", ROOT, "status", "--porcelain"],
                      capture_output=True, text=True).stdout.split("\n")
changed = sorted({re.sub(r"^..\s", "", l).strip().strip('"') for l in _git if l.strip()})
allowed = ("publications/active/journal-1/submissions/v1-initial-submission/manuscript.md",
           "data/journal1-theorem-numbering-repair/", "docs/tasks/")
unexpected = [c for c in changed if not c.startswith(allowed)]
chk("no_scientific_code_changed",
    not any(c.startswith(("scripts/", "governance/")) for c in changed), f"changed: {changed}")
chk("no_experiment_executed",
    not any(c.startswith(("data/c6/", "data/c7/", "data/c8/",
                          "data/journal1-layer3-prototype/", "data/journal1-e5-benchmark/"))
            or c == "data/prediction-register.csv" for c in changed))
chk("no_literature_search_performed",
    "publications/active/ipsci-2026" not in " ".join(changed)
    and re.findall(r"\[\d{1,2}\]", prev) == re.findall(r"\[\d{1,2}\]", text))
chk("no_unexpected_file_change", not unexpected, f"unexpected: {unexpected}")

drift = {}
for rel, exp in base.items():
    p = os.path.join(ROOT, rel)
    if sha(p) != exp:
        drift[rel] = {"before": exp[:16], "now": sha(p)[:16]}
chk("frozen_evaluation_authority_unchanged",
    "publications/active/journal-1/evaluation-specification.md" not in drift)
chk("algorithm_specification_unchanged",
    "publications/active/journal-1/algorithm-specification.md" not in drift)
chk("layer3_specification_unchanged",
    "publications/active/journal-1/layer3-prototype-specification.md" not in drift)
chk("canonical_appendix_c_unchanged",
    "docs/canonical/appendix-c-formalisation.md" not in drift)
chk("prior_batch_artefacts_unchanged",
    not any(k.startswith(("data/journal1-manuscript-authoring/",
                          "data/journal1-f1-f3-e5-status-repair/",
                          "data/journal1-manuscript-framing/")) for k in drift),
    f"drifted: {list(drift)}")
chk("only_manuscript_changed_among_frozen",
    set(drift) == {"publications/active/journal-1/submissions/v1-initial-submission/manuscript.md"},
    f"drifted: {sorted(drift)}")

_diff = subprocess.run(["git", "-C", ROOT, "diff", "--numstat", "--", MAN],
                       capture_output=True, text=True).stdout.strip()
ins, dele = (int(x) for x in _diff.split("\t")[:2]) if _diff else (0, 0)
chk("minimal_diff", ins <= 10 and dele <= 10, f"+{ins} -{dele}")

integrity = {
    "batch": "theorem-numbering-repair", "date": "2026-09-14",
    "branch": subprocess.run(["git", "-C", ROOT, "branch", "--show-current"],
                             capture_output=True, text=True).stdout.strip(),
    "HEAD_before": "dca5aed", "HEAD_after": "dca5aed (uncommitted)",
    "manuscript": {"sha256_before": base["publications/active/journal-1/submissions/v1-initial-submission/manuscript.md"][:16],
                   "sha256_after": sha(MAN)[:16], "diff": f"+{ins} -{dele}"},
    "frozen_authority_hashes": {k: sha(os.path.join(ROOT, k))[:16] for k in base
                                if not k.startswith("data/")},
    "changed_paths": changed, "unexpected_changed_paths": unexpected,
    "drift_among_baseline_files": drift,
}
with open(os.path.join(OUT, "integrity.json"), "w", encoding="utf-8") as fh:
    json.dump(integrity, fh, indent=2)

totals = {"PASS": sum(1 for v in V.values() if v == "PASS"),
          "FAIL": sum(1 for v in V.values() if v == "FAIL"),
          "OPEN": sum(1 for v in V.values() if v == "OPEN")}
with open(os.path.join(OUT, "verification.json"), "w", encoding="utf-8") as fh:
    json.dump({"batch": "theorem-numbering-repair", "checks": V,
               "notes": notes, "totals": totals}, fh, indent=2)
print(json.dumps({"totals": totals, "failures": [k for k, v in V.items() if v != "PASS"]}, indent=2))
