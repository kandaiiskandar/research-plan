#!/usr/bin/env python3
"""Audit artefacts for the reference metadata / standards citation closure."""

import csv
import json
import os

OUT = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------ provenance
PROV_FIELDS = ["reference_number", "field", "old_value", "new_value",
               "source_type", "source_identifier", "verification_status"]

CROSSREF14 = "Crossref REST API, DOI 10.1109/SII55687.2023.10039301"
CROSSREF18 = "Crossref REST API, DOI 10.1145/3744916.3764546"
PMLR19 = "Official PMLR publication record, https://proceedings.mlr.press/v267/chen25ae.html"

PROV = [
    ("14", "pages_or_article_number", "(absent)", "pp. 1–8",
     "TIER_2_CROSSREF_DOI_METADATA", CROSSREF14 + ' — "page":"1-8"', "VERIFIED"),
    ("14", "venue_location", "(absent)", "Atlanta, GA, USA",
     "TIER_2_CROSSREF_DOI_METADATA",
     CROSSREF14 + ' — event.location "Atlanta, GA, USA"', "VERIFIED"),
    ("14", "doi", "10.1109/SII55687.2023.10039301", "10.1109/SII55687.2023.10039301",
     "TIER_2_CROSSREF_DOI_METADATA", CROSSREF14 + " — DOI confirmed, unchanged",
     "VERIFIED — pre-existing value confirmed"),
    ("14", "authors/title/year/venue", "(as published)", "(unchanged)",
     "TIER_2_CROSSREF_DOI_METADATA",
     CROSSREF14 + " — all fields matched the existing entry",
     "VERIFIED — no discrepancy"),

    ("18", "doi", "(absent)", "10.1145/3744916.3764546",
     "TIER_2_CROSSREF_BIBLIOGRAPHIC_QUERY",
     CROSSREF18 + " — exact title and all three author names matched", "VERIFIED"),
    ("18", "pages_or_article_number", "(absent)", "pp. 2938–2950",
     "TIER_2_CROSSREF_BIBLIOGRAPHIC_QUERY", CROSSREF18 + ' — "page":"2938-2950"', "VERIFIED"),
    ("18", "venue", "Proc. IEEE/ACM 48th Int. Conf. Software Engineering (ICSE '26)",
     "Proc. 2026 IEEE/ACM 48th Int. Conf. Software Engineering (ICSE '26)",
     "TIER_2_CROSSREF_BIBLIOGRAPHIC_QUERY",
     CROSSREF18 + " — container-title 'Proceedings of the 2026 IEEE/ACM 48th "
     "International Conference on Software Engineering'", "VERIFIED"),
    ("18", "publisher", "(absent)", "ACM (recorded in audit; not printed in IEEE-style entry)",
     "TIER_2_CROSSREF_BIBLIOGRAPHIC_QUERY", CROSSREF18 + ' — "publisher":"ACM"', "VERIFIED"),

    ("19", "pages_or_article_number", "(absent)", "pp. 8313–8344",
     "TIER_2_OFFICIAL_PUBLICATION_RECORD",
     PMLR19 + " — citation_firstpage 8313, citation_lastpage 8344; BibTeX pages {8313--8344}",
     "VERIFIED"),
    ("19", "volume", "PMLR 267 (unstructured)", "vol. 267",
     "TIER_2_OFFICIAL_PUBLICATION_RECORD", PMLR19 + " — BibTeX volume {267}", "VERIFIED"),
    # Rationale is an observation about THIS paper's authoritative record. An
    # earlier wording said "venue assigns no DOI", which generalises to a
    # PMLR-wide policy the evidence does not establish.
    ("19", "doi", "(absent)", "(none listed in the official publication record)",
     "TIER_2_OFFICIAL_PUBLICATION_RECORD",
     PMLR19 + " — the official record for this paper supplies BibTeX, EndNote "
     "and APA citation formats; none contains a DOI field. The record identifies "
     "this version of record by ISSN 2640-3498, volume, page range and URL. "
     "Scope: an observation about this paper's record, not a claim about PMLR "
     "policy for all volumes.",
     "NOT_APPLICABLE — no DOI in the authoritative publication record"),
    ("19", "url_or_identifier", "arXiv:2503.22738v2",
     "https://proceedings.mlr.press/v267/chen25ae.html",
     "TIER_2_OFFICIAL_PUBLICATION_RECORD",
     PMLR19 + " — preprint identifier replaced by the version-of-record URL; "
     "the arXiv preprint and the published paper are distinct artefacts",
     "VERIFIED — deliberate substitution, recorded"),
    ("19", "publisher", "PMLR", "PMLR",
     "TIER_2_OFFICIAL_PUBLICATION_RECORD", PMLR19 + " — publisher PMLR confirmed",
     "VERIFIED — pre-existing value confirmed"),
    ("19", "authors/title/year", "(as published)", "(unchanged)",
     "TIER_2_OFFICIAL_PUBLICATION_RECORD",
     PMLR19 + " — Chen, Kang, Li; title and year matched the existing entry",
     "VERIFIED — no discrepancy"),
]

# ------------------------------------------------------------ citation support
CIT_FIELDS = ["claim_id", "manuscript_section", "claim_text", "citation",
              "source_type", "support_level", "status"]

CIT = [
    ("CLAIM-S2.6-01", "2.6",
     "Integrity-level schemes assign criticality at design time to a system or "
     "function, and this is distinct from a runtime state classification "
     "governing system behaviour",
     "[2] Perez-Cerrolaza et al. (2024), ACM Computing Surveys 56(7):176",
     "PEER_REVIEWED_CROSS_DOMAIN_SURVEY", "DIRECT",
     "RETAINED — supported by two independent phrasings in papers/comparison-table.md: "
     "'SIL/ASIL/DAL design-time classifications' and 'design-time SIL/ASIL not runtime "
     "state classification'"),
    ("CLAIM-S2.6-02", "2.6",
     "The governance pair specified here is evaluated at runtime, per decision "
     "episode, against the currently classified environmental state",
     "(internal — manuscript §§5, 7, 9)", "OWN_SPECIFICATION", "DIRECT",
     "RETAINED — a statement about this architecture, established in its own "
     "specification sections; requires no external citation"),
    ("CLAIM-S2.6-03", "2.6",
     "The two are complementary rather than competing; no claim of compliance, "
     "conformance or certification against any integrity-level scheme is made",
     "(no citation — explicit disclaimer)", "DISCLAIMER", "CONTEXT_ONLY",
     "RETAINED — a negative statement disclaiming a claim; needs no supporting evidence"),
    ("CLAIM-S2.6-04", "2.6",
     "A comparison against IEC 61508 SIL, ISO 26262 ASIL and maritime instruments "
     "beyond COLREGs was planned but omitted for want of repository extraction notes",
     "(none available)", "NONE", "NOT_SUPPORTED",
     "REMOVED — Outcome C. Research-process prose rather than publication prose; "
     "carried no scientific proposition and named standards for which the repository "
     "holds no evidence"),
    ("CLAIM-S2.6-05", "2.6",
     "Governance frameworks operate at organisational and lifecycle level and do not "
     "specify what an advisory system may output under a given environmental condition",
     "[22] NIST AI RMF 1.0; [23] Reuel et al.; [24] Engin & Hand; [25] Kolt et al.",
     "FRAMEWORK_AND_PEER_REVIEWED", "DIRECT",
     "UNCHANGED — pre-existing, not touched by this task"),
]

# ------------------------------------------------------------ external log
EXT_FIELDS = ["query_or_identifier", "source", "authority_type", "purpose",
              "used_or_rejected", "reason"]

EXT = [
    ("DOI 10.1109/SII55687.2023.10039301", "api.crossref.org/works/{doi}",
     "TIER_2_ITEM_1 — DOI/Crossref metadata", "Resolve missing page range for [14]",
     "USED", "Authoritative DOI registration metadata; page '1-8' plus event location; "
     "title, authors, year and venue all matched the existing entry"),
    ("query.bibliographic=AgentSpec Customizable Runtime Enforcement...",
     "api.crossref.org/works", "TIER_2_ITEM_1 — DOI/Crossref metadata",
     "Resolve missing DOI and page range for [18]", "USED",
     "First result matched the exact title and all three authors with ORCIDs and "
     "affiliation; supplied DOI, pages, publisher and container title"),
    ("ShieldAgent ... ICML 2025 PMLR v267 (web search, domain-restricted to "
     "proceedings.mlr.press)", "WebSearch", "DISCOVERY ONLY — not cited as authority",
     "Locate the official PMLR record URL for [19]", "USED FOR DISCOVERY ONLY",
     "Used solely to find the canonical URL; no metadata was taken from the search "
     "summary. All fields were read from the official record itself"),
    ("https://proceedings.mlr.press/v267/chen25ae.html", "proceedings.mlr.press",
     "TIER_2_ITEM_4 — official institutional publication record",
     "Resolve page range and establish whether a DOI exists for [19]", "USED",
     "Official version-of-record page: citation_firstpage/lastpage metadata, BibTeX, "
     "EndNote and APA blocks. No DOI in any of them — establishes NOT_APPLICABLE"),
    ("api.crossref.org query for ShieldAgent", "api.crossref.org",
     "TIER_2_ITEM_1 — DOI/Crossref metadata",
     "Cross-check whether a DOI exists for [19]", "REJECTED — returned no usable result",
     "Two queries returned empty bodies. No DOI was inferred from the absence; the "
     "NOT_APPLICABLE determination rests on the positive evidence of the official "
     "PMLR record, not on a failed lookup"),
    ("IEC 61508 / ISO 26262 / ICAO / SOLAS", "(not searched)",
     "n/a", "Would have been needed for Outcome A on the standards gap",
     "NOT SEARCHED — out of scope",
     "Decision 1 selected Outcome C. External lookup was authorised for bibliographic "
     "metadata only, not for expanding Related Work or adding standards literature"),
]


def write(name, fields, rows):
    p = os.path.join(OUT, name)
    with open(p, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow(dict(zip(fields, r)))
    return p


paths = [write("metadata-provenance.csv", PROV_FIELDS, PROV),
         write("citation-support-matrix.csv", CIT_FIELDS, CIT),
         write("external-source-log.csv", EXT_FIELDS, EXT)]

import pandas as pd
res = {}
for p, n, f in zip(paths, (len(PROV), len(CIT), len(EXT)),
                   (PROV_FIELDS, CIT_FIELDS, EXT_FIELDS)):
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
res["status_label_counts"] = {
    lab: sum(1 for r in PROV if r[6].startswith(lab))
    for lab in ("VERIFIED", "NOT_APPLICABLE", "UNRESOLVED", "MISSING")}
with open(os.path.join(OUT, "parser-test.json"), "w", encoding="utf-8") as fh:
    json.dump(res, fh, indent=2)
print(json.dumps(res, indent=2))
