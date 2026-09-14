# Journal 1 — Reference Metadata Completion and Standards Citation Gap Closure

You are acting as a **scientific evidence, citation, and bibliographic provenance auditor** for Journal 1.

This is a **bounded documentation/evidence-closure task**.

The manuscript scientific architecture, formal results, algorithms, implementation fidelity results, empirical results, evaluation design, and theorem numbering are frozen.

Your task is to resolve:

1. the remaining `REFERENCE_METADATA_INCOMPLETE` entries; and
2. the explicit `[CITATION SUPPORT REQUIRED]` standards-comparison gap in Section 2.6,

using traceable evidence and without expanding the scientific scope of the paper.

Do not start any other manuscript task.

---

# 1. PREFLIGHT — STOP IF THE PREVIOUS REPAIR IS NOT COMMITTED

Before doing anything:

1. record Git branch;
2. record HEAD;
3. record `git status`;
4. compute SHA-256 of the active manuscript;
5. verify that the theorem-numbering micro-repair is present;
6. verify that:

   * `Theorem 5.1` no longer exists as a competing theorem identity;
   * canonical Totality = `Theorem 6.1`;
   * canonical Monotonicity = `Theorem 6.2`;
   * `Corollary 6.2b` exists;
   * canonical Safety Dominance = `Theorem 6.3`;
   * no dangling theorem references remain.

Expected post-repair manuscript prefix:

`9fbf75fe050a4d91`

The previous task should already be committed.

If the manuscript repair itself is still uncommitted, STOP and report:

`BLOCKED — THEOREM NUMBERING MICRO-REPAIR MUST BE COMMITTED BEFORE REFERENCE/CITATION CLOSURE`

Do not mix the two tasks into one commit.

---

# 2. ACTIVE MANUSCRIPT

Use:

`publications/active/journal-1/submissions/v1-initial-submission/manuscript.md`

Read the **entire current manuscript**, not only Section 2 or References.

This is necessary because a bibliographic repair must verify both:

* the reference entry; and
* every manuscript claim that cites it.

---

# 3. FROZEN SCIENTIFIC STATUS

The following status is frozen:

* P1–P4 = CLOSED
* F1–F3 = CLOSED
* E1–E4 = CLOSED
* E6 = CLOSED
* E5 = OPEN
* E5_HARNESS = CLOSED
* MacBook benchmark = DEVELOPMENT-MACHINE REFERENCE ONLY
* E5 Android target-hardware benchmark = DEFERRED MANDATORY
* H3 = OPEN / UNSUPPORTED
* R-SAFE-001 = DEFERRED
* THEOREM_NUMBERING_DEFECT = CLOSED
* FINAL_REVIEWER_READY = false

This task must not change any of these.

---

# 4. FIRST TASK — COMPLETE REFERENCE METADATA CENSUS

Before editing, parse the entire References section.

Build a census containing at minimum:

`reference_number`
`authors`
`title`
`year`
`venue`
`volume`
`issue`
`pages_or_article_number`
`publisher`
`doi`
`url_or_identifier`
`metadata_status`
`provenance_source`

Identify every occurrence of:

`REFERENCE_METADATA_INCOMPLETE`

Batch 8B-2 reported three incomplete entries.

Do not assume there are still exactly three.

Re-derive the count from the current manuscript.

For each incomplete entry, determine exactly which fields are missing.

---

# 5. REFERENCE METADATA SOURCE HIERARCHY

Use this hierarchy.

## Tier 1 — existing repository evidence

Search existing repository materials first:

* conference manuscript and verified reference list;
* literature-review artefacts;
* citation maps;
* evidence matrices;
* existing corpus notes;
* canonical documentation;
* prior manuscript versions;
* reference provenance artefacts.

If complete metadata is available there, use it.

Record the exact repository source.

## Tier 2 — authoritative external bibliographic source

Only if repository evidence is insufficient, external verification is permitted for **metadata completion**.

Prefer:

1. DOI/Crossref metadata;
2. publisher journal page;
3. official standards-body page;
4. official institutional publication record;
5. recognised bibliographic index.

Do not use:

* citation-generator websites;
* SEO bibliography pages;
* ResearchGate metadata as primary authority;
* random PDFs;
* blogs;
* AI-generated bibliography;
* unverified Google snippets.

External search in this task is for **verification and completion**, not literature expansion.

---

# 6. STRICT RULE — NEVER INVENT METADATA

Never infer:

* DOI;
* volume;
* issue;
* page range;
* article number;
* publisher;
* edition;
* publication year;
* report number;

from formatting conventions or similar papers.

Every completed field must have provenance.

If authoritative metadata cannot be established, retain:

`REFERENCE_METADATA_INCOMPLETE`

and classify the exact missing field as:

`UNRESOLVED`

Do not fabricate completeness merely to remove the marker.

---

# 7. SECOND TASK — SECTION 2.6 STANDARDS GAP

Locate the surviving:

`[CITATION SUPPORT REQUIRED]`

marker in Section 2.6.

Read the complete paragraph and determine the **exact proposition** the missing citation would be required to support.

Do not begin by searching for the named standards.

First write the proposition as a structured claim.

For example:

`CLAIM-S2.6-01 = <exact manuscript proposition>`

Then classify it:

* descriptive;
* comparative;
* novelty-supporting;
* normative;
* contextual.

Determine whether the proposition is actually necessary to the paper's argument.

---

# 8. STANDARDS PREVIOUSLY MENTIONED IN PLANNING ARE NOT AUTHORITIES

Earlier planning material mentioned possible comparisons involving:

* IEC 61508;
* ISO 26262;
* ICAO safety-assurance concepts;
* SOLAS.

Those planning notes are **not evidence**.

Do not cite these standards merely because an earlier stub or planning file named them.

Each standard may enter the manuscript only if:

1. an authoritative source is obtained;
2. the exact relevant provision/concept is identified;
3. that provision supports the manuscript's actual proposition;
4. the comparison is scientifically necessary;
5. the manuscript does not overstate what the standard says.

---

# 9. PREFERRED SOURCES FOR STANDARDS CLAIMS

For standards/regulatory claims, use **primary or authoritative sources wherever possible**.

Examples of acceptable source classes:

* ISO official catalogue / standard description;
* IEC official standard page;
* ICAO official publication/material;
* IMO official material;
* NIST official publication;
* official government or intergovernmental regulatory material.

Secondary academic literature may contextualise a standard, but should not replace the primary source when the claim concerns what the standard itself requires or defines.

---

# 10. THREE POSSIBLE OUTCOMES FOR THE STANDARDS GAP

The standards gap must end in exactly one of these states.

## Outcome A — SUPPORTED

Use this only if authoritative evidence directly supports the exact proposition.

Then:

* insert the minimum necessary citation(s);
* remove `[CITATION SUPPORT REQUIRED]`;
* do not expand the paragraph beyond what the evidence supports.

Status:

`STANDARDS_CITATION_GAP = CLOSED_SUPPORTED`

## Outcome B — CLAIM NARROWED

Use this if the general comparison is defensible but the existing wording exceeds available evidence.

Then:

* narrow the sentence;
* preserve the manuscript's argument;
* cite authoritative evidence;
* document exactly what wording was weakened and why.

Status:

`STANDARDS_CITATION_GAP = CLOSED_CLAIM_NARROWED`

This is allowed only as a citation-evidence repair, not as a new scientific contribution.

## Outcome C — CLAIM REMOVED

Use this if the standards comparison is unnecessary or cannot be supported without speculative interpretation.

Then:

* remove only the unsupported standards-comparison sentence;
* preserve surrounding Related Work logic;
* document why removal is scientifically safer than adding weak citations.

Status:

`STANDARDS_CITATION_GAP = CLOSED_CLAIM_REMOVED`

**Do not keep an unsupported claim merely because it sounds useful.**

---

# 11. DO NOT TURN THIS INTO A NEW LITERATURE REVIEW

Prohibited:

* broad searches for additional related work;
* adding papers because they are interesting;
* rewriting Section 2;
* expanding the novelty argument;
* adding new research gaps;
* adding new standards frameworks unrelated to the exact Section 2.6 proposition;
* comparing the architecture against every safety standard;
* creating a standards taxonomy;
* adding governance frameworks opportunistically.

The task is:

`close existing evidence gaps`

not:

`strengthen the literature review`.

---

# 12. NOVELTY CLAIM MUST REMAIN NARROW

Do not strengthen the manuscript's novelty claim.

The bounded distinction remains:

> graduated governance exists; the identified gap concerns graduated **AI advisory scope** conditioned on environmental state.

Do not transform this into claims such as:

* no safety standard supports graduated control;
* no prior system has multiple safety states;
* no previous architecture restricts AI output;
* first formally verified AI governance architecture;
* first safety-state AI system;
* first human-in-the-loop safety architecture.

Any such statement requires separate evidence and is outside this task.

---

# 13. SAFETY-STANDARD SEMANTICS

Do not imply that compliance with or similarity to a standard proves this architecture safe.

In particular, no standards citation may be used to claim:

* certification;
* compliance;
* conformance;
* deployment safety;
* physical safety;
* accident reduction;
* regulatory approval;
* recommendation correctness.

Unless the manuscript has actually undergone the corresponding process, those claims are prohibited.

The standards discussion is contextual/comparative only.

---

# 14. EXISTING GOVERNANCE REFERENCES

Existing repository-supported governance references may be used where they genuinely support the existing text.

Examples previously identified in repository evidence include:

* NIST AI RMF 1.0;
* COLREGs Rule 20(b);
* IMO material/statistics.

However:

**re-verify their exact repository evidence before using them.**

Do not treat this task brief as citation authority.

---

# 15. STALE SECTION-5 PLAN INSTRUCTION

A previous audit identified a superseded instruction in:

`section-5-plan.md`

that still says, in substance:

`Use Section 5 numbering (Theorem 5.1, 5.2, 5.3) in the journal paper.`

This is now contradicted by the closed theorem-numbering repair.

Do NOT use that instruction as authority.

Search the relevant planning file and verify the stale instruction exists.

Preferred handling:

* preserve historical provenance;
* do not silently rewrite historical scientific records;
* if the file already has a superseded banner, record the stale instruction in this task's audit as:

`STALE_SUPERSEDED_INSTRUCTION — NON-AUTHORITATIVE`

Only modify the planning file if an explicit active-authority mechanism requires a clarification to prevent future agents from treating the stale line as current instruction.

If modification is unnecessary, leave it untouched.

This issue must not reopen theorem numbering.

---

# 16. PROTECTED MANUSCRIPT CONTENT

Except for the bounded reference/citation repairs authorised here, preserve:

* Abstract;
* Keywords;
* Introduction;
* architecture;
* all definitions;
* all properties;
* all theorems;
* all corollaries;
* all equations;
* all algorithms;
* all pseudocode;
* thresholds;
* evaluation design;
* experimental results;
* tables;
* quantitative values;
* discussion;
* threats to validity;
* conclusion.

No theorem numbering change is permitted.

---

# 17. NO NEW SCIENTIFIC WORK

Do not:

* modify code;
* execute a scientific experiment;
* regenerate empirical results;
* perform retrospective replay;
* run Android benchmarks;
* perform human evaluation;
* change thresholds;
* change architecture;
* change Layer 3 rules;
* modify evaluation specifications;
* modify algorithm specifications;
* modify canonical Appendix C.

Bibliographic verification scripts are permitted.

Scientific computation is not.

---

# 18. REQUIRED ARTEFACT DIRECTORY

Create:

`data/journal1-reference-standards-closure/`

At minimum produce:

### `reference-metadata-before.csv`

Complete pre-repair census.

### `reference-metadata-after.csv`

Post-repair census.

### `metadata-provenance.csv`

Suggested columns:

`reference_number,field,old_value,new_value,source_type,source_identifier,verification_status`

### `standards-claim-audit.md`

Include:

* exact Section 2.6 proposition;
* claim classification;
* whether the claim is necessary;
* evidence considered;
* evidence rejected;
* final outcome A/B/C;
* exact rationale.

### `citation-support-matrix.csv`

Suggested columns:

`claim_id,manuscript_location,claim_text,citation,source_type,support_level,status`

Use bounded support labels such as:

* `DIRECT`
* `PARTIAL`
* `CONTEXT_ONLY`
* `NOT_SUPPORTED`

Do not call partial evidence direct.

### `external-source-log.csv`

If external verification is used:

`query_or_identifier,source,authority_type,purpose,used_or_rejected,reason`

### `diff-audit.md`

Every manuscript edit classified as:

* `REFERENCE_METADATA_COMPLETION`
* `CITATION_SUPPORT_REPAIR`
* `CLAIM_NARROWING`
* `UNSUPPORTED_CLAIM_REMOVAL`

No other class should appear.

### `integrity.json`

Record hashes and changed paths.

### `verification.json`

Machine-readable checks.

### `report.md`

Final closure report.

---

# 19. REFERENCE CONSISTENCY AUDIT

After repair, verify the entire manuscript:

1. every in-text numeric citation resolves to a reference;
2. every reference is cited at least once;
3. no orphan references;
4. no duplicate reference entries;
5. numbering is consecutive;
6. no citation renumbering error;
7. citation groups remain syntactically valid;
8. no `REFERENCE_METADATA_INCOMPLETE` remains unless explicitly classified UNRESOLVED;
9. no invented DOI;
10. no invented bibliographic field;
11. every modified metadata field has provenance.

If any incomplete metadata remains unresolved, do not falsely close:

`REFERENCE_METADATA_COMPLETION`

as fully complete.

Report:

`PARTIAL — AUTHORITATIVE METADATA UNAVAILABLE`

instead.

---

# 20. STANDARDS CITATION VERIFICATION

Verify:

1. `[CITATION SUPPORT REQUIRED]` is either properly resolved or explicitly retained because closure failed;
2. every standards-related proposition has evidence;
3. every cited standard actually supports the wording attached to it;
4. no compliance claim was introduced;
5. no certification claim was introduced;
6. no physical-safety guarantee was introduced;
7. no novelty claim was strengthened;
8. no unsupported standard was added merely because it appeared in planning notes.

---

# 21. WHOLE-MANUSCRIPT NEGATIVE CONTROLS

Verification must discriminate against at least these mutations:

1. insert a fake DOI into a repaired reference;
2. change a repaired publication year;
3. remove the source supporting the standards claim;
4. replace a direct-support citation with a context-only citation;
5. insert “complies with IEC 61508”;
6. insert “certified safe”;
7. strengthen the novelty claim to “first”;
8. reintroduce `[CITATION SUPPORT REQUIRED]` after a claimed closure;
9. orphan an in-text citation;
10. create an uncited reference;
11. change a theorem number;
12. change 5.81% to another value;
13. change E5 from OPEN to CLOSED;
14. change H3 to PASS.

A verifier that only searches for absence of markers is insufficient.

---

# 22. STOP CONDITIONS

STOP and report rather than guessing if:

* an incomplete reference cannot be uniquely identified;
* two authoritative bibliographic records conflict materially;
* the standards proposition cannot be mapped to a precise authoritative source;
* resolving the standards gap would require a new literature-review argument;
* resolving it would require changing the architecture;
* resolving it would require strengthening novelty;
* the current manuscript differs materially from the expected post-numbering-repair baseline;
* theorem numbering is no longer in the closed state;
* E5 status has changed unexpectedly.

Do not solve scientific uncertainty with editorial confidence.

---

# 23. SUCCESS CRITERIA

The task succeeds only if:

### References

* every resolvable incomplete metadata field is completed from traceable evidence;
* every modification has provenance;
* no metadata is invented;
* citation/reference consistency remains intact.

### Standards

* the Section 2.6 marker is resolved by Outcome A, B, or C;
* the final sentence is evidence-supported;
* no compliance or certification implication is introduced;
* novelty remains bounded.

### Scientific integrity

* no theorem changes;
* no equation changes;
* no quantitative result changes;
* no evaluation status changes;
* no scientific code changes;
* no new experiment;
* frozen authorities remain unchanged.

---

# 24. FINAL STATUS RULES

Possible reference status:

`REFERENCE_METADATA_COMPLETION = CLOSED`

or, if authoritative metadata genuinely remains unavailable:

`REFERENCE_METADATA_COMPLETION = PARTIAL — AUTHORITATIVE METADATA UNAVAILABLE`

Possible standards status:

`STANDARDS_CITATION_GAP = CLOSED_SUPPORTED`

or:

`STANDARDS_CITATION_GAP = CLOSED_CLAIM_NARROWED`

or:

`STANDARDS_CITATION_GAP = CLOSED_CLAIM_REMOVED`

or, only if no defensible closure is possible:

`STANDARDS_CITATION_GAP = OPEN`

Regardless of outcome:

`E5 = OPEN`

`H3 = OPEN/UNSUPPORTED`

`FINAL_REVIEWER_READY = false`

Do not claim reviewer-ready status.

---

# 25. FINAL REPORT FORMAT

Report exactly:

1. branch;
2. HEAD before / after;
3. manuscript hash before / after;
4. reference count before / after;
5. incomplete references before / after;
6. exact metadata fields repaired;
7. provenance for each repair;
8. Section 2.6 claim audited;
9. standards sources considered;
10. standards sources used/rejected;
11. standards outcome A/B/C;
12. manuscript lines changed;
13. citation consistency result;
14. verification PASS/FAIL/OPEN totals;
15. negative-control result;
16. integrity status;
17. stale `section-5-plan.md` instruction status;
18. E5/H3 status;
19. remaining manuscript dependencies.

If both documentation gaps close successfully, use:

`JOURNAL 1 REFERENCE METADATA AND STANDARDS CITATION GAP CLOSURE COMPLETED — BIBLIOGRAPHIC PROVENANCE VERIFIED AND SECTION 2.6 EVIDENCE BOUNDED WITHOUT SCIENTIFIC SCOPE EXPANSION`

Do not automatically use the word `CLOSED` if either subtask remains unresolved.

Finally recommend **exactly one next task**.

Do not execute it.
