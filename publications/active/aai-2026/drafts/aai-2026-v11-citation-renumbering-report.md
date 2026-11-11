# AAI 2026 — Citation Renumbering Change Report (v11)

| Item | Value |
|---|---|
| Input | `[Rewrite v4] aai-2026-manuscript-v10-final-A4(4).docx`, SHA-256 `629afb1e5f406b35989a232587913fa150dbde13554c0bfaa0e8e65810e23db9` |
| Output (DOCX) | `aai-2026-manuscript-v11-renumbered-A4.docx`, SHA-256 `387d34f52ab4cce49c3e4ce57b626c65a3356f63e89354f8f5d5743550883a95` |
| Output (PDF) | `aai-2026-manuscript-v11-renumbered-A4.pdf`, SHA-256 `e8f614aa99f708579ccd8753c1a0e62a21c1c1a31646e1de8b8a56aeaa169686` |
| Date | 27 October 2026 |
| Scope | Citation numbering and bibliography order only |
| Verdict | **Renumbering complete and validated. Page count 7 — exceeds the AAI 2026 six-page limit (pre-existing in the input, not caused by this edit).** |

The original file was opened read-only and is not modified.

---

## 1. Citation mechanism found

No reference-manager fields are present: the document contains zero `fldChar`, `instrText`, `ADDIN CITATION` or content-control constructs. In-text citations are **manually typed bracketed text**. Bibliography numbers are **automatic** — paragraph style `references` carries `numId 8`, whose level-0 format is `[%1]`. Reordering a bibliography paragraph therefore renumbers the list by itself; no entry text contains a hard-coded number.

Instruction 4 (update the underlying references rather than displayed text) therefore does not apply to the in-text citations, and instruction 5 governs: a single simultaneous mapping pass was used, not sequential find-and-replace, so no intermediate collision was possible (`[7]→[8]` could not be re-read as the old `[8]`). All 31 in-text edits were computed as offsets first and applied last-to-first in one pass.

---

## 2. Citation mapping applied

| Old | New | Source | In-text occurrences |
|---|---|---|---|
| [1]–[6] | unchanged | NIST; ASTM; Alshiekh et al.; FAA; Parasuraman et al.; Batool et al. | 13 |
| **[20]** | **[7]** | **Corsi et al.** | 1 |
| [7] | [8] | Aarab | 1 |
| [8] | [9] | Miller | 1 |
| [9] | [10] | Kim et al. | 1 |
| [10] | [11] | Flehmig et al. | 1 |
| [11] | [12] | Open-Meteo | 1 |
| [12] | [13] | Zippenfenig | 1 |
| [13] | [14] | Hersbach et al. | 1 |
| [14] | [15] | MMD — strong wind | 1 |
| [15] | [16] | MMD — thunderstorm | 1 |
| [16] | [17] | Jeong and Im | 4 |
| [17] | [18] | Yaakob et al. | 2 |
| [18] | [19] | IMO (COLREGs) | 1 |
| [19] | [20] | DID Malaysia | 1 |

**31 in-text citations** were rewritten or verified. The mapping was asserted to be a bijection on 1–20 before any edit, and the per-number occurrence counts were asserted to transfer exactly (e.g. old `[16]`×4 → new `[17]`×4).

Three citations — Corsi `[20]`, MMD-thunderstorm `[15]` and DID `[19]` — had their digits typed in a separate text run from their brackets (`[` + `20` + `]` across three runs). These were rewritten across the run boundary into the first run; the runs carried no distinguishing formatting, so the rendering is unchanged.

The bracket pair `[13], [14]` (Open-Meteo archive, formerly `[12], [13]`) was handled as two independent citations. No citation ranges of the form `[3]–[5]` occur in the document.

---

## 3. Bibliography ordering

The Corsi paragraph was moved from position 20 to position 7, immediately before Aarab. Automatic numbering produced the rest.

Resulting order, with the old number each entry held:

| New | Entry | Old |
|---|---|---|
| [1] | National Institute of Standards and Technology | 1 |
| [2] | ASTM International | 2 |
| [3] | M. Alshiekh et al. | 3 |
| [4] | Federal Aviation Administration | 4 |
| [5] | R. Parasuraman et al. | 5 |
| [6] | A. Batool et al. | 6 |
| **[7]** | **D. Corsi, G. Amir, A. Rodríguez, G. Katz, C. Sánchez, R. Fox** | **20** |
| [8] | H. Aarab | 7 |
| [9] | T. Miller | 8 |
| [10] | Y.-T. Kim et al. | 9 |
| [11] | N. Flehmig et al. | 10 |
| [12] | Open-Meteo | 11 |
| [13] | P. Zippenfenig | 12 |
| [14] | H. Hersbach et al. | 13 |
| [15] | Malaysian Meteorological Department — strong wind | 14 |
| [16] | Malaysian Meteorological Department — thunderstorm | 15 |
| [17] | Y. Jeong and N. Im | 16 |
| [18] | O. Yaakob et al. | 17 |
| [19] | International Maritime Organization | 18 |
| [20] | Department of Irrigation and Drainage Malaysia | 19 |

The permutation `[1,2,3,4,5,6,20,7,8,9,10,11,12,13,14,15,16,17,18,19]` matches the requested mapping exactly.

---

## 4. Validation

| Check | Result |
|---|---|
| References [1]–[20] appear in order of first citation | **PASS for the requested mapping, with one pre-existing exception.** First-appearance order in the body is now 1, 2, 3, 4, 5, 6, **7 (Corsi)**, 8, 9, 10, 11, **17**, 12, 13, 14, 15, 16, 18, 19, 20. Corsi is correctly placed. The exception is [17] (Jeong and Im), first cited in §IV ahead of [12]–[16]; in the input it was [16] cited ahead of [11]–[15], so this is inherited, not introduced, and the author-specified mapping preserves it. Strict first-appearance order would require Jeong and Im to become [12] and [12]–[16] to shift up by one — **not applied**, since it is outside the supplied table. See §6. |
| Every in-text citation points to the correct entry | **PASS** — all 31 resolved against the new bibliography and checked in context (e.g. "Corsi et al. [7]", "6.54 m hull tested in [18]" → Yaakob, "COLREGs, Rule 20(b) [19]" → IMO) |
| No number duplicated, skipped or misassigned | **PASS** — rendered list is [1]…[20], each exactly once; no [21] or higher |
| Bibliography contains the same 20 sources | **PASS** — the 20 entry texts are byte-identical as a set before and after; author names, titles, years, DOIs and URLs unchanged |
| No citation still points to Corsi as [20] | **PASS** — the only `[20]` in the body is the DID rainfall citation; `[20]` in the bibliography is the DID entry |
| Formatting unaltered | **PASS** — `styles.xml`, `numbering.xml`, `settings.xml`, `fontTable.xml`, `footer1.xml`, `footnotes.xml`, `endnotes.xml`, `theme1.xml` and `media/image1.png` are byte-identical to the input; all 9 section properties, both tables and the single drawing are byte-identical; 141 paragraphs before and after; `document.xml` validates as well-formed |
| No content change beyond numbering | **PASS** — with every bracketed number masked, all 119 body paragraphs are character-identical to the input. No claim, result, method, limitation or conclusion was touched |

Rendering: LibreOffice 24.2.7.2. A4, 595.304 × 841.89 pt, two-column geometry unchanged.

---

## 5. Page count — action needed

**The output is 7 pages. So is the input.**

| Page | Input chars | Output chars |
|---|---|---|
| 1 | 6,640 | 6,640 |
| 2 | 10,181 | 10,180 |
| 3 | 6,071 | 6,071 |
| 4 | 10,056 | 10,056 |
| 5 | 9,276 | 9,276 |
| 6 | 9,478 | 9,536 |
| 7 | 1,102 | 1,073 |

Page 7 carries four reference entries ([17]–[20]) and is otherwise empty. This spill is present in the uploaded "Rewrite v4" file and was **not** introduced by the renumbering, which is length-neutral to within two characters.

AAI 2026 requires 4–6 A4 pages including references, and states that a paper exceeding six pages will be rejected. The manuscript as it stands would be rejected on length.

Resolving this requires removing roughly 1,100 characters of body text, which is outside the scope of this citation-maintenance task and was therefore not done. For reference, v10 fitted six pages at 6,924 words; the uploaded Rewrite v4 adds the Corsi paragraph in §II and further body text beyond that. The shortest route back is to trim §II, where the new material was added, rather than the results or limitations.

---

## 6. Unresolved, carried forward

- **Page limit** — 7 pages; see §5. Blocking for submission.
- **One remaining out-of-sequence citation** — [17] (Jeong and Im) is first cited in §IV before [12]–[16]. This is inherited from the input, where the same entry was [16] cited before [11]–[15], and the supplied mapping preserves it. Correcting it strictly would mean Jeong and Im → [12] with [12]–[16] shifting up by one. Not applied, because it is outside the mapping table provided; say the word and it is a one-line change to the same script.
- **Microsoft Word page count** — unverified; LibreOffice only. A Word render could differ by a line.
- **IEEE PDF eXpress** — not run (Conference ID 71745X).
- **Official IEEE A4 template comparison** — the template is still not held in the repository; compliance is verified for page geometry only, not fonts or heading styles.
