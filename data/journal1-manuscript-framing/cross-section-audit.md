# Batch 8B-2 — Cross-Section Consistency and Overclaim Audit

**Scope:** the complete manuscript — Abstract through Section 15, plus References.
**Manuscript:** `a91ede5ff8518e46` → `7b571aac8d6f9b7a` (1,246 → 1,662 lines)

---

## 1. Symbol and status consistency

Each symbol below was traced across every section that uses it and checked for a contradictory statement.

| Symbol / status | Sections | Result |
|---|---|---|
| `SAFE` / `CAUTION` / `UNSAFE` | 1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15 | **Consistent.** UNSAFE is a governance state in which advisory participation is unavailable, everywhere it is defined or used. No section equates it with certain danger or prohibition. |
| `G(S)` / `A_AI(S)` | 1, 3, 4, 5, 6, 7, 9, 10, 11, 13, 14, 15 | **Consistent.** Participation and advisory scope are separated identically in §1.1, §3.2 and §4.3. |
| `RS(S)` | 4, 5, 7, 9, 10, 14 | **Consistent.** `RS(UNSAFE) = ∅` is the absence of a rule set, not an empty collection, in §5 and §9. `RS(SAFE)` is empty in the prototype in §9.3, §11.2, §14.5 and §15. |
| `F1`–`F3` | 9, 10, 11, 13, 14 | **Consistent — CLOSED PASS throughout.** No surviving statement that fidelity is open, future, or deferred to a Layer 3 build. |
| `E1`, `E2` | 10, 11, 12, 13, 14, Abstract | **Consistent.** 42.88 / 48.69 / 5.81 and 41.08 / 45.56 / 4.48 identical in every occurrence. |
| `E3` scope | 10, 11, 12, 14 | **Consistent — `{E1, E2, E6}`** in every mention; matches the evaluation specification. |
| `E4` | 9, 11, 12, 14 | **Consistent — PRIMARY-only.** No RESOLUTION analogue anywhere, and no resolution-insensitivity claim. |
| `E5` | 1, 8, 10, 11, 13, 14, 15, Abstract | **Consistent — OPEN in all eight.** |
| `H3` | 8, 10, 11, 14 | **Consistent — OPEN/UNSUPPORTED.** No numeric substitution anywhere. |
| `PRIMARY` / `RESOLUTION` | 10, 11, 12, 13, 14 | **Consistent.** Described as two measurements and a sensitivity result, never as an interval, in all five. |
| `C0` / `C1` / `C2` | 4, 10, 11, 12, 13 | **Consistent.** No residue of the retired journal-local labelling. |
| `C3` | 10, 11, 12, 13, 14 | **Consistent — structural comparator, never a fourth arm.** The fairness qualification and the modelling premise travel with it in §10.1, §13.3 and §14.8. |
| Safety Dominance | 1, 3, 4, 5, 6, 7, 9, 11, 13, 14, 15 | **Consistent and bounded.** Every statement of the property is accompanied by what it does not establish. |
| Human authority | 1, 3, 4, 5, 7, 9, 13, 14 | **Consistent — unconditional in all.** |
| `Android` | 11 only | **One occurrence, inside a prohibition.** |
| `MacBook` | 11 only | Development-machine reference, labelled at point of use. |
| `latency` / `real-time` / `deployment` | 1, 3, 8, 9, 10, 11, 13, 14, 15 | **Consistent.** Every performance-adjacent statement is bounded or negated. |

**No contradiction was found between any two sections on any of these.**

## 2. Known cross-section tension, resolved by wording

**§8 versus §13.6 on resource claims.** Section 8 warns that "small fixed state space, therefore suitable for low-resource deployment" is not a valid inference. Section 13.6 argues that determinism and offline operation make the design suitable for low-resource settings. These would contradict if §13.6 were a performance claim; it is labelled explicitly as a design argument, and closes by stating that whether the implementation meets any device budget is exactly what §11.7 does not establish. §14.7 repeats the warning. **Consistent as written.**

---

## 3. Overclaim audit — whole manuscript

Every prohibited phrase was scanned across the full text, with each occurrence required to sit inside a sentence whose negation *precedes* the term.

| Phrase | Occurrences | Unnegated | Outcome |
|---|---|---|---|
| proved safe / proven safe | 0 | 0 | — |
| validated safety | 0 | 0 | — |
| guarantees safety / guarantees safe | 0 | 0 | — |
| safe to depart | 0 | 0 | — |
| prevents accidents | 0 | 0 | — |
| risk reduction | 2 | **0** | Both inside prohibitions (§11.4, §13.2) |
| accuracy improvement | 1 | **0** | Prohibition (§11.4) |
| deployment-ready / mobile-ready | 0 | 0 | — |
| acceptable latency | 0 | 0 | — |
| statistically significant | 0 | 0 | — |
| confidence interval | 2 | **0** | §10.5, §14.9 — both prohibitions |
| p-value | 2 | **0** | §10.5, §14.9 — both prohibitions |
| error bar | 1 | **0** | Prohibition (§10.5) |
| human trust | 1 | **0** | Prohibition (§13.9) |
| user acceptance | 0 | 0 | — |
| universally applicable | 0 | 0 | — |
| real-time | 3 | **0** | All three prohibitions (§11.7, §14.7) |
| "safer" | 3 | **0** | All inside the explicit refusal of the reading (§11.4, §13.2) |

**Outcome: 0 unnegated occurrences. Nothing justified, bounded, replaced or removed was required** — every occurrence was authored inside its bound.

**One wording change was made as a result of this audit.** §14.9 originally read *"Reporting p-values, confidence intervals or significance tests over it would impute sampling variability to an enumeration that has none, and none is reported."* The prohibition trailed the terms, which is both harder to detect mechanically and weaker prose. Rewritten to lead with it: *"No p-value, confidence interval or significance test is reported anywhere in this paper, because reporting one would impute sampling variability to an enumeration that has none."* Meaning unchanged.

---

## 4. Defect found and **not** repaired — dangling theorem references

**Section 7 refers seven times to theorems that are declared nowhere in the manuscript.**

| Reference | Occurrences | Location | Declared? |
|---|---|---|---|
| Theorem 5.1 | 1 | §7.1 | Yes — §5.3 (line 457) |
| **Theorem 5.2** | **2** | §7.2 | **No** |
| **Theorem 5.3** | **5** | §7.4, §7.5 | **No** |

The results these refer to exist, under different numbers: Monotonicity is **Theorem 6.2** and Safety Dominance is **Theorem 6.3**, both declared in §6. Section 5 additionally declares a **Theorem 5.1** (Totality) that restates §6's **Theorem 6.1**, so the same result carries two numbers.

**A reviewer would find this immediately**, and it is the kind of defect that costs credibility disproportionately to its severity.

**It was not repaired in this batch**, for two reasons. Sections 5–8 are protected, modifiable only where drafting exposes a *direct scientific contradiction*; this is a cross-reference defect, not a contradiction of evidence, and no scientific claim is wrong. And the fix requires a decision this batch is not authorised to take: either §5's duplicate Theorem 5.1 is removed and §7 repointed to 6.1–6.3, or §5 becomes the declaring section and §6 is renumbered. Those have different consequences for the structure of §§5–6.

**All sections authored by 8B-2 use the §6 numbering exclusively** (verified: `theorem_references_resolve_in_new_sections`), matching the evaluation specification. The defect is confined to §7 and is recorded here and in the report as the recommended next task.

---

## 5. Stub audit

| Marker | Occurrences | Classification |
|---|---|---|
| `UNDRAFTED` | **0** | All twelve Batch 8A markers discharged |
| `(Draft here)` / `(Draft after results)` / `(Draft last)` | **0** | Discharged |
| `To be written` / `To be compiled` | **0** | Discharged |
| `Purpose:` / `Key content to include` planning blocks | **0** | Discharged |
| `TODO` / `TBD` / `placeholder` | **0** | None present |
| `[CITATION SUPPORT REQUIRED]` | **1** | §2.6 — **justified OPEN dependency**, retained deliberately. No repository evidence supports a functional-safety standards comparison; omitting the marker would hide the gap. |
| `REFERENCE_METADATA_INCOMPLETE` | **3** | References [14], [18], [19] — **justified OPEN dependency**. Metadata the repository does not carry; completion requires consulting the publications. |
| Figures placeholder | 1 | **Production note, not a drafting stub.** Six figures are named and specified; producing them is a separate task. |
| Author affiliation `[Your university]` | 1 | **Submission-metadata placeholder**, not scientific content. |

**No substantive manuscript section contains a drafting stub.** Every remaining marker is either a scientifically justified open dependency or a production/metadata item, and none was removed for cosmetic completeness.
