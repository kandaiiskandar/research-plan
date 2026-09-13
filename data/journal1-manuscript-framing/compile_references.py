#!/usr/bin/env python3
"""Compile the Journal 1 reference list from repository sources only.

Sources of bibliographic metadata, in order of authority:
  1. publications/active/ipsci-2026/submissions/v3-revision/manuscript-v3.md
     — 40 reference entries, already verified during the conference audit.
  2. notes/*.md "Paper Identity" blocks for corpus papers not cited by the
     conference paper.

No web search is performed and no DOI, volume, issue or page value is
reconstructed from memory. Where the repository supports only partial
metadata, the entry is emitted with what exists and flagged
REFERENCE_METADATA_INCOMPLETE.

In-text keys are renumbered to order of first appearance, as the reference
list must contain exactly the works cited, numbered consecutively.
"""

import csv
import json
import os
import re

ROOT = "/sessions/charming-magical-euler/mnt/research-test-2"
OUT = os.path.join(ROOT, "data/journal1-manuscript-framing")
MAN = os.path.join(ROOT, "publications/active/journal-1/submissions/v1-initial-submission/manuscript.md")
CONF = os.path.join(ROOT, "publications/active/ipsci-2026/submissions/v3-revision/manuscript-v3.md")

# ---------------------------------------------------------------- source 1
conf_text = open(CONF, encoding="utf-8").read()
conf_refs = {}
for m in re.finditer(r"^\[(\d+)\]\s+(.+?)$", conf_text, re.M):
    conf_refs[int(m.group(1))] = m.group(2).strip()
assert len(conf_refs) == 40, f"expected 40 conference refs, got {len(conf_refs)}"

# ---------------------------------------------------------------- source 2
# Corpus papers cited by Journal 1 but not by the conference paper. Every
# field below is transcribed from the named notes file's Paper Identity block.
CORPUS = {
    41: {
        "text": ("D. Corsi, G. Amir, A. Rodríguez, C. Sánchez, G. Katz, and R. Fox, "
                 "\"Verification-guided shielding for deep reinforcement learning,\" in "
                 "*Proc. 1st Reinforcement Learning Conf. (RLC)*, 2024. "
                 "doi: 10.48550/arXiv.2406.06507"),
        "notes": "notes/Verification-Guided Shielding for Deep Reinforcement Learning.md",
        "complete": True, "missing": "",
    },
    42: {
        "text": ("H. Wang, C. M. Poskitt, and J. Sun, \"AgentSpec: Customizable runtime "
                 "enforcement for safe and reliable LLM agents,\" in *Proc. IEEE/ACM 48th "
                 "Int. Conf. Software Engineering (ICSE '26)*, Rio de Janeiro, Brazil, "
                 "Apr. 2026. [REFERENCE_METADATA_INCOMPLETE — no DOI or page range in "
                 "repository evidence]"),
        "notes": "notes/AgentSpec- Customizable Runtime Enforcement for Safe and Reliable LLM Agents.md",
        "complete": False, "missing": "DOI; page range",
    },
    43: {
        "text": ("H. Odriozola-Olalde, M. Zamalloa, and N. Arana-Arexolaleiba, \"Shielded "
                 "reinforcement learning: A review of reactive methods for safe learning,\" "
                 "in *Proc. 2023 IEEE/SICE Int. Symp. System Integration (SII)*, 2023. "
                 "doi: 10.1109/SII55687.2023.10039301 "
                 "[REFERENCE_METADATA_INCOMPLETE — no page range in repository evidence]"),
        "notes": "notes/Shielded Reinforcement Learning- A review of reactive methods for safe learning.md",
        "complete": False, "missing": "page range",
    },
    44: {
        "text": ("M. Kwon, T. Ingebrand, U. Topcu, and L. Feng, \"Adaptive shielding for safe "
                 "reinforcement learning under hidden-parameter dynamics shifts,\" "
                 "*arXiv preprint* arXiv:2506.11033v2, 2026."),
        "notes": "notes/Runtime Safety through Adaptive Shielding- From Hidden Parameter Inference to Provable Guarantees.md",
        "complete": True, "missing": "",
    },
    45: {
        "text": ("Z. Chen, M. Kang, and B. Li, \"SHIELDAGENT: Shielding agents via verifiable "
                 "safety policy reasoning,\" in *Proc. 42nd Int. Conf. Machine Learning "
                 "(ICML)*, Vancouver, Canada, PMLR 267, 2025. arXiv:2503.22738v2 "
                 "[REFERENCE_METADATA_INCOMPLETE — no DOI or page range in repository evidence]"),
        "notes": "notes/SHIELDAGENT- Shielding Agents via Verifiable Safety Policy Reasoning.md",
        "complete": False, "missing": "DOI; page range",
    },
}


def main():
    text = open(MAN, encoding="utf-8").read()
    body = text.split("## References")[0]

    # Order of first appearance in the body (excludes the References section).
    order, seen = [], set()
    for m in re.finditer(r"\[(\d{1,2})\]", body):
        k = int(m.group(1))
        if k not in seen:
            seen.add(k)
            order.append(k)

    remap = {old: new for new, old in enumerate(order, start=1)}

    # Rewrite in-text keys in one pass so no new number collides with an old one.
    def sub(m):
        return f"[{remap[int(m.group(1))]}]"

    head, sep, tail = text.partition("## References")
    head = re.sub(r"\[(\d{1,2})\]", sub, head)

    rows, entries = [], []
    for old in order:
        new = remap[old]
        if old in conf_refs:
            entry, src, complete, missing = (
                conf_refs[old],
                "publications/active/ipsci-2026/submissions/v3-revision/manuscript-v3.md",
                True, "",
            )
        else:
            c = CORPUS[old]
            entry, src, complete, missing = c["text"], c["notes"], c["complete"], c["missing"]
        entries.append(f"[{new}] {entry}")
        rows.append({
            "new_key": new,
            "conference_key": old if old in conf_refs else "",
            "reference_text": entry,
            "metadata_source": src,
            "source_type": "conference manuscript (verified)" if old in conf_refs else "corpus notes file",
            "metadata_complete": "YES" if complete else "REFERENCE_METADATA_INCOMPLETE",
            "missing_fields": missing,
            "new_to_journal1": "no" if old in conf_refs else "yes",
        })

    reflist = ("## References\n\n"
               "*Compiled from repository sources only — verified entries reused from the "
               "conference manuscript and from corpus extraction notes. No new literature "
               "search was performed and no bibliographic metadata was reconstructed. "
               "Entries marked `REFERENCE_METADATA_INCOMPLETE` carry the metadata the "
               "repository supports; the missing fields are recorded in "
               "`data/journal1-manuscript-framing/citation-audit.md` and must be completed "
               "before submission.*\n\n"
               + "\n\n".join(entries) + "\n\n---\n\n")

    tail = tail.split("---", 1)[1].lstrip("\n") if "---" in tail else ""
    open(MAN, "w", encoding="utf-8").write(head + reflist + tail)

    path = os.path.join(OUT, "citation-audit.csv")
    fields = list(rows[0].keys())
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    import pandas as pd
    with open(path, newline="", encoding="utf-8") as fh:
        chk = list(csv.DictReader(fh))
    df = pd.read_csv(path)
    res = {
        "citation-audit.csv": {
            "dictreader_rows": len(chk), "pandas_rows": int(df.shape[0]),
            "row_counts_agree": len(chk) == int(df.shape[0]) == len(rows),
            "fields_match": list(chk[0].keys()) == fields == list(df.columns),
        },
        "total_references": len(rows),
        "reused_from_conference": sum(1 for r in rows if r["new_to_journal1"] == "no"),
        "new_to_journal1_from_corpus": sum(1 for r in rows if r["new_to_journal1"] == "yes"),
        "incomplete_metadata": [r["new_key"] for r in rows
                                if r["metadata_complete"] != "YES"],
        "remap": remap,
    }
    with open(os.path.join(OUT, "reference-compilation.json"), "w", encoding="utf-8") as fh:
        json.dump(res, fh, indent=2)
    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
