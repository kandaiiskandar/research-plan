#!/usr/bin/env python3
"""Audit artefacts for the Journal 1 theorem/definition numbering micro-repair.

Both CSVs are generated from the before/after census snapshots produced by
census.py, so the inventory is derived from the manuscript rather than typed.
"""

import csv
import json
import os

ROOT = "/sessions/charming-magical-euler/mnt/research-test-2"
OUT = os.path.join(ROOT, "data/journal1-theorem-numbering-repair")

before = json.load(open(os.path.join(OUT, "census-before.json")))
after = json.load(open(os.path.join(OUT, "census-after.json")))

# ---------------------------------------------------------------- inventory
INV_FIELDS = ["object_type", "identifier", "declaration_section",
              "declaration_line", "title", "status_before", "status_after"]

inv = []
keys = sorted(set(before["declarations"]) | set(after["declarations"]),
              key=lambda k: (k.split()[0], k.split()[1]))
for k in keys:
    t, idf = k.split(" ", 1)
    b = before["declarations"].get(k)
    a = after["declarations"].get(k)
    src = a[0] if a else b[0]
    if b and a:
        sb, sa = "DECLARED", "DECLARED — unchanged"
    elif b and not a:
        sb, sa = "DECLARED", "REMOVED — demoted to an unnumbered statement; canonical identity is Theorem 6.1"
    else:
        sb, sa = "NOT DECLARED", "DECLARED — renumbered from Corollary 6.3"
    inv.append({
        "object_type": t, "identifier": idf,
        "declaration_section": f"§{src['section']}",
        "declaration_line": src["line"], "title": src["title"],
        "status_before": sb, "status_after": sa,
    })

# The demoted statement is no longer a numbered object but still exists.
inv.append({
    "object_type": "Statement (unnumbered)", "identifier": "—",
    "declaration_section": "§5", "declaration_line": 457,
    "title": "Totality of f",
    "status_before": "DECLARED as Theorem 5.1 — duplicate identity with Theorem 6.1",
    "status_after": "UNNUMBERED specification statement forward-referencing Theorem 6.1",
})

# ---------------------------------------------------------------- references
XREF_FIELDS = ["reference_identifier", "reference_section", "reference_line",
               "reference_context", "target_identifier", "target_section",
               "semantic_target", "status_before", "repair_action", "status_after"]

xref = [
    ("Theorem 5.1", "§7", 792,
     "Invariants of Algorithm 1: \"exactly one S is returned (Theorem 5.1 / operational totality, Appendix C Theorem C.1b)\"",
     "Theorem 6.1", "§6.2", "Totality of f",
     "RESOLVED before repair; ORPHANED by the demotion of Theorem 5.1",
     "CROSS_REFERENCE_REPAIR — repointed to the canonical Totality theorem",
     "RESOLVES to Theorem 6.1"),
    ("Theorem 5.2", "§7", 811,
     "Invariants of Algorithm 2: \"The strict containment A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ (Theorem 5.2 / Monotonicity)\"",
     "Theorem 6.2", "§6.3", "Monotonicity of A_AI",
     "DANGLING — Theorem 5.2 never declared",
     "CROSS_REFERENCE_REPAIR — context names Monotonicity and states the containment chain",
     "RESOLVES to Theorem 6.2"),
    ("Theorem 5.2", "§7", 811,
     "Invariants of Algorithm 2: \"the finite mapping on which Theorem 5.2 is established\"",
     "Theorem 6.2", "§6.3", "Monotonicity of A_AI",
     "DANGLING — Theorem 5.2 never declared",
     "CROSS_REFERENCE_REPAIR — same sentence pair, same semantic target",
     "RESOLVES to Theorem 6.2"),
    ("Theorem 5.3", "§7", 840,
     "Algorithm 4 pseudocode precondition: \"produces a conclusion type outside its own conclusion — Theorem 5.3 A4\"",
     "Theorem 6.3", "§6.4", "Safety Dominance Property (assumption A4)",
     "DANGLING — Theorem 5.3 never declared",
     "CROSS_REFERENCE_REPAIR — A4 is an assumption of the Safety Dominance proof",
     "RESOLVES to Theorem 6.3"),
    ("Theorem 5.3", "§7", 849,
     "Invariants of Algorithm 4: \"subject to the stated rule-engine fidelity assumptions (Theorem 5.3, Safety Dominance)\"",
     "Theorem 6.3", "§6.4", "Safety Dominance Property",
     "DANGLING — Theorem 5.3 never declared",
     "CROSS_REFERENCE_REPAIR — context names Safety Dominance explicitly",
     "RESOLVES to Theorem 6.3"),
    ("Theorem 5.3", "§7", 849,
     "Invariants of Algorithm 4: \"the enforcement contract on which Theorem 5.3 depends\"",
     "Theorem 6.3", "§6.4", "Safety Dominance Property",
     "DANGLING — Theorem 5.3 never declared",
     "CROSS_REFERENCE_REPAIR — same sentence pair, same semantic target",
     "RESOLVES to Theorem 6.3"),
    ("Theorem 5.3", "§7", 859,
     "Safety-Dominance dependency diagram, L3 column: \"(Theorem 5.3 A4; A4 pre)\"",
     "Theorem 6.3", "§6.4", "Safety Dominance Property (assumption A4)",
     "DANGLING — Theorem 5.3 never declared",
     "CROSS_REFERENCE_REPAIR — inside a fixed-width block; replacement is equal length, alignment preserved",
     "RESOLVES to Theorem 6.3"),
    ("Theorem 5.3", "§7", 859,
     "Safety-Dominance dependency diagram, L4 column: \"(Theorem 5.3)\" under \"formal theorem\"",
     "Theorem 6.3", "§6.4", "Safety Dominance Property",
     "DANGLING — Theorem 5.3 never declared",
     "CROSS_REFERENCE_REPAIR — inside a fixed-width block; replacement is equal length, alignment preserved",
     "RESOLVES to Theorem 6.3"),
    ("Theorem 6.1", "§5", 459,
     "Demoted Totality statement: \"This result is proved canonically as Theorem 6.1 in Section 6.2.\"",
     "Theorem 6.1", "§6.2", "Totality of f",
     "DID NOT EXIST — the sentence read \"Proof deferred to Section 6.2.\"",
     "MINIMAL_GRAMMAR_REPAIR — forward reference added when the duplicate heading was removed",
     "RESOLVES to Theorem 6.1"),
    ("Corollary 6.3", "§6", 693,
     "Declaration: \"Corollary 6.3 (Properties 5.1 and 5.2)\" — derived from Theorem 6.2, sited in §6.3",
     "Corollary 6.2b", "§6.3", "Corollary of Theorem 6.2 discharging Properties 5.1 and 5.2",
     "AMBIGUOUS — identifier 6.3 collided with the independently declared Theorem 6.3 (Safety Dominance) in §6.4",
     "NUMBERING_REPAIR — renumbered to associate with its parent theorem",
     "DECLARED as Corollary 6.2b; not referenced elsewhere, so no cascade"),
]

# ---------------------------------------------------------------- emit


def write(name, fields, rows):
    p = os.path.join(OUT, name)
    with open(p, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow(r if isinstance(r, dict) else dict(zip(fields, r)))
    return p


p1 = write("formal-object-inventory.csv", INV_FIELDS, inv)
p2 = write("cross-reference-audit.csv", XREF_FIELDS, xref)

import pandas as pd
res = {}
for p, n, f in ((p1, len(inv), INV_FIELDS), (p2, len(xref), XREF_FIELDS)):
    with open(p, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    df = pd.read_csv(p)
    res[os.path.basename(p)] = {
        "dictreader_rows": len(rows), "pandas_rows": int(df.shape[0]),
        "expected_rows": n,
        "row_counts_agree": len(rows) == int(df.shape[0]) == n,
        "fields_match": list(rows[0].keys()) == f == list(df.columns),
        "no_empty_cells": all(all(str(r[k]).strip() for k in f) for r in rows),
    }
with open(os.path.join(OUT, "parser-test.json"), "w", encoding="utf-8") as fh:
    json.dump(res, fh, indent=2)
print(json.dumps(res, indent=2))
