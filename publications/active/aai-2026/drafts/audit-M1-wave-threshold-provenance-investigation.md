# Audit Investigation — M-1: Wave UNSAFE Threshold Provenance

**Scope:** Finding M-1 only.
**Manuscript:** `publications/active/aai-2026/drafts/aai-2026-manuscript-v6-rewrite-v2.docx`
**Investigation date:** 8 October 2026
**Mode:** read-only. Nothing modified. No experiment re-run. The original publication was read directly from the repository copy.

---

## A. Executive Finding

**Overall classification: PARTIALLY CONFIRMED — and the auditor's central premise is wrong.**

The investigation reached the original publication, `papers/sources/STABILITY, SEAKEEPING AND SAFETY ASSESSMENT OF SMALL FISHING BOATS OPERATING IN SOUTHERN COAST OF PENINSULAR MALAYSIA.pdf`, and read its tables directly. The paper **does** publish metre-valued significant wave heights. Its own **Table 4 (WMO Sea State Code)** gives Sea State 3 as a range of **0.5 – 1.25 m** and Sea State 4 as **1.25 – 2.5 m**; its **Table 5** records the tested conditions at Hs = 0.550 / 0.875 / 1.875 m. Its **Table 8** quantifies Boat A's failure at Sea State 4 — *RMS Vertical Acceleration at FP 0.332 g against a NORDFORSK limit of 0.275 g, Bridge 0.195 g against 0.150 g, both marked "Fail"*.

**The auditor's claim that the metre values are a researcher-invented conversion is not supported.** The 1.25 m and 1.875 m figures are the source's own numbers. Two of the auditor's four sub-claims fall; two survive, in narrowed form.

**What does survive, and matters:**

1. **The selection rule is undisclosed in the manuscript.** 1.25 m is the **upper limit of the band the hull passes**, not a number the paper nominates as a limit. The paper's recommendation is categorical — *"Boat A should only operate in sea states up to sea state condition 3"* — and converting that to 1.25 m by taking the top of the band is a research-team step. It is **fully documented in the repository** (`scripts/threshold_comparison.py:37` labels it *"NORDFORSK, top of Sea State 3"*) but appears nowhere in the manuscript.
2. **"reported by [17]" overstates.** The repository is explicit that *"Yaakob et al. do not themselves characterise either value as a departure prohibition"* (`docs/canonical/appendix-c-formalisation.md`, C.9 design-decision block) and that *"reading the ceiling as a departure prohibition is our interpretation"* (`docs/canonical/paper-review-synopsis.md:182`). The manuscript's "follows the operational ceiling reported by [17]" asserts more than the source does, and less than the project's own records concede.

**Submission risk: LOW. The defect is a reporting omission, not an experimental one.** Every threshold is correctly implemented, the provenance chain is intact and better documented internally than in any paper I have audited, and no number changes. The manuscript is *less careful than the research record it rests on* — which is unusual, and easily fixed.

**A correction I owe to my own earlier audit.** In the pre-submission audit I wrote that [17] "does not quantify a failure point" and gave Boat A's ceiling as 0.875 m. Both statements were wrong, and I had not read the paper. 0.875 m is the **mean** of the SS3 band and the Hs at which SS3 was *tested*; the band's ceiling is 1.25 m. The failure at 1.875 m is quantified in Table 8. The present report supersedes those statements.

---

## B. Evidence Inventory

| Path | Location | Evidence | Strength |
|---|---|---|---|
| `papers/sources/STABILITY, SEAKEEPING…pdf` | Table 4, p.56 | WMO Sea State Code with **significant wave height ranges in metres**: SS2 0.1–0.5 (mean 0.3); **SS3 0.5–1.25 (mean 0.875)**; **SS4 1.25–2.5 (mean 1.875)** | **Direct — original publication** |
| same | Table 5, p.56 | Tested sea states (after N. Ahmad, 2008): SS2 Hs 0.550 m / 6.5 s; **SS3 Hs 0.875 m / 7.5 s**; **SS4 Hs 1.875 m / 8.8 s** | **Direct — original publication** |
| same | Table 8, p.57 | Boat A at SS4 (JONSWAP 8.8 s, 1.875 m): RMS vert. accel. FP **0.332** vs limit **0.275** → **Fail**; Bridge **0.195** vs **0.150** → **Fail**; lateral 0.031 vs 0.070 Pass; Roll 3.94° vs 4.0° Pass | **Direct — original publication** |
| same | narrative, p.56 | *"if Boat A operates in sea state condition 4, it may encounter loss in operability and survivability with risk to capsizing. Therefore, for the interests of comfort, operability and safety, Boat A should only operate in sea states up to sea state condition 3."* | **Direct — verbatim quotation** |
| same | narrative, p.57 | *"Unlike Boat A, Boat B only passed the limiting criteria for sea state condition 2, and unfortunately failed to meet certain limiting criteria in sea state condition 3 and 4."* | **Direct — verbatim quotation** |
| same | Abstract | *"allowed operating in restricted operational area with maximum sea state 2, while the other can be allowed to operate in operational area up to sea state 3"* | **Direct — verbatim quotation** |
| same | Methods, p.55 | Seakeeping criteria: NORDFORSK 1987 (Ormala, 1989), heavy-manual-work category; Maxsurf Seakeeper; JONSWAP spectrum; 9 kn | **Direct — original publication** |
| `scripts/condition_comparison.py` | line 76 | `LO, HI = 1.0, 1.25` — the canonical small-vessel wave thresholds | **Direct — code** |
| `scripts/condition_comparison.py` | (classifier) | `g_o = np.where(d["wave"] > HI, UNSAFE, np.where(d["wave"] >= LO, CAUTION, SAFE))` | **Direct — code** |
| `scripts/sensitivity/threshold_sensitivity.py` | line 19 | `CANON = dict(W_C=21.6, W_U=27.0, R_C=10.0, R_U=20.0, O_C=1.0, O_U=1.25)` | **Direct — code** |
| `scripts/sensitivity/threshold_sensitivity.py` | line 37 | `g_o = np.where(d["wave"] > p["O_U"], UNSAFE, np.where(d["wave"] >= p["O_C"], CAUTION, SAFE))` — **UNSAFE strict, CAUTION inclusive** | **Direct — code** |
| `scripts/sensitivity/threshold_sensitivity.py` | lines 113–115 | The six wave settings swept, including `(1.0, 1.9, "Yaakob failure point as O_U")` — **only `O_C`/`O_U` vary; all other CANON parameters held** | **Direct — code** |
| **`scripts/threshold_comparison.py`** | **line 37** | **`("Yaakob Boat A — operational ceiling", 1.25, "NORDFORSK, top of Sea State 3")` — the conversion rule, stated in code** | **Direct — the decisive provenance artefact** |
| `scripts/threshold_comparison.py` | line 38 | `("Yaakob Boat A (6.54 m) — fails SS4", 1.875, "NORDFORSK seakeeping failure")` | **Direct — code** |
| `scripts/threshold_comparison.py` | line 36 | `("Current model — small UNSAFE", 1.90, "This architecture (SS4 = 1.875 m, rounded)")` — **1.90 is 1.875 rounded, and the rounding is declared** | **Direct — code** |
| `scripts/threshold_comparison.py` | lines 40–41 | Boat B: `fails SS3 → 0.875`; `operational ceiling → 0.50 ("NORDFORSK, top of Sea State 2")` — the same rule applied consistently to the second hull | **Direct — code** |
| `scripts/historical_replay.py` / `hysteresis_analysis.py` / `canonical_figures.py` / `compare_v1_v2.py` / `diagnostic_binding.py` / `sensitivity/gt_counterfactual.py` | lines 58 / 61 / 93 / 21 / 54 / 25 | All carry `small = (1.0, 1.25)` — **one value, consistent across every canonical script** | **Direct — code** |
| `notes/Stability, Seakeeping…md` | lines 63–75 | The research team's transcription of the paper's Tables 4 and 5 — matches the PDF exactly | **Direct — corroborates the extraction** |
| `notes/Stability, Seakeeping…md` | line 128 | *"reading NORDFORSK operability failure as an UNSAFE trigger is an interpretation. This paper reports that the crew cannot safely perform heavy manual work at that sea state; it does not characterise this as a departure prohibition."* | **Direct — the team's own caveat** |
| `docs/canonical/appendix-c-formalisation.md` | line 607 | *"The 1.25 m CAUTION/UNSAFE boundary is Yaakob et al.'s (2015) operational ceiling for their 6.54 m Malaysian vessel — the top of Sea State 3, the highest band the hull passes under NORDFORSK 1987 criteria."* | **Direct — canonical record** |
| `docs/canonical/appendix-c-formalisation.md` | C.9 design-decision block | *"Yaakob et al. do not themselves characterise either value as a departure prohibition… The true limit lies between the last passing test (0.875 m) and the first failing test (1.875 m); 1.25 m is the highest value the evidence supports as safe. Recorded as a threat to internal validity in C.9."* | **Direct — canonical record** |
| `docs/canonical/appendix-c-formalisation.md` | line 1041 | *"treating the operational ceiling as the gate is an interpretation, though a conservative one"* | **Direct — canonical record** |
| `docs/canonical/appendix-c-formalisation.md` | line 601 | Records the 2026-09-06 amendment from 1.9 m to 1.25 m, adopted the same day | **Direct — decision record** |
| `docs/canonical/paper-review-synopsis.md` | line 182 | *"the operational ceiling and the failure point are distinct quantities… reading the ceiling as a departure prohibition is our interpretation, since the paper characterises SS4 as the sea state at which heavy manual work cannot be safely performed, not as a departure rule"* | **Direct — canonical record** |
| `docs/canonical/report-c7-closure-2026-09-08.md` | line 69 | *"1.9 → 1.25 m — superseded, not erroneous"* | **Direct — change record** |
| `docs/analysis/threshold-sensitivity-analysis.md` | lines 109–115 | The sensitivity table: (1.00, 1.25) → 5.81% / 4.48%; **(1.00, 1.90) → 9.22% / 6.08%** | **Analysis document — the only surviving record of 9.22%** |
| `docs/analysis/threshold-sensitivity-analysis.md` | lines 3–20 | Dated 2026-09-21; baseline reproduces 5.81% / 4.48% / 9,135 / 5,935 exactly | **Analysis document** |
| `data/c8/canonical-results-post-migration.txt` | lines 215–226 | PRIMARY departure window n = 9,135; SAFE 4,687 / **CAUTION 531** / UNSAFE 3,917; C1↔C2 = **5.81%** | **Direct — stored execution output** |
| `scripts/sensitivity/threshold_sensitivity.py` | line 150 | `Path("/tmp/sens_out.txt").write_text(...)` — **the sensitivity run writes to a temp path; no copy is retained in the repository** (verified absent) | **Direct — gap in the artefact trail** |
| `git log -- docs/analysis/threshold-sensitivity-analysis.md` | commit `3c70a1d` | Committed 2026-09-22 09:35:46 +0800 | **Direct — version control** |

---

## C. Implemented Thresholds

| Question | Answer | Location |
|---|---|---|
| Small-vessel wave CAUTION threshold (`O_C` / `LO`) | **1.0 m** | `condition_comparison.py:76`; `threshold_sensitivity.py:19`; and five other canonical scripts |
| Small-vessel wave UNSAFE threshold (`O_U` / `HI`) | **1.25 m** | same |
| Alternative producing 9.22% | **`O_U` = 1.90 m**, `O_C` held at 1.00 | `threshold_sensitivity.py:114`; `threshold-sensitivity-analysis.md:114` |
| Comparison operators | **UNSAFE iff `wave > O_U` (strict); CAUTION iff `O_C <= wave <= O_U` (inclusive both ends); SAFE otherwise.** An hour at exactly 1.25 m is CAUTION, not UNSAFE. | `threshold_sensitivity.py:37`; `condition_comparison.py` `classify()` |
| Wave variable | `wave_height` from the Open-Meteo marine API = **significant wave height (Hs)** | `docs/canonical/data-provenance.md:99` — *"`wave_height` = significant wave height (Hs) — semantically correct for thresholds derived from Yaakob and Jeong & Im"* |
| Units | metres | CSV column `wave_height (m)` |
| Overlapping conditions | Not applicable within `g_o` — the three intervals **partition ℝ≥0 exhaustively with no overlap** for each fixed vessel class (`appendix-c-formalisation.md`, `g_o` domain note). Across components, resolution is by **maximum severity**. | `condition_comparison.py` `classify()` |
| Vessel-dependent? | **Yes.** `TH = {"small": (1.0, 1.25), "medium": (1.4, 2.8), "big": (1.5, 3.5)}` | `canonical_figures.py:93`; `compare_v1_v2.py:21`; `diagnostic_binding.py:54`; `historical_replay.py:58` |

**Statistic compatibility.** The source's thresholds are expressed in significant wave height (Table 4 column header: *"Significant Wave Height (m)"*; Table 5: *"Significant wave height (m)"*). The experimental variable is also Hs. **The statistics match.** There is no significant-vs-individual wave-height confusion.

---

## D. Original Source Verification

### What [17] establishes

1. **A WMO sea-state code table in metres (Table 4).** SS3 = 0.5–1.25 m (mean 0.875); SS4 = 1.25–2.5 m (mean 1.875). This is the paper's own table, reproduced in its own text.
2. **Metre-valued test conditions (Table 5).** Seakeeping was evaluated at Hs = 0.550, 0.875 and 1.875 m, with periods 6.5, 7.5 and 8.8 s.
3. **A quantified failure for Boat A at SS4 (Table 8).** RMS vertical acceleration at FP **0.332 g** against the NORDFORSK 1987 limit of **0.275 g**, and at the bridge **0.195 g** against **0.150 g**; both "Fail". Lateral acceleration and roll pass.
4. **A categorical operating recommendation.** *"Boat A should only operate in sea states up to sea state condition 3."* For Boat B: passes only SS2, fails SS3 and SS4.
5. **A qualitative capsize statement.** At SS4, Boat A *"may encounter loss in operability and survivability with risk to capsizing"*.
6. **That dynamic seakeeping, not static stability, is binding** — both hulls pass IMO static criteria.

### What [17] does **not** establish

1. **It does not nominate 1.25 m as a limit.** The recommendation is a sea-state *code*. 1.25 m is the top of the band that code names, taken from the paper's Table 4.
2. **It does not use the phrase "operational ceiling".** That is the project's label.
3. **It does not give a continuous failure threshold.** Only three sea states were tested. The true boundary lies somewhere in **(0.875 m, 1.875 m]** — the interval between Boat A's last pass and its first fail. The paper does not locate it.
4. **It does not characterise any value as a departure prohibition.** It frames SS4 as the condition in which heavy manual work cannot be safely performed and operability and survivability are lost.
5. **It does not report a measured capsize point.** "Risk to capsizing" is a qualitative inference from the acceleration results.
6. **Sample size is two vessels**, both from the Johor coast — not the deployment site.

**External verification status:** performed directly against the repository's PDF copy of the publication (Adobe InDesign CS4, created 2015-05-25). Bibliographic fields were independently confirmed against the publisher's open copy in the earlier reference audit. No outstanding external verification.

---

## E. Threshold Derivation

### E.1 The chain, step by step

| Step | Content | Classification |
|---|---|---|
| **Original source** | Boat A (6.54 m LOA, < 10 GRT) passes NORDFORSK 1987 at SS2 and SS3; fails at SS4 (FP 0.332 g vs 0.275 g). *"Boat A should only operate in sea states up to sea state condition 3."* | **SOURCE-DEFINED** |
| **Sea-state → metre mapping** | SS3 = 0.5–1.25 m; SS4 = 1.25–2.5 m — **the paper's own Table 4**, itself the WMO sea-state code | **SOURCE-DEFINED** *(and STANDARD-DEFINED — the WMO code)* |
| **Tested Hs values** | SS3 = 0.875 m; SS4 = 1.875 m — the paper's Table 5 | **SOURCE-DEFINED** |
| **Interpretation: "operational ceiling" = top of the highest passing band** | 1.25 m, under the documented rule *"NORDFORSK, top of Sea State 3"* (`threshold_comparison.py:37`). Applied consistently: Boat B's ceiling = top of SS2 = 0.50 m (line 41) | **SOURCE-DERIVED** *(documented rule, applied consistently)* |
| **Interpretation: "failure point" = the tested Hs at which the hull first fails** | 1.875 m (`threshold_comparison.py:38`) | **SOURCE-DERIVED** *(the value itself is SOURCE-DEFINED; its designation as a threshold is the derivation)* |
| **Rounding for implementation** | 1.875 → **1.90 m**, declared as *"SS4 = 1.875 m, rounded"* (`threshold_comparison.py:36`) | **RESEARCHER-DEFINED** |
| **Treating either value as a departure gate** | Not a claim the source makes. Recorded as an interpretation in `appendix-c-formalisation.md` C.9, `notes/…:128`, `paper-review-synopsis.md:182` | **RESEARCHER-DEFINED** |
| **Choosing the ceiling over the failure point as canonical** | Amended 1.9 → 1.25 m on 2026-09-06, rationale: *"a departure gate should sit at the edge of the demonstrated-safe envelope, not at the point of demonstrated failure"* | **RESEARCHER-DEFINED** *(documented design decision)* |
| **Implemented threshold** | `O_U = 1.25`, `O_C = 1.00` | — |
| **Experimental result** | Δ<sub>L2</sub> = 5.81% PRIMARY / 4.48% RESOLUTION | — |

The CAUTION onset `O_C` = 1.00 m comes from a **different source** — Jeong & Im's Table 12 restriction for vessels ≤ 10 m LOA (reference [16]) — and is **SOURCE-DEFINED**. It is corroborated by, not derived from, [17].

### E.2 Alternative defensible conversions

The documented rule is not the only defensible one. Four candidates, none preferred here:

| Reading | Value | Defensibility |
|---|---|---|
| Top of the highest passing band (SS3) | **1.25 m** | The implemented canonical. Conservative; the highest value the evidence demonstrates as safe. |
| Mean of the highest passing band | 0.875 m | The Hs actually *tested* and passed. The most conservative; arguably the only directly demonstrated safe value. |
| Mean of the first failing band (SS4) | 1.875 m | The Hs actually *tested* and failed. The implemented alternative (rounded to 1.90). |
| Bottom of the first failing band | 1.25 m | Identical to the first, since the SS3/SS4 boundary is shared. |

The first and fourth coincide, which is a point in the canonical choice's favour: **1.25 m is simultaneously the top of the last passing band and the bottom of the first failing band.** The interval the source leaves genuinely unresolved is (0.875, 1.875].

### E.3 Distinctions checked

- **Significant vs individual wave height** — no confusion. Both source and experiment use Hs.
- **Operational restriction vs structural failure** — the project separates these explicitly and consistently, in code (two labelled entries), in the canonical record and in the sensitivity analysis. This is the distinction the manuscript compresses.
- **Sea-state band boundaries vs vessel-specific limits** — the vessel-specific result is a *band*; the metre value is a band boundary. The project is aware of this (`appendix-c`: *"the true limit lies between…"*). The manuscript is not.
- **Published operating recommendation vs researcher-defined safety gate** — the source recommends; the project gates. Documented internally, absent from the manuscript.

---

## F. Sensitivity Result Traceability

### F.1 What changed between the two runs

From `threshold_sensitivity.py:113–115`, the wave sweep varies **only** `O_C` and `O_U`, with every other parameter held at `CANON` (`W_C=21.6, W_U=27.0, R_C=10.0, R_U=20.0`), the same data configuration, the same denominator and the same classifier:

| Setting | `O_C` | `O_U` | Δ<sub>L2</sub> PRIMARY | Δ<sub>L2</sub> RESOLUTION |
|---|---|---|---|---|
| Canonical | 1.00 | **1.25** | **5.81%** | **4.48%** |
| Alternative reading | 1.00 | **1.90** | **9.22%** | **6.08%** |

`O_C` is identical in both. **The 5.81 → 9.22 movement is attributable to `O_U` alone.**

### F.2 Traceability status — not equal for the two figures

| Figure | Status |
|---|---|
| **5.81% / 4.48%** | **Traceable to a stored execution artefact.** `data/c8/canonical-results-post-migration.txt` lines 215–226 and 249–260 carry n = 9,135, CAUTION 531, C1↔C2 = 5.81%; and n = 5,935, CAUTION 266, C1↔C2 = 4.48%. |
| **9.22% / 6.08%** | **Traceable only to an analysis document.** `docs/analysis/threshold-sensitivity-analysis.md:114` (dated 2026-09-21, committed 2026-09-22). `threshold_sensitivity.py:150` writes its output to `/tmp/sens_out.txt`, which is not retained; the file is absent. **No machine-generated artefact for 9.22% survives in the repository.** |

This is a genuine gap in the artefact trail, though a mild one: the document states the baseline reproduced 5.81% / 4.48% / 9,135 / 5,935 exactly in the same run, which is a strong consistency signal.

### F.3 Mechanism

`g_o` assigns UNSAFE when `wave > O_U`. Raising `O_U` from 1.25 to 1.90 moves every hour with **1.25 < Hs ≤ 1.90** from `g_o` = UNSAFE to `g_o` = CAUTION. Under max-severity aggregation, such an hour becomes CAUTION overall **only if no other component is UNSAFE**; hours already UNSAFE for another reason (chiefly the night→UNSAFE time rule) stay UNSAFE. CAUTION occupancy therefore rises, and since Δ<sub>L2</sub> ≡ P(S = CAUTION), so does Δ<sub>L2</sub>.

**Quantified from the data files** (count inspection only — no classifier was run):

| | PRIMARY | RESOLUTION |
|---|---|---|
| Departure-window hours | 9,135 | 5,935 |
| Max observed Hs in window | 2.06 m | 1.80 m |
| Hours with 1.25 < Hs ≤ 1.875 | **511** | **164** |
| Hours with 1.875 < Hs ≤ 1.90 | **10** | **0** |
| Hours with Hs > 1.90 | 3 | 0 |

Δ<sub>L2</sub> rises by 9.22 − 5.81 = 3.41 pp = **312 hours** of the ~521 that `g_o` reclassifies. The remaining ~209 stay UNSAFE because another component already was. The mechanism is coherent and the magnitudes are consistent.

### F.4 Effect of the 1.875 → 1.90 rounding

The source's value is 1.875 m; the run used 1.90 m. The difference affects **10 departure hours in PRIMARY (0.11%) and 0 in RESOLUTION**. Running the alternative at the source's own 1.875 m would therefore give essentially the same figure — the sensitivity document's observation that the gradient saturates above ~1.9 m is confirmed by the data. **The rounding is immaterial to the result**, but the manuscript currently implies the alternative *is* the source value, and it is the source value rounded.

---

## G. Assessment of Auditor M-1

| Claim | Verdict | Evidence and reasoning |
|---|---|---|
| **A.** [17] reports WMO sea-state categories rather than metre-valued wave thresholds | **PARTIALLY CONFIRMED — mostly NOT SUPPORTED** | The *operating recommendation* is categorical (*"up to sea state condition 3"*). But the paper publishes the metre mapping itself in Table 4 (SS3 = 0.5–1.25 m, SS4 = 1.25–2.5 m) and tests at metre-valued Hs in Table 5. The metres are the source's, not the researchers'. What is the researchers' is the **choice of which point in the band** to use. |
| **B.** The implemented thresholds were obtained through an undisclosed conversion | **PARTIALLY CONFIRMED** | **Confirmed against the manuscript** — the rule appears nowhere in it. **Not supported against the research record** — `threshold_comparison.py:37` states it in code (*"NORDFORSK, top of Sea State 3"*), `appendix-c-formalisation.md:607` states it in prose, and both Boat A and Boat B are converted by the same rule. The conversion is documented; it is simply not in the paper. |
| **C.** [17] does not establish a quantitative vessel-failure point | **NOT SUPPORTED** | Table 8 quantifies it: Boat A fails at the tested Hs = **1.875 m**, FP acceleration 0.332 g against a 0.275 g limit, bridge 0.195 g against 0.150 g. What the source does not give is a *continuous* threshold — only three sea states were tested, and the true boundary lies in (0.875, 1.875]. The auditor's claim overstates the gap. |
| **D.** The manuscript describes a researcher-derived threshold as a source-reported operational ceiling | **CONFIRMED** | "the UNSAFE boundary follows the operational ceiling reported by [17]" — the paper does not use the term, does not nominate 1.25 m, and does not frame any value as a departure prohibition. The project's own records say so plainly: *"reading the ceiling as a departure prohibition is our interpretation"* (`paper-review-synopsis.md:182`). The manuscript is less careful than the record behind it. |
| **E.** The 5.81% vs 9.22% comparison remains scientifically meaningful after clarification | **CONFIRMED** | Both endpoints correspond to real, distinct findings in the source — the highest band the hull passes, and the band at which it demonstrably fails. Only `O_U` changed between runs; everything else was held. The comparison is a legitimate and informative sensitivity scenario, and the manuscript is right to present neither as correct. |

---

## H. Scientific Validity Assessment

**1. Does this invalidate the deterministic classifier?**
**No.** `g_o` is a total, non-overlapping partition of ℝ≥0 for each vessel class, implemented identically across seven canonical scripts, with explicit and consistent comparison operators. Nothing in M-1 touches its construction.

**2. Does it invalidate the reported experimental counts?**
**No.** 5.81% / 4.48% and the underlying counts (CAUTION 531 / 266) are traceable to a stored execution artefact and are internally consistent. A threshold's *justification* is not its *implementation*.

**3. Does it weaken the justification for the baseline threshold?**
**Marginally, and in a direction the project already anticipated.** 1.25 m is not a number the source nominates — but it is a boundary in the source's own table, it is simultaneously the top of the last passing band and the bottom of the first failing band, and the same rule applied to Boat B gives 0.50 m, which the project also records. The justification is *inferential*, not arbitrary, and the inference is conservative. The honest description is **source-derived under a documented rule**, which is a weaker claim than the manuscript makes and a stronger one than the auditor allows.

**4. Is the alternative threshold a legitimate sensitivity scenario?**
**Yes.** 1.875 m is a tested, failed, quantified condition in the source. Using it as `O_U` asks a real question: what if the gate sits at demonstrated failure rather than at the edge of the demonstrated-safe envelope? That is exactly the kind of question a sensitivity analysis should ask. The only blemish is the undeclared rounding to 1.90, which moves 10 hours.

**5. Does the manuscript overstate the authority of [17]?**
**Yes, in one phrase.** "the operational ceiling reported by [17]" implies a reported value. Everything else in §IV — *"Source provenance indicates where a boundary comes from; it does not establish that it is optimal"* — is well judged, and the sensitivity section's *"neither is selected here as correct"* is exactly right.

**6. Resolvable by clarification, or does it need new experiments?**
**Clarification alone.** The evidence is complete: the source has been read, the conversion rule is in the code, both readings have been run, and the gradient between them is characterised. Nothing is missing that an experiment would supply. Re-running the alternative at 1.875 m instead of 1.90 m would change PRIMARY by at most ~0.11 pp and RESOLUTION by nothing — not worth a page-limited paper's space, and not required for correctness.

**7. Should "operational ceiling" and "failure point" be retained?**
**Retain both, with one qualifying clause.** They are the right terms — they name a distinction the source genuinely supports and that the project has maintained consistently for over a month. What is needed is one clause making clear they are the research team's reading of the source's sea-state findings, not labels the source applies. Replacing them would lose a real distinction and would misdescribe the sensitivity analysis.

**Real-world safety note.** Neither value is a validated safety threshold, and the manuscript should not be read as proposing one. The source's own recommendation concerns *comfort, operability and the ability to perform heavy manual work* — not a departure prohibition. The manuscript's existing limitations section already says the thresholds are not validated; nothing in M-1 requires strengthening that, and nothing here should be used to argue that 1.25 m is an established safe-departure limit for any vessel.

---

## I. Recommended Manuscript Action

### I.1 Threshold provenance sentence (§IV)

**Exact original:**

> "For the small-vessel class, the ocean-state CAUTION onset follows the departure restriction proposed for vessels under 10 m by [16] and the UNSAFE boundary follows the operational ceiling reported by [17]."

**Minimal replacement:**

> "For the small-vessel class, the ocean-state CAUTION onset follows the departure restriction proposed for vessels under 10 m by [16]. The UNSAFE boundary is taken as the upper limit of the highest sea state the 6.54 m hull of [17] passes under NORDFORSK 1987 criteria — Sea State 3, which that paper's own table gives as 0.5–1.25 m. Reading that limit as a departure boundary is an evaluation choice, not a recommendation made by [17]."

**Justification.** Three things are fixed in one sentence and a clause. The conversion rule is stated, so a reviewer can reconstruct 1.25 m. The metre range is attributed to the source's own table, which is where it comes from. And the interpretive step is declared — bringing the manuscript into line with `appendix-c-formalisation.md` C.9 and `paper-review-synopsis.md:182`, which have said this all along. Cost: about 25 words.

### I.2 Sensitivity sentence (§V-B)

**Exact original:**

> "The small-vessel wave source supports two defensible readings of the UNSAFE boundary, an operational ceiling and a failure point, which give 5.81% and 9.22% respectively. Both are traceable to the same source [17], and neither is selected here as correct."

**Minimal replacement:**

> "The small-vessel wave source supports two defensible readings of the UNSAFE boundary — the top of the highest sea state the hull passes (1.25 m) and the sea state at which it fails the seakeeping criteria (1.875 m) — which give 5.81% and 9.22% respectively. Both derive from the same source [17], and neither is selected here as correct."

**Justification.** Naming the two metre values makes the sensitivity reconstructible and shows the reader the size of the perturbation driving the paper's largest movement. "derive from" replaces "are traceable to", which is the accurate relation. Cost: about 15 words. (The 9.22% run used 1.90 m, the rounded value; the difference is 10 departure hours in PRIMARY and none in RESOLUTION, so quoting 1.875 m is faithful. If the authors prefer exactness over brevity, "(1.875 m, implemented as 1.90 m)" is three words more.)

### I.3 Citation placement

[16] stays on the CAUTION onset — it is the source of that value and the attribution is correct. [17] stays on the UNSAFE boundary, now cited for the sea-state finding it actually reports rather than for a metre value it does not nominate.

### I.4 Does [17] remain relevant?

**Yes, and it remains the right citation.** It is the only source in the corpus assessing actual Malaysian small fishing hulls by naval-architecture methods, it supplies the vessel-conditional structure of `g_o`, and it supplies both endpoints of the paper's principal sensitivity. Nothing about M-1 argues for replacing or demoting it.

### I.5 Additional reference support

**Not required.** The WMO sea-state code is reproduced in [17]'s own Table 4, so no separate WMO citation is needed; NORDFORSK 1987 is cited within [17] and the manuscript does not need to cite it independently at this level of detail. Adding either would cost a reference slot for no gain in a six-page paper.

### I.6 Numerical changes

**None.** No threshold, count, percentage or envelope changes. 5.81%, 9.22%, 4.48%, 6.08%, the 5.67–9.56% envelope and every count stand exactly as reported.

---

## J. Unresolved Questions

1. **No machine artefact survives for 9.22%.** `threshold_sensitivity.py:150` writes to `/tmp/sens_out.txt`, which is not in the repository and no longer exists on the device. The figure rests on `threshold-sensitivity-analysis.md` alone. The document records that the same run reproduced the baseline exactly, which is reassuring but is not a captured log. *Suggested for the record, not for this manuscript: have the script write beside the analysis document rather than to `/tmp`.*

2. **Where in (0.875, 1.875] the true limit lies is not resolved, and cannot be from this source.** Only three sea states were tested. `appendix-c-formalisation.md:1041` states this plainly. It is a limitation of the evidence, not a defect of the paper, and the manuscript's sensitivity treatment is the right response to it.

3. **Whether "top of the passing band" or "mean of the passing band" is the better operationalisation.** 1.25 m and 0.875 m are both defensible; the project chose 1.25 m with a recorded rationale. No external authority settles it. The choice is disclosed in the repository and would be disclosed in the manuscript under the replacement text above.

4. **Two vessels, one coast.** [17]'s sample is two Johor-coast hulls; the deployment site is Kota Kinabalu. The manuscript's limitations section already confines its claims to the evaluated site, so no action follows — noted because it bounds how far the threshold's authority extends.

---

## K. Final Verdict

> ## MINOR CLARIFICATION REQUIRED

One sentence in §IV, one in §V-B, about 40 words in total. No numerical result, threshold, count or reference changes.

The experiment is sound and the provenance chain is complete — it is simply recorded in the repository rather than in the paper. The project's own canonical documents have, since 6 September 2026, stated the conversion rule, named the interpretive step and flagged it as a threat to internal validity. The manuscript needs to say what its own records already say.

**Two of the four auditor sub-claims (A on metre values, C on the failure point) are not supported and should be withdrawn.** The two that stand (B as to the manuscript, D) are reporting omissions, not experimental defects, and both are fixed by the text above.
