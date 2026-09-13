# Batch 8B-2 — Citation Audit

**Reference list:** 33 entries, numbered consecutively by order of first appearance.
**Machine-readable:** `citation-audit.csv` (8 columns, 33 rows) · `reference-compilation.json`

---

## 1. Provenance of every entry

| Source | Count | Basis |
|---|---|---|
| **Conference manuscript, verified entries** | **28** | `publications/active/ipsci-2026/submissions/v3-revision/manuscript-v3.md`, whose 40-entry list was verified during the conference reviewer audit. Transcribed programmatically, not retyped. |
| **Corpus extraction notes** | **5** | Paper Identity blocks in `notes/*.md` for works cited by Journal 1 but not by the conference paper. |
| **New literature search** | **0** | None performed. |
| **Invented or reconstructed metadata** | **0** | No DOI, volume, issue, page or venue value was supplied from memory. |

**New citations added relative to the conference reference pool: 5.** The original brief anticipated zero. The five additions are all pre-existing corpus papers already analysed in `papers/comparison-table.md`, drawn on to support the execution-restriction and output-filtering categories in Section 2, which the conference paper's narrower review did not need to populate. They are reuse of repository evidence, not new search.

| New key | Work | Category it supports |
|---|---|---|
| [11] | Corsi et al. (2024) — verification-guided shielding | §2.1 execution restriction |
| [12] | Kwon et al. (2026) — adaptive shielding | §2.1 execution restriction |
| [14] | Odriozola-Olalde et al. (2023) — shielded RL review | §2.1 execution restriction |
| [18] | Wang, Poskitt & Sun (2026) — AgentSpec | §2.3 output filtering |
| [19] | Chen, Kang & Li (2025) — SHIELDAGENT | §2.3 output filtering |

---

## 2. Incomplete metadata — 3 entries

These carry the metadata the repository supports and are flagged in the reference list itself. **They must be completed before submission**; completing them requires consulting the publications, which is outside this batch's authorisation.

| Key | Work | Present | Missing |
|---|---|---|---|
| **[14]** | Odriozola-Olalde et al. (2023) | Authors, title, venue, year, DOI | Page range |
| **[18]** | Wang, Poskitt & Sun (2026) | Authors, title, venue, location, month, year | DOI; page range |
| **[19]** | Chen, Kang & Li (2025) | Authors, title, venue, location, PMLR volume, year, arXiv ID | DOI; page range |

The remaining 30 entries carry complete bibliographic metadata.

---

## 3. Resolution check

- Every in-text key `[1]`–`[33]` resolves to a reference entry. **Verified programmatically.**
- Every reference entry is cited at least once — no orphan entries. **Verified programmatically.**
- Numbering is consecutive from 1 with no gaps. **Verified programmatically.**
- The conference paper's numbering was **not** carried over: 33 of its 40 entries are not cited here, so retaining the old keys would have left gaps. In-text keys were remapped in a single pass to order of first appearance, and `reference-compilation.json` records the full old → new mapping for traceability.

---

## 4. Citation-dependent claims requiring future repair

**One `[CITATION SUPPORT REQUIRED]` marker remains in the manuscript**, in Section 2.6.

> A comparison against functional-safety integrity-level schemes (IEC 61508 SIL, ISO 26262 ASIL) and maritime regulatory instruments beyond COLREGs Rule 20(b) was planned for Section 2 and for the Section 13 discussion. **The repository contains no extraction notes for any of these standards**, and no bibliographic entry for them is supported by repository evidence.

This was handled by omission plus an explicit marker rather than by assertion from general knowledge. Two repository-supported observations were retained in its place: that integrity-level schemes assign criticality at design time whereas the governance pair is evaluated at runtime, and that a cross-domain survey [2] distinguishes design-time criticality classification from runtime governance mechanisms.

The same gap propagates to Section 13.8, which states that no compliance or certification claim is made and declines the comparison for the same reason. **Neither section asserts a standards relationship it cannot support.**

Closing this requires a bounded literature pass adding extraction notes for the relevant standards — a separate authorised task, not manuscript repair.

---

## 5. What was deliberately not done

- No web search, and no attempt to retrieve any publication.
- No citation added to support a claim that the repository could not already support.
- No standards citation fabricated to fill the Section 2.6 gap.
- No DOI or page range inferred for the three incomplete entries.
- The conference manuscript was **read only**; its reference list is unchanged.
