# Diff Audit — Reference Metadata and Standards Citation Closure

**File changed:** `publications/active/journal-1/submissions/v1-initial-submission/manuscript.md` — **the only file modified**
**Hash:** `9fbf75fe050a4d91` → **`f8a0587d8e687cc1`** · **Diff: 5 lines changed (+5 / −5)**
**Sections touched:** §2.6 (1 paragraph) and References (4 lines). §§1, 3–15, Abstract and Keywords byte-identical.

Five changes, each in one of the four permitted classes. No change falls outside them.

---

## REFERENCE_METADATA_COMPLETION — 3 changes

### [14] Odriozola-Olalde et al. (2023)

```diff
- ... in *Proc. 2023 IEEE/SICE Int. Symp. System Integration (SII)*, 2023.
-     doi: 10.1109/SII55687.2023.10039301
-     [REFERENCE_METADATA_INCOMPLETE — no page range in repository evidence]
+ ... in *Proc. 2023 IEEE/SICE Int. Symp. System Integration (SII)*,
+     Atlanta, GA, USA, 2023, pp. 1–8. doi: 10.1109/SII55687.2023.10039301
```

Fields added: **pages 1–8**, **location Atlanta, GA, USA**. Source: Crossref DOI metadata for the DOI already in the entry (`"page":"1-8"`, `event.location`). Title, authors, year and venue were returned identically and are unchanged.

### [18] Wang, Poskitt & Sun (2026)

```diff
- ... in *Proc. IEEE/ACM 48th Int. Conf. Software Engineering (ICSE '26)*,
-     Rio de Janeiro, Brazil, Apr. 2026.
-     [REFERENCE_METADATA_INCOMPLETE — no DOI or page range in repository evidence]
+ ... in *Proc. 2026 IEEE/ACM 48th Int. Conf. Software Engineering (ICSE '26)*,
+     Rio de Janeiro, Brazil, Apr. 2026, pp. 2938–2950. doi: 10.1145/3744916.3764546
```

Fields added: **DOI 10.1145/3744916.3764546**, **pages 2938–2950**, and **"2026" in the proceedings title** (Crossref container-title: *Proceedings of the 2026 IEEE/ACM 48th International Conference on Software Engineering*). Match confirmed on the exact title and all three authors, with ORCIDs and a common affiliation.

### [19] Chen, Kang & Li (2025)

```diff
- ... in *Proc. 42nd Int. Conf. Machine Learning (ICML)*, Vancouver, Canada,
-     PMLR 267, 2025. arXiv:2503.22738v2
-     [REFERENCE_METADATA_INCOMPLETE — no DOI or page range in repository evidence]
+ ... in *Proc. 42nd Int. Conf. Machine Learning (ICML)*, Vancouver, Canada,
+     in *Proceedings of Machine Learning Research*, vol. 267, 2025, pp. 8313–8344.
+     [Online]. Available: https://proceedings.mlr.press/v267/chen25ae.html
```

Fields added: **pages 8313–8344**, **volume 267 (structured)**, **series name**, **version-of-record URL**. Source: the official PMLR publication record.

**The DOI field is classified `NOT_APPLICABLE — no DOI in the authoritative publication record`, not `UNRESOLVED`.** This is a positive finding, not a failed lookup: the official record for this paper supplies BibTeX, EndNote and APA citation blocks, and **none contains a DOI field**. The record identifies this version of record by ISSN 2640-3498, volume, page range and URL. A Crossref query for this title returned nothing, but that absence is *not* the basis for the determination — the official record is.

**Scope of the finding.** It is an observation about *this paper's* authoritative record. It is **not** a claim that PMLR assigns no DOI to any paper, which the evidence gathered here does not establish. An earlier wording of both the manuscript preamble and this audit said "venue assigns no DOI"; that generalisation was corrected by a follow-up micro-repair and is now guarded by two verification checks and two negative controls.

**One deliberate substitution:** the arXiv preprint identifier was replaced by the version-of-record URL. The preprint and the published paper are distinct artefacts, and the citation should point at the latter. Recorded in `metadata-provenance.csv` rather than made silently.

---

## CITATION_SUPPORT_REPAIR — 1 change

The References preamble previously explained the `REFERENCE_METADATA_INCOMPLETE` convention. With no entry carrying that marker, the note was stale. It was replaced with the one fact a reader or copy-editor still needs:

```diff
- *Compiled from repository sources only — verified entries reused from the conference
-  manuscript and from corpus extraction notes. No new literature search was performed
-  ... the missing fields are recorded in ... and must be completed before submission.*
+ *Reference [19] is published in Proceedings of Machine Learning Research; no DOI is
+  listed in its official PMLR publication record, so its version of record is
+  identified by volume, page range and URL.*
```

The compilation narrative was removed for the same reason as the §2.6 block: it described the authors' process rather than the work. Provenance for every field now lives in `metadata-provenance.csv`, where it is auditable without occupying manuscript prose.

---

## UNSUPPORTED_CLAIM_REMOVAL — 1 change

§2.6's `[CITATION SUPPORT REQUIRED]` block was removed and replaced by publication prose carrying the three propositions worth keeping. Full reasoning: `standards-claim-audit.md`.

The removed block contained a statement that a comparison "was planned", that "the repository contains no extraction notes for these standards", and that "closing this gap requires a literature pass that this work has not performed" — research-process notes, not scientific claims.

**Citation integrity check.** The removed block cited **[26]** (COLREGs). Before accepting the removal, [26] was confirmed still cited at five other locations — §3.1, §13.5, §13.8, §14.2 and §14.4 — so no reference was orphaned. Verified: `colregs_reference_not_orphaned`, and the whole-manuscript census reports zero orphans and zero dangling citations.

---

## CLAIM_NARROWING — 0 changes

No claim was narrowed. Outcome C removes rather than weakens.

---

## Nothing else changed

| Item | Check |
|---|---|
| Abstract, Keywords, §1, §§3–15 | 4 byte-comparison checks |
| §§5–8 (theorems, proofs, algorithms) | `theorem_sections_untouched` |
| Theorem numbering still closed | `theorem_numbering_still_closed` |
| All 15 quantitative values in the body | `quantitative_values_unchanged` |
| Publication years of all 33 entries | `no_publication_year_changed` (field-level comparison) |
| Pre-existing DOIs | `no_doi_removed_or_altered` |
| E5 OPEN, H3 OPEN/UNSUPPORTED, R-SAFE-001 DEFERRED | 3 checks |
| Evaluation spec, algorithm spec, Layer 3 spec, Appendix C, comparison table, conference manuscript | hash checks |
| All 48 prior-batch artefacts | `prior_batch_artefacts_unchanged` |
| `section-5-plan.md` | `section5_plan_unmodified` — hash-identical |

---

## Out-of-scope finding

**`section-5-plan.md` L273** — *"Use Section 5 numbering (Theorem 5.1, 5.2, 5.3) in the journal paper, not the appendix C numbering from the thesis."*

Verified present and now contradicted by the closed theorem-numbering repair. Recorded as:

```
STALE_SUPERSEDED_INSTRUCTION — NON-AUTHORITATIVE
```

**Not modified**, per Decision 3. The file already carries a "historical drafting plan, superseded" banner at its head, and the evaluation specification lists it as a non-maintained artefact. A negative control confirms the verifier would catch any edit to it.
