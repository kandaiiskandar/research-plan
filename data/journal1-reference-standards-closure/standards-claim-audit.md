# Standards Claim Audit — Section 2.6

**Outcome: C — CLAIM REMOVED** · `STANDARDS_CITATION_GAP = CLOSED_CLAIM_REMOVED`

---

## 1. The exact proposition carried by the marked passage

The `[CITATION SUPPORT REQUIRED]` block contained four distinct propositions, not one. Separating them was the necessary first step, because only one of them was a scientific claim at all.

```
CLAIM-S2.6-01  Integrity-level schemes assign criticality at DESIGN TIME to a
               system or function, and this is distinct from a runtime state
               classification governing system behaviour.

CLAIM-S2.6-02  The governance pair specified here is evaluated AT RUNTIME, per
               decision episode, against the currently classified environmental
               state.

CLAIM-S2.6-03  No claim of compliance, conformance or certification against any
               integrity-level scheme is made.

CLAIM-S2.6-04  A comparison against IEC 61508 SIL, ISO 26262 ASIL and maritime
               instruments beyond COLREGs Rule 20(b) "was planned for this
               section"; "the repository contains no extraction notes for these
               standards"; "closing this gap requires a literature pass that this
               work has not performed."
```

## 2. Classification and necessity

| Claim | Classification | Necessary to the paper's argument? | Evidence status |
|---|---|---|---|
| **S2.6-01** | **Comparative / contextual** | **Yes** — it positions the contribution against the most familiar safety-engineering framing a Safety Science reader will bring | **DIRECT support from [2]** |
| **S2.6-02** | Descriptive, about this architecture | Yes | Established in §§5, 7, 9 of this manuscript; needs no external citation |
| **S2.6-03** | Normative disclaimer | Yes — it prevents a misreading | A negative statement; requires no supporting evidence |
| **S2.6-04** | **Research-process note** | **No** | **None** |

**S2.6-04 is not a scientific proposition.** It describes the authors' workflow — what was planned, what the internal repository did or did not contain, and what a future pass would need to do. It asserts nothing about the world, the architecture, or the literature. Its presence in a manuscript is a category error regardless of whether the standards could be cited.

## 3. Evidence considered

### Accepted

**[2] Perez-Cerrolaza et al. (2024)**, *Artificial intelligence for safety-critical systems in industrial and transportation domains: A survey*, ACM Computing Surveys 56(7), art. 176. doi: 10.1145/3626314

Support for S2.6-01 was verified against the repository's own extraction record before the claim was retained. `papers/comparison-table.md` records the survey's position in two independent phrasings:

- *"Class I/II/III taxonomy; **SIL/ASIL/DAL design-time classifications**; safety envelope concept; no formal runtime governance model"*
- *"Binary runtime governance universal across all surveyed domains; no Level 2 advisory scope governance; **design-time SIL/ASIL not runtime state classification**"*

This is a peer-reviewed cross-domain survey stating precisely the design-time/runtime distinction the manuscript draws. **Support level: DIRECT.** It is secondary literature *about* the standards rather than the standards themselves — which is appropriate here, because the claim concerns how integrity-level schemes are positioned relative to runtime governance, not what any clause of any standard requires.

### Rejected — not sought

**IEC 61508, ISO 26262, ICAO safety-assurance material, SOLAS.** No authoritative source was obtained and none was cited.

Three reasons, in order:

1. **Decision 1 selected Outcome C**, which resolves the gap by removal rather than by citation.
2. **Obtaining and interpreting these standards would constitute a new literature-review argument**, which task §11 prohibits and §22 lists as a stop condition. External lookup in this task was authorised for bibliographic metadata only.
3. **Naming them in planning material is not evidence** (§8). The standards appeared in a §3 drafting stub and in `papers/review-plan.md`; neither is an authority, and the corpus contains **zero** extraction notes for any of them — verified by search.

Had Outcome A been attempted, the manuscript would have acquired citations to primary standards documents that no one on this project has read into the repository, to support a comparison the paper does not need. That is the failure mode the brief's §8 exists to prevent.

## 4. What changed

**Removed** — the entire `[CITATION SUPPORT REQUIRED]` block, containing S2.6-04 and the process prose.

**Retained, rewritten as publication prose** — S2.6-01, S2.6-02 and S2.6-03, which the block had buried:

> A related distinction concerns the integrity-level schemes used in functional safety. A cross-domain survey of AI in safety-critical industrial and transportation systems records that such schemes assign criticality **at design time** to a system or function, and that this is distinct from a runtime state classification governing system behaviour [2]. The governance pair specified here operates on the other side of that distinction: it is evaluated **at runtime**, per decision episode, against the currently classified environmental state. The two are complementary rather than competing, and no claim of compliance, conformance or certification against any integrity-level scheme is made or implied.

**No standard is named.** The paragraph discusses integrity-level schemes as a class, which is exactly what [2] supports and no more. Verified: `no_new_standards_citation_added` confirms the strings `IEC 61508`, `ISO 26262`, `ICAO` and `SOLAS` appear nowhere in the manuscript.

## 5. Boundaries held

| Requirement | Result |
|---|---|
| No compliance, conformance or certification claim | **PASS** — the paragraph disclaims all three explicitly; every such phrase in the manuscript is negated |
| No physical-safety guarantee | **PASS** |
| Novelty not strengthened | **PASS** — no "first" claim; the bounded framing "graduated governance itself is not new" is intact |
| No absolute negative claim about standards | **PASS** — the manuscript does not say that no standard supports graduated control |
| Related Work not broadened | **PASS** — §2 is shorter, and every surviving paragraph either predates this task or is the single authorised replacement |
| Comparison necessary, not decorative | The retained distinction earns its place; the removed comparison did not |

## 6. Why removal is safer than weak citation

The alternative was to cite IEC 61508 and ISO 26262 for a general statement about design-time integrity levels. That would have looked more scholarly and been less honest: the citations would have been to documents absent from this project's evidence base, supporting a claim already carried by a source that *is* in the evidence base and that states it directly.

The claim the paper needs survives, with better support than the standards themselves would have provided for this particular proposition. What was lost is a note about work not done — which belongs in a task report, not a manuscript.
