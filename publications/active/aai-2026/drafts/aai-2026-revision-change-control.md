# AAI 2026 — Surgical Revision Plan and Change-Control Table

**Manuscript:** `[Rewrite V2] conference-template-letter.docx`, SHA-256 `a29a0c27bf5b631c36ecbbaa92ecd7e7cc6cf2acabf95ef4d79c628804f41f97`
**Basis:** `aai-2026-independent-review-v8.md` rev 4, and the verified canonical outputs in `data/c8/reproducibility-verification/`
**Date:** 9 October 2026
**Scope:** editorial and claim-scoping only. No experiment, no implementation change, no data change, no study redesign.

---

## 0. Venue constraints — verified, not assumed

Confirmed from `aai-2026-phase9-layout-submission-audit.md:13–21`, sourced to aai.unimap.edu.my and recorded as ✅ VERIFIED:

| | |
|---|---|
| Paper size | **A4** — "Paper must be 4 to 6 pages of A4 size in length including all texts, references, figures and photographs." |
| Page limit | **4–6 pages, references included** — "Any submitted paper that exceeds six (6) pages will be rejected." |
| Template | IEEE Manuscript Template for Conference Proceedings |
| PDF | IEEE PDF eXpress, Conference ID **71745X** |
| Submission | EDAS, https://edas.info/N34957 |
| **Code / data availability** | **No requirement of any kind appears in the recorded venue requirements.** |

**Two facts that govern this plan.**

1. **A compliant layout already existed.** `aai-2026-v4-final-verification-report.md:14–18` records v4 rendering at **595.304 × 841.89 pt (A4)** with a **PASS** on the hard 6-page limit. The current v8 renders at **612 × 792 pt (US Letter), 7 pages**. The regression is a template regression, and A4 compliance is a revert to a known-good layout rather than an untested conversion.
2. **The v4 layout sat *at* the limit, not under it.** `phase9:178`: "The paper sits **at** the limit rather than under it, so the margin is thin. Anything later added … could push it to 7 and trigger rejection." So every word added below must be paid for.

**Consequence for M-2.** My review graded the missing availability statement **Major** on reviewer-expectation grounds. The venue requires nothing of the kind, references count toward a hard limit, and the paper is over-length. **E-20 is therefore reclassified from Major to Optional and recommended for deferral.** This corrects my own grading; the earlier project audit reached the same conclusion and I had not checked it before grading.

---

## 1. Change-control table

Word counts are estimates for the inserted or deleted prose, excluding table cells. **Net: +493 words before compression** — see §3, which is not optional.

### A. Title and Abstract

| ID | Section ¶ | Existing wording | Proposed replacement | Scientific reason | Evidence | Words | Class |
|---|---|---|---|---|---|---|---|
| **E-1** | Title | "…**Measuring the Operational Effect of AI Governance** Through Deterministic Historical Replay" | "…**Measuring How Often an Intermediate Governance Level Binds** in Deterministic Historical Replay" | Δ<sub>L2</sub> carries one bit of sensitivity to the contract: 0 if `A_AI(CAUTION) = FULL`, else P(CAUTION) whatever the contract says. "Operational effect of AI governance" claims what the metric cannot measure. The body already says "governance activation" and "binding frequency" throughout. | §III invariance passage; verified ∅ case | **0** | **Critical** |
| **E-2** | Abstract ¶10 | "The intermediate restriction bound in 5.81% of evaluated departure-window hours under the PRIMARY configuration and 4.48% under RESOLUTION." | "**Under a stipulated three-state classifier**, the intermediate restriction bound in 5.81% of evaluated departure-window hours under the PRIMARY configuration and 4.48% under RESOLUTION." | 97.6% of the measured quantity is produced by the stipulated ocean-state band; the figure is not a property of the site. | stdout:19 — `g_o` binds 518 of 531 | **+5** | **Major** |
| **E-3** | Abstract ¶10 | "…falling to 1.26% under a large-vessel configuration." | "…falling to 1.26% under a large-vessel configuration, **and differing by 1.97 percentage points between two wave data products evaluated on identical hours**." | Strongest unreported empirical result; data-product selection is a distinct sensitivity dimension currently absent from the abstract. | stdout:117–118 — 6.45% vs 4.48%, common n = 28,501, departure n = 5,935 | **+15** | **Major** |

### B. Introduction and Research Question

| ID | Section ¶ | Existing wording | Proposed replacement | Scientific reason | Evidence | Words | Class |
|---|---|---|---|---|---|---|---|
| **E-4** | §I ¶17 | "RQ1. Over a multi-year environmental record for one deployment site, how often does an intermediate advisory-scope governance level **change the admissible recommendation set relative to a participation-only gate**, and how sensitive is that frequency to defensible **threshold, vessel-class and denominator-policy** configurations?" | "RQ1. Over a multi-year environmental record for one deployment site, how often **is an intermediate advisory-scope governance level reached under a stipulated three-state classifier**, and — **the comparator difference being fixed by the admissible-set mappings** — how sensitive is that frequency to defensible **threshold, wave-data-product, vessel-class and evaluation-set** configurations? | Separates the entailed comparator identity from the genuinely empirical dependencies. Adds the verified product dimension. "Evaluation-set" is the convention the 56-count sentence already uses, and is accurate where "denominator-policy" is not: the daylight variant is a denominator identity with an invariant numerator. | Δ<sub>L2</sub> ≡ P(CAUTION); daylight numerator invariant at 531 and 266 | **+12** | **Major** |

### C. Contributions

| ID | Section ¶ | Existing wording | Proposed replacement | Scientific reason | Evidence | Words | Class |
|---|---|---|---|---|---|---|---|
| **E-5** | §I ¶18 | "…**the isolation of an intermediate advisory-scope level against a participation-only configuration differing from it at one state**;" | **Delete.** The construction is already stated in §III. | A design choice, not a result. The isolation is achieved by *defining* C1 and C2 to differ at one state; nothing is discovered. Listing it as a contribution claims credit for a definition. | §III ¶47–48 already describes the construction | **−17** | **Critical** |
| **E-6** | §I ¶18 | "…the sensitivity of that binding rate to **the threshold that governs it**; and the attribution of which state component produces the intermediate classification in the evaluated record." | "…the sensitivity of that binding rate to **the threshold, data product and evaluation set that govern it**; the attribution of which state component produces the intermediate classification in the evaluated record; **and two limits of the measure itself — it is invariant to the content of the restricted recommendation set, including the empty set, and it does not distinguish a three-state declaration that leaves scope unchanged from a two-state participation gate**." | Promotes the two strongest empirical items and states the blind spots as scope rather than as concessions. The ∅ clause also corrects the narrower proviso in §III. | Verified: `A_AI(CAUTION) = ∅` still yields Δ<sub>L2</sub> = P(CAUTION); C1 ≡ C3 | **+35** | **Major** |

### D. Methodology

| ID | Section ¶ | Existing wording | Proposed replacement | Scientific reason | Evidence | Words | Class |
|---|---|---|---|---|---|---|---|
| **E-7** | §III ¶62 | "the value of ΔL2 is invariant to the content of AAI(CAUTION), **provided that set remains a non-empty strict subset of FULL**" | "the value of ΔL2 is invariant to the content of AAI(CAUTION) **for any proper subset of FULL, including the empty set; non-emptiness is a property of the declared contract rather than something the metric detects**" | The proviso is narrower than the arithmetic requires. With `A_AI(CAUTION) = ∅`, C2 still differs from C0 on CAUTION ∪ UNSAFE and Δ<sub>L2</sub> = P(CAUTION) again. As written, the sentence disguises that the metric cannot distinguish contracted advisory from total withdrawal. | Verified algebraically and against the mappings | **+8** | **Major** |
| **E-8** | §III ¶46, ¶49, ¶53; §V-A ¶81; Table II | Four locations on C3: the ¶46 clause "C3 declares three states without contracting scope at the intermediate one."; ¶49 in full; ¶53 in full; ¶81 in full; the Table II `C1↔C3` row and its caption clause. | **One passage in §III, replacing all four:** "A three-state configuration that does not contract scope at the intermediate state — such as a traffic-light topology in which the intermediate level raises supervisory intensity rather than restricting what the AI may recommend [10] — assigns the same admissible sets at every state as a two-state participation gate. Under the criterion the two are the same governance function, and the criterion therefore cannot distinguish them: a governance difference expressed as supervisory intensity rather than admissible scope lies outside what this metric observes. Declared state cardinality is not by itself evidence of a governance effect." Keep [10] cited. Delete the Table II row. | `C1` and `C3` are character-identical dict literals six lines apart returning the same `frozenset` objects; the 0.00% is guaranteed by object identity, there is no assertion in the script, and the test is strictly weaker than a one-line map comparison and conditional on state coverage. The pipeline's sensitivity is already evidenced by the non-zero comparisons beside it. What is worth keeping is the criterion's blind spot, not a conformance claim. | `condition_comparison.py:90–105`, `:198`; `grep assert` returns nothing | **−120** | **Major** |
| **E-9** | §IV ¶69 | After "…reported in [17]." | **Insert a component table** (5 rows × 3 cols): wind `> 21.6 kn` / `> 27.0 kn`; rainfall `> 10.0 mm h⁻¹` / `> 20.0 mm h⁻¹ or WMO code 95, 96, 99`; ocean state, small vessel `≥ 1.0 m` / `> 1.25 m`; daylight — / outside `sunrise ≤ t < sunset`; marine warning — / excluded, held at SAFE. | Ten rules are required to reproduce the labels; the manuscript supplies four. The undocumented inclusive ocean-state onset alone moves the headline: an implementation faithful to every word of the paper returns **5.22%**, not 5.81% — a 10.2% relative discrepancy. | Counterfactual: 477/9,135 = 5.221675% vs 531/9,135 = 5.812808%; 237/5,935 = 3.993260% vs 266/5,935 = 4.481887% | **+120** (table) | **Critical** |
| **E-10** | §IV ¶69 | — | **Insert after the table:** "The ocean-state CAUTION onset is inclusive, following the phrasing of the cited restriction ("1 m or above" [16]); the wind and rainfall CAUTION onsets and the rainfall UNSAFE trigger are strict, and the ocean-state UNSAFE boundary is strict so that the upper limit of the highest passing sea-state category falls within CAUTION. The classified state is the maximum over the five components under SAFE < CAUTION < UNSAFE, and a missing clock, date or solar lookup resolves to UNSAFE. Solar events are taken from a frozen daily table for 5.98° N, 116.01° E (UTC+8), with exact sunrise SAFE and exact sunset UNSAFE. These conventions are stated so the classification can be reproduced exactly; they are not claims that the boundaries are correct, optimal or validated for the baseline vessel class." | Each operator tracks its source's own phrasing, so the conventions are principled — but unstated. The final clause withholds any validation claim while making the labels reconstructible. | [16] primary text retrieved: "a significant wave height of **1 m or above**"; `solar-spec-v1` in `build_solar_artefacts.py`; 1,827/1,827 solar rows regenerated exactly | **+70** | **Critical** |
| **E-11** | §IV ¶66 | After "…Weather records were retrieved through the Open-Meteo archive [12], [13]." | **Insert:** "Records were retrieved for 5.940° N, 116.025° E (weather), 6.00° N, 116.00° E (ERA5-Ocean waves) and 5.958° N, 116.042° E (MFWAM waves), with `cell_selection=sea`, `timezone=Asia/Kuching`, and models `era5_ocean` and `meteofrance_wave`." | Without the coordinates, the sea-cell flag and the model identifiers a reader cannot reach the same input rows. `cell_selection=sea` is not cosmetic: the project records F-10, a land-cell defect in the v1 collection that this flag exists to fix. **Two** wave cells, 4.5 km apart, at 7.2 km and 2.7 km from the shared weather cell. | `collect_raw_v2.py:51–53, 113–150`; CSV headers; `data-provenance.md:70–71` | **+40** | **Major** |
| **E-12** | §IV ¶67 | "The evaluation window is **05:00–09:00 local time (UTC+8)**, which defines Neval." | "The evaluation window is the **five hourly timestamps from 05:00 to 09:00 inclusive (UTC+8)**, which defines Neval." | 9,135 / 1,827 days = exactly 5 timestamps per day. Read as a four-hour interval, the stated window gives 7,308 hours and reproduces nothing. Closed-interval indexing is legitimate; the convention is simply unstated. | 1,827 × 5 = 9,135; 1,188 × 5 − 5 = 5,935 | **+8** | **Minor** |
| **E-13** | §IV ¶65, ¶69 | ¶69: "the ocean-state CAUTION onset follows the **departure restriction** proposed for vessels under 10 m by [16], while the UNSAFE boundary is derived from the upper limit of the highest passing sea-state category reported in [17]." | "the ocean-state CAUTION onset is set at 1.0 m, following the departure **restrictions or cautions** proposed for vessels ≤ 10 m in length in [16] — the source does not distinguish the two, and the evaluated contract adopts the non-prohibitive reading — while the UNSAFE boundary is 1.25 m, the upper limit of the highest sea-state category passed by the 6.54 m hull tested in [17]. **[16] proposes no upper boundary for that state. Neither source is keyed to the tonnage-defined baseline, so the CAUTION band is a stipulated evaluation parameter composed from two source-supported edges rather than a validated operational transition, and its application to a tonnage class is a researcher-defined transfer of a length-parameterised guideline.**" | The manuscript twice describes [16] using only the stronger limb, then maps it to a state where Go remains admissible. The source's own word that licenses the mapping — "cautions" — is the one omitted. [16] supplies no upper edge; the band is a splice. | [16] primary text: "should be subject to **departure restrictions or cautions**", with "prohibited" reserved for 3 m, 5.5 m and wind-wave warnings | **+55** | **Major** |

### E. Results

| ID | Section ¶ | Existing wording | Proposed replacement | Scientific reason | Evidence | Words | Class |
|---|---|---|---|---|---|---|---|
| **E-14** | §V-A ¶79 | After "…the difference is not attributed to spatial resolution alone." | **Insert:** "Evaluated on the 5,935 hours common to both records, with identical thresholds and denominator, the two products give 6.45% and 4.48% — 1.97 percentage points apart. The full-record gap of 1.33 points understates this, because the longer record independently lowers the rate by 0.64 points. The products differ in resolution, model type, observation assimilation and cell siting." | The strongest empirical result absent from the manuscript. Controls verified from source: identical timestamps, thresholds, denominator and atmospheric inputs, with the wave column the sole variable. The opposite signs of the two terms are the empirical content; their sum is an arithmetic identity. | stdout:117–118; `data-provenance.md:62–77` | **+60** | **Major** |
| **E-15** | §V-B ¶113 | "In a separate researcher-defined rainfall-boundary sensitivity sweep, varying the rainfall CAUTION threshold changes ΔL2 by 0.48 percentage points in PRIMARY and 0.78 percentage points in RESOLUTION. This variation had a smaller effect than the alternative wave UNSAFE boundary interpretation in the evaluated configurations." | "Varying the wave UNSAFE boundary across its two source-grounded readings moves ΔL2 by 3.41 percentage points, while varying the rainfall CAUTION boundary across the widest researcher-defined range evaluated here moves it by 0.48 points in PRIMARY and 0.78 in RESOLUTION — a ratio of about seven to one, with the wave boundary varied only over sourced values and rainfall over unsourced ones." | The comparison is deliberately stacked against the conclusion and the conclusion holds. The existing sentence asserts the ordering without the magnitudes, and the unqualified "smaller effect" invites the question of how much. | 9.22 − 5.81 = 3.41; 6.15 − 5.67 = 0.48; ratio 7.1× | **−5** | **Major** |
| **E-16** | §V-B ¶113 | "Varying the wind CAUTION boundary across the evaluated range WC = 18–25 kn produced no change in ΔL2 in either environmental-data configuration." | "**At the sourced wind settings the component binds in no evaluated hour, the maximum departure-window wind being 21.80 kn in PRIMARY and 19.30 kn in RESOLUTION against an UNSAFE boundary of 27.0 kn;** varying the wind CAUTION boundary across the evaluated range WC = 18–25 kn produced no change in ΔL2 in either configuration." | Wind inertness is establishable from **source-grounded values alone**, with no perturbation — more robust than any elasticity claim, and currently stated only in its weaker perturbation form. | stdout:17 (`g_w` enters 1, binds 0), :73 (0/0), :9, :65 (max 21.80, 19.30) | **+25** | **Major** |
| **E-17** | §V-C ¶115 | After "…the rainfall component for the remaining 13, or 2.4%." | **Insert:** "Because the ocean-state component produces 97.6% of these hours, the reported frequency rests substantially on the stipulated wave band and on the length-to-tonnage transfer declared in Section IV. Across the band's evaluated CAUTION-onset range the figure spans approximately 0.1% to 13%." | Each fact is disclosed separately; their conjunction is not. A reviewer who connects §IV's transfer assumption to §V-C's attribution will raise it — better raised by the authors. | stdout:19; `O_C` gradient 12.94% → 0.14% (labelled researcher-defined) | **+40** | **Critical** |
| **E-18** | §V-C ¶117 | "Restricting the evaluated departure-window hours to daylight gives denominators of 5,536 hours in PRIMARY and 3,594 hours in RESOLUTION, **increasing the measured binding frequency to 9.59% and 7.40%**, respectively." | "Restricting the evaluated departure-window hours to daylight gives denominators of 5,536 and 3,594 hours. **Because a CAUTION classification requires that the time component not be UNSAFE, every CAUTION hour already lies inside the daylight subset, so the numerator is unchanged at 531 and 266 and the rate rises to 9.59% and 7.40% by denominator reduction alone.**" | Presented as a sensitivity, this reads as an empirical finding. It is a ratio identity: 531/5,536 and 266/3,594 are the exact quotients. The only empirical content is that 60.6% of the window is daylight. | 531/5,536 = 9.59176%; 266/3,594 = 7.40122% | **+18** | **Major** |
| **E-19** | §V-A ¶79 | "…**86.5%** of PRIMARY UNSAFE hours and **93.2%** of RESOLUTION UNSAFE hours were classified UNSAFE solely because they occurred before sunrise, without another UNSAFE trigger." | Append: "; **99% of the ocean-state CAUTION conditions that did not reach the final state were likewise pre-sunrise**." | Absorbs the masking rate into an existing finding instead of promoting it. **The masking rate must not be reported as a separate contribution:** 357 of 359 and 183 of 183 non-binding hours are darkness alone, so it is the night result restated. | 359 non-binding, `g_t` only 357 (99.44%); RESOLUTION 183/183 (100%) | **+20** | **Minor** (optional) |

### F. Discussion, Limitations, Reproducibility, Conclusion

| ID | Section ¶ | Existing wording | Proposed replacement | Scientific reason | Evidence | Words | Class |
|---|---|---|---|---|---|---|---|
| **E-20** | §VI ¶121 | "Several governance choices remain researcher-defined rather than empirically validated: the three-state cardinality, the evaluation policies fixed in Section IV, and the admissible set AAI(CAUTION) = {Go, Delay}." | "…the evaluation policies fixed in Section IV, the admissible set AAI(CAUTION) = {Go, Delay}, **and the intermediate ocean-state band, which is composed from two sources keyed to vessel length rather than tonnage and is not validated for the baseline class.**" | The band determines 97.6% of the measured quantity and is the paper's most attackable element. Declared, it is rigour; discovered, it reads as concealment. | §IV ¶65 transfer assumption; stdout:19 | **+30** | **Critical** |
| **E-21** | §V-D ¶118 | "**RQ1 can now be answered.** … The intermediate level therefore measurably changes the admissible recommendation set under the evaluated contract, with the frequency of that change depending on threshold, vessel-class and denominator choices." | "**RQ1 can be answered conditionally.** … The intermediate level therefore measurably changes the admissible recommendation set under the evaluated contract, with the frequency of that change depending on threshold, wave-data-product, vessel-class and evaluation-set choices, **under the stipulated classifier whose intermediate band is not validated for the baseline vessel class.**" | An unconditional answer is the single largest drift toward a maritime-safety claim the construct cannot carry. | As E-17, E-20 | **+15** | **Major** |
| **E-22** | §IV ¶73 | "Because the replay is deterministic, no configuration needs replication." | "Because the replay is deterministic, no configuration needs replication: **the reported figures are exactly repeatable from the archived input records, which are not guaranteed to be re-retrievable, the environmental series being served by a third-party API over reanalysis products subject to revision.**" | §IV's claim is correct but silently carries the whole conditional. The phrase "an identical record" never tells the reader the record is *archived* rather than *re-obtainable*. Three provider-side dependencies stand between the documented query and the archived rows: cell resolution under `cell_selection=sea`, reanalysis reprocessing, and eleven provider-side nulls that fix the 28,501 figure. | `data-provenance.md:62–88`; 11 empty CSV fields verified from raw text | **+25** | **Major** |
| **E-23** | — | — | **Code/data availability statement.** | **DEFER.** The venue requires none, references count toward a hard 6-page limit, and the paper is over-length. Repository accessibility is also unestablished, so no honest sentence can be written yet. Add only if the A4 re-render leaves headroom. | `phase9:13–21` — no availability requirement recorded | +60 if added | **Optional** *(downgraded from Major; see §0)* |
| **E-24** | §VI ¶123/124 | "These are conditional measurements rather than stable site properties; the contribution is the assembly that makes such a figure interpretable, together with the criterion." | "These are conditional measurements rather than stable site properties. **What the replay establishes is an activation frequency for one declared contract at one site under one classifier; what follows by construction is that the isolated increment equals the intermediate state's occupancy, so the figure is a property of the classifier rather than of the contract; and what remains unvalidated is the intermediate wave band itself, the admissible set at CAUTION, and any link between activation and operational outcome.** The contribution is the assembly that makes such a figure interpretable, together with the criterion." | Gives the three-way separation explicitly, in one sentence, in the author's own register. Pre-empts the "contribution is a tautology" objection by stating the boundary rather than leaving a reviewer to find it. | Δ<sub>L2</sub> ≡ P(CAUTION); §III invariance; absence of outcome data | **+45** | **Major** |

**Net before compression: +493 words.** Deletions already included (E-5 −17, E-8 −120, E-15 −5).

---

## 2. Classification summary

| Class | IDs | Count |
|---|---|---|
| **Critical** | E-1, E-5, E-9, E-10, E-17, E-20 | 6 |
| **Major** | E-2, E-3, E-4, E-6, E-7, E-8, E-11, E-13, E-14, E-15, E-16, E-18, E-21, E-22, E-24 | 15 |
| **Minor** | E-12, E-19 | 2 |
| **Optional** | E-23 | 1 |

Editorial items carried from the review and not tabled here because they cost no words: PDF metadata (`Title: Paper Title (use style: paper title)`, `Author: IEEE`); reference [14]'s URL, which mixes English "and" into a Malay slug; and the run-together author block.

**References: no change.** No citation was shown to be incorrect. [16]'s *characterisation* is corrected in E-13, not the citation itself. [11]'s replacement of the Copernicus product citation is already an improvement and stays.

---

## 3. Mandatory compression — not optional

+493 words cannot be absorbed by a paper that renders at 7 Letter pages and whose predecessor sat *at* the 6-page A4 limit.

**Step 1 — re-render on A4 first.** The available budget is unknown until v8 is on the A4 IEEE template. v4 fitted 6 A4 pages, so the target is known to be achievable; what is not known is how much v8 added relative to v4.

**Step 2 — cuts, ranked by scientific cost (lowest first).**

| | Cut | Est. words |
|---|---|---|
| 1 | **Deduplicate §I ¶14 against §II ¶21–22.** Run-time assurance [2], shielding [3], TCAS [4] and Parasuraman [5] are introduced in §I and re-introduced in §II in near-identical terms. Keep §II; reduce §I to one sentence carrying the four citations. **Zero scientific cost — pure repetition.** | **−200** |
| 2 | **Consolidate the non-claims.** The list of what the study does not establish appears at length in §I ¶18, §III ¶62, §V-D ¶119 and §VI ¶121–122. State once in §VI; replace the others with a clause. **No caveat is lost.** | **−150** |
| 3 | **C3 demotion** (E-8, already counted above) | −120 |
| 4 | **Tighten §III ¶62–63**, folding E-7 and the ladder-collapse note in rather than adding to them. | **−85** |
| 5 | **Trim Table II** — "Period" and "Small-vessel baseline" duplicate §IV; the `C1↔C3` row goes with E-8. | **−25** + a table row |
| 6 | **Compress §II's three-paragraph treatment of [2]–[5] to one** once §I's duplicate is gone. | **−100** |
| | **Available** | **−560** (excluding E-8, already in the net) |

**Arithmetic.** +493 − 560 = **−67 words net**, i.e. the plan is just inside budget *for word count*, before the page-count regression is addressed. The regression itself must come from the A4 re-render, not from prose.

**If the A4 re-render still exceeds six pages**, cut in this order: E-23 (already deferred); then E-9's table moved to a footnote at 8 pt, which the template permits, retaining about 60% of the space; then E-19; then the exploratory `O_C` gradient figure in E-17, keeping only the attribution–transfer clause.

**Do not cut:** §VI ¶122 (limitations), §IV ¶71 (the marine-warning exclusion argument), §V-C ¶116 (the three component zeros), or Figure 1's legibility. Those are the paper's defensive core, and E-8 raises the stakes on the figure: the C₀–C₃ mappings must appear as text before Figure 1 is rescaled, or the paper becomes formally incomplete.

---

## 4. Unresolved factual issues

### Genuinely blocking

**B-1 — The A4 page budget for v8 is not established.** v4 rendered at 6 A4 pages and passed; v8 renders at 7 US Letter pages. Until v8 is re-rendered on the A4 IEEE template, the compression target in §3 cannot be set and the fallback order cannot be triggered in the right place. **This blocks sizing the revision, not deciding its content** — every edit above can be drafted now, and only the final cut depth waits on the render.

### Not blocking — proceed, and improve if resolved

| | Issue | Effect if resolved |
|---|---|---|
| **N-1** | Table 12's cell label for vessels ≤10 m at Hs 1 m. Not retrievable from the publisher's HTML or PDF; the body text's own narration is the disjunction quoted in E-13. | If labelled "caution", one word shortens E-13 by about 15 words and closes the item outright. Obtain the open-access PDF and hold it in `papers/sources/` — [16] carries the dominant threshold and the project does not have it. |
| **N-2** | MMD's exact phrasing, inclusive or strict, for the wind and rainfall criteria. Supported only by the project's code provenance comments; reference [14]'s URL appears broken. | Would let E-10's rule sentence drop its hedging, saving about 20 words. |
| **N-3** | Repository public accessibility. | Governs whether E-23 can ever be written honestly. Already deferred. |

### Already resolved — do not reopen

No source-to-policy contradiction exists in [16] (the source says "restrictions or cautions" and reserves "prohibited" for 3 m, 5.5 m and wind-wave warnings). The solar specification exists, is pinned, is USNO-validated and regenerates exactly (1,827/1,827). The classifier's equality operators are source-faithful, not arbitrary. The 56-combination count is correct under the convention the manuscript now names. The 518/13 attribution is exclusive by unique component trigger, with ties = 0. All 28 numerical claims reproduce. **None of these needs further investigation.**

---

## 5. What this plan does not do

No experiment is proposed. No implementation script, input dataset or archived output is modified. No new reference is introduced and none removed. No result is changed: 5.81%, 4.48%, 42.88%, 41.08%, 48.69%, 45.56%, 0.00%, 9.22%, 6.08%, 1.26%, 0.37%, 9.59%, 7.40%, 531, 518, 13, 97.6%, 2.4%, 9,135, 5,935, 43,848, 28,501, 5,536, 3,594, 78, 56, 0.48 and 0.78 all stand exactly as reported, and 6.45% is added from the same preserved capture.

Twenty-four edits. Six Critical, fifteen Major, two Minor, one deferred. Net word impact after the mandatory compression: approximately zero.
