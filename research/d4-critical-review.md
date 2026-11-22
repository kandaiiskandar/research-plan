# Critical Review of the D-4 Report and the N1–N4 Gate

**Prepared:** 17 November 2026 · **Author of this document:** Claude (Cowork session) · **Status:** adversarial self-review. Three of the four answers below are negative.

**Nothing is overwritten.** Every original criterion, threshold and result from `research/d4-reference-validity-and-non-degeneracy.md` and `research/next-research-decision-package.md` is preserved verbatim in those files and restated here before any revision. Revisions are additive and labelled. Where I am correcting my own error, I say so.

**Authorization boundary observed.** No experiment was run. No frozen artefact was modified. The distribution table in §1.3 is a **read-only descriptive query** over the case table the gate already produced — percentiles of a column that already exists, not a new experiment and not a new result.

**Evidence conventions.** **[VERIFIED]** = read from a primary source or computed from the existing record on 17 Nov 2026. **[CORRECTION]** = an error in my own prior output. **[UNQUANTIFIED]** = a real effect whose size is not known and was not measured here.

---

## 1. Can FAO/ILO/IMO design categories serve as an episode-level hazard reference without a defined vessel design category?

### 1.1 Verdict

**No — and it fails twice, for independent reasons. Without a category assignment the reference is undefined; with any defensible assignment it is degenerate at this site. The second failure is the fatal one, because it cannot be fixed by doing the missing work.**

This retracts the D-4 report's recommendation. FAO/ILO/IMO 2012 remains the best *source* found — independent, free, correctly scoped, verified verbatim. It is not a usable **episode-level reference**, and I conflated those two things.

### 1.2 Failure one — the mapping runs the wrong way, and inverting it needs an input nobody has

FAO clause 1.2.14 is a statement of the form:

> *vessel* → *category* → *the conditions that vessel "is considered suitable to operate in"*

An episode-level hazard reference needs the inverse:

> *conditions at this episode* → *hazard level*

That inversion is only defined once the vessel's category is fixed. **No category has been assigned to the Sabah small-scale fleet, and FAO's categories apply to *new* vessels assessed under that standard** — traditional Malaysian open boats were never assessed under it. So three problems compound:

1. **The assignment is missing**, and the reference is literally undefined without it.
2. **Assigning one is a researcher judgement** — precisely the kind of load-bearing designer decision that an "independent" reference was introduced to avoid. It would reintroduce at the reference what the architecture already concedes at the classifier.
3. **The most natural way to assign it is circular.** The obvious evidence for which category these hulls belong to is their measured operability envelope — which is Yaakob et al., the dependent source. The independence won back in the D-4 report would be lost through the back door.

There is also a defect in the statement itself that no assignment repairs. FAO's lead-in reads **"provided the vessel is correctly operated and is operating at a speed appropriate to the prevailing sea state"** **[VERIFIED verbatim]**. The category is therefore a conditional claim about *vessel plus conduct*, and conduct is unobserved in a five-year reanalysis record. Even fully assigned, FAO says "this hull is suitable here *if handled well*" — it cannot grade the hazard of an episode independently of how the boat was handled.

**One further error of my own. [CORRECTION]** The D-4 report called FAO's four categories "four graded levels" and proposed re-deriving a hazard scale from them. That reads the table along the wrong axis. A/B/C/D are **four classes of vessel capability, not four levels of hazard for one vessel.** The figures 0.30 m, 2 m and 4 m are envelope ceilings for *different boats*. Treating them as an ordinal hazard scale for one fleet is a category error. For a single assigned category, FAO yields **one binary threshold — inside or outside the envelope — not a graded scale.**

### 1.3 Failure two — at this site, every plausible assignment is degenerate **[VERIFIED]**

Read-only percentiles of wave height over the 9,135 departure-window cases already in `research/non-degeneracy/n1-n4-case-table.csv`:

| | Hs |
|---|---|
| minimum | 0.08 m |
| median | 0.54 m |
| p90 | 1.12 m |
| p95 | 1.28 m |
| p99 | 1.62 m |
| **maximum over five years** | **2.06 m** |

Against each candidate boundary:

| Boundary | Cases exceeding | Share |
|---|---|---|
| **FAO D ceiling, 0.30 m** | 7,206 / 9,135 | **78.88%** |
| FAO D "occasional" 0.50 m | 4,960 / 9,135 | 54.30% |
| architecture CAUTION onset 1.00 m | 1,304 / 9,135 | 14.27% |
| architecture UNSAFE 1.25 m | 524 / 9,135 | 5.74% |
| **FAO C ceiling, 2.00 m** | **2 / 9,135** | **0.02%** |
| **FAO B ceiling, 4.00 m** | **0 / 9,135** | **0.00%** |

**The whole site lives inside FAO Category C, with two exceptions in five years.**

- **Assign Category C** — the natural reading for a decked vessel working at sea — and the reference answers "within envelope" for **99.98%** of departure hours. A reference with no variance has no discriminating power, and a scale that never varies is not a scale. Stage A's own no-go rule ("disagreement in <10% of cases") kills it outright.
- **Assign Category B** and it is worse: zero exceedances, a constant.
- **Assign Category D** and it declares the fleet outside its envelope on **79%** of mornings — empirically false, since these boats demonstrably go to sea on most of them. Category D describes sheltered-water craft, which contradicts FAO's own scope wording that these are *"undecked vessels intended to operate at sea"*. Using D's 0.5 m as a graded marker would be taking a number that means "this boat should not be out here at all" and reading it as a hazard band.

Note what the table also shows: **the architecture's own boundaries sit at roughly p90 and p94 of the site's distribution** — inside the range where a reference can actually discriminate. That is not an argument that the architecture's thresholds are correct. It is an argument that FAO's are in the wrong place for this site, and it explains why: FAO's categories were drawn to separate ocean-going hulls from sheltered-water hulls globally, not to grade mornings at one tropical coastal site where Hs never reaches 2.1 m.

### 1.4 What FAO can still legitimately be used for

Not nothing, but much less than claimed:

- **As a declared admissibility bound.** "No departure hour in the five-year record exceeds a Category C envelope" is a true, citable, independently sourced sanity statement about the operating domain. It bounds; it does not grade.
- **As an independence benchmark in the provenance audit** (§3, A1), where its value is that it shares no lineage with Jeong & Im, Yaakob, MET or JPS.
- **As the source of the vessel-scope definition** — its clause 1.1.2 scope wording is the best available published definition of the fleet this project targets, and belongs in the vessel assumptions of §4.

**What it cannot do is anchor K1 or K3.** The hazard-reference route is now closed by evidence, not by lack of searching: there is no harm reference (D-4 report §4), and the best independent hazard reference has no discriminating power here. That is why §4 of this document stops trying to build a reference and builds an **appropriateness** instrument instead.

---

## 2. Temporal information leakage in the external candidate generator

### 2.1 Verdict

**Three distinct leaks, all real, all mine. The generator is anticipative — it sees the future — and the architecture it is being compared against is not. That violates the decision package's own §5.2 information-parity requirement, and it biases the study against the graduated arm.**

### 2.2 The three leaks

| | Leak | Where | What it means |
|---|---|---|---|
| **L1** | **Whole-record distributional look-ahead** | `exposure_index()` computes `d[col].rank(pct=True)` over all 43,848 hours | Advice at 05:00 on 2020-01-01 depends on conditions in 2024. A real pre-departure advisor has only the past |
| **L2** | **Whole-record cutoff look-ahead** | `P_GO` and `P_OK` are `np.percentile(e, …)` over the full record | The Go/Delay boundary itself is set using future data. Compounds L1 |
| **L3** | **Episode-level outcome look-ahead** | `DepartureTime` reads realised exposure at later window hours; `Duration` reads up to **9 realised forward hours** | The generator does not forecast — it *knows*. Its `DepartureTime` is correct by construction, and its `Duration` is a measured outcome dressed as advice |

L3 is the serious one. L1 and L2 are the familiar normalisation leak and would shift the generator's calibration. L3 makes the generator an oracle on exactly the two advice types the comparison turns on.

**One thing that is *not* leakage, stated so it is not confused with the above.** The exposure index uses the same three variables the classifier uses. That is shared causation, not leakage, and information parity *requires* it. Correlation between the generator's index and `S` is expected and harmless.

### 2.3 Why this is not just noise — it has a direction

C2 withholds `DepartureTime` and `Duration` in CAUTION; C1 shows them. Because of L3 those withheld types are **oracle-accurate**. So C1 presents advice that is right by construction, and C2 looks like it is withholding good advice.

**The leak therefore tilts the study toward the conclusion that graduated gating is harmful.** Two consequences follow, and they are not symmetric:

- If a study run on this generator found graduated restriction no better or actively worse, **that finding would be partly an artefact** and could not be reported.
- If it found graduated restriction better *despite* the leak, that would be a conservative result — the leak worked against it. That is the only direction in which the current generator could yield a usable finding, and designing a study that is only interpretable in one direction is poor practice.

### 2.4 The leak also inflates N1 — the one criterion that passed **[UNQUANTIFIED]**

`Duration` appears in **72.56%** of cases and `DepartureTime` in **36.12%**. Both rates are achieved by reading realised future hours. Under a non-anticipative generator both would fall, and the drop is **not estimated here** because estimating it means re-running, which this review does not do.

**So N1's pass must be read as conditional: a non-degenerate pool is achievable *by an anticipative generator*. Whether it is achievable by a causally honest one is open.** The D-4 report stated N1's pass without that qualifier. **[CORRECTION]**

### 2.5 The finding underneath the leak, which matters more than the leak

Trying to remove L3 exposes something structural. Consider what information each advice type needs:

| Type | Information required |
|---|---|
| `Go` | Concurrent conditions — is it acceptable now? |
| `Delay` | Concurrent conditions — is it unacceptable now? |
| `DepartureTime` | **A forecast** — when will it be better? |
| `Duration` | **A forecast** — how long will it stay acceptable? |

**Two of the four admissible advice types are forecast-dependent by their semantics.** The prototype has no forecast input. Therefore it cannot produce them — and that is exactly what the fidelity census shows: 244 of 292 episodes yield `["Delay"]`, 48 yield `[]`, and `R-SAFE-001` sits `DEFERRED`.

**So the prototype's degeneracy is not an implementation oversight. It is a faithful consequence of the architecture's richest admissible set presupposing a forecast capability the system was never given.** This reframes blocker B2: `A_AI(SAFE) = {Go, Delay, DepartureTime, Duration}` is specified over a recommendation space two of whose members are unreachable from the inputs the prototype has. That is worth saying plainly to a supervisor, and it is a more interesting observation than "the rule set is incomplete".

**And it corrects the decision package. [CORRECTION]** Its §3.0 asserted that "the advisory comparison does not need issue-time forecasts" and that the forecast-source audit was "not on the critical path". **That was wrong.** Any non-degenerate, information-parity-respecting candidate generator needs a forecast input — real issue-time forecasts, or an explicitly declared surrogate. Issue-time data moves from "staleness strand only" to **"required for the advisory comparison as well"**, which makes blocker B8 and decision D-5 live again, and raises the cost of the whole design.

### 2.6 Specified remedies — not implemented

| Leak | Remedy | Cost |
|---|---|---|
| **L1, L2** | Compute percentile ranks and cutoffs on an **expanding prior window** (hours strictly before the episode), or fix them from a held-out earlier baseline period and freeze them | Cheap. Loses the first year or so of the record to warm-up |
| **L3** | Replace realised forward hours with a declared forecast surrogate. In increasing order of defensibility: **(a) persistence** — assume current conditions hold, the honest null and free; **(b) degraded persistence** — persistence plus a declared error model; **(c) real issue-time forecasts** from the archives audited in the decision package §3, which costs the licence decision and a collection step | (a) free; (c) expensive and needs authorization |
| **All three** | Alternative: restrict the generator to concurrent information only — but then it can barely produce `DepartureTime` or `Duration`, and **N1 would likely fail** | Free, and probably fatal to the design |

**The tension this exposes is the sharpest finding of this review: information parity and non-degeneracy pull against each other.** A generator honest about what it could know at 05:00 struggles to produce the two advice types that make the arms differ; a generator that produces them freely is cheating. The resolution is (a) or (c) — a declared forecast surrogate — never a silent oracle. Persistence is the right first move: it is free, it is the honest null, and if N1 survives under persistence the design is in much better shape than it is now.

---

## 3. Stage A, revised into three separated layers

**Original Stage A and Stage B are preserved unchanged in the D-4 report §7.** The original conflated three different kinds of validity into one pass/fail, which is the defect being fixed: each layer fails for a different reason and each failure has a different remedy, so a conflated failure is uninterpretable.

| Layer | Question | Needs | Remedy if it fails |
|---|---|---|---|
| **A1 Source independence** | Is the reference's provenance independent of what the architecture already uses? | Documents only | **A different source** |
| **A2 Construct validity** | Does the reference measure what it claims, for this fleet, at this site? | Documents + existing data, no raters | **A different construct** |
| **A3 Statistical agreement** | Can two people apply it consistently? | Raters, ethics approval | **Better anchors** |

Order is deliberate and ordered by cost: A1 and A2 are free and can both kill a candidate before any ethics application.

### A1 — Source independence (documentary; no data, no raters)

| Step | Action |
|---|---|
| A1.1 | Record every threshold's source document, clause and page |
| A1.2 | Apply the five-signal test from the decision package §4.4 — S1 source, S2 citation overlap with the architecture's provenance table, S3 numeric coincidence, S4 variable-set coincidence, S5 derivation order |
| A1.3 | **Lineage audit** — trace each source's own derivation one level back, to catch common-source agreement. This is the step that caught Wolfson ← Jeong & Im |
| A1.4 | Record shared authorship across candidates |

**Go / no-go, unchanged from the original where it applies:** no-go if the provenance test flags the **wave** threshold as architecture-dependent (S2∧S3, or S3∧S4∧S5), since wave drives 97.6% of activation. A flagged wind or rain threshold is a declarable limitation, not a no-go. **Added:** no-go if A1.3 shows the candidate shares a derivation chain with a source the architecture already uses, even when the numbers differ.

*FAO 2012 passes A1.* That was never the problem.

### A2 — Construct validity (documents + existing data; no raters)

This layer is new as a separate stage, and it is where FAO dies.

| Step | Check | Go / no-go |
|---|---|---|
| **A2.1** | **Referent form.** Is the reference a statement about *conditions*, or about *vessel plus conduct*? | **No-go** if it cannot be evaluated from observed conditions alone. *FAO fails: its lead-in conditions every category on correct operation and speed* |
| **A2.2** | **Vessel-class definition.** Is the vessel class the reference requires actually defined and defensibly assigned, from evidence independent of the architecture? | **No-go** if the assignment is missing, or if assigning it requires a source the architecture already uses. *FAO fails: no assignment exists, and the natural route is Yaakob* |
| **A2.3** | **Discriminating power.** What share of the 9,135 cases fall on each side of each boundary? | **No-go** if any boundary splits the record more extremely than **95 / 5**. *FAO Category C fails at 99.98 / 0.02; Category B at 100 / 0* |
| **A2.4** | **Non-redundancy with `S`.** Cramér's V and rank-disagreement share against the architecture's state | **No-go** if V ≥ 0.90 or disagreement < 10% (**original criteria, retained**) |
| **A2.5** | **Convergent / divergent behaviour.** Does the reference track the component it claims to measure (wave) more strongly than components it should not (time-of-day, rainfall)? | **No-go** if it tracks `g_t` as strongly as `g_o` — that would mean it is measuring daylight, not sea state |

**A2.3 is the cheapest decisive check in the whole programme and it was missing from the original Stage A.** It costs one query against a table that already exists, and it would have rejected FAO before anything else was written. It is now the first thing any future candidate reference faces. **[CORRECTION]**

### A3 — Statistical agreement (raters; ethics approval required; not initiated)

Original Stage B is preserved; these are additions.

| | Specification |
|---|---|
| Scale | 2 raters, 20 cases — 10 boundary drawn from the 176 CAUTION-boundary cases, 10 non-boundary |
| Primary statistic | **Gwet's AC1**, for the prevalence-skew reason already given; report Krippendorff's ordinal α alongside |
| **Added: intra-rater reliability** | 5 of the 20 cases repeated, unmarked, later in the sequence. Test–retest agreement is reported separately. An instrument a single rater cannot reproduce against themselves cannot be fixed by adding raters |
| Blind integrity | Each rater states any selection rule they think the cases followed. Recovering the classifier's thresholds is a **result**, not a nuisance |
| **Added: information-parity audit** | Every case's materials are checked to contain **only decision-time information**. Any case whose materials reveal post-decision conditions is void. This is §2's leak guard at the instrument level |

**Go / no-go:** GO at AC1 ≥ 0.70 with the blind intact; REVISE at 0.50–0.70 (rewrite anchors, re-run once); NO-GO below 0.50, or if either rater recovers the thresholds, or if test–retest falls below the inter-rater figure.

---

## 4. Minimum viable advice-appropriateness rubric **[PROPOSED — not run, no recruitment]**

### 4.1 Why the construct changed, and what it costs

The reference route is closed: no harm reference exists (D-4 §4), and the best independent hazard reference has no power here (§1). **Appropriateness** is the construct that remains available, and it is honest because it does not pretend to a reference it does not have.

**What it is.** Whether the advice was appropriate to the conditions **as knowable at decision time**, judged by domain experts against a declared vessel.

**What it costs, stated first so it is not discovered later.** The reference becomes the expert panel. So the study can support:

> *"Category restriction produces advice that experienced practitioners judge more appropriate to the conditions."*

and it cannot support:

> *"Category restriction produces safer outcomes."*

That ceiling is intrinsic, not a limitation of this design. Agreement among experts is not safety, and Kim et al. is the standing warning: radiologist accuracy was **lowest** where the AI was most confident, which expert agreement alone would never have revealed. **Say the ceiling in the abstract, not the limitations section.**

### 4.2 Explicit vessel assumptions — stated because §1 proved that leaving them implicit breaks the instrument

Every rater sees this profile, verbatim and identically, before scoring. Each line is marked **[S]** sourced or **[D]** researcher-declared.

| Attribute | Assumption | |
|---|---|---|
| Length | 5–12 m LOA | **[S]** FAO 2012 cl. 1.1.2 scope; Yaakob's hulls are 5.03 and 6.54 m |
| Tonnage | < 10 GRT | **[S]** Yunus (2007) via Yaakob Table 1 |
| Construction | Open or partly decked, wooden or GRP | **[S]** Yaakob |
| Propulsion | Single outboard, **no redundancy** | **[D]** |
| Dominant failure mode | **Swamping before capsize** — low freeboard, manual bailing only | **[D]** — and load-bearing, since it is what makes short steep seas matter more than Hs alone |
| Trip pattern | Day trip, departs 05:00–09:00, returns same day | **[S]** the canonical departure window |
| Navigation equipment | No radar, no AIS; mobile coverage near shore only | **[D]** |
| Crew | 1–3; lifejacket use variable; no immersion suits | **[D]** |
| Operating area | Coastal, partly sheltered by the Tunku Abdul Rahman islands | **[D]** |
| Site sea state | Hs median 0.54 m, p95 1.28 m, five-year max 2.06 m | **[S]** **[VERIFIED]** §1.3 |
| **Design category** | **None assigned. Deliberately left undefined** | **[D]** — §1.2 shows that assigning one is either missing evidence or circular. The rubric must not need it |

**The last row is the design constraint.** A rubric that cannot be scored without a design category inherits FAO's failure. This one is scored against the profile and the conditions, never against a category.

### 4.3 The instrument — three items, nothing more

| | Item | Scale | Why it is in a minimum viable set |
|---|---|---|---|
| **R1** | **Conservatism match.** Given the conditions and the vessel profile, was this advice appropriately cautious? | **−2** far too permissive · **−1** somewhat too permissive · **0** appropriate · **+1** somewhat over-restrictive · **+2** far too restrictive | **The core item — it alone answers the study's question.** Signed, because over- and under-restriction are different errors and a single unsigned "quality" score hides which one occurred. An architecture that only ever over-restricts is failing in a specific way worth naming |
| **R2** | **Specificity support.** The advice claims a degree of knowledge. Was that claim supportable from what could be known at decision time? | **0** not supportable · **1** partly · **2** supportable | **The leak guard made visible.** A `DepartureTime` asserts knowledge of a future hour. If the generator is anticipative, R2 should expose it: raters who cannot see how 07:00 was knowable will score 0. R2 is therefore also a live check on §2 |
| **R3** | **Actionability.** Could a fisher with this vessel act on this advice as given? | **0** no · **1** partly · **2** yes | Captures the usefulness side of the trade-off. Without it the study can only show restriction is safe, never what it costs — and the cost is the whole reason gating is interesting |

**Plus one unscored free-text field: "What would you have advised?"** Cheap, and it supplies the unaided-expert comparator that is the only element of Kim et al.'s design transferable here without a harm reference.

**Not included, deliberately:** any harm or severity item (no reference exists); admissibility (machine-checkable, and showing it to a rater reveals the arm); any merged "overall quality" score (it would hide the R1/R3 trade-off, which is the finding).

### 4.4 Go / no-go criteria, pre-registered

| | Criterion | Rationale |
|---|---|---|
| **NO-GO** | Any rater reports having imagined a vessel materially different from the §4.2 profile | The profile is the reference. If raters substitute their own boat, they are scoring different instruments |
| **NO-GO** | **R1 = 0 in ≥ 80% of cases** | A rubric that calls everything appropriate cannot discriminate between arms. This is §1's A2.3 lesson applied to the instrument itself |
| **NO-GO** | Any case's materials contain post-decision conditions | Information-parity violation; voids the case and, if systematic, the run |
| **NO-GO** | AC1 < 0.50 on R1 collapsed to three levels (too permissive / appropriate / too restrictive) | Below this the instrument is not reproducible |
| **REVISE** | AC1 0.50–0.70 on collapsed R1 | Anchors ambiguous; rewrite and re-run once |
| **GO** | AC1 ≥ 0.70 on collapsed R1, **and** R1 non-degenerate, **and** the blind intact, **and** R2 scores distinguish anticipative from persistence-based advice | Report the five-level AC1 as well, and expect it lower |
| **Diagnostic, not a gate** | R2 scoring 0–1 on most `DepartureTime` advice | Would confirm §2's leak from the raters' side — valuable either way, so it must not be a pass condition |

**One pre-registration that protects the study from its own result.** R1's sign must be reported as a distribution, never as a mean. A mean R1 near zero can arise from genuine appropriateness or from offsetting over- and under-restriction, and those are opposite findings. **[VERIFIED]** The same logic that makes a mean illegitimate on the ordinal severity scale applies here.

---

## 5. Change ledger — what this review alters, with originals preserved

| | Original claim | Status after this review |
|---|---|---|
| D-4 §1 and §9: FAO/ILO/IMO 2012 is the recommended independent reference; relabel K1/K3 as a hazard scale | **RETRACTED as an episode-level reference** (§1). FAO remains a valid *source* and a valid *admissibility bound* and *scope definition*. The hazard-reference route is closed |
| D-4 §4.3 / decision package §4.3: a graded scale re-derived from FAO's four levels | **RETRACTED** (§1.2). A/B/C/D are vessel classes, not hazard levels. One assigned category yields a binary, not a scale |
| D-4 §6.4: "N1 passes decisively — a non-degenerate pool is achievable at this site" | **QUALIFIED** (§2.4). True for an *anticipative* generator. Unknown for a causally honest one. **[UNQUANTIFIED]** |
| Decision package §3.0: issue-time forecasts are not on the advisory comparison's critical path | **WRONG** (§2.5). Two of the four advice types are forecast-dependent by semantics. B8 and D-5 are live for this strand too |
| Decision package §5.1 / B2: the prototype's degeneracy is an incomplete rule set | **REFRAMED** (§2.5). It is a faithful consequence of `A_AI(SAFE)` ranging over types unreachable from the prototype's inputs |
| D-4 §7 Stage A / Stage B | **PRESERVED unchanged**, and superseded for future use by the three-layer A1 / A2 / A3 in §3. A2.3 (discriminating power) is new and is now the first gate |
| N1–N4 numbers and thresholds | **PRESERVED verbatim.** No number is restated differently anywhere in this document |
| The rubric's four constructs K1–K4 and the 5-point severity scale | **PRESERVED in place, SUPERSEDED in use** by the three-item appropriateness rubric in §4. K2 and K4 survive in substance as the admissibility exclusion and R3 |

---

## 6. Uncertainties

1. **The §1.3 degeneracy finding is specific to this site and this five-year record.** A site with Hs reaching 3–4 m would put FAO's Category C boundary inside its distribution and the objection would not apply.
2. **The leak's effect on N1 is [UNQUANTIFIED].** Whether a persistence-based generator passes N1 is the single most important open empirical question, and answering it needs one re-run that was not performed here.
3. **Whether R2 can actually detect anticipative advice is untested.** It is a plausible mechanism, not a validated one, and it is listed as a diagnostic rather than a gate for that reason.
4. **The appropriateness construct's ceiling may be judged insufficient for a thesis contribution.** That is a supervisor judgement, not a methodological fact, and it should be put to them explicitly rather than assumed either way.
5. **The §4.2 profile contains seven researcher-declared rows.** Each is a point a reviewer can contest, and the swamping-failure-mode row is load-bearing.
6. **Nothing here was checked against the RESOLUTION (MFWAM) configuration.** All figures are PRIMARY.
7. **A1.3's lineage audit was run informally, one level back.** A deeper trace could find further common sources among the candidates.

---

## 7. Next supervisor decisions, revised

| | Decision | Who | Cost | Recommendation |
|---|---|---|---|---|
| **D-4a′** | **Supersedes D-4a.** Accept that **no usable external reference exists** — not harm, and not hazard either — and that the study's construct becomes **advice appropriateness judged by experts**, with the ceiling in §4.1 stated in the abstract | Supervisor | One meeting | **Accept, and state the ceiling up front.** The honest claim is narrower than "safer advice" and it is defensible; the wider one is not available at any price this project can pay |
| **D-3″** | **Re-run the gate once under a persistence-based, non-anticipative generator** (remedies L1–L3, option (a)), publishing the anticipative and persistence results side by side | Author | Hours | **Proceed.** This is the decisive open question and it is cheap. If N1 survives persistence, the design is sound; if not, the forecast-input problem is the blocker, not the rule set |
| **D-5′** | **Reinstated.** Decide the forecast-input route for the generator — persistence surrogate, declared error model, or real issue-time archives from the decision package §3 | Supervisor | Varies | **Start with persistence.** Escalate to real forecasts only if persistence fails N1, since that is where the licence cost and the collection step live |
| **D-4b′** | Run A1 and **A2** for any future candidate reference, with **A2.3 first** | Author | Minutes per candidate | **Proceed.** One query would have saved the FAO recommendation from being made |
| **D-4f** | Record in Appendix C that `A_AI(SAFE)` ranges over two advice types unreachable from the prototype's inputs | Author | Minutes | **Record it.** It is a specification observation, not a defect, and it is better stated by the author than found by an examiner |
| **D-4d** | Unchanged: request Wu, Pelot & Hilliard (2009) by interlibrary loan | Author | One request | **Request it.** Still the only source that could overturn the TYPE A void |

**What I would do first.** D-3″, because it is cheap, it answers the question everything else depends on, and the current N1 pass cannot be reported as it stands. D-4a′ next, because the construct has to be settled before an ethics application can describe what the study measures.

**One honest summary of where this leaves the programme.** Three of this review's four answers are negative, and the design is in better shape for it: the reference search is over and can stop consuming effort, the construct is now one the available evidence can actually support, and the generator's defect was found before a single participant was approached rather than after.
