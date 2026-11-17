# Next Research Decision Package

> **PARTLY RETRACTED — 17 Nov 2026, same day.** A critical review in `research/d4-critical-review.md` retracts the recommendation of FAO/ILO/IMO 2012 as an **episode-level** hazard reference (no vessel design category is assigned, and at this site every plausible assignment is degenerate: Category C is exceeded in 2 of 9,135 cases), qualifies the N1 pass as holding only for an **anticipative** generator (three temporal leaks identified), and corrects the claim that issue-time forecasts are off the advisory comparison's critical path. **Nothing below is edited** — every original criterion, threshold and result is preserved verbatim. Read the review alongside this document.


**Prepared:** 17 November 2026 · **Author of this document:** Claude (Cowork session) · **Status:** decision support, not an endorsement

**Input read in full:** [`research/phd-proposal-defence-readiness.md`](phd-proposal-defence-readiness.md), together with [`research/next-research-plan.md`](next-research-plan.md) and [`papers/consolidated-literature-review-gap-matrix.md`](../papers/consolidated-literature-review-gap-matrix.md). All three are preserved; this document adds to them and overwrites none of their findings.

**Authorization boundary observed.** No experiment was run. No participant was recruited or contacted. No external request, data request, account registration, licence enquiry or ethics submission was submitted. The forecast-source work in §3 is an **audit of published documentation only**; no collector was written and no archive was queried for data. Where a step would require authorization, it is named as a decision in §6 and left undone.

**Frozen documents untouched.** `docs/analysis/final-research-chain-lock.md`, `CLAUDE.md`, `docs/canonical/*` and the Journal 1 submission manuscript were read and are unmodified. The reconciliation in §2 is a **crosswalk that sits beside** the frozen set; it proposes no edit to it.

**One correction was applied to a non-frozen document.** `research/phd-proposal-defence-readiness.md` is this session's own prior output, and the user instructed its count be corrected. The change is recorded in §1.

**Superseded in part, 17 Nov 2026 (same day).** D-4 and D-3 were prioritised and worked immediately after this package was written. `research/d4-reference-validity-and-non-degeneracy.md` carries the result and **supersedes §4.3, §4.4 and §5.5 below**: no harm-severity reference exists for this vessel class in these waters, so the §4.3 scale must be relabelled as a **hazard** scale; FAO/ILO/IMO (2012) clause 1.2.14 is the verified independent candidate; and the N1–N4 gate has been **run once and failed as pre-registered**, while establishing that a non-degenerate candidate pool is achievable. Read that document alongside this one.

**Evidence conventions.** **[VERIFIED]** = read from a primary source or executed against the repository on 17 Nov 2026. **[DOCUMENTED]** = a repository file asserts it. **[PROPOSED]** = a plan, not an artefact. **[NOT FOUND]** = does not exist in this repository. **[UNRESOLVED]** = a live contradiction between sources, reported rather than settled. **[AUDIT]** = assessed from a source's own public documentation, not from retrieved data.

---

## 1. Corrections applied

### 1.1 Classification count — corrected

The readiness package said *"eight restrict the actions of an autonomous system; one restricts output shown to a human"*. **That was wrong, and it contradicted the package's own §2.4 table one page earlier, where P9 is already graded "Neither".** The corrected split: **[VERIFIED]**

| Object of restriction | Count | Papers |
|---|---|---|
| An autonomous system's **actions** | **7** | P1 Vaaler, P2 Ghaleb, P4 AAAI-25, P5 Corsi, P6 ProSh, P7 (augmented action space), P8 Gerold & Lucia |
| **Advice** shown to a human who decides | **1** | P3 Kim et al. (SA-ROC) |
| A **human user's own data permissions** — neither of the above | **1** | P9 CARAC |
| **Total** | **9** | |

Both occurrences in the readiness package (§1.1, §2.4) now carry the 7 / 1 / 1 split with the correction noted inline.

### 1.2 Novelty claim — qualified as sample-limited

Every *"no competitor"* and *"none of the nine"* statement in the readiness package is now explicitly bounded, and a new §8.6 states the bound in full. The substance:

**The claim that survives.** *Within a non-systematic sample of nine primary sources, none restricts which category of advisory output may be shown to a human who retains authority.*

**The claim that does not.** *No prior work does this.*

**Why the distinction is not pedantry.** The nine-paper pool came from Scopus AI synthesis plus GPT's Matrix A, screened by one reviewer. There is no registered protocol, no documented database set, date range or query string, no inclusion/exclusion criteria, no PRISMA flow, no second rater, no inter-rater statistic, and no backward or forward citation chase. Two further named competitors (CAP, Miller's *Adaptive Human Oversight*) are unheld and uncounted. A reviewer overturns the unqualified claim with a single paper; the qualified claim survives that. Converting the first into the second requires a registered systematic review for this specific question, which **this project has not run** and which is not costed anywhere in the plan.

**Consequence for the defence.** The §3 novelty gradings should be presented as *defensibility under a declared sample limit*, never as literature-wide absence. Saying so first is stronger than being caught: a declared limit is methodological honesty, an undeclared one is an error.

---

## 2. RQ reconciliation — crosswalk, no frozen document changed

### 2.1 The first finding is that there are two live RQ sets, not one **[UNRESOLVED]**

Both are dated **2026-09-21**. They are not compatible.

| Source | Authority it claims | RQ set |
|---|---|---|
| `docs/analysis/final-research-chain-lock.md:44-50` | *"Authoritative specification. Subsequent canonical revisions must follow this document."* | **RQ1** operational specification · **RQ2** empirical characterisation and robustness · **RQ3** structural warrant of the multi-component classifier |
| `CLAUDE.md:47-51` | Project instructions; its own core-contribution paragraph says it was *"revised 2026-09-21 under `docs/analysis/final-research-chain-lock.md`"* | **RQ1** architecture design · **RQ2** formal specification · **RQ3** prototype implementation · **RQ4** technical validation (three-condition comparison) · ~~**RQ5**~~ struck |

The lock resolves the conflict against `CLAUDE.md` on its own terms: its **"Not reintroduced"** list explicitly excludes *"prototype implementation as an RQ"* and *"Safety Dominance as an independent thesis-level RQ"* — which are `CLAUDE.md`'s RQ3 and the substance of its RQ2. **So `CLAUDE.md`'s RQ table is stale, and the lock supersedes it.** That reading is internally consistent and requires editing nothing, but it is an inference from two documents of the same date, so it is a **supervisor sign-off item, not a settled fact** (§6, D-1). Until it is signed off, every RQ number in conversation is ambiguous, and that alone can damage a defence.

**This crosswalk uses the lock's numbering throughout, and says so wherever a number appears.**

### 2.2 Does the proposed advisory comparison answer a frozen RQ? No. **[VERIFIED]**

| Frozen RQ | What it asks | How it is answered today | Does the proposed study answer it? |
|---|---|---|---|
| **RQ1** Operational specification | Can `G(S)` and `A_AI(S)` be specified as separate state-conditioned functions with totality and containment preserved under structural unavailability; which elements are designer-decided | By construction and proof — `appendix-c-formalisation.md`, P1–P3, the `D = {m}` lower-bound consequence, the threshold-provenance table | **No.** RQ1 is settled by proof. Human scores cannot confirm or refute a containment property |
| **RQ2** Empirical characterisation and robustness | How often the intermediate state yields a stricter admissible set than a participation-only gate, and how sensitive that frequency is to threshold and data configuration | By replay — Δ_L2 = 5.81% / 4.48%, envelope 5.67–9.56%, `threshold_sensitivity.py` | **No, not as asked.** RQ2's dependent variable is a *set-difference frequency*, and its robustness clause is scoped to *"environmental-threshold and data configurations"* — not to advisory content, not to human judgement |
| **RQ3** Structural warrant | Which components actually determine the intermediate classification, and is the multi-component structure warranted | By component attribution over the same replay — `g_o` 97.6%, `g_r` 2.4%, three components never bind | **No.** Component attribution is a property of the classifier over the record |

**Conclusion.** The proposed study answers none of frozen RQ1–RQ3 and populates no chapter that the lock provides for. The readiness package's §1.2 finding stands, and nothing in this crosswalk softens it.

### 2.3 But it is **not** the struck RQ5 either — and this is the strongest available card **[VERIFIED]**

Struck RQ5 was: *"Contextual validation — user study with fishers across three safety states"*, re-designated as *"future socio-technical/contextual validation"* (`CLAUDE.md:51`). The lock's "Not reintroduced" list bars *"contextual fisher validation as a completed RQ"*.

An expert-rater advisory-content study is a **different construct on three axes**:

| Axis | Struck RQ5 | Proposed study |
|---|---|---|
| **What is scored** | The users' response to the system — trust, reliance, comprehension, acceptance | The **advice itself**, against an external safety reference |
| **Who participates** | Fishers, as the deployment population | Domain experts, as **raters of advice**, not as subjects of a socio-technical claim |
| **What is claimed** | That the architecture works with real users in context | That restricting advisory **categories** changes the safety character of what a human is shown |

**What follows.** The lock does not bar this study. It simply has no slot for it. Those are different problems with different fixes, and conflating them is what makes the obstacle look fatal when it is not.

**Two cautions, so this card is not overplayed.** First, if the raters are drawn from the fisher population, the distinction collapses and the study becomes the struck RQ5 by another name — so rater provenance is load-bearing, not a detail (§4.5). Second, "the lock does not bar it" is not "the lock permits it as an RQ": adding one is an act of supervisory authority, not of inference.

### 2.4 The three sitings available, stated honestly

| | Siting | What it requires | Strength | Honest cost |
|---|---|---|---|---|
| **S-A** | **Construct-validity study for RQ2's dependent variable.** No new RQ; the result enters the RQ2 chapter's validity section and the limitations chapter | Supervisor agreement that a validity study may occupy chapter space without its own RQ | **Strongest fit to existing documents.** The hook already exists in the project's own words — Journal 1 concedes at `manuscript.md:1462` that divergence *"counts admissible-set differences, not differences in what was actually recommended or what an operator would have done"*, and that *"only one conclusion type is generated … the withheld types are withheld from a rule set that could not have produced them"*. That concession is a threat to the construct validity of RQ2's headline number. A study that bounds it is doing RQ2's work, not new work | A validity study is a **defensive** contribution. It will not read as a thesis's novel claim, and an examiner may ask why it needed a human panel rather than a rule-set extension |
| **S-B** | **New RQ4 under supervisory authority**, declared as advisory-content safety, explicitly distinguished from struck RQ5 per §2.3 | Supervisor, and plausibly committee, sign-off; a documented amendment to the frozen set; ethics approval | Gives the result a chapter and an RQ of its own. Uses the §2.3 argument at full strength | **Reopens a set that was frozen deliberately.** The lock exists because the RQ set had already churned. Reopening invites the question of what else is unsettled, and sets a precedent for the next addition |
| **S-C** | **Outside the thesis** — a standalone paper after submission | Nothing now | Zero risk to the thesis timeline. Keeps the frozen set frozen | Forgoes the contribution in the thesis. If the structural-novelty claim in §1.2 is the project's best one, this is the option that leaves it unevidenced |

**My reading, offered as a judgement and not as a finding.** S-A is the one to take to the supervisor first, with S-B as the fallback if the supervisor wants the result to carry an RQ. The reason is not that S-A is more ambitious — it is less — but that it is the only option whose justification is already written down in the project's own documents, in the project's own words, as a conceded weakness. An examiner who reads `manuscript.md:1462` and then finds a study that closes exactly that gap sees a researcher who took their own limitation seriously. S-B asks the examiner to accept a late addition to a set whose own lock document says subsequent revisions must follow it.

### 2.5 One false dependency to remove **[VERIFIED]**

`publications/active/journal-1/README.md:60` claims *"Experimental evidence: graduated vs. binary-gated vs. ungated baseline comparison"*. **That claim is already satisfied** by the existing C0 / C1 / C2 replay. It does **not** depend on the proposed human study. If the advisory comparison is deferred or dropped, that README claim does not fall with it. Any argument that the study is needed to keep a publication promise is mistaken, and should not be used on the supervisor.

---

## 3. Issue-time forecast source audit **[AUDIT — no collection implemented]**

### 3.0 The finding that changes the priority

**The advisory comparison does not need issue-time forecasts.** Its stimulus cases can be drawn from the existing ERA5-Ocean record already in the repository. Issue-time data is a blocker for a **different** strand — the staleness / delayed-observation strand at readiness §3.3, which the readiness package already graded *"lowest of the three, and currently unsupportable"*.

So this audit answers a question that is **not on the critical path for the decision in §6**. It is reported in full because it was asked for, and because its conclusion is decisive for whether that third strand is ever viable. **If the §6 decision is S-A or S-C, none of §3 needs to be acted on.**

### 3.1 What a usable issue-time record must contain

Per record: forecast issue time (model run), valid time, lead time, model identifier and version, and the variables 10 m wind, significant wave height, precipitation rate, ideally wave period — at or near 5.98° N, 116.01° E, hourly or 3-hourly, **retrievable for runs issued in the past**. A reanalysis cannot serve: it is not what anyone was shown at decision time. Neither can a hindcast or a reforecast, for the same reason. **This distinction disqualifies most of the long archives that look suitable at first glance.**

### 3.2 Candidate assessment **[AUDIT]**

| Source | Real past-run archive? | Depth | Wind / Hs / Precip / Period | Licence | Verdict |
|---|---|---|---|---|---|
| **ECMWF MARS operational archive** (HRES + HRES-WAM) | **Yes** | Hourly output from all four cycles archived since 15 Nov 2011; wave coupling since 1998 — covers 2020–2025 | ✓ / ✓ / ✓ / ✓ | Service Agreement; €3,000/yr commercial, **waivable at ECMWF's discretion for time-bound non-commercial research** | **The only single source covering all four variables across 2020–2025.** Licence is the problem, not the data: the fee-waiver terms treat dissemination and distribution as commercial use, so **the extracted records could not be published as supplementary data** |
| **GEE `NOAA/GFS0P25`** | **Yes** — `creation_time`, `forecast_time`, `forecast_hours` preserved | **1 Jul 2015 →** | ✓ / ✗ / ✓ / ✗ | **Public domain, no restrictions** | **Best free source for wind and rainfall.** Two traps: `precipitation_rate` exists only from 15 Jan 2025, so earlier work must use `total_precipitation_surface` with its variable 1–6 h accumulation window; and the catalogue does not state which of `creation_time` / `forecast_time` is the run time — verify against a known run before relying on it |
| **GEE Copernicus Marine `WAV_ANFC_0_083DEG_PT3H`** | **Yes** — `run_time`, `forecast_hours`, `observation_type` | **1 Jun 2022 →** | ✗ / ✓ / ✗ / ✓ | CMEMS licence; credit required | **Best free wave source, and the finest grid of any candidate (~9 km).** Starts mid-2022, 3-hourly |
| **dynamical.org GFS Zarr** | Yes — explicit `init_time` | 2021-05-01 → | ✓ / ✗ / ✓ / ✗ | Not stated on the GFS page | Cleaner than GEE to work with; misses 2020 and the first four months of 2021; licence unstated, which for a thesis is itself a defect |
| **ECMWF Open Data** (free real-time) | **No** — *"retained for the most recent 12 forecast runs"*, ≈2–3 days | none | ✓ / ✓ / ✓ / ✓ | **CC-BY-4.0, redistributable** | Useless retrospectively; **excellent for prospective collection** if that route is ever taken |
| **NOMADS / AWS–Azure NODD mirrors** | **No** — rolling 4 weeks / 30 days | none | ✓ / ✓ / ✓ / ✓ | US public domain | Not an archive. Commonly mistaken for one |
| **NOAA WAVEWATCH III long records** | **No** | — | — | — | **The long records are hindcasts; the ensemble product is a reforecast.** Neither is what a forecaster issued. Disqualified on construct, not on coverage |
| **CMEMS native** | **Partly** — *"the data from the previous forecast production cycle is erased and replaced"*; archived NRT forecasts from the past two years *"available on demand through User Support"* | ~2 years, per-request | ✗ / ✓ / ✗ / ✓ | CMEMS | A support ticket per request is unworkable for a systematic study. The GEE mirror is the practical route to the same product |
| **Met Office Global Wave on AWS** | Yes — *"2-year rolling archive"* | 2 years rolling, so cannot reach 2020 | ✗ (has 10 m wind) / ✓ / ✗ / ✓ | **Crown copyright, CC BY-SA** | Public beta, explicitly non-operational; share-alike may propagate to a derived published dataset; coarsest wave grid here (~39 × 26 km at this latitude) |
| **METMalaysia** | **No archive found** | — | text bulletins only | No published licence | API `start_date` must be today or later; warning dates are validity dates, not publication dates; `METToken` issuance route is undocumented. **For a decision-reconstruction study the official local bulletin is arguably the most relevant forecast of all, and it appears not to be archived anywhere retrievable.** Settling this needs a direct written enquiry to METMalaysia — **not submitted, per the authorization boundary** (§6, D-5) |

### 3.3 Retrospective coverage for 2020–2025 — direct answer

- **Wind and rainfall: yes, free, no negotiation.** GEE `NOAA/GFS0P25` from 1 July 2015, four runs daily, issue/valid/lead all preserved, public domain.
- **Significant wave height and wave period: not free back to 2020.** The earliest free issue-time wave archive reaching this site starts **1 June 2022**.
- **All four variables, one archive, full 2020–2025 window: exactly one source — ECMWF MARS**, under a Service Agreement with a discretionary research fee waiver whose terms forbid redistributing the extracted records.

So a staleness study restricted to wind and rainfall needs no prospective collection and no licence negotiation at all. One requiring waves back to 2020 must either accept MARS's no-redistribution condition or shorten its window to 2022–2025 and stay free and publishable. **Given that `g_o` (wave) accounts for 97.6% of intermediate-state activation at this site (RQ3's own result), a wind-and-rainfall-only staleness study would characterise the 2.4% and miss the mechanism — so the shortened 2022–2025 window is the realistic free option, not the wind-only one.**

### 3.4 Prospective collection is not a viable route — computed from the project's own record **[VERIFIED]**

The binding constraint is independent **events**, not records. Using the repository's own PRIMARY record (ERA5-Ocean, 43,848 hourly rows ending 2024-12-31, i.e. **five years**; 9,135 departure-window hours; **531 CAUTION hours**), the event clustering computed earlier in this work gives **85–123 independent CAUTION events** at separation thresholds of >3 days and >1 day respectively.

Over five years, that is **17 to 25 independent events per year**.

| Target | Accumulation period at this site |
|---|---|
| 100 independent CAUTION events | **4 to 6 years** |
| 50 | 2 to 3 years |
| 30 | 1.2 to 1.8 years |

**This is site-specific, threshold-specific and derived from the project's own data**, so it should be preferred over any estimate from rainfall-day climatology. It settles the question: **prospective collection cannot deliver a 100-event issue-time dataset within a PhD.** A retrospective archive is a requirement for that strand, not a convenience. And even 50 events gathered prospectively would span only two or three monsoon seasons, which is pseudo-replication a reviewer will name.

### 3.5 Recommendation, if and only if the staleness strand is pursued

**Primary: the Earth Engine pairing** — `NOAA/GFS0P25` for wind and rainfall joined on issue time to `COPERNICUS_MARINE_WAV_ANFC_0_083DEG_PT3H` for waves, window 2022-06-01 onward. Costs: a mixed-model record that must be declared, 3-hourly wave cadence, and a window that cannot reach 2020. Gains: no licence negotiation, finer wave resolution than MARS, and terms that let the extracted records be published with the thesis.

**Fallback: ECMWF MARS** under a research fee waiver, accepted only if the full 2020–2025 window is judged essential and the no-redistribution condition is acceptable to the supervisor and the examiners.

**One caveat that applies to every candidate.** At 5.98° N, 116.01° E every grid here is 9–55 km, so the point falls in a cell that may sit substantially offshore of the sheltered water behind the Tunku Abdul Rahman islands. Open-Meteo's own marine documentation warns that accuracy in coastal areas is limited and the data is not suitable for coastal navigation; the Met Office configuration targets open waters. **Grid-cell displacement must be documented as a limitation, because it is a known weak point in exactly this kind of study** — and it applies to the existing ERA5-Ocean record too, not only to any new collection.

### 3.6 Audit gaps — stated rather than papered over

Pages that could not be read, and for which no substitute was accepted: the AWS `noaa-gfs-bdp-pds` registry and readme (so that bucket's depth, and whether `gfswave` is in it, is unconfirmed); `rda.ucar.edu/datasets/d084001`; METMalaysia's official API documentation (findings rest on a January 2022 third-party mirror); NCEI's GFS product page; WeatherBench 2's data guide (so **no claim** is made about its IFS HRES forecast archive, which may be relevant); and Open-Meteo's marine past-run capability, where the documentation is ambiguous and direct probes were refused — **treat Open-Meteo marine as unverified**. ECMWF publishes no explicit start date for the operational wave streams; 2020–2025 coverage is **inferred** from the November 2011 hourly-archiving date, not stated.

---

## 4. Independent safety-reference rubric **[PROPOSED]**

### 4.1 The requirement the rubric must meet

Kim et al. (P3) is the only paper in the sample with a reference **independent of both the model and the human** — biopsy plus long-term follow-up, plus the unaided radiologist's own reading as a separate comparator. It is also the paper that found radiologist accuracy **lowest where the AI was most confident**, which is the result that makes an independent reference non-optional: a reference derived from the system's own logic cannot detect that pattern, because it agrees with the system by construction.

**The trap this rubric exists to avoid**, already named at readiness §4.3: if the rubric's thresholds are the architecture's thresholds, then "advice was unsafe" means "advice disagreed with the architecture", and a successful result is circular. §4.4 is the test that keeps this honest.

### 4.2 Four constructs, never merged

| # | Construct | Measured by | Independent of the architecture? | Who or what scores it |
|---|---|---|---|---|
| **K1** | **Hazard realisation** — what the sea and sky actually did across the advised window | The environmental record for the advised hours, read against **rubric thresholds sourced independently** (§4.4) | **Must be.** This is where circularity enters if it is going to | Machine, deterministic |
| **K2** | **Admissibility** — was the advice type inside `A_AI(S)` | The governance contract | **No, by definition** | Machine. **Excluded from rater scoring entirely** — showing it to a rater destroys blinding, because it reveals the arm |
| **K3** | **Harm exposure** — would acting on this advice have placed the vessel in realised hazard | K1 joined to the advice's own time span | Yes, if K1 is | Machine for the exposure window; **rater for severity** (§4.3) |
| **K4** | **Actionability** — does the advice let a fisher plan: is it specific, timely, and followable | Rater judgement on the advice text alone | Yes | Rater |

**Relabelling required (17 Nov 2026).** K1 and K3 as written assume a harm reference. None exists (see the D-4 report §4). K1 becomes **hazard realisation against an independent graded hazard scale**, and K3 becomes **hazard exposure**, not harm exposure. The four-construct separation survives; the word "harm" does not.

**Why the separation is load-bearing.** K3 and K4 trade off against each other, and the whole point of the architecture is that restriction buys safety at a cost in usefulness. A rubric that merges them produces a single "quality" score in which the trade-off is invisible, and the study then cannot say what it was built to say. An arm that scores better on K3 and worse on K4 is the **expected** result, and the design must be able to show it.

### 4.3 Severity scale

**Superseded — see the D-4 report §1 and §4.** No source anchors these five levels in observed harm to vessels of this class in these waters. The scale below is retained as the *form* the instrument should take; its anchors must be re-derived from a hazard reference (FAO/ILO/IMO 2012 gives **four** graded levels, not five). Retained unedited so the change is visible:

A **5-point harm-potential scale anchored in observable consequences**, never in the architecture's states:

| | Anchor |
|---|---|
| **0** | No adverse exposure. Conditions across the advised window stayed within what a small vessel routinely works in |
| **1** | Discomfort or inefficiency. Wet, slow, poor working conditions; no loss of control or equipment |
| **2** | Recoverable incident potential. Gear loss, swamping risk, a return trip that must be aborted |
| **3** | Serious incident potential. Loss of propulsion or steering in exposed water; capsize risk in realised conditions |
| **4** | Life-threatening exposure. Conditions in which a small open vessel is unlikely to remain viable |

The scale is ordinal, **not interval** — analysis must use ordinal methods, and a mean severity is not a legitimate statistic on it. Anchors must be written in the raters' own working vocabulary and pre-tested with the first two raters before any case is scored (§7, Stage 1a).

### 4.4 Independence provenance test — the multi-signal version

Threshold agreement **alone does not demonstrate dependence**. Two parties can land on the same number from independent physical evidence, and treating coincidence as proof of contamination would reject a correct rubric. So dependence is concluded only when **multiple signals coincide**. For every rubric threshold, record:

| Signal | What is recorded |
|---|---|
| **S1 Source document** | The exact publication the rubric threshold came from, with page or clause |
| **S2 Citation overlap** | Whether that source appears anywhere in the architecture's own threshold-provenance table |
| **S3 Numeric coincidence** | Whether the value equals an architecture threshold |
| **S4 Variable-set coincidence** | Whether the rubric conditions on the same variable set as the classifier (`g_w, g_r, g_m, g_o, g_t`) |
| **S5 Derivation path** | Whether the rubric threshold was chosen before or after the author knew the architecture's value |

**Decision rule, pre-registered:** flag a threshold as architecture-dependent when **S2 and S3 both hold**, or when **S3, S4 and S5 all hold**. A flagged threshold must be replaced or the dependence declared as a limitation on that specific construct. **S3 alone is not a flag** — and this is the correction that matters, because the single-signal version would have rejected any rubric that happened to agree with a correctly chosen threshold.

**Candidate independent sources**, to be assessed rather than assumed: small-vessel stability and freeboard limits from naval-architecture literature; IMO or national small-craft operating guidance; COLREGs visibility and lookout provisions; published small-vessel capsize and swamping studies. **Assessed 17 Nov 2026 — see the D-4 report §3.** Of these, **FAO/ILO/IMO (2012) clause 1.2.14** is the one credible independent candidate: scope *"new decked vessels of less than 12 m in length (L) and new undecked vessels intended to operate at sea"*, four graded levels, free to read, sharing no source or author with anything the architecture uses. It is **TYPE H (hazard), not harm**. The Wolfson Unit 2024 report must **not** be used: it shares its derivation chain with Jeong & Im, so it cannot corroborate the 1.0 m onset. The remaining stability studies are at wave heights an order of magnitude above this site.

### 4.5 Raters, blinding and agreement

| | Specification |
|---|---|
| **Raters** | **Domain experts, not fishers.** Rater provenance is what distinguishes this study from struck RQ5 (§2.3), so it is a design constraint, not a convenience. Minimum 2, target 3. Candidate pools: marine safety officers, small-craft skippers with commercial tickets, fisheries extension officers, maritime enforcement personnel. **No recruitment has taken place** |
| **What a rater sees** | The advice text, and the environmental conditions as a fisher would have had them at decision time. Nothing else |
| **What a rater must not see** | The arm label; the safety state `S`; whether any advice type was withheld; the admissibility verdict K2; the other arms' advice for the same case within the same session |
| **Order** | Case order randomised per rater; arm order randomised within matched sets |
| **Coverage** | **Two independent raters on 100% of cases**, not on a subsample. With a case count this small there is no reason to subsample, and a subsampled agreement statistic invites the question of what the unsampled cases would have shown |
| **Agreement statistic** | **Gwet's AC1 as primary**, Krippendorff's ordinal α as secondary. Both pre-registered with their thresholds before any scoring. **Reason for AC1:** severity will be heavily skewed toward 0–1, and κ-family statistics collapse under high prevalence skew — reporting a low κ on skewed data and calling it poor agreement would be a statistical artefact, not a finding |
| **Disagreement handling** | Pre-registered: adjudication by a third rater, **with the original two scores retained and reported**. Consensus must never silently replace the disagreement record |

### 4.6 Case selection — two case classes that earn their place

| Class | What it is | Why it is needed |
|---|---|---|
| **Boundary cases** | Cases where at least one component sits within ±ε of a classification threshold (ε pre-registered per component) | These are where the architecture's behaviour is genuinely contestable and where rater disagreement is **informative rather than noise**. A design that samples only clear-cut cases measures nothing about the mechanism |
| **Matched-context cases** | The **same** environmental case presented under more than one arm, blinded and separated in the rating sequence | Isolates the effect of the advice from the effect of the conditions. Without matching, an arm difference is confounded with case difference, and with ~40 cases the confound will not average out |

**Pre-registered minimums:** ≥30% boundary cases; every case appears in ≥2 arms; no rater sees the same environmental case twice within one session.

---

## 5. Non-degenerate candidate-advice pool **[PROPOSED]**

### 5.1 Why the governed prototype cannot supply the stimulus — verified, and decisive

| Finding | Evidence |
|---|---|
| The implemented rule registry contains **four CAUTION rules, all with `conclusion_type: "Delay"`** | `scripts/journal1_layer3_fidelity_evaluation.py:632-635` **[VERIFIED]** |
| The only SAFE rule, **R-SAFE-001 (`Go`), is `DEFERRED` and not executable** | same file, lines 651-662 **[VERIFIED]** |
| Across the full fidelity census of **292 episodes**, the advisory output is `["Delay"]` in **244** and `[]` in **48**. **Zero** episodes produce `Go`, `DepartureTime` or `Duration` | `data/journal1-layer3-prototype/batch5-fidelity-evaluation/fidelity-traces.csv` **[VERIFIED]** |

**What this means for the study.** `A_AI(CAUTION) = {Go, Delay}` withholds `DepartureTime` and `Duration` — **two types no implemented rule can produce**. `A_AI(SAFE) = FULL` admits four types, and **no implemented rule produces any of them**. So if the governed prototype supplied the stimulus, the ungated, participation-only and graduated arms would present **identical advice** on every case: `Delay`, or nothing. A human panel would be scoring three labels on one body of text, at full ethics and recruitment cost, and the study could not detect a difference **even if a large one existed**.

This is exactly the defect Journal 1 already conceded in its own words at `manuscript.md:1462`. **The concession is not a caveat to be managed — it is a specification for what has to be built before any human sees anything.**

### 5.2 Two ways out, and why the second is the right one

| | Approach | Assessment |
|---|---|---|
| **A** | **Extend the governed rule set** so SAFE produces `DepartureTime` and `Duration` and `R-SAFE-001` becomes executable | **Rejected for this purpose.** It is prototype development, not experiment design; it needs authorization; and it would invalidate the batch-5 fidelity census unless the whole census were re-run on a branch. It also entangles a stimulus problem with a canonical artefact, which is how frozen results get damaged. Worth doing **on its own merits** for the prototype's completeness — but as separate work, not as a precondition for this study |
| **B** | **Generate the candidate pool outside the governed architecture**, as stimulus material, and apply the three governance filters to it | **Correct.** It touches no canonical script, no dataset and no result. The generator is never proposed as a system — it is a source of realistic candidate advice, exactly as a stimulus set in any rating study |

### 5.3 Specification of the external generator

| Property | Requirement |
|---|---|
| **Inputs** | The same environmental record the architecture sees, at the same hours. Nothing the architecture does not have |
| **Must not use** | The safety state `S`; `G(S)`; `A_AI(S)`; the classifier's thresholds; any architecture output. **The generator must be constructible by someone who has never seen the architecture** |
| **Output** | For each case, a candidate advice set drawn from all four types `{Go, Delay, DepartureTime, Duration}`, as text a fisher could act on |
| **Documentation** | Its rule basis published in full alongside the study. A generator a reviewer cannot inspect is a strawman accusation waiting to happen |
| **Candidate designs** | (i) a transparent forecast-exposure heuristic — departure window minimising forecast wind and wave exposure across the working window, duration from forecast persistence; (ii) an expert-authored advice set written by a skipper blind to the architecture; (iii) an LLM-generated advisory conditioned only on the environmental record. **(ii) is the most defensible and the most expensive. (i) is the most reproducible. (iii) is the cheapest and the easiest to attack** |
| **What it is not** | Not a proposed system, not a baseline advisory system, not a competitor. It is stimulus material, and the write-up must say so in those words |

### 5.4 The three arms, once the pool is external

| Arm | Filter applied to the candidate set |
|---|---|
| **C0 ungated** | None. Every candidate type is shown |
| **C1 participation-only** | All four types when `G(S) = 1`; nothing when `G(S) = 0` |
| **C2 graduated** | `A_AI(S)` — FULL in SAFE, `{Go, Delay}` in CAUTION, ∅ in UNSAFE |

Now C1 and C2 **genuinely differ in content**, because the generator produces the types C2 withholds. That is the whole purpose of taking the pool outside the architecture.

### 5.5 The non-degeneracy gate — pre-registered, machine-checkable, needs no authorization

Run the generator over the existing 9,135 departure-window hours and compute, **before any human is contacted**:

| Criterion | Threshold | Why |
|---|---|---|
| **N1 Type coverage** | Each of the four types appears in ≥10% of cases | A generator that produces one type reproduces the degeneracy it was built to escape |
| **N2 Arm content divergence** | C1 and C2 differ in presented content in ≥20% of cases | This is the study's effect channel. Below this, the design has no power regardless of sample size |
| **N3 Withheld-type realisation** | Within CAUTION hours, the generator produces `DepartureTime` or `Duration` in ≥50% of cases | If the withheld types are rarely generated, C2's restriction is again withholding what would not have appeared |
| **N4 Boundary-case availability** | ≥30% of eligible cases qualify as boundary cases per §4.6 | Needed to fill the boundary stratum without reusing cases |

**If any of N1–N4 fails, the study must not proceed to human rating.** Stop, report the failure, and revise the generator — and note that a generator tuned until it passes is a generator tuned to produce the result, so **N1–N4 and the generator design must both be fixed before the gate is run, and the gate run once**.

**RUN 17 Nov 2026 — result: `GATE_PASS_as_preregistered: false`.** N1 **PASS** (Go 69.38%, Delay 30.62%, DepartureTime 36.12%, Duration 72.56%). N2 **FAIL** at 2.69% unstratified — structurally capped by `P(S = CAUTION) = 5.81%`, so the 20% bar was unreachable by construction and was mis-specified here; **46.33% on a CAUTION-stratified pool**. N3 **FAIL** at 46.33% against 50%, leaving **246 usable differing-arm cases**. N4 **FAIL** at 6.17% against 30% — wrong units: 564 boundary cases exist in absolute terms (557 wave, 2 wind, 6 rain), which is ample for a 40-case pilot. **The decisive positive: a non-degenerate candidate pool is achievable at this site.** Full result and respecification in the D-4 report §6.

**This gate is the cheapest decisive step available.** It uses only data already in the repository, needs no ethics approval, no recruitment, no external request and no new collection, and it can **falsify the study's feasibility before anything irreversible is spent**. It is Stage 0 in §7.

---

## 6. Supervisor decision brief

**One page. Five decisions. Four of them cannot be made by the researcher alone.**

### The situation in four sentences

The literature position is defensible but narrower than previously written, and it is bounded by a nine-paper non-systematic sample — both now corrected in the readiness package. The proposed advisory comparison answers **none** of the frozen thesis RQ1–RQ3, so as things stand it would produce evidence with no chapter to live in. It is **not** the struck RQ5 fisher study, and can be distinguished from it on three axes — so the obstacle is a missing slot, not a prohibition. The prototype currently produces **one advice type in 244 of 292 episodes and nothing in the other 48**, so the comparison cannot be run at all until candidate advice is generated outside the governed architecture.

### D-1 · Which RQ set is authoritative? **Decision required — supervisor only**

`final-research-chain-lock.md` and `CLAUDE.md` carry **two incompatible RQ sets, both dated 2026-09-21**. The lock claims authority and its "Not reintroduced" list strikes `CLAUDE.md`'s RQ3 and much of its RQ2, so the lock appears to supersede — but that is an inference, and until it is confirmed every RQ number in a defence is ambiguous. **Cheapest item on this list and the highest embarrassment-per-pound.** Recommended: confirm the lock, and let `CLAUDE.md`'s table be corrected by whoever owns it.

### D-2 · Where does the advisory comparison sit? **Decision required — supervisor, possibly committee**

Three options, costed at §2.4. **S-A** — construct-validity study for RQ2's dependent variable, no new RQ, justified by Journal 1's own conceded limitation at `manuscript.md:1462`. **S-B** — a new RQ4 under supervisory authority, explicitly distinguished from struck RQ5. **S-C** — defer entirely to a post-submission paper. Recommended: **put S-A first, hold S-B in reserve.** S-A is the only option whose justification is already written down in the project's own documents as an acknowledged weakness.

### D-3 · May the external candidate-advice generator be built? **Decision required — authorization**

Without it there is no study (§5.1). It touches no canonical script, dataset or result, and it is stimulus material, not a proposed system. Building it, running the §5.5 non-degeneracy gate over existing data, and reporting the result requires **no ethics approval, no participants and no external request**. Recommended: authorize this and nothing else, then re-decide on the gate's result.

### D-4 · Does the rubric have an independent source? **Decision required — and it may be fatal**

The whole design rests on a safety reference independent of both the architecture and the rater (§4.1). **ANSWERED 17 Nov 2026: no harm-severity reference exists; an independent *hazard* reference does.** See the D-4 report. The decision is now narrower and sharper — not *does a reference exist* but *will the project say "hazard" instead of "severity"*. If no independent source exists for small-vessel harm thresholds at this site, the rubric cannot be made independent by careful wording, and the study collapses into circularity no matter how well the rest is executed. Recommended: **settle this before D-2 is finalised**, because a negative answer makes S-A and S-B both moot and S-C the only option.

### D-5 · Shall METMalaysia be approached? **Decision required — external contact**

For a decision-reconstruction study, the **official local bulletin is arguably the most relevant forecast of all**, and this audit found no retrievable archive of it anywhere (§3.2). Only a direct written enquiry can settle it. **Not submitted, per the authorization boundary.** Note this is only on the critical path for the staleness strand, not for the advisory comparison. Recommended: hold until D-2 resolves.

### What is recommended overall

**Authorize D-3 alone. Settle D-1 and D-4 in parallel, as they cost nothing and can both kill or reshape the design. Do not decide D-2 until the §5.5 gate has produced a number. Leave D-5 until last.** The §5.5 gate is the only step here that can falsify the study's feasibility for the price of a few hours of computation on data already in hand, and no decision that follows it should be made before it.

### Go / Revise / No-Go

**REVISE**, unchanged from the readiness package's verdict, and now for a sharper reason: the study is not blocked by novelty, by feasibility of data, or by prohibition. It is blocked by **a missing thesis slot (D-2), a degenerate stimulus source (D-3) and an unconfirmed independent reference (D-4)** — in that order of resolvability, and the reverse order of severity.

---

## 7. Pilot specification **[PROPOSED — no stage has been executed]**

Staged so that **every authorization-free step comes first**, and each stage can kill the design before the next is paid for.

### Stage 0 — no authorization, no participants, no external request

| | Step | Output | Kill condition |
|---|---|---|---|
| **0a** | Build the external candidate-advice generator per §5.3 | Documented generator + its rule basis | Cannot be specified without reference to `S` or the classifier's thresholds |
| **0b** | Run the §5.5 non-degeneracy gate over the existing 9,135 departure-window hours | N1–N4 statistics, reported whatever they say | **Any of N1–N4 fails** |
| **0c** | Assess candidate independent rubric sources against the §4.4 multi-signal test | Provenance table, one row per threshold, S1–S5 populated | **No source clears the test for the dominant component** — and given `g_o` drives 97.6% of activation, a rubric with no independent wave-severity source fails here |
| **0d** | Draft the pre-registration: hypotheses, arms, rubric, severity anchors, agreement statistic and threshold, N1–N4, stopping rules | Pre-registration document, unsubmitted | — |

**Stage 0 is the whole of what can be done now.** It is also where the design is most likely to die, which is the right place for it to die.

### Stage 1 — minimum human pilot. Requires D-3, D-4 and ethics approval

| | Step | Scale | Purpose |
|---|---|---|---|
| **1a** | Severity-anchor pre-test with the first 2 raters | ~10 cases, discarded from analysis | Do the §4.3 anchors mean the same thing to a working skipper as to the author? Anchors revised **before** any analysed case is scored |
| **1b** | Blinded rating pilot | **~40 cases**, ≥30% boundary, every case in ≥2 arms, 2 raters on 100% | Feasibility, rating time per case, AC1 on real data, whether matched-context blinding actually holds |
| **1c** | Independence audit of the executed pilot | — | Did any rater infer the arm? A rater who can name the arm has broken the blind, and the pilot says so |

**Stage 1 is a feasibility pilot, not a result.** It is not powered for an effect, and no effect estimate from it may be reported as a finding. Its deliverable is *whether the full study can be run*, plus the variance estimate needed to size it.

### Stage 2 — full study. Requires a successful Stage 1 and a resolved D-2

Not specified here, deliberately. Its case count must be sized from Stage 1b's observed severity variance and AC1, not guessed now; and its design must match whichever siting D-2 produces, since S-A and S-B imply different write-ups, different claims and different chapters.

### What the pilot cannot deliver, whatever its result

It cannot establish real-world safety outcomes, fisher behaviour, trust, reliance or adoption — those are struck RQ5's territory and remain future work. It cannot establish that the architecture is safe; it can only establish whether category restriction changes the safety character of advice **as scored by experts against a declared reference**. And it cannot escape the single-site limitation that already bounds RQ2 and RQ3.

---

## 8. Prioritized blockers

| # | Blocker | Severity | Resolvable by | Cost | Status |
|---|---|---|---|---|---|
| **B1** | **ANSWERED 17 Nov 2026 — reframed, not closed.** No *harm-severity* reference exists for this vessel class in these waters; FAO/ILO/IMO 2012 is a verified independent *hazard* reference. The blocker is now a labelling decision (D-4a), not a search. Superseded text: **No independent safety reference confirmed.** The rubric's independence rests on sources none of which has cleared the §4.4 test. `g_o` drives 97.6% of activation, so a wave-severity source is the one that must clear it | **Fatal if unresolved.** Circularity cannot be written around | Researcher (assessment) + supervisor (acceptance) | Days of literature work. **No authorization needed** | **OPEN — Stage 0c** |
| **B2** | **MITIGATED 17 Nov 2026.** The prototype is still degenerate (244 of 292 episodes yield `["Delay"]`, 48 yield `[]`, zero yield the other three types), but an external generator produces **all four types** (N1 PASS) and **246 CAUTION cases with genuinely differing arm content**. Residual: N2/N3/N4 need respecification and one re-run | **Blocking.** The study cannot detect its own effect | Researcher, given D-3 | Build + one gate run on existing data | **OPEN — Stage 0a/0b** |
| **B3** | **No thesis slot.** The study answers none of frozen RQ1–RQ3 and populates no chapter | **Blocking for the thesis**, not for the science | **Supervisor only** (D-2) | One meeting | **OPEN** |
| **B4** | **Two live RQ sets, both dated 2026-09-21.** `final-research-chain-lock.md` vs `CLAUDE.md:47-51` | **High** — ambiguity in a defence | **Supervisor only** (D-1) | Minutes | **OPEN** |
| **B5** | **Novelty claim was unqualified.** Nine-paper non-systematic sample, single reviewer, no protocol | **Was high; now mitigated** by the §1.2 qualification. Residual: converting to a literature-wide claim needs a registered systematic review that is **not costed anywhere** | Researcher, if the stronger claim is wanted | Months | **MITIGATED — declared, not removed** |
| **B6** | **Classification miscount** (8/1 → 7/1/1) | Was moderate — a self-contradicting table invites a reviewer to re-grade the rest | — | — | **CLOSED 17 Nov 2026** (§1.1) |
| **B7** | **Ethics approval** not sought; no participant recruited | **Blocking for Stage 1 only** | Institution | Weeks to months | **OPEN — not started, per the authorization boundary** |
| **B8** | **No issue-time forecast data**, and prospective collection needs 4–6 years for 100 events at this site | **Blocking for the staleness strand only.** Not on the advisory comparison's critical path | Retrospective archive: GEE pairing from 2022-06, or ECMWF MARS for 2020–2025 with no-redistribution terms | Licence decision; no collection yet | **OPEN — audited, not actioned** |
| **B9** | **METMalaysia bulletins appear unarchived.** The most locally relevant forecast of all may be unobtainable | Moderate, staleness strand only | Written enquiry (D-5) | One letter | **OPEN — not submitted** |
| **B10** | **Grid-cell displacement.** At 9–55 km resolution the site may sit offshore of its own sheltered water. Applies to the **existing ERA5-Ocean record too**, not only to new collection | Moderate, and it touches results already published | Researcher — document as a limitation | Days | **OPEN** |
| **B11** | Carried from readiness §7, unchanged: three Journal 1 / publication-sequence inconsistencies; three competing chapter structures; `evaluation-design-rq4.md`'s expected-S circularity; `graduated-advisory-safety-novelty-assessment.md` untracked; **the AAI 2026 manuscript's 7-page overrun against a 6-page limit** | The page overrun is a **live submission defect** | Researcher | Varies | **OPEN** |

**Read in order.** B1 and B2 are the two that can be settled now, without authorization, and either can end the design. B3 and B4 cost one conversation each and must not be left to be discovered at a defence. Everything below B7 is conditional on the strand that §3.0 shows is not on the critical path.

---

## 9. What this package does not establish

1. **No experiment was run, no participant contacted, no external request submitted, no archive queried for data.** Every number from the repository is a re-verification of an existing artefact; §3 is documentation audit only.
2. **The §2.4 sitings are options, not a recommendation with authority.** Only the supervisor can site a result in a thesis, and the preference stated for S-A is a judgement, labelled as one.
3. **The §2.1 reading that the lock supersedes `CLAUDE.md` is an inference** from two documents of the same date. It is coherent, and it is not a settled fact.
4. **The rubric is unvalidated.** Its constructs, severity anchors and agreement thresholds have never been applied to a case. §4.3's anchors in particular are the author's wording, not a tested instrument.
5. **No independent safety reference has been confirmed to exist.** §4.4 specifies the test; it has not been run. This is the most consequential open question in the package, and a negative answer invalidates §4 and §7 entirely.
6. **The generator does not exist.** §5.3 is a specification; §5.5's gate has not been run, so whether a non-degenerate pool is achievable at this site is **unknown**.
7. **The event-rate figures (85–123 events, 17–25/yr, 4–6 years for 100 events) depend on the clustering separation thresholds** of >3 days and >1 day. They are the project's own record and its own CAUTION definition, not a climatological constant, and a different separation rule gives different numbers.
8. **The forecast audit has stated gaps** (§3.6). Open-Meteo marine past-run capability is **unverified**; ECMWF's wave-stream start date is **inferred, not documented**; METMalaysia findings rest on a January 2022 third-party mirror; no claim is made about WeatherBench 2.
9. **Novelty assessments remain judgements about defensibility against a reviewer**, not predictions of acceptance — and after §1.2 they are judgements explicitly bounded by a nine-paper non-systematic sample.
