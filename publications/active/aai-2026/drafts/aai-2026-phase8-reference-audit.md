# AAI 2026 — Phase 8 Reference & Assembly Audit

**Date:** 2026-09-24
**Manuscript assembled:** `aai-2026-manuscript-v1-full-assembled.md`
**Body source:** `aai-2026-manuscript-v1-prefinal.md` · **Abstract source:** `aai-2026-manuscript-v1-abstract.md`

---

## 1. Executive Status

| Check | Result |
|---|---|
| Bibliographic verification | **PARTIAL** — 16 of 18 fully verified this phase; 2 carried from the prior lock because their official pages could not be fetched |
| Claim-to-source verification | **PARTIAL** — 17 VERIFIED, 1 carried (MET thunderstorm criterion) |
| IEEE numbering | **PASS** |
| Full assembly | **PASS** |
| Manuscript prose integrity | **PASS** — one authorised citation insertion, no prose change |
| Reference readiness | **READY** |

---

## 2. Citation Inventory

**TOTAL UNIQUE IN-TEXT CITATION KEYS = 18** (17 present in the pre-final body, plus one authorised insertion).

| Order | Symbolic key | First occurrence | IEEE no. | Reference type |
|---|---|---|---|---|
| 1 | NIST | §I, risk-management guidance sentence | **[1]** | Official guidance |
| 2 | ASTM | §I, run-time assurance concession | **[2]** | Standard |
| 3 | ALSHIEKH | §I, shielding concession | **[3]** | Conference paper |
| 4 | FAA | §I, advisory-inhibition concession | **[4]** | Government / regulatory document |
| 5 | PARASURAMAN | §I, graduated contraction of alternatives | **[5]** | Journal article |
| 6 | AI-GOV-SLR | §II, implementation-and-validation gap | **[6]** | Journal article |
| 7 | AARAB | §II, Cluster D | **[7]** | Conference paper |
| 8 | MILLER | §II, Cluster D | **[8]** | Journal article |
| 9 | KIM | §II, Cluster D | **[9]** | Journal article |
| 10 | FLEHMIG | §III, C3 topology provenance | **[10]** | Conference paper |
| 11 | **MFWAM** *(inserted)* | §IV, RESOLUTION wave source | **[11]** | Dataset / data product |
| 12 | OPEN-METEO | §IV, retrieval sentence | **[12]** | Dataset / data product |
| 13 | ERA5 | §IV, retrieval sentence | **[13]** | Dataset / data product |
| 14 | MET-WIND | §IV, wind boundary provenance | **[14]** | Official web documentation |
| 15 | MET-THUNDERSTORM | §IV, rainfall UNSAFE boundary | **[15]** | Official web documentation |
| 16 | YAAKOB | §IV, ocean-state boundary | **[16]** | Journal article |
| 17 | IMO-COLREG | §IV, day boundary | **[17]** | Government / regulatory document |
| 18 | DID-RAINFALL | §IV, rainfall CAUTION boundary | **[18]** | Official web documentation |

Numbering follows first appearance in the assembled manuscript, not the old symbolic names and not alphabetical order. The MFWAM insertion sits ahead of the retrieval sentence, which is why `[OPEN-METEO]` and `[ERA5]` became [12] and [13] rather than [11] and [12].

---

## 3. Verified Bibliography Ledger

| No. | Verified source | Metadata status | DOI / identifier | Authority | Status |
|---|---|---|---|---|---|
| [1] | NIST AI RMF 1.0, NIST AI 100-1, 2023 | VERIFIED | 10.6028/NIST.AI.100-1 | PRIMARY / OFFICIAL | ✅ |
| [2] | ASTM F3269-21 | VERIFIED (title + scope) | 10.1520/F3269-21 | PRIMARY / OFFICIAL | ✅ **no clause claim** |
| [3] | Alshiekh et al., AAAI-18, pp. 2669–2678 | VERIFIED; **no DOI established** — cited by proceedings | — | PRIMARY | ✅ |
| [4] | FAA AC 20-151C, 2017 | VERIFIED | AC 20-151C | PRIMARY / OFFICIAL | ✅ |
| [5] | Parasuraman, Sheridan & Wickens, 2000, 30(3):286–297 | VERIFIED | 10.1109/3468.844354 | PRIMARY | ✅ |
| [6] | Batool, Zowghi & Bano, *AI and Ethics* **5(3):3265–3279, 2025** | VERIFIED this phase — Crossref + publisher | 10.1007/s43681-024-00653-w | PRIMARY + REGISTRY | ✅ **year corrected** |
| [7] | Aarab (single author), ICHCAI 2026, pp. 1–10 | VERIFIED — Crossref registry | 10.1109/ICHCAI70183.2026.11607581 | REGISTRY (Xplore access-restricted) | ✅ |
| [8] | Miller (single author), *MAKE* 8(5):125, 2026 | VERIFIED — publisher record | 10.3390/make8050125 | PRIMARY | ✅ |
| [9] | Kim et al. (7 authors), *npj Digit. Med.* 9:281, 2026 | VERIFIED — publisher record | 10.1038/s41746-026-02450-7 | PRIMARY | ✅ |
| [10] | Flehmig, Lundteigen & Yin, IECON 2024 | VERIFIED; **pages not established** | 10.1109/IECON55916.2024.10906021 | PRIMARY | ✅ |
| [11] | Copernicus Marine, *Global Ocean Waves Analysis and Forecast* (MFWAM), GLOBAL_ANALYSISFORECAST_WAV_001_027 | VERIFIED this phase — official catalogue | 10.48670/moi-00017 | PRIMARY / OFFICIAL | ✅ |
| [12] | Zippenfenig, *Open-Meteo.com Weather API*, Zenodo | Concept DOI VERIFIED; **year carried** — see §10 | 10.5281/zenodo.7970649 | PRIMARY | ⚠️ |
| [13] | Hersbach et al., *ERA5 hourly data on single levels from 1940 to present*, C3S CDS | VERIFIED this phase — DOI resolves to `reanalysis-era5-single-levels` | 10.24381/cds.adbb2d47 | PRIMARY / OFFICIAL | ✅ |
| [14] | MET Malaysia, *Kriteria Amaran Angin Kencang dan Laut Bergelora* | VERIFIED this phase — page fetched, criteria quoted | official URL | PRIMARY / OFFICIAL | ✅ |
| [15] | MET Malaysia, *Kriteria Amaran Ribut Petir* | Page identity VERIFIED on issuing domain; **content not re-fetched** (redirect loop) | official URL | PRIMARY / OFFICIAL | ⚠️ |
| [16] | Yaakob et al., *J. Sustain. Sci. Manage.* 10(1):50–65, 2015 | VERIFIED — corpus note + EA reference list | — | PRIMARY | ✅ |
| [17] | IMO, COLREGs 1972, Rule 20(b) | Carried from prior lock; **official page not fetchable** (robots.txt) | official URL | PRIMARY / OFFICIAL | ⚠️ |
| [18] | DID Malaysia, *Rainfall Data — categorization of rainfall intensity*, Public Infobanjir | VERIFIED this phase — page fetched, table quoted | official URL | PRIMARY / OFFICIAL | ✅ |

**No invented metadata.** Three fields are explicitly left unestablished rather than guessed: the Alshiekh DOI, the Flehmig page range, and the MET thunderstorm numeric criterion as re-read this phase.

---

## 4. Claim-to-Source Support Ledger

| No. | Section | Claim supported | Support status | Notes |
|---|---|---|---|---|
| [1] | I, II | AI risks analysed, assessed, benchmarked, monitored; systems tested before deployment and regularly in operation | **VERIFIED** | Used conservatively. The manuscript never says NIST *requires* a control-effectiveness criterion |
| [2] | I, II | Run-time assurance bounds the behaviour of a component containing complex functions | **VERIFIED (title-and-scope)** | No clause number appears anywhere in the manuscript |
| [3] | I, II | A shield computes safe actions and removes unsafe ones **before** the agent selects, as distinct from post-selection correction | **VERIFIED** | *"pre-inference"* absent, as required |
| [4] | I, II | Progressive inhibition of advisory categories as external state worsens; crew retains authority | **VERIFIED** | |
| [5] | I, II, III | Levels are function-relative; graduated contraction complete set → narrowed → single suggestion | **VERIFIED** | Cited four times, each for one of these two points |
| [6] | II | (a) frameworks lack real-world implementation detail **and validation**; (b) few studies answer who/what/when/how together | **VERIFIED** | Both limbs quoted verbatim in Phase 7 §5. Only 3 of 28 reviewed studies answer all four |
| [7] | II | Graduated runtime autonomy modes in which permitted directives contract as severity rises | **VERIFIED** | Manuscript states the directive-frequency simulation was run under the permissive mode — it does **not** imply Aarab measures the binding-frequency question |
| [8] | II | Ablation across enforcement operators including an ungoverned baseline | **VERIFIED** | Manuscript states these compare operators rather than graduated risk levels |
| [9] | II | Burden of an intermediate zone requiring mandatory human review, characterised across reliability targets | **VERIFIED** | Manuscript states the zone withdraws automated action rather than retaining an active contracted set |
| [10] | III | C3's governance topology is ported from this source, which conditions on AI degradation rather than environmental state | **VERIFIED** | The non-deficiency qualification is attached in the same paragraph |
| [11] | IV | Identity and provenance of the MFWAM wave model | **VERIFIED (provenance only)** | 🔴 Does **not** support the ~8 km figure — see §5 |
| [12] | IV | Retrieval archive; and the ~8 km / October 2021 particulars | **VERIFIED** | Open-Meteo documents its MFWAM at 0.08° (~8 km), archive from October 2021 |
| [13] | IV | ERA5 reanalysis provenance for the PRIMARY wave source | **VERIFIED** | DOI resolves to the ERA5 single-levels dataset |
| [14] | IV | Wind boundary follows MET strong-wind criteria | **VERIFIED** | Category One is *"40–50 kmsj"* = **21.6–27.0 kn**, exactly the canonical W_C / W_U |
| [15] | IV | Rainfall UNSAFE boundary follows MET thunderstorm criteria | **PARTIAL (carried)** | Page would not render this phase; support carried from Citation Lock v1 |
| [16] | IV, V | Small-vessel operational ceiling; and the second failure-point reading giving 9.22% | **VERIFIED** | Manuscript states provenance *"does not establish that it is optimal"* |
| [17] | IV | Day boundary follows COLREGs Rule 20(b) | **METADATA ONLY (carried)** | Official page not fetchable; the non-daylight→UNSAFE policy is separately declared researcher-defined |
| [18] | IV | Rainfall CAUTION boundary is source-supported but non-MET | **VERIFIED** | DID *Light* = 1–10 mm in one hour; upper limit **10 mm/hr** = canonical R_C. Confirms the source is DID, not MET |

---

## 5. Corrections Carried Forward

| Item | Confirmed in the assembled manuscript |
|---|---|
| **AI-GOV-SLR year** | **2025** — reference [6] reads *vol. 5, no. 3, pp. 3265–3279, 2025*. The Citation Lock's 2024 was not propagated |
| **MFWAM** | **Resolved** — reference [11], DOI 10.48670/moi-00017 |
| **IPoSCI** | **Not cited.** The string does not appear in the assembled manuscript or the reference list |
| **ASTM** | **No invented clause** — [2] is title-and-scope only |
| **RESOLUTION pairwise** | **Withheld** — 41.08 and 45.56 absent; Table III cells remain em dashes |
| **Wave sensitivity** | **−1.2**, not −1.4. The string "−1.4" does not appear |
| **Figure 1** | **Absent** — no `FIGURE` token anywhere in the manuscript |

**🔴 On the MFWAM resolution figure.** The Copernicus product states **0.083°**; Open-Meteo documents the product it serves at **0.08° (~8 km)**. The manuscript says *approximately 8 km*. The citation was therefore placed at the **model-identity** mention — *"wave data from MFWAM [11] at approximately 8 km resolution"* — so [11] supports which model was used, while the resolution figure rests on [12] in the same paragraph. Reference [11] is not made to support Open-Meteo's exact wording.

---

## 6. Citation Changes

**A. Symbolic → numeric conversions: 18.** Every occurrence of all 18 symbolic keys was replaced by its assigned number. Zero unresolved symbolic keys remain (regex sweep for `[A-Z]`-style keys returns nothing).

**B. Citation insertions: 1.**
Section IV — `[MFWAM]` inserted at the model-identity mention:
*"…comprising 28,501 hourly records with wave data from MFWAM **[11]** at approximately 8 km resolution…"*
Classified as a **REFERENCE-SUPPORT INSERTION**. No word of the sentence was changed, added or removed.

**C. Citation removals: 0.**

**Prose changes: NONE.** A normalised comparison — all citation tokens replaced by a single placeholder in both files — found the assembled body byte-identical to the pre-final body except for the one inserted marker.

---

## 7. Reference Integrity

| Check | Result |
|---|---|
| Total in-text unique references | **18** |
| Total bibliography entries | **18** |
| Orphan bibliography entries | **0** |
| Missing bibliography entries | **0** |
| Duplicate DOI | **0** |
| Duplicate source under different keys | **0** |
| Unresolved symbolic keys | **0** |
| Unverified metadata | **3 fields**, each explicitly marked: Alshiekh DOI (not established), Flehmig pages (not established), MET thunderstorm content (not re-fetched) |

In-text numbers form a complete, gapless 1–18 set, and every entry is cited at least once.

**Citation density (Part N).** No factual external claim was found without a citation. No citation is attached to a claim its source does not support. `[5]` appears four times and `[1]`–`[4]`, `[8]`, `[10]`, `[16]` twice each; every repeat sits in a different section supporting a different point, so none is redundant within a paragraph. No reference exists solely to enlarge the list — all 18 support a specific concession, threshold provenance or data source. No citation-level fix is recommended.

---

## 8. Manuscript Integrity

| Item | Status |
|---|---|
| Title unchanged | ✅ |
| Abstract unchanged | ✅ **217 words**, one paragraph, no citation, no symbolic key |
| Index Terms unchanged | ✅ seven terms, verbatim |
| Sections I–VI prose unchanged | ✅ identical under citation normalisation |
| Tables I–III unchanged | ✅ including both withheld em dashes |
| No Figure 1 | ✅ |
| −1.2 retained | ✅ |
| Headline results unchanged | ✅ 5.81% / 4.48% / 42.88% / 48.69% / envelopes / 97.6% / vessel and denominator variants |
| Contribution unchanged | ✅ both I-P6 and VI-P3 |
| RQ unchanged | ✅ |
| Limitations unchanged | ✅ |

**Literature-gap safety check (Part O): PASS.** Both scoped statements survive verbatim — *"Within the reviewed literature, no empirical characterisation was identified…"* and *"Within the reviewed literature, these works do not combine…"*. No novelty escalation was introduced. The single occurrence of *unexplored* is a **negation** — *"Measuring how often such a boundary is encountered is not an unexplored activity"* — and *novel*, *first*, *unique*, *unprecedented*, *never studied* and *no previous study* have zero occurrences.

---

## 9. Reference Count and Layout Implication

**Final reference count: 18.** Inside the 17–20 planning expectation, reached without filler and without deleting evidence. The count equals the Citation Lock's REQUIRED list of 17 plus the one MFWAM entry that Phase 7 resolved. The three SHOULD-KEEP / OPTIONAL and all DROPPED candidates were left out because the manuscript does not cite them.

**Layout pressure: LOW.** Eighteen IEEE entries at 8 pt, several short, sit comfortably inside the 1.1-column reserve, and Phase 7A's removal of Figure 1 freed roughly half a column that has not been refilled. The two longest entries are [4] and [18], whose URLs may each wrap to a third line; even so the list should not exceed the reserve. No page layout was performed and none is asserted.

---

## 10. Remaining Pre-Layout Issues

1. **Author metadata not supplied.** `[AUTHOR NAME]`, `[AFFILIATION]`, `[EMAIL]` are placeholders. AAI 2026 is **non-blind**, so these must be real before submission. Not a Phase 8 blocker.

2. **[15] MET thunderstorm criterion not re-verified.** `met.gov.my/ramalan/ribut-petir/` returned a redirect loop on two attempts. The page exists on the issuing authority's domain and the claim is carried from Citation Lock v1's EA-reference-list verification. The companion wind page fetched cleanly and confirmed its criteria exactly, so the domain is live. Re-check before camera-ready.

3. **[17] COLREGs page not fetchable.** The IMO page refused automated access (robots.txt). The reference uses the convention's own designation rather than any metadata I could not confirm. Re-check before camera-ready.

4. **[12] Open-Meteo year.** The concept DOI 10.5281/zenodo.7970649 is stable and correct, but its landing page currently surfaces version 1.4.0 dated 2024. The reference retains **2023**, carried from the Citation Lock and the earlier reference list. Confirm against Open-Meteo's own recommended citation before camera-ready rather than changing it on the strength of a version page.

5. **IPoSCI publication-status recheck** remains required immediately before submission.

6. **[3] Alshiekh DOI and [10] Flehmig pages** remain unestablished. Both are cited adequately without them.

---

## 11. Phase Decision

### Final validation

**A.** Every `[n]` maps to exactly one reference; 1–18 gapless. **Yes.**
**B.** Every reference is cited at least once; zero orphans. **Yes.**
**C.** Every citation supports the claim beside it, with two carried and marked. **Yes, with §4 notes.**
**D.** Aarab — graduated runtime contraction, simulation under the permissive mode, not the same measurement. Miller — operator ablation, not graduated-level binding frequency. Kim et al. — mandatory human-review zone that withdraws automated action, not active contracted scope. **All three accurate.**
**E.** Batool et al. dated **2025**. **Yes.**
**F.** MFWAM resolved via Copernicus for identity only; the ~8 km wording rests on Open-Meteo. **Yes.**
**G.** ASTM limited to title and scope. **Yes.**
**H.** IPoSCI absent from References and from the manuscript. **Yes.**
**I.** RESOLUTION pairwise values still withheld. **Yes.**
**J.** −1.2 retained. **Yes.**
**K.** −1.4 absent. **Yes.**
**L.** Figure 1 absent. **Yes.**
**M.** Abstract is the locked Phase 6 version, 217 words. **Yes.**
**N.** Index Terms unchanged. **Yes.**
**O.** Did any prose change? **No.** The only manuscript change is the authorised `[MFWAM]` citation insertion.

---

PHASE 8 STATUS: READY FOR IEEE 6-PAGE LAYOUT & SUBMISSION AUDIT
