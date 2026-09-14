# Journal 1 — Reference Metadata Completion and Standards Citation Gap Closure

**Date:** 2026-09-14 · **Branch:** `docs/journal1-manuscript-evidence-sync` · **HEAD:** `535d556`
**Manuscript:** `9fbf75fe050a4d91` → **`f8a0587d8e687cc1`** (5 lines changed, +5 / −5)
**Verification:** 50 PASS · 0 FAIL · 0 OPEN · **20/20 negative controls discriminating** (14 mandated + 6 extra)

---

## 1. Preflight

The theorem-numbering micro-repair was **committed** at `535d556`, and the manuscript hashed `9fbf75fe050a4d91` — the exact value the brief expected. All six numbering assertions re-verified independently: no `Theorem 5.x` anywhere, Totality = 6.1, Monotonicity = 6.2, Safety Dominance = 6.3, `Corollary 6.2b` present, zero dangling references. **No stop condition triggered**, and the two tasks are not mixed in one commit.

---

## 2. Reference metadata — CLOSED

The full References section was parsed into a 13-field census rather than inspected by eye. The `REFERENCE_METADATA_INCOMPLETE` string occurs **4 times**, but only **3 are reference entries** — the fourth was the explanatory preamble note. The brief was right to require re-derivation.

### Tier 1 exhausted first

Every repository artefact mentioning the three works was searched — comparison table, review plan, paper tracker, master coding table, review synopsis, corpus notes. **No page range or DOI existed anywhere beyond what the entries already carried.** Only then was external lookup used.

### Tier 2 results

| Ref | Field | Value | Authority |
|---|---|---|---|
| [14] | pages | 1–8 | Crossref, DOI 10.1109/SII55687.2023.10039301 |
| [14] | location | Atlanta, GA, USA | Crossref `event.location` |
| [18] | **DOI** | **10.1145/3744916.3764546** | Crossref — exact title + all three authors matched |
| [18] | pages | 2938–2950 | Crossref `"page"` |
| [18] | venue year | *Proc. 2026 IEEE/ACM 48th…* | Crossref `container-title` |
| [19] | pages | 8313–8344 | Official PMLR record, `citation_firstpage`/`lastpage` + BibTeX |
| [19] | volume | 267 | Official PMLR record |
| [19] | **DOI** | **`NOT_APPLICABLE — no DOI in the authoritative publication record`** | Official PMLR record |

**14 provenance rows: 13 VERIFIED, 1 NOT_APPLICABLE, 0 UNRESOLVED, 0 MISSING.** No field was inferred from convention, and every completed field names the record it came from.

**The [19] determination rests on positive evidence.** The official PMLR page for this paper supplies BibTeX, EndNote and APA citation blocks and **none contains a DOI field**; the record identifies this version of record by ISSN 2640-3498, volume, pages and URL. A Crossref query for the title returned nothing, but that failed lookup is *not* the basis for the classification — absence of a search result is not evidence of absence.

**The finding is scoped to this paper's record.** A follow-up micro-repair corrected both the manuscript preamble and the provenance record, which had stated that the *venue* assigns no DOI — a PMLR-wide policy claim the gathered evidence does not support. The observation is now confined to what the authoritative record for this paper shows, and two verification checks plus two negative controls guard the boundary.

One deliberate substitution is recorded rather than made silently: [19]'s arXiv preprint identifier was replaced by the version-of-record URL, since the preprint and the published paper are distinct artefacts.

`REFERENCE_METADATA_COMPLETION = CLOSED` — incomplete entries 3 → **0**, with no marker remaining and nothing falsely closed.

---

## 3. Standards gap — CLOSED_CLAIM_REMOVED

The marked passage contained **four propositions, not one**, and separating them was the work. Three were worth keeping; one was not a scientific claim at all.

**Removed:** the statement that a comparison "was planned", that the repository held no extraction notes, and that a future literature pass is required. That is research-process prose — it asserts nothing about the world, the architecture or the literature.

**Retained and rewritten as publication prose:** that integrity-level schemes assign criticality at design time and that this is distinct from runtime state classification; that the governance pair is evaluated at runtime per decision episode; and that no compliance, conformance or certification is claimed.

**Support was verified before the claim was retained.** [2] (Perez-Cerrolaza et al., *ACM Computing Surveys*) carries the design-time/runtime distinction in two independent phrasings in the repository's own extraction record: *"SIL/ASIL/DAL design-time classifications"* and *"design-time SIL/ASIL not runtime state classification"*. Support level: **DIRECT**.

**No standard was named or cited.** `IEC 61508`, `ISO 26262`, `ICAO` and `SOLAS` appear nowhere in the manuscript — verified. Obtaining and interpreting them would have been a new literature-review argument, which §11 prohibits and §22 lists as a stop condition.

**A citation-integrity trap was checked before accepting the removal:** the deleted block cited **[26]** (COLREGs). It remains cited at five other locations, so no reference was orphaned.

---

## 4. Verification — 50 PASS, 0 FAIL, 0 OPEN

All 14 mandated negative controls plus 6 extras discriminate, including mutations that insert a fake DOI, change a repaired year, downgrade the supporting citation to industry commentary, assert IEC 61508 compliance, claim certified-safe, strengthen novelty to "first", reintroduce the marker, orphan a citation, add an uncited entry, alter a theorem number, change 5.81%, flip E5 to CLOSED, pass H3, and edit `section-5-plan.md`.

**Five defects were found in my own checks, none in the manuscript** — the same pattern as the last four batches, so worth itemising:

1. **`no_publication_year_changed`** counted every 4-digit token in the reference list, so the verified venue-name correction *"Proc. **2026** IEEE/ACM 48th…"* read as a changed publication year. Now compares the parsed `year` **field** of each entry.
2. **`quantitative_values_unchanged`** counted substrings across the whole document. `454` is a substring of the new DOI `10.1145/3744916.376**454**6`. Now counts in the body only.
3. **`no_compliance_or_certification_claim`** flagged the manuscript's own disclaimers, because it matched the phrase without checking for a preceding negation. Widening the verb forms then over-reached and caught *"conforms to the specification"* — code conforming to its own spec, not to a standard. Both corrected.
4. **`novelty_claim_not_strengthened`** matched *"robustness-first architecture"* inside the **title of reference [5]** — a cited paper's name, not a claim by this manuscript. Now scans the body with a word boundary excluding `-first`.
5. **`related_work_not_broadened`** tested only that §2 got shorter. Since Outcome C removed a long paragraph, an inserted sentence still left it shorter and the control passed. Now requires every surviving paragraph to have existed before or to be the single authorised replacement.

A sixth issue was a **mis-aimed control, not a bad check**: the §21.4 mutation reworded a framing sentence instead of downgrading the attribution, so the check correctly passed. The control was rewritten to test what §21.4 specifies.

One control crashed the verifier (`.group(0)` on a `None` match); key access there is now defensive, so a removed paragraph fails the check instead of aborting the run.

---

## 5. Integrity

One file changed: the manuscript, 5 lines. Unchanged and individually verified — Abstract, Keywords, §1, §§3–15, §§5–8 including all theorems and proofs, every quantitative value in the body, every pre-existing DOI, all publication years, the evaluation and algorithm and Layer 3 specifications, Appendix C, the comparison table, the conference manuscript, and all 48 artefacts from the four preceding batches.

**`section-5-plan.md` is hash-identical** — recorded, not modified.

---

## 6. Status

```
REFERENCE_METADATA_COMPLETION = CLOSED
STANDARDS_CITATION_GAP = CLOSED_CLAIM_REMOVED
STALE_SUPERSEDED_INSTRUCTION — NON-AUTHORITATIVE (section-5-plan.md L273, unmodified)

THEOREM_NUMBERING_DEFECT = CLOSED
P1–P4 = CLOSED · F1–F3 = CLOSED · E1–E4 = CLOSED · E6 = CLOSED
E5 = OPEN · E5_HARNESS = CLOSED
MACBOOK_REFERENCE = DEVELOPMENT_MACHINE_REFERENCE
E5_ANDROID_TARGET_BENCHMARK = DEFERRED_MANDATORY
H3 = OPEN/UNSUPPORTED · R_SAFE_001 = DEFERRED

MANUSCRIPT_STATUS = DRAFT_COMPLETE_WITH_OPEN_E5_DEPENDENCY
Remaining dependencies: 6 figures unproduced; E5 target-hardware benchmark
FINAL_REVIEWER_READY = false
```

**Closure:**

```
JOURNAL 1 REFERENCE METADATA AND STANDARDS CITATION GAP CLOSURE COMPLETED —
BIBLIOGRAPHIC PROVENANCE VERIFIED AND SECTION 2.6 EVIDENCE BOUNDED WITHOUT
SCIENTIFIC SCOPE EXPANSION
```
