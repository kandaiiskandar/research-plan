# V. Results and Discussion

## A. Binding Frequency and Comparator Decomposition

The PRIMARY replay gave Δ<sub>L2</sub> = 5.81% and the RESOLUTION configuration gave 4.48%. These are proportions of evaluated departure-window hours in which the intermediate advisory-scope restriction binds. As established in Section III, this equals CAUTION occupancy under these mappings.

The PRIMARY comparator decomposition separates the two levels. C0↔C1 gave 42.88%, the frequency associated with participation gating alone, and C0↔C2 gave 48.69%, the frequency associated with participation gating together with the intermediate contraction. The difference, 48.69 − 42.88 = 5.81 percentage points, isolates the incremental binding frequency associated with the intermediate level under the comparator construction. The direct C1↔C2 comparison returned the same value. The RESOLUTION pairwise components are not reported because their provenance is incomplete; Δ<sub>L2</sub> is unaffected.

The two configurations differ in both wave source and record period, and the gap between 5.81% and 4.48% indicates that the measured binding frequency depends on the environmental-data configuration used for replay. Neither value is treated here as more accurate than the other, and the difference is not attributed to spatial resolution alone.

Both configurations returned C1↔C3 = 0.00%. This is the entailed result rather than an empirical finding: C1 and C3 assign identical admissible sets at every state, so the replay provides a conformance check on the configured mappings. It indicates that C1 and C3 are equivalent as governance functions under the admissible-set criterion, and nothing about whether three-state designs are useful in general.

**TABLE III**
*Binding frequency, comparator decomposition and robustness results.*

| Metric | PRIMARY | RESOLUTION |
|---|---|---|
| Period | 2020–2024 | 2021-10–2024 |
| Departure-window hours | 9,135 | 5,935 |
| C0↔C1 | 42.88% | — |
| C0↔C2 | 48.69% | — |
| Δ<sub>L2</sub> | 5.81% | 4.48% |
| C1↔C3 | 0.00% | 0.00% |
| Sourced-threshold envelope | 5.67–9.56% | 4.26–6.64% |
| Small-vessel baseline | <10 GRT | <10 GRT |

— indicates pairwise resolution components withheld because provenance is incomplete; Δ<sub>L2</sub> is unaffected. C1↔C3 = 0.00% is entailed by the mappings and is reported as an implementation conformance check. The sourced-threshold envelope is a deterministic configuration range, not a confidence interval.

## B. Threshold Sensitivity

Across externally sourced threshold configurations for the small-vessel baseline, Δ<sub>L2</sub> spans 5.67–9.56% in PRIMARY and 4.26–6.64% in RESOLUTION. These are deterministic configuration ranges obtained by replaying defensible threshold settings, not confidence intervals or uncertainty estimates. The measured binding frequency is therefore not a threshold-invariant property of the site.

Provenance does not by itself remove designer interpretation. The small-vessel wave source supports two defensible readings of the UNSAFE boundary, an operational ceiling and a failure point, which give 5.81% and 9.22% respectively. Both are traceable to the same source [YAAKOB], and neither is selected here as correct.

A separate perturbation of the wave CAUTION onset by ±0.25 m moves Δ<sub>L2</sub> across 2.54–14.75%. This is a controlled movement of one boundary rather than a survey of sourced configurations, and the two ranges answer different questions. Over the evaluated perturbation the sensitivity is approximately −1.4 percentage points per 0.05 m, which describes how the measurement responds across the evaluated range rather than a causal derivative.

Other components contribute far less. Varying the rainfall CAUTION boundary moves Δ<sub>L2</sub> by 0.48 percentage points in PRIMARY and 0.78 in RESOLUTION, so the non-MET boundary identified in Section IV had comparatively little influence on the result in this evaluation. The wind boundary is a structural zero across the evaluated range *W*<sub>C</sub> = 18–25 kn: no setting within that range altered the classification of any evaluated hour.

**FIGURE 1** *(placeholder — plot data not yet exported)*
*Δ<sub>L2</sub> against the wave CAUTION onset for the PRIMARY and RESOLUTION configurations. The sourced-threshold region is marked as a shaded band, and the operational-ceiling reading used throughout is marked on the PRIMARY trace.*

## C. Component Attribution and Scope Dependence

Within the PRIMARY departure window, 531 hours were classified CAUTION, and attribution across the component classifiers is uneven. The ocean-state component accounted for 518 of those 531 hours, or 97.6%, and the rainfall component for the remaining 13, or 2.4%. These are attributions of CAUTION classification, not of incidents or unsafe outcomes, none of which is observed here.

The three remaining components register zero, for three different reasons, and the distinction matters. No PRIMARY CAUTION hour was attributed to wind, which is an empirical negative finding for the evaluated record and is separate from the structural zero reported for the wind threshold range above. The time component emits no CAUTION by construction, so its zero is definitional. The marine-warning component is structurally excluded, and its zero reflects unavailability rather than evidence that marine warnings never bind.

The measured frequency also depends on configuration choices fixed in Section IV. Under the medium- and large-vessel threshold configurations the PRIMARY value falls to 1.96% and 1.26% respectively, and to 0.66% and 0.37% in RESOLUTION. Replacing the departure-window denominator with a daylight-only denominator raises it to 9.59% in PRIMARY and 7.40% in RESOLUTION. Vessel class and denominator are evaluation-policy settings, and neither variant is presented as more appropriate than the departure-window baseline. Because the marine-warning component was held at its least-severe value and classification aggregates by maximum severity, the activation frequencies reported here are interpreted as lower bounds under that exclusion.

RQ1 can now be answered. For the PRIMARY configuration at the evaluated site and small-vessel baseline, the intermediate advisory-scope contraction binds in 5.81% of departure-window hours, and in 4.48% under the RESOLUTION configuration. That frequency is conditional rather than fixed: it spans 5.67–9.56% across sourced threshold configurations, moves across 2.54–14.75% under a ±0.25 m wave-onset perturbation, falls to 1.96% and 1.26% for the medium and large vessel classes, and rises to 9.59% under a daylight-only denominator. The intermediate level therefore measurably changes the admissible recommendation set under the evaluated contract, while the frequency of that change is conditional on threshold, vessel-class and denominator choices.

The interpretation this supports is narrow. A declared intermediate level can be audited through whether, and how often, it changes the admissible recommendation set, and for this contract it does bind in historical replay. The resulting rate cannot be read without also examining threshold provenance, component attribution, vessel-class assumptions, denominator policy and the treatment of the excluded component. The results do not establish that the restriction is correct, optimal, safer or beneficial, that decision quality or oversight improved, or that these figures extend to other sites, vessel classes or periods.

---

## Drafting Audit

| # | Check | Result |
|---|---|---|
| 1 | Section V prose word count | **899** — inside target 850–910 and the preferred 870–900 band; ceiling 930 not approached. Table and figure captions excluded |
| 2 | TABLE III included | **YES** — single compact table, eight rows |
| 3 | FIGURE 1 included or placeholder | **PLACEHOLDER** — caption and axis specification given, no plotted data |
| 4 | FIGURE DATA EXTRACTION REQUIRED | **YES** — see carried-forward task below |
| 5 | PRIMARY Δ<sub>L2</sub> = 5.81% | **YES** |
| 6 | RESOLUTION Δ<sub>L2</sub> = 4.48% | **YES** |
| 7 | PRIMARY C0↔C1 = 42.88% | **YES** |
| 8 | PRIMARY C0↔C2 = 48.69% | **YES** |
| 9 | Decomposition stated in percentage points | **YES** — *"48.69 − 42.88 = 5.81 percentage points"*; not framed as a relative increase |
| 10 | RESOLUTION pairwise components not invented | **YES** — em dash in Table III, with the short provenance note; no value stated, inferred or back-solved |
| 11 | C1↔C3 = 0.00% only as entailed conformance | **YES** — *"the entailed result rather than an empirical finding"*, plus the explicit guard that it says nothing about whether three-state designs are useful in general |
| 12 | Δ<sub>L2</sub> identity not re-derived | **YES** — one clause, *"As established in Section III, this equals CAUTION occupancy under these mappings"* |
| 13 | 5.81% as binding frequency, not safety effect | **YES** |
| 14 | Sourced-threshold envelopes reported | **YES** — 5.67–9.56% PRIMARY, 4.26–6.64% RESOLUTION |
| 15 | Envelope as deterministic configuration range | **YES** — *"not confidence intervals or uncertainty estimates"*, repeated in the table note |
| 16 | Same-source readings 5.81% / 9.22% | **YES** |
| 17 | Operational-ceiling vs failure-point distinction | **YES** — neither selected as correct |
| 18 | Wave perturbation ±0.25 m = 2.54–14.75% | **YES** |
| 19 | Envelope and perturbation kept distinct | **YES** — *"the two ranges answer different questions"* |
| 20 | ≈ −1.4 pp per 0.05 m without causal language | **YES** — *"rather than a causal derivative"* |
| 21 | Rainfall 0.48 pp PRIMARY / 0.78 RESOLUTION | **YES** — *"had comparatively little influence"*; no claim that rainfall does not matter |
| 22 | Wind structural zero over 18–25 kn | **YES** |
| 23 | PRIMARY CAUTION total = 531 | **YES** |
| 24 | *g*<sub>o</sub> = 518/531 = 97.6% | **YES** — stated as attribution of CAUTION classification, not of risk or unsafe outcomes |
| 25 | *g*<sub>r</sub> = 13/531 = 2.4% | **YES** |
| 26 | *g*<sub>w</sub> = 0 as empirical negative finding | **YES** |
| 27 | *g*<sub>t</sub> = 0 as definitional | **YES** |
| 28 | *g*<sub>m</sub> as structurally excluded | **YES** — *"reflects unavailability rather than evidence that marine warnings never bind"* |
| 29 | Two wind zeros kept epistemically distinct | **YES** — the attribution zero is explicitly marked *"separate from the structural zero reported for the wind threshold range above"* |
| 30 | Vessel class 5.81 / 1.96 / 1.26 | **YES** — with the locked RESOLUTION variants 0.66% / 0.37% |
| 31 | No "larger vessels are safer" claim | **YES** — presented as deterministic configuration variants |
| 32 | Daylight denominator 9.59% / 7.40% | **YES** |
| 33 | Denominator dependence as policy dependence | **YES** — neither variant presented as more appropriate |
| 34 | Lower-bound qualification carried forward | **YES** — one sentence, no re-derivation |
| 35 | Lower bound not a contribution claim | **YES** |
| 36 | Direct answer to RQ1 | **YES** — one compact paragraph, prose not list |
| 37 | RQ1 answer includes configuration dependence | **YES** — envelope, perturbation, vessel class and denominator all carried in the answer |
| 38 | No claim three-state is better than binary | **YES** |
| 39 | No safety / accident / decision-quality claim | **YES** |
| 40 | No optimality claim | **YES** |
| 41 | No generalisation claim | **YES** |
| 42 | No statistical inference language | **YES** — no *significant*, *p-value*, *confidence interval*, *sampling error* |
| 43 | No new experiment introduced | **YES** |
| 44 | No new literature discovery | **YES** — the only citation key used is [YAAKOB], already locked |
| 45 | IPoSCI absent | **YES** |
| 46 | MFWAM citation-resolution task carried forward | **YES** |

**47. Unsupported numbers.** None. Every numeral was checked against the locked set in `aai-2026-locked-research-chain-patched.md` §§11–12. The only bare numerals are `48.69`, `42.88` and `5.81` in the decomposition sentence, which are the locked percentages written without the sign in an arithmetic statement.

**48. Deviation from the patched locked research chain.** None.

**49. Result whose epistemic status was changed.** None. The five component zeros retain their three distinct statuses, C1↔C3 remains entailed, the envelope remains a deterministic configuration range, and the lower bound remains a qualification.

**50. Claim that should be deferred to Section VI.** None identified. Limitations are touched only where a result requires immediate qualification; the consolidated limitations, the non-claims list and future validation remain undrafted.

### Carried forward

**FIGURE DATA EXTRACTION REQUIRED.** No canonical export of Δ<sub>L2</sub> against wave CAUTION onset exists in the supplied files. `scripts/sensitivity/threshold_sensitivity.py` is present but no sweep output is stored, and the locked documents record only summary statistics. No coordinates were interpolated or invented. Figure 1 is a labelled caption and axis specification; the sweep must be exported from the canonical script before camera-ready.

**CITATION-RESOLUTION TASK — MFWAM.** Unchanged from Phase 2. Not addressed here.

### Final logical check

**A.** Yes. The opening sentence defines the values as proportions of hours in which the restriction binds; no safety framing appears anywhere.
**B.** Yes. The decomposition is given as percentage points separating the two levels, while Section III's identity is recalled in one clause; the section never claims the ladder was needed to obtain the value.
**C.** Yes. Five distinct dependencies are reported — sourced thresholds, wave perturbation, vessel class, denominator policy and environmental-data configuration — and the RQ1 answer states the frequency is conditional rather than fixed.
**D.** Yes. Each zero is labelled: *g*<sub>w</sub> empirical negative, *g*<sub>t</sub> definitional, *g*<sub>m</sub> structurally excluded, with *g*<sub>w</sub> additionally separated from the wind threshold zero.
**E.** Yes. C1↔C3 is stated as entailed, with the reason given and its scope limited to equivalence as governance functions under the criterion.
**F.** Yes. The closing paragraph states the measurable effect and then denies correctness, optimality, safety, benefit, decision quality, oversight and extension to other settings.

---

PHASE 3 STATUS: READY FOR REVIEW

---

## Micro-Revision Audit

| # | Check | Result |
|---|---|---|
| 1 | Authorised RQ1 sentence replaced | **YES** — single `str.replace`, guarded by an assertion that exactly one occurrence existed |
| 2 | "has a measurable operational effect" absent from manuscript body | **YES** — substring search returns no match anywhere in the file |
| 3 | "measurably changes the admissible recommendation set" present | **YES** |
| 4 | RQ1 numerical results unchanged | **YES** — 5.81%, 4.48%, 5.67–9.56%, 2.54–14.75%, 1.96%, 1.26%, 9.59% all byte-identical in the same order |
| 5 | Section V-A unchanged | **YES** |
| 6 | TABLE III unchanged | **YES** — all eight rows and both notes byte-identical; RESOLUTION pairwise cells remain em dashes |
| 7 | Section V-B unchanged | **YES** |
| 8 | FIGURE 1 placeholder unchanged | **YES** — label, caption and axis specification byte-identical; no data generated |
| 9 | Component attribution unchanged | **YES** — 531, 518/531, 97.6%, 13, 2.4% and the three zero statuses byte-identical |
| 10 | Vessel-class results unchanged | **YES** — 5.81 / 1.96 / 1.26 PRIMARY, 0.66 / 0.37 RESOLUTION |
| 11 | Denominator-policy results unchanged | **YES** — 9.59% / 7.40% |
| 12 | Lower-bound qualification unchanged | **YES** — not re-derived; no partial identification, no Manski |
| 13 | Final discussion paragraph unchanged | **YES** — line 52 byte-identical |
| 14 | Δ<sub>L2</sub> = 5.81% / 4.48% unchanged | **YES** |
| 15 | PRIMARY decomposition 42.88% / 48.69% unchanged | **YES** — including "48.69 − 42.88 = 5.81 percentage points" |
| 16 | C1↔C3 = 0.00% remains entailed conformance | **YES** |
| 17 | Sourced-threshold envelopes unchanged | **YES** — 5.67–9.56% and 4.26–6.64%, still labelled deterministic configuration ranges |
| 18 | Wave perturbation result unchanged | **YES** — ±0.25 m, 2.54–14.75%, ≈ −1.4 pp per 0.05 m, still non-causal |
| 19 | Component epistemic statuses unchanged | **YES** — *g*<sub>w</sub> empirical negative, *g*<sub>t</sub> definitional, *g*<sub>m</sub> structurally excluded; the two wind zeros still separated |
| 20 | No new citation introduced | **YES** |
| 21 | No new result introduced | **YES** |
| 22 | No new experiment introduced | **YES** |
| 23 | No safety / effectiveness / generalisation claim introduced | **YES** — see note below on the replacement's semantics |
| 24 | Section V prose word count | **888** — see the counting note below |
| 25 | FIGURE DATA EXTRACTION REQUIRED carried forward | **YES** |
| 26 | MFWAM citation-resolution task carried forward | **YES** |
| 27 | Number of substantive manuscript-body changes | **1** |
| 28 | Any unintended substantive change | **NONE** |

### Strict diff result

`diff` between `aai-2026-manuscript-v1-phase3.md` and `aai-2026-manuscript-v1-phase3-revised.md` reports exactly one changed line (line 50) and nothing else. Every other byte of the manuscript body, TABLE III, the figure placeholder and the Phase 3 Drafting Audit is identical. No revert was necessary because no other difference arose.

### Note on item 24 — counting basis

The replacement is word-neutral: the old sentence and the new sentence are both 28 words, verified by token count before writing. The revision therefore did not change the length of Section V at all.

The figure reported here is nevertheless **888**, not the **899** recorded in the Phase 3 Drafting Audit. That is a difference in counting basis, not in text. The count above uses an explicit rule: narrative paragraph text only, with the section headings, TABLE III and its caption, the table note, and the FIGURE 1 label and caption all excluded, and symbol-only tokens (`=`, `−`) not counted as words. Under that rule Section V is 888 words; counting the symbol-only tokens as well gives 893; counting the 39-word table note as prose would give 927. The Phase 3 figure of 899 could not be reproduced from the file under any of these rules, so it is recorded here as superseded rather than confirmed. The Phase 3 Drafting Audit above has been left exactly as written, since it is the Phase 3 record.

All three readings sit below the 930 hard ceiling, and no sentence was edited to adjust the count.

### Note on item 23 — semantics of the replacement

The new predicate is "measurably changes the admissible recommendation set". Its object is A<sub>AI</sub>(*S*), which is what the census actually observes. The sentence asserts only that the admissible set differs under the intermediate level, at a frequency the same sentence immediately makes conditional on threshold, vessel-class and denominator choices. It does not assert that the change is correct, beneficial, safety-relevant, or that anyone acted differently as a result, and the locked paragraph that follows denies each of those explicitly.

### Final logical check

**A.** Yes. The conclusion now names the measured object — change in the admissible recommendation set — rather than an unscoped "operational effect".
**B.** No. The predicate is confined to the admissible set; it makes no claim about safety, decision quality, human performance or downstream benefit, and the immediately following locked paragraph rules each of these out by name.
**C.** Yes. Every numerical finding is byte-identical to the approved Phase 3 draft, confirmed by diff.
**D.** Yes. Figure 1 remains a labelled placeholder with the extraction task carried forward; no coordinates were generated, interpolated or invented.
**E.** Yes. MFWAM remains an open citation-resolution task; no bibliographic record was created or substituted.

---

PHASE 3 REVISION STATUS: READY FOR PHASE 4
