#!/usr/bin/env python3
"""Reference metadata census for Journal 1.

Parses the manuscript References section into structured fields. Run with
`before` or `after`; the same parser produces both so they are comparable.

The parser is deliberately conservative: a field is reported only when it can
be extracted from the entry text. It never guesses, and anything it cannot
extract is reported empty so that a human-visible gap remains a gap.
"""

import csv
import json
import os
import re
import sys

ROOT = "/sessions/charming-magical-euler/mnt/research-test-2"
OUT = os.path.join(ROOT, "data/journal1-reference-standards-closure")
MAN = os.path.join(ROOT, "publications/active/journal-1/submissions/v1-initial-submission/manuscript.md")

FIELDS = ["reference_number", "authors", "title", "year", "venue", "volume",
          "issue", "pages_or_article_number", "publisher", "doi",
          "url_or_identifier", "metadata_status", "provenance_source"]


def parse(entry):
    f = dict.fromkeys(FIELDS, "")
    # authors: up to the first quoted title, or to the first comma-italic for books
    m = re.match(r'^(.*?),\s*[“"]', entry)
    f["authors"] = m.group(1).strip() if m else ""
    m = re.search(r'[“"](.+?),?[”"]', entry)
    if m:
        f["title"] = m.group(1).strip().rstrip(",")
    else:  # italicised standalone title (reports, standards, books)
        m = re.search(r"\*(.+?)\*", entry)
        if m:
            f["title"] = m.group(1).strip()
            am = re.match(r"^(.*?),\s*\*", entry)
            f["authors"] = am.group(1).strip() if am else ""
    years = re.findall(r"\b(19|20|21)(\d{2})\b", entry)
    if years:
        f["year"] = "".join(years[-1])
    m = re.search(r"\bin \*(.+?)\*", entry) or re.search(r"\*(.+?)\*", entry)
    if m and m.group(1).strip() != f["title"]:
        f["venue"] = m.group(1).strip()
    m = re.search(r"\bvol\.\s*([\w.]+)", entry)
    f["volume"] = m.group(1).rstrip(",.") if m else ""
    m = re.search(r"\bno\.\s*([\w.]+)", entry)
    f["issue"] = m.group(1).rstrip(",.") if m else ""
    m = (re.search(r"\bpp\.\s*([\d–\-]+)", entry)
         or re.search(r"\bp\.\s*([\w–\-]+)", entry)
         or re.search(r"\bart(?:icle)?\.?\s*(?:no\.)?\s*([\w–\-]+)", entry, re.I))
    f["pages_or_article_number"] = m.group(1).rstrip(",.") if m else ""
    m = re.search(r"doi:\s*([^\s\[]+)", entry)
    f["doi"] = m.group(1).rstrip(".,") if m else ""
    m = re.search(r"(arXiv:[\w.\/]+|https?://[^\s\]]+|hdl\.handle\.net/[\w./]+)", entry)
    f["url_or_identifier"] = m.group(1).rstrip(".,") if m else ""
    for pub in ("NIST", "IMO", "SRI International", "PMLR", "IEEE", "ACM", "Springer", "Elsevier"):
        if pub in entry:
            f["publisher"] = pub
            break
    if "REFERENCE_METADATA_INCOMPLETE" in entry:
        f["metadata_status"] = "REFERENCE_METADATA_INCOMPLETE"
        m = re.search(r"REFERENCE_METADATA_INCOMPLETE\s*—\s*([^\]]+)", entry)
        f["provenance_source"] = ("gap noted in entry: " + m.group(1).strip()) if m else ""
    elif "NOT_APPLICABLE" in entry:
        f["metadata_status"] = "COMPLETE_WITH_NOT_APPLICABLE_FIELD"
    else:
        f["metadata_status"] = "COMPLETE"
    return f


def main():
    tag = sys.argv[1] if len(sys.argv) > 1 else "snapshot"
    text = open(MAN, encoding="utf-8").read()
    body, _, ref = text.partition("## References")
    rows = []
    for m in re.finditer(r"^\[(\d+)\]\s+(.+?)$", ref, re.M):
        f = parse(m.group(2).strip())
        f["reference_number"] = m.group(1)
        if not f["provenance_source"]:
            f["provenance_source"] = "manuscript References section"
        rows.append(f)

    path = os.path.join(OUT, f"reference-metadata-{tag}.csv")
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)

    incomplete = [r["reference_number"] for r in rows
                  if r["metadata_status"] == "REFERENCE_METADATA_INCOMPLETE"]
    cited = sorted({int(n) for n in re.findall(r"\[(\d{1,2})\]", body)})
    listed = [int(r["reference_number"]) for r in rows]
    summary = {
        "tag": tag, "reference_count": len(rows),
        "incomplete_entries": incomplete,
        "incomplete_count": len(incomplete),
        "marker_occurrences_in_full_text": text.count("REFERENCE_METADATA_INCOMPLETE"),
        "citation_support_required_markers": text.count("[CITATION SUPPORT REQUIRED]"),
        "all_citations_resolve": set(cited) <= set(listed),
        "no_orphan_references": set(listed) <= set(cited),
        "consecutive": listed == list(range(1, len(listed) + 1)),
        "duplicate_entries": [t for t in {r["title"] for r in rows}
                              if [r["title"] for r in rows].count(t) > 1 and t],
        "missing_fields_for_incomplete": {
            r["reference_number"]: [k for k in ("doi", "pages_or_article_number",
                                                "volume", "issue")
                                    if not r[k]]
            for r in rows if r["metadata_status"] == "REFERENCE_METADATA_INCOMPLETE"},
    }
    with open(os.path.join(OUT, f"census-{tag}.json"), "w", encoding="utf-8") as fh:
        json.dump(summary, fh, indent=2)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
