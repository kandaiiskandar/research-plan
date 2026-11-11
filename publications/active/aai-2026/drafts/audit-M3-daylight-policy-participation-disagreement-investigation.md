# Audit Investigation — M-3: Daylight Policy and Participation-Only Disagreement

**Scope:** Finding M-3 only.
**Manuscript:** `publications/active/aai-2026/drafts/aai-2026-manuscript-v6-rewrite-v2.docx`
**Investigation date:** 8 October 2026
**Mode:** read-only. The manuscript, scripts, datasets and reports were not modified, and no canonical experiment was re-run. Two **new diagnostic calculations** were performed from existing data to establish the attribution breakdown; they are labelled as such throughout and were validated by reproducing the stored canonical counts exactly.

---

## A. Executive Finding

**Verdict: CONFIRMED — and the effect is larger than the auditor estimated.**

The daylight policy does not merely influence the participation-only disagreement rate; it **is** that rate, almost entirely.

| Departure window | C0↔C1 as reported | C0↔C1 with the time rule removed |
|---|---|---|
| **PRIMARY** | **42.88%** | **5.78%** |
| **RESOLUTION** | **41.08%** | **2.80%** |

Of the 3,917 UNSAFE hours behind PRIMARY's 42.88%, **3,389 (86.52%) are night hours with no environmental trigger whatsoever** — no wind, no rainfall, no wave, no storm code. A further 210 (5.36%) are night hours that also carry an environmental UNSAFE trigger, and only **318 (8.12%)** are daylight hours made UNSAFE by conditions. RESOLUTION is starker: **93.19% night-only**, 3.98% environmental-only.

**But three things keep this from being a correction rather than a clarification.**

1. **The arithmetic is right.** D(C0,C1) = P(S = UNSAFE) was verified from the mappings, and my diagnostic reproduced the canonical state distributions to the hour — 4,687 / 531 / 3,917 = 9,135 and 3,231 / 266 / 2,438 = 5,935. Nothing is miscounted.
2. **The policy is already declared.** §IV states: *"Researcher-defined choices are the three-state cardinality, A_AI(CAUTION), **the policy treating non-daylight hours as UNSAFE**, the evaluation window, and the declared exclusion described next."* The manuscript does not pretend the rule is externally mandated.
3. **No sentence claims 42.88% is weather-driven.** It is consistently described as *"the frequency associated with participation gating alone"*, which is literally accurate. I searched the abstract, introduction, method, results, discussion, limitations and conclusion and found **no overclaim of the kind M-3 anticipates**.

**The defect is an absent disclosure, not a false statement.** A reader meeting "42.88%" in Table II, between a list of environmental thresholds and an envelope of sourced threshold settings, will read it as environmental severity. Nothing in the paper prevents that reading, and a reviewer who checks will find the 86.5% figure unaided.

**One finding that runs the other way, and that the paper should have.** The time rule does not inflate Δ<sub>L2</sub> — it **suppresses** it. Removing g_t moves Δ<sub>L2</sub> from 5.81% to **9.73%** (PRIMARY) and 4.48% to **7.58%** (RESOLUTION), because 358 and 184 CAUTION hours are currently absorbed into UNSAFE by the night rule. The headline figure is **conservative** with respect to the project's most-criticised policy choice. That is a defensive result, and it is not reported anywhere.

**Submission risk: MODERATE — the highest of the three findings investigated so far.** Not because anything is wrong, but because this is the one a reviewer can compute from the paper's own numbers and will find surprising. **About 25 words of disclosure removes it entirely.** No numerical result changes.

---

## B. Evidence Inventory

| Path | Location | Evidence | Strength |
|---|---|---|---|
| `scripts/canonical_gt.py` | lines 8–14 | **`g_t : SAFE if sunrise(date) ≤ t < sunset(date); UNSAFE otherwise; UNSAFE on ⊥`** — astronomical, half-open, *"exact sunrise is SAFE, exact sunset is UNSAFE"* | **Direct — canonical implementation** |
| same | lines 15–19 | *"g_t emits NO CAUTION. Im(g_t) = {SAFE, UNSAFE}"* — the time component cannot produce CAUTION | **Direct — code** |
| same | **lines 38–47** | **The evidence/policy separation, verbatim:** *"Evidence: … COLREGs Rule 20(b) defines sunset-to-sunrise as the navigation-LIGHT boundary; no source supports 06:00/17:00/19:00 … Policy: `night ⇒ g_t = UNSAFE ⇒ AI advisory unavailable` is a conservative **ARCHITECTURAL GOVERNANCE CHOICE. No source establishes it.** COLREGs does not require AI abstention, and nothing here asserts that night operation is prohibited or physically unsafe."* | **Direct — decisive for Q4** |
| same | lines 27–31 | Solar source: frozen artefact `data/solar/solar-events-daily.csv`, spec `solar-spec-v1`, impl `solar-v1`, location 5.98 N 116.01 E UTC+8, no DST | **Direct — provenance** |
| same | lines 33–35 | Classification consumes `sunrise_hours`/`sunset_hours` floats, *"NEVER the HH:MM:SS display columns"* | **Direct — code** |
| same | lines 21–23 | Supersedes a fixed-clock rule (06:00/17:00/19:00) whose *"boundaries had no located source"*, replaced by SDR-001 on 2026-09-08 | **Direct — change record** |
| same | lines 108–115 | `is_daylight()` = `g_t(...) == SAFE`; *"'Daylight' in all current canonical analysis means this, and nothing else."* | **Direct — code** |
| `scripts/condition_comparison.py` | line 213 | `dep = (d.hour >= 5) & (d.hour <= 9)` — 5 hours/day inclusive | **Direct — code** |
| same | classifier | `g_m = np.full(len(d), SAFE)` — marine warning held at least-severe throughout | **Direct — code** |
| same | lines 63, 72, 76 | Thresholds `W_CAUTION/W_UNSAFE = 21.6/27.0`; `R_CAUTION/R_UNSAFE = 10.0/20.0`; `LO/HI = 1.0/1.25` | **Direct — code** |
| `data/c8/canonical-results-post-migration.txt` | line 217 | PRIMARY departure window: SAFE 4,687 / **CAUTION 531** / **UNSAFE 3,917**, n = 9,135 | **Direct — stored artefact** |
| same | line 251 | RESOLUTION: SAFE 3,231 / CAUTION 266 / UNSAFE 2,438, n = 5,935 | **Direct — stored artefact** |
| same | **lines 368–374** | **`DEPARTURE WINDOW 05:00-09:00 — non-SAFE hours: 4,448`; `g_w at max: 0`; `g_r at max: 18 (0.4%)`; `g_m at max: 0`; `g_o at max: 1,042 (23.4%)`; `g_t at max: 3,599 (80.9%)`** | **Direct — stored attribution, but OVERLAPPING (0.4 + 23.4 + 80.9 = 104.7%)** |
| same | line 375 | *"Distinct functions ever at the maximum (departure window): 3 — g_r, g_o, g_t"*; *"NEVER binds: g_w, g_m"* | **Direct — stored artefact** |
| same | lines 54–55 | All-hours: `daylight UNSAFE hours 1,262 / 455`; `daylight UNSAFE share 5.80% / 3.23%` | **Direct — stored artefact** |
| same | lines 65–66 | `g_t — daylight CAUTION 0.00%`; `g_t — all-hours non-SAFE 86.82% / 90.19%` | **Direct — stored artefact** |
| `docs/analysis/threshold-sensitivity-analysis.md` | **line 136** | **`T1 daylight-only — non-daylight hours excluded from denominator | 5,536 / 3,594 | 9.59% | 7.40%`** — the denominators are published | **Direct — analysis document** |
| `scripts/sensitivity/threshold_sensitivity.py` | lines 118–124 | T1 implementation: `dl_mask = is_daylight(...)`; `m2 = m.values & dl_mask`; `run(d, CANON, mask=m2)` — **a denominator restriction; CANON is unchanged, g_t still runs** | **Direct — code; decisive for §H** |
| `docs/canonical/appendix-c-formalisation.md` | lines 44, 129–131, 657 | *"no source establishes that AI advisory participation must be withdrawn there"*; *"Withdrawing advisory participation under elevated risk is therefore a defensible policy — but it is a policy"*; *"COLREGs regulates lights, not decision support, and does not require AI abstention"* | **Direct — canonical record** |
| same | lines 1105, 1109 | Records the step-discontinuity tension and that *"No evidence was identified supporting a twilight CAUTION band"* | **Direct — canonical record** |
| manuscript §IV | — | *"Researcher-defined choices are … **the policy treating non-daylight hours as UNSAFE** …"* | **Direct — already disclosed** |
| manuscript §IV | — | *"The day boundary follows COLREGs Rule 20(b) [18]."* | **Direct — the one sentence needing qualification (= M-7)** |
| manuscript §V-A | — | *"C0↔C1 gave 42.88%, the frequency associated with participation gating alone"* | **Direct — accurate but undisclosed in composition** |
| manuscript §V-C | — | *"The time component emits no CAUTION by construction, so its zero is definitional."* | **Direct — correct** |
| **Diagnostic 1** (`$HOME/m3_diag.py`, outside the repo) | — | Exclusive partition of UNSAFE by trigger; reproduces canonical counts exactly | **New diagnostic calculation — validated** |
| **Diagnostic 2** (`$HOME/m3_diag2.py`, outside the repo) | — | Counterfactual with g_t removed from max-severity aggregation | **New diagnostic calculation — counterfactual, not a canonical result** |

---

## C. Daylight Policy Implementation

**Q1 — How is it operationalised?**

| Property | Finding |
|---|---|
| Form | **(A) Actual astronomical sunrise and sunset.** Not a fixed clock, not a departure-time rule. |
| Rule | `g_t = SAFE` iff `sunrise(date) ≤ t < sunset(date)`; `UNSAFE` otherwise; `UNSAFE` on missing/invalid input (fail-safe, Corollary C.1b.1) |
| Boundary convention | **Half-open** — exact sunrise SAFE, exact sunset UNSAFE |
| Source of times | Frozen artefact `data/solar/solar-events-daily.csv`, spec `solar-spec-v1`, impl `solar-v1`, 5.98 N 116.01 E, UTC+8, no DST |
| Precision | Float hours to 6 dp; display strings deliberately never used |
| Image | **{SAFE, UNSAFE} — CAUTION is not in the image, by design** |
| Does it make pre-dawn automatically UNSAFE? | **Yes.** Any hour before sunrise or at/after sunset is UNSAFE regardless of conditions. |
| Same rule for both configurations? | **Yes** — one module, imported by every canonical script; the configurations differ only in the wave file |
| Vessel-dependent? | **No.** Vessel class parameterises `g_o` only |
| Navigation-light-dependent? | **No.** No lighting state is modelled |
| Precedence | None special — `g_t` enters max-severity aggregation like any component. Because UNSAFE is ≻-maximal, a night hour is UNSAFE whatever the other components say |
| Timezone | Asia/Kuching (UTC+8), consistent across the solar artefact and the data files |

**Which category of restriction is it?** The canonical module answers this itself, and the four categories must be kept apart:

- **Not a legal prohibition.** *"COLREGs does not require AI abstention, and nothing here asserts that night operation is prohibited or physically unsafe."*
- **Partly a safety warning.** The underlying *evidence* is Atacan & Düzbastılar (2023) on elevated night-time accident probability and consequence — evidence of elevated risk, not of a required response.
- **Implemented as an operational restriction**, and specifically —
- **a researcher-defined conservative evaluation assumption.** *"Policy: `night ⇒ g_t = UNSAFE ⇒ AI advisory unavailable` is a conservative ARCHITECTURAL GOVERNANCE CHOICE. No source establishes it."*

---

## D. Authoritative Basis

**Q4 — is the daylight restriction externally supported?**

**What [18] establishes.** COLREGs Rule 20(b): *"The Rules concerning lights shall be complied with from sunset to sunrise, and during such times no other lights shall be exhibited…"* It establishes **a navigation-light obligation keyed to the sunset–sunrise interval**. That interval is a real, authoritative boundary, and the project uses it as such.

**What [18] does not establish:**

| Claim | Supported by [18]? |
|---|---|
| Vessels must display navigation lights between sunset and sunrise | **Yes** |
| Vessels may not depart before sunrise | **No** |
| Small-scale fishing may not operate in darkness | **No** |
| AI advisory participation must be withdrawn at night | **No** |
| Darkness is inherently an unsafe departure condition | **No** |

Rule 20(c) cuts further against a clean day/night split, since lights are also required from sunrise to sunset in restricted visibility.

**The project's own record is explicit and correct on this.** `appendix-c-formalisation.md:657`: *"**No source establishes this implication.** COLREGs regulates lights, not decision support, and **does not require AI abstention**. Nothing here asserts that night operation is prohibited or physically unsafe — fishers demonstrably operate at night."*

**Separation of fact from choice:**

| Element | Status |
|---|---|
| Sunset-to-sunrise as a defined maritime boundary | **SOURCE-SUPPORTED** — COLREGs Rule 20(b) |
| Solar times for the site | **COMPUTED** — frozen artefact, versioned |
| Elevated night-time operational risk | **SOURCE-SUPPORTED** — Atacan & Düzbastılar (2023) |
| `night ⇒ UNSAFE` | **RESEARCHER-DEFINED** — conservative governance policy, no source |
| `UNSAFE ⇒ AI advisory withdrawn` | **RESEARCHER-DEFINED** — architectural choice |

**The manuscript's one weak sentence**, *"The day boundary follows COLREGs Rule 20(b) [18],"* attributes the **boundary** to [18], which is correct. It does not attribute the **policy** — but it sits in a paragraph headed "Threshold provenance is separated from design choice", where every neighbouring sentence *is* a provenance claim, so a reader may carry the attribution further than intended. This is the same sentence flagged as **M-7** in the pre-submission audit, and M-3 strengthens the case for qualifying it.

---

## E. UNSAFE Trigger Reconstruction

**Q6 — every condition capable of producing UNSAFE.** All five components feed one max-severity aggregation; UNSAFE is ≻-maximal, so **each trigger is independently sufficient** and triggers may overlap freely.

| Component | UNSAFE condition | Threshold | Basis | Independently sufficient? | Can overlap? | Priority over CAUTION | Consistent across both datasets? |
|---|---|---|---|---|---|---|---|
| `g_w` wind | `wind > W_U` | **27.0 kn** | MET Malaysia Cat 2 onset (50 km/h) | Yes | Yes | Yes (max-severity) | Yes — **never fires** in either |
| `g_r` rainfall | `precip > R_U` **or** WMO code ∈ {95, 96, 99} | **20.0 mm/h** | MET Malaysia thunderstorm criteria | Yes | Yes | Yes | Yes. The storm-code route is **structurally unexercised** — the provider returns no 95/96/99 codes for this region |
| `g_o` ocean | `wave > O_U` | **1.25 m** (small vessel) | Yaakob SS3 ceiling (see M-1) | Yes | Yes | Yes | Yes — different wave source per configuration |
| `g_t` time | `t < sunrise` or `t ≥ sunset` | astronomical, per date | **Researcher-defined policy** on a COLREGs boundary | Yes | Yes | Yes | Yes — one shared module |
| `g_m` marine warning | held at `SAFE` throughout | — | declared exclusion (no archive) | — | — | — | Yes — **never fires** |
| Visibility | **not modelled** | — | — | — | — | — | — |

**Tie-breaking:** none is needed. Aggregation is `max` over the five severities; ties are immaterial because the output is the maximum, not the identity of the arg-max. The "at max" attribution counts in the stored artefact are therefore **overlapping by construction** — which is exactly why §F required a separate exclusive partition.

---

## F. Attribution Analysis

### F.1 What the stored artefact gives — and why it is insufficient

`data/c8/canonical-results-post-migration.txt:368–374` reports, for the PRIMARY departure window over the 4,448 non-SAFE hours: `g_r` at max 18 (0.4%), `g_o` at max 1,042 (23.4%), `g_t` at max 3,599 (80.9%), `g_w` and `g_m` zero. **These sum to 4,659 against 4,448 hours, and the percentages to 104.7%** — they are trigger-incidence counts with overlap, not an exclusive attribution. They cannot answer items 3–6 and 8–10 of the brief.

### F.2 New diagnostic calculation — method and validation

**This is a new read-only diagnostic, not a canonical experiment result.** It imports the canonical `g_t` module, uses the canonical thresholds verbatim, and applies the identical load / merge / `dropna` / window filter. Nothing was written to the repository.

**Validation:** the diagnostic reproduced the stored canonical state distributions exactly — PRIMARY 4,687 / 531 / 3,917 = 9,135, D(C0,C1) = 42.88%, Δ<sub>L2</sub> = 5.81%; RESOLUTION 3,231 / 266 / 2,438 = 5,935, 41.08%, 4.48%. It also reproduced the stored `g_t at max: 3,599` independently. The partition below rests on a classifier demonstrably identical to the canonical one.

"Environmental trigger" means `g_w`, `g_r` or `g_o` = UNSAFE. `g_m` is excluded by declaration and never fires.

### F.3 PRIMARY — departure window 05:00–09:00

| # | Quantity | Count | % of UNSAFE | % of n = 9,135 |
|---|---|---|---|---|
| 1 | Evaluated hours | **9,135** | — | 100% |
| 2 | UNSAFE hours | **3,917** | 100% | **42.88%** |
| 3 | Hours where darkness triggers UNSAFE (any) | 3,599 | 91.88% | 39.40% |
| 4 | **Hours where darkness is the *only* trigger** | **3,389** | **86.52%** | **37.10%** |
| 5 | Hours where darkness overlaps an environmental trigger | 210 | 5.36% | 2.30% |
| 6 | **Hours where only environmental conditions trigger UNSAFE** | **318** | **8.12%** | **3.48%** |
| 7 | Night hours in the window (any state) | 3,599 | — | 39.40% |
| 8 | % of UNSAFE attributable to darkness **alone** | — | **86.52%** | — |
| 9 | % of UNSAFE **involving** darkness (incl. overlap) | — | **91.88%** | — |
| 10 | **UNSAFE surviving removal of the time rule** | **528** | — | **5.78%** |

Rows 4 + 5 + 6 = 3,389 + 210 + 318 = **3,917** ✔ exclusive and exhaustive, no double-counting.

### F.4 RESOLUTION — departure window 05:00–09:00

| # | Quantity | Count | % of UNSAFE | % of n = 5,935 |
|---|---|---|---|---|
| 1 | Evaluated hours | **5,935** | — | 100% |
| 2 | UNSAFE hours | **2,438** | 100% | **41.08%** |
| 3 | Darkness triggers UNSAFE (any) | 2,341 | 96.02% | 39.44% |
| 4 | **Darkness only** | **2,272** | **93.19%** | **38.28%** |
| 5 | Darkness + environmental | 69 | 2.83% | 1.16% |
| 6 | **Environmental only** | **97** | **3.98%** | **1.63%** |
| 7 | Night hours in the window | 2,341 | — | 39.44% |
| 8 | % attributable to darkness alone | — | **93.19%** | — |
| 9 | % involving darkness | — | **96.02%** | — |
| 10 | **UNSAFE surviving removal of the time rule** | **166** | — | **2.80%** |

Rows 4 + 5 + 6 = 2,272 + 69 + 97 = **2,438** ✔

### F.5 Why the night share is ~39.4% of the window

The window is 05:00–09:00 (5 hours/day). Sunrise at 5.98 N, 116.07 E runs 05:59–06:32 year-round, so the 05:00 hour is pre-dawn every day and the 06:00 hour on most. Two of five window hours ≈ 40% — the measured 39.40% / 39.44%. **The 42.88% participation-gating figure is, to within ~3.5 percentage points, the fraction of the chosen departure window that falls before sunrise.**

---

## G. Participation-Only Disagreement Interpretation

**Q8 — verify D(C0,C1) = P(S = UNSAFE).** C0 admits FULL at every state; C1 admits FULL at SAFE and CAUTION and ∅ at UNSAFE. They differ exactly on UNSAFE hours. Therefore D(C0,C1) = P(UNSAFE). Confirmed numerically: 3,917/9,135 = 42.88%; 2,438/5,935 = 41.08%.

**What 42.88% and 41.08% primarily reflect:** the researcher-defined night→UNSAFE policy applied to a departure window that opens before sunrise. Adverse ocean conditions contribute ~3.5% / ~1.6% of evaluated hours; rainfall a fraction of that; wind and marine warning nothing at all.

| Description | Classification | Reasoning |
|---|---|---|
| **A.** Participation-gating disagreement | **SUPPORTED** | Exactly what it is: the frequency at which C0 and C1 admit different sets. The manuscript's own wording. |
| **B.** Weather-driven participation restriction | **MISLEADING** | Weather and sea state account for 8.12% (PRIMARY) and 3.98% (RESOLUTION) of the UNSAFE hours. The manuscript does not use this description — but Table II's placement invites it. |
| **C.** Environmental-risk-driven restriction | **NOT SUPPORTED** without heavy qualification | Darkness is an environmental *fact*; treating it as *risk* is the policy step, and no source supports it. Describing the figure this way would import the unsourced inference. |
| **D.** Combined environmental and operational-policy restriction | **SUPPORTED WITH QUALIFICATION** | Accurate in kind, but misleading in proportion unless the ~86–93% policy share is stated. The most defensible description once the split is given. |
| **E.** A direct measure of unsafe fishing conditions | **MISLEADING** | No incident record exists; the canonical record states *"fishers demonstrably operate at night"*. The manuscript explicitly disclaims this (*"activation is not linked to unsafe departures or avoided harm"*). |

**Implication.** The decomposition C0↔C1 / C0↔C2 / Δ<sub>L2</sub> is presented as a substantive result — *"The PRIMARY comparator decomposition separates the two levels."* It does separate them correctly. But the Level-1 term it isolates is, empirically, mostly a clock. Saying so costs one clause and converts the paper's most attackable number into a demonstration of the attribution analysis the paper claims as part of its contribution.

---

## H. Daylight Sensitivity Verification

**Q9 — what does "daylight-only" mean?**

`scripts/sensitivity/threshold_sensitivity.py:118–124`:

```python
dl_mask = np.asarray(_is_daylight(d["time"], d["hour"]))
m2 = m.values & dl_mask
r2, S2, _, _ = run(d, CANON, mask=m2)
```

**It restricts the evaluation set to departure-window ∩ daylight hours.** `CANON` is passed unchanged, so the classifier — including `g_t` — is untouched. It is a **denominator change**, not a removal of the rule, not a policy change.

**Verification of the published values** (arithmetic from stored counts, no re-run):

| | Numerator (CAUTION hours) | Denominator | Computed | Published |
|---|---|---|---|---|
| PRIMARY | 531 | 9,135 − 3,599 = **5,536** | 531/5,536 = **9.5918%** | **9.59%** ✔ |
| RESOLUTION | 266 | 5,935 − 2,341 = **3,594** | 266/3,594 = **7.4012%** | **7.40%** ✔ |

`threshold-sensitivity-analysis.md:136` publishes the denominators as "5,536 / 3,594", matching exactly.

**Why the numerator is unchanged:** `g_t` emits only SAFE or UNSAFE, and UNSAFE is ≻-maximal, so every night hour is UNSAFE and no night hour can be CAUTION. CAUTION hours ⊆ daylight hours, and restricting to daylight removes none of them.

**The trap the brief warns about, confirmed.** 9.59% − 5.81% = 3.78 pp is **purely a denominator artefact** — the same 531 hours over 5,536 instead of 9,135. It carries no information about how many UNSAFE hours darkness caused. Treating it as such would be a straightforward error.

**Does the existing sensitivity analysis already demonstrate M-3?** **No.** T1 shows that Δ<sub>L2</sub> is sensitive to the *denominator policy* — a different and lesser claim. **No existing sensitivity analysis examines the composition of C0↔C1.** That is precisely the gap M-3 identifies, and the attribution in §F fills it.

**Does T1 support a causal or robustness claim?** It supports a **robustness** claim about Δ<sub>L2</sub> under an alternative denominator. It supports **no causal claim** about darkness.

### H.1 A counterfactual the paper does not have — and that favours it

**New diagnostic calculation (counterfactual; not a canonical result).** Dropping `g_t` from the max-severity aggregation:

| | Δ<sub>L2</sub> canonical | Δ<sub>L2</sub> without the time rule | CAUTION hours suppressed | D(C0,C1) canonical | D(C0,C1) without |
|---|---|---|---|---|---|
| PRIMARY | 5.81% | **9.73%** | 358 | 42.88% | **5.78%** |
| RESOLUTION | 4.48% | **7.58%** | 184 | 41.08% | **2.80%** |

**The time rule suppresses Δ<sub>L2</sub>.** 358 and 184 hours that would classify CAUTION on sea state or rainfall are absorbed into UNSAFE by darkness. The reported headline is therefore **conservative** with respect to the policy choice most open to challenge — the opposite of what a sceptical reviewer would assume.

**Caution for anyone reusing these numbers:** the counterfactual Δ<sub>L2</sub> (9.73%) and the T1 daylight-denominator figure (9.59%) are **close but unrelated** — 889/9,135 versus 531/5,536. They must not be conflated or quoted interchangeably.

---

## I. Impact on Contribution and Validity

| Aspect | Impact | Reasoning |
|---|---|---|
| **A. Mathematical correctness of the comparator construction** | **None.** | D(C0,C1) = P(UNSAFE) derived and verified. The construction is sound whatever populates UNSAFE. |
| **B. Correctness of 42.88% and 41.08%** | **None.** | Reproduced exactly from the canonical classifier. They are correct values of a correctly defined quantity. |
| **C. Interpretation of those rates** | **Materially affected — this is where M-3 lands.** | They measure participation gating under a classifier whose UNSAFE state is ~86–93% policy-driven. Correct as stated, misleading if left unqualified. |
| **D. Interpretation of Δ<sub>L2</sub>** | **Minor, and in the paper's favour.** | Δ<sub>L2</sub> = P(CAUTION) is untouched by the composition of UNSAFE, and `g_t` emits no CAUTION. The time rule *suppresses* it (§H.1), so the headline is conservative. |
| **E. Robustness of the evaluation** | **Improved by disclosure.** | The paper already reports threshold, vessel-class and denominator sensitivity. Adding the UNSAFE composition completes the attribution analysis it claims as a contribution. |
| **F. Generalisability to vessels operating at night** | **Genuinely limited, and currently understated.** | Any operator with navigation lights and night practice would see a radically different C0↔C1. The canonical record notes *"fishers demonstrably operate at night"*. §VI confines claims to the evaluated site but does not name the night policy as a generalisation boundary. |
| **G. Novelty of the measurement assembly** | **None.** | The contribution is the assembly — criterion, comparator, replay, sensitivity and attribution. Attribution finding that one component dominates is the assembly *working*, not failing. |
| **H. Claims of safety effectiveness** | **None — none are made.** | *"No incident or outcome record exists for the site, so activation is not linked to unsafe departures or avoided harm."* |

**A researcher-defined policy does not invalidate the experiment.** The paper measures the operational effect of a *declared* governance contract, and the night rule is part of that contract, declared as researcher-defined in §IV. **Equally, correct arithmetic does not license an unqualified reading.** A number that is 86.5% clock, presented beside environmental thresholds without comment, will be read as weather.

---

## J. Assessment of Auditor M-3

| Claim | Verdict | Evidence |
|---|---|---|
| The daylight restriction drives the C0↔C1 rate rather than weather or ocean conditions | **CONFIRMED — and understated.** | 86.52% / 93.19% of UNSAFE hours are night-only. Removing the rule: 42.88% → 5.78%, 41.08% → 2.80%. My own pre-submission estimate ("roughly 40 of the 42.88 points") was directionally right but imprecise; the verified figure is larger. |
| ~40% of window hours are definitionally UNSAFE from the time rule | **CONFIRMED.** | 3,599/9,135 = 39.40%; 2,341/5,935 = 39.44% |
| This does not affect Δ<sub>L2</sub> | **CONFIRMED, with a refinement.** | `g_t` emits no CAUTION, so it cannot create CAUTION hours. But it *removes* them: Δ<sub>L2</sub> would be 9.73% / 7.58% without the rule. Δ<sub>L2</sub> is conditional on the policy — conservatively so. |
| The manuscript should say the C0↔C1 magnitude is governed by the non-daylight policy | **CONFIRMED.** | No such statement exists; the composition is nowhere disclosed. |
| **(Implied) the manuscript presents 42.88% as an environmental-severity measure** | **NOT SUPPORTED.** | Every occurrence reads *"the frequency associated with participation gating alone"*. I searched all sections for the seven overclaim patterns in the brief and found none. The risk is reader inference, not authorial claim. |
| **(Implied) the daylight policy is presented as externally mandated** | **NOT SUPPORTED.** | §IV explicitly lists *"the policy treating non-daylight hours as UNSAFE"* among researcher-defined choices. Only *"The day boundary follows COLREGs Rule 20(b)"* needs qualification, and that is M-7. |

---

## K. Recommended Manuscript Action

| Option | Scientific necessity | Evidence available? | Reviewer risk if omitted | Impact on contribution | Impact on results | Page cost |
|---|---|---|---|---|---|---|
| **1. No change** | Insufficient — the composition is undisclosed and a reviewer can derive it | — | **Moderate.** This is the finding most likely to be found independently | None | None | 0 |
| **2. Clarify the daylight policy as researcher-defined** | **Already done** in §IV | — | — | None | None | 0 |
| **3. Qualify the participation-only result** | **Necessary** | Yes | Low once applied | None | None | ~12 words |
| **4. Add verified attribution** | **Now available and warranted** | **Yes — §F, validated against stored counts** | Low once applied | **Strengthens** — demonstrates the attribution analysis the paper claims | None | ~12 words |
| **5. Add another sensitivity experiment** | **Not necessary** | — | — | Dilutes | None | ~100 words |
| **6. Combined minimal correction** (3 + 4) | **Correct and sufficient** | Yes | **Lowest** | Strengthens | None | **~25 words** |

### Recommendation: **Option 6.**

Option 5 is unnecessary: the attribution is exactly computable from existing records, cross-validates against the stored artefact, and needs no new run. Option 3 alone is weaker than Option 4 — a qualitative hedge invites the reviewer to compute the number themselves, whereas giving the number closes the question. The brief's caution against "adding numerical attribution without verifying its provenance" is satisfied: the partition reproduces the canonical state distributions to the hour and matches the stored `g_t at max: 3,599` independently.

**I do not recommend reporting the §H.1 counterfactual in the paper.** It is favourable, but it is a counterfactual classifier rather than an evaluated configuration, and introducing it would invite questions about a contract the paper does not evaluate. It belongs in the thesis and in the response to reviewers.

---

## L. Exact Proposed Text Changes

### L.1 §V-A — the comparator decomposition *(required)*

**Original:**

> "The PRIMARY comparator decomposition separates the two levels. C0↔C1 gave 42.88%, the frequency associated with participation gating alone, and C0↔C2 gave 48.69%, the frequency associated with participation gating together with the intermediate contraction."

**Minimal replacement — append one sentence:**

> "The PRIMARY comparator decomposition separates the two levels. C0↔C1 gave 42.88%, the frequency associated with participation gating alone, and C0↔C2 gave 48.69%, the frequency associated with participation gating together with the intermediate contraction. **The C0↔C1 magnitude is governed by the non-daylight policy rather than by environmental severity: 86.5% of the PRIMARY UNSAFE hours and 93.2% of the RESOLUTION UNSAFE hours are pre-sunrise hours carrying no other trigger, the departure window opening before sunrise year-round.**"

**Justification.** States the composition where the number first appears, with figures verified against the canonical classifier. Pre-empts the one derivation a reviewer is most likely to perform, and does so in the paper's own terms. **Δ<sub>L2</sub> is unaffected and needs no caveat here** — `g_t` emits no CAUTION, which §V-C already says. Cost: ~40 words; ~25 if the RESOLUTION figure is dropped.

### L.2 §VI Limitations — generalisation boundary *(recommended)*

**Original:**

> "Several governance choices remain researcher-defined rather than empirically validated: the three-state cardinality, the evaluation policies fixed in Section IV, and the admissible set AAI(CAUTION) = {Go, Delay}."

**Minimal replacement:**

> "Several governance choices remain researcher-defined rather than empirically validated: the three-state cardinality, the evaluation policies fixed in Section IV, and the admissible set AAI(CAUTION) = {Go, Delay}. **The non-daylight policy in particular bounds generalisation: an operator equipped and practised for night departure would produce a materially different participation-gating rate under the same conditions.**"

**Justification.** The paper limits its claims to the site and vessel class but not to the *operating policy*, which here is the dominant driver. One sentence, ~28 words. Lower priority than L.1 — drop it first if space is tight.

### L.3 §IV — COLREGs attribution

Already covered by **M-7** in the pre-submission audit (*"The day boundary is taken from the sunset-to-sunrise trigger in COLREGs Rule 20(b)"*). M-3 raises its priority: with L.1 in place, a reader sees that the night rule drives 86.5% of the Level-1 figure, which makes the precision of its attribution matter more.

### L.4 No change required

- §IV's researcher-defined list — **already correct**, and it is what keeps this a clarification.
- §V-C's *"The time component emits no CAUTION by construction, so its zero is definitional"* — **correct and well judged.**
- §V-C's daylight-only denominator sentence — **correct**; it says "denominator", which is exactly what T1 does.
- §VI's disclaimer that activation is not linked to unsafe departures — **correct.**

### L.5 Numerical results

**None change.** 42.88%, 41.08%, 48.69%, 45.56%, 5.81%, 4.48%, 9.59%, 7.40%, every count and every envelope stand exactly as reported. The proposed text adds two verified percentages that are not currently in the paper.

---

## M. Unresolved Questions

1. **The counterfactual Δ<sub>L2</sub> values (9.73% / 7.58%) are new diagnostic output, not canonical.** They were produced by a classifier with `g_t` removed, which is not an evaluated configuration and has no stored artefact. If the authors want to cite them anywhere, they should be produced by a canonical script and stored.

2. **No existing sensitivity analysis varies the time policy itself.** T1 varies the denominator. A "no-night-rule" or "twilight-CAUTION-band" variant has never been run. `appendix-c-formalisation.md:1109` records that no evidence was found for a twilight band, so adding one would mean adopting a state for its smoothing effect — which the project explicitly declined. **No new experiment is necessary for the paper's claims**; this is noted as a gap in the sensitivity coverage, not a defect.

3. **The 05:00–09:00 window was chosen without an observed departure record.** §IV says so: *"an evaluation-policy choice rather than an observed departure period."* Because the window straddles sunrise, the night share — and therefore C0↔C1 — is highly sensitive to where it starts. A 06:00–10:00 window would change the figure substantially. Not computed here; outside M-3's remit.

4. **Whether a reviewer would accept the disclosure as sufficient.** My judgement is yes: the quantity is correctly defined, correctly computed and, with L.1, correctly characterised. That is a prediction, not a result.

---

## N. Final Verdict

> ## MINOR CLARIFICATION REQUIRED

One sentence in §V-A, optionally one in §VI. **~25–40 words.** No numerical result changes and no new experiment is needed.

**M-3 is the strongest of the three findings investigated.** The hypothesis is confirmed and larger than estimated: **86.5% (PRIMARY) and 93.2% (RESOLUTION) of the UNSAFE hours behind the participation-gating figure are pre-sunrise hours with no environmental trigger**, and removing the policy would move 42.88% to 5.78% and 41.08% to 2.80%.

What keeps it a clarification rather than a correction is that the arithmetic is right, the policy is already declared researcher-defined, and the manuscript makes no claim that the figure is weather-driven. What makes it the most urgent of the three is that a reviewer can derive the 86.5% from the paper's own method section, and will find it unannounced.

**And the disclosure is in the paper's favour.** The time rule suppresses Δ<sub>L2</sub> rather than inflating it: the headline would be 9.73% without it, not 5.81%. Stating the composition turns the paper's most attackable number into an instance of the attribution analysis it claims as part of its contribution.
