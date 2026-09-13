# Journal 1 — Manuscript Theorem and Definition Numbering Consistency Micro-Repair

You are acting as a **scientific manuscript consistency auditor and bounded editorial repair agent**.

This is a **MICRO-REPAIR**, not a manuscript-writing batch.

Your task is to repair the theorem/property/definition numbering inconsistency identified after Journal 1 Batch 8B-2 while preserving all scientific meaning, equations, proofs, evidence, architecture, evaluation results, citations, and manuscript structure.

Do not broaden the task.

---

# 1. ACTIVE MANUSCRIPT

Use the active Journal 1 manuscript:

`publications/active/journal-1/submissions/v1-initial-submission/manuscript.md`

The user-provided current manuscript corresponds to the post-Batch-8B-2 manuscript.

Before editing:

1. record current Git branch and HEAD;
2. compute the manuscript SHA-256;
3. record repository status;
4. identify every theorem, property, definition, lemma, proposition, corollary, and cross-reference appearing in the manuscript;
5. construct a complete declaration/reference inventory before making any change.

Do not edit anything until the inventory is complete.

---

# 2. SCIENTIFIC STATUS IS FROZEN

The following scientific status must not change:

* P1–P4 = CLOSED
* F1–F3 = CLOSED
* E1–E4 = CLOSED
* E6 = CLOSED
* E5 = OPEN
* E5 benchmark harness = CLOSED
* MacBook benchmark = development-machine REFERENCE ONLY
* E5 Android target-hardware benchmark = DEFERRED MANDATORY
* H3 = OPEN / UNSUPPORTED
* R-SAFE-001 = DEFERRED
* FINAL_REVIEWER_READY = false

This task must not reopen, reinterpret, strengthen, weaken, or close any of these items.

---

# 3. KNOWN DEFECT

Batch 8B-2 identified a pre-existing manuscript numbering defect.

At minimum, independently verify:

* Section 5 declares `Theorem 5.1 (Totality of f)`;
* Section 6 contains the canonical formal proofs;
* Section 7 contains references to `Theorem 5.2` and `Theorem 5.3`;
* `Theorem 5.2` and `Theorem 5.3` are not actually declared;
* the corresponding proved results appear in Section 6;
* one formal result appears to carry duplicate numbering across Sections 5 and 6.

Do not assume the Batch 8B-2 report is correct.

Verify all of this directly against the current manuscript.

Also search the entire manuscript for any additional numbering defects not mentioned by Batch 8B-2.

---

# 4. CANONICAL NUMBERING DECISION

Apply the following editorial decision unless direct manuscript evidence proves that doing so would alter scientific meaning:

> **Section 6 is the canonical home of proved theorems.**

Section 5 specifies the architecture, definitions, constraints, properties, and theorem motivation.

Section 6 contains the canonical theorem declarations and proofs.

Therefore:

* do not maintain duplicate theorem identities across Sections 5 and 6;
* references to proved formal results should resolve to their canonical Section 6 theorem numbers;
* Section 5 may state a property or preview a result and forward-reference its proof in Section 6;
* do not create new scientific theorems merely to preserve old numbering;
* do not renumber Section 6 theorems unless absolutely necessary;
* prefer repairing stale references over renumbering valid canonical declarations.

The desired principle is:

`SPECIFICATION / PROPERTY in §5 → CANONICAL THEOREM + PROOF in §6`

not:

`duplicate theorem declaration in §5 → second theorem declaration in §6`.

---

# 5. EXPECTED REPAIR DIRECTION

First verify the actual declarations.

If the manuscript confirms that:

* Totality is canonically proved as Theorem 6.1;
* Monotonicity is canonically proved as Theorem 6.2;
* Safety Dominance is canonically proved as Theorem 6.3;

then preserve those numbers as canonical.

Repair stale downstream references accordingly.

For example, a reference to a nonexistent:

`Theorem 5.2`

should become:

`Theorem 6.2`

**only if direct manuscript inspection confirms that the referenced statement is the Monotonicity result proved as Theorem 6.2.**

Likewise:

`Theorem 5.3`

→ `Theorem 6.3`

only where the referenced result is actually Safety Dominance.

Do not perform blind global string replacement.

Every replacement must be semantically verified in context.

---

# 6. HANDLING THE DUPLICATE THEOREM 5.1

Inspect `Theorem 5.1 (Totality of f)` in Section 5 and the corresponding theorem/proof in Section 6.

If they represent the same scientific result, eliminate the duplicate theorem identity while preserving the Section 5 specification content.

Preferred repair:

* Section 5 states the relevant totality property/result without assigning a competing theorem number;
* it explicitly points to the canonical theorem/proof in Section 6;
* Section 6 retains the canonical theorem number.

For example, conceptually:

> The classifier is total over the stated domain; this result is proved formally in Theorem 6.1.

However, preserve the manuscript's existing terminology and wording as much as possible.

Do **not** rewrite the scientific explanation simply for stylistic improvement.

If removing `Theorem 5.1` causes references such as `Property 5.1`, `Definition 5.1`, or other numbering to shift, **do not automatically renumber them**.

Theorem numbering and Definition/Property numbering are separate namespaces unless the manuscript explicitly establishes otherwise.

---

# 7. COMPLETE NUMBERING CENSUS

Before and after repair, inventory all occurrences matching at least:

* `Definition X.Y`
* `Property X.Y`
* `Theorem X.Y`
* `Lemma X.Y`
* `Proposition X.Y`
* `Corollary X.Y`
* textual references such as `Theorem X.Y`, `Definition X.Y`, etc.

For every reference, determine:

1. referenced identifier;
2. declaration exists / does not exist;
3. declaration location;
4. reference location;
5. semantic target;
6. status before repair;
7. status after repair.

The audit must detect:

* dangling references;
* duplicate theorem identifiers;
* multiple identifiers for the same theorem;
* references pointing to the wrong scientific result;
* definitions referenced under nonexistent numbers;
* stale section-local numbering;
* accidental numbering gaps only where they produce ambiguity or dangling references.

A numbering gap by itself is not automatically a defect.

---

# 8. STRICT SCOPE BOUNDARY

This task MAY modify only text necessary to repair formal-object numbering and its immediate grammatical consequences.

Allowed:

* theorem/property/definition labels;
* theorem cross-references;
* immediate phrases such as “proved in Theorem …”;
* removal of a duplicate theorem heading where the same result is canonically declared elsewhere;
* minimal connective wording needed after removing a duplicate heading;
* audit artefacts created for this task.

Not allowed:

* new scientific claims;
* new equations;
* modified equations;
* modified proofs except identifier references;
* new empirical values;
* changed empirical values;
* new experiments;
* replay;
* statistical analysis;
* Android benchmarking;
* Mac benchmark reinterpretation;
* threshold changes;
* architecture changes;
* algorithm changes;
* Layer 3 implementation changes;
* rule changes;
* citation additions;
* literature search;
* reference metadata repair;
* standards literature repair;
* figure production;
* Abstract rewriting;
* Related Work rewriting;
* Discussion rewriting;
* stylistic manuscript cleanup unrelated to numbering.

Do not opportunistically fix unrelated defects.

Record them as `OUT_OF_SCOPE_FINDING` if discovered.

---

# 9. PROTECTED SCIENTIFIC CONTENT

The following meanings must remain invariant:

### Safety Dominance

`AI(E) ⊆ A_AI(f(E))`

Do not strengthen this into physical safety, recommendation correctness, optimality, accident reduction, deployment safety, or human validation.

### Human authority

Human authority remains unconditional and final.

### UNSAFE

UNSAFE remains a governance state where AI advisory participation is unavailable.

It is not automatically:

* physical danger;
* departure prohibition;
* legal prohibition;
* certainty of harm.

### Governance pair

Preserve:

* SAFE → full advisory scope;
* CAUTION → restricted advisory scope;
* UNSAFE → empty advisory scope.

### E5

E5 remains OPEN.

No target-hardware performance conclusion may be introduced.

H3 remains OPEN / UNSUPPORTED.

---

# 10. NO SCIENTIFIC RE-NUMBERING CASCADE

Do not use a generic renumbering tool that rewrites every formal object.

The repair should be minimal.

In particular:

* preserve valid Definition numbering;
* preserve valid Property numbering;
* preserve canonical Section 6 theorem numbering;
* preserve equation numbering if any;
* preserve table numbering;
* preserve figure numbering;
* preserve citation numbering.

Only identifiers demonstrated to be inconsistent may change.

---

# 11. REQUIRED AUDIT ARTEFACTS

Create a dedicated evidence directory, for example:

`data/journal1-theorem-numbering-repair/`

Create at minimum:

### `formal-object-inventory.csv`

Suggested columns:

`object_type,identifier,declaration_section,declaration_line,title,status_before,status_after`

### `cross-reference-audit.csv`

Suggested columns:

`reference_identifier,reference_section,reference_context,target_identifier,target_section,status_before,repair_action,status_after`

### `duplicate-result-audit.md`

Document:

* whether Theorem 5.1 and Theorem 6.1 are the same result;
* evidence for that determination;
* which identity was retained;
* why;
* confirmation that scientific content was unchanged.

### `diff-audit.md`

Classify every manuscript change as:

* `NUMBERING_REPAIR`
* `CROSS_REFERENCE_REPAIR`
* `MINIMAL_GRAMMAR_REPAIR`

Anything else is a failure unless explicitly justified.

### `integrity.json`

Record:

* branch;
* HEAD before;
* HEAD after if committed;
* manuscript hash before;
* manuscript hash after;
* frozen-authority hashes;
* changed paths;
* unexpected changed paths.

### `verification.json`

Machine-readable PASS/FAIL/OPEN results.

### `report.md`

Concise scientific closure report.

---

# 12. REQUIRED VERIFICATION

At minimum verify:

1. every theorem reference resolves;
2. every definition reference resolves;
3. every property reference resolves;
4. no duplicate theorem identity remains for the same result;
5. no references to nonexistent `Theorem 5.2`;
6. no references to nonexistent `Theorem 5.3`;
7. canonical Section 6 theorem numbering remains coherent;
8. Totality references resolve to the canonical Totality theorem;
9. Monotonicity references resolve to the canonical Monotonicity theorem;
10. Safety Dominance references resolve to the canonical Safety Dominance theorem;
11. Safety Dominance equation/meaning unchanged;
12. definitions unchanged except identifiers if absolutely required;
13. properties unchanged except identifiers if absolutely required;
14. proofs scientifically unchanged;
15. equations unchanged;
16. quantitative empirical values unchanged;
17. citation keys unchanged;
18. reference list unchanged;
19. Abstract unchanged;
20. Related Work unchanged;
21. Sections 9–15 scientifically unchanged;
22. E5 remains OPEN;
23. H3 remains OPEN / UNSUPPORTED;
24. no target-hardware result introduced;
25. no scientific code changed;
26. no experiment executed;
27. no new literature search performed;
28. no frozen evaluation authority changed;
29. no algorithm specification changed;
30. no Layer 3 specification or implementation changed.

Use negative controls where useful.

A verifier that only confirms that expected strings disappeared is insufficient.

It must also establish that each repaired reference points to the **correct semantic theorem**.

---

# 13. STOP CONDITIONS

STOP without making the scientific repair if:

* Section 6 does not actually contain the expected canonical theorem results;
* `Theorem 5.2` or `Theorem 5.3` turns out to refer to scientifically different results;
* repairing the defect requires changing a proof;
* repairing it requires changing architecture semantics;
* formal authorities conflict about theorem identity;
* a renumbering cascade into equations/tables/figures becomes necessary;
* a supposed duplicate turns out to contain scientifically distinct claims.

If stopped, produce a blocker report with the exact conflicting passages.

Do not choose a new scientific interpretation.

---

# 14. SUCCESS CRITERIA

The task succeeds only if:

* the complete manuscript has no dangling theorem references;
* each theorem has one canonical identity;
* Section 6 remains the canonical home of proved theorems;
* Section 5 continues to specify the architecture without competing theorem identities;
* all cross-references resolve semantically;
* no scientific content changes;
* no empirical evidence changes;
* no E5 status changes;
* frozen authorities remain unchanged.

The maximum manuscript status after this task remains:

`DRAFT_COMPLETE_WITH_OPEN_E5_DEPENDENCY`

and:

`FINAL_REVIEWER_READY = false`

This task does not make the manuscript reviewer-ready.

---

# 15. FINAL RESPONSE FORMAT

Report:

1. branch;
2. HEAD before / after;
3. manuscript hash before / after;
4. formal objects inventoried;
5. dangling references before / after;
6. duplicate theorem identities before / after;
7. exact numbering decisions;
8. exact manuscript locations changed;
9. verification totals;
10. integrity status;
11. E5/H3 status;
12. any `OUT_OF_SCOPE_FINDING`.

Explicitly state whether:

`THEOREM_NUMBERING_DEFECT = CLOSED`

or:

`THEOREM_NUMBERING_DEFECT = OPEN`

If all checks pass, close with exactly:

`JOURNAL 1 THEOREM AND DEFINITION NUMBERING CONSISTENCY MICRO-REPAIR CLOSED — CANONICAL SECTION 6 THEOREM IDENTITIES RESTORED AND ALL FORMAL CROSS-REFERENCES RESOLVED WITHOUT SCIENTIFIC CHANGE`

Then report:

`MANUSCRIPT_STATUS = DRAFT_COMPLETE_WITH_OPEN_E5_DEPENDENCY`

`E5 = OPEN`

`H3 = OPEN/UNSUPPORTED`

`FINAL_REVIEWER_READY = false`

Do not execute another task.

Recommend at most **one** next task, but do not start it.
