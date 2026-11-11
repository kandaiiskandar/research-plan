# Independent Review — AAI 2026 Submission

### Revision 3, after author rebuttal, six rounds of targeted re-examination and a full data-pipeline audit

**Manuscript:** *From Declared Risk Levels to Admissible Recommendations: Measuring the Operational Effect of AI Governance Through Deterministic Historical Replay*
**File reviewed:** `[Rewrite V2] conference-template-letter.docx`, SHA-256 `a29a0c27bf5b631c36ecbbaa92ecd7e7cc6cf2acabf95ef4d79c628804f41f97`, 420,280 bytes
**Reviewer role:** independent senior academic reviewer — CS, AI governance, safety-critical decision support, empirical software engineering
**Revision 1:** 9 October 2026 · **Revision 2:** 9 October 2026 · **Revision 3:** 9 October 2026

---

## Revision log

Revision 1 was written from the manuscript alone. Revision 2 follows author rebuttal on seven points, inspection of the executable classifier, retrieval of reference [16] from the publisher, and one isolated read-only counterfactual. **Six findings moved, two recommendations were withdrawn, one was withdrawn and then reinstated in altered form, and two diagnoses were corrected.** The movement is recorded here because the author is entitled to see which arguments carried.

| Item | Rev 1 | Rev 2 | Why it moved |
|---|---|---|---|
| **C-2** | Critical | **Major** | Rev 1 said the paper's concessions "hand a reviewer the rejection argument". The author correctly objected that this penalises disclosure rather than the gap. Restated as *under-specified*, not over-claimed. |
| C-2 recommendation #1 | "state the identity as a result" | **WITHDRAWN** | The author's own challenge was decisive: the identity is elementary and the manuscript itself calls it "not a result". Presenting it as a finding would invite the objection it was meant to deflect. |
| **M-1** | Major (formatting-adjacent) | **Major (specification)** | Diagnosis corrected after reading the classifier. Not a readability matter: ten rules are required and the manuscript supplies four. Quantified below. |
| **M-3** | Major | **Minor** | Author correct. Closed-interval timestamp indexing is a legitimate convention; the defect is an *ambiguity*, not an arithmetic inconsistency. My characterisation was wrong. |
| **M-4** | Major (disclosure gap) | **Major (construct validity)** | Diagnosis corrected and escalated in kind, not severity. A limitation sentence cannot repair a construct that determines 97.6% of the measured quantity. |
| M-4 sub-claim: source/policy contradiction | raised as live possibility | **WITHDRAWN** | Retrieved [16]'s primary text. No contradiction exists. Raising it before attempting retrieval was a sequencing error on my part. |
| **M-5** | Major | **Minor** | Author correct. The disclosure is present, accurate and new; only its magnitude is missing. I over-graded it. |
| **M-6** | Major | **folded into C-2** | The title mismatch is part of the contribution-statement repair, not a separate defect. |
| **M-7, M-8** | Major | **Minor** | Author correct that severity should not inflate because a consequence is large when the fix is one line and nothing in the body is wrong. |
| **m-5 (C₃)** | Minor: "compress" | **WITHDRAWN, then reinstated as Minor: "demote"** | Withdrawn on the author's formal-verification analogy. Reinstated after reading the code: equivalence checking is informative only between *independently constructed* artefacts, and I failed to check independence before conceding. New evidence changed the recommendation's content. |
| New: m-8, m-9 | — | **Minor** | Surfaced by code inspection and source retrieval. |

### Revision 3 — after auditing the complete data pipeline

Revision 3 follows an audit of the chain from API query to the reported 531 and 266 CAUTION hours: the retrieval script, the solar generator and its pinned specification, git tracking of every link, and an in-memory regeneration of the solar artefact. **One implication in revision 2 was wrong and is corrected; one finding was re-scoped and its cost revised upward; one finding was added; and a section of verified strengths was added because the pipeline is in materially better shape than the manuscript conveys.**

| Item | Rev 2 | Rev 3 | Why it moved |
|---|---|---|---|
| **M-1(v)** | "`g_t` entirely unspecified" | **corrected** | True of the manuscript, **false of the project.** The solar specification exists, is pinned, is script-generated and is externally validated against USNO. I regenerated all **1,827 of 1,827 rows exactly**. Rev 2 implied the specification might not exist; it does, and it is the best-documented element in the chain. |
| **M-2** | "No availability statement" (~150 ch) | **re-scoped, ~330–520 ch** | The honest statement must carry a provider caveat. Without it the sentence implies recollection from live services, which the project cannot support. Now also covers the repeatability/recollection distinction. |
| **m-10** | — | **new Minor** | Second instance of the stale-comment class: `solar.py`'s docstring still says it is "NOT part of the canonical model" while it is now the canonical generator. |
| **New section** | — | **Verified reproducibility posture** | Three inputs, no intermediate state, every link tracked, solar artefact regenerated exactly, canonical figures reproduced twice. A review that records only defects would misrepresent the evidence. |

**Net after revision 3:** Critical 2 → **1**. Major 8 → **4**. Minor 7 → **14**. Editorial 4 → **4**. Withdrawn: **3**. Corrected implications: **1**.

---

## Verification basis

| | |
|---|---|
| Numerical claims checked against preserved machine output | **28, all reproduce exactly** |
| Classifier source inspected | `scripts/condition_comparison.py` (constants, `load`, `classify`, `divergence_matrix`, `run_config`), `scripts/canonical_gt.py`, `scripts/collect_raw_v2.py`, `scripts/sensitivity/solar.py`, `scripts/solar/build_solar_artefacts.py` |
| Raw input precision verified from CSV text | PRIMARY 43,848 wave values at 2 dp; RESOLUTION 28,501 at 2 dp plus 11 provider-side empty fields |
| Primary source retrieved | [16] Jeong & Im 2023 via publisher (MDPI) — body text and table captions obtained; **table cell contents not retrievable** |
| Isolated read-only counterfactual | one, on the ocean-state equality convention; baseline reproduced all canonical figures exactly before the counterfactual was trusted |
| Solar artefact regenerated in memory | **1,827 of 1,827 rows exact** on `sunrise_hours` and `sunset_hours` at 6 dp |
| Git tracking verified for every chain link | 10 of 10 **TRACKED** |
| Canonical figures reproduced independently | **twice** — sensitivity run and counterfactual baseline |
| Repository integrity | branch `AMIT-v5`, HEAD `a7f77d8`, 0 modified tracked files throughout |
| Experiments recommended | **zero** |

**No numerical error has been found anywhere in the manuscript across either revision.** Every defect below is specification, framing or provenance.

---

# CRITICAL

## C-1 — Letter page size and seven pages against an A4, six-page hard limit

**Severity:** Critical (automatic rejection) · **Section:** whole document · **Conceded by both sides**

Rendering the submitted `.docx` gives `Page size: 612 x 792 pts (letter)` and `Pages: 7`. The template filename is itself `conference-template-letter.docx`. The venue requires A4 and rejects any paper exceeding six pages.

**Correction.** Rebuild on the A4 IEEE conference template, then re-measure. A4 (595 × 842 pt) is narrower and taller than Letter; with comparable margins it holds roughly 6% more text per page, which materially changes the compression arithmetic in §8 below. **Convert first, measure second.**

**Experiments:** none.

---

# MAJOR

## C-2 — The contribution statement is under-specified

**Severity:** Major (downgraded from Critical) · **Sections:** title, §I, §III

**Quoted passages.**

> "This is an operational measurement rule rather than a result. It restates, for a declared state, the position already established in the levels-of-automation literature…" (§III)
> "ΔL2 ≡ P(S = CAUTION) … This is a metric-interpretation identity, not a result." (§III)
> "Because the identity holds, the CAUTION base rate yields the same number and the comparator ladder is not required to compute it." (§III)
> "the value of ΔL2 is invariant to the content of AAI(CAUTION), provided that set remains a non-empty strict subset of FULL" (§III)

**Justification.** The paper concedes everything and claims nothing, which is strictly worse than its actual position. Its own §I statement — "a measurement assembly and its interpretation rather than any of its constituent techniques" — is closer to defensible than the stronger claim I proposed in revision 1.

Three facts bound the achievable claim, and they should be stated rather than fought:

- **Theoretical novelty is nil.** The identity is the definition of a disagreement region plus finite additivity on a three-element state space. The criterion restates [5].
- **The metric carries one bit of contract sensitivity.** If `A_AI(CAUTION) = FULL`, Δ<sub>L2</sub> = 0; otherwise Δ<sub>L2</sub> = P(CAUTION), whatever the contract says. Everything else is the classifier.
- **Invariance is broader than the manuscript states.** It holds for *any* proper subset, including ∅: if `A_AI(CAUTION) = ∅`, C₂ still differs from C₀ on CAUTION ∪ UNSAFE and Δ<sub>L2</sub> = P(CAUTION) again. So the metric cannot distinguish a contracted active advisory from total AI withdrawal at CAUTION. Non-emptiness is imposed by the contract, not detected by the measurement.

**Correction — subtractive, not additive.**

1. **Retitle** to the activation framing, e.g. *"Measuring How Often a Declared Risk Level Binds: …"*. The body already uses "governance activation" and "binding frequency" throughout; the title has not caught up. Free in page terms.
2. **Promote the operationalisation-dependence result** from §V-B caveat to the paper's claim. The strongest defensible statement, using only existing evidence:

> Under a stipulated three-state classifier whose intermediate ocean-state band is defined here, the declared intermediate governance level is reached in 5.81% of departure-window hours at this site over 2020–2024. That figure is produced almost entirely by the stipulated band (97.6% of activations) and spans roughly 0.1% to 13% across the band's evaluated range, while remaining invariant to the content of the restricted recommendation set. An activation rate reported without its threshold construction is therefore uninterpretable, and a declared level's binding frequency is a property of its operationalisation rather than of the deployment site.

3. **State the ladder-collapse condition as a scope limit of the method**, in the manuscript's existing "not a result" register — two sentences, not a theorem.
4. **Correct the invariance proviso** to cover the empty set.

**Do not delete any existing concession.** They are the paper's best feature.

**Experiments:** none.

**Ceiling, stated honestly.** After the best available reframing the contribution is a reporting protocol demonstrated once, plus a negative stability result, from one site and one contract shape. That is vulnerable to *not validated against an alternative*, *n = 1 site* and *n = 1 contract*, and no rewording touches those. What the revision buys is that rejection becomes a disagreement about significance rather than a finding of defect. A second contract shape — one where configurations differ at more than one state, or the sets are not nested, so the ladder does not collapse — would lift it, and **that is a different paper. Do not attempt it for AAI 2026.**

---

## M-1 — The classifier specification is incomplete; the labels cannot be reproduced from the paper

**Severity:** Major · **Section:** §IV · **Diagnosis corrected in revision 2**

Revision 1 treated this as a readability matter and costed the fix at ~400 characters. That was wrong. Reading the classifier shows that **ten rules are required to reproduce the labels and the manuscript supplies four.**

### The complete rule set, verified from source

**Data preparation**
1. Retrieve from Open-Meteo: weather at **5.940246 N, 116.025 E**; ERA5 waves at **6.0 N, 116.0 E**; both with **`cell_selection=sea`**, **`timezone=Asia/Kuching`** (UTC+8), models **`era5_ocean`** and **`meteofrance_wave`**; CSV with 3 metadata lines before the header.
2. Variables: `wind_speed_10m` (**knots**), `precipitation` (mm), `weather_code` (WMO), `wave_height` (m).
3. **Inner** merge on `time`; drop rows missing `wave`, `wind` *or* `precip` (not `weather_code`); `hour = time.dt.hour` on already-local timestamps.

**Components** (`condition_comparison.py:160–166`)
4. `g_w`: wind > 27.0 → UNSAFE; elif > 21.6 → CAUTION; else SAFE *(strict)*
5. `g_r`: `(precip > 20.0) OR (weather_code ∈ {95, 96, 99})` → UNSAFE; elif precip > 10.0 → CAUTION; else SAFE *(strict)*
6. `g_o`: wave > 1.25 → UNSAFE; elif wave **≥** 1.0 → CAUTION; else SAFE *(inclusive onset)*
7. `g_t`: SAFE **iff** `sunrise_hours ≤ hour < sunset_hours` from a frozen daily table computed for **5.98 N, 116.01 E, UTC+8**, read as float hours at 6 dp — never the HH:MM:SS columns. Missing date, missing lookup or non-finite hour → **UNSAFE** (fail-safe).
8. `g_m` ≡ SAFE for every row.

**Aggregation**
9. `S = max(g_w, g_r, g_m, g_o, g_t)`, SAFE = 0 < CAUTION = 1 < UNSAFE = 2.
10. Window: `hour ≥ 5 AND hour ≤ 9` — five hourly timestamps.

**The manuscript supplies 8, 9, 10 (ambiguously — see M-3) and the existence of 4–7 without values, operators or the solar specification.** Items 1, 2, 3, the operators, the categorical trigger in 5, and all of 7 are absent.

### Quantified impact of the one undocumented operator

The ocean-state CAUTION onset is **inclusive** while wind and rainfall are strict. Wave data is stored at two decimal places — verified from CSV text, not from parsed floats — so boundary hours are frequent, and `1.00` parses to the exactly representable float 1.0, making the comparison exact with no floating-point hazard.

An isolated read-only counterfactual, with the baseline first confirmed to reproduce every canonical figure:

| | PRIMARY (n = 9,135) | RESOLUTION (n = 5,935) |
|---|---|---|
| Hours with wave exactly 1.00 m in window | 97 | 50 |
| …baseline label SAFE / CAUTION / UNSAFE | 0 / **54** / 43 | 0 / **29** / 21 |
| Labels changed under `> 1.0 m` | **54** (CAUTION → SAFE only) | **29** (CAUTION → SAFE only) |
| Full-record labels changed | 169 of 43,848 | 120 of 28,501 |
| Δ<sub>L2</sub> baseline | 531 / 9,135 = **5.812808%** | 266 / 5,935 = **4.481887%** |
| Δ<sub>L2</sub> counterfactual | 477 / 9,135 = **5.221675%** | 237 / 5,935 = **3.993260%** |
| **Change** | **−0.5911 pts (−10.17%)** | **−0.4886 pts (−10.90%)** |
| P(UNSAFE) | 42.88% → 42.88% (**exactly 0**) | 41.08% → 41.08% (**0**) |
| C0↔C1 | 42.88% → 42.88% (**0**) | 41.08% → 41.08% (**0**) |
| C0↔C2 | 48.69% → 48.10% | 45.56% → 45.07% |
| `g_o` binding share | 518 (97.6%) → 464 (97.3%) | 253 (95.1%) → 224 (94.5%) |
| `g_r` binding / ties | 13 / 0 → 13 / 0 | 13 / 0 → 13 / 0 |

So an independent reimplementation faithful to every word of the manuscript returns **5.22%, not 5.81%** — a 10.2% relative discrepancy on the headline, from an operator the paper never mentions.

### The operators are principled, which revision 1 denied

Revision 1 implied the asymmetry was arbitrary. It is not. [16]'s primary text, retrieved verbatim, reads *"a significant wave height of **1 m or above**"* — inclusive. The code's provenance comment records the MMD *Ribut Petir* trigger as "> 20 mm/hr" — strict. And 1.25 m is "the upper limit of the highest **passing** category", so a vessel at exactly 1.25 m still passes, making CAUTION the coherent label. **Each operator tracks its source's own phrasing.** The defect is that none of it is stated.

### Four further gaps, classified

| | Finding | Class | Material to reported results? |
|---|---|---|---|
| (i) | Equality conventions undocumented | **Ambiguous specification** | **Yes — 10.2% / 10.9% relative** |
| (ii) | The rainfall UNSAFE rule is a *disjunction* with a categorical WMO-code term (95, 96, 99), not the single "boundary" §IV describes | **Manuscript–implementation inconsistency** | **No** — zero occurrences of 95/96/99 in either window. A reimplementation on other data diverges |
| (iii) | Asymmetric missing-data policy: `g_t` fails safe to UNSAFE; a missing `weather_code` fails *open* and is excluded from the `dropna` subset | **Ambiguous specification** | **No** — zero NaN weather codes. Latent |
| (iv) | Retrieval parameters absent: coordinates, `cell_selection=sea`, `era5_ocean`, timezone. `cell_selection=sea` is not cosmetic — the code records F-10, a land-cell defect in the v1 collection that this flag exists to fix | **Missing documentation** | **Yes, for re-collection** |
| (v) | `g_t` unspecified **in the manuscript** beyond the COLREGs citation — no solar coordinates (which differ from both data cells), no frozen-table provenance, no half-open convention, no precision policy | **Missing documentation (manuscript only)** | **Yes** — this component determines ~60% of the window's UNSAFE labels |

**Correction to revision 2 on item (v).** Rev 2 implied the solar specification might not exist. **It does, and it is exemplary.** `scripts/solar/build_solar_artefacts.py` pins `solar-spec-v1`: the implementation and its SHA-256; `LAT = 5.98`, `LON = 116.01` ("authoritative, resolved under C-1") with the superseded `116.07` default explicitly recorded as matching nothing in the project; UTC+8 fixed, no DST; zeniths 90.833° and 96.0°; the calendar day-of-year convention with its fixed-365 leap-day consequence stated as "bounded and documented, not silently absorbed"; the half-open boundary rule; and a precision policy — compute float64, store 6 dp of an hour, **compare on the stored float, never the display string**. Every row of the artefact self-documents latitude, longitude, timezone, offset, zenith, implementation version and hash, and spec version. Two companion artefacts are tracked beside it: a 28-row **USNO validation** file and a boundary audit. **I regenerated all 1,827 rows from the preserved code at the documented coordinates: 0 mismatches.** The required manuscript addition is therefore a *summary* of an existing specification, not the creation of one — which makes it cheaper and more defensible, not less necessary.

Two things the manuscript gets **right**, checked specifically: the merge is lossless (43,848 weather rows match 43,848 ERA5 rows; all 28,512 MFWAM timestamps are present in weather), so the eleven excluded observations are exactly the `dropna` and the account is accurate; and the timezone *is* set at retrieval (`utc_offset_seconds 28800`, `Asia/Kuching`), so "05:00–09:00 local time (UTC+8)" is correct with no UTC/local defect.

### Correction — approximately 920 characters

**(a) Component table (~450 ch), operators inline.**

> wind `> 21.6 kn` / `> 27.0 kn` · rainfall `> 10.0 mm h⁻¹` / `> 20.0 mm h⁻¹ or WMO code 95, 96, 99` · ocean state, small vessel `≥ 1.0 m` / `> 1.25 m` · daylight — / outside `sunrise ≤ t < sunset` · marine warning — / excluded, held at SAFE

**(b) Rule sentence (~430 ch) — highest priority if space binds.**

> "The ocean-state CAUTION onset is inclusive, following the phrasing of the cited restriction ("1 m or above" [16]); the wind and rainfall CAUTION onsets and the rainfall UNSAFE trigger are strict, and the ocean-state UNSAFE boundary is strict so that the upper limit of the highest passing sea-state category falls within CAUTION. The classified state is the maximum over the five components under SAFE < CAUTION < UNSAFE, and a missing clock, date or solar lookup resolves to UNSAFE. Solar events are taken from a frozen daily table for 5.98° N, 116.01° E (UTC+8), with exact sunrise SAFE and exact sunset UNSAFE. These conventions are stated so the classification can be reproduced exactly; they are not claims that the boundaries are correct, optimal or validated for the baseline vessel class."

**(c) Retrieval sentence (~250 ch).**

> "Records were retrieved from Open-Meteo for 5.940° N, 116.025° E (weather) and 6.00° N, 116.00° E (waves), with `cell_selection=sea`, `timezone=Asia/Kuching`, and models `era5_ocean` and `meteofrance_wave`."

**Why Major and not Critical.** Nothing is wrong, every operator is defensible, no reported number is incorrect for the configuration used, and no conclusion changes: Δ<sub>L2</sub> stays non-vacuous, the attribution share stays above 94%, the identity holds, P(UNSAFE) and C0↔C1 are invariant to the decimal, and ties stay zero. **Why still Major.** The paper's own methodological claim is that "replaying an identical record under an identical configuration reproduces an identical result"; a reader cannot construct the identical configuration, so the claim is unverifiable against the artefact offered.

**Experiments:** none.

---

## M-2 — No availability statement, and the reproducibility claim does not distinguish repeatability from recollection

**Severity:** Major · **Section:** absent, and §IV · **Re-scoped in revision 3**

### The three senses, and which one the paper supports

> "Because the replay is deterministic, no configuration needs replication… replaying an identical record under an identical configuration reproduces an identical result." (§IV)

| Sense | Claimed? | True? |
|---|---|---|
| **Repeatability from frozen inputs** | Yes, in §IV | **Yes — verified twice in this session** |
| **Reproducibility from archived artefacts** | No | Not currently possible for a reader: no availability statement, and repository accessibility is unestablished |
| **Recollection from live external services** | No | **Would be false if claimed** — the retrieval is not pinned against provider change |

So the paper is **not overclaiming**: its one claim is the narrow true one. The defect is that a reader cannot tell which sense is meant. The phrase "an identical record" silently carries the entire conditional, and the reader is never told that the record is *archived* rather than *re-obtainable*.

Three provider-side dependencies stand between the documented query and the archived rows: the provider resolves the request coordinate (5.98 / 116.01) to a grid cell under `cell_selection=sea`, and the returned cells are 5.940246 / 116.025 and 6.0 / 116.0; ERA5 and MFWAM are reanalysis products subject to reprocessing; and the eleven missing MFWAM wave values are **provider-side empty fields** that fix the 28,501 figure. None is pinned by the query.

### Correction

**~330 characters, short form:**

> "The replay scripts, the three retrieved hourly datasets and the generated solar table are version-controlled and available from the authors on request. The reported figures are exactly repeatable from those archived inputs; re-retrieval from the provider is not guaranteed to reproduce them, as the underlying reanalysis products are subject to revision."

**~520 characters, full form**, if space allows — adds that the classified record is derived deterministically from three retrieved datasets and one generated solar table, and points at §IV for the retrieval parameters and classification rules.

**This revises revision 2's ~150-character estimate upward.** That figure assumed a one-line claim. The provider caveat is not padding: without it the sentence implies recollection, which is the one sense the project cannot support.

**Do not fabricate a repository URL, DOI or access guarantee.** Repository accessibility has not been established, and the honesty of the sentence depends on settling that first.

**Experiments:** none.

---

## M-4 — The dominant threshold is a construct-validity limitation, not a disclosure gap

**Severity:** Major · **Sections:** §I, §IV, §V-B, §V-C, §V-D, §VI, abstract · **Diagnosis corrected; one sub-claim withdrawn**

### What was withdrawn

Revision 1 raised the possibility that [16] recommends *prohibiting* departure at Hs ≥ 1.0 m while the contract admits {Go, Delay}. **No such contradiction exists.** [16]'s primary text, retrieved verbatim:

> "when the weather conditions reach a significant wave height of 1 m or above, fishing vessels with a length less than 10 m should be subject to **departure restrictions or cautions**."

The source is disjunctive and does not define the two terms. Decisively, it reserves "prohibited" for much higher sea states — ">3 m" for <15 GT, ">5.5 m" for all vessels, and wind-wave warnings — and never applies it here. `{Go, Delay}` is consistent with the "cautions" limb. **Withdrawn**, and I should have attempted retrieval before leaving it as a live possibility.

### What stands, and is confirmed from primary text

The CAUTION band [1.0, 1.25] m is **a researcher-defined interval with source-supported edges**, and the interval — not the edges — is what the metric counts.

- **Neither source defines an interval.** [16] supplies a monotone length ladder (≥1 m for <10 m; ≥2 m for <24 m) with **no upper boundary**; a <10 m vessel at 1.25 m remains in the same category a fortiori. The upper edge is **wholly** [17]'s, a seakeeping ceiling for one 6.54 m hull, not a departure policy.
- **The edges are different kinds of quantity** — an administrative onset spliced to a hydrodynamic operability limit. Their *difference* has no single physical or regulatory meaning, and that difference is what Δ<sub>L2</sub> counts.
- **The source's own hydrodynamics place the critical height inside the band.** The Wolfson-derived formula gives 1.13 m at 10 m LOA — mid-band.
- **The class transfer is not a function.** [16]'s guideline is parameterised by LOA by construction; GRT is a volume measure. A <10 GRT boat may be roughly 6–12 m LOA, over which [16]'s own formula returns materially different critical heights. Notably [16] *does* use gross tonnage elsewhere (15 GT, 30 GT) for existing Korean regulation, so the distinction is live in the source's own domain.
- **The dominant parameter is not swept in any reported range.** §V-B varies only `O_U` (1.25 → 1.90 m). `O_C` is held at the transferred value throughout, despite ranking **first** in the project's own elasticity table at ≈ −1.4 points per 0.05 m against `O_U`'s ≈ +0.2. The internal `O_C` gradient spans **12.94% at 0.80 m to 0.14% at 1.25 m** in PRIMARY; the reported envelope is ~3.4 points wide where the dominant parameter spans nearly 13.
- **97.6% of the measured quantity comes from this band**, and the manuscript never connects §IV's transfer assumption to §V-C's attribution.

### Sensitivity analysis is not validation

| | Status |
|---|---|
| **Parameter sensitivity** | Partially addressed; the dominant parameter is excluded |
| **Construct validity** | **Not addressed, and cannot be** by parameter sweeping |
| **Uncertainty quantification** | Not attempted — correctly disclaimed |
| **External validity** | Not attempted — correctly disclaimed |

### Correction — six locations, ~750 characters

A limitation sentence is inadequate and revision 1's prescription is withdrawn. A construct determining 97.6% of the measured quantity belongs in the question, the method, the results and the conclusion.

**(a) §I, RQ1** — insert four words: "…relative to a participation-only gate **under a stipulated three-state classifier**, and how sensitive…"

**(b) §IV, provenance** — replace the wave clause:
> "For the small-vessel class the ocean-state CAUTION onset is set at 1.0 m, following the departure **restrictions or cautions** proposed for vessels ≤ 10 m LOA in [16]; the source does not distinguish the two, and the evaluated contract adopts the non-prohibitive reading. The UNSAFE boundary is 1.25 m, the upper limit of the highest sea-state category passed by the 6.54 m hull tested in [17]. [16] proposes no upper boundary for that state. Neither source is keyed to the tonnage-defined baseline; the CAUTION band is therefore a stipulated evaluation parameter composed from two source-supported edges rather than a validated operational transition, and its application to a tonnage class is a researcher-defined transfer of a length-parameterised guideline."

**(c) §V-C, after the 97.6% sentence** — the change that does the real work:
> "The measured frequency is therefore substantially the frequency with which historical wave heights fall inside the stipulated band. Across the band's evaluated CAUTION-onset range the figure spans approximately 0.1% to 13%, so the reported value should be read as conditional on that construction rather than as a characterisation of conditions at the site."

**(d) §V-D** — "RQ1 can now be answered" → "RQ1 can be answered conditionally", and append "…under the stipulated classifier, whose intermediate band is not validated for the baseline vessel class."

**(e) §VI** — one clause into the existing limitations sentence naming the band alongside the other researcher-defined choices.

**(f) Abstract** — one clause: "…under the PRIMARY configuration **and a stipulated intermediate wave band**…"

**Experiments:** none. Report the existing `O_C` gradient labelled researcher-defined, exactly as rainfall already is, or state that the dominant parameter was held fixed in the reported envelope. Either closes it.

**Non-experimental action:** obtain the [16] PDF (MDPI, open access) and hold it in `papers/sources/`. It carries the paper's dominant threshold and the project does not have it.

**Conditional upgrade.** If the authors decline the reframing and submit with the current title and unconditional RQ1 answer, this becomes **Critical**, because the paper would then assert a maritime-safety-adjacent result its construct cannot carry.

---

# MINOR

## M-3 — The stated evaluation window is ambiguous

**Severity:** Minor (downgraded from Major) · **Section:** §IV

> "The evaluation window is 05:00–09:00 local time (UTC+8), which defines Neval."

PRIMARY spans 1,827 days; 9,135 / 1,827 = exactly 5, so the implementation uses five hourly timestamps (05–09 inclusive). RESOLUTION confirms it: 1,188 days × 5 = 5,940, less 5 of the eleven excluded observations = 5,935.

Closed-interval timestamp indexing is a legitimate convention and the arithmetic is consistent under it, so **my "arithmetic inconsistency" characterisation was wrong**. The residual defect is that the convention is unstated and the word "window" pushes a reader toward the duration reading, which gives 7,308 hours — a 25% denominator ambiguity in a paper about exact reproducibility.

**Correction.** "the five hourly timestamps from 05:00 to 09:00 inclusive (UTC+8)". ~12 words.

## M-5 — The night-dominance disclosure omits its magnitude

**Severity:** Minor (downgraded from Major) · **Section:** §V-A

> "86.5% of PRIMARY UNSAFE hours and 93.2% of RESOLUTION UNSAFE hours were classified UNSAFE solely because they occurred before sunrise, without another UNSAFE trigger."

Verified: 3,389 of 3,917 = 86.52%; RESOLUTION 93.19%. The disclosure is accurate, prominent and new to this version; **I over-graded its absence of magnitude as Major.** Residual: Table II presents 42.88% among environmental metrics with the qualification living only in §V-A prose, and internal diagnostics indicate that removing the policy moves it to roughly 5.8% / 2.8%.

**Correction.** One clause giving the magnitude, or the qualitative form "predominantly a consequence of the declared non-daylight rule interacting with a pre-sunrise evaluation window". If the counterfactual figure is reported it must come through the canonical path and be labelled a diagnostic.

**Caution on the rebuttal's wording, not the paper's.** "Real-world operational gates bind primarily due to daylight rules" overstates it: *this* gate does, because night ⇒ UNSAFE is a researcher-defined policy interacting with a chosen window. The manuscript gets this right. Do not let the rebuttal's gloss migrate into the paper.

## m-5 — C₃ should be demoted, not retained and not deleted

**Severity:** Minor · **Sections:** §III, §V-A, Table II · **Withdrawn in rev 1, reinstated in altered form**

Code inspection (`condition_comparison.py:90–105`) settles this. `C1` and `C3` are **character-identical dict literals six lines apart**, and because `FULL` and `EMPTY` are module-level `frozenset` constants they return the *same objects*; line 198's `x != y` is therefore `False` on every hour by object identity. **There is no assertion anywhere in the script** — the zero is printed in a matrix cell, not checked.

What the zero tests is transcription of two literals, **conditioned on state coverage**: a typo at a state that never occurred would still read 0.00%. That makes it **strictly weaker** than a one-line direct map comparison. And the pipeline's sensitivity is already evidenced beside it by Δ(C0,C1) = 42.88% and Δ(C0,C2) = 48.69% being non-zero.

My rev-1 withdrawal accepted the formal-verification analogy without checking the condition that makes equivalence checking informative: **independence of construction**. Equivalence checking an artefact against a copy of itself carries no information.

But the code comment reveals the point worth keeping: C₃ models a design in which "the intermediate level changes **supervisory intensity**, not AI scope." So **the zero does not show C₃ is the same design as C₁ — it shows the metric cannot see the dimension in which they differ.** That is a limitation of the paper's own criterion, currently sold as a verification result.

**Correction — demote.** One passage in §III (~480 ch) replacing ~1,110 ch across four locations; delete the Table II row and its caption clause; delete the §V-A paragraph; keep [10] cited in §II. Drop "conformance check" from the manuscript's vocabulary. If a conformance check is wanted, add the one-line `assert` to the script.

> "A three-state configuration that does not contract scope at the intermediate state — such as a traffic-light topology in which the intermediate level raises supervisory intensity rather than restricting what the AI may recommend [10] — assigns the same admissible sets at every state as a two-state participation gate. Under the criterion the two are the same governance function, and the criterion therefore cannot distinguish them: a governance difference expressed as supervisory intensity rather than admissible scope lies outside what this metric observes. Declared state cardinality is not by itself evidence of a governance effect."

## M-7 — The C₀–C₃ mappings exist only inside Figure 1

**Severity:** Minor (downgraded), **conditional** · **Section:** §III

**Correction.** Add the four mappings as text (~200 ch). **Do this before Figure 1 is rescaled under the compression plan**, or the definitions become illegible and the paper formally incomplete — at which point this reverts to Major.

## M-8 — The large-vessel configuration is unspecified

**Severity:** Minor (downgraded) · **Sections:** abstract, §V-C, §V-D, §VI

1.26% appears four times from a configuration whose boundaries and source are never given. **Correction:** "…(CAUTION 1.5 m, UNSAFE 3.5 m, > 25 GRT, from [17])…" once, ~60 ch.

## m-1 — Δ is defined without arguments

§III defines Δ for an unnamed pair, then uses "C0↔C2" without binding it to Δ. **Correction:** write Δ(X, Y) and define C0↔C2 ≡ Δ(C0, C2).

## m-2 — "strictly smaller set" versus set inequality

The implementation counts set *inequality*; §III's added nestedness sentence correctly licenses the equivalence, so this is no longer an error. Cleaner to define N<sub>restricted</sub> as hours on which the sets **differ**, then note nestedness makes every difference a strict restriction — property after definition, not before.

## m-3 — The PRIMARY wave source is uncited at the point of claim

[13] is attached to the *weather* records while the ERA5 *wave* claim — the component producing 97.6% of the result — carries no citation. **Correction:** move or duplicate the marker, and note the data came through Open-Meteo's `era5_ocean` endpoint rather than directly from the CDS.

## m-4 — An unverifiable negative claim

> "…since no criterion is published below the thunderstorm level."

**Correction:** "…since no criterion below the thunderstorm level was located in [15]."

## m-6 — "approximately 50 km" is the served grid, not ERA5's native wave resolution

ERA5's wave model runs near 0.36°; 0.5° ≈ 50 km is Open-Meteo's serving grid, confirmed in the project's own provenance record. **Correction:** "ERA5 ocean-wave fields served on an approximately 50 km grid".

## m-7 — One sentence mixes percentage points with raw counts

> "…C0↔C1 = 41.08% and C0↔C2 = 45.56%, a difference of 266 of the 5,935 evaluated hours."

**Correction:** "…a difference of 4.48 percentage points, or 266 of the 5,935 evaluated hours."

## m-8 — Stale code comment contradicts the corrected manuscript — NEW

`classify()`'s docstring states "every figure produced here is a lower bound". The current manuscript correctly says "not necessarily lower bounds". **Class:** manuscript–implementation inconsistency, in the artefact rather than the paper. **Correction:** update the docstring; the code is a cited artefact.

## m-9 — The primary source for the dominant threshold is not held — NEW in rev 2

[16] is absent from `papers/sources/`, and Table 12's cell contents could not be retrieved from the publisher's HTML or PDF. **Correction:** download and hold it; read the ≤10 m / 1 m cell. If it is labelled "caution", one word in §IV closes M-4(b) entirely.

## m-10 — Second stale comment: the solar generator disclaims its own canonical role — NEW in rev 3

`scripts/sensitivity/solar.py`'s docstring states: "Used **ONLY** by the g_t counterfactual sensitivity analysis. **NOT part of the canonical model.**" It is in fact the canonical solar implementation — `build_solar_artefacts.py` imports it unmodified and records its hash, and `canonical_gt.py` cites that hash. **Class:** manuscript–implementation inconsistency, in the artefact. **Correction:** update the docstring; a reader auditing the chain currently meets a file denying it belongs to the chain.

---

# EDITORIAL

**e-1 — PDF metadata.** `Title: Paper Title (use style: paper title)`, `Author: IEEE`. Will propagate to the submitted PDF and may be flagged by IEEE PDF eXpress.

**e-2 — Reference [14] URL appears broken.** `.../angin-kencang-and-laut-bergelora/` mixes English "and" into a Malay slug ("dan"). Verify before submission; it also blocks independent checking of the wind threshold phrasing.

**e-3 — Author block has run-together text.** "SamsuddinFaculty…", "Malaysiamohd_iskandar…", "88400Sabah". Rebuild from the template.

**e-4 — Non-claims restated four times** (§I ¶18, §III ¶62, §V-D ¶119, §VI ¶121–122). State once in §VI, refer elsewhere in a clause. The cheapest space on the page.

---

# Verified reproducibility posture — NEW in rev 3

A review that recorded only defects would misrepresent the evidence. The pipeline audit found the substance in materially better shape than the manuscript conveys.

| Element | Finding | Classification |
|---|---|---|
| **The irreducible archive is three files** | `raw_weather_sea.csv`, `raw_marine_era5_sea.csv`, `raw_marine_mfwam.csv`. Everything downstream is a deterministic function of them. | — |
| **No intermediate state** | `condition_comparison.py` reads the three CSVs, classifies in memory and prints. The prediction-register write is opt-in behind `--write-register` and affects no reported figure. Three inputs, two scripts, print. | **Fully reproducible** |
| **Every chain link is version-controlled** | 10 of 10 checked are git-TRACKED: the three raw CSVs, the solar artefact and both its validation companions, the solar generator, `solar.py`, `canonical_gt.py`, `condition_comparison.py`, `collect_raw_v2.py`, and the archived capture. | **Reproducible only with preserved inputs** |
| **The solar artefact is derived, not an input** | Regenerated **1,827/1,827 rows exactly** from preserved code under a pinned, USNO-validated specification. | **Fully reproducible** |
| **No manual files in the canonical chain** | The one artefact that looked hand-made is script-generated and verified. | **Fully reproducible** |
| **Canonical figures** | Reproduced twice independently in this session: 9,135 / 531 / 42.88% / 48.69% / 5.81% and 5,935 / 266 / 41.08% / 45.56% / 4.48%, with 518 + 13 and ties 0. | **Reproducible only with preserved inputs** |
| **Re-collection from the provider** | Not pinned: grid resolution, reanalysis revision, and eleven provider-side nulls. | **Dependent on external service stability** |
| **Historical Python minor version; cross-platform float behaviour** | Unrecorded; no byte-level evidence across builds or architectures. | **Missing or unverifiable** |
| **Repository public accessibility** | Not established. | **Missing or unverifiable** |

**What the manuscript should claim: deterministic repeatability from archived inputs.** Not "exact reproducibility", which most reviewers read as recollection — the one sense the project cannot support. Not "conditional reproducibility", which is vague where the evidence is precise; the condition is nameable. The honest formulation is two clauses: *the reported figures are exactly repeatable from the archived inputs, and the archived inputs are not guaranteed to be re-retrievable.* Both are verified.

# Open verification items

Recorded as unverified, not doubted.

1. **Table 12's cell label** for vessels ≤10 m at Hs 1 m — "restriction", "caution", both, or a graduated tier. Not retrievable from the publisher through this channel; the body text's own narration is the disjunction quoted in M-4.
2. **MMD's exact phrasing** (inclusive or strict) for the wind and rainfall criteria. Supported only by the project's code provenance comments; reference [14]'s URL appears broken.
3. **References [7], [8], [9], [10]** — not verified against primary texts; recent or not held locally.
4. **Repository public accessibility** — not established.
5. **ERA5 wave native resolution** vs the served 0.5° grid — see m-6.

---

# Section-by-section assessment

**1. Gap, novelty, contribution.** The gap is scoped with unusual discipline — bounded to "the reviewed literature", with three near-neighbour works distinguished on specific properties. The weakness is C-2: nothing is claimed after the concessions.

**2. Alignment RQ → method → experiment → result → conclusion.** Strong and consistent. RQ1 names threshold, vessel-class and denominator sensitivity; §IV specifies all three; §V reports all three; §V-D answers in the same terms. No conclusion is unevidenced. The single misalignment is the title.

**3. Mathematical validity.** Sound. I re-derived the identity independently: C0↔C1 = P(UNSAFE), C0↔C2 = P(UNSAFE) + P(CAUTION), difference = P(CAUTION); the reported decomposition is consistent with this (48.69 − 42.88 = 5.81, and 42.88% is the reported UNSAFE rate). Monotone nesting holds and is correctly invoked. C1 ≡ C3 is correctly characterised as entailed. **No mathematical error.** Defects here are notational (m-1), presentational (M-7), and one proviso stated too narrowly (C-2, the ∅ case).

**4. Reproducibility, numerical consistency, sensitivity.** Numerical consistency **excellent** — 28 claims, zero errors, across two revisions. Sensitivity is honest about being a deterministic configuration range. Reproducibility *from the paper* fails on M-1, M-2 and M-3, and the sensitivity analysis omits its dominant parameter (M-4).

**5. Are conclusions supported?** Yes. The qualification is that the strongest-sounding one — "the intermediate level therefore measurably changes the admissible recommendation set" — is close to analytic given the identity plus a non-zero CAUTION count.

**6. Literature positioning and provenance.** Positioning good; [2]–[5] correctly characterised and correctly disclaimed as not the contribution. Bibliographic details for [1]–[5], [17], [18], [19] check out; [16]'s substantive content now verified from the publisher. Replacing the Copernicus MFWAM product citation with an attribution to the provider's documentation [11] is a clear improvement over v7 — it matches what the evidence supports.

**7. Rejection risk, ordered.** (1) Desk rejection on format — certain if submitted as-is. (2) "The contribution is a tautology" — the paper supplies the ammunition. (3) "Not reproducible from the paper" — fatal at this venue, entirely fixable. (4) "The headline is one unvalidated threshold transfer" — better raised by the authors than discovered by a reviewer. (5) "42.88% is a clock, not the weather" — now disclosed; magnitude still absent.

---

# 8. Page reduction — recosted, and tighter than revision 1 claimed

**Measured starting point (Letter).** Body ends on page 6; **page 7 carries references only, ~2,600 characters.**

### Savings available

| | Cut | Saving |
|---|---|---|
| 1 | **Deduplicate §I ¶14 against §II ¶21–22.** Run-time assurance [2], shielding [3], TCAS [4] and Parasuraman [5] are introduced twice in near-identical terms. Keep §II; reduce §I to one sentence with four citations. | ~1,200 ch |
| 2 | **Consolidate the non-claims** (e-4). | ~900 ch |
| 3 | **Demote C₃** (m-5). | ~630 ch net |
| 4 | **Tighten §III ¶62–63**, folding C-2's reframing in rather than adding to it. | ~500 ch |
| 5 | **Trim Table II** — "Period", "Small-vessel baseline" duplicate §IV; C1↔C3 row removed with m-5. | ~250 ch + ~110 caption |
| 6 | **Merge [11] and [12]** — both cover Open-Meteo retrieval. | ~180 ch |
| | **Total** | **~3,770 ch** |

### Additions required

| | Addition | Cost |
|---|---|---|
| M-1(b) | rule sentence — **highest priority** | ~430 ch |
| M-1(a) | component table | ~450 ch |
| M-1(c) | retrieval sentence | ~250 ch |
| M-4(a)–(f) | six locations | ~750 ch |
| M-2 | availability statement, short form with the provider caveat | ~330 ch |
| M-3 | window clarification | ~70 ch |
| M-7 | inline C₀–C₃ mappings | ~200 ch |
| M-8 | large-vessel configuration | ~60 ch |
| | **Total** | **~2,540 ch** |

### The arithmetic, honestly

Dropping page 7 needs ~2,600 ch freed; the additions need ~2,540 more. **Required: ~5,140 ch. Available from the list above: ~3,770. Deficit ≈ 1,370 ch.**

Revision 1 said the additions fit "with room to spare". That was based on a smaller M-1 fix and no M-4 reframing, and it is **no longer true on Letter**. Three ways to close it, in order of preference:

1. **Convert to A4 first and re-measure.** A4 is 50 pt taller with comparable margins, holding roughly 6% more text per page — on six pages, approximately 2,200 ch of extra capacity. **This alone likely closes the deficit**, and C-1 requires the conversion regardless. Do not plan on Letter numbers.
2. **Compress §II harder.** The three-paragraph treatment of [2]–[5] can go to one paragraph once §I's duplicate is gone: a further ~600 ch.
3. **Move M-1(a) and M-1(c) to a footnote.** IEEE permits footnotes at 8 pt; the table's content survives as prose at roughly 60% of the space.

**Do not cut:** §VI ¶122 (limitations), §IV ¶71 (the marine-warning exclusion argument), §V-C ¶116 (the three component zeros), or Figure 1's legibility. Those are the paper's defensive core and three of them are its best writing.

---

# Overall publication-readiness verdict

> ## MAJOR REVISION — no additional experiments required

**Revision 1 recorded "Accept with Minor Revisions, conditional on two items", on the assumption that M-4 was a one-sentence fix.** It is not. The required changes now touch the title, abstract, research question, method, results, conclusion and limitations. That is a major revision by any ordinary definition, and the honest classification follows the scope of the editing, not the quality of the work.

**The work has not got worse. My reading of what it needs got more accurate.** Across two revisions and five rounds of adversarial re-examination I have checked twenty-eight quantitative claims against preserved machine output, read the classifier line by line, verified the raw input precision from CSV text, retrieved the primary source for the paper's dominant threshold, and run one counterfactual — and found **no numerical error, no mathematical error, and no fabricated provenance.** That is a stronger record than most submissions survive, and several of the author's rebuttals were correct against me.

**What must change before submission.**

1. **C-1** — A4 template, six pages. Mechanical and decisive.
2. **C-2** — rescope the contribution statement: retitle, promote the operationalisation-dependence result, state the ladder-collapse condition as a scope limit, correct the invariance proviso. **All subtractive.**
3. **M-1** — the component table, the rule sentence and the retrieval sentence. Without these, the paper's own reproducibility claim is unverifiable, and an independent reimplementation returns 5.22% rather than 5.81%.
4. **M-2** — one honest availability sentence.
5. **M-4** — six short edits converting an unconditional site measurement into a conditional replay finding.

**What remains after all of that.** One site, one contract shape, and a metric with one bit of sensitivity to the contract it names. A reviewer who requires theoretical novelty may still reject it, and no revision changes that — it is a property of the scope, not the prose. What the revisions buy is that such a rejection becomes a disagreement about significance rather than a finding of defect.

**One thing the pipeline audit changed in the paper's favour.** The reproducibility *substance* is in better shape than the manuscript conveys. The chain is three inputs, two scripts and no intermediate state; every link is version-controlled; the solar artefact — which looked like the weakest link — regenerates exactly from preserved code under a pinned, USNO-validated specification; there are no manual files; and the canonical figures reproduced twice independently. The paper's §IV claim of deterministic repeatability is **true and verified**. What is missing is disclosure: the parameters (M-1), the availability sentence and the repeatability-versus-recollection distinction (M-2). That is the cheapest class of gap there is, and it means the reproducibility criticism in this review is about what the paper *says*, not about what the project *is*.

**On the achievable claim.** The paper can support a conditional replay finding and a negative stability result: *a declared level's binding frequency is a property of its threshold operationalisation rather than of the deployment site.* That claim needs no threshold validation, uses only evidence already in hand, and is more interesting than 5.81%. It is the claim the paper should make, and it is within one editing pass of making it.
