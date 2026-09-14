# Diff Audit — Theorem and Definition Numbering Micro-Repair

**File changed:** `publications/active/journal-1/submissions/v1-initial-submission/manuscript.md` — **the only file modified**
**Hash:** `7b571aac8d6f9b7a` → **`9fbf75fe050a4d91`** · **Diff: 8 lines changed (+8 / −8)**
**Sections touched:** §5 (1 statement), §6 (1 identifier), §7 (5 lines of references). §§1–4 and 8–15, the Abstract, Keywords and References are byte-identical.

Every change is classified below. Nine changes across eight lines; no change falls outside the three permitted classes.

---

## NUMBERING_REPAIR — 2 changes

| # | Line | Before | After |
|---|---|---|---|
| 1 | §5 L457 | `**Theorem 5.1 (Totality of f).**` | `**Totality of f.**` |
| 2 | §6.3 L693 | `**Corollary 6.3 (Properties 5.1 and 5.2).**` | `**Corollary 6.2b (Properties 5.1 and 5.2).**` |

**Change 1** removes a duplicate theorem identity. The statement text following the label is unchanged; only the label was removed. Rationale and evidence: `duplicate-result-audit.md` §1.

**Change 2** resolves an identifier collision. `Corollary 6.3` is sited in §6.3 and derives from Theorem 6.2 — as does `Corollary 6.2` immediately above it — but its number implied association with `Theorem 6.3 (Safety Dominance Property)`, an unrelated result declared in §6.4. Renumbering to `6.2b` associates it with its parent theorem. **No theorem identifier changed**, and the corollary is referenced nowhere else in the manuscript, so no cascade occurred (verified: `corollary_6_2b_not_referenced_elsewhere`).

---

## CROSS_REFERENCE_REPAIR — 6 changes across 5 lines

Each was verified in context before editing. No global string replacement was used; every edit was applied individually against a unique anchor.

| # | Line | Reference | Repaired to | Semantic evidence in the referring text |
|---|---|---|---|---|
| 3 | §7.1 L792 | `Theorem 5.1` | `Theorem 6.1` | "exactly one `S` is returned (… / **operational totality** …)" — Totality |
| 4 | §7.2 L811 | `Theorem 5.2` ×2 | `Theorem 6.2` ×2 | "The strict containment `A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅` (… / **Monotonicity**)" |
| 5 | §7.4 L840 | `Theorem 5.3` | `Theorem 6.3` | pseudocode precondition "…produces a conclusion type outside its own conclusion — … **A4**" — assumption A4 of the Safety Dominance proof |
| 6 | §7.4 L849 | `Theorem 5.3` ×2 | `Theorem 6.3` ×2 | "(… , **Safety Dominance**)" and "the enforcement contract on which … depends" |
| 7 | §7.5 L859 | `Theorem 5.3` ×2 | `Theorem 6.3` ×2 | dependency diagram, columns L3 "**A4**" and L4 "**formal theorem**" |

**Reference 3 was not dangling before the repair** — it resolved to `Theorem 5.1`. It was *orphaned by change 1* and had to be repointed as a direct consequence. It was not listed in the task brief; it was found by the pre-edit census.

**Fixed-width block integrity (change 7).** L859 sits inside a fenced code block with column alignment. `Theorem 5.3` → `Theorem 6.3` is character-for-character equal width, so the row length and the theorem-column offset are unchanged. Verified mechanically against the pre-repair text (`fixed_width_diagram_alignment_preserved`).

---

## MINIMAL_GRAMMAR_REPAIR — 1 change

| # | Line | Before | After |
|---|---|---|---|
| 8 | §5 L459 | `Proof deferred to Section 6.2. Totality follows from…` | `This result is proved canonically as Theorem 6.1 in Section 6.2. Totality follows from…` |

This is the immediate grammatical consequence of change 1: with the theorem label removed, "Proof deferred to Section 6.2" had no theorem to attach to. The replacement names the canonical identity explicitly, which is what the governing decision asks §5 to do. **The remainder of the sentence — the entire mathematical justification — is unchanged**, as is every other word in the paragraph.

---

## Nothing else changed

Verified mechanically rather than asserted: normalising the pre-repair manuscript by exactly the transformations listed above reproduces the post-repair manuscript **byte for byte** (`no_change_beyond_authorised_identifier_edits`). Any edit outside this set — including a single inserted sentence anywhere in the document — fails that check, confirmed by negative control.

Specifically unchanged and verified individually:

| Item | Check |
|---|---|
| All 12 Definitions (5.1–5.11 incl. 5.2a) | `definitions_unchanged` |
| All 3 Properties (5.1, 5.2, 5.3) | `properties_unchanged` |
| Proofs, `∎` count, "assumptions A1–A4" | `proofs_scientifically_unchanged` |
| The four governance equations | `equations_unchanged` |
| All 15 quantitative values | `quantitative_values_unchanged` |
| Citation keys and the reference list | `citation_keys_unchanged`, `reference_list_unchanged` |
| Abstract, Keywords, §§1–4, §2, §8, §§9–15 | 6 separate checks, byte-comparison |
| E5 OPEN, H3 OPEN/UNSUPPORTED, R-SAFE-001 DEFERRED | 3 checks |
| Evaluation spec, algorithm spec, Layer 3 spec, Appendix C | 4 hash checks |
| All 31 prior-batch artefacts | `prior_batch_artefacts_unchanged` |

---

## Out-of-scope findings — recorded, not repaired

| ID | Finding | Disposition |
|---|---|---|
| **OOS-1** | `Definition 5.11` is declared before `Definition 5.10` in §5 | Per decision 4. No gap exists (5.1–5.11 all present) and **every Definition reference resolves**, so this produces no ambiguity. Renumbering would cascade into references for cosmetic gain. |
| **OOS-2** | `publications/active/journal-1/section-5-plan.md` line 273 instructs: *"Use Section 5 numbering (Theorem 5.1, 5.2, 5.3) in the journal paper"* — now contradicted by the manuscript | Not modified. The file already carries a "historical drafting plan, superseded" banner at its head, and the evaluation specification lists it as a non-maintained artefact. It is nonetheless a **stale instruction**, the residue class this project has hit repeatedly. |
| **OOS-3** | `publications/active/journal-1/session-log.md` lines 156, 199, 207 record the old Theorem 5.1/5.2/5.3 numbering | Not modified. A session log is a historical record by nature; correcting it would falsify the record of what was planned at the time. |

OOS-2 is the only one carrying any risk: a future batch reading that plan as current guidance would reintroduce the defect just repaired.
