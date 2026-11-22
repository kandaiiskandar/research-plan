# D-4 Priority Report — Safety-Reference Validity, and the N1–N4 Non-Degeneracy Gate Result

> **PARTLY RETRACTED — 17 Nov 2026, same day.** A critical review in `research/d4-critical-review.md` retracts the recommendation of FAO/ILO/IMO 2012 as an **episode-level** hazard reference (no vessel design category is assigned, and at this site every plausible assignment is degenerate: Category C is exceeded in 2 of 9,135 cases), qualifies the N1 pass as holding only for an **anticipative** generator (three temporal leaks identified), and corrects the claim that issue-time forecasts are off the advisory comparison's critical path. **Nothing below is edited** — every original criterion, threshold and result is preserved verbatim. Read the review alongside this document.


**Prepared:** 17 November 2026 · **Author of this document:** Claude (Cowork session) · **Status:** critical review and one executed check, not an endorsement

**Authorization boundary observed.** No participant was recruited or contacted. No external request, data request, licence enquiry or ethics submission was sent. The literature work below is source verification from published documents. The N1–N4 gate was run on data already in the repository.

**Frozen artefacts untouched — verified by checksum.** `data/raw_weather_sea.csv`, `data/raw_marine_era5_sea.csv`, `scripts/historical_replay.py` and `scripts/canonical_gt.py` were MD5-checked before and after execution and are byte-identical. The gate script reads them and imports `canonical_gt.g_t`; it writes only into `research/non-degeneracy/`.

**Evidence conventions.** **[VERIFIED]** = read from a primary source or executed against the repository on 17 Nov 2026. **[REPO]** = already documented in this repository. **[UNVERIFIED]** = reported by a source I could not read in the original, or taken from a model-extracted summary rather than page text — flagged, not relied on. **[UNRESOLVED]** = a live contradiction.

**A new three-way distinction is used throughout**, because the two-way one the brief asked for turned out not to be enough:

| Type | What the source evidences | What it can legitimately anchor |
|---|---|---|
| **TYPE A** | **Actual harm** — casualties, capsizes, sinkings, fatalities — related to measured environmental conditions | A **harm-severity** scale |
| **TYPE H** | A **hazard or design limit** — a design category, class rule, warning threshold, stability criterion | A **hazard** scale. Not severity |
| **TYPE O** | **Operability or habitability** — whether a crew can work, whether motion is tolerable | **Neither.** It anchors *workability*, which is not safety |

TYPE O was not in the brief, and separating it out is what makes the §2 finding visible: one of the project's two load-bearing wave boundaries rests on TYPE O evidence, not TYPE H and certainly not TYPE A.

---

## 1. Headline answer to D-4

**No independent harm-severity reference exists for this vessel class in these waters. One credible independent *hazard* reference does. The severity scale specified in the decision package §4.3 therefore cannot be built as written, and must be relabelled rather than rescued.**

Three findings in order of consequence:

1. **The TYPE A void is total, not marginal. [VERIFIED]** There is no study anywhere I could reach that relates realised harm to open or partly decked fishing vessels under about 12 m to **measured** significant wave height in **tropical coastal** water. Every candidate fails on vessel size, on ocean basin, on measurement, or on having no measured wave height at all — and the failures are systematic, not accidental (§4).

2. **An independent graded hazard reference does exist, and it is a good one. [VERIFIED]** FAO/ILO/IMO (2012), *Safety Recommendations for Decked Fishing Vessels of Less than 12 metres in Length and Undecked Fishing Vessels*, clause 1.2.14, gives four graded design categories in significant wave height and wind force. Its scope is the closest match to this project's fleet of any source found, it is free to read, and it shares no source, author or derivation with anything the architecture already uses.

3. **The project's 1.25 m CAUTION/UNSAFE boundary rests on TYPE O evidence. [VERIFIED, REPO]** It is the ceiling of WMO Sea State 3, taken from the highest sea state at which Yaakob et al.'s 6.54 m hull passes **NORDFORSK 1987 criteria in the "heavy manual work" category** — a crew-workability standard. The repository documents every step of this honestly (§2). What it has never said in one place is the consequence: **a boundary anchored in whether a crew can work cannot anchor a scale of how badly they are harmed.** That is the D-4 problem in one sentence, and it is a labelling problem, not a data problem.

---

## 2. What the repository already documents — and where my own subagent overclaimed

A literature subagent reported two "critical provenance findings". **Both are already in this repository, documented more carefully than the subagent credited.** Reporting them as discoveries would have been wrong and would have implied sloppiness that is not there. Setting the record straight:

| Claimed as new | Actually already documented | Where |
|---|---|---|
| "Jeong & Im's formula is built from Wolfson Unit capsize experiments — so Wolfson cannot independently corroborate it" | The repo states the derivation outright: *"Derives a vessel-length-specific departure restriction formula (Hs_KIMO) based on the UK Wolfson Unit MCA capsize research"*, and warns **"Do not say the paper conducted wave tank experiments"** | `notes/Proposal of Restrictions…md:11,30,77` **[REPO]** |
| "Yaakob et al. never derive 1.25 m — it is the WMO Sea State 3 ceiling under motion-comfort criteria" | Appendix C says exactly this: *"the top of Sea State 3, the highest band the hull passes under NORDFORSK 1987 criteria"*, adds **"Yaakob et al. do not themselves characterise either value as a departure prohibition"**, and records it as a threat to internal validity in C.9 | `docs/canonical/appendix-c-formalisation.md:607,609,1041` **[REPO]** |

The notes go further than the subagent did, stating that NORDFORSK was applied in the **"heavy manual work category"** and that *"This paper reports that the crew cannot safely perform heavy manual work at that sea state; it does not characterise this as a departure prohibition"* (`notes/Stability, Seakeeping…md:30,128`). **That is a TYPE O characterisation, written down by this project, a year before anyone asked the D-4 question.**

**So the provenance record is sound. The gap is interpretive, and it is narrow but load-bearing:** nothing in the repository states that a crew-workability criterion cannot anchor a harm-severity scale, because until the rubric was proposed, nothing needed it to. The rubric is what turns a well-documented caveat into a blocker.

**One genuinely new and prospective warning, which is not in the repository. [VERIFIED]** Because Jeong & Im's Hs_KIMO is derived from the Wolfson Unit formula, the Wolfson Unit's own 2024 inshore-fishing-vessel report (a 10.43 m hull, graded notice: ≥43 cm residual freeboard unrestricted, 21–43 cm max 1.3 m Hs, <21 cm max 0.6 m Hs) **cannot be cited as independent corroboration of the 1.0 m CAUTION onset.** Checking Jeong & Im's own formula makes the shared lineage concrete: `Hs = √(1 + 0.352·LOA) − 1` returns ≈0.86 m at 7 m LOA, ≈1.13 m at 10 m and ≈1.29 m at 12 m — essentially Wolfson's 1.3 m. The agreement is one evidence chain seen twice. Nobody has made this error yet; the warning exists so nobody does.

---

## 3. Candidate reference inventory

Independence is assessed against what the architecture already uses: MET Malaysia Cat 1/2 (40 / 50 km/h), MET *Ribut Petir* (20 mm/hr), JPS/DID Infobanjir Light (10 mm/hr), Jeong & Im Table 12 (1.0 m), Yaakob et al. 2015 (1.25 m), COLREGs 20(b).

| Source | Type | Vessel match | Setting | Measurement validity | Licence | Independent? | Verdict |
|---|---|---|---|---|---|---|---|
| **FAO/ILO/IMO 2012**, clause 1.2.14 **[VERIFIED verbatim]** | **H** | **Best available.** Scope is *"new decked vessels of less than 12 m in length (L) and new undecked vessels intended to operate at sea"*; excludes sport and recreation (1.1.4) | Global instrument; Preface directs authorities to adapt to local conditions | Design categories, not measurements. **A** >4 m / >Bft 8 (19 m/s); **B** ≤4 m / ≤Bft 8; **C** ≤2 m / ≤Bft 6 (12 m/s); **D** ≤0.30 m, occasional 0.5 m / ≤Bft 4 (7 m/s) — all conditional on the lead-in *"provided the vessel is correctly operated and is operating at a speed appropriate to the prevailing sea state"* | *"FAO ILO or IMO encourages the reproduction and dissemination"*; non-commercial use authorised free **upon request**. Citing the figures is ordinary citation; reproducing the table verbatim should be requested | **Yes** — cites none of the project's sources. **Caveat:** the four categories coincide exactly with the EU Recreational Craft Directive / ISO 12217 categories, and **FAO does not state where it took them from [UNRESOLVED]** — so whether FAO and ISO are one reference or two is unsettled. Use FAO, cite FAO, and do not present ISO as separate corroboration | **The recommended independent reference — for a hazard scale only** |
| **Jeong & Im 2023** | **H** formula + **A** validation (66 Korean capsizes 1999–2022) | Length-based, <10 m and <24 m | Korea, temperate | Formula from Wolfson + IMO intact-stability minimum; validated against capsize counts, not casualties | CC BY | **No — already used** (the 1.0 m onset) | Cannot serve. Its TYPE A element is the closest thing to harm evidence the project has, and it is Korean |
| **Yaakob et al. 2015** | **O** | **Exact** — two <10 GRT Malaysian hulls, 5.03 and 6.54 m | **Peninsular Malaysia** — Johor / Malacca Strait, **not Sabah / South China Sea** | Maxsurf/Seakeeper against NORDFORSK 1987 **heavy manual work** limits (RMS vert. accel. 0.275 g FP, 0.150 g bridge; lateral 0.070 g; roll 4.0°). **No accident data** | Open access | **No — already used** (the 1.25 m boundary) | Cannot serve, and is TYPE O: it evidences crew workability, not harm |
| **Wolfson Unit 2024**, report 2900_Rev11 | **H** | **10.43 m inshore fishing vessel** — best single-vessel match with a graded Hs scale | UK inshore, temperate; tank tests | 1:6 scale model; graded by residual freeboard | Freely downloadable | **No — shared derivation with Jeong & Im** (§2) | **Must not be cited as corroborating the 1.0 m onset** |
| **MAIB 2002 / 2008** | **A** | **Best size granularity of any TYPE A source** — MAIB 2008 has <10 m *and* <12 m classes | UK, temperate | **Weather qualitative only** — "calm / moderate / rough", "poor / moderate"; **no wave height in any form.** Denominator per 1,000 registered vessels, not vessel-hours. MAIB 2008 **explicitly warns against reading a weather risk gradient from its own data**, because fewer vessels fish in poor weather | UK Open Government Licence — fully reproducible | Yes | Right vessels, real harm, **no wave height.** And a government investigator declining to make the exact inference this project would need |
| **Kim et al. 2024** (Korea, KMST) | **A** | **Explicitly <10 tons** — 94% of the fleet | Korea, temperate | Weather qualitative only; **no wave or wind figures.** Has a real denominator (ship-years, PLL) | CC BY | Yes | Right vessels, real harm, no measured conditions |
| **Wu, Pelot & Hilliard 2009** | **A** | **Unverified — paywalled [UNVERIFIED]** | Atlantic Canada; ice a covariate with the largest effect | The only fishing-vessel study found with wave height **and** a real exposure denominator (traffic per area-day) | Paywalled | Yes | **The one worth an interlibrary request.** Cannot be relied on until the vessel classes are confirmed |
| **Rezaee, Pelot & Ghasemi 2016** | **A** | Four length classes incl. <45 ft | Atlantic Canada | Best exposure measure found (VMS activity) — and **no wave height at all** | Paywalled | Shares an author with the above | Not usable for a wave axis |
| **Heij & Knapp 2014** | **A** | **No fishing vessels** — six commercial ship types | Includes a "Japan, Korea and South Chinese Sea" region | **Decisive defect: incident wave/wind values are not observed at the incident** — they are averages of non-incident records for the same day and area. Authors state risk *levels* cannot be estimated, only slopes | Working paper, free | Yes | Wrong vessels, broken measurement |
| **Rasolofoson et al. 2024** (Lake Victoria) | **A** | **Correct class** — ~50% non-motorised small-scale | **Tropical, but a lake** — no wave climate | **Verbal autopsy**, not measurement. "Rough water" in 47.5% of 141 deaths. Authors state they **did not estimate incidence** — no denominator, so proportions among the dead, not risks | CC BY 4.0 | Yes | Right fleet, right latitude, no measured conditions and no denominator |
| **Al-Salem et al. 2006** (Kuwait) | **H** | 3–25 m risk tables | **Sub-tropical semi-enclosed — closest *setting*** | Critical capsize height ≈8.08 m for a 19 m boat; test Hs ≈7.14 m | Free PDF | Cited **by** Jeong & Im | **Wave heights an order of magnitude above a site where Hs is usually under 1.5 m.** Not transferable |
| **Dahle, Myrhaug & Dahl 1988** | Mixed **H** + **A** | Vessels <45 m; worked at 34.7 m and 15 m — **nothing near 5–12 m** | Norway, temperate | Crest-front steepness ε ≥ 0.25 with H ≥ 4 m (≥3 m for one case); genuine rate: fishing vessels 2.5×10⁻⁴ capsize/vessel-year | Free PDF, Elsevier journal | Yes | Real harm rate, wrong vessel size, wave heights far above this site |
| **Niclasen et al. 2010** | **H** review, relaying others' **A** | **"Small vessels are shorter than 45 m"**, after Dahle **[VERIFIED verbatim]** | North Sea, Iceland | See §5 — the figures commonly quoted from this paper are **[UNVERIFIED]** | Free PDF | Cited **by** Jeong & Im | **Its argument matters more than its numbers.** See §5 |
| **SEAFDEC 2010** | **A** in kind | Right fleet, right region | **Southeast Asia — the closest geographic match of any source** | **No wave-height statistics and no numeric limits anywhere.** For Malaysia, reports regulation only — no accident statistics at all | Free | Yes | The right region's evidence base is empty |
| **MMEA SAR statistics** | — | — | Malaysia | **No structured or published dataset found** — press reports only, with no weather covariates, vessel sizes or denominators | — | — | Would need a formal data request, which is outside authorization |

**Not verified at all, and not to be cited from this review: [UNVERIFIED]** Wang, Pillay, Kwon, Wall & Loughran (2005) — could not be retrieved by any route; Roberts on UK fishing fatalities — blocked by a CAPTCHA wall; ISO 12217-1:2022 scope and category clause — paywalled and absent from the free preview, so **the category figures must not be cited to ISO**; the authoritative RCD Annex I legal text; any Japanese aggregate capsize-versus-wave study.

---

## 4. Hazardous conditions versus actual harm — the direct answer

**Question: is there a TYPE A source relating realised harm to small open fishing vessels to measured wave height in tropical coastal waters?**

**No. Not a near miss — a complete and structured absence.** The literature divides into three groups, and no source sits in the intersection:

- **Right fleet, right region, no measured conditions.** SEAFDEC 2010 covers exactly this fleet in exactly this region and contains no wave-height data of any kind. Rasolofoson et al. 2024 has the right vessel class, tropical latitude and 141 real deaths — assigned by verbal autopsy, with no measured wave height and no denominator.
- **Right vessels, real harm, no wave height.** MAIB 2008 (<10 m and <12 m classes) and Kim et al. 2024 (<10 tons, with a proper ship-year denominator) record weather only qualitatively. MAIB 2008 additionally warns against inferring a weather gradient from its own data.
- **Measured wave height, wrong fleet or wrong basin or broken measurement.** Wu et al. 2009 is the only fishing-vessel study with wave height and a real denominator — Atlantic Canada, ice-dominated, vessel classes unverified. Heij & Knapp 2014 reaches the South China Sea region but covers no fishing vessels and assigns conditions from same-day area averages rather than the incident location.

**One named candidate behaved opposite to expectation, and this matters for how the project argues. [VERIFIED]** The Jin corpus — Jin et al. 2002, Jin & Thunberg 2005, Jin 2014 — **does not use wave height at all**; it models wind speed and, in 2014, sea-level pressure. It also found **small vessels had the *lowest* accident probability** in a temperate 16–165 ft fleet. So it cannot support a wave threshold, and its size gradient runs against the project's premise. Jin 2014 is nonetheless the best *methodological* template found anywhere: two ordered-probit severity scales, which is the shape a graded harm model needs. **[UNVERIFIED]** — these readings rest on abstracts and preview text, not full text; confirm before citing.

### What this does to the project's own thresholds

| Boundary | Evidence type it actually rests on | Can it anchor severity? |
|---|---|---|
| Wave 1.0 m (CAUTION onset) | **H** — Jeong & Im Table 12, from the Wolfson formula, validated against Korean capsize counts | Partly. It is the strongest wave number the project has, and it is Korean and formula-derived |
| Wave 1.25 m (UNSAFE) | **O** — WMO Sea State 3 ceiling, via NORDFORSK 1987 heavy-manual-work limits | **No.** Workability is not harm |
| Wind 21.6 / 27.0 kn | **H** — MET Malaysia Cat 1/2 warning onsets | No. A warning trigger is a hazard statement |
| Rain 10 / 20 mm/hr | **H** — JPS/DID Light upper limit; MET *Ribut Petir* | No |

**Every graded wave number available to this project — 0.30 m, 1.0 m, 1.25 m, 1.3 m, 2.0 m — is a design category, model-test, or motion-comfort limit. None is calibrated against observed harm to boats of this size in these waters.** Given that Δ_L2 = 5.81% is governed almost entirely by the wave CAUTION onset at ≈ −1.2 pp per 0.05 m, this is not cosmetic: the headline result's sensitivity is a direct consequence of a severity boundary resting on non-severity evidence.

---

## 5. The alternative construct, and why I am not yet recommending it

Niclasen et al. (2010) suggests that **how unexpected a sea state is matters more than its absolute height**. The abstract says so in the paper's own words, verbatim: *"Ship accident statistics suggest that the Hm0 value of sea state is not as important as whether this value is unexpected, due to rapid development or compared to local wave climate."* **[VERIFIED verbatim]**

That is attractive here. A climatological-percentile onset is computable from the 43,848-record archive the project already holds, needs no new data and no licence, and would be far less sensitive than a 0.05 m shift in an absolute boundary. The gate run in §6 incidentally demonstrates that percentile logic works cleanly on this record.

**Three reasons to hold it as a candidate rather than a recommendation:**

1. **The figures usually quoted from this paper are [UNVERIFIED].** "Two in three accidents below Hm0 4 m", "three in four above the 0.8 monthly quantile", "four in five with a ≥20% wind-sea rise in 6 h", and the "surprisingly low correlation between high waves and accidents" all come from a **model-extracted summary of the unread portion**, not from page text. They must be verified in the original before any of them appears in a thesis.
2. **Its "small vessel" means under 45 m. [VERIFIED verbatim]** The paper takes the definition from Dahle et al. A 7 m open outboard boat is not what it is about.
3. **The 270 accidents' vessel types are not stated in the read portion,** nor is it confirmed whether conditions were measured at the accident site or assigned from a model. For a paper whose central claim is about measurement reference, that is exactly the thing that needs checking.

**It also would not solve D-4.** A climatological-unexpectedness onset is still a **hazard** construct. It would be better-argued and less threshold-sensitive, but it would not turn a hazard scale into a harm scale.

---

## 6. The N1–N4 non-degeneracy gate — specified, then run once **[VERIFIED]**

### 6.1 What was built, and how independence was kept

An external candidate-advice generator, written to `research/non-degeneracy/non_degeneracy_gate.py`. It is **stimulus material, not a proposed system**, and it is independent of the architecture by construction:

- it never reads `S`, `G(S)` or `A_AI(S)`;
- it uses **no architecture threshold** — not 21.6/27.0 kn, not 10/20 mm/hr, not 1.0/1.25 m. Its only parameters are percentiles of the record's own empirical distribution;
- it aggregates by the **arithmetic mean** of the three variables' percentile ranks, deliberately **not** by max-severity, so it does not mirror the classifier's aggregation rule.

Advice per departure-window hour: `Go` if exposure ≤ P60 else `Delay`; `DepartureTime` when a strictly better later hour exists in the same window (≥5 percentile points better, and itself ≤ P70); `Duration` when ≥2 consecutive forward hours are ≤ P70. The three arms then filter that pool: C0 unfiltered, C1 by `G(S)`, C2 by `A_AI(S)`.

**N1–N4 and their thresholds were fixed in the decision package before the generator existed, and the gate was run once.** The ε values for N4 (wave ±0.05 m, wind ±0.5 kn, rain ±0.5 mm/hr) were fixed in the script before first execution, taken from the project's own sensitivity step granularity and each variable's data resolution.

### 6.2 Method validation — two independent reproductions

| Quantity | Canonical value | This run | |
|---|---|---|---|
| Record hours | 43,848 | **43,848** | ✓ |
| Departure-window cases | 9,135 | **9,135** | ✓ |
| CAUTION hours | 531 | **531** | ✓ |
| P(S = CAUTION) ≡ Δ_L2 | 5.81% | **5.8128%** | ✓ |
| UNSAFE share ≡ C0↔C1 | 42.88% | 3,917 / 9,135 = **42.88%** | ✓ |

The read-only classifier reproduction recovers two independently published headline figures exactly. That is the method check for everything below it.

### 6.3 Results, reported as they came out

| | Criterion | Threshold | Result | |
|---|---|---|---|---|
| **N1** | Each advice type appears in ≥10% of the ungated pool | 10% | `Go` **69.38%** · `Delay` **30.62%** · `DepartureTime` **36.12%** · `Duration` **72.56%** | **PASS** |
| **N2** | C1 and C2 differ in presented content in ≥20% of cases | 20% | **2.69%** over all 9,135 cases | **FAIL** |
| **N2′** | same, over a CAUTION-only pool | 20% | **46.33%** | **PASS** |
| **N3** | Within CAUTION, a withheld type (`DepartureTime` or `Duration`) is actually generated in ≥50% of cases | 50% | **46.33%** | **FAIL by 3.7 points** |
| **N4** | ≥30% of cases qualify as boundary cases | 30% | **6.17%** (564 of 9,135) | **FAIL** |

**`GATE_PASS_as_preregistered: false`.**

### 6.4 What each result actually means

**N1 passes decisively, and this is the finding that unblocks B2.** The degeneracy is in the *prototype's rule set*, not in the problem. An external generator produces all four advice types at usable rates from the same environmental record. The pool composition is varied — `Duration|Go` 3,798 cases, `DepartureTime|Duration|Go` 2,254, `Delay` 1,534, `Delay|DepartureTime` 687, `Delay|DepartureTime|Duration` 342 — against the prototype's `["Delay"]` × 244 and `[]` × 48. **A non-degenerate candidate pool is achievable at this site.**

**N2's unstratified failure is structural and no generator can fix it.** C1 and C2 differ only at CAUTION, so the ceiling on unstratified divergence is `P(S = CAUTION) = 5.81%`. The observed 2.69% is that ceiling multiplied by the 46.33% of CAUTION hours in which a withheld type was actually generated — the two numbers are consistent to the case. **N2 was mis-specified as written: a 20% unstratified divergence requirement is unreachable by construction, and I set it.** The usable form is N2′, which passes — but it requires deliberate CAUTION stratification, and that must be declared, because it changes the population the result generalises to from "departure hours at this site" to "departure hours in the intermediate state".

**N3 fails narrowly, and the bar stays where it is.** 46.33% against a pre-registered 50%. I am not moving it: a threshold adjusted after seeing the result is not a threshold. What the number means in practice is that **246 of the 531 CAUTION cases have genuinely differing arm content** — ample for a 40-case pilot and for a full study of a few hundred. So N3's failure says the pre-registered bar was optimistic, not that the study is impossible. The honest report is: *failed as pre-registered; the available pool is nonetheless sufficient; re-specify and re-run before claiming a pass.*

**N4 fails badly, and it was the wrong criterion.** At ε = 0.05 m only 6.17% of cases sit within a boundary band, and the composition shows why: **wave 557 cases, wind 2, rain 6.** Reaching 30% would need ε ≈ 0.25 m, which is no longer a boundary. But 564 boundary cases exist in absolute terms, and a 40-case pilot needs about 12. **The criterion should have been absolute availability, not share** — boundary cases are to be obtained by stratified sampling from the 564, not by hoping a third of the pool qualifies. The figure the design actually needs is the intersection: **176 of the 564 boundary cases are CAUTION hours**, and a 40-case pilot drawing ≥12 boundary cases from a CAUTION-stratified pool is comfortably inside that. This is a respecification I am flagging as my own error, not retrofitting to pass.

The wind and rain counts are themselves a finding that corroborates RQ3's negative result from a new direction: with 2 wind and 6 rain boundary cases in five years, **those components cannot support a boundary stratum at all.** Any boundary-case design here is a wave-boundary design.

### 6.5 Honest verdict on the gate

**The gate fails as pre-registered, and the study is nonetheless more feasible than before it ran.** N1 — the question of whether a non-degenerate pool is possible — is answered yes with room to spare. The three failures are: one structural ceiling I specified wrongly (N2), one optimistic bar that the available pool still satisfies in absolute terms (N3), and one criterion in the wrong units (N4). None of them is a property of the site or the data that blocks the design. **But "pre-registered criteria failed, then were respecified" is exactly the pattern a reviewer distrusts**, so the respecified gate must be published with both the original and the revised criteria, the reasons, and this run's numbers — not quietly replaced.

---

## 7. Minimal blinded reference-validity test **[PROPOSED — not run, no recruitment]**

This test asks one question: **does a candidate reference tell us anything the architecture does not already tell us?** It is the cheapest possible way to detect circularity, and it needs no raters at all in Stage A.

### Stage A — machine-only, no participants, runs on existing data

**Purpose.** Reject any candidate reference that is informationally redundant with the classifier before spending human time on it.

| Step | What is done |
|---|---|
| **A1** | Encode the candidate reference as a scoring function over the environmental record, independent of `S`. For FAO 2012, that is the four design categories applied to Hs and wind |
| **A2** | Score all 9,135 departure-window cases under both the candidate reference and the architecture's `S` |
| **A3** | Cross-tabulate. Compute Cramér's V, and the share of cases where the two disagree in rank order |
| **A4** | Apply the §4.4 multi-signal provenance test (S1–S5) to every threshold in the candidate reference, and record the table |

**Go / no-go for Stage A, pre-registered:**

| | Criterion | Rationale |
|---|---|---|
| **NO-GO** | Cramér's V ≥ 0.90 against `S` | The reference is a relabelling of the classifier. A rubric built on it cannot detect the classifier being wrong |
| **NO-GO** | Disagreement in <10% of cases | Too few cases where the reference could contradict the architecture; the study has no discriminating power |
| **NO-GO** | The provenance test flags the reference's **wave** threshold as architecture-dependent (S2∧S3, or S3∧S4∧S5) | Wave is 97.6% of activation. A dependent wave threshold is fatal; a dependent wind or rain threshold is a declarable limitation |
| **GO** | V < 0.90, disagreement ≥10%, wave threshold unflagged | Proceed to Stage B |

**FAO 2012's expected position, stated before the test is run so it cannot be fitted afterwards:** its wave figures (2.0 m, 0.30 m) do not coincide with 1.0 m or 1.25 m and should pass S3 cleanly. **Its wind figure will not.** Category C's Bft 6 ≈ 12 m/s sits essentially on MET Malaysia's 40 km/h = 11.1 m/s, which the architecture already uses — so **FAO Category C cannot be presented as independent corroboration of the wind boundary**, and that must be declared whether or not the multi-signal rule formally flags it. **[VERIFIED]** The derivations are unrelated; the values nearly coincide; both facts go in the write-up.

### Stage B — minimal blinded human test. Requires ethics approval; **not initiated**

**Purpose.** Establish that the reference can be applied consistently by someone who cannot see the architecture — the only way to show the scale is a scale and not a restatement.

| | Specification |
|---|---|
| **Scale** | 2 raters, **20 cases**, drawn as 10 boundary (from the 564) and 10 non-boundary, stratified across `S` |
| **What a rater sees** | The environmental conditions, and the candidate reference's own definitions. **Not** `S`, not the arm, not any advice |
| **Task** | Assign each case a level on the candidate reference's scale — nothing else. This is an instrument test, not an advice-rating task |
| **Blind integrity check** | After scoring, each rater is asked to state any rule they think the cases were selected by. A rater who names the classifier's thresholds has broken the blind, and that is a result, not a nuisance |

**Go / no-go for Stage B, pre-registered:**

| | Criterion |
|---|---|
| **GO** | Gwet's AC1 ≥ 0.70 between raters **and** neither rater recovers the classifier's thresholds in the blind check |
| **REVISE** | AC1 0.50–0.70 — the anchors are ambiguous; rewrite them and re-run Stage B once |
| **NO-GO** | AC1 < 0.50 — the reference cannot be applied consistently, so it cannot serve as a reference however well-sourced it is |
| **NO-GO** | Either rater recovers the classifier's thresholds from the cases alone — the reference is not operationally independent of the architecture, whatever its paper provenance says |

**Gwet's AC1, not κ**, for the reason already in the decision package: severity here will be heavily skewed toward the low anchors, and κ-family statistics collapse under prevalence skew. Reporting a low κ on skewed data and calling it poor agreement would be an artefact.

**Why 20 cases and 2 raters.** This is deliberately below any effect-detecting size. It is an instrument check, and it is specified at the smallest scale that can fail informatively — because if the instrument does not survive this, nothing built on it is worth the ethics application.

### What the test cannot do

It cannot make a hazard reference into a harm reference. **If FAO 2012 passes both stages, the project has a validated, independent, graded *hazard* scale — and the rubric's K1 and K3 constructs must be relabelled accordingly.** There is no version of this test that produces a harm-severity scale from the sources that exist.

---

## 8. Uncertainties

1. **The TYPE A void is an absence of found evidence, not a proof of absence.** It rests on one search pass with several blocked sources (§3). Wu et al. 2009 in particular could change the picture if its vessel classes include boats under 12 m — it is the single interlibrary request most worth making.
2. **Whether FAO 2012 and ISO 12217 are one reference or two is [UNRESOLVED].** The categories coincide exactly; FAO does not state a source; ISO's own text is paywalled and absent from the free preview. Until that is settled, they must be treated as **one**.
3. **The Niclasen figures are [UNVERIFIED]** — summary-derived, not read from the page. None may be cited until confirmed in the original.
4. **The Jin corpus readings are [UNVERIFIED]** — abstracts and preview text only. The claim that none of the three uses wave height needs full-text confirmation.
5. **The generator is one of three designs named in the decision package**, and the cheapest. An expert-authored stimulus set would be more defensible and much more expensive. N1's pass is a property of *this* generator, not of all possible generators.
6. **N2′, N3 and N4 all need respecification, and respecified criteria are weaker evidence than pre-registered ones.** Both versions must be published.
7. **The 246 differing-arm CAUTION cases are concentrated in the wave component.** With 2 wind and 6 rain boundary cases in five years, any finding from this design is a finding about waves, generalising to other components only by assumption.
8. **The exposure index weights all three variables equally.** That is a declared arbitrary choice, not a derived one, and a different weighting would change N1's type shares.
9. **Nothing here was run against the RESOLUTION (MFWAM) configuration.** All gate figures are PRIMARY only.

---

## 9. Next supervisor decisions

| | Decision | Who | Cost | Recommendation |
|---|---|---|---|---|
| **D-4a** | **Accept that no harm-severity reference exists, and relabel the rubric's K1/K3 as a hazard scale anchored in FAO/ILO/IMO 2012.** This is the substantive answer to D-4 | Supervisor | One meeting | **Accept.** The alternative is a severity claim the evidence cannot carry. Relabelling costs the word "severity" and keeps the design |
| **D-4b** | Authorize Stage A of the reference-validity test — machine-only, existing data, no participants | Author | Hours | **Proceed.** It can reject FAO 2012 for redundancy before anything else is spent |
| **D-4c** | Decide whether to pursue the Niclasen climatological-unexpectedness construct as the wave axis, **conditional on verifying its figures first** | Supervisor | Days to verify | **Verify, then decide.** Promising and less threshold-sensitive, but still a hazard construct and defined for vessels under 45 m |
| **D-4d** | Whether to request Wu et al. 2009 by interlibrary loan — the one source that could overturn the TYPE A void | Author | One request | **Request it.** Cheapest way to test the review's central negative claim |
| **D-3′** | **Re-specify N2, N3 and N4 and re-run the gate once**, publishing both criterion sets and this run's numbers | Author | Hours | **Proceed, with both versions published.** Silently replacing failed criteria is the one thing that would make this worse than leaving them failed |
| **D-4e** | Record in Appendix C that the 1.25 m boundary rests on **TYPE O** (crew-workability) evidence, and that the Wolfson Unit report cannot corroborate the 1.0 m onset | Author | Minutes | **Record it.** Appendix C already documents the provenance correctly; this adds the two interpretive consequences, alongside the open 2.8 m item |

**What I would do first.** D-4b, because it is free and can kill the chosen reference; then D-4a, because every other decision depends on whether the project is willing to say "hazard" instead of "severity". **D-4a is not a retreat.** A graded hazard scale with a verified independent source, honestly labelled, is defensible at a viva. A severity scale resting on a crew-workability criterion is not, and an examiner who reads Appendix C C.9 will find the thread already pulled.
