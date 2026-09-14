#!/usr/bin/env python3
"""Formal-object census for the Journal 1 theorem/definition numbering repair.

Run with `before` or `after` to emit a census snapshot. The same code produces
both, so the two are directly comparable.

A *declaration* is a bold-leading formal object heading. The §6.1 overview
bullets preview the three theorems and are NOT declarations; they are detected
and excluded by content (they sit inside the overview list and carry a colon
rather than a full stop), not by hard-coded line numbers, so the exclusion
survives the edits this batch makes.
"""

import csv
import json
import os
import re
import sys

ROOT = "/sessions/charming-magical-euler/mnt/research-test-2"
OUT = os.path.join(ROOT, "data/journal1-theorem-numbering-repair")
MAN = os.path.join(ROOT, "publications/active/journal-1/submissions/v1-initial-submission/manuscript.md")

TYPES = r"(Theorem|Definition|Property|Lemma|Proposition|Corollary)"
DECL = re.compile(rf"\*\*{TYPES}\s+([\w.]+?)\s*\(([^)]*)\)")
REF = re.compile(rf"\b{TYPES}\s+(\d+\.\d+[a-z]?)")


def load():
    lines = open(MAN, encoding="utf-8").read().split("\n")
    out, sec, sub = [], "", ""
    for i, l in enumerate(lines, 1):
        if l.startswith("## "):
            sec = l[3:].split(".")[0].strip()
        if l.startswith("### "):
            sub = l[4:].split(" ")[0].strip()
        out.append((i, sec, sub, l))
    return out


def is_preview(line):
    """§6.1 overview bullets: list items that preview a theorem with a colon."""
    return bool(re.match(r"^\s*[-*]\s+\*\*(Theorem|Corollary)\s+[\w.]+\s*\([^)]*\):", line))


def census():
    rows = load()
    decls, previews = {}, []
    for i, sec, sub, l in rows:
        if is_preview(l):
            for m in DECL.finditer(l):
                previews.append((m.group(1), m.group(2), sec, i))
            continue
        for m in DECL.finditer(l):
            decls.setdefault((m.group(1), m.group(2)), []).append(
                {"section": sec, "subsection": sub, "line": i,
                 "title": m.group(3).strip().rstrip(".")})
    refs = []
    for i, sec, sub, l in rows:
        for m in REF.finditer(l):
            # Skip the declaration occurrence itself on a declaration line.
            if DECL.search(l) and not is_preview(l) and m.start() == DECL.search(l).start() + 2:
                continue
            refs.append({"type": m.group(1), "identifier": m.group(2),
                         "section": sec, "line": i,
                         "context": l.strip()[:200]})
    return decls, previews, refs


def main():
    tag = sys.argv[1] if len(sys.argv) > 1 else "snapshot"
    decls, previews, refs = census()
    declared = set(decls)
    dangling = [r for r in refs if (r["type"], r["identifier"]) not in declared]
    dup_ident = {f"{t} {i}": v for (t, i), v in decls.items() if len(v) > 1}
    by_title = {}
    for (t, i), v in decls.items():
        for d in v:
            by_title.setdefault(d["title"], []).append(f"{t} {i} (§{d['section']}/L{d['line']})")
    dup_result = {k: v for k, v in by_title.items() if len(v) > 1}

    snap = {
        "tag": tag,
        "declaration_count": sum(len(v) for v in decls.values()),
        "declarations": {f"{t} {i}": v for (t, i), v in sorted(decls.items())},
        "overview_previews_excluded": [f"{t} {i} (§{s}/L{l})" for t, i, s, l in previews],
        "reference_count": len(refs),
        "dangling_references": dangling,
        "duplicate_identifiers": dup_ident,
        "same_title_two_identities": dup_result,
    }
    with open(os.path.join(OUT, f"census-{tag}.json"), "w", encoding="utf-8") as fh:
        json.dump(snap, fh, indent=2)
    print(json.dumps({
        "tag": tag,
        "declarations": snap["declaration_count"],
        "references": snap["reference_count"],
        "dangling": sorted({f"{d['type']} {d['identifier']}" for d in dangling}),
        "dangling_count": len(dangling),
        "duplicate_identifiers": list(dup_ident),
        "same_title_two_identities": dup_result,
    }, indent=2))


if __name__ == "__main__":
    main()
